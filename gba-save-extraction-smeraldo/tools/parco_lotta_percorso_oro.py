#!/usr/bin/env python3
"""Aggiorna le parti generate della guida al Parco Lotta: calendario, squadre posizione per posizione, misura delle riserve, schede e disposizione nei box.

Perche' esiste
--------------

Il catalogo dice quali squadre portare e STUDIO-04 dice quante lotte servono, ma chi gioca ha davanti il PC del gioco e non un file: gli serve sapere che per la Torre Lotta il Latios da prendere e' quello del box 14 in prima riga e prima colonna, con quale strumento, in quale ordine di squadra, e a quale lotta arrivera' l'Asso. La guida `GUIDA-PARCO-LOTTA.md` e' un solo documento, per scelta del proprietario del 2026-09-23 che ha fuso in esso tre file separati: la prosa vi e' scritta a mano, e le tabelle che discendono dal catalogo vi stanno fra coppie di marcatori che questo strumento riscrive. Le tabelle si generano con codice perche' la disposizione nei box discende da una regola, e una regola applicata a mano a sessantaquattro posizioni sbaglia; stanno dentro la guida perche' chi gioca deve trovare tutto in un posto solo.

La disposizione, che e' ADR-078
-------------------------------

Dal 2026-09-23 il lotto e' in copia unica, trentadue esemplari, e chiude il deposito: l'ultimo sta nell'ultima posizione del box 14, e i due che non entrano nel box 14 occupano le ultime due posizioni del box 13. Le copie 2 per lo scambio sono uscite dal deposito per ADR-077 e restano soltanto come file. La disposizione di ADR-074, in due copie affiancate nei box 12, 13 e 14, resta disponibile con `storica=True` perche' e' quella dei giri scritti fino al settimo. Prima gli otto titolari, nell'ordine in cui compaiono per la prima volta nelle squadre del catalogo; poi le ventiquattro riserve, in ordine di frequenza nelle squadre dei thread come la misura della sezione 10 della guida, cosi' che le riserve piu' probabili stiano piu' vicine ai titolari e le due meno usate finiscano nel box 13. La funzione `disposizione` e' la sola fonte di questa regola: lo strumento di riordino del deposito la importa invece di riscriverla, perche' due copie della stessa regola possono divergere.

Il box ha trenta posizioni in cinque righe da sei. La posizione si scrive come box, riga e colonna, contando dall'alto a sinistra, perche' e' cosi' che la si trova sullo schermo.

Che cosa non e' ancora vero
---------------------------

La disposizione di ADR-078 e' quella del file di `giro11`, prodotto da `emerald_cartuccia_completa.py` che importa `disposizione` da qui; finche' quel file non e' scritto sulla cartuccia, sulla cartuccia c'e' ancora la disposizione storica del settimo giro. Resta non verificato in partita l'effetto delle squadre, che e' materia della guida e non dello strumento.

Uso
---

    python gba-save-extraction-smeraldo/tools/parco_lotta_percorso_oro.py
    python gba-save-extraction-smeraldo/tools/parco_lotta_percorso_oro.py --check

La prima forma aggiorna le tabelle della guida e rigenera ogni volta le figure, con `parco_lotta_figure.py`, e la copia `GUIDA-PARCO-LOTTA.docx`, con `tools/md-to-docx.py`. La seconda non scrive nulla e controlla soltanto le tabelle.
"""

import argparse
import csv
import importlib.util
import json
import os
import re
import sys
from pathlib import Path

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
CATALOGO = CARTELLA.joinpath("squadre-parco-lotta.json")
GLOSSARIO = CARTELLA.joinpath("GLOSSARIO-MOSSE.md")
GUIDA = CARTELLA.joinpath("GUIDA-PARCO-LOTTA.md")
LOTTO = RADICE.joinpath("_notes", "lotto-parco-lotta")
# Dal 2026-09-23 il dump e' quello del deposito intero, `round 4`, che contiene l'ottavo giro del lotto
# in copia unica; si accoppia al manifesto corrente per personalita'.
_DUMP_TROVATI = sorted(RADICE.joinpath("_notes").glob("backup salvataggi pok* cartucce vere/smeraldo/dump-pkhex/Box Data Dump smeraldo vero ALEX-45761 - round 6.csv"))
DUMP = Path(os.environ["SMERALDO_DUMP_CSV"]) if "SMERALDO_DUMP_CSV" in os.environ else (
    _DUMP_TROVATI[0] if len(_DUMP_TROVATI) == 1 else RADICE.joinpath("_notes", "ARCHIVIO_PRIVATO_NON_TROVATO"))
