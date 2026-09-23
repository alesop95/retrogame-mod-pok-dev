#!/usr/bin/env python3
"""Misura, sulle squadre estratte dai thread, dove e accanto a chi compare ciascun esemplare del lotto del Parco Lotta.

Perche' esiste
--------------

Il lotto ha otto titolari, che stanno nelle sei squadre di STUDIO-05, e ventiquattro riserve, che si generano ma non entrano in alcuna squadra. Una riserva serve solo se si sa quando tirarla fuori, e la domanda ha due forme. La prima e' per edificio: in quale dei sette edifici chi ha giocato l'ha portata, e con quale serie. La seconda e' per sostituzione: se in una squadra un titolare manca o non rende, quale riserva ha giocato piu' spesso accanto agli altri due. Entrambe sono conteggi sulle 268 squadre di `squadre.json`, e un conteggio si fa con codice e non a occhio, per la regola sull'economia dei token.

Che cosa questo strumento non fa
--------------------------------

Non sceglie. Un conteggio dice che cosa hanno fatto altri, non che cosa convenga fare con questi esemplari, e la differenza pesa per tre ragioni che il documento generato ripete. I thread nominano la specie e quasi mai la natura, quindi un conteggio su Latios vale per entrambi i Latios del lotto. Un thread registra chi ha voluto scrivere, di solito chi ha fatto una serie buona, quindi il campione e' sbilanciato verso i successi. E la Torre Lotta pesa quanto tutti gli altri edifici insieme, quindi un numero alto alla Torre significa meno di un numero alto al Palazzo. La scelta resta nella parte autorata del documento, che si scrive sopra queste tabelle.

Uso
---

    python gba-save-extraction-smeraldo/tools/parco_lotta_mappa_riserve.py
    python gba-save-extraction-smeraldo/tools/parco_lotta_mappa_riserve.py --out gba-save-extraction-smeraldo/MAPPA-RISERVE.md
"""

import argparse
import collections
import json
from pathlib import Path

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
CATALOGO = CARTELLA.joinpath("squadre-parco-lotta.json")
THREAD = RADICE.joinpath("_notes", "fonti", "smogon-parco-lotta-2026-09-21", "squadre.json")

EDIFICI = ["Cupola Lotta", "Torre Lotta", "Dojo Lotta", "Palazzo Lotta", "Serpe Lotta", "Piramide Lotta",
           "Azienda Lotta"]
SIGLE = {"Cupola Lotta": "Cup", "Torre Lotta": "Tor", "Dojo Lotta": "Doj", "Palazzo Lotta": "Pal",
         "Serpe Lotta": "Ser", "Piramide Lotta": "Pir", "Azienda Lotta": "Azi", None: "n.d."}


def misura(catalogo, thread):
    generati = {k: e for k, e in catalogo["esemplari"].items()
                if e.get("genera") is not False and (e.get("origine") or {}).get("genera") is not False}
    titolari = {k for k, e in generati.items() if not e.get("riserva")}
    per_specie = collections.defaultdict(list)
    for chiave, e in generati.items():
        per_specie[e["specie"]].append(chiave)

    specie_squadra = [({x["specie"] for x in s["esemplari"]}, s) for s in thread]
    righe = {}
    for specie in per_specie:
        edifici = collections.Counter()
        compagni = collections.Counter()
        serie = collections.defaultdict(int)
        for insieme, s in specie_squadra:
            if specie not in insieme:
                continue
            edificio = s.get("edificio")
            edifici[edificio] += 1
            for altro in insieme - {specie}:
                compagni[altro] += 1
            dichiarata = s.get("serie_dichiarata")
            if isinstance(dichiarata, int) and dichiarata > serie[edificio]:
                serie[edificio] = dichiarata
        righe[specie] = {"edifici": edifici, "compagni": compagni, "serie": serie}

    # La sostituzione: per ogni squadra con tre posti e per ogni posto, le riserve che hanno giocato
    # accanto agli ALTRI DUE titolari. Si contano le squadre che contengono la riserva e almeno uno dei
    # due, e a parte quelle che li contengono entrambi, perche' la seconda cifra e' la piu' forte e la
    # piu' rara, e fonderle nasconderebbe proprio la differenza che interessa.
    sostituzioni = []
    riserve_specie = {generati[k]["specie"] for k in generati if k not in titolari}
    for squadra in catalogo["squadre"]:
        membri = [v["chiave"] for v in squadra["esemplari"]]
        if len(membri) != 3:
            continue
        for uscente in membri:
            restano = {generati[k]["specie"] for k in membri if k != uscente}
            candidati = []
            for specie in riserve_specie:
                con_uno = con_entrambi = allo_stesso = 0
                for insieme, s in specie_squadra:
                    if specie not in insieme:
                        continue
                    comuni = len(insieme & restano)
                    if comuni:
                        con_uno += 1
                        if s.get("edificio") == squadra["edificio"]:
                            allo_stesso += 1
                    if comuni == 2:
                        con_entrambi += 1
                if con_uno:
                    candidati.append((con_entrambi, con_uno, allo_stesso, specie))
            candidati.sort(reverse=True)
            sostituzioni.append((squadra["edificio"], uscente, sorted(restano), candidati[:4]))
    return generati, titolari, per_specie, righe, sostituzioni


