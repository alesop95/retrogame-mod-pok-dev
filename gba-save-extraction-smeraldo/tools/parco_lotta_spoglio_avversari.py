#!/usr/bin/env python3
"""Spoglia le due tabelle indipendenti degli avversari del Parco Lotta, le confronta l'una contro l'altra, e ne ricava le distribuzioni contro cui una squadra si progetta.

Perche' esiste
--------------

Il Parco Lotta non estrae i propri avversari da una popolazione libera ma da un catalogo chiuso di insiemi, dove ogni insieme e' una specie con una natura, uno strumento, quattro mosse e una distribuzione di punti base gia' decisi. Progettare una squadra contro un'idea di avversario e' quindi un lavoro inutile quando il catalogo si puo' leggere: si progetta contro il catalogo, cioe' contro le specie che ricorrono davvero, gli strumenti che si incontrano davvero e le mosse di stato che si subiscono davvero.

Il catalogo esiste in due copie indipendenti, ed e' la ragione per cui questo strumento confronta invece di limitarsi a leggere. La prima e' il database dello strumento `DomeAssistantWeb`, che lo porta come sorgente JavaScript perche' gli serve per simulare il Cupola Lotta. La seconda e' il foglio `EmeraldBattleFrontierComplete`, pubblicato su Smogon, che porta in piu' le abilita' possibili, le statistiche gia' calcolate a livello 100 e a livello 50, e i punti individuali fissi dei soli Assi. Due copie della stessa tabella, fatte da persone diverse, valgono molto piu' di una sola: dove concordano, il dato e' fermo; dove divergono, c'e' esattamente un punto da guardare invece di ottocentottantadue.

Il confronto non e' decorativo. Le due copie non hanno nemmeno lo stesso numero di voci, e la differenza non e' un errore di nessuna delle due ma un fatto sulla natura del catalogo che solo il confronto rende visibile.

Che cosa produce
----------------

Sotto la cartella di uscita scrive sei file. `avversari.json` e' il catalogo unito, cioe' ogni insieme con i campi su cui le due fonti concordano piu' le colonne che solo il foglio porta; `assi.json` sono le squadre dei sette Assi nelle due comparse, d'argento e d'oro, che il database dello strumento non ha affatto; `formazioni-smogon.json` sono le formazioni dei trecento allenatori con la loro classe, che il database non porta; `bacini-per-sfida.json` dice quali insiemi il gioco puo' davvero pescare a ciascun numero di sfida; `distribuzioni.json` sono i conteggi per specie, strumento, natura, abilita' e mossa calcolati su quei bacini e non sul catalogo intero; e `SPOGLIO.md` e' la lettura di Livello 1 di tutto cio', cioe' il documento che si apre invece di rilanciare lo strumento.

Il confronto fra le due fonti finisce in `divergenze.json` e nella sezione corrispondente del documento, con una riga per ogni campo che diverge. Una divergenza non viene mai risolta in silenzio scegliendo una fonte: viene elencata, perche' chi la legge sa cose che lo strumento non sa.

I bacini per numero di sfida, e perche' contano piu' della media
----------------------------------------------------------------

Una media calcolata su tutti gli insiemi del catalogo descrive un avversario che non si incontra mai, perche' il gioco non pesca uniformemente e non pesca nemmeno dal catalogo. Pesca in due stadi: prima un allenatore, dentro un intervallo di identificativi che dipende dal numero di sfida gia' vinta, e poi gli esemplari di quell'allenatore dentro la sua formazione, che e' una lista chiusa. L'unita' di conteggio giusta e' quindi l'unione delle formazioni degli allenatori raggiungibili a una data sfida, ed e' cio' che questo strumento calcola.

Le tabelle degli intervalli non sono un'ipotesi ma una lettura del sorgente, e la loro provenienza puntuale sta nei commenti accanto alle costanti in testa al file. Una prima versione di questo strumento usava invece le fasce di indice dedotte da una nota del foglio Smogon sugli insiemi di Noland: erano plausibili e non erano il meccanismo, e la differenza si vede subito, perche' il meccanismo vero mostra un salto di difficolta' alla settima lotta di ogni serie che nessuna fascia di indice avrebbe fatto emergere.

Uso
---

    python gba-save-extraction-smeraldo/tools/parco_lotta_spoglio_avversari.py --domeassistant _notes/fonti/raccolte/domeassistant-2026-09-21/grezzo --smogon _notes/fonti/raccolte/smogon-maxstats-2026-09-21/EmeraldBattleFrontierComplete.txt --out _notes/fonti/raccolte/parco-lotta-spoglio-2026-09-21
"""

