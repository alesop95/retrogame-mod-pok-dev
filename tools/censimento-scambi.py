#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Censisce gli scambi in gioco di tutte le generazioni, dalle tabelle del verificatore.

Perche' questa classe merita un censimento proprio
--------------------------------------------------
Un esemplare da scambio in gioco e' consegnato da un personaggio in cambio di un altro, e porta
l'allenatore di chi lo ha allevato, di norma un soprannome fissato, e in molte generazioni un
valore di personalita' e dei valori individuali scritti nel gioco. Ne segue che non e'
riproducibile da una cattura propria: e' un collezionabile distinto anche quando la sua specie e'
coperta altrove, per la stessa ragione per cui lo e' un esemplare da distribuzione. La classe era
nominata da due enumerazioni della comunita' lette il 2026-09-08 e non era mai stata contata sulla
fonte di primo livello, che sono le tabelle del verificatore.

Come la fonte tiene questi dati, e perche' il conto non e' una somma
--------------------------------------------------------------------
Ogni titolo ha una o piu' tabelle, e le tabelle di una coppia di titoli si sovrappongono per
costruzione: c'e' una tabella comune alla coppia e, accanto, una tabella per ciascuna versione con
le voci che quella versione ha in piu' o in forma diversa. Sommare le lunghezze darebbe quindi un
totale gonfiato. Il programma riferisce entrambi i numeri, cioe' le voci di tabella e le voci
distinte, e la deduplicazione e' dichiarata: due voci sono la stessa quando concordano su specie,
livello e identificativo dell'allenatore.

Il presidio, che e' lo stesso della famiglia
--------------------------------------------
La posizione della specie e del livello dentro la chiamata cambia da una generazione all'altra, e
dedurla a occhio e' il modo di sbagliare senza accorgersene. Le posizioni sono quindi dichiarate in
una tabella dentro questo programma, ricavate una per una dalle firme dei costruttori della fonte
e non indovinate, e ogni voce viene comunque confrontata con il commento che la fonte le scrive
accanto, che nomina la specie in inglese: se il numero e il nome non concordano, il programma lo
riferisce come discordanza invece di scrivere un censimento che sembrerebbe verificato.

Che cosa questo programma non fa
--------------------------------
Non produce alcun esemplare, non giudica alcuna legittimita' e non decide se una voce entri
nell'obiettivo di collezione. Dichiara pero' un dato che serve a quella decisione, cioe' se la voce
porti un valore di personalita' fissato nella fonte: dove c'e', l'esemplare e' riproducibile byte
per byte senza alcuna ricerca di semi; dove manca, la fedelta' va discussa come per le altre classi.

Uso
---
    python tools/censimento-scambi.py --pkhex _notes/fonti/pkhex
    python tools/censimento-scambi.py --pkhex _notes/fonti/pkhex --check
    python tools/censimento-scambi.py --self-test
