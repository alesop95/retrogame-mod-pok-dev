#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone gli esemplari da evento di quinta generazione a partire dalle carte dei doni segreti.

L'archivio, che non e' a passo fisso
------------------------------------
La struttura della carta dichiara 0xCC byte e il file ne misura 145345, che non e' un multiplo di
0xCC: il resto diverso da zero confuta l'ipotesi del passo fisso senza bisogno di leggere alcun
campo, e la lunghezza di un file e' cosi' essa stessa una affermazione verificabile sulla sua
struttura. L'archivio e' invece la concatenazione di due piani. Il primo porta gli n record a passo
fisso, il secondo porta n byte allineati per indice, uno per record, che impacchettano due campi da
quattro bit: il vincolo di versione nel semiottetto basso e quello di lingua in quello alto. Ne
segue n uguale alla lunghezza diviso 0xCD, cioe' 709 esatti e senza resto.

I due campi stanno fuori dal record per due ragioni che portano alla stessa scelta. La prima e' di
compatibilita': i 0xCC byte non sono un formato interno dell'archivio ma il formato del file di
distribuzione vero, quindi allungare il record avrebbe reso i record non piu' estraibili come file
validi. La seconda e' semantica: quei due campi non sono dati della distribuzione ma conoscenza
ricostruita su di essa, cioe' quali versioni e quali lingue ricevettero davvero quella carta.

Quanto va composto, e perche' la quinta e' il caso piu' estremo dei tre
----------------------------------------------------------------------
Delle 709 voci, 700 sono esemplari e 9 sono consegne di altro genere. Di quelle 700, tutte e 700
portano il valore di personalita' nullo, cioe' nessuna lo dichiara; 647 portano i sei valori
individuali al valore che il formato riserva all'indefinito, cioe' 0xFF, e 53 li fissano.

Il confronto con la quarta generazione e' netto. La' il valore di personalita' era dichiarato su
128 voci su 247 e composto sulle altre 119; qui e' composto su tutte. La quinta e' dunque, sull'asse
della composizione, il caso piu' estremo dei tre studiati, e non il piu' semplice come la maggiore
modernita' del formato lascerebbe supporre.

Su un punto pero' e' la piu' onesta delle tre, e conviene dirlo perche' rovescia il verso della
difficolta'. La quarta nascondeva la richiesta di comporre dentro un valore magico, cioe' un valore
di personalita' pari a uno, che nulla nella struttura dichiara come segnale. La quinta la scrive in
chiaro in un campo dedicato all'offset 0x37, che vale zero per mai cromatico, uno per casuale e due
per sempre cromatico, e la distribuzione su 700 voci e' 517, 83 e 100.

Che cosa cambia nel valore di personalita' fra la quarta e la quinta generazione
-------------------------------------------------------------------------------
La differenza non e' di grado ma di architettura, e governa tutto il procedimento di composizione.

In terza e quarta generazione il valore di personalita' e' un accumulatore di significati: da esso
discendono la natura come resto per venticinque, il sesso come confronto del byte basso con il
rapporto della specie, la casella di abilita' come bit meno significativo, e la lucentezza come
somma esclusiva con gli identificativi. Un solo numero porta quattro decisioni, e fissarne una
vincola le altre.

In quinta generazione la natura esce dal valore e diventa un campo memorizzato per conto proprio, e
la casella di abilita' si sposta dal bit zero al bit sedici. Restano legati al valore soltanto il
sesso e la lucentezza. E' un disaccoppiamento deliberato, e la sua conseguenza osservabile e' che
una distribuzione di quinta generazione poteva fissare la natura senza fissare il valore di
personalita', cosa impossibile nelle generazioni precedenti: infatti tutte e 700 le carte lasciano
libero il valore e molte dichiarano la natura.

Ne segue la sequenza che questo programma esegue, che e' quella della fonte. Si tira un valore, se
ne forza il byte basso finche' il sesso che ne discende e' quello dichiarato dalla carta, si impone
la lucentezza secondo la direttiva della carta, e infine si forza il bit sedici sulla casella di
abilita' voluta. L'ordine conta: il bit del sesso sta nel byte basso e la lucentezza si ottiene
scrivendo la parola alta, quindi imporre la lucentezza dopo il sesso non lo distrugge, mentre il
contrario si'.

La lucentezza imposta, e la sua forma chiusa
--------------------------------------------
Dove la carta dichiara di consegnare un esemplare cromatico, il valore non si cerca ma si
costruisce. Detta g la parola bassa gia' fissata dal vincolo di sesso, il valore che rende
l'esemplare cromatico e' quello la cui parola alta vale g in somma esclusiva con i due
identificativi dell'allenatore, cosicche' la somma esclusiva delle quattro parole risulti nulla e
quindi minore di otto. E' una soluzione in forma chiusa e non una ricerca, ed e' la ragione per cui
le cento carte sempre cromatiche non costano nulla piu' delle altre.

La riproducibilita'
-------------------
I semi non vengono dal generatore di sistema ma da un'impronta SHA-256 che nomina la voce, cosicche'
il lotto sia una funzione della base dati e non del momento in cui lo si produce. Vale la stessa
disciplina per la data di incontro, che si prende dalla carta quando la carta la dichiara e da una
costante dichiarata quando non la dichiara.

Uso
---
    python tools/genera-evento-gen5.py --pkhex _notes/fonti/pkhex
    python tools/genera-evento-gen5.py --pkhex <clone> --lotto _notes/lotto-gen5
    python tools/genera-evento-gen5.py --self-test
