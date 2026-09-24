#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Censisce gli scambi in gioco di tutte le generazioni, dalle tabelle del verificatore.

Perche' questa classe merita un censimento proprio
--------------------------------------------------
Un esemplare da scambio in gioco e' consegnato da un personaggio in cambio di un altro, e porta
l'allenatore di chi lo ha allevato, di norma un soprannome fissato, e in molte generazioni un
valore di personalita' e dei valori individuali scritti nel gioco. Ne segue che non e'
riproducibile da una cattura propria: e' un collezionabile distinto anche quando la sua specie e'
coperta altrove, per la stessa ragione per cui lo e' un esemplare da distribuzione. La classe era
nominata da due enumerazioni della comunita' lette il 2026-09-08 e non era mai stata contata sulla
fonte di primo livello, che sono le tabelle del verificatore.

Come la fonte tiene questi dati, e perche' il conto non e' una somma
--------------------------------------------------------------------
Ogni titolo ha una o piu' tabelle, e le tabelle di una coppia di titoli si sovrappongono per
costruzione: c'e' una tabella comune alla coppia e, accanto, una tabella per ciascuna versione con
le voci che quella versione ha in piu' o in forma diversa. Sommare le lunghezze darebbe quindi un
totale gonfiato. Il programma riferisce entrambi i numeri, cioe' le voci di tabella e le voci
distinte, e la deduplicazione e' dichiarata: due voci sono la stessa quando concordano su specie,
livello e identificativo dell'allenatore.

Il presidio, che e' lo stesso della famiglia
--------------------------------------------
La posizione della specie e del livello dentro la chiamata cambia da una generazione all'altra, e
dedurla a occhio e' il modo di sbagliare senza accorgersene. Le posizioni sono quindi dichiarate in
una tabella dentro questo programma, ricavate una per una dalle firme dei costruttori della fonte
e non indovinate, e ogni voce viene comunque confrontata con il commento che la fonte le scrive
accanto, che nomina la specie in inglese: se il numero e il nome non concordano, il programma lo
riferisce come discordanza invece di scrivere un censimento che sembrerebbe verificato.

Il soprannome, che e' meta' dell'identita' di questi esemplari
--------------------------------------------------------------
Un esemplare da scambio porta un soprannome fissato dal gioco, e quel soprannome e' specifico
della lingua: non e' un dettaglio di resa ma un campo dell'esemplare, e su cartucce italiane
scriverne uno inglese produrrebbe un esemplare che nessuno scambio ha mai consegnato. Fino al
2026-09-14 questo censimento portava le voci e non le stringhe, e la lacuna fu attribuita alla
fonte: era invece del nostro clone, che e' sparso e non scaricava le risorse di testo. La
correzione e' stata estendere il clone, non cercare le stringhe su una fonte di secondo livello,
e le due vie sono state comunque confrontate sulle cinque voci controllabili a mano, che
concordano.

Le stringhe si leggono dagli elenchi che la fonte stessa usa, uno per lingua, e la corrispondenza
fra una tabella e il proprio elenco non si trascrive: si legge dalle due dichiarazioni con cui il
sorgente la stabilisce, cioe' la costante che nomina il file e la variabile che vi si lega. Una
trascrizione di dodici righe sbaglierebbe qui in modo invisibile, perche' un indice letto
nell'elenco sbagliato restituisce comunque un nome.

Un caso va conosciuto perche' la prima stesura lo trattava come difetto e non lo e'. Gli elenchi
occidentali di prima generazione hanno sedici voci e quello giapponese ventisei, perche' gli
scambi del Blu giapponese e uno dei due Nidoran esistono soltanto in quel gioco: per quelle voci
il soprannome italiano non manca, non esiste. Si dichiara difetto soltanto un indice fuori da
ogni elenco, che vorrebbe dire tavola sbagliata o tabella cambiata a monte.

Che cosa questo programma non fa
--------------------------------
Non produce alcun esemplare, non giudica alcuna legittimita' e non decide se una voce entri
nell'obiettivo di collezione. Dichiara pero' due dati che servono a quella decisione. Il primo e'
se la voce porti un valore di personalita' fissato nella fonte: dove c'e', l'esemplare e'
riproducibile byte per byte senza alcuna ricerca di semi; dove manca, la fedelta' va discussa come
per le altre classi. Il secondo e' il soprannome nelle lingue che servono, senza il quale un
esemplare riproducibile byte per byte resta comunque non scrivibile.

Uso
---
    python tools/censimento-scambi.py --pkhex _notes/fonti/pkhex
    python tools/censimento-scambi.py --pkhex _notes/fonti/pkhex --check
    python tools/censimento-scambi.py --self-test
