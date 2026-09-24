#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Costruisce le richieste di generazione del complemento di terza generazione per il Rubino di prova, secondo ADR-080.

Perche' esiste
--------------
ADR-080 chiede la collezione completa di terza generazione su due cartucce: Smeraldo resta com'e', e il
Rubino riceve tutto cio' che Smeraldo non ha. Questo programma decide che cosa sia quel tutto, e lo
decide dai byte del deposito di Smeraldo e dalle tabelle di PKHeX attraverso le funzioni di
`tools/verifica-terza-generazione.py`, cosi' che le due misure non possano divergere. Non genera nulla:
scrive le richieste in un file JSON che `tools/pkhex-genera` esegue con la libreria del verificatore.

Gli assi, e che cosa ciascuno chiede
------------------------------------
Gli incontri statici, i doni e le uova dei portatili che Smeraldo non ha dal loro gioco. Starter di Kanto
evoluti per le due sfide del deposito: Bulbasaur e Charmander di Rosso Fuoco o Verde Foglia nascono come
Venusaur e Charizard. Colosseum e XD per intero, una voce per specie e classe. I tre doni di Colosseum che
arrivano nei portatili e il Jirachi di Pokemon Channel. Le 28 forme di Unown. Gli esclusivi di versione,
ciascuno dal proprio gioco se Smeraldo non ce l'ha da li'. Le specie che dopo tutto cio' restano scoperte,
da un incontro selvatico o da un uovo. Le mosse perdute insegnabili in terza generazione, ciascuna su un
esemplare che la impara. E i fiocchi legali, su un esemplare che li porta tutti.

L'allenatore
------------
Alessio, maschio, lingua italiana, con un identificativo per gioco d'origine, come deciso in ADR-080. Per
Smeraldo resta 42317, quello degli incontri da biglietto; per gli altri giochi l'identificativo e il
segreto sono derivati in modo deterministico dal nome del gioco, cosi' che rilanciare dia gli stessi numeri.

Uso
---
    python tools/manifesto-complemento-rubino.py SALVATAGGIO_SMERALDO.sav --dump DUMP.csv

