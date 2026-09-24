#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone gli scambi in gioco di quarta generazione che portano un valore di personalita' fissato.

Perche' questo strumento, e perche' non e' un dono
---------------------------------------------------
`tools/censimento-scambi.py` legge dalle tabelle del verificatore sedici voci di quarta
generazione che dichiarano un valore di personalita' fisso: sono riproducibili byte per byte,
esattamente come gli scambi di terza generazione che `tools/genera-scambio-gen3.py` gia' compone.
La fonte autorevole non e' pero' la stessa classe di quella dei doni: `EncounterTrade4PID.cs`, letta
per intero il 2026-09-15, mostra che uno scambio non arriva da un modello gia' quasi finito come un
dono, ma da un costruttore che assembla l'esemplare da zero a ogni campo. Questo programma rifa'
quella costruzione, `ConvertToPKM`, invece di adattare quella dei doni.

Il vincolo di lingua, che due voci rompono per davvero
--------------------------------------------------------
Le cartucce del progetto sono italiane, ma la fonte dichiara che due dei sedici scambi non parlano
la lingua del giocatore: sono un difetto storico del gioco vero, non un'approssimazione nostra, e
va riprodotto perche' e' cio' che rende l'esemplare quello storico.

Il Magikarp di Platino (`GetLanguageDPPt`) riceve sempre il tedesco, con l'unica eccezione di chi
gioca in tedesco, che riceve l'inglese: un giocatore italiano non rientra in quella eccezione, quindi
riceve il tedesco. Il Pikachu di Argento SoulSilver (`GetReceivedLanguage`) riceve sempre l'inglese,
con l'unica eccezione di chi gioca in inglese, che riceve il francese: un giocatore italiano riceve
quindi l'inglese. Su queste due voci il nomignolo, il nome dell'allenatore e il campo lingua
dell'esemplare NON sono italiani, e scriverli in italiano produrrebbe un esemplare che nessuno
scambio ha mai consegnato: e' la stessa avvertenza gia' registrata da `censimento-scambi.py` sulle
altre generazioni, applicata qui al caso che la lettura del sorgente ha scoperto.

Un secondo effetto della stessa regola, dichiarato e non risolto: la fonte dice anche che i giochi
inglesi di Diamante e Perla (non Platino) ricevono per errore la lingua giapponese su ogni scambio
tranne il Magikarp. Non riguarda un giocatore italiano e non produce quindi alcuna voce di questo
lotto, ma va saputo da chi in futuro estenda questo programma a un'altra lingua di partenza.

Che cosa viene dal modello e che cosa si compone
-------------------------------------------------
Valore di personalita', valori individuali, genere, abilita' concessa e identificativi sono tutti
scritti dalla fonte e si copiano senza ricalcolo. Quel che manca e va composto e' quanto un dono
gia' porta pronto: l'esperienza dal livello dichiarato, le mosse dal repertorio di livello della
specie salvo le tre voci che la fonte fissa esplicitamente, la cordialita' di base della specie, la
data di incontro fissa, e il testo di nomignolo e allenatore nella lingua che la regola sopra
assegna. Il luogo di incontro, quando il modello non ne fissa uno, e' la costante dello scambio
locale (`Locations.LinkTrade4NPC`, 2001): due sole voci, Spearow e Shuckle, dichiarano un luogo
proprio perche' furono raccolte da testimonianze dirette invece che dallo scambio generico.

Il gioco di destinazione, dichiarato invece che dedotto
---------------------------------------------------------
La tabella della fonte non lega ciascuna voce a un titolo preciso ma a un gruppo di titoli
compatibili (DPPt oppure HGSS), perche' lo scambio si riceve identico su ognuno di essi. Il
repertorio di mosse per livello differisce pero' da un titolo all'altro dentro lo stesso gruppo, e
serve quindi scegliere un titolo concreto per calcolarlo: questo programma sceglie Platino per il
gruppo DPPt e Argento SoulSilver per il gruppo HGSS, perche' sono i veicoli che il progetto ha gia'
in raccolta per il Parco Amici. E' una decisione di prodotto dichiarata e non una deduzione, e la
si cambia con `--dppt` e `--hgss`.

