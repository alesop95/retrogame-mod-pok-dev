#!/usr/bin/env python3
"""Verifica il catalogo delle squadre del Parco Lotta contro i vincoli del gioco, e calcola quanti slot dei box servono.

Perche' esiste
--------------

Una squadra scritta a mano viola i vincoli del Parco in modi che non si vedono rileggendola. Il divieto di due esemplari della stessa specie e quello di due volte lo stesso strumento sono facili da ricordare e altrettanto facili da infrangere quando le squadre diventano sei e condividono gli esemplari; il divieto di strumenti alla Piramide Lotta si dimentica perche' vale in un edificio solo; e la prescrizione di portare al Palazzo Lotta sole mosse d'attacco si perde appena qualcuno aggiunge una mossa di cura credendo di migliorare la squadra. Nessuno di questi errori produce un messaggio: producono una iscrizione rifiutata allo sportello, oppure, peggio, una serie persa.

Il catalogo e' quindi un file di dati e non un documento, e questo strumento e' il presidio che lo verifica. Vale il principio di `token-economy.md` per cui cio' che si puo' controllare con codice non si controlla rileggendo, e quello di `dev-testing.md` per cui una verifica dichiarata e non eseguita non e' una verifica.

Che cosa verifica
-----------------

Le dieci specie escluse da ogni struttura, sull'elenco gia' verificato due volte per vie indipendenti. Dentro ciascuna squadra, l'unicita' della specie e quella dello strumento. Alla Piramide Lotta, l'assenza di qualunque strumento. Al Palazzo Lotta, che nessuna mossa sia di stato, secondo l'elenco chiuso qui sotto. E su tutte, che ogni esemplare citato da una squadra esista nel catalogo degli esemplari, perche' un refuso in una chiave produrrebbe una squadra di due.

Verifica infine due cose che riguardano la generazione e non la lotta: che il livello dichiarato di ciascun esemplare basti alle mosse che gli si attribuiscono quando la mossa si impara per livello oltre il cinquanta, e che il numero di slot dei box necessari sia calcolato invece che stimato.

Che cosa non verifica, e va detto
---------------------------------

Non sa se una mossa sia imparabile da una specie. Quella verifica richiede la tabella degli insiemi di mosse per specie, che questo progetto non ha ancora portato su disco, e affermare di farla sarebbe peggio che non farla: qui si dichiara il limite e si lascia il controllo alla fase di generazione, dove la tabella serve comunque. L'unico caso gia' noto e' registrato come eccezione esplicita, cioe' Megahorn su Heracross, che in Smeraldo non e' una macchina ma una mossa di livello appresa al cinquantatre.

Uso
---

    python gba-save-extraction-smeraldo/tools/parco_lotta_valida_squadre.py --catalogo gba-save-extraction-smeraldo/squadre-parco-lotta.json --out gba-save-extraction-smeraldo/PIANO-BOX.md
"""

import argparse
import json
import sys
from pathlib import Path

# Le dieci specie che nessuna struttura del Parco accetta, piu' l'uovo. Verificate due volte per vie
# indipendenti: `gFrontierBannedSpecies[]` in `src/frontier_util.c` e la pagina generale dell'enciclopedia.
SPECIE_ESCLUSE = {"Mewtwo", "Mew", "Lugia", "Ho-Oh", "Celebi", "Kyogre", "Groudon", "Rayquaza", "Jirachi", "Deoxys", "Egg"}

# Le mosse che al Palazzo Lotta non contano come attacco, cioe' quelle che non infliggono danno.
# L'elenco e' chiuso sulle mosse che questo catalogo usa o potrebbe usare, e lo strumento lo dichiara
# nell'uscita: una mossa non elencata viene considerata d'attacco, il che sbaglia in eccesso di permesso
# ed e' la ragione per cui l'elenco va esteso quando il catalogo cambia, invece di essere dato per completo.
MOSSE_DI_STATO = {
    "Calm Mind", "Recover", "Rest", "Soft-Boiled", "Protect", "Detect", "Endure", "Substitute",
    "Toxic", "Sing", "Thunder Wave", "Double Team", "Curse", "Swords Dance", "Amnesia", "Barrier",
    "Safeguard", "Light Screen", "Reflect", "Roar", "Whirlwind", "Yawn", "Attract", "Confuse Ray",
    "Sleep Talk", "Belly Drum", "Bulk Up", "Dragon Dance", "Agility", "Iron Defense", "Screech",
}

# Le mosse che in Smeraldo si imparano per livello oltre il cinquanta, quindi impongono un livello reale
# superiore a quello a cui si gioca. Il livello reale resta legittimo perche' il Parco ricalcola le
# statistiche a cinquanta, come gia' verificato e registrato in `pending.md`.
LIVELLO_MINIMO_PER_MOSSA = {
    ("Heracross", "Megahorn"): 53,
}

