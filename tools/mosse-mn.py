#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trova nei lotti prodotti gli esemplari che conoscono una macchina nascosta, e che quindi il
trasferimento rifiuta.

Perche' questo controllo, e da dove nasce
----------------------------------------
Il Parco Amico, che e' il solo passaggio dalla terza alla quarta generazione, rifiuta qualunque
esemplare che conosca una mossa che nel gioco d'origine sia una macchina nascosta, e il rifiuto e'
categorico: non esiste alcuna eccezione in gioco per Surf, mentre Mulinello e Scacciabruma in alcuni
titoli non sono macchine nascoste e quindi hanno un aggiramento naturale. Il Trasferitore, che e' il
passaggio dalla quinta generazione e dalle riedizioni per Console Virtuale verso la banca, porta la
medesima restrizione insieme a quelle sull'oggetto tenuto e sull'uovo.

Ne segue che una parte dei nostri lotti non passa la catena, e la cosa non si vede guardando i file:
si vede solo contando le mosse. Questo programma conta.

La conseguenza che rende il controllo urgente e' che la mossa non si puo' semplicemente cancellare.
Il caso studiato e' il Pikachu surfista dei premi di Stadium: Surf non sta nel suo insieme di mosse
apprendibili in alcun gioco successivo, quindi togliergliela per far passare il controllo la
perderebbe per sempre, e con essa la ragione per cui quell'esemplare e' un collezionabile. La via
che resta e' scrivere il dato direttamente nel formato di destinazione, cioe' saltare il passaggio
invece di soddisfarlo, che e' esattamente cio' che `tools/carica-lotto-gen3.py` fa un anello piu'
sotto.

L'elenco delle macchine nascoste, e il limite dichiarato
--------------------------------------------------------
Le mosse sono dichiarate per generazione nella tabella qui sotto, ricavate dalla pagina
enciclopedica dedicata e non dalla memoria. Il limite e' che l'elenco e' l'unione dei titoli di
ciascuna generazione, mentre il controllo del Parco Amico guarda il gioco d'origine: una mossa che
sia macchina nascosta in un titolo e non nell'altro fa quindi scattare la segnalazione anche dove
non servirebbe. E' il verso prudente dell'errore, e la riga segnalata dice quale mossa l'ha fatta
scattare cosicche' un umano possa raffinare.

Uso
---
    python tools/mosse-mn.py
    python tools/mosse-mn.py --check
    python tools/mosse-mn.py --self-test
