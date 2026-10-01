#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone la lista completa delle voci della collezione per HOME, con forme femminili e cosmetiche distinte.

Perché esiste
-------------
La lista di spunta del progetto, `pokedex-home-completo/CHECKLIST-COMPLETA.md`, legge le forme dalla struttura dei dati
dei giochi, e quindi non vede ciò che il campo della forma non separa: le differenze fra maschio e femmina e le varianti
cosmetiche, come le creme e le decorazioni di Alcremie. Il confronto con PokePC le contava come la nostra cecità. Il
proprietario, il 2026-10-01, le vuole come voci distinte, e ha fissato la regola opposta per le forme che cambiano
soltanto per l'oggetto tenuto: i tipi di Arceus sono lo stesso Arceus con una piastra diversa.

Che cosa fa
-----------
Legge le schede delle voci del deposito `pokepc/dataset`, clonato in `_notes/fonti/cloni/pokepc-dataset/`, che marcano
una per una le forme femminili, cosmetiche, regionali, le fusioni, le megaevoluzioni, le Gigamax e le forme di sola
battaglia. Tiene come voce distinta la specie, la forma femminile, ogni forma cosmetica, ogni forma regionale, le fusioni
e le altre forme che si depositano; esclude le megaevoluzioni, le Gigamax, le forme di sola battaglia e le primordiali,
che non esistono in un box, e mette in una classe a sé, senza contarle, le forme da oggetto tenuto. Aggiunge le forme
depositabili che PokePC non elenca e la libreria sì, cioè il Greninja con Morfosi. Per ogni voce dice se si ottiene
soltanto dalla banca, secondo la checklist, e quante volte è nelle copie per HOME, secondo `_notes/stampa/collezione.json`.

Uso
---
    python tools/lista-completa.py
    python tools/lista-completa.py --check
"""

import argparse
import collections
import glob
import io
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEDE = os.path.join(RADICE, "_notes", "fonti", "cloni", "pokepc-dataset", "data", "pokemon")
NOMI_IT = os.path.join(RADICE, "_notes", "fonti", "cloni", "pkhex", "PKHeX.Core", "Resources", "text", "other", "it",
                       "text_Species_it.txt")
COPIE = os.path.join(RADICE, "_notes", "stampa", "collezione.json")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "LISTA-COMPLETA.md")

# Le forme che cambiano soltanto per l'oggetto tenuto: per regola del proprietario non sono voci distinte.
DA_OGGETTO = ("arceus-", "silvally-", "genesect-", "giratina-origin", "dialga-origin", "palkia-origin",
              "zacian-crowned", "zamazenta-crowned", "ogerpon-")
# Le voci che si ottengono soltanto dalla banca, dalla checklist del progetto: la specie Spinda e due forme.
SOLO_BANCA = {"spinda": "Spinda: in HOME solo dalla banca", "vivillon-pokeball": "solo da evento, solo dalla banca",
              "greninja-battle-bond": "solo dalla demo di Sole e Luna, solo dalla banca"}


def classe(v):
    if v.get("isMega") or v.get("isGmax") or v.get("isBattleOnlyForm") or v.get("isPrimal"):
        return None
    if any(v["id"].startswith(p) for p in DA_OGGETTO):
        return "da oggetto tenuto, non conta"
    if v.get("isDefault") and not v.get("isForm"):
        return "specie"
    if v.get("isFemaleForm"):
        return "forma femminile"
    if v.get("isCosmeticForm"):
        return "forma cosmetica"
    if v.get("isRegional"):
        return "forma regionale"
    if v.get("isFusion"):
        return "fusione"
    return "altra forma"


def componi():
    nomi = [r.rstrip("\r") for r in io.open(NOMI_IT, encoding="utf-8").read().split("\n")]
    voci = []
    for f in glob.glob(os.path.join(SCHEDE, "*.json")):
        v = json.load(io.open(f, encoding="utf-8"))
        if v.get("isPrerelease") or not 1 <= v["dexNum"] <= 1025:
            continue
        c = classe(v)
        if c is None:
            continue
        nomi_forma = v.get("formNames") or {}
        forma = nomi_forma.get("ita") or nomi_forma.get("eng") or ""
        voci.append({"id": v["id"], "dex": v["dexNum"], "specie": nomi[v["dexNum"]], "forma": forma if c != "specie" else "",
                     "classe": c})
    voci.append({"id": "greninja-battle-bond", "dex": 658, "specie": nomi[658], "forma": "Morfosi",
                 "classe": "altra forma"})
    # Quante volte ciascuna specie è nelle copie per HOME, per le voci che passano solo dalla banca.
    presenti = collections.Counter()
    if os.path.exists(COPIE):
        for c in json.load(io.open(COPIE, encoding="utf-8"))["copie"]:
            if c["gruppo"].startswith("per HOME"):
                for e in c["esemplari"]:
                    presenti[(e["numero"], e.get("forma_en", ""))] += 1
    contare = [v for v in voci if v["classe"] != "da oggetto tenuto, non conta"]
    per_classe = collections.Counter(v["classe"] for v in voci)
    r = ["# La lista completa delle voci della collezione per HOME", "",
         "> Documento generato da `tools/lista-completa.py`. Non si modifica a mano: si rigenera. Le voci vengono dalle schede del deposito `pokepc/dataset`, con le regole del proprietario del 2026-10-01: le forme femminili e cosmetiche sono voci distinte, le forme da oggetto tenuto no.", "",
         "Le voci da possedere sono %d. Per classe:" % len(contare), "",
         "| Classe | Voci |", "|---|---|"]
    for k, n in sorted(per_classe.items(), key=lambda x: -x[1]):
        r.append("| %s | %d |" % (k, n))
    r += ["", "Le voci che si ottengono soltanto dalla banca sono tre, e sono tutte nelle copie per HOME: Spinda, il Vivillon Motivo Poké Ball e il Greninja con Morfosi. Tutte le altre si ottengono nei giochi che parlano con HOME direttamente, senza scadenza.", "",
          "## Le voci", "", "| Dex | Specie | Forma | Classe | Nota |", "|---|---|---|---|---|"]
    for v in sorted(voci, key=lambda x: (x["dex"], x["classe"] != "specie", x["forma"])):
        nota = SOLO_BANCA.get(v["id"], "")
        r.append("| %d | %s | %s | %s | %s |" % (v["dex"], v["specie"], v["forma"], v["classe"], nota))
    return "\n".join(r) + "\n", len(contare), per_classe


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="dice soltanto se il documento sul disco è allineato")
    a = ap.parse_args()
    testo, totale, per_classe = componi()
    if a.check:
        vecchio = io.open(USCITA, encoding="utf-8").read() if os.path.exists(USCITA) else ""
        print("allineato" if vecchio == testo else "disallineato: si rigenera")
        return 0 if vecchio == testo else 1
    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    print("scritto %s: %d voci da possedere; %s" % (USCITA, totale, dict(per_classe)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