Scrive `_notes/lotto-complemento-rubino/richieste.json`.
"""

import argparse
import collections
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = Path(__file__).resolve().parents[1]
USCITA = RADICE.joinpath("_notes", "lotto-complemento-rubino", "richieste.json")

# I giochi nella sigla di PKHeX, e i due gruppi che il generatore conosce.
GIOCHI = {"R": ["R"], "S": ["S"], "E": ["E"], "FR": ["FR"], "LG": ["LG"], "RSE": ["E", "R", "S"], "RS": ["R", "S"],
          "FRLG": ["FR", "LG"], "CXD": ["CXD"]}
NOME_GIOCO = {"Rubino": "R", "Zaffiro": "S", "Smeraldo": "E", "Rosso Fuoco": "FR", "Verde Foglia": "LG"}
CLASSI_GC = {"starter di Colosseum": "EncounterStarter3Colo", "dono di Colosseum": "EncounterGift3Colo",
             "Ombra di Colosseum": "EncounterShadow3Colo", "dono di XD": "EncounterStatic3XD",
             "scambio di XD": "EncounterTrade3XD", "Ombra di XD": "EncounterShadow3XD"}
# Le mosse perdute insegnabili in terza generazione, con la specie che la impara secondo
# `gba-save-extraction-smeraldo/mosse-imparabili.json`. Incubo manca: in terza generazione nessuna specie
# la impara, quindi non ha portatore e lo si dichiara invece di inventarlo.
MOSSE_PERDUTE = [(169, "Ragnatela", 167), (193, "Preveggenza", 355), (218, "Frustrazione", 359), (265, "Maniereforti", 296),
                 (274, "Assistente", 52), (302, "Pugnospine", 331), (320, "Meloderba", 1), (324, "Segnoraggio", 313)]
# I 26 fiocchi legali su un esemplare che non sia Ombra: i venti di gara al rango massimo, e sei di merito.
FIOCCHI = ["RibbonCountG3Cool=4", "RibbonCountG3Beauty=4", "RibbonCountG3Cute=4", "RibbonCountG3Smart=4", "RibbonCountG3Tough=4",
           "RibbonChampionG3", "RibbonWinning", "RibbonVictory", "RibbonArtist", "RibbonEffort", "RibbonEarth"]


def _modulo(percorso, nome):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def allenatori():
    fuori = {}
    # Colosseum e XD sono due partite distinte, ciascuna con il proprio identificativo: con uno solo, gli
    # esemplari che il gioco deriva dal seme dell'identificativo, come gli starter, verrebbero uguali
    for gioco in ("R", "S", "E", "FR", "LG", "COLO", "XD"):
        if gioco == "E":
            fuori[gioco] = {"OT": "Alessio", "TID16": 42317, "SID16": 0}
            continue
        d = hashlib.sha256(("Alessio|" + gioco).encode()).digest()
        fuori[gioco] = {"OT": "Alessio", "TID16": int.from_bytes(d[:2], "little"), "SID16": int.from_bytes(d[2:4], "little")}
    return fuori


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("salvataggio")
    p.add_argument("--dump", required=True)
    args = p.parse_args()
    v = _modulo(RADICE.joinpath("tools", "verifica-terza-generazione.py"), "verifica")
    dep = v.deposito(args.salvataggio, args.dump)
    fam = v.famiglie()
    nomi_luoghi = v.luoghi()
    richieste = []
    coperte = {d["naz"] for d in dep}

    def aggiungi(**r):
        r.setdefault("id", "%03d-%s" % (len(richieste) + 1, r["motivo"].split(",")[0].replace(" ", "-")[:40]))
        richieste.append(r)
        coperte.add(r.get("evolvi_a") or r["specie"])

    # 1. statici, doni e uova che Smeraldo non ha dal loro gioco
    for s in v.statici():
        luogo = nomi_luoghi[s["luogo"]] if s["luogo"] is not None else None
        chi = [d for d in dep if d["naz"] in fam[s["specie"]] and d["gioco"] in v.GIOCHI[s["giochi"]]
               and (luogo is None or (d["uovo_luogo"] if s["uovo"] else d["luogo"]) == luogo)]
        if chi:
            continue
        r = {"specie": s["specie"], "giochi": GIOCHI[s["giochi"]], "classi": ["EncounterStatic3"], "luogo": s["luogo"],
             "motivo": "statico, %s" % s["commento"]}
        if s["specie"] == 1 and s["giochi"] == "FRLG":
            r.update(evolvi_a=3, motivo="statico e sfida del deposito, Venusaur da Rosso Fuoco o Verde Foglia")
        if s["specie"] == 4 and s["giochi"] == "FRLG":
            r.update(evolvi_a=6, motivo="statico e sfida del deposito, Charizard da Rosso Fuoco o Verde Foglia")
        aggiungi(**r)

    # 2. i doni di Colosseum verso i portatili, e il Jirachi di Pokemon Channel
    _, bonus = v.gamecube()
    for b in bonus:
        if not [d for d in dep if d["naz"] == b["specie"] and d["ot"] in b["allenatori"]]:
            aggiungi(specie=b["specie"], giochi=["R", "S"], classi=["EncounterGift3Colo"], luogo=None, motivo="dono di Colosseum, %s" % b["commento"])
    aggiungi(specie=385, giochi=["R", "S"], classi=["EncounterGift3"], luogo=None, allenatore_evento="CHANNEL", motivo="evento, Jirachi di Pokemon Channel")

    # 3. Colosseum e XD, una voce per specie e classe
    gc, _ = v.gamecube()
    for g in gc:
        # presente se Smeraldo ha la specie con il tipo d'incontro che il dump di PKHeX scrive per quella classe
        prefisso = {"Ombra di Colosseum": "COLO Shadow", "Ombra di XD": "XD Shadow"}.get(g["classe"])
        if prefisso and [d for d in dep if d["naz"] == g["specie"] and d["tipo"].startswith(prefisso)]:
            continue
        aggiungi(specie=g["specie"], giochi=["COLO" if "Colosseum" in g["classe"] else "XD"], classi=[CLASSI_GC[g["classe"]]], luogo=None, motivo="%s, %s" % (g["classe"], g["commento"] or g["specie"]))

    # 4. le 28 forme di Unown, dalle Rovine Tanoby
    forme = {d["forma"] for d in dep if d["naz"] == 201}
    for f in range(28):
        if f not in forme:
            aggiungi(specie=201, forma=f, giochi=["FR", "LG"], classi=["EncounterSlot3"], luogo=None, motivo="forma di Unown %d" % f)

    # 5. gli esclusivi di versione, ciascuno dal proprio gioco
    selv = v.selvatici()
    for a, b in (("Rubino", "Zaffiro"), ("Zaffiro", "Rubino"), ("Rosso Fuoco", "Verde Foglia"), ("Verde Foglia", "Rosso Fuoco")):
        for n in sorted(selv[a] - selv[b]):
            if not [d for d in dep if d["naz"] == n and d["gioco"] == a] and not [r for r in richieste if r["specie"] == n and r["giochi"] == [NOME_GIOCO[a]]]:
                aggiungi(specie=n, giochi=[NOME_GIOCO[a]], classi=["EncounterSlot3"], luogo=None, motivo="esclusivo di %s" % a)

    # 6. le mosse perdute, ciascuna su una specie che la impara
    for mossa, nome, specie in MOSSE_PERDUTE:
        aggiungi(specie=specie, giochi=["E", "R", "S", "FR", "LG"], classi=[], luogo=None, mosse=[mossa], motivo="mossa perduta %s" % nome)

    # 7. i fiocchi legali, su un Absol del Percorso 120 di Smeraldo che li porta tutti. Il portatore pensato
    # all'inizio era un Milotic, ma il verificatore non ricollega l'evoluzione da un Feebas generato a un
    # incontro d'origine, mentre accetta tutti e 26 i fiocchi su un esemplare che non si evolve.
    aggiungi(specie=359, giochi=["E"], classi=["EncounterSlot3"], luogo=None, fiocchi=FIOCCHI, livello=100,
             motivo="fiocchi, i 26 legali fuori dal Nazionale su un solo esemplare")

    # 8. le specie che restano scoperte, da un selvatico o da un uovo
    for n in range(1, 387):
        if n not in coperte:
            giochi = [g for g in ("E", "R", "S", "FR", "LG") if n in selv[{"E": "Smeraldo", "R": "Rubino", "S": "Zaffiro", "FR": "Rosso Fuoco", "LG": "Verde Foglia"}[g]]]
            aggiungi(specie=n, giochi=giochi or ["E", "R", "S", "FR", "LG"], classi=[], luogo=None, motivo="specie scoperta")

    USCITA.parent.mkdir(parents=True, exist_ok=True)
    # le personalita' del deposito di Smeraldo non si ripetono nel complemento, cosi' che fra le due cartucce
    # nessun esemplare sembri il clone di un altro
    escluse = sorted({"%08X" % int(r["PID"], 16) for r in __import__("csv").DictReader(open(args.dump, encoding="utf-8-sig"))})
    USCITA.write_text(json.dumps({"formato": 1, "allenatori": allenatori(), "personalita_escluse": escluse, "richieste": richieste},
                                 ensure_ascii=False, indent=1),
                      encoding="utf-8")
    conti = collections.Counter(r["motivo"].split(",")[0].split(" ")[0] for r in richieste)
    for k, n in conti.most_common():
        print("  %-20s %d" % (k, n))
    print("richieste %d, scritte in %s" % (len(richieste), USCITA))


if __name__ == "__main__":
    main()