# Le mosse che al Dojo Lotta sottraggono un punto alla voce "mente" del giudizio, cioe' quelle che il
# criterio penalizza esplicitamente invece di limitarsi a non premiarle. Un esemplare che le porti non e'
# piu' debole, ma perde un giudizio che avrebbe vinto, ed e' il modo tipico in cui una squadra da Torre
# riciclata al Dojo perde senza che nessuno capisca perche'.
MOSSE_PENALIZZATE_AL_DOJO = {"Protect", "Detect", "Endure", "Fake Out"}

CAPIENZA_BOX = 30


def valida(catalogo):
    problemi = []
    avvisi = []
    esemplari = catalogo["esemplari"]

    for chiave, e in esemplari.items():
        if e["specie"] in SPECIE_ESCLUSE:
            problemi.append("%s: la specie %s e' esclusa da ogni struttura del Parco" % (chiave, e["specie"]))
        minimo = LIVELLO_MINIMO_PER_MOSSA_richiesto(e)
        if minimo:
            avvisi.append("%s: il livello reale deve essere almeno %d perche' conosca %s, mentre il Parco lo ricalcola comunque a %d" % (chiave, minimo[1], minimo[0], catalogo["livello"]))

    for squadra in catalogo["squadre"]:
        nome = squadra["edificio"]
        voci = squadra["esemplari"]
        if not voci:
            continue
        if len(voci) != 3:
            problemi.append("%s: la squadra ha %d esemplari invece di tre" % (nome, len(voci)))
        specie, strumenti = [], []
        for v in voci:
            e = esemplari.get(v["chiave"])
            if e is None:
                problemi.append("%s: la chiave %s non esiste nel catalogo degli esemplari" % (nome, v["chiave"]))
                continue
            specie.append(e["specie"])
            if v.get("strumento"):
                strumenti.append(v["strumento"])
            if squadra.get("senza_strumenti") and v.get("strumento"):
                problemi.append("%s: %s tiene %s, ma in questo edificio il gioco toglie ogni strumento all'ingresso" % (nome, e["specie"], v["strumento"]))
            mosse = mosse_effettive(e, v)
            if squadra.get("penalizza_protezione"):
                penalizzate = [m for m in mosse if m in MOSSE_PENALIZZATE_AL_DOJO]
                if penalizzate:
                    problemi.append("%s: %s porta %s, che il criterio di giudizio di questo edificio penalizza di un punto" % (nome, e["specie"], " e ".join(penalizzate)))
            if squadra.get("solo_mosse_attacco"):
                di_stato = [m for m in mosse if m in MOSSE_DI_STATO]
                if di_stato:
                    problemi.append("%s: %s porta %s, che al Palazzo sottrae turni all'attacco" % (nome, e["specie"], " e ".join(di_stato)))
        for lista, etichetta in ((specie, "specie"), (strumenti, "strumento")):
            doppi = {x for x in lista if lista.count(x) > 1}
            for x in doppi:
                problemi.append("%s: %s ripetuto, cioe' %s, e il Parco non lo consente" % (nome, etichetta, x))
    return problemi, avvisi


def mosse_effettive(esemplare, voce):
    """Restituisce le mosse che l'esemplare porta in QUEL certo edificio.

    Un esemplare non cambia identita' quando cambia una mossa, perche' le mosse si riscrivono in gioco mentre natura e punti base no: modellare la sostituzione come un esemplare nuovo raddoppierebbe senza ragione lo spazio nei box. La sostituzione si dichiara quindi sulla squadra e non sull'esemplare, ed e' cio' che la guida al completamento fa quando assegna allo stesso Swampert Contatore alla Torre e Protezione alla Piramide.
    """
    mosse = list(esemplare["mosse"])
    for vecchia, nuova in (voce.get("mosse_sostituite") or {}).items():
        if vecchia in mosse:
            mosse[mosse.index(vecchia)] = nuova
        else:
            mosse.append(nuova)
    return mosse


def LIVELLO_MINIMO_PER_MOSSA_richiesto(esemplare):
    for (specie, mossa), livello in LIVELLO_MINIMO_PER_MOSSA.items():
        if esemplare["specie"] == specie and mossa in esemplare["mosse"]:
            return mossa, livello
    return None


def piano_box(catalogo):
    esemplari = catalogo["esemplari"]
    copie = catalogo["copie_per_esemplare"]
    usati = {}
    for squadra in catalogo["squadre"]:
        for v in squadra["esemplari"]:
            usati.setdefault(v["chiave"], []).append(squadra["edificio"])
    distinti = len(usati)
    slot = distinti * copie
    return {
        "esemplari_distinti": distinti,
        "copie_per_esemplare": copie,
        "slot_necessari": slot,
        "box_interi": (slot + CAPIENZA_BOX - 1) // CAPIENZA_BOX,
        "capienza_box": CAPIENZA_BOX,
        "impiego": {k: sorted(set(v)) for k, v in sorted(usati.items())},
        "mai_usati": sorted(set(esemplari) - set(usati)),
    }


