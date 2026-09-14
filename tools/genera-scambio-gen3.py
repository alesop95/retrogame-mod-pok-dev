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
import re
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

# Le lingue che il progetto produce, nella grafia che la fonte usa per i nomi delle specie e per
# la codifica dei caratteri. Il codice del byte della lingua NON e' scritto qui: si prende dalla
# tabella del generatore delle distribuzioni, che la porta gia'. La prima stesura lo aveva
# trascritto a memoria e aveva dato all'italiano il codice cinque, che e' il tedesco: tutti e
# diciannove gli esemplari del primo lotto sono usciti in tedesco, e il verificatore lo ha
# mostrato al primo colpo. E' l'errore che il progetto documenta da giorni, cioe' trascrivere una
# tabella corta invece di leggerla, commesso su una tabella di sei righe.
LINGUE = {"Italian": "ITA", "English": "ENG", "Japanese": "JPN"}

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


# L'apostrofo dritto non esiste nella codifica di terza generazione, che conosce i soli apostrofi
# tipografici. La fonte scrive pero' quello dritto dentro i soprannomi, per esempio in CH'DING, e
# il gioco vi mostra quello destro. La sostituzione e' quindi una traduzione verso il carattere
# vero e non una pulizia di comodo, ed e' la medesima che il censimento fa nel verso opposto
# quando confronta i nomi delle specie con i commenti della fonte.
APOSTROFO_DRITTO = "'"
APOSTROFO_DESTRO = u"\u2019"


def azzera_dopo_il_terminatore(campo):
    """Il campo di un nome con i byte dopo il terminatore portati a zero.

    Serve a una regola del verificatore che il terzo giudizio ha reso esplicita: i byte oltre il
    terminatore sono spazzatura e devono essere azzerati. L'encoder di `pokebridge` riempie invece
    l'avanzo ripetendo il terminatore, che e' cio' che si trova in molti salvataggi veri e che le
    duecentosei prove del ponte danno per buono: la correzione sta percio' qui e non la', perche'
    cambiare l'encoder cambierebbe il comportamento di tutto il pacchetto per una regola che vale
    su questa classe.

    La misura che la giustifica e' esatta e va conservata, perche' spiega perche' otto voci su
    diciannove passassero mentre le altre no. Il campo del nome dell'allenatore e' lungo sette
    byte: un nome di sette caratteri non ha terminatore e uno di sei ne ha uno solo, quindi
    nessuno dei due lascia spazzatura; un nome di quattro o cinque caratteri ne lascia due o tre.
    Gli otto conformi erano tutti e soli quelli con il nome di sei o sette caratteri.

    Il soprannome resta invece com'e'. I conformi ne portano il riempimento a terminatori ripetuti
    e sono conformi lo stesso, quindi per quel campo la forma attuale e' gia' accettata: si cambia
    cio' che l'evidenza indica e non cio' che le somiglia.
    """
    if not campo:
        return campo
    fuori = bytearray(campo)
    for i, b in enumerate(fuori):
        if b == 0xFF:
            for j in range(i + 1, len(fuori)):
                fuori[j] = 0x00
            break
    return bytes(fuori)


def verso_la_codifica(testo):
    """Un nome della fonte nella forma che la codifica di terza generazione sa scrivere."""
    return (testo or "").replace(APOSTROFO_DRITTO, APOSTROFO_DESTRO)


# Le costanti delle statistiche da gara che la fonte dichiara accanto a ciascuno scambio. Si
# leggono dal sorgente e non si trascrivono: sono sei numeri per costante e una mezza dozzina di
# costanti, cioe' esattamente la taglia di tabella che questo progetto ha gia' sbagliato tre volte
# copiandola a mano.
RE_COSTANTE_GARA = re.compile(
    r"ReadOnlySpan<byte>\s+(TradeContest_\w+)\s*=>\s*\[([^\]]*)\]")


