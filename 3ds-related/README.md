# Sottoprogetto: modding del Nintendo 3DS e dump delle cartucce possedute

Installare il custom firmware su un Nintendo 3DS e dumpare le cartucce DS e 3DS di proprieta', per conservarle e per poterle usare in emulazione locale. E' un runbook operativo su hardware fisico, non un progetto software.

## Che cosa c'e' in questa cartella

Il documento di riferimento e' `handoff/HANDOFF_progetto_3DS.md`, che contiene il perimetro vincolante del sottoprogetto, l'inventario dell'hardware, lo stato di avanzamento dei dump cartuccia per cartuccia, l'elenco dell'homebrew installato con le versioni verificate e l'analisi del percorso verso i servizi in rete.

Accanto stanno i due passi documentati singolarmente. `handoff/step02_cfw_mset9.md` e' il resoconto dell'installazione del custom firmware su questa console, con le versioni e i problemi incontrati: e' storia, ma e' la storia di questa console e serve come riferimento in caso di troubleshooting. `handoff/step03_dump_cartucce.md` e' la procedura di dump, ed e' il passo attivo, perche' restano cinque cartucce DS da dumpare.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| perimetro, hardware, stato dei dump | `handoff/HANDOFF_progetto_3DS.md` |
| la procedura di dump da eseguire adesso | `handoff/step03_dump_cartucce.md` |
| come e' stato installato il custom firmware | `handoff/step02_cfw_mset9.md` |
| le guide canoniche e gli strumenti di terze parti | `SOURCES.md` alla radice, colonna 3DS |
| a che punto e' il track e qual e' il prossimo passo | `.claude/context/sub-3ds-modding.md` |

Lo stato canonico del track vive nella scheda, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`. Questo file dice cos'e' il sottoprogetto; quelli dicono a che punto e'.

Il formato dei salvataggi Pokemon non riguarda questo track, che dumpa file senza interpretarli: se un giorno servisse aprirli, la referenza e' `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md` per le generazioni da 1 a 3, e per le successive PKHeX, che `SOURCES.md` elenca.

## Le due avvertenze di perimetro

Il dump si applica soltanto a esemplari di proprieta', e i salvataggi scaricati da internet non si importano su questa console. L'assistenza tecnica non copre Pokemon Bank e Pokemon Transporter su questa console, ne' file `.cia` di provenienza non chiarita: e' un limite dichiarato che vale per tutte le sessioni e non si riapre implicitamente.

Il materiale di chiave console-unica, cioe' `movable.sed`, `boot9.bin`, `boot11.bin`, `otp.bin`, i dump della NAND e i seed, e' segreto nel senso pieno del termine e non e' rigenerabile. Non entra nel version control, non si incolla in una chat e non si carica su servizi di terze parti. Anche l'identificatore della scheda SD, che ne e' derivato, va trattato con la stessa riservatezza.
