#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Identifica e verifica un salvataggio di provenienza esterna, e ne censisce il contenuto.

Perché esiste
-------------
Un salvataggio scaricato da terzi pone tre domande distinte, e confonderle è il modo tipico di
sbagliare. La prima è se il file sia strutturalmente un salvataggio funzionante del gioco che
dichiara di essere. La seconda è che cosa contenga, cioè quali esemplari e quindi quali specie
porterebbe. La terza è se sia lecito usarlo, che è una questione di perimetro e non di byte.

Questo programma risponde alle prime due e si astiene deliberatamente dalla terza, che sta in
`.claude/rules/hardware-and-perimeter.md` e si decide per ADR, non per strumento.

Sul pericolo, una precisazione che vale scrivere perché la rassicurazione comune è quella
sbagliata. Un salvataggio è dato e non codice: non si esegue, quindi non può contenere un
programma dannoso nel senso in cui lo contiene un allegato eseguibile, e un esito pulito di un
antivirus su questi file non dice nulla di interessante perché non c'era nulla da trovare. I
rischi reali sono altri tre. Il primo è un file malformato che il gioco rifiuta all'avvio, o che
accetta e poi corrompe: si esclude verificando le somme di controllo, che è ciò che questo
programma fa. Il secondo è un esemplare costruito per innescare un difetto del gioco, cioè le
cosiddette Uova Peste e i loro parenti, e si riconosce dai campi incoerenti: qui si censisce e si
segnala ciò che non torna, senza pretendere di essere un verificatore di legittimità, che è
PKHeX. Il terzo non è tecnico ed è il più importante: usare esemplari di altri sul proprio
account, che è precisamente la questione di perimetro di cui sopra.

Il metodo di identificazione
----------------------------
Non si indovina il gioco dal nome del file. La dimensione restringe la famiglia, e dentro la
famiglia si prova ciascun candidato con il predicato che la fonte usa per distinguerli,
riferendo quale ha risposto e quali no. Tutti i predicati impiegati qui sono letti dal sorgente
di PKHeX il 2026-09-02, `PKHeX.Core/Saves/Util/SaveUtil.cs` e i file che vi sono richiamati, e
ciascuno porta accanto il riferimento: un predicato inventato che per caso funzioni su un file
è indistinguibile da uno giusto, e la differenza si vede solo sul file successivo.

Uso
---
    python tools/verifica-salvataggi.py _notes/salvataggi
    python tools/verifica-salvataggi.py _notes/salvataggi --censimento --ace <clone> --pkhex <clone>
    python tools/verifica-salvataggi.py _notes/salvataggi --json esito.json
    python tools/verifica-salvataggi.py --self-test
