#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controlla, a ogni apertura di sessione, se le fonti degli eventi Pokémon hanno qualcosa di nuovo da censire.

Perché esiste
-------------
Il 2026-11-03 il proprietario ha chiesto che a ogni riapertura del progetto parta da sé un controllo delle fonti
di eventi nuovi, perché la collezione continua anche quando tutto il lavoro sarà sui giochi per Switch, e un
evento che nessuno ha censito non entra mai in nessuna lista. Il controllo è deterministico e costa due chiamate
di rete: un programma, non un modello, perché la domanda è se due impronte coincidono.

Le fonti sorvegliate sono due, e sono quelle da cui il progetto già genera. La prima è l'archivio
`projectpokemon/EventsGallery`, l'archivio collettivo dei doni segreti di tutte le generazioni, letto per intero
dal progetto il 2026-10-05 (16397 file, ultimo commit di allora `154d81b` del 2026-09-06): ogni file nuovo sotto
`Released/` è un evento da censire. La seconda è la libreria `kwsch/PKHeX`, che gli strumenti `tools/pkhex-*`
compilano dal clone in `_notes/fonti/cloni/pkhex`: un commit a monte che tocca gli incontri o il database dei doni
cambia ciò che la libreria sa generare e giudicare, e da quel momento i giudizi dei lotti presi con il clone vecchio
non sono più quelli della libreria corrente.

Che cosa fa
-----------
Per l'archivio confronta il commit fino al quale il progetto ha censito, registrato in
`_notes/lavoro/stato/controllo-eventi.json`, con la testa del ramo a monte, ed elenca i file aggiunti o modificati
sotto `Released/`, raggruppati per generazione e gioco. Per la libreria confronta il commit del clone locale con la
testa a monte ed elenca i file toccati che riguardano incontri o doni. Non scrive niente nelle liste del progetto:
il censimento lo fa l'agente, e quando è fatto lo si registra con `--segna`, che sposta il punto di partenza alla
testa corrente dell'archivio. Finché non lo si fa, ogni apertura ripete il promemoria, ed è voluto.

Senza rete, o con il servizio che non risponde, dice «non verificabile» ed esce con zero: un controllo di apertura
non deve mai bloccare una sessione, ma non deve nemmeno far passare il silenzio per un esito.

Uso
---
    python tools/controlla-eventi-nuovi.py             rapporto completo
    python tools/controlla-eventi-nuovi.py --breve     poche righe, per l'hook SessionStart
    python tools/controlla-eventi-nuovi.py --segna     censimento fatto fino alla testa corrente dell'archivio
    python tools/controlla-eventi-nuovi.py --autotest  prove interne, senza rete
"""

import argparse
import collections
import datetime
import json
import os
import subprocess
import sys
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATO = os.path.join(RADICE, "_notes", "lavoro", "stato", "controllo-eventi.json")
CLONE_PKHEX = os.path.join(RADICE, "_notes", "fonti", "cloni", "pkhex")
ARCHIVIO = "projectpokemon/EventsGallery"
LIBRERIA = "kwsch/PKHeX"
BASE_ARCHIVIO = "154d81b"  # ultimo commit dell'archivio prima della lettura integrale del 2026-10-05
UA = "retrogame-mod-pok-dev (controllo eventi, sola lettura)"
PAROLE_LIBRERIA = ("mgdb", "resources/byte", "encounter", "mysterygift", "wondercard")


def api(percorso, timeout=10):
    """Chiama l'API di GitHub: prima con `gh`, che è autenticato, poi senza credenziali."""
    try:
        uscita = subprocess.run(["gh", "api", percorso], capture_output=True, text=True, encoding="utf-8",
                                timeout=timeout)
        if uscita.returncode == 0 and uscita.stdout.strip():
            return json.loads(uscita.stdout)
    except (OSError, subprocess.TimeoutExpired, ValueError):
        pass
    richiesta = urllib.request.Request("https://api.github.com/" + percorso, headers={"User-Agent": UA})
    with urllib.request.urlopen(richiesta, timeout=timeout) as risposta:
        return json.loads(risposta.read().decode("utf-8"))


