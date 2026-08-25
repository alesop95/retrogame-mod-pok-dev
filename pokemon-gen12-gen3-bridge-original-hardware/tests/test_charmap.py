# -*- coding: utf-8 -*-
"""Prove sulla transcodifica del testo, contro le tabelle generate dai disassemblati.

Le sentinelle qui non ripetono quelle del generatore: quelle verificano che la tabella
sia stata letta bene, queste verificano che il codice che la usa la usi bene.
"""

import unittest

from pokebridge.charmap import Charmap, Gen12ToGen3, UntranslatableCharacter


class TestTabelle(unittest.TestCase):

    def setUp(self):
        self.g12 = Charmap.gen12()
        self.g3 = Charmap.gen3()

    def test_valori_di_controllo_gen12(self):
        self.assertEqual(self.g12.terminator, 0x50)
        self.assertEqual(self.g12.space, 0x7F)
        self.assertEqual(self.g12.char_to_byte["A"], 0x80)
        self.assertEqual(self.g12.char_to_byte["Z"], 0x99)
        self.assertEqual(self.g12.char_to_byte["a"], 0xA0)
        self.assertEqual(self.g12.char_to_byte["0"], 0xF6)
        self.assertEqual(self.g12.char_to_byte["9"], 0xFF)

    def test_valori_di_controllo_gen3(self):
        self.assertEqual(self.g3.terminator, 0xFF)
        self.assertEqual(self.g3.space, 0x00)
        self.assertEqual(self.g3.char_to_byte["A"], 0xBB)
        self.assertEqual(self.g3.char_to_byte["Z"], 0xD4)
        self.assertEqual(self.g3.char_to_byte["a"], 0xD5)
        self.assertEqual(self.g3.char_to_byte["0"], 0xA1)
        self.assertEqual(self.g3.char_to_byte["9"], 0xAA)

    def test_le_due_tabelle_sono_incompatibili(self):
        # Nessuna lettera cade sullo stesso byte: e' la ragione per cui la conversione di
        # un nome e' una transcodifica e non una copia.
        collisioni = [c for c in "ABCXYZabcxyz09"
                      if self.g12.char_to_byte[c] == self.g3.char_to_byte[c]]
        self.assertEqual(collisioni, [])

    def test_le_cifre_non_stanno_a_0xF0(self):
        # La fonte secondaria collocava le cifre di Gen 1 a 0xF0: qui e' scritto che non
        # e' vero, cosi' se qualcuno rigenera la tabella da una fonte sbagliata il test
        # lo dice.
        self.assertNotEqual(self.g12.char_to_byte["0"], 0xF0)

    def test_le_maiuscole_gen3_non_stanno_a_0xC1(self):
        self.assertNotEqual(self.g3.char_to_byte["A"], 0xC1)


class TestDecodifica(unittest.TestCase):

    def setUp(self):
        self.g12 = Charmap.gen12()

    def test_decodifica_si_ferma_al_terminatore(self):
        # P i k a t, poi terminatore e riempimento. I byte non sono scritti a mano ma
        # ricavati dalla tabella: la prima stesura di questa prova aveva 0xA4 al posto di
        # 0xA0, cioe' "e" invece di "a", ed e' lo stesso errore silenzioso contro cui il
        # generatore delle tabelle esiste.
        raw = bytes([self.g12.char_to_byte[c] for c in "Pikat"]) + bytes([0x50, 0xFF, 0xFF])
        self.assertEqual(self.g12.decode(raw), "Pikat")

    def test_riempimento_dopo_il_terminatore_e_ignorato(self):
        nome = self.g12.encode("ASH", length=11)
        self.assertEqual(len(nome), 11)
        self.assertEqual(self.g12.decode(nome), "ASH")

    def test_simmetria_su_un_nome(self):
        for testo in ("ASH", "MISTY", "A", "ABCDEFGHIJ"):
            raw = self.g12.encode(testo, length=11)
            self.assertEqual(self.g12.decode(raw), testo)

    def test_troncamento_di_un_nome_troppo_lungo(self):
        raw = self.g12.encode("ABCDEFGHIJKLMNOP", length=11)
        self.assertEqual(len(raw), 11)
        self.assertEqual(self.g12.decode(raw), "ABCDEFGHIJ")

    def test_un_byte_ignoto_non_fa_esplodere_la_decodifica(self):
        # Su un salvataggio corrotto vedere dove sta il byte strano aiuta, un'eccezione no.
        self.assertIn("\\x", self.g12.decode(bytes([0x80, 0x01, 0x50])))


class TestTraduzione(unittest.TestCase):

    def setUp(self):
        self.tr = Gen12ToGen3()
        self.g12 = Charmap.gen12()
        self.g3 = Charmap.gen3()

    def test_un_nome_attraversa_le_due_codifiche(self):
        raw12 = self.g12.encode("ASH", length=11)
        raw3 = self.tr.translate(raw12, length=7)
        self.assertEqual(len(raw3), 7)
        self.assertEqual(self.g3.decode(raw3), "ASH")

    def test_lo_spazio_cambia_byte(self):
        raw12 = self.g12.encode("A B", length=11)
        raw3 = self.tr.translate(raw12, length=7)
        self.assertEqual(self.g3.decode(raw3), "A B")
        self.assertIn(0x00, raw3)      # lo spazio in Gen 3 vale 0x00
        self.assertIn(0x7F, raw12)     # e in Gen 1 e 2 vale 0x7F

    def test_nome_dell_allenatore_troncato_a_sette_byte(self):
        raw12 = self.g12.encode("ABCDEFGHIJ", length=11)
        raw3 = self.tr.translate(raw12, length=7)
        self.assertEqual(self.g3.decode(raw3), "ABCDEFG")

    def test_caratteri_senza_destinazione(self):
        # Cinquantatre byte di Gen 1 e 2 non hanno un corrispondente in Gen 3, e la
        # decisione su cosa farne e' del chiamante: non c'e' un default silenzioso.
        self.assertGreater(len(self.tr.orphans), 0)
        orfano = sorted(self.tr.orphans)[0]
        raw = bytes([0x80, orfano, 0x50])
        with self.assertRaises(UntranslatableCharacter):
            self.tr.translate(raw, length=7)
        salto = self.tr.translate(raw, length=7, on_missing="skip")
        self.assertEqual(self.g3.decode(salto), "A")
        sost = self.tr.translate(raw, length=7, on_missing="replace",
                                 filler=self.g3.char_to_byte["?"])
        self.assertEqual(self.g3.decode(sost), "A?")

    def test_la_traduzione_non_passa_dal_testo(self):
        # Tradurre byte per byte invece di decodificare e ricodificare: una conversione
        # invece di due, e nessun punto intermedio in cui perdere un byte.
        self.assertEqual(self.tr.mapping[self.g12.char_to_byte["A"]],
                         self.g3.char_to_byte["A"])


if __name__ == "__main__":
    unittest.main()
