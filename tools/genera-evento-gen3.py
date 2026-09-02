#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone un esemplare da evento di generazione 3 e lo scrive nella forma di scambio.

Perché esiste
-------------
È il passo che il progetto ha dichiarato aperto il 2026-08-28 e non ha mai eseguito:
costruire un esemplare con il proprio codice e sottoporlo a un verificatore di conformità
indipendente, per sapere se una ricreazione fedele passi i controlli. Non richiede hardware,
non tocca alcun account e non produce nulla destinato a una collezione: produce un caso di
prova. La verifica che ne segue la compie una persona, aprendo il file prodotto con lo
strumento di conformità della comunità e leggendo che cosa esso obietta.

Che cosa fa, e su quali basi
----------------------------
Il valore di personalità, i sei valori individuali e il sesso dell'allenatore di provenienza
non sono scelti: discendono dal seme attraverso le formule di `pokebridge.eventi`, verificate
su un corpus di duecentonove esemplari conservati. Su questa parte il grado di fiducia è alto
e documentato.

Tutto il resto è metadato dell'evento, cioè identificativo dell'allenatore, nome, lingua,
livello, specie, mosse, sfera e luogo di incontro, e viene da fonti di grado diverso che il
programma dichiara una per una nel proprio rapporto. Alcune di esse portano nel codice
d'origine la parola segnaposto, ed è precisamente la ragione per cui questo programma non
tace la provenienza di alcun campo: l'esperimento consiste nel far dire al verificatore quali
di quei campi sono sbagliati, e un campo la cui provenienza non sia dichiarata non insegna
nulla quando viene contestato.

Le correzioni, e chi le autorizza
---------------------------------
Su alcuni campi il corpus del costruttore e il suo codice non concordano: il corpus dichiara un
valore e il codice lo sovrascrive con un caso speciale. Davanti a una divergenza interna alla
fonte questo programma non sceglie a occhio: attende che un verificatore indipendente dica quale
delle due parti ha ragione, e registra la risposta nella tavola delle correzioni con l'autorità e
la data. Il rapporto dichiara poi la correzione accanto al valore, cosicché nessun campo cambi in
silenzio rispetto alla fonte da cui è stato letto.

La prima voce di quella tavola è nata così. Il rapporto del primo esemplare prodotto marcava il
contrassegno dell'incontro fatidico come contraddittorio nella fonte; il verificatore ha
contestato quel solo campo e nessun altro; la tavola registra il valore corretto con la citazione
dell'obiezione. È il modo in cui la dichiarazione di provenienza si è ripagata alla prima corsa.

Le due forme del dato
---------------------
Il programma scrive due file. Quello con estensione `.pk3` è la forma decifrata a ordine
fisso, che è ciò che gli strumenti della comunità accettano in ingresso. Quello con
estensione `.ek3` è la forma che il salvataggio contiene, cioè permutata secondo il valore di
personalità e cifrata. Contengono gli stessi dati e la conversione è esatta nei due versi.

Uso
---
    python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --elenco
    python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --evento 10ANNI --specie Pikachu --seme 0x9DF6 --lingua ITA --out _notes/prova
    python tools/genera-evento-gen3.py --self-test

Il sorgente del costruttore della comunità, da cui vengono i metadati, non è una dipendenza
di questo repository e non vi entra: si ottiene con `tools/confronta-ace-builder.py --scarica`.
"""

import argparse
import io
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))

from pokebridge import charmap as cm  # noqa: E402
from pokebridge import eventi  # noqa: E402
from pokebridge import gen3  # noqa: E402

CORPUS = "src/data/Mystery gift pokemon gen 3.json"
MOVESET = "src/data/gen3_event_movesets.json"
SPECIE = "src/data/species.gen3.js"
GRUPPI = "src/data/expGroups.gen3.js"
MOSSE = "src/data/moves.gen3.data.js"

# I giochi di origine per nome, dal tavolo verificato di `pokebridge.gen3`. Il campo va
# scelto e non subito, perché da esso dipende quale porta verso il deposito in rete
# l'esemplare potrà impiegare: la porta che si apre a ottobre 2026 accetta i soli due titoli
# della riedizione, e un esemplare che dichiari un altro titolo dovrà comunque trovarsi in un
# salvataggio di quei due, condizione in cui le fonti dichiarano ignoto se il servizio lo
# accetti. Dichiarare l'origine compatibile con la porta rimuove l'incognita invece di
# aggirarla.
GIOCHI = {v.lower().replace(" ", ""): k for k, v in gen3.ORIGIN_GAMES.items() if k}

# I codici di lingua del byte a 0x12. Vengono dalle chiavi che il corpus usa per i nomi
# dell'allenatore per lingua, e coincidono con la numerazione nota della generazione 3.
LINGUE = {"JPN": 1, "ENG": 2, "FRA": 3, "ITA": 4, "GER": 5, "SPA": 7}

# I gruppi di crescita, nell'ordine in cui il costruttore li numera.
MEDIUM_FAST, ERRATIC, FLUCTUATING, MEDIUM_SLOW, FAST, SLOW = range(6)

# Le correzioni ai metadati del corpus, ciascuna con l'autorità che la impone. Questa tavola
# esiste perché il corpus del costruttore e il codice del costruttore, su alcuni campi, non
# concordano fra loro: il corpus dichiara un valore e il codice lo sovrascrive con un caso
# speciale. Dove le due parti divergono non si sceglie a occhio, si aspetta che un verificatore
# indipendente dica quale ha ragione, e si registra la sua risposta qui con la data.
#
# Schema: (sigla evento, campo, valore corretto, autorità e data)
CORREZIONI = [
    ("10ANNI", "fateful", False,
     "PKHeX 26.08.26, il 2026-09-01, sul primo esemplare prodotto da questo programma: "
     "unica obiezione del rapporto, «Fateful: Evento Speciale non dovrebbe essere "
     "selezionato». Il corpus dichiarava il contrassegno attivo, il codice del costruttore "
     "lo disattiva con un caso speciale dedicato a questo evento, e il verificatore conferma "
     "il codice contro il corpus"),
]


def esperienza(gruppo, livello):
    """L'esperienza totale per raggiungere un livello, secondo il gruppo di crescita.

    Le sei formule sono quelle canoniche della generazione 3. Vanno segnalate come non
    verificate sul disassemblato da questo progetto: sono state trascritte dalla loro forma
    corrente e il verificatore esterno è precisamente lo strumento che dirà se sono giuste,
    perché un'esperienza incoerente con il livello è fra le prime cose che esso controlla.
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


def leggi(ace, rel):
    p = os.path.join(ace, rel.replace("/", os.sep))
    if not os.path.exists(p):
        sys.exit("manca " + rel + " sotto " + ace + ".\n"
                 "Si ottiene con: python tools/confronta-ace-builder.py --scarica " + ace)
    return io.open(p, encoding="utf-8", errors="ignore").read()


def specie_per_nome(ace):
    """Nome della specie verso identificativo interno, e l'inverso."""
    testo = leggi(ace, SPECIE)
    per_nome, per_id = {}, {}
    for numero, nome in re.findall(r"\[\s*(\d+)\s*,\s*\"([^\"]+)\"\s*\]", testo):
        per_nome[nome.lower()] = int(numero)
        per_id.setdefault(int(numero), nome)
    return per_nome, per_id


def gruppo_di_crescita(ace):
    """Identificativo interno di specie verso gruppo di crescita."""
    testo = leggi(ace, GRUPPI)
    nomi = {"MEDIUM_FAST": MEDIUM_FAST, "ERRATIC": ERRATIC, "FLUCTUATING": FLUCTUATING,
            "MEDIUM_SLOW": MEDIUM_SLOW, "FAST": FAST, "SLOW": SLOW}
    fuori = {}
    for etichetta, valore in nomi.items():
        m = re.search(r"export const " + etichetta + r"\s*=\s*\[([^\]]*)\]", testo)
        if not m:
            continue
        for numero in re.findall(r"\d+", m.group(1)):
            fuori[int(numero)] = valore
    return fuori


def punti_potenza(ace):
    """Identificativo di mossa verso i suoi punti potenza di base.

    Il file delle mosse è la conversione di un foglio di calcolo, e la colonna
    dell'identificativo ha per nome la stringa vuota: si cerca quindi una chiave `""` e non
    una chiave `id`, che non esiste. Cercare il nome sbagliato non produce un errore ma un
    dizionario vuoto, e i punti potenza restano a zero senza che nulla lo segnali.
    """
    testo = leggi(ace, MOSSE)
    fuori = {}
    for blocco in re.finditer(r"\{[^{}]*\}", testo):
        corpo = blocco.group(0)
        numero = re.search(r"\"\"\s*:\s*(\d+)", corpo)
        pp = re.search(r"\"PP\"\s*:\s*(\d+)", corpo)
        if numero and pp:
            fuori[int(numero.group(1))] = int(pp.group(1))
    return fuori


