#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Terzo giro di correzione: accende i tre flag di abilitazione delle isole.

Perché esiste
-------------
Il secondo giro (`emerald_bag_fix_round2.py`) ha messo nella tasca Oggetti Chiave il
Biglietto Aurora e la Mappa Stinta, e il Biglietto Eone c'era già dal dump
originale. Nessuno dei tre apre alcuna destinazione al porto di Alghepoli, perché il gioco
non guarda soltanto lo zaino.

    // pret/pokeemerald, src/script_menu.c, CreateLilycoveSSTidalMultichoice
    if (CheckBagHasItem(ITEM_EON_TICKET, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_SOUTHERN_ISLAND) == TRUE)
    if (CheckBagHasItem(ITEM_AURORA_TICKET, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_BIRTH_ISLAND) == TRUE)
    if (CheckBagHasItem(ITEM_OLD_SEA_MAP, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_FARAWAY_ISLAND) == TRUE)

La condizione è una congiunzione, e il secondo termine lo accende soltanto lo script di
consegna del Dono Segreto, che esegue `giveitem` e `setflag` nello stesso punto. Un oggetto
scritto nella tasca da fuori ottiene quindi la prima metà della consegna e non la seconda.
La diagnosi completa, con la misura sui quattro salvataggi conservati e le tre vie fra cui
l'utente ha scelto questa, è in `STUDIO-03-doni-segreti-e-flag-delle-isole.md`.

Che cosa fa, e che cosa deliberatamente non fa
-----------------------------------------------
Accende tre bit in due byte della sezione 2 e ricalcola il checksum di quella sola sezione.
Nient'altro. In particolare non tocca i flag `FLAG_RECEIVED_*`, che il gioco usa per sapere
se un dono sia già stato consegnato dal Dono Segreto e che su questa partita sono spenti
perché quella consegna non è mai avvenuta: accenderli dichiarerebbe un fatto falso e non
servirebbe a nulla, perché il menu del porto non li guarda. Non tocca nemmeno i flag
`FLAG_SHOWN_*`, che il gioco accende da sé la prima volta che il biglietto viene mostrato al
marinaio. Fino al terzo giro non toccava nemmeno `FLAG_ENABLE_SHIP_NAVEL_ROCK`, perche' il
Biglietto Magico non era nello zaino e accendere un flag senza il suo oggetto avrebbe
ricostruito la stessa coppia rotta al contrario; dal 2026-09-18 a sera, con ADR-066, quel
biglietto viene messo in tasca da `emerald_key_item_add.py` e la quarta riga del piano e'
quindi attiva. L'ordine di esecuzione conta: prima l'oggetto, poi il flag.

I tre flag e la loro aritmetica, verificati su pret/pokeemerald
---------------------------------------------------------------
I flag stanno in `SaveBlock1.flags`, che `include/global.h` colloca a 0x1270, un bit per
flag; il flag n sta nel byte 0x1270 + n / 8 al bit n % 8. Gli identificativi vengono da
`include/constants/flags.h`, dove i flag di sistema partono da `SYSTEM_FLAGS`, che vale
0x860 perché è `TRAINER_FLAGS_END + 1`. Poiché la sezione con identificativo 2 contiene i
byte di SaveBlock1 da 3968 a 7935, i tre flag cadono tutti dentro quella sola sezione.

    FLAG_ENABLE_SHIP_SOUTHERN_ISLAND = 0x8B3 -> SaveBlock1 0x1386, bit 3 -> sezione 2, offset 0x406
    FLAG_ENABLE_SHIP_BIRTH_ISLAND    = 0x8D5 -> SaveBlock1 0x138A, bit 5 -> sezione 2, offset 0x40A
    FLAG_ENABLE_SHIP_FARAWAY_ISLAND  = 0x8D6 -> SaveBlock1 0x138A, bit 6 -> sezione 2, offset 0x40A

La stessa aritmetica è confermata in modo indipendente dal sorgente di NDSEventTool.nds 1.0,
che in `arm9/source/poke.cpp` legge il flag del Dono Segreto a `sav[0x40B + 0x1000 * sec[2]]`
bit 3: tradotto, è SaveBlock1 0x138B bit 3, cioè il flag 0x8DB, `FLAG_SYS_MYSTERY_GIFT_ENABLE`.
Due fonti che non si sono usate a vicenda concordano, ed è la ragione per cui questi offset
si possono usare su una cartuccia vera.

Questo strumento non scrive mai sulla cartuccia: produce soltanto un nuovo file .sav locale,
e non sovrascrive mai il file passato in ingresso. La scrittura fisica resta un'operazione
separata e manuale con FlashGBX, con il read-back obbligatorio richiesto da
`.claude/rules/hardware-and-perimeter.md`.

Uso
---
    python emerald_event_flags_fix.py INGRESSO.sav USCITA.sav
    python emerald_event_flags_fix.py INGRESSO.sav USCITA.sav --verifica-soltanto
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
    OFF_FLAGS, ITEM_EON_TICKET, ITEM_AURORA_TICKET, ITEM_OLD_SEA_MAP, ITEM_MYSTIC_TICKET,
    FLAG_ENABLE_SHIP_SOUTHERN_ISLAND, FLAG_ENABLE_SHIP_BIRTH_ISLAND,
    FLAG_ENABLE_SHIP_FARAWAY_ISLAND, FLAG_ENABLE_SHIP_NAVEL_ROCK,
)

