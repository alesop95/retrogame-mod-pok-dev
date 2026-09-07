#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confronta l'enumerazione del progetto con il foglio comunitario del living dex.

Perche' un confronto e non una fusione
--------------------------------------
Il foglio mantenuto dalla comunita' e la nostra enumerazione contano la stessa cosa in due modi
diversi, e la tentazione naturale e' fonderli prendendo il massimo. Sarebbe l'errore: due misure
indipendenti valgono in quanto indipendenti, e mescolarle distrugge proprio l'informazione per cui
si e' cercata la seconda. Questo programma quindi non fonde nulla. Mette le due enumerazioni una
accanto all'altra, specie per specie, e riferisce dove divergono e di quanto.

Le divergenze non sono tutte dello stesso genere, ed e' il punto per cui il confronto vale il suo
costo. Una divergenza in cui il foglio conta di piu' indica di norma una nostra cecita', perche' il
foglio enumera categorie che il campo della forma non separa, cioe' le differenze di sesso e le
varianti puramente cromatiche. Una divergenza in cui contiamo di piu' noi indica di norma un nostro
rumore, perche' leggiamo il numero di forme dalla tabella del gioco e quel numero comprende
posizioni che non sono oggetti distinti da possedere. Le due direzioni vanno quindi lette in modo
diverso, e il documento le separa invece di sommarle in un unico scarto.

Che cosa questo programma non decide
------------------------------------
Non decide chi abbia ragione. Una divergenza resta una divergenza finche' una persona non la
risolve con un argomento, e il documento la registra come tale. La sola cosa che il programma
stabilisce da se' e' la classificazione della divergenza nelle due direzioni, che e' meccanica.

Uso
---
    python tools/confronta-foglio-livingdex.py
    python tools/confronta-foglio-livingdex.py --check
    python tools/confronta-foglio-livingdex.py --self-test
