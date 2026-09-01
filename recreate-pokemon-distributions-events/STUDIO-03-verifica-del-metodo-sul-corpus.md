# Studio 03: la verifica del metodo di generazione su un corpus indipendente

Le due note precedenti hanno stabilito quali eventi sono esistiti e con quale metodo, leggendo la tabella di un'implementazione di riferimento. Restava una lacuna che quelle note non nascondevano: il progetto conosceva i nomi dei metodi e la loro descrizione in prosa, e non aveva mai eseguito una formula per vedere se producesse i numeri giusti. Questa nota chiude quella lacuna, e la chiude con un esito che vale scrivere in apertura: la formula riproduce un corpus di duecentonove esemplari conservati che il progetto non ha contribuito a produrre, con una sola deviazione, la quale è a sua volta spiegata.

Il metodo di questa verifica va dichiarato perché ne qualifica la portata. Il costruttore di esemplari della comunità, registrato fra le fonti e fino a ieri mai aperto, non è un programma compilato ma un albero di moduli serviti come file separati, quindi il suo codice si legge con i nomi originali. Insieme al codice esso porta un corpus di esemplari conservati, ciascuno con il proprio seme di origine accanto al valore di personalità, ai valori individuali e al sesso dell'allenatore di provenienza. Quel corpus è precisamente il banco di prova che mancava: non una descrizione del metodo, ma i suoi esiti su casi reali.

Lo strumento che esegue il confronto è `tools/confronta-ace-builder.py`, che scarica il sorgente sotto `_notes/`, dove non entra in git, e produce cinque confronti. Il modulo che implementa le formule è `pokebridge/eventi.py`, collaudato da `tests/test_eventi.py`.

## 1. La formula, e come è stata trovata

Il valore di personalità e i valori individuali di un esemplare da evento discendono da un seme attraverso il generatore congruenziale lineare della terza generazione, cioè la ricorrenza con moltiplicatore `0x41C64E6D` e incremento `0x6073` modulo due alla trentaduesima, di cui il gioco usa la sola metà alta di ogni stato.

Le formule non sono state assunte dalla prosa delle fonti ma cercate. Si sono enumerate le composizioni plausibili delle prime quattro estrazioni e si è tenuta quella che riproduce il corpus, che è un modo di procedere diverso dal dedurre e più solido, perché un'ipotesi sbagliata non produce un accordo parziale ma un accordo nullo. L'esito è il seguente.

Il valore di personalità è la prima estrazione nella metà alta e la seconda nella metà bassa. È l'inversione rispetto a un incontro ordinario, dove la prima va nella metà bassa, ed è la firma di provenienza da evento che la nota precedente aveva descritto: qui è verificata invece di riportata. La composizione ordinaria, provata sullo stesso corpus, dà accordo su zero vettori su duecentonove, il che è la forma più netta in cui un'ipotesi alternativa può cadere.

I valori individuali vengono dalla terza e dalla quarta estrazione, cinque bit per campo a partire dal bit meno significativo: la terza porta punti vita, attacco e difesa, la quarta velocità, attacco speciale e difesa speciale. Qui l'accordo è su duecentonove vettori su duecentonove, cioè totale, e su questo punto non resta alcuna incertezza.

Il sesso dell'allenatore di provenienza, per la derivazione che le fonti chiamano a scorrimento di sette e che è quella dei novantasette eventi più numerosi del catalogo, si ottiene con cinque avanzamenti dal seme, prendendo poi il bit di posizione sette della metà alta e negandolo. Due dettagli meritano di essere fissati perché non sono deducibili. Il primo è il numero cinque: il sesso è determinato dopo il valore di personalità e i valori individuali, che consumano quattro estrazioni, e la quinta è quella che lo decide. Il secondo è la negazione, senza la quale la formula sbaglia esattamente tutti i casi invece di metà, che è il modo in cui un errore di questo tipo si nasconde meglio.

## 2. L'esito, in numeri

Il valore di personalità si riproduce su duecentotto vettori su duecentonove. I valori individuali su duecentonove su duecentonove. Il sesso dell'allenatore su cento vettori su cento, cioè su tutti quelli appartenenti ai sette eventi che il costruttore dichiara usare quella derivazione, e su nessun altro: sugli eventi che usano derivazioni diverse la formula sbaglia con la frequenza del caso, che è la controprova migliore, perché una formula che indovinasse anche là non sarebbe una formula ma una coincidenza.

Un esemplare del corpus non porta il seme e non è confrontabile, ed è quello dell'evento distribuito attraverso il disco per la console domestica, che impiega un generatore diverso: il costruttore lo dichiara e rimanda alla propria ricerca inversa invece di fissare un valore.

## 3. La deviazione, e perché conta più delle conferme

Il vettore che non si riproduce appartiene alla distribuzione del decennale e il suo scarto è di due unità nella metà bassa del valore di personalità: il seme dichiarato produce un valore che finisce per `0x3B0E`, mentre accanto ad esso è scritto un valore che finisce per `0x3B10`.

Ciò che rende quella deviazione informativa è che i valori individuali del medesimo esemplare, calcolati dal medesimo seme, tornano esatti. Ne segue che il seme non è sbagliato e che il modello non è sbagliato: è sbagliato il valore di personalità scritto accanto, che quel seme non può produrre. La voce del corpus è dunque internamente incoerente, e chi la usasse come preimpostazione otterrebbe un esemplare i cui campi non sono mutuamente coerenti, che è precisamente la condizione che un verificatore di legittimità rileva.

