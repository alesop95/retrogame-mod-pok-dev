#!/usr/bin/env python3
"""Estrae dal sorgente di pret/pokeemerald i venti giri della Piramide Lotta, cioe' quali specie selvatiche si incontrano a ciascuna serie.

Perche' esiste
--------------

La Piramide Lotta e' il solo edificio del Parco in cui l'avversario principale non e' un allenatore ma il piano, e in cui cio' che si incontra cambia per intero da una serie alla successiva secondo un ciclo dichiarato. Il gioco calcola il giro come la serie di vittorie divisa per sette e presa modulo venti, quindi ogni sette piani il bestiario si sostituisce da capo e dopo venti giri ricomincia. Ne segue che la domanda "quale squadra porto alla Piramide" non ha una risposta sola: ne ha venti, e per il simbolo d'oro ne servono le prime undici, perche' l'oro arriva a settanta piani e il settantesimo e' gia' nel giro undicesimo.

Una tabella del genere si legge una volta e si sbaglia a memoria per sempre, e sull'enciclopedia e' scritta in prosa a fianco delle frasi che l'indovina pronuncia in gioco. Questo strumento la prende invece dal sorgente, che e' la fonte su cui questo progetto ha gia' corretto quattro affermazioni sbagliate, e la scrive come dato ispezionabile.

Che cosa estrae, e da dove
--------------------------

Legge `src/data/battle_frontier/battle_pyramid_level_50_wild_mons.h` da un clone di `pret/pokeemerald` e ne ricava, per ciascuno dei venti giri, le otto voci con specie, livello e mosse. Il nome del giro nel sorgente e' a base uno, mentre l'indice che il gioco calcola e' a base zero: la corrispondenza fra i due e' la sola aritmetica che questo strumento fa, ed e' anche l'unico punto in cui si potrebbe sbagliare di uno, quindi e' scritta esplicitamente in ogni riga dell'uscita invece che lasciata al lettore.

Il clone del sorgente non e' versionato in questo progetto e non deve esserlo: si ottiene con un clone superficiale al momento del bisogno, e il percorso si passa da riga di comando. Se il percorso non esiste, lo strumento lo dice e si ferma invece di indovinare.

Uso
---

    git clone --depth 1 --filter=blob:none --sparse https://github.com/pret/pokeemerald.git <cartella>
    python gba-save-extraction-smeraldo/tools/parco_lotta_piramide_giri.py --sorgente <cartella> --out _notes/fonti/raccolte/parco-lotta-spoglio-2026-09-21
"""

import argparse
import json
import re
import sys
from pathlib import Path

PERCORSO_INTERNO = "src/data/battle_frontier/battle_pyramid_level_50_wild_mons.h"

# Il tema di ciascun giro, cioe' la ragione per cui quelle otto specie stanno insieme, come l'indovina
# accanto al computer lo annuncia in gioco. Non e' nel sorgente, che porta solo le specie: viene dalla
# pagina Bulbapedia della Piramide, e sta qui perche' e' l'unica cosa che rende la tabella leggibile.
# La corrispondenza fra i venti temi e i venti giri e' stata verificata voce per voce contro le specie.
TEMI = [
    "mosse che paralizzano", "mosse che avvelenano", "mosse che scottano", "consumo dei punti potere",
    "abilita' Levitazione", "abilita' che intrappolano", "tipo Ghiaccio", "Autodistruzione ed Esplosione",
    "tipo Psico", "tipo Roccia", "tipo Lotta", "mosse che cambiano il tempo", "tipo Coleottero",
    "tipo Buio", "tipo Acqua", "tipo Spettro", "tipo Acciaio", "tipi Volante e Drago",
    "evoluzioni da pietra, con fuoco acqua ed elettricita'", "tipo Normale che conosce Iper Raggio",
]


def estrai(percorso_sorgente):
    intestazione = Path(percorso_sorgente).joinpath(PERCORSO_INTERNO)
    if not intestazione.exists():
        sys.exit("intestazione non trovata: %s\nserve un clone di pret/pokeemerald, vedi il docstring" % intestazione)
    testo = intestazione.read_text(encoding="utf-8")
    giri = []
    for numero in range(1, 21):
        blocco = re.search(r"sLevel50WildMons_Round%d\[\]\s*=\s*\{(.*?)\n\};" % numero, testo, re.S)
        if blocco is None:
            sys.exit("giro %d non trovato nell'intestazione: la fonte e' cambiata, non indovino" % numero)
        voci = []
        for voce in re.finditer(r"\{(.*?)\}\s*,?\s*(?=\{|\Z)", blocco.group(1), re.S):
            corpo = voce.group(1)
            specie = re.search(r"\.species\s*=\s*SPECIES_(\w+)", corpo)
            if specie is None:
                continue
            livello = re.search(r"\.lvl\s*=\s*(\d+)", corpo)
            mosse = re.findall(r"MOVE_(\w+)", corpo)
            voci.append({
                "specie": specie.group(1).title().replace("_", " "),
                "livello": int(livello.group(1)) if livello else None,
                "mosse": [m.title().replace("_", " ") for m in mosse],
            })
        if len(voci) != 8:
            sys.exit("giro %d: lette %d voci invece di otto, la forma della fonte e' cambiata" % (numero, len(voci)))
        giri.append({
            "giro_sorgente": numero,
            "indice_calcolato": numero - 1,
            "serie": [(numero - 1) * 7, (numero - 1) * 7 + 6],
            "tema": TEMI[numero - 1],
            "specie": voci,
        })
    return giri


def scrivi_documento(percorso, giri):
    r = []
    r.append("# I venti giri della Piramide Lotta, a livello 50")
    r.append("")
    r.append("> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_piramide_giri.py` dal sorgente `pret/pokeemerald`, intestazione `%s`. Non si modifica a mano: si rigenera." % PERCORSO_INTERNO)
    r.append("")
    r.append("Il gioco calcola il giro come `(serie di vittorie / 7) % 20`, quindi l'indice e' a base zero mentre il nome nel sorgente e' a base uno. Il simbolo d'argento arriva a ventuno piani e l'oro a settanta, quindi per l'oro si attraversano i giri da 1 a 10 e si affronta Brandon all'inizio dell'undicesimo.")
    r.append("")
    r.append("| Giro | Indice | Piani | Tema | Specie |")
    r.append("|---|---|---|---|---|")
    for g in giri:
        r.append("| %d | %d | %d-%d | %s | %s |" % (
            g["giro_sorgente"], g["indice_calcolato"], g["serie"][0], g["serie"][1], g["tema"],
            ", ".join(sorted({v["specie"] for v in g["specie"]}))))
    r.append("")
    for g in giri:
        r.append("## Giro %d, piani %d-%d, %s" % (g["giro_sorgente"], g["serie"][0], g["serie"][1], g["tema"]))
        r.append("")
        for v in g["specie"]:
            r.append("- %s, livello %s: %s" % (v["specie"], v["livello"], ", ".join(v["mosse"])))
        r.append("")
    Path(percorso).write_text("\n".join(r) + "\n", encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--sorgente", required=True, help="cartella di un clone di pret/pokeemerald")
    p.add_argument("--out", required=True)
    args = p.parse_args()

    giri = estrai(args.sorgente)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    out.joinpath("piramide-giri.json").write_text(json.dumps(giri, ensure_ascii=False, indent=1), encoding="utf-8")
    scrivi_documento(out.joinpath("PIRAMIDE-GIRI.md"), giri)
    print("venti giri estratti, otto specie ciascuno, uscita in %s" % out)


if __name__ == "__main__":
    main()