import argparse
import collections
import json
import re
from pathlib import Path

# Gli intervalli di identificativo dell'allenatore da cui il gioco pesca, per numero di sfida gia' vinta,
# verificati su `pret/pokeemerald`, `src/battle_tower.c`, tabelle `sFrontierTrainerIdRanges` e
# `sFrontierTrainerIdRangesHard`. Il numero di sfida e' la serie di vittorie divisa per sette; la settima
# lotta di ogni serie pesca dalla tabella dura, le prime sei da quella ordinaria; dalla sfida otto in poi
# entrambe le tabelle coincidono con l'ultima riga.
INTERVALLI_ALLENATORE = [
    (0, (0, 99), (100, 119)),
    (1, (80, 119), (120, 139)),
    (2, (100, 139), (140, 159)),
    (3, (120, 159), (160, 179)),
    (4, (140, 179), (180, 199)),
    (5, (160, 199), (200, 219)),
    (6, (180, 219), (220, 239)),
    (7, (200, 299), (200, 299)),
]

# I punti individuali che il gioco fissa su ogni statistica dell'avversario, per identificativo di allenatore,
# da `GetFrontierTrainerFixedIvs` nello stesso file. Non sono casuali: sono lo stesso valore su tutte e sei.
IV_FISSI_PER_ALLENATORE = [
    (99, 3), (119, 6), (139, 9), (159, 12), (179, 15), (199, 18), (219, 21), (299, 31),
]

# A livello 50 il gioco scarta gli insiemi oltre questa soglia, che compaiono quindi solo a Livello Aperto.
# Da `FRONTIER_MONS_HIGH_TIER` in `include/constants/battle_frontier_mons.h`, con il confronto stretto
# `monId > FRONTIER_MONS_HIGH_TIER` in `src/battle_tower.c` e in `src/battle_factory.c`.
INSIEME_ALTO_LIVELLO = 849

# Le mosse che non infliggono danno e che cambiano il modo in cui si progetta una squadra,
# raggruppate per cio' che fanno subire invece che per tipo.
CATEGORIE_STATO = {
    "sonno": {"Spore", "Sleep Powder", "Hypnosis", "Sing", "Lovely Kiss", "Grass Whistle", "Yawn"},
    "paralisi": {"Thunder Wave", "Stun Spore", "Glare"},
    "confusione": {"Confuse Ray", "Supersonic", "Sweet Kiss", "Swagger", "Teeter Dance"},
    "veleno": {"Toxic", "Poison Powder", "Poison Gas"},
    "elusione": {"Double Team", "Minimize"},
    "un-colpo": {"Fissure", "Horn Drill", "Guillotine", "Sheer Cold"},
    "intrappolamento": {"Mean Look", "Spider Web", "Block"},
    "recupero": {"Rest", "Recover", "Softboiled", "Milk Drink", "Moonlight", "Morning Sun", "Synthesis", "Slack Off", "Swallow"},
    "protezione": {"Protect", "Detect", "Endure"},
}


# ---------------------------------------------------------------------------
# Lettura del database di DomeAssistantWeb, che e' sorgente JavaScript e non JSON
# ---------------------------------------------------------------------------

def _oggetto_javascript(testo, nome):
    """Estrae il letterale che segue `const <nome> =` e lo riduce a JSON.

    Il file non e' JSON: le chiavi interne sono identificatori nudi, ci sono commenti sia di riga sia di blocco, questi ultimi anche in mezzo a una chiave, e in coda c'e' un punto e virgola. La riduzione percorre il testo carattere per carattere tenendo conto dello stato di stringa, invece di applicare espressioni regolari sul testo intero: una chiave nuda dentro una stringa non esiste in questi file, ma la differenza fra il non averla incontrata e il non poterla incontrare vale il tokenizzatore.
    """
    inizio = testo.index("const " + nome)
    inizio = testo.index("=", inizio) + 1
    fuori = []
    i, n = inizio, len(testo)
    profondita = 0
    avviato = False
    while i < n:
        c = testo[i]
        if c in "\"'":
            chiusura = c
            j = i + 1
            while j < n and testo[j] != chiusura:
                if testo[j] == "\\":
                    j += 1
                j += 1
            fuori.append('"' + testo[i + 1:j].replace('"', '\\"') + '"')
            i = j + 1
            continue
        if c == "/" and i + 1 < n and testo[i + 1] == "/":
            while i < n and testo[i] != "\n":
                i += 1
            continue
        if c == "/" and i + 1 < n and testo[i + 1] == "*":
            fine = testo.find("*/", i + 2)
            i = n if fine < 0 else fine + 2
            continue
        if c in "{[":
            profondita += 1
            avviato = True
        elif c in "}]":
            profondita -= 1
        fuori.append(c)
        i += 1
        if avviato and profondita == 0:
            break
    grezzo = "".join(fuori)
    grezzo = re.sub(r'([{,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2":', grezzo)
    grezzo = re.sub(r",(\s*[}\]])", r"\1", grezzo)
    return json.loads(grezzo)


