#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone le schede tecniche dei repository di codice citati dalle fonti in un documento.

Perché esiste
-------------
Il proprietario ha chiesto il 2026-10-07 che tutte le fonti con codice compaiano con una
descrizione tecnica, perché il lavoro analizza il web e vale come portfolio. Le descrizioni si
scrivono leggendo README e metadati di ciascun repository, raccolti da
`tools/raccogli-fonti-codice.py`, e stanno in `_notes/fonti/raccolte/fonti-codice/schede-*.json`.
Questo strumento le unisce ai dati del censimento (`tools/censimento-fonti-codice.py`) e scrive
`docs/fonti-codice-schede.md`, una scheda per repository, raggruppate per track del progetto, con
l'indirizzo, i metadati, che cosa è, come funziona, la relazione con il progetto e ciò che la
scheda non ha potuto accertare. Rifiuta di scrivere se una scheda manca o se una scheda nomina un
repository che il censimento non conosce, così il documento non può dirsi completo quando non lo è.

Uso
---
    python tools/schede-fonti-codice.py            # scrive docs/fonti-codice-schede.md
    python tools/schede-fonti-codice.py --check    # esce con 1 se il documento è da rigenerare
"""

import argparse
import glob
import importlib.util
import io
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACCOLTA = os.path.join(RADICE, "_notes", "fonti", "raccolte", "fonti-codice")
USCITA = os.path.join(RADICE, "docs", "fonti-codice-schede.md")
TRACK = [
    ("PKD", "Pokédex completo in HOME"), ("EVT", "Distribuzioni di eventi"), ("SME", "Salvataggio di Smeraldo"),
    ("BRI", "Ponte fra generazioni su hardware originale"), ("3DS", "Modding del 3DS"), ("LDN", "Scambio fra GBA e Switch"),
    ("ACE", "Esecuzione di codice"), ("AUT", "Automazione su Switch"), ("BAT", "Pila tampone"),
]


def carica_censimento():
    spec = importlib.util.spec_from_file_location("censimento", os.path.join(RADICE, "tools", "censimento-fonti-codice.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m, m.censisci()


def documento():
    m, repo = carica_censimento()
    schede = {}
    for f in sorted(glob.glob(os.path.join(RACCOLTA, "schede-*.json"))):
        for s in json.load(io.open(f, encoding="utf-8")):
            schede[s["nome"].lower()] = s
    attesi = {k for k in repo if k != "wiki/flagbrew"}
    mancanti = sorted(attesi - set(schede))
    estranee = sorted(set(schede) - attesi)
    if mancanti or estranee:
        sys.exit(f"schede mancanti {mancanti}, schede estranee {estranee}: il documento non si scrive")
    gruppi = {sigla: [] for sigla, _ in TRACK}
    gruppi["altro"] = []
    for k in sorted(attesi, key=lambda x: repo[x]["nome"].lower()):
        tracks = [t for t, _ in TRACK if t in repo[k]["track"]] or (["altro"])
        gruppi[tracks[0]].append(k)
    righe = [
        "# Le fonti con codice, scheda per scheda",
        "",
        "> Documento generato da `tools/schede-fonti-codice.py` dalle schede scritte leggendo README e metadati "
        "di ciascun repository, raccolti da `tools/raccogli-fonti-codice.py`. Non si modifica a mano: si correggono "
        "le schede e si rigenera. Il censimento con i dati di uso è `docs/censimento-fonti-codice.md`, il giudizio su "
        "che cosa ciascuna fonte può aggiungere agli strumenti è `docs/potenziamento-dalle-fonti.md`.",
        "",
        f"Repository descritti: {len(attesi)}, raggruppati per il primo track del progetto che li cita; quelli che il "
        "registro non associa a un track stanno in fondo. La riga dei metadati dice linguaggio, licenza, data dell'ultimo "
        "aggiornamento e stato, letti dall'API di GitHub il giorno della raccolta. Una scheda dice su che cosa poggia, e ciò "
        "che non ha potuto accertare è scritto, non taciuto.",
        "",
    ]
    for sigla, titolo in TRACK + [("altro", "Senza track dichiarato nel registro")]:
        if not gruppi[sigla]:
            continue
        righe += [f"## {titolo}" + (f" ({sigla})" if sigla != "altro" else ""), ""]
        for k in gruppi[sigla]:
            v, s = repo[k], schede[k]
            md = m.metadati(v["nome"]) or {"linguaggio": "non raccolto", "licenza": "-", "aggiornato": "-", "stato": "-"}
            url = f"https://github.com/{v['nome']}" if not (len(k.split('/')[1]) == 32) else f"https://gist.github.com/{v['nome']}"
            righe += [
                f"### `{v['nome']}`",
                "",
                f"{url} · {md['linguaggio']} · licenza {md['licenza']} · aggiornato {md['aggiornato'] or '-'} · {md['stato']} · "
                f"track {', '.join(sorted(v['track'])) or '-'} · {'usato dal codice del progetto' if v['codice'] else 'non usato dal codice del progetto'} · "
                f"scheda da {s['basato_su']}",
                "",
                f"Che cosa è. {s['che_cosa_e']}",
                "",
                f"Come funziona. {s['come_funziona']}",
                "",
                f"Relazione con il progetto. {s['relazione_col_progetto']}",
                "",
            ]
            if s.get("da_verificare"):
                righe += [f"Da verificare. {s['da_verificare']}", ""]
    return "\n".join(righe).rstrip("\n") + "\n"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    testo = documento()
    vecchio = io.open(USCITA, encoding="utf-8").read() if os.path.exists(USCITA) else None
    if a.check:
        print("allineato" if vecchio == testo else "da rigenerare")
        return 0 if vecchio == testo else 1
    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    print(f"scritto {USCITA}: {testo.count(chr(10) + '### ')} schede")
    return 0


if __name__ == "__main__":
    sys.exit(main())
