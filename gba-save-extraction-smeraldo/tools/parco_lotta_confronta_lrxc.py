#!/usr/bin/env python3
"""Confronta il foglio di LRXC sull'Azienda Lotta di Smeraldo con il sorgente del gioco, e dice che cosa del foglio è fermo e che cosa no.

Perché esiste
-------------

Il foglio che accompagna il video di LRXC sull'Azienda Lotta (Battle Factory) al livello 50 è la fonte più comoda da tenere aperta in partita: una riga per insieme, con la specie, la natura, lo strumento, le quattro mosse, le abilità possibili, la distribuzione dei punti base, la velocità già calcolata e una colonna "Style #" che nessun'altra fonte del progetto porta. Una fonte comoda è però anche quella che si consulta senza verificarla, e il foglio è una trascrizione fatta a mano, quindi è esattamente il tipo di fonte che va confrontata una volta con il sorgente prima di fidarsene per sempre.

Il sorgente è il disassemblato `pret/pokeemerald`, clonato in `_notes/fonti/cloni/pokeemerald`. Il confronto non si fida dei nomi delle costanti per decidere che due insiemi siano lo stesso: confronta i campi, e usa il nome solo per dire quale costante il foglio intendeva.

Che cosa confronta
------------------

La prima parte prende ogni riga della scheda "Pokémon" e cerca in `gBattleFrontierMons` l'insieme con la stessa specie e lo stesso numero d'insieme, poi confronta natura, strumento, quattro mosse nell'ordine, distribuzione dei punti base, tipi e abilità; separatamente cerca un insieme identico per contenuto, così che un numero d'insieme sbagliato nel foglio si distingua da un contenuto sbagliato. Ne ricava quali numeri `FRONTIER_MON` il foglio copre, e li mette accanto agli intervalli che il gioco usa davvero per pescare gli avversari dell'Azienda al livello 50, cioè la tabella `sInitialRentalMonRanges` di `src/battle_factory.c`.

La seconda parte legge la colonna "Style #" come quattro cifre, una per mossa, e la confronta con lo stile che `GetMoveBattleStyle` assegna a ciascuna mossa scorrendo le tabelle `sMoveStyles` nello stesso ordine del gioco, primo riscontro vincente.

La terza parte cerca il livello e i punti individuali con cui la colonna "Speed" torna, provando livello 50 e livello 100 e ogni valore di punti individuali da 0 a 31, con la formula della terza generazione e i punti base che il gioco assegna davvero, cioè 510 diviso il numero di statistiche marcate.

La quarta parte confronta la scheda "Trainers" con `gBattleFrontierTrainers` e con gli elenchi di `battle_frontier_trainer_mons.h`, espandendo le macro annidate: nome, classe, e l'elenco degli insiemi nell'ordine. Alla fine ricorda che cosa dice il sorgente sull'uso di quegli elenchi nell'Azienda, perché è il punto che decide se la scheda serva in partita.

Uso
---

    python gba-save-extraction-smeraldo/tools/parco_lotta_confronta_lrxc.py
    python gba-save-extraction-smeraldo/tools/parco_lotta_confronta_lrxc.py --foglio <xlsx> --sorgente <clone pokeemerald>

Lo strumento è in sola lettura e deterministico: non scrive niente, stampa il rapporto sull'uscita standard in UTF-8.
"""

import argparse
import collections
import re
import sys
from pathlib import Path

import openpyxl

RADICE = Path(__file__).resolve().parents[2]
FOGLIO_PREDEFINITO = RADICE / "_notes/fonti/consegne/2026-09-28-LRXC-Level-50-Round-1-Round-15.xlsx"
SORGENTE_PREDEFINITO = RADICE / "_notes/fonti/cloni/pokeemerald"

STATISTICHE = ["HP", "ATTACK", "DEFENSE", "SPEED", "SP_ATTACK", "SP_DEFENSE"]
# Ordine delle nature in Gen 3: la natura n aumenta la statistica n // 5 e riduce la n % 5,
# su Attacco, Difesa, Velocità, Attacco Speciale, Difesa Speciale.
NATURE = ["HARDY", "LONELY", "BRAVE", "ADAMANT", "NAUGHTY", "BOLD", "DOCILE", "RELAXED", "IMPISH", "LAX",
          "TIMID", "HASTY", "SERIOUS", "JOLLY", "NAIVE", "MODEST", "MILD", "QUIET", "BASHFUL", "RASH",
          "CALM", "GENTLE", "SASSY", "CAREFUL", "QUIRKY"]


def norma(testo):
    """Riduce un nome alla forma confrontabile: maiuscole, solo lettere e cifre, {PKMN} come POKEMON."""
    if testo is None:
        return ""
    t = str(testo).upper().replace("{PKMN}", "POKEMON").replace("PKMN", "POKEMON").replace("É", "E")
    return re.sub(r"[^A-Z0-9]", "", t)


def riga_di(testo, posizione):
    return testo.count("\n", 0, posizione) + 1


# ---------------------------------------------------------------------------
# Lettura del sorgente
# ---------------------------------------------------------------------------

