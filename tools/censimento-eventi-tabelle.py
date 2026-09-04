#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Censisce gli esemplari da evento che NON stanno nella base dei doni segreti.

Perche' questo programma esiste
-------------------------------
L'asse degli eventi della lista di spunta nasce da due sole fonti, cioe' la tabella delle carte
meraviglia di terza generazione e i file binari della base dei doni segreti. Sono le due fonti
giuste per le distribuzioni fatte come dono, e sono cieche su tutto il resto: e' un difetto di
copertura e non di lettura, quindi non produce alcun errore e non si manifesta mai da se'.

Il resto e' piu' grande di quanto sembri, e si divide in classi che non vanno confuse perche'
hanno natura diversa. Ci sono le distribuzioni in cui il dono era un oggetto e l'esemplare e' un
incontro dentro il gioco, come i quattro biglietti di terza generazione, la Tessera Membro e la
Lettera di Oak in quarta e il Passo Liberta' in quinta: sono distribuzioni a tutti gli effetti, e
la sola ragione per cui sfuggono e' che il verificatore le tiene fra gli incontri statici invece
che fra i doni. Ci sono le periferiche, cioe' il Pokewalker, il Dream Radar e il Ranch, dove
l'esemplare arriva da un apparecchio e non da una carta. Ci sono i giochi da console fissa, cioe'
Colosseum e XD, dove gli esemplari non sono distribuzioni ma sono irripetibili altrove. E ci sono
i doni interni condizionati dell'ottava generazione, che pretendono il salvataggio di un altro
gioco.

Il programma legge tutte queste classi dalle tabelle del verificatore e le tiene separate
nell'uscita, perche' mescolarle darebbe un totale grande e inutilizzabile: la decisione su quali
classi entrino nell'obiettivo di collezione appartiene a chi colleziona, e un censimento che
avesse gia' deciso al posto suo gliela toglierebbe.

Che cosa questo programma non fa
--------------------------------
Non produce alcun esemplare e non giudica alcuna legittimita'. Enumera, e per ogni voce dice da
quale tabella viene, cosicche' chi voglia verificarla sappia dove guardare. Le classi di cui non
sappiamo leggere il formato sono dichiarate non lette e non contate a zero.

Uso
---
    python tools/censimento-eventi-tabelle.py --pkhex _notes/fonti/pkhex
    python tools/censimento-eventi-tabelle.py --pkhex <clone> --markdown <file.md>
    python tools/censimento-eventi-tabelle.py --self-test