# Il manifesto del giro a cui il dump appartiene, e non quello corrente: il dump si accoppia al lotto
# per personalita', e la personalita' degli esemplari statici cambia a ogni rigenerazione. I nomi
# italiani, l'esperienza e i luoghi non cambiano fra un giro e l'altro, quindi il dump del sesto giro
# resta valido per la guida finche' non ne arriva uno nuovo, purche' lo si legga con il suo manifesto.
MANIFESTO_DUMP = LOTTO.joinpath("manifesto.json")

BOX_DEL_LOTTO = (12, 13, 14)
POSIZIONI = 30
# ADR-078: il lotto in copia unica chiude il deposito, e l'ultimo esemplare sta nell'ultima posizione
# del box 14. I primi trenta dell'ordine riempiono il box 14, gli altri risalgono in coda al box 13.
BOX_FINALE = 14
COLONNE = 6

# Il calendario degli Assi, da `sFrontierBrainStreakAppearances` in `src/frontier_util.c`, come
# registrato e spiegato in STUDIO-04 sezione 5: unita' contata, soglia d'argento, soglia d'oro, e
# ampiezza di una serie in quell'unita'. Dove l'Asso cade lo dice la funzione `dove_cade`.
CALENDARIO = {
    "Cupola Lotta": ("tornei", 4, 9, 1, "Astro Cupola Tolomeo", "Tattica", 0),
    "Azienda Lotta": ("lotte", 21, 42, 7, "Boss Azienda Savino", "Sapienza", 1),
    "Torre Lotta": ("lotte", 35, 70, 7, "Dama Torre Alberta", "Abilita'", 1),
    "Dojo Lotta": ("lotte", 28, 56, 7, "Maestra Dojo Valentina", "Valore", 1),
    "Palazzo Lotta": ("lotte", 21, 42, 7, "Sire Palazzo Spartaco", "Spirito", 1),
    "Serpe Lotta": ("sale", 28, 140, 14, "Regina Serpe Fortunata", "Fortuna", 1),
    "Piramide Lotta": ("piani", 21, 70, 7, "Re Piramide Baldo", "Audacia", 0),
}

