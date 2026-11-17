#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controlla la data di incontro di ogni esemplare dei lotti per HOME e scrive l'esito.

Perché esiste
--------------
Il 2026-11-16 il proprietario ha visto nel calendario delle catture di HOME un Pumpkaboo
dell'evento di Halloween 2014 datato 2003-10-19, impossibile perché la specie e la regione
sono del 2013. La data di incontro è un campo dell'esemplare e HOME la mostra così com'è;
il giudizio di PKHeX sulla sesta e settima generazione non la confronta con l'uscita del
gioco, quindi nessuno dei controlli del progetto l'aveva vista. Questo strumento la
controlla su tutte le righe dei pedigree, che riportano la data letta dal file
dell'esemplare, e scrive l'esito in `pokedex-home-completo/DATE-INCONTRO.md`.

Le classi
----------
Ogni esemplare cade in una classe sola, nell'ordine in cui sono elencate.

    impossibile          data anteriore all'uscita giapponese del gioco d'origine
    anteriore-finestra   data anteriore di oltre 60 giorni alla finestra dell'evento che la
                         colonna Storia attribuisce all'esemplare da Serebii; l'abbinamento
                         con Serebii è euristico, quindi è un caso da verificare, non un errore
    produzione           data dell'anno 2026, cioè il giorno in cui il lotto è stato prodotto
    storica              ogni altra data

Le date d'uscita sono quelle giapponesi, le prime nel mondo, e vanno rilette su Bulbapedia
prima di fidarsi di un caso al limite: lo strumento le usa solo come soglia inferiore.

Uso
---
    python tools/controlla-date-incontro.py            scrive DATE-INCONTRO.md
    python tools/controlla-date-incontro.py --check    esce con 1 se il file non è allineato
