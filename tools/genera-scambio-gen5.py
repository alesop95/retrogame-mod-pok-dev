#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone gli scambi in gioco di quinta generazione che portano un valore di personalita' fissato.

Le sette voci, e perche' vengono tutte da Nero e Bianco
---------------------------------------------------------
`tools/censimento-scambi.py` legge sette voci di quinta generazione con un valore di personalita'
dichiarato dalla fonte: tre da `TradeGift_BW` (Emolga, Rotom, Munchlax), due da `TradeGift_B`
(Petilil, Basculin rosso) e due da `TradeGift_W` (Cottonee, Basculin blu). Nessuna viene da
`EncounterTrade5B2W2`, e non e' un caso: quella classe, letta per intero il 2026-09-16 in
`EncounterTrade5B2W2.cs`, non ha affatto un campo per il valore di personalita' nel proprio
costruttore, quindi uno scambio di Nero 2 o Bianco 2 e' sempre casuale e non puo' mai comparire in
questo censimento.

Il formato pk5, letto da PK5.cs invece che assunto identico a pk4
--------------------------------------------------------------------
Il record di scatola misura ancora 136 byte, la stessa somma di controllo a sedici bit dal byte
0x08, e la stessa cifratura a blocchi permutati secondo il valore di personalita': `PokeCrypto.cs`
dichiara `SIZE_5STORED = 136` e tratta la permutazione di quarta e quinta generazione con la
medesima funzione. Quasi tutti gli offset di campo coincidono byte per byte con quelli di
`genera-evento-gen4.py`, e questo programma li importa da li' invece di ripeterli: specie,
identificativi, esperienza, cordialita', abilita', lingua, i trentadue bit dei valori individuali
con il bit piu' alto per il nomignolo fissato, il byte di sesso/forma/incontro fatidico, la
versione, il nome dell'allenatore, la data di incontro, il luogo di incontro, la sfera, e il byte
di livello di incontro con il sesso dell'allenatore cedente.

Tre differenze vere, non assunte, tutte verificate sul sorgente. La prima: la quinta generazione
aggiunge un byte di natura esplicito a 0x41, che nelle generazioni precedenti non esiste perche' la
natura si deriva dal valore di personalita'; qui la fonte lo dichiara per nome insieme al valore di
personalita' stesso, quindi si scrivono entrambi senza calcolarli l'uno dall'altro. La seconda: la
quinta generazione non porta il campo esteso del luogo che affliggeva Platino e HGSS, quindi il
luogo si scrive una sola volta e la sfera una sola volta, senza la duplicazione che
`genera-scambio-gen4.py` doveva fare. La terza, la piu' importante: il testo non passa da una
tabella di caratteri. `StringConverter5.cs` mostra che il nome si scrive come sedici bit per
carattere presi direttamente dal punto di codice Unicode, senza alcuna tabella di sostituzione
salvo il simbolo di genere, che nessuna delle sette voci usa: questo programma scrive quindi
`ord(carattere)` invece di interrogare la tabella della quarta generazione, che qui non si applica
e avrebbe potuto sembrare necessaria senza esserlo.

Il luogo, la sfera e la lingua, che qui non hanno eccezioni
--------------------------------------------------------------
Nessuna delle sette voci dichiara un luogo di incontro proprio nelle sue proprieta', quindi tutte
arrivano dalla costante dello scambio locale di quinta generazione, `Locations.LinkTrade5NPC`, che
vale 30002 e non 2001: e' un valore diverso da quello di quarta generazione, letto dalla stessa
fonte (`Locations.cs`) e non riusato per analogia. Tutte e sette portano una Poke Ball. Sulla
lingua, `EncounterTrade5BW.ConvertToPKM` scrive `language == 1 ? 0 : language`: il ramo che azzera
la lingua riguarda solo chi gioca in giapponese, e un giocatore italiano (lingua 4) non lo
incontra mai. Nessuna delle sette voci ha quindi bisogno dell'eccezione di lingua che invece
governava il Magikarp e il Pikachu di quarta generazione.

Che cosa viene dalla fonte e che cosa si compone
---------------------------------------------------
Valore di personalita', valori individuali, natura, genere, abilita' e identificativi sono tutti
dichiarati dalla fonte e si copiano senza ricalcolo. Si compongono l'esperienza dal livello
dichiarato, le mosse dal repertorio di livello della specie (nessuna delle sette fissa mosse
proprie), la cordialita' di base della specie, la data di incontro fissa, e il testo di nomignolo e
allenatore in italiano, che la fonte fornisce per tutte e sette le voci.