"""

import argparse
import io
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATI = os.path.join("PKHeX.Core", "Legality", "Encounters", "Data")
NOMI_EN = os.path.join("PKHeX.Core", "Resources", "text", "other", "en", "text_Species_en.txt")
NOMI_IT = os.path.join("PKHeX.Core", "Resources", "text", "other", "it", "text_Species_it.txt")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "CENSIMENTO-SCAMBI.md")
NORMALIZZATO = os.path.join(RADICE, "pokedex-home-completo", "scambi.csv")

# Le posizioni della specie e del livello dentro la chiamata, per tipo di voce, ricavate dalle
# firme dei costruttori sotto `Legality/Encounters/Templates`. Il valore None dice che il dato non
# sta fra gli argomenti ma fra le proprieta' scritte dopo la graffa, dove si legge per nome.
#
#   EncounterTrade1(names, index, species, version, levelRBY [, levelGSC])
#   EncounterTrade2(names, index, species, level, tid16)
#   EncounterTrade3(names, index, version, pid, species, level)
#   EncounterTrade3XD(species, level, trainer [, nicknames])
#   EncounterTrade4PID(names, index, version, pid, species, level)
#   EncounterTrade4RanchGift(pid, species, met, level) oppure (species, met, level)
#   EncounterTrade8(names, index, version, species, level, memory, arg, feel, intensity)
#   EncounterTrade9(names, index, version, species, level)
#   EncounterTrade9a(names, index, species, form, level)
POSIZIONI = {
    "EncounterTrade1": (2, 4),
    "EncounterTrade2": (2, 3),
    "EncounterTrade3": (4, 5),
    "EncounterTrade3XD": (0, 1),
    "EncounterTrade4PID": (4, 5),
    "EncounterTrade4RanchGift": ("ranch", "ranch"),
    "EncounterTrade5BW": (None, None),
    "EncounterTrade5B2W2": (None, None),
    "EncounterTrade6": (None, None),
    "EncounterTrade7": (None, None),
    "EncounterTrade7b": (None, None),
    # L'ottava generazione ha due costruttori e la fonte li usa entrambi nella medesima tabella:
    # uno prende la tavola dei nomi con l'indice della voce, l'altro prende direttamente i nomi
    # dell'allenatore e non ha indice, quindi la specie scorre di una posizione. Si distinguono
    # contando gli argomenti, ed e' la ragione per cui questa voce e' un dizionario per arieta'
    # invece di una coppia: senza la distinzione sette voci su quattordici uscivano con la specie
    # di un'altra, e il presidio sul commento lo ha rilevato.
    "EncounterTrade8": {9: (3, 4), 8: (2, 3)},
    "EncounterTrade8b": (None, None),
    "EncounterTrade9": (3, 4),
    "EncounterTrade9a": (2, 4),
}

# La generazione di ciascuna cartella della fonte, che e' anche l'ordine in cui il censimento
# presenta i titoli.
GENERAZIONI = ("Gen1", "Gen2", "Gen3", "Gen4", "Gen5", "Gen6", "Gen7", "Gen8", "Gen9")

MAX_SPECIE = 1025


def nomi_specie(percorso):
    """I nomi delle specie per numero nazionale, con l'indice zero occupato dalla parola uovo."""
    if not os.path.exists(percorso):
        return None
    righe = io.open(percorso, encoding="utf-8").read().split("\n")
    return [r.strip() for r in righe]


def argomenti(chiamata):
    """Gli argomenti di primo livello di una chiamata, senza entrare nelle parentesi annidate."""
    fuori, corrente, profondita = [], "", 0
    for c in chiamata:
        if c == "(":
            profondita += 1
            if profondita == 1:
                # Alla parentesi che apre la chiamata si butta cio' che la precede, cioe' la parola
                # `new`: senza questo azzeramento il primo argomento uscirebbe attaccato a essa e
                # ogni lettura per posizione sarebbe sfasata di un carattere invece che di un
                # campo, che e' il genere di difetto che non produce un errore ma un numero falso.
                corrente = ""
                continue
        elif c == ")":
            profondita -= 1
            if profondita == 0:
                break
        if profondita == 1 and c == ",":
            fuori.append(corrente.strip())
            corrente = ""
        else:
            corrente += c
    if corrente.strip():
        fuori.append(corrente.strip())
    return fuori


def numero(testo):
    """Un argomento come intero, se lo e': accetta il decimale con gli zeri davanti e l'esadecimale."""
    testo = testo.strip()
    if re.fullmatch(r"0[xX][0-9a-fA-F]+", testo):
        return int(testo, 16)
    if re.fullmatch(r"\d+", testo):
        return int(testo)
    return None


def proprieta(voce):
    """Le proprieta' scritte fra graffe dopo la chiamata, come dizionario di stringhe."""
    m = re.search(r"\{(.*)\}", voce, re.S)
    if not m:
        return {}
    fuori = {}
    for coppia in re.finditer(r"(\w+)\s*=\s*([^,{}]+(?:\([^()]*\))?)", m.group(1)):
        fuori[coppia.group(1)] = coppia.group(2).strip()
    return fuori


