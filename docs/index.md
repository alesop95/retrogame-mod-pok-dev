---
tipo: indice
tags: [indice, studio]
---

# Percorso di studio tecnico

Questa cartella e' il percorso di studio del progetto. Non e' documentazione di stato e non e' un manuale operativo: e' il materiale che serve a capire, a livelli crescenti di profondita', come sono fatti i dati dei giochi su cui il progetto lavora e come si costruisce il software che li manipola. Lo stato di avanzamento sta altrove, in `.claude/memory/index.md`, e le procedure su hardware fisico stanno negli handoff dei rispettivi sottoprogetti.

La cartella e' pensata per essere aperta come vault Obsidian con la radice del repository come cartella di lavoro, cosi' che i collegamenti fra note e verso i documenti tecnici e le schede si vedano come grafo. Ogni nota dichiara nel proprio frontmatter il livello e i suoi collegamenti, e ogni nota rimanda alla riga del registro delle fonti da cui viene cio' che afferma.

## Come si legge

Il percorso ha tre livelli e una coda. Le fondamenta servono a chi non ha mai aperto un salvataggio con un editor esadecimale, e non danno per scontato nulla. Il livello intermedio spiega i meccanismi che rendono un salvataggio piu' di un file di byte, cioe' integrita', cifratura e codifica. Il livello avanzato affronta i problemi che non hanno una soluzione unica, cioe' la conversione fra generazioni e il trasporto dei dati fra due console. La coda riguarda il software che scriveremo, la sua architettura e il suo collaudo.

Chi vuole soltanto gli offset non ha bisogno di questo percorso: gli serve [[DATA-FORMATS_Gen1-Gen2-Gen3]], che e' la referenza byte per byte e sta accanto al sottoprogetto del ponte.

## Fondamenta

| Nota | Che cosa risolve |
|---|---|
| [[01-fondamenta-salvataggio]] | che cos'e' un salvataggio, su che supporto vive, perche' il backup non e' negoziabile |
| [[02-numeri-e-bit]] | ordine dei byte, nibble, campi di bit, e perche' un errore qui non fa rumore |

## Livello intermedio

| Nota | Che cosa risolve |
|---|---|
| [[03-integrita-checksum]] | i tre algoritmi di checksum delle tre generazioni e cosa succede quando non tornano |
| [[04-cifratura-gen3]] | perche' la generazione 3 cifra e permuta, e come si legge e riscrive quel blocco |
| [[05-testo-e-charmap]] | perche' nessuna generazione usa ASCII, e come si transcodifica un nome senza sbagliare |
| [[06-identita-pokemon]] | che cosa identifica un Pokemon in ciascuna generazione, fra indici, DV, IV e valore di personalita' |

## Livello avanzato

| Nota | Che cosa risolve |
|---|---|
| [[07-conversione-vincoli]] | la conversione come problema di soddisfacimento di vincoli, e dove stanno i gradi di liberta' |
| [[08-cavo-link]] | il protocollo seriale del Game Boy, blocco per blocco |
| [[09-esecuzione-codice]] | come si arriva a far eseguire codice proprio a un gioco del 1996, e perche' il ponte lo fa |
| [[10-multiboot-hardware]] | il lato Game Boy Advance, fra multiboot e scambio a caldo della cartuccia |

## Il software che scriveremo

| Nota | Che cosa risolve |
|---|---|
| [[20-architettura-codice]] | come si stratifica il codice perche' resti valido qualunque opzione si scelga |
| [[21-collaudo]] | che cosa si collauda su dati sintetici, che cosa su emulatore e che cosa solo su ferro |
| [[22-strumenti]] | gli strumenti che il progetto ha gia', cosa fanno e come si rilanciano |

## Decisioni e riferimenti

| Nota | Che cosa contiene |
|---|---|
| [[30-opzioni-implementative]] | le quattro strade di ADR-008, il loro costo reale alla luce di cio' che sappiamo oggi |
| [[31-glossario]] | i termini che ricorrono in tutto il progetto |

## Da quale sottoprogetto arrivi

I quattro sottoprogetti hanno scopi diversi e quindi hanno bisogno di cose diverse da questo percorso. Il punto di ingresso di ciascuno e' il `README.md` della sua cartella, che dice cos'e' il sottoprogetto e dove sta la sua conoscenza; questa tabella dice quali note servono a chi.

| Sottoprogetto | Che cosa e' | Note che gli servono |
|---|---|---|
| `pokemon-gen12-gen3-bridge-original-hardware/` | l'unico che diventa software: il ponte fra generazioni | tutte, piu' [[DATA-FORMATS_Gen1-Gen2-Gen3]] come referenza |
| `gba-save-extraction-smeraldo/` | runbook: riparare un inventario corrotto su cartuccia | [[01-fondamenta-salvataggio]], [[03-integrita-checksum]], [[04-cifratura-gen3]], [[22-strumenti]] |
| `3ds-related/` | runbook: modding della console e dump delle cartucce | nessuna in modo diretto, perche' dumpa file senza interpretarli; [[01-fondamenta-salvataggio]] se un giorno servisse aprirli |
| `gba-switch-pokemon-trading/` | reverse engineering di rete fra PC e Switch | [[06-identita-pokemon]] e [[04-cifratura-gen3]], perche' i dati scambiati sono strutture Gen 3 |

Il formato dei dati Gen 3 e' quindi la conoscenza piu' trasversale del progetto: serve al ponte per costruirlo, a Smeraldo per diagnosticarlo e allo scambio con la Switch per interpretarlo. E' la ragione per cui la referenza vive accanto al ponte ma e' citata dalle schede degli altri.

## Ancoraggi fuori da questa cartella

La referenza byte per byte e' [[DATA-FORMATS_Gen1-Gen2-Gen3]]. Il registro delle fonti, con la colonna che dice a quale sottoprogetto serve ciascuna voce, e' [[SOURCES]]. Lo stato dei quattro track e la riga del fuoco corrente stanno in `.claude/memory/index.md`, le decisioni in `.claude/memory/decisions.md`, e le regole normative sull'hardware in `.claude/rules/hardware-and-perimeter.md`, che va letta prima di qualsiasi operazione fisica.