Il gioco di destinazione
---------------------------
Le tre voci di `TradeGift_BW` e le due di `TradeGift_B` si calcolano su Nero; le due di
`TradeGift_W` su Bianco, perche' sono le versioni che le rispettive tabelle dichiarano. Il
repertorio di mosse per livello e' condiviso da Nero e Bianco in un solo file della fonte
(`lvlmove_bw.pkl`), quindi la scelta incide solo sul campo Versione scritto nel record, non sul
calcolo delle mosse. Nessun salvataggio di quinta generazione e' oggi nella raccolta del progetto:
il lotto resta quindi in attesa non solo del giudizio ma anche del veicolo su cui farlo aprire.

Uso
---
    python tools/genera-scambio-gen5.py --pkhex _notes/fonti/pkhex --lotto _notes/lotto-scambi-gen5
    python tools/genera-scambio-gen5.py --self-test
"""

import argparse
import hashlib
import importlib.util
import io
import json
import os
import re
import struct
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

G4 = None    # genera-evento-gen4.py: gli offset del record e la somma di controllo, condivisi
I4 = None    # genera-incontro-gen4.py: esperienza, punti potenza, tabella personale
I3 = None    # genera-incontro-gen3.py: repertorio di livello a partire dal file grezzo
CS = None    # censimento-scambi.py: la lettura delle tabelle di scambio dalla fonte

# La tabella personale di quinta generazione NON condivide gli offset con quella di quarta: e' un
# record piu' lungo (0x3C e non 0x2C, da PersonalInfo5BW.cs, SIZE) e con i campi in altre
# posizioni, scoperto perche' il primo tentativo con gli offset di quarta generazione ha letto un
# gruppo di crescita inesistente invece di uno sbagliato ma plausibile: il presidio ha funzionato.
DIM_PERSONALE = 0x3C
OFF_P_GENERE = 0x12
OFF_P_CORDIALITA = 0x14
OFF_P_CRESCITA = 0x15
OFF_P_ABILITA1 = 0x18
OFF_P_ABILITA2 = 0x19

OFF_NATURA = 0x41  # non esiste in pk3/pk4: la natura vi si deriva dal valore di personalita'

LINGUE = ("it", "en", "ja")
CODICE_LINGUA_IT = 4  # dalla tavola empirica gia' verificata sul progetto (byte 0x12 di 172 file)

LOCATIONS_LINK_TRADE_5NPC = 30002  # da Locations.cs; non e' il 2001 di quarta generazione
PALLA_POKE = 4
DATA_INCONTRO = (2026, 9, 16)

# Da Nature.cs: l'ordine dei nomi e' l'indice del byte.
NOMI_NATURA = ("Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed",
               "Impish", "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild",
               "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky")
INDICE_NATURA = {nome: i for i, nome in enumerate(NOMI_NATURA)}

# Da GameVersion.cs.
VERSIONE_CODICE = {"w": 20, "b": 21, "w2": 22, "b2": 23}
GIOCO_PER_TABELLA = {"TradeGift_BW": "b", "TradeGift_B": "b", "TradeGift_W": "w"}
TABELLE_VALIDE = tuple(GIOCO_PER_TABELLA)

REPERTORIO_BW = "lvlmove_bw.pkl"
PERSONALE_BW = "personal_bw"


def _modulo(nome_file, alias):
    percorso = os.path.join(RADICE, "tools", nome_file)
    spec = importlib.util.spec_from_file_location(alias, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _carica_moduli():
    global G4, I4, I3
    G4 = _modulo("genera-evento-gen4.py", "genera_evento_gen4")
    I4 = _modulo("genera-incontro-gen4.py", "genera_incontro_gen4")
    I3 = _modulo("genera-incontro-gen3.py", "genera_incontro_gen3")
    I3.G3 = I3._fratello()
    I4.I3 = I3


def numeri_di(testo):
    m = re.search(r"new\(([^()]*)\)", testo)
    if not m:
        return []
    return [int(x) for x in re.split(r"\s*,\s*", m.group(1).strip()) if x]


def leggi_scambi5(pkhex):
    """Le sette voci di quinta generazione con valore di personalita' fissato, dalla fonte."""
    nomi_en = CS.nomi_specie(os.path.join(pkhex, CS.NOMI_EN))
    if nomi_en is None:
        return None, None, "mancano i nomi delle specie sotto " + pkhex
    tabelle_lette = CS.censisci(pkhex, nomi_en, lingue=LINGUE)
    if tabelle_lette is None:
        return None, None, "manca la cartella delle tabelle sotto " + pkhex
    fuori = []
    for t in tabelle_lette:
        if t["generazione"] != "5" or t["tabella"] not in TABELLE_VALIDE:
            continue
        for v in t["voci"]:
            if not v["pid"]:
                continue
            fuori.append({"tabella": t["tabella"], "voce": v})
    return fuori, nomi_en, None


