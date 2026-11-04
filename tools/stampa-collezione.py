#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone il catalogo stampabile della collezione per HOME, un PDF con una riga per esemplare e la sua immagine.

Perché esiste
-------------
Il proprietario ha chiesto, il 2026-09-30, un PDF separato e stampabile di tutta la collezione, aggiornato man mano
che il lavoro procede, e il 2026-10-01 ne ha precisato la forma: non il box della copia da cui l'esemplare parte, ma
che tipo di evento è, nel dettaglio; niente spiegazioni in apertura; una riga per esemplare, molto dettagliata, con
una piccola immagine del Pokémon in un quadratino, presa dalla raccolta delle illustrazioni di Sugimori che il
proprietario tiene in locale.

Il catalogo si compone dai dati e non si scrive a mano. `tools/pkhex-elenco-copie` legge le copie dei salvataggi,
che sono ciò che arriva in HOME, e dà per ogni esemplare l'evento come lo riconosce la libreria: titolo e numero
della carta per un dono segreto, altrimenti il nome dell'incontro. Questo strumento lo arricchisce con la
descrizione che il progetto ha già per i lotti che non portano una carta: il nome dell'evento nel file degli eventi
di terza generazione, i gruppi di `SCHEDE-EVENTI-GB.md`, la tabella di `COMPLEMENTO-RUBINO.md` e la provenienza della
checklist. Raggruppa per generazione d'origine in ordine di Pokédex e compila con LuaLaTeX, l'ambiente della tesi.
Il margine sinistro è largo per i fori di un quaderno ad anelli, e un carattere di ripiego stampa i nomi
giapponesi, coreani e cinesi.

Le miniature si generano una volta in `_notes/stampa/miniature/` con Pillow, a 96 pixel, e non entrano in Git.

Uso
---
    python tools/stampa-collezione.py _notes/stampa/collezione.json _notes/stampa/collezione.tex --pdf
    python tools/stampa-collezione.py ... --immagini "<cartella delle illustrazioni, divisa per generazione>"
"""

import argparse
import glob
import io
import json
import os
import re
import subprocess
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMMAGINI = os.path.join(os.path.expanduser("~"), "Proton Drive", "alesop95", "My files",
                        "Sugimori Pokémon Gen1-9 DLC3 Organized", "Sugimori Pokémon Gen1-9 DLC3 Organized",
                        "Pokémon By Generation")

SOSTITUZIONI = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
                "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}

GIOCHI = {"RD": "Rosso", "GN": "Verde", "BU": "Blu", "YW": "Giallo", "GD": "Oro", "SI": "Argento", "C": "Cristallo",
          "R": "Rubino", "S": "Zaffiro", "E": "Smeraldo", "FR": "Rosso Fuoco", "LG": "Verde Foglia", "CXD": "Colosseum/XD",
          "D": "Diamante", "P": "Perla", "Pt": "Platino", "HG": "HeartGold", "SS": "SoulSilver",
          "B": "Nero", "W": "Bianco", "B2": "Nero 2", "W2": "Bianco 2", "X": "X", "Y": "Y", "OR": "Rubino Omega",
          "AS": "Zaffiro Alpha", "SN": "Sole", "MN": "Luna", "US": "Ultrasole", "UM": "Ultraluna"}

# I nomi d'incontro della libreria, resi in italiano quando non c'è una descrizione migliore.
INCONTRI = [("Event Gift", "evento"), ("Egg", "uovo"), ("Static Encounter", "incontro fisso"),
            ("In-game Trade", "scambio in gioco"), ("Virtual Console Transfer", "evento di Game Boy"),
            ("Wild Encounter", "selvatico"), ("Pokéwalker Encounter", "Pokéwalker"),
            ("Dream Radar Encounter", "Dream Radar"), ("My Pokémon Ranch", "My Pokémon Ranch")]

ETICHETTE_GB = {"stadium-jp": "Pokémon Stadium giapponese", "stadium2-jp": "Pokémon Stadium 2 giapponese",
                "uovo-strano": "Uovo Strano di Cristallo", "tour-jp": "Mew delle manifestazioni giapponesi"}


def tex(testo):
    return "".join(SOSTITUZIONI.get(c, c) for c in str(testo))


def descrizioni_del_progetto():
    """Il dettaglio dell'evento che il progetto ha già, per codice della checklist e per file di lotto."""
    per_codice, per_file = {}, {}
    chk = os.path.join(RADICE, "pokedex-home-completo", "CHECKLIST-COMPLETA.md")
    for riga in io.open(chk, encoding="utf-8"):
        m = re.match(r"\| `(EVT-[^`]+)` \| \d \| ([^|]+) \| \d+ \| \d+ \| ([^|]+) \|", riga)
        # Per i doni segreti e le tabelle di incontro la provenienza della checklist è generica, cioè l'elenco dei
        # giochi o la classe: il dettaglio viene allora dalla carta o dalle schede.
        if m and m.group(2).strip() not in ("dono segreto", "tabella di incontro"):
            per_codice[m.group(1)] = m.group(3).strip()
    gruppo = None
    for riga in io.open(os.path.join(RADICE, "pokedex-home-completo", "SCHEDE-EVENTI-GB.md"), encoding="utf-8"):
        if riga.startswith("## "):
            gruppo = riga[3:].strip()
        m = re.match(r"### (EVT-\d-\d{4}) ", riga)
        if m and gruppo:
            per_codice[m.group(1)] = gruppo
    for riga in io.open(os.path.join(RADICE, "pokedex-home-completo", "COMPLEMENTO-RUBINO.md"), encoding="utf-8"):
        celle = [c.strip() for c in riga.split("|")]
        if len(celle) >= 8 and re.match(r"\d{3}-", celle[1]):
            # L'origine di un esemplare del complemento è lotto-complemento-rubino/esemplari/... nei rapporti delle
            # copie scritti dal 2026-10-07, ed esemplari/... in quelli precedenti: valgono entrambe finché le copie
            # non sono rifatte (ADR-099). La forma breve era anche di lotto-parco-lotta, che non va nelle copie.
            for prefisso in ("lotto-complemento-rubino/esemplari/", "esemplari/"):
                per_file[prefisso + celle[1] + ".pk3"] = celle[6]
    # I file che la checklist collega per tabella, come gli incontri dei biglietti.
    sorgente = io.open(os.path.join(RADICE, "tools", "checklist-pokedex.py"), encoding="utf-8").read()
    for m in re.finditer(r'"(EVT-[^"]+)": \("([^"]+)", "([^"]+)"\)', sorgente):
        lotto = m.group(2)
        if per_codice.get(m.group(1)):
            per_file.setdefault("%s/%s" % (lotto, m.group(3)), per_codice[m.group(1)])
    return per_codice, per_file


