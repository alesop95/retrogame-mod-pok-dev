#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera gli esemplari da evento di prima e seconda generazione, e li documenta uno per uno.

Perché esiste, e perché è il primo tempo della roadmap
-----------------------------------------------------
Il 2026-09-03 il conteggio delle voci da evento ha portato un risultato che contraddice
l'intuizione e riordina l'ordine di lavoro: prima e seconda generazione sono le meno costose e
non le più costose. Non hanno doni segreti, perché quel meccanismo non esisteva, e i loro eventi
sono descritti da tabelle di incontro a record di lunghezza fissa con i campi in chiaro, otto
byte per la prima e dodici per la seconda.

Il punto che decide tutto è che in quelle generazioni non esiste alcun valore di personalità e
nessun generatore pseudocasuale da ricostruire: natura, sesso, lucentezza e caratteristiche non
derivano da un seme. La terza generazione ha richiesto settimane perché il valore di personalità
determina metà dei campi e va trovato per ricerca inversa; qui non c'è nulla da trovare. Comporre
un esemplare significa scrivere una struttura con campi noti, che è ciò che `pokebridge` sa già
fare e ha verificato.

La conseguenza sulla fedeltà, che è l'immagine speculare della terza generazione
-------------------------------------------------------------------------------
Vale enunciarla perché è un risultato e non un limite dello strumento. In terza generazione il
seme determina valore di personalità e valori individuali insieme, quindi dato un esemplare
autentico la ricerca inversa ne ricava il seme e la fedeltà di una ricreazione è decidibile: si
confrontano i semi. In prima e seconda generazione i valori individuali furono estratti dal gioco
al momento della consegna e non derivano da nulla che l'esemplare porti con sé, quindi la fedeltà
su quel campo non è decidibile nemmeno in principio.

Ne segue una asimmetria fra le due nozioni che il progetto già distingue. La legittimità qui è
banale, perché qualunque combinazione di valori individuali è legale; la fedeltà è impossibile,
perché nessuna informazione la determina. Dove la terza generazione permetteva di dimostrare la
fedeltà e rendeva difficile la legittimità, queste due fanno l'opposto. Questo programma dichiara
quindi i valori individuali come una scelta e non come una ricostruzione, e li scrive dove la
fonte li fissa, cioè per gli esemplari dei tour, dove sono parte dell'evento.

Uso
---
    python tools/genera-evento-gb.py --pkhex <clone> --elenca
    python tools/genera-evento-gb.py --pkhex <clone> --lotto --destinazione _notes/lotto-gb
    python tools/genera-evento-gb.py --pkhex <clone> --schede pokedex-home-completo/SCHEDE-EVENTI-GB.md
    python tools/genera-evento-gb.py --self-test
