#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone gli esemplari da evento di quarta generazione a partire dai modelli dei doni segreti.

Che cosa contiene davvero un dono di quarta generazione
------------------------------------------------------
Il record del dono e' lungo 0x358 byte e porta, a otto byte dal proprio inizio, una struttura di
esemplare nel formato di squadra del gioco, lunga 236 byte e conservata in chiaro. E' facile
scambiare quella struttura per l'esemplare consegnato, ed e' l'errore che questo programma ha
commesso nella sua prima stesura: la struttura non e' l'esemplare, e' il suo modello. La misura di
quanto vi manchi si legge nei numeri della base dati stessa, che questo programma riferisce a ogni
corsa: tutti e duecentoquarantasette i modelli portano i valori individuali a zero, e
centodiciannove dei duecentoquarantasette portano il valore di personalita' uguale a uno, che nella
convenzione della fonte non e' un valore ma un ordine, cioe' generane uno che non sia cromatico.

Ne segue che il valore di personalita' e i valori individuali di un evento di quarta generazione
non esistono nel dono e non sono mai esistiti prima della consegna: li tirava il gioco sulla
console di chi riceveva. Non c'e' quindi un dato originale da estrarre, e la quarta generazione non
e' piu' economica della terza per la parte che conta: e' composizione, esattamente come la terza,
con la differenza che qui il modello fissa gia' specie, mosse, livello, palla, allenatore, lingua e
fiocchi, mentre in terza generazione andava composto anche quello.

Le mutazioni della consegna, verificate sulla fonte e su un esemplare vero
-------------------------------------------------------------------------
La consegna applica al modello un insieme chiuso di mutazioni, che la fonte concentra in
`PGT.ConvertToPKM` e questo programma rifa' una per una. La piu' importante non e' un calcolo ma
uno spostamento: il modello tiene il luogo della distribuzione nel campo del luogo dell'uovo, e la
consegna lo sposta nel campo del luogo di incontro sommandovi tremila, azzerando il campo di
partenza. Un modello non trasformato ha percio' il luogo di incontro nullo, ed e' la ragione per
cui il verificatore rifiutava tutte e duecentoquarantasette le voci del primo lotto.

Questa regola non e' stata presa sulla parola. E' stata confrontata con i byte di esemplari da
evento veri e riconosciuti legali, letti dal salvataggio di Argento SoulSilver della raccolta: la'
i valori del campo sono 3060 per l'evento Pokemon, 3073 per il dono Wi-Fi e 3001 per Pokemon
Ranger, e i modelli corrispondenti portano nel campo dell'uovo rispettivamente 60, 73 e 1. E' lo
stesso genere di ancoraggio esterno che ADR-036 prescrive dopo il difetto della permutazione:
nessun controllo interno avrebbe potuto stabilire quella somma.

Le altre mutazioni sono minori e si elencano per completezza. Il campo di integrita' formale va
azzerato, perche' un solo dono storico lo porta diverso da zero. La cordialita' si riporta al
valore base della specie. Il contrassegno di uovo si spegne. La data di incontro si scrive, e
questo programma la fissa a una data dichiarata invece che al giorno della corsa, cosicche' due
corse producano gli stessi byte. Il campo esteso del luogo, infine, si scrive o no secondo il gioco
su cui la consegna si intende riscossa, che questo programma prende come parametro e per difetto
suppone Argento SoulSilver, cioe' il gioco in cui il lotto verra' iniettato.

La composizione del valore di personalita', e perche' non puo' avere una correlazione
-------------------------------------------------------------------------------------
Dove il modello porta un valore di personalita' maggiore di uno, quel valore e' il dato storico e
si conserva. Dove porta uno, va composto, e i vincoli sono tre: l'esemplare non deve risultare
cromatico rispetto agli identificativi che il modello stesso dichiara, il genere che ne discende
deve essere quello che il modello dichiara, e la parita' deve concordare con la casella di abilita'
del modello per le specie che ne hanno due.

