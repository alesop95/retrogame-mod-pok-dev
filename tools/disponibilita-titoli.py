#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calcola quali specie e forme la chiusura della banca vincoli davvero, e quali no.

Perché esiste
-------------
L'obiettivo del progetto è avere in Pokemon Home ogni specie. Il deposito accetta esemplari per
due vie con proprietà temporali opposte: quella diretta dei titoli dell'ottava e della nona
generazione, che non ha scadenza, e quella della banca, che cessa il 26 febbraio 2027. Ne segue
che il vincolo di tempo riguarda soltanto ciò che nessun titolo a via diretta produce, e che
sapere quanto sia quel sottoinsieme decide come si spendono i giorni che restano.

Questo programma lo calcola invece di stimarlo, leggendo le tabelle delle statistiche di base che
l'implementazione di riferimento porta per ciascun titolo. Quelle tabelle sono array di record a
dimensione fissa, quindi si leggono senza riscrivere alcun lettore: per ogni specie il record
base dichiara quante forme essa abbia e da quale indice comincino, e un contrassegno dice se
quella voce esista nel gioco.

I tre filtri che rendono il risultato onesto
-------------------------------------------
Il contrassegno di presenza dice che una voce esiste nei dati del gioco, non che sia ottenibile
né che possa uscirne. Su questo il programma applica due filtri, entrambi letti dalla fonte e non
congetturati, senza i quali il conto sarebbe sbagliato in eccesso.

Il primo sono le forme di sola battaglia, cioè quelle che esistono soltanto durante un incontro:
le megaevoluzioni, i cambi di forma temporanei, le fusioni. Non possono stare in un deposito
perché non possono stare in una scatola.

Il secondo sono le forme totemiche della settima generazione, e il loro caso è il più
istruttivo perché la loro esclusione non è ovvia. Il verificatore dei trasferimenti dichiara che
una di esse, per passare all'ottava generazione, deve essere già tornata alla propria forma base,
e che quattro specie non si trasferiscono affatto. Ne segue che nessuna forma totemica può
esistere nel deposito, né prima né dopo la chiusura della banca: non sono voci in attesa di
scadenza, sono voci irraggiungibili per costruzione.

Il terzo filtro non è nei dati ed è dichiarato: la tabella di Let's Go non porta il contrassegno
di presenza, quindi il suo insieme di specie è scritto qui a mano e non letto. È l'unico dato
trascritto di questo programma, ed è piccolo e verificabile a occhio.

Uso
---
    python tools/disponibilita-titoli.py --pkhex _notes/fonti/pkhex
