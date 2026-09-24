#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica, asse per asse, che cosa della terza generazione il deposito di Smeraldo porta e che cosa manca.

Perche' esiste
--------------
Il 2026-09-23, chiusa la cartuccia di Smeraldo, il proprietario ha chiesto se nella collezione fosse
rimasto indietro qualcosa di davvero speciale, e ha chiesto un controllo profondo su tutte le fonti,
non a pezzi. I censimenti del progetto coprono gia' molti assi, ma ciascuno su un asse solo e nessuno
confrontato con la cartuccia vera: le misure sulle mosse perdute e sui fiocchi erano fatte sui lotti
generati, non sul deposito. Questo strumento mette insieme gli assi e li misura sul deposito reale.

Le fonti sono tre, e nessuna e' trascritta a mano. Le tabelle degli incontri di PKHeX, cioe' gli
archivi dei selvatici di Rubino, Zaffiro, Smeraldo, Rosso Fuoco e Verde Foglia, gli incontri
statici, i doni, gli scambi, i doni di Colosseum verso i giochi portatili e le tabelle di Colosseum e
XD. La tabella degli eventi, attraverso `tools/catalogo-eventi.py`. E i documenti generati del
progetto che misurano un asse, cioe' le mosse perdute e le sfide del deposito di HOME. Il deposito
si legge dai byte del salvataggio e dal dump di PKHeX dello stesso file.

Che cosa conta come presente
----------------------------
Una voce e' presente quando nel deposito o in squadra c'e' un esemplare della specie con il gioco
d'origine che la voce richiede. Non si pretende la corrispondenza esatta del luogo, perche' il dump di
PKHeX scrive il luogo in italiano e le tabelle lo scrivono come numero: il criterio e' dichiarato e
misura la provenienza per gioco, che e' quella che le sfide del deposito e la legittimita' guardano.

Uso
---
    python tools/verifica-terza-generazione.py SALVATAGGIO.sav --dump DUMP.csv

