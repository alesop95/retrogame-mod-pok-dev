#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quarto giro di correzione: spegne i flag che dichiarano gia' avvenuti gli incontri delle isole.

Perché esiste
-------------
Il terzo giro ha acceso i tre flag di abilitazione della nave, e la verifica in gioco del
2026-09-18 ha dato esito positivo: il marinaio di Alghepoli offre Porto Selcepoli, Parco Lotta,
Isola Remota, Isola Materna e Isola Suprema. Sbarcando, pero', due isole su tre sono vuote:
sull'Isola Materna non c'e' il triangolo del rompicapo, sull'Isola Suprema non c'e' Mew
nell'erba alta, mentre sull'Isola Remota l'incontro parte regolarmente.

Non e' una incoerenza del salvataggio ma di due famiglie di flag che non si parlano. Il
biglietto e il suo FLAG_ENABLE_SHIP_* decidono il viaggio; una seconda famiglia decide se
all'arrivo ci sia ancora qualcosa da incontrare, e su questa partita quella seconda famiglia
dice che Deoxys, Mew, Lugia e Ho-Oh sono gia' stati presi.

    @ pret/pokeemerald, data/maps/BirthIsland_Exterior/scripts.inc, OnTransition
    call_if_set   FLAG_BATTLED_DEOXYS, BirthIsland_Exterior_EventScript_HideDeoxysAndPuzzle
    call_if_unset FLAG_BATTLED_DEOXYS, BirthIsland_Exterior_EventScript_TryShowDeoxysPuzzle

    @ pret/pokeemerald, data/maps/FarawayIsland_Interior/scripts.inc, OnTransition
    call_if_unset FLAG_CAUGHT_MEW, FarawayIsland_Interior_EventScript_TryShowMew

    @ pret/pokeemerald, data/maps/NavelRock_Bottom/scripts.inc e NavelRock_Top/scripts.inc
    call_if_unset FLAG_CAUGHT_LUGIA, NavelRock_Bottom_EventScript_TryShowLugia
    call_if_unset FLAG_CAUGHT_HO_OH, NavelRock_Top_EventScript_TryShowHoOh

In tutti e quattro i casi lo script di transizione, quando il flag e' spento, provvede da se' a
scoprire l'oggetto sulla mappa: ne segue che a questo strumento basta spegnere il flag di testa
di ciascuna coppia, e che i flag FLAG_HIDE_* non vanno toccati perche' li gestisce il gioco.

Perché spegnere e' una restituzione e non una fabbricazione
-----------------------------------------------------------
Questi bit non sono stati accesi giocando questa partita, e non e' una ipotesi ma una
dimostrazione, che sta per esteso in STUDIO-03. In breve: nessuno script di pret/pokeemerald
spegne mai un FLAG_ENABLE_SHIP_*, quindi i quattro flag misurati spenti nel dump originale non
erano mai stati accesi; senza di essi il menu del porto non costruisce la voce dell'isola e
quelle mappe restano irraggiungibili. Di piu', FLAG_CAUGHT_MEW risulta acceso mentre
FLAG_ARRIVED_ON_FARAWAY_ISLAND e' spento, e l'unico ingresso a FarawayIsland_Interior passa per
FarawayIsland_Entrance, la cui transizione accende quel flag senza condizioni: la coppia
osservata e' quindi uno stato che il gioco non puo' produrre.

Spegnerli riporta il salvataggio a cio' che sarebbe stato se nessuno lo avesse manipolato, e
l'esemplare che ne verra' sara' generato dal gioco stesso. Vale registrare che il comando di
script `seteventmon` porta a CreateEnemyEventMon e quindi a CreateEventMon, che in
src/pokemon.c imposta MON_DATA_MODERN_FATEFUL_ENCOUNTER a vero: l'esemplare catturato
sull'isola porta il contrassegno di incontro fatidico, che e' esattamente il tratto che un
verificatore si aspetta di trovare su un Deoxys dell'Isola Materna o su un Mew dell'Isola
Suprema.

Che cosa questo strumento non tocca
-----------------------------------
Non tocca il Pokedex. I flag FLAG_CAUGHT_* di questa famiglia sono flag di evento e non hanno
alcun rapporto con il registro delle specie viste e catturate, che vive in un'altra struttura:
spegnerli non toglie nulla dal Pokedex e non cambia il suo stato di completamento.

