#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Giro del 2026-11-20 sul Rubino: gli otto della Grotta Mutevole nel box 13 e il Biglietto Eone.

Perché esiste
-------------
ADR-134, terza modifica, manda sul Rubino gli otto incontri della Grotta Mutevole composti da
`emerald_grotta_mutevole.py`, che PKHeX contesta perché l'evento della grotta non è mai stato
distribuito: per questo non li scrive `tools/pkhex-scrivi-salvataggio`, che esclude i contestati,
e li scrive questo strumento, byte per byte, dai file del lotto. ADR-135 aggiunge il Biglietto
Eone, l'unico evento a biglietto del Rubino. Il SID e il Pokédex (ADR-099 e ADR-089) li fa prima
`tools/pkhex-allinea-gen3`, il cui file è l'ingresso di questo strumento; il Pokédex è già giusto
anche per gli otto, perché le loro specie sono già nei box.

Che cosa fa, verificato su pret/pokeruby
----------------------------------------
Gli otto esemplari vanno nel box 13, posti 17-24, che devono essere vuoti: il deposito
(`PokemonStorage`) comincia con quattro byte e poi tiene 14 box da 30 posti di 80 byte, e il
record si copia com'è, già cifrato e con il suo checksum. Il Biglietto Eone (`ITEM_EON_TICKET`, 275)
entra nel primo posto vuoto della tasca Oggetti Chiave, a SaveBlock1 0x5B0, con quantità 1 in
chiaro, perché il Rubino non maschera le quantità; `FLAG_SYS_HAS_EON_TICKET` (0x853) si accende nei
flag a SaveBlock1 0x1220. Sono le due scritture di `ReceiveGiftItem` in `src/record_mixing.c`.

Ogni sezione toccata riceve il checksum ricalcolato; si scrive nello slot attivo e l'altro resta
com'era. Lo strumento non scrive mai sulla cartuccia e non sovrascrive l'uscita.

Uso
---
    python rubino_ultimo_giro.py INGRESSO.sav USCITA.sav --lotto CARTELLA [--verifica-soltanto]
