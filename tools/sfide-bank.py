#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le sfide di HOME che diventano impossibili con la chiusura di Bank, confrontate con le copie del progetto.

Perché esiste
-------------
Il 2026-11-03 il proprietario ha deciso di completare tutte le sfide di HOME (ADR-107) e ha chiesto di controllare
subito quali dipendano da Bank, perché quelle si possono completare solo con esemplari che passano dalla banca prima
del 26 febbraio 2027, cioè con i nostri lotti. L'elenco di partenza è quello del post di r/PokemonHome
`1voa411` del 2026-08-14, che l'autore dichiara preso dall'elenco di Serebii: 42 sfide visibili e 5 nascoste.

Che cosa fa
-----------
Per ogni sfida, scritta qui come regola di specie e giochi d'origine, cerca negli esiti di `tools/pkhex-elenco-copie`
un esemplare che la soddisfi: specie per numero nazionale, gioco d'origine fra quelli della sfida, cromatico se la
sfida lo chiede e forma se la sfida ne nomina una. Dal 2026-11-03 l'elenco è confrontato anche con la pagina delle
sfide di Serebii e con il foglio comunitario «Bank Closing all possible things checklist V0.5». Distingue le cinque copie per HOME, che passano tutte, dai gruppi a parte, cioè la decisione finale e
i giapponesi, che dipendono da una decisione. Una sfida che chiede più specie è coperta solo se le copre tutte.
Stampa per ogni sfida lo stato e la copia che la copre, e alla fine le scoperte, cioè le sfide che nessuna copia per
HOME soddisfa. Il controllo legge i dati degli esemplari, non lo stato delle sfide nell'app.

Uso
---
    python tools/sfide-bank.py                       sulle copie giudicate in _notes/lavoro/giudizi-copie/dopo-bfe89c7.json
    python tools/sfide-bank.py --giudizio FILE.json  su un altro esito di pkhex-elenco-copie
    python tools/sfide-bank.py --scrivi              scrive anche pokedex-home-completo/SFIDE-BANK.md, generato