def tabelle(testo):
    """Le tabelle di scambi di un file, come terne fra tipo, nome e voci grezze.

    Il ritaglio tollera un commento fra il segno di uguale e la parentesi quadra, che nella fonte
    compare su almeno una tabella e che una lettura ingenua farebbe perdere in silenzio.
    """
    fuori = []
    for m in re.finditer(r"readonly\s+(\w*Trade\w*)\[\]\s+(\w+)\s*=\s*(?://[^\n]*\n\s*)?\[(.*?)\n\s*\];",
                         testo, re.S):
        tipo, nome, corpo = m.group(1), m.group(2), m.group(3)
        voci = []
        for riga in corpo.split("\n"):
            riga = riga.strip()
            if riga.startswith("new("):
                voci.append(riga)
        if voci:
            fuori.append((tipo, nome, voci))
    return fuori


def leggi_voce(tipo, riga, nomi_en):
    """Una voce di tabella come dizionario, con la discordanza dichiarata se il commento smentisce."""
    args = argomenti(riga)
    props = proprieta(riga)
    commento = ""
    m = re.search(r"//\s*(.*)$", riga)
    if m:
        commento = m.group(1).strip()

    dichiarate = POSIZIONI.get(tipo, (None, None))
    if isinstance(dichiarate, dict):
        dichiarate = dichiarate.get(len(args), (None, None))
    pos_specie, pos_livello = dichiarate
    specie = livello = None
    if pos_specie == "ranch":
        # I due costruttori del ranch differiscono per il valore di personalita' iniziale, e si
        # distinguono contando gli argomenti invece che indovinando.
        numeri = [numero(a) for a in args]
        numeri = [n for n in numeri if n is not None]
        if len(numeri) >= 4:
            specie, livello = numeri[1], numeri[3]
        elif len(numeri) == 3:
            specie, livello = numeri[0], numeri[2]
    else:
        if pos_specie is not None and pos_specie < len(args):
            specie = numero(args[pos_specie])
        if pos_livello is not None and pos_livello < len(args):
            livello = numero(args[pos_livello])
    if specie is None and "Species" in props:
        specie = numero(props["Species"])
    if livello is None and "Level" in props:
        livello = numero(props["Level"])

    pid = None
    for chiave in ("PID",):
        if chiave in props:
            pid = props[chiave]
    if pid is None:
        for a in args:
            if re.fullmatch(r"0[xX][0-9a-fA-F]{6,8}", a.strip()):
                pid = a.strip()
                break

    identificativo = ""
    for chiave in ("ID32", "TID16"):
        if chiave in props:
            identificativo = props[chiave]
            break

    discordanza = ""
    if specie is not None and nomi_en and 0 < specie < len(nomi_en) and commento:
        # L'apostrofo va normalizzato prima del confronto: la tavola dei nomi scrive Farfetch con
        # l'apostrofo tipografico e i commenti della fonte con quello dritto, e senza questa
        # normalizzazione due scritture della stessa specie risultano discordanti.
        def piano(s):
            return s.lower().replace(u"’", "'").replace(u"ʼ", "'")

        atteso = nomi_en[specie]
        # Il commento apre col nome della specie ricevuta, seguito da un separatore: basta quindi
        # controllare che il nome atteso compaia, non che il commento sia uguale a esso.
        if atteso and piano(atteso) not in piano(commento):
            discordanza = "il commento dice %r e il numero %d vale %s" % (commento[:60], specie, atteso)
    return {
        "specie": specie,
        "livello": livello,
        "pid": pid or "",
        "identificativo": identificativo,
        "forma": props.get("Form", ""),
        "luogo": props.get("Location", ""),
        "commento": commento,
        "discordanza": discordanza,
    }


def censisci(pkhex, nomi_en):
    """Tutte le tabelle di scambio della fonte, in ordine di generazione."""
    fuori = []
    base = os.path.join(pkhex, DATI)
    if not os.path.isdir(base):
        return None
    for gen in GENERAZIONI:
        cartella = os.path.join(base, gen)
        if not os.path.isdir(cartella):
            continue
        for nome_file in sorted(os.listdir(cartella)):
            if not nome_file.endswith(".cs"):
                continue
            testo = io.open(os.path.join(cartella, nome_file), encoding="utf-8",
                            errors="replace").read()
            for tipo, nome, righe in tabelle(testo):
                voci = [leggi_voce(tipo, r, nomi_en) for r in righe]
                fuori.append({
                    "generazione": gen.replace("Gen", ""),
                    "file": nome_file,
                    "tipo": tipo,
                    "tabella": nome,
                    "voci": voci,
                    "ignoto": tipo not in POSIZIONI,
                })
    return fuori


