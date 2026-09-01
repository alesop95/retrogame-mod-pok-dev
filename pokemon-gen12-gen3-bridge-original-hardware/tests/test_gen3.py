# -*- coding: utf-8 -*-
"""Prove sulla struttura di generazione 3, cioè cifratura, permutazione e checksum.

La prova portante resta la simmetria, ma qui va formulata in due versioni invece di una,
e la ragione è il checksum. Uno scrittore corretto ricalcola il checksum, quindi su un
buffer casuale, il cui checksum non torna quasi mai, la riscrittura differisce
dall'originale in due byte per un motivo giusto. Le due versioni separano le due cose che
la simmetria deve dimostrare: che nessun bit va perso nella lettura, e che il checksum
calcolato dallo scrittore è lo stesso che il lettore considera valido.
"""

import itertools
import random
import unittest

from pokebridge import gb
from pokebridge.gen3 import (Attacks, EvsCondition, Gen3Mon, Growth, Misc,
                             BOX_STRUCT_LENGTH, OFF_SECURE, PARTY_STRUCT_LENGTH,
                             SECURE_LENGTH, SUBSTRUCT_LENGTH, SUBSTRUCT_POSITIONS,
                             compute_checksum, crypt_key, crypt_secure, substruct_order,
                             u16, u32, put_u16, put_u32)


def blob(rng, size):
    return bytes(rng.randrange(256) for _ in range(size))


def normalizza(raw):
    """Riscrive il checksum di un buffer perché corrisponda ai suoi dati.

    Serve a costruire buffer casuali ma validi: senza questo, la simmetria col percorso di
    default fallirebbe sul checksum e non su un errore vero.
    """
    mon = Gen3Mon.from_bytes(raw)
    buf = bytearray(raw)
    put_u16(buf, 0x1C, mon.checksum_computed)
    return bytes(buf)


class TestSimmetria(unittest.TestCase):
    """Nessun bit va perso, e il checksum dello scrittore è quello del lettore."""

    def test_box_mon_conservando_il_checksum(self):
        rng = random.Random(20260826)
        for _ in range(500):
            raw = blob(rng, BOX_STRUCT_LENGTH)
            mon = Gen3Mon.from_bytes(raw)
            self.assertEqual(mon.to_bytes(preserve_checksum=True), raw)

    def test_party_mon_conservando_il_checksum(self):
        rng = random.Random(11)
        for _ in range(500):
            raw = blob(rng, PARTY_STRUCT_LENGTH)
            mon = Gen3Mon.from_bytes(raw)
            self.assertEqual(mon.to_bytes(preserve_checksum=True), raw)

    def test_box_mon_su_buffer_validi(self):
        # Percorso di default, cioè checksum ricalcolato: su un buffer il cui checksum è
        # coerente la riscrittura deve essere identica byte per byte.
        rng = random.Random(12)
        for _ in range(500):
            raw = normalizza(blob(rng, BOX_STRUCT_LENGTH))
            self.assertEqual(Gen3Mon.from_bytes(raw).to_bytes(), raw)

    def test_party_mon_su_buffer_validi(self):
        rng = random.Random(13)
        for _ in range(500):
            raw = normalizza(blob(rng, PARTY_STRUCT_LENGTH))
            self.assertEqual(Gen3Mon.from_bytes(raw).to_bytes(), raw)

    def test_le_sottostrutture_sono_simmetriche_da_sole(self):
        rng = random.Random(14)
        for tipo in (Growth, Attacks, EvsCondition, Misc):
            for _ in range(200):
                raw = blob(rng, SUBSTRUCT_LENGTH)
                self.assertEqual(tipo.from_bytes(raw).to_bytes(), raw,
                                 "asimmetria in %s" % tipo.__name__)

    def test_i_campi_di_riempimento_sopravvivono(self):
        # Growth.filler e i quattro bit unusedRibbons sono i due posti dove un lettore
        # distratto perde informazione senza che nessun campo nominato se ne accorga.
        raw = bytearray(BOX_STRUCT_LENGTH)
        put_u32(raw, 0x00, 0)          # personalità 0, permutazione GAEM, chiave 0
        put_u32(raw, 0x04, 0)
        put_u16(raw, 0x20 + 10, 0xBEEF)             # Growth.filler, slot 0
        put_u32(raw, 0x20 + 3 * SUBSTRUCT_LENGTH + 8, 0x78000000)  # unusedRibbons = 0xF
        mon = Gen3Mon.from_bytes(bytes(raw))
        self.assertEqual(mon.growth.filler, 0xBEEF)
        self.assertEqual(mon.misc.unused_ribbons, 0x0F)
        self.assertEqual(mon.to_bytes(preserve_checksum=True), bytes(raw))


