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

# Il tetto di livello che il Parco impone in modalita' cinquanta, verificato su GetBattleEntryLevelCap e
# GetBattleEntryEligibility in src/party_menu.c: un esemplare di livello superiore non e' penalizzato, e'
# RIFIUTATO all'iscrizione. Il gioco non normalizza in alcun modo il livello del giocatore, quindi un
# esemplare di livello inferiore combatte al proprio livello reale e non viene portato a cinquanta.
#
# Questa costante corregge una affermazione che il progetto aveva registrato il 2026-09-17 e creduta per
# giorni, secondo cui la modalita' cinquanta ricalcolerebbe a cinquanta le statistiche di un esemplare piu'
# alto. E' il funzionamento della quarta generazione e non della terza, e assumerlo qui avrebbe prodotto
# una squadra che allo sportello viene respinta.
TETTO_LIVELLO_MODALITA_50 = 50

# Le mosse che al Dojo Lotta sottraggono un punto alla voce "mente" del giudizio, cioe' quelle che il
# criterio penalizza esplicitamente invece di limitarsi a non premiarle. Un esemplare che le porti non e'
# piu' debole, ma perde un giudizio che avrebbe vinto, ed e' il modo tipico in cui una squadra da Torre
# riciclata al Dojo perde senza che nessuno capisca perche'.
MOSSE_PENALIZZATE_AL_DOJO = {"Protect", "Detect", "Endure", "Fake Out"}

CAPIENZA_BOX = 30


def valida(catalogo, imparabili=None):
    problemi = []
    avvisi = []
    esemplari = catalogo["esemplari"]

    for chiave, e in esemplari.items():
        if e["specie"] in SPECIE_ESCLUSE:
            problemi.append("%s: la specie %s e' esclusa da ogni struttura del Parco" % (chiave, e["specie"]))
        for bloccante, nota in mosse_non_legittime(e, catalogo["livello"], imparabili):
            (problemi if bloccante else avvisi).append("%s: %s" % (chiave, nota))

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


def _chiave_mossa(nome):
    """Normalizza il nome di una mossa per il confronto fra il catalogo e la tabella estratta dal sorgente.

    Le due grafie divergono su trattini e apostrofi, per esempio Soft-Boiled contro Soft Boiled, e un confronto letterale dichiarerebbe non imparabile una mossa che la specie impara benissimo. Si confronta quindi sulle sole lettere e cifre.
    """
    return "".join(c for c in nome.lower() if c.isalnum())


def mosse_non_legittime(esemplare, livello_di_gioco, imparabili):
    """Verifica che ogni mossa sia imparabile dalla specie, e per una via compatibile con il livello di gioco.

    Le vie non sono equivalenti e il loro esito qui non e' lo stesso. Una macchina, un insegnamosse o una mossa da uovo non impongono alcun livello, quindi passano senza rilievi. Una mossa di livello passa se il livello richiesto non supera quello a cui si gioca, tenendo conto che la specie puo' averla imparata da una forma precedente a un livello piu' basso.

    Se il livello richiesto supera il tetto, la mossa non e' perduta e il rilievo non e' un errore: resta la via verificata sul sorgente, cioe' l'eredita' da due genitori che entrambi la conoscono, e l'esito e' un avviso con la catena da dichiarare. Se invece la mossa non compare affatto per quella specie, non esiste via alcuna ed e' un problema bloccante.
    """
    specie = esemplare["specie"]
    tabella = imparabili.get(specie) if imparabili else None
    if tabella is None:
        return []
    per_chiave = {_chiave_mossa(k): (k, v) for k, v in tabella.items()}
    fuori = []
    for mossa in esemplare["mosse"]:
        voce = per_chiave.get(_chiave_mossa(mossa))
        if voce is None:
            fuori.append((True, "%s non e' imparabile da %s per alcuna via nota" % (mossa, specie)))
            continue
        vie = voce[1]
        if vie.get("macchina") or vie.get("insegnamosse") or vie.get("uovo"):
            continue
        livello = vie.get("livello")
        if livello is None or livello <= livello_di_gioco:
            continue
        da = vie.get("da_forma_precedente")
        fuori.append((False, "%s si impara al livello %d%s, oltre il tetto di %d che la modalita' cinquanta impone all'ISCRIZIONE: l'esemplare va quindi ottenuto da due genitori che la conoscono entrambi, secondo la regola di BuildEggMoveset, e non alzando il proprio livello" % (
            mossa, livello, (" su %s" % da) if da else "", TETTO_LIVELLO_MODALITA_50)))
    return fuori


def piano_box(catalogo):
    esemplari = catalogo["esemplari"]
    copie = catalogo["copie_per_esemplare"]
    usati = {}
    for squadra in catalogo["squadre"]:
        for v in squadra["esemplari"]:
            usati.setdefault(v["chiave"], []).append(squadra["edificio"])
    distinti = len(usati)
    slot = distinti * copie
    riserve = sorted(k for k in esemplari if k not in usati and esemplari[k].get("riserva"))
    orfani = sorted(k for k in esemplari if k not in usati and not esemplari[k].get("riserva"))
    totali = distinti + len(riserve)
    slot = totali * copie
    return {
        "esemplari_in_squadra": distinti,
        "esemplari_di_riserva": len(riserve),
        "esemplari_distinti": totali,
        "copie_per_esemplare": copie,
        "slot_necessari": slot,
        "box_interi": (slot + CAPIENZA_BOX - 1) // CAPIENZA_BOX,
        "capienza_box": CAPIENZA_BOX,
        "impiego": {k: sorted(set(v)) for k, v in sorted(usati.items())},
        "riserve": riserve,
        "orfani": orfani,
    }


