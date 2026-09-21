#!/usr/bin/env python3
"""Legge i thread e le guide di Smogon senza credenziali, e ne scrive i post come testo con l'autore accanto.

Perche' esiste
--------------

Il registro delle fonti di questo progetto ha portato per settimane una trentina di voci Smogon etichettate in blocco come "dietro autenticazione". L'etichetta era falsa, ed e' precisamente il difetto che `web-sources-not-fetchable.md` chiama una etichetta di indisponibilita' sopravvissuta alla propria causa: scoraggia dal riprovare, e cosi' la fonte resta non letta per una ragione che nessuno ha piu' verificato. Il 2026-09-21 il recupero locale ha risposto duecento su tutte quelle provate, con il corpo dei post presente nel documento: non serve alcuna credenziale, serviva soltanto chiedere.

Sul perche' quelle fonti valgano la fatica, la ragione e' di merito e non di completezza. Il catalogo degli avversari dice contro che cosa si combatte, ma non dice che cosa ha funzionato: quello lo dicono le persone che hanno tenuto una serie per centinaia di lotte e hanno poi scritto la squadra con cui l'hanno tenuta, e quelle squadre stanno in questi thread, discusse e corrette da altri che le hanno riprovate. E' la differenza fra un avversario misurato e una strategia collaudata, e nessuna delle due sostituisce l'altra.

Il criterio di legittimita' della via
-------------------------------------

Vale il criterio di `web-sources-not-fetchable.md`, e va enunciato perche' qui non c'e' un canale programmatico dichiarato dal fornitore come ce n'era uno per Bulbapedia. Il servizio pubblica queste pagine senza credenziali e senza muro di accesso, il suo `robots.txt` non porta alcuna direttiva restrittiva per gli agenti generici, e lo strumento si dichiara con uno user agent descrittivo invece di fingersi un browser, attende fra due richieste e non tenta alcun accesso a contenuto riservato. Cio' che si legge e' scritto da altre persone, quindi vale per intero l'ultima sezione di quella regola: l'identificativo dell'autore si conserva accanto al contenuto, l'archivio sta in un posto solo sotto `_notes/fonti/`, e il grezzo e' sacrificabile una volta che la sintesi con l'attribuzione e' entrata nel registro.

Che cosa produce
----------------

Sotto la cartella di uscita scrive il grezzo per pagina, il derivato in Markdown con un blocco per post, e un indice di Livello 1 che per ciascuna pagina elenca i post con autore, data, lunghezza e un contrassegno per quelli che sembrano contenere una squadra. Il contrassegno non e' una lettura ma un filtro: riconosce la forma con cui una squadra si scrive su quel forum, cioe' una riga con la specie e lo strumento dopo la chiocciola, una riga dei punti base e le mosse elencate con il trattino. Serve a decidere quali dei duemila post meritino una lettura vera, che e' esattamente il Livello 1 della disclosure progressiva prescritta da `token-economy.md`.

Il numero dell'ultima pagina non si indovina e non si passa da riga di comando: si legge dalla barra di navigazione della prima pagina scaricata, e se non c'e' il thread ha una pagina sola. Un thread che cresce fra due corse produce quindi una corsa piu' lunga senza che nessuno debba aggiornare un parametro.

Uso
---

    python tools/fetch-smogon.py --thread https://www.smogon.com/forums/threads/<slug>.<id>/ --out _notes/fonti/smogon-parco-lotta-2026-09-21
    python tools/fetch-smogon.py --elenco <file con un indirizzo per riga> --out <cartella>
"""

import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

UA = "retrogame-mod-pok-dev/1.0 (lettore di fonti per un progetto personale di retrogaming; contatto tramite il repository)"
ATTESA = 1.5

# La forma con cui una squadra si scrive su questo forum. Non e' una lettura del contenuto ma un filtro
# sulla forma, e sbaglia in eccesso di proposito: meglio segnalare un post che non porta una squadra che
# perderne uno che la porta.
INDIZI_SQUADRA = [
    re.compile(r"^\s*[A-Z][A-Za-z.'\- ]{2,20}\s*@\s*\S", re.M),
    re.compile(r"^\s*EVs?\s*:", re.M | re.I),
    re.compile(r"^\s*(Adamant|Modest|Jolly|Timid|Bold|Calm|Careful|Impish|Brave|Quiet|Relaxed|Sassy|Hasty|Naive|Lonely|Mild|Rash|Naughty|Gentle|Docile|Hardy|Serious|Bashful|Quirky|Lax)\s+Nature", re.M | re.I),
    re.compile(r"^\s*-\s+[A-Z][A-Za-z ]{2,20}\s*$", re.M),
]


