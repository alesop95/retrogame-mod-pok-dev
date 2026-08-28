#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la bibliografia della tesi dalla stessa tabella che genera le note di fonte.

Perché esiste
--------------
La tesi deve citare una fonte per ogni affermazione, e quelle fonti sono le stesse che
`SOURCES.md` registra e che `docs/fonti/` descrive. Scriverle a mano una terza volta
significherebbe garantire che le tre copie divergano: è la ragione per cui questo
strumento legge la tabella `FONTI` di `build-source-map.py` e ne produce la bibliografia,
esattamente come quello ne produce le note. La tabella resta la fonte unica.

Perché un ambiente thebibliography e non un file .bib
------------------------------------------------------
La TinyTeX di questa macchina è minimale e `tlmgr` rifiuta di installare pacchetti
senza aggiornare prima se stesso, come documenta il preambolo dei report a proposito di
`fancyhdr` e `siunitx`. Un file `.bib` richiederebbe BibTeX o biber e uno stile
bibliografico, cioè tre dipendenze in più e un passaggio di compilazione in più.
L'ambiente `thebibliography` è invece parte del nucleo di LaTeX: `\\cite{chiave}`
funziona senza alcun pacchetto e senza alcun passaggio esterno. Il controllo che BibTeX
farebbe, cioè segnalare le citazioni senza voce e le voci senza citazione, lo fa
`check-thesis-coverage.py`, e lo fa meglio perché conosce anche la copertura dei
documenti sorgente.

La chiave di citazione è lo slug della fonte, quindi `\\cite{pokered}` nella tesi e
`docs/fonti/pokered.md` nel vault sono la stessa cosa vista da due parti.

Uso
---
    python tools/build-bibliography.py
    python tools/build-bibliography.py --check     verifica senza scrivere
