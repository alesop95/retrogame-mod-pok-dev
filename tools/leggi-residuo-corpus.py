#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legge i collegamenti del corpus della collezione che il censimento aveva soltanto catalogato.

Perché esiste
-------------
Il censimento del corpus, `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md`, ha seguito i collegamenti del post di
raccolta per tre livelli e ne ha scaricati 670; altri 2582 indirizzi unici sono rimasti catalogati, non raggiunti o
falliti, e nessuno li ha letti. Il proprietario chiedeva da settimane che la lista completa si facesse dopo aver letto
tutto, e il 2026-10-01 il conto è venuto fuori. Questo strumento li legge per tipo, con le vie del progetto, e scrive
ciascun testo su disco, perché poi `tools/estrai-affermazioni-ollama.py --chat` ne estragga ciò che serve senza
consumare token dell'agente.

Che cosa fa
-----------
Classifica ogni indirizzo di `_notes/fonti/da-leggere-corpus.json`. Le discussioni Reddit si leggono da Arctic Shift con
le funzioni di `tools/fetch-reddit.py`, post e albero dei commenti. I fogli Google si esportano in xlsx e se ne scrivono
tutte le schede come testo; i documenti Google si esportano in testo. Le pagine di Bulbapedia si leggono dalla copia più
recente della Wayback Machine, perché la pagina viva risponde con una verifica anti-bot. Le altre pagine si leggono
dirette, e se falliscono dalla Wayback Machine. Le immagini si scaricano in `immagini/` per un modello di visione, e i
video si mettono in `video.txt` per la catena dei sottotitoli. WolframAlpha, che contiene calcoli e non fonti, gli inviti
di Discord e i post di Twitter e X, che senza account non si leggono, si registrano con il motivo e non si leggono.
L'esito di ogni indirizzo va in `esiti.json`, e un indirizzo già letto non si rilegge.

Uso
---
    python tools/leggi-residuo-corpus.py
    python tools/leggi-residuo-corpus.py --solo reddit
