#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica sulle copie della collezione le distribuzioni che gli estratti del corpus nominano con allenatore e ID.

Perché esiste
-------------
Gli estratti di Ollama dal residuo del corpus, letto il 2026-10-01, sono in gran parte elenchi di distribuzioni con il
nome dell'allenatore originale e l'identificativo, presi dalle liste di Bulbapedia. Rileggerli a mano uno per uno
consuma token e sbaglia; la domanda che pongono è deterministica: quella distribuzione è in una delle nostre copie? Lo
strumento estrae dagli estratti ogni coppia allenatore e ID con la specie della stessa riga, e la cerca fra gli
esemplari di `_notes/stampa/collezione.json`, per specie, allenatore senza distinzione di maiuscole e ID a cinque cifre.

Che cosa fa
-----------
Scrive in `_notes/fonti/corpus-residuo/verifica-ot-id.md` le coppie trovate e quelle non trovate. Le non trovate sono le
candidate a lacuna, da controllare sul registro dei doni segreti del progetto: una distribuzione può mancare dalle copie
perché la libreria la respinge, perché è nel gruppo a parte, o perché l'estratto ha sbagliato un numero.

Uso
---
    python tools/verifica-affermazioni-corpus.py
"""

import collections
import glob
import io
import json
import os
import re

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA = os.path.join(RADICE, "_notes", "fonti", "corpus-residuo")
COPIE = os.path.join(RADICE, "_notes", "stampa", "collezione.json")
NOMI_EN = os.path.join(RADICE, "_notes", "fonti", "cloni", "pkhex", "PKHeX.Core", "Resources", "text", "other", "en",
                       "text_Species_en.txt")
COPPIA = re.compile(r"OT[:\s]+[\"“]?([A-Za-z0-9.&'\-ァ-ヶぁ-んー一-龯]{2,12})[\"”]?[\s,]+(?:and\s+)?(?:Trainer\s+)?ID(?:\s+No\.)?[:\s]+[\"“]?(\d{4,6})")


def main():
    nomi = [r.rstrip("\r") for r in io.open(NOMI_EN, encoding="utf-8").read().split("\n")]
    per_nome = sorted(((n, i) for i, n in enumerate(nomi) if i and n), key=lambda x: -len(x[0]))
    nostre = collections.defaultdict(list)
    for c in json.load(io.open(COPIE, encoding="utf-8"))["copie"]:
        for e in c["esemplari"]:
            nostre[(e["numero"], str(e["allenatore"]).lower(), int(e["id"]))].append(c["gruppo"] + " / " + c["copia"])
    estratti = glob.glob(os.path.join(CARTELLA, "estratti", "*.txt")) + glob.glob(os.path.join(CARTELLA, "video*", "estratti", "*.txt"))
    trovate, mancanti = {}, {}
    for f in estratti:
        for riga in io.open(f, encoding="utf-8").read().splitlines():
            for m in COPPIA.finditer(riga):
                specie = next((i for n, i in per_nome if re.search(r"\b%s\b" % re.escape(n), riga)), None)
                if not specie:
                    continue
                chiave = (specie, m.group(1).lower(), int(m.group(2)))
                if chiave in nostre:
                    trovate[chiave] = nostre[chiave][0]
                else:
                    mancanti.setdefault(chiave, (os.path.basename(f), riga.strip()[:200]))
    r = ["# Distribuzioni con allenatore e ID nominate dal corpus, verificate sulle copie", "",
         "> Generato da `tools/verifica-affermazioni-corpus.py` dagli estratti in `_notes/fonti/corpus-residuo/`.", "",
         "Coppie trovate nelle copie: %d. Non trovate: %d." % (len(trovate), len(mancanti)), "",
         "## Non trovate", "", "| Specie | Allenatore | ID | Estratto | Riga |", "|---|---|---|---|---|"]
    for (s, ot, tid), (f, riga) in sorted(mancanti.items()):
        r.append("| %s | %s | %05d | %s | %s |" % (nomi[s], ot, tid, f, riga.replace("|", "/")))
    r += ["", "## Trovate", "", "| Specie | Allenatore | ID | Copia |", "|---|---|---|---|"]
    for (s, ot, tid), dove in sorted(trovate.items()):
        r.append("| %s | %s | %05d | %s |" % (nomi[s], ot, tid, dove))
    io.open(os.path.join(CARTELLA, "verifica-ot-id.md"), "w", encoding="utf-8").write("\n".join(r) + "\n")
    print("trovate", len(trovate), "non trovate", len(mancanti))


if __name__ == "__main__":
    main()
