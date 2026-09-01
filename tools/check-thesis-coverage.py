#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica che ogni riga dei documenti del progetto finisca da qualche parte nella tesi.

Il requisito, detto con precisione
----------------------------------
Il PDF deve contenere tutto ciò che sta nei documenti Markdown del progetto. Non serve una
corrispondenza uno a uno fra un documento e un capitolo: l'organizzazione in parti,
capitoli e paragrafi è libera, e un capitolo può raccogliere pezzi di documenti diversi
mentre un documento può finire spezzato in più capitoli. Ciò che non è libero è la
copertura: nessun pezzo deve restare fuori senza che qualcuno lo abbia deciso.

Perché si conta per sezione e non per riga
-----------------------------------------
Contare le righe sarebbe illusorio: una riga di prosa riscritta per un lettore diverso non
ha lo stesso testo, quindi nessun confronto meccanico fra righe può dire se il contenuto è
passato. L'unità verificabile più fine è la sezione, cioè l'intestazione Markdown con il
testo che le sta sotto: è abbastanza piccola da rendere il controllo utile, ed è
abbastanza stabile da poter essere nominata in una dichiarazione.

Quando una sezione risulta reclamata, il controllo non garantisce che il suo contenuto sia
stato reso fedelmente: quello resta lavoro umano. Garantisce che nessuna sezione sia stata
dimenticata, che è il modo in cui il contenuto si perde davvero.

Come si dichiara
----------------
In testa a ogni capitolo, come commenti LaTeX. Un capitolo può reclamare interi documenti
o singole sezioni, e più capitoli possono reclamare lo stesso documento senza conflitto.

    % copre: docs/03-integrita-checksum.md
    % copre: docs/01-fondamenta-salvataggio.md#il-supporto-fisico
    % verificato-al-commit: 3f1c9b3

La forma con il cancelletto nomina una sezione per slug, cioè il titolo ridotto a
minuscole con i non alfanumerici sostituiti da trattini, come fanno i generatori di
ancore. Se un titolo viene riscritto lo slug cambia e il controllo lo segnala come
sconosciuto: non è un falso allarme, è il segnale che quel capitolo va riletto.

Le omissioni deliberate
-----------------------
Un documento o una sezione che la tesi non deve contenere va dichiarato in
`tesi/non-coperti.txt`, con il motivo dopo un cancelletto. Le righe di quel file usano la
stessa sintassi delle dichiarazioni, quindi si può escludere un intero documento oppure una
sua sezione. Un'esenzione senza motivo viene rifiutata.

Le quattro verifiche
--------------------
La copertura, cioè quali sezioni nessuno reclama. Il drift, cioè quali capitoli dichiarano
un commit anteriore all'ultima modifica dei documenti che coprono. Le citazioni orfane,
cioè i riferimenti bibliografici senza voce. Le fonti mai citate, che sono un avviso.

Uso
---
    python tools/check-thesis-coverage.py
    python tools/check-thesis-coverage.py --verbose
    python tools/check-thesis-coverage.py --scoperte      solo l'elenco da distribuire
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

