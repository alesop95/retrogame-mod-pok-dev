---
tipo: fonte
livello: 1
letto: si
track: [BRI, LDN, SME]
url: https://github.com/pret/pokefirered
tags: [fonte, livello-1]
corregge: "[[bulbapedia]]"
---

# pret/pokefirered

https://github.com/pret/pokefirered

## Abstract

Decompilazione di Rosso Fuoco e Verde Foglia. Struttura del salvataggio diversa da quella di Smeraldo in ogni offset che conta: chiave di cifratura, conteggio della squadra, denaro e tasche dello zaino.

## Perche' e' in archivio

Ha corretto un errore nel nostro strumento: la chiave sta a 0xF20 dentro un blocco che misura 0xF24, non a 0x0AF8 come riportava la fonte secondaria. Serve anche al track LDN, perche' quelli sono i giochi dello scambio con la Switch.

## A quale punto del progetto serve

- [[22-strumenti]], offset e capienze delle tasche per quel gioco
- [[DATA-FORMATS_Gen1-Gen2-Gen3]], sezione 6, differenze fra i giochi Gen 3

## Relazioni con altre fonti

- corregge un'affermazione di [[bulbapedia]]

## Contesto

Livello 1 di affidabilita' secondo la gerarchia di [[SOURCES]]. Track serviti: BRI, LDN, SME. La mappa di tutte le fonti e delle loro relazioni e' [[index-fonti]].
