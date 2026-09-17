#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Applica al file di backup la correzione dell'inventario e del simbolo Pike confermate.

Perché esiste
-------------
La diagnosi (`emerald_bag_decode.py`) e la proposta di correzione sono in
`STUDIO-01-diagnosi-e-correzione-inventario.md` e `STUDIO-02-box-glitch-storici-e-frontiera.md`,
entrambe confermate dall'utente il 2026-09-17. Questo script esegue quella correzione sul file,
byte per byte, invece di farla a mano in PKHeX: è deterministico, ripetibile e verificabile con
un diff, mentre una sequenza di click non lo è. Riusa gli offset e l'algoritmo di checksum già
verificati da `emerald_bag_decode.py` (che a sua volta li verifica su `pret/pokeemerald`), non ne
introduce di nuovi.

Che cosa fa, in ordine
-----------------------
1. Legge il file, sceglie lo slot attivo con lo stesso criterio del contatore di `emerald_bag_decode.py`.
2. Nella tasca Oggetti Chiave: sostituisce le dodici voci-Palla spurie con le sette voci mancanti
   verificate sul sorgente (Merce Devon, Chiave Sotterranei, Sfera Rossa, Sfera Blu, Sacco Cenere,
   Tessera Gare, Vaso Polvere), tutte a quantità 1, mantenendo intatte le dodici legittime già presenti.
3. Nella tasca Palle: riporta la Master Ball a quantità 1 e rimuove le quattro Ultra Ball duplicate.
4. Nella tasca Oggetti: rimuove le dieci voci duplicate delle sei vitamine, mantenendo una voce
   sola per vitamina con la sua quantità reale.
