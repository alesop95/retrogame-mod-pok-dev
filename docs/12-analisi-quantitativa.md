---
tipo: nota di studio
livello: avanzato
tags: [analisi, teoria-informazione, codici, quantizzazione, probabilita, telecomunicazioni]
up: "[[index]]"
vedi_anche: ["[[03-integrita-checksum]]", "[[04-cifratura-gen3]]", "[[07-conversione-vincoli]]", "[[08-cavo-link]]", "[[11-wireless-locale-e-ponte-switch]]"]
---

# Analisi quantitativa: che cosa dicono i numeri dei meccanismi già descritti

Le note precedenti descrivono i meccanismi e ne spiegano il funzionamento. Questa nota fa una cosa diversa e complementare: li misura. Prende i medesimi meccanismi e ne calcola le grandezze che decidono se funzionano, quanto costano e che cosa perdono, con gli strumenti della teoria dell'informazione, della teoria dei codici e del calcolo delle probabilità che si applicherebbero a qualunque sistema di trasmissione.

La ragione per cui vale la pena farlo non è ornamentale. Una descrizione qualitativa dice che un checksum a 8 bit protegge meno di uno a 16; la misura dice quanto, e quel quanto cambia la decisione su cosa fidarsi. Una descrizione dice che la conversione dell'allenamento perde informazione; il calcolo dice quanti bit, e soprattutto dimostra che la perdita è imposta dal formato di destinazione e non dalla formula scelta, il che sposta la discussione dal terreno dell'implementazione a quello della specifica. In quattro punti di questa nota un limite comunemente attribuito all'implementazione si rivela appartenere al formato o al canale.

Ogni derivazione è condotta per esteso, con i passaggi algebrici esplicitati invece che asseriti, perché un risultato di cui non si vede il passaggio non è verificabile e in questo progetto la verificabilità è il criterio che governa tutto il resto.

Sui riferimenti va detta una cosa che riguarda l'onestà del registro. I concetti impiegati qui hanno una letteratura canonica, e quella letteratura va citata: entropia e informazione mutua vengono da Shannon, la sicurezza perfetta dal suo articolo del 1949, i codici ciclici da Peterson e Brown, la quantizzazione da Gray e Neuhoff, il campionamento con rifiuto da von Neumann e da Devroye, il sistema numerico fattoriale da Knuth, la trasparenza a byte dalla RFC 1662, il ripiegamento del riporto dalla RFC 1071, gli indirizzi link-local dalla RFC 3927, il piano dei canali dallo standard 802.11. Queste voci stanno in un elenco separato dentro `tools/build-source-map.py`, chiamato `RIFERIMENTI_TEORICI`, e finiscono in bibliografia sotto un'intestazione che dichiara la loro natura: sono citate per attribuzione del concetto e non come fonti consultate in sessione. La distinzione non è formale. Se stessero nella tabella `FONTI`, che per ogni voce dichiara se è stata letta, il conteggio delle fonti lette di [[SOURCES]] si gonfierebbe di diciannove voci che nessuno ha aperto. I numeri di pagina non sono riportati dove non sono stati verificati, perché un numero di pagina inventato è esattamente il genere di dettaglio che la regola sull'onestà del contenuto vieta.

Una avvertenza finale sui numeri. Sono calcolati e non stimati, e lo strumento che li produce è `tools/analisi-quantitativa.py`, cosicché ciascuno sia riproducibile e correggibile invece di essere una cifra da credere. Dove un valore poggia su un'assunzione, l'assunzione è dichiarata nel punto in cui serve con la sua conseguenza sull'attendibilità; dove il risultato è una derivazione fatta qui e non una formula pubblicata, è marcato come tale con la stessa disciplina di [[07-conversione-vincoli]].

## Premesse di teoria dell'informazione

Poiché la nota impiega ripetutamente tre grandezze, conviene definirle una volta con le loro proprietà invece di richiamarle in modo implicito.

L'entropia di una variabile aleatoria discreta X su un insieme finito, secondo la definizione di Shannon, è la somma cambiata di segno dei prodotti fra ciascuna probabilità e il suo logaritmo in base due, e si misura in bit.

```
H(X) = - somma su x di p(x) * log2 p(x)
```

Il caso che ricorre più spesso qui è quello uniforme, e vale svolgerne il calcolo perché ne segue la sola formula che poi si usa. Se p(x) = 1/n per ogni x, con n il numero di valori possibili, allora ogni termine della somma vale (1/n) * log2(1/n) = -(1/n) * log2 n, i termini sono n, e il risultato è H(X) = log2 n. Un campo di b bit i cui valori siano equiprobabili porta quindi esattamente b bit di informazione, e questo giustifica l'uso della larghezza in bit come misura di informazione per i campi delle strutture dati descritte in [[DATA-FORMATS_Gen1-Gen2-Gen3]]. La stessa formula fissa anche il limite superiore: qualunque sia la distribuzione, H(X) non supera log2 n, con uguaglianza se e solo se la distribuzione è uniforme.

L'entropia condizionata H(X | Y) misura l'incertezza residua su X quando Y è noto, e l'informazione mutua I(X; Y) = H(X) - H(X | Y) misura quanta incertezza la conoscenza di Y rimuove. La proprietà che questa nota impiega due volte è la seguente: se X è una funzione deterministica di Y, cioè X = f(Y), allora H(X | Y) = 0, perché noto Y la distribuzione di X è concentrata su un solo valore e ogni termine della somma si annulla; ne segue I(X; Y) = H(X), cioè Y determina interamente X.

