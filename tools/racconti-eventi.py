#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unisce e verifica i racconti in inglese degli eventi del catalogo vivente di HOME (ADR-138).

I racconti li scrivono agenti economici, a lotti, sui soli dati che il progetto ha per ogni carta
(`_notes/lavoro/collezione/eventi-da-raccontare.json`, con la storia del pedigree e le righe di Serebii). Un agente
economico aggiunge a volte un fatto che i dati non portano: il 2026-11-23 un Zekrom distribuito in America diventava
«in America and Europe». Per questo nessun racconto entra nel catalogo senza passare il controllo di questo strumento:
ogni nome proprio, mese, anno e numero del racconto deve comparire nei dati d'ingresso della sua carta. Un racconto che
non passa si sostituisce con una frase composta qui dai campi, senza modello, che non può dire più dei dati.

Uso
---
    python tools/racconti-eventi.py prepara     # ingresso e lotti per le sole carte senza racconto
    python tools/racconti-eventi.py unisci      # racconti-*.json, verificati, in pokedex-home-completo/data/racconti-eventi.json
    python tools/racconti-eventi.py pulisci     # toglie i file intermedi di _notes/lavoro/collezione/
    python tools/racconti-eventi.py verifica    # esce con 1 se una carta dei pedigree non ha il racconto, per chiudi
"""

import glob
import io
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAVORO = os.path.join(RADICE, "_notes", "lavoro", "collezione")
INGRESSO = os.path.join(LAVORO, "eventi-da-raccontare.json")
DATE = os.path.join(RADICE, "pokedex-home-completo", "data", "date-eventi.json")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "data", "racconti-eventi.json")
# parole con la maiuscola che non sono fatti: inizio di frase, nomi di metodo e di forma generici
COMUNI = {"A", "An", "The", "It", "This", "These", "Its", "In", "On", "From", "For", "With", "As", "At", "By", "And",
          "Pokemon", "Pokémon", "Wi-Fi", "Fi", "Wi", "Serial", "Code", "Local", "Wireless", "Ribbon", "Classic", "Event",
          "Trainer", "OT", "Original", "Only", "Players", "Each", "They", "He", "She", "Ball", "Cherish", "Level", "Lv",
          "Shiny", "Ability", "Nature", "Held", "Item", "Distribution", "Gift", "Mystery", "Received", "Given", "Was",
          "Card", "Center", "Centre", "Present", "Place", "Venues", "Codes", "Other", "Poke", "Store", "Stores"}
MESI = "January February March April May June July August September October November December".split()


GIOCHI_EN = {"bianco": "white", "nero": "black", "sole": "sun", "luna": "moon", "diamante": "diamond", "perla": "pearl",
             "platino": "platinum", "rubino": "ruby", "zaffiro": "sapphire", "smeraldo": "emerald", "omega": "omega",
             "alpha": "alpha", "ultrasole": "ultra sun", "ultraluna": "ultra moon", "argento": "silver", "oro": "gold",
             "cristallo": "crystal", "rosso": "red", "verde": "green", "blu": "blue", "giallo": "yellow"}
AGGETTIVI = {"european": "europe", "japanese": "japan", "american": "america", "korean": "korea", "spanish": "spain",
             "french": "france", "german": "germany", "italian": "italy", "austrian": "austria", "british": "kingdom",
             "australian": "australia", "taiwanese": "taiwan", "chinese": "china"}


def _norma(s):
    return re.sub(r"[^0-9a-z぀-ヿ一-鿿가-힯０-ｚ]", "", (s or "").lower())


def serebii_validi(x):
    """Le righe di Serebii la cui distribuzione ha lo stesso allenatore della carta: l'ID da solo non basta, perche'
    la stessa coppia di specie e ID esiste in piu' regioni (Meloetta, ID 3013: PRI2013 in Spagna e SPR2013 in America)."""
    nostri = {_norma(a.split(",")[0]) for a in x.get("allenatori", [])}
    return [s for s in x.get("serebii", []) if any(_norma(o) in nostri for o in re.split(r"[/,]", s.get("ot") or "") if o.strip())]


