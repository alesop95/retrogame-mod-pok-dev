# -*- coding: utf-8 -*-
"""Verifica che ogni collegamento scritto nei documenti del progetto sia classificato.

Perché esiste
-------------

Il 2026-10-06 il proprietario ha osservato che il progetto dichiarava lette tutte le fonti mentre i collegamenti scritti dentro i suoi stessi documenti, cioè handoff, note, consegne, decisioni e studi, non erano mai stati confrontati con il registro delle fonti, e i collegamenti brevi di condivisione di Reddit, nella forma `/r/<sub>/s/<codice>`, non erano mai stati risolti. Il registro sapeva che cosa aveva letto, ma nessuno sapeva che cosa il progetto citava: un collegamento incollato in un handoff restava fuori da entrambi i conti senza produrre alcun errore.

Che cosa fa
-----------

Estrae ogni indirizzo dai file tracciati e dal materiale scritto dal proprietario o dal progetto sotto `_notes/`, escludendo i testi di terzi scaricati sotto `_notes/fonti/` (salvo le consegne del proprietario in `_notes/fonti/consegne/`, nei soli `.md`, `.txt` e `.url` fuori dalle cartelle di trascrizioni), i lotti, i salvataggi, i cloni, l'output compilato, i modelli del template e le guide copiate intere dal template. Normalizza ogni indirizzo: toglie gli escape con la barra rovescia, la punteggiatura finale, il punto e virgola dei CSV, i parametri di tracciamento, i prefissi `www.`, `old.`, `np.` e `m.`, il frammento, e abbassa l'host. Riduce un post di Reddit al suo identificativo e un video di YouTube al suo, così che due forme dello stesso contenuto contino come una. Risolve i collegamenti brevi di Reddit seguendo il reindirizzamento, con l'archivio Arctic Shift come seconda via, e tiene i risultati in `_notes/fonti/link-brevi.json` per non chiederli due volte.

Poi confronta con le fonti conosciute: `SOURCES.md`, `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md`, gli esiti e i dimenticati del residuo del corpus, la lista di lettura del corpus, e l'elenco `_notes/fonti/link-non-fonti.json` degli indirizzi che non sono fonti, ciascuno con il proprio motivo (endpoint di strumenti, pagine di scaricamento di programmi, il repository stesso, stringhe d'esempio). Un indirizzo che non sta in nessuno di questi è non classificato.

Uso
---

    python tools/verifica-link-progetto.py                 riepilogo per host
    python tools/verifica-link-progetto.py --check         esce con 1 se c'è un indirizzo non classificato
    python tools/verifica-link-progetto.py --json FILE     scrive i non classificati con i file che li citano
    python tools/verifica-link-progetto.py --senza-rete    non risolve i collegamenti brevi nuovi
"""

import argparse
import collections
import io
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_BREVI = "_notes/fonti/link-brevi.json"
NON_FONTI = "_notes/fonti/link-non-fonti.json"
REGISTRI_TESTO = ["SOURCES.md", "pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md"]
REGISTRI_JSON = [
    "_notes/fonti/corpus-residuo/esiti.json",
    "_notes/fonti/corpus-residuo/dimenticati.json",
    "_notes/fonti/da-leggere-corpus.json",
]
ESCLUSI_TRACCIATI = (".claude/templates/", "docs/separazione-ambienti/", "docs/anti-slop/")
ESTENSIONI = (".md", ".txt", ".url", ".py", ".ps1", ".sh", ".json", ".tex", ".bib", ".csv",
              ".html", ".cs", ".yml", ".yaml", ".toml", ".js", ".cfg", ".ini")
# Sotto _notes/ si salta ciò che non è scritto dal proprietario o dal progetto.
NOTES_SALTATE = {"fonti", "lotti", "salvataggi", "cloni", "media", "bin", "obj", "tmp"}
CONSEGNE_SALTATE = {"testo", "estratti", "sub"}
TRACCIAMENTO = {"si", "share_id", "ref", "ref_source", "ref_src", "feature", "fbclid", "gclid",
                "igshid", "context", "rdt", "s", "t", "utm_name", "pp", "ab_channel", "is",
                "dl", "e", "usp", "ouid", "rtpof", "sd"}
# s e t sono parametri di tracciamento solo su questi host; altrove possono identificare la pagina.
TRACCIAMENTO_SOLO = {"s": ("twitter.com", "x.com"), "t": ("twitter.com", "x.com", "youtube.com", "youtu.be"),
                     "pp": ("youtube.com",), "ab_channel": ("youtube.com",), "context": ("reddit.com",),
                     "is": ("youtu.be",), "dl": ("dropbox.com",), "e": ("dropbox.com",),
                     "usp": ("google.com",), "ouid": ("google.com",), "rtpof": ("google.com",),
                     "sd": ("google.com",)}
PREFISSI_HOST = ("www.", "old.", "np.", "new.", "m.")

