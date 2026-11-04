#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Il design system del progetto: dai token agli stili che lo applicano.

Perché esiste
-------------
Il proprietario ha chiesto il 2026-11-04 (ADR-110) un design system proprio per i documenti della collezione e per i
PDF stampabili, retrò e ispirato a Ken Sugimori, costruito sulla suite ArtCraft installata in locale; e lo stesso
giorno (ADR-111) che ogni esemplare abbia un pedigree nella documentazione e nella stampa. Gli stili si applicano da
due catene diverse: LuaLaTeX, che compone il catalogo stampabile da `tools/stampa-collezione.py`, e le applicazioni
Craft, che leggono `.claude/craft-stile.json` attraverso `craft-documento.py --stile auto`. Se i due stili si
scrivessero a mano divergerebbero alla prima correzione, quindi la fonte è una sola,
`pokedex-home-completo/design-system/tokens.json`, e questo strumento ne ricava gli altri due file.

I caratteri sono tutti con licenza SIL Open Font License e vengono dal repository dei Google Fonts a un commit
fissato nei token. Non entrano in Git e non si installano nel sistema: si scaricano in `_notes/design-system/caratteri/`
e LuaLaTeX li carica per percorso. L'impronta SHA-256 di ogni file si registra nei token alla prima corsa e si
verifica a ogni corsa successiva, così che un file cambiato a monte si veda invece di passare.

Uso
---
    python tools/design-system.py caratteri          scarica o verifica i caratteri
    python tools/design-system.py genera             scrive collezione-stile.tex e .claude/craft-stile.json
    python tools/design-system.py genera --check     esce con 1 se i file ricavati non corrispondono ai token
    python tools/design-system.py campionario        compone il campionario in _notes/design-system/
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA = os.path.join(RADICE, "pokedex-home-completo", "design-system")
TOKEN = os.path.join(CARTELLA, "tokens.json")
STILE_TEX = os.path.join(CARTELLA, "collezione-stile.tex")
STILE_CRAFT = os.path.join(RADICE, ".claude", "craft-stile.json")
CARATTERI = os.path.join(RADICE, "_notes", "design-system", "caratteri")
LAVORO = os.path.join(RADICE, "_notes", "design-system")


def leggi_token():
    with open(TOKEN, encoding="utf-8") as f:
        return json.load(f)


def scrivi_lf(percorso, testo):
    with open(percorso, "w", encoding="utf-8", newline="\n") as f:
        f.write(testo)


def caratteri(tok):
    src = tok["sorgente_caratteri"]
    os.makedirs(CARATTERI, exist_ok=True)
    nuove = {}
    errori = 0
    for nome, percorso in src["percorsi"].items():
        dest = os.path.join(CARATTERI, nome)
        if not os.path.exists(dest):
            url = "https://raw.githubusercontent.com/google/fonts/%s/%s" % (src["commit"], percorso)
            with urllib.request.urlopen(url, timeout=60) as r:
                dati = r.read()
            with open(dest, "wb") as f:
                f.write(dati)
            print("scaricato  %s (%d byte)" % (nome, len(dati)))
        h = hashlib.sha256(open(dest, "rb").read()).hexdigest()
        atteso = src["sha256"].get(nome)
        if atteso is None:
            nuove[nome] = h
        elif atteso != h:
            print("IMPRONTA DIVERSA  %s: attesa %s, trovata %s" % (nome, atteso, h))
            errori += 1
        else:
            print("verificato %s" % nome)
    if nuove:
        src["sha256"].update(nuove)
        scrivi_lf(TOKEN, json.dumps(tok, ensure_ascii=False, indent=2) + "\n")
        print("registrate nei token %d impronte nuove" % len(nuove))
    return 1 if errori else 0