# I documenti il cui contenuto deve finire nel PDF. Le schede di .claude/context/ e i file
# di .claude/memory/ non entrano: sono stato del lavoro e non conoscenza, e il loro posto è
# il repository, non un documento che si legge dall'inizio alla fine. Le note di
# docs/fonti/ non entrano perché sono generate dalla stessa tabella da cui nasce la
# bibliografia del PDF, quindi vi sono già dentro per costruzione.
ALTRI_DOCUMENTI = (
    "pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md",
    "SOURCES.md",
    "poke-automation-study/STUDIO-01-architettura-e-perimetro.md",
    "3ds-related/README.md",
    "gba-save-extraction-smeraldo/README.md",
    "gba-switch-pokemon-trading/README.md",
    "poke-automation-study/README.md",
    "recreate-pokemon-distributions-events/README.md",
    "recreate-pokemon-distributions-events/STUDIO-01-distribuzioni-gen3-e-ricreazione.md",
    "recreate-pokemon-distributions-events/STUDIO-02-metodi-di-generazione.md",
    "recreate-pokemon-distributions-events/EVENTI-GEN3.md",
    "poke-ace/README.md",
    "poke-ace/STUDIO-01-ace-e-legalita-in-home.md",
    "poke-ace/STUDIO-02-marchi-di-origine-e-che-cosa-conta-una-collezione.md",
    "recreate-pokemon-distributions-events/STUDIO-03-verifica-del-metodo-sul-corpus.md",
    "recreate-pokemon-distributions-events/STUDIO-04-campagna-di-trasferimento-e-il-tracciatore.md",
    "poke-ace/STUDIO-03-la-risposta-della-comunita-e-le-due-severita.md",
    "cart-battery-restoration/README.md",
    "cart-battery-restoration/STUDIO-01-batteria-e-ritenzione.md",
    "generation-from-switch/README.md",
    "generation-from-switch/STUDIO-01-scambio-automatico-e-provenienza.md",
    "pokemon-gen12-gen3-bridge-original-hardware/README.md",
    "3ds-related/handoff/HANDOFF_progetto_3DS.md",
    "gba-save-extraction-smeraldo/handoff/HANDOFF_progetto_smeraldo.md",
    "gba-switch-pokemon-trading/HANDOFF_frlg-ldn-trade.md",
)


def documenti():
    fonti = []
    docs = os.path.join(ROOT, "docs")
    for nome in sorted(os.listdir(docs)):
        if nome.endswith(".md") and nome != "index.md":
            fonti.append("docs/" + nome)
    for rel in ALTRI_DOCUMENTI:
        if os.path.exists(os.path.join(ROOT, rel)):
            fonti.append(rel)
    return fonti


def slug(titolo):
    """Il titolo ridotto ad ancora, come fanno i generatori di indici."""
    s = titolo.strip().lower()
    s = re.sub(r"[`*_\[\]()]", "", s)
    s = re.sub(r"[^a-z0-9àèéìòù]+", "-", s)
    return s.strip("-")


def sezioni_di(rel):
    """Le sezioni di un documento, ciascuna con il numero di righe non vuote.

    Il testo che precede la prima intestazione è una sezione propria, chiamata preambolo:
    spesso contiene il paragrafo che spiega a cosa serve il documento, e lasciarlo fuori
    dal conteggio significherebbe non accorgersi se manca. Il front matter YAML, invece,
    non è contenuto e non si conta.
    """
    with open(os.path.join(ROOT, rel), "rb") as f:
        testo = f.read().decode("utf-8")

    righe = testo.split("\n")
    inizio = 0
    if righe and righe[0].strip() == "---":
        for i in range(1, len(righe)):
            if righe[i].strip() == "---":
                inizio = i + 1
                break

    sezioni = []
    corrente = {"slug": "(preambolo)", "titolo": "(preambolo)", "righe": 0, "livello": 0}
    dentro = False
    for r in righe[inizio:]:
        if re.match(r"^\s*(```|~~~)", r):
            dentro = not dentro
            corrente["righe"] += 1
            continue
        m = None if dentro else re.match(r"^(#{1,6})\s+(.*)$", r)
        if m:
            sezioni.append(corrente)
            corrente = {"slug": slug(m.group(2)), "titolo": m.group(2).strip(),
                        "righe": 0, "livello": len(m.group(1))}
            continue
        if r.strip():
            corrente["righe"] += 1
    sezioni.append(corrente)
    return [s for s in sezioni if s["righe"] > 0]


def git(*args):
    out = subprocess.run(["git", "-C", ROOT] + list(args),
                         capture_output=True, text=True)
    return out.stdout.strip(), out.returncode


