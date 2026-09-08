#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone gli esemplari di terza generazione che i biglietti sbloccavano, e non consegnavano.

Perche' esiste, e perche' e' un programma diverso dagli altri
------------------------------------------------------------
Ogni generatore prodotto finora parte da una consegna: una carta, un dono, un record di
archivio che porta gia' dentro di se' l'esemplare o il suo modello. Queste dieci voci non
hanno nulla del genere, e la ragione sta nella cosa stessa che veniva distribuita. Il
biglietto non consegnava un Pokemon: consegnava un oggetto, e l'oggetto sbloccava una nave
per un'isola dove il Pokemon andava cercato, indebolito e catturato come qualunque altro.

Ne discendono tre conseguenze che nessuna delle classi precedenti aveva, e che vanno enunciate
perche' ciascuna cambia un campo diverso.

L'allenatore non e' il distributore ma il giocatore, e cosi' l'identificativo: l'archivio
enciclopedico li dichiara entrambi con la parola che significa i tuoi. Ne segue che qui va
scritto l'allenatore del progetto, non per ripiego ma per fedelta'.

La sfera non e' quella della consegna ma quella della cattura, cioe' la Poke Ball ordinaria
che il modello del verificatore assegna quando l'incontro non ne fissa una.

E soprattutto il valore di personalita' non e' libero. Un esemplare catturato nasce dal
generatore congruenziale del gioco, e i suoi sei valori individuali non sono indipendenti dal
valore di personalita': provengono dalle due estrazioni immediatamente successive. E' il primo
metodo, ed e' il terzo regime di correlazione che questo progetto incontra, incompatibile con
i due precedenti. Le distribuzioni di terza generazione vogliono la correlazione a seme
ristretto; i doni di quinta vogliono l'assenza di ogni correlazione; questi vogliono il primo
metodo. Un esemplare composto con il regime sbagliato non e' sbagliato in un campo: e'
sbagliato nella relazione fra due campi, che nessuna ispezione del singolo campo rivela.

La forma di Deoxys, e perche' il fatto e' piu' sottile di come lo si racconta
----------------------------------------------------------------------------
Si dice che Deoxys abbia una forma diversa per gioco. La formulazione esatta e' un'altra, e la
differenza decide quanti esemplari servano. In terza generazione la forma non e' un campo
memorizzato: il verificatore la calcola sempre zero per ogni specie tranne Unown, dove discende
dal valore di personalita'. Un file di terza generazione che contiene un Deoxys non porta
dunque alcuna forma. Cio' che decide l'aspetto e' il gioco che apre il file, e i quattro giochi
lo decidono diversamente: le due versioni di apertura mostrano la forma normale, la riedizione
rossa quella d'attacco, la verde quella di difesa, e Smeraldo quella di velocita'.

Le tabelle degli incontri del verificatore registrano quindi tre voci e non quattro, una per
ciascuno dei tre giochi che ospitano l'Isola della Nascita: la forma normale non ha una voce
perche' le due versioni di apertura non ricevettero mai quel biglietto. La quarta forma non e'
per questo irraggiungibile, ed e' l'altra meta' del fatto: dalla quarta generazione in avanti
la forma diventa un campo memorizzato e Deoxys sta nell'elenco delle specie che cambiano forma
liberamente, indipendentemente dalla propria origine. Le quattro caselle si riempiono dunque
con quattro corpi, che questo programma produce come tre piu' uno, e non con quattro biglietti.

Uso
---
    python tools/genera-incontro-gen3.py --elenco
    python tools/genera-incontro-gen3.py --lotto _notes/lotto-incontri-gen3
    python tools/genera-incontro-gen3.py --self-test