def scrivi(percorso, catalogo, problemi, avvisi, piano, mosse_controllate):
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
    controllato = "Che cosa e' stato controllato: le dieci specie escluse da ogni struttura, l'unicita' della specie e dello strumento dentro ciascuna squadra, l'assenza di strumenti alla Piramide Lotta, l'assenza di mosse di stato al Palazzo Lotta, il divieto delle mosse che il criterio di giudizio del Dojo Lotta penalizza, e l'esistenza di ogni chiave citata."
    if mosse_controllate:
        controllato += " In piu', per ogni esemplare, che ciascuna mossa sia imparabile dalla propria specie e per quale via, sulla tabella estratta dal sorgente del gioco. Una mossa che richieda un livello oltre il tetto di cinquanta non e' un errore ma una catena di riproduzione da dichiarare, e compare fra gli avvisi."
    else:
        controllato += " NON e' stato controllato se ciascuna mossa sia imparabile dalla propria specie, perche' la tabella non e' stata passata: si rigenera con estrai_mosse_imparabili.py e si passa con --imparabili."
    r.append(controllato)
    r.append("")
    r.append("## Quanti esemplari servono, e quanto spazio")
    r.append("")
    r.append("Esemplari distinti da generare: **%d**, cioe' %d impiegati dalle squadre piu' %d di riserva, che per decisione dell'utente si generano subito insieme agli altri invece di restare sulla carta. Copie per esemplare: %d, perche' una delle due e' destinata a uno scambio gia' concordato. Slot dei box necessari: **%d**, cioe' %d box da %d su quattordici disponibili." % (
        piano["esemplari_distinti"], piano["esemplari_in_squadra"], piano["esemplari_di_riserva"],
        piano["copie_per_esemplare"], piano["slot_necessari"], piano["box_interi"], piano["capienza_box"]))
    r.append("")
    r.append("| Esemplare | Specie | Natura | Edifici in cui entra |")
    r.append("|---|---|---|---|")
    for chiave, edifici in piano["impiego"].items():
        e = catalogo["esemplari"][chiave]
        r.append("| %s | %s | %s | %s |" % (chiave, e["specie"], e["natura"], ", ".join(edifici)))
    r.append("")
    if piano["riserve"]:
        r.append("| Esemplare | Specie | Natura | Ruolo |")
        r.append("|---|---|---|---|")
        for chiave in piano["riserve"]:
            e = catalogo["esemplari"][chiave]
            r.append("| %s | %s | %s | riserva, si genera ma non entra in alcuna squadra iniziale |" % (chiave, e["specie"], e["natura"]))
        r.append("")
        r.append("Le riserve esistono per una ragione operativa e non per completezza: quando una squadra si rompe sul campo, la correzione e' la sostituzione di un esemplare, e averla gia' nella cartuccia significa riprovare la sera stessa invece di aprire una corsa di generazione. Il loro insieme di mosse resta pero' provvisorio, perche' e' stato deciso senza sapere contro che cosa serviranno.")
        r.append("")
    if piano["orfani"]:
        r.append("PROBLEMA: esemplari nel catalogo che non entrano in alcuna squadra e non sono marcati come riserva: %s. Vanno assegnati, marcati o tolti." % ", ".join(piano["orfani"]))
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
            r.append(squadra.get("nota_giri", "I giri non chiedono una squadra ciascuno ma un ordine di conduzione ciascuno."))
            r.append("")
            r.append("| Giro | Tema del bestiario | Primo in campo | Cambio | Da dove viene |")
            r.append("|---|---|---|---|---|")
            for g in squadra["ordine_per_giro"]:
                provenienza = "guida" if g.get("fonte", "").startswith("guida") else "calcolato, da verificare sul campo"
                r.append("| %d | %s | %s | %s | %s |" % (g["giro"], g["tema"], g["primo"], g["cambio"] or "nessuno", provenienza))
            r.append("")
    Path(percorso).write_text("\n".join(r) + "\n", encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--catalogo", required=True)
    p.add_argument("--imparabili", help="mosse-imparabili.json estratto dal sorgente; senza di esso il controllo sulle mosse non viene fatto e l'uscita lo dichiara")
    p.add_argument("--out", required=True)
    args = p.parse_args()

    catalogo = json.loads(Path(args.catalogo).read_text(encoding="utf-8"))
    imparabili = json.loads(Path(args.imparabili).read_text(encoding="utf-8")) if args.imparabili else None
    problemi, avvisi = valida(catalogo, imparabili)
    piano = piano_box(catalogo)
    scrivi(args.out, catalogo, problemi, avvisi, piano, imparabili is not None)

    for x in problemi:
        print("PROBLEMA: %s" % x)
    for x in avvisi:
        print("avviso:   %s" % x)
    for x in piano["orfani"]:
        print("PROBLEMA: %s non entra in alcuna squadra e non e' marcato come riserva" % x)
    print("esemplari distinti: %d (%d in squadra, %d di riserva), slot nei box: %d (%d box da %d)" % (
        piano["esemplari_distinti"], piano["esemplari_in_squadra"], piano["esemplari_di_riserva"],
        piano["slot_necessari"], piano["box_interi"], piano["capienza_box"]))
    print("uscita in %s" % args.out)
    if problemi:
        sys.exit("catalogo non valido: %d problemi" % len(problemi))


if __name__ == "__main__":
    main()