"""

import argparse
import io
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATI = os.path.join("PKHeX.Core", "Legality", "Encounters", "Data")
NOMI_EN = os.path.join("PKHeX.Core", "Resources", "text", "other", "en", "text_Species_en.txt")
NOMI_IT = os.path.join("PKHeX.Core", "Resources", "text", "other", "it", "text_Species_it.txt")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "CENSIMENTO-SCAMBI.md")
NORMALIZZATO = os.path.join(RADICE, "pokedex-home-completo", "data", "scambi.csv")

# Le posizioni della specie e del livello dentro la chiamata, per tipo di voce, ricavate dalle
# firme dei costruttori sotto `Legality/Encounters/Templates`. Il valore None dice che il dato non
# sta fra gli argomenti ma fra le proprieta' scritte dopo la graffa, dove si legge per nome.
#
#   EncounterTrade1(names, index, species, version, levelRBY [, levelGSC])
#   EncounterTrade2(names, index, species, level, tid16)
#   EncounterTrade3(names, index, version, pid, species, level)
#   EncounterTrade3XD(species, level, trainer [, nicknames])
#   EncounterTrade4PID(names, index, version, pid, species, level)
#   EncounterTrade4RanchGift(pid, species, met, level) oppure (species, met, level)
#   EncounterTrade8(names, index, version, species, level, memory, arg, feel, intensity)
#   EncounterTrade9(names, index, version, species, level)
#   EncounterTrade9a(names, index, species, form, level)
POSIZIONI = {
    "EncounterTrade1": (2, 4),
    "EncounterTrade2": (2, 3),
    "EncounterTrade3": (4, 5),
    "EncounterTrade3XD": (0, 1),
    "EncounterTrade4PID": (4, 5),
    "EncounterTrade4RanchGift": ("ranch", "ranch"),
    "EncounterTrade5BW": (None, None),
    "EncounterTrade5B2W2": (None, None),
    "EncounterTrade6": (None, None),
    "EncounterTrade7": (None, None),
    "EncounterTrade7b": (None, None),
    # L'ottava generazione ha due costruttori e la fonte li usa entrambi nella medesima tabella:
    # uno prende la tavola dei nomi con l'indice della voce, l'altro prende direttamente i nomi
    # dell'allenatore e non ha indice, quindi la specie scorre di una posizione. Si distinguono
    # contando gli argomenti, ed e' la ragione per cui questa voce e' un dizionario per arieta'
    # invece di una coppia: senza la distinzione sette voci su quattordici uscivano con la specie
    # di un'altra, e il presidio sul commento lo ha rilevato.
    "EncounterTrade8": {9: (3, 4), 8: (2, 3)},
    "EncounterTrade8b": (None, None),
    "EncounterTrade9": (3, 4),
    "EncounterTrade9a": (2, 4),
}

# La generazione di ciascuna cartella della fonte, che e' anche l'ordine in cui il censimento
# presenta i titoli.
GENERAZIONI = ("Gen1", "Gen2", "Gen3", "Gen4", "Gen5", "Gen6", "Gen7", "Gen8", "Gen9")

# Dove la fonte tiene i soprannomi e i nomi di allenatore di questi esemplari, una lista per
# lingua. Il percorso e' relativo al clone e la lingua si aggiunge in coda al nome del file.
ELENCHI = os.path.join("PKHeX.Core", "Resources", "legality")

# Le due dichiarazioni con cui la fonte lega una tavola di nomi al proprio file di stringhe. La
# prima nomina il file, la seconda lega quel nome alla variabile che le voci useranno come primo
# argomento. Si leggono entrambe invece di trascrivere la corrispondenza, per la ragione di
# sempre: una trascrizione di dodici righe e' un difetto che aspetta, e qui sbaglierebbe in modo
# invisibile, perche' un indice letto nella tavola sbagliata restituisce comunque un nome.
RE_COSTANTE = re.compile(r'private const string (\w+)\s*=\s*"([a-z0-9]+)"')
RE_TAVOLA_NOMI = re.compile(r"(?:readonly )?string\[\]\[\] (\w+)\s*=\s*GetLanguageStrings\((\w+)")


# I modelli di incontro, dove la fonte dichiara se un tipo divida il proprio elenco di nomi.
MODELLI = os.path.join("PKHeX.Core", "Legality", "Encounters", "Templates")
# Il segno che un tipo spezza l'elenco. La classe negata non puo' escludere la parentesi,
# perche' la riga vera ne contiene gia' una nel cast: la prima stesura lo faceva e non
# trovava nulla, cioe' dichiarava che nessun tipo spezza.
RE_SPEZZA = re.compile(r"TrainerNames\s*=\s*EncounterUtil\.GetNamesForLanguage\(.*index\s*\+")


def tipi_con_allenatore(pkhex):
    """I tipi di incontro che ricavano il nome dell'allenatore dalla seconda meta' dell'elenco.

    La regola non e' uniforme e assumerla lo e' costa un nome sbagliato su ogni voce di una
    generazione intera. La prima generazione, per esempio, NON la segue: il suo allenatore non e'
    un nome ma un codice di controllo che il gioco rende come la parola allenatore nella propria
    lingua, quindi il suo elenco e' tutto di soprannomi. Applicarvi la meta' produrrebbe, per ogni
    scambio, un soprannome preso dalla posizione sbagliata e un allenatore inventato.

    Si legge percio' dai modelli della fonte quali tipi assegnino il nome dell'allenatore con lo
    scarto, invece di elencarli qui: se un tipo nuovo lo fara', il programma se ne accorgera' da
    se'.
    """
    fuori = set()
    radice = os.path.join(pkhex, MODELLI)
    if not os.path.isdir(radice):
        return fuori
    for cartella, _sub, file_ in os.walk(radice):
        for nome in file_:
            if not nome.endswith(".cs"):
                continue
            testo = io.open(os.path.join(cartella, nome), encoding="utf-8",
                            errors="replace").read()
            if RE_SPEZZA.search(testo):
                fuori.add(nome[:-3])
    return fuori


def tavole_dei_nomi(testo):
    """Dalla variabile della tavola dei nomi al nome del file di stringhe, letti dal sorgente."""
    costanti = dict(RE_COSTANTE.findall(testo))
    fuori = {}
    for variabile, simbolo in RE_TAVOLA_NOMI.findall(testo):
        if simbolo in costanti:
            fuori[variabile] = costanti[simbolo]
    return fuori


def elenco_nomi(pkhex, base, lingua):
    """Una lista di nomi per una tavola e una lingua, indicizzata come la fonte la indicizza.

    Il file vive sotto la cartella della generazione a cui appartiene, e quale sia non e' scritto
    da nessuna parte in modo comodo: si cerca, perche' cercare fra dieci cartelle costa nulla e
    indovinare costa un censimento sbagliato. Se il file manca si restituisce una lista vuota, e
    il censimento lo dichiara invece di lasciare la colonna vuota senza spiegazione: un clone
    sparso puo' non avere le risorse di testo, ed e' precisamente cio' che accadeva a questo
    progetto fino al 2026-09-14.
    """
    nome = "text_" + base + "_" + lingua + ".txt"
    radice = os.path.join(pkhex, ELENCHI)
    if not os.path.isdir(radice):
        return []
    for cartella in sorted(os.listdir(radice)):
        percorso = os.path.join(radice, cartella, nome)
        if not os.path.exists(percorso):
            continue
        grezzo = io.open(percorso, encoding="utf-8-sig").read()
        righe = [r.rstrip("\r") for r in grezzo.split("\n")]
        # Una riga vuota in mezzo e' uno slot e non rumore: significa che quella voce non ha un
        # nome in questa lingua, e scartarla sposterebbe di uno ogni indice successivo, cioe'
        # darebbe il nome sbagliato a ogni voce da li' in avanti senza che nulla protesti.
        # L'elenco giapponese di prima generazione ne ha una alla posizione uno, ed e' il caso
        # su cui questo difetto e' stato trovato il 2026-09-14. Si toglie soltanto l'ultima, e
        # soltanto quando e' l'artefatto di un file che termina con un a capo.
        if grezzo.endswith("\n") and righe and righe[-1] == "":
            righe.pop()
        return righe
    return []

MAX_SPECIE = 1025


def nomi_specie(percorso):
    """I nomi delle specie per numero nazionale, con l'indice zero occupato dalla parola uovo."""
    if not os.path.exists(percorso):
        return None
    righe = io.open(percorso, encoding="utf-8").read().split("\n")
    return [r.strip() for r in righe]


