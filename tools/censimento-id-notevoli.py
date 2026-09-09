#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Censisce gli identificativi di allenatore notevoli, dalla pagina di Bulbapedia salvata su disco.

Perche' questa enumerazione serve
---------------------------------
Un esemplare da distribuzione o da personaggio non giocante si riconosce dalla coppia fra nome
dell'allenatore e suo identificativo, che nella grande maggioranza dei casi e' fissa e documentata.
Il progetto quella coppia la ha per le voci che ha enumerato, cioe' le distribuzioni dell'archivio
enciclopedico e gli scambi in gioco delle tabelle del verificatore, e non ha alcun modo di sapere
quante coppie documentate esistano al di fuori delle proprie liste. Questa pagina lo dice: e' una
tabella di quasi novecento righe che raccoglie gli identificativi notevoli con il loro allenatore e
l'evento a cui appartengono.

Il confronto e' nei due versi, come ADR-044 prescrive
----------------------------------------------------
Il programma misura due numeri e non uno. Quante righe della fonte trovino corrispondenza nelle
nostre liste, che dice quanto del documentato il progetto copra. E quante non ne trovino, che e' la
nostra cecita' e va guardata riga per riga, perche' la fonte comprende anche identificativi che non
appartengono ad alcun esemplare da collezione, per esempio quelli dei Pokemon da noleggio o quelli
usati internamente dal catalogo di un gioco.

Il presidio sulla forma dell'identificativo, e perche' esiste
-------------------------------------------------------------
La fonte scrive gli identificativi con un numero di cifre variabile, e la differenza non e'
cosmetica: cinque cifre indicano la parte visibile dell'identificativo, sei cifre l'identificativo
completo di alcune generazioni. Confrontare le stringhe cosi' come sono darebbe quindi falsi
negativi, e confrontare i soli numeri interi darebbe falsi positivi fra un identificativo a cinque
cifre e uno a sei che finisce con le stesse. Il programma confronta il valore intero e conserva
accanto la forma originale, dichiarando la coincidenza come debole quando le due forme hanno
lunghezze diverse.

Uso
---
    python tools/censimento-id-notevoli.py
    python tools/censimento-id-notevoli.py --check
    python tools/censimento-id-notevoli.py --self-test
"""

import argparse
import csv
import html
import io
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTE = os.path.join(RADICE, "_notes", "fonti", "2026-09-09-bulbapedia-id-notevoli.html")
NOSTRI_EVENTI = os.path.join(RADICE, "pokedex-home-completo", "serebii-eventi.csv")
NOSTRI_SCAMBI = os.path.join(RADICE, "pokedex-home-completo", "scambi.csv")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "ID-NOTEVOLI.md")
NORMALIZZATO = os.path.join(RADICE, "pokedex-home-completo", "id-notevoli.csv")

# Le diciture con cui la fonte marca righe che non appartengono ad alcun esemplare da collezione:
# servono a spiegare la parte non coperta invece di contarla come cecita' nostra.
NON_COLLEZIONABILI = (
    "rental", "noleggio", "fake trainer", "pokédex", "pokedex", "internally",
    "e-reader trainers", "battle tower", "trainer used internally",
)


def piano(frammento):
    """Il testo di un frammento di HTML, senza marcatori e con le entita' risolte."""
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", frammento))).strip()


def sezione(pagina):
    """La sola sezione dell'elenco, fra l'intestazione che lo apre e quella che lo chiude."""
    inizio = pagina.find('id="List_of_ID_numbers"')
    fine = pagina.find('id="Related_articles"')
    if inizio < 0 or fine < 0 or fine <= inizio:
        return None
    return pagina[inizio:fine]


