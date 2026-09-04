#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ripara i difetti riparabili degli esemplari nel deposito di un salvataggio di sesta generazione.

Che cosa ripara, e perche' proprio questi
-----------------------------------------
Il 2026-09-04 la lettura dei due salvataggi di Rubino Omega della raccolta ha mostrato che i loro
difetti sono di due nature ben separate, e che una delle due si chiude con una riscrittura mentre
l'altra no.

La prima e' la memoria di geolocalizzazione. Il formato riserva cinque coppie di paese e regione,
e la regola e' che una coppia vuota non possa essere seguita da una piena e che una regione non
possa esistere senza il proprio paese. I salvataggi trovati in rete violano spesso quella regola,
e il verificatore lo dichiara con la formula sul ricordo di geolocalizzazione. E' il difetto piu'
frequente del salvataggio migliore della raccolta, e colpisce esemplari per il resto perfetti: la
lettura di uno di essi mostra un Muk con incontro selvatico reale in Rubino Omega, punti
allenamento che sommano centocinquanta e nessun altro rilievo. Azzerare le dieci posizioni rende
tutte e cinque le coppie vuote, che e' lo stato di un esemplare mai scambiato in rete, ed e' quindi
una riparazione e non una falsificazione.

La seconda sono i punti allenamento oltre il tetto. Il formato ne ammette al piu' duecentocinquanta
due per statistica e cinquecentodieci in totale, e i salvataggi costruiti al massimo ne portano
duecentocinquantadue su tutte e sei, cioe' millecinquecentododici. La riparazione conserva
l'intenzione di chi li aveva costruiti invece di azzerare tutto: le due statistiche che erano piu'
alte ricevono duecentocinquantadue ciascuna e sei vanno alla terza, che e' la distribuzione che il
gioco competitivo usa davvero.

La terza, opzionale, e' il luogo di incontro. Un esemplare i cui campi di incontro non
corrispondono ad alcun incontro reale viene respinto qualunque cosa si faccia sui punti
allenamento, e questo e' il caso del salvataggio peggiore della raccolta. La riparazione assegna
un incontro selvatico vero di Rubino Omega per quella specie, con il luogo e il livello che la
tabella degli incontri dichiara. Il fatto che la renda possibile e' proprio della sesta
generazione: li' i valori individuali e il valore di personalita' sono indipendenti fra loro e
dall'incontro, quindi non esiste il vincolo che nelle generazioni precedenti obbligherebbe a
ricalcolare tutto.

Che cosa non ripara, e va detto prima di usarlo
-----------------------------------------------
Non rende legittimo un esemplare: rimuove alcune cause di rifiuto e non tutte. Restano fuori dalla
sua portata le mosse non apprendibili al livello dichiarato, le mosse da ricordare, i nastri
impossibili per quell'incontro, i ricordi diversi da quello di geolocalizzazione, e ogni vincolo
che dipenda dalla storia dell'esemplare invece che dai suoi campi. Il criterio di successo non e'
quindi questo programma ma il verificatore, e il modo di lavorare e' il solito di questo progetto:
si ripara, si fa giudicare, si legge che cosa resti.

Non tocca mai il file di partenza. Scrive un file nuovo e lascia l'originale dov'e', perche' un
salvataggio della raccolta e' materiale di terzi e sovrascriverlo distruggerebbe la sola copia.

Uso
---
    python tools/ripara-deposito-gen6.py <file> --out <file nuovo>
    python tools/ripara-deposito-gen6.py <file> --out <file nuovo> --incontri --pkhex <clone>
    python tools/ripara-deposito-gen6.py --self-test