Vale registrare il principio, perché è generale e questo progetto lo aveva già incontrato. Una sola eccezione spiegata vale più di duecentootto conferme, perché un modello che rende conto anche del caso deviante è di natura diversa da un modello che ha avuto fortuna. La prova che lo fissa è un controllo negativo nella suite: se un giorno il codice riproducesse anche quel vettore, non sarebbe un progresso ma il segno che qualcuno lo ha piegato per farlo tornare.

## 4. Gli altri quattro confronti, e i due difetti trovati nel costruttore

Sulla tabella delle ventiquattro permutazioni delle sottostrutture l'accordo è esatto su tutte le righe. Le due derivazioni sono indipendenti, poiché la nostra viene dalla macro del disassemblato del gioco e la loro dal proprio modulo, e l'accordo su una tabella che decide dove si trovano i byte è la conferma più economica che il progetto potesse ottenere.

Sull'inventario delle distribuzioni, congiunto sulla coppia formata dal nome dell'allenatore e dall'identificativo, le chiavi in comune sono trentacinque, l'accordo sul metodo di generazione è su venticinque casi su venticinque confrontabili, e l'accordo sulla derivazione del sesso è su diciannove su diciannove. Va notato un errore di lettura commesso e corretto in corso d'opera, perché è del genere che si ripete: il costruttore tiene il proprio inventario in due posti, un file di moduli e un corpus curato a mano che carica a tempo di esecuzione, e leggerne uno solo produceva sedici assenze che sembravano lacune sue mentre erano lacune nostre.

Sul vocabolario dei metodi il costruttore copre tutto ciò che il nostro catalogo usa tranne uno, cioè il metodo ordinario delle uova di una campagna dei negozi, e non implementa una delle derivazioni del sesso, quella che la fonte stessa dichiara di non verificare con la logica ordinaria. Sono lacune dichiarate e non difetti.

I difetti trovati sono due, e il primo ha una conseguenza operativa immediata.

Il primo sta nella tabella dei caratteri. Il costruttore colloca i trentotto caratteri accentati in un blocco contiguo che va da `0x80` a `0xA9`, e dichiara nel proprio commento di averla tratta dalla documentazione di dominio. Il sorgente del gioco, a cui la gerarchia delle fonti di questo progetto assegna la precedenza e da cui la nostra tabella è generata a un commit fissato, li colloca nella fascia bassa da `0x01` a `0x29`, con i salti che impone dove il byte è occupato da un altro segno, e nella fascia che il costruttore usa colloca i sillabari giapponesi e le cifre. La prova che non dipende dalla nostra fonte è interna al costruttore: la sua stessa tabella assegna a quei byte anche i segni giusti, quindi contiene due caratteri per byte e non è invertibile. La conseguenza pratica è che un soprannome o un nome di allenatore contenente una lettera accentata, scritto con quello strumento, non produce l'accento ma il segno che occupa davvero quel byte. Per il caso di questo progetto la conseguenza è nulla, perché l'allenatore della distribuzione italiana del decennale è composto di sole maiuscole e cifre, e su maiuscole e cifre l'accordo è esatto; ma un soprannome italiano con un accento sarebbe scritto male, e questo è il genere di difetto che si scopre in gioco e non prima.

Il secondo è la voce incoerente della sezione tre.

## 5. Che cosa questa nota cambia per la scelta fra le due vie

La domanda che ha motivato la verifica era se la ricreazione della distribuzione originale e la scrittura diretta dei byte producano lo stesso esemplare. La risposta è che sui dati concordano: le due parti usano la medesima tabella di permutazione, attribuiscono a ciascun evento il medesimo metodo, e la formula che il progetto ha ora verificato è quella che il corpus del costruttore incorpora. Non esiste un vantaggio tecnico della via lenta sul piano dei valori.

Ne segue che il confronto ha fatto esattamente ciò per cui era stato scelto: ha eliminato una delle due ragioni possibili per preferire la via lenta, e ha lasciato l'altra intatta. Ciò che distingue le due vie non è più un'ipotesi sui dati ma soltanto la provenienza, che è la grandezza su cui il track dell'esecuzione di codice ha già stabilito che il servizio di destinazione tiene un proprio archivio e appone un marchio visibile. La decisione fra le due vie è dunque interamente una decisione di provenienza, e non ha più alcuna componente tecnica su cui rimandarla.

Un guadagno collaterale va registrato perché è del progetto e non della comparazione. Il modulo scritto per la verifica non serve solo a essa: implementa anche la ricerca inversa, cioè l'insieme dei semi a sedici bit che producono un dato valore di personalità e dati valori individuali. La restrizione a sedici bit che molti metodi da evento dichiarano rende quella ricerca esaustiva e non euristica, perché sono sessantacinquemilacinquecentotrentasei possibilità e si percorrono tutte. È lo strumento che servirà quando il lettore arriverà e gli esemplari del decennale saranno estratti dalla cartuccia: da un esemplare autentico si ricaverà il seme che lo ha generato, e quello è il modo di verificare che una ricreazione sia fedele a un originale posseduto invece che soltanto conforme a una tabella.