def argomenti(chiamata):
    """Gli argomenti di primo livello di una chiamata, senza entrare nelle parentesi annidate."""
    fuori, corrente, profondita = [], "", 0
    for c in chiamata:
        if c == "(":
            profondita += 1
            if profondita == 1:
                # Alla parentesi che apre la chiamata si butta cio' che la precede, cioe' la parola
                # `new`: senza questo azzeramento il primo argomento uscirebbe attaccato a essa e
                # ogni lettura per posizione sarebbe sfasata di un carattere invece che di un
                # campo, che e' il genere di difetto che non produce un errore ma un numero falso.
                corrente = ""
                continue
        elif c == ")":
            profondita -= 1
            if profondita == 0:
                break
        if profondita == 1 and c == ",":
            fuori.append(corrente.strip())
            corrente = ""
        else:
            corrente += c
    if corrente.strip():
        fuori.append(corrente.strip())
    return fuori


def numero(testo):
    """Un argomento come intero, se lo e': accetta il decimale con gli zeri davanti e l'esadecimale."""
    testo = testo.strip()
    if re.fullmatch(r"0[xX][0-9a-fA-F]+", testo):
        return int(testo, 16)
    if re.fullmatch(r"\d+", testo):
        return int(testo)
    return None


def proprieta(voce):
    """Le proprieta' scritte fra graffe dopo la chiamata, come dizionario di stringhe.

    La virgola separa due proprieta' soltanto fuori dalle parentesi, e la prima stesura non lo
    distingueva: un valore come `IVs = new(20,15,17,24,23,22)` usciva troncato a `new(20`, cioe'
    plausibile e sbagliato. Il difetto e' rimasto invisibile finche' il censimento ha usato le
    sole proprieta' semplici; e' emerso il 2026-09-14, quando il generatore degli scambi ha
    avuto bisogno proprio dei valori individuali. La forma con le parentesi si riconosce quindi
    per prima, cosicche' cio' che sta dentro non venga spezzato.
    """
    m = re.search(r"\{(.*)\}", voce, re.S)
    if not m:
        return {}
    fuori = {}
    for coppia in re.finditer(r"(\w+)\s*=\s*(\w*\s*\([^()]*\)|[^,{}]+)", m.group(1)):
        fuori[coppia.group(1)] = coppia.group(2).strip()
    return fuori


def tabelle(testo):
    """Le tabelle di scambi di un file, come terne fra tipo, nome e voci grezze.

    Il ritaglio tollera un commento fra il segno di uguale e la parentesi quadra, che nella fonte
    compare su almeno una tabella e che una lettura ingenua farebbe perdere in silenzio.
    """
    fuori = []
    for m in re.finditer(r"readonly\s+(\w*Trade\w*)\[\]\s+(\w+)\s*=\s*(?://[^\n]*\n\s*)?\[(.*?)\n\s*\];",
                         testo, re.S):
        tipo, nome, corpo = m.group(1), m.group(2), m.group(3)
        voci = []
        for riga in corpo.split("\n"):
            riga = riga.strip()
            if riga.startswith("new("):
                voci.append(riga)
        if voci:
            fuori.append((tipo, nome, voci))
    return fuori


