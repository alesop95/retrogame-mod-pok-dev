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

## La specifica esatta, dalla bocca dell'autore

Fin qui il meccanismo era ricostruito: la primitiva dal codice del gioco, la conseguenza dal codice del ponte. La specifica precisa dell'innesco l'ha pubblicata l'autore di Poke Transporter GB nell'articolo del suo dev log titolato The Power of a REALLY Big Party, e il titolo e' la risposta: la squadra grande non e' un contesto, e' l'exploit.

Le sue parole descrivono l'innesco come una squadra di 352 Pokemon con identificativo interno 0xE3, seguita da un Pokemon con identificativo interno 0xFC, che corrompe lo stack e dirotta l'esecuzione. Vale la pena fermarsi su ciascuno dei tre numeri, perche' insieme spiegano tutto quanto detto sopra.

Il conteggio 352 e' molto oltre i sei di una squadra legittima, ed e' cio' che fa scrivere la funzione di stampa dei nomi fino a superare il buffer video e raggiungere lo stack: e' la conseguenza diretta dell'assenza del terminatore descritta sopra, misurata in quanto lontano serve arrivare.

L'identificativo 0xE3 e' il riempimento, cioe' la specie che occupa le 352 posizioni. Cade nell'intervallo che [[06-identita-pokemon]] descrive come invalido in generazione 1, e serve non per cio' che rappresenta ma per il byte che il gioco recupera cercandone il nome.

L'identificativo 0xFC e' il vettore, cioe' il valore che, letto dalla tabella dei nomi, fornisce i byte che diventano l'indirizzo di ritorno sovrascritto. Vale la pena notare che lo stesso indice compare nella ricerca sui glitch come TRAINER 4, che e' una delle porte d'ingresso classiche all'esecuzione di codice in generazione 1: se sia la stessa strada percorsa in senso opposto oppure una coincidenza fra due usi dello stesso indice e' una mia congettura e non un fatto stabilito, e per deciderlo servirebbe leggere il payload generato.

Con questi tre numeri l'affermazione che il ponte usa esecuzione di codice remota non e' piu' un'inferenza dal codice: e' una dichiarazione dell'autore, e il codice ne e' la conferma.

## Il lato che scrive: il Dono Segreto, non la struttura

C'e' una seconda scoperta nello stesso dev log, e cambia il modo di immaginare il lato generazione 3. Chi legge la referenza dei formati si aspetta che il ponte, dopo aver convertito, scriva la struttura da 80 o 100 byte nel posto giusto del salvataggio. Non fa questo.

Nell'articolo titolato The Main Event l'autore descrive di iniettare un evento Dono Segreto nella sezione del salvataggio destinata agli script in RAM, dove lo spazio disponibile e' fatto di due byte di checksum, due di riempimento e mille byte per lo script, e lo script usa il comando `CallASM` per chiamare il codice assembly del gioco, facendo depositare il Pokemon nel deposito PC e aggiornare il Pokedex.

La differenza e' architetturale e va capita perche' e' elegante. Scrivere la struttura significa assumersi la responsabilita' di ogni campo derivato, di ogni indice, di ogni coerenza interna; far eseguire al gioco la propria routine di deposito significa che il gioco fa cio' che farebbe normalmente, e la coerenza e' garantita da chi ha scritto il gioco. Il prezzo e' che serve conoscere l'indirizzo di quelle routine, e quell'indirizzo cambia con la versione e con la lingua: l'autore dichiara quarantotto combinazioni fra release e lingue, gestite con un compilatore assembly scritto per l'occasione.

E' la seconda ragione, indipendente dal payload sul lato Game Boy, per cui il supporto di quel progetto e' per versione e per lingua, e per cui una cartuccia contraffatta rompe tutto.

## Il lato generazione 3: un escape di testo, e una differenza fra versioni

Tutto quanto precede riguarda le generazioni 1 e 2. Sul lato generazione 3 il progetto non aveva nulla, e la lettura del canale del Glitch City Research Institute fatta il 2026-08-26 ha prodotto un quadro abbastanza preciso da essere utile, con una distinzione fra versioni che vale piu' di tutto il resto.

