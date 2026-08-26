#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cancello di sicurezza e pianificatore per la scrittura di un salvataggio su hardware.

Perché esiste
--------------
Tre dei cinque sottoprogetti finiscono, presto o tardi, con la stessa operazione: prendere
un file di salvataggio e metterlo su un supporto fisico, cioè una cartuccia tramite il
lettore oppure la scheda SD della console modificata. È l'unica operazione irreversibile
del progetto, ed è la sola dove un errore banale, per esempio scrivere un salvataggio da
128 KiB su una memoria da 64, distrugge dati di vent'anni.

Questo strumento è la parte di quell'operazione che si può scrivere e collaudare oggi,
senza avere l'hardware in mano, ed è anche la parte che evita i danni: valida il file,
identifica il gioco, verifica che i backup obbligatori esistano davvero, e produce il piano
dei passi da eseguire. La scrittura vera non è implementata e non lo sarà finché il
lettore non è presente e collaudato: lo strumento la dichiara e si ferma.

La regola normativa che questo codice mette in atto è `.claude/rules/hardware-and-perimeter.md`,
cioè nessuna scrittura senza backup in doppia copia su percorsi distinti e verificato
leggibile, e nessuna scrittura senza rilettura confrontata byte per byte.

Cosa non fa, dichiarato
-----------------------
Non scrive, non apre porte seriali, non parla con FlashGBX né con la console. Non modifica
il file di salvataggio in alcun modo: lo apre in sola lettura. Non giudica la legalità del
contenuto, che è un'altra cosa e appartiene agli strumenti di verifica come PKHeX.

Uso
---
    python tools/save-deploy.py check "percorso/salvataggio.sav"
    python tools/save-deploy.py targets
    python tools/save-deploy.py plan "percorso/salvataggio.sav" --target gbxcart --backup "D:/bk1/pre.sav" --backup "E:/bk2/pre.sav"