"""

import argparse
import json
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emerald_bag_decode import (  # noqa: E402
    u16, checksum_prefix, read_slot, assemble, SECTOR_SIZE, SECTORS_PER_SLOT, OFF_CHECKSUM,
)

SECTOR_DATA_SIZE = 3968
TID_RUBINO = 49107
ITEM_EON_TICKET = 275
OFF_TASCA_CHIAVE = 0x5B0
POSTI_TASCA_CHIAVE = 20
OFF_FLAGS = 0x1220
FLAG_SYS_HAS_EON_TICKET = 0x853
BOX_GROTTA = 12            # box 13, indice da zero
PRIMO_POSTO = 16           # posto 17, indice da zero
ORDINE = ["mareep", "pineco", "houndour", "teddiursa", "aipom", "shuckle", "stantler", "smeargle"]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--lotto", required=True)
    ap.add_argument("--verifica-soltanto", action="store_true")
    args = ap.parse_args()
    if os.path.abspath(args.input) == os.path.abspath(args.output):
        raise SystemExit("l'uscita non può essere l'ingresso")
    if os.path.exists(args.output) and not args.verifica_soltanto:
        raise SystemExit("l'uscita esiste già: non la sovrascrivo")

    blob = bytearray(open(args.input, "rb").read())
    slots = [read_slot(blob, i) for i in range(2)]
    validi = [(i, s) for i, s in enumerate(slots) if sorted(s["sezioni"]) == list(range(14))]
    if not validi:
        raise SystemExit("nessuno slot con 14 sezioni valide")
    slot_index, slot = max(validi, key=lambda t: max(t[1]["contatori"]))
    sb2, _ = assemble(slot)
    if u16(sb2, 0x0A) != TID_RUBINO:
        raise SystemExit("il TID non è quello del Rubino (%d)" % TID_RUBINO)

    base = slot_index * SECTORS_PER_SLOT * SECTOR_SIZE
    settori = {}

    def settore(sec_id):
        if sec_id not in settori:
            off = base + slot["sezioni"][sec_id]["posizione"] * SECTOR_SIZE
            settori[sec_id] = [off, bytearray(blob[off:off + SECTOR_SIZE])]
        return settori[sec_id][1]

    def dove(prima_sezione, off, n):
        s, o = prima_sezione + off // SECTOR_DATA_SIZE, off % SECTOR_DATA_SIZE
        if o + n > SECTOR_DATA_SIZE:
            raise SystemExit("campo a cavallo di due sezioni, non previsto")
        return s, o

    def leggi(prima, off, n):
        s, o = dove(prima, off, n)
        return bytes(settore(s)[o:o + n])

    def scrivi(prima, off, dati):
        s, o = dove(prima, off, len(dati))
        settore(s)[o:o + len(dati)] = dati

    rapporto = []

    # 1. Gli otto della Grotta Mutevole
    manifesto = json.load(open(os.path.join(args.lotto, "manifesto.json"), encoding="utf-8"))
    for k, nome in enumerate(ORDINE):
        voce = manifesto[nome.capitalize()]
        if not voce.get("mai_in_home"):
            raise SystemExit("%s: il manifesto non dichiara mai_in_home" % nome)
        dati = open(os.path.join(args.lotto, voce["file"]), "rb").read()
        if len(dati) != 80:
            raise SystemExit("%s: attesi 80 byte" % voce["file"])
        indice = BOX_GROTTA * 30 + PRIMO_POSTO + k
        off = 4 + indice * 80
        if any(leggi(5, off, 80)):
            raise SystemExit("box 13 posto %d non è vuoto" % (PRIMO_POSTO + k + 1))
        if struct.unpack_from("<I", dati, 0)[0] != int(voce["personalita"], 16):
            raise SystemExit("%s: personalità diversa dal manifesto" % nome)
        scrivi(5, off, dati)
        rapporto.append("box 13 posto %d: %s (%s)" % (PRIMO_POSTO + k + 1, nome.capitalize(), voce["personalita"]))

    # 2. Biglietto Eone
    tasca = leggi(1, OFF_TASCA_CHIAVE, POSTI_TASCA_CHIAVE * 4)
    posti = [struct.unpack_from("<HH", tasca, i * 4) for i in range(POSTI_TASCA_CHIAVE)]
    if any(iid == ITEM_EON_TICKET for iid, _ in posti):
        raise SystemExit("il Biglietto Eone è già nella tasca")
    libero = next((i for i, (iid, _) in enumerate(posti) if iid == 0), None)
    if libero is None:
        raise SystemExit("tasca Oggetti Chiave piena")
    scrivi(1, OFF_TASCA_CHIAVE + libero * 4, struct.pack("<HH", ITEM_EON_TICKET, 1))
    rapporto.append("tasca Oggetti Chiave posto %d: Biglietto Eone, quantità 1" % (libero + 1))
    off_flag = OFF_FLAGS + FLAG_SYS_HAS_EON_TICKET // 8
    bit = 1 << (FLAG_SYS_HAS_EON_TICKET % 8)
    vecchio = leggi(1, off_flag, 1)[0]
    if vecchio & bit:
        raise SystemExit("FLAG_SYS_HAS_EON_TICKET è già acceso")
    scrivi(1, off_flag, bytes([vecchio | bit]))
    rapporto.append("FLAG_SYS_HAS_EON_TICKET (0x853) acceso")

    for sec_id, (_, sett) in sorted(settori.items()):
        prima = u16(sett, OFF_CHECKSUM)
        struct.pack_into("<H", sett, OFF_CHECKSUM, checksum_prefix(sett, slot["sezioni"][sec_id]["lunghezza_checksum"] // 4))
        rapporto.append("sezione %d: checksum 0x%04X -> 0x%04X" % (sec_id, prima, u16(sett, OFF_CHECKSUM)))

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
