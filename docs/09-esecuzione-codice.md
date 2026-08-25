---
tipo: nota di studio
livello: avanzato
tags: [ace, exploit, payload, sicurezza]
up: "[[index]]"
vedi_anche: ["[[08-cavo-link]]", "[[10-multiboot-hardware]]", "[[30-opzioni-implementative]]", "[[SOURCES]]"]
---

# Far eseguire codice proprio a un gioco del 1996

Questa nota spiega come si arriva a far eseguire a un gioco Game Boy un programma che i suoi autori non hanno scritto, perche' e' il meccanismo su cui poggia il ponte fra generazioni. Il contesto e' interamente quello di questo progetto, cioe' cartucce possedute e console propria, e la ragione per cui vale la pena capirlo invece di usarlo come scatola nera e' che le sue proprieta' spiegano tutti i limiti dei tool esistenti.

## Il concetto

Un processore non distingue fra dati e istruzioni: distingue solo fra l'indirizzo da cui sta leggendo istruzioni e tutto il resto. Se un bug fa deviare il flusso di esecuzione verso una zona di memoria il cui contenuto e' controllato dal giocatore, il processore eseguira' quel contenuto come programma. Questa e' l'esecuzione di codice arbitrario, e su queste console e' particolarmente potente perche' non c'e' nessuna protezione: nessuna separazione fra memoria eseguibile e memoria dati, nessun controllo sugli indirizzi, nessun sistema operativo sotto.

Il risultato e' che chi ottiene la deviazione ottiene la macchina: puo' leggere e scrivere qualsiasi indirizzo, compresa la SRAM della cartuccia, e puo' pilotare qualsiasi periferica, compresa la porta seriale.

## La primitiva piu' elegante: un terminatore che manca

Il vettore che conta per questo progetto passa dal cavo, e sfrutta una proprieta' che [[08-cavo-link]] descrive come innocua. La lista degli indici di specie in una squadra e' terminata da un byte 0xFF, e i cicli del gioco iterano finche' non lo trovano.

Quando il gioco riceve una squadra dal cavo e ne stampa i nomi per mostrarli al giocatore, itera su quella lista. Una squadra costruita senza terminatore fa proseguire l'iterazione oltre la fine della lista, e la scrittura dei nomi continua oltre il buffer video, arrivando fino all'area dello stack e sovrascrivendo un indirizzo di ritorno. Da quel momento il flusso di esecuzione va dove ha deciso chi ha costruito la squadra.

I passi successivi sono un esercizio di catena: l'indirizzo raggiungibile porta prima al nome del giocatore avversario, che sono undici byte controllabili, sufficienti per un salto; il salto porta alla lista di correzione, che offre quasi duecento byte utili di codice. C'e' una simmetria che vale notare: il campo che esiste per aggirare un limite del protocollo e' anche il piu' grande buffer controllabile che il protocollo trasmette.

## Che cosa ci fa il ponte

Sul modo in cui il progetto di riferimento usa questa primitiva il suo README non dice nulla, ma il codice lo dice con chiarezza, e la risposta e' piu' pulita di quanto si potrebbe immaginare. Durante la fase di scambio delle squadre, la funzione che risponde al Game Boy non invia una squadra: invia byte per byte un buffer precalcolato.

```cpp
byte exchange_parties(byte curr_in, byte *curr_payload)
{
  int ret = curr_payload[data_counter];
  data_counter += 1;
  return ret;
};
```

Quel buffer e' un programma Z80. Il repository contiene un generatore di payload con un assemblatore Z80 proprio, un generatore di patch binarie e tabelle di valori di ROM per lingua.

Il quadro completo e' quindi questo: il giocatore non deve fare nessun setup dentro il gioco, non serve nessun oggetto glitch e nessuna procedura preparatoria, e l'esecuzione di codice viene ottenuta interamente dal lato ricevente, mandando al Game Boy una finta squadra che e' codice. E' esecuzione di codice remota attraverso il cavo.

Da qui seguono due conseguenze che il README elenca senza spiegarle, e che ora si capiscono. Il supporto e' per lingua e variante di ROM, perche' il payload contiene indirizzi assoluti che dipendono da quella specifica compilazione del gioco. E le cartucce contraffatte fanno sparire i Pokemon, perche' hanno una ROM diversa da quella su cui il payload e' tarato, quindi il salto finisce da qualche altra parte.

## Il precedente minimale, che e' anche il piu' istruttivo

`PkSploit` fa la stessa cosa in forma ridotta all'essenziale: un Arduino si finge un Game Boy sul cavo, avvia uno scambio, trasmette una squadra malformata e ottiene esecuzione di codice. Con i circa centonovantadue byte utili di payload apre un'interfaccia di lettura e scrittura sulla memoria, e da la' dumpa la ROM e legge e scrive la SRAM.

Vale la pena fermarsi su cosa significhi: un microcontrollore da pochi euro, collegato solo al connettore del cavo, ottiene accesso completo alla cartuccia senza alcun lettore dedicato. Per l'opzione D di [[30-opzioni-implementative]] e' il riferimento piu' vicino all'obiettivo, e per il progetto in generale e' la dimostrazione che il cavo, da solo, e' un canale di accesso completo.

## Le vie dal lato del giocatore, per completezza

Esiste una letteratura ampia su come ottenere esecuzione di codice giocando, senza alcun hardware esterno, e non serve al ponte ma serve a orientarsi nel campo e a valutare alternative. In generazione 1 le vie piu' pratiche sono gli oggetti glitch il cui puntatore di effetto cade nei dati della squadra, chiamati 8F nelle versioni inglesi di Rosso e Blu e ws m in Giallo, che si usano come trampolino per saltare in una zona piu' comodamente scrivibile come lo zaino. In Oro e Argento la via nota e' il glitch del Salvadanaio, che finisce per eseguire dalla echo RAM. In Cristallo si passa da un nome non terminato ottenuto con il glitch dei cloni difettosi, con i nomi dei box usati come deposito del codice.

Il catalogo completo sta sul Glitch City Wiki, che [[SOURCES]] elenca insieme al suo mirror statico, perche' il sito respinge le richieste automatiche.

## Cosa leggere dopo

[[10-multiboot-hardware]] copre il lato che riceve, cioe' il Game Boy Advance, e [[21-collaudo]] spiega come si prova tutto questo senza rompere una cartuccia.