"""

import argparse
import collections
import concurrent.futures
import gzip
import hashlib
import importlib.util
import io
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ELENCO = os.path.join(RADICE, "_notes", "fonti", "da-leggere-corpus.json")
USCITA = os.path.join(RADICE, "_notes", "fonti", "corpus-residuo")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) retrogame-mod-pok-dev lettore del corpus"
IMMAGINI = (".png", ".jpg", ".jpeg", ".gif", ".webp")

spec = importlib.util.spec_from_file_location("fetch_reddit", os.path.join(RADICE, "tools", "fetch-reddit.py"))
fr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fr)


def chiave(url):
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def get(url, binario=False):
    # Un indirizzo con caratteri non ASCII, come Pokémon nei titoli di Bulbapedia, va codificato prima della richiesta.
    url = urllib.parse.quote(url, safe=":/?&=%#@+!$,;~*'()[]")
    r = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    # La Wayback Machine risponde 429 alle letture in parallelo: si attende e si riprova, con pause crescenti.
    for tentativo in range(4):
        try:
            with urllib.request.urlopen(r, timeout=40, context=fr.contesto_tls()) as risposta:
                corpo = risposta.read(30_000_000)
                intestazioni = dict(risposta.headers)
                # Alcuni server, e la Wayback Machine con la forma id_, mandano gzip anche a chi chiede identity:
                # il 2026-10-01 cento testi «letti» erano byte compressi decodificati come testo.
                if corpo[:2] == b"\x1f\x8b":
                    corpo = gzip.decompress(corpo)
                    intestazioni = {k: v for k, v in intestazioni.items() if k.lower() != "content-encoding"}
                return corpo if binario else (corpo, intestazioni)
        except urllib.error.HTTPError as e:
            if e.code != 429 or tentativo == 3:
                raise
            time.sleep(15 * (tentativo + 1))


def wayback(url):
    """La copia più recente nella Wayback Machine, con la forma id_ che restituisce il documento originale."""
    # L'interfaccia «available» risponde vuota anche per pagine con decine di copie, e quando l'archivio è
    # temporaneamente fuori linea restituisce una pagina HTML: il 2026-10-05 diciannove pagine di Bulbapedia
    # risultavano «senza copia» per questo. Si chiede quindi l'elenco CDX delle copie valide, riprovando.
    q = urllib.parse.quote(url.split("#")[0], safe="")
    ts = None
    for tentativo in range(4):
        try:
            righe = get("https://web.archive.org/cdx/search/cdx?url=%s&filter=statuscode:200&fl=timestamp&limit=-1" % q)[0].decode("utf-8", "replace").split()
        except (urllib.error.URLError, OSError):
            righe = []
        if righe and righe[-1].isdigit():
            ts = righe[-1]
            break
        if righe == [] and tentativo >= 1:
            # Una risposta CDX vuota, ripetuta, vuol dire davvero nessuna copia.
            break
        time.sleep(20 * (tentativo + 1))
    if not ts:
        dati = json.loads(get("https://archive.org/wayback/available?url=" + q)[0].decode("utf-8"))
        vicina = (dati.get("archived_snapshots") or {}).get("closest") or {}
        if not vicina.get("available"):
            return None
        ts = vicina["timestamp"]
    copia = get("https://web.archive.org/web/%sid_/%s" % (ts, url.split("#")[0]))
    if b"Temporarily Offline" in copia[0][:3000]:
        raise OSError("Internet Archive temporaneamente fuori linea")
    return copia


def tipo_di(url):
    host = re.sub(r"^https?://(www\.|m\.|np\.|old\.)?", "", url).split("/")[0].lower()
    percorso = urllib.parse.urlsplit(url).path.lower()
    if re.fullmatch(r"[0-9.]+(:[0-9]+)?", host) or host == "localhost":
        return "salta", "indirizzo numerico o locale, non una pagina di contenuto"
    if "wolframalpha.com" in host:
        return "salta", "calcolo di WolframAlpha, non una fonte"
    if host in ("twitter.com", "x.com", "mobile.twitter.com"):
        return "salta", "Twitter e X non si leggono senza account"
    if host in ("discord.gg", "discord.com") and "/invite" in url or host == "discord.gg":
        return "salta", "invito a un server Discord, non un contenuto"
    if host in ("mega.nz",):
        return "salta", "archivio cifrato di Mega, si scarica a mano"
    if percorso.endswith(IMMAGINI) or host in ("preview.redd.it", "i.redd.it", "i.imgur.com") or "bp.blogspot.com" in host:
        return "immagine", ""
    if host in ("youtube.com", "youtu.be", "m.youtube.com"):
        return "video", ""
    if host.endswith("reddit.com") or host == "redd.it":
        return "reddit", ""
    if host == "docs.google.com":
        return "google", ""
    if host == "drive.google.com":
        return "drive", ""
    if "bulbapedia" in host:
        return "bulbapedia", ""
    if host in ("imgur.com",):
        return "imgur", ""
    return "web", ""


def leggi_reddit(url, trasporto):
    if "message/compose" in url or "RemindMe" in url:
        return None, "SALTA:collegamento del bot RemindMe, un promemoria e non un contenuto"
    m = re.search(r"/comments/([a-z0-9]+)", url) or re.search(r"/gallery/([a-z0-9]+)", url)
    if not m and "/s/" in url:
        percorso = urllib.parse.urlsplit(url).path
        mappa = fr.risolvi_brevi(trasporto, [percorso])
        nuovo = mappa.get(percorso)
        m = re.search(r"/comments/([a-z0-9]+)", nuovo or "")
    if not m and "/wiki" in url:
        return leggi_web(url.split("#")[0], prima_wayback=True)
    if not m:
        return None, "SALTA:pagina di profilo o di sottocomunità, un elenco e non un contenuto"
    pid = m.group(1)
    post = fr.post_per_id(trasporto, [pid]).get(pid)
    if not post:
        return None, "post non presente nell'archivio"
    righe = ["# " + (post.get("title") or ""), "", "Autore: %s. Sottocomunità: %s." % (post.get("author"), post.get("subreddit")),
             "", post.get("selftext") or "", "", "## Commenti", ""]
    for prof, genere, dato in fr.percorri_albero(fr.albero_commenti(trasporto, pid)):
        if genere == "t1" and dato.get("body"):
            righe.append("%s- %s: %s" % ("  " * prof, dato.get("author"), dato["body"].replace("\n", " ")))
    return "\n".join(righe), ""


def foglio_a_testo(dati):
    import openpyxl
    libro = openpyxl.load_workbook(io.BytesIO(dati), read_only=True, data_only=True)
    righe = []
    for scheda in libro.worksheets:
        righe.append("## Scheda: " + scheda.title)
        for riga in scheda.iter_rows(values_only=True):
            celle = [str(c) for c in riga if c not in (None, "")]
            if celle:
                righe.append(" | ".join(celle))
    return "\n".join(righe)


def leggi_drive(url):
    """Un file caricato su Drive, compresi i fogli Excel che Google mostra come fogli ma non esporta come tali."""
    m = re.search(r"/(?:file|spreadsheets|document)/d/([A-Za-z0-9_-]{20,})", url) or re.search(r"[?&]id=([A-Za-z0-9_-]{20,})", url)
    if not m:
        c = re.search(r"/folders/([A-Za-z0-9_-]{20,})", url)
        if c:
            # Una cartella pubblica si elenca dalla vista incorporata, che è HTML semplice con i nomi dei file.
            return leggi_web("https://drive.google.com/embeddedfolderview?id=" + c.group(1) + "#list")
        return None, "indirizzo Drive senza identificativo di file"
    dati = get("https://drive.usercontent.google.com/download?export=download&confirm=t&id=" + m.group(1), binario=True)
    if dati.startswith(b"PK"):
        try:
            return foglio_a_testo(dati), ""
        except Exception:
            return None, "archivio compresso su Drive, non un foglio: si apre a mano"
    if dati.startswith(b"%PDF"):
        io.open(os.path.join(USCITA, "immagini", chiave(url) + ".pdf"), "wb").write(dati)
        return None, "PDF scaricato in immagini/, da leggere"
    testo = dati.decode("utf-8", errors="replace")
    if testo.lstrip().startswith("<"):
        return None, ("file su Drive che chiede l accesso a Google, non pubblico" if "Sign-in" in testo else "file su Drive non scaricabile senza browser")
    return testo, ""


def leggi_google(url):
    if "/pub" in url or "/d/e/" in url:
        return leggi_web(url)
    m = re.search(r"/spreadsheets/(?:u/[0-9]+/)?d/([A-Za-z0-9_-]+)", url)
    if m:
        try:
            dati = get("https://docs.google.com/spreadsheets/d/%s/export?format=xlsx" % m.group(1), binario=True)
        except Exception:
            dati = b""
        if not dati.startswith(b"PK"):
            return leggi_drive(url)
        return foglio_a_testo(dati), ""
    m = re.search(r"/document/d/([A-Za-z0-9_-]+)", url)
    if m:
        dati = get("https://docs.google.com/document/d/%s/export?format=txt" % m.group(1), binario=True)
        testo = dati.decode("utf-8", errors="replace")
        return (testo, "") if not testo.lstrip().startswith("<") else (None, "documento non pubblico")
    return None, "indirizzo Google non riconosciuto"


def leggi_imgur(url):
    """Un album o un post di Imgur dall'interfaccia che usa la pagina stessa, perché la pagina è uno scheletro."""
    m = (re.search(r"imgur\.com/(?:a|gallery)/(?:[^/#?]*-)?([A-Za-z0-9]{5,8})(?:[#?/]|$)", url)
         or re.search(r"imgur\.com/([A-Za-z0-9]{5,8})(?:[#?/]|$)", url))
    if not m:
        return None, "indirizzo Imgur non riconosciuto"
    dati = None
    for genere in ("albums", "media", "posts"):
        try:
            dati = json.loads(get("https://api.imgur.com/post/v1/%s/%s?client_id=546c25a59c58ad7&include=media" % (genere, m.group(1)))[0].decode("utf-8"))
            break
        except Exception:
            continue
    if not dati:
        return None, "Imgur non restituisce il post, forse rimosso"
    righe = ["# " + (dati.get("title") or ""), "", dati.get("description") or ""]
    for i, media in enumerate(dati.get("media") or []):
        meta = media.get("metadata") or {}
        righe += ["## Immagine %d: %s" % (i + 1, meta.get("title") or ""), meta.get("description") or ""]
        try:
            nome = "%s-%02d%s" % (chiave(url), i + 1, os.path.splitext(media["url"])[1] or ".jpg")
            io.open(os.path.join(USCITA, "immagini", nome), "wb").write(get(media["url"], binario=True))
            righe.append("(immagine in immagini/%s)" % nome)
        except Exception as e:
            righe.append("(immagine non scaricata: %s)" % e)
    return "\n".join(righe), ""


