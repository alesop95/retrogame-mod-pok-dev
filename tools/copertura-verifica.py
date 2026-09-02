#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Misura che cosa la verifica esterna copra, e che cosa resti scoperto.

Perché esiste
-------------
Sette esemplari giudicati su centoventidue prodotti è un rapporto che non dice nulla. Non dice
nulla perché gli esemplari non sono intercambiabili: differiscono lungo dimensioni indipendenti,
e un giudizio su un esemplare vale per la dimensione che quell'esemplare esercita e non per le
altre. Un metodo di generazione provato è provato una volta per tutte, poiché il codice che lo
implementa è lo stesso per ogni esemplare che lo usi; una lingua provata dice che la tabella dei
caratteri di quella lingua funziona e non dice niente sulle altre; un gruppo di crescita provato
dice che quella formula dell'esperienza è giusta e non dice niente sulle altre cinque.

Questo programma calcola quindi la copertura per dimensione, che è la misura utile: per ciascuna
dimensione elenca i valori presenti nel lotto prodotto, quali sono stati toccati da un giudizio e
quali no. Il risultato dice dove sta il rischio residuo con la precisione di un elenco, invece di
un rapporto fra due numeri che nasconde tutto ciò che conta.

La distinzione fra una dimensione strutturale e una dimensione di dato è il punto
-------------------------------------------------------------------------------
Le dimensioni non hanno tutte lo stesso peso, e vale dirlo perché cambia come si legge l'esito.
Il metodo di generazione, il ramo della lucentezza e la derivazione del sesso sono dimensioni
strutturali: sono rami di codice, e provarne uno lo prova per ogni esemplare che vi passi. La
specie, il livello e le mosse sono dimensioni di dato: provarne uno prova quella riga di una
tabella e nessun'altra, quindi la loro copertura completa richiederebbe di provare tutto, che è
precisamente ciò che si vuole evitare. Fra le due sta il gruppo di crescita, che è una formula
scelta da un dato: le formule sono sei e provarle tutte è fattibile, mentre provare tutte le
specie non lo è.

Ne segue la lettura corretta dell'uscita di questo programma: sulle dimensioni strutturali la
copertura va portata a completa, e quando lo è il rischio su di esse è chiuso; sulle dimensioni
di dato la copertura resterà sempre parziale, e il rischio si riduce non provando di più ma
generando i dati da una fonte invece di trascriverli, che è la ragione per cui questo progetto
non trascrive tabelle.

Uso
---
    python tools/copertura-verifica.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex
