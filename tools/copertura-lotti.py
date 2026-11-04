#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quali caselle di specie e forma, fra quelle che esistono fino alla settima generazione, le copie per HOME non coprono.

Perché esiste
-------------
Il 2026-11-03 il proprietario ha chiesto, per l'ennesima volta, se i lotti siano completi, e ha ribadito la regola che
il progetto dice da mesi: tutto ciò che esiste nei giochi fino al 3DS va nei lotti prima della chiusura di Bank, e
la Switch serve solo per ciò che lì non esiste. I lotti erano stati prodotti solo per le voci «sotto scadenza», e le
specie e forme «a via diretta» erano rimaste fuori. Questo strumento rende la domanda una misura ripetibile.

Che cosa fa
-----------
Le caselle attese vengono da `tools/pkhex-attese-fino-gen7`, cioè dalle tabelle personali della libreria del
verificatore per i giochi da Rosso e Blu a Ultrasole e Ultraluna, senza le forme da sola battaglia, fuse e totem. Da
queste toglie le forme che HOME registra senza un esemplare dedicato o che non riconosce, secondo l'articolo di
Bulbapedia «Pokédex (HOME)», revisione 4643615, letto il 2026-11-03. Sono le forme da oggetto tenuto di Arceus,
Genesect e Silvally, Giratina Origine, le forme tecniche di Mothim, Scatterbug, Spewpa e Minior Meteora, e il Pichu
Spunzorecchio. Ci sono poi le varianti Power Construct di Zygarde e le forme che fino alla settima generazione non
restano tali in un box o non sono mai state distribuite. Le differenze di sesso non chiedono un esemplare per sesso,
perché un deposito non cromatico le registra entrambe. Confronta il resto con le copie giudicate da
`tools/pkhex-elenco-copie` e scrive l'elenco delle mancanti.

Uso
---
    python tools/copertura-lotti.py            riepilogo
    python tools/copertura-lotti.py --scrivi   scrive anche pokedex-home-completo/COPERTURA-LOTTI.md, generato
"""
import argparse
import collections
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATTESE = os.path.join(RADICE, "_notes", "lavoro", "giudizi-copie", "attese-fino-gen7.json")
COPIE = os.path.join(RADICE, "_notes", "lavoro", "giudizi-copie", "dopo-bfe89c7-pedigree.json")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "COPERTURA-LOTTI.md")

# Chiuso il 2026-11-04: il proprietario, che ha giocato Leggende Z-A, conferma che le tosature sono varianti contate,
# e il sorgente della libreria (FormArgumentVerifier.CheckFurfrou) dice che in sesta generazione la tosatura torna
# Naturale al deposito e in settima al passaggio da Bank. Quindi non passano da Bank: vanno nel lavoro su Switch.
DA_VERIFICARE = {}


def escluso(n, f):
    if f == 0:
        return None
    if n in (493, 649, 773):
        return "forma da oggetto tenuto, registrata depositando una forma qualsiasi"
    if n == 487:
        return "Giratina Origine, torna Alterata in HOME"
    if n in (414, 664, 665) or (n == 774 and 1 <= f <= 6):
        return "forma tecnica identica, non riconosciuta da HOME"
    if n == 172:
        return "Pichu Spunzorecchio, non riconosciuto da HOME"
    if n == 718 and f in (2, 3):
        return "Zygarde Power Construct, non distinto nell'app"
    if n in (492, 720):
        return "Shaymin Cielo e Hoopa Libero, tornano alla forma base nel box fino alla settima generazione"
    if n == 676:
        return "tosature di Furfrou, tornano Naturali al deposito e in Bank: si portano da Leggende Z-A, nel lavoro su Switch"
    if (n == 670 and f == 5) or (n == 801 and f == 1):
        return "Floette Fiore Eterno e Magearna Colore Antico, mai distribuiti fino alla settima generazione"
    return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scrivi", action="store_true")
    a = p.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    attese = json.load(open(ATTESE, encoding="utf-8"))
    copie = json.load(open(COPIE, encoding="utf-8"))["copie"]
    home = {(x["numero"], x["forma_n"]) for c in copie if c["gruppo"].startswith("HOME") for x in c["esemplari"]}
    escluse = collections.Counter()
    mancanti = []
    for v in attese:
        e = escluso(v["numero"], v["forma_n"])
        if e:
            escluse[e] += 1
        elif (v["numero"], v["forma_n"]) not in home:
            mancanti.append(v)
    totale = len(attese) - sum(escluse.values())
    specie = [v for v in mancanti if v["forma_n"] == 0]
    forme = [v for v in mancanti if v["forma_n"] > 0]
    print("caselle che chiedono un esemplare: %d, coperte %d, mancanti %d (specie %d, forme %d)" %
          (totale, totale - len(mancanti), len(mancanti), len(specie), len(forme)))
    if a.scrivi:
        r = ["# Le caselle che i lotti devono coprire fino alla settima generazione, e quelle che mancano", "",
             "> Documento generato da `tools/copertura-lotti.py --scrivi`. Non si modifica a mano: si rigenera dopo ogni copia "
             "nuova. Regola: tutto ciò che esiste nei giochi fino al 3DS va nei lotti prima della chiusura di Bank, la Switch serve "
             "solo per ciò che lì non esiste. Caselle attese dalla libreria PKHeX 26.10.18 (`tools/pkhex-attese-fino-gen7`), "
             "regole di registrazione di HOME da Bulbapedia, «Pokédex (HOME)», revisione 4643615; copie da `tools/pkhex-elenco-copie`.", "",
             "Caselle che chiedono un esemplare: %d. Coperte dalle copie per HOME: %d. Mancanti: %d, di cui %d specie intere e %d forme." %
             (totale, totale - len(mancanti), len(mancanti), len(specie), len(forme)), "",
             "Escluse, con il motivo: " + "; ".join("%d, %s" % (n, e) for e, n in escluse.items()) + ".", "",
             "Da verificare: " + ("; ".join(DA_VERIFICARE.values()) or "niente") + ".", "",
             "Le forme escluse perché non passano da Bank, come le tosature di Furfrou, non escono dal Pokédex: per la regola del "
             "proprietario del 2026-11-04 (ADR-110) il Pokédex deve essere completo comunque, e quelle forme si producono nel lavoro "
             "su Switch, con una Switch modificata se si trova la via di iniezione, altrimenti giocando e depositando in HOME.", "",
             "## Specie intere mancanti", "", "| Numero | Specie | Giochi fino alla settima generazione |", "|---|---|---|"]
        r += ["| %d | %s | %s |" % (v["numero"], v["specie"], ", ".join(v["giochi"])) for v in specie]
        r += ["", "## Forme mancanti", "", "| Numero | Specie | Forma | Giochi |", "|---|---|---|---|"]
        r += ["| %d | %s | %s | %s |" % (v["numero"], v["specie"], v["forma"], ", ".join(v["giochi"])) for v in forme]
        with open(USCITA, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(r) + "\n")
        print("Scritto " + os.path.relpath(USCITA, RADICE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
