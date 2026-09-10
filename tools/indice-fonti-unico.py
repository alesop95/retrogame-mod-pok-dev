#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rigenera dentro SOURCES.md l'indice unico che lega ogni fonte al documento che la usa e al capitolo che la cita.

Il problema che risolve
-----------------------
Il progetto ha tre luoghi dove una fonte puo' comparire e nessuno dei tre vede gli altri. La tabella
`FONTI` dentro `tools/build-source-map.py` porta le fonti registrate con l'abstract e il perche'.
Il censimento del corpus porta le centosettantuno voci del post di raccolta, che sono fonti in
attesa di essere lette. La tesi cita per chiave bibliografica, e una fonte registrata che nessun
capitolo cita e' una fonte che il lavoro non ha ancora usato. Chi legge SOURCES.md vede la prima
lista, chi legge il censimento vede la seconda, e la terza si vede solo compilando: la relazione
fra le tre non esisteva in nessun file, e chiederla a una persona significa chiederle di tenere a
mente duecentosessanta righe.

Questo programma la scrive. Non aggiunge fonti e non ne toglie: legge le tre viste che gia'
esistono, le mette in corrispondenza e riscrive un blocco delimitato dentro SOURCES.md, cosicche'
la domanda "questa fonte dove sta scritta, e finisce in tesi?" abbia una risposta in una lettura.

Le tre viste, e come si incrociano
----------------------------------
La corrispondenza fra corpus e fonti registrate si fa sull'indirizzo normalizzato, perche' e' la
sola chiave che le due viste condividono: normalizzare significa togliere lo schema, il prefisso
del sito, la barra finale e i parametri di tracciamento, che sono la ragione per cui due
scritture dello stesso indirizzo sembrano due fonti. La corrispondenza fra fonti registrate e tesi
si fa sulla chiave bibliografica, che e' lo slug della fonte.

Lo stato di lettura dei cluster viene dalla tabella di `LETTURA-DEL-CORPUS.md`, e il programma
pretende che il nome del cluster in quella tabella sia esattamente quello del censimento, oppure un
elenco di quei nomi separati da virgola. Non indovina: se un nome non corrisponde lo dichiara nel
documento generato, perche' un accoppiamento indovinato produrrebbe uno stato di lettura falso, che
e' peggio di uno stato mancante.

Uso
---
    python tools/indice-fonti-unico.py
    python tools/indice-fonti-unico.py --check
    python tools/indice-fonti-unico.py --self-test