def corpus(ace):
    p = os.path.join(ace, CORPUS.replace("/", os.sep))
    if not os.path.exists(p):
        sys.exit("manca il corpus degli eventi sotto " + ace + ".\n"
                 "Lo scarica `tools/confronta-ace-builder.py --scarica`, che lo prende a "
                 "parte perché il costruttore lo carica a tempo di esecuzione.")
    return json.load(io.open(p, encoding="utf-8"))


def movimenti(ace):
    p = os.path.join(ace, MOVESET.replace("/", os.sep))
    if not os.path.exists(p):
        return {}
    return json.load(io.open(p, encoding="utf-8"))


def etichette(ace):
    """Sigla dell'evento verso etichetta leggibile, dalla funzione che le mappa.

    Serve perché le due tabelle del costruttore usano chiavi diverse: gli eventi sono
    indicizzati per sigla, le mosse per etichetta. Cercare per sigla in quella delle mosse
    non produce un errore ma zero risultati, e un esemplare senza mosse sembra una lacuna
    della fonte invece di un difetto della nostra lettura.
    """
    testo = leggi(ace, "src/main.js")
    m = re.search(r"const labels = \{(.*?)\};", testo, re.S)
    if not m:
        return {}
    fuori = {}
    for chiave, valore in re.findall(r"'?([A-Z0-9_]+)'?\s*:\s*'([^']+)'", m.group(1)):
        fuori[chiave.upper()] = valore
    return fuori


def elenca(ace):
    dati = corpus(ace)
    _per_nome, per_id = specie_per_nome(ace)
    print("")
    print("=== Eventi disponibili nel corpus del costruttore")
    for tag, ev in sorted(dati.get("events", {}).items()):
        specie = ev.get("species") or []
        nomi = ", ".join(per_id.get(s, str(s)) for s in specie[:12])
        print("")
        print("  " + tag)
        print("    allenatore " + str(ev.get("ot_name")) + ", identificativo " +
              str(ev.get("fixedTID")) + ", livello " + str(ev.get("defaultMetLevel")))
        print("    metodo " + str(ev.get("pidMethod") or "non dichiarato") +
              ", lucentezza bloccata " + str(bool(ev.get("shinyLocked"))) +
              ", incontro fatidico " + str(bool(ev.get("defaultFatefulEncounter"))))
        print("    specie (" + str(len(specie)) + "): " + nomi)
        if ev.get("ot_names"):
            print("    allenatore per lingua: " +
                  ", ".join(k + "=" + v for k, v in sorted(ev["ot_names"].items())))
    return 0


def componi(ace, tag, nome_specie, seme, lingua, gioco=None, verbose=False):
    """Compone la struttura, e restituisce l'oggetto insieme al rapporto di provenienza."""
    dati = corpus(ace)
    eventi_noti = dati.get("events", {})
    if tag not in eventi_noti:
        sys.exit("evento " + tag + " non presente nel corpus; --elenco li mostra tutti")
    ev = eventi_noti[tag]

    per_nome, per_id = specie_per_nome(ace)
    if nome_specie.lower() not in per_nome:
        sys.exit("specie " + nome_specie + " non riconosciuta")
    specie_id = per_nome[nome_specie.lower()]
    if ev.get("species") and specie_id not in ev["species"]:
        sys.exit("la specie " + nome_specie + " non appartiene all'evento " + tag +
                 "; --elenco mostra quali vi appartengono")

    if lingua not in LINGUE:
        sys.exit("lingua " + lingua + " sconosciuta; ammesse: " + ", ".join(LINGUE))
    codice_lingua = LINGUE[lingua]

    nome_ot = (ev.get("ot_names") or {}).get(str(codice_lingua)) or ev.get("ot_name") or ""
    tid = int(ev.get("fixedTID") or 0)
    sid = int(ev.get("fixedSID") or 0)
    livello = int(ev.get("defaultMetLevel") or ev.get("current_level") or 5)

    personalita, iv = eventi.personalita_e_iv(seme)
    sesso_ot = eventi.sesso_allenatore_rand_s7(seme)

    gruppi = gruppo_di_crescita(ace)
    gruppo = gruppi.get(specie_id)
    if gruppo is None:
        sys.exit("gruppo di crescita non noto per la specie " + str(specie_id) +
                 ": il dato del costruttore non la copre, e inventarlo produrrebbe "
                 "un'esperienza incoerente con il livello")

    mosse_evento = movimenti(ace)
    # Le chiavi possibili, in ordine di specificità: l'etichetta dichiarata dall'evento,
    # quella della tabella di corrispondenza, e la sigla stessa. Il confronto è fatto su
    # chiavi normalizzate perché le due tabelle differiscono per maiuscole e accenti.
    def normalizza(t):
        return re.sub(r"[^a-z0-9]", "", str(t or "").lower())

    per_normale = {normalizza(k): v for k, v in mosse_evento.items()}
    candidate = [ev.get("label"), etichette(ace).get(tag.upper()), tag,
                 tag.replace("_", " ")]
    mosse = []
    for chiave in candidate:
        blocco = per_normale.get(normalizza(chiave))
        if not isinstance(blocco, dict):
            continue
        per_specie = {normalizza(k): v for k, v in blocco.items()}
        voci = per_specie.get(normalizza(per_id.get(specie_id, ""))) or []
        mosse = [int(v["index"]) for v in voci if isinstance(v, dict) and "index" in v]
        if mosse:
            break
    pp_base = punti_potenza(ace)
    pp = [pp_base.get(m, 0) for m in mosse]

    tabella = cm.Charmap.gen3()
    nome_visibile = per_id.get(specie_id, "").upper()
    try:
        soprannome = tabella.encode(nome_visibile, length=gen3.NICKNAME_LENGTH)
    except ValueError as e:
        sys.exit("il nome della specie non si codifica: " + str(e))
    try:
        ot_bytes = tabella.encode(nome_ot, length=gen3.OT_NAME_LENGTH)
    except ValueError as e:
        sys.exit("il nome dell'allenatore non si codifica: " + str(e) + "\n"
                 "È il caso che la tabella dei caratteri decide, e su cui il confronto con "
                 "il costruttore ha trovato un disaccordo negli accentati.")

    # Le correzioni si applicano qui, dopo la lettura dei metadati e prima della
    # costruzione, cosicché il rapporto possa dichiararle insieme al valore corretto.
    gioco_id = int(ev.get("defaultOriginGame") or 2)
    if gioco is not None:
        chiave = str(gioco).lower().replace(" ", "")
        if chiave.isdigit():
            gioco_id = int(chiave)
        elif chiave in GIOCHI:
            gioco_id = GIOCHI[chiave]
        else:
            sys.exit("gioco di origine non riconosciuto: " + str(gioco) + "\n"
                     "ammessi, per nome o per numero: " +
                     ", ".join("%s=%d" % (n, i) for n, i in sorted(GIOCHI.items(),
                                                                   key=lambda x: x[1])))
    ammessi = ev.get("allowedOriginGames")
    if ammessi and gioco_id not in [int(x) for x in ammessi]:
        sys.exit("l'evento dichiara come giochi di origine ammessi " + str(ammessi) +
                 " e " + str(gioco_id) + " non vi appartiene")

    fatidico = bool(ev.get("defaultFatefulEncounter"))
    correzioni_applicate = []
    for sigla, campo, valore, autorita in CORREZIONI:
        if sigla != tag:
            continue
        if campo == "fateful":
            if fatidico != valore:
                correzioni_applicate.append((campo, fatidico, valore, autorita))
            fatidico = valore

    mon = gen3.Gen3Mon(
        personality=personalita,
        ot_id=(tid | (sid << 16)) & 0xFFFFFFFF,
        nickname=soprannome,
        language=codice_lingua,
        # Bit 1: la struttura contiene una specie. Senza di esso il gioco la tratta come
        # una casella vuota, che è il modo più silenzioso di produrre un file inerte.
        flags=0x02,
        ot_name=ot_bytes,
        markings=0,
        growth=gen3.Growth(species=specie_id, held_item=0,
                           experience=esperienza(gruppo, livello),
                           pp_bonuses=0, friendship=int(ev.get("friendship") or 70)),
        attacks=gen3.Attacks(moves=(mosse + [0, 0, 0, 0])[:4], pp=(pp + [0, 0, 0, 0])[:4]),
        evs=gen3.EvsCondition(),
        misc=gen3.Misc(
            pokerus=0,
            met_location=int(ev.get("defaultMetLocationId") or 255),
            met_level=livello,
            met_game=gioco_id,
            pokeball=4,
            ot_female=(sesso_ot == "femmina"),
            ivs={n: iv[k] for n, k in zip(gen3.EV_ORDER, eventi.ORDINE_IV)},
            is_egg=False,
            ability_num=personalita & 0x01,
            modern_fateful_encounter=fatidico,
        ),
    )

    rapporto = [
        ("valore di personalità", "0x%08X" % personalita,
         "derivato dal seme, formula verificata su 208 vettori su 209"),
        ("valori individuali", ", ".join("%s=%d" % (k, iv[k]) for k in eventi.ORDINE_IV),
         "derivati dal seme, formula verificata su 209 vettori su 209"),
        ("sesso dell'allenatore", sesso_ot,
         "derivato dal seme con la derivazione a scorrimento di sette, verificata su 100 "
         "vettori su 100 fra gli eventi che la usano"),
        ("identificativo dell'allenatore", str(tid) + " con segreto " + str(sid),
         "corpus del costruttore; concorda con il catalogo generato da PKHeX"),
        ("nome dell'allenatore", nome_ot,
         "corpus del costruttore, tabella per lingua; concorda con il catalogo per l'italiano"),
        ("lingua", lingua + " (" + str(codice_lingua) + ")",
         "numerazione nota della generazione 3, non verificata sul disassemblato"),
        ("specie", per_id.get(specie_id, "?") + " (" + str(specie_id) + ")",
         "identificativo interno dal costruttore, il cui file dichiara di essere un "
         "sottoinsieme di esempio: da verificare"),
        ("livello e luogo di incontro", str(livello) + " a " +
         str(mon.misc.met_location), "corpus del costruttore"),
        ("esperienza", str(mon.growth.experience),
         "calcolata dalla formula canonica del gruppo di crescita " + str(gruppo) +
         "; la formula NON è verificata sul disassemblato da questo progetto"),
        ("mosse", ", ".join(str(m) for m in mon.attacks.moves) or "nessuna",
         "tabella delle mosse per evento del costruttore" if mosse
         else "NON TROVATE nel costruttore per questa specie: restano a zero, e un "
              "verificatore lo contesterà"),
        ("punti potenza", ", ".join(str(p) for p in mon.attacks.pp),
         "valori di base delle mosse dal costruttore, senza alcun PP Up"),
        ("sfera", "4",
         "SEGNAPOSTO: il file dei contenitori del costruttore dichiara di essere una "
         "mappatura provvisoria da confermare. È il campo con la provenienza peggiore"),
        ("gioco di origine", gen3.ORIGIN_GAMES.get(gioco_id, "?") +
         " (" + str(gioco_id) + ")",
         ("scelto sulla riga di comando; il corpus proponeva " +
          gen3.ORIGIN_GAMES.get(int(ev.get("defaultOriginGame") or 2), "?") +
          " e l'evento non dichiara alcun insieme di giochi ammessi, quindi il valore non è "
          "vincolato dalla fonte")
         if gioco is not None else
         "corpus del costruttore come valore per difetto, non come vincolo: l'evento non "
         "dichiara alcun insieme di giochi ammessi. Va notato che da questo campo dipende "
         "quale porta verso il deposito l'esemplare potrà impiegare, quindi conviene "
         "scegliersi con --gioco invece di accettare il difetto"),
        ("incontro fatidico", str(mon.misc.modern_fateful_encounter),
         ("CORRETTO rispetto al corpus, che dichiarava " +
          str(correzioni_applicate[0][1]) + ". " + correzioni_applicate[0][3])
         if correzioni_applicate else
         "corpus del costruttore. Dove il corpus e il codice del costruttore divergono su "
         "questo campo, la tavola delle correzioni registra quale dei due un verificatore "
         "indipendente ha confermato; per questo evento non c'è divergenza registrata"),
        ("abilità", str(mon.misc.ability_num),
         "bit meno significativo del valore di personalità, che è la regola ordinaria"),
        ("EV, statistiche da gara, lucentezza estetica, nastri, Pokerus", "tutti a zero",
         "scelta deliberata: un esemplare appena distribuito non ne ha, e metterne "
         "qualcuno sarebbe inventare"),
    ]
    return mon, rapporto


