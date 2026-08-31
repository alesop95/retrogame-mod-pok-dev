---
tipo: fonte
livello: 3
letto: si
track: [EVT, BRI, SME]
url: https://github.com/kwsch/PKHeX
tags: [fonte, livello-3]
corregge: "[[video-distribuzioni]]"
conferma: "[[video-distribuzioni]]"
---

# PKHeX, tabella degli eventi Gen 3 e vocabolario dei metodi

https://github.com/kwsch/PKHeX

## Abstract

Le due parti di PKHeX che documentano le distribuzioni di terza generazione: la tabella `PKHeX.Core/Legality/Encounters/Data/Gen3/EncountersWC3.cs`, con centosettantasette voci ciascuna corredata del proprio metodo di generazione pseudocasuale, e l'enumerazione `PKHeX.Core/Legality/RNG/PIDType.cs`, che documenta i metodi uno per uno. La tabella vive nel codice e non in un documento perché, come dichiara il suo stesso commento, i dati di quella generazione non sono mai stati conservati in forma binaria uniforme e sono quindi scritti a mano.

## Perché è in archivio

È la fonte che ha spostato il track dalla congettura al dato, ed è più affidabile dei video su ogni questione di offset e di metodo. La sigla BACD nomina l'ordine invertito con cui le quattro estrazioni compongono valore di personalità e valori individuali, e quell'inversione è la firma di un esemplare da evento: ne segue che ricreare un evento non è produrre i campi visibili giusti ma produrli attraverso la sequenza corretta. Conferma per via indipendente quattro affermazioni tratte dai video, nominandone i metodi, e ne chiude una che i video dichiaravano aperta, cioè la derivazione del sesso dell'allenatore di provenienza dei tre leggendari del film, che risulta uno scorrimento di quindici bit dopo l'oggetto tenuto e non la divisione congetturata. Porta infine il fatto più notevole della ricerca: nel blocco delle uova dichiara che il gioco riceve un'interruzione di sincronismo verticale fra la generazione della personalità e quella dei valori individuali, e che rimuovendola con una modifica alla ROM i medesimi script producono la correlazione ordinaria, quindi il metodo di generazione dipende da un'interruzione hardware e non soltanto dal codice.

## A quale punto del progetto serve

- [[06-identita-pokemon]], il valore di personalità visto dal lato di chi genera e di chi verifica
- [[12-analisi-quantitativa]], lo spazio dei semi a sedici bit e la sua esplorazione esaustiva
- [[23-prove-eseguite]], la prova di conformità su un esemplare autentico invece che sintetico

## Relazioni con altre fonti

- corregge un'affermazione di [[video-distribuzioni]]
- conferma in modo indipendente [[video-distribuzioni]]

## Contesto

Livello 3 di affidabilità secondo la gerarchia di [[SOURCES]]. Track serviti: EVT, BRI, SME. La mappa di tutte le fonti e delle loro relazioni è [[index-fonti]].