"""

import argparse
import csv
import io
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRO = os.path.join(RADICE, "SOURCES.md")
CORPUS = os.path.join(RADICE, "pokedex-home-completo", "fonti-collezione.csv")
LETTURA = os.path.join(RADICE, "pokedex-home-completo", "LETTURA-DEL-CORPUS.md")
CAPITOLI = os.path.join(RADICE, "tesi", "capitoli")

INIZIO = "<!-- indice-fonti-unico: inizio, generato da tools/indice-fonti-unico.py -->"
FINE = "<!-- indice-fonti-unico: fine -->"

TRACK = {
    "BRI": "ponte fra generazioni",
    "SME": "salvataggio di Smeraldo",
    "3DS": "modding della console",
    "LDN": "scambio locale",
    "EVT": "ricreazione degli eventi",
    "ACE": "esecuzione di codice",
    "GEN": "generazione da console corrente",
    "BAT": "pila tampone",
    "PKD": "Pokedex nel deposito",
}


def normalizza_url(u):
    """L'indirizzo ridotto alla sua identita', per riconoscere due scritture della stessa pagina."""
    u = (u or "").strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^(www|m|old|classic)\.", "", u)
    u = u.split("?")[0].split("#")[0]
    u = u.rstrip("/")
    # Un post di Reddit ha due scritture correnti, con e senza il titolo appeso dopo
    # l'identificativo, e sono la stessa pagina: senza questa riduzione il registro e il
    # censimento sembrano portare due fonti dove ne portano una.
    m = re.match(r"(reddit\.com/r/[^/]+/comments/[a-z0-9]+)", u)
    if m:
        return m.group(1)
    return u


def carica_fonti():
    """Le fonti registrate, dalla tabella che ADR-055 dichiara fonte unica."""
    import importlib.util
    percorso = os.path.join(RADICE, "tools", "build-source-map.py")
    if not os.path.exists(percorso):
        return None, "manca il programma che possiede la tabella delle fonti"
    spec = importlib.util.spec_from_file_location("build_source_map", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    if not hasattr(modulo, "FONTI"):
        return None, "il programma delle fonti non espone piu' la tabella FONTI"
    return modulo.FONTI, None


def carica_corpus(percorso):
    """Le voci del corpus, con cluster, indirizzo ed esito della corsa."""
    if not os.path.exists(percorso):
        return None, "manca il censimento del corpus in " + percorso
    voci = []
    with io.open(percorso, encoding="utf-8", newline="") as f:
        for riga in csv.DictReader(f, delimiter=";"):
            cluster = riga["cluster"]
            if riga.get("sottocluster"):
                cluster = cluster + " / " + riga["sottocluster"]
            voci.append({"cluster": cluster, "url": riga["indirizzo"],
                         "esito": riga["esito"], "titolo": riga.get("titolo") or riga.get("ancora") or ""})
    return voci, None


def carica_stato_lettura(percorso):
    """Lo stato dichiarato di ciascun cluster, dalla tabella del registro di lettura."""
    if not os.path.exists(percorso):
        return {}, []
    stato, righe_non_accoppiate = {}, []
    testo = io.open(percorso, encoding="utf-8").read()
    for riga in testo.split("\n"):
        if not riga.startswith("| ") or riga.startswith("| Cluster") or riga.startswith("|---"):
            continue
        celle = [c.strip() for c in riga.strip().strip("|").split("|")]
        if len(celle) < 4:
            continue
        nomi, _voci, esito, dove = celle[0], celle[1], celle[2], celle[3]
        for nome in [n.strip() for n in nomi.split(",")]:
            if not nome:
                continue
            stato[nome] = (esito, dove)
        righe_non_accoppiate.append(nomi)
    return stato, righe_non_accoppiate


def carica_citazioni(cartella):
    """Le chiavi citate, capitolo per capitolo, cosicche' si veda dove una fonte entra nel documento."""
    per_chiave = {}
    if not os.path.isdir(cartella):
        return per_chiave
    for nome in sorted(os.listdir(cartella)):
        if not nome.endswith(".tex"):
            continue
        testo = io.open(os.path.join(cartella, nome), encoding="utf-8").read()
        etichetta = nome.split("-")[0]
        for m in re.finditer(r"\\cite\{([^}]*)\}", testo):
            for chiave in m.group(1).split(","):
                chiave = chiave.strip()
                if chiave:
                    per_chiave.setdefault(chiave, set()).add(etichetta)
    return per_chiave


