---
tipo: fonte
livello: 4
letto: si
track: [BRI]
url: https://discord.com/invite/EA7jxJ6
tags: [fonte, livello-4]
conferma: "[[pokeemerald]]"
documenta: "[[glitchcity]]"
---

# Glitch City Research Institute, canali

https://discord.com/invite/EA7jxJ6

## Abstract

Server della community che studia i difetti sfruttabili dei giochi Pokemon. I canali per generazione contengono il lavoro corrente, che il wiki recepisce con ritardo o non recepisce affatto.

## Perché è in archivio

Ha portato al progetto tutto cio che sa sull esecuzione di codice in generazione 3, che prima non copriva: il ruolo dei byte 0xFC e 0xFD come codice di controllo e sostituzione di variabile nel motore di stampa del testo, la differenza fra Rubino e Zaffiro, dove quei codici passano da una tabella di puntatori senza controllo dei limiti, e le altre tre versioni, dove passano da un costrutto di scelta multipla che rende inerte un indice fuori intervallo, e la catena completa che parte da una posta difettosa. Dal lato generazione 2 ha portato il vincolo per cui un identificativo dell allenatore contenente il byte 0xFF impedisce il traboccamento della squadra, perché introduce un terminatore dove non era previsto.

## A quale punto del progetto serve

- [[09-esecuzione-codice]], il lato generazione 3, e il vincolo sul traboccamento
- [[05-testo-e-charmap]], i byte di controllo non sono caratteri

## Relazioni con altre fonti

- conferma in modo indipendente [[pokeemerald]]
- documenta il funzionamento di [[glitchcity]]

## Contesto

Livello 4 di affidabilità secondo la gerarchia di [[SOURCES]]. Track serviti: BRI. La mappa di tutte le fonti e delle loro relazioni è [[index-fonti]].
