# -*- coding: utf-8 -*-
"""Prove sulla generazione pseudocasuale degli esemplari da evento.

Queste prove sono di natura diversa dalle altre della suite, e vale dirlo perché cambia come
si leggono. Le prove sulla struttura sono di simmetria: costruiscono un dato, lo riscrivono e
verificano che nulla si sia perso, e non hanno bisogno di sapere quale sia il dato giusto.
Queste non possono esserlo, perché il generatore non è invertibile in modo utile e perché la
domanda non è se il codice sia coerente con se stesso ma se riproduca un comportamento
osservato in natura vent'anni fa.

Sono dunque prove su vettori, e i vettori sono fatti. Provengono dal corpus di esemplari
conservati che accompagna il costruttore di esemplari della comunità, e ciascuno porta il
seme di origine accanto al valore di personalità, ai valori individuali e al sesso
dell'allenatore. Quelli riportati qui sono un sottoinsieme scelto per coprire eventi
diversi: la verifica sull'intero corpus la esegue `tools/confronta-ace-builder.py`, che lo
legge da una copia locale non versionata, e questa suite conserva i pochi che bastano a
segnalare una regressione senza dipendere da materiale esterno al repository.

Fra essi c'è la distribuzione italiana del decennale, con l'allenatore che questo progetto
possiede su cartuccia: è il vettore che conta più degli altri, perché è quello su cui il
lavoro verrà misurato.
"""

import unittest

from pokebridge import eventi


# Ogni voce: (evento, seme, valore di personalità, valori individuali nell'ordine del
# generatore, sesso dell'allenatore atteso dove la derivazione è quella a scorrimento di
# sette). I valori individuali sono nell'ordine ps, attacco, difesa, velocità, attacco
# speciale, difesa speciale, che è quello in cui le due estrazioni li producono.
VETTORI = (
    ("10ANNI", 0x00009DF6, 0xD2A8AA71, (31, 31, 25, 28, 30, 25), "maschio"),
    ("10ANNI", 0x0000AF34, 0xEBE49A13, (27, 31, 23, 31, 30, 30), "femmina"),
    ("10ANNI", 0x0000D726, 0x4F4D5D4F, (23, 20, 31, 31, 26, 30), "maschio"),
    ("WISHMKR_BEST", 0x00008BCB, 0xD4D58A45, (28, 28, 30, 21, 30, 29), None),
    ("WISHMKR_BEST", 0x00005ADE, 0xC18ADCC9, (18, 30, 28, 31, 31, 24), None),
    ("WISHMKR_SHINY", 0x0000A030, 0x4633087D, (21, 31, 31, 19, 18, 24), None),
    ("AURA_MEW", 0x00009DF6, 0xD2A8AA71, (31, 31, 25, 28, 30, 25), "maschio"),
)

# Il vettore che il corpus dichiara e che il suo stesso seme non produce. Sta qui come
# controllo negativo: se un giorno il modulo lo riproducesse, non sarebbe un progresso ma il
# segno che qualcuno ha piegato il codice per farlo tornare.
VETTORE_INCOERENTE = ("PARTY_OF_THE_DECADE", 0x0000A823, 0x21943B10,
                      (24, 27, 25, 23, 31, 31))


class ProveGeneratore(unittest.TestCase):

    def test_periodo_del_bit_basso(self):
        """Il bit meno significativo alterna con periodo due, che è la ragione dello scarto.

        Non è una curiosità: è la dimostrazione operativa del perché il gioco usi la metà
        alta. Se il modulo esponesse i bit bassi, chi li usasse otterrebbe una sequenza che
        si ripete due valori dopo.
        """
        stato = 0x12345678
        bassi = []
        for _ in range(8):
            stato = eventi.avanza(stato)
            bassi.append(stato & 1)
        self.assertEqual(bassi, [bassi[i % 2] for i in range(8)])

    def test_estrazioni_negative_rifiutate(self):
        with self.assertRaises(Exception):
            eventi.estrazioni(0, -1)

    def test_estrazioni_deterministiche(self):
        self.assertEqual(eventi.estrazioni(0x1234, 4), eventi.estrazioni(0x1234, 4))

    def test_spacchetta_iv_copre_l_intervallo(self):
        self.assertEqual(eventi.spacchetta_iv(0), (0, 0, 0))
        self.assertEqual(eventi.spacchetta_iv(31 | (31 << 5) | (31 << 10)), (31, 31, 31))


