# Studio 01: l'esecuzione di codice come via di generazione, e la domanda sulla legittimità in Home

Questa nota è la prima del track e ne fissa la conoscenza di partenza. È scritta il 2026-08-31 dal materiale che l'utente ha procurato, cioè l'elenco degli strumenti dal canale dedicato di un server di community e un video del 26 agosto 2026, più due verifiche su fonte ufficiale che sono la parte su cui poggia tutto il resto.

L'ordine in cui è scritta non è quello dell'argomento ma quello della decisione: prima la domanda che stabilisce se il track sia percorribile, poi la notizia che cambia il calendario del progetto, poi gli strumenti, e infine la strategia che ne discende. Chi ha poco tempo legga le prime due sezioni.

## 1. La domanda, e la risposta verificata

La domanda è se un esemplare prodotto scrivendo i suoi byte nel salvataggio, tramite esecuzione di codice arbitrario, venga accettato come legittimo da Pokemon Home, e se il tentativo esponga l'account a una sanzione.

La risposta ha tre parti e nessuna delle tre è un sì o un no.

Va premesso un rinvio, perché questa sezione è stata superata in parte. Lo `STUDIO-03-la-risposta-della-comunita-e-le-due-severita.md`, scritto il 2026-09-01 dopo la lettura del server della comunità, stabilisce che i verificatori non sono uno ma tre con severità decrescente, e che la domanda giusta non è se un esemplare passi ma quale dei tre lo esamini. Dove le due note divergono vale quella, e questa resta per il ragionamento che vi conduce.

La prima parte è tecnica e favorevole. I byte di un esemplare di terza generazione prodotti in quel modo possono essere identici a quelli di un esemplare autentico: la struttura è documentata, la cifratura e il checksum sono calcolabili, e il metodo di generazione pseudocasuale è noto evento per evento, come il track delle distribuzioni ha stabilito. Se il dato è coerente, un verificatore che guardi il dato non trova nulla.

La seconda parte è quella che rovescia la prima, e viene dall'autore degli strumenti stessi. Pokemon Home **conserva sul proprio lato l'informazione di quale via un esemplare abbia usato per entrare**. Un esemplare autentico di terza generazione entra attraverso Pokemon Bank; uno che venga dalla versione per console moderna di Rosso Fuoco e Verde Foglia entra per una via diversa. Ne segue, nelle parole della fonte, che anche a parità di dati sottostanti non è garantito che l'esemplare risultante in Home sia un clone indistinguibile da uno passato per Bank. La coerenza del dato non implica la coerenza della storia, e il servizio conosce la storia.

La terza parte è la politica dichiarata, e va citata perché è l'unico elemento non congetturale sul rischio. La verifica del 2026-08-31 sulle pagine ufficiali del titolare del servizio stabilisce che chi risulti impiegare dati alterati può subire la restrizione del gioco in linea, la restrizione delle funzioni di scambio nella versione per dispositivo mobile, e **la sospensione di Pokemon Home nelle versioni per console e per dispositivo mobile**, in forma temporanea o indefinita a discrezione del titolare, senza rimborso. La medesima fonte dichiara un'eccezione che va conosciuta perché delimita il rischio: non vi sono restrizioni per chi possieda dati alterati senza intenzione, per esempio ricevendoli in uno scambio senza saperlo. L'eccezione non copre chi li produce.

Sulla verificabilità pratica la risposta è netta e va scritta come tale: **non è verificabile oggi**. La compatibilità fra la versione per console moderna di quei due giochi e Pokemon Home non esiste ancora, e i controlli che il servizio applicherà a un esemplare proveniente da là non sono noti perché non sono ancora in funzione. Non è nemmeno noto se Home accetterà esemplari di provenienza dichiarata Rubino, Zaffiro o Smeraldo che si trovino dentro un salvataggio di quei due giochi, oppure se rifiuterà combinazioni che il titolare consideri impossibili.

## 2. La notizia che cambia il calendario del progetto