Scrive `pokedex-home-completo/VERIFICA-TERZA-GENERAZIONE.md`.
"""

import argparse
import collections
import csv
import importlib.util
import io
import json
import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RADICE.joinpath("pokemon-gen12-gen3-bridge-original-hardware")))
from pokebridge import gen3, save3  # noqa: E402

PKHEX = RADICE.joinpath("_notes", "fonti", "cloni", "pkhex")
DATI3 = PKHEX.joinpath("PKHeX.Core", "Legality", "Encounters", "Data", "Gen3")
TESTI = PKHEX.joinpath("PKHeX.Core", "Resources", "text", "other", "it")
USCITA = RADICE.joinpath("pokedex-home-completo", "VERIFICA-TERZA-GENERAZIONE.md")
PER_BOX = 30

# I giochi come il dump di PKHeX li nomina, e come le tabelle li raggruppano.
GIOCHI = {"R": {"Rubino"}, "S": {"Zaffiro"}, "E": {"Smeraldo"}, "FR": {"Rosso Fuoco"}, "LG": {"Verde Foglia"}}
GIOCHI["RSE"] = GIOCHI["R"] | GIOCHI["S"] | GIOCHI["E"]
GIOCHI["RS"] = GIOCHI["R"] | GIOCHI["S"]
GIOCHI["FRLG"] = GIOCHI["FR"] | GIOCHI["LG"]
GIOCHI["CXD"] = {"Colosseum/XD"}
SELVATICI = [("Rubino", "encounter_r.pkl"), ("Zaffiro", "encounter_s.pkl"), ("Smeraldo", "encounter_e.pkl"),
             ("Rosso Fuoco", "encounter_fr.pkl"), ("Verde Foglia", "encounter_lg.pkl"), ("sciami di Hoenn", "encounter_rse_swarm.pkl")]


def _modulo(percorso, nome):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def testo(nome):
    return [r.strip() for r in TESTI.joinpath(nome).read_text(encoding="utf-8").split("\n")]


def deposito(salvataggio, dump):
    """Gli esemplari del deposito e della squadra: dal dump i campi leggibili, dai byte fiocchi e mosse."""
    s = save3.Save3(Path(salvataggio).read_bytes())
    righe, fuori = [], []
    with open(dump, encoding="utf-8-sig") as f:
        righe = list(csv.DictReader(f))
    for r in righe:
        m = re.search(r"@ \[(\d+)\] \([^)]*\)-(\d+)", r["Position"])
        naz = int(re.search(r": (\d{4})\b", r["Position"]).group(1))
        voce = {"naz": naz, "forma": int(r["Form"] or 0), "gioco": r["Version"], "tipo": r["EncounterType"], "ot": r["OT"],
                "sfera": r["Ball"], "specie": r["Species"], "luogo": r["MetLoc"], "uovo": r["IsEgg"] == "True", "uovo_luogo": r["EggLoc"],
                "posto": "squadra", "mosse": None, "gara": {}, "meriti": 0}
        if m:
            i = (int(m.group(1)) - 1) * PER_BOX + int(m.group(2)) - 1
            mon = gen3.Gen3Mon.from_bytes(s.leggi_posizione(i))
            if "%08X" % mon.personality != r["PID"]:
                sys.exit("il dump non appartiene al salvataggio: posizione %d" % i)
            voce.update(posto="B%d-%d" % (i // PER_BOX + 1, i % PER_BOX + 1), mosse=[x for x in mon.attacks.moves if x],
                        gara=dict(mon.misc.contest_ribbons), meriti=mon.misc.merit_ribbons)
        fuori.append(voce)
    return fuori


def presente(dep, naz, giochi, filtro=None):
    return [d for d in dep if d["naz"] == naz and d["gioco"] in giochi and (filtro is None or filtro(d))]


def selvatici():
    """{gioco: insieme delle specie selvatiche}, dagli archivi di PKHeX letti come fa il censimento dei condizionati."""
    cond = _modulo(RADICE.joinpath("tools", "censimento-condizionati.py"), "condizionati")
    fuori = {}
    for gioco, nome in SELVATICI:
        aree = cond.leggi_titolo(str(PKHEX.joinpath(cond.WILD, "Gen3", nome)), "3", "Gen3/" + nome)
        if aree is None:
            sys.exit("archivio dei selvatici illeggibile: %s" % nome)
        fuori[gioco] = set().union(*(sp for _, _, sp in aree))
    return fuori


def tabella(file_, nome, modo="primo"):
    tab = _modulo(RADICE.joinpath("tools", "censimento-eventi-tabelle.py"), "tabelle")
    voci = tab.voci_array(DATI3.joinpath(file_).read_text(encoding="utf-8"), nome, modo)
    if voci is None:
        sys.exit("tabella %s assente da %s" % (nome, file_))
    return voci


def famiglie():
    """{numero nazionale: insieme della famiglia evolutiva}, dalla tabella delle evoluzioni di pokeemerald.

    Serve agli incontri statici: chi ha ricevuto un Treecko e oggi ha uno Sceptile ha soddisfatto la voce,
    e il confronto per specie esatta lo darebbe per assente. I nomi delle costanti del sorgente si
    accoppiano ai nomi inglesi di PKHeX ridotti a lettere e cifre.
    """
    sorgente = Path(os.environ.get("TEMP", "")).joinpath("tmp.l1KqDBm5ER", "pokeemerald", "src", "data", "pokemon", "evolution.h")
    if not sorgente.exists():
        sys.exit("manca %s: si riclona con git clone --depth 1 https://github.com/pret/pokeemerald" % sorgente)
    inglesi = [re.sub(r"[^A-Z0-9]", "", n.upper().replace("♀", "F").replace("♂", "M")) for n in
               PKHEX.joinpath("PKHeX.Core", "Resources", "text", "other", "en", "text_Species_en.txt").read_text(encoding="utf-8").split("\n")]
    naz = {n: i for i, n in enumerate(inglesi) if n}
    def numero(costante):
        return naz[costante.replace("_", "")]
    vicini = collections.defaultdict(set)
    for da, a in re.findall(r"\[SPECIES_(\w+)\]\s*=\s*\{(.*?)\}\}", sorgente.read_text(encoding="utf-8"), re.S):
        for dest in re.findall(r"SPECIES_(\w+)", a):
            x, y = numero(da), numero(dest)
            vicini[x].add(y)
            vicini[y].add(x)
    fuori = {}
    for n in range(1, 387):
        visto, coda = {n}, [n]
        while coda:
            for v in vicini[coda.pop()]:
                if v not in visto:
                    visto.add(v)
                    coda.append(v)
        fuori[n] = visto
    return fuori


def luoghi():
    return [r.strip() for r in PKHEX.joinpath("PKHeX.Core", "Resources", "text", "locations", "gen3",
                                              "text_rsefrlg_00000_it.txt").read_text(encoding="utf-8").split("\n")]


def statici():
    """Incontri statici, doni, uova e doni di Colosseum verso i portatili, con i giochi e il luogo a cui valgono."""
    tab = _modulo(RADICE.joinpath("tools", "censimento-eventi-tabelle.py"), "tabelle")
    fuori = []
    for file_, nome, giochi in (("Encounters3RSE.cs", "StaticRSE", "RSE"), ("Encounters3RSE.cs", "StaticR", "R"),
                                ("Encounters3RSE.cs", "StaticS", "S"), ("Encounters3RSE.cs", "StaticE", "E"),
                                ("Encounters3FRLG.cs", "StaticFRLG", "FRLG"), ("Encounters3FRLG.cs", "StaticFR", "FR"),
                                ("Encounters3FRLG.cs", "StaticLG", "LG")):
        corpo = tab.blocco_array(DATI3.joinpath(file_).read_text(encoding="utf-8"), nome)
        for riga in corpo.splitlines():
            m = re.search(r"new\(\s*(\d+)\s*,", riga)
            if not m or riga.lstrip().startswith("//"):
                continue
            # chi vaga si cattura su qualunque percorso, quindi il luogo della tabella non lo individua
            luogo = None if "IsRoaming = true" in riga else re.search(r"Location\s*=\s*(\d+)", riga)
            commento = riga.split("//", 1)[1].strip() if "//" in riga else ""
            fuori.append({"specie": int(m.group(1)), "luogo": int(luogo.group(1)) if luogo else None,
                          "uovo": "IsEgg = true" in riga, "commento": commento, "giochi": giochi, "fonte": nome})
    return fuori


def gamecube():
    """Colosseum e XD: starter, doni, scambi e Ombra, piu' i doni di Colosseum che arrivano nei portatili."""
    fuori = []
    for file_, nome, modo, classe in (("Encounters3Colo.cs", "Starters", "primo", "starter di Colosseum"),
                                      ("Encounters3Colo.cs", "Gifts", "primo", "dono di Colosseum"),
                                      ("Encounters3Colo.cs", "Shadow", "campo", "Ombra di Colosseum"),
                                      ("Encounters3XD.cs", "Gifts", "primo", "dono di XD"),
                                      ("Encounters3XD.cs", "Trades", "primo", "scambio di XD"),
                                      ("Encounters3XD.cs", "Shadow", "campo", "Ombra di XD")):
        viste = set()
        for v in tabella(file_, nome, modo):
            if v["specie"] in viste:
                continue
            viste.add(v["specie"])
            fuori.append(dict(v, classe=classe))
    bonus = []
    for nome, allenatori in (("ColoGiftsR", ("COLOS", "コロシアム", "ARENA", "CLAUDIO", "AGATE", "アゲト", "SAMARAGD", "SOFO", "EMERITAE", "ÁGATA")),
                             ("ColoGiftsS", ("MATTLE", "バトルやま", "MT BATAILL", "MONTE LOTT", "DUELLBERG", "ERNESTO"))):
        for v in tabella("Encounters3RSE.cs", nome):
            bonus.append(dict(v, allenatori=allenatori))
    return fuori, bonus


