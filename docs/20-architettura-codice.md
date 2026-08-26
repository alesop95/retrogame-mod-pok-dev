---
tipo: nota di studio
livello: codice
tags: [architettura, moduli, progetto]
up: "[[index]]"
vedi_anche: ["[[07-conversione-vincoli]]", "[[21-collaudo]]", "[[22-strumenti]]", "[[30-opzioni-implementative]]"]
---

# Architettura del software: stratificare ciò che non dipende dalla scelta

Il progetto ha una decisione aperta, registrata come ADR-008, fra quattro strade implementative molto diverse fra loro. La tentazione naturale è aspettare la decisione prima di scrivere codice. Questa nota sostiene il contrario, e propone una stratificazione in cui la maggior parte del lavoro è indipendente dalla scelta.

## L'osservazione che rende possibile tutto

Chiunque trasferisca un Pokemon da generazione 1 o 2 a generazione 3 deve fare le stesse cose, indipendentemente da dove giri il codice. Deve interpretare la struttura sorgente, tradurre il testo, mappare la specie, ricostruire i campi che non esistono, comporre la struttura di destinazione, cifrarla e calcolarne il checksum. Che questo avvenga in Python su un portatile o in C su una GBA compilato con devkitARM non cambia niente della logica: cambia soltanto da dove arrivano i byte e dove vanno.

Ne segue che il confine architetturale giusto non è fra generazioni: è fra la logica di formato e conversione da un lato, e il trasporto dall'altro.

## I cinque strati

Il primo strato è quello dei dati costanti generati. Non contiene logica: contiene le tabelle che nessuno deve scrivere a mano, cioè le due codifiche dei caratteri, la loro traduzione, la mappa dagli indici interni di generazione 1 ai numeri nazionali e le soglie di sesso per specie. Sono file JSON prodotti da script a partire dai disassemblati, e la ragione per cui sono uno strato e non un dettaglio è spiegata in [[05-testo-e-charmap]].

Il secondo strato è quello dei modelli. Un Pokemon di generazione 1, uno di generazione 2 e uno di generazione 3 sono tre tipi distinti, ciascuno con i propri campi, e nessuno dei tre sa nulla degli altri. Questa separazione costa qualche riga in più e paga subito, perché evita il modello unico con i campi opzionali, che è il modo classico di rendere impossibile capire quali campi siano validi quando.

Il terzo strato è quello di lettura e scrittura, e va tenuto separato dai modelli. Un lettore prende byte e restituisce un modello; uno scrittore prende un modello e restituisce byte. Sono le sole parti che conoscono gli offset, l'ordine dei byte, la cifratura e i checksum, e sono anche le sole che si possono collaudare con una proprietà forte: leggere e riscrivere deve restituire byte identici. Quel test da solo copre la maggior parte degli errori possibili in questo strato.

Il quarto strato è la conversione, che è l'unico posto dove si prendono decisioni discutibili. Prende un modello sorgente e produce un modello di destinazione, e va scritto in modo che le sue scelte siano parametri espliciti e non costanti sparse: la politica per gli EV, quella per i valori individuali, quella per il gioco di origine, quella per i caratteri senza destinazione. La tabella dei quattro metodi del PCCS, che come si vede in [[07-conversione-vincoli]] non è implementata da nessuno, è l'insieme di valori che questi parametri devono poter assumere.

Il quinto strato è il trasporto, e questo sì, dipende dalla scelta fra le quattro opzioni. Può essere un lettore di file di salvataggio, il protocollo seriale su BGB via TCP, il protocollo seriale su hardware reale attraverso un adattatore, oppure niente affatto se il codice gira dentro la console. Ma qualunque sia, parla con lo strato di lettura e scrittura e non con quello di conversione.

## Perché l'ordine di costruzione conta

C'è un vincolo di ordine che nasce dal formato e va rispettato anche nel codice, ed è descritto in [[04-cifratura-gen3]]: il valore di personalità è anche chiave di cifratura e selettore di permutazione, quindi va deciso prima di comporre la struttura. Uno scrittore che permette di cambiarlo dopo, invalidando silenziosamente il blocco già composto, è uno scrittore che produrrà Uova Difettose.

La conseguenza pratica è che il modello di generazione 3 non dovrebbe permettere di modificare il valore di personalità dopo la costruzione. Renderlo immutabile è una scelta di progettazione che chiude a chiave un intero genere di bug.

## Dove gira questo codice

La domanda non è oziosa e merita una risposta precisa, perché il codice scritto finora è Python e un Game Boy Advance non esegue Python. Vale la pena mettere in fila le quattro forme che il sistema finito può assumere, perché due di esse non richiedono alcuna riscrittura e due sì.

| Forma | Dove gira la logica di formato e conversione | Che cosa serve in più |
|---|---|---|
| Opzione B, tool su PC | interamente sul PC, in Python | un lettore di cartucce per ottenere e riscrivere i dump |
| Opzione D, dispositivo intermedio | sul PC in Python; sul microcontrollore solo il protocollo seriale | firmware in C o C++ per il microcontrollore, poche centinaia di righe |
| Opzione A, usare Poke Transporter GB | sulla console, dentro codice di altri | nulla da scrivere, ma nulla da riusare del nostro |
| Opzione C, ponte homebrew proprio | sulla console, in C compilato con devkitARM | riscrittura degli strati di formato e conversione |

Ne segue la correzione a una cosa che ho scritto in modo troppo sbrigativo in una sessione precedente, cioè che il Python sarebbe un prototipo in attesa di una riscrittura in C. È vero soltanto per l'opzione C. Nelle opzioni B e D il Python è il linguaggio definitivo della logica, non un passaggio intermedio: nell'opzione D il microcontrollore fa il lavoro che nessun PC può fare, cioè parlare un protocollo seriale sincrono a tempo con un Game Boy, e tutto il resto resta sul PC. È esattamente la forma di `PkSploit` e di `PokemonGB_Online_Trades`, entrambi descritti in [[SOURCES]], e ha la proprietà notevole di rendere superfluo anche il lettore di cartucce, perché il canale di accesso diventa il connettore del cavo.

L'opzione A merita una nota a sé. È l'unica in cui non si scrive quasi nulla, ma è anche l'unica in cui nulla del nostro codice serve, perché la logica sta dentro un programma altrui. Chi la sceglie non sta scegliendo un'architettura, sta scegliendo di non averne una.

## Che linguaggio, e quando la riscrittura costa

Gli strati dal primo al quarto sono aritmetica su interi e manipolazione di byte, cioè il tipo di codice che si scrive bene in qualsiasi linguaggio e si collauda bene solo dove i test costano poco da scrivere. Python è stato scelto per due ragioni concrete: gli strumenti già nel repository sono Python, e in un progetto dove la verifica conta più della prestazione il costo di scrivere una prova è la variabile che decide quante prove esistono.

Se un giorno servisse l'opzione C, la riscrittura in C riguarderebbe gli strati dal secondo al quarto, e sarebbe fra le riscritture meno dolorose che esistano a una condizione: che i casi di prova siano dati e non codice. Oggi quella condizione non è rispettata, perché le prove sono metodi Python che generano i propri buffer. Trasformarle in vettori su file, cioè coppie di byte attesi in JSON, è un lavoro piccolo che rende la suite riusabile da un'implementazione in qualsiasi linguaggio, e va fatto prima che la suite diventi grande. È la stessa idea dei dati generati del primo strato, applicata ai test, e resta il debito tecnico più evidente del pacchetto.

## Cosa leggere dopo

[[21-collaudo]] descrive la strategia di verifica strato per strato, e [[22-strumenti]] documenta ciò che esiste già.
