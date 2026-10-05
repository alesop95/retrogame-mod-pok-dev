#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trascrive fonti video con il riconoscimento vocale su una macchina con GPU della rete locale.

Perché esiste
-------------
La via economica per leggere un video è scaricarne i sottotitoli automatici con `yt-dlp` e
ripulirli con `tools/vtt-to-text.py`. Il 2026-09-29 YouTube ha negato i sottotitoli con risposte
429 ripetute anche a una lingua per video con pause di venti secondi, mentre l'audio si scaricava
senza errori. Questo strumento percorre quindi la seconda via della norma sulle fonti non
recuperabili: scarica il solo audio, lo trascrive con faster-whisper sulla GPU di un'altra
macchina, riporta il testo nel progetto con la sua provenienza, e cancella l'audio da entrambe le
macchine appena la trascrizione è su disco, perché un audio non si conserva e non pesa sul progetto.

Che cosa richiede
-----------------
Sulla macchina con GPU: un ambiente con faster-whisper, per esempio creato con
`python3 -m venv ~/trascrizione` e `~/trascrizione/bin/pip install faster-whisper
nvidia-cublas-cu12 'nvidia-cudnn-cu12==9.*'`. L'accesso è con chiave SSH: indirizzo e utente
arrivano dalle variabili d'ambiente GPU_HOST e GPU_USER, oppure da un alias in `~/.ssh/config`
passato come GPU_HOST, e nessuna password passa mai da qui. Sulla macchina locale: `yt-dlp` e il
client OpenSSH di sistema.

Uso
---
    python tools/trascrivi-video-gpu.py --uscita <cartella> --elenco <file con un id per riga>
    python tools/trascrivi-video-gpu.py --uscita <cartella> --id <id> [--id <id> ...]

