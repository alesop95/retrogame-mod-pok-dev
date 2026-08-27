---
tipo: nota di studio
livello: avanzato
tags: [analisi, teoria-informazione, codici, quantizzazione, probabilita]
up: "[[index]]"
vedi_anche: ["[[03-integrita-checksum]]", "[[04-cifratura-gen3]]", "[[07-conversione-vincoli]]", "[[08-cavo-link]]", "[[11-wireless-locale-e-ponte-switch]]"]
---

# Analisi quantitativa: che cosa dicono i numeri dei meccanismi già descritti

Le note precedenti descrivono i meccanismi e ne spiegano il funzionamento. Questa nota fa una cosa diversa e complementare: li misura. Prende i medesimi meccanismi e ne calcola le grandezze che decidono se funzionano, quanto costano e che cosa perdono, con gli strumenti che si applicherebbero a qualunque sistema di trasmissione e di elaborazione dell'informazione.

La ragione per cui vale la pena farlo non è ornamentale. Una descrizione qualitativa dice che un checksum a 8 bit protegge meno di uno a 16; la misura dice quanto, e quel quanto cambia la decisione su cosa fidarsi. Una descrizione dice che la conversione dell'allenamento perde informazione; il calcolo dice quanti bit, e soprattutto dimostra che la perdita è imposta dal formato di destinazione e non dalla formula scelta, il che sposta la discussione dal terreno dell'implementazione a quello della specifica. Ogni sezione di questa nota chiude su una conseguenza operativa di questo tipo.

Una avvertenza sulla natura di ciò che segue. I numeri sono calcolati e non stimati, e lo script che li produce sta in `tools/analisi-quantitativa.py`, cosicché ciascuno sia riproducibile e correggibile invece di essere una cifra da credere. Dove un valore poggia su un'assunzione, l'assunzione è dichiarata nel punto in cui serve; dove il risultato è una derivazione fatta qui e non una formula pubblicata, è marcato come tale con la stessa disciplina di [[07-conversione-vincoli]].

## Il checksum come codice rilevatore d'errore

Un checksum a *n* bit è un codice rilevatore, e la grandezza che lo caratterizza è la probabilità che un'alterazione del messaggio passi inosservata. Sotto l'assunzione che un'alterazione produca un valore di checksum uniformemente distribuito sui 2ⁿ possibili, quella probabilità è 2⁻ⁿ, ed è un limite che nessuna scelta di algoritmo additivo migliora.

Sui tre casi del progetto le cifre sono queste. Il checksum a 8 bit della generazione 1 lascia passare un'alterazione su 256, cioè con probabilità 3,9 per mille. I checksum a 16 bit della generazione 2 e delle strutture della generazione 3 lasciano passare un'alterazione su 65 536, cioè con probabilità 1,5 per centomila. Il salto fra i due non è di grado ma di ordine di grandezza: duecentocinquantasei volte.

C'è però una proprietà del checksum additivo che questo conto non cattura, e che è più interessante del conto stesso perché individua un intero genere di alterazioni contro cui la protezione è nulla anziché piccola. La somma è commutativa, dunque il checksum è invariante rispetto a qualunque permutazione degli addendi. Le sei parole da 16 bit di una sottostruttura della generazione 3 ammettono 720 riordini, e tutti e 720 producono il medesimo checksum: un blocco le cui parole fossero permutate passerebbe la verifica con certezza, non con probabilità 2⁻¹⁶.

Vale registrare che questa è esattamente la medesima cecità che [[23-prove-eseguite]] attribuisce alla prova di simmetria fra lettura e scrittura, la quale è invariante rispetto a una permutazione di etichette. Le due invarianze hanno la stessa origine, cioè un'operazione che non distingue l'ordine dei propri operandi, e la conseguenza è che le due difese non si coprono a vicenda: né il checksum né la prova di simmetria rileverebbero uno scambio fra due campi della medesima larghezza. È la ragione per cui serve la terza difesa, il confronto con un'implementazione indipendente.

### Perché una somma e non un CRC

La domanda naturale, per chi ha in mente i codici, è perché quei giochi impieghino una somma anziché un CRC[^1], che a pari lunghezza rileva tutti gli errori a burst fino a *n* bit e non è invariante per permutazione. La risposta è il costo di calcolo su quell'hardware, e si può quantificare.