"""

import argparse
import hashlib
import importlib.util
import io
import json
import os
import struct
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))

from pokebridge import charmap as cm  # noqa: E402
from pokebridge import gen3  # noqa: E402


def _fratello():
    """Il generatore delle distribuzioni di terza, caricato come modulo nonostante il trattino.

    Non e' un vezzo: quel programma porta gia' l'esperienza per gruppo di crescita, la
    corrispondenza fra numerazione nazionale e identificativo interno, i punti potenza di base,
    i nomi localizzati delle specie e la scrittura delle due forme del file. Riscriverne una
    copia significherebbe avere due verita' su ciascuno di quei dati, e la seconda diverge dalla
    prima senza che nessuno se ne accorga.
    """
    percorso = os.path.join(RADICE, "tools", "genera-evento-gen3.py")
    spec = importlib.util.spec_from_file_location("genera_evento_gen3", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


G3 = None  # si carica in `main`, cosi' che `--self-test` non paghi la lettura del fratello

# ---------------------------------------------------------------------------------------
# Il generatore congruenziale della terza generazione, e il primo metodo.
# ---------------------------------------------------------------------------------------

MOLT = 0x41C64E6D
SOMMA = 0x00006073


def avanza(seme):
    return (seme * MOLT + SOMMA) & 0xFFFFFFFF


def prossimo16(seme):
    seme = avanza(seme)
    return seme, (seme >> 16) & 0xFFFF


def prossimo15(seme):
    seme = avanza(seme)
    return seme, (seme >> 16) & 0x7FFF


def primo_metodo(seme):
    """Il valore di personalita' e i sei valori individuali, dalle quattro estrazioni in fila.

    L'ordine e' quello che il verificatore ricostruisce all'indietro quando giudica: due
    estrazioni a sedici bit compongono il valore di personalita' con la seconda in alto, poi due
    estrazioni a quindici bit compongono la parola dei valori individuali, la prima delle quali
    porta salute, attacco e difesa e la seconda velocita', attacco speciale e difesa speciale.

    Che l'ordine sia questo e non un altro non e' una convenzione scelta da noi: e' la
    condizione perche' l'esemplare sia riconoscibile come catturato. Scambiare le due parole del
    valore di personalita', oppure le due meta' della parola dei valori individuali, produce un
    esemplare i cui campi sono tutti nell'intervallo e la cui relazione reciproca non esiste in
    natura, ed e' precisamente cio' che il verificatore cerca.
    """
    s = seme
    s, basso = prossimo16(s)
    s, alto = prossimo16(s)
    personalita = ((alto << 16) | basso) & 0xFFFFFFFF
    s, iv1 = prossimo15(s)
    s, iv2 = prossimo15(s)
    valori = {
        "hp": iv1 & 0x1F,
        "atk": (iv1 >> 5) & 0x1F,
        "def": (iv1 >> 10) & 0x1F,
        "spd": iv2 & 0x1F,
        "satk": (iv2 >> 5) & 0x1F,
        "sdef": (iv2 >> 10) & 0x1F,
    }
    return personalita, valori, s


def cromatico(personalita, tid, sid):
    return ((personalita >> 16) ^ (personalita & 0xFFFF) ^ tid ^ sid) < 8


# ---------------------------------------------------------------------------------------
# La tavola degli incontri, letta dalle tabelle del verificatore e non da un'enciclopedia.
# ---------------------------------------------------------------------------------------

# Schema: sigla, numero nazionale, livello, sigla di versione, luogo, forma resa dal gioco,
# lingua, e il nome umano del luogo. La forma non e' un campo che si scrive: e' cio' che il
# gioco indicato mostrera' aprendo il file, ed e' qui perche' senza di essa la tavola non
# spiegherebbe perche' esistano tre righe di Deoxys identiche in tutto tranne la versione.
#
# Fonte: PKHeX, `PKHeX.Core/Legality/Encounters/Data/Gen3/Encounters3RSE.cs` righe 109-112 e
# `Encounters3FRLG.cs` righe 61-62, 74 e 86, lette il 2026-09-07.
INCONTRI = [
    ("mew-e", 151, 30, "E", 201, None, "Japanese", "Isola Lontana"),
    ("lugia-e", 249, 70, "E", 211, None, "Italian", "Roccia Ombelico"),
    ("hooh-e", 250, 70, "E", 211, None, "Italian", "Roccia Ombelico"),
    ("lugia-fr", 249, 70, "FR", 174, None, "Italian", "Roccia Ombelico"),
    ("hooh-fr", 250, 70, "FR", 174, None, "Italian", "Roccia Ombelico"),
    ("lugia-lg", 249, 70, "LG", 174, None, "Italian", "Roccia Ombelico"),
    ("hooh-lg", 250, 70, "LG", 174, None, "Italian", "Roccia Ombelico"),
    ("deoxys-e", 386, 30, "E", 200, 3, "Italian", "Isola della Nascita"),
    ("deoxys-fr", 386, 30, "FR", 187, 1, "Italian", "Isola della Nascita"),
    ("deoxys-lg", 386, 30, "LG", 187, 2, "Italian", "Isola della Nascita"),
    # Il Biglietto Eone e l'Isola del Sud, aggiunti il 2026-09-08 su segnalazione dell'utente.
    # La loro asimmetria non e' un capriccio della tavola ed e' l'informazione piu' densa di
    # questo blocco: nelle due versioni di apertura il biglietto consegna il leggendario opposto
    # a quello che vaga per la regione, cioe' Latias in Rubino e Latios in Zaffiro, e l'incontro
    # NON e' fatidico; in Smeraldo sono disponibili entrambi e l'incontro e' fatidico. Ne segue
    # che il contrassegno fatidico qui non e' una proprieta' dell'evento ma della versione, ed e'
    # il solo caso del lotto in cui due esemplari della stessa specie differiscono su quel campo.
    ("latias-r", 380, 50, "R", 73, None, "Italian", "Isola del Sud"),
    ("latios-s", 381, 50, "S", 73, None, "Italian", "Isola del Sud"),
    ("latias-e", 380, 50, "E", 73, None, "Italian", "Isola del Sud"),
    ("latios-e", 381, 50, "E", 73, None, "Italian", "Isola del Sud"),
]

# Il nome dell'allenatore in katakana, per la sola voce giapponese. La traslitterazione e' una
# scelta di questo progetto e va dichiarata come tale: non e' un dato storico, perche' nessun
# dato storico esiste per il nome di un giocatore. La ragione per cui la voce e' giapponese
# invece che italiana e' invece un dato: il biglietto della Vecchia Mappa non usci' mai dal
# Giappone, e il modello del verificatore forza quella lingua sulla sola specie Mew.
NOME_GIAPPONESE = u"アレシオ"

# Il codice di lingua che il byte a 0x12 porta, nella numerazione della terza generazione.
LINGUE = {"Japanese": 1, "English": 2, "French": 3, "Italian": 4, "German": 5, "Spanish": 7}

# I repertori di livello, uno per gioco, dal deposito compilato del verificatore.
REPERTORI = {"E": "lvlmove_e.pkl", "FR": "lvlmove_fr.pkl", "LG": "lvlmove_lg.pkl",
             "R": "lvlmove_rs.pkl", "S": "lvlmove_rs.pkl"}

# Le due voci che il verificatore NON marca come incontro fatidico, cioe' quelle delle due
# versioni di apertura. Sta qui come insieme e non come colonna della tavola perche' e'
# un'eccezione a una regola e non una proprieta' indipendente: tutto il resto del lotto e'
# fatidico, e scrivere una colonna quasi costante nasconde proprio le due righe che contano.
SENZA_INCONTRO_FATIDICO = frozenset(["latias-r", "latios-s"])

CARTELLA_REPERTORI = os.path.join("PKHeX.Core", "Resources", "byte", "levelup")
CARTELLA_INDOLI = os.path.join("PKHeX.Core", "Resources", "byte", "personal")

# La chiave con cui si derivano i semi. Il seme non e' casuale e non e' scelto a mano: discende
# da una chiave stabile, cosicche' due corse dello stesso programma producano gli stessi
# esemplari e la differenza fra due lotti sia sempre imputabile a una modifica del programma e
# mai al caso.
SALE = "INC-3|2026-09-07"


def seme_della_voce(sigla, tid, sid, giro):
    chiave = "%s|%s|%d|%d|%d" % (SALE, sigla, tid, sid, giro)
    return struct.unpack("<I", hashlib.sha256(chiave.encode("utf-8")).digest()[:4])[0]


# ---------------------------------------------------------------------------------------
# La lettura dei due depositi compilati.
# ---------------------------------------------------------------------------------------

def aree_indicizzate(dati):
    """Le aree di un archivio con la tavola delle posizioni a sedici bit.

    Due byte di firma, il conto delle voci, poi una posizione per voce, dove la fine di
    un'area coincide con l'inizio della successiva: la coppia si legge come un intero doppio.
    """
    quante = struct.unpack_from("<H", dati, 2)[0]
    fuori = []
    for i in range(quante):
        coppia = struct.unpack_from("<I", dati, 4 + i * 2)[0]
        inizio, fine = coppia & 0xFFFF, coppia >> 16
        fuori.append(dati[inizio:fine])
    return fuori


def repertorio_di_livello(area):
    """Le coppie di mossa e livello di una specie: prima tutte le mosse, poi tutti i livelli."""
    n = len(area) // 3
    mosse = [struct.unpack_from("<H", area, 2 * i)[0] for i in range(n)]
    livelli = list(area[2 * n:3 * n])
    return list(zip(mosse, livelli))


def mosse_al_livello(coppie, livello):
    """Le ultime quattro mosse imparate entro un livello, che e' cio' che il gioco assegna.

    Il gioco insegna in ordine e scarta la piu' vecchia quando le quattro caselle sono piene,
    quindi il risultato e' la coda dell'elenco filtrato e non la sua testa. Le mosse ripetute
    non si accumulano: una specie che reimpari una mossa gia' nota non ne occupa due caselle.
    """
    imparate = []
    for mossa, liv in coppie:
        if liv > livello:
            continue
        if mossa in imparate:
            imparate.remove(mossa)
        imparate.append(mossa)
    return imparate[-4:]


def nome_allenatore(tabella, nome, lingua):
    """Il campo del nome dell'allenatore, che non si riempie allo stesso modo nelle due lingue.

    Il campo misura sette byte e il verificatore non lo legge come una stringa ma come una
    impronta di riempimento, perche' il gioco lo copia dal salvataggio byte per byte e quindi la
    spazzatura che vi resta dietro e' essa stessa un dato. La regola che esso applica sta in
    `MiscVerifierG3.VerifyTrashJPN` e in `VerifyTrashINT`, ed e' diversa per le due lingue.

    Su un gioco internazionale tutti e sette i byte sono inizializzati al terminatore, quindi un
    nome che li riempia tutti e' lecito senza terminatore finale: e' il caso del nostro
    allenatore, il cui nome misura esattamente sette caratteri.

    Su un gioco giapponese sono inizializzati al terminatore i soli primi sei, e il settimo
    resta a zero. Ne segue che un nome giapponese va scritto in sei byte con il riempimento a
    terminatore, e il settimo byte deve valere zero. Scriverlo a terminatore come gli altri
    produce l'unico rilievo che il primo giudizio di questo lotto ha portato, cioe' che manca il
    terminatore finale, ed e' un difetto che nessun controllo interno poteva cogliere perche' i
    byte sono tutti leciti e la stringa si rilegge correttamente in entrambi i casi.
    """
    if lingua != "Japanese":
        return tabella.encode(nome, length=gen3.OT_NAME_LENGTH)
    return tabella.encode(nome, length=gen3.OT_NAME_LENGTH - 1) + b"\x00"


def indole_di_specie(pkhex, nazionale):
    """Amicizia di base e le due caselle di abilita', dal deposito delle indoli di Smeraldo.

    Si legge da Smeraldo perche' e' cio' che il modello del verificatore fa per tutti e cinque i
    giochi di terza generazione, e non perche' i quattro depositi coincidano: la scelta e' del
    verificatore e va copiata, non ricalcolata su una fonte diversa.
    """
    percorso = os.path.join(pkhex, CARTELLA_INDOLI, "personal_e")
    dati = io.open(percorso, "rb").read()
    passo = 0x1C
    blocco = dati[nazionale * passo:(nazionale + 1) * passo]
    if len(blocco) < passo:
        raise KeyError("numero nazionale fuori dal deposito delle indoli: %d" % nazionale)
    return {"amicizia": blocco[0x12], "rapporto_sessi": blocco[0x10],
            "abilita": (blocco[0x16], blocco[0x17])}


# ---------------------------------------------------------------------------------------
# La composizione.
# ---------------------------------------------------------------------------------------

def componi(ace, pkhex, voce, allenatore, giro=0):
    sigla, nazionale, livello, versione, luogo, forma, lingua, nome_luogo = voce
    fatidico = sigla not in SENZA_INCONTRO_FATIDICO

    mappa = G3.nazionale_verso_interno(ace)
    specie_id = mappa.get(nazionale)
    if specie_id is None:
        raise KeyError("nessun identificativo interno per il numero nazionale %d" % nazionale)

    gruppo = G3.gruppo_di_crescita(ace).get(specie_id)
    if gruppo is None:
        raise KeyError("gruppo di crescita ignoto per la specie interna %d" % specie_id)

    indole = indole_di_specie(pkhex, nazionale)

    # Il seme. Le quattro specie sono tutte asessuate e tutte a una sola abilita', quindi
    # nessun vincolo di sesso o di abilita' scarta semi: il primo seme derivato e' buono, e il
    # parametro del giro esiste soltanto perche' un vincolo futuro possa entrare senza cambiare
    # la forma del programma.
    seme = seme_della_voce(sigla, allenatore["identificativo"], allenatore["segreto"], giro)
    personalita, iv, _ = primo_metodo(seme)

    tabella = cm.Charmap.gen3_per_lingua(lingua)
    nomi = G3.nomi_specie_per_lingua(ace, lingua)
    nome_visibile = nomi.get(specie_id, "")
    if not nome_visibile:
        raise KeyError("nome di specie assente per l'identificativo interno %d in %s"
                       % (specie_id, lingua))
    if lingua != "Japanese":
        nome_visibile = nome_visibile.upper()
    soprannome = tabella.encode(nome_visibile, length=gen3.NICKNAME_LENGTH)

    nome_ot = NOME_GIAPPONESE if lingua == "Japanese" else allenatore["nome"]
    ot_bytes = nome_allenatore(tabella, nome_ot, lingua)

    grezzo = io.open(os.path.join(pkhex, CARTELLA_REPERTORI, REPERTORI[versione]), "rb").read()
    coppie = repertorio_di_livello(aree_indicizzate(grezzo)[nazionale])
    mosse = mosse_al_livello(coppie, livello)
    pp_base = G3.punti_potenza(ace)
    pp = [pp_base.get(m, 0) for m in mosse]

    prima, seconda = indole["abilita"]
    bit = 0 if prima == seconda else (personalita & 1)

    mon = gen3.Gen3Mon(
        personality=personalita,
        ot_id=((allenatore["segreto"] & 0xFFFF) << 16) | (allenatore["identificativo"] & 0xFFFF),
        nickname=soprannome,
        language=LINGUE[lingua],
        flags=0x02,
        ot_name=ot_bytes,
        markings=0,
        growth=gen3.Growth(species=specie_id, held_item=0,
                           experience=G3.esperienza(gruppo, livello),
                           pp_bonuses=0, friendship=indole["amicizia"]),
        attacks=gen3.Attacks(moves=(mosse + [0, 0, 0, 0])[:4], pp=(pp + [0, 0, 0, 0])[:4]),
        evs=gen3.EvsCondition(),
        misc=gen3.Misc(
            pokerus=0,
            met_location=luogo,
            met_level=livello,
            met_game=G3.VERSIONI[versione],
            pokeball=4,
            ot_female=(allenatore.get("sesso") == "femmina"),
            ivs=iv,
            is_egg=False,
            ability_num=bit,
            modern_fateful_encounter=fatidico,
        ),
    )
    return mon, {
        "sigla": sigla, "seme": seme, "personalita": personalita, "iv": iv,
        "mosse": mosse, "livello": livello, "versione": versione, "luogo": luogo,
        "nome_luogo": nome_luogo, "forma": forma, "lingua": lingua,
        "cromatico": cromatico(personalita, allenatore["identificativo"],
                               allenatore["segreto"]),
        "amicizia": indole["amicizia"], "nome_ot": nome_ot,
    }


def elenca():
    print("Le voci sbloccate da un biglietto, e i loro giochi.")
    print("")
    print("%-11s %-8s %-4s %-4s %-6s %-9s %s"
          % ("sigla", "specie", "liv", "ver", "luogo", "lingua", "forma resa dal gioco"))
    for sigla, naz, liv, ver, luo, forma, lingua, _nome_luogo in INCONTRI:
        resa = {0: "normale", 1: "attacco", 2: "difesa", 3: "velocita"}.get(forma, "-")
        print("%-11s %-8d %-4d %-4s %-6d %-9s %s" % (sigla, naz, liv, ver, luo, lingua, resa))
    print("")
    print("La forma normale di Deoxys non compare perche' le due versioni di apertura non")
    print("ricevettero il biglietto. Si ottiene cambiando forma a un quarto corpo dalla quarta")
    print("generazione in avanti, dove la forma diventa un campo memorizzato e questa specie")
    print("puo' cambiarla liberamente qualunque sia la sua origine.")


def lotto(ace, pkhex, cartella, allenatore):
    if not os.path.isdir(cartella):
        os.makedirs(cartella)
    impronte, fatti = {}, 0
    for voce in INCONTRI:
        mon, r = componi(ace, pkhex, voce, allenatore)
        nome = r["sigla"]
        G3.scrivi(mon, os.path.join(cartella, nome))
        canonica = mon.to_canonical_bytes(party=False)
        impronte[r["sigla"]] = {
            "file": nome + ".pk3",
            "sha256": hashlib.sha256(canonica).hexdigest(),
            "seme": "0x%08X" % r["seme"],
            "personalita": "0x%08X" % r["personalita"],
            "correlazione": "primo metodo",
        }
        fatti += 1
        print("  %-11s liv %-3d %-3s luogo %-4d  seme 0x%08X  PID 0x%08X  IV %s%s"
              % (r["sigla"], r["livello"], r["versione"], r["luogo"], r["seme"],
                 r["personalita"],
                 "/".join(str(r["iv"][k]) for k in ("hp", "atk", "def", "spd", "satk", "sdef")),
                 "  CROMATICO" if r["cromatico"] else ""))
    manifesto = os.path.join(cartella, "manifesto.json")
    io.open(manifesto, "w", encoding="utf-8").write(
        json.dumps(impronte, indent=1, ensure_ascii=False))
    print("")
    print("%d esemplari scritti in %s, con il manifesto delle impronte." % (fatti, cartella))
    return fatti


def self_test():
    esiti = []

    def prova(nome, condizione, dettaglio=""):
        esiti.append((nome, bool(condizione), dettaglio))

    prova("avanza dal seme nullo", avanza(0) == SOMMA, hex(avanza(0)))

    # Il primo metodo: le quattro estrazioni devono essere le prime quattro del generatore, e la
    # prova e' ricomporre a mano cio' che la funzione compone.
    seme = 0x12345678
    p, iv, _ = primo_metodo(seme)
    t = seme
    t, a = prossimo16(t)
    t, b = prossimo16(t)
    t, c = prossimo15(t)
    t, d = prossimo15(t)
    prova("valore di personalita dalle prime due estrazioni", p == ((b << 16) | a), hex(p))
    prova("valori individuali dalle due successive",
          iv["hp"] == (c & 0x1F) and iv["spd"] == (d & 0x1F)
          and iv["sdef"] == ((d >> 10) & 0x1F), str(iv))
    prova("valori individuali nell'intervallo", all(0 <= v <= 31 for v in iv.values()), str(iv))

    # Il controllo negativo che rende la prova precedente utile: se le due meta' della parola
    # dei valori individuali fossero scambiate, salute e velocita' si scambierebbero. La prova
    # esiste perche' quello scambio produce sei valori tutti leciti e nessun sintomo.
    prova("lo scambio delle due meta produrrebbe un esemplare diverso",
          (c & 0x1F) != (d & 0x1F) or (c >> 10) != (d >> 10),
          "vettore degenere: sceglierne un altro")

    # Il repertorio: la coda e non la testa, e le mosse ripetute non occupano due caselle.
    coppie = [(1, 1), (2, 5), (3, 10), (4, 15), (5, 20), (1, 25)]
    prova("le ultime quattro entro il livello",
          mosse_al_livello(coppie, 20) == [2, 3, 4, 5], str(mosse_al_livello(coppie, 20)))
    prova("una mossa reimparata non occupa due caselle",
          mosse_al_livello(coppie, 25) == [3, 4, 5, 1], str(mosse_al_livello(coppie, 25)))
    prova("sotto il primo livello utile resta cio che si conosce",
          mosse_al_livello(coppie, 1) == [1], str(mosse_al_livello(coppie, 1)))

    prova("la lucentezza si annulla per costruzione",
          cromatico(((0x1234 ^ 111 ^ 222) << 16) | 0x1234, 111, 222), "")
    prova("e non si annulla altrimenti", not cromatico(0x00000001, 111, 222), "")

    # Il riempimento del nome dell'allenatore, che e' il difetto trovato dal primo giudizio.
    class _Finta(object):
        def encode(self, testo, length):
            return bytes(range(0x50, 0x50 + len(testo))) + bytes([0xFF]) * (length - len(testo))
    f = _Finta()
    jp = nome_allenatore(f, "abcd", "Japanese")
    it = nome_allenatore(f, "abcdefg", "Italian")
    prova("il nome giapponese finisce con un byte nullo",
          len(jp) == 7 and jp[-1] == 0x00 and jp[4:6] == bytes([0xFF, 0xFF]), jp.hex(" "))
    prova("il nome internazionale riempie tutti e sette i byte",
          len(it) == 7 and 0x00 not in it, it.hex(" "))
    # I due controlli negativi riproducono la regola del verificatore invece di fidarsi della
    # nostra lettura: un campo giapponese chiuso a terminatore, che e' il difetto corretto qui,
    # deve fallire la prova che il campo corretto supera.
    def terminato_ff_zero(dati, prefill):
        i = dati.find(0xFF)
        if i == -1 or i >= len(dati) - 1:
            return True
        i += 1
        if i < prefill:
            if any(b != 0xFF for b in dati[i:prefill]):
                return False
            i = prefill
            if i >= len(dati):
                return True
        return all(b == 0 for b in dati[i:])
    prova("il campo giapponese corretto supera la regola del verificatore",
          terminato_ff_zero(jp, 6), jp.hex(" "))
    prova("negativo: il campo giapponese chiuso a terminatore la fallisce",
          not terminato_ff_zero(f.encode("abcd", 7), 6), f.encode("abcd", 7).hex(" "))
    prova("il campo internazionale pieno supera la regola",
          terminato_ff_zero(it, 7), it.hex(" "))

    # La tavola dell'Isola del Sud, e l'asimmetria del contrassegno fatidico.
    eone = {v[0]: v for v in INCONTRI if v[1] in (380, 381)}
    prova("quattro voci dall'Isola del Sud", len(eone) == 4, str(sorted(eone)))
    prova("le due versioni di apertura non sono fatidiche",
          SENZA_INCONTRO_FATIDICO == frozenset(["latias-r", "latios-s"]),
          str(sorted(SENZA_INCONTRO_FATIDICO)))
    prova("le due voci di Smeraldo lo sono",
          "latias-e" not in SENZA_INCONTRO_FATIDICO
          and "latios-e" not in SENZA_INCONTRO_FATIDICO, "")
    prova("ogni versione della tavola ha un repertorio",
          all(v[3] in REPERTORI for v in INCONTRI),
          str(sorted({v[3] for v in INCONTRI} - set(REPERTORI))))

    forme = sorted(v[5] for v in INCONTRI if v[1] == 386)
    prova("tre voci di Deoxys con tre forme rese distinte", forme == [1, 2, 3], str(forme))
    prova("nessuna voce rende la forma normale", 0 not in forme, str(forme))
    prova("la sola voce giapponese e Mew",
          [v[0] for v in INCONTRI if v[6] == "Japanese"] == ["mew-e"], "")

    larghezza = max(len(n) for n, _, _ in esiti)
    for nome, ok, dettaglio in esiti:
        print("  %-*s  %s%s" % (larghezza, nome, "ok" if ok else "FALLITO",
                                ("  " + dettaglio) if (dettaglio and not ok) else ""))
    caduti = [n for n, ok, _ in esiti if not ok]
    print("")
    print("%d prove, %d fallite." % (len(esiti), len(caduti)))
    return 1 if caduti else 0


def main():
    global G3
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--ace", default=os.path.join("_notes", "fonti", "ace-builder"))
    p.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "pkhex"))
    p.add_argument("--lotto")
    p.add_argument("--elenco", action="store_true")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()

    if a.self_test:
        return self_test()
    if a.elenco:
        elenca()
        return 0
    if not a.lotto:
        p.error("serve --lotto con la cartella di destinazione, oppure --elenco o --self-test")

    G3 = _fratello()
    allenatore = G3.allenatore_del_progetto()
    if allenatore is None:
        sys.exit("manca il registro dell'allenatore del progetto: senza di esso non si puo "
                 "scrivere il campo che questi esemplari prendono dal giocatore")
    print("Allenatore: %s, identificativo %d, segreto %d."
          % (allenatore["nome"], allenatore["identificativo"], allenatore["segreto"]))
    print("")
    lotto(a.ace, a.pkhex, a.lotto, allenatore)
    return 0


if __name__ == "__main__":
    sys.exit(main())