def leggi_domeassistant(cartella):
    cartella = Path(cartella)

    def carica(nome_file, nome_const):
        return _oggetto_javascript(cartella.joinpath(nome_file).read_text(encoding="utf-8"), nome_const)

    return {
        "insiemi": carica("frontierPokemon.js", "frontierPokemon"),
        "formazioni": carica("rosters.js", "rosters"),
        "allenatori": carica("trainers.js", "trainers"),
        "specie": carica("pokemon.js", "pokemon"),
        "mosse": carica("moves.js", "moves"),
        "nature": carica("natures.js", "natures"),
    }


# ---------------------------------------------------------------------------
# Lettura del foglio Smogon, che e' testo a colonne con un difetto di separatori
# ---------------------------------------------------------------------------

_PUNTI_BASE = re.compile(r"(\d+)\s*/\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)\s*$")


def _separa_abilita_e_punti(campi_centrali):
    """Restituisce (abilita, punti base) da uno o due campi.

    Il foglio, esportato in testo, perde il separatore fra la colonna delle abilita' e quella dei punti base in poco meno della meta' delle righe, e il caso si riconosce dal numero di colonne. Non e' un difetto del contenuto ma della conversione, e va sanato qui invece che a mano: sanarlo a mano significherebbe riscrivere quattrocento righe della fonte, cioe' rendere la fonte non piu' confrontabile con se stessa.
    """
    if len(campi_centrali) == 2:
        return campi_centrali[0], campi_centrali[1]
    unito = campi_centrali[0]
    trovato = _PUNTI_BASE.search(unito)
    if not trovato:
        return unito, ""
    return unito[:trovato.start()].strip(), trovato.group(0)


def _punti_base(testo):
    trovato = _PUNTI_BASE.search(testo.strip())
    if not trovato:
        return None
    etichette = ["hp", "atk", "def", "spa", "spd", "spe"]
    return {e: int(trovato.group(i + 1)) for i, e in enumerate(etichette)}


def _statistiche(testo):
    parti = [p.strip() for p in testo.split("/")]
    if len(parti) != 6 or not all(p.isdigit() for p in parti):
        return None
    etichette = ["hp", "atk", "def", "spa", "spd", "spe"]
    return {e: int(parti[i]) for i, e in enumerate(etichette)}


def _mosse(campi):
    return [c for c in campi if c and c != "---"]


