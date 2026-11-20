#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ultimo giro su Smeraldo: Roccia di Re doppia, sfondi dei box 10 e 11, quattro decorazioni.

Perché esiste
-------------
Il 2026-11-18 il proprietario ha chiesto di chiudere per sempre le scritture rimaste in sospeso
su Smeraldo, con il criterio dello Smeraldo più completo che un giocatore italiano potesse avere
(ADR-134). Misurate sull'estrazione del 2026-11-18 restavano tre cose.

1. La Roccia di Re è doppia: cinque nel deposito PC, dal sesto giro, e una nella tasca Oggetti,
   che c'era già. Il proprietario ha deciso il 2026-09-21 di togliere quella della tasca.
2. ADR-075 ha deciso lo sfondo Plain per i box 10 e 11, e la scrittura del 2026-09-23 non lo ha
   portato: i due box hanno ancora gli sfondi predefiniti, Seafloor e River. Gli altri dodici sono
   già quelli decisi (nove ordinari diversi sui box 1-9, Sky sul 12 per ADR-078, Amici sul 13 e
   sul 14).
3. Delle 120 decorazioni del gioco la cartuccia ne ha 116. Mancano la Sedia Vetro (Pretty Chair,
   Laboratorio del Vetro sul Percorso 113 con la cenere), la Sedia Mattoni e la Sedia Roccia
   (Brick Chair e Hard Chair, negozio di Forestopoli), il Cuscino Bacio (Kiss Cushion, Parco Lotta,
   32 punti lotta). Sono tutte e quattro ottenibili giocando uno Smeraldo italiano.

Che cosa fa, e dove, verificato su pret/pokeemerald
---------------------------------------------------
La tasca Oggetti sta a SaveBlock1 0x560, trenta posizioni da quattro byte, con la quantità in XOR
con i 16 bit bassi della chiave di sicurezza. Lo strumento toglie l'unica posizione con la Roccia
di Re (187) e fa scorrere le successive, come fa il gioco quando una posizione si svuota; l'ultima
diventa vuota, cioè identificativo 0 e quantità 0 mascherata, che sul disco è la chiave stessa.

Le decorazioni stanno in SaveBlock1 da 0x2734 (`include/global.h`), una categoria dopo l'altra; le
sedie a 0x273E (dieci posti) e i cuscini a 0x27C0 (dieci posti). Il gioco tiene ogni categoria
ordinata per identificativo crescente (`CondenseDecorationsInCategory`, `src/decoration_inventory.c`),
e lo strumento scrive nello stesso ordine.

Gli sfondi stanno nel deposito, `boxWallpapers` a 0x83C2 di `PokemonStorage`
(`include/pokemon_storage_system.h`), un byte per box; Plain vale 15 (`src/data/wallpapers.h`).

Ogni sezione toccata riceve il checksum ricalcolato. Si scrive nello slot attivo e l'altro resta
com'era. Lo strumento non scrive mai sulla cartuccia e non sovrascrive l'ingresso: la scrittura
fisica resta manuale con FlashGBX, con la rilettura voluta da `.claude/rules/hardware-and-perimeter.md`.

Uso
---
    python emerald_ultimo_giro.py INGRESSO.sav USCITA.sav
    python emerald_ultimo_giro.py INGRESSO.sav USCITA.sav --verifica-soltanto
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

SECTOR_DATA_SIZE = 3968

ITEM_KINGS_ROCK = 187
OFF_TASCA_OGGETTI = 0x560
POSTI_TASCA_OGGETTI = 30

# Decorazioni, da include/constants/decorations.h
DECOR_PRETTY_CHAIR = 13
DECOR_BRICK_CHAIR = 16
DECOR_HARD_CHAIR = 18
DECOR_KISS_CUSHION = 103
CATEGORIE = {
    "sedie": (0x273E, 10, (DECOR_PRETTY_CHAIR, DECOR_BRICK_CHAIR, DECOR_HARD_CHAIR)),
    "cuscini": (0x27C0, 10, (DECOR_KISS_CUSHION,)),
}

OFF_SFONDI = 0x83C2
WALLPAPER_PLAIN = 15
SFONDI_NUOVI = {9: WALLPAPER_PLAIN, 10: WALLPAPER_PLAIN}  # box 10 e 11, indice da zero