def voce_personale(pkhex, nazionale):
    dati = io.open(os.path.join(pkhex, I4.CARTELLA_PERSONALI, PERSONALE_BW), "rb").read()
    inizio = nazionale * DIM_PERSONALE
    blocco = dati[inizio:inizio + DIM_PERSONALE]
    if len(blocco) < DIM_PERSONALE:
        raise KeyError("numero nazionale fuori dalla tabella personale: %d" % nazionale)
    return blocco


def mosse_al_livello(pkhex, nazionale, livello):
    grezzo = io.open(os.path.join(pkhex, I4.CARTELLA_REPERTORI, REPERTORIO_BW), "rb").read()
    area = I3.aree_indicizzate(grezzo)[nazionale]
    return I3.mosse_al_livello(I3.repertorio_di_livello(area), livello)


def codifica_nome5(testo):
    """Il nome nella codifica di quinta generazione: punti di codice Unicode diretti, non una
    tabella. Verificato su `StringConverter5.SetString`, che scrive `chr` cosi' com'e' salvo
    l'unica eccezione del simbolo di genere, che nessuna delle sette voci usa."""
    fuori = bytearray()
    for ch in testo:
        fuori += struct.pack("<H", ord(ch))
    fuori += struct.pack("<H", 0xFFFF)
    return bytes(fuori)


