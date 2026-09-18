#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legge un salvataggio di Pokemon Smeraldo e diagnostica lo stato degli eventi di distribuzione.

Perché esiste
--------------
Il 2026-09-18 l'utente ha verificato in gioco che la tasca Oggetti Chiave contiene Biglietto
Eone, Biglietto Aurora e Mappa Stinta, ma che al porto di Alghepoli il marinaio non
offre alcuna isola: le sole voci sono Porto Selcepoli, Parco Lotta e Annulla. La diagnosi
ingenua sarebbe che il Dono Segreto si sia corrotto, ma il sorgente dice un'altra cosa, e la
dice in modo univoco.

    // src/script_menu.c, CreateLilycoveSSTidalMultichoice
    if (CheckBagHasItem(ITEM_EON_TICKET, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_SOUTHERN_ISLAND) == TRUE)
    if (CheckBagHasItem(ITEM_AURORA_TICKET, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_BIRTH_ISLAND) == TRUE)
    if (CheckBagHasItem(ITEM_OLD_SEA_MAP, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_FARAWAY_ISLAND) == TRUE)
    if (CheckBagHasItem(ITEM_MYSTIC_TICKET, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_NAVEL_ROCK) == TRUE)

La condizione è una congiunzione, non una disgiunzione: il biglietto nello zaino è necessario
e non sufficiente, e il flag che lo accompagna non si accende mettendo l'oggetto nella tasca.
A metterlo sono gli script di consegna del Dono Segreto, che fanno le due cose insieme, come
si legge in data/scripts/gift_aurora_ticket.inc dove a `giveitem ITEM_AURORA_TICKET` segue
immediatamente `setflag FLAG_ENABLE_SHIP_BIRTH_ISLAND`. Un oggetto inserito scrivendo sul
salvataggio ottiene quindi la prima metà della consegna e non la seconda, e il risultato in
gioco è esattamente quello osservato, cioè un biglietto che esiste e non apre nulla.

Questo strumento non scrive nulla: legge i flag pertinenti, li nomina, e riferisce quali voci
il menu del porto costruirebbe con lo stato attuale. La scrittura resta un'operazione separata.

Gli offset, e come sono stati verificati
-----------------------------------------
I flag di gioco stanno dentro SaveBlock1, che è la concatenazione delle sezioni con id da 1 a 4.

    // include/global.h, struct SaveBlock1
    /*0x1270*/ u8 flags[NUM_FLAG_BYTES];
    /*0x139C*/ u16 vars[VARS_COUNT];

Un flag di identificativo n sta quindi nel byte 0x1270 + n / 8, al bit n % 8. Gli identificativi
vengono da include/constants/flags.h, dove i flag di sistema si contano a partire da
SYSTEM_FLAGS, che vale 0x860 perché è TRAINER_FLAGS_END + 1.

La stessa aritmetica è confermata in modo indipendente da una seconda fonte, cioè il sorgente di
NDSEventTool.nds 1.0, che è l'homebrew con cui si iniettano gli eventi ufficiali da una scheda
di flash su Nintendo DS. In arm9/source/poke.cpp quel programma verifica che il Dono Segreto sia
abilitato leggendo `sav[0x40B + 0x1000 * sec[2]] & 0x8`, e verifica il Mistery Event leggendo
`sav[0x405 + 0x1000 * sec[2]] & 0x10`. Poiché la sezione con id 2 contiene i byte di SaveBlock1
da 3968 a 7935, il primo dei due indirizzi corrisponde a SaveBlock1 0x138B bit 3, che per
l'aritmetica qui sopra è il flag 0x8DB, cioè FLAG_SYS_MYSTERY_GIFT_ENABLE; il secondo corrisponde
a SaveBlock1 0x1385 bit 4, cioè il flag 0x8AC, FLAG_SYS_MYSTERY_EVENT_ENABLE. Le due fonti
coincidono senza che nessuna delle due sia stata usata per ricavare l'altra, ed è la ragione per
cui questi offset si possono usare su una cartuccia vera invece che su una copia di prova.

Uso
---
    python tools/emerald_event_flags_decode.py PERCORSO.sav
    python tools/emerald_event_flags_decode.py PERCORSO.sav --json out.json
