#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone gli esemplari di quarta generazione che un oggetto sbloccava, e che nessuno consegnava.

Perché esiste
-------------
È la seconda metà della direttiva dell'utente del 2026-09-08: il progetto deve saper generare
qualunque esemplare che in qualunque generazione si otteneva con un oggetto che sbloccava un
luogo, e non con una consegna diretta. La terza generazione è fatta e conforme su quattordici
voci; questa è la quarta.

La ragione per cui questa classe non era stata vista prima merita di essere ripetuta, perché è
strutturale e non distrazione: nella base dei doni segreti queste voci non ci sono, perché ciò
che la carta consegnava era l'oggetto e non l'esemplare. Sono invisibili a chiunque enumeri
partendo dalle carte, ed è la stessa cecità per costruzione già misurata in ADR-044.

Che cosa cambia rispetto alla terza generazione, e che cosa no
--------------------------------------------------------------
Non cambia la parte difficile. Gli incontri statici di quarta generazione richiedono la
correlazione del primo metodo, cioè la stessa della terza: quattro estrazioni consecutive dal
generatore lineare, le prime due che compongono il valore di personalità e le altre due i valori
individuali. Il ramo è quindi quello già scritto e già giudicato conforme, e questo programma lo
carica dal suo fratello di terza invece di riscriverlo.

Cambia tutto il resto, perché il formato è un altro. La struttura è cifrata e permutata secondo il
valore di personalità, porta una somma di controllo, e tiene il luogo di incontro in due campi
distinti secondo il gioco che lo scriverà. Porta inoltre un campo che la terza generazione non
aveva e che qui non si può lasciare a zero: il tipo di terreno su cui l'incontro è avvenuto, che
il verificatore controlla contro quello che la propria tabella dichiara per quell'incontro.

Un esemplare che non si può produrre, e perché si registra invece di tacerlo
----------------------------------------------------------------------------
Il flauto azzurro sbloccava la sala d'origine e con essa Arceus, e le tabelle del verificatore
non portano alcuna voce per quell'incontro. Non è una lacuna della tabella: quel flauto non fu
mai distribuito ufficialmente in alcuna regione, quindi non esiste alcun Arceus di quella
provenienza che sia conforme, e comporne uno significherebbe produrre un esemplare che il
verificatore rifiuterà sempre. La voce va quindi in coda d'attesa secondo ADR-046, e questo
programma la nomina invece di ometterla, perché una voce omessa in silenzio è indistinguibile da
una dimenticata.

Uso
---
    python tools/genera-incontro-gen4.py --elenco
    python tools/genera-incontro-gen4.py --lotto _notes/lotto-incontri-gen4
    python tools/genera-incontro-gen4.py --self-test