Il checksum principale di Cristallo copre 2 938 byte, dai byte 0x2009 a 0x2B82. Sul processore Sharp LR35902, che opera a 4,194 MHz, un ciclo di somma con caricamento e incremento del puntatore costa dell'ordine di sedici cicli per byte, un CRC realizzato con tabella di 256 voci circa ventiquattro, e un CRC calcolato bit per bit dell'ordine di centotrenta. Ne seguono, per l'intero blocco, circa 11 ms per la somma, 17 ms per il CRC tabellare e 91 ms per quello bit per bit.

I numeri di cicli per byte sono stime d'ordine di grandezza e non conteggi su codice reale, e vanno letti come tali; il rapporto fra i tre, invece, è robusto rispetto all'errore sulla singola stima. La conclusione è che il CRC tabellare non era proibitivo in tempo, ma costava 256 byte di ROM e un algoritmo in più da scrivere e collaudare, mentre quello bit per bit avrebbe introdotto un ritardo percepibile in un'operazione che il giocatore compie continuamente. La somma non è dunque una scelta ingenua: è il punto di un compromesso in cui il costo era tutto da un lato e il beneficio era piccolo, perché il canale contro cui difendersi non era un canale rumoroso ma una batteria che si esaurisce.

## La cifratura della generazione 3 misurata contro il criterio di Shannon

Il capitolo sulla cifratura afferma che il meccanismo della generazione 3 non è sicurezza. L'affermazione si può rendere precisa, e la forma precisa è più forte di quella qualitativa.

Il cifrario è c = m ⊕ k, cioè un cifrario di Vernam. Il criterio di sicurezza perfetta stabilisce che un cifrario di questa forma non rivela alcuna informazione sul messaggio se e solo se la chiave è uniformemente distribuita, indipendente dal messaggio, lunga almeno quanto il messaggio e impiegata una sola volta. Qui il messaggio è di 384 bit, cioè 48 byte, e la chiave è di 32 bit: la condizione sulla lunghezza è violata di un fattore dodici, perché la medesima chiave copre dodici parole consecutive.

Da questa violazione segue un risultato standard e verificabile. Per due parole qualunque del blocco vale c_i ⊕ c_j = m_i ⊕ m_j, perché la chiave si elide: il testo cifrato rivela dunque lo XOR di ogni coppia di parole in chiaro, e le coppie confrontabili sono 66. Ne segue che chi possiede il solo testo cifrato conosce già le differenze fra tutte le parole del blocco, senza conoscere la chiave.

> Da verificare. Il passo successivo è una derivazione fatta qui e non una tecnica riportata da una fonte, e conviene marcarla come tale. La sottostruttura della crescita termina con due byte di riempimento che valgono zero, e quei due byte occupano metà di una parola da 32 bit. Su quella parola vale allora c = m ⊕ k con sedici bit di m noti, dunque sedici bit della chiave si leggono direttamente dal testo cifrato. Poiché i due byte adiacenti, che portano amicizia e bonus ai punti potenza, hanno un'entropia molto bassa, la restante metà della chiave è ricavabile per enumerazione dei pochi valori plausibili. La conseguenza è che la chiave sarebbe recuperabile anche se non fosse scritta in chiaro nella struttura: il fatto che vi sia scritta non è la sola ragione per cui il meccanismo non protegge nulla, ed è il tipo di conclusione a cui si arriva soltanto misurando invece di descrivere.

Sulla permutazione delle sottostrutture il conto è immediato e chiude il discorso. Le ventiquattro permutazioni portano log₂(24) = 4,585 bit di informazione, ma la permutazione è una funzione del valore di personalità, cioè è interamente determinata da un campo che sta in chiaro nella medesima struttura. L'informazione mutua fra la permutazione e il valore di personalità coincide dunque con l'entropia della permutazione, e il contributo della permutazione all'incertezza di chi osserva, dato il valore di personalità, è esattamente nullo.

### La tabella di permutazione è il codice di Lehmer, e lo si dimostra

Il capitolo sulla cifratura riporta la tabella delle ventiquattro permutazioni verbatim dal sorgente, e osserva di passaggio che la sequenza corrisponde all'ordinamento lessicografico. L'osservazione si può dimostrare, e la dimostrazione ha valore pratico perché sostituisce una tabella da trascrivere con un algoritmo da verificare.