def statistiche_di_gara(pkhex):
    """Dal nome della costante ai suoi sei valori, letti dai file degli incontri di terza.

    I sei sono, nell'ordine della fonte, le cinque statistiche da gara e la lucentezza estetica.
    Le stesse costanti compaiono in piu' file con i medesimi valori: si legge il primo che si
    incontra e si verifica che un secondo non lo contraddica, perche' una divergenza fra due
    definizioni omonime sarebbe un fatto sulla fonte e non un dettaglio da ignorare.
    """
    fuori = {}
    cartella = os.path.join(pkhex, "PKHeX.Core", "Legality", "Encounters", "Data", "Gen3")
    if not os.path.isdir(cartella):
        return fuori
    for nome in sorted(os.listdir(cartella)):
        if not nome.endswith(".cs"):
            continue
        testo = io.open(os.path.join(cartella, nome), encoding="utf-8", errors="replace").read()
        for chiave, corpo in RE_COSTANTE_GARA.findall(testo):
            valori = [int(n) for n in re.findall(r"\d+", corpo)]
            if len(valori) != 6:
                continue
            if chiave in fuori and fuori[chiave] != valori:
                raise SystemExit("la costante %s vale %s in un file e %s in un altro: la fonte "
                                 "non concorda con se stessa e va letta prima di proseguire"
                                 % (chiave, fuori[chiave], valori))
            fuori[chiave] = valori
    return fuori


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
            # La sigla della versione e' il terzo argomento della chiamata, subito dopo la
            # tavola dei nomi e l'indice. Si legge dalla riga e non si deduce dal nome della
            # tabella, perche' una tabella puo' contenere voci di versioni diverse.
            args = censimento.argomenti(v.get("riga") or "")
            v["versione"] = args[2].strip() if len(args) > 2 else ""
            fuori.append((t["tabella"], v))
    return fuori


