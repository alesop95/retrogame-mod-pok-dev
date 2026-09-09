# -*- coding: utf-8 -*-
"""Prove sullo strato del salvataggio di generazione 3.

Le prove che contano qui non sono quelle sull'aritmetica del checksum, che è una somma, ma quelle
sui tre punti dove due implementazioni ragionevoli divergono: la scelta dello slot a parità di
indice, il trattamento di uno slot mai scritto, e la scrittura di un record che cade a cavallo fra
due sezioni. L'ultimo è il più insidioso, perché scrivere come se il buffer fosse contiguo
sovrascriverebbe il piede di una sezione e invaliderebbe lo slot senza che nulla se ne accorga
fino al caricamento nel gioco.
"""

import random
import struct
import unittest

from pokebridge.save3 import (DATI_SEZIONE, DIMENSIONE, FIRMA, OFF_CHECKSUM, OFF_FIRMA,
                              OFF_ID, OFF_INDICE, POSIZIONI, RECORD, SEZIONE,
                              SEZIONI_PER_SLOT, SEZIONI_STORAGE, SLOT, Save3, checksum,
                              crea_vuoto, file_da_record, record_da_file)


class TestChecksum(unittest.TestCase):
    def test_forma_della_somma(self):
        # Una sezione di soli zeri ha checksum zero, e una con una sola parola a uno ha uno:
        # sono i due casi che verificano che la somma sia sulle parole e non sui byte.
        self.assertEqual(0, checksum(bytearray(DATI_SEZIONE)))
        dati = bytearray(DATI_SEZIONE)
        struct.pack_into("<I", dati, 0, 1)
        self.assertEqual(1, checksum(dati))

    def test_riporto_ripiegato(self):
        # Due parole da 0xFFFFFFFF sommano a 0x1FFFFFFFE: i sedici alti valgono 0xFFFF e i bassi
        # 0xFFFE, e la piega dà 0xFFFD. È il caso che dimostra che la piega c'è.
        dati = bytearray(DATI_SEZIONE)
        struct.pack_into("<I", dati, 0, 0xFFFFFFFF)
        struct.pack_into("<I", dati, 4, 0xFFFFFFFF)
        self.assertEqual(0xFFFD, checksum(dati))

    def test_ignora_il_piede(self):
        # Il checksum copre i 3968 byte di dati e non i dodici del piede: scrivere nel piede non
        # deve cambiarlo, altrimenti il valore non sarebbe mai stabile.
        dati = bytearray(SEZIONE)
        primo = checksum(dati)
        struct.pack_into("<I", dati, OFF_FIRMA, FIRMA)
        self.assertEqual(primo, checksum(dati))


