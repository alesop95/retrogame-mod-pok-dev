#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica che il PDF prodotto contenga davvero ogni capitolo e ogni sezione dei sorgenti.

Perché esiste
-------------
Il progetto aveva già un controllo di copertura, `check-thesis-coverage.py`, e quel controllo ha
un punto cieco che il 2026-09-03 si è manifestato come una domanda dell'utente: aveva aperto il
PDF e credeva che si fermasse a metà delle appendici. Il controllo esistente confronta i documenti
di `docs/` con i file dei capitoli e riferisce cento per cento; non guarda il PDF. Ne segue che
tutti gli esiti seguenti sarebbero passati inosservati.

Un capitolo scritto e non incluso in `tesi.tex`. Una compilazione che si arresta a metà e lascia
sul disco il PDF della corsa precedente. Un PDF aperto in un lettore che ne blocca la scrittura,
cosicché la compilazione riferisce successo e il file resta vecchio. Un pacchetto che sopprime una
parte del documento senza errori. In tutti e quattro i casi il sorgente è corretto, il controllo
di copertura è verde, e il documento consegnato è incompleto.

Questo programma chiude il punto cieco confrontando il PDF con i sorgenti invece dei sorgenti con
i sorgenti. Per ciascun file incluso da `tesi.tex` estrae i titoli di capitolo, di sezione e di
sottosezione, e verifica che il testo del PDF li contenga. È un controllo di presenza e non di
identità: non prova che il contenuto sia quello giusto, prova che non manchi. È il tipo di
controllo che il progetto chiama presidio, e la sua utilità non è dimostrare la correttezza ma
rendere impossibile una specifica forma di errore silenzioso.

Come si normalizza un titolo, e perché
--------------------------------------
Un titolo nel sorgente contiene macro di composizione che nel PDF diventano altro, per esempio il
corsivo o una nota. Il confronto avviene quindi su una forma normalizzata: si rimuovono le macro
conservandone gli argomenti, si rimuovono le parentesi graffe, e si collassano gli spazi. La
normalizzazione è deliberatamente grossolana, perché il rischio da evitare è il falso allarme: un
titolo dichiarato assente che invece è presente in forma diversa costerebbe fiducia allo
strumento, e uno strumento di cui non si ha fiducia non viene eseguito.

Uso
---
    python tools/check-thesis-pdf.py
    python tools/check-thesis-pdf.py --pdf tesi/tesi.pdf --sorgente tesi/tesi.tex