## Il checksum come codice rilevatore d'errore

### La probabilità di errore non rilevato, e l'assunzione da cui dipende

Sia m il messaggio e s = f(m) il suo checksum, con f a valori in un insieme di 2 alla n elementi. Un'alterazione trasforma m in m diverso da m, e il difetto passa inosservato se e solo se il checksum del messaggio alterato coincide con quello originale. Assumendo che il nuovo checksum sia distribuito uniformemente sui 2 alla n valori possibili e indipendentemente dal precedente, la probabilità di non rilevamento è 2 alla meno n.

L'assunzione di uniformità è la parte da guardare con sospetto, e conviene dichiararne subito il regime di validità. Per alterazioni casuali e indipendenti, come quelle prodotte dal degrado di una memoria, è una buona approssimazione, ed è il regime in cui si colloca il caso d'uso reale, cioè una batteria che si esaurisce. Per alterazioni strutturate l'assunzione è falsa, e la sottosezione seguente esibisce un'intera classe di alterazioni per cui la probabilità di non rilevamento vale esattamente uno invece di 2 alla meno n. La distinzione fra i due regimi è il contributo principale di questa sezione: un codice rilevatore non offre una garanzia uniforme, offre una garanzia media su un modello di errore, e cambiare modello di errore cambia la garanzia.

Sui tre casi del progetto le cifre sono queste. Il checksum a 8 bit della generazione 1 lascia passare un'alterazione con probabilità 1 su 256, cioè 3,9 per mille. I checksum a 16 bit della generazione 2 e delle strutture della generazione 3 la lasciano passare con probabilità 1 su 65 536, cioè 1,5 per centomila. Il rapporto fra i due è 256: il passaggio da 8 a 16 bit non migliora la protezione di un grado ma di due ordini di grandezza, ed è la ragione per cui un dato coperto da 8 bit merita una diffidenza qualitativamente diversa.

### L'invarianza per permutazione, dimostrata

Il checksum di una sottostruttura della generazione 3 è, come [[04-cifratura-gen3]] stabilisce leggendo il sorgente, la somma di sei parole da 16 bit calcolata modulo 2 alla 16. Sia ora una permutazione qualunque dei sei indici. Poiché l'addizione modulo 2 alla 16 è commutativa e associativa, cioè l'insieme dei resti con l'addizione è un gruppo abeliano, il valore di una somma finita non dipende dall'ordine degli addendi, quindi il checksum del blocco permutato coincide con quello del blocco originale.

Il checksum è dunque invariante rispetto a ogni permutazione delle parole. Le permutazioni di sei elementi sono 720, di cui 719 diverse dall'identità: esistono cioè 719 alterazioni distinte del blocco che il checksum non rileva con probabilità uno. Non con probabilità 1 su 65 536: con certezza.

Questa cecità è esattamente la stessa che [[23-prove-eseguite]] attribuisce alla prova di simmetria fra lettura e scrittura, la quale è invariante rispetto a una permutazione di etichette. Le due invarianze hanno la stessa origine formale, cioè un'operazione che non distingue l'ordine dei propri operandi, e la conseguenza pratica è che le due difese non si coprono a vicenda: né il checksum né la prova di simmetria rileverebbero uno scambio fra due campi della stessa larghezza. È la dimostrazione che la terza difesa, cioè il confronto con un'implementazione indipendente, non è ridondante rispetto alle prime due ma copre precisamente ciò che entrambe mancano. Un codice ciclico non ha questa proprietà, perché la sua sindrome dipende dalla posizione dei simboli attraverso la divisione polinomiale, e questa è la differenza sostanziale fra le due famiglie al di là della lunghezza della sindrome.

### Il ripiegamento del riporto, e la sua origine

Il checksum delle sezioni del salvataggio di generazione 3 si calcola sommando parole da 32 bit e ripiegando poi il risultato a 16, sommando la metà alta alla metà bassa. La tecnica non è locale al gioco: è la stessa impiegata dal checksum dei protocolli di rete definito nella RFC 1071, dove la si adotta per due proprietà che vale enunciare perché spiegano la scelta.

La prima è che la somma con ripiegamento è indipendente dall'ordine dei byte con cui si accumula, quindi una macchina big-endian e una little-endian ottengono lo stesso valore senza conversioni. La seconda è che il ripiegamento conserva l'informazione del riporto invece di scartarla: sommando a 32 bit e ripiegando, i riporti che una somma a 16 bit avrebbe perso rientrano nel risultato. Ne segue che il checksum ripiegato non è equivalente a una somma troncata a 16 bit, e che leggere il sorgente era necessario per stabilire quale delle due il gioco impieghi, come [[03-integrita-checksum]] documenta.

### Perché una somma e non un CRC

La domanda naturale, per chi ha in mente i codici, è perché quei giochi impieghino una somma anziché un CRC[^1], che a pari lunghezza rileva tutti gli errori a raffica fino al proprio grado e non è invariante per permutazione. La risposta è il costo di calcolo su quell'hardware, e si può quantificare.

