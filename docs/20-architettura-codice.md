---
tipo: nota di studio
livello: codice
tags: [architettura, moduli, progetto]
up: "[[index]]"
vedi_anche: ["[[07-conversione-vincoli]]", "[[21-collaudo]]", "[[22-strumenti]]", "[[30-opzioni-implementative]]"]
---

# Architettura del software: stratificare cio' che non dipende dalla scelta

Il progetto ha una decisione aperta, registrata come ADR-008, fra quattro strade implementative molto diverse fra loro. La tentazione naturale e' aspettare la decisione prima di scrivere codice. Questa nota sostiene il contrario, e propone una stratificazione in cui la maggior parte del lavoro e' indipendente dalla scelta.

## L'osservazione che rende possibile tutto

Chiunque trasferisca un Pokemon da generazione 1 o 2 a generazione 3 deve fare le stesse cose, indipendentemente da dove giri il codice. Deve interpretare la struttura sorgente, tradurre il testo, mappare la specie, ricostruire i campi che non esistono, comporre la struttura di destinazione, cifrarla e calcolarne il checksum. Che questo avvenga in Python su un portatile o in C su una GBA compilato con devkitARM non cambia niente della logica: cambia soltanto da dove arrivano i byte e dove vanno.

Ne segue che il confine architetturale giusto non e' fra generazioni: e' fra la logica di formato e conversione da un lato, e il trasporto dall'altro.

## I cinque strati

Il primo strato e' quello dei dati costanti generati. Non contiene logica: contiene le tabelle che nessuno deve scrivere a mano, cioe' le due codifiche dei caratteri, la loro traduzione, la mappa dagli indici interni di generazione 1 ai numeri nazionali e le soglie di sesso per specie. Sono file JSON prodotti da script a partire dai disassemblati, e la ragione per cui sono uno strato e non un dettaglio e' spiegata in [[05-testo-e-charmap]].

Il secondo strato e' quello dei modelli. Un Pokemon di generazione 1, uno di generazione 2 e uno di generazione 3 sono tre tipi distinti, ciascuno con i propri campi, e nessuno dei tre sa nulla degli altri. Questa separazione costa qualche riga in piu' e paga subito, perche' evita il modello unico con i campi opzionali, che e' il modo classico di rendere impossibile capire quali campi siano validi quando.

Il terzo strato e' quello di lettura e scrittura, e va tenuto separato dai modelli. Un lettore prende byte e restituisce un modello; uno scrittore prende un modello e restituisce byte. Sono le sole parti che conoscono gli offset, l'ordine dei byte, la cifratura e i checksum, e sono anche le sole che si possono collaudare con una proprieta' forte: leggere e riscrivere deve restituire byte identici. Quel test da solo copre la maggior parte degli errori possibili in questo strato.

Il quarto strato e' la conversione, che e' l'unico posto dove si prendono decisioni discutibili. Prende un modello sorgente e produce un modello di destinazione, e va scritto in modo che le sue scelte siano parametri espliciti e non costanti sparse: la politica per gli EV, quella per i valori individuali, quella per il gioco di origine, quella per i caratteri senza destinazione. La tabella dei quattro metodi del PCCS, che come si vede in [[07-conversione-vincoli]] non e' implementata da nessuno, e' l'insieme di valori che questi parametri devono poter assumere.

Il quinto strato e' il trasporto, e questo si', dipende dalla scelta fra le quattro opzioni. Puo' essere un lettore di file di salvataggio, il protocollo seriale su BGB via TCP, il protocollo seriale su hardware reale attraverso un adattatore, oppure niente affatto se il codice gira dentro la console. Ma qualunque sia, parla con lo strato di lettura e scrittura e non con quello di conversione.

## Perche' l'ordine di costruzione conta

C'e' un vincolo di ordine che nasce dal formato e va rispettato anche nel codice, ed e' descritto in [[04-cifratura-gen3]]: il valore di personalita' e' anche chiave di cifratura e selettore di permutazione, quindi va deciso prima di comporre la struttura. Uno scrittore che permette di cambiarlo dopo, invalidando silenziosamente il blocco gia' composto, e' uno scrittore che produrra' Uova Difettose.

La conseguenza pratica e' che il modello di generazione 3 non dovrebbe permettere di modificare il valore di personalita' dopo la costruzione. Renderlo immutabile e' una scelta di progettazione che chiude a chiave un intero genere di bug.

## Che linguaggio

La decisione non e' presa e questa nota non la prende, ma ci sono due osservazioni utili. La prima e' che gli strati dal primo al quarto sono aritmetica su interi e manipolazione di byte, cioe' il tipo di codice che si scrive bene in qualsiasi linguaggio e si collauda bene solo dove i test costano poco da scrivere. La seconda e' che se un giorno la logica dovesse girare su console, l'unica strada e' il C compilato con devkitARM, e riscrivere aritmetica su interi da un linguaggio a un altro e' fra le riscritture meno dolorose che esistano, purche' i test siano dati e non codice.

Da qui una raccomandazione concreta: qualunque linguaggio si scelga, i casi di prova vanno tenuti come dati esterni, per esempio coppie di byte attesi in file JSON, cosi' che sopravvivano a una riscrittura. E' la stessa idea dei dati generati del primo strato, applicata ai test.

## Cosa leggere dopo

[[21-collaudo]] descrive la strategia di verifica strato per strato, e [[22-strumenti]] documenta cio' che esiste gia'.