BROWSER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.9",
           "Accept-Encoding": "gzip"}


def come_browser(url):
    """La pagina chiesta come la chiede un browser. Il 2026-10-01 Glitch City e GameBrew rispondevano 403 al lettore e
    200 a queste intestazioni; un collegamento a una revisione, con «?oldid=», si riporta alla pagina corrente."""
    m = re.match(r"(https?://[^/]+)/(?:w/)?index\.php\?title=([^&]+)", url)
    if m:
        url = m.group(1) + "/wiki/" + m.group(2)
    url = re.sub(r"[?&]oldid=\d+", "", url)
    r = urllib.request.Request(urllib.parse.quote(url, safe=":/?&=%#@+!$,;~*'()[]"), headers=BROWSER)
    with urllib.request.urlopen(r, timeout=40, context=fr.contesto_tls()) as risposta:
        corpo = risposta.read(30_000_000)
        if corpo[:2] == b"\x1f\x8b":
            corpo = gzip.decompress(corpo)
        return corpo, {k: v for k, v in dict(risposta.headers).items() if k.lower() != "content-encoding"}


def leggi_web(url, prima_wayback=False):
    if not prima_wayback:
        try:
            corpo, intest = come_browser(url)
            titolo, testo, motivo = fr.html_a_testo(corpo, {k.lower(): v for k, v in intest.items()})
            if not motivo:
                return "# %s\n\n%s" % (titolo, testo), ""
        except Exception:
            pass
    if prima_wayback:
        corpo, intest = wayback(url) or (None, None)
    else:
        try:
            corpo, intest = get(url)
        except Exception as e:
            copia = wayback(url)
            if not copia:
                return None, "%s, e nessuna copia nella Wayback Machine" % e
            corpo, intest = copia
    if corpo is None and prima_wayback:
        return None, "nessuna copia nella Wayback Machine"
    titolo, testo, motivo = fr.html_a_testo(corpo, {k.lower(): v for k, v in intest.items()})
    if motivo and not prima_wayback:
        copia = wayback(url)
        if copia:
            titolo, testo, motivo = fr.html_a_testo(copia[0], {k.lower(): v for k, v in copia[1].items()})
    if motivo:
        return None, motivo
    return "# %s\n\n%s" % (titolo, testo), ""


