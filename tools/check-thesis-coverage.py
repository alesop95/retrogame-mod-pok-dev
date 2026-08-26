#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica che la tesi vada di pari passo con i documenti del progetto.

Il problema
-----------
La tesi spiega dallo zero assoluto gli stessi argomenti che le note di `docs/` trattano
per un lettore che ha già il contesto, e la referenza dei formati documenta byte per
byte. Sono tre registri diversi dello stesso sapere, e tre testi che dicono la stessa
cosa in tre modi divergono: è quasi una legge. Il modo di non farli divergere non è
la buona volontà, è un controllo che fallisce.

Il meccanismo, che è lo stesso di sync-context
-----------------------------------------------
Ogni capitolo della tesi dichiara in testa, come commenti LaTeX, quali documenti copre e
a quale commit è stato verificato contro di essi:

    % copre: docs/03-integrita-checksum.md
    % copre: pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md
    % verificato-al-commit: 3f1c9b3

Da qui lo strumento ricava quattro verifiche, e ciascuna corrisponde a un modo concreto
in cui i testi divergerebbero senza accorgersene.

La prima è il drift: se un documento coperto è cambiato dopo il commit dichiarato, il
capitolo che lo copre è sospetto e va riletto. È esattamente il confronto che
sync-context fa sulle schede di contesto, applicato ai capitoli.

La seconda è la copertura: se un documento di `docs/` non è coperto da alcun capitolo,
la tesi ha un buco. Non è necessariamente un errore, perché un documento può essere
deliberatamente fuori perimetro, ma deve essere una scelta dichiarata e non una
dimenticanza: per questo esiste il file di esenzione descritto sotto.

La terza è l'integrità delle citazioni: ogni `\\cite{chiave}` deve corrispondere a una
voce della bibliografia generata. È il controllo che BibTeX farebbe, e che qui serve
farlo perché la bibliografia non passa da BibTeX.

La quarta è l'inverso della terza: una fonte in bibliografia che nessun capitolo cita
è una fonte che il registro tiene e la tesi non usa. Non è un errore, è un elenco da
guardare, perché spesso significa che un argomento è stato scritto senza appoggiarlo
alla fonte che lo sosteneva.

Le esenzioni
------------
Un documento che la tesi non copre di proposito va elencato in `tesi/non-coperti.txt`,
una riga per percorso, con il motivo dopo un cancelletto. Un'esenzione senza motivo è
rifiutata, perché il senso del file è costringere a dichiarare la ragione.

Uso
---
    python tools/check-thesis-coverage.py
    python tools/check-thesis-coverage.py --verbose