I valori individuali si tirano da un secondo seme, indipendente dal primo. Non e' una comodita': la
fonte dichiara che per questi doni la coppia di personalita' e valori individuali non deve esibire
alcuna delle correlazioni note fra i due, cioe' deve risultare del tipo nessuna. Comporli dal
medesimo seme in sequenza produrrebbe la correlazione del primo metodo e l'esemplare verrebbe
rifiutato proprio perche' troppo regolare.

Entrambi i semi si ricavano da un'impronta della voce e non da un generatore di sistema, cosicche'
il lotto sia riproducibile byte per byte: rilanciare il programma sulla stessa base dati e con lo
stesso allenatore riscrive file identici, ed e' il requisito che il pedigree impone.

Uso
---
    python tools/genera-evento-gen4.py --pkhex _notes/fonti/pkhex
    python tools/genera-evento-gen4.py --pkhex <clone> --lotto _notes/lotto-gen4
    python tools/genera-evento-gen4.py --self-test
"""

import argparse
import hashlib
import io
import json
import os
import struct
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MGDB = os.path.join("PKHeX.Core", "Resources", "legality", "mgdb")
PERSONALI = os.path.join("PKHeX.Core", "Resources", "byte", "personal")
REGISTRO_ALLENATORE = os.path.join("recreate-pokemon-distributions-events", "allenatore.json")

MAX_SPECIE_4 = 493

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
OFF_SANITA = 0x04
OFF_CHECKSUM = 0x06
OFF_SPECIE = 0x08
OFF_TID = 0x0C
OFF_SID = 0x0E
OFF_ESPERIENZA = 0x10
OFF_CORDIALITA = 0x14
OFF_ABILITA = 0x15
OFF_LINGUA = 0x17
OFF_IV32 = 0x38
OFF_FLAG_GENERE = 0x40     # bit 0 incontro fatidico, bit 1 e 2 genere, dal bit 3 la forma
OFF_UOVO_ESTESO = 0x44     # il luogo dell'uovo nella forma di Platino e HGSS
OFF_INCONTRO_ESTESO = 0x46  # il luogo di incontro nella forma di Platino e HGSS
OFF_VERSIONE = 0x5F
OFF_OT_NOME = 0x68         # sedici byte, sette caratteri piu' il terminatore
OFF_UOVO_ANNO = 0x78
OFF_INCONTRO_ANNO = 0x7B
OFF_UOVO_DP = 0x7E         # il luogo dell'uovo nella forma di Diamante e Perla
OFF_INCONTRO_DP = 0x80     # il luogo di incontro nella forma di Diamante e Perla
OFF_PALLA_DPPT = 0x83
OFF_LIVELLO_INCONTRO = 0x84
OFF_TIPO_INCONTRO = 0x85
OFF_PALLA_HGSS = 0x86

# Il campo che dice se la struttura sia cifrata, da PokeCrypto.IsEncrypted45: sono i bit di fiocco
# inutilizzati, che in chiaro valgono zero. Il controllo e' della fonte e non nostro, e vale
# richiamarlo perche' e' l'unico modo di distinguere le due forme senza provarle entrambe.
OFF_PROVA_CIFRATURA = 0x64

# Lo scostamento che la consegna somma al luogo dichiarato dal modello, da PGT.SetMetData. Il
# valore non e' deducibile dalla struttura e viene dalla fonte, confermato sui byte di esemplari
# veri letti dal salvataggio di Argento SoulSilver.
SCOSTAMENTO_LUOGO = 3000

# Il campo esteso del luogo si scrive quando il gioco che riceve la consegna e' Platino, Oro
# HeartGold o Argento SoulSilver, e resta nullo su Diamante e Perla, che quel campo non conoscono.
# La distinzione e' del gioco che riceve e non della versione che la carta dichiara, e il progetto
# lo sa perche' l'ha visto: nel salvataggio di Argento SoulSilver della raccolta un Pichu che
# dichiara Diamante come versione di origine porta il campo esteso scritto, ed e' legale, mentre un
# Manaphy e un Darkrai che dichiarano la stessa versione lo portano nullo, e sono legali anch'essi.
# Il campo racconta dunque dove la carta e' stata riscossa, e le due forme convivono nel medesimo
# salvataggio senza che il verificatore obietti.
GIOCHI_DESTINAZIONE = {"dp": False, "pt": True, "hgss": True}

# La tabella personale da consultare, per versione di origine dichiarata dal modello.
TABELLA_DI_VERSIONE = {10: "personal_dp", 11: "personal_dp", 12: "personal_pt",
                       7: "personal_hgss", 8: "personal_hgss"}
DIM_PERSONALE = 0x2C
OFF_P_GENERE = 0x10
OFF_P_CORDIALITA = 0x12
OFF_P_ABILITA1 = 0x16
OFF_P_ABILITA2 = 0x17

# I magici del rapporto fra i generi, da PersonalInfo.
RAPPORTO_SOLO_MASCHI = 0
RAPPORTO_SOLO_FEMMINE = 254
RAPPORTO_ASESSUATO = 255

# I due generatori lineari congruenziali della quarta generazione, da LCRNG e ARNG.
LCRNG_MULT, LCRNG_ADD = 0x41C64E6D, 0x00006073
ARNG_MULT, ARNG_ADD = 0x6C078965, 0x00000001

# La data che si scrive come giorno di incontro. E' fissa e dichiarata invece che presa
# dall'orologio, perche' un lotto riproducibile non puo' dipendere da quando lo si produce.
DATA_INCONTRO = (2026, 9, 4)


def allenatore_del_progetto():
    percorso = os.path.join(RADICE, REGISTRO_ALLENATORE)
    if not os.path.exists(percorso):
        return None
    return json.load(io.open(percorso, encoding="utf-8"))


def e_cifrata(pk4):
    """Vero se la struttura e' nella forma cifrata, secondo il controllo della fonte."""
    return struct.unpack_from("<I", pk4, OFF_PROVA_CIFRATURA)[0] != 0


