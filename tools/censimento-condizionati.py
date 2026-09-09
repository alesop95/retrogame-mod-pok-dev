#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Censisce gli incontri selvatici che una condizione sblocca, dalla prima alla quinta generazione.

La classe, e il criterio che la rende misurabile
-----------------------------------------------
Un esemplare puo' portare nel proprio dato la traccia di una circostanza che non si ripete: non la
rarita', che e' soltanto tempo speso, ma una condizione che il gioco deve avere soddisfatto perche'
quell'incontro esistesse. Il caso che ha aperto questo lavoro e' il Wynaut dell'Isola Miraggio in
terza generazione.

Su quel caso va scritta subito una correzione, perche' la premessa naturale e' sbagliata e sarebbe
finita nei documenti. L'isola non ha un luogo d'incontro proprio: nella fonte e' l'area d'erba del
luogo quarantacinque, cioe' della rotta che l'isola affaccia, e quel medesimo luogo porta accanto le
proprie aree d'acqua e di pesca con Tentacool, Wingull, Pelipper, Magikarp e Sharpedo. Un Wynaut
catturato la' registra dunque la rotta e non l'isola, e la traccia non e' il nome del luogo ma la
terna fra luogo, tipo di casella e specie: in quel luogo l'erba esiste soltanto quando l'isola
compare, e ospita quella specie sola.

Dire "condizione" a parole non basta, perche' senza un criterio meccanico l'elenco diventa una
raccolta di impressioni. Questo programma ne usa tre, e li tiene separati perche' rispondono a
domande diverse.

Il primo criterio e' il tipo di casella. La fonte classifica ogni area con un tipo, e alcuni tipi
sono essi stessi una condizione: lo sciame annunciato alla televisione in terza e quinta
generazione, la grotta nascosta di quinta, la gara di scarabei e l'albero del miele di quarta, le
aree della zona safari. Sono dichiarati in una tabella dentro questo programma, divisi fra
condizione di evento, cioe' qualcosa che accade nel mondo, e condizione di metodo, cioe' un modo di
cercare che il giocatore deve avere a disposizione. La divisione non e' un dettaglio: la prima
famiglia produce esemplari che nessun altro incontro produce, la seconda spesso no.

Il secondo criterio e' l'area monospecie esclusiva, ed e' quello che coglie il caso dell'isola: una
singola area che ospita una specie sola, la quale non compare in nessun'altra area del titolo. Non
serve sapere come si chiami il luogo quarantacinque per accorgersi che la sua erba ospita soltanto
Wynaut e che nel resto del gioco quella specie non si incontra.

Il terzo criterio e' il luogo dedicato, cioe' un luogo che ospita una sola specie contando tutte le
sue aree. E' piu' stretto del secondo e non lo sostituisce: e' la traccia piu' forte quando c'e',
perche' non richiede di guardare il tipo di casella, ma esclude proprio i casi come l'isola, dove
il luogo porta accanto le aree ordinarie della rotta.

Che cosa questo programma non fa, e va letto prima dei numeri
-------------------------------------------------------------
Legge le sole tabelle degli incontri selvatici. Gli incontri fissi, i doni e gli scambi stanno
altrove, nei file di codice della fonte, quindi la frase "unica via nel gioco" che questo programma
calcola vale sulle vie selvatiche e non su tutte: una specie che qui risulta ottenibile solo da una
condizione potrebbe essere anche un dono altrove, e il censimento lo dichiara invece di tacerlo.
Non copre inoltre la sesta generazione in avanti, dove il formato delle aree e' un altro e dove la
questione della scadenza non si pone.

Uso
---
    python tools/censimento-condizionati.py --pkhex _notes/fonti/pkhex
    python tools/censimento-condizionati.py --pkhex _notes/fonti/pkhex --check
    python tools/censimento-condizionati.py --self-test
