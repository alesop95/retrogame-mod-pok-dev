"""Il controllo complessivo di ciò che deve passare da Bank prima della chiusura, su ciò che è davvero in HOME.

Perché esiste. Il 2026-11-25, con l'ultima cartuccia in HOME (giro 16, 7892), il proprietario ha chiesto un controllo
completo di tutto ciò che va chiuso come lotto prima che Bank chiuda il 2027-02-26, perché dopo non si potrà più. Le
misure c'erano, ma sparse in strumenti diversi e su giudizi vecchi. Questo strumento le rifà tutte sullo stesso giudizio,
contando i soli esemplari passati a HOME (`tools/in_home.py`), e scrive un documento solo che dice che cosa manca.

Che cosa misura, e da dove.
1. Caselle di specie e forma, sfide di Bank, fiocchi e sfere persi con Bank: lancia `copertura-lotti.py`,
   `sfide-bank.py` e `fiocchi-e-sfere-prima-di-bank.py` e ne riporta il riepilogo.
2. Eventi della libreria fino alla settima generazione: `pkhex-produci-elenco --carte` sulle copie in HOME; ogni gruppo
   scoperto si cerca nei rapporti dei lotti, per dire se è stato prodotto ed è in HOME sotto una carta gemella.
3. Varianti d'allenatore dei doni di terza generazione dei Pokémon Center giapponesi e di New York (ADR-118):
   `pkhex-produci-elenco --varianti-gen3`, con i nomi validi della libreria.
4. Eventi dell'Eventdex di Serebii dell'epoca di Bank (copia del 2026-11-04) per specie, allenatore e ID, con una sonda
   che distingue le differenze di trascrizione dalle mancanze vere.
5. Sfide dell'app di HOME che si chiudono con Pokémon dell'epoca del 3DS: contatori letti dalle schermate del proprietario
   (`pokedex-home-completo/data/sfide-home-app-20261125.json`).

Uso:
    python tools/controllo-prima-di-bank.py            riepilogo
    python tools/controllo-prima-di-bank.py --scrivi   scrive anche pokedex-home-completo/CONTROLLO-PRIMA-DI-BANK.md
"""
import argparse
import collections
import glob
import json
import os
import subprocess
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import in_home  # noqa: E402

RADICE = in_home.RADICE
LAVORO = os.path.join(RADICE, "_notes", "lavoro", "controllo-prima-di-bank")
ESEGUIBILE = os.path.join(RADICE, "tools", "pkhex-produci-elenco", "bin", "Release", "net10.0", "pkhex-produci-elenco.exe")
EVENTDEX = os.path.join(RADICE, "_notes", "fonti", "raccolte", "serebii-eventdex-2026-11-04", "serebii-eventdex-eventi.json")
SFIDE_APP = os.path.join(RADICE, "pokedex-home-completo", "data", "sfide-home-app-20261125.json")
# le sfide della scheda «Trades», registrate per la prima volta il 2026-11-26
SFIDE_SCAMBI = os.path.join(RADICE, "pokedex-home-completo", "data", "sfide-home-scambi-20261126.json")
# Il lotto delle sfide prodotto da tools/pkhex-sfide-app, privato: se c'è, il giro 17 conta i suoi esemplari, che sono meno
# delle mancanze perché un esemplare conta per tutte le sfide che soddisfa.
LOTTO_SFIDE = os.path.join(RADICE, "_notes", "lotti", "lotto-sfide-app", "rapporto.json")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "CONTROLLO-PRIMA-DI-BANK.md")
GIOCHI_BANK = ("Ruby", "Sapphire", "Emerald", "FireRed", "LeafGreen", "Colosseum", "XD", "Diamond", "Pearl", "Platinum",
               "HeartGold", "SoulSilver", "Black", "White", "X", "Y", "OmegaRuby", "AlphaSapphire", "Sun", "Moon", "Ultra",
               "Ranger", "Battle Revolution")


# Gli eventi che la sonda non ritrova e che si sono verificati a mano, con l'esito (2026-11-25).
_WCS14 = ("in HOME con allenatore WCS14K e ID 07054, HOME3 box 23: Serebii scrive WCSK14 07064 per tutti e sei i doni coreani "
          "del WCS 2014, la libreria (carte di sesta generazione) ne ha tre con 07064 e tre con 07054, e gli esemplari sono conformi")
