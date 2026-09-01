---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - gba-switch-pokemon-trading/
last-verified-commit: 7696c46
stato: in ricerca, nessun ambiente allestito
---

# Sottoprogetto: trading wireless locale fra PC e Nintendo Switch

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`. La sezione 14 dell'handoff propone un prompt di ripartenza scritto per una chat: resta come storico, la precedenza è qui.

Obiettivo: far comunicare un PC Linux con una Nintendo Switch tramite LDN, il protocollo wireless locale proprietario di Nintendo, per eseguire uno scambio di Pokemon con una copia di FireRed o LeafGreen in esecuzione sulla console. Il PC simula la seconda console. È un proof of concept dimostrativo, non un tool finito.

## Dove siamo

Fase di ricerca conclusa, nessun ambiente allestito e nessun repository clonato. Sono identificati i due progetti su cui il lavoro si appoggerebbe: `kinnay/LDN`, la libreria Python del protocollo, e `tornadus/frlg-ldn-trade`, il proof of concept che la usa per il trade. Il funzionamento lato gioco dipende dalla decompilazione comunitaria `pret/pokefirered`, quindi un aggiornamento del gioco sulla console potrebbe romperne la compatibilità.

Questo track ribalta il presupposto con cui era stato aperto: non è una via verso Pokemon Home né una sovrapposizione con il track 3DS, come si era ipotizzato quando la cartella era vuota. È un lavoro di rete e di reverse engineering, ed è il secondo destinato a produrre software vero, accanto al ponte fra generazioni.

## Prossimo passo concreto

Clonare i due repository e leggere il codice di `frlgtrade.py` e del pacchetto `ldn`, che nessuno ha ancora aperto: l'handoff è costruito su README e metadati, non sul sorgente. Da lì si colmano le lacune della sezione 13.

## Vincolo che condiziona tutto

Serve una scheda Wi-Fi che supporti la modalità monitor, e la scelta è il fattore critico dichiarato: le schede USB esterne di fascia adatta risultano affidabili nei test degli autori, mentre alcune schede interne moderne sono fino alla metà più lente e soggette a deadlock. Prima di allestire qualsiasi cosa va accertato quale scheda è disponibile su questa macchina, perché da quella risposta dipende se il track è praticabile o no.

## Materiale ora letto

Le due fonti portanti del track sono state lette per la prima volta. La libreria di kinnay richiede Linux con Python 3.12 o successivo, il privilegio `CAP_NET_ADMIN`, l'arresto di NetworkManager e hardware wireless capace di ricevere e trasmettere action frame in modalità monitor. La specifica del protocollo non sta nel suo README ma nel wiki di NintendoClients, che documenta l'action frame vendor-specific trasmesso ogni 100 millisecondi con OUI 00:22:AA, i canali 1, 6 e 11 in banda 2.4 GHz, la struttura dell'advertisement campo per campo, i tre livelli di cifratura e la derivazione delle chiavi dalle chiavi di console, la sequenza di connessione con i suoi timeout e l'assegnazione degli indirizzi nella forma 169.254.X.Y.

Il proof of concept di tornadus richiede Python 3.12 o successivo, la libreria di kinnay, le chiavi della console e una scheda Wi-Fi compatibile, e opera facendosi passare per un giocatore che si collega come leader mentre la console avvia lo scambio dal Direct Corner. La logica sta in `frlgtrade.py` con la cartella `frlgsim/`, e i Pokemon si scambiano nei formati `.pk3` in chiaro e `.ek3` cifrato.

Sulla domanda che blocca il track la risposta è arrivata, ed è in due parti. La prima: questa macchina è un computer fisso senza alcuna interfaccia Wi-Fi, quindi la scheda non c'è e non va accertata, va procurata. La seconda: oltre alla lista del progetto, che dichiara affidabili ALFA AWUS036ACHM e Realtek RTL8821CE e poco affidabile AMD RZ616, esiste una testimonianza di campo nel canale di supporto del server Pokemon Multiplayer Research, dove un utente dichiara che il TP-Link AC600 funziona bene e che al contrario una Intel Pro Wireless 5100 AGN integrata non funziona.

La lettura integrale di quel canale, fatta il 2026-08-26, ha corretto la premessa su cui poggiava la riserva registrata qui prima, ed è la correzione più utile di questa scheda. Si era scritto che l'Archer T2U Nano monta un RTL8811AU il cui supporto alla modalità monitor passa da un driver fuori albero. La testimonianza positiva riguarda invece l'Archer T2U Plus, e chi l'ha fatto funzionare su Linux Mint dichiara di non avere installato alcun driver custom e riporta il proprio dispositivo come `driver: rtw_8821cu`, cioè un chip RTL8821CU servito dal driver in albero `rtw88`. Il nome commerciale AC600 copre quindi chip diversi, e ciò che decide non è il nome ma la coppia di identificatori USB e il modulo del kernel che li reclama. La ricerca nel canale con il filtro `8811` non restituisce alcun risultato: sul chip che si credeva montato non esiste alcuna testimonianza, né positiva né negativa.

Il primo passo materiale su questo track è quindi diventato più semplice ed economico di quanto sembrasse. Non serve comprare nulla per sapere se l'adattatore in mano sia adatto: basta collegarlo e leggere il suo identificatore USB, e da quello ricavare il chip e il driver. Se è un chip della famiglia servita da `rtw88` la strada è aperta; se è un RTL8811AU si resta nell'incertezza documentata e conviene procurare uno dei modelli dichiarati affidabili.

## La via Windows, che cancella la tensione di piattaforma

Il fatto più importante emerso il 2026-08-26 è che questo track non richiede necessariamente Linux, e quindi la tensione con il track dello Smeraldo, che richiede Windows per PKHeX, non è più una decisione da prendere. Esiste una seconda implementazione, il demone `ldnd`, che gira su Windows senza macchina virtuale: collega il kernel Linux come libreria statica dentro un eseguibile costruito con MinGW, riceve l'adattatore USB attraverso WinUSB e gli fa caricare i driver e il firmware di Linux. Il meccanismo, il suo prezzo e i suoi guasti tipici sono descritti in `docs/11-wireless-locale-e-ponte-switch.md`.

Ne discendono tre conseguenze operative. La prima è che le due implementazioni non hanno la stessa compatibilità hardware, verificato sul campo da un utente il cui adattatore funziona con quella Windows e non con quella Linux, e la ragione è che quella Windows scavalca gestore di rete e driver di sistema. La seconda è che la via Windows funziona soltanto con adattatori USB, mentre su Linux va bene anche una scheda interna se il suo driver collabora. La terza è che, dopo avere riassegnato il dispositivo a WinUSB con Zadig, quello non funziona più come scheda di rete ordinaria, quindi serve un altro accesso a internet su quella macchina.

## Il ponte verso il Game Boy Advance, e il legame con l'altro track

Questo track e quello del ponte fra generazioni non sono paralleli come si credeva: si toccano, e il punto di contatto è dichiarato dall'autore del progetto. Il Wireless Adapter del Game Boy Advance non è un dispositivo 802.11 ma un progetto interamente proprietario, quindi nessuna scheda Wi-Fi potrà mai parlare con un Game Boy Advance, e la via che l'autore indica per quel tratto è un microcontrollore che si finge quel dispositivo. È parola per parola l'opzione D di ADR-008, e nel canale compare la fotografia di una catena funzionante descritta come Game Boy Advance, adattatore wireless finto costruito su misura, progetto LDN e Nintendo Switch.

Nello stesso canale si chiude anche il punto che questa scheda teneva aperto sul rapporto con il GBxCart RW: l'autore dichiara di distribuire strumenti e non dati, e indica il GBxCart RW o il GB Operator come il modo di ottenere i propri salvataggi da cartuccia fisica per produrre le strutture `.pk3` di partenza. È quindi lo stesso apparecchio del track Smeraldo, e la fase in cui entra è la preparazione dei dati; chi lavora su copie proprie in emulazione non ha bisogno di hardware.

Un ultimo elemento, che vale come rischio e non come opportunità: l'emulatore sulla console riproduce il Wireless Adapter in emulazione di alto livello, dove risulta sempre collegato, e non riproduce il cavo Link. Verso un gioco di generazione 3 su Switch non esiste quindi alcuna via che passi dal cavo.

## Un vincolo di gioco che nessuna documentazione dichiarava

Il giocatore simulato dal computer, nella configurazione predefinita, non ha il Pokedex nazionale, e finché non lo ha il gioco rifiuta lo scambio di molte specie. Chi lo ha scoperto ha modificato il codice del giocatore simulato imponendo il valore `0x0F` alle sue flag di progressione. Per un ponte che porta esemplari dalle generazioni 1 e 2 questo è centrale, perché sono precisamente le specie fuori dalla prima regione a essere rifiutate, e un fallimento per questa ragione somiglierebbe a un errore di formato senza esserlo. Va registrato anche che, per testimonianza di un utente, gli oggetti tenuti non passano nello scambio.

## Da verificare prima di pianificare

La domanda sulla disponibilità di Rosso Fuoco e Verde Foglia su Switch è risolta: il repository del proof of concept dichiara il supporto a Switch e Switch 2, la procedura richiede di aver sbloccato la sala degli scambi con venti o quaranta minuti di gioco, e la decompilazione `pret/pokefirered` comprende il port per Switch. Il presupposto del track esiste quindi già. Resta aperto, come dato di terzi non verificato sul sorgente, che anche Rubino e Zaffiro riceveranno il supporto al Wireless Adapter, cosa che un partecipante dichiara di avere dedotto ispezionando il binario dell'emulatore.

## Decisioni aperte

Serve Linux, e l'handoff propone una chiavetta avviabile con Linux Mint. Questo mette il track in tensione con quello dello Smeraldo, che richiede Windows 11 per PKHeX: va deciso se convivono sulla stessa macchina in dual boot o live USB, o se si separano. La decisione non è ancora presa e non è urgente finché il track resta in ricerca.

Restano da chiarire le discrepanze registrate nella sezione 13 dell'handoff: quale versione di Python sia realmente richiesta, quale scheda Wi-Fi sia quella usata nella dimostrazione, e soprattutto in che forma giri FireRed sulla console, dato che il materiale non chiarisce se sia emulazione, port ufficiale o altro. Quest'ultimo punto condiziona la spiegazione del meccanismo di scambio.

Il rapporto con il GBxCart RW non è spiegato dal materiale: l'apparecchio compare fra i requisiti ma non è detto in quale fase entri. È lo stesso lettore del track Smeraldo, quindi una sovrapposizione hardware esiste, ma non è documentata.

## Perimetro

Le `prod.keys` della console sono materiale di chiave proprietario, si estraggono solo da una console modificata e non sono redistribuibili. Sono escluse dal version control dal blocco dedicato del `.gitignore`, insieme ai file di dati `.pk3`, e valgono le stesse cautele del materiale di chiave del 3DS descritte in `design-and-security.md`.

## Evidenze e materiale locale

L'handoff `HANDOFF_frlg-ldn-trade.md` sta nella cartella del sottoprogetto ed è l'unico materiale esistente. Non ci sono media. Il codice dei due repository di riferimento non è ancora presente in locale.

## Aggiunta del 2026-09-01: il track è riconosciuto dall'esterno, e siamo più aggiornati della fonte

Nel server della comunità dell'esecuzione di codice, l'autore degli strumenti indica il proof of concept su cui questo track si appoggia come la via alternativa alla propria per portare un esemplare di terza generazione dentro la riedizione per console moderna, osservando che per questa via non serve alcun codice e che il suo costruttore può produrre il file di struttura da trasferire. È una conferma esterna che il track affronta un problema reale e non una curiosità.

Sulla medesima descrizione il progetto è però più aggiornato della fonte, e vale registrarlo perché è il tipo di scarto che si perde: la fonte elenca fra i requisiti Linux, mentre ADR-015 ha stabilito che quel requisito è decaduto, perché esiste un demone che porta lo stack senza fili di Linux su Windows. Una fonte di quinto livello resta ferma al momento in cui è stata scritta, e su un dominio che si muove questo è il modo normale in cui invecchia.