"""

import argparse
import hashlib
import importlib.util
import io
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))

MGDB = os.path.join("PKHeX.Core", "Resources", "legality", "mgdb")
PERSONAL = os.path.join("PKHeX.Core", "Resources", "byte", "personal")
NOMI_SPECIE = os.path.join("PKHeX.Core", "Resources", "text", "other", "it",
                           "text_Species_it.txt")
NOMI_MOSSE = os.path.join("PKHeX.Core", "Resources", "text", "other", "it",
                          "text_Moves_it.txt")
PROVENIENZE = os.path.join(RADICE, "recreate-pokemon-distributions-events",
                           "provenienze-eventi-gb.json")

# ---------------------------------------------------------------------------------------------
# Tabelle trascritte dalla fonte, con la loro provenienza accanto
# ---------------------------------------------------------------------------------------------
# La corrispondenza fra numero del Dex Nazionale e identificativo interno di prima generazione,
# da PKHeX.Core/PKM/Util/Conversion/SpeciesConverter.cs, campo Table1NationalToInternal, letto il
# 2026-09-03. Serve perché la prima generazione non numera le specie come il Dex: la tabella degli
# eventi porta il numero nazionale e la struttura vuole quello interno, e confonderli scambia una
# specie con un'altra. È lo stesso rischio che il progetto ha già incontrato fra la numerazione
# nazionale e quella di terza generazione, e la stessa cura si applica: il self-test verifica la
# corrispondenza su specie di controllo e l'iniettività della tabella.
NAZIONALE_A_INTERNO_1 = [
    0x00, 0x99, 0x09, 0x9A, 0xB0, 0xB2, 0xB4, 0xB1, 0xB3, 0x1C, 0x7B, 0x7C, 0x7D, 0x70, 0x71,
    0x72, 0x24, 0x96, 0x97, 0xA5, 0xA6, 0x05, 0x23, 0x6C, 0x2D, 0x54, 0x55, 0x60, 0x61, 0x0F,
    0xA8, 0x10, 0x03, 0xA7, 0x07, 0x04, 0x8E, 0x52, 0x53, 0x64, 0x65, 0x6B, 0x82, 0xB9, 0xBA,
    0xBB, 0x6D, 0x2E, 0x41, 0x77, 0x3B, 0x76, 0x4D, 0x90, 0x2F, 0x80, 0x39, 0x75, 0x21, 0x14,
    0x47, 0x6E, 0x6F, 0x94, 0x26, 0x95, 0x6A, 0x29, 0x7E, 0xBC, 0xBD, 0xBE, 0x18, 0x9B, 0xA9,
    0x27, 0x31, 0xA3, 0xA4, 0x25, 0x08, 0xAD, 0x36, 0x40, 0x46, 0x74, 0x3A, 0x78, 0x0D, 0x88,
    0x17, 0x8B, 0x19, 0x93, 0x0E, 0x22, 0x30, 0x81, 0x4E, 0x8A, 0x06, 0x8D, 0x0C, 0x0A, 0x11,
    0x91, 0x2B, 0x2C, 0x0B, 0x37, 0x8F, 0x12, 0x01, 0x28, 0x1E, 0x02, 0x5C, 0x5D, 0x9D, 0x9E,
    0x1B, 0x98, 0x2A, 0x1A, 0x48, 0x35, 0x33, 0x1D, 0x3C, 0x85, 0x16, 0x13, 0x4C, 0x66, 0x69,
    0x68, 0x67, 0xAA, 0x62, 0x63, 0x5A, 0x5B, 0xAB, 0x84, 0x4A, 0x4B, 0x49, 0x58, 0x59, 0x42,
    0x83, 0x15,
]

# I punti potenza di base delle mosse, indicizzati per identificativo di mossa. Da
# PKHeX.Core/Moves/MoveInfo1.cs e MoveInfo2.cs, campo PP, letti il 2026-09-03. Le due tabelle
# coincidono sul prefisso comune e la seconda prosegue con le mosse introdotte allora, quindi si
# conserva quella lunga e si verifica nel self-test che il prefisso combaci.
PP_MOSSE = [
    0, 35, 25, 10, 15, 20, 20, 15, 15, 15, 35, 30, 5, 10, 30, 30, 35, 35, 20, 15,
    20, 20, 10, 20, 30, 5, 25, 15, 15, 15, 25, 20, 5, 35, 15, 20, 20, 20, 15, 30,
    35, 20, 20, 30, 25, 40, 20, 15, 20, 20, 20, 30, 25, 15, 30, 25, 5, 15, 10, 5,
    20, 20, 20, 5, 35, 20, 25, 20, 20, 20, 15, 20, 10, 10, 40, 25, 10, 35, 30, 15,
    20, 40, 10, 15, 30, 15, 20, 10, 15, 10, 5, 10, 10, 25, 10, 20, 40, 30, 30, 20,
    20, 15, 10, 40, 15, 20, 30, 20, 20, 10, 40, 40, 30, 30, 30, 20, 30, 10, 10, 20,
    5, 10, 30, 20, 20, 20, 5, 15, 10, 20, 15, 15, 35, 20, 15, 10, 20, 30, 15, 40,
    20, 15, 10, 5, 10, 30, 10, 15, 20, 15, 40, 40, 10, 5, 15, 10, 10, 10, 15, 30,
    30, 10, 10, 20, 10, 1, 1, 10, 10, 10, 5, 15, 25, 15, 10, 15, 30, 5, 40, 15,
    10, 25, 10, 30, 10, 20, 10, 10, 10, 10, 10, 20, 5, 40, 5, 5, 15, 5, 10, 5,
    15, 10, 5, 10, 20, 20, 40, 15, 10, 20, 20, 25, 5, 15, 10, 5, 20, 15, 20, 25,
    20, 5, 30, 5, 10, 20, 40, 5, 20, 40, 20, 15, 35, 10, 5, 5, 5, 15, 5, 20,
    5, 5, 15, 20, 10, 5, 5, 15, 15, 15, 15, 10,
]
PP_MOSSE_GEN1_LUNGHEZZA = 166   # la tabella di prima generazione si ferma qui

# I sei gruppi di crescita, nell'ordine in cui le tabelle dei dati li codificano. Lo stesso
# ordine della terza generazione, e la funzione dell'esperienza si importa da quel generatore
# invece di essere riscritta: due copie della medesima formula sono il difetto che questo
# progetto ha registrato tre volte.
MEDIUM_FAST, ERRATIC, FLUCTUATING, MEDIUM_SLOW, FAST, SLOW = range(6)

# Gli offset dentro i record delle tabelle delle statistiche di base, da
# PKHeX.Core/PersonalInfo/Info/PersonalInfo1.cs e PersonalInfo2.cs, letti il 2026-09-03.
PERSONALE_1 = {"dim": 0x1C, "hp": 0x01, "atk": 0x02, "def": 0x03, "spd": 0x04, "spc": 0x05,
               "tipo1": 0x06, "tipo2": 0x07, "cattura": 0x08, "crescita": 0x13}
PERSONALE_2 = {"dim": 0x20, "hp": 0x01, "atk": 0x02, "def": 0x03, "spd": 0x04, "satk": 0x05,
               "sdef": 0x06, "tipo1": 0x07, "tipo2": 0x08, "cattura": 0x09, "crescita": 0x16}

# Le lunghezze delle liste che la fonte usa come formato di file per un esemplare singolo, da
# PKHeX.Core/PKM/Util/PokeCrypto.cs e dalla struttura descritta in PokeList1.cs: un byte di
# conteggio, capienza più uno byte di marcatori di specie, la struttura di squadra, il nome
# dell'allenatore e il soprannome.
LUNGHEZZA_NOME_INT = 11
LUNGHEZZA_NOME_JP = 6

# I tipi di donatore, dai template degli incontri della fonte. Il numero è il valore nel record.
TIPO_1 = {0: "destinatario", 1: "Mew della Virtual Console", 2: "Stadium",
          3: "tour europeo", 4: "tour giapponese"}
TIPO_2 = {0: "destinatario", 1: "Stadium giapponese", 2: "Stadium inglese",
          3: "Stadium internazionale", 4: "Pokemon Center New York"}

LINGUA_1 = {0: "qualunque", 1: "giapponese", 2: "internazionale"}
LINGUA_2 = {0: "internazionale", 1: "giapponese", 2: "inglese",
            3: "internazionale non inglese"}

# L'identità dell'allenatore per ciascun tipo di donatore, dalle costanti dei template della
# fonte. Dove la fonte fissa il nome e l'identificativo, si usano quelli e sono parte
# dell'evento; dove la fonte accetta un insieme di nomi, si sceglie e la scelta si dichiara.
# Il nome scelto per i due tour è il primo dell'elenco della fonte, che è anche quello che i
# suoi commenti nominano per primo.
ALLENATORI = {
    (1, 2): {"nome": "STADIO", "tid": 2000, "nota": "nome e identificativo fissati dalla fonte "
             "per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non "
             "giapponesi"},
    (1, 3): {"nome": "YOSHIRA", "tid": 6000, "nota": "la fonte accetta diciannove nomi per il "
             "tour europeo e non fissa alcun identificativo: si sceglie il primo dell'elenco, e "
             "l'identificativo è una scelta nostra dichiarata e non un dato"},
    (1, 4): {"nome": "マクハリ", "tid": 6000, "nota": "nome dello Space World '99 di Makuhari, "
             "primo dell'elenco giapponese della fonte; l'identificativo è una scelta nostra"},
    (2, 1): {"nome": "スタジアム", "tid": 2000, "nota": "nome e identificativo fissati dalla "
             "fonte per la versione giapponese"},
    (2, 2): {"nome": "Stadium", "tid": 2000, "nota": "nome e identificativo fissati dalla fonte "
             "per la versione inglese"},
    (2, 3): {"nome": "Stadio", "tid": 2001, "nota": "nome e identificativo fissati dalla fonte "
             "per le versioni internazionali non inglesi, qui in italiano"},
    (2, 4): {"nome": "PCNYa", "tid": 1000, "nota": "la fonte accetta quattro nomi per il "
             "Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si "
             "sceglie il primo e l'identificativo è una scelta nostra dichiarata"},
}

# Il tasso di cattura degli esemplari premio di Pokemon Stadium, da EncounterGift1.IsCatchRateValid
# letto il 2026-09-03 dopo che il verificatore ha rifiutato sei voci su nove. Il byte del tasso di
# cattura di quel gruppo non porta il tasso della specie ma uno di due valori fissi, e i due valori
# sono gli identificativi di due oggetti: la Scatola Normale e la Scatola Splendida, cioè
# letteralmente la confezione in cui il premio veniva consegnato. Psyduck pretende la seconda e
# tutti gli altri accettano entrambe.
#
# Il dettaglio non è una curiosità ma la chiave del difetto: avevo scritto il tasso della specie,
# preso dalla tabella delle statistiche di base, e con quello l'incontro diventa una
# corrispondenza soltanto parziale. Su Bulbasaur non si notava, perché esiste un incontro statico
# che lo accetta ed è quello che il verificatore ha scelto, riportandolo legale ma con la
# provenienza sbagliata; sulle sei voci senza alternativa statica il verificatore non ha trovato
# alcuna corrispondenza e le ha dichiarate non valide. È il caso in cui una voce legale nasconde
# un difetto che si manifesta soltanto sulle voci vicine.
#
# Vale inoltre notare la conseguenza sul trasferimento, che è il motivo per cui questi due valori
# esistono in questa posizione: passando alla seconda generazione il byte del tasso di cattura
# diventa il byte dell'oggetto tenuto, quindi un premio di Stadium arriva in Johto tenendo in mano
# la propria scatola.
SCATOLA_NORMALE = 167
SCATOLA_SPLENDIDA = 168
PSYDUCK = 54

# I valori individuali che la fonte fissa, da EncounterGift1: i due tour hanno valori dichiarati
# e il Mew della Virtual Console li ha tutti al massimo. Dove la fonte non li fissa restano una
# scelta nostra, per la ragione spiegata nel docstring.
# L'ordine dei sei valori nella dichiarazione della fonte è punti salute, attacco, difesa,
# velocità, attacco speciale e difesa speciale, verificato su
# IndividualValueSet il 2026-09-03. La prima stesura di questo programma lo aveva letto come se
# fosse attacco, difesa, velocità e speciale, cioè aveva saltato i punti salute e slittato tutto
# di una posizione: il verificatore ha rifiutato entrambi i Mew dei tour.
#
# Il controllo che rende questa lettura certa e non probabile è interno al dato, e vale
# registrarlo perché è elegante. In prima generazione il valore dei punti salute non è
# indipendente: si ricava dai bit meno significativi degli altri quattro. La fonte lo dichiara
# comunque, quindi la lettura giusta è la sola in cui il valore derivato coincide con quello
# dichiarato. Con la lettura sbagliata i punti salute derivati valgono dieci contro i cinque
# dichiarati; con quella giusta valgono cinque. Il self-test verifica questa coincidenza.
DV_FISSI_1 = {
    3: {"atk": 10, "def": 1, "spd": 12, "spc": 5},
    4: {"atk": 10, "def": 1, "spd": 12, "spc": 5},
    1: {"atk": 15, "def": 15, "spd": 15, "spc": 15},
}
# I punti salute che la fonte dichiara per i due tour, usati dal self-test come controllo della
# lettura e non come dato da scrivere: nella struttura quel valore non esiste come campo.
DV_HP_DICHIARATO_TOUR = 5
DV_PREDEFINITI = {"atk": 15, "def": 15, "spd": 15, "spc": 15}

# L'allenatore segnaposto per le voci che lo prendono da chi riceve. È la medesima situazione
# delle sessanta voci di terza generazione: il nome e l'identificativo appartengono al
# salvataggio di destinazione, che oggi non esiste in forma leggibile, quindi si scrive un
# segnaposto dichiarato e il lotto va rifatto quando l'identificativo vero sarà noto. La
# differenza rispetto alla terza generazione, e va detta perché è a nostro favore, è che qui
# l'identificativo non entra in alcun calcolo: non esiste un valore di personalità che dipenda da
# esso, quindi cambiarlo non cambia nessun altro campo e la rigenerazione è una riscrittura di
# due campi invece di un ricalcolo.
# La lunghezza massima di un nome di allenatore nelle prime due generazioni, da
# PKM.MaxStringLengthTrainer per quei formati: sette caratteri, come in terza generazione. Il
# segnaposto della prima stesura ne aveva dieci e il verificatore ha rifiutato quindici voci con
# la formula che il nome è troppo lungo. È il difetto speculare a quello di terza generazione del
# 2026-09-02, dove il nome era troppo corto: là era vuoto e qui eccedeva, e in entrambi i casi la
# causa era che nessuno controllava la lunghezza contro il limite del formato. Ora la si controlla.
LUNGHEZZA_MASSIMA_NOME = 7

ALLENATORE_SEGNAPOSTO = {"nome": "ALLENAT", "tid": 31121,
                         "nota": "segnaposto dichiarato: questa voce prende nome e "
                                 "identificativo dal salvataggio che la riceve, e va riscritta "
                                 "con i valori veri quando quel salvataggio esisterà; sette "
                                 "caratteri perché è il massimo che il formato ammette"}


def carica_modulo(nome, percorso):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def esperienza_da_gen3():
    """La formula dell'esperienza, importata dal generatore di terza generazione.

    Non si riscrive: le sei curve sono le medesime, e una seconda copia della medesima formula e'
    esattamente il difetto che il progetto ha registrato tre volte in tre giorni. Quella copia e'
    inoltre già passata sotto il giudizio del verificatore esterno su centosettantadue
    esemplari, quindi importarla porta con sè la sua verifica.
    """
    g = carica_modulo("gen3gen", os.path.join(RADICE, "tools", "genera-evento-gen3.py"))
    return g.esperienza


def tabelle_personali(pkhex, nome, mappa):
    """Le statistiche di base per identificativo di specie, dalla tabella binaria della fonte."""
    p = os.path.join(pkhex, PERSONAL, nome)
    if not os.path.exists(p):
        sys.exit("manca la tabella " + nome + " sotto " + pkhex)
    d = io.open(p, "rb").read()
    dim = mappa["dim"]
    fuori = {}
    for i in range(len(d) // dim):
        rec = d[i * dim:(i + 1) * dim]
        voce = {}
        for chiave, off in mappa.items():
            if chiave == "dim":
                continue
            voce[chiave] = rec[off]
        fuori[i] = voce
    return fuori


def nomi_specie(pkhex):
    p = os.path.join(pkhex, NOMI_SPECIE)
    righe = io.open(p, encoding="utf-8").read().split("\n")
    return {i: righe[i] for i in range(1, min(1026, len(righe))) if righe[i]}


def nomi_mosse(pkhex):
    """I nomi delle mosse in italiano, per identificativo.

    Servono alle schede, e vengono dalla fonte invece che da me: il nome di una mossa scritto a
    memoria è un'affermazione non verificata, e su una scheda che si presenta come tecnica
    sarebbe indistinguibile da un dato letto.
    """
    p = os.path.join(pkhex, NOMI_MOSSE)
    if not os.path.exists(p):
        return {}
    righe = io.open(p, encoding="utf-8").read().split(chr(10))
    return {i: righe[i] for i in range(1, len(righe)) if righe[i] and righe[i] != "-----"}


def statistica_gen1(base, dv, livello, e_hp):
    """La statistica di un esemplare di prima generazione, con esperienza di statistica nulla.

    La formula è quella canonica delle prime due generazioni e va segnalata come non verificata
    sul disassemblato da questo progetto: è trascritta dalla sua forma corrente, e il
    verificatore esterno è lo strumento che dira' se è giusta. E' la medesima cautela con cui
    il progetto ha trattato la formula dell'esperienza, che poi il verificatore ha confermato su
    centosettantadue esemplari.

    Con esperienza di statistica nulla il termine che ne dipende si annulla, quindi la formula si
    riduce alla parte che dipende da base, valore individuale e livello.
    """
    n = (((base + dv) * 2) * livello) // 100
    return n + livello + 10 if e_hp else n + 5


def dv_hp(dvs):
    """Il valore individuale dei punti salute, derivato dagli altri quattro."""
    return (((dvs["atk"] & 1) << 3) | ((dvs["def"] & 1) << 2)
            | ((dvs["spd"] & 1) << 1) | (dvs["spc"] & 1))


def leggi_voci(pkhex):
    """Le voci delle due tabelle degli eventi, con i campi che ciascun formato porta."""
    c = os.path.join(pkhex, MGDB)
    fuori = []
    d = io.open(os.path.join(c, "event1.pkl"), "rb").read()
    for i in range(len(d) // 8):
        r = d[i * 8:(i + 1) * 8]
        fuori.append({"generazione": 1, "indice": i, "nazionale": r[0], "livello": r[1],
                      "mosse": [r[2], r[3], r[4], r[5]], "lingua": r[6], "tipo": r[7]})
    d = io.open(os.path.join(c, "event2.pkl"), "rb").read()
    for i in range(len(d) // 12):
        r = d[i * 12:(i + 1) * 12]
        fuori.append({"generazione": 2, "indice": i, "nazionale": r[0], "livello": r[1],
                      "mosse": [r[2], r[3], r[4], r[5]], "luogo": r[6],
                      "livello_attuale": r[7], "cromatico": r[8] != 0,
                      "incubazioni": 10 if r[9] == 1 else 0, "lingua": r[10], "tipo": r[11]})
    return fuori


def codice(v):
    return "EVT-%d-%04d" % (v["generazione"], v["indice"])


def dvs_per_voce(v):
    """I valori individuali di una voce, e se siano un dato della fonte o una scelta nostra."""
    if v["generazione"] == 1 and v["tipo"] in DV_FISSI_1:
        return dict(DV_FISSI_1[v["tipo"]]), "fissati dalla fonte"
    if v["generazione"] == 2 and v["cromatico"]:
        # In seconda generazione la cromaticità non è un contrassegno ma una proprietà dei
        # valori individuali, quindi una voce dichiarata cromatica li vincola. La condizione e'
        # in `pokebridge` e verificata: difesa, velocità e speciale a dieci, e attacco in un
        # insieme di otto valori. Qui si usa l'attacco massimo fra gli ammessi.
        return {"atk": 15, "def": 10, "spd": 10, "spc": 10}, \
               "vincolati dalla cromaticità dichiarata dalla fonte"
    return dict(DV_PREDEFINITI), "scelta nostra dichiarata, non un dato"


def componi(v, gen1, gen2, gb, pers1, pers2, esperienza):
    """La struttura di un esemplare, composta dai campi che la voce dichiara."""
    dvs, origine_dv = dvs_per_voce(v)
    # I due livelli della seconda generazione, e perche' usarne uno solo produceva quindici voci
    # respinte. Il record di dodici byte ne porta due: quello a un byte dall'inizio e' il livello
    # di incontro, cioe' quello che il gioco scrive nei dati di cattura, e quello a sette byte e'
    # il livello a cui l'esemplare si trova davvero. Nelle voci ordinarie coincidono, e in quelle
    # del gruppo notevole del Pokemon Center di New York no: la fonte dichiara incontro a cinque e
    # livello corrente quaranta, cinquanta o settanta.
    #
    # Fino al 2026-09-04 questo programma leggeva il campo a sette byte, lo conservava nella voce
    # e non lo usava: scriveva l'esemplare al livello di incontro. Il verificatore lo rifiutava
    # senza spiegarlo, dicendo soltanto che nessun incontro corrispondeva, perche' la sua
    # condizione e' che il livello corrente dichiarato dalla tabella non superi quello
    # dell'esemplare. E' l'ennesima occorrenza della stessa forma di difetto: due campi che
    # sembrano lo stesso campo, e la scorciatoia che ne prende uno.
    livello, livello_corrente, livello_incontro = livelli_della_voce(v)
    mosse = [m for m in v["mosse"] if m]
    pp = []
    for m in v["mosse"]:
        base = PP_MOSSE[m] if 0 < m < len(PP_MOSSE) else 0
        pp.append((base, 0))

    if v["generazione"] == 1:
        interno = NAZIONALE_A_INTERNO_1[v["nazionale"]]
        # La tabella delle statistiche di base di prima generazione è indicizzata per numero del
        # Dex e non per identificativo interno, come la fonte stessa fa quando la interroga: il
        # file ha centocinquantadue record per centocinquantuno specie più lo zero. La
        # numerazione interna serve al campo della struttura e non a questa tabella, e confondere
        # le due era il primo difetto di questo programma.
        p = pers1[v["nazionale"]]
        exp = esperienza(p["crescita"], livello)
        # Il tasso di cattura del gruppo di Stadium non è quello della specie ma la scatola in cui
        # il premio veniva consegnato: vedi il commento accanto alle due costanti.
        if v["tipo"] == 2:
            cattura = (SCATOLA_SPLENDIDA if v["nazionale"] == PSYDUCK else SCATOLA_NORMALE)
        else:
            cattura = p["cattura"]
        mon = gen1.Gen1Mon(
            species=interno,
            box_level=livello,
            type1=p["tipo1"], type2=p["tipo2"], catch_rate=cattura,
            moves=list(v["mosse"]),
            ot_id=0, exp=exp, dvs=dvs, pp=pp,
            level=livello,
        )
        hp = statistica_gen1(p["hp"], dv_hp(dvs), livello, True)
        mon.hp = hp
        mon.stats = {
            "max_hp": hp,
            "atk": statistica_gen1(p["atk"], dvs["atk"], livello, False),
            "def": statistica_gen1(p["def"], dvs["def"], livello, False),
            "spd": statistica_gen1(p["spd"], dvs["spd"], livello, False),
            "spc": statistica_gen1(p["spc"], dvs["spc"], livello, False),
        }
        return mon, dvs, origine_dv, p

    p = pers2[v["nazionale"]]
    exp = esperienza(p["crescita"], livello_corrente)
    caught = gen2.CaughtData(level=livello_incontro, time_of_day=fase_del_giorno(v),
                             ot_female=False, location=v.get("luogo", 0))
    mon = gen2.Gen2Mon(
        species=v["nazionale"],
        held_item=0,
        moves=list(v["mosse"]),
        ot_id=0, exp=exp, dvs=dvs, pp=pp,
        friendship=v["incubazioni"] if v["incubazioni"] else 70,
        pokerus=0, caught=caught,
        level=livello_corrente,
        # In seconda generazione la struttura di squadra si distingue da quella di scatola per
        # la presenza dei due byte di stato, quindi vanno scritti anche se nulli: senza di essi
        # `pokebridge` considera la struttura di scatola e rifiuta di scriverne una di squadra.
        status=0, unused=0,
    )
    # Le statistiche si calcolano al livello corrente e non a quello di incontro, per la stessa
    # ragione per cui il livello della struttura e' quello corrente: sono le statistiche che
    # l'esemplare ha, non quelle che aveva quando fu consegnato.
    hp = statistica_gen1(p["hp"], dv_hp(dvs), livello_corrente, True)
    mon.hp = hp
    mon.stats = {
        "max_hp": hp,
        "atk": statistica_gen1(p["atk"], dvs["atk"], livello_corrente, False),
        "def": statistica_gen1(p["def"], dvs["def"], livello_corrente, False),
        "spd": statistica_gen1(p["spd"], dvs["spd"], livello_corrente, False),
        "satk": statistica_gen1(p["satk"], dvs["spc"], livello_corrente, False),
        "sdef": statistica_gen1(p["sdef"], dvs["spc"], livello_corrente, False),
    }
    return mon, dvs, origine_dv, p


def livelli_della_voce(v):
    """I tre livelli di una voce: quello dichiarato, quello corrente e quello dei dati di cattura.

    Ha una funzione propria perche' i difetti che chiude erano esattamente confusioni fra questi
    numeri, e una funzione si puo' provare mentre una espressione sparsa in mezzo al codice no.

    Il primo e' il livello che la tabella dichiara. Il secondo e' il livello a cui l'esemplare si
    trova, che sta in un campo diverso e che sulle quindici voci del gruppo notevole e' quaranta,
    cinquanta o settanta invece di cinque.

    Il terzo e' il livello che va scritto nei dati di cattura, e non coincide con il primo su
    tutte le voci consegnate come uovo. La condizione del verificatore e' esplicita: per un uovo
    il livello di incontro deve essere uno, per tutto il resto deve essere quello dichiarato. La
    ragione sta nel gioco e non nella tabella, poiche' un uovo viene ricevuto a livello uno e
    schiude a cinque, e il livello di incontro registra il momento in cui e' stato ricevuto.
    Centotrentaquattro delle centocinquantasette voci di seconda generazione sono uova, quindi la
    confusione fra questi due numeri non e' un caso limite ma la maggioranza del lotto.
    """
    dichiarato = v["livello"]
    corrente = v.get("livello_attuale") or dichiarato
    incontro = 1 if v.get("incubazioni") else dichiarato
    return dichiarato, corrente, incontro


def fase_del_giorno(v):
    """La fase del giorno da scrivere nei dati di cattura, e perche' non e' sempre nulla.

    La regola del verificatore e' esplicita e va letta al contrario di come verrebbe da scriverla.
    Per un dono che uovo non e', e per un uovo ancora tale, la fase deve valere zero: non c'e'
    stato alcun momento della giornata in cui e' stato incontrato, perche' e' stato consegnato.
    Per un uovo gia' schiuso invece la fase deve valere uno, due o tre, perche' quel momento
    esiste ed e' quello della schiusa.

    Questo programma scrive esemplari schiusi e non uova, quindi le voci consegnate come uovo
    vogliono una fase vera. Si sceglie il mattino, che e' una scelta nostra dichiarata come lo
    sono i valori individuali dove la fonte non li fissa: la fonte non dice a che ora schiuse.
    """
    return 1 if v.get("incubazioni") else 0


def self_test():
    """Controlli sulle tabelle trascritte e sulle funzioni aritmetiche.

    Sono i controlli che coglierebbero una trascrizione sbagliata, che è il difetto piu'
    probabile in un programma come questo: due tabelle copiate a mano dalla fonte e una formula
    riscritta.
    """
    falliti = []

    def prova(descrizione, condizione):
        print("  %-7s %s" % ("ok" if condizione else "FALLITO", descrizione))
        if not condizione:
            falliti.append(descrizione)

    prova("la tabella delle specie copre i centocinquantuno del Dex",
          len(NAZIONALE_A_INTERNO_1) == 152)
    prova("Bulbasaur, numero uno, ha identificativo interno 153",
          NAZIONALE_A_INTERNO_1[1] == 0x99)
    prova("Mew, numero centocinquantuno, ha identificativo interno 21",
          NAZIONALE_A_INTERNO_1[151] == 0x15)
    # L'iniettività è la proprietà che impedisce di scambiare due specie, ed è lo stesso
    # controllo che il difetto di Nidoran ha insegnato a scrivere.
    interni = NAZIONALE_A_INTERNO_1[1:]
    prova("la tabella delle specie è iniettiva", len(set(interni)) == len(interni))
    prova("nessun identificativo interno è nullo", 0 not in interni)

    prova("la tabella dei punti potenza copre le mosse di seconda generazione",
          len(PP_MOSSE) == 252)
    prova("la mossa uno ha trentacinque punti potenza", PP_MOSSE[1] == 35)
    prova("la mossa centosessantacinque ne ha uno", PP_MOSSE[165] == 1)

    prova("il valore individuale dei punti salute deriva dagli altri quattro",
          dv_hp({"atk": 15, "def": 15, "spd": 15, "spc": 15}) == 15)
    prova("e vale zero quando i quattro sono pari",
          dv_hp({"atk": 10, "def": 10, "spd": 10, "spc": 10}) == 0)

    # Il controllo interno al dato che rende certa la lettura dei valori individuali dei tour:
    # i punti salute derivati dai quattro valori devono coincidere con quelli che la fonte
    # dichiara. Con la lettura sbagliata questo controllo falliva.
    prova("i punti salute derivati dei Mew dei tour coincidono con quelli dichiarati",
          dv_hp(DV_FISSI_1[3]) == DV_HP_DICHIARATO_TOUR)
    prova("le due scatole di Stadium hanno gli identificativi contigui che la fonte dichiara",
          SCATOLA_SPLENDIDA == SCATOLA_NORMALE + 1)
    prova("il massimo del nome dell'allenatore e' sette caratteri",
          LUNGHEZZA_MASSIMA_NOME == 7 and len(ALLENATORE_SEGNAPOSTO["nome"]) <= 7)

    # Un caso di controllo calcolato a mano: Mew ha base cento in tutto, e al livello cinque con
    # valore individuale quindici i punti salute valgono ((100+15)*2*5)//100 + 5 + 10 = 26.
    prova("i punti salute di un caso calcolato a mano tornano",
          statistica_gen1(100, 15, 5, True) == 26)
    prova("una statistica diversa dai punti salute usa la costante cinque",
          statistica_gen1(100, 15, 5, False) == 16)

    print("")
    # I due livelli della seconda generazione. Il difetto corretto il 2026-09-04 stava qui: il
    # campo del livello corrente veniva letto, conservato e mai usato, e le quindici voci in cui
    # differisce dal livello di incontro venivano scritte al livello sbagliato. Il verificatore le
    # respingeva senza spiegare, dicendo soltanto che nessun incontro corrispondeva.
    prova("i due livelli coincidono quando il campo corrente e' assente",
          livelli_della_voce({"livello": 5}) == (5, 5, 5))
    prova("i due livelli coincidono quando il campo corrente e' zero",
          livelli_della_voce({"livello": 5, "livello_attuale": 0}) == (5, 5, 5))
    prova("i due livelli divergono quando la fonte lo dichiara",
          livelli_della_voce({"livello": 5, "livello_attuale": 40}) == (5, 40, 5))
    prova("un uovo ha livello di incontro uno e non quello dichiarato",
          livelli_della_voce({"livello": 5, "incubazioni": 10}) == (5, 5, 1))
    prova("una voce che uovo non e' conserva il livello di incontro dichiarato",
          livelli_della_voce({"livello": 20, "incubazioni": 0}) == (20, 20, 20))
    prova("un dono che uovo non e' ha fase del giorno nulla",
          fase_del_giorno({"incubazioni": 0}) == 0)
    prova("un uovo schiuso ha una fase del giorno vera",
          fase_del_giorno({"incubazioni": 10}) in (1, 2, 3))
    print("self-test: %d controlli falliti su %d" % (len(falliti), 22))
    return 1 if falliti else 0


def provenienze():
    if not os.path.exists(PROVENIENZE):
        return {}
    return json.loads(io.open(PROVENIENZE, encoding="utf-8").read())


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pkhex", help="clone del verificatore")
    ap.add_argument("--elenca", action="store_true", help="elenca le voci con i loro campi")
    ap.add_argument("--lotto", action="store_true", help="scrive gli esemplari su disco")
    ap.add_argument("--destinazione", default=os.path.join("_notes", "lotto-gb"))
    ap.add_argument("--schede", help="scrive le schede tecniche come documento tracciato")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)

    if a.self_test:
        return self_test()
    if not a.pkhex:
        ap.error("serve --pkhex, oppure --self-test")

    from pokebridge import gen1, gen2, gb, charmap as cm
    esperienza = esperienza_da_gen3()
    pers1 = tabelle_personali(a.pkhex, "personal_rb", PERSONALE_1)
    pers2 = tabelle_personali(a.pkhex, "personal_gs", PERSONALE_2)
    nomi = nomi_specie(a.pkhex)
    mosse = nomi_mosse(a.pkhex)
    prov = provenienze()
    voci = leggi_voci(a.pkhex)

    prodotti, saltate = [], []
    for v in voci:
        try:
            mon, dvs, origine_dv, p = componi(v, gen1, gen2, gb, pers1, pers2, esperienza)
        except Exception as exc:
            saltate.append((codice(v), str(exc)))
            continue
        prodotti.append({"voce": v, "mon": mon, "dvs": dvs, "origine_dv": origine_dv,
                         "personale": p})

    print("Esemplari da evento di prima e seconda generazione")
    print("")
    print("  voci nelle tabelle della fonte      %d" % len(voci))
    print("  esemplari composti                  %d" % len(prodotti))
    print("  voci saltate                        %d" % len(saltate))
    for c, ragione in saltate[:10]:
        print("    %s: %s" % (c, ragione))
    print("")
    for generazione in (1, 2):
        gruppo = [x for x in prodotti if x["voce"]["generazione"] == generazione]
        if not gruppo:
            continue
        specie = {x["voce"]["nazionale"] for x in gruppo}
        print("  generazione %d: %d esemplari, %d specie distinte"
              % (generazione, len(gruppo), len(specie)))
        tipi = {}
        for x in gruppo:
            etichetta = (TIPO_1 if generazione == 1 else TIPO_2).get(x["voce"]["tipo"], "?")
            tipi[etichetta] = tipi.get(etichetta, 0) + 1
        for k, n in sorted(tipi.items(), key=lambda t: -t[1]):
            print("    %-30s %4d" % (k, n))
    print("")
    fissi = sum(1 for x in prodotti if x["origine_dv"] == "fissati dalla fonte")
    vincolati = sum(1 for x in prodotti if x["origine_dv"].startswith("vincolati"))
    print("  valori individuali fissati dalla fonte      %d" % fissi)
    print("  vincolati dalla cromaticità dichiarata     %d" % vincolati)
    print("  scelta nostra dichiarata                    %d"
          % (len(prodotti) - fissi - vincolati))

    if a.elenca:
        print("")
        for x in prodotti:
            v = x["voce"]
            print("  %s  %-12s liv %3d  mosse %-18s dv %s  %s"
                  % (codice(v), nomi.get(v["nazionale"], "?"), v["livello"],
                     ",".join(str(m) for m in v["mosse"] if m),
                     "".join("%X" % x["dvs"][k] for k in ("atk", "def", "spd", "spc")),
                     (TIPO_1 if v["generazione"] == 1 else TIPO_2).get(v["tipo"], "?")))

    if a.lotto:
        scritti, saltati = scrivi_lotto(prodotti, a.destinazione, nomi, cm, gb)
        print("")
        print("  scritti %d file in %s" % (scritti, a.destinazione))
        segnaposto = sum(1 for x in prodotti
                         if (x["voce"]["generazione"], x["voce"]["tipo"]) not in ALLENATORI)
        if segnaposto:
            print("  di cui %d con allenatore segnaposto, da riscrivere quando il salvataggio "
                  "di destinazione esisterà" % segnaposto)
        if saltati:
            print("  non scritti %d, con la ragione di ciascuno:" % len(saltati))
            visti = set()
            for c, ragione in saltati:
                chiave = ragione.split(":")[0]
                if chiave in visti:
                    continue
                visti.add(chiave)
                print("    %s e simili: %s" % (c, ragione))

    if a.schede:
        scrivi_schede(a.schede, prodotti, nomi, mosse, prov)
        print("")
        print("  scritto " + a.schede)
    return 0


def scrivi_lotto(prodotti, destinazione, nomi, cm, gb):
    """Scrive un file per esemplare nel formato di lista che la fonte usa per un singolo.

    La struttura è quella descritta in PokeList1: un byte di conteggio, capienza più uno byte di
    marcatori di specie, la struttura di squadra, il nome dell'allenatore e il soprannome. Le
    lunghezze dei due nomi decidono se la fonte legga il file come giapponese o internazionale,
    quindi non sono un dettaglio estetico ma parte del formato.
    """
    if not os.path.isdir(destinazione):
        os.makedirs(destinazione)
    tabella = cm.Charmap.gen12()
    scritti = 0
    saltati = []
    for x in prodotti:
        v = x["voce"]
        chiave = (v["generazione"], v["tipo"])
        allenatore = ALLENATORI.get(chiave, ALLENATORE_SEGNAPOSTO)
        nome_ot = allenatore["nome"]
        # Il presidio sulla lunghezza. Non si tronca: un nome troncato sarebbe accettato dalla
        # tabella dei caratteri e rifiutato dal verificatore, che è esattamente il difetto del
        # 2026-09-03, quindi si solleva e la voce non entra nel lotto con un nome sbagliato.
        if len(nome_ot) > LUNGHEZZA_MASSIMA_NOME:
            saltati.append((codice(v), "nome dell'allenatore %r di %d caratteri, oltre il "
                                       "massimo di %d che il formato ammette"
                            % (nome_ot, len(nome_ot), LUNGHEZZA_MASSIMA_NOME)))
            continue
        giapponese = bool(re.search(r"[^\x00-\x7F]", nome_ot))
        lung = LUNGHEZZA_NOME_JP if giapponese else LUNGHEZZA_NOME_INT
        try:
            ot_bytes = tabella.encode(nome_ot, length=lung)
        except ValueError as exc:
            # Il nome non si scrive con la tabella dei caratteri disponibile, e il caso è uno
            # solo: i nomi giapponesi. Il progetto ha la tabella giapponese di terza generazione
            # e non quella delle prime due, quindi queste voci restano fuori dal lotto e la loro
            # esclusione va dichiarata invece di ridurre il conto in silenzio.
            saltati.append((codice(v), "nome dell'allenatore %r non scrivibile con la tabella "
                                       "dei caratteri disponibile: %s" % (nome_ot, exc)))
            continue
        specie_nome = nomi.get(v["nazionale"], "?")
        # Il nome della specie arriva dalla fonte con l'apostrofo tipografico, che nessuna delle
        # due generazioni possiede nella propria tabella dei caratteri: la tabella porta
        # l'apostrofo diritto. La normalizzazione è quindi sul nome e non sulla tabella, ed è
        # legittima perché i due segni sono lo stesso carattere in due convenzioni tipografiche.
        # Senza di essa tre esemplari restavano fuori dal lotto per una ragione che sembrava un
        # limite del formato e non lo era.
        specie_nome = specie_nome.replace("’", "'")
        try:
            nick = tabella.encode(specie_nome.upper(), length=lung)
        except ValueError as exc:
            saltati.append((codice(v), "soprannome %r non scrivibile: %s"
                            % (specie_nome, exc)))
            continue

        mon = x["mon"]
        mon.ot_id = allenatore["tid"]
        struttura = mon.to_bytes(party=True)
        marcatore = (mon.species if v["generazione"] == 1 else v["nazionale"])
        buf = bytearray()
        buf.append(1)
        buf.append(marcatore)
        buf.append(0xFF)
        buf.extend(struttura)
        buf.extend(ot_bytes)
        buf.extend(nick)
        estensione = ".pk1" if v["generazione"] == 1 else ".pk2"
        nome_file = "%s-%s%s" % (codice(v),
                                 re.sub(r"[^A-Za-z0-9]", "", specie_nome), estensione)
        byte = bytes(buf)
        io.open(os.path.join(destinazione, nome_file), "wb").write(byte)
        # L'impronta si calcola qui e non altrove, cioe' sui byte che sono stati scritti davvero
        # e non su una loro ricostruzione: e' la differenza fra dichiarare che il file sia
        # riproducibile e poterlo dimostrare.
        x["impronta"] = hashlib.sha256(byte).hexdigest()
        x["nome_file"] = nome_file
        scritti += 1
    return scritti, saltati


REGISTRO_GIUDIZI = os.path.join("recreate-pokemon-distributions-events", "giudizi-esterni.json")


def giudizi_del_lotto():
    """I giudizi esterni che coprono il lotto di prima e seconda generazione.

    Restituisce una funzione che dato un codice dice se quella voce sia stata giudicata, con
    quale esito e quando. Un giudizio che dichiari di coprire tutto vale per ogni voce; uno che
    nomini un file vale per quella sola. La distinzione conta perche' una scheda che tacesse lo
    stato della verifica descriverebbe un esemplare che nessuno ha controllato senza dirlo.
    """
    percorso = os.path.join(RADICE, REGISTRO_GIUDIZI)
    if not os.path.exists(percorso):
        return lambda _codice: None
    try:
        registro = json.loads(io.open(percorso, encoding="utf-8").read())
    except Exception:
        return lambda _codice: None
    massa, singoli = [], {}
    for g in registro.get("giudizi", []):
        if "prima e seconda generazione" not in g.get("file", ""):
            continue
        if g.get("copre") == "tutti":
            massa.append(g)
        else:
            singoli[g.get("file", "")] = g

    def per_voce(codice_voce):
        g = singoli.get(codice_voce)
        if g is None and massa:
            g = massa[-1]
        if g is None:
            return None
        return {"esito": g.get("esito", "?"), "data": g.get("data", "?"),
                "come": "lettura di massa delle nove scatole in un salvataggio vuoto di seconda "
                        "generazione, dove l'assenza del contrassegno di non conformità su una "
                        "posizione equivale a un rapporto senza rilievi su quell'esemplare"
                        if g.get("copre") == "tutti" else "prova singola registrata"}
    return per_voce


def scrivi_schede(percorso, prodotti, nomi, mosse, prov):
    """Le schede tecniche, raggruppate per evento: il racconto una volta, i byte per esemplare.

    Il raggruppamento non è estetico. Centotrentasei delle centosessantotto voci vengono dal
    medesimo luogo, quindi ripetere il racconto sotto ciascuna produrrebbe un documento in cui la
    stessa pagina ricorre centotrentasei volte e in cui la parte che varia, cioè i byte, si perde
    nella parte che non varia. È la medesima ragione per cui le schede di terza generazione
    tengono la trattazione distesa nel catalogo e sulla scheda soltanto la riga di provenienza.
    """
    gruppi_prov = prov.get("gruppi", {})
    fonti = prov.get("fonti", {})
    voci_prov = prov.get("voci", {})

    r = []
    r.append("# Schede degli esemplari da evento di prima e seconda generazione")
    r.append("")
    r.append("> Documento generato da `tools/genera-evento-gb.py`. Non si modifica a mano, e non "
             "legge i file prodotti: ricalcola gli esemplari dalle tabelle della fonte con il "
             "medesimo codice che li scrive.")
    r.append("")
    r.append("Il documento porta due cose di natura diversa e le tiene separate. Il racconto di "
             "ciascun evento è letto da un file autorato e citato, e dove una fonte non esiste lo "
             "dichiara invece di riempire il campo per ipotesi; i dati tecnici di ciascun "
             "esemplare sono calcolati dalle tabelle della fonte e dalle formule, e sono "
             "verificabili uno per uno. Il racconto sta una volta per gruppo e non una volta per "
             "esemplare, perché centotrentasei delle centosessantotto voci vengono dal medesimo "
             "luogo e ripeterlo seppellirebbe la parte che varia sotto quella che non varia.")
    r.append("")
    r.append("Una avvertenza sui valori individuali, che è un risultato e non un limite dello "
             "strumento. In queste due generazioni non esiste alcun valore di personalità: i "
             "valori individuali furono estratti dal gioco al momento della consegna e non "
             "derivano da nulla che l'esemplare porti con sé. La fedeltà su quel campo non è "
             "quindi decidibile nemmeno in principio, al contrario della terza generazione dove "
             "il seme la determina. Ogni scheda dichiara se i propri valori individuali siano un "
             "dato della fonte, un vincolo della cromaticità dichiarata, oppure una scelta "
             "nostra: i primi due casi sono verificabili, il terzo no.")
    r.append("")

    # L'ordine dei gruppi segue la generazione e poi il tipo di donatore, che è l'ordine in cui
    # le tabelle della fonte li presentano.
    giudizio_per_voce = giudizi_del_lotto()
    ordinati = {}
    for x in prodotti:
        v = x["voce"]
        ordinati.setdefault((v["generazione"], v["tipo"]), []).append(x)

    for chiave in sorted(ordinati):
        generazione, tipo = chiave
        gruppo = ordinati[chiave]
        etichetta = (TIPO_1 if generazione == 1 else TIPO_2).get(tipo, "?")
        g = gruppi_prov.get("%d-%d" % (generazione, tipo))
        titolo = g.get("nome") if g else ("gruppo %s di generazione %d" % (etichetta, generazione))

        r.append("## %s" % titolo)
        r.append("")
        specie = sorted({x["voce"]["nazionale"] for x in gruppo})
        r.append("Generazione %d, donatore dichiarato dalla fonte come %s. Il gruppo porta %d "
                 "voci e %d specie distinte."
                 % (generazione, etichetta, len(gruppo), len(specie)))
        r.append("")
        if g is None:
            r.append("Provenienza storica non documentata per questo gruppo.")
            r.append("")
        else:
            r.append("Quando: %s. Dove: %s. Come: %s."
                     % (g.get("date", "non documentate"), g.get("luogo", "non documentato"),
                        g.get("come", "non documentato")))
            r.append("")
            if g.get("racconto"):
                r.append(g["racconto"])
                r.append("")
            # Il collegamento alla pagina che descrive l'evento. Sta accanto alle fonti e non
            # fra loro, perché ha una funzione diversa: le fonti sono ciò su cui il racconto
            # poggia, la pagina è dove chi legge va a leggere di più. Sono spesso lo stesso
            # indirizzo e non sempre.
            if g.get("pagina"):
                r.append("Pagina che descrive l'evento: <%s>." % g["pagina"])
                r.append("")
            citate = []
            for chiave_fonte in ("fonte", "fonte_secondaria"):
                nome_fonte = g.get(chiave_fonte)
                if nome_fonte and nome_fonte in fonti:
                    f = fonti[nome_fonte]
                    citate.append("[%s](%s), letta il %s" % (f["titolo"], f["url"], f["letta"]))
            if citate:
                r.append("Fonti: " + "; ".join(citate) + ".")
            else:
                r.append("Fonti: nessuna letta per questo gruppo, quindi quanto sopra è "
                         "dichiarato e non verificato.")
            r.append("")
            # Le divergenze fra le fonti non si mediano e non si tacciono: si dichiarano, con la
            # ragione per cui si è seguita l'una e non l'altra. Una divergenza taciuta diventa
            # un difetto quando la fonte che non abbiamo seguito ha ragione.
            if g.get("divergenze"):
                r.append("Divergenza fra le fonti: " + g["divergenze"])
                r.append("")

        for x in gruppo:
            v = x["voce"]
            mon = x["mon"]
            p = x["personale"]
            nome = nomi.get(v["nazionale"], "?")
            giudizio = giudizio_per_voce(codice(v))
            r.append("### %s %s" % (codice(v), nome))
            r.append("")
            # L'attribuzione della singola voce, dove il gruppo non basta. Serve al solo gruppo
            # delle uova, dove un medesimo tipo di donatore raccoglie tre campagne distinte e il
            # marcatore che le separa è una mossa.
            vp = voci_prov.get(codice(v))
            if vp:
                r.append("Attribuzione di questa voce: %s. Il marcatore che la distingue è %s."
                         % (vp.get("campagna", "non determinata"),
                            vp.get("marcatore", "non dichiarato")))
                r.append("")
            r.append("| Campo | Valore | Provenienza |")
            r.append("|---|---|---|")
            r.append("| numero del Dex | %d | tabella degli eventi |" % v["nazionale"])
            if generazione == 1:
                r.append("| identificativo interno | %d | corrispondenza fra numerazione del "
                         "Dex e numerazione interna di prima generazione |" % mon.species)
            dichiarato, corrente, incontro = livelli_della_voce(v)
            r.append("| livello dichiarato | %d | tabella degli eventi, campo a un byte "
                     "dall'inizio del record |" % dichiarato)
            if incontro != dichiarato:
                r.append("| livello nei dati di cattura | %d | non è quello dichiarato, perché "
                         "questa voce è consegnata come uovo: un uovo si riceve a livello uno e "
                         "schiude a cinque, e i dati di cattura registrano il momento in cui è "
                         "stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte "
                         "e centotrentaquattro le uova del lotto |" % incontro)
            else:
                r.append("| livello nei dati di cattura | %d | coincide con quello dichiarato, "
                         "perché questa voce non è un uovo |" % incontro)
            if corrente != dichiarato:
                r.append("| livello corrente | %d | tabella degli eventi, campo a sette byte "
                         "dall'inizio del record: è il livello a cui l'esemplare si trova, "
                         "mentre quello di incontro resta nei dati di cattura. I due divergono "
                         "sulle quindici voci del gruppo notevole, e usare il solo livello di "
                         "incontro le faceva respingere tutte |" % corrente)
            else:
                r.append("| livello corrente | %d | coincide con quello dichiarato, come nella "
                         "grande maggioranza delle voci |" % corrente)
            r.append("| mosse | %s | tabella degli eventi, con i nomi dalla tabella dei nomi |"
                     % ", ".join("%s (%d)" % (mosse.get(m, "?"), m) for m in v["mosse"] if m))
            r.append("| punti potenza | %s | tabella dei punti potenza di base |"
                     % ", ".join(str(pp[0]) for pp in mon.pp if pp[0]))
            r.append("| esperienza | %d | formula del gruppo di crescita %d, importata dal "
                     "generatore di terza generazione |" % (mon.exp, p["crescita"]))
            r.append("| valori individuali | attacco %d, difesa %d, velocità %d, speciale %d, "
                     "punti salute %d | %s |"
                     % (x["dvs"]["atk"], x["dvs"]["def"], x["dvs"]["spd"], x["dvs"]["spc"],
                        dv_hp(x["dvs"]), x["origine_dv"]))
            if generazione == 1:
                r.append("| tipi | %d e %d | tabella delle statistiche di base |"
                         % (p["tipo1"], p["tipo2"]))
                r.append("| tasso di cattura | %d | tabella delle statistiche di base |"
                         % p["cattura"])
            else:
                r.append("| cromatico | %s | tabella degli eventi |"
                         % ("sì" if v["cromatico"] else "no"))
                r.append("| uovo | %s | tabella degli eventi, dove le incubazioni diverse da "
                         "zero lo dichiarano |"
                         % ("sì, %d incubazioni" % v["incubazioni"] if v["incubazioni"] else "no"))
                r.append("| luogo di cattura | %d | tabella degli eventi |" % v.get("luogo", 0))
            r.append("| statistiche | %s | formula delle prime due generazioni, con esperienza "
                     "di statistica nulla |"
                     % ", ".join("%s %d" % (k, val) for k, val in mon.stats.items()))
            allenatore = ALLENATORI.get(chiave)
            if allenatore:
                r.append("| allenatore | %s, identificativo %d | %s |"
                         % (allenatore["nome"], allenatore["tid"], allenatore["nota"]))
            r.append("| restrizione di lingua | %s | tabella degli eventi |"
                     % (LINGUA_1 if generazione == 1 else LINGUA_2).get(v["lingua"], "?"))
            # Le tre righe che chiudono il pedigree, e che non descrivono l'esemplare ma la sua
            # tracciabilita'. La prima lega la voce al gruppo, cosicche' chi legge una scheda
            # sappia dove sta il racconto dell'evento senza cercarlo. La seconda e' l'impronta
            # del file prodotto, che rende la ricreazione dimostrabile e non soltanto dichiarata:
            # chi rigenera il lotto e ottiene la medesima impronta ha una prova, non una
            # impressione. La terza dice se il verificatore esterno abbia giudicato quella voce e
            # quando, perche' una scheda senza quel dato descrive un esemplare che nessuno ha
            # ancora controllato e non lo dichiara.
            r.append("| gruppo di appartenenza | %s | il racconto dell'evento, le date, il luogo "
                     "e le fonti stanno nella sezione di gruppo di questo documento |"
                     % titolo)
            impronta = x.get("impronta")
            if impronta:
                r.append("| impronta del file prodotto | `%s` | SHA-256 dei byte scritti in "
                         "`_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto "
                         "dalle medesime tabelle deve riprodurla identica, e una differenza "
                         "segnala che qualcosa è cambiato nelle tabelle o nel programma |"
                         % impronta)
            else:
                r.append("| impronta del file prodotto | non calcolata | l'impronta si calcola "
                         "sui byte scritti, quindi esiste soltanto quando le schede si "
                         "generano insieme al lotto: se manca su tutte le voci la corsa è "
                         "stata di sole schede, se manca su alcune quelle voci non sono state "
                         "scritte e il motivo è dichiarato nell'elenco delle non scritte |")
            if giudizio:
                r.append("| giudizio del verificatore | %s, %s | %s |"
                         % (giudizio["esito"], giudizio["data"], giudizio["come"]))
            else:
                r.append("| giudizio del verificatore | non ancora giudicata | nessuna prova "
                         "esterna registrata copre questa voce, quindi la sua conformità non è "
                         "stabilita: le prove interne dicono che i campi sono scritti dove la "
                         "struttura li vuole, non che i valori siano quelli giusti |")
            r.append("")

    io.open(percorso, "w", encoding="utf-8", newline="").write("\n".join(r) + "\n")

if __name__ == "__main__":
    sys.exit(main())
