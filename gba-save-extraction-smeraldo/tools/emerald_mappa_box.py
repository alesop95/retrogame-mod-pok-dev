#!/usr/bin/env python3
"""Genera la mappa stampabile dei quattordici box di Smeraldo: che cosa c'e' in ogni posizione, con l'illustrazione di Sugimori, e da dove viene.

Perche' esiste
--------------

Dopo ADR-076, ADR-077 e ADR-078 il deposito e' pieno, 420 su 420, e mescola sette provenienze: la collezione di catture vere, gli eventi in tutte le lingue, gli incontri da biglietto, gli scambi in gioco, il Seedot e il Lotad piu' grandi possibili, il Wynaut dell'Isola Miraggio e il lotto del Parco Lotta. Chi apre il PC del gioco vede soltanto trenta icone per box e non sa quale di tre Latios sia l'evento e quale la cattura. Questo strumento risponde posizione per posizione, e lo fa leggendo i byte del salvataggio invece di fidarsi della regola che li ha disposti: la provenienza di ogni posizione si riconosce confrontando il record con i file dei lotti, e i dati leggibili vengono dal dump di PKHeX.

Il dump puo' appartenere a un altro file, purche' contenga gli stessi record, perche' lo strumento lo accoppia per contenuto e non per posizione; se ne possono passare piu' d'uno. Un record che nessun dump contiene, come un esemplare appena aggiunto e non ancora giudicato, si descrive dai suoi byte e dalle tabelle del progetto, e lo strumento lo dichiara a terminale.

Per gli eventi la tabella riporta la storia della distribuzione, cioe' quando, dove e come fu consegnata e perche' e' notevole, da `recreate-pokemon-distributions-events/provenienze-eventi.json`, che e' la stessa fonte autorata del catalogo degli eventi, con l'evento individuato dalla coppia allenatore e identificativo della tabella del verificatore. Per non ripetere lo stesso testo, la storia si scrive alla prima posizione del box in cui l'evento compare, e le successive vi rimandano.

La stampa
---------

Il proprietario ha fissato il formato il 2026-09-23: foglio orizzontale, per ogni box una pagina con la figura e una con la tabella, mai di piu'; la legenda dei colori e il riepilogo una volta sola in testa; carattere sempre nero; nessuna colonna di legalita', perche' il deposito e' tutto legale e la colonna sarebbe costante. La copia `.docx` si costruisce qui con python-docx invece che dal convertitore generico, perche' servono l'orientamento orizzontale e il salto di pagina per box; poi Word la esporta in PDF e lo strumento conta le pagine di ogni tabella, e dove una tabella sfora rimpicciolisce il carattere di quel box e ricomincia. Le figure usano Arial e le tabelle Arial Narrow, caratteri da ufficio invece di quello predefinito di matplotlib.

Le illustrazioni vengono dalla raccolta locale del proprietario e restano fuori da git con le figure e le copie da stampare, per ADR-005; il documento Markdown generato si versiona.

Uso
---

    python gba-save-extraction-smeraldo/tools/emerald_mappa_box.py SALVATAGGIO.sav --dump DUMP.csv FILE_DEL_DUMP.sav [--dump ...]

Scrive `gba-save-extraction-smeraldo/MAPPA-BOX-SMERALDO.md`, le figure `figure/mappa-box-NN.png`, e le copie `MAPPA-BOX-SMERALDO.docx` e `MAPPA-BOX-SMERALDO.pdf`.
"""

import argparse
import collections
import csv
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402
from PIL import Image  # noqa: E402

# Arial per le figure; il font giapponese di Windows fa da riserva per gli allenatori in kana.
plt.rcParams["font.family"] = ["Arial", "Yu Gothic", "MS Gothic"]

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
sys.path.insert(0, str(RADICE.joinpath("pokemon-gen12-gen3-bridge-original-hardware")))

from pokebridge import charmap, gen3, save3  # noqa: E402