"""

import argparse
import io
import os
import struct
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WILD = os.path.join("PKHeX.Core", "Resources", "legality", "wild")
NOMI_IT = os.path.join("PKHeX.Core", "Resources", "text", "other", "it", "text_Species_it.txt")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "CENSIMENTO-CONDIZIONATI.md")
NORMALIZZATO = os.path.join(RADICE, "pokedex-home-completo", "condizionati.csv")

# I tipi di casella che sono essi stessi una condizione, per generazione, con la famiglia a cui
# appartengono. I numeri vengono dalle enumerazioni `SlotType1` a `SlotType5` della fonte, lette
# una per una sotto `Legality/Encounters/Templates`: la prima generazione non ne ha alcuno.
#
#   evento: qualcosa e' accaduto nel mondo di gioco, e senza di esso la casella non esiste
#   metodo: il giocatore deve avere un modo di cercare, e la casella esiste sempre
CONDIZIONI = {
    "1": {},
    "2": {5: ("metodo", "spaccaroccia"), 6: ("metodo", "colpo di testa"),
          7: ("metodo", "colpo di testa su albero speciale"),
          8: ("evento", "gara di scarabei")},
    "3": {5: ("metodo", "spaccaroccia"), 6: ("evento", "sciame nell'erba"),
          7: ("evento", "sciame in acqua")},
    "4": {5: ("metodo", "spaccaroccia"), 6: ("metodo", "colpo di testa"),
          7: ("metodo", "colpo di testa su albero speciale"),
          8: ("evento", "gara di scarabei"), 9: ("evento", "albero del miele"),
          10: ("evento", "zona safari, erba"), 11: ("evento", "zona safari, acqua"),
          12: ("evento", "zona safari, canna corta"), 13: ("evento", "zona safari, canna buona"),
          14: ("evento", "zona safari, canna super")},
    "5": {4: ("evento", "sciame"), 5: ("evento", "grotta nascosta")},
}

# Il formato di un'area per generazione: quanto misura l'intestazione, dove sta il luogo e con
# quale ampiezza, quanto misura una casella e dove sta la specie dentro di essa. Ricavato dai
# costruttori `EncounterArea1` a `EncounterArea5` della fonte.
FORMATI = {
    "1": {"intestazione": 4, "luogo16": False, "casella": 4, "specie16": False},
    "2": {"intestazione": 4, "luogo16": False, "casella": 4, "specie16": False, "tariffe": True},
    "3": {"intestazione": 4, "luogo16": False, "casella": 10, "specie16": True},
    "4": {"intestazione": 6, "luogo16": False, "casella": 10, "specie16": True},
    "5": {"intestazione": 4, "luogo16": True, "casella": 4, "specie16": True, "maschera": 0x3FF},
}

# I file di ciascun titolo, in ordine di generazione. I due che la fonte tiene a parte sono
# dichiarati per quello che sono: lo sciame di terza generazione, che e' una condizione a tutti gli
# effetti, e le caselle della distribuzione del negozio di New York, che sono un evento e non una
# condizione, quindi si nominano e non si contano qui.
TITOLI = (
    ("1", "Rosso", "Gen1/encounter_red.pkl"),
    ("1", "Blu", "Gen1/encounter_blue.pkl"),
    ("1", "Giallo", "Gen1/encounter_yellow.pkl"),
    ("2", "Oro", "Gen2/encounter_gold.pkl"),
    ("2", "Argento", "Gen2/encounter_silver.pkl"),
    ("2", "Cristallo", "Gen2/encounter_crystal.pkl"),
    ("3", "Rubino", "Gen3/encounter_r.pkl"),
    ("3", "Zaffiro", "Gen3/encounter_s.pkl"),
    ("3", "Smeraldo", "Gen3/encounter_e.pkl"),
    ("3", "Rosso Fuoco", "Gen3/encounter_fr.pkl"),
    ("3", "Verde Foglia", "Gen3/encounter_lg.pkl"),
    ("3", "sciami di Hoenn", "Gen3/encounter_rse_swarm.pkl"),
    ("4", "Diamante", "Gen4/encounter_d.pkl"),
    ("4", "Perla", "Gen4/encounter_p.pkl"),
    ("4", "Platino", "Gen4/encounter_pt.pkl"),
    ("4", "Oro HeartGold", "Gen4/encounter_hg.pkl"),
    ("4", "Argento SoulSilver", "Gen4/encounter_ss.pkl"),
    ("5", "Nero", "Gen5/encounter_b.pkl"),
    ("5", "Bianco", "Gen5/encounter_w.pkl"),
    ("5", "Nero 2", "Gen5/encounter_b2.pkl"),
    ("5", "Bianco 2", "Gen5/encounter_w2.pkl"),
)

# Il file degli sciami di terza generazione non porta il tipo dentro l'area, perche' la fonte lo
# impone da fuori chiamando un costruttore diverso: tutte le sue aree sono uno sciame.
TIPO_IMPOSTO = {"Gen3/encounter_rse_swarm.pkl": 6}

MAX_SPECIE = 1025


def nomi_specie(percorso):
    if not os.path.exists(percorso):
        return None
    return [r.strip() for r in io.open(percorso, encoding="utf-8").read().split("\n")]


def aree(dati):
    """Le aree di un archivio indicizzato, con la tabella delle posizioni a trentadue bit.

    La fine di un'area coincide con l'inizio della successiva, quindi la coppia si legge come un
    intero doppio: e' la stessa lettura che `tools/ottenibilita-titoli.py` fa sugli archivi
    moderni, e sta qui in forma ridotta invece di essere importata perche' i due programmi non
    devono dipendere l'uno dall'altro.
    """
    if len(dati) < 4:
        return None
    quante = struct.unpack_from("<H", dati, 2)[0]
    fuori = []
    for i in range(quante):
        off = 4 + i * 4
        if off + 8 > len(dati):
            return None
        coppia = struct.unpack_from("<Q", dati, off)[0]
        inizio, fine = coppia & 0xFFFFFFFF, coppia >> 32
        if not (0 <= inizio <= fine <= len(dati)):
            return None
        fuori.append(dati[inizio:fine])
    return fuori


def leggi_area(area, formato, tipo_imposto=None):
    """Un'area come terna fra luogo, tipo e insieme delle specie che ospita."""
    if len(area) < formato["intestazione"]:
        return None
    luogo = (struct.unpack_from("<H", area, 0)[0] if formato["luogo16"] else area[0])
    tipo = tipo_imposto if tipo_imposto is not None else area[2]
    corpo = area[formato["intestazione"]:]
    if formato.get("tariffe") and tipo > 1:
        # In seconda generazione le aree che non sono erba o acqua portano davanti alle caselle
        # una tariffa per casella, quindi la regione delle caselle comincia piu' avanti. Ignorare
        # questo scostamento non produce un errore ma specie inventate, ed e' il genere di difetto
        # che si vede solo confrontando con una fonte umana.
        quante = len(corpo) // (formato["casella"] + 1)
        corpo = corpo[quante:]
    specie = set()
    passo = formato["casella"]
    for off in range(0, len(corpo) - passo + 1, passo):
        if formato["specie16"]:
            sp = struct.unpack_from("<H", corpo, off)[0]
            if "maschera" in formato:
                sp &= formato["maschera"]
        else:
            sp = corpo[off]
        if 1 <= sp <= MAX_SPECIE:
            specie.add(sp)
    return luogo, tipo, specie