"""

import argparse
import hashlib
import io
import json
import os
import re
import struct
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MGDB = os.path.join("PKHeX.Core", "Resources", "legality", "mgdb")
PERSONALI = os.path.join("PKHeX.Core", "Resources", "byte", "personal")
TESTI = os.path.join("PKHeX.Core", "Resources", "text", "other")
REGISTRO_ALLENATORE = os.path.join("recreate-pokemon-distributions-events", "allenatore.json")

MAX_SPECIE_5 = 649

# La carta, da PGF. Il record dichiara 0xCC byte e l'archivio ne aggiunge uno per record in coda.
DIM_CARTA = 0xCC
DIM_VINCOLO = 1

OFF_TID = 0x00
OFF_SID = 0x02
OFF_GIOCO_ORIGINE = 0x04
OFF_PID = 0x08
OFF_PALLA = 0x0E
OFF_OGGETTO = 0x10
OFF_MOSSE = 0x12          # quattro parole
OFF_SPECIE = 0x1A
OFF_FORMA = 0x1C
OFF_LINGUA = 0x1D
OFF_SOPRANNOME = 0x1E     # undici caratteri a sedici bit
OFF_NATURA = 0x34
OFF_SESSO = 0x35
OFF_TIPO_ABILITA = 0x36
OFF_DIRETTIVA_LUCE = 0x37
OFF_LUOGO_UOVO = 0x38
OFF_LUOGO = 0x3A
OFF_LIVELLO_INCONTRO = 0x3C
OFF_CONCORSO = 0x3D       # sei byte
OFF_IV = 0x43             # sei byte, nell'ordine PS Att Dif Vel Asp Dsp
OFF_OT_NOME = 0x4A        # otto caratteri a sedici bit
OFF_OT_SESSO = 0x5A
OFF_LIVELLO = 0x5B
OFF_UOVO = 0x5C
OFF_GIORNO = 0xAC
OFF_MESE = 0xAD
OFF_ANNO = 0xAE           # una parola
OFF_TIPO_CARTA = 0xB3

TIPO_ESEMPLARE = 1

# I fiocchi di merito, e la loro rimappatura fra i due formati.
#
# La carta li impacchetta in due byte contigui, l'esemplare li sparpaglia su tre byte che stanno in
# tre punti diversi della struttura, perche' quei byte servivano gia' ai fiocchi delle generazioni
# precedenti e i quindici nuovi sono stati infilati nei bit che restavano liberi. Non c'e' quindi
# alcuna regola di traduzione da dedurre: c'e' una tabella, e va scritta per intero.
#
# Ometterla e' il difetto che ha fatto rifiutare il secondo giro del lotto, ed e' un difetto
# invisibile a qualunque controllo interno: un esemplare senza fiocchi e' ben formato, ha la somma
# di controllo giusta, e sbaglia soltanto rispetto alla carta da cui dice di venire.
#
# La tabella dice, per ciascun fiocco: il byte e il bit nella carta, il byte e il bit
# nell'esemplare, e il nome.
FIOCCHI = (
    (0x0C, 0, 0x3F, 4, "Nazione"),
    (0x0C, 1, 0x3F, 5, "Nazionale"),
    (0x0C, 2, 0x3F, 6, "Terra"),
    (0x0C, 3, 0x3F, 7, "Mondo"),
    (0x0C, 4, 0x27, 2, "Classico"),
    (0x0C, 5, 0x27, 3, "Premier"),
    (0x0C, 6, 0x26, 3, "Evento"),
    (0x0C, 7, 0x26, 6, "Compleanno"),
    (0x0D, 0, 0x26, 7, "Speciale"),
    (0x0D, 1, 0x27, 0, "Ricordo"),
    (0x0D, 2, 0x27, 1, "Desiderio"),
    (0x0D, 3, 0x3F, 1, "Campione di Lotta"),
    (0x0D, 4, 0x3F, 2, "Campione Regionale"),
    (0x0D, 5, 0x3F, 3, "Campione Nazionale"),
    (0x0D, 6, 0x26, 5, "Campione Mondiale"),
)

# L'esemplare, da PK5. La parte di scatola e' lunga 136 byte come in quarta generazione, ma i
# significati dei campi cambiano e in particolare la natura ha un campo proprio.
DIM_PK5_SCATOLA = 136
P_PID = 0x00
P_SANITA = 0x04
P_CHECKSUM = 0x06
P_SPECIE = 0x08
P_OGGETTO = 0x0A
P_TID = 0x0C
P_SID = 0x0E
P_ESPERIENZA = 0x10
P_CORDIALITA = 0x14
P_ABILITA = 0x15
P_LINGUA = 0x17
P_CONCORSO = 0x1E
P_MOSSE = 0x28
P_PP = 0x30
P_IV32 = 0x38
P_FLAG = 0x40             # bit 0 fatidico, bit 1 e 2 sesso, dal bit 3 la forma
P_NATURA = 0x41
P_ABILITA_NASCOSTA = 0x42
P_SOPRANNOME = 0x48
P_VERSIONE = 0x5F
P_OT_NOME = 0x68
P_UOVO_ANNO = 0x78
P_INCONTRO_ANNO = 0x7B
P_LUOGO_UOVO = 0x7E
P_LUOGO = 0x80
P_PALLA = 0x83
P_LIVELLO_INCONTRO = 0x84

TERMINATORE = 0xFFFF

# La tabella personale di quinta generazione.
DIM_PERSONALE = 0x4C
OFF_P_GENERE = 0x12
OFF_P_CICLI = 0x13
OFF_P_CORDIALITA = 0x14
OFF_P_CRESCITA = 0x15
OFF_P_ABILITA1 = 0x18
OFF_P_ABILITA2 = 0x19
OFF_P_ABILITA_NASCOSTA = 0x1A

RAPPORTO_SOLO_MASCHI = 0
RAPPORTO_SOLO_FEMMINE = 254
RAPPORTO_ASESSUATO = 255

# I sei gruppi di crescita, nella numerazione della tabella personale.
MEDIUM_FAST, ERRATIC, FLUCTUATING, MEDIUM_SLOW, FAST, SLOW = 0, 1, 2, 3, 4, 5

# La data che si scrive quando la carta non ne dichiara una. E' una costante e non l'orologio,
# perche' un lotto riproducibile non puo' dipendere da quando lo si produce.
DATA_SUPPLENTE = (2026, 9, 7)

LINGUE = {1: "ja", 2: "en", 3: "fr", 4: "it", 5: "de", 7: "es", 8: "ko"}

# I due nomi che la consegna scrive al posto di quello di chi riceve, quando la lingua dell'uovo e
# quella di chi riceve stanno su lati opposti della barriera giapponese. Vengono da TrainerName e
# non sono una convenzione nostra: un uovo giapponese consegnato a un allenatore non giapponese non
# porta il nome di quell'allenatore, perche' il gioco non saprebbe scriverlo.
SEGNAPOSTO_GIAPPONESE = "ゲーフリ"
SEGNAPOSTO_INTERNAZIONALE = "GF"
LINGUA_GIAPPONESE = 1

# Il livello di incontro di un uovo di quinta generazione, da EggStateLegality: e' uno, e non zero
# come in terza e quarta. Nove carte su quarantotto lo portano a zero e vanno corrette.
LIVELLO_INCONTRO_UOVO = 1


def nome_dell_allenatore(nome_proprio, lingua_allenatore, lingua_uovo):
    """Il nome che l'uovo porta, da EncounterUtil.GetTrainerName."""
    if lingua_uovo == LINGUA_GIAPPONESE:
        return nome_proprio if lingua_allenatore == LINGUA_GIAPPONESE else SEGNAPOSTO_GIAPPONESE
    return SEGNAPOSTO_INTERNAZIONALE if lingua_allenatore == LINGUA_GIAPPONESE else nome_proprio


