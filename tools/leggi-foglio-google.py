#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legge una cartella di calcolo esportata da Google Fogli, per livelli crescenti di dettaglio.

Perche' uno strumento e non una lettura diretta
-----------------------------------------------
Le cartelle di calcolo che la comunita' mantiene su Google Fogli sono documenti voluminosi: quella
delle sfide del deposito ha quattordici schede e quella delle due sfide del catalogo ne ha sei, con
decine di migliaia di celle in tutto. Caricarle in conversazione per capire che cosa contengano
sarebbe il modo piu' caro possibile di rispondere a una domanda che e' quasi sempre soltanto quale
scheda guardare. Questo programma applica quindi la disclosure progressiva della regola
sull'economia dei token: al Livello 1 riferisce lo scheletro di tutte le schede in poche righe, al
Livello 2 l'intestazione e le prime e ultime righe di una scheda sola, al Livello 3 esporta una
scheda intera in CSV perche' la si possa confrontare con le nostre enumerazioni.

Le tre insidie del formato, che il programma tratta e dichiara
-------------------------------------------------------------
La prima e' l'estensione dichiarata. Un foglio esportato da Google porta di norma righe e colonne
vuote in coda, perche' l'estensione che il file dichiara e' quella della griglia dell'applicazione e
non quella del dato: leggere l'estensione dichiarata significa quindi leggere un numero che non
misura nulla. Il programma calcola l'estensione effettiva scandendo le celle e cercando l'ultima
riga e l'ultima colonna che portino contenuto.

La seconda e' il nome delle schede. Il formato di Excel tronca il titolo di una scheda a trentuno
caratteri, quindi il nome che il file dichiara puo' non essere quello che si vede nel documento in
rete: la scheda "Standard Living origin that can" finisce a meta' frase, e non e' un difetto
dell'esportazione. Il programma riferisce il troncamento cosicche' si riconosca invece di essere
preso per il nome vero.

La terza e' la natura di lista di controllo. In questi documenti le colonne che contano sono spesso
caselle di spunta, che il formato conserva come valori booleani: contarle e' l'unico modo di sapere
se una scheda sia una enumerazione da leggere oppure lo stato di avanzamento di chi l'ha compilata,
che a noi non serve. Il programma le conta a parte.

Che cosa questo programma non fa
--------------------------------
Non interpreta il contenuto e non lo confronta con le nostre liste. Riconoscere che una scheda
enumeri le mosse perdute invece dei fiocchi e' lavoro semantico, e sta a chi legge; qui c'e' la sola
parte deterministica, cioe' portare il dato fuori dal formato binario in una forma ispezionabile.
Il riconoscimento della riga di intestazione e' l'unica euristica presente, ed e' dichiarata: si
prende, fra le prime dodici righe con contenuto, quella con piu' celle piene, e a parita' vince la
prima.

Uso
---
    python tools/leggi-foglio-google.py
    python tools/leggi-foglio-google.py --check
    python tools/leggi-foglio-google.py --scheda "Home Move Dex"
    python tools/leggi-foglio-google.py --scheda "Home Move Dex" --csv fogli/mosse.csv
    python tools/leggi-foglio-google.py --file "percorso/altro.xlsx"
    python tools/leggi-foglio-google.py --self-test
