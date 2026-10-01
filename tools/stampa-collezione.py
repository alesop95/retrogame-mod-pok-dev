#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone il catalogo stampabile della collezione per HOME, un PDF con ogni esemplare per copia, box e posto.

Perché esiste
-------------
Il proprietario ha chiesto, il 2026-09-30, un PDF separato e stampabile di tutta la collezione, aggiornato man mano
che il lavoro procede. Il catalogo si compone dai dati e non si scrive a mano: `tools/pkhex-elenco-copie` legge le
copie dei salvataggi, che sono ciò che arriva in HOME, e questo strumento ne fa un documento LaTeX e lo compila con
LuaLaTeX, l'ambiente della tesi. A ogni aggiornamento delle copie si rilanciano i due strumenti.

Il documento si apre con il riepilogo per gruppi, lo stesso di `pokedex-home-completo/COPIE-PER-HOME.md`, e prosegue
con una sezione per copia e una tabella per box, nell'ordine in cui il box si vede in gioco. Il margine sinistro è
largo per i fori di un quaderno ad anelli. Gli allenatori con nome giapponese si stampano con un carattere di
ripiego che ha quei glifi.

Uso
---
    python tools/stampa-collezione.py _notes/stampa/collezione.json _notes/stampa/collezione.tex
    python tools/stampa-collezione.py _notes/stampa/collezione.json _notes/stampa/collezione.tex --pdf
"""

import argparse
import datetime
import io
import json
import os
import subprocess
import sys

SOSTITUZIONI = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
                "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}

GIOCHI = {"RD": "Rosso", "GN": "Verde", "BU": "Blu", "YW": "Giallo", "GD": "Oro", "SI": "Argento", "C": "Cristallo",
          "R": "Rubino", "S": "Zaffiro", "E": "Smeraldo", "FR": "Rosso Fuoco", "LG": "Verde Foglia", "CXD": "Colosseum/XD",
          "D": "Diamante", "P": "Perla", "Pt": "Platino", "HG": "HeartGold", "SS": "SoulSilver",
          "B": "Nero", "W": "Bianco", "B2": "Nero 2", "W2": "Bianco 2", "X": "X", "Y": "Y", "OR": "Rubino Omega",
          "AS": "Zaffiro Alpha", "SN": "Sole", "MN": "Luna", "US": "Ultrasole", "UM": "Ultraluna"}


def tex(testo):
    return "".join(SOSTITUZIONI.get(c, c) for c in str(testo))


def codice(origine):
    """Il codice della checklist quando il file lo porta nel nome, altrimenti il nome del file."""
    nome = os.path.splitext(os.path.basename(origine))[0]
    parti = nome.split("-")
    if len(parti) >= 3 and parti[0] == "EVT":
        return "-".join(parti[:3])
    # I file del primo lotto di terza generazione portano numero, nome dell'evento e specie: basta il numero e l'evento.
    if len(parti) >= 3 and parti[0].isdigit():
        nome = "-".join(parti[:2])
    # La colonna è stretta: un nome lungo si tronca, e il nome intero resta nel rapporto della copia.
    return nome if len(nome) <= 16 else nome[:15] + "…"


def componi(dati):
    oggi = datetime.date.today().isoformat()
    righe = [r"""\documentclass[9pt,a4paper]{extarticle}
