#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enumera le specie con differenze di sesso visibili, dalla pagina di Bulbapedia salvata su disco.

Perche' questa enumerazione serve
---------------------------------
Il foglio comunitario del living dex distingue i due sessi come voci separate e ne da' il conto, cioe'
centotre specie, ma un conto non e' una enumerazione: per portare quelle voci nella nostra lista di
spunta occorre sapere quali siano, e il campo della forma del formato di gioco non le separa, quindi
il dato non si ricava dalle tabelle del verificatore. La pagina di Bulbapedia dedicata alle
differenze di sesso e' la fonte che le nomina una per una, ed e' di secondo livello: la si usa per
enumerare, non per decidere.

Il presidio che questo programma porta, e perche' esiste
-------------------------------------------------------
Una pagina di enciclopedia si presta a essere letta a occhio e riassunta, e cosi' si sbaglia il
conto senza accorgersene: la prima lettura a espressioni regolari di questa stessa pagina produceva
centoquattro specie contro le centodue che la pagina stessa dichiara, perche' raccoglieva anche i
collegamenti che stanno dentro il testo di una descrizione, per esempio Espurr nominato nella riga
di Meowstic. Il programma quindi non si fida della propria estrazione: ogni sezione di generazione
dichiara in prosa quante specie contenga, e l'estrazione viene confrontata con quel numero. Se i due
non concordano il programma lo riferisce come discordanza invece di scrivere un documento che
sembrerebbe misurato.

Il riconoscimento di una riga poggia sul numero di catalogo a quattro cifre che la precede, che e'
la parte piu' stabile della pagina: una riga di tabella e' la coppia fra quel numero e il nome che
lo segue, mentre un nome citato dentro una descrizione non ha alcun numero davanti.

Il caso che non e' una specie, e va tenuto fuori dal conto
---------------------------------------------------------
La pagina aggiunge in prosa, fuori tabella, che la forma di Hisui di Sneasel ha una differenza di
sesso. Non e' una riga e non e' una specie in piu': e' una forma di una specie che nella medesima
pagina non compare fra le righe. Il programma la riferisce a parte, perche' per la nostra lista e'
una voce che nasce sull'asse delle forme e non su quello delle specie.

Uso
---
    python tools/enumera-differenze-sesso.py
    python tools/enumera-differenze-sesso.py --check
    python tools/enumera-differenze-sesso.py --self-test
"""

import argparse
import html
import io
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTE = os.path.join(RADICE, "_notes", "fonti", "2026-09-08-bulbapedia-differenze-di-sesso.html")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "DIFFERENZE-DI-SESSO.md")
NORMALIZZATO = os.path.join(RADICE, "pokedex-home-completo", "differenze-di-sesso.csv")

# I numerali che la pagina scrive in parola invece che in cifra sulle generazioni con poche voci.
NUMERALI = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
            "eight": 8, "nine": 9, "ten": 10}


def in_chiaro(frammento):
    """Il testo di un frammento di HTML, senza marcatori e con le entita' risolte."""
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", frammento))).strip()


def sezione_elenco(pagina):
    """La sola parte della pagina che porta l'elenco, cioe' fra le due intestazioni che lo chiudono.

    Restringere prima di estrarre non e' un ottimizzazione ma un presidio: la pagina nomina altrove
    decine di specie, per esempio nelle sezioni sull'animazione, e senza questo taglio finirebbero
    nell'enumerazione.
    """
    inizio = pagina.find('id="List_of_Pok')
    fine = pagina.find('id="In_the_Pok')
    if inizio < 0 or fine < 0 or fine <= inizio:
        return None
    return pagina[inizio:fine]


def dichiarato(testo):
    """Quante specie la prosa di una sezione dichiari, oppure None se non lo dichiara."""
    # La pagina alterna il plurale e il singolare, e sulla generazione con una sola voce scrive "with
    # a gender difference": senza l'articolo facoltativo quella sezione risultava non dichiarata, e
    # il totale dichiarato veniva riferito piu' basso di uno.
    m = re.search(r"There (?:are|is) (?:only )?(\d+|[a-z]+) Generation [IVX]+ Pok.mon with (?:a )?gender difference",
                  testo)
    if not m:
        return None
    quante = m.group(1)
    if quante.isdigit():
        return int(quante)
    return NUMERALI.get(quante.lower())