Il checksum principale di Cristallo copre i byte da 0x2009 a 0x2B82, cioè 11138 meno 8201 più 1, che fa 2 938 byte. Sul processore Sharp LR35902, che opera a 4,194304 MHz, un ciclo di somma con caricamento e incremento del puntatore costa dell'ordine di sedici cicli per byte, un CRC realizzato con tabella di 256 voci circa ventiquattro, e un CRC calcolato bit per bit dell'ordine di centotrenta, poiché ogni bit richiede uno scorrimento e uno XOR condizionato. Dividendo i cicli per la frequenza si ottengono circa 11,2 ms per la somma, 16,8 ms per il CRC tabellare e 91,1 ms per quello bit per bit.

I numeri di cicli per byte sono stime d'ordine di grandezza e non conteggi su codice reale, e vanno letti come tali; il rapporto fra i tre, invece, è robusto rispetto all'errore sulla singola stima, perché un errore del venti per cento su ciascuna lascia inalterati l'ordinamento e gli ordini di grandezza. La conclusione è che il CRC tabellare non era proibitivo in tempo, ma costava 256 byte di ROM e un algoritmo in più da scrivere e collaudare, mentre quello bit per bit avrebbe introdotto un ritardo di quasi un decimo di secondo in un'operazione che il giocatore compie continuamente.

La somma non è dunque una scelta ingenua: è il punto di un compromesso in cui il costo stava tutto da un lato e il beneficio era piccolo, perché il canale contro cui difendersi non era un canale rumoroso, dove gli errori a raffica sono il modello dominante e il CRC è progettato per essi, ma una memoria che perde alimentazione, dove il modello di errore è la perdita totale del contenuto e nessun codice la corregge.

## La cifratura della generazione 3 misurata contro il criterio di Shannon

### Il cifrario, il criterio, e la dimostrazione del limite

Il cifrario è la somma bit a bit modulo due fra messaggio e chiave, cioè il cifrario introdotto da Vernam nel 1926. Un cifrario si dice perfettamente sicuro quando l'osservazione del testo cifrato non modifica la distribuzione a posteriori del messaggio.

Il teorema di Shannon del 1949 stabilisce che la sicurezza perfetta richiede uno spazio delle chiavi almeno grande quanto quello dei messaggi. La dimostrazione per assurdo è breve e vale riportarla, perché ne segue direttamente la misura del deficit nel nostro caso. Si supponga che le chiavi siano meno dei messaggi e si fissi un cifrato osservabile. L'insieme dei messaggi compatibili con quel cifrato è l'immagine della decifratura al variare della chiave, e la sua cardinalità è al più quella dello spazio delle chiavi, dunque strettamente minore di quella dei messaggi. Esiste allora almeno un messaggio non compatibile con il cifrato osservato, per il quale la probabilità a posteriori è nulla mentre quella a priori è positiva. Le due differiscono, e la sicurezza perfetta è violata.

### Il deficit, misurato in bit, e la grandezza che non è la stessa cosa

Nel caso della generazione 3 il messaggio è il blocco di 48 byte, cioè 2 alla 384 messaggi possibili, e la chiave è di 32 bit, cioè 2 alla 32 chiavi. Il deficit è la differenza dei logaritmi, cioè 384 meno 32, che fa 352 bit: un fattore 2 alla 352 fra ciò che il criterio richiede e ciò che il formato fornisce.

Vale distinguere questa grandezza da un'altra che le si affianca e che non è la stessa cosa, perché confonderle è facile e una versione precedente di questa nota lo faceva. Il tasso di chiave, cioè il rapporto fra la lunghezza della chiave e quella del messaggio, è 32 su 384, cioè un dodicesimo, e misura quante volte la chiave viene riusata: dodici. Il deficit di entropia misura invece quanto manca alla sicurezza perfetta, e vale 352 bit. La prima grandezza descrive la struttura del cifrario, la seconda la distanza dal criterio: sono numeri diversi che rispondono a domande diverse, e vanno detti entrambi.

### L'attacco per sovrapposizione, in tre passaggi

Siano due parole cifrate con la stessa chiave. Lo XOR fra i due cifrati si sviluppa così: per associatività e commutatività si raccolgono i due termini di chiave; poiché in aritmetica modulo due ogni elemento è il proprio inverso, la chiave in XOR con sé stessa dà zero; poiché lo zero è neutro, resta lo XOR fra i due messaggi in chiaro.

Il testo cifrato rivela dunque lo XOR di ogni coppia di parole in chiaro, e le coppie confrontabili in un blocco di dodici parole sono 12 per 11 diviso 2, cioè 66. Chi possiede il solo testo cifrato conosce già sessantasei relazioni fra le parole del messaggio, senza conoscere la chiave.

> Da verificare. Il passo successivo è una derivazione fatta qui e non una tecnica riportata da una fonte. La sottostruttura della crescita termina con due byte di riempimento che valgono zero, e quei due byte occupano metà di una parola da 32 bit. Su quella parola il cifrato è lo XOR fra messaggio e chiave con sedici bit di messaggio noti e nulli, e poiché lo zero in XOR con un bit restituisce quel bit, quei sedici bit del cifrato sono i corrispondenti sedici bit della chiave: si leggono direttamente, senza alcun calcolo. Poiché i due byte adiacenti, che portano amicizia e bonus ai punti potenza, hanno entropia molto bassa, la restante metà della chiave è ricavabile per enumerazione dei pochi valori plausibili. La conseguenza è che la chiave sarebbe recuperabile anche se non fosse scritta in chiaro nella struttura: il fatto che vi sia scritta non è la sola ragione per cui il meccanismo non protegge nulla, e il difetto è strutturale prima di essere una scelta di collocazione dei campi.