def leggi_titolo(percorso, generazione, chiave_file):
    """Le aree di un titolo, oppure None se l'archivio non si legge."""
    if not os.path.exists(percorso):
        return None
    dati = io.open(percorso, "rb").read()
    blocchi = aree(dati)
    if blocchi is None:
        return None
    formato = FORMATI[generazione]
    imposto = TIPO_IMPOSTO.get(chiave_file)
    fuori = []
    for a in blocchi:
        letta = leggi_area(a, formato, imposto)
        if letta is not None:
            fuori.append(letta)
    return fuori


def analizza(titolo_aree, generazione):
    """I due criteri applicati a un titolo.

    Restituisce le specie che nelle sole vie selvatiche vengono da una condizione, divise per
    famiglia, e i luoghi che ospitano una sola specie in tutto il titolo.
    """
    condizioni = CONDIZIONI[generazione]
    da_condizione = {}
    da_ordinario = set()
    per_luogo = {}
    for luogo, tipo, specie in titolo_aree:
        per_luogo.setdefault(luogo, set()).update(specie)
        if tipo in condizioni:
            famiglia, etichetta = condizioni[tipo]
            for sp in specie:
                da_condizione.setdefault(sp, set()).add((famiglia, etichetta))
        else:
            da_ordinario.update(specie)
    solo_condizione = {sp: v for sp, v in da_condizione.items() if sp not in da_ordinario}
    dedicati = {l: sorted(s)[0] for l, s in per_luogo.items() if len(s) == 1}

    # Il terzo criterio, che e' quello che coglie il caso dell'Isola Miraggio, e la ragione per cui
    # esiste va scritta perche' e' una correzione a come la classe era stata immaginata. Il luogo
    # dell'isola non e' un luogo proprio: la fonte la tiene come l'area d'erba del luogo
    # quarantacinque, cioe' la rotta che l'isola affaccia, e quel luogo porta accanto le sue aree
    # d'acqua ordinarie. Cercare un luogo dedicato non la trova quindi mai. Ciò che la distingue e'
    # che la sua area ospita una specie sola, cosa che nel resto del gioco quasi non accade, e che
    # quella specie non compare in nessun'altra area del titolo.
    monospecie = []
    for luogo, tipo, specie in titolo_aree:
        if len(specie) != 1:
            continue
        sp = sorted(specie)[0]
        altrove = any(sp in s2 for l2, t2, s2 in titolo_aree if (l2, t2) != (luogo, tipo))
        monospecie.append({"luogo": luogo, "tipo": tipo, "specie": sp, "altrove": altrove})
    return {
        "aree": len(titolo_aree),
        "specie": len({sp for _, _, s in titolo_aree for sp in s}),
        "da_condizione": da_condizione,
        "solo_condizione": solo_condizione,
        "luoghi": per_luogo,
        "dedicati": dedicati,
        "monospecie": monospecie,
    }