class Sorgente:
    def __init__(self, radice):
        self.radice = Path(radice)
        self._leggi_nomi()
        self._leggi_specie()
        self._leggi_costanti_insiemi()
        self._leggi_insiemi()
        self._leggi_stili()
        self._leggi_intervalli()
        self._leggi_allenatori()

    def testo(self, relativo):
        return (self.radice / relativo).read_text(encoding="utf-8", errors="replace")

    def _leggi_nomi(self):
        self.nome_mossa = dict(re.findall(r"\[(MOVE_\w+)\]\s*=\s*_\(\"([^\"]*)\"\)", self.testo("src/data/text/move_names.h")))
        self.nome_specie = dict(re.findall(r"\[(SPECIES_\w+)\]\s*=\s*_\(\"([^\"]*)\"\)", self.testo("src/data/text/species_names.h")))
        self.nome_abilita = dict(re.findall(r"\[(ABILITY_\w+)\]\s*=\s*_\(\"([^\"]*)\"\)", self.testo("src/data/text/abilities.h")))
        self.nome_strumento = dict(re.findall(r"\[(ITEM_\w+)\]\s*=\s*\{\s*\.name\s*=\s*_\(\"([^\"]*)\"\)", self.testo("src/data/items.h")))
        self.strumento_frontiera = dict(re.findall(r"\[(BATTLE_FRONTIER_ITEM_\w+)\]\s*=\s*(ITEM_\w+)", self.testo("src/battle_tower.c")))
        self.nome_classe = dict(re.findall(r"\[(TRAINER_CLASS_\w+)\]\s*=\s*_\(\"([^\"]*)\"\)", self.testo("src/data/text/trainer_class_names.h")))
        lookup = self.testo("src/data/pokemon/trainer_class_lookups.h")
        blocco = lookup[lookup.index("gFacilityClassToTrainerClass"):]
        blocco = blocco[:blocco.index("};")]
        self.classe_da_struttura = dict(re.findall(r"\[(FACILITY_CLASS_\w+)\]\s*=\s*(TRAINER_CLASS_\w+)", blocco))

    def _leggi_specie(self):
        testo = self.testo("src/data/pokemon/species_info.h")
        self.base = {}
        for m in re.finditer(r"\[(SPECIES_\w+)\]\s*=\s*\{(.*?)\n    \}", testo, re.S):
            corpo = m.group(2)
            valori = dict(re.findall(r"\.(base\w+)\s*=\s*(\d+)", corpo))
            tipi = re.search(r"\.types\s*=\s*\{\s*(TYPE_\w+)\s*,\s*(TYPE_\w+)\s*\}", corpo)
            abil = re.search(r"\.abilities\s*=\s*\{\s*(ABILITY_\w+)\s*,\s*(ABILITY_\w+)\s*\}", corpo)
            if "baseSpeed" not in valori:
                continue
            self.base[m.group(1)] = {
                "HP": int(valori["baseHP"]), "ATTACK": int(valori["baseAttack"]), "DEFENSE": int(valori["baseDefense"]),
                "SPEED": int(valori["baseSpeed"]), "SP_ATTACK": int(valori["baseSpAttack"]), "SP_DEFENSE": int(valori["baseSpDefense"]),
                "tipi": sorted({tipi.group(1), tipi.group(2)}) if tipi else [],
                "abilita": [a for a in (abil.groups() if abil else []) if a != "ABILITY_NONE"],
            }

    def _leggi_costanti_insiemi(self):
        testo = self.testo("include/constants/battle_frontier_mons.h")
        self.id_insieme = {}
        self.riga_costante = {}
        for m in re.finditer(r"#define\s+(FRONTIER_MON_\w+)\s+(\d+)", testo):
            self.id_insieme[m.group(1)] = int(m.group(2))
            self.riga_costante[m.group(1)] = riga_di(testo, m.start())
        alto = re.search(r"#define\s+FRONTIER_MONS_HIGH_TIER\s+(\d+)", testo)
        self.alto_livello = int(alto.group(1))
        self.riga_alto_livello = riga_di(testo, alto.start())
        self.costante_da_id = {v: k for k, v in self.id_insieme.items()}

    def _leggi_insiemi(self):
        percorso = "src/data/battle_frontier/battle_frontier_mons.h"
        testo = self.testo(percorso)
        self.insiemi = {}
        for m in re.finditer(r"\[(FRONTIER_MON_\w+)\]\s*=\s*\{(.*?)\}\s*,?\s*\n\s*(?=\[|\})", testo, re.S):
            costante, corpo = m.group(1), m.group(2)
            mosse = re.search(r"\.moves\s*=\s*\{([^}]*)\}", corpo).group(1)
            mosse = [x.strip() for x in mosse.split(",") if x.strip()]
            ev = re.search(r"\.evSpread\s*=\s*([^,\n]+)", corpo).group(1)
            ev = {s for s in re.findall(r"F_EV_SPREAD_(\w+)", ev)}
            numero = re.search(r"_(\d+)$", costante)
            ident = self.id_insieme[costante]
            self.insiemi[ident] = {
                "id": ident,
                "costante": costante,
                "riga": riga_di(testo, m.start()),
                "specie": re.search(r"\.species\s*=\s*(SPECIES_\w+)", corpo).group(1),
                "mosse": mosse,
                "strumento": re.search(r"\.itemTableId\s*=\s*(BATTLE_FRONTIER_ITEM_\w+)", corpo).group(1),
                "ev": ev,
                "natura": re.search(r"\.nature\s*=\s*NATURE_(\w+)", corpo).group(1),
                "numero": int(numero.group(1)) if numero else 1,
            }
        self.file_insiemi = percorso

    def _leggi_stili(self):
        testo = self.testo("include/constants/battle_factory.h")
        self.codice_stile = {k: int(v) for k, v in re.findall(r"#define\s+FACTORY_STYLE_(\w+)\s+(\d+)", testo)}
        fabbrica = self.testo("src/battle_factory.c")
        self.fabbrica = fabbrica
        tabelle = {}
        for m in re.finditer(r"static const u16 (sMoves_\w+)\[\]\s*=\s*\{(.*?)\};", fabbrica, re.S):
            tabelle[m.group(1)] = [x for x in re.findall(r"MOVE_\w+", m.group(2)) if x != "MOVE_NONE"]
        blocco = fabbrica[fabbrica.index("sMoveStyles[FACTORY_NUM_STYLES - 1] ="):]
        blocco = blocco[:blocco.index("};")]
        self.ordine_stili = []
        for stile, tabella in re.findall(r"\[FACTORY_STYLE_(\w+) - 1\]\s*=\s*(sMoves_\w+)", blocco):
            self.ordine_stili.append((self.codice_stile[stile], stile, tabella, tabelle[tabella]))
        self.ordine_stili.sort()
        self.riga_stili = riga_di(fabbrica, fabbrica.index("sMoveStyles[FACTORY_NUM_STYLES - 1] ="))
        self.soglie_stile = {}
        blocco = fabbrica[fabbrica.index("sRequiredMoveCounts"):]
        blocco = blocco[:blocco.index("};")]
        for stile, n in re.findall(r"\[FACTORY_STYLE_(\w+) - 1\]\s*=\s*(\d+)", blocco):
            self.soglie_stile[stile] = int(n)
        self.riga_soglie = riga_di(fabbrica, fabbrica.index("sRequiredMoveCounts"))
        # Mosse presenti in più di una tabella: vince la prima, come in GetMoveBattleStyle.
        viste = collections.defaultdict(list)
        for codice, stile, _, mosse in self.ordine_stili:
            for mossa in mosse:
                viste[mossa].append(stile)
        self.mosse_in_piu_stili = {k: v for k, v in viste.items() if len(v) > 1}

    def stile_mossa(self, mossa):
        for codice, _, _, mosse in self.ordine_stili:
            if mossa in mosse:
                return codice
        return 0

    def _leggi_intervalli(self):
        f = self.fabbrica
        pos = f.index("sInitialRentalMonRanges[][2] =")
        self.riga_intervalli = riga_di(f, pos)
        blocco = f[pos:f.index("};", pos)]
        coppie = re.findall(r"\{\s*(\w+)\s*,\s*([\w -]+?)\s*\}", blocco)

        def valore(nome):
            nome = nome.strip()
            if nome == "FRONTIER_MONS_HIGH_TIER":
                return self.alto_livello
            if nome == "NUM_FRONTIER_MONS - 1":
                return len(self.insiemi) - 1
            return self.id_insieme[nome]

        self.intervalli = [(valore(a), valore(b)) for a, b in coppie]
        self.intervalli_50 = self.intervalli[:8]

    def _leggi_allenatori(self):
        percorso_mons = "src/data/battle_frontier/battle_frontier_trainer_mons.h"
        testo = self.testo(percorso_mons)
        # Le macro sono di due specie: semplici, e con parametri incollati con `##`, come
        # FRONTIER_MONS_COOLTRAINER_2C(LATIOS) che produce FRONTIER_MON_LATIOS_1. Si espandono
        # sul testo, come farebbe il preprocessore, e poi si riducono a simboli.
        macro = {}
        for m in re.finditer(r"#define\s+(FRONTIER_MONS_\w+)(\(([^)]*)\))?[ \t]*\\?\n((?:.*\\\n)*.*)", testo):
            parametri = [x.strip() for x in m.group(3).split(",")] if m.group(2) else None
            macro[m.group(1)] = (parametri, m.group(4).replace("\\\n", "\n"))

        def espandi_testo(corpo, profondita=0):
            if profondita > 10:
                return corpo
            chiamata = re.compile(r"\b(FRONTIER_MONS_\w+)\b(\s*\(([^)]*)\))?")

            def sostituisci(m):
                nome = m.group(1)
                if nome not in macro:
                    return m.group(0)
                parametri, testo_macro = macro[nome]
                if parametri is not None:
                    argomenti = [x.strip() for x in (m.group(3) or "").split(",")]
                    for par, arg in zip(parametri, argomenti):
                        testo_macro = re.sub(r"\b%s\b" % re.escape(par), arg, testo_macro)
                    testo_macro = re.sub(r"\s*##\s*", "", testo_macro)
                elif m.group(2):
                    testo_macro = testo_macro + m.group(2)
                return espandi_testo(testo_macro, profondita + 1)

            return chiamata.sub(sostituisci, corpo)

        def espandi(corpo):
            return [s for s in re.findall(r"-1|[A-Z_][A-Z0-9_]*", espandi_testo(corpo)) if s == "-1" or s.startswith("FRONTIER_MON_")]

        elenchi = {}
        for m in re.finditer(r"const u16 (gBattleFrontierTrainerMons_\w+)\[\]\s*=\s*\{(.*?)\};", testo, re.S):
            simboli = espandi(m.group(2))
            if "-1" in simboli:
                simboli = simboli[:simboli.index("-1")]
            elenchi[m.group(1)] = (simboli, riga_di(testo, m.start()))
        percorso = "src/data/battle_frontier/battle_frontier_trainers.h"
        testo = self.testo(percorso)
        self.allenatori = []
        for m in re.finditer(r"\[(FRONTIER_TRAINER_\w+)\]\s*=\s*\{(.*?)\n    \}", testo, re.S):
            corpo = m.group(2)
            insieme = re.search(r"\.monSet\s*=\s*(\w+)", corpo).group(1)
            classe = re.search(r"\.facilityClass\s*=\s*(FACILITY_CLASS_\w+)", corpo).group(1)
            simboli, riga_elenco = elenchi[insieme]
            self.allenatori.append({
                "costante": m.group(1),
                "riga": riga_di(testo, m.start()),
                "nome": re.search(r"\.trainerName\s*=\s*_\(\"([^\"]*)\"\)", corpo).group(1),
                "classe": classe,
                "nome_classe": self.nome_classe.get(self.classe_da_struttura.get(classe, ""), classe),
                "elenco": [self.id_insieme[s] for s in simboli],
                "riga_elenco": riga_elenco,
            })
        self.file_allenatori = percorso
        self.file_elenchi = percorso_mons

    def etichetta(self, ident):
        """Il nome che il foglio userebbe per un insieme, per esempio "Sunkern 1"."""
        i = self.insiemi[ident]
        return "%s %d" % (self.nome_specie[i["specie"]], i["numero"])


