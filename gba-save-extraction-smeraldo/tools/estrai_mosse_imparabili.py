#!/usr/bin/env python3
"""Estrae dal sorgente di pret/pokeemerald, per ogni specie, l'insieme completo delle mosse che puo' imparare e per quale via.

Perche' esiste
--------------

Il verificatore delle squadre del Parco Lotta dichiarava di non saper controllare se una mossa fosse imparabile dalla specie a cui la si attribuisce, e quel limite era corretto ma non sostenibile: una squadra il cui insieme di mosse non e' verificabile non e' una squadra, e' una proposta. La tabella che serve a chiudere quel limite non e' una fonte da procurarsi ma un dato che sta nel sorgente del gioco, in quattro file distinti, e questo strumento la porta su disco in una forma sola.

La ragione per cui le vie vanno tenute distinte e non fuse in un unico elenco e' che decidono la legittimita' e non solo la possibilita'. Una mossa di livello impone un livello minimo, e al Parco Lotta in modalita' cinquanta un livello superiore a cinquanta rende l'esemplare inammissibile: e' il vincolo che ha fatto cadere una prima versione del catalogo delle squadre. Una mossa da uovo impone invece un percorso di riproduzione, quindi nessun livello minimo ma una catena di genitori da dichiarare. Una macchina e un insegnamosse sono le vie piu' semplici, con la sola avvertenza che un insegnamosse in terza generazione si usa una volta sola per salvataggio.

La quinta via, quella che questo strumento calcola invece di leggere
---------------------------------------------------------------------

Esiste un caso che nessuno dei quattro file dichiara e che cambia la risposta su almeno un esemplare di questo progetto: una mossa di livello puo' arrivare a un esemplare appena nato, se entrambi i genitori la conoscono. La regola sta in `BuildEggMoveset` di `src/daycare.c` e va letta con attenzione, perche' la formulazione diffusa e' sbagliata: non basta che il padre la conosca, come in altre generazioni. Il codice raccoglie prima le mosse comuni a padre e madre, e poi da' al nato quelle fra queste che compaiono nel suo elenco di livello.

Ne segue che un Heracross di livello cinquanta puo' legittimamente conoscere Megahorn, che si impara al cinquantatre, purche' derivi da due genitori che entrambi la conoscono. Lo strumento marca quindi ogni mossa di livello anche come ereditabile, con il livello minimo che i genitori devono avere, cosicche' il verificatore possa distinguere fra una mossa impossibile e una che richiede soltanto una catena da dichiarare.

Uso
---

    python gba-save-extraction-smeraldo/tools/estrai_mosse_imparabili.py --sorgente <clone di pret/pokeemerald> --out gba-save-extraction-smeraldo/mosse-imparabili.json
"""

import argparse
import json
import re
import sys
from pathlib import Path


def nome(costante):
    """Da `MOVE_METEOR_MASH` a `Meteor Mash`, e da `SPECIES_HERACROSS` a `Heracross`."""
    pezzi = costante.split("_", 1)[1] if "_" in costante else costante
    return " ".join(p.capitalize() for p in pezzi.split("_"))


def livello_per_specie(radice):
    """Legge `level_up_learnsets.h` e il suo file di puntatori, che sono due e vanno incrociati.

    L'elenco per specie non porta il nome della specie: porta il nome di un array, e la corrispondenza fra array e specie sta nel secondo file. Leggere il solo primo darebbe elenchi corretti attribuiti alla specie sbagliata, che e' il genere di difetto che non si vede finche' qualcuno non prova a insegnare la mossa.
    """
    testo = radice.joinpath("src/data/pokemon/level_up_learnsets.h").read_text(encoding="utf-8")
    per_array = {}
    for blocco in re.finditer(r"static const u16 (\w+)\[\]\s*=\s*\{(.*?)\n\};", testo, re.S):
        voci = re.findall(r"LEVEL_UP_MOVE\(\s*(\d+)\s*,\s*(MOVE_\w+)\s*\)", blocco.group(2))
        per_array[blocco.group(1)] = [{"livello": int(l), "mossa": nome(m)} for l, m in voci]

    puntatori = radice.joinpath("src/data/pokemon/level_up_learnset_pointers.h").read_text(encoding="utf-8")
    fuori = {}
    for riga in re.finditer(r"\[(SPECIES_\w+)\]\s*=\s*(\w+)", puntatori):
        array = per_array.get(riga.group(2))
        if array is not None:
            fuori[nome(riga.group(1))] = array
    if len(fuori) < 300:
        sys.exit("elenchi di livello letti solo in parte: %d specie" % len(fuori))
    return fuori


