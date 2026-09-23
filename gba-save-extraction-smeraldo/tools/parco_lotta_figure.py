#!/usr/bin/env python3
"""Disegna le figure della guida al Parco Lotta: la mappa dei box 13 e 14, il calendario degli Assi, e una mappa per squadra con i tre esemplari da prelevare.

Perche' esiste
--------------

Chi prepara una sfida ha davanti il PC del gioco, cioe' una griglia di sei colonne per cinque righe, e una griglia si legge prima come figura che come tabella: una casella evidenziata con il numero dell'ordine di squadra dice dove cliccare piu' in fretta di "box 14, riga 2, colonna 1". Dal 2026-09-23, per ADR-078, il lotto e' in copia unica e chiude il deposito: il box 14 e' tutto del lotto, e del box 13 lo sono soltanto le ultime due posizioni, che la figura mostra mentre lascia vuote le altre, dove stanno esemplari che non sono del lotto. Le figure si generano dalla stessa funzione `disposizione` che ha scritto la cartuccia, quindi non possono divergere da cio' che c'e' nei box.

I colori seguono la tavolozza di riferimento della skill di visualizzazione: blu per i titolari, grigio neutro per le riserve, e il giallo di stato per l'avvertimento sul livello 51, che non compare mai da solo ma sempre con la scritta, perche' il giallo su fondo chiaro non ha contrasto sufficiente per reggersi senza testo.

Uso
---

    python gba-save-extraction-smeraldo/tools/parco_lotta_figure.py

Scrive i PNG sotto `gba-save-extraction-smeraldo/figure/`, dove la guida li richiama.
"""

import importlib.util
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

CARTELLA = Path(__file__).resolve().parents[1]
FIGURE = CARTELLA.joinpath("figure")

SUPERFICIE = "#fcfcfb"
INCHIOSTRO = "#0b0b0b"
SECONDARIO = "#52514e"
MUTO = "#898781"
TITOLARE = "#cde2fb"
TITOLARE_BORDO = "#2a78d6"
RISERVA = "#f0efec"
VUOTO = "#ffffff"
ATTENZIONE = "#fab219"
METADATI = {"Software": None}


def _percorso():
    percorso = Path(__file__).resolve().parent.joinpath("parco_lotta_percorso_oro.py")
    spec = importlib.util.spec_from_file_location("percorso_oro", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def griglia(ax, box, contenuto, titolo, evidenzia=None):
    """Disegna un box: contenuto e' {posizione: (testo, stile)}, evidenzia e' {posizione: numero d'ordine}."""
    evidenzia = evidenzia or {}
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5)
    ax.invert_yaxis()
    ax.axis("off")
    ax.set_title(titolo, fontsize=11, color=INCHIOSTRO, loc="left", pad=6)
    for n in range(1, 31):
        r, c = (n - 1) // 6, (n - 1) % 6
        testo, stile = contenuto.get(n, ("", "vuoto"))
        fondo = {"titolare": TITOLARE, "riserva": RISERVA, "vuoto": VUOTO}[stile]
        # Nelle figure di squadra le caselle da non prelevare si attenuano, cosi' che le tre giuste
        # si trovino a colpo d'occhio invece che per lettura.
        attenua = bool(evidenzia) and n not in evidenzia
        bordo = TITOLARE_BORDO if n in evidenzia else ("#d8d7d2" if stile != "vuoto" else "#e8e7e3")
        spessore = 2.2 if n in evidenzia else 0.8
        ax.add_patch(FancyBboxPatch((c + 0.06, r + 0.06), 0.88, 0.88, boxstyle="round,pad=0,rounding_size=0.08",
                                    facecolor=fondo, edgecolor=bordo, linewidth=spessore,
                                    alpha=0.35 if attenua else 1.0))
        righe = testo.split("\n")
        ax.text(c + 0.5, r + 0.42, righe[0], ha="center", va="center", fontsize=6.6,
                color=MUTO if attenua else INCHIOSTRO)
        if len(righe) > 1:
            ax.text(c + 0.5, r + 0.66, righe[1], ha="center", va="center", fontsize=5.6,
                    color=MUTO if attenua else SECONDARIO)
        if len(righe) > 2:
            ax.add_patch(FancyBboxPatch((c + 0.14, r + 0.12), 0.72, 0.16, boxstyle="round,pad=0,rounding_size=0.04",
                                        facecolor=ATTENZIONE, edgecolor="none"))
            ax.text(c + 0.5, r + 0.20, righe[2], ha="center", va="center", fontsize=5.0, color=INCHIOSTRO)
        if n in evidenzia:
            ax.add_patch(plt.Circle((c + 0.2, r + 0.84), 0.11, color=TITOLARE_BORDO))
            ax.text(c + 0.2, r + 0.84, str(evidenzia[n]), ha="center", va="center", fontsize=7, color="#ffffff",
                    fontweight="bold")