Il punto di partenza e' un dettaglio del formato del testo, che [[05-testo-e-charmap]] tratta come questione di codifica e che qui diventa una superficie di attacco. In generazione 3 due byte non sono caratteri ma comandi rivolti al motore che stampa il testo: il byte 0xFC introduce un codice di controllo, cioe' dice al motore che cio' che segue va interpretato come istruzione e non come lettera, e il byte 0xFD introduce la sostituzione di una variabile di stringa. Un nome, quindi, non e' soltanto una sequenza di caratteri: e' un programma per il motore di stampa, e chi controlla quei byte controlla in parte cio' che il motore fa.

Qui interviene la differenza fra versioni, ed e' netta. In Rosso Fuoco, Verde Foglia e Smeraldo le funzioni associate ai codici di controllo sono selezionate da un costrutto di scelta multipla, che per costruzione non fa nulla quando l'indice e' fuori intervallo: un indice assurdo produce quindi un nulla di fatto. In Rubino e Zaffiro le stesse funzioni sono prelevate da una tabella di puntatori senza alcun controllo dei limiti, e un indice fuori intervallo diventa una lettura oltre la tabella, cioe' un indirizzo preso da memoria che si puo' manipolare, cioe' esecuzione di codice arbitrario. E' un esempio da manuale di come la stessa funzionalita' scritta in due modi equivalenti abbia conseguenze di sicurezza opposte, e della ragione per cui il controllo dei limiti non e' una formalita'.

La catena documentata su Smeraldo non passa quindi dai codici di controllo fuori intervallo ma da una posta difettosa, e vale la pena seguirla perche' mostra quanto sia lunga una catena reale. Una posta rimossa fuori da un edificio lascia in memoria una stringa senza terminatore; il gioco, leggendo il nome dell'allenatore che l'avrebbe scritta, prosegue oltre la posta e oltre la cassetta, attraversa sessantaquattro byte di una struttura secondaria e arriva ai dati delle tendenze di una citta'; la prima di quelle tendenze contiene la sequenza 0xFD 0x00, che il gioco riconosce come sostituzione della variabile di stringa numero zero, una variabile che nessuno aveva previsto di usare e il cui puntatore cade in una posizione arbitraria della memoria interna di lavoro; da la' la lettura prosegue attraverso zeri fino a incontrare i dati della squadra del giocatore, e dentro la squadra incontra nell'ordine il valore di personalita' e l'identificativo dell'allenatore, il soprannome, i byte di lingua e di flag, il nome dell'allenatore, le marcature, il checksum e infine il blocco cifrato; nel blocco cifrato incontra la sequenza 0xFC seguita dal valore che l'autore ha costruito scegliendo opportunamente i punti potenza delle mosse, quella sequenza viene interpretata come codice di controllo, e il gioco chiama come funzione un indirizzo che cade dentro il soprannome di un Pokemon in deposito.

Tre cose di questa catena meritano di essere estratte, perche' valgono anche fuori dal caso specifico.

La prima e' che l'ordine in cui il motore di stampa incontra i campi della struttura e' esattamente l'ordine dell'intestazione documentato nella sezione 5 di [[DATA-FORMATS_Gen1-Gen2-Gen3]], ed e' quindi una conferma indipendente di quel layout, arrivata da una fonte che non stava documentando il formato ma sfruttandolo. Conferme di questo tipo sono fra le piu' affidabili che esistano, perche' chi le produce paga un prezzo immediato se sbaglia.

La seconda e' che i byte cercati stanno nel blocco cifrato, e che l'autore li ottiene scegliendo i punti potenza. Non e' una contraddizione: poiche' la cifratura e' uno XOR con una chiave derivata dal valore di personalita' e dall'identificativo dell'allenatore, chi controlla il contenuto in chiaro e la chiave controlla anche il testo cifrato, e puo' cercare la combinazione che produce i byte desiderati dopo la cifratura. E' anche la ragione per cui il soprannome deve essere una serie di lettere identiche e il nome dell'allenatore un'altra: quei campi non sono decorativi, sono il riempimento che porta la lettura fino al punto giusto.