"""

import argparse
import hashlib
import importlib.util
import io
import json
import os
import struct
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

G4 = None   # il generatore dei doni di quarta, per gli scostamenti e la somma di controllo
I3 = None   # il generatore degli incontri di terza, per il primo metodo


def _modulo(nome_file, alias):
    percorso = os.path.join(RADICE, "tools", nome_file)
    spec = importlib.util.spec_from_file_location(alias, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


# ---------------------------------------------------------------------------------------
# La tavola degli incontri sbloccati da un oggetto, letta dalle tabelle del verificatore.
# ---------------------------------------------------------------------------------------

# Schema: sigla, numero nazionale, livello, versione, luogo, fatidico, tipo di terreno, oggetto
# che lo sbloccava, e il nome umano del luogo. Il tipo di terreno e' l'indice del bit piu' basso
# acceso nella maschera che la tabella dichiara, che e' la regola del verificatore e non una
# nostra convenzione: la maschera dice quali terreni siano ammessi, e l'indice scelto e' il primo.
#
# Fonte: PKHeX, `PKHeX.Core/Legality/Encounters/Data/Gen4/Encounters4DPPt.cs` righe 93 e 94 per i
# due dell'oggetto e riga 89 per quello della condizione, lette il 2026-09-08.
INCONTRI = [
    ("darkrai-pt", 491, 50, "pt", 79, False, 2,
     "Carta Iscrizione", "Isola Nuovaluna"),
    ("shaymin-pt", 492, 30, "pt", 63, True, 0,
     "Lettera del Professore", "Giardinfiore"),
    # Non lo sblocca un oggetto ma una condizione, cioe' il possesso dei tre golem regionali
    # portati dalla terza generazione. Sta qui perche' appartiene alla stessa famiglia, cioe' gli
    # esemplari che un evento rende raggiungibili senza consegnarli, ed e' distinto nella colonna
    # della chiave. Il suo livello uno esiste soltanto in Platino: negli altri giochi con questo
    # evento lo stesso esemplare e' al settanta.
    ("regigigas-pt", 486, 1, "pt", 64, False, 5,
     "possesso dei tre golem", "Tempio Nevepoli"),
]

# La voce che non si puo' produrre, nominata perche' una voce omessa in silenzio e'
# indistinguibile da una dimenticata.
NON_PRODUCIBILI = [
    ("arceus-sala-origine", 493, "Flauto Azzurro", "Sala Origine",
     "le tabelle del verificatore non portano alcuna voce per questo incontro, perche' il flauto "
     "non fu mai distribuito ufficialmente in alcuna regione. Un esemplare composto per questa "
     "provenienza sarebbe rifiutato sempre. Va in coda d'attesa secondo ADR-046. Il progetto "
     "possiede comunque nove Arceus da distribuzione nel lotto di quarta generazione, che sono "
     "un'altra provenienza e non un ripiego"),
]

VERSIONI = {"d": 10, "p": 11, "pt": 12, "hg": 7, "ss": 8}
REPERTORI = {"pt": "lvlmove_pt.pkl", "d": "lvlmove_dp.pkl", "p": "lvlmove_dp.pkl",
             "hg": "lvlmove_hgss.pkl", "ss": "lvlmove_hgss.pkl"}

# La tabella personale che il modello del verificatore impiega per questi incontri e' quella
# delle riedizioni di seconda generazione, e vale per tutti i giochi di quarta: e' una scelta
# sua, si copia e non si ricalcola su una tabella diversa.
PERSONALE = "personal_hgss"
DIM_PERSONALE = 0x2C
OFF_P_GENERE = 0x10
OFF_P_CORDIALITA = 0x12
OFF_P_CRESCITA = 0x13
OFF_P_ABILITA1 = 0x16
OFF_P_ABILITA2 = 0x17

CARTELLA_REPERTORI = os.path.join("PKHeX.Core", "Resources", "byte", "levelup")
CARTELLA_PERSONALI = os.path.join("PKHeX.Core", "Resources", "byte", "personal")
TESTI = os.path.join("PKHeX.Core", "Resources", "text", "other", "en")

SALE = "INC-4|2026-09-08"
DATA_INCONTRO = (2026, 9, 8)
LINGUA = 4          # italiano, la lingua dell'allenatore del progetto
PALLA = 4           # Poke Ball, che il modello assegna quando l'incontro non ne fissa una


def seme_della_voce(sigla, tid, sid, giro):
    chiave = "%s|%s|%d|%d|%d" % (SALE, sigla, tid, sid, giro)
    return struct.unpack("<I", hashlib.sha256(chiave.encode("utf-8")).digest()[:4])[0]


def voce_personale(pkhex, nazionale):
    dati = io.open(os.path.join(pkhex, CARTELLA_PERSONALI, PERSONALE), "rb").read()
    inizio = nazionale * DIM_PERSONALE
    blocco = dati[inizio:inizio + DIM_PERSONALE]
    if len(blocco) < DIM_PERSONALE:
        raise KeyError("numero nazionale fuori dalla tabella personale: %d" % nazionale)
    return blocco


def esperienza(gruppo, livello):
    """L'esperienza totale per un livello, con le formule gia' verificate dal fratello di terza."""
    return I3.G3.esperienza(gruppo, livello)


def mosse_al_livello(pkhex, versione, nazionale, livello):
    grezzo = io.open(os.path.join(pkhex, CARTELLA_REPERTORI, REPERTORI[versione]), "rb").read()
    area = I3.aree_indicizzate(grezzo)[nazionale]
    return I3.mosse_al_livello(I3.repertorio_di_livello(area), livello)


def nome_specie(pkhex, nazionale):
    """Il nome della specie nella lingua dell'esemplare, che e' il soprannome di chi non ne ha uno.

    La quarta generazione conserva i nomi in una tabella per lingua, e per l'italiano il nome e'
    quello inglese salvo poche specie: il progetto usa la tabella italiana del verificatore
    quando c'e', e altrimenti dichiara di ripiegare su quella inglese invece di tacerlo.
    """
    for cartella, quale in ((os.path.join("PKHeX.Core", "Resources", "text", "other", "it"),
                             "text_Species_it.txt"),
                            (TESTI, "text_Species_en.txt")):
        percorso = os.path.join(pkhex, cartella, quale)
        if os.path.exists(percorso):
            righe = io.open(percorso, encoding="utf-8-sig").read().splitlines()
            if nazionale < len(righe) and righe[nazionale].strip():
                return righe[nazionale].strip(), quale
    raise KeyError("nome di specie assente per il numero nazionale %d" % nazionale)


def codifica_nome(testo, caratteri):
    """Il nome nella codifica a sedici bit della quarta generazione, con il terminatore.

    Il formato tiene i nomi come parole a sedici bit e non come byte, e chiude con la parola
    0xFFFF. Il riempimento oltre il terminatore resta a zero, che e' cio' che il gioco lascia.
    """
    fuori = bytearray()
    for ch in testo:
        codice = caratteri.get(ch)
        if codice is None:
            raise KeyError("carattere %r non presente nella tabella della quarta generazione" % ch)
        fuori += struct.pack("<H", codice)
    fuori += struct.pack("<H", 0xFFFF)
    return bytes(fuori)


def componi(pkhex, voce, allenatore, caratteri, giro=0):
    sigla, nazionale, livello, versione, luogo, fatidico, terreno, oggetto, nome_luogo = voce
    personale = voce_personale(pkhex, nazionale)
    rapporto = personale[OFF_P_GENERE]
    ab1, ab2 = personale[OFF_P_ABILITA1], personale[OFF_P_ABILITA2]

    seme = seme_della_voce(sigla, allenatore["tid"], allenatore["sid"], giro)
    pid, iv, _ = I3.primo_metodo(seme)

    pk4 = bytearray(G4.DIM_PK4_SCATOLA)
    struct.pack_into("<I", pk4, G4.OFF_PID, pid)
    struct.pack_into("<H", pk4, G4.OFF_SANITA, 0)
    struct.pack_into("<H", pk4, G4.OFF_SPECIE, nazionale)
    struct.pack_into("<H", pk4, G4.OFF_TID, allenatore["tid"] & 0xFFFF)
    struct.pack_into("<H", pk4, G4.OFF_SID, allenatore["sid"] & 0xFFFF)
    struct.pack_into("<I", pk4, G4.OFF_ESPERIENZA,
                     esperienza(personale[OFF_P_CRESCITA], livello))
    pk4[G4.OFF_CORDIALITA] = personale[OFF_P_CORDIALITA]
    # Il bit dell'abilita' segue il valore di personalita' soltanto quando le due caselle
    # differiscono; se portano la medesima abilita' il bit resta a zero, che e' la regola gia'
    # pagata sul lotto di terza generazione il 2026-09-02.
    bit = 0 if ab1 == ab2 else (pid & 1)
    pk4[G4.OFF_ABILITA] = ab2 if bit else ab1
    pk4[G4.OFF_LINGUA] = LINGUA

    iv32 = 0
    for i, chiave in enumerate(("hp", "atk", "def", "spd", "satk", "sdef")):
        iv32 |= (iv[chiave] & 0x1F) << (5 * i)
    if bit:
        iv32 |= 1 << 31
    struct.pack_into("<I", pk4, G4.OFF_IV32, iv32)

    genere = genere_da_pid(pid, rapporto)
    pk4[G4.OFF_FLAG_GENERE] = (1 if fatidico else 0) | (genere << 1)

    struct.pack_into("<H", pk4, G4.OFF_INCONTRO_DP, luogo)
    struct.pack_into("<H", pk4, G4.OFF_INCONTRO_ESTESO, luogo)
    struct.pack_into("<H", pk4, G4.OFF_UOVO_DP, 0)
    struct.pack_into("<H", pk4, G4.OFF_UOVO_ESTESO, 0)
    anno, mese, giorno = DATA_INCONTRO
    pk4[G4.OFF_INCONTRO_ANNO] = (anno - 2000) & 0xFF
    pk4[G4.OFF_INCONTRO_ANNO + 1] = mese
    pk4[G4.OFF_INCONTRO_ANNO + 2] = giorno
    pk4[G4.OFF_VERSIONE] = VERSIONI[versione]
    pk4[G4.OFF_PALLA_DPPT] = PALLA
    pk4[G4.OFF_LIVELLO_INCONTRO] = livello
    pk4[G4.OFF_TIPO_INCONTRO] = terreno

    nome, tabella_usata = nome_specie(pkhex, nazionale)
    soprannome = codifica_nome(nome.upper(), caratteri)
    pk4[0x48:0x48 + len(soprannome)] = soprannome
    ot = codifica_nome(allenatore["nome"], caratteri)
    pk4[G4.OFF_OT_NOME:G4.OFF_OT_NOME + len(ot)] = ot

    mosse = mosse_al_livello(pkhex, versione, nazionale, livello)
    pp_base = punti_potenza(pkhex)
    for i, m in enumerate((mosse + [0, 0, 0, 0])[:4]):
        struct.pack_into("<H", pk4, 0x28 + 2 * i, m)
        pk4[0x30 + i] = pp_base.get(m, 0)

    struct.pack_into("<H", pk4, G4.OFF_CHECKSUM, G4.somma_controllo(pk4))
    return bytes(pk4), {
        "sigla": sigla, "seme": seme, "pid": pid, "iv": iv, "mosse": mosse,
        "livello": livello, "versione": versione, "luogo": luogo, "nome_luogo": nome_luogo,
        "oggetto": oggetto, "fatidico": fatidico, "terreno": terreno,
        "cromatico": G4.e_cromatico(pid, allenatore["tid"], allenatore["sid"]),
        "genere": genere, "nome": nome, "tabella_nomi": tabella_usata,
    }


def genere_da_pid(pid, rapporto):
    """Il genere dal valore di personalita', con la stessa regola del fratello dei doni."""
    return G4.genere_da_pid(pid, rapporto)