class ProveVettori(unittest.TestCase):

    def test_personalita_riprodotta(self):
        for nome, seme, attesa, _iv, _sesso in VETTORI:
            personalita, _valori = eventi.personalita_e_iv(seme)
            self.assertEqual(personalita, attesa,
                             "%s con seme 0x%08X" % (nome, seme))

    def test_valori_individuali_riprodotti(self):
        for nome, seme, _p, attesi, _sesso in VETTORI:
            _personalita, valori = eventi.personalita_e_iv(seme)
            ottenuti = tuple(valori[k] for k in eventi.ORDINE_IV)
            self.assertEqual(ottenuti, attesi, "%s con seme 0x%08X" % (nome, seme))

    def test_sesso_allenatore_riprodotto(self):
        provati = 0
        for nome, seme, _p, _iv, atteso in VETTORI:
            if atteso is None:
                continue
            self.assertEqual(eventi.sesso_allenatore_rand_s7(seme), atteso,
                             "%s con seme 0x%08X" % (nome, seme))
            provati += 1
        self.assertGreater(provati, 0, "nessun vettore con sesso dichiarato: prova vuota")

    def test_l_inversione_non_e_simmetrica(self):
        """La composizione ordinaria non riproduce i vettori: l'inversione è necessaria.

        Senza questa prova il test precedente passerebbe anche con una implementazione che
        avesse invertito due volte, cioè per niente, su un vettore in cui le due metà si
        somigliano. Qui si verifica che la composizione sbagliata sia effettivamente sbagliata.
        """
        for nome, seme, attesa, _iv, _sesso in VETTORI:
            a, b = eventi.estrazioni(seme, 2)
            ordinaria = ((b << 16) | a) & 0xFFFFFFFF
            if a == b:
                continue
            self.assertNotEqual(ordinaria, attesa,
                                "%s: la composizione ordinaria coincide, vettore inutile"
                                % nome)

    def test_vettore_incoerente_resta_incoerente(self):
        """Il vettore deviante del corpus non si riproduce, e i suoi IV sì.

        È la prova che l'anomalia sta nel dato e non nel modello: dal medesimo seme i valori
        individuali tornano esatti, quindi il seme è quello giusto e il valore di personalità
        scritto accanto non è quello che quel seme produce.
        """
        _nome, seme, dichiarata, iv_attesi = VETTORE_INCOERENTE
        personalita, valori = eventi.personalita_e_iv(seme)
        self.assertNotEqual(personalita, dichiarata)
        self.assertEqual(tuple(valori[k] for k in eventi.ORDINE_IV), iv_attesi)
        self.assertEqual(dichiarata - personalita, 2,
                         "lo scarto atteso è di due unità nella metà bassa")


class ProveRicercaInversa(unittest.TestCase):

    def test_il_seme_di_un_vettore_si_ritrova(self):
        nome, seme, personalita, iv_attesi, _sesso = VETTORI[0]
        _p, valori = eventi.personalita_e_iv(seme)
        trovati = eventi.cerca_seme(personalita, valori)
        self.assertIn(seme, trovati, nome)

    def test_la_ricerca_e_esaustiva_e_non_euristica(self):
        """Su un valore di personalità impossibile la ricerca restituisce l'insieme vuoto.

        Serve a escludere che la funzione restituisca sempre qualcosa: una ricerca che non
        sa dire di no non è una ricerca.
        """
        self.assertEqual(eventi.cerca_seme(0xFFFFFFFF, {"ps": 0, "attacco": 0, "difesa": 0,
                                                        "velocita": 0, "attacco_speciale": 0,
                                                        "difesa_speciale": 0}), [])


if __name__ == "__main__":
    unittest.main()
