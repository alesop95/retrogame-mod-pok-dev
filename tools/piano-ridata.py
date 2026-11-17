#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara il piano delle date da riscrivere nei doni da carta: una finestra per ogni esemplare, con la sua fonte.

Perché esiste
--------------
Il 2026-11-16 il proprietario ha deciso di rigenerare tutto ciò che è rigenerabile, con una data
di incontro dentro la finestra dell'evento e un giorno diverso per ciascun esemplare
(`pending.md`, voce «AL 2026-11-16, terza parte»). `tools/finestre-eventi.py` divide i doni da
carta in gruppi confrontando la data di incontro con le finestre delle liste di Bulbapedia; qui si
sceglie, per ogni esemplare, la finestra da usare, e la si scrive in un piano che
`tools/pkhex-ridata` applica leggendo l'esemplare dalla copia. La scelta del campo da riscrivere,
data di incontro o data dell'uovo, la fa lo strumento C#, perché solo lui vede se l'esemplare è
nato da un uovo.

La finestra, in ordine di fonte
--------------------------------
1. Le schede delle liste di Bulbapedia abbinate, preferendo quelle della regione che corrisponde
   alla lingua dell'esemplare (giapponese, coreana, taiwanese per il cinese, PAL per le lingue
   europee, PAL o americana per l'inglese) e le liste locali; se nessuna corrisponde, tutte.
2. Le date di ricezione reali delle carte estratte dai giocatori, dalla base dei doni di PKHeX
   (`pokedex-home-completo/data/date-carte-pkhex.json`, `tools/pkhex-date-carte`), per stessa
   generazione e numero di carta, scartando quelle anteriori all'uscita della generazione: un
   intervallo osservato, non una finestra dichiarata.
3. Serebii, per allenatore e ID esatti (`pokedex-home-completo/data/serebii-eventi.csv`).
4. La finestra di Serebii nella colonna Storia dei pedigree, abbinata in modo euristico.
5. Il Magearna da codice QR: Serebii lo dà senza data di fine; la finestra va dall'uscita del
   gioco d'origine a un anno dopo, scelta dell'agente dichiarata nel piano.

Uso
---
    python tools/piano-ridata.py            scrive pokedex-home-completo/data/piano-ridata.json
    python tools/piano-ridata.py --check    esce con 1 se il piano non è allineato
