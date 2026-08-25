---
tipo: nota di studio
livello: fondamenta
tags: [endianness, bit, formati]
up: "[[index]]"
vedi_anche: ["[[01-fondamenta-salvataggio]]", "[[06-identita-pokemon]]", "[[DATA-FORMATS_Gen1-Gen2-Gen3]]"]
---

# Numeri, byte e bit: come si legge un dato senza sbagliarlo in silenzio

Tutti gli errori descritti in questa nota hanno una proprieta' comune, ed e' la ragione per cui la nota esiste: non fanno rumore. Un offset sbagliato di solito produce un crash o un valore assurdo, e lo si nota. Un byte letto nell'ordine sbagliato o un nibble estratto dalla meta' sbagliata producono un numero perfettamente plausibile, e passano tutti i controlli a occhio.

## L'ordine dei byte

Un numero che non sta in un byte solo occupa due o quattro byte consecutivi, e c'e' una scelta arbitraria da fare: mettere per primo il byte piu' significativo o quello meno significativo. La prima scelta si chiama *big-endian*, la seconda *little-endian*, e le due sono incompatibili senza essere distinguibili guardando i byte.

Le generazioni 1 e 2 girano su un processore Sharp LR35902 e usano big-endian: i due byte `01 F4` valgono 500. La generazione 3 gira su un ARM7TDMI e usa little-endian: gli stessi due byte valgono 62465. Questo significa che un parser scritto per Gen 1 e riusato su Gen 3 senza cambiare l'ordine produce numeri sbagliati che restano numeri validi, e per esempio un livello letto al contrario resta un livello.

C'e' un caso limite che vale registrare perche' sembra una contraddizione: i checksum di generazione 2 sono a 16 bit little-endian, in una generazione che per tutto il resto e' big-endian. Non e' un errore di documentazione, e' una scelta del codice originale, e chi scrive un writer deve trattare quel campo diversamente da tutti gli altri.

## Nibble e campi di bit

Un byte sono otto bit, e i giochi di quell'epoca non si permettevano di sprecarne nemmeno uno. Da qui due tecniche che ricorrono in tutte le strutture.

La prima e' il *nibble*, cioe' la meta' di un byte, quattro bit, che tiene un valore da 0 a 15. Le generazioni 1 e 2 memorizzano quattro DV in due soli byte proprio cosi': il primo byte porta l'Attacco nel nibble alto e la Difesa nel nibble basso, il secondo la Velocita' nel nibble alto e lo Speciale nel nibble basso. Estrarre il nibble alto significa spostare a destra di quattro posizioni, estrarre quello basso significa mascherare con 0x0F, e scambiare i due e' l'errore silenzioso per eccellenza.

La seconda e' il *campo di bit*, cioe' un numero che occupa un intervallo di bit non allineato al byte. Il caso piu' denso in questo progetto e' la parola da 32 bit della generazione 3 che tiene sei valori individuali da 5 bit ciascuno, piu' il flag di uovo e lo slot di abilita': in trentadue bit stanno otto informazioni. Leggere un campo di bit significa spostare a destra di quanti bit lo precedono e mascherare con tanti uni quanti ne occupa, e scriverlo significa azzerare quella finestra e inserirvi il valore, senza toccare i vicini.

Un dettaglio che fa sbagliare spesso: quando i bit di un campo attraversano il confine fra due byte, l'ordine dei byte torna a contare. Per questo conviene leggere l'intera parola nel suo ordine corretto e poi lavorare sui bit del numero, invece di lavorare byte per byte.

## Il byte che contiene due cose diverse

Esiste una variante del campo di bit che merita una menzione a se', perche' e' un caso in cui due informazioni concettualmente separate condividono un byte per pura economia. Nelle generazioni 1 e 2 il byte dei PP di una mossa usa i sei bit bassi per i punti potenza correnti e i due bit alti per il numero di PP Up applicati. In generazione 3 quelle due informazioni finiscono in posti diversi, i PP nella sottostruttura delle mosse e i bonus in quella della crescita, quindi la conversione deve smontare un byte e distribuirlo su due strutture.

## Perche' questo si genera invece di trascriverlo

La conclusione operativa di questa nota e' un metodo, non una tabella. Ogni volta che un valore costante puo' essere ricavato da una fonte autorevole, va ricavato da quella fonte con un programma, e non ricopiato a mano dentro il codice. Il progetto ha una dimostrazione concreta di quanto serva: la tabella di codifica dei caratteri era sbagliata in due punti in tutte le fonti secondarie consultate, e l'errore e' emerso solo confrontandola con il charmap del disassemblato. La risposta non e' stata correggere la tabella a mano ma generarla, e lo strumento e' descritto in [[22-strumenti]].

## Cosa leggere dopo

[[03-integrita-checksum]] spiega cosa protegge questi byte da una lettura o scrittura sbagliata, e [[06-identita-pokemon]] mostra i campi di bit piu' densi del progetto nel loro contesto.