TRADUZIONI = [("incontrato al livello", "met at level"), ("allenatore", "OT"), ("Evento Pokémon", "Pokémon event"),
              ("Luogo grazioso", "a lovely place"), ("Centro Pokémon", "Pokémon Center"), ("Scambio in link", "link trade"),
              ("Ponte Freccialuce", "Skyarrow Bridge"), ("Fattoria Ohana", "Paniola Ranch"),
              # le etichette d'evento dei pedigree, dal 2026-11-23 per il catalogo inglese
              ("evento di terza generazione", "Generation III event"), ("evento di Game Boy", "Game Boy event"),
              ("Distribuzioni del Pokemon Center di New York", "Pokémon Center New York distributions"),
              ("Uova misteriose dei Pokemon Center giapponesi", "Mystery Eggs of the Japanese Pokémon Centers"),
              ("incontro fisso", "fixed encounter"), ("scambio in gioco", "in-game trade"), ("selvatico", "wild"),
              ("specie scoperta", "species discovered"), ("forma di Unown", "Unown form"), ("statico", "static"),
              ("(carta ", "(card "), ("uovo", "egg"), ("evento", "event")]


def in_inglese(testo):
    for it, en in TRADUZIONI:
        testo = testo.replace(it, en)
    for it, en in GIOCHI_EN.items():
        testo = re.sub(r"\b%s\b" % it.capitalize(), en.title(), testo)
    return testo


def testo_di(x):
    """Il testo dei dati della carta, con le forme in cui un racconto inglese li può dire legittimamente."""
    t = json.dumps(dict(x, serebii=serebii_validi(x)), ensure_ascii=False).lower()
    extra = []
    for a, m, _ in re.findall(r"(\d{4})-(\d{2})-(\d{2})", t):
        extra += [a, MESI[int(m) - 1].lower()]
    for it, en in GIOCHI_EN.items():
        if re.search(r"\b%s\b" % it, t):
            extra.append(en)
    for agg, paese in AGGETTIVI.items():
        if agg in t or paese in t:
            extra += [agg, paese]
    return t + " " + " ".join(extra)


def sospetti(racconto, x):
    """I fatti del racconto che non compaiono nei dati della carta: numeri, mesi e nomi propri."""
    fonte = testo_di(x)
    fuori = []
    for n in re.findall(r"\b\d{1,4}\b", racconto):
        if n not in fonte:
            fuori.append(n)
    for p in re.findall(r"\b[A-Z][A-Za-zÀ-ÿ'.-]+\b", racconto):
        if p in COMUNI or p.rstrip(".") in COMUNI:
            continue
        p = re.sub(r"-language$", "", p)
        if p.lower().rstrip(".") not in fonte:
            fuori.append(p)
    return fuori


def frase_dai_campi(x):
    validi = serebii_validi(x)
    s = validi[0] if validi else None
    specie = ", ".join(v.split(" ", 1)[-1] for v in x["specie"])
    if s:
        parti = ["%s: %s." % (s["description"] or x["evento"], specie)]
        luogo = ", ".join(v for v in [s["place"], s["region"] if s["region"] != s["place"] else ""] if v)
        quando = s["start"] + (" to " + s["end"] if s["end"] and s["end"] != s["start"] else "")
        parti.append("Distributed via %s%s%s for %s." % (s["method"], " in " + luogo if luogo else "",
                                                          ", " + quando if quando else "", s["games"]))
        parti.append("OT %s%s." % (s["ot"], ", " + s["ribbons"] if s["ribbons"] else ""))
        return " ".join(parti)
    return "%s: %s. Event data as read by PKHeX: %s" % (x["evento"], specie, in_inglese(x["storia"]))


