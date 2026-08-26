# Studio 01: architettura di Pokemon Automation, e il suo perimetro

Prima nota di studio del track, scritta il 2026-08-26 leggendo la documentazione ufficiale del progetto, cioè la pagina principale, la lista dei controller, le domande frequenti e la pagina del programma di base. È uno studio per curiosità e non un piano di costruzione: serve a capire com'è fatta quella macchina, perché è fatta così, e quali sue parti hanno un significato per gli altri track di questo progetto.

## L'idea, detta in una riga

Un computer vede lo schermo della console attraverso una scheda di acquisizione video e agisce sulla console attraverso un controller finto costruito su microcontrollore, quindi prende il posto del giocatore senza che la console sappia di parlare con un programma.

Vale la pena riformularla in termini che a un ingegnere delle telecomunicazioni dicono di più: è un anello di controllo chiuso su un sistema che non espone alcuna interfaccia di stato. La grandezza osservata è il fotogramma video, e in alcuni titoli anche il canale audio; l'attuatore è un dispositivo che parla il protocollo di un controller legittimo; il controllore è un programma sul computer che decide la prossima pressione in funzione di ciò che ha riconosciuto. Non esiste alcun canale di ritorno strutturato: lo stato del gioco non si legge, si stima da un'immagine. Tutta la difficoltà del progetto sta in questo, e non nella pressione dei tasti.

## I tre strati, e cosa costa ciascuno

Lo strato di attuazione è il più documentato e il meno interessante concettualmente, ma è quello che decide se si comincia o no. Il dispositivo emula un controller Nintendo, e le combinazioni supportate sono una tabella con un costo e una difficoltà dichiarati per ciascuna. La via consigliata oggi è un Raspberry Pi Pico W o Pico 2 W in modalità USB, che emula un controller Pro senza fili o un singolo Joy-Con, costa circa otto dollari ed è dichiarata di difficoltà uno su dieci. Seguono l'ESP32, circa dieci dollari e difficoltà tre, che fa la stessa cosa via Bluetooth, e l'ESP32-S3, circa quindici dollari e difficoltà tre, che è la via cablata via USB e viene indicata come la migliore per l'uso continuativo. Le famiglie RP2040 e RP2350 in modalità UART esistono e arrivano a difficoltà dieci, con una nota che vale la pena registrare perché è un problema di elettronica e non di software: sono vulnerabili al power glitching, cioè a disturbi sull'alimentazione. Le schede storiche, Arduino Leonardo e Uno, Teensy 2 e Pro Micro, sono tutte dichiarate dismesse.

Su una console modificata l'attuatore cambia natura: al posto del microcontrollore si usa `sys-botbase`, un modulo di sistema che riceve i comandi dal computer. È l'unico punto in cui il custom firmware compare, e il progetto lo tratta come una comodità e non come un requisito.

Lo strato di percezione è quello dove sta il valore vero. Il riconoscimento avviene per confronto di immagini e per riconoscimento ottico dei caratteri, con pagine di documentazione dedicate a entrambi nella sezione per sviluppatori, e in alcuni titoli anche per riconoscimento audio, per esempio individuando il suono che accompagna un incontro raro. Gli esempi che il progetto porta sono istruttivi perché mostrano il livello di finezza raggiunto: il riconoscimento visivo dell'animazione di scintillio che segnala un Pokemon cromatico, e il riconoscimento acustico dello stesso evento in un titolo dove il segnale visivo non basta.

Lo strato di decisione è un programma per compito, e i compiti sono oltre cento. La struttura del catalogo dice quali giochi sono coperti, e uno di quei nomi riguarda direttamente un altro track di questo progetto: fra i titoli automatizzati compaiono Pokemon Rosso Fuoco e Verde Foglia nella versione per Nintendo Switch, oltre a Let's Go, Spada e Scudo, Diamante Lucente e Perla Splendente, Leggende Arceus, Scarlatto e Violetto, Leggende Z-A e Pokemon Casa.

## Il perimetro, che il progetto dichiara meglio di quanto mi aspettassi

Questa parte va letta con attenzione perché determina se il track può esistere senza contraddire le regole di questo progetto, e la risposta è che il perimetro dichiarato è compatibile.

