#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Studia quali giochi per Switch servono a ottenere le voci della lista completa, in che ordine comprarli, e dove e
come si ottiene ciascuna voce.

Perché esiste
-------------
Il 2026-10-01 il proprietario ha a disposizione una Switch 2, con il solo Leggende Pokémon Z-A, e vuole ottenere sulle
console moderne tutto ciò che vi si ottiene legittimamente. La domanda ha una risposta deterministica, perché la
libreria del verificatore conosce ogni incontro di ogni gioco per Switch con la versione, il metodo e il luogo: sono
gli stessi incontri con cui giudica un esemplare. `tools/pkhex-incontri-switch` li scrive in `_notes/incontri-switch.json`.

Che cosa fa
-----------
Prende le voci della lista completa dal dataset di PokePC, con le regole di `tools/lista-completa.py`, e le collega agli
incontri della libreria per specie e forma; le forme femminili e le varianti che la libreria non tiene come forma, come
le decorazioni di Alcremie, seguono la forma che le porta. Tiene soltanto gli incontri che la libreria, rigenerato l'esemplare con la specie e la forma cercate, giudica legali, e scarta gli incontri a tempo, cioè doni segreti, raid e
focolai di distribuzione e raid a sette stelle, che oggi non si giocano più. Riconosce dal luogo gli incontri dei
contenuti scaricabili e li attribuisce a un prodotto a parte, che richiede il gioco base della stessa versione. Calcola
un ordine di acquisto goloso, a partire da Leggende Z-A posseduto, e per ogni voce sceglie la via migliore nel primo
prodotto dell'ordine che la dà, preferendo la cattura alla schiusa e la schiusa all'evoluzione. Le voci che nessun gioco
per Switch dà si cercano in Pokémon GO e nei regali di HOME dal dataset di PokePC, e poi nelle copie del progetto.
Scrive `pokedex-home-completo/STUDIO-SWITCH.md`.

Uso
---
    python tools/studio-switch.py