"""

import argparse
import io
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USCITA = os.path.join(RADICE, "pokedex-home-completo", "INDICE-FOGLI-ESTERNI.md")

# Le cartelle di calcolo che il corpus della collezione porta e che il progetto tiene su disco. Non
# sono versionate, perche' `_notes/` e' escluso e perche' sono file di terzi: ne entra in git il solo
# scheletro generato, che e' il livello che serve a decidere dove guardare. Il percorso e' relativo
# alla radice del repository, perche' le prime due sono arrivate come consegna dell'utente e le
# altre due sono state scaricate dai collegamenti del corpus e stanno quindi fra le fonti.
FOGLI = [
    (os.path.join("_notes", "spreadsheets e passaggi home",
                  "Bank Closing all possible things checklist V0.5.xlsx"),
     "le sfide del deposito e gli assi della collezione, dal cluster della chiusura della banca"),
    (os.path.join("_notes", "spreadsheets e passaggi home",
                  "Pokémon Master Dex and Retro Dex Challenges.xlsx"),
     "le due sfide del catalogo, con la scheda dei rimandi"),
    (os.path.join("_notes", "fonti", "2026-09-08-foglio-ingame-events-chaboijish.xlsx"),
     "gli esemplari da evento interno al gioco, di ChaBoiJish, dal cluster delle enumerazioni trasversali"),
    (os.path.join("_notes", "fonti", "2026-09-08-foglio-scambi-e-doni-greenpangolin17.xlsx"),
     "gli scambi in gioco, i doni e gli esemplari interagibili, di greenpangolin17, dal medesimo cluster"),
]

RIGHE_INTESTAZIONE = 12   # entro quante righe con contenuto si cerca l'intestazione
ANTEPRIMA_TESTA = 8       # righe iniziali mostrate al Livello 2
ANTEPRIMA_CODA = 4        # righe finali mostrate al Livello 2
MAX_CELLA = 60            # troncamento di una cella nella resa a video, non nel CSV


def testo_cella(v):
    """Una cella come stringa, con i booleani resi nella forma che le liste di controllo usano."""
    if v is None:
        return ""
    if v is True:
        return "TRUE"
    if v is False:
        return "FALSE"
    return str(v).strip()


def scandisci(ws):
    """Una sola passata sulla scheda, da cui si ricava tutto cio' che i tre livelli richiedono.

    La passata e' una perche' su una cartella da dieci megabyte riaprire la scheda per ogni misura
    costerebbe piu' del resto del programma. Ne escono l'estensione effettiva, il riempimento, il
    conto delle caselle di spunta, le prime righe per il riconoscimento dell'intestazione e le
    ultime per l'anteprima.
    """
    ultima_riga = 0
    ultima_colonna = 0
    piene = 0
    booleane = 0
    teste = []
    code = []
    for i, riga in enumerate(ws.iter_rows(values_only=True), start=1):
        celle = [testo_cella(v) for v in riga]
        indici = [j for j, c in enumerate(celle, start=1) if c != ""]
        if not indici:
            continue
        ultima_riga = i
        ultima_colonna = max(ultima_colonna, indici[-1])
        piene += len(indici)
        booleane += sum(1 for v in riga if v is True or v is False)
        if len(teste) < RIGHE_INTESTAZIONE:
            teste.append((i, celle))
        code.append((i, celle))
        if len(code) > ANTEPRIMA_CODA:
            code.pop(0)
    griglia = ultima_riga * ultima_colonna
    return {
        "titolo": ws.title,
        "righe": ultima_riga,
        "colonne": ultima_colonna,
        "piene": piene,
        "booleane": booleane,
        "riempimento": (100.0 * piene / griglia) if griglia else 0.0,
        "teste": teste,
        "code": code,
    }


def riconosci_intestazione(teste):
    """La riga di intestazione secondo l'euristica dichiarata: piu' celle piene, a parita' la prima.

    Restituisce la coppia fra il numero di riga e le sue celle, oppure la coppia fra zero e la lista
    vuota se la scheda non porta alcuna riga con contenuto. L'euristica sbaglia sui fogli che aprono
    con un titolo su una riga larga quanto la tabella, e per questo il Livello 2 mostra comunque le
    righe che le stanno intorno.
    """
    migliore, quante = (0, []), -1
    for numero, celle in teste:
        n = sum(1 for c in celle if c != "")
        if n > quante:
            migliore, quante = (numero, celle), n
    return migliore


def campo_csv(c):
    """Un campo CSV con le virgole, gli apici e gli a capo protetti."""
    if any(x in c for x in (",", '"', "\n", "\r")):
        return '"%s"' % c.replace('"', '""')
    return c


def apri(percorso):
    """La cartella di calcolo in sola lettura, con le formule risolte al loro ultimo valore."""
    try:
        import openpyxl
    except ImportError:
        return None, "manca openpyxl: si installa con `pip install openpyxl`"
    if not os.path.exists(percorso):
        return None, "manca la cartella di calcolo in " + percorso
    return openpyxl.load_workbook(percorso, read_only=True, data_only=True), None


def scheletro(percorso):
    """Il Livello 1 di una cartella intera: una riga per scheda."""
    libro, errore = apri(percorso)
    if errore:
        return None, errore
    schede = [scandisci(ws) for ws in libro.worksheets]
    libro.close()
    return schede, None


def componi(inventario):
    """Il documento di Livello 1, che e' cio' che entra in git al posto dei file binari."""
    r = ["# Indice delle cartelle di calcolo esterne della collezione", ""]
    r.append("> Documento generato da `tools/leggi-foglio-google.py`. Non si modifica a mano: si rigenera. E' lo scheletro di Livello 1 delle cartelle di calcolo che il corpus della collezione porta e che stanno in `_notes/spreadsheets e passaggi home/`, cioe' fuori dal version control perche' sono file di terzi. Serve a decidere quale scheda valga la lettura, non a sostituirla.")
    r.append("")
    r.append("Il riempimento e' la frazione di celle piene sulla griglia effettiva, e va letto come indizio della forma di una scheda: un valore basso indica una tabella sparsa o una scheda di sola prosa, un valore alto una enumerazione densa. Le caselle di spunta sono contate a parte perche' distinguono una enumerazione da leggere dallo stato di avanzamento di chi ha compilato il foglio, che a noi non serve. Un titolo dichiarato troncato ha esattamente trentuno caratteri, che e' il tetto del formato e non la fine del nome.")
    r.append("")
    for nome, che_cosa, schede, errore in inventario:
        r.append("## %s" % nome)
        r.append("")
        r.append("Che cosa porta: %s." % che_cosa)
        r.append("")
        if errore:
            r.append("Non letta: %s." % errore)
            r.append("")
            continue
        r.append("| Scheda | Righe | Colonne | Celle piene | Riempimento | Spunte | Intestazione riconosciuta |")
        r.append("|---|---|---|---|---|---|---|")
        for s in schede:
            numero, celle = riconosci_intestazione(s["teste"])
            etichette = [c for c in celle if c != ""][:6]
            titolo = s["titolo"] + (" (troncato)" if len(s["titolo"]) == 31 else "")
            r.append("| %s | %d | %d | %d | %.0f%% | %d | riga %d: %s |"
                     % (titolo, s["righe"], s["colonne"], s["piene"], s["riempimento"],
                        s["booleane"], numero,
                        "; ".join(e[:40].replace("|", "/") for e in etichette)
                        if etichette else "nessuna"))
        r.append("")
        totale = sum(s["piene"] for s in schede)
        r.append("Il totale delle celle piene di questa cartella e' %d su %d schede."
                 % (totale, len(schede)))
        r.append("")
    return "\n".join(r) + "\n"


def mostra_anteprima(percorso, nome_scheda):
    """Il Livello 2 su una scheda sola, a video e non su disco."""
    libro, errore = apri(percorso)
    if errore:
        print("rifiutato: " + errore)
        return 1
    titoli = libro.sheetnames
    if nome_scheda not in titoli:
        vicini = [t for t in titoli if nome_scheda.lower() in t.lower()]
        libro.close()
        print("rifiutato: la cartella non ha la scheda %r" % nome_scheda)
        if vicini:
            print("  forse intendevi: " + " | ".join(vicini))
        else:
            print("  schede presenti: " + " | ".join(titoli))
        return 1
    s = scandisci(libro[nome_scheda])
    libro.close()
    numero, _ = riconosci_intestazione(s["teste"])
    print("scheda %s: %d righe per %d colonne, %d celle piene (%.0f%%), %d spunte"
          % (s["titolo"], s["righe"], s["colonne"], s["piene"], s["riempimento"], s["booleane"]))
    print("intestazione riconosciuta alla riga %d" % numero)
    mostrate = s["teste"][:ANTEPRIMA_TESTA]
    for i, celle in mostrate:
        print("%5d | %s" % (i, " | ".join(c[:MAX_CELLA] for c in celle if c != "")))
    ultima_mostrata = mostrate[-1][0] if mostrate else 0
    ultime = [(i, c) for i, c in s["code"] if i > ultima_mostrata]
    if ultime:
        print("  ...")
        for i, celle in ultime:
            print("%5d | %s" % (i, " | ".join(c[:MAX_CELLA] for c in celle if c != "")))
    return 0


def esporta(percorso, nome_scheda, destinazione):
    """Il Livello 3: una scheda intera in CSV, che e' la forma su cui si fa un confronto."""
    libro, errore = apri(percorso)
    if errore:
        print("rifiutato: " + errore)
        return 1
    if nome_scheda not in libro.sheetnames:
        libro.close()
        print("rifiutato: la cartella non ha la scheda %r" % nome_scheda)
        return 1
    righe = []
    for riga in libro[nome_scheda].iter_rows(values_only=True):
        celle = [testo_cella(v) for v in riga]
        while celle and celle[-1] == "":
            celle.pop()
        if celle:
            righe.append(",".join(campo_csv(c) for c in celle))
    libro.close()
    if not os.path.isabs(destinazione):
        destinazione = os.path.join(RADICE, destinazione)
    cartella = os.path.dirname(destinazione)
    if cartella and not os.path.isdir(cartella):
        os.makedirs(cartella)
    io.open(destinazione, "w", encoding="utf-8", newline="\n").write("\n".join(righe) + "\n")
    print("scritte %d righe in %s" % (len(righe), destinazione))
    return 0


