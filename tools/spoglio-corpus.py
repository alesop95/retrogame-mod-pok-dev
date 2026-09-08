#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legge tutto un corpus scaricato e dice che cosa esso nomina e noi non abbiamo.

Perché esiste
-------------
L'utente ha chiesto che le fonti del corpus si leggano tutte, e ha ragione sul perché: sono il
controllo incrociato più ampio disponibile sullo scopo del progetto. Leggerle una per una
sarebbe però il modo peggiore di farlo, per due ragioni che non sono di comodo. La prima è che
sono trecento documenti e la lettura in sequenza non finisce. La seconda, più importante, è che
la lettura umana di trecento documenti non è più affidabile di una macchina proprio sulla cosa
che qui conta, cioè accorgersi che una specie o una mossa nominata in mezzo a un paragrafo non
compare nelle nostre enumerazioni.

Il metodo è quello già impiegato con successo sulle mosse perdute, e vale enunciarlo perché è
generale. Una fonte che elenca cose non si legge per crederle: si trasforma in un predicato e lo
si esegue sui propri dati. Il risultato non dipende dall'affidabilità della fonte per la parte
che conta, cioè che cosa noi possediamo, e dipende da essa soltanto per che cosa sia da cercare.

Che cosa fa, esattamente
------------------------
Riconosce dentro ogni documento del corpus le entità dei vocabolari chiusi del dominio, cioè i
nomi delle specie, delle mosse e dei fiocchi, letti dalle tabelle del verificatore e non
trascritti. Poi confronta l'insieme di ciò che il corpus nomina con l'insieme di ciò che i nostri
lotti contengono, e riferisce la differenza nei due versi.

La direzione che interessa è una sola e va detta: ciò che il corpus nomina e noi non abbiamo. La
direzione opposta, cioè ciò che abbiamo e nessuno nomina, non è un difetto e non si riferisce,
perché il corpus non pretende di essere completo.

Il riconoscimento è deliberatamente conservativo, e le sue due debolezze vanno dichiarate perché
si vedono nell'esito. I nomi brevi e ambigui producono falsi positivi, cioè una mossa che si
chiama come una parola comune viene riconosciuta dentro una frase che non parla di lei; per
questo i nomi di una sola parola corta sono esclusi dal riconoscimento delle mosse e dei fiocchi,
dove il vocabolario ne ha molti. E un nome scritto in una lingua diversa da quella della tabella
non viene riconosciuto affatto, quindi il corpus in italiano o giapponese resta invisibile a
questo strumento, che lavora sui nomi inglesi perché il corpus è in inglese.

Uso
---
    python tools/spoglio-corpus.py --corsa _notes/fonti/reddit-pokemonhome-1vtj5hf-2026-09-08
    python tools/spoglio-corpus.py --corsa <cartella> --out pokedex-home-completo/SPOGLIO-CORPUS.md
    python tools/spoglio-corpus.py --self-test