VERIFICATI_A_MANO = {(127, "WCSK14"): _WCS14, (248, "WCSK14"): _WCS14, (310, "WCSK14"): _WCS14}


def riepilogo(strumento):
    r = subprocess.run([sys.executable, os.path.join(RADICE, "tools", strumento)], capture_output=True, text=True,
                       encoding="utf-8", cwd=RADICE)
    if r.returncode != 0:
        raise SystemExit("%s fallito: %s" % (strumento, r.stderr[-500:]))
    return [r for r in r.stdout.splitlines() if r.strip() and not r.startswith((" ", "[nascosta]", "Register", "Deposit"))]


def misura_libreria(copie):
    os.makedirs(LAVORO, exist_ok=True)
    carte = os.path.join(LAVORO, "carte.json")
    varianti = os.path.join(LAVORO, "varianti-gen3.json")
    vcarte = os.path.join(LAVORO, "varianti-carte.json")
    for modo, uscita in (("--carte", carte), ("--varianti-gen3", varianti), ("--varianti-carte", vcarte)):
        r = subprocess.run([ESEGUIBILE, modo, uscita] + copie, capture_output=True, text=True, encoding="utf-8")
        if r.returncode != 0:
            raise SystemExit("pkhex-produci-elenco %s fallito: %s" % (modo, r.stdout[-500:] + r.stderr[-500:]))
    return [json.load(open(x, encoding="utf-8")) for x in (carte, varianti, vcarte)]


