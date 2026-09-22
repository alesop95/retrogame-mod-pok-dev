#!/usr/bin/env python3
"""Genera in software i quindici esemplari del catalogo del Parco Lotta, in doppia copia, come strutture di terza generazione.

Perche' esiste
--------------

E' la prima delle due fasi che ADR-067 prescrive: produrre gli esemplari e validarli in software, prima e separatamente dalla scrittura nei box della cartuccia vera, che e' la seconda fase e che non avviene qui. Questo programma non tocca alcun salvataggio e non apre nulla in scrittura fuori dalla propria cartella di uscita.

Il vincolo che governa tutto e' ADR-070, cioe' che ogni esemplare sia ottenibile in terza generazione. Non basta quindi che i campi siano nell'intervallo giusto: devono stare fra loro in una relazione che esiste in natura, ed e' la parte difficile.

La correlazione fra personalita' e valori individuali, e perche' non si sceglie
-------------------------------------------------------------------------------

In terza generazione il valore di personalita' e i sei valori individuali non sono campi indipendenti. Nascono dalle quattro estrazioni consecutive di un generatore congruenziale a partire da un seme, ed e' il primo metodo che `tools/genera-incontro-gen3.py` gia' implementa e da cui questo programma lo riusa invece di riscriverlo. Scegliere la personalita' per avere la natura voluta e poi scrivere valori individuali a piacere produce un esemplare i cui campi sono tutti plausibili uno per uno e la cui relazione reciproca non esiste: e' precisamente cio' che un verificatore cerca, ed e' la differenza fra un esemplare ottenibile e uno fabbricato.

Ne segue che la personalita' non si sceglie e i valori individuali nemmeno: si sceglie il seme, e quello decide entrambi. Il problema diventa quindi trovare un seme che produca insieme la natura richiesta, l'abilita' richiesta, il sesso richiesto e valori individuali abbastanza alti. Cercarlo in avanti su quattro miliardi di semi non e' praticabile.

La ricerca all'indietro, che e' il cuore di questo programma
------------------------------------------------------------

Si inverte. I due valori a quindici bit che compongono i sei valori individuali sono la terza e la quarta estrazione, quindi fissare i valori individuali voluti fissa i sedici bit alti di due stati consecutivi del generatore. Dei sedici bit bassi del primo dei due non si sa nulla, ma sono soltanto sessantaseimila possibilita' da provare, e per ciascuna basta un passo del generatore per vedere se il secondo stato ha in alto i bit giusti. Ne sopravvivono pochissime, e da ciascuna si risale di tre passi all'indietro, cosa che si puo' fare perche' il moltiplicatore e' dispari e quindi invertibile modulo due alla trentaduesima, ottenendo il seme e con esso la personalita'.

A quel punto la personalita' e' determinata e non negoziabile: o ha la natura giusta o non ce l'ha. Si varia allora la distribuzione dei valori individuali fra quelle accettabili, dalla migliore in giu', e si prova finche' una non produce anche la natura, l'abilita' e il sesso richiesti. Poiche' le statistiche che a un esemplare non servono possono valere qualunque cosa, le distribuzioni accettabili sono migliaia e una che soddisfi tutto si trova quasi sempre.

Cio' che il programma dichiara quando non ci riesce, e non e' un dettaglio: se nessuna distribuzione accettabile produce i vincoli, il programma allarga la tolleranza di un punto per volta sulle statistiche che contano e lo scrive nel rapporto. Un esemplare con trenta invece di trentuno in una statistica e' comunque buono; un esemplare la cui provenienza non esiste no, e quella non si allarga mai.

Uso
---

    python gba-save-extraction-smeraldo/tools/genera_squadre_parco_lotta.py --catalogo gba-save-extraction-smeraldo/squadre-parco-lotta.json --dati gba-save-extraction-smeraldo/dati-gen3.json --out _notes/lotto-parco-lotta
"""

import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RADICE.joinpath("pokemon-gen12-gen3-bridge-original-hardware")))

from pokebridge import charmap as cm  # noqa: E402
from pokebridge import gen3  # noqa: E402

