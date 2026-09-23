#!/usr/bin/env python3
"""Cerca, fra tutti i semi del generatore di Smeraldo, gli incontri selvatici di Lotad e Seedot con la taglia massima, e compone i due esemplari.

Perche' esiste
--------------

A Ceneride due fratelli misurano Lotad e Seedot e premiano chi supera il loro record. La taglia non e' casuale ne' scritta in un campo: la calcola `GetMonSizeHash` in `src/pokemon_size_record.c` dai sedici bit bassi della personalita' e dai quattro bit bassi di ciascun valore individuale, e `GetMonSize` la traduce in centimetri con una tabella a gradini. Il massimo si ha quando i due byte del risultato valgono entrambi 255, e per le due specie, alte mezzo metro, vale 86,2 centimetri; pokemonrng lo conferma e lo stima a circa uno su trentaduemila.

```c
u32 hibyte = ((attackIV ^ defenseIV) * hpIV) ^ (personality & 0xFF);
u32 lobyte = ((spAtkIV ^ spDefIV) * speedIV) ^ (personality >> 8);
return (hibyte << 8) + lobyte;
```

Il vincolo che rende la ricerca non banale e' che l'esemplare deve essere un selvatico legittimo, e in Smeraldo un selvatico nasce da una catena di estrazioni che il verificatore risale: prima il riquadro della tabella, `ChooseWildMonIndex_Land`, poi il livello, `ChooseWildMonLevel`, poi la natura, `PickWildMonNature`, poi la personalita' rigenerata finche' la sua natura coincide, poi le due parole dei valori individuali. Questo programma cerca il caso piu' semplice e pulito, quello con un capogruppo senza abilita' che interferiscano e la personalita' riuscita al primo tentativo: dallo stato della meta' bassa della personalita' si risale di tre passi per il riquadro, di due per il livello e di uno per la natura, e si scende di uno per la meta' alta e di due e tre per i valori individuali.

Gli incontri, da `src/data/wild_encounters.json`: Lotad al Percorso 114, riquadro 1, livello 16; Seedot al Percorso 120, riquadro 11, livello 25. Fra tutti i semi validi si tiene quello con la somma di valori individuali piu' alta.

Il Wynaut dell'Isola Miraggio
-----------------------------

Dal 2026-09-23, su richiesta del proprietario, lo stesso generatore produce anche un Wynaut catturato all'Isola Miraggio, con `--isola-miraggio`. L'isola compare sul Percorso 130, e la sua erba e' la tabella `gRoute130` di `wild_encounters.json`, dodici riquadri tutti di Wynaut; la mappa `Route130` ha come sezione `MAPSEC_ROUTE_130`, quindi il luogo d'incontro che il gioco scrive, e che PKHeX mostra, e' il Percorso 130 e non un luogo chiamato Isola Miraggio. Si usa il riquadro 0, il piu' frequente, livello 30. Non c'e' alcun vincolo di taglia: e' una cattura qualunque, quindi non si sceglie il seme con i valori individuali migliori ma il primo valido nell'ordine di ricerca, che da' valori ordinari come quelli di chi ha catturato davvero il primo Wynaut incontrato. La sfera e' una Ultra Ball.

Uso
---

    python gba-save-extraction-smeraldo/tools/emerald_selvatico_gigante.py --out _notes/lotto-giganti
    python gba-save-extraction-smeraldo/tools/emerald_selvatico_gigante.py --out _notes/lotto-wynaut --isola-miraggio
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
sys.path.insert(0, str(RADICE.joinpath("pokemon-gen12-gen3-bridge-original-hardware")))

from pokebridge import charmap, gen3  # noqa: E402

M = 0x41C64E6D
A = 0x6073
MI = pow(M, -1, 1 << 32)
MASK = np.uint64(0xFFFFFFFF)
TID, SID = 45761, 56446
# Le soglie cumulative dei dodici riquadri d'erba, da `ENCOUNTER_CHANCE_LAND_MONS_SLOT_*`.
SOGLIE_ERBA = [20, 40, 50, 60, 70, 80, 85, 90, 94, 98, 99, 100]

ULTRA_BALL = 2
# Le quattro mosse di Wynaut al livello 30 si scrivono nell'ordine della tabella del gioco e non si
# ricavano da `mosse-imparabili.json`: quattro mosse si imparano tutte al livello 15, e a pari livello
# `GiveMonInitialMoveset` segue l'ordine di `sWynautLevelUpLearnset` in
# `src/data/pokemon/level_up_learnsets.h`, righe 4835-4838, che il dizionario non conserva. La ricerca
# parte da uno stato arbitrario e non da zero, perche' dallo zero il primo seme valido ha la meta'
# bassa della personalita' nulla, che e' legale ma non e' cio' che una cattura qualunque produce.
MIRAGGIO = {"Wynaut": {"luogo": 0x10 + 130 - 101, "nome_luogo": "Percorso 130, Isola Miraggio", "riquadro": 0, "livello": 30,
                       "mosse": ["Counter", "Mirror Coat", "Safeguard", "Destiny Bond"], "partenza": 0x9E3779B9}}

INCONTRI = {
    "Lotad": {"luogo": 0x10 + 114 - 101, "nome_luogo": "Percorso 114", "riquadro": 1, "livello": 16},
    "Seedot": {"luogo": 0x10 + 120 - 101, "nome_luogo": "Percorso 120", "riquadro": 11, "livello": 25},
}


def avanti(x):
    return (x * np.uint64(M) + np.uint64(A)) & MASK


def indietro(x):
    return ((x - np.uint64(A)) * np.uint64(MI)) & MASK


def cerca(riquadro, soglia_femmina=None, blocco=1 << 24, taglia=True, primo=False, partenza=0):
    lo = 0 if riquadro == 0 else SOGLIE_ERBA[riquadro - 1]
    hi = SOGLIE_ERBA[riquadro]
    migliori = []
    for inizio in range(0, 1 << 32, blocco):
        x = (np.arange(inizio, inizio + blocco, dtype=np.uint64) + np.uint64(partenza)) & MASK  # stato della meta' bassa
        s_nat = indietro(x)
        s_liv = indietro(s_nat)
        s_riq = indietro(s_liv)
        r_riq = (s_riq >> np.uint64(16)) % np.uint64(100)
        ok = (r_riq >= lo) & (r_riq < hi)
        s_alta = avanti(x)
        pid = ((s_alta >> np.uint64(16)) << np.uint64(16)) | (x >> np.uint64(16))
        ok &= ((s_nat >> np.uint64(16)) % np.uint64(25)) == (pid % np.uint64(25))
        s_iv1 = avanti(s_alta)
        s_iv2 = avanti(s_iv1)
        p1 = (s_iv1 >> np.uint64(16)) & np.uint64(0x7FFF)
        p2 = (s_iv2 >> np.uint64(16)) & np.uint64(0x7FFF)
        hp, at, de = p1 & np.uint64(31), (p1 >> np.uint64(5)) & np.uint64(31), (p1 >> np.uint64(10)) & np.uint64(31)
        ve, sa, sd = p2 & np.uint64(31), (p2 >> np.uint64(5)) & np.uint64(31), (p2 >> np.uint64(10)) & np.uint64(31)
        n = np.uint64(15)
        alto = (((at & n) ^ (de & n)) * (hp & n)) ^ (pid & np.uint64(0xFF))
        basso = (((sa & n) ^ (sd & n)) * (ve & n)) ^ ((pid >> np.uint64(8)) & np.uint64(0xFF))
        if taglia:
            ok &= (alto == 255) & (basso == 255)
        # non cromatico, per non consegnare per sbaglio un cromatico che nessuno ha chiesto
        ok &= ((pid >> np.uint64(16)) ^ (pid & np.uint64(0xFFFF)) ^ np.uint64(TID) ^ np.uint64(SID)) >= 8
        for i in np.nonzero(ok)[0]:
            iv = {"hp": int(hp[i]), "atk": int(at[i]), "def": int(de[i]), "spe": int(ve[i]), "spa": int(sa[i]), "spd": int(sd[i])}
            migliori.append((sum(iv.values()), int(pid[i]), int(s_riq[i]), iv))
            if primo:
                return migliori
    migliori.sort(key=lambda t: -t[0])
    return migliori


def componi(nome, info, dati, pid, iv, incontro, esperienza_tab, sfera=4):
    tabella = charmap.Charmap.gen3()
    gruppo = info["gruppo_crescita"]
    abilita = info["abilita"]
    bit = (pid & 1) if len(abilita) == 2 and abilita[1] != "None" else 0
    mosse = incontro["mosse"]
    return gen3.Gen3Mon(
        personality=pid, ot_id=(SID << 16) | TID,
        nickname=tabella.encode(nome.upper(), length=gen3.NICKNAME_LENGTH), language=4, flags=0x02,
        ot_name=tabella.encode("ALEX", length=gen3.OT_NAME_LENGTH), markings=0,
        growth=gen3.Growth(species=info["id"], held_item=0, experience=esperienza_tab[gruppo][incontro["livello"]],
                           pp_bonuses=0, friendship=70),
        attacks=gen3.Attacks(moves=(mosse + [0, 0, 0, 0])[:4], pp=([m[1] for m in incontro["pp"]] + [0, 0, 0, 0])[:4]),
        evs=gen3.EvsCondition(evs={"hp": 0, "atk": 0, "def": 0, "spd": 0, "satk": 0, "sdef": 0},
                              contest={n: 0 for n in ("cool", "beauty", "cute", "smart", "tough")}, sheen=0),
        misc=gen3.Misc(pokerus=0, met_location=incontro["luogo"], met_level=incontro["livello"], met_game=3,
                       pokeball=sfera, ot_female=False,
                       ivs={"hp": iv["hp"], "atk": iv["atk"], "def": iv["def"], "spd": iv["spe"], "satk": iv["spa"], "sdef": iv["spd"]},
                       is_egg=False, ability_num=bit, modern_fateful_encounter=False),
    )


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--out", required=True)
    p.add_argument("--isola-miraggio", action="store_true", help="il Wynaut dell'Isola Miraggio invece dei due giganti")
    args = p.parse_args()
    dati = json.loads(CARTELLA.joinpath("dati-gen3.json").read_text(encoding="utf-8"))
    imparabili = json.loads(CARTELLA.joinpath("mosse-imparabili.json").read_text(encoding="utf-8"))
    uscita = Path(args.out)
    uscita.mkdir(parents=True, exist_ok=True)
    riepilogo = {}
    for nome, incontro in (MIRAGGIO if args.isola_miraggio else INCONTRI).items():
        info = dati["specie"][nome]
        trovati = cerca(incontro["riquadro"], taglia=False, primo=True, partenza=incontro["partenza"]) if args.isola_miraggio else cerca(incontro["riquadro"])
        if not trovati:
            sys.exit("nessun seme per %s" % nome)
        somma, pid, seme, iv = trovati[0]
        # Le mosse di un selvatico sono le ultime quattro che impara per livello fino al livello
        # d'incontro, come fa `GiveMonInitialMoveset`; si leggono dalla tabella del sorgente su disco.
        per_livello = [(mossa, v["livello"]) for mossa, v in imparabili[nome].items()
                       if "livello" in v and v["livello"] <= incontro["livello"]]
        nomi_mosse = []
        for mossa, _liv in sorted(per_livello, key=lambda t: t[1]):
            if mossa in nomi_mosse:
                nomi_mosse.remove(mossa)
            nomi_mosse.append(mossa)
        nomi_mosse = incontro.get("mosse") or nomi_mosse[-4:]
        per_chiave = {"".join(c for c in k.lower() if c.isalnum()): v for k, v in dati["mosse"].items()}
        voci = [per_chiave["".join(c for c in m.lower() if c.isalnum())] for m in nomi_mosse]
        incontro = dict(incontro, mosse=[v["id"] for v in voci], pp=[(v["id"], v["pp"]) for v in voci])
        mon = componi(nome, info, dati, pid, iv, incontro, dati["esperienza"], ULTRA_BALL if args.isola_miraggio else 4)
        uscita.joinpath("%s-%s.bin" % (nome.lower(), "isola-miraggio" if args.isola_miraggio else "gigante")).write_bytes(mon.to_bytes())
        riepilogo[nome] = {"candidati": len(trovati), "personalita": "%08X" % pid, "seme_del_riquadro": "%08X" % seme,
                           "iv": iv, "mosse": nomi_mosse, "luogo": incontro["nome_luogo"], "livello": incontro["livello"]}
        print("%s: %d semi validi, scelto personalita' %08X, IV %s, mosse %s" % (nome, len(trovati), pid, iv, nomi_mosse))
    uscita.joinpath("manifesto.json").write_text(json.dumps(riepilogo, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