def estrai(sezione):
    """Le specie per generazione, con il numero dichiarato accanto a quello contato.

    Ogni voce e' la terna fra il numero di catalogo, il nome e la differenza descritta, e l'ordine
    e' quello della pagina, che e' l'ordine di catalogo.
    """
    blocchi = re.split(r'id="(Generation_[IVX]+)"', sezione)
    generazioni = []
    for i in range(1, len(blocchi), 2):
        nome, corpo = blocchi[i].replace("Generation_", ""), blocchi[i + 1]
        piano = in_chiaro(corpo)
        voci = []
        # La descrizione puo' essere lunga e contenere cifre, quindi il taglio non lo fa un divieto
        # di cifre ma il fatto che il quantificatore sia pigro e si fermi al primo numero di
        # catalogo successivo. Il tetto e' generoso perche' su Frillish e Basculegion la
        # descrizione supera i trecento caratteri, e un tetto stretto faceva perdere la riga
        # intera invece di troncarla.
        for m in re.finditer(r"(\d{4}) ([A-Z][A-Za-z'\. ]{2,20}?) ([A-Z].{5,1200}?)(?=(?: \d{4} )|$)",
                             piano):
            voci.append((int(m.group(1)), m.group(2).strip(), m.group(3).strip()))
        specie, forme = separa_forme(voci)
        generazioni.append({
            "generazione": nome,
            "voci": specie,
            "forme": forme,
            "dichiarato": dichiarato(piano),
        })
    return generazioni


def separa_forme(voci):
    """Le righe di specie da un lato, quelle di una forma regionale dall'altro.

    La tabella della seconda generazione porta due righe con il medesimo numero di catalogo, cioe'
    Sneasel e la sua forma di Hisui, e sommarle darebbe ventitre specie dove la pagina dichiara
    ventidue. La regola e' quindi che la prima riga di un numero e' la specie e ogni riga successiva
    con quel numero e' una forma di essa, che nella nostra lista nasce sull'asse delle forme.
    """
    specie, forme, visti = [], [], set()
    for dex, nome, differenza in voci:
        if dex in visti:
            forme.append((dex, nome, differenza))
        else:
            visti.add(dex)
            specie.append((dex, nome, differenza))
    return specie, forme


def forme_fuori_tabella(sezione):
    """Le differenze che la pagina aggiunge in prosa e non come riga, cioe' le forme."""
    trovate = []
    for m in re.finditer(r"Additionally, ([A-Z][A-Za-z'\.]+) 's ([A-Za-z ]+form)", in_chiaro(sezione)):
        trovate.append((m.group(1), m.group(2)))
    return trovate


def componi(generazioni, forme, discordanze):
    r = ["# Le specie con differenze di sesso visibili", ""]
    r.append("> Documento generato da `tools/enumera-differenze-sesso.py` dalla pagina di Bulbapedia salvata in `_notes/fonti/`. Non si modifica a mano: si rigenera. La fonte e' di secondo livello e serve a enumerare, non a decidere: il conto che il progetto adotta resta quello del foglio comunitario, e questo documento dice quali siano le specie che quel conto conta.")
    r.append("")
    contate = sum(len(g["voci"]) for g in generazioni)
    somma_dichiarata = sum(g["dichiarato"] for g in generazioni if g["dichiarato"] is not None)
    r.append("Le specie estratte sono %d e la pagina ne dichiara %d nella prosa delle sue sezioni. %s"
             % (contate, somma_dichiarata,
                "I due numeri concordano su tutte le generazioni."
                if not discordanze else
                "I due numeri NON concordano su %d generazioni, elencate in coda: dove discordano vale il numero dichiarato, e l'estrazione va corretta prima di usare questo documento come misura."
                % len(discordanze)))
    r.append("")
    if forme:
        r.append("La pagina aggiunge fuori tabella %s, che non e' una specie in piu' ma una voce sull'asse delle forme: %s."
                 % ("una differenza" if len(forme) == 1 else "%d differenze" % len(forme),
                    "; ".join("%s nella sua %s" % (n, f) for n, f in forme)))
        r.append("")
    righe_forma = [(g["generazione"], v) for g in generazioni for v in g.get("forme", [])]
    if righe_forma:
        r.append("Dentro le tabelle ci sono inoltre %d righe che ripetono un numero di catalogo gia' presente: sono forme regionali e non specie, e vanno sull'asse delle forme come la precedente. Sono %s."
                 % (len(righe_forma),
                    "; ".join("%04d nella generazione %s" % (v[0], gen) for gen, v in righe_forma)))
        r.append("")
    for g in generazioni:
        r.append("## Generazione %s" % g["generazione"])
        r.append("")
        r.append("Voci estratte %d, dichiarate %s."
                 % (len(g["voci"]),
                    g["dichiarato"] if g["dichiarato"] is not None else "non dichiarate"))
        r.append("")
        r.append("| Dex | Specie | Differenza descritta dalla fonte |")
        r.append("|---|---|---|")
        for dex, nome, differenza in g["voci"]:
            r.append("| %04d | %s | %s |" % (dex, nome, differenza.replace("|", "/")[:220]))
        r.append("")
    if discordanze:
        r.append("## Discordanze fra estrazione e dichiarazione")
        r.append("")
        r.append("| Generazione | Estratte | Dichiarate |")
        r.append("|---|---|---|")
        for g in discordanze:
            r.append("| %s | %d | %s |" % (g["generazione"], len(g["voci"]), g["dichiarato"]))
        r.append("")
    return "\n".join(r) + "\n"