def leggi_capitoli():
    capitoli = []
    if not os.path.isdir(CAPITOLI):
        return capitoli
    for nome in sorted(os.listdir(CAPITOLI)):
        if not nome.endswith(".tex"):
            continue
        with open(os.path.join(CAPITOLI, nome), "rb") as f:
            testo = f.read().decode("utf-8")
        interi, sezioni = set(), set()
        for voce in re.findall(r"^%\s*copre:\s*(\S+)\s*$", testo, re.M):
            if "#" in voce:
                doc, sez = voce.split("#", 1)
                sezioni.add((doc, sez))
            else:
                interi.add(voce)
        commit = re.search(r"^%\s*verificato-al-commit:\s*(\S+)\s*$", testo, re.M)
        chiavi = set()
        for gruppo in re.findall(r"\\cite\{([^}]+)\}", testo):
            for k in gruppo.split(","):
                if k.strip():
                    chiavi.add(k.strip())
        capitoli.append({"file": "tesi/capitoli/" + nome, "interi": interi,
                         "sezioni": sezioni, "citazioni": chiavi,
                         "commit": commit.group(1) if commit else None})
    return capitoli


def leggi_esenzioni():
    esenti_doc, esenti_sez, malformate = {}, {}, []
    if not os.path.exists(ESENZIONI):
        return esenti_doc, esenti_sez, malformate
    with open(ESENZIONI, "rb") as f:
        for riga in f.read().decode("utf-8").splitlines():
            riga = riga.strip()
            if not riga or riga.startswith("##"):
                continue
            if "#" not in riga:
                malformate.append(riga)
                continue
            # L'ultimo cancelletto introduce il motivo; uno precedente, se c'è, separa il
            # documento dalla sezione.
            testa, motivo = riga.rsplit("#", 1)
            testa, motivo = testa.strip(), motivo.strip()
            if not testa or not motivo:
                malformate.append(riga)
                continue
            if "#" in testa:
                doc, sez = testa.split("#", 1)
                esenti_sez[(doc.strip(), sez.strip())] = motivo
            else:
                esenti_doc[testa] = motivo
    return esenti_doc, esenti_sez, malformate


def igiene_tex():
    """Errori di sorgente LaTeX che si manifestano solo nel PDF composto.

    Due casi reali, entrambi incontrati durante la stesura. Il backtick di Markdown, che in
    LaTeX non delimita il monospazio ma apre una virgoletta: il documento compila senza
    lamentarsi e il difetto si vede soltanto rileggendo la pagina. E i caratteri di
    controllo, che entrano quando una sostituzione automatica interpreta come sequenza di
    escape ciò che doveva essere un backslash seguito da una lettera: la macro perde il
    backslash, il suo nome perde la prima lettera, e il testo esce in chiaro nel PDF.
    """
    BS = chr(92)
    NL = chr(10)
    # Perché il controllo guarda il contesto e non la sottostringa. Il nome di una
    # macro è spesso contenuto in quello di un'altra: SECTIONBS è dentro SUBSECTIONBS,
    # REFBS è dentro PAGEREFBS. Cercare il nome come sottostringa segnalerebbe ogni
    # titolo del documento. Una macro legittima è preceduta da un backslash, una
    # mutilata da qualunque cosa che non sia una lettera: un solo lookbehind che escluda
    # entrambi riconosce il secondo caso senza toccare il primo.
    #
    # L'elenco tiene insieme due categorie. I nomi interi valgono per il caso in cui il
    # solo backslash sia caduto. I frammenti valgono per il caso in cui la sostituzione
    # abbia mangiato backslash e lettera iniziale insieme, che è quanto è avvenuto con
    # sed su LABELBS diventato ABELBS: la compilazione si arresta su una macro che non
    # esiste, e il nome sopravvive privo della prima lettera.
    NOMI = ("file", "term", "hx", "bin", "cite", "emph", "texttt", "SI",
            "label", "ref", "chapter", "section", "subsection", "input",
            "abel", "hapter", "ection", "nput", "ite", "ile", "erm", "ubsection")
    SOSPETTE = re.compile(r"(?<![A-Za-z" + BS + BS + BS + BS + r"])(" +
                          "|".join(NOMI) + r")" + BS + "{")
    problemi = []
    if not os.path.isdir(CAPITOLI):
        return problemi
    for nome in sorted(os.listdir(CAPITOLI)):
        if not nome.endswith(".tex"):
            continue
        rel = "tesi/capitoli/" + nome
        with open(os.path.join(CAPITOLI, nome), "rb") as f:
            testo = f.read().decode("utf-8")

        n = testo.count(chr(96))
        if n:
            problemi.append("%s contiene %d backtick: in LaTeX aprono una virgoletta, "
                            "non il monospazio" % (rel, n))

        ctrl = sorted(set(ord(c) for c in testo if ord(c) < 32 and c != NL))
        if ctrl:
            problemi.append("%s contiene i caratteri di controllo %s, probabile sequenza "
                            "di escape interpretata da una sostituzione" % (rel, ctrl))

        for numero, riga in enumerate(testo.split(NL), 1):
            for m in SOSPETTE.finditer(riga):
                problemi.append("%s riga %d: %s{ non ha il backslash, o è il residuo di "
                                "una macro a cui è stata mangiata la lettera iniziale"
                                % (rel, numero, m.group(1)))
    return problemi



