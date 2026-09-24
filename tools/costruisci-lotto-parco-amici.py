#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Applica la sintesi del Parco Amici (`pokebridge.parco_amici`) ai tre lotti Gen3 gia' prodotti.

Legge `_notes/lotti/lotto-eventi/`, `_notes/lotti/lotto-incontri-gen3/` e `_notes/lotti/lotto-scambi-gen3/`, converte
ogni voce nel record di scatola di quarta generazione equivalente a un vero passaggio dal Parco
Amici, ed esclude (senza correggere) le voci che portano una macchina nascosta di terza
generazione: la mossa e' spesso la ragione per cui l'esemplare e' un collezionabile, quindi
togliergliela e' una decisione dell'utente e non dello strumento. Scrive il lotto in
`_notes/lotti/lotto-parco-amici-gen4/` con un manifesto.

Superato il 2026-09-24 da ADR-082. Al primo giudizio con la libreria del verificatore, il lotto prodotto da
questa sintesi aveva 148 esemplari contestati su 203, mentre la conversione della libreria sugli stessi
esemplari ne dava 203 su 203. Il lotto si genera ora con `tools/pkhex-parco-amici`, e questo programma
resta soltanto come riferimento della sintesi di `pokebridge.parco_amici`: scrive in una cartella di prova
e rifiuta la destinazione del lotto.

Uso
---
    python tools/costruisci-lotto-parco-amici.py <cartella di prova>
"""
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.join("pokemon-gen12-gen3-bridge-original-hardware"))
sys.stdout.reconfigure(encoding="utf-8")

from pokebridge.gen3 import Gen3Mon
from pokebridge import parco_amici as PA

CARTELLE = ["_notes/lotti/lotto-eventi", "_notes/lotti/lotto-incontri-gen3", "_notes/lotti/lotto-scambi-gen3"]
# Per ADR-082 il lotto vero lo scrive tools/pkhex-parco-amici: qui si accetta solo una cartella di prova.
if len(sys.argv) != 2 or os.path.abspath(sys.argv[1]) == os.path.abspath("_notes/lotti/lotto-parco-amici-gen4"):
    sys.exit("uso: python tools/costruisci-lotto-parco-amici.py <cartella di prova>; "
             "il lotto del Parco Amici si genera con tools/pkhex-parco-amici (ADR-082)")
DESTINAZIONE = sys.argv[1]
os.makedirs(DESTINAZIONE, exist_ok=True)

scritti, esclusi, errori = [], [], []
impronte = {}

for cartella in CARTELLE:
    for nome in sorted(os.listdir(cartella)):
        if not nome.endswith(".pk3"):
            continue
        percorso = os.path.join(cartella, nome)
        dati = io.open(percorso, "rb").read()
        mon = Gen3Mon.from_canonical_bytes(dati[:80])
        try:
            esito = PA.converti(mon)
        except PA.MacchinaNascostaTrovata as e:
            esclusi.append({"file": nome, "cartella": cartella, "mossa": e.mossa})
            continue
        except Exception as e:
            errori.append({"file": nome, "cartella": cartella, "errore": str(e)})
            continue
        nome_out = os.path.splitext(nome)[0] + ".pk4"
        io.open(os.path.join(DESTINAZIONE, nome_out), "wb").write(esito.byte)
        scritti.append(nome_out)
        impronte[nome_out] = {
            "da": nome, "cartella_origine": cartella,
            "sha256": hashlib.sha256(esito.byte).hexdigest(),
            "gioco_di_origine": mon.misc.met_game,
            "luogo": PA.LUOGO_PARCO_AMICI,
            "da_uovo": esito.schiuso,
            "senza_soprannome": not esito.is_nicknamed,
            "soprannome": esito.soprannome_testo,
            "ot": esito.ot_testo,
        }

io.open(os.path.join(DESTINAZIONE, "manifesto.json"), "w", encoding="utf-8").write(
    json.dumps({
        "fonte": "PK3.ConvertToPK4 in _notes/fonti/cloni/pkhex/PKHeX.Core/PKM/PK3.cs, letto il 2026-09-16",
        "stato": "prodotto, in attesa del giudizio esterno",
        "escluse_macchina_nascosta": esclusi,
        "errori": errori,
        "voci": impronte,
    }, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
)

print("scritti:", len(scritti))
print("esclusi per macchina nascosta:", len(esclusi))
for e in esclusi:
    print("  ", e["cartella"], e["file"], "mossa", e["mossa"])
print("errori:", len(errori))
for e in errori[:10]:
    print("  ", e["cartella"], e["file"], e["errore"])