PP_SORGENTE = os.path.join("PKHeX.Core", "Moves", "MoveInfo5.cs")
REPERTORIO = os.path.join("PKHeX.Core", "Resources", "byte", "levelup", "lvlmove_b2w2.pkl")


def aree_indicizzate(dati):
    """Le aree di un archivio con la tabella delle posizioni a sedici bit.

    E' la medesima forma gia' incontrata negli archivi degli incontri: due byte di firma, il conto
    delle voci, e poi una posizione per voce, dove la fine di un'area coincide con l'inizio della
    successiva e quindi la coppia si legge come un intero doppio.
    """
    if len(dati) < 4:
        return None
    quante = struct.unpack_from("<H", dati, 2)[0]
    fuori = []
    for i in range(quante):
        off = 4 + i * 2
        if off + 4 > len(dati):
            return None
        coppia = struct.unpack_from("<I", dati, off)[0]
        inizio, fine = coppia & 0xFFFF, coppia >> 16
        if not (0 <= inizio <= fine <= len(dati)):
            return None
        fuori.append(dati[inizio:fine])
    return fuori


def repertorio_di_livello(area):
    """Le mosse che una specie impara salendo di livello, come coppie di mossa e livello.

    L'area non e' fatta di coppie ma di due elenchi consecutivi di lunghezza diversa: prima le
    mosse, una parola ciascuna, poi i livelli, un byte ciascuno. Ne segue che l'area misura tre
    byte per mossa, ed e' la relazione che permette di stabilire il numero delle voci senza che
    l'archivio lo dichiari. Le due letture piu' naturali, cioe' coppie alternate oppure due meta'
    uguali, danno entrambe risultati privi di senso e sono state escluse guardandoli.
    """
    n = len(area) // 3
    mosse = [struct.unpack_from("<H", area, 2 * i)[0] for i in range(n)]
    livelli = list(area[2 * n:3 * n])
    return list(zip(mosse, livelli))


def mosse_al_livello(area, livello):
    """Le ultime quattro mosse imparate entro un livello, che e' cio' che il gioco assegna.

    La verifica non e' interna. Le sei carte di Keldeo e la sola di Meloetta che non dichiarano
    mosse hanno un gemello nell'archivio enciclopedico, che quelle mosse le registra: per Keldeo al
    livello quindici le quattro calcolate coincidono esattamente con le quattro registrate, e per
    Meloetta coincide l'insieme mentre l'ordine di visualizzazione della fonte esterna differisce,
    che e' una convenzione sua e non un disaccordo.
    """
    return [mv for mv, lv in repertorio_di_livello(area) if lv <= livello][-4:]


def tabella_repertorio(pkhex):
    percorso = os.path.join(pkhex, REPERTORIO)
    if not os.path.exists(percorso):
        return None
    return aree_indicizzate(io.open(percorso, "rb").read())



def tabella_pp(pkhex):
    """I punti potenza base di ciascuna mossa, letti dal sorgente della fonte.

    Si leggono invece di trascriverli perche' sono cinquecentosessanta numeri e una trascrizione di
    quella lunghezza e' un difetto che aspetta: il progetto ha gia' pagato una volta il prezzo di
    una tabella copiata a mano.
    """
    percorso = os.path.join(pkhex, PP_SORGENTE)
    if not os.path.exists(percorso):
        return None
    testo = io.open(percorso, encoding="utf-8").read()
    inizio = testo.index("[", testo.index("PP =>"))
    fine = testo.index("];", inizio)
    return [int(x) for x in re.findall("[0-9]+", testo[inizio:fine])]


def allenatore_del_progetto():
    percorso = os.path.join(RADICE, REGISTRO_ALLENATORE)
    if not os.path.exists(percorso):
        return None
    return json.load(io.open(percorso, encoding="utf-8"))