NOTE = RADICE.joinpath("_notes")
FIGURE = CARTELLA.joinpath("figure")
USCITA = CARTELLA.joinpath("MAPPA-BOX-SMERALDO.md")
PKHEX = NOTE.joinpath("fonti", "pkhex")
SUGIMORI = Path.home().joinpath("Proton Drive", "alesop95", "My files", "Sugimori Pokémon Gen1-9 DLC3 Organized",
                                "Sugimori Pokémon Gen1-9 DLC3 Organized", "Pokémon By Generation")
PER_BOX = 30
COLONNE = 6
VUOTO = bytes(save3.RECORD)

# Sette provenienze, sette slot categoriali nell'ordine fisso della tavolozza di riferimento della
# skill di visualizzazione. Il testo e' sempre nero, per scelta del proprietario, quindi le caselle
# usano una tinta schiarita di ciascun colore, sulla quale il nero si legge; il colore non e' mai il
# solo segnale, perche' ogni casella porta la provenienza scritta.
PROVENIENZE = [
    ("collezione", "Collezione", "Collezione", "#2a78d6"),
    ("evento", "Evento", "Evento", "#eb6834"),
    ("biglietto", "Incontro da biglietto", "Incontro da biglietto", "#1baf7a"),
    ("scambio", "Scambio in gioco", "Scambio in gioco", "#eda100"),
    ("gigante", "Seedot e Lotad più grandi possibili", "Il più grande possibile", "#e87ba4"),
    ("selvatico", "Wynaut dell'Isola Miraggio", "Isola Miraggio", "#4a3aa7"),
    ("lotto", "Parco Lotta", "Parco Lotta", "#008300"),
]
ETICHETTA = {k: e for k, e, _, _ in PROVENIENZE}
BANDA = {k: b for k, _, b, _ in PROVENIENZE}
NERO = "#000000"
SUPERFICIE = "#ffffff"
BORDO = "#bdbcb6"
FORME_DEOXYS = {"1": "Attack", "2": "Defense", "3": "Speed"}
# Le note delle provenienze mescolano la storia della distribuzione con osservazioni sul lavoro del
# progetto, cioe' su tabelle, verificatore e fonti. La stampa e' per chi guarda la collezione e ne
# tiene soltanto la storia: una frase che nomina uno di questi termini resta nel catalogo degli eventi
# e non entra qui. Per la stessa ragione non entrano le divergenze fra le fonti.
DI_LAVORO = re.compile(r"verificator|progett|tabella|PKHeX|enciclopedi|fonte|fonti|strumento|campo", re.IGNORECASE)
UOVA_POKEMON_BOX = {"Swablu": 333, "Zigzagoon": 263, "Skitty": 300, "Pichu": 172}