def b32(x):
    """Un intero a trentadue bit in binario, spezzato fra le due metà."""
    t = format(x & 0xFFFFFFFF, "032b")
    return t[:16] + " " + t[16:]


def b16_campi(x):
    """Un intero a sedici bit spezzato nei tre campi da cinque bit e nel bit inutilizzato."""
    t = format(x & 0xFFFF, "016b")
    return t[:1] + " " + t[1:6] + " " + t[6:11] + " " + t[11:]


def derivazione(seme, tid, sid, soglia_sesso=None):
    """Stampa la catena completa dal seme ai campi derivati, in esadecimale e in binario.

    Serve a due cose. La prima è documentaria: la nota di studio e la tesi riportano questa
    derivazione, e chi le legge deve poterla rifare con un comando invece di fidarsi di numeri
    trascritti. La seconda è diagnostica: quando un verificatore esterno contesta un campo
    derivato, la sola informazione utile è quale passo della catena lo produce.
    """
    print("")
    print("=== gli stati del generatore, e perché si usa la metà alta")
    stato, meta = seme & 0xFFFFFFFF, []
    for i in range(1, 6):
        stato = eventi.avanza(stato)
        meta.append(stato >> 16)
        print("  s%d = 0x%08X   %s   metà alta 0x%04X"
              % (i, stato, b32(stato), stato >> 16))
    print("")
    print("  I bit bassi non si usano perché il bit di posizione k ha periodo 2^(k+1):")
    for k in (0, 1, 2):
        seq, st = [], seme & 0xFFFFFFFF
        for _ in range(8):
            st = eventi.avanza(st)
            seq.append((st >> k) & 1)
        print("    bit %d: %s   (periodo %d)" % (k, " ".join(str(v) for v in seq), 2 ** (k + 1)))

    a, b, terza, quarta, quinta = meta
    pid = ((a << 16) | b) & 0xFFFFFFFF

    print("")
    print("=== valore di personalità, con le due metà scambiate")
    print("  A, prima estrazione  = 0x%04X = %s" % (a, format(a, "016b")))
    print("  B, seconda estrazione = 0x%04X = %s" % (b, format(b, "016b")))
    print("  evento:    (A << 16) | B = 0x%08X   %s" % (pid, b32(pid)))
    ordinario = ((b << 16) | a) & 0xFFFFFFFF
    print("  ordinario: (B << 16) | A = 0x%08X   %s" % (ordinario, b32(ordinario)))
    print("  Le due composizioni differiscono su tutti i campi derivati: è la ragione per cui")
    print("  l'inversione è la firma di provenienza da evento e non un dettaglio di ordine.")

    print("")
    print("=== valori individuali, tre campi da cinque bit per estrazione")
    for etichetta, parola, campi in (
            ("terza estrazione", terza, ("PS", "Attacco", "Difesa")),
            ("quarta estrazione", quarta, ("Velocità", "Att. speciale", "Dif. speciale"))):
        print("  %s = 0x%04X" % (etichetta, parola))
        print("    bit   %s   (inutilizzato | 10-14 | 5-9 | 0-4)" % b16_campi(parola))
        for nome, valore in zip(campi, (parola & 31, (parola >> 5) & 31, (parola >> 10) & 31)):
            print("    %-14s %2d" % (nome, valore))
        print("    il bit 15 vale %d e non entra in alcun campo" % ((parola >> 15) & 1))

    print("")
    print("=== i campi che si calcolano dal valore di personalità e non si memorizzano")
    print("  natura   = PID mod 25 = %d" % (pid % 25))
    print("  abilità  = PID and 1  = %d" % (pid & 1))
    basso = pid & 0xFF
    print("  il byte basso del PID è 0x%02X = %d = %s"
          % (basso, basso, format(basso, "08b")))
    if soglia_sesso is not None:
        print("  sesso    = %s, perché %d %s %d, che è la soglia della specie"
              % ("femmina" if basso < soglia_sesso else "maschio", basso,
                 "<" if basso < soglia_sesso else ">=", soglia_sesso))
    else:
        print("  sesso    = dipende dalla soglia della specie, confrontata con quel byte")

    x = (tid ^ sid ^ (pid >> 16) ^ (pid & 0xFFFF)) & 0xFFFF
    print("")
    print("=== lucentezza, come somma esclusiva di quattro parole")
    for nome, valore in (("TID ", tid), ("SID ", sid),
                         ("PIDh", pid >> 16), ("PIDl", pid & 0xFFFF)):
        print("  %s = 0x%04X = %s" % (nome, valore & 0xFFFF, format(valore & 0xFFFF, "016b")))
    print("  xor  = 0x%04X = %s = %d" % (x, format(x, "016b"), x))
    print("  cromatico se il risultato è minore di 8: %s" % ("sì" if x < 8 else "no"))

    print("")
    print("=== sesso dell'allenatore, derivazione a scorrimento di sette")
    print("  quinta estrazione = 0x%04X = %s" % (quinta, format(quinta, "016b")))
    print("  bit di posizione 7 = %d, negato = %d, quindi %s"
          % ((quinta >> 7) & 1, ((quinta >> 7) & 1) ^ 1,
             eventi.sesso_allenatore_rand_s7(seme)))
    print("  Il numero cinque non è deducibile dalla struttura: le prime quattro estrazioni")
    print("  sono consumate dal valore di personalità e dai valori individuali, e la quinta")
    print("  è quella che decide questo campo.")
    return 0