"""

import collections
import glob
import importlib.util
import io
import json
import os
import re

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEDE = os.path.join(RADICE, "_notes", "fonti", "cloni", "pokepc-dataset", "data", "pokemon")
INCONTRI = os.path.join(RADICE, "_notes", "incontri-switch.json")
COPIE = os.path.join(RADICE, "_notes", "stampa", "collezione.json")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "STUDIO-SWITCH.md")

spec = importlib.util.spec_from_file_location("lista", os.path.join(RADICE, "tools", "lista-completa.py"))
lista = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lista)

A_TEMPO = {"EncounterDist9", "EncounterMight9", "EncounterOutbreak9", "EncounterStatic8ND"}
DLC_SV = re.compile(r"Kitakami|Apple Hills|Reveler|Oni |Oni's|Infernal Pass|Crystal Pool|Wistful Fields|Mossfell|Fellhorn|"
                    r"Paradise Barrens|Timeless Woods|Chilling Waterhead|Loyalty Plaza|Mossui|Savanna Biome|Coastal Biome|"
                    r"Canyon Biome|Polar Biome|Blueberry|Terarium|Underdepths|Central Plaza|Dreaded Den")
DLC_SWSH = re.compile(r"Fields of Honor|Soothing Wetlands|Forest of Focus|Challenge Beach|Brawlers|Challenge Road|"
                      r"Courageous Cavern|Loop Lagoon|Training Lowlands|Warm-Up Tunnel|Potbottom|Workout Sea|Stepping-Stone|"
                      r"Insular Sea|Honeycalm|Master Dojo|Tower of|Isle of Armor|Slippery Slope|Freezington|Frostpoint|"
                      r"Giant's Bed|Old Cemetery|Snowslide|Tunnel to the Top|Path to the Peak|Crown Shrine|Giant's Foot|"
                      r"Roaring-Sea|Frigid Sea|Three-Point|Ballimere|Lakeside Cave|Dyna Tree|Max Lair|Crown Tundra")
# Il DLC Mega Dimension di Leggende Z-A si riconosce dai luoghi dell'iperspazio e di Quasartico Inc., verificato il
# 2026-10-01 sul dono di Magearna (missione «Restarting Magearna», Game8 e Dexerto).
DLC_ZA = re.compile(r"Hyperspace|Quasartico")
NOMI_EN = os.path.join(RADICE, "_notes", "fonti", "cloni", "pkhex", "PKHeX.Core", "Resources", "text", "other", "en",
                       "text_Species_en.txt")
BASE = {"ZA": "Leggende Pokémon Z-A", "SL": "Scarlatto", "VL": "Violetto", "SW": "Spada", "SH": "Scudo",
        "BD": "Diamante Lucente", "SP": "Perla Splendente", "PLA": "Leggende Pokémon Arceus", "GP": "Let's Go Pikachu",
        "GE": "Let's Go Eevee"}
DLC = {"ZA": "DLC di Leggende Z-A (Mega Dimension)", "SL": "DLC di Scarlatto (Il tesoro dell'Area Zero)", "VL": "DLC di Violetto (Il tesoro dell'Area Zero)",
       "SW": "DLC di Spada (L'isola solitaria dell'armatura e Le terre innevate della corona)",
       "SH": "DLC di Scudo (L'isola solitaria dell'armatura e Le terre innevate della corona)"}
POSSEDUTI = {"ZA"}
# Il rifiuto per «Memory» è un artefatto della ricostruzione: doni e scambi in gioco portano un ricordo che il gioco
# assegna e che l'esemplare costruito fuori contesto non ha. Il caso che lo ha mostrato è Floette Fiore Eterno, dono
# di trama di Leggende Z-A a Lumiose, scartato il 2026-10-01 e riammesso lo stesso giorno.
# Le evoluzioni con una condizione che la simulazione del giudizio non riproduce: la libreria trova l'incontro della
# pre-evoluzione, ma l'esemplare evoluto costruito cambiando la specie non passa. Si accettano con la condizione scritta.
EVOLUZIONI_SPECIALI = {(367, 0): "scambio con Dente Abissale", (368, 0): "scambio con Squama Abissale",
                       (982, 1): "tre segmenti solo per una parte degli esemplari, decisa dalla chiave di crittazione",
                       (1000, 0): "raccogliere 999 Monete di Gimmighoul", (1019, 0): "conoscere Vocedrago (Dragon Cheer)"}
METODO = {"Slot": "selvatico", "Static": "incontro fisso", "Fixed": "incontro fisso", "Tera9": "raid Teracristal",
          "Static8N": "raid Dynamax in una tana", "Static8NC": "raid Dynamax da Cristallo", "Static8U": "Avventura Dynamax",
          "Egg": "uovo", "Trade": "scambio in gioco", "Gift": "dono in gioco"}
RANGO = {"selvatico": 0, "incontro fisso": 0, "dono in gioco": 0, "raid Teracristal": 1, "raid Dynamax in una tana": 1,
         "raid Dynamax da Cristallo": 1, "Avventura Dynamax": 1, "scambio in gioco": 1, "uovo": 2}


def metodo_di(classe):
    nome = re.sub(r"^Encounter|[0-9]+[a-z]?$", "", classe)
    for k, v in METODO.items():
        if classe.replace("Encounter", "").startswith(k):
            return v
    return nome


def norma(s):
    s = s.lower().replace("é", "e")
    s = re.sub(r"\b(form|forme|style|mode|pattern|cloak|breed|size|plumage|color|colour|core|trim|flower|sweet|cream)\b", "", s)
    s = s.replace("alolan", "alola").replace("galarian", "galar").replace("hisuian", "hisui").replace("paldean", "paldea")
    return re.sub(r"[^a-z0-9]+", "", s)


def main():
    nomi = [r.rstrip("\r") for r in io.open(lista.NOMI_IT, encoding="utf-8").read().split("\n")]
    # Il nome inglese accanto all'italiano quando differiscono: per le specie recenti il solo nome italiano non si
    # riconosce a colpo d'occhio, e il 2026-10-01 ha fatto credere inventati Acquecrespe e Fogliaferrea.
    inglesi = [r.rstrip("\r") for r in io.open(NOMI_EN, encoding="utf-8").read().split("\n")]

    def doppio(n):
        return nomi[n] if nomi[n] == inglesi[n] else "%s (%s)" % (nomi[n], inglesi[n])
    incontri = [x for x in json.load(io.open(INCONTRI, encoding="utf-8"))["incontri"]
                if not x["evento"] and x["classe"] not in A_TEMPO
                and (x.get("legale", True) or x.get("motivo") == "Memory"
                     # In Let's Go l'evoluzione costruita cambiando la specie non ricalcola i valori risveglio
                     # (AV): è lo stesso artefatto, e la pre-evoluzione dello stesso incontro è giudicata legale.
                     or x.get("motivo") == "AVs" and x["da_specie"] and x["versione"] in ("GP", "GE")
                     or (x["numero"], x["forma"]) in EVOLUZIONI_SPECIALI and x["da_specie"])]
    per_forma = collections.defaultdict(list)
    forme_en = collections.defaultdict(dict)
    for x in incontri:
        x["prodotto"] = x["versione"]
        if x["versione"] == "ZA" and DLC_ZA.search(x["luogo"]) or x["versione"] in ("SL", "VL") and DLC_SV.search(x["luogo"]) or x["versione"] in ("SW", "SH") and DLC_SWSH.search(x["luogo"]):
            x["prodotto"] = x["versione"] + "+DLC"
        x["metodo"] = metodo_di(x["classe"])
        if x["da_specie"]:
            x["metodo"] = "evoluzione da " + x["da_specie"] + (" (" + x["metodo"] + ")" if x["metodo"] else "")
            if (x["numero"], x["forma"]) in EVOLUZIONI_SPECIALI:
                x["metodo"] += ", condizione: " + EVOLUZIONI_SPECIALI[(x["numero"], x["forma"])] + ", da verificare in gioco"
        per_forma[(x["numero"], x["forma"])].append(x)
        forme_en[x["numero"]][x["forma"]] = x["forma_en"]

    voci = []
    for f in glob.glob(os.path.join(SCHEDE, "*.json")):
        v = json.load(io.open(f, encoding="utf-8"))
        if v.get("isPrerelease") or not 1 <= v["dexNum"] <= 1025:
            continue
        c = lista.classe(v)
        if c is None or c.startswith("da oggetto"):
            continue
        eng = (v.get("formNames") or {}).get("eng") or ""
        forma_it = (v.get("formNames") or {}).get("ita") or eng
        # Il collegamento alla forma della libreria: specie e femmine alla forma 0, le altre per nome inglese normalizzato.
        # Minior si tiene nel box con il nucleo scoperto: la sua forma base nella libreria è il nucleo rosso, la 7.
        # Il dataset chiama «Maschio» e «Femmina» anche le forme regionali con differenze di sesso, come lo Sneasel di
        # Hisui: la regione sta nell'identificativo, quindi la femmina si collega alla forma del proprio identificativo
        # senza il suffisso «-f».
        resto = v["id"].split("-", 1)[1] if "-" in v["id"] else ""
        if v.get("isFemaleForm"):
            resto = re.sub(r"(^|-)f$", "", resto)
        regione = "" if "cap" in resto else next((r for r in ("alola", "galar", "hisui", "paldea") if r in resto), "")
        if regione:
            forma_it = regione.capitalize() + (", " + forma_it if forma_it in ("Maschio", "Femmina") else "")
        indice = 7 if v["dexNum"] == 774 else 0
        if resto and (c not in ("specie", "forma femminile") or regione):
            candidati = forme_en.get(v["dexNum"], {})
            n = norma(eng) if not regione else regione
            pref = norma(resto)
            trovato = [i for i, nome in candidati.items() if norma(nome) and (norma(nome) == n or norma(nome) in n or n in norma(nome) or norma(nome) == pref)]
            if v["dexNum"] == 869:  # Alcremie: la forma della libreria è la crema, la decorazione segue
                trovato = [i for i, nome in candidati.items() if norma(nome) and norma(nome) in norma(v["id"])]
            indice = trovato[0] if trovato else None
        voci.append({"id": v["id"], "dex": v["dexNum"], "specie": doppio(v["dexNum"]), "forma": forma_it if c != "specie" else "",
                     "classe": c, "indice": indice,
                     "gratis": sorted(set(v.get("obtainableIn") or []) & {"go", "home"} | set(v.get("eventOnlyIn") or []) & {"home"})})
    for v in voci:
        v["incontri"] = per_forma.get((v["dex"], v["indice"]), []) if v["indice"] is not None else []
        v["prodotti"] = {x["prodotto"] for x in v["incontri"]}

    # Ordine di acquisto goloso: un DLC si può scegliere solo dopo il suo gioco base.
    prodotti = set(BASE) | {k + "+DLC" for k in DLC}
    presi = set(POSSEDUTI)
    coperte = {v["id"] for v in voci if v["prodotti"] & presi}
    passi = [("ZA", len(coperte), len(coperte))]
    while True:
        scelte = [p for p in prodotti - presi if not p.endswith("+DLC") or p[:-4] in presi]
        guadagno = {p: sum(1 for v in voci if p in v["prodotti"] and v["id"] not in coperte) for p in scelte}
        # Un DLC si valuta insieme al suo gioco base, perché comprarlo da solo non serve.
        for p in [p for p in prodotti - presi if p.endswith("+DLC") and p[:-4] not in presi]:
            base = p[:-4]
            guadagno[base + "&DLC"] = sum(1 for v in voci if (base in v["prodotti"] or p in v["prodotti"]) and v["id"] not in coperte)
        if not guadagno or max(guadagno.values()) == 0:
            break
        p = max(sorted(guadagno), key=lambda x: guadagno[x])
        nuovi = {p[:-4], p[:-4] + "+DLC"} if p.endswith("&DLC") else {p}
        presi |= nuovi
        coperte |= {v["id"] for v in voci if v["prodotti"] & nuovi}
        passi.append((p, guadagno[p], len(coperte)))
    ordine = [q for p, _, _ in passi for q in ([p[:-4], p[:-4] + "+DLC"] if p.endswith("&DLC") else [p])]

    def nome_prodotto(p):
        if p.endswith("&DLC"):
            return BASE[p[:-4]] + " con il suo DLC"
        return DLC[p[:-4]] if p.endswith("+DLC") else BASE[p]

    def migliore(v):
        for p in ordine:
            cand = [x for x in v["incontri"] if x["prodotto"] == p]
            if cand:
                x = min(cand, key=lambda x: (RANGO.get(x["metodo"], 3 if x["da_specie"] else 1), x["luogo"] == ""))
                return p, x
        return None, None

    copie = collections.Counter()
    if os.path.exists(COPIE):
        for c in json.load(io.open(COPIE, encoding="utf-8"))["copie"]:
            if c["gruppo"].startswith("per HOME"):
                for e in c["esemplari"]:
                    copie[e["numero"]] += 1
    senza = [v for v in voci if not v["prodotti"]]
    non_collegate = [v for v in voci if v["indice"] is None]
    r = ["# Studio Switch: quali giochi comprare, in che ordine, e dove si ottiene ogni voce", "",
         "> Documento generato da `tools/studio-switch.py` dagli incontri della libreria (`tools/pkhex-incontri-switch`, clone PKHeX `e15d246`) e dal dataset `pokepc/dataset` (`5fd44c1`). Non si modifica a mano: si rigenera.", "",
         "Le voci della lista completa, senza le forme da oggetto tenuto, sono %d. Quelle che almeno un gioco per Switch dà con un incontro permanente sono %d; quelle che nessuno dà sono %d. Gli incontri a tempo (doni segreti, raid e focolai di distribuzione, raid a sette stelle) non contano, perché oggi non si giocano più. Una voce si ottiene anche per evoluzione o per uovo: la colonna del metodo lo dice." % (
             len(voci), len(voci) - len(senza), len(senza)), "",
         "## L'ordine di acquisto", "",
         "A ogni riga il prodotto che aggiunge più voci non ancora coperte, partendo da Leggende Z-A. Le due versioni di una coppia sono due prodotti: la seconda serve per le esclusive, che altrimenti si scambiano con un'altra persona. Un DLC conta come prodotto a parte e si riconosce dal luogo dell'incontro.", "",
         "| Passo | Prodotto | Voci nuove | Voci coperte in tutto |", "|---|---|---|---|"]
    for n, (p, g, tot) in enumerate(passi):
        r.append("| %d | %s | %d | %d |" % (n, nome_prodotto(p) + (" (posseduto)" if p in POSSEDUTI else ""), g, tot))
    r += ["", "## Le voci che nessun gioco per Switch dà", "",
          "Per queste la via è Pokémon GO, un regalo di HOME, oppure le copie preparate dal progetto per la banca. L'ultima colonna conta gli esemplari della specie, in qualunque forma, nelle copie per HOME.", "",
          "| Dex | Specie | Forma | Classe | Via gratuita | Esemplari nelle copie |", "|---|---|---|---|---|---|"]
    for v in sorted(senza, key=lambda x: (x["dex"], x["forma"])):
        via = ", ".join({"go": "Pokémon GO", "home": "regalo di HOME"}[g] for g in v["gratis"]) or "nessuna"
        r.append("| %d | %s | %s | %s | %s | %d |" % (v["dex"], v["specie"], v["forma"], v["classe"], via, copie[v["dex"]]))
    r += ["", "## Dove e come, voce per voce", "",
          "La via indicata è nel primo prodotto dell'ordine di acquisto che dà la voce, preferendo la cattura alla schiusa e la schiusa all'evoluzione. I luoghi sono i nomi inglesi della libreria. La colonna degli altri prodotti dice dove altro si trova.", "",
          "| Dex | Specie | Forma | Prodotto | Metodo | Luogo | Livello | Altri prodotti |", "|---|---|---|---|---|---|---|---|"]
    for v in sorted(voci, key=lambda x: (x["dex"], x["classe"] != "specie", x["forma"])):
        p, x = migliore(v)
        if not x:
            continue
        altri = ", ".join(nome_prodotto(q).split(" (")[0] for q in ordine if q in v["prodotti"] and q != p)
        r.append("| %d | %s | %s | %s | %s | %s | %s | %s |" % (v["dex"], v["specie"], v["forma"], nome_prodotto(p).split(" (")[0],
                                                               x["metodo"], x["luogo"], x["livello"], altri))
    if non_collegate:
        r += ["", "## Forme senza alcun incontro permanente nella libreria", "",
              "Queste forme non compaiono in nessun incontro permanente dei giochi per Switch, quindi la libreria non ne espone il nome: sono già fra le voci che nessun gioco per Switch dà, e sono elencate qui per controllo.", "",
              "| Dex | Specie | Forma | Classe |", "|---|---|---|---|"]
        for v in sorted(non_collegate, key=lambda x: (x["dex"], x["forma"])):
            r.append("| %d | %s | %s | %s |" % (v["dex"], v["specie"], v["forma"], v["classe"]))
    io.open(USCITA, "w", encoding="utf-8", newline="\n").write("\n".join(r) + "\n")
    print("voci", len(voci), "senza switch", len(senza), "non collegate", len(non_collegate))
    for p, g, tot in passi:
        print(nome_prodotto(p), g, tot)


if __name__ == "__main__":
    main()
