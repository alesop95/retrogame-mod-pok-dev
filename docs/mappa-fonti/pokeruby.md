---
tipo: fonte
livello: 1
letto: si
track: [BRI, SME]
url: https://github.com/pret/pokeruby
tags: [fonte, livello-1]
---

# pret/pokeruby

https://github.com/pret/pokeruby

## Abstract

Decompilazione di Rubino e Zaffiro. Non ha alcuna chiave di cifratura, quindi le quantità degli oggetti sono in chiaro, ed è l'unico dei tre giochi Gen 3 a comportarsi così. Riclonata il 2026-10-07 al commit 5784633 e letta per il Pokédex: la funzione GetSetPokedexFlag in src/pokedex.c riga 3986, che accetta un contrassegno di specie vista solo se è acceso in tre copie e altrimenti le spegne tutte, e gli offset delle copie in include/global.h.

## Perché è in archivio

Serve come controprova: conferma tutti gli offset che il nostro strumento usava per Rubino e Zaffiro, e la sua assenza di maschera è ciò che rende necessario identificare il gioco prima di leggere lo zaino.

## A quale punto del progetto serve

- [[22-strumenti]], il candidato senza maschera nel rilevamento del gioco

## Contesto

Livello 1 di affidabilità secondo la gerarchia di [[SOURCES]]. Track serviti: BRI, SME. La mappa di tutte le fonti e delle loro relazioni è [[index-fonti]].