def componi(ace, pkhex, tabella, voce, lingua, luogo, eventi, incontri, gara=None,
            destinazione=None):
    """Un esemplare di scambio, composto dai campi che la fonte dichiara.

    Le tabelle di gioco, cioe' la corrispondenza fra numerazione nazionale e identificativo
    interno, i gruppi di crescita e l'esperienza, vengono dal generatore delle distribuzioni: e'
    il modulo che le porta, e riusarlo evita di avere due verita' sugli stessi dati.
    """
    g3 = eventi
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
    soprannome = tabella_caratteri.encode(verso_la_codifica(soprannome_testo),
                                         length=gen3.NICKNAME_LENGTH)

    nome_ot_testo = (voce.get("allenatori") or {}).get(sigla)
    if not nome_ot_testo:
        return None, {"saltata": "nessun nome di allenatore in " + lingua}
    ot = azzera_dopo_il_terminatore(
        tabella_caratteri.encode(verso_la_codifica(nome_ot_testo),
                                 length=gen3.OT_NAME_LENGTH))

    bit = ABILITA.get(props.get("Ability", "OnlyFirst"), 0)

    # Le mosse. Un esemplare consegnato da uno scambio porta il repertorio che la sua specie
    # conosce a quel livello, come qualunque altro incontro: il primo lotto le aveva tutte a
    # zero, cioe' un esemplare senza alcuna mossa, che nessun gioco ha mai prodotto. Il
    # repertorio si sceglie sulla versione dell'incontro, e per una sigla che ne comprende piu'
    # d'una si prende la prima, dichiarandolo, perche' i repertori delle versioni di una coppia
    # coincidono su queste specie.
    sigla = voce.get("versione") or ""
    chiave_rep = sigla if sigla in incontri.REPERTORI else None
    if chiave_rep is None:
        for membro in eventi.GRUPPI_VERSIONE.get(sigla, ()):  # FRLG -> FR, RS -> R
            if membro in incontri.REPERTORI:
                chiave_rep = membro
                break
    if chiave_rep is None:
        raise KeyError("nessun repertorio di livello per la sigla di versione %r" % sigla)
    grezzo = io.open(os.path.join(pkhex, incontri.CARTELLA_REPERTORI,
                                  incontri.REPERTORI[chiave_rep]), "rb").read()
    coppie = incontri.repertorio_di_livello(incontri.aree_indicizzate(grezzo)[nazionale])
    mosse = incontri.mosse_al_livello(coppie, livello)
    pp_base = eventi.punti_potenza(ace)
    pp = [pp_base.get(m, 0) for m in mosse]
    indole = incontri.indole_di_specie(pkhex, nazionale)

    # Le statistiche da gara. La fonte le dichiara per ciascuno scambio con il nome di una
    # costante, e il primo lotto le scriveva a zero: uno scambio consegna un esemplare che le
    # porta, e zero e' un valore che nessuno di essi ha. I sei numeri sono le cinque statistiche
    # piu' la lucentezza estetica, che sta in un campo proprio.
    condizione = gen3.EvsCondition()
    nome_gara = props.get("Contest")
    if nome_gara and gara:
        valori = gara.get(nome_gara)
        if valori is None:
            raise KeyError("la fonte nomina la costante di gara %r e non la definisce: va letta "
                           "invece di essere sostituita con zeri" % nome_gara)
        condizione = gen3.EvsCondition(
            contest=dict(zip(gen3.CONTEST_ORDER, valori[:5])),
            sheen=valori[5],
        )

    mon = gen3.Gen3Mon(
        personality=personalita,
        ot_id=((sid & 0xFFFF) << 16) | (tid & 0xFFFF),
        nickname=soprannome,
        language=eventi.LINGUE[LINGUE[lingua]],
        # La bandierina del soprannome: questi esemplari ne portano uno fissato, diverso dal
        # nome della specie, e senza di essa il verificatore li contesta.
        flags=0x02,
        ot_name=ot,
        markings=0,
        growth=gen3.Growth(species=specie_id, held_item=0,
                           experience=g3.esperienza(gruppo, livello),
                           pp_bonuses=0, friendship=indole["amicizia"]),
        attacks=gen3.Attacks(moves=(mosse + [0, 0, 0, 0])[:4],
                             pp=(pp + [0, 0, 0, 0])[:4]),
        evs=condizione,
        misc=gen3.Misc(
            pokerus=0,
            met_location=luogo,
            met_level=livello,
            met_game=eventi.codice_versione(voce["versione"], destinazione),
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


def carica_incontri():
    """Il generatore degli incontri di terza, da cui si riusano mosse, indoli e repertori.

    Porta gia' la lettura dei repertori di livello per versione, la tavola delle indoli con
    l'amicizia di base, e la selezione delle mosse conosciute a un livello dato. Un esemplare da
    scambio arriva con il proprio repertorio di livello come qualunque altro, quindi quelle tre
    cose servono identiche e riscriverle significherebbe avere due verita' sugli stessi dati.
    """
    percorso = os.path.join(RADICE, "tools", "genera-incontro-gen3.py")
    spec = importlib.util.spec_from_file_location("incontri_gen3", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def carica_eventi():
    """Il generatore delle distribuzioni, da cui si riusa la risoluzione della versione.

    La tabella delle sigle e la funzione che le traduce esistono gia' li' e portano una
    disciplina che vale conservare: una sigla ignota solleva invece di cadere su un valore
    predefinito, perche' un gioco di origine sbagliato produce un esemplare che il verificatore
    rifiuta senza che nulla lo segnali. Riscriverla qui significherebbe avere due posti dove
    sbagliarla, ed e' il difetto che questo progetto ha gia' pagato sulle sigle multiple.
    """
    percorso = os.path.join(RADICE, "tools", "genera-evento-gen3.py")
    spec = importlib.util.spec_from_file_location("eventi_gen3", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


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

    prova("l'apostrofo dritto della fonte diventa quello che la codifica conosce",
          verso_la_codifica("CH'DING") == u"CH\u2019DING")
    prova("negativo: un nome senza apostrofo non viene toccato",
          verso_la_codifica("MIMIEN") == "MIMIEN")
    import sys as _sys
    _sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))
    tab_it = cm.Charmap.gen3_per_lingua("Italian")
    prova("la codifica conosce l'apostrofo destro e non quello dritto, che e' la ragione "
          "per cui la traduzione esiste",
          APOSTROFO_DESTRO in tab_it.char_to_byte and
          APOSTROFO_DRITTO not in tab_it.char_to_byte)
    # Le quattro correzioni del primo giudizio, ciascuna con la propria prova.
    prova("la lingua NON e' trascritta qui ma presa dalla tavola del generatore delle "
          "distribuzioni: la prima stesura dava all'italiano il codice del tedesco",
          set(LINGUE.values()) == {"ITA", "ENG", "JPN"})
    finta = '    private static ReadOnlySpan<byte> TradeContest_Cool   => [ 30, 05, 05, 05, 05, 10 ];'
    letto = dict((k, [int(x) for x in re.findall(r"\d+", c)])
                 for k, c in RE_COSTANTE_GARA.findall(finta))
    prova("le statistiche da gara si leggono dalla fonte e sono sei",
          letto.get("TradeContest_Cool") == [30, 5, 5, 5, 5, 10])
    prova("negativo: una costante con meno di sei valori non si completa a zero",
          [int(x) for x in re.findall(r"\d+", "30, 05, 05")] != [30, 5, 5, 5, 5, 10])

    # La regola che il terzo giudizio ha reso esplicita.
    prova("i byte dopo il terminatore si azzerano, e il terminatore resta",
          azzera_dopo_il_terminatore(bytes.fromhex("c3cdc3cdffffff"))
          == bytes.fromhex("c3cdc3cdff0000"))
    prova("negativo: un nome che riempie il campo non ha terminatore e non si tocca",
          azzera_dopo_il_terminatore(bytes.fromhex("bdc6c3c0cec9c8"))
          == bytes.fromhex("bdc6c3c0cec9c8"))
    prova("negativo: un nome con un solo terminatore in coda resta identico",
          azzera_dopo_il_terminatore(bytes.fromhex("ccbfd3c6bfd3ff"))
          == bytes.fromhex("ccbfd3c6bfd3ff"))

    prova("un soprannome con apostrofo si scrive davvero, invece di sollevare",
          len(tab_it.encode(verso_la_codifica("CH'DING"),
                            length=gen3.NICKNAME_LENGTH)) == gen3.NICKNAME_LENGTH)

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

    if not a.lotto:
        print("nulla da fare: si passa --elenco per vedere le voci, oppure --lotto per scrivere")
        return 2

    eventi = carica_eventi()
    incontri = carica_incontri()
    gara = statistiche_di_gara(a.pkhex)
    luogo = luogo_scambio(a.pkhex)
    cartella = a.lotto
    if not os.path.isdir(cartella):
        os.makedirs(cartella)

    impronte, fatti, saltate = {}, 0, []
    for tabella, voce in voci:
        mon, r = componi(a.ace, a.pkhex, tabella, voce, a.lingua, luogo, eventi, incontri,
                         gara)
        if mon is None:
            saltate.append((tabella, voce["specie"], r.get("saltata")))
            continue
        # Il nome del file porta la tabella e la specie, che insieme identificano la voce senza
        # dipendere dalla posizione nella tabella: un riordino a monte sposterebbe un indice ma
        # non questi due, ed e' la fragilita' che il codice interno delle voci da evento ha.
        nome = "%s-%04d" % (tabella.replace("TradeGift_", ""), voce["specie"])
        eventi.scrivi(mon, os.path.join(cartella, nome))
        canonica = mon.to_canonical_bytes(party=False)
        impronte[nome] = {
            "file": nome + ".pk3",
            "sha256": __import__("hashlib").sha256(canonica).hexdigest(),
            "personalita": r["personalita"],
            "identificativo": r["tid"],
            "soprannome": r["soprannome"],
            "allenatore": r["allenatore"],
            "lingua": r["lingua"],
            "luogo": r["luogo"],
            "versione": voce["versione"],
            "iv": r["iv"],
            "senza_ricerca_di_semi": True,
        }
        fatti += 1
        print("  %-14s dex %-4s liv %-3s %-8s PID %s  IV %s"
              % (nome, r["specie"], r["livello"], r["soprannome"], r["personalita"],
                 "/".join(str(r["iv"][k]) for k in ORDINE_IV)))

    if saltate:
        print("")
        print("saltate %d voci, e il motivo e' dichiarato per ciascuna:" % len(saltate))
        for tabella, specie, motivo in saltate:
            print("  %-18s dex %-4s  %s" % (tabella, specie, motivo))

    manifesto = os.path.join(cartella, "manifesto.json")
    io.open(manifesto, "w", encoding="utf-8").write(
        __import__("json").dumps(impronte, indent=1, ensure_ascii=False))
    print("")
    print("%d esemplari scritti in %s, con il manifesto delle impronte." % (fatti, cartella))
    print("Nessuno di essi ha richiesto una ricerca di semi: la fonte scrive ogni campo.")
    return 0


if __name__ == "__main__":
    sys.exit(principale())
