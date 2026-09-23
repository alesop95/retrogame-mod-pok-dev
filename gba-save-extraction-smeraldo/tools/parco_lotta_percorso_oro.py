#!/usr/bin/env python3
"""Compone il percorso ai sette simboli d'oro: per ogni edificio le serie da giocare, dove compare l'Asso, e quale esemplare prendere da quale posizione di quale box.

Perche' esiste
--------------

Il catalogo dice quali squadre portare e STUDIO-04 dice quante lotte servono, ma chi gioca ha davanti il PC del gioco e non un file: gli serve sapere che per la Torre Lotta il Latios da prendere e' quello del box 12 in prima riga e prima colonna, con quale strumento, in quale ordine di squadra, e a quale lotta arrivera' l'Asso. Questo documento ricompone quelle tre fonti in una sola lista, e lo fa con codice perche' la disposizione nei box discende da una regola, e una regola applicata a mano a sessantaquattro posizioni sbaglia.

La disposizione, che e' ADR-074
-------------------------------

I sessantaquattro file del lotto vanno nei box 12, 13 e 14, con le due copie di ciascun esemplare affiancate: la copia 1 si usa, la copia 2 e' quella destinata allo scambio. Prima gli otto titolari, nell'ordine in cui compaiono per la prima volta nelle squadre del catalogo; poi le ventiquattro riserve, in ordine di frequenza nelle squadre dei thread come la misura `MAPPA-RISERVE.md`, cosi' che le riserve piu' probabili stiano piu' vicine ai titolari. La funzione `disposizione` e' la sola fonte di questa regola: lo strumento di riordino del deposito la importera' invece di riscriverla, perche' due copie della stessa regola possono divergere.

Il box ha trenta posizioni in cinque righe da sei. La posizione si scrive come box, riga e colonna, contando dall'alto a sinistra, perche' e' cosi' che la si trova sullo schermo.

Che cosa non e' ancora vero
---------------------------

Le posizioni sono quelle di DOPO il riordino di ADR-074, che non e' ancora avvenuto: oggi i sessantaquattro esemplari esistono soltanto come file sotto `_notes/lotto-parco-lotta/esemplari`. Il documento generato lo ripete in testa.

Uso
---

    python gba-save-extraction-smeraldo/tools/parco_lotta_percorso_oro.py --out gba-save-extraction-smeraldo/PERCORSO-SIMBOLI-ORO.md
"""

import argparse
import csv
import importlib.util
import json
import re
from pathlib import Path

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
CATALOGO = CARTELLA.joinpath("squadre-parco-lotta.json")
GLOSSARIO = CARTELLA.joinpath("GLOSSARIO-MOSSE.md")
LOTTO = RADICE.joinpath("_notes", "lotto-parco-lotta")
DUMP = LOTTO.joinpath("Box Data Dump round6.csv")

BOX_DEL_LOTTO = (12, 13, 14)
POSIZIONI = 30
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

NOTE_EDIFICIO = {
    "Cupola Lotta": "Torneo a eliminazione di sedici, quattro incontri per torneo, due contro due: si iscrivono tre esemplari e prima di ogni incontro, vista la squadra avversaria, se ne scelgono due. Gli avversari hanno tre punti individuali su ogni statistica fino alla fine, per il difetto di `CreateDomeOpponentMon`. Un pareggio, per esempio con Esplosione, lo vince la testa di serie migliore, e questa squadra si piazza quasi sempre prima.",
    "Azienda Lotta": "Non si porta nulla dal PC: si combatte con esemplari in prestito, e dopo ogni vittoria si puo' scambiarne uno con uno dell'avversario battuto. Va portata all'oro PRIMA di costruire una serie lunga alla Torre Lotta a livello 50, perche' i punti individuali dei suoi avversari dipendono dalla serie corrente della Torre, per il difetto in `src/battle_tower.c`.",
    "Torre Lotta": "Tre contro tre, nessuna regola in piu'. Il primo della squadra e' il primo a scendere in campo.",
    "Dojo Lotta": "Tre turni per incontro, poi giudizio a punti: premia le mosse che fanno danno e quelle che vanno a segno, toglie un punto a Protezione, Individua e Resistenza, che questa squadra non porta. Il primo della squadra scende per primo, e l'ordine conta perche' gli esemplari si affrontano uno contro uno in sequenza.",
    "Palazzo Lotta": "Non si comanda: ogni esemplare sceglie da se' secondo la propria natura. E' la ragione per cui questa squadra ha nature proprie e solo mosse d'attacco, spiegata in STUDIO-04 sezione 12.",
    "Serpe Lotta": "Quattordici sale per serie, tre porte per sala, e solo alcune sale sono lotte. Metagross e' immune all'iperavvelenamento della sala delle alterazioni di stato, che e' la piu' probabile al trentacinque per cento.",
    "Piramide Lotta": "Gli strumenti vengono tolti all'ingresso, quindi si entra senza. Ogni serie di sette piani ha un bestiario a tema, il giro, e cambia chi conduce. Gli oggetti si raccolgono dentro.",
}


