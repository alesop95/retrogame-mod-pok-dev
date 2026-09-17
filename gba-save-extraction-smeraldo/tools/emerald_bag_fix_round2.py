#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Secondo giro di correzione: sfere, Merce Devon, due biglietti, squadra, record Pike.

Perché esiste
-------------
Il primo giro (`emerald_bag_fix.py`) è stato scritto sulla cartuccia vera il 2026-09-17 e
verificato byte per byte. Fra quella scrittura e questo secondo giro l'utente ha continuato
a giocare (un salvataggio nuovo al Parco Lotta), quindi questo script opera su un dump
nuovo (`round2.sav`), mai sul file già scritto in precedenza, come impone
`.claude/rules/hardware-and-perimeter.md`. Il piano è confermato dall'utente nella stessa
giornata ed è scritto per intero in `STUDIO-01`, sezioni 15-17, e in ADR-063.

Che cosa fa, in ordine
-----------------------
1. Nella tasca Oggetti Chiave: rimuove Merce Devon (269, consegnata a Stern molto prima
   della Frontiera di Lotta, verificato su `data/event_scripts.s` di pret/pokeemerald che
   la consegna esegue `removeitem`), Sfera Rossa (276) e Sfera Blu (277, mai ottenibili in
   Smeraldo per gioco normale, verificato su Bulbapedia alla voce Monte Pyre). Aggiunge
   Biglietto Aurora (371) e Vecchia Mappa Marina (376): l'utente ha confermato di non
   averli mai ottenuti per davvero, quindi sono contenuto prodotto su sua richiesta
   esplicita e non una restituzione di corruzione, per ADR-063.
2. Nella squadra: rimuove il secondo Doduo e il secondo Paras rimasti dal primo giro
   (identificati per valore di personalità, stesso metodo del primo giro), lasciando
   Linoone e Nidoran maschio, gli unici due esemplari senza il sospetto allenatore
   `C6B4D7EF` in comune con tutti e quattro gli individui trovati nella squadra originale.
3. Azzera il record di serie di vittorie della Battle Pike in entrambe le modalità di
   livello (Lv.50 e Libero), offset SaveBlock2+0xE08, verificato su include/global.h di
   pret/pokeemerald (`pikeRecordStreaks[FRONTIER_LVL_MODE_COUNT]`, struct BattleFrontier
   incorporata in SaveBlock2 a 0x64C, quindi i commenti di offset nella struct sono già
   assoluti dentro SaveBlock2). Non tocca il flag dei simboli, già corretto nel primo
   giro, né il totale storico delle sfide vinte, che non implica alcun livello di simbolo.
4. Ricalcola il checksum delle sezioni toccate (la sezione 1, per zaino e squadra, e la
   sezione 0, per il record della Pike) e scrive il risultato in un file NUOVO: non
   sovrascrive mai il file di backup passato in ingresso.

Questo strumento non scrive mai sulla cartuccia: produce soltanto un nuovo file .sav
locale. La scrittura fisica resta un'operazione separata e manuale con FlashGBX, con il
read-back obbligatorio richiesto da .claude/rules/hardware-and-perimeter.md.

Uso
---
    python emerald_bag_fix_round2.py ROUND2.sav OUTPUT.sav
    python emerald_bag_fix_round2.py ROUND2.sav OUTPUT.sav --verifica-soltanto