def somma_controllo(pk4):
    """La somma a sedici bit sulla parte di scatola, dal 0x08 in poi.

    E' la medesima famiglia di somme delle altre generazioni, e vale qui l'avvertenza gia'
    registrata: sommando parole non dipende dall'ordine dei blocchi, quindi non puo' rivelare una
    permutazione sbagliata. Chi la usasse come sola prova di una lettura si ingannerebbe.
    """
    somma = 0
    for i in range(0x08, DIM_PK4_SCATOLA, 2):
        somma = (somma + struct.unpack_from("<H", pk4, i)[0]) & 0xFFFF
    return somma


def leggi_personali(pkhex):
    """Le tabelle personali delle tre famiglie di quarta generazione, indicizzate per nome."""
    fuori = {}
    for nome in set(TABELLA_DI_VERSIONE.values()):
        percorso = os.path.join(pkhex, PERSONALI, nome)
        if not os.path.exists(percorso):
            return None, "manca la tabella personale " + nome
        fuori[nome] = io.open(percorso, "rb").read()
    return fuori, None


def voce_personale(personali, versione, specie):
    nome = TABELLA_DI_VERSIONE.get(versione)
    if nome is None:
        return None
    dati = personali[nome]
    inizio = specie * DIM_PERSONALE
    if inizio + DIM_PERSONALE > len(dati):
        return None
    return dati[inizio:inizio + DIM_PERSONALE]


def avanza_lcrng(seme):
    return (seme * LCRNG_MULT + LCRNG_ADD) & 0xFFFFFFFF


def avanza_arng(valore):
    return (valore * ARNG_MULT + ARNG_ADD) & 0xFFFFFFFF


def e_cromatico(pid, tid, sid):
    """La condizione di lucentezza della terza, quarta e quinta generazione.

    Si scrive per esteso perche' e' il vincolo che governa la composizione: un dono che dichiara di
    non essere cromatico deve restare tale rispetto agli identificativi che porta con se'.
    """
    return (tid ^ sid ^ (pid >> 16) ^ (pid & 0xFFFF)) < 8