def componi(risultati, nomi):
    def nome(sp):
        return nomi[sp] if nomi and 0 < sp < len(nomi) else str(sp)

    r = ["# Censimento degli incontri che una condizione sblocca", ""]
    r.append("> Documento generato da `tools/censimento-condizionati.py` dalle tabelle degli incontri selvatici del verificatore. Non si modifica a mano: si rigenera. Copre dalla prima alla quinta generazione, cioe' i titoli la cui via verso il deposito passa dalla banca.")
    r.append("")
    r.append("I due criteri sono dichiarati nel docstring del programma e vanno letti prima dei numeri. Il primo e' il tipo di casella, dove alcuni tipi sono essi stessi una condizione, divisi fra condizione di evento e condizione di metodo. Il secondo e' il luogo dedicato, cioe' un luogo che in tutto il titolo ospita una sola specie: la sua presenza sul dato di un esemplare identifica quell'incontro e nessun altro.")
    r.append("")
    r.append("Il limite da tenere presente e' che qui stanno le sole vie selvatiche: incontri fissi, doni e scambi stanno in altre tabelle, quindi una specie che risulti ottenibile solo da una condizione lo e' fra le vie selvatiche e non necessariamente in assoluto.")
    r.append("")

    r.append("## Quadro d'insieme")
    r.append("")
    r.append("| Titolo | Gen | Aree | Specie selvatiche | Aree condizionate | Specie solo da condizione | Aree monospecie esclusive | Luoghi dedicati |")
    r.append("|---|---|---|---|---|---|---|---|")
    for t in risultati:
        if t["errore"]:
            r.append("| %s | %s | non letto: %s | | | | | |" % (t["titolo"], t["gen"], t["errore"]))
            continue
        a = t["analisi"]
        condizionate = sum(1 for luogo, tipo, _ in t["aree_lette"] if tipo in CONDIZIONI[t["gen"]])
        esclusive = len({(v["luogo"], v["tipo"], v["specie"])
                         for v in a["monospecie"] if not v["altrove"]})
        r.append("| %s | %s | %d | %d | %d | %d | %d | %d |"
                 % (t["titolo"], t["gen"], a["aree"], a["specie"], condizionate,
                    len(a["solo_condizione"]), esclusive, len(a["dedicati"])))
    r.append("")

    r.append("## Le specie che fra le vie selvatiche vengono solo da una condizione")
    r.append("")
    r.append("E' la parte che pesa per la collezione, perche' un esemplare di queste specie porta necessariamente la traccia della condizione che lo ha prodotto.")
    r.append("")
    for t in risultati:
        if t["errore"] or not t["analisi"]["solo_condizione"]:
            continue
        r.append("### %s" % t["titolo"])
        r.append("")
        r.append("| Specie | Dex | Condizione |")
        r.append("|---|---|---|")
        for sp in sorted(t["analisi"]["solo_condizione"]):
            etichette = sorted({e for _, e in t["analisi"]["solo_condizione"][sp]})
            r.append("| %s | %d | %s |" % (nome(sp), sp, "; ".join(etichette)))
        r.append("")

    r.append("## Le aree che ospitano una specie sola, e non compare altrove nel titolo")
    r.append("")
    r.append("E' il criterio che coglie il caso da cui questo lavoro e' nato, e la sua formulazione e' una correzione a come la classe era stata immaginata. L'Isola Miraggio non ha un luogo proprio: la fonte la tiene come l'area d'erba del luogo che la rotta affaccia, e quel medesimo luogo porta accanto le proprie aree d'acqua ordinarie, quindi cercare un luogo dedicato non la trova mai. Cio' che la distingue e' che la sua area ospita una specie sola e che quella specie non compare in nessun'altra area del titolo: la traccia sul dato e' allora la terna fra luogo, tipo di casella e specie, non il nome del luogo.")
    r.append("")
    for t in risultati:
        if t["errore"]:
            continue
        # Piu' aree dello stesso luogo e dello stesso tipo, che la fonte tiene separate per
        # fascia oraria o per stanza, sono la medesima traccia: si contano una volta.
        viste, sole = set(), []
        for v in t["analisi"]["monospecie"]:
            if v["altrove"]:
                continue
            firma = (v["luogo"], v["tipo"], v["specie"])
            if firma in viste:
                continue
            viste.add(firma)
            sole.append(v)
        if not sole:
            continue
        r.append("### %s" % t["titolo"])
        r.append("")
        r.append("| Luogo | Tipo di casella | Specie | Dex |")
        r.append("|---|---|---|---|")
        for v in sorted(sole, key=lambda x: (x["luogo"], x["tipo"])):
            etichetta = CONDIZIONI[t["gen"]].get(v["tipo"], (None, "ordinaria"))[1]
            r.append("| %d | %d, %s | %s | %d |"
                     % (v["luogo"], v["tipo"], etichetta, nome(v["specie"]), v["specie"]))
        r.append("")

    r.append("## I luoghi dedicati a una sola specie")
    r.append("")
    r.append("Un luogo dedicato e' il criterio piu' stretto: se in tutto il titolo quel numero di luogo ospita una specie sola, contando tutte le sue aree, allora un esemplare che lo porti viene da la' e da nessun altro posto. E' piu' stretto del criterio precedente e non lo sostituisce, perche' un luogo che ospiti anche una sola area d'acqua ordinaria esce da questo elenco pur restando una traccia valida nel precedente.")
    r.append("")
    for t in risultati:
        if t["errore"] or not t["analisi"]["dedicati"]:
            continue
        r.append("### %s" % t["titolo"])
        r.append("")
        r.append("| Luogo | Specie | Dex |")
        r.append("|---|---|---|")
        for luogo in sorted(t["analisi"]["dedicati"]):
            sp = t["analisi"]["dedicati"][luogo]
            r.append("| %d | %s | %d |" % (luogo, nome(sp), sp))
        r.append("")
    return "\n".join(r) + "\n"


