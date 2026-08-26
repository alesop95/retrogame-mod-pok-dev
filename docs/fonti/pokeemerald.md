---
tipo: fonte
livello: 1
letto: si
track: [BRI, SME]
url: https://github.com/pret/pokeemerald
tags: [fonte, livello-1]
corregge: "[[bulbapedia]]"
---

# pret/pokeemerald

https://github.com/pret/pokeemerald

## Abstract

Decompilazione di Pokemon Smeraldo in C e assembly ARM che ricompila in una ROM identica. Contiene la struttura cifrata del Pokemon, il calcolo del checksum, la mappa dei settori del salvataggio, la chiave di cifratura e la maschera sulle quantità degli oggetti.

## Perché è in archivio

È la fonte di tutto il lato generazione 3 e l'unica su cui il checksum è verificabile: la sua formula per parole da 16 bit corregge una fonte secondaria che lo descriveva byte per byte, errore che distrugge un Pokemon.

## A quale punto del progetto serve

- [[DATA-FORMATS_Gen1-Gen2-Gen3]], sezioni 5 e 6, struttura cifrata e salvataggio
- [[04-cifratura-gen3]], cifratura, permutazione e checksum
- [[03-integrita-checksum]], checksum di settore
- [[22-strumenti]], offset e chiave usati dallo strumento di diagnosi

## Relazioni con altre fonti

- corregge un'affermazione di [[bulbapedia]]

## Contesto

Livello 1 di affidabilità secondo la gerarchia di [[SOURCES]]. Track serviti: BRI, SME. La mappa di tutte le fonti e delle loro relazioni è [[index-fonti]].