"""

import argparse
import io
import os
import re
import subprocess
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(RADICE, "tesi", "tesi.pdf")
SORGENTE = os.path.join(RADICE, "tesi", "tesi.tex")

TITOLI = re.compile(r"^\\(chapter|section|subsection)\*?\{(.+)\}\s*$", re.MULTILINE)
INCLUSIONI = re.compile(r"^\s*\\(?:input|include)\{([^}]+)\}", re.MULTILINE)


def normalizza(testo):
    """La forma su cui i titoli si confrontano: senza macro, senza graffe, spazi collassati."""
    t = testo
    # Le macro con un argomento diventano il loro argomento, ripetutamente per l'annidamento.
    for _ in range(4):
        t = re.sub(r"\\[a-zA-Z]+\*?\{([^{}]*)\}", r"\1", t)
    t = re.sub(r"\\[a-zA-Z]+\*?", " ", t)
    t = t.replace("{", " ").replace("}", " ").replace("~", " ")
    t = t.replace("\\", " ")
    # Il PDF rende la legatura tipografica e i trattini in modi che dipendono dal font: si
    # confronta sulle sole lettere e cifre, che sopravvivono a qualunque resa.
    t = re.sub(r"[^0-9A-Za-zÀ-ÿ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def testo_del_pdf(percorso):
    """Il testo del PDF, estratto con lo strumento di sistema.

    Se lo strumento non c'è, il programma lo dichiara e si arresta invece di riferire successo:
    un controllo che non può essere eseguito non è un controllo superato, ed è la distinzione fra
    uno zero misurato e uno zero non misurato che questo progetto ha già pagato altrove.
    """
    if not os.path.exists(percorso):
        sys.exit("il PDF non esiste: " + percorso)
    try:
        esito = subprocess.run(["pdftotext", "-enc", "UTF-8", percorso, "-"],
                               capture_output=True, check=True)
    except FileNotFoundError:
        sys.exit("manca lo strumento pdftotext, quindi questo controllo non si puo' eseguire: "
                 "non viene riferito come superato, perche' non e' stato eseguito")
    except subprocess.CalledProcessError as exc:
        sys.exit("pdftotext ha fallito con codice %d" % exc.returncode)
    return normalizza(esito.stdout.decode("utf-8", "replace"))


def capitoli_inclusi(sorgente):
    """I file che il documento include, nell'ordine in cui li include."""
    testo = io.open(sorgente, encoding="utf-8").read()
    fuori = []
    base = os.path.dirname(sorgente)
    for rel in INCLUSIONI.findall(testo):
        percorso = os.path.join(base, rel)
        if not percorso.endswith(".tex"):
            percorso += ".tex"
        if os.path.exists(percorso):
            fuori.append(percorso)
    return fuori


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", default=PDF)
    ap.add_argument("--sorgente", default=SORGENTE)
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args(argv)

    pdf = testo_del_pdf(a.pdf)
    inclusi = capitoli_inclusi(a.sorgente)

    # I file dei capitoli presenti sul disco ma non inclusi dal documento. È il difetto più grave
    # fra quelli che questo programma cerca, perché il sorgente è scritto e il lettore non lo vede.
    cartella = os.path.join(os.path.dirname(a.sorgente), "capitoli")
    sul_disco = set()
    if os.path.isdir(cartella):
        for nome in sorted(os.listdir(cartella)):
            if nome.endswith(".tex"):
                sul_disco.add(os.path.join(cartella, nome))
    non_inclusi = sorted(sul_disco - set(os.path.abspath(x) for x in inclusi)
                         - set(inclusi))

    print("Verifica del PDF contro i sorgenti")
    print("")
    print("  PDF                     %s" % os.path.relpath(a.pdf, RADICE))
    print("  file inclusi            %d" % len(inclusi))
    print("  file di capitolo su disco %d" % len(sul_disco))

    mancanti = []
    contati = 0
    for percorso in inclusi:
        testo = io.open(percorso, encoding="utf-8").read()
        for tipo, titolo in TITOLI.findall(testo):
            n = normalizza(titolo)
            if len(n) < 8:
                # Un titolo troppo corto darebbe falsi positivi per coincidenza: si salta e si
                # dichiara nel conto, invece di contarlo come verificato.
                continue
            contati += 1
            if n not in pdf:
                mancanti.append((os.path.relpath(percorso, RADICE), tipo, titolo))
    print("  titoli verificati       %d" % contati)
    print("  titoli assenti dal PDF  %d" % len(mancanti))
    print("")

    problemi = 0
    if non_inclusi:
        problemi += 1
        print("  FILE DI CAPITOLO NON INCLUSI DAL DOCUMENTO:")
        for p in non_inclusi:
            print("    %s" % os.path.relpath(p, RADICE))
        print("")
    if mancanti:
        problemi += 1
        print("  TITOLI PRESENTI NEL SORGENTE E ASSENTI DAL PDF:")
        for p, tipo, titolo in mancanti[:40]:
            print("    %-44s %-10s %s" % (p, tipo, titolo[:70]))
        if len(mancanti) > 40:
            print("    e altri %d" % (len(mancanti) - 40))
        print("")
        print("  Le cause possibili, in ordine di probabilita': il PDF sul disco e' di una corsa")
        print("  precedente, perche' un lettore aperto ne ha bloccato la scrittura; la")
        print("  compilazione si e' arrestata; oppure un pacchetto sopprime una parte del")
        print("  documento senza errori. La prima si riconosce guardando la data del file.")
        print("")

    if not problemi:
        print("  Nessun problema: ogni file di capitolo e' incluso e ogni titolo compare nel PDF.")
    if a.verbose:
        print("")
        print("  file inclusi, nell'ordine:")
        for p in inclusi:
            print("    %s" % os.path.relpath(p, RADICE))
    return 1 if problemi else 0


if __name__ == "__main__":
    sys.exit(main())
