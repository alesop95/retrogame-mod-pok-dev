---
tipo: nota di studio
livello: avanzato
tags: [cavo-link, protocollo, seriale]
up: "[[index]]"
vedi_anche: ["[[09-esecuzione-codice]]", "[[10-multiboot-hardware]]", "[[21-collaudo]]", "[[DATA-FORMATS_Gen1-Gen2-Gen3]]"]
---

# Il cavo Link, blocco per blocco

Il cavo Link è un'interfaccia seriale sincrona a un byte per volta, e la sua caratteristica fondamentale è che ogni trasferimento è uno scambio: il byte che esce e quello che entra attraversano lo stesso registro a scorrimento, quindi non esiste inviare senza ricevere. Un dispositivo fornisce il clock e si chiama master, l'altro lo segue e si chiama slave.

Questa simmetria forzata spiega la forma di tutto il protocollo. Non ci sono richieste e risposte: ci sono sequenze concordate in cui entrambi i lati sanno cosa mandare a ogni passo, e chi non ha nulla da dire manda un byte convenzionale di riempimento.

## L'hardware sotto il protocollo

Prima delle convenzioni del gioco conviene sapere cosa fa il silicio, e la fonte è Pan Docs alla pagina sul trasferimento seriale. Due registri governano tutto. Il primo, chiamato SB e mappato a 0xFF01, è il registro a scorrimento: prima di un trasferimento contiene il byte che uscirà, durante il trasferimento contiene un misto fra il byte in uscita e quello in entrata, perché a ogni colpo di clock il bit più a sinistra esce sul filo e un bit entra da destra. Il secondo, SC a 0xFF02, ha il bit 7 che abilita il trasferimento, il bit 1 che sceglie la velocità del clock solo su Game Boy Color, e il bit 0 che decide il ruolo, con 0 per clock esterno e 1 per clock interno. Il master carica il byte in SB e scrive 0x81 in SC; lo slave scrive 0x80.

Sulle frequenze c'è un fatto che vale più di tutti gli altri per questo progetto. Il clock interno del Game Boy monocromatico è fisso a 8192 Hz, cioè circa un kilobyte al secondo, mentre il Color offre quattro frequenze fino a 524288 Hz. Ma il clock esterno, cioè quello che fornirebbe un dispositivo nostro, non ha un limite fissato dal gioco: Pan Docs dichiara che anche il Game Boy monocromatico riconosce clock esterni fino a 500 kHz, che non c'è alcun limite inferiore, e che gli impulsi non devono nemmeno essere a intervalli regolari. La formulazione della fonte è che anche fornendo un bit al mese il Game Boy attenderebbe pazientemente il bit successivo.

Ne segue che il vincolo di tempo reale che si immagina guardando un protocollo sincrono, sul lato hardware, non esiste: chi fornisce il clock decide quando, e può fermarsi a pensare fra un bit e l'altro. È la ragione per cui un microcontrollore da pochi euro riesce a parlare con un Game Boy senza acrobazie, come mostra [[09-esecuzione-codice]]. Il vincolo che resta è software, cioè i tempi che il gioco si aspetta fra un blocco e il successivo, e l'autore di Poke Transporter GB lo conferma per esperienza scrivendo che tenere il clock né troppo veloce né troppo lento è cruciale e che quella è stata la parte più frustrante dello sviluppo.

Sull'elettricità, dalla parte 3 del dev log: il Game Boy lavora a 5 volt e il Game Boy Advance a 3.3, e i test di Goppier confermano che collegarli non danneggia nessuno dei due. È un'affermazione di terzi su hardware proprio, quindi da trattare come tale, ma è l'unica testimonianza diretta che il progetto ha su quel punto.

## Le costanti, che conviene leggere dalla fonte

Il disassemblato dichiara le costanti del protocollo in un unico file, e leggerle da là evita di ricavarle per osservazione. Il byte 0x01 e 0x02 sono i due esiti della negoziazione dei ruoli. Il byte 0xFD è il preambolo che delimita l'inizio di ogni blocco. Il byte 0xFE significa assenza di dati, ed è anche ciò che si legge su un cavo staccato, che è la ragione della sua esistenza. Il byte 0xFF termina una parte della lista di correzione. Il preambolo è lungo sei byte, quello della lista di numeri casuali sette, la lista di numeri casuali dieci, il riempimento finale tre.

## La sequenza di uno scambio

Prima viene la negoziazione dei ruoli: il candidato slave risponde 0x02 se rileva un trasferimento in corso, altrimenti passa a master e invia 0x01. Poi uno scambio di byte nulli e un byte di sincronizzazione 0x60. Poi la selezione della modalità, dove il master trasmette valori della forma 0xDx con i due bit bassi a indicare la voce evidenziata nel menu e un bit a confermare, con 0xD4 per il Centro Scambi.

Nello scambio vero e proprio ciascuna console invia tre blocchi consecutivi, ciascuno precedito dal suo preambolo di byte 0xFD. Il primo blocco è una lista di dieci numeri casuali, che serve a mettere d'accordo i due giochi su una sorgente comune di casualità. Il secondo è la struttura di scambio, che contiene i dati della squadra. Il terzo è la lista di correzione.

