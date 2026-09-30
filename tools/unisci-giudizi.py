#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aggiunge al registro unico dei giudizi le voci di uno o più file di giudizio di un lotto.

Perché esiste
-------------
Il registro unico `recreate-pokemon-distributions-events/giudizi-pkhex-core.json` è scritto da
`tools/pkhex-giudica`, che lo serializza con il formato .NET: fine riga CRLF, rientro di due spazi e
caratteri escapati. Rigiudicare tutti i lotti per aggiungerne uno costa minuti e chiede di ricordare il
contesto di ciascuno, mentre riscrivere il file con `json` di Python ne cambia la formattazione e produce un
diff di decine di migliaia di righe. Questo strumento inserisce le voci nuove sul testo, prese dai file di
giudizio che lo stesso `pkhex-giudica` scrive per un lotto e che hanno quindi lo stesso formato, e aggiorna
il conteggio dei conformi. Rifiuta una voce già presente e un giudizio che non sia conforme.

Uso
---
    python tools/unisci-giudizi.py <giudizio.json> [<giudizio.json> ...]
"""

import io
import json
import re
import sys

REGISTRO = "recreate-pokemon-distributions-events/giudizi-pkhex-core.json"


def corpo_voci(testo):
    """Il testo fra la graffa di apertura di `voci`, che è l'ultimo campo, e la chiusura del documento."""
    inizio = testo.index('"voci": {') + len('"voci": {')
    fine = len(testo.rstrip().rstrip('}').rstrip().rstrip('}').rstrip())
    return inizio, fine


def main(argv):
    if not argv:
        sys.exit(__doc__)
    registro = io.open(REGISTRO, encoding="utf-8", newline="").read()
    presenti = set(json.loads(registro)["voci"])
    aggiunte = []
    for percorso in argv:
        testo = io.open(percorso, encoding="utf-8", newline="").read()
        dati = json.loads(testo)
        if list(dati)[-1] != "voci":
            sys.exit("il campo voci non è l'ultimo in " + percorso)
        for chiave, voce in dati["voci"].items():
            if chiave in presenti:
                sys.exit("voce già nel registro: " + chiave)
            if voce.get("esito") != "conforme":
                sys.exit("voce non conforme, non la aggiungo: " + chiave)
        inizio, fine = corpo_voci(testo)
        aggiunte.append(testo[inizio:fine])
    fine = corpo_voci(registro)[1]
    registro = registro[:fine] + "".join("," + a for a in aggiunte) + registro[fine:]
    conformi = sum(1 for v in json.loads(registro)["voci"].values() if v["esito"] == "conforme")
    registro = re.sub(r'"conformi": \d+', '"conformi": %d' % conformi, registro, count=1)
    io.open(REGISTRO, "w", encoding="utf-8", newline="").write(registro)
    print("registro: %d conformi" % conformi)


if __name__ == "__main__":
    main(sys.argv[1:])
