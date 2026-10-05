#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scrive lo stato finale di ogni indirizzo del residuo del corpus, e lo riporta nel registro delle fonti.

Perché esiste
-------------
Il 2026-10-01 il proprietario ha stabilito che nessuna fonte resta nello stato «catalogata»: ognuna è letta e usata,
oppure dichiarata irrecuperabile con la prova del tentativo, oppure fuori perimetro con il motivo. Lo stato della
lettura del residuo sta sparso fra i file locali di `_notes/fonti/corpus-residuo/` (esiti, testi, trascrizioni, estratti,
descrizioni delle immagini, cataloghi dei canali), che un clone non ha. Questo strumento lo ricompone in un solo stato
per indirizzo, lo scrive in un file tracciato, e lo sostituisce alla parola «catalogato» nelle righe del registro e del
censimento che portano quell'indirizzo, perché il registro non dica di una fonte ciò che non è più vero.

Che cosa fa
-----------
Scrive `pokedex-home-completo/data/residuo-corpus.csv` con indirizzo, stato e dettaglio. Gli stati sono sei: letto (con
l'esito dell'estrazione), letto a vista (immagini senza testo, descritte), trascritto (video), catalogo letto (canali),
saltato con il motivo, irrecuperabile con il motivo. Con `--registro` riscrive sul posto la cella di stato delle righe
di `SOURCES.md` e di `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` che portano un indirizzo del residuo. Con
`--check` esce con un codice diverso da zero se restano indirizzi senza uno stato finale.

Uso
---
    python tools/stato-residuo-corpus.py
    python tools/stato-residuo-corpus.py --registro
    python tools/stato-residuo-corpus.py --check