def leggi_voce(tipo, riga, nomi_en, tavole=None, elenchi=None, spezza=False, meta=None):
    """Una voce di tabella come dizionario, con la discordanza dichiarata se il commento smentisce.

    Le due tavole facoltative servono al soprannome. `tavole` lega la variabile che la voce passa
    come primo argomento al nome del file di stringhe, e `elenchi` porta quelle stringhe gia'
    lette per lingua. Sono facoltative perche' non tutte le generazioni passano una tavola di
    nomi, e dove non la passano la colonna resta vuota invece di essere inventata.
    """
    args = argomenti(riga)
    props = proprieta(riga)
    commento = ""
    m = re.search(r"//\s*(.*)$", riga)
    if m:
        commento = m.group(1).strip()

    dichiarate = POSIZIONI.get(tipo, (None, None))
    if isinstance(dichiarate, dict):
        dichiarate = dichiarate.get(len(args), (None, None))
    pos_specie, pos_livello = dichiarate
    specie = livello = None
    if pos_specie == "ranch":
        # I due costruttori del ranch differiscono per il valore di personalita' iniziale, e si
        # distinguono contando gli argomenti invece che indovinando.
        numeri = [numero(a) for a in args]
        numeri = [n for n in numeri if n is not None]
        if len(numeri) >= 4:
            specie, livello = numeri[1], numeri[3]
        elif len(numeri) == 3:
            specie, livello = numeri[0], numeri[2]
    else:
        if pos_specie is not None and pos_specie < len(args):
            specie = numero(args[pos_specie])
        if pos_livello is not None and pos_livello < len(args):
            livello = numero(args[pos_livello])
    if specie is None and "Species" in props:
        specie = numero(props["Species"])
    if livello is None and "Level" in props:
        livello = numero(props["Level"])

    pid = None
    for chiave in ("PID",):
        if chiave in props:
            pid = props[chiave]
    if pid is None:
        for a in args:
            if re.fullmatch(r"0[xX][0-9a-fA-F]{6,8}", a.strip()):
                pid = a.strip()
                break

    identificativo = ""
    for chiave in ("ID32", "TID16"):
        if chiave in props:
            identificativo = props[chiave]
            break

    discordanza = ""
    if specie is not None and nomi_en and 0 < specie < len(nomi_en) and commento:
        # L'apostrofo va normalizzato prima del confronto: la tavola dei nomi scrive Farfetch con
        # l'apostrofo tipografico e i commenti della fonte con quello dritto, e senza questa
        # normalizzazione due scritture della stessa specie risultano discordanti.
        def piano(s):
            return s.lower().replace(u"’", "'").replace(u"ʼ", "'")

        atteso = nomi_en[specie]
        # Il commento apre col nome della specie ricevuta, seguito da un separatore: basta quindi
        # controllare che il nome atteso compaia, non che il commento sia uguale a esso.
        if atteso and piano(atteso) not in piano(commento):
            discordanza = "il commento dice %r e il numero %d vale %s" % (commento[:60], specie, atteso)
    # Il soprannome, quando la voce lo prende da una tavola di nomi. Il primo argomento e' la
    # variabile della tavola e il secondo l'indice dentro di essa: si leggono entrambi dalla riga
    # invece di dedurli dal tipo, perche' una generazione che cambi costruttore non deve poter
    # spostare in silenzio la colonna. Se l'indice esce dall'elenco non si prende il nome
    # sbagliato: si dichiara che manca.
    # Un solo elenco per lingua contiene due cose, e la fonte lo dice nel costruttore invece che
    # in un commento: i soprannomi stanno nella prima meta' e i nomi di allenatore nella seconda,
    # e il nome dell'allenatore di una voce sta all'indice della voce piu' meta' della lunghezza.
    # La meta' si calcola quindi dall'elenco e non si trascrive, perche' cambia da una coppia di
    # titoli all'altra: quattordici voci per una, ventiquattro per l'altra.
    soprannomi = {}
    allenatori = {}
    mancanti = []
    trovato = False
    if tavole and elenchi and len(args) >= 2:
        variabile = args[0].strip()
        base = tavole.get(variabile)
        indice = numero(args[1])
        if base is not None and indice is not None:
            # Lo scarto si calcola sulla lunghezza dell'elenco GIAPPONESE e non su quella di
            # ciascuna lingua, perche' e' cosi' che la fonte lo calcola: un elenco piu' corto in
            # una lingua darebbe altrimenti una meta' diversa e un allenatore sbagliato.
            scarto = meta if (spezza and meta) else 0
            for lingua, per_base in elenchi.items():
                elenco = per_base.get(base) or []
                if 0 <= indice < len(elenco):
                    # Una casella vuota e' una risposta e non un'assenza: quella voce non ha un
                    # nome in questa lingua, e dirlo vale piu' che lasciare la colonna muta.
                    if elenco[indice] != "":
                        soprannomi[lingua] = elenco[indice]
                    trovato = True
                    if scarto and indice + scarto < len(elenco):
                        nome_ot = elenco[indice + scarto]
                        if nome_ot != "":
                            allenatori[lingua] = nome_ot
                elif elenco:
                    mancanti.append(lingua)
            # Un indice fuori dall'elenco di una lingua e dentro quello di un'altra non e' un
            # difetto ma un fatto sul gioco, e confonderli produrrebbe un allarme su ogni voce
            # esclusiva di una edizione. Gli elenchi occidentali di prima generazione hanno
            # sedici voci e quello giapponese ventisei, perche' gli scambi del Blu giapponese e
            # uno dei due Nidoran esistono soltanto la': per quelli il soprannome italiano non
            # manca, non esiste. Si dichiara difetto soltanto un indice fuori da ogni elenco,
            # che vorrebbe dire tavola sbagliata o tabella cambiata a monte.
            if mancanti and not trovato:
                discordanza = discordanza or (
                    "indice %d fuori da ogni elenco di %s" % (indice, base))
            elif mancanti:
                soprannomi["_solo"] = ",".join(sorted(soprannomi))

    return {
        "specie": specie,
        "livello": livello,
        "pid": pid or "",
        "identificativo": identificativo,
        "forma": props.get("Form", ""),
        "luogo": props.get("Location", ""),
        "commento": commento,
        "discordanza": discordanza,
        "soprannomi": soprannomi,
        "allenatori": allenatori,
        "proprieta": props,
        # La riga grezza resta accanto ai campi estratti, perche' un consumatore puo' avere
        # bisogno di un argomento che questo censimento non interpreta: il generatore degli
        # scambi, per esempio, ne ricava la sigla della versione. Conservarla costa nulla ed
        # evita che chi la vuole rilegga il file per conto proprio, cioe' che esistano due
        # letture della stessa tabella.
        "riga": riga,
    }