def leggi_smogon(percorso):
    """Legge le tre tabelle del foglio: gli insiemi numerati, le squadre degli Assi, e le formazioni degli allenatori.

    Le tre si riconoscono da come comincia la riga, non da un conteggio di righe fissato a mano, perche' un conteggio fissato si rompe in silenzio alla prima riga aggiunta alla fonte.
    """
    righe = Path(percorso).read_text(encoding="utf-16").split("\n")
    insiemi, assi, formazioni, note = [], [], [], []
    for riga in righe:
        nuda = riga.strip()
        if not nuda:
            continue
        campi = [c.strip() for c in nuda.split("|")]
        testa = campi[0]
        if testa.startswith(("*", "†")):
            note.append(nuda)
            continue
        if testa in ("Entry", "Name"):
            continue
        if testa.isdigit() and len(campi) >= 14:
            abilita, punti = _separa_abilita_e_punti(campi[9:-5])
            insiemi.append({
                "indice": int(testa),
                "specie": campi[1],
                "istanza": int(campi[2]) if campi[2].isdigit() else None,
                "natura": campi[3],
                "strumento": campi[4],
                "mosse": _mosse(campi[5:9]),
                "abilita": [a.strip() for a in abilita.split("/") if a.strip()],
                "punti_base": _punti_base(punti),
                "statistiche_lv100": _statistiche(campi[-5]),
                "statistiche_lv50": _statistiche(campi[-3]),
                "iv_fissi": int(campi[-1]) if campi[-1].isdigit() else None,
            })
            continue
        if re.match(r"^[A-Z][a-z]+ (Silver|Gold)", testa.replace("†", "").strip()) and len(campi) >= 13:
            abilita, punti = _separa_abilita_e_punti(campi[8:-5])
            asso, comparsa = testa.replace("†", "").strip().rsplit(" ", 1)
            assi.append({
                "asso": asso,
                "comparsa": "argento" if comparsa == "Silver" else "oro",
                "specie": campi[1],
                "natura": campi[2],
                "strumento": campi[3],
                "mosse": _mosse(campi[4:8]),
                "abilita": [a.strip() for a in abilita.split("/") if a.strip()],
                "punti_base": _punti_base(punti),
                "statistiche_lv100": _statistiche(campi[-5]),
                "statistiche_lv50": _statistiche(campi[-3]),
                "iv_fissi": int(campi[-1]) if campi[-1].isdigit() else None,
            })
            continue
        if len(campi) > 3 and campi[1] and not campi[1].isdigit():
            formazioni.append({"allenatore": testa, "classe": campi[1], "insiemi": [c for c in campi[2:] if c]})
    return {"insiemi": insiemi, "assi": assi, "formazioni": formazioni, "note": note}


# ---------------------------------------------------------------------------
# Confronto
# ---------------------------------------------------------------------------

# Le due fonti scrivono diversamente le sole due specie il cui nome porta un simbolo di sesso.
# La differenza e' di grafia e non di contenuto, e va normalizzata prima del confronto: lasciarla
# produrrebbe due false divergenze che coprirebbero di rumore quelle vere.
ALIAS_SPECIE = {"Nidoran♀": "NidoranF", "Nidoran♂": "NidoranM"}


def _chiave(specie, istanza):
    return "%s %s" % (ALIAS_SPECIE.get(specie, specie), istanza)


def confronta(dome, smogon):
    """Confronta insieme per insieme le due copie del catalogo e restituisce l'elenco delle divergenze.

    Il confronto avviene sulla coppia specie-istanza e non sull'indice, perche' l'indice e' una convenzione di ciascuna fonte mentre la coppia e' un fatto del gioco. Se anche le due fonti numerassero diversamente, il confronto reggerebbe.
    """
    da_dome = dome["insiemi"]
    da_smogon = {_chiave(s["specie"], s["istanza"]): s for s in smogon["insiemi"]}
    divergenze = []
    solo_dome = sorted(set(da_dome) - set(da_smogon))
    solo_smogon = sorted(set(da_smogon) - set(da_dome))
    for nome in sorted(set(da_dome) & set(da_smogon)):
        a, b = da_dome[nome], da_smogon[nome]
        if a["nature"] != b["natura"]:
            divergenze.append({"insieme": nome, "campo": "natura", "domeassistant": a["nature"], "smogon": b["natura"]})
        if a["item"] != b["strumento"]:
            divergenze.append({"insieme": nome, "campo": "strumento", "domeassistant": a["item"], "smogon": b["strumento"]})
        if list(a["moves"]) != list(b["mosse"]):
            divergenze.append({"insieme": nome, "campo": "mosse", "domeassistant": a["moves"], "smogon": b["mosse"]})
        if b["punti_base"] and a["evs"] != b["punti_base"]:
            divergenze.append({"insieme": nome, "campo": "punti_base", "domeassistant": a["evs"], "smogon": b["punti_base"]})
    return {"solo_domeassistant": solo_dome, "solo_smogon": solo_smogon, "divergenze": divergenze}


def unisci(dome, smogon):
    da_smogon = {_chiave(s["specie"], s["istanza"]): s for s in smogon["insiemi"]}
    uniti = {}
    for nome, a in dome["insiemi"].items():
        b = da_smogon.get(nome, {})
        specie = dome["specie"].get(a["species"], {})
        uniti[nome] = {
            "indice_domeassistant": a["index"],
            "indice_smogon": b.get("indice"),
            "specie": a["species"],
            "istanza": a["instance"],
            "tipi": [t for t in (specie.get("type1"), specie.get("type2")) if t],
            "natura": a["nature"],
            "strumento": a["item"],
            "mosse": a["moves"],
            "punti_base": a["evs"],
            "abilita": b.get("abilita", []),
            "statistiche_lv50": b.get("statistiche_lv50"),
            "statistiche_lv100": b.get("statistiche_lv100"),
            "iv_fissi": b.get("iv_fissi"),
        }
    return uniti


