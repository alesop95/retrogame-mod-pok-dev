#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legge il testo delle immagini del corpus della collezione con il riconoscimento ottico dei caratteri.

Perché esiste
-------------
Fra i collegamenti del corpus che il censimento aveva soltanto catalogato, circa trecento sono immagini: schermate di
elenchi di eventi, tabelle, caselle di HOME, anteprime di Reddit e di Imgur. `tools/leggi-residuo-corpus.py` le scarica
in `_notes/fonti/corpus-residuo/immagini/`, e questo strumento ne estrae il testo con RapidOCR, in locale e senza token.
Il 2026-10-01 il modello di visione di Ollama non si è potuto scaricare sul server, per un permesso della cartella dei
modelli; il riconoscimento ottico copre la parte che conta di più, cioè il testo scritto nelle schermate, e le immagini
da cui esce poco testo si elencano a parte, perché un modello di visione le descriva quando sarà disponibile.

Uso
---
    python tools/leggi-immagini-corpus.py
"""

import io
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA = os.path.join(RADICE, "_notes", "fonti", "corpus-residuo")
IMMAGINI = os.path.join(CARTELLA, "immagini")
USCITA = os.path.join(CARTELLA, "immagini-testo")
POCO_TESTO = 40


def main():
    from PIL import Image
    from rapidocr_onnxruntime import RapidOCR
    motore = RapidOCR()
    os.makedirs(USCITA, exist_ok=True)
    esiti = json.load(io.open(os.path.join(CARTELLA, "esiti.json"), encoding="utf-8"))
    origine = {v["file"]: u for u, v in esiti.items() if v.get("esito") == "immagine"}
    scarse = []
    for nome in sorted(os.listdir(IMMAGINI)):
        dest = os.path.join(USCITA, os.path.splitext(nome)[0] + ".md")
        if os.path.exists(dest):
            continue
        percorso = os.path.join(IMMAGINI, nome)
        try:
            with Image.open(percorso) as im:
                im.seek(0)
                rgb = im.convert("RGB")
                temporaneo = os.path.join(USCITA, "_corrente.png")
                rgb.save(temporaneo)
            risultato, _ = motore(temporaneo)
            righe = [r[1] for r in (risultato or [])]
        except Exception as e:
            righe = ["(immagine non leggibile: %s)" % e]
        testo = "\n".join(righe)
        io.open(dest, "w", encoding="utf-8").write("<!-- %s; %s -->\n%s\n" % (nome, origine.get(nome, "da un album"), testo))
        if len(testo) < POCO_TESTO:
            scarse.append(nome)
        print(nome, len(testo), flush=True)
    io.open(os.path.join(CARTELLA, "immagini-poco-testo.txt"), "a", encoding="utf-8").write("".join(n + "\n" for n in scarse))
    print("FINE", flush=True)


if __name__ == "__main__":
    sys.exit(main())