"""

import argparse
import io
import os
import struct
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "tools"))

DIM_ORAS = 0x76000
OFF_DEPOSITO = 0x33000
SCATOLE = 31
POSIZIONI = 30
DIM_STORED = 0xE8
DIM_BLOCCO = 56

OFF_CHECKSUM = 0x06
OFF_SPECIE = 0x08
OFF_EV = 0x1E
OFF_GEO = 0x94          # dieci byte: cinque coppie di regione e paese
LUN_GEO = 10
OFF_MET_ANNO = 0xD4
OFF_MET_MESE = 0xD5
OFF_MET_GIORNO = 0xD6
OFF_MET_LUOGO = 0xDA
OFF_BALL = 0xDC
OFF_MET_LIVELLO = 0xDD

EV_TOTALE_MASSIMO = 510
EV_SINGOLO_MASSIMO = 252
PALLA_POKE = 4

# La data di incontro va scritta come tre byte, con l'anno contato dal duemila. Rubino Omega e
# Zaffiro Alpha uscirono il 21 novembre 2014, quindi nessuna data anteriore a quell'anno e'
# possibile per un esemplare che vi sia stato incontrato. La data che il programma scrive quando
# quella trovata non e' valida e' una scelta nostra dichiarata, come lo sono i valori individuali
# dove la fonte non li fissa: si sceglie un giorno ben dentro la vita del gioco invece del giorno
# dell'uscita, perche' il giorno dell'uscita su centinaia di esemplari sarebbe esso stesso un
# indizio.
ANNO_MINIMO = 14
DATA_PREDEFINITA = (15, 6, 15)   # 15 giugno 2015
GIORNI_DEL_MESE = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

WILD = os.path.join("PKHeX.Core", "Resources", "legality", "wild")
INCONTRI_ORAS = ("Gen6/encounter_or.pkl", "Gen6/encounter_as.pkl")
# Gli incontri fissi, che le tabelle selvatiche non contengono. Sono la casa dei leggendari e
# degli iniziali, cioe' esattamente le specie che un deposito costruito contiene e che nessuna
# tabella selvatica dichiara: senza questa fonte centosettantadue esemplari su
# quattrocentocinquantaquattro restavano senza un incontro possibile.
STATICI_ORAS = "Gen6/Encounters6AO.cs"
DATI_INCONTRI = os.path.join("PKHeX.Core", "Legality", "Encounters", "Data")


def carica_lettore():
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "g6", os.path.join(RADICE, "tools", "leggi-deposito-gen6.py"))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def cifra(chiaro, blocchi):
    """L'inverso della decifratura: prima si rimescolano i blocchi, poi si cifra.

    L'ordine e' quello inverso della lettura, e sbagliarlo produce un file che il gioco rifiuta
    senza dire perche': la somma di controllo tornerebbe comunque, perche' e' una somma di parole
    e non dipende dall'ordine dei blocchi.
    """
    ec = struct.unpack_from("<I", chiaro, 0)[0]
    scelta = (ec >> 13) & 31
    ordine = blocchi[scelta]
    corpo = bytearray(DIM_STORED - 8)
    for posizione, blocco in enumerate(ordine):
        corpo[posizione * DIM_BLOCCO:(posizione + 1) * DIM_BLOCCO] = \
            chiaro[8 + blocco * DIM_BLOCCO:8 + (blocco + 1) * DIM_BLOCCO]
    seme = ec
    for i in range(0, len(corpo), 2):
        seme = (0x41C64E6D * seme + 0x00006073) & 0xFFFFFFFF
        x = (seme >> 16) & 0xFFFF
        v = struct.unpack_from("<H", corpo, i)[0] ^ x
        struct.pack_into("<H", corpo, i, v)
    return bytes(chiaro[:8]) + bytes(corpo)


def aggiorna_somma(chiaro):
    """Ricalcola la somma di controllo e la scrive dove il formato la vuole.

    Va fatta dopo ogni modifica e prima di cifrare: un esemplare modificato con la somma vecchia
    viene letto dal gioco come dato guasto, che e' peggio del difetto che si voleva togliere.
    """
    somma = 0
    for i in range(8, DIM_STORED, 2):
        somma = (somma + struct.unpack_from("<H", chiaro, i)[0]) & 0xFFFF
    struct.pack_into("<H", chiaro, OFF_CHECKSUM, somma)
    return chiaro


def ripara_ev(ev):
    """Una distribuzione legale che conserva l'intenzione dell'originale.

    Le due statistiche che erano piu' alte ricevono il massimo per statistica e la terza riceve il
    resto, che e' la distribuzione che il gioco competitivo usa davvero. Azzerare tutto sarebbe
    stato piu' semplice e avrebbe buttato via l'unica informazione che quei numeri portavano,
    cioe' su quali statistiche chi li aveva costruiti voleva puntare.
    """
    if sum(ev) <= EV_TOTALE_MASSIMO and all(v <= EV_SINGOLO_MASSIMO for v in ev):
        return list(ev), False
    ordine = sorted(range(6), key=lambda i: (-ev[i], i))
    nuovo = [0] * 6
    nuovo[ordine[0]] = EV_SINGOLO_MASSIMO
    nuovo[ordine[1]] = EV_SINGOLO_MASSIMO
    nuovo[ordine[2]] = EV_TOTALE_MASSIMO - 2 * EV_SINGOLO_MASSIMO
    return nuovo, True


def data_valida(anno, mese, giorno, _anno_massimo=None):
    """Se i tre byte formino una data del calendario, e nient'altro.

    La prima stesura di questa funzione controllava tre cose: che i tre byte formassero una data,
    che l'anno non precedesse l'uscita di Rubino Omega e che non venisse dal futuro. Le ultime due
    erano sbagliate e hanno rotto centosessantotto esemplari su un salvataggio che ne aveva pochi
    di guasti, ed e' il difetto peggiore commesso su questo track perche' ha peggiorato cio' che
    doveva riparare.

    L'errore di ragionamento e' preciso e vale enunciarlo. La data di incontro appartiene al gioco
    di origine e non al gioco che ospita l'esemplare: un Pokemon catturato in Diamante nel 2008 e
    poi trasferito porta legittimamente il 2008, e imporgli l'anno di uscita di Rubino Omega
    significa dichiarare impossibile una cosa che e' avvenuta. Nel salvataggio esaminato quasi
    tutte le specie vengono da giochi anteriori, quindi la regola sbagliata colpiva la maggioranza.

    Resta il solo controllo che non dipende da alcuna assunzione sul gioco: che mese e giorno
    formino una data che esiste. Un mese zero o un giorno quaranta non sono una data in nessun
    gioco e in nessun anno, e quello e' il difetto che i salvataggi trovati in rete portano
    davvero.
    """
    if not 1 <= mese <= 12:
        return False
    return 1 <= giorno <= GIORNI_DEL_MESE[mese - 1]


def geo_valida(geo):
    """La regola della fonte: dopo una coppia vuota non ne puo' venire una piena."""
    vuota_vista = False
    for i in range(5):
        regione, paese = geo[2 * i], geo[2 * i + 1]
        if paese == 0:
            if regione != 0:
                return False
            vuota_vista = True
        elif vuota_vista:
            return False
    return True


