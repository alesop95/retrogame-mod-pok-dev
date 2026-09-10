#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confronta l'enumerazione del progetto con quella di PokePC Classic, terza misura indipendente.

Perche' una terza enumerazione
------------------------------
Il progetto aveva due enumerazioni del living dex, la propria e quella del foglio comunitario, e
`tools/confronta-foglio-livingdex.py` le mette una accanto all'altra. Due misure che divergono
dicono che una delle due sbaglia e non quale: e' il caso classico in cui la terza misura vale piu'
della somma delle prime due, perche' rompe la parita'. PokePC Classic, gia' SuperEffective.gg, e'
un tracciatore di living dex che pubblica i propri dati come JSON sotto licenza MIT, quindi la sua
enumerazione si legge dal dato e non dall'interfaccia, il che la rende confrontabile riga per riga
invece che a occhio.

Che cosa e' la sua enumerazione, esattamente
--------------------------------------------
Non e' una lista di specie ma una disposizione in scatole, cioe' l'elenco delle caselle che quel
tracciatore ritiene si debbano riempire per dire completo un deposito. E' precisamente la domanda
che la nostra lista di spunta dichiara indeterminata, cioe' quali forme il deposito conti come
casella separata, quindi vale come risposta di terzo livello a una domanda su cui nessuna fonte di
primo livello si pronuncia. Le disposizioni disponibili per il deposito sono sette, e la prima
stesura di questo programma assumeva che differissero per il solo ordinamento: non e' vero, perche'
due di esse danno una casella propria alla forma gigamax e due si dichiarano minime. Il programma
quindi non lo assume ma lo misura, le raggruppa per insieme di voci collocate e dichiara nel
documento quale delle sette usa e che cosa quella scelta cambi nel totale.

Il programma non fonde e non decide, per la stessa ragione del suo fratello maggiore: due misure
indipendenti valgono in quanto indipendenti. Classifica pero' le divergenze, e qui la
classificazione e' migliore di quella sul foglio, perche' i dati di PokePC portano per ogni voce i
contrassegni che dicono che cosa essa sia, cioe' forma femminile, forma cosmetica, forma di sola
battaglia, megaevoluzione o gigamax. Una divergenza classificata per contrassegno e' un fatto e non
un indizio.

Da dove vengono i dati
----------------------
Dal deposito pubblico `pokepc/classic.pokepc.net`, file `legacy-pokemon.min.json` e
`legacy-boxpresets.min.json` sotto `src/lib/data-client`, scaricati in `_notes/fonti/pokepc/`, che
e' materiale di terzi e non entra nel version control: cio' che entra e' questo confronto. I due
file si riprendono con le due righe seguenti, che sono l'unica dipendenza esterna del programma.

    curl -sL -o _notes/fonti/pokepc/pokemon.min.json https://raw.githubusercontent.com/pokepc/classic.pokepc.net/main/src/lib/data-client/pokemon/legacy-pokemon.min.json
    curl -sL -o _notes/fonti/pokepc/boxpresets.min.json https://raw.githubusercontent.com/pokepc/classic.pokepc.net/main/src/lib/data-client/box-presets/legacy-boxpresets.min.json

Uso
---
    python tools/confronta-livingdex-pokepc.py
    python tools/confronta-livingdex-pokepc.py --check
    python tools/confronta-livingdex-pokepc.py --self-test
