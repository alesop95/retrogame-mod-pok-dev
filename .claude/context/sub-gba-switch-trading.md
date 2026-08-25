---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - gba-switch-pokemon-trading/
last-verified-commit: d08a011
stato: in ricerca, nessun ambiente allestito
---

# Sottoprogetto: trading wireless locale fra PC e Nintendo Switch

Lo stato canonico di questo track e' questo file, insieme alla riga che lo riguarda in `memory/index.md`. La sezione 14 dell'handoff propone un prompt di ripartenza scritto per una chat: resta come storico, la precedenza e' qui.

Obiettivo: far comunicare un PC Linux con una Nintendo Switch tramite LDN, il protocollo wireless locale proprietario di Nintendo, per eseguire uno scambio di Pokemon con una copia di FireRed o LeafGreen in esecuzione sulla console. Il PC simula la seconda console. E' un proof of concept dimostrativo, non un tool finito.

## Dove siamo

Fase di ricerca conclusa, nessun ambiente allestito e nessun repository clonato. Sono identificati i due progetti su cui il lavoro si appoggerebbe: `kinnay/LDN`, la libreria Python del protocollo, e `tornadus/frlg-ldn-trade`, il proof of concept che la usa per il trade. Il funzionamento lato gioco dipende dalla decompilazione comunitaria `pret/pokefirered`, quindi un aggiornamento del gioco sulla console potrebbe romperne la compatibilita'.

Questo track ribalta il presupposto con cui era stato aperto: non e' una via verso Pokemon Home ne' una sovrapposizione con il track 3DS, come si era ipotizzato quando la cartella era vuota. E' un lavoro di rete e di reverse engineering, ed e' il secondo destinato a produrre software vero, accanto al ponte fra generazioni.

## Prossimo passo concreto

Clonare i due repository e leggere il codice di `frlgtrade.py` e del pacchetto `ldn`, che nessuno ha ancora aperto: l'handoff e' costruito su README e metadati, non sul sorgente. Da li' si colmano le lacune della sezione 13.

## Vincolo che condiziona tutto

Serve una scheda Wi-Fi che supporti la modalita' monitor, e la scelta e' il fattore critico dichiarato: le schede USB esterne di fascia adatta risultano affidabili nei test degli autori, mentre alcune schede interne moderne sono fino alla meta' piu' lente e soggette a deadlock. Prima di allestire qualsiasi cosa va accertato quale scheda e' disponibile su questa macchina, perche' da quella risposta dipende se il track e' praticabile o no.

## Da verificare prima di pianificare

La data di disponibilita' di Rosso Fuoco e Verde Foglia su Switch e' incerta: la sezione 7 dell'handoff 3DS dice ottobre 2026, mentre fonti secondarie trovate il 2026-08-25 indicano il 27 febbraio 2026, con scambio locale che emula l'adattatore wireless del Game Boy Advance. Se la seconda e' corretta il presupposto del track esiste gia'. Va verificato su fonte primaria.

## Decisioni aperte

Serve Linux, e l'handoff propone una chiavetta avviabile con Linux Mint. Questo mette il track in tensione con quello dello Smeraldo, che richiede Windows 11 per PKHeX: va deciso se convivono sulla stessa macchina in dual boot o live USB, o se si separano. La decisione non e' ancora presa e non e' urgente finche' il track resta in ricerca.

Restano da chiarire le discrepanze registrate nella sezione 13 dell'handoff: quale versione di Python sia realmente richiesta, quale scheda Wi-Fi sia quella usata nella dimostrazione, e soprattutto in che forma giri FireRed sulla console, dato che il materiale non chiarisce se sia emulazione, port ufficiale o altro. Quest'ultimo punto condiziona la spiegazione del meccanismo di scambio.

Il rapporto con il GBxCart RW non e' spiegato dal materiale: l'apparecchio compare fra i requisiti ma non e' detto in quale fase entri. E' lo stesso lettore del track Smeraldo, quindi una sovrapposizione hardware esiste, ma non e' documentata.

## Perimetro

Le `prod.keys` della console sono materiale di chiave proprietario, si estraggono solo da una console modificata e non sono redistribuibili. Sono escluse dal version control dal blocco dedicato del `.gitignore`, insieme ai file di dati `.pk3`, e valgono le stesse cautele del materiale di chiave del 3DS descritte in `design-and-security.md`.

## Evidenze e materiale locale

L'handoff `HANDOFF_frlg-ldn-trade.md` sta nella cartella del sottoprogetto ed e' l'unico materiale esistente. Non ci sono media. Il codice dei due repository di riferimento non e' ancora presente in locale.
