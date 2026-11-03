#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controlla, a ogni apertura di sessione, se le fonti degli eventi Pokémon hanno qualcosa di nuovo da censire.

Perché esiste
-------------
Il 2026-11-03 il proprietario ha chiesto che a ogni riapertura del progetto parta da sé un controllo delle fonti
di eventi nuovi, perché la collezione continua anche quando tutto il lavoro sarà sui giochi per Switch, e un
evento che nessuno ha censito non entra mai in nessuna lista. Lo stesso giorno ha chiesto che le fonti sorvegliate
siano tutte quelle necessarie alla completezza, non due. Il controllo è deterministico: un programma, non un
modello, perché la domanda è se qualcosa è cambiato rispetto a ciò che il progetto ha già censito.

Le fonti sono cinque, perché un evento passa da tre stati e ciascuno ha la sua fonte. Annunciato: Serebii, i
titoli delle notizie del giorno filtrati sui giochi della collezione e la pagina dei doni di HOME, che riportano
una distribuzione appena viene comunicata, prima che esista un file. La pagina degli eventi in corso di Serebii
è stata scartata il 2026-11-03 perché ferma al 2024. Registrato: Bulbapedia, tutte le liste di distribuzioni collegate dalla pagina indice
«List of event Pokémon distributions», compresa quella di HOME, sorvegliate per numero di revisione attraverso
l'API MediaWiki, la stessa via di `tools/fetch-bulbapedia.py`. Conservato: l'archivio
`projectpokemon/EventsGallery`, i cui file sotto `Released/` sono i doni stessi, letto per intero dal progetto il
2026-10-05 fino a `154d81b`, e la libreria `kwsch/PKHeX`, da cui gli strumenti `tools/pkhex-*` generano e
giudicano, confrontata con il clone locale. Un evento che salti tutte e cinque non è stato distribuito.

Che cosa fa
-----------
Per ogni fonte confronta lo stato corrente con quello censito, registrato in
`pokedex-home-completo/data/controllo-eventi.json`, tracciato, ed elenca ciò che è cambiato: file nuovi dell'archivio per
generazione e gioco, commit della libreria che toccano incontri o doni, pagine di Bulbapedia con una revisione
nuova, righe nuove delle due pagine di Serebii. Non scrive niente nelle liste del progetto: il censimento lo fa
l'agente, e a censimento fatto lo si registra con `--segna`, che porta tutte le fonti allo stato corrente.
Finché non lo si fa, ogni apertura ripete il promemoria, ed è voluto. Una fonte che non risponde dice «non
verificabile» ed esce con zero: un controllo di apertura non blocca una sessione, ma non fa passare il silenzio
per un esito. Alla prima corsa di una fonte nuova non c'è uno stato censito, e lo strumento lo dice invece di
segnalare come nuove tutte le voci.

Uso
---
    python tools/controlla-eventi-nuovi.py             rapporto completo
    python tools/controlla-eventi-nuovi.py --breve     poche righe, per l'hook SessionStart
    python tools/controlla-eventi-nuovi.py --segna     censimento fatto: tutte le fonti allo stato corrente
    python tools/controlla-eventi-nuovi.py --autotest  prove interne, senza rete