Non tocca i FLAG_HIDE_*, per la ragione detta sopra. Non tocca nessuno dei flag di abilitazione
della nave, che sono materia del terzo giro. E rifiuta di spegnere il flag di un'isola che non
sia raggiungibile, cioe' dove manchi l'oggetto in tasca o il suo flag di abilitazione:
sbloccare un incontro dove non si puo' sbarcare produrrebbe la stessa asimmetria che il terzo
giro esiste per riparare, soltanto nell'altro verso.

Ogni gruppo va chiesto esplicitamente: senza opzioni lo strumento non fa nulla e lo dichiara.
La decisione su quali incontri riaprire e' dell'utente e va registrata come ADR.

Questo strumento non scrive mai sulla cartuccia: produce soltanto un nuovo file .sav locale, e
non sovrascrive mai il file passato in ingresso. La scrittura fisica resta un'operazione
separata e manuale con FlashGBX, con il read-back obbligatorio richiesto da
`.claude/rules/hardware-and-perimeter.md`.

Uso
---
    python emerald_encounter_flags_fix.py INGRESSO.sav USCITA.sav --deoxys --mew
    python emerald_encounter_flags_fix.py INGRESSO.sav USCITA.sav --tutti --verifica-soltanto
"""

import argparse
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emerald_bag_decode import (  # noqa: E402
    u16, u32, checksum_prefix, read_slot, assemble, detect_game,
    GAMES, ITEM_SLOT_SIZE, SECTOR_SIZE, SECTORS_PER_SLOT, OFF_CHECKSUM,
)
from emerald_event_flags_decode import (  # noqa: E402
    OFF_FLAGS, flag_get,
    ITEM_MYSTIC_TICKET, ITEM_AURORA_TICKET, ITEM_OLD_SEA_MAP,
    FLAG_ENABLE_SHIP_BIRTH_ISLAND, FLAG_ENABLE_SHIP_FARAWAY_ISLAND,
    FLAG_ENABLE_SHIP_NAVEL_ROCK,
    FLAG_BATTLED_DEOXYS, FLAG_DEFEATED_DEOXYS,
    FLAG_CAUGHT_MEW, FLAG_DEFEATED_MEW,
    FLAG_CAUGHT_LUGIA, FLAG_DEFEATED_LUGIA,
    FLAG_CAUGHT_HO_OH, FLAG_DEFEATED_HO_OH,
)

SECTOR_DATA_SIZE = 3968

# Un gruppo per esemplare. Ogni voce lega l'esemplare all'isola che lo ospita, alla coppia
# oggetto/flag senza la quale quell'isola non e' raggiungibile, e ai flag da spegnere.
# L'ordine dei flag e' quello in cui gli script di transizione li leggono.
GRUPPI = {
    "deoxys": {
        "esemplare": "Deoxys", "isola": "Isola Materna",
        "oggetto": (ITEM_AURORA_TICKET, "Biglietto Aurora"),
        "abilitazione": (FLAG_ENABLE_SHIP_BIRTH_ISLAND, "FLAG_ENABLE_SHIP_BIRTH_ISLAND"),
        "flag": ((FLAG_BATTLED_DEOXYS, "FLAG_BATTLED_DEOXYS"),
                 (FLAG_DEFEATED_DEOXYS, "FLAG_DEFEATED_DEOXYS")),
    },
    "mew": {
        "esemplare": "Mew", "isola": "Isola Suprema",
        "oggetto": (ITEM_OLD_SEA_MAP, "Mappa Stinta"),
        "abilitazione": (FLAG_ENABLE_SHIP_FARAWAY_ISLAND, "FLAG_ENABLE_SHIP_FARAWAY_ISLAND"),
        "flag": ((FLAG_CAUGHT_MEW, "FLAG_CAUGHT_MEW"),
                 (FLAG_DEFEATED_MEW, "FLAG_DEFEATED_MEW")),
    },
    "lugia": {
        "esemplare": "Lugia", "isola": "Monte Cordone",
        "oggetto": (ITEM_MYSTIC_TICKET, "Biglietto Magico"),
        "abilitazione": (FLAG_ENABLE_SHIP_NAVEL_ROCK, "FLAG_ENABLE_SHIP_NAVEL_ROCK"),
        "flag": ((FLAG_CAUGHT_LUGIA, "FLAG_CAUGHT_LUGIA"),
                 (FLAG_DEFEATED_LUGIA, "FLAG_DEFEATED_LUGIA")),
    },
    "hooh": {
        "esemplare": "Ho-Oh", "isola": "Monte Cordone",
        "oggetto": (ITEM_MYSTIC_TICKET, "Biglietto Magico"),
        "abilitazione": (FLAG_ENABLE_SHIP_NAVEL_ROCK, "FLAG_ENABLE_SHIP_NAVEL_ROCK"),
        "flag": ((FLAG_CAUGHT_HO_OH, "FLAG_CAUGHT_HO_OH"),
                 (FLAG_DEFEATED_HO_OH, "FLAG_DEFEATED_HO_OH")),
    },
}

ORDINE = ("deoxys", "mew", "lugia", "hooh")


def scegli_slot(blob):
    """Lo slot piu' recente fra i due, fra quelli che hanno una sezione 0 valida."""
    slots = []
    for idx in range(2):
        if len(blob) < (idx + 1) * SECTORS_PER_SLOT * SECTOR_SIZE:
            break
        slots.append(read_slot(blob, idx))
    usable = [(i, s) for i, s in enumerate(slots) if 0 in s["sezioni"]]
    if not usable:
        raise SystemExit("nessuno slot ha una sezione 0 valida")

    def counter_of(s):
        return max(s["contatori"]) if s["contatori"] else -1

    if len(usable) == 2 and counter_of(usable[0][1]) > counter_of(usable[1][1]):
        return usable[0]
    return usable[-1]


