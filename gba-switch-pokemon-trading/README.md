# Sottoprogetto: trading wireless locale fra PC e Nintendo Switch

Scambio di Pokemon fra un PC Linux e una Nintendo Switch attraverso LDN, il protocollo wireless locale proprietario di Nintendo, con una copia di FireRed o LeafGreen in esecuzione sulla console. Il PC simula la seconda console. E' un proof of concept dimostrativo e non un tool finito.

Il documento di riferimento e' `HANDOFF_frlg-ldn-trade.md`, in questa cartella: contiene contesto, glossario, architettura, i due repository su cui il lavoro si appoggia, la procedura operativa in sei fasi, i comandi annotati, i rischi e un elenco onesto delle lacune ancora aperte.

Lo stato canonico del track vive in `.claude/context/sub-gba-switch-trading.md`, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`. Questo file dice cos'e' il sottoprogetto; quelli dicono a che punto e'.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| contesto, architettura, procedura in sei fasi | `HANDOFF_frlg-ldn-trade.md`, in questa cartella |
| il formato dei dati Pokemon che viaggiano nello scambio | `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`, sezioni 5 e 6 |
| perche' quei dati sono cifrati e come si leggono | `docs/04-cifratura-gen3.md` e `docs/06-identita-pokemon.md` |
| il protocollo LDN, i due repository e gli strumenti | `SOURCES.md` alla radice, colonna LDN |
| a che punto e' il track e qual e' il prossimo passo | `.claude/context/sub-gba-switch-trading.md` |

Due avvertenze prima di iniziare, entrambe motivate nell'handoff. Il fattore critico e' la scheda Wi-Fi, che deve supportare la modalita' monitor, e da quale scheda e' disponibile dipende se il track sia praticabile. Le `prod.keys` della console sono materiale di chiave proprietario e non redistribuibile: non entrano nel version control, e il `.gitignore` le esclude insieme ai file di dati `.pk3`.