"""

import argparse
import io
import os
import re
import struct
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATI = os.path.join("PKHeX.Core", "Legality", "Encounters", "Data")
WILD = os.path.join("PKHeX.Core", "Resources", "legality", "wild")


# --------------------------------------------------------------------------------------------
# Le distribuzioni in cui il dono era un oggetto
#
# Queste voci si scrivono a mano e non si estraggono con una regola, ed e' una scelta e non una
# pigrizia. Nelle tabelle del verificatore stanno in mezzo agli incontri ordinari e nulla nel
# testo dichiara quale distribuzione le abbia sbloccate: il contrassegno di incontro fatidico c'e'
# su alcune e manca su altre, per ragioni storiche del gioco e non della distribuzione. Dedurle
# darebbe un elenco che sembra completo e non lo e'. Ciascuna riga porta quindi la sua fonte,
# cioe' il file della tabella da cui e' stata letta il 2026-09-04, e chi la rivede la ritrova.
#
# (gen, oggetto distribuito, luogo, specie, forma, livello, giochi, fatidico, riferimento)
OGGETTO_DISTRIBUITO = (
    (3, "Biglietto Eone", "Isola del Sud", 380, 0, 50, "Rubino", False,
     "Encounters3RSE.cs StaticR"),
    (3, "Biglietto Eone", "Isola del Sud", 381, 0, 50, "Zaffiro", False,
     "Encounters3RSE.cs StaticS"),
    (3, "Biglietto Eone", "Isola del Sud", 380, 0, 50, "Smeraldo", True,
     "Encounters3RSE.cs StaticE"),
    (3, "Biglietto Eone", "Isola del Sud", 381, 0, 50, "Smeraldo", True,
     "Encounters3RSE.cs StaticE"),
    (3, "Carta Mare Antica", "Isola Lontana", 151, 0, 30, "Smeraldo", True,
     "Encounters3RSE.cs StaticE, la fonte annota che fuori dal Giappone non fu distribuita"),
    (3, "Biglietto Mistico", "Rocca Ombelico", 249, 0, 70, "Smeraldo", True,
     "Encounters3RSE.cs StaticE"),
    (3, "Biglietto Mistico", "Rocca Ombelico", 250, 0, 70, "Smeraldo", True,
     "Encounters3RSE.cs StaticE"),
    (3, "Biglietto Aurora", "Isola Nascita", 386, 3, 30, "Smeraldo", True,
     "Encounters3RSE.cs StaticE, forma Velocita'"),
    (3, "Biglietto Mistico", "Rocca Ombelico", 249, 0, 70, "Rosso Fuoco e Verde Foglia", True,
     "Encounters3FRLG.cs"),
    (3, "Biglietto Mistico", "Rocca Ombelico", 250, 0, 70, "Rosso Fuoco e Verde Foglia", True,
     "Encounters3FRLG.cs"),
    (3, "Biglietto Aurora", "Isola Nascita", 386, 1, 30, "Rosso Fuoco", True,
     "Encounters3FRLG.cs StaticFR, forma Attacco"),
    (3, "Biglietto Aurora", "Isola Nascita", 386, 2, 30, "Verde Foglia", True,
     "Encounters3FRLG.cs StaticLG, forma Difesa"),
    (4, "Tessera Membro", "Isola Lunanova", 491, 0, 50, "Platino", False,
     "Encounters4DPPt.cs, in Diamante e Perla la voce e' commentata come non distribuita"),
    (4, "Lettera di Oak", "Giardino Floreale", 492, 0, 30, "Platino", True,
     "Encounters4DPPt.cs, in Diamante e Perla la voce e' commentata come non distribuita"),
    (5, "Passo Liberta'", "Giardino Liberta'", 494, 0, 15, "Nero e Bianco", False,
     "Encounters5BW.cs, la fonte dichiara che non puo' essere cromatico"),
)

# Le voci che una fonte dichiara mai distribuite. Vanno scritte perche' la loro assenza dal
# censimento e' un risultato e non una lacuna: chi cercasse l'Arceus del Flauto Azzurro senza
# questa riga concluderebbe che il censimento sia incompleto, e cercherebbe per giorni una
# distribuzione che non e' mai avvenuta.
MAI_DISTRIBUITE = (
    (4, "Flauto Azzurro", "Colonna Lancia", 493,
     "il verificatore non porta alcuna voce per questo incontro, cioe' non fu mai distribuito "
     "per via ufficiale in alcuna regione"),
    (4, "Lettera di Oak", "Giardino Floreale", 492,
     "in Diamante e Perla la voce esiste nella fonte ma e' commentata come non distribuita: "
     "la ebbe soltanto Platino"),
)

# Le tabelle binarie, lette il 2026-09-04. Erano dichiarate non lette fino a quel giorno, ed e'
# il motivo per cui la sezione delle lacune di questo documento e' ora vuota: la dichiarazione di
# non lettura era onesta, ma era un debito e non una conclusione.
#
# Il passo di ciascun formato non si indovina e non si deduce dalla dimensione del file: si legge
# dalla classe che lo interpreta, e il programma verifica poi che la dimensione sia un multiplo
# esatto del passo. Un resto diverso da zero significa che il passo e' sbagliato, e proseguire
# darebbe specie plausibili e false, che e' il modo in cui questo progetto ha gia' perso una
# giornata sulla quinta generazione.
#
# (classe, gen, etichetta, file relativo a legality/wild, passo, off specie, off forma,
#  off livello, sotto scadenza)
BINARI = (
    ("incursione", 8, "Spada, incursioni da distribuzione", "Gen8/encounter_sw_dist.pkl",
     0x10, 0x00, 0x02, 0x0C, False),
    ("incursione", 8, "Scudo, incursioni da distribuzione", "Gen8/encounter_sh_dist.pkl",
     0x10, 0x00, 0x02, 0x0C, False),
    ("incursione", 8, "Spada e Scudo, avventure Dynamax nei sotterranei",
     "Gen8/encounter_swsh_underground.pkl", 14, 0x00, 0x02, 0x03, False),
    ("incursione", 9, "Scarlatto e Violetto, incursioni da distribuzione",
     "Gen9/encounter_dist_paldea.pkl", 62, 0x00, 0x02, 0x07, False),
    ("incursione", 9, "Scarlatto e Violetto, esemplari di potere",
     "Gen9/encounter_might_paldea.pkl", 62, 0x00, 0x02, 0x07, False),
)

# I trasferimenti da Pokemon GO. Stanno in una classe propria e non fra le incursioni, e la
# ragione e' di sostanza e non di ordinamento: non sono una distribuzione ma una porta di
# ingresso permanente, che non chiude il 26 febbraio 2027 e non chiude affatto. Il censimento li
# conta perche' l'obiettivo dichiarato e' la collezione completa, e li tiene separati perche'
# chiamarli eventi sarebbe falso.
#
# Il formato e' un archivio indicizzato: due byte di identificativo, il numero delle aree a
# sedici bit, e poi una tabella di posizioni dove l'inizio dell'area i-esima e la fine coincidono
# con l'inizio della successiva. Ogni area vale una coppia di specie e forma, e porta N finestre
# temporali da dieci byte. La voce da contare e' l'area e non la finestra: una finestra e' un
# periodo in cui quella specie era ottenibile, non un collezionabile in piu'.
GO = (
    ("porta-permanente", 8, "Pokemon GO verso il deposito", "encounter_go_home.pkl", False),
    ("porta-permanente", 7, "Pokemon GO verso Let's Go", "encounter_go_lgpe.pkl", False),
)

NON_LETTE = ()

# --------------------------------------------------------------------------------------------
# Le tabelle che si estraggono per intero, dichiarate una per una.
#
# Il modo di leggere la specie e' 'campo' quando la riga porta `Species = N`, 'primo' quando il
# numero e' il primo argomento del costruttore, 'secondo' quando e' il secondo, e 'fatidico'
# quando si prendono le sole righe con il contrassegno di incontro fatidico. Sbagliare il modo non
# produce un errore ma numeri plausibili, ed e' il motivo per cui e' dichiarato per tabella invece
# di essere indovinato dal programma.
#
# (classe, gen, etichetta, file relativo, array, modo, sotto scadenza)
TABELLE = (
    ("disco-bonus", 3, "Colosseum, disco bonus, solo Giappone", "Gen3/Encounters3RSE.cs",
     "ColoGiftsR", "primo", True),
    ("spinoff", 3, "Colosseum, premio del Monte Lotta", "Gen3/Encounters3RSE.cs", "ColoGiftsS",
     "primo", True),
    ("spinoff", 3, "Colosseum, iniziali", "Gen3/Encounters3Colo.cs", "Starters", "primo", True),
    ("spinoff", 3, "Colosseum, doni", "Gen3/Encounters3Colo.cs", "Gifts", "primo", True),
    ("spinoff", 3, "Colosseum, ombra", "Gen3/Encounters3Colo.cs", "Shadow", "campo", True),
    ("spinoff", 3, "XD, doni", "Gen3/Encounters3XD.cs", "Gifts", "primo", True),
    ("spinoff", 3, "XD, scambi", "Gen3/Encounters3XD.cs", "Trades", "primo", True),
    ("spinoff", 3, "XD, ombra", "Gen3/Encounters3XD.cs", "Shadow", "campo", True),
    ("periferica", 4, "My Pokemon Ranch", "Gen4/Encounters4DPPt.cs", "RanchGifts", "secondo",
     True),
    ("periferica", 5, "Dream Radar", "Gen5/Encounters5DR.cs", "Encounter_DreamRadar", "primo",
     True),
    ("incursione", 8, "Spada e Scudo, incursioni delle grotte di cristallo",
     "Gen8/Encounters8Nest.cs", "Crystal_SWSH", "campo", False),
    ("condizionato", 8, "Leggende Arceus, doni fatidici", "Gen8/Encounters8a.cs", None,
     "fatidico", False),
    ("condizionato", 8, "Diamante Lucente e Perla Splendente, doni fatidici",
     "Gen8/Encounters8b.cs", None, "fatidico", False),
    ("condizionato", 8, "Spada e Scudo, doni fatidici", "Gen8/Encounters8.cs", None, "fatidico",
     False),
)

# Nota sul disco bonus di Colosseum, che vale registrare perche' e' un difetto commesso e
# corretto nella medesima ora. Queste voci erano state scritte a mano in una costante, con una
# sola riga per il Celebi di Ageto, perche' era la sola che una ricerca sul nome avesse trovato.
# Leggendo l'array invece di trascriverlo sono comparse le altre due: accanto al Celebi il disco
# consegnava anche un Pikachu, e la tabella gemella porta l'Ho-Oh premio del Monte Lotta, che non
# viene dal disco ed e' un'altra cosa. Un elenco scritto a mano da chi cerca un nome trova quel
# nome e si ferma; per questo tutte e tre stanno ora nell'elenco delle tabelle lette.

# I corsi del Pokewalker. I primi ventidue arrivavano con l'apparecchio, gli ultimi cinque erano
# distribuiti: la distinzione conta, perche' i secondi sono eventi e i primi no.
CORSI_POKEWALKER = (
    "Prato Ristoro", "Bosco Rumoroso", "Strada Sconnessa", "Bella Spiaggia", "Zona Suburbana",
    "Grotta Buia", "Lago Blu", "Periferia", "Prato di Hoenn", "Spiaggia Calda", "Via del Vulcano",
    "Casa sull Albero", "Grotta Spaventosa", "Prato di Sinnoh", "Strada Ghiacciata",
    "Grande Foresta", "Lago Bianco", "Spiaggia Tempestosa", "Villaggio Turistico",
    "Grotta Silente", "Oltre il Mare", "Confine del Cielo",
    "Foresta Gialla", "Raduno", "Gita", "Via del Vincitore", "Prato Amicizia",
)
CORSI_DISTRIBUITI = 22  # dal ventiduesimo indice in avanti i corsi furono distribuiti


def blocco_array(testo, nome):
    """Il corpo di un array C# dichiarato nella forma che le tabelle del verificatore usano."""
    schema = r"\[\]\s+" + re.escape(nome) + r"\s*=\s*\[(.*?)\n    \];"
    trovato = re.search(schema, testo, re.S)
    return trovato.group(1) if trovato else None