"""

import argparse
import importlib.util
import io
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))

GIUDIZI = os.path.join(RADICE, "recreate-pokemon-distributions-events", "giudizi-esterni.json")

# Le dimensioni lungo cui gli esemplari differiscono, con la loro natura. Le strutturali sono
# rami di codice e la loro copertura si può chiudere; quelle di dato sono righe di tabella e la
# loro copertura resta parziale per costruzione.
STRUTTURALI = ("metodo", "lucentezza", "sesso_ot", "lingua", "uovo")
DI_DATO = ("nazionale", "livello")
FORMULA = ("gruppo",)

# I sei gruppi di crescita, nell'ordine in cui il costruttore li numera, per nominarli invece di
# stampare un indice.
NOMI_GRUPPI = ("medio veloce", "irregolare", "fluttuante", "medio lento", "veloce", "lento")


def carica_generatore():
    percorso = os.path.join(RADICE, "tools", "genera-evento-gen3.py")
    spec = importlib.util.spec_from_file_location("genera_evento_gen3", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def indice_dal_nome(nome):
    """L'indice della voce, dal nome del file che il lotto scrive.

    I nomi cominciano con l'indice a tre cifre. Le voci del registro che non seguono quella
    convenzione, come i due bracci dell'esperimento e l'esemplare composto a mano, non hanno un
    indice e vanno riconosciute per altra via: il registro le nomina in prosa e questo programma
    le associa al loro evento tramite il nome dell'allenatore, oppure le esclude dichiarandolo.
    """
    m = re.match(r"^(\d{3})-", os.path.basename(nome))
    return int(m.group(1)) if m else None


def giudicati(voci):
    """Le voci della tabella che un giudizio esterno ha toccato, e quelle senza indice.

    Restituisce la coppia fra l'insieme degli indici coperti e l'elenco delle voci del registro
    che non si sono potute associare a un indice, cosicché la loro esistenza non sia taciuta.
    """
    dati = json.loads(io.open(GIUDIZI, encoding="utf-8").read())
    coperti, senza = set(), []
    for g in dati["giudizi"]:
        indice = indice_dal_nome(g["file"])
        if indice is not None and 0 <= indice < len(voci):
            coperti.add(indice)
            continue
        # L'esemplare del decennale composto a mano corrisponde a una voce della tabella e va
        # associato per allenatore: senza questa associazione la copertura della lingua italiana
        # e del gruppo di crescita medio veloce risulterebbe assente mentre è stata provata.
        if "10ANNI" in g["file"]:
            for i, v in enumerate(voci):
                if v.get("ot") == "10ANNI" and v.get("nazionale") == 25:
                    coperti.add(i)
                    break
            else:
                senza.append(g["file"])
            continue
        senza.append(g["file"])
    return coperti, senza, dati


def etichetta_voce(v, indice):
    """Il nome del file che il lotto scrive per quella voce, per poterla ritrovare sul disco."""
    descrizione = re.sub(r"[^A-Za-z0-9]", "",
                         v.get("commento") or v.get("ot") or "evento") or "evento"
    return "%03d-%s-*.pk3" % (indice, descrizione)


def valore(v, dimensione, gruppi, mappa):
    if dimensione == "gruppo":
        interno = mappa.get(v["nazionale"])
        indice = gruppi.get(interno)
        return NOMI_GRUPPI[indice] if indice is not None and indice < len(NOMI_GRUPPI) else None
    if dimensione == "uovo":
        return "uovo" if v.get("uovo") else "esemplare"
    if dimensione == "lucentezza":
        return v.get("lucentezza") or "non vincolata"
    if dimensione == "sesso_ot":
        return v.get("sesso_ot") or "non dichiarata"
    if dimensione == "lingua":
        return v.get("lingua") or "di chi riceve"
    return v.get(dimensione)


def producibili(g, voci, ace, pkhex):
    """Gli indici delle voci che il lotto produce davvero.

    La copertura si misura sul prodotto e non sul catalogo, perché una voce che il programma non
    sa produrre non è esposta ad alcun rischio: non esiste alcun esemplare da giudicare.
    """
    fuori = set()
    for indice, v in enumerate(voci):
        if v.get("metodo") not in g.METODI_PRODUCIBILI:
            continue
        if v.get("uovo") or "ot_irrisolto" in v:
            continue
        fuori.add(indice)
    return fuori


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--ace", required=True)
    ap.add_argument("--pkhex", required=True)
    a = ap.parse_args(argv)

    g = carica_generatore()
    voci = g.voci_wc3(a.pkhex)
    mappa = g.nazionale_verso_interno(a.ace)
    gruppi = g.gruppo_di_crescita(a.ace)
    prodotti = producibili(g, voci, a.ace, a.pkhex)
    coperti, senza, dati = giudicati(voci)
    coperti_prodotti = coperti & prodotti

    print("Copertura della verifica esterna, verificatore " + dati["verificatore"]["nome"] +
          " " + dati["verificatore"]["versione"])
    print("")
    print("  voci producibili        " + str(len(prodotti)))
    print("  giudizi registrati      " + str(len(dati["giudizi"])))
    print("  voci toccate da almeno un giudizio " + str(len(coperti_prodotti)))
    if senza:
        print("  giudizi non associabili a una voce della tabella, e quindi non conteggiati "
              "nella copertura: " + str(len(senza)))
        for n in senza:
            print("    " + n)
    print("")

    for etichetta, dimensioni in (("Dimensioni strutturali, la cui copertura si può chiudere",
                                   STRUTTURALI),
                                  ("Formule scelte da un dato, la cui copertura si può chiudere "
                                   "con sforzo finito", FORMULA),
                                  ("Dimensioni di dato, la cui copertura resta parziale per "
                                   "costruzione", DI_DATO)):
        print("=== " + etichetta)
        for d in dimensioni:
            presenti = {}
            for i in sorted(prodotti):
                val = valore(voci[i], d, gruppi, mappa)
                presenti.setdefault(val, []).append(i)
            provati = sorted(v for v, ind in presenti.items()
                             if any(i in coperti_prodotti for i in ind))
            scoperti = sorted(v for v in presenti if v not in provati)
            print("  %-12s %d valori, %d provati, %d scoperti"
                  % (d, len(presenti), len(provati), len(scoperti)))
            if d in DI_DATO and len(presenti) > 12:
                print("               provati: " + ", ".join(str(x) for x in provati))
                print("               (l'elenco degli scoperti si omette: sono %d)"
                      % (len(scoperti),))
            else:
                if provati:
                    print("               provati: " + ", ".join(str(x) for x in provati))
                if scoperti:
                    print("               scoperti: " + ", ".join(str(x) for x in scoperti))
                    # Per ciascun valore scoperto si nomina una voce che lo esercita, perche' un
                    # elenco di valori dice dove sta il rischio e non dice che cosa fare. Si
                    # sceglie la prima in ordine di indice, che e' arbitrario ma deterministico:
                    # cio' che conta e' che il suggerimento non cambi fra due corse.
                    if d in STRUTTURALI or d in FORMULA:
                        for val in scoperti:
                            i = min(presenti[val])
                            print("               per %-14s prova la voce %3d, %s"
                                  % (str(val), i, etichetta_voce(voci[i], i)))
        print("")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
