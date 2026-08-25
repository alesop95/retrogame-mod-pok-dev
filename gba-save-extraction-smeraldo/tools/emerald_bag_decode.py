#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legge un salvataggio Gen 3 e diagnostica lo zaino, smascherando le quantita'.

Perche' esiste
--------------
In Pokemon Smeraldo le quantita' degli oggetti nello zaino non stanno in chiaro nel
salvataggio: sono in XOR con una chiave di sicurezza per Pokemon specifica di quel
salvataggio. La verifica sul sorgente di pret/pokeemerald e' univoca:

    struct SaveBlock2 { ... /*0xAC*/ u32 encryptionKey; ... };

    static u16 GetBagItemQuantity(u16 *quantity)
    { return gSaveBlock2Ptr->encryptionKey ^ *quantity; }

    static u16 GetPCItemQuantity(u16 *quantity)
    { return *quantity; }

Ne segue il punto che conta per una diagnosi: una quantita' assurda letta in chiaro
dallo zaino non prova nulla, perche' e' l'aspetto normale di un dato mascherato. Solo
dopo lo smascheramento si puo' dire che cosa e' davvero corrotto. Nel deposito PC,
invece, le quantita' sono in chiaro e un valore assurdo la' e' un'anomalia vera.

I tre giochi non si somigliano e nulla si riusa fra loro. Rubino e Zaffiro non mascherano
affatto. Rosso Fuoco e Verde Foglia mascherano, ma tengono la chiave a 0xF20 dentro
SaveBlock2 e hanno tasche di capienza diversa: sono valori verificati su pret/pokefirered
e pret/pokeruby il 2026-08-25, e per Rosso Fuoco correggono una fonte secondaria che
indicava la chiave a 0x0AF8.

Questo strumento non scrive nulla: legge, valida e riferisce. La scrittura su un
salvataggio reale resta un'operazione separata e manuale, dopo il backup in doppia
copia richiesto da .claude/rules/hardware-and-perimeter.md.

Uso
---
    python tools/emerald_bag_decode.py PERCORSO.sav
    python tools/emerald_bag_decode.py PERCORSO.sav --game frlg --json out.json
