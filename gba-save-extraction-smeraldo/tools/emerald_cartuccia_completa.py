#!/usr/bin/env python3
"""Compone la cartuccia di Smeraldo come collezione completa di terza generazione, secondo ADR-076, in un file NUOVO.

Perche' esiste
--------------

ADR-076 chiede una scrittura sola che porti il deposito da quello che e' oggi a quello deciso dal proprietario il 2026-09-23. Dalla collezione escono le undici copie del noleggio dell'Azienda Lotta e i ventisette cromatici del codice Action Replay, perche' nessuno dei due gruppi e' stato catturato da una persona; delle catture vere resta per ogni specie la piu' vecchia, cioe' la prima nel deposito; i cloni del glitch di clonazione che sopravvivono a questa selezione diventano incontri distinti; Seedot e Wurmple ricevono la Poke Ball. Entrano i 176 eventi di terza generazione in tutte le lingue, i 19 scambi in gioco, i 14 incontri da biglietto dell'allenatore Alessio, e il Lotad e il Seedot con la taglia massima. Il lotto del Parco Lotta passa all'ottavo giro, senza la copia 2 delle cinque riserve meno usate. Il deposito arriva a 420 su 420.

Due opzioni aggiunte il 2026-09-23 dopo la seconda decisione del proprietario: `--senza-copie-di-scambio` toglie dal lotto tutte le copie 2, e `--rientrano` fa restare nella collezione i doppioni indicati per posizione, purche' siano catture distinte e non cloni di un esemplare tenuto. Cosi' i posti delle copie di scambio passano a catture vere.

Dal 2026-09-23, per ADR-078, con `--senza-copie-di-scambio` il lotto non resta dove l'ha messo il settimo giro ma passa alla disposizione finale di `parco_lotta_percorso_oro.disposizione`, in coda al deposito: la collezione e le aggiunte occupano senza buchi i box dal primo in poi, e l'ultimo esemplare del lotto sta nell'ultima posizione del box 14.

Riusa le funzioni gia' verificate di `emerald_risana_deposito.py` invece di riscriverle: la classificazione degli irregolari dal dump di PKHeX, la ricerca di una personalita' del primo metodo con natura, sesso e allenatore dati, e la generazione di un esemplare distinto dell'evento 10ANNI.

La disposizione
---------------

La collezione occupa i primi box nell'ordine in cui sta oggi. Gli esemplari nuovi seguono nell'ordine eventi, incontri da biglietto, scambi in gioco, giganti, e riempiono ogni posizione libera fuori dal lotto, comprese le cinque lasciate dalle copie di scambio tolte. Il lotto resta nelle posizioni della funzione `disposizione`, che la guida documenta. Gli sfondi seguono il tema per contenuto di ADR-075, esteso: uno sfondo ordinario diverso per ogni box fino all'undicesimo, e lo sfondo Amici sui tre del lotto.

Le personalita' condivise ammesse
---------------------------------

Una sola eccezione alla regola che nessuna personalita' si ripeta, e va dichiarata perche' altrimenti sembrerebbe un clone: gli scambi in gioco di Rosso Fuoco e di Verde Foglia hanno la personalita' fissata nel codice del gioco, quindi lo stesso scambio fatto su entrambe le cartucce da' due esemplari con la stessa personalita', e chi possiede le due cartucce li ha davvero. Lo strumento ammette una personalita' condivisa soltanto fra esemplari che vengono entrambi dai file degli scambi in gioco, o fra uno di quelli e un esemplare della collezione con la medesima personalita' fissa.

Uso
---

    python gba-save-extraction-smeraldo/tools/emerald_cartuccia_completa.py INGRESSO.sav USCITA.sav --dump "... round 3.csv" --lotto-precedente _notes/lotto-parco-lotta/esemplari-round7 [--senza-copie-di-scambio] [--rientrano B1-26,B9-5]
"""

import argparse
import collections
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
sys.path.insert(0, str(RADICE.joinpath("pokemon-gen12-gen3-bridge-original-hardware")))

from pokebridge import gen3, save3  # noqa: E402

NOTE = RADICE.joinpath("_notes")
LOTTO = NOTE.joinpath("lotto-parco-lotta", "esemplari")
AGGIUNTE = [("evento", NOTE.joinpath("lotto-eventi")), ("biglietto", NOTE.joinpath("lotto-incontri-gen3")),
            ("scambio", NOTE.joinpath("lotto-scambi-gen3"))]
