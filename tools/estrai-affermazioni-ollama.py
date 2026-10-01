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


ISTRUZIONE_CHAT = """You are extracting facts from messages of a Pokemon development Discord channel, filtered for keywords about Pokemon Bank, HOME, transfers and event distributions.
List EVERY concrete claim relevant to building a complete Pokemon HOME collection before Pokemon Bank closes (Feb 2027): a specific event, distribution, gift or in-game Pokemon that cannot be obtained otherwise; a legality rule (what HOME, Bank, Poke Transporter or Pal Park accept or reject, and why); a known bug or glitch that makes a Pokemon illegal or untransferable; a method to obtain or transfer something. Skip code discussion, ROM hacking, greetings and anything about disassembly work.
Output one line per claim, format: - <claim in English> (author, date if present)
If there are no such claims, output: - NONE
Messages:
"""
ISTRUZIONE_PAGINE = """You are extracting facts from a web page, a Reddit thread with its comments, a spreadsheet or the OCR text of an image, collected from a community guide about completing a Pokemon HOME living dex before Pokemon Bank closes (Feb 2027).
List EVERY concrete claim relevant to a complete collection: a species or form (female, cosmetic, regional, event-only) and how it is obtained; a specific event, distribution, gift, in-game trade or special trainer/OT/ID; a Pokemon or form that can reach HOME only through Bank, or cannot reach HOME at all; a legality rule or a known bug; a method (DNS exploit, QR code, demo, Virtual Console, Pokewalker, Ranch, Dream Radar, Ranger, Colosseum/XD, Stadium, glitch, RNG). Skip navigation text, greetings, shiny-hunting odds, team building and anything not about obtaining or transferring.
Output one line per claim, format: - <claim in English> (author if present)
If there are no such claims, output: - NONE
Text:
"""
PEZZO = 20000


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--testi", required=True, help="cartella delle trascrizioni <id>.txt")
    ap.add_argument("--elenco", required=True, help="file con un identificativo di video per riga")
    ap.add_argument("--chat", action="store_true",
                    help="i testi sono chat ridotte in Markdown, <nome>.md: istruzione per le chat e testi divisi in pezzi")
    ap.add_argument("--pagine", action="store_true",
                    help="i testi sono pagine, thread o testo di immagini, <nome>.md: istruzione per le pagine e testi divisi in pezzi")
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
        estensione = ".md" if (a.chat or a.pagine) else ".txt"
        testo = open(os.path.join(a.testi, vid + estensione), encoding="utf-8").read()
        # Le chat filtrate possono superare la finestra del modello: si dividono in pezzi a confine di riga.
        pezzi, corrente = [], ""
        for riga in testo.splitlines(keepends=True):
            if (a.chat or a.pagine) and corrente and len(corrente) + len(riga) > PEZZO:
                pezzi.append(corrente)
                corrente = ""
            corrente += riga
        pezzi.append(corrente)
        risposte = []
        for pezzo in pezzi:
            corpo = json.dumps({"model": modello, "prompt": (ISTRUZIONE_PAGINE if a.pagine else ISTRUZIONE_CHAT if a.chat else ISTRUZIONE) + pezzo + "\n/no_think",
                                "stream": False,
                                "options": {"num_ctx": 16384, "temperature": 0, "num_predict": 2000, "repeat_penalty": 1.15}}).encode()
            richiesta = urllib.request.Request(url.rstrip("/") + "/api/generate", corpo, {"Content-Type": "application/json"})
            r = json.loads(urllib.request.urlopen(richiesta, timeout=1800).read())["response"]
            risposte.append(r.split("</think>")[-1].strip())
        risposta = "\n".join(risposte)
        with open(dest, "w", encoding="utf-8") as f:
            f.write("Estratto di %s dal testo %s%s con il modello %s. È un filtro e non una fonte: "
                    "si verifica sul testo prima di citarlo.\n\n%s\n" % (vid, vid, estensione, modello, risposta))
        print(vid, len(testo.split()), "parole ->", len(risposta.splitlines()), "righe", flush=True)
    print("FINE", flush=True)


if __name__ == "__main__":
    main()