"""

import argparse
import io
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "tools"))

DATI = os.path.join(RADICE, "_notes", "fonti", "pokepc")
SPECIE = os.path.join(DATI, "pokemon.min.json")
SCATOLE = os.path.join(DATI, "boxpresets.min.json")
NOSTRA = os.path.join(RADICE, "pokedex-home-completo", "CHECKLIST-COMPLETA.md")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "CONFRONTO-LIVINGDEX-POKEPC.md")

INSIEME = "home"
DISPOSIZIONE = "fully-sorted"
MAX_SPECIE = 1025

# I contrassegni che il dato porta per ogni voce, nell'ordine in cui il programma li prova: la
# prima corrispondenza vince, cosicche' una voce cada in una classe sola e le classi si sommino
# al totale senza doppi conteggi.
CLASSI = (
    ("isFemaleForm", "forma femminile, cioe' una differenza di sesso resa come voce propria"),
    ("isMega", "megaevoluzione"),
    ("isGmax", "forma gigamax"),
    ("isBattleOnlyForm", "forma di sola battaglia"),
    ("isCosmeticForm", "forma cosmetica, cioe' una variante che il campo della forma non separa"),
)


def carica_fratello():
    """Il lettore della nostra lista di spunta, preso dal programma che lo possiede invece di ricopiarlo.

    La regola che il progetto applica altrove vale anche qui: chi ha bisogno di una tavola o di un
    lettore che vive gia' in un altro programma lo carica come modulo, cosicche' una correzione la'
    valga anche qui. Il nome del file porta trattini e non e' un identificativo Python valido,
    quindi il caricamento passa dalla via esplicita invece che da un import.
    """
    import importlib.util
    percorso = os.path.join(RADICE, "tools", "confronta-foglio-livingdex.py")
    if not os.path.exists(percorso):
        return None, "manca il programma che legge la nostra lista, cioe' " + percorso
    spec = importlib.util.spec_from_file_location("confronta_foglio_livingdex", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    if not hasattr(modulo, "leggi_nostra"):
        return None, "il programma fratello non espone piu' il lettore della nostra lista"
    return modulo, None


def carica_specie(percorso):
    """L'anagrafica delle voci, indicizzata per identificativo, con il numero di catalogo e i contrassegni."""
    if not os.path.exists(percorso):
        return None, "mancano i dati di PokePC in " + percorso
    dati = json.load(io.open(percorso, encoding="utf-8"))
    if not isinstance(dati, list) or not dati:
        return None, "i dati di PokePC non sono l'elenco atteso"
    per_id = {}
    for voce in dati:
        per_id[voce["id"]] = voce
    return per_id, None


def carica_disposizione(percorso, insieme=INSIEME, quale=DISPOSIZIONE):
    """Gli identificativi che una disposizione colloca in una casella, e le disposizioni sorelle per il controllo."""
    if not os.path.exists(percorso):
        return None, None, "mancano le disposizioni di PokePC in " + percorso
    dati = json.load(io.open(percorso, encoding="utf-8"))
    if insieme not in dati:
        return None, None, "le disposizioni non contengono l'insieme " + insieme
    gruppo = dati[insieme]
    if quale not in gruppo:
        return None, None, "l'insieme %s non ha la disposizione %s" % (insieme, quale)

    def identificativi(voce):
        """Le caselle piene di una disposizione, come coppia fra identificativo e contrassegno gigamax.

        Una cella e' di norma un identificativo, ma puo' essere una casella vuota, che si salta, o un
        oggetto con un contrassegno gigamax: in quel caso la casella chiede la forma gigamax della
        medesima specie, quindi e' un collezionabile distinto e va contata a parte. Identificare una
        cella con il solo identificativo, come il programma faceva alla prima stesura, confonde le due
        e fa sparire trentotto caselle nelle disposizioni che le usano.
        """
        visti = []
        for scatola in voce.get("boxes", []):
            for cella in scatola.get("pokemon", []):
                if not cella:
                    continue
                if isinstance(cella, dict):
                    visti.append((cella.get("pid"), bool(cella.get("gmax"))))
                else:
                    visti.append((cella, False))
        return visti

    scelti = identificativi(gruppo[quale])
    sorelle = {}
    for nome, voce in gruppo.items():
        sorelle[nome] = set(identificativi(voce))
    return scelti, sorelle, None


def classe_di(voce):
    """La classe di una voce che non sia la specie base, letta dai suoi contrassegni."""
    for campo, etichetta in CLASSI:
        if voce.get(campo):
            return etichetta
    return "altra forma, cioe' una variante che il campo della forma separa"


