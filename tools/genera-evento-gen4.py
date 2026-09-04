#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Estrae gli esemplari da evento di quarta generazione dalla base dei doni segreti.

Perche' e' un problema diverso da quello di terza generazione
-------------------------------------------------------------
Per la terza generazione questo progetto ha dovuto ricostruire il generatore pseudocasuale, cioe'
rifare il procedimento con cui il gioco componeva l'esemplare a partire da un seme, e la campagna
e' costata settimane e otto difetti. Per la quarta generazione quel lavoro non serve, e la ragione
e' nella forma stessa del dono: un dono di quarta generazione non descrive un esemplare da
generare, lo contiene gia' fatto.

Il record del dono e' lungo 0x358 byte e comincia con la carta, che a otto byte dal proprio inizio
porta la struttura dell'esemplare nel formato di squadra del gioco, lunga 236 byte. Nella base dati
della fonte quella struttura e' conservata in chiaro invece che cifrata, il che si riconosce dal
campo che porterebbe i bit di fiocco inutilizzati: se e' nullo il dato non e' cifrato. Produrre un
esemplare significa quindi estrarlo, non calcolarlo, e il valore di personalita' e i valori
individuali sono quelli che la distribuzione aveva davvero invece che un seme che li riproduca.

Ne segue una differenza di natura sulla fedelta' che va enunciata perche' rovescia il quadro delle
generazioni precedenti. In terza generazione la fedelta' era il risultato di una ricostruzione e si
poteva sbagliare in molti modi; qui l'esemplare e' il dato originale, e cio' che si puo' sbagliare
non e' il suo contenuto ma la sua estrazione.

Che cosa resta da decidere e non si estrae
------------------------------------------
Alcune voci dichiarano che il nome e gli identificativi dell'allenatore appartengono a chi riceve
la consegna, e la struttura contenuta li porta a zero o a un valore convenzionale. Per quelle si
scrive l'allenatore del progetto, che e' lo stesso delle altre generazioni e sta nel file condiviso
`recreate-pokemon-distributions-events/allenatore.json`.

Uso
---
    python tools/genera-evento-gen4.py --pkhex _notes/fonti/pkhex
    python tools/genera-evento-gen4.py --pkhex <clone> --lotto _notes/lotto-gen4
    python tools/genera-evento-gen4.py --self-test
"""

import argparse
import io
import json
import os
import re
import struct
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MGDB = os.path.join("PKHeX.Core", "Resources", "legality", "mgdb")
REGISTRO_ALLENATORE = os.path.join("recreate-pokemon-distributions-events", "allenatore.json")

# Il record del dono, da PCD e PGT.
DIM_DONO = 0x358
OFF_TIPO = 0x00            # il tipo di dono, una parola a inizio record
DIM_PGT = 0x104
OFF_PK4 = 0x08             # la struttura dell'esemplare, dentro la carta
DIM_PK4_SQUADRA = 236
DIM_PK4_SCATOLA = 136

# I valori del tipo che indicano un esemplare, da GiftType4: Pokemon, uovo, uovo di Manaphy e
# Pokemon da film. Gli altri sono oggetti, regole, merci e non ci riguardano.
TIPI_ESEMPLARE = {1, 2, 7, 13}

# Gli offset dentro la struttura dell'esemplare, da PK4.
OFF_PID = 0x00
OFF_CHECKSUM = 0x06
OFF_SPECIE = 0x08
OFF_TID = 0x0C
OFF_SID = 0x0E
OFF_VERSIONE = 0x5F
OFF_OT_NOME = 0x68         # sedici byte, sette caratteri piu' il terminatore
OFF_PALLA_DPPT = 0x83
OFF_LIVELLO_INCONTRO = 0x84
OFF_PALLA_HGSS = 0x86

# Il campo che dice se la struttura sia cifrata, da PokeCrypto.IsEncrypted45: sono i bit di fiocco
# inutilizzati, che in chiaro valgono zero. Il controllo e' della fonte e non nostro, e vale
# richiamarlo perche' e' l'unico modo di distinguere le due forme senza provarle entrambe.
OFF_PROVA_CIFRATURA = 0x64

MAX_SPECIE_4 = 493


def allenatore_del_progetto():
    """L'allenatore per le voci che lo prendono da chi riceve, dal file condiviso."""
    percorso = os.path.join(RADICE, REGISTRO_ALLENATORE)
    if not os.path.exists(percorso):
        return None
    d = json.loads(io.open(percorso, encoding="utf-8").read())
    return {"nome": d["nome"], "tid": int(d["tid"]), "sid": int(d.get("sid", 0))}


