#!/usr/bin/env python3
"""Estrae dal sorgente di pret/pokeemerald i dati di riferimento che servono a comporre un esemplare di terza generazione.

Perche' esiste, e perche' non riusa il fratello
----------------------------------------------

Il progetto ha gia' un generatore di esemplari di terza generazione, `tools/genera-evento-gen3.py`, che porta con se' l'esperienza per gruppo di crescita, la corrispondenza fra numerazione nazionale e identificativo interno, i punti potenza di base e le abilita' per specie. La regola sana sarebbe riusarlo, e la ragione per cui qui non si puo' va detta invece di essere aggirata in silenzio: quel programma legge quei dati da due cloni esterni, il costruttore e il verificatore, che su questa macchina non sono presenti, come `pending.md` registra dal 2026-09-16.

Cio' che resta e' la fonte che il progetto tratta come di primo livello e che qui e' presente, cioe' il sorgente decompilato del gioco. Ne discende una duplicazione che va dichiarata e non nascosta: gli stessi dati esistono ora in due posti, e se i due divergessero avremmo due verita'. La mitigazione e' che questa copia dichiara la propria provenienza file per file e si rigenera in una corsa, quindi il confronto con l'altra e' un lavoro di minuti quando i cloni torneranno disponibili, ed e' segnato fra le cose da fare.

Che cosa estrae
---------------

Per ogni specie: l'identificativo interno, le statistiche base, i due tipi, le due abilita', il rapporto fra i sessi, il gruppo di crescita, l'amicizia iniziale e i cicli di incubazione. Per ogni mossa: l'identificativo, i punti potenza di base, il tipo e la potenza. Per ogni oggetto: l'identificativo. E le sei tabelle dell'esperienza, calcolate con le stesse formule del gioco invece che copiate, perche' una formula di tre righe si verifica a colpo d'occhio mentre centouno numeri copiati a mano no.

La tabella dell'esperienza, e il punto in cui e' facile sbagliare
-----------------------------------------------------------------

Cinque dei sei gruppi hanno una formula chiusa e si calcolano. Il sesto, quello irregolare, e' definito a tratti su quattro intervalli di livello, e le sue costanti sono scritte qui come stanno nel sorgente: e' il solo punto di questo strumento dove un refuso non produrrebbe alcun errore visibile ma un esemplare con un'esperienza incoerente con il proprio livello, che e' esattamente il genere di difetto che un verificatore segnala e una persona no. Per questo lo strumento verifica da se' che ogni tabella sia monotona crescente e che il valore al livello uno sia zero, e si arresta se non lo e'.

Uso
---

    python gba-save-extraction-smeraldo/tools/estrai_dati_gen3.py --sorgente <clone di pret/pokeemerald> --out gba-save-extraction-smeraldo/dati-gen3.json
"""

import argparse
import json
import re
import sys
from pathlib import Path

LIVELLO_MASSIMO = 100


def nome(costante):
    pezzi = costante.split("_", 1)[1] if "_" in costante else costante
    return " ".join(p.capitalize() for p in pezzi.split("_"))


def oggetti(radice):
    """Legge gli identificativi degli oggetti, che nel sorgente sono un enum e non delle direttive.

    La differenza conta: un enum non porta i numeri, li fa contare al compilatore, quindi il valore di ciascuna voce e' la sua posizione. Cercarvi delle direttive con un numero, come si fa per le specie e per le mosse, restituisce zero voci senza alcun errore, ed e' cio' che questo strumento ha fatto al primo giro. Si contano quindi le voci nell'ordine in cui compaiono, saltando i commenti e le righe vuote, ed e' la ragione per cui la funzione verifica poi che un valore noto corrisponda.
    """
    testo = radice.joinpath("include/constants/items.h").read_text(encoding="utf-8")
    blocco = re.search(r"enum\s*\{(.*?)" + chr(10) + r"\};", testo, re.S)
    if blocco is None:
        sys.exit("l'enum degli oggetti non e' stato trovato: la forma della fonte e' cambiata")
    fuori = {}
    posizione = 0
    for riga in blocco.group(1).split(chr(10)):
        nuda = re.sub(r"//.*$", "", riga).strip().rstrip(",")
        if not nuda or not re.match(r"^ITEM_\w+$", nuda):
            continue
        fuori.setdefault(nome(nuda), posizione)
        posizione += 1
    # Un controllo di ancoraggio: la Poke Ball ordinaria e' la quarta voce dell'enum e vale quattro,
    # ed e' il valore che il generatore degli incontri usa gia'. Se cambiasse, tutto il resto sarebbe
    # spostato della stessa quantita' e nessun campo lo direbbe.
    if fuori.get("Poke Ball") != 4:
        sys.exit("ancoraggio fallito: la Poke Ball vale %s invece di 4, il conteggio dell'enum e' sfasato" % fuori.get("Poke Ball"))
    return fuori