def stile_tex(tok):
    c, g, ca = tok["colori"], tok["geometria"], tok["caratteri"]
    righe = [
        "% Generato da tools/design-system.py dai token di pokedex-home-completo/design-system/tokens.json.",
        "% Non si modifica a mano: si cambia il token e si rigenera. Chi lo include definisce prima",
        "% \\DScaratteri, la cartella dei caratteri con la barra finale.",
        "\\usepackage{fontspec}",
        "\\usepackage{xcolor}",
        "\\usepackage{graphicx}",
        "\\usepackage{tcolorbox}",
        "\\tcbuselibrary{skins}",
        "\\directlua{luaotfload.add_fallback(\"asia\", {\"Malgun Gothic:mode=harf;\", \"Microsoft YaHei:mode=harf;\", \"Microsoft JhengHei:mode=harf;\", \"YuGothic:mode=harf;\"})}",
    ]

    def famiglia(comando, voce, principale=False):
        v = ca[voce]
        opz = "Path=\\DScaratteri, UprightFont=%s" % v["normale"]
        if "grassetto" in v:
            opz += ", BoldFont=%s" % v["grassetto"]
        opz += ", RawFeature={fallback=asia}"
        if principale:
            return "\\setmainfont{%s}[%s]" % (v["normale"], opz)
        return "\\newfontfamily%s{%s}[%s]" % (comando, v["normale"], opz)

    righe.append(famiglia(None, "testo", principale=True))
    righe.append(famiglia("\\DStitoli", "titoli"))
    righe.append(famiglia("\\DSdati", "dati"))
    righe.append(famiglia("\\DSpixel", "pixel"))
    righe.append("\\setmonofont{%s}[Path=\\DScaratteri, UprightFont=%s, BoldFont=%s, Scale=0.92]"
                 % (ca["codice"]["normale"], ca["codice"]["normale"], ca["codice"]["grassetto"]))
    for nome, hexa in c.items():
        righe.append("\\definecolor{DS%s}{HTML}{%s}" % (nome.replace("_", ""), hexa))
    for n, hexa in tok["generazioni"].items():
        righe.append("\\definecolor{DSgen%s}{HTML}{%s}" % ("ABCDEFG"[int(n) - 1], hexa))
    for stato, colore in tok["stati"].items():
        righe.append("\\colorlet{DSstato%s}{DS%s}" % (stato.replace("_", ""), colore.replace("_", "")))
    righe += [
        "\\color{DSinchiostro}",
        "% La scheda di un esemplare: carta crema, filetto seppia, angoli tondi, striscia del colore della generazione.",
        "\\newtcolorbox{DSscheda}[1]{enhanced, colback=DScarta, colframe=DSfiletto, boxrule=%spt, arc=%smm,"
        % (g["filetto_pt"], g["raggio_mm"]),
        "  left=3mm, right=2mm, top=1.5mm, bottom=1.5mm, before skip=1.2mm, after skip=1.2mm,",
        "  overlay={\\fill[#1] ([xshift=0.3pt]frame.north west) rectangle ([xshift=%spt]frame.south west);}}"
        % g["striscia_generazione_pt"],
        "% La miniatura dell'illustrazione di Sugimori, nella sua finestra bianca: le illustrazioni hanno lo sfondo bianco,",
        "% e una cornice propria lo rende voluto invece che una macchia sulla carta crema.",
        "% Il primo argomento, facoltativo, è la larghezza dell'illustrazione; la finestra aggiunge 1,6 millimetri.",
        "\\newcommand{\\DSminiatura}[2][%smm]{\\tcbox[colback=white, colframe=DSfiletto, boxrule=0.4pt, arc=1.6mm, boxsep=0pt,"
        " left=0.6mm, right=0.6mm, top=0.6mm, bottom=0.6mm]{\\includegraphics[width=#1]{#2}}}"
        % (g["miniatura_mm"] - 2),
        "% Il numero di Pokédex con il carattere a punti, come sullo schermo del Game Boy.",
        "\\newcommand{\\DSnumero}[1]{{\\DSpixel\\color{DSseppia}\\##1}}",
        "% L'etichetta di un campo del pedigree.",
        "% Prende la dimensione del contesto, così che etichetta e valore abbiano lo stesso corpo.",
        "\\newcommand{\\DScampo}[1]{{\\DSdati\\color{DSseppia}#1}}",
        "% Il bollino dello stato dell'esemplare.",
        "\\newcommand{\\DSstato}[2]{\\tcbox[on line, colback=#1!18, colframe=#1, boxrule=0.4pt, arc=1.2mm, boxsep=0pt,"
        " left=1.2mm, right=1.2mm, top=0.4mm, bottom=0.4mm]{\\DSdati\\scriptsize\\bfseries\\color{DSinchiostro}#2}}",
    ]
    return "\n".join(righe) + "\n"