La terza e' che il codice vero risiede nei soprannomi dei Pokemon in deposito e nei nomi dei box, che stanno in memoria subito dopo di essi. I Pokemon inesistenti dei box vuoti si comportano da istruzioni innocue, e la lettura scorre fino ad arrivare al codice utile. E' la stessa idea del deposito di codice nei nomi dei box che le generazioni 1 e 2 usano, applicata a un'architettura diversa.

Una via alternativa, piu' vicina al nostro dominio, la nomina un altro partecipante allo stesso canale: si puo' semplicemente scambiare un Pokemon che contenga la sequenza di controllo, facendola arrivare nel buffer di ricezione del blocco. E' interessante perche' e' esattamente il canale che il ponte usa, e va registrata come rischio prima che come opportunita': una struttura costruita male, scambiata verso un gioco di generazione 3, non e' solo un dato sbagliato, e' potenzialmente un dato che quel gioco esegue.

Su tutto questo va detto che il progetto non ha alcun bisogno di eseguire codice sul lato generazione 3, perche' la via scelta dai tool esistenti e' un'altra e la descrive la sezione precedente. Lo si studia per due ragioni: perche' spiega quali strutture un gioco di generazione 3 accetta e quali gli fanno fare cose non previste, e perche' la differenza fra il costrutto di scelta multipla e la tabella senza controllo dei limiti e' una delle lezioni piu' trasferibili che questo dominio offra.

## Un vincolo del traboccamento della squadra che si scopre solo provando

Un'ultima aggiunta sul lato generazione 2, che viene dallo stesso canale e ha un valore pratico immediato per chiunque costruisca strutture da inviare sul cavo. Nelle procedure che sfruttano il traboccamento della lista della squadra esiste una condizione necessaria non ovvia: nessuno dei Pokemon usati puo' avere un identificativo dell'allenatore che contenga un byte di valore 0xFF, ne' nel byte alto ne' nel basso, altrimenti la procedura non funziona.

La ragione e' la stessa che rende possibile l'attacco: 0xFF e' il terminatore della lista delle specie, e il gioco lo cerca scorrendo la memoria. Un identificativo dell'allenatore che contenga quel byte introduce un terminatore in un posto dove non era previsto, e la scansione si ferma prima. E' un buon esempio di una proprieta' che [[02-numeri-e-bit]] enuncia in astratto, cioe' che su queste architetture un valore e un marcatore condividono lo spazio dei byte e non c'e' nulla che li distingua: qui la conseguenza e' che un campo di dati puo' accidentalmente terminare una struttura.

Nello stesso contesto compaiono una seconda condizione, specifica di Cristallo, per cui nessuna statistica dei Pokemon coinvolti puo' valere 21, punti salute correnti e massimi inclusi, e una terza per cui i cicli di cova residui di un uovo dipendono dai punti potenza della sua quarta mossa. Sono tutti casi dello stesso fenomeno, cioe' campi che il gioco riusa per scopi diversi da quello dichiarato, e sono la ragione per cui [[20-architettura-codice]] insiste che il lettore conservi ogni byte anche quando non ne conosce il significato.

## Le vie dal lato del giocatore, per completezza

Esiste una letteratura ampia su come ottenere esecuzione di codice giocando, senza alcun hardware esterno, e non serve al ponte ma serve a orientarsi nel campo e a valutare alternative. In generazione 1 le vie piu' pratiche sono gli oggetti glitch il cui puntatore di effetto cade nei dati della squadra, chiamati 8F nelle versioni inglesi di Rosso e Blu e ws m in Giallo, che si usano come trampolino per saltare in una zona piu' comodamente scrivibile come lo zaino. In Oro e Argento la via nota e' il glitch del Salvadanaio, che finisce per eseguire dalla echo RAM. In Cristallo si passa da un nome non terminato ottenuto con il glitch dei cloni difettosi, con i nomi dei box usati come deposito del codice.

Il catalogo completo sta sul Glitch City Wiki, che [[SOURCES]] elenca insieme al suo mirror statico, perche' il sito respinge le richieste automatiche.

## Cosa leggere dopo

[[10-multiboot-hardware]] copre il lato che riceve, cioe' il Game Boy Advance, e [[21-collaudo]] spiega come si prova tutto questo senza rompere una cartuccia.