# ---------------------------------------------------------------------------------------
# La tabella del verificatore, che elenca tutti gli eventi e non i soli conservati
# ---------------------------------------------------------------------------------------

WC3 = "PKHeX.Core/Legality/Encounters/Data/Gen3/EncountersWC3.cs"

# Le versioni che la tabella dichiara, verso il codice del campo di provenienza. La voce
# doppia RS non e' decidibile dalla tabella e si risolve sulla prima delle due, dichiarandolo.
VERSIONI = {"R": 2, "S": 1, "E": 3, "FR": 4, "LG": 5, "RS": 2}

# I nomi di lingua dell'enumerazione del verificatore verso i codici del byte a 0x12.
LINGUE_PKHEX = {"Japanese": 1, "English": 2, "French": 3, "Italian": 4, "German": 5,
                "Spanish": 7}

# Il costruttore della tabella ha tre forme, con tre, quattro o cinque argomenti: le due
# forme lunghe aggiungono un booleano e un luogo di incontro. Accettarle tutte e' necessario,
# perche' la forma a tre argomenti copre centoventidue voci su centosettantasette e le
# cinquantacinque restanti sono precisamente quelle degli insiemi giapponese e delle uova,
# cioe' meta' del materiale che il progetto non ha altrove.
VOCE_WC3 = re.compile(
    r"new\(\s*(\d+)\s*,\s*(\d+)\s*,\s*([A-Za-z]+)\s*((?:,[^){]*)?)\)\s*\{(.*?)\}"
    r"\s*,?\s*(?://\s*(.*))?$", re.M)

# La mossa che nella tabella del quinto anniversario distingue le due meta' delle otto voci.
# Il suo numero e' un dato e non una convenzione, e sta qui perche' senza di esso il metodo a
# tabella non sa quale delle due voci della specie stia producendo.
MOSSA_DESIDERIO = 273

# I nomi di allenatore che la tabella non scrive come stringa ma come costante dichiarata
# altrove nel medesimo file. Vanno risolti leggendo quella dichiarazione, e non indovinati: uno
# dei due vale la stringa vuota, che non e' una lacuna ma una istruzione, cioe' prendi il nome
# dal salvataggio che riceve, e l'altro e' un nome giapponese che con la tabella occidentale
# darebbe byte plausibili e sbagliati.
COSTANTE_OT = re.compile(r"OriginalTrainerName = ([A-Za-z_][A-Za-z0-9_]*)")
DICHIARAZIONE_COSTANTE = r'const string %s = "([^"]*)"'


def costanti_ot(testo):
    """Le costanti di nome allenatore dichiarate nel file della tabella, con il loro valore."""
    return dict(re.findall(r'const string ([A-Za-z_][A-Za-z0-9_]*) = "([^"]*)"', testo))


def voci_wc3(pkhex):
    """Le voci della tabella, come dizionari con i soli campi che essa dichiara.

    Si leggono i campi presenti e non si inventano i mancanti: un campo assente dalla voce
    significa che la tabella non lo vincola, ed e' informazione, non una lacuna da colmare.
    """
    p = os.path.join(pkhex, WC3.replace("/", os.sep))
    if not os.path.exists(p):
        sys.exit("manca " + WC3 + " sotto " + pkhex + ".\n"
                 "Si ottiene con un clone superficiale di PKHeX, come per il catalogo: il "
                 "clone non e una dipendenza di questo repository.")
    testo = io.open(p, encoding="utf-8", errors="ignore").read()
    fuori = []
    costanti = costanti_ot(testo)
    for m in VOCE_WC3.finditer(testo):
        specie, livello, versione, coda, corpo, commento = m.groups()
        voce = {
            "nazionale": int(specie),
            "livello": int(livello),
            "versione": versione,
            "commento": (commento or "").strip(),
            # Il quarto argomento posizionale del costruttore, quando c'e' e vale vero, dichiara
            # che la voce e' un uovo. Va letto perche' un uovo non e' un esemplare con un campo
            # in piu': ha soprannome, lingua e amicizia stabiliti dalla sua condizione.
            "uovo": bool(re.search(r"\btrue\b", coda or "")),
        }
        mosse = re.search(r"Moves = new\(([\d,\s]+)\)", corpo)
        if mosse:
            voce["mosse"] = [int(x) for x in re.findall(r"\d+", mosse.group(1))]
        for chiave, schema, conversione in (
                ("metodo", r"Method = ([A-Za-z0-9_]+)", str),
                ("ot", r'OriginalTrainerName = "([^"]*)"', str),
                ("sesso_ot", r"OriginalTrainerGender = ([A-Za-z0-9_]+)", str),
                ("identificativo", r"ID32 = (\d+)", int),
                ("lucentezza", r"Shiny = ([A-Za-z]+)", str),
                ("lingua", r"Language = \(int\)([A-Za-z]+)", str),
                ("fatidico", r"FatefulEncounter = (true|false)", lambda v: v == "true"),
        ):
            trovato = re.search(schema, corpo)
            if trovato:
                voce[chiave] = conversione(trovato.group(1))
        if "ot" not in voce:
            # Il nome puo' essere scritto come costante invece che come stringa. Se lo e' e non
            # si risolve, la voce porta la ragione invece di un nome vuoto: un nome vuoto e' una
            # istruzione legittima in questa tabella, quindi confonderlo con un dato mancante
            # produrrebbe un esemplare con l'allenatore sbagliato e nessun segnale.
            simbolo = COSTANTE_OT.search(corpo)
            if simbolo:
                nome = simbolo.group(1)
                if nome in costanti:
                    voce["ot"] = costanti[nome]
                    voce["ot_da_costante"] = nome
                else:
                    voce["ot_irrisolto"] = nome
        voce["desiderio"] = MOSSA_DESIDERIO in voce.get("mosse", [])
        fuori.append(voce)
    return fuori


SORGENTE_MYSTRY = "PKHeX.Core/Legality/RNG/ClassicEra/Gen3/MystryMew.cs"

# Il numero di semi che l'elenco deve contenere, e perche' il conteggio e' un presidio e non
# una curiosita': l'elenco e' l'unico dato di questo strumento che non discende da una formula,
# quindi una lettura che ne perdesse una parte non produrrebbe un errore ma un insieme piu'
# povero, dal quale si continuerebbe a generare esemplari validi. Il conteggio atteso e' il
# solo modo di accorgersene.
SEMI_MYSTRY_ATTESI = 86


def semi_mystry_mew(pkhex):
    """I semi ammessi dell'unico evento che non si genera da una formula ma da un elenco.

    L'elenco non e' derivabile: sono i semi che l'organizzatore dell'evento ha effettivamente
    distribuito, quindi e' un fatto storico e non un calcolo. Si legge dalla fonte invece di
    trascriverlo, per la stessa ragione per cui nessuna tabella di questo progetto e' scritta a
    mano, e si esclude il seme che la fonte dichiara distribuito solo in una delle sue cinque
    varianti, perche' produrre quella sbagliata darebbe un esemplare mai esistito.
    """
    percorso = os.path.join(pkhex, SORGENTE_MYSTRY.replace("/", os.sep))
    if not os.path.exists(percorso):
        sys.exit("manca " + SORGENTE_MYSTRY + " sotto " + pkhex + ".")
    testo = io.open(percorso, encoding="utf-8", errors="ignore").read()
    inizio = testo.find("Seeds =>")
    if inizio < 0:
        sys.exit("non trovo l'elenco dei semi in " + SORGENTE_MYSTRY)
    corpo = testo[testo.index("[", inizio):testo.index("];", inizio)]
    semi = [int(x, 16) for x in re.findall(r"0x([0-9A-Fa-f]{4})", corpo)]
    if len(semi) != SEMI_MYSTRY_ATTESI:
        sys.exit("l'elenco dei semi ha %d voci invece di %d: la lettura ha perso qualcosa, e "
                 "un elenco piu povero non produce errori ma esemplari tratti da un "
                 "sottoinsieme, che e il modo peggiore di sbagliare"
                 % (len(semi), SEMI_MYSTRY_ATTESI))
    rilasciato = re.search(r"ReleasedSeed = 0x([0-9A-Fa-f]+)", testo)
    if rilasciato:
        # Questo seme fu distribuito in una sola delle sue cinque varianti, e questo strumento
        # produce la prima: escluderlo costa un seme su ottantasei e rimuove la possibilita' di
        # comporre un esemplare che nessuno ha mai ricevuto.
        semi = [x for x in semi if x != int(rilasciato.group(1), 16)]
    return semi