"""
import argparse
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GIUDIZIO = os.path.join(RADICE, "_notes", "lavoro", "giudizi-copie", "dopo-bfe89c7.json")

KANTO_VC = {"RD", "GN", "BU", "YW"}
JOHTO_VC = {"GD", "SI", "C"}
RSE = {"R", "S", "E"}
FRLG = {"FR", "LG"}
DPPT = {"D", "P", "Pt"}
HGSS = {"HG", "SS"}
BW = {"B", "W"}
B2W2 = {"B2", "W2"}
XY = {"X", "Y"}
ORAS = {"OR", "AS"}
SM = {"SN", "MN"}
USUM = {"US", "UM"}
ALOLA = SM | USUM
TRANSPORTER = KANTO_VC | JOHTO_VC | RSE | FRLG | {"CXD"} | DPPT | HGSS | BW | B2W2

# (testo della sfida, specie richieste per numero nazionale, giochi d'origine ammessi, cromatico richiesto, nascosta)
SFIDE = [
    ("Register Blastoise from the good ol' Kanto Region!", [9], KANTO_VC, False, False),
    ("Register Charizard from the good ol' Kanto Region!", [6], KANTO_VC, False, False),
    ("Register Venusaur from the good ol' Kanto Region!", [3], KANTO_VC, False, False),
    ("Register Pikachu from the good ol' Kanto Region!", [25], KANTO_VC, False, False),
    ("Register Cosmog, Cosmoem, Solgaleo and Lunala from the Alola Region", [789, 790, 791, 792], ALOLA, False, False),
    ("Register Dialga from Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum!", [483], DPPT, False, False),
    ("Register Palkia from Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum", [484], DPPT, False, False),
    ("Register Giratina from Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum!", [487], DPPT, False, False),
    ("Register Dialga, Palkia and Giratina from the Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum", [483, 484, 487], DPPT, False, False),
    ("Register Groudon and Kyogre from Pokémon Omega Ruby or Pokémon Alpha Sapphire", [383, 382], ORAS, False, False),
    ("Register Groudon from Pokémon Omega Ruby or Pokémon Alpha Sapphire", [383], ORAS, False, False),
    ("Register Kyogre from Pokémon Omega Ruby or Pokémon Alpha Sapphire", [382], ORAS, False, False),
    ("Register Rayquaza from Pokémon Omega Ruby or Pokémon Alpha Sapphire", [384], ORAS, False, False),
    ("Register Groudon from Pokémon Ruby, Pokémon Sapphire, or Pokémon Emerald", [383], RSE, False, False),
    ("Register Kyogre from Pokémon Ruby, Pokémon Sapphire, or Pokémon Emerald", [382], RSE, False, False),
    ("Register Rayquaza from Pokémon Ruby, Pokémon Sapphire, or Pokémon Emerald", [384], RSE, False, False),
    ("Register Ho-Oh from Pokémon HeartGold or Pokémon SoulSilver!", [250], HGSS, False, False),
    ("Register Lugia from Pokémon HeartGold or Pokémon SoulSilver", [249], HGSS, False, False),
    ("Register Ho-Oh from the good ol' Johto Region", [250], JOHTO_VC, False, False),
    ("Register Lugia from the good ol' Johto Region", [249], JOHTO_VC, False, False),
    ("Register Suicune from the good ol' Johto Region", [245], JOHTO_VC, False, False),
    ("Register Lunala and Necrozma from Pokémon Ultra Sun or Pokémon Ultra Moon", [792, 800], USUM, False, False),
    ("Register Solgaleo and Necrozma from Pokémon Ultra Sun or Pokémon Ultra Moon", [791, 800], USUM, False, False),
    ("Register Lunala from Pokémon Sun or Pokémon Moon", [792], SM, False, False),
    ("Register Solgaleo from Pokémon Sun or Pokémon Moon", [791], SM, False, False),
    ("Register Solgaleo, Lunala and Necrozma from the Alola Region", [791, 792, 800], ALOLA, False, False),
    ("Register Treecko, Grovyle and Sceptile from Pokémon Omega Ruby or Pokémon Alpha Sapphire!", [252, 253, 254], ORAS, False, False),
    ("Register Torchic, Combusken and Blaziken from Pokémon Omega Ruby or Pokémon Alpha Sapphire!", [255, 256, 257], ORAS, False, False),
    ("Register Mudkip, Marshtomp and Swampert from Pokémon Omega Ruby or Pokémon Alpha Sapphire!", [258, 259, 260], ORAS, False, False),
    ("Register Treecko, Torchic, and Mudkip from Pokémon Omega Ruby or Pokémon Alpha Sapphire!", [252, 255, 258], ORAS, False, False),
    ("Register Turtwig, Chimchar and Piplup from Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum", [387, 390, 393], DPPT, False, False),
    ("Register Venusaur from Pokémon FireRed & LeafGreen", [3], FRLG, False, False),
    ("Register Reshiram from the Pokémon Black or Pokémon White", [643], BW, False, False),
    ("Register Reshiram and Kyurem from Pokémon Black 2 or Pokémon White 2", [643, 646], B2W2, False, False),
    ("Register Zekrom and Kyurem from Pokémon Black 2 or Pokémon White 2", [644, 646], B2W2, False, False),
    ("Register Xerneas from Pokémon X or Pokémon Y", [716], XY, False, False),
    ("Register Yveltal from Pokémon X or Pokémon Y", [717], XY, False, False),
    ("Register Shiny Genesect", [649], None, True, False),
    ("Register Diancie from Pokémon X or Pokémon Y!", [719], XY, False, True),
    ("Register Eevee brought over using Poké Transporter!", [133], TRANSPORTER, False, True),
    ("Register Litwick brought over using Poké Transporter!", [607], TRANSPORTER, False, True),
    # Aggiunte il 2026-11-03 dal confronto con la scheda «Home Challenges from bank» del foglio comunitario
    # «Bank Closing all possible things checklist V0.5», terza fonte dopo il post 1voa411 e la pagina di Serebii.
    ("Register Charizard from Pokémon FireRed & LeafGreen", [6], FRLG, False, False),
    ("Register Zekrom from Pokémon Black or Pokémon White", [644], BW, False, False),
    ("Register Pikachu wearing a hat", [25], ALOLA, False, False,
     {"Originale", "Hoenn", "Sinnoh", "Unima", "Kalos", "Alola", "Berretto Compagni", "Berretto Mondiale"}),
    # Aggiunta il 2026-11-03 dalla sezione «HOME Challenges» del foglio «Here's a Checklist to 100% Complete Pokémon
    # HOME» (post 1bwr0l1): il testo non nomina un gioco, il foglio la attribuisce a Sole e Luna, e qui la si tratta
    # con la regola prudente, cioè origine Alola.
    ("Register the guardian deities of Alola!", [785, 786, 787, 788], ALOLA, False, False),
    # Identificata il 2026-11-03 su Bulbapedia, «Challenge (HOME)», revisione 4643183: uno Snorlax da evento, cioè il
    # Munchlax del dono con Snorlium Z (carta 1601) evoluto, oppure lo Snorlax di Nihonbashi (carta 286).
    ("Register Pulverizing Snorlax", [143], ALOLA, False, True, None, ("carta 1601", "carta 286")),
]

# Sfide che contano specie distinte invece di nominarle: (testo, minimo, giochi d'origine, nota sulla regola).
SFIDE_CONTEGGIO = [
    ("Register 100 different species of Pokémon that live in the Alola Region", 100, ALOLA,
     "regola prudente, origine Alola; resta da confermare che almeno 100 delle specie siano nel Pokédex di Alola"),
]


def carica(percorso):
    d = json.load(open(percorso, encoding="utf-8"))
    return d["copie"] if isinstance(d, dict) else d


def soddisfa(x, numero, giochi, cromatico, forme=None, eventi=None):
    return (x["numero"] == numero and (giochi is None or x["gioco"] in giochi)
            and (not cromatico or x["cromatico"]) and (forme is None or x["forma"] in forme)
            and (eventi is None or any(e in x.get("evento", "") for e in eventi)))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--giudizio", default=GIUDIZIO)
    p.add_argument("--scrivi", action="store_true")
    a = p.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    copie = carica(a.giudizio)
    scoperte = []
    righe = []
    for voce in SFIDE:
        testo, specie, giochi, cromatico, nascosta = voce[:5]
        forme = voce[5] if len(voce) > 5 else None
        eventi = voce[6] if len(voce) > 6 else None
        dove_home, dove_parte = [], []
        for numero in specie:
            h = [(c["gruppo"], x["box"], x["posto"]) for c in copie if c["gruppo"].startswith("HOME")
                 for x in c["esemplari"] if soddisfa(x, numero, giochi, cromatico, forme, eventi)]
            q = [(c["gruppo"], x["box"], x["posto"]) for c in copie if not c["gruppo"].startswith("HOME")
                 for x in c["esemplari"] if soddisfa(x, numero, giochi, cromatico, forme, eventi)]
            dove_home.append(h[0] if h else None)
            dove_parte.append(q[0] if q else None)
        if all(dove_home):
            stato = "COPERTA dalle copie per HOME: " + ", ".join("%s box %d posto %d" % t for t in dove_home)
        elif all(h or q for h, q in zip(dove_home, dove_parte)):
            stato = "COPERTA solo con un gruppo a parte: " + ", ".join(
                "%s box %d posto %d" % (h or q) for h, q in zip(dove_home, dove_parte))
            scoperte.append(testo)
        else:
            mancanti = [n for n, h, q in zip(specie, dove_home, dove_parte) if not (h or q)]
            stato = "SCOPERTA: manca la specie %s con l'origine richiesta" % ", ".join(map(str, mancanti))
            scoperte.append(testo)
        print("%s%s\n    %s" % ("[nascosta] " if nascosta else "", testo, stato))
        righe.append("| %s | %s | %s |" % (testo.replace("|", "/"), "sì" if nascosta else "", stato))
    for testo, minimo, giochi, nota in SFIDE_CONTEGGIO:
        specie = {x["numero"] for c in copie if c["gruppo"].startswith("HOME") for x in c["esemplari"] if x["gioco"] in giochi}
        if len(specie) >= minimo:
            stato = "COPERTA dalle copie per HOME: %d specie distinte con l'origine richiesta, %s" % (len(specie), nota)
        else:
            stato = "SCOPERTA: %d specie distinte su %d, %s" % (len(specie), minimo, nota)
            scoperte.append(testo)
        print("%s\n    %s" % (testo, stato))
        righe.append("| %s |  | %s |" % (testo, stato))
    print("\n%d sfide controllate, %d non coperte dalle sole copie per HOME:" % (len(SFIDE) + len(SFIDE_CONTEGGIO), len(scoperte)))
    for t in scoperte:
        print("  - " + t)
    print("Non controllabile dai dati: «Move Pokémon from Pokémon Bank», già fatta il 2026-11-03.")
    if a.scrivi:
        uscita = os.path.join(RADICE, "pokedex-home-completo", "SFIDE-BANK.md")
        fonte = os.path.relpath(a.giudizio, RADICE).replace(os.sep, "/")
        testa = [
            "# Le sfide di HOME che dipendono da Bank, e se le copie le coprono",
            "",
            "> Documento generato da `tools/sfide-bank.py --scrivi`. Non si modifica a mano: si rigenera dopo ogni giro e dopo "
            "ogni copia nuova. L'elenco delle sfide viene dal post di r/PokemonHome `1voa411` del 2026-08-14, che lo dichiara "
            "preso da Serebii; il controllo legge i dati degli esemplari nelle copie giudicate da `tools/pkhex-elenco-copie`, "
            "cioè `%s`, e non lo stato delle sfide nell'app." % fonte,
            "",
            "Sfide controllate: %d. Non coperte dalle sole copie per HOME: %d. Le non coperte vanno prodotte prima della chiusura "
            "di Bank, dentro la produzione degli statici, dei doni e degli starter di ADR-106. «Move Pokémon from Pokémon Bank» è fatta dal 2026-11-03. Fonti dell'elenco: il post 1voa411, la pagina delle sfide di Serebii, la scheda «Home Challenges from bank» del foglio «Bank Closing all possible things checklist V0.5» la sezione «HOME Challenges» del foglio del post 1bwr0l1 e l'articolo di Bulbapedia «Challenge (HOME)», revisione 4643183, con 269 sfide." % (len(SFIDE) + len(SFIDE_CONTEGGIO), len(scoperte)),
            "",
            "| Sfida | Nascosta | Stato |",
            "|---|---|---|",
        ]
        with open(uscita, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(testa + righe) + "\n")
        print("Scritto " + os.path.relpath(uscita, RADICE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