"""

import argparse
import collections
import csv
import datetime as dt
import importlib.util
import json
import os
import re
import sys
import unicodedata

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import rigenera_sicuro  # noqa: E402

RADICE = os.path.dirname(QUI)
DATI = os.path.join(RADICE, "pokedex-home-completo", "data")
USCITA = os.path.join(DATI, "piano-ridata.json")


def carica(nome, file):
    s = importlib.util.spec_from_file_location(nome, os.path.join(QUI, file))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


fe = carica("finestre_eventi", "finestre-eventi.py")
cdi = fe.cdi

USCITA_GEN = {5: dt.date(2010, 9, 18), 6: dt.date(2013, 10, 12), 7: dt.date(2016, 11, 18)}
# il gioco precedente della stessa generazione, con le sigle di PKHeX
GIOCO_PRECEDENTE = {"Rubino Omega": ("X", "Y"), "Zaffiro Alpha": ("X", "Y"),
                    "Ultrasole": ("SN", "MN"), "Ultraluna": ("SN", "MN")}
REGIONI = {"Japanese": ("Japanese",), "Korean": ("Korean",), "ChineseS": ("Taiwanese",), "ChineseT": ("Taiwanese",),
           "Italian": ("PAL", "Italian"), "French": ("PAL", "French"), "German": ("PAL", "German"),
           "Spanish": ("PAL", "Spanish"), "English": ("PAL", "American", "English")}


def norma(s):
    return unicodedata.normalize("NFKC", s or "").strip().casefold()


def regione_ok(fonte, lingua):
    if "local_event" in fonte or "game_based" in fonte or "other_event" in fonte or "traded" in fonte:
        return True
    return any("_%s_" % r in fonte or fonte.startswith("List_of_%s" % r) for r in REGIONI.get(lingua, ()))


def finestre_bulbapedia(r, schede, gen):
    trovate = fe.abbina(r, schede, gen)
    preferite = [s for s in trovate if regione_ok(s["fonte"], r["Lingua"]) and s["finestre"]]
    scelte = preferite or [s for s in trovate if s["finestre"]]
    # un abbinamento per sola specie e livello, quando l'allenatore è chi riceve o chi schiude, è debole: la stessa
    # specie può avere più distribuzioni con lo stesso livello
    debole = bool(scelte) and all(fe.del_giocatore(s) for s in scelte)
    return sorted({f for s in scelte for f in s["finestre"]}), sorted({s["fonte"] for s in scelte}), debole


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    schede = fe.carica_schede()
    osservate = collections.defaultdict(list)
    serie = collections.defaultdict(list)
    for c in json.load(open(os.path.join(DATI, "date-carte-pkhex.json"), encoding="utf-8")):
        if c["data"]:
            d = dt.date.fromisoformat(c["data"])
            if USCITA_GEN[c["generazione"]] <= d and d.year < 2026:
                osservate[(c["generazione"], c["carta"])].append(d)
                # la quinta generazione distribuisce in serie settimanali con lo stesso titolo e un numero di carta per
                # settimana: le date reali si raccolgono anche per titolo, cioè per distribuzione
                serie[(c["generazione"], norma(c["titolo"]).replace("\u3000", " "))].append(d)
    serebii = collections.defaultdict(list)
    for x in csv.DictReader(open(os.path.join(DATI, "serebii-eventi.csv"), encoding="utf-8")):
        a, b = cdi.data_inglese(x["inizio"]), cdi.data_inglese(x["fine"])
        if a:
            serebii[(norma(x["allenatore"]), x["identificativo"].strip())].append((a, b or dt.date(2026, 12, 31)))
    copie = {x["gruppo"]: x["copia"] for x in json.load(open(os.path.join(
        RADICE, "_notes", "lavoro", "giudizi-copie", "dopo-20261116-ridata.json"), encoding="utf-8"))["copie"]}
    p = os.path.join(DATI, "sostituzioni-ridata.json")
    sostituiti = {x["impronta_vecchia"] for x in json.load(open(p, encoding="utf-8"))} if os.path.exists(p) else set()

    piano, fonti = [], collections.Counter()
    for r in cdi.leggi_pedigree():
        if not cdi.CARTA.search(r["Evento"]) or r["Impronta"] in sostituiti:
            # un esemplare già sostituito da un rigenerato (ADR-126) non si pianifica di nuovo
            continue
        gen = cdi.GENERAZIONE.get(r["Gioco d'origine"], 0)
        if gen < 5:
            continue
        finestre, liste, debole = finestre_bulbapedia(r, schede, gen)
        fonte = "bulbapedia"
        m = re.search(r"\(carta (\d+)\)", r["Evento"])
        carta = int(m.group(1)) if m else None
        titolo = norma(r["Evento"][:m.start()].strip()).replace("\u3000", " ") if m else None
        reali = sorted(set(osservate.get((gen, carta), [])) | set(serie.get((gen, titolo), []))) if carta else []
        if debole and reali:
            o = reali
            finestre, fonte = [(min(o), max(o))], "date osservate nella base dei doni di PKHeX, preferite a un abbinamento per sola specie"
        uscita_gioco = dt.date.fromisoformat(cdi.USCITE[r["Gioco d'origine"]])
        if not finestre and reali:
            o = reali
            finestre, fonte = [(min(o), max(o))], "date osservate nella base dei doni di PKHeX"
        if not finestre:
            a = re.match(r"(.*?), ID (\d+)", r["Allenatore"])
            s = serebii.get((norma(a.group(1)), a.group(2))) if a else None
            if s:
                finestre, fonte = sorted(set(s)), "Serebii, allenatore e ID"
        if not finestre:
            f = cdi.finestra(r["Storia"])
            if f:
                finestre, fonte = [f], "Serebii, colonna Storia"
        if not finestre and r["Specie"].startswith("801 "):
            finestre = [(uscita_gioco, uscita_gioco + dt.timedelta(days=365))]
            fonte = "Magearna da codice QR, senza data di fine: un anno dall'uscita del gioco, scelta dell'agente"
        # una finestra anteriore all'uscita del gioco d'origine si accorcia all'uscita: la carta è di un gioco
        # precedente, e l'esemplare l'ha ricevuta nel gioco più recente
        versione = None
        utili = [(max(a, uscita_gioco), b) for a, b in finestre if b >= uscita_gioco]
        data_attuale = dt.date.fromisoformat(r["Data"])
        if finestre and not utili and r["Gioco d'origine"] in GIOCO_PRECEDENTE and data_attuale < uscita_gioco:
            # la distribuzione era finita prima dell'uscita del gioco d'origine: la carta si riceveva solo nel gioco
            # precedente della stessa generazione, quindi l'esemplare cambia gioco d'origine e tiene la finestra. Solo se
            # la data attuale è a sua volta impossibile per il gioco d'origine: un abbinamento debole con una carta
            # finita prima non basta a cambiare il gioco di un esemplare la cui data è possibile
            coppia = GIOCO_PRECEDENTE[r["Gioco d'origine"]]
            versione = coppia[int(r["Impronta"][:8], 16) % 2]
        else:
            finestre = utili
        fonti[fonte if finestre else "nessuna"] += 1
        piano.append({
            "gruppo": r["_gruppo"], "copia": copie.get(r["_gruppo"]), "box": int(r["Box"]), "posto": int(r["Posto"]),
            "impronta": r["Impronta"], "specie": r["Specie"], "evento": r["Evento"], "lingua": r["Lingua"],
            "generazione": gen, "gioco": r["Gioco d'origine"], "data_attuale": r["Data"],
            "finestre": [[a.isoformat(), b.isoformat()] for a, b in finestre],
            "fonte": fonte if finestre else "nessuna", "liste": liste if fonte == "bulbapedia" else [],
            "versione_nuova": versione,
            # le date di ricezione reali della stessa carta: una data uguale a una di queste è autentica
            "date_reali": sorted({d.isoformat() for d in reali if d >= uscita_gioco}),
        })
    testo = json.dumps(piano, ensure_ascii=False, indent=1) + "\n"
    riepilogo = ", ".join("%s %d" % kv for kv in fonti.most_common())
    if args.check:
        if not os.path.exists(USCITA) or open(USCITA, encoding="utf-8").read() != testo:
            print("piano-ridata.json non allineato: rilanciare tools/piano-ridata.py")
            return 1
        print("piano allineato: %d esemplari; %s" % (len(piano), riepilogo))
        return 0
    if rigenera_sicuro.scrivi(USCITA, testo):
        return 1
    print("scritto %s: %d esemplari; %s" % (os.path.relpath(USCITA, RADICE), len(piano), riepilogo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
