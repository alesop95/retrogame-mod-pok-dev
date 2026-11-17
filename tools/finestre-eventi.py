#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Abbina ogni dono da carta di quinta, sesta e settima generazione alla sua finestra di distribuzione.

Perché esiste
--------------
Il 2026-11-16 il proprietario ha chiesto, per i doni da carta, una data di incontro dentro la
finestra dell'evento, e prima di decidere ha voluto l'elenco completo (ADR in attesa,
`pending.md`, voce «AL 2026-11-16, seconda parte»). La colonna Storia dei pedigree porta una
finestra di Serebii abbinata in modo euristico, e solo per una parte delle righe. Questo
strumento la ricava invece dalle liste di distribuzione di Bulbapedia salvate dalla Wayback
Machine il 2026-11-07 (`_notes/fonti/raccolte/bulbapedia-wayback-2026-11-07/`, ADR-119),
abbinando ogni riga dei pedigree a una scheda per numero del Pokédex, ID e allenatore, oppure
per numero del Pokédex e livello quando la carta dà l'allenatore del giocatore.

La regola di plausibilità, letta nelle stesse liste
----------------------------------------------------
Sesta generazione: «Date received is the receiving system's date when the Wonder Card is
received», quindi la data deve stare nella finestra. Quinta generazione, stesse liste: «The date
this Pokémon was received is determined by the date on the DS when the Wonder Card is received»,
quindi vale lo stesso. Settima generazione: «Date received is the date on the system when the
gift is picked up from the deliveryman», quindi una data dopo la finestra è possibile, una
prima no. Le carte di quinta, sesta e settima generazione non si ricevono più nel 2026: un
esemplare di quinta o sesta generazione datato 2026 è fuori da ogni finestra anche quando la
sua scheda non si trova.

Le classi
----------
    dentro          la data sta in almeno una delle finestre abbinate
    prima           la data è anteriore a tutte le finestre abbinate
    dopo            la data è posteriore a tutte le finestre abbinate
    senza scheda    nessuna scheda delle liste salvate si abbina alla riga

Uso
---
    python tools/finestre-eventi.py            scrive ELENCO-DATE-FINESTRA.md e data/finestre-eventi.json
    python tools/finestre-eventi.py --check    esce con 1 se i due file non sono allineati
