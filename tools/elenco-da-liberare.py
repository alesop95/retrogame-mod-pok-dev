#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lega ogni esemplare con la data fuori finestra al suo sostituto e compone l'elenco stampabile di ciò che va liberato in HOME.

Perché esiste
--------------
Il 2026-11-16 il proprietario ha deciso di rigenerare i doni da carta con una data di incontro fuori dalla finestra
dell'evento (ADR-126). `tools/pkhex-ridata` ha scritto gli esemplari con la data nuova, e `tools/pkhex-scrivi-salvataggio`
li ha messi nelle copie RIDATA1 (Rubino Omega) e RIDATA2 (Ultraluna), insieme ai due Jirachi cromatici di terza
generazione, che non sostituiscono nessuno. In HOME restano intanto gli esemplari vecchi, che vanno liberati a mano,
uno per uno, e il proprietario vuole stamparne l'elenco con tutto ciò che serve a riconoscere ciascuno e con il totale
di HOME atteso a ogni passo.

Questo strumento lega ogni posto delle copie nuove al posto della copia vecchia da cui viene, attraverso il nome del
file d'origine che il rapporto della copia conserva (GRUPPO-bBOX-pPOSTO-SPECIE), e scrive:
`pokedex-home-completo/data/sostituzioni-ridata.json`, che `tools/stampa-collezione.py` usa per lo stato dei pedigree;
`pokedex-home-completo/data/esito-ridata.json`, l'esito di `tools/pkhex-ridata` per ogni esemplare del piano;
e, con `--stampa`, l'elenco per etichetta in `_notes/stampa/da-liberare/`, in Markdown e in PDF da stampare. L'elenco non
entra in Git e non si tiene: il proprietario lo stampa e lo cancella, perché si rigenera dai dati (2026-11-16).

In HOME l'etichetta «Bank N» corrisponde al box N della copia da cui l'esemplare è passato: verificato dal proprietario il
2026-11-16 sul Pumpkaboo di HOME2, box 23, che sta sotto «Bank 23». Al momento della liberazione in HOME ci sono sia il
vecchio sia il sostituto, uguali in tutto salvo la data di incontro: il vecchio si riconosce dall'etichetta e dalla data.

Uso
---
    python tools/elenco-da-liberare.py            scrive i file tracciati
    python tools/elenco-da-liberare.py --stampa   e scrive l'elenco Markdown e il PDF da stampare
    python tools/elenco-da-liberare.py --check    esce con 1 se i file tracciati non sono allineati