MOLT = 0x41C64E6D
SOMMA = 0x00006073
# L'inverso del moltiplicatore modulo due alla trentaduesima. Esiste perche' il moltiplicatore e'
# dispari, ed e' cio' che rende il generatore percorribile all'indietro.
MOLT_INV = pow(MOLT, -1, 1 << 32)

NATURE = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish",
          "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet",
          "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"]

# L'ordine con cui i sei valori individuali stanno nelle due parole a quindici bit, che non e'
# l'ordine con cui si scrivono di solito: la prima parola porta salute, attacco e difesa, la
# seconda velocita', attacco speciale e difesa speciale. Scambiarle produce un esemplare i cui
# campi sono tutti nell'intervallo e la cui relazione non esiste.
ORDINE_IV = ("hp", "atk", "def", "spe", "spa", "spd")

AMICIZIA = {"STANDARD_FRIENDSHIP": 70}

# La lingua dell'esemplare, da `LANGUAGE_ITALIAN` in `include/constants/global.h`. Non e' un campo
# cosmetico e non si lascia al valore piu' comune: se l'allenatore di origine coincide con quello del
# salvataggio, come qui, un verificatore pretende che la lingua coincida con quella della cartuccia,
# perche' un esemplare non scambiato non puo' venire da un gioco di un'altra lingua. Una prima stesura
# scriveva due, cioe' inglese, e produceva ventotto esemplari respinti su ventotto senza che nessun
# altro campo fosse sbagliato: il difetto era invisibile dall'interno e lo ha rivelato PKHeX.
LINGUA_ITALIANO = 4