# ---------------------------------------------------------------------------
# Lettura del foglio
# ---------------------------------------------------------------------------

def leggi_foglio(percorso):
    wb = openpyxl.load_workbook(percorso, data_only=True, read_only=True)
    schede = {norma(ws.title): ws for ws in wb.worksheets}
    righe = list(schede["POKEMON"].iter_rows(values_only=True))
    intestazione = [str(c).strip() if c is not None else "" for c in righe[0]]
    insiemi = []
    for n, r in enumerate(righe[1:], start=2):
        if not any(c is not None and str(c).strip() for c in r):
            continue
        d = dict(zip(intestazione, r))
        d["_riga"] = n
        insiemi.append(d)
    allenatori = []
    for n, r in enumerate(schede["TRAINERS"].iter_rows(values_only=True), start=1):
        if n == 1 or r[0] is None:
            continue
        allenatori.append({"_riga": n, "nome": str(r[0]).strip(), "classe": str(r[1] or "").strip(),
                           "elenco": [str(c).strip() for c in r[2:] if c is not None and str(c).strip()]})
    return intestazione, insiemi, allenatori


def ev_del_foglio(testo):
    parti = [p.strip() for p in str(testo or "").split("/")]
    if len(parti) != 6 or not all(p.isdigit() for p in parti):
        return None
    return [int(p) for p in parti]


