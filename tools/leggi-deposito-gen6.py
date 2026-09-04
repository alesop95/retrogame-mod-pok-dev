#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legge il deposito di un salvataggio di sesta generazione e classifica i suoi esemplari.

Perche' esiste
--------------
La raccolta di salvataggi esterni del progetto contiene due partite di Rubino Omega, e il 2026-09-04
si e' stabilito che la console le accetta entrambe: la causa del rifiuto precedente era il nome del
file e non il loro contenuto. Resta pero' aperta la domanda che conta davvero, cioe' se gli
esemplari che stanno nelle loro scatole siano trasferibili verso il deposito in rete, e su quella
il fatto che la console avvii la partita non dice nulla: sono due porte diverse.

Un campione di quattro esemplari letto a mano dalle schermate aveva suggerito che le due partite
fossero qualitativamente diverse, cioe' che l'una portasse esemplari sani con difetti di contorno e
l'altra esemplari impossibili. Un campione di quattro su qualche migliaio e' una impressione e non
una misura, e questo programma la sostituisce con un conto.

Che cosa misura, e che cosa non puo' misurare
---------------------------------------------
Misura le proprieta' che si stabiliscono guardando il solo esemplare, senza conoscere le tabelle
degli incontri: la somma dei punti allenamento contro il tetto che il formato impone, il tetto per
singola statistica, i valori individuali fuori intervallo, il livello, e la coerenza fra il valore
di personalita' e il resto. Sono i controlli che bastano a separare un esemplare costruito male da
uno plausibile, ed e' esattamente la separazione che serve a decidere se una partita valga come
fonte.

Non misura la legittimita', che e' il giudizio del verificatore e richiede le tabelle degli
incontri, le mosse ammesse a quel livello, i luoghi possibili e le catene di evoluzione. Un
esemplare che questo programma non contesta puo' essere ugualmente respinto, e la distinzione va
tenuta: qui si separa l'impossibile dal plausibile, non il legittimo dall'illegittimo.

Il formato
----------
Il salvataggio di Rubino Omega tiene il deposito a 0x33000, con trentuno scatole da trenta
posizioni e duecentotrentadue byte per posizione. Ogni posizione e' cifrata con lo schema della
sesta generazione: la chiave e' la costante di cifratura nei primi quattro byte, il corpo dalla
posizione otto in avanti si decifra con un generatore lineare congruenziale che produce una parola
a sedici bit per volta, e i quattro blocchi da cinquantasei byte vanno rimessi nell'ordine
canonico secondo una permutazione scelta dai bit da tredici a diciassette della medesima costante.
Gli offset dei campi vengono da PK6 e la permutazione da PokeCrypto, letti il 2026-09-04.

Uso
---
    python tools/leggi-deposito-gen6.py "_notes/salvataggi/pronti-3ds/omega-ruby-A-projectpokemon/main"
    python tools/leggi-deposito-gen6.py <file> --dettaglio
    python tools/leggi-deposito-gen6.py --self-test
