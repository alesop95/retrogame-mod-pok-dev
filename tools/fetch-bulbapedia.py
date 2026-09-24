#!/usr/bin/env python3
"""Legge una o piu' pagine di Bulbapedia attraverso la sua API MediaWiki e ne produce lo scheletro di Livello 1.

Perche' esiste
--------------

Bulbapedia e' la fonte che questo progetto consulta piu' spesso, e finora l'ha consultata a mano, una pagina alla volta, attraverso il recupero della pagina HTML. Quella via funziona ma e' cara due volte: porta in contesto il rumore della navigazione del sito insieme al contenuto, e non lascia nulla su disco, cosicche' la sessione successiva rilegge da capo cio' che questa aveva gia' letto. Su un fronte come il Parco Lotta, dove le pagine da leggere sono nove e alcune superano le mille righe di wikitesto, la differenza fra le due vie non e' di comodita' ma di fattibilita'.

La via, e perche' e' legittima
------------------------------

La via non e' il recupero della pagina destinata alle persone ma `api.php`, cioe' l'interfaccia programmatica che MediaWiki espone e che Bulbapedia lascia aperta senza credenziali. E' il criterio che `web-sources-not-fetchable.md` fissa per separare le vie legittime da quelle vietate: si interroga un canale costruito dal proprietario del servizio per l'accesso automatico, chiedendogli i propri dati, invece di imitare un browser su un canale destinato a chi legge. Da qui discendono i due obblighi che questo strumento si da' e che non si possono disattivare da riga di comando, uno user agent descrittivo che dice chi chiama e un'attesa fra due richieste consecutive.

Il contenuto si chiede in wikitesto e non in HTML, e la scelta ha una ragione che va oltre il peso. Il wikitesto conserva i modelli, le tabelle e i collegamenti nella forma in cui gli autori li hanno scritti, quindi una tabella di dati resta una tabella di dati invece di diventare una griglia di marcatori di presentazione: su una pagina come quella degli allenatori del Parco Lotta, che e' quasi tutta tabelle, il wikitesto e' la forma in cui i numeri si possono ancora estrarre con del codice.

Che cosa scrive, e perche' due strati
-------------------------------------

Sotto la cartella di destinazione finiscono due cose. Il grezzo, cioe' il wikitesto di ogni pagina esattamente come l'API lo ha restituito, con accanto l'identificativo della revisione e il momento della lettura: serve a poter rigenerare qualunque derivato senza ri-scaricare, e a poter dire fra sei mesi quale versione della pagina il progetto aveva letto, che su una wiki e' una domanda con una risposta che cambia. E un indice `_INDEX.md` che e' lo scheletro di Livello 1 prescritto da `token-economy.md`, cioe' titolo, gerarchia delle intestazioni e conteggio delle righe per sezione, per ogni pagina. Lo scheletro esiste perche' una cartella di nove pagine non si legge per intero: si guarda l'indice, si decide quali sezioni servono, e si scendono i Livelli 2 e 3 soltanto la'.

Il presidio
-----------

Una pagina che non si riesce a leggere non diventa una pagina vuota: finisce nell'indice come non letta, con il motivo, per la stessa ragione per cui il lettore di Reddit elenca cio' che il tetto ha escluso. Una copertura parziale dichiarata e' usabile, una che somiglia a una completa no.

Uso
---

    python tools/fetch-bulbapedia.py --out _notes/fonti/bulbapedia-parco-lotta-2026-09-21 "Battle Arena" "Battle Dome"
    python tools/fetch-bulbapedia.py --out <cartella> --da-file <elenco.txt>
"""

import argparse
import json
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://bulbapedia.bulbagarden.net/w/api.php"
UA = "retrogame-mod-pok-dev/1.0 (ricerca personale su retrogaming; repository del progetto)"
ATTESA = 1.5          # secondi fra due richieste, non disattivabile
LOTTO = 20            # titoli per richiesta; l'API ne accetta 50, si resta larghi