### La permutazione non aggiunge incertezza

Le ventiquattro permutazioni, se equiprobabili, portano log2 di 24, cioè 4,585 bit. La permutazione è però determinata dal valore di personalità modulo 24, cioè è una funzione deterministica di un campo che sta in chiaro nella stessa struttura. Per la proprietà enunciata in apertura, l'entropia condizionata è nulla e l'informazione mutua coincide con l'entropia: il valore di personalità determina interamente la permutazione, e l'incertezza residua di chi osserva la struttura è esattamente zero.

Il contributo della permutazione alla protezione del blocco è dunque nullo, non piccolo. La disuguaglianza di elaborazione dei dati fornisce la formulazione generale del fatto: nessuna trasformazione deterministica di un dato osservabile può aumentare l'incertezza di chi lo osserva.

### La tabella di permutazione è il codice di Lehmer, e lo si dimostra

La rappresentazione impiegata è il sistema numerico fattoriale, la cui corrispondenza con le permutazioni Knuth tratta sotto il nome di tavole di inversione. L'enunciato è che ogni intero i minore di n fattoriale ammette una e una sola rappresentazione come somma dei prodotti fra coefficienti e fattoriali decrescenti, con il k-esimo coefficiente compreso fra zero e n meno uno meno k.

L'unicità si dimostra per conteggio, e il conteggio è istruttivo. Il numero di tuple di coefficienti che rispettano i vincoli è il prodotto del numero di scelte per ciascuna posizione, cioè n per n meno uno per n meno due e così via fino a uno, che è n fattoriale: il primo coefficiente ammette n valori, il secondo n meno uno, e l'ultimo il solo zero. Poiché le tuple sono tante quanti gli interi dell'intervallo, e poiché la mappa dalla tupla all'intero è iniettiva per la divisione euclidea successiva, essa è anche biiettiva.

La costruzione della permutazione procede allora prelevando ripetutamente dalla lista degli elementi rimanenti quello in posizione data dal coefficiente. Applicata ai quattro elementi nell'ordine G, A, E, M, riproduce la tabella del gioco su tutti e ventiquattro gli indici, e la verifica è stata condotta esaustivamente e non su un campione. Tre casi rendono visibile il meccanismo.

Per i = 5 la scomposizione dà i coefficienti 0, 2, 1, 0: si prende l'elemento in posizione 0 di GAEM, che è G; dalla lista rimanente AEM quello in posizione 2, che è M; da AE quello in posizione 1, che è E; resta A. Si ottiene GMEA, che è ciò che la tabella riporta. Per i = 12 la scomposizione è 2 per 6 più 0 per 2 più 0 per 1 e si ottiene EGAM. Per i = 23, cioè l'ultimo indice, la scomposizione è 3 per 6 più 2 per 2 più 1 per 1 e si ottiene MEAG.

La conseguenza operativa riguarda la scelta fra tabulare e calcolare, che [[04-cifratura-gen3]] attribuisce all'implementazione di riferimento. Le due vie sono equivalenti nel risultato, e la scelta fra esse non è di correttezza ma di verificabilità: una tabella si verifica per confronto diretto con la fonte, che è un controllo semplice da ripetere ventiquattro volte, mentre un algoritmo si verifica con una prova esaustiva sui ventiquattro indici, che si scrive una volta e gira in un istante. Il progetto ha adottato la tabella nella referenza, per fedeltà alla fonte, e la dimostrazione qui sopra come controllo indipendente: le due si confermano a vicenda, che è la condizione in cui un dato si può usare senza riserve.

## Il campionamento con rifiuto: quante iterazioni servono davvero

Il metodo, la cui formulazione originale risale a von Neumann e la cui trattazione sistematica sta in Devroye, ha un costo che si deriva in forma chiusa, e il conto individua due punti in cui l'ipotesi che si dà per scontata non vale.

### Il costo, derivato

Il numero di iterazioni fino al primo successo, quando ogni tentativo ha probabilità p di riuscire indipendentemente dagli altri, è una variabile geometrica. Il valore atteso si ricava dalla serie dei prodotti fra n e la probabilità che il primo successo arrivi alla n-esima prova; portando fuori p e riconoscendo la derivata della serie geometrica, cioè che la somma di n per x alla n meno uno vale uno su uno meno x tutto al quadrato, si ottiene che il valore atteso è p per uno su p al quadrato, cioè uno su p.

La varianza è uno meno p diviso p al quadrato, quindi la deviazione standard è la radice di uno meno p diviso p, che per p piccolo vale circa uno su p, cioè lo stesso ordine del valore atteso. Il costo è quindi altamente variabile, e questo è un fatto da conoscere prima di misurare un tempo su una singola esecuzione: una misura isolata non stima nulla, perché la distribuzione ha coda geometrica.

### Il bias del modulo, che nessuna fonte segnala

