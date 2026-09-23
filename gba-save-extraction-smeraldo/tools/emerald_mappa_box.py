#!/usr/bin/env python3
"""Genera la mappa stampabile dei quattordici box di Smeraldo: che cosa c'e' in ogni posizione, con l'illustrazione di Sugimori, e da dove viene.

Perche' esiste
--------------

Dopo ADR-076, ADR-077 e ADR-078 il deposito e' pieno, 420 su 420, e mescola sei provenienze: la collezione di catture vere, gli eventi in tutte le lingue, gli incontri da biglietto, gli scambi in gioco, i due giganti e il lotto del Parco Lotta. Chi apre il PC del gioco vede soltanto trenta icone per box e non sa quale di tre Latios sia l'evento e quale la cattura. Questo strumento risponde posizione per posizione, e lo fa leggendo i byte del salvataggio invece di fidarsi della regola che li ha disposti: la provenienza di ogni posizione si riconosce confrontando il record con i file dei lotti, e i dati leggibili vengono dal dump di PKHeX.

Il dump puo' appartenere a un altro file, purche' contenga gli stessi record: il file di `giro11` e' una permutazione di quello di `giro10`, verificata record per record, quindi il dump `round 4` di `giro10` vale per entrambi, e lo strumento lo accoppia per contenuto e non per posizione. Se un record del salvataggio non si trova nel file del dump, lo strumento si ferma.

Le illustrazioni vengono dalla raccolta locale del proprietario e restano fuori da git con le figure, per ADR-005; il documento Markdown generato si versiona.

Uso
---

    python gba-save-extraction-smeraldo/tools/emerald_mappa_box.py SALVATAGGIO.sav --dump DUMP.csv --file-del-dump FILE_DEL_DUMP.sav

Scrive `gba-save-extraction-smeraldo/MAPPA-BOX-SMERALDO.md`, le figure `figure/mappa-box-NN.png` e la copia `MAPPA-BOX-SMERALDO.docx`.
"""

import argparse
import collections
import csv
import importlib.util
import re
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402
from PIL import Image  # noqa: E402

# Gli allenatori degli eventi giapponesi hanno il nome in kana, che DejaVu non ha: il font di sistema
# giapponese di Windows fa da riserva, e matplotlib lo usa soltanto per i glifi mancanti.
plt.rcParams["font.family"] = ["DejaVu Sans", "Yu Gothic", "MS Gothic"]

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
sys.path.insert(0, str(RADICE.joinpath("pokemon-gen12-gen3-bridge-original-hardware")))

from pokebridge import save3  # noqa: E402

NOTE = RADICE.joinpath("_notes")
FIGURE = CARTELLA.joinpath("figure")
USCITA = CARTELLA.joinpath("MAPPA-BOX-SMERALDO.md")
SUGIMORI = Path.home().joinpath("Proton Drive", "alesop95", "My files", "Sugimori Pokémon Gen1-9 DLC3 Organized",
                                "Sugimori Pokémon Gen1-9 DLC3 Organized", "Pokémon By Generation")
PER_BOX = 30
COLONNE = 6
VUOTO = bytes(save3.RECORD)

# Sei provenienze, sei slot categoriali nell'ordine fisso della tavolozza di riferimento, validati
# con lo script della skill di visualizzazione: il contrasto di acqua, giallo e magenta sul fondo e'
# sotto 3:1, quindi il colore non e' mai solo e ogni casella porta la provenienza scritta.
PROVENIENZE = [
    ("collezione", "Collezione", "#2a78d6"),
    ("evento", "Evento", "#eb6834"),
    ("biglietto", "Biglietto", "#1baf7a"),
    ("scambio", "Scambio in gioco", "#eda100"),
    ("gigante", "Gigante", "#e87ba4"),
    ("lotto", "Parco Lotta", "#008300"),
]
COLORE = {k: c for k, _, c in PROVENIENZE}
ETICHETTA = {k: e for k, e, _ in PROVENIENZE}
SUPERFICIE = "#fcfcfb"
INCHIOSTRO = "#0b0b0b"
SECONDARIO = "#52514e"
BORDO = "#d8d7d2"
FORME_DEOXYS = {"1": "Attack", "2": "Defense", "3": "Speed"}