"""

import argparse
import io
import json
import os
import struct
import sys
import zipfile

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))
sys.path.insert(0, os.path.join(RADICE, "tools"))

# ---------------------------------------------------------------------------------------------
# Dimensioni note, dal sorgente della fonte
# ---------------------------------------------------------------------------------------------
# PKHeX.Core/Saves/Util/SaveUtil.cs, costanti SIZE_*. Le riportiamo con il nome originale
# accanto, cosicche' un confronto con la fonte sia una ricerca e non una traduzione.
SIZE_G1RAW = 0x8000        # 32768   Gen 1, prima generazione su Game Boy
SIZE_G2RAW_U = 0x8000      # 32768   Gen 2 internazionale, stessa dimensione di Gen 1
SIZE_G2RAW_J = 0x10000     # 65536   Gen 2 giapponese
SIZE_G3RAW = 0x20000       # 131072  Gen 3 su Game Boy Advance
SIZE_G3RAWHALF = 0x10000   # 65536   mezzo salvataggio Gen 3
SIZE_G4RAW = 0x80000       # 524288  Gen 4 e Gen 5 su Nintendo DS
SIZE_G3BOX = 0x76000       # 483328  Pokemon Box Rubino e Zaffiro, su GameCube
SIZE_G6XY = 0x65600        # 415232  Gen 6 X e Y
SIZE_G6ORAS = 0x76000      # 483328  Gen 6 Rubino Omega e Zaffiro Alpha
SIZE_G7SM = 0x6BE00        # 442880  Gen 7 Sole e Luna
SIZE_G7USUM = 0x6CC00      # 445440  Gen 7 UltraSole e UltraLuna

# Gen 4: dimensione del blocco generale per gioco, da SAV4DP/SAV4Pt/SAV4HGSS, campo GeneralSize.
GEN4_BLOCCO_GENERALE = (
    ("Diamante o Perla", 0xC100),
    ("Platino", 0xCF2C),
    ("Oro HeartGold o Argento SoulSilver", 0xF628),
)
GEN4_PARTIZIONE = 0x40000
GEN4_MAGIA_GIAPPONE_INTL = 0x20060623   # SAV4.MAGIC_JAPAN_INTL
GEN4_MAGIA_COREA = 0x20070903           # SAV4.MAGIC_KOREAN

# Gen 5: (nome, dimensione della parte principale, lunghezza dell'area su cui gira il CRC).
# Da SaveUtil.IsG5BW e IsG5B2W2, che passano SIZE_G5BW con 0x8C e SIZE_G5B2W2 con 0x94.
GEN5_CANDIDATI = (
    ("Bianco o Nero", 0x24000, 0x8C),
    ("Bianco 2 o Nero 2", 0x26000, 0x94),
)

# Gen 6 e 7: (nome, dimensione). La verifica e' la firma di coda comune, HasSaveFooterBEEF.
TRE_DS_CANDIDATI = (
    ("X o Y", SIZE_G6XY),
    ("Rubino Omega o Zaffiro Alpha", SIZE_G6ORAS),
    ("Sole o Luna", SIZE_G7SM),
    ("UltraSole o UltraLuna", SIZE_G7USUM),
)
TRE_DS_FIRMA = 0x42454546   # SaveUtil.HasSaveFooterBEEF, u32 letto a lunghezza meno 0x1F0

# Gen 3: piede di sezione, da include/save.h di pokeemerald e da SAV3 di PKHeX.
SEZIONE_DIM = 4096
SEZIONE_DATI = 3968
SEZIONI_PER_SLOT = 14
SEZIONE_FIRMA = 0x08012025
OFF_SEZIONE_ID = 0x0FF4
OFF_SEZIONE_CHECKSUM = 0x0FF6
OFF_SEZIONE_FIRMA = 0x0FF8
OFF_SEZIONE_CONTATORE = 0x0FFC

# Gen 3: offset del blocco piccolo, cioe' la sezione con identificativo zero. Da
# PKHeX.Core/Saves/Blocks/Gen3/SaveBlock3SmallE.cs, e comuni ai tre giochi.
OFF_OT_NOME = 0x00
LUN_OT_NOME = 8
OFF_OT_SESSO = 0x08
OFF_OT_TID = 0x0A
OFF_OT_SID = 0x0C
OFF_ORE = 0x0E
OFF_MINUTI = 0x10

# Gen 3: deposito. Da SAV3.GetBoxOffset, che vale 4 + 80 * box * 30, quindi quattro byte di
# scatola corrente e poi le quattordici scatole da trenta posizioni.
DEPOSITO_PRIMA_SEZIONE = 5
DEPOSITO_ULTIMA_SEZIONE = 13
DEPOSITO_OFF_SCATOLE = 4
SCATOLE = 14
POSIZIONI_PER_SCATOLA = 30
STRUTTURA_BOX = 80

# Gen 1: le due liste di Pokemon che la fonte usa per distinguere il formato, da
# SaveUtil.IsG1INT e IsG1JPN. La prova e' che il contatore non superi il massimo e che il byte
# subito dopo la lista degli identificativi sia il terminatore 0xFF.
GEN1_CANDIDATI = (
    ("internazionale", 0x2F2C, 0x30C0, 20),
    ("giapponese", 0x2ED5, 0x302D, 30),
)
# SAV1.IsYellowINT e IsYellowJPN: (offset dello starter, offset dell'affetto iniziale).
GEN1_GIALLA = {"internazionale": (0x29C3, 0x271C), "giapponese": (0x29B9, 0x2712)}
GEN1_PIKACHU = 0x54
# Il checksum principale, dalla sezione 4 della referenza del progetto: complemento a uno della
# somma dei byte da 0x2598 a 0x3522, memorizzato a 0x3523. Vale per le versioni internazionali;
# per quelle giapponesi gli offset non sono verificati in questo progetto e non si inventano.
GEN1_CHECKSUM_DA = 0x2598
GEN1_CHECKSUM_A = 0x3523
GEN1_CHECKSUM_OFF = 0x3523

# Gen 2: le stesse liste, da SaveUtil. Servono a non confondere un salvataggio Gen 2
# internazionale con uno Gen 1, che hanno la medesima dimensione.
GEN2_CANDIDATI = (
    ("Oro o Argento internazionale", 0x288A, 0x2D6C, 20),
    ("Cristallo internazionale", 0x2865, 0x2D10, 20),
    ("Oro o Argento giapponese", 0x2D10, 0x283E, 30),
    ("Cristallo giapponese", 0x2D10, 0x281A, 30),
    ("Oro o Argento coreano", 0x2DAE, 0x28CC, 20),
)

# GameCube: intestazione di un file di scheda di memoria, cioe' il formato .gci. Sono 0x40 byte
# davanti al contenuto, e i primi quattro sono il codice del gioco.
GCI_INTESTAZIONE = 0x40


def u16(b, off):
    return struct.unpack_from("<H", b, off)[0]


def u32(b, off):
    return struct.unpack_from("<I", b, off)[0]


def u32be(b, off):
    return struct.unpack_from(">I", b, off)[0]


def crc16_ccitt(dati):
    """Il CRC a sedici bit usato dai salvataggi di quarta e quinta generazione.

    Trascritto da PKHeX.Core/Saves/Util/Checksums.cs, metodo CRC16_CCITT. Non e' il CRC16 con
    tabella che sta nello stesso file: sono due funzioni diverse nella medesima fonte, e usare
    l'una al posto dell'altra produce un rifiuto su ogni file, che e' il modo in cui questo
    errore si scopre.
    """
    alto, basso = 0xFF, 0xFF
    for b in dati:
        x = b ^ alto
        x ^= (x >> 4)
        alto = (basso ^ (x >> 3) ^ (x << 4)) & 0xFF
        basso = (x ^ (x << 5)) & 0xFF
    return ((alto << 8) | basso) & 0xFFFF


def somma16_be_invertita(dati):
    """La somma di controllo di Pokemon Box, da Checksums.CheckSum16BigInvert.

    Somma parole da sedici bit lette in ordine di byte inverso, e restituisce nella parte alta
    la somma e nella parte bassa la differenza fra 0xF004 e la somma.
    """
    chk = 0
    for i in range(0, len(dati) - 1, 2):
        chk = (chk + struct.unpack_from(">H", dati, i)[0]) & 0xFFFFFFFF
    chk &= 0xFFFF
    return ((chk << 16) | ((0xF004 - chk) & 0xFFFF)) & 0xFFFFFFFF


# ---------------------------------------------------------------------------------------------
# Generazione 3
# ---------------------------------------------------------------------------------------------

def checksum_sezione(sezione):
    """Il checksum di una sezione, e la lunghezza del prefisso che lo riproduce.

    Il gioco calcola il checksum su una lunghezza che dipende dal sizeof delle strutture di
    salvataggio, e quel numero non e' ricavabile da qui senza compilare. Invece di indovinarlo si
    cerca quale prefisso di parole da trentadue bit riproduce il valore memorizzato, che e' la
    stessa strada dello strumento dello zaino di questo progetto.
    """
    memorizzato = u16(sezione, OFF_SEZIONE_CHECKSUM)
    corrente = 0
    trovato = None
    for i in range(SEZIONE_DATI // 4):
        corrente = (corrente + u32(sezione, i * 4)) & 0xFFFFFFFF
        ripiegato = ((corrente >> 16) + corrente) & 0xFFFF
        if ripiegato == memorizzato:
            trovato = (i + 1) * 4
            if trovato == SEZIONE_DATI:
                break
    return memorizzato, trovato


def leggi_slot_gen3(dati, slot):
    base = slot * SEZIONI_PER_SLOT * SEZIONE_DIM
    sezioni, difetti, contatori = {}, [], set()
    for n in range(SEZIONI_PER_SLOT):
        off = base + n * SEZIONE_DIM
        grezzo = dati[off:off + SEZIONE_DIM]
        if len(grezzo) < SEZIONE_DIM:
            difetti.append((n, "sezione troncata"))
            continue
        if u32(grezzo, OFF_SEZIONE_FIRMA) != SEZIONE_FIRMA:
            difetti.append((n, "firma assente"))
            continue
        _memorizzato, lunghezza = checksum_sezione(grezzo)
        if lunghezza is None:
            difetti.append((n, "checksum non riproducibile su alcun prefisso"))
            continue
        sec_id = u16(grezzo, OFF_SEZIONE_ID)
        contatori.add(u32(grezzo, OFF_SEZIONE_CONTATORE))
        sezioni[sec_id] = {"posizione": n, "dati": grezzo[:SEZIONE_DATI],
                           "lunghezza_checksum": lunghezza}
    return {"sezioni": sezioni, "difetti": difetti,
            "contatore": max(contatori) if contatori else None}


def versione_gen3(piccolo):
    """Il gioco, dal valore a 0xAC del blocco piccolo, da SaveUtil.GetVersionG3SAV.

    Il criterio della fonte e' che a quell'offset Rosso Fuoco e Verde Foglia tengono un valore
    fisso pari a uno, Rubino e Zaffiro i dati della Torre Lotta, e Smeraldo la chiave di
    cifratura; e che, quando il valore non e' ne uno ne zero, si distingue Smeraldo da Rubino e
    Zaffiro guardando se ci sia dato oltre 0x890, che e' dove la struttura di quei due finisce.
    """
    valore = u32(piccolo, 0xAC)
    if valore == 1:
        return "Rosso Fuoco o Verde Foglia"
    if valore == 0:
        return "Rubino o Zaffiro, senza dati della Torre Lotta"
    resto = piccolo[0x890:0xF2C]
    if any(b != 0 for b in resto):
        return "Smeraldo"
    return "Rubino o Zaffiro"


def nome_gen3(byte_nome, tabella):
    if tabella is None:
        return None
    try:
        return tabella.decode(byte_nome).rstrip()
    except Exception:
        return None


def censisci_deposito_gen3(slot, gen3):
    """Il censimento del deposito: quante posizioni occupate, quali specie, quante cromatiche.

    Il conto delle posizioni occupate non si fa sul byte della specie ma sul bit che il gioco
    usa per dire che la posizione ha un contenuto, perche' una posizione vuota non e' azzerata in
    ogni suo byte e contarla per specie diversa da zero conta anche i residui.
    """
    sezioni = slot["sezioni"]
    parti = []
    for sec_id in range(DEPOSITO_PRIMA_SEZIONE, DEPOSITO_ULTIMA_SEZIONE + 1):
        if sec_id not in sezioni:
            return None
        parti.append(sezioni[sec_id]["dati"])
    deposito = b"".join(parti)

    occupate, uova, cromatici, difettosi = 0, 0, 0, 0
    specie = {}
    per_scatola = []
    for scatola in range(SCATOLE):
        conto = 0
        for posizione in range(POSIZIONI_PER_SCATOLA):
            off = (DEPOSITO_OFF_SCATOLE
                   + STRUTTURA_BOX * (scatola * POSIZIONI_PER_SCATOLA + posizione))
            grezzo = deposito[off:off + STRUTTURA_BOX]
            if len(grezzo) < STRUTTURA_BOX:
                continue
            try:
                mon = gen3.Gen3Mon.from_bytes(grezzo, party=False)
            except Exception:
                difettosi += 1
                continue
            if not mon.has_species:
                continue
            occupate += 1
            conto += 1
            if mon.is_bad_egg:
                difettosi += 1
            if mon.is_egg:
                uova += 1
            if mon.is_shiny:
                cromatici += 1
            interno = mon.growth.species
            specie[interno] = specie.get(interno, 0) + 1
        per_scatola.append(conto)
    return {"occupate": occupate, "uova": uova, "cromatici": cromatici,
            "difettosi": difettosi, "specie": specie, "per_scatola": per_scatola}


def analizza_gen3(dati, gen3, tabella, censimento):
    esito = {"famiglia": "Gen 3 su Game Boy Advance"}
    slot_a = leggi_slot_gen3(dati, 0)
    slot_b = leggi_slot_gen3(dati, 1)
    valide = (len(slot_a["sezioni"]), len(slot_b["sezioni"]))
    esito["sezioni_valide"] = {"slot A": valide[0], "slot B": valide[1]}
    esito["difetti"] = {"slot A": slot_a["difetti"], "slot B": slot_b["difetti"]}

    scelto = None
    if valide[0] == SEZIONI_PER_SLOT and valide[1] == SEZIONI_PER_SLOT:
        scelto = slot_a if (slot_a["contatore"] or 0) >= (slot_b["contatore"] or 0) else slot_b
        esito["slot_attivo"] = "A" if scelto is slot_a else "B"
    elif valide[0] == SEZIONI_PER_SLOT:
        scelto, esito["slot_attivo"] = slot_a, "A, il solo completo"
    elif valide[1] == SEZIONI_PER_SLOT:
        scelto, esito["slot_attivo"] = slot_b, "B, il solo completo"
    else:
        esito["valido"] = False
        esito["ragione"] = ("nessuno dei due slot ha tutte e quattordici le sezioni valide, "
                           "quindi il file non e' un salvataggio Gen 3 leggibile")
        return esito

    esito["valido"] = True
    esito["contatore_salvataggi"] = scelto["contatore"]
    piccolo = scelto["sezioni"][0]["dati"]
    esito["gioco"] = versione_gen3(piccolo)
    esito["allenatore"] = {
        "nome": nome_gen3(piccolo[OFF_OT_NOME:OFF_OT_NOME + LUN_OT_NOME], tabella),
        "sesso": "femmina" if piccolo[OFF_OT_SESSO] else "maschio",
        "id_visibile": u16(piccolo, OFF_OT_TID),
        "id_segreto": u16(piccolo, OFF_OT_SID),
        "ore_di_gioco": u16(piccolo, OFF_ORE),
        "minuti": piccolo[OFF_MINUTI],
    }
    if censimento:
        esito["deposito"] = censisci_deposito_gen3(scelto, gen3)
    return esito


# ---------------------------------------------------------------------------------------------
# Generazione 1 e 2
# ---------------------------------------------------------------------------------------------

def lista_valida_g12(dati, off, massimo):
    """Il predicato della fonte, SaveUtil.IsListValidG12: contatore entro il massimo, e
    terminatore 0xFF subito dopo la lista degli identificativi di specie."""
    if off + 1 + massimo >= len(dati):
        return False
    conto = dati[off]
    return conto <= massimo and dati[off + 1 + conto] == 0xFF


def analizza_gen12(dati):
    esito = {"famiglia": "Gen 1 o Gen 2 su Game Boy", "candidati": []}
    trovato = None
    for nome, off1, off2, massimo in GEN1_CANDIDATI:
        ok = lista_valida_g12(dati, off1, massimo) and lista_valida_g12(dati, off2, massimo)
        esito["candidati"].append(("Gen 1 " + nome, ok))
        if ok and trovato is None:
            trovato = ("Gen 1", nome)
    for nome, off1, off2, massimo in GEN2_CANDIDATI:
        ok = lista_valida_g12(dati, off1, massimo) and lista_valida_g12(dati, off2, massimo)
        esito["candidati"].append(("Gen 2 " + nome, ok))
        if ok and trovato is None:
            trovato = ("Gen 2", nome)
    if trovato is None:
        esito["valido"] = False
        esito["ragione"] = ("nessuno dei predicati di prima e seconda generazione riconosce "
                            "questo file: le due liste di Pokemon non hanno ne un contatore "
                            "plausibile ne il terminatore atteso")
        return esito

    esito["valido"] = True
    esito["generazione"], esito["formato"] = trovato
    if trovato[0] == "Gen 1":
        off_starter, off_affetto = GEN1_GIALLA[trovato[1]]
        starter = dati[off_starter]
        gialla = (starter == GEN1_PIKACHU) if starter != 0 else (dati[off_affetto] != 0)
        esito["gioco"] = "Giallo" if gialla else "Rosso, Verde o Blu"
        if trovato[1] == "internazionale":
            somma = sum(dati[GEN1_CHECKSUM_DA:GEN1_CHECKSUM_A]) & 0xFF
            esito["checksum"] = {
                "memorizzato": dati[GEN1_CHECKSUM_OFF],
                "calcolato": (0xFF - somma) & 0xFF,
                "torna": dati[GEN1_CHECKSUM_OFF] == ((0xFF - somma) & 0xFF),
            }
        else:
            esito["checksum"] = {
                "non_verificato": "gli offset del checksum di una versione giapponese di prima "
                                  "generazione non sono verificati in questo progetto, e non si "
                                  "inventano: resta il riconoscimento del formato, che poggia su "
                                  "due strutture indipendenti"}
    return esito


# ---------------------------------------------------------------------------------------------
# Generazione 4 e 5
# ---------------------------------------------------------------------------------------------

def analizza_nds(dati):
    """Prova i cinque candidati di quarta e quinta generazione e riferisce il confronto.

    I predicati vengono dalla fonte. Per la quarta si guarda la seconda partizione, perche' il
    primo salvataggio si scrive nella meta' alta del binario, e nel piede del blocco generale si
    controlla che il campo della dimensione coincida con la dimensione del blocco e che la
    parola seguente sia una delle due magie note. Per la quinta si verifica il CRC del piede.
    """
    esito = {"famiglia": "Gen 4 o Gen 5 su Nintendo DS", "candidati": []}
    trovato = None

    for nome, lunghezza in GEN4_BLOCCO_GENERALE:
        base = GEN4_PARTIZIONE
        if base + lunghezza > len(dati):
            esito["candidati"].append(("Gen 4 " + nome, False))
            continue
        generale = dati[base:base + lunghezza]
        dimensione = u32(generale, lunghezza - 0xC)
        magia = u32(generale, lunghezza - 0x8)
        ok = (dimensione == lunghezza
              and magia in (GEN4_MAGIA_GIAPPONE_INTL, GEN4_MAGIA_COREA))
        esito["candidati"].append(("Gen 4 " + nome, ok))
        if ok and trovato is None:
            trovato = ("Gen 4", nome,
                       "coreano" if magia == GEN4_MAGIA_COREA else "giapponese o internazionale")

    for nome, principale, lunghezza_crc in GEN5_CANDIDATI:
        inizio = principale - 0x100
        piede = dati[inizio:inizio + lunghezza_crc + 0x10]
        if len(piede) < lunghezza_crc + 0x10:
            esito["candidati"].append(("Gen 5 " + nome, False))
            continue
        memorizzato = u16(piede, len(piede) - 2)
        calcolato = crc16_ccitt(piede[:lunghezza_crc])
        ok = memorizzato == calcolato
        esito["candidati"].append(("Gen 5 " + nome, ok))
        if ok and trovato is None:
            trovato = ("Gen 5", nome, None)

    if trovato is None:
        esito["valido"] = False
        esito["ragione"] = ("nessuno dei cinque candidati risponde: il piede del blocco "
                            "generale non torna per Diamante e Perla, Platino ne HeartGold e "
                            "SoulSilver, e il CRC del piede non torna per Bianco e Nero ne per "
                            "i loro seguiti")
        return esito
    esito["valido"] = True
    esito["generazione"], esito["gioco"], esito["localizzazione"] = trovato
    return esito


# ---------------------------------------------------------------------------------------------
# Generazione 6 e 7, e Pokemon Box
# ---------------------------------------------------------------------------------------------

def analizza_tre_ds(dati):
    """La firma di coda comune ai salvataggi decifrati di Nintendo 3DS, HasSaveFooterBEEF.

    La dimensione da sola identifica il titolo, con una ambiguita' che va detta: Rubino Omega e
    Zaffiro Alpha hanno esattamente la dimensione di Pokemon Box su GameCube, e i due si
    distinguono perche' il secondo arriva dentro un file di scheda di memoria con la propria
    intestazione. Qui si vede la firma, che il file GameCube non ha.
    """
    esito = {"famiglia": "salvataggio decifrato di Nintendo 3DS"}
    nomi = [n for n, dim in TRE_DS_CANDIDATI if dim == len(dati)]
    if len(dati) < 0x1F0:
        esito["valido"] = False
        esito["ragione"] = "file troppo corto per contenere la firma di coda"
        return esito
    firma = u32(dati, len(dati) - 0x1F0)
    esito["firma_di_coda"] = "0x%08X" % firma
    esito["firma_attesa"] = "0x%08X" % TRE_DS_FIRMA
    esito["valido"] = firma == TRE_DS_FIRMA and bool(nomi)
    esito["gioco"] = nomi[0] if nomi else "dimensione non fra quelle note"
    if not esito["valido"]:
        esito["ragione"] = ("la firma di coda non e' quella attesa"
                            if firma != TRE_DS_FIRMA else
                            "la dimensione non corrisponde a nessun titolo noto")
    return esito


def analizza_box_gc(dati):
    """Pokemon Box Rubino e Zaffiro, dentro un file di scheda di memoria GameCube.

    Il predicato della fonte, SaveUtil.IsG3RSBox, verifica la prima somma di controllo: a 0x2000
    stanno quattro byte di somma memorizzata in ordine di byte diretto, e la somma si calcola sui
    0x1FF8 byte che seguono.
    """
    esito = {"famiglia": "Pokemon Box Rubino e Zaffiro, su GameCube"}
    if len(dati) == SIZE_G3BOX + GCI_INTESTAZIONE:
        esito["intestazione_gci"] = True
        esito["codice_gioco"] = dati[:4].decode("ascii", "replace")
        corpo = dati[GCI_INTESTAZIONE:]
    elif len(dati) == SIZE_G3BOX:
        esito["intestazione_gci"] = False
        corpo = dati
    else:
        esito["valido"] = False
        esito["ragione"] = "dimensione non compatibile con Pokemon Box, con o senza intestazione"
        return esito

    off = 0x2000
    span = corpo[off:off + 0x1FFC]
    memorizzato = u32be(span, 0)
    calcolato = somma16_be_invertita(span[4:])
    esito["somma_memorizzata"] = "0x%08X" % memorizzato
    esito["somma_calcolata"] = "0x%08X" % calcolato
    esito["valido"] = memorizzato == calcolato
    if not esito["valido"]:
        esito["ragione"] = "la prima somma di controllo non torna"
    return esito, corpo


# Pokemon Box: la disposizione del deposito. Da SAV3RSBox e BlockInfoRSBOX, letti il 2026-09-04.
# Il file porta due salvataggi da ventitre blocchi di 0x2000 byte a partire da 0x2000, e quello
# valido e' l'insieme dei ventitre con il contatore di salvataggio piu' alto. Ogni blocco ha
# dodici byte di intestazione, cioe' somma, identificativo e contatore, tutti in ordine di byte
# inverso, e 0x1FF0 byte di contenuto; i contenuti si concatenano nell'ordine dell'identificativo
# e formano un'area continua in cui vive il deposito.
BOX_BLOCCHI = 23
BOX_DIM_BLOCCO = 0x2000
BOX_UTILE = BOX_DIM_BLOCCO - 0x10
BOX_SCATOLE = 50
BOX_POSIZIONI = 30
# Una posizione e' l'esemplare da ottanta byte piu' quattro byte con gli identificativi di chi lo
# ha depositato, che e' la differenza con il deposito di una cartuccia e la ragione per cui il
# passo qui e' ottantaquattro e non ottanta.
BOX_PASSO = STRUTTURA_BOX + 4
BOX_PRIMO = 8


def spacchetta_box_gc(corpo):
    """L'area continua del deposito, ricomposta dai blocchi del salvataggio valido.

    Riferisce anche quale dei due salvataggi sia stato scelto e con quale contatore, perche' un
    file di Pokemon Box ne porta due e leggere quello vecchio darebbe un deposito plausibile e
    non quello corrente.
    """
    blocchi = []
    for i in range(2 * BOX_BLOCCHI):
        off = BOX_DIM_BLOCCO + i * BOX_DIM_BLOCCO
        if off + BOX_DIM_BLOCCO > len(corpo):
            break
        blocchi.append({"off": off,
                        "id": u32be(corpo, off + 4),
                        "conteggio": u32be(corpo, off + 8)})
    if len(blocchi) < 2 * BOX_BLOCCHI:
        return None, None
    conteggi = [b["conteggio"] for b in blocchi]
    massimo = max(conteggi)
    quale = conteggi.index(massimo) // BOX_BLOCCHI
    scelti = sorted(blocchi[quale * BOX_BLOCCHI:(quale + 1) * BOX_BLOCCHI],
                    key=lambda b: b["id"])
    area = bytearray(BOX_BLOCCHI * BOX_UTILE)
    for b in scelti:
        base = b["id"] * BOX_UTILE
        if base + BOX_UTILE > len(area):
            return None, None
        area[base:base + BOX_UTILE] = corpo[b["off"] + 0xC:b["off"] + 0xC + BOX_UTILE]
    return bytes(area), {"salvataggio": quale, "conteggio": massimo}


def censisci_deposito_box(corpo, gen3):
    """Il censimento del deposito di Pokemon Box, cioe' millecinquecento posizioni.

    Restituisce le stesse grandezze del censimento di una cartuccia, cosicche' i due si possano
    confrontare senza tradurre nulla: e' il punto di questo lavoro, perche' il confronto fra
    questo deposito e il nostro conto di terza generazione e' il solo controllo indipendente che
    il progetto possa fare sulla completezza della propria enumerazione.
    """
    area, scelta = spacchetta_box_gc(corpo)
    if area is None:
        return None
    occupate, uova, cromatici, difettosi = 0, 0, 0, 0
    specie = {}
    for scatola in range(BOX_SCATOLE):
        for posizione in range(BOX_POSIZIONI):
            off = BOX_PRIMO + BOX_PASSO * (scatola * BOX_POSIZIONI + posizione)
            grezzo = area[off:off + STRUTTURA_BOX]
            if len(grezzo) < STRUTTURA_BOX:
                continue
            try:
                mon = gen3.Gen3Mon.from_bytes(grezzo, party=False)
            except Exception:
                difettosi += 1
                continue
            if not mon.has_species:
                continue
            occupate += 1
            if mon.is_bad_egg:
                difettosi += 1
            if mon.is_egg:
                uova += 1
            if mon.is_shiny:
                cromatici += 1
            interno = mon.growth.species
            specie[interno] = specie.get(interno, 0) + 1
    return {"occupate": occupate, "uova": uova, "cromatici": cromatici,
            "difettosi": difettosi, "specie": specie,
            "salvataggio_scelto": scelta["salvataggio"], "conteggio": scelta["conteggio"]}


# ---------------------------------------------------------------------------------------------
# Esemplari singoli e archivi
# ---------------------------------------------------------------------------------------------

def leggi_esemplare(dati, gen3):
    """Un esemplare di terza generazione, nella forma in cui il file lo porta.

    Le due forme sono la canonica, con le quattro sottostrutture in chiaro e in ordine fisso, e
    quella del gioco, con le sottostrutture permutate secondo il valore di personalità e messe
    sotto somma esclusiva. Il progetto scrive la prima come `.pk3` e la seconda come `.ek3`, e
    così fa PKHeX, ma un file trovato altrove può portare l'una o l'altra a prescindere
    dall'estensione: leggerlo con la forma sbagliata non produce un errore ma un esemplare
    plausibile e falso, cioè specie diciottomila e checksum che non torna.

    Si provano dunque entrambe e si riferisce quale ha risposto, che è la stessa disciplina con
    cui si identifica il gioco di un salvataggio: il criterio è il checksum, non l'estensione.
    """
    tentativi = []
    for etichetta, funzione in (("canonica", gen3.Gen3Mon.from_canonical_bytes),
                                ("del gioco, cifrata", gen3.Gen3Mon.from_bytes)):
        for party in (len(dati) >= 100, False):
            try:
                mon = funzione(dati, party=party)
            except Exception as exc:
                tentativi.append((etichetta, party, str(exc)))
                continue
            if mon.checksum_ok:
                return mon, etichetta, tentativi
            tentativi.append((etichetta, party, "checksum non torna"))
    return None, None, tentativi


def analizza_pk3(dati, gen3, tabella):
    esito = {"famiglia": "esemplare singolo di terza generazione"}
    mon, forma, tentativi = leggi_esemplare(dati, gen3)
    if mon is None:
        esito["valido"] = False
        esito["ragione"] = ("nessuna delle due forme dà un checksum che torna: "
                            + "; ".join("%s: %s" % (e, m) for e, _p, m in tentativi))
        return esito
    esito["forma"] = forma
    esito["valido"] = mon.checksum_ok
    esito["checksum_torna"] = mon.checksum_ok
    esito["specie_interna"] = mon.growth.species
    esito["cromatico"] = mon.is_shiny
    esito["uovo"] = mon.is_egg
    esito["uovo_peste"] = mon.is_bad_egg
    esito["personalita"] = "0x%08X" % mon.personality
    esito["id_allenatore"] = "0x%08X" % mon.ot_id
    esito["gioco_di_origine"] = mon.misc.origin_game_name
    if tabella is not None:
        esito["nome_allenatore"] = nome_gen3(mon.ot_name, tabella)
        esito["soprannome"] = nome_gen3(mon.nickname, tabella)
    return esito


def censisci_archivio_pk3(z, voci, gen3):
    """Il censimento degli esemplari dentro un archivio, che è il suo contenuto informativo.

    Contare le voci di un archivio dice quanto pesa, non che cosa porta. Qui si legge ciascun
    esemplare e si riferisce quante specie distinte contenga, quanti siano cromatici e quanti
    non si leggano: è la sola forma in cui un archivio di esemplari serve al confronto con un
    elenco di specie da completare.
    """
    specie, cromatici, uova, illeggibili = {}, 0, 0, []
    forme = {}
    for v in voci:
        if not v.filename.lower().endswith((".pk3", ".ek3")):
            continue
        try:
            dati = z.read(v)
        except Exception as exc:
            illeggibili.append((v.filename, str(exc)))
            continue
        mon, forma, _t = leggi_esemplare(dati, gen3)
        if mon is None:
            illeggibili.append((v.filename, "checksum non torna in nessuna delle due forme"))
            continue
        forme[forma] = forme.get(forma, 0) + 1
        specie[mon.growth.species] = specie.get(mon.growth.species, 0) + 1
        if mon.is_shiny:
            cromatici += 1
        if mon.is_egg:
            uova += 1
    return {"esemplari": sum(specie.values()), "specie": specie, "cromatici": cromatici,
            "uova": uova, "illeggibili": illeggibili, "forme": forme}


def analizza_zip(percorso, gen3=None):
    esito = {"famiglia": "archivio"}
    try:
        with zipfile.ZipFile(percorso) as z:
            danneggiato = z.testzip()
            voci = z.infolist()
            esito["voci"] = len(voci)
            esito["integro"] = danneggiato is None
            if danneggiato is not None:
                esito["prima_voce_danneggiata"] = danneggiato
            estensioni = {}
            fuori_cartella = []
            for v in voci:
                ext = os.path.splitext(v.filename)[1].lower() or "(senza estensione)"
                estensioni[ext] = estensioni.get(ext, 0) + 1
                # Una voce con percorso assoluto o con risalita e' il solo modo in cui un archivio
                # di dati puo' fare danno: scrivere fuori dalla cartella di estrazione. Si guarda,
                # perche' costa nulla e perche' e' l'unico rischio reale di questi file.
                if v.filename.startswith("/") or ".." in v.filename.replace("\\", "/").split("/"):
                    fuori_cartella.append(v.filename)
            esito["estensioni"] = estensioni
            esito["voci_con_percorso_pericoloso"] = fuori_cartella
            esito["valido"] = danneggiato is None and not fuori_cartella
            if gen3 is not None and any(e in estensioni for e in (".pk3", ".ek3")):
                esito["censimento"] = censisci_archivio_pk3(z, voci, gen3)
    except zipfile.BadZipFile as exc:
        esito["valido"] = False
        esito["ragione"] = "archivio non leggibile: " + str(exc)
    return esito


# ---------------------------------------------------------------------------------------------
# Instradamento
# ---------------------------------------------------------------------------------------------

def analizza(percorso, gen3, tabella, censimento):
    nome = os.path.basename(percorso)
    ext = os.path.splitext(nome)[1].lower()
    dimensione = os.path.getsize(percorso)

    if ext == ".zip":
        esito = analizza_zip(percorso, gen3)
        esito["dimensione"] = dimensione
        return esito

    with io.open(percorso, "rb") as f:
        dati = f.read()

    if ext in (".pk3", ".ek3"):
        esito = analizza_pk3(dati, gen3, tabella)
    elif ext == ".gci" or dimensione == SIZE_G3BOX + GCI_INTESTAZIONE:
        esito, corpo = analizza_box_gc(dati)
        if esito.get("valido") and censimento and corpo is not None:
            deposito = censisci_deposito_box(corpo, gen3)
            if deposito is not None:
                esito["deposito"] = deposito
    elif dimensione in (SIZE_G3RAW,) or (SIZE_G3RAW < dimensione <= SIZE_G3RAW + 64):
        # Un salvataggio di terza generazione con una coda: alcuni strumenti di estrazione
        # aggiungono al file un piede con l'orologio in tempo reale o con la propria firma. La
        # coda non tocca le trentadue sezioni, quindi si analizza il prefisso e la si dichiara,
        # invece di rifiutare il file per una differenza che non lo rende illeggibile.
        esito = analizza_gen3(dati[:SIZE_G3RAW], gen3, tabella, censimento)
        if dimensione > SIZE_G3RAW:
            esito["coda_oltre_il_salvataggio"] = dimensione - SIZE_G3RAW
    elif dimensione == SIZE_G4RAW:
        esito = analizza_nds(dati)
    elif dimensione in (SIZE_G1RAW, SIZE_G2RAW_J):
        esito = analizza_gen12(dati)
    elif dimensione in [d for _n, d in TRE_DS_CANDIDATI]:
        esito = analizza_tre_ds(dati)
    else:
        esito = {"famiglia": "non riconosciuta", "valido": False,
                 "ragione": "la dimensione %d non corrisponde a nessuna famiglia nota" % dimensione}
    esito["dimensione"] = dimensione
    return esito


def carica_supporti(ace, pkhex):
    """Le tabelle opzionali: la charmap per i nomi, e la corrispondenza fra le due numerazioni."""
    from pokebridge import gen3 as modulo_gen3
    from pokebridge import charmap as cm
    tabella = None
    try:
        tabella = cm.Charmap.gen3()
    except Exception:
        tabella = None
    interno_verso_nazionale, per_id = {}, {}
    if ace:
        try:
            import importlib.util
            percorso = os.path.join(RADICE, "tools", "genera-evento-gen3.py")
            spec = importlib.util.spec_from_file_location("generatore", percorso)
            generatore = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(generatore)
            for nazionale, interno in generatore.nazionale_verso_interno(ace).items():
                interno_verso_nazionale[interno] = nazionale
            _per_nome, per_id = generatore.specie_per_nome(ace)
        except Exception as exc:
            print("  nota: la corrispondenza fra le numerazioni non si e' potuta caricare (%s), "
                  "quindi le specie restano in numerazione interna" % exc)
    return modulo_gen3, tabella, interno_verso_nazionale, per_id


def scrivi_markdown(percorso, esiti, interno_verso_nazionale, per_id, cartella, data):
    """Il censimento come documento generato, e perché descriva una cartella locale.

    Un documento generato che legge il disco descrive lo stato di una macchina, e questo
    progetto ha già registrato quella obiezione a proposito delle schede degli esemplari, che
    per quella ragione si ricalcolano dalle sorgenti invece di leggere i file prodotti. Qui la
    scelta è opposta e la ragione è che il soggetto è cambiato: là il soggetto era ciò che il
    programma produce, e il disco era un accidente; qui il soggetto è precisamente una raccolta
    di file che vive su un disco e non entra nel controllo di versione. Descriverla è l'unico
    modo di conservarne la conoscenza, e il documento lo dichiara nella propria intestazione
    insieme alla data, cosicché nessuno lo prenda per una proprietà del progetto.
    """
    r = []
    r.append("# Censimento dei salvataggi esterni")
    r.append("")
    r.append("> Documento generato da `tools/verifica-salvataggi.py --markdown`. Non si modifica "
             "a mano. Descrive una cartella locale che non entra nel controllo di versione, "
             "cioè `%s`, allo stato del %s: è un inventario di materiale di riferimento e non "
             "una proprietà del progetto, e va rigenerato quando la cartella cambia."
             % (cartella, data))
    r.append("")
    r.append("Che cosa ciascuna colonna dice, e che cosa non dice. L'esito è strutturale: dice "
             "che il file è un salvataggio leggibile del gioco indicato, con le somme di "
             "controllo che tornano, e non dice nulla sulla legittimità degli esemplari che "
             "contiene né sulla liceità del loro uso. Il conto delle specie riguarda ciò che sta "
             "nel deposito, non le caselle del Pokedex: un giocatore che abbia completato il "
             "Pokedex e poi liberato un esemplare ha la casella accesa e la scatola vuota, e "
             "queste due grandezze non si sommano.")
    r.append("")
    r.append("| File | Esito | Famiglia | Gioco | Allenatore | Esemplari | Specie | Cromatici |")
    r.append("|---|---|---|---|---|---|---|---|")
    for nome, e in sorted(esiti.items()):
        stato = e.get("valido")
        marca = "integro" if stato else ("rifiutato" if stato is False else "senza esito")
        gioco = str(e.get("gioco", "")) or "-"
        allenatore = "-"
        if "allenatore" in e:
            a = e["allenatore"]
            allenatore = "%s, id %s" % (a.get("nome") or "?", a.get("id_visibile"))
        censimento = e.get("deposito") or e.get("censimento")
        if censimento:
            esemplari = str(censimento.get("occupate", censimento.get("esemplari", 0)))
            specie = str(len(censimento["specie"]))
            cromatici = str(censimento["cromatici"])
        else:
            esemplari = specie = cromatici = "-"
        r.append("| `%s` | %s | %s | %s | %s | %s | %s | %s |"
                 % (nome, marca, e.get("famiglia", "?"), gioco, allenatore,
                    esemplari, specie, cromatici))
    r.append("")

    # L'unione delle specie coperte, che e' il numero utile all'obiettivo del Pokedex: quante
    # delle trecentottantasei voci nazionali di terza generazione questa raccolta porti come
    # esemplare, e quali manchino. Il conto si fa sull'unione e non fonte per fonte, perche' le
    # fonti si sovrappongono e sommarle direbbe un numero senza significato.
    if interno_verso_nazionale:
        unione = set()
        for e in esiti.values():
            censimento = e.get("deposito") or e.get("censimento")
            if not censimento:
                continue
            for interno in censimento["specie"]:
                nazionale = interno_verso_nazionale.get(int(interno))
                if nazionale is not None:
                    unione.add(nazionale)
        mancanti = sorted(set(range(1, 387)) - unione)
        r.append("## Copertura complessiva delle trecentottantasei voci di terza generazione")
        r.append("")
        r.append("L'unione delle specie presenti come esemplare in questa raccolta copre %d "
                 "delle trecentottantasei voci nazionali di terza generazione. Il conto è "
                 "sull'unione e non fonte per fonte, perché le fonti si sovrappongono e la "
                 "somma dei loro conti non significherebbe nulla." % len(unione))
        r.append("")
        if mancanti:
            nomi = ", ".join("%d %s" % (m, per_id.get(interno_verso_nazionale_inverso(
                interno_verso_nazionale, m), "?")) for m in mancanti)
            r.append(("Manca una voce sola, ed è: %s." % nomi) if len(mancanti) == 1
                     else ("Mancano %d voci, e sono: %s." % (len(mancanti), nomi)))
        else:
            r.append("Non manca nessuna voce.")
        r.append("")
    io.open(percorso, "w", encoding="utf-8", newline="").write("\n".join(r) + "\n")


def interno_verso_nazionale_inverso(mappa, nazionale):
    """L'identificativo interno di un numero nazionale, dalla mappa inversa gia' caricata."""
    for interno, naz in mappa.items():
        if naz == nazionale:
            return interno
    return None


def stampa(nome, esito, interno_verso_nazionale):
    stato = esito.get("valido")
    marca = "OK   " if stato else ("NO   " if stato is False else "?    ")
    print("%s%s" % (marca, nome))
    print("      famiglia: %s, %d byte" % (esito.get("famiglia", "?"), esito["dimensione"]))
    for chiave in ("gioco", "generazione", "formato", "localizzazione", "slot_attivo",
                   "contatore_salvataggi", "codice_gioco", "coda_oltre_il_salvataggio"):
        if chiave in esito and esito[chiave] is not None:
            print("      %s: %s" % (chiave.replace("_", " "), esito[chiave]))
    if "allenatore" in esito:
        a = esito["allenatore"]
        print("      allenatore: %s, %s, id %s e segreto %s, %s ore e %s minuti"
              % (a["nome"], a["sesso"], a["id_visibile"], a["id_segreto"],
                 a["ore_di_gioco"], a["minuti"]))
    if "checksum" in esito:
        c = esito["checksum"]
        if "torna" in c:
            print("      checksum principale: %s" % ("torna" if c["torna"] else "NON torna"))
        else:
            print("      checksum principale: %s" % c["non_verificato"])
    if esito.get("deposito"):
        d = esito["deposito"]
        if d is None:
            print("      deposito: sezioni mancanti, non censito")
        else:
            distinte = len(d["specie"])
            print("      deposito: %d posizioni occupate, %d specie distinte, %d cromatici, "
                  "%d uova, %d strutture rifiutate"
                  % (d["occupate"], distinte, d["cromatici"], d["uova"], d["difettosi"]))
            if interno_verso_nazionale:
                nazionali = sorted({interno_verso_nazionale[i] for i in d["specie"]
                                    if i in interno_verso_nazionale})
                senza = [i for i in d["specie"] if i not in interno_verso_nazionale]
                print("      numeri nazionali distinti: %d%s"
                      % (len(nazionali),
                         ", piu' %d identificativi interni senza corrispondenza" % len(senza)
                         if senza else ""))
    if esito.get("censimento"):
        c = esito["censimento"]
        print("      censimento dell'archivio: %d esemplari, %d specie distinte, %d cromatici, "
              "%d uova, %d illeggibili"
              % (c["esemplari"], len(c["specie"]), c["cromatici"], c["uova"],
                 len(c["illeggibili"])))
        print("      forme trovate: %s"
              % ", ".join("%s x%d" % (k, v) for k, v in sorted(c["forme"].items())))
        if interno_verso_nazionale:
            nazionali = sorted({interno_verso_nazionale[i] for i in c["specie"]
                                if i in interno_verso_nazionale})
            senza = [i for i in c["specie"] if i not in interno_verso_nazionale]
            print("      numeri nazionali distinti: %d%s"
                  % (len(nazionali),
                     ", piu' %d identificativi interni senza corrispondenza" % len(senza)
                     if senza else ""))
    if "candidati" in esito:
        risposte = [n for n, ok in esito["candidati"] if ok]
        print("      candidati che rispondono: %s"
              % (", ".join(risposte) if risposte else "nessuno"))
    for chiave in ("forma", "specie_interna", "personalita", "id_allenatore", "nome_allenatore",
                   "soprannome", "gioco_di_origine", "cromatico", "uovo", "uovo_peste",
                   "voci", "estensioni", "voci_con_percorso_pericoloso", "firma_di_coda",
                   "somma_memorizzata", "somma_calcolata"):
        if chiave in esito:
            print("      %s: %s" % (chiave.replace("_", " "), esito[chiave]))
    if "ragione" in esito:
        print("      ragione: %s" % esito["ragione"])
    if esito.get("difetti"):
        for slot, elenco in esito["difetti"].items():
            if elenco:
                print("      difetti in slot %s: %s"
                      % (slot, "; ".join("sezione %d, %s" % d for d in elenco)))


def self_test():
    """Controlli sulle sole funzioni aritmetiche, che sono le uniche verificabili senza un file.

    Il valore atteso del CRC non e' inventato: e' calcolato a mano dalla definizione della fonte
    su un ingresso di un byte, cosi' che il controllo fallisca se la trascrizione della funzione
    e' sbagliata invece di limitarsi a fotografare cio' che il codice fa.
    """
    falliti = []

    def prova(descrizione, condizione):
        print("  %-7s %s" % ("ok" if condizione else "FALLITO", descrizione))
        if not condizione:
            falliti.append(descrizione)

    # CRC su ingresso vuoto: nessun giro di ciclo, quindi resta lo stato iniziale 0xFFFF.
    prova("il CRC di un ingresso vuoto e' lo stato iniziale", crc16_ccitt(b"") == 0xFFFF)
    # Un giro a mano con b = 0x00: x = 0x00 ^ 0xFF = 0xFF; x ^= x >> 4 -> 0xFF ^ 0x0F = 0xF0;
    # alto = 0xFF ^ (0xF0 >> 3) ^ (0xF0 << 4) = 0xFF ^ 0x1E ^ 0x00 = 0xE1;
    # basso = 0xF0 ^ (0xF0 << 5) = 0xF0 ^ 0x00 = 0xF0.
    prova("il CRC di un byte nullo torna il valore calcolato a mano",
          crc16_ccitt(b"\x00") == 0xE1F0)
    prova("il CRC dipende dall'ordine dei byte",
          crc16_ccitt(b"\x01\x02") != crc16_ccitt(b"\x02\x01"))
    # La somma di Pokemon Box su due byte 0x00 0x01. La fonte legge la parola in ordine di byte
    # diretto e poi la rovescia, che equivale a leggerla in ordine inverso: vale dunque 0x0001 e
    # non 0x0100. Il controllo era scritto con il valore rovesciato e ha colto la differenza al
    # primo lancio, che e' esattamente il suo scopo.
    atteso = (0x0001 << 16) | ((0xF004 - 0x0001) & 0xFFFF)
    prova("la somma di Pokemon Box compone somma e complemento",
          somma16_be_invertita(b"\x00\x01") == atteso)
    prova("una lista con contatore oltre il massimo e' rifiutata",
          not lista_valida_g12(b"\x63" + b"\xFF" * 40, 0, 20))
    prova("una lista senza terminatore e' rifiutata",
          not lista_valida_g12(b"\x02\x01\x02\x03" + b"\x00" * 40, 0, 20))
    prova("una lista con contatore e terminatore validi e' accettata",
          lista_valida_g12(b"\x02\x01\x02\xFF" + b"\x00" * 40, 0, 20))
    print("")
    print("self-test: %d controlli falliti su %d" % (len(falliti), 7))
    return 1 if falliti else 0


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cartella", nargs="?", help="cartella o file da analizzare")
    p.add_argument("--censimento", action="store_true",
                   help="censisce il deposito dei salvataggi di terza generazione")
    p.add_argument("--ace", help="clone di ace-builder, per la corrispondenza fra le numerazioni")
    p.add_argument("--pkhex", help="clone di PKHeX, riservato a usi futuri")
    p.add_argument("--json", help="scrive l'esito completo in un file JSON")
    p.add_argument("--markdown", help="scrive il censimento come documento tracciato")
    p.add_argument("--self-test", action="store_true", help="controlla le funzioni aritmetiche")
    a = p.parse_args()

    if a.self_test:
        return self_test()
    if not a.cartella:
        p.error("serve una cartella o un file, oppure --self-test")

    modulo_gen3, tabella, interno_verso_nazionale, per_id = carica_supporti(a.ace, a.pkhex)

    if os.path.isdir(a.cartella):
        percorsi = [os.path.join(a.cartella, n) for n in sorted(os.listdir(a.cartella))]
        percorsi = [x for x in percorsi if os.path.isfile(x)]
    else:
        percorsi = [a.cartella]

    esiti = {}
    validi, non_validi, ignoti = 0, 0, 0
    for percorso in percorsi:
        nome = os.path.basename(percorso)
        if os.path.splitext(nome)[1].lower() in (".txt", ".md", ".json"):
            continue
        esito = analizza(percorso, modulo_gen3, tabella, a.censimento)
        esiti[nome] = esito
        stampa(nome, esito, interno_verso_nazionale)
        print("")
        if esito.get("valido") is True:
            validi += 1
        elif esito.get("valido") is False:
            non_validi += 1
        else:
            ignoti += 1

    print("=" * 90)
    print("%d file analizzati: %d riconosciuti e integri, %d rifiutati, %d senza esito"
          % (len(esiti), validi, non_validi, ignoti))
    print("")
    print("Che cosa questo esito non dice. Non dice se un esemplare sia legittimo, che e' il "
          "giudizio di PKHeX e non di una somma di controllo; non dice se il salvataggio sia "
          "originale o costruito, perche' un salvataggio costruito bene ha le somme giuste; e "
          "non dice se sia lecito usarlo, che e' una questione di perimetro e sta in "
          ".claude/rules/hardware-and-perimeter.md.")

    if a.markdown:
        import datetime
        scrivi_markdown(a.markdown, esiti, interno_verso_nazionale, per_id, a.cartella,
                        datetime.date.today().isoformat())
        print("")
        print("scritto " + a.markdown)

    if a.json:
        with io.open(a.json, "w", encoding="utf-8") as f:
            f.write(json.dumps(esiti, ensure_ascii=False, indent=2, default=str) + "\n")
        print("")
        print("scritto " + a.json)
    return 0 if non_validi == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