"""

import argparse
import collections
import datetime as dt
import glob
import html
import importlib.util
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rigenera_sicuro  # noqa: E402

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTE = os.path.join(RADICE, "_notes", "fonti", "raccolte", "bulbapedia-wayback-2026-11-07")
USCITA_MD = os.path.join(RADICE, "pokedex-home-completo", "ELENCO-DATE-FINESTRA.md")
USCITA_JSON = os.path.join(RADICE, "pokedex-home-completo", "data", "finestre-eventi.json")

_spec = importlib.util.spec_from_file_location(
    "controlla_date_incontro", os.path.join(os.path.dirname(os.path.abspath(__file__)), "controlla-date-incontro.py"))
cdi = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cdi)

MESI = {m: i + 1 for i, m in enumerate(
    "January February March April May June July August September October November December".split())}
MESE = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
# «July 1 to 22, 2013», «April 29 to May 26, 2016», «November 17, 2017 to January 10, 2018», «July 6, 2014»
DATA = re.compile(MESE + r" (\d{1,2})(?:, (\d{4}))?(?:\s*(?:to|-|\u2013)\s*(?:" + MESE + r" )?(\d{1,2}),? (\d{4}))?")

SENZA_FINE = dt.date(2099, 12, 31)

FAMIGLIA = {5: re.compile(r"Generation_V\.html$"), 6: re.compile(r"Generation_VI\.html$"),
            7: re.compile(r"Sun_Moon_Ultra_Sun_and_Ultra_Moon\.html$|Generation_VII\.html$")}


def norma(s):
    return re.sub(r"[\s.\-]", "", unicodedata.normalize("NFKC", s or "").casefold())


def testo(h):
    h = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", h))
    return [x.strip() for x in t.split("\n") if x.strip()]


def finestre_in(righe):
    """Le finestre scritte in un insieme di righe di testo."""
    out = []
    for riga in righe:
        # «on October 7 and 8, 2017» è un intervallo di due giorni
        riga = re.sub(r"\b(\d{1,2}) and (\d{1,2}), (\d{4})", r"\1 to \2, \3", riga)
        # «October 15, 2014 onwards» è una finestra senza fine
        for m in re.finditer(MESE + r" (\d{1,2}), (\d{4}) onwards", riga):
            try:
                out.append((dt.date(int(m.group(3)), MESI[m.group(1)], int(m.group(2))), SENZA_FINE))
            except ValueError:
                pass
        riga = re.sub(MESE + r" \d{1,2}, \d{4} onwards", "", riga)
        for m in DATA.finditer(riga):
            m1, g1, a1, m2, g2, a2 = m.groups()
            try:
                if g2 is None:
                    if not a1:
                        continue
                    d = dt.date(int(a1), MESI[m1], int(g1))
                    out.append((d, d))
                else:
                    fine = dt.date(int(a2), MESI[m2 or m1], int(g2))
                    inizio = dt.date(int(a1 or a2), MESI[m1], int(g1))
                    if inizio > fine:
                        inizio = dt.date(int(a2) - 1, MESI[m1], int(g1))
                    out.append((inizio, fine))
            except ValueError:
                continue
    return out


def schede_gen5(righe, fonte):
    out = []
    for i, r in enumerate(righe):
        if r != "Dex No." or i + 1 >= len(righe) or not righe[i + 1].isdigit():
            continue
        blocco = righe[i:i + 90]
        dex = int(righe[i + 1])
        ot = blocco[blocco.index("OT") + 1] if "OT" in blocco else None
        ids = [blocco[blocco.index("ID No.") + 1]] if "ID No." in blocco else []
        lv = None
        if "Lv." in blocco:
            k = blocco.index("Lv.")
            lv = int(blocco[k + 1]) if blocco[k + 1].isdigit() else None
        f = []
        if "This Pokémon was available in" in blocco:
            k = blocco.index("This Pokémon was available in")
            f = finestre_in(blocco[k:k + 6])
        if not f:
            # le liste locali danno le date in una tabella dopo la scheda; la prosa della scheda
            # seguente comincia con «This» o «These», o con un rimando a Bulbanews
            coda = righe[i + 1:i + 200]
            fine = next((j for j, x in enumerate(coda) if x == "Dex No." or x in ("This", "These", "Bulbanews")), len(coda))
            f = finestre_in(coda[:fine])
        out.append({"fonte": fonte, "dex": dex, "ids": ids, "ot": [ot] if ot else [], "livello": lv, "finestre": f})
    return out


def schede_gen67(righe, fonte):
    out = []
    for i, r in enumerate(righe):
        m = re.fullmatch(r"#(\d{3,4})", r)
        if not m:
            continue
        blocco = righe[i:i + 120]
        prossimo = next((k for k in range(1, len(blocco)) if re.fullmatch(r"#\d{3,4}", blocco[k])), len(blocco))
        blocco = blocco[:prossimo]
        dex = int(m.group(1))
        lv = next((int(x.split()[1]) for x in blocco if re.fullmatch(r"Level \d+", x)), None)
        ids, ots = [], []
        if "ID:" in blocco and "OT:" in blocco and blocco.index("ID:") < blocco.index("OT:"):
            ids = blocco[blocco.index("ID:") + 1:blocco.index("OT:")]
        if "OT:" in blocco and "Met:" in blocco:
            ots = blocco[blocco.index("OT:") + 1:blocco.index("Met:")]
        f = []
        if "Duration" in blocco:
            k = blocco.index("Duration")
            fine = next((j for j in range(k, len(blocco)) if blocco[j] in ("Moves in", "Distribution")
                         or blocco[j].startswith("Date received")), len(blocco))
            f = finestre_in(blocco[k:fine])
        if not f:
            # la frase prima della scheda: «This X was distributed ... from A to B»
            prima = righe[max(0, i - 25):i]
            f = finestre_in([x for x in prima if "distributed" in x or "available" in x])
        out.append({"fonte": fonte, "dex": dex, "ids": ids, "ot": ots, "livello": lv, "finestre": f})
    return out


def carica_schede():
    schede = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(LISTE, "*.html"))):
        nome = os.path.basename(f)
        gen = next((g for g, rx in FAMIGLIA.items() if rx.search(nome)), None)
        if gen is None:
            continue
        righe = testo(open(f, encoding="utf-8", errors="replace").read())
        for s in (schede_gen5 if gen == 5 else schede_gen67)(righe, nome):
            schede[gen].append(s)
    return schede


def del_giocatore(s):
    # «(Player's)» per i doni, «(Hatcher's)» per le uova: l'allenatore è chi riceve o chi schiude
    return any(x.startswith(("(Player", "(Hatcher")) for x in s["ids"] + s["ot"])


def vari(s):
    return any(norma(o) in ("(various)", "various") for o in s["ot"])


def abbina(r, schede, gen):
    dex = int(r["Specie"].split()[0])
    m = re.match(r"(.*?), ID (\d+)", r["Allenatore"])
    ot, idn = (m.group(1), m.group(2)) if m else ("", "")
    liv = re.match(r"\d+, incontrato al (\d+)", r["Livello"])
    liv = int(liv.group(1)) if liv else None
    stessa, evoluta, altra_lingua = [], [], []
    for s in schede.get(gen, []):
        if del_giocatore(s):
            if s["dex"] == dex and s["livello"] is not None and s["livello"] == liv:
                stessa.append(s)
            continue
        if not any(x.lstrip("0") == idn.lstrip("0") for x in s["ids"] if x.isdigit()):
            continue
        if vari(s):
            # allenatore che cambia col luogo: si accetta solo con la stessa specie
            if s["dex"] == dex:
                stessa.append(s)
        elif any(norma(o) == norma(ot) for o in s["ot"]):
            (stessa if s["dex"] == dex else evoluta).append(s)
        elif s["dex"] == dex:
            # l'allenatore della carta cambia con la lingua del gioco, e la lista non le elenca tutte
            altra_lingua.append(s)
    # un esemplare evoluto conserva ID e allenatore della carta, non la specie
    return stessa or evoluta or altra_lingua


def classifica(d, finestre):
    if not finestre:
        return "senza scheda"
    if any(a <= d <= b for a, b in finestre):
        return "dentro"
    if all(d < a for a, b in finestre):
        return "prima"
    if all(d > b for a, b in finestre):
        return "dopo"
    return "fra due finestre"


SOSTITUZIONI = os.path.join(RADICE, "pokedex-home-completo", "data", "sostituzioni-ridata.json")
SOSTITUITI = ({x["impronta_vecchia"]: x for x in json.load(open(SOSTITUZIONI, encoding="utf-8"))}
              if os.path.exists(SOSTITUZIONI) else {})
ESITI = os.path.join(RADICE, "pokedex-home-completo", "data", "esito-ridata.json")
GIA_DENTRO = ({k for k, v in json.load(open(ESITI, encoding="utf-8")).items() if v["esito"] == "gia' dentro"}
              if os.path.exists(ESITI) else set())

VICINO = 60  # giorni: oltre questa distanza una data storica non è un fuso orario o un luogo non elencato

GRUPPI = [
    ("A", "impossibile per il gioco", "data anteriore all'uscita del gioco d'origine, oppure del 2026 in quinta o sesta generazione, oppure fuori dalle finestre di oltre 60 giorni in quinta e sesta, oppure prima della finestra in settima"),
    ("B", "possibile ma fuori dalla finestra", "settima generazione con data successiva alla finestra o del 2026: il dono si può ritirare dal fattorino dopo l'evento"),
    ("C", "storica vicina alla finestra", "data di una carta reale a meno di 60 giorni dalle finestre elencate: fuso orario, luogo o giorno non elencati"),
    ("D", "storica senza finestra", "data storica senza una scheda o una finestra abbinata"),
    ("E", "dentro la finestra", "nessuna azione: data di incontro dentro la finestra, oppure, secondo `tools/pkhex-ridata`, data dell'uovo dentro la finestra o data di ricezione reale della stessa distribuzione"),
    ("F", "sostituito", "esemplare già rigenerato con la data dentro la finestra nelle copie RIDATA (ADR-126), da liberare in HOME secondo l'elenco da liberare di `python tools/elenco-da-liberare.py --stampa`"),
]


def distanza(d, finestre):
    return min(min(abs((d - a).days), abs((d - b).days)) for a, b in finestre)


def gruppo(v):
    d = dt.date.fromisoformat(v["data"])
    finestre = [(dt.date.fromisoformat(a), dt.date.fromisoformat(b)) for a, b in v["finestre"]]
    g = v["generazione"]
    if v["impronta"] in SOSTITUITI:
        return "F"
    # `tools/pkhex-ridata` ha guardato il campo che conta, cioè la data dell'uovo per un dono in forma d'uovo, e le date di
    # ricezione reali della stessa distribuzione: se lo ha trovato a posto, l'esemplare è dentro
    if v["impronta"] in GIA_DENTRO:
        return "E"
    # una data anteriore all'uscita del gioco d'origine è impossibile anche dentro la finestra della carta:
    # la carta è di un gioco precedente e l'esemplare è stato attribuito a uno uscito dopo
    if v["gioco"] in cdi.USCITE and d < dt.date.fromisoformat(cdi.USCITE[v["gioco"]]):
        return "A"
    if v["classe"] == "dentro":
        return "E"
    if g in (5, 6):
        if d.year == 2026:
            return "A"
        if finestre:
            return "A" if distanza(d, finestre) > VICINO else "C"
        return "D"
    if v["classe"] == "prima":
        return "A"
    if d.year == 2026 or v["classe"] == "dopo":
        return "B"
    return "D"


def componi():
    schede = carica_schede()
    righe = [r for r in cdi.leggi_pedigree()
             if cdi.CARTA.search(r["Evento"]) and cdi.GENERAZIONE.get(r["Gioco d'origine"], 0) >= 5]
    voci = []
    for r in righe:
        gen = cdi.GENERAZIONE[r["Gioco d'origine"]]
        trovate = abbina(r, schede, gen)
        finestre = sorted({f for s in trovate for f in s["finestre"]})
        d = dt.date.fromisoformat(r["Data"])
        classe = classifica(d, finestre)
        if trovate and not finestre:
            classe = "scheda senza finestra"
        m = re.match(r"(.*?), ID (\d+)", r["Allenatore"])
        voci.append({
            "gruppo": r["_gruppo"], "stato": r["_stato"], "box": int(r["Box"]), "posto": int(r["Posto"]),
            "specie": r["Specie"], "forma": r["Forma"], "cromatico": r["Cromatico"], "evento": r["Evento"],
            "gioco": r["Gioco d'origine"], "generazione": gen, "data": r["Data"], "sfera": r["Sfera"],
            "lingua": r["Lingua"], "allenatore": m.group(1) if m else r["Allenatore"], "id": m.group(2) if m else "",
            "classe": classe, "finestre": [[a.isoformat(), b.isoformat()] for a, b in finestre],
            "liste": sorted({s["fonte"] for s in trovate}), "impronta": r["Impronta"],
        })
        voci[-1]["gruppo_decisione"] = gruppo(voci[-1])
    ordine = ["dentro", "prima", "dopo", "fra due finestre", "scheda senza finestra", "senza scheda"]
    per_gen = collections.defaultdict(collections.Counter)
    for v in voci:
        per_gen[v["generazione"]][v["classe"]] += 1
    per_gruppo = collections.defaultdict(collections.Counter)
    for v in voci:
        per_gruppo[v["gruppo_decisione"]][v["generazione"]] += 1
    o = ["# Date di incontro dei doni da carta rispetto alla finestra dell'evento", "",
         "> Documento generato da `tools/finestre-eventi.py` dai pedigree e dalle liste di distribuzione di Bulbapedia salvate il 2026-11-07. Non si modifica a mano. I dati per esemplare, con le finestre e le liste abbinate, stanno in `pokedex-home-completo/data/finestre-eventi.json`.", "",
         "Le righe sono quelle dei pedigree il cui Evento porta il numero di una carta, con gioco d'origine di quinta, sesta o settima generazione: per la terza e la quarta HOME mostra per forza la data di Poké Transfer (`DATE-INCONTRO.md`). Ogni riga si abbina alle schede delle liste per ID e allenatore, anche quando l'esemplare si è evoluto, oppure per specie e livello di incontro quando la carta dà l'allenatore del giocatore; un allenatore «(Various)» vale solo con la stessa specie. Le finestre di tutte le schede abbinate, di ogni regione, valgono insieme.", "",
         "Le stesse liste dicono quale data è plausibile. In quinta e sesta generazione la data è quella del sistema quando si riceve la carta, quindi deve stare nella finestra. In settima è quella in cui si ritira il dono dal fattorino, quindi può stare dopo la finestra ma non prima. Nel 2026 nessuna di queste carte si riceve più.", "",
         "## Totali per generazione e classe", "",
         "| Generazione | %s | totale |" % " | ".join(ordine), "|---|%s---|" % ("---|" * len(ordine))]
    for g in sorted(per_gen):
        c = per_gen[g]
        o.append("| %d | %s | %d |" % (g, " | ".join(str(c[k]) for k in ordine), sum(c.values())))
    o += ["", "## Gruppi di decisione", "",
          "| Gruppo | Nome | Quinta | Sesta | Settima | Totale | Criterio |", "|---|---|---|---|---|---|---|"]
    for sigla, nome, criterio in GRUPPI:
        c = per_gruppo[sigla]
        o.append("| %s | %s | %d | %d | %d | %d | %s |" % (sigla, nome, c[5], c[6], c[7], sum(c.values()), criterio))
    o += ["", "Box e posto sono quelli della copia del gruppo. L'etichetta di HOME è un'inferenza da verificare su un esemplare: i conteggi delle etichette «Bank N» sono compatibili con un'etichetta per box di Bank, cioè per box della copia."]
    for sigla, nome, _c in GRUPPI[:4]:
        sel = sorted((v for v in voci if v["gruppo_decisione"] == sigla), key=lambda v: (v["gruppo"], v["box"], v["posto"]))
        o += ["", "## Gruppo %s, %s" % (sigla, nome), "", "Esemplari: %d." % len(sel), "",
              "| Gruppo | Box | Posto | Etichetta presunta | Specie | Cromatico | Lingua | Allenatore | ID | Data | Finestre |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for v in sel:
            o.append("| %s | %d | %d | Bank %d | %s | %s | %s | %s | %s | %s | %s |" % (
                v["gruppo"], v["box"], v["posto"], v["box"], v["specie"], v["cromatico"], v["lingua"], v["allenatore"],
                v["id"], v["data"], "; ".join("%s, %s" % tuple(f) for f in v["finestre"]) or "nessuna"))
    o.append("")
    return "\n".join(o), voci, per_gen


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="verifica senza scrivere")
    ap.add_argument("--forza", action="store_true", help="scrive anche se sparirebbero titoli di sezione")
    args = ap.parse_args()
    testo_md, voci, per_gen = componi()
    testo_json = json.dumps(voci, ensure_ascii=False, indent=1) + "\n"
    riepilogo = "; ".join("gen %d: %s" % (g, ", ".join("%s %d" % kv for kv in sorted(c.items())))
                          for g, c in sorted(per_gen.items()))
    if args.check:
        ok = True
        for p, t in ((USCITA_MD, testo_md), (USCITA_JSON, testo_json)):
            if not os.path.exists(p) or open(p, encoding="utf-8").read() != t:
                print("%s non allineato: rilanciare tools/finestre-eventi.py" % os.path.relpath(p, RADICE))
                ok = False
        if ok:
            print("finestre allineate: %d righe; %s" % (len(voci), riepilogo))
        return 0 if ok else 1
    fermi = rigenera_sicuro.scrivi(USCITA_MD, testo_md, schema=r"^#{1,6} ", forza=args.forza)
    fermi += rigenera_sicuro.scrivi(USCITA_JSON, testo_json, forza=args.forza)
    if fermi:
        return 1
    print("scritti %s e %s: %d righe; %s" % (os.path.relpath(USCITA_MD, RADICE), os.path.relpath(USCITA_JSON, RADICE),
                                             len(voci), riepilogo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
