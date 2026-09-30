#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Estrae da trascrizioni di video le affermazioni pertinenti con un modello locale servito da Ollama.

Perché esiste
-------------
Le fonti video consegnate per il Pokédex completo sono decine di trascrizioni da migliaia di parole,
per la maggior parte chiacchiera. Leggerle tutte con l'agente consuma token su testo che non serve;
un modello locale sulla macchina con GPU della rete le riduce alle sole affermazioni su specie, forme,
esemplari, metodi e vincoli della catena, senza costo di token. L'estratto è un filtro e non una fonte:
ogni affermazione che cambia lo stato del progetto si verifica sulla trascrizione e sul verificatore
prima di essere scritta, perché un modello da quattordici miliardi di parametri sbaglia nomi e numeri.

Lo stato intermedio sta accanto alle trascrizioni, in una cartella `estratti/`, e non in una cartella
temporanea: il 2026-09-30 una pulizia della cartella di sessione ha cancellato un primo giro di estratti.
Un video già estratto non si rifà, quindi il lavoro è riprendibile.

Uso
---
    python tools/estrai-affermazioni-ollama.py --testi <cartella delle trascrizioni> --elenco <file con un id per riga>

L'indirizzo del servizio viene da OLLAMA_URL, per esempio http://<host>:<porta>, e il modello da
OLLAMA_MODELLO, con qwen3:14b come valore predefinito.
"""

import argparse
import json
import os
import sys
import urllib.request

ISTRUZIONE = """You are extracting facts from an auto-generated YouTube transcript about Pokemon Bank closing (Feb 2027).
List EVERY concrete claim about: a species, form, or specific Pokemon (event, gift, in-game trade, special trainer/OT/ID, ball, move, ribbon, mark) that someone should obtain or transfer before Bank closes; a method (DNS exploit, QR code, demo, Virtual Console, Pokewalker, Ranch, Dream Radar, Ranger, Colosseum/XD, Stadium, glitch, RNG); a transfer limitation (something that cannot go to HOME, or only via Bank). Skip chatter, greetings, sponsors, personal anecdotes without a fact.
Output one line per claim, format: - <claim in English, with game names and species names corrected to their official spelling>
If there are no such claims, output: - NONE
Transcript:
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--testi", required=True, help="cartella delle trascrizioni <id>.txt")
    ap.add_argument("--elenco", required=True, help="file con un identificativo di video per riga")
    a = ap.parse_args()
    url = os.environ.get("OLLAMA_URL")
    if not url:
        sys.exit("manca OLLAMA_URL, l'indirizzo del servizio Ollama")
    modello = os.environ.get("OLLAMA_MODELLO", "qwen3:14b")
    uscita = os.path.join(a.testi, "..", "estratti")
    os.makedirs(uscita, exist_ok=True)
    ids = [l.strip() for l in open(a.elenco, encoding="utf-8") if l.strip()]
    for vid in ids:
        dest = os.path.join(uscita, vid + ".txt")
        if os.path.exists(dest):
            continue
        testo = open(os.path.join(a.testi, vid + ".txt"), encoding="utf-8").read()
        corpo = json.dumps({"model": modello, "prompt": ISTRUZIONE + testo + "\n/no_think", "stream": False,
                            "options": {"num_ctx": 16384, "temperature": 0}}).encode()
        richiesta = urllib.request.Request(url.rstrip("/") + "/api/generate", corpo, {"Content-Type": "application/json"})
        risposta = json.loads(urllib.request.urlopen(richiesta, timeout=1800).read())["response"]
        risposta = risposta.split("</think>")[-1].strip()
        with open(dest, "w", encoding="utf-8") as f:
            f.write("Estratto di %s dalla trascrizione %s.txt con il modello %s. È un filtro e non una fonte: "
                    "si verifica sulla trascrizione prima di citarlo.\n\n%s\n" % (vid, vid, modello, risposta))
        print(vid, len(testo.split()), "parole ->", len(risposta.splitlines()), "righe", flush=True)
    print("FINE", flush=True)


if __name__ == "__main__":
    main()
