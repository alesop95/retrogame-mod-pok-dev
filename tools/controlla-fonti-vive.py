#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controlla, a ogni apertura di sessione, se le fonti vive da cui dipendono i lotti di Bank sono cambiate.

Perché esiste
-------------
Il proprietario ha chiesto il 2026-11-04 che ogni fonte abbia un controllo che dica se si è aggiornata. Fino a quel
giorno il controllo esisteva per le sole cinque fonti degli eventi, in `tools/controlla-eventi-nuovi.py`. Le decisioni
ADR-108, ADR-109, ADR-110 e ADR-111 poggiano su altre fonti che cambiano nel tempo: le pagine di Bulbapedia sui
fiocchi, sulle sfide e sul Pokédex di HOME, i fogli comunitari sulla chiusura di Bank, i post di Reddit che li
collegano, i dati di ribbons.guide, la pagina delle sfide di Serebii e il manuale di Athis. Se una di queste cambia e
nessuno se ne accorge, l'elenco di produzione resta indietro in silenzio.

Che cosa sorveglia e come
-------------------------
L'elenco sta in `pokedex-home-completo/data/fonti-sorvegliate.json`, tracciato, insieme allo stato censito di ogni
fonte. Ogni tipo ha la sua misura, scelta perché non cambi da sola fra due letture identiche: per Bulbapedia il
numero di revisione dall'API, per un repository di GitHub l'ultimo commit, per un foglio di Google l'impronta dei
valori delle celle dell'esportazione, non del file, che porta date proprie; per un post di Reddit l'impronta del testo
e il numero di commenti come li conserva Arctic Shift, che è un archivio e può arrivare in ritardo; per una pagina web
l'impronta del testo senza marcatori. Le fonti che non cambiano, cioè video, tweet e fotografie dello schermo, e quelle
che da qui non si leggono, come PokéOS e IGN, sono elencate nel file con il motivo, così che l'assenza di un controllo
sia dichiarata e non dimenticata.

Una fonte che non risponde dice «non verificabile» ed esce con zero, come il controllo degli eventi: un controllo di
apertura non blocca una sessione, ma non fa passare il silenzio per un esito. A lettura fatta della fonte cambiata si
registra lo stato con `--segna`.

Uso
---
    python tools/controlla-fonti-vive.py            rapporto completo
    python tools/controlla-fonti-vive.py --breve    poche righe, per l'hook SessionStart
    python tools/controlla-fonti-vive.py --segna    fonti lette: tutte allo stato corrente
"""

import argparse
import datetime
import hashlib
import html
import io
import json
import os
import re
import sys
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRO = os.path.join(RADICE, "pokedex-home-completo", "data", "fonti-sorvegliate.json")
UA = "retrogame-mod-pok-dev (controllo fonti, sola lettura)"
BULBA_API = "https://bulbapedia.bulbagarden.net/w/api.php"
ARCTIC = "https://arctic-shift.photon-reddit.com/api/posts/ids?ids="


def scarica(url, timeout=20, binario=False):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=timeout) as r:
        dati = r.read()
    return dati if binario else dati.decode("utf-8", errors="replace")


def impronta(testo):
    return hashlib.sha256(testo.encode("utf-8")).hexdigest()[:16]


def misura(f):
    tipo, rif = f["tipo"], f["riferimento"]
    if tipo == "bulbapedia":
        q = urllib.parse.urlencode({"action": "query", "prop": "revisions", "rvprop": "ids|timestamp", "titles": rif,
                                    "format": "json"})
        p = next(iter(json.loads(scarica(BULBA_API + "?" + q))["query"]["pages"].values()))
        return "revisione %s del %s" % (p["revisions"][0]["revid"], p["revisions"][0]["timestamp"][:10])
    if tipo == "github":
        d = json.loads(scarica("https://api.github.com/repos/%s/commits?per_page=1" % rif))
        return "commit %s del %s" % (d[0]["sha"][:7], d[0]["commit"]["committer"]["date"][:10])
    if tipo == "foglio":
        import openpyxl
        dati = scarica("https://docs.google.com/spreadsheets/d/%s/export?format=xlsx" % rif, timeout=60, binario=True)
        wb = openpyxl.load_workbook(io.BytesIO(dati), read_only=True)
        h = hashlib.sha256()
        for ws in wb.worksheets:
            h.update(ws.title.encode("utf-8"))
            for riga in ws.iter_rows(values_only=True):
                h.update(repr(riga).encode("utf-8"))
        return "celle %s, %d schede" % (h.hexdigest()[:16], len(wb.worksheets))
    if tipo == "reddit":
        d = json.loads(scarica(ARCTIC + rif))["data"][0]
        return "testo %s, %d commenti" % (impronta(d.get("selftext", "")), d.get("num_comments", 0))
    if tipo == "pagina":
        testo = re.sub(r"<script.*?</script>|<style.*?</style>", " ", scarica(rif), flags=re.S | re.I)
        testo = html.unescape(re.sub(r"<[^>]+>", " ", testo))
        return "testo " + impronta(" ".join(testo.split()))
    raise ValueError("tipo sconosciuto: " + tipo)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--breve", action="store_true")
    ap.add_argument("--segna", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    reg = json.load(io.open(REGISTRO, encoding="utf-8"))
    cambiate, nuove, mute = [], [], []
    for f in reg["sorvegliate"]:
        try:
            ora = misura(f)
        except Exception as e:  # una fonte che non risponde non blocca, ma si dice
            mute.append("%s (%s)" % (f["nome"], type(e).__name__))
            continue
        if a.segna:
            f["censito"], f["segnato_il"] = ora, datetime.date.today().isoformat()
        elif not f.get("censito"):
            nuove.append("%s: %s" % (f["nome"], ora))
        elif f["censito"] != ora:
            cambiate.append("%s: era «%s», ora «%s» (%s)" % (f["nome"], f["censito"], ora, f["url"]))
    if a.segna:
        with io.open(REGISTRO, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(reg, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        print("Fonti vive: %d segnate allo stato corrente, %d non verificabili %s" %
              (len(reg["sorvegliate"]) - len(mute), len(mute), mute))
        return 0
    n = len(reg["sorvegliate"])
    if a.breve:
        print("=== Fonti vive dei lotti di Bank (tools/controlla-fonti-vive.py), %d sorvegliate ===" % n)
        if cambiate:
            print("CAMBIATE, da rileggere prima di produrre: " + "; ".join(cambiate))
        if nuove:
            print("Mai censite: %d, da segnare con --segna dopo averle lette." % len(nuove))
        if mute:
            print("Non verificabili ora: " + ", ".join(mute))
        if not (cambiate or nuove or mute):
            print("Nessuna fonte cambiata dall'ultimo censimento.")
        return 0
    print("Fonti sorvegliate: %d. Cambiate: %d. Mai censite: %d. Non verificabili: %d." %
          (n, len(cambiate), len(nuove), len(mute)))
    for r in cambiate + nuove + mute:
        print("  " + r)
    print("Senza controllo, con il motivo: %d fonti (vedi `non_sorvegliate` nel registro)." % len(reg["non_sorvegliate"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