def conta_per_dex(scelti, per_id):
    """Il conto delle caselle per numero di catalogo, e le voci sconosciute all'anagrafica.

    Una casella con il contrassegno gigamax non e' la voce che il suo identificativo nomina ma la
    forma gigamax di quella specie, quindi entra nel conto con una classe propria invece di
    duplicare la voce base.
    """
    conto, dettaglio, ignote = {}, {}, []
    for identificativo, gigamax in scelti:
        voce = per_id.get(identificativo)
        if voce is None:
            ignote.append(identificativo)
            continue
        if gigamax:
            voce = dict(voce, isForm=True, isDefault=False, isGmax=True)
        dex = voce["dexNum"]
        conto[dex] = conto.get(dex, 0) + 1
        dettaglio.setdefault(dex, []).append(voce)
    return conto, dettaglio, ignote


def indizio_loro(voci):
    """Che cosa PokePC conti in piu' su una specie, per classe e non per congettura."""
    classi = {}
    for voce in voci:
        if voce.get("isDefault") and not voce.get("isForm"):
            continue
        classi.setdefault(classe_di(voce), 0)
        classi[classe_di(voce)] += 1
    if not classi:
        return "nessuna voce oltre la specie base"
    return "; ".join("%d %s" % (n, e) for e, n in sorted(classi.items(), key=lambda x: -x[1]))