"""

import argparse
import collections
import importlib.util
import io
import json
import os
import re
import subprocess
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import rigenera_sicuro  # noqa: E402

RADICE = os.path.dirname(QUI)
GIUDIZIO_NUOVE = os.path.join(RADICE, "_notes", "lavoro", "giudizi-copie", "ridata-20261116b.json")
MANIFESTO = os.path.join(RADICE, "_notes", "lotti", "lotto-ridata-20261116c", "manifesto.json")
USCITA_JSON = os.path.join(RADICE, "pokedex-home-completo", "data", "sostituzioni-ridata.json")
USCITA_ESITI = os.path.join(RADICE, "pokedex-home-completo", "data", "esito-ridata.json")
USCITA_MD = os.path.join(RADICE, "_notes", "stampa", "da-liberare", "DA-LIBERARE-IN-HOME.md")
USCITA_PDF = os.path.join(RADICE, "_notes", "stampa", "da-liberare")
DS = os.path.join(RADICE, "pokedex-home-completo", "design-system")
ORIGINE = re.compile(r"/(?:pk6|pk7)/([A-Z0-9]+)-b(\d+)-p(\d+)-\d+\.pk[67]$")
AGGIUNTI = "lotto-jirachi-cromatico-"

# Il totale di HOME, letto dalla foto del proprietario del 2026-11-13, e la sequenza dei giri di ADR-126. Gli esemplari
# di Verde Foglia vengono dopo la liberazione, in un giro loro (correzione del proprietario del 2026-11-16), e qui non si contano.
HOME_OGGI = 6223
GIRO_RIDATA = {"RIDATA2": 12, "RIDATA1": 13}
# Il giro 14, DIAMANTE1 (ADR-130, ADR-131), è entrato in HOME il 2026-11-17 prima che cominciasse la liberazione:
# foto del proprietario con 7466, cioè 7221 più 245. I suoi esemplari non sono voci dell'elenco, ma spostano i totali.
GIRO14_DIAMANTE = 245

_s = importlib.util.spec_from_file_location("cdi", os.path.join(QUI, "controlla-date-incontro.py"))
cdi = importlib.util.module_from_spec(_s)
_s.loader.exec_module(cdi)

SESSO = {"M": "♂", "F": "♀"}


def livello(r):
    m = re.match(r"(\d+)", r["Livello"])
    return m.group(1) if m else r["Livello"]


def componi():
    vecchi = {(r["_gruppo"], int(r["Box"]), int(r["Posto"])): r for r in cdi.leggi_pedigree()}
    sostituzioni, aggiunti, per_copia = [], [], collections.Counter()
    for copia in json.load(open(GIUDIZIO_NUOVE, encoding="utf-8"))["copie"]:
        per_copia[copia["gruppo"]] = len(copia["esemplari"])
        for e in copia["esemplari"]:
            if AGGIUNTI in e["origine"]:
                aggiunti.append((copia["gruppo"], e))
                continue
            m = ORIGINE.search(e["origine"])
            if not m:
                raise SystemExit("origine non riconosciuta in %s: %s" % (copia["gruppo"], e["origine"]))
            chiave = (m.group(1), int(m.group(2)), int(m.group(3)))
            r = vecchi.get(chiave)
            if r is None:
                raise SystemExit("posto d'origine assente dai pedigree: %s" % (chiave,))
            sostituzioni.append({
                "gruppo_vecchio": chiave[0], "box_vecchio": chiave[1], "posto_vecchio": chiave[2],
                "impronta_vecchia": r["Impronta"], "data_vecchia": r["Data"],
                "gruppo_nuovo": copia["gruppo"], "box_nuovo": e["box"], "posto_nuovo": e["posto"],
                "impronta_nuova": e["impronta"], "data_nuova": e["data_incontro"], "gioco_nuovo": e["gioco"],
                "specie": r["Specie"], "forma": r["Forma"], "sesso": r["Sesso"], "cromatico": r["Cromatico"],
                "livello": livello(r), "sfera": r["Sfera"], "natura": r["Natura"], "abilita": r["Abilità"],
                "mosse": r["Mosse"], "oggetto": r["Oggetto"], "lingua": r["Lingua"], "allenatore": r["Allenatore"],
                "luogo": r["Luogo"], "gioco_vecchio": r["Gioco d'origine"], "evento": r["Evento"],
                "stato_vecchio": r["_stato"],
            })
    sostituzioni.sort(key=lambda s: (s["box_vecchio"], s["specie"], s["gruppo_vecchio"], s["posto_vecchio"]))
    per_etichetta = collections.defaultdict(list)
    for s in sostituzioni:
        per_etichetta[s["box_vecchio"]].append(s)

    dopo12 = HOME_OGGI + per_copia["RIDATA2"]
    dopo13 = dopo12 + per_copia["RIDATA1"]
    dopo14 = dopo13 + GIRO14_DIAMANTE
    finale = dopo14 - len(sostituzioni)
    o = ["# Esemplari da liberare in HOME dopo i giri 12 e 13", "",
         "> Documento generato da `tools/elenco-da-liberare.py --stampa`, insieme al PDF accanto. Non si modifica a mano e non si tiene: si rigenera. Il legame fra esemplare vecchio e nuovo sta in `pokedex-home-completo/data/sostituzioni-ridata.json`.", "",
         "Ogni voce è un esemplare già in HOME con la data di incontro fuori dalla finestra dell'evento (ADR-126). Il suo sostituto è uguale in tutto, specie, sesso, livello, sfera, natura, abilità, mosse, allenatore, lingua e statistiche, salvo la data di incontro, e arriva in HOME con i giri 12 (RIDATA2, Ultraluna) e 13 (RIDATA1, Rubino Omega). Si libera solo dopo che entrambi i giri sono passati: se un sostituto non arrivasse, il vecchio sarebbe ancora lì.", "",
         "Come si trova il vecchio. In HOME si apre l'etichetta «Bank N» della voce, che è il box N della copia da cui l'esemplare è passato. Si cerca la specie con quel sesso, quel livello e quell'allenatore, e si apre la scheda: la data di incontro deve essere quella da liberare. Se la data è quella da tenere, quello è il sostituto e non si tocca. Il sostituto di solito sta sotto un'altra etichetta, perché nella copia nuova ha un altro box, ma non sempre: la data decide. Si liberano a gruppi fino a 100, spuntando la casella di ogni voce.", "",
         "## Il totale di HOME", "",
         "| Momento | Totale atteso |", "|---|---|",
         "| Prima dei giri | %d |" % HOME_OGGI,
         "| Dopo il giro 12 (RIDATA2, %d esemplari, compreso il Jirachi cromatico WISHMKR) | %d |" % (per_copia["RIDATA2"], dopo12),
         "| Dopo il giro 13 (RIDATA1, %d esemplari, compreso il Jirachi cromatico CHANNEL) | %d |" % (per_copia["RIDATA1"], dopo13),
         "| Dopo il giro 14 (DIAMANTE1, %d esemplari, entrato prima della liberazione) | %d |" % (GIRO14_DIAMANTE, dopo14),
         "| Dopo la liberazione di tutte le %d voci | %d |" % (len(sostituzioni), finale), "",
         "Il totale cresce di %d rispetto a prima dei giri: sono i due Jirachi cromatici, che non sostituiscono nessuno, e i %d di Diamante." % (finale - HOME_OGGI, GIRO14_DIAMANTE), "",
         "## Riepilogo per etichetta, nell'ordine di liberazione", "",
         "| Etichetta | Voci | Totale prima | Totale dopo |", "|---|---|---|---|"]
    totale = dopo14
    for box in sorted(per_etichetta):
        n = len(per_etichetta[box])
        o.append("| Bank %d | %d | %d | %d |" % (box, n, totale, totale - n))
        totale -= n
    numero = 0
    totale = dopo14
    for box in sorted(per_etichetta):
        voci = per_etichetta[box]
        o += ["", "## Etichetta Bank %d" % box, "",
              "Voci: %d. HOME prima di questa etichetta: %d; dopo: %d." % (len(voci), totale, totale - len(voci)), ""]
        totale -= len(voci)
        for s in voci:
            numero += 1
            o.append(("- [ ] %d. %s%s%s%s, livello %s; %s, %s, %s; allenatore %s, %s; %s, %s. "
                      "Data da liberare %s; il sostituto sta sotto «Bank %d» con la data %s (%s, box %d, posto %d). Copia vecchia %s, box %d, posto %d.") % (
                numero, s["specie"], " " + s["forma"] if s["forma"] else "", " " + SESSO.get(s["sesso"], "") if s["sesso"] else "",
                " cromatico" if s["cromatico"] else "", s["livello"], s["sfera"], s["natura"], s["abilita"],
                s["allenatore"].replace("|", "/"), s["lingua"], s["luogo"], s["gioco_vecchio"],
                s["data_vecchia"], s["box_nuovo"], s["data_nuova"], s["gruppo_nuovo"], s["box_nuovo"], s["posto_nuovo"],
                s["gruppo_vecchio"], s["box_vecchio"], s["posto_vecchio"]))
    o += ["", "## Esemplari nuovi che non sostituiscono nessuno", ""]
    for gruppo, e in aggiunti:
        o.append("- %s %s cromatico, allenatore %s, ID %s, %s, giro %d: copia %s, box %d, posto %d." % (
            e["numero"], e["specie"], e["allenatore"], e["id"], e["gioco"], GIRO_RIDATA[gruppo], gruppo, e["box"], e["posto"]))
    o.append("")
    esiti = {v["impronta"]: {k: v.get(k) for k in ("esito", "campo", "data_vecchia", "data_nuova")}
             for v in json.load(open(MANIFESTO, encoding="utf-8"))["voci"]}
    return {"md": "\n".join(o), "json": json.dumps(sostituzioni, ensure_ascii=False, indent=1) + "\n",
            "esiti": json.dumps(esiti, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
            "n": len(sostituzioni), "per_etichetta": per_etichetta, "aggiunti": aggiunti,
            "totali": (HOME_OGGI, dopo12, dopo14, finale), "per_copia": per_copia}


def tex(testo):
    sost = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
            "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(sost.get(c, c) for c in str(testo))


GEN7 = {"Sole", "Luna", "Ultrasole", "Ultraluna"}


def data_home(iso):
    """La data come la mostra HOME in inglese, cioè mese/giorno/anno, che è ciò che il proprietario legge nella scheda."""
    a, m, g = iso.split("-")
    return "%s/%s/%s" % (m, g, a)


def allenatore_home(s):
    """Nome e ID dell'allenatore come li mostra HOME: ID a sei cifre per la settima generazione, a cinque per la sesta."""
    parti = [p.strip() for p in s["allenatore"].split(",")]
    nome, ident = parti[0], next((p[3:] for p in parti if p.startswith("ID ")), "")
    if ident.isdigit():
        ident = ident.zfill(6 if s["gioco_vecchio"] in GEN7 else 5)
    return nome, ident


