#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Raccoglie metadati e README dei repository di codice citati in SOURCES.md.

Perché esiste
-------------
Il censimento delle fonti con codice (ADR-100, `tools/censimento-fonti-codice.py`) dice quali
repository il registro cita e quali il progetto usa, ma non che cosa siano. Il proprietario ha
chiesto il 2026-10-07 che compaiano tutte, ciascuna con una descrizione tecnica, perché il lavoro
analizza il web e vale come portfolio. Le descrizioni si scrivono leggendo, e leggere 110
repository a mano dal browser non si ripete; questo strumento fa la parte che si ripete: per ogni
repository interroga l'API di GitHub con la CLI `gh` autenticata, e salva in
`_notes/fonti/raccolte/fonti-codice/<proprietario>__<nome>/` i metadati (`repo.json`) e il README
(`README.md`), oppure, per un gist, il gist (`gist.json`). La cartella è fuori da Git: sono copie
di testi di terzi.

È riprendibile: un repository già raccolto non si richiede di nuovo, salvo con `--forza`. Un
repository che non risponde, perché rimosso, rinominato o privato, si registra in
`esiti.json` con il codice d'errore invece di sparire dal conto. Non scrive nulla su GitHub.

Uso
---
    python tools/raccogli-fonti-codice.py            # raccoglie ciò che manca
    python tools/raccogli-fonti-codice.py --forza    # raccoglie tutto di nuovo
"""

import argparse
import base64
import importlib.util
import io
import json
import os
import subprocess
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA = os.path.join(RADICE, "_notes", "fonti", "raccolte", "fonti-codice")


def censimento():
    spec = importlib.util.spec_from_file_location("censimento", os.path.join(RADICE, "tools", "censimento-fonti-codice.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.censisci()


def gh(percorso):
    r = subprocess.run(["gh", "api", percorso], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        return None, (r.stderr.strip().splitlines() or ["errore"])[-1][:200]
    return json.loads(r.stdout), None


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--forza", action="store_true")
    a = ap.parse_args()
    os.makedirs(CARTELLA, exist_ok=True)
    percorso_esiti = os.path.join(CARTELLA, "esiti.json")
    esiti = json.load(io.open(percorso_esiti, encoding="utf-8")) if os.path.exists(percorso_esiti) else {}
    conto = {"raccolti": 0, "già presenti": 0, "non raggiungibili": 0}
    for k, v in censimento().items():
        proprietario, nome = v["nome"].split("/", 1)
        dest = os.path.join(CARTELLA, f"{proprietario}__{nome}")
        if os.path.isdir(dest) and not a.forza and esiti.get(k, {}).get("esito") == "raccolto":
            conto["già presenti"] += 1
            continue
        os.makedirs(dest, exist_ok=True)
        if len(nome) == 32 and all(c in "0123456789abcdef" for c in nome.lower()):
            dati, errore = gh(f"gists/{nome}")
            if dati:
                io.open(os.path.join(dest, "gist.json"), "w", encoding="utf-8").write(json.dumps(dati, ensure_ascii=False, indent=1))
        else:
            dati, errore = gh(f"repos/{proprietario}/{nome}")
            if dati:
                io.open(os.path.join(dest, "repo.json"), "w", encoding="utf-8").write(json.dumps(dati, ensure_ascii=False, indent=1))
                readme, _ = gh(f"repos/{proprietario}/{nome}/readme")
                if readme and readme.get("content"):
                    testo = base64.b64decode(readme["content"]).decode("utf-8", errors="replace")
                    io.open(os.path.join(dest, "README.md"), "w", encoding="utf-8").write(testo)
        if dati:
            esiti[k] = {"esito": "raccolto", "nome": v["nome"]}
            conto["raccolti"] += 1
        else:
            esiti[k] = {"esito": "non raggiungibile", "nome": v["nome"], "errore": errore}
            conto["non raggiungibili"] += 1
            print(f"non raggiungibile: {v['nome']}: {errore}")
        io.open(percorso_esiti, "w", encoding="utf-8").write(json.dumps(esiti, ensure_ascii=False, indent=1))
    print(", ".join(f"{n} {c}" for n, c in conto.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