def evento_di(e, per_codice, per_file):
    origine = e["origine"]
    nome = os.path.splitext(os.path.basename(origine))[0]
    parti = nome.split("-")
    if per_file.get(origine):
        return per_file[origine]
    if "carta" in e["evento"]:
        return e["evento"]
    if len(parti) >= 3 and parti[0] == "EVT" and per_codice.get("-".join(parti[:3])):
        return per_codice["-".join(parti[:3])]
    if origine.startswith("lotto-eventi/") and len(parti) >= 3:
        return "evento di terza generazione: " + re.sub(r"(?<=[a-z])(?=[A-Z0-9])", " ", parti[1])
    for chiave, etichetta in ETICHETTE_GB.items():
        if nome.startswith("GB-" + chiave + "-"):
            return etichetta
    for inglese, italiano in INCONTRI:
        if e["evento"].startswith(inglese):
            resto = e["evento"][len(inglese):].strip(" ()")
            return italiano + (" (%s)" % resto if resto else "")
    return e["evento"]


def miniatura(e, cartella, cache):
    """La miniatura della specie e della forma, generata una volta; None se l'illustrazione non c'è."""
    chiave = "%04d-%s" % (e["numero"], e.get("forma_en") or "")
    if chiave in cache:
        return cache[chiave]
    candidati = glob.glob(os.path.join(cartella, "*", "%04d *.png" % e["numero"]))
    scelto = None
    forma = (e.get("forma_en") or "").lower()
    if forma:
        scelto = next((c for c in candidati if forma in os.path.basename(c).lower()), None)
    if scelto is None:
        base = [c for c in candidati if re.fullmatch(r"\d{4} [^ ]+\.png", os.path.basename(c))]
        scelto = (base or sorted(candidati, key=len) or [None])[0]
    if scelto is None:
        cache[chiave] = None
        return None
    from PIL import Image
    uscita = os.path.join(RADICE, "_notes", "stampa", "miniature", re.sub(r"[^A-Za-z0-9-]", "_", chiave) + ".png")
    if not os.path.exists(uscita):
        os.makedirs(os.path.dirname(uscita), exist_ok=True)
        img = Image.open(scelto).convert("RGBA")
        img.thumbnail((96, 96))
        fondo = Image.new("RGBA", (96, 96), (255, 255, 255, 255))
        fondo.paste(img, ((96 - img.width) // 2, (96 - img.height) // 2), img)
        fondo.convert("RGB").save(uscita)
    cache[chiave] = uscita.replace("\\", "/")
    return cache[chiave]


def componi(dati, cartella_immagini):
    per_codice, per_file = descrizioni_del_progetto()
    cache = {}
    righe = [r"""\documentclass[8pt,a4paper]{extarticle}
\usepackage[top=12mm,bottom=12mm,left=26mm,right=10mm]{geometry}
\usepackage{fontspec}
\directlua{luaotfload.add_fallback("asia", {"YuGothic:mode=harf;", "MS Gothic:mode=harf;", "Malgun Gothic:mode=harf;", "Microsoft YaHei:mode=harf;", "Microsoft JhengHei:mode=harf;"})}
\setmainfont{Arial}[RawFeature={fallback=asia}]
\usepackage{longtable,booktabs,array,graphicx}
\usepackage[italian]{babel}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\setlength{\tabcolsep}{2.5pt}
\renewcommand{\arraystretch}{1.1}
\pagestyle{plain}
\begin{document}
\section*{La collezione per HOME}
"""]
    gruppi = {}
    for c in dati["copie"]:
        nome = "Per HOME" if c["gruppo"].startswith("per HOME") else "Decisione finale: " + c["gruppo"].split(", ", 1)[1]
        gruppi.setdefault(nome, []).extend(c["esemplari"])
    for nome_gruppo, esemplari in gruppi.items():
        righe.append(r"\subsection*{%s, %d esemplari}" % (tex(nome_gruppo), len(esemplari)))
        per_gen = {}
        for e in esemplari:
            per_gen.setdefault(e["generazione"], []).append(e)
        for gen in sorted(per_gen):
            righe += [r"\subsubsection*{Generazione d'origine %d, %d esemplari}" % (gen, len(per_gen[gen])),
                      r"\begin{longtable}{c L{23mm} r l L{23mm} L{19mm} L{54mm} L{25mm}}", r"\toprule",
                      r" & Specie & Liv. & & Allenatore & Lingua, gioco & Evento & Luogo, sfera\\", r"\midrule",
                      r"\endhead"]
            for e in sorted(per_gen[gen], key=lambda x: (x["numero"], x["forma"], x["origine"])):
                img = miniatura(e, cartella_immagini, cache)
                cella_img = (r"\raisebox{-0.4\height}{\includegraphics[width=7mm,height=7mm,keepaspectratio]{%s}}" % img
                             if img else "")
                specie = e["specie"] + (" (%s)" % e["forma"] if e["forma"] else "")
                segni = e["sesso"] + (" C" if e["cromatico"] else "")
                righe.append(r"%s & %s & %d & %s & %s %s & %s, %s & %s & %s; %s\\" % (
                    cella_img, tex(specie), e["livello"], tex(segni), tex(e["allenatore"]), tex(e["id"]),
                    tex(e["lingua"][:3]), tex(GIOCHI.get(e["gioco"], e["gioco"])),
                    tex(evento_di(e, per_codice, per_file)), tex(e["luogo"]), tex(e["sfera"])))
            righe += [r"\bottomrule", r"\end{longtable}"]
        righe.append(r"\clearpage")
    righe.append(r"\end{document}")
    mancanti = sorted(k for k, v in cache.items() if v is None)
    return "\n".join(righe) + "\n", len(cache), mancanti


# Il pedigree di ogni esemplare (ADR-111, 2026-11-04): una scheda per esemplare nel PDF stampabile, con il design
# system di `pokedex-home-completo/design-system/`, e una riga per esemplare nel documento generato e tracciato, dalla
# stessa funzione, così che i due non divergano. Lo stato viene dal gruppo: il giro 1 è in HOME dal 2026-11-03.
STATO_GRUPPO = {"HOME1": ("DSstatoinhome", "in HOME")}
DS = os.path.join(RADICE, "pokedex-home-completo", "design-system")
PEDIGREE_MD = os.path.join(RADICE, "pokedex-home-completo", "pedigree")
PEDIGREE_PDF = os.path.join(RADICE, "_notes", "stampa", "pedigree")


def campi_pedigree(e, per_codice, per_file):
    """I campi del pedigree di un esemplare, come coppie etichetta e valore, nell'ordine di ADR-111."""
    iv = "/".join(str(v) for v in e["iv"])
    fiocchi = len(e["fiocchi"])
    return [
        ("gioco d'origine", GIOCHI.get(e["gioco"], e["gioco"])), ("luogo", e["luogo"]),
        ("data", e["data_incontro"] or "non registrata"),
        ("livello", "%d, incontrato al %d" % (e["livello"], e["livello_incontro"])), ("sfera", e["sfera"]),
        ("lingua", e["lingua"]),
        ("allenatore", "%s, ID %s, SID %s" % (e["allenatore"], e["id"], e["sid"])), ("natura", e["natura"]),
        ("abilità", e["abilita"]),
        ("mosse", ", ".join(e["mosse"]) or "nessuna"), ("oggetto", e["oggetto"] or "nessuno"),
        ("fiocchi", ("%d" % fiocchi) if fiocchi else "nessuno"),
        ("IV", iv), ("PID", e["pid"]), ("EC", e["ec"]),
    ]


def scheda_tex(e, gruppo, per_codice, per_file, img):
    gen = "DSgen" + "ABCDEFG"[max(1, min(7, e["generazione"])) - 1]
    colore, stato = STATO_GRUPPO.get(gruppo, ("DSstatoincopia", "in copia"))
    nome = tex(e["specie"]) + (" \\textnormal{\\small %s}" % tex(e["forma"]) if e["forma"] else "")
    segni = {"M": "♂", "F": "♀"}.get(e["sesso"], "") + (" ★" if e["cromatico"] else "")
    campi = campi_pedigree(e, per_codice, per_file)
    celle = []
    for i in range(0, len(campi), 3):
        celle.append(" & ".join("\\DScampo{%s} & %s" % (tex(k), tex(v)) for k, v in campi[i:i + 3]) + r"\\")
    mini = r"\DSminiatura[14mm]{%s}" % img if img else r"\tcbox[colback=DScartascura, colframe=DSfiletto, boxrule=0.4pt, arc=1.6mm, width=14mm, height=14mm]{}"
    giudizio = "conforme" if e["conforme"] else "NON conforme"
    return "\n".join([
        r"\begin{DSscheda}{%s}" % gen,
        r"\begin{minipage}[t]{16mm}\vspace{0pt}%s\end{minipage}\hspace{2mm}%%" % mini,
        r"\begin{minipage}[t]{\dimexpr\linewidth-18mm\relax}\vspace{0pt}",
        r"{\DStitoli\bfseries %s}\hspace{1.5mm}\DSnumero{%03d}\hspace{1.5mm}{\DSdati %s}\hfill\DSstato{%s}{%s}\par" % (
            nome, e["numero"], segni, colore, stato),
        r"{\footnotesize %s}\par\vspace{0.6mm}" % tex(evento_di(e, per_codice, per_file)),
        r"{\DSdati\scriptsize\setlength{\tabcolsep}{2pt}\begin{tabular}{@{}l L{29mm} l L{30mm} l L{34mm}@{}}",
        *celle,
        r"\end{tabular}}\par",
        r"{\DSdati\tiny\color{DSseppia} %s, PKHeX %s; %s box %d posto %d; impronta {\ttfamily %s}}" % (
            giudizio, tex(e["libreria"]), tex(gruppo), e["box"], e["posto"], e["impronta"]),
        r"\end{minipage}",
        r"\end{DSscheda}",
    ])


def pedigree(dati, cartella_immagini, pdf, solo=None):
    per_codice, per_file = descrizioni_del_progetto()
    cache = {}
    g = json.load(io.open(os.path.join(DS, "tokens.json"), encoding="utf-8"))["geometria"]
    caratteri = os.path.join(RADICE, "_notes", "design-system", "caratteri").replace("\\", "/") + "/"
    os.makedirs(PEDIGREE_MD, exist_ok=True)
    os.makedirs(PEDIGREE_PDF, exist_ok=True)
    for c in dati["copie"]:
        gruppo, esemplari = c["gruppo"], c["esemplari"]
        if solo and gruppo not in solo:
            continue
        colore, stato = STATO_GRUPPO.get(gruppo, ("", "in copia"))
        md = ["# Pedigree degli esemplari del gruppo %s" % gruppo, "",
              "> Documento generato da `tools/stampa-collezione.py --pedigree`, dalla stessa funzione che compone il PDF "
              "stampabile in `_notes/stampa/pedigree/%s.pdf`. Non si modifica a mano. Una riga per esemplare, nell'ordine di "
              "box e posto della copia, giudicata da `tools/pkhex-elenco-copie`; i campi sono quelli di ADR-111. Stato del "
              "gruppo: %s. Esemplari: %d, conformi: %d." % (gruppo, stato, len(esemplari),
                                                            sum(e["conforme"] for e in esemplari)), "",
              "| Box | Posto | Specie | Forma | Sesso | Cromatico | Evento | " +
              " | ".join(k[0].upper() + k[1:] for k, _ in campi_pedigree(esemplari[0], per_codice, per_file)) +
              " | Giudizio | Impronta |",
              "|" + "---|" * (9 + len(campi_pedigree(esemplari[0], per_codice, per_file)))]
        corpo = [r"""\documentclass[9pt,a4paper]{extarticle}
\usepackage[top=%(v)smm,bottom=%(v)smm,left=%(a)smm,right=%(m)smm]{geometry}
\def\DScaratteri{%(car)s}
\input{%(stile)s}
\usepackage[italian]{babel}
\usepackage{array}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\setlength{\parindent}{0pt}
\pagestyle{plain}
\begin{document}
{\DStitoli\bfseries\fontsize{20}{24}\selectfont\color{DSrosso} Pedigree, gruppo %(gr)s}\par
{\DSdati\small\color{DSseppia} %(n)d esemplari, %(stato)s. Generato da tools/design-system.py e tools/stampa-collezione.py.}\par\medskip
""" % {"v": g["margine_verticale_mm"], "a": g["margine_anelli_mm"], "m": g["margine_mm"], "car": caratteri,
       "stile": os.path.join(DS, "collezione-stile.tex").replace("\\", "/"), "gr": tex(gruppo), "n": len(esemplari),
       "stato": tex(stato)}]
        for e in esemplari:
            img = miniatura(e, cartella_immagini, cache)
            corpo.append(scheda_tex(e, gruppo, per_codice, per_file, img))
            valori = [v for _, v in campi_pedigree(e, per_codice, per_file)]
            md.append("| " + " | ".join(str(x).replace("|", "/") for x in [
                e["box"], e["posto"], "%d %s" % (e["numero"], e["specie"]), e["forma"], e["sesso"],
                "sì" if e["cromatico"] else "", evento_di(e, per_codice, per_file)] + valori +
                ["conforme" if e["conforme"] else "NON conforme", e["impronta"]]) + " |")
        corpo.append(r"\end{document}")
        with io.open(os.path.join(PEDIGREE_MD, gruppo + ".md"), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(md) + "\n")
        uscita = os.path.join(PEDIGREE_PDF, gruppo + ".tex")
        with io.open(uscita, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(corpo) + "\n")
        if pdf:
            r = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", os.path.basename(uscita)],
                               cwd=PEDIGREE_PDF, capture_output=True, text=True, encoding="utf-8", errors="replace")
            if r.returncode != 0:
                print(r.stdout[-3000:])
                sys.exit("lualatex non ha compilato il pedigree di " + gruppo)
        print("%s: %d esemplari; %s%s" % (gruppo, len(esemplari), os.path.relpath(os.path.join(PEDIGREE_MD, gruppo + ".md"), RADICE),
                                          ", " + os.path.splitext(uscita)[0] + ".pdf" if pdf else ""))
    mancanti = sorted(k for k, v in cache.items() if v is None)
    print("miniature %d, senza illustrazione %d %s" % (len(cache), len(mancanti), mancanti[:10]))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dati", help="JSON di tools/pkhex-elenco-copie")
    ap.add_argument("uscita", nargs="?", help="file .tex da scrivere, per il catalogo")
    ap.add_argument("--immagini", default=IMMAGINI, help="cartella delle illustrazioni, divisa per generazione")
    ap.add_argument("--pdf", action="store_true", help="compila anche il PDF con lualatex, due passate")
    ap.add_argument("--pedigree", action="store_true",
                    help="compone il pedigree per gruppo: PDF in _notes/stampa/pedigree/, Markdown in pokedex-home-completo/pedigree/")
    ap.add_argument("--gruppo", action="append", help="con --pedigree, solo questo gruppo; si ripete")
    a = ap.parse_args()
    if a.pedigree:
        pedigree(json.load(io.open(a.dati, encoding="utf-8")), a.immagini, a.pdf, a.gruppo)
        return
    if not a.uscita:
        ap.error("serve il file .tex da scrivere, oppure --pedigree")
    dati = json.load(io.open(a.dati, encoding="utf-8"))
    testo, figure, mancanti = componi(dati, a.immagini)
    io.open(a.uscita, "w", encoding="utf-8").write(testo)
    print("scritto %s; miniature %d, senza illustrazione %d %s" % (a.uscita, figure, len(mancanti), mancanti[:10]))
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