RE_URL = re.compile(r"https?://(?:\\[_*()\[\]#~.\-]|[^\s<>\"'`|;\]\}\\])+")
RE_BREVE = re.compile(r"^https?://(?:[a-z0-9.-]*\.)?reddit\.com/(r|u|user)/([^/]+)/s/([A-Za-z0-9]+)", re.I)
RE_POST = re.compile(r"/comments/([a-z0-9]{3,10})(?:/|$)", re.I)
RE_REDD_IT = re.compile(r"^https?://(?:www\.)?redd\.it/([a-z0-9]{3,10})/?$", re.I)
RE_YT = re.compile(r"(?:youtube\.com/(?:watch\?(?:.*&)?v=|shorts/|embed/|live/)|youtu\.be/)([A-Za-z0-9_-]{11})")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"


def pulisci(url):
    url = url.replace("\\", "").split("&quot")[0]
    while True:
        prima = url
        url = url.rstrip(".,;:!?*_'\">]}(")
        # Una parentesi chiusa finale appartiene all'indirizzo solo se ne apre una (Wikipedia).
        if url.endswith(")") and url.count(")") > url.count("("):
            url = url[:-1]
        if url == prima:
            return url


def host_breve(host):
    host = host.lower().split("@")[-1].split(":")[0]
    for p in PREFISSI_HOST:
        if host.startswith(p) and host.count(".") >= 2:
            host = host[len(p):]
    return host


def chiave(url):
    """La chiave di confronto: post di Reddit e video di YouTube per identificativo, il resto normalizzato."""
    url = pulisci(url)
    m = RE_REDD_IT.match(url)
    if m:
        return "reddit:" + m.group(1).lower()
    m = RE_YT.search(url)
    if m:
        return "youtube:" + m.group(1)
    try:
        p = urllib.parse.urlsplit(url)
    except ValueError:
        return None
    host = host_breve(p.netloc)
    if not host or "." not in host:
        return None
    percorso = urllib.parse.unquote(p.path)
    if host.endswith("reddit.com"):
        m = RE_POST.search(percorso)
        if m:
            return "reddit:" + m.group(1).lower()
        percorso = percorso.lower()
    tenuti = []
    for k, v in urllib.parse.parse_qsl(p.query, keep_blank_values=True):
        kl = k.lower()
        if kl.startswith("utm_"):
            continue
        if kl in TRACCIAMENTO:
            solo = TRACCIAMENTO_SOLO.get(kl)
            if solo is None or any(host.endswith(h) for h in solo):
                continue
        tenuti.append((k, v))
    percorso = percorso.rstrip("/")
    if host == "github.com" and percorso.endswith(".git"):
        percorso = percorso[:-4]
    q = urllib.parse.urlencode(tenuti)
    return host + percorso + ("?" + q if q else "")


def estrai(testo):
    for u in RE_URL.findall(testo):
        yield pulisci(u)


def leggi(percorso):
    try:
        with io.open(os.path.join(RADICE, percorso), "rb") as f:
            dati = f.read()
    except OSError:
        return ""
    try:
        return dati.decode("utf-8")
    except UnicodeDecodeError:
        # I file .url e le note salvate da Windows sono spesso in cp1252.
        return dati.decode("cp1252", errors="replace")


def file_da_scandire():
    out = subprocess.run(["git", "ls-files"], cwd=RADICE, capture_output=True, text=True,
                         encoding="utf-8").stdout.split("\n")
    registri = set(REGISTRI_TESTO)
    files = [f for f in out if f and f.endswith(ESTENSIONI) and f not in registri
             and not f.startswith(ESCLUSI_TRACCIATI) and not f.startswith("_notes/")]
    base = os.path.join(RADICE, "_notes")
    for radice, cartelle, nomi in os.walk(base):
        rel = os.path.relpath(radice, RADICE).replace("\\", "/")
        if rel == "_notes":
            cartelle[:] = [c for c in cartelle if c not in NOTES_SALTATE]
        else:
            cartelle[:] = [c for c in cartelle if c not in {"bin", "obj", "cloni"}]
        for n in nomi:
            if n.endswith(ESTENSIONI) and not n.endswith(".vtt"):
                files.append(rel + "/" + n)
    cons = os.path.join(base, "fonti", "consegne")
    for radice, cartelle, nomi in os.walk(cons):
        cartelle[:] = [c for c in cartelle if c not in CONSEGNE_SALTATE]
        rel = os.path.relpath(radice, RADICE).replace("\\", "/")
        for n in nomi:
            if n.endswith((".md", ".txt", ".url")):
                files.append(rel + "/" + n)
    return sorted(set(files))