def _modulo(percorso, nome):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def origini():
    """Ogni record dei lotti, nella forma che il salvataggio contiene, con provenienza e dettaglio."""
    noti = {}
    for f in sorted(NOTE.joinpath("lotto-eventi").glob("*.pk3")):
        cifrato = NOTE.joinpath("lotto-eventi", "forma-cifrata", f.stem + ".ek3").read_bytes()
        parti = f.stem.split("-")
        noti[cifrato] = ("evento", "-".join(parti[1:-1]) or parti[-1])
    for tipo, cartella in (("biglietto", "lotto-incontri-gen3"), ("scambio", "lotto-scambi-gen3")):
        for f in sorted(NOTE.joinpath(cartella).glob("*.pk3")):
            noti[NOTE.joinpath(cartella, "forma-cifrata", f.stem + ".ek3").read_bytes()] = (tipo, f.stem)
    for f in sorted(NOTE.joinpath("lotto-giganti").glob("*-gigante.bin")):
        noti[f.read_bytes()] = ("gigante", "taglia massima, 86,2 cm")
    percorso = _modulo(CARTELLA.joinpath("tools", "parco_lotta_percorso_oro.py"), "percorso_oro")
    catalogo = percorso.json.loads(percorso.CATALOGO.read_text(encoding="utf-8"))
    thread = percorso.json.loads(percorso._mappa().THREAD.read_text(encoding="utf-8"))
    _, _, _, titolari = percorso.disposizione(catalogo, thread)
    for f in sorted(NOTE.joinpath("lotto-parco-lotta", "esemplari").glob("*-copia1.bin")):
        chiave = f.stem[:-len("-copia1")]
        noti[f.read_bytes()] = ("lotto", "titolare" if chiave in titolari else "riserva")
    return noti


def righe_dump(dump, file_del_dump):
    """Le righe del dump per contenuto del record: {record: [riga, ...]}, dalle posizioni del file a cui il dump appartiene."""
    salvataggio = save3.Save3(Path(file_del_dump).read_bytes())
    per_posizione = {}
    with open(dump, encoding="utf-8-sig") as f:
        for riga in csv.DictReader(f):
            m = re.search(r"@ \[(\d+)\] \([^)]*\)-(\d+)", riga["Position"])
            if m:
                per_posizione[(int(m.group(1)) - 1) * PER_BOX + int(m.group(2)) - 1] = riga
    per_record = collections.defaultdict(list)
    for i in range(save3.POSIZIONI):
        r = salvataggio.leggi_posizione(i)
        if r != VUOTO:
            if i not in per_posizione:
                sys.exit("il dump non ha la posizione %d del suo file" % i)
            per_record[r].append(per_posizione[i])
    return per_record


def illustrazioni():
    """Il file di Sugimori per numero nazionale, dalle prime tre generazioni."""
    indice = {}
    for n in (1, 2, 3):
        for f in SUGIMORI.joinpath("Generation %d Pokémon" % n).glob("*.png"):
            m = re.match(r"(\d{4}) ", f.name)
            if m:
                indice[int(m.group(1))] = f
    forme = SUGIMORI.joinpath("Generation 3 Pokémon", "Pokémon Specific Forms Gen 3")
    return indice, forme


def miniatura(percorso, cache):
    if percorso not in cache:
        im = Image.open(percorso).convert("RGBA")
        im.thumbnail((220, 220))
        cache[percorso] = im
    return cache[percorso]