def contesto_tls():
    """Contesto TLS che verifica sempre, ma con il paniere di radici che su questa macchina non e' scaduto.

    Su Windows lo store di sistema che Python usa per difetto contiene una radice scaduta nella catena di questo host, e la verifica fallisce con `CERTIFICATE_VERIFY_FAILED: certificate has expired` mentre `curl`, che usa un paniere proprio, passa senza rilievi. La correzione giusta non e' disattivare la verifica, che sarebbe un declassamento silenzioso della sicurezza per un sintomo che non c'entra, ma usare un paniere aggiornato: `certifi` lo e', e su questa macchina la catena vi si verifica correttamente. Se `certifi` manca si torna al contesto di difetto, che verifica comunque, e l'eventuale errore resta visibile invece di essere nascosto.
    """
    try:
        import certifi
    except ImportError:
        return ssl.create_default_context()
    return ssl.create_default_context(cafile=certifi.where())


_CONTESTO = None


def chiama(parametri):
    global _CONTESTO
    if _CONTESTO is None:
        _CONTESTO = contesto_tls()
    parametri = dict(parametri, format="json", formatversion="2")
    url = API + "?" + urllib.parse.urlencode(parametri)
    richiesta = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(richiesta, timeout=60, context=_CONTESTO) as risposta:
        return json.loads(risposta.read().decode("utf-8"))


def slug(titolo):
    return re.sub(r"[^a-z0-9]+", "-", titolo.lower()).strip("-")


def scheletro(wikitesto):
    """Gerarchia delle intestazioni con il numero di righe di ciascuna sezione."""
    sezioni = []
    corrente = {"livello": 0, "titolo": "(preambolo)", "righe": 0}
    for riga in wikitesto.splitlines():
        trovata = re.match(r"^(={2,6})\s*(.+?)\s*\1\s*$", riga)
        if trovata:
            sezioni.append(corrente)
            corrente = {"livello": len(trovata.group(1)), "titolo": trovata.group(2), "righe": 0}
        else:
            corrente["righe"] += 1
    sezioni.append(corrente)
    return sezioni