def censisci(pkhex, nomi_en, lingue=("it", "en", "ja")):
    """Tutte le tabelle di scambio della fonte, in ordine di generazione."""
    fuori = []
    cache = {}
    spezzano = tipi_con_allenatore(pkhex)

    def elenchi_per(testo):
        """Gli elenchi di nomi che servono a un file, letti una volta sola per file di stringhe."""
        tavole = tavole_dei_nomi(testo)
        per_lingua = {}
        for lingua in lingue:
            per_base = {}
            for base in set(tavole.values()):
                if (base, lingua) not in cache:
                    cache[(base, lingua)] = elenco_nomi(pkhex, base, lingua)
                per_base[base] = cache[(base, lingua)]
            per_lingua[lingua] = per_base
        return tavole, per_lingua
    base = os.path.join(pkhex, DATI)
    if not os.path.isdir(base):
        return None
    for gen in GENERAZIONI:
        cartella = os.path.join(base, gen)
        if not os.path.isdir(cartella):
            continue
        for nome_file in sorted(os.listdir(cartella)):
            if not nome_file.endswith(".cs"):
                continue
            testo = io.open(os.path.join(cartella, nome_file), encoding="utf-8",
                            errors="replace").read()
            tavole, elenchi = elenchi_per(testo)
            for tipo, nome, righe in tabelle(testo):
                spezza = tipo in spezzano
                meta = None
                if spezza:
                    # Il nome della variabile non e' indifferente: chiamarla `base` ombreggiava
                    # il percorso della cartella dei dati, e dalla prima tabella che spezza in
                    # avanti ogni generazione successiva risultava inesistente. Il censimento
                    # scendeva da trentadue tabelle a quattro senza alcun errore.
                    for elenco_base in set(tavole.values()):
                        ja = (elenchi.get("ja") or {}).get(elenco_base) or []
                        if ja:
                            meta = len(ja) // 2
                voci = [leggi_voce(tipo, r, nomi_en, tavole, elenchi, spezza, meta)
                        for r in righe]
                fuori.append({
                    "generazione": gen.replace("Gen", ""),
                    "file": nome_file,
                    "tipo": tipo,
                    "tabella": nome,
                    "voci": voci,
                    "ignoto": tipo not in POSIZIONI,
                })
    return fuori


def chiave(v):
    """L'identita' di una voce ai fini della deduplicazione, dichiarata invece che implicita."""
    return (v["specie"], v["livello"], v["identificativo"], v["forma"])