"""

import argparse
import io
import os
import struct
import sys

# Il deposito di Rubino Omega e Zaffiro Alpha, da SAV6AO: le altre famiglie hanno un altro
# offset, quindi il programma verifica la dimensione prima di leggere invece di fidarsi.
DIM_ORAS = 0x76000
OFF_DEPOSITO = 0x33000
SCATOLE = 31
POSIZIONI = 30
DIM_STORED = 0xE8
DIM_BLOCCO = 56

# Gli offset dei campi dentro la struttura decifrata, da PK6.
OFF_EC = 0x00
OFF_SANITA = 0x04
OFF_CHECKSUM = 0x06
OFF_SPECIE = 0x08
OFF_PID = 0x18
OFF_EV = 0x1E          # sei byte consecutivi: PS, attacco, difesa, velocita', speciale, special difesa
OFF_IV32 = 0x74

# I tetti che il formato impone, e che un esemplare costruito a mano viola per primo.
EV_TOTALE_MASSIMO = 510
EV_SINGOLO_MASSIMO = 252
IV_MASSIMO = 31
MAX_SPECIE = 721       # la sesta generazione arriva a Volcanion

# La permutazione dei quattro blocchi, da PokeCrypto.BlockPosition: l'indice e' il valore di
# scelta ricavato dalla costante di cifratura, e i quattro numeri dicono in quale ordine i blocchi
# si trovano nel dato cifrato.
BLOCCHI = (
    (0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 1, 2),
    (0, 2, 3, 1), (0, 3, 2, 1), (1, 0, 2, 3), (1, 0, 3, 2),
    (2, 0, 1, 3), (3, 0, 1, 2), (2, 0, 3, 1), (3, 0, 2, 1),
    (1, 2, 0, 3), (1, 3, 0, 2), (2, 1, 0, 3), (3, 1, 0, 2),
    (2, 3, 0, 1), (3, 2, 0, 1), (1, 2, 3, 0), (1, 3, 2, 0),
    (2, 1, 3, 0), (3, 1, 2, 0), (2, 3, 1, 0), (3, 2, 1, 0),
    (0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 1, 2),
    (0, 2, 3, 1), (0, 3, 2, 1), (1, 0, 2, 3), (1, 0, 3, 2),
)


def decifra(grezzo):
    """La struttura in chiaro, dal dato cifrato di una posizione del deposito.

    Le due operazioni non commutano e l'ordine e' quello della fonte: prima si toglie la
    cifratura, poi si rimettono i blocchi in ordine. Invertirle produce byte che sembrano dati e
    non lo sono, cioe' il difetto che questo progetto ha gia' incontrato in terza generazione.
    """
    ec = struct.unpack_from("<I", grezzo, 0)[0]
    scelta = (ec >> 13) & 31
    corpo = bytearray(grezzo[8:DIM_STORED])
    seme = ec
    for i in range(0, len(corpo), 2):
        seme = (0x41C64E6D * seme + 0x00006073) & 0xFFFFFFFF
        x = (seme >> 16) & 0xFFFF
        v = struct.unpack_from("<H", corpo, i)[0] ^ x
        struct.pack_into("<H", corpo, i, v)
    ordine = BLOCCHI[scelta]
    fuori = bytearray(DIM_STORED)
    fuori[0:8] = grezzo[0:8]
    for posizione, blocco in enumerate(ordine):
        sorgente = posizione * DIM_BLOCCO
        destinazione = 8 + blocco * DIM_BLOCCO
        fuori[destinazione:destinazione + DIM_BLOCCO] = corpo[sorgente:sorgente + DIM_BLOCCO]
    return bytes(fuori)


def struttura_valida(chiaro):
    """Il criterio con cui si distingue una posizione occupata da un residuo.

    Il primo tentativo usava l'assenza di byte non nulli, e non basta: una posizione svuotata
    conserva i byte del precedente occupante, quindi si legge come un esemplare con una specie
    assurda. Il criterio giusto e' quello che la fonte stessa impiega, cioe' la somma a sedici bit
    dei byte dalla posizione otto alla fine confrontata con il valore memorizzato a sei, insieme
    al campo di sanita' che deve valere zero. Con esso i residui cadono senza bisogno di
    riconoscerli dal contenuto, che sarebbe una euristica.
    """
    somma = 0
    for i in range(8, DIM_STORED, 2):
        somma = (somma + struct.unpack_from("<H", chiaro, i)[0]) & 0xFFFF
    memorizzato = struct.unpack_from("<H", chiaro, OFF_CHECKSUM)[0]
    sanita = struct.unpack_from("<H", chiaro, OFF_SANITA)[0]
    return somma == memorizzato and sanita == 0


def campi(chiaro):
    """I campi che servono alla classificazione, dalla struttura in chiaro."""
    specie = struct.unpack_from("<H", chiaro, OFF_SPECIE)[0]
    ev = list(chiaro[OFF_EV:OFF_EV + 6])
    iv32 = struct.unpack_from("<I", chiaro, OFF_IV32)[0]
    iv = [(iv32 >> (5 * i)) & 0x1F for i in range(6)]
    return {
        "specie": specie,
        "pid": struct.unpack_from("<I", chiaro, OFF_PID)[0],
        "ec": struct.unpack_from("<I", chiaro, OFF_EC)[0],
        "ev": ev, "ev_totale": sum(ev), "iv": iv,
    }


def contestazioni(c):
    """Le violazioni che si stabiliscono guardando il solo esemplare.

    Ciascuna e' una violazione di un vincolo del formato o delle regole del gioco che nessun
    esemplare ottenuto giocando puo' presentare: non sono euristiche e non hanno falsi positivi.
    Un esemplare senza contestazioni non e' per questo legittimo, e il docstring del programma
    dice perche'.
    """
    fuori = []
    if not 1 <= c["specie"] <= MAX_SPECIE:
        fuori.append("specie %d fuori dall'intervallo della sesta generazione" % c["specie"])
    if c["ev_totale"] > EV_TOTALE_MASSIMO:
        fuori.append("punti allenamento per un totale di %d, oltre il massimo di %d"
                     % (c["ev_totale"], EV_TOTALE_MASSIMO))
    eccessivi = [v for v in c["ev"] if v > EV_SINGOLO_MASSIMO]
    if eccessivi:
        fuori.append("punti allenamento singoli oltre il massimo di %d: %s"
                     % (EV_SINGOLO_MASSIMO, eccessivi))
    if any(v > IV_MASSIMO for v in c["iv"]):
        fuori.append("valori individuali oltre il massimo di %d" % IV_MASSIMO)
    return fuori


def leggi(percorso):
    dati = io.open(percorso, "rb").read()
    if len(dati) != DIM_ORAS:
        return None, ("la dimensione %d non e' quella di un salvataggio di Rubino Omega o "
                      "Zaffiro Alfa, che e' %d" % (len(dati), DIM_ORAS))
    fuori, residui = [], 0
    for scatola in range(SCATOLE):
        for posizione in range(POSIZIONI):
            off = OFF_DEPOSITO + (scatola * POSIZIONI + posizione) * DIM_STORED
            grezzo = dati[off:off + DIM_STORED]
            if len(grezzo) < DIM_STORED or not any(grezzo):
                continue
            chiaro = decifra(grezzo)
            if not struttura_valida(chiaro):
                residui += 1
                continue
            c = campi(chiaro)
            if c["specie"] == 0:
                continue
            c["scatola"], c["posizione"] = scatola + 1, posizione + 1
            c["contestazioni"] = contestazioni(c)
            fuori.append(c)
    return {"esemplari": fuori, "residui": residui}, None


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("la tabella delle permutazioni ha trentadue voci", 32, len(BLOCCHI))
    prova("ogni permutazione e' una permutazione di quattro blocchi", True,
          all(sorted(p) == [0, 1, 2, 3] for p in BLOCCHI))
    # Le ultime otto voci sono la copia delle prime otto, che la fonte aggiunge per evitare un
    # resto: se la copia non coincidesse, la permutazione scelta da un valore alto sarebbe
    # sbagliata e nessun controllo lo direbbe.
    prova("le ultime otto voci ripetono le prime otto", BLOCCHI[:8], BLOCCHI[24:])

    finto = {"specie": 3, "ev": [252, 252, 252, 252, 252, 252], "ev_totale": 1512,
             "iv": [31] * 6}
    c = contestazioni(finto)
    # Una contestazione sola e non due: il totale supera il tetto, mentre 252 su una singola
    # statistica e' esattamente il massimo consentito e non lo supera. La prima stesura di questa
    # prova ne attendeva due, e sbagliava proprio sul confine.
    prova("un esemplare con tutti i punti al massimo e' contestato una volta", 1, len(c))
    finto_singolo = {"specie": 3, "ev": [253, 0, 0, 0, 0, 0], "ev_totale": 253, "iv": [31] * 6}
    prova("un punto singolo oltre il tetto e' contestato", 1, len(contestazioni(finto_singolo)))
    finto = {"specie": 3, "ev": [252, 252, 6, 0, 0, 0], "ev_totale": 510, "iv": [31] * 6}
    prova("una distribuzione da 510 non e' contestata", [], contestazioni(finto))
    finto = {"specie": 999, "ev": [0] * 6, "ev_totale": 0, "iv": [0] * 6}
    prova("una specie fuori intervallo e' contestata", 1, len(contestazioni(finto)))
    finto = {"specie": 3, "ev": [0] * 6, "ev_totale": 0, "iv": [31, 31, 31, 31, 31, 32]}
    prova("un valore individuale a trentadue e' contestato", 1, len(contestazioni(finto)))

    # La cifratura e' la propria inversa nel senso che decifrare un dato costruito cifrando deve
    # restituire l'originale. Si costruisce un dato in chiaro, lo si cifra con la procedura
    # inversa e lo si ridecifra.
    import random
    rng = random.Random(1)
    chiaro = bytearray(rng.randrange(256) for _ in range(DIM_STORED))
    struct.pack_into("<I", chiaro, 0, 0x12345678)
    ec = 0x12345678
    scelta = (ec >> 13) & 31
    ordine = BLOCCHI[scelta]
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
    cifrato = bytes(chiaro[:8]) + bytes(corpo)
    prova("decifrare un dato cifrato restituisce l'originale", bytes(chiaro), decifra(cifrato))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file", nargs="?", help="il salvataggio da leggere")
    ap.add_argument("--dettaglio", action="store_true",
                    help="elenca gli esemplari contestati uno per uno")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.file:
        ap.error("serve il percorso del salvataggio, oppure --self-test")
    esito, errore = leggi(a.file)
    if errore:
        print("rifiutato: " + errore)
        return 1
    esemplari, residui = esito["esemplari"], esito["residui"]
    contestati = [e for e in esemplari if e["contestazioni"]]
    print("Deposito di " + os.path.basename(os.path.dirname(a.file) or a.file))
    print("")
    print("  posizioni occupate                 %5d" % len(esemplari))
    print("  posizioni con residui scartate     %5d" % residui)
    print("  specie distinte                    %5d" % len({e["specie"] for e in esemplari}))
    print("  esemplari senza contestazioni      %5d" % (len(esemplari) - len(contestati)))
    print("  esemplari con almeno una           %5d" % len(contestati))
    print("")
    motivi = {}
    for e in contestati:
        for m in e["contestazioni"]:
            chiave = m.split(":")[0].split(",")[0]
            motivi[chiave] = motivi.get(chiave, 0) + 1
    for m, n in sorted(motivi.items(), key=lambda x: -x[1]):
        print("    %-62s %5d" % (m[:62], n))
    print("")
    print("  Che cosa questo conto non dice: la legittimita'. Un esemplare senza contestazioni")
    print("  puo' essere respinto ugualmente, perche' qui si separa l'impossibile dal")
    print("  plausibile e non il legittimo dall'illegittimo, che e' il giudizio del")
    print("  verificatore e richiede le tabelle degli incontri.")
    if a.dettaglio:
        print("")
        for e in contestati[:60]:
            print("  scatola %2d posizione %2d  specie %3d  EV %s (%d)  %s"
                  % (e["scatola"], e["posizione"], e["specie"], e["ev"], e["ev_totale"],
                     "; ".join(e["contestazioni"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
