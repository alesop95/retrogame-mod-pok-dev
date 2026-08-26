#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legge un thread o un listato di Reddit tramite l'API ufficiale.

Perché esiste
--------------
Reddit non è recuperabile con gli strumenti di sessione, e non per un difetto di
configurazione del progetto: il dominio blocca il crawler del modello, e l'accesso
anonimo programmatico è chiuso anche a curl, all'endpoint JSON di old.reddit.com, ai
frontend alternativi e ai proxy di lettura. La diagnosi completa, con l'esito di ogni via
tentata, sta in .claude/rules/web-sources-not-fetchable.md.

L'API ufficiale invece funziona, con un flusso a sole credenziali applicative che non
richiede un account collegato e basta per leggere contenuto pubblico.

Come si allestisce, una volta sola
----------------------------------
1. Su https://www.reddit.com/prefs/apps si crea una applicazione di tipo "script".
   Il campo redirect uri può essere http://localhost:8080, non viene usato.
2. Si copiano l'identificativo, che sta sotto il nome dell'applicazione, e il segreto.
3. Si scrivono in .env nella radice del progetto, che il .gitignore esclude:

       REDDIT_CLIENT_ID=...
       REDDIT_CLIENT_SECRET=...
       REDDIT_USER_AGENT=windows:nome-progetto:v1 (by /u/tuo_utente)

   Lo user agent va compilato: Reddit rifiuta o limita le richieste con user agent
   generici, e chiede quel formato nella propria documentazione.

Uso
---
    python tools/fetch-reddit.py https://www.reddit.com/r/Gameboy/comments/xxxxxx/titolo/
    python tools/fetch-reddit.py r/pokemonrng --top --limit 10
    python tools/fetch-reddit.py https://... --comments 30 --json out.json

Stato di collaudo
-----------------
Il flusso è scritto sulla documentazione dell'API e non è stato eseguito contro il
servizio, perché in questa sessione non esistono credenziali. Il percorso senza
credenziali è invece provato e riferisce le istruzioni. Alla prima esecuzione riuscita
va aggiornata questa nota e va aggiornata la voce di Reddit nel registro delle fonti.
"""

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
API_BASE = "https://oauth.reddit.com"


def load_env(path=".env"):
    """Carica le variabili da .env senza dipendenze, ignorando commenti e righe vuote."""
    values = {}
    if not os.path.exists(path):
        return values
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def credentials():
    env = load_env()
    def get(name):
        return os.environ.get(name) or env.get(name)
    cid, secret, agent = (get("REDDIT_CLIENT_ID"), get("REDDIT_CLIENT_SECRET"),
                          get("REDDIT_USER_AGENT"))
    if not (cid and secret and agent):
        print(__doc__.split("Come si allestisce")[1].split("Uso\n---")[0].strip(),
              file=sys.stderr)
        print("\nMancano: %s" % ", ".join(
            n for n, v in (("REDDIT_CLIENT_ID", cid), ("REDDIT_CLIENT_SECRET", secret),
                           ("REDDIT_USER_AGENT", agent)) if not v), file=sys.stderr)
        sys.exit(2)
    return cid, secret, agent


def get_token(cid, secret, agent):
    body = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode()
    auth = base64.b64encode(("%s:%s" % (cid, secret)).encode()).decode()
    req = urllib.request.Request(TOKEN_URL, data=body, method="POST", headers={
        "Authorization": "Basic " + auth,
        "User-Agent": agent,
        "Content-Type": "application/x-www-form-urlencoded",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if "access_token" not in payload:
        raise RuntimeError("risposta senza token: %r" % payload)
    return payload["access_token"]


def api_get(path, token, agent, params=None):
    url = API_BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Authorization": "Bearer " + token,
        "User-Agent": agent,
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def normalize(target):
    """Da un URL o da una forma abbreviata al percorso API, più il tipo di richiesta."""
    target = target.strip()
    if target.startswith("http"):
        path = urllib.parse.urlparse(target).path
    elif target.startswith("r/") or target.startswith("/r/"):
        path = "/" + target.lstrip("/")
    else:
        raise SystemExit("non riconosco %r: passa un URL o una forma r/nome" % target)
    path = re.sub(r"/+$", "", path)
    if "/comments/" in path:
        return path, "thread"
    return path, "listing"


def render_thread(payload, max_comments):
    post = payload[0]["data"]["children"][0]["data"]
    print("# %s" % post.get("title", "senza titolo"))
    print("autore: %s | punteggio: %s | commenti: %s"
          % (post.get("author"), post.get("score"), post.get("num_comments")))
    print("url: https://www.reddit.com%s\n" % post.get("permalink", ""))
    body = (post.get("selftext") or "").strip()
    if body:
        print(body)
        print()
    print("## commenti (primi %d per punteggio)\n" % max_comments)
    shown = 0
    for child in payload[1]["data"]["children"]:
        if child.get("kind") != "t1" or shown >= max_comments:
            continue
        c = child["data"]
        print("- [%s, %s punti] %s" % (c.get("author"), c.get("score"),
                                       (c.get("body") or "").strip().replace("\n", " ")))
        shown += 1


def render_listing(payload):
    for child in payload["data"]["children"]:
        d = child["data"]
        print("- [%s punti, %s commenti] %s"
              % (d.get("score"), d.get("num_comments"), d.get("title", "")))
        print("  https://www.reddit.com%s" % d.get("permalink", ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("target", help="URL di un thread, oppure r/nome per un listato")
    ap.add_argument("--comments", type=int, default=20, help="quanti commenti mostrare")
    ap.add_argument("--limit", type=int, default=25, help="quante voci nel listato")
    ap.add_argument("--top", action="store_true", help="ordina il listato per punteggio")
    ap.add_argument("--json", help="salva la risposta grezza in questo file")
    args = ap.parse_args()

    cid, secret, agent = credentials()
    path, kind = normalize(args.target)

    try:
        token = get_token(cid, secret, agent)
        if kind == "thread":
            payload = api_get(path, token, agent, {"limit": args.comments, "raw_json": 1})
        else:
            suffix = "/top" if args.top else ""
            payload = api_get(path + suffix, token, agent,
                              {"limit": args.limit, "t": "year", "raw_json": 1})
    except urllib.error.HTTPError as exc:
        print("errore HTTP %s da Reddit: %s" % (exc.code, exc.reason), file=sys.stderr)
        print("un 401 indica credenziali sbagliate, un 429 il limite di frequenza",
              file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print("errore di rete: %s" % exc.reason, file=sys.stderr)
        return 1

    if args.json:
        with open(args.json, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
        print("risposta grezza salvata in %s" % args.json, file=sys.stderr)

    if kind == "thread":
        render_thread(payload, args.comments)
    else:
        render_listing(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