def genere_da_pid(pid, rapporto):
    """Il genere che discende dal valore di personalita', da EntityGender."""
    if rapporto == RAPPORTO_ASESSUATO:
        return 2
    if rapporto == RAPPORTO_SOLO_FEMMINE:
        return 1
    if rapporto == RAPPORTO_SOLO_MASCHI:
        return 0
    return 1 if (pid & 0xFF) < rapporto else 0


def seme_della_voce(indice, pid_modello, tid, sid, sale):
    """Il seme deterministico di una voce, cosicche' due corse producano gli stessi byte."""
    chiave = "EVT-4|%d|%08X|%d|%d|%s" % (indice, pid_modello, tid, sid, sale)
    return struct.unpack("<I", hashlib.sha256(chiave.encode("utf-8")).digest()[:4])[0]


def componi_pid(seme, tid, sid, genere_voluto, rapporto, parita_voluta):
    """Compone un valore di personalita' che rispetti i tre vincoli del modello.

    Rifa' il procedimento di `PGT.GetPID`: si tira dal generatore lineare, e finche' il valore
    risulta cromatico lo si fa avanzare con il secondo generatore, che e' il modo in cui il gioco
    evitava di consegnare per sbaglio un esemplare cromatico a chi non doveva riceverlo. Ai due
    vincoli della fonte questo programma ne aggiunge un terzo, la parita', perche' in quarta
    generazione la casella di abilita' discende dalla parita' del valore e il modello dichiara gia'
    quale abilita' l'esemplare porti: un valore di parita' sbagliata produrrebbe un esemplare la cui
    abilita' non e' quella che il suo stesso valore impone.
    """
    for _ in range(1 << 20):
        seme = avanza_lcrng(seme)
        pid = seme
        for _ in range(64):
            if not e_cromatico(pid, tid, sid):
                break
            pid = avanza_arng(pid)
        else:
            continue
        if genere_da_pid(pid, rapporto) != genere_voluto:
            continue
        if parita_voluta is not None and (pid & 1) != parita_voluta:
            continue
        return pid
    return None


def componi_iv32(seme):
    """I trenta bit dei valori individuali, da ClassicEraRNG.GetSequentialIVs."""
    seme = avanza_lcrng(seme)
    primo = (seme >> 16) & 0x7FFF
    seme = avanza_lcrng(seme)
    secondo = (seme >> 16) & 0x7FFF
    return ((secondo << 15) | primo) & 0x3FFFFFFF


def leggi_doni(pkhex):
    """Le voci della base dei doni di quarta generazione, con il modello che contengono.

    Riferisce anche le voci che esemplari non sono, perche' contarle fra gli scarti senza dirlo
    darebbe l'impressione di una lettura parziale: la medesima base dati porta oggetti e altre
    consegne, e la loro presenza non e' un difetto.
    """
    percorso = os.path.join(pkhex, MGDB, "wc4.pkl")
    if not os.path.exists(percorso):
        return None, "manca wc4.pkl sotto " + os.path.join(pkhex, MGDB)
    personali, errore = leggi_personali(pkhex)
    if errore:
        return None, errore
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
        versione = pk4[OFF_VERSIONE]
        personale = voce_personale(personali, versione, specie)
        if personale is None:
            difettosi.append((indice, "nessuna tabella personale per la versione %d" % versione))
            continue
        iv32 = struct.unpack_from("<I", pk4, OFF_IV32)[0]
        pid = struct.unpack_from("<I", pk4, OFF_PID)[0]
        fuori.append({
            "indice": indice,
            "tipo": tipo,
            "cifrata": e_cifrata(pk4),
            "specie": specie,
            "pid": pid,
            "tid": struct.unpack_from("<H", pk4, OFF_TID)[0],
            "sid": struct.unpack_from("<H", pk4, OFF_SID)[0],
            "versione": versione,
            "lingua": pk4[OFF_LINGUA],
            "livello_incontro": pk4[OFF_LIVELLO_INCONTRO] & 0x7F,
            "palla": pk4[OFF_PALLA_HGSS] or pk4[OFF_PALLA_DPPT],
            "luogo_modello": struct.unpack_from("<H", pk4, OFF_UOVO_DP)[0],
            "iv_nulli": (iv32 & 0x3FFFFFFF) == 0,
            "pid_da_comporre": pid < 2,
            "checksum_memorizzato": struct.unpack_from("<H", pk4, OFF_CHECKSUM)[0],
            "checksum_calcolato": somma_controllo(pk4),
            "personale": personale,
            "byte": pk4,
        })
    return {"voci": fuori, "non_esemplari": non_esemplari, "difettosi": difettosi,
            "record": quante}, None