"""

import argparse
import struct
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emerald_bag_decode import (  # noqa: E402
    u16, u32, checksum_prefix, read_slot, assemble, detect_game,
    GAMES, ITEM_SLOT_SIZE, SECTOR_SIZE, SECTORS_PER_SLOT, SECTOR_DATA_SIZE, OFF_CHECKSUM,
)

# --- Il piano del secondo giro, confermato dall'utente il 2026-09-17 -------------------

CHIAVE_DA_RIMUOVERE = {269, 276, 277}          # Merce Devon, Sfera Rossa, Sfera Blu
CHIAVE_DA_AGGIUNGERE = [371, 376]              # Biglietto Aurora, Vecchia Mappa Marina

# I due esemplari superstiti dal primo giro, allenatore sospetto `C6B4D7EF` come i due
# già rimossi: individui distinti (STUDIO-01, sezione 17), non un doppione da clonazione.
SQUADRA_PID_DA_RIMUOVERE = {0x4084BA91, 0x81B5D401}
PARTY_COUNT_OFF = 0x234
PARTY_DATA_OFF = 0x238
PARTY_STRUCT_LEN = 100
PARTY_MAX = 6

# Record di serie della Battle Pike: SaveBlock2 (sezione 0), verificato su include/global.h
# di pret/pokeemerald il 2026-09-17. FRONTIER_LVL_MODE_COUNT = 2 (Lv.50, Libero).
PIKE_RECORD_STREAKS_OFF_SB2 = 0xE08
FRONTIER_LVL_MODE_COUNT = 2


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


def patch_pocket_bytes(sec1_data, offset_in_sb1, nuove_voci):
    rel = offset_in_sb1
    for item_id, raw_qty in nuove_voci:
        struct.pack_into("<HH", sec1_data, rel, item_id, raw_qty)
        rel += ITEM_SLOT_SIZE
    return rel


def zero_pocket_tail(sec1_data, start_rel, offset_in_sb1, count):
    end_rel = offset_in_sb1 + count * ITEM_SLOT_SIZE
    for rel in range(start_rel, end_rel, ITEM_SLOT_SIZE):
        struct.pack_into("<HH", sec1_data, rel, 0, 0)


def ricalcola_checksum(sector_full, lunghezza):
    nuovo = checksum_prefix(sector_full, lunghezza // 4)
    struct.pack_into("<H", sector_full, OFF_CHECKSUM, nuovo)
    return nuovo


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("input", help="dump aggiornato e verificato (es. round2.sav), in sola lettura")
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

    sec0_pos = slot["sezioni"][0]["posizione"]
    sec1_pos = slot["sezioni"][1]["posizione"]
    base = slot_index * SECTORS_PER_SLOT * SECTOR_SIZE
    sec0_off_file = base + sec0_pos * SECTOR_SIZE
    sec1_off_file = base + sec1_pos * SECTOR_SIZE
    sec0_len = slot["sezioni"][0]["lunghezza_checksum"]
    sec1_len = slot["sezioni"][1]["lunghezza_checksum"]

    sec0_full = bytearray(blob[sec0_off_file:sec0_off_file + SECTOR_SIZE])
    sec1_full = bytearray(blob[sec1_off_file:sec1_off_file + SECTOR_SIZE])
    sec1_data = sec1_full

    # --- Oggetti Chiave: filtra le rimozioni, aggiungi le due nuove, azzera il resto ---
    esistenti = []
    for i in range(cnt_chiave):
        rel = off_chiave + i * ITEM_SLOT_SIZE
        item_id = u16(sec1_data, rel)
        if item_id == 0:
            break
        esistenti.append((item_id, u16(sec1_data, rel + 2)))

    prima_del_chiave = len(esistenti)
    rimosse = [t for t in esistenti if t[0] in CHIAVE_DA_RIMUOVERE]
    rimaste = [t for t in esistenti if t[0] not in CHIAVE_DA_RIMUOVERE]
    if len(rimosse) != len(CHIAVE_DA_RIMUOVERE):
        trovati = {t[0] for t in rimosse}
        mancanti = CHIAVE_DA_RIMUOVERE - trovati
        raise SystemExit("attesi in tasca Oggetti Chiave gli id %s da rimuovere, non trovati: %s"
                          % (sorted(CHIAVE_DA_RIMUOVERE), sorted(mancanti)))

    nuove = [(item_id, (1 ^ key16) & 0xFFFF) for item_id in CHIAVE_DA_AGGIUNGERE]
    voci_chiave = rimaste + nuove
    if len(voci_chiave) > cnt_chiave:
        raise SystemExit("la tasca Oggetti Chiave non ha posto: %d voci per %d slot"
                          % (len(voci_chiave), cnt_chiave))
    primo_vuoto = patch_pocket_bytes(sec1_data, off_chiave, voci_chiave)
    zero_pocket_tail(sec1_data, primo_vuoto, off_chiave, cnt_chiave)

    # --- Squadra: rimuovi i due superstiti per PID, compatta, aggiorna il contatore ----
    party_count = sec1_data[PARTY_COUNT_OFF]
    party_slots = []
    for i in range(party_count):
        off = PARTY_DATA_OFF + i * PARTY_STRUCT_LEN
        pid = u32(sec1_data, off)
        party_slots.append((pid, bytes(sec1_data[off:off + PARTY_STRUCT_LEN])))
    superstiti = [(pid, dati) for pid, dati in party_slots if pid not in SQUADRA_PID_DA_RIMUOVERE]
    rimossi_party = len(party_slots) - len(superstiti)
    if rimossi_party != len(SQUADRA_PID_DA_RIMUOVERE):
        raise SystemExit("attesi in squadra i PID %s da rimuovere, trovati %d su %d attesi"
                          % ([hex(p) for p in SQUADRA_PID_DA_RIMUOVERE], rimossi_party,
                             len(SQUADRA_PID_DA_RIMUOVERE)))
    for i in range(PARTY_MAX):
        off = PARTY_DATA_OFF + i * PARTY_STRUCT_LEN
        if i < len(superstiti):
            sec1_data[off:off + PARTY_STRUCT_LEN] = superstiti[i][1]
        else:
            sec1_data[off:off + PARTY_STRUCT_LEN] = bytes(PARTY_STRUCT_LEN)
    sec1_data[PARTY_COUNT_OFF] = len(superstiti)

    vecchio_cs1 = u16(sec1_full, OFF_CHECKSUM)
    nuovo_cs1 = ricalcola_checksum(sec1_full, sec1_len)

    # --- Record della Battle Pike, dentro la sezione 0 (SaveBlock2) --------------------
    record_prima = [u16(sec0_full, PIKE_RECORD_STREAKS_OFF_SB2 + i * 2)
                     for i in range(FRONTIER_LVL_MODE_COUNT)]
    for i in range(FRONTIER_LVL_MODE_COUNT):
        struct.pack_into("<H", sec0_full, PIKE_RECORD_STREAKS_OFF_SB2 + i * 2, 0)
    vecchio_cs0 = u16(sec0_full, OFF_CHECKSUM)
    nuovo_cs0 = ricalcola_checksum(sec0_full, sec0_len)

    print("Slot scelto: %d, chiave 0x%08X" % (slot_index, key))
    print("Oggetti Chiave: %d prima, rimosse %s, aggiunte %s, %d dopo (capienza %d)"
          % (prima_del_chiave, sorted(CHIAVE_DA_RIMUOVERE), CHIAVE_DA_AGGIUNGERE,
             len(voci_chiave), cnt_chiave))
    print("Squadra: %d esemplari rimossi per PID, da %d a %d rimasti"
          % (rimossi_party, len(party_slots), len(superstiti)))
    print("Record Battle Pike: %s -> %s (Lv.50, Libero)"
          % (record_prima, [0] * FRONTIER_LVL_MODE_COUNT))
    print("Checksum sezione 1: 0x%04X -> 0x%04X" % (vecchio_cs1, nuovo_cs1))
    print("Checksum sezione 0: 0x%04X -> 0x%04X" % (vecchio_cs0, nuovo_cs0))

    if args.verifica_soltanto:
        print("\n--verifica-soltanto: nessun file scritto")
        return 0

    blob[sec1_off_file:sec1_off_file + SECTOR_SIZE] = sec1_full
    blob[sec0_off_file:sec0_off_file + SECTOR_SIZE] = sec0_full
    with open(args.output, "wb") as fh:
        fh.write(blob)
    print("\nScritto: %s" % args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