def righe(sez):
    """Le righe della tabella come quaterne fra identificativo, allenatore, evento e nota."""
    fuori = []
    for blocco in re.split(r"<tr[^>]*>", sez)[1:]:
        celle = [piano(c) for c in re.split(r"<t[dh][^>]*>", blocco)[1:]]
        celle = [c for c in celle if c != ""]
        if len(celle) < 3:
            continue
        identificativo = celle[0]
        if not re.fullmatch(r"[0-9]{1,6}", identificativo):
            continue
        fuori.append({
            "id": identificativo,
            "valore": int(identificativo),
            "cifre": len(identificativo),
            "allenatore": celle[1],
            "evento": celle[2],
            "nota": celle[3] if len(celle) > 3 else "",
        })
    return fuori


def nostri():
    """Le coppie fra allenatore e identificativo che il progetto ha gia' enumerato."""
    coppie = set()
    valori = set()
    if os.path.exists(NOSTRI_EVENTI):
        with io.open(NOSTRI_EVENTI, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                ot = (r.get("allenatore") or "").strip()
                ident = (r.get("identificativo") or "").strip()
                if re.fullmatch(r"[0-9]{1,6}", ident):
                    valori.add(int(ident))
                    if ot:
                        coppie.add((ot.lower(), int(ident)))
    if os.path.exists(NOSTRI_SCAMBI):
        with io.open(NOSTRI_SCAMBI, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                ident = (r.get("identificativo") or "").strip()
                if re.fullmatch(r"[0-9]{1,6}", ident):
                    valori.add(int(ident))
    return coppie, valori


def classifica(riga, coppie, valori):
    """Come una riga della fonte si colloca rispetto alle nostre liste."""
    chiave = (riga["allenatore"].lower(), riga["valore"])
    if chiave in coppie:
        return "coperta con allenatore"
    if riga["valore"] in valori:
        return "coperta sul solo identificativo"
    testo = (riga["evento"] + " " + riga["nota"]).lower()
    if any(m in testo for m in NON_COLLEZIONABILI):
        return "non collezionabile"
    return "non coperta"


def componi(dati, conti):
    r = ["# Gli identificativi di allenatore notevoli, e quanto ne copriamo", ""]
    r.append("> Documento generato da `tools/censimento-id-notevoli.py` dalla pagina di Bulbapedia salvata in `_notes/fonti/`. Non si modifica a mano: si rigenera. La fonte e' di secondo livello e serve a misurare la nostra copertura, non a decidere: dove una riga contraddice le tabelle del verificatore, ha ragione il verificatore.")
    r.append("")
    r.append("La fonte porta %d righe utili. Di queste, %d trovano corrispondenza nelle nostre liste sulla coppia fra allenatore e identificativo, %d sul solo identificativo, %d sono dichiarate dalla fonte stessa come non appartenenti a un esemplare da collezione, e %d restano non coperte: quest'ultimo numero e' la nostra cecita' e va guardato riga per riga."
             % (conti["totale"], conti["coperta con allenatore"], conti["coperta sul solo identificativo"],
                conti["non collezionabile"], conti["non coperta"]))
    r.append("")
    r.append("Il confronto sul solo identificativo e' dichiarato debole e tenuto in una colonna a parte, perche' due eventi diversi possono condividere un numero e perche' la fonte scrive gli identificativi con un numero di cifre variabile: cinque cifre sono la parte visibile, sei l'identificativo completo.")
    r.append("")
    for stato in ("non coperta", "coperta sul solo identificativo", "coperta con allenatore",
                  "non collezionabile"):
        gruppo = [d for d in dati if d["stato"] == stato]
        if not gruppo:
            continue
        r.append("## %s: %d righe" % (stato.capitalize(), len(gruppo)))
        r.append("")
        r.append("| Identificativo | Cifre | Allenatore | Evento |")
        r.append("|---|---|---|---|")
        for d in gruppo:
            r.append("| %s | %d | %s | %s |"
                     % (d["id"], d["cifre"],
                        d["allenatore"].replace("|", "/")[:60],
                        d["evento"].replace("|", "/")[:90]))
        r.append("")
    return "\n".join(r) + "\n"


def normalizza(dati):
    r = ["identificativo,cifre,allenatore,evento,stato,nota"]
    for d in dati:
        campi = [d["id"], str(d["cifre"]), d["allenatore"], d["evento"], d["stato"], d["nota"]]
        r.append(",".join('"%s"' % c.replace('"', '""') if ("," in c or '"' in c) else c
                          for c in campi))
    return "\n".join(r) + "\n"


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("le entita' vengono risolte", "GF & altro", piano("<b>GF</b> &amp; altro"))

    finta = ('id="List_of_ID_numbers"> <table><tr><th>ID number</th><th>OT</th><th>Event</th></tr>'
             '<tr><td>22796</td><td>GF</td><td>Mew</td><td>nota</td></tr>'
             '<tr><td>000001</td><td>AZ</td><td>Floette</td></tr>'
             '<tr><td>non un numero</td><td>x</td><td>y</td></tr></table> id="Related_articles">')
    sez = sezione(finta)
    prova("la sezione viene ritagliata", True, sez is not None and "Related" not in sez)
    lette = righe(sez)
    prova("due righe utili", 2, len(lette))
    prova("l'identificativo resta nella forma originale", "000001", lette[1]["id"])
    prova("e il valore e' l'intero", 1, lette[1]["valore"])
    prova("le cifre vengono conservate", 6, lette[1]["cifre"])
    prova("l'intestazione non entra fra le righe", "22796", lette[0]["id"])

    # Una pagina senza le due intestazioni non si legge a meta': si rifiuta.
    prova("una pagina senza elenco viene rifiutata", None, sezione("<p>niente</p>"))

    coppie = {("gf", 22796)}
    valori = {22796, 1}
    prova("la coppia esatta e' coperta", "coperta con allenatore",
          classifica(lette[0], coppie, valori))
    prova("il solo numero da una copertura debole", "coperta sul solo identificativo",
          classifica(lette[1], coppie, valori))
    # Controllo negativo: una riga che la fonte dichiara di noleggio non e' una nostra cecita'.
    riga = {"id": "000000", "valore": 0, "cifre": 6, "allenatore": "Mr. Al Rent",
            "evento": "Multiple", "nota": "The ID of the Rental Pokemon given to the player"}
    prova("il noleggio non conta come cecita'", "non collezionabile",
          classifica(riga, coppie, valori))
    riga["nota"] = "un evento qualunque"
    prova("mentre una riga ordinaria non coperta lo e'", "non coperta",
          classifica(riga, coppie, valori))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    if not os.path.exists(FONTE):
        print("rifiutato: manca la pagina salvata in " + FONTE)
        return 1
    pagina = io.open(FONTE, encoding="utf-8", errors="replace").read()
    sez = sezione(pagina)
    if sez is None:
        print("rifiutato: la pagina non porta le intestazioni che delimitano l'elenco")
        return 1
    coppie, valori = nostri()
    dati = []
    conti = {"totale": 0, "coperta con allenatore": 0, "coperta sul solo identificativo": 0,
             "non collezionabile": 0, "non coperta": 0}
    for riga in righe(sez):
        riga["stato"] = classifica(riga, coppie, valori)
        dati.append(riga)
        conti["totale"] += 1
        conti[riga["stato"]] += 1

    testo = componi(dati, conti)
    csv_testo = normalizza(dati)
    if a.check:
        disallineati = [p for p, atteso in ((USCITA, testo), (NORMALIZZATO, csv_testo))
                        if (io.open(p, encoding="utf-8").read() if os.path.exists(p) else "") != atteso]
        for p in disallineati:
            print("disallineato: %s va rigenerato" % p)
        if disallineati:
            return 1
        print("allineati: %s e %s" % (USCITA, NORMALIZZATO))
        return 0

    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    io.open(NORMALIZZATO, "w", encoding="utf-8", newline="\n").write(csv_testo)
    print("scritti %s e %s" % (USCITA, NORMALIZZATO))
    print("  righe utili %d | con allenatore %d | solo numero %d | non collezionabili %d | non coperte %d"
          % (conti["totale"], conti["coperta con allenatore"],
             conti["coperta sul solo identificativo"], conti["non collezionabile"],
             conti["non coperta"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