Il progetto è pensato per console non modificate, e dichiara di non supportare l'accesso alla memoria di gioco o di sistema, né nulla che non si possa fare per via legittima; la formula che usa è che non è un gruppo di hacking e non intende diventarlo. Sul rischio di sospensione dell'account afferma che a oggi non risultano casi di sanzione per l'uso di schede di acquisizione e controller di terze parti. Sulla legalità dei Pokemon ottenuti l'argomento è strutturale e regge: poiché gli ingressi sono gli stessi di una partita manuale, il risultato è indistinguibile da una partita manuale, al contrario di un Pokemon costruito modificando il salvataggio, che può sembrare legittimo e rivelarsi illegale più tardi.

Resta un limite pratico che riguarda questa macchina e va scritto adesso: la piattaforma preferita è Windows su x64, il supporto per macOS su ARM è presente ma in ritardo sulle versioni, e Linux non è ufficialmente supportato, con un problema noto di sfarfallio nell'acquisizione video. Un Raspberry Pi o un tablet al posto del computer sono esplicitamente esclusi, perché l'inferenza sul video è costosa e richiede una macchina potente.

## Che cosa questo track condivide davvero con gli altri, e che cosa no

La sovrapposizione con il ponte fra generazioni è il microcontrollore, e va misurata per non illudersi. Qui il microcontrollore emula un controller e parla un protocollo documentato dalla community su un bus USB o Bluetooth, mentre nell'opzione D del ponte dovrebbe generare il clock di un collegamento seriale e rispettare temporizzazioni a livello di bit. Il codice non si riusa e nemmeno la libreria; si riusa l'esperienza di allestimento, cioè saper compilare e caricare un firmware, saper diagnosticare un dispositivo che non viene riconosciuto, e sapere che l'alimentazione è una variabile e non una costante, cosa che la nota sul power glitching rende esplicita.

La sovrapposizione con lo scambio fra GBA e Switch è più concreta di quanto avessi scritto nella scheda, e questa nota la corregge. Non è solo la piattaforma: quel progetto automatizza anche Rosso Fuoco e Verde Foglia su Switch, che è esattamente il gioco al centro del track LDN. Ne segue una domanda che vale la pena porre, e che ho registrato fra le pendenze: i loro programmi per quel titolo toccano lo scambio locale, e in tal caso come riconoscono lo stato della schermata di scambio, oppure si limitano alle parti in singolo giocatore.

C'è infine una differenza di metodo che merita di essere detta, perché è la ragione per cui questo track è interessante e non solo curioso. Tutto il resto di questo progetto lavora a scatola aperta: legge i disassemblati, calcola i checksum, decifra le strutture, e la sua verità è il sorgente. Questa macchina lavora a scatola chiusa: non apre nulla, osserva l'uscita e agisce sull'ingresso, e la sua verità è statistica, cioè un riconoscimento che funziona nella grande maggioranza dei fotogrammi. Sono i due approcci classici al reverse engineering di un sistema, e vederli accanto sullo stesso dominio è un buon esercizio: dove il sorgente esiste conviene la prima via, dove non esiste, come sui titoli recenti, resta solo la seconda.

## Cosa studiare dopo, in ordine

Le pagine per sviluppatori su confronto di immagini e riconoscimento ottico dei caratteri, che sono la parte trasferibile a qualunque altro dominio e l'unica capacità che questo progetto non ha in nessun altro track. Poi la pagina sul power glitching, per capire se descrive un problema di alimentazione del microcontrollore o una tecnica deliberata. Poi la lista dei programmi per Rosso Fuoco e Verde Foglia su Switch, per rispondere alla domanda sullo scambio locale. Il codice del framework resta l'ultimo passo, ed è quello dove serve una decisione di scopo prima di investire: è un programma C++ con Qt di dimensioni non piccole, e leggerlo per curiosità non è lo stesso che leggerlo per contribuire.

## Dove sta il resto

| Cosa cerchi | Dove sta |
|---|---|
| la fonte, con abstract e relazioni | `docs/fonti/pokemon-automation.md` |
| lo stato del track e le tre letture possibili | `.claude/context/sub-poke-automation.md` |
| le domande aperte e le pendenze | `.claude/memory/pending.md` |
| il confronto fra le opzioni del ponte, dove il microcontrollore è l'opzione D | `docs/30-opzioni-implementative.md` |