def stile_craft(tok):
    ca, c, d = tok["caratteri"], tok["colori"], tok["dimensioni_pt"]
    s = {
        "nome": tok["nome"],
        "descrizione": "Generato da tools/design-system.py dai token di pokedex-home-completo/design-system/tokens.json: "
                       + tok["descrizione"],
        "font_titoli": ca["titoli"]["famiglia"],
        "font_testo": ca["testo"]["famiglia"],
        "colore_titoli": c["rosso"],
        "colore_testo": c["inchiostro"],
        "font_codice": ca["codice"]["famiglia"],
        "dimensioni": {k: d[k] for k in ("Title", "Heading 1", "Heading 2", "Heading 3", "Normal", "Code")},
        "colori_slide": {"dk1": "#" + c["inchiostro"], "lt1": "#" + c["carta"], "dk2": "#" + c["rosso"],
                         "lt2": "#" + c["carta_scura"], "accent1": "#" + c["rosso"], "accent2": "#" + c["blu"],
                         "hlink": "#" + c["blu"]},
    }
    return json.dumps(s, ensure_ascii=False, indent=2) + "\n"


def genera(tok, check):
    attesi = {STILE_TEX: stile_tex(tok), STILE_CRAFT: stile_craft(tok)}
    diversi = 0
    for p, testo in attesi.items():
        ora = open(p, encoding="utf-8").read() if os.path.exists(p) else None
        if ora == testo:
            print("allineato  %s" % os.path.relpath(p, RADICE))
            continue
        if check:
            print("DA RIGENERARE  %s" % os.path.relpath(p, RADICE))
            diversi += 1
        else:
            scrivi_lf(p, testo)
            print("scritto    %s" % os.path.relpath(p, RADICE))
    return 1 if diversi else 0