def leggi_stato():
    try:
        with open(STATO, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def scrivi_stato(stato):
    os.makedirs(os.path.dirname(STATO), exist_ok=True)
    with open(STATO, "w", encoding="utf-8", newline="\n") as f:
        json.dump(stato, f, ensure_ascii=False, indent=1)
        f.write("\n")


def commit_clone():
    try:
        uscita = subprocess.run(["git", "-C", CLONE_PKHEX, "rev-parse", "HEAD"], capture_output=True, text=True,
                                timeout=10)
        return uscita.stdout.strip() or None
    except (OSError, subprocess.TimeoutExpired):
        return None


def nuovi_eventi(confronto):
    """Dai file di un confronto dell'archivio tiene quelli sotto Released/, per generazione e gioco."""
    gruppi = collections.OrderedDict()
    for f in confronto.get("files", []):
        nome = f.get("filename", "")
        if not nome.startswith("Released/") or f.get("status") == "removed":
            continue
        parti = nome.split("/")
        chiave = " ".join(parti[1:3]) if len(parti) > 3 else parti[1]
        gruppi.setdefault(chiave, []).append(parti[-1])
    return gruppi


def file_libreria(confronto):
    return [f["filename"] for f in confronto.get("files", [])
            if any(p in f.get("filename", "").lower() for p in PAROLE_LIBRERIA)]


def controlla(chiama=api):
    stato = leggi_stato()
    esito = {"archivio": None, "libreria": None, "errori": []}
    base = stato.get("archivio_censito_fino_a", BASE_ARCHIVIO)
    try:
        c = chiama("repos/%s/compare/%s...master" % (ARCHIVIO, base))
        esito["archivio"] = {"base": base[:7], "testa": c["commits"][-1]["sha"] if c.get("commits") else None,
                             "commit": c.get("ahead_by", 0), "gruppi": nuovi_eventi(c),
                             "messaggi": [x["commit"]["message"].split("\n")[0] for x in c.get("commits", [])][-5:]}
    except Exception as e:  # rete, servizio o risposta inattesa: non verificabile, non zero eventi
        esito["errori"].append("archivio: %s" % e.__class__.__name__)
    clone = commit_clone()
    if clone:
        try:
            c = chiama("repos/%s/compare/%s...master" % (LIBRERIA, clone))
            esito["libreria"] = {"base": clone[:7], "commit": c.get("ahead_by", 0), "file": file_libreria(c)}
        except Exception as e:
            esito["errori"].append("libreria: %s" % e.__class__.__name__)
    else:
        esito["errori"].append("libreria: clone locale assente in _notes/fonti/cloni/pkhex")
    return esito


def stampa(esito, breve):
    print("=== Controllo eventi nuovi (tools/controlla-eventi-nuovi.py) ===")
    a, l = esito["archivio"], esito["libreria"]
    da_fare = False
    if a is None:
        print("EventsGallery: non verificabile adesso.")
    elif not a["gruppi"]:
        print("EventsGallery: nessun evento nuovo dal commit censito %s." % a["base"])
    else:
        da_fare = True
        n = sum(len(v) for v in a["gruppi"].values())
        print("EventsGallery: %d file di eventi nuovi in %d commit dal commit censito %s." % (n, a["commit"], a["base"]))
        for chiave, nomi in a["gruppi"].items():
            print("  %s: %d%s" % (chiave, len(nomi), "" if breve else " -> " + "; ".join(nomi[:8])))
    if l is None:
        print("PKHeX: non verificabile adesso.")
    elif not l["commit"]:
        print("PKHeX: il clone locale %s è alla testa a monte." % l["base"])
    else:
        da_fare = da_fare or bool(l["file"])
        print("PKHeX: il clone locale %s è indietro di %d commit; %d file toccano incontri o doni." %
              (l["base"], l["commit"], len(l["file"])))
        if not breve:
            for f in l["file"][:20]:
                print("  " + f)
    for e in esito["errori"]:
        print("  (" + e + ")")
    if da_fare:
        print("Per l'agente: ricorda al proprietario questi eventi a inizio sessione e registrali in "
              "`.claude/memory/pending.md`; a censimento fatto, `python tools/controlla-eventi-nuovi.py --segna`.")


def segna(chiama=api):
    c = chiama("repos/%s/commits/master" % ARCHIVIO)
    stato = leggi_stato()
    stato["archivio_censito_fino_a"] = c["sha"]
    stato["segnato_il"] = datetime.date.today().isoformat()
    scrivi_stato(stato)
    print("Censimento dell'archivio registrato fino a %s." % c["sha"][:7])


def autotest():
    global STATO
    finto_confronto = {"ahead_by": 2, "commits": [{"sha": "a" * 40, "commit": {"message": "Add Z-A WCs\nx"}}],
                       "files": [{"filename": "Released/Gen 9/ZA/Wondercards/0104 ZA - Item.wa9", "status": "added"},
                                 {"filename": "Released/Gen 9/ZA/Wondercards/0105 ZA - Pkmn.wa9", "status": "modified"},
                                 {"filename": "Released/Gen 9/ZA/Wondercards/old.wa9", "status": "removed"},
                                 {"filename": "README.md", "status": "modified"}]}
    g = nuovi_eventi(finto_confronto)
    casi = [(list(g) == ["Gen 9 ZA"], "raggruppa per generazione e gioco"),
            (len(g.get("Gen 9 ZA", [])) == 2, "conta aggiunti e modificati, non i rimossi né i file fuori da Released/"),
            (file_libreria({"files": [{"filename": "PKHeX.Core/Legality/Encounters/X.cs"},
                                      {"filename": "PKHeX.WinForms/Y.cs"}]}) == ["PKHeX.Core/Legality/Encounters/X.cs"],
             "filtra i file della libreria che toccano incontri o doni")]

    def guasto(_):
        raise OSError("rete assente")
    vecchio, STATO = STATO, os.path.join(RADICE, "_notes", "tmp", "controllo-eventi-autotest.json")
    try:
        e = controlla(chiama=guasto)
        casi.append((e["archivio"] is None and e["errori"], "senza rete l'esito è non verificabile, non zero eventi"))
    finally:
        STATO = vecchio
    falliti = [n for ok, n in casi if not ok]
    for n in falliti:
        print("FALLITO: " + n)
    print("%d casi superati su %d" % (len(casi) - len(falliti), len(casi)))
    return 1 if falliti else 0


def main():
    p = argparse.ArgumentParser(description="Controllo delle fonti di eventi nuovi.")
    p.add_argument("--breve", action="store_true")
    p.add_argument("--segna", action="store_true")
    p.add_argument("--autotest", action="store_true")
    a = p.parse_args()
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    if a.autotest:
        return autotest()
    if a.segna:
        segna()
        return 0
    stampa(controlla(), a.breve)
    return 0


if __name__ == "__main__":
    sys.exit(main())