"""

import argparse
import collections
import glob
import io
import os
import re
import struct
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))

TESTI = os.path.join("PKHeX.Core", "Resources", "text", "other", "en")

# I nomi troppo corti o troppo comuni per essere riconosciuti dentro una frase senza produrre
# falsi positivi. Non e' una lista di eccezioni ma un criterio: sotto questa soglia un nome
# inglese di una parola sola coincide quasi sempre con una parola comune.
LUNGHEZZA_MINIMA = 7

# I nomi che superano la soglia e restano comunque ambigui, esclusi uno per uno perche' ciascuno
# ha una ragione propria. Vanno tenuti pochi: una lista che cresce e' il segno che il criterio
# sopra e' sbagliato e va cambiato, non allungata.
AMBIGUI = frozenset([
    "Transform", "Nightmare", "Frustration", "Recover", "Present", "Confide", "Celebrate",
    "Sketch", "Splash", "Rollout", "Bestow", "Captivate", "Foresight", "Refresh", "Snatch",
    "Powder", "Spotlight", "Charge", "Wish", "Trick", "Growth", "Attract", "Disable",
])


def carica_nomi(pkhex, file_):
    """I nomi di un vocabolario, dalla tabella del verificatore.

    Due formati convivono in quella cartella e confonderli produce un vocabolario che non
    riconosce nulla senza dirlo: gli elenchi indicizzati per numero, come le specie e le mosse,
    hanno un nome per riga; quelli indicizzati per chiave, come i fiocchi, hanno la chiave e il
    nome separati da una tabulazione. Nel secondo caso il nome e' il secondo campo, e prendere la
    riga intera significa cercare nel testo una stringa che nel testo non compare mai.
    """
    percorso = os.path.join(pkhex, TESTI, file_)
    righe = io.open(percorso, encoding="utf-8-sig").read().splitlines()
    return [(r.split("\t", 1)[1] if "\t" in r else r).strip() for r in righe]


def vocabolario(nomi, minima=0, escludi=frozenset()):
    """Il vocabolario riconoscibile, con l'espressione che lo cerca.

    Si scarta il vuoto, i segnaposto e cio' che e' troppo corto o ambiguo. L'espressione richiede
    un confine di parola ai due estremi, cosicche' un nome non venga riconosciuto dentro un altro.
    """
    buoni = {}
    for i, n in enumerate(nomi):
        if not n or n.startswith("---") or n in escludi:
            continue
        if len(n) < minima:
            continue
        buoni[n] = i
    if not buoni:
        return {}, None
    # L'ordine per lunghezza decrescente conta: cosi' il nome piu' lungo vince quando due si
    # sovrappongono, per esempio la forma regionale rispetto alla specie che la contiene.
    schema = "|".join(re.escape(n) for n in sorted(buoni, key=len, reverse=True))
    return buoni, re.compile(r"(?<![A-Za-z])(" + schema + r")(?![A-Za-z])")


def vocabolario_fiocchi(nomi):
    """Il vocabolario dei fiocchi, che si cerca in coppia con la parola che lo qualifica.

    Restituisce la stessa forma di `vocabolario`, cioe' il dizionario dal nome all'indice e
    l'espressione, ma l'espressione cattura il solo nome dentro una coppia. Le due forme che il
    testo inglese usa sono il nome seguito dalla parola e la parola seguita dal nome, e vanno
    accettate entrambe perche' convivono nella stessa pagina.
    """
    buoni = {}
    for i, n in enumerate(nomi):
        if not n or n.startswith("---") or len(n) < 4:
            continue
        buoni.setdefault(n, i)
    if not buoni:
        return {}, None
    schema = "|".join(re.escape(n) for n in sorted(buoni, key=len, reverse=True))
    return buoni, re.compile(
        r"(?<![A-Za-z])(?:(" + schema + r")\s+Ribbons?|Ribbons?\s+(" + schema + r"))"
        r"(?![A-Za-z])", re.IGNORECASE)


def documenti(cartella):
    """Ogni documento scaricato della corsa, come coppia di percorso relativo e testo."""
    fuori = []
    for pat in ("posts/*.md", "esterni/*/*.md"):
        for f in sorted(glob.glob(os.path.join(cartella, pat))):
            rel = os.path.relpath(f, cartella).replace("\\", "/")
            try:
                fuori.append((rel, io.open(f, encoding="utf-8", errors="replace").read()))
            except OSError:
                continue
    return fuori


def nostre_specie(pkhex):
    """Le specie che i nostri lotti contengono, come insieme di numeri nazionali."""
    from pokebridge import gen3  # noqa: E402
    fuori = set()
    for f in glob.glob(os.path.join(RADICE, "_notes", "lotto-gen5", "*.pk5")):
        fuori.add(struct.unpack_from("<H", open(f, "rb").read(), 0x08)[0])
    for f in glob.glob(os.path.join(RADICE, "_notes", "lotto-gen4", "*.pk4")):
        fuori.add(struct.unpack_from("<H", open(f, "rb").read(), 0x08)[0])
    interne = set()
    for pat in ("lotto-eventi/*.pk3", "lotto-incontri-gen3/*.pk3"):
        for f in glob.glob(os.path.join(RADICE, "_notes", pat)):
            m = gen3.Gen3Mon.from_canonical_bytes(open(f, "rb").read(), party=False)
            interne.add(m.growth.species)
    return fuori, interne


def nostre_mosse():
    """Le mosse che i nostri lotti contengono, come insieme di identificativi."""
    from pokebridge import gen3  # noqa: E402
    fuori = set()
    for pat, off in (("lotto-gen5/*.pk5", 0x28), ("lotto-gen4/*.pk4", 0x28)):
        for f in glob.glob(os.path.join(RADICE, "_notes", pat)):
            d = open(f, "rb").read()
            for i in range(4):
                fuori.add(struct.unpack_from("<H", d, off + 2 * i)[0])
    for pat in ("lotto-eventi/*.pk3", "lotto-incontri-gen3/*.pk3"):
        for f in glob.glob(os.path.join(RADICE, "_notes", pat)):
            m = gen3.Gen3Mon.from_canonical_bytes(open(f, "rb").read(), party=False)
            fuori.update(m.attacks.moves)
    fuori.discard(0)
    return fuori


def spoglia(cartella, pkhex):
    specie_nomi = carica_nomi(pkhex, "text_Species_en.txt")
    mosse_nomi = carica_nomi(pkhex, "text_Moves_en.txt")
    fiocchi_nomi = carica_nomi(pkhex, "text_Ribbons_en.txt")

    voc_specie, re_specie = vocabolario(specie_nomi, minima=4)
    voc_mosse, re_mosse = vocabolario(mosse_nomi, minima=LUNGHEZZA_MINIMA, escludi=AMBIGUI)
    # I fiocchi hanno nomi che sono parole comuni, come Speciale, Abilita' o Vittoria, e cercarli
    # nudi produce quasi solo falsi positivi: nel primo giro le quattro voci piu' citate erano
    # tutte occorrenze di quelle parole in frasi che di fiocchi non parlavano. Il rimedio non e'
    # allungare la lista degli ambigui ma cambiare cio' che si cerca: nel testo un fiocco compare
    # sempre accanto alla parola che lo qualifica, quindi si cerca la coppia e non il nome.
    voc_fiocchi, re_fiocchi = vocabolario_fiocchi(fiocchi_nomi)

    trovate = {"specie": collections.defaultdict(set),
               "mosse": collections.defaultdict(set),
               "fiocchi": collections.defaultdict(set)}
    docs = documenti(cartella)
    for rel, testo in docs:
        # L'intestazione che il lettore scrive in cima a ogni file non e' contenuto della fonte e
        # nomina cose nostre: si taglia, altrimenti ogni documento sembrerebbe nominarle.
        i = testo.find("\n## ")
        corpo = testo[i:] if i > 0 else testo
        for chiave, espr, voc in (("specie", re_specie, voc_specie),
                                  ("mosse", re_mosse, voc_mosse),
                                  ("fiocchi", re_fiocchi, voc_fiocchi)):
            if espr is None:
                continue
            for m in set(espr.findall(corpo)):
                # Un'espressione con piu' gruppi rende tuple: il nome e' il solo gruppo non
                # vuoto, e appiattirlo qui evita di avere due rami di lettura piu' sotto.
                if isinstance(m, tuple):
                    m = next((x for x in m if x), "")
                if not m:
                    continue
                if m not in voc:
                    # La ricerca dei fiocchi non distingue le maiuscole, quindi il nome catturato
                    # puo' differire per grafia da quello della tabella: si riporta alla tabella.
                    per_minuscolo = {k.lower(): k for k in voc}
                    m = per_minuscolo.get(m.lower())
                    if m is None:
                        continue
                trovate[chiave][voc[m]].add(rel)
    return {"documenti": len(docs), "trovate": trovate,
            "nomi": {"specie": specie_nomi, "mosse": mosse_nomi, "fiocchi": fiocchi_nomi}}


def rapporto(s, pkhex):
    fuori_nostre, interne = nostre_specie(pkhex)
    mosse_nostre = nostre_mosse()
    nomi = s["nomi"]
    t = s["trovate"]

    r = ["# Spoglio del corpus: che cosa le fonti nominano e noi non abbiamo", ""]
    r.append("> Documento generato da `tools/spoglio-corpus.py`. Non si modifica a mano: si "
             "rigenera. Nasce dalla richiesta di leggere tutte le fonti del corpus come controllo "
             "incrociato, eseguita con il metodo del predicato invece che con la lettura in "
             "sequenza.")
    r.append("")
    r.append("Sono stati spogliati %d documenti scaricati. Il riconoscimento e' sui vocabolari "
             "chiusi del dominio, cioe' i nomi inglesi di specie, mosse e fiocchi letti dalle "
             "tabelle del verificatore. Due limiti vanno dichiarati perche' si vedono nell'esito: "
             "i nomi corti o ambigui sono esclusi per non produrre falsi positivi, e un nome "
             "scritto in una lingua diversa dall'inglese non viene riconosciuto affatto."
             % s["documenti"])
    r.append("")
    r.append("La direzione che interessa e' una sola, cioe' cio' che il corpus nomina e i nostri "
             "lotti non contengono. La direzione opposta non e' un difetto e non si riferisce, "
             "perche' il corpus non pretende di essere completo.")
    r.append("")

    # Specie.
    citate = sorted(t["specie"])
    assenti = [i for i in citate if i not in fuori_nostre and i not in interne]
    r.append("## Specie")
    r.append("")
    r.append("Il corpus nomina %d specie distinte. I nostri lotti ne contengono %d, e %d delle "
             "nominate non vi compaiono. L'assenza non e' di per se' una lacuna, perche' un lotto "
             "di distribuzioni non ha ragione di contenere ogni specie del gioco: e' una lista di "
             "controllo, e le voci che pesano sono quelle che compaiono in molti documenti."
             % (len(citate), len(fuori_nostre | interne), len(assenti)))
    r.append("")
    r.append("| Specie | Documenti che la nominano | Uno dei documenti |")
    r.append("|---|---|---|")
    for i in sorted(assenti, key=lambda k: (-len(t["specie"][k]), nomi["specie"][k]))[:120]:
        dove = sorted(t["specie"][i])
        r.append("| %s | %d | %s |" % (nomi["specie"][i], len(dove), dove[0]))
    r.append("")

    # Mosse.
    citate_m = sorted(t["mosse"])
    assenti_m = [i for i in citate_m if i not in mosse_nostre]
    r.append("## Mosse")
    r.append("")
    r.append("Il corpus nomina %d mosse distinte fra quelle riconoscibili. I nostri lotti ne "
             "contengono %d, e %d delle nominate non vi compaiono."
             % (len(citate_m), len(mosse_nostre), len(assenti_m)))
    r.append("")
    r.append("| Mossa | Documenti | Uno dei documenti |")
    r.append("|---|---|---|")
    for i in sorted(assenti_m, key=lambda k: (-len(t["mosse"][k]), nomi["mosse"][k]))[:80]:
        dove = sorted(t["mosse"][i])
        r.append("| %s | %d | %s |" % (nomi["mosse"][i], len(dove), dove[0]))
    r.append("")

    # Fiocchi.
    r.append("## Fiocchi")
    r.append("")
    r.append("Il corpus nomina %d fiocchi distinti. Il progetto non ha ancora un'enumerazione "
             "dell'asse dei fiocchi, quindi qui non c'e' un confronto ma un elenco, ed e' il "
             "materiale di partenza per costruirla." % len(t["fiocchi"]))
    r.append("")
    r.append("| Fiocco | Documenti | Uno dei documenti |")
    r.append("|---|---|---|")
    for i in sorted(t["fiocchi"], key=lambda k: (-len(t["fiocchi"][k]), nomi["fiocchi"][k])):
        dove = sorted(t["fiocchi"][i])
        r.append("| %s | %d | %s |" % (nomi["fiocchi"][i], len(dove), dove[0]))
    return "\n".join(r) + "\n"


def self_test():
    esiti = []

    def prova(nome, cond, det=""):
        esiti.append((nome, bool(cond), det))

    nomi = ["", "Bulbasaur", "Mew", "Ho-Oh", "Farfetch'd", "---", "Charizard"]
    voc, espr = vocabolario(nomi, minima=4)
    prova("il vuoto e i segnaposto non entrano nel vocabolario",
          "" not in voc and "---" not in voc, str(sorted(voc)))
    prova("i nomi troppo corti restano fuori", "Mew" not in voc, str(sorted(voc)))
    prova("un nome con trattino o apostrofo entra",
          "Ho-Oh" in voc and "Farfetch'd" in voc, str(sorted(voc)))
    prova("il riconoscimento trova il nome dentro una frase",
          espr.findall("I traded my Bulbasaur today") == ["Bulbasaur"], "")
    prova("negativo: non lo trova dentro un'altra parola",
          espr.findall("Bulbasaurus") == [], str(espr.findall("Bulbasaurus")))

    # Il nome piu' lungo vince quando due si sovrappongono.
    voc2, espr2 = vocabolario(["Charizard", "Charizard-Mega-X"], minima=4)
    prova("fra due nomi sovrapposti vince il piu' lungo",
          espr2.findall("a Charizard-Mega-X here") == ["Charizard-Mega-X"],
          str(espr2.findall("a Charizard-Mega-X here")))

    # Il taglio dell'intestazione, che e' il presidio contro l'autoriconoscimento.
    testo = "riga di intestazione con Bulbasaur dentro\n## Corpo\nqui c'e' Charizard\n"
    i = testo.find("\n## ")
    prova("l'intestazione del lettore si taglia prima di spogliare",
          "Bulbasaur" not in testo[i:], testo[i:][:40])

    # I due formati della cartella dei testi, che confonderli rende un vocabolario cieco.
    import tempfile
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, TESTI))
    io.open(os.path.join(d, TESTI, "prova.txt"), "w", encoding="utf-8").write(
        "RibbonChampionKalos\tKalos Champion\nRibbonEffort\tEffort\n")
    letti = carica_nomi(d, "prova.txt")
    prova("dalla tabella a due campi si prende il nome e non la chiave",
          letti == ["Kalos Champion", "Effort"], str(letti))
    io.open(os.path.join(d, TESTI, "prova2.txt"), "w", encoding="utf-8").write(
        "Bulbasaur\nIvysaur\n")
    prova("dalla tabella a un campo si prende la riga",
          carica_nomi(d, "prova2.txt") == ["Bulbasaur", "Ivysaur"], "")

    prova("gli ambigui sono pochi", len(AMBIGUI) < 40, str(len(AMBIGUI)))

    larghezza = max(len(n) for n, _, _ in esiti)
    for nome, ok, det in esiti:
        print("  %-*s  %s%s" % (larghezza, nome, "ok" if ok else "FALLITO",
                                ("  " + det) if (det and not ok) else ""))
    caduti = [n for n, ok, _ in esiti if not ok]
    print("")
    print("%d prove, %d fallite." % (len(esiti), len(caduti)))
    return 1 if caduti else 0


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--corsa")
    p.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "pkhex"))
    p.add_argument("--out", default=os.path.join("pokedex-home-completo", "SPOGLIO-CORPUS.md"))
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()

    if a.self_test:
        return self_test()
    if not a.corsa:
        p.error("serve --corsa con la cartella di una corsa del lettore di Reddit")

    s = spoglia(a.corsa, a.pkhex)
    testo = rapporto(s, a.pkhex)
    io.open(a.out, "w", encoding="utf-8", newline="\n").write(testo)
    print("%d documenti spogliati; specie %d, mosse %d, fiocchi %d nominati; rapporto in %s"
          % (s["documenti"], len(s["trovate"]["specie"]), len(s["trovate"]["mosse"]),
             len(s["trovate"]["fiocchi"]), a.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