_PP = {}


def punti_potenza(pkhex):
    """I punti potenza di base per mossa, dalla tabella della quinta generazione del verificatore.

    Si legge di la' e non da una trascrizione, per la ragione consueta; la tabella della quinta
    copre tutte le mosse della quarta con i medesimi valori, e dove il progetto ha gia' verificato
    quella coincidenza non la riverifica.
    """
    if not _PP:
        import re
        percorso = os.path.join(pkhex, "PKHeX.Core", "Moves", "MoveInfo5.cs")
        testo = io.open(percorso, encoding="utf-8").read()
        i = testo.find("PP")
        j = testo.index("[", i)
        k = testo.index("]", j)
        valori = [int(x) for x in re.findall(r"\b(\d{1,3})\b", testo[j:k])]
        for n, v in enumerate(valori):
            _PP[n] = v
    return _PP


def tabella_caratteri(pkhex):
    """La tabella dei caratteri della quarta generazione, dal lettore gia' scritto e verificato.

    Non si rilegge il convertitore del verificatore, perche' il progetto lo ha gia' letto una
    volta e quella lettura ha richiesto due correzioni: le costanti nominate dentro il letterale,
    che senza trattamento decodificavano i nomi come parole diverse, e l'ancora di lunghezza che
    dice se la lettura si sia fermata presto. Riscrivere quel lettore qui significherebbe rifare
    quelle due correzioni oppure rifare quei due errori.
    """
    schede = _modulo("schede-esemplari-gen4.py", "schede_esemplari_gen4")
    testo = io.open(os.path.join(pkhex, schede.CONVERTITORE), encoding="utf-8").read()
    internazionale = schede._voci_tabella(testo, "TableINT", schede.LUNGHEZZA_TABELLA)
    fuori = {}
    for codice, ch in enumerate(internazionale):
        # Il primo valore che rende un glifo vince: la tabella porta piu' posizioni con il
        # medesimo carattere di riempimento, e prendere l'ultima scriverebbe un codice che il
        # gioco non usa per quel glifo.
        fuori.setdefault(ch, codice)
    return fuori