def componi(pkhex, entry, allenatore, nomi_en):
    v = entry["voce"]
    gioco = GIOCO_PER_TABELLA[entry["tabella"]]
    props = v["proprieta"]
    specie = v["specie"]
    livello = v["livello"]
    pid = int(v["pid"], 16)
    tid = int(props.get("TID16", "0"))
    sid = 0  # EncounterTrade5BW.SID16 => 0 sempre
    ot_gender = int(props.get("OTGender", "0"))
    gender = int(props.get("Gender", "0"))
    ability_dichiarata = props.get("Ability", "")
    forma = int(props.get("Form", "0"))
    natura_testo = props.get("Nature", "")
    natura_nome = natura_testo.split(".", 1)[1] if "." in natura_testo else natura_testo
    if natura_nome not in INDICE_NATURA:
        return None, {"errore": "natura non riconosciuta: %r" % natura_testo}
    iv_lista = numeri_di(props.get("IVs", ""))
    if len(iv_lista) != 6:
        return None, {"errore": "IVs non leggibili dalla proprieta': %r" % props.get("IVs")}

    personale = voce_personale(pkhex, specie)
    ab1, ab2 = personale[OFF_P_ABILITA1], personale[OFF_P_ABILITA2]
    # A differenza del modello di un dono di quarta generazione, qui l'abilita' non si deriva dal
    # valore di personalita': `PK5.RefreshAbility` scrive lo slot che la fonte dichiara (Ability
    # in AbilityPermission) senza guardare la parita' del PID, ed `EncounterTrade5BW.ConvertToPKM`
    # chiama esattamente quella funzione. Il presidio di parita' che il fratello di quarta
    # generazione applica al proprio modello non vale quindi qui, e usarlo ha respinto per errore
    # due voci vere (i due Basculin) prima di essere tolto: lezione registrata, non ipotizzata.
    if "OnlySecond" in ability_dichiarata:
        bit_abilita = 1
    elif "OnlyFirst" in ability_dichiarata:
        bit_abilita = 0
    else:
        return None, {"errore": "abilita' non riconosciuta: %r" % ability_dichiarata}

    esperienza = I4.esperienza(personale[OFF_P_CRESCITA], livello)

    pk5 = bytearray(G4.DIM_PK4_SCATOLA)
    struct.pack_into("<I", pk5, G4.OFF_PID, pid)
    struct.pack_into("<H", pk5, G4.OFF_SANITA, 0)
    struct.pack_into("<H", pk5, G4.OFF_SPECIE, specie)
    struct.pack_into("<H", pk5, G4.OFF_TID, tid & 0xFFFF)
    struct.pack_into("<H", pk5, G4.OFF_SID, sid)
    struct.pack_into("<I", pk5, G4.OFF_ESPERIENZA, esperienza)
    pk5[G4.OFF_CORDIALITA] = personale[OFF_P_CORDIALITA]
    pk5[G4.OFF_ABILITA] = ab2 if bit_abilita else ab1
    pk5[G4.OFF_LINGUA] = CODICE_LINGUA_IT
    pk5[OFF_NATURA] = INDICE_NATURA[natura_nome]

    iv32 = 0
    for i, val in enumerate(iv_lista):  # ordine di IndividualValueSet: HP, ATK, DEF, SPE, SPA, SPD
        iv32 |= (val & 0x1F) << (5 * i)
    iv32 |= 1 << 31  # IsNicknamed: uno scambio porta sempre un nomignolo fissato
    struct.pack_into("<I", pk5, G4.OFF_IV32, iv32)

    pk5[G4.OFF_FLAG_GENERE] = (gender << 1) | (forma << 3)

    struct.pack_into("<H", pk5, G4.OFF_INCONTRO_DP, LOCATIONS_LINK_TRADE_5NPC)
    struct.pack_into("<H", pk5, G4.OFF_UOVO_DP, 0)
    anno, mese, giorno = DATA_INCONTRO
    pk5[G4.OFF_INCONTRO_ANNO] = (anno - 2000) & 0xFF
    pk5[G4.OFF_INCONTRO_ANNO + 1] = mese
    pk5[G4.OFF_INCONTRO_ANNO + 2] = giorno
    pk5[G4.OFF_VERSIONE] = VERSIONE_CODICE[gioco]
    pk5[G4.OFF_LIVELLO_INCONTRO] = (livello & 0x7F) | ((ot_gender & 1) << 7)
    pk5[G4.OFF_PALLA_DPPT] = PALLA_POKE

    mosse = mosse_al_livello(pkhex, specie, livello)
    mosse = (mosse + [0, 0, 0, 0])[:4]
    pp_base = I4.punti_potenza(pkhex)
    for i, m in enumerate(mosse):
        struct.pack_into("<H", pk5, 0x28 + 2 * i, m)
        pk5[0x30 + i] = pp_base.get(m, 0)

    sn = v.get("soprannomi") or {}
    al = v.get("allenatori") or {}
    soprannome_testo = sn.get("it")
    allenatore_testo = al.get("it")
    if not soprannome_testo or not allenatore_testo:
        return None, {"errore": "manca il soprannome o il nome dell'allenatore in italiano"}
    soprannome = codifica_nome5(soprannome_testo.upper())
    pk5[0x48:0x48 + len(soprannome)] = soprannome
    ot = codifica_nome5(allenatore_testo)
    pk5[G4.OFF_OT_NOME:G4.OFF_OT_NOME + len(ot)] = ot

    struct.pack_into("<H", pk5, G4.OFF_CHECKSUM, G4.somma_controllo(pk5))
    return bytes(pk5), {
        "specie": specie, "livello": livello, "pid": "0x%08X" % pid, "natura": natura_nome,
        "soprannome": soprannome_testo, "allenatore": allenatore_testo, "gioco": gioco,
        "luogo": LOCATIONS_LINK_TRADE_5NPC, "forma": forma,
        "abilita": "prima" if bit_abilita == 0 else "seconda",
    }


