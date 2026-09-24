# -*- coding: utf-8 -*-
"""Aggiorna l'indice pubblico dei sottoprogetti e verifica i link locali del README."""

import argparse
import pathlib
import re
import sys


RADICE = pathlib.Path(__file__).resolve().parents[1]
README = RADICE / "README.md"
INIZIO = "<!-- indice-pubblico:inizio -->"
FINE = "<!-- indice-pubblico:fine -->"
ESCLUSE = {"docs", "tesi", "tools", "_notes"}


def sottoprogetti():
    righe = []
    for cartella in sorted(RADICE.iterdir(), key=lambda p: p.name.casefold()):
        if not cartella.is_dir() or cartella.name.startswith(".") or cartella.name in ESCLUSE:
            continue
        ingresso = cartella / "README.md"
        if not ingresso.is_file():
            continue
        prima = ingresso.read_text(encoding="utf-8").splitlines()[0]
        if not prima.startswith("# "):
            raise ValueError("Titolo mancante: " + str(ingresso))
        titolo = prima[2:].removeprefix("Sottoprogetto: ").replace("|", "\\|")
        righe.append((cartella.name, titolo))
    if not righe:
        raise ValueError("Nessun sottoprogetto trovato")
    return righe


def blocco():
    righe = [INIZIO, "## Sottoprogetti", "", "| Area | Punto di ingresso |", "|---|---|"]
    for nome, titolo in sottoprogetti():
        righe.append(f"| `{nome}/` | [{titolo}]({nome}/README.md) |")
    righe.extend([FINE])
    return "\n".join(righe)


def verifica_link(testo):
    mancanti = []
    for indirizzo in re.findall(r"\]\(([^)]+)\)", testo):
        if indirizzo.startswith(("#", "https://", "http://", "mailto:")):
            continue
        percorso = indirizzo.split("#", 1)[0]
        if percorso and not (RADICE / percorso).exists():
            mancanti.append(percorso)
    return sorted(set(mancanti))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true", help="verifica senza scrivere")
    a = p.parse_args(argv)
    testo = README.read_text(encoding="utf-8")
    if testo.count(INIZIO) != 1 or testo.count(FINE) != 1:
        raise ValueError("Marcatori dell'indice pubblico mancanti o duplicati")
    inizio = testo.index(INIZIO)
    fine = testo.index(FINE, inizio) + len(FINE)
    nuovo = testo[:inizio] + blocco() + testo[fine:]
    mancanti = verifica_link(nuovo)
    if mancanti:
        print("Collegamenti locali mancanti: " + ", ".join(mancanti))
        return 1
    if a.check:
        if testo != nuovo:
            print("README.md da aggiornare: python tools/aggiorna-readme.py")
            return 1
        print("README.md allineato; collegamenti locali validi")
        return 0
    if testo != nuovo:
        README.write_text(nuovo, encoding="utf-8", newline="\n")
        print("README.md aggiornato")
    else:
        print("README.md già allineato")
    return 0


if __name__ == "__main__":
    sys.exit(main())