def uova_per_specie(radice):
    testo = radice.joinpath("src/data/pokemon/egg_moves.h").read_text(encoding="utf-8")
    fuori = {}
    for blocco in re.finditer(r"egg_moves\((\w+)\s*,(.*?)\)\s*,", testo, re.S):
        mosse = re.findall(r"(MOVE_\w+)", blocco.group(2))
        fuori[nome("SPECIES_" + blocco.group(1))] = [nome(m) for m in mosse]
    return fuori


def macchine_per_specie(radice):
    """Legge `tmhm_learnsets.h`, dove ogni specie porta i nomi dei campi posti a vero.

    I nomi dei campi sono quelli delle mosse e non i numeri delle macchine, il che rende la lettura piu' semplice e piu' robusta: se una revisione del sorgente rinumerasse le macchine, questo codice continuerebbe a funzionare.
    """
    testo = radice.joinpath("src/data/pokemon/tmhm_learnsets.h").read_text(encoding="utf-8")
    fuori = {}
    for blocco in re.finditer(r"\[(SPECIES_\w+)\]\s*=\s*\{\s*\.learnset\s*=\s*\{(.*?)\}\s*\}", testo, re.S):
        campi = re.findall(r"\.(\w+)\s*=\s*TRUE", blocco.group(2))
        fuori[nome(blocco.group(1))] = [nome("X_" + c) for c in campi]
    if len(fuori) < 300:
        sys.exit("elenchi delle macchine letti solo in parte: %d specie" % len(fuori))
    return fuori


def insegnamosse_per_specie(radice):
    testo = radice.joinpath("src/data/pokemon/tutor_learnsets.h").read_text(encoding="utf-8")
    fuori = {}
    for blocco in re.finditer(r"\[(SPECIES_\w+)\]\s*=\s*\((.*?)\),\s*\n", testo, re.S):
        mosse = re.findall(r"TUTOR\((MOVE_\w+)\)", blocco.group(2))
        fuori[nome(blocco.group(1))] = [nome(m) for m in mosse]
    return fuori


def pre_evoluzioni(radice):
    """Ricava, per ogni specie, la catena delle sue forme precedenti.

    Serve perche' una specie conosce anche cio' che ha imparato prima di evolvere, e in almeno un caso di questo progetto e' la differenza fra una squadra ammissibile e una no: Metagross impara Meteor Mash al cinquantacinque, ma Metang la impara al cinquanta, e un Metang portato al cinquanta con l'evoluzione rimandata la impara e poi evolve. Un controllo che guardasse la sola specie finale dichiarerebbe illegittimo un esemplare che il gioco produce senza alcun artificio.
    """
    testo = radice.joinpath("src/data/pokemon/evolution.h").read_text(encoding="utf-8")
    successore = {}
    for riga in re.finditer(r"\[(SPECIES_\w+)\]\s*=\s*\{(.*?)\}\s*,\s*$", testo, re.S | re.M):
        partenza = nome(riga.group(1))
        for evo in re.finditer(r"\{\s*EVO_\w+\s*,\s*\d+\s*,\s*(SPECIES_\w+)\s*\}", riga.group(2)):
            successore.setdefault(partenza, []).append(nome(evo.group(1)))
    precedente = {}
    for prima, dopo in successore.items():
        for d in dopo:
            precedente.setdefault(d, []).append(prima)
    catene = {}
    for specie in set(list(precedente) + list(successore)):
        catena, corrente = [], specie
        while corrente in precedente:
            corrente = precedente[corrente][0]
            if corrente in catena:
                break
            catena.append(corrente)
        if catena:
            catene[specie] = catena
    return catene