Questa sezione è la ragione per cui il track nasce ora e non dopo, e riguarda tutto il progetto e non solo questo sottoprogetto.

Il 13 agosto 2026 il titolare della serie ha annunciato che le versioni per console moderna di Rosso Fuoco e Verde Foglia **si collegheranno a Pokemon Home a ottobre 2026**, con l'aggiornamento 4.1.0 del servizio. Da quel momento un esemplare di quei giochi potrà entrare in Home direttamente, senza passare da Pokemon Bank. Lo stesso annuncio porta tre dettagli che vale registrare: il trasferimento è a senso unico, cioè un esemplare che lascia quei giochi non può rientrarvi e nessun esemplare di altri giochi può visitarli; la capienza del piano a pagamento sale da seimila a novemila esemplari; e chi completa il registro di quei giochi riceve un Celebi.

La conseguenza per il progetto è grande e va enunciata con precisione. Il progetto aveva registrato la chiusura di Pokemon Bank del 26 febbraio 2027 come la scadenza oltre la quale nessun esemplare anteriore all'ottava generazione può più raggiungere Home. **Per la terza generazione quella affermazione cessa di essere vera** se il nuovo collegamento funziona come annunciato, perché apre una seconda porta che non dipende da Bank. Resta vera per la prima, la seconda, la quarta e la quinta generazione, che non hanno alcun collegamento diretto e per cui la catena passa necessariamente da Bank.

Un secondo fatto viene dalla medesima fonte di quarto livello e conferma ciò che il progetto aveva già stabilito: i due passaggi interni alla catena, cioè dalla terza alla quarta generazione e dalla quarta alla quinta, sono funzioni locali dei giochi stessi e **continueranno a funzionare anche dopo la chiusura di Bank**. Ciò che muore il 26 febbraio 2027 è il solo tratto finale, da Bank a Home.

Ne segue una correzione operativa alla pianificazione: la corsa contro il tempo riguarda gli esemplari che devono attraversare Bank, non tutti. Un esemplare di terza generazione può attendere ottobre e provare la porta nuova; uno di seconda no.

## 3. Il fatto architetturale più importante, che nessuna fonte dice

Questa sezione era un'inferenza del progetto e non una citazione, e la marca va rimossa: il 2026-09-01 la via è stata trovata attribuita al suo autore nel server della comunità, in una forma più semplice di quella ipotizzata qui, perché non richiede lo scambio via rete locale ma la ricostruzione dell'esemplare dentro la riedizione per console. Il dettaglio sta in `STUDIO-03`, sezione 4. Ciò che segue resta come documentazione di come l'inferenza era stata costruita, che è il caso in cui una congettura del progetto si è rivelata corretta e vale conservarne il metodo.

Il progetto possiede già un track dedicato allo scambio fra un calcolatore e la versione per console moderna di Rosso Fuoco e Verde Foglia, attraverso il protocollo di rete locale: è `gba-switch-pokemon-trading/`, che è ricerca conclusa e codice non iniziato. Quel track prende strutture di terza generazione da un calcolatore e le fa entrare nel gioco su console tramite lo scambio, cioè attraverso il meccanismo di gioco previsto. E il progetto ha già registrato che quelle strutture si producono da cartucce proprie con il lettore che sta arrivando.

Componendo i due fatti si ottiene una via che nessuna delle due fonti nomina:

```
cartuccia Game Boy Advance propria
  -> dump del salvataggio con il lettore
  -> estrazione della struttura dell'esemplare
  -> scambio via rete locale verso la versione su console
  -> da ottobre 2026, trasferimento diretto in Pokemon Home
```