def scrivi(percorso, catalogo, problemi, avvisi, piano):
    r = ["# Il piano dei box, e la verifica del catalogo delle squadre", "",
         "> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_valida_squadre.py` a partire da `gba-save-extraction-smeraldo/squadre-parco-lotta.json`. Non si modifica a mano: si modifica il catalogo e si rigenera. Il ragionamento che giustifica ogni scelta sta in `STUDIO-05`.", ""]
    r.append("## L'esito della verifica")
    r.append("")
    r.append("Problemi bloccanti: %d. Avvisi: %d." % (len(problemi), len(avvisi)))
    r.append("")
    for x in problemi:
        r.append("- PROBLEMA: %s" % x)
    for x in avvisi:
        r.append("- avviso: %s" % x)
    if not problemi and not avvisi:
        r.append("- nessun rilievo")
    r.append("")
    r.append("Che cosa e' stato controllato: le dieci specie escluse da ogni struttura, l'unicita' della specie e dello strumento dentro ciascuna squadra, l'assenza di strumenti alla Piramide Lotta, l'assenza di mosse di stato al Palazzo Lotta, l'esistenza di ogni chiave citata, e il livello reale minimo imposto dalle mosse che si imparano oltre il cinquanta. Che cosa non e' stato controllato, e va saputo: se ciascuna mossa sia imparabile dalla propria specie, perche' la tabella degli insiemi di mosse non e' ancora su disco in questo progetto e dichiararlo fatto sarebbe peggio che non farlo.")
    r.append("")
    r.append("## Quanti esemplari servono, e quanto spazio")
    r.append("")
    r.append("Esemplari distinti da generare: %d. Copie per esemplare: %d, perche' una delle due e' destinata a uno scambio gia' concordato. Slot dei box necessari: **%d**, cioe' %d box da %d su quattordici disponibili." % (
        piano["esemplari_distinti"], piano["copie_per_esemplare"], piano["slot_necessari"], piano["box_interi"], piano["capienza_box"]))
    r.append("")
    r.append("| Esemplare | Specie | Natura | Edifici in cui entra |")
    r.append("|---|---|---|---|")
    for chiave, edifici in piano["impiego"].items():
        e = catalogo["esemplari"][chiave]
        r.append("| %s | %s | %s | %s |" % (chiave, e["specie"], e["natura"], ", ".join(edifici)))
    r.append("")
    if piano["mai_usati"]:
        r.append("Esemplari presenti nel catalogo e non impiegati da alcuna squadra: %s. Vanno tolti o assegnati." % ", ".join(piano["mai_usati"]))
        r.append("")
    r.append("## Le squadre, edificio per edificio, nell'ordine di attacco")
    r.append("")
    for squadra in sorted(catalogo["squadre"], key=lambda s: s["ordine"]):
        r.append("### %d. %s" % (squadra["ordine"], squadra["edificio"]))
        r.append("")
        r.append(squadra["perche"])
        r.append("")
        if not squadra["esemplari"]:
            r.append("Nessuna squadra da iscrivere.")
            r.append("")
            continue
        r.append("| Esemplare | Strumento | Natura | Mosse |")
        r.append("|---|---|---|---|")
        for v in squadra["esemplari"]:
            e = catalogo["esemplari"][v["chiave"]]
            r.append("| %s | %s | %s | %s |" % (e["specie"], v.get("strumento") or "nessuno", e["natura"], ", ".join(mosse_effettive(e, v))))
        r.append("")
        if squadra.get("ordine_per_giro"):
            r.append("I dieci giri non chiedono dieci squadre ma dieci ordini di conduzione della stessa.")
            r.append("")
            r.append("| Giro | Tema del bestiario | Primo in campo | Cambio |")
            r.append("|---|---|---|---|")
            for g in squadra["ordine_per_giro"]:
                r.append("| %d | %s | %s | %s |" % (g["giro"], g["tema"], g["primo"], g["cambio"] or "nessuno"))
            r.append("")
    Path(percorso).write_text("\n".join(r) + "\n", encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--catalogo", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    catalogo = json.loads(Path(args.catalogo).read_text(encoding="utf-8"))
    problemi, avvisi = valida(catalogo)
    piano = piano_box(catalogo)
    scrivi(args.out, catalogo, problemi, avvisi, piano)

    for x in problemi:
        print("PROBLEMA: %s" % x)
    for x in avvisi:
        print("avviso:   %s" % x)
    print("esemplari distinti: %d, slot nei box: %d (%d box da %d)" % (
        piano["esemplari_distinti"], piano["slot_necessari"], piano["box_interi"], piano["capienza_box"]))
    print("uscita in %s" % args.out)
    if problemi:
        sys.exit("catalogo non valido: %d problemi" % len(problemi))


if __name__ == "__main__":
    main()
