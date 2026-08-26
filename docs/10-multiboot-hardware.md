---
tipo: nota di studio
livello: avanzato
tags: [gba, multiboot, hardware]
up: "[[index]]"
vedi_anche: ["[[08-cavo-link]]", "[[09-esecuzione-codice]]", "[[30-opzioni-implementative]]"]
---

# Il lato Game Boy Advance: multiboot, cavi e scambio a caldo

Il ponte ha due lati. Quello del Game Boy è descritto in [[08-cavo-link]] e [[09-esecuzione-codice]]; questo è il lato che riceve, converte e scrive, e i suoi vincoli sono tutti hardware.

## Perché il cavo deve essere quello sbagliato

La prima cosa che sorprende chi si avvicina al progetto è che serve il cavo del Game Boy Color e non quello del Game Boy Advance, nonostante uno dei due dispositivi sia una GBA. La ragione è che il lato che decide non è la GBA: è il gioco di generazione 1 o 2, che parla con l'hardware seriale del Game Boy, e non sa nulla delle modalità aggiuntive introdotte dalla console più recente.

La GBA è retrocompatibile e sa parlare quel protocollo, ma solo se il collegamento fisico è quello. I due cavi non sono elettricamente equivalenti per questo scenario, e usare quello sbagliato non produce un errore comprensibile: produce silenzio.

## Multiboot

Il programma che gira sulla GBA arriva senza cartuccia. La console ha una modalità hardware, documentata in GBATEK, che permette di ricevere un programma dal cavo e di eseguirlo in RAM: si chiama multiboot, e la sua esistenza è la ragione per cui progetti come questo si possono distribuire come file invece che come cartucce.

Le vie per spingere il programma dentro la console sono tre in pratica. Una console GameCube o Wii con homebrew, che invia il programma via cavo GBA; una flashcart che supporta il lancio in modalità multiboot; oppure un caricatore su flashcart per le flashcart che non lo supportano direttamente. Esiste anche la via da PC via USB, con hardware dedicato.

Il fatto architetturale che conta è che il programma gira in RAM, non da cartuccia. Ne segue che la cartuccia può essere qualsiasi cosa, compresa quella che il programma deve modificare, ed è precisamente questo che rende possibile il passo successivo.

## La procedura di multiboot, per come la documenta GBATEK

Vale scriverla perché è ciò che va implementato se si sceglie l'opzione C o D, e perché i numeri dicono quanto spazio si ha davvero.

L'apertura è una stretta di mano ripetuta: il master invia 0x6200 finché lo slave non risponde 0x0000, poi seguono uno scambio con 0x610y e 0x720x dove le cifre variabili identificano il client e lo slave. Il trasferimento vero e proprio ha una lunghezza che, esclusa l'intestazione, deve essere multipla di 0x10, con un minimo di 0x100 byte e un massimo di 0x3FF40, cioè circa 256 kilobyte. L'intestazione finisce in memoria fra 0x2000000 e 0x20000BF, e il programma occupa da 0x20000C0 a 0x203FFFF.

Da qui il vincolo che sorprende chi arriva dal mondo delle cartucce: gli indirizzi assoluti dentro il programma devono riferirsi a 0x2000000 e non a 0x8000000, perché il programma non gira dalla cartuccia ma dalla memoria di lavoro. Il trasferimento è inoltre protetto da trasformazioni XOR e da un checksum ciclico a 16 bit, e dopo ogni trasferimento il master deve attendere che il bit di start si azzeri nel registro di controllo seriale, più un ritardo di 36 microsecondi.

Sulla memoria in cui quel programma vive, la descrizione architetturale di Copetti dà le due cifre che contano: la memoria di lavoro interna è 32 kilobyte a 32 bit, quella esterna 256 kilobyte a 16 bit e fino a sei volte più lenta da raggiungere. Un programma multiboot vive nella seconda, e questo spiega perché i progetti di questo tipo curano la compressione dei dati.

## Il lato che scrive, che non è quello che si immagina

C'è un fatto architetturale che [[09-esecuzione-codice]] documenta e che va ripetuto qui, perché riguarda il lato Game Boy Advance. Il ponte di riferimento non scrive la struttura del Pokemon nel salvataggio di generazione 3: inietta un evento Dono Segreto nella sezione degli script in RAM, e lascia che il gioco stesso depositi il Pokemon e aggiorni il Pokedex chiamando le proprie routine. Chi progetta l'opzione C deve decidere quale delle due strade prendere, e sono decisioni molto diverse: scrivere la struttura richiede padroneggiare ogni campo derivato, iniettare uno script richiede conoscere gli indirizzi delle routine per ciascuna delle quarantotto combinazioni di versione e lingua.

## Lo scambio a caldo, che è la parte fragile

Il programma multiboot deve leggere e scrivere il salvataggio del gioco di generazione 3, quindi quella cartuccia deve essere inserita. Ma all'accensione la cartuccia inserita era quella di avvio. La soluzione è scambiarle mentre la console è accesa e il programma gira in RAM.

Questo funziona perché il programma non dipende più dalla cartuccia, ma non è privo di rischi: il connettore non è progettato per l'inserimento a caldo, e la console può resettarsi durante l'operazione. Il progetto di riferimento documenta il problema, lo attribuisce anche allo stato delle batterie e offre vie alternative per chi ha una flashcart che permette di evitarlo.

Vale la pena osservare che un reset durante lo scambio non è catastrofico in sé: è catastrofico se avviene mentre il programma sta scrivendo il salvataggio. Da qui il valore della regola sul backup: l'operazione ha una finestra di rischio reale, e l'unica difesa è avere una copia.

## Perché non si emula

Nessun emulatore riproduce l'interazione fra un Game Boy e un Game Boy Advance collegati da un cavo Link con questa dinamica. Il progetto di riferimento lo dichiara e nulla lo contraddice.

Ma la conclusione da trarne è più stretta di come viene spesso riportata, ed è una precisazione che cambia il piano di lavoro. Ciò che non si emula è il ponte fra le due console. Il collegamento fra due Game Boy si emula bene, perché BGB espone il cavo su TCP, quindi il lato protocollo di generazione 1 e 2 è collaudabile su emulatore, con la riserva spiegata in [[21-collaudo]]: provarlo contro un gioco vero richiede una ROM, e dentro il perimetro quella ROM viene dal dump di una cartuccia propria. E il lato generazione 3, cioè parser, writer, cifratura e checksum, si collauda contro file di salvataggio senza alcuna console. Solo il passaggio finale, il ponte vero, richiede il ferro.

## Che cosa serve avere in mano

Questa è la lista che l'handoff di ricerca chiamava discovery hardware, e resta il preliminare a qualsiasi scelta fra le opzioni di [[30-opzioni-implementative]]. Serve sapere quante console Game Boy Advance sono disponibili, perché due permettono la via più semplice al multiboot. Serve sapere se esiste un GameCube o un Wii con homebrew, che è l'alternativa alla seconda GBA. Serve sapere se c'è una flashcart e quale, perché il modello determina se lo scambio a caldo si può evitare. Serve un cavo Link del Game Boy Color, non del Game Boy Advance. E serve sapere se c'è la capacità di saldare e di programmare microcontrollori, che è il discriminante per l'opzione basata su hardware intermedio.

## Cosa leggere dopo

[[30-opzioni-implementative]] mette insieme questi vincoli con il costo di sviluppo di ciascuna strada.
