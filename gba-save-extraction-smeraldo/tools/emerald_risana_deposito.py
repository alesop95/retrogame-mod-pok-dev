#!/usr/bin/env python3
"""Risana gli esemplari irregolari del deposito di Smeraldo secondo ADR-075, e nella stessa scrittura aggiorna il lotto del Parco Lotta e gli sfondi dei box.

Perche' esiste
--------------

ADR-075 chiude Smeraldo con una scrittura sola che porta quattro cambiamenti. I quaranta esemplari che PKHeX giudica irregolari si trattano ciascuno secondo la sua causa: le undici copie livello cento del noleggio dell'Azienda Lotta si cancellano, perche' il gioco non le consegna mai; i ventisette cromatici del codice Action Replay si rigenerano cromatici con un seme reale; Seedot e Wurmple ricevono la Poke Ball al posto della Safari Ball. Il deposito si ricompatta, cosi' che la cancellazione non lasci buchi. Il lotto riceve l'ottavo giro, che corregge l'amicizia degli esemplari con Ritorno. E i quattordici box ricevono gli sfondi decisi.

Il risanamento dei cromatici, spiegato
---------------------------------------

Il codice che li ha prodotti scriveva la stessa personalita' `007EB2C1` e un identificativo segreto alterato, 126 al posto di quello vero: accanto ai valori individuali dell'esemplare, quella personalita' non forma alcuna coppia del primo metodo, ed e' cio' che il verificatore rifiuta. Un cromatico selvatico legittimo esiste, e nasce come ogni incontro statico o selvatico di Smeraldo da un seme del generatore: le prime due estrazioni danno la meta' bassa e la meta' alta della personalita', le due successive le due parole dei valori individuali. Qui la ricerca e' rovesciata come negli altri strumenti del progetto: si fissa la meta' bassa, si percorrono i sedici bit ignoti dello stato che la produce, e ogni stato da' una meta' alta; la personalita' e' cromatica se le due meta' in XOR con identificativo e segreto veri scendono sotto otto, cosa che accade una volta su ottomila, quindi bastano poche meta' basse per trovare una personalita' che sia insieme cromatica, della natura voluta e del sesso originale. I valori individuali sono quelli del seme, e non si scelgono: e' il prezzo della legittimita'.

Si conservano specie, livello, esperienza, luogo e livello d'incontro, sfera, mosse, punti base, strumento, amicizia, soprannome, allenatore, natura e sesso. Cambiano personalita', valori individuali, bit dell'abilita' e identificativo segreto, che torna quello vero.

Che cosa garantisce
-------------------

Ogni esemplare da toccare si individua sul dump di PKHeX del file riordinato, `round 3`, e prima di toccarlo si pretende che la posizione contenga la personalita' che quel dump riporta: una partita che nel frattempo avesse spostato un esemplare ferma lo strumento. Le posizioni del lotto devono contenere esattamente il giro precedente, come in `emerald_riordino_deposito.py --sostituisci-lotto`. Dopo la scrittura in memoria il file si rilegge e si verificano integrita', il multinsieme degli esemplari non toccati, la cromaticita' e la correlazione del primo metodo dei risanati, l'assenza di personalita' condivise nell'intero deposito, il lotto, gli sfondi, e l'invarianza di tutto cio' che sta fuori dal deposito.

Uso
---

    python gba-save-extraction-smeraldo/tools/emerald_risana_deposito.py INGRESSO.sav USCITA.sav --dump "BOX DATA DUMP round 3.csv" --lotto-precedente _notes/lotto-parco-lotta/esemplari-round7
"""

import argparse
import collections
import csv
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
sys.path.insert(0, str(RADICE.joinpath("pokemon-gen12-gen3-bridge-original-hardware")))

from pokebridge import gen3, save3  # noqa: E402

LOTTO = RADICE.joinpath("_notes", "lotto-parco-lotta", "esemplari")
CATALOGO = CARTELLA.joinpath("squadre-parco-lotta.json")
DATI = CARTELLA.joinpath("dati-gen3.json")
PER_BOX = 30
BOX_DEPOSITO = 9
VUOTO = bytes(save3.RECORD)
POKE_BALL = 4
TID, SID = 45761, 56446
PERSONALITA_DEL_CODICE = 0x007EB2C1

# Gli sfondi di ADR-075, per box, con gli identificativi di `src/data/wallpapers.h`: nove sfondi
# ordinari diversi sui box della collezione, Plain sui due vuoti, lo sfondo Amici sul lotto.
SFONDI = [0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 15, 16, 16, 16]
NOMI_SFONDI = ["Forest", "City", "Desert", "Savanna", "Crag", "Volcano", "Snow", "Cave", "Beach",
               "Seafloor", "River", "Sky", "Polkadot", "Pokecenter", "Machine", "Plain", "Friends"]