Uso
---
    python tools/genera-scambio-gen4.py --pkhex _notes/fonti/cloni/pkhex --lotto _notes/lotti/lotto-scambi-gen4
    python tools/genera-scambio-gen4.py --self-test
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

G4 = None    # genera-evento-gen4.py: gli offset del record e la somma di controllo
I4 = None    # genera-incontro-gen4.py: esperienza, repertorio di livello, tabella caratteri
CS = None    # censimento-scambi.py: la lettura delle tabelle di scambio dalla fonte

DIM_PERSONALE = 0x2C
OFF_P_GENERE = 0x10
OFF_P_CORDIALITA = 0x12
OFF_P_CRESCITA = 0x13
OFF_P_ABILITA1 = 0x16
OFF_P_ABILITA2 = 0x17
PERSONALE = "personal_hgss"  # copre tutte e sei le versioni di quarta, per costruzione della fonte

# I nomi di lingua che il censimento deve leggere. "de" si aggiunge al gruppo predefinito it/en/ja
# soltanto qui, perche' serve al solo Magikarp e non ha ragione di entrare nell'uscita condivisa
# del censimento.
LINGUE = ("it", "en", "de", "ja")

# Il codice di lingua scritto nel campo dell'esemplare, dalla tavola gia' verificata sul progetto
# leggendo il byte 0x12 di 172 file prodotti (vedi sessione del 2026-09-15).
CODICE_LINGUA = {"ja": 1, "en": 2, "fr": 3, "it": 4, "de": 5, "es": 7}

# Le due voci per cui la lingua ricevuta da un giocatore italiano non e' l'italiano, da
# `EncounterTrade4PID.GetReceivedLanguage` e `GetLanguageDPPt`, lette il 2026-09-15.
LINGUA_SPECIALE = {"Magikarp": "de", "Pikachu": "en"}

LOCATIONS_LINK_TRADE_4NPC = 2001
PALLA_POKE = 4
DATA_INCONTRO = (2026, 9, 15)

VERSIONI_CONCRETE_DEFAULT = {"DPPt": "pt", "HGSS": "ss"}
VERSIONE_CODICE = {"d": 10, "p": 11, "pt": 12, "hg": 7, "ss": 8}

TABELLE_VALIDE = ("TradeGift_DPPtIngame", "TradeGift_HGSS")