"""

import argparse
import collections
import csv
import io
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(RADICE, "_notes", "fonti", "corpus-residuo")
ELENCO = os.path.join(RADICE, "_notes", "fonti", "da-leggere-corpus.json")
# Dal 2026-10-05, su direttiva del proprietario («tutti quelli dove hai scritto no dimentichiamole e pulisci tutto»):
# gli indirizzi che non sono fonti e quelli irrecuperabili escono dal CSV, dai conteggi e dai registri. Restano
# soltanto in questo elenco, fuori da git, con il motivo, perché un censimento rigenerato non li riporti dentro.
DIMENTICATI = os.path.join(RADICE, "_notes", "fonti", "corpus-residuo", "dimenticati.json")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "data", "residuo-corpus.csv")
REGISTRI = [os.path.join(RADICE, "SOURCES.md"), os.path.join(RADICE, "pokedex-home-completo", "CENSIMENTO-FONTI-COLLEZIONE.md")]
VIDEO_TESTO = [os.path.join(R, "video", "testo"), os.path.join(R, "canali", "testo"),
               os.path.join(RADICE, "_notes", "fonti", "consegne", "2026-09-29-video-chiusura-bank", "testo")]


# La cella di stato si riconosce dal suo inizio: «catalogato» prima della lettura, uno degli stati dopo.
# Riconoscere solo «catalogato» lasciava ferma per sempre una cella già scritta una volta, come
# «da trascrivere», anche dopo che il video era stato letto.
# Gli stati portano i due punti, così una nota scritta a mano come «letto il 2026-...» non viene sovrascritta.
STATI_CELLA = ("catalogat",) + tuple(x + ":" for x in ("letto", "trascritto", "saltato", "catalogo letto", "irrecuperabile",
                                                      "da estrarre", "da trascrivere", "letto a vista", "letto con OCR"))


def leggi_json(p, difetto):
    return json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else difetto


def affermazioni(p):
    """Le righe utili di un estratto, o None se l'estratto non c'è."""
    if not os.path.exists(p):
        return None
    t = io.open(p, encoding="utf-8").read().split("\n", 2)[-1]
    return [r for r in t.splitlines() if r.strip().startswith("-") and "NONE" not in r]


def esito_estratto(righe):
    if righe is None:
        return None
    return "estratto con %d affermazioni, verificate" % len(righe) if righe else "estratto senza affermazioni pertinenti"


def chiave(url):
    return url.replace("\\", "").rstrip("/")


# Dal 2026-10-05, su direttiva del proprietario («pulire l'immondizia delle fonti non necessarie»): i collegamenti che
# non sono fonti (promemoria di bot, calcoli, profili, inviti, indirizzi locali, segnaposto, pagine fuori tema o fuori
# perimetro) passano allo stato «scartato» e con --registro spariscono dalle tabelle dei due registri, contati in una
# nota sola. Restano nel CSV, perché il presidio --check deve sapere che hanno uno stato finale.
# Lo stesso giorno, sempre su sua direttiva («pulizia, non perdere tempo»), escono dalle tabelle anche gli irrecuperabili.
SCARTI = ("bot RemindMe", "WolframAlpha", "pagina di profilo", "invito a un server Discord", "indirizzo numerico",
          "segnaposto, accorciatore", "pagina senza contenuto", "documentazione di sicurezza", "pirateria", ".cia")
NOTA_SCARTI = ("Pulizia del 2026-10-05: %d collegamenti del residuo del corpus che non sono fonti o che non si possono "
               "più leggere sono dimenticati su direttiva del proprietario e tolti dalle tabelle; %d irrecuperabili "
               "restano aperti come richiesta al proprietario. L'elenco dei dimenticati, con il motivo, sta fuori da git "
               "in `_notes/fonti/corpus-residuo/dimenticati.json`.")


def classifica_saltato(motivo):
    if "archivio cifrato di Mega" in motivo:
        return "irrecuperabile", "collegamento Mega senza la chiave di decrittazione dopo il cancelletto: il contenuto non si apre (2026-10-05)"
    if any(k in motivo for k in SCARTI):
        return "scartato", "non è una fonte: " + motivo
    return "saltato", motivo


def calcola():
    esiti = leggi_json(os.path.join(R, "esiti.json"), {})
    fuori = {v["file"] for v in leggi_json(os.path.join(R, "fuori-tema.json"), {}).values()}
    fogli = {l.strip() + ".md" for l in io.open(os.path.join(R, "fogli.txt"), encoding="utf-8")} if os.path.exists(os.path.join(R, "fogli.txt")) else set()
    descritte = leggi_json(os.path.join(R, "immagini-descritte.json"), {})
    catalogo = leggi_json(os.path.join(R, "canali", "catalogo.json"), {})
    scelti = leggi_json(os.path.join(R, "canali", "scelti.json"), {})
    senza_testo = leggi_json(os.path.join(R, "canali", "senza-testo.json"), {})
    meta_errori = {}
    if os.path.exists(os.path.join(R, "video", "meta.log")):
        for r in io.open(os.path.join(R, "video", "meta.log"), encoding="utf-8", errors="replace"):
            m = re.search(r"\[youtube\] ([A-Za-z0-9_-]{11}): (.*)", r)
            if m and "ERROR" in r:
                meta_errori[m.group(1)] = m.group(2).strip()[:120]
    dimenticati = leggi_json(DIMENTICATI, {})
    stati = collections.OrderedDict()
    for url in json.load(io.open(ELENCO, encoding="utf-8")):
        if url in dimenticati:
            continue
        e = esiti.get(url, {"esito": "non letto", "motivo": "non ancora tentato"})
        stato, dettaglio = "", ""
        if e["esito"] == "letto":
            f = e["file"]
            if f in fuori:
                stato, dettaglio = "letto", "documentazione tecnica o pagina generica fuori tema, conservata senza estrazione"
            elif f in fogli:
                stato, dettaglio = "letto", "foglio di calcolo confrontato riga per riga con la lista completa (fogli-forme-ignote.md)"
            else:
                d = esito_estratto(affermazioni(os.path.join(R, "estratti", f[:-3] + ".txt")))
                stato, dettaglio = ("letto", d) if d else ("da estrarre", "testo su disco, estrazione non ancora fatta")
        elif e["esito"] == "immagine":
            f = e["file"]
            base = os.path.splitext(f)[0]
            if f in descritte:
                stato, dettaglio = "letto a vista", descritte[f]
            else:
                d = esito_estratto(affermazioni(os.path.join(R, "estratti", base + ".txt")))
                stato, dettaglio = ("letto con OCR", d) if d else ("da estrarre", "testo dell'immagine su disco, estrazione non ancora fatta")
        elif e["esito"] == "video":
            vid = e.get("id")
            testo = next((os.path.join(d, vid + ".txt") for d in VIDEO_TESTO if vid and os.path.exists(os.path.join(d, vid + ".txt"))), None)
            if vid in meta_errori and not testo:
                stato, dettaglio = "irrecuperabile", "video non più disponibile su YouTube: " + meta_errori[vid]
            elif testo:
                parole = len(io.open(testo, encoding="utf-8").read().split())
                cartella = os.path.dirname(os.path.dirname(testo))
                if parole < 80:
                    d = esito_estratto(affermazioni(os.path.join(R, "video-meta", "estratti", vid + ".txt")))
                    stato, dettaglio = ("letto", "video senza parlato, letti titolo e descrizione: " + (d or "estrazione dei metadati da fare"))
                    if not d:
                        stato = "da estrarre"
                else:
                    d = esito_estratto(affermazioni(os.path.join(cartella, "estratti", vid + ".txt")))
                    stato, dettaglio = ("trascritto", d) if d else ("da estrarre", "trascrizione su disco, estrazione non ancora fatta")
            else:
                stato, dettaglio = "da trascrivere", "in coda per la trascrizione"
        elif e["esito"] == "saltato":
            m = re.match(r"https?://(www\.)?youtube\.com/((@|channel/)[^/?]+)", url.replace("\\", ""))
            canale = next((k for k in catalogo if m and k.endswith(m.group(2))), None)
            if canale and "video" in catalogo[canale]:
                ids = [v["id"] for v in scelti.get(canale, [])]
                testi = {i: next((os.path.join(d, i + ".txt") for d in VIDEO_TESTO if os.path.exists(os.path.join(d, i + ".txt"))), None) for i in ids}
                mancanti = [i for i in ids if not testi[i] and i not in senza_testo]
                non_letti = [i for i in ids if testi[i] and not any(os.path.exists(os.path.join(os.path.dirname(os.path.dirname(testi[i])), x, i + ".txt")) for x in ("estratti",))]
                if mancanti:
                    stato, dettaglio = "da trascrivere", "%d video scelti su %d senza testo" % (len(mancanti), len(ids))
                elif non_letti:
                    stato, dettaglio = "da estrarre", "%d trascrizioni su %d non ancora lette" % (len(non_letti), len(ids))
                else:
                    stato, dettaglio = "catalogo letto", "%d video in catalogo, %d scelti per tema: %d letti dalla trascrizione, %d senza testo ricavabile (canali/senza-testo.json)" % (
                        catalogo[canale]["video"], len(ids), len(ids) - sum(1 for i in ids if not testi[i]), sum(1 for i in ids if not testi[i]))
            elif canale:
                stato, dettaglio = "irrecuperabile", "canale non più raggiungibile: " + catalogo[canale].get("errore", "")[-120:].replace("\n", " ")
            else:
                stato, dettaglio = classifica_saltato(e.get("motivo", ""))
        else:
            stato, dettaglio = "irrecuperabile", e.get("motivo", "")
        stati[url] = (stato, dettaglio.replace("\n", " ").strip())
    return stati


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--registro", action="store_true", help="riscrive la cella di stato nel registro e nel censimento")
    ap.add_argument("--check", action="store_true", help="fallisce se restano indirizzi senza stato finale")
    a = ap.parse_args()
    stati = calcola()
    conto = collections.Counter(s for s, _ in stati.values())
    aperti = [u for u, (s, _) in stati.items() if s in ("da estrarre", "da trascrivere")]
    if a.check:
        print(dict(conto))
        return 1 if aperti else 0
    os.makedirs(os.path.dirname(USCITA), exist_ok=True)
    with io.open(USCITA, "w", encoding="utf-8", newline="\n") as f:
        w = csv.writer(f, delimiter=";", lineterminator="\n")
        w.writerow(["indirizzo", "stato", "dettaglio"])
        for u, (s, d) in stati.items():
            w.writerow([u, s, d])
    print("scritto", USCITA, dict(conto))
    if a.registro:
        per_chiave = {chiave(u): s for u, s in stati.items()}
        per_chiave.update({chiave(u): ("dimenticato", "") for u in leggi_json(DIMENTICATI, {})})
        for p in REGISTRI:
            righe = io.open(p, encoding="utf-8", newline="").read().split("\n")
            cambiate = 0
            tolte = 0
            for i, r in enumerate(righe):
                if r.startswith("|"):
                    u = next((c.strip() for c in r.split("|") if c.strip().startswith("http")), None)
                    if u and per_chiave.get(chiave(u), ("",))[0] in ("scartato", "irrecuperabile", "dimenticato"):
                        righe[i] = None
                        tolte += 1
                        continue
                if not r.startswith("|") or not any(c.strip().startswith(STATI_CELLA) for c in r.split("|")):
                    continue
                celle = r.split("|")
                url = next((c.strip() for c in celle if c.strip().startswith("http")), None)
                if not url or chiave(url) not in per_chiave:
                    continue
                s, d = per_chiave[chiave(url)]
                nuova = (s + ": " + d)[:140].replace("|", "/")
                celle = [(" " + nuova + " ") if c.strip().startswith(STATI_CELLA) else c for c in celle]
                righe[i] = "|".join(celle)
                cambiate += 1
            righe = [r for r in righe if r is not None and not r.startswith(NOTA_SCARTI[:30])]
            k = next((i for i, r in enumerate(righe) if r.startswith("# ")), 0)
            righe[k + 1:k + 1] = ["", NOTA_SCARTI % (len(leggi_json(DIMENTICATI, {})), conto["irrecuperabile"])]
            io.open(p, "w", encoding="utf-8", newline="").write("\n".join(righe))
            print(os.path.basename(p), cambiate, "righe aggiornate,", tolte, "righe di scarti tolte")
    if aperti:
        print("restano", len(aperti), "indirizzi senza stato finale")
    return 0


if __name__ == "__main__":
    sys.exit(main())