"""

import argparse
import io
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PONTE = os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware")
sys.path.insert(0, PONTE)

from pokebridge import gb                       # noqa: E402
from pokebridge.gen1 import Gen1Mon             # noqa: E402
from pokebridge.gen2 import Gen2Mon             # noqa: E402
from pokebridge.gen3 import Gen3Mon             # noqa: E402
from pokebridge.save3 import record_da_file     # noqa: E402

USCITA = os.path.join(RADICE, "pokedex-home-completo", "MOSSE-MN.md")
NORMALIZZATO = os.path.join(RADICE, "pokedex-home-completo", "mosse-mn.csv")

# Le macchine nascoste per generazione, con il numero della mossa. I nomi vengono dalla pagina
# enciclopedica dedicata alle macchine nascoste, letta il 2026-09-09; i numeri sono quelli della
# tavola delle mosse del verificatore, che il programma verifica all'avvio invece di assumerli.
MN_PER_GENERAZIONE = {
    1: ("Cut", "Fly", "Surf", "Strength", "Flash"),
    2: ("Cut", "Fly", "Surf", "Strength", "Flash", "Whirlpool", "Waterfall"),
    3: ("Cut", "Fly", "Surf", "Strength", "Flash", "Rock Smash", "Waterfall", "Dive"),
}

# I lotti prodotti, con la generazione del formato e il gate che li aspetta.
LOTTI = (
    ("lotto-gb", (".pk1",), 1, "Trasferitore dalla Console Virtuale"),
    ("lotto-gb", (".pk2",), 2, "Trasferitore dalla Console Virtuale"),
    ("lotto-eventi", (".pk3",), 3, "Parco Amico verso la quarta generazione"),
    ("lotto-incontri-gen3", (".pk3",), 3, "Parco Amico verso la quarta generazione"),
)

NOMI_MOSSE = os.path.join("PKHeX.Core", "Resources", "text", "other", "en", "text_Moves_en.txt")


def numeri_delle_mn(pkhex):
    """La tavola dei numeri delle macchine nascoste, ricavata dai nomi e non assunta.

    Se un nome non compare nella tavola delle mosse il programma lo dichiara invece di ignorarlo:
    un nome che non si risolve significherebbe un controllo che passa sempre, cioe' il difetto
    peggiore per un controllo di questo tipo.
    """
    percorso = os.path.join(pkhex, NOMI_MOSSE)
    if not os.path.exists(percorso):
        return None, "manca la tavola delle mosse sotto " + pkhex
    nomi = [r.strip() for r in io.open(percorso, encoding="utf-8").read().split("\n")]
    per_nome = {}
    for numero, nome in enumerate(nomi):
        if nome and nome not in per_nome:
            per_nome[nome] = numero
    fuori, mancanti = {}, []
    for gen, mosse in MN_PER_GENERAZIONE.items():
        insieme = {}
        for nome in mosse:
            if nome in per_nome:
                insieme[per_nome[nome]] = nome
            else:
                mancanti.append((gen, nome))
        fuori[gen] = insieme
    if mancanti:
        return None, "nomi di mossa non risolti: %s" % mancanti
    return fuori, None


GB_INTESTAZIONE = 3      # conteggio, marcatore di specie, terminatore
# La struttura di squadra misura quarantaquattro byte in prima generazione e quarantotto in
# seconda, e la differenza non e' un dettaglio: prendere quarantaquattro byte da un file di seconda
# generazione produce un buffer che il lettore rifiuta, ed e' il difetto che questo controllo ha
# incontrato al secondo lancio dopo averne corretto un altro al primo.
GB_STRUTTURA = {1: 44, 2: 48}


def mosse_del_file(percorso, generazione):
    """Le quattro mosse di un file di lotto, secondo il formato della sua generazione.

    I file di prima e seconda generazione del nostro lotto non sono la struttura nuda: sono la
    forma di lista con cui il gioco tiene una squadra, cioe' tre byte di intestazione, la struttura
    di squadra, il nome dell'allenatore e il soprannome. Leggerli come struttura nuda fallisce sulla
    lunghezza, ed e' il difetto che questo controllo ha incontrato al primo lancio: sessantacinque
    voci dichiarate illeggibili mentre erano soltanto incartate.
    """
    dati = io.open(percorso, "rb").read()
    if generazione in (1, 2):
        quanti = GB_STRUTTURA[generazione]
        if len(dati) >= GB_INTESTAZIONE + quanti and dati[0] == 1:
            dati = dati[GB_INTESTAZIONE:GB_INTESTAZIONE + quanti]
        lettore = Gen1Mon if generazione == 1 else Gen2Mon
        return lettore.from_bytes(dati).moves
    # In terza generazione il file dell'editor e' in chiaro e non permutato: si converte nella
    # forma del salvataggio prima di leggerlo, altrimenti le mosse escono dal blocco sbagliato.
    return Gen3Mon.from_bytes(record_da_file(dati[:80])).attacks.moves


def esamina(cartella_notes, tavola):
    """Ogni voce dei lotti, con le macchine nascoste che conosce."""
    fuori, difetti = [], []
    for nome_lotto, estensioni, generazione, gate in LOTTI:
        cartella = os.path.join(cartella_notes, nome_lotto)
        if not os.path.isdir(cartella):
            difetti.append("manca il lotto " + nome_lotto)
            continue
        for nome in sorted(os.listdir(cartella)):
            if os.path.splitext(nome)[1].lower() not in estensioni:
                continue
            percorso = os.path.join(cartella, nome)
            try:
                mosse = mosse_del_file(percorso, generazione)
            except (gb.FormatError, ValueError) as errore:
                difetti.append("%s/%s non si legge: %s" % (nome_lotto, nome, errore))
                continue
            trovate = [tavola[generazione][m] for m in mosse if m in tavola[generazione]]
            fuori.append({
                "lotto": nome_lotto,
                "file": nome,
                "generazione": generazione,
                "gate": gate,
                "mn": trovate,
            })
    return fuori, difetti


def componi(voci, difetti):
    bloccate = [v for v in voci if v["mn"]]
    r = ["# Le voci dei lotti che una macchina nascosta blocca", ""]
    r.append("> Documento generato da `tools/mosse-mn.py`. Non si modifica a mano: si rigenera. Elenca gli esemplari prodotti che conoscono una mossa che nel gioco d'origine e' una macchina nascosta, e che quindi il passaggio fra generazioni rifiuta.")
    r.append("")
    r.append("Esaminate %d voci su quattro lotti, e %d sono bloccate. Il rifiuto non e' negoziabile e non si risolve cancellando la mossa, perche' su alcune specie quella mossa non e' piu' apprendibile in alcun gioco successivo: la via che resta e' scrivere il dato direttamente nel formato di destinazione, cioe' saltare il passaggio invece di soddisfarlo."
             % (len(voci), len(bloccate)))
    r.append("")
    if difetti:
        r.append("Difetti di lettura da guardare, perche' una voce non letta non e' una voce senza macchine nascoste: %s." % "; ".join(difetti[:8]))
        r.append("")
    if bloccate:
        r.append("| Lotto | File | Gen | Macchine nascoste | Passaggio che rifiuta |")
        r.append("|---|---|---|---|---|")
        for v in bloccate:
            r.append("| %s | %s | %d | %s | %s |"
                     % (v["lotto"], v["file"], v["generazione"], "; ".join(v["mn"]), v["gate"]))
        r.append("")
    else:
        r.append("Nessuna voce dei lotti conosce una macchina nascosta, quindi su questo fronte la catena non rifiuta nulla.")
        r.append("")
    return "\n".join(r) + "\n"


def normalizza(voci):
    r = ["lotto,file,generazione,mn,gate"]
    for v in voci:
        if not v["mn"]:
            continue
        campi = [v["lotto"], v["file"], str(v["generazione"]), "; ".join(v["mn"]), v["gate"]]
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

    pkhex = os.path.join(RADICE, "_notes", "fonti", "pkhex")
    tavola, errore = numeri_delle_mn(pkhex)
    if errore:
        print("  self-test parziale: " + errore)
    else:
        # I numeri che la tavola del verificatore assegna: sono il dato su cui il controllo
        # poggia, quindi vanno visti almeno una volta invece di essere assunti.
        prova("Surf e' la mossa 57", "Surf", tavola[1].get(57))
        prova("Cut e' la mossa 15", "Cut", tavola[1].get(15))
        prova("in prima generazione le MN sono cinque", 5, len(tavola[1]))
        prova("in seconda sono sette", 7, len(tavola[2]))
        prova("in terza sono otto", 8, len(tavola[3]))
        # Controllo negativo: una mossa qualunque non deve risultare macchina nascosta.
        prova("Placcaggio non e' una MN", None, tavola[1].get(33))
        prova("Mulinello non e' MN in prima generazione", None, tavola[1].get(250))
        prova("ma lo e' in seconda", "Whirlpool", tavola[2].get(250))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "pkhex"))
    ap.add_argument("--notes", default="_notes")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    pkhex = a.pkhex if os.path.isabs(a.pkhex) else os.path.join(RADICE, a.pkhex)
    tavola, errore = numeri_delle_mn(pkhex)
    if errore:
        print("rifiutato: " + errore)
        return 1
    notes = a.notes if os.path.isabs(a.notes) else os.path.join(RADICE, a.notes)
    voci, difetti = esamina(notes, tavola)

    testo = componi(voci, difetti)
    csv = normalizza(voci)
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
    bloccate = [v for v in voci if v["mn"]]
    print("scritti %s e %s" % (USCITA, NORMALIZZATO))
    print("  esaminate %d voci | bloccate da una macchina nascosta %d | difetti di lettura %d"
          % (len(voci), len(bloccate), len(difetti)))
    for d in difetti[:5]:
        print("  DIFETTO " + d)
    return 0


if __name__ == "__main__":
    sys.exit(main())
