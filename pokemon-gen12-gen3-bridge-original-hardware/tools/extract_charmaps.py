#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera le tabelle di codifica dei caratteri dai disassemblati, invece di ricopiarle.

Perche' esiste
--------------
Le pagine enciclopediche sbagliano la tabella caratteri in due punti verificati: per la
generazione 1 collocano le cifre a 0xF0 mentre il sorgente le colloca a 0xF6, e per la
generazione 3 collocano le maiuscole a 0xC1 mentre il sorgente le colloca a 0xBB. Un
errore di questo tipo non fa fallire nulla: produce soprannomi con caratteri sbagliati
ma stampabili, quindi passa i test a occhio. La sola difesa strutturale e' non trascrivere
mai la tabella a mano e generarla dal charmap del gioco, che e' la definizione autorevole.

Sorgenti
--------
Generazione 1 e 2:  pret/pokecrystal, constants/charmap.asm   -> charmap "A", $80
Generazione 3:      pret/pokeemerald, charmap.txt             -> 'A'         = BB

I due repository si ottengono con un clone superficiale, per esempio
    git clone --depth 1 https://github.com/pret/pokecrystal
    git clone --depth 1 https://github.com/pret/pokeemerald

Uso
---
    python tools/extract_charmaps.py --pokecrystal PATH --pokeemerald PATH --out data

Produce tre file in --out:
    charmap-gen12.json          byte -> carattere per Gen 1 e 2, piu' i token di controllo
    charmap-gen3.json           byte -> carattere per Gen 3, piu' i token di controllo
    charmap-gen12-to-gen3.json  traduzione diretta fra i due spazi di codifica

Lo script si rifiuta di scrivere se i valori di controllo non corrispondono a quelli
attesi: se il formato del sorgente a monte cambia, il fallimento e' rumoroso.
"""

import argparse
import json
import os
import re
import subprocess
import sys

# Valori di controllo. Non sono la tabella: sono le sentinelle che dimostrano che la
# tabella e' stata letta correttamente. Verificati sul sorgente il 2026-08-25.
EXPECTED_GEN12 = {0x50: "@", 0x7F: " ", 0x80: "A", 0x99: "Z",
                  0xA0: "a", 0xB9: "z", 0xF6: "0", 0xFF: "9"}
EXPECTED_GEN3 = {0x00: " ", 0xA1: "0", 0xAA: "9", 0xBB: "A",
                 0xD4: "Z", 0xD5: "a", 0xEE: "z"}

RE_GEN12 = re.compile(r'^\s*charmap\s+"(?P<tok>(?:[^"\\]|\\.)*)"\s*,\s*\$(?P<val>[0-9a-fA-F]{2})')
RE_GEN3 = re.compile(r"^'(?P<tok>.+?)'\s*=\s*(?P<val>[0-9A-Fa-f]{2})\s*$")
RE_GEN3_NAMED = re.compile(r"^(?P<tok>[A-Z_][A-Z0-9_]*)\s*=\s*(?P<val>[0-9A-Fa-f]{2})\s*$")


def git_commit(repo_path):
    """Hash del commit clonato, cosi' che la tabella sia riconducibile a una revisione."""
    try:
        out = subprocess.check_output(["git", "-C", repo_path, "rev-parse", "HEAD"],
                                      stderr=subprocess.DEVNULL)
        return out.decode("ascii").strip()
    except Exception:
        return "sconosciuto"