Il pregio di quella via, rispetto alla scrittura diretta dei byte, è che **il dato non è generato ma autentico**: viene da una cartuccia posseduta, con la sua storia vera, e il suo ingresso nel gioco su console avviene per scambio, cioè per il meccanismo che il gioco prevede. Resta la medesima incertezza della sezione 1 su ciò che Home registrerà come provenienza, perché anche qui l'ingresso in Home avviene dalla porta nuova e non da Bank; ma la differenza fra un dato autentico consegnato per una via non ufficiale e un dato costruito è la stessa differenza che questo progetto documenta altrove fra coerenza per costruzione e coerenza rispetto ai controlli noti.

Va dichiarato ciò che rende questa via non ancora praticabile, perché sono tre cose e nessuna è piccola. Il lettore di cartucce non è arrivato. Il codice del track dello scambio non è iniziato e la sua praticabilità dipende da una misura sull'adattatore senza fili che non è stata fatta. E il collegamento con Home non esiste fino a ottobre. La via è quindi una ipotesi di lavoro con tre precondizioni, non un piano.

## 4. Che cos'è l'esecuzione di codice arbitrario in questo contesto

Il progetto documenta già la tecnica in `docs/09-esecuzione-codice.md`, dove serve al ponte fra generazioni, quindi qui basta la parte che è propria di questo track.

Nella terza generazione la tecnica sfrutta punti in cui il gioco tratta come indirizzo o come istruzione un dato che l'utente controlla, tipicamente attraverso i nomi delle scatole del deposito, che sono stringhe scritte dal giocatore e che si trovano in memoria in una posizione raggiungibile. La conseguenza che interessa qui è che quelle stringhe diventano un canale di ingresso per codice: si scrive nei nomi delle scatole una sequenza che il gioco esegue, e quella sequenza scrive dove le si dice di scrivere.

Sopra quella primitiva la comunità ha costruito ciò che rende la tecnica utile invece che solo notevole, e la fonte lo chiama scrittore in base 64: un programma che, una volta in funzione, accetta dati codificati in una forma digitabile e li scrive nel salvataggio byte per byte. Da quel momento il problema non è più far eseguire codice ma comporre i byte giusti, che è precisamente il problema che il progetto ha già risolto per altre ragioni, con la referenza dei formati e con il pacchetto software del ponte.

## 5. Gli strumenti della comunità, e la funzione di ciascuno

L'elenco viene dal canale dedicato del server di community indicato dall'utente. Nessuno di questi strumenti è stato eseguito in questa sessione, e per la maggior parte le pagine non sono state aperte: quanto segue è la funzione dichiarata, e l'inventario serve a sapere che cosa esiste e quando serve, non a fidarsi del suo funzionamento.

Sulla generazione del codice da eseguire ci sono i due generatori di E-Sh4rk, uno generale e uno specifico per Rosso Fuoco e Verde Foglia, che producono la sequenza da digitare a partire da ciò che si vuole ottenere. Sono il primo strumento della catena e quello che rende la tecnica accessibile senza scrivere assembly a mano.

Sulla composizione dei dati ci sono tre strumenti di MankeyMite. Il convertitore da esadecimale a base 64 serve allo scrittore descritto nella sezione precedente. Lo strumento che ottiene un oggetto qualunque su Smeraldo converte la richiesta di un oggetto in nomi di scatola da digitare, ed è il caso semplice della medesima tecnica. E il costruttore di esemplari di terza generazione è il più rilevante per questo progetto, perché costruisce il dato completo di un esemplare comprese le vecchie distribuzioni di evento, con le opzioni di generazione legale attive per difetto e con l'avvertenza dichiarata dal suo autore che l'accettazione da parte di Home non è garantita.

Sulle procedure ci sono due guide di allestimento, una per Rosso Fuoco e Verde Foglia nelle versioni non giapponesi prima dei capi dei Quattro, l'altra per Rubino e Zaffiro, più una guida scritta generale che è un indice di rimandi e non un testo, e un archivio che raccoglie codici, guide, domande frequenti e risoluzione dei problemi. Su quest'ultimo va registrata una assenza, perché è significativa: l'archivio non contiene alcuna dichiarazione sulla legittimità degli esemplari prodotti, sulla loro accettazione da parte dei verificatori, né sui rischi per l'account. Tratta la tecnica come problema di implementazione e non di conseguenze.