def voci_array(testo, nome, modo):
    """Le voci di un array, con la specie e il commento di riga che la fonte porta accanto.

    Il commento non e' decorazione: nelle tabelle del verificatore e' l'unico posto dove sia
    scritto quale distribuzione o quale incontro una riga rappresenti, e senza di esso il
    censimento sarebbe un elenco di numeri.
    """
    corpo = blocco_array(testo, nome)
    if corpo is None:
        return None
    fuori = []
    for riga in corpo.splitlines():
        if "new(" not in riga or riga.lstrip().startswith("//"):
            continue
        commento = ""
        taglio = riga.find("//")
        if taglio >= 0:
            commento = riga[taglio + 2:].strip()
            riga = riga[:taglio]
        specie = None
        if modo == "campo":
            m = re.search(r"Species\s*=\s*(\d+)", riga)
            specie = int(m.group(1)) if m else None
        else:
            m = re.search(r"new\(\s*(\d+)\s*,\s*(\d+)", riga)
            if m:
                specie = int(m.group(1) if modo == "primo" else m.group(2))
        if specie is None:
            continue
        forma = 0
        mf = re.search(r"Form\s*=\s*(\d+)", riga)
        if mf:
            forma = int(mf.group(1))
        fuori.append({"specie": specie, "forma": forma, "commento": commento})
    return fuori