def _mappa():
    percorso = Path(__file__).resolve().parent.joinpath("parco_lotta_mappa_riserve.py")
    spec = importlib.util.spec_from_file_location("mappa_riserve", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def disposizione(catalogo, thread, storica=False):
    """Restituisce l'elenco ordinato delle chiavi del lotto e la posizione di ciascuna copia: {(chiave, copia): (box, posizione)}.

    Senza argomenti e' la disposizione di ADR-078, in copia unica: i primi trenta esemplari dell'ordine
    occupano il box 14 dalla prima all'ultima posizione, cosi' che i titolari stiano tutti in un box
    solo, e i restanti, cioe' le riserve meno usate, occupano le ultime posizioni del box 13. Con
    `storica=True` e' la disposizione di ADR-074 in due copie dal box 12, che e' quella dei giri
    scritti fino al settimo e che gli strumenti di lavoro sul salvataggio verificano in ingresso.
    """
    generati, titolari, per_specie, righe, _ = _mappa().misura(catalogo, thread)
    ordine = []
    for squadra in catalogo["squadre"]:
        for v in squadra["esemplari"]:
            if v["chiave"] in titolari and v["chiave"] not in ordine:
                ordine.append(v["chiave"])
    riserve = [k for k in generati if k not in titolari]
    riserve.sort(key=lambda k: (-sum(righe[generati[k]["specie"]]["edifici"].values()), k))
    ordine += riserve
    posizioni = {}
    if not storica:
        for i, chiave in enumerate(ordine):
            if i < POSIZIONI:
                posizioni[(chiave, 1)] = (BOX_FINALE, i + 1)
            else:
                posizioni[(chiave, 1)] = (BOX_FINALE - 1, POSIZIONI - (len(ordine) - POSIZIONI) + (i - POSIZIONI) + 1)
        return ordine, posizioni, generati, titolari
    copie = catalogo["copie_per_esemplare"]
    indice = 0
    for chiave in ordine:
        for copia in range(1, copie + 1):
            box = BOX_DEL_LOTTO[indice // POSIZIONI]
            posizioni[(chiave, copia)] = (box, indice % POSIZIONI + 1)
            indice += 1
    return ordine, posizioni, generati, titolari


SIGLE_PUNTI_BASE = {"HP": "PS", "Atk": "Att", "Def": "Dif", "SpA": "AttSp", "SpD": "DifSp", "Spe": "Vel"}


def punti_base_it(testo):
    return " / ".join(" ".join([p.split()[0], SIGLE_PUNTI_BASE.get(p.split()[1], p.split()[1])]) for p in testo.split(" / "))


def dove(posizione):
    box, n = posizione
    return "box %d, riga %d, colonna %d" % (box, (n - 1) // COLONNE + 1, (n - 1) % COLONNE + 1)


def glossario():
    nomi = {}
    for riga in GLOSSARIO.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| ([^|]+?) \| ([^|]+?) \|$", riga)
        if m and m.group(1) not in ("Nome nel catalogo", "---"):
            nomi[m.group(1)] = m.group(2)
    return nomi


def nature_italiane():
    """Il nome italiano di ciascuna natura, letto dal dump di PKHeX del settimo giro come per gli strumenti."""
    manifesto = json.loads(MANIFESTO_DUMP.read_text(encoding="utf-8"))
    per_pid = {}
    with DUMP.open(encoding="utf-8-sig") as f:
        for riga in csv.DictReader(f):
            per_pid[riga["PID"].upper()] = riga["Nature"]
    return {voce["natura"]: per_pid[voce["copie"][0]["personalita"][2:].upper()]
            for voce in manifesto["esemplari"] if voce["copie"][0]["personalita"][2:].upper() in per_pid}


def righe_dump():
    """Le righe del dump di PKHeX del sesto giro, per personalita' della copia 1 di ciascun esemplare del manifesto."""
    manifesto = json.loads(MANIFESTO_DUMP.read_text(encoding="utf-8"))
    per_pid = {}
    with DUMP.open(encoding="utf-8-sig") as f:
        for riga in csv.DictReader(f):
            per_pid[riga["PID"].upper()] = riga
    return {voce["chiave"]: per_pid.get(voce["copie"][0]["personalita"][2:].upper()) for voce in manifesto["esemplari"]}


def strumenti_italiani():
    """Il nome italiano di ciascuno strumento, letto dove il gioco lo scrive e non tradotto: dal dump di PKHeX del settimo giro, accoppiato alla personalita' registrata nel manifesto."""
    manifesto = json.loads(MANIFESTO_DUMP.read_text(encoding="utf-8"))
    per_pid = {}
    with DUMP.open(encoding="utf-8-sig") as f:
        for riga in csv.DictReader(f):
            per_pid[riga["PID"].upper()] = riga["HeldItem"]
    nomi = {}
    for voce in manifesto["esemplari"]:
        if voce.get("strumento"):
            pid = voce["copie"][0]["personalita"][2:].upper()
            if pid in per_pid:
                nomi[voce["strumento"]] = per_pid[pid]
    return nomi


def dove_cade(edificio, soglia):
    """In quale serie e a quale incontro cade l'Asso, applicando lo scarto come STUDIO-04 sezione 5 lo spiega."""
    unita, _, _, per_serie, _, _, scarto = CALENDARIO[edificio]
    if edificio == "Cupola Lotta":
        return "finale del torneo %d" % (soglia + 1)
    numero = soglia if scarto == 1 else soglia + 1
    serie = (numero - 1) // per_serie + 1
    posto = (numero - 1) % per_serie + 1
    parola, articolo = {"lotte": ("lotta", "alla"), "sale": ("sala", "alla"), "piani": ("piano", "al")}[unita]
    return "%s %s %d, cioe' serie %d, %s %d di %d" % (articolo, parola, numero, serie, parola, posto, per_serie)


def blocchi(catalogo, thread):
    """I blocchi generati della guida, per nome: il calendario, una squadra per edificio, la misura delle riserve, le schede e la disposizione."""
    ordine, posizioni, generati, titolari = disposizione(catalogo, thread)
    mosse_it = glossario()
    # Il glossario e' generato su un giro vecchio del catalogo, quindi una mossa entrata dopo non vi
    # compare. Il dump del sesto giro porta le mosse di ogni esemplare nell'ordine del catalogo, e
    # l'accoppiamento per posizione le completa senza tradurre nulla.
    for chiave, riga in righe_dump().items():
        if riga:
            for inglese, italiano in zip(catalogo["esemplari"][chiave]["mosse"],
                                         [riga["Move%d" % i] for i in range(1, 5)]):
                mosse_it.setdefault(inglese, italiano)
    strum_it = strumenti_italiani()
    nat_it = nature_italiane()
    mappa = _mappa()
    sostituzioni = mappa.misura(catalogo, thread)[4]
    manifesto = json.loads(LOTTO.joinpath("manifesto.json").read_text(encoding="utf-8"))
    nel_file = {v["chiave"]: v.get("strumento") for v in manifesto["esemplari"]}
    fuori = {}

    righe = ["| Edificio | Asso | Argento | Oro | Serie di fila per l'oro |", "|---|---|---|---|---|"]
    for squadra in sorted(catalogo["squadre"], key=lambda s: int(s["ordine"])):
        edificio = squadra["edificio"]
        unita, argento, oro, per_serie, asso, simbolo, scarto = CALENDARIO[edificio]
        if edificio == "Cupola Lotta":
            serie = "10 tornei da 4 incontri"
        else:
            serie = "%d serie da %d %s" % (-(-(oro if scarto == 1 else oro + 1) // per_serie), per_serie, unita)
        righe.append("| %s | %s | %s | %s | %s |" % (edificio, asso, dove_cade(edificio, argento), dove_cade(edificio, oro), serie))
    fuori["calendario"] = "\n".join(righe)

    for squadra in catalogo["squadre"]:
        edificio = squadra["edificio"]
        if not squadra["esemplari"]:
            continue
        out = ["| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |", "|---|---|---|---|---|"]
        for n, v in enumerate(squadra["esemplari"], start=1):
            e = generati[v["chiave"]]
            mosse = list(e["mosse"])
            for vecchia, nuova in (v.get("mosse_sostituite") or {}).items():
                mosse = [nuova if m == vecchia else m for m in mosse]
            mosse_testo = ", ".join(mosse_it.get(m, m) for m in mosse)
            if v.get("mosse_sostituite"):
                mosse_testo += " (cambiata per la Piramide: %s)" % ", ".join(
                    "%s al posto di %s" % (mosse_it.get(b, b), mosse_it.get(a, a)) for a, b in v["mosse_sostituite"].items())
            strumento = v.get("strumento")
            strumento_testo = strum_it.get(strumento, strumento) if strumento else "nessuno"
            # Il file porta lo strumento della PRIMA squadra in cui l'esemplare compare, perche' un
            # esemplare ne tiene uno solo: dove l'edificio ne vuole un altro, lo scambio si fa in gioco.
            gia = nel_file.get(v["chiave"])
            if gia != strumento:
                strumento_testo += " (il file porta %s: %s)" % (
                    strum_it.get(gia, gia) if gia else "nessuno strumento",
                    "toglierlo" if not strumento else "scambiarlo in gioco")
            out.append("| %d | %s %s | %s | %s | %s |" % (n, e["specie"], nat_it.get(e["natura"], e["natura"]), dove(posizioni[(v["chiave"], 1)]), strumento_testo, mosse_testo))
        if squadra.get("ordine_per_giro"):
            out.append("")
            out.append("Chi conduce, serie per serie. Le prime dieci serie bastano all'oro e vengono dalla guida al completamento; la colonna del calcolo e' il controllo di `parco_lotta_piramide_ordine.py`, che concorda con la guida in sette casi su dieci sul membro impiegato.")
            out.append("")
            out.append("| Serie | Piani | Tema del giro | Primo in campo | Cambio | Calcolo |")
            out.append("|---|---|---|---|---|---|")
            for g in squadra["ordine_per_giro"][:10]:
                a = (g["giro"] - 1) * 7 + 1
                out.append("| %d | %d-%d | %s | %s | %s | %s |" % (g["giro"], a, a + 6, g["tema"], g["primo"], g["cambio"] or "nessuno", g["calcolato"]))
        candidati = [(u, c) for e_, u, _, c in sostituzioni if e_ == edificio]
        if candidati:
            testo = "; ".join("al posto di %s, %s" % (generati[u]["specie"], ", ".join(
                "%s (%s)" % (sp, dove(posizioni[(next(k for k in ordine if generati[k]["specie"] == sp), 1)])) for _, _, _, sp in c[:2]))
                for u, c in candidati)
            out.append("")
            out.append("Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 10 e quindi non ancora una scelta: %s." % testo)
        fuori["squadra " + edificio] = "\n".join(out)

    # La misura delle riserve, cioe' le due tabelle dello strumento gemello senza la sua testata: i
    # titoli scendono di un livello perche' qui sono sottosezioni della sezione 10 della guida.
    misura = mappa.scrivi(*mappa.misura(catalogo, thread), thread).split("\n")
    inizio = next(i for i, r in enumerate(misura) if r.startswith("Squadre per edificio nel campione"))
    fuori["misura delle riserve"] = "\n".join("#" + r if r.startswith("## ") else r for r in misura[inizio:]).rstrip()

    out = ["| Posizione | Esemplare | Abilita' | Punti base | Mosse | Strumento nel file | Incontro | Margine al 51 |",
           "|---|---|---|---|---|---|---|---|"]
    dump = righe_dump()
    dati = json.loads(CARTELLA.joinpath("dati-gen3.json").read_text(encoding="utf-8"))
    for chiave in ordine:
        e = generati[chiave]
        riga = dump.get(chiave) or {}
        gruppo = dati["specie"][e["specie"]]["gruppo_crescita"]
        soglia = dati["esperienza"][gruppo][catalogo["livello"] + 1]
        margine = soglia - int(riga.get("EXP", 0) or 0) if riga else None
        incontro = "%s, %s, livello %s" % (riga.get("MetLoc", "?"), riga.get("Version", "?"),
                                          riga.get("MetLevel", "?") if riga.get("MetLevel") not in ("0", None) else "uovo")
        gia = nel_file.get(chiave)
        out.append("| %s | %s %s | %s | %s | %s | %s | %s | %s |" % (
            dove(posizioni[(chiave, 1)]), e["specie"], nat_it.get(e["natura"], e["natura"]), riga.get("Ability", e["abilita"]),
            punti_base_it(e["punti_base"]), ", ".join(mosse_it.get(m, m) for m in e["mosse"]),
            strum_it.get(gia, gia) if gia else "nessuno", incontro,
            ("%d, ATTENZIONE" % margine if margine == 1 else "%d" % margine) if margine is not None else "?"))
    fuori["schede"] = "\n".join(out)

    out = ["| Box | Riga | Colonna | Esemplare | Ruolo |", "|---|---|---|---|---|"]
    for (chiave, copia), (box, n) in sorted(posizioni.items(), key=lambda x: x[1]):
        e = generati[chiave]
        out.append("| %d | %d | %d | %s %s | %s |" % (box, (n - 1) // COLONNE + 1, (n - 1) % COLONNE + 1, e["specie"], nat_it.get(e["natura"], e["natura"]), "titolare" if chiave in titolari else "riserva"))
    fuori["disposizione"] = "\n".join(out)
    return fuori


def marcatori(nome):
    return ("<!-- generato da parco_lotta_percorso_oro.py: %s, inizio -->" % nome,
            "<!-- generato da parco_lotta_percorso_oro.py: %s, fine -->" % nome)


def inserisci(testo, generati):
    """Sostituisce il contenuto fra i marcatori di ciascun blocco; un marcatore mancante o doppio ferma tutto, perche' scrivere a meta' una guida e' peggio che non scriverla."""
    for nome, blocco in generati.items():
        apri, chiudi = marcatori(nome)
        if testo.count(apri) != 1 or testo.count(chiudi) != 1:
            raise SystemExit("la guida non ha una e una sola coppia di marcatori per il blocco %r" % nome)
        a = testo.index(apri) + len(apri)
        b = testo.index(chiudi)
        testo = testo[:a] + "\n\n" + blocco + "\n\n" + testo[b:]
    return testo


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--guida", default=str(GUIDA))
    p.add_argument("--check", action="store_true", help="non scrive: esce con codice 1 se la guida non e' aggiornata")
    args = p.parse_args()
    catalogo = json.loads(CATALOGO.read_text(encoding="utf-8"))
    thread = json.loads(_mappa().THREAD.read_text(encoding="utf-8"))
    guida = Path(args.guida)
    prima = guida.read_bytes().decode("utf-8")
    dopo = inserisci(prima, blocchi(catalogo, thread))
    if args.check:
        if dopo != prima:
            sys.exit("la guida non e' aggiornata: rilancia senza --check")
        print("la guida e' aggiornata")
        return
    if dopo != prima:
        guida.write_bytes(dopo.encode("utf-8"))
        print("aggiornata %s" % guida)
    else:
        print("nessun cambiamento in %s" % guida)
    # Le figure e la copia .docx si rifanno sempre, perche' dipendono anche dalla prosa, che si scrive
    # a mano: un .docx rigenerato solo quando cambiano le tabelle resterebbe indietro sulla prosa.
    _modulo(Path(__file__).resolve().parent.joinpath("parco_lotta_figure.py"), "figure").main()
    _modulo(RADICE.joinpath("tools", "md-to-docx.py"), "md_to_docx").converti(guida, guida.with_suffix(".docx"))
    print("rigenerate le figure e %s" % guida.with_suffix(".docx"))


def _modulo(percorso, nome):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


if __name__ == "__main__":
    main()