def _mappa():
    percorso = Path(__file__).resolve().parent.joinpath("parco_lotta_mappa_riserve.py")
    spec = importlib.util.spec_from_file_location("mappa_riserve", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def disposizione(catalogo, thread):
    """Restituisce l'elenco ordinato delle chiavi del lotto e la posizione di ciascuna copia: {(chiave, copia): (box, posizione)}."""
    generati, titolari, per_specie, righe, _ = _mappa().misura(catalogo, thread)
    ordine = []
    for squadra in catalogo["squadre"]:
        for v in squadra["esemplari"]:
            if v["chiave"] in titolari and v["chiave"] not in ordine:
                ordine.append(v["chiave"])
    riserve = [k for k in generati if k not in titolari]
    riserve.sort(key=lambda k: (-sum(righe[generati[k]["specie"]]["edifici"].values()), k))
    ordine += riserve
    copie = catalogo["copie_per_esemplare"]
    posizioni = {}
    indice = 0
    for chiave in ordine:
        for copia in range(1, copie + 1):
            box = BOX_DEL_LOTTO[indice // POSIZIONI]
            posizioni[(chiave, copia)] = (box, indice % POSIZIONI + 1)
            indice += 1
    return ordine, posizioni, generati, titolari


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
    """Il nome italiano di ciascuna natura, letto dal dump di PKHeX del sesto giro come per gli strumenti."""
    manifesto = json.loads(LOTTO.joinpath("manifesto.json").read_text(encoding="utf-8"))
    per_pid = {}
    with DUMP.open(encoding="utf-8-sig") as f:
        for riga in csv.DictReader(f):
            per_pid[riga["PID"].upper()] = riga["Nature"]
    return {voce["natura"]: per_pid[voce["copie"][0]["personalita"][2:].upper()]
            for voce in manifesto["esemplari"] if voce["copie"][0]["personalita"][2:].upper() in per_pid}


def strumenti_italiani():
    """Il nome italiano di ciascuno strumento, letto dove il gioco lo scrive e non tradotto: dal dump di PKHeX del sesto giro, accoppiato alla personalita' registrata nel manifesto."""
    manifesto = json.loads(LOTTO.joinpath("manifesto.json").read_text(encoding="utf-8"))
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


def scrivi(catalogo, thread):
    ordine, posizioni, generati, titolari = disposizione(catalogo, thread)
    mosse_it = glossario()
    strum_it = strumenti_italiani()
    nat_it = nature_italiane()
    sostituzioni = _mappa().misura(catalogo, thread)[4]
    manifesto = json.loads(LOTTO.joinpath("manifesto.json").read_text(encoding="utf-8"))
    nel_file = {v["chiave"]: v.get("strumento") for v in manifesto["esemplari"]}
    out = []
    out.append("# Il percorso ai sette simboli d'oro, edificio per edificio e posizione per posizione")
    out.append("")
    out.append("> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_percorso_oro.py` dal catalogo `squadre-parco-lotta.json`, dal calendario di `src/frontier_util.c` registrato in STUDIO-04 sezione 5, dal glossario delle mosse e dal dump di PKHeX del sesto giro per i nomi italiani degli strumenti. Non si modifica a mano: si rigenera.")
    out.append(">")
    out.append("> Le posizioni nei box sono quelle di DOPO il riordino di ADR-074, che non e' ancora avvenuto: oggi i sessantaquattro esemplari esistono soltanto come file. Tutte le sfide sono nella modalita' Livello 50. La copia 1 di ogni esemplare si usa, la copia 2 accanto e' quella per lo scambio.")
    out.append("")
    out.append("## L'ordine degli edifici")
    out.append("")
    out.append("L'ordine viene dai difetti del gioco e non dal gusto, ed e' spiegato in STUDIO-05 sezione 1: prima la Cupola, poi l'Azienda, che va chiusa prima di allungare la serie alla Torre, poi Torre, Dojo, Palazzo, Serpe e Piramide. L'Azienda si puo' giocare subito, perche' non chiede nulla dal PC.")
    out.append("")
    for squadra in sorted(catalogo["squadre"], key=lambda s: int(s["ordine"])):
        edificio = squadra["edificio"]
        unita, argento, oro, per_serie, asso, simbolo, _ = CALENDARIO[edificio]
        out.append("## %s. %s, Simbolo %s" % (squadra["ordine"], edificio, simbolo))
        out.append("")
        out.append(NOTE_EDIFICIO[edificio])
        out.append("")
        if edificio == "Cupola Lotta":
            out.append("Si gioca torneo dopo torneo, senza perderne uno. %s compare la prima volta nella %s e da' il simbolo d'argento; la seconda volta nella %s e da' il simbolo d'oro. In tutto sono dieci tornei e quaranta incontri." % (asso, dove_cade(edificio, argento), dove_cade(edificio, oro)))
        else:
            serie_oro = -(-(oro if CALENDARIO[edificio][6] == 1 else oro + 1) // per_serie)
            out.append("Si gioca una serie dopo l'altra senza interruzioni, perche' una sconfitta azzera la serie. %s compare la prima volta %s, per l'argento, e la seconda %s, per l'oro: servono %d serie di fila." % (asso, dove_cade(edificio, argento), dove_cade(edificio, oro), serie_oro))
        out.append("")
        if not squadra["esemplari"]:
            continue
        out.append("| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |")
        out.append("|---|---|---|---|---|")
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
        out.append("")
        if any(v.get("mosse_sostituite") for v in squadra["esemplari"]):
            out.append("Le mosse cambiate per questo edificio si insegnano in gioco con le MT prima di entrare. In terza generazione una MT si consuma all'uso, e la mossa sovrascritta non torna gratis: e' una delle ragioni per cui questo edificio viene per ultimo.")
            out.append("")
        if squadra.get("ordine_per_giro"):
            out.append("Chi conduce, serie per serie. Le prime dieci serie bastano all'oro e vengono dalla guida al completamento; la colonna del calcolo e' il controllo di `parco_lotta_piramide_ordine.py`, che concorda con la guida in sette casi su dieci sul membro impiegato.")
            out.append("")
            out.append("| Serie | Piani | Tema del giro | Primo in campo | Cambio | Calcolo |")
            out.append("|---|---|---|---|---|---|")
            for g in squadra["ordine_per_giro"][:10]:
                a = (g["giro"] - 1) * 7 + 1
                out.append("| %d | %d-%d | %s | %s | %s | %s |" % (g["giro"], a, a + 6, g["tema"], g["primo"], g["cambio"] or "nessuno", g["calcolato"]))
            out.append("")
        candidati = [(u, c) for e_, u, _, c in sostituzioni if e_ == edificio]
        if candidati:
            testo = "; ".join("al posto di %s, %s" % (generati[u]["specie"], ", ".join(
                "%s (%s)" % (sp, dove(posizioni[(next(k for k in ordine if generati[k]["specie"] == sp), 1)])) for _, _, _, sp in c[:2]))
                for u, c in candidati)
            out.append("Riserve con piu' riscontri accanto agli altri due, dalla misura di `MAPPA-RISERVE.md` e quindi non ancora una scelta: %s." % testo)
            out.append("")
    out.append("## La disposizione completa dei box 12, 13 e 14")
    out.append("")
    out.append("| Box | Riga | Colonna | Esemplare | Copia | Ruolo |")
    out.append("|---|---|---|---|---|---|")
    for (chiave, copia), (box, n) in sorted(posizioni.items(), key=lambda x: x[1]):
        e = generati[chiave]
        out.append("| %d | %d | %d | %s %s | %d | %s |" % (box, (n - 1) // COLONNE + 1, (n - 1) % COLONNE + 1, e["specie"], nat_it.get(e["natura"], e["natura"]), copia, "titolare" if chiave in titolari else "riserva"))
    out.append("")
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--out")
    args = p.parse_args()
    catalogo = json.loads(CATALOGO.read_text(encoding="utf-8"))
    thread = json.loads(_mappa().THREAD.read_text(encoding="utf-8"))
    testo = scrivi(catalogo, thread)
    if args.out:
        Path(args.out).write_bytes((testo + "\n").encode("utf-8"))
        print("scritto %s" % args.out)
    else:
        print(testo)


if __name__ == "__main__":
    main()