\usepackage[top=15mm,bottom=15mm,left=28mm,right=12mm]{geometry}
\usepackage{fontspec}
\directlua{luaotfload.add_fallback("giapponese", {"YuGothic:mode=harf;", "MS Gothic:mode=harf;", "Malgun Gothic:mode=harf;", "Microsoft YaHei:mode=harf;", "Microsoft JhengHei:mode=harf;"})}
\setmainfont{Arial}[RawFeature={fallback=giapponese}]
\usepackage{longtable,booktabs,array}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\usepackage[italian]{babel}
\setlength{\tabcolsep}{2.5pt}
\renewcommand{\arraystretch}{1.05}
\pagestyle{plain}
\begin{document}
""",
              r"\section*{La collezione per HOME}",
              r"Catalogo composto il %s da \texttt{tools/stampa-collezione.py} sulle copie dei salvataggi, cioè su ciò "
              r"che arriva in HOME. Per ogni esemplare: box e posto nella copia, specie e forma, livello, sesso e "
              r"cromatico (\textbf{C}), allenatore originale e identificativo, lingua, gioco d'origine, luogo "
              r"d'incontro, sfera, e il codice della checklist o il file del lotto da cui viene." % oggi, "",
              r"\begin{longtable}{p{62mm}rr}", r"\toprule", r"Copia & Esemplari & Non conformi\\", r"\midrule"]
    for c in dati["copie"]:
        nc = sum(1 for e in c["esemplari"] if not e["conforme"])
        righe.append(r"%s & %d & %d\\" % (tex(c["gruppo"]), len(c["esemplari"]), nc))
    righe += [r"\bottomrule", r"\end{longtable}", "",
              r"Una copia del gruppo della decisione finale può avere esemplari non conformi nel contesto in cui "
              r"PKHeX apre il salvataggio: è la ragione per cui sta in quel gruppo.", r"\clearpage"]
    for c in dati["copie"]:
        righe.append(r"\section*{%s}" % tex(c["gruppo"]))
        righe.append(r"Gioco: %s, %d esemplari." % (tex(GIOCHI.get(c["gioco"], c["gioco"])), len(c["esemplari"])))
        per_box = {}
        for e in c["esemplari"]:
            per_box.setdefault(e["box"], []).append(e)
        for box in sorted(per_box):
            righe += [r"\subsection*{Box %d}" % box,
                      r"\begin{longtable}{r L{25mm} r l L{25mm} L{17mm} L{30mm} L{15mm} L{22mm}}", r"\toprule",
                      r"Posto & Specie & Liv. & & Allenatore & Lingua, gioco & Luogo & Sfera & Codice\\",
                      r"\midrule", r"\endhead"]
            for e in sorted(per_box[box], key=lambda x: x["posto"]):
                specie = e["specie"] + (" (%s)" % e["forma"] if e["forma"] else "")
                segni = e["sesso"] + (" C" if e["cromatico"] else "")
                righe.append(r"%d & %s & %d & %s & %s %s & %s, %s & %s & %s & %s\\" % (
                    e["posto"], tex(specie), e["livello"], tex(segni), tex(e["allenatore"]), tex(e["id"]),
                    tex(e["lingua"][:3]), tex(GIOCHI.get(e["gioco"], e["gioco"])), tex(e["luogo"]),
                    tex(e["sfera"]), tex(codice(e["origine"]))))
            righe += [r"\bottomrule", r"\end{longtable}"]
        righe.append(r"\clearpage")
    righe.append(r"\end{document}")
    return "\n".join(righe) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dati", help="JSON di tools/pkhex-elenco-copie")
    ap.add_argument("uscita", help="file .tex da scrivere")
    ap.add_argument("--pdf", action="store_true", help="compila anche il PDF con lualatex, due passate")
    a = ap.parse_args()
    dati = json.load(io.open(a.dati, encoding="utf-8"))
    io.open(a.uscita, "w", encoding="utf-8").write(componi(dati))
    print("scritto", a.uscita)
    if a.pdf:
        cartella = os.path.dirname(os.path.abspath(a.uscita))
        for _ in range(2):
            r = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", os.path.basename(a.uscita)],
                               cwd=cartella, capture_output=True, text=True, encoding="utf-8", errors="replace")
            if r.returncode != 0:
                print(r.stdout[-3000:])
                sys.exit("lualatex non ha compilato il documento")
        print("scritto", os.path.splitext(a.uscita)[0] + ".pdf")


if __name__ == "__main__":
    main()
