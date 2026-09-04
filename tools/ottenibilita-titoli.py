#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Misura quali specie siano davvero ottenibili nei titoli che parlano al deposito.

La domanda, e perche' la risposta precedente era un limite inferiore
--------------------------------------------------------------------
Il progetto ha finora risposto alla domanda sulla scadenza con il contrassegno di presenza delle
tabelle delle statistiche, cioe' con l'affermazione che una specie esiste nei dati di un gioco. Da
li' veniva il risultato per cui tutte e milleventicinque le specie sono raggiungibili per via
diretta e nessuna e' vincolata dal 26 febbraio 2027.

Quel risultato e' un limite inferiore e non la risposta, e la ragione e' che la presenza non e'
l'ottenibilita'. Un gioco moderno porta i dati di una specie anche soltanto perche' il deposito
gliela possa mandare: la specie esiste nel gioco, si puo' allenare e mostrare, e non si puo'
prendere. Contare quella specie fra le raggiungibili per via diretta significa dichiarare
raggiungibile per via diretta qualcosa che per entrare in quel gioco deve prima passare dal
deposito, che e' esattamente il contrario.

Questo programma sostituisce la presenza con l'incontro. Per ciascun titolo a via diretta legge le
tabelle degli incontri, cioe' i luoghi selvatici, gli incontri fissi, i doni, gli scambi interni e
le incursioni, e ne ricava l'insieme delle specie che quel gioco sa consegnare da se'.

La chiusura per evoluzione, che non e' un dettaglio
--------------------------------------------------
Un insieme di soli incontri sottostima di molto, perche' chi prende un Bulbasaur ottiene anche
Ivysaur e Venusaur senza che alcuna tabella li dichiari da nessuna parte. L'insieme degli incontri
va dunque chiuso rispetto alle evoluzioni del titolo, in avanti; e va chiuso anche all'indietro,
perche' dalla riproduzione si ottiene la forma base di una linea, ed e' cosi' che si prendono i
cuccioli che nessuno incontra.

La chiusura si ferma pero' dentro il titolo: si aggiunge una specie soltanto se quel titolo la
dichiara presente, poiche' un'evoluzione verso una specie che il gioco non conosce non avviene. E
resta un'approssimazione dichiarata in un punto: la chiusura all'indietro assume che una linea sia
riproducibile, che e' vero per quasi tutte e falso per i leggendari, i quali pero' non hanno
preevoluzioni e non sono quindi toccati dall'assunzione.

I due versi dell'errore, che non sono lo stesso verso
----------------------------------------------------
Questo programma sbaglia in due modi opposti, e va detto per intero perche' una prima stesura di
queste righe dichiarava soltanto il primo e concludeva che l'errore fosse tutto prudente. Non lo e'.

Il primo verso e' prudente. Le tabelle lette sono molte ma non tutte, e dove una fonte non e'
letta la specie che solo quella consegnerebbe risulta non ottenibile: si finisce per dichiarare
vincolata dalla scadenza una specie che invece si prende. Si rischia cioe' di lavorare su qualcosa
che non serviva, che su una scadenza e' il rischio accettabile.

Il secondo verso non lo e'. Gli incontri scritti in codice si leggono con una regola generosa, che
prende sia le righe con la specie dichiarata per nome di campo sia quelle il cui costruttore
comincia con un numero, perche' le tabelle usano entrambe le forme. Una lettura generosa puo'
raccogliere un numero che specie non e', e allora una specie risulterebbe ottenibile senza esserlo:
si perderebbe qualcosa per sempre. Il presidio contro questo non e' un controllo automatico ma una
verifica fatta a mano il 2026-09-04 sulle cinquanta specie che soltanto quella lettura aggiunge,
campionandone sei fra le piu' sospette, cioe' i mitici: tutte e sei venivano da righe di incontro
vere. Chi tocchi quella regola rifaccia il campione.

Il programma elenca in chiaro le tabelle lette per ciascun titolo, cosicche' il primo verso si
possa stringere aggiungendone.

Uso
---
    python tools/ottenibilita-titoli.py --pkhex _notes/fonti/pkhex
    python tools/ottenibilita-titoli.py --pkhex <clone> --markdown <file.md>
    python tools/ottenibilita-titoli.py --self-test