def scegli_slot(blob):
    slots = [read_slot(blob, i) for i in range(2)]
    usable = [(i, s) for i, s in enumerate(slots) if 0 in s["sezioni"]]
    if not usable:
        raise SystemExit("nessuno slot ha una sezione 0 valida")
    return max(usable, key=lambda t: max(t[1]["contatori"]) if t[1]["contatori"] else -1)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--verifica-soltanto", action="store_true")
    args = ap.parse_args()
    if os.path.abspath(args.input) == os.path.abspath(args.output):
        raise SystemExit("l'uscita non può essere l'ingresso")
    if os.path.exists(args.output) and not args.verifica_soltanto:
        raise SystemExit("l'uscita esiste già: non la sovrascrivo")

    blob = bytearray(open(args.input, "rb").read())
    slot_index, slot = scegli_slot(blob)
    sb2, sb1 = assemble(slot)
    esiti = detect_game(sb2, sb1)
    punti, nome, game, _ = esiti[0]
    if game is not GAMES["emerald"] or punti <= 0:
        raise SystemExit("il file non è Smeraldo con margine sufficiente")
    chiave16 = u32(sb2, game["chiave_offset"]) & 0xFFFF

    base = slot_index * SECTORS_PER_SLOT * SECTOR_SIZE
    settori = {}

    def settore(sec_id):
        if sec_id not in settori:
            if sec_id not in slot["sezioni"]:
                raise SystemExit("sezione %d assente" % sec_id)
            pos = slot["sezioni"][sec_id]["posizione"]
            off = base + pos * SECTOR_SIZE
            settori[sec_id] = [off, bytearray(blob[off:off + SECTOR_SIZE])]
        return settori[sec_id][1]

    def dove_sb1(off):
        return 1 + off // SECTOR_DATA_SIZE, off % SECTOR_DATA_SIZE

    def dove_deposito(off):
        return 5 + off // SECTOR_DATA_SIZE, off % SECTOR_DATA_SIZE

    def leggi(dove, off, n):
        s, o = dove(off)
        if o + n > SECTOR_DATA_SIZE:
            raise SystemExit("campo a cavallo di due sezioni, non previsto")
        return bytes(settore(s)[o:o + n])

    def scrivi(dove, off, dati):
        s, o = dove(off)
        settore(s)[o:o + len(dati)] = dati

    rapporto = []

    # 1. Roccia di Re dalla tasca Oggetti
    grezzo = leggi(dove_sb1, OFF_TASCA_OGGETTI, POSTI_TASCA_OGGETTI * ITEM_SLOT_SIZE)
    posti = [struct.unpack_from("<HH", grezzo, i * 4) for i in range(POSTI_TASCA_OGGETTI)]
    trovati = [i for i, (iid, _) in enumerate(posti) if iid == ITEM_KINGS_ROCK]
    if len(trovati) != 1:
        raise SystemExit("attesa una sola Roccia di Re nella tasca Oggetti, trovate %d" % len(trovati))
    i = trovati[0]
    quantita = posti[i][1] ^ chiave16
    if quantita != 1:
        raise SystemExit("la Roccia di Re della tasca ha quantità %d, attesa 1" % quantita)
    nuovi = posti[:i] + posti[i + 1:] + [(0, chiave16)]
    scrivi(dove_sb1, OFF_TASCA_OGGETTI, b"".join(struct.pack("<HH", a, b) for a, b in nuovi))
    rapporto.append("tasca Oggetti: tolta la Roccia di Re dalla posizione %d, %d posizioni scorse"
                    % (i + 1, POSTI_TASCA_OGGETTI - 1 - i))

    # 2. Decorazioni
    for nome_cat, (off, n, aggiunte) in CATEGORIE.items():
        prima = list(leggi(dove_sb1, off, n))
        presenti = [x for x in prima if x]
        gia = [d for d in aggiunte if d in presenti]
        if gia:
            raise SystemExit("%s: già presenti %s" % (nome_cat, gia))
        dopo = sorted(presenti + list(aggiunte))
        if len(dopo) > n:
            raise SystemExit("%s: non c'è posto" % nome_cat)
        dopo += [0] * (n - len(dopo))
        scrivi(dove_sb1, off, bytes(dopo))
        rapporto.append("%s: %s -> %s" % (nome_cat, presenti, [x for x in dopo if x]))

    # 3. Sfondi dei box 10 e 11
    sfondi = list(leggi(dove_deposito, OFF_SFONDI, 14))
    nuovi_sfondi = list(sfondi)
    for box, valore in SFONDI_NUOVI.items():
        nuovi_sfondi[box] = valore
    scrivi(dove_deposito, OFF_SFONDI, bytes(nuovi_sfondi))
    rapporto.append("sfondi: %s -> %s" % (sfondi, nuovi_sfondi))

    # Checksum
    for sec_id, (off_file, sett) in sorted(settori.items()):
        lunghezza = slot["sezioni"][sec_id]["lunghezza_checksum"]
        vecchio = u16(sett, OFF_CHECKSUM)
        struct.pack_into("<H", sett, OFF_CHECKSUM, checksum_prefix(sett, lunghezza // 4))
        rapporto.append("sezione %d: checksum 0x%04X -> 0x%04X" % (sec_id, vecchio, u16(sett, OFF_CHECKSUM)))

    print("slot attivo %d" % slot_index)
    print("\n".join(rapporto))
    if args.verifica_soltanto:
        print("--verifica-soltanto: nessun file scritto")
        return 0
    for off_file, sett in settori.values():
        blob[off_file:off_file + SECTOR_SIZE] = sett
    with open(args.output, "wb") as fh:
        fh.write(blob)
    print("scritto %s" % args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