SPECIE_LOCALIZZATE = "src/data/localizedSpeciesNames.gen3.js"

# Le tabelle dei nomi di specie per lingua, con il nome che la fonte usa per ciascuna. Le
# lingue assenti non sono una lacuna: la fonte dichiara che lo spagnolo e l'italiano, nella
# terza generazione, impiegano i nomi inglesi, quindi per esse la tabella inglese e' la tabella
# giusta e non un ripiego.
TABELLE_NOMI_SPECIE = {
    "Japanese": "JAPANESE_SPECIES_NAMES",
    "English": "ENGLISH_SPECIES_NAMES",
    "French": "FRENCH_SPECIES_NAMES",
    "German": "GERMAN_SPECIES_NAMES",
    "Spanish": "ENGLISH_SPECIES_NAMES",
    "Italian": "ENGLISH_SPECIES_NAMES",
}


def nomi_specie_per_lingua(ace, lingua):
    """I nomi delle specie nella lingua richiesta, indicizzati per identificativo interno.

    Esiste perche' il soprannome di un esemplare senza soprannome non e' una stringa vuota ma
    il nome della sua specie nella lingua dell'esemplare, e la differenza non e' cosmetica: un
    esemplare giapponese con il nome inglese della specie porta un soprannome che il gioco
    giapponese non avrebbe mai scritto, e un verificatore lo nota. Fino al 2026-09-01 questo
    programma scriveva il nome inglese su tutte le voci, comprese le giapponesi.
    """
    nome_tabella = TABELLE_NOMI_SPECIE.get(lingua)
    if nome_tabella is None:
        sys.exit("nessuna tabella di nomi di specie per la lingua " + repr(lingua) + ": le "
                 "lingue note sono " + ", ".join(sorted(TABELLE_NOMI_SPECIE)))
    testo = leggi(ace, SPECIE_LOCALIZZATE)
    apertura = testo.find("const " + nome_tabella)
    if apertura < 0:
        sys.exit("non trovo la tabella " + nome_tabella + " in " + SPECIE_LOCALIZZATE)
    inizio = testo.index("[", apertura)
    corpo = testo[inizio + 1:testo.index("]", inizio)]
    voci = []
    for pezzo in corpo.split(","):
        pezzo = pezzo.strip()
        if not pezzo:
            continue
        if pezzo == "null":
            voci.append(None)
        elif pezzo.startswith('"') and pezzo.endswith('"'):
            voci.append(pezzo[1:-1])
        else:
            sys.exit("voce non riconosciuta in " + nome_tabella + ": " + repr(pezzo))
    # Il controllo che rende la lettura verificata: la tabella e' indicizzata per
    # identificativo interno e comincia con una posizione nulla, quindi la sua lunghezza deve
    # coprire almeno le specie della terza generazione. Una lettura troncata darebbe nomi
    # assenti per le specie alte, che poi diventerebbero soprannomi vuoti.
    if len(voci) < 412:
        sys.exit("la tabella " + nome_tabella + " ha %d voci, troppo poche per coprire gli "
                 "identificativi interni della terza generazione: la lettura si e fermata "
                 "presto e i nomi delle specie alte mancherebbero in silenzio" % (len(voci),))
    return {i: n for i, n in enumerate(voci) if n}


def nazionale_verso_interno(ace):
    """La corrispondenza fra numero nazionale e identificativo interno di terza generazione.

    Serve perche' le due fonti numerano le specie in modo diverso, e la differenza non e'
    visibile su Charizard ma lo e' su Latias, che e' 380 per la tabella e 407 per il
    costruttore. Confondere le due numerazioni scambia una specie con un'altra, che e' il
    difetto piu' grave possibile su questo dato.
    """
    per_nome, per_id = specie_per_nome(ace)
    testo = leggi(ace, "src/data/nationalDex.gen3.js")
    fuori = {}
    for numero, nome in re.findall(r"\[\s*(\d+)\s*,\s*\"([^\"]+)\"\s*\]", testo):
        chiave = re.sub(r"[^a-z0-9]", "", nome.lower())
        for candidato, ident in per_nome.items():
            if re.sub(r"[^a-z0-9]", "", candidato) == chiave:
                fuori[int(numero)] = ident
                break
    return fuori


def elenca_wc3(pkhex):
    voci = voci_wc3(pkhex)
    print("")
    print("=== Tabella del verificatore: " + str(len(voci)) + " voci")
    per_evento = {}
    for i, v in enumerate(voci):
        chiave = (v.get("ot", "?"), v.get("identificativo", 0))
        per_evento.setdefault(chiave, []).append((i, v))
    print("    " + str(len(per_evento)) + " combinazioni di allenatore e identificativo")
    for (ot, ident), gruppo in sorted(per_evento.items(), key=lambda x: x[0][1]):
        specie = ", ".join(str(v.get("commento") or v["nazionale"]) for _i, v in gruppo[:8])
        print("")
        print("  " + ot + "  identificativo " + str(ident) + "  (" + str(len(gruppo)) +
              " voci, indici " + str(gruppo[0][0]) + "-" + str(gruppo[-1][0]) + ")")
        primo = gruppo[0][1]
        print("    livello " + str(primo["livello"]) + ", versione " + primo["versione"] +
              ", metodo " + str(primo.get("metodo")) + ", lucentezza " +
              str(primo.get("lucentezza")) + ", sesso OT " + str(primo.get("sesso_ot")) +
              ", fatidico " + str(primo.get("fatidico", False)))
        print("    " + specie)
    return 0


