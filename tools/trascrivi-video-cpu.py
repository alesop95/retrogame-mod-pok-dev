#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trascrive in locale, sul processore, l'audio dei video che non hanno sottotitoli.

Perché esiste
-------------
Il 2026-10-05 tre video del registro delle fonti non avevano sottotitoli di alcun tipo, e per questi la trascrizione
non la può procurare nemmeno il proprietario, perché il pulsante della trascrizione nella pagina del video esiste solo
dove esistono i sottotitoli. La macchina con scheda grafica del vecchio `tools/trascrivi-video-gpu.py`, rimosso il 2026-10-06 e recuperabile dalla storia git, è dismessa dal
2026-10-02, quindi la trascrizione si fa su questa macchina, sul processore, con `faster-whisper` e il modello piccolo:
per video di qualche minuto il costo è di minuti. Lo script nasce nella cartella temporanea della sessione e vive qui
perché lì una pulizia lo avrebbe cancellato.

Che cosa fa
-----------
Per ogni identificativo scarica il solo audio con `yt-dlp` nella cartella di lavoro, lo decodifica con `ffmpeg` in un
flusso a 16 kHz mono e passa i campioni al modello. La decodifica con `ffmpeg` non è un dettaglio: la libreria di
decodifica che `faster-whisper` usa per aprire un file, PyAV, in una versione incompatibile fallisce con un errore
sull'argomento `metadata_errors`, e passare i campioni aggira il problema. Scrive `<cartella>/testo/<id>.txt`, salta
gli identificativi che hanno già il testo, e cancella l'audio a trascrizione scritta, perché un audio non si conserva.
La trascrizione non è riletta: nomi propri e numeri sono ciò che il riconoscimento sbaglia, e si verificano sul video
prima di citarli.

Uso
---
    python tools/trascrivi-video-cpu.py --cartella _notes/fonti/consegne/<data>-video-locali inMbtwmVlKQ aQWsNIWu3FQ
    python tools/trascrivi-video-cpu.py --cartella <cartella> --lingua it --modello small <id> ...
"""

import argparse
import os
import subprocess
import sys


def scarica_audio(vid, cartella):
    uscita = os.path.join(cartella, vid + ".mp3")
    if not os.path.exists(uscita):
        subprocess.run([sys.executable, "-m", "yt_dlp", "-f", "ba", "-x", "--audio-format", "mp3",
                        "-o", os.path.join(cartella, "%(id)s.%(ext)s"), "https://www.youtube.com/watch?v=" + vid],
                       check=True, capture_output=True)
    return uscita


def campioni(percorso):
    import numpy as np
    grezzo = subprocess.run(["ffmpeg", "-v", "quiet", "-i", percorso, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                            capture_output=True, check=True).stdout
    return np.frombuffer(grezzo, np.int16).astype(np.float32) / 32768


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("id", nargs="+", help="identificativi dei video")
    ap.add_argument("--cartella", required=True, help="cartella di lavoro, ignorata da git")
    ap.add_argument("--lingua", default="en")
    ap.add_argument("--modello", default="small")
    a = ap.parse_args()
    from faster_whisper import WhisperModel
    os.makedirs(os.path.join(a.cartella, "testo"), exist_ok=True)
    modello = WhisperModel(a.modello, device="cpu", compute_type="int8")
    for vid in a.id:
        testo = os.path.join(a.cartella, "testo", vid + ".txt")
        if os.path.exists(testo):
            print(vid, "già trascritto")
            continue
        audio = scarica_audio(vid, a.cartella)
        segmenti, _ = modello.transcribe(campioni(audio), language=a.lingua, vad_filter=True)
        t = " ".join(s.text.strip() for s in segmenti)
        open(testo, "w", encoding="utf-8").write(t)
        os.remove(audio)
        print(vid, len(t.split()), "parole")
    return 0


if __name__ == "__main__":
    sys.exit(main())