def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--scoperte", action="store_true",
                    help="stampa solo le sezioni da distribuire, dalla più grande")
    args = ap.parse_args()

    head, rc = git("rev-parse", "--short", "HEAD")
    if rc != 0:
        head = None

    capitoli = leggi_capitoli()
    esenti_doc, esenti_sez, malformate = leggi_esenzioni()
    chiavi_bib = None
    if os.path.exists(BIBLIOGRAFIA):
        with open(BIBLIOGRAFIA, "rb") as f:
            chiavi_bib = set(re.findall(r"\\bibitem\{([^}]+)\}",
                                        f.read().decode("utf-8")))

    reclamati_interi, reclamate_sezioni = set(), set()
    for c in capitoli:
        reclamati_interi |= c["interi"]
        reclamate_sezioni |= c["sezioni"]

    errori, avvisi = [], []

    for problema in igiene_tex():
        print("IGIENE DEL SORGENTE LATEX: %s" % problema)
        errori.append("igiene del sorgente")
    if errori:
        print()
    scoperte = []
    righe_totali = righe_coperte = 0
    slug_esistenti = set()

    for rel in documenti():
        sezioni = sezioni_di(rel)
        doc_coperto = rel in reclamati_interi or rel in esenti_doc
        for s in sezioni:
            slug_esistenti.add((rel, s["slug"]))
            righe_totali += s["righe"]
            chiave = (rel, s["slug"])
            if doc_coperto or chiave in reclamate_sezioni or chiave in esenti_sez:
                righe_coperte += s["righe"]
            else:
                scoperte.append((rel, s["slug"], s["titolo"], s["righe"]))

    righe_scoperte = righe_totali - righe_coperte

    slug_sconosciuti = [(d, s) for d, s in sorted(reclamate_sezioni | set(esenti_sez))
                        if (d, s) not in slug_esistenti]

    stale = []
    for c in capitoli:
        if not c["commit"] or head is None:
            continue
        _, rc = git("cat-file", "-e", c["commit"] + "^{commit}")
        if rc != 0:
            errori.append("%s dichiara il commit %s, inesistente"
                          % (c["file"], c["commit"]))
            continue
        percorsi = sorted(c["interi"] | {d for d, _ in c["sezioni"]})
        if not percorsi:
            continue
        out, _ = git("diff", "--name-only", c["commit"] + "..HEAD", "--", *percorsi)
        cambiati = [r for r in out.splitlines() if r.strip()]
        if cambiati:
            stale.append((c["file"], c["commit"], cambiati))

    citate = set()
    for c in capitoli:
        citate |= c["citazioni"]
    orfane = sorted(citate - chiavi_bib) if chiavi_bib is not None else []
    mai_citate = sorted(chiavi_bib - citate) if chiavi_bib is not None else []

    if args.scoperte:
        print("sezioni non ancora reclamate, dalla più grande:\n")
        for rel, sl, tit, n in sorted(scoperte, key=lambda x: -x[3]):
            print("  %4d righe  %s#%s" % (n, rel, sl))
            print("              %s" % tit[:88])
        print("\n%d sezioni, %d righe di contenuto da distribuire"
              % (len(scoperte), righe_scoperte))
        return 1 if scoperte else 0

    pct = (100.0 * righe_coperte / righe_totali) if righe_totali else 100.0
    print("Copertura del contenuto nella tesi (HEAD = %s)\n" % (head or "n/d"))
    print("  capitoli              %d" % len(capitoli))
    print("  documenti da coprire  %d" % len(documenti()))
    print("  righe di contenuto    %d, coperte %d (%.1f%%)"
          % (righe_totali, righe_coperte, pct))
    print("  sezioni scoperte      %d, per %d righe" % (len(scoperte), righe_scoperte))
    if chiavi_bib is not None:
        print("  bibliografia          %d voci, citate %d" % (len(chiavi_bib), len(citate)))
    print()

    if stale:
        print("CAPITOLI DA RILEGGERE, un documento coperto è cambiato dopo la verifica:")
        for f, commit, cambiati in stale:
            print("  %s (a %s): %s" % (f, commit, ", ".join(cambiati)))
        print()
        errori.append("%d capitoli in drift" % len(stale))

    if slug_sconosciuti:
        print("SEZIONI DICHIARATE CHE NON ESISTONO, titolo riscritto o slug sbagliato:")
        for doc, sez in slug_sconosciuti:
            print("  %s#%s" % (doc, sez))
        print()
        errori.append("%d sezioni dichiarate inesistenti" % len(slug_sconosciuti))

    if orfane:
        print("CITAZIONI SENZA VOCE in bibliografia:")
        for k in orfane:
            print("  \\cite{%s}" % k)
        print()
        errori.append("%d citazioni orfane" % len(orfane))

    if malformate:
        print("ESENZIONI SENZA MOTIVO in tesi/non-coperti.txt:")
        for r in malformate:
            print("  %s" % r)
        print()
        errori.append("%d esenzioni malformate" % len(malformate))

    if scoperte:
        print("le dieci sezioni scoperte più grandi, per orientare il lavoro:")
        for rel, sl, tit, n in sorted(scoperte, key=lambda x: -x[3])[:10]:
            print("  %4d righe  %s#%s" % (n, rel, sl))
        print("\n  elenco completo con --scoperte\n")
        avvisi.append("%.1f%% del contenuto ancora da distribuire" % (100.0 - pct))

    if mai_citate:
        print("avviso, %d fonti in bibliografia che nessun capitolo cita\n"
              % len(mai_citate))

    if args.verbose:
        print("dettaglio dei capitoli:")
        for c in capitoli:
            quante = len(c["interi"]) + len(c["sezioni"])
            print("  %s: %d dichiarazioni, %d citazioni, a %s"
                  % (c["file"], quante, len(c["citazioni"]), c["commit"]))
        if esenti_doc or esenti_sez:
            print("\nesenzioni dichiarate:")
            for k, v in sorted(esenti_doc.items()):
                print("  %s: %s" % (k, v))
            for (d, s), v in sorted(esenti_sez.items()):
                print("  %s#%s: %s" % (d, s, v))
        print()

    if errori:
        print("%d problemi: %s" % (len(errori), "; ".join(errori)))
        return 1
    if scoperte:
        print("nessun errore, ma la copertura non è completa: %s" % "; ".join(avvisi))
        return 0
    print("copertura completa, nessun problema")
    return 0


if __name__ == "__main__":
    sys.exit(main())
