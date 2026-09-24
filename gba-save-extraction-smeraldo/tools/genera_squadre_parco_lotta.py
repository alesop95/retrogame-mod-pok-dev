#!/usr/bin/env python3
"""Genera in software i quindici esemplari del catalogo del Parco Lotta, in doppia copia, come strutture di terza generazione.

Perche' esiste
--------------

E' la prima delle due fasi che ADR-067 prescrive: produrre gli esemplari e validarli in software, prima e separatamente dalla scrittura nei box della cartuccia vera, che e' la seconda fase e che non avviene qui. Questo programma non tocca alcun salvataggio e non apre nulla in scrittura fuori dalla propria cartella di uscita.

Il vincolo che governa tutto e' ADR-070, cioe' che ogni esemplare sia ottenibile in terza generazione. Non basta quindi che i campi siano nell'intervallo giusto: devono stare fra loro in una relazione che esiste in natura, ed e' la parte difficile.

La correlazione fra personalita' e valori individuali, e perche' non si sceglie
-------------------------------------------------------------------------------

In terza generazione il valore di personalita' e i sei valori individuali non sono campi indipendenti. Nascono dalle quattro estrazioni consecutive di un generatore congruenziale a partire da un seme, ed e' il primo metodo che `tools/genera-incontro-gen3.py` gia' implementa e da cui questo programma lo riusa invece di riscriverlo. Scegliere la personalita' per avere la natura voluta e poi scrivere valori individuali a piacere produce un esemplare i cui campi sono tutti plausibili uno per uno e la cui relazione reciproca non esiste: e' precisamente cio' che un verificatore cerca, ed e' la differenza fra un esemplare ottenibile e uno fabbricato.

Ne segue che la personalita' non si sceglie e i valori individuali nemmeno: si sceglie il seme, e quello decide entrambi. Il problema diventa quindi trovare un seme che produca insieme la natura richiesta, l'abilita' richiesta, il sesso richiesto e valori individuali abbastanza alti. Cercarlo in avanti su quattro miliardi di semi non e' praticabile.

La ricerca all'indietro, che e' il cuore di questo programma
------------------------------------------------------------

Si inverte. I due valori a quindici bit che compongono i sei valori individuali sono la terza e la quarta estrazione, quindi fissare i valori individuali voluti fissa i sedici bit alti di due stati consecutivi del generatore. Dei sedici bit bassi del primo dei due non si sa nulla, ma sono soltanto sessantaseimila possibilita' da provare, e per ciascuna basta un passo del generatore per vedere se il secondo stato ha in alto i bit giusti. Ne sopravvivono pochissime, e da ciascuna si risale di tre passi all'indietro, cosa che si puo' fare perche' il moltiplicatore e' dispari e quindi invertibile modulo due alla trentaduesima, ottenendo il seme e con esso la personalita'.

A quel punto la personalita' e' determinata e non negoziabile: o ha la natura giusta o non ce l'ha. Si varia allora la distribuzione dei valori individuali fra quelle accettabili, dalla migliore in giu', e si prova finche' una non produce anche la natura, l'abilita' e il sesso richiesti. Poiche' le statistiche che a un esemplare non servono possono valere qualunque cosa, le distribuzioni accettabili sono migliaia e una che soddisfi tutto si trova quasi sempre.

Cio' che il programma dichiara quando non ci riesce, e non e' un dettaglio: se nessuna distribuzione accettabile produce i vincoli, il programma allarga la tolleranza di un punto per volta sulle statistiche che contano e lo scrive nel rapporto. Un esemplare con trenta invece di trentuno in una statistica e' comunque buono; un esemplare la cui provenienza non esiste no, e quella non si allarga mai.

Uso
---

    python gba-save-extraction-smeraldo/tools/genera_squadre_parco_lotta.py --catalogo gba-save-extraction-smeraldo/squadre-parco-lotta.json --dati gba-save-extraction-smeraldo/dati-gen3.json --out _notes/lotti/lotto-parco-lotta
"""

import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RADICE.joinpath("pokemon-gen12-gen3-bridge-original-hardware")))

from pokebridge import charmap as cm  # noqa: E402
from pokebridge import gen3  # noqa: E402

MOLT = 0x41C64E6D
SOMMA = 0x00006073
# L'inverso del moltiplicatore modulo due alla trentaduesima. Esiste perche' il moltiplicatore e'
# dispari, ed e' cio' che rende il generatore percorribile all'indietro.
MOLT_INV = pow(MOLT, -1, 1 << 32)

# Il generatore di Colosseum e XD, che non e' quello delle cartucce: stessa forma, costanti diverse,
# da `XDRNG.cs` del verificatore. Un esemplare che viene da quei giochi porta una correlazione fra
# personalita' e valori individuali costruita con QUESTE costanti, e una coppia del primo metodo accanto
# al gioco di origine quindici sarebbe tanto irregolare quanto una coppia assente.
XD_MOLT = 0x000343FD
XD_SOMMA = 0x00269EC3
XD_MOLT_INV = pow(XD_MOLT, -1, 1 << 32)
# La soglia della schermata del nome, da `IsValidNameScreenEndSeed` in `MethodCXD.cs`: a ogni fotogramma
# il gioco fa comparire una palla con probabilita' di un decimo, cioe' quando i sedici bit alti del
# generatore non superano questo valore.
SOGLIA_SCHERMATA_NOME = 0x1999
# Le due coppie di identificativi che il verificatore considera sospette per costruzione.
ID_SOSPETTI = {(12345, 54321), (15040, 18831)}

NATURE = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish",
          "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet",
          "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"]

# L'ordine con cui i sei valori individuali stanno nelle due parole a quindici bit, che non e'
# l'ordine con cui si scrivono di solito: la prima parola porta salute, attacco e difesa, la
# seconda velocita', attacco speciale e difesa speciale. Scambiarle produce un esemplare i cui
# campi sono tutti nell'intervallo e la cui relazione non esiste.
ORDINE_IV = ("hp", "atk", "def", "spe", "spa", "spd")

AMICIZIA = {"STANDARD_FRIENDSHIP": 70}

# La lingua dell'esemplare, da `LANGUAGE_ITALIAN` in `include/constants/global.h`. Non e' un campo
# cosmetico e non si lascia al valore piu' comune: se l'allenatore di origine coincide con quello del
# salvataggio, come qui, un verificatore pretende che la lingua coincida con quella della cartuccia,
# perche' un esemplare non scambiato non puo' venire da un gioco di un'altra lingua. Una prima stesura
# scriveva due, cioe' inglese, e produceva ventotto esemplari respinti su ventotto senza che nessun
# altro campo fosse sbagliato: il difetto era invisibile dall'interno e lo ha rivelato PKHeX.
LINGUA_ITALIANO = 4