Esce con codice diverso da zero se una delle verifiche vincolanti fallisce, cioè drift,
copertura mancante o citazione orfana. Le fonti mai citate sono un avviso e non un
errore.
"""

import argparse
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESI = os.path.join(ROOT, "tesi")
CAPITOLI = os.path.join(TESI, "capitoli")
BIBLIOGRAFIA = os.path.join(TESI, "bibliografia.tex")
ESENZIONI = os.path.join(TESI, "non-coperti.txt")

# I documenti che la tesi deve coprire. Sono le note di studio e la referenza dei
# formati: le schede di .claude/context/ sono stato e non conoscenza, quindi non entrano.
def documenti_da_coprire():
    fonti = []
    docs = os.path.join(ROOT, "docs")
    for nome in sorted(os.listdir(docs)):
        if nome.endswith(".md") and nome != "index.md":
            fonti.append("docs/" + nome)
    fonti.append("pokemon-gen12-gen3-bridge-original-hardware/"
                 "DATA-FORMATS_Gen1-Gen2-Gen3.md")
    return fonti


def git(*args):
    out = subprocess.run(["git", "-C", ROOT] + list(args),
                         capture_output=True, text=True)
    return out.stdout.strip(), out.returncode


def leggi_capitoli():
    """Ogni capitolo con le sue dichiarazioni. Un capitolo senza dichiarazioni è un errore."""
    capitoli = []
    if not os.path.isdir(CAPITOLI):
        return capitoli
    for nome in sorted(os.listdir(CAPITOLI)):
        if not nome.endswith(".tex"):
            continue
        percorso = os.path.join(CAPITOLI, nome)
        with open(percorso, "rb") as f:
            testo = f.read().decode("utf-8")
        copre = re.findall(r"^%\s*copre:\s*(\S+)\s*$", testo, re.M)
        commit = re.search(r"^%\s*verificato-al-commit:\s*(\S+)\s*$", testo, re.M)
        cita = set(re.findall(r"\\cite\{([^}]+)\}", testo))
        chiavi = set()
        for gruppo in cita:
            for k in gruppo.split(","):
                k = k.strip()
                if k:
                    chiavi.add(k)
        capitoli.append({
            "file": "tesi/capitoli/" + nome,
            "copre": copre,
            "commit": commit.group(1) if commit else None,
            "citazioni": chiavi,
        })
    return capitoli


def leggi_chiavi_bibliografia():
    if not os.path.exists(BIBLIOGRAFIA):
        return None
    with open(BIBLIOGRAFIA, "rb") as f:
        testo = f.read().decode("utf-8")
    return set(re.findall(r"\\bibitem\{([^}]+)\}", testo))


def leggi_esenzioni():
    """I documenti dichiarati fuori perimetro, con il motivo. Senza motivo si rifiuta."""
    esenti, malformate = {}, []
    if not os.path.exists(ESENZIONI):
        return esenti, malformate
    with open(ESENZIONI, "rb") as f:
        for riga in f.read().decode("utf-8").splitlines():
            riga = riga.strip()
            if not riga or riga.startswith("##"):
                continue
            if "#" not in riga:
                malformate.append(riga)
                continue
            percorso, motivo = riga.split("#", 1)
            percorso, motivo = percorso.strip(), motivo.strip()
            if not percorso or not motivo:
                malformate.append(riga)
                continue
            esenti[percorso] = motivo
    return esenti, malformate


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--verbose", action="store_true",
                    help="elenca anche ciò che è in ordine")
    args = ap.parse_args()

    head, rc = git("rev-parse", "--short", "HEAD")
    if rc != 0:
        print("nessun commit: il controllo di drift non si applica")
        head = None

    capitoli = leggi_capitoli()
    if not capitoli:
        print("nessun capitolo in tesi/capitoli/: niente da verificare")
        return 0

    chiavi_bib = leggi_chiavi_bibliografia()
    esenti, esenzioni_malformate = leggi_esenzioni()

    errori, avvisi = [], []

    # --- 1. dichiarazioni presenti -------------------------------------------------
    for cap in capitoli:
        if not cap["copre"]:
            errori.append("%s non dichiara alcun 'copre:'" % cap["file"])
        if cap["commit"] is None:
            errori.append("%s non dichiara 'verificato-al-commit:'" % cap["file"])

    # --- 2. drift ------------------------------------------------------------------
    stale = []
    for cap in capitoli:
        if not cap["commit"] or not cap["copre"] or head is None:
            continue
        _, rc = git("cat-file", "-e", cap["commit"] + "^{commit}")
        if rc != 0:
            errori.append("%s dichiara il commit %s, che non esiste"
                          % (cap["file"], cap["commit"]))
            continue
        out, _ = git("diff", "--name-only", cap["commit"] + "..HEAD", "--", *cap["copre"])
        cambiati = [r for r in out.splitlines() if r.strip()]
        if cambiati:
            stale.append((cap["file"], cap["commit"], cambiati))

    # --- 3. copertura --------------------------------------------------------------
    coperti = set()
    for cap in capitoli:
        coperti.update(cap["copre"])
    scoperti = []
    for doc in documenti_da_coprire():
        if doc in coperti or doc in esenti:
            continue
        scoperti.append(doc)

    # Un 'copre:' che punta a un file inesistente è un errore, non una copertura.
    for cap in capitoli:
        for doc in cap["copre"]:
            if not os.path.exists(os.path.join(ROOT, doc)):
                errori.append("%s dichiara di coprire %s, che non esiste"
                              % (cap["file"], doc))

    # --- 4. citazioni --------------------------------------------------------------
    citate = set()
    for cap in capitoli:
        citate.update(cap["citazioni"])
    orfane = []
    if chiavi_bib is None:
        errori.append("bibliografia assente: eseguire tools/build-bibliography.py")
    else:
        orfane = sorted(citate - chiavi_bib)
        mai_citate = sorted(chiavi_bib - citate)

    # --- rapporto ------------------------------------------------------------------
    print("Controllo di pari passo della tesi (HEAD = %s)\n" % (head or "n/d"))
    print("capitoli: %d, documenti da coprire: %d, coperti: %d, esenti: %d"
          % (len(capitoli), len(documenti_da_coprire()),
             len(documenti_da_coprire()) - len(scoperti) - len(esenti), len(esenti)))
    if chiavi_bib is not None:
        print("bibliografia: %d voci, citate: %d" % (len(chiavi_bib), len(citate)))
    print()

    if stale:
        print("CAPITOLI DA RILEGGERE, il documento coperto è cambiato dopo la verifica:")
        for f, commit, cambiati in stale:
            print("  %s (verificato a %s)" % (f, commit))
            for c in cambiati:
                print("      cambiato: %s" % c)
        print()
        errori.append("%d capitoli in drift" % len(stale))

    if scoperti:
        print("DOCUMENTI NON COPERTI da alcun capitolo, né dichiarati esenti:")
        for d in scoperti:
            print("  %s" % d)
        print()
        errori.append("%d documenti non coperti" % len(scoperti))

    if orfane:
        print("CITAZIONI SENZA VOCE in bibliografia:")
        for k in orfane:
            print("  \\cite{%s}" % k)
        print()
        errori.append("%d citazioni orfane" % len(orfane))

    if esenzioni_malformate:
        print("ESENZIONI SENZA MOTIVO in tesi/non-coperti.txt:")
        for r in esenzioni_malformate:
            print("  %s" % r)
        print()
        errori.append("%d esenzioni malformate" % len(esenzioni_malformate))

    if chiavi_bib is not None and mai_citate:
        print("avviso, fonti in bibliografia che nessun capitolo cita (%d):"
              % len(mai_citate))
        print("  " + ", ".join(mai_citate))
        print()
        avvisi.append("%d fonti mai citate" % len(mai_citate))

    if args.verbose:
        print("dettaglio dei capitoli:")
        for cap in capitoli:
            print("  %s -> %s (a %s, %d citazioni)"
                  % (cap["file"], ", ".join(cap["copre"]) or "nulla",
                     cap["commit"], len(cap["citazioni"])))
        if esenti:
            print("\nesenzioni dichiarate:")
            for percorso, motivo in sorted(esenti.items()):
                print("  %s: %s" % (percorso, motivo))
        print()

    if errori:
        print("%d problemi: %s" % (len(errori), "; ".join(errori)))
        return 1
    print("nessun problema%s" % (", %s" % "; ".join(avvisi) if avvisi else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