GIGANTI = NOTE.joinpath("lotto-giganti")
SENZA_COPIA_DUE = ["marowak-jolly", "regirock-adamant", "steelix-adamant", "dusclops-bold", "scizor-adamant"]
PER_BOX = 30
VUOTO = bytes(save3.RECORD)
SFONDI = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 16, 16]
# ADR-078: con il lotto in coda il box 12 contiene soltanto eventi, e prende uno sfondo ordinario
SFONDI_FINALI = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 16]
NOMI_SFONDI = ["Forest", "City", "Desert", "Savanna", "Crag", "Volcano", "Snow", "Cave", "Beach",
               "Seafloor", "River", "Sky", "Polkadot", "Pokecenter", "Machine", "Plain", "Friends"]


def _modulo(nome):
    percorso = Path(__file__).resolve().parent.joinpath(nome + ".py")
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def personalita(record):
    return int.from_bytes(record[:4], "little")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("ingresso")
    p.add_argument("uscita")
    p.add_argument("--dump", required=True)
    p.add_argument("--lotto-precedente", required=True)
    p.add_argument("--senza-copie-di-scambio", action="store_true",
                   help="toglie dal lotto tutte le copie 2, non solo le cinque di SENZA_COPIA_DUE")
    p.add_argument("--rientrano", default="",
                   help="posizioni del deposito d'ingresso, nella forma B7-2,B9-5, di doppioni da tenere perche' catture distinte")
    args = p.parse_args()
    ingresso, uscita = Path(args.ingresso), Path(args.uscita)
    if uscita.exists() or uscita.resolve() == ingresso.resolve():
        sys.exit("l'uscita esiste gia' o coincide con l'ingresso: questo strumento non sovrascrive")

    risana = _modulo("emerald_risana_deposito")
    gen = _modulo("genera_squadre_parco_lotta")
    percorso = _modulo("parco_lotta_percorso_oro")
    dati = json.loads(CARTELLA.joinpath("dati-gen3.json").read_text(encoding="utf-8"))
    per_id = {v["id"]: (nome, v) for nome, v in dati["specie"].items()}
    catalogo = json.loads(CARTELLA.joinpath("squadre-parco-lotta.json").read_text(encoding="utf-8"))
    thread = json.loads(percorso._mappa().THREAD.read_text(encoding="utf-8"))
    # l'ingresso e' il READBACK del settimo giro, quindi si verifica sulla disposizione storica; l'uscita
    # usa quella di ADR-078 quando le copie di scambio escono tutte, cioe' il lotto in coda al box 14
    _, posizioni, _, _ = percorso.disposizione(catalogo, thread, storica=True)
    _, finale, _, _ = percorso.disposizione(catalogo, thread)

    grezzo = ingresso.read_bytes()
    vecchio = save3.Save3(grezzo)
    if not vecchio.integro():
        sys.exit("lo slot attivo dell'ingresso non e' integro")
    posti = [vecchio.leggi_posizione(i) for i in range(save3.POSIZIONI)]

    # 1. il lotto: il giro precedente deve esserci; il nuovo entra senza le cinque copie di scambio
    lotto = {}
    for (chiave, copia), (box, n) in posizioni.items():
        indice = (box - 1) * PER_BOX + n - 1
        if posti[indice] != Path(args.lotto_precedente).joinpath("%s-copia%d.bin" % (chiave, copia)).read_bytes():
            sys.exit("il box %d, posizione %d, non contiene il giro precedente del lotto" % (box, n))
        if copia == 2 and (args.senza_copie_di_scambio or chiave in SENZA_COPIA_DUE):
            continue
        if args.senza_copie_di_scambio:
            box, n = finale[(chiave, 1)]
            destinazione = (box - 1) * PER_BOX + n - 1
        else:
            destinazione = indice
        lotto[destinazione] = LOTTO.joinpath("%s-copia%d.bin" % (chiave, copia)).read_bytes()
    posti_lotto = {(box - 1) * PER_BOX + n - 1 for (box, n) in posizioni.values()}

    # 2. la collezione: via noleggio e cromatici forzati, Poke Ball a Seedot e Wurmple
    irregolari = risana.classifica(args.dump)
    for indice, (causa, pid, specie) in irregolari.items():
        if personalita(posti[indice]) != pid:
            sys.exit("la posizione %d non contiene piu' il %s del dump" % (indice, specie))
    rapporto = collections.Counter()
    collezione = []
    for indice in range(save3.POSIZIONI):
        if indice in posti_lotto or posti[indice] == VUOTO:
            continue
        causa = irregolari.get(indice, (None,))[0]
        if causa in ("noleggio", "cromatico"):
            rapporto["tolti, " + causa] += 1
            continue
        record = posti[indice]
        if causa == "sfera":
            mon = gen3.Gen3Mon.from_bytes(record).with_personality(personalita(record))
            mon.misc.pokeball = risana.POKE_BALL
            record = mon.to_bytes()
            rapporto["sfera corretta"] += 1
        collezione.append((indice, record))

    # 3. i doppioni: per ogni specie resta la cattura piu' vecchia, cioe' la prima nel deposito
    # tranne quelli che il proprietario fa rientrare: devono essere catture distinte, non cloni di un esemplare tenuto
    rientrano = set()
    for voce in filter(None, (v.strip() for v in args.rientrano.split(","))):
        box, n = voce.upper().lstrip("B").split("-")
        rientrano.add((int(box) - 1) * PER_BOX + int(n) - 1)
    trovati = {indice for indice, _ in collezione} & rientrano
    if trovati != rientrano:
        sys.exit("posizioni da far rientrare assenti dalla collezione: %s" % sorted(rientrano - trovati))
    viste = set()
    pid_visti = set()
    tenuti = []
    for indice, record in collezione:
        specie = gen3.Gen3Mon.from_bytes(record).growth.species
        if specie in viste and indice in rientrano:
            if personalita(record) in pid_visti:
                sys.exit("la posizione %d e' un clone di un esemplare tenuto e non puo' rientrare" % indice)
            rapporto["doppione rientrato"] += 1
        elif specie in viste:
            rapporto["tolti, doppione"] += 1
            continue
        viste.add(specie)
        pid_visti.add(personalita(record))
        tenuti.append((indice, record))

    # 4. i cloni superstiti: in ogni gruppo con la stessa personalita' il primo resta, gli altri diventano distinti
    incontri = risana.incontri_del_dump(args.dump)
    escluse = {personalita(r) for _, r in tenuti} | {personalita(r) for r in lotto.values()}
    gruppi = collections.defaultdict(list)
    for posto, (indice, record) in enumerate(tenuti):
        gruppi[personalita(record)].append(posto)
    for pid, membri in gruppi.items():
        for posto in membri[1:]:
            indice, record = tenuti[posto]
            tipo, cromatico, _ = incontri[indice]
            mon = gen3.Gen3Mon.from_bytes(record)
            nome, info = per_id[mon.growth.species]
            if tipo.startswith("Event Gift"):
                esito = risana.evento_diverso(mon, escluse)
                nuova, iv = esito["personalita"], esito["iv"]
                iv = {"hp": iv["ps"], "atk": iv["attacco"], "def": iv["difesa"], "spd": iv["velocita"],
                      "satk": iv["attacco_speciale"], "sdef": iv["difesa_speciale"]}
            else:
                soglia = info.get("soglia_femmina")
                nuova, iv2, _seme = risana.cerca_cromatico(gen.NATURE[mon.personality % 25],
                                                           soglia is not None and (mon.personality & 0xFF) < soglia,
                                                           soglia, escluse, indice * 40503 + 7,
                                                           mon.ot_id & 0xFFFF, mon.ot_id >> 16, cromatico)
                iv = {"hp": iv2["hp"], "atk": iv2["atk"], "def": iv2["def"], "spd": iv2["spe"],
                      "satk": iv2["spa"], "sdef": iv2["spd"]}
            escluse.add(nuova)
            mon = mon.with_personality(nuova)
            mon.misc.ivs = iv
            mon.misc.ability_num = gen.bit_abilita_di(info["abilita"], nuova)
            tenuti[posto] = (indice, mon.to_bytes())
            rapporto["clone reso distinto"] += 1

    # 5. le aggiunte, nella forma cifrata che il salvataggio vuole
    aggiunte = []
    for tipo, cartella in AGGIUNTE:
        for f in sorted(cartella.glob("*.pk3")):
            cifrato = cartella.joinpath("forma-cifrata", f.stem + ".ek3").read_bytes()
            if cifrato != save3.record_da_file(f.read_bytes()):
                sys.exit("la forma cifrata di %s non corrisponde al file" % f.name)
            aggiunte.append((tipo, f.stem, cifrato))
    for f in sorted(GIGANTI.glob("*-gigante.bin")):
        aggiunte.append(("gigante", f.stem, f.read_bytes()))
    rapporto.update(t for t, _, _ in aggiunte)

    # 6. la disposizione: collezione dall'inizio, poi le aggiunte in ogni posizione libera fuori dal lotto
    previsto = [VUOTO] * save3.POSIZIONI
    for indice, r in lotto.items():
        previsto[indice] = r
    liberi = [i for i in range(save3.POSIZIONI) if i not in lotto]
    da_mettere = [r for _, r in tenuti] + [r for _, _, r in aggiunte]
    if len(da_mettere) > len(liberi):
        sys.exit("servono %d posizioni e ne restano %d" % (len(da_mettere), len(liberi)))
    for i, r in zip(liberi, da_mettere):
        previsto[i] = r

    nuovo = save3.Save3(grezzo)
    for i, r in enumerate(previsto):
        nuovo.scrivi_posizione(i, r)
    sfondi = SFONDI_FINALI if args.senza_copie_di_scambio else SFONDI
    nuovo._scrivi_in_buffer(save3.SEZIONI_STORAGE, save3.OFF_SFONDI, bytes(sfondi))
    prodotto = nuovo.to_bytes()

    # 7. la verifica, dai byte prodotti
    riletto = save3.Save3(prodotto)
    errori = []
    if not riletto.integro():
        errori.append("slot attivo non integro")
    letti = [riletto.leggi_posizione(i) for i in range(save3.POSIZIONI)]
    if letti != previsto:
        errori.append("le posizioni non sono quelle previste")
    for i, r in enumerate(letti):
        if r != VUOTO:
            try:
                if gen3.Gen3Mon.from_bytes(r).to_bytes() != r:
                    errori.append("posizione %d non simmetrica" % i)
            except Exception as e:
                errori.append("posizione %d illeggibile: %s" % (i, e))
    scambi = {personalita(save3.record_da_file(f.read_bytes())) for f in NOTE.joinpath("lotto-scambi-gen3").glob("*.pk3")}
    conteggio = collections.Counter(personalita(r) for r in letti if r != VUOTO)
    condivise = [pid for pid, n in conteggio.items() if n > 1]
    non_ammesse = [pid for pid in condivise if pid not in scambi]
    if non_ammesse:
        errori.append("%d personalita' condivise fuori dall'eccezione degli scambi a personalita' fissa, per esempio %08X"
                      % (len(non_ammesse), non_ammesse[0]))
    if riletto.small() != vecchio.small() or riletto.large() != vecchio.large():
        errori.append("i dati fuori dal deposito sono cambiati")
    base = (1 - vecchio.attivo) * save3.SLOT
    if prodotto[base:base + save3.SLOT] != grezzo[base:base + save3.SLOT]:
        errori.append("lo slot inattivo e' cambiato")
    st = riletto.storage()
    if list(st[save3.OFF_SFONDI:save3.OFF_SFONDI + 14]) != sfondi:
        errori.append("sfondi non scritti")
    if st[save3.OFF_NOMI_BOX:save3.OFF_SFONDI] != vecchio.storage()[save3.OFF_NOMI_BOX:save3.OFF_SFONDI]:
        errori.append("nomi dei box cambiati")
    if errori:
        for e in errori:
            print("VERIFICA FALLITA: %s" % e)
        sys.exit("il file non e' stato scritto")

    uscita.write_bytes(prodotto)
    occupati = sum(1 for r in letti if r != VUOTO)
    for k, v in sorted(rapporto.items()):
        print("  %-28s %d" % (k, v))
    print("collezione %d, aggiunte %d, lotto %d: %d posizioni occupate su %d" % (
        len(tenuti), len(aggiunte), len(lotto), occupati, save3.POSIZIONI))
    print("personalita' condivise ammesse, scambi a personalita' fissa: %d" % len(condivise))
    print("sfondi: " + ", ".join("BOX %d %s" % (i + 1, NOMI_SFONDI[s]) for i, s in enumerate(sfondi)))
    print("scritto %s" % uscita)
    print("SHA-256 %s" % hashlib.sha256(prodotto).hexdigest())


if __name__ == "__main__":
    main()