"""

import argparse
import json
import struct
import sys

SECTOR_SIZE = 4096
SECTOR_DATA_SIZE = 3968
SECTORS_PER_SLOT = 14
SECTOR_SIGNATURE = 0x08012025

# Offset del piede di sezione, verificati su include/save.h di pokeemerald:
# data[3968], unused[116], id(u16), checksum(u16), signature(u32), counter(u32)
OFF_ID = 0x0FF4
OFF_CHECKSUM = 0x0FF6
OFF_SIGNATURE = 0x0FF8
OFF_COUNTER = 0x0FFC

ITEM_SLOT_SIZE = 4          # u16 itemId, u16 quantity
MAX_BAG_ITEM_CAPACITY = 99
MAX_BERRY_CAPACITY = 999
MAX_MONEY = 999999

# Offset dentro SaveBlock1, da include/global.h di pokeemerald.
# SaveBlock1 e' la concatenazione delle sezioni con id da 1 a 4.
EMERALD = {
    "nome": "Smeraldo",
    "chiave_offset": 0xAC,          # dentro SaveBlock2, cioe' la sezione con id 0
    "maschera": True,
    "party_count": 0x234,
    "money": 0x490,
    "coins": 0x494,
    "tasche": [
        ("Deposito PC", 0x498, 50, False, MAX_BAG_ITEM_CAPACITY),
        ("Oggetti", 0x560, 30, True, MAX_BAG_ITEM_CAPACITY),
        ("Oggetti chiave", 0x5D8, 30, True, MAX_BAG_ITEM_CAPACITY),
        ("Poke Ball", 0x650, 16, True, MAX_BAG_ITEM_CAPACITY),
        ("MT e MN", 0x690, 64, True, MAX_BAG_ITEM_CAPACITY),
        ("Bacche", 0x790, 46, True, MAX_BERRY_CAPACITY),
    ],
    "items_count": 377,
}

# Rosso Fuoco e Verde Foglia: tutto diverso, e verificato su pret/pokefirered il
# 2026-08-25. La chiave sta a 0xF20 dentro SaveBlock2, che misura 0xF24 byte: la fonte
# secondaria che indicava 0x0AF8 e' sbagliata, ed e' il quinto errore di quel tipo che
# questo progetto documenta. Le capienze delle tasche sono diverse da quelle di Smeraldo
# e da quelle di Rubino e Zaffiro, quindi non si possono riusare.
FRLG = {
    "nome": "Rosso Fuoco e Verde Foglia",
    "chiave_offset": 0xF20,
    "maschera": True,
    "party_count": 0x34,
    "money": 0x290,
    "coins": None,
    "tasche": [
        ("Deposito PC", 0x298, 30, False, MAX_BAG_ITEM_CAPACITY),
        ("Oggetti", 0x310, 42, True, MAX_BAG_ITEM_CAPACITY),
        ("Oggetti chiave", 0x3B8, 30, True, MAX_BAG_ITEM_CAPACITY),
        ("Poke Ball", 0x430, 13, True, MAX_BAG_ITEM_CAPACITY),
        ("MT e MN", 0x464, 58, True, MAX_BAG_ITEM_CAPACITY),
        ("Bacche", 0x54C, 43, True, MAX_BERRY_CAPACITY),
    ],
    "items_count": 375,
}

RUBY_SAPPHIRE = {
    "nome": "Rubino e Zaffiro",
    "chiave_offset": None,
    "maschera": False,
    "party_count": 0x234,
    "money": 0x490,
    "coins": 0x494,
    "tasche": [
        ("Deposito PC", 0x498, 50, False, MAX_BAG_ITEM_CAPACITY),
        ("Oggetti", 0x560, 20, False, MAX_BAG_ITEM_CAPACITY),
        ("Oggetti chiave", 0x5B0, 20, False, MAX_BAG_ITEM_CAPACITY),
        ("Poke Ball", 0x600, 16, False, MAX_BAG_ITEM_CAPACITY),
        ("MT e MN", 0x640, 64, False, MAX_BAG_ITEM_CAPACITY),
        ("Bacche", 0x740, 46, False, MAX_BERRY_CAPACITY),
    ],
    "items_count": 349,
}

GAMES = {"emerald": EMERALD, "frlg": FRLG, "rs": RUBY_SAPPHIRE}


def score_candidate(game, sb2, sb1):
    """Quanto un salvataggio somiglia a quello del gioco indicato, con le prove.

    Serve a non fidarsi di un parametro. Un thread di Project Pokemon documenta un caso
    reale in cui un editor ha identificato un salvataggio di Smeraldo come Rubino o
    Zaffiro, e la conseguenza e' stata che gli oggetti sono finiti negli slot sbagliati:
    e' esattamente l'errore che questa funzione esiste per intercettare, perche' Smeraldo
    maschera le quantita' e Rubino e Zaffiro no.

    Ritorna (punteggio, elenco di prove). Non decide: riferisce.
    """
    prove = []
    punti = 0

    key = u32(sb2, game["chiave_offset"]) if game["maschera"] else 0
    if game["maschera"]:
        prove.append("chiave a 0x%03X: 0x%08X" % (game["chiave_offset"], key))

    party = sb1[game["party_count"]]
    if 1 <= party <= 6:
        punti += 2
        prove.append("squadra di %d Pokemon a 0x%03X, plausibile" % (party, game["party_count"]))
    elif party == 0:
        prove.append("squadra vuota a 0x%03X, non discrimina" % game["party_count"])
    else:
        punti -= 2
        prove.append("squadra di %d a 0x%03X, implausibile" % (party, game["party_count"]))

    if game["money"] is not None:
        raw = u32(sb1, game["money"])
        money = (raw ^ key) & 0xFFFFFFFF if game["maschera"] else raw
        if money == 0:
            # Zero non e' una prova: e' cio' che si legge da un'area non pertinente.
            prove.append("denaro nullo, non discrimina")
        elif money <= MAX_MONEY:
            punti += 3
            prove.append("denaro %d entro il tetto, coerente" % money)
        else:
            punti -= 3
            prove.append("denaro %d oltre il tetto, incoerente" % money)

    # Uno slot vuoto in una tasca mascherata contiene la chiave: se la chiave dedotta
    # coincide con quella letta, la maschera e' quella giusta e quindi il gioco lo e'.
    if game["maschera"] and game["tasche"]:
        for nome, offset, count, masked, _cap in game["tasche"]:
            if not masked:
                continue
            for i in range(count):
                base = offset + i * ITEM_SLOT_SIZE
                if u16(sb1, base) == 0 and u16(sb1, base + 2) == 0:
                    # Uno slot vuoto vale come prova solo se la chiave che ne deriva non
                    # e' nulla: una chiave a zero e' il caso degenere di un'area di soli
                    # zeri, che somiglia a qualunque cosa.
                    if key & 0xFFFF:
                        punti += 3
                        prove.append("slot vuoto in %s conferma la maschera" % nome)
                    else:
                        prove.append("chiave nulla, lo slot vuoto non discrimina")
                    break
            break

    return punti, prove


def detect_game(sb2, sb1):
    """Prova tutti i candidati e riferisce il confronto, invece di indovinare."""
    esiti = []
    for nome, game in GAMES.items():
        try:
            punti, prove = score_candidate(game, sb2, sb1)
        except (IndexError, struct.error) as exc:
            punti, prove = -99, ["struttura troppo corta per questo candidato: %s" % exc]
        esiti.append((punti, nome, game, prove))
    esiti.sort(key=lambda e: -e[0])
    return esiti


def u16(buf, off):
    return struct.unpack_from("<H", buf, off)[0]


def u32(buf, off):
    return struct.unpack_from("<I", buf, off)[0]


def checksum_prefix(data, words):
    """Somma di `words` parole da 32 bit, ripiegata a 16 bit.

    Replica CalculateChecksum di src/save.c:
        for (i = 0; i < size / 4; i++) checksum += *((u32 *)data)++;
        return ((checksum >> 16) + checksum);
    """
    total = 0
    for i in range(words):
        total = (total + u32(data, i * 4)) & 0xFFFFFFFF
    return ((total >> 16) + total) & 0xFFFF


def validate_sector(sector):
    """Ritorna (id, counter, lunghezza_verificata) oppure None se la sezione non e' valida.

    La lunghezza su cui il gioco calcola il checksum dipende da sizeof delle strutture
    di salvataggio, che non e' ricavabile da qui senza compilare. Invece di indovinarla
    si cerca quale prefisso di parole da 32 bit riproduce il checksum memorizzato,
    partendo dalla sezione piena, che e' il caso normale.
    """
    signature = u32(sector, OFF_SIGNATURE)
    if signature != SECTOR_SIGNATURE:
        return None
    stored = u16(sector, OFF_CHECKSUM)
    sec_id = u16(sector, OFF_ID)
    counter = u32(sector, OFF_COUNTER)

    running = 0
    match = None
    for i in range(SECTOR_DATA_SIZE // 4):
        running = (running + u32(sector, i * 4)) & 0xFFFFFFFF
        folded = ((running >> 16) + running) & 0xFFFF
        if folded == stored:
            match = (i + 1) * 4      # prefisso piu' corto che torna
            if match == SECTOR_DATA_SIZE:
                break
    if match is None:
        return None
    return sec_id, counter, match


def read_slot(blob, slot_index):
    base = slot_index * SECTORS_PER_SLOT * SECTOR_SIZE
    sectors, invalid = {}, []
    counters = set()
    for n in range(SECTORS_PER_SLOT):
        off = base + n * SECTOR_SIZE
        raw = blob[off:off + SECTOR_SIZE]
        if len(raw) < SECTOR_SIZE:
            invalid.append((n, "troncata"))
            continue
        parsed = validate_sector(raw)
        if parsed is None:
            invalid.append((n, "firma o checksum non validi"))
            continue
        sec_id, counter, length = parsed
        sectors[sec_id] = {"posizione": n, "dati": raw[:SECTOR_DATA_SIZE],
                           "lunghezza_checksum": length, "contatore": counter}
        counters.add(counter)
    return {"sezioni": sectors, "non_valide": invalid, "contatori": sorted(counters)}


def assemble(slot):
    """SaveBlock2 dalla sezione 0, SaveBlock1 dalle sezioni da 1 a 4 in ordine di id."""
    sec = slot["sezioni"]
    sb2 = sec[0]["dati"] if 0 in sec else None
    parts = []
    for sec_id in range(1, 5):
        if sec_id not in sec:
            return sb2, None
        parts.append(sec[sec_id]["dati"])
    return sb2, b"".join(parts)


def decode_pockets(sb1, key16, game):
    """Decodifica le tasche. Solo la quantita' e' mascherata, l'id oggetto mai.

    Uno slot vuoto ha id oggetto zero e quantita' grezza zero, quindi in una tasca
    mascherata la sua quantita' decodificata vale esattamente la chiave a 16 bit. E'
    un controllo incrociato gratuito: la chiave letta a 0xAC deve coincidere con
    quella che si ricava da qualunque slot vuoto.
    """
    out = []
    for nome, offset, count, masked, cap in game["tasche"]:
        slots, anomalies, vuoti = [], [], []
        seen, hole = {}, False
        for i in range(count):
            base = offset + i * ITEM_SLOT_SIZE
            item_id = u16(sb1, base)
            raw_qty = u16(sb1, base + 2)
            qty = (raw_qty ^ key16) & 0xFFFF if masked else raw_qty
            if item_id == 0:
                hole = True
                if masked and raw_qty == 0:
                    vuoti.append(qty)
                elif raw_qty != 0:
                    anomalies.append("slot %d: id oggetto nullo con quantita' grezza "
                                     "0x%04X invece di 0x0000" % (i, raw_qty))
                continue
            if hole:
                anomalies.append("slot %d popolato dopo uno slot vuoto" % i)
            if item_id >= game["items_count"]:
                anomalies.append("slot %d: id oggetto %d fuori intervallo" % (i, item_id))
            if qty == 0:
                anomalies.append("slot %d: id oggetto %d con quantita' zero" % (i, item_id))
            if qty > cap:
                anomalies.append("slot %d: id %d con quantita' %d oltre il tetto di %d"
                                 % (i, item_id, qty, cap))
            if item_id in seen:
                anomalies.append("slot %d: id oggetto %d duplicato dello slot %d"
                                 % (i, item_id, seen[item_id]))
            seen[item_id] = i
            slots.append({"slot": i, "id": item_id, "quantita": qty,
                          "grezzo": raw_qty, "mascherato": masked})
        chiave_dedotta = vuoti[0] if vuoti else None
        if chiave_dedotta is not None and any(v != chiave_dedotta for v in vuoti):
            anomalies.append("gli slot vuoti non concordano sulla chiave dedotta")
        out.append({"tasca": nome, "occupati": len(slots), "capienza": count,
                    "voci": slots, "anomalie": anomalies,
                    "chiave_dedotta_da_slot_vuoto": chiave_dedotta})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("save", help="file di salvataggio, tipicamente 128 KiB")
    ap.add_argument("--game", choices=sorted(GAMES) + ["auto"], default="auto",
                    help="auto rileva il gioco dal salvataggio e riferisce le prove")
    ap.add_argument("--json", help="scrive il rapporto completo in JSON su questo percorso")
    args = ap.parse_args()

    with open(args.save, "rb") as fh:
        blob = fh.read()

    report = {"file": args.save, "dimensione": len(blob), "slot": []}
    print("File: %s (%d byte)" % (args.save, len(blob)))
    if len(blob) < SECTORS_PER_SLOT * SECTOR_SIZE:
        print("ERRORE: il file e' piu' corto di un singolo slot di salvataggio", file=sys.stderr)
        return 2

    slots = []
    for idx in range(2):
        if len(blob) < (idx + 1) * SECTORS_PER_SLOT * SECTOR_SIZE:
            break
        slot = read_slot(blob, idx)
        slots.append(slot)
        etichetta = "A" if idx == 0 else "B"
        print("\nSlot %s: %d sezioni valide su %d, contatori %s"
              % (etichetta, len(slot["sezioni"]), SECTORS_PER_SLOT, slot["contatori"]))
        for n, motivo in slot["non_valide"]:
            print("  sezione in posizione %d scartata: %s" % (n, motivo))
        if len(slot["contatori"]) > 1:
            print("  ATTENZIONE: contatori discordanti dentro lo stesso slot, "
                  "salvataggio interrotto a meta' o slot misto")
        report["slot"].append({"etichetta": etichetta,
                               "sezioni_valide": sorted(slot["sezioni"]),
                               "contatori": slot["contatori"],
                               "non_valide": [{"posizione": n, "motivo": m}
                                              for n, m in slot["non_valide"]]})

    # Scelta dello slot: A vince solo se il suo contatore e' strettamente maggiore.
    def counter_of(slot):
        return max(slot["contatori"]) if slot["contatori"] else -1

    usable = [s for s in slots if 0 in s["sezioni"]]
    if not usable:
        print("\nERRORE: nessuno slot ha una sezione 0 valida, niente da decodificare",
              file=sys.stderr)
        return 3
    if len(usable) == 2 and counter_of(usable[0]) > counter_of(usable[1]):
        chosen, etichetta = usable[0], "A"
    elif len(usable) == 2:
        chosen, etichetta = usable[1], "B"
    else:
        chosen = usable[0]
        etichetta = "A" if chosen is slots[0] else "B"
    print("\nSlot scelto: %s (contatore %d)" % (etichetta, counter_of(chosen)))
    report["slot_scelto"] = etichetta

    sb2, sb1 = assemble(chosen)
    if sb1 is None:
        print("ERRORE: lo slot scelto non ha tutte le sezioni da 1 a 4, "
              "SaveBlock1 non ricostruibile", file=sys.stderr)
        return 4

    # Identificazione del gioco. Non si fida del parametro: lo verifica, perche' un
    # gioco identificato male applica la maschera sbagliata alle quantita' e fa
    # sembrare corrotto uno zaino sano, o viceversa.
    esiti = detect_game(sb2, sb1)
    print("\nIdentificazione del gioco")
    for punti, nome, _g, prove in esiti:
        print("  %-8s punteggio %+d" % (nome, punti))
        for pr in prove:
            print("      %s" % pr)
    report["identificazione"] = [{"gioco": n, "punteggio": p, "prove": pr}
                                 for p, n, _g, pr in esiti]

    if args.game == "auto":
        punti, nome, game, _prove = esiti[0]
        if punti <= 0:
            print("\nERRORE: nessun candidato e' plausibile, il salvataggio non e' "
                  "riconoscibile. Indica il gioco a mano con --game.", file=sys.stderr)
            return 5
        if len(esiti) > 1 and esiti[1][0] == punti:
            print("\nERRORE: %s e %s pareggiano, l'identificazione e' ambigua. "
                  "Indica il gioco a mano con --game." % (nome, esiti[1][1]), file=sys.stderr)
            return 5
        print("\nGioco rilevato: %s" % game["nome"])
    else:
        game = GAMES[args.game]
        atteso = esiti[0][1]
        print("\nGioco dichiarato: %s" % game["nome"])
        if atteso != args.game:
            print("  ATTENZIONE: le prove indicano %s, non %s. Un gioco identificato "
                  "male applica la maschera sbagliata: verifica prima di fidarti."
                  % (atteso, args.game))
    report["gioco"] = game["nome"]

    key = 0
    if game["maschera"]:
        key = u32(sb2, game["chiave_offset"])
        print("Chiave di sicurezza a 0x%03X: 0x%08X (16 bit bassi: 0x%04X)"
              % (game["chiave_offset"], key, key & 0xFFFF))
    else:
        print("Questo gioco non maschera le quantita': nessuna chiave da applicare")
    report["chiave"] = key

    # Autoverifica della chiave: il denaro smascherato deve stare nel suo intervallo.
    if game["money"] is not None:
        money_raw = u32(sb1, game["money"])
        money = (money_raw ^ key) & 0xFFFFFFFF if game["maschera"] else money_raw
        coerente = money <= MAX_MONEY
        print("Denaro: %d %s" % (money, "(coerente, la chiave e' quella giusta)"
                                 if coerente else "(FUORI INTERVALLO: chiave o offset sbagliati)"))
        report["denaro"] = {"valore": money, "coerente": coerente}

    party = sb1[game["party_count"]]
    print("Pokemon in squadra: %d%s" % (party, "" if party <= 6 else "  ANOMALO"))
    report["squadra"] = party

    if not game["tasche"]:
        print("\nGli offset delle tasche per questo gioco non sono verificati in questa "
              "revisione dello strumento: chiave e denaro sono riferiti, lo zaino no.")
        report["tasche"] = []
    else:
        pockets = decode_pockets(sb1, key & 0xFFFF, game)
        report["tasche"] = pockets
        totale_anomalie = 0
        for p in pockets:
            print("\n%s: %d/%d slot occupati" % (p["tasca"], p["occupati"], p["capienza"]))
            dedotta = p["chiave_dedotta_da_slot_vuoto"]
            if dedotta is not None:
                stato = "concorda" if dedotta == (key & 0xFFFF) else "NON CONCORDA"
                print("  chiave dedotta da slot vuoto: 0x%04X (%s con quella a 0x%03X)"
                      % (dedotta, stato, game["chiave_offset"]))
            for v in p["voci"][:100]:
                nota = "  (grezzo 0x%04X)" % v["grezzo"] if v["mascherato"] else ""
                print("  slot %2d  id %4d  quantita' %4d%s"
                      % (v["slot"], v["id"], v["quantita"], nota))
            for a in p["anomalie"]:
                print("  ANOMALIA: " + a)
            totale_anomalie += len(p["anomalie"])
        print("\nAnomalie totali: %d" % totale_anomalie)
        report["anomalie_totali"] = totale_anomalie

    if args.json:
        with open(args.json, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=2)
        print("Rapporto JSON scritto in " + args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