# ---------------------------------------------------------------------------
# Distribuzioni
# ---------------------------------------------------------------------------

def _iv_fissi(id_allenatore):
    for soglia, valore in IV_FISSI_PER_ALLENATORE:
        if id_allenatore <= soglia:
            return valore
    return IV_FISSI_PER_ALLENATORE[-1][1]


def insiemi_per_sfida(dome, solo_livello_50=True):
    """Restituisce, per ogni numero di sfida, l'insieme degli indici che il gioco puo' davvero pescare.

    E' la differenza fra progettare contro il catalogo e progettare contro cio' che si incontra. Il gioco non pesca uniformemente fra gli ottocentottantadue insiemi: pesca un allenatore dentro un intervallo che dipende dal numero di serie gia' vinte, e quell'allenatore pesca a sua volta dentro la propria formazione, che e' una lista chiusa. Ne segue che una statistica calcolata sull'intero catalogo descrive un avversario che non si incontra mai, e che l'unita' di conteggio giusta e' l'unione delle formazioni degli allenatori raggiungibili a una data sfida.

    La settima lotta di ogni serie merita una colonna propria e non una media con le altre sei, perche' pesca da una tabella diversa e piu' dura: e' il punto in cui una serie si perde, e progettare sulla media delle sette lo nasconde.
    """
    per_indice = {}
    for nome, voce in dome["allenatori"].items():
        per_indice[voce["index"]] = voce
    uscita = []
    for sfida, ordinario, duro in INTERVALLI_ALLENATORE:
        righe = {}
        for etichetta, (primo, ultimo) in (("lotte 1-6", ordinario), ("lotta 7", duro)):
            nomi = set()
            iv = set()
            for id_allenatore in range(primo, ultimo + 1):
                voce = per_indice.get(id_allenatore)
                if voce is None:
                    continue
                iv.add(_iv_fissi(id_allenatore))
                nomi.update(dome["formazioni"][voce["roster"]])
            righe[etichetta] = {
                "allenatori": [primo, ultimo],
                "iv_fissi": sorted(iv),
                "insiemi": sorted(nomi),
            }
        uscita.append({"sfida": sfida, "serie": [sfida * 7 + 1, sfida * 7 + 7], "tabelle": righe})
    return uscita