def mosse_perdute():
    """Le mosse perdute con la chiusura dal documento generato, ridotte a quelle che esistono in terza generazione."""
    testo_ = RADICE.joinpath("pokedex-home-completo", "MOSSE-PERDUTE.md").read_text(encoding="utf-8")
    parte = testo_[testo_.index("## Che cosa i nostri lotti gia' portano"):]
    return sorted({(int(i), n) for n, i in re.findall(r"^\| ([^|]+?) \| (\d+) \|", parte, re.M) if int(i) <= 354})


def sfide():
    fuori = []
    with open(RADICE.joinpath("pokedex-home-completo", "data", "foglio-sfide-deposito.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            g = r["Games"].strip().upper()
            if g in ("RSE", "FRLG", "RS", "E", "FR", "LG", "CXD", "COLO", "XD"):
                fuori.append((int(float(r["#"])), g, r["Home Description"].strip()))
    return fuori


def componi(dep, nomi, mosse_it):
    specie_dep = {d["naz"] for d in dep}
    righe = []
    avvisi = collections.OrderedDict()

    def nome(n):
        return nomi[n] if 0 < n < len(nomi) else str(n)

    # 1. le specie
    selv = selvatici()
    stat = statici()
    gc, bonus = gamecube()
    mancanti = [n for n in range(1, 387) if n not in specie_dep]
    righe += ["## 1. Le 386 specie", "",
              "Specie della terza generazione presenti nel deposito o in squadra, con qualunque gioco d'origine: %d su 386. Per quelle che mancano, la colonna dice dove la terza generazione le offre." % (386 - len(mancanti)), ""]
    if mancanti:
        righe += ["| Specie | Selvatica in | Statica, dono o uovo in | Colosseum o XD |", "|---|---|---|---|"]
        for n in mancanti:
            dove = [g for g, sp in selv.items() if n in sp]
            st = sorted({v["giochi"] for v in stat if v["specie"] == n})
            c = sorted({v["classe"] for v in gc if v["specie"] == n})
            righe.append("| %s | %s | %s | %s |" % (nome(n), ", ".join(dove) or "nessuno", ", ".join(st) or "nessuno", ", ".join(c) or "nessuno"))
    avvisi["specie mancanti"] = len(mancanti)

    # 2. le forme
    unown = sorted({d["forma"] for d in dep if d["naz"] == 201})
    deoxys = sorted({(d["forma"], d["gioco"]) for d in dep if d["naz"] == 386})
    righe += ["", "## 2. Le forme che la terza generazione fissa", "",
              "Unown ha 28 forme; nel deposito ce ne sono %d, cioè %s. Deoxys ha la forma fissata dal gioco d'origine: Normale da evento su Rubino e Zaffiro, Attacco su Rosso Fuoco, Difesa su Verde Foglia, Velocità su Smeraldo; nel deposito le coppie di forma e gioco sono %s." % (
                  len(unown), ", ".join(map(str, unown)) or "nessuna", ", ".join("%d da %s" % t for t in deoxys) or "nessuna"), ""]
    avvisi["forme di Unown mancanti"] = 28 - len(unown)

    # 3. statici, doni e uova dei portatili
    righe += ["", "## 3. Incontri statici, doni e uova di Rubino, Zaffiro, Smeraldo, Rosso Fuoco e Verde Foglia", "",
              "Una riga per voce delle tabelle di PKHeX. Presente vuol dire un esemplare della stessa famiglia evolutiva, con uno dei giochi della voce e con il luogo d'incontro della voce; per le uova donate, il luogo d'origine dell'uovo.", "",
              "| Specie | Giochi | Voce nella tabella | Presente |", "|---|---|---|---|"]
    assenti_stat = 0
    fam = famiglie()
    nomi_luoghi = luoghi()
    for v in stat:
        # stesso gioco, stessa famiglia evolutiva e stesso luogo: per le uova donate il luogo e' quello
        # dell'uovo, che il dump scrive nella colonna del luogo d'origine dell'uovo
        luogo = nomi_luoghi[v["luogo"]] if v["luogo"] is not None and v["luogo"] < len(nomi_luoghi) else None
        chi = [d for d in dep if d["naz"] in fam[v["specie"]] and d["gioco"] in GIOCHI[v["giochi"]]
               and (luogo is None or (d["uovo_luogo"] if v["uovo"] else d["luogo"]) == luogo)]
        assenti_stat += not chi
        righe.append("| %s | %s | %s | %s |" % (nome(v["specie"]), v["giochi"], v["commento"].replace("|", "/"),
                                                 "sì, %s" % ", ".join(sorted({c["posto"] for c in chi}))[:60] if chi else "**no**"))
    avvisi["voci statiche senza esemplare dal loro gioco"] = assenti_stat

    # 4. i doni di Colosseum verso i portatili
    righe += ["", "## 4. I doni di Colosseum che arrivano nei portatili", "",
              "Il Pikachu e il Celebi del disco bonus giapponese, e l'Ho-Oh del Monte Lotta, sono esemplari con allenatore fisso che nascono in un gioco portatile.", "",
              "| Specie | Voce | Presente |", "|---|---|---|"]
    for v in bonus:
        chi = [d for d in dep if d["naz"] == v["specie"] and d["ot"] in v["allenatori"]]
        righe.append("| %s | %s | %s |" % (nome(v["specie"]), v["commento"], "sì, %s" % chi[0]["posto"] if chi else "**no**"))
        avvisi.setdefault("doni di Colosseum assenti", 0)
        avvisi["doni di Colosseum assenti"] += not chi

    # 5. Colosseum e XD
    righe += ["", "## 5. Colosseum e XD", "",
              "Specie distinte per classe. Gli esemplari Ombra purificati portano il fiocco Nazionale, che solo questi due giochi conferiscono.", "",
              "| Classe | Specie | Presenti da Colosseum o XD | Quali mancano |", "|---|---|---|---|"]
    per_classe = collections.OrderedDict()
    for v in gc:
        per_classe.setdefault(v["classe"], []).append(v["specie"])
    tot_gc = 0
    for classe, sp in per_classe.items():
        ci = [n for n in sp if presente(dep, n, GIOCHI["CXD"])]
        tot_gc += len(sp) - len(ci)
        righe.append("| %s | %d | %d | %s |" % (classe, len(sp), len(ci), ", ".join(nome(n) for n in sp if n not in ci)))
    avvisi["specie di Colosseum e XD assenti, per classe"] = tot_gc

    # 6. gli esclusivi di versione fra i selvatici
    righe += ["", "## 6. Gli esclusivi di versione fra i selvatici", "",
              "Specie selvatiche in un gioco della coppia e non nell'altro. Presente vuol dire un esemplare della specie da quel gioco; il deposito può comunque avere la specie da un altro gioco, e lo dice la terza colonna.", "",
              "| Gioco | Esclusive | Con esemplare da quel gioco | Senza, ma con la specie da altrove | Assenti del tutto |", "|---|---|---|---|---|"]
    for a, b in (("Rubino", "Zaffiro"), ("Zaffiro", "Rubino"), ("Rosso Fuoco", "Verde Foglia"), ("Verde Foglia", "Rosso Fuoco")):
        escl = sorted(selv[a] - selv[b])
        da_li = [n for n in escl if presente(dep, n, {a})]
        altrove = [n for n in escl if n not in da_li and n in specie_dep]
        via = [n for n in escl if n not in specie_dep]
        righe.append("| %s | %d | %d | %s | %s |" % (a, len(escl), len(da_li), ", ".join(nome(n) for n in altrove) or "nessuna",
                                                     ", ".join(nome(n) for n in via) or "nessuna"))
    solo_e = sorted(selv["Smeraldo"] - selv["Rubino"] - selv["Zaffiro"])
    righe.append("")
    righe.append("Selvatiche di Smeraldo che Rubino e Zaffiro non hanno: %s." % ", ".join(
        "%s%s" % (nome(n), "" if presente(dep, n, {"Smeraldo"}) else " (non da Smeraldo)") for n in solo_e))

    # 7. i fiocchi
    conti = collections.Counter()
    for d in dep:
        for k, v in d["gara"].items():
            for rango in range(1, v + 1):
                conti["gara %s, rango %d" % (k, rango)] += 1
        for j, n in enumerate(gen3.Misc.MERIT_RIBBON_NAMES):
            if d["meriti"] >> j & 1:
                conti[n] += 1
    tutti = ["gara %s, rango %d" % (k, r) for k in gen3.CONTEST_ORDER for r in range(1, 5)] + list(gen3.Misc.MERIT_RIBBON_NAMES)
    assenti_f = [f for f in tutti if not conti[f]]
    righe += ["", "## 7. I fiocchi di terza generazione", "",
              "I 32 fiocchi della parola dei meriti: i venti di gara, cinque categorie per quattro ranghi, e i dodici di merito. Presenti su almeno un esemplare: %d." % (len(tutti) - len(assenti_f)), "",
              "| Fiocco | Esemplari |", "|---|---|"] + ["| %s | %d |" % (f, conti[f]) for f in tutti]
    avvisi["fiocchi assenti"] = len(assenti_f)

    # 8. le mosse perdute
    righe += ["", "## 8. Le mosse perdute che esistono in terza generazione", "",
              "Dall'elenco di `MOSSE-PERDUTE.md`, le mosse con identificativo fino a 354, cioè insegnabili in terza generazione, misurate sul deposito e non sui lotti.", "",
              "| Mossa | Esemplari che la conoscono | Esempi |", "|---|---|---|"]
    assenti_m = 0
    for i, n in mosse_perdute():
        chi = [d for d in dep if d["mosse"] and i in d["mosse"]]
        assenti_m += not chi
        righe.append("| %s | %d | %s |" % (mosse_it[i] if i < len(mosse_it) else n, len(chi), ", ".join("%s %s" % (c["specie"], c["posto"]) for c in chi[:3]) or "**nessuno**"))
    avvisi["mosse perdute senza esemplare"] = assenti_m

    # 9. le sfide del deposito
    righe += ["", "## 9. Le sfide del deposito che chiedono un gioco di terza generazione", "",
              "| Sfida | Giochi | Esemplari che la soddisfano |", "|---|---|---|"]
    assenti_s = 0
    for n, g, testo_ in sfide():
        chi = presente(dep, n, GIOCHI.get(g, set()))
        assenti_s += not chi
        righe.append("| %s | %s | %s |" % (testo_, g, ", ".join(c["posto"] for c in chi) or "**nessuno**"))
    avvisi["sfide senza esemplare"] = assenti_s

    # 10. le combinazioni di sfera
    mew = [d for d in dep if d["naz"] == 151]
    righe += ["", "## 10. Le combinazioni di sfera che solo la terza generazione produce", "",
              "Il caso documentato da `STUDIO-05-gli-assi-che-non-contavamo.md` è Mew in una sfera diversa dalla Poké Ball, possibile soltanto con l'Isola Suprema di Smeraldo, che il verificatore accetta anche fuori dal Giappone. I Mew del deposito: %s." % "; ".join(
                  "%s, %s, %s" % (d["ot"], d["sfera"], d["tipo"]) for d in mew)]
    avvisi["Mew in una sfera diversa dalla Poké Ball"] = 0 if any(d["sfera"] != "Poké Ball" for d in mew) else 1
    return righe, avvisi


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("salvataggio")
    p.add_argument("--dump", required=True)
    args = p.parse_args()
    dep = deposito(args.salvataggio, args.dump)
    nomi = testo("text_Species_it.txt")
    mosse_it = testo("text_Moves_it.txt")
    corpo, avvisi = componi(dep, nomi, mosse_it)
    testa = ["# Verifica della terza generazione sul deposito di Smeraldo", "",
             "> Documento generato da `tools/verifica-terza-generazione.py`. Non si modifica a mano: si rigenera. Misura sul deposito reale della cartuccia, cioè sui byte del salvataggio e sul dump di PKHeX dello stesso file, ciò che le tabelle di PKHeX e i censimenti del progetto dicono che la terza generazione offre. Il criterio di presenza è la specie con il gioco d'origine, non il luogo esatto.", "",
             "Esemplari letti, deposito e squadra: %d." % len(dep), "", "## Riepilogo", "", "| Asse | Voci senza esemplare |", "|---|---|"]
    testa += ["| %s | %d |" % (k, v) for k, v in avvisi.items()]
    USCITA.write_text("\n".join(testa + [""] + corpo) + "\n", encoding="utf-8", newline="\n")
    for k, v in avvisi.items():
        print("  %-50s %d" % (k, v))
    print("scritto %s" % USCITA)


if __name__ == "__main__":
    main()
