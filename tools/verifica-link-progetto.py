# -*- coding: utf-8 -*-
"""Verifica che ogni collegamento scritto nei documenti del progetto sia classificato.

Perché esiste
-------------

Il 2026-10-06 il proprietario ha osservato che il progetto dichiarava lette tutte le fonti mentre i collegamenti scritti dentro i suoi stessi documenti, cioè handoff, note, consegne, decisioni e studi, non erano mai stati confrontati con il registro delle fonti, e i collegamenti brevi di condivisione di Reddit, nella forma `/r/<sub>/s/<codice>`, non erano mai stati risolti. Il registro sapeva che cosa aveva letto, ma nessuno sapeva che cosa il progetto citava: un collegamento incollato in un handoff restava fuori da entrambi i conti senza produrre alcun errore.

Che cosa fa
-----------

Estrae ogni indirizzo dai file tracciati e dal materiale scritto dal proprietario o dal progetto sotto `_notes/`, escludendo i testi di terzi scaricati sotto `_notes/fonti/` (salvo le consegne del proprietario in `_notes/fonti/consegne/`, nei soli `.md`, `.txt` e `.url` fuori dalle cartelle di trascrizioni), i lotti, i salvataggi, i cloni, l'output compilato, i modelli del template e le guide copiate intere dal template. Normalizza ogni indirizzo: toglie gli escape con la barra rovescia, la punteggiatura finale, il punto e virgola dei CSV, i parametri di tracciamento, i prefissi `www.`, `old.`, `np.` e `m.`, il frammento, e abbassa l'host. Riduce un post di Reddit al suo identificativo e un video di YouTube al suo, così che due forme dello stesso contenuto contino come una. Risolve i collegamenti brevi di Reddit seguendo il reindirizzamento, con l'archivio Arctic Shift come seconda via, e tiene i risultati in `_notes/fonti/link-brevi.json` per non chiederli due volte.

Non sono indirizzi, e non si contano, tre forme che uno strumento scrive senza che indichino una pagina: un modello di formato che lo strumento completa a runtime (un `%` che non introduce una codifica valida, una graffa, un parametro finale vuoto come `?url=`), un nome riservato alla documentazione dalla RFC 2606 e dalla RFC 6761 (`example.org`, `.example`, `.test`, `.invalid`), e un video di YouTube il cui identificativo non ha undici caratteri. Un collegamento breve di Reddit ha un codice di dieci caratteri: un codice di altra lunghezza è un segnaposto. La pagina d'ingresso di un sito, senza percorso, è classificata quando il registro ha già fonti di quel sito.

Poi confronta con le fonti conosciute: `SOURCES.md`, `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md`, gli esiti e i dimenticati del residuo del corpus, la lista di lettura del corpus, e l'elenco `_notes/fonti/link-non-fonti.json` degli indirizzi che non sono fonti, ciascuno con il proprio motivo (endpoint di strumenti, pagine di scaricamento di programmi, il repository stesso, stringhe d'esempio). Una voce di quell'elenco può dichiarare `solo_in`, cioè i file in cui vale: gli indirizzi fittizi delle prove di uno strumento si escludono solo dentro quello strumento, e lo stesso indirizzo scritto in un documento resta non classificato. La chiave `file_dati` elenca i manifesti scaricati che enumerano il contenuto di una fonte già registrata. Un indirizzo che non sta in nessuno di questi è non classificato.

Uso
---

    python tools/verifica-link-progetto.py                 riepilogo per host
    python tools/verifica-link-progetto.py --check         esce con 1 se c'è un indirizzo non classificato
    python tools/verifica-link-progetto.py --json FILE     scrive i non classificati con i file che li citano
    python tools/verifica-link-progetto.py --senza-rete    non risolve i collegamenti brevi nuovi
    python tools/verifica-link-progetto.py --prova         esegue le prove interne
"""

