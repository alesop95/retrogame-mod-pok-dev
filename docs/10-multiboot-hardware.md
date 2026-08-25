---
tipo: nota di studio
livello: avanzato
tags: [gba, multiboot, hardware]
up: "[[index]]"
vedi_anche: ["[[08-cavo-link]]", "[[09-esecuzione-codice]]", "[[30-opzioni-implementative]]"]
---

# Il lato Game Boy Advance: multiboot, cavi e scambio a caldo

Il ponte ha due lati. Quello del Game Boy e' descritto in [[08-cavo-link]] e [[09-esecuzione-codice]]; questo e' il lato che riceve, converte e scrive, e i suoi vincoli sono tutti hardware.

## Perche' il cavo deve essere quello sbagliato

La prima cosa che sorprende chi si avvicina al progetto e' che serve il cavo del Game Boy Color e non quello del Game Boy Advance, nonostante uno dei due dispositivi sia una GBA. La ragione e' che il lato che decide non e' la GBA: e' il gioco di generazione 1 o 2, che parla con l'hardware seriale del Game Boy, e non sa nulla delle modalita' aggiuntive introdotte dalla console piu' recente.

La GBA e' retrocompatibile e sa parlare quel protocollo, ma solo se il collegamento fisico e' quello. I due cavi non sono elettricamente equivalenti per questo scenario, e usare quello sbagliato non produce un errore comprensibile: produce silenzio.

## Multiboot

Il programma che gira sulla GBA arriva senza cartuccia. La console ha una modalita' hardware, documentata in GBATEK, che permette di ricevere un programma dal cavo e di eseguirlo in RAM: si chiama multiboot, e la sua esistenza e' la ragione per cui progetti come questo si possono distribuire come file invece che come cartucce.

Le vie per spingere il programma dentro la console sono tre in pratica. Una console GameCube o Wii con homebrew, che invia il programma via cavo GBA; una flashcart che supporta il lancio in modalita' multiboot; oppure un caricatore su flashcart per le flashcart che non lo supportano direttamente. Esiste anche la via da PC via USB, con hardware dedicato.

Il fatto architetturale che conta e' che il programma gira in RAM, non da cartuccia. Ne segue che la cartuccia puo' essere qualsiasi cosa, compresa quella che il programma deve modificare, ed e' precisamente questo che rende possibile il passo successivo.

## La procedura di multiboot, per come la documenta GBATEK

Vale scriverla perche' e' cio' che va implementato se si sceglie l'opzione C o D, e perche' i numeri dicono quanto spazio si ha davvero.

L'apertura e' una stretta di mano ripetuta: il master invia 0x6200 finche' lo slave non risponde 0x0000, poi seguono uno scambio con 0x610y e 0x720x dove le cifre variabili identificano il client e lo slave. Il trasferimento vero e proprio ha una lunghezza che, esclusa l'intestazione, deve essere multipla di 0x10, con un minimo di 0x100 byte e un massimo di 0x3FF40, cioe' circa 256 kilobyte. L'intestazione finisce in memoria fra 0x2000000 e 0x20000BF, e il programma occupa da 0x20000C0 a 0x203FFFF.

Da qui il vincolo che sorprende chi arriva dal mondo delle cartucce: gli indirizzi assoluti dentro il programma devono riferirsi a 0x2000000 e non a 0x8000000, perche' il programma non gira dalla cartuccia ma dalla memoria di lavoro. Il trasferimento e' inoltre protetto da trasformazioni XOR e da un checksum ciclico a 16 bit, e dopo ogni trasferimento il master deve attendere che il bit di start si azzeri nel registro di controllo seriale, piu' un ritardo di 36 microsecondi.

Sulla memoria in cui quel programma vive, la descrizione architetturale di Copetti da' le due cifre che contano: la memoria di lavoro interna e' 32 kilobyte a 32 bit, quella esterna 256 kilobyte a 16 bit e fino a sei volte piu' lenta da raggiungere. Un programma multiboot vive nella seconda, e questo spiega perche' i progetti di questo tipo curano la compressione dei dati.

## Il lato che scrive, che non e' quello che si immagina

C'e' un fatto architetturale che [[09-esecuzione-codice]] documenta e che va ripetuto qui, perche' riguarda il lato Game Boy Advance. Il ponte di riferimento non scrive la struttura del Pokemon nel salvataggio di generazione 3: inietta un evento Dono Segreto nella sezione degli script in RAM, e lascia che il gioco stesso depositi il Pokemon e aggiorni il Pokedex chiamando le proprie routine. Chi progetta l'opzione C deve decidere quale delle due strade prendere, e sono decisioni molto diverse: scrivere la struttura richiede padroneggiare ogni campo derivato, iniettare uno script richiede conoscere gli indirizzi delle routine per ciascuna delle quarantotto combinazioni di versione e lingua.

## Lo scambio a caldo, che e' la parte fragile

Il programma multiboot deve leggere e scrivere il salvataggio del gioco di generazione 3, quindi quella cartuccia deve essere inserita. Ma all'accensione la cartuccia inserita era quella di avvio. La soluzione e' scambiarle mentre la console e' accesa e il programma gira in RAM.

Questo funziona perche' il programma non dipende piu' dalla cartuccia, ma non e' privo di rischi: il connettore non e' progettato per l'inserimento a caldo, e la console puo' resettarsi durante l'operazione. Il progetto di riferimento documenta il problema, lo attribuisce anche allo stato delle batterie e offre vie alternative per chi ha una flashcart che permette di evitarlo.

Vale la pena osservare che un reset durante lo scambio non e' catastrofico in se': e' catastrofico se avviene mentre il programma sta scrivendo il salvataggio. Da qui il valore della regola sul backup: l'operazione ha una finestra di rischio reale, e l'unica difesa e' avere una copia.

## Perche' non si emula

Nessun emulatore riproduce l'interazione fra un Game Boy e un Game Boy Advance collegati da un cavo Link con questa dinamica. Il progetto di riferimento lo dichiara e nulla lo contraddice.

Ma la conclusione da trarne e' piu' stretta di come viene spesso riportata, ed e' una precisazione che cambia il piano di lavoro. Cio' che non si emula e' il ponte fra le due console. Il collegamento fra due Game Boy si emula bene, perche' BGB espone il cavo su TCP, quindi il lato protocollo di generazione 1 e 2 e' collaudabile su emulatore, con la riserva spiegata in [[21-collaudo]]: provarlo contro un gioco vero richiede una ROM, e dentro il perimetro quella ROM viene dal dump di una cartuccia propria. E il lato generazione 3, cioe' parser, writer, cifratura e checksum, si collauda contro file di salvataggio senza alcuna console. Solo il passaggio finale, il ponte vero, richiede il ferro.

## Che cosa serve avere in mano

Questa e' la lista che l'handoff di ricerca chiamava discovery hardware, e resta il preliminare a qualsiasi scelta fra le opzioni di [[30-opzioni-implementative]]. Serve sapere quante console Game Boy Advance sono disponibili, perche' due permettono la via piu' semplice al multiboot. Serve sapere se esiste un GameCube o un Wii con homebrew, che e' l'alternativa alla seconda GBA. Serve sapere se c'e' una flashcart e quale, perche' il modello determina se lo scambio a caldo si puo' evitare. Serve un cavo Link del Game Boy Color, non del Game Boy Advance. E serve sapere se c'e' la capacita' di saldare e di programmare microcontrollori, che e' il discriminante per l'opzione basata su hardware intermedio.

## Cosa leggere dopo

[[30-opzioni-implementative]] mette insieme questi vincoli con il costo di sviluppo di ciascuna strada.