def aree(dati, larghezza=4):
    if len(dati) < 4:
        return None
    quante = struct.unpack_from("<H", dati, 2)[0]
    fuori = []
    for i in range(quante):
        off = 4 + i * larghezza
        if off + 8 > len(dati):
            return None
        coppia = struct.unpack_from("<Q", dati, off)[0]
        inizio, fine = coppia & 0xFFFFFFFF, coppia >> 32
        if not (0 <= inizio <= fine <= len(dati)):
            return None
        fuori.append(dati[inizio:fine])
    return fuori


def incontri_fissi(pkhex):
    """Gli incontri fissi di Rubino Omega, letti dalla tabella scritta in codice.

    Un leggendario non si incontra in un luogo selvatico ma in un punto preciso della mappa, e il
    verificatore chiama quel caso incontro fisso: la sua tabella dichiara specie, livello e luogo
    riga per riga. Gli iniziali stanno nella medesima tabella per la medesima ragione.
    """
    import re
    percorso = os.path.join(pkhex, DATI_INCONTRI, STATICI_ORAS.replace("/", os.sep))
    if not os.path.exists(percorso):
        return {}
    fuori = {}
    for riga in io.open(percorso, encoding="utf-8"):
        nuda = riga.lstrip()
        if nuda.startswith("//") or "new(" not in nuda:
            continue
        taglio = riga.find("//")
        if taglio >= 0:
            riga = riga[:taglio]
        ms = re.search(r"Species = (\d+)", riga)
        ml = re.search(r"Level = (\d+)", riga)
        mp = re.search(r"Location = (\d+)", riga)
        if not (ms and ml and mp):
            continue
        specie = int(ms.group(1))
        if 1 <= specie <= 721 and specie not in fuori:
            fuori[specie] = {"luogo": int(mp.group(1)), "min": int(ml.group(1)),
                             "max": int(ml.group(1)), "fisso": True}
    return fuori