import argparse
import base64
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
# Il codice di un collegamento breve di Reddit ha dieci caratteri: lo dicono tutte le diciassette
# risoluzioni in cache al 2026-10-06. Un codice di altra lunghezza è un segnaposto, non un breve.
RE_BREVE = re.compile(r"^https?://(?:[a-z0-9.-]*\.)?reddit\.com/(r|u|user)/([^/]+)/s/([A-Za-z0-9]{10})(?![A-Za-z0-9])", re.I)
# Un video di YouTube ha un identificativo di undici caratteri; un indirizzo di video con un
# identificativo di altra lunghezza, o vuoto, non porta a nessun video.
RE_YT_FORMA = re.compile(r"(?:youtube\.com/(?:watch\?(?:[^#]*&)?v=|shorts/|embed/|live/)|youtu\.be/)([^&?/#]*)")
# Un % che non introduce una codifica valida, o una graffa, è il segnaposto di un modello di formato
# (%s, %d, {id}) in uno strumento che costruisce l'indirizzo a runtime: non è una pagina.
RE_MODELLO = re.compile(r"%(?![0-9A-Fa-f]{2})|[{}]")
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


def modello(url):
    """Vero se l'indirizzo è un modello che uno strumento completa a runtime, non una pagina.

    Due forme: un segnaposto di formato (un % che non è una codifica valida, o una graffa), e una
    interrogazione che finisce con un parametro senza valore (`?url=`, `?v=`), a cui lo strumento
    accoda l'indirizzo o l'identificativo vero.
    """
    if RE_MODELLO.search(url):
        return True
    if "?" not in url:
        return False
    ultimo = url.split("?", 1)[1].split("#")[0].split("&")[-1]
    # "id=abc==" è un valore con il riempimento base64, non un parametro vuoto.
    return ultimo.endswith("=") and ultimo.count("=") == 1


# Nomi riservati alla documentazione e alle prove dalla RFC 2606 e dalla RFC 6761: non indicano
# nessuna pagina reale, ed è la forma in cui le prove degli strumenti dovrebbero scrivere i loro esempi.
RISERVATI_TLD = (".example", ".test", ".invalid", ".localhost")
RISERVATI_HOST = ("example.com", "example.org", "example.net", "localhost")


def riservato(host):
    return host.endswith(RISERVATI_TLD) or host in RISERVATI_HOST or host.endswith(
        tuple("." + h for h in RISERVATI_HOST))


def host_breve(host):
    host = host.lower().split("@")[-1].split(":")[0]
    for p in PREFISSI_HOST:
        if host.startswith(p) and host.count(".") >= 2:
            host = host[len(p):]
    return host


def chiave(url):
    """La chiave di confronto: post di Reddit e video di YouTube per identificativo, il resto normalizzato."""
    url = pulisci(url)
    if modello(url):
        return None
    m = RE_REDD_IT.match(url)
    if m:
        return "reddit:" + m.group(1).lower()
    m = RE_YT.search(url)
    if m:
        return "youtube:" + m.group(1)
    m = RE_YT_FORMA.search(url)
    if m and len(m.group(1)) != 11:
        return None
    try:
        p = urllib.parse.urlsplit(url)
    except ValueError:
        return None
    host = host_breve(p.netloc)
    if not host or "." not in host or riservato(host):
        return None
    if host == "onedrive.live.com":
        # Un collegamento di condivisione aperto nel browser porta in `redeem` il collegamento breve
        # 1drv.ms da cui è nato, codificato in base64: sono lo stesso documento, e la chiave è quella.
        r = dict(urllib.parse.parse_qsl(p.query)).get("redeem")
        if r:
            try:
                dec = base64.urlsafe_b64decode(r + "=" * (-len(r) % 4)).decode("ascii")
                if dec.startswith("https://1drv.ms/"):
                    return chiave(dec)
            except (ValueError, UnicodeDecodeError):
                pass
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


def radice_di_sito_noto(k, host_noti):
    """La pagina d'ingresso di un sito, senza percorso né interrogazione, cita il sito e non una pagina:
    è classificata quando il registro ha già fonti di quel sito."""
    return "/" not in k and "?" not in k and ":" not in k and k.lower() in host_noti


