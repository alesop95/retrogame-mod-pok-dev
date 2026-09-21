#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Settimo giro: accende il permesso per il menu di reset dell'RTC, senza toccare l'orologio.

Perche' esiste
--------------
Dopo il cambio di pila tampone l'orologio interno va risincronizzato con una procedura
del gioco stesso, raggiungibile dalla schermata del titolo con Sinistra (D-pad) + Select
+ B. Verificato su `pret/pokeemerald`, `src/event_data.c`: `CanResetRTC()` (chiamata da
`src/title_screen.c` prima di mostrare quel menu) richiede in congiunzione
`FLAG_SYS_RESET_RTC_ENABLE` acceso e `VAR_RESET_RTC_ENABLE` uguale a `0x920`. Sono
esattamente il flag e la costante che una guida della community (r/PokemonEmerald,
"How to actually fix/reset the Emerald RTC?") imposta a mano in PKHex, scheda Event
Flags e Event Constants. Questo strumento fa la stessa cosa in modo verificabile byte
per byte, come ogni altra correzione di questo progetto, invece di un clic manuale.

Non tocca l'orologio stesso, che il gioco calcola dall'RTC fisico e che nessuno
strumento esterno può impostare: accende solo il permesso per il menu, che va poi
completato in gioco (Sinistra+Select+B alla schermata del titolo, A per confermare,
NON toccare i giorni, solo ora e minuti, poi salvare). Il permesso è a uso singolo per
costruzione: il gioco stesso lo spegne con `DisableResetRTC()` non appena il menu viene
confermato (`src/reset_rtc_screen.c`), quindi non serve e non esiste un'opzione per
spegnerlo da qui.

Non tocca il campo "Berry fix" di PKHex: quel pulsante opera su un campo del
salvataggio (verosimilmente `lastBerryTreeUpdate`) che questo studio non ha ancora
verificato sul sorgente del gioco, perche' PKHex e' un progetto diverso. Vedi
STUDIO-01, sezione 23, per la spiegazione completa e per il perche' i giorni non
vanno mai alterati nel menu.

Uso
---
    python emerald_rtc_reset_fix.py INGRESSO.sav USCITA.sav
    python emerald_rtc_reset_fix.py INGRESSO.sav USCITA.sav --verifica-soltanto
"""

import argparse
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emerald_bag_decode import (  # noqa: E402
    u16, checksum_prefix, read_slot, assemble, detect_game,
    GAMES, SECTOR_SIZE, SECTORS_PER_SLOT, OFF_CHECKSUM,
)
from emerald_event_flags_decode import (  # noqa: E402
    OFF_FLAGS, OFF_VARS, VARS_START, flag_get, var_get,
)

SECTOR_DATA_SIZE = 3968

# Verificati su include/constants/flags.h e include/constants/vars.h di pret/pokeemerald
# il 2026-09-21: FLAG_SYS_RESET_RTC_ENABLE = SYSTEM_FLAGS (0x860) + 0x62 = 0x8C2;
# VAR_RESET_RTC_ENABLE = 0x402C. Il valore atteso, 0x920, e' quello che EnableResetRTC()
# scrive in src/event_data.c.
FLAG_SYS_RESET_RTC_ENABLE = 0x8C2
VAR_RESET_RTC_ENABLE = 0x402C
VALORE_ABILITATO = 0x920


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

    flag_prima = flag_get(sb1, FLAG_SYS_RESET_RTC_ENABLE)
    var_prima = var_get(sb1, VAR_RESET_RTC_ENABLE)
    if flag_prima and var_prima == VALORE_ABILITATO:
        raise SystemExit("il permesso di reset RTC è già acceso: nessuna scrittura da fare. "
                          "Se il menu in gioco non compare, il problema è altrove.")

    off_flag_sb1 = OFF_FLAGS + (FLAG_SYS_RESET_RTC_ENABLE >> 3)
    bit = 1 << (FLAG_SYS_RESET_RTC_ENABLE & 7)
    off_var_sb1 = OFF_VARS + (VAR_RESET_RTC_ENABLE - VARS_START) * 2

    sec_flag = 1 + off_flag_sb1 // SECTOR_DATA_SIZE
    sec_var = 1 + off_var_sb1 // SECTOR_DATA_SIZE
    if sec_flag != sec_var:
        raise SystemExit("il flag e la costante non stanno nella stessa sezione: "
                          "lo strumento non gestisce questo caso, verificare gli offset")

    sec_pos = slot["sezioni"][sec_flag]["posizione"]
    base = slot_index * SECTORS_PER_SLOT * SECTOR_SIZE
    sec_off_file = base + sec_pos * SECTOR_SIZE
    sec_len = slot["sezioni"][sec_flag]["lunghezza_checksum"]
    sec_full = bytearray(blob[sec_off_file:sec_off_file + SECTOR_SIZE])

    off_flag_sec = off_flag_sb1 % SECTOR_DATA_SIZE
    off_var_sec = off_var_sb1 % SECTOR_DATA_SIZE
    sec_full[off_flag_sec] |= bit
    struct.pack_into("<H", sec_full, off_var_sec, VALORE_ABILITATO)

    vecchio_cs = u16(sec_full, OFF_CHECKSUM)
    nuovo_cs = ricalcola_checksum(sec_full, sec_len)

    print("Slot scelto: %d, sezione %d" % (slot_index, sec_flag))
    print("FLAG_SYS_RESET_RTC_ENABLE: %s -> True" % flag_prima)
    print("VAR_RESET_RTC_ENABLE: 0x%04X -> 0x%04X" % (var_prima, VALORE_ABILITATO))
    print("Checksum sezione %d: 0x%04X -> 0x%04X" % (sec_flag, vecchio_cs, nuovo_cs))
    print("\nDopo la scrittura: alla console, schermata del titolo, tenere Sinistra+Select+B,")
    print("premere A per confermare, NON toccare i giorni, solo ora e minuti, poi salvare.")

    if args.verifica_soltanto:
        print("\n--verifica-soltanto: nessun file scritto")
        return 0

    blob[sec_off_file:sec_off_file + SECTOR_SIZE] = sec_full
    with open(args.output, "wb") as fh:
        fh.write(blob)
    print("\nScritto: %s" % args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