def voci_fatidiche(testo):
    """Le righe di una tabella che portano il contrassegno di incontro fatidico.

    In ottava generazione il contrassegno non nomina una distribuzione ma un dono interno che
    pretende una condizione esterna, tipicamente il salvataggio di un altro gioco sulla medesima
    console. Sono esemplari irripetibili e vanno censiti, ma non sono distribuzioni e per questo
    stanno in una classe propria.
    """
    fuori = []
    for riga in testo.splitlines():
        if "FatefulEncounter = true" not in riga or riga.lstrip().startswith("//"):
            continue
        commento = ""
        taglio = riga.find("//")
        if taglio >= 0:
            commento = riga[taglio + 2:].strip()
            riga = riga[:taglio]
        m = re.search(r"Species\s*=\s*(\d+)", riga)
        if m:
            specie = int(m.group(1))
        else:
            m = re.search(r"new\(\s*(\d+)\s*,", riga)
            if not m:
                continue
            specie = int(m.group(1))
        mf = re.search(r"Form\s*=\s*(\d+)", riga)
        fuori.append({"specie": specie, "forma": int(mf.group(1)) if mf else 0,
                      "commento": commento})
    return fuori


def pokewalker(pkhex):
    """Gli incontri del Pokewalker, letti dal file binario del verificatore.

    Il formato e' dichiarato in EncounterStatic4Pokewalker: ventisette corsi da sei posizioni,
    dodici byte per posizione, con la specie nei primi due byte e il livello nel terzo. La prova
    che il formato sia quello giusto e' che il file misuri esattamente millenovecentoquarantaquattro
    byte, cioe' ventisette per sei per dodici, e il programma la fa invece di fidarsi: una
    dimensione diversa significa che il formato e' cambiato, e proseguire produrrebbe specie
    plausibili e sbagliate.
    """
    percorso = os.path.join(pkhex, WILD, "Gen4", "encounter_walker4.pkl")
    if not os.path.exists(percorso):
        return None, "il file non e' nel clone: aggiungere PKHeX.Core/Resources/legality/wild"
    dati = io.open(percorso, "rb").read()
    atteso = len(CORSI_POKEWALKER) * 6 * 0xC
    if len(dati) != atteso:
        return None, ("la dimensione %d non e' quella attesa %d: il formato che stiamo usando "
                      "e' sbagliato" % (len(dati), atteso))
    fuori = []
    for indice in range(len(CORSI_POKEWALKER) * 6):
        off = indice * 0xC
        specie = struct.unpack_from("<H", dati, off)[0]
        if specie == 0:
            continue
        corso = indice // 6
        fuori.append({"specie": specie, "forma": 0, "livello": dati[off + 2],
                      "corso": CORSI_POKEWALKER[corso],
                      "distribuito": corso >= CORSI_DISTRIBUITI})
    return fuori, None