def elenca():
    print("Gli incontri di quarta generazione che un oggetto o una condizione sbloccava.")
    print("")
    print("%-13s %-8s %-4s %-4s %-6s %-9s %-9s %s"
          % ("sigla", "specie", "liv", "ver", "luogo", "fatidico", "terreno", "sbloccato da"))
    for sigla, naz, liv, ver, luo, fat, ter, ogg, _nome in INCONTRI:
        print("%-13s %-8d %-4d %-4s %-6d %-9s %-9d %s"
              % (sigla, naz, liv, ver, luo, "si" if fat else "no", ter, ogg))
    print("")
    print("Non producibili come conformi:")
    for sigla, naz, ogg, luogo, perche in NON_PRODUCIBILI:
        print("  %-22s %s da %s: %s" % (sigla, luogo, ogg, perche))


def lotto(pkhex, cartella, allenatore):
    if not os.path.isdir(cartella):
        os.makedirs(cartella)
    caratteri = tabella_caratteri(pkhex)
    impronte, fatti = {}, 0
    for voce in INCONTRI:
        byte, r = componi(pkhex, voce, allenatore, caratteri)
        nome = r["sigla"]
        io.open(os.path.join(cartella, nome + ".pk4"), "wb").write(byte)
        impronte[nome] = {
            "file": nome + ".pk4",
            "sha256": hashlib.sha256(byte).hexdigest(),
            "seme": "0x%08X" % r["seme"],
            "personalita": "0x%08X" % r["pid"],
            "correlazione": "primo metodo",
            "sbloccato_da": r["oggetto"],
        }
        fatti += 1
        print("  %-13s liv %-3d %-3s luogo %-4d terreno %d  seme 0x%08X  PID 0x%08X  IV %s%s"
              % (nome, r["livello"], r["versione"], r["luogo"], r["terreno"], r["seme"], r["pid"],
                 "/".join(str(r["iv"][k]) for k in ("hp", "atk", "def", "spd", "satk", "sdef")),
                 "  CROMATICO" if r["cromatico"] else ""))
    io.open(os.path.join(cartella, "manifesto.json"), "w", encoding="utf-8").write(
        json.dumps(impronte, indent=1, ensure_ascii=False))
    print("")
    print("%d esemplari scritti in %s, con il manifesto delle impronte." % (fatti, cartella))
    for sigla, _naz, ogg, luogo, _p in NON_PRODUCIBILI:
        print("Non prodotto: %s, cioe' %s da %s. Vedi ADR-046." % (sigla, luogo, ogg))
    return fatti