def distribuzioni(uniti, per_sfida, solo_livello_50=True):
    """Conta specie, strumenti, nature, abilita' e mosse dentro ciascun bacino di sfida.

    Il filtro di livello 50 non si applica ai conteggi come una nota a margine ma come un taglio: a quel livello il gioco scarta gli insiemi oltre la soglia alta, e contarli significherebbe progettare contro trentadue avversari che non si presenteranno.
    """
    uscita = {}
    for blocco in per_sfida:
        for etichetta, riga in blocco["tabelle"].items():
            chiave = "sfida-%d %s" % (blocco["sfida"], etichetta)
            specie = collections.Counter()
            strumento = collections.Counter()
            natura = collections.Counter()
            abilita = collections.Counter()
            mossa = collections.Counter()
            stato = collections.Counter()
            velocita = []
            conteggio = 0
            for nome in riga["insiemi"]:
                voce = uniti.get(nome)
                if voce is None:
                    continue
                if solo_livello_50 and voce["indice_domeassistant"] > INSIEME_ALTO_LIVELLO:
                    continue
                conteggio += 1
                specie[voce["specie"]] += 1
                strumento[voce["strumento"]] += 1
                natura[voce["natura"]] += 1
                for ab in voce["abilita"]:
                    abilita[ab] += 1
                for m in voce["mosse"]:
                    mossa[m] += 1
                    for categoria, elenco in CATEGORIE_STATO.items():
                        if m in elenco:
                            stato[categoria] += 1
                if voce["statistiche_lv50"]:
                    velocita.append(voce["statistiche_lv50"]["spe"])
            velocita.sort()
            uscita[chiave] = {
                "sfida": blocco["sfida"],
                "serie": blocco["serie"],
                "tabella": etichetta,
                "allenatori": riga["allenatori"],
                "iv_fissi": riga["iv_fissi"],
                "insiemi": conteggio,
                "specie_piu_frequenti": specie.most_common(25),
                "strumenti": strumento.most_common(15),
                "nature": natura.most_common(10),
                "abilita_piu_frequenti": abilita.most_common(15),
                "mosse_piu_frequenti": mossa.most_common(25),
                "mosse_di_stato_per_categoria": sorted(stato.items(), key=lambda v: -v[1]),
                "velocita_lv50": {
                    "conteggio": len(velocita),
                    "minima": velocita[0] if velocita else None,
                    "mediana": velocita[len(velocita) // 2] if velocita else None,
                    "novantesimo": velocita[int(len(velocita) * 0.9)] if velocita else None,
                    "massima": velocita[-1] if velocita else None,
                },
            }
    return uscita


# ---------------------------------------------------------------------------
# Documento di Livello 1
# ---------------------------------------------------------------------------

def scrivi_documento(percorso, confronto, uniti, dist, smogon):
    r = []
    r.append("# Spoglio del catalogo degli avversari del Parco Lotta")
    r.append("")
    r.append("> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_spoglio_avversari.py`. Non si modifica a mano: si rigenera. La lettura in profondita' sta in `gba-save-extraction-smeraldo/STUDIO-04-parco-lotta-simboli-oro.md`, che e' autorato; questo file e' derivato e serve a non dover rilanciare lo strumento per ricordare un numero.")
    r.append("")
    r.append("## Il confronto fra le due copie del catalogo")
    r.append("")
    r.append("Insiemi nel database di DomeAssistantWeb: %d. Insiemi numerati nel foglio Smogon: %d." % (len(uniti), len(smogon["insiemi"])))
    r.append("")
    r.append("Presenti solo in DomeAssistantWeb: %d%s" % (len(confronto["solo_domeassistant"]), (", cioe' " + ", ".join(confronto["solo_domeassistant"])) if confronto["solo_domeassistant"] else "."))
    r.append("")
    r.append("Presenti solo nel foglio Smogon: %d%s" % (len(confronto["solo_smogon"]), (", cioe' " + ", ".join(confronto["solo_smogon"])) if confronto["solo_smogon"] else "."))
    r.append("")
    r.append("Divergenze sui campi condivisi: %d." % len(confronto["divergenze"]))
    r.append("")
    if confronto["divergenze"]:
        r.append("| Insieme | Campo | DomeAssistantWeb | Foglio Smogon |")
        r.append("|---|---|---|---|")
        for d in confronto["divergenze"][:200]:
            r.append("| %s | %s | %s | %s |" % (d["insieme"], d["campo"], json.dumps(d["domeassistant"], ensure_ascii=False), json.dumps(d["smogon"], ensure_ascii=False)))
        r.append("")
    r.append("Note che il foglio porta in calce alle proprie tabelle, riportate verbatim perche' sono affermazioni della fonte e non conclusioni di questo strumento:")
    r.append("")
    for n in smogon["note"]:
        r.append("- %s" % n)
    r.append("")
    r.append("## I bacini da cui il gioco pesca, per numero di sfida")
    r.append("")
    r.append("Il numero di sfida e' la serie di vittorie divisa per sette. Le prime sei lotte di ogni serie pescano l'allenatore dalla tabella ordinaria, la settima da quella dura, e dalla sfida otto in poi entrambe coincidono con l'ultima riga: da li' in avanti il bacino non cresce piu'. I punti individuali sono fissati dall'identificativo dell'allenatore e valgono uguali su tutte e sei le statistiche. I conteggi escludono gli insiemi oltre l'indice %d, che a livello 50 il gioco non pesca." % INSIEME_ALTO_LIVELLO)
    r.append("")
    r.append("| Sfida | Serie | Tabella | Allenatori | Punti individuali | Insiemi pescabili a Lv50 |")
    r.append("|---|---|---|---|---|---|")
    for chiave in sorted(dist, key=lambda k: (dist[k]["sfida"], dist[k]["tabella"])):
        d = dist[chiave]
        r.append("| %d | %d-%d | %s | %d-%d | %s | %d |" % (
            d["sfida"], d["serie"][0], d["serie"][1], d["tabella"],
            d["allenatori"][0], d["allenatori"][1],
            "-".join(str(v) for v in d["iv_fissi"]), d["insiemi"]))
    r.append("")
    for chiave in sorted(dist, key=lambda k: (dist[k]["sfida"], dist[k]["tabella"])):
        d = dist[chiave]
        r.append("## Sfida %d, %s, %d insiemi pescabili" % (d["sfida"], d["tabella"], d["insiemi"]))
        r.append("")
        r.append("Allenatori da %d a %d, punti individuali %s su ogni statistica. Velocita' a livello 50 sugli insiemi di cui il foglio porta le statistiche (%d): minima %s, mediana %s, novantesimo percentile %s, massima %s." % (
            d["allenatori"][0], d["allenatori"][1], "-".join(str(v) for v in d["iv_fissi"]),
            d["velocita_lv50"]["conteggio"], d["velocita_lv50"]["minima"], d["velocita_lv50"]["mediana"], d["velocita_lv50"]["novantesimo"], d["velocita_lv50"]["massima"]))
        r.append("")
        r.append("Specie piu' frequenti: " + ", ".join("%s (%d)" % v for v in d["specie_piu_frequenti"]) + ".")
        r.append("")
        r.append("Strumenti piu' frequenti: " + ", ".join("%s (%d)" % v for v in d["strumenti"]) + ".")
        r.append("")
        r.append("Mosse piu' frequenti: " + ", ".join("%s (%d)" % v for v in d["mosse_piu_frequenti"]) + ".")
        r.append("")
        r.append("Mosse di stato per categoria: " + (", ".join("%s (%d)" % v for v in d["mosse_di_stato_per_categoria"]) or "nessuna") + ".")
        r.append("")
        r.append("Abilita' piu' frequenti: " + ", ".join("%s (%d)" % v for v in d["abilita_piu_frequenti"]) + ".")
        r.append("")
    Path(percorso).write_text("\n".join(r) + "\n", encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--domeassistant", required=True)
    p.add_argument("--smogon", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    dome = leggi_domeassistant(args.domeassistant)
    smogon = leggi_smogon(args.smogon)

    assert len(dome["insiemi"]) > 800, "database di DomeAssistantWeb letto solo in parte: %d insiemi" % len(dome["insiemi"])
    assert len(smogon["insiemi"]) > 800, "foglio Smogon letto solo in parte: %d insiemi" % len(smogon["insiemi"])
    assert len(smogon["assi"]) == 42, "gli Assi devono essere sette per due comparse per tre esemplari, letti %d" % len(smogon["assi"])

    confronto = confronta(dome, smogon)
    uniti = unisci(dome, smogon)
    per_sfida = insiemi_per_sfida(dome)
    dist = distribuzioni(uniti, per_sfida)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    out.joinpath("avversari.json").write_text(json.dumps(uniti, ensure_ascii=False, indent=1), encoding="utf-8")
    out.joinpath("assi.json").write_text(json.dumps(smogon["assi"], ensure_ascii=False, indent=1), encoding="utf-8")
    out.joinpath("divergenze.json").write_text(json.dumps(confronto, ensure_ascii=False, indent=1), encoding="utf-8")
    out.joinpath("distribuzioni.json").write_text(json.dumps(dist, ensure_ascii=False, indent=1), encoding="utf-8")
    out.joinpath("bacini-per-sfida.json").write_text(json.dumps(per_sfida, ensure_ascii=False, indent=1), encoding="utf-8")
    out.joinpath("formazioni-smogon.json").write_text(json.dumps(smogon["formazioni"], ensure_ascii=False, indent=1), encoding="utf-8")
    scrivi_documento(out.joinpath("SPOGLIO.md"), confronto, uniti, dist, smogon)

    print("insiemi DomeAssistantWeb: %d" % len(uniti))
    print("insiemi foglio Smogon:    %d" % len(smogon["insiemi"]))
    print("squadre degli Assi:       %d esemplari" % len(smogon["assi"]))
    print("formazioni di allenatore: %d" % len(smogon["formazioni"]))
    print("solo in DomeAssistantWeb: %d" % len(confronto["solo_domeassistant"]))
    print("solo nel foglio Smogon:   %d" % len(confronto["solo_smogon"]))
    print("divergenze sui campi:     %d" % len(confronto["divergenze"]))
    print("uscita in %s" % out)


if __name__ == "__main__":
    main()