def chiave(v):
    """L'identita' di una voce ai fini della deduplicazione, dichiarata invece che implicita."""
    return (v["specie"], v["livello"], v["identificativo"], v["forma"])


def componi(tabelle_lette, nomi_it):
    r = ["# Censimento degli scambi in gioco, tutte le generazioni", ""]
    r.append("> Documento generato da `tools/censimento-scambi.py` dalle tabelle del verificatore. Non si modifica a mano: si rigenera. Enumera la classe degli esemplari consegnati da un personaggio in cambio di un altro, che portano allenatore e soprannome altrui e non sono riproducibili da una cattura propria.")
    r.append("")
    totale = sum(len(t["voci"]) for t in tabelle_lette)
    distinte = len({chiave(v) for t in tabelle_lette for v in t["voci"]})
    con_pid = sum(1 for t in tabelle_lette for v in t["voci"] if v["pid"])
    specie = {v["specie"] for t in tabelle_lette for v in t["voci"] if v["specie"]}
    r.append("Le voci di tabella sono %d e quelle distinte %d, su %d specie diverse. I due numeri differiscono perche' le tabelle di una coppia di titoli si sovrappongono per costruzione: c'e' una tabella comune e accanto una tabella per versione, e la stessa voce compare in entrambe. Due voci sono contate come una quando concordano su specie, livello, identificativo dell'allenatore e forma."
             % (totale, distinte, len(specie)))
    r.append("")
    r.append("Di %d voci la fonte scrive il valore di personalita', quindi quegli esemplari sono riproducibili byte per byte senza alcuna ricerca di semi. Sulle altre la fedelta' va discussa come per le altre classi, perche' il valore lo genera il gioco al momento della consegna."
             % con_pid)
    r.append("")
    discordanze = [(t, v) for t in tabelle_lette for v in t["voci"] if v["discordanza"]]
    ignote = [t for t in tabelle_lette if t["ignoto"]]
    r.append("Controlli: %s %s"
             % ("nessuna voce discorda dal commento che la fonte le scrive accanto."
                if not discordanze else
                "%d voci discordano dal commento e sono elencate in coda; il censimento non va usato come misura finche' non sono risolte." % len(discordanze),
                "Tutti i tipi di voce hanno le posizioni dichiarate."
                if not ignote else
                "ATTENZIONE: %d tabelle hanno un tipo che questo programma non conosce, e le loro voci sono lette solo dalle proprieta'." % len(ignote)))
    r.append("")

    for gen in GENERAZIONI:
        sigla = gen.replace("Gen", "")
        gruppo = [t for t in tabelle_lette if t["generazione"] == sigla]
        if not gruppo:
            continue
        r.append("## Generazione %s" % sigla)
        r.append("")
        for t in gruppo:
            r.append("### %s, da `%s`" % (t["tabella"], t["file"]))
            r.append("")
            r.append("Tipo di voce `%s`, %d voci." % (t["tipo"], len(t["voci"])))
            r.append("")
            r.append("| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |")
            r.append("|---|---|---|---|---|---|")
            for v in t["voci"]:
                nome = "?"
                if v["specie"] and nomi_it and v["specie"] < len(nomi_it):
                    nome = nomi_it[v["specie"]]
                r.append("| %s | %s | %s | %s | %s | %s |"
                         % (nome,
                            v["specie"] if v["specie"] is not None else "?",
                            v["livello"] if v["livello"] is not None else "?",
                            v["pid"] or "-",
                            v["identificativo"] or "-",
                            (v["commento"] or "-").replace("|", "/")[:120]))
            r.append("")

    if discordanze:
        r.append("## Discordanze fra numero e commento")
        r.append("")
        r.append("| Tabella | Discordanza |")
        r.append("|---|---|")
        for t, v in discordanze:
            r.append("| %s | %s |" % (t["tabella"], v["discordanza"].replace("|", "/")))
        r.append("")
    return "\n".join(r) + "\n"