def quale_cartella(nome_scheda):
    """In quale delle cartelle registrate esista una scheda con questo nome.

    Serve perche' con piu' cartelle registrate il solo nome della scheda e' ambiguo, e indovinare
    sarebbe il genere di comodita' che poi fa leggere il foglio sbagliato senza dirlo.
    """
    trovate = []
    for percorso, _ in FOGLI:
        libro, errore = apri(os.path.join(RADICE, percorso))
        if errore:
            continue
        if nome_scheda in libro.sheetnames:
            trovate.append(percorso)
        libro.close()
    return trovate


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    # I booleani sono la forma in cui una casella di spunta arriva, e vanno resi come tali: senza
    # questa conversione una spunta finirebbe nel CSV come True, che nessuna lista di controllo usa.
    prova("una spunta vera", "TRUE", testo_cella(True))
    prova("una spunta falsa", "FALSE", testo_cella(False))
    prova("una cella vuota", "", testo_cella(None))
    prova("uno spazio non e' contenuto", "", testo_cella("   "))
    prova("un numero diventa testo", "12", testo_cella(12))

    class SchedaFinta(object):
        """Il minimo che `scandisci` richiede, cosicche' il self-test non dipenda da alcun file."""

        title = "finta"

        def __init__(self, righe):
            self.righe = righe

        def iter_rows(self, values_only=True):
            for r in self.righe:
                yield tuple(r)

    # L'estensione effettiva e' il presidio contro la griglia di Google: la scheda finta qui sotto
    # dichiara quattro righe per cinque colonne e ne porta due per tre.
    finta = SchedaFinta([
        ["Dex", "Nome", "Preso", None, None],
        [1, "Bulbasaur", True, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
    ])
    s = scandisci(finta)
    prova("le righe vuote in coda non contano", 2, s["righe"])
    prova("le colonne vuote in coda non contano", 3, s["colonne"])
    prova("le celle piene sono contate", 6, s["piene"])
    prova("la spunta e' contata a parte", 1, s["booleane"])
    prova("il riempimento e' pieno", 100, int(round(s["riempimento"])))
    # Controllo negativo: senza il calcolo dell'estensione la scheda direbbe quattro righe, ed e'
    # esattamente il numero che non va riferito.
    prova("l'estensione dichiarata non e' quella effettiva", True, s["righe"] != len(finta.righe))

    # Una riga vuota in mezzo non chiude la scheda, altrimenti una tabella con uno stacco fra due
    # blocchi verrebbe misurata al solo primo blocco.
    finta = SchedaFinta([
        ["Dex", "Nome"],
        [None, None],
        [2, "Ivysaur"],
    ])
    prova("una riga vuota in mezzo non chiude la scheda", 3, scandisci(finta)["righe"])

    # Il riconoscimento dell'intestazione: vince la riga con piu' celle piene, non la prima.
    finta = SchedaFinta([
        ["Titolo del foglio", None, None],
        [None, None, None],
        ["Dex", "Nome", "Nota"],
        [1, "Bulbasaur", "-"],
    ])
    numero, celle = riconosci_intestazione(scandisci(finta)["teste"])
    prova("l'intestazione non e' il titolo", 3, numero)
    prova("e porta le sue etichette", ["Dex", "Nome", "Nota"], celle)
    prova("una scheda vuota non ha intestazione", (0, []), riconosci_intestazione([]))

    # Il CSV protegge cio' che spezzerebbe una riga o un campo.
    prova("la virgola viene protetta", '"uno, due"', campo_csv("uno, due"))
    prova("l'apice viene raddoppiato", '"lui ""disse"""', campo_csv('lui "disse"'))
    prova("l'a capo viene protetto", '"uno\ndue"', campo_csv("uno\ndue"))
    prova("un campo semplice resta nudo", "Bulbasaur", campo_csv("Bulbasaur"))

    # La riga di tabella del documento non deve poter essere spezzata da una barra verticale che
    # arrivi da una etichetta del foglio, perche' romperebbe la griglia Markdown senza errore.
    inventario = [("finta.xlsx", "prova", [{
        "titolo": "s", "righe": 1, "colonne": 2, "piene": 2, "booleane": 0,
        "riempimento": 100.0, "teste": [(1, ["a|b", "c"])], "code": [],
    }], None)]
    testo = componi(inventario)
    prova("la barra dentro una etichetta viene neutralizzata", True, "a/b" in testo)

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--file", help="una cartella di calcolo diversa da quelle registrate")
    ap.add_argument("--scheda", help="Livello 2 o 3 su questa scheda invece del Livello 1 su tutte")
    ap.add_argument("--csv", help="con --scheda, esporta la scheda in questo percorso")
    ap.add_argument("--check", action="store_true",
                    help="non scrive: dice soltanto se lo scheletro sul disco sia allineato")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    if a.scheda:
        percorso = a.file
        if not percorso:
            trovate = quale_cartella(a.scheda)
            if len(trovate) > 1:
                print("rifiutato: la scheda %r esiste in piu' cartelle, serve --file" % a.scheda)
                for n in trovate:
                    print("  " + n)
                return 1
            percorso = trovate[0] if trovate else FOGLI[0][0]
        if not os.path.isabs(percorso):
            percorso = os.path.join(RADICE, percorso)
        if a.csv:
            return esporta(percorso, a.scheda, a.csv)
        return mostra_anteprima(percorso, a.scheda)

    bersagli = ([(a.file, "indicata a riga di comando")] if a.file else list(FOGLI))
    inventario = []
    for percorso, che_cosa in bersagli:
        assoluto = percorso if os.path.isabs(percorso) else os.path.join(RADICE, percorso)
        schede, errore = scheletro(assoluto)
        inventario.append((os.path.basename(percorso), che_cosa, schede, errore))

    testo = componi(inventario)
    if a.file:
        # Una cartella indicata a riga di comando non entra nel documento tracciato, altrimenti una
        # esplorazione occasionale sostituirebbe l'indice delle cartelle registrate.
        sys.stdout.write(testo)
        return 0
    if a.check:
        vecchio = io.open(USCITA, encoding="utf-8").read() if os.path.exists(USCITA) else ""
        if vecchio != testo:
            print("disallineato: %s va rigenerato" % USCITA)
            return 1
        print("allineato: " + USCITA)
        return 0
    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    print("scritto " + USCITA)
    for nome, _, schede, errore in inventario:
        if errore:
            print("  %s: NON letta, %s" % (nome, errore))
        else:
            print("  %s: %d schede, %d celle piene"
                  % (nome, len(schede), sum(s["piene"] for s in schede)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