def parse_gen12(repo_path):
    path = os.path.join(repo_path, "constants", "charmap.asm")
    printable, control = {}, {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = RE_GEN12.match(line)
            if not m:
                continue
            tok, val = m.group("tok"), int(m.group("val"), 16)
            # Il charmap assegna piu' token allo stesso byte (varianti giapponesi,
            # alias di font). Il primo vince, che e' l'ordine di dichiarazione.
            target = control if tok.startswith("<") else printable
            target.setdefault(val, tok)
    return printable, control, path


def parse_gen3(repo_path):
    path = os.path.join(repo_path, "charmap.txt")
    printable, control = {}, {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.split("@@")[0].rstrip("\n")
            m = RE_GEN3.match(line)
            if m:
                printable.setdefault(int(m.group("val"), 16), m.group("tok"))
                continue
            m = RE_GEN3_NAMED.match(line)
            if m:
                control.setdefault(int(m.group("val"), 16), m.group("tok"))
    return printable, control, path


def check(name, printable, expected):
    """Verifica le sentinelle. Ritorna la lista degli scostamenti trovati."""
    problems = []
    for byte, want in expected.items():
        got = printable.get(byte)
        if got != want:
            problems.append("%s: 0x%02X vale %r, atteso %r" % (name, byte, got, want))
    return problems


def dump(out_dir, filename, payload):
    path = os.path.join(out_dir, filename)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write("\n")
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pokecrystal", required=True, help="clone di pret/pokecrystal")
    ap.add_argument("--pokeemerald", required=True, help="clone di pret/pokeemerald")
    ap.add_argument("--out", default="data", help="cartella di destinazione dei JSON")
    args = ap.parse_args()

    g12, g12_ctrl, g12_path = parse_gen12(args.pokecrystal)
    g3, g3_ctrl, g3_path = parse_gen3(args.pokeemerald)

    problems = check("gen12", g12, EXPECTED_GEN12) + check("gen3", g3, EXPECTED_GEN3)
    if problems:
        print("VERIFICA FALLITA, nessun file scritto:", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        return 1

    os.makedirs(args.out, exist_ok=True)

    meta12 = {"repo": "pret/pokecrystal", "file": "constants/charmap.asm",
              "commit": git_commit(args.pokecrystal)}
    meta3 = {"repo": "pret/pokeemerald", "file": "charmap.txt",
             "commit": git_commit(args.pokeemerald)}

    p1 = dump(args.out, "charmap-gen12.json", {
        "generazioni": [1, 2], "fonte": meta12,
        "terminatore": 0x50, "spazio": 0x7F,
        "stampabili": {"0x%02X" % k: v for k, v in sorted(g12.items())},
        "controllo": {"0x%02X" % k: v for k, v in sorted(g12_ctrl.items())},
    })
    p2 = dump(args.out, "charmap-gen3.json", {
        "generazioni": [3], "fonte": meta3,
        "terminatore": 0xFF, "spazio": 0x00,
        "stampabili": {"0x%02X" % k: v for k, v in sorted(g3.items())},
        "controllo": {"0x%02X" % k: v for k, v in sorted(g3_ctrl.items())},
    })

    # Traduzione diretta: e' questo il file che il convertitore usa davvero.
    # Un carattere presente in Gen 1 e 2 ma assente in Gen 3 non ha destinazione e
    # viene elencato a parte, perche' e' una decisione di prodotto e non un dettaglio.
    gen3_by_char = {}
    for byte, ch in sorted(g3.items()):
        gen3_by_char.setdefault(ch, byte)
    mapping, orphans = {}, {}
    for byte, ch in sorted(g12.items()):
        if ch in gen3_by_char:
            mapping["0x%02X" % byte] = "0x%02X" % gen3_by_char[ch]
        else:
            orphans["0x%02X" % byte] = ch
    p3 = dump(args.out, "charmap-gen12-to-gen3.json", {
        "descrizione": "byte Gen 1 e 2 -> byte Gen 3, per identita' del carattere reso",
        "fonti": [meta12, meta3],
        "terminatore": {"gen12": 0x50, "gen3": 0xFF},
        "traduzione": mapping,
        "senza_destinazione": orphans,
    })

    print("gen12: %d stampabili, %d di controllo (%s)" % (len(g12), len(g12_ctrl), g12_path))
    print("gen3:  %d stampabili, %d di controllo (%s)" % (len(g3), len(g3_ctrl), g3_path))
    print("traduzione: %d corrispondenze, %d senza destinazione" % (len(mapping), len(orphans)))
    print("sentinelle verificate su entrambe le tabelle")
    for p in (p1, p2, p3):
        print("scritto " + p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