def componi(radice):
    livello = livello_per_specie(radice)
    uova = uova_per_specie(radice)
    macchine = macchine_per_specie(radice)
    insegnate = insegnamosse_per_specie(radice)

    catene = pre_evoluzioni(radice)

    fuori = {}
    for specie, elenco in livello.items():
        vie = {}
        for v in elenco:
            vie.setdefault(v["mossa"], {})["livello"] = v["livello"]
            # La quinta via: una mossa di livello arriva anche a un nato, se ENTRAMBI i genitori la conoscono.
            # Da `BuildEggMoveset` in `src/daycare.c`. E' cio' che consente a un esemplare di livello cinquanta
            # di conoscere una mossa che si imparerebbe piu' tardi, senza superare il tetto d'iscrizione.
            vie[v["mossa"]]["eredita_da_due_genitori_di_livello"] = v["livello"]
        for m in uova.get(specie, []):
            vie.setdefault(m, {})["uovo"] = True
        for m in macchine.get(specie, []):
            vie.setdefault(m, {})["macchina"] = True
        for m in insegnate.get(specie, []):
            vie.setdefault(m, {})["insegnamosse"] = True
        # Cio' che una forma precedente sapeva imparare resta noto dopo l'evoluzione, e a un livello che
        # puo' essere piu' basso di quello della forma finale. Si tiene il piu' basso fra i due, con il nome
        # della forma da cui viene, perche' chi legge deve sapere che quell'esemplare va cresciuto senza
        # far evolvere prima del tempo.
        for prima in catene.get(specie, []):
            for v in livello.get(prima, []):
                voce = vie.setdefault(v["mossa"], {})
                if "livello" not in voce or v["livello"] < voce["livello"]:
                    voce["livello"] = v["livello"]
                    voce["da_forma_precedente"] = prima
                    voce["eredita_da_due_genitori_di_livello"] = min(v["livello"], voce.get("eredita_da_due_genitori_di_livello", v["livello"]))
            for m in macchine.get(prima, []):
                vie.setdefault(m, {})["macchina"] = True
            for m in insegnate.get(prima, []):
                vie.setdefault(m, {})["insegnamosse"] = True
            for m in uova.get(prima, []):
                vie.setdefault(m, {})["uovo"] = True
        fuori[specie] = vie
    return fuori


def indici_di_specie(radice):
    """Mappa l'indice interno di specie al nome, da `include/constants/species.h`.

    L'indice interno non e' il numero del Pokedex nazionale e confonderli produce nomi sbagliati senza alcun errore: le specie di Hoenn cominciano al duecentosettantasette e non al duecentocinquantadue, quindi un salvataggio letto con la numerazione del Pokedex attribuirebbe a ogni esemplare di Hoenn la specie di un altro. E' l'indice interno quello che sta nel record del deposito, ed e' questo che serve.
    """
    testo = radice.joinpath("include/constants/species.h").read_text(encoding="utf-8")
    fuori = {}
    for riga in re.finditer(r"^#define (SPECIES_\w+)\s+(\d+)\s*$", testo, re.M):
        etichetta, indice = riga.group(1), int(riga.group(2))
        if etichetta.endswith("_COUNT") or etichetta == "SPECIES_NONE":
            continue
        fuori.setdefault(str(indice), nome(etichetta))
    if len(fuori) < 380:
        sys.exit("indici di specie letti solo in parte: %d voci" % len(fuori))
    return fuori


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--sorgente", required=True, help="cartella di un clone di pret/pokeemerald")
    p.add_argument("--out", required=True)
    p.add_argument("--out-specie", help="dove scrivere la mappa fra indice interno di specie e nome")
    args = p.parse_args()

    radice = Path(args.sorgente)
    if not radice.joinpath("src/data/pokemon/level_up_learnsets.h").exists():
        sys.exit("sorgente non trovato in %s: serve un clone di pret/pokeemerald" % radice)

    dati = componi(radice)
    Path(args.out).write_text(json.dumps(dati, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    mosse = sum(len(v) for v in dati.values())
    print("%d specie, %d coppie specie-mossa" % (len(dati), mosse))
    for specie in ("Heracross", "Metagross", "Blissey"):
        if specie in dati:
            print("  %-12s %d mosse imparabili" % (specie, len(dati[specie])))
    if args.out_specie:
        indici = indici_di_specie(radice)
        Path(args.out_specie).write_text(json.dumps(indici, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
        print("%d indici di specie in %s" % (len(indici), args.out_specie))
    print("uscita in %s" % args.out)


if __name__ == "__main__":
    main()