def _modulo(percorso, nome):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def classifica(dump):
    """Dal dump di PKHeX del file riordinato, gli esemplari irregolari dei box 1-9 con la loro causa: {indice: (causa, personalita', specie)}."""
    irregolari = {}
    with open(dump, encoding="utf-8-sig") as f:
        for riga in csv.DictReader(f):
            if riga["Legal"] == "True":
                continue
            m = re.search(r"@ \[(\d+)\] \([^)]*\)-(\d+)", riga["Position"])
            if not m or int(m.group(1)) > BOX_DEPOSITO:
                continue
            indice = (int(m.group(1)) - 1) * PER_BOX + int(m.group(2)) - 1
            if riga["Level"] == "100" and "Invalid" in riga["EncounterType"]:
                causa = "noleggio"
            elif riga["IsShiny"] == "True":
                causa = "cromatico"
            elif "Safari" in riga["Ball"]:
                causa = "sfera"
            else:
                raise SystemExit("irregolare senza una causa prevista da ADR-075: %s in %s" % (riga["Species"], riga["Position"]))
            irregolari[indice] = (causa, int(riga["PID"], 16), riga["Species"])
    return irregolari


def cerca_cromatico(natura, femmina, soglia, escluse, partenza, tid=TID, sid=SID, cromatico=True):
    """Una personalita' del primo metodo, cromatica o no per l'allenatore dato, con natura e sesso dati, e i valori individuali che il suo seme produce."""
    gen = _modulo(CARTELLA.joinpath("tools", "genera_squadre_parco_lotta.py"), "genera")
    bassa = partenza & 0xFFFF
    for _ in range(1 << 16):
        bassa = (bassa * 0x6255 + 0x3039) & 0xFFFF
        for resto in range(1 << 16):
            s1 = (bassa << 16) | resto
            s2 = gen.avanti(s1)
            alta = s2 >> 16
            if (alta ^ bassa ^ tid ^ sid < 8) != cromatico:
                continue
            personalita = (alta << 16) | bassa
            if personalita in escluse or gen.NATURE[personalita % 25] != natura:
                continue
            if soglia is not None and soglia not in (0, 254, 255) and ((personalita & 0xFF) < soglia) != femmina:
                continue
            s3 = gen.avanti(s2)
            s4 = gen.avanti(s3)
            p1, p2 = (s3 >> 16) & 0x7FFF, (s4 >> 16) & 0x7FFF
            iv = {"hp": p1 & 31, "atk": (p1 >> 5) & 31, "def": (p1 >> 10) & 31,
                  "spe": p2 & 31, "spa": (p2 >> 5) & 31, "spd": (p2 >> 10) & 31}
            return personalita, iv, gen.indietro(s1)
    raise SystemExit("nessuna personalita' trovata per natura %s" % natura)


def incontri_del_dump(dump):
    """Tipo d'incontro e cromaticita' di ogni posizione dei box 1-9, dal dump di PKHeX."""
    fuori = {}
    with open(dump, encoding="utf-8-sig") as f:
        for riga in csv.DictReader(f):
            m = re.search(r"@ \[(\d+)\] \([^)]*\)-(\d+)", riga["Position"])
            if m and int(m.group(1)) <= BOX_DEPOSITO:
                indice = (int(m.group(1)) - 1) * PER_BOX + int(m.group(2)) - 1
                fuori[indice] = (riga["EncounterType"], riga["IsShiny"] == "True", int(riga["PID"], 16))
    return fuori


def evento_diverso(mon, escluse):
    """Un nuovo esemplare della distribuzione italiana 10ANNI, metodo BACD_R_A, con lo stesso sesso dell'allenatore e una personalita' non gia' usata.

    Il metodo viene da `EncountersWC3.cs` del verificatore, righe 97 e seguenti, e le formule da `pokebridge.eventi`, verificate su un corpus di duecentonove esemplari conservati. L'evento a seme ristretto ha sessantacinquemila semi possibili, quindi tre copie distinte dello stesso dono esistono davvero: sono tre persone che hanno ricevuto lo stesso evento.
    """
    from pokebridge import eventi
    tid, sid = mon.ot_id & 0xFFFF, mon.ot_id >> 16
    voluto = "femmina" if mon.misc.ot_female else "maschio"
    for seme in eventi.semi_a_sedici_bit():
        esito = eventi.esemplare_da_evento("BACD_R_A", tid, sid, lucentezza="Never", derivazione="RandS7",
                                           semi=[seme])
        if not esito or esito["personalita"] in escluse:
            continue
        if esito.get("sesso_ot") != voluto:
            continue
        return esito
    raise SystemExit("nessun seme dell'evento 10ANNI disponibile")