Il calcolo di p richiede una premessa che l'analisi corrente del progetto aveva trascurato, ed è il tipo di dettaglio che questa nota esiste per esplicitare.

La natura è il valore di personalità modulo 25, con il valore di personalità uniforme sui 2 alla 32 valori. Poiché 25 non divide 2 alla 32, la distribuzione del resto non è esattamente uniforme. La divisione euclidea dà 2 alla 32 uguale a 25 per 171 798 691 più 21, dunque ventuno classi di resto hanno 171 798 692 preimmagini e le restanti quattro ne hanno 171 798 691. La verifica torna: ventuno per 171 798 692 più quattro per 171 798 691 fa esattamente 4 294 967 296.

La probabilità massima è quindi 171 798 692 diviso 2 alla 32, che vale circa 0,0400000000373 contro il valore ideale 0,04, con deviazione relativa di 9,3 per dieci alla meno dieci.

La conclusione è che il bias esiste, è misurabile, e vale un miliardesimo: irrilevante per qualunque scopo pratico, e i conti che seguono usano legittimamente l'ipotesi di uniformità. Vale però averlo calcolato invece che assunto, per due ragioni. La prima è che lo stesso ragionamento su un modulo maggiore, o su un campo più corto, produrrebbe un bias non trascurabile, e chi non ha svolto il conto una volta non sa dove cambia il regime. La seconda è che questo è il difetto che rende non uniformi molti generatori scritti prendendo un modulo di un valore casuale, ed è quindi un errore la cui misura conviene conoscere.

### L'indipendenza, dove vale e dove non vale

I tre vincoli agiscono su tre moduli diversi: la natura è il valore modulo 25, lo slot di abilità è il valore modulo 2, e il sesso confronta il valore modulo 256 con la soglia della specie.

Fra la natura e le altre due l'indipendenza vale, e la ragione è il teorema cinese del resto: poiché 25 e 256 sono coprimi, la mappa che associa a un intero la coppia dei suoi resti è una biiezione, e per un intero uniforme le due componenti sono uniformi e indipendenti, a meno del bias appena quantificato.

Fra il sesso e l'abilità l'indipendenza non vale, e questo è il punto che un calcolo distratto sbaglia. Entrambi sono funzioni dello stesso byte: il sesso ne è una soglia e l'abilità la parità, e le due non si possono moltiplicare, vanno contate congiuntamente enumerando i 256 valori. Per soglia 127, corrispondente al rapporto paritario, i valori maggiori o uguali a 127 sono 129, e fra questi i pari sono 64: la probabilità congiunta è 64 su 256, cioè un quarto, mentre il prodotto delle marginali darebbe 0,2520. Lo scostamento è dell'ordine dell'uno per cento: piccolo, ma è il genere di scostamento che si accumula quando i vincoli aumentano.

### Il risultato

Componendo, la probabilità di accettazione per una specie con rapporto paritario è un venticinquesimo per un quarto, cioè 0,01, e le iterazioni attese sono cento. Per le specie con rapporto sbilanciato il caso peggiore scende a 0,00234, cioè 427 iterazioni attese. Per Unown il vincolo sulla lettera aggiunge un fattore un ventottesimo, la probabilità scende a 3,57 per dieci alla meno quattro e le iterazioni attese diventano 2 800, con deviazione standard dello stesso ordine.

La conclusione è che il caso peggiore fra quelli reali richiede alcune migliaia di iterazioni di aritmetica intera, cioè un tempo che resta sotto il millisecondo su qualunque processore coinvolto in questo progetto, compreso quello del Game Boy Advance. Il metodo è adeguato con un margine di tre ordini di grandezza, e la sua sostituzione con una costruzione bit per bit, che [[07-conversione-vincoli]] giudica più fragile, non comprerebbe nulla di misurabile. È il genere di conclusione che una misura permette e una descrizione no: non che il metodo sia accettabile, ma che l'alternativa non abbia alcun vantaggio da opporre alla propria fragilità.

## La lucentezza: probabilità e soddisfacibilità garantita

La condizione richiede che lo XOR fra identificativo visibile, identificativo segreto e le due metà del valore di personalità sia minore di otto. Poiché lo XOR di variabili indipendenti di cui almeno una è uniforme è uniforme, il risultato è uniforme sui 65 536 valori a 16 bit, e i valori minori di otto sono esattamente otto: la probabilità è 8 su 65 536, cioè una su 8 192, che coincide con il valore documentato per quella generazione. La coincidenza è una verifica indipendente della lettura della formula: se l'avessimo letta male, i due numeri non tornerebbero.

Sul grado di libertà individuato in [[07-conversione-vincoli]] il conto dice qualcosa di più forte della semplice esistenza, e la dimostrazione è immediata. Fissati l'identificativo visibile e il valore di personalità, si ponga t lo XOR dei tre termini noti. La condizione diventa che lo XOR fra identificativo segreto e t sia minore di otto, e poiché la mappa che manda x nello XOR fra x e t è una biiezione, essendo la propria inversa, esistono esattamente otto valori dell'identificativo segreto che la soddisfano. Almeno uno esiste sempre: la soddisfacibilità non è probabile ma certa, e questo rende quella scelta non un espediente fortunato ma una soluzione completa.

