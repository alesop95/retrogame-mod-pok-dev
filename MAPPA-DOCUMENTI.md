# Mappa dei documenti

Una pagina sola, riscritta da zero il 2026-11-20 su richiesta del proprietario; la versione precedente è conservata identica in `archivio/MAPPA-DOCUMENTI-fino-al-2026-11-20.md`. Per ogni cartella dice a che cosa serve e quali file si aprono. I file segnati come generati non si leggono in sequenza e non si scrivono a mano: li produce lo strumento indicato, e si rigenerano.

## Da dove si comincia

| Domanda | File |
|---|---|
| A che punto è il progetto | `.claude/memory/index.md` |
| Che cosa resta da fare, e chi lo fa | `.claude/memory/pending.md` |
| Che cosa è successo, giorno per giorno | `.claude/memory/progress.md` |
| Perché si è deciso così | `.claude/memory/decisions.md` (ADR-001 e seguenti) |
| Stato di un sottoprogetto | `.claude/context/sub-<nome>.md` |
| Da dove viene un'informazione | `SOURCES.md` |
| Come si lavora qui | `CLAUDE.md` e `.claude/rules/` |

## Memoria e regole, in `.claude/`

| Cartella | A che serve |
|---|---|
| `memory/` | i quattro registri qui sopra, più `lezioni-template.md`; `memory/archivio/` tiene identici i registri prima della riduzione del 2026-11-20 |
| `context/` | una scheda breve per sottoprogetto (`sub-*.md`), le schede trasversali (`STACK.md`, `roadmap.md`, `current-work.md`, `dev-testing.md`, `design-and-security.md`) e il livello didattico (`studio-didattico-master.md` con le schede `refactor-NN`) |
| `rules/`, `skills/`, `norme/` | le regole sempre attive, le procedure e la loro motivazione, ereditate dal template |
| `templates/` | i modelli del template; non si modificano qui, li porta l'allineamento |

## Sottoprogetti

| Cartella | A che serve | Si apre | Generati |
|---|---|---|---|
| `pokedex-home-completo/` | il fuoco: tutte le specie e gli esemplari in HOME prima della chiusura di Bank | `ROADMAP.md`, `COPIE-PER-HOME.md`, `RUNBOOK-PASSO-2.md`, `RUNBOOK-ESTRAZIONI.md`, `CATENA-DI-TRASFERIMENTO.md`, gli `STUDIO-NN` | `pedigree/` (`tools/stampa-collezione.py`), i `CENSIMENTO-*`, `LISTA-COMPLETA.md`, `DATE-INCONTRO.md`, `FIOCCHI*`, `SFERE-*`, `SFIDE-BANK.md`, `ELENCO-*`; solo su disco e non in git dal 2026-11-20: `CHECKLIST-COMPLETA.md`, `SCHEDE-EVENTI-GB.md`, `SCHEDE-ESCLUSIVI.md`, `CENSIMENTO-EVENTI-FUORI-DONI.md`, `STUDIO-SWITCH.md`, `SPOGLIO-CORPUS.md` |
| `gba-save-extraction-smeraldo/` | le cartucce GBA di Smeraldo e Rubino: correzioni, scritture, collezione di terza generazione | `README.md`, `RUNBOOK-RUBINO-SID-POKEDEX.md`, gli `STUDIO-NN` | `MAPPA-BOX-SMERALDO.md`, `MAPPA-BOX-RUBINO.md`, `PIANO-BOX.md`, `GUIDA-PARCO-LOTTA.md` (`tools/emerald_mappa_box.py` e altri) |
| `recreate-pokemon-distributions-events/` | gli eventi di distribuzione e come si ricreano | `README.md`, gli `STUDIO-NN` | `CATALOGO-EVENTI.md`, `EVENTI-GEN3.md`; solo su disco: `SCHEDE-ESEMPLARI.md`, `SCHEDE-ESEMPLARI-GEN4.md` |
| `pokemon-gen12-gen3-bridge-original-hardware/` | il ponte fra le generazioni su hardware originale, con il pacchetto `pokebridge` | `DATA-FORMATS_Gen1-Gen2-Gen3.md` | |
| `3ds-related/` | il 3DS modificato e i dump delle cartucce | `README.md`, `handoff/` | |
| `switch-modding/` | la Switch modificata per la fase Switch | `STUDIO-01-switch-usata-da-modificare.md` | |
| `poke-ace/` | esecuzione di codice e legittimità di ciò che produce | gli `STUDIO-NN` | |
| `cart-battery-restoration/` | la pila tampone delle cartucce | `STUDIO-01-batteria-e-ritenzione.md` | |
| `gba-switch-pokemon-trading/` | lo scambio fra GBA e Switch, ricerca conclusa | la scheda `.claude/context/sub-gba-switch-trading.md`; l'handoff è in `archivio/handoff/` | |
| `generation-from-switch/`, `poke-automation-study/` | due track in studio | il loro `STUDIO-01` | |

## Trasversali

| Percorso | A che serve |
|---|---|
| `tools/` | gli strumenti: generatori, controlli, strumenti PKHeX in C#; ogni file dice in testa perché esiste e come si usa |
| `docs/` | il percorso di studio tecnico, da `docs/index.md`; `docs/mappa-fonti/` è generata da `tools/build-source-map.py`, una nota per fonte, ed è il grafo delle fonti nel vault |
| `SOURCES.md` | il registro delle fonti, con il sottoprogetto che ciascuna serve |
| `archivio/` | documenti tolti dall'uso e conservati identici: la mappa precedente, la wiki `knowledge/` mai popolata e, dal 2026-11-23, i cinque handoff in `handoff/` (ADR-137) |
| `_vault/` | il vault di Obsidian, fatto di soli collegamenti; si ricrea con `python tools/vault-progetto.py crea` e non è in git |

## Fuori da git

`_notes/` tiene salvataggi, lotti, cloni dei disassemblati, fonti scaricate, consegne del proprietario e il file di ripresa; il suo registro dei salvataggi è `_notes/salvataggi/cartucce/LEGGIMI.md`. `tesi/` è il documento composto locale. Nessuno dei due entra nel repository.