def componi(fonti, corpus, stato, citazioni):
    per_url = {}
    for f in fonti:
        per_url.setdefault(normalizza_url(f[2]), f[0])

    cluster_ordine, per_cluster = [], {}
    for v in corpus:
        if v["cluster"] not in per_cluster:
            cluster_ordine.append(v["cluster"])
            per_cluster[v["cluster"]] = []
        per_cluster[v["cluster"]].append(v)

    promosse = {}
    for v in corpus:
        slug = per_url.get(normalizza_url(v["url"]))
        if slug:
            promosse[slug] = v["cluster"]

    senza_citazione = [f for f in fonti if f[0] not in citazioni]
    senza_documento = [f for f in fonti if not f[8]]
    cluster_senza_stato = [c for c in cluster_ordine if c not in stato]
    nomi_stato_ignoti = [n for n in stato if n not in per_cluster]

    r = []
    r.append(INIZIO)
    r.append("")
    r.append("## Indice unico: dove sta ciascuna fonte, e dove finisce")
    r.append("")
    r.append("> Blocco generato da `tools/indice-fonti-unico.py`. Non si modifica a mano: si rigenera. Non aggiunge e non toglie fonti, perche' non e' un registro ma una vista: mette in corrispondenza le tre liste che il progetto gia' possiede, cioe' le fonti registrate, le voci del corpus e le citazioni della tesi.")
    r.append("")
    r.append("Esiste per una ragione dichiarata dall'utente il 2026-09-10, ed e' la stessa che giustifica `MAPPA-DOCUMENTI.md`: un progetto che produce documenti generati a partire da fonti perde in fretta la relazione fra i due, e la domanda utile non e' quali fonti esistano ma dove sia scritto cio' che ciascuna ha dato. Le tre liste non si vedono fra loro: chi legge il registro vede le fonti registrate, chi legge il censimento vede il corpus, e le citazioni della tesi si vedono soltanto compilando.")
    r.append("")
    r.append("### Il conto")
    r.append("")
    r.append("| Misura | Valore |")
    r.append("|---|---|")
    r.append("| fonti registrate nella tabella unica | %d |" % len(fonti))
    r.append("| di esse, lette | %d |" % sum(1 for f in fonti if f[4]))
    r.append("| di esse, citate in tesi | %d |" % (len(fonti) - len(senza_citazione)))
    r.append("| di esse, con almeno un documento del progetto che le usa | %d |" % (len(fonti) - len(senza_documento)))
    r.append("| voci del corpus della collezione | %d |" % len(corpus))
    r.append("| di esse, promosse a fonte registrata | %d |" % len(promosse))
    r.append("| cluster del corpus | %d |" % len(cluster_ordine))
    r.append("| di essi, con uno stato di lettura dichiarato | %d |" % (len(cluster_ordine) - len(cluster_senza_stato)))
    r.append("")
    r.append("### Le fonti registrate, e dove finisce ciascuna")
    r.append("")
    r.append("La colonna dei documenti dice dove sta la sintesi di quella fonte dentro il progetto, cioe' quale nota, referenza o censimento la usa; la colonna dei capitoli dice dove la tesi la cita. Una riga senza documenti e' una fonte registrata e non ancora sfruttata; una riga senza capitoli e' una fonte che il documento composto non ha ancora assorbito.")
    r.append("")
    r.append("| Fonte | Liv | Track | Dove sta la sintesi | Capitoli |")
    r.append("|---|---|---|---|---|")
    for f in sorted(fonti, key=lambda x: (x[3], x[0])):
        slug, nome, _url, livello, letto, track, _abs, _perche, serve, _rel = f
        documenti = ", ".join("`%s`" % d.strip("[]") for d, _ in serve) if serve else "nessuno"
        capitoli = ", ".join(sorted(citazioni.get(slug, []))) or "nessuno"
        marca = "" if letto else " (non letta)"
        origine = " (dal corpus)" if slug in promosse else ""
        r.append("| %s%s%s | %d | %s | %s | %s |"
                 % (nome, marca, origine, livello,
                    ", ".join(TRACK.get(t, t) for t in track) or "trasversale",
                    documenti, capitoli))
    r.append("")
    r.append("### Il corpus della collezione, cluster per cluster")
    r.append("")
    r.append("Ogni riga e' un cluster del post di raccolta. Lo stato viene dal registro di lettura e non da questa vista, che si limita a metterlo accanto al conto delle voci e a quante di esse siano diventate fonti registrate. Un cluster letto le cui voci non abbiano prodotto alcuna fonte registrata non e' un difetto: significa che il cluster ha confermato cose gia' note, e il registro di lettura lo dice.")
    r.append("")
    r.append("| Cluster | Voci | Promosse | Stato di lettura | Dove sta l'esito |")
    r.append("|---|---|---|---|---|")
    for c in cluster_ordine:
        voci = per_cluster[c]
        n_prom = sum(1 for v in voci if per_url.get(normalizza_url(v["url"])))
        esito, dove = stato.get(c, ("da leggere", ""))
        r.append("| %s | %d | %d | %s | %s |" % (c, len(voci), n_prom, esito, dove or "-"))
    r.append("")
    r.append("### I buchi, dichiarati invece che dedotti")
    r.append("")
    if senza_citazione:
        r.append("Fonti registrate che nessun capitolo cita, %d: %s."
                 % (len(senza_citazione), ", ".join(f[1] for f in senza_citazione)))
    else:
        r.append("Non ci sono fonti registrate che nessun capitolo cita.")
    r.append("")
    if senza_documento:
        r.append("Fonti registrate che nessun documento del progetto usa, %d: %s."
                 % (len(senza_documento), ", ".join(f[1] for f in senza_documento)))
    else:
        r.append("Non ci sono fonti registrate che nessun documento del progetto usa.")
    r.append("")
    if nomi_stato_ignoti:
        r.append("Righe del registro di lettura il cui nome non corrisponde ad alcun cluster del censimento, %d: %s. Vanno riscritte con il nome esatto, perche' finche' non corrispondono il loro stato non compare nella tabella qui sopra."
                 % (len(nomi_stato_ignoti), ", ".join(sorted(nomi_stato_ignoti))))
    else:
        r.append("Ogni riga del registro di lettura corrisponde a un cluster del censimento.")
    r.append("")
    r.append(FINE)
    return "\n".join(r)