Ogni trascrizione porta in testa la dichiarazione che non è riletta: i nomi propri e i numeri sono
ciò che il riconoscimento sbaglia, e si verificano sulla fonte prima di citarli.
"""

import argparse
import datetime
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

SSH = r"C:\Windows\System32\OpenSSH\ssh.exe" if os.name == "nt" else "ssh"
SCP = r"C:\Windows\System32\OpenSSH\scp.exe" if os.name == "nt" else "scp"
OPZIONI = ["-o", "BatchMode=yes", "-o", "ConnectTimeout=15"]
AMBIENTE = "~/trascrizione"
LAVORO = "~/trascrizione/lavoro"

# Gira sulla macchina con GPU. Le librerie CUDA installate con pip si dichiarano nel percorso
# prima di avviare Python, perché il caricatore le cerca all'avvio e non le rilegge dopo.
REMOTO = r'''
import json, os, sys, time
from faster_whisper import WhisperModel
modello = WhisperModel(os.environ.get("MODELLO", "large-v3"), device="cuda", compute_type="float16")
for audio in sys.argv[1:]:
    t0 = time.time()
    segmenti, info = modello.transcribe(audio, language=os.environ.get("LINGUA", "en"), vad_filter=True, beam_size=5)
    seg = [{"inizio": round(s.start, 2), "fine": round(s.end, 2), "testo": s.text.strip()} for s in segmenti]
    base = os.path.splitext(audio)[0]
    json.dump({"modello": os.environ.get("MODELLO", "large-v3"), "lingua": info.language,
               "durata": info.duration, "segmenti": seg}, open(base + ".json", "w", encoding="utf-8"), ensure_ascii=False)
    print("%s %.0fs di audio in %.0fs" % (os.path.basename(audio), info.duration, time.time() - t0), flush=True)
'''


def destinazione():
    host = os.environ.get("GPU_HOST")
    if not host:
        sys.exit("manca GPU_HOST: l'indirizzo o l'alias SSH della macchina con GPU")
    utente = os.environ.get("GPU_USER")
    return "%s@%s" % (utente, host) if utente else host


def ssh(dest, comando, timeout=3600):
    r = subprocess.run([SSH] + OPZIONI + [dest, comando], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    return r.returncode, r.stdout + r.stderr


def scp(sorgente, destinazione_file):
    r = subprocess.run([SCP] + OPZIONI + [sorgente, destinazione_file], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=1800)
    return r.returncode == 0


def scarica_audio(vid, cartella, url=None):
    """Il solo audio, con tre tentativi: il rifiuto 403 di YouTube sui formati è intermittente."""
    for tentativo in range(3):
        trovati = [x for x in glob.glob(os.path.join(cartella, vid + ".*")) if not x.endswith(".json")]
        if trovati:
            break
        r = subprocess.run([sys.executable, "-m", "yt_dlp", "-f", "ba[ext=m4a]/ba", "--write-info-json",
                            "-o", os.path.join(cartella, vid + ".%(ext)s"), url or ("https://www.youtube.com/watch?v=" + vid)],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            time.sleep(30)
    trovati = [x for x in glob.glob(os.path.join(cartella, vid + ".*")) if not x.endswith(".json")]
    info = os.path.join(cartella, vid + ".info.json")
    titolo = "?"
    if os.path.exists(info):
        titolo = json.load(open(info, encoding="utf-8")).get("title", "?")
        os.remove(info)
    return (trovati[0] if trovati else None), titolo


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--uscita", required=True, help="cartella del progetto dove scrivere le trascrizioni")
    ap.add_argument("--elenco", help="file con un identificativo di video per riga")
    ap.add_argument("--id", action="append", default=[], help="identificativo di un video")
    a = ap.parse_args()
    ids = list(a.id)
    indirizzi = {}
    if a.elenco:
        # Una riga porta l'identificativo e, facoltativo, l'indirizzo: senza indirizzo è un video di YouTube, con
        # l'indirizzo può essere un video di Twitch o di Reddit, che yt-dlp legge allo stesso modo.
        righe = [l.split() for l in open(a.elenco, encoding="utf-8") if l.strip()]
        ids += [r[0] for r in righe]
        indirizzi.update({r[0]: r[1] for r in righe if len(r) > 1})
    os.makedirs(a.uscita, exist_ok=True)
    dest = destinazione()
    rc, out = ssh(dest, "mkdir -p %s && ls %s/bin/python" % (LAVORO, AMBIENTE))
    if rc != 0:
        sys.exit("macchina con GPU non raggiungibile o ambiente mancante:\n" + out[-500:])
    temporanea = tempfile.mkdtemp(prefix="trascrivi-")
    script = os.path.join(temporanea, "trascrivi_remoto.py")
    open(script, "w", encoding="utf-8").write(REMOTO)
    if not scp(script, "%s:%s/trascrivi_remoto.py" % (dest, LAVORO)):
        sys.exit("impossibile copiare lo script sulla macchina con GPU")
    librerie = "$(ls -d %s/lib/python3*/site-packages/nvidia/*/lib | tr '\\n' ':')" % AMBIENTE
    fatti = falliti = 0
    try:
        for vid in ids:
            finale = os.path.join(a.uscita, vid + ".txt")
            if os.path.exists(finale):
                print(vid, "gia trascritto", flush=True)
                continue
            locale, titolo = scarica_audio(vid, temporanea, indirizzi.get(vid))
            if not locale:
                print(vid, "AUDIO NON SCARICATO", flush=True)
                falliti += 1
                continue
            nome = os.path.basename(locale)
            base = os.path.splitext(nome)[0]
            ok = scp(locale, "%s:%s/%s" % (dest, LAVORO, nome))
            os.remove(locale)
            if not ok:
                print(vid, "COPIA SULLA GPU FALLITA", flush=True)
                falliti += 1
                continue
            rc, esito = ssh(dest, "cd %s && export LD_LIBRARY_PATH=%s$LD_LIBRARY_PATH && %s/bin/python trascrivi_remoto.py %s"
                            % (LAVORO, librerie, AMBIENTE, nome))
            meta_locale = os.path.join(temporanea, base + ".json")
            ok = rc == 0 and scp("%s:%s/%s.json" % (dest, LAVORO, base), meta_locale)
            ssh(dest, "rm -f %s/%s %s/%s.json" % (LAVORO, nome, LAVORO, base))
            if not ok:
                print(vid, "TRASCRIZIONE FALLITA", esito[-400:], flush=True)
                falliti += 1
                continue
            meta = json.load(open(meta_locale, encoding="utf-8"))
            os.remove(meta_locale)
            testo = " ".join(s["testo"] for s in meta["segmenti"])
            testata = ("Trascrizione per riconoscimento vocale, NON riletta. Video %s, \"%s\". "
                       "Modello faster-whisper %s su GPU, lingua %s, durata %.0f secondi, trascritto il %s. "
                       "I nomi propri e i numeri sono ciò che il riconoscimento sbaglia: si verificano sulla fonte prima di citarli.\n\n"
                       % (indirizzi.get(vid, "https://www.youtube.com/watch?v=" + vid), titolo, meta["modello"], meta["lingua"], meta["durata"], datetime.date.today().isoformat()))
            open(finale, "w", encoding="utf-8").write(testata + testo + "\n")
            json.dump(meta, open(os.path.join(a.uscita, vid + ".segmenti.json"), "w", encoding="utf-8"), ensure_ascii=False)
            fatti += 1
            print(vid, esito.strip().split("\n")[-1], flush=True)
    finally:
        shutil.rmtree(temporanea, ignore_errors=True)
    print("trascritti %d, falliti %d" % (fatti, falliti), flush=True)
    return 1 if falliti else 0


if __name__ == "__main__":
    sys.exit(main())