"""

import argparse
import collections
import datetime as dt
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rigenera_sicuro  # noqa: E402

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PEDIGREE = os.path.join(RADICE, "pokedex-home-completo", "pedigree")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "DATE-INCONTRO.md")

# Uscita giapponese di ciascun gioco d'origine, con il nome che usano i pedigree.
# Rosso e le versioni della seconda generazione sono quelle della Console Virtuale,
# perché solo da lì un esemplare arriva al 3DS e quindi a una data.
USCITE = {
    "Rubino": "2002-11-21", "Zaffiro": "2002-11-21", "Colosseum/XD": "2003-11-21",
    "Rosso Fuoco": "2004-01-29", "Verde Foglia": "2004-01-29", "Smeraldo": "2004-09-16",
    "Diamante": "2006-09-28", "Perla": "2006-09-28", "Platino": "2008-09-13",
    "HeartGold": "2009-09-12", "SoulSilver": "2009-09-12",
    "Nero": "2010-09-18", "Bianco": "2010-09-18", "Nero 2": "2012-06-23", "Bianco 2": "2012-06-23",
    "X": "2013-10-12", "Y": "2013-10-12", "Rubino Omega": "2014-11-21", "Zaffiro Alpha": "2014-11-21",
    "Rosso": "2016-02-27", "Oro": "2017-09-22", "Argento": "2017-09-22", "Cristallo": "2018-01-26",
    "Sole": "2016-11-18", "Luna": "2016-11-18", "Ultrasole": "2017-11-17", "Ultraluna": "2017-11-17",
}

MESI = {m: i + 1 for i, m in enumerate(
    "January February March April May June July August September October November December".split())}

TOLLERANZA = dt.timedelta(days=60)

GENERAZIONE = {
    "Rosso": 1, "Oro": 2, "Argento": 2, "Cristallo": 2,
    "Rubino": 3, "Zaffiro": 3, "Smeraldo": 3, "Rosso Fuoco": 3, "Verde Foglia": 3, "Colosseum/XD": 3,
    "Diamante": 4, "Perla": 4, "Platino": 4, "HeartGold": 4, "SoulSilver": 4,
    "Nero": 5, "Bianco": 5, "Nero 2": 5, "Bianco 2": 5,
    "X": 6, "Y": 6, "Rubino Omega": 6, "Zaffiro Alpha": 6,
    "Sole": 7, "Luna": 7, "Ultrasole": 7, "Ultraluna": 7,
}

# Un dono da carta segreta: la colonna Evento porta il numero della carta o il formato della carta.
CARTA = re.compile(r"\(carta \d+\)|evento \(WC")


def rispetto_finestra(r):
    """Dove cade la data di un dono da carta rispetto alla finestra di Serebii, senza tolleranza."""
    d = dt.date.fromisoformat(r["Data"])
    f = finestra(r.get("Storia", ""))
    anno = "giorno di produzione" if d.year == 2026 else "data storica"
    if not f:
        return "senza finestra, " + anno
    if f[0] <= d <= f[1]:
        return "dentro la finestra"
    if d < f[0]:
        return "prima della finestra"
    return "dopo la finestra, " + anno


def leggi_pedigree():
    """Le righe di tutte le tabelle dei pedigree, con il gruppo e il suo stato."""
    righe = []
    for f in sorted(glob.glob(os.path.join(PEDIGREE, "*.md"))):
        testo = open(f, encoding="utf-8").read()
        m = re.search(r"Stato del gruppo: ([^.]*)\.", testo)
        stato = m.group(1) if m else "?"
        gruppo = os.path.splitext(os.path.basename(f))[0]
        intest = None
        for linea in testo.splitlines():
            if not linea.startswith("|"):
                continue
            celle = [c.strip() for c in linea.strip().strip("|").split("|")]
            if celle[0] == "Box":
                intest = celle
                continue
            if intest is None or set(celle[0]) <= set("-:") or len(celle) != len(intest):
                continue
            r = dict(zip(intest, celle))
            r["_gruppo"], r["_stato"] = gruppo, stato
            righe.append(r)
    return righe


def data_inglese(s):
    m = re.match(r"(\d{1,2}) (\w+) (\d{4})$", s.strip())
    if not m or m.group(2) not in MESI:
        return None
    try:
        return dt.date(int(m.group(3)), MESI[m.group(2)], int(m.group(1)))
    except ValueError:
        return None


def finestra(storia):
    """La finestra dell'evento scritta da Serebii nella colonna Storia, se c'è."""
    m = re.search(r", ([^,;]*?\d{4})(?: - ([^,;]*?\d{4}))?; giochi", storia)
    if not m:
        return None
    a = data_inglese(m.group(1))
    b = data_inglese(m.group(2)) if m.group(2) else a
    if a is None:
        return None
    return a, b or a


def classifica(r):
    """La classe e il motivo di una riga."""
    try:
        d = dt.date.fromisoformat(r["Data"])
    except ValueError:
        return "impossibile", "data illeggibile «%s»" % r["Data"]
    gioco = r["Gioco d'origine"]
    if gioco in USCITE and d < dt.date.fromisoformat(USCITE[gioco]):
        return "impossibile", "anteriore all'uscita di %s (%s)" % (gioco, USCITE[gioco])
    f = finestra(r.get("Storia", ""))
    if f and d < f[0] - TOLLERANZA:
        return "anteriore-finestra", "finestra Serebii %s, %s" % (f[0].isoformat(), f[1].isoformat())
    if d.year == 2026:
        return "produzione", ""
    return "storica", ""


def componi(righe):
    classi = collections.Counter()
    per_gruppo = collections.defaultdict(collections.Counter)
    casi = []
    giochi_ignoti = collections.Counter()
    for r in righe:
        c, motivo = classifica(r)
        classi[c] += 1
        per_gruppo[(r["_gruppo"], r["_stato"])][c] += 1
        if r["Gioco d'origine"] not in USCITE:
            giochi_ignoti[r["Gioco d'origine"]] += 1
        if c in ("impossibile", "anteriore-finestra"):
            casi.append((c, r, motivo))
    ordine = ["impossibile", "anteriore-finestra", "produzione", "storica"]
    o = []
    o.append("# Date di incontro degli esemplari dei lotti per HOME")
    o.append("")
    o.append("> Documento generato da `tools/controlla-date-incontro.py` a partire dai pedigree di `pokedex-home-completo/pedigree/`. Non si modifica a mano: si rilancia lo strumento dopo ogni rigenerazione dei pedigree, e `--check` dice se il file è allineato.")
    o.append("")
    o.append("La data di incontro è un campo dell'esemplare e HOME la mostra così com'è nella scheda e nel calendario delle catture. Per i doni di sesta e settima generazione la sceglie PKHeX quando costruisce l'esemplare dalla carta: `WC6.ConvertToPKM` e `WC7.ConvertToPKM` scrivono la data della carta, e la base dei doni della libreria ne ha di due tipi. Le carte complete del server ufficiale non portano una data, e `WC6Full` e `WC7Full` danno loro il giorno in cui la libreria gira, cioè quello di produzione del lotto. Le carte estratte dai salvataggi dei giocatori portano la data in cui quel giocatore le ha ricevute, che in quattro casi è anteriore all'uscita di X e Y perché l'orologio della console era sbagliato. Il giudizio di PKHeX non confronta la data con l'uscita del gioco, quindi nessun controllo del progetto l'aveva vista prima del 2026-11-16.")
    o.append("")
    o.append("Le classi, nell'ordine in cui si assegnano: *impossibile* è una data anteriore all'uscita giapponese del gioco d'origine; *anteriore alla finestra* è una data anteriore di oltre 60 giorni alla finestra dell'evento che la colonna Storia attribuisce all'esemplare da Serebii, e siccome quell'abbinamento è euristico è un caso da verificare e non un errore; *produzione* è una data del 2026; *storica* è ogni altra data.")
    o.append("")
    o.append("## Totali")
    o.append("")
    o.append("| Classe | Esemplari |")
    o.append("|---|---|")
    for c in ordine:
        o.append("| %s | %d |" % (c, classi[c]))
    o.append("| totale | %d |" % sum(classi.values()))
    o.append("")
    o.append("## Per gruppo")
    o.append("")
    o.append("| Gruppo | Stato | %s |" % " | ".join(ordine))
    o.append("|---|---|%s" % ("---|" * len(ordine)))
    for (g, s), cnt in sorted(per_gruppo.items()):
        o.append("| %s | %s | %s |" % (g, s, " | ".join(str(cnt[c]) for c in ordine)))
    o.append("")
    o.append("## I doni da carta, per generazione d'origine")
    o.append("")
    o.append("In HOME la data di un esemplare di terza o quarta generazione non è mai quella originale. La terza generazione non ha un campo per la data: la data nasce al Parco Amici con il giorno della migrazione (`PK3.ConvertToPK4` di PKHeX). Poké Transfer, dalla quarta alla quinta generazione, sostituisce la data con il giorno del trasferimento (Bulbapedia, «Poké Transfer», e Project Pokémon, estratti di ricerca del 2026-11-16 in `SOURCES.md`), e quella data passa invariata alle generazioni successive e a HOME. La data più vecchia che HOME può mostrare per quelle due generazioni è quindi l'uscita di Nero e Bianco, il 2010-09-18. La prima e la seconda generazione prendono il giorno del Pokétrasporto. Per la quinta e la sesta generazione la data è quella del sistema quando si riceve la carta, per la settima quella in cui il dono si ritira dal fattorino: lo dicono le liste di distribuzione di Bulbapedia salvate il 2026-11-07, e il confronto con le finestre sta in `ELENCO-DATE-FINESTRA.md`.")
    o.append("")
    o.append("Una data dentro la finestra dell'evento si può quindi chiedere soltanto ai doni da carta di quinta, sesta e settima generazione, ed è obbligata per la quinta e la sesta. La tabella conta le righe dei pedigree il cui Evento porta il numero di una carta, rispetto alla finestra che Serebii dà nella colonna Storia, senza tolleranza; *senza finestra* vuol dire che la colonna non ne riporta una, quindi la finestra va cercata in un'altra fonte.")
    o.append("")
    colonne = ["dentro la finestra", "prima della finestra", "dopo la finestra, data storica",
               "dopo la finestra, giorno di produzione", "senza finestra, data storica",
               "senza finestra, giorno di produzione"]
    per_gen = collections.defaultdict(collections.Counter)
    for r in righe:
        if CARTA.search(r["Evento"]):
            per_gen[GENERAZIONE.get(r["Gioco d'origine"], 0)][rispetto_finestra(r)] += 1
    o.append("| Generazione | %s | totale |" % " | ".join(colonne))
    o.append("|---|%s---|" % ("---|" * len(colonne)))
    for g in sorted(per_gen):
        cnt = per_gen[g]
        o.append("| %s | %s | %d |" % (g or "?", " | ".join(str(cnt[c]) for c in colonne), sum(cnt.values())))
    o.append("")
    o.append("## Casi")
    o.append("")
    o.append("Box e posto sono quelli della copia del gruppo, non quelli di HOME, dove gli esemplari si ritrovano per specie, allenatore e data.")
    o.append("")
    o.append("| Classe | Gruppo | Box | Posto | Specie | Evento | Gioco d'origine | Data | Allenatore | Motivo |")
    o.append("|---|---|---|---|---|---|---|---|---|---|")
    sostituiti = {}
    p = os.path.join(RADICE, "pokedex-home-completo", "data", "sostituzioni-ridata.json")
    if os.path.exists(p):
        sostituiti = {x["impronta_vecchia"]: x for x in json.load(open(p, encoding="utf-8"))}
    for c, r, motivo in sorted(casi, key=lambda x: (ordine.index(x[0]), x[1]["_gruppo"], int(x[1]["Box"]), int(x[1]["Posto"]))):
        o.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            c, r["_gruppo"], r["Box"], r["Posto"], r["Specie"], r["Evento"], r["Gioco d'origine"],
            r["Data"], r["Allenatore"], motivo + "".join(
                "; sostituito in %s, box %d, posto %d, data %s (ADR-126)" % (
                    x["gruppo_nuovo"], x["box_nuovo"], x["posto_nuovo"], x["data_nuova"])
                for x in [sostituiti.get(r["Impronta"])] if x)))
    if giochi_ignoti:
        o.append("")
        o.append("Giochi d'origine senza data d'uscita nello strumento, quindi non controllati sulla soglia: %s." % ", ".join(
            "%s (%d)" % kv for kv in sorted(giochi_ignoti.items())))
    o.append("")
    return "\n".join(o), classi


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="verifica senza scrivere")
    ap.add_argument("--forza", action="store_true", help="scrive anche se sparirebbero titoli di sezione")
    args = ap.parse_args()
    righe = leggi_pedigree()
    if not righe:
        print("PROBLEMA: nessuna riga letta dai pedigree in %s" % PEDIGREE, file=sys.stderr)
        return 1
    testo, classi = componi(righe)
    riepilogo = ", ".join("%s %d" % kv for kv in sorted(classi.items()))
    if args.check:
        attuale = open(USCITA, encoding="utf-8").read() if os.path.exists(USCITA) else None
        if attuale != testo:
            print("DATE-INCONTRO.md non allineato ai pedigree: rilanciare tools/controlla-date-incontro.py (%s)" % riepilogo)
            return 1
        print("DATE-INCONTRO.md allineato: %d righe, %s" % (len(righe), riepilogo))
        return 0
    fermi = rigenera_sicuro.scrivi(USCITA, testo, schema=r"^#{1,6} ", forza=args.forza)
    if fermi:
        return 1
    print("scritto %s: %d righe, %s" % (os.path.relpath(USCITA, RADICE), len(righe), riepilogo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