def carica_json(percorso, difetto):
    try:
        with io.open(os.path.join(RADICE, percorso), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return difetto


def risolvi_breve(url, senza_rete):
    """Segue il reindirizzamento di un collegamento breve; seconda via Arctic Shift."""
    if senza_rete:
        return None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA}, method="HEAD")
        with urllib.request.urlopen(req, timeout=20) as r:
            finale = r.geturl()
        if RE_POST.search(urllib.parse.urlsplit(finale).path):
            return finale
    except Exception as e:  # un 403 sulla pagina finale porta comunque l'indirizzo
        finale = getattr(e, "url", None) or (e.geturl() if hasattr(e, "geturl") else None)
        if finale and RE_POST.search(urllib.parse.urlsplit(finale).path):
            return finale
    m = RE_BREVE.match(url)
    if m:
        percorso = "/%s/%s/s/%s" % m.groups()
        try:
            q = urllib.parse.urlencode({"paths": percorso})
            req = urllib.request.Request("https://arctic-shift.photon-reddit.com/api/short_links?" + q,
                                         headers={"User-Agent": "retrogame-mod-pok-dev verifica-link"})
            with urllib.request.urlopen(req, timeout=30) as r:
                dati = json.load(r)
            for rec in dati.get("data") or []:
                dest = rec.get("resolved_path")
                if dest:
                    return "https://www.reddit.com" + dest if dest.startswith("/") else dest
        except Exception:
            pass
    return None


def chiave_breve(url):
    m = RE_BREVE.match(pulisci(url))
    return ("breve:/%s/%s/s/%s" % (m.group(1).lower(), m.group(2).lower(), m.group(3))) if m else None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--senza-rete", action="store_true")
    a = ap.parse_args()

    brevi = carica_json(CACHE_BREVI, {})
    brevi_cambiati = False

    def chiavi_di(url):
        nonlocal brevi_cambiati
        ks = set()
        kb = chiave_breve(url)
        if kb:
            ks.add(kb)
            if kb not in brevi:
                ris = risolvi_breve(pulisci(url), a.senza_rete)
                if ris or not a.senza_rete:
                    brevi[kb] = ris
                    brevi_cambiati = True
            if brevi.get(kb):
                ks.add(chiave(brevi[kb]))
            return {k for k in ks if k}
        k = chiave(url)
        return {k} if k else set()

    noti = set()
    for p in REGISTRI_TESTO:
        for u in estrai(leggi(p)):
            noti |= chiavi_di(u)
    for p in REGISTRI_JSON:
        d = carica_json(p, [])
        for u in (d.keys() if isinstance(d, dict) else d):
            if isinstance(u, str):
                noti |= chiavi_di(u)
    nf = carica_json(NON_FONTI, {})
    non_fonti = set()
    for u in (nf.get("voci") or {}):
        non_fonti |= chiavi_di(u) or {u}
    prefissi = [p.lower() for p in (nf.get("prefissi") or {})]
    noti_min = {k.lower() for k in noti}

    citati = collections.defaultdict(set)
    for f in file_da_scandire():
        for u in estrai(leggi(f)):
            ks = chiavi_di(u)
            if not ks:
                continue
            if any(k in noti or k.lower() in noti_min or k in non_fonti for k in ks):
                continue
            k0 = sorted(ks)[-1]
            if any(k0.lower().startswith(p) for p in prefissi):
                continue
            citati[(k0, u)].add(f)

    if brevi_cambiati:
        os.makedirs(os.path.join(RADICE, os.path.dirname(CACHE_BREVI)), exist_ok=True)
        with io.open(os.path.join(RADICE, CACHE_BREVI), "w", encoding="utf-8") as f:
            json.dump(dict(sorted(brevi.items())), f, ensure_ascii=False, indent=1)
            f.write("\n")

    per_chiave = collections.defaultdict(lambda: [None, set()])
    for (k, u), fs in citati.items():
        per_chiave[k][0] = per_chiave[k][0] or u
        per_chiave[k][1] |= fs
    if a.json:
        with io.open(a.json, "w", encoding="utf-8") as f:
            json.dump({k: {"url": v[0], "file": sorted(v[1])} for k, v in sorted(per_chiave.items())},
                      f, ensure_ascii=False, indent=1)
    irrisolti = sorted(k for k, v in brevi.items() if not v and k not in non_fonti)
    if a.check:
        for k, (u, fs) in sorted(per_chiave.items()):
            print("%s\n    citato in: %s" % (u, ", ".join(sorted(fs))))
        for k in irrisolti:
            print("collegamento breve non risolto: %s" % k)
        if per_chiave:
            print("%d indirizzi non classificati." % len(per_chiave))
        else:
            print("Tutti gli indirizzi citati sono classificati.")
        return 1 if per_chiave else 0
    host = collections.Counter(k.split("/")[0] for k in per_chiave)
    print("%d indirizzi non classificati, %d brevi non risolti" % (len(per_chiave), len(irrisolti)))
    for h, c in host.most_common():
        print("%5d %s" % (c, h))
    return 0


if __name__ == "__main__":
    sys.exit(main())
