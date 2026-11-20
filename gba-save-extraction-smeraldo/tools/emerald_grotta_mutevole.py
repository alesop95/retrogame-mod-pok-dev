#!/usr/bin/env python3
"""Compone gli otto incontri della Grotta Mutevole di Smeraldo, uno per specie, come li produrrebbe il gioco.

Perche' esiste
--------------
Il 2026-11-18 il proprietario ha deciso (ADR-134, seconda modifica) di avere su Smeraldo le otto specie che la Grotta
Mutevole avrebbe offerto con l'evento del Dono Segreto mai distribuito, ma mai in HOME. La grotta tiene una specie alla
volta (`VAR_ALTERING_CAVE_WILD_SET`, `src/wild_encounter.c` righe 318-326) e sulla cartuccia resta a zero, cioe' Zubat:
le otto specie entrano invece nei box come catture gia' fatte.

Come nasce ciascuno, dal sorgente di pret/pokeemerald
-----------------------------------------------------
La tabella e' `gAlteringCave2`-`gAlteringCave9` di `src/data/wild_encounters.json`, erba con dodici riquadri; si usa il
riquadro 0, il piu' frequente, con il suo livello. La catena di estrazioni del selvatico e la ricerca del seme sono
quelle di `emerald_selvatico_gigante.py` (riquadro, livello, natura, personalita' al primo tentativo, due parole di valori
individuali), con il primo seme valido da una partenza diversa per specie, cosi' che i valori siano quelli di una cattura
qualunque. Il luogo d'incontro e' `MAPSEC_ALTERING_CAVE`, che vale 210 in `src/data/region_map/region_map_sections.json`
ed e' «Altering Cave (E)» anche nei testi di PKHeX. Lo strumento tenuto e' quello della grotta attiva,
`sAlteringCaveWildMonHeldItems` di `src/pokemon.c`, che `SetWildMonHeldItem` assegna con probabilita' 5 su 100: il
proprietario vuole l'esemplare con lo strumento, ed e' un esito che il gioco produce. Le mosse sono quelle di
`GiveMonInitialMoveset`: si percorre la tabella di apprendimento di `src/data/pokemon/level_up_learnsets.h` nell'ordine
del file fino al livello d'incontro, saltando le mosse gia' note e facendo scorrere la piu' vecchia quando sono quattro.
Allenatore ALEX 45761 con il segreto vero, Poke Ball, lingua italiana.

Uso
---
    python gba-save-extraction-smeraldo/tools/emerald_grotta_mutevole.py --out _notes/lotti/lotto-grotta-mutevole
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import emerald_selvatico_gigante as sg  # noqa: E402

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
EMERALD = RADICE.joinpath("_notes", "fonti", "cloni", "pokeemerald")
LUOGO_GROTTA = 210
POKE_BALL = 4

# specie, strumento della grotta attiva, partenza della ricerca del seme
SPECIE = [
    ("Mareep", "Ganlon Berry", 0x1B873593),
    ("Pineco", "Apicot Berry", 0x2C1B3C6D),
    ("Houndour", "Big Mushroom", 0x297A2D39),
    ("Teddiursa", "Petaya Berry", 0x68E31DA4),
    ("Aipom", "Berry Juice", 0x5BD1E995),
    ("Shuckle", "Berry Juice", 0x85EBCA6B),
    ("Stantler", "Petaya Berry", 0xC2B2AE35),
    ("Smeargle", "Salac Berry", 0x27D4EB2F),
]


def tabella_grotta():
    dati = json.loads(EMERALD.joinpath("src", "data", "wild_encounters.json").read_text(encoding="utf-8"))
    per_specie = {}
    for gruppo in dati["wild_encounter_groups"]:
        for e in gruppo["encounters"]:
            etichetta = e.get("base_label", "")
            if etichetta.startswith("gAlteringCave") and etichetta != "gAlteringCave1":
                mons = e["land_mons"]["mons"]
                nome = mons[0]["species"].replace("SPECIES_", "").capitalize()
                if any(m["species"] != mons[0]["species"] for m in mons):
                    sys.exit("%s: la tabella non ha una specie sola" % etichetta)
                per_specie[nome] = {"tabella": etichetta, "livello": mons[0]["min_level"]}
    return per_specie


def mosse_iniziali(nome, livello):
    testo = EMERALD.joinpath("src", "data", "pokemon", "level_up_learnsets.h").read_text(encoding="utf-8")
    m = re.search(r"s%sLevelUpLearnset\[\] = \{(.*?)\};" % nome, testo, re.S)
    if not m:
        sys.exit("tabella di apprendimento di %s non trovata" % nome)
    mosse = []
    for liv, mossa in re.findall(r"LEVEL_UP_MOVE\(\s*(\d+),\s*(MOVE_\w+)\)", m.group(1)):
        if int(liv) > livello or mossa in mosse:
            continue
        if len(mosse) == 4:
            mosse.pop(0)
        mosse.append(mossa)
    return mosse


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--out", required=True)
    args = p.parse_args()
    dati = json.loads(CARTELLA.joinpath("dati-gen3.json").read_text(encoding="utf-8"))
    costanti = EMERALD.joinpath("include", "constants", "moves.h").read_text(encoding="utf-8")
    id_mossa = {k: int(v) for k, v in re.findall(r"#define (MOVE_\w+)\s+(\d+)", costanti)}
    pp_per_id = {v["id"]: v["pp"] for v in dati["mosse"].values()}
    tabella = tabella_grotta()
    uscita = Path(args.out)
    uscita.mkdir(parents=True, exist_ok=True)
    riepilogo = {}
    for nome, strumento, partenza in SPECIE:
        info = dati["specie"][nome]
        livello = tabella[nome]["livello"]
        trovati = sg.cerca(0, taglia=False, primo=True, partenza=partenza)
        if not trovati:
            sys.exit("nessun seme per %s" % nome)
        _somma, pid, seme, iv = trovati[0]
        nomi = mosse_iniziali(nome, livello)
        ids = [id_mossa[m] for m in nomi]
        incontro = {"luogo": LUOGO_GROTTA, "livello": livello, "mosse": ids, "pp": [(i, pp_per_id[i]) for i in ids]}
        mon = sg.componi(nome, info, dati, pid, iv, incontro, dati["esperienza"], POKE_BALL)
        mon.growth.held_item = dati["oggetti"][strumento]
        file = uscita.joinpath("%s-grotta-mutevole.bin" % nome.lower())
        file.write_bytes(mon.to_bytes())
        riepilogo[nome] = {"tabella": tabella[nome]["tabella"], "riquadro": 0, "livello": livello,
                           "personalita": "%08X" % pid, "seme_del_riquadro": "%08X" % seme, "iv": iv,
                           "mosse": nomi, "strumento": strumento, "luogo": "Grotta Mutevole (210)",
                           "file": file.name, "mai_in_home": True}
        print("%s L%d: personalita' %08X, IV %s, mosse %s, strumento %s" % (nome, livello, pid, iv, nomi, strumento))
    uscita.joinpath("manifesto.json").write_text(json.dumps(riepilogo, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