class TestCifratura(unittest.TestCase):

    def test_la_chiave_e_lo_xor_dei_due_valori(self):
        self.assertEqual(crypt_key(0x12345678, 0x9ABCDEF0), 0x12345678 ^ 0x9ABCDEF0)

    def test_e_involutiva(self):
        rng = random.Random(15)
        for _ in range(200):
            raw = blob(rng, SECURE_LENGTH)
            pv, ot = rng.randrange(1 << 32), rng.randrange(1 << 32)
            self.assertEqual(crypt_secure(crypt_secure(raw, pv, ot), pv, ot), raw)

    def test_agisce_su_parole_da_32_bit_e_non_su_byte(self):
        # Con una chiave asimmetrica nei suoi quattro byte, uno XOR byte per byte darebbe
        # un risultato diverso: è l'errore che i test costruiti a mano non catturano.
        raw = bytes(SECURE_LENGTH)
        out = crypt_secure(raw, 0x000000FF, 0)
        self.assertEqual(out[0:4], b"\xFF\x00\x00\x00")
        self.assertNotEqual(out[0:4], b"\xFF\xFF\xFF\xFF")

    def test_chiave_nulla_lascia_i_byte_intatti(self):
        rng = random.Random(16)
        raw = blob(rng, SECURE_LENGTH)
        # personalità e ID uguali danno chiave zero, che è un caso reale e non teorico.
        self.assertEqual(crypt_secure(raw, 0x1234, 0x1234), raw)

    def test_rifiuta_un_blocco_di_lunghezza_sbagliata(self):
        with self.assertRaises(gb.FormatError):
            crypt_secure(bytes(47), 0, 0)


