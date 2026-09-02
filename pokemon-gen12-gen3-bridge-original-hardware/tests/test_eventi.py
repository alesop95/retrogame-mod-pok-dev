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
from pokebridge import gb


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



class ProveDerivazioniDelSesso(unittest.TestCase):
    """Le nove derivazioni del sesso dell'allenatore di provenienza.

    Le formule vengono dal codice della implementazione di riferimento e non da congettura, e
    queste prove servono a due cose distinte: che ciascuna sia implementata, e che le due con
    una particolarità la conservino. Le due particolarità sono la negazione della derivazione a
    scorrimento di sette e il fatto che quella a scorrimento di quindici legga la sesta
    estrazione anziché la quinta, e una riscrittura che le uniformasse passerebbe le prove
    banali e sbaglierebbe queste.
    """

    def test_le_derivazioni_fisse_non_guardano_il_seme(self):
        for seme in (0x0000, 0x1234, 0x9DF6, 0xFFFF):
            self.assertEqual(eventi.sesso_allenatore("Only0", seme), "maschio")
            self.assertEqual(eventi.sesso_allenatore("Only1", seme), "femmina")
            self.assertEqual(eventi.sesso_allenatore("RandD3_0", seme), "maschio")
            self.assertEqual(eventi.sesso_allenatore("RandD3_1", seme), "femmina")

    def test_la_derivazione_a_scorrimento_di_sette_e_negata(self):
        """Femmina quando il bit vale zero: senza la negazione sbaglia tutti i casi.

        La prova confronta il valore restituito con il bit grezzo, cosicché una
        implementazione che perdesse la negazione fallisca qui e non altrove.
        """
        for seme in (0x0000, 0x1234, 0x9DF6, 0xABCD, 0xFFFF):
            bit = (eventi.estrazioni(seme, 5)[4] >> 7) & 1
            atteso = "femmina" if bit == 0 else "maschio"
            self.assertEqual(eventi.sesso_allenatore("RandS7", seme), atteso)

    def test_la_derivazione_a_scorrimento_di_quindici_legge_la_sesta(self):
        """Legge la sesta estrazione, perché fra gli IV e il sesso si consuma l'oggetto.

        Il controllo negativo è nella seconda parte: su almeno un seme la quinta e la sesta
        estrazione danno esiti diversi, quindi una implementazione che leggesse la quinta
        sarebbe distinguibile da questa.
        """
        for seme in (0x0000, 0x1234, 0x9DF6, 0xFFFF):
            sesta = eventi.estrazioni(seme, 6)[5]
            atteso = "femmina" if (sesta >> 15) & 1 else "maschio"
            self.assertEqual(eventi.sesso_allenatore("RandSG15", seme), atteso)
        diversi = 0
        for seme in range(0, 4096):
            quinta = eventi.estrazioni(seme, 6)[4]
            sesta = eventi.estrazioni(seme, 6)[5]
            if ((quinta >> 15) & 1) != ((sesta >> 15) & 1):
                diversi += 1
        self.assertGreater(diversi, 0, "leggere la quinta invece della sesta sarebbe "
                                       "indistinguibile: la prova non dimostrerebbe nulla")

    def test_la_derivazione_per_divisione_usa_il_quoziente(self):
        for seme in (0x0000, 0x1234, 0x9DF6, 0xFFFF):
            quinta = eventi.estrazioni(seme, 5)[4]
            atteso = "femmina" if ((quinta // 3) & 1) else "maschio"
            self.assertEqual(eventi.sesso_allenatore("RandD3", seme), atteso)

    def test_la_derivazione_a_scorrimento_di_tre(self):
        for seme in (0x0000, 0x1234, 0x9DF6, 0xFFFF):
            quinta = eventi.estrazioni(seme, 5)[4]
            atteso = "femmina" if ((quinta >> 3) & 1) else "maschio"
            self.assertEqual(eventi.sesso_allenatore("RandS3", seme), atteso)

    def test_la_derivazione_dal_ricevente_pretende_il_dato(self):
        self.assertEqual(eventi.sesso_allenatore("Recipient", 0, "femmina"), "femmina")
        with self.assertRaises(Exception):
            eventi.sesso_allenatore("Recipient", 0)

    def test_la_derivazione_non_implementabile_si_dichiara(self):
        """Solleva invece di restituire un valore qualunque.

        È la differenza fra un limite dichiarato e un difetto silenzioso: la fonte stessa non
        verifica quella derivazione con la logica ordinaria, e scrivere un valore inventato
        sarebbe peggio di non scriverlo.
        """
        with self.assertRaises(Exception):
            eventi.sesso_allenatore("RandAlgo", 0x9DF6)

    def test_una_derivazione_sconosciuta_solleva(self):
        with self.assertRaises(Exception):
            eventi.sesso_allenatore("NonEsiste", 0)

    def test_tutte_le_derivazioni_dichiarate_sono_chiamabili(self):
        for d in eventi.DERIVAZIONI_SESSO:
            eventi.sesso_allenatore(d, 0x9DF6, "maschio")


class ProveLucentezza(unittest.TestCase):

    def test_la_soglia_e_otto(self):
        """Cromatico se la somma esclusiva delle quattro parole è minore di otto."""
        # Si costruisce il caso limite: identificativi nulli e le due metà del valore di
        # personalità uguali fra loro danno somma esclusiva nulla, cioè cromatico.
        self.assertTrue(eventi.e_cromatico(0x12341234, 0, 0))
        self.assertFalse(eventi.e_cromatico(0x12345678, 0, 0))

    def test_gli_identificativi_partecipano(self):
        """Il medesimo valore di personalità cambia esito al variare dell'allenatore.

        Serve a escludere una implementazione che ignorasse gli identificativi, la quale
        passerebbe la prova precedente.
        """
        personalita = 0x12341234
        self.assertTrue(eventi.e_cromatico(personalita, 0, 0))
        self.assertFalse(eventi.e_cromatico(personalita, 0x9999, 0))

    def test_il_vettore_del_decennale_non_e_cromatico(self):
        personalita, _iv = eventi.personalita_e_iv(0x9DF6)
        self.assertFalse(eventi.e_cromatico(personalita, 6227, 0))


class ProveRicercaDelSeme(unittest.TestCase):
    """La scelta del seme che soddisfa i vincoli dichiarati dall'evento.

    Esiste perché scegliere un seme senza verificare è un difetto latente: su un evento a
    lucentezza negata un seme sfortunato produce un esemplare cromatico, che nessun
    verificatore accetta, e nulla lo segnalerebbe.
    """

    def test_il_seme_trovato_rispetta_la_lucentezza_negata(self):
        seme = eventi.cerca_seme_per_evento(6227, 0, "Never")
        self.assertIsNotNone(seme)
        personalita, _iv = eventi.personalita_e_iv(seme)
        self.assertFalse(eventi.e_cromatico(personalita, 6227, 0))

    def test_il_seme_trovato_rispetta_la_lucentezza_imposta(self):
        seme = eventi.cerca_seme_per_evento(6227, 0, "Always")
        self.assertIsNotNone(seme)
        personalita, _iv = eventi.personalita_e_iv(seme)
        self.assertTrue(eventi.e_cromatico(personalita, 6227, 0))

    def test_il_vincolo_sul_sesso_e_rispettato(self):
        for atteso in ("maschio", "femmina"):
            seme = eventi.cerca_seme_per_evento(6227, 0, "Never", "RandS7", atteso)
            self.assertIsNotNone(seme, atteso)
            self.assertEqual(eventi.sesso_allenatore("RandS7", seme), atteso)
            personalita, _iv = eventi.personalita_e_iv(seme)
            self.assertFalse(eventi.e_cromatico(personalita, 6227, 0))

    def test_la_dicitura_casuale_non_vincola(self):
        self.assertIsNotNone(eventi.cerca_seme_per_evento(6227, 0, "Random"))

    def test_vincoli_incompatibili_restituiscono_nulla(self):
        """Nessun seme trovato è informazione e non un guasto.

        Si impone un insieme di semi di un solo elemento e un vincolo che quel seme non
        soddisfa: la funzione deve dire di no invece di restituire quel seme.
        """
        personalita, _iv = eventi.personalita_e_iv(0x9DF6)
        self.assertFalse(eventi.e_cromatico(personalita, 6227, 0))
        self.assertIsNone(eventi.cerca_seme_per_evento(6227, 0, "Always", semi=[0x9DF6]))



class ProveQuattroRami(unittest.TestCase):
    """I quattro rami della composizione, e i loro controlli negativi.

    Ogni prova qui porta un controllo negativo, e la ragione e' la stessa in tutti i casi: i
    rami differiscono fra loro per pochi bit o per una estrazione, quindi una prova che accerti
    soltanto il valore giusto non distingue il ramo giusto da uno sbagliato che per caso
    coincide. Il controllo negativo dice che cosa il ramo NON produce.
    """

    # Il vettore che per un giorno e' stato chiamato deviante, e che invece esercita la
    # mutazione antilucente. Vale come prova di regressione piu' di ogni altro, perche' e' il
    # solo esemplare del corpus in cui quel ramo scatta.
    SEME_MUTATO = 0x0000A823
    ID_DECENNALE = 6808
    PERSONALITA_ORDINARIA = 0x21943B0E
    PERSONALITA_MUTATA = 0x21943B10

    def test_mutazione_antilucente_spiega_il_vettore_deviante(self):
        """La differenza di due unita' e' la mutazione, non una incoerenza della fonte."""
        piana = eventi.personalita_invertita(*eventi.estrazioni(self.SEME_MUTATO, 2))
        self.assertEqual(piana, self.PERSONALITA_ORDINARIA)
        self.assertTrue(eventi.e_cromatico_da_xor(piana, self.ID_DECENNALE))
        self.assertEqual(eventi.correggi_antilucente(piana), self.PERSONALITA_MUTATA)

    def test_il_ramo_a_lucentezza_negata_applica_la_mutazione(self):
        """Il ramo intero, non la sola formula: e' cio' che il generatore chiama davvero."""
        personalita, _iv, _stato = eventi.genera(
            "BACD_R_A", self.SEME_MUTATO, "Never", self.ID_DECENNALE)
        self.assertEqual(personalita, self.PERSONALITA_MUTATA)

    def test_senza_il_vincolo_di_lucentezza_lo_stesso_seme_da_il_valore_non_mutato(self):
        """Il controllo negativo del ramo: la mutazione dipende dal vincolo, non dal seme."""
        personalita, _iv, _stato = eventi.genera(
            "BACD_R_A", self.SEME_MUTATO, None, self.ID_DECENNALE)
        self.assertEqual(personalita, self.PERSONALITA_ORDINARIA)
        self.assertNotEqual(personalita, self.PERSONALITA_MUTATA)

    def test_la_mutazione_non_consuma_estrazioni(self):
        """I valori individuali sono gli stessi con e senza mutazione.

        E' il fatto che rendeva il vettore apparentemente incoerente, ed e' invece la prova che
        la mutazione agisce sul valore e non sullo stato del generatore.
        """
        _p1, iv_mutato, _s1 = eventi.genera(
            "BACD_R_A", self.SEME_MUTATO, "Never", self.ID_DECENNALE)
        _p2, iv_piano, _s2 = eventi.genera(
            "BACD_R_A", self.SEME_MUTATO, None, self.ID_DECENNALE)
        self.assertEqual(iv_mutato, iv_piano)

    def test_composizione_diretta_e_invertita_non_coincidono(self):
        """Le due composizioni si distinguono, altrimenti la distinzione sarebbe decorativa."""
        self.assertEqual(eventi.personalita_invertita(0x1234, 0xABCD), 0x1234ABCD)
        self.assertEqual(eventi.personalita_diretta(0x1234, 0xABCD), 0xABCD1234)

    def test_lucentezza_garantita_produce_un_esemplare_cromatico(self):
        """Il ramo che scrive i bit dell'identificativo: la lucentezza non si cerca, si ottiene.

        La prova gira su tutti i semi ammessi del metodo a orologio invece che su uno, perche'
        l'affermazione da verificare e' universale: quel ramo deve produrre un esemplare
        cromatico sempre, non su un seme fortunato.
        """
        id_xor = 30317
        for seme in eventi.semi_ammessi("BACD_RBCD"):
            personalita, _iv, _stato = eventi.genera("BACD_RBCD", seme, "Always", id_xor)
            self.assertTrue(eventi.e_cromatico_da_xor(personalita, id_xor),
                            "il seme %d non ha prodotto un esemplare cromatico" % (seme,))

    def test_la_vecchia_ricerca_non_avrebbe_trovato_quel_valore(self):
        """Il controllo negativo che giustifica l'esistenza del ramo.

        Con la composizione invertita e i semi ammessi dal metodo a orologio nessun valore e'
        cromatico, quindi la vecchia via, che cercava un seme fortunato, avrebbe restituito
        nulla o, peggio, un esemplare non cromatico su un evento che lo dichiara sempre.
        """
        id_xor = 30317
        cromatici = [s for s in eventi.semi_ammessi("BACD_RBCD")
                     if eventi.e_cromatico_da_xor(
                         eventi.personalita_invertita(*eventi.estrazioni(s, 2)), id_xor)]
        self.assertEqual(cromatici, [])

    def test_lucentezza_garantita_consuma_tre_estrazioni(self):
        """I valori individuali vengono dalla quarta e dalla quinta, non dalla terza e quarta.

        Il controllo negativo e' che leggerli dalla terza e dalla quarta dia valori diversi:
        senza di esso la prova non distinguerebbe le due letture.
        """
        seme = 100
        _p, iv, _stato = eventi.genera("BACD_RBCD", seme, "Always", 30317)
        parole = eventi.estrazioni(seme, 5)
        quarta, quinta = parole[3], parole[4]
        atteso = dict(zip(("ps", "attacco", "difesa"), eventi.spacchetta_iv(quarta)))
        atteso.update(zip(("velocita", "attacco_speciale", "difesa_speciale"),
                          eventi.spacchetta_iv(quinta)))
        self.assertEqual(iv, atteso)
        terza = parole[2]
        self.assertNotEqual(eventi.spacchetta_iv(terza), eventi.spacchetta_iv(quarta))

    def test_metodo_delle_uova_scarta_una_estrazione(self):
        """Composizione diretta, poi una estrazione di quadro, poi i valori individuali."""
        seme = 4242
        personalita, iv, _stato = eventi.genera("Method_2", seme, None, 0)
        parole = eventi.estrazioni(seme, 5)
        self.assertEqual(personalita, eventi.personalita_diretta(parole[0], parole[1]))
        atteso = dict(zip(("ps", "attacco", "difesa"), eventi.spacchetta_iv(parole[3])))
        atteso.update(zip(("velocita", "attacco_speciale", "difesa_speciale"),
                          eventi.spacchetta_iv(parole[4])))
        self.assertEqual(iv, atteso)

    def test_ramo_antilucente_non_ristretto_evita_i_bit_nulli(self):
        """La prima estrazione utilizzabile ha almeno un bit oltre il terzo.

        Il controllo negativo e' sul valore prodotto: deve differire dalla composizione
        invertita delle medesime estrazioni, altrimenti il ramo non starebbe facendo nulla.
        """
        seme, id_xor = 777, 30719
        personalita, _iv, _stato = eventi.genera("BACD_U_AX", seme, "Never", id_xor)
        self.assertFalse(eventi.e_cromatico_da_xor(personalita, id_xor))
        piana = eventi.personalita_invertita(*eventi.estrazioni(seme, 2))
        self.assertNotEqual(personalita, piana)


class ProveTabellaQuintoAnniversario(unittest.TestCase):
    """La tabella degli otto doni, che e' aritmetica e non un elenco di dati."""

    # Le quattro specie della tabella, nell'ordine in cui l'aritmetica le mette.
    SPECIE = (172, 371, 359, 280)

    def test_indice_delle_quattro_specie(self):
        """La via aritmetica da' proprio zero, uno, due e tre, nell'ordine della fonte."""
        self.assertEqual([eventi.indice_quinto_anniversario(s) for s in self.SPECIE],
                         [0, 1, 2, 3])

    def test_il_peso_resta_nell_intervallo(self):
        """Mille valori possibili, e nessuno fuori: e' cio' che la funzione promette."""
        for seme in range(0, 0x10000, 997):
            peso = eventi.peso_periodico(eventi.casuale32_tabella(seme),
                                         eventi.PESO_MASSIMO_TABELLA)
            self.assertTrue(0 <= peso < eventi.PESO_MASSIMO_TABELLA)

    def test_il_peso_non_e_un_resto_della_divisione(self):
        """Il controllo negativo che protegge la formula da una semplificazione.

        La tentazione di scrivere un resto della divisione al posto della moltiplicazione a
        precisione estesa e' forte e il risultato sembrerebbe plausibile. Questa prova esiste
        per mostrare che i due non coincidono, cosicche' la semplificazione rompa la suite
        invece di passare inosservata.
        """
        diversi = 0
        for seme in range(0, 0x1000):
            casuale = eventi.casuale32_tabella(seme)
            if (eventi.peso_periodico(casuale, eventi.PESO_MASSIMO_TABELLA)
                    != casuale % eventi.PESO_MASSIMO_TABELLA):
                diversi += 1
        self.assertGreater(diversi, 0)

    def test_ogni_dono_ha_un_seme(self):
        """Per ciascuna delle otto voci esiste un seme che la tabella risolve in quella."""
        for specie in self.SPECIE:
            for desiderio in (False, True):
                seme = eventi.seme_quinto_anniversario(specie, False, desiderio, 1)
                self.assertIsNotNone(seme, "nessun seme per specie %d desiderio %s"
                                     % (specie, desiderio))
                self.assertTrue(eventi.combacia_quinto_anniversario(
                    specie, False, desiderio, seme))

    def test_solo_il_pichu_puo_essere_cromatico(self):
        """La lucentezza appartiene alla tabella, e la tabella la concede a una specie sola."""
        self.assertIsNotNone(eventi.seme_quinto_anniversario(172, True, False, 1))
        for specie in (371, 359, 280):
            self.assertIsNone(eventi.seme_quinto_anniversario(
                specie, True, False, 1, tentativi=0x4000))


class ProveTrasformazioneDelSeme(unittest.TestCase):
    """Cio' che sta fra il numero di partenza e la generazione, caso per caso."""

    def test_il_metodo_a_orologio_restringe_a_duecentoquattordici_valori(self):
        """Il massimo e' la somma delle cifre di un'ora in decimale codificato in binario."""
        self.assertEqual(len(eventi.semi_ammessi("BACD_RBCD")), 214)
        self.assertEqual(eventi.seme_effettivo("BACD_RBCD", 0), 0)
        self.assertEqual(eventi.seme_effettivo("BACD_RBCD", 213), 213)
        self.assertEqual(eventi.seme_effettivo("BACD_RBCD", 5000), 213)

    def test_il_jirachi_a_tabella_avanza_di_due(self):
        """Tutte le voci della sua tabella danno lo stesso dono, ma le estrazioni si consumano."""
        seme = 0x1234
        self.assertEqual(eventi.seme_effettivo("BACD_TA", seme, specie=385),
                         eventi.avanza(eventi.avanza(seme)))

    def test_i_metodi_a_tabella_chiedono_la_specie(self):
        """Senza la specie non si puo' scegliere la voce, e il modulo lo dice invece di indovinare."""
        with self.assertRaises(gb.FormatError):
            eventi.seme_effettivo("BACD_TS", 1, specie=None)

    def test_il_metodo_a_elenco_chiede_i_semi(self):
        """I semi ammessi non sono derivabili da una formula e vanno estratti dalla fonte."""
        with self.assertRaises(gb.FormatError):
            eventi.seme_effettivo("BACD_M", 1)
        self.assertEqual(eventi.seme_effettivo("BACD_M", 3, semi_mystry=[10, 20, 30]), 10)

    def test_il_seme_vincolato_dal_sesso_produce_il_bit_richiesto(self):
        """Le due derivazioni che dichiarano il sesso tengono il seme coerente con esso."""
        for bit in (0, 1):
            seme = eventi.seme_ristretto_per_sesso(1, bit)
            self.assertIsNotNone(seme)
            quinta = eventi.estrazioni(seme, 5)[4]
            self.assertEqual(eventi._bit0_diviso_tre(quinta), bit)

    def test_i_metodi_non_ristretti_conservano_il_seme(self):
        """Il controllo negativo della restrizione: non tutti i metodi la applicano."""
        self.assertEqual(eventi.seme_effettivo("Method_2", 0x1234ABCD), 0x1234ABCD)
        self.assertEqual(eventi.seme_effettivo("BACD_R", 0x1234ABCD), 0xABCD)


class ProveSessoDalloStato(unittest.TestCase):
    """La lettura del sesso dallo stato residuo, e la sua coerenza con quella dal seme."""

    def test_coincide_con_la_lettura_dal_seme_quando_le_estrazioni_sono_quattro(self):
        """Le due letture devono concordare esattamente dove il vecchio conteggio valeva.

        Sono le derivazioni che leggono la quinta estrazione, su un ramo che ne consuma quattro:
        la' contare dal seme e portare avanti lo stato sono la medesima cosa, e questa prova lo
        fissa cosicche' una modifica a una delle due non passi inosservata.
        """
        for derivazione in ("RandD3", "RandS3", "RandS7", "RandSG15"):
            for seme in (1, 0x9DF6, 0xA823, 0xFFFF):
                stato = seme
                for _ in range(4):
                    stato = eventi.avanza(stato)
                self.assertEqual(
                    eventi.sesso_allenatore_da_stato(derivazione, stato),
                    eventi.sesso_allenatore(derivazione, seme),
                    "%s sul seme 0x%04X" % (derivazione, seme))

    def test_la_derivazione_a_scorrimento_di_quindici_legge_la_sesta(self):
        """Il controllo negativo: leggere la quinta darebbe un esito distinguibile."""
        distinti = 0
        for seme in range(1, 500):
            stato = seme
            for _ in range(4):
                stato = eventi.avanza(stato)
            parole = eventi.estrazioni(seme, 6)
            da_quinta = "femmina" if (parole[4] >> 15) & 1 else "maschio"
            if eventi.sesso_allenatore_da_stato("RandSG15", stato) != da_quinta:
                distinti += 1
        self.assertGreater(distinti, 0)


class ProveEsemplareCompleto(unittest.TestCase):
    """La funzione che mette assieme tutto, e i vincoli che verifica."""

    def test_l_evento_a_lucentezza_garantita_esce_cromatico(self):
        esito = eventi.esemplare_da_evento("BACD_RBCD", 30317, 0, "Always",
                                           derivazione="RandD3_1")
        self.assertIsNotNone(esito)
        self.assertTrue(esito["cromatico"])
        self.assertEqual(esito["sesso_ot"], "femmina")

    def test_l_evento_a_lucentezza_negata_non_esce_cromatico(self):
        esito = eventi.esemplare_da_evento("BACD_R_A", 6808, 0, "Never",
                                           derivazione="RandS7")
        self.assertIsNotNone(esito)
        self.assertFalse(esito["cromatico"])

    def test_l_evento_con_oggetto_consuma_una_estrazione_in_piu(self):
        """L'evento del desiderio estrae anche l'oggetto tenuto, e questo sposta il sesso.

        Il controllo negativo e' che l'estrazione dell'oggetto sia riportata soltanto per quel
        identificativo: su un altro evento resta assente, cosicche' la prova distingua i due
        casi invece di accertare un valore sempre presente.
        """
        con = eventi.esemplare_da_evento("BACD_R", eventi.ID_ALLENATORE_CON_OGGETTO, 0)
        senza = eventi.esemplare_da_evento("BACD_R", 6808, 0)
        self.assertIsNotNone(con["estrazione_oggetto"])
        self.assertIsNone(senza["estrazione_oggetto"])

    def test_il_metodo_a_elenco_produce_da_un_seme_dell_elenco(self):
        esito = eventi.esemplare_da_evento("BACD_M", 6930, 0, "Never", derivazione="RandD3",
                                           semi_mystry=[0x0652, 0x0932, 0x0C13])
        self.assertIsNotNone(esito)
        self.assertIn(esito["seme_effettivo"], (0x0652, 0x0932, 0x0C13))
        self.assertFalse(esito["cromatico"])


if __name__ == "__main__":
    unittest.main()
