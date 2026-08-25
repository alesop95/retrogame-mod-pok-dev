# -*- coding: utf-8 -*-
"""Prove sui primitivi. Sono le piu' economiche e catturano gli errori piu' silenziosi."""

import unittest

from pokebridge import gb


class TestInteri(unittest.TestCase):

    def test_u16_e_big_endian(self):
        # Il byte piu' significativo viene per primo: 0x01F4 vale 500, non 62465.
        self.assertEqual(gb.u16(bytes([0x01, 0xF4]), 0), 500)

    def test_u24_e_big_endian(self):
        self.assertEqual(gb.u24(bytes([0x01, 0x86, 0xA0]), 0), 100000)

    def test_simmetria_su_tutto_l_intervallo_a_16_bit(self):
        buf = bytearray(2)
        for value in range(0, 0x10000, 97):   # passo primo, copre tutto lo spazio
            gb.put_u16(buf, 0, value)
            self.assertEqual(gb.u16(buf, 0), value)

    def test_simmetria_su_24_bit(self):
        buf = bytearray(3)
        for value in range(0, 0x1000000, 9973):
            gb.put_u24(buf, 0, value)
            self.assertEqual(gb.u24(buf, 0), value)

    def test_rifiuta_valori_fuori_intervallo(self):
        buf = bytearray(4)
        with self.assertRaises(gb.FormatError):
            gb.put_u16(buf, 0, 0x10000)
        with self.assertRaises(gb.FormatError):
            gb.put_u24(buf, 0, -1)


class TestDV(unittest.TestCase):

    def test_ordine_dei_nibble(self):
        # Verificato su pokecrystal, CalcMonStatC: primo byte Attacco alto e Difesa basso,
        # secondo byte Velocita' alta e Speciale basso.
        dvs = gb.unpack_dvs(0xAB, 0xCD)
        self.assertEqual(dvs, {"atk": 0xA, "def": 0xB, "spd": 0xC, "spc": 0xD})

    def test_simmetria_su_tutte_le_combinazioni(self):
        for hi in range(256):
            for lo in range(0, 256, 17):
                dvs = gb.unpack_dvs(hi, lo)
                self.assertEqual(gb.pack_dvs(dvs), (hi, lo))

    def test_dv_dei_punti_salute_dalla_formula_del_disassemblato(self):
        # DV_HP = (ATK&1)<<3 | (DEF&1)<<2 | (SPD&1)<<1 | (SPC&1)
        self.assertEqual(gb.hp_dv({"atk": 15, "def": 15, "spd": 15, "spc": 15}), 15)
        self.assertEqual(gb.hp_dv({"atk": 0, "def": 0, "spd": 0, "spc": 0}), 0)
        self.assertEqual(gb.hp_dv({"atk": 1, "def": 0, "spd": 0, "spc": 0}), 8)
        self.assertEqual(gb.hp_dv({"atk": 0, "def": 1, "spd": 0, "spc": 0}), 4)
        self.assertEqual(gb.hp_dv({"atk": 0, "def": 0, "spd": 1, "spc": 0}), 2)
        self.assertEqual(gb.hp_dv({"atk": 0, "def": 0, "spd": 0, "spc": 1}), 1)
        # Solo la parita' conta: 14 e 0 sono entrambi pari e danno lo stesso contributo.
        self.assertEqual(gb.hp_dv({"atk": 14, "def": 12, "spd": 8, "spc": 2}), 0)

    def test_dv_non_e_un_grado_di_liberta_indipendente(self):
        # Cambiare il DV di Attacco da pari a dispari cambia anche i punti salute.
        base = {"atk": 10, "def": 10, "spd": 10, "spc": 10}
        alt = dict(base, atk=11)
        self.assertNotEqual(gb.hp_dv(base), gb.hp_dv(alt))

    def test_rifiuta_dv_fuori_intervallo(self):
        with self.assertRaises(gb.FormatError):
            gb.pack_dvs({"atk": 16, "def": 0, "spd": 0, "spc": 0})

    def test_lucentezza_gen2(self):
        # Difesa, Velocita' e Speciale a 10, Attacco in un insieme di otto valori.
        self.assertTrue(gb.is_shiny_gen2({"atk": 10, "def": 10, "spd": 10, "spc": 10}))
        self.assertTrue(gb.is_shiny_gen2({"atk": 2, "def": 10, "spd": 10, "spc": 10}))
        self.assertFalse(gb.is_shiny_gen2({"atk": 4, "def": 10, "spd": 10, "spc": 10}))
        self.assertFalse(gb.is_shiny_gen2({"atk": 10, "def": 9, "spd": 10, "spc": 10}))

    def test_conteggio_dei_dv_lucenti(self):
        # Otto valori di Attacco su una sola combinazione degli altri tre: 8 su 65536,
        # cioe' la probabilita' documentata di uno su 8192.
        lucenti = sum(1 for a in range(16) for d in range(16) for s in range(16)
                      for c in range(16)
                      if gb.is_shiny_gen2({"atk": a, "def": d, "spd": s, "spc": c}))
        self.assertEqual(lucenti, 8)
        self.assertEqual(16 ** 4 // lucenti, 8192)


class TestPP(unittest.TestCase):

    def test_simmetria_su_tutti_i_256_byte(self):
        for byte in range(256):
            pp, ups = gb.unpack_pp(byte)
            self.assertEqual(gb.pack_pp(pp, ups), byte)

    def test_divisione_sei_piu_due_bit(self):
        # 0xC1 = 11 000001: tre PP Up e un solo PP residuo.
        self.assertEqual(gb.unpack_pp(0xC1), (1, 3))
        self.assertEqual(gb.unpack_pp(0x3F), (63, 0))

    def test_rifiuta_valori_fuori_intervallo(self):
        with self.assertRaises(gb.FormatError):
            gb.pack_pp(64, 0)
        with self.assertRaises(gb.FormatError):
            gb.pack_pp(0, 4)


class TestNomi(unittest.TestCase):

    def test_simmetria_di_un_array_di_nomi(self):
        names = [bytes([0x80 + i] * gb.NAME_LENGTH) for i in range(6)]
        buf = bytearray(6 * gb.NAME_LENGTH)
        gb.write_name_array(buf, 0, names)
        self.assertEqual(gb.read_name_array(buf, 0, 6), names)

    def test_rifiuta_un_nome_di_lunghezza_sbagliata(self):
        buf = bytearray(gb.NAME_LENGTH)
        with self.assertRaises(gb.FormatError):
            gb.write_name_array(buf, 0, [b"corto"])


if __name__ == "__main__":
    unittest.main()