def normalizza(tabelle_lette, nomi_it):
    r = ["generazione,tabella,tipo,dex,specie,livello,pid,identificativo,forma,luogo,nota"]
    for t in tabelle_lette:
        for v in t["voci"]:
            nome = nomi_it[v["specie"]] if (v["specie"] and nomi_it and v["specie"] < len(nomi_it)) else ""
            campi = [t["generazione"], t["tabella"], t["tipo"],
                     str(v["specie"] if v["specie"] is not None else ""), nome,
                     str(v["livello"] if v["livello"] is not None else ""),
                     v["pid"], v["identificativo"], v["forma"], v["luogo"], v["commento"]]
            r.append(",".join('"%s"' % c.replace('"', '""') if ("," in c or '"' in c) else c
                              for c in campi))
    return "\n".join(r) + "\n"


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("gli argomenti non entrano nelle parentesi annidate",
          ["TradeNames", "00", "RS", "0x00009C40", "296", "05"],
          argomenti("new(TradeNames, 00, RS, 0x00009C40, 296, 05) { IVs = new(5,5,4,4,4,4) }"))
    prova("un numero decimale con gli zeri davanti", 5, numero("05"))
    prova("un numero esadecimale", 0x8E, numero("0x0000008E"))
    prova("un argomento che non e' un numero", None, numero("TradeNames"))

    props = proprieta("new(TradeNames, 00, SV, 0194, 18) { ID32 = 033081, Nature = Nature.Relaxed }")
    prova("le proprieta' si leggono per nome", "033081", props.get("ID32"))
    prova("e i valori con il punto restano interi", "Nature.Relaxed", props.get("Nature"))

    nomi = [""] * 1026
    nomi[296], nomi[194], nomi[63] = "Makuhita", "Wooper", "Abra"

    # Terza generazione: la specie sta in quarta posizione e il livello in quinta.
    v = leggi_voce("EncounterTrade3",
                   "new(TradeNames, 00, RS, 0x00009C40, 296, 05) { TID16 = 49562 }, // Makuhita",
                   nomi)
    prova("la specie di terza generazione", 296, v["specie"])
    prova("il livello di terza generazione", 5, v["livello"])
    prova("il valore di personalita' viene riconosciuto", "0x00009C40", v["pid"])
    prova("l'identificativo viene riconosciuto", "49562", v["identificativo"])
    prova("e non c'e' discordanza", "", v["discordanza"])

    # Nona generazione: la specie sta in terza posizione, e il commento la conferma.
    v = leggi_voce("EncounterTrade9",
                   "new(TradeNames, 00, SV, 0194, 18) { ID32 = 033081 }, // Wooper", nomi)
    prova("la specie di nona generazione", 194, v["specie"])
    prova("il livello di nona generazione", 18, v["livello"])

    # Controllo negativo: se il numero e il commento dicono due specie diverse, si dichiara.
    v = leggi_voce("EncounterTrade9",
                   "new(TradeNames, 00, SV, 0194, 18) { ID32 = 033081 }, // Abra", nomi)
    prova("la discordanza viene dichiarata", True, v["discordanza"] != "")

    # Quinta generazione: specie e livello stanno fra le proprieta' e non fra gli argomenti.
    v = leggi_voce("EncounterTrade5B2W2",
                   "new(TradeNames, 00, B2  ) { Species = 296, Level = 20, ID32 = 65217 },", nomi)
    prova("la specie dalle proprieta'", 296, v["specie"])
    prova("il livello dalle proprieta'", 20, v["livello"])

    # L'ottava generazione usa due costruttori nella stessa tabella, e la specie scorre di una
    # posizione fra l'uno e l'altro: e' il difetto che il presidio sul commento ha rilevato, e
    # queste due prove lo tengono chiuso.
    nomi[52], nomi[110] = "Meowth", "Weezing"
    v = leggi_voce("EncounterTrade8",
                   "new(TradeNames, 00, SWSH, 052,18,08,000,04,5) { ID32 = 263455 }, // Meowth",
                   nomi)
    prova("l'ottava con indice", 52, v["specie"])
    prova("e il suo livello", 18, v["livello"])
    v = leggi_voce("EncounterTrade8",
                   "new(TradeOT_R1, SWSH, 110,15,01,040,12,2) { ID32 = 101141 }, // Weezing", nomi)
    prova("l'ottava senza indice", 110, v["specie"])
    prova("e il suo livello", 15, v["livello"])

    # L'apostrofo tipografico della tavola dei nomi non deve produrre una falsa discordanza.
    nomi[83] = u"Farfetch’d"
    v = leggi_voce("EncounterTrade2",
                   "new(TradeNames, 5, 083, 02, 15616) { Gender = 0 }, // Farfetch'd", nomi)
    prova("l'apostrofo non produce discordanza", "", v["discordanza"])

    # I due costruttori del ranch si distinguono contando gli argomenti.
    v = leggi_voce("EncounterTrade4RanchGift",
                   "new(323975838, 025, 18, 20) { Location = 0068 }, // Pikachu", nomi)
    prova("il ranch con il valore di personalita'", 25, v["specie"])
    prova("e il suo livello", 20, v["livello"])
    v = leggi_voce("EncounterTrade4RanchGift", "new(025, 18, 20) { Location = 0068 }, // Pikachu",
                   nomi)
    prova("il ranch senza il valore di personalita'", 25, v["specie"])
    prova("e il suo livello", 20, v["livello"])

    # Il ritaglio delle tabelle tollera un commento fra l'uguale e la parentesi quadra: senza
    # questa tolleranza la tabella della settima generazione veniva perduta in silenzio.
    testo = ("    internal static readonly EncounterTrade7[] TradeGift_SM = // @ a\\1\\5\\5\n"
             "    [\n"
             "        new(TradeNames, 00, SM) { Species = 066, Level = 09 }, // Machop\n"
             "    ];\n")
    trovate = tabelle(testo)
    prova("la tabella col commento viene trovata", 1, len(trovate))
    prova("e porta la sua voce", 1, len(trovate[0][2]))

    prova("la chiave di deduplicazione", (296, 5, "49562", ""),
          chiave({"specie": 296, "livello": 5, "identificativo": "49562", "forma": ""}))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "pkhex"),
                    help="il clone del verificatore da cui leggere le tabelle")
    ap.add_argument("--check", action="store_true",
                    help="non scrive: dice soltanto se i documenti sul disco siano allineati")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    pkhex = a.pkhex if os.path.isabs(a.pkhex) else os.path.join(RADICE, a.pkhex)
    nomi_en = nomi_specie(os.path.join(pkhex, NOMI_EN))
    nomi_it = nomi_specie(os.path.join(pkhex, NOMI_IT))
    if nomi_en is None or nomi_it is None:
        print("rifiutato: mancano i nomi delle specie sotto " + pkhex)
        return 1
    lette = censisci(pkhex, nomi_en)
    if lette is None:
        print("rifiutato: manca la cartella delle tabelle sotto " + pkhex)
        return 1

    testo = componi(lette, nomi_it)
    csv = normalizza(lette, nomi_it)
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
    totale = sum(len(t["voci"]) for t in lette)
    distinte = len({chiave(v) for t in lette for v in t["voci"]})
    con_pid = sum(1 for t in lette for v in t["voci"] if v["pid"])
    discordanze = [v for t in lette for v in t["voci"] if v["discordanza"]]
    print("scritti %s e %s" % (USCITA, NORMALIZZATO))
    print("  tabelle %d | voci %d | distinte %d | con valore di personalita' %d"
          % (len(lette), totale, distinte, con_pid))
    for t in lette:
        if t["ignoto"]:
            print("  TIPO IGNOTO: %s in %s" % (t["tipo"], t["file"]))
    for v in discordanze:
        print("  DISCORDANZA: " + v["discordanza"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