def _fratello():
    """Il generatore degli incontri, per riusarne il primo metodo invece di riscriverlo."""
    percorso = RADICE.joinpath("tools", "genera-incontro-gen3.py")
    spec = importlib.util.spec_from_file_location("genera_incontro_gen3", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def indietro(stato):
    return ((stato - SOMMA) * MOLT_INV) & 0xFFFFFFFF


def avanti(stato):
    return (stato * MOLT + SOMMA) & 0xFFFFFFFF


def xd_avanti(stato):
    return (stato * XD_MOLT + XD_SOMMA) & 0xFFFFFFFF


def xd_indietro(stato):
    return ((stato - XD_SOMMA) * XD_MOLT_INV) & 0xFFFFFFFF


def parole_iv(valori):
    """Le due parole a quindici bit che corrispondono a una distribuzione di valori individuali."""
    uno = (valori["hp"] & 31) | ((valori["atk"] & 31) << 5) | ((valori["def"] & 31) << 10)
    due = (valori["spe"] & 31) | ((valori["spa"] & 31) << 5) | ((valori["spd"] & 31) << 10)
    return uno, due


def bit_abilita_di(abilita, personalita):
    """Il bit dell'abilita' che una cartuccia scrive accanto a questa personalita'.

    La regola non e' quella che il nome del campo suggerisce, cioe' avere due abilita' diverse, ma avere il secondo slot pieno. In `CreateBoxMon` il gioco copia il bit basso della personalita' quando il secondo slot della specie non e' vuoto, anche se contiene la stessa abilita' del primo, e lascia il bit a zero quando lo slot e' vuoto. Flygon, Vibrava e Granbull hanno i due slot uguali, e il verificatore li nomina come eccezione in `AbilityVerifier.cs`: su di essi il bit deve seguire la personalita', sulle specie a slot unico deve restare spento. Una prima stesura lo legava invece alla diversita' delle due abilita', e il Flygon con personalita' dispari del quinto giro e' stato l'unico esemplare respinto su sessanta.
    """
    return (personalita & 1) if len(abilita) == 2 and abilita[1] != "None" else 0


def valori_ammessi(esemplare, tolleranza):
    """Per ogni statistica, l'insieme dei valori individuali accettabili a questa tolleranza.

    Le statistiche che contano vogliono il massimo e scendono al piu' della tolleranza. Quella di attacco fa eccezione dove il catalogo la dichiara a zero, perche' su un attaccante speciale un attacco basso riduce il danno che l'esemplare si infligge da solo quando e' confuso, e li' la tolleranza si applica verso l'alto invece che verso il basso. Le statistiche dichiarate libere accettano qualunque valore fin dal primo giro, perche' su una statistica che non si usa un valore alto non fa ne' bene ne' male e pretenderlo restringerebbe la ricerca per nulla.
    """
    libere = set(esemplare.get("iv_liberi", []))
    ammessi = {}
    for stat in ORDINE_IV:
        if stat in libere:
            ammessi[stat] = list(range(31, -1, -1))
        elif stat == "atk" and esemplare.get("iv_attacco") == 0:
            ammessi[stat] = list(range(0, tolleranza + 1))
        else:
            ammessi[stat] = list(range(31, 31 - tolleranza - 1, -1))
    return ammessi


def punti_base_di(esemplare):
    """I punti base dichiarati dal catalogo nella forma "252 HP / 252 SpA / 4 Spe", come dizionario."""
    punti = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
    for pezzo in esemplare["punti_base"].split("/"):
        parti = pezzo.strip().split()
        if len(parti) == 2 and parti[0].isdigit() and parti[1].lower() in punti:
            punti[parti[1].lower()] = int(parti[0])
    return punti


def statistiche(specie_dati, natura, iv, punti, livello=50):
    """Le sei statistiche come le calcola il gioco, da `CALC_STAT` e `ModifyStatByNature` in `src/pokemon.c`.

    Ogni divisione e' intera, ed e' la ragione per cui al livello 50 un punto di valore individuale sposta la statistica soltanto meta' delle volte: il valore entra moltiplicato per il livello e diviso per cento, quindi conta per mezzo punto, e mezzo punto si vede solo quando completa un intero. I punti base entrano divisi per quattro e poi dimezzati allo stesso modo, quindi al livello 50 ne servono otto per un punto di statistica, e non quattro come al livello 100.
    """
    base = specie_dati["base"]
    indice = NATURE.index(natura)
    aumenta, riduce = indice // 5, indice % 5
    fuori = {"hp": (2 * base["hp"] + iv["hp"] + punti["hp"] // 4) * livello // 100 + livello + 10}
    for posto, stat in enumerate(("atk", "def", "spe", "spa", "spd")):
        n = (2 * base[stat] + iv[stat] + punti[stat] // 4) * livello // 100 + 5
        if aumenta != riduce:
            if posto == aumenta:
                n = n * 110 // 100
            elif posto == riduce:
                n = n * 90 // 100
        fuori[stat] = n
    return fuori


def chiave_gemelle(specie_dati, esemplare):
    """Che cosa devono condividere due copie per essere gemelle: le statistiche, oppure i valori individuali quando l'esemplare usa Introforza, il cui tipo e la cui potenza dipendono dai valori individuali e non dalle statistiche."""
    if any(m.lower().replace(" ", "") == "hiddenpower" for m in esemplare["mosse"]):
        return lambda c: tuple(sorted(c["iv"].items()))
    punti = punti_base_di(esemplare)
    return lambda c: tuple(sorted(statistiche(specie_dati, esemplare["natura"], c["iv"], punti).items()))


def valore_gemelle(specie_dati, esemplare):
    """Quanto vale un gruppo di gemelle: prima la somma di tutte le statistiche, poi quella delle statistiche su cui il catalogo investe punti base, sempre senza l'attacco quando il catalogo lo vuole basso."""
    punti = punti_base_di(esemplare)
    basso = esemplare.get("iv_attacco") == 0

    def valore(c):
        st = statistiche(specie_dati, esemplare["natura"], c["iv"], punti)
        contate = {k: v for k, v in st.items() if not (basso and k == "atk")}
        # Prima tutte le statistiche e poi quelle investite, e non il contrario: una statistica senza
        # punti base puo' essere quella che l'esemplare usa per attaccare, come l'attacco speciale di un
        # Moltres che porta Lanciafiamme con i punti base su salute, difesa e velocita'.
        return (sum(contate.values()), sum(v for k, v in contate.items() if punti[k] > 0))
    return valore


def gruppo_gemelle(liberi, quante, chiave=None, valore=None):
    """Fra i candidati gia' ordinati dal migliore, il primo gruppo di almeno `quante` che condividono gli stessi valori individuali.

    Le copie di un esemplare devono essere gemelle, cioe' avere le stesse statistiche, e non soltanto la stessa natura e gli stessi obiettivi. Il criterio e' la chiave passata da chi chiama, di solito le statistiche calcolate con la formula del gioco, perche' pretendere valori individuali identici costa punti veri per un'uguaglianza che in lotta non si vede. La prima stesura prendeva per ciascuna copia il miglior seme ancora libero, e su un incontro statico due semi diversi danno quasi sempre valori individuali diversi di un punto: il proprietario lo ha visto in gioco il 2026-09-23 come statistiche che differivano di uno fra due copie dichiarate uguali. Due semi con gli stessi valori individuali e personalita' diverse esistono, perche' la personalita' viene dalle due estrazioni che precedono i valori individuali e un valore individuale si ottiene da piu' stati; ma sono rari, e vanno cercati apposta invece di sperare che capitino.

    Restituisce la lista del gruppo, oppure None se a questa tolleranza nessun gruppo e' abbastanza grande: chi chiama allarga allora la tolleranza.
    """
    chiave = chiave or (lambda c: tuple(sorted(c["iv"].items())))
    gruppi = {}
    ordine = []
    for c in liberi:
        k = chiave(c)
        if k not in gruppi:
            gruppi[k] = []
            ordine.append(k)
        gruppi[k].append(c)
    pieni = [gruppi[k] for k in ordine if len(gruppi[k]) >= quante]
    if not pieni:
        return None
    if valore is None:
        return pieni[0]
    return max(pieni, key=lambda g: valore(g[0]))


def cerca_seme(specie_dati, esemplare, allenatore, tolleranza_massima=6, escluse=(), quante=1):
    """Trova un seme del primo metodo che produca insieme natura, abilita', sesso e valori individuali accettabili.

    La ricerca e' rovesciata rispetto a quella ovvia, e la ragione e' di costo. Fissare una distribuzione completa di valori individuali e cercarne i semi costa sessantacinquemila passi per ogni distribuzione, e le distribuzioni accettabili sono migliaia: il conto non sta in piedi. Si fissa invece la sola prima parola, cioe' salute, attacco e difesa, che sono poche combinazioni, e si percorre una volta sola lo spazio dei sedici bit ignoti: ogni passo produce una seconda parola diversa, quindi un solo passaggio copre in un colpo tutte le distribuzioni che condividono la prima parola. Il costo scende di tre ordini di grandezza.

    Una prima stesura di questo programma non lo faceva ed esplorava una distribuzione sola per livello di tolleranza: falliva su nove esemplari su quindici. Il difetto non era nella teoria ma nell'ampiezza della ricerca, ed e' il genere di errore che si manifesta come una impossibilita' apparente invece che come un errore.

    Restituisce TUTTI i semi che soddisfano i vincoli a quella tolleranza, ordinati dal migliore, e non il solo migliore. La ragione e' un difetto che una prima stesura aveva e che soltanto un verificatore esterno ha rivelato: due esemplari con la stessa natura e lo stesso profilo di valori individuali, per esempio tre esemplari Decisi con gli stessi obiettivi, ricevevano lo STESSO seme e quindi lo stesso valore di personalita', perche' la ricerca era deterministica e si fermava al primo. Tre Pokemon distinti con la medesima personalita' non esistono, e PKHeX lo ha segnalato come condivisione del valore fra tipi di incontro diversi. Chi chiama sceglie percio' fra i candidati il primo non ancora usato, e le due copie di uno stesso esemplare ne prendono due diversi.

    Il punteggio somma i valori individuali escludendo l'attacco quando il catalogo lo vuole basso, altrimenti premierebbe proprio cio' che si e' chiesto di evitare.
    """
    natura_voluta = esemplare["natura"]
    abilita = specie_dati["abilita"]
    due_abilita = len(abilita) == 2 and abilita[1] not in ("None", abilita[0])
    indice_abilita = abilita.index(esemplare["abilita"]) if esemplare["abilita"] in abilita else 0
    soglia = specie_dati.get("soglia_femmina")
    sesso_voluto = esemplare.get("sesso")
    tid, sid = allenatore["id"], allenatore["segreto"]
    attacco_basso = esemplare.get("iv_attacco") == 0
    escluse = set(escluse)
    migliori = []
    scelte = None
    trovata = None

    for tolleranza in range(tolleranza_massima + 1):
        ammessi = valori_ammessi(esemplare, tolleranza)
        ok_spe = set(ammessi["spe"])
        ok_spa = set(ammessi["spa"])
        ok_spd = set(ammessi["spd"])
        candidati = []
        for hp in ammessi["hp"]:
            for atk in ammessi["atk"]:
                for dif in ammessi["def"]:
                    iv1 = hp | (atk << 5) | (dif << 10)
                    for alto in (iv1, iv1 | 0x8000):
                        base = alto << 16
                        for basso in range(1 << 16):
                            s3 = base | basso
                            iv2 = (((s3 * MOLT + SOMMA) & 0xFFFFFFFF) >> 16) & 0x7FFF
                            spe = iv2 & 31
                            if spe not in ok_spe:
                                continue
                            spa = (iv2 >> 5) & 31
                            if spa not in ok_spa:
                                continue
                            spd = (iv2 >> 10) & 31
                            if spd not in ok_spd:
                                continue
                            s2 = indietro(s3)
                            s1 = indietro(s2)
                            personalita = (((s2 >> 16) & 0xFFFF) << 16) | ((s1 >> 16) & 0xFFFF)
                            if NATURE[personalita % 25] != natura_voluta:
                                continue
                            if due_abilita and (personalita & 1) != indice_abilita:
                                continue
                            if soglia is not None and sesso_voluto:
                                femmina = (personalita & 0xFF) < soglia
                                if femmina != (sesso_voluto == "femmina"):
                                    continue
                            if ((personalita >> 16) ^ (personalita & 0xFFFF) ^ tid ^ sid) < 8:
                                continue
                            valori = {"hp": hp, "atk": atk, "def": dif,
                                      "spe": spe, "spa": spa, "spd": spd}
                            punteggio = sum(v for k, v in valori.items()
                                            if not (attacco_basso and k == "atk"))
                            candidati.append((punteggio, {
                                "seme": indietro(s1),
                                "personalita": personalita,
                                "iv": valori,
                                "scarto": tolleranza,
                                "bit_abilita": bit_abilita_di(abilita, personalita),
                            }))
        if candidati:
            candidati.sort(key=lambda c: -c[0])
            liberi = [c[1] for c in candidati if c[1]["personalita"] not in escluse]
            # Si allarga la tolleranza anche quando dei candidati ci sono, se non bastano: due specie
            # con la stessa natura e lo stesso profilo producono la MEDESIMA lista, perche' la lista
            # dipende dai vincoli e non dalla specie, e la seconda trova consumato cio' che la prima ha
            # preso. Fermarsi qui faceva fallire sette esemplari su trentatre con un messaggio che
            # parlava di candidati insufficienti invece che della causa.
            # Non ci si ferma alla prima tolleranza che offre una coppia di gemelle: una tolleranza piu'
            # larga contiene tutti i candidati della precedente e altri ancora, e fra questi puo' esserci
            # una coppia con le statistiche che contano piu' alte, perche' lo scarto cade su una
            # statistica che non si usa. Si proseguono due gradini e si tiene la coppia migliore.
            gemelle = gruppo_gemelle(liberi, quante, chiave_gemelle(specie_dati, esemplare),
                                     valore_gemelle(specie_dati, esemplare))
            if gemelle and (scelte is None or valore_gemelle(specie_dati, esemplare)(gemelle[0])
                            > valore_gemelle(specie_dati, esemplare)(scelte[0])):
                scelte = gemelle
            if scelte is not None:
                if trovata is None:
                    trovata = tolleranza
                if tolleranza >= trovata + 2:
                    return scelte
            migliori = liberi
    return scelte if scelte is not None else migliori



def personalita_di_metodo_uno(iv):
    """Restituisce l'insieme dei valori di personalita' che, accanto a QUESTI valori individuali, formerebbero una coppia del primo metodo.

    Serve a una verifica al contrario. Su un esemplare allevato la personalita' deve essere scorrelata dai valori individuali, e il modo di dimostrarlo non e' affermarlo ma escludere l'insieme delle personalita' che una correlazione la produrrebbero. L'insieme e' piccolo e si calcola in un passaggio solo: fissati i valori individuali, la prima parola fissa i sedici bit alti dello stato che li genera, a meno del bit di riempimento, e i sedici bit bassi si percorrono tutti; ogni stato che riproduce anche la seconda parola determina i due tiri precedenti, e quindi una personalita'.
    """
    parola1 = iv["hp"] | (iv["atk"] << 5) | (iv["def"] << 10)
    parola2 = iv["spe"] | (iv["spa"] << 5) | (iv["spd"] << 10)
    fuori = set()
    for alto in (parola1, parola1 | 0x8000):
        base = alto << 16
        for basso in range(1 << 16):
            s3 = base | basso
            if ((((s3 * MOLT + SOMMA) & 0xFFFFFFFF) >> 16) & 0x7FFF) != parola2:
                continue
            s2 = indietro(s3)
            s1 = indietro(s2)
            fuori.add((((s2 >> 16) & 0xFFFF) << 16) | ((s1 >> 16) & 0xFFFF))
    return fuori


def cerca_personalita_libera(specie_dati, esemplare, allenatore, chiave, escluse=(), quante=1):
    """Sceglie la personalita' di un esemplare ALLEVATO, dove la correlazione con i valori individuali non deve esistere.

    Un uovo della terza generazione non nasce dal primo metodo, e il verificatore lo pretende: nel suo sorgente la forma di correlazione suggerita per l'incontro da uovo e' nessuna, e una coppia riconosciuta come primo metodo viene respinta. E' la causa per cui quarantadue righe su sessantaquattro venivano rifiutate pur avendo luogo, livello e gioco corretti, e non si sarebbe potuta trovare guardando i campi: nessun campo la contiene, perche' e' una relazione fra due campi.

    Il vincolo capovolge la convenienza. Sulle statiche il seme decide insieme personalita' e valori individuali, e si prende cio' che passa, con lo scarto di uno o due punti che il catalogo registra; qui i due sono indipendenti, quindi i valori individuali si scrivono esatti come il catalogo li vuole e la ricerca lavora sulla sola personalita'. Gli esemplari allevati escono percio' migliori di quelli statici, non peggiori.

    I vincoli sulla personalita' sono quattro e vengono tutti dal sorgente del verificatore: natura, che e' il resto della divisione per venticinque; abilita', che per una specie a due abilita' e' il bit meno significativo, perche' il verificatore ricalcola l'abilita' da quel bit; sesso, dalla soglia della specie sugli otto bit bassi; e assenza di cromaticita', per non consegnare per sbaglio un esemplare cromatico dove non lo si e' chiesto. Il valore zero e' escluso, perche' la generazione di un uovo non lo produce mai.

    La sequenza dei candidati e' deterministica e dipende dalla chiave dell'esemplare, cosi' che due corse dello stesso catalogo diano lo stesso lotto e due esemplari diversi non partano dallo stesso punto.
    """
    natura_voluta = esemplare["natura"]
    abilita = specie_dati["abilita"]
    due_abilita = len(abilita) == 2 and abilita[1] not in ("None", abilita[0])
    indice_abilita = abilita.index(esemplare["abilita"]) if esemplare["abilita"] in abilita else 0
    soglia = specie_dati.get("soglia_femmina")
    sesso_voluto = esemplare.get("sesso")
    tid, sid = allenatore["id"], allenatore["segreto"]

    iv = {}
    for stat in ORDINE_IV:
        if stat == "atk" and esemplare.get("iv_attacco") == 0:
            iv[stat] = 0
        else:
            iv[stat] = 31
    vietate = personalita_di_metodo_uno(iv)

    escluse = set(escluse)
    stato = (sum(ord(c) * (i + 1) for i, c in enumerate(chiave)) * 2654435761) & 0xFFFFFFFF
    trovate = []
    for _ in range(1 << 22):
        stato = avanti(stato)
        personalita = (((stato >> 16) & 0xFFFF) << 16) | ((avanti(stato) >> 16) & 0xFFFF)
        stato = avanti(stato)
        if personalita == 0 or personalita in escluse or personalita in vietate:
            continue
        if NATURE[personalita % 25] != natura_voluta:
            continue
        if due_abilita and (personalita & 1) != indice_abilita:
            continue
        if soglia is not None and sesso_voluto:
            femmina = (personalita & 0xFF) < soglia
            if femmina != (sesso_voluto == "femmina"):
                continue
        if ((personalita >> 16) ^ (personalita & 0xFFFF) ^ tid ^ sid) < 8:
            continue
        trovate.append({
            "seme": None,
            "personalita": personalita,
            "iv": dict(iv),
            "scarto": 0,
            "bit_abilita": bit_abilita_di(abilita, personalita),
        })
        if len(trovate) >= quante:
            return trovate
    return trovate


def schermata_nome_valida(stato):
    """Porta di `IsValidNameScreenEndSeed`: dice se il gioco puo' uscire dalla schermata del nome su questo stato.

    Lo stato e' accettabile in due modi, e il verificatore li prova entrambi. Il primo e' arrivarci senza palle, cioe' con quattro fotogrammi consecutivi i cui sedici bit alti superano la soglia. Il secondo e' esserci catapultati da una palla comparsa poco prima, che consuma quattro chiamate del generatore: allora si risale oltre la palla e si ripete la domanda su uno stato piu' vecchio. La ricorsione e' quella del sorgente, riga per riga.
    """
    p1 = (stato >> 16) > SOGLIA_SCHERMATA_NOME
    stato = xd_indietro(stato)
    p2 = (stato >> 16) > SOGLIA_SCHERMATA_NOME
    stato = xd_indietro(stato)
    p3 = (stato >> 16) > SOGLIA_SCHERMATA_NOME
    stato = xd_indietro(stato)
    p4 = (stato >> 16) > SOGLIA_SCHERMATA_NOME
    if p1 and p2 and p3 and p4:
        return True
    for richiesti in ((), (p1,), (p1, p2), (p1, p2, p3)):
        stato = xd_indietro(stato)
        if (stato >> 16) <= SOGLIA_SCHERMATA_NOME and all(richiesti) \
                and schermata_nome_valida(xd_indietro(stato)):
            return True
    return False


def indietro_di_mille(stato):
    for _ in range(1000):
        stato = xd_indietro(stato)
    return stato


def id_colosseum_valido(tid, sid):
    """Porta per forza bruta di `TryGetSeedTrainerID`: esiste uno stato che produca questo identificativo e questo segreto uscendo dalla schermata del nome?

    Non condivide la direzione con `allenatore_colosseum`, che costruisce l'identificativo in avanti, ed e' voluto: questa lo rifa' all'indietro come fa il verificatore, percorrendo i sedici bit ignoti dello stato che ha prodotto l'identificativo, quindi un errore di direzione o di conteggio in una delle due non puo' compensarsi con lo stesso errore nell'altra.
    """
    if tid == sid or tid == 0 or sid == 0 or (tid, sid) in ID_SOSPETTI:
        return False
    for basso in range(1 << 16):
        t = (tid << 16) | basso
        if (xd_avanti(t) >> 16) != sid:
            continue
        if schermata_nome_valida(indietro_di_mille(xd_indietro(t))):
            return True
    return False


def allenatore_colosseum(nome):
    """Costruisce l'identificativo e il segreto di un allenatore di Colosseum che il verificatore accetta.

    In Colosseum e XD l'identificativo non e' libero: il gioco lo estrae dal proprio generatore mille chiamate dopo l'uscita dalla schermata del nome, e il verificatore lo rifiuta se non trova un'uscita plausibile. Si parte quindi da uno stato fisso derivato dal nome, si cerca in avanti uno stato di uscita con quattro fotogrammi senza palle, si avanza di mille, e le due chiamate successive danno identificativo e segreto. Il risultato e' deterministico e si scrive nel catalogo, cosi' che il catalogo lo dichiari invece di lasciarlo implicito nel programma.
    """
    stato = (sum(ord(c) * (i + 1) for i, c in enumerate(nome)) * 2654435761) & 0xFFFFFFFF
    while True:
        stato = xd_avanti(stato)
        precedenti = [stato]
        for _ in range(3):
            precedenti.append(xd_indietro(precedenti[-1]))
        if not all((x >> 16) > SOGLIA_SCHERMATA_NOME for x in precedenti):
            continue
        s = stato
        for _ in range(1000):
            s = xd_avanti(s)
        tid = xd_avanti(s) >> 16
        sid = xd_avanti(xd_avanti(s)) >> 16
        if id_colosseum_valido(tid, sid):
            return {"nome": nome, "id": tid, "segreto": sid}


def cerca_seme_cxd(specie_dati, esemplare, allenatore_origine, tolleranza_massima=6, escluse=(), quante=1):
    """La ricerca di `cerca_seme`, rifatta sulla correlazione di Colosseum e XD.

    L'ordine delle chiamate viene da `MethodCXD.SetFromIVs`, che lo annota come valori individuali, valori individuali, abilita', personalita', personalita': dallo stato della prima parola, la seconda parola e' la chiamata successiva, poi una chiamata per l'abilita', poi la meta' alta e la meta' bassa della personalita'. Due differenze rispetto al primo metodo contano. La personalita' viene DOPO i valori individuali e non prima, e l'abilita' ha una chiamata propria invece di leggersi dal bit basso della personalita': il verificatore infatti accetta per questi giochi qualunque bit senza confrontarlo con la personalita'.

    La cromaticita' si esclude rispetto all'allenatore di origine e non rispetto al salvataggio, perche' e' contro di lui che il gioco la controlla: un esemplare Ombra cromatico viene rifatto dal gioco, e la personalita' risultante appartiene a una variante della correlazione che questo programma non produce.
    """
    natura_voluta = esemplare["natura"]
    abilita = specie_dati["abilita"]
    due_abilita = len(abilita) == 2 and abilita[1] not in ("None", abilita[0])
    slot_pieno = len(abilita) == 2 and abilita[1] != "None"
    indice_abilita = abilita.index(esemplare["abilita"]) if esemplare["abilita"] in abilita else 0
    soglia = specie_dati.get("soglia_femmina")
    sesso_voluto = esemplare.get("sesso")
    tid, sid = allenatore_origine["id"], allenatore_origine["segreto"]
    attacco_basso = esemplare.get("iv_attacco") == 0
    escluse = set(escluse)
    migliori = []
    scelte = None
    trovata = None

    for tolleranza in range(tolleranza_massima + 1):
        ammessi = valori_ammessi(esemplare, tolleranza)
        ok_spe = set(ammessi["spe"])
        ok_spa = set(ammessi["spa"])
        ok_spd = set(ammessi["spd"])
        candidati = []
        for hp in ammessi["hp"]:
            for atk in ammessi["atk"]:
                for dif in ammessi["def"]:
                    iv1 = hp | (atk << 5) | (dif << 10)
                    for alto in (iv1, iv1 | 0x8000):
                        base = alto << 16
                        for basso in range(1 << 16):
                            s1 = base | basso
                            s2 = xd_avanti(s1)
                            iv2 = (s2 >> 16) & 0x7FFF
                            spe = iv2 & 31
                            if spe not in ok_spe:
                                continue
                            spa = (iv2 >> 5) & 31
                            if spa not in ok_spa:
                                continue
                            spd = (iv2 >> 10) & 31
                            if spd not in ok_spd:
                                continue
                            s3 = xd_avanti(s2)
                            s4 = xd_avanti(s3)
                            s5 = xd_avanti(s4)
                            personalita = (s4 & 0xFFFF0000) | (s5 >> 16)
                            if NATURE[personalita % 25] != natura_voluta:
                                continue
                            bit = (s3 >> 16) & 1
                            if due_abilita and bit != indice_abilita:
                                continue
                            # Su una specie con il secondo slot vuoto il bit deve essere zero. Smeraldo
                            # legge l'abilita' con `GetAbilityBySpecies`, che non ha alcun ripiego: con
                            # il bit a uno restituisce il secondo slot, cioe' nessuna abilita', e il
                            # primo Raikou del sesto giro e' apparso cosi' in gioco pur essendo legale
                            # per il verificatore, che su Colosseum accetta qualunque bit.
                            if not slot_pieno and bit:
                                continue
                            if soglia is not None and sesso_voluto:
                                femmina = (personalita & 0xFF) < soglia
                                if femmina != (sesso_voluto == "femmina"):
                                    continue
                            if ((personalita >> 16) ^ (personalita & 0xFFFF) ^ tid ^ sid) < 8:
                                continue
                            valori = {"hp": hp, "atk": atk, "def": dif,
                                      "spe": spe, "spa": spa, "spd": spd}
                            punteggio = sum(v for k, v in valori.items()
                                            if not (attacco_basso and k == "atk"))
                            candidati.append((punteggio, {
                                "seme": xd_indietro(s1),
                                "personalita": personalita,
                                "iv": valori,
                                "scarto": tolleranza,
                                "bit_abilita": bit,
                            }))
        if candidati:
            candidati.sort(key=lambda c: -c[0])
            liberi = [c[1] for c in candidati if c[1]["personalita"] not in escluse]
            # Non ci si ferma alla prima tolleranza che offre una coppia di gemelle: una tolleranza piu'
            # larga contiene tutti i candidati della precedente e altri ancora, e fra questi puo' esserci
            # una coppia con le statistiche che contano piu' alte, perche' lo scarto cade su una
            # statistica che non si usa. Si proseguono due gradini e si tiene la coppia migliore.
            gemelle = gruppo_gemelle(liberi, quante, chiave_gemelle(specie_dati, esemplare),
                                     valore_gemelle(specie_dati, esemplare))
            if gemelle and (scelte is None or valore_gemelle(specie_dati, esemplare)(gemelle[0])
                            > valore_gemelle(specie_dati, esemplare)(scelte[0])):
                scelte = gemelle
            if scelte is not None:
                if trovata is None:
                    trovata = tolleranza
                if tolleranza >= trovata + 2:
                    return scelte
            migliori = liberi
    return scelte if scelte is not None else migliori


def correlazione_cxd(personalita, iv):
    """Porta di `GetXDRNGMatch`, senza il ramo della cromaticita' rifatta: questi valori individuali stanno accanto a questa personalita' in Colosseum e XD?

    Si parte dalla personalita', come fa il verificatore, e non dal seme che il generatore ha usato: si percorrono i sedici bit ignoti dello stato della meta' alta, si tengono quelli che producono la meta' bassa, e si risale di tre chiamate per rileggere le due parole dei valori individuali.
    """
    parola1, parola2 = parole_iv(iv)
    alta, bassa = personalita >> 16, personalita & 0xFFFF
    for basso in range(1 << 16):
        t = (alta << 16) | basso
        if (xd_avanti(t) >> 16) != bassa:
            continue
        b = xd_indietro(xd_indietro(t))
        a = xd_indietro(b)
        if ((a >> 16) & 0x7FFF) == parola1 and ((b >> 16) & 0x7FFF) == parola2:
            return True
    return False


def e_di_colosseum(origine):
    return origine.get("tipo", "").lower().startswith("ombra di colosseum")


AMICIZIA_MASSIMA = 255


def amicizia_di(esemplare, info):
    """L'amicizia con cui l'esemplare esce dal PC: il massimo per chi porta Ritorno, la base della specie per gli altri.

    Ritorno non ha una potenza fissa: `Cmd_happinesstodamagecalculation` in `src/battle_script_commands.c`, riga 8606, la calcola come dieci volte l'amicizia divisa per venticinque. Con l'amicizia di base, settanta, vale ventotto; al massimo, duecentocinquantacinque, vale centodue. La prima stesura scriveva a tutti la base della specie, e quattro esemplari del catalogo, fra cui lo Slaking titolare della Cupola, portavano quindi Ritorno a un terzo della potenza: lo ha notato il proprietario il 2026-09-23. L'amicizia massima e' legittima, perche' in terza generazione si raggiunge giocando, e il verificatore non la vincola su un esemplare che non sia un uovo. Frustrazione vorrebbe il contrario, amicizia zero, e nessun esemplare del catalogo la porta.
    """
    mosse = {"".join(ch for ch in m.lower() if ch.isalnum()) for m in esemplare["mosse"]}
    if "return" in mosse:
        return AMICIZIA_MASSIMA
    if "frustration" in mosse:
        return 0
    return AMICIZIA.get(info["amicizia"], 70)


def componi(esemplare, chiave, specie_dati, dati, allenatore, tabella, esito, strumento):
    specie = esemplare["specie"]
    info = dati["specie"][specie]
    livello = dati["livello_di_gioco"]
    gruppo = info["gruppo_crescita"]

    # La grafia delle mosse diverge fra il catalogo e il sorgente su trattini e apostrofi, per
    # esempio Soft-Boiled contro Soft Boiled: si confronta sulle sole lettere e cifre, come fa gia'
    # il verificatore delle squadre, invece di tenere due grafie sincronizzate a mano.
    per_chiave = {"".join(c for c in k.lower() if c.isalnum()): v for k, v in dati["mosse"].items()}
    mosse = []
    pp = []
    for m in esemplare["mosse"]:
        voce = per_chiave.get("".join(c for c in m.lower() if c.isalnum()))
        if voce is None:
            raise KeyError("mossa ignota nei dati: %r" % m)
        mosse.append(voce["id"])
        # I punti potenza sono massimizzati come se fosse stato usato PP Max su ciascuna mossa,
        # come ADR-067 prescrive: il bonus e' tre sesti in piu' sul valore di base, e il campo
        # dei bonus porta due bit per mossa, quindi tre per tutte e quattro.
        pp.append(min(99, voce["pp"] + (voce["pp"] * 3) // 5))

    # Il campo dei bonus porta due bit per slot e va acceso SOLTANTO sugli slot occupati: un PP Max
    # applicato a una mossa che non c'e' e' una combinazione che il gioco non puo' produrre, ed e'
    # il difetto che rendeva irregolare il Metagross del Palazzo, che porta due mosse per scelta.
    bonus_pp = 0
    for i in range(len(mosse)):
        bonus_pp |= 3 << (2 * i)

    punti_base = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
    etichette = {"hp": "hp", "atk": "atk", "def": "def", "spa": "spa", "spd": "spd", "spe": "spe"}
    for pezzo in esemplare["punti_base"].split("/"):
        parti = pezzo.strip().split()
        if len(parti) == 2 and parti[0].isdigit():
            chiave_ev = etichette.get(parti[1].lower())
            if chiave_ev:
                punti_base[chiave_ev] = int(parti[0])

    # Le cinque statistiche da gara non sono decorazione: l'evoluzione di Feebas in Milotic e'
    # EVO_BEAUTY con soglia 170 in src/data/pokemon/evolution.h, quindi un Milotic con bellezza zero
    # descrive una evoluzione che non puo' essere avvenuta. Il catalogo le dichiara dove servono.
    condizione = {n: 0 for n in ("cool", "beauty", "cute", "smart", "tough")}
    for nome, valore in esemplare.get("condizione", {}).items():
        condizione[nome] = valore

    nome_visibile = specie.upper()
    soprannome = tabella.encode(nome_visibile, length=gen3.NICKNAME_LENGTH)
    origine = esemplare.get("origine", {})
    # Un esemplare che viene da un altro gioco porta l'allenatore di quel gioco, non quello del
    # salvataggio: e' lo scambio dichiarato, e l'identificativo e' quello che il catalogo registra.
    allenatore = origine.get("allenatore", allenatore)
    ot = tabella.encode(allenatore["nome"], length=gen3.OT_NAME_LENGTH)

    # Il Nastro Nazionale non e' un premio facoltativo per un esemplare Ombra: il gioco lo assegna alla
    # purificazione, e il verificatore in `GetValidRibbonStateNational` lo pretende su ogni esemplare di
    # Colosseum o XD che non sia piu' Ombra, e lo vieta su tutti gli altri.
    nastri_merito = 0
    if e_di_colosseum(origine):
        nastri_merito = 1 << gen3.Misc.MERIT_RIBBON_NAMES.index("national")

    # L'esperienza non e' il minimo del livello per tutti, e la ragione e' un vincolo del
    # verificatore che vale la pena enunciare perche' la prima correzione lo aveva frainteso. Il
    # verificatore ragiona cosi': se l'esperienza dell'esemplare e' esattamente quella del suo livello
    # di incontro, allora non ha mai combattuto, e senza combattere i soli punti base ottenibili sono
    # quelli delle vitamine, cioe' al piu' cento per statistica; altrimenti calcola quanta esperienza
    # serviva a guadagnare i punti base dichiarati e la confronta con quella guadagnata davvero.
    #
    # La prima correzione ne aveva dedotto che un esemplare incontrato al livello di gioco fosse
    # condannato ai punti base da vitamine, e la deduzione era sbagliata perche' confondeva il livello
    # con l'esperienza. Il livello si RICAVA dall'esperienza, quindi fra la soglia del livello di
    # gioco e quella del livello successivo c'e' un intervallo intero di valori che lasciano
    # l'esemplare al livello di gioco pur essendo esperienza guadagnata. Su un gruppo di crescita
    # lento quell'intervallo vale novemilacinquecentosessantadue punti al livello cinquanta, mentre i
    # punti base piu' cari del catalogo ne costano qualche centinaio: la finestra e' larga due ordini
    # di grandezza piu' del necessario.
    #
    # Si scrive percio' il massimo dell'intervallo, cioe' un punto sotto la soglia del livello
    # successivo. E' il valore che giustifica il maggior numero di punti base restando al livello di
    # gioco, e descrive un esemplare allenato fin quasi al livello successivo, che e' esattamente cio'
    # che e' avvenuto. Per chi si incontra a un livello piu' basso non serve, perche' i livelli
    # guadagnati portano gia' esperienza in abbondanza.
    esperienza = dati["esperienza"][gruppo][livello]
    if origine.get("livello_incontro", 0) >= livello:
        esperienza = dati["esperienza"][gruppo][livello + 1] - 1

    return gen3.Gen3Mon(
        personality=esito["personalita"],
        ot_id=((allenatore["segreto"] & 0xFFFF) << 16) | (allenatore["id"] & 0xFFFF),
        nickname=soprannome,
        language=LINGUA_ITALIANO,
        flags=0x02,
        ot_name=ot,
        markings=0,
        growth=gen3.Growth(species=info["id"], held_item=strumento,
                           experience=esperienza,
                           pp_bonuses=bonus_pp, friendship=amicizia_di(esemplare, info)),
        attacks=gen3.Attacks(moves=(mosse + [0, 0, 0, 0])[:4], pp=(pp + [0, 0, 0, 0])[:4]),
        evs=gen3.EvsCondition(evs={
            "hp": punti_base["hp"], "atk": punti_base["atk"], "def": punti_base["def"],
            "spd": punti_base["spe"], "satk": punti_base["spa"], "sdef": punti_base["spd"],
        }, contest=condizione, sheen=esemplare.get("lucentezza", 0)),
        misc=gen3.Misc(
            pokerus=0,
            met_location=origine.get("luogo", 32),
            met_level=origine.get("livello_incontro", 0),
            met_game=origine.get("gioco", 3),
            pokeball=origine.get("sfera", 4),
            ot_female=False,
            ivs={"hp": esito["iv"]["hp"], "atk": esito["iv"]["atk"], "def": esito["iv"]["def"],
                 "spd": esito["iv"]["spe"], "satk": esito["iv"]["spa"], "sdef": esito["iv"]["spd"]},
            is_egg=False,
            ability_num=esito["bit_abilita"],
            modern_fateful_encounter=bool(origine.get("fatidico", False)),
            merit_ribbons=nastri_merito,
        ),
    )


def _chiave(nome_mossa):
    return "".join(c for c in nome_mossa.lower() if c.isalnum())


def verifica(uscita, catalogo, dati, manifesto):
    """Rilegge dal disco ogni struttura scritta e controlla che dica cio' che si voleva scrivere.

    Non e' una formalita' e non ripete cio' che la generazione ha appena fatto: legge i byte, li decifra, ne ricompone le sottostrutture e confronta il risultato con il catalogo di partenza. Fra la volonta' e il file ci sono la permutazione delle quattro sottostrutture, la cifratura con la chiave derivata, il checksum e la conversione dell'esperienza in livello, e ciascuno di quei passaggi puo' sbagliare in un modo che nessun campo dichiara.

    Il controllo di simmetria vale piu' degli altri messi insieme: ricifrare cio' che si e' decifrato deve restituire gli stessi byte. Se non li restituisce, una qualunque delle trasformazioni non e' invertibile come si crede, e l'esemplare che il gioco leggera' non e' quello che si e' composto.
    """
    per_mossa = {_chiave(k): v for k, v in dati["mosse"].items()}
    problemi = []
    for voce in manifesto:
        chiave = voce["chiave"]
        esemplare = catalogo["esemplari"][chiave]
        info = dati["specie"][esemplare["specie"]]
        grezzo = Path(uscita).joinpath("esemplari", "%s-copia1.bin" % chiave).read_bytes()
        mon = gen3.Gen3Mon.from_bytes(grezzo)
        prima_copia = voce["copie"][0]
        errori = []
        if mon.growth.species != info["id"]:
            errori.append("specie %d invece di %d" % (mon.growth.species, info["id"]))
        if NATURE[mon.personality % 25] != esemplare["natura"]:
            errori.append("natura %s invece di %s" % (NATURE[mon.personality % 25], esemplare["natura"]))
        # L'esperienza si verifica come intervallo e non come valore, perche' il livello si ricava
        # dall'esperienza e non viceversa: qualunque valore fra la soglia del livello di gioco e quella
        # del livello successivo descrive un esemplare a quel livello. Chi si incontra al livello di
        # gioco porta il massimo dell'intervallo, per giustificare i punti base guadagnati combattendo.
        tabella = dati["esperienza"][info["gruppo_crescita"]]
        minima = tabella[dati["livello_di_gioco"]]
        massima = tabella[dati["livello_di_gioco"] + 1] - 1
        if not minima <= mon.growth.experience <= massima:
            errori.append("esperienza %d fuori dall'intervallo del livello %d, che va da %d a %d"
                          % (mon.growth.experience, dati["livello_di_gioco"], minima, massima))
        letti = {"hp": mon.misc.ivs["hp"], "atk": mon.misc.ivs["atk"], "def": mon.misc.ivs["def"],
                 "spe": mon.misc.ivs["spd"], "spa": mon.misc.ivs["satk"], "spd": mon.misc.ivs["sdef"]}
        if letti != prima_copia["iv"]:
            errori.append("valori individuali %s invece di %s" % (letti, prima_copia["iv"]))
        attese = [per_mossa[_chiave(m)]["id"] for m in esemplare["mosse"]]
        if list(mon.attacks.moves[:len(attese)]) != attese:
            errori.append("mosse diverse da quelle del catalogo")
        abilita = info["abilita"]
        if len(abilita) == 2 and abilita[1] not in ("None", abilita[0]):
            if abilita[mon.misc.ability_num] != esemplare["abilita"]:
                errori.append("abilita' %s invece di %s" % (abilita[mon.misc.ability_num], esemplare["abilita"]))
        origine = esemplare.get("origine", {})
        if e_di_colosseum(origine):
            if not correlazione_cxd(mon.personality, letti):
                errori.append("personalita' e valori individuali non formano una coppia di Colosseum e XD")
            if not mon.misc.has_merit_ribbon("national"):
                errori.append("manca il Nastro Nazionale, obbligatorio per un esemplare Ombra purificato")
            if mon.misc.met_game != 15:
                errori.append("gioco di origine %d invece di 15" % mon.misc.met_game)
            if mon.misc.modern_fateful_encounter:
                errori.append("incontro fatidico acceso, che il verificatore degrada a corrispondenza parziale")
            dichiarato = origine["allenatore"]
            if mon.ot_id != ((dichiarato["segreto"] << 16) | dichiarato["id"]):
                errori.append("identificativo dell'allenatore diverso da quello dichiarato nel catalogo")
        elif mon.misc.ability_num != bit_abilita_di(info["abilita"], mon.personality):
            errori.append("bit dell'abilita' %d, la personalita' ne vuole %d"
                          % (mon.misc.ability_num, bit_abilita_di(info["abilita"], mon.personality)))
        if mon.growth.friendship != amicizia_di(esemplare, info):
            errori.append("amicizia %d invece di %d, che serve alla potenza di Ritorno o Frustrazione"
                          % (mon.growth.friendship, amicizia_di(esemplare, info)))
        if len(abilita) == 2 and abilita[1] == "None" and mon.misc.ability_num:
            errori.append("bit dell'abilita' a uno su una specie con il secondo slot vuoto: in gioco non avrebbe abilita'")
        chiave = chiave_gemelle(info, esemplare)
        for altra in voce["copie"][1:]:
            if chiave(altra) != chiave(prima_copia):
                errori.append("le copie non sono gemelle: valori individuali %s contro %s" % (prima_copia["iv"], altra["iv"]))
        totale = sum(mon.evs.evs.values())
        if totale > 510:
            errori.append("punti base %d, oltre il tetto di 510" % totale)
        if grezzo != mon.to_bytes():
            errori.append("non simmetrico: ricifrare cio' che si e' decifrato non restituisce gli stessi byte")
        if errori:
            problemi.append((chiave, errori))
    return problemi


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--catalogo", required=True)
    p.add_argument("--dati", required=True)
    p.add_argument("--out", required=True,
                   help="la cartella DEL LOTTO, non quella degli esemplari: il programma crea "
                        "lui la sottocartella esemplari e vi scrive accanto il manifesto")
    p.add_argument("--pulisci", action="store_true",
                   help="rimuove dalla cartella degli esemplari i file di un lotto precedente "
                        "prima di scrivere il nuovo, invece di lasciarli mescolati a questo")
    p.add_argument("--allenatore", default="ALEX:45761:56446")
    args = p.parse_args()

    catalogo = json.loads(Path(args.catalogo).read_text(encoding="utf-8"))
    dati = json.loads(Path(args.dati).read_text(encoding="utf-8"))
    dati["livello_di_gioco"] = catalogo["livello"]
    nome, tid, sid = args.allenatore.split(":")
    allenatore = {"nome": nome, "id": int(tid), "segreto": int(sid)}
    tabella = cm.Charmap.gen3()

    strumento_per_chiave = {}
    for squadra in catalogo["squadre"]:
        for v in squadra["esemplari"]:
            if v.get("strumento"):
                strumento_per_chiave.setdefault(v["chiave"], v["strumento"])

    uscita = Path(args.out)

    # Due difetti di uso sono possibili su questo argomento e nessuno dei due si manifesta come un
    # errore, il che li rende peggiori di un errore. Il primo e' passare gia' la cartella degli
    # esemplari: il programma ne creerebbe una dentro, e chi poi carica il lotto nel verificatore si
    # trova due cartelle omonime annidate senza sapere quale sia quella buona. Il secondo e' scrivere
    # un lotto nuovo sopra uno vecchio: i file di un esemplare che nel frattempo e' uscito dal
    # catalogo restano dov'erano, e il lotto caricato e' la somma di due giri diversi, che e' proprio
    # cio' che ogni verifica su questo materiale esiste per escludere.
    if uscita.name == "esemplari":
        raise SystemExit("--out vuole la cartella DEL LOTTO e non quella degli esemplari: questo "
                         "programma crea lui la sottocartella. Passa %s." % uscita.parent)

    cartella = uscita.joinpath("esemplari")
    cartella.mkdir(parents=True, exist_ok=True)
    vecchi = sorted(cartella.glob("*.bin"))
    if vecchi and not args.pulisci:
        raise SystemExit("la cartella %s contiene gia' %d file di un lotto precedente. Rilancia con "
                         "--pulisci per sostituirli, oppure indica una cartella di lotto diversa: "
                         "scrivere sopra lascerebbe in giro gli esemplari usciti dal catalogo, e il "
                         "lotto caricato sarebbe la somma di due giri." % (cartella, len(vecchi)))
    for v in vecchi:
        v.unlink()
    if vecchi:
        print("rimossi %d file del lotto precedente da %s" % (len(vecchi), cartella))
    manifesto = []
    # I valori di personalita' gia' assegnati, perche' due esemplari non possono condividerlo e
    # nemmeno le due copie dello stesso: due Pokemon con la medesima personalita' sono cloni, e un
    # verificatore li rifiuta prima ancora di guardare qualunque altro campo.
    usate = set()
    for chiave, esemplare in sorted(catalogo["esemplari"].items()):
        origine = esemplare.get("origine", {})
        if origine.get("genera") is False or esemplare.get("genera") is False:
            motivo = esemplare.get("nota_esclusione") or origine.get("nota", "provenienza non modellata")
            print("SALTATO %-19s %s" % (chiave, motivo[:90]))
            continue
        info = dati["specie"][esemplare["specie"]]
        # Le due vie sono incompatibili per costruzione e la scelta la detta la provenienza. Un
        # incontro statico DEVE portare una coppia del primo metodo, un esemplare allevato NON deve
        # portarla: sono due regole opposte, e applicare la prima a tutti e' cio' che rendeva
        # irregolare ogni uovo del lotto pur avendone corretti luogo, livello e gioco.
        if e_di_colosseum(origine):
            dichiarato = origine.get("allenatore")
            if not dichiarato or not id_colosseum_valido(dichiarato["id"], dichiarato["segreto"]):
                print("FALLITO %s: l'allenatore di Colosseum dichiarato nel catalogo manca o ha un "
                      "identificativo che la schermata del nome non puo' produrre" % chiave)
                continue
            candidati = cerca_seme_cxd(info, esemplare, dichiarato, escluse=usate,
                                       quante=catalogo["copie_per_esemplare"])
        elif origine.get("tipo", "").startswith("uovo"):
            candidati = cerca_personalita_libera(info, esemplare, allenatore, chiave,
                                                 escluse=usate,
                                                 quante=catalogo["copie_per_esemplare"])
        else:
            candidati = cerca_seme(info, esemplare, allenatore,
                                   escluse=usate, quante=catalogo["copie_per_esemplare"])
        if not candidati:
            print("FALLITO %s: nessun seme trovato entro la tolleranza" % chiave)
            continue
        nome_strumento = strumento_per_chiave.get(chiave)
        strumento = dati["oggetti"].get(nome_strumento, 0) if nome_strumento else 0
        scelti = []
        for esito in candidati:
            if esito["personalita"] in usate:
                continue
            usate.add(esito["personalita"])
            scelti.append(esito)
            if len(scelti) == catalogo["copie_per_esemplare"]:
                break
        if len(scelti) < catalogo["copie_per_esemplare"]:
            print("FALLITO %s: %d candidati distinti su %d richiesti"
                  % (chiave, len(scelti), catalogo["copie_per_esemplare"]))
            continue
        for numero, esito in enumerate(scelti, start=1):
            mon = componi(esemplare, chiave, info, dati, allenatore, tabella, esito, strumento)
            uscita.joinpath("esemplari", "%s-copia%d.bin" % (chiave, numero)).write_bytes(mon.to_bytes())
        manifesto.append({
            "chiave": chiave, "specie": esemplare["specie"], "natura": esemplare["natura"],
            "provenienza": origine.get("tipo"), "luogo": origine.get("nome_luogo"),
            "copie": [{"seme": ("0x%08X" % e["seme"]) if e["seme"] is not None else "nessuno, esemplare allevato", "personalita": "0x%08X" % e["personalita"],
                       "iv": e["iv"], "scarto_tollerato": e["scarto"]} for e in scelti],
            "strumento": nome_strumento,
        })
        print("%-19s %-11s %-8s  %s  scarto %d  personalita' %s" % (
            chiave, esemplare["specie"], esemplare["natura"],
            "/".join(str(scelti[0]["iv"][k]) for k in ORDINE_IV), scelti[0]["scarto"],
            " e ".join("%08X" % e["personalita"] for e in scelti)))

    uscita.joinpath("manifesto.json").write_text(
        json.dumps({"allenatore": allenatore, "livello": catalogo["livello"], "esemplari": manifesto},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n%d esemplari generati, %d file scritti in %s" % (len(manifesto), len(manifesto) * 2, uscita))

    problemi = verifica(uscita, catalogo, dati, manifesto)
    for chiave, errori in problemi:
        for e in errori:
            print("VERIFICA FALLITA %s: %s" % (chiave, e))
    if problemi:
        sys.exit("la verifica ha trovato %d esemplari difettosi: il lotto non e' utilizzabile" % len(problemi))
    print("verifica: %d esemplari riletti dal disco, tutti conformi al catalogo, tutti simmetrici" % len(manifesto))


if __name__ == "__main__":
    main()