def esperienza(gruppo, livello):
    """L'esperienza totale per raggiungere un livello, secondo il gruppo di crescita.

    Le sei formule sono le medesime gia' usate per la terza generazione e sono canoniche; il
    verificatore esterno e' lo strumento che dira' se sono giuste, perche' una esperienza
    incoerente con il livello e' fra le prime cose che esso controlla.
    """
    n = max(1, min(100, int(livello)))
    if n <= 1:
        return 0
    if gruppo == MEDIUM_FAST:
        return n ** 3
    if gruppo == ERRATIC:
        if n < 50:
            return (n ** 3 * (100 - n)) // 50
        if n < 68:
            return (n ** 3 * (150 - n)) // 100
        if n < 98:
            return (n ** 3 * ((1911 - 10 * n) // 3)) // 500
        return (n ** 3 * (160 - n)) // 100
    if gruppo == FLUCTUATING:
        if n < 15:
            return (n ** 3 * (((n + 1) // 3) + 24)) // 50
        if n < 36:
            return (n ** 3 * (n + 14)) // 50
        return (n ** 3 * ((n // 2) + 32)) // 50
    if gruppo == MEDIUM_SLOW:
        return (6 * n ** 3) // 5 - 15 * n ** 2 + 100 * n - 140
    if gruppo == FAST:
        return (4 * n ** 3) // 5
    if gruppo == SLOW:
        return (5 * n ** 3) // 4
    raise ValueError("gruppo di crescita sconosciuto: %r" % (gruppo,))


def stringa_utf16(dati, offset, quanti):
    """Una stringa di quinta generazione: parole a sedici bit terminate da 0xFFFF."""
    fuori = []
    for k in range(quanti):
        v = struct.unpack_from("<H", dati, offset + 2 * k)[0]
        if v in (TERMINATORE, 0):
            break
        fuori.append(chr(v))
    return "".join(fuori)


def scrivi_utf16(dati, offset, quanti, testo):
    for k in range(quanti):
        v = ord(testo[k]) if k < len(testo) else TERMINATORE
        struct.pack_into("<H", dati, offset + 2 * k, v)


def e_cromatico(pid, tid, sid):
    return (tid ^ sid ^ (pid >> 16) ^ (pid & 0xFFFF)) < 8


def sesso_da_pid(pid, rapporto):
    if rapporto == RAPPORTO_ASESSUATO:
        return 2
    if rapporto == RAPPORTO_SOLO_FEMMINE:
        return 1
    if rapporto == RAPPORTO_SOLO_MASCHI:
        return 0
    return 1 if (pid & 0xFF) < rapporto else 0


def pid_cromatico(basso_byte, tid, sid):
    """Il valore di personalita' che rende cromatico un esemplare, in forma chiusa.

    Da MonochromeRNG.GetShinyPID. Fissata la parola bassa dal vincolo di sesso, la parola alta che
    annulla la somma esclusiva delle quattro parole e' quella stessa parola in somma esclusiva con
    i due identificativi: non c'e' nulla da cercare.
    """
    gb = basso_byte & 0xFF
    return (((gb ^ tid ^ sid) & 0xFFFF) << 16) | gb


def forza_abilita(pid, casella):
    """Impone il bit sedici, che in quinta generazione porta la casella di abilita'."""
    voluto = (casella & 1) << 16
    return pid ^ 0x10000 if (pid & 0x10000) != voluto else pid


def seme(indice, sale):
    chiave = "EVT-5|%d|%s" % (indice, sale)
    return struct.unpack("<I", hashlib.sha256(chiave.encode("utf-8")).digest()[:4])[0]


def prossimo(stato):
    """Un generatore congruenziale a 32 bit, deterministico e nostro.

    Non imita alcun generatore del gioco e non deve: la fonte stessa, per questi doni, tira il
    valore da un generatore di sistema, quindi la coppia di personalita' e valori individuali non
    esibisce alcuna correlazione nota. Qui serve soltanto una sorgente riproducibile.
    """
    return (stato * 1664525 + 1013904223) & 0xFFFFFFFF


def componi_pid(indice, carta_pid, direttiva, tid, sid, sesso_voluto, rapporto, casella):
    """Il valore di personalita' di una voce, secondo la sequenza della fonte.

    Se la carta ne dichiara uno, quello e' il dato storico e si conserva. Altrimenti si compone
    nell'ordine che la fonte impone: prima il sesso, che vive nel byte basso, poi la lucentezza,
    che si ottiene scrivendo la parola alta e quindi non tocca il byte basso, e infine la casella
    di abilita', che vive nel bit sedici e non tocca ne' l'uno ne' l'altra.
    """
    if carta_pid != 0:
        return carta_pid, "dalla carta"
    stato = seme(indice, "pid")
    pid = 0
    for _ in range(1 << 16):
        stato = prossimo(stato)
        pid = stato
        if sesso_da_pid(pid, rapporto) == sesso_voluto:
            break
    else:
        return None, "nessun valore soddisfa il vincolo di sesso"
    if direttiva == 2:
        # Si passa il solo byte basso e non la parola: il verificatore riconosce la forma
        # cromatica dei doni di quinta generazione soltanto se la parola bassa non supera 0xFF,
        # perche' il gioco costruiva quel valore a partire da un byte. Con la parola intera
        # l'esemplare risulta cromatico e nondimeno illegittimo, che e' il caso peggiore: giusto
        # nell'effetto e sbagliato nel procedimento.
        pid = pid_cromatico(pid, tid, sid)
    elif direttiva != 1 and e_cromatico(pid, tid, sid):
        pid ^= 0x10000000
    return forza_abilita(pid, casella), "composto"


def componi_iv(indice, modello):
    """I sei valori individuali, con i due segnali che il formato riserva.

    Un valore fino a 31 e' fissato dalla carta. Il valore 0xFF significa tiralo. I valori da 0xFC a
    0xFE significano che un certo numero di statistiche deve valere 31 e le altre vanno tirate: e'
    un caso raro e va riconosciuto, perche' trattarlo come un valore lo scriverebbe fuori intervallo.
    """
    stato = seme(indice, "iv")
    fuori, perfetti = list(modello), 0
    for v in modello:
        if 0xFC <= v <= 0xFE:
            perfetti = max(perfetti, v - 0xFB)
    da_tirare = [k for k, v in enumerate(modello) if v > 31]
    for k in da_tirare:
        stato = prossimo(stato)
        fuori[k] = (stato >> 16) % 32
    for k in da_tirare[:perfetti]:
        fuori[k] = 31
    return fuori


def leggi_carte(pkhex):
    percorso = os.path.join(pkhex, MGDB, "pgf.pkl")
    if not os.path.exists(percorso):
        return None, "manca pgf.pkl sotto " + os.path.join(pkhex, MGDB)
    dati = io.open(percorso, "rb").read()
    quante, resto = divmod(len(dati), DIM_CARTA + DIM_VINCOLO)
    if resto:
        return None, ("la dimensione %d non chiude con record da %d piu' un byte di vincolo: la "
                      "forma dell'archivio che stiamo usando e' sbagliata"
                      % (len(dati), DIM_CARTA))
    coda = quante * DIM_CARTA
    personale = os.path.join(pkhex, PERSONALI, "personal_b2w2")
    if not os.path.exists(personale):
        return None, "manca la tabella personale personal_b2w2"
    tabella = io.open(personale, "rb").read()

    fuori, non_esemplari, difettose = [], 0, []
    for indice in range(quante):
        r = dati[indice * DIM_CARTA:(indice + 1) * DIM_CARTA]
        vincolo = dati[coda + indice]
        if r[OFF_TIPO_CARTA] != TIPO_ESEMPLARE:
            non_esemplari += 1
            continue
        specie = struct.unpack_from("<H", r, OFF_SPECIE)[0]
        if not 1 <= specie <= MAX_SPECIE_5:
            difettose.append((indice, "specie %d fuori dall'intervallo" % specie))
            continue
        inizio = specie * DIM_PERSONALE
        if inizio + DIM_PERSONALE > len(tabella):
            difettose.append((indice, "la specie %d non sta nella tabella personale" % specie))
            continue
        fuori.append({
            "indice": indice,
            "carta": r,
            "personale": tabella[inizio:inizio + DIM_PERSONALE],
            "specie": specie,
            "pid": struct.unpack_from("<I", r, OFF_PID)[0],
            "direttiva": r[OFF_DIRETTIVA_LUCE],
            "iv": list(r[OFF_IV:OFF_IV + 6]),
            "uovo": r[OFF_UOVO] == 1,
            "lingua": r[OFF_LINGUA],
            "vincolo_versione": vincolo & 0x0F,
            "vincolo_lingua": (vincolo >> 4) & 0x0F,
        })
    return {"voci": fuori, "non_esemplari": non_esemplari, "difettose": difettose,
            "record": quante}, None


def consegna(v, allenatore, nomi_specie, pp, repertorio):
    """Applica alla carta le mutazioni della consegna e restituisce i byte dell'esemplare."""
    r = v["carta"]
    p = bytearray(DIM_PK5_SCATOLA)
    resoconto = {"pid": "dalla carta", "iv": "composti", "allenatore": "storico",
                 "natura": "dalla carta", "sesso": "dalla carta", "fiocchi": 0,
                 "mosse": "dalla carta"}

    struct.pack_into("<H", p, P_SPECIE, v["specie"])
    struct.pack_into("<H", p, P_OGGETTO, struct.unpack_from("<H", r, OFF_OGGETTO)[0])
    # Le mosse: dalla carta se la carta ne dichiara, altrimenti quelle che la specie ha imparato
    # entro il livello. Sette carte su settecento non ne dichiarano alcuna, e sono le sei di Keldeo
    # e la sola di Meloetta: copiare i loro zeri produce un esemplare senza mosse, che il
    # verificatore rifiuta dicendo che la prima mossa e' vuota.
    dalla_carta = [struct.unpack_from("<H", r, OFF_MOSSE + 2 * k)[0] for k in range(4)]
    if dalla_carta[0] == 0 and repertorio is not None and v["specie"] < len(repertorio):
        dalla_carta = mosse_al_livello(repertorio[v["specie"]], r[OFF_LIVELLO])
        dalla_carta = dalla_carta + [0] * (4 - len(dalla_carta))
        resoconto["mosse"] = "dal repertorio di livello"
    for k in range(4):
        struct.pack_into("<H", p, P_MOSSE + 2 * k, dalla_carta[k])
    p[P_LINGUA] = v["lingua"] or v["vincolo_lingua"] or 2
    p[P_PALLA] = r[OFF_PALLA]
    struct.pack_into("<H", p, P_LUOGO, struct.unpack_from("<H", r, OFF_LUOGO)[0])
    struct.pack_into("<H", p, P_LUOGO_UOVO, struct.unpack_from("<H", r, OFF_LUOGO_UOVO)[0])
    for k in range(6):
        p[P_CONCORSO + k] = r[OFF_CONCORSO + k]
    # La natura: la carta la dichiara oppure porta 255, che non e' una natura ma il segnale di
    # tirarla. Copiare 255 nel campo produce un esemplare la cui natura non esiste, e il
    # verificatore lo mostra come una cella vuota invece che come un errore.
    if r[OFF_NATURA] <= 24:
        p[P_NATURA] = r[OFF_NATURA]
        resoconto["natura"] = "dalla carta"
    else:
        p[P_NATURA] = prossimo(seme(v["indice"], "natura")) % 25
        resoconto["natura"] = "composta"
    # Il livello di incontro viene dal livello della carta e non dal campo che la struttura
    # chiama livello di incontro. La distinzione sembra pedanteria e non lo e': la consegna
    # scrive nel livello di incontro il livello a cui l'esemplare viene consegnato, e il
    # campo 0x3C porta altro. I due coincidono su seicentottantasette carte su settecento e
    # divergono su tredici, cioe' nove uova e quattro voci; quelle quattro sono esattamente
    # le quattro che il verificatore non riconosceva.
    p[P_LIVELLO_INCONTRO] = r[OFF_LIVELLO] & 0x7F
    versione = r[OFF_GIOCO_ORIGINE]
    if versione == 0:
        # Il vincolo dichiara con quali delle quattro versioni la carta funzionava, un bit
        # ciascuna: si sceglie la prima ammessa invece di tirarla, perche' il lotto e' riproducibile.
        for k in range(4):
            if v["vincolo_versione"] & (1 << k):
                versione = 20 + k  # Bianco, Nero, Bianco 2, Nero 2 nella numerazione della fonte
                break
        else:
            versione = 20
    p[P_VERSIONE] = versione

    # L'allenatore: dalla carta, salvo le uova, che nella fonte prendono quello di chi riceve.
    if v["uovo"] and allenatore:
        tid, sid = allenatore["tid"] & 0xFFFF, allenatore["sid"] & 0xFFFF
        nome = nome_dell_allenatore(allenatore.get("nome", "Alessio"),
                                    allenatore.get("lingua", 4),
                                    p[P_LINGUA])
        resoconto["allenatore"] = "del progetto"
    else:
        tid = struct.unpack_from("<H", r, OFF_TID)[0]
        sid = struct.unpack_from("<H", r, OFF_SID)[0]
        nome = stringa_utf16(r, OFF_OT_NOME, 8)
    struct.pack_into("<H", p, P_TID, tid)
    struct.pack_into("<H", p, P_SID, sid)
    scrivi_utf16(p, P_OT_NOME, 8, nome)
    # Il livello di incontro, e per le uova il sesso di chi riceve invece di quello della carta.
    if v["uovo"]:
        p[P_LIVELLO_INCONTRO] = LIVELLO_INCONTRO_UOVO
    else:
        p[P_LIVELLO_INCONTRO] = (p[P_LIVELLO_INCONTRO] & 0x7F) | ((r[OFF_OT_SESSO] & 1) << 7)

    lingua = p[P_LINGUA]
    soprannome = stringa_utf16(r, OFF_SOPRANNOME, 11)
    ha_soprannome = bool(soprannome)
    if v["uovo"]:
        # Un uovo porta sempre come nome quello dell'uovo nella propria lingua, ed e' contrassegnato
        # come soprannominato: e' la fonte a stabilirlo, e non lo si deduce dalla carta.
        soprannome = nome_nella_lingua(nomi_specie, lingua, 0)
        ha_soprannome = True
    elif not soprannome:
        soprannome = nome_nella_lingua(nomi_specie, lingua, v["specie"])
    scrivi_utf16(p, P_SOPRANNOME, 11, soprannome)

    # La data di incontro: dalla carta se la dichiara, altrimenti da una costante nostra.
    giorno, mese = r[OFF_GIORNO], r[OFF_MESE]
    anno = struct.unpack_from("<H", r, OFF_ANNO)[0]
    if giorno == 0:
        anno, mese, giorno = DATA_SUPPLENTE
    p[P_INCONTRO_ANNO] = (anno - 2000) & 0xFF
    p[P_INCONTRO_ANNO + 1] = mese
    p[P_INCONTRO_ANNO + 2] = giorno

    # L'abilita': la carta dichiara la casella, non il numero.
    tipo = r[OFF_TIPO_ABILITA]
    casella = tipo if tipo <= 2 else 0
    ab = (v["personale"][OFF_P_ABILITA1], v["personale"][OFF_P_ABILITA2],
          v["personale"][OFF_P_ABILITA_NASCOSTA])
    p[P_ABILITA] = ab[casella]
    if casella == 2:
        p[P_ABILITA_NASCOSTA] |= 1

    # Il sesso: la carta lo dichiara oppure porta due, che significa lasciarlo libero. Dove e'
    # libero va tirato secondo il rapporto della specie e non fissato a una costante: la prima
    # stesura lo derivava da un valore di personalita' nullo, che rendeva femmina ogni esemplare
    # di ogni specie a due sessi, cioe' cinquecentonove voci su settecento.
    rapporto = v["personale"][OFF_P_GENERE]
    sesso_carta = r[OFF_SESSO]
    if rapporto in (RAPPORTO_ASESSUATO, RAPPORTO_SOLO_FEMMINE, RAPPORTO_SOLO_MASCHI):
        sesso = sesso_da_pid(0, rapporto)
    elif sesso_carta in (0, 1):
        sesso = sesso_carta
    else:
        sesso = 1 if (prossimo(seme(v["indice"], "sesso")) >> 16) % 256 < rapporto else 0
        resoconto["sesso"] = "composto"

    pid, come = componi_pid(v["indice"], v["pid"], v["direttiva"], tid, sid, sesso, rapporto,
                            min(casella, 1))
    if pid is None:
        return None, {"errore": come}
    struct.pack_into("<I", p, P_PID, pid)
    resoconto["pid"] = come

    iv = componi_iv(v["indice"], v["iv"])
    if all(x <= 31 for x in v["iv"]):
        resoconto["iv"] = "dalla carta"
    iv32 = 0
    for k, valore in enumerate(iv):
        iv32 |= (valore & 31) << (5 * k)
    bandiere = 0x80000000 if ha_soprannome else 0
    if v["uovo"]:
        bandiere |= 0x40000000
    struct.pack_into("<I", p, P_IV32, iv32 | bandiere)

    # I punti potenza: la consegna li riporta al massimo della mossa. Lasciarli a zero produce un
    # esemplare le cui mosse non si possono usare, e il verificatore lo rileva.
    for k in range(4):
        mossa = struct.unpack_from("<H", p, P_MOSSE + 2 * k)[0]
        p[P_PP + k] = pp[mossa] if mossa and mossa < len(pp) else 0

    # I fiocchi, uno per uno secondo la tabella di rimappatura.
    quanti = 0
    for byte_carta, bit_carta, byte_pk, bit_pk, _ in FIOCCHI:
        if r[byte_carta] & (1 << bit_carta):
            p[byte_pk] |= 1 << bit_pk
            quanti += 1
    resoconto["fiocchi"] = quanti

    if v["uovo"]:
        # La data si sposta dall'incontro all'uovo, e quella dell'incontro si azzera. Non e' una
        # scelta ma una regola del verificatore, che pretende la corrispondenza fra un luogo e la
        # sua data in entrambi i versi: dove il luogo e' nullo la data dev'essere interamente
        # nulla, e dove il luogo c'e' la data deve esserci. Un uovo non ancora schiuso non ha
        # luogo di incontro, perche' non e' ancora stato incontrato, e non puo' quindi averne la
        # data. Scriverla produce il rilievo che dichiara la data non valida nel calendario, il
        # che inganna perche' la data e' una data perfettamente valida: cio' che non e' valido e'
        # che esista.
        p[P_UOVO_ANNO] = p[P_INCONTRO_ANNO]
        p[P_UOVO_ANNO + 1] = p[P_INCONTRO_ANNO + 1]
        p[P_UOVO_ANNO + 2] = p[P_INCONTRO_ANNO + 2]
        p[P_INCONTRO_ANNO] = 0
        p[P_INCONTRO_ANNO + 1] = 0
        p[P_INCONTRO_ANNO + 2] = 0

    p[P_FLAG] = 1 | (sesso << 1) | (r[OFF_FORMA] << 3)
    p[P_CORDIALITA] = (v["personale"][OFF_P_CICLI] if v["uovo"]
                       else v["personale"][OFF_P_CORDIALITA])
    struct.pack_into("<I", p, P_ESPERIENZA,
                     esperienza(v["personale"][OFF_P_CRESCITA], r[OFF_LIVELLO]))
    struct.pack_into("<H", p, P_SANITA, 0)

    somma = 0
    for i in range(0x08, DIM_PK5_SCATOLA, 2):
        somma = (somma + struct.unpack_from("<H", p, i)[0]) & 0xFFFF
    struct.pack_into("<H", p, P_CHECKSUM, somma)
    return bytes(p), resoconto


def nomi_delle_specie(pkhex):
    """I nomi delle specie in ciascuna delle sette lingue, indicizzati per codice di lingua.

    Servono tutte e sette e non una sola. Il soprannome di un esemplare non soprannominato e' il
    nome della specie nella lingua dell'esemplare, e scriverlo in una lingua sola produce un
    esemplare giapponese che si chiama Mewtwo invece di quel nome scritto in giapponese. Il difetto
    e' invisibile finche' non si guarda la legittimita' per lingua, perche' le cinque lingue
    occidentali condividono quasi tutti i nomi e sembrano confermare la scelta.

    La voce di indice zero di ciascun elenco non e' una specie ma il nome dell'uovo in quella
    lingua, che serve alle quarantotto carte che consegnano un uovo.
    """
    fuori = {}
    for codice, sigla in LINGUE.items():
        percorso = os.path.join(pkhex, TESTI, sigla, "text_Species_%s.txt" % sigla)
        if not os.path.exists(percorso):
            continue
        righe = io.open(percorso, encoding="utf-8-sig").read().splitlines()
        fuori[codice] = righe
    return fuori


def nome_nella_lingua(nomi, lingua, indice):
    """Il nome di indice dato nella lingua data, con l'inglese come ripiego dichiarato."""
    elenco = nomi.get(lingua) or nomi.get(2) or []
    return elenco[indice] if indice < len(elenco) else ""


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("la carta e' lunga 0xCC", 204, DIM_CARTA)
    prova("l'archivio aggiunge un byte per record", 1, DIM_VINCOLO)
    prova("la parte di scatola e' lunga 136", 136, DIM_PK5_SCATOLA)

    # La forma dell'archivio: e' la divisione che stabilisce il numero dei record.
    prova("709 record da 145345 byte", 709, 145345 // (DIM_CARTA + DIM_VINCOLO))
    prova("e la divisione non lascia resto", 0, 145345 % (DIM_CARTA + DIM_VINCOLO))

    # La lucentezza in forma chiusa: la parola alta si costruisce, non si cerca.
    pid = pid_cromatico(0x1234, 1000, 2000)
    prova("il valore costruito e' cromatico", True, e_cromatico(pid, 1000, 2000))
    prova("conserva il byte basso che il sesso aveva fissato", 0x34, pid & 0xFF)
    # Il vincolo che il secondo giro aveva violato: il verificatore riconosce la forma cromatica
    # dei doni di quinta soltanto se la parola bassa non supera 0xFF, perche' il gioco la
    # costruiva da un byte. Con la parola intera l'esemplare risulta cromatico e nondimeno
    # illegittimo, cioe' giusto nell'effetto e sbagliato nel procedimento.
    prova("la parola bassa non supera un byte", True, (pid & 0xFFFF) <= 0xFF)
    prova("e resta cromatico anche dopo il bit dell'abilita'", True,
          e_cromatico(forza_abilita(pid, 1), 1000, 2000))
    prova("che a sua volta non tocca la parola bassa", True,
          (forza_abilita(pid, 1) & 0xFFFF) <= 0xFF)

    # Il bit dell'abilita' sta al sedici e non allo zero, che e' la differenza con la quarta.
    prova("la casella zero spegne il bit sedici", 0, forza_abilita(0x00010000, 0) & 0x10000)
    prova("la casella uno lo accende", 0x10000, forza_abilita(0x00000000, 1) & 0x10000)
    prova("e non tocca il byte basso", 0xAB, forza_abilita(0x000000AB, 1) & 0xFF)

    prova("asessuato", 2, sesso_da_pid(0x12345678, RAPPORTO_ASESSUATO))
    prova("sotto la soglia e' femmina", 1, sesso_da_pid(0x00000010, 31))
    prova("sopra la soglia e' maschio", 0, sesso_da_pid(0x000000FF, 31))

    # I due segnali dei valori individuali.
    iv = componi_iv(1, [31, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
    prova("il valore fissato dalla carta si conserva", 31, iv[0])
    prova("gli altri stanno nell'intervallo", True, all(0 <= x <= 31 for x in iv))
    prova("la composizione e' deterministica", iv, componi_iv(1, [31, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]))
    iv = componi_iv(2, [0xFD, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
    prova("il segnale di due perfetti ne produce almeno due", True,
          sum(1 for x in iv if x == 31) >= 2)

    # La composizione del valore rispetta i due vincoli insieme.
    pid, come = componi_pid(7, 0, 2, 1000, 2000, 0, 31, 1)
    prova("il valore composto e' dichiarato tale", "composto", come)
    prova("e' cromatico quando la carta lo impone", True, e_cromatico(pid, 1000, 2000))
    prova("ha il sesso voluto", 0, sesso_da_pid(pid, 31))
    prova("e la casella di abilita' voluta", 0x10000, pid & 0x10000)
    pid, come = componi_pid(7, 0, 0, 1000, 2000, 0, 31, 0)
    prova("dove la carta vieta la lucentezza il valore non e' cromatico", False,
          e_cromatico(pid, 1000, 2000))
    pid, come = componi_pid(7, 0xABCDEF01, 0, 1000, 2000, 0, 31, 0)
    prova("un valore dichiarato dalla carta si conserva", 0xABCDEF01, pid)
    prova("e si dichiara tale", "dalla carta", come)

    # Le stringhe di quinta generazione sono parole a sedici bit con terminatore.
    b = bytearray(24)
    scrivi_utf16(b, 0, 8, "Alessio")
    prova("una stringa si rilegge", "Alessio", stringa_utf16(b, 0, 8))
    prova("e il terminatore chiude", TERMINATORE, struct.unpack_from("<H", b, 14)[0])

    # I fiocchi: quindici, tutti distinti nell'origine e tutti distinti nella destinazione. La
    # prova che conta e' che nessuna coppia si sovrapponga, perche' una sovrapposizione farebbe
    # accendere due fiocchi con un bit solo e nessun controllo interno se ne accorgerebbe.
    prova("i fiocchi sono quindici", 15, len(FIOCCHI))
    prova("nessuna sorgente si ripete", 15, len({(b, i) for b, i, _, _, _ in FIOCCHI}))
    prova("nessuna destinazione si ripete", 15, len({(b, i) for _, _, b, i, _ in FIOCCHI}))
    prova("le sorgenti stanno nei due byte della carta", {0x0C, 0x0D},
          {b for b, _, _, _, _ in FIOCCHI})
    prova("le destinazioni stanno nei tre byte dell'esemplare", {0x26, 0x27, 0x3F},
          {b for _, _, b, _, _ in FIOCCHI})
    prova("i bit stanno negli otto", True,
          all(0 <= i < 8 and 0 <= j < 8 for _, i, _, j, _ in FIOCCHI))

    # I tre difetti del primo giro, ciascuno con la prova che lo terrebbe corretto.
    # Il primo: 255 nel campo della natura non e' una natura ma il segnale di tirarla, e copiarlo
    # crudo produceva un esemplare la cui natura non esiste su 586 voci su 700.
    prova("una natura tirata sta nell'intervallo", True,
          all(0 <= prossimo(seme(i, "natura")) % 25 <= 24 for i in range(200)))
    prova("e la stessa voce da' sempre la stessa natura",
          prossimo(seme(3, "natura")) % 25, prossimo(seme(3, "natura")) % 25)

    # Il secondo: il sesso lasciato libero dalla carta va tirato secondo il rapporto della specie.
    # La prima stesura lo derivava da un valore di personalita' nullo, che rendeva femmina ogni
    # esemplare di ogni specie a due sessi. La prova e' che su molte voci compaiano entrambi.
    tirati = {1 if (prossimo(seme(i, "sesso")) >> 16) % 256 < 127 else 0 for i in range(200)}
    prova("il sesso tirato non e' costante", {0, 1}, tirati)
    prova("i rapporti magici restano deterministici", (2, 1, 0),
          (sesso_da_pid(0, RAPPORTO_ASESSUATO), sesso_da_pid(0, RAPPORTO_SOLO_FEMMINE),
           sesso_da_pid(0, RAPPORTO_SOLO_MASCHI)))

    # Il terzo: i punti potenza restavano a zero, cioe' mosse che non si possono usare. La prova
    # sulla tabella non si puo' fare senza il sorgente, ma si puo' provare la regola: una mossa
    # nulla non consuma una voce della tabella e una mossa vera si'.
    finta = [0, 35, 25, 10]
    prova("una mossa nulla da' zero punti", 0, finta[0])
    prova("una mossa vera da' i punti della tabella", 35, finta[1])

    # Il nome che un uovo porta, secondo la barriera giapponese.
    prova("un uovo giapponese a un allenatore italiano porta il segnaposto giapponese",
          SEGNAPOSTO_GIAPPONESE, nome_dell_allenatore("Alessio", 4, 1))
    prova("un uovo giapponese a un allenatore giapponese porta il suo nome",
          "Alessio", nome_dell_allenatore("Alessio", 1, 1))
    prova("un uovo occidentale a un allenatore italiano porta il suo nome",
          "Alessio", nome_dell_allenatore("Alessio", 4, 8))
    prova("un uovo occidentale a un allenatore giapponese porta il segnaposto internazionale",
          SEGNAPOSTO_INTERNAZIONALE, nome_dell_allenatore("Alessio", 1, 2))
    prova("il livello di incontro di un uovo di quinta e' uno", 1, LIVELLO_INCONTRO_UOVO)
    # La corrispondenza fra luogo e data, che il verificatore pretende nei due versi. La prova non
    # puo' toccare il verificatore, quindi verifica l'enunciato: un luogo nullo vuole una data
    # nulla, e un luogo non nullo vuole una data non nulla.
    def coerente(luogo, data):
        return (luogo == 0) == (data == (0, 0, 0))
    prova("luogo nullo e data nulla vanno d'accordo", True, coerente(0, (0, 0, 0)))
    prova("luogo nullo e data scritta no", False, coerente(0, (11, 4, 27)))
    prova("luogo scritto e data scritta vanno d'accordo", True, coerente(40059, (11, 4, 27)))
    prova("luogo scritto e data nulla no", False, coerente(40059, (0, 0, 0)))
    # Il campo da cui viene il livello di incontro: e' quello del livello e non quello che la
    # struttura chiama livello di incontro, e i due offset non vanno confusi.
    prova("il livello sta a 0x5B", 0x5B, OFF_LIVELLO)
    prova("e il campo omonimo, che non si usa, sta a 0x3C", 0x3C, OFF_LIVELLO_INCONTRO)

    # Il repertorio delle mosse per livello: l'area non e' fatta di coppie ma di due elenchi
    # consecutivi di lunghezza diversa, e la relazione fra la lunghezza dell'area e il numero delle
    # voci e' cio' che permette di leggerla senza che l'archivio dichiari quel numero.
    finta = struct.pack("<HHH", 453, 43, 24) + bytes([1, 1, 7])
    prova("l'area misura tre byte per mossa", 3, len(finta) // 3)
    prova("il repertorio si legge come mosse e poi livelli",
          [(453, 1), (43, 1), (24, 7)], repertorio_di_livello(finta))
    prova("al livello sei si conoscono le due di livello uno", [453, 43],
          mosse_al_livello(finta, 6))
    prova("al livello sette entra anche la terza", [453, 43, 24],
          mosse_al_livello(finta, 7))
    lunga = struct.pack("<HHHHH", 1, 2, 3, 4, 5) + bytes([1, 2, 3, 4, 5])
    prova("non se ne prendono mai piu' di quattro", [2, 3, 4, 5],
          mosse_al_livello(lunga, 9))

    prova("l'esperienza al livello uno e' nulla", 0, esperienza(MEDIUM_FAST, 1))
    prova("il gruppo medio veloce e' il cubo", 1000000, esperienza(MEDIUM_FAST, 100))

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
    esito, errore = leggi_carte(a.pkhex)
    if errore:
        print("rifiutato: " + errore)
        return 1
    voci = esito["voci"]
    print("Esemplari da evento di quinta generazione")
    print("")
    print("  record nell'archivio                %5d" % esito["record"])
    print("  di cui esemplari                    %5d" % len(voci))
    print("  di cui consegne di altro genere     %5d" % esito["non_esemplari"])
    print("  carte rifiutate                     %5d" % len(esito["difettose"]))
    print("")
    print("  con il valore di personalita' da comporre %5d su %d"
          % (sum(1 for v in voci if v["pid"] == 0), len(voci)))
    print("  con almeno un valore individuale da tirare %5d su %d"
          % (sum(1 for v in voci if any(x > 31 for x in v["iv"])), len(voci)))
    per_direttiva = {}
    for v in voci:
        per_direttiva[v["direttiva"]] = per_direttiva.get(v["direttiva"], 0) + 1
    nomi_d = {0: "mai cromatico", 1: "casuale", 2: "sempre cromatico"}
    print("  direttiva di lucentezza: "
          + ", ".join("%s %d" % (nomi_d.get(k, "codice %d" % k), n)
                      for k, n in sorted(per_direttiva.items())))
    print("  uova                                %5d" % sum(1 for v in voci if v["uovo"]))
    print("  specie distinte                     %5d" % len({v["specie"] for v in voci}))
    if a.lotto:
        if not os.path.isdir(a.lotto):
            os.makedirs(a.lotto)
        allenatore = allenatore_del_progetto()
        nomi = nomi_delle_specie(a.pkhex)
        pp = tabella_pp(a.pkhex)
        repertorio = tabella_repertorio(a.pkhex)
        if pp is None:
            print('rifiutato: manca il sorgente dei punti potenza')
            return 1
        impronte, scritti, composti, rifiutati = {}, 0, 0, []
        for v in voci:
            pk5, resoconto = consegna(v, allenatore, nomi, pp, repertorio)
            if pk5 is None:
                rifiutati.append((v["indice"], resoconto["errore"]))
                continue
            composti += 1 if resoconto["pid"] == "composto" else 0
            nome = "EVT-5-%04d-%03d.pk5" % (v["indice"], v["specie"])
            io.open(os.path.join(a.lotto, nome), "wb").write(pk5)
            impronte[nome] = {"sha256": hashlib.sha256(pk5).hexdigest(),
                              "specie": v["specie"], "pid": resoconto["pid"],
                              "iv": resoconto["iv"], "allenatore": resoconto["allenatore"]}
            scritti += 1
        io.open(os.path.join(a.lotto, "impronte.json"), "w", encoding="utf-8").write(
            json.dumps({"data_supplente": "%04d-%02d-%02d" % DATA_SUPPLENTE,
                        "voci": impronte}, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
        print("")
        print("  scritti %d file in %s, con il valore di personalita' composto su %d"
              % (scritti, a.lotto, composti))
        for indice, ragione in rifiutati:
            print("  rifiutata la carta %d: %s" % (indice, ragione))
    return 0


if __name__ == "__main__":
    sys.exit(main())