class TestPermutazione(unittest.TestCase):

    def test_ventiquattro_righe_tutte_permutazioni(self):
        self.assertEqual(len(SUBSTRUCT_POSITIONS), 24)
        for riga in SUBSTRUCT_POSITIONS:
            self.assertEqual(sorted(riga), [0, 1, 2, 3])
        self.assertEqual(len(set(SUBSTRUCT_POSITIONS)), 24)

    def test_coincide_con_la_tabella_della_referenza(self):
        # La sezione 5 di DATA-FORMATS elenca l'ordine per slot; il sorgente elenca la
        # posizione per tipo. Le due devono essere trasposte l'una dell'altra: se un giorno
        # divergono, una delle due è stata trascritta male.
        attesi = ("GAEM", "GAME", "GEAM", "GEMA", "GMAE", "GMEA",
                  "AGEM", "AGME", "AEGM", "AEMG", "AMGE", "AMEG",
                  "EGAM", "EGMA", "EAGM", "EAMG", "EMGA", "EMAG",
                  "MGAE", "MGEA", "MAGE", "MAEG", "MEGA", "MEAG")
        for pv in range(24):
            self.assertEqual(substruct_order(pv), attesi[pv], "riga %d" % pv)

    def test_e_l_enumerazione_lessicografica(self):
        # Proprietà osservata e non dichiarata da alcuna fonte: le ventiquattro righe sono
        # esattamente le permutazioni di GAEM in ordine lessicografico su quell'alfabeto.
        # Non la si usa al posto della tabella, che resta il dato: la si verifica, perché
        # una regolarità verificata rende evidente un eventuale errore di trascrizione.
        lessicografiche = ["".join(p) for p in itertools.permutations("GAEM")]
        self.assertEqual([substruct_order(pv) for pv in range(24)], lessicografiche)

    def test_dipende_solo_dal_modulo_24(self):
        self.assertEqual(substruct_order(7), substruct_order(7 + 24 * 1000))

    def test_la_permutazione_e_effettiva_nel_buffer(self):
        # Due valori di personalità con lo stesso resto darebbero lo stesso ordine; questi
        # due hanno resti diversi, quindi la stessa specie deve finire in slot diversi.
        mon0 = Gen3Mon(personality=0, growth=Growth(species=0x0181))
        mon6 = Gen3Mon(personality=6, growth=Growth(species=0x0181))
        self.assertEqual(substruct_order(0), "GAEM")
        self.assertEqual(substruct_order(6), "AGEM")
        # Il blocco va decifrato prima di guardarlo: con personalità 6 e ID nullo la
        # chiave è 6, non zero, e leggere i byte cifrati darebbe 0x0187 al posto di 0x0181.
        for mon, slot in ((mon0, 0), (mon6, 1)):
            raw = mon.to_bytes(party=False)
            plain = crypt_secure(raw[0x20:0x20 + SECURE_LENGTH], mon.personality, mon.ot_id)
            self.assertEqual(u16(plain, slot * SUBSTRUCT_LENGTH), 0x0181,
                             "Growth atteso nello slot %d" % slot)


class TestChecksum(unittest.TestCase):

    def test_somma_parole_da_16_bit_e_non_byte(self):
        # Il caso che distingue le due letture: un solo 0xFFFF vale 65535 sommando parole e
        # 510 sommando byte. La fonte secondaria che dice byte per byte sbaglia qui.
        plain = bytearray(SECURE_LENGTH)
        put_u16(plain, 0, 0xFFFF)
        self.assertEqual(compute_checksum(bytes(plain)), 0xFFFF)

    def test_tronca_a_16_bit(self):
        plain = bytearray(SECURE_LENGTH)
        for i in range(0, SECURE_LENGTH, 2):
            put_u16(plain, i, 0xFFFF)
        # Ventiquattro volte 0xFFFF fa 0x17FFE8, che troncato a 16 bit è 0xFFE8.
        self.assertEqual(24 * 0xFFFF & 0xFFFF, 0xFFE8)
        self.assertEqual(compute_checksum(bytes(plain)), 0xFFE8)

    def test_non_dipende_dall_ordine_delle_sottostrutture(self):
        # Proprietà dichiarata nel docstring di compute_checksum: la somma è commutativa,
        # quindi il checksum si verifica senza sapere quale permutazione sia in uso.
        rng = random.Random(17)
        blocchi = [blob(rng, SUBSTRUCT_LENGTH) for _ in range(4)]
        atteso = compute_checksum(b"".join(blocchi))
        for perm in itertools.permutations(range(4)):
            self.assertEqual(compute_checksum(b"".join(blocchi[i] for i in perm)), atteso)

    def test_lo_scrittore_produce_un_checksum_che_il_lettore_accetta(self):
        rng = random.Random(18)
        for _ in range(200):
            mon = Gen3Mon.from_bytes(blob(rng, BOX_STRUCT_LENGTH))
            riletto = Gen3Mon.from_bytes(mon.to_bytes())
            self.assertTrue(riletto.checksum_ok)

    def test_un_buffer_corrotto_e_segnalato_e_non_rifiutato(self):
        mon = Gen3Mon(personality=1, growth=Growth(species=1))
        raw = bytearray(mon.to_bytes(party=False))
        raw[0x1C] ^= 0xFF
        guasto = Gen3Mon.from_bytes(bytes(raw))
        self.assertFalse(guasto.checksum_ok)
        # E il dato resta leggibile, che è il punto: è ciò che permette di diagnosticare.
        self.assertEqual(guasto.growth.species, 1)

    def test_nessun_checksum_memorizzato_da_None(self):
        self.assertIsNone(Gen3Mon(personality=3).checksum_ok)

    def test_preserve_checksum_senza_checksum_e_un_errore(self):
        with self.assertRaises(gb.FormatError):
            Gen3Mon(personality=3).to_bytes(party=False, preserve_checksum=True)

    def test_refresh_checksum_riallinea(self):
        mon = Gen3Mon.from_bytes(bytes(BOX_STRUCT_LENGTH))
        mon.growth.species = 0x0097
        self.assertFalse(mon.checksum_ok)
        mon.refresh_checksum()
        self.assertTrue(mon.checksum_ok)


