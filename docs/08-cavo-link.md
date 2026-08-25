---
tipo: nota di studio
livello: avanzato
tags: [cavo-link, protocollo, seriale]
up: "[[index]]"
vedi_anche: ["[[09-esecuzione-codice]]", "[[10-multiboot-hardware]]", "[[21-collaudo]]", "[[DATA-FORMATS_Gen1-Gen2-Gen3]]"]
---

# Il cavo Link, blocco per blocco

Il cavo Link e' un'interfaccia seriale sincrona a un byte per volta, e la sua caratteristica fondamentale e' che ogni trasferimento e' uno scambio: il byte che esce e quello che entra attraversano lo stesso registro a scorrimento, quindi non esiste inviare senza ricevere. Un dispositivo fornisce il clock e si chiama master, l'altro lo segue e si chiama slave.

Questa simmetria forzata spiega la forma di tutto il protocollo. Non ci sono richieste e risposte: ci sono sequenze concordate in cui entrambi i lati sanno cosa mandare a ogni passo, e chi non ha nulla da dire manda un byte convenzionale di riempimento.

## Le costanti, che conviene leggere dalla fonte

Il disassemblato dichiara le costanti del protocollo in un unico file, e leggerle da la' evita di ricavarle per osservazione. Il byte 0x01 e 0x02 sono i due esiti della negoziazione dei ruoli. Il byte 0xFD e' il preambolo che delimita l'inizio di ogni blocco. Il byte 0xFE significa assenza di dati, ed e' anche cio' che si legge su un cavo staccato, che e' la ragione della sua esistenza. Il byte 0xFF termina una parte della lista di correzione. Il preambolo e' lungo sei byte, quello della lista di numeri casuali sette, la lista di numeri casuali dieci, il riempimento finale tre.

## La sequenza di uno scambio

Prima viene la negoziazione dei ruoli: il candidato slave risponde 0x02 se rileva un trasferimento in corso, altrimenti passa a master e invia 0x01. Poi uno scambio di byte nulli e un byte di sincronizzazione 0x60. Poi la selezione della modalita', dove il master trasmette valori della forma 0xDx con i due bit bassi a indicare la voce evidenziata nel menu e un bit a confermare, con 0xD4 per il Centro Scambi.

Nello scambio vero e proprio ciascuna console invia tre blocchi consecutivi, ciascuno precedito dal suo preambolo di byte 0xFD. Il primo blocco e' una lista di dieci numeri casuali, che serve a mettere d'accordo i due giochi su una sorgente comune di casualita'. Il secondo e' la struttura di scambio, che contiene i dati della squadra. Il terzo e' la lista di correzione.

Alla scelta del Pokemon ciascuna console invia 0x60 sommato all'indice di squadra, e poi 0x62 per accettare o 0x61 per rifiutare.

## La dimensione, e come si smette di litigare sulle cifre

Sulla dimensione della struttura di scambio le fonti secondarie danno cifre in conflitto, tipicamente 415 e 424. Il modo di chiudere la questione non e' scegliere la fonte piu' autorevole ma leggere il codice che trasmette, dove il conteggio e' scritto come somma di costanti.

```
ld bc, SERIAL_PREAMBLE_LENGTH + NAME_LENGTH + 1 + PARTY_LENGTH + 1
        + (PARTYMON_STRUCT_LENGTH + NAME_LENGTH * 2) * PARTY_LENGTH + 3
```

Sostituendo le costanti, cioe' preambolo 6, nomi 11, squadra 6, struttura di squadra 44 e riempimento 3, si ottengono 424 byte sul filo e 418 di dati utili senza preambolo. Entrambe le cifre delle fonti secondarie misuravano qualcosa di reale, semplicemente non la stessa cosa, e la lezione generale e' che una dimensione va sempre accompagnata dall'indicazione di dove si taglia.

## La lista di correzione, che e' piu' interessante di come sembra

Il protocollo si riserva due valori, 0xFD per il preambolo e 0xFE per l'assenza di dati, e quindi non puo' trasmetterli come dati. Ma i dati della squadra contengono byte arbitrari, e prima o poi uno di quelli sara' 0xFE.

La soluzione del gioco e' sostituire ogni 0xFE con 0xFF e trasmettere separatamente l'elenco delle posizioni in cui la sostituzione e' avvenuta, cosi' che il ricevente possa rimetterle a posto. Quell'elenco e' la lista di correzione, ed e' uno scambio di esattamente duecento byte.

Il dettaglio che rivela la ricorsivita' del problema e' il motivo per cui la lista e' divisa in due parti. Anche gli indici sono byte trasmessi, e un indice uguale a 0xFD verrebbe letto come preambolo: quando il contatore delle posizioni raggiunge quel valore, il gioco chiude la prima parte con 0xFF e riparte a contare per la seconda. Non e' una divisione arbitraria, e' l'unica soluzione possibile dato che il protocollo si riserva due valori e li deve poter indicizzare.

## Il lato generazione 2, e una scoperta che vale per tutto il progetto

Il disassemblato di pokecrystal dichiara due strutture di invio distinte, e la seconda e' un regalo per questo progetto.

La prima, quella nativa, aggiunge un identificatore del giocatore a 16 bit e usa la struttura di squadra da 48 byte, per un totale di 450 byte sul filo. La seconda si chiama struttura del Time Capsule, non ha l'identificatore, e usa una macro chiamata `red_party_struct`, cioe' la struttura di generazione 1 da 44 byte: misura 424 byte, esattamente il blocco di generazione 1.

Questo significa che la conversione fra il formato di generazione 1 e quello di generazione 2 esiste gia' dentro il gioco di generazione 2, scritta dagli autori originali per il Time Capsule, ed e' leggibile nel disassemblato. Per chi costruisce un ponte verso la generazione 3 e' il precedente piu' utile che ci sia: mostra quali campi gli autori hanno lasciato cadere, quali hanno inventato e come hanno gestito il byte che in generazione 1 e' il tasso di cattura e in generazione 2 l'oggetto tenuto. Non e' un'analogia, e' lo stesso problema risolto da chi aveva scritto entrambi i formati.

Il lato generazione 2 trasmette inoltre un blocco separato per la posta, con un preambolo proprio e una propria lista di correzione, e questa e' la ragione strutturale per cui i progetti esistenti dichiarano di non poter trasferire un Pokemon che tiene una lettera.

## Perche' questa nota e' collaudabile senza hardware

Il fatto piu' utile in pratica: BGB espone il cavo Link su una connessione TCP con un protocollo documentato a pacchetti di otto byte, e `PokemonGB_Online_Trades` implementa gli scambi proprio su quell'interfaccia. Tutto quanto descritto in questa nota si puo' quindi implementare e verificare in emulazione, senza toccare una console, a una condizione che vale dichiarare: verificarlo contro un gioco vero richiede la ROM di quel gioco, e dentro il perimetro del progetto quella ROM viene dal dump di una cartuccia propria, quindi dal lettore. Il dettaglio di come si organizza quel collaudo, e cosa resta possibile prima che il lettore arrivi, sta in [[21-collaudo]].

## Cosa leggere dopo

[[09-esecuzione-codice]] mostra come lo stesso canale diventi un canale di esecuzione, e [[10-multiboot-hardware]] copre il lato Game Boy Advance.
