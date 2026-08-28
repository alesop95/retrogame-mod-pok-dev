---
tipo: fonte
livello: 4
letto: si
track: [EVT, BRI]
url: https://www.youtube.com/watch?v=NKBb-YS34wg
tags: [fonte, livello-4]
conferma: "[[pokeemerald]]"
documenta: "[[gen3distributions]]"
---

# Goppier, la ricreazione delle distribuzioni Gen 3

https://www.youtube.com/watch?v=NKBb-YS34wg

## Abstract

Racconto tecnico della ricreazione di tutte le distribuzioni di eventi di terza generazione, inglesi, giapponesi e da GameCube, trascritto e letto per intero il 2026-08-28. Descrive come si trova il multiboot dentro la ROM di distribuzione confrontando i byte che passano sul cavo, come lo si decomprime attraverso la chiamata di sistema del BIOS, come si aggira il checksum additivo che ne difende l'integrità, e come si impostano i parametri dell'esemplare riusando il codice del gioco per indice di parametro.

## Perché è in archivio

È la sola fonte esistente sul formato interno di una ROM di distribuzione, e porta due contributi che il progetto non aveva. Il primo è la conferma indipendente, ottenuta per reverse engineering e non dal disassemblato, che il salvataggio di terza generazione ha quattordici sezioni che ruotano fra gli slot e due copie alternate, con la posta nella sezione quattro. Il secondo è la disciplina con cui tratta i casi indeterminati: dei tre non chiusi dichiara l'ipotesi e la sua improbabilità invece di promuoverla a fatto, e su uno chiude la questione per ricerca esaustiva sui 65536 semi possibili, trovando l'unico compatibile.

## A quale punto del progetto serve

- [[03-integrita-checksum]], il checksum additivo come difesa dalla corruzione e non da un avversario
- [[10-multiboot-hardware]], il multiboot come canale ufficiale delle distribuzioni
- [[06-identita-pokemon]], il valore di personalità visto dal lato di chi genera

## Relazioni con altre fonti

- conferma in modo indipendente [[pokeemerald]]
- documenta il funzionamento di [[gen3distributions]]

## Contesto

Livello 4 di affidabilità secondo la gerarchia di [[SOURCES]]. Track serviti: EVT, BRI. La mappa di tutte le fonti e delle loro relazioni è [[index-fonti]].