"""

import argparse
import json
import struct
import sys

from emerald_bag_decode import (
    ITEM_SLOT_SIZE,
    SECTORS_PER_SLOT,
    SECTOR_SIZE,
    assemble,
    read_slot,
    u16,
    u32,
)

# Offset dentro SaveBlock1, da include/global.h di pret/pokeemerald.
OFF_FLAGS = 0x1270
OFF_VARS = 0x139C
OFF_EXTERNAL_EVENT_DATA = 0x31B3
LEN_EXTERNAL_EVENT_DATA = 0x14           # fino a externalEventFlags, che comincia a 0x31C7
OFF_EXTERNAL_EVENT_FLAGS = 0x31C7
LEN_EXTERNAL_EVENT_FLAGS = 0x15          # fino a roamer, che comincia a 0x31DC
OFF_MYSTERY_GIFT = 0x322C
LEN_MYSTERY_GIFT = 0x36C
OFF_RAM_SCRIPT = 0x3728
LEN_RAM_SCRIPT = 0x3EC
OFF_RECORD_MIXING_GIFT = 0x3B14
LEN_RECORD_MIXING_GIFT = 0x10

# Offset delle tasche che servono qui, dalla stessa struttura.
OFF_KEY_ITEMS = 0x5D8
N_KEY_ITEMS = 30

VARS_START = 0x4000

# Identificativi da include/constants/flags.h. I flag di sistema sono scritti come somma
# esplicita di SYSTEM_FLAGS, che vale 0x860, per rendere ispezionabile la derivazione.
SYSTEM_FLAGS = 0x860

FLAG_SYS_MYSTERY_EVENT_ENABLE = SYSTEM_FLAGS + 0x4C      # 0x8AC
FLAG_SYS_MYSTERY_GIFT_ENABLE = SYSTEM_FLAGS + 0x7B       # 0x8DB
FLAG_ENABLE_SHIP_SOUTHERN_ISLAND = SYSTEM_FLAGS + 0x53   # 0x8B3
FLAG_ENABLE_SHIP_BIRTH_ISLAND = SYSTEM_FLAGS + 0x75      # 0x8D5
FLAG_ENABLE_SHIP_FARAWAY_ISLAND = SYSTEM_FLAGS + 0x76    # 0x8D6
FLAG_ENABLE_SHIP_NAVEL_ROCK = SYSTEM_FLAGS + 0x80        # 0x8E0
FLAG_LANDMARK_SOUTHERN_ISLAND = SYSTEM_FLAGS + 0x49      # 0x8A9
FLAG_ARRIVED_ON_FARAWAY_ISLAND = SYSTEM_FLAGS + 0x78     # 0x8D8
FLAG_ARRIVED_AT_NAVEL_ROCK = SYSTEM_FLAGS + 0x81         # 0x8E1
FLAG_SYS_GAME_CLEAR = SYSTEM_FLAGS + 0x4                 # 0x864

VAR_DISTRIBUTE_EON_TICKET = 0x403F

# Identificativi degli oggetti, ricavati numerando l'enum di include/constants/items.h, che
# non porta valori espliciti. Coincidono con quelli gia' usati da emerald_bag_fix_round2.py
# per il Biglietto Aurora e la Mappa Stinta, che e' la verifica incrociata.
ITEM_EON_TICKET = 275
ITEM_MYSTIC_TICKET = 370
ITEM_AURORA_TICKET = 371
ITEM_OLD_SEA_MAP = 376

# Le quattro isole, ciascuna con l'oggetto che la sblocca, il flag che deve accompagnarlo, e
# il nome italiano della voce che comparirebbe al porto. L'ordine è quello in cui
# CreateLilycoveSSTidalMultichoice le valuta, così che l'elenco prodotto qui sia lo stesso
# elenco che il gioco mostrerebbe.
ISOLE = (
    ("Isola Remota", ITEM_EON_TICKET, "Biglietto Eone", FLAG_ENABLE_SHIP_SOUTHERN_ISLAND,
     "FLAG_ENABLE_SHIP_SOUTHERN_ISLAND", "Latias o Latios"),
    ("Monte Cordone", ITEM_MYSTIC_TICKET, "Biglietto Magico", FLAG_ENABLE_SHIP_NAVEL_ROCK,
     "FLAG_ENABLE_SHIP_NAVEL_ROCK", "Lugia e Ho-Oh"),
    ("Isola Materna", ITEM_AURORA_TICKET, "Biglietto Aurora", FLAG_ENABLE_SHIP_BIRTH_ISLAND,
     "FLAG_ENABLE_SHIP_BIRTH_ISLAND", "Deoxys"),
    ("Isola Suprema", ITEM_OLD_SEA_MAP, "Mappa Stinta", FLAG_ENABLE_SHIP_FARAWAY_ISLAND,
     "FLAG_ENABLE_SHIP_FARAWAY_ISLAND", "Mew"),
)

# I flag di contorno, che non decidono nulla da soli ma dicono se l'evento sia già stato vissuto.
FLAG_CONTORNO = (
    (FLAG_SYS_MYSTERY_GIFT_ENABLE, "FLAG_SYS_MYSTERY_GIFT_ENABLE",
     "il Dono Segreto compare nel menu iniziale"),
    (FLAG_SYS_MYSTERY_EVENT_ENABLE, "FLAG_SYS_MYSTERY_EVENT_ENABLE",
     "il Mistery Event e-Reader e' abilitato"),
    (FLAG_SYS_GAME_CLEAR, "FLAG_SYS_GAME_CLEAR", "Lega battuta, la nave S.S. Tidal esiste"),
    (FLAG_LANDMARK_SOUTHERN_ISLAND, "FLAG_LANDMARK_SOUTHERN_ISLAND",
     "l'Isola Remota compare sulla mappa"),
    (FLAG_ARRIVED_ON_FARAWAY_ISLAND, "FLAG_ARRIVED_ON_FARAWAY_ISLAND",
     "l'Isola Suprema e' gia' stata visitata"),
    (FLAG_ARRIVED_AT_NAVEL_ROCK, "FLAG_ARRIVED_AT_NAVEL_ROCK",
     "il Monte Cordone e' gia' stato visitato"),
    (0x13A, "FLAG_RECEIVED_AURORA_TICKET", "Biglietto Aurora ricevuto dal Dono Segreto"),
    (0x13B, "FLAG_RECEIVED_MYSTIC_TICKET", "Biglietto Magico ricevuto dal Dono Segreto"),
    (0x13C, "FLAG_RECEIVED_OLD_SEA_MAP", "Mappa Stinta ricevuta dal Dono Segreto"),
    (0x1AE, "FLAG_SHOWN_EON_TICKET", "Biglietto Eone gia' mostrato al marinaio"),
    (0x1AF, "FLAG_SHOWN_AURORA_TICKET", "Biglietto Aurora gia' mostrato al marinaio"),
    (0x1B0, "FLAG_SHOWN_OLD_SEA_MAP", "Mappa Stinta gia' mostrata al marinaio"),
    (0x1DB, "FLAG_SHOWN_MYSTIC_TICKET", "Biglietto Magico gia' mostrato al marinaio"),
    (0x1D0, "FLAG_MET_SCOTT_ON_SS_TIDAL", "Parco Lotta raggiungibile dal porto"),
    (0x1AC, "FLAG_DEFEATED_DEOXYS", "Deoxys battuto"),
    (0x1AD, "FLAG_BATTLED_DEOXYS", "Deoxys incontrato"),
    (0x1C7, "FLAG_DEFEATED_MEW", "Mew battuto"),
    (0x1CA, "FLAG_CAUGHT_MEW", "Mew catturato"),
    (0x2FC, "FLAG_HIDE_BIRTH_ISLAND_DEOXYS_TRIANGLE", "il triangolo dell'Isola Materna e' nascosto"),
    (0x38E, "FLAG_HIDE_SOUTHERN_ISLAND_EON_STONE", "la Sfera Eone dell'Isola Remota e' nascosta"),
)


def flag_get(sb1, flag_id):
    """Replica FlagGet: byte 0x1270 + n / 8 di SaveBlock1, bit n % 8."""
    return bool(sb1[OFF_FLAGS + (flag_id >> 3)] >> (flag_id & 7) & 1)


def var_get(sb1, var_id):
    """Replica VarGet per le variabili di salvataggio, cioè quelle da 0x4000 in su."""
    return u16(sb1, OFF_VARS + (var_id - VARS_START) * 2)


def key_items(sb1):
    """Gli identificativi presenti nella tasca Oggetti Chiave, che non è mascherata nel numero."""
    presenti = []
    for i in range(N_KEY_ITEMS):
        item_id = u16(sb1, OFF_KEY_ITEMS + i * ITEM_SLOT_SIZE)
        if item_id:
            presenti.append(item_id)
    return presenti


def area_stato(sb1, offset, length):
    """Riferisce se un'area sia tutta a zero e quanti byte non nulli contenga.

    Serve a distinguere un'area mai usata da una che contiene qualcosa, senza interpretare
    quel qualcosa: interpretare una struttura di cui non si è verificato il formato è
    precisamente il modo in cui si producono le affermazioni che questo progetto evita.
    """
    blocco = sb1[offset:offset + length]
    non_nulli = sum(1 for b in blocco if b)
    return {"offset": offset, "lunghezza": length, "byte_non_nulli": non_nulli,
            "tutta_a_zero": non_nulli == 0,
            "primi_16_byte": blocco[:16].hex()}


def analizza(blob):
    slot_scelto, slot_dati = None, None
    for idx in range(2):
        if len(blob) < (idx + 1) * SECTORS_PER_SLOT * SECTOR_SIZE:
            continue
        slot = read_slot(blob, idx)
        if not slot["sezioni"]:
            continue
        contatore = max(slot["contatori"]) if slot["contatori"] else -1
        if slot_scelto is None or contatore > slot_scelto:
            slot_scelto, slot_dati = contatore, slot
    if slot_dati is None:
        raise SystemExit("Nessuno slot valido: il file non sembra un salvataggio Gen 3.")

    _sb2, sb1 = assemble(slot_dati)
    if sb1 is None:
        raise SystemExit("SaveBlock1 incompleto: mancano sezioni fra la 1 e la 4.")

    presenti = set(key_items(sb1))

    isole = []
    for nome, item_id, nome_item, flag_id, flag_nome, premio in ISOLE:
        ha_item = item_id in presenti
        ha_flag = flag_get(sb1, flag_id)
        isole.append({
            "isola": nome,
            "oggetto": nome_item,
            "oggetto_id": item_id,
            "oggetto_nello_zaino": ha_item,
            "flag": flag_nome,
            "flag_id": flag_id,
            "flag_acceso": ha_flag,
            "voce_al_porto": ha_item and ha_flag,
            "premio": premio,
        })

    contorno = [{"flag": nome, "flag_id": fid, "acceso": flag_get(sb1, fid), "significato": desc}
                for fid, nome, desc in FLAG_CONTORNO]

    aree = {
        "mysteryGift": area_stato(sb1, OFF_MYSTERY_GIFT, LEN_MYSTERY_GIFT),
        "ramScript": area_stato(sb1, OFF_RAM_SCRIPT, LEN_RAM_SCRIPT),
        "recordMixingGift": area_stato(sb1, OFF_RECORD_MIXING_GIFT, LEN_RECORD_MIXING_GIFT),
        "externalEventData": area_stato(sb1, OFF_EXTERNAL_EVENT_DATA, LEN_EXTERNAL_EVENT_DATA),
        "externalEventFlags": area_stato(sb1, OFF_EXTERNAL_EVENT_FLAGS, LEN_EXTERNAL_EVENT_FLAGS),
    }

    return {
        "contatore_slot": slot_scelto,
        "sezioni_lette": sorted(slot_dati["sezioni"]),
        "sezioni_non_valide": slot_dati["non_valide"],
        "isole": isole,
        "flag_di_contorno": contorno,
        "var_distribute_eon_ticket": var_get(sb1, VAR_DISTRIBUTE_EON_TICKET),
        "aree": aree,
    }


def stampa(esito):
    print("Slot corrente: contatore %d, sezioni lette %s"
          % (esito["contatore_slot"], esito["sezioni_lette"]))
    if esito["sezioni_non_valide"]:
        print("Sezioni non valide: %s" % (esito["sezioni_non_valide"],))
    print()

    print("Le quattro isole, e che cosa serve a ciascuna")
    print("-" * 78)
    print("%-18s %-24s %-9s %-7s %s" % ("Isola", "Oggetto", "in zaino", "flag", "voce al porto"))
    for r in esito["isole"]:
        print("%-18s %-24s %-9s %-7s %s"
              % (r["isola"], r["oggetto"],
                 "si" if r["oggetto_nello_zaino"] else "NO",
                 "si" if r["flag_acceso"] else "NO",
                 "COMPARE" if r["voce_al_porto"] else "non compare"))
    print()

    voci = [r["isola"] for r in esito["isole"] if r["voce_al_porto"]]
    print("Menu che il porto di Alghepoli costruirebbe adesso: %s"
          % (", ".join(voci) if voci else "nessuna isola, solo Porto Selcepoli, Parco Lotta, Annulla"))
    print()

    print("Flag di contorno")
    print("-" * 78)
    for r in esito["flag_di_contorno"]:
        print("%-42s 0x%03X  %-3s %s"
              % (r["flag"], r["flag_id"], "si" if r["acceso"] else "no", r["significato"]))
    print()
    print("VAR_DISTRIBUTE_EON_TICKET (0x403F): %d" % esito["var_distribute_eon_ticket"])
    print()

    print("Aree di salvataggio legate alla distribuzione")
    print("-" * 78)
    for nome, a in esito["aree"].items():
        print("%-20s offset 0x%04X, %4d byte, %4d non nulli%s"
              % (nome, a["offset"], a["lunghezza"], a["byte_non_nulli"],
                 "  (tutta a zero)" if a["tutta_a_zero"] else ""))
        print("%-20s primi 16 byte: %s" % ("", a["primi_16_byte"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("save", help="percorso del file .sav da 128 KiB")
    ap.add_argument("--json", help="scrive l'esito completo anche in un file JSON")
    args = ap.parse_args()

    with open(args.save, "rb") as fh:
        blob = fh.read()

    esito = analizza(blob)
    stampa(esito)

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(esito, fh, indent=2, ensure_ascii=False)
        print()
        print("Scritto %s" % args.json)


if __name__ == "__main__":
    main()