def incontri_selvatici(pkhex):
    """Per ciascuna specie, un incontro selvatico vero di Rubino Omega o Zaffiro Alpha.

    Si sceglie il primo che la tabella dichiara, in ordine di area e di posizione, e la scelta e'
    deterministica per la stessa ragione per cui lo sono i semi del generatore di terza
    generazione: due corse devono dare lo stesso risultato, altrimenti il file riparato non e'
    riproducibile e non si puo' dimostrare nulla su di esso.
    """
    fuori = {}
    for relativo in INCONTRI_ORAS:
        percorso = os.path.join(pkhex, WILD, relativo.replace("/", os.sep))
        if not os.path.exists(percorso):
            continue
        blocchi = aree(io.open(percorso, "rb").read())
        if blocchi is None:
            continue
        for area in blocchi:
            if len(area) < 4:
                continue
            luogo = struct.unpack_from("<H", area, 0)[0]
            corpo = area[4:]
            for off in range(0, len(corpo) - 3, 4):
                grezzo = struct.unpack_from("<H", corpo, off)[0]
                specie = grezzo & 0x3FF
                if not 1 <= specie <= 721 or specie in fuori:
                    continue
                fuori[specie] = {"luogo": luogo, "min": corpo[off + 2], "max": corpo[off + 3]}
    return fuori


def preevoluzioni(pkhex):
    """Per ciascuna specie, le sue preevoluzioni in sesta generazione.

    Serve perche' la maggior parte delle specie non si incontra allo stato selvatico: si incontra
    la forma base e la si fa evolvere. Un Venusaur legittimo porta i dati di incontro di un
    Bulbasaur, e cercare un incontro selvatico di Venusaur significa cercare una cosa che non
    esiste. Senza questa risalita il programma lasciava intatti duecentotrentasette esemplari su
    quattrocentocinquantaquattro, cioe' la maggioranza, e la riparazione non serviva a nulla su di
    essi.
    """
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "ott", os.path.join(RADICE, "tools", "ottenibilita-titoli.py"))
    ott = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ott)
    presenti, indice_a_specie = ott.mappa_personale(
        pkhex, "personal_ao", 0x50, 0x1C, 0x20, None, 721)
    if presenti is None:
        # La tabella di Rubino Omega non e' nel clone: si ripiega su quella della settima
        # generazione, che contiene le medesime catene per le specie fino alla sesta.
        presenti, indice_a_specie = ott.mappa_personale(
            pkhex, "personal_uu", 0x54, 0x1C, 0x20, None, 721)
    if presenti is None:
        return {}
    archi = ott.archi_evoluzione(pkhex, "evos_g6.pkl", indice_a_specie) or []
    indietro = {}
    for da, a in archi:
        indietro.setdefault(a, set()).add(da)
    return indietro


def risali(specie, incontri, indietro, visti=None):
    """L'incontro selvatico della prima preevoluzione che ne abbia uno.

    La risalita e' in ampiezza e non in profondita' perche' una linea puo' biforcarsi, e si ferma
    alla prima che risponde: la scelta e' deterministica sull'ordine dei numeri di specie, per la
    stessa ragione per cui lo e' la scelta dell'incontro.
    """
    if specie in incontri:
        return incontri[specie], specie
    visti = visti or set()
    coda = sorted(indietro.get(specie, ()))
    while coda:
        s = coda.pop(0)
        if s in visti:
            continue
        visti.add(s)
        if s in incontri:
            return incontri[s], s
        coda.extend(sorted(indietro.get(s, ())))
    return None, None