def tinta(esadecimale, quota=0.42):
    """Il colore mescolato al bianco: quota e' la parte di colore che resta."""
    r, g, b = (int(esadecimale[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02x%02x%02x" % tuple(round(255 - (255 - c) * quota) for c in (r, g, b))


TINTA = {k: tinta(c) for k, _, _, c in PROVENIENZE}


def _modulo(percorso, nome):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def storie_degli_eventi():
    """{record cifrato: chiave dell'evento} e le provenienze storiche per chiave."""
    catalogo = _modulo(RADICE.joinpath("tools", "catalogo-eventi.py"), "catalogo_eventi")
    voci = catalogo.carica_generatore().voci_wc3(str(PKHEX))
    provenienze = json.loads(Path(catalogo.PROVENIENZE).read_text(encoding="utf-8"))
    per_record = {}
    for f in sorted(NOTE.joinpath("lotto-eventi").glob("*.pk3")):
        indice = int(f.stem.split("-")[0])
        # Le quattro uova di Pokemon Box hanno nel nome un numero che non e' l'indice della tabella:
        # si ritrovano per specie fra le voci dell'allenatore del blocco "Pokemon Box -- Recipient".
        if indice >= len(voci):
            specie = UOVA_POKEMON_BOX[f.stem.split("-")[-1]]
            indice = next(i for i, v in enumerate(voci) if "ＡＺＵＳＡ" in v["ot"] and v["nazionale"] == specie)
        cifrato = NOTE.joinpath("lotto-eventi", "forma-cifrata", f.stem + ".ek3").read_bytes()
        per_record[cifrato] = catalogo.chiave(voci[indice])
    return per_record, provenienze["gruppi"]


def origini():
    """Ogni record dei lotti, nella forma che il salvataggio contiene, con provenienza e dettaglio grezzo."""
    noti = {}
    for tipo, cartella in (("biglietto", "lotto-incontri-gen3"), ("scambio", "lotto-scambi-gen3")):
        for f in sorted(NOTE.joinpath(cartella).glob("*.pk3")):
            noti[NOTE.joinpath(cartella, "forma-cifrata", f.stem + ".ek3").read_bytes()] = (tipo, f.stem)
    for f in sorted(NOTE.joinpath("lotto-giganti").glob("*-gigante.bin")):
        noti[f.read_bytes()] = ("gigante", "86,2 cm, il massimo per la specie, da mostrare ai fratelli di Ceneride")
    manifesto = json.loads(NOTE.joinpath("lotto-wynaut", "manifesto.json").read_text(encoding="utf-8"))
    for f in sorted(NOTE.joinpath("lotto-wynaut").glob("*.bin")):
        voce = manifesto[f.stem.split("-")[0].capitalize()]
        noti[f.read_bytes()] = ("selvatico", "%s, livello %d, Ultra Ball: l'isola compare sul Percorso 130 e il gioco "
                                "registra quel percorso come luogo d'incontro" % (voce["luogo"], voce["livello"]))
    percorso = _modulo(CARTELLA.joinpath("tools", "parco_lotta_percorso_oro.py"), "percorso_oro")
    catalogo = json.loads(percorso.CATALOGO.read_text(encoding="utf-8"))
    thread = json.loads(percorso._mappa().THREAD.read_text(encoding="utf-8"))
    _, _, _, titolari = percorso.disposizione(catalogo, thread)
    for f in sorted(NOTE.joinpath("lotto-parco-lotta", "esemplari").glob("*-copia1.bin")):
        chiave = f.stem[:-len("-copia1")]
        noti[f.read_bytes()] = ("lotto", "titolare" if chiave in titolari else "riserva")
    return noti


def righe_dump(coppie):
    """Le righe dei dump per contenuto del record: {record: riga}, dalle posizioni dei file a cui i dump appartengono."""
    per_record = {}
    for dump, file_del_dump in coppie:
        salvataggio = save3.Save3(Path(file_del_dump).read_bytes())
        per_posizione = {}
        with open(dump, encoding="utf-8-sig") as f:
            for riga in csv.DictReader(f):
                m = re.search(r"@ \[(\d+)\] \([^)]*\)-(\d+)", riga["Position"])
                if m:
                    per_posizione[(int(m.group(1)) - 1) * PER_BOX + int(m.group(2)) - 1] = riga
        for i in range(save3.POSIZIONI):
            r = salvataggio.leggi_posizione(i)
            if r != VUOTO:
                if i not in per_posizione:
                    sys.exit("il dump %s non ha la posizione %d del suo file" % (dump, i))
                per_record.setdefault(r, per_posizione[i])
    return per_record


def riga_dai_byte(record, nature):
    """I campi della tabella per un record che nessun dump contiene, ricavati dai byte e dalle tabelle del progetto."""
    dati = json.loads(CARTELLA.joinpath("dati-gen3.json").read_text(encoding="utf-8"))
    mon = gen3.Gen3Mon.from_bytes(record)
    nome, info = next((n, v) for n, v in dati["specie"].items() if v["id"] == mon.growth.species)
    curva = dati["esperienza"][info["gruppo_crescita"]]
    livello = max(liv for liv in range(1, 101) if curva[liv] <= mon.growth.experience)
    tabella = charmap.Charmap.gen3()
    return {"Species": nome, "Nickname": "", "IsNicknamed": "False", "Level": str(livello),
            "OT": tabella.decode(mon.ot_name).strip(), "Nature": nature.get(mon.personality % 25, ""),
            "Form": "0", "MetLoc": "", "Version": "Smeraldo", "OTLang": "Italian",
            "Position": ": %04d" % nazionale_per_nome(nome)}


def nazionale_per_nome(nome):
    """Il numero nazionale dal nome inglese della specie, letto dai nomi dei file della raccolta di Sugimori: `dati-gen3.json` porta soltanto l'indice interno, che per le specie di Hoenn e' diverso."""
    for n in (1, 2, 3):
        for f in SUGIMORI.joinpath("Generation %d Pokémon" % n).glob("*.png"):
            m = re.match(r"(\d{4}) (.+)\.png$", f.name)
            if m and m.group(2).lower() == nome.lower():
                return int(m.group(1))
    sys.exit("specie %s assente dalla raccolta di Sugimori" % nome)


def illustrazioni():
    """Il file di Sugimori per numero nazionale, dalle prime tre generazioni."""
    indice = {}
    for n in (1, 2, 3):
        for f in SUGIMORI.joinpath("Generation %d Pokémon" % n).glob("*.png"):
            m = re.match(r"(\d{4}) ", f.name)
            if m:
                indice[int(m.group(1))] = f
    return indice, SUGIMORI.joinpath("Generation 3 Pokémon", "Pokémon Specific Forms Gen 3")


def miniatura(percorso, cache):
    if percorso not in cache:
        im = Image.open(percorso).convert("RGBA")
        im.thumbnail((260, 260))
        cache[percorso] = im
    return cache[percorso]


def figura(box, voci, indice, forme, cache, uscita):
    """La griglia del box in proporzione A4 orizzontale, testo nero, senza legenda."""
    fig, ax = plt.subplots(figsize=(11.69, 8.27), facecolor=SUPERFICIE)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    ax.set_xlim(0, COLONNE)
    ax.set_ylim(0, 5.3)
    ax.invert_yaxis()
    ax.set_aspect("auto")
    ax.axis("off")
    ax.text(0.04, 0.15, "Box %d" % box, fontsize=17, color=NERO, fontweight="bold", va="center")
    for n, v in enumerate(voci, start=1):
        r, c = (n - 1) // COLONNE, (n - 1) % COLONNE
        y0 = r + 0.3
        ax.add_patch(FancyBboxPatch((c + 0.04, y0 + 0.04), 0.92, 0.92, boxstyle="round,pad=0,rounding_size=0.05",
                                    facecolor=SUPERFICIE, edgecolor=BORDO, linewidth=0.9))
        ax.text(c + 0.1, y0 + 0.13, str(n), fontsize=8, color=NERO, va="center")
        if not v:
            continue
        ax.add_patch(FancyBboxPatch((c + 0.04, y0 + 0.82), 0.92, 0.14, boxstyle="round,pad=0,rounding_size=0.04",
                                    facecolor=TINTA[v["provenienza"]], edgecolor="none"))
        ax.text(c + 0.5, y0 + 0.89, v["banda"], fontsize=6.8, color=NERO, ha="center", va="center")
        percorso = indice.get(v["nazionale"])
        if v["nazionale"] == 386 and v["forma"] in FORME_DEOXYS:
            alternativa = forme.joinpath("0386 Deoxys %s.png" % FORME_DEOXYS[v["forma"]])
            percorso = alternativa if alternativa.exists() else percorso
        if percorso:
            # la griglia riempie il foglio, quindi un'unita' orizzontale e una verticale non hanno la stessa
            # lunghezza: il lato orizzontale dell'immagine si corregge perche' l'illustrazione resti in proporzione
            lato = 0.46
            largo = lato * (8.27 * 0.96 / 5.3) / (11.69 * 0.96 / COLONNE)
            ax.imshow(miniatura(percorso, cache), extent=(c + 0.5 - largo / 2, c + 0.5 + largo / 2, y0 + 0.08 + lato, y0 + 0.08),
                      zorder=3, aspect="auto")
        ax.text(c + 0.5, y0 + 0.63, v["specie"], fontsize=9, color=NERO, ha="center", va="center", fontweight="bold")
        ax.text(c + 0.5, y0 + 0.74, "Liv. %s   %s" % (v["livello"], v["allenatore"]), fontsize=7.4, color=NERO,
                ha="center", va="center")
    fig.savefig(uscita, dpi=170, facecolor=SUPERFICIE, metadata={"Software": None})
    plt.close(fig)


def racconto(chiave, riga, provenienze):
    """La storia dell'evento come testo continuo: nome, allenatore, lingua, quando, dove, come e perche' conta."""
    p = provenienze.get(chiave)
    ot, ident = chiave.rsplit("|", 1)
    testa = "allenatore %s, identificativo %s, lingua %s" % (riga["OT"] or ot, ident, riga["OTLang"])
    if p is None:
        return ("Uovo del blocco «Pokémon Box -- Recipient» della tabella di PKHeX, consegnato con una mossa "
                "che la specie non impara, e schiuso dal ricevente; %s. Il catalogo non ne registra ancora data, "
                "luogo e modo: la tradizione lo lega al programma Pokémon Box Rubino e Zaffiro per GameCube, "
                "da verificare su una fonte." % testa)
    parti = ["%s: %s." % (p["nome"], testa), "Quando: %s." % p["date"], "Dove: %s." % p["luogo"], "Come: %s." % p["come"]]
    if p.get("oggetto_tenuto"):
        parti.append("Oggetto tenuto: %s." % p["oggetto_tenuto"].rstrip("."))
    if p.get("note"):
        parti.extend(frase for frase in re.split(r"(?<=[.;])\s+", p["note"]) if not DI_LAVORO.search(frase))
    return " ".join(parti)


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("salvataggio")
    p.add_argument("--dump", nargs=2, action="append", required=True, metavar=("DUMP", "FILE_DEL_DUMP"))
    args = p.parse_args()
    salvataggio = save3.Save3(Path(args.salvataggio).read_bytes())
    if not salvataggio.integro():
        sys.exit("lo slot attivo non e' integro")
    noti = origini()
    eventi, provenienze = storie_degli_eventi()
    per_record = righe_dump(args.dump)
    nature = {int(r["PID"], 16) % 25: r["Nature"] for r in per_record.values()}
    indice, forme = illustrazioni()

    voci = []
    specie_viste = set()
    for i in range(save3.POSIZIONI):
        r = salvataggio.leggi_posizione(i)
        if r == VUOTO:
            voci.append(None)
            continue
        riga = per_record.get(r)
        if riga is None:
            riga = riga_dai_byte(r, nature)
            print("posizione %d: nessun dump contiene questo record, descritto dai byte" % i)
        chiave = eventi.get(r)
        provenienza, dettaglio = ("evento", None) if chiave else noti.get(r, ("collezione", None))
        nazionale = int(re.search(r": (\d{4})\b", riga["Position"]).group(1))
        banda = BANDA[provenienza]
        if provenienza == "collezione":
            dettaglio = "%s, %s" % (riga["MetLoc"], riga["Version"])
            if nazionale in specie_viste:
                dettaglio += ", seconda cattura della specie"
            specie_viste.add(nazionale)
        elif provenienza == "evento":
            prov = provenienze.get(chiave)
            banda = prov["nome"] if prov else "Pokémon Box"
            banda = banda if len(banda) <= 26 else banda[:25].rstrip(" ,") + "…"
            dettaglio = racconto(chiave, riga, provenienze)
        elif provenienza == "biglietto":
            dettaglio = "%s, %s, catturato da un amico con il biglietto dell'evento e ricevuto in scambio" % (
                riga["MetLoc"], riga["Version"])
        elif provenienza == "scambio":
            dettaglio = "ricevuto in %s da %s, scambio a personalità fissa del gioco" % (riga["Version"], riga["OT"])
        elif provenienza == "lotto":
            banda = "Parco Lotta, %s" % dettaglio
            dettaglio = "%s, natura %s" % (dettaglio, riga["Nature"])
        voci.append({"specie": riga["Species"], "nazionale": nazionale, "forma": riga["Form"],
                     "soprannome": riga["Nickname"] if riga["IsNicknamed"] == "True" else "",
                     "livello": riga["Level"], "allenatore": riga["OT"], "lingua": riga["OTLang"],
                     "provenienza": provenienza, "dettaglio": dettaglio, "banda": banda, "chiave": chiave})

    # la storia di un evento si scrive alla prima posizione del box che lo contiene, le altre vi rimandano
    per_box = [voci[b * PER_BOX:(b + 1) * PER_BOX] for b in range(save3.POSIZIONI // PER_BOX)]
    for contenuto in per_box:
        prima = {}
        for n, v in enumerate(contenuto, start=1):
            if v and v["chiave"]:
                if v["chiave"] in prima:
                    v["dettaglio"] = "Stesso evento della posizione %d; allenatore %s, lingua %s." % (
                        prima[v["chiave"]], v["allenatore"], v["lingua"])
                else:
                    prima[v["chiave"]] = n

    FIGURE.mkdir(exist_ok=True)
    cache = {}
    for b, contenuto in enumerate(per_box, start=1):
        figura(b, contenuto, indice, forme, cache, FIGURE.joinpath("mappa-box-%02d.png" % b))

    completa = _modulo(CARTELLA.joinpath("tools", "emerald_cartuccia_completa.py"), "cartuccia_completa")
    sfondi = list(salvataggio.storage()[save3.OFF_SFONDI:save3.OFF_SFONDI + 14])
    conteggio = collections.Counter(v["provenienza"] for v in voci if v)
    riepilogo = []
    for b, contenuto in enumerate(per_box, start=1):
        parti = collections.Counter(v["provenienza"] for v in contenuto if v)
        riepilogo.append((b, "; ".join("%s %d" % (ETICHETTA[k], parti[k]) for k, _, _, _ in PROVENIENZE if parti[k]),
                          completa.NOMI_SFONDI[sfondi[b - 1]]))
    scrivi_markdown(per_box, conteggio, riepilogo)
    scrivi_stampa(per_box, conteggio, riepilogo)
    for k, e, _, _ in PROVENIENZE:
        print("  %-38s %d" % (e, conteggio[k]))


def scrivi_markdown(per_box, conteggio, riepilogo):
    md = ["<!-- generato da gba-save-extraction-smeraldo/tools/emerald_mappa_box.py: non si modifica a mano -->", "",
          "## Legenda e riepilogo", "", "| Colore | Provenienza | Esemplari |", "|---|---|---|"]
    for k, e, _, _ in PROVENIENZE:
        md.append("| %s | %s | %d |" % (TINTA[k], e, conteggio[k]))
    md.append("|  | Totale | %d su %d |" % (sum(conteggio.values()), save3.POSIZIONI))
    md += ["", "| Box | Contenuto | Sfondo |", "|---|---|---|"]
    md += ["| %d | %s | %s |" % t for t in riepilogo]
    for b, contenuto in enumerate(per_box, start=1):
        md += ["", "## Box %d" % b, "", "![Box %d](figure/mappa-box-%02d.png)" % (b, b), "",
               "| Posizione | Riga | Colonna | Pokémon | Soprannome | Livello | Allenatore | Provenienza | Dettaglio |",
               "|---|---|---|---|---|---|---|---|---|"]
        for n, v in enumerate(contenuto, start=1):
            r, c = (n - 1) // COLONNE + 1, (n - 1) % COLONNE + 1
            if not v:
                md.append("| %d | %d | %d | vuoto |  |  |  |  |  |" % (n, r, c))
                continue
            md.append("| %d | %d | %d | %s | %s | %s | %s | %s | %s |" % (
                n, r, c, v["specie"], v["soprannome"], v["livello"], v["allenatore"], ETICHETTA[v["provenienza"]],
                v["dettaglio"].replace("|", "/")))
    USCITA.write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")


def scrivi_stampa(per_box, conteggio, riepilogo):
    """La copia da stampare: .docx orizzontale costruito qui, esportato in PDF da Word, con il controllo delle pagine."""
    corpi = {b: 7.0 for b in range(1, 15)}
    passo = 0.25
    docx_out, pdf_out = USCITA.with_suffix(".docx"), USCITA.with_suffix(".pdf")
    for tentativo in range(8):
        componi_docx(per_box, conteggio, riepilogo, corpi, docx_out)
        esporta_pdf(docx_out, pdf_out)
        sforano, pagine = pagine_che_sforano(pdf_out)
        if not sforano:
            print("stampa: %s e %s, %d pagine: una di legenda e due per box" % (docx_out.name, pdf_out.name, pagine))
            return
        for b in sforano:
            corpi[b] -= passo
            if corpi[b] < 4.5:
                sys.exit("la tabella del box %d non entra in una pagina neppure a 4,5 punti" % b)
        print("tentativo %d: sforano i box %s, riduco il carattere" % (tentativo + 1, sforano))
    sys.exit("impaginazione non riuscita")


def componi_docx(per_box, conteggio, riepilogo, corpi, uscita):
    from docx import Document
    from docx.enum.section import WD_ORIENT
    from docx.enum.text import WD_BREAK
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor

    doc = Document()
    sezione = doc.sections[0]
    sezione.orientation = WD_ORIENT.LANDSCAPE
    sezione.page_width, sezione.page_height = Cm(29.7), Cm(21.0)
    for lato in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sezione, lato, Cm(0.9))
    stile = doc.styles["Normal"]
    stile.font.name = "Arial"
    stile.font.size = Pt(2)
    stile.font.color.rgb = RGBColor(0, 0, 0)
    stile.element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), "MS Gothic")
    stile.paragraph_format.space_after = Pt(0)
    stile.paragraph_format.space_before = Pt(0)

    def testo(paragrafo, contenuto, corpo, grassetto=False, font="Arial Narrow"):
        run = paragrafo.add_run(contenuto)
        run.font.size = Pt(corpo)
        run.font.name = font
        run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), "MS Gothic")
        run.font.bold = grassetto
        run.font.color.rgb = RGBColor(0, 0, 0)
        return run

    def ombra(cella, colore):
        tcPr = cella._element.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), colore.lstrip("#"))
        tcPr.append(shd)

    def margini_stretti(t, cm=0.06):
        mar = OxmlElement("w:tblCellMar")
        for lato in ("top", "bottom", "left", "right"):
            e = OxmlElement("w:%s" % lato)
            e.set(qn("w:w"), str(int(cm * 567)))
            e.set(qn("w:type"), "dxa")
            mar.append(e)
        t._element.tblPr.append(mar)

    def tabella(intestazione, righe, larghezze, corpo, colori=None):
        t = doc.add_table(rows=1 + len(righe), cols=len(intestazione))
        t.style = "Table Grid"
        t.autofit = False
        margini_stretti(t)
        for j, (h, w) in enumerate(zip(intestazione, larghezze)):
            cella = t.rows[0].cells[j]
            cella.width = Cm(w)
            testo(cella.paragraphs[0], h, corpo, grassetto=True)
        for i, riga in enumerate(righe, start=1):
            for j, (valore, w) in enumerate(zip(riga, larghezze)):
                cella = t.rows[i].cells[j]
                cella.width = Cm(w)
                testo(cella.paragraphs[0], valore, corpo)
            if colori and colori[i - 1]:
                ombra(t.rows[i].cells[colori[i - 1][0]], colori[i - 1][1])
        return t

    def a_capo_pagina():
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    testo(doc.add_paragraph(), "Legenda e riepilogo", 12, grassetto=True, font="Arial")
    testo(doc.add_paragraph(), " ", 8)
    tabella(["Colore", "Provenienza", "Esemplari"],
            [("", e, str(conteggio[k])) for k, e, _, _ in PROVENIENZE] + [("", "Totale", "%d su %d" % (sum(conteggio.values()), save3.POSIZIONI))],
            [1.5, 8.0, 3.0], 9, colori=[(0, TINTA[k]) for k, _, _, _ in PROVENIENZE] + [None])
    testo(doc.add_paragraph(), " ", 8)
    tabella(["Box", "Contenuto", "Sfondo"], [(str(b), c, s) for b, c, s in riepilogo], [1.5, 20.0, 3.0], 9)

    for b, contenuto in enumerate(per_box, start=1):
        a_capo_pagina()
        doc.add_paragraph().add_run().add_picture(str(FIGURE.joinpath("mappa-box-%02d.png" % b)), height=Cm(18.4))
        a_capo_pagina()
        testo(doc.add_paragraph(), "Box %d, posizione per posizione" % b, 10, grassetto=True, font="Arial")
        righe, colori = [], []
        for n, v in enumerate(contenuto, start=1):
            rc = "%d (%d-%d)" % (n, (n - 1) // COLONNE + 1, (n - 1) % COLONNE + 1)
            if not v:
                righe.append((rc, "vuoto", "", "", "", "", ""))
                colori.append(None)
                continue
            righe.append((rc, v["specie"], v["soprannome"], v["livello"], v["allenatore"], ETICHETTA[v["provenienza"]], v["dettaglio"]))
            colori.append((5, TINTA[v["provenienza"]]))
        tabella(["Posto (riga-colonna)", "Pokémon", "Soprannome", "Liv.", "Allenatore", "Provenienza", "Dettaglio"],
                righe, [1.4, 1.7, 1.5, 0.6, 1.7, 1.9, 19.1], corpi[b], colori)
    doc.save(str(uscita))


def esporta_pdf(docx_in, pdf_out):
    """Word esporta il .docx in PDF: e' l'impaginazione che il proprietario stampera', non una stima."""
    comando = ("$w = New-Object -ComObject Word.Application; $w.Visible = $false; "
               "$d = $w.Documents.Open('%s'); $d.ExportAsFixedFormat('%s', 17); $d.Close($false); $w.Quit()"
               % (str(docx_in.resolve()), str(pdf_out.resolve())))
    # la prima apertura di Word dopo un avvio a volte esce senza scrivere: si cancella il PDF vecchio,
    # cosi' che non passi per nuovo, e si riprova una volta prima di arrendersi
    for _ in range(2):
        if pdf_out.exists():
            pdf_out.unlink()
        subprocess.run(["powershell", "-NoProfile", "-Command", comando], check=True)
        if pdf_out.exists():
            return
    sys.exit("Word non ha esportato %s" % pdf_out)


def pagine_che_sforano(pdf):
    """I box la cui tabella occupa piu' di una pagina: dopo la pagina con il titolo della tabella deve venire la figura del box seguente."""
    import fitz
    documento = fitz.open(str(pdf))
    titoli = {}
    for i, pagina in enumerate(documento):
        m = re.search(r"Box (\d+), posizione per posizione", pagina.get_text())
        if m:
            titoli[int(m.group(1))] = i
    sforano = []
    for b in range(1, 15):
        fine = titoli[b + 1] - 1 if b < 14 else len(documento)
        if fine - titoli[b] > 1:
            sforano.append(b)
    pagine = len(documento)
    documento.close()
    return sforano, pagine


if __name__ == "__main__":
    main()
