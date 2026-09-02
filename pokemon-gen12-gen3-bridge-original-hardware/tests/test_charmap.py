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
        # Nessuna lettera cade sullo stesso byte: è la ragione per cui la conversione di
        # un nome è una transcodifica e non una copia.
        collisioni = [c for c in "ABCXYZabcxyz09"
                      if self.g12.char_to_byte[c] == self.g3.char_to_byte[c]]
        self.assertEqual(collisioni, [])

    def test_le_cifre_non_stanno_a_0xF0(self):
        # La fonte secondaria collocava le cifre di Gen 1 a 0xF0: qui è scritto che non
        # è vero, così se qualcuno rigenera la tabella da una fonte sbagliata il test
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
        # 0xA0, cioè "e" invece di "a", ed è lo stesso errore silenzioso contro cui il
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
        """Il taglio avviene alla lunghezza del campo, non a un carattere in meno.

        Questa prova ha cambiato attesa il 2026-09-02, e il motivo va scritto perché la
        modifica di una prova esistente è il momento in cui si può nascondere un errore. La
        versione precedente attendeva dieci caratteri su undici byte, cioè riservava sempre un
        byte al terminatore. Non misurava il formato ma l'implementazione che il progetto aveva
        allora: il codice della implementazione di riferimento, letto in `StringConverter1.cs`,
        scrive il terminatore soltanto se dopo i caratteri resta almeno un byte libero, e in
        `StringConverter3.cs` fa la stessa cosa. La regola è quindi uniforme fra le generazioni,
        e la vecchia attesa era sbagliata.

        Va aggiunto che nella prima e nella seconda generazione il caso non si presenta con i
        nomi reali, perché il limite di lunghezza imposto dal gioco è di sette caratteri per le
        versioni occidentali e di cinque per quelle giapponesi, su un campo di undici byte:
        il terminatore ci sta sempre. È la ragione per cui il difetto è rimasto invisibile qui e
        si è manifestato invece nella terza generazione, dove il nome dell'allenatore può
        riempire esattamente i suoi sette byte.
        """
        raw = self.g12.encode("ABCDEFGHIJKLMNOP", length=11)
        self.assertEqual(len(raw), 11)
        self.assertEqual(self.g12.decode(raw), "ABCDEFGHIJK")
        self.assertNotEqual(raw[10], self.g12.terminator)

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
        # decisione su cosa farne è del chiamante: non c'è un default silenzioso.
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


class ProveNomePieno(unittest.TestCase):
    """Il confine del terminatore, che è la sola parte non ovvia della codifica di un nome.

    Il difetto che queste prove fissano è stato scoperto il 2026-09-02 da una obiezione del
    verificatore esterno su un esemplare il cui nome di allenatore era lungo esattamente quanto
    il campo: veniva scritto con un carattere in meno, e il nome troncato era una parola
    plausibile appartenente a un altro evento.
    """

    def setUp(self):
        self.tabella = Charmap.gen3()

    def test_un_nome_piu_corto_del_campo_porta_il_terminatore(self):
        fuori = self.tabella.encode("MYSTRY", length=7)
        self.assertEqual(len(fuori), 7)
        self.assertEqual(fuori[6], self.tabella.terminator)
        self.assertEqual(self.tabella.decode(fuori), "MYSTRY")

    def test_un_nome_lungo_quanto_il_campo_non_porta_terminatore(self):
        """È il caso che il difetto sbagliava: sette caratteri in sette byte."""
        fuori = self.tabella.encode("WISHMKR", length=7)
        self.assertEqual(len(fuori), 7)
        self.assertNotEqual(fuori[6], self.tabella.terminator)
        self.assertEqual(self.tabella.decode(fuori), "WISHMKR")

    def test_il_controllo_negativo_del_troncamento(self):
        """Il nome pieno non deve coincidere con quello troncato di un carattere.

        Senza questo controllo la prova precedente passerebbe anche con una implementazione che
        tronchi, purché scriva sette byte: ciò che si vuole verificare è che il settimo
        carattere ci sia.
        """
        pieno = self.tabella.encode("WISHMKR", length=7)
        troncato = self.tabella.encode("WISHMK", length=7)
        self.assertNotEqual(pieno, troncato)
        self.assertEqual(self.tabella.decode(troncato), "WISHMK")

    def test_un_nome_piu_lungo_del_campo_si_taglia_alla_lunghezza_del_campo(self):
        fuori = self.tabella.encode("ABCDEFGHI", length=7)
        self.assertEqual(len(fuori), 7)
        self.assertEqual(self.tabella.decode(fuori), "ABCDEFG")

    def test_il_soprannome_segue_la_medesima_regola_su_dieci_byte(self):
        """Le specie con dieci lettere nel nome sono il caso analogo sul campo del soprannome."""
        fuori = self.tabella.encode("CHARMANDER", length=10)
        self.assertEqual(len(fuori), 10)
        self.assertEqual(self.tabella.decode(fuori), "CHARMANDER")


if __name__ == "__main__":
    unittest.main()