class TestValoreDiPersonalita(unittest.TestCase):

    def test_non_si_modifica_dopo_la_costruzione(self):
        mon = Gen3Mon(personality=0x12345678)
        with self.assertRaises(gb.FormatError):
            mon.personality = 0
        self.assertEqual(mon.personality, 0x12345678)

    def test_gli_altri_campi_restano_modificabili(self):
        mon = Gen3Mon(personality=1)
        mon.markings = 0x0F
        self.assertEqual(mon.markings, 0x0F)

    def test_with_personality_ricompone_e_non_muta_l_originale(self):
        mon = Gen3Mon(personality=0, growth=Growth(species=0x0025))
        clone = mon.with_personality(6)
        self.assertEqual(mon.personality, 0)
        self.assertEqual(clone.personality, 6)
        self.assertEqual(clone.growth.species, 0x0025)
        self.assertNotEqual(mon.substruct_order, clone.substruct_order)

    def test_with_personality_scarta_il_checksum_vecchio(self):
        mon = Gen3Mon.from_bytes(bytes(BOX_STRUCT_LENGTH))
        self.assertIsNotNone(mon.checksum_stored)
        self.assertIsNone(mon.with_personality(5).checksum_stored)

    def test_natura_e_il_modulo_25(self):
        # Non è memorizzata da nessuna parte: è il primo campo di Gen 3 che una
        # conversione deve produrre scegliendo il valore di personalità.
        self.assertEqual(Gen3Mon(personality=0).nature_index, 0)
        self.assertEqual(Gen3Mon(personality=26).nature_index, 1)


