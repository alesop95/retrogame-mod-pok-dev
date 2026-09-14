#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone gli esemplari degli scambi in gioco di terza generazione, byte per byte.

Perche' questa classe si genera senza cercare alcun seme
--------------------------------------------------------
Le altre classi che questo progetto produce hanno un punto in comune: il gioco calcola il valore
di personalita' e i valori individuali al momento della consegna, quindi riprodurli richiede o un
generatore da ricostruire o una ricerca di semi. Gli scambi in gioco di terza generazione no. La
fonte li scrive: per diciannove voci il valore di personalita' e' una costante esadecimale nella
tabella, i sei valori individuali sono un insieme dichiarato, e con essi sono dichiarati
l'identificativo dell'allenatore, il suo sesso, il sesso dell'esemplare, quale delle due abilita'
porti e le cinque statistiche di gara. Non resta nulla da indovinare, e questo programma non
contiene alcun generatore pseudocasuale: e' un compositore e non un cercatore.

Ne segue che la fedelta' qui non e' un argomento ma una identita'. Dove per una distribuzione il
progetto deve discutere quanto un esemplare composto somigli a quello storico, per queste
diciannove voci l'esemplare composto e' quello storico, campo per campo, salvo cio' che il
giocatore aggiunge dopo averlo ricevuto.

Che cosa distingue uno scambio da tutto il resto
------------------------------------------------
Tre cose, e vanno tenute insieme perche' sbagliarne una sola produce un esemplare che il
verificatore rifiuta senza dire quale. La prima e' che l'allenatore non e' il giocatore: nome,
identificativo e sesso sono quelli del personaggio che consegna, e il nome e' specifico della
lingua. La seconda e' che il soprannome e' fissato e anch'esso specifico della lingua, quindi la
bandierina che distingue un esemplare soprannominato da uno che porta il proprio nome di specie
va accesa. La terza e' che il luogo d'incontro non e' un luogo del mondo ma il codice dello
scambio con un personaggio, che vale duecentocinquantaquattro, e la sfera e' sempre la Poke Ball.

L'ordine dei valori individuali, che e' la trappola di questa classe
--------------------------------------------------------------------
La fonte dichiara i sei valori individuali in un insieme il cui ordine e' punti salute, attacco,
difesa, VELOCITA', attacco speciale e difesa speciale. La velocita' sta al quarto posto e non al
sesto, che e' l'ordine che verrebbe naturale scrivere: chi assumesse l'ordine consueto otterrebbe
sei numeri plausibili nelle posizioni sbagliate, e nessun controllo interno se ne accorgerebbe
perche' ogni valore resta dentro il proprio intervallo. L'ordine e' stato verificato sulla
definizione della struttura invece che dedotto, e coincide con quello che lo strato di terza
generazione di questo progetto usa per impacchettare la parola dei valori individuali: il
programma lo verifica comunque a ogni corsa, invece di fidarsi della coincidenza.

Uso
---
    python tools/genera-scambio-gen3.py --elenco --pkhex <clone>
    python tools/genera-scambio-gen3.py --pkhex <clone> --ace <clone> --lotto _notes/lotto-scambi-gen3
    python tools/genera-scambio-gen3.py --self-test
