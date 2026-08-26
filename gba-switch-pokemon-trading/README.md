# Sottoprogetto: trading wireless locale fra PC e Nintendo Switch

Scambio di Pokemon fra un PC Linux e una Nintendo Switch attraverso LDN, il protocollo wireless locale proprietario di Nintendo, con una copia di FireRed o LeafGreen in esecuzione sulla console. Il PC simula la seconda console. È un proof of concept dimostrativo e non un tool finito.

Il documento di riferimento è `HANDOFF_frlg-ldn-trade.md`, in questa cartella: contiene contesto, glossario, architettura, i due repository su cui il lavoro si appoggia, la procedura operativa in sei fasi, i comandi annotati, i rischi e un elenco onesto delle lacune ancora aperte.

Lo stato canonico del track vive in `.claude/context/sub-gba-switch-trading.md`, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`. Questo file dice cos'è il sottoprogetto; quelli dicono a che punto è.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| contesto, architettura, procedura in sei fasi | `HANDOFF_frlg-ldn-trade.md`, in questa cartella |
| il formato dei dati Pokemon che viaggiano nello scambio | `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`, sezioni 5 e 6 |
| perché quei dati sono cifrati e come si leggono | `docs/04-cifratura-gen3.md` e `docs/06-identita-pokemon.md` |
| il protocollo LDN, i due repository e gli strumenti | `SOURCES.md` alla radice, colonna LDN |
| a che punto è il track e qual è il prossimo passo | `.claude/context/sub-gba-switch-trading.md` |

## Che cosa serve, per come lo dichiarano le due fonti portanti

Un sistema Linux con Python 3.12 o successivo, il privilegio `CAP_NET_ADMIN`, NetworkManager fermo, le chiavi della console, e soprattutto una scheda Wi-Fi capace di ricevere e trasmettere action frame in modalità monitor. Su quest'ultimo punto il proof of concept dichiara affidabili la ALFA AWUS036ACHM e la Realtek RTL8821CE, e poco affidabile la AMD RZ616: è la lista che decide se il track sia praticabile su questa macchina.

La specifica del protocollo non sta nel README della libreria ma nel wiki di NintendoClients, che `SOURCES.md` indicizza: action frame vendor-specific ogni 100 millisecondi con OUI 00:22:AA, canali 1, 6 e 11 in banda 2.4 GHz, advertisement documentato campo per campo, tre livelli di cifratura con chiavi derivate da quelle di console, e indirizzi assegnati nella forma 169.254.X.Y con l'host sempre a 169.254.X.1.

Due avvertenze prima di iniziare, entrambe motivate nell'handoff. Il fattore critico è la scheda Wi-Fi, che deve supportare la modalità monitor, e da quale scheda è disponibile dipende se il track sia praticabile. Le `prod.keys` della console sono materiale di chiave proprietario e non redistribuibile: non entrano nel version control, e il `.gitignore` le esclude insieme ai file di dati `.pk3`.