Il *codice di Lehmer* di un indice *i* fra 0 e n!-1 si ottiene dalla scomposizione in base fattoriale, cioè i = a₀·(n-1)! + a₁·(n-2)! + … + a_{n-1}·0!, con 0 ≤ a_k ≤ n-1-k. La permutazione di indice *i* nell'ordine lessicografico si costruisce allora prelevando ripetutamente dalla lista degli elementi rimanenti quello in posizione a_k.

Applicato ai quattro elementi nell'ordine G, A, E, M, l'algoritmo riproduce la tabella del gioco su tutti e ventiquattro gli indici, e la verifica è stata condotta esaustivamente e non su un campione. Tre casi per rendere visibile il meccanismo. Per i = 5 la scomposizione è 5 = 0·6 + 2·2 + 1·1, dunque si prende l'elemento in posizione 0 di [G,A,E,M], che è G, poi quello in posizione 2 di [A,E,M], che è M, poi quello in posizione 1 di [A,E], che è E, e resta A: si ottiene GMEA, che è ciò che la tabella riporta. Per i = 12 la scomposizione è 2·6 + 0·2 + 0·1 e si ottiene EGAM. Per i = 23, cioè l'ultimo indice, la scomposizione è 3·6 + 2·2 + 1·1 e si ottiene MEAG.

La conseguenza operativa è quella registrata in [[04-cifratura-gen3]] a proposito dell'implementazione di riferimento, che calcola la permutazione per fattoriali invece di tabularla: le due vie sono equivalenti, e la scelta fra esse non è di correttezza ma di verificabilità. Una tabella si verifica per confronto diretto con la fonte, che è un controllo semplice ma da ripetere per ventiquattro righe; un algoritmo si verifica con una prova esaustiva sui ventiquattro indici, che è un controllo che si scrive una volta e gira in un istante. Questo progetto ha adottato la tabella nella referenza, per fedeltà alla fonte, e la dimostrazione qui sopra come controllo indipendente.

## Il campionamento con rifiuto: quante iterazioni servono davvero

La nota sulla conversione descrive la generazione del valore di personalità come un problema di soddisfacimento di vincoli risolto per campionamento con rifiuto, e osserva che il metodo è inefficiente in teoria e adeguato in pratica. Il conto rende quantitativa quella adeguatezza, e mostra anche un caso in cui l'indipendenza dei vincoli, che si dà per scontata, non vale.

Il numero di iterazioni di un campionamento con rifiuto è una variabile geometrica di parametro *p*, dove *p* è la probabilità che un candidato soddisfi tutti i vincoli insieme. Il valore atteso è 1/p e la deviazione standard è dell'ordine di 1/p: il costo è dunque altamente variabile, e questo è un fatto da conoscere prima di misurare un tempo su una singola esecuzione.

Il calcolo di *p* richiede attenzione all'indipendenza. La natura è il valore di personalità modulo 25, lo slot di abilità è il bit meno significativo, cioè il valore modulo 2, e il sesso confronta il byte meno significativo, cioè il valore modulo 256, con la soglia della specie. Poiché il massimo comune divisore fra 25 e 256 è uno, il teorema cinese del resto garantisce che la natura sia indipendente dalla coppia formata da sesso e abilità. Fra sesso e abilità, invece, l'indipendenza non vale, perché entrambi sono funzioni del medesimo byte: il sesso ne è una soglia e l'abilità la parità, e le due vanno contate congiuntamente.

Per una specie con rapporto di sesso paritario e soglia 127, la probabilità congiunta di una combinazione richiesta di sesso e abilità è di un quarto, e moltiplicata per un venticinquesimo della natura dà p = 0,01, cioè cento iterazioni attese. Per le specie con rapporto sbilanciato il caso peggiore sale a circa 427 iterazioni attese. Per Unown, dove anche la lettera è un vincolo e vale un ventottesimo, la probabilità scende a 3,6 per diecimila e le iterazioni attese diventano 2 800.

La conclusione è che il caso peggiore fra quelli reali richiede alcune migliaia di iterazioni di aritmetica intera, cioè un tempo che resta sotto il millisecondo su qualunque processore coinvolto in questo progetto, compreso quello del Game Boy Advance. Il metodo è dunque adeguato con un margine di tre ordini di grandezza, e la sua sostituzione con una costruzione bit per bit, che [[07-conversione-vincoli]] giudica più fragile, non comprerebbe nulla di misurabile. È il genere di conclusione che una misura permette e una descrizione no: non che il metodo sia accettabile, ma che l'alternativa non abbia alcun vantaggio da opporre alla propria fragilità.