def leggi_binario(pkhex, relativo, passo, off_specie, off_forma, off_livello):
    """Le voci di una tabella binaria a record di lunghezza fissa.

    Restituisce la lista delle voci e, in caso di rifiuto, il motivo. Il rifiuto e' deliberato e
    non un ripiego: se la dimensione non e' un multiplo del passo, il passo che stiamo usando non
    e' quello del formato, e leggere comunque produrrebbe un elenco di specie esistenti e
    sbagliate invece di un errore.
    """
    percorso = os.path.join(pkhex, WILD, relativo.replace("/", os.sep))
    if not os.path.exists(percorso):
        return None, "il file non e' nel clone: " + percorso
    dati = io.open(percorso, "rb").read()
    quante, resto = divmod(len(dati), passo)
    if resto:
        return None, ("la dimensione %d non e' multipla del passo %d, resto %d: il passo che "
                      "stiamo usando e' sbagliato" % (len(dati), passo, resto))
    fuori = []
    for indice in range(quante):
        off = indice * passo
        specie = struct.unpack_from("<H", dati, off + off_specie)[0]
        if specie == 0:
            continue
        if not 1 <= specie <= 1025:
            return None, ("la voce %d porta la specie %d, fuori dall'intervallo noto: il "
                          "formato non e' quello che stiamo usando" % (indice, specie))
        fuori.append({"specie": specie, "forma": dati[off + off_forma],
                      "livello": dati[off + off_livello]})
    return fuori, None


def leggi_go(pkhex, nome):
    """Le aree di un archivio di Pokemon GO, una per coppia di specie e forma.

    L'archivio comincia con due byte di identificativo e il numero delle aree a sedici bit, e
    prosegue con una tabella di posizioni in cui la fine di un'area coincide con l'inizio della
    successiva: la posizione dell'area i-esima si legge come intero a sessantaquattro bit alla
    quarta posizione piu' quattro volte l'indice, di cui la meta' bassa e' l'inizio e quella alta
    la fine. Ogni area porta specie, forma e formato di importazione nei primi quattro byte, e poi
    finestre temporali da dieci byte.

    Si contano le aree e non le finestre, e la distinzione e' di sostanza: una finestra e' un
    periodo in cui quella specie era ottenibile, non un collezionabile in piu'.
    """
    percorso = os.path.join(pkhex, WILD, nome)
    if not os.path.exists(percorso):
        return None, "il file non e' nel clone: " + percorso
    dati = io.open(percorso, "rb").read()
    if dati[:2] != b"go":
        return None, ("l'identificativo dell'archivio e' %r invece di 'go': il formato non e' "
                      "quello che stiamo usando" % dati[:2])
    quante = struct.unpack_from("<H", dati, 2)[0]
    fuori = []
    for indice in range(quante):
        inizio_fine = struct.unpack_from("<Q", dati, 4 + indice * 4)[0]
        inizio = inizio_fine & 0xFFFFFFFF
        fine = inizio_fine >> 32
        area = dati[inizio:fine]
        if len(area) < 4:
            continue
        specie = struct.unpack_from("<H", area, 0)[0]
        if not 1 <= specie <= 1025:
            return None, ("l'area %d porta la specie %d, fuori dall'intervallo noto"
                          % (indice, specie))
        finestre = (len(area) - 4) // 10
        fuori.append({"specie": specie, "forma": area[2], "finestre": finestre})
    return fuori, None


