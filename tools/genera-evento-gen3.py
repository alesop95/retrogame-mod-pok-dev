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


def componi(ace, tag, nome_specie, seme, lingua, verbose=False):
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
            met_game=int(ev.get("defaultOriginGame") or 2),
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
        ("gioco di origine", str(mon.misc.met_game),
         "corpus del costruttore, non verificato"),
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
    ap.add_argument("--evento", help="sigla dell'evento, per esempio 10ANNI")
    ap.add_argument("--specie", help="nome della specie")
    ap.add_argument("--seme", help="seme di origine, in esadecimale o decimale")
    ap.add_argument("--lingua", default="ITA", help="ITA, ENG, JPN, FRA, GER, SPA")
    ap.add_argument("--out", help="prefisso dei due file da scrivere, senza estensione")
    ap.add_argument("--self-test", action="store_true", dest="self_test",
                    help="prove che non richiedono il sorgente del costruttore")
    a = ap.parse_args()

    if a.self_test:
        return self_test()
    if not a.ace:
        ap.error("serve --ace con la cartella del sorgente del costruttore")
    if a.elenco:
        return elenca(a.ace)
    if not (a.evento and a.specie and a.seme):
        ap.error("servono --evento, --specie e --seme; oppure --elenco")

    seme = int(a.seme, 16) if a.seme.lower().startswith("0x") else int(a.seme)
    mon, rapporto = componi(a.ace, a.evento, a.specie, seme, a.lingua)

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