def componi(tabelle_lette, nomi_it):
    r = ["# Censimento degli scambi in gioco, tutte le generazioni", ""]
    r.append("> Documento generato da `tools/censimento-scambi.py` dalle tabelle del verificatore. Non si modifica a mano: si rigenera. Enumera la classe degli esemplari consegnati da un personaggio in cambio di un altro, che portano allenatore e soprannome altrui e non sono riproducibili da una cattura propria.")
    r.append("")
    totale = sum(len(t["voci"]) for t in tabelle_lette)
    distinte = len({chiave(v) for t in tabelle_lette for v in t["voci"]})
    con_pid = sum(1 for t in tabelle_lette for v in t["voci"] if v["pid"])
    specie = {v["specie"] for t in tabelle_lette for v in t["voci"] if v["specie"]}
    r.append("Le voci di tabella sono %d e quelle distinte %d, su %d specie diverse. I due numeri differiscono perche' le tabelle di una coppia di titoli si sovrappongono per costruzione: c'e' una tabella comune e accanto una tabella per versione, e la stessa voce compare in entrambe. Due voci sono contate come una quando concordano su specie, livello, identificativo dell'allenatore e forma."
             % (totale, distinte, len(specie)))
    r.append("")
    r.append("Di %d voci la fonte scrive il valore di personalita', quindi quegli esemplari sono riproducibili byte per byte senza alcuna ricerca di semi. Sulle altre la fedelta' va discussa come per le altre classi, perche' il valore lo genera il gioco al momento della consegna."
             % con_pid)
    r.append("")
    discordanze = [(t, v) for t in tabelle_lette for v in t["voci"] if v["discordanza"]]
    ignote = [t for t in tabelle_lette if t["ignoto"]]
    r.append("Controlli: %s %s"
             % ("nessuna voce discorda dal commento che la fonte le scrive accanto."
                if not discordanze else
                "%d voci discordano dal commento e sono elencate in coda; il censimento non va usato come misura finche' non sono risolte." % len(discordanze),
                "Tutti i tipi di voce hanno le posizioni dichiarate."
                if not ignote else
                "ATTENZIONE: %d tabelle hanno un tipo che questo programma non conosce, e le loro voci sono lette solo dalle proprieta'." % len(ignote)))
    r.append("")

    for gen in GENERAZIONI:
        sigla = gen.replace("Gen", "")
        gruppo = [t for t in tabelle_lette if t["generazione"] == sigla]
        if not gruppo:
            continue
        r.append("## Generazione %s" % sigla)
        r.append("")
        for t in gruppo:
            r.append("### %s, da `%s`" % (t["tabella"], t["file"]))
            r.append("")
            r.append("Tipo di voce `%s`, %d voci." % (t["tipo"], len(t["voci"])))
            r.append("")
            r.append("| Specie | Dex | Livello | Soprannome IT | Allenatore IT | Soprannome JA | Valore di personalita | Identificativo | Nota della fonte |")
            r.append("|---|---|---|---|---|---|---|---|---|")
            for v in t["voci"]:
                nome = "?"
                if v["specie"] and nomi_it and v["specie"] < len(nomi_it):
                    nome = nomi_it[v["specie"]]
                sn = v.get("soprannomi") or {}
                al = v.get("allenatori") or {}
                r.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |"
                         % (nome,
                            v["specie"] if v["specie"] is not None else "?",
                            v["livello"] if v["livello"] is not None else "?",
                            (sn.get("it") or "-").replace("|", "/"),
                            (al.get("it") or "-").replace("|", "/"),
                            (sn.get("ja") or "-").replace("|", "/"),
                            v["pid"] or "-",
                            v["identificativo"] or "-",
                            (v["commento"] or "-").replace("|", "/")[:120]))
            r.append("")

    if discordanze:
        r.append("## Discordanze fra numero e commento")
        r.append("")
        r.append("| Tabella | Discordanza |")
        r.append("|---|---|")
        for t, v in discordanze:
            r.append("| %s | %s |" % (t["tabella"], v["discordanza"].replace("|", "/")))
        r.append("")
    return "\n".join(r) + "\n"