def scarica(url, attesa=ATTESA):
    richiesta = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9",
    })
    time.sleep(attesa)
    with urllib.request.urlopen(richiesta, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def robots_permette(host):
    """Verifica che il servizio non vieti la lettura all'agente generico.

    Il controllo si fa e non si assume, perche' e' la sola parte della legittimita' della via che dipende dal fornitore e puo' cambiare senza preavviso. Una direttiva restrittiva per l'agente generico ferma lo strumento invece di essere ignorata.
    """
    try:
        testo = scarica("https://%s/robots.txt" % host, attesa=0)
    except urllib.error.URLError:
        return True, "robots.txt non raggiungibile, si procede con cautela"
    blocco = None
    for riga in testo.split("\n"):
        nuda = riga.split("#")[0].strip()
        if not nuda:
            continue
        chiave, _, valore = nuda.partition(":")
        chiave, valore = chiave.strip().lower(), valore.strip()
        if chiave == "user-agent":
            blocco = valore == "*"
        elif chiave == "disallow" and blocco and valore not in ("", "/robots.txt"):
            if valore == "/" or "/forums" in valore or "/ingame" in valore:
                return False, "robots.txt vieta %s all'agente generico" % valore
    return True, "robots.txt non pone restrizioni all'agente generico"


# ---------------------------------------------------------------------------
# Estrazione
# ---------------------------------------------------------------------------

_TAG = re.compile(r"<[^>]+>")


def _testo(frammento):
    """Riduce a testo il corpo di un post conservando cio' che ne porta il senso.

    Le interruzioni di riga contano piu' di quanto sembri, perche' una squadra scritta su questo forum e' un elenco di righe e appiattirla in un paragrafo la rende illeggibile proprio nel punto in cui serve. Per la stessa ragione le citazioni restano marcate: un post che cita un altro e' una correzione, e senza la marcatura la correzione e il testo corretto si confondono.
    """
    t = frammento
    t = re.sub(r"<script.*?</script>", "", t, flags=re.S)
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = re.sub(r"</(p|div|li|tr|h[1-6])>", "\n", t)
    t = re.sub(r"<li[^>]*>", "- ", t)
    t = re.sub(r"<blockquote[^>]*>", "\n[citazione]\n", t)
    t = re.sub(r"</blockquote>", "\n[/citazione]\n", t)
    t = _TAG.sub("", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def post_di_pagina(documento):
    """Estrae i post di una pagina di thread XenForo.

    L'articolo porta l'identificativo del post e quello dell'autore nei propri attributi, e il corpo sta in un contenitore con una classe dedicata. Si legge da li' e non dal testo visibile, perche' il testo visibile porta anche firme, contatori di reazioni e pulsanti, che non sono contenuto.
    """
    voci = []
    for pezzo in re.finditer(r'<article[^>]*data-content="post-(\d+)"[^>]*>(.*?)</article>', documento, re.S):
        identificativo, corpo = pezzo.group(1), pezzo.group(2)
        autore = re.search(r'data-author="([^"]*)"', pezzo.group(0))
        quando = re.search(r'<time[^>]*datetime="([^"]*)"', corpo)
        testo_post = ""
        wrapper = re.search(r'<div class="bbWrapper">(.*?)</div>\s*</div>\s*</div>', corpo, re.S)
        if wrapper is None:
            wrapper = re.search(r'<div class="bbWrapper">(.*)', corpo, re.S)
        if wrapper:
            testo_post = _testo(wrapper.group(1))
        voci.append({
            "id": "post-" + identificativo,
            "autore": html.unescape(autore.group(1)) if autore else None,
            "data": quando.group(1) if quando else None,
            "caratteri": len(testo_post),
            "squadra_probabile": sum(1 for r in INDIZI_SQUADRA if r.search(testo_post)) >= 2,
            "testo": testo_post,
        })
    return voci


def articolo(documento):
    """Estrae il corpo di una pagina che non e' un thread, cioe' una guida sotto /ingame/."""
    corpo = re.search(r'<div[^>]*class="[^"]*\bcontent\b[^"]*"[^>]*>(.*?)</div>\s*</div>\s*<footer', documento, re.S)
    if corpo is None:
        corpo = re.search(r"<body[^>]*>(.*)</body>", documento, re.S)
    return _testo(corpo.group(1)) if corpo else ""


def ultima_pagina(documento, percorso_thread):
    """Legge il numero dell'ultima pagina dalla barra di navigazione di QUESTO thread.

    Il vincolo sul percorso non e' pignoleria: una pagina di questo forum porta nelle barre laterali i collegamenti ad altre discussioni, alcuni dei quali puntano a una loro pagina interna. Cercare il numero piu' alto in tutto il documento restituisce quindi la lunghezza della discussione piu' lunga fra quelle citate, non di quella che si sta leggendo, e la prova sul campo e' stata una discussione di una pagina sola dichiarata di quattro, con la prima riscaricata quattro volte. Il difetto e' silenzioso perche' una pagina che non esiste risponde comunque duecento con la prima.
    """
    percorso = re.escape(percorso_thread.rstrip("/"))
    numeri = [int(x) for x in re.findall(percorso + r"/page-(\d+)", documento)]
    return max(numeri) if numeri else 1


# ---------------------------------------------------------------------------
# Corsa
# ---------------------------------------------------------------------------

def slug_di(url):
    pezzo = url.rstrip("/").split("/")[-1]
    pezzo = re.sub(r"#.*$", "", pezzo)
    pezzo = re.sub(r"^page-\d+$", "", pezzo)
    if not pezzo:
        pezzo = url.rstrip("/").split("/")[-2]
    return re.sub(r"[^A-Za-z0-9._-]", "-", pezzo)[:80]


def corsa(indirizzi, uscita, tetto_pagine):
    uscita = Path(uscita)
    uscita.joinpath("grezzo").mkdir(parents=True, exist_ok=True)
    uscita.joinpath("derivato").mkdir(parents=True, exist_ok=True)
    stato = {"letti": [], "falliti": [], "avviato": time.strftime("%Y-%m-%dT%H:%M:%S")}

    for url in indirizzi:
        base = re.sub(r"#.*$", "", url)
        base = re.sub(r"/page-\d+/?$", "/", base)
        slug = slug_di(base)
        e_thread = "/forums/threads/" in base
        try:
            primo = scarica(base)
        except Exception as errore:
            stato["falliti"].append({"url": base, "motivo": str(errore)})
            print("FALLITO %s: %s" % (base, errore))
            continue

        if not e_thread:
            testo = articolo(primo)
            uscita.joinpath("grezzo", slug + ".html").write_text(primo, encoding="utf-8")
            uscita.joinpath("derivato", slug + ".md").write_text(
                "# %s\n\n> Fonte: %s, letta il %s.\n\n%s\n" % (slug, base, time.strftime("%Y-%m-%d"), testo), encoding="utf-8")
            stato["letti"].append({"url": base, "slug": slug, "tipo": "guida", "caratteri": len(testo)})
            print("guida %-55s %6d caratteri" % (slug, len(testo)))
            continue

        percorso = re.sub(r"^https?://[^/]+", "", base)
        pagine = ultima_pagina(primo, percorso)
        if tetto_pagine and pagine > tetto_pagine:
            pagine = tetto_pagine
        tutti = []
        for n in range(1, pagine + 1):
            if n == 1:
                documento = primo
            else:
                try:
                    documento = scarica(base.rstrip("/") + "/page-%d" % n)
                except Exception as errore:
                    stato["falliti"].append({"url": base + "page-%d" % n, "motivo": str(errore)})
                    print("FALLITO pagina %d di %s: %s" % (n, slug, errore))
                    continue
            voci = post_di_pagina(documento)
            if n > 1 and voci and tutti and {x["id"] for x in voci} == {x["id"] for x in tutti[-len(voci):]}:
                # Il servizio risponde duecento anche a una pagina che non esiste, restituendo la prima:
                # se i post coincidono con quelli appena letti, la barra di navigazione ha mentito e ci si
                # ferma, invece di riscrivere n volte lo stesso contenuto credendo di aver letto n pagine.
                print("thread %-42s pagina %3d ripete la precedente, mi fermo" % (slug[:42], n))
                break
            uscita.joinpath("grezzo", "%s-page-%d.html" % (slug, n)).write_text(documento, encoding="utf-8")
            for v in voci:
                v["pagina"] = n
            tutti.extend(voci)
            print("thread %-42s pagina %3d/%3d  %3d post" % (slug[:42], n, pagine, len(voci)))

        righe = ["# %s" % slug, "", "> Fonte: %s, %d pagine lette il %s con `tools/fetch-smogon.py`. Ogni post porta l'identificativo del proprio autore, come prescrive l'ultima sezione di `web-sources-not-fetchable.md`." % (base, pagine, time.strftime("%Y-%m-%d")), ""]
        for v in tutti:
            righe.append("## %s, pagina %d, di %s, %s%s" % (v["id"], v["pagina"], v["autore"] or "autore ignoto", v["data"] or "data ignota", "  [SQUADRA PROBABILE]" if v["squadra_probabile"] else ""))
            righe.append("")
            righe.append(v["testo"] or "(vuoto)")
            righe.append("")
        uscita.joinpath("derivato", slug + ".md").write_text("\n".join(righe), encoding="utf-8")
        stato["letti"].append({
            "url": base, "slug": slug, "tipo": "thread", "pagine": pagine, "post": len(tutti),
            "post_con_squadra": sum(1 for v in tutti if v["squadra_probabile"]),
            "indice": [{k: v[k] for k in ("id", "pagina", "autore", "data", "caratteri", "squadra_probabile")} for v in tutti],
        })

    scrivi_indice(uscita, stato)
    uscita.joinpath("stato.json").write_text(json.dumps(stato, ensure_ascii=False, indent=1), encoding="utf-8")
    return stato


def scrivi_indice(uscita, stato):
    r = ["# Indice di Livello 1 delle fonti Smogon sul Parco Lotta", "",
         "> Generato da `tools/fetch-smogon.py`. Non si modifica a mano: si rigenera. Serve a decidere quali post meritino una lettura vera fra le migliaia scaricate, che e' il Livello 1 della disclosure progressiva di `token-economy.md`.", "",
         "Il contrassegno di squadra probabile e' un filtro sulla forma e non una lettura: riconosce la riga con la specie e lo strumento dopo la chiocciola, la riga dei punti base, la natura dichiarata e le mosse elencate col trattino, e segnala un post quando ne ricorrono almeno due. Sbaglia in eccesso di proposito.", ""]
    totale_post = sum(v.get("post", 0) for v in stato["letti"])
    totale_squadre = sum(v.get("post_con_squadra", 0) for v in stato["letti"])
    r.append("Fonti lette: %d. Post totali: %d, di cui %d con una squadra probabile. Fallite: %d." % (len(stato["letti"]), totale_post, totale_squadre, len(stato["falliti"])))
    r.append("")
    r.append("| Fonte | Tipo | Pagine | Post | Con squadra |")
    r.append("|---|---|---|---|---|")
    for v in stato["letti"]:
        r.append("| %s | %s | %s | %s | %s |" % (v["slug"], v["tipo"], v.get("pagine", ""), v.get("post", ""), v.get("post_con_squadra", "")))
    r.append("")
    if stato["falliti"]:
        r.append("## Non raggiunte, con il motivo")
        r.append("")
        for v in stato["falliti"]:
            r.append("- %s: %s" % (v["url"], v["motivo"]))
        r.append("")
    r.append("## I post con una squadra probabile, per fonte")
    r.append("")
    for v in stato["letti"]:
        if v["tipo"] != "thread":
            continue
        candidati = [p for p in v["indice"] if p["squadra_probabile"]]
        if not candidati:
            continue
        r.append("### %s, %d candidati su %d post" % (v["slug"], len(candidati), v["post"]))
        r.append("")
        for p in candidati:
            r.append("- pagina %d, %s, di %s, %s, %d caratteri" % (p["pagina"], p["id"], p["autore"] or "ignoto", (p["data"] or "")[:10], p["caratteri"]))
        r.append("")
    uscita.joinpath("_INDEX.md").write_text("\n".join(r) + "\n", encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--thread", action="append", default=[])
    p.add_argument("--elenco", help="file con un indirizzo per riga")
    p.add_argument("--out", required=True)
    p.add_argument("--tetto-pagine", type=int, default=0, help="massimo di pagine per thread, zero per nessun tetto")
    args = p.parse_args()

    indirizzi = list(args.thread)
    if args.elenco:
        for riga in Path(args.elenco).read_text(encoding="utf-8").split("\n"):
            riga = riga.strip()
            if riga and not riga.startswith("#"):
                indirizzi.append(riga)
    if not indirizzi:
        sys.exit("nessun indirizzo: servono --thread o --elenco")

    permesso, motivo = robots_permette("www.smogon.com")
    print(motivo)
    if not permesso:
        sys.exit("la lettura automatica non e' permessa, non si procede")

    stato = corsa(indirizzi, args.out, args.tetto_pagine)
    print("\nfonti lette: %d, fallite: %d" % (len(stato["letti"]), len(stato["falliti"])))
    print("uscita in %s" % args.out)


if __name__ == "__main__":
    main()
