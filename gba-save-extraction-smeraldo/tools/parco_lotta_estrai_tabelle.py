#!/usr/bin/env python3
"""Estrae dal wikitesto di Bulbapedia le tabelle numeriche del Parco Lotta che servono alla composizione di una squadra.

Perche' esiste
--------------

Le pagine del Parco Lotta contengono, in mezzo a molta prosa, un piccolo numero di tabelle che sono dati veri e non descrizione: le proporzioni con cui ogni natura sceglie la categoria di mossa al Palazzo Lotta, e le soglie di serie a cui compare ciascun Asso del Parco. Una squadra si progetta su quei numeri, e leggerli a occhio dal wikitesto e' il modo in cui un numero sbagliato entra in un progetto senza che nessuno se ne accorga: la tabella del Palazzo ha sei colonne per venticinque righe, e l'occhio salta una riga con facilita'.

L'estrazione e' quindi deterministica, come prescrive `token-economy.md`, e il suo esito e' uno stato su disco ispezionabile invece di un numero ricordato in chat. Il derivato si rigenera dal grezzo senza ri-scaricare nulla, perche' il grezzo porta nella propria intestazione la revisione da cui viene.

Che cosa estrae, e perche' proprio queste
-----------------------------------------

La tabella delle nature del Palazzo Lotta e' l'unico punto del Parco in cui la natura di un esemplare smette di essere una modifica alle statistiche e diventa il suo comportamento: al Palazzo l'allenatore non sceglie le mosse, le sceglie la natura, con proporzioni diverse sopra e sotto la meta' dei punti salute. Una squadra costruita per gli altri sei edifici puo' quindi essere inservibile qui, e non per debolezza ma perche' rifiuta di attaccare. E' il vincolo piu' facile da ignorare quando si copia una squadra da un forum, dove quasi sempre e' pensata per la Torre.

Le soglie degli Assi vengono invece dalle schede informative in testa a ogni pagina, e dicono dopo quante serie vinte compare l'Asso la prima volta, per il simbolo d'argento, e la seconda, per quello d'oro. Sono il calendario dell'obiettivo dichiarato, cioe' i sette simboli d'oro, e vanno letti tutti insieme perche' i sette edifici non costano lo stesso.

Uso
---

    python gba-save-extraction-smeraldo/tools/parco_lotta_estrai_tabelle.py --grezzo _notes/fonti/raccolte/bulbapedia-parco-lotta-2026-09-21/grezzo --out <cartella>
"""

import argparse
import json
import re
from pathlib import Path

CATEGORIE = ["attacco", "difesa", "supporto", "attacco_sotto50", "difesa_sotto50", "supporto_sotto50"]

EDIFICI = [
    ("battle-factory-generation-iii", "Azienda Lotta", "Conoscenza"),
    ("battle-arena", "Dojo Lotta", "Tenacia"),
    ("battle-dome", "Cupola Lotta", "Tattica"),
    ("battle-pike", "Serpe Lotta", "Fortuna"),
    ("battle-palace", "Palazzo Lotta", "Spirito"),
    ("battle-pyramid", "Piramide Lotta", "Coraggio"),
    ("battle-tower-generation-iii", "Torre Lotta", "Abilita"),
]


def nature_del_palazzo(wikitesto):
    """Legge la tabella natura-per-categoria, che nel wikitesto e' una riga `! Nome` seguita da due righe di percentuali.

    L'ultima riga della tabella non ha la stessa forma delle altre ventiquattro: porta lo stile che arrotonda l'angolo in basso a sinistra, quindi si presenta come `! style="..." | Quirky` invece che come `! Quirky`. Una lettura che riconoscesse solo la forma nuda perderebbe in silenzio esattamente una natura, e lo farebbe sull'ultima riga, cioe' dove nessuno guarda. E' il motivo per cui l'intestazione si riconosce con lo stile facoltativo e per cui il conteggio finale e' un'asserzione e non una stampa.
    """
    righe = wikitesto.splitlines()
    tabella = {}
    indice = 0
    while indice < len(righe):
        intestazione = re.match(r"^!\s*(?:.*\|\s*)?([A-Z][a-z]+)\s*$", righe[indice])
        if not intestazione:
            indice += 1
            continue
        valori = []
        scorri = indice + 1
        while scorri < len(righe) and len(valori) < 6:
            riga = righe[scorri].strip()
            if riga.startswith("|") and "%" in riga:
                valori.extend(int(v) for v in re.findall(r"(\d+)%", riga))
                scorri += 1
            elif riga.startswith("|-") or riga == "":
                scorri += 1
            else:
                break
        if len(valori) == 6:
            tabella[intestazione.group(1)] = dict(zip(CATEGORIE, valori))
            indice = scorri
        else:
            indice += 1
    return tabella