def ripara(percorso, uscita, incontri=None, indietro=None, ripara_date=False):
    lettore = carica_lettore()
    dati = bytearray(io.open(percorso, "rb").read())
    if len(dati) != DIM_ORAS:
        return None, ("la dimensione %d non e' quella di un salvataggio di Rubino Omega o "
                      "Zaffiro Alfa" % len(dati))
    conto = {"esaminati": 0, "geo": 0, "ev": 0, "data": 0, "incontro": 0, "intatti": 0,
             "per_preevoluzione": 0, "senza_incontro": []}
    for scatola in range(SCATOLE):
        for posizione in range(POSIZIONI):
            off = OFF_DEPOSITO + (scatola * POSIZIONI + posizione) * DIM_STORED
            grezzo = bytes(dati[off:off + DIM_STORED])
            if not any(grezzo):
                continue
            chiaro = bytearray(lettore.decifra(grezzo))
            specie = struct.unpack_from("<H", chiaro, OFF_SPECIE)[0]
            if not 1 <= specie <= 721:
                continue
            conto["esaminati"] += 1
            toccato = False

            geo = list(chiaro[OFF_GEO:OFF_GEO + LUN_GEO])
            # Si azzera soltanto quando la sequenza e' rotta, e non ogni volta che c'e' qualcosa.
            # La prima stesura scriveva `or any(geo)`, cioe' azzerava anche le sequenze valide, e
            # il confronto fra i rapporti del salvataggio originale e di quello riparato ha
            # mostrato che quella clausola concorre a rompere duecentoundici esemplari che erano
            # legali: una geolocalizzazione valida porta informazione sugli scambi che
            # l'esemplare ha subito, e cancellarla la mette in contraddizione con i ricordi
            # dell'allenatore che lo ha ricevuto.
            if not geo_valida(geo):
                chiaro[OFF_GEO:OFF_GEO + LUN_GEO] = bytes(LUN_GEO)
                conto["geo"] += 1
                toccato = True

            anno, mese, giorno = (chiaro[OFF_MET_ANNO], chiaro[OFF_MET_MESE],
                                  chiaro[OFF_MET_GIORNO])
            # La riparazione della data e' spenta per difetto, e la ragione e' una misura e non
            # una prudenza generica: il confronto fra i rapporti del 2026-09-04 mostra che da
            # sola porta a non legali trentadue esemplari che lo erano, mentre l'insieme delle
            # riparazioni ne recupera quattordici in tutto. Una riparazione che perde piu' di
            # quanto guadagni non e' una riparazione, e va accesa soltanto da chi sappia perche'.
            if ripara_date and not data_valida(anno, mese, giorno):
                # L'anno si conserva quando e' un anno e non un byte qualunque, perche' e'
                # l'unica parte della data che porti informazione sulla storia dell'esemplare:
                # si riscrivono il mese e il giorno, che erano fuori dal calendario.
                chiaro[OFF_MET_ANNO] = anno if 1 <= anno <= 99 else DATA_PREDEFINITA[0]
                chiaro[OFF_MET_MESE] = DATA_PREDEFINITA[1]
                chiaro[OFF_MET_GIORNO] = DATA_PREDEFINITA[2]
                conto["data"] += 1
                toccato = True

            ev = list(chiaro[OFF_EV:OFF_EV + 6])
            nuovo, cambiato = ripara_ev(ev)
            if cambiato:
                chiaro[OFF_EV:OFF_EV + 6] = bytes(nuovo)
                conto["ev"] += 1
                toccato = True

            if incontri is not None:
                slot, da_specie = risali(specie, incontri, indietro or {})
                if slot is not None and da_specie != specie:
                    conto["per_preevoluzione"] += 1
                if slot is None:
                    conto["senza_incontro"].append(specie)
                else:
                    struct.pack_into("<H", chiaro, OFF_MET_LUOGO, slot["luogo"])
                    # Il bit alto del byte del livello porta il sesso dell'allenatore e non va
                    # toccato: si scrive il solo livello nei sette bit bassi.
                    chiaro[OFF_MET_LIVELLO] = ((chiaro[OFF_MET_LIVELLO] & 0x80)
                                               | (slot["min"] & 0x7F))
                    chiaro[OFF_BALL] = PALLA_POKE
                    conto["incontro"] += 1
                    toccato = True

            if not toccato:
                conto["intatti"] += 1
                continue
            aggiorna_somma(chiaro)
            dati[off:off + DIM_STORED] = cifra(bytes(chiaro), lettore.BLOCCHI)
    io.open(uscita, "wb").write(bytes(dati))
    return conto, None


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("una distribuzione gia' legale non si tocca",
          ([4, 252, 0, 252, 0, 2], False), ripara_ev([4, 252, 0, 252, 0, 2]))
    riparato, cambiato = ripara_ev([252] * 6)
    prova("una distribuzione al massimo si ripara", True, cambiato)
    prova("la riparazione somma esattamente il tetto", EV_TOTALE_MASSIMO, sum(riparato))
    prova("nessuna statistica supera il proprio tetto", True,
          all(v <= EV_SINGOLO_MASSIMO for v in riparato))
    riparato, _ = ripara_ev([0, 300, 0, 0, 400, 100])
    prova("la riparazione punta sulle due statistiche piu' alte",
          [0, 252, 0, 0, 252, 6], riparato)

    prova("una data del calendario e' valida", True, data_valida(15, 6, 15))
    prova("il mese zero non e' una data", False, data_valida(15, 0, 15))
    prova("il giorno quaranta non e' una data", False, data_valida(15, 6, 40))
    prova("il 31 novembre non esiste", False, data_valida(15, 11, 31))
    # Le due prove che documentano il difetto corretto: un anno anteriore all'uscita di Rubino
    # Omega e un anno alto restano validi, perche' la data appartiene al gioco di origine e non a
    # quello che ospita l'esemplare. La regola che li rifiutava ha rotto centosessantotto voci.
    prova("un anno anteriore all'uscita resta valido", True, data_valida(8, 6, 15))
    prova("un anno alto resta valido", True, data_valida(30, 6, 15))
    prova("la data predefinita e' essa stessa valida", True,
          data_valida(DATA_PREDEFINITA[0], DATA_PREDEFINITA[1], DATA_PREDEFINITA[2]))

    prova("cinque coppie vuote sono valide", True, geo_valida([0] * 10))
    prova("una coppia piena seguita da vuote e' valida", True,
          geo_valida([1, 2, 0, 0, 0, 0, 0, 0, 0, 0]))
    prova("una regione senza paese non e' valida", False,
          geo_valida([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    prova("una coppia piena dopo una vuota non e' valida", False,
          geo_valida([0, 0, 1, 2, 0, 0, 0, 0, 0, 0]))

    # Cifrare e decifrare devono essere l'una l'inversa dell'altra: se non lo fossero, ogni file
    # riparato uscirebbe illeggibile e il difetto si vedrebbe solo sulla console.
    lettore = carica_lettore()
    import random
    rng = random.Random(7)
    chiaro = bytearray(rng.randrange(256) for _ in range(DIM_STORED))
    struct.pack_into("<I", chiaro, 0, 0xABCDEF01)
    aggiorna_somma(chiaro)
    cifrato = cifra(bytes(chiaro), lettore.BLOCCHI)
    prova("cifrare e decifrare si annullano", bytes(chiaro), lettore.decifra(cifrato))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file", nargs="?", help="il salvataggio da riparare")
    ap.add_argument("--out", help="il file nuovo da scrivere; l'originale non si tocca mai")
    ap.add_argument("--date", action="store_true",
                    help="riscrive anche le date di incontro che non sono date del calendario; "
                         "spenta per difetto perche' la misura del 2026-09-04 mostra che perde "
                         "piu' di quanto guadagni")
    ap.add_argument("--incontri", action="store_true",
                    help="assegna anche un luogo e un livello di incontro selvatico veri")
    ap.add_argument("--pkhex", help="clone del verificatore, necessario con --incontri")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.file or not a.out:
        ap.error("servono il file e --out, oppure --self-test")
    if os.path.abspath(a.file) == os.path.abspath(a.out):
        ap.error("il file di uscita non puo' essere quello di partenza: questo programma non "
                 "sovrascrive mai l'originale")
    incontri, indietro = None, {}
    if a.incontri:
        if not a.pkhex:
            ap.error("--incontri richiede --pkhex")
        incontri = incontri_selvatici(a.pkhex)
        # I fissi non sovrascrivono i selvatici: un esemplare che si puo' incontrare
        # nell'erba e' meglio spiegato da quello, e il fisso resta per le specie che
        # nell'erba non ci sono.
        fissi = incontri_fissi(a.pkhex)
        aggiunti = 0
        for specie, slot in fissi.items():
            if specie not in incontri:
                incontri[specie] = slot
                aggiunti += 1
        if aggiunti:
            print("incontri fissi aggiunti per %d specie che nessuna tabella selvatica porta"
                  % aggiunti)
        if not incontri:
            print("nessun incontro letto: il clone non porta le tabelle di Rubino Omega")
            return 1
        indietro = preevoluzioni(a.pkhex)
        print("incontri selvatici letti per %d specie, catene di evoluzione per %d"
              % (len(incontri), len(indietro)))
    conto, errore = ripara(a.file, a.out, incontri, indietro, a.date)
    if errore:
        print("rifiutato: " + errore)
        return 1
    print("")
    print("  esemplari esaminati                %5d" % conto["esaminati"])
    print("  con la geolocalizzazione azzerata  %5d" % conto["geo"])
    print("  con i punti allenamento riportati  %5d" % conto["ev"])
    print("  con la data di incontro corretta   %5d" % conto["data"])
    if incontri is not None:
        print("  con un incontro selvatico vero     %5d" % conto["incontro"])
        print("  di cui presi da una preevoluzione   %5d" % conto["per_preevoluzione"])
        senza = sorted(set(conto["senza_incontro"]))
        print("  senza alcun incontro selvatico     %5d specie: %s"
              % (len(senza), senza[:20] if senza else "nessuna"))
    print("  lasciati intatti                   %5d" % conto["intatti"])
    print("")
    print("  scritto " + a.out + ", e l'originale non e' stato toccato.")
    print("  Il criterio di successo non e' questo programma ma il verificatore: si apre il file")
    print("  nuovo e si legge che cosa resti da obiettare.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
