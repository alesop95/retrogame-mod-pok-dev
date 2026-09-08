#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enumera l'asse dei fiocchi e misura che cosa i nostri lotti ne portano.

Perché esiste
-------------
Lo Studio 05 ha stabilito che gli assi della collezione sono almeno sei e non tre, e che i tre
nuovi sono indipendenti dai vecchi, nel senso preciso che una collezione completa sui primi può
essere vuota sui secondi. Delle mosse esiste ora una derivazione dai dati; dei fiocchi non
esisteva nulla, nemmeno un elenco. Questo strumento lo produce, e nello stesso passo misura la
copertura, perché enumerare senza misurare produce una lista che nessuno confronta con niente.

Perché si legge dal sorgente invece di trascrivere
--------------------------------------------------
Le posizioni dei fiocchi dentro l'esemplare sono ottanta coppie di byte e bit. Trascriverle a
mano è esattamente il difetto che questo progetto ha già pagato due volte, con la tabella dei
caratteri di quarta generazione e con la tabella dei punti potenza: una trascrizione lunga è un
difetto che aspetta, e sbaglia in un modo che nessun controllo interno rivela, perché un bit
letto nella posizione sbagliata dà comunque un valore booleano plausibile. Il programma legge
quindi le definizioni dal sorgente del verificatore e le compone, e se quel sorgente cambia il
nostro elenco cambia con esso.

Il nome umano di ciascun fiocco viene da una tabella diversa, indicizzata per chiave e non per
numero, e va unita alle posizioni sulla chiave. Le due tabelle non sono ordinate allo stesso modo
e non hanno la stessa cardinalità, quindi l'unione va fatta per nome e mai per posizione.

Che cosa la misura può dire, e che cosa no
-------------------------------------------
Dice quali fiocchi i nostri lotti portano e quali no, e la seconda parte è la lista di lavoro.
Non dice quali siano ottenibili oggi, che è una domanda diversa e a cui questo dato non risponde:
un fiocco assente dai lotti può essere ancora conferito da un gioco corrente, oppure essere
perduto con la chiusura, e distinguere i due casi richiede le regole di conferimento e non le
posizioni dei bit. Quella distinzione è il passo successivo ed è dichiarata come mancante.

Uso
---
    python tools/fiocchi.py
    python tools/fiocchi.py --out pokedex-home-completo/FIOCCHI.md
    python tools/fiocchi.py --self-test