Alla scelta del Pokemon ciascuna console invia 0x60 sommato all'indice di squadra, e poi 0x62 per accettare o 0x61 per rifiutare.

## La dimensione, e come si smette di litigare sulle cifre

Sulla dimensione della struttura di scambio le fonti secondarie danno cifre in conflitto, tipicamente 415 e 424. Il modo di chiudere la questione non è scegliere la fonte più autorevole ma leggere il codice che trasmette, dove il conteggio è scritto come somma di costanti.

```
ld bc, SERIAL_PREAMBLE_LENGTH + NAME_LENGTH + 1 + PARTY_LENGTH + 1
        + (PARTYMON_STRUCT_LENGTH + NAME_LENGTH * 2) * PARTY_LENGTH + 3
```

Sostituendo le costanti, cioè preambolo 6, nomi 11, squadra 6, struttura di squadra 44 e riempimento 3, si ottengono 424 byte sul filo e 418 di dati utili senza preambolo. Entrambe le cifre delle fonti secondarie misuravano qualcosa di reale, semplicemente non la stessa cosa, e la lezione generale è che una dimensione va sempre accompagnata dall'indicazione di dove si taglia.

## La lista di correzione, che è più interessante di come sembra

Il protocollo si riserva due valori, 0xFD per il preambolo e 0xFE per l'assenza di dati, e quindi non può trasmetterli come dati. Ma i dati della squadra contengono byte arbitrari, e prima o poi uno di quelli sarà 0xFE.

La soluzione del gioco è sostituire ogni 0xFE con 0xFF e trasmettere separatamente l'elenco delle posizioni in cui la sostituzione è avvenuta, così che il ricevente possa rimetterle a posto. Quell'elenco è la lista di correzione, ed è uno scambio di esattamente duecento byte.

Il dettaglio che rivela la ricorsività del problema è il motivo per cui la lista è divisa in due parti. Anche gli indici sono byte trasmessi, e un indice uguale a 0xFD verrebbe letto come preambolo: quando il contatore delle posizioni raggiunge quel valore, il gioco chiude la prima parte con 0xFF e riparte a contare per la seconda. Non è una divisione arbitraria, è l'unica soluzione possibile dato che il protocollo si riserva due valori e li deve poter indicizzare.

## Il lato generazione 2, e una scoperta che vale per tutto il progetto

Il disassemblato di pokecrystal dichiara due strutture di invio distinte, e la seconda è un regalo per questo progetto.

La prima, quella nativa, aggiunge un identificatore del giocatore a 16 bit e usa la struttura di squadra da 48 byte, per un totale di 450 byte sul filo. La seconda si chiama struttura del Time Capsule, non ha l'identificatore, e usa una macro chiamata `red_party_struct`, cioè la struttura di generazione 1 da 44 byte: misura 424 byte, esattamente il blocco di generazione 1.

Questo significa che la conversione fra il formato di generazione 1 e quello di generazione 2 esiste già dentro il gioco di generazione 2, scritta dagli autori originali per il Time Capsule, ed è leggibile nel disassemblato. Per chi costruisce un ponte verso la generazione 3 è il precedente più utile che ci sia: mostra quali campi gli autori hanno lasciato cadere, quali hanno inventato e come hanno gestito il byte che in generazione 1 è il tasso di cattura e in generazione 2 l'oggetto tenuto. Non è un'analogia, è lo stesso problema risolto da chi aveva scritto entrambi i formati.

Il lato generazione 2 trasmette inoltre un blocco separato per la posta, con un preambolo proprio e una propria lista di correzione, e questa è la ragione strutturale per cui i progetti esistenti dichiarano di non poter trasferire un Pokemon che tiene una lettera.

## Una conferma indipendente, che vale più di una rilettura

Tutte le costanti di questa nota sono state ricavate dal disassemblato. Esiste una seconda fonte che le conferma senza averle prese da noi, ed è un firmware che funziona: `cable-link` dell'organizzazione CableClub, sotto licenza Apache 2.0, un circuito stampato con il suo firmware per Raspberry Pi Pico. Il suo file `src/pokemon_gen1_link_protocol.h` dichiara le costanti del protocollo, e coincidono con le nostre una per una.

```c
#define PKMN_MASTER 0x01
#define PKMN_SLAVE 0x02
#define PKMN_CONNECTED 0x60
#define PKMN_WAIT 0x7F
#define PKMN_NO_DATA 0xFE
#define ITEM_1_SELECTED 0xD4          /* Centro Scambi */
#define ITEM_2_SELECTED 0xD5          /* Colosseo */
#define ITEM_3_SELECTED 0xD6          /* interrompi */
#define TRADE_CENTRE_WAIT 0xFD        /* il byte di preambolo */
```