## La lucentezza: probabilità e soddisfacibilità garantita

La condizione di lucentezza della generazione 3 richiede che lo XOR fra identificativo visibile, identificativo segreto e le due metà del valore di personalità sia minore di otto. Per valori uniformi il risultato dello XOR è uniforme sui 65 536 valori a sedici bit, e i valori minori di otto sono otto: la probabilità è dunque 8/65 536, cioè una su 8 192, che coincide con il valore documentato per quella generazione.

Sul grado di libertà individuato in [[07-conversione-vincoli]] il conto dice qualcosa di più forte della semplice esistenza. Lo XOR è una biiezione in ciascuno dei propri argomenti, dunque fissati l'identificativo visibile e il valore di personalità esistono esattamente otto valori dell'identificativo segreto che soddisfano la condizione, e almeno uno esiste sempre. La soddisfacibilità del vincolo di lucentezza non è quindi probabile ma certa, e questa è la proprietà che rende la scelta di quell'implementazione non un espediente fortunato ma una soluzione completa.

## La conversione dell'allenamento come quantizzazione con saturazione

La conversione dalla Stat Experience ai valori di allenamento, derivata in [[07-conversione-vincoli]] nella forma EV = min(252, ⌊√StatExp⌋), è un quantizzatore, e conviene analizzarla come tale perché la sua caratteristica non uniforme spiega dove la perdita si concentra.

I livelli in ingresso sono 65 536 e quelli in uscita 253, dunque l'entropia dell'ingresso è al più sedici bit e quella dell'uscita al più log₂(253) = 7,98 bit. La perdita nominale è di circa otto bit per statistica. Il quantizzatore inverso è StatExp = EV², e l'ampiezza del gradino fra due livelli consecutivi è (k+1)² - k² = 2k+1: vale una unità in fondo alla scala e 503 unità in cima. La risoluzione è dunque finissima in basso e grossolana in alto, che è la forma corretta per una grandezza il cui effetto passa per una radice quadrata, e non è un difetto della formula ma la sua proprietà desiderabile.

La perdita nominale, però, non è la perdita rilevante, e la distinzione è il punto di questa sezione. Il contributo dell'allenamento alla statistica finale satura a 63 punti, cioè assume 64 valori distinti, che sono sei bit. Tutto ciò che si perde oltre quei sei bit è informazione che nessuna statistica osserva, dunque la conversione è esatta rispetto a ciò che il gioco calcola pur essendo lossy rispetto al valore memorizzato. Ne segue anche la sorte dell'intervallo fra 63 504 e 65 535, che è di 2 032 valori, cioè il 3,1 per cento dello spazio di ingresso: quei valori sono tutti indistinguibili nel loro effetto, e la loro perdita non è osservabile.

### Il tetto complessivo, e la dimostrazione che la fedeltà è impossibile

Sul vincolo di somma il conto trasforma un'osservazione in un teorema, e vale condurlo perché sposta la responsabilità dal convertitore al formato.

Lo spazio di partenza è il prodotto di cinque valori a sedici bit, cioè 65 536⁵, che è circa 1,21 × 10²⁴ configurazioni, ottanta bit. Lo spazio di arrivo è l'insieme dei punti a coordinate intere del politopo definito dalle sei coordinate non negative, ciascuna non superiore a 252, con somma non superiore a 510. Contati per inclusione ed esclusione, quei punti sono circa 2,29 × 10¹³, cioè 44,4 bit.

Poiché lo spazio di arrivo è più piccolo di quello di partenza di un fattore 5,3 × 10¹⁰, nessuna funzione dal primo al secondo può essere iniettiva: la perdita di circa 35,6 bit non dipende dalla formula scelta ma è imposta dalla cardinalità della destinazione. Ne segue che la conversione fedele delle statistiche è impossibile in senso stretto, e che ogni implementazione deve scegliere quali configurazioni collassare. La cifra che rende concreto il vincolo è che cinque statistiche al massimo darebbero 1 260 unità contro un tetto di 510, cioè un eccesso del 147 per cento.