"""

import argparse
import collections
import glob
import io
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))

PKM_DIR = os.path.join("PKHeX.Core", "PKM")
TESTI = os.path.join("PKHeX.Core", "Resources", "text", "other", "en")

# Le due dichiarazioni che il sorgente usa: il byte che ospita un gruppo di fiocchi, e il singolo
# fiocco con il proprio bit dentro quel gruppo.
RE_GRUPPO = re.compile(r"private byte (RIB\d)\s*\{\s*get => Data\[(0x[0-9A-Fa-f]+)\]")
RE_FIOCCO = re.compile(
    r"public override bool (Ribbon\w+)\s*\{\s*get => \((RIB\d) & \(1 << (\d)\)\)")


def posizioni(pkhex, file_):
    """Le posizioni dei fiocchi dentro un formato, come mappa dal nome alla coppia byte e bit."""
    testo = io.open(os.path.join(pkhex, PKM_DIR, file_), encoding="utf-8").read()
    gruppi = {n: int(off, 16) for n, off in RE_GRUPPO.findall(testo)}
    fuori = {}
    for nome, gruppo, bit in RE_FIOCCO.findall(testo):
        if gruppo in gruppi:
            fuori[nome] = (gruppi[gruppo], int(bit))
    return fuori, gruppi


def nomi_umani(pkhex):
    """Dalla chiave del fiocco al suo nome leggibile, dalla tabella a due campi."""
    percorso = os.path.join(pkhex, TESTI, "text_Ribbons_en.txt")
    fuori = {}
    for r in io.open(percorso, encoding="utf-8-sig").read().splitlines():
        if "\t" in r:
            chiave, nome = r.split("\t", 1)
            fuori[chiave.strip()] = nome.strip()
    return fuori


def portati(percorsi, pos):
    """I fiocchi accesi nei file di un lotto, con quanti esemplari li portano."""
    conto = collections.Counter()
    quanti = 0
    for f in percorsi:
        d = open(f, "rb").read()
        quanti += 1
        for nome, (off, bit) in pos.items():
            if off < len(d) and (d[off] & (1 << bit)):
                conto[nome] += 1
    return conto, quanti


# La terza generazione non impacchetta i propri fiocchi come le successive, e la differenza va
# letta dal sorgente e non supposta. I cinque fiocchi di gara non sono bit ma contatori a tre bit
# ciascuno, perche' ognuno porta un livello da zero a quattro invece di un si' o un no; soltanto
# dal sedicesimo bit in avanti cominciano i fiocchi veri e propri, uno per bit.
#
# Va registrato che alla prima stesura questo programma aveva l'ordine scritto a mano, supponendo
# venti bit di gara al posto di quindici, e il risultato non era un errore ma qualcosa di
# peggiore: un conteggio plausibile e sbagliato, che dichiarava due esemplari con un fiocco che
# nessuno di essi porta. E' esattamente il difetto contro cui il resto di questo programma era
# stato scritto, cioe' la trascrizione di una tabella lunga, e averlo commesso qui mentre lo si
# evitava altrove e' la ragione per cui questo commento e' lungo.

# Il primo bit assoluto che non appartiene ai fiocchi di gara, e quindi l'origine della
# numerazione del campo dei meriti come il pacchetto del ponte lo espone.
PRIMO_BIT_MERITO = 15

RE_CONTATORE3 = re.compile(
    r"public override byte (Ribbon\w+)\s*\{\s*get => \(byte\)\(\(RIB0 >> (\d+)\) & 7\)")
RE_BIT3 = re.compile(
    r"public override bool (Ribbon\w+)\s*\{\s*get => \(RIB0 & \(1 << (\d+)\)\)")


def posizioni_gen3(pkhex):
    """I fiocchi di terza generazione, come contatori a tre bit e come bit singoli."""
    testo = io.open(os.path.join(pkhex, PKM_DIR, "PK3.cs"), encoding="utf-8").read()
    contatori = [(n, int(s)) for n, s in RE_CONTATORE3.findall(testo)]
    bit = [(n, int(b)) for n, b in RE_BIT3.findall(testo)]
    return contatori, bit


def portati_gen3(percorsi, pkhex):
    """I fiocchi di terza generazione accesi nei nostri file, per nome.

    La parola dei meriti si legge dal pacchetto del ponte, che la espone gia' estratta dalla
    sottostruttura varia; le posizioni dentro quella parola si leggono invece dal sorgente del
    verificatore, per la ragione scritta sopra.
    """
    from pokebridge import gen3  # noqa: E402
    contatori, bit = posizioni_gen3(pkhex)
    ordine = [n for n, _ in contatori] + [n for n, _ in bit]
    conto = collections.Counter()
    quanti = 0
    for f in percorsi:
        m = gen3.Gen3Mon.from_canonical_bytes(open(f, "rb").read(), party=False)
        quanti += 1
        # Il pacchetto del ponte espone i due gruppi separati e non la parola intera, e questa e'
        # la seconda trappola di questa funzione dopo quella dei contatori a tre bit. I fiocchi
        # di gara stanno in un dizionario, i fiocchi di merito in un intero il cui bit zero e' il
        # quindicesimo bit assoluto, cioe' il primo che non appartiene alle gare. Leggere quel
        # campo come se fosse la parola assoluta sposta ogni fiocco di quindici posizioni e
        # produce un conteggio plausibile: alla prima corsa questo programma dichiarava due
        # esemplari con il fiocco di gara raffinata, mentre quei due portano il fiocco nazionale,
        # che e' precisamente quello che la tabella del verificatore dichiara per loro. Il
        # generatore era corretto e questo lettore no.
        gare = m.misc.contest_ribbons or {}
        for nome, spostamento in contatori:
            # Il nome del contatore nella fonte e' del tipo RibbonCountG3Cool: la chiave del
            # dizionario e' la sola categoria in minuscolo.
            categoria = nome.replace("RibbonCountG3", "").lower()
            if gare.get(categoria, 0):
                conto[nome] += 1
        meriti = m.misc.merit_ribbons
        for nome, b in bit:
            if b >= PRIMO_BIT_MERITO and (meriti & (1 << (b - PRIMO_BIT_MERITO))):
                conto[nome] += 1
    return conto, quanti, ordine


# La cartella dei verificatori raggruppa i fiocchi per insieme, e ciascun insieme appartiene a una
# generazione. Il raggruppamento si legge dal sorgente; l'attribuzione dell'insieme alla
# generazione e la conseguenza sulla scadenza sono invece nostre e stanno qui dichiarate, perche'
# sono un giudizio e non un dato.
#
# Il criterio della scadenza e' questo: un fiocco si perde con la chiusura quando il solo gioco
# che lo conferisce raggiunge il deposito attraverso la banca. I titoli per console corrente non
# hanno quel problema, quindi i loro fiocchi restano conquistabili dopo la chiusura.
INSIEMI = [
    ("Common3", 3, True, "gara e campione di terza generazione"),
    ("Only3", 3, True, "esclusivi della terza generazione"),
    ("Unique3", 3, True, "unici della terza generazione"),
    ("Event3", 3, True, "conferiti da distribuzioni di terza generazione"),
    ("Common4", 4, True, "comuni di quarta generazione"),
    ("Unique4", 4, True, "gara e abilita' di quarta generazione"),
    ("Event4", 4, True, "conferiti da distribuzioni di quarta generazione"),
    ("Common6", 6, True, "comuni di sesta generazione"),
    ("Common7", 7, True, "comuni di settima generazione"),
    ("Common8", 8, False, "comuni di ottava generazione, su console corrente"),
    ("Common9", 9, False, "comuni di nona generazione, su console corrente"),
    ("Mark9", 9, False, "contrassegni di nona generazione, su console corrente"),
]

RE_USO = re.compile(r"r\.(Ribbon[A-Za-z0-9]+)")
# Il verificatore nomina un fiocco in due modi dentro lo stesso file: come proprieta' letta
# dall'esemplare, con il prefisso, e come voce dell'elenco dei rilievi, senza. Cercare soltanto la
# prima forma lascia fuori i fiocchi che quel file segnala e non legge, che nella sesta e settima
# generazione sono la maggioranza. Le due forme si uniscono ricomponendo il prefisso.
RE_SEGNALATO = re.compile(r"list\.Add\(([A-Z][A-Za-z0-9]*)\)")


def insiemi_di_appartenenza(pkhex, chiavi=frozenset()):
    """Per ciascun fiocco, gli insiemi del verificatore che lo trattano.

    Un fiocco puo' appartenere a piu' insiemi, e non e' un difetto della lettura: significa che
    piu' generazioni lo conferiscono, ed e' precisamente l'informazione che decide se si perda
    con la chiusura. Un fiocco trattato da un insieme di ottava o nona generazione resta
    conquistabile su console corrente, qualunque altro insieme lo tratti.
    """
    cartella = os.path.join(pkhex, "PKHeX.Core", "Legality", "Verifiers", "Ribbons")
    fuori = collections.defaultdict(list)
    for nome, gen, scade, umano in INSIEMI:
        percorso = os.path.join(cartella, "RibbonVerifier%s.cs" % nome)
        if not os.path.exists(percorso):
            continue
        testo = io.open(percorso, encoding="utf-8").read()
        trovati = set(RE_USO.findall(testo))
        for corto in RE_SEGNALATO.findall(testo):
            lungo = "Ribbon" + corto
            if lungo in chiavi:
                trovati.add(lungo)
        for fiocco in sorted(trovati):
            fuori[fiocco].append((nome, gen, scade, umano))
    return fuori


def rapporto(pkhex):
    pos4, gruppi4 = posizioni(pkhex, "PK4.cs")
    umani = nomi_umani(pkhex)

    lotti = {
        "gen4": sorted(glob.glob(os.path.join(RADICE, "_notes", "lotto-gen4", "*.pk4"))),
        "gen5": sorted(glob.glob(os.path.join(RADICE, "_notes", "lotto-gen5", "*.pk5"))),
    }
    conti = {}
    for et, percorsi in lotti.items():
        conti[et] = portati(percorsi, pos4)

    g3 = sorted(glob.glob(os.path.join(RADICE, "_notes", "lotto-eventi", "*.pk3"))
                + glob.glob(os.path.join(RADICE, "_notes", "lotto-incontri-gen3", "*.pk3")))
    conto3, quanti3, ordine3 = portati_gen3(g3, pkhex)

    r = ["# L'asse dei fiocchi: enumerazione e copertura", ""]
    r.append("> Documento generato da `tools/fiocchi.py`. Non si modifica a mano: si rigenera. Le "
             "posizioni dei bit sono lette dal sorgente del verificatore e non trascritte, per la "
             "ragione gia' pagata due volte da questo progetto su tabelle lunghe.")
    r.append("")
    r.append("Il formato di quarta e quinta generazione dichiara %d fiocchi distinti, distribuiti "
             "in %d byte dell'esemplare. La terza generazione ne tiene trentadue in una parola "
             "sola dentro la propria sottostruttura varia." % (len(pos4), len(gruppi4)))
    r.append("")
    r.append("Va detto subito cio' che questa misura non dice, perche' e' la domanda che verra' "
             "subito dopo: dice quali fiocchi i nostri lotti portano, non quali siano ancora "
             "ottenibili oggi. Un fiocco assente dai lotti puo' essere ancora conferito da un "
             "gioco corrente oppure essere perduto con la chiusura, e distinguere i due casi "
             "richiede le regole di conferimento e non le posizioni dei bit.")
    r.append("")

    r.append("## Terza generazione, i trentadue della parola dei meriti")
    r.append("")
    r.append("Sui %d esemplari dei due lotti di terza generazione." % quanti3)
    r.append("")
    r.append("| Fiocco | Esemplari che lo portano |")
    r.append("|---|---|")
    for nome in ordine3:
        r.append("| %s | %d |" % (nome, conto3.get(nome, 0)))
    r.append("")

    r.append("## Quarta e quinta generazione")
    r.append("")
    r.append("Sui %d esemplari di quarta e %d di quinta. La colonna del nome umano viene dalla "
             "tabella dei testi, unita alle posizioni sulla chiave e mai sulla posizione, perche' "
             "le due tabelle non hanno lo stesso ordine ne' la stessa cardinalita'."
             % (conti["gen4"][1], conti["gen5"][1]))
    r.append("")
    r.append("| Fiocco | Nome umano | Byte | Bit | Quarta | Quinta |")
    r.append("|---|---|---|---|---|---|")
    for nome in sorted(pos4, key=lambda n: pos4[n]):
        off, bit = pos4[nome]
        r.append("| %s | %s | 0x%02X | %d | %d | %d |"
                 % (nome, umani.get(nome, "-"), off, bit,
                    conti["gen4"][0].get(nome, 0), conti["gen5"][0].get(nome, 0)))
    r.append("")

    # L'asse non e' quello che il formato di quarta generazione sa rappresentare, ed e' un errore
    # che questo programma ha fatto alla prima stesura: quel formato porta i soli fiocchi che
    # esistevano fino alla quinta generazione, quindi enumerare da la' significa dichiarare come
    # asse completo un suo sottoinsieme, e per giunta senza accorgersene, perche' il conto torna.
    # L'asse vero e' la tabella dei nomi, che li elenca tutti fino alla nona generazione.
    tutti = sorted(umani)
    r.append("## L'asse intero, e la parte che i nostri formati sanno rappresentare")
    r.append("")
    r.append("La tabella dei nomi del verificatore elenca %d fiocchi, ed e' l'asse. Il formato di "
             "quarta e quinta generazione ne rappresenta %d, cioe' quelli che esistevano fino "
             "alla quinta: gli altri vivono nei formati successivi e nessun nostro lotto puo' "
             "portarli, perche' i nostri lotti arrivano alla quinta. Enumerare l'asse dal formato "
             "invece che dalla tabella dei nomi e' l'errore che questa sezione esiste per non far "
             "commettere: il conto torna e il denominatore e' sbagliato."
             % (len(tutti), len(pos4)))
    r.append("")

    assenti = [n for n in pos4 if not conti["gen4"][0].get(n) and not conti["gen5"][0].get(n)]
    r.append("## Quelli rappresentabili che nessun nostro esemplare porta (%d su %d)"
             % (len(assenti), len(pos4)))
    r.append("")
    r.append("E' la lista di lavoro dell'asse, e comprende cose di natura molto diversa: fiocchi "
             "di gara che si conquistano giocando, fiocchi di ricordo che un gioco assegna una "
             "volta sola, e fiocchi che soltanto una distribuzione conferiva. La classificazione "
             "per via di conferimento e' quella che decide quali siano perduti con la chiusura, "
             "ed e' qui sotto.")
    r.append("")
    appartenenza = insiemi_di_appartenenza(pkhex, frozenset(umani))

    def classifica(nome):
        gruppi = appartenenza.get(nome, [])
        if not gruppi:
            return None, "nessun insieme del verificatore lo tratta"
        # Basta un insieme di console corrente perche' il fiocco non si perda.
        if any(not scade for _, _, scade, _ in gruppi):
            return False, "; ".join(u for _, _, _, u in gruppi)
        return True, "; ".join(u for _, _, _, u in gruppi)

    perduti, salvi, ignoti = [], [], []
    for nome in assenti:
        scade, perche = classifica(nome)
        (perduti if scade else (salvi if scade is False else ignoti)).append((nome, perche))

    r.append("La classificazione che segue viene dal raggruppamento che il verificatore stesso fa "
             "dei fiocchi in insiemi, uno per generazione: quel raggruppamento e' letto dal "
             "sorgente, mentre l'attribuzione di ciascun insieme alla propria generazione e la "
             "conseguenza sulla scadenza sono un nostro giudizio, dichiarato dentro il programma. "
             "Il criterio e' che un fiocco si perde con la chiusura quando il solo gioco che lo "
             "conferisce raggiunge il deposito attraverso la banca; basta invece un solo insieme "
             "di console corrente perche' resti conquistabile.")
    r.append("")
    r.append("Va dichiarata una approssimazione, perche' rende questo conto un limite superiore e "
             "non un numero esatto. Le riedizioni della quarta generazione per console corrente "
             "riconferiscono una parte dei fiocchi di quarta, e il verificatore lo esprime dentro "
             "condizioni che questo programma non interpreta: alcune voci contate qui come "
             "perdute sono quindi riconquistabili la'. Distinguerle richiede di leggere quelle "
             "condizioni una per una, ed e' il passo successivo.")
    r.append("")
    r.append("| Esito | Quanti |")
    r.append("|---|---|")
    r.append("| perduti con la chiusura, al piu' | %d |" % len(perduti))
    r.append("| conquistabili su console corrente | %d |" % len(salvi))
    r.append("| non trattati da alcun insieme | %d |" % len(ignoti))
    r.append("")
    for titolo, gruppo in (("Perduti con la chiusura, al piu'", perduti),
                           ("Conquistabili su console corrente", salvi),
                           ("Non trattati da alcun insieme del verificatore", ignoti)):
        r.append("### %s (%d)" % (titolo, len(gruppo)))
        r.append("")
        r.append("| Fiocco | Nome umano | Insiemi che lo trattano |")
        r.append("|---|---|---|")
        for nome, perche in sorted(gruppo, key=lambda x: pos4[x[0]]):
            r.append("| %s | %s | %s |" % (nome, umani.get(nome, "-"), perche))
        r.append("")

    # La parte dell'asse che i nostri formati non rappresentano affatto, e che va dichiarata
    # perche' altrimenti sembra assente per scelta invece che per struttura.
    fuori_formato = [n for n in tutti if n not in pos4]
    per_gruppo = collections.Counter()
    for nome in fuori_formato:
        gruppi = appartenenza.get(nome, [])
        per_gruppo[gruppi[0][3] if gruppi else "nessun insieme lo tratta"] += 1
    r.append("## La parte dell'asse fuori dai nostri formati (%d)" % len(fuori_formato))
    r.append("")
    r.append("Sono i fiocchi introdotti dalla sesta generazione in avanti, piu' i contrassegni "
             "della nona. Nessun esemplare dei nostri lotti puo' portarli, e non e' una lacuna "
             "della produzione ma una proprieta' del perimetro: i lotti arrivano alla quinta "
             "generazione. Si ottengono giocando i titoli che li conferiscono, e per quelli di "
             "ottava e nona generazione la chiusura non li tocca.")
    r.append("")
    r.append("| Insieme che li tratta | Quanti |")
    r.append("|---|---|")
    for gruppo, quanti in per_gruppo.most_common():
        r.append("| %s | %d |" % (gruppo, quanti))
    return "\n".join(r) + "\n", len(tutti), len(assenti), len(perduti)


def self_test():
    esiti = []

    def prova(nome, cond, det=""):
        esiti.append((nome, bool(cond), det))

    sorgente = (
        "    private byte RIB0 { get => Data[0x24]; set => Data[0x24] = value; } // Sinnoh 1\n"
        "    private byte RIB4 { get => Data[0x3C]; set => Data[0x3C] = value; } // Hoenn 1a\n"
        "    public override bool RibbonChampionSinnoh { get => (RIB0 & (1 << 0)) == 1 << 0; }\n"
        "    public override bool RibbonAlert { get => (RIB0 & (1 << 7)) == 1 << 7; }\n"
        "    public override bool RibbonG3Cool { get => (RIB4 & (1 << 0)) == 1 << 0; }\n")
    gruppi = {n: int(o, 16) for n, o in RE_GRUPPO.findall(sorgente)}
    prova("i gruppi si leggono con il loro byte",
          gruppi == {"RIB0": 0x24, "RIB4": 0x3C}, str(gruppi))
    fio = {n: (gruppi[g], int(b)) for n, g, b in RE_FIOCCO.findall(sorgente)}
    prova("ogni fiocco prende byte e bit dal proprio gruppo",
          fio == {"RibbonChampionSinnoh": (0x24, 0), "RibbonAlert": (0x24, 7),
                  "RibbonG3Cool": (0x3C, 0)}, str(fio))
    # Il controllo negativo: un fiocco il cui gruppo non e' dichiarato non deve entrare con un
    # byte inventato, perche' un byte sbagliato produce un valore booleano plausibile.
    orfano = "    public override bool RibbonX { get => (RIB9 & (1 << 2)) == 1 << 2; }\n"
    trovati = [n for n, g, _ in RE_FIOCCO.findall(sorgente + orfano) if g in gruppi]
    prova("negativo: un fiocco senza gruppo dichiarato resta fuori",
          "RibbonX" not in trovati, str(trovati))

    sorgente3 = (
        "    public override byte RibbonCountG3Cool { get => (byte)((RIB0 >> 00) & 7); }\n"
        "    public override byte RibbonCountG3Tough { get => (byte)((RIB0 >> 12) & 7); }\n"
        "    public override bool RibbonChampionG3 { get => (RIB0 & (1 << 15)) == 1 << 15; }\n"
        "    public override bool RibbonWorld { get => (RIB0 & (1 << 26)) == 1 << 26; }\n")
    cont = [(n, int(s)) for n, s in RE_CONTATORE3.findall(sorgente3)]
    bit3 = [(n, int(b)) for n, b in RE_BIT3.findall(sorgente3)]
    prova("i fiocchi di gara di terza sono contatori a tre bit",
          cont == [("RibbonCountG3Cool", 0), ("RibbonCountG3Tough", 12)], str(cont))
    prova("i fiocchi singoli di terza cominciano dal quindicesimo bit",
          bit3 == [("RibbonChampionG3", 15), ("RibbonWorld", 26)], str(bit3))
    # Il controllo negativo che avrebbe colto il difetto della prima stesura: con quattro bit per
    # gara il primo fiocco singolo cadrebbe al ventesimo, e la lettura sarebbe tutta spostata.
    prova("negativo: la supposizione di quattro bit per gara sposta ogni fiocco singolo",
          bit3[0][1] != 20, str(bit3[0]))

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
    p.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "pkhex"))
    p.add_argument("--out", default=os.path.join("pokedex-home-completo", "FIOCCHI.md"))
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()
    if a.self_test:
        return self_test()
    testo, quanti, assenti, perduti = rapporto(a.pkhex)
    io.open(a.out, "w", encoding="utf-8", newline="\n").write(testo)
    print("%d fiocchi nell'asse, %d rappresentabili e non portati da alcun nostro esemplare, "
          "di cui al piu' %d perduti con la chiusura; rapporto in %s"
          % (quanti, assenti, perduti, a.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