"""

import argparse
import collections
import datetime
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Tracciato, perché su una macchina nuova il controllo deve sapere fino a dove si è censito (2026-11-03).
STATO = os.path.join(RADICE, "pokedex-home-completo", "data", "controllo-eventi.json")
CLONE_PKHEX = os.path.join(RADICE, "_notes", "fonti", "cloni", "pkhex")
ARCHIVIO = "projectpokemon/EventsGallery"
LIBRERIA = "kwsch/PKHeX"
BASE_ARCHIVIO = "154d81b"  # ultimo commit dell'archivio prima della lettura integrale del 2026-10-05
BULBA_API = "https://bulbapedia.bulbagarden.net/w/api.php"
BULBA_INDICE = "List of event Pokémon distributions"
SEREBII = {"serebii-notizie": "https://www.serebii.net/index2.shtml",
           "serebii-doni-home": "https://www.serebii.net/pokemonhome/giftpokemon.shtml"}
# I titoli delle notizie si tengono solo per i giochi che portano esemplari collezionabili verso HOME.
GIOCHI_COLLEZIONE = re.compile(r"Scarlet|Violet|Legends: Z-A|Legends: Arceus|HOME|Sword|Shield|Brilliant Diamond|"
                               r"Shining Pearl|Let's Go|FireRed|LeafGreen|Pokémon Champions|Mystery Gift|Distribution", re.I)
UA = "retrogame-mod-pok-dev (controllo eventi, sola lettura)"
PAROLE_LIBRERIA = ("mgdb", "resources/byte", "encounter", "mysterygift", "wondercard")


def scarica(url, timeout=15):
    richiesta = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(richiesta, timeout=timeout) as risposta:
        return risposta.read().decode("utf-8", errors="replace")


def api(percorso, timeout=10):
    """Chiama l'API di GitHub: prima con `gh`, che è autenticato, poi senza credenziali."""
    try:
        uscita = subprocess.run(["gh", "api", percorso], capture_output=True, text=True, encoding="utf-8",
                                timeout=timeout)
        if uscita.returncode == 0 and uscita.stdout.strip():
            return json.loads(uscita.stdout)
    except (OSError, subprocess.TimeoutExpired, ValueError):
        pass
    return json.loads(scarica("https://api.github.com/" + percorso, timeout))


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


def titoli_notizie(testo):
    """Dai titoli delle notizie di Serebii, uno per giorno, le parti che riguardano i giochi della collezione."""
    righe = {}
    for t in re.findall(r"<h2[^>]*>(.*?)</h2>", testo, flags=re.S | re.I):
        t = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", t)).split())
        for parte in t.split(" + "):
            parte = parte.split(": ", 1)[1] if re.match(r"^[A-Z][a-z]+day: ", parte) else parte
            if GIOCHI_COLLEZIONE.search(parte):
                righe[hashlib.sha256(parte.encode("utf-8")).hexdigest()[:16]] = parte[:160]
    return righe


def righe_serebii(testo):
    """Le righe di tabella che descrivono un evento o un dono, ridotte a testo e a impronta breve."""
    testo = re.sub(r"<script.*?</script>", " ", testo, flags=re.S | re.I)
    righe = {}
    for r in re.findall(r"<tr[^>]*>(.*?)</tr>", testo, flags=re.S | re.I):
        t = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", r)).split())
        if 20 < len(t) < 600 and re.search(r"Available|Obtainable|Gift|Distribution|Mystery", t, re.I):
            righe[hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]] = t[:160]
    return righe


def pagine_bulbapedia(leggi=scarica):
    """Le pagine di distribuzioni collegate dall'indice, con il numero di revisione corrente."""
    q = urllib.parse.urlencode({"action": "query", "prop": "links", "titles": BULBA_INDICE, "pllimit": "500",
                                "format": "json"})
    dati = json.loads(leggi(BULBA_API + "?" + q))
    titoli = [BULBA_INDICE] + [l["title"] for p in dati["query"]["pages"].values() for l in p.get("links", [])
                               if "distribution" in l["title"].lower()]
    revisioni = {}
    for i in range(0, len(titoli), 50):
        q = urllib.parse.urlencode({"action": "query", "prop": "revisions", "rvprop": "ids|timestamp",
                                    "titles": "|".join(titoli[i:i + 50]), "format": "json"})
        for p in json.loads(leggi(BULBA_API + "?" + q))["query"]["pages"].values():
            if p.get("revisions"):
                revisioni[p["title"]] = [p["revisions"][0]["revid"], p["revisions"][0]["timestamp"]]
    return revisioni