class NonFonti:
    """Gli indirizzi che non sono fonti, da `link-non-fonti.json`, ciascuno con il proprio motivo.

    Una voce è un indirizzo esatto (`voci`) o un prefisso di chiave (`prefissi`); il valore è il motivo,
    oppure un oggetto con `motivo` e `solo_in`, l'elenco dei file in cui la voce vale. `solo_in` serve
    agli indirizzi fittizi delle prove degli strumenti: lo stesso indirizzo scritto in un documento
    resta non classificato, così che un'esclusione pensata per un file non nasconda un collegamento
    vero altrove.
    """

    def __init__(self, nf, chiavi_di):
        self.voci = []
        for u, v in (nf.get("voci") or {}).items():
            self.voci.append((chiavi_di(u) or {u}, None, self._ambito(v)))
        for p, v in (nf.get("prefissi") or {}).items():
            self.voci.append((None, p.lower(), self._ambito(v)))

    @staticmethod
    def _ambito(v):
        if isinstance(v, dict) and v.get("solo_in"):
            return set(v["solo_in"])
        return None

    def copre(self, ks, f):
        for chiavi, prefisso, ambito in self.voci:
            if ambito is not None and f is not None and f not in ambito:
                continue
            for k in ks:
                if chiavi is not None and k in chiavi:
                    return True
                if prefisso is not None and k.lower().startswith(prefisso):
                    return True
        return False