5. Riempie i 16 posti liberi rimasti nella tasca Oggetti e tutti i 50 del deposito PC (che
   l'utente ha autorizzato a svuotare) con la collezione di 66 oggetti da tenuta e simili
   verificata in `STUDIO-01`, sezioni 10 e 12.
6. Rimuove dalla squadra Doduo e Paras (identificati per valore di personalità, non per
   nome), compatta gli slot rimasti e aggiorna il contatore della squadra.
7. Azzera il flag di sistema 2255 (`FLAG_SYS_PIKE_GOLD`) lasciando impostato il 2254
   (`FLAG_SYS_PIKE_SILVER`), senza toccare nessun altro bit dello stesso byte.
8. Ricalcola il checksum delle sole due sezioni toccate (quella dello zaino e quella dei flag),
   con lo stesso prefisso di parole già validato in lettura, e scrive il risultato in un file NUOVO:
   non sovrascrive mai il file di backup passato in ingresso.

Questo strumento non scrive mai sulla cartuccia: produce soltanto un nuovo file .sav locale.
La scrittura fisica resta un'operazione separata e manuale con FlashGBX, con il read-back
obbligatorio richiesto da .claude/rules/hardware-and-perimeter.md.

Uso
---
    python emerald_bag_fix.py INPUT.sav OUTPUT.sav
    python emerald_bag_fix.py INPUT.sav OUTPUT.sav --verifica-soltanto
"""

import argparse
import struct
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emerald_bag_decode import (  # noqa: E402
    u16, u32, checksum_prefix, validate_sector, read_slot, assemble, detect_game,
    decode_pockets, GAMES, ITEM_SLOT_SIZE, SECTOR_SIZE, SECTORS_PER_SLOT,
    SECTOR_DATA_SIZE, OFF_CHECKSUM,
)

# --- Il piano di correzione, confermato dall'utente il 2026-09-17 ---------------------

# Le dodici voci legittime già presenti nella tasca Oggetti Chiave, nell'ordine in cui
# risultavano nel dump originale (slot 0-11): non si toccano.
CHIAVE_ESISTENTI = 12

# Le sette voci da aggiungere, verificate sul sorgente (STUDIO-01, sezione 7): tutte
# permanenti (nessun `removeitem` nel sorgente) e ottenibili con gioco normale in Smeraldo.
CHIAVE_NUOVE = [269, 271, 276, 277, 270, 266, 372]

# Tasca Palle: lo slot 0 (Master Ball) va riportato a quantità 1; gli slot 12-15
# (quattro Ultra Ball duplicate) vanno azzerati. Gli slot 1-11 non si toccano.
PALLE_MASTER_SLOT = 0
PALLE_MASTER_QTY = 1
PALLE_DUPLICATI_DA_SLOT = 12  # tutto da qui in poi, nella tasca Palle, si azzera

# Tasca Oggetti: mappa da id vitamina a quale slot originale tenere come "quello vero".
# HP Up=63, Protein=64, Iron=65, Carbos=66, Calcium=67, Zinc=70 (src/data/items.h).
VITAMINE_SLOT_DA_TENERE = {63: 5, 66: 8, 70: 11, 65: 14, 67: 17, 64: 20}
VITAMINE_ID = set(VITAMINE_SLOT_DA_TENERE)
OGGETTI_SLOT_NON_VITAMINA_DA_TENERE = [0, 1, 2, 3, 4, 23, 24, 25]

# Simbolo Battle Pike: flag 2255 (FLAG_SYS_PIKE_GOLD) da azzerare, flag 2254
# (FLAG_SYS_PIKE_SILVER) da lasciare intatto. include/global.h: flags a SaveBlock1+0x1270;
# include/constants/flags.h: SYSTEM_FLAGS=0x860, PIKE_SILVER=+0x6E, PIKE_GOLD=+0x6F.
FLAG_GOLD_NUM = 0x860 + 0x6F
FLAG_OFFSET_SB1 = 0x1270 + (FLAG_GOLD_NUM // 8)
FLAG_BIT_MASK = 1 << (FLAG_GOLD_NUM % 8)
assert FLAG_GOLD_NUM == 2255 and FLAG_OFFSET_SB1 == 0x1389 and FLAG_BIT_MASK == 0x80

# La collezione di 66 oggetti da tenuta e simili, verificata su src/data/items.h (obtenibilità
# e permanenza) e sui nomi italiani ufficiali su wiki.pokemoncentral.it, "Elenco strumenti per
# numero d'indice (terza generazione)" (STUDIO-01, sezioni 10 e 12). Esclude di proposito gli
# id 179 (Polvefosca), 181 (Bretella) e 187 (Roccapietra), già presenti fra le voci non-vitamina
# mantenute nella tasca Oggetti (`OGGETTI_SLOT_NON_VITAMINA_DA_TENERE`): includerli anche qui
# li avrebbe duplicati. I primi 16 riempiono la tasca Oggetti fino a capienza 30 (14 già
# presenti dopo la correzione sopra), i restanti 50 vanno nel deposito PC, che l'utente ha
# autorizzato a svuotare perché non conteneva nulla fuori da questa stessa lista.
COLLEZIONE_66 = [
    180, 182, 183, 184, 185, 186, 188, 189, 194, 196, 198, 200, 203,
    205, 206, 208, 209, 213, 215, 219, 220, 221,
    190, 191, 192, 193, 195, 197, 199, 201, 202, 204, 207, 210, 211, 212, 214, 216,
    217, 218, 223, 224,
    93, 94, 97, 48, 49, 51, 103, 104, 106, 107, 108, 109, 45, 258, 73, 74, 75, 76, 77, 78, 79,
]
assert len(COLLEZIONE_66) == 63 and len(set(COLLEZIONE_66)) == 63

# I due esemplari in squadra da rimuovere (Doduo e Paras, allenatore AXEL, da uno scambio
# FireRed/Verde Foglia): identificati per PID, che nel formato di terza generazione sta in
# chiaro nei primi quattro byte di ogni esemplare, sia in squadra sia nei box.
SQUADRA_PID_DA_RIMUOVERE = {0x078F8A4C, 0x955DA089}
PARTY_COUNT_OFF = 0x234
PARTY_DATA_OFF = 0x238
PARTY_STRUCT_LEN = 100
PARTY_MAX = 6


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


def patch_pocket_bytes(sec1_data, offset_in_sb1, sec1_base_in_sb1, nuove_voci):
    """Scrive `nuove_voci` (lista di (id, raw_qty)) compattate da offset, azzera il resto
    della tasca. `sec1_data` è la sezione 1 come bytearray, `offset_in_sb1` l'offset della
    tasca dentro SaveBlock1, `sec1_base_in_sb1` è 0 perché la sezione 1 e' il primo pezzo
    di SaveBlock1 (le tasche di questo gioco stanno tutte dentro la sezione 1)."""
    rel = offset_in_sb1 - sec1_base_in_sb1
    for item_id, raw_qty in nuove_voci:
        struct.pack_into("<HH", sec1_data, rel, item_id, raw_qty)
        rel += ITEM_SLOT_SIZE
    return rel  # offset (relativo alla sezione) del primo slot ora vuoto


def zero_pocket_tail(sec1_data, start_rel, offset_in_sb1, count):
    end_rel = (offset_in_sb1 - 0) + count * ITEM_SLOT_SIZE
    for rel in range(start_rel, end_rel, ITEM_SLOT_SIZE):
        struct.pack_into("<HH", sec1_data, rel, 0, 0)


def ricalcola_checksum(sector_full, lunghezza):
    nuovo = checksum_prefix(sector_full, lunghezza // 4)
    struct.pack_into("<H", sector_full, OFF_CHECKSUM, nuovo)
    return nuovo


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("input", help="file di backup verificato, in sola lettura")
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

    key = u32(sb2, game["chiave_offset"])
    key16 = key & 0xFFFF
    tasche = {nome_t: (off, cnt) for nome_t, off, cnt, _m, _cap in game["tasche"]}
    off_chiave, cnt_chiave = tasche["Oggetti chiave"]
    off_palle, cnt_palle = tasche["Poke Ball"]
    off_oggetti, cnt_oggetti = tasche["Oggetti"]
    off_pc, cnt_pc = tasche["Deposito PC"]

    sec1_pos = slot["sezioni"][1]["posizione"]
    sec2_pos = slot["sezioni"][2]["posizione"]
    base = slot_index * SECTORS_PER_SLOT * SECTOR_SIZE
    sec1_off_file = base + sec1_pos * SECTOR_SIZE
    sec2_off_file = base + sec2_pos * SECTOR_SIZE
    sec1_len = slot["sezioni"][1]["lunghezza_checksum"]
    sec2_len = slot["sezioni"][2]["lunghezza_checksum"]

    sec1_full = bytearray(blob[sec1_off_file:sec1_off_file + SECTOR_SIZE])
    sec1_data = sec1_full  # i primi SECTOR_DATA_SIZE byte sono i dati; il resto è il piede

    # --- Oggetti Chiave: leggi le 12 legittime, scrivi 12+7, azzera il resto -----------
    esistenti = []
    for i in range(CHIAVE_ESISTENTI):
        rel = off_chiave + i * ITEM_SLOT_SIZE
        esistenti.append((u16(sec1_data, rel), u16(sec1_data, rel + 2)))
    nuove = [(item_id, (1 ^ key16) & 0xFFFF) for item_id in CHIAVE_NUOVE]
    primo_vuoto = patch_pocket_bytes(sec1_data, off_chiave, 0, esistenti + nuove)
    zero_pocket_tail(sec1_data, primo_vuoto, off_chiave, cnt_chiave)

    # --- Palle: correggi lo slot 0, azzera gli slot 12-15 ------------------------------
    struct.pack_into("<HH", sec1_data, off_palle + PALLE_MASTER_SLOT * ITEM_SLOT_SIZE,
                      1, (PALLE_MASTER_QTY ^ key16) & 0xFFFF)
    zero_pocket_tail(sec1_data, off_palle + PALLE_DUPLICATI_DA_SLOT * ITEM_SLOT_SIZE,
                      off_palle, cnt_palle)

    # --- Oggetti: ricompatta, una voce per vitamina più le voci non-vitamina -----------
    tenute = []
    for i in OGGETTI_SLOT_NON_VITAMINA_DA_TENERE:
        rel = off_oggetti + i * ITEM_SLOT_SIZE
        item_id = u16(sec1_data, rel)
        tenute.append((i, item_id, u16(sec1_data, rel + 2)))
    for item_id, slot_i in VITAMINE_SLOT_DA_TENERE.items():
        rel = off_oggetti + slot_i * ITEM_SLOT_SIZE
        letto_id = u16(sec1_data, rel)
        if letto_id != item_id:
            raise SystemExit("atteso id %d allo slot %d della tasca Oggetti, trovato %d: "
                              "il layout del dump non è quello previsto, mi fermo"
                              % (item_id, slot_i, letto_id))
        tenute.append((slot_i, item_id, u16(sec1_data, rel + 2)))
    tenute.sort(key=lambda t: t[0])
    voci_oggetti = [(item_id, raw_qty) for _orig_slot, item_id, raw_qty in tenute]

    # --- La collezione: prime 16 nella tasca Oggetti (fino a capienza 30), il resto nel
    # deposito PC (che non maschera le quantità: la quantità grezza è quella vera). --------
    posti_oggetti_liberi = cnt_oggetti - len(voci_oggetti)
    collezione_oggetti = COLLEZIONE_66[:posti_oggetti_liberi]
    collezione_pc = COLLEZIONE_66[posti_oggetti_liberi:]
    voci_oggetti += [(item_id, (1 ^ key16) & 0xFFFF) for item_id in collezione_oggetti]

    primo_vuoto_o = patch_pocket_bytes(sec1_data, off_oggetti, 0, voci_oggetti)
    zero_pocket_tail(sec1_data, primo_vuoto_o, off_oggetti, cnt_oggetti)

    if len(collezione_pc) > cnt_pc:
        raise SystemExit("la collezione non entra nel deposito PC: %d voci per %d posti"
                          % (len(collezione_pc), cnt_pc))
    voci_pc = [(item_id, 1) for item_id in collezione_pc]
    primo_vuoto_pc = patch_pocket_bytes(sec1_data, off_pc, 0, voci_pc)
    zero_pocket_tail(sec1_data, primo_vuoto_pc, off_pc, cnt_pc)

    # --- Squadra: rimuovi Doduo e Paras per PID, compatta, aggiorna il contatore ---------
    party_count = sec1_data[PARTY_COUNT_OFF]
    party_slots = []
    for i in range(party_count):
        off = PARTY_DATA_OFF + i * PARTY_STRUCT_LEN
        pid = u32(sec1_data, off)
        party_slots.append((pid, bytes(sec1_data[off:off + PARTY_STRUCT_LEN])))
    superstiti = [(pid, dati) for pid, dati in party_slots if pid not in SQUADRA_PID_DA_RIMUOVERE]
    rimossi = len(party_slots) - len(superstiti)
    for i in range(PARTY_MAX):
        off = PARTY_DATA_OFF + i * PARTY_STRUCT_LEN
        if i < len(superstiti):
            sec1_data[off:off + PARTY_STRUCT_LEN] = superstiti[i][1]
        else:
            sec1_data[off:off + PARTY_STRUCT_LEN] = bytes(PARTY_STRUCT_LEN)
    sec1_data[PARTY_COUNT_OFF] = len(superstiti)

    vecchio_cs1 = u16(sec1_full, OFF_CHECKSUM)
    nuovo_cs1 = ricalcola_checksum(sec1_full, sec1_len)

    # --- Flag della Battle Pike, dentro la sezione 2 -----------------------------------
    sec2_full = bytearray(blob[sec2_off_file:sec2_off_file + SECTOR_SIZE])
    rel_flag = FLAG_OFFSET_SB1 - SECTOR_DATA_SIZE  # SaveBlock1 = sezioni 1..4 concatenate
    prima = sec2_full[rel_flag]
    sec2_full[rel_flag] = prima & (~FLAG_BIT_MASK & 0xFF)
    vecchio_cs2 = u16(sec2_full, OFF_CHECKSUM)
    nuovo_cs2 = ricalcola_checksum(sec2_full, sec2_len)

    print("Slot scelto: %d, chiave 0x%08X" % (slot_index, key))
    print("Oggetti Chiave: %d voci esistenti mantenute, %d nuove aggiunte, resto azzerato"
          % (len(esistenti), len(nuove)))
    print("Palle: Master Ball riportata a quantità 1, 4 duplicati azzerati")
    print("Oggetti: %d voci base + %d dalla collezione = %d totali (capienza %d)"
          % (len(voci_oggetti) - len(collezione_oggetti), len(collezione_oggetti),
             len(voci_oggetti), cnt_oggetti))
    print("Deposito PC: svuotato e ripopolato con %d voci della collezione (capienza %d)"
          % (len(voci_pc), cnt_pc))
    print("Squadra: %d esemplari rimossi per PID, da %d a %d rimasti"
          % (rimossi, len(party_slots), len(superstiti)))
    print("Flag Battle Pike: byte 0x%02X -> 0x%02X (bit oro azzerato, resto intatto)"
          % (prima, sec2_full[rel_flag]))
    print("Checksum sezione 1: 0x%04X -> 0x%04X" % (vecchio_cs1, nuovo_cs1))
    print("Checksum sezione 2: 0x%04X -> 0x%04X" % (vecchio_cs2, nuovo_cs2))

    if args.verifica_soltanto:
        print("\n--verifica-soltanto: nessun file scritto")
        return 0

    blob[sec1_off_file:sec1_off_file + SECTOR_SIZE] = sec1_full
    blob[sec2_off_file:sec2_off_file + SECTOR_SIZE] = sec2_full
    with open(args.output, "wb") as fh:
        fh.write(blob)
    print("\nScritto: %s" % args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