Sull'ispezione e la correzione ci sono due editor. Il primo è quello di riferimento sui formati di salvataggio di tutte le generazioni e sulle regole di legittimità, che il progetto già registra fra le proprie fonti e che è lo strumento con cui si verifica ciò che si è prodotto. Il secondo è un editor di salvataggi pensato per chi usa i glitch, dello stesso autore dei generatori.

Vale registrare la convergenza con l'altro track, perché cambia le opzioni di entrambi. Il costruttore di esemplari genera anche le vecchie distribuzioni di evento, cioè lo stesso risultato che il track delle distribuzioni persegue ricreando la ROM di distribuzione e inviandola per multiboot su hardware proprio. Le due vie producono lo stesso esemplare per strade opposte: una fa rifare al gioco ciò che il gioco faceva allora, l'altra scrive il risultato. La prima è più lenta e più laboriosa; la seconda non ha la storia. Quale delle due convenga dipende interamente dalla risposta alla domanda della sezione 1, e questo è il modo in cui una domanda aperta governa una scelta di metodo.

## 6. La strategia che ne discende

La conclusione operativa non è mia ma dell'autore delle fonti, e coincide con ciò che il progetto aveva già stabilito per altra via, il che è la migliore conferma disponibile.

Ciò che si può trasferire ora per la via ufficiale, si trasferisce ora. Non si attende alcun aggiramento per gli esemplari che contano e che hanno una strada legittima aperta, perché quella strada ha una data di scadenza e gli aggiramenti hanno un rischio non quantificato. Per il progetto questo significa che la catena dalla terza alla quarta alla quinta generazione e poi a Bank va percorsa nei prossimi diciotto mesi per tutto ciò che esiste su cartuccia, ed è già il passo dichiarato.

Ciò che non si può ottenere per alcuna via legittima è il solo caso in cui questo track ha senso. Gli anni non giocati e gli eventi passati sono quel caso, ed è la ragione per cui il track esiste.

La porta nuova di ottobre 2026 si prova quando esiste, su materiale sacrificabile e non sulla collezione. Il modo prudente di provarla è con un esemplare di nessun valore, verificando che cosa Home accetti, prima di esporvi qualunque cosa a cui si tenga.

E la decisione sull'uso della tecnica va presa esplicitamente, perché il rischio dichiarato non è la perdita dell'esemplare ma la sospensione dell'accesso al servizio che custodisce la collezione. È il medesimo genere di decisione già presa in questo progetto sul token personale di una piattaforma di conversazione, con una differenza che ne cambia il peso: là l'oggetto a rischio era un account di conversazione, qui è il contenitore dell'obiettivo dichiarato del progetto.

## 7. Punti aperti

Se Pokemon Home accetti esemplari prodotti per questa via, e con quali controlli: non verificabile prima di ottobre 2026, ed è la domanda che decide il track.

Se Home accetti esemplari di provenienza dichiarata Rubino, Zaffiro o Smeraldo che si trovino in un salvataggio della versione su console di Rosso Fuoco e Verde Foglia: non noto, e la fonte lo dichiara ignoto.

Che cosa esattamente il servizio conservi come informazione di provenienza, e se sia consultabile dall'utente: la fonte afferma che esiste ma non ne descrive la forma. Il titolo dello strumento di spunta della collezione indicato dall'utente nomina i marchi di origine, che sono la parte visibile di quella informazione, e vale approfondire perché tocca la definizione stessa di collezione completa.

Se la via composta della sezione 3 regga: è un'inferenza del progetto e ha tre precondizioni non soddisfatte.

Se il costruttore di esemplari produca, per le distribuzioni di evento, dati che coincidono con quelli che il track delle distribuzioni ricostruisce dal metodo di generazione: è un confronto fattibile senza hardware, e falsificherebbe o confermerebbe entrambe le vie in un colpo.