SECTOR_DATA_SIZE = 3968

# Il piano del terzo giro, deciso dall'utente il 2026-09-18. Ogni riga lega un flag
# all'oggetto senza il quale accenderlo non avrebbe senso: la precondizione è verificata
# prima di scrivere, e se un oggetto manca lo strumento si ferma invece di procedere.
PIANO = (
    ("Isola Remota", FLAG_ENABLE_SHIP_SOUTHERN_ISLAND, "FLAG_ENABLE_SHIP_SOUTHERN_ISLAND",
     ITEM_EON_TICKET, "Biglietto Eone"),
    ("Isola Materna", FLAG_ENABLE_SHIP_BIRTH_ISLAND, "FLAG_ENABLE_SHIP_BIRTH_ISLAND",
     ITEM_AURORA_TICKET, "Biglietto Aurora"),
    ("Isola Suprema", FLAG_ENABLE_SHIP_FARAWAY_ISLAND, "FLAG_ENABLE_SHIP_FARAWAY_ISLAND",
     ITEM_OLD_SEA_MAP, "Mappa Stinta"),
    # Quarta riga aggiunta il 2026-09-18 a sera con ADR-066. Al terzo giro non c'era perche'
    # il Biglietto Magico non era nella tasca e la precondizione lo avrebbe fermato; adesso
    # ve lo mette `emerald_key_item_add.py`, che va eseguito prima di questo strumento.
    ("Monte Cordone", FLAG_ENABLE_SHIP_NAVEL_ROCK, "FLAG_ENABLE_SHIP_NAVEL_ROCK",
     ITEM_MYSTIC_TICKET, "Biglietto Magico"),
)


def scegli_slot(blob):
    """Lo slot più recente fra i due, fra quelli che hanno una sezione 0 valida."""
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
    ap.add_argument("--verifica-soltanto", action="store_true",
                    help="calcola e riferisce le modifiche senza scrivere il file di output")
    args = ap.parse_args()

    if os.path.abspath(args.input) == os.path.abspath(args.output):
        raise SystemExit("l'output non può essere uguale all'input: si rischierebbe di "
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
        raise SystemExit("il file non è identificato come Smeraldo con margine sufficiente "
                         "(punteggio %d su %s): questo script corregge solo Smeraldo"
                         % (punti, nome))

    presenti = oggetti_chiave(sb1, game)

    # Precondizione: nessun flag si accende se il suo oggetto non è in tasca. È la
    # simmetrica della coppia rotta che questo giro esiste per riparare, e ometterla
    # permetterebbe di produrne una nuova nell'altro verso.
    mancanti = [(isola, nome_it) for isola, _f, _fn, item, nome_it in PIANO
                if item not in presenti]
    if mancanti:
        raise SystemExit("oggetti non presenti nella tasca Oggetti Chiave, nessun flag acceso: "
                         + ", ".join("%s (%s)" % (n, i) for i, n in mancanti))

    # Raggruppa i flag per sezione: su questa partita cadono tutti nella sezione 2, ma il
    # raggruppamento non lo assume, così che lo strumento resti corretto se un giorno il
    # piano includesse un flag che cade altrove.
    per_sezione = {}
    righe = []
    for isola, flag_id, flag_nome, _item, nome_it in PIANO:
        sec_id, off_sec, mask = posizione_flag(flag_id)
        per_sezione.setdefault(sec_id, []).append((off_sec, mask))
        righe.append((isola, flag_nome, flag_id, nome_it, sec_id, off_sec, mask))

    for sec_id in per_sezione:
        if sec_id not in slot["sezioni"]:
            raise SystemExit("la sezione %d non è presente nello slot scelto" % sec_id)

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
            settore[off_sec] |= mask

        vecchio_cs = u16(settore, OFF_CHECKSUM)
        nuovo_cs = ricalcola_checksum(settore, lunghezza)
        settori[sec_id] = (off_file, settore)
        modifiche.append((sec_id, pos, byte_prima,
                          {o: settore[o] for o in byte_prima}, vecchio_cs, nuovo_cs))

    print("Slot scelto: %d, chiave 0x%08X" % (slot_index, u32(sb2, game["chiave_offset"])))
    print()
    print("%-16s %-34s %-22s %-9s %s" % ("Isola", "Flag", "Oggetto", "gia' acceso", "dove"))
    for isola, flag_nome, flag_id, nome_it, sec_id, off_sec, mask in righe:
        gia = bool(sb1[OFF_FLAGS + (flag_id >> 3)] & mask)
        print("%-16s %-34s %-22s %-11s sez.%d +0x%03X bit %d"
              % (isola, flag_nome, nome_it, "si" if gia else "no",
                 sec_id, off_sec, mask.bit_length() - 1))
    print()
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