def self_test():
    esiti = []

    def prova(nome, cond, det=""):
        esiti.append((nome, bool(cond), det))

    prova("tre incontri nella tavola", len(INCONTRI) == 3, str(len(INCONTRI)))
    prova("uno solo e' fatidico",
          [v[0] for v in INCONTRI if v[5]] == ["shaymin-pt"], "")
    prova("tutti da Platino", all(v[3] == "pt" for v in INCONTRI), "")
    prova("ogni versione ha un repertorio e un codice",
          all(v[3] in REPERTORI and v[3] in VERSIONI for v in INCONTRI), "")
    prova("la voce non producibile e' nominata e non omessa",
          len(NON_PRODUCIBILI) == 1 and NON_PRODUCIBILI[0][1] == 493, "")

    # Il terreno, che e' il campo nuovo rispetto alla terza generazione. La regola del
    # verificatore e' l'indice del bit piu' basso acceso nella maschera dei terreni ammessi.
    def indice(maschera):
        return (maschera & ~(maschera - 1)).bit_length() - 1
    prova("il terreno erboso ha indice due", indice(1 << 2) == 2, str(indice(1 << 2)))
    prova("il terreno di caverna ha indice cinque", indice(1 << 5) == 5, str(indice(1 << 5)))
    prova("l'assenza di terreno ha indice zero", indice(1 << 0) == 0, str(indice(1 << 0)))
    # Il controllo negativo: con piu' terreni ammessi vince il piu' basso e non il piu' alto.
    prova("negativo: fra piu' terreni ammessi vince il piu' basso",
          indice((1 << 2) | (1 << 7)) == 2, str(indice((1 << 2) | (1 << 7))))

    larghezza = max(len(n) for n, _, _ in esiti)
    for nome, ok, det in esiti:
        print("  %-*s  %s%s" % (larghezza, nome, "ok" if ok else "FALLITO",
                                ("  " + det) if (det and not ok) else ""))
    caduti = [n for n, ok, _ in esiti if not ok]
    print("")
    print("%d prove, %d fallite." % (len(esiti), len(caduti)))
    return 1 if caduti else 0


def main():
    global G4, I3
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "pkhex"))
    p.add_argument("--lotto")
    p.add_argument("--elenco", action="store_true")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()

    if a.self_test:
        return self_test()
    if a.elenco:
        elenca()
        return 0
    if not a.lotto:
        p.error("serve --lotto con la cartella di destinazione, oppure --elenco o --self-test")

    G4 = _modulo("genera-evento-gen4.py", "genera_evento_gen4")
    I3 = _modulo("genera-incontro-gen3.py", "genera_incontro_gen3")
    I3.G3 = I3._fratello()
    allenatore = G4.allenatore_del_progetto()
    if allenatore is None:
        sys.exit("manca il registro dell'allenatore del progetto")
    print("Allenatore: %s, identificativo %d, segreto %d."
          % (allenatore["nome"], allenatore["tid"], allenatore["sid"]))
    print("")
    lotto(a.pkhex, a.lotto, allenatore)
    return 0


if __name__ == "__main__":
    sys.exit(main())