def soglie_degli_assi(cartella):
    soglie = []
    for nome_file, nome_italiano, simbolo in EDIFICI:
        testo = (cartella / (nome_file + ".wikitext")).read_text(encoding="utf-8")
        scheda = re.search(r"\{\{Facility infobox(.*?)^\}\}", testo, re.S | re.M)
        campi = dict(re.findall(r"^\|(\w+)=(.*)$", scheda.group(1), re.M)) if scheda else {}
        soglie.append({
            "edificio": nome_italiano,
            "pagina": nome_file,
            "asso": campi.get("brain", "?").strip(),
            "simbolo": simbolo,
            "serie_argento": int(campi["silver"]) if campi.get("silver", "").strip().isdigit() else None,
            "serie_oro": int(campi["gold"]) if campi.get("gold", "").strip().isdigit() else None,
            "squadra_singolo": campi.get("partsing", "").strip() or None,
            "bp_massimi_per_serie": campi.get("bpr", "").strip() or None,
        })
    return soglie


def main():
    ap = argparse.ArgumentParser(description="Estrae le tabelle numeriche del Parco Lotta dal wikitesto Bulbapedia.")
    ap.add_argument("--grezzo", required=True, help="cartella con i .wikitext prodotti da tools/fetch-bulbapedia.py")
    ap.add_argument("--out", required=True, help="cartella di destinazione dei derivati")
    argomenti = ap.parse_args()

    grezzo = Path(argomenti.grezzo)
    destinazione = Path(argomenti.out)
    destinazione.mkdir(parents=True, exist_ok=True)

    nature = nature_del_palazzo((grezzo / "battle-palace.wikitext").read_text(encoding="utf-8"))
    if len(nature) != 25:
        raise SystemExit("estratte " + str(len(nature)) + " nature invece di 25: la tabella e' cambiata di forma, correggere il lettore invece di fidarsi del derivato")
    anomale = [n for n, q in nature.items()
               if q["attacco"] + q["difesa"] + q["supporto"] != 100
               or q["attacco_sotto50"] + q["difesa_sotto50"] + q["supporto_sotto50"] != 100]
    if anomale:
        raise SystemExit("nature con proporzioni che non sommano a cento: " + ", ".join(sorted(anomale)))
    soglie = soglie_degli_assi(grezzo)

    (destinazione / "palazzo-nature.json").write_text(
        json.dumps(nature, ensure_ascii=False, indent=2), encoding="utf-8", newline="")
    (destinazione / "assi-soglie.json").write_text(
        json.dumps(soglie, ensure_ascii=False, indent=2), encoding="utf-8", newline="")

    print("nature estratte:", len(nature), "(attese 25)")
    for natura, quote in sorted(nature.items()):
        somma_alta = quote["attacco"] + quote["difesa"] + quote["supporto"]
        somma_bassa = quote["attacco_sotto50"] + quote["difesa_sotto50"] + quote["supporto_sotto50"]
        stato = "ok" if somma_alta == 100 and somma_bassa == 100 else "SOMMA ANOMALA " + str(somma_alta) + "/" + str(somma_bassa)
        print("  " + natura.ljust(10) + " sopra " + str(quote["attacco"]).rjust(3) + "/" + str(quote["difesa"]).rjust(3) + "/" + str(quote["supporto"]).rjust(3)
              + "   sotto " + str(quote["attacco_sotto50"]).rjust(3) + "/" + str(quote["difesa_sotto50"]).rjust(3) + "/" + str(quote["supporto_sotto50"]).rjust(3) + "   " + stato)
    print()
    print("soglie degli Assi (serie vinte prima della comparsa):")
    for voce in soglie:
        print("  " + voce["edificio"].ljust(16) + " argento alla serie " + str(voce["serie_argento"]).rjust(2)
              + ", oro alla serie " + str(voce["serie_oro"]).rjust(2) + "   " + voce["asso"])


if __name__ == "__main__":
    main()