def main():
    ap = argparse.ArgumentParser(description="Legge pagine di Bulbapedia via API MediaWiki.")
    ap.add_argument("titoli", nargs="*", help="titoli delle pagine, nella forma esatta della wiki")
    ap.add_argument("--da-file", help="file di testo con un titolo per riga")
    ap.add_argument("--out", required=True, help="cartella di destinazione, tipicamente sotto _notes/fonti/")
    argomenti = ap.parse_args()

    titoli = list(argomenti.titoli)
    if argomenti.da_file:
        for riga in Path(argomenti.da_file).read_text(encoding="utf-8").splitlines():
            riga = riga.strip()
            if riga and not riga.startswith("#"):
                titoli.append(riga)
    if not titoli:
        ap.error("nessun titolo indicato")

    destinazione = Path(argomenti.out)
    (destinazione / "grezzo").mkdir(parents=True, exist_ok=True)
    momento = datetime.now(timezone.utc).isoformat(timespec="seconds")

    risultati = {}
    for indice in range(0, len(titoli), LOTTO):
        blocco = titoli[indice:indice + LOTTO]
        if indice:
            time.sleep(ATTESA)
        dati = chiama({
            "action": "query",
            "prop": "revisions",
            "rvprop": "content|ids|timestamp",
            "rvslots": "main",
            "titles": "|".join(blocco),
        })
        query = dati.get("query", {})
        normalizzazioni = {n["to"]: n["from"] for n in query.get("normalized", [])}
        for pagina in query.get("pages", []):
            titolo = pagina.get("title", "?")
            chiesto = normalizzazioni.get(titolo, titolo)
            if pagina.get("missing"):
                risultati[chiesto] = {
                    "titolo": titolo,
                    "esito": "assente",
                    "motivo": "la wiki non ha una pagina con questo titolo",
                }
                continue
            revisione = pagina["revisions"][0]
            testo = revisione["slots"]["main"]["content"]
            nome = slug(titolo) + ".wikitext"
            percorso_wiki = urllib.parse.quote(titolo.replace(" ", "_"))
            intestazione = (
                "<!-- fonte: https://bulbapedia.bulbagarden.net/wiki/" + percorso_wiki + " -->\n"
                "<!-- revisione: " + str(revisione["revid"]) + " del " + revisione["timestamp"] + " -->\n"
                "<!-- letta il: " + momento + " via api.php, prop=revisions -->\n\n"
            )
            (destinazione / "grezzo" / nome).write_text(intestazione + testo, encoding="utf-8", newline="")
            risultati[chiesto] = {
                "titolo": titolo,
                "esito": "letta",
                "file": "grezzo/" + nome,
                "revisione": revisione["revid"],
                "timestamp": revisione["timestamp"],
                "byte": len(testo.encode("utf-8")),
                "righe": len(testo.splitlines()),
                "sezioni": scheletro(testo),
            }

    for titolo in titoli:
        risultati.setdefault(titolo, {
            "titolo": titolo,
            "esito": "fallita",
            "motivo": "nessuna risposta dall'API per questo titolo",
        })

    lette = [r for r in risultati.values() if r["esito"] == "letta"]
    righe = []
    righe.append("# Scheletro di Livello 1 delle pagine Bulbapedia lette")
    righe.append("")
    righe.append("Lettura del " + momento + ", via `api.php` con `prop=revisions` e `rvslots=main`, cioe' il canale programmatico che MediaWiki espone senza credenziali. Il wikitesto grezzo di ogni pagina sta sotto `grezzo/`, con la revisione e il momento della lettura nella propria intestazione, cosi' che qualunque derivato si possa rigenerare senza ri-scaricare. Questo indice e' lo scheletro di Livello 1 prescritto da `token-economy.md`: si legge per decidere dove scendere, non al posto delle pagine.")
    righe.append("")
    righe.append("Pagine chieste " + str(len(titoli)) + ", lette " + str(len(lette)) + ", non lette " + str(len(titoli) - len(lette)) + ". Righe di wikitesto complessive " + str(sum(r["righe"] for r in lette)) + ".")
    righe.append("")
    righe.append("| Pagina | Esito | Revisione | Righe | File |")
    righe.append("|---|---|---|---|---|")
    for titolo in titoli:
        r = risultati[titolo]
        if r["esito"] == "letta":
            righe.append("| " + r["titolo"] + " | letta | " + str(r["revisione"]) + " del " + r["timestamp"][:10] + " | " + str(r["righe"]) + " | `" + r["file"] + "` |")
        else:
            righe.append("| " + r["titolo"] + " | NON LETTA: " + r["esito"] + " | - | - | " + r["motivo"] + " |")
    righe.append("")

    for titolo in titoli:
        r = risultati[titolo]
        if r["esito"] != "letta":
            continue
        righe.append("## " + r["titolo"])
        righe.append("")
        for sezione in r["sezioni"]:
            if sezione["livello"] == 0 and sezione["righe"] == 0:
                continue
            rientro = "  " * max(0, sezione["livello"] - 2)
            righe.append("- " + rientro + sezione["titolo"] + " (" + str(sezione["righe"]) + " righe)")
        righe.append("")

    (destinazione / "_INDEX.md").write_text("\n".join(righe) + "\n", encoding="utf-8", newline="")
    (destinazione / "stato.json").write_text(json.dumps(risultati, ensure_ascii=False, indent=2), encoding="utf-8", newline="")

    print("pagine chieste " + str(len(titoli)) + ", lette " + str(len(lette)) + ", non lette " + str(len(titoli) - len(lette)))
    print("indice: " + str(destinazione / "_INDEX.md"))
    for titolo in titoli:
        r = risultati[titolo]
        if r["esito"] != "letta":
            print("  NON LETTA " + titolo + ": " + r["esito"] + ", " + r["motivo"], file=sys.stderr)


if __name__ == "__main__":
    main()