def censisci(pkhex):
    gruppi, difetti = [], []

    gruppi.append({
        "classe": "oggetto-distribuito", "gen": None,
        "etichetta": "Distribuzioni in cui il dono era un oggetto",
        "voci": [{"specie": s, "forma": f,
                  "commento": "%s, %s, %s, livello %d" % (oggetto, luogo, giochi, liv),
                  "gen": g, "riferimento": rif}
                 for (g, oggetto, luogo, s, f, liv, giochi, _fat, rif) in OGGETTO_DISTRIBUITO],
        "sotto_scadenza": True, "letto": True})

    for classe, gen, etichetta, relativo, array, modo, scad in TABELLE:
        percorso = os.path.join(pkhex, DATI, relativo.replace("/", os.sep))
        if not os.path.exists(percorso):
            difetti.append((etichetta, "file assente: " + percorso))
            gruppi.append({"classe": classe, "gen": gen, "etichetta": etichetta, "voci": [],
                           "sotto_scadenza": scad, "letto": False})
            continue
        testo = io.open(percorso, encoding="utf-8").read()
        voci = voci_fatidiche(testo) if modo == "fatidico" else voci_array(testo, array, modo)
        if voci is None:
            difetti.append((etichetta, "l'array %s non e' nel file" % array))
            gruppi.append({"classe": classe, "gen": gen, "etichetta": etichetta, "voci": [],
                           "sotto_scadenza": scad, "letto": False})
            continue
        for v in voci:
            v["gen"] = gen
            v["riferimento"] = relativo + (" " + array if array else " incontri fatidici")
        gruppi.append({"classe": classe, "gen": gen, "etichetta": etichetta, "voci": voci,
                       "sotto_scadenza": scad, "letto": True})

    voci, errore = pokewalker(pkhex)
    if errore:
        difetti.append(("Pokewalker", errore))
        gruppi.append({"classe": "periferica", "gen": 4, "etichetta": "Pokewalker", "voci": [],
                       "sotto_scadenza": True, "letto": False})
    else:
        for v in voci:
            v["gen"] = 4
            v["riferimento"] = "encounter_walker4.pkl, corso " + v["corso"]
            v["commento"] = ("corso %s, livello %d, %s"
                             % (v["corso"], v["livello"],
                                "corso distribuito" if v["distribuito"] else "corso in dotazione"))
        gruppi.append({"classe": "periferica", "gen": 4, "etichetta": "Pokewalker",
                       "voci": voci, "sotto_scadenza": True, "letto": True})

    for classe, gen, etichetta, relativo, passo, o_s, o_f, o_l, scad in BINARI:
        voci, errore = leggi_binario(pkhex, relativo, passo, o_s, o_f, o_l)
        if errore:
            difetti.append((etichetta, errore))
            gruppi.append({"classe": classe, "gen": gen, "etichetta": etichetta, "voci": [],
                           "sotto_scadenza": scad, "letto": False})
            continue
        for v in voci:
            v["gen"] = gen
            v["riferimento"] = relativo
            v["commento"] = "livello %d" % v["livello"]
        gruppi.append({"classe": classe, "gen": gen, "etichetta": etichetta, "voci": voci,
                       "sotto_scadenza": scad, "letto": True})

    for classe, gen, etichetta, nome, scad in GO:
        voci, errore = leggi_go(pkhex, nome)
        if errore:
            difetti.append((etichetta, errore))
            gruppi.append({"classe": classe, "gen": gen, "etichetta": etichetta, "voci": [],
                           "sotto_scadenza": scad, "letto": False})
            continue
        for v in voci:
            v["gen"] = gen
            v["riferimento"] = nome
            v["commento"] = ("%d finestre temporali" % v["finestre"]) if v["finestre"] else "-"
        gruppi.append({"classe": classe, "gen": gen, "etichetta": etichetta, "voci": voci,
                       "sotto_scadenza": scad, "letto": True})
    return gruppi, difetti


def self_test():
    """Controlla le funzioni di lettura su testo di prova, senza toccare il clone."""
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    finto = """
    internal static readonly EncounterX[] Tavola =
    [
        new(025, 05) { Location = 1 }, // Pikachu di prova
        // new(026, 05) { Location = 2 }, // riga commentata, non deve entrare
        new(01, 3000, Prima) { Species = 296, Level = 30, Form = 2 }, // Makuhita ombra
    ];
"""
    voci = voci_array(finto, "Tavola", "primo")
    prova("array, modo primo, quante", 2, len(voci))
    prova("array, modo primo, specie", 25, voci[0]["specie"])
    prova("array, modo primo, commento", "Pikachu di prova", voci[0]["commento"])
    # Nel modo primo la riga con Species esplicito porta il proprio primo argomento, che e'
    # l'indice dell'ombra e non una specie: e' esattamente il motivo per cui il modo si dichiara
    # per tabella e non si indovina.
    prova("array, modo primo su riga a indice", 1, voci[1]["specie"])
    voci = voci_array(finto, "Tavola", "campo")
    prova("array, modo campo, quante", 1, len(voci))
    prova("array, modo campo, specie", 296, voci[0]["specie"])
    prova("array, modo campo, forma", 2, voci[0]["forma"])
    prova("array assente", None, voci_array(finto, "NonEsiste", "campo"))

    finto2 = """
        new(BDSP) { Species = 151, Level = 01, FatefulEncounter = true }, // Mew
        new(BDSP) { Species = 152, Level = 01 }, // non fatidico
"""
    voci = voci_fatidiche(finto2)
    prova("fatidici, quante", 1, len(voci))
    prova("fatidici, specie", 151, voci[0]["specie"])

    prova("corsi del Pokewalker", 27, len(CORSI_POKEWALKER))
    prova("classi dichiarate non lette", 0, len(NON_LETTE))
    prova("tabelle binarie dichiarate", 5, len(BINARI))
    prova("archivi di Pokemon GO dichiarati", 2, len(GO))
    prova("voci con dono a oggetto", 15, len(OGGETTO_DISTRIBUITO))
    specie_biglietti = {s for (_g, _o, _l, s, _f, _lv, _gi, _fa, _r) in OGGETTO_DISTRIBUITO}
    prova("specie dei doni a oggetto", {151, 249, 250, 380, 381, 386, 491, 492, 494},
          specie_biglietti)
    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