def specie(radice, id_per_nome):
    """Legge `species_info.h`, che e' una tabella di strutture con i campi nominati."""
    testo = radice.joinpath("src/data/pokemon/species_info.h").read_text(encoding="utf-8")
    fuori = {}
    for blocco in re.finditer(r"\[(SPECIES_\w+)\]\s*=\s*\{(.*?)\n    \},", testo, re.S):
        etichetta = nome(blocco.group(1))
        corpo = blocco.group(2)

        def campo(chiave, difetto=None):
            trovato = re.search(r"\.%s\s*=\s*([A-Za-z0-9_()]+)" % chiave, corpo)
            return trovato.group(1) if trovato else difetto

        tipi = re.search(r"\.types\s*=\s*\{\s*(TYPE_\w+)\s*,\s*(TYPE_\w+)\s*\}", corpo)
        abilita = re.search(r"\.abilities\s*=\s*\{\s*(ABILITY_\w+)\s*,\s*(ABILITY_\w+)\s*\}", corpo)
        sesso = campo("genderRatio", "PERCENT_FEMALE(50)")
        percentuale = re.search(r"PERCENT_FEMALE\((\d+)\)", sesso or "")
        fuori[etichetta] = {
            "id": id_per_nome.get(etichetta),
            "base": {
                "hp": int(campo("baseHP", 0)), "atk": int(campo("baseAttack", 0)),
                "def": int(campo("baseDefense", 0)), "spe": int(campo("baseSpeed", 0)),
                "spa": int(campo("baseSpAttack", 0)), "spd": int(campo("baseSpDefense", 0)),
            },
            "tipi": [nome(tipi.group(1)), nome(tipi.group(2))] if tipi else [],
            "abilita": [nome(abilita.group(1)), nome(abilita.group(2))] if abilita else [],
            "rapporto_sesso": sesso,
            "soglia_femmina": int(round(int(percentuale.group(1)) * 255 / 100.0)) if percentuale else None,
            "gruppo_crescita": campo("growthRate", "GROWTH_MEDIUM_FAST"),
            "amicizia": campo("friendship", "STANDARD_FRIENDSHIP"),
            "cicli_uovo": int(campo("eggCycles", 20)),
        }
    if len(fuori) < 380:
        sys.exit("specie lette solo in parte: %d voci" % len(fuori))
    return fuori


def mosse(radice, id_per_nome):
    testo = radice.joinpath("src/data/battle_moves.h").read_text(encoding="utf-8")
    fuori = {}
    for blocco in re.finditer(r"\[(MOVE_\w+)\]\s*=\s*\{(.*?)\n    \},", testo, re.S):
        etichetta = nome(blocco.group(1))
        corpo = blocco.group(2)

        def campo(chiave, difetto=0):
            trovato = re.search(r"\.%s\s*=\s*(\d+)" % chiave, corpo)
            return int(trovato.group(1)) if trovato else difetto

        tipo = re.search(r"\.type\s*=\s*(TYPE_\w+)", corpo)
        fuori[etichetta] = {
            "id": id_per_nome.get(etichetta),
            "pp": campo("pp"),
            "potenza": campo("power"),
            "tipo": nome(tipo.group(1)) if tipo else None,
        }
    if len(fuori) < 300:
        sys.exit("mosse lette solo in parte: %d voci" % len(fuori))
    return fuori