# ---------------------------------------------------------------------------
# Calcoli
# ---------------------------------------------------------------------------

def velocita(base, iv, ev, livello, natura):
    grezza = (2 * base + iv + ev // 4) * livello // 100 + 5
    indice = NATURE.index(natura)
    su, giu = indice // 5, indice % 5
    if su != giu:
        if su == 2:
            grezza = grezza * 110 // 100
        elif giu == 2:
            grezza = grezza * 90 // 100
    return grezza


def ev_assegnati(insieme):
    quanti = len(insieme["ev"])
    return {s: (510 // quanti if s in insieme["ev"] else 0) for s in STATISTICHE}


# ---------------------------------------------------------------------------
# Rapporto
# ---------------------------------------------------------------------------

def intervalli_di(ids):
    ids = sorted(ids)
    fuori = []
    for i in ids:
        if fuori and i == fuori[-1][1] + 1:
            fuori[-1][1] = i
        else:
            fuori.append([i, i])
    return ", ".join("%d-%d" % (a, b) if a != b else str(a) for a, b in fuori)


def confronta(src, foglio_path):
    intestazione, insiemi_foglio, allenatori_foglio = leggi_foglio(foglio_path)
    out = []
    p = out.append
    p("Confronto fra il foglio LRXC dell'Azienda Lotta e pret/pokeemerald")
    p("=" * 68)
    p("Foglio: %s" % foglio_path)
    p("Sorgente: %s" % src.radice)
    p("Scheda Pokémon: %d righe con dati; colonne: %s" % (len(insiemi_foglio), ", ".join(intestazione)))
    p("Scheda Trainers: %d allenatori" % len(allenatori_foglio))
    p("Sorgente: %d insiemi in gBattleFrontierMons (%s), %d allenatori in gBattleFrontierTrainers (%s)" % (
        len(src.insiemi), src.file_insiemi, len(src.allenatori), src.file_allenatori))
    p("")

    # Indici per nome normalizzato.
    specie_da_nome = {norma(v): k for k, v in src.nome_specie.items()}
    mossa_da_nome = {norma(v): k for k, v in src.nome_mossa.items()}
    per_specie_numero = {(i["specie"], i["numero"]): i for i in src.insiemi.values()}

    def nome_strumento(chiave):
        return src.nome_strumento.get(src.strumento_frontiera.get(chiave, ""), chiave)

    # L'ordine delle colonne EV del foglio si decide sui dati, provando i due ordini plausibili.
    ordini = {
        "PS/Att/Dif/AttSp/DifSp/Vel": ["HP", "ATTACK", "DEFENSE", "SP_ATTACK", "SP_DEFENSE", "SPEED"],
        "PS/Att/Dif/Vel/AttSp/DifSp": ["HP", "ATTACK", "DEFENSE", "SPEED", "SP_ATTACK", "SP_DEFENSE"],
    }

    # --- Parte 1 -----------------------------------------------------------
    p("1. Insiemi del foglio contro gBattleFrontierMons")
    p("-" * 68)
    esiti = []
    nomi_ignoti = collections.Counter()
    for r in insiemi_foglio:
        specie = specie_da_nome.get(norma(r.get("Species")))
        numero = r.get("Set#")
        try:
            numero = int(numero)
        except (TypeError, ValueError):
            numero = None
        mosse_f = []
        for k in ("Move 1", "Move 2", "Move 3", "Move 4"):
            v = r.get(k)
            if v is None or not str(v).strip() or str(v).strip() in ("-", "---"):
                mosse_f.append("MOVE_NONE")
            else:
                mm = mossa_da_nome.get(norma(v))
                if mm is None:
                    nomi_ignoti["mossa: %s" % v] += 1
                mosse_f.append(mm or ("?" + str(v)))
        if specie is None:
            nomi_ignoti["specie: %s" % r.get("Species")] += 1
        esiti.append({"r": r, "specie": specie, "numero": numero, "mosse": mosse_f,
                      "ev": ev_del_foglio(r.get("EV Spread"))})

    punteggio_ordine = {}
    for nome_ordine, ordine in ordini.items():
        buoni = 0
        for e in esiti:
            s = per_specie_numero.get((e["specie"], e["numero"]))
            if s and e["ev"]:
                atteso = ev_assegnati(s)
                if [atteso[x] for x in ordine] == e["ev"]:
                    buoni += 1
        punteggio_ordine[nome_ordine] = buoni
    ordine_ev_nome = max(punteggio_ordine, key=punteggio_ordine.get)
    ordine_ev = ordini[ordine_ev_nome]
    p("Ordine delle colonne EV del foglio dedotto dai dati: %s (concordi per ordine: %s)" % (
        ordine_ev_nome, ", ".join("%s=%d" % kv for kv in punteggio_ordine.items())))

    def firma(specie, natura, strumento, mosse, ev):
        return (specie, natura, strumento, tuple(mosse), tuple(ev) if ev else None)

    firme_sorgente = collections.defaultdict(list)
    for s in src.insiemi.values():
        atteso = ev_assegnati(s)
        firme_sorgente[firma(s["specie"], s["natura"], s["strumento"], s["mosse"], [atteso[x] for x in ordine_ev])].append(s["id"])
    strumento_da_nome = {norma(nome_strumento(k)): k for k in src.strumento_frontiera}

    identici, divergenti, assenti = [], [], []
    coperti = set()
    for e in esiti:
        r = e["r"]
        natura = norma(r.get("Nature"))
        strumento = strumento_da_nome.get(norma(r.get("Item")))
        if strumento is None and r.get("Item"):
            nomi_ignoti["strumento: %s" % r.get("Item")] += 1
        e["natura"], e["strumento"] = natura, strumento
        s = per_specie_numero.get((e["specie"], e["numero"]))
        per_contenuto = firme_sorgente.get(firma(e["specie"], natura, strumento, e["mosse"], e["ev"]), [])
        e["per_contenuto"] = per_contenuto
        if s is None:
            e["id"] = per_contenuto[0] if per_contenuto else None
            assenti.append(e)
            if e["id"] is not None:
                coperti.add(e["id"])
            continue
        e["id"] = s["id"]
        coperti.add(s["id"])
        diff = []
        if s["natura"] != natura:
            diff.append("natura foglio %s, sorgente %s" % (r.get("Nature"), s["natura"].title()))
        if s["strumento"] != strumento:
            diff.append("strumento foglio %s, sorgente %s" % (r.get("Item"), nome_strumento(s["strumento"])))
        if s["mosse"] != e["mosse"]:
            if sorted(s["mosse"]) == sorted(e["mosse"]):
                diff.append("mosse uguali in ordine diverso")
            else:
                diff.append("mosse foglio %s, sorgente %s" % (
                    "/".join(str(r.get(k)) for k in ("Move 1", "Move 2", "Move 3", "Move 4")),
                    "/".join(src.nome_mossa.get(m, m) for m in s["mosse"])))
        atteso = ev_assegnati(s)
        if e["ev"] != [atteso[x] for x in ordine_ev]:
            diff.append("EV foglio %s, sorgente %s" % (str(r.get("EV Spread")).strip(), "/".join(str(atteso[x]) for x in ordine_ev)))
        base = src.base.get(s["specie"], {})
        tipi_f = sorted("TYPE_" + t.upper() for t in str(r.get("Type") or "").split())
        if base and tipi_f != base["tipi"]:
            diff.append("tipi foglio %s, sorgente %s" % (r.get("Type"), "/".join(t[5:].title() for t in base["tipi"])))
        abil_f = sorted(set(norma(a) for a in str(r.get("Possible Ability") or "").split("/") if a.strip()))
        abil_s = sorted(set(norma(src.nome_abilita[a]) for a in base.get("abilita", [])))
        if base and abil_f != abil_s:
            diff.append("abilità foglio %s, sorgente %s" % (r.get("Possible Ability"), " / ".join(src.nome_abilita[a] for a in base["abilita"])))
        e["diff"] = diff
        (divergenti if diff else identici).append(e)

    p("Righe confrontate: %d; identiche su specie, numero, natura, strumento, mosse, EV, tipi e abilità: %d; divergenti: %d; senza insieme con quel nome nel sorgente: %d" % (
        len(esiti), len(identici), len(divergenti), len(assenti)))
    if nomi_ignoti:
        p("Nomi del foglio che non corrispondono a nessun nome del sorgente:")
        for k, v in sorted(nomi_ignoti.items()):
            p("  %s (%d righe)" % (k, v))
    duplicati = [k for k, v in collections.Counter((e["specie"], e["numero"]) for e in esiti).items() if v > 1]
    p("Righe duplicate (stessa specie e numero): %d%s" % (len(duplicati), "" if not duplicati else " -> " + ", ".join(
        "%s %s" % (src.nome_specie.get(a, a), b) for a, b in duplicati)))
    if divergenti:
        p("")
        p("Divergenze, riga del foglio -> costante e riga di %s:" % src.file_insiemi)
        for e in divergenti:
            s = src.insiemi[e["id"]]
            nota = ""
            if e["per_contenuto"] and e["id"] not in e["per_contenuto"]:
                nota = " [il contenuto del foglio coincide invece con %s]" % ", ".join(
                    "%s (%d)" % (src.insiemi[i]["costante"], i) for i in e["per_contenuto"])
            p("  riga %d %s %s -> %s = %d, riga %d: %s%s" % (e["r"]["_riga"], e["r"].get("Species"), e["numero"],
                                                         s["costante"], s["id"], s["riga"], "; ".join(e["diff"]), nota))
    if assenti:
        p("")
        p("Righe senza insieme omonimo nel sorgente:")
        for e in assenti:
            p("  riga %d %s %s%s" % (e["r"]["_riga"], e["r"].get("Species"), e["numero"],
                                    " (contenuto identico a %s)" % e["per_contenuto"] if e["per_contenuto"] else ""))

    p("")
    p("Copertura: il foglio copre %d numeri FRONTIER_MON distinti: %s" % (len(coperti), intervalli_di(coperti)))
    p("Intervalli di pesca dell'Azienda al livello 50, src/battle_factory.c:%d (sInitialRentalMonRanges, righe 0-7):" % src.riga_intervalli)
    unione_50 = set()
    for sfida, (a, b) in enumerate(src.intervalli_50):
        tratto = set(range(a, b + 1))
        dentro = len(tratto & coperti)
        unione_50 |= tratto
        etichetta = "sfida %d (lotte %d-%d)" % (sfida, sfida * 7 + 1, sfida * 7 + 7) if sfida < 7 else "sfida 7 e oltre (lotte 50+)"
        p("  %s: %d-%d, %d insiemi, di cui nel foglio %d" % (etichetta, a, b, b - a + 1, dentro))
    unione_50 = {i for i in unione_50 if i <= src.alto_livello}
    p("Unione degli intervalli al livello 50, con il taglio monId > FRONTIER_MONS_HIGH_TIER = %d (include/constants/battle_frontier_mons.h:%d): %d insiemi (%s)" % (
        src.alto_livello, src.riga_alto_livello, len(unione_50), intervalli_di(unione_50)))
    fuori = sorted(coperti - unione_50)
    p("Insiemi del foglio fuori da ogni intervallo del livello 50: %d%s" % (len(fuori), "" if not fuori else " -> " + ", ".join(
        "%s (%d)" % (src.etichetta(i), i) for i in fuori)))
    mancanti = sorted(unione_50 - coperti)
    unown = [i for i in mancanti if src.insiemi[i]["specie"] == "SPECIES_UNOWN"]
    p("Insiemi pescabili al livello 50 che il foglio non porta: %d (%s), di cui Unown, che il gioco scarta sempre come avversario (src/battle_factory.c:337): %d" % (
        len(mancanti), intervalli_di(mancanti), len(unown)))
    aperto = set()
    for a, b in src.intervalli[8:]:
        aperto |= set(range(a, b + 1))
    p("Unione degli intervalli del Livello Aperto (righe 8-15 della stessa tabella): %d insiemi (%s); coincide con la copertura del foglio: %s" % (
        len(aperto), intervalli_di(aperto), "sì" if aperto == coperti else "no"))
    fasce = collections.Counter()
    for i in coperti:
        n = src.insiemi[i]["numero"]
        fasce[n] += 1
    p("Numero d'insieme dei set coperti: %s" % ", ".join("%d -> %d" % kv for kv in sorted(fasce.items())))
    p("")

    # --- Parte 2 -----------------------------------------------------------
    p("2. Colonna \"Style #\" contro GetMoveBattleStyle")
    p("-" * 68)
    p("Tabelle di stile, src/battle_factory.c:%d (sMoveStyles), soglie src/battle_factory.c:%d (sRequiredMoveCounts):" % (src.riga_stili, src.riga_soglie))
    for codice, stile, tabella, mosse in src.ordine_stili:
        p("  %d = FACTORY_STYLE_%s (%s, %d mosse, soglia di squadra %d)" % (codice, stile, tabella, len(mosse), src.soglie_stile.get(stile, 0)))
    p("  0 = FACTORY_STYLE_NONE, ogni mossa che non sta in nessuna tabella")
    if src.mosse_in_piu_stili:
        p("Mosse in più tabelle, dove vince la prima: %s" % ", ".join("%s in %s" % (k[5:], "+".join(v)) for k, v in src.mosse_in_piu_stili.items()))
    concordi, discordi, illeggibili = 0, [], 0
    for e in esiti:
        cifre = re.findall(r"\d", str(e["r"].get("Style #") or ""))
        if len(cifre) != 4:
            illeggibili += 1
            continue
        attese = [src.stile_mossa(m) for m in e["mosse"]]
        if [int(c) for c in cifre] == attese:
            concordi += 1
        else:
            discordi.append((e, cifre, attese))
    p("Righe con quattro cifre leggibili: %d; concordi mossa per mossa: %d; discordi: %d; illeggibili: %d" % (
        len(esiti) - illeggibili, concordi, len(discordi), illeggibili))
    for e, cifre, attese in discordi:
        p("  riga %d %s %s: foglio %s, sorgente %s (%s)" % (e["r"]["_riga"], e["r"].get("Species"), e["numero"], " ".join(cifre),
                                                        " ".join(map(str, attese)), "/".join(str(e["r"].get(k)) for k in ("Move 1", "Move 2", "Move 3", "Move 4"))))
    p("")

    # --- Parte 3 -----------------------------------------------------------
    p("3. Colonna \"Speed\"")
    p("-" * 68)
    candidati = {}
    for livello in (50, 100):
        for iv in range(32):
            buoni = 0
            for e in identici + divergenti:
                s = src.insiemi[e["id"]]
                try:
                    v = int(e["r"].get("Speed"))
                except (TypeError, ValueError):
                    continue
                if velocita(src.base[s["specie"]]["SPEED"], iv, ev_assegnati(s)["SPEED"], livello, s["natura"]) == v:
                    buoni += 1
            candidati[(livello, iv)] = buoni
    migliori = sorted(candidati.items(), key=lambda kv: -kv[1])[:4]
    totale_v = sum(1 for e in identici + divergenti if str(e["r"].get("Speed") or "").strip().isdigit())
    p("Righe con velocità numerica e insieme identificato: %d" % totale_v)
    p("Combinazioni che tornano su più righe (livello, IV): %s" % ", ".join("L%d IV%d -> %d" % (k[0], k[1], v) for k, v in migliori))
    (liv, ivm), _ = migliori[0]
    scarti = []
    for e in identici + divergenti:
        s = src.insiemi[e["id"]]
        try:
            v = int(e["r"].get("Speed"))
        except (TypeError, ValueError):
            continue
        calc = velocita(src.base[s["specie"]]["SPEED"], ivm, ev_assegnati(s)["SPEED"], liv, s["natura"])
        if calc != v:
            scarti.append((e, v, calc, s))
    p("Con livello %d e IV %d, righe che non tornano: %d" % (liv, ivm, len(scarti)))
    def fattore(natura):
        indice = NATURE.index(natura)
        if indice // 5 == 2 and indice % 5 != 2:
            return 1.1
        if indice % 5 == 2 and indice // 5 != 2:
            return 0.9
        return 1.0

    for e, v, calc, s in scarti:
        grezza = velocita(src.base[s["specie"]]["SPEED"], ivm, ev_assegnati(s)["SPEED"], liv, "HARDY")
        k = fattore(s["natura"])
        p("  riga %d %s %s: foglio %d, calcolato %d (natura %s; senza natura %d, per %.1f fa %.1f: il foglio arrotonda invece di troncare)" % (
            e["r"]["_riga"], e["r"].get("Species"), e["numero"], v, calc, s["natura"].title(), grezza, k, grezza * k))
    modificate, meta_su = 0, 0
    for e in identici + divergenti:
        s = src.insiemi[e["id"]]
        k = fattore(s["natura"])
        if k == 1.0:
            continue
        modificate += 1
        grezza = velocita(src.base[s["specie"]]["SPEED"], ivm, ev_assegnati(s)["SPEED"], liv, "HARDY")
        if (grezza * k) % 1 >= 0.5 - 1e-9:
            meta_su += 1
    p("Righe con una natura che modifica la velocità: %d; di queste, con parte decimale di almeno 0,5 dopo il 10%%: %d; righe sbagliate: %d. %s" % (
        modificate, meta_su, len(scarti),
        "Il foglio arrotonda sistematicamente dove il gioco tronca." if meta_su == len(scarti) else
        "Gli scarti non sono sistematici: il foglio tronca quasi sempre come il gioco, e i casi sbagliati sono refusi isolati."))
    tab = src.fabbrica[src.fabbrica.index("sFixedIVTable[][2] ="):]
    tab = tab[:tab.index("};")]
    coppie = re.findall(r"\{\s*(\d+)\s*,\s*(\d+)\s*\}", tab)
    p("sFixedIVTable (src/battle_factory.c:%d), per indice di sfida: %s" % (riga_di(src.fabbrica, src.fabbrica.index("sFixedIVTable[][2] =")),
        ", ".join("%d: %s/%s" % (i, a, b) for i, (a, b) in enumerate(coppie))))
    p("Formula usata: floor(floor((2*base + IV + floor(EV/4)) * livello / 100) + 5) per il modificatore di natura, con EV = 510 / numero di statistiche marcate in evSpread (src/pokemon.c, CreateMonWithEVSpreadNatureOTID).")
    p("IV reali degli avversari dell'Azienda: sFixedIVTable in src/battle_factory.c, scelti da GetFactoryMonFixedIV; FillFactoryFrontierTrainerParty (src/battle_tower.c) usa per errore la serie della Torre Lotta livello 50 e non quella dell'Azienda.")
    p("")

    # --- Parte 4 -----------------------------------------------------------
    p("4. Scheda Trainers contro gBattleFrontierTrainers")
    p("-" * 68)
    etichette = {i: norma(src.etichetta(i)) for i in src.insiemi}
    uguali, diversi = 0, []
    for n, (f, s) in enumerate(zip(allenatori_foglio, src.allenatori)):
        problemi = []
        if norma(f["nome"]) != norma(s["nome"]):
            problemi.append("nome foglio %s, sorgente %s" % (f["nome"], s["nome"]))
        # Il foglio scrive la classe come il gioco la mostra, più fra parentesi la variante di
        # struttura (sesso, e per i triatleti la disciplina), che si confronta con FACILITY_CLASS_*.
        classe_f = re.match(r"([^(]*)(?:\((.*)\))?", f["classe"])
        sinonimi = {"RUNNER": "RUNNING", "SWIMMER": "SWIMMING", "BIKER": "CYCLING"}
        variante = {sinonimi.get(x, x) for x in re.findall(r"[A-Z]+", (classe_f.group(2) or "").upper())}
        parole_struttura = set(s["classe"][len("FACILITY_CLASS_"):].split("_"))
        if norma(classe_f.group(1)) != norma(s["nome_classe"]) or not variante <= parole_struttura:
            problemi.append("classe foglio %s, sorgente %s (%s)" % (f["classe"], s["nome_classe"], s["classe"]))
        attese = [etichette[i] for i in s["elenco"]]
        ottenute = [norma(x) for x in f["elenco"]]
        if attese != ottenute:
            if sorted(attese) == sorted(ottenute):
                problemi.append("stessi insiemi in ordine diverso")
            else:
                mancano = collections.Counter(attese) - collections.Counter(ottenute)
                in_piu = collections.Counter(ottenute) - collections.Counter(attese)
                problemi.append("elenco: foglio %d, sorgente %d; mancano nel foglio %s; in più nel foglio %s" % (
                    len(ottenute), len(attese), sorted(mancano.elements())[:12] or "-", sorted(in_piu.elements())[:12] or "-"))
        if problemi:
            diversi.append((n, f, s, problemi))
        else:
            uguali += 1
    p("Allenatori confrontati per posizione (id 0-%d): %d; identici su nome, classe ed elenco ordinato: %d; diversi: %d" % (
        min(len(allenatori_foglio), len(src.allenatori)) - 1, min(len(allenatori_foglio), len(src.allenatori)), uguali, len(diversi)))
    for n, f, s, problemi in diversi:
        p("  id %d, riga %d del foglio, %s (%s:%d, elenco %s:%d): %s" % (n, f["_riga"], s["costante"], src.file_allenatori, s["riga"],
                                                                    src.file_elenchi, s["riga_elenco"], "; ".join(problemi)))
    lunghezze = [len(s["elenco"]) for s in src.allenatori]
    p("Lunghezza degli elenchi nel sorgente: minimo %d, massimo %d" % (min(lunghezze), max(lunghezze)))
    p("Uso degli elenchi nell'Azienda: GenerateOpponentMons (src/battle_factory.c:303) sceglie l'allenatore con GetRandomScaledFrontierTrainerId e poi pesca i sei insiemi con GetFactoryMonId, cioè dagli intervalli di sInitialRentalMonRanges, senza leggere il monSet dell'allenatore. Nell'Azienda l'allenatore decide solo nome, aspetto e frasi; l'elenco della scheda Trainers vale per le strutture che passano da FillTrainerParty, che legge monSet (src/battle_tower.c:1633 e 1648), non per l'Azienda, che passa da FillFactoryTrainerParty (src/battle_tower.c:1815) e usa gFrontierTempParty.")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--foglio", default=str(FOGLIO_PREDEFINITO))
    ap.add_argument("--sorgente", default=str(SORGENTE_PREDEFINITO))
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    src = Sorgente(args.sorgente)
    sys.stdout.write(confronta(src, args.foglio))


if __name__ == "__main__":
    main()