def main():
    percorso = _percorso()
    catalogo = json.loads(percorso.CATALOGO.read_text(encoding="utf-8"))
    thread = json.loads(percorso._mappa().THREAD.read_text(encoding="utf-8"))
    ordine, posizioni, generati, titolari = percorso.disposizione(catalogo, thread)
    nat_it = percorso.nature_italiane()
    dump = percorso.righe_dump()
    dati = json.loads(CARTELLA.joinpath("dati-gen3.json").read_text(encoding="utf-8"))
    FIGURE.mkdir(exist_ok=True)

    per_box = {13: {}, 14: {}}
    for (chiave, copia), (box, n) in posizioni.items():
        e = generati[chiave]
        riga = dump.get(chiave) or {}
        soglia = dati["esperienza"][dati["specie"][e["specie"]]["gruppo_crescita"]][catalogo["livello"] + 1]
        margine_uno = riga and soglia - int(riga.get("EXP", 0)) == 1
        testo = "%s\n%s" % (e["specie"], nat_it.get(e["natura"], e["natura"]))
        if margine_uno:
            testo += "\na 1 PE dal 51"
        per_box[box][n] = (testo, "titolare" if chiave in titolari else "riserva")

    scritte = []
    fig, assi = plt.subplots(1, 2, figsize=(10.4, 4.6), facecolor=SUPERFICIE)
    for ax, box in zip(assi, (13, 14)):
        griglia(ax, box, per_box[box], "Box %d" % box + (": del lotto solo le ultime due posizioni" if box == 13 else ""))
    fig.text(0.01, 0.01, "Blu: titolari delle squadre. Grigio: riserve. Una copia per esemplare. "
             "Etichetta gialla: esperienza a un punto dal livello 51, mai usare fuori dal Parco.",
             fontsize=8.5, color=SECONDARIO)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    uscita = FIGURE.joinpath("box-13-14.png")
    fig.savefig(uscita, dpi=160, facecolor=SUPERFICIE, metadata=METADATI)
    plt.close(fig)
    scritte.append(uscita)

    for squadra in catalogo["squadre"]:
        if not squadra["esemplari"]:
            continue
        evidenzia = {}
        for i, v in enumerate(squadra["esemplari"], start=1):
            box, n = posizioni[(v["chiave"], 1)]
            evidenzia[n] = i
        fig, ax = plt.subplots(figsize=(5.4, 4.3), facecolor=SUPERFICIE)
        # i titolari sono i primi otto dell'ordine, quindi stanno tutti nel box 14
        assert all(posizioni[(v["chiave"], 1)][0] == 14 for v in squadra["esemplari"])
        griglia(ax, 14, per_box[14], "%s: i tre da prelevare dal box 14, nell'ordine" % squadra["edificio"], evidenzia)
        fig.tight_layout()
        uscita = FIGURE.joinpath("squadra-%s.png" % squadra["edificio"].split()[0].lower())
        fig.savefig(uscita, dpi=160, facecolor=SUPERFICIE, metadata=METADATI)
        plt.close(fig)
        scritte.append(uscita)

    # Il calendario: una barra per edificio, lunga quanto le serie di fila che servono all'oro, con il
    # punto dell'argento segnato. Una sola serie di dati, quindi nessuna legenda: le etichette dirette
    # dicono tutto, e il colore e' uno solo.
    righe = []
    for squadra in sorted(catalogo["squadre"], key=lambda s: -int(s["ordine"])):
        ed = squadra["edificio"]
        unita, argento, oro, per_serie, asso, simbolo, scarto = percorso.CALENDARIO[ed]
        if ed == "Cupola Lotta":
            tot, arg = 10, 5
        else:
            tot = -(-(oro if scarto == 1 else oro + 1) // per_serie)
            arg = -(-(argento if scarto == 1 else argento + 1) // per_serie)
        righe.append(("%s. %s" % (squadra["ordine"], ed), tot, arg, "tornei" if ed == "Cupola Lotta" else "serie"))
    fig, ax = plt.subplots(figsize=(8.5, 3.6), facecolor=SUPERFICIE)
    ax.set_facecolor(SUPERFICIE)
    for y, (nome, tot, arg, unita) in enumerate(righe):
        ax.barh(y, tot, height=0.5, color=TITOLARE_BORDO)
        ax.plot([arg, arg], [y - 0.32, y + 0.32], color=INCHIOSTRO, linewidth=2)
        ax.text(arg, y - 0.36, "argento", ha="center", va="top", fontsize=7, color=SECONDARIO)
        ax.text(tot + 0.15, y, "oro: %d %s di fila" % (tot, unita), va="center", fontsize=8, color=INCHIOSTRO)
    ax.set_yticks(range(len(righe)))
    ax.set_yticklabels([r[0] for r in righe], fontsize=9, color=INCHIOSTRO)
    ax.set_xlim(0, 14.5)
    ax.set_xlabel("serie (alla Cupola, tornei) vinte senza perdere", fontsize=8, color=MUTO)
    for lato in ("top", "right", "left"):
        ax.spines[lato].set_visible(False)
    ax.spines["bottom"].set_color("#d8d7d2")
    ax.tick_params(axis="x", colors=MUTO, labelsize=8)
    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    uscita = FIGURE.joinpath("calendario.png")
    fig.savefig(uscita, dpi=160, facecolor=SUPERFICIE, metadata=METADATI)
    plt.close(fig)
    scritte.append(uscita)
    for s in scritte:
        print("scritta %s" % s)


if __name__ == "__main__":
    main()