"""

import argparse
import io
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOGLIO = os.path.join(RADICE, "_notes", "spreadsheets e passaggi home",
                      "LivingDex Spreadsheet.xlsx")
NOSTRA = os.path.join(RADICE, "pokedex-home-completo", "CHECKLIST-COMPLETA.md")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "CONFRONTO-FOGLIO-LIVINGDEX.md")
NORMALIZZATO = os.path.join(RADICE, "pokedex-home-completo", "foglio-livingdex.csv")

SCHEDA = "Living Dex"
PRIMA_RIGA = 3          # le prime due righe sono intestazione a due livelli
COL_DEX = 6
COL_NOME = 7
COL_SESSO = 10
COL_GMAX = 11
COL_FORMA = 12
COL_COMMENTO = 13
COL_REGIONE = 14

MAX_SPECIE = 1025

# La dicitura con cui la nostra lista marca le forme che ADR-035 ha deciso di perseguire come
# oggetti. Le altre due diciture, cioe' sola battaglia e totemica, marcano posizioni che nel
# deposito non possono esistere e restano fuori dal confronto per costruzione.
CONSERVABILE = "indeterminato"


def leggi_foglio(percorso):
    """Le voci del foglio comunitario, normalizzate in tuple.

    La lettura richiede openpyxl, che e' l'unica dipendenza esterna di questo strumento. Se manca,
    il programma lo dice invece di fallire con un errore di importazione, perche' una dipendenza
    assente e' una condizione dell'ambiente e non un difetto del dato.
    """
    try:
        import openpyxl
    except ImportError:
        return None, "manca openpyxl: si installa con `pip install openpyxl`"
    if not os.path.exists(percorso):
        return None, "manca il foglio in " + percorso
    libro = openpyxl.load_workbook(percorso, data_only=True)
    if SCHEDA not in libro.sheetnames:
        return None, "il foglio non ha la scheda '%s'" % SCHEDA
    voci = []
    for riga in libro[SCHEDA].iter_rows(min_row=PRIMA_RIGA, values_only=True):
        if not riga[COL_NOME] or riga[COL_DEX] is None:
            continue
        voci.append({
            "dex": int(riga[COL_DEX]),
            "nome": str(riga[COL_NOME]).strip(),
            "sesso": (riga[COL_SESSO] or "").strip(),
            "gmax": bool(riga[COL_GMAX]),
            "forma": str(riga[COL_FORMA] or "").strip(),
            "commento": str(riga[COL_COMMENTO] or "").strip().replace("\n", " "),
            "regione": str(riga[COL_REGIONE] or "").strip(),
        })
    return voci, None


def leggi_nostra(percorso):
    """Il conto delle nostre voci conservabili per numero di catalogo.

    Una specie vale sempre una voce di base; a quella si sommano le sole forme che la nostra lista
    marca come conservabili, che sono quelle che ADR-035 ha deciso di perseguire come oggetti.
    """
    if not os.path.exists(percorso):
        return None, None, "manca la nostra lista in " + percorso
    testo = io.open(percorso, encoding="utf-8").read()
    if "## Voci di forma" not in testo:
        return None, None, "la nostra lista non ha la sezione delle voci di forma"
    sezione = testo.split("## Voci di forma")[1]
    forme, escluse = {}, {}
    for riga in sezione.split("\n"):
        if not riga.startswith("| `PKD-"):
            continue
        celle = [c.strip() for c in riga.split("|")]
        dex, natura = int(celle[2]), celle[6]
        if CONSERVABILE in natura:
            forme[dex] = forme.get(dex, 0) + 1
        else:
            escluse.setdefault(dex, []).append(natura)
    conto = {n: 1 + forme.get(n, 0) for n in range(1, MAX_SPECIE + 1)}
    return conto, escluse, None


def classifica(dex, loro, noi, voci_loro, escluse):
    """La direzione della divergenza, e l'indizio che la spiega.

    L'indizio non e' una diagnosi ma un puntatore: dice quale categoria del foglio o quale dicitura
    della nostra lista renda plausibile lo scarto, cosicche' chi lo risolve sappia dove guardare.
    """
    if loro == noi:
        return None, ""
    if loro > noi:
        sessi = {v["sesso"] for v in voci_loro if v["sesso"]}
        forme = {v["forma"] for v in voci_loro if v["forma"]}
        indizi = []
        if len(sessi) > 1:
            indizi.append("il foglio distingue i due sessi, che il campo della forma non separa")
        if forme:
            indizi.append("il foglio nomina %d forme: %s"
                          % (len(forme), ", ".join(sorted(forme))[:160]))
        return "foglio", "; ".join(indizi) or "nessun indizio leggibile dal foglio"
    diciture = escluse.get(dex, [])
    if diciture:
        return "nostra", ("la nostra lista scarta %d posizioni con la dicitura: %s"
                          % (len(diciture), diciture[0][:90]))
    return "nostra", ("la nostra lista conta %d posizioni di forma nella tabella del gioco che il "
                      "foglio non riconosce come oggetti distinti" % (noi - 1))


def componi(voci, conto, escluse):
    per_dex = {}
    for v in voci:
        per_dex.setdefault(v["dex"], []).append(v)
    loro = {n: len(per_dex.get(n, [])) for n in range(1, MAX_SPECIE + 1)}

    piu_foglio, piu_nostre, accordo = [], [], 0
    for n in range(1, MAX_SPECIE + 1):
        verso, indizio = classifica(n, loro[n], conto[n], per_dex.get(n, []), escluse)
        nome = per_dex.get(n, [{}])[0].get("nome", "?")
        if verso is None:
            accordo += 1
        elif verso == "foglio":
            piu_foglio.append((n, nome, loro[n], conto[n], indizio))
        else:
            piu_nostre.append((n, nome, conto[n], loro[n], indizio))

    r = []
    r.append("# Confronto fra la nostra enumerazione e il foglio comunitario del living dex")
    r.append("")
    r.append("> Documento generato da `tools/confronta-foglio-livingdex.py`. Non si modifica a "
             "mano: si rigenera. Non fonde le due enumerazioni e non decide chi abbia ragione; le "
             "mette una accanto all'altra e classifica le divergenze.")
    r.append("")
    r.append("Il foglio è mantenuto dalla comunità, deriva a sua volta da un foglio più antico di "
             "un altro utente, ed è stato consegnato a questo progetto il 2026-09-07. È registrato "
             "in `SOURCES.md` al quinto livello, che è quello dei materiali di community: "
             "accuratissimo o meno, la sua autorevolezza non è verificabile dall'esterno, e per "
             "questo vale come controprova indipendente e non come autorità.")
    r.append("")
    r.append("## Il conto delle due enumerazioni")
    r.append("")
    r.append("| Misura | Foglio | Nostra |")
    r.append("|---|---|---|")
    r.append("| voci totali da possedere | %d | %d |" % (sum(loro.values()), sum(conto.values())))
    r.append("| numeri di catalogo distinti | %d | %d |"
             % (len([n for n in loro if loro[n]]), MAX_SPECIE))
    r.append("| voci oltre la specie base | %d | %d |"
             % (sum(loro.values()) - MAX_SPECIE, sum(conto.values()) - MAX_SPECIE))
    r.append("| specie su cui le due concordano | %d | %d |" % (accordo, accordo))
    r.append("")
    r.append("Le due somme differiscono di %d voci, ma quel numero da solo inganna, perché è la "
             "differenza fra due scarti che vanno in versi opposti e si compensano in parte: il "
             "foglio conta più voci di noi su %d specie, per un totale di %d voci, e noi ne "
             "contiamo più del foglio su %d specie, per un totale di %d voci."
             % (abs(sum(loro.values()) - sum(conto.values())),
                len(piu_foglio), sum(x[2] - x[3] for x in piu_foglio),
                len(piu_nostre), sum(x[2] - x[3] for x in piu_nostre)))
    r.append("")
    r.append("## Dove il foglio conta più di noi, cioè dove siamo ciechi")
    r.append("")
    r.append("Sono %d specie. La causa prevalente è che il foglio enumera categorie che il campo "
             "della forma non separa: le differenze di sesso, che nei dati non sono una forma, e "
             "le varianti puramente cromatiche, che il gioco tiene in campi diversi da quello "
             "della forma." % len(piu_foglio))
    r.append("")
    r.append("| Dex | Specie | Foglio | Nostra | Indizio |")
    r.append("|---|---|---|---|---|")
    for n, nome, l, c, indizio in sorted(piu_foglio, key=lambda x: (-(x[2] - x[3]), x[0])):
        r.append("| %d | %s | %d | %d | %s |" % (n, nome, l, c, indizio))
    r.append("")
    r.append("## Dove contiamo più del foglio, cioè dove abbiamo rumore")
    r.append("")
    r.append("Sono %d specie. La causa prevalente è che leggiamo il numero di forme dalla tabella "
             "del gioco, e quel numero comprende posizioni che non sono oggetti distinti da "
             "possedere: forme che cambiano con un oggetto tenuto, posizioni di riempimento, e "
             "forme che una pre-evoluzione porta nei dati senza esibirle. Una divergenza in questa "
             "direzione non è però automaticamente un nostro errore, e almeno un caso va guardato "
             "in senso contrario, cioè le forme originarie di Dialga e Palkia, che sono oggetti "
             "distinti e conservabili." % len(piu_nostre))
    r.append("")
    r.append("| Dex | Specie | Nostra | Foglio | Indizio |")
    r.append("|---|---|---|---|---|")
    for n, nome, c, l, indizio in sorted(piu_nostre, key=lambda x: (-(x[2] - x[3]), x[0])):
        r.append("| %d | %s | %d | %d | %s |" % (n, nome, c, l, indizio))
    r.append("")
    r.append("## Le voci del foglio che portano una nota sull'ottenimento")
    r.append("")
    note = [v for v in voci if v["commento"]]
    r.append("Sono %d, e sono la parte del foglio che riguarda l'asse degli eventi invece di "
             "quello delle forme: dicono come si ottiene una voce che non si cattura." % len(note))
    r.append("")
    r.append("| Dex | Specie | Forma | Nota |")
    r.append("|---|---|---|---|")
    for v in sorted(note, key=lambda x: x["dex"]):
        r.append("| %d | %s | %s | %s |"
                 % (v["dex"], v["nome"], v["forma"] or "-", v["commento"][:300]))
    r.append("")
    return "\n".join(r) + "\n"


def normalizza(voci):
    """Il foglio in forma di testo tracciabile, cosicche' il confronto sia riproducibile senza il file binario."""
    r = ["dex,nome,sesso,gmax,forma,regione,commento"]
    for v in voci:
        campi = [str(v["dex"]), v["nome"], v["sesso"], "1" if v["gmax"] else "",
                 v["forma"], v["regione"], v["commento"]]
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

    prova("la dicitura delle forme conservabili", "indeterminato", CONSERVABILE)
    prova("il tetto delle specie", 1025, MAX_SPECIE)

    # La classificazione della direzione, che e' la sola cosa che il programma decide da se'.
    verso, indizio = classifica(1, 1, 1, [], {})
    prova("nessuna divergenza da' nessun verso", None, verso)
    verso, indizio = classifica(3, 2, 1, [{"sesso": "M", "forma": ""}, {"sesso": "F", "forma": ""}], {})
    prova("il foglio che conta di piu' punta al foglio", "foglio", verso)
    prova("e l'indizio nomina i due sessi", True, "due sessi" in indizio)
    verso, indizio = classifica(493, 1, 19, [], {})
    prova("noi che contiamo di piu' punta a noi", "nostra", verso)
    prova("e l'indizio nomina le posizioni della tabella", True, "tabella del gioco" in indizio)
    verso, indizio = classifica(978, 1, 2, [], {978: ["forma di sola battaglia: eccetera"]})
    prova("una dicitura di scarto entra nell'indizio", True, "sola battaglia" in indizio)

    # La normalizzazione protegge le virgole, altrimenti una nota le spezzerebbe in piu' campi.
    testo = normalizza([{"dex": 1, "nome": "Bulbasaur", "sesso": "", "gmax": False,
                         "forma": "", "regione": "Kanto", "commento": "uno, due"}])
    prova("la virgola dentro una nota viene protetta", True, '"uno, due"' in testo)
    prova("e la riga resta una sola", 2, len(testo.rstrip("\n").split("\n")))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="non scrive: dice soltanto se i documenti sul disco siano allineati")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    voci, errore = leggi_foglio(FOGLIO)
    if errore:
        print("rifiutato: " + errore)
        return 1
    conto, escluse, errore = leggi_nostra(NOSTRA)
    if errore:
        print("rifiutato: " + errore)
        return 1

    testo = componi(voci, conto, escluse)
    csv = normalizza(voci)
    if a.check:
        disallineati = []
        for percorso, atteso in ((USCITA, testo), (NORMALIZZATO, csv)):
            vecchio = io.open(percorso, encoding="utf-8").read() if os.path.exists(percorso) else ""
            if vecchio != atteso:
                disallineati.append(percorso)
        if disallineati:
            for p in disallineati:
                print("disallineato: %s va rigenerato" % p)
            return 1
        print("allineati: %s e %s" % (USCITA, NORMALIZZATO))
        return 0

    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    io.open(NORMALIZZATO, "w", encoding="utf-8", newline="\n").write(csv)
    print("scritti %s e %s" % (USCITA, NORMALIZZATO))
    print("  voci del foglio: %d | nostre: %d" % (len(voci), sum(conto.values())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