ORDINE_CLASSI = ("oggetto-distribuito", "disco-bonus", "periferica", "spinoff", "condizionato",
                 "incursione", "porta-permanente")


def stampa(gruppi, difetti):
    print("Censimento degli esemplari da evento fuori dalla base dei doni segreti")
    print("")
    print("  %-52s %5s %6s" % ("gruppo", "voci", "specie"))
    per_classe = {}
    for g in gruppi:
        per_classe.setdefault(g["classe"], []).append(g)
    for classe in ORDINE_CLASSI:
        for g in per_classe.get(classe, []):
            if not g["letto"]:
                print("  %-52s %5s %6s" % (g["etichetta"][:52], "n.l.", "n.l."))
                continue
            print("  %-52s %5d %6d"
                  % (g["etichetta"][:52], len(g["voci"]),
                     len({v["specie"] for v in g["voci"]})))
    tutte = [v for g in gruppi if g["letto"] for v in g["voci"]]
    scad = [v for g in gruppi if g["letto"] and g["sotto_scadenza"] for v in g["voci"]]
    print("")
    print("  totale delle voci censite:            %5d" % len(tutte))
    print("  specie distinte fra queste voci:      %5d" % len({v["specie"] for v in tutte}))
    print("  di cui sotto scadenza:                %5d voci, %d specie distinte"
          % (len(scad), len({v["specie"] for v in scad})))
    print("")
    print("  Voci che una fonte dichiara mai distribuite, quindi assenti per risultato e non")
    print("  per lacuna: %d" % len(MAI_DISTRIBUITE))
    print("  Classi che esistono e che questo programma non legge: %d" % len(NON_LETTE))
    if difetti:
        print("")
        for nome, motivo in difetti:
            print("  difetto: %s: %s" % (nome, motivo))