## La conversione dell'allenamento come quantizzazione con saturazione

La conversione derivata in [[07-conversione-vincoli]], cioè il minimo fra 252 e la parte intera della radice quadrata della Stat Experience, è un quantizzatore scalare non uniforme con saturazione, e conviene analizzarla con gli strumenti della teoria della quantizzazione perché la sua caratteristica spiega dove la perdita si concentra e perché sia innocua.

### Le regioni, e la verifica che partizionano lo spazio

Un quantizzatore è definito dalle proprie regioni, cioè dagli insiemi di valori d'ingresso che condividono la stessa uscita. Qui la regione di indice k, per k fino a 251, è l'insieme dei valori compresi fra k al quadrato e il quadrato successivo escluso, mentre la regione di saturazione raccoglie tutti i valori da 63 504 in su. L'ampiezza di una regione non satura è la differenza fra i due quadrati consecutivi, cioè 2k più 1, che vale una unità per k uguale a zero e 503 unità per k uguale a 251.

Vale verificare che le regioni partizionino esattamente lo spazio d'ingresso, perché una partizione incompleta significherebbe che qualche valore non ha immagine o ne ha due. La somma delle ampiezze delle regioni non sature è la somma di 2k più 1 per k da zero a 251, che per l'identità elementare vale 252 al quadrato, cioè 63 504. La regione di saturazione contiene 65 536 meno 63 504, cioè 2 032 valori. Il totale è 65 536, che è esattamente lo spazio d'ingresso: la partizione è esatta e ogni valore appartiene a una e una sola regione.

### La perdita nominale e la perdita rilevante

I livelli d'ingresso sono 65 536 e quelli d'uscita 253, dunque per la formula dell'entropia uniforme l'entropia dell'ingresso è al più 16 bit e quella dell'uscita al più log2 di 253, cioè 7,983 bit, con perdita nominale di circa otto bit per statistica.

La perdita nominale non è però la perdita rilevante, e la distinzione è il punto di questa sezione. Il contributo dell'allenamento alla statistica finale satura a 63 punti, cioè assume 64 valori distinti, corrispondenti a sei bit. Tutto ciò che si perde oltre quei sei bit è informazione che nessuna statistica osserva: la conversione è esatta rispetto a ciò che il gioco calcola, pur essendo con perdita rispetto al valore memorizzato. Ne segue anche la sorte dei 2 032 valori della regione di saturazione, cioè il 3,1 per cento dello spazio d'ingresso: sono tutti indistinguibili nel proprio effetto, e la loro perdita non è osservabile.

La forma della caratteristica merita un'ultima osservazione, perché non è un difetto ma una proprietà desiderabile. Poiché il quantizzatore inverso è il quadrato e le regioni si allargano linearmente, la risoluzione è finissima in fondo alla scala e grossolana in cima. È esattamente la distribuzione di risoluzione corretta per una grandezza il cui effetto passa per una radice quadrata: il passo di quantizzazione misurato nell'effetto sulla statistica è approssimativamente costante, che è il criterio con cui si progetta un quantizzatore non uniforme.

### Il tetto complessivo, e la dimostrazione che la fedeltà è impossibile

Lo spazio di partenza è il prodotto di cinque valori a 16 bit, cioè 2 alla 80, che vale circa 1,209 per dieci alla 24: ottanta bit esatti. Lo spazio di arrivo è l'insieme dei punti a coordinate intere del politopo definito da sei coordinate non negative, ciascuna non superiore a 252, con somma non superiore a 510.

La sua cardinalità si conta in tre passi. Primo passo: si trasforma la disuguaglianza in uguaglianza introducendo una variabile di scarto non negativa, cosicché la somma delle sette variabili faccia 510; il numero di soluzioni intere non negative di questa equazione in sette variabili è il coefficiente binomiale di 516 su 6, cioè 25 462 191 460 608. Secondo passo: si sottraggono le soluzioni che violano un tetto individuale, con il principio di inclusione ed esclusione, imponendo che j variabili scelte valgano almeno 253 e sottraendo quindi 253 per j dal totale disponibile. Terzo passo: si svolgono i termini, che sono tre perché il quarto ha argomento negativo e si annulla, ottenendo 25 462 191 460 608 meno 2 603 808 971 946 più 3 150, cioè 22 858 382 491 812, che vale circa 2,286 per dieci alla 13, cioè 44,38 bit.

Poiché lo spazio di arrivo è più piccolo di quello di partenza di un fattore 5,29 per dieci alla 10, nessuna funzione dal primo al secondo può essere iniettiva, per il principio dei cassetti. La perdita di 35,62 bit non dipende dunque dalla formula scelta ma è imposta dalla cardinalità della destinazione: qualunque conversione, presente o futura, deve collassare configurazioni distinte in una sola. La cifra che rende concreto il vincolo è che cinque statistiche al massimo darebbero 1 260 unità contro un tetto di 510, cioè un eccesso del 147 per cento.

La conclusione operativa è quella già enunciata in [[07-conversione-vincoli]], ma qui ha un fondamento diverso: la politica per il caso di sforamento non è un dettaglio implementativo lasciato aperto per pigrizia, è la scelta di una fra molte proiezioni possibili su un insieme che non può contenere il dominio. Chiamarla parametro dello strato di conversione, come fa [[20-architettura-codice]], è la conseguenza corretta di questo conto.