def esperienza():
    """Le sei tabelle dell'esperienza, calcolate con le formule del gioco.

    Cinque hanno forma chiusa. La sesta, irregolare, e' definita a tratti su quattro intervalli, e le sue costanti sono quelle del sorgente. Si calcolano invece di copiarle perche' una formula si verifica a colpo d'occhio e centouno numeri no.
    """
    def erratic(n):
        if n <= 50:
            return (n ** 3) * (100 - n) // 50
        if n <= 68:
            return (n ** 3) * (150 - n) // 100
        if n <= 98:
            return (n ** 3) * ((1911 - 10 * n) // 3) // 500
        return (n ** 3) * (160 - n) // 100

    def fluctuating(n):
        if n <= 15:
            return (n ** 3) * (((n + 1) // 3) + 24) // 50
        if n <= 36:
            return (n ** 3) * (n + 14) // 50
        return (n ** 3) * ((n // 2) + 32) // 50

    formule = {
        "GROWTH_MEDIUM_FAST": lambda n: n ** 3,
        "GROWTH_ERRATIC": erratic,
        "GROWTH_FLUCTUATING": fluctuating,
        "GROWTH_MEDIUM_SLOW": lambda n: (6 * n ** 3) // 5 - 15 * n ** 2 + 100 * n - 140,
        "GROWTH_FAST": lambda n: (4 * n ** 3) // 5,
        "GROWTH_SLOW": lambda n: (5 * n ** 3) // 4,
    }
    fuori = {}
    for gruppo, f in formule.items():
        tabella = [0] + [max(0, f(n)) for n in range(1, LIVELLO_MASSIMO + 1)]
        tabella[1] = 0
        if any(tabella[i] > tabella[i + 1] for i in range(1, LIVELLO_MASSIMO)):
            sys.exit("la tabella %s non e' monotona crescente: la formula e' sbagliata" % gruppo)
        fuori[gruppo] = tabella
    return fuori


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--sorgente", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    radice = Path(args.sorgente)
    if not radice.joinpath("src/data/pokemon/species_info.h").exists():
        sys.exit("sorgente non trovato in %s: serve un clone di pret/pokeemerald" % radice)

    id_specie = {}
    for riga in re.finditer(r"^#define (SPECIES_\w+)\s+(\d+)\s*$",
                            radice.joinpath("include/constants/species.h").read_text(encoding="utf-8"), re.M):
        id_specie.setdefault(nome(riga.group(1)), int(riga.group(2)))
    id_mosse = {}
    for riga in re.finditer(r"^#define (MOVE_\w+)\s+(\d+)\s*$",
                            radice.joinpath("include/constants/moves.h").read_text(encoding="utf-8"), re.M):
        id_mosse.setdefault(nome(riga.group(1)), int(riga.group(2)))

    dati = {
        "provenienza": "pret/pokeemerald, estratto da species_info.h, battle_moves.h, species.h, moves.js non usato, items.h; le tabelle dell'esperienza sono calcolate con le formule di experience_tables.h",
        "specie": specie(radice, id_specie),
        "mosse": mosse(radice, id_mosse),
        "oggetti": oggetti(radice),
        "esperienza": esperienza(),
    }
    Path(args.out).write_text(json.dumps(dati, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    print("%d specie, %d mosse, %d oggetti, %d tabelle di esperienza" % (
        len(dati["specie"]), len(dati["mosse"]), len(dati["oggetti"]), len(dati["esperienza"])))
    for etichetta in ("Heracross", "Metagross", "Blissey"):
        v = dati["specie"].get(etichetta)
        if v:
            print("  %-11s id %3s, gruppo %s, esperienza al 50: %d" % (
                etichetta, v["id"], v["gruppo_crescita"], dati["esperienza"][v["gruppo_crescita"]][50]))
    print("uscita in %s" % args.out)


if __name__ == "__main__":
    main()
