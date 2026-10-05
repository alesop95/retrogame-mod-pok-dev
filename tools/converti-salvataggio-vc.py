#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Converte un salvataggio di Game Boy o Game Boy Color fra il formato grezzo e il `sav.dat` della Virtual Console del 3DS.

Perché esiste
-------------
Il residuo del corpus della collezione cita due volte il convertitore web dell'iniettore Crystal Clear,
`inject.sigkill.tech/converter/3dsvc` e `/vc-save`, che il 2026-10-05 risultava un'applicazione interattiva senza testo
da leggere. Il proprietario ha chiesto che la logica degli strumenti interattivi utili non resti fuori dal progetto, e
questa serve al ponte fra le generazioni 1 e 2 e la terza e al ramo `tools/pkhex-mew-vc`, che lavorano su salvataggi di
Virtual Console. La logica è letta nel pacchetto compilato della pagina, componente `3DSVCSaveView`, e descritta in
`docs/strumenti-interattivi.md`: la pagina copia i primi 0x8010 byte del file in un buffer di 0x8010 byte azzerato e lo
offre come `sav.dat`, quindi un salvataggio grezzo di 0x8000 byte riceve 16 byte finali a zero, e nessuna somma di
controllo viene ricalcolata.

Che cosa fa
-----------
`--verso vc` scrive il `sav.dat` da un salvataggio grezzo di 0x8000 byte, accodando 16 byte a zero, come la pagina.
`--verso grezzo` toglie la coda e scrive il salvataggio di 0x8000 byte, che è la forma che leggono gli emulatori e gli
strumenti del ponte. Un file di dimensione diversa da quella attesa si rifiuta invece di essere troncato in silenzio.
Lo strumento non scrive mai sul file di partenza: scrive accanto, oppure dove dice `--uscita`.

Che cosa non è verificato
-------------------------
Il significato dei 16 byte finali. PKHeX riconosce come coda di orologio, in `SaveHandlerFooterRTC.cs`, le code fra 0x0C
e 0x30 byte dei salvataggi di prima, seconda e terza generazione, e la scarta alla lettura; che la Virtual Console del
3DS accetti una coda tutta a zero è quanto fa la pagina, non una prova fatta dal progetto. Prima di caricare un file
prodotto qui su una console vale `rules/hardware-and-perimeter.md`: copia di riserva del salvataggio originale in
doppia copia, e rilettura dopo la scrittura.

Uso
---
    python tools/converti-salvataggio-vc.py --verso vc salvataggio.sav
    python tools/converti-salvataggio-vc.py --verso grezzo sav.dat --uscita salvataggio.sav
    python tools/converti-salvataggio-vc.py --autotest
"""

import argparse
import hashlib
import os
import sys

GREZZO = 0x8000
CODA = 0x10
VC = GREZZO + CODA


def a_vc(dati):
    if len(dati) == VC:
        raise ValueError("il file ha già la dimensione di un sav.dat (0x%X byte)" % VC)
    if len(dati) != GREZZO:
        raise ValueError("attesi 0x%X byte di salvataggio grezzo, trovati 0x%X" % (GREZZO, len(dati)))
    return dati + bytes(CODA)


def a_grezzo(dati):
    if len(dati) != VC:
        raise ValueError("attesi 0x%X byte di sav.dat, trovati 0x%X" % (VC, len(dati)))
    return dati[:GREZZO]


def autotest():
    campione = bytes((i * 7 + 3) & 0xFF for i in range(GREZZO))
    vc = a_vc(campione)
    assert len(vc) == VC and vc[GREZZO:] == bytes(CODA), "la coda deve essere di 16 byte a zero"
    assert a_grezzo(vc) == campione, "andata e ritorno devono restituire i byte di partenza"
    for sbagliato, funzione in ((campione[:-1], a_vc), (vc, a_vc), (campione, a_grezzo)):
        try:
            funzione(sbagliato)
        except ValueError:
            continue
        raise AssertionError("una dimensione sbagliata deve essere rifiutata")
    print("autotest: 4 prove superate")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file", nargs="?")
    ap.add_argument("--verso", choices=("vc", "grezzo"))
    ap.add_argument("--uscita", help="percorso del file da scrivere; per difetto accanto al file di partenza")
    ap.add_argument("--autotest", action="store_true", help="esegue le prove interne")
    a = ap.parse_args()
    if a.autotest:
        return autotest()
    if not a.file or not a.verso:
        ap.error("servono il file e --verso")
    dati = open(a.file, "rb").read()
    try:
        nuovi = a_vc(dati) if a.verso == "vc" else a_grezzo(dati)
    except ValueError as e:
        sys.exit("rifiutato: %s" % e)
    uscita = a.uscita or os.path.join(os.path.dirname(os.path.abspath(a.file)),
                                      "sav.dat" if a.verso == "vc" else os.path.splitext(os.path.basename(a.file))[0] + ".sav")
    if os.path.abspath(uscita) == os.path.abspath(a.file):
        sys.exit("rifiutato: l'uscita coincide con il file di partenza")
    open(uscita, "wb").write(nuovi)
    riletto = open(uscita, "rb").read()
    if riletto != nuovi:
        sys.exit("rilettura diversa da quanto scritto: %s" % uscita)
    print("scritto %s, 0x%X byte, SHA-256 %s" % (uscita, len(riletto), hashlib.sha256(riletto).hexdigest()[:16]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
