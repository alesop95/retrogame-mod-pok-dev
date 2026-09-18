#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aggiunge uno o più oggetti alla tasca Oggetti Chiave di un salvataggio di Smeraldo.

Perché esiste
-------------
Il secondo giro di correzione (`emerald_bag_fix_round2.py`) sapeva aggiungere oggetti chiave,
ma dentro un piano fisso che faceva anche altro: rimuoveva tre oggetti, cancellava due
esemplari dalla squadra e azzerava un record della Frontiera. Riusarlo per la sola aggiunta
di un oggetto non era possibile senza eseguirne anche il resto. Questo strumento fa la sola
aggiunta, prende gli identificativi da riga di comando e non tocca nient'altro.

La quantità si scrive mascherata, come il gioco si aspetta
-----------------------------------------------------------
In Smeraldo le quantità degli oggetti nello zaino non stanno in chiaro: sono in XOR con i
sedici bit bassi della chiave di sicurezza a 32 bit che sta in SaveBlock2. `GetBagItemQuantity`
in `src/item.c` di pret/pokeemerald applica la maschera in lettura, quindi scrivere una
quantità in chiaro produrrebbe un numero assurdo in gioco. Questo strumento scrive
`1 XOR chiave16`, che è la stessa formula già usata e verificata nel secondo giro.

Precondizioni e rifiuti
-----------------------
Rifiuta se l'oggetto è già presente, perché duplicare un oggetto chiave non ha senso e
sarebbe la firma di un errore. Rifiuta se la tasca non ha posto. Rifiuta se il file non è
identificato come Smeraldo con margine sufficiente. E non sovrascrive mai il file in ingresso.

Questo strumento non scrive mai sulla cartuccia: produce soltanto un nuovo file .sav locale.
La scrittura fisica resta un'operazione separata e manuale con FlashGBX, con il read-back
obbligatorio richiesto da `.claude/rules/hardware-and-perimeter.md`.

Uso
---
    python emerald_key_item_add.py INGRESSO.sav USCITA.sav --item 370
    python emerald_key_item_add.py INGRESSO.sav USCITA.sav --item 370 --verifica-soltanto
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

# Nomi noti, soltanto per rendere leggibile il resoconto. Un identificativo non elencato
# qui si scrive comunque: lo strumento non tiene una lista chiusa di oggetti ammessi.
NOMI = {
    275: "Biglietto Eone",
    370: "Biglietto Magico",
    371: "Biglietto Aurora",
    376: "Mappa Stinta",
}


def scegli_slot(blob):
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


def ricalcola_checksum(sector_full, lunghezza):
    nuovo = checksum_prefix(sector_full, lunghezza // 4)
    struct.pack_into("<H", sector_full, OFF_CHECKSUM, nuovo)
    return nuovo


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("input", help="dump verificato della cartuccia, in sola lettura")
    ap.add_argument("output", help="percorso del nuovo file corretto (mai uguale all'input)")
    ap.add_argument("--item", type=int, action="append", required=True,
                    metavar="ID", help="identificativo dell'oggetto da aggiungere, ripetibile")
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

    key = u32(sb2, game["chiave_offset"])
    key16 = key & 0xFFFF
    tasche = {n: (off, cnt) for n, off, cnt, _m, _cap in game["tasche"]}
    off_chiave, cnt_chiave = tasche["Oggetti chiave"]

    sec1_pos = slot["sezioni"][1]["posizione"]
    sec1_len = slot["sezioni"][1]["lunghezza_checksum"]
    base = slot_index * SECTORS_PER_SLOT * SECTOR_SIZE
    sec1_off_file = base + sec1_pos * SECTOR_SIZE
    sec1_full = bytearray(blob[sec1_off_file:sec1_off_file + SECTOR_SIZE])

    esistenti = []
    for i in range(cnt_chiave):
        rel = off_chiave + i * ITEM_SLOT_SIZE
        item_id = u16(sec1_full, rel)
        if item_id == 0:
            break
        esistenti.append(item_id)

    gia = [i for i in args.item if i in esistenti]
    if gia:
        raise SystemExit("gia' presenti nella tasca Oggetti Chiave, nessuna scrittura: %s"
                         % ", ".join("%d (%s)" % (i, NOMI.get(i, "sconosciuto")) for i in gia))

    if len(esistenti) + len(args.item) > cnt_chiave:
        raise SystemExit("la tasca Oggetti Chiave non ha posto: %d voci per %d slot"
                         % (len(esistenti) + len(args.item), cnt_chiave))

    print("Slot scelto: %d, chiave 0x%08X" % (slot_index, key))
    print("Tasca Oggetti Chiave: %d voci su %d slot prima, %d dopo"
          % (len(esistenti), cnt_chiave, len(esistenti) + len(args.item)))
    print()

    rel = off_chiave + len(esistenti) * ITEM_SLOT_SIZE
    for item_id in args.item:
        raw_qty = (1 ^ key16) & 0xFFFF
        struct.pack_into("<HH", sec1_full, rel, item_id, raw_qty)
        print("Aggiunto id %d (%s) allo slot %d, sezione 1 offset 0x%03X, "
              "quantita' 1 scritta mascherata come 0x%04X"
              % (item_id, NOMI.get(item_id, "sconosciuto"),
                 (rel - off_chiave) // ITEM_SLOT_SIZE, rel, raw_qty))
        rel += ITEM_SLOT_SIZE

    vecchio_cs = u16(sec1_full, OFF_CHECKSUM)
    nuovo_cs = ricalcola_checksum(sec1_full, sec1_len)
    print("Checksum sezione 1: 0x%04X -> 0x%04X" % (vecchio_cs, nuovo_cs))

    if args.verifica_soltanto:
        print("\n--verifica-soltanto: nessun file scritto")
        return 0

    blob[sec1_off_file:sec1_off_file + SECTOR_SIZE] = sec1_full
    with open(args.output, "wb") as fh:
        fh.write(blob)
    print("\nScritto: %s" % args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
