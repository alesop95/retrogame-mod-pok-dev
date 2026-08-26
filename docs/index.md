---
tipo: indice
tags: [indice, studio]
---

# Percorso di studio tecnico

Questa cartella è il percorso di studio del progetto. Non è documentazione di stato e non è un manuale operativo: è il materiale che serve a capire, a livelli crescenti di profondità, come sono fatti i dati dei giochi su cui il progetto lavora e come si costruisce il software che li manipola. Lo stato di avanzamento sta altrove, in `.claude/memory/index.md`, e le procedure su hardware fisico stanno negli handoff dei rispettivi sottoprogetti.

La cartella è pensata per essere aperta come vault Obsidian con la radice del repository come cartella di lavoro, così che i collegamenti fra note e verso i documenti tecnici e le schede si vedano come grafo. Ogni nota dichiara nel proprio frontmatter il livello e i suoi collegamenti, e ogni nota rimanda alla riga del registro delle fonti da cui viene ciò che afferma.

## Come si legge

Il percorso ha tre livelli e una coda. Le fondamenta servono a chi non ha mai aperto un salvataggio con un editor esadecimale, e non danno per scontato nulla. Il livello intermedio spiega i meccanismi che rendono un salvataggio più di un file di byte, cioè integrità, cifratura e codifica. Il livello avanzato affronta i problemi che non hanno una soluzione unica, cioè la conversione fra generazioni e il trasporto dei dati fra due console. La coda riguarda il software che scriveremo, la sua architettura e il suo collaudo.

Chi vuole soltanto gli offset non ha bisogno di questo percorso: gli serve [[DATA-FORMATS_Gen1-Gen2-Gen3]], che è la referenza byte per byte e sta accanto al sottoprogetto del ponte.

## Fondamenta

| Nota | Che cosa risolve |
|---|---|
| [[01-fondamenta-salvataggio]] | che cos'è un salvataggio, su che supporto vive, perché il backup non è negoziabile |
| [[02-numeri-e-bit]] | ordine dei byte, nibble, campi di bit, e perché un errore qui non fa rumore |

## Livello intermedio

| Nota | Che cosa risolve |
|---|---|
| [[03-integrita-checksum]] | i tre algoritmi di checksum delle tre generazioni e cosa succede quando non tornano |
| [[04-cifratura-gen3]] | perché la generazione 3 cifra e permuta, e come si legge e riscrive quel blocco |
| [[05-testo-e-charmap]] | perché nessuna generazione usa ASCII, e come si transcodifica un nome senza sbagliare |
| [[06-identita-pokemon]] | che cosa identifica un Pokemon in ciascuna generazione, fra indici, DV, IV e valore di personalità |

## Livello avanzato

| Nota | Che cosa risolve |
|---|---|
| [[07-conversione-vincoli]] | la conversione come problema di soddisfacimento di vincoli, e dove stanno i gradi di libertà |
| [[08-cavo-link]] | il protocollo seriale del Game Boy, blocco per blocco |
| [[09-esecuzione-codice]] | come si arriva a far eseguire codice proprio a un gioco del 1996, e perché il ponte lo fa |
| [[10-multiboot-hardware]] | il lato Game Boy Advance, fra multiboot e scambio a caldo della cartuccia |
| [[11-wireless-locale-e-ponte-switch]] | il protocollo di rete locale della Switch, la modalità monitor, e il ponte verso una console moderna |

## Il software che scriveremo

| Nota | Che cosa risolve |
|---|---|
| [[20-architettura-codice]] | come si stratifica il codice perché resti valido qualunque opzione si scelga |
| [[21-collaudo]] | che cosa si collauda su dati sintetici, che cosa su emulatore e che cosa solo su ferro |
| [[22-strumenti]] | gli strumenti che il progetto ha già, cosa fanno e come si rilanciano |
| [[23-prove-eseguite]] | l'inventario di ciò che è stato verificato, con che cosa, e di ciò che non lo è |

## Decisioni e riferimenti

| Nota | Che cosa contiene |
|---|---|
| [[24-fonti-di-community]] | perché alcune informazioni esistono solo in una chat, come si esportano e a quale costo |
| [[30-opzioni-implementative]] | le quattro strade di ADR-008, il loro costo reale alla luce di ciò che sappiamo oggi |
| [[31-glossario]] | i termini che ricorrono in tutto il progetto |

## Da quale sottoprogetto arrivi

I cinque sottoprogetti hanno scopi diversi e quindi hanno bisogno di cose diverse da questo percorso. Il punto di ingresso di ciascuno è il `README.md` della sua cartella, che dice cos'è il sottoprogetto e dove sta la sua conoscenza; questa tabella dice quali note servono a chi.

| Sottoprogetto | Che cosa è | Note che gli servono |
|---|---|---|
| `pokemon-gen12-gen3-bridge-original-hardware/` | l'unico che diventa software: il ponte fra generazioni | tutte, più [[DATA-FORMATS_Gen1-Gen2-Gen3]] come referenza |
| `gba-save-extraction-smeraldo/` | runbook: riparare un inventario corrotto su cartuccia | [[01-fondamenta-salvataggio]], [[03-integrita-checksum]], [[04-cifratura-gen3]], [[22-strumenti]] |
| `3ds-related/` | runbook: modding della console e dump delle cartucce | nessuna in modo diretto, perché dumpa file senza interpretarli; [[01-fondamenta-salvataggio]] se un giorno servisse aprirli |
| `gba-switch-pokemon-trading/` | reverse engineering di rete fra PC e Switch | [[11-wireless-locale-e-ponte-switch]] per prima, poi [[06-identita-pokemon]] e [[04-cifratura-gen3]], perché i dati scambiati sono strutture Gen 3 |
| `poke-automation-study/` | studio dell'automazione su Switch, scopo da definire | la nota di studio vive nella cartella del sottoprogetto, cioè `poke-automation-study/STUDIO-01-architettura-e-perimetro.md`, perché studia un progetto esterno e non il nostro codice; la sovrapposizione con il ponte è il microcontrollore, trattato in [[30-opzioni-implementative]] |

Il formato dei dati Gen 3 è quindi la conoscenza più trasversale del progetto: serve al ponte per costruirlo, a Smeraldo per diagnosticarlo e allo scambio con la Switch per interpretarlo. È la ragione per cui la referenza vive accanto al ponte ma è citata dalle schede degli altri.

## La mappa delle fonti

Le fonti che portano peso tecnico hanno una nota propria sotto `docs/fonti/`, con abstract, motivo per cui sono in archivio, punto esatto del progetto che servono e relazioni verso le altre fonti. L'indice è [[index-fonti]], e da là il grafo di Obsidian mostra chi conferma chi, chi corregge chi e chi discende da chi. Il registro completo, comprese le voci minori e quelle non lette, resta [[SOURCES]].

## Ancoraggi fuori da questa cartella

La referenza byte per byte è [[DATA-FORMATS_Gen1-Gen2-Gen3]]. Il registro delle fonti, con la colonna che dice a quale sottoprogetto serve ciascuna voce, è [[SOURCES]]. Lo stato dei quattro track e la riga del fuoco corrente stanno in `.claude/memory/index.md`, le decisioni in `.claude/memory/decisions.md`, e le regole normative sull'hardware in `.claude/rules/hardware-and-perimeter.md`, che va letta prima di qualsiasi operazione fisica.