def scrivi(percorso, gruppi, difetti):
    r = []
    r.append("# Censimento degli esemplari da evento fuori dalla base dei doni segreti")
    r.append("")
    r.append("> Documento generato da `tools/censimento-eventi-tabelle.py`. Non si modifica a "
             "mano: si rigenera. La fonte sono le tabelle degli incontri di PKHeX, che il "
             "programma legge dal clone passato sulla riga di comando.")
    r.append("")
    r.append("Questo censimento esiste perché l'asse degli eventi della lista di spunta nasce da "
             "due sole fonti, cioè la tabella delle carte meraviglia di terza generazione e i "
             "file binari della base dei doni segreti, ed è cieco su tutto ciò che il "
             "verificatore tiene altrove. Il difetto è di copertura e non di lettura, quindi non "
             "produce alcun errore e non si manifesta da sé: una distribuzione che nessuna "
             "tabella letta dichiara semplicemente non compare, e la lista sembra completa.")
    r.append("")
    r.append("Le classi restano separate, e non è una precauzione formale. Una distribuzione in "
             "cui il dono era un oggetto è un evento a tutti gli effetti, e la sola ragione per "
             "cui sfugge è che il verificatore la tiene fra gli incontri statici; un esemplare di "
             "Colosseum non è invece una distribuzione ma un incontro ordinario di un gioco "
             "diverso, irripetibile altrove; un dono condizionato di ottava generazione pretende "
             "il salvataggio di un altro gioco e non una consegna. Sommarle darebbe un totale "
             "grande e inutilizzabile, e deciderebbe al posto di chi colleziona quale sia "
             "l'ambito.")
    r.append("")
    r.append("## Il conto per gruppo")
    r.append("")
    r.append("| Classe | Gen | Gruppo | Voci | Specie distinte | Sotto scadenza |")
    r.append("|---|---|---|---|---|---|")
    for classe in ORDINE_CLASSI:
        for g in gruppi:
            if g["classe"] != classe:
                continue
            if not g["letto"]:
                r.append("| %s | %s | %s | non letto | non letto | %s |"
                         % (g["classe"], g["gen"] if g["gen"] else "varie", g["etichetta"],
                            "sì" if g["sotto_scadenza"] else "no"))
                continue
            r.append("| %s | %s | %s | %d | %d | %s |"
                     % (g["classe"], g["gen"] if g["gen"] else "varie", g["etichetta"],
                        len(g["voci"]), len({v["specie"] for v in g["voci"]}),
                        "sì" if g["sotto_scadenza"] else "no"))
    r.append("")
    tutte = [v for g in gruppi if g["letto"] for v in g["voci"]]
    scad = [v for g in gruppi if g["letto"] and g["sotto_scadenza"] for v in g["voci"]]
    r.append("Le voci censite sono %d e portano %d specie distinte; quelle sotto scadenza sono %d "
             "e portano %d specie distinte. Fino al 2026-09-04 nessuna di esse compariva nella "
             "lista di spunta, che le ignorava tutte: da quella data `tools/checklist-pokedex.py` "
             "invoca questo programma e le voci entrano nel suo asse degli eventi con la classe "
             "dichiarata e il codice `EVT-T-`. Il numero da guardare per misurare quanto pesassero "
             "è quello delle specie distinte sotto scadenza, perché è la parte che il primo tempo "
             "della coda deve coprire e che prima non sapeva di dover coprire."
             % (len(tutte), len({v["specie"] for v in tutte}),
                len(scad), len({v["specie"] for v in scad})))
    r.append("")
    r.append("## Le voci che nessuna fonte dichiara distribuite")
    r.append("")
    r.append("Vanno scritte perché la loro assenza dal censimento è un risultato e non una "
             "lacuna: chi le cercasse senza questa sezione concluderebbe che il censimento sia "
             "incompleto, e cercherebbe per giorni una distribuzione che non è mai avvenuta.")
    r.append("")
    r.append("| Gen | Oggetto | Luogo | Dex | Perché non c'è |")
    r.append("|---|---|---|---|---|")
    for gen, oggetto, luogo, specie, motivo in MAI_DISTRIBUITE:
        r.append("| %d | %s | %s | %d | %s |" % (gen, oggetto, luogo, specie, motivo))
    r.append("")
    r.append("## Che cosa questo censimento non copre")
    r.append("")
    if NON_LETTE:
        r.append("Un censimento che tacesse le proprie lacune sarebbe peggio di uno dichiarato "
                 "incompleto, perché chi lo legge conta le voci e conclude di avere l'insieme "
                 "intero. Queste classi esistono, il programma non le legge, e il motivo è "
                 "scritto accanto a ciascuna.")
        r.append("")
        r.append("| Gen | Classe | Dove sta nella fonte | Perché non è letta |")
        r.append("|---|---|---|---|")
        for gen, classe, dove, perche in NON_LETTE:
            r.append("| %d | %s | %s | %s |" % (gen, classe, dove, perche))
    else:
        r.append("Nessuna, fra le classi che il verificatore porta. Il 2026-09-04 questa sezione "
                 "elencava tre classi non lette, cioè le incursioni da distribuzione di ottava e "
                 "di nona generazione e i trasferimenti da Pokemon GO, e nella stessa giornata "
                 "sono state lette tutte e tre: la dichiarazione di non lettura era onesta, ma era "
                 "un debito e non una conclusione. Resta vero, e va ripetuto qui perché è il "
                 "limite di questo documento, che il censimento copre ciò che il verificatore "
                 "sa: una distribuzione che nessuna sua tabella conosce non comparirebbe, e non "
                 "avremmo modo di accorgercene da dentro.")
    r.append("")
    for classe in ORDINE_CLASSI:
        for g in gruppi:
            if g["classe"] != classe or not g["letto"] or not g["voci"]:
                continue
            r.append("## %s" % g["etichetta"])
            r.append("")
            r.append("| Dex | Forma | Descrizione | Riferimento nella fonte |")
            r.append("|---|---|---|---|")
            for v in g["voci"]:
                r.append("| %d | %d | %s | `%s` |"
                         % (v["specie"], v.get("forma", 0),
                            (v.get("commento") or "-").replace("|", "/"),
                            v.get("riferimento", "-")))
            r.append("")
    if difetti:
        r.append("## Difetti dichiarati")
        r.append("")
        for nome, motivo in difetti:
            r.append("- %s: %s" % (nome, motivo))
        r.append("")
    io.open(percorso, "w", encoding="utf-8", newline="").write("\n".join(r) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", help="clone del verificatore")
    ap.add_argument("--markdown", help="scrive il censimento come documento tracciato")
    ap.add_argument("--self-test", action="store_true", dest="self_test",
                    help="controlla le funzioni di lettura senza toccare il clone")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.pkhex:
        ap.error("serve --pkhex, oppure --self-test")
    gruppi, difetti = censisci(a.pkhex)
    stampa(gruppi, difetti)
    if a.markdown:
        scrivi(a.markdown, gruppi, difetti)
        print("")
        print("  scritto " + a.markdown)
    return 0


if __name__ == "__main__":
    sys.exit(main())