def leggi_uno(url, trasporto):
    """L'esito di un indirizzo, letto secondo il suo tipo; il testo letto va su disco."""
    tipo, motivo = tipo_di(url)
    k = chiave(url)
    try:
        if tipo == "salta":
            return {"esito": "saltato", "motivo": motivo}
        if tipo == "video":
            m = re.search(r"(?:v=|youtu\.be/|shorts/|embed/|live/)([A-Za-z0-9_-]{11})", url.replace("\\", ""))
            if not m:
                return {"esito": "saltato", "tipo": tipo, "motivo": "pagina di un canale, non un video"}
            return {"esito": "video", "id": m.group(1)}
        if tipo == "immagine":
            pulito = url.replace("\\", "")
            try:
                dati = get(pulito, binario=True)
            except urllib.error.HTTPError:
                # Un'anteprima di Reddit scade; l'originale resta spesso su i.redd.it con lo stesso nome.
                if "preview.redd.it" not in pulito:
                    raise
                dati = get("https://i.redd.it/" + urllib.parse.urlsplit(pulito).path.lstrip("/"), binario=True)
            est = os.path.splitext(urllib.parse.urlsplit(url).path)[1].lower() or ".jpg"
            io.open(os.path.join(USCITA, "immagini", k + est), "wb").write(dati)
            return {"esito": "immagine", "file": k + est}
        # Il censimento ha preso alcuni indirizzi dal Markdown di Reddit, con i trattini bassi protetti.
        pulito = url.replace("\\", "")
        # Il censimento ha chiuso alcuni indirizzi alla prima parentesi chiusa, come in «(Generation_I»: si richiude.
        if pulito.count("(") > pulito.count(")"):
            pulito += ")"
        if tipo == "reddit":
            testo, motivo = leggi_reddit(pulito, trasporto)
        elif tipo == "google":
            testo, motivo = leggi_google(pulito)
        elif tipo == "drive":
            testo, motivo = leggi_drive(pulito)
        elif tipo == "imgur":
            testo, motivo = leggi_imgur(pulito)
        elif tipo == "bulbapedia":
            testo, motivo = leggi_web(pulito, prima_wayback=True)
        else:
            testo, motivo = leggi_web(pulito)
        if testo:
            io.open(os.path.join(USCITA, "testi", k + ".md"), "w", encoding="utf-8").write("<!-- %s -->\n%s\n" % (url, testo))
            return {"esito": "letto", "tipo": tipo, "file": k + ".md"}
        if motivo.startswith("SALTA:"):
            return {"esito": "saltato", "tipo": tipo, "motivo": motivo[6:]}
        return {"esito": "non letto", "tipo": tipo, "motivo": motivo}
    except Exception as e:
        return {"esito": "non letto", "tipo": tipo, "motivo": "%s: %s" % (type(e).__name__, str(e)[:200])}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--solo", help="limita a un tipo: reddit, google, drive, bulbapedia, web, imgur, immagine, video")
    ap.add_argument("--thread", type=int, default=8, help="letture parallele fuori da Reddit")
    a = ap.parse_args()
    for sotto in ("testi", "immagini"):
        os.makedirs(os.path.join(USCITA, sotto), exist_ok=True)
    percorso_esiti = os.path.join(USCITA, "esiti.json")
    esiti = json.load(io.open(percorso_esiti, encoding="utf-8")) if os.path.exists(percorso_esiti) else {}
    trasporto = fr.TrasportoHTTP()
    da_fare = [u for u in json.load(io.open(ELENCO, encoding="utf-8"))
               if not (u in esiti and esiti[u]["esito"] in ("letto", "immagine", "video", "saltato"))
               and (not a.solo or tipo_di(u)[0] == a.solo)]
    blocco = threading.Lock()

    def salva():
        with blocco:
            json.dump(esiti, io.open(percorso_esiti, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
            ids = sorted(set(v["id"] for v in esiti.values() if v.get("esito") == "video" and v.get("id")))
            io.open(os.path.join(USCITA, "video.txt"), "w", encoding="utf-8").write("\n".join(ids) + "\n")

    fatti = [0]

    def registra(url, esito):
        with blocco:
            # Una riprova fallita non cancella il motivo già scritto, che è spesso una diagnosi a mano più
            # precisa del codice d'errore: il 2026-10-05 una riprova aveva ridotto settanta motivi a «404».
            prima = esiti.get(url, {})
            if esito.get("esito") == "non letto" and prima.get("esito") == "non letto" and prima.get("motivo"):
                esito = dict(prima, riprova="%s il %s" % (esito.get("motivo", ""), time.strftime("%Y-%m-%d")))
            esiti[url] = esito
            fatti[0] += 1
            n = fatti[0]
        if n % 25 == 0:
            salva()
            print(n, len(da_fare), flush=True)

    # Arctic Shift ha un limite di frequenza e TrasportoHTTP lo rispetta: Reddit va in un solo filo, il resto in parallelo.
    reddit = [u for u in da_fare if tipo_di(u)[0] == "reddit"]
    altri = [u for u in da_fare if tipo_di(u)[0] != "reddit"]

    def filo_reddit():
        for u in reddit:
            registra(u, leggi_uno(u, trasporto))

    filo = threading.Thread(target=filo_reddit)
    filo.start()
    with concurrent.futures.ThreadPoolExecutor(a.thread) as pool:
        for u, esito in zip(altri, pool.map(lambda x: leggi_uno(x, None), altri)):
            registra(u, esito)
    filo.join()
    salva()
    conto = collections.Counter(v["esito"] for v in esiti.values())
    print("FINE", dict(conto), flush=True)


if __name__ == "__main__":
    main()