def componi_da_wc3(ace, pkhex, indice, seme):
    """Compone un esemplare da una voce della tabella del verificatore.

    La differenza rispetto al percorso che parte dal corpus e' la fonte dei metadati, e con
    essa il grado di fiducia: qui vengono dalla tabella che il verificatore stesso impiega per
    giudicare, quindi ogni campo che essa dichiara e' per costruzione quello atteso. I campi
    che la tabella non dichiara restano quelli che il giudizio del 2026-09-01 ha confermato
    corretti, cioe' la sfera ordinaria e il luogo di incontro speciale, e il rapporto continua
    a dichiararne la provenienza invece di presentarli come letti.
    """
    voci = voci_wc3(pkhex)
    if not 0 <= indice < len(voci):
        sys.exit("indice fuori intervallo: la tabella ha %d voci leggibili, da 0 a %d"
                 % (len(voci), len(voci) - 1))
    v = voci[indice]

    mappa = nazionale_verso_interno(ace)
    specie_id = mappa.get(v["nazionale"])
    if specie_id is None:
        sys.exit("nessun identificativo interno per il numero nazionale %d: la corrispondenza "
                 "fra le due numerazioni non copre quella specie, e indovinarla scambierebbe "
                 "una specie con un'altra" % v["nazionale"])
    _per_nome, per_id = specie_per_nome(ace)

    gruppo = gruppo_di_crescita(ace).get(specie_id)
    if gruppo is None:
        sys.exit("gruppo di crescita non noto per la specie interna %d" % specie_id)

    codice_lingua = LINGUE_PKHEX.get(v.get("lingua", "English"), 2)
    gioco_id = VERSIONI.get(v["versione"], 2)
    livello = v["livello"]
    ident = int(v.get("identificativo", 0))

    personalita, iv = eventi.personalita_e_iv(seme)
    sesso_ot = eventi.sesso_allenatore_rand_s7(seme)
    derivazione = v.get("sesso_ot", "")

    tabella = cm.Charmap.gen3()
    nome_visibile = per_id.get(specie_id, "").upper()
    try:
        soprannome = tabella.encode(nome_visibile, length=gen3.NICKNAME_LENGTH)
    except ValueError as e:
        sys.exit("il nome della specie non si codifica: " + str(e))
    try:
        ot_bytes = tabella.encode(v.get("ot", ""), length=gen3.OT_NAME_LENGTH)
    except ValueError as e:
        sys.exit("il nome dell'allenatore non si codifica: " + str(e) + "\n"
                 "Le voci giapponesi della tabella portano nomi che la tabella dei caratteri "
                 "occidentale non contiene: per esse serve la codifica giapponese, che questo "
                 "progetto non ha ancora estratto.")

    mosse = [m for m in v.get("mosse", []) if m]
    pp_base = punti_potenza(ace)
    pp = [pp_base.get(m, 0) for m in mosse]

    mon = gen3.Gen3Mon(
        personality=personalita,
        ot_id=ident & 0xFFFFFFFF,
        nickname=soprannome,
        language=codice_lingua,
        flags=0x02,
        ot_name=ot_bytes,
        markings=0,
        growth=gen3.Growth(species=specie_id, held_item=0,
                           experience=esperienza(gruppo, livello),
                           pp_bonuses=0, friendship=70),
        attacks=gen3.Attacks(moves=(mosse + [0, 0, 0, 0])[:4], pp=(pp + [0, 0, 0, 0])[:4]),
        evs=gen3.EvsCondition(),
        misc=gen3.Misc(
            pokerus=0,
            met_location=255,
            met_level=livello,
            met_game=gioco_id,
            pokeball=4,
            ot_female=(sesso_ot == "femmina"),
            ivs={n: iv[k] for n, k in zip(gen3.EV_ORDER, eventi.ORDINE_IV)},
            is_egg=False,
            ability_num=personalita & 0x01,
            modern_fateful_encounter=bool(v.get("fatidico", False)),
        ),
    )

    rapporto = [
        ("voce della tabella", "indice " + str(indice) + ", " +
         (v.get("commento") or ("numero nazionale " + str(v["nazionale"]))),
         "tabella del verificatore, che e la fonte con cui esso stesso giudica"),
        ("valore di personalita", "0x%08X" % personalita,
         "derivato dal seme, formula verificata su 208 vettori su 209 e confermata dalla "
         "ricostruzione inversa del verificatore"),
        ("valori individuali", ", ".join("%s=%d" % (k, iv[k]) for k in eventi.ORDINE_IV),
         "derivati dal seme, formula verificata su 209 vettori su 209"),
        ("sesso dell'allenatore", sesso_ot,
         ("derivato dal seme con la derivazione a scorrimento di sette, che la tabella "
          "dichiara per questa voce") if derivazione == "RandS7" else
         ("ATTENZIONE: la tabella dichiara per questa voce la derivazione " +
          (derivazione or "nessuna") + ", che questo progetto non implementa. Il valore "
          "scritto viene dalla derivazione a scorrimento di sette e sara contestato")),
        ("allenatore e identificativo", v.get("ot", "?") + ", " + str(ident),
         "tabella del verificatore"),
        ("lingua", v.get("lingua", "?") + " (" + str(codice_lingua) + ")",
         "tabella del verificatore, con la numerazione nota del byte a 0x12"),
        ("specie", per_id.get(specie_id, "?") + " (interna " + str(specie_id) +
         ", nazionale " + str(v["nazionale"]) + ")",
         "numero nazionale dalla tabella, convertito nell'identificativo interno: la "
         "conversione e necessaria perche le due fonti numerano le specie in modo diverso"),
        ("livello", str(livello), "tabella del verificatore"),
        ("gioco di origine", gen3.ORIGIN_GAMES.get(gioco_id, "?") + " (" + str(gioco_id) + ")",
         "tabella del verificatore, che per questo campo e vincolante: la versione dichiarata "
         "la e " + v["versione"]),
        ("mosse", ", ".join(str(m) for m in mon.attacks.moves),
         "tabella del verificatore"),
        ("punti potenza", ", ".join(str(p) for p in mon.attacks.pp),
         "valori di base delle mosse dal costruttore, senza alcun PP Up"),
        ("incontro fatidico", str(mon.misc.modern_fateful_encounter),
         "tabella del verificatore, che lo dichiara solo dove serve: e la fonte che ha "
         "sostituito la correzione empirica registrata il 2026-09-01"),
        ("metodo dichiarato", str(v.get("metodo")),
         "tabella del verificatore. Il progetto implementa la famiglia BACD con seme a sedici "
         "bit; su un metodo diverso il seme scelto non produce un esemplare conforme"),
        ("lucentezza attesa", str(v.get("lucentezza", "non dichiarata")),
         "tabella del verificatore; il seme va scelto in coerenza con essa"),
        ("sfera e luogo di incontro", "4 e 255",
         "non dichiarati dalla tabella: sono i valori che il giudizio del 2026-09-01 ha "
         "confermato corretti per il tipo di incontro"),
        ("EV, statistiche da gara, lucentezza estetica, nastri, Pokerus", "tutti a zero",
         "scelta deliberata: un esemplare appena distribuito non ne ha"),
    ]
    return mon, rapporto


# I metodi di generazione che questo programma sa produrre. Fino al 2026-09-01 erano quattro,
# ed erano quelli in cui il valore di personalita' discende direttamente dalle prime due
# estrazioni di un seme a sedici bit. Dopo il confronto riga per riga con il codice della
# implementazione di riferimento sono tutti tranne uno, perche' cio' che li distingueva non era
# un algoritmo diverso ma una trasformazione del seme e un ramo di composizione, e l'una e
# l'altro sono ora implementati e provati.
#
# Resta fuori il solo metodo del canale televisivo, che impiega un generatore
# pseudocasuale differente, cioe' quello dei titoli del cubo, e la sola derivazione del sesso
# che la fonte stessa dichiara di non verificare con la logica ordinaria. Non si tenta, e la
# ragione per cui non si tenta e' la medesima di sempre: un esemplare prodotto con il metodo
# sbagliato e' indistinguibile a occhio da uno giusto.
METODI_PRODUCIBILI = ("BACD_R", "BACD_R_A", "BACD_A", "BACD", "BACD_RBCD", "BACD_TA",
                      "BACD_TS", "BACD_U_AX", "BACD_M", "Method_2")

# Il metodo che resta fuori, nominato invece di essere semplicemente assente, cosicche' il
# rapporto possa dirne la ragione al posto di un silenzio.
METODO_NON_IMPLEMENTATO = "Channel"


def allenatore_da_argomento(testo):
    """L'allenatore di destinazione, letto dalla forma `nome:identificativo:segreto:sesso`.

    Serve a due gruppi di voci che senza di esso non si possono produrre, e vale distinguerli
    perche' la ragione e' diversa. Alcune voci dichiarano il sesso dell'allenatore uguale a
    quello di chi riceve, quindi non e' un dato dell'evento. Altre dichiarano il nome vuoto, che
    non e' una lacuna della tabella ma una istruzione: quell'evento prende il nome dal
    salvataggio in cui viene riscattato. In entrambi i casi il dato manca all'evento e appartiene
    alla destinazione, e chiederlo e' l'unica via corretta: metterci un valore inventato
    produrrebbe una collezione che porta per sempre il nome di uno sconosciuto.
    """
    if not testo:
        return None
    pezzi = testo.split(":")
    if len(pezzi) != 4:
        sys.exit("l'allenatore si scrive come nome:identificativo:segreto:sesso, per esempio "
                 "MARIO:31121:5432:maschio")
    nome, ident, segreto, sesso = pezzi
    if sesso not in ("maschio", "femmina"):
        sys.exit("il sesso dell'allenatore vale maschio o femmina, non " + repr(sesso))
    return {"nome": nome, "identificativo": int(ident, 0), "segreto": int(segreto, 0),
            "sesso": sesso}


