#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scrive il documento del complemento di terza generazione per il Rubino di prova, dal rapporto del generatore.

Perche' esiste
--------------
Il complemento di ADR-080 vive in `_notes/lotto-complemento-rubino/`, che git ignora come tutti i lotti,
e il rapporto che `tools/pkhex-genera` scrive accanto ai file e' un JSON per programmi. Questo documento
e' la sua forma leggibile e versionata: che cosa c'e', perche', da quale voce della libreria, con quale
allenatore, e l'impronta di ciascun file, cosi' che un clone sappia che cosa il lotto contiene senza
contenerlo.

Uso
---
    python tools/complemento-rubino-md.py

Scrive `pokedex-home-completo/COMPLEMENTO-RUBINO.md`.
"""

import collections
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = Path(__file__).resolve().parents[1]
LOTTO = RADICE.joinpath("_notes", "lotto-complemento-rubino")
USCITA = RADICE.joinpath("pokedex-home-completo", "COMPLEMENTO-RUBINO.md")
NOMI = RADICE.joinpath("_notes", "fonti", "pkhex", "PKHeX.Core", "Resources", "text", "other", "it", "text_Species_it.txt")
GRUPPI = [("statico", "Incontri statici, doni e uova dei portatili"), ("incontro speciale", "Incontri speciali dei selvatici"), ("dono", "Doni di Colosseum e di XD"),
          ("evento", "Evento"), ("starter", "Starter di Colosseum"), ("Ombra di Colosseum", "Ombra di Colosseum"),
          ("Ombra di XD", "Ombra di XD"), ("scambio", "Scambi di XD"), ("forma", "Forme di Unown"),
          ("esclusivo", "Esclusivi di versione"), ("mossa", "Portatori di mosse perdute"), ("fiocchi", "Portatore dei fiocchi"),
          ("specie", "Specie che nessuna voce speciale copriva")]


def gruppo(motivo):
    for chiave, titolo in GRUPPI:
        if motivo.startswith(chiave):
            return titolo
    return "Altro"


def main():
    rapporto = json.loads(LOTTO.joinpath("esemplari", "rapporto.json").read_text(encoding="utf-8"))
    nomi = NOMI.read_text(encoding="utf-8").split("\n")
    per_gruppo = collections.OrderedDict((t, []) for _, t in GRUPPI)
    for e in rapporto["esiti"]:
        per_gruppo.setdefault(gruppo(e["motivo"]), []).append(e)
    md = ["# Il complemento di terza generazione per il Rubino di prova", "",
          "> Documento generato da `tools/complemento-rubino-md.py` dal rapporto di `tools/pkhex-genera`. Non si modifica a mano: si rigenera. I file stanno in `_notes/lotto-complemento-rubino/esemplari/`, fuori da git; le richieste da cui nascono le scrive `tools/manifesto-complemento-rubino.py`, e il ragionamento sta in `STUDIO-10-la-libreria-del-verificatore-come-generatore.md`.", "",
          "Esemplari generati e giudicati legali dalla libreria del verificatore: %d su %d richieste." % (rapporto["riuscite"], rapporto["richieste"]), "",
          "## Gli allenatori", "", "| Gioco | Allenatore | Identificativo | Segreto |", "|---|---|---|---|"]
    for sigla, a in rapporto["allenatori"].items():
        md.append("| %s | %s | %d | %d |" % (sigla, a["OT"], a["TID16"], a["SID16"]))
    md += ["", "L'allenatore Alessio di ciascun gioco non corrisponde a una partita reale: è un allenatore valido, cioè con un identificativo che quel gioco può produrre, che avrebbe potuto giocare un'ipotetica partita di quel gioco. Gli esemplari con allenatore fisso, cioè i doni di Colosseum, gli scambi di XD e il Jirachi di Pokémon Channel, portano l'allenatore che la voce della tabella impone.", "",
           "## Riepilogo", "", "| Gruppo | Esemplari |", "|---|---|"]
    md += ["| %s | %d |" % (t, len(v)) for t, v in per_gruppo.items() if v]
    for titolo, voci in per_gruppo.items():
        if not voci:
            continue
        md += ["", "## %s" % titolo, "", "| Richiesta | Pokémon | Livello | Voce della libreria | Allenatore | Motivo | SHA-256 |", "|---|---|---|---|---|---|---|"]
        for e in voci:
            if "file" not in e:
                md.append("| %s | non generato |  |  |  | %s | %s |" % (e["id"], e["motivo"], e.get("difetto", "")))
                continue
            md.append("| %s | %s | %d | %s | %s | %s | `%s…%s` |" % (
                e["id"], nomi[e["specie"]], e["livello"], e["voce"], e["allenatore"], e["motivo"].replace("|", "/"),
                e["sha256"][:8], e["sha256"][-8:]))
    USCITA.write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")
    print("scritto %s" % USCITA)


if __name__ == "__main__":
    main()
