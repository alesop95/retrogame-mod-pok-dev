"""Ricava la corrispondenza fra i nomi inglesi delle mosse del catalogo e i nomi italiani che il
gioco mostra, accoppiandoli posizione per posizione su un dump dei box esportato da PKHeX.

Il glossario non si scrive a mano e non si traduce: si deduce da una misura. Il catalogo dichiara le
mosse in inglese perche' quella e' la lingua del sorgente, mentre sulla cartuccia italiana il
giocatore legge altro, e la distanza fra le due grafie e' la ragione per cui un insieme corretto puo'
sembrare irriconoscibile. Accoppiare le due liste nella stessa posizione dello stesso esemplare
produce la corrispondenza senza alcuna inferenza.

Uso: python tools/parco_lotta_glossario_mosse.py --catalogo <json> --dump <csv> --out <md>
"""

import argparse
import csv
import io
import json


def principale():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--catalogo", required=True)
    p.add_argument("--dump", required=True)
    p.add_argument("--out", required=True)
    a = p.parse_args()

    catalogo = json.loads(io.open(a.catalogo, encoding="utf-8").read())
    righe = list(csv.DictReader(io.open(a.dump, encoding="utf-8-sig")))

    # L'accoppiamento fra il catalogo e il dump non passa da specie e natura, perche' il dump scrive
    # la natura gia' tradotta, che e' proprio la differenza da misurare; e non passa dai punti base,
    # perche' i due Latios li hanno identici. Passa dall'ordine, che e' esatto: il generatore scrive
    # gli esemplari in ordine di chiave e ne scrive due copie ciascuno, quindi la riga 2i e la 2i+1
    # del dump sono le due copie della i-esima chiave. L'ordine si verifica invece di essere creduto,
    # confrontando la specie a ogni passo, e un disallineamento interrompe con il punto in cui cade.
    chiavi = sorted(catalogo["esemplari"])
    copie = catalogo["copie_per_esemplare"]
    if len(righe) != len(chiavi) * copie:
        raise SystemExit("il dump ha %d righe e il catalogo ne prevede %d: il dump non e' di questo "
                         "catalogo, e l'accoppiamento per ordine non e' applicabile"
                         % (len(righe), len(chiavi) * copie))

    # Una corrispondenza si accetta solo se e' unanime su tutte le occorrenze. Una mossa cambiata nel
    # catalogo dopo l'esportazione del dump produce un disaccordo, ed e' giusto che resti fuori
    # invece di entrare con il nome della mossa che ha sostituito.
    voti = {}
    voti_natura = {}
    for i, chiave in enumerate(chiavi):
        voce = catalogo["esemplari"][chiave]
        for r in righe[i * copie:(i + 1) * copie]:
            if r["Species"] != voce["specie"]:
                raise SystemExit("disallineamento alla chiave %s: il dump dice %s e il catalogo %s"
                                 % (chiave, r["Species"], voce["specie"]))
            voti_natura.setdefault(voce["natura"], set()).add(r["Nature"])
            for k, en in enumerate(voce["mosse"]):
                it = r.get("Move%d" % (k + 1), "").strip()
                if it and not it.startswith("("):
                    voti.setdefault(en, set()).add(it)

    glossario = {en: next(iter(v)) for en, v in voti.items() if len(v) == 1}
    nature = {en: next(iter(v)) for en, v in voti_natura.items() if len(v) == 1}
    conflitti = [(en, sorted(v)) for en, v in sorted(voti.items()) if len(v) > 1]
    conflitti += [(en, sorted(v)) for en, v in sorted(voti_natura.items()) if len(v) > 1]

    fuori = io.open(a.out, "w", encoding="utf-8", newline="\n")
    fuori.write("# Glossario delle mosse del lotto, inglese del catalogo contro italiano sullo schermo\n\n")
    fuori.write("Documento generato da `tools/parco_lotta_glossario_mosse.py`, che non traduce nulla: accoppia le due liste di mosse dello stesso esemplare nella stessa posizione, prendendo l'inglese dal catalogo e l'italiano dal dump dei box di PKHeX. Serve a una domanda sola, cioe' riconoscere sulla cartuccia italiana l'insieme che il catalogo dichiara in inglese, perche' la distanza fra le due grafie e' la ragione per cui un insieme giusto puo' sembrare irriconoscibile: Frana e Rock Slide sono la stessa mossa, e Breccia e Brick Break anche.\n\n")
    fuori.write("Le due fonti di questa corsa sono il catalogo %s e il dump %s. La coppia conta, perche' un dump esportato prima di una modifica del catalogo produrrebbe corrispondenze sfasate di una mossa: quando il catalogo cambia, il glossario si rigenera sul dump corrispondente, e per un giro gia' archiviato lo si rigenera sul catalogo di quel giro preso dalla storia del repository.\n\n" % (a.catalogo, a.dump))
    fuori.write("| Nome nel catalogo | Nome sullo schermo in italiano |\n|---|---|\n")
    for en in sorted(glossario):
        fuori.write("| %s | %s |\n" % (en, glossario[en]))
    fuori.write("\nLo stesso accoppiamento, applicato alle nature, produce il glossario che segue. Vale la stessa avvertenza gia' registrata sul nome Contatore: PKHeX mostra la localizzazione corrente e non quella dell'epoca, quindi questa tabella dice come si legge il dump, e per i nomi che il gioco del 2004 mostrava resta autorevole la wiki italiana.\n\n")
    fuori.write("| Natura nel catalogo | Natura nel dump |\n|---|---|\n")
    for en in sorted(nature):
        fuori.write("| %s | %s |\n" % (en, nature[en]))
    if conflitti:
        fuori.write("\nCorrispondenze in conflitto, da guardare a mano.\n\n")
        for en, valori in conflitti:
            fuori.write("- %s compare come %s: o il catalogo e' cambiato dopo l'esportazione del dump, oppure due voci si sovrappongono\n" % (en, " e come ".join(valori)))
    fuori.close()
    print("%d corrispondenze scritte in %s" % (len(glossario), a.out))
    if conflitti:
        print("ATTENZIONE: %d conflitti" % len(conflitti))


if __name__ == "__main__":
    principale()