def inserisci(testo, blocco):
    """Il blocco al posto del precedente, oppure in coda alla sezione che descrive la struttura del file."""
    if INIZIO in testo and FINE in testo:
        i = testo.index(INIZIO)
        j = testo.index(FINE) + len(FINE)
        return testo[:i] + blocco + testo[j:]
    ancora = "\n## Livello 1:"
    k = testo.index(ancora)
    return testo[:k] + "\n" + blocco + "\n" + testo[k:]


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("lo schema non fa differenza", normalizza_url("http://a.com/x"), normalizza_url("https://a.com/x"))
    prova("il prefisso del sito non fa differenza", normalizza_url("https://www.reddit.com/r/x/"), normalizza_url("https://old.reddit.com/r/x"))
    prova("i parametri di tracciamento non fanno differenza", normalizza_url("https://a.com/x?utm_source=y"), normalizza_url("https://a.com/x"))
    prova("due pagine diverse restano diverse", False, normalizza_url("https://a.com/x") == normalizza_url("https://a.com/y"))
    prova("un post di Reddit con e senza titolo e' lo stesso post",
          normalizza_url("https://www.reddit.com/r/x/comments/abc123/"),
          normalizza_url("https://www.reddit.com/r/x/comments/abc123/un_titolo_lungo/"))
    prova("ma due post diversi restano diversi", False,
          normalizza_url("https://www.reddit.com/r/x/comments/abc123/") ==
          normalizza_url("https://www.reddit.com/r/x/comments/abc124/"))

    stato, _ = carica_stato_lettura(os.devnull)
    prova("un registro assente non inventa stati", {}, stato)

    # Il blocco si sostituisce al precedente invece di accumularsi.
    testo = "testa\n" + INIZIO + "\nvecchio\n" + FINE + "\ncoda\n"
    nuovo = inserisci(testo, INIZIO + "\nnuovo\n" + FINE)
    prova("il blocco vecchio sparisce", False, "vecchio" in nuovo)
    prova("e il resto del file resta", True, "testa" in nuovo and "coda" in nuovo)

    citazioni = carica_citazioni(CAPITOLI)
    prova("le citazioni si leggono dai capitoli", True, len(citazioni) > 50)

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="non scrive: dice soltanto se il blocco nel registro sia allineato")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    fonti, errore = carica_fonti()
    if errore:
        print("rifiutato: " + errore)
        return 1
    corpus, errore = carica_corpus(CORPUS)
    if errore:
        print("rifiutato: " + errore)
        return 1
    stato, _ = carica_stato_lettura(LETTURA)
    citazioni = carica_citazioni(CAPITOLI)

    blocco = componi(fonti, corpus, stato, citazioni)
    vecchio = io.open(REGISTRO, encoding="utf-8").read()
    nuovo = inserisci(vecchio, blocco)

    if a.check:
        if vecchio != nuovo:
            print("disallineato: il blocco dentro %s va rigenerato" % REGISTRO)
            return 1
        print("allineato: il blocco dentro %s" % REGISTRO)
        return 0

    io.open(REGISTRO, "w", encoding="utf-8", newline="\n").write(nuovo)
    print("aggiornato il blocco dentro %s" % REGISTRO)
    print("  fonti registrate %d, voci di corpus %d, chiavi citate in tesi %d"
          % (len(fonti), len(corpus), len(citazioni)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