class TestStruttura(unittest.TestCase):
    def test_sintetico_valido(self):
        s = crea_vuoto()
        self.assertEqual(0, s.attivo)
        self.assertTrue(s.integro())
        self.assertEqual(SEZIONI_PER_SLOT, len(s.sezioni_valide()))
        self.assertEqual(DIMENSIONE, len(s.to_bytes()))

    def test_slot_mai_scritto(self):
        # Lo slot B del sintetico è tutto zeri, quindi la sua firma non è valida: non deve essere
        # scelto, e il suo indice non deve essere letto come 0xFFFFFFFF o come zero.
        s = crea_vuoto()
        self.assertIsNone(s._indice_slot(1))
        self.assertFalse(s.integro(1))

    def test_parita_vince_b(self):
        # È la regola che la referenza dichiara e il punto dove un'implementazione ingenua
        # sceglierebbe A: a parità di indice vince B.
        s = crea_vuoto(indice=5)
        grezzo = bytearray(s.to_bytes())
        for i in range(SEZIONI_PER_SLOT):
            base = SLOT + i * SEZIONE
            struct.pack_into("<H", grezzo, base + OFF_ID, i)
            struct.pack_into("<I", grezzo, base + OFF_FIRMA, FIRMA)
            struct.pack_into("<I", grezzo, base + OFF_INDICE, 5)
            struct.pack_into("<H", grezzo, base + OFF_CHECKSUM,
                             checksum(grezzo[base:base + DATI_SEZIONE]))
        self.assertEqual(1, Save3(bytes(grezzo)).attivo)
        # E con l'indice di A maggiore di uno, vince A.
        for i in range(SEZIONI_PER_SLOT):
            base = i * SEZIONE
            struct.pack_into("<I", grezzo, base + OFF_INDICE, 6)
            struct.pack_into("<H", grezzo, base + OFF_CHECKSUM,
                             checksum(grezzo[base:base + DATI_SEZIONE]))
        self.assertEqual(0, Save3(bytes(grezzo)).attivo)

    def test_firma_sbagliata_invalida(self):
        s = crea_vuoto()
        grezzo = bytearray(s.to_bytes())
        struct.pack_into("<I", grezzo, OFF_FIRMA, FIRMA ^ 1)
        letto = Save3(bytes(grezzo))
        self.assertFalse(letto.integro())
        self.assertEqual(SEZIONI_PER_SLOT - 1, len(letto.sezioni_valide()))

    def test_gioco_ignoto_rifiutato(self):
        with self.assertRaises(ValueError):
            Save3(bytes(DIMENSIONE), gioco="Verde")


class TestDeposito(unittest.TestCase):
    def test_andata_e_ritorno(self):
        s = crea_vuoto()
        rng = random.Random(7)
        record = bytes(rng.randrange(256) for _ in range(RECORD))
        s.scrivi_posizione(3, record)
        self.assertEqual(record, s.leggi_posizione(3))
        # E dopo la serializzazione il file resta valido, cioè i checksum sono stati rifatti.
        riletto = Save3(s.to_bytes())
        self.assertTrue(riletto.integro())
        self.assertEqual(record, riletto.leggi_posizione(3))

    def test_record_a_cavallo_di_due_sezioni(self):
        # È la prova che giustifica l'aritmetica di `_scrivi_in_buffer`. Con 3968 byte di dati per
        # sezione e record da ottanta, la posizione 49 comincia a 0x0F84 e finisce oltre il
        # confine: metà del record sta nella sezione 5 e metà nella 6.
        s = crea_vuoto()
        indice = 49
        inizio = 0x0004 + indice * RECORD
        self.assertLess(inizio, DATI_SEZIONE)
        self.assertGreater(inizio + RECORD, DATI_SEZIONE)
        record = bytes(range(RECORD))
        s.scrivi_posizione(indice, record)
        self.assertEqual(record, s.leggi_posizione(indice))
        riletto = Save3(s.to_bytes())
        self.assertTrue(riletto.integro(), "la scrittura a cavallo ha rotto una sezione")
        self.assertEqual(record, riletto.leggi_posizione(indice))
        # Controllo negativo: le posizioni vicine non sono state toccate.
        self.assertEqual(bytes(RECORD), riletto.leggi_posizione(indice - 1))
        self.assertEqual(bytes(RECORD), riletto.leggi_posizione(indice + 1))

    def test_tutte_le_posizioni_scrivibili(self):
        # Le 420 posizioni cadono dentro le nove sezioni del deposito: se l'aritmetica sbagliasse
        # sull'ultima, questa prova lo direbbe invece di scoprirlo il gioco.
        s = crea_vuoto()
        marchio = bytes([0xAB]) * RECORD
        for indice in (0, 1, POSIZIONI - 2, POSIZIONI - 1):
            s.scrivi_posizione(indice, marchio)
            self.assertEqual(marchio, s.leggi_posizione(indice))
        riletto = Save3(s.to_bytes())
        self.assertTrue(riletto.integro())
        self.assertEqual(marchio, riletto.leggi_posizione(POSIZIONI - 1))

    def test_posizione_fuori_intervallo(self):
        s = crea_vuoto()
        with self.assertRaises(ValueError):
            s.leggi_posizione(POSIZIONI)
        with self.assertRaises(ValueError):
            s.scrivi_posizione(-1, bytes(RECORD))
        with self.assertRaises(ValueError):
            s.scrivi_posizione(0, bytes(RECORD - 1))

    def test_buffer_del_deposito_ha_la_misura_attesa(self):
        s = crea_vuoto()
        self.assertEqual(len(SEZIONI_STORAGE) * DATI_SEZIONE, len(s.storage()))
        self.assertGreaterEqual(len(s.storage()), 0x83D0)