"""

import argparse
import hashlib
import importlib.util
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Le dimensioni che hanno un significato, con il supporto che le produce. Una dimensione
# fuori da questa tabella non è necessariamente sbagliata, ma è sempre sospetta, e la
# lezione viene da un caso reale letto su GBAtemp: un salvataggio da 128 KiB scritto su una
# cartuccia con SRAM da 64 KiB non entra, e il tentativo fallisce ogni volta.
DIMENSIONI = {
    8 * 1024: "SRAM da 8 KiB, tipica di una cartuccia Game Boy di prima generazione",
    32 * 1024: "SRAM da 32 KiB, tipica di Game Boy Color e di alcune cartucce GBA",
    64 * 1024: "SRAM o flash da 64 KiB, tipica delle riproduzioni senza batteria",
    128 * 1024: "flash da 128 KiB, la dimensione dei giochi Pokemon di terza generazione",
    131072 + 16: "flash da 128 KiB più un'intestazione di 16 byte aggiunta da alcuni strumenti",
}

# Le destinazioni possibili. La colonna che conta è l'ultima: cosa manca perché quella
# destinazione diventi eseguibile. Nessuna è eseguibile oggi.
DESTINAZIONI = {
    "gbxcart": {
        "descrizione": "cartuccia originale tramite il lettore GBxCart RW, con FlashGBX",
        "dimensioni_ammesse": (32 * 1024, 64 * 1024, 128 * 1024),
        "eseguibile": False,
        "manca": "il lettore, che non è ancora arrivato; e un collaudo su una cartuccia sacrificabile prima di toccare quella di Smeraldo",
    },
    "3ds-sd": {
        "descrizione": "salvataggio sulla scheda SD della console modificata, per un titolo installato",
        "dimensioni_ammesse": (32 * 1024, 128 * 1024),
        "eseguibile": False,
        "manca": "la decisione su quale percorso della SD sia quello giusto per il titolo, che dipende da come è installato; e la conferma che il salvataggio sia nel formato che quel titolo si aspetta",
    },
    "file": {
        "descrizione": "copia su disco, che non è hardware ma è la destinazione dei collaudi",
        "dimensioni_ammesse": tuple(DIMENSIONI.keys()),
        "eseguibile": False,
        "manca": "nulla di tecnico: è disabilitata per coerenza, perché una copia di file la fa il sistema operativo e non serve uno strumento",
    },
}

SETTORE = 4096
FIRMA = 0x08012025


def carica_diagnostica():
    """Importa il lettore di salvataggi Gen 3 del track Smeraldo, se è al suo posto.

    La logica di validazione dei settori, di scelta dello slot più recente e di
    identificazione del gioco vive là e non va duplicata qui: un secondo esemplare della
    stessa formula è un secondo posto dove sbagliarla.
    """
    percorso = os.path.join(ROOT, "gba-save-extraction-smeraldo", "tools", "emerald_bag_decode.py")
    if not os.path.exists(percorso):
        return None
    spec = importlib.util.spec_from_file_location("emerald_bag_decode", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def sha256(percorso):
    h = hashlib.sha256()
    with io.open(percorso, "rb") as fh:
        for blocco in iter(lambda: fh.read(1 << 20), b""):
            h.update(blocco)
    return h.hexdigest()


def esamina(percorso):
    """Ritorna un dizionario di fatti sul file, senza giudizio, più la lista dei problemi."""
    esito = {"percorso": percorso, "problemi": [], "note": []}
    if not os.path.exists(percorso):
        esito["problemi"].append("il file non esiste")
        return esito

    with io.open(percorso, "rb") as fh:
        blob = fh.read()

    esito["dimensione"] = len(blob)
    esito["sha256"] = sha256(percorso)
    esito["forma"] = DIMENSIONI.get(len(blob))
    if esito["forma"] is None:
        esito["problemi"].append(
            "dimensione di %d byte non riconosciuta: le dimensioni con un significato sono %s"
            % (len(blob), ", ".join(str(d) for d in sorted(DIMENSIONI)))
        )

    # La firma di settore è il primo controllo diagnostico che conta su un salvataggio di
    # terza generazione, e la sua assenza è il sintomo che su GBAtemp è costato due giorni
    # a chi non lo conosceva: se non c'è, quel file non è un salvataggio Gen 3 valido,
    # qualunque cosa dica la sua dimensione.
    firme = 0
    if len(blob) >= SETTORE:
        for base in range(0, len(blob) - SETTORE + 1, SETTORE):
            if int.from_bytes(blob[base + 0x0FF8:base + 0x0FFC], "little") == FIRMA:
                firme += 1
    esito["settori_firmati"] = firme

    if firme == 0:
        esito["note"].append(
            "nessun settore porta la firma 0x08012025: non è un salvataggio di terza generazione. "
            "Se doveva essere un salvataggio Game Boy di prima o seconda generazione, la firma non è attesa e questa nota non è un errore"
        )
    else:
        diag = carica_diagnostica()
        if diag is None:
            esito["note"].append("il lettore di diagnosi del track Smeraldo non è al suo posto, quindi slot e gioco non sono stati identificati")
        else:
            valide = [i for i in range(len(blob) // SETTORE)
                      if diag.validate_sector(blob[i * SETTORE:(i + 1) * SETTORE]) is not None]
            esito["settori_validi"] = len(valide)
            if len(valide) < diag.SECTORS_PER_SLOT:
                esito["problemi"].append(
                    "solo %d settori superano la verifica del checksum, e un solo slot ne richiede %d"
                    % (len(valide), diag.SECTORS_PER_SLOT)
                )
            try:
                slot = diag.read_slot(blob, 0)
                sb2, sb1 = diag.assemble(slot)
                # detect_game riferisce tutti i candidati in ordine di punteggio, invece di
                # indovinare: qui interessa il primo, e il margine sul secondo, perché un
                # margine nullo significa che il gioco non è identificato.
                esiti = diag.detect_game(sb2, sb1)
                punti, nome = esiti[0][0], esiti[0][1]
                esito["punteggi"] = {e[1]: e[0] for e in esiti}
                margine = punti - esiti[1][0] if len(esiti) > 1 else punti
                esito["gioco"] = diag.GAMES[nome]["nome"] if margine > 0 and punti > 0 else None
                if esito["gioco"] is None:
                    esito["problemi"].append("il gioco non è identificabile dal contenuto: scrivere un salvataggio senza sapere di che gioco è non è un'operazione da fare")
            except Exception as errore:  # la diagnosi è informativa: il suo fallimento non deve nascondere gli altri esiti
                esito["note"].append("la ricostruzione dello slot non è riuscita: %s" % errore)

    if all(b == 0 for b in blob):
        esito["problemi"].append("il file è interamente a zero: non contiene un salvataggio")
    if all(b == 0xFF for b in blob):
        esito["problemi"].append("il file è interamente a 0xFF, che è lo stato di una memoria flash cancellata")

    return esito


def stampa_esame(esito):
    print("File           %s" % esito["percorso"])
    if "dimensione" in esito:
        print("Dimensione     %d byte (%s)" % (esito["dimensione"], esito["forma"] or "forma non riconosciuta"))
        print("SHA-256        %s" % esito["sha256"])
        print("Settori firmati %d" % esito.get("settori_firmati", 0))
        if "settori_validi" in esito:
            print("Settori validi  %d" % esito["settori_validi"])
        if "gioco" in esito:
            print("Gioco          %s" % (esito["gioco"] or "non identificato"))
            if esito.get("punteggi"):
                print("Punteggi       %s" % ", ".join("%s=%s" % (k, v) for k, v in sorted(esito["punteggi"].items())))
    for nota in esito["note"]:
        print("Nota           %s" % nota)
    for problema in esito["problemi"]:
        print("PROBLEMA       %s" % problema)
    print("Esito          %s" % ("passa" if not esito["problemi"] else "non passa"))


def verifica_backup(percorsi, dimensione_attesa):
    """Il vincolo normativo del progetto, messo in atto: due copie, due percorsi, leggibili."""
    problemi = []
    if len(percorsi) < 2:
        problemi.append("servono due backup su percorsi distinti, ne sono stati dichiarati %d" % len(percorsi))
    reali = [os.path.abspath(p) for p in percorsi]
    if len(set(reali)) < len(reali):
        problemi.append("due percorsi di backup coincidono: una copia sola non è una doppia copia")
    if len({os.path.splitdrive(p)[0].lower() or os.path.dirname(p) for p in reali}) < 2 and len(reali) >= 2:
        problemi.append("i backup stanno sullo stesso volume: un guasto del supporto li perde insieme")
    impronte = set()
    for p in reali:
        if not os.path.exists(p):
            problemi.append("il backup dichiarato non esiste: %s" % p)
            continue
        try:
            impronte.add(sha256(p))
        except OSError as errore:
            problemi.append("il backup non è leggibile, quindi non è un backup: %s (%s)" % (p, errore))
            continue
        if dimensione_attesa is not None and os.path.getsize(p) != dimensione_attesa:
            problemi.append("il backup %s misura %d byte e l'originale %d: non è una copia dello stesso supporto" % (p, os.path.getsize(p), dimensione_attesa))
    if len(impronte) > 1:
        problemi.append("i due backup hanno contenuto diverso: uno dei due non è la copia che si crede")
    return problemi


def piano(esito, destinazione, backup):
    nome = destinazione
    dest = DESTINAZIONI[nome]
    print("Destinazione   %s, cioè %s" % (nome, dest["descrizione"]))
    dimensione = esito.get("dimensione")

    ostacoli = []
    if dimensione is not None and dimensione not in dest["dimensioni_ammesse"]:
        ostacoli.append("quella destinazione accetta %s byte, il file ne ha %d"
                        % (" o ".join(str(d) for d in dest["dimensioni_ammesse"]), dimensione))
    ostacoli.extend(verifica_backup(backup, dimensione))
    for p in ostacoli:
        print("PROBLEMA       %s" % p)

    # Il piano non si mostra quando le precondizioni non sono soddisfatte, e la ragione è
    # di sicurezza e non di forma: una lista di passi stampata sotto un elenco di problemi
    # invita a eseguirla comunque. Il vincolo del backup in doppia copia non ha eccezioni.
    if ostacoli:
        print("")
        print("Il piano non viene prodotto: le precondizioni non sono soddisfatte.")
        print("Il vincolo del backup in doppia copia su percorsi distinti e verificato leggibile è normativo, vedi .claude/rules/hardware-and-perimeter.md, e non si aggira per fretta.")
        return 1

    print("Backup         due copie distinte, leggibili e di dimensione coerente: il vincolo normativo è soddisfatto")
    print("")
    print("Passi previsti, nell'ordine")
    print("  1. dump del contenuto attuale del supporto, che diventa il terzo riferimento della sessione")
    print("  2. confronto del dump con i backup dichiarati: se differiscono, fermarsi e capire perché prima di scrivere")
    print("  3. scrittura del file sul supporto")
    print("  4. rilettura del supporto e confronto byte per byte con il file scritto, che è l'unico modo per dire che la scrittura è avvenuta")
    print("  5. avvio del gioco e verifica che il salvataggio si carichi, che è un controllo diverso dal precedente e non lo sostituisce")
    print("")
    if not dest["eseguibile"]:
        print("La scrittura non viene tentata: questa destinazione non è eseguibile.")
        print("Manca %s" % dest["manca"])
        return 3
    return 0


def main():
    ap = argparse.ArgumentParser(description="valida un salvataggio e pianifica la sua scrittura su hardware, senza scrivere")
    sub = ap.add_subparsers(dest="comando")

    c = sub.add_parser("check", help="esamina un file di salvataggio e dice se è scrivibile")
    c.add_argument("file")

    sub.add_parser("targets", help="elenca le destinazioni e cosa manca a ciascuna")

    p = sub.add_parser("plan", help="produce il piano dei passi verso una destinazione")
    p.add_argument("file")
    p.add_argument("--target", required=True, choices=sorted(DESTINAZIONI))
    p.add_argument("--backup", action="append", default=[], help="percorso di un backup già esistente; va ripetuto due volte")

    args = ap.parse_args()

    if args.comando == "targets":
        for nome, dest in sorted(DESTINAZIONI.items()):
            print("%-10s %s" % (nome, dest["descrizione"]))
            print("%-10s dimensioni ammesse: %s" % ("", " o ".join(str(d) for d in dest["dimensioni_ammesse"])))
            print("%-10s stato: %s" % ("", "eseguibile" if dest["eseguibile"] else "non eseguibile, manca " + dest["manca"]))
            print("")
        return 0

    if args.comando == "check":
        esito = esamina(args.file)
        stampa_esame(esito)
        return 0 if not esito["problemi"] else 1

    if args.comando == "plan":
        esito = esamina(args.file)
        stampa_esame(esito)
        print("")
        if esito["problemi"]:
            print("Il piano non viene prodotto: il file non passa l'esame, e un file che non passa l'esame non si scrive su hardware.")
            return 1
        return piano(esito, args.target, args.backup)

    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