def figura(box, voci, indice, forme, cache, uscita):
    fig, ax = plt.subplots(figsize=(11.2, 8.0), facecolor=SUPERFICIE)
    ax.set_xlim(0, COLONNE)
    ax.set_ylim(0, 5.35)
    ax.invert_yaxis()
    ax.axis("off")
    ax.text(0.02, 0.18, "Box %d" % box, fontsize=15, color=INCHIOSTRO, fontweight="bold", va="center")
    presenti = [k for k, _, _ in PROVENIENZE if any(v and v["provenienza"] == k for v in voci)]
    x = 1.2
    for k in presenti:
        ax.add_patch(FancyBboxPatch((x, 0.1), 0.16, 0.16, boxstyle="round,pad=0,rounding_size=0.03",
                                    facecolor=COLORE[k], edgecolor="none"))
        ax.text(x + 0.22, 0.18, ETICHETTA[k], fontsize=9, color=SECONDARIO, va="center")
        x += 0.35 + 0.075 * len(ETICHETTA[k])
    for n, v in enumerate(voci, start=1):
        r, c = (n - 1) // COLONNE, (n - 1) % COLONNE
        y0 = r + 0.35
        ax.add_patch(FancyBboxPatch((c + 0.04, y0 + 0.04), 0.92, 0.92, boxstyle="round,pad=0,rounding_size=0.06",
                                    facecolor="#ffffff", edgecolor=BORDO, linewidth=0.8))
        ax.text(c + 0.1, y0 + 0.13, str(n), fontsize=7, color=SECONDARIO, va="center")
        if not v:
            continue
        ax.add_patch(FancyBboxPatch((c + 0.04, y0 + 0.83), 0.92, 0.13, boxstyle="round,pad=0,rounding_size=0.04",
                                    facecolor=COLORE[v["provenienza"]], edgecolor="none"))
        ax.text(c + 0.5, y0 + 0.895, v["banda"], fontsize=6.0, color="#ffffff" if v["provenienza"] in ("collezione", "evento", "lotto") else INCHIOSTRO,
                ha="center", va="center", fontweight="bold")
        percorso = indice.get(v["nazionale"])
        if v["nazionale"] == 386 and v["forma"] in FORME_DEOXYS:
            alternativa = forme.joinpath("0386 Deoxys %s.png" % FORME_DEOXYS[v["forma"]])
            percorso = alternativa if alternativa.exists() else percorso
        if percorso:
            im = miniatura(percorso, cache)
            lato = 0.46
            ax.imshow(im, extent=(c + 0.5 - lato / 2, c + 0.5 + lato / 2, y0 + 0.08 + lato, y0 + 0.08), zorder=3)
        ax.text(c + 0.5, y0 + 0.64, v["specie"], fontsize=7.6, color=INCHIOSTRO, ha="center", va="center")
        ax.text(c + 0.5, y0 + 0.75, "Liv. %s  %s" % (v["livello"], v["allenatore"]), fontsize=6.2, color=SECONDARIO,
                ha="center", va="center")
    fig.tight_layout(pad=0.4)
    fig.savefig(uscita, dpi=150, facecolor=SUPERFICIE, metadata={"Software": None})
    plt.close(fig)


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("salvataggio")
    p.add_argument("--dump", required=True)
    p.add_argument("--file-del-dump", required=True)
    args = p.parse_args()
    grezzo = Path(args.salvataggio).read_bytes()
    salvataggio = save3.Save3(grezzo)
    if not salvataggio.integro():
        sys.exit("lo slot attivo non e' integro")
    noti = origini()
    per_record = righe_dump(args.dump, args.file_del_dump)
    indice, forme = illustrazioni()

    voci = []
    specie_viste = set()
    for i in range(save3.POSIZIONI):
        r = salvataggio.leggi_posizione(i)
        if r == VUOTO:
            voci.append(None)
            continue
        if not per_record.get(r):
            sys.exit("la posizione %d non e' nel file del dump" % i)
        riga = per_record[r].pop(0)
        provenienza, dettaglio = noti.get(r, ("collezione", None))
        banda = ETICHETTA[provenienza]
        if provenienza == "evento":
            banda = dettaglio[:14]
        elif provenienza == "lotto":
            banda = "Parco Lotta, %s" % dettaglio
        # dopo il numero nazionale PKHeX scrive il simbolo del sesso quando c'e', quindi non si pretende il trattino
        m = re.search(r": (\d{4})\b", riga["Position"])
        nazionale = int(m.group(1))
        if provenienza == "collezione":
            dettaglio = "%s, %s" % (riga["MetLoc"], riga["Version"])
            if nazionale in specie_viste:
                dettaglio += ", seconda cattura della specie (ADR-077)"
            specie_viste.add(nazionale)
        elif provenienza == "evento":
            dettaglio = "%s, lingua %s" % (dettaglio, riga["OTLang"])
        elif provenienza in ("biglietto", "scambio"):
            dettaglio = "%s, %s" % (riga["MetLoc"], riga["Version"])
        elif provenienza == "lotto":
            dettaglio = "%s, natura %s" % (dettaglio, riga["Nature"])
        voci.append({"specie": riga["Species"], "nazionale": nazionale, "forma": riga["Form"],
                     "soprannome": riga["Nickname"] if riga["IsNicknamed"] == "True" else "",
                     "livello": riga["Level"], "allenatore": riga["OT"], "legale": riga["Legal"],
                     "provenienza": provenienza, "dettaglio": dettaglio, "banda": banda})

    FIGURE.mkdir(exist_ok=True)
    cache = {}
    conteggio = collections.Counter(v["provenienza"] for v in voci if v)
    per_box = [voci[b * PER_BOX:(b + 1) * PER_BOX] for b in range(save3.POSIZIONI // PER_BOX)]
    md = ["# Mappa dei box di Smeraldo, posizione per posizione", "",
          "> Documento generato da `tools/emerald_mappa_box.py`: non si modifica a mano. Descrive il file di `giro11`, cioè la disposizione di ADR-078: la collezione di catture vere dal box 1, poi gli eventi, gli incontri da biglietto, gli scambi in gioco e i due giganti, e in fondo il lotto del Parco Lotta, che finisce nell'ultima posizione del box 14. Per usare il lotto la guida è `GUIDA-PARCO-LOTTA.md`; questo documento serve a sapere che cosa c'è in ogni posizione. Le figure e la copia `.docx` da stampare non entrano in git per ADR-005.",
          "", "Posizione si conta dall'alto a sinistra, sei colonne per cinque righe, come sullo schermo del PC. La colonna Legale è il giudizio di PKHeX sul record.", "",
          "## Riepilogo", "", "| Provenienza | Esemplari |", "|---|---|"]
    for k, e, _ in PROVENIENZE:
        md.append("| %s | %d |" % (e, conteggio[k]))
    md.append("| Totale | %d su %d |" % (sum(conteggio.values()), save3.POSIZIONI))
    md += ["", "| Box | Contenuto | Sfondo |", "|---|---|---|"]
    completa = _modulo(CARTELLA.joinpath("tools", "emerald_cartuccia_completa.py"), "cartuccia_completa")
    sfondi = list(salvataggio.storage()[save3.OFF_SFONDI:save3.OFF_SFONDI + 14])
    for b, contenuto in enumerate(per_box, start=1):
        parti = collections.Counter(v["provenienza"] for v in contenuto if v)
        md.append("| %d | %s | %s |" % (b, ", ".join("%s %d" % (ETICHETTA[k], parti[k]) for k, _, _ in PROVENIENZE if parti[k]) or "vuoto",
                                        completa.NOMI_SFONDI[sfondi[b - 1]]))
    for b, contenuto in enumerate(per_box, start=1):
        nome = "mappa-box-%02d.png" % b
        figura(b, contenuto, indice, forme, cache, FIGURE.joinpath(nome))
        md += ["", "## Box %d" % b, "", "![Box %d](figure/%s)" % (b, nome), "",
               "| Posizione | Riga | Colonna | Pokémon | Soprannome | Livello | Allenatore | Provenienza | Dettaglio | Legale |",
               "|---|---|---|---|---|---|---|---|---|---|"]
        for n, v in enumerate(contenuto, start=1):
            r, c = (n - 1) // COLONNE + 1, (n - 1) % COLONNE + 1
            if not v:
                md.append("| %d | %d | %d | vuoto |  |  |  |  |  |  |" % (n, r, c))
                continue
            md.append("| %d | %d | %d | %s | %s | %s | %s | %s | %s | %s |" % (
                n, r, c, v["specie"], v["soprannome"], v["livello"], v["allenatore"], ETICHETTA[v["provenienza"]],
                v["dettaglio"], "sì" if v["legale"] == "True" else "no"))
    USCITA.write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")
    _modulo(RADICE.joinpath("tools", "md-to-docx.py"), "md_to_docx").converti(USCITA, USCITA.with_suffix(".docx"))
    print("scritto %s, 14 figure e %s" % (USCITA, USCITA.with_suffix(".docx")))
    for k, e, _ in PROVENIENZE:
        print("  %-18s %d" % (e, conteggio[k]))


if __name__ == "__main__":
    main()