def gemelli(scoperti, esemplari):
    """Per ogni gruppo scoperto dalla libreria: epoca Game Boy, prodotto e in HOME, prodotto e non in HOME, mai prodotto."""
    pid_home = {x["pid"] for _, x in esemplari}
    prodotti = collections.defaultdict(list)
    for r in glob.glob(os.path.join(RADICE, "_notes", "lotti", "*", "rapporto.json")):
        try:
            d = json.load(open(r, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for v in (d.get("voci") or d.get("esiti") or []) if isinstance(d, dict) else []:
            if isinstance(v, dict) and v.get("gruppo") and v.get("pid"):
                prodotti[v["gruppo"]].append(v["pid"])
    esito = []
    for v in scoperti:
        k = v["gruppo"]
        if "GBEra" in k:
            stato = "epoca Game Boy"
        elif any(p in pid_home for p in prodotti.get(k, [])):
            stato = "in HOME sotto una carta gemella"
        elif prodotti.get(k):
            stato = "prodotto, non in HOME"
        else:
            stato = "mai prodotto"
        esito.append((stato, v))
    return esito


def norma(s):
    return unicodedata.normalize("NFKC", str(s)).casefold().replace(" ", "").replace("－", "ー").replace("-", "ー")


def serebii(esemplari):
    """Ogni evento dell'Eventdex dell'epoca di Bank contro gli esemplari in HOME, variante d'allenatore per variante."""
    ev = json.load(open(EVENTDEX, encoding="utf-8"))
    per_specie = collections.defaultdict(list)
    for _, x in esemplari:
        per_specie[x["numero"]].append(x)

    def varianti(x):
        ot, i = x.get("ot", ""), x.get("id", "")
        ots = ot if isinstance(ot, list) else [ot]
        ids = i if isinstance(i, list) else [i] * len(ots)
        return list(zip(ots, ids))

    def stesso_ot(e, ot):
        o, a = norma(ot), norma(e["allenatore"])
        # «Yours» e «Player» sono l'allenatore di chi riceve; i nomi lunghi in HOME sono troncati al limite del gioco
        return o in ("", "??", "?") or "player" in o or "your" in o or a == o or (len(a) >= 5 and o.startswith(a))

    def stesso_id(e, t):
        t = str(t)
        if t in ("", "??", "?") or "-" in t or "your" in t.lower() or "player" in t.lower():
            return True
        try:
            return int(e["id"]) in (int(t), int(t[-5:]), int(t[-6:]))
        except ValueError:
            return True

    conto = collections.Counter()
    trascrizione, parziali = [], []
    tutti = [x for _, x in esemplari]
    for x in ev:
        if not any(g in x.get("giochi", "") for g in GIOCHI_BANK):
            conto["fuori dall'epoca di Bank"] += 1
            continue
        cand = per_specie.get(x["numero"], [])
        vs = varianti(x)
        presenti = [v for v in vs if any(stesso_ot(e, v[0]) and stesso_id(e, v[1]) for e in cand)]
        if len(presenti) == len(vs):
            conto["in HOME"] += 1
        elif presenti:
            conto["in HOME, non tutte le varianti d'allenatore"] += 1
            parziali.append((x, [v for v in vs if v not in presenti]))
        else:
            ot, t = vs[0]
            if any(stesso_ot(e, ot) for e in cand):
                spiega = "stessa specie e allenatore, ID diverso da quello trascritto"
            elif any(stesso_id(e, t) and str(t).strip("0") for e in cand):
                spiega = "stessa specie e ID, allenatore scritto in un'altra lingua o grafia"
            elif any(stesso_ot(e, ot) and stesso_id(e, t) for e in tutti):
                spiega = "stesso allenatore e ID su un'altra specie: evoluzione per scambio o voce sulla forma evoluta"
            elif (x["numero"], str(ot)) in VERIFICATI_A_MANO:
                spiega = VERIFICATI_A_MANO[(x["numero"], str(ot))]
            else:
                spiega = "DA VERIFICARE a mano"
            conto["in HOME con una differenza di trascrizione" if spiega != "DA VERIFICARE a mano" else "da verificare"] += 1
            trascrizione.append((x, spiega))
    return conto, trascrizione, parziali


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scrivi", action="store_true")
    a = p.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    giudizio = json.load(open(in_home.GIUDIZIO_CORRENTE, encoding="utf-8"))["copie"]
    esemplari = in_home.esemplari_in_home(giudizio)
    copie = [c["copia"] for c in giudizio if c["gruppo"] in in_home.GRUPPI_IN_HOME]
    gruppi = sorted(in_home.GRUPPI_IN_HOME)

    misure = {t: riepilogo(t) for t in ("copertura-lotti.py", "sfide-bank.py", "fiocchi-e-sfere-prima-di-bank.py", "elenco-produzione.py")}
    carte, var3, vcar = misura_libreria(copie)
    gem = gemelli(carte["voci"], esemplari)
    conto_gem = collections.Counter(s for s, _ in gem)
    conto_s, trascr, parz = serebii(esemplari)
    mancanti3 = [v for v in var3["voci"] if v["esito"] != "gia' in una copia"]
    per_dist = collections.Counter("%s %s" % (v["tipo"], v["distribuzione"]) for v in mancanti3)
    app = json.load(open(SFIDE_APP, encoding="utf-8"))
    ditto = sum(1 for _, x in esemplari if x["numero"] == 132)
    sfere = collections.Counter(x["sfera"] for _, x in esemplari)
    righe_app = []
    for s in app["sfide"]:
        oggi = s["app"] if s["app"] is not None else ditto
        servono = max(0, s["soglia"] - oggi)
        nelle_copie = sfere.get(s["sfera"]) if "sfera" in s else (ditto if s.get("specie") == 132 else None)
        righe_app.append((s, oggi, servono, nelle_copie))
    servono_app = sum(r[2] for r in righe_app)
    prodotti_app = json.load(open(LOTTO_SFIDE, encoding="utf-8"))["prodotti"] if os.path.exists(LOTTO_SFIDE) else None
    # il lotto delle sfide conta solo finché l'app dice che mancano esemplari: dopo il giro 17 sono tutte d'oro
    esemplari_app = (prodotti_app or servono_app) if servono_app else 0
    scambi = json.load(open(SFIDE_SCAMBI, encoding="utf-8")) if os.path.exists(SFIDE_SCAMBI) else None

    print("esemplari in HOME dai giudizi: %d in %d gruppi" % (len(esemplari), len(gruppi)))
    for t, r in misure.items():
        print("%s: %s" % (t, " | ".join(r[:3])))
    print("eventi della libreria: %d gruppi, coperti %d, scoperti %d: %s" % (
        carte["eventi"], carte["gruppi_coperti"], carte["gruppi_scoperti"], dict(conto_gem)))
    print("varianti d'allenatore di terza generazione: %d combinazioni, presenti %d, mancanti %d" % (
        var3["combinazioni"], var3["presenti"], len(mancanti3)))
    print("varianti d'allenatore delle carte dalla quarta alla settima generazione: %d su %d carte, presenti %d, mancanti %d" % (
        vcar["varianti"], vcar["carte"], vcar["presenti"], vcar["mancanti"]))
    print("Eventdex di Serebii: %s" % dict(conto_s))
    print("sfide dell'app chiudibili con l'epoca del 3DS: %d esemplari da aggiungere" % servono_app)

    if not a.scrivi:
        return
    lotto = len(mancanti3) + esemplari_app
    r = ["# Controllo prima della chiusura di Bank: che cosa è in HOME e che cosa deve ancora passare", "",
         "> Documento generato da `tools/controllo-prima-di-bank.py --scrivi`. Non si modifica a mano: si rigenera dopo ogni giro. Conta i soli esemplari passati a HOME, letti dal giudizio `%s` attraverso `tools/in_home.py`: %d esemplari in %d gruppi (%s). Il totale dell'app, 8557 il 2026-11-26 dopo il giro 17, comprende anche i 34 che erano in HOME prima del giro 1 e quelli arrivati da GO, che i giudizi non leggono, e i 996 vecchi da liberare, che hanno un sostituto identico salvo la data." % (os.path.basename(in_home.GIUDIZIO_CORRENTE), len(esemplari), len(gruppi), ", ".join(gruppi)), "",
         "## Il verdetto", "",
         (("Prima del 2027-02-26 deve passare da Bank un altro giro con %d esemplari: %d varianti d'allenatore dei doni di terza generazione dei Pokémon Center giapponesi e di New York che ADR-118 vuole tutte, %d varianti d'allenatore delle carte dalla quarta alla settima generazione e %d esemplari che chiudono le sfide dell'app di HOME raggiungibili con i giochi del 3DS." % (lotto + vcar["mancanti"], len(mancanti3), vcar["mancanti"], esemplari_app))
          if lotto + vcar["mancanti"] else
          "Tutte le misure di questo documento sono complete sugli esemplari in HOME: caselle di specie e forma, sfide di Bank, fiocchi e sfere, eventi della libreria contati sia per carta sia per allenatore e ID, varianti di terza generazione, Eventdex di Serebii e sfide della scheda Pokémon dell'app.") +
         " Restano fuori dalle misure, e sono scritte sotto: le sfide della scheda «Trades» dell'app, registrate il 2026-11-26 e non ancora misurate contro HOME; la ridatazione dei 1964 esemplari di terza e quarta generazione già in HOME con la data del 2026 (ADR-128), che il proprietario ha rimandato il 2026-11-26 alla fine, se avanza tempo (ADR-143), e che dopo la chiusura non si potrà più fare. Una misura vede soltanto ciò per cui è scritta: il 2026-11-25 le varianti di terza generazione erano sfuggite a ogni misura che contava per carta, e il 2026-11-26 si è aggiunta quella per allenatore e ID delle generazioni successive.", "",
         "## Le misure complete", "",
         "| Misura | Esito | Strumento |", "|---|---|---|"]
    for t, righe in misure.items():
        r.append("| %s | %s | `tools/%s` |" % ({"copertura-lotti.py": "Caselle di specie e forma fino alla settima generazione",
                                                 "sfide-bank.py": "Sfide di HOME che dipendono da Bank",
                                                 "fiocchi-e-sfere-prima-di-bank.py": "Sfere e fiocchi che si perdono con Bank",
                                                 # dal 2026-11-26: le voci degli assi del foglio «Bank Closing all possible things checklist» (ADR-108-111)
                                                 "elenco-produzione.py": "Voci del foglio comunitario «Bank Closing» per origine, scambi, sesso e forma, livelli minimi, stelle"}[t],
                                                "; ".join(x.strip() for x in righe[:1 if t == "elenco-produzione.py" else 3]).replace("|", "/") +
                                                ("; delle 4 voci rimaste, il Mew in Cura Ball non esiste (ADR-116); Electivire al livello 15 e Magmortar al 14 di quarta generazione restano aperte perché nessun Electabuzz o Magmar di quarta generazione arriva a quei livelli nella libreria (ADR-116); la voce dell'anziano di Batikopoli in X e Y, troncata nel foglio («requests that you give him a Pokémon for him to take»), non nomina un incontro che il generatore possa costruire; le 50 mosse sono quelle che sul 3DS non si imparano e vanno alla fase Switch (`ELENCO-PRODUZIONE.md`)" if t == "elenco-produzione.py" else ""), t))
    r.append("| Eventi che la libreria PKHeX conosce fino alla settima generazione | %d gruppi, %d riconosciuti negli esemplari in HOME; dei %d scoperti, %d sono in HOME sotto una carta gemella con dati identici, %d sono doni dell'epoca Game Boy, %d prodotti e non in HOME, %d mai prodotti | `pkhex-produci-elenco --carte` |" % (
        len(set(v["gruppo"] for v in carte["voci"])) + carte["gruppi_coperti"], carte["gruppi_coperti"], carte["gruppi_scoperti"],
        conto_gem["in HOME sotto una carta gemella"], conto_gem["epoca Game Boy"], conto_gem["prodotto, non in HOME"], conto_gem["mai prodotto"]))
    r.append("| Varianti d'allenatore e ID delle carte dalla quarta alla settima generazione (ADR-045, ADR-118) | %d varianti su %d carte, %d con più varianti: presenti %d, mancanti %d | `pkhex-produci-elenco --varianti-carte` |" % (
        vcar["varianti"], vcar["carte"], vcar["carte_con_piu_varianti"], vcar["presenti"], vcar["mancanti"]))
    r.append("| Eventi dell'Eventdex di Serebii dell'epoca di Bank | %s | questo strumento |" % "; ".join("%s %d" % (k, n) for k, n in conto_s.most_common()))
    r += ["", "I doni dell'epoca Game Boy non passano da Bank per costruzione: esistono solo su cartuccia e il Trasportatore non li riceve, e vanno sulle cartucce dopo la sostituzione della pila (ADR-117).", ""]
    resto = [(s, v) for s, v in gem if s in ("prodotto, non in HOME", "mai prodotto")]
    if resto:
        r += ["Gruppi della libreria prodotti e non in HOME, o mai prodotti:", ""]
        r += ["- %s: %s." % (v["descrizione"], s) for s, v in resto]
        r += ["", "Lo Skitty dell'uovo del PokéPark (allenatore ポケパーク, ID 50318, con Rollout) è in HOME, HOME1 box 6 posto 10, dal lotto degli eventi di terza generazione: la libreria lo attribuisce a una voce gemella della stessa tabella, quindi la sua voce risulta scoperta ma l'esemplare c'è.", ""]
    r += ["## Le varianti d'allenatore di terza generazione, da produrre", "",
          "La libreria conosce %d doni dei Pokémon Center giapponesi («Gotta Catch 'Em All», 2005-2006) e del Pokémon Center di New York (2003-2005), con %d combinazioni di dono e nome d'allenatore valido: in Giappone il nome è la città del negozio (Sapporo esclusa dalla sesta distribuzione), a New York la macchina, PCNYb, PCNYc o PCNYd secondo la settimana (`Distribution3JPN.cs`, `Distribution3NY.cs`; PCNYa non è mai esistito). Le copie ne avevano %d, perché la libreria genera questi doni con un nome solo. ADR-118 vuole tutte le varianti che differiscono per allenatore: ne mancano %d, elencate una per riga in `_notes/lavoro/controllo-prima-di-bank/varianti-gen3.json`." % (var3["doni"], var3["combinazioni"], var3["presenti"], len(mancanti3)), "",
          "| Distribuzione | Varianti mancanti |", "|---|---|"]
    r += ["| %s | %d |" % (k, n) for k, n in sorted(per_dist.items())]
    r += ["", "## Le sfide dell'app di HOME che si chiudono con i giochi del 3DS", "",
          "I contatori dell'app coincidono con gli esemplari delle copie in HOME nella stessa sfera: l'app conta anche i Pokémon arrivati da Bank, un deposito per esemplare. Le sfide sotto si chiudono quindi con esemplari prodotti nei giochi dalla quarta alla settima generazione e portati con il giro 17. Fonte dei contatori: le schermate del proprietario del 2026-11-25; soglie da Bulbapedia, «Challenge (HOME)».", "",
          "| Sfida | Nell'app | Nelle copie in HOME | Soglia d'oro | Da aggiungere |", "|---|---|---|---|---|"]
    for s, oggi, servono, nc in righe_app:
        r.append("| %s | %d%s | %s | %d | %d |" % (s["sfida"], oggi, " (stima dalla barra)" if s.get("stima") else "", "" if nc is None else nc, s["soglia"], servono))
    r += ["", "Totale delle mancanze: %d. Un esemplare conta per tutte le sfide che soddisfa, quindi `tools/pkhex-sfide-app` mette i Ditto e gli esemplari con le condizioni al massimo dentro le sfere che hanno ancora un bisogno, e dà a dieci esemplari tutte e cinque le condizioni e la lucentezza a 255, che chiudono insieme le sei sfide di gara. La lucentezza si accumula soltanto con i Pokémelle di terza generazione e i Poffin di quarta (`ContestStatInfo.GetContestStatRestriction` della libreria), quindi quei dieci sono catture di Smeraldo; la sfida della lucentezza è aperta per il proprietario (2026-11-26) e il contatore, non fotografato, si prende a zero.%s" % (servono_app, "" if prodotti_app is None else " Il lotto prodotto ne contiene %d." % prodotti_app), "",
          "Si chiudono solo su Switch, e restano alla fase Switch: " + "; ".join(app["solo_switch"]) + ".", "",
          "## Eventi di Serebii con una differenza di trascrizione", "",
          "Il confronto per specie, allenatore e ID manca %d eventi; la sonda li ritrova tutti in HOME con una differenza nella trascrizione di Serebii, salvo quelli segnati da verificare." % len(trascr), "",
          "| Specie | Evento | Allenatore e ID di Serebii | Esito |", "|---|---|---|---|"]
    for x, spiega in trascr:
        r.append("| %s %s | %s | %s %s | %s |" % (x["numero"], x["specie"], x["evento"].replace("|", "/"), x["ot"], x["id"], spiega))
    r += ["", "## Eventi di Serebii con più nomi d'allenatore", "",
          "%d eventi hanno in HOME solo una parte dei nomi che Serebii elenca. Per la terza generazione le varianti vere sono quelle della libreria, contate sopra: Serebii elenca anche PCNYa, che non è mai esistito, e Sapporo nella sesta distribuzione. Per le generazioni successive la misura per allenatore e ID delle carte della libreria, qui sopra, dice se manca una variante vera; i nomi che seguono non sono carte della libreria, ma grafie di Serebii di carte che in HOME ci sono (per esempio «ふめやすみ» per la carta «ふゆやすみ» 12270, «ETE2012» per «ÉTÉ2012», «Sunset» e «Moonset» per «Eclipse» 100419). Fino al 2026-11-26 questa frase diceva che ADR-045 conta un nome tradotto come un allenatore solo: era sbagliata, perché ADR-118 vuole tutte le varianti che differiscono per allenatore o per ID." % len(parz), ""]
    altri = [(x, m) for x, m in parz if "Gotta Catch" not in x["evento"] and "Pkmn Centre NY" not in x["evento"]]
    r += ["- %s %s, %s: mancano %s." % (x["numero"], x["specie"], x["evento"], ", ".join("%s %s" % v for v in m)) for x, m in altri]
    if scambi:
        r += ["", "## Le sfide degli scambi dell'app, da misurare", "",
              scambi["nota"], "",
              "| Sfida | Soglie | Stato il %s |" % scambi["data"], "|---|---|---|"]
        r += ["| %s | %s | %s |" % (c["sfida"], "/".join(str(x) for x in c["soglie"]) if c["soglie"] else "una volta", c["stato"]) for c in scambi["contatori"]]
        r += ["", "Coppie con entrambe le metà nei giochi del 3DS (%d): %s." % (len(scambi["coppie_entrambe_3ds"]), "; ".join(scambi["coppie_entrambe_3ds"])),
              "", "Coppie con una sola metà nei giochi del 3DS (%d), l'altra su Switch: %s." % (len(scambi["coppie_una_meta_3ds"]), "; ".join("%s (con %s)" % (c["3ds"], c["switch"]) for c in scambi["coppie_una_meta_3ds"])),
              "", "Coppie della sola Switch (%d): %s." % (len(scambi["coppie_solo_switch"]), "; ".join(scambi["coppie_solo_switch"]))]
    r += ["", "## Che cosa resta fuori da Bank, per scelta o perché non esiste fino al 3DS", "",
          "Gli eventi di Scarlatto e Violetto, che il proprietario non ha, si recuperano scambiando con la comunità dopo la chiusura di Bank, a cominciare dal Dragapult con il marchio dell'Imbattibile; le sfide della sola Switch qui sopra; le forme e i fiocchi che si prendono solo giocando su Switch (`COPERTURA-LOTTI.md`, `FIOCCHI-PRIMA-DI-BANK.md`). La loro sorte è in `pending.md`, nelle voci da ricordare sempre.", ""]
    with open(USCITA, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(r) + "\n")
    print("scritto", USCITA)


if __name__ == "__main__":
    main()