def scrivi(generati, titolari, per_specie, righe, sostituzioni, thread):
    conteggio = collections.Counter(s.get("edificio") for s in thread)
    out = []
    out.append("# Mappa delle riserve agli edifici, la misura")
    out.append("")
    out.append("> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_mappa_riserve.py` sul catalogo `squadre-parco-lotta.json` e sulle %d squadre estratte dai thread in `_notes/fonti/smogon-parco-lotta-2026-09-21/squadre.json`. Non si modifica a mano: si rigenera. E' la misura su cui si scrive la scelta, non la scelta, e le tre avvertenze del docstring dello strumento valgono per ogni numero qui sotto: i thread nominano la specie e non la natura, registrano soprattutto chi ha fatto una serie buona, e la Torre Lotta pesa quanto tutti gli altri edifici insieme." % len(thread))
    out.append("")
    out.append("Squadre per edificio nel campione: " + ", ".join(
        "%s %d" % (e if e else "edificio non dichiarato", conteggio[e]) for e in EDIFICI + [None]) + ".")
    out.append("")
    out.append("## Per esemplare: in quali edifici e con quale serie")
    out.append("")
    out.append("Ogni cella dice in quante squadre dei thread la specie compare in quell'edificio, e fra parentesi la serie piu' lunga dichiarata. Le specie con due esemplari nel lotto, cioe' Latios, Metagross e Swampert, condividono la riga.")
    out.append("")
    out.append("| Esemplari | Ruolo | " + " | ".join(SIGLE[e] for e in EDIFICI) + " | n.d. | Compagni piu' frequenti |")
    out.append("|---|---|" + "---|" * (len(EDIFICI) + 1) + "---|")
    ordine = sorted(per_specie, key=lambda sp: (not any(k in titolari for k in per_specie[sp]),
                                                -sum(righe[sp]["edifici"].values()), sp))
    for specie in ordine:
        r = righe[specie]
        ruolo = "titolare" if any(k in titolari for k in per_specie[specie]) else "riserva"
        celle = []
        for e in EDIFICI + [None]:
            n = r["edifici"].get(e, 0)
            s = r["serie"].get(e, 0)
            celle.append("" if n == 0 else ("%d (%d)" % (n, s) if s else "%d" % n))
        compagni = ", ".join("%s %d" % c for c in r["compagni"].most_common(3)) or "nessuno"
        out.append("| %s | %s | %s | %s |" % (", ".join(sorted(per_specie[specie])), ruolo, " | ".join(celle), compagni))
    out.append("")
    out.append("## Per sostituzione: chi ha giocato accanto agli altri due")
    out.append("")
    out.append("Per ogni squadra e per ogni posto, le riserve del lotto che nei thread compaiono accanto ai due titolari che restano. La prima cifra conta le squadre con entrambi, la seconda quelle con almeno uno, la terza quelle con almeno uno nello stesso edificio. L'Azienda Lotta non compare perche' vi si combatte con esemplari in prestito.")
    out.append("")
    out.append("| Edificio | Esce | Restano | Candidati: entrambi / almeno uno / stesso edificio |")
    out.append("|---|---|---|---|")
    for edificio, uscente, restano, candidati in sostituzioni:
        testo = "; ".join("%s %d/%d/%d" % (sp, a, b, c) for a, b, c, sp in candidati) or "nessun riscontro"
        out.append("| %s | %s | %s | %s |" % (edificio, uscente, ", ".join(restano), testo))
    out.append("")
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--catalogo", default=str(CATALOGO))
    p.add_argument("--thread", default=str(THREAD))
    p.add_argument("--out")
    args = p.parse_args()
    catalogo = json.loads(Path(args.catalogo).read_text(encoding="utf-8"))
    thread = json.loads(Path(args.thread).read_text(encoding="utf-8"))
    testo = scrivi(*misura(catalogo, thread), thread)
    if args.out:
        Path(args.out).write_bytes((testo + "\n").encode("utf-8"))
        print("scritto %s" % args.out)
    else:
        print(testo)


if __name__ == "__main__":
    main()