"""

import argparse
import importlib.util
import io
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))

from pokebridge import charmap as cm  # noqa: E402
from pokebridge import gen3  # noqa: E402

# Il codice del luogo d'incontro per uno scambio con un personaggio, letto dalla tabella dei
# luoghi della fonte e non trascritto a memoria.
NOME_LUOGO = "LinkTrade3NPC"
FILE_LUOGHI = os.path.join("PKHeX.Core", "Game", "Locations", "Locations.cs")

# L'ordine con cui la fonte dichiara i sei valori individuali. Sta qui dichiarato perche' il
# programma lo verifichi contro lo strato di terza generazione, non perche' lo si possa cambiare.
ORDINE_IV = ("hp", "atk", "def", "spd", "satk", "sdef")

# Le lingue che il progetto produce, con il codice che il formato usa. L'italiano c'e' perche' le
# cartucce possedute sono italiane; il giapponese perche' una parte di questi scambi esiste
# soltanto la'.
LINGUE = {"Italian": 5, "English": 2, "Japanese": 1}

# Le due abilita' come la fonte le nomina, e il bit che ne discende.
ABILITA = {"OnlyFirst": 0, "OnlySecond": 1}


def carica_censimento():
    """Il lettore delle tabelle degli scambi, usato come modulo invece che riscritto."""
    percorso = os.path.join(RADICE, "tools", "censimento-scambi.py")
    spec = importlib.util.spec_from_file_location("censimento_scambi", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def luogo_scambio(pkhex):
    """Il codice del luogo, letto dalla tabella dei luoghi della fonte."""
    percorso = os.path.join(pkhex, FILE_LUOGHI)
    if not os.path.exists(percorso):
        raise SystemExit("manca la tabella dei luoghi sotto " + pkhex + ": questo programma non "
                         "inventa il codice del luogo di scambio")
    import re
    testo = io.open(percorso, encoding="utf-8-sig").read()
    m = re.search(r"const\s+ushort\s+" + NOME_LUOGO + r"\s*=\s*(\d+)", testo)
    if not m:
        raise SystemExit("la tabella dei luoghi non dichiara piu' " + NOME_LUOGO +
                         ": la fonte e' cambiata e va riletta")
    return int(m.group(1))


def valori_individuali(testo):
    """I sei valori individuali di una voce, nell'ordine con cui la fonte li dichiara.

    Restituisce un dizionario con le chiavi dello strato di terza generazione, cosicche' la
    corrispondenza fra i due ordini sia fatta qui una volta sola e in un posto solo.
    """
    if not testo:
        return None
    import re
    numeri = [int(n) for n in re.findall(r"\d+", testo)]
    if len(numeri) != 6:
        return None
    return dict(zip(ORDINE_IV, numeri))


def verifica_ordine_iv():
    """Che l'ordine dichiarato qui sia quello che lo strato di terza generazione impacchetta.

    Non e' una formalita': i due ordini coincidono oggi, e se un giorno uno dei due cambiasse il
    programma scriverebbe sei numeri giusti in posizioni sbagliate, che e' un difetto che nessun
    controllo interno rivela perche' ogni valore resta nel proprio intervallo.
    """
    if tuple(gen3.EV_ORDER) != ORDINE_IV:
        raise SystemExit("l'ordine dei valori individuali dichiarato qui, %s, non coincide con "
                         "quello dello strato di terza generazione, %s: uno dei due e' cambiato "
                         "e finche' non si sa quale non si scrive nulla"
                         % (ORDINE_IV, tuple(gen3.EV_ORDER)))


def voci_scambio(censimento, pkhex):
    """Le voci di scambio di terza generazione che la fonte descrive per intero."""
    tabelle = censimento.censisci(pkhex, [], lingue=("it", "en", "ja"))
    if tabelle is None:
        raise SystemExit("il clone non porta le tabelle degli incontri sotto " + pkhex)
    fuori = []
    for t in tabelle:
        if t["generazione"] != "3" or t["tipo"] != "EncounterTrade3":
            continue
        for v in t["voci"]:
            if not v.get("pid"):
                continue
            fuori.append((t["tabella"], v))
    return fuori


def componi(ace, pkhex, tabella, voce, lingua, luogo):
    """Un esemplare di scambio, composto dai campi che la fonte dichiara."""
    g3 = carica_g3(ace)
    props = voce.get("proprieta") or {}
    nazionale = voce["specie"]
    livello = voce["livello"]

    mappa = g3.nazionale_verso_interno(ace)
    specie_id = mappa.get(nazionale)
    if specie_id is None:
        raise KeyError("nessun identificativo interno per il numero nazionale %d" % nazionale)
    gruppo = g3.gruppo_di_crescita(ace).get(specie_id)
    if gruppo is None:
        raise KeyError("gruppo di crescita ignoto per la specie interna %d" % specie_id)

    iv = valori_individuali(props.get("IVs"))
    if iv is None:
        raise KeyError("la voce non dichiara sei valori individuali: %r" % props.get("IVs"))

    personalita = int(voce["pid"], 16)
    tid = int(props.get("TID16", "0"))
    sid = int(props.get("SID16", "0"))

    sigla = {"Italian": "it", "English": "en", "Japanese": "ja"}[lingua]
    soprannome_testo = (voce.get("soprannomi") or {}).get(sigla)
    if not soprannome_testo:
        return None, {"saltata": "nessun soprannome in " + lingua}

    tabella_caratteri = cm.Charmap.gen3_per_lingua(lingua)
    soprannome = tabella_caratteri.encode(soprannome_testo, length=gen3.NICKNAME_LENGTH)

    nome_ot_testo = (voce.get("allenatori") or {}).get(sigla)
    if not nome_ot_testo:
        return None, {"saltata": "nessun nome di allenatore in " + lingua}
    ot = tabella_caratteri.encode(nome_ot_testo, length=gen3.OT_NAME_LENGTH)

    bit = ABILITA.get(props.get("Ability", "OnlyFirst"), 0)

    mon = gen3.Gen3Mon(
        personality=personalita,
        ot_id=((sid & 0xFFFF) << 16) | (tid & 0xFFFF),
        nickname=soprannome,
        language=LINGUE[lingua],
        # La bandierina del soprannome: questi esemplari ne portano uno fissato, diverso dal
        # nome della specie, e senza di essa il verificatore li contesta.
        flags=0x02,
        ot_name=ot,
        markings=0,
        growth=gen3.Growth(species=specie_id, held_item=0,
                           experience=g3.esperienza(gruppo, livello),
                           pp_bonuses=0, friendship=0),
        attacks=gen3.Attacks(moves=[0, 0, 0, 0], pp=[0, 0, 0, 0]),
        evs=gen3.EvsCondition(),
        misc=gen3.Misc(
            pokerus=0,
            met_location=luogo,
            met_level=livello,
            met_game=0,
            pokeball=4,
            ot_female=(props.get("OTGender") == "1"),
            ivs=iv,
            is_egg=False,
            ability_num=bit,
            modern_fateful_encounter=False,
        ),
    )
    return mon, {
        "tabella": tabella, "specie": nazionale, "livello": livello,
        "personalita": "0x%08X" % personalita, "tid": tid, "sid": sid,
        "iv": iv, "soprannome": soprannome_testo, "allenatore": nome_ot_testo,
        "lingua": lingua, "luogo": luogo, "abilita": bit,
    }


def carica_g3(ace):
    """Lo strato che sa leggere le tabelle di gioco, caricato come fa il resto della famiglia."""
    percorso = os.path.join(RADICE, "tools", "genera-incontro-gen3.py")
    spec = importlib.util.spec_from_file_location("gen3_incontri", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.G3


def collaudo():
    esiti = []

    def prova(nome, condizione):
        esiti.append((nome, bool(condizione)))

    verifica_ordine_iv()
    prova("l'ordine dei valori individuali coincide con quello dello strato di terza generazione",
          tuple(gen3.EV_ORDER) == ORDINE_IV)
    prova("la velocita' sta al quarto posto e non al sesto, che e' la trappola di questa classe",
          ORDINE_IV[3] == "spd")

    iv = valori_individuali("new(20,15,17,24,23,22)")
    prova("i sei valori individuali si leggono nell'ordine della fonte",
          iv == {"hp": 20, "atk": 15, "def": 17, "spd": 24, "satk": 23, "sdef": 22})
    prova("negativo: un insieme con meno di sei valori non si completa a caso",
          valori_individuali("new(20,15,17)") is None)
    prova("negativo: una proprieta' assente non produce valori individuali a zero",
          valori_individuali(None) is None)

    finto = "public const ushort LinkTrade3NPC = 254;"
    import re
    m = re.search(r"const\s+ushort\s+" + NOME_LUOGO + r"\s*=\s*(\d+)", finto)
    prova("il codice del luogo si legge dalla tabella invece di essere trascritto",
          m and int(m.group(1)) == 254)

    prova("negativo: le abilita' note sono due e non si indovina una terza",
          set(ABILITA) == {"OnlyFirst", "OnlySecond"} and ABILITA["OnlySecond"] == 1)

    falliti = [n for n, e in esiti if not e]
    for nome, esito in esiti:
        print(("  ok   " if esito else "  FALLITO ") + nome)
    print("")
    print(str(len(esiti) - len(falliti)) + " prove, " + str(len(falliti)) + " fallite.")
    return 1 if falliti else 0


def principale(argomenti=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--pkhex", default=os.path.join(RADICE, "_notes", "fonti", "pkhex"))
    p.add_argument("--ace", default=os.path.join(RADICE, "_notes", "fonti", "ace-builder"))
    p.add_argument("--lingua", default="Italian", choices=sorted(LINGUE))
    p.add_argument("--elenco", action="store_true",
                   help="stampa le voci che la fonte descrive per intero, senza comporre nulla")
    p.add_argument("--lotto", default=None, help="cartella in cui scrivere gli esemplari")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args(argomenti)
    if a.self_test:
        return collaudo()

    verifica_ordine_iv()
    censimento = carica_censimento()
    voci = voci_scambio(censimento, a.pkhex)
    if not voci:
        print("nessuna voce di scambio di terza generazione con il valore di personalita'")
        return 1

    if a.elenco:
        print("Gli scambi in gioco di terza generazione che la fonte descrive per intero.")
        print("")
        print("%-18s %5s %4s %-12s %-8s %-12s %s"
              % ("tabella", "dex", "lv", "personalita", "id", "soprannome IT", "nota"))
        for tabella, v in voci:
            sn = (v.get("soprannomi") or {}).get("it") or "-"
            print("%-18s %5s %4s %-12s %-8s %-12s %s"
                  % (tabella, v["specie"], v["livello"], v["pid"],
                     (v.get("proprieta") or {}).get("TID16", "-"), sn,
                     (v["commento"] or "")[:40]))
        print("")
        print("%d voci." % len(voci))
        return 0

    # La scrittura degli esemplari non e' ancora attiva, e vale dire con precisione che cosa le
    # manchi invece di lasciarlo intendere. Le stringhe ci sono dal 2026-09-14, i valori
    # individuali e il valore di personalita' pure, il codice del luogo si legge dalla fonte. Ne
    # manca uno solo: la versione in cui lo scambio avviene, che la tabella dichiara come terzo
    # argomento e che va tradotta nel codice del gioco di incontro. Finche' quella traduzione non
    # e' letta dalla fonte come tutto il resto, comporre significherebbe indovinare un campo, ed
    # e' esattamente il genere di ipotesi che in questa giornata ha gia' prodotto tre difetti
    # invisibili.
    print("composizione non ancora attiva: manca la traduzione della versione di incontro, che e'")
    print("il terzo argomento della tabella. Tutto il resto e' pronto, cioe' valore di")
    print("personalita', valori individuali, identificativo, soprannome e allenatore per lingua,")
    print("abilita', sesso e codice del luogo. La voce sta in pending.md.")
    return 2


if __name__ == "__main__":
    sys.exit(principale())