"""

import argparse
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORGENTE = os.path.join(ROOT, "tools", "build-source-map.py")
USCITA = os.path.join(ROOT, "tesi", "bibliografia.tex")

# I nomi dei livelli, per rendere leggibile la gerarchia dentro la voce bibliografica.
# Coincidono con le intestazioni di SOURCES.md, e ripeterli qui è accettabile perché
# sono cinque etichette stabili, non un secondo registro.
LIVELLI = {
    1: "disassemblato o documentazione dell'hardware",
    2: "wiki o riferimento di dominio",
    3: "implementazione di riferimento",
    4: "articolo, blog o ricerca applicata",
    5: "forum o community",
}


def carica_fonti():
    """Importa la tabella FONTI dal generatore delle note.

    Il nome del file contiene trattini e non è quindi un identificatore Python valido,
    per questo si passa da importlib invece di un import ordinario.
    """
    spec = importlib.util.spec_from_file_location("build_source_map", SORGENTE)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.FONTI, getattr(modulo, "RIFERIMENTI_TEORICI", [])


def escape_tex(testo):
    """Neutralizza i caratteri che LaTeX interpreta.

    Si tratta di testo descrittivo scritto in italiano, quindi i casi reali sono pochi:
    la percentuale, che aprirebbe un commento, l'e commerciale e il carattere di
    sottolineatura, che compaiono nei nomi dei repository, e le graffe.
    """
    sostituzioni = (
        ("\\", r"\textbackslash{}"),
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
    )
    for vecchio, nuovo in sostituzioni:
        testo = testo.replace(vecchio, nuovo)
    return testo


def url_tex(url):
    """Un indirizzo dentro \\url{} non va neutralizzato come il testo, ma protetto.

    `hyperref` gestisce da sé i caratteri speciali dentro \\url, a condizione che non
    ci siano graffe sbilanciate. Si sostituisce quindi soltanto il carattere di
    percentuale, che il lettore di LaTeX tronca prima che \\url lo veda.
    """
    return url.replace("%", r"\%")


def genera(fonti, teorici):
    righe = []
    righe.append("% " + "=" * 69)
    righe.append("% tesi/bibliografia.tex - GENERATO, non modificare a mano")
    righe.append("% " + "=" * 69)
    righe.append("% Prodotto da tools/build-bibliography.py dalla tabella FONTI di")
    righe.append("% tools/build-source-map.py, che è la stessa da cui nascono le note di")
    righe.append("% docs/fonti/. Modificare quella tabella e rigenerare: una correzione fatta")
    righe.append("% qui sparisce alla corsa successiva.")
    righe.append("%")
    righe.append("% La chiave di ogni voce è lo slug della fonte, quindi \\cite{pokered} qui e")
    righe.append("% docs/fonti/pokered.md nel vault sono la stessa fonte vista da due parti.")
    righe.append("")

    # L'argomento di thebibliography dimensiona il rientro dell'elenco sulla larghezza
    # dell'etichetta più larga, e le etichette qui sono i numeri progressivi che LaTeX
    # genera, non le chiavi di citazione. Passare la chiave più lunga, come faceva una
    # prima versione di questo generatore, produceva un rientro di venti caratteri per
    # ospitare etichette che ne occupano due: da qui la colonna di spazio bianco che
    # rendeva la bibliografia illeggibile. Si passa quindi il numero più largo possibile.
    piu_larga = "9" * len(str(len(fonti) + len(teorici)))
    righe.append(r"\begin{thebibliography}{%s}" % piu_larga)
    righe.append(r"\addcontentsline{toc}{chapter}{Bibliografia}")
    # A bandiera e non giustificato: su una voce breve che contiene un
    # indirizzo lungo la giustificazione è precisamente ciò che spinge la
    # riga fuori dal margine, perché' il compositore non ha spazi elastici a
    # sufficienza per rientrare.
    righe.append(r"\raggedright")
    # Solo i parametri che hanno effetto dentro una lista già' iniziata: labelsep e
    # itemsep vengono riletti a ogni voce, mentre leftmargin e itemindent sono fissati
    # dal egin e cambiarli qui non farebbe nulla. Il rientro vero lo determina
    # l'argomento passato sopra.
    righe.append(r"\setlength{\labelsep}{0.5em}")
    righe.append(r"\setlength{\itemsep}{0.8ex}")
    righe.append("")

    for slug, nome, url, livello, letto, track, abstract, _perche, _serve, _rel in fonti:
        etichetta = LIVELLI.get(livello, "fonte")
        stato = "letta" if letto else "catalogata e non letta"
        voce = [r"\bibitem{%s}" % slug]
        voce.append(r"  \textbf{%s}." % escape_tex(nome))
        voce.append(r"  \\ \url{%s}" % url_tex(url))
        voce.append(r"  \\ \emph{Livello %d, %s; %s. Track: %s.}"
                    % (livello, escape_tex(etichetta), escape_tex(stato),
                       escape_tex(", ".join(track))))
        # L'abstract entra in bibliografia perché in questo progetto una fonte vale per
        # ciò su cui la si può citare, e quel dettaglio deve stare accanto alla voce.
        voce.append(r"  \\ %s" % escape_tex(abstract))
        righe.append("\n".join(voce))
        righe.append("")

    # I riferimenti teorici, con l'intestazione che ne dichiara la natura. Senza quella
    # dichiarazione la bibliografia affermerebbe implicitamente che sono stati consultati
    # come le altre voci, e non è così: sono citati per attribuzione del concetto.
    if teorici:
        righe.append(r"\medskip")
        righe.append(
            r"\noindent \textbf{Riferimenti teorici.} Le voci che seguono sono la "
            r"letteratura canonica dei concetti impiegati nell'analisi quantitativa, "
            r"citate per attribuzione del concetto e non come fonti consultate nel corso "
            r"del lavoro: la definizione di entropia si attribuisce a Shannon perché è "
            r"sua, non perché quell'articolo sia stato aperto qui. I numeri di pagina "
            r"non sono riportati dove non sono stati verificati.\\[0.8ex]")
        righe.append("")
        for slug, autori, titolo, sede, anno, per_cosa in teorici:
            voce = [r"\bibitem{%s}" % slug]
            voce.append(r"  \textbf{%s}. %s." % (escape_tex(autori), escape_tex(titolo)))
            voce.append(r"  \\ %s, %s." % (escape_tex(sede), escape_tex(anno)))
            voce.append(r"  \\ \emph{Riferimento teorico, citato per attribuzione.}")
            voce.append(r"  \\ %s" % escape_tex(per_cosa))
            righe.append("\n".join(voce))
            righe.append("")
    righe.append(r"\end{thebibliography}")
    righe.append("")
    return "\n".join(righe)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="verifica che il file su disco sia aggiornato, senza scrivere")
    args = ap.parse_args()

    fonti, teorici = carica_fonti()
    testo = genera(fonti, teorici)

    if args.check:
        if not os.path.exists(USCITA):
            print("la bibliografia non esiste ancora: %s" % USCITA)
            return 1
        with open(USCITA, "rb") as f:
            attuale = f.read().decode("utf-8")
        if attuale != testo:
            print("la bibliografia è disallineata dalla tabella FONTI: rigenerare")
            return 1
        print("%d voci, bibliografia allineata" % len(fonti))
        return 0

    os.makedirs(os.path.dirname(USCITA), exist_ok=True)
    with open(USCITA, "wb") as f:
        f.write(testo.encode("utf-8"))
    # Il conteggio distingue le due tranche: dire soltanto len(fonti) mentre il file
    # ne contiene anche i riferimenti teorici sarebbe un rapporto che sottostima.
    print("%d voci scritte in %s: %d fonti di dominio e %d riferimenti teorici"
          % (len(fonti) + len(teorici), USCITA, len(fonti), len(teorici)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
