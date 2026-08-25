# -*- coding: utf-8 -*-
"""Prove sulle strutture di generazione 1.

La prova portante e' la simmetria: leggere e riscrivere deve restituire i byte identici.
Una sola proprieta' cattura un intero genere di errori, perche' un offset sbagliato, un
ordine di byte invertito, un nibble letto dalla meta' sbagliata o un campo dimenticato la
rompono tutti. Vedi docs/21-collaudo.md.
"""

import random
import unittest

from pokebridge import gb
from pokebridge.gen1 import Gen1Mon, Gen1PartyList, BOX_STRUCT_LENGTH, PARTY_STRUCT_LENGTH


def blob(rng, size):
    return bytes(rng.randrange(256) for _ in range(size))


class TestSimmetria(unittest.TestCase):
    """Il seme e' fissato: un fallimento e' riproducibile e non capriccioso."""

    def test_party_mon(self):
        rng = random.Random(20260825)
        for _ in range(500):
            raw = blob(rng, PARTY_STRUCT_LENGTH)
            self.assertEqual(Gen1Mon.from_bytes(raw).to_bytes(), raw)

    def test_box_mon(self):
        rng = random.Random(1)
        for _ in range(500):
            raw = blob(rng, BOX_STRUCT_LENGTH)
            self.assertEqual(Gen1Mon.from_bytes(raw).to_bytes(), raw)

    def test_lista_della_squadra(self):
        rng = random.Random(2)
        for _ in range(50):
            raw = blob(rng, Gen1PartyList.TOTAL_LENGTH)
            self.assertEqual(Gen1PartyList.from_bytes(raw).to_bytes(), raw)


class TestDimensioni(unittest.TestCase):

    def test_costanti_dal_disassemblato(self):
        self.assertEqual(BOX_STRUCT_LENGTH, 0x21)
        self.assertEqual(PARTY_STRUCT_LENGTH, 0x2C)

    def test_lista_squadra_e_404_byte(self):
        # 1 contatore + 7 specie + 6*44 strutture + 6*11 nomi OT + 6*11 soprannomi.
        # Vale 0x194: una fonte secondaria riporta "194 byte" leggendo l'esadecimale
        # come decimale, ed e' il tipo di errore che questa asserzione impedisce.
        self.assertEqual(Gen1PartyList.TOTAL_LENGTH, 404)
        self.assertEqual(hex(Gen1PartyList.TOTAL_LENGTH), "0x194")


class TestCampi(unittest.TestCase):
    """Un caso costruito a mano, per verificare che i campi cadano dove devono."""

    def setUp(self):
        raw = bytearray(PARTY_STRUCT_LENGTH)
        raw[0x00] = 0x99            # specie: indice interno 153
        raw[0x01:0x03] = b"\x00\x2A"  # punti salute correnti 42, big-endian
        raw[0x03] = 50              # livello di box
        raw[0x07] = 45              # tasso di cattura
        raw[0x08:0x0C] = bytes([33, 45, 22, 0])
        raw[0x0C:0x0E] = b"\x30\x39"  # ID allenatore 12345
        raw[0x0E:0x11] = b"\x01\x86\xA0"  # esperienza 100000
        raw[0x11:0x13] = b"\xFF\xFF"  # Stat Experience dei punti salute al massimo
        raw[0x1B] = 0xAB            # DV: Attacco 10, Difesa 11
        raw[0x1C] = 0xCD            # DV: Velocita' 12, Speciale 13
        raw[0x1D] = 0xC1            # PP: 1 residuo, 3 PP Up
        raw[0x21] = 50              # livello di squadra
        raw[0x22:0x24] = b"\x00\x64"  # punti salute massimi 100
        self.raw = bytes(raw)
        self.mon = Gen1Mon.from_bytes(self.raw)

    def test_campi_semplici(self):
        self.assertEqual(self.mon.species, 0x99)
        self.assertEqual(self.mon.hp, 42)
        self.assertEqual(self.mon.catch_rate, 45)
        self.assertEqual(self.mon.ot_id, 12345)
        self.assertEqual(self.mon.exp, 100000)
        self.assertEqual(self.mon.moves, [33, 45, 22, 0])

    def test_stat_experience_al_massimo(self):
        self.assertEqual(self.mon.stat_exp["hp"], 65535)

    def test_dv_e_dv_derivato(self):
        self.assertEqual(self.mon.dvs, {"atk": 10, "def": 11, "spd": 12, "spc": 13})
        # ATK 10 pari, DEF 11 dispari, SPD 12 pari, SPC 13 dispari: 4 + 1 = 5
        self.assertEqual(self.mon.hp_dv, 5)

    def test_pp_e_pp_up(self):
        self.assertEqual(self.mon.pp[0], (1, 3))

    def test_doppio_livello(self):
        # Il gioco usa quello di squadra e ricalcola quello di box al deposito: un writer
        # che ne aggiorna solo uno produce un Pokemon che cambia livello.
        self.assertEqual(self.mon.box_level, 50)
        self.assertEqual(self.mon.level, 50)
        self.assertEqual(self.mon.stats["max_hp"], 100)

    def test_e_un_party_mon(self):
        self.assertTrue(self.mon.is_party)

    def test_simmetria_del_caso_costruito(self):
        self.assertEqual(self.mon.to_bytes(), self.raw)


class TestErrori(unittest.TestCase):

    def test_lunghezza_non_riconosciuta(self):
        with self.assertRaises(gb.FormatError):
            Gen1Mon.from_bytes(bytes(40))

    def test_box_mon_non_diventa_party_mon_per_sbaglio(self):
        mon = Gen1Mon.from_bytes(bytes(BOX_STRUCT_LENGTH))
        self.assertFalse(mon.is_party)
        self.assertEqual(len(mon.to_bytes()), BOX_STRUCT_LENGTH)
        with self.assertRaises(gb.FormatError):
            mon.to_bytes(party=True)

    def test_troncamento_di_una_lista(self):
        with self.assertRaises(gb.FormatError):
            Gen1PartyList.from_bytes(bytes(100))


if __name__ == "__main__":
    unittest.main()