class TestCampiDiBit(unittest.TestCase):

    def test_iv_sei_campi_da_cinque_bit(self):
        raw = bytearray(SUBSTRUCT_LENGTH)
        # Tutti gli IV a 31 e i due flag alti spenti.
        put_u32(raw, 4, 0x3FFFFFFF)
        misc = Misc.from_bytes(bytes(raw))
        self.assertEqual(set(misc.ivs.values()), {31})
        self.assertFalse(misc.is_egg)
        self.assertEqual(misc.ability_num, 0)

    def test_flag_uovo_e_slot_abilita_sono_i_due_bit_alti(self):
        raw = bytearray(SUBSTRUCT_LENGTH)
        put_u32(raw, 4, 0xC0000000)
        misc = Misc.from_bytes(bytes(raw))
        self.assertTrue(misc.is_egg)
        self.assertEqual(misc.ability_num, 1)
        self.assertEqual(set(misc.ivs.values()), {0})

    def test_origini_quattro_campi_in_una_parola(self):
        # Livello 50, Smeraldo, Poke Ball 4, allenatore femmina.
        origins = 50 | (3 << 7) | (4 << 11) | (1 << 15)
        raw = bytearray(SUBSTRUCT_LENGTH)
        put_u16(raw, 2, origins)
        misc = Misc.from_bytes(bytes(raw))
        self.assertEqual(misc.met_level, 50)
        self.assertEqual(misc.met_game, 3)
        self.assertEqual(misc.origin_game_name, "Smeraldo")
        self.assertEqual(misc.pokeball, 4)
        self.assertTrue(misc.ot_female)

    def test_pokerus_due_nibble_come_in_gen2(self):
        raw = bytearray(SUBSTRUCT_LENGTH)
        raw[0] = 0x43
        misc = Misc.from_bytes(bytes(raw))
        self.assertEqual(misc.pokerus_strain, 4)
        self.assertEqual(misc.pokerus_days, 3)

    def test_nastri_da_gara_a_tre_bit(self):
        raw = bytearray(SUBSTRUCT_LENGTH)
        put_u32(raw, 8, 0x7 | (0x3 << 3))
        misc = Misc.from_bytes(bytes(raw))
        self.assertEqual(misc.contest_ribbons["cool"], 7)
        self.assertEqual(misc.contest_ribbons["beauty"], 3)
        self.assertEqual(misc.contest_ribbons["cute"], 0)

    def test_nastri_di_merito_e_incontro_fatidico(self):
        raw = bytearray(SUBSTRUCT_LENGTH)
        put_u32(raw, 8, (1 << 15) | (1 << 31))
        misc = Misc.from_bytes(bytes(raw))
        self.assertTrue(misc.has_merit_ribbon("champion"))
        self.assertFalse(misc.has_merit_ribbon("winning"))
        self.assertTrue(misc.modern_fateful_encounter)

    def test_rifiuta_iv_fuori_intervallo(self):
        misc = Misc()
        misc.ivs["hp"] = 32
        with self.assertRaises(gb.FormatError):
            misc.to_bytes()

    def test_rifiuta_livello_di_incontro_fuori_intervallo(self):
        with self.assertRaises(gb.FormatError):
            Misc(met_level=128).to_bytes()

    def test_pp_up_due_bit_per_mossa(self):
        # In Gen 2 PP e PP Up stanno nello stesso byte; qui sono in sottostrutture diverse.
        growth = Growth(pp_bonuses=0b11_10_01_00)
        self.assertEqual([growth.pp_bonus(i) for i in range(4)], [0, 1, 2, 3])
        with self.assertRaises(gb.FormatError):
            growth.pp_bonus(4)


class TestDimensioniEFlag(unittest.TestCase):

    def test_costanti(self):
        self.assertEqual(BOX_STRUCT_LENGTH, 80)
        self.assertEqual(PARTY_STRUCT_LENGTH, 100)
        self.assertEqual(PARTY_STRUCT_LENGTH - BOX_STRUCT_LENGTH, 20)
        self.assertEqual(SECURE_LENGTH, 4 * SUBSTRUCT_LENGTH)

    def test_ordine_dei_byte_opposto_a_quello_di_gen1_e_gen2(self):
        # La differenza che rende sbagliato riusare i primitivi di gb.py.
        raw = b"\x01\x02"
        self.assertEqual(u16(raw, 0), 0x0201)
        self.assertEqual(gb.u16(raw, 0), 0x0102)

    def test_flag_dal_byte_a_0x13(self):
        raw = bytearray(BOX_STRUCT_LENGTH)
        raw[0x13] = 0x0F
        mon = Gen3Mon.from_bytes(bytes(raw))
        self.assertTrue(mon.is_bad_egg)
        self.assertTrue(mon.has_species)
        self.assertTrue(mon.is_egg)
        self.assertTrue(mon.block_box_rs)
        raw[0x13] = 0x02
        mon = Gen3Mon.from_bytes(bytes(raw))
        self.assertFalse(mon.is_bad_egg)
        self.assertTrue(mon.has_species)

    def test_lucentezza_e_un_conto_sui_32_bit(self):
        # Con ID e personalità nulli lo XOR è zero, quindi sotto la soglia di 8.
        self.assertTrue(Gen3Mon(personality=0, ot_id=0).is_shiny)
        self.assertFalse(Gen3Mon(personality=0, ot_id=0x00000100).is_shiny)

    def test_una_struttura_di_box_non_si_riscrive_come_squadra(self):
        mon = Gen3Mon.from_bytes(bytes(BOX_STRUCT_LENGTH))
        self.assertFalse(mon.is_party)
        with self.assertRaises(gb.FormatError):
            mon.to_bytes(party=True)

    def test_lunghezza_ambigua_rifiutata(self):
        with self.assertRaises(gb.FormatError):
            Gen3Mon.from_bytes(bytes(90))

    def test_nomi_di_lunghezza_sbagliata_rifiutati(self):
        mon = Gen3Mon(personality=1)
        mon.nickname = b"corto"
        with self.assertRaises(gb.FormatError):
            mon.to_bytes(party=False)

    def test_i_nomi_restano_byte_e_non_diventano_testo(self):
        # Come in gen1 e gen2: la transcodifica sta in charmap.py, e tenerla fuori da qui
        # è ciò che rende possibile la simmetria byte-perfetta.
        raw = bytearray(BOX_STRUCT_LENGTH)
        raw[0x08:0x12] = bytes(range(0xB0, 0xBA))
        mon = Gen3Mon.from_bytes(bytes(raw))
        self.assertIsInstance(mon.nickname, bytes)
        self.assertEqual(mon.nickname, bytes(range(0xB0, 0xBA)))

    def test_i_nomi_sono_piu_corti_che_in_gen1_e_gen2(self):
        # Vincolo vero della conversione: undici byte a monte, dieci e sette a valle.
        from pokebridge.gen3 import NICKNAME_LENGTH, OT_NAME_LENGTH
        self.assertEqual(gb.NAME_LENGTH, 11)
        self.assertEqual(NICKNAME_LENGTH, 10)
        self.assertEqual(OT_NAME_LENGTH, 7)