La sua macchina a stati conferma anche la sequenza: gli stati vanno da `INIT` a dieci stati `SEND_RAND` numerati da zero a nove, poi `WAIT`, poi `SEND_DATA`, poi `SEND_PATCH`. Sono esattamente i dieci byte di numeri casuali, la struttura di scambio e la lista di correzione descritti sopra, ricavati da noi contando i campi nel disassemblato.

Un dettaglio chiude il cerchio con la sezione sull'hardware: quel firmware apre la porta seriale con `spi_init(spi_default, 500 * 1000)`, cioè esattamente il mezzo megahertz che Pan Docs dichiara come massimo riconosciuto dal Game Boy monocromatico. Due fonti indipendenti, una documentazione dell'hardware e un firmware che funziona sul campo, concordano sul numero.

## Il vincolo di sincronizzazione, che è il vero problema del ponte

C'è un aspetto del protocollo che non riguarda i byte ma il tempo, ed è quello che decide se un ponte funziona bene o funziona a metà. Viene dalla trascrizione dell'aggiornamento di sviluppo di Goppier, letta il 2026-08-25, ed è l'unica fonte che lo descriva.

Dal lato generazione 3 la squadra non viaggia in un blocco unico: viaggia a blocchi di duecento byte, due Pokemon per volta, tre volte. L'affermazione veniva da un video, quindi è stata verificata sul sorgente il 2026-08-26, ed era esatta: in `pokefirered/src/trade.c` la macchina a stati che prepara la squadra chiama `SendBlockRequest(BLOCK_REQ_SIZE_200)` in tre punti distinti, e a ogni giro copia `2 * sizeof(struct Pokemon)` nella squadra avversaria alle posizioni zero, due e quattro, alternando l'invio dei propri due. La cifra torna con la struttura che conosciamo, perché due record da cento byte fanno esattamente duecento byte, ed è anche la stessa dimensione della lista di correzione di generazione 1, che è una coincidenza e non una relazione. Dopo i tre blocchi ne parte un quarto con la posta, dimensionato come sei strutture di posta più quattro byte, con un commento nel sorgente che ammette di non sapere perché ci siano quei quattro byte in più.

Il punto che conta per il ponte non è la dimensione ma la reciprocità: la copia dei propri Pokemon successivi avviene fra due ricezioni, quindi il gioco non consegna i due successivi finché non ha ricevuto i propri.

Dal lato generazione 2 la struttura del trasferimento è diversa, e la differenza è quella che il capitolo sui formati ha già mostrato, cioè che la struttura principale non contiene il soprannome né il nome dell'allenatore originale. Ne segue che il gioco invia in tre sezioni successive: prima i dati principali di tutti e sei, poi i nomi degli allenatori originali di tutti e sei, poi i soprannomi.

Sovrapposte, le due cose producono uno stallo che non è un difetto di implementazione ma una proprietà dei due protocolli. Chi sta in mezzo può ricevere due Pokemon da generazione 3 e trattenere i propri, e può anche trattenere generazione 2, ma non può costruire un solo Pokemon completo di generazione 3 finché non ha ricevuto almeno due soprannomi, che arrivano nell'ultima delle tre sezioni; e quando generazione 2 ha finito di inviare, smette anche di ricevere, quindi la finestra per rispondergli si è chiusa. Il ponte non ha abbastanza informazione al momento in cui gli viene chiesta.

La soluzione adottata da Goppier è istruttiva proprio perché è imperfetta e lui la dichiara tale: il dispositivo invia dati di riempimento che costringono il giocatore ad annullare lo scambio e a ripeterlo, e al secondo passaggio conosce entrambe le squadre e converte correttamente. È una trasformazione del problema in un protocollo a due passaggi, dove il primo serve solo a osservare. Le alternative che restano aperte sono tre, e vanno tenute presenti prima di scrivere codice: bufferizzare in modo asimmetrico se una delle due direzioni tollera l'attesa, prevedere il contenuto quando è derivabile da ciò che si è già visto, oppure cambiare il lato del problema eseguendo codice proprio sul Game Boy, che è la strada di Poke Transporter GB e che elimina la reciprocità perché non c'è più un partner da soddisfare.

## Perché questa nota è collaudabile senza hardware

Il fatto più utile in pratica: BGB espone il cavo Link su una connessione TCP con un protocollo documentato a pacchetti di otto byte, e `PokemonGB_Online_Trades` implementa gli scambi proprio su quell'interfaccia. Tutto quanto descritto in questa nota si può quindi implementare e verificare in emulazione, senza toccare una console, a una condizione che vale dichiarare: verificarlo contro un gioco vero richiede la ROM di quel gioco, e dentro il perimetro del progetto quella ROM viene dal dump di una cartuccia propria, quindi dal lettore. Il dettaglio di come si organizza quel collaudo, e cosa resta possibile prima che il lettore arrivi, sta in [[21-collaudo]].

## Cosa leggere dopo

[[09-esecuzione-codice]] mostra come lo stesso canale diventi un canale di esecuzione, e [[10-multiboot-hardware]] copre il lato Game Boy Advance.