def e_cifrata(pk4):
    """Se la struttura sia nella forma cifrata del gioco invece che in chiaro."""
    return struct.unpack_from("<I", pk4, OFF_PROVA_CIFRATURA)[0] != 0


def somma_controllo(pk4):
    """La somma a sedici bit dei byte dal 0x08 alla fine della parte di scatola.

    E' la medesima famiglia di somme delle altre generazioni, e vale qui l'avvertenza gia'
    registrata: sommando parole non dipende dall'ordine dei blocchi, quindi non puo' rivelare una
    permutazione sbagliata. Chi la usasse come sola prova di una lettura si ingannerebbe.
    """
    somma = 0
    for i in range(0x08, DIM_PK4_SCATOLA, 2):
        somma = (somma + struct.unpack_from("<H", pk4, i)[0]) & 0xFFFF
    return somma


def leggi_doni(pkhex):
    """Le voci della base dei doni di quarta generazione, con l'esemplare che contengono.

    Riferisce anche le voci che esemplari non sono, perche' contarle fra gli scarti senza dirlo
    darebbe l'impressione di una lettura parziale: la medesima base dati porta oggetti e altre
    consegne, e la loro presenza non e' un difetto.
    """
    percorso = os.path.join(pkhex, MGDB, "wc4.pkl")
    if not os.path.exists(percorso):
        return None, "manca wc4.pkl sotto " + os.path.join(pkhex, MGDB)
    dati = io.open(percorso, "rb").read()
    quante, resto = divmod(len(dati), DIM_DONO)
    if resto:
        return None, ("la dimensione %d non e' multipla del passo %d: la lunghezza del record che "
                      "stiamo usando e' sbagliata" % (len(dati), DIM_DONO))
    fuori, non_esemplari, difettosi = [], 0, []
    for indice in range(quante):
        rec = dati[indice * DIM_DONO:(indice + 1) * DIM_DONO]
        tipo = struct.unpack_from("<H", rec, OFF_TIPO)[0]
        if tipo not in TIPI_ESEMPLARE:
            non_esemplari += 1
            continue
        pk4 = rec[OFF_PK4:OFF_PK4 + DIM_PK4_SQUADRA]
        if len(pk4) < DIM_PK4_SQUADRA:
            difettosi.append((indice, "il record e' piu' corto della struttura"))
            continue
        specie = struct.unpack_from("<H", pk4, OFF_SPECIE)[0]
        if not 1 <= specie <= MAX_SPECIE_4:
            difettosi.append((indice, "specie %d fuori dall'intervallo della quarta generazione"
                              % specie))
            continue
        fuori.append({
            "indice": indice,
            "tipo": tipo,
            "cifrata": e_cifrata(pk4),
            "specie": specie,
            "pid": struct.unpack_from("<I", pk4, OFF_PID)[0],
            "tid": struct.unpack_from("<H", pk4, OFF_TID)[0],
            "sid": struct.unpack_from("<H", pk4, OFF_SID)[0],
            "versione": pk4[OFF_VERSIONE],
            "livello_incontro": pk4[OFF_LIVELLO_INCONTRO] & 0x7F,
            "palla": pk4[OFF_PALLA_HGSS] or pk4[OFF_PALLA_DPPT],
            "checksum_memorizzato": struct.unpack_from("<H", pk4, OFF_CHECKSUM)[0],
            "checksum_calcolato": somma_controllo(pk4),
            "byte": pk4,
        })
    return {"voci": fuori, "non_esemplari": non_esemplari, "difettosi": difettosi,
            "record": quante}, None