class TestStatisticheDiSquadra(unittest.TestCase):

    def test_sette_statistiche_nei_venti_byte_in_piu(self):
        rng = random.Random(19)
        raw = bytearray(blob(rng, PARTY_STRUCT_LENGTH))
        mon = Gen3Mon.from_bytes(bytes(raw))
        self.assertEqual(len(mon.stats), 7)
        self.assertEqual(mon.stats["hp"], u16(raw, 0x56))
        self.assertEqual(mon.stats["sdef"], u16(raw, 0x56 + 12))
        self.assertEqual(mon.status, u32(raw, 0x50))

    def test_sei_iv_contro_quattro_dv(self):
        # L'asimmetria che rende non banale la conversione: a monte quattro DV e cinque
        # Stat Experience con un solo Speciale, a valle sei IV e sei EV.
        mon = Gen3Mon(personality=1)
        self.assertEqual(len(mon.misc.ivs), 6)
        self.assertEqual(len(mon.evs.evs), 6)
        self.assertEqual(len(gb.DV_ORDER), 4)
        self.assertEqual(len(gb.STAT_EXP_ORDER), 5)

    def test_nessuna_posta_e_0xff(self):
        from pokebridge.gen3 import NO_MAIL
        raw = bytearray(PARTY_STRUCT_LENGTH)
        raw[0x55] = NO_MAIL
        self.assertEqual(Gen3Mon.from_bytes(bytes(raw)).mail, 0xFF)

    def test_somma_degli_ev(self):
        ev = EvsCondition()
        ev.evs["hp"] = 252
        ev.evs["atk"] = 252
        ev.evs["spd"] = 6
        self.assertEqual(ev.ev_total, 510)


if __name__ == "__main__":
    unittest.main()


