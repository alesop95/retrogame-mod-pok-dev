#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confronta le forme elencate nei fogli di calcolo del corpus con le voci della lista completa.

Perché esiste
-------------
Fra i collegamenti del corpus della collezione letti il 2026-10-01 ci sono 25 fogli di calcolo, quasi tutti tracciatori
di living dex, che insieme pesano dodici megabyte. Passarli a un modello per estrarne affermazioni sarebbe lento e poco
utile, perché il loro contenuto non è prosa ma una griglia di specie e forme. La domanda che pongono è deterministica:
c'è una forma che qualcuno conta e noi no? Questo strumento la pone riga per riga.

Che cosa fa
-----------
Per ogni riga di un foglio cerca una cella che sia il nome inglese di una specie, dalla tabella dei nomi della libreria,
e prende come etichetta di forma le celle di testo accanto, scartando numeri, segni di spunta e nomi di gioco. Confronta
l'etichetta, normalizzata, con i nomi inglesi delle forme di quella specie nel dataset di PokePC, che è la base di
`LISTA-COMPLETA.md`. Scrive in `_notes/fonti/corpus-residuo/fogli-forme-ignote.md` le coppie specie ed etichetta che
non trovano riscontro, con il numero di fogli che le citano: conta come forma solo un'etichetta con una parola del vocabolario delle forme
del dataset; le citate da più fogli sono le candidate da verificare a mano. È un filtro e non un giudizio: il riscontro si fa sulla fonte.

Uso
---
    python tools/confronta-fogli-corpus.py
"""

import collections
import glob
import io
import json
import os
import re

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA = os.path.join(RADICE, "_notes", "fonti", "corpus-residuo")
SCHEDE = os.path.join(RADICE, "_notes", "fonti", "cloni", "pokepc-dataset", "data", "pokemon")
NOMI_EN = os.path.join(RADICE, "_notes", "fonti", "cloni", "pkhex", "PKHeX.Core", "Resources", "text", "other", "en",
                       "text_Species_en.txt")
# Le celle che non sono forme: segni di spunta, sessi, versioni, colonne di stato dei tracciatori.
RUMORE = re.compile(r"^(true|false|none|yes|no|x|y|n|i|ii|iii|iv|v|vi|vii|viii|ix|male|m|f|gen ?\d|generation \d|"
                    r"caught|owned|seen|have|need|done|shiny|normal|default|regular|base|standard|-|\?|"
                    r"(red|blue|yellow|gold|silver|crystal|ruby|sapphire|emerald|firered|leafgreen|diamond|pearl|platinum|"
                    r"heartgold|soulsilver|black|white|x|y|sun|moon|sword|shield|scarlet|violet|home|bank|go|lgpe|bdsp|pla|"
                    r"usum|oras|swsh|sv)( ?2| version)?)$", re.I)


def norma(s):
    s = s.lower().replace("’", "'").replace("é", "e")
    s = re.sub(r"\b(form|forme|style|mode|pattern|flower|cloak|breed|size|sea|plumage|color|colour|face|core|trim)\b", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def main():
    nomi = [r.rstrip("\r") for r in io.open(NOMI_EN, encoding="utf-8").read().split("\n")]
    per_nome = {n.lower(): i for i, n in enumerate(nomi) if i and n}
    forme = collections.defaultdict(set)
    for f in glob.glob(os.path.join(SCHEDE, "*.json")):
        v = json.load(io.open(f, encoding="utf-8"))
        if not 1 <= v.get("dexNum", 0) <= 1025:
            continue
        eng = (v.get("formNames") or {}).get("eng") or ""
        forme[v["dexNum"]].add(norma(eng))
        forme[v["dexNum"]].add(norma(v["id"].split("-", 1)[1] if "-" in v["id"] else ""))
        if v.get("isFemaleForm"):
            forme[v["dexNum"]].add("female")
    # Il vocabolario delle forme: ogni parola che compare nel nome inglese di una forma del dataset. Un'etichetta che
    # non ne contiene nessuna è un soprannome, una nota o una colonna di servizio, come i nomi degli scambi in gioco.
    vocabolario = set()
    for f in glob.glob(os.path.join(SCHEDE, "*.json")):
        eng = ((json.load(io.open(f, encoding="utf-8")).get("formNames") or {}).get("eng") or "")
        vocabolario |= {w for w in re.findall(r"[a-z]+", eng.lower()) if len(w) > 2 and w not in ("the", "and", "form")}
    # I tipi vengono dalle forme di Arceus e Silvally, che dipendono dall'oggetto tenuto: non distinguono una voce.
    vocabolario -= {"normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying",
                    "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy", "pok", "mon", "pokemon",
                    "any", "random", "box", "type", "null"}
    vocabolario |= {"female", "alolan", "galarian", "hisuian", "paldean", "forme", "cap", "origin", "therian"}
    elenco = [l.strip() for l in io.open(os.path.join(CARTELLA, "fogli.txt"), encoding="utf-8") if l.strip()]
    citazioni = collections.defaultdict(set)
    righe_viste = 0
    for nome_file in elenco:
        testo = io.open(os.path.join(CARTELLA, "testi", nome_file + ".md"), encoding="utf-8", errors="replace").read()
        for riga in testo.splitlines():
            celle = [c.strip() for c in riga.split(" | ")]
            for i, c in enumerate(celle):
                dex = per_nome.get(c.lower())
                if not dex:
                    continue
                righe_viste += 1
                for altra in celle[i + 1:i + 4]:
                    if not altra or re.fullmatch(r"[\d.,%/#: -]+", altra) or RUMORE.match(altra) or altra.lower() in per_nome:
                        continue
                    if len(altra) > 40:
                        continue
                    if altra.endswith(".") or "★" in altra:
                        continue
                    if not set(re.findall(r"[a-z]+", altra.lower())) & vocabolario:
                        continue
                    n = norma(altra)
                    if not n or any(n in k or k in n for k in forme[dex] if k):
                        continue
                    citazioni[(dex, altra.strip())].add(nome_file)
                break
    candidate = sorted(citazioni.items(), key=lambda x: (-len(x[1]), x[0][0]))
    r = ["# Forme dei fogli del corpus senza riscontro nella lista completa", "",
         "> Generato da `tools/confronta-fogli-corpus.py`. Filtro e non giudizio: ogni candidata si verifica sulla fonte.", "",
         "Fogli esaminati: %d. Righe con un nome di specie: %d. Coppie senza riscontro: %d, di cui %d citate da almeno due fogli." % (
             len(elenco), righe_viste, len(candidate), sum(1 for _, s in candidate if len(s) >= 2)), "",
         "| Dex | Specie | Etichetta nel foglio | Fogli |", "|---|---|---|---|"]
    for (dex, etichetta), fogli in candidate:
        r.append("| %d | %s | %s | %d |" % (dex, nomi[dex], etichetta.replace("|", "/"), len(fogli)))
    io.open(os.path.join(CARTELLA, "fogli-forme-ignote.md"), "w", encoding="utf-8").write("\n".join(r) + "\n")
    print("righe", righe_viste, "candidate", len(candidate), "da almeno due fogli", sum(1 for _, s in candidate if len(s) >= 2))


if __name__ == "__main__":
    main()