def normalizza(generazioni):
    r = ["generazione,dex,specie,differenza"]
    for g in generazioni:
        for dex, nome, differenza in g["voci"]:
            campi = [g["generazione"], "%04d" % dex, nome, differenza]
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

    prova("le entita' vengono risolte", "Pokemon &", in_chiaro("<b>Pokemon</b> &amp;"))
    prova("una cifra dichiarata", 23, dichiarato("There are 23 Generation I Pokemon with gender differences"))
    prova("un numerale in parola", 3, dichiarato("There are three Generation V Pokemon with gender differences"))
    prova("una prosa che non dichiara", None, dichiarato("Questa sezione non dichiara nulla"))

    finta = ('id="List_of_Pok"> id="Generation_I"> There are 2 Generation I Pokemon with gender '
             'differences 0003 Venusaur Female has a visible gynoecium 0025 Pikachu Female tail '
             'ends in a heart id="In_the_Pok">')
    sezione = sezione_elenco(finta)
    prova("la sezione viene ritagliata", True, sezione is not None and "In_the_Pok" not in sezione)
    generazioni = estrai(sezione)
    prova("una generazione sola", 1, len(generazioni))
    prova("due voci estratte", 2, len(generazioni[0]["voci"]))
    prova("il numero di catalogo", 3, generazioni[0]["voci"][0][0])
    prova("il nome", "Venusaur", generazioni[0]["voci"][0][1])
    prova("la differenza", True, "gynoecium" in generazioni[0]["voci"][0][2])
    prova("e concorda col dichiarato", 2, generazioni[0]["dichiarato"])

    # Controllo negativo, ed e' il difetto che ha motivato il presidio: un nome citato dentro una
    # descrizione, senza numero di catalogo davanti, non deve entrare nell'enumerazione.
    finta = ('id="List_of_Pok"> id="Generation_VI"> There is one Generation VI Pokemon with gender '
             'differences 0678 Meowstic The moves Espurr can learn vary by gender id="In_the_Pok">')
    voci = estrai(sezione_elenco(finta))[0]["voci"]
    prova("il nome citato in descrizione non entra", 1, len(voci))
    prova("e la voce e' quella giusta", "Meowstic", voci[0][1])

    # Una pagina senza le due intestazioni non si legge a meta': si rifiuta.
    prova("una pagina senza elenco viene rifiutata", None, sezione_elenco("<p>niente</p>"))

    forme = forme_fuori_tabella("Additionally, Sneasel 's Hisuian form , introduced in Legends")
    prova("la forma fuori tabella viene riconosciuta", [("Sneasel", "Hisuian form")], forme)

    # Il numero di catalogo ripetuto e' una forma e non una specie: e' il caso di Sneasel, che
    # senza questa separazione portava la seconda generazione a ventitre contro le ventidue
    # dichiarate.
    specie, righe = separa_forme([(215, "Sneasel", "orecchio"), (215, "Hisuian", "Sneasel orecchio"),
                                  (217, "Ursaring", "pelo")])
    prova("le specie sono due", 2, len(specie))
    prova("la riga ripetuta finisce fra le forme", 1, len(righe))
    prova("ed e' quella col numero ripetuto", 215, righe[0][0])
    prova("l'ordine delle specie resta quello di catalogo", [215, 217], [v[0] for v in specie])

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="non scrive: dice soltanto se i documenti sul disco siano allineati")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    if not os.path.exists(FONTE):
        print("rifiutato: manca la pagina salvata in " + FONTE)
        return 1
    pagina = io.open(FONTE, encoding="utf-8", errors="replace").read()
    sezione = sezione_elenco(pagina)
    if sezione is None:
        print("rifiutato: la pagina non porta le due intestazioni che delimitano l'elenco")
        return 1
    generazioni = estrai(sezione)
    forme = forme_fuori_tabella(sezione)
    discordanze = [g for g in generazioni
                   if g["dichiarato"] is not None and len(g["voci"]) != g["dichiarato"]]

    testo = componi(generazioni, forme, discordanze)
    csv = normalizza(generazioni)
    if a.check:
        disallineati = [p for p, atteso in ((USCITA, testo), (NORMALIZZATO, csv))
                        if (io.open(p, encoding="utf-8").read() if os.path.exists(p) else "") != atteso]
        for p in disallineati:
            print("disallineato: %s va rigenerato" % p)
        if disallineati:
            return 1
        print("allineati: %s e %s" % (USCITA, NORMALIZZATO))
        return 0

    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    io.open(NORMALIZZATO, "w", encoding="utf-8", newline="\n").write(csv)
    contate = sum(len(g["voci"]) for g in generazioni)
    dichiarate = sum(g["dichiarato"] for g in generazioni if g["dichiarato"] is not None)
    print("scritti %s e %s" % (USCITA, NORMALIZZATO))
    print("  specie estratte %d, dichiarate dalla fonte %d" % (contate, dichiarate))
    for g in discordanze:
        print("  DISCORDANZA generazione %s: estratte %d, dichiarate %d"
              % (g["generazione"], len(g["voci"]), g["dichiarato"]))
    for n, f in forme:
        print("  fuori tabella: %s nella sua %s" % (n, f))
    return 0


if __name__ == "__main__":
    sys.exit(main())
