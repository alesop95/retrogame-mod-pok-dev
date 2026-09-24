#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confronta l'impronta di fine sessione con lo stato reale di git.

Perche' esiste
--------------
`_notes/resume-prompt.md` descrive lo stato del progetto a fine sessione, ma una
sessione che cade a meta' (limite di utilizzo, crash, chiusura della finestra) lascia
quel file a descrivere un passato che non e' piu' il presente. Il 2026-09-21 e' successo
davvero: il resume-prompt dichiarava un commit "non ancora fatto" quando quel commit
era gia' HEAD. Questo strumento rende meccanica la verifica invece di affidarla alla
lettura sola del file.

Uso
---
    python tools/verifica-ripresa.py             legge l'impronta e la confronta con HEAD
    python tools/verifica-ripresa.py --registra  scrive l'impronta corrente

L'impronta vive in `_notes/lavoro/stato/impronta-sessione.json`, non tracciato: e' un presidio
locale di macchina, non uno stato condiviso da versionare.
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
IMPRONTA_PATH = REPO_ROOT / "_notes" / "lavoro" / "stato" / "impronta-sessione.json"


def git(*args):
    result = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    )
    return result.stdout.strip()


def registra():
    head = git("rev-parse", "HEAD")
    status = git("status", "--short")
    impronta = {
        "commit": head,
        "status": status,
        "registrato_il": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    IMPRONTA_PATH.parent.mkdir(parents=True, exist_ok=True)
    IMPRONTA_PATH.write_text(
        json.dumps(impronta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"impronta registrata: {head[:7]}, albero {'sporco' if status else 'pulito'}")


def verifica():
    if not IMPRONTA_PATH.exists():
        print("nessuna impronta registrata: prima esecuzione, o sessione precedente all'adozione di questo strumento.")
        print("confronto a mano: leggere il commit dichiarato in .claude/memory/index.md e confrontarlo con HEAD.")
        return 2

    impronta = json.loads(IMPRONTA_PATH.read_text(encoding="utf-8"))
    commit_registrato = impronta["commit"]
    status_registrato = impronta["status"]
    head_attuale = git("rev-parse", "HEAD")
    status_attuale = git("status", "--short")

    divergenze = False

    if commit_registrato != head_attuale:
        divergenze = True
        try:
            log = git("log", "--oneline", f"{commit_registrato}..{head_attuale}")
        except subprocess.CalledProcessError:
            log = "(il commit registrato non e' un antenato di HEAD: verificare a mano, potrebbe essere un reset o un rebase)"
        print(f"COMMIT DIVERGENTE: registrato {commit_registrato[:7]}, HEAD attuale {head_attuale[:7]}.")
        print("Commit comparsi dopo la registrazione (lavoro fatto da una sessione che non ha chiuso bene):")
        print(log if log else "(nessuno: HEAD e' precedente al registrato, verificare a mano)")
    else:
        print(f"Commit invariato dalla registrazione: {head_attuale[:7]}.")

    if status_attuale != status_registrato:
        divergenze = True
        print("ALBERO DI LAVORO DIVERSO da quello registrato a fine sessione:")
        print(f"  registrato: {status_registrato or '(pulito)'}")
        print(f"  attuale:    {status_attuale or '(pulito)'}")
    else:
        print(f"Albero di lavoro invariato: {'pulito' if not status_attuale else 'sporco, come alla registrazione'}.")

    print(f"(impronta registrata il {impronta['registrato_il']})")

    return 1 if divergenze else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--registra", action="store_true", help="scrive l'impronta corrente invece di verificarla")
    args = parser.parse_args()

    if args.registra:
        registra()
        return 0
    return verifica()


if __name__ == "__main__":
    sys.exit(main())