def controlla(chiama=api, leggi=scarica):
    stato = leggi_stato()
    esito = {"archivio": None, "libreria": None, "bulbapedia": None, "serebii": {}, "errori": [], "corrente": {}}
    base = stato.get("archivio_censito_fino_a", BASE_ARCHIVIO)
    try:
        c = chiama("repos/%s/compare/%s...master" % (ARCHIVIO, base))
        testa = c["commits"][-1]["sha"] if c.get("commits") else stato.get("archivio_censito_fino_a")
        esito["archivio"] = {"base": base[:7], "commit": c.get("ahead_by", 0), "gruppi": nuovi_eventi(c)}
        esito["corrente"]["archivio_censito_fino_a"] = testa
    except Exception as e:  # rete, servizio o risposta inattesa: non verificabile, non zero eventi
        esito["errori"].append("EventsGallery: %s" % e.__class__.__name__)
    clone = commit_clone()
    if clone:
        try:
            rilascio = chiama("repos/%s/releases/latest" % LIBRERIA)["tag_name"]
            c = chiama("repos/%s/compare/%s...%s" % (LIBRERIA, clone, rilascio))
            esito["libreria"] = {"base": clone[:7], "rilascio": rilascio, "commit": c.get("ahead_by", 0), "file": file_libreria(c)}
        except Exception as e:
            esito["errori"].append("PKHeX: %s" % e.__class__.__name__)
    else:
        esito["errori"].append("PKHeX: clone locale assente in _notes/fonti/cloni/pkhex")
    try:
        ora = pagine_bulbapedia(leggi)
        prima = stato.get("bulbapedia")
        cambiate = None if prima is None else sorted(t for t, r in ora.items() if prima.get(t, [None])[0] != r[0])
        esito["bulbapedia"] = {"pagine": len(ora), "cambiate": cambiate, "revisioni": ora}
        esito["corrente"]["bulbapedia"] = ora
    except Exception as e:
        esito["errori"].append("Bulbapedia: %s" % e.__class__.__name__)
    for nome, url in SEREBII.items():
        try:
            ora = (titoli_notizie if nome == "serebii-notizie" else righe_serebii)(leggi(url))
            prima = stato.get(nome)
            nuove = None if prima is None else [t for k, t in ora.items() if k not in prima]
            esito["serebii"][nome] = {"righe": len(ora), "nuove": nuove}
            esito["corrente"][nome] = sorted(ora)
        except Exception as e:
            esito["errori"].append("%s: %s" % (nome, e.__class__.__name__))
    return esito


def stampa(esito, breve):
    print("=== Controllo eventi nuovi (tools/controlla-eventi-nuovi.py), cinque fonti ===")
    da_fare = False
    a = esito["archivio"]
    if a is None:
        print("EventsGallery: non verificabile adesso.")
    elif not a["gruppi"]:
        print("EventsGallery: nessun file nuovo dal commit censito %s." % a["base"])
    else:
        da_fare = True
        print("EventsGallery: %d file nuovi in %d commit dal commit censito %s." %
              (sum(len(v) for v in a["gruppi"].values()), a["commit"], a["base"]))
        for chiave, nomi in a["gruppi"].items():
            print("  %s: %d%s" % (chiave, len(nomi), "" if breve else " -> " + "; ".join(nomi[:8])))
    l = esito["libreria"]
    if l is None:
        print("PKHeX: non verificabile adesso.")
    elif not l["commit"]:
        print("PKHeX: il clone locale %s è all'ultima release, %s." % (l["base"], l["rilascio"]))
    else:
        da_fare = da_fare or bool(l["file"])
        print("PKHeX: il clone locale %s è indietro di %d commit rispetto alla release %s; %d file toccano incontri o doni; "
              "si aggiorna `tools/pkhex-versione.txt` e si lancia `tools/ripristina-ambiente.ps1`." %
              (l["base"], l["commit"], l["rilascio"], len(l["file"])))
        if not breve:
            for f in l["file"][:20]:
                print("  " + f)
    b = esito["bulbapedia"]
    if b is None:
        print("Bulbapedia: non verificabile adesso.")
    elif b["cambiate"] is None:
        da_fare = True
        print("Bulbapedia: %d liste di distribuzioni, prima lettura: nessuno stato censito da confrontare." % b["pagine"])
    elif not b["cambiate"]:
        print("Bulbapedia: nessuna delle %d liste di distribuzioni è cambiata." % b["pagine"])
    else:
        da_fare = True
        print("Bulbapedia: %d liste su %d hanno una revisione nuova." % (len(b["cambiate"]), b["pagine"]))
        for t in b["cambiate"][:5 if breve else 50]:
            print("  " + t)
    for nome, s in esito["serebii"].items():
        if s["nuove"] is None:
            da_fare = True
            print("%s: %d righe, prima lettura: nessuno stato censito da confrontare." % (nome, s["righe"]))
        elif not s["nuove"]:
            print("%s: nessuna riga nuova." % nome)
        else:
            da_fare = True
            print("%s: %d righe nuove." % (nome, len(s["nuove"])))
            for t in s["nuove"][:3 if breve else 30]:
                print("  " + t)
    for e in esito["errori"]:
        print("  (non verificabile: " + e + ")")
    if da_fare:
        print("Per l'agente: ricorda al proprietario queste novità a inizio sessione e registrale in "
              "`.claude/memory/pending.md`; a censimento fatto, `python tools/controlla-eventi-nuovi.py --segna`.")