def consegna(v, allenatore, gioco="hgss"):
    """Applica al modello le mutazioni che la consegna avrebbe applicato, e restituisce i byte.

    Restituisce anche il resoconto di che cosa sia stato composto e che cosa conservato, perche' il
    pedigree deve poter dire di ciascun campo se venga dalla distribuzione o da noi.
    """
    pk4 = bytearray(v["byte"][:DIM_PK4_SCATOLA])
    resoconto = {"pid": "dal modello", "iv": "composti", "allenatore": "storico"}

    if allenatore and v["tid"] == 0 and v["sid"] == 0:
        struct.pack_into("<H", pk4, OFF_TID, allenatore["tid"] & 0xFFFF)
        struct.pack_into("<H", pk4, OFF_SID, allenatore["sid"] & 0xFFFF)
        resoconto["allenatore"] = "del progetto"
    tid = struct.unpack_from("<H", pk4, OFF_TID)[0]
    sid = struct.unpack_from("<H", pk4, OFF_SID)[0]

    # Il campo di integrita' formale: la fonte lo azzera per il solo dono storico che lo porta
    # diverso da zero, e azzerarlo sempre e' quindi conforme e innocuo.
    struct.pack_into("<H", pk4, OFF_SANITA, 0)

    # Lo spostamento del luogo, che e' la mutazione che il primo lotto non faceva.
    luogo = (v["luogo_modello"] + SCOSTAMENTO_LUOGO) & 0xFFFF
    struct.pack_into("<H", pk4, OFF_INCONTRO_DP, luogo)
    esteso = luogo if GIOCHI_DESTINAZIONE[gioco] else 0
    struct.pack_into("<H", pk4, OFF_INCONTRO_ESTESO, esteso)
    struct.pack_into("<H", pk4, OFF_UOVO_DP, 0)
    struct.pack_into("<H", pk4, OFF_UOVO_ESTESO, 0)

    # La data di incontro, e l'azzeramento di quella dell'uovo.
    anno, mese, giorno = DATA_INCONTRO
    pk4[OFF_INCONTRO_ANNO] = (anno - 2000) & 0xFF
    pk4[OFF_INCONTRO_ANNO + 1] = mese
    pk4[OFF_INCONTRO_ANNO + 2] = giorno
    pk4[OFF_UOVO_ANNO] = 0
    pk4[OFF_UOVO_ANNO + 1] = 0
    pk4[OFF_UOVO_ANNO + 2] = 0

    # La cordialita' al valore base della specie, come fa la consegna.
    pk4[OFF_CORDIALITA] = v["personale"][OFF_P_CORDIALITA]

    # Il valore di personalita': si conserva se il modello ne dichiara uno, si compone se il
    # modello porta l'ordine di comporlo.
    if v["pid_da_comporre"]:
        rapporto = v["personale"][OFF_P_GENERE]
        genere = (pk4[OFF_FLAG_GENERE] >> 1) & 3
        ab1 = v["personale"][OFF_P_ABILITA1]
        ab2 = v["personale"][OFF_P_ABILITA2]
        parita = None
        if ab1 != ab2:
            parita = 0 if pk4[OFF_ABILITA] == ab1 else (1 if pk4[OFF_ABILITA] == ab2 else None)
        pid = componi_pid(seme_della_voce(v["indice"], v["pid"], tid, sid, "pid"),
                          tid, sid, genere, rapporto, parita)
        if pid is None:
            return None, {"errore": "nessun valore di personalita' soddisfa i vincoli"}
        struct.pack_into("<I", pk4, OFF_PID, pid)
        resoconto["pid"] = "composto"

    # I valori individuali, da un seme indipendente perche' la coppia non deve avere correlazione.
    iv32 = struct.unpack_from("<I", pk4, OFF_IV32)[0]
    if (iv32 & 0x3FFFFFFF) == 0:
        nuovi = componi_iv32(seme_della_voce(v["indice"], v["pid"], tid, sid, "iv"))
        iv32 = (iv32 & 0xC0000000) | nuovi
    else:
        resoconto["iv"] = "dal modello"

    # Il contrassegno di uovo si spegne: questi doni non sono uova.
    struct.pack_into("<I", pk4, OFF_IV32, iv32 & ~0x40000000)

    struct.pack_into("<H", pk4, OFF_CHECKSUM, somma_controllo(pk4))
    return bytes(pk4), resoconto