def numero_specie(s):
    m = re.match(r"(\d+)", s["specie"])
    return int(m.group(1)) if m else 0


def pdf(c):
    """Il foglio da stampare, ridotto a ciò che serve a riconoscere il vecchio in HOME e a sapere dove sta il sostituto.

    Dal 2026-11-17, su richiesta del proprietario: nel minor numero di pagine, con le sole informazioni che distinguono
    un esemplare in HOME (etichetta, numero e specie, forma, sesso, cromatico, livello, allenatore e ID, data da liberare)
    e con l'etichetta di HOME del sostituto, che prima era data solo come copia e box e ha prodotto un equivoco. Le voci
    identiche nella stessa etichetta si uniscono con il loro numero: si liberano tutte, sono indistinguibili.
    """
    g = json.load(io.open(os.path.join(DS, "tokens.json"), encoding="utf-8"))["geometria"]
    caratteri = os.path.join(RADICE, "_notes", "design-system", "caratteri").replace("\\", "/") + "/"
    oggi, dopo12, dopo14, finale = c["totali"]
    t = [r"""\documentclass[8pt,a4paper]{extarticle}
\usepackage[top=8mm,bottom=10mm,left=%(a)smm,right=8mm]{geometry}
\def\DScaratteri{%(car)s}
\input{%(stile)s}
\usepackage[italian]{babel}
\usepackage{amssymb}
\usepackage{multicol}
\setlength{\parindent}{0pt}
\setlength{\columnsep}{5mm}
\setlength{\columnseprule}{0.3pt}
\pagestyle{plain}
\newcommand{\V}[1]{\par\hangindent=4mm\hangafter=1\noindent$\square$\,#1\par}
\begin{document}
{\DStitoli\bfseries\fontsize{15}{18}\selectfont\color{DSrosso} Da liberare in HOME}\hfill{\DSdati\small %(n)d esemplari \textbullet\ HOME con Diamante, prima di liberare: \textbf{%(d13)d} \textbullet\ a liberazione finita: \textbf{%(fin)d}}\par\smallskip
{\footnotesize\textbf{Come si libera in sicurezza.} 1) In HOME scegli l'etichetta \textbf{Bank N} del riquadro e cerca la specie. 2) Apri la scheda: allenatore, ID e livello devono essere quelli della riga, e la data di incontro (\emph{fateful encounter on\dots}) deve essere la \textbf{data da liberare}. 3) Solo allora libera. Dopo la freccia ci sono l'etichetta e la data del sostituto, identico salvo la data: una scheda con quella data è il sostituto e non si tocca. Dove è scritto \textbf{stessa data}, vecchio e sostituto differiscono solo per il gioco d'origine e decide l'etichetta: si libera quello sotto la Bank del riquadro. Le date sono scritte come le mostra HOME, mese/giorno/anno. Un \textbf{\texttimes 2} significa due esemplari identici nella stessa etichetta: si liberano entrambi. $\bigstar$ = cromatico.}\par\smallskip
\hrule\smallskip
\begin{multicols}{2}\footnotesize
""" % {"a": g["margine_anelli_mm"], "car": caratteri,
       "stile": os.path.join(DS, "collezione-stile.tex").replace("\\", "/"), "n": c["n"],
       "d13": dopo14, "fin": finale}]
    totale = dopo14
    for box in sorted(c["per_etichetta"]):
        voci = c["per_etichetta"][box]
        t.append(r"\par\smallskip{\setlength{\fboxsep}{1pt}\colorbox{DSgiallo!35}{\parbox{\linewidth}{\DStitoli\bfseries\small Bank %d\hfill{\DSdati\scriptsize %d voci \textbullet\ HOME da %d a %d}}}}\par\smallskip" % (
            box, len(voci), totale, totale - len(voci)))
        totale -= len(voci)
        gruppi = collections.OrderedDict()
        for s in sorted(voci, key=lambda s: (numero_specie(s), s["forma"], s["sesso"], s["livello"], s["allenatore"], s["data_vecchia"])):
            nome, ident = allenatore_home(s)
            chiave = (s["specie"], s["forma"], s["sesso"], s["cromatico"], s["livello"], nome, ident, s["data_vecchia"])
            gruppi.setdefault(chiave, []).append(s)
        for (specie, forma, sesso, crom, liv, nome, ident, dv), ss in gruppi.items():
            sostituti = collections.Counter((x["box_nuovo"], x["data_nuova"]) for x in ss)
            dove = "; ".join(("Bank %d %s" % (b, data_home(d))) + (r" \texttimes%d" % k if k > 1 else "")
                             for (b, d), k in sorted(sostituti.items()))
            if any(x["data_nuova"] == dv for x in ss):
                # Tre doni coreani del WCS 2014 hanno cambiato solo il gioco d'origine (ADR-126): la data non li distingue.
                dove += r" {\color{DSrosso}\bfseries stessa data}"
            t.append(r"\V{%s{\bfseries %s}%s%s%s Lv%s \textbullet\ %s %s \hfill {\bfseries %s} $\rightarrow$ {\color{DSseppia}%s}}" % (
                r"{\bfseries\texttimes%d}\ " % len(ss) if len(ss) > 1 else "",
                tex(specie), tex(" " + forma) if forma else "", " " + SESSO.get(sesso, "") if sesso else "",
                r" $\bigstar$" if crom else "", liv, tex(nome), ident, data_home(dv), dove))
    t.append(r"\end{multicols}")
    t.append(r"\end{document}")
    os.makedirs(USCITA_PDF, exist_ok=True)
    sorgente = os.path.join(USCITA_PDF, "DA-LIBERARE-IN-HOME.tex")
    with io.open(sorgente, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(t) + "\n")
    r = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", os.path.basename(sorgente)],
                       cwd=USCITA_PDF, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(r.stdout[-3000:])
        raise SystemExit("lualatex non ha compilato l'elenco da liberare")
    for est in (".aux", ".log"):
        p = os.path.splitext(sorgente)[0] + est
        if os.path.exists(p):
            os.remove(p)
    return os.path.splitext(sorgente)[0] + ".pdf"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--stampa", action="store_true",
                    help="scrive anche l'elenco Markdown e compila il PDF da stampare, che non si tengono")
    ap.add_argument("--forza", action="store_true")
    a = ap.parse_args()
    c = componi()
    # Dal 2026-11-16 l'elenco Markdown e il PDF si producono solo a richiesta: il proprietario li stampa e li cancella,
    # perché si rigenerano dai dati. Restano tracciati e controllati soltanto i due file di dati, che i pedigree usano.
    coppie = ((USCITA_JSON, c["json"]), (USCITA_ESITI, c["esiti"]))
    if a.check:
        ok = all(os.path.exists(p) and open(p, encoding="utf-8").read() == t for p, t in coppie)
        print(("elenco da liberare allineato: %d esemplari" if ok else
               "elenco da liberare non allineato: rilanciare tools/elenco-da-liberare.py (%d)") % c["n"])
        return 0 if ok else 1
    if rigenera_sicuro.scrivi(USCITA_JSON, c["json"]) + rigenera_sicuro.scrivi(USCITA_ESITI, c["esiti"]):
        return 1
    print("scritti %s e %s: %d esemplari" % (os.path.relpath(USCITA_JSON, RADICE), os.path.relpath(USCITA_ESITI, RADICE), c["n"]))
    if a.stampa:
        os.makedirs(os.path.dirname(USCITA_MD), exist_ok=True)
        with io.open(USCITA_MD, "w", encoding="utf-8", newline="\n") as f:
            f.write(c["md"])
        print("scritto %s; compilato %s" % (os.path.relpath(USCITA_MD, RADICE), pdf(c)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