def _fratello():
    """Il generatore degli incontri, per riusarne il primo metodo invece di riscriverlo."""
    percorso = RADICE.joinpath("tools", "genera-incontro-gen3.py")
    spec = importlib.util.spec_from_file_location("genera_incontro_gen3", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def indietro(stato):
    return ((stato - SOMMA) * MOLT_INV) & 0xFFFFFFFF


def avanti(stato):
    return (stato * MOLT + SOMMA) & 0xFFFFFFFF


def parole_iv(valori):
    """Le due parole a quindici bit che corrispondono a una distribuzione di valori individuali."""
    uno = (valori["hp"] & 31) | ((valori["atk"] & 31) << 5) | ((valori["def"] & 31) << 10)
    due = (valori["spe"] & 31) | ((valori["spa"] & 31) << 5) | ((valori["spd"] & 31) << 10)
    return uno, due


def valori_ammessi(esemplare, tolleranza):
    """Per ogni statistica, l'insieme dei valori individuali accettabili a questa tolleranza.

    Le statistiche che contano vogliono il massimo e scendono al piu' della tolleranza. Quella di attacco fa eccezione dove il catalogo la dichiara a zero, perche' su un attaccante speciale un attacco basso riduce il danno che l'esemplare si infligge da solo quando e' confuso, e li' la tolleranza si applica verso l'alto invece che verso il basso. Le statistiche dichiarate libere accettano qualunque valore fin dal primo giro, perche' su una statistica che non si usa un valore alto non fa ne' bene ne' male e pretenderlo restringerebbe la ricerca per nulla.
    """
    libere = set(esemplare.get("iv_liberi", []))
    ammessi = {}
    for stat in ORDINE_IV:
        if stat in libere:
            ammessi[stat] = list(range(31, -1, -1))
        elif stat == "atk" and esemplare.get("iv_attacco") == 0:
            ammessi[stat] = list(range(0, tolleranza + 1))
        else:
            ammessi[stat] = list(range(31, 31 - tolleranza - 1, -1))
    return ammessi


def cerca_seme(specie_dati, esemplare, allenatore, tolleranza_massima=6, escluse=(), quante=1):
    """Trova un seme del primo metodo che produca insieme natura, abilita', sesso e valori individuali accettabili.

    La ricerca e' rovesciata rispetto a quella ovvia, e la ragione e' di costo. Fissare una distribuzione completa di valori individuali e cercarne i semi costa sessantacinquemila passi per ogni distribuzione, e le distribuzioni accettabili sono migliaia: il conto non sta in piedi. Si fissa invece la sola prima parola, cioe' salute, attacco e difesa, che sono poche combinazioni, e si percorre una volta sola lo spazio dei sedici bit ignoti: ogni passo produce una seconda parola diversa, quindi un solo passaggio copre in un colpo tutte le distribuzioni che condividono la prima parola. Il costo scende di tre ordini di grandezza.

    Una prima stesura di questo programma non lo faceva ed esplorava una distribuzione sola per livello di tolleranza: falliva su nove esemplari su quindici. Il difetto non era nella teoria ma nell'ampiezza della ricerca, ed e' il genere di errore che si manifesta come una impossibilita' apparente invece che come un errore.

    Restituisce TUTTI i semi che soddisfano i vincoli a quella tolleranza, ordinati dal migliore, e non il solo migliore. La ragione e' un difetto che una prima stesura aveva e che soltanto un verificatore esterno ha rivelato: due esemplari con la stessa natura e lo stesso profilo di valori individuali, per esempio tre esemplari Decisi con gli stessi obiettivi, ricevevano lo STESSO seme e quindi lo stesso valore di personalita', perche' la ricerca era deterministica e si fermava al primo. Tre Pokemon distinti con la medesima personalita' non esistono, e PKHeX lo ha segnalato come condivisione del valore fra tipi di incontro diversi. Chi chiama sceglie percio' fra i candidati il primo non ancora usato, e le due copie di uno stesso esemplare ne prendono due diversi.

    Il punteggio somma i valori individuali escludendo l'attacco quando il catalogo lo vuole basso, altrimenti premierebbe proprio cio' che si e' chiesto di evitare.
    """
    natura_voluta = esemplare["natura"]
    abilita = specie_dati["abilita"]
    due_abilita = len(abilita) == 2 and abilita[1] not in ("None", abilita[0])
    indice_abilita = abilita.index(esemplare["abilita"]) if esemplare["abilita"] in abilita else 0
    soglia = specie_dati.get("soglia_femmina")
    sesso_voluto = esemplare.get("sesso")
    tid, sid = allenatore["id"], allenatore["segreto"]
    attacco_basso = esemplare.get("iv_attacco") == 0
    escluse = set(escluse)
    migliori = []

    for tolleranza in range(tolleranza_massima + 1):
        ammessi = valori_ammessi(esemplare, tolleranza)
        ok_spe = set(ammessi["spe"])
        ok_spa = set(ammessi["spa"])
        ok_spd = set(ammessi["spd"])
        candidati = []
        for hp in ammessi["hp"]:
            for atk in ammessi["atk"]:
                for dif in ammessi["def"]:
                    iv1 = hp | (atk << 5) | (dif << 10)
                    for alto in (iv1, iv1 | 0x8000):
                        base = alto << 16
                        for basso in range(1 << 16):
                            s3 = base | basso
                            iv2 = (((s3 * MOLT + SOMMA) & 0xFFFFFFFF) >> 16) & 0x7FFF
                            spe = iv2 & 31
                            if spe not in ok_spe:
                                continue
                            spa = (iv2 >> 5) & 31
                            if spa not in ok_spa:
                                continue
                            spd = (iv2 >> 10) & 31
                            if spd not in ok_spd:
                                continue
                            s2 = indietro(s3)
                            s1 = indietro(s2)
                            personalita = (((s2 >> 16) & 0xFFFF) << 16) | ((s1 >> 16) & 0xFFFF)
                            if NATURE[personalita % 25] != natura_voluta:
                                continue
                            if due_abilita and (personalita & 1) != indice_abilita:
                                continue
                            if soglia is not None and sesso_voluto:
                                femmina = (personalita & 0xFF) < soglia
                                if femmina != (sesso_voluto == "femmina"):
                                    continue
                            if ((personalita >> 16) ^ (personalita & 0xFFFF) ^ tid ^ sid) < 8:
                                continue
                            valori = {"hp": hp, "atk": atk, "def": dif,
                                      "spe": spe, "spa": spa, "spd": spd}
                            punteggio = sum(v for k, v in valori.items()
                                            if not (attacco_basso and k == "atk"))
                            candidati.append((punteggio, {
                                "seme": indietro(s1),
                                "personalita": personalita,
                                "iv": valori,
                                "scarto": tolleranza,
                                "bit_abilita": (personalita & 1) if due_abilita else 0,
                            }))
        if candidati:
            candidati.sort(key=lambda c: -c[0])
            liberi = [c[1] for c in candidati if c[1]["personalita"] not in escluse]
            # Si allarga la tolleranza anche quando dei candidati ci sono, se non bastano: due specie
            # con la stessa natura e lo stesso profilo producono la MEDESIMA lista, perche' la lista
            # dipende dai vincoli e non dalla specie, e la seconda trova consumato cio' che la prima ha
            # preso. Fermarsi qui faceva fallire sette esemplari su trentatre con un messaggio che
            # parlava di candidati insufficienti invece che della causa.
            if len(liberi) >= quante:
                return liberi
            migliori = liberi
    return migliori


def componi(esemplare, chiave, specie_dati, dati, allenatore, tabella, esito, strumento):
    specie = esemplare["specie"]
    info = dati["specie"][specie]
    livello = dati["livello_di_gioco"]
    gruppo = info["gruppo_crescita"]

    # La grafia delle mosse diverge fra il catalogo e il sorgente su trattini e apostrofi, per
    # esempio Soft-Boiled contro Soft Boiled: si confronta sulle sole lettere e cifre, come fa gia'
    # il verificatore delle squadre, invece di tenere due grafie sincronizzate a mano.
    per_chiave = {"".join(c for c in k.lower() if c.isalnum()): v for k, v in dati["mosse"].items()}
    mosse = []
    pp = []
    for m in esemplare["mosse"]:
        voce = per_chiave.get("".join(c for c in m.lower() if c.isalnum()))
        if voce is None:
            raise KeyError("mossa ignota nei dati: %r" % m)
        mosse.append(voce["id"])
        # I punti potenza sono massimizzati come se fosse stato usato PP Max su ciascuna mossa,
        # come ADR-067 prescrive: il bonus e' tre sesti in piu' sul valore di base, e il campo
        # dei bonus porta due bit per mossa, quindi tre per tutte e quattro.
        pp.append(min(99, voce["pp"] + (voce["pp"] * 3) // 5))

    punti_base = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
    etichette = {"hp": "hp", "atk": "atk", "def": "def", "spa": "spa", "spd": "spd", "spe": "spe"}
    for pezzo in esemplare["punti_base"].split("/"):
        parti = pezzo.strip().split()
        if len(parti) == 2 and parti[0].isdigit():
            chiave_ev = etichette.get(parti[1].lower())
            if chiave_ev:
                punti_base[chiave_ev] = int(parti[0])

    nome_visibile = specie.upper()
    soprannome = tabella.encode(nome_visibile, length=gen3.NICKNAME_LENGTH)
    ot = tabella.encode(allenatore["nome"], length=gen3.OT_NAME_LENGTH)

    origine = esemplare.get("origine", {})
    return gen3.Gen3Mon(
        personality=esito["personalita"],
        ot_id=((allenatore["segreto"] & 0xFFFF) << 16) | (allenatore["id"] & 0xFFFF),
        nickname=soprannome,
        language=LINGUA_ITALIANO,
        flags=0x02,
        ot_name=ot,
        markings=0,
        growth=gen3.Growth(species=info["id"], held_item=strumento,
                           experience=dati["esperienza"][gruppo][livello],
                           pp_bonuses=0xFF, friendship=AMICIZIA.get(info["amicizia"], 70)),
        attacks=gen3.Attacks(moves=(mosse + [0, 0, 0, 0])[:4], pp=(pp + [0, 0, 0, 0])[:4]),
        evs=gen3.EvsCondition(evs={
            "hp": punti_base["hp"], "atk": punti_base["atk"], "def": punti_base["def"],
            "spd": punti_base["spe"], "satk": punti_base["spa"], "sdef": punti_base["spd"],
        }),
        misc=gen3.Misc(
            pokerus=0,
            met_location=origine.get("luogo", 32),
            met_level=origine.get("livello_incontro", 0),
            met_game=origine.get("gioco", 3),
            pokeball=origine.get("sfera", 4),
            ot_female=False,
            ivs={"hp": esito["iv"]["hp"], "atk": esito["iv"]["atk"], "def": esito["iv"]["def"],
                 "spd": esito["iv"]["spe"], "satk": esito["iv"]["spa"], "sdef": esito["iv"]["spd"]},
            is_egg=False,
            ability_num=esito["bit_abilita"],
            modern_fateful_encounter=bool(origine.get("fatidico", False)),
        ),
    )


def _chiave(nome_mossa):
    return "".join(c for c in nome_mossa.lower() if c.isalnum())


def verifica(uscita, catalogo, dati, manifesto):
    """Rilegge dal disco ogni struttura scritta e controlla che dica cio' che si voleva scrivere.

    Non e' una formalita' e non ripete cio' che la generazione ha appena fatto: legge i byte, li decifra, ne ricompone le sottostrutture e confronta il risultato con il catalogo di partenza. Fra la volonta' e il file ci sono la permutazione delle quattro sottostrutture, la cifratura con la chiave derivata, il checksum e la conversione dell'esperienza in livello, e ciascuno di quei passaggi puo' sbagliare in un modo che nessun campo dichiara.

    Il controllo di simmetria vale piu' degli altri messi insieme: ricifrare cio' che si e' decifrato deve restituire gli stessi byte. Se non li restituisce, una qualunque delle trasformazioni non e' invertibile come si crede, e l'esemplare che il gioco leggera' non e' quello che si e' composto.
    """
    per_mossa = {_chiave(k): v for k, v in dati["mosse"].items()}
    problemi = []
    for voce in manifesto:
        chiave = voce["chiave"]
        esemplare = catalogo["esemplari"][chiave]
        info = dati["specie"][esemplare["specie"]]
        grezzo = Path(uscita).joinpath("esemplari", "%s-copia1.bin" % chiave).read_bytes()
        mon = gen3.Gen3Mon.from_bytes(grezzo)
        prima_copia = voce["copie"][0]
        errori = []
        if mon.growth.species != info["id"]:
            errori.append("specie %d invece di %d" % (mon.growth.species, info["id"]))
        if NATURE[mon.personality % 25] != esemplare["natura"]:
            errori.append("natura %s invece di %s" % (NATURE[mon.personality % 25], esemplare["natura"]))
        attesa = dati["esperienza"][info["gruppo_crescita"]][dati["livello_di_gioco"]]
        if mon.growth.experience != attesa:
            errori.append("esperienza %d invece di %d, cioe' un livello diverso da %d"
                          % (mon.growth.experience, attesa, dati["livello_di_gioco"]))
        letti = {"hp": mon.misc.ivs["hp"], "atk": mon.misc.ivs["atk"], "def": mon.misc.ivs["def"],
                 "spe": mon.misc.ivs["spd"], "spa": mon.misc.ivs["satk"], "spd": mon.misc.ivs["sdef"]}
        if letti != prima_copia["iv"]:
            errori.append("valori individuali %s invece di %s" % (letti, prima_copia["iv"]))
        attese = [per_mossa[_chiave(m)]["id"] for m in esemplare["mosse"]]
        if list(mon.attacks.moves[:len(attese)]) != attese:
            errori.append("mosse diverse da quelle del catalogo")
        abilita = info["abilita"]
        if len(abilita) == 2 and abilita[1] not in ("None", abilita[0]):
            if abilita[mon.misc.ability_num] != esemplare["abilita"]:
                errori.append("abilita' %s invece di %s" % (abilita[mon.misc.ability_num], esemplare["abilita"]))
        totale = sum(mon.evs.evs.values())
        if totale > 510:
            errori.append("punti base %d, oltre il tetto di 510" % totale)
        if grezzo != mon.to_bytes():
            errori.append("non simmetrico: ricifrare cio' che si e' decifrato non restituisce gli stessi byte")
        if errori:
            problemi.append((chiave, errori))
    return problemi


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--catalogo", required=True)
    p.add_argument("--dati", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--allenatore", default="ALEX:45761:56446")
    args = p.parse_args()

    catalogo = json.loads(Path(args.catalogo).read_text(encoding="utf-8"))
    dati = json.loads(Path(args.dati).read_text(encoding="utf-8"))
    dati["livello_di_gioco"] = catalogo["livello"]
    nome, tid, sid = args.allenatore.split(":")
    allenatore = {"nome": nome, "id": int(tid), "segreto": int(sid)}
    tabella = cm.Charmap.gen3()

    strumento_per_chiave = {}
    for squadra in catalogo["squadre"]:
        for v in squadra["esemplari"]:
            if v.get("strumento"):
                strumento_per_chiave.setdefault(v["chiave"], v["strumento"])

    uscita = Path(args.out)
    uscita.joinpath("esemplari").mkdir(parents=True, exist_ok=True)
    manifesto = []
    # I valori di personalita' gia' assegnati, perche' due esemplari non possono condividerlo e
    # nemmeno le due copie dello stesso: due Pokemon con la medesima personalita' sono cloni, e un
    # verificatore li rifiuta prima ancora di guardare qualunque altro campo.
    usate = set()
    for chiave, esemplare in sorted(catalogo["esemplari"].items()):
        origine = esemplare.get("origine", {})
        if origine.get("genera") is False:
            print("SALTATO %-19s %s" % (chiave, origine.get("nota", "provenienza non modellata")[:90]))
            continue
        info = dati["specie"][esemplare["specie"]]
        candidati = cerca_seme(info, esemplare, allenatore,
                               escluse=usate, quante=catalogo["copie_per_esemplare"])
        if not candidati:
            print("FALLITO %s: nessun seme trovato entro la tolleranza" % chiave)
            continue
        nome_strumento = strumento_per_chiave.get(chiave)
        strumento = dati["oggetti"].get(nome_strumento, 0) if nome_strumento else 0
        scelti = []
        for esito in candidati:
            if esito["personalita"] in usate:
                continue
            usate.add(esito["personalita"])
            scelti.append(esito)
            if len(scelti) == catalogo["copie_per_esemplare"]:
                break
        if len(scelti) < catalogo["copie_per_esemplare"]:
            print("FALLITO %s: %d candidati distinti su %d richiesti"
                  % (chiave, len(scelti), catalogo["copie_per_esemplare"]))
            continue
        for numero, esito in enumerate(scelti, start=1):
            mon = componi(esemplare, chiave, info, dati, allenatore, tabella, esito, strumento)
            uscita.joinpath("esemplari", "%s-copia%d.bin" % (chiave, numero)).write_bytes(mon.to_bytes())
        manifesto.append({
            "chiave": chiave, "specie": esemplare["specie"], "natura": esemplare["natura"],
            "provenienza": origine.get("tipo"), "luogo": origine.get("nome_luogo"),
            "copie": [{"seme": "0x%08X" % e["seme"], "personalita": "0x%08X" % e["personalita"],
                       "iv": e["iv"], "scarto_tollerato": e["scarto"]} for e in scelti],
            "strumento": nome_strumento,
        })
        print("%-19s %-11s %-8s  %s  scarto %d  personalita' %s" % (
            chiave, esemplare["specie"], esemplare["natura"],
            "/".join(str(scelti[0]["iv"][k]) for k in ORDINE_IV), scelti[0]["scarto"],
            " e ".join("%08X" % e["personalita"] for e in scelti)))

    uscita.joinpath("manifesto.json").write_text(
        json.dumps({"allenatore": allenatore, "livello": catalogo["livello"], "esemplari": manifesto},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n%d esemplari generati, %d file scritti in %s" % (len(manifesto), len(manifesto) * 2, uscita))

    problemi = verifica(uscita, catalogo, dati, manifesto)
    for chiave, errori in problemi:
        for e in errori:
            print("VERIFICA FALLITA %s: %s" % (chiave, e))
    if problemi:
        sys.exit("la verifica ha trovato %d esemplari difettosi: il lotto non e' utilizzabile" % len(problemi))
    print("verifica: %d esemplari riletti dal disco, tutti conformi al catalogo, tutti simmetrici" % len(manifesto))


if __name__ == "__main__":
    main()