def componi(conto_loro, dettaglio, nostro, escluse, ignote, sorelle):
    loro_totale = sum(conto_loro.get(n, 0) for n in range(1, MAX_SPECIE + 1))
    nostro_totale = sum(nostro.values())
    dex_loro = len([n for n in range(1, MAX_SPECIE + 1) if conto_loro.get(n, 0)])

    piu_loro, piu_nostre, accordo = [], [], 0
    for n in range(1, MAX_SPECIE + 1):
        loro, noi = conto_loro.get(n, 0), nostro[n]
        if loro == noi:
            accordo += 1
            continue
        voci = dettaglio.get(n, [])
        nome = voci[0]["name"] if voci else "?"
        if loro > noi:
            piu_loro.append((n, nome, loro, noi, indizio_loro(voci)))
        else:
            diciture = escluse.get(n, [])
            motivo = ("la nostra lista scarta %d posizioni con la dicitura: %s"
                      % (len(diciture), diciture[0][:90]) if diciture else
                      "la nostra lista conta %d posizioni di forma che PokePC non colloca in una casella"
                      % (noi - 1))
            piu_nostre.append((n, nome, loro, noi, motivo))

    classi = {}
    for n in range(1, MAX_SPECIE + 1):
        for voce in dettaglio.get(n, []):
            if voce.get("isDefault") and not voce.get("isForm"):
                continue
            classi[classe_di(voce)] = classi.get(classe_di(voce), 0) + 1

    gruppi = {}
    for nome, insieme in sorelle.items():
        gruppi.setdefault(frozenset(insieme), []).append(nome)

    r = []
    r.append("# Confronto fra la nostra enumerazione e quella di PokePC Classic")
    r.append("")
    r.append("> Documento generato da `tools/confronta-livingdex-pokepc.py`. Non si modifica a mano: si rigenera. Non fonde le due enumerazioni e non decide chi abbia ragione; le mette una accanto all'altra e classifica le divergenze per contrassegno.")
    r.append("")
    r.append("PokePC Classic, gia' SuperEffective.gg, e' un tracciatore di living dex che pubblica i propri dati come JSON sotto licenza MIT. E' la terza enumerazione indipendente che il progetto possiede, dopo la propria e quella del foglio comunitario, e serve a rompere la parita' fra le prime due: due misure che divergono dicono che una sbaglia e non quale. Resta una fonte di terzo livello, cioe' l'implementazione di un autore, e vale come controprova e non come autorita'.")
    r.append("")
    r.append("Cio' che si confronta non e' una lista di specie ma una disposizione in scatole, cioe' l'elenco delle caselle che quel tracciatore ritiene si debbano riempire perche' un deposito sia completo. E' esattamente la domanda che la nostra lista di spunta dichiara indeterminata, cioe' quali forme il deposito conti come casella separata.")
    r.append("")
    r.append("## Il conto delle due enumerazioni")
    r.append("")
    r.append("| Misura | PokePC | Nostra |")
    r.append("|---|---|---|")
    r.append("| voci totali da possedere | %d | %d |" % (loro_totale, nostro_totale))
    r.append("| numeri di catalogo distinti | %d | %d |" % (dex_loro, MAX_SPECIE))
    r.append("| voci oltre la specie base | %d | %d |" % (loro_totale - dex_loro, nostro_totale - MAX_SPECIE))
    r.append("| specie su cui le due concordano | %d | %d |" % (accordo, accordo))
    r.append("")
    r.append("Lo scarto complessivo e' di %d voci, e come nel confronto con il foglio va letto nelle due direzioni separatamente, perche' sono scarti di natura diversa che si compensano in parte. PokePC conta piu' di noi su %d specie, per %d voci in eccesso; noi contiamo piu' di PokePC su %d specie, per %d voci."
             % (abs(loro_totale - nostro_totale), len(piu_loro),
                sum(l - n for _, _, l, n, _ in piu_loro), len(piu_nostre),
                sum(n - l for _, _, l, n, _ in piu_nostre)))
    r.append("")
    r.append("## Che cosa PokePC colloca in una casella, per classe")
    r.append("")
    r.append("Il conto seguente riguarda le sole voci oltre la specie base, e le classi vengono dai contrassegni del dato e non da una nostra lettura. Una voce cade in una classe sola, quindi le classi si sommano al totale.")
    r.append("")
    r.append("| Classe | Voci |")
    r.append("|---|---|")
    for etichetta, n in sorted(classi.items(), key=lambda x: -x[1]):
        r.append("| %s | %d |" % (etichetta, n))
    r.append("")
    r.append("## Le disposizioni sorelle, che non concordano fra loro")
    r.append("")
    r.append("Le disposizioni del deposito sono %d, e la prima stesura di questo programma assumeva che differissero per il solo ordinamento. Non e' vero, e la verifica lo dice: si raggruppano per insieme di voci collocate in %d insiemi distinti. La differenza non e' un difetto del dato ma una scelta di chi lo ha scritto, cioe' se dare una casella propria alla forma gigamax di una specie che ne ha una."
             % (len(sorelle), len(gruppi)))
    r.append("")
    r.append("| Voci collocate | Disposizioni |")
    r.append("|---|---|")
    for insieme, nomi in sorted(gruppi.items(), key=lambda x: -len(x[0])):
        r.append("| %d | %s |" % (len(insieme), ", ".join(sorted(nomi))))
    r.append("")
    r.append("Il confronto usa `%s`, che appartiene al gruppo intermedio: conta le forme regionali e le differenze di sesso, non duplica una specie per la sua forma gigamax, e non applica la compattazione delle due dichiarate minime. La scelta va dichiarata perche' cambia il totale di trentotto voci in un verso e di quattordici nell'altro."
             % DISPOSIZIONE)
    if ignote:
        r.append("")
        r.append("Voci collocate in una casella e ignote all'anagrafica: %d, cioe' %s. Sono escluse dal confronto e la loro presenza va spiegata prima di fidarsi del totale."
                 % (len(ignote), ", ".join(sorted(set(ignote))[:10])))
    r.append("")
    r.append("## Dove PokePC conta piu' di noi")
    r.append("")
    r.append("Sono %d specie. La classe prevalente dice la natura della nostra cecita': cio' che il campo della forma non separa, come le differenze di sesso e le varianti cosmetiche, non entra nella nostra enumerazione perche' la leggiamo dalla struttura del dato e non da un catalogo di collezionabili." % len(piu_loro))
    r.append("")
    r.append("| Dex | Specie | PokePC | Nostra | Che cosa conta in piu' |")
    r.append("|---|---|---|---|---|")
    for n, nome, loro, noi, indizio in piu_loro:
        r.append("| %d | %s | %d | %d | %s |" % (n, nome, loro, noi, indizio))
    r.append("")
    r.append("## Dove contiamo piu' di PokePC")
    r.append("")
    r.append("Sono %d specie. Qui la lettura si rovescia: la nostra enumerazione legge le posizioni di forma dalla tabella del gioco, e quel numero comprende posizioni che non sono oggetti distinti da possedere." % len(piu_nostre))
    r.append("")
    r.append("| Dex | Specie | PokePC | Nostra | Perche' |")
    r.append("|---|---|---|---|---|")
    for n, nome, loro, noi, motivo in piu_nostre:
        r.append("| %d | %s | %d | %d | %s |" % (n, nome, loro, noi, motivo))
    r.append("")
    return "\n".join(r) + "\n"


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("il tetto delle specie", 1025, MAX_SPECIE)
    prova("l'insieme confrontato e' il deposito", "home", INSIEME)

    # La classificazione per contrassegno, che e' la sola cosa che il programma decide da se'.
    prova("una forma femminile e' una differenza di sesso", True,
          "differenza di sesso" in classe_di({"isFemaleForm": True}))
    prova("una megaevoluzione ha classe propria", "megaevoluzione", classe_di({"isMega": True}))
    prova("il primo contrassegno vince sul secondo", True,
          "differenza di sesso" in classe_di({"isFemaleForm": True, "isCosmeticForm": True}))
    prova("una forma senza contrassegni cade nella classe residua", True,
          "altra forma" in classe_di({}))

    # Il conto per numero di catalogo, e il rifiuto dichiarato di cio' che l'anagrafica non conosce.
    per_id = {"a": {"id": "a", "dexNum": 1, "name": "Uno", "isDefault": True, "isForm": False},
              "a-f": {"id": "a-f", "dexNum": 1, "name": "Uno", "isForm": True, "isFemaleForm": True}}
    conto, dettaglio, ignote = conta_per_dex([("a", False), ("a-f", False), ("ignoto", False)], per_id)
    prova("il conto somma le voci della stessa specie", 2, conto[1])
    prova("e la voce ignota non entra nel conto", ["ignoto"], ignote)
    conto_g, dettaglio_g, _ = conta_per_dex([("a", False), ("a", True)], per_id)
    prova("la casella gigamax non duplica la voce base ma si aggiunge", 2, conto_g[1])
    prova("e porta la classe della forma gigamax", True,
          any(classe_di(v) == "forma gigamax" for v in dettaglio_g[1]))
    prova("l'indizio nomina la classe e non la specie base", True,
          "1 forma femminile" in indizio_loro(list(per_id.values())))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="non scrive: dice soltanto se il documento sul disco sia allineato")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    per_id, errore = carica_specie(SPECIE)
    if errore:
        print("rifiutato: " + errore)
        return 1
    scelti, sorelle, errore = carica_disposizione(SCATOLE)
    if errore:
        print("rifiutato: " + errore)
        return 1

    fratello, errore = carica_fratello()
    if errore:
        print("rifiutato: " + errore)
        return 1
    nostro, escluse, errore = fratello.leggi_nostra(NOSTRA)
    if errore:
        print("rifiutato: " + errore)
        return 1

    conto_loro, dettaglio, ignote = conta_per_dex(scelti, per_id)
    testo = componi(conto_loro, dettaglio, nostro, escluse, ignote, sorelle)

    if a.check:
        vecchio = io.open(USCITA, encoding="utf-8").read() if os.path.exists(USCITA) else ""
        if vecchio != testo:
            print("disallineato: %s va rigenerato" % USCITA)
            return 1
        print("allineato: %s" % USCITA)
        return 0

    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    print("scritto %s" % USCITA)
    print("  voci di PokePC: %d | nostre: %d" % (sum(conto_loro.values()), sum(nostro.values())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