def unisci():
    ingresso = {x["id"]: x for x in json.load(io.open(INGRESSO, encoding="utf-8"))}
    scritti = {}
    for f in sorted(glob.glob(os.path.join(LAVORO, "racconti-*.json"))):
        scritti.update(json.load(io.open(f, encoding="utf-8")))
    uscita = json.load(io.open(USCITA, encoding="utf-8")) if os.path.exists(USCITA) else {}
    sostituiti, mancanti = [], []
    for k, x in sorted(ingresso.items()):
        r = (scritti.get(k) or "").strip()
        fuori = sospetti(r, x) if r else ["mancante"]
        if not r:
            mancanti.append(k)
        if fuori:
            sostituiti.append((k, fuori[:5]))
            r = frase_dai_campi(x)
        uscita[x["evento"]] = r
    with io.open(USCITA, "w", encoding="utf-8", newline="\n") as f:
        json.dump(uscita, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    # la data d'inizio della distribuzione, per l'ordine cronologico del catalogo: solo da una riga di Serebii con lo
    # stesso allenatore, mai stimata
    date = json.load(io.open(DATE, encoding="utf-8")) if os.path.exists(DATE) else {}
    for x in ingresso.values():
        for s in serebii_validi(x):
            g = re.match(r"(\d{1,2}) (\w+) (\d{4})", s.get("start") or "")
            if g and g.group(2) in MESI:
                date[x["evento"]] = "%s-%02d-%02d" % (g.group(3), MESI.index(g.group(2)) + 1, int(g.group(1)))
                break
    with io.open(DATE, "w", encoding="utf-8", newline="\n") as f:
        json.dump(date, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print("date d'inizio da Serebii: %d" % len(date))
    print("carte %d, racconti scritti %d, mancanti %d, sostituiti con la frase dai campi %d" % (
        len(ingresso), len(scritti), len(mancanti), len(sostituiti)))
    for k, fuori in sostituiti[:15]:
        print("  %s: %s" % (k, ", ".join(fuori)))


def carte_senza_racconto():
    fatti = json.load(io.open(USCITA, encoding="utf-8")) if os.path.exists(USCITA) else {}
    mancano = set()
    for f in sorted(glob.glob(os.path.join(RADICE, "pokedex-home-completo", "pedigree", "*.md"))):
        if f.endswith("FINALE.md"):
            continue
        hdr = None
        for l in io.open(f, encoding="utf-8"):
            if l.startswith("| Box"):
                hdr = [c.strip() for c in l.strip().strip("|").split("|")]
            elif hdr and l.startswith("| ") and not l.startswith("|---"):
                r = [c.strip() for c in l.strip().strip("|").split("|")]
                if len(r) == len(hdr):
                    e = dict(zip(hdr, r))["Evento"]
                    if e not in fatti and ("(carta" in e or re.search(r"\bWC\d|evento \(", e)):
                        mancano.add(e)
    return sorted(mancano)


def verifica():
    """Esce con 1 se una carta dei pedigree non ha il racconto: il catalogo segue lo stato (ADR-127)."""
    mancano = carte_senza_racconto()
    print("carte dei pedigree senza racconto: %d" % len(mancano))
    for e in mancano[:10]:
        print("  " + e)
    if mancano:
        print("rimedio: python tools/racconti-eventi.py prepara, gli agenti sui lotti, poi unisci e pulisci")
    return 1 if mancano else 0


def prepara(lotti=4):
    """L'ingresso degli agenti per le sole carte dei pedigree che non hanno ancora un racconto, diviso in lotti."""
    import collections
    import csv
    fatti = json.load(io.open(USCITA, encoding="utf-8")) if os.path.exists(USCITA) else {}
    ev = {}
    for f in sorted(glob.glob(os.path.join(RADICE, "pokedex-home-completo", "pedigree", "*.md"))):
        if f.endswith("FINALE.md"):
            continue
        hdr = None
        for l in io.open(f, encoding="utf-8"):
            if l.startswith("| Box"):
                hdr = [c.strip() for c in l.strip().strip("|").split("|")]
                continue
            if not hdr or not l.startswith("| ") or l.startswith("|---"):
                continue
            r = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(r) != len(hdr):
                continue
            d = dict(zip(hdr, r))
            e = d["Evento"]
            if e in fatti or not ("(carta" in e or re.search(r"\bWC\d|evento \(", e)):
                continue
            x = ev.setdefault(e, {"storie": collections.Counter(), "fonti": set(), "specie": set(), "giochi": set(),
                                  "allenatori": set(), "date": set(), "lingue": set(), "n": 0})
            # la nota di stato di un esemplare da liberare o sostituto non e' la storia dell'evento
            if not d["Storia"].startswith(("Da liberare", "Sostituisce")):
                x["storie"][d["Storia"]] += 1
            x["fonti"].add(d["Fonti"]); x["specie"].add(d["Specie"]); x["giochi"].add(d["Gioco d'origine"])
            x["allenatori"].add(d["Allenatore"]); x["date"].add(d["Data"]); x["lingue"].add(d["Lingua"]); x["n"] += 1
    indice = collections.defaultdict(list)
    for r in csv.DictReader(io.open(os.path.join(RADICE, "pokedex-home-completo", "data", "serebii-eventi.csv"), encoding="utf-8")):
        indice[(r["nome"].lower(), r["identificativo"].lstrip("0"))].append(r)
    uscita = []
    for i, (k, x) in enumerate(sorted(ev.items())):
        visti, serebii = set(), []
        for sp in sorted(x["specie"]):
            for a in sorted(x["allenatori"]):
                g = re.search(r"ID (\d+)", a)
                for r in indice.get((sp.split(" ", 1)[-1].lower(), g.group(1).lstrip("0")), []) if g else []:
                    c = (r["descrizione"], r["luogo"], r["inizio"], r["fine"], r["metodo"])
                    if c not in visti:
                        visti.add(c)
                        serebii.append({"description": r["descrizione"], "method": r["metodo"], "place": r["luogo"],
                                        "region": r["regione"], "start": r["inizio"], "end": r["fine"],
                                        "games": r["giochi"], "ot": r["allenatore"], "ribbons": r["fiocchi"]})
        uscita.append({"id": "E%04d" % (i + 1), "evento": k,
                       "storia": x["storie"].most_common(1)[0][0] if x["storie"] else "",
                       "fonti": sorted(f for f in x["fonti"] if f), "specie": sorted(x["specie"]),
                       "giochi": sorted(x["giochi"]), "allenatori": sorted(x["allenatori"])[:4],
                       "date": sorted(x["date"])[:4], "lingue": sorted(x["lingue"]), "esemplari": x["n"],
                       "serebii": serebii[:3]})
    os.makedirs(LAVORO, exist_ok=True)
    json.dump(uscita, io.open(INGRESSO, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    passo = -(-len(uscita) // lotti) if uscita else 0
    for j in range(lotti if uscita else 0):
        json.dump(uscita[j * passo:(j + 1) * passo], io.open(os.path.join(LAVORO, "lotto-racconti-%d.json" % (j + 1)), "w",
                  encoding="utf-8"), ensure_ascii=False, indent=0)
    print("carte senza racconto %d, in %d lotti da %d" % (len(uscita), lotti if uscita else 0, passo))


STORIE_EN = os.path.join(RADICE, "pokedex-home-completo", "data", "storie-en.json")


def unisci_storie():
    """Le traduzioni inglesi delle storie libere dei pedigree, dagli agenti: una traduzione entra solo se porta gli
    stessi numeri dell'originale, altrimenti resta la traduzione a schema di in_inglese."""
    fatte = json.load(io.open(STORIE_EN, encoding="utf-8")) if os.path.exists(STORIE_EN) else {}
    scritte = {}
    for f in sorted(glob.glob(os.path.join(LAVORO, "traduzioni-*.json"))):
        scritte.update(json.load(io.open(f, encoding="utf-8")))
    # correzioni del 2026-11-23 dopo la lettura dei rapporti degli agenti: nomi italiani di mosse lasciati nel testo
    # inglese, e due nature rese male (Placido e' Relaxed, Sicuro e' Bold)
    mosse = {"Comete": "Comet Punch", "Demonbacio": "Lovely Kiss", "Elettrocannone": "Zap Cannon", "Flagello": "Flail",
             "Furia": "Rage", "Movim. Sismico": "Seismic Toss", "Picchiaduro": "Beat Up", "Raffica": "Gust",
             "Stordiraggio": "Confuse Ray", "Tornado": "Twister", "Turbine": "Whirlwind", "Visotruce": "Scary Face"}
    for k, v in list(scritte.items()):
        for it, en in mosse.items():
            v = re.sub(r"(?<![A-Za-z])%s(?![A-Za-z])" % re.escape(it), en, v)
        if "Placid" in k:
            v = v.replace("Quiet", "Relaxed")
        if "Sicur" in k:
            v = re.sub(r"\bSure\b", "Bold", v)
        scritte[k] = v
    numeri = lambda s: sorted(re.findall(r"\d+", s))
    scartate = [k for k, v in scritte.items() if numeri(k) != numeri(v)]
    for k, v in scritte.items():
        if k not in scartate:
            fatte[k] = v
    with io.open(STORIE_EN, "w", encoding="utf-8", newline="\n") as f:
        json.dump(fatte, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print("traduzioni ricevute %d, scartate per numeri diversi %d, nel file %d" % (len(scritte), len(scartate), len(fatte)))
    for k in scartate[:5]:
        print("  scartata: " + k[:100])


def pulisci():
    """Toglie i file intermedi degli agenti, dopo che unisci li ha portati nel file tracciato."""
    tolti = 0
    for f in glob.glob(os.path.join(LAVORO, "*.json")):
        os.remove(f)
        tolti += 1
    print("file intermedi tolti: %d" % tolti)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    comandi = {"prepara": prepara, "unisci": unisci, "pulisci": pulisci, "verifica": verifica, "unisci-storie": unisci_storie}
    if len(sys.argv) == 2 and sys.argv[1] in comandi:
        sys.exit(comandi[sys.argv[1]]() or 0)
    else:
        sys.exit(__doc__)
