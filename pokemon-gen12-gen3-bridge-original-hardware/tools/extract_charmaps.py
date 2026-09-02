#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera le tabelle di codifica dei caratteri dai disassemblati, invece di ricopiarle.

Perché esiste
--------------
Le pagine enciclopediche sbagliano la tabella caratteri in due punti verificati: per la
generazione 1 collocano le cifre a 0xF0 mentre il sorgente le colloca a 0xF6, e per la
generazione 3 collocano le maiuscole a 0xC1 mentre il sorgente le colloca a 0xBB. Un
errore di questo tipo non fa fallire nulla: produce soprannomi con caratteri sbagliati
ma stampabili, quindi passa i test a occhio. La sola difesa strutturale è non trascrivere
mai la tabella a mano e generarla dal charmap del gioco, che è la definizione autorevole.

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
    charmap-gen12.json          byte -> carattere per Gen 1 e 2, più i token di controllo
    charmap-gen3.json           byte -> carattere per Gen 3, più i token di controllo
    charmap-gen12-to-gen3.json  traduzione diretta fra i due spazi di codifica

Lo script si rifiuta di scrivere se i valori di controllo non corrispondono a quelli
attesi: se il formato del sorgente a monte cambia, il fallimento è rumoroso.
"""

import argparse
import json
import os
import re
import subprocess
import sys

# Valori di controllo. Non sono la tabella: sono le sentinelle che dimostrano che la
# tabella è stata letta correttamente. Verificati sul sorgente il 2026-08-25.
EXPECTED_GEN12 = {0x50: "@", 0x7F: " ", 0x80: "A", 0x99: "Z",
                  0xA0: "a", 0xB9: "z", 0xF6: "0", 0xFF: "9"}
EXPECTED_GEN3 = {0x00: " ", 0xA1: "0", 0xAA: "9", 0xBB: "A",
                 0xD4: "Z", 0xD5: "a", 0xEE: "z"}

RE_GEN12 = re.compile(r'^\s*charmap\s+"(?P<tok>(?:[^"\\]|\\.)*)"\s*,\s*\$(?P<val>[0-9a-fA-F]{2})')
RE_GEN3 = re.compile(r"^'(?P<tok>.+?)'\s*=\s*(?P<val>[0-9A-Fa-f]{2})\s*$")
RE_GEN3_NAMED = re.compile(r"^(?P<tok>[A-Z_][A-Z0-9_]*)\s*=\s*(?P<val>[0-9A-Fa-f]{2})\s*$")


def git_commit(repo_path):
    """Hash del commit clonato, così che la tabella sia riconducibile a una revisione."""
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
            # Il charmap assegna più token allo stesso byte (varianti giapponesi,
            # alias di font). Il primo vince, che è l'ordine di dichiarazione.
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

    # Traduzione diretta: è questo il file che il convertitore usa davvero.
    # Un carattere presente in Gen 1 e 2 ma assente in Gen 3 non ha destinazione e
    # viene elencato a parte, perché è una decisione di prodotto e non un dettaglio.
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
        "descrizione": "byte Gen 1 e 2 -> byte Gen 3, per identità del carattere reso",
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
# ---------------------------------------------------------------------------------------------
# La tabella giapponese, e perche' viene da una fonte di rango diverso
# ---------------------------------------------------------------------------------------------
# Le altre tabelle di questo strumento vengono dai disassemblati, che sono la fonte di rango piu'
# alto: sono il gioco stesso, tradotto in una forma leggibile. Per la tabella giapponese di terza
# generazione quella via non e' disponibile, perche' il disassemblato che il progetto clona e'
# quello della versione internazionale e la sua tabella e' quella internazionale.
#
# La fonte impiegata qui e' quindi di rango inferiore e va dichiarata come tale: e' il codice
# della implementazione di riferimento, cioe' il verificatore di conformita' che la comunita'
# usa. Non e' il gioco, ma e' cio' contro cui gli esemplari verranno misurati, che per questo
# scopo e' esattamente la cosa giusta: se il verificatore leggera' i nostri byte con la sua
# tabella, la tabella con cui li scriviamo deve essere la sua.
#
# Il fatto che rende necessaria una seconda tabella vale scritto perche' non e' evidente e
# perche' sbagliarlo non produce un errore ma un nome plausibile e sbagliato. Nella terza
# generazione un byte non ha un carattere: ha due caratteri, e quale dei due si veda dipende
# dalla lingua del gioco. Due esempi verificati fra i tanti: il byte 0x6F rende "ma" in
# katakana su un gioco giapponese e la lettera i con accento acuto su uno internazionale, e il
# byte 0x52 rende "i" in katakana sul primo e "ka" in katakana sul secondo, cioe' due sillabe
# diverse. Un nome giapponese scritto con la tabella internazionale produce dunque byte che il
# gioco giapponese legge come un'altra parola, e nessun controllo di formato lo segnala.

# I nomi simbolici che la fonte impiega dentro le tabelle al posto di un carattere letterale,
# con il valore che la fonte stessa dichiara accanto alla loro definizione.
SIMBOLI_CSHARP = {
    "FGM": "\u2642",
    "FGF": "\u2640",
    "HGM": "\u2642",
    "HGF": "\u2640",
}

# Il byte di terminazione, che nella fonte riempie la coda della tabella per portarla a
# duecentocinquantasei posizioni. Non e' un carattere e non entra nella corrispondenza.
TERMINATORE_CSHARP = "Terminator"

SORGENTE_JP = "PKHeX.Core/PKM/Strings/StringConverter3.cs"


def _voci_array_csharp(testo, nome):
    """Le voci dell'array di caratteri che la fonte definisce con quel nome.

    Si legge il testo fra la freccia e la parentesi quadra di chiusura, e da la' si estraggono
    in ordine i letterali di carattere e i nomi simbolici. L'ordine e' l'informazione: la
    posizione di una voce nell'array e' il byte che le corrisponde, quindi perdere una voce non
    sposta una riga ma tutte quelle che seguono.
    """
    apertura = testo.find("ReadOnlySpan<char> " + nome)
    if apertura < 0:
        raise SystemExit("non trovo la tabella " + nome + " in " + SORGENTE_JP)
    inizio = testo.index("[", apertura)
    chiusura = testo.index("];", inizio)
    corpo = testo[inizio + 1:chiusura]
    # Si tolgono i commenti di riga, che nella fonte portano il numero della riga di sedici.
    corpo = re.sub(r"//[^\n]*", "", corpo)
    voci = []
    for pezzo in corpo.split(","):
        pezzo = pezzo.strip()
        if not pezzo:
            continue
        letterale = re.match(r"^'(\\.|[^'])'$", pezzo)
        if letterale:
            grezzo = letterale.group(1)
            voci.append({"\\'": "'", "\\\\": "\\"}.get(grezzo, grezzo))
        elif pezzo == TERMINATORE_CSHARP:
            voci.append(None)
        elif pezzo in SIMBOLI_CSHARP:
            voci.append(SIMBOLI_CSHARP[pezzo])
        else:
            raise SystemExit("voce non riconosciuta nella tabella " + nome + ": " + repr(pezzo))
    return voci


def estrai_gen3_giapponese(pkhex):
    """La corrispondenza byte-carattere della tabella giapponese, dalla fonte di riferimento.

    Restituisce il dizionario nella forma che il modulo di transcodifica attende, cioe' con la
    chiave del byte in esadecimale. Le posizioni di terminazione non entrano.
    """
    percorso = os.path.join(pkhex, SORGENTE_JP.replace("/", os.sep))
    if not os.path.exists(percorso):
        raise SystemExit(
            "manca " + SORGENTE_JP + " sotto " + pkhex + ".\n"
            "Si ottiene estendendo il clone superficiale con la cartella PKM/Strings.")
    testo = open(percorso, encoding="utf-8", errors="ignore").read()
    voci = _voci_array_csharp(testo, "G3_JP")
    if len(voci) != 256:
        raise SystemExit(
            "la tabella giapponese ha %d voci invece di 256: la lettura ha perso o duplicato "
            "qualcosa, e siccome la posizione e il byte, un solo scostamento sposta tutto cio "
            "che segue" % (len(voci),))
    # Il controllo che rende l'estrazione verificata e non soltanto eseguita: tre byte di cui
    # si conosce il valore atteso, scelti perche' sono quelli su cui la tabella internazionale
    # dice altro. Se la lettura si sposta di una posizione, questi tre non tornano.
    ATTESI = {0x6F: "\u30de", 0x52: "\u30a4", 0xAE: "\u30fc"}
    for byte, carattere in ATTESI.items():
        if voci[byte] != carattere:
            raise SystemExit(
                "il byte 0x%02X della tabella giapponese vale %r invece di %r: la lettura non "
                "e allineata" % (byte, voci[byte], carattere))
    return {"%02X" % b: c for b, c in enumerate(voci) if c is not None}