def _modulo(nome_file, alias):
    percorso = os.path.join(RADICE, "tools", nome_file)
    spec = importlib.util.spec_from_file_location(alias, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _carica_moduli():
    global G4, I4
    G4 = _modulo("genera-evento-gen4.py", "genera_evento_gen4")
    I4 = _modulo("genera-incontro-gen4.py", "genera_incontro_gen4")
    I4.G4 = G4
    I4.I3 = _modulo("genera-incontro-gen3.py", "genera_incontro_gen3")
    I4.I3.G3 = I4.I3._fratello()


def numeri_di(testo):
    """Gli interi separati da virgola dentro una `new(...)`, per esempio la lista di mosse."""
    m = re.search(r"new\(([^()]*)\)", testo)
    if not m:
        return []
    return [int(x) for x in re.split(r"\s*,\s*", m.group(1).strip()) if x]


def leggi_scambi4(pkhex):
    """Le sedici voci di quarta generazione con valore di personalita' fissato, dalla fonte.

    Rilegge le tabelle con `censimento-scambi.py` invece di trascriverle, per lo stesso motivo per
    cui quello strumento esiste: leggere dal sorgente evita una trascrizione che sbaglierebbe in
    modo invisibile. La lettura qui chiede anche il tedesco, che il censimento condiviso non porta
    perche' nessun'altra classe ne ha bisogno.
    """
    nomi_en = CS.nomi_specie(os.path.join(pkhex, CS.NOMI_EN))
    if nomi_en is None:
        return None, None, "mancano i nomi delle specie sotto " + pkhex
    tabelle_lette = CS.censisci(pkhex, nomi_en, lingue=LINGUE)
    if tabelle_lette is None:
        return None, None, "manca la cartella delle tabelle sotto " + pkhex
    fuori = []
    for t in tabelle_lette:
        if t["generazione"] != "4" or t["tabella"] not in TABELLE_VALIDE:
            continue
        gruppo_versione = "DPPt" if t["tabella"] == "TradeGift_DPPtIngame" else "HGSS"
        for v in t["voci"]:
            if not v["pid"]:
                continue
            fuori.append({"gruppo_versione": gruppo_versione, "voce": v})
    return fuori, nomi_en, None


def voce_personale(pkhex, nazionale):
    dati = io.open(os.path.join(pkhex, I4.CARTELLA_PERSONALI, PERSONALE), "rb").read()
    inizio = nazionale * DIM_PERSONALE
    blocco = dati[inizio:inizio + DIM_PERSONALE]
    if len(blocco) < DIM_PERSONALE:
        raise KeyError("numero nazionale fuori dalla tabella personale: %d" % nazionale)
    return blocco


def lingua_ricevuta(nome_specie_en, lingua_giocatore):
    """La lingua che l'esemplare riceve davvero, secondo `GetReceivedLanguage`/`GetLanguageDPPt`.

    Per un giocatore italiano nessuna delle due funzioni innesca il ramo del bug su Diamante e
    Perla inglesi, quindi la sola deviazione dall'italiano e' quella delle due specie speciali.
    """
    return LINGUA_SPECIALE.get(nome_specie_en, lingua_giocatore)


def componi(pkhex, entry, allenatore, caratteri, versioni_concrete, nomi_en):
    v = entry["voce"]
    gruppo_versione = entry["gruppo_versione"]
    props = v["proprieta"]
    specie = v["specie"]
    livello = v["livello"]
    pid = int(v["pid"], 16)
    tid = int(props.get("TID16", "0"))
    sid = int(props.get("SID16", "0"))
    ot_gender = int(props.get("OTGender", "0"))
    gender = int(props.get("Gender", "0"))
    ability_dichiarata = props.get("Ability", "")
    contest = int(props.get("Contest", "0"))
    met_location = props.get("MetLocation")
    iv_lista = numeri_di(props.get("IVs", ""))
    if len(iv_lista) != 6:
        return None, {"errore": "IVs non leggibili dalla proprieta': %r" % props.get("IVs")}
    mosse_fisse = numeri_di(props.get("Moves", "")) if "Moves" in props else None

    personale = voce_personale(pkhex, specie)
    ab1, ab2 = personale[OFF_P_ABILITA1], personale[OFF_P_ABILITA2]
    bit_abilita = 0 if ab1 == ab2 else (pid & 1)
    # Presidio: il valore di personalita' e' fissato dalla fonte, quindi la sua parita' deve gia'
    # concordare con l'abilita' che la fonte stessa dichiara. Se non concordasse, o il valore di
    # personalita' letto o l'etichetta dell'abilita' sarebbero stati letti nel posto sbagliato.
    attesa = 1 if "OnlySecond" in ability_dichiarata else (0 if "OnlyFirst" in ability_dichiarata
                                                            else None)
    if attesa is not None and attesa != bit_abilita and ab1 != ab2:
        return None, {"errore": ("l'abilita' dichiarata (%s) non concorda con la parita' del "
                                 "valore di personalita' 0x%08X" % (ability_dichiarata, pid))}

    versione_concreta = versioni_concrete[gruppo_versione]
    esperienza = I4.esperienza(personale[OFF_P_CRESCITA], livello)

    pk4 = bytearray(G4.DIM_PK4_SCATOLA)
    struct.pack_into("<I", pk4, G4.OFF_PID, pid)
    struct.pack_into("<H", pk4, G4.OFF_SANITA, 0)
    struct.pack_into("<H", pk4, G4.OFF_SPECIE, specie)
    struct.pack_into("<H", pk4, G4.OFF_TID, tid & 0xFFFF)
    struct.pack_into("<H", pk4, G4.OFF_SID, sid & 0xFFFF)
    struct.pack_into("<I", pk4, G4.OFF_ESPERIENZA, esperienza)
    pk4[G4.OFF_CORDIALITA] = personale[OFF_P_CORDIALITA]
    pk4[G4.OFF_ABILITA] = ab2 if bit_abilita else ab1

    nome_en = nomi_en[specie] if specie < len(nomi_en) else ""
    lingua = lingua_ricevuta(nome_en, "it")
    pk4[G4.OFF_LINGUA] = CODICE_LINGUA[lingua]

    iv32 = 0
    for i, val in enumerate(iv_lista):  # ordine della fonte: HP, ATK, DEF, SPE, SPA, SPD
        iv32 |= (val & 0x1F) << (5 * i)
    iv32 |= 1 << 31  # IsNicknamed: uno scambio porta sempre un nomignolo fissato
    struct.pack_into("<I", pk4, G4.OFF_IV32, iv32)

    # Il genere e' un campo indipendente in uno scambio, non derivato dal valore di personalita'
    # come in un incontro selvatico: si scrive quello che la fonte dichiara.
    pk4[G4.OFF_FLAG_GENERE] = gender << 1

    luogo = LOCATIONS_LINK_TRADE_4NPC if met_location is None else int(met_location)
    struct.pack_into("<H", pk4, G4.OFF_INCONTRO_DP, luogo)
    struct.pack_into("<H", pk4, G4.OFF_INCONTRO_ESTESO, luogo)
    struct.pack_into("<H", pk4, G4.OFF_UOVO_DP, 0)
    struct.pack_into("<H", pk4, G4.OFF_UOVO_ESTESO, 0)
    anno, mese, giorno = DATA_INCONTRO
    pk4[G4.OFF_INCONTRO_ANNO] = (anno - 2000) & 0xFF
    pk4[G4.OFF_INCONTRO_ANNO + 1] = mese
    pk4[G4.OFF_INCONTRO_ANNO + 2] = giorno
    pk4[G4.OFF_VERSIONE] = VERSIONE_CODICE[versione_concreta]
    # Il campo del genere dell'allenatore che cede l'esemplare vive nel bit alto del livello di
    # incontro, per la stessa ragione per cui `genera-evento-gen4.py` maschera quel campo con
    # 0x7F in lettura.
    pk4[G4.OFF_LIVELLO_INCONTRO] = (livello & 0x7F) | ((ot_gender & 1) << 7)
    pk4[G4.OFF_PALLA_DPPT] = PALLA_POKE
    pk4[G4.OFF_PALLA_HGSS] = PALLA_POKE

    if mosse_fisse:
        mosse = (mosse_fisse + [0, 0, 0, 0])[:4]
    else:
        mosse = I4.mosse_al_livello(pkhex, versione_concreta, specie, livello)
        mosse = (mosse + [0, 0, 0, 0])[:4]
    pp_base = I4.punti_potenza(pkhex)
    for i, m in enumerate(mosse):
        struct.pack_into("<H", pk4, 0x28 + 2 * i, m)
        pk4[0x30 + i] = pp_base.get(m, 0)

    pk4[0x1E] = contest  # ContestCool: la sola statistica da gara che la fonte fissi in queste voci
    # Le altre quattro statistiche da gara (0x1F-0x22) restano a zero perche' la fonte non ne
    # dichiara altre per alcuna delle sedici voci: non e' un valore lasciato di default, e' il
    # valore che la fonte stessa assegna.

    sn = v.get("soprannomi") or {}
    al = v.get("allenatori") or {}
    soprannome_testo = sn.get(lingua)
    allenatore_testo = al.get(lingua)
    if not soprannome_testo or not allenatore_testo:
        return None, {"errore": "manca il soprannome o il nome dell'allenatore in lingua '%s'"
                                % lingua}
    soprannome = I4.codifica_nome(soprannome_testo.upper(), caratteri)
    pk4[0x48:0x48 + len(soprannome)] = soprannome
    ot = I4.codifica_nome(allenatore_testo, caratteri)
    pk4[G4.OFF_OT_NOME:G4.OFF_OT_NOME + len(ot)] = ot

    struct.pack_into("<H", pk4, G4.OFF_CHECKSUM, G4.somma_controllo(pk4))
    return bytes(pk4), {
        "specie": specie, "livello": livello, "pid": "0x%08X" % pid, "lingua": lingua,
        "soprannome": soprannome_testo, "allenatore": allenatore_testo,
        "versione_concreta": versione_concreta, "luogo": luogo,
        "abilita": "prima" if bit_abilita == 0 else "seconda",
        "mosse_fisse": bool(mosse_fisse),
    }


def scrivi_lotto(pkhex, entries, destinazione, allenatore, versioni_concrete, nomi_en):
    if not os.path.isdir(destinazione):
        os.makedirs(destinazione)
    caratteri = I4.tabella_caratteri(pkhex)
    scritti, rifiutati, impronte = [], [], {}
    for entry in entries:
        v = entry["voce"]
        byte, esito = componi(pkhex, entry, allenatore, caratteri, versioni_concrete, nomi_en)
        if byte is None:
            rifiutati.append((v["specie"], v["livello"], esito["errore"]))
            continue
        nome = "SCB-4-%03d-%02d.pk4" % (v["specie"], v["livello"])
        io.open(os.path.join(destinazione, nome), "wb").write(byte)
        impronte[nome] = {
            "sha256": hashlib.sha256(byte).hexdigest(),
            "specie": esito["specie"], "livello": esito["livello"], "pid": esito["pid"],
            "lingua": esito["lingua"], "soprannome": esito["soprannome"],
            "allenatore": esito["allenatore"], "versione_concreta": esito["versione_concreta"],
            "luogo": esito["luogo"], "abilita": esito["abilita"],
            "mosse_fisse": esito["mosse_fisse"], "stato": "prodotto, in attesa del giudizio",
        }
        scritti.append(nome)
    io.open(os.path.join(destinazione, "manifesto.json"), "w", encoding="utf-8").write(
        json.dumps({
            "fonte": "PKHeX.Core/Legality/Encounters/Data/Gen4/Encounters4{DPPt,HGSS}.cs, "
                     "tabelle TradeGift_DPPtIngame e TradeGift_HGSS, lette il 2026-09-15",
            "gioco_concreto_per_gruppo": versioni_concrete,
            "data_incontro": "%04d-%02d-%02d" % DATA_INCONTRO,
            "stato": "prodotto, in attesa del giudizio esterno",
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

    prova("i numeri di una lista Moves si leggono in ordine",
          [43, 31, 228, 332], numeri_di("new(043,031,228,332)"))
    prova("una proprieta' senza parentesi non produce numeri", [], numeri_di("OnlyFirst"))
    prova("il Magikarp riceve il tedesco da un giocatore italiano",
          "de", lingua_ricevuta("Magikarp", "it"))
    prova("il Pikachu riceve l'inglese da un giocatore italiano",
          "en", lingua_ricevuta("Pikachu", "it"))
    prova("una specie ordinaria riceve la lingua del giocatore",
          "it", lingua_ricevuta("Onix", "it"))
    prova("la costante dello scambio locale e' 2001", 2001, LOCATIONS_LINK_TRADE_4NPC)
    prova("il codice lingua italiano e' quattro, dalla tavola empirica del progetto",
          4, CODICE_LINGUA["it"])
    prova("il codice lingua tedesco e' cinque", 5, CODICE_LINGUA["de"])

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "cloni", "pkhex"))
    ap.add_argument("--lotto", help="cartella in cui scrivere gli esemplari")
    ap.add_argument("--dppt", default="pt", choices=sorted(k for k in VERSIONE_CODICE if k in
                                                            ("d", "p", "pt")),
                    help="il titolo concreto del gruppo DPPt su cui calcolare le mosse di livello")
    ap.add_argument("--hgss", default="ss", choices=sorted(k for k in VERSIONE_CODICE if k in
                                                            ("hg", "ss")),
                    help="il titolo concreto del gruppo HGSS su cui calcolare le mosse di livello")
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
    entries, nomi_en, errore = leggi_scambi4(pkhex)
    if errore:
        print("rifiutato: " + errore)
        return 1
    print("Scambi in gioco di quarta generazione con valore di personalita' fissato: %d voci."
          % len(entries))

    allenatore = G4.allenatore_del_progetto()
    if allenatore is None:
        print("rifiutato: manca il registro dell'allenatore del progetto")
        return 1

    versioni_concrete = {"DPPt": a.dppt, "HGSS": a.hgss}
    scritti, rifiutati = scrivi_lotto(pkhex, entries, a.lotto, allenatore, versioni_concrete, nomi_en)
    print("  scritti %d file in %s" % (len(scritti), a.lotto))
    print("  rifiutati %d" % len(rifiutati))
    print("  Il passo seguente non e' di questo programma: si aprono con il verificatore nel")
    print("  contesto della quarta generazione e si legge che cosa esso obietti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
