---
tipo: fonte
livello: 3
letto: si
track: [PKD, EVT, SME]
url: https://github.com/kwsch/PKHeX
tags: [fonte, livello-3]
---

# PKHeX.Core, la libreria del verificatore usata come giudice e come generatore

https://github.com/kwsch/PKHeX

## Abstract

La libreria che il progetto compila dal clone e chiama dagli strumenti in C# dal 2026-09-25 (ADR-081): l'analisi di legalità con un salvataggio vuoto attivo e le classi d'incontro da cui si genera. Letta nel clone locale al commit e15d246 per i punti della generazione e al commit bfe89c7, release 26.10.18, per quelli del trasferimento. Per la generazione: il calcolo del valore di personalità del contapassi da entrambi gli identificativi, in PKHeX.Core/Legality/RNG/ClassicEra/Gen4/PokewalkerRNG.cs riga 280; il vincolo fra il bit più alto del valore di personalità e la parità della somma esclusiva degli identificativi in quinta generazione, in PKHeX.Core/Legality/RNG/ClassicEra/MonochromeRNG.cs righe 14-25; l'identificativo segreto all'offset 6 e la somma di controllo calcolata sui soli dati da 0x20 in terza generazione, in PKHeX.Core/PKM/PK3.cs righe 56 e 204. Per la scrittura delle copie: il sentimento del ricordo del detentore scelto a caso nella conversione verso la sesta generazione, in PKHeX.Core/PKM/PK5.cs riga 479, con il generatore condiviso di PKHeX.Core/Util/RandUtil.cs riga 8; la data d'incontro posta al giorno della conversione verso la quarta generazione, in PK3.cs riga 255; i due campi agli offset 0xA6 e 0xD6 del formato della sesta generazione, in PKHeX.Core/PKM/PK6.cs righe 333 e 360; l'aggiornamento del registro delle specie a ogni scrittura in un contenitore, in PKHeX.Core/Saves/SaveFile.cs riga 263. Per il trasferimento, letti il 2026-11-11: il rifiuto ha un codice solo, TransferBad, emesso in sei punti, cioè PKHeX.Core/Legality/Verifiers/FormVerifier.cs riga 47 (Pikachu Cosplay fuori dal formato 6), Misc/MiscVerifierPK7.cs righe 20-21 (stato d'evento del resort fuori dai valori da 0 a 19 dell'enumerazione ResortEventState, PKHeX.Core/PKM/PK7.cs righe 584-607), TransferVerifier.cs righe 154 (totem, con IsTotemNoTransfer in Legality/Encounters/Templates/Gen7/EncounterStatic7.cs riga 40), 170 (dimensioni nulle) e 186 (specie assente dal gioco di destinazione), Misc/MiscVerifierPK9.cs riga 75; gli esemplari e gli oggetti che non si scambiano in Legality/Tables/TradeRestrictions.cs righe 15 e 24; la chiamata del verificatore della settima generazione per ogni esemplare in formato 7 in Legality/Verifiers/MiscVerifier.cs riga 49, e la validità come assenza di righe non valide in Legality/LegalityAnalysis.cs riga 157.

## Perché è in archivio

È il giudice di tutte le copie per HOME e il generatore dei lotti: ogni affermazione del progetto su che cosa sia conforme rimanda a questo codice e non a una pagina che lo descrive. Le righe sul trasferimento servono a una distinzione che il capitolo 28 della tesi racconta: un vincolo che vale nel formato di partenza il giudizio lo vede, uno che vale soltanto nel formato di arrivo no, ed è così che i Pikachu Cosplay del giro 6 e i quattro totem del giro 8 sono risultati conformi e non sono passati.

## A quale punto del progetto serve

- [[07-conversione-vincoli]], i vincoli che la conversione fra formati impone
- pokedex-home-completo/COPIE-PER-HOME.md, il controllo delle copie dei giri 9, 10 e 11 sulle regole di rifiuto

## Contesto

Livello 3 di affidabilità secondo la gerarchia di [[SOURCES]]. Track serviti: PKD, EVT, SME. La mappa di tutte le fonti e delle loro relazioni è [[index-fonti]].