def normalizza(tabelle_lette, nomi_it):
    # Le due colonne dei soprannomi stanno anche qui e non solo nel documento, perche' i due file
    # escono dallo stesso strumento e nascono per essere confrontati: una tabella che portasse
    # meno campi del documento farebbe fallire in silenzio proprio i confronti per cui esiste.
    r = ["generazione,tabella,tipo,dex,specie,livello,soprannome_it,allenatore_it,"
         "soprannome_ja,allenatore_ja,pid,identificativo,forma,luogo,nota"]
    for t in tabelle_lette:
        for v in t["voci"]:
            nome = nomi_it[v["specie"]] if (v["specie"] and nomi_it and v["specie"] < len(nomi_it)) else ""
            sn = v.get("soprannomi") or {}
            campi = [t["generazione"], t["tabella"], t["tipo"],
                     str(v["specie"] if v["specie"] is not None else ""), nome,
                     str(v["livello"] if v["livello"] is not None else ""),
                     sn.get("it") or "", (v.get("allenatori") or {}).get("it") or "",
                     sn.get("ja") or "", (v.get("allenatori") or {}).get("ja") or "",
                     v["pid"], v["identificativo"], v["forma"], v["luogo"], v["commento"]]
            r.append(",".join('"%s"' % c.replace('"', '""') if ("," in c or '"' in c) else c
                              for c in campi))
    return "\n".join(r) + "\n"


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("gli argomenti non entrano nelle parentesi annidate",
          ["TradeNames", "00", "RS", "0x00009C40", "296", "05"],
          argomenti("new(TradeNames, 00, RS, 0x00009C40, 296, 05) { IVs = new(5,5,4,4,4,4) }"))
    prova("un numero decimale con gli zeri davanti", 5, numero("05"))
    # Il difetto del 2026-09-14: la virgola separa due proprieta' solo fuori dalle parentesi.
    prova("una proprieta' con le parentesi non si spezza sulla virgola interna",
          "new(20,15,17,24,23,22)",
          proprieta("new(x) { IVs = new(20,15,17,24,23,22), Gender = 0 }").get("IVs"))
    prova("la proprieta' che segue quella con le parentesi si legge comunque",
          "0", proprieta("new(x) { IVs = new(20,15,17,24,23,22), Gender = 0 }").get("Gender"))
    prova("un numero esadecimale", 0x8E, numero("0x0000008E"))
    prova("un argomento che non e' un numero", None, numero("TradeNames"))

    props = proprieta("new(TradeNames, 00, SV, 0194, 18) { ID32 = 033081, Nature = Nature.Relaxed }")
    prova("le proprieta' si leggono per nome", "033081", props.get("ID32"))
    prova("e i valori con il punto restano interi", "Nature.Relaxed", props.get("Nature"))

    nomi = [""] * 1026
    nomi[296], nomi[194], nomi[63] = "Makuhita", "Wooper", "Abra"

    # Terza generazione: la specie sta in quarta posizione e il livello in quinta.
    v = leggi_voce("EncounterTrade3",
                   "new(TradeNames, 00, RS, 0x00009C40, 296, 05) { TID16 = 49562 }, // Makuhita",
                   nomi)
    prova("la specie di terza generazione", 296, v["specie"])
    prova("il livello di terza generazione", 5, v["livello"])
    prova("il valore di personalita' viene riconosciuto", "0x00009C40", v["pid"])
    prova("l'identificativo viene riconosciuto", "49562", v["identificativo"])
    prova("e non c'e' discordanza", "", v["discordanza"])

    # Nona generazione: la specie sta in terza posizione, e il commento la conferma.
    v = leggi_voce("EncounterTrade9",
                   "new(TradeNames, 00, SV, 0194, 18) { ID32 = 033081 }, // Wooper", nomi)
    prova("la specie di nona generazione", 194, v["specie"])
    prova("il livello di nona generazione", 18, v["livello"])

    # Controllo negativo: se il numero e il commento dicono due specie diverse, si dichiara.
    v = leggi_voce("EncounterTrade9",
                   "new(TradeNames, 00, SV, 0194, 18) { ID32 = 033081 }, // Abra", nomi)
    prova("la discordanza viene dichiarata", True, v["discordanza"] != "")

    # Quinta generazione: specie e livello stanno fra le proprieta' e non fra gli argomenti.
    v = leggi_voce("EncounterTrade5B2W2",
                   "new(TradeNames, 00, B2  ) { Species = 296, Level = 20, ID32 = 65217 },", nomi)
    prova("la specie dalle proprieta'", 296, v["specie"])
    prova("il livello dalle proprieta'", 20, v["livello"])

    # L'ottava generazione usa due costruttori nella stessa tabella, e la specie scorre di una
    # posizione fra l'uno e l'altro: e' il difetto che il presidio sul commento ha rilevato, e
    # queste due prove lo tengono chiuso.
    nomi[52], nomi[110] = "Meowth", "Weezing"
    v = leggi_voce("EncounterTrade8",
                   "new(TradeNames, 00, SWSH, 052,18,08,000,04,5) { ID32 = 263455 }, // Meowth",
                   nomi)
    prova("l'ottava con indice", 52, v["specie"])
    prova("e il suo livello", 18, v["livello"])
    v = leggi_voce("EncounterTrade8",
                   "new(TradeOT_R1, SWSH, 110,15,01,040,12,2) { ID32 = 101141 }, // Weezing", nomi)
    prova("l'ottava senza indice", 110, v["specie"])
    prova("e il suo livello", 15, v["livello"])

    # L'apostrofo tipografico della tavola dei nomi non deve produrre una falsa discordanza.
    nomi[83] = u"Farfetch’d"
    v = leggi_voce("EncounterTrade2",
                   "new(TradeNames, 5, 083, 02, 15616) { Gender = 0 }, // Farfetch'd", nomi)
    prova("l'apostrofo non produce discordanza", "", v["discordanza"])

    # I due costruttori del ranch si distinguono contando gli argomenti.
    v = leggi_voce("EncounterTrade4RanchGift",
                   "new(323975838, 025, 18, 20) { Location = 0068 }, // Pikachu", nomi)
    prova("il ranch con il valore di personalita'", 25, v["specie"])
    prova("e il suo livello", 20, v["livello"])
    v = leggi_voce("EncounterTrade4RanchGift", "new(025, 18, 20) { Location = 0068 }, // Pikachu",
                   nomi)
    prova("il ranch senza il valore di personalita'", 25, v["specie"])
    prova("e il suo livello", 20, v["livello"])

    # Il ritaglio delle tabelle tollera un commento fra l'uguale e la parentesi quadra: senza
    # questa tolleranza la tabella della settima generazione veniva perduta in silenzio.
    testo = ("    internal static readonly EncounterTrade7[] TradeGift_SM = // @ a\\1\\5\\5\n"
             "    [\n"
             "        new(TradeNames, 00, SM) { Species = 066, Level = 09 }, // Machop\n"
             "    ];\n")
    trovate = tabelle(testo)
    prova("la tabella col commento viene trovata", 1, len(trovate))
    prova("e porta la sua voce", 1, len(trovate[0][2]))

    prova("la chiave di deduplicazione", (296, 5, "49562", ""),
          chiave({"specie": 296, "livello": 5, "identificativo": "49562", "forma": ""}))


    # -- i soprannomi per lingua, aggiunti il 2026-09-14 ---------------------------------------
    sorgente_finta = (
        '    private const string tradeFinto = "tradefinto";\n'
        '    private static readonly string[][] TradeNames = GetLanguageStrings(tradeFinto, 7);\n')
    tav = tavole_dei_nomi(sorgente_finta)
    prova("la tavola dei nomi si lega al proprio file leggendo il sorgente",
          {"TradeNames": "tradefinto"}, tav)
    prova("negativo: una tavola senza costante dichiarata non si inventa",
          {}, tavole_dei_nomi("string[][] X = GetLanguageStrings(ignoto, 7);"))

    # La regola della meta': la prima parte dell'elenco sono i soprannomi, la seconda i nomi di
    # allenatore, e il nome della voce i sta a i piu' meta' lunghezza.
    meta_finti = {"it": {"tf": ["NICK1", "NICK2", "OT1", "OT2"]}}
    tav_meta = {"TradeNames": "tf"}
    vm = leggi_voce("EncounterTrade3", "new(TradeNames, 01, 122, RB, 06)", [], tav_meta,
                    meta_finti, spezza=True, meta=2)
    prova("il nome dell'allenatore sta a indice piu' meta' lunghezza dell'elenco",
          ("NICK2", "OT2"), (vm["soprannomi"].get("it"), vm["allenatori"].get("it")))
    meta_coda = {"it": {"tf": ["NICK1", "NICK2", "OT1", "OT2", ""]}}
    vc = leggi_voce("EncounterTrade3", "new(TradeNames, 00, 122, RB, 06)", [], tav_meta,
                    meta_coda, spezza=True, meta=2)
    prova("negativo: una riga vuota in coda non sposta la meta' e non falsa l'allenatore",
          ("NICK1", "OT1"), (vc["soprannomi"].get("it"), vc["allenatori"].get("it")))
    # Il difetto che il collaudo ha colto il 2026-09-14: la regola della meta' non e' universale.
    # La prima generazione non la segue, perche' il suo allenatore e' un codice di controllo e
    # non un nome, e applicargliela darebbe un allenatore inventato su ogni voce.
    v1 = leggi_voce("EncounterTrade1", "new(TradeNames, 00, 122, RB, 06)", [], tav_meta,
                    meta_finti, spezza=False, meta=None)
    prova("negativo: un tipo che non spezza l'elenco non produce alcun allenatore",
          ("NICK1", {}), (v1["soprannomi"].get("it"), v1["allenatori"]))

    elenchi_finti = {"it": {"tradefinto": ["ALFA", "BETA"]},
                     "ja": {"tradefinto": [u"\u30a2", u"\u30d9", u"\u30ac"]}}
    riga = "new(TradeNames, 01, 122, RB, 06, 05), // Mr. Mime - Abra"
    v = leggi_voce("EncounterTrade1", riga, [], tav, elenchi_finti)
    prova("il soprannome si prende dall'indice della voce e non dalla sua posizione",
          ("BETA", u"\u30d9"), (v["soprannomi"].get("it"), v["soprannomi"].get("ja")))

    # Il caso che ha fatto sbagliare la prima stesura: un indice dentro l'elenco giapponese e
    # fuori da quello italiano non e' un difetto, e' uno scambio che esiste solo in Giappone.
    riga_jp = "new(TradeNames, 02, 032, BU, 02), // Nidoran - solo giapponese"
    vj = leggi_voce("EncounterTrade1", riga_jp, [], tav, elenchi_finti)
    prova("negativo: un indice fuori dal solo elenco italiano non e' una discordanza",
          ("", None, u"\u30ac"),
          (vj["discordanza"], vj["soprannomi"].get("it"), vj["soprannomi"].get("ja")))

    riga_rotta = "new(TradeNames, 99, 122, RB, 06), // fuori da ogni elenco"
    vr = leggi_voce("EncounterTrade1", riga_rotta, [], tav, elenchi_finti)
    prova("un indice fuori da OGNI elenco si dichiara, perche' vuol dire tavola sbagliata",
          True, "fuori da ogni elenco" in vr["discordanza"])

    prova("negativo: senza le tavole la colonna resta vuota invece di essere inventata",
          {}, leggi_voce("EncounterTrade1", riga, [])["soprannomi"])

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "pkhex"),
                    help="il clone del verificatore da cui leggere le tabelle")
    ap.add_argument("--check", action="store_true",
                    help="non scrive: dice soltanto se i documenti sul disco siano allineati")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    pkhex = a.pkhex if os.path.isabs(a.pkhex) else os.path.join(RADICE, a.pkhex)
    nomi_en = nomi_specie(os.path.join(pkhex, NOMI_EN))
    nomi_it = nomi_specie(os.path.join(pkhex, NOMI_IT))
    if nomi_en is None or nomi_it is None:
        print("rifiutato: mancano i nomi delle specie sotto " + pkhex)
        return 1
    lette = censisci(pkhex, nomi_en)
    if lette is None:
        print("rifiutato: manca la cartella delle tabelle sotto " + pkhex)
        return 1

    testo = componi(lette, nomi_it)
    csv = normalizza(lette, nomi_it)
    if a.check:
        disallineati = [p for p, atteso in ((USCITA, testo), (NORMALIZZATO, csv))
                        if (io.open(p, encoding="utf-8").read() if os.path.exists(p) else "") != atteso]
        for p in disallineati:
            print("disallineato: %s va rigenerato" % p)
        if disallineati:
            return 1
        print("allineati: %s e %s" % (USCITA, NORMALIZZATO))
        return 0

    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    io.open(NORMALIZZATO, "w", encoding="utf-8", newline="\n").write(csv)
    totale = sum(len(t["voci"]) for t in lette)
    distinte = len({chiave(v) for t in lette for v in t["voci"]})
    con_pid = sum(1 for t in lette for v in t["voci"] if v["pid"])
    discordanze = [v for t in lette for v in t["voci"] if v["discordanza"]]
    print("scritti %s e %s" % (USCITA, NORMALIZZATO))
    print("  tabelle %d | voci %d | distinte %d | con valore di personalita' %d"
          % (len(lette), totale, distinte, con_pid))
    for t in lette:
        if t["ignoto"]:
            print("  TIPO IGNOTO: %s in %s" % (t["tipo"], t["file"]))
    for v in discordanze:
        print("  DISCORDANZA: " + v["discordanza"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
