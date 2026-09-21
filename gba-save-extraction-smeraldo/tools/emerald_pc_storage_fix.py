#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sesto giro: rivede la collezione del deposito PC, dentro la capienza di 50 slot.

Perche' esiste
--------------
Il primo giro (`emerald_bag_fix.py`) aveva riempito il deposito PC con una collezione
di 47 oggetti rari verificati su `src/data/items.h` e su `wiki.pokemoncentral.it`
(STUDIO-01, sezioni 10-12). Il 2026-09-21 l'utente ha chiesto una revisione: fuori i
sette oggetti da battaglia comuni (acquistabili in qualunque negozio), fuori due
oggetti collezionabili ma meno prioritari (Polvostella, Pezzo Stella), dentro dodici
oggetti rari non acquistabili in nessun negozio di Smeraldo (verificato assente da
ogni lista "Mart" sotto `data/maps`), scelti da un censimento sul sorgente degli
oggetti tenuti dalle 143 specie selvatiche di Smeraldo incrociato con la lista
esplicita dell'utente. Il conto e' esatto: 47 - 9 + 12 = 50, la capienza del deposito.

La tasca Bacche non e' toccata: il censimento ha trovato che le sette bacche candidate
(Chesto, Leppa, Oran, Pecha, Persim, Rawst, Sitrus) sono TUTTE gia' presenti, perche'
quella tasca ha gia' le 43 bacche del gioco al completo (verificato con
`emerald_bag_decode.py`, 43/46 slot occupati). Nessuna scrittura serve la' sopra.

Uso
---
    python emerald_pc_storage_fix.py INGRESSO.sav USCITA.sav
    python emerald_pc_storage_fix.py INGRESSO.sav USCITA.sav --verifica-soltanto
"""

import argparse
import struct
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emerald_bag_decode import (  # noqa: E402
    u16, checksum_prefix, read_slot, assemble, detect_game,
    GAMES, ITEM_SLOT_SIZE, SECTOR_SIZE, SECTORS_PER_SLOT, OFF_CHECKSUM,
)

# --- Il piano del sesto giro, deciso dall'utente il 2026-09-21 -------------------------

PC_DA_RIMUOVERE = {
    73: "Superguardia", 74: "Supercolpo", 75: "Attacco X", 76: "Difesa X",
    77: "Velocita X", 78: "Precisione X", 79: "Special X",
    108: "Polvostella", 109: "Pezzo Stella",
}

# Quantita' decise dall'utente il 2026-09-21: 99 (il tetto del gioco, MAX_BAG_ITEM_CAPACITY)
# per i due consumabili, che si usano e si esauriscono; 5 per tutti gli altri, che sono
# oggetti da tenuta o strumenti permanenti e restano nello zaino finche' non li si assegna.
PC_DA_AGGIUNGERE = [
    (68, "Caram. Rara", 99), (71, "PP-Max", 99),
    (222, "Fortunpugno", 5), (225, "Gambo", 5),
    (39, "Flauto Blu", 5), (40, "Flauto Gial.", 5), (41, "Flauto Rosso", 5),
    (42, "Flauto Nero", 5), (43, "Flauto Bianco", 5),
    (187, "Roccia di Re", 5), (29, "Latte Mumu", 5), (50, "Coccio Giallo", 5),
]


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
    ap.add_argument("input", help="dump aggiornato e verificato, in sola lettura")
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
                          "(punteggio %d su %s): questo script corregge solo Smeraldo" % (punti, nome))

    tasche = {nome_t: (off, cnt) for nome_t, off, cnt, _m, _cap in game["tasche"]}
    off_pc, cnt_pc = tasche["Deposito PC"]

    sec1_pos = slot["sezioni"][1]["posizione"]
    base = slot_index * SECTORS_PER_SLOT * SECTOR_SIZE
    sec1_off_file = base + sec1_pos * SECTOR_SIZE
    sec1_len = slot["sezioni"][1]["lunghezza_checksum"]
    sec1_full = bytearray(blob[sec1_off_file:sec1_off_file + SECTOR_SIZE])

    esistenti = []
    for i in range(cnt_pc):
        rel = off_pc + i * ITEM_SLOT_SIZE
        item_id = u16(sec1_full, rel)
        if item_id == 0:
            break
        esistenti.append((item_id, u16(sec1_full, rel + 2)))

    prima = len(esistenti)
    rimosse = [t for t in esistenti if t[0] in PC_DA_RIMUOVERE]
    rimaste = [t for t in esistenti if t[0] not in PC_DA_RIMUOVERE]
    if len(rimosse) != len(PC_DA_RIMUOVERE):
        trovati = {t[0] for t in rimosse}
        mancanti = set(PC_DA_RIMUOVERE) - trovati
        raise SystemExit("attesi nel deposito PC gli id %s da rimuovere, non trovati: %s"
                          % (sorted(PC_DA_RIMUOVERE), sorted(mancanti)))

    id_gia_presenti = {t[0] for t in rimaste}
    duplicati = [item_id for item_id, _nome, _qty in PC_DA_AGGIUNGERE if item_id in id_gia_presenti]
    if duplicati:
        raise SystemExit("gli id %s da aggiungere sono già nel deposito PC: "
                          "aggiungerli di nuovo li duplicherebbe" % sorted(duplicati))

    nuove = [(item_id, qty) for item_id, _nome, qty in PC_DA_AGGIUNGERE]
    voci_finali = rimaste + nuove
    if len(voci_finali) != cnt_pc:
        raise SystemExit("il deposito PC avrebbe %d voci per %d slot: non è la capienza esatta "
                          "prevista, verificare il piano prima di scrivere" % (len(voci_finali), cnt_pc))

    rel = off_pc
    for item_id, raw_qty in voci_finali:
        struct.pack_into("<HH", sec1_full, rel, item_id, raw_qty)
        rel += ITEM_SLOT_SIZE

    vecchio_cs = u16(sec1_full, OFF_CHECKSUM)
    nuovo_cs = ricalcola_checksum(sec1_full, sec1_len)

    print("Slot scelto: %d" % slot_index)
    print("Deposito PC: %d voci prima, rimosse %d (%s), aggiunte %d (%s), %d dopo (capienza %d)"
          % (prima, len(rimosse), sorted(t[0] for t in rimosse),
             len(nuove), [(i, q) for i, _n, q in PC_DA_AGGIUNGERE],
             len(voci_finali), cnt_pc))
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
