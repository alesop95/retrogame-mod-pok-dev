# Sottoprogetto: modding del Nintendo 3DS e dump delle cartucce possedute

Installare il custom firmware su un Nintendo 3DS e dumpare le cartucce DS e 3DS di proprietà, per conservarle e per poterle usare in emulazione locale. È un runbook operativo su hardware fisico, non un progetto software.

## Che cosa c'è in questa cartella

Dal 2026-11-23 il documento di riferimento è la scheda `.claude/context/sub-3ds-modding.md`, che porta lo stato, il perché di MSET9 e le procedure di dump DS e 3DS travasate dall'handoff (ADR-137). L'handoff `HANDOFF_progetto_3DS.md` e i due file di passo sono conservati identici in `archivio/handoff/3ds-related/`, come storia della console.

Il resoconto dell'installazione del custom firmware (`step02_cfw_mset9.md`) e il registro del dump (`step03_dump_cartucce.md`) servono ancora per il troubleshooting di questa console e si aprono dall'archivio quando servono.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| la procedura di dump da eseguire adesso, e il troubleshooting del seed e della SD | `.claude/context/sub-3ds-modding.md`, sezione «Procedure», e `.claude/context/dev-testing.md` |
| l'handoff originale: perimetro, hardware, dump cartuccia per cartuccia, homebrew | `archivio/handoff/3ds-related/HANDOFF_progetto_3DS.md` |
| come è stato installato il custom firmware, passo per passo | `archivio/handoff/3ds-related/step02_cfw_mset9.md` |
| le guide canoniche e gli strumenti di terze parti | `SOURCES.md` alla radice, colonna 3DS |
| a che punto è il track e qual è il prossimo passo | `.claude/context/sub-3ds-modding.md` |
| gli appunti operativi scritti prima del sistema: dove sta il salvataggio reale rispetto a Checkpoint, i dati sulla SD, l'installazione dei dump da GodMode9, il recap del dump, l'elenco dei giochi dumpati con i title ID, il collegamento all'emulatore Azahar | `appunti/` |

Lo stato canonico del track vive nella scheda, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`. Questo file dice cos'è il sottoprogetto; quelli dicono a che punto è.

Il formato dei salvataggi Pokemon non riguarda questo track, che dumpa file senza interpretarli: se un giorno servisse aprirli, la referenza è `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md` per le generazioni da 1 a 3, e per le successive PKHeX, che `SOURCES.md` elenca.

## Le due avvertenze di perimetro

Il dump si applica soltanto a esemplari di proprietà, e i salvataggi scaricati da internet non si importano su questa console. L'assistenza tecnica non copre Pokemon Bank e Pokemon Transporter su questa console, né file `.cia` di provenienza non chiarita: è un limite dichiarato che vale per tutte le sessioni e non si riapre implicitamente. Limite tolto dal proprietario il 2026-11-17, ADR-132.

Il materiale di chiave console-unica, cioè `movable.sed`, `boot9.bin`, `boot11.bin`, `otp.bin`, i dump della NAND e i seed, è segreto nel senso pieno del termine e non è rigenerabile. Non entra nel version control, non si incolla in una chat e non si carica su servizi di terze parti. Anche l'identificatore della scheda SD, che ne è derivato, va trattato con la stessa riservatezza.