def posizione_flag(flag_id):
    """Ritorna (id_sezione, offset dentro la sezione, maschera di bit) per un flag."""
    off_sb1 = OFF_FLAGS + (flag_id >> 3)
    sec_id = 1 + off_sb1 // SECTOR_DATA_SIZE
    off_sec = off_sb1 % SECTOR_DATA_SIZE
    return sec_id, off_sec, 1 << (flag_id & 7)


def oggetti_chiave(sb1, game):
    tasche = {nome: (off, cnt) for nome, off, cnt, _m, _cap in game["tasche"]}
    off, cnt = tasche["Oggetti chiave"]
    presenti = set()
    for i in range(cnt):
        item_id = u16(sb1, off + i * ITEM_SLOT_SIZE)
        if item_id == 0:
            break
        presenti.add(item_id)
    return presenti


def ricalcola_checksum(sector_full, lunghezza):
    nuovo = checksum_prefix(sector_full, lunghezza // 4)
    struct.pack_into("<H", sector_full, OFF_CHECKSUM, nuovo)
    return nuovo


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("input", help="dump verificato della cartuccia, in sola lettura")
    ap.add_argument("output", help="percorso del nuovo file corretto (mai uguale all'input)")
    for chiave in ORDINE:
        g = GRUPPI[chiave]
        ap.add_argument("--" + chiave, action="store_true",
                        help="riapre l'incontro di %s (%s)" % (g["esemplare"], g["isola"]))
    ap.add_argument("--tutti", action="store_true",
                    help="equivale a chiedere tutti e quattro i gruppi")
    ap.add_argument("--verifica-soltanto", action="store_true",
                    help="calcola e riferisce le modifiche senza scrivere il file di output")
    args = ap.parse_args()

    chiesti = [c for c in ORDINE if args.tutti or getattr(args, c)]
    if not chiesti:
        raise SystemExit("nessun gruppo chiesto: indica almeno fra --deoxys, --mew, --lugia, "
                         "--hooh, oppure --tutti. Senza una scelta esplicita questo strumento "
                         "non tocca nulla, perche' la scelta e' dell'utente e va registrata "
                         "come ADR.")

    if os.path.abspath(args.input) == os.path.abspath(args.output):
        raise SystemExit("l'output non puo' essere uguale all'input: si rischierebbe di "
                         "perdere il backup verificato")

    with open(args.input, "rb") as fh:
        blob = bytearray(fh.read())

    slot_index, slot = scegli_slot(blob)
    sb2, sb1 = assemble(slot)
    if sb1 is None:
        raise SystemExit("SaveBlock1 non ricostruibile dallo slot scelto")

    esiti = detect_game(sb2, sb1)
    punti, nome, game, _prove = esiti[0]
    if game is not GAMES["emerald"] or punti <= 0:
        raise SystemExit("il file non e' identificato come Smeraldo con margine sufficiente "
                         "(punteggio %d su %s): questo script corregge solo Smeraldo"
                         % (punti, nome))

    presenti = oggetti_chiave(sb1, game)

    # Precondizione di raggiungibilita': un incontro si riapre solo dove si possa sbarcare.
    non_raggiungibili = []
    for chiave in chiesti:
        g = GRUPPI[chiave]
        item_id, item_nome = g["oggetto"]
        flag_id, flag_nome = g["abilitazione"]
        mancanze = []
        if item_id not in presenti:
            mancanze.append("%s non e' nella tasca Oggetti Chiave" % item_nome)
        if not flag_get(sb1, flag_id):
            mancanze.append("%s e' spento" % flag_nome)
        if mancanze:
            non_raggiungibili.append((g["esemplare"], g["isola"], mancanze))
    if non_raggiungibili:
        righe = ["%s (%s): %s" % (e, i, "; ".join(m)) for e, i, m in non_raggiungibili]
        raise SystemExit("isola non raggiungibile, nessun flag spento:\n  " + "\n  ".join(righe))

    per_sezione = {}
    righe = []
    for chiave in chiesti:
        g = GRUPPI[chiave]
        for flag_id, flag_nome in g["flag"]:
            sec_id, off_sec, mask = posizione_flag(flag_id)
            gia_spento = not flag_get(sb1, flag_id)
            righe.append((g["esemplare"], g["isola"], flag_nome, flag_id,
                          sec_id, off_sec, mask, gia_spento))
            if not gia_spento:
                per_sezione.setdefault(sec_id, []).append((off_sec, mask))

    print("Slot scelto: %d, chiave 0x%08X" % (slot_index, u32(sb2, game["chiave_offset"])))
    print()
    print("%-10s %-16s %-34s %-12s %s"
          % ("Esemplare", "Isola", "Flag", "gia' spento", "dove"))
    for esemplare, isola, flag_nome, flag_id, sec_id, off_sec, mask, gia in righe:
        print("%-10s %-16s %-34s %-12s sez.%d +0x%03X bit %d"
              % (esemplare, isola, flag_nome, "si" if gia else "no",
                 sec_id, off_sec, mask.bit_length() - 1))
    print()

    if not per_sezione:
        print("Tutti i flag chiesti erano gia' spenti: nessuna modifica da fare, "
              "nessun file scritto.")
        return 0

    for sec_id in per_sezione:
        if sec_id not in slot["sezioni"]:
            raise SystemExit("la sezione %d non e' presente nello slot scelto" % sec_id)

    base = slot_index * SECTORS_PER_SLOT * SECTOR_SIZE
    modifiche = []
    settori = {}

    for sec_id, punti_flag in sorted(per_sezione.items()):
        pos = slot["sezioni"][sec_id]["posizione"]
        lunghezza = slot["sezioni"][sec_id]["lunghezza_checksum"]
        off_file = base + pos * SECTOR_SIZE
        settore = bytearray(blob[off_file:off_file + SECTOR_SIZE])

        byte_prima = {}
        for off_sec, mask in punti_flag:
            byte_prima.setdefault(off_sec, settore[off_sec])
            settore[off_sec] &= 0xFF ^ mask

        vecchio_cs = u16(settore, OFF_CHECKSUM)
        nuovo_cs = ricalcola_checksum(settore, lunghezza)
        settori[sec_id] = (off_file, settore)
        modifiche.append((sec_id, pos, byte_prima,
                          {o: settore[o] for o in byte_prima}, vecchio_cs, nuovo_cs))

    for sec_id, pos, prima, dopo, vecchio_cs, nuovo_cs in modifiche:
        for off in sorted(prima):
            print("Sezione %d (settore fisico %d), offset 0x%03X: 0x%02X -> 0x%02X"
                  % (sec_id, pos, off, prima[off], dopo[off]))
        print("Checksum sezione %d: 0x%04X -> 0x%04X" % (sec_id, vecchio_cs, nuovo_cs))

    if args.verifica_soltanto:
        print("\n--verifica-soltanto: nessun file scritto")
        return 0

    for _sec_id, (off_file, settore) in settori.items():
        blob[off_file:off_file + SECTOR_SIZE] = settore
    with open(args.output, "wb") as fh:
        fh.write(blob)
    print("\nScritto: %s" % args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