CAMPIONARIO = r"""\documentclass[10pt]{article}
\usepackage[a4paper,top=%(mv)smm,bottom=%(mv)smm,left=%(ma)smm,right=%(mm)smm]{geometry}
\def\DScaratteri{%(car)s/}
\input{%(stile)s}
\usepackage[italian]{babel}
\usepackage{array}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
{\DStitoli\bfseries\fontsize{24}{28}\selectfont\color{DSrosso} Campionario del design system}\par
{\DSdati\small\color{DSseppia} pokedex-sugimori-retro, versione %(ver)s. Generato da tools/design-system.py.}\par\medskip
{\DStitoli\bfseries\fontsize{13}{16}\selectfont Caratteri}\par\smallskip
{\DStitoli\bfseries Titoli, M PLUS Rounded 1c: La collezione per HOME}\par
{Testo, Zen Old Mincho: il pedigree racconta da dove viene ogni esemplare, e i nomi giapponesi ミュウ, ピカチュウ si leggono senza ripiego.}\par
{\DSdati Dati, M PLUS Rounded 1c: livello 10, Poké Ball, Rubino, conforme}\par
{\DSpixel Pixel, DotGothic16: \#151 \#025 ABCDEF 0123456789}\par
{\ttfamily Codice, IBM Plex Mono: 3f9a 0c21 e7b4 sha256}\par\medskip
{\DStitoli\bfseries\fontsize{13}{16}\selectfont Colori}\par\smallskip
%(colori)s
\par\medskip
{\DStitoli\bfseries\fontsize{13}{16}\selectfont Generazioni}\par\smallskip
%(gen)s
\par\medskip
{\DStitoli\bfseries\fontsize{13}{16}\selectfont Scheda di pedigree, esempio}\par\smallskip
\begin{DSscheda}{DSgenC}
\begin{minipage}[t]{%(mini)smm}\vspace{0pt}%(img)s\end{minipage}\hspace{3mm}%%
\begin{minipage}[t]{\dimexpr\linewidth-%(mini)smm-3mm\relax}\vspace{0pt}
{\DStitoli\bfseries\large Mew}\hspace{2mm}\DSnumero{151}\hfill\DSstato{DSstatoinhome}{in HOME}\par
{\small Dono segreto di terza generazione, distribuito come evento; lotto \texttt{lotto-eventi/000-Mew-Mew.pk3}.}\par\smallskip
\begin{tabular}{@{}>{\DSdati\footnotesize\color{DSseppia}}l>{\DSdati\footnotesize}l>{\DSdati\footnotesize\color{DSseppia}}l>{\DSdati\footnotesize}l@{}}
gioco d'origine & Rubino & allenatore & MYSTRY, ID 06930\\
livello & 10 & sfera & Poké Ball\\
lingua & inglese & abilità & Synchronize\\
mosse & Pound, Transform & fiocchi & nessuno\\
giudizio & conforme, PKHeX 26.10.18 & copia, box & HOME1, box 1 posto 1\\
\end{tabular}
\end{minipage}
\end{DSscheda}
\end{document}
"""


def campionario(tok):
    os.makedirs(LAVORO, exist_ok=True)
    colori = " ".join(
        "\\tcbox[on line, colback=DS%s, colframe=DSfiletto, boxrule=0.4pt, arc=1mm, left=6mm, right=0mm, top=3mm, bottom=3mm]{}"
        "\\,{\\DSdati\\scriptsize %s}\\quad" % (n.replace("_", ""), n.replace("_", " ")) for n in tok["colori"])
    gen = " ".join(
        "\\tcbox[on line, colback=DSgen%s, colframe=DSgen%s, arc=1mm, left=6mm, right=0mm, top=3mm, bottom=3mm]{}"
        "\\,{\\DSdati\\scriptsize gen %s}\\quad" % ("ABCDEFG"[int(n) - 1], "ABCDEFG"[int(n) - 1], n)
        for n in tok["generazioni"])
    mini = os.path.join(RADICE, "_notes", "stampa", "miniature", "0151-.png")
    m = tok["geometria"]["miniatura_mm"]
    img = ("\\DSminiatura{%s}" % mini.replace("\\", "/")) if os.path.exists(mini) \
        else "\\tcbox[colback=DScartascura, width=%smm, height=%smm]{}" % (m, m)
    g = tok["geometria"]
    tex = CAMPIONARIO % {"mv": g["margine_verticale_mm"], "ma": g["margine_anelli_mm"], "mm": g["margine_mm"],
                         "car": CARATTERI.replace("\\", "/"), "stile": STILE_TEX.replace("\\", "/"),
                         "ver": tok["versione"], "colori": colori, "gen": gen, "mini": m, "img": img}
    p = os.path.join(LAVORO, "campionario.tex")
    scrivi_lf(p, tex)
    r = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "campionario.tex"],
                       cwd=LAVORO, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(r.stdout[-3000:])
        return 1
    print("composto   %s" % os.path.join(LAVORO, "campionario.pdf"))
    return 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("comando", choices=["caratteri", "genera", "campionario"])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    tok = leggi_token()
    if a.comando == "caratteri":
        return caratteri(tok)
    if a.comando == "genera":
        return genera(tok, a.check)
    return campionario(tok)


if __name__ == "__main__":
    sys.exit(main())