def normalizza(risultati, nomi):
    r = ["titolo,generazione,criterio,luogo,dex,specie,condizione"]
    for t in risultati:
        if t["errore"]:
            continue
        for sp, marche in sorted(t["analisi"]["solo_condizione"].items()):
            nome = nomi[sp] if nomi and sp < len(nomi) else ""
            etichette = "; ".join(sorted({e for _, e in marche}))
            r.append(",".join(['"%s"' % t["titolo"], t["gen"], "tipo di casella", "",
                               str(sp), nome, '"%s"' % etichette]))
        for luogo, sp in sorted(t["analisi"]["dedicati"].items()):
            nome = nomi[sp] if nomi and sp < len(nomi) else ""
            r.append(",".join(['"%s"' % t["titolo"], t["gen"], "luogo dedicato", str(luogo),
                               str(sp), nome, ""]))
        viste = set()
        for v in sorted(t["analisi"]["monospecie"], key=lambda x: (x["luogo"], x["tipo"])):
            if v["altrove"]:
                continue
            firma = (v["luogo"], v["tipo"], v["specie"])
            if firma in viste:
                continue
            viste.add(firma)
            sp = v["specie"]
            nome = nomi[sp] if nomi and sp < len(nomi) else ""
            etichetta = CONDIZIONI[t["gen"]].get(v["tipo"], (None, "ordinaria"))[1]
            r.append(",".join(['"%s"' % t["titolo"], t["gen"], "area monospecie", str(v["luogo"]),
                               str(sp), nome, '"tipo %d, %s"' % (v["tipo"], etichetta)]))
    return "\n".join(r) + "\n"


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    # Un'area di terza generazione: intestazione di quattro byte e caselle da dieci, con la specie
    # su due byte in testa alla casella.
    area = bytes([45, 0, 0, 20]) + struct.pack("<H", 360) + bytes([0, 0, 25, 30, 0, 0, 0, 0])
    prova("l'area di terza generazione", (45, 0, {360}), leggi_area(area, FORMATI["3"]))

    # Il tipo imposto dall'esterno, che e' il caso dell'archivio degli sciami.
    prova("il tipo imposto vince su quello scritto", 6, leggi_area(area, FORMATI["3"], 6)[1])

    # La prima generazione: specie su un byte e casella da quattro.
    area = bytes([88, 0, 2, 0]) + bytes([129, 0, 5, 5])
    prova("l'area di prima generazione", (88, 2, {129}), leggi_area(area, FORMATI["1"]))

    # La quinta generazione: luogo su due byte, e specie e forma impacchettate in due byte.
    area = bytes([0x2C, 0x01, 4, 0]) + struct.pack("<H", 519 | (0 << 11)) + bytes([10, 12])
    prova("l'area di quinta generazione", (300, 4, {519}), leggi_area(area, FORMATI["5"]))

    # La seconda generazione con le tariffe: un'area di tipo maggiore di uno porta una tariffa per
    # casella davanti alle caselle, e ignorarla produce specie inventate. Due caselle, quindi due
    # byte di tariffa: senza lo scostamento la prima specie letta sarebbe la tariffa stessa.
    corpo = bytes([30, 40]) + bytes([16, 0, 3, 3]) + bytes([19, 1, 4, 4])
    area = bytes([2, 0, 8, 20]) + corpo
    prova("l'area di seconda generazione salta le tariffe", (2, 8, {16, 19}),
          leggi_area(area, FORMATI["2"]))

    # Controllo negativo: senza lo scostamento le specie sarebbero altre, e questa e' la prova che
    # il presidio serva.
    senza = leggi_area(bytes([2, 0, 0, 20]) + corpo, FORMATI["2"])
    prova("e senza lo scostamento sarebbero diverse", True, senza[2] != {16, 19})

    # I due criteri su un titolo finto: Wynaut sta in un luogo dedicato, e la specie 265 viene
    # soltanto da uno sciame mentre la 263 viene anche da un'area ordinaria.
    finto = [
        (45, 0, {360}),
        (16, 0, {263, 261}),
        (16, 6, {265, 263}),
    ]
    a = analizza(finto, "3")
    prova("le aree contate", 3, a["aree"])
    prova("il luogo dedicato e' quello di Wynaut", {45: 360}, a["dedicati"])
    prova("la specie solo da sciame", [265], sorted(a["solo_condizione"]))
    prova("e quella che viene anche da un'area ordinaria non entra", False, 263 in a["solo_condizione"])
    prova("la famiglia della condizione", {("evento", "sciame nell'erba")},
          a["solo_condizione"][265])

    # L'archivio indicizzato: due aree, con la coppia di posizioni come intero doppio.
    testa = struct.pack("<HH", 0, 2)
    a1 = bytes([1, 0, 0, 10]) + bytes([16, 0, 2, 2])
    a2 = bytes([2, 0, 0, 10]) + bytes([19, 0, 2, 2])
    inizio1 = 4 + 2 * 4
    inizio2 = inizio1 + len(a1)
    tabella = struct.pack("<II", inizio1, inizio2) + struct.pack("<II", inizio2, inizio2 + len(a2))
    prova("l'archivio si scompone in due aree", 2, len(aree(testa + tabella + a1 + a2)))
    prova("un archivio troncato viene rifiutato", None, aree(b"\x00"))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "pkhex"))
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    pkhex = a.pkhex if os.path.isabs(a.pkhex) else os.path.join(RADICE, a.pkhex)
    nomi = nomi_specie(os.path.join(pkhex, NOMI_IT))
    risultati = []
    for gen, titolo, chiave in TITOLI:
        percorso = os.path.join(pkhex, WILD, *chiave.split("/"))
        lette = leggi_titolo(percorso, gen, chiave)
        if lette is None:
            risultati.append({"titolo": titolo, "gen": gen, "errore": "archivio assente o illeggibile",
                              "aree_lette": [], "analisi": None})
            continue
        risultati.append({"titolo": titolo, "gen": gen, "errore": "",
                          "aree_lette": lette, "analisi": analizza(lette, gen)})

    testo = componi(risultati, nomi)
    csv = normalizza(risultati, nomi)
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
    print("scritti %s e %s" % (USCITA, NORMALIZZATO))
    for t in risultati:
        if t["errore"]:
            print("  %-20s NON letto: %s" % (t["titolo"], t["errore"]))
        else:
            an = t["analisi"]
            print("  %-20s aree %3d | specie %4d | solo da condizione %3d | luoghi dedicati %3d"
                  % (t["titolo"], an["aree"], an["specie"], len(an["solo_condizione"]),
                     len(an["dedicati"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