def scrivi_lotto(voci, destinazione, allenatore):
    """Scrive un file per esemplare nella forma di scatola, che e' quella che il verificatore apre.

    Le voci che dichiarano gli identificativi a zero prendono quelli del progetto, e la
    sostituzione si annota nel nome del file cosicche' chi guarda la cartella veda subito quali
    voci portano un dato nostro e quali il dato storico.
    """
    if not os.path.isdir(destinazione):
        os.makedirs(destinazione)
    scritti, con_allenatore = 0, 0
    for v in voci:
        pk4 = bytearray(v["byte"][:DIM_PK4_SCATOLA])
        nostro = False
        if allenatore and v["tid"] == 0 and v["sid"] == 0:
            struct.pack_into("<H", pk4, OFF_TID, allenatore["tid"] & 0xFFFF)
            struct.pack_into("<H", pk4, OFF_SID, allenatore["sid"] & 0xFFFF)
            nostro = True
            con_allenatore += 1
        struct.pack_into("<H", pk4, OFF_CHECKSUM, somma_controllo(pk4))
        nome = "EVT-4-%04d-%03d%s.pk4" % (v["indice"], v["specie"], "-nostro" if nostro else "")
        io.open(os.path.join(destinazione, nome), "wb").write(bytes(pk4))
        scritti += 1
    return scritti, con_allenatore


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("il record del dono e' lungo 0x358", 856, DIM_DONO)
    prova("la struttura di squadra e' lunga 236", 236, DIM_PK4_SQUADRA)
    prova("la struttura di scatola e' lunga 136", 136, DIM_PK4_SCATOLA)
    prova("i tipi che indicano un esemplare sono quattro", 4, len(TIPI_ESEMPLARE))

    finto = bytearray(DIM_PK4_SQUADRA)
    prova("una struttura azzerata non risulta cifrata", False, e_cifrata(finto))
    struct.pack_into("<I", finto, OFF_PROVA_CIFRATURA, 1)
    prova("una struttura con quel campo non nullo risulta cifrata", True, e_cifrata(finto))

    finto = bytearray(DIM_PK4_SQUADRA)
    struct.pack_into("<H", finto, OFF_SPECIE, 0x0102)
    # La somma copre dal 0x08 alla fine della parte di scatola, quindi la specie vi entra e la
    # somma di una struttura per il resto nulla vale la specie stessa.
    prova("la somma di una struttura con la sola specie vale la specie", 0x0102,
          somma_controllo(finto))
    struct.pack_into("<H", finto, 0x86, 0x0001)
    prova("la somma cresce di quanto si aggiunge", 0x0103, somma_controllo(finto))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", help="clone del verificatore")
    ap.add_argument("--lotto", help="cartella in cui scrivere gli esemplari")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.pkhex:
        ap.error("serve --pkhex, oppure --self-test")
    esito, errore = leggi_doni(a.pkhex)
    if errore:
        print("rifiutato: " + errore)
        return 1
    voci = esito["voci"]
    print("Esemplari da evento di quarta generazione")
    print("")
    print("  record nella base dei doni          %5d" % esito["record"])
    print("  di cui esemplari                    %5d" % len(voci))
    print("  di cui oggetti e altre consegne     %5d" % esito["non_esemplari"])
    print("  strutture rifiutate                 %5d" % len(esito["difettosi"]))
    cifrate = sum(1 for v in voci if v["cifrata"])
    print("")
    print("  strutture conservate in chiaro      %5d" % (len(voci) - cifrate))
    print("  strutture conservate cifrate        %5d" % cifrate)
    somme_ok = sum(1 for v in voci if v["checksum_memorizzato"] == v["checksum_calcolato"])
    print("  con la somma di controllo che torna %5d su %d" % (somme_ok, len(voci)))
    senza_id = sum(1 for v in voci if v["tid"] == 0 and v["sid"] == 0)
    print("  con gli identificativi a zero, cioe' dal ricevente: %d" % senza_id)
    print("")
    print("  specie distinte                     %5d" % len({v["specie"] for v in voci}))
    if esito["difettosi"]:
        print("")
        for indice, ragione in esito["difettosi"][:10]:
            print("  difetto: voce %d: %s" % (indice, ragione))
    if a.lotto:
        allenatore = allenatore_del_progetto()
        scritti, nostri = scrivi_lotto(voci, a.lotto, allenatore)
        print("")
        print("  scritti %d file in %s, di cui %d con l'allenatore del progetto"
              % (scritti, a.lotto, nostri))
        print("  Il passo seguente non e' di questo programma: si aprono con il verificatore nel")
        print("  contesto della quarta generazione e si legge che cosa esso obietti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