## Il cavo Link come canale, e la lista di correzione come byte stuffing

### Banda, tempi, efficienza

Il collegamento trasmette un bit per colpo di clock, dunque la velocità coincide numericamente con la frequenza, e il tempo per trasmettere L byte è otto L diviso la frequenza. Le tre frequenze rilevanti sono 8 192 Hz per il clock interno del Game Boy monocromatico, 524 288 Hz per quello del Color, e 500 kHz per il massimo clock esterno dichiarato per il monocromatico. Il rapporto fra il clock esterno massimo e quello interno è 61: è la misura del guadagno che un dispositivo esterno ottiene per il solo fatto di fornire il clock, senza alcuna modifica al protocollo, ed è la giustificazione quantitativa dell'osservazione di [[08-cavo-link]] sul vincolo di tempo reale inesistente.

Il blocco di scambio è di 424 byte sul filo e la lista di correzione di 200, per 624 complessivi. A clock interno il solo blocco richiede 414 ms e i due insieme 609 ms, cioè oltre mezzo secondo; a 500 kHz i due insieme richiedono 10 ms. L'efficienza di trama, cioè la frazione di byte trasmessi che porta dati utili, è 418 su 624, cioè il 67 per cento: un terzo della capacità del canale è impiegato dalla struttura del protocollo.

### Perché una lista a lunghezza fissa e non lo stuffing

Il meccanismo risolve il problema classico di un canale che riserva alcuni simboli al controllo, e la soluzione usuale è la trasparenza a byte, cioè la sostituzione del simbolo riservato con una sequenza di fuga, nella forma che la RFC 1662 standardizza per i collegamenti punto a punto.

Il confronto quantitativo è netto e apparentemente sfavorevole alla soluzione adottata. Il numero di occorrenze del byte riservato in n byte indipendenti e uniformi è binomiale di parametri n e un duecentocinquantaseiesimo, che per n uguale a 418 si approssima con una legge di Poisson di parametro 1,633; l'approssimazione è lecita perché l'errore è d'ordine n p al quadrato, cioè lo 0,64 per cento. Uno stuffing classico costerebbe dunque in media meno di due byte, mentre la lista costa 200 byte fissi, cioè centoventidue volte l'atteso. Il dimensionamento è inoltre largamente sovrabbondante rispetto al rischio: la probabilità che le occorrenze superino diciotto è già inferiore a dieci alla meno dodici, mentre la lista ne indicizza fino a duecento.

La ragione per cui la scelta apparentemente peggiore è l'unica ammissibile sta nella natura del canale, e conviene enunciarla come principio perché si applica a qualunque collegamento sincrono. In uno scambio in cui il byte che esce e quello che entra attraversano lo stesso registro, ogni trasferimento è simultaneo e la lunghezza del blocco deve essere concordata prima di cominciare. Lo stuffing produce un blocco di lunghezza dipendente dal contenuto, quindi richiederebbe di comunicare quella lunghezza al ricevente; ma comunicarla richiederebbe a sua volta uno scambio di lunghezza concordata, e la ricorsione non termina. Lo stuffing è dunque strutturalmente inammissibile su questo canale, e la lista a lunghezza fissa non è una soluzione costosa ma la sola soluzione: i 200 byte sono il prezzo della sincronia, non un'inefficienza.

Vale osservare che nei protocolli in cui lo stuffing è impiegato la condizione che manca qui è presente: là la trama è delimitata da un simbolo di apertura e uno di chiusura, e il ricevente scopre la lunghezza leggendo fino al delimitatore. Un canale sincrono a scambio simultaneo non ammette quella scoperta, perché entrambi i lati devono trasmettere lo stesso numero di byte.

Lo stesso argomento spiega infine la divisione della lista in due parti, che [[08-cavo-link]] attribuisce alla collisione fra un indice e il byte di preambolo: gli indici indirizzabili per parte arrivano a 253, mentre i byte da indicizzare sono 418, dunque una parte sola non basterebbe nemmeno in assenza di quella collisione.

## Il wireless locale: canali, cadenza, occupazione

### Il piano dei canali, e perché la terna è forzata

Nella banda a 2,4 GHz le frequenze centrali seguono la relazione 2412 più cinque per k meno uno, in megahertz, quindi il primo canale sta a 2412, il sesto a 2437, l'undicesimo a 2462 e il tredicesimo a 2472. L'occupazione di banda di una portante a spettro espanso è di circa 22 MHz, e due canali si dicono non sovrapposti quando la distanza fra le frequenze centrali è almeno pari alla banda occupata. Fra il primo e il sesto la distanza è 25 MHz, fra il sesto e l'undicesimo 25, fra il primo e l'undicesimo 50: la terna è mutuamente non sovrapposta.

Che sia anche la più numerosa possibile si dimostra con un conteggio. Poiché servono almeno 22 MHz e i canali distano 5 MHz, due canali non sovrapposti differiscono di almeno cinque posizioni. Nell'intervallo dal primo al tredicesimo, ampio 60 MHz, il numero massimo di canali con quella spaziatura è la parte intera di 60 diviso 25, più uno, cioè tre. La scelta della terna non è dunque convenzionale ma forzata dalla geometria dello spettro, e nessun piano alternativo ne ospita quattro.