def scrivi_lotto(pkhex, entries, destinazione, allenatore, nomi_en):
    if not os.path.isdir(destinazione):
        os.makedirs(destinazione)
    scritti, rifiutati, impronte = [], [], {}
    for entry in entries:
        v = entry["voce"]
        byte, esito = componi(pkhex, entry, allenatore, nomi_en)
        if byte is None:
            rifiutati.append((v["specie"], v["livello"], esito["errore"]))
            continue
        # Il gioco entra nel nome perche' i due Basculin condividono specie e livello e
        # differiscono solo per versione: senza di esso il secondo file scritto avrebbe
        # sovrascritto il primo in silenzio, come e' accaduto al primo lancio di questo
        # strumento prima che il difetto fosse notato contando i file scritti sul disco.
        nome = "SCB-5-%03d-%02d-%s.pk5" % (v["specie"], v["livello"], esito["gioco"])
        io.open(os.path.join(destinazione, nome), "wb").write(byte)
        impronte[nome] = {
            "sha256": hashlib.sha256(byte).hexdigest(),
            "specie": esito["specie"], "livello": esito["livello"], "pid": esito["pid"],
            "natura": esito["natura"], "soprannome": esito["soprannome"],
            "allenatore": esito["allenatore"], "gioco": esito["gioco"], "luogo": esito["luogo"],
            "forma": esito["forma"], "abilita": esito["abilita"],
            "stato": "prodotto, in attesa del giudizio esterno",
        }
        scritti.append(nome)
    io.open(os.path.join(destinazione, "manifesto.json"), "w", encoding="utf-8").write(
        json.dumps({
            "fonte": "PKHeX.Core/Legality/Encounters/Templates/Gen5/EncounterTrade5BW.cs, tabelle "
                     "TradeGift_BW/TradeGift_B/TradeGift_W, lette il 2026-09-16",
            "data_incontro": "%04d-%02d-%02d" % DATA_INCONTRO,
            "stato": "prodotto, in attesa del giudizio esterno; nessun veicolo di quinta "
                     "generazione ancora nella raccolta del progetto",
            "voci": impronte,
        }, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    for specie, livello, errore in rifiutati:
        print("  RIFIUTATA specie %d livello %d: %s" % (specie, livello, errore))
    return scritti, rifiutati


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("la costante dello scambio locale di quinta generazione e' 30002", 30002,
          LOCATIONS_LINK_TRADE_5NPC)
    prova("non e' quella di quarta generazione", True, LOCATIONS_LINK_TRADE_5NPC != 2001)
    prova("Hardy e' la natura zero", 0, INDICE_NATURA["Hardy"])
    prova("Quirky e' la natura ventiquattro", 24, INDICE_NATURA["Quirky"])
    prova("ventiquattro nomi coprono l'intervallo", 25, len(NOMI_NATURA))
    prova("Nero vale ventuno", 21, VERSIONE_CODICE["b"])
    prova("Bianco vale venti", 20, VERSIONE_CODICE["w"])
    prova("TradeGift_B usa Nero", "b", GIOCO_PER_TABELLA["TradeGift_B"])
    prova("TradeGift_W usa Bianco", "w", GIOCO_PER_TABELLA["TradeGift_W"])

    codificato = codifica_nome5("Flò")
    prova("il nome codificato ha sette byte: tre caratteri piu' terminatore",
          8, len(codificato))
    prova("il primo carattere e' il suo punto di codice Unicode", ord("F"),
          struct.unpack_from("<H", codificato, 0)[0])
    prova("la o accentata e' il proprio punto di codice, non una tabella", ord("ò"),
          struct.unpack_from("<H", codificato, 4)[0])
    prova("il terminatore e' 0xFFFF", 0xFFFF, struct.unpack_from("<H", codificato, 6)[0])

    prova("i numeri di una lista IVs si leggono in ordine",
          [20, 20, 31, 20, 20, 20], numeri_di("new(20,20,31,20,20,20)"))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "pkhex"))
    ap.add_argument("--lotto", help="cartella in cui scrivere gli esemplari")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.lotto:
        ap.error("serve --lotto, oppure --self-test")

    global CS
    _carica_moduli()
    CS = _modulo("censimento-scambi.py", "censimento_scambi")

    pkhex = a.pkhex if os.path.isabs(a.pkhex) else os.path.join(RADICE, a.pkhex)
    entries, nomi_en, errore = leggi_scambi5(pkhex)
    if errore:
        print("rifiutato: " + errore)
        return 1
    print("Scambi in gioco di quinta generazione con valore di personalita' fissato: %d voci."
          % len(entries))

    allenatore = G4.allenatore_del_progetto()
    if allenatore is None:
        print("rifiutato: manca il registro dell'allenatore del progetto")
        return 1

    scritti, rifiutati = scrivi_lotto(pkhex, entries, a.lotto, allenatore, nomi_en)
    print("  scritti %d file in %s" % (len(scritti), a.lotto))
    print("  rifiutati %d" % len(rifiutati))
    print("  Il passo seguente non e' di questo programma: si aprono con il verificatore nel")
    print("  contesto della quinta generazione e si legge che cosa esso obietti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