class TestFormaCanonica(unittest.TestCase):
    """La forma decifrata a ordine fisso, cioè il formato di scambio.

    La prova portante è di nuovo la simmetria, ma qui va formulata su tre percorsi invece di
    uno, perché esistono due forme e quattro conversioni possibili fra esse. Un errore in una
    sola direzione passerebbe inosservato su una prova che ne verifichi due.
    """

    def setUp(self):
        self.rng = random.Random(20260901)

    def buffer_valido(self, party=False):
        lunghezza = PARTY_STRUCT_LENGTH if party else BOX_STRUCT_LENGTH
        return normalizza(blob(self.rng, lunghezza))

    def test_simmetria_della_forma_canonica(self):
        for party in (False, True):
            for _ in range(40):
                raw = self.buffer_valido(party)
                mon = Gen3Mon.from_bytes(raw)
                canonica = mon.to_canonical_bytes(party=party)
                riletto = Gen3Mon.from_canonical_bytes(canonica, party=party)
                self.assertEqual(riletto.to_canonical_bytes(party=party), canonica)

    def test_le_due_forme_si_convertono_a_vicenda(self):
        """Dalla forma del salvataggio alla canonica e ritorno si torna agli stessi byte."""
        for party in (False, True):
            for _ in range(40):
                raw = self.buffer_valido(party)
                mon = Gen3Mon.from_bytes(raw)
                canonica = mon.to_canonical_bytes(party=party)
                ritorno = Gen3Mon.from_canonical_bytes(canonica, party=party)
                self.assertEqual(ritorno.to_bytes(party=party), mon.to_bytes(party=party))

    def test_l_intestazione_e_il_checksum_non_cambiano(self):
        """I primi trentadue byte sono identici nelle due forme, checksum compreso.

        Se cambiassero, il checksum della forma canonica sarebbe calcolato sull'ordine fisso
        e non su quello permutato, che è il modo di produrre un file che nessuno strumento
        accetta e di non capire perché.
        """
        for _ in range(20):
            mon = Gen3Mon.from_bytes(self.buffer_valido())
            a = mon.to_bytes(party=False)
            b = mon.to_canonical_bytes(party=False)
            self.assertEqual(a[:OFF_SECURE], b[:OFF_SECURE])

    def test_i_quarantotto_byte_centrali_differiscono(self):
        """Il corpo differisce, altrimenti la conversione non sta facendo niente.

        È il controllo negativo della prova precedente: senza di esso una implementazione
        che restituisse gli stessi byte passerebbe tutte le altre prove.
        """
        differiscono = 0
        for _ in range(20):
            mon = Gen3Mon.from_bytes(self.buffer_valido())
            a = mon.to_bytes(party=False)
            b = mon.to_canonical_bytes(party=False)
            if a[OFF_SECURE:] != b[OFF_SECURE:]:
                differiscono += 1
        self.assertEqual(differiscono, 20,
                         "su qualche buffer le due forme coincidono: la cifratura o la "
                         "permutazione non stanno operando")

    def test_le_sottostrutture_stanno_in_chiaro_e_in_ordine(self):
        """Nella forma canonica le quattro sottostrutture si leggono senza decifrare.

        È la proprietà per cui questa forma esiste, e va verificata direttamente invece di
        essere dedotta dalla simmetria: si compone una struttura con valori riconoscibili e
        li si ricerca nei byte alla posizione attesa.
        """
        mon = Gen3Mon(personality=0x12345679, ot_id=0xABCDEF01,
                      growth=Growth(species=0x0199, experience=0x000103F1),
                      attacks=Attacks(moves=[0x0111, 0x0122, 0x0133, 0x0144],
                                      pp=[10, 20, 30, 40]))
        b = mon.to_canonical_bytes(party=False)
        self.assertEqual(u16(b, OFF_SECURE + 0), 0x0199)
        self.assertEqual(u32(b, OFF_SECURE + 4), 0x000103F1)
        self.assertEqual(u16(b, OFF_SECURE + SUBSTRUCT_LENGTH + 0), 0x0111)
        self.assertEqual(list(b[OFF_SECURE + SUBSTRUCT_LENGTH + 8:
                               OFF_SECURE + SUBSTRUCT_LENGTH + 12]), [10, 20, 30, 40])

    def test_lunghezza_sbagliata_rifiutata(self):
        with self.assertRaises(Exception):
            Gen3Mon.from_canonical_bytes(b"\x00" * 64)