### Cadenza e ciclo di lavoro

Un action frame ogni 100 ms corrisponde a dieci trasmissioni al secondo. La durata di trasmissione di un frame di cento byte è 0,800 ms a 1 Mbit/s e 0,073 ms a 11 Mbit/s, dunque il ciclo di lavoro dell'annuncio è compreso fra lo 0,80 e lo 0,073 per cento: la scoperta della rete consuma meno dell'uno per cento della capacità, che è la proprietà desiderabile per un meccanismo che deve restare attivo mentre il traffico utile scorre.

### Gli indirizzi

La forma 169.254.x.y è il blocco link-local con prefisso di 16 bit definito dalla RFC 3927, che contiene 65 536 indirizzi, dei quali 65 534 utilizzabili. La scelta di quel blocco per una rete priva di infrastruttura è coerente con la sua definizione, che lo destina esattamente ai collegamenti senza servizio di assegnazione, e ha la conseguenza pratica che nessun servizio di quel tipo è necessario: l'host occupa la prima posizione per convenzione e le altre stazioni ricavano la propria.

## L'automazione come anello di controllo, e perché l'errore è certo

Il sistema è un anello di controllo chiuso su un impianto che non espone alcuna variabile di stato: la grandezza osservata è il fotogramma, l'attuatore emula un controller, e il controllore stima lo stato dall'immagine. La stima ha una probabilità di errore per fotogramma, che chiamiamo p.

Su una sequenza di k fotogrammi, sotto l'assunzione che gli errori siano indipendenti, la probabilità che nessuno sia errato è uno meno p elevato a k, dunque quella di almeno un errore è uno meno quella quantità. Per p piccolo e k p non grande, lo sviluppo al primo ordine dà circa k p, che rende immediato l'ordine di grandezza; per k p grande la probabilità tende a uno esponenzialmente.

Le cifre rendono il fatto concreto. Una corsa di otto ore a sessanta fotogrammi al secondo osserva 1 728 000 fotogrammi. Con p uguale a un millesimo, che per un riconoscitore fondato sul confronto di immagini è ottimistico, k p vale 1 728 e la probabilità è indistinguibile da uno. Con un centomillesimo k p vale 17,3 e resta indistinguibile da uno. Con un decimilionesimo la probabilità scende a 0,159.

Invertendo la formula si ricava il requisito: per tenere la probabilità sotto una soglia, p deve essere minore di uno meno la radice k-esima del complemento della soglia. Per una soglia dell'uno per cento su 1 728 000 fotogrammi questo dà p minore di 5,82 per dieci alla meno nove, cioè un errore ogni 172 milioni di fotogrammi, che nessun riconoscitore di questo tipo raggiunge.

L'assunzione di indipendenza va dichiarata perché è la parte debole del conto: gli errori di un riconoscitore visivo sono in realtà correlati, poiché dipendono dalla scena, e la correlazione riduce il numero di prove indipendenti effettive, cioè sposta il risultato nella direzione favorevole. La conclusione non cambia però di segno, perché la correlazione agisce sul numero effettivo di prove e non sull'andamento della curva: per qualunque riduzione ragionevole, k p resta molto maggiore di uno.

Ne segue la conseguenza progettuale, che è quella che [[STUDIO-01-architettura-e-perimetro]] enuncia in forma qualitativa dicendo che la verità di quella macchina è statistica: un sistema di questo tipo non può essere progettato per non sbagliare, deve essere progettato per accorgersi di avere sbagliato e per rimediare. In termini di anello di controllo, la differenza fra le due impostazioni è la presenza di una verifica periodica dello stato contro un riferimento noto, cioè di un secondo anello più lento che corregge la deriva del primo. È il criterio con cui valutare la qualità di un programma di automazione al di là del suo tasso di riconoscimento nominale, e la sua assenza è un difetto di architettura e non di taratura.

## Che cosa questa nota aggiunge, in una riga

Le note precedenti stabiliscono che i meccanismi funzionano; questa stabilisce entro quali margini, e in quattro casi dimostra che un limite attribuito all'implementazione appartiene invece al formato o al canale: la perdita nella conversione dell'allenamento, imposta dalla cardinalità della destinazione; l'inammissibilità dello stuffing su un canale sincrono, imposta dall'impossibilità di annunciare una lunghezza variabile; la cecità del checksum additivo verso le permutazioni, imposta dalla commutatività della somma; e l'inevitabilità dell'errore su un orizzonte lungo, imposta dalla forma della curva. Un limite del formato non si risolve scrivendo codice migliore, si dichiara e si governa con una politica, ed è la ragione per cui riconoscerlo cambia il progetto e non solo la sua documentazione.

## Cosa leggere dopo

[[03-integrita-checksum]] e [[04-cifratura-gen3]] per i meccanismi che le prime due sezioni misurano, [[07-conversione-vincoli]] per la derivazione della formula che la quinta analizza, e [[08-cavo-link]] per il protocollo di cui la sesta calcola i tempi.

[^1]: *CRC*, Cyclic Redundancy Check - codice rilevatore d'errore fondato sulla divisione polinomiale in aritmetica binaria, che a differenza di una somma rileva con certezza tutti gli errori a raffica non più lunghi del proprio grado e non è invariante per permutazione.