def prova():
    """Prove interne: ciascuna fallisce sulla versione dello strumento precedente la correzione del 2026-10-06."""
    esiti = []

    def p(nome, cond):
        esiti.append(cond)
        print("%s %s" % ("ok  " if cond else "FALL", nome))

    p("un segnaposto %s è un modello, non un indirizzo", chiave("https://web.archive.org/web/%sid_/%s") is None)
    p("un segnaposto %d è un modello", chiave("https://a.it/%d") is None)
    p("una graffa è un modello", chiave("https://api.example.org/v1/{id}/x") is None)
    p("un parametro finale vuoto è un modello", chiave("https://archive.org/wayback/available?url=") is None)
    p("una codifica valida non è un modello", not modello("https://example.org/5599-pok%C3%A9mon"))
    p("un dominio riservato alla documentazione non è una pagina", chiave("https://pokemon.example/a") is None
      and chiave("https://example.org/a") is None and chiave("https://sito.test/a") is None)
    p("il riempimento base64 non è un parametro vuoto", not modello("https://example.org/p?id=abc=="))
    p("youtu.be con identificativo corto non è un video", chiave("https://youtu.be/xyz") is None)
    p("watch?v= vuoto non è un video", chiave("https://www.youtube.com/watch?v=") is None)
    p("watch?v=x non è un video", chiave("https://www.youtube.com/watch?v=x") is None)
    p("?si= di condivisione si toglie", chiave("https://youtu.be/7TCf0a04I4U?si=jemqHA6AT1k_Y3bs") == "youtube:7TCf0a04I4U")
    p("?is= di condivisione si toglie", chiave("https://youtu.be/MWwTGl6IK_Q?is=Wz659sDKgT2g-Uei") == "youtube:MWwTGl6IK_Q")
    BREVE_OD = "/x/c/0/ABC"  # separato dall'host perché la scansione non lo legga come un indirizzo
    p("il redeem di OneDrive si riduce al collegamento 1drv.ms",
      chiave("https://onedrive.live.com/:x:/g/personal/0/X?rtime=1&redeem=" +
             base64.urlsafe_b64encode(("https://1drv.ms" + BREVE_OD).encode()).decode().rstrip("="))
      == chiave("https://1drv.ms" + BREVE_OD))
    p("watch e youtu.be danno la stessa chiave",
      chiave("https://www.youtube.com/watch?v=AI1ZdVQ6DfU&t=30") == chiave("https://youtu.be/AI1ZdVQ6DfU"))
    p("un breve ha un codice di dieci caratteri", chiave_breve("https://www.reddit.com/r/s/s/CODICE1") is None)
    p("un breve vero si riconosce",
      chiave_breve("https://www.reddit.com/r/PokemonHome/s/00gpFvJHo4") == "breve:/r/pokemonhome/s/00gpFvJHo4")
    p("un post di Reddit si riduce al suo identificativo",
      chiave("https://old.reddit.com/r/X/comments/AbC123/titolo/?utm_source=share") == "reddit:abc123")
    p("la punteggiatura finale si toglie", list(estrai("vedi [x](https://example.org/p).")) == ["https://example.org/p"])
    p("la parentesi di Wikipedia resta", pulisci("https://example.org/wiki/A_(b)") == "https://example.org/wiki/A_(b)")
    nf = NonFonti({"prefissi": {"esempio.it": {"motivo": "prova", "solo_in": ["tools/a.py"]}},
                   "voci": {"https://example.com/o/r": "il repository stesso"}}, lambda u: {u.split("://")[1]})
    p("una voce con ambito vale nel suo file", nf.copre({"esempio.it/x"}, "tools/a.py"))
    p("una voce con ambito non vale in un documento", not nf.copre({"esempio.it/x"}, "docs/b.md"))
    p("una voce senza ambito vale ovunque", nf.copre({"example.com/o/r"}, "docs/b.md"))
    p("la radice di un sito registrato è classificata", radice_di_sito_noto("smogon.com", {"smogon.com"}))
    p("una pagina di un sito registrato no", not radice_di_sito_noto("smogon.com/forums", {"smogon.com"}))
    p("la radice di un sito non registrato no", not radice_di_sito_noto("rotomlabs.net", {"smogon.com"}))
    print("%d prove, %d fallite" % (len(esiti), esiti.count(False)))
    return 0 if all(esiti) else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--senza-rete", action="store_true")
    ap.add_argument("--prova", action="store_true", help="esegue le prove interne e termina")
    a = ap.parse_args()

    if a.prova:
        return prova()
    brevi = carica_json(CACHE_BREVI, {})
    # Una voce che non ha più la forma di un breve, per esempio un segnaposto entrato in cache
    # prima che il codice di dieci caratteri fosse richiesto, non è più un breve da risolvere.
    validi = {k: v for k, v in brevi.items() if chiave_breve("https://www.reddit.com" + k[len("breve:"):])}
    brevi_cambiati = len(validi) != len(brevi)
    brevi = validi

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
    non_fonti = NonFonti(nf, chiavi_di)
    noti_min = {k.lower() for k in noti}
    host_noti = {k.split("/")[0].split("?")[0] for k in noti_min if ":" not in k.split("/")[0]}
    file_dati = set(nf.get("file_dati") or {})

    citati = collections.defaultdict(set)
    for f in file_da_scandire():
        if f in file_dati:
            continue
        for u in estrai(leggi(f)):
            ks = chiavi_di(u)
            if not ks:
                continue
            if any(k in noti or k.lower() in noti_min for k in ks):
                continue
            if any(radice_di_sito_noto(k, host_noti) for k in ks):
                continue
            if non_fonti.copre(ks, f):
                continue
            k0 = sorted(ks)[-1]
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
    irrisolti = sorted(k for k, v in brevi.items() if not v and not non_fonti.copre({k}, None))
    if a.check:
        for k, (u, fs) in sorted(per_chiave.items()):
            print("%s\n    citato in: %s" % (u, ", ".join(sorted(fs))))
        for k in irrisolti:
            print("collegamento breve non risolto: %s" % k)
        if per_chiave or irrisolti:
            print("%d indirizzi non classificati, %d brevi non risolti." % (len(per_chiave), len(irrisolti)))
            return 1
        print("Tutti gli indirizzi citati sono classificati.")
        return 0
    host = collections.Counter(k.split("/")[0] for k in per_chiave)
    print("%d indirizzi non classificati, %d brevi non risolti" % (len(per_chiave), len(irrisolti)))
    for h, c in host.most_common():
        print("%5d %s" % (c, h))
    return 0


if __name__ == "__main__":
    sys.exit(main())