def scrivi_lotto(voci, destinazione, allenatore, gioco="hgss"):
    """Scrive un file per esemplare nella forma di scatola, che e' quella che il verificatore apre.

    Accanto ai file scrive un manifesto con l'impronta di ciascuno, che e' la sola riga del pedigree
    a venire dal disco invece che dal ricalcolo: nessun ricalcolo puo' dimostrare che un file
    esista.
    """
    if not os.path.isdir(destinazione):
        os.makedirs(destinazione)
    impronte, scritti, nostri, composti, rifiutati = {}, 0, 0, 0, []
    for v in voci:
        pk4, resoconto = consegna(v, allenatore, gioco)
        if pk4 is None:
            rifiutati.append((v["indice"], resoconto["errore"]))
            continue
        nostro = resoconto["allenatore"] == "del progetto"
        nostri += 1 if nostro else 0
        composti += 1 if resoconto["pid"] == "composto" else 0
        nome = "EVT-4-%04d-%03d%s.pk4" % (v["indice"], v["specie"], "-nostro" if nostro else "")
        io.open(os.path.join(destinazione, nome), "wb").write(pk4)
        impronte[nome] = {"sha256": hashlib.sha256(pk4).hexdigest(),
                          "specie": v["specie"], "versione": v["versione"],
                          "pid": resoconto["pid"], "iv": resoconto["iv"],
                          "allenatore": resoconto["allenatore"]}
        scritti += 1
    io.open(os.path.join(destinazione, "impronte.json"), "w", encoding="utf-8").write(
        json.dumps({"data_incontro": "%04d-%02d-%02d" % DATA_INCONTRO,
                    "gioco_che_riceve": gioco,
                    "scostamento_luogo": SCOSTAMENTO_LUOGO,
                    "voci": impronte}, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return scritti, nostri, composti, rifiutati


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

    # I tre luoghi che l'ancoraggio esterno ha fissato: sono i valori letti dai byte di esemplari
    # veri e riconosciuti legali dentro il salvataggio di Argento SoulSilver, e sono l'unica prova
    # possibile della somma, che nessun controllo interno potrebbe stabilire.
    prova("evento Pokemon", 3060, 60 + SCOSTAMENTO_LUOGO)
    prova("dono Wi-Fi", 3073, 73 + SCOSTAMENTO_LUOGO)
    prova("Pokemon Ranger", 3001, 1 + SCOSTAMENTO_LUOGO)
    prova("Diamante e Perla non scrivono il campo esteso", False, GIOCHI_DESTINAZIONE["dp"])
    prova("Platino e HGSS lo scrivono", [True, True],
          [GIOCHI_DESTINAZIONE["pt"], GIOCHI_DESTINAZIONE["hgss"]])

    # La lucentezza non guarda quale sia il valore ma soltanto lo scarto della sua parola alta con
    # quella bassa e con gli identificativi.
    prova("una coppia con scarto nullo e' cromatica", True, e_cromatico(0x00010001, 0, 0))
    prova("una coppia con scarto otto non lo e'", False, e_cromatico(0x00080000, 0, 0))
    prova("gli identificativi entrano nella condizione", True, e_cromatico(0x00080000, 8, 0))

    # Il genere che discende dal valore, e i tre rapporti magici.
    prova("asessuato", 2, genere_da_pid(0x12345678, RAPPORTO_ASESSUATO))
    prova("solo femmine", 1, genere_da_pid(0x12345678, RAPPORTO_SOLO_FEMMINE))
    prova("solo maschi", 0, genere_da_pid(0x12345678, RAPPORTO_SOLO_MASCHI))
    prova("sotto la soglia e' femmina", 1, genere_da_pid(0x00000010, 31))
    prova("sopra la soglia e' maschio", 0, genere_da_pid(0x000000FF, 31))

    # La composizione rispetta i tre vincoli, e li si verifica uno per uno perche' il fallimento di
    # uno solo non sarebbe visibile guardando il valore prodotto.
    pid = componi_pid(seme_della_voce(1, 1, 1000, 2000, "prova"), 1000, 2000, 0, 31, 1)
    prova("il valore composto non e' cromatico", False, e_cromatico(pid, 1000, 2000))
    prova("il valore composto ha il genere voluto", 0, genere_da_pid(pid, 31))
    prova("il valore composto ha la parita' voluta", 1, pid & 1)
    prova("la composizione e' deterministica", pid,
          componi_pid(seme_della_voce(1, 1, 1000, 2000, "prova"), 1000, 2000, 0, 31, 1))

    # I valori individuali stanno nei trenta bit e non toccano i due contrassegni.
    iv = componi_iv32(seme_della_voce(1, 1, 1000, 2000, "iv"))
    prova("i valori individuali stanno in trenta bit", 0, iv >> 30)
    prova("nessuna delle sei statistiche supera trentuno", True,
          all(((iv >> (5 * k)) & 31) <= 31 for k in range(6)))

    # I due semi di una stessa voce sono diversi, che e' la condizione perche' la coppia non abbia
    # correlazione: comporli dal medesimo seme produrrebbe la correlazione del primo metodo.
    prova("i due semi di una voce sono distinti", True,
          seme_della_voce(1, 1, 1, 1, "pid") != seme_della_voce(1, 1, 1, 1, "iv"))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", help="clone del verificatore")
    ap.add_argument("--lotto", help="cartella in cui scrivere gli esemplari")
    ap.add_argument("--gioco", choices=sorted(GIOCHI_DESTINAZIONE), default="hgss",
                    help="il gioco su cui la consegna si intende riscossa, che decide il campo "
                         "esteso del luogo di incontro")
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
    print("")
    print("  Quanto del modello e' esemplare, e quanto va composto:")
    print("  con i valori individuali a zero           %5d su %d" %
          (sum(1 for v in voci if v["iv_nulli"]), len(voci)))
    print("  con il valore di personalita' da comporre %5d su %d" %
          (sum(1 for v in voci if v["pid_da_comporre"]), len(voci)))
    print("  con gli identificativi a zero             %5d" %
          sum(1 for v in voci if v["tid"] == 0 and v["sid"] == 0))
    luoghi = {}
    for v in voci:
        chiave = v["luogo_modello"] + SCOSTAMENTO_LUOGO
        luoghi[chiave] = luoghi.get(chiave, 0) + 1
    print("")
    print("  luoghi di incontro dopo la consegna: "
          + ", ".join("%d su %d voci" % (k, n)
                      for k, n in sorted(luoghi.items(), key=lambda x: -x[1])))
    print("  specie distinte                     %5d" % len({v["specie"] for v in voci}))
    if esito["difettosi"]:
        print("")
        for indice, ragione in esito["difettosi"][:10]:
            print("  difetto: voce %d: %s" % (indice, ragione))
    if a.lotto:
        allenatore = allenatore_del_progetto()
        scritti, nostri, composti, rifiutati = scrivi_lotto(voci, a.lotto, allenatore, a.gioco)
        print("")
        print("  scritti %d file in %s" % (scritti, a.lotto))
        print("  di cui con l'allenatore del progetto %d, con il valore di personalita' composto %d"
              % (nostri, composti))
        for indice, ragione in rifiutati:
            print("  rifiutata la voce %d: %s" % (indice, ragione))
        print("  Il passo seguente non e' di questo programma: si aprono con il verificatore nel")
        print("  contesto della quarta generazione e si legge che cosa esso obietti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