"""

import argparse
import io
import os
import re
import struct
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# (etichetta, file, dimensione del record, offset di FormStatsIndex, offset di FormCount,
#  come si legge la presenza, massimo di specie, via)
TAVOLE = (
    ("LGPE", "personal_gg",   0x54, 0x1C, 0x20, None,             809,  "diretta"),
    ("SwSh", "personal_swsh", 0xB0, 0x1E, 0x20, ("bit", 0x21, 6), 898,  "diretta"),
    ("BDSP", "personal_bdsp", 0x44, 0x1E, 0x20, ("bit", 0x21, 6), 493,  "diretta"),
    ("PLA",  "personal_la",   0xB0, 0x1E, 0x20, ("bit", 0x21, 6), 905,  "diretta"),
    ("SV",   "personal_sv",   0x50, 0x18, 0x1A, ("byte", 0x1C),   1025, "diretta"),
    ("Z-A",  "personal_za",   0x50, 0x18, 0x1A, ("byte", 0x1C),   1025, "diretta"),
    ("USUM", "personal_uu",   0x54, 0x1C, 0x20, None,             807,  "indiretta"),
)

CARTELLA_TABELLE = "PKHeX.Core/Resources/byte/personal"
SORGENTE_SPECIE = "PKHeX.Core/Game/Enums/Species.cs"
SORGENTE_FORME = "PKHeX.Core/Legality/Tables/FormInfo.cs"

# L'insieme delle specie di Let's Go, scritto e non letto perché quella tabella non porta il
# contrassegno di presenza: i centocinquantuno di Kanto più le due specie che quel titolo ha
# introdotto. È l'unico dato trascritto di questo programma.
LGPE_SPECIE = frozenset(range(1, 152)) | {808, 809}

# L'ultimo numero del Dex Nazionale considerato. Coincide con il massimo che i titoli della nona
# generazione dichiarano, e va aggiornato quando un titolo nuovo lo alza.
DEX_MASSIMO = 1025


def specie_per_nome(pkhex):
    """La corrispondenza fra nome inglese e numero, dalla posizione nell'enumerazione.

    L'enumerazione della fonte comincia da una voce nulla e prosegue senza salti, quindi il
    numero di una specie è la sua posizione. Vale controllarlo invece di fidarsi: se un giorno
    la fonte introducesse un valore esplicito, la posizione non basterebbe più.
    """
    testo = leggi(pkhex, SORGENTE_SPECIE)
    corpo = testo[testo.index("public enum Species"):]
    corpo = corpo[corpo.index("{") + 1:corpo.index("}")]
    voci = [v.strip() for v in corpo.split(",")]
    voci = [re.sub(r"//.*", "", v).strip() for v in voci]
    voci = [v for v in voci if v and not v.startswith("/")]
    if any("=" in v for v in voci):
        sys.exit("l'enumerazione delle specie contiene un valore esplicito: la posizione non "
                 "basta piu a ricavare il numero, e il programma va adeguato invece di "
                 "restituire numeri sbagliati in silenzio")
    fuori = {nome: i for i, nome in enumerate(voci)}
    if fuori.get("Bulbasaur") != 1 or fuori.get("Pecharunt") != DEX_MASSIMO:
        sys.exit("i due controlli sull'enumerazione non tornano: la prima specie dovrebbe "
                 "valere uno e l'ultima %d" % (DEX_MASSIMO,))
    return fuori


def leggi(pkhex, rel):
    p = os.path.join(pkhex, rel.replace("/", os.sep))
    if not os.path.exists(p):
        sys.exit("manca " + rel + " sotto " + pkhex + ".")
    return io.open(p, encoding="utf-8", errors="ignore").read()


def elenco_specie(testo, nome_campo, per_nome):
    """I numeri di specie di un elenco che la fonte scrive come nomi dell'enumerazione."""
    inizio = testo.find("ReadOnlySpan<ushort> " + nome_campo)
    if inizio < 0:
        sys.exit("non trovo l'elenco " + nome_campo + " in " + SORGENTE_FORME)
    corpo = testo[testo.index("[", inizio):testo.index("];", inizio)]
    fuori = set()
    for nome in re.findall(r"\(u?short\)([A-Za-z0-9_]+)|\(int\)([A-Za-z0-9_]+)", corpo):
        n = nome[0] or nome[1]
        if n not in per_nome:
            sys.exit("l'elenco " + nome_campo + " nomina " + n + ", che l'enumerazione delle "
                     "specie non contiene")
        fuori.add(per_nome[n])
    return fuori


def specie_con_forma_totemica(testo, per_nome):
    """Le specie che hanno una forma totemica, dal ramo di scelta della fonte."""
    inizio = testo.find("HasTotemForm(ushort species) => species switch")
    if inizio < 0:
        sys.exit("non trovo il ramo di scelta delle forme totemiche in " + SORGENTE_FORME)
    corpo = testo[testo.index("{", inizio):testo.index("};", inizio)]
    fuori = set()
    for nome in re.findall(r"\(ushort\)([A-Za-z0-9_]+)\s*=>\s*true", corpo):
        if nome not in per_nome:
            sys.exit("il ramo delle forme totemiche nomina " + nome + ", ignoto")
        fuori.add(per_nome[nome])
    return fuori


def e_totemica(specie, forma, totemiche, per_nome):
    """Se quella coppia sia una forma totemica, secondo la logica della fonte.

    Le tre eccezioni sono trascritte dalla fonte e non dedotte, e vanno lette accanto a essa:
    il travestimento ha due forme totemiche perché ne porta anche la variante rotta, e due
    specie di prima generazione hanno la forma totemica in seconda posizione perché la prima è
    già occupata dalla loro variante di Alola.
    """
    if forma == 0 or specie not in totemiche:
        return False
    if specie == per_nome["Mimikyu"]:
        return forma in (2, 3)
    if specie in (per_nome["Raticate"], per_nome["Marowak"]):
        return forma == 2
    return forma == 1


def presente(rec, modo):
    if modo is None:
        return True
    if modo[0] == "bit":
        return ((rec[modo[1]] >> modo[2]) & 1) == 1
    return rec[modo[1]] != 0