La conclusione operativa è quella già enunciata in [[07-conversione-vincoli]], ma qui ha un fondamento diverso: la politica per il caso di sforamento non è un dettaglio implementativo lasciato aperto per pigrizia, è la scelta di una fra molte proiezioni possibili su un insieme che non può contenere il dominio. Chiamarla parametro dello strato di conversione, come fa [[20-architettura-codice]], è la conseguenza corretta di questo conto.

## Il cavo Link come canale, e la lista di correzione come byte stuffing

Il protocollo del cavo si presta a un'analisi da canale di trasmissione, e da quell'analisi emerge la ragione ingegneristica di una scelta che [[08-cavo-link]] descrive come necessaria senza spiegare perché lo sia.

Sulla banda le cifre sono queste. Il clock interno del Game Boy monocromatico è di 8 192 Hz, cioè 1 024 byte al secondo; quello del Color arriva a 524 288 Hz; il clock esterno massimo dichiarato per il monocromatico è di 500 kHz, cioè 62 500 byte al secondo. Il rapporto fra il clock esterno massimo e quello interno è di sessantuno volte, e questa è la misura del guadagno che un dispositivo esterno ottiene per il solo fatto di fornire il clock.

Sul tempo di uno scambio: il blocco di scambio è di 424 byte sul filo e la lista di correzione di 200, per 624 byte complessivi. A clock interno il solo blocco di scambio richiede 414 ms e i due insieme 609 ms, cioè oltre mezzo secondo; a 500 kHz i due insieme richiedono 10 ms. L'efficienza di trama, cioè il rapporto fra i 418 byte di dati utili e i 624 trasmessi, è del 67 per cento.

### Perché una lista a lunghezza fissa e non lo stuffing

Il meccanismo della lista di correzione risolve il problema classico di un canale che riserva alcuni simboli del proprio alfabeto al controllo, e la soluzione usuale a quel problema è il *byte stuffing*, cioè la sostituzione del simbolo riservato con una sequenza di fuga.

Il confronto quantitativo fra le due soluzioni è netto e apparentemente sfavorevole a quella adottata. Con un solo valore riservato su 256 e 418 byte di dati, il numero atteso di occorrenze è 1,63, dunque uno stuffing classico costerebbe in media meno di due byte. La lista costa 200 byte fissi, cioè centoventidue volte l'atteso. Il dimensionamento è inoltre largamente sovrabbondante rispetto al rischio: la probabilità che le occorrenze superino diciotto è già inferiore a 10⁻¹², e la lista ne indicizza fino a duecento.

La ragione per cui la scelta apparentemente peggiore è l'unica ammissibile sta nella natura del canale, e conviene enunciarla come principio perché si applica a qualunque collegamento sincrono. In uno scambio in cui il byte che esce e quello che entra attraversano il medesimo registro, ogni trasferimento è simultaneo e la lunghezza del blocco deve essere concordata prima di cominciare: non esiste alcun canale su cui annunciare una lunghezza variabile, perché annunciarla richiederebbe a sua volta uno scambio di lunghezza concordata. Lo stuffing, che produce un blocco di lunghezza dipendente dal contenuto, è dunque strutturalmente inammissibile, e la lista a lunghezza fissa non è una soluzione costosa ma la sola soluzione. Il costo di 200 byte è il prezzo della sincronia, non un'inefficienza.

Vale aggiungere che il medesimo argomento spiega la divisione della lista in due parti, che [[08-cavo-link]] attribuisce alla collisione fra un indice e il byte di preambolo: gli indici indirizzabili per parte arrivano a 253, mentre i byte da indicizzare sono 418, dunque una parte sola non basterebbe a coprire il blocco nemmeno in assenza della collisione.

## Il wireless locale: canali, cadenza, occupazione

Sul protocollo di rete locale della console moderna alcune scelte descritte in [[11-wireless-locale-e-ponte-switch]] hanno una giustificazione numerica immediata, e riportarla chiude la domanda su perché siano quelle.

I canali impiegati sono il primo, il sesto e l'undicesimo della banda a 2,4 GHz. Poiché i canali sono spaziati di 5 MHz e l'occupazione di banda di una portante è di 22 MHz, due canali sono non sovrapposti quando distano più di quattro posizioni: fra il primo e il sesto la distanza è di 25 MHz, fra il sesto e l'undicesimo di 25 MHz, fra il primo e l'undicesimo di 50 MHz. La terna 1, 6, 11 è dunque la più numerosa fra quelle mutuamente non sovrapposte in quella banda, e la sua scelta non è convenzionale ma forzata.