def correlazione_metodo_uno(personalita, iv):
    gen = _modulo(CARTELLA.joinpath("tools", "genera_squadre_parco_lotta.py"), "genera")
    return personalita in gen.personalita_di_metodo_uno(iv)


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("ingresso")
    p.add_argument("uscita")
    p.add_argument("--dump", required=True, help="il dump di PKHeX del file riordinato, da cui si leggono gli irregolari")
    p.add_argument("--lotto-precedente", required=True, help="la cartella del giro del lotto che la cartuccia contiene")
    args = p.parse_args()
    ingresso, uscita = Path(args.ingresso), Path(args.uscita)
    if uscita.exists() or uscita.resolve() == ingresso.resolve():
        sys.exit("l'uscita esiste gia' o coincide con l'ingresso: questo strumento non sovrascrive")

    grezzo = ingresso.read_bytes()
    vecchio = save3.Save3(grezzo)
    if not vecchio.integro():
        sys.exit("lo slot attivo dell'ingresso non e' integro")
    dati = json.loads(DATI.read_text(encoding="utf-8"))
    per_id = {v["id"]: (nome, v) for nome, v in dati["specie"].items()}
    gen = _modulo(CARTELLA.joinpath("tools", "genera_squadre_parco_lotta.py"), "genera")
    percorso = _modulo(CARTELLA.joinpath("tools", "parco_lotta_percorso_oro.py"), "percorso")
    catalogo = json.loads(CATALOGO.read_text(encoding="utf-8"))
    thread = json.loads(percorso._mappa().THREAD.read_text(encoding="utf-8"))
    _, posizioni, _, _ = percorso.disposizione(catalogo, thread, storica=True)

    posti = [vecchio.leggi_posizione(i) for i in range(save3.POSIZIONI)]

    # 1. il lotto: il giro precedente deve esserci, e si sostituisce con quello corrente
    lotto = {}
    for (chiave, copia), (box, n) in posizioni.items():
        indice = (box - 1) * PER_BOX + n - 1
        if posti[indice] != Path(args.lotto_precedente).joinpath("%s-copia%d.bin" % (chiave, copia)).read_bytes():
            sys.exit("il box %d, posizione %d, non contiene il giro precedente del lotto" % (box, n))
        lotto[indice] = LOTTO.joinpath("%s-copia%d.bin" % (chiave, copia)).read_bytes()

    # 2. gli irregolari: ogni posizione deve contenere la personalita' che il dump riporta
    irregolari = classifica(args.dump)
    conteggio = collections.Counter(c for c, _, _ in irregolari.values())
    for indice, (causa, personalita, specie) in irregolari.items():
        if int.from_bytes(posti[indice][:4], "little") != personalita:
            sys.exit("la posizione %d non contiene piu' il %s del dump: la partita l'ha cambiata" % (indice, specie))

    escluse = {int.from_bytes(r[:4], "little") for r in posti if r != VUOTO}
    escluse |= {int.from_bytes(r[:4], "little") for r in lotto.values()}
    risanati = {}
    rapporto = []
    for indice in sorted(irregolari):
        causa, personalita, specie = irregolari[indice]
        if causa == "noleggio":
            rapporto.append((indice, specie, "cancellato"))
            continue
        mon = gen3.Gen3Mon.from_bytes(posti[indice])
        nome, info = per_id[mon.growth.species]
        if causa == "sfera":
            # La copia ricomposta azzera il checksum memorizzato, che altrimenti resterebbe quello
            # calcolato sulla sfera vecchia e il gioco leggerebbe l'esemplare come Uovo Peste.
            mon = mon.with_personality(mon.personality)
            mon.misc.pokeball = POKE_BALL
            rapporto.append((indice, specie, "sfera: Poke Ball"))
        else:
            natura = gen.NATURE[mon.personality % 25]
            soglia = info.get("soglia_femmina")
            femmina = soglia is not None and (mon.personality & 0xFF) < soglia
            nuova, iv, seme = cerca_cromatico(natura, femmina, soglia, escluse, indice * 2654435761)
            escluse.add(nuova)
            mon = mon.with_personality(nuova)
            mon.ot_id = (SID << 16) | TID
            mon.misc.ivs = {"hp": iv["hp"], "atk": iv["atk"], "def": iv["def"],
                            "spd": iv["spe"], "satk": iv["spa"], "sdef": iv["spd"]}
            mon.misc.ability_num = gen.bit_abilita_di(info["abilita"], nuova)
            rapporto.append((indice, specie, "cromatico: personalita' %08X, seme %08X, IV %s" % (
                nuova, seme, "/".join(str(iv[k]) for k in gen.ORDINE_IV))))
        risanati[indice] = mon.to_bytes()

    # 2b. i cloni del glitch di clonazione: in ogni gruppo di esemplari con la stessa personalita' si
    # tiene il primo, e gli altri diventano incontri distinti e legittimi della stessa specie, con il
    # loro allenatore, la loro natura e il loro sesso. Il proprietario lo ha chiesto il 2026-09-23.
    incontri = incontri_del_dump(args.dump)
    gruppi = collections.defaultdict(list)
    for indice in range(BOX_DEPOSITO * PER_BOX):
        if posti[indice] != VUOTO and indice not in irregolari:
            gruppi[int.from_bytes(posti[indice][:4], "little")].append(indice)
    cloni = {}
    for pid, indici in sorted(gruppi.items()):
        for indice in indici[1:]:
            tipo, cromatico, pid_dump = incontri[indice]
            if pid_dump != pid:
                sys.exit("la posizione %d non contiene piu' il clone del dump" % indice)
            mon = gen3.Gen3Mon.from_bytes(posti[indice])
            nome, info = per_id[mon.growth.species]
            tid, sid = mon.ot_id & 0xFFFF, mon.ot_id >> 16
            if tipo.startswith("Event Gift"):
                esito = evento_diverso(mon, escluse)
                nuova, iv = esito["personalita"], esito["iv"]
                descrizione = "evento 10ANNI, seme %04X" % esito["seme"]
            elif tipo.startswith("Static Encounter") or tipo.startswith("Wild Encounter"):
                natura = gen.NATURE[mon.personality % 25]
                soglia = info.get("soglia_femmina")
                femmina = soglia is not None and (mon.personality & 0xFF) < soglia
                nuova, iv, seme = cerca_cromatico(natura, femmina, soglia, escluse, indice * 40503 + 7,
                                                  tid, sid, cromatico)
                descrizione = "%s, seme del primo metodo %08X" % (tipo.split(" (")[0].split(" Encounter")[0].lower(), seme)
            else:
                sys.exit("clone con un tipo d'incontro non previsto: %s" % tipo)
            escluse.add(nuova)
            mon = mon.with_personality(nuova)
            chiavi = ("hp", "atk", "def", "spd", "satk", "sdef")
            if "spe" in iv:
                mon.misc.ivs = {"hp": iv["hp"], "atk": iv["atk"], "def": iv["def"],
                                "spd": iv["spe"], "satk": iv["spa"], "sdef": iv["spd"]}
            else:
                # `pokebridge.eventi` nomina i valori individuali in italiano
                mon.misc.ivs = {"hp": iv["ps"], "atk": iv["attacco"], "def": iv["difesa"],
                                "spd": iv["velocita"], "satk": iv["attacco_speciale"],
                                "sdef": iv["difesa_speciale"]}
            mon.misc.ability_num = gen.bit_abilita_di(info["abilita"], nuova)
            cloni[indice] = mon.to_bytes()
            rapporto.append((indice, nome, "clone reso distinto: %s, personalita' %08X" % (descrizione, nuova)))
    risanati.update(cloni)

    # 3. il deposito ricompattato: esistenti nei box 1-9 nell'ordine, senza i cancellati
    deposito = []
    for indice in range(BOX_DEPOSITO * PER_BOX):
        if indice in irregolari and irregolari[indice][0] == "noleggio":
            continue
        record = risanati.get(indice, posti[indice])
        if record != VUOTO:
            deposito.append(record)
    for indice in range(BOX_DEPOSITO * PER_BOX, (BOX_DEPOSITO + 2) * PER_BOX):
        if posti[indice] != VUOTO:
            sys.exit("i box 10 e 11 non sono vuoti: la partita li ha usati, e questo strumento non lo prevede")
    previsto = [VUOTO] * save3.POSIZIONI
    for i, r in enumerate(deposito):
        previsto[i] = r
    for indice, r in lotto.items():
        previsto[indice] = r

    nuovo = save3.Save3(grezzo)
    for i, r in enumerate(previsto):
        nuovo.scrivi_posizione(i, r)
    nuovo._scrivi_in_buffer(save3.SEZIONI_STORAGE, save3.OFF_SFONDI, bytes(SFONDI))
    prodotto = nuovo.to_bytes()

    # 4. la verifica, dai byte prodotti
    riletto = save3.Save3(prodotto)
    errori = []
    if not riletto.integro():
        errori.append("slot attivo non integro")
    letti = [riletto.leggi_posizione(i) for i in range(save3.POSIZIONI)]
    if letti != previsto:
        errori.append("le posizioni non sono quelle previste")
    non_toccati = collections.Counter(posti[i] for i in range(BOX_DEPOSITO * PER_BOX)
                                      if posti[i] != VUOTO and i not in irregolari and i not in cloni)
    dopo = collections.Counter(letti[:BOX_DEPOSITO * PER_BOX])
    del dopo[VUOTO]
    for r, n in non_toccati.items():
        if dopo[r] < n:
            errori.append("un esemplare non toccato e' andato perso")
    atteso = sum(non_toccati.values()) + len(risanati)
    if sum(dopo.values()) != atteso:
        errori.append("nei box 1-9 ci sono %d esemplari invece di %d" % (sum(dopo.values()), atteso))
    # Dopo i cloni resi distinti nessuna personalita' deve ripetersi nell'intero deposito.
    tutte = [int.from_bytes(r[:4], "little") for r in letti if r != VUOTO]
    clonate = [pid for pid, n in collections.Counter(tutte).items() if n > 1]
    for indice, record in risanati.items():
        mon = gen3.Gen3Mon.from_bytes(record)
        if mon.to_bytes() != record:
            errori.append("il risanato in %d non e' simmetrico" % indice)
        if indice in irregolari and irregolari[indice][0] == "cromatico":
            iv = {"hp": mon.misc.ivs["hp"], "atk": mon.misc.ivs["atk"], "def": mon.misc.ivs["def"],
                  "spe": mon.misc.ivs["spd"], "spa": mon.misc.ivs["satk"], "spd": mon.misc.ivs["sdef"]}
            pid = mon.personality
            if (pid >> 16) ^ (pid & 0xFFFF) ^ (mon.ot_id & 0xFFFF) ^ (mon.ot_id >> 16) >= 8:
                errori.append("il risanato in %d non e' cromatico" % indice)
            if mon.ot_id >> 16 != SID:
                errori.append("il risanato in %d non ha il segreto vero" % indice)
            if not correlazione_metodo_uno(pid, iv):
                errori.append("il risanato in %d non porta una coppia del primo metodo" % indice)
    if riletto.small() != vecchio.small() or riletto.large() != vecchio.large():
        errori.append("i dati fuori dal deposito sono cambiati")
    base = (1 - vecchio.attivo) * save3.SLOT
    if prodotto[base:base + save3.SLOT] != grezzo[base:base + save3.SLOT]:
        errori.append("lo slot inattivo e' cambiato")
    st = riletto.storage()
    if list(st[save3.OFF_SFONDI:save3.OFF_SFONDI + 14]) != SFONDI:
        errori.append("gli sfondi non sono quelli di ADR-075")
    if st[save3.OFF_NOMI_BOX:save3.OFF_SFONDI] != vecchio.storage()[save3.OFF_NOMI_BOX:save3.OFF_SFONDI]:
        errori.append("i nomi dei box sono cambiati")
    if errori or clonate:
        for e in errori:
            print("VERIFICA FALLITA: %s" % e)
        if clonate:
            print("VERIFICA FALLITA: %d personalita' condivise nel deposito, per esempio %08X" % (len(clonate), clonate[0]))
        sys.exit("il file non e' stato scritto")

    uscita.write_bytes(prodotto)
    for indice, specie, esito in rapporto:
        print("box %2d posizione %2d  %-11s %s" % (indice // PER_BOX + 1, indice % PER_BOX + 1, specie, esito))
    print("irregolari: %s" % dict(conteggio))
    print("cloni resi distinti: %d, e nessuna personalita' condivisa nel deposito" % len(cloni))
    print("deposito: %d esemplari nei box 1-%d, lotto aggiornato nei box 12-14" % (len(deposito), (len(deposito) - 1) // PER_BOX + 1))
    print("sfondi: " + ", ".join("BOX %d %s" % (i + 1, NOMI_SFONDI[s]) for i, s in enumerate(SFONDI)))
    print("scritto %s" % uscita)
    print("SHA-256 %s" % hashlib.sha256(prodotto).hexdigest())


if __name__ == "__main__":
    main()