def segna():
    esito = controlla()
    if esito["errori"]:
        print("Non segno: alcune fonti non sono verificabili adesso, e segnarle registrerebbe uno stato parziale.")
        for e in esito["errori"]:
            print("  " + e)
        return 1
    stato = leggi_stato()
    stato.update(esito["corrente"])
    stato["segnato_il"] = datetime.date.today().isoformat()
    scrivi_stato(stato)
    print("Censimento registrato per tutte le fonti, al %s." % stato["segnato_il"])
    return 0


def autotest():
    global STATO
    finto_confronto = {"ahead_by": 2, "commits": [{"sha": "a" * 40}],
                       "files": [{"filename": "Released/Gen 9/ZA/Wondercards/0104 ZA - Item.wa9", "status": "added"},
                                 {"filename": "Released/Gen 9/ZA/Wondercards/0105 ZA - Pkmn.wa9", "status": "modified"},
                                 {"filename": "Released/Gen 9/ZA/Wondercards/old.wa9", "status": "removed"},
                                 {"filename": "README.md", "status": "modified"}]}
    g = nuovi_eventi(finto_confronto)
    pagina = ("<table><tr><td>Games Obtainable With : Legends Z-A Available from : October 29th 2026</td></tr>"
              "<tr><td>Menu</td></tr><script>var x='<tr><td>Available from fake</td></tr>'</script></table>")
    casi = [(list(g) == ["Gen 9 ZA"], "raggruppa per generazione e gioco"),
            (len(g.get("Gen 9 ZA", [])) == 2, "conta aggiunti e modificati, non i rimossi né i file fuori da Released/"),
            (file_libreria({"files": [{"filename": "PKHeX.Core/Legality/Encounters/X.cs"},
                                      {"filename": "PKHeX.WinForms/Y.cs"}]}) == ["PKHeX.Core/Legality/Encounters/X.cs"],
             "filtra i file della libreria che toccano incontri o doni"),
            (len(righe_serebii(pagina)) == 1, "Serebii: tiene la riga di un evento, scarta il menu e gli script"),
            (list(titoli_notizie("<h2>Friday: Pokémon Scarlet & Violet - Tera Raid + Pokémon GO - Raid Day</h2>").values())
             == ["Pokémon Scarlet & Violet - Tera Raid"], "Serebii: dei titoli tiene i giochi della collezione, non GO")]

    def guasto(*_a, **_k):
        raise OSError("rete assente")
    vecchio, STATO = STATO, os.path.join(RADICE, "_notes", "tmp", "controllo-eventi-autotest.json")
    try:
        e = controlla(chiama=guasto, leggi=guasto)
        casi.append((e["archivio"] is None and e["bulbapedia"] is None and len(e["errori"]) >= 4,
                     "senza rete ogni fonte è non verificabile, non zero eventi"))
        scrivi_stato({"bulbapedia": {"Pagina A": [1, "t"]}, "serebii-notizie": [], "serebii-doni-home": []})

        def finta_lettura(url, timeout=15):
            if "api.php" in url and "prop=links" in url:
                return json.dumps({"query": {"pages": {"1": {"links": [{"title": "Pagina A distributions"}]}}}})
            if "api.php" in url:
                return json.dumps({"query": {"pages": {"1": {"title": "Pagina A", "revisions": [{"revid": 2, "timestamp": "t"}]}}}})
            return pagina
        e = controlla(chiama=guasto, leggi=finta_lettura)
        casi.append((e["bulbapedia"]["cambiate"] == ["Pagina A"], "Bulbapedia: una revisione nuova è una pagina cambiata"))
        casi.append((len(e["serebii"]["serebii-doni-home"]["nuove"]) == 1, "Serebii: una riga mai vista è nuova"))
    finally:
        try:
            os.remove(STATO)
        except OSError:
            pass
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
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    if a.autotest:
        return autotest()
    if a.segna:
        return segna()
    stampa(controlla(), a.breve)
    return 0


if __name__ == "__main__":
    sys.exit(main())