def lotto(ace, pkhex, cartella, solo_ot=None, primo_seme=1, allenatore=None):
    """Produce un esemplare per ogni voce producibile, e riferisce sulle altre.

    Il seme si cerca invece di chiederlo, e i vincoli verificati sono quelli che la tabella
    dichiara, cioe' la lucentezza e, dove la derivazione e' implementata, il sesso
    dell'allenatore. Il seme di partenza della ricerca e' un parametro perche' due voci del
    medesimo evento con i medesimi vincoli otterrebbero altrimenti il medesimo seme, e due
    esemplari distinti dello stesso evento con il medesimo valore di personalita' sarebbero
    un duplicato riconoscibile.
    """
    voci = voci_wc3(pkhex)
    mappa = nazionale_verso_interno(ace)
    _per_nome, per_id = specie_per_nome(ace)
    gruppi = gruppo_di_crescita(ace)
    pp_base = punti_potenza(ace)
    semi_mystry = semi_mystry_mew(pkhex)
    # Le tabelle dei nomi di specie si leggono una volta per lingua e non una volta per voce,
    # perche' ciascuna e' una lettura di file.
    nomi_localizzati = {}
    os.makedirs(cartella, exist_ok=True)

    fatti, saltate = 0, []
    seme_corrente = primo_seme
    for indice, v in enumerate(voci):
        nome_ot = v.get("ot", "")
        etichetta = ((nome_ot or "(dal ricevente)") + " " +
                     str(v.get("identificativo", 0)) + " " +
                     (v.get("commento") or str(v["nazionale"])))
        if solo_ot and nome_ot != solo_ot:
            continue

        metodo = v.get("metodo", "")
        if metodo not in METODI_PRODUCIBILI:
            saltate.append((indice, etichetta, "metodo " + str(metodo) +
                            ": impiega un generatore pseudocasuale diverso da quello della "
                            "terza generazione su cartuccia"))
            continue
        if "ot_irrisolto" in v:
            saltate.append((indice, etichetta, "il nome dell'allenatore e scritto come "
                            "costante " + v["ot_irrisolto"] + ", che non si risolve nel file "
                            "della tabella: si rifiuta invece di scrivere un nome vuoto"))
            continue
        if v.get("uovo"):
            # Un uovo non e' un esemplare con un contrassegno in piu': il soprannome e la
            # lingua sono imposti dalla sua condizione, e l'amicizia porta il conto delle
            # incubazioni, che e' un dato per specie che questo progetto non ha ancora estratto.
            # Si rifiuta, e la ragione nomina il dato che manca.
            saltate.append((indice, etichetta, "e un uovo: il generatore pseudocasuale e "
                            "pronto, ma manca il conto delle incubazioni per specie, che "
                            "nell'uovo occupa il campo dell'amicizia e che un verificatore "
                            "controlla"))
            continue
        derivazione = v.get("sesso_ot")
        if derivazione and derivazione not in eventi.DERIVAZIONI_SESSO:
            saltate.append((indice, etichetta, "derivazione del sesso " + derivazione +
                            ": non implementata, e la fonte stessa non la verifica con la "
                            "logica ordinaria"))
            continue
        if (derivazione == "Recipient" or not nome_ot) and not allenatore:
            saltate.append((indice, etichetta, "dipende dall'allenatore che riceve, che non e "
                            "un dato dell'evento: si passa con --allenatore"))
            continue
        specie_id = mappa.get(v["nazionale"])
        if specie_id is None:
            saltate.append((indice, etichetta, "nessun identificativo interno per il numero "
                            "nazionale " + str(v["nazionale"])))
            continue
        gruppo = gruppi.get(specie_id)
        if gruppo is None:
            saltate.append((indice, etichetta, "gruppo di crescita non noto"))
            continue

        # La tabella dei caratteri si scegli per lingua e non una volta per tutte: nella terza
        # generazione il medesimo byte rende un glifo diverso secondo la lingua del gioco,
        # quindi un nome giapponese scritto con la tabella internazionale non produce un errore
        # ma un nome plausibile e sbagliato.
        lingua_voce = v.get("lingua", "English")
        tabella = cm.Charmap.gen3_per_lingua(lingua_voce)
        nome_effettivo = nome_ot or (allenatore["nome"] if allenatore else "")
        nome_specie = nomi_localizzati.setdefault(
            lingua_voce, nomi_specie_per_lingua(ace, lingua_voce)).get(specie_id)
        if not nome_specie:
            saltate.append((indice, etichetta, "nessun nome di specie in " + lingua_voce +
                            " per l'identificativo interno " + str(specie_id)))
            continue
        try:
            ot_bytes = tabella.encode(nome_effettivo, length=gen3.OT_NAME_LENGTH)
            soprannome = tabella.encode(nome_specie, length=gen3.NICKNAME_LENGTH)
        except ValueError as e:
            saltate.append((indice, etichetta, "codifica dei caratteri: " + str(e)))
            continue

        if v.get("identificativo") is not None:
            ident = int(v["identificativo"])
        elif allenatore:
            ident = (allenatore["identificativo"] & 0xFFFF) | \
                    ((allenatore["segreto"] & 0xFFFF) << 16)
        else:
            saltate.append((indice, etichetta, "la tabella non fissa l'identificativo, quindi "
                            "viene dal salvataggio che riceve: si passa con --allenatore"))
            continue

        semi = list(range(seme_corrente, 0x10000)) + list(range(0, seme_corrente))
        if metodo in ("BACD_RBCD", "BACD_M"):
            # Questi due metodi schiacciano il seme su un insieme molto piu' piccolo, quindi
            # percorrere i sessantacinquemila ripeterebbe lo stesso esemplare migliaia di volte
            # dando l'impressione di una ricerca che non c'e'. La rotazione va conservata anche
            # qui, e vale dirlo perche' dimenticarla non produce un errore: due voci del
            # medesimo evento ripartirebbero dallo stesso punto e riceverebbero il medesimo
            # valore di personalita', cioe' un duplicato riconoscibile a occhio.
            ammessi = list(eventi.semi_ammessi(metodo, semi_mystry))
            taglio = seme_corrente % max(1, len(ammessi))
            semi = ammessi[taglio:] + ammessi[:taglio]
        try:
            esito = eventi.esemplare_da_evento(
                metodo, ident & 0xFFFF, (ident >> 16) & 0xFFFF, v.get("lucentezza"),
                specie=v["nazionale"], desiderio=v.get("desiderio"), derivazione=derivazione,
                sesso_ricevente=(allenatore["sesso"] if allenatore else None),
                semi_mystry=semi_mystry, semi=semi)
        except gb_errore() as e:
            saltate.append((indice, etichetta, "il generatore si rifiuta: " + str(e)))
            continue
        if esito is None:
            saltate.append((indice, etichetta, "nessun seme soddisfa i vincoli dichiarati"))
            continue
        seme_corrente = (esito["seme"] + 1) & 0xFFFF or 1

        personalita, iv, sesso_ot = esito["personalita"], esito["iv"], esito["sesso_ot"]
        # L'evento del desiderio consuma una estrazione per l'oggetto tenuto, e quella
        # estrazione porta un'informazione che va scritta: un esemplare di quell'evento senza
        # la sua bacca non e' sbagliato in un campo vincolato, ma non e' l'esemplare che
        # l'originale era. Gli altri eventi non consumano quella estrazione e restano a zero.
        oggetto = 0
        if esito["estrazione_oggetto"] is not None:
            oggetto = eventi.oggetto_tenuto_desiderio(esito["estrazione_oggetto"])
        mosse = [m for m in v.get("mosse", []) if m]
        pp = [pp_base.get(m, 0) for m in mosse]
        livello = v["livello"]

        mon = gen3.Gen3Mon(
            personality=personalita,
            ot_id=ident & 0xFFFFFFFF,
            nickname=soprannome,
            language=LINGUE_PKHEX.get(lingua_voce, 2),
            flags=0x02,
            ot_name=ot_bytes,
            growth=gen3.Growth(species=specie_id, held_item=oggetto,
                               experience=esperienza(gruppo, livello), friendship=70),
            attacks=gen3.Attacks(moves=(mosse + [0, 0, 0, 0])[:4],
                                 pp=(pp + [0, 0, 0, 0])[:4]),
            evs=gen3.EvsCondition(),
            misc=gen3.Misc(met_location=255, met_level=livello,
                           met_game=VERSIONI.get(v["versione"], 2), pokeball=4,
                           ot_female=(sesso_ot == "femmina"),
                           ivs={n: iv[k] for n, k in zip(gen3.EV_ORDER, eventi.ORDINE_IV)},
                           ability_num=personalita & 0x01,
                           modern_fateful_encounter=bool(v.get("fatidico", False))),
        )
        # Il nome del file porta la descrizione dell'evento e non il nome dell'allenatore, e la
        # ragione e' pratica: i nomi giapponesi non sopravvivono alla riduzione ai caratteri
        # latini, quindi cinquanta file su centoventidue si chiamerebbero allo stesso modo a
        # meno dell'indice. La descrizione e' in latino nella tabella e distingue le voci.
        descrizione = re.sub(r"[^A-Za-z0-9]", "",
                             v.get("commento") or nome_effettivo or "ricevente")
        nome = "%03d-%s-%s" % (indice, descrizione or "evento",
                               re.sub(r"[^A-Za-z0-9]", "", per_id.get(specie_id, "x")))
        scrivi(mon, os.path.join(cartella, nome))
        fatti += 1
        print("  %-40s %-9s seme 0x%04X  PID 0x%08X%s%s"
              % (etichetta[:40], metodo, esito["seme"], personalita,
                 "  cromatico" if esito["cromatico"] else "",
                 "  oggetto %d" % oggetto if oggetto else ""))

    print("")
    print("prodotti " + str(fatti) + ", non producibili " + str(len(saltate)))
    if saltate:
        print("")
        print("=== Voci non prodotte, con la ragione")
        for indice, etichetta, ragione in saltate:
            print("  [%3d] %-40s %s" % (indice, etichetta[:40], ragione))
    print("")
    print("I file stanno in " + cartella + ", che non entra in git. Il passo seguente non e")
    print("di questo programma: si aprono con il verificatore di conformita, nel contesto della")
    print("terza generazione, e si legge che cosa esso obietti.")
    return 0