def voci_del_titolo(pkhex, nome, size, off_fsi, off_fc, modo, maxsp):
    """Le coppie specie e forma che quel titolo dichiara presenti."""
    p = os.path.join(pkhex, CARTELLA_TABELLE.replace("/", os.sep), nome)
    if not os.path.exists(p):
        sys.exit("manca la tabella " + nome + " sotto " + pkhex + ".")
    d = io.open(p, "rb").read()
    n = len(d) // size
    fuori = set()
    for sp in range(1, min(maxsp, n - 1) + 1):
        base = d[sp * size:(sp + 1) * size]
        if len(base) < size:
            break
        if presente(base, modo):
            fuori.add((sp, 0))
        fc = base[off_fc]
        fsi = struct.unpack_from("<H", base, off_fsi)[0]
        for f in range(1, max(fc, 1)):
            idx = fsi + f - 1
            if idx <= 0 or (idx + 1) * size > len(d):
                continue
            if presente(d[idx * size:(idx + 1) * size], modo):
                fuori.add((sp, f))
    return fuori


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", required=True, help="cartella del clone del verificatore")
    a = ap.parse_args(argv)

    per_nome = specie_per_nome(a.pkhex)
    forme = leggi(a.pkhex, SORGENTE_FORME)
    battaglia = elenco_specie(forme, "BattleMegas", per_nome) \
        | elenco_specie(forme, "BattleForms", per_nome)
    totemiche = specie_con_forma_totemica(forme, per_nome)
    per_numero = {v: k for k, v in per_nome.items()}

    print("Fonti lette")
    print("  specie nell'enumerazione                 " + str(DEX_MASSIMO))
    print("  specie con forme di sola battaglia       " + str(len(battaglia)))
    print("  specie con forma totemica                " + str(len(totemiche)))
    print("")

    insiemi = {}
    for et, nome, size, fsi, fc, modo, maxsp, via in TAVOLE:
        v = voci_del_titolo(a.pkhex, nome, size, fsi, fc, modo, maxsp)
        if et == "LGPE":
            # La sua tabella non porta il contrassegno, quindi si filtra per l'insieme scritto.
            v = {(s, f) for (s, f) in v if s in LGPE_SPECIE}
        insiemi[et] = v
        print("  %-5s via %-10s specie %4d   voci-forma %4d"
              % (et, via, len({s for s, _ in v}), len(v)))
    print("")

    diretta = set()
    for et, *_rest, via in TAVOLE:
        if via == "diretta":
            diretta |= insiemi[et]
    indiretta = set()
    for et, *_rest, via in TAVOLE:
        if via == "indiretta":
            indiretta |= insiemi[et]

    print("=== Livello di specie")
    sp_diretta = {s for s, _ in diretta}
    mancanti = sorted(set(range(1, DEX_MASSIMO + 1)) - sp_diretta)
    print("  specie raggiungibili per via diretta: %d su %d" % (len(sp_diretta), DEX_MASSIMO))
    print("  specie che la scadenza vincola: %d" % len(mancanti))
    for s in mancanti:
        print("    #%4d %s" % (s, per_numero.get(s, "?")))
    print("")

    print("=== Livello di voce-forma")
    solo_indiretta = sorted(indiretta - diretta)
    print("  voci-forma raggiungibili per via diretta: %d" % len(diretta))
    print("  voci-forma che soltanto la via indiretta dichiara: %d" % len(solo_indiretta))
    resta = []
    for s, f in solo_indiretta:
        if e_totemica(s, f, totemiche, per_nome):
            motivo = "forma totemica: al trasferimento torna alla forma base, oppure non si trasferisce"
        elif s in battaglia:
            motivo = "forma di sola battaglia: non puo stare in una scatola"
        else:
            motivo = "NESSUN FILTRO LA ESCLUDE: e una voce che la scadenza vincola"
            resta.append((s, f))
        print("    #%4d %-12s forma %d  %s" % (s, per_numero.get(s, "?"), f, motivo))
    print("")
    print("=== Esito")
    print("  voci-forma che la chiusura della banca vincola davvero: %d" % len(resta))
    if not resta:
        print("  Nessuna. Al livello di specie e al livello di forma il completamento del Dex")
        print("  Nazionale in Home non ha scadenza: cio che la scadenza vincola non e la")
        print("  collezione ma i singoli esemplari la cui identita richiede una provenienza")
        print("  anteriore all'ottava generazione, che sono un'altra cosa e non si contano qui.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