"""

import argparse
import io
import os
import re
import struct
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "tools"))
WILD = os.path.join("PKHeX.Core", "Resources", "legality", "wild")
EVOLVE = os.path.join("PKHeX.Core", "Resources", "byte", "evolve")
PERSONAL = os.path.join("PKHeX.Core", "Resources", "byte", "personal")
DATI = os.path.join("PKHeX.Core", "Legality", "Encounters", "Data")

MAX_SPECIE = 1025


# --------------------------------------------------------------------------------------------
# I titoli a via diretta, cioe' quelli che parlano al deposito senza passare dalla banca.
#
# Per ciascuno: la tabella delle statistiche con i suoi offset, la tabella delle evoluzioni, i
# file degli incontri selvatici con il loro formato di area, i file binari di incontri fissi, e i
# file di codice da cui si prendono incontri fissi, doni e scambi.
#
# I formati di area sono quattro e vengono dalle classi EncounterArea del verificatore, lette il
# 2026-09-04. Si chiamano qui con il nome della loro generazione perche' e' cosi' che la fonte li
# distingue: '7b' e '8b' hanno intestazione di quattro byte e posizioni di quattro, '9' ha
# intestazione di quattro e posizioni di otto, '8' ha una intestazione di due byte seguita da
# gruppi con sei byte di testata ciascuno e posizioni di due byte in cui la forma sta nei cinque
# bit alti, e '8a' ha una intestazione di lunghezza variabile allineata a due.
TITOLI = (
    {
        "sigla": "LGPE", "nome": "Let's Go Pikachu ed Eevee",
        "personal": ("personal_gg", 0x54, 0x1C, 0x20, None, 809),
        "evoluzioni": "evos_gg.pkl",
        "selvatici": (("Gen7/encounter_gp.pkl", "7b"), ("Gen7/encounter_ge.pkl", "7b")),
        "binari": (),
        "codice": ("Gen7/Encounters7GG.cs",),
    },
    {
        "sigla": "SwSh", "nome": "Spada e Scudo",
        "personal": ("personal_swsh", 0xB0, 0x1E, 0x20, ("bit", 0x21, 6), 898),
        "evoluzioni": "evos_ss.pkl",
        "selvatici": (("Gen8/encounter_sw_symbol.pkl", "8"), ("Gen8/encounter_sh_symbol.pkl", "8"),
                      ("Gen8/encounter_sw_hidden.pkl", "8"), ("Gen8/encounter_sh_hidden.pkl", "8")),
        # I nidi non sono aree ma una serie piatta di record da dieci byte: la loro classe e'
        # EncounterStatic8N e non EncounterArea8, e trattarli come aree e' l'errore che il primo
        # tentativo ha fatto. Il programma se ne e' accorto perche' l'archivio non si e' aperto,
        # non perche' il numero fosse strano.
        "binari": (("Gen8/encounter_sw_dist.pkl", 0x10, 0x00, 0x02),
                   ("Gen8/encounter_sh_dist.pkl", 0x10, 0x00, 0x02),
                   ("Gen8/encounter_sw_nest.pkl", 10, 0x00, 0x02),
                   ("Gen8/encounter_sh_nest.pkl", 10, 0x00, 0x02),
                   ("Gen8/encounter_swsh_underground.pkl", 14, 0x00, 0x02)),
        "codice": ("Gen8/Encounters8.cs", "Gen8/Encounters8Nest.cs"),
    },
    {
        "sigla": "BDSP", "nome": "Diamante Lucente e Perla Splendente",
        "personal": ("personal_bdsp", 0x44, 0x1E, 0x20, ("bit", 0x21, 6), 493),
        "evoluzioni": "evos_bs.pkl",
        "selvatici": (("Gen8/encounter_bd.pkl", "8b"), ("Gen8/encounter_sp.pkl", "8b"),
                      ("Gen8/encounter_bd_underground.pkl", "8b"),
                      ("Gen8/encounter_sp_underground.pkl", "8b")),
        "binari": (),
        "codice": ("Gen8/Encounters8b.cs",),
    },
    {
        "sigla": "PLA", "nome": "Leggende Arceus",
        "personal": ("personal_la", 0xB0, 0x1E, 0x20, ("bit", 0x21, 6), 905),
        "evoluzioni": "evos_la.pkl",
        "selvatici": (("Gen8/encounter_la.pkl", "8a"),),
        "binari": (),
        "codice": ("Gen8/Encounters8a.cs",),
    },
    {
        "sigla": "SV", "nome": "Scarlatto e Violetto",
        "personal": ("personal_sv", 0x50, 0x18, 0x1A, ("byte", 0x1C), MAX_SPECIE),
        "evoluzioni": "evos_sv.pkl",
        "selvatici": (("Gen9/encounter_wild_paldea.pkl", "9"),),
        "binari": (("Gen9/encounter_dist_paldea.pkl", 62, 0x00, 0x02),
                   ("Gen9/encounter_might_paldea.pkl", 62, 0x00, 0x02),
                   ("Gen9/encounter_fixed_paldea.pkl", 0x14, 0x00, 0x02),
                   ("Gen9/encounter_outbreak_paldea.pkl", 0xC + 16, 0x00, 0x02),
                   ("Gen9/encounter_gem_paldea.pkl", 0x18, 0x00, 0x02),
                   ("Gen9/encounter_gem_kitakami.pkl", 0x18, 0x00, 0x02),
                   ("Gen9/encounter_gem_blueberry.pkl", 0x18, 0x00, 0x02)),
        "codice": ("Gen9/Encounters9.cs",),
    },
    {
        "sigla": "Z-A", "nome": "Leggende Z-A",
        "personal": ("personal_za", 0x50, 0x18, 0x1A, ("byte", 0x1C), MAX_SPECIE),
        "evoluzioni": "evos_za.pkl",
        # Le aree di Z-A stanno in un archivio con posizioni a sedici bit e non a trentadue, che
        # e' la differenza fra le due classi gemelle del verificatore: il formato si chiama qui
        # '9a' proprio per portarla, perche' la disposizione interna dell'area e' invece identica
        # a quella di Scarlatto e Violetto.
        "selvatici": (("Gen9/encounter_za.pkl", "9a"),
                      ("Gen9/encounter_hyperspace_za.pkl", "9a")),
        "binari": (),
        "codice": ("Gen9/Encounters9a.cs",),
    },
)


# --------------------------------------------------------------------------------------------
# Lettura degli archivi indicizzati
# --------------------------------------------------------------------------------------------

def aree(dati, larghezza):
    """Le aree di un archivio indicizzato, con la tabella delle posizioni a 32 o a 16 bit.

    I due archivi differiscono solo per l'ampiezza delle posizioni, e la fonte li tiene in due
    classi gemelle: quello degli incontri usa interi a trentadue bit, quello delle evoluzioni a
    sedici. In entrambi la fine di un'area coincide con l'inizio della successiva, quindi la
    posizione si legge come un intero doppio a partire dalla voce i-esima.
    """
    if len(dati) < 4:
        return None
    quante = struct.unpack_from("<H", dati, 2)[0]
    fuori = []
    for i in range(quante):
        off = 4 + i * larghezza
        if larghezza == 4:
            if off + 8 > len(dati):
                return None
            coppia = struct.unpack_from("<Q", dati, off)[0]
            inizio, fine = coppia & 0xFFFFFFFF, coppia >> 32
        else:
            if off + 4 > len(dati):
                return None
            coppia = struct.unpack_from("<I", dati, off)[0]
            inizio, fine = coppia & 0xFFFF, coppia >> 16
        if not (0 <= inizio <= fine <= len(dati)):
            return None
        fuori.append(dati[inizio:fine])
    return fuori


def specie_selvatiche(dati, formato):
    """Le specie delle posizioni selvatiche di un archivio, secondo il formato della sua area."""
    blocchi = aree(dati, 2 if formato == "9a" else 4)
    if blocchi is None:
        return None
    fuori = set()
    for area in blocchi:
        if formato in ("7b", "8b"):
            corpo = area[4:]
            for off in range(0, len(corpo) - 3, 4):
                sp = struct.unpack_from("<H", corpo, off)[0]
                if 1 <= sp <= MAX_SPECIE:
                    fuori.add(sp)
        elif formato in ("9", "9a"):
            corpo = area[4:]
            for off in range(0, len(corpo) - 7, 8):
                sp = struct.unpack_from("<H", corpo, off)[0]
                if 1 <= sp <= MAX_SPECIE:
                    fuori.add(sp)
        elif formato == "8":
            if len(area) < 2:
                continue
            quante = area[1]
            letti, off = 0, 2
            while letti < quante and off + 6 <= len(area):
                conto = area[off + 4]
                off += 6
                for _ in range(conto):
                    if off + 2 > len(area) or letti >= quante:
                        break
                    grezzo = struct.unpack_from("<H", area, off)[0]
                    sp = grezzo & 0x3FF
                    if 1 <= sp <= MAX_SPECIE:
                        fuori.add(sp)
                    off += 2
                    letti += 1
        elif formato == "8a":
            if len(area) < 1:
                continue
            quanti_luoghi = area[0]
            allinea = quanti_luoghi + 1
            allinea += allinea & 1
            corpo = area[allinea:]
            if len(corpo) < 2:
                continue
            quante = corpo[1]
            posizioni = corpo[2:]
            for i in range(quante):
                off = i * 8
                if off + 8 > len(posizioni):
                    break
                sp = struct.unpack_from("<H", posizioni, off)[0]
                if 1 <= sp <= MAX_SPECIE:
                    fuori.add(sp)
        else:
            return None
    return fuori


def specie_binario(dati, passo, off_specie, _off_forma):
    """Le specie di una tabella a record di lunghezza fissa."""
    quante, resto = divmod(len(dati), passo)
    if resto:
        return None
    fuori = set()
    for i in range(quante):
        sp = struct.unpack_from("<H", dati, i * passo + off_specie)[0]
        if 1 <= sp <= MAX_SPECIE:
            fuori.add(sp)
    return fuori


def specie_da_codice(testo):
    """Le specie nominate da una tabella di incontri scritta in codice.

    Si prendono sia le righe con `Species = N` sia quelle il cui costruttore comincia con un
    numero, perche' le tabelle del verificatore usano entrambe le forme e nessuna delle due
    copre l'altra. E' una lettura generosa e lo si dichiara: puo' raccogliere qualche numero che
    specie non e', e su questo programma l'errore generoso e' quello innocuo, perche' una specie
    in piu' fra le ottenibili non fa perdere nulla mentre una in meno farebbe lavorare a vuoto.
    """
    fuori = set()
    for riga in testo.splitlines():
        nuda = riga.lstrip()
        if nuda.startswith("//") or "new(" not in nuda:
            continue
        taglio = riga.find("//")
        if taglio >= 0:
            riga = riga[:taglio]
        m = re.search(r"Species\s*=\s*(\d+)", riga)
        if m:
            sp = int(m.group(1))
            if 1 <= sp <= MAX_SPECIE:
                fuori.add(sp)
            continue
        m = re.search(r"new\(\s*(\d{1,4})\s*,\s*\d+", riga)
        if m:
            sp = int(m.group(1))
            if 1 <= sp <= MAX_SPECIE:
                fuori.add(sp)
    return fuori


# --------------------------------------------------------------------------------------------
# Tabelle delle statistiche e delle evoluzioni
# --------------------------------------------------------------------------------------------

def presente(rec, modo):
    if modo is None:
        return True
    if modo[0] == "bit":
        return ((rec[modo[1]] >> modo[2]) & 1) == 1
    return rec[modo[1]] != 0


def mappa_personale(pkhex, nome, size, off_fsi, off_fc, modo, maxsp):
    """Le specie presenti nel titolo, e la corrispondenza fra indice di tabella e specie.

    La seconda serve alle evoluzioni, che sono indicizzate per riga della tabella delle
    statistiche e non per numero di specie: senza la corrispondenza si leggerebbero evoluzioni
    attribuite alla specie sbagliata, che e' un errore invisibile perche' il risultato resta un
    numero di specie valido.
    """
    p = os.path.join(pkhex, PERSONAL, nome)
    if not os.path.exists(p):
        return None, None
    d = io.open(p, "rb").read()
    n = len(d) // size
    presenti, indice_a_specie = set(), {}
    for sp in range(1, min(maxsp, n - 1) + 1):
        base = d[sp * size:(sp + 1) * size]
        if len(base) < size:
            break
        indice_a_specie[sp] = sp
        if presente(base, modo):
            presenti.add(sp)
        fc = base[off_fc]
        fsi = struct.unpack_from("<H", base, off_fsi)[0]
        for f in range(1, max(fc, 1)):
            idx = fsi + f - 1
            if idx <= 0 or (idx + 1) * size > len(d):
                continue
            indice_a_specie[idx] = sp
            if presente(d[idx * size:(idx + 1) * size], modo):
                presenti.add(sp)
    return presenti, indice_a_specie


def archi_evoluzione(pkhex, nome, indice_a_specie):
    """Gli archi da specie a specie che il titolo dichiara, letti dalla sua tabella.

    Ogni voce dell'archivio corrisponde a una riga della tabella delle statistiche, cioe' a una
    coppia di specie e forma, e porta record da otto byte in cui la specie di destinazione sta a
    quattro. Si collassa tutto al livello di specie, perche' e' il livello a cui questo programma
    risponde.
    """
    p = os.path.join(pkhex, EVOLVE, nome)
    if not os.path.exists(p):
        return None
    blocchi = aree(io.open(p, "rb").read(), 2)
    if blocchi is None:
        return None
    archi = []
    for indice, blocco in enumerate(blocchi):
        da = indice_a_specie.get(indice)
        if da is None:
            continue
        for off in range(0, len(blocco) - 7, 8):
            a = struct.unpack_from("<H", blocco, off + 4)[0]
            if 1 <= a <= MAX_SPECIE and a != da:
                archi.append((da, a))
    return archi


def chiudi(seme, archi, presenti):
    """La chiusura dell'insieme degli incontri rispetto alle evoluzioni, nei due versi.

    In avanti perche' chi prende la forma base ottiene le evolute; all'indietro perche' dalla
    riproduzione si ottiene la forma base di una linea. La chiusura si ferma su cio' che il
    titolo dichiara presente, poiche' un'evoluzione verso una specie che il gioco non conosce non
    avviene.
    """
    avanti, indietro = {}, {}
    for da, a in archi:
        avanti.setdefault(da, set()).add(a)
        indietro.setdefault(a, set()).add(da)
    fuori = set(s for s in seme if s in presenti)
    coda = list(fuori)
    while coda:
        s = coda.pop()
        for vicino in list(avanti.get(s, ())) + list(indietro.get(s, ())):
            if vicino in presenti and vicino not in fuori:
                fuori.add(vicino)
                coda.append(vicino)
    return fuori


# --------------------------------------------------------------------------------------------

def doni_senza_scadenza(pkhex):
    """Le specie consegnate come dono nelle generazioni che parlano al deposito direttamente.

    Vanno contate fra le raggiungibili senza banca, ed e' una correzione a un modello che questo
    programma aveva sbagliato al primo tentativo. Un dono non e' un incontro e nessuna tabella
    degli incontri lo dichiara, ma un esemplare consegnato in ottava o nona generazione, o nei due
    titoli di Let's Go, arriva al deposito senza toccare la banca: dire che dipende dalla scadenza
    sarebbe falso. La distribuzione puo' essere chiusa da anni, e allora quell'esemplare e'
    difficile da procurarsi, ma la difficolta' non e' la scadenza e le due non si confondono.

    Restituisce anche il motivo in caso di fallimento, invece di un insieme vuoto che sembrerebbe
    una misura.
    """
    import importlib.util
    percorso = os.path.join(RADICE, "tools", "conteggio-doni-moderni.py")
    if not os.path.exists(percorso):
        return None, "manca tools/conteggio-doni-moderni.py"
    spec = importlib.util.spec_from_file_location("conteggio", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    righe, _antichi, _difetti = modulo.conta(pkhex)
    fuori = set()
    for r in righe:
        if r.get("letti") and not r.get("sotto_scadenza"):
            fuori |= set(r.get("specie", ()))
    return fuori, None


def misura(pkhex):
    titoli, difetti = [], []
    for t in TITOLI:
        nome_p, size, off_fsi, off_fc, modo, maxsp = t["personal"]
        presenti, indice_a_specie = mappa_personale(pkhex, nome_p, size, off_fsi, off_fc, modo,
                                                    maxsp)
        if presenti is None:
            difetti.append((t["sigla"], "manca la tabella delle statistiche " + nome_p))
            continue
        incontri, lette, mancate = set(), [], []
        for relativo, formato in t["selvatici"]:
            p = os.path.join(pkhex, WILD, relativo.replace("/", os.sep))
            if not os.path.exists(p):
                mancate.append(relativo)
                continue
            trovate = specie_selvatiche(io.open(p, "rb").read(), formato)
            if trovate is None:
                difetti.append((t["sigla"], "il formato di area %s non ha risposto su %s"
                                % (formato, relativo)))
                mancate.append(relativo)
                continue
            incontri |= trovate
            lette.append(relativo)
        for relativo, passo, o_s, o_f in t["binari"]:
            p = os.path.join(pkhex, WILD, relativo.replace("/", os.sep))
            if not os.path.exists(p):
                mancate.append(relativo)
                continue
            trovate = specie_binario(io.open(p, "rb").read(), passo, o_s, o_f)
            if trovate is None:
                difetti.append((t["sigla"], "il passo %d non divide %s" % (passo, relativo)))
                mancate.append(relativo)
                continue
            incontri |= trovate
            lette.append(relativo)
        for relativo in t["codice"]:
            p = os.path.join(pkhex, DATI, relativo.replace("/", os.sep))
            if not os.path.exists(p):
                mancate.append(relativo)
                continue
            incontri |= specie_da_codice(io.open(p, encoding="utf-8").read())
            lette.append(relativo)
        archi = archi_evoluzione(pkhex, t["evoluzioni"], indice_a_specie)
        if archi is None:
            difetti.append((t["sigla"], "manca la tabella delle evoluzioni " + t["evoluzioni"]))
            archi = []
        ottenibili = chiudi(incontri, archi, presenti)
        titoli.append({
            "sigla": t["sigla"], "nome": t["nome"],
            "presenti": presenti, "incontri": incontri & presenti, "ottenibili": ottenibili,
            "archi": len(archi), "lette": lette, "mancate": mancate,
        })
    doni, errore = doni_senza_scadenza(pkhex)
    if errore:
        difetti.append(("doni senza scadenza", errore))
        doni = set()
    return titoli, difetti, doni


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    # archivio indicizzato a 32 bit: due aree, ciascuna con intestazione di quattro byte e
    # posizioni di quattro, cioe' il formato di Let's Go e di Diamante Lucente.
    testa = b"xx" + struct.pack("<H", 2)
    tabella = struct.pack("<II", 16, 24) + struct.pack("<I", 32)
    a1 = struct.pack("<HH", 7, 0) + struct.pack("<HH", 25, 0)          # 8 byte
    a2 = struct.pack("<HH", 1, 0) + struct.pack("<HH", 4, 0)           # 8 byte
    dati = testa + tabella + b"\x00" * (16 - len(testa) - len(tabella)) + a1 + a2
    prova("archivio a 32 bit, quante aree", 2, len(aree(dati, 4) or []))
    prova("selvatici, formato 7b", {25, 4}, specie_selvatiche(dati, "7b"))

    # record di lunghezza fissa
    fisso = struct.pack("<HH", 150, 0) + struct.pack("<HH", 151, 0)
    prova("binario a passo 4", {150, 151}, specie_binario(fisso, 4, 0, 2))
    prova("binario con passo sbagliato", None, specie_binario(fisso + b"\x00", 4, 0, 2))

    # lettura dal codice
    codice = """
        new(SWSH) { Species = 782, Level = 16 }, // Jangmo-o
        new(025, 05) { Location = 1 }, // Pikachu
        // new(026, 05), // commentata
    """
    prova("dal codice", {782, 25}, specie_da_codice(codice))

    # chiusura: da Bulbasaur si arriva a Venusaur e viceversa, e non si esce dai presenti
    archi = [(1, 2), (2, 3), (10, 11)]
    prova("chiusura in avanti", {1, 2, 3}, chiudi({1}, archi, {1, 2, 3, 10, 11}))
    prova("chiusura all'indietro", {1, 2, 3}, chiudi({3}, archi, {1, 2, 3, 10, 11}))
    prova("chiusura fermata dalla presenza", {1, 2}, chiudi({1}, archi, {1, 2}))
    prova("seme non presente scartato", set(), chiudi({99}, archi, {1, 2}))

    # solo da dono: l'insieme deve stare dentro i doni e non toccare gli incontri
    prova("solo da dono", {7}, solo_da_dono({1, 7}, {1, 2, 3}))
    prova("solo da dono, nessuno", set(), solo_da_dono({1}, {1, 2}))
    prova("solo da dono, doni vuoti", set(), solo_da_dono(set(), {1, 2}))
    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def solo_da_dono(doni, in_gioco):
    """Le specie che soltanto un dono consegna, cioe' quelle nei doni e non negli incontri.

    E' una riga sola e ha una funzione propria perche' la prima scrittura era sbagliata: sottraeva
    i doni da un'unione che i doni li conteneva gia', operazione priva di senso che restituiva
    mezzo Pokedex. Il difetto si e' visto perche' fra i nomi comparivano specie che in gioco si
    prendono di sicuro, e non perche' il conto fosse strano; ora e' coperto da una prova.
    """
    return doni - in_gioco


def stampa(titoli, difetti, nomi, doni):
    print("Ottenibilita' nei titoli a via diretta")
    print("")
    print("  %-6s %-38s %8s %10s %12s" % ("sigla", "titolo", "presenti", "incontri", "ottenibili"))
    unione_pres, unione_ott = set(), set()
    for t in titoli:
        print("  %-6s %-38s %8d %10d %12d"
              % (t["sigla"], t["nome"][:38], len(t["presenti"]), len(t["incontri"]),
                 len(t["ottenibili"])))
        unione_pres |= t["presenti"]
        unione_ott |= t["ottenibili"]
    print("")
    print("  specie dai doni delle generazioni a via diretta: %d" % len(doni))
    print("")
    print("  unione delle presenti:              %4d su %d" % (len(unione_pres), MAX_SPECIE))
    print("  unione delle ottenibili in gioco:   %4d su %d" % (len(unione_ott), MAX_SPECIE))
    in_gioco = set(unione_ott)
    unione_ott = unione_ott | doni
    print("  unione con i doni a via diretta:    %4d su %d" % (len(unione_ott), MAX_SPECIE))
    vincolate = set(range(1, MAX_SPECIE + 1)) - unione_ott
    print("")
    print("  SPECIE VINCOLATE DALLA SCADENZA: %d" % len(vincolate))
    print("  cioe' quelle che nessun titolo a via diretta sa consegnare da se', e che per")
    print("  arrivare al deposito devono passare dalla banca entro il 26 febbraio 2027.")
    if vincolate:
        print("")
        for s in sorted(vincolate):
            print("    %4d %s" % (s, nomi.get(s, "?")))
    # Le specie che soltanto un dono consegna: stanno nell'insieme dei doni e non in quello degli
    # incontri. La prima scrittura di questa riga sottraeva i doni dall'unione gia' unita ai doni,
    # che e' un'operazione priva di senso e restituiva mezzo Pokedex: il difetto si e' visto
    # perche' fra i nomi comparivano specie che in gioco si prendono di sicuro, non perche' il
    # conto fosse strano.
    solo_dono = sorted(solo_da_dono(doni, in_gioco))
    print("")
    print("  Specie senza alcun incontro in un titolo a via diretta: %d" % len(solo_dono))
    print("  Non sono vincolate dalla scadenza, perche' il dono che le consegna sta in una")
    print("  generazione che parla al deposito direttamente, ma non si prendono in alcun gioco:")
    print("  l'unica via e' un esemplare da distribuzione, quindi stanno sull'asse degli eventi.")
    for s in solo_dono:
        print("    %4d %s" % (s, nomi.get(s, "?")))
    if difetti:
        print("")
        for sigla, motivo in difetti:
            print("  difetto: %s: %s" % (sigla, motivo))
    return vincolate, unione_ott, unione_pres, in_gioco


def scrivi(percorso, titoli, difetti, nomi, vincolate, unione_ott, unione_pres, doni,
           in_gioco):
    r = []
    r.append("# Ottenibilità nei titoli a via diretta")
    r.append("")
    r.append("> Documento generato da `tools/ottenibilita-titoli.py`. Non si modifica a mano: si "
             "rigenera. La fonte sono le tabelle degli incontri, delle statistiche e delle "
             "evoluzioni di PKHeX, lette dal clone passato sulla riga di comando.")
    r.append("")
    r.append("Questo documento sostituisce una risposta che il progetto dava da giorni e che era "
             "un limite inferiore travestito da risultato. La domanda è quali specie la chiusura "
             "della banca porti via, e fino al 2026-09-04 la risposta veniva dal contrassegno di "
             "presenza delle tabelle delle statistiche, cioè dall'affermazione che una specie "
             "esiste nei dati di un gioco. La presenza però non è l'ottenibilità: un gioco "
             "moderno porta i dati di una specie anche soltanto perché il deposito gliela possa "
             "mandare, e quella specie si può allenare e mostrare ma non prendere. Contarla fra "
             "le raggiungibili per via diretta significa dichiarare raggiungibile senza banca "
             "qualcosa che per entrare in quel gioco dalla banca deve passare.")
    r.append("")
    r.append("Qui la presenza è sostituita dall'incontro. Per ciascun titolo si leggono le "
             "tabelle dei luoghi selvatici, degli incontri fissi, dei doni, degli scambi interni "
             "e delle incursioni, e se ne ricava l'insieme delle specie che quel gioco sa "
             "consegnare da sé. L'insieme viene poi chiuso rispetto alle evoluzioni del titolo, "
             "nei due versi: in avanti perché chi prende un Bulbasaur ottiene anche Venusaur "
             "senza che alcuna tabella lo dichiari, e all'indietro perché dalla riproduzione si "
             "ottiene la forma base di una linea, che è il modo in cui si prendono i cuccioli che "
             "nessuno incontra. La chiusura si ferma su ciò che il titolo dichiara presente, "
             "poiché un'evoluzione verso una specie che il gioco non conosce non avviene.")
    r.append("")
    r.append("## Il conto per titolo")
    r.append("")
    r.append("| Sigla | Titolo | Presenti nei dati | Con un incontro | Ottenibili dopo la chiusura |")
    r.append("|---|---|---|---|---|")
    for t in titoli:
        r.append("| %s | %s | %d | %d | %d |"
                 % (t["sigla"], t["nome"], len(t["presenti"]), len(t["incontri"]),
                    len(t["ottenibili"])))
    r.append("")
    r.append("A questi si aggiungono le %d specie consegnate come dono nelle generazioni che "
             "parlano al deposito direttamente, cioè l'ottava, la nona e i due titoli di Let's "
             "Go. Vanno contate, e la ragione va detta perché il primo tentativo di questa misura "
             "le aveva dimenticate: un dono non è un incontro e nessuna tabella degli incontri lo "
             "dichiara, ma un esemplare consegnato in quelle generazioni arriva al deposito senza "
             "toccare la banca. Che la distribuzione sia chiusa da anni lo rende difficile da "
             "procurarsi, non lo rende vincolato dalla scadenza, e le due cose non si confondono."
             % len(doni))
    r.append("")
    r.append("L'unione delle specie presenti nei dati dei sei titoli è %d su %d, ed è il numero "
             "da cui veniva il risultato vecchio. L'unione delle specie ottenibili in gioco è %d, "
             "e con i doni a via diretta sale a %d. La differenza fra la presenza e "
             "l'ottenibilità è %d: sono le specie che esistono nei dati di un gioco moderno senza "
             "che quel gioco le sappia consegnare in alcun modo."
             % (len(unione_pres), MAX_SPECIE, len(in_gioco),
                len(unione_ott), len(unione_pres) - len(unione_ott)))
    r.append("")
    r.append("## Le specie che la scadenza vincola davvero")
    r.append("")
    r.append("Sono %d, e sono quelle che nessun titolo a via diretta sa consegnare da sé: per "
             "arrivare al deposito devono passare dalla banca, quindi entro il 26 febbraio 2027 "
             "o mai più." % len(vincolate))
    r.append("")
    if vincolate:
        r.append("| Dex | Specie |")
        r.append("|---|---|")
        for s in sorted(vincolate):
            r.append("| %d | %s |" % (s, nomi.get(s, "?")))
    else:
        r.append("Nessuna. Il risultato precedente regge anche alla misura severa, e ora è un "
                 "risultato misurato invece di un limite inferiore: la differenza non è nel "
                 "numero ma in ciò che il numero significa.")
    r.append("")
    solo_dono = sorted(solo_da_dono(doni, in_gioco))
    r.append("## Le specie che nessun gioco moderno sa far prendere")
    r.append("")
    r.append("Sono %d, e sono il risultato nuovo di questa misura. Non sono vincolate dalla "
             "scadenza, perché il dono che le consegna sta in una generazione che parla al "
             "deposito direttamente; ma non hanno alcun incontro in alcuno dei sei titoli, quindi "
             "l'unica via per averle è un esemplare da distribuzione. Stanno cioè sull'asse degli "
             "eventi e non su quello delle specie, e chi pianificasse di prenderle giocando "
             "perderebbe il proprio tempo." % len(solo_dono))
    r.append("")
    if solo_dono:
        r.append("| Dex | Specie |")
        r.append("|---|---|")
        for s in solo_dono:
            r.append("| %d | %s |" % (s, nomi.get(s, "?")))
        r.append("")
    r.append("## Il verso dell'errore, e come stringere il limite")
    r.append("")
    r.append("Questa misura sbaglia in due modi opposti, e vanno detti entrambi perché una prima "
             "stesura dichiarava soltanto il primo e concludeva che l'errore fosse tutto "
             "prudente. Non lo è.")
    r.append("")
    r.append("Il primo verso è prudente. Le tabelle lette sono molte ma non tutte, e dove una "
             "fonte non è letta la specie che solo quella consegnerebbe risulta non ottenibile: "
             "si finisce per dichiarare vincolata dalla scadenza una specie che invece si prende, "
             "cioè si lavora su qualcosa che non serviva. Su una scadenza è il rischio "
             "accettabile.")
    r.append("")
    r.append("Il secondo verso non lo è. Gli incontri scritti in codice si leggono con una regola "
             "generosa, che accetta sia le righe con la specie dichiarata per nome di campo sia "
             "quelle il cui costruttore comincia con un numero, perché le tabelle usano entrambe "
             "le forme e nessuna copre l'altra. Una lettura generosa può raccogliere un numero "
             "che specie non è, e allora una specie risulterebbe ottenibile senza esserlo: quella "
             "si perderebbe per sempre. Il presidio non è automatico ma è una verifica fatta a "
             "mano il 2026-09-04 sulle cinquanta specie che soltanto quella lettura aggiunge, con "
             "sei campionate fra le più sospette, cioè i mitici Keldeo, Genesect, Marshadow, "
             "Zeraora, Mew e Manaphy: tutte e sei venivano da righe di incontro vere, in Leggende "
             "Z-A le prime quattro, in Diamante Lucente Mew e in Leggende Arceus Manaphy. Chi "
             "tocchi quella regola rifaccia il campione.")
    r.append("")
    r.append("Il primo verso si stringe aggiungendo tabelle, e quelle lette per ciascun titolo "
             "sono elencate qui sotto perché si veda che cosa manchi.")
    r.append("")
    r.append("| Sigla | Tabelle lette | Tabelle dichiarate e non trovate |")
    r.append("|---|---|---|")
    for t in titoli:
        r.append("| %s | %s | %s |"
                 % (t["sigla"], ", ".join("`%s`" % x for x in t["lette"]) or "nessuna",
                    ", ".join("`%s`" % x for x in t["mancate"]) or "nessuna"))
    r.append("")
    if difetti:
        r.append("## Difetti dichiarati")
        r.append("")
        for sigla, motivo in difetti:
            r.append("- %s: %s" % (sigla, motivo))
        r.append("")
    io.open(percorso, "w", encoding="utf-8", newline="").write("\n".join(r) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", help="clone del verificatore")
    ap.add_argument("--markdown", help="scrive la misura come documento tracciato")
    ap.add_argument("--self-test", action="store_true", dest="self_test",
                    help="controlla i lettori su dati di prova, senza toccare il clone")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.pkhex:
        ap.error("serve --pkhex, oppure --self-test")
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "disp", os.path.join(RADICE, "tools", "disponibilita-titoli.py"))
    disp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(disp)
    nomi = {}
    try:
        per_nome = disp.specie_per_nome(a.pkhex)
        nomi = {v: k for k, v in per_nome.items()}
    except Exception as exc:
        print("  nota: i nomi delle specie non si sono caricati (%s)" % exc)
    titoli, difetti, doni = misura(a.pkhex)
    vincolate, unione_ott, unione_pres, in_gioco = stampa(titoli, difetti, nomi, doni)
    if a.markdown:
        scrivi(a.markdown, titoli, difetti, nomi, vincolate, unione_ott, unione_pres, doni,
               in_gioco)
        print("")
        print("  scritto " + a.markdown)
    return 0


if __name__ == "__main__":
    sys.exit(main())