def gb_errore():
    """L'eccezione che il pacchetto solleva, presa senza importare il modulo per nome."""
    from pokebridge import gb
    return gb.FormatError


def scrivi(mon, base):
    cartella = os.path.dirname(base)
    if cartella:
        os.makedirs(cartella, exist_ok=True)
    pk3 = base + ".pk3"
    ek3 = base + ".ek3"
    io.open(pk3, "wb").write(mon.to_canonical_bytes(party=False))
    io.open(ek3, "wb").write(mon.to_bytes(party=False))
    return pk3, ek3


def self_test():
    """Prove che non richiedono il sorgente del costruttore.

    Verificano la parte di questo programma che è propria e non la parte che dipende dai
    dati di terzi: le formule dell'esperienza contro valori noti, e il fatto che i due file
    prodotti siano convertibili l'uno nell'altro.
    """
    fallite = 0

    def controlla(nome, condizione):
        nonlocal fallite
        print(("  ok      " if condizione else "  FALLITO ") + nome)
        if not condizione:
            fallite += 1

    controlla("esperienza medium fast al livello 100 vale un milione",
              esperienza(MEDIUM_FAST, 100) == 1000000)
    controlla("esperienza fast al livello 100 vale ottocentomila",
              esperienza(FAST, 100) == 800000)
    controlla("esperienza slow al livello 100 vale un milione duecentocinquantamila",
              esperienza(SLOW, 100) == 1250000)
    controlla("esperienza medium slow al livello 100 vale 1059860",
              esperienza(MEDIUM_SLOW, 100) == 1059860)
    controlla("esperienza al livello 1 è nulla in ogni gruppo",
              all(esperienza(g, 1) == 0 for g in range(6)))
    controlla("l'esperienza cresce con il livello in ogni gruppo",
              all(esperienza(g, 70) > esperienza(g, 69) for g in range(6)))

    tabella = cm.Charmap.gen3()
    controlla("il nome dell'allenatore del decennale si codifica",
              len(tabella.encode("10ANNI", length=gen3.OT_NAME_LENGTH)) ==
              gen3.OT_NAME_LENGTH)

    personalita, iv = eventi.personalita_e_iv(0x9DF6)
    controlla("il vettore del decennale si riproduce", personalita == 0xD2A8AA71)

    mon = gen3.Gen3Mon(
        personality=personalita, ot_id=6227,
        nickname=tabella.encode("PIKACHU", length=gen3.NICKNAME_LENGTH),
        language=4, flags=0x02,
        ot_name=tabella.encode("10ANNI", length=gen3.OT_NAME_LENGTH),
        growth=gen3.Growth(species=25, experience=esperienza(MEDIUM_FAST, 70)),
        misc=gen3.Misc(met_level=70, ivs={n: iv[k] for n, k
                                          in zip(gen3.EV_ORDER, eventi.ORDINE_IV)}),
    )
    canonica = mon.to_canonical_bytes(party=False)
    riletto = gen3.Gen3Mon.from_canonical_bytes(canonica, party=False)
    controlla("le due forme si convertono a vicenda",
              riletto.to_bytes(party=False) == mon.to_bytes(party=False))
    controlla("la forma di scambio è lunga ottanta byte", len(canonica) == 80)
    controlla("il soprannome si rilegge",
              tabella.decode(riletto.nickname) == "PIKACHU")
    controlla("il nome dell'allenatore si rilegge",
              tabella.decode(riletto.ot_name) == "10ANNI")

    print("")
    print("self-test: %d controlli falliti su %d" % (fallite, 12))
    return 1 if fallite else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ace", help="cartella con il sorgente del costruttore")
    ap.add_argument("--elenco", action="store_true", help="elenca gli eventi disponibili")
    ap.add_argument("--pkhex", help="clone di PKHeX, per leggere la tabella dei "
                                    "centosettantasette eventi invece del corpus dei diciassette")
    ap.add_argument("--indice", type=int, help="indice della voce nella tabella del verificatore")
    ap.add_argument("--lotto", metavar="CARTELLA",
                    help="produce tutti gli esemplari producibili nella cartella indicata")
    ap.add_argument("--solo-ot", dest="solo_ot",
                    help="limita il lotto alle voci con questo nome di allenatore")
    ap.add_argument("--allenatore", metavar="NOME:ID:SEGRETO:SESSO",
                    help="l'allenatore di destinazione, per le voci che lo prendono da chi "
                         "riceve invece di fissarlo")
    ap.add_argument("--evento", help="sigla dell'evento, per esempio 10ANNI")
    ap.add_argument("--specie", help="nome della specie")
    ap.add_argument("--seme", help="seme di origine, in esadecimale o decimale")
    ap.add_argument("--lingua", default="ITA", help="ITA, ENG, JPN, FRA, GER, SPA")
    ap.add_argument("--gioco", help="gioco di origine, per nome o per numero: rubino, "
                                    "zaffiro, smeraldo, rossofuoco, verdefoglia")
    ap.add_argument("--out", help="prefisso dei due file da scrivere, senza estensione")
    ap.add_argument("--derivazione", action="store_true",
                    help="stampa la catena dal seme ai campi derivati, in binario, ed esce")
    ap.add_argument("--soglia-sesso", type=int, dest="soglia_sesso",
                    help="soglia di sesso della specie, per far calcolare anche quel campo")
    ap.add_argument("--self-test", action="store_true", dest="self_test",
                    help="prove che non richiedono il sorgente del costruttore")
    a = ap.parse_args()

    if a.self_test:
        return self_test()
    if a.elenco and a.pkhex:
        return elenca_wc3(a.pkhex)
    if a.derivazione:
        if not a.seme:
            ap.error("--derivazione richiede --seme")
        seme = int(a.seme, 16) if a.seme.lower().startswith("0x") else int(a.seme)
        tid, sid = 6227, 0
        if a.ace and a.evento:
            ev = corpus(a.ace).get("events", {}).get(a.evento)
            if ev:
                tid = int(ev.get("fixedTID") or 0)
                sid = int(ev.get("fixedSID") or 0)
        return derivazione(seme, tid, sid, a.soglia_sesso)
    if not a.ace:
        ap.error("serve --ace con la cartella del sorgente del costruttore")
    if a.elenco:
        return elenca(a.ace)
    if a.lotto:
        if not (a.ace and a.pkhex):
            ap.error("--lotto richiede --ace e --pkhex")
        return lotto(a.ace, a.pkhex, a.lotto, a.solo_ot,
                     allenatore=allenatore_da_argomento(a.allenatore))
    if a.indice is not None:
        if not (a.pkhex and a.seme):
            ap.error("--indice richiede --pkhex e --seme")
        seme = int(a.seme, 16) if a.seme.lower().startswith("0x") else int(a.seme)
        mon, rapporto = componi_da_wc3(a.ace, a.pkhex, a.indice, seme)
    else:
        if not (a.evento and a.specie and a.seme):
            ap.error("servono --evento, --specie e --seme; oppure --indice con --pkhex; "
                     "oppure --elenco")
        seme = int(a.seme, 16) if a.seme.lower().startswith("0x") else int(a.seme)
        mon, rapporto = componi(a.ace, a.evento, a.specie, seme, a.lingua, a.gioco)

    print("")
    print("=== Esemplare composto, campo per campo con la provenienza")
    for nome, valore, provenienza in rapporto:
        print("")
        print("  " + nome + ": " + valore)
        print("    " + provenienza)

    print("")
    print("=== Verifiche interne")
    canonica = mon.to_canonical_bytes(party=False)
    riletto = gen3.Gen3Mon.from_canonical_bytes(canonica, party=False)
    print("  le due forme si convertono a vicenda: " +
          str(riletto.to_bytes(party=False) == mon.to_bytes(party=False)))
    print("  checksum calcolato: 0x%04X" % mon.checksum_computed)
    print("  ordine delle sottostrutture nel salvataggio: " + mon.substruct_order)

    if a.out:
        pk3, ek3 = scrivi(mon, a.out)
        print("")
        print("scritti " + pk3 + " e " + ek3)
        print("Il passo seguente non è di questo programma: si apre il file .pk3 con lo "
              "strumento di conformità")
        print("della comunità e si legge che cosa esso obietta. Ogni obiezione va confrontata "
              "con la colonna")
        print("della provenienza qui sopra, perché è quella che dice se il difetto sia nostro "
              "o dei dati di terzi.")
    else:
        print("")
        print("nessun file scritto: si passa --out con il prefisso dei due file")
    return 0


if __name__ == "__main__":
    sys.exit(main())