Sulla cadenza degli annunci, un action frame ogni 100 ms corrisponde a dieci trasmissioni al secondo. Un frame dell'ordine di cento byte occupa 0,8 ms alla velocità di 1 Mbit/s e 0,073 ms a 11 Mbit/s, dunque il ciclo di lavoro dell'annuncio è compreso fra lo 0,8 e lo 0,07 per cento: la scoperta della rete consuma una frazione trascurabile della capacità, che è la proprietà desiderabile per un meccanismo che deve restare attivo mentre il traffico utile scorre.

Sugli indirizzi, la forma 169.254.x.y è il blocco link-local con prefisso di sedici bit, che offre 65 534 indirizzi utilizzabili. La scelta di quel blocco per una rete senza infrastruttura è coerente con la sua definizione, e ha la conseguenza pratica che nessun servizio di assegnazione degli indirizzi è necessario: l'host occupa la prima posizione per convenzione e le altre stazioni ricavano la propria.

## L'automazione: perché su orizzonti lunghi l'errore è certo

L'ultimo conto riguarda il caso di studio dell'automazione, e produce la conseguenza progettuale più forte fra quelle di questa nota.

Il riconoscimento di uno stato per visione artificiale ha una probabilità di errore per fotogramma, chiamiamola *p*. Su una sequenza di *k* fotogrammi, sotto l'assunzione di indipendenza, la probabilità che almeno un fotogramma sia classificato male è 1 - (1-p)^k, che cresce verso l'unità con *k* qualunque sia *p*.

Le cifre rendono il fatto concreto. Una corsa di otto ore a sessanta fotogrammi al secondo osserva 1 728 000 fotogrammi. Con una probabilità di errore per fotogramma di un millesimo, che per un riconoscitore per confronto di immagini è ottimistica, la probabilità di almeno un errore è indistinguibile da uno. Con un centomillesimo resta indistinguibile da uno. Con un decimilionesimo scende a 0,16. Per tenere la probabilità di errore sull'intera corsa sotto l'uno per cento occorrerebbe una probabilità per fotogramma inferiore a 5,8 × 10⁻⁹, cioè un errore ogni 172 milioni di fotogrammi, che nessun riconoscitore di questo tipo raggiunge.

L'assunzione di indipendenza va dichiarata perché è la parte debole del conto: gli errori di un riconoscitore visivo sono in realtà correlati, perché dipendono dalla scena, e la correlazione riduce il numero di eventi indipendenti effettivi. La conclusione non cambia di segno, però, perché la correlazione agisce sul numero effettivo di prove e non sull'andamento della curva.

Ne segue la conseguenza progettuale, che è quella che [[STUDIO-01-architettura-e-perimetro]] enuncia in forma qualitativa dicendo che la verità di quella macchina è statistica: un sistema di questo tipo non può essere progettato per non sbagliare, deve essere progettato per accorgersi di avere sbagliato e per rimediare. La differenza fra le due impostazioni è la presenza o l'assenza di uno stato atteso contro cui confrontarsi periodicamente, ed è il criterio con cui valutare la qualità di un programma di automazione al di là del suo tasso di riconoscimento nominale.

## Che cosa questa nota aggiunge, in una riga

Le note precedenti stabiliscono che i meccanismi funzionano; questa stabilisce entro quali margini, e in tre casi dimostra che un limite attribuito all'implementazione appartiene invece al formato: la perdita nella conversione dell'allenamento, l'inammissibilità dello stuffing su un canale sincrono, e l'inevitabilità dell'errore su un orizzonte lungo. Un limite del formato non si risolve scrivendo codice migliore, si dichiara e si governa con una politica, ed è la ragione per cui riconoscerlo cambia il progetto.

## Cosa leggere dopo

[[03-integrita-checksum]] e [[04-cifratura-gen3]] per i meccanismi che le prime due sezioni misurano, [[07-conversione-vincoli]] per la derivazione della formula che la quinta analizza, e [[08-cavo-link]] per il protocollo di cui la sesta calcola i tempi.

[^1]: *CRC*, Cyclic Redundancy Check - codice rilevatore d'errore fondato sulla divisione polinomiale in aritmetica binaria, che a differenza di una somma rileva con certezza tutti gli errori a raffica non più lunghi del proprio grado.