class TestDueForme(unittest.TestCase):
    """Le prove sulla conversione fra la forma del file e quella del salvataggio.

    Sono qui e non fra le prove di `gen3` perché la distinzione appartiene al confine fra il
    formato in memoria e il contenitore: un file dell'editor è in chiaro e con le sottostrutture
    nell'ordine logico, una posizione del deposito le vuole permutate e cifrate. Scambiare le due
    non produce alcun errore visibile e produce esemplari che il gioco distrugge.
    """

    def _mon(self, personality=0x273B858B, ot_id=0x0000A5A5):
        from pokebridge.gen3 import Gen3Mon
        return Gen3Mon(personality=personality, ot_id=ot_id).to_bytes(party=False)

    def test_le_due_forme_differiscono(self):
        record = self._mon()
        self.assertNotEqual(record, file_da_record(record))

    def test_andata_e_ritorno(self):
        record = self._mon()
        self.assertEqual(record, record_da_file(file_da_record(record)))

    def test_l_intestazione_non_si_tocca(self):
        # I primi trentadue byte, cioè valore di personalità, identificativo, soprannome, nome
        # dell'allenatore e checksum, sono in chiaro in entrambe le forme e non vanno permutati.
        record = self._mon()
        self.assertEqual(record[:0x20], file_da_record(record)[:0x20])

    def test_ogni_permutazione_e_invertibile(self):
        # Le ventiquattro permutazioni si selezionano col resto del valore di personalità: la
        # prova le esercita tutte, perché un errore su una sola riga della tavola colpirebbe un
        # ventiquattresimo del lotto e sarebbe difficile da attribuire.
        for resto in range(24):
            record = self._mon(personality=0x10000000 + resto)
            self.assertEqual(record, record_da_file(file_da_record(record)),
                             "permutazione %d non invertibile" % resto)

    def test_un_buffer_corto_viene_rifiutato(self):
        with self.assertRaises(ValueError):
            record_da_file(bytes(40))
        with self.assertRaises(ValueError):
            file_da_record(bytes(40))


class TestSquadra(unittest.TestCase):
    def test_offset_diversi_fra_i_due_gruppi(self):
        # Non è un dettaglio cosmetico: leggere la squadra all'offset dell'altro gruppo non
        # produce un errore ma sei strutture di rumore, ed è il genere di difetto che si scopre
        # tardi. La prova scrive un conteggio riconoscibile all'offset di Hoenn e verifica che il
        # lettore di Kanto rifatto non lo veda.
        s = crea_vuoto("RSE")
        s._scrivi_in_buffer((1, 2, 3, 4), 0x0234, struct.pack("<I", 3))
        self.assertEqual(3, s.conteggio_squadra())
        altro = Save3(s.to_bytes(), gioco="FRLG")
        self.assertNotEqual(3, altro.conteggio_squadra())

    def test_lettura_di_una_posizione(self):
        s = crea_vuoto("RSE")
        struttura = bytes([0x5A]) * 100
        s._scrivi_in_buffer((1, 2, 3, 4), 0x0238 + 100, struttura)
        self.assertEqual(struttura, s.leggi_squadra(1))
        with self.assertRaises(ValueError):
            s.leggi_squadra(6)


if __name__ == "__main__":
    unittest.main()
