# -*- coding: utf-8 -*-
"""Prove sulle strutture di generazione 2, compresi i campi che non esistono in Gen 1."""

import random
import unittest

from pokebridge import gb
from pokebridge.gen2 import (CaughtData, Gen2Mon, Gen2PartyList,
                             BOX_STRUCT_LENGTH, PARTY_STRUCT_LENGTH)


def blob(rng, size):
    return bytes(rng.randrange(256) for _ in range(size))


class TestSimmetria(unittest.TestCase):

    def test_party_mon(self):
        rng = random.Random(20260825)
        for _ in range(500):
            raw = blob(rng, PARTY_STRUCT_LENGTH)
            self.assertEqual(Gen2Mon.from_bytes(raw).to_bytes(), raw)

    def test_box_mon(self):
        rng = random.Random(3)
        for _ in range(500):
            raw = blob(rng, BOX_STRUCT_LENGTH)
            self.assertEqual(Gen2Mon.from_bytes(raw).to_bytes(), raw)

    def test_lista_della_squadra(self):
        rng = random.Random(4)
        for _ in range(50):
            raw = blob(rng, Gen2PartyList.TOTAL_LENGTH)
            self.assertEqual(Gen2PartyList.from_bytes(raw).to_bytes(), raw)

    def test_il_byte_inutilizzato_sopravvive(self):
        # A 0x21 c'è un byte che il gioco non usa. Se il lettore lo scartasse, la
        # simmetria si romperebbe su un salvataggio reale che lo trova non nullo.
        raw = bytearray(PARTY_STRUCT_LENGTH)
        raw[0x21] = 0x7E
        mon = Gen2Mon.from_bytes(bytes(raw))
        self.assertEqual(mon.unused, 0x7E)
        self.assertEqual(mon.to_bytes(), bytes(raw))


class TestDimensioni(unittest.TestCase):

    def test_costanti(self):
        self.assertEqual(BOX_STRUCT_LENGTH, 32)
        self.assertEqual(PARTY_STRUCT_LENGTH, 48)

    def test_lista_squadra_e_428_byte(self):
        # Corrisponde alla dimensione documentata per le versioni occidentali.
        self.assertEqual(Gen2PartyList.TOTAL_LENGTH, 428)

    def test_riordino_e_non_estensione(self):
        # In Gen 1 l'ID dell'allenatore sta a 0x0C, in Gen 2 a 0x06: le due strutture non
        # si leggono con lo stesso parser e uno scostamento di offset.
        from pokebridge import gen1, gen2
        self.assertNotEqual(gen1.OFF_OT_ID, gen2.OFF_OT_ID)


class TestDatiDiCattura(unittest.TestCase):
    """I due byte densi che solo Cristallo popola."""

    def test_esempio_documentato(self):
        # Livello 5, di giorno, luogo 1, allenatore femmina: 0x85 0x81.
        caught = CaughtData.from_bytes(0x85, 0x81)
        self.assertEqual(caught.time_of_day, 2)
        self.assertEqual(caught.level, 5)
        self.assertTrue(caught.ot_female)
        self.assertEqual(caught.location, 1)

    def test_simmetria_su_tutte_le_combinazioni_di_byte(self):
        for hi in range(256):
            for lo in range(256):
                caught = CaughtData.from_bytes(hi, lo)
                self.assertEqual(caught.to_bytes(), (hi, lo))

    def test_oro_e_argento_non_popolano(self):
        self.assertTrue(CaughtData.from_bytes(0, 0).is_empty)
        self.assertFalse(CaughtData.from_bytes(0x85, 0x81).is_empty)

    def test_rifiuta_campi_fuori_intervallo(self):
        with self.assertRaises(gb.FormatError):
            CaughtData(level=64).to_bytes()
        with self.assertRaises(gb.FormatError):
            CaughtData(location=128).to_bytes()


class TestCampiNuovi(unittest.TestCase):

    def test_pokerus_due_nibble(self):
        raw = bytearray(PARTY_STRUCT_LENGTH)
        raw[0x1C] = 0x43          # ceppo 4, tre giorni residui
        mon = Gen2Mon.from_bytes(bytes(raw))
        self.assertEqual(mon.pokerus_strain, 4)
        self.assertEqual(mon.pokerus_days, 3)

    def test_oggetto_tenuto_dove_gen1_ha_il_tasso_di_cattura(self):
        # È il riuso di posizione che rende il Time Capsule ufficiale generatore di
        # oggetti apparentemente casuali sui Pokemon che salgono da Gen 1.
        raw = bytearray(PARTY_STRUCT_LENGTH)
        raw[0x01] = 0x9E
        self.assertEqual(Gen2Mon.from_bytes(bytes(raw)).held_item, 0x9E)

    def test_amicizia(self):
        raw = bytearray(PARTY_STRUCT_LENGTH)
        raw[0x1B] = 70            # il valore che il PCCS assegna in conversione
        self.assertEqual(Gen2Mon.from_bytes(bytes(raw)).friendship, 70)

    def test_lucentezza_da_dv(self):
        raw = bytearray(PARTY_STRUCT_LENGTH)
        raw[0x15], raw[0x16] = 0xAA, 0xAA   # tutti i DV a 10
        self.assertTrue(Gen2Mon.from_bytes(bytes(raw)).is_shiny)
        raw[0x15] = 0x4A                     # Attacco 4
        self.assertFalse(Gen2Mon.from_bytes(bytes(raw)).is_shiny)

    def test_sei_statistiche_ma_quattro_dv(self):
        # Gen 2 separa Attacco e Difesa Speciale nelle statistiche calcolate, ma DV e
        # Stat Experience restano cinque campi con un solo Speciale: è l'asimmetria che
        # rende non banale la conversione verso i sei IV di Gen 3.
        mon = Gen2Mon.from_bytes(bytes(PARTY_STRUCT_LENGTH))
        self.assertEqual(len(mon.stats), 6)
        self.assertEqual(len(mon.dvs), 4)
        self.assertEqual(len(mon.stat_exp), 5)


if __name__ == "__main__":
    unittest.main()
