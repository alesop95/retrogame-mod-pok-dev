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

Il valore di personalità si riproduce su duecentonove vettori su duecentonove. I valori individuali su duecentonove su duecentonove. Il primo dei due numeri è stato duecentotto per una giornata, e la sezione seguente racconta perché: mancava un ramo dell'algoritmo, non un dato della fonte. Il sesso dell'allenatore su cento vettori su cento, cioè su tutti quelli appartenenti ai sette eventi che il costruttore dichiara usare quella derivazione, e su nessun altro: sugli eventi che usano derivazioni diverse la formula sbaglia con la frequenza del caso, che è la controprova migliore, perché una formula che indovinasse anche là non sarebbe una formula ma una coincidenza.

Un esemplare del corpus non porta il seme e non è confrontabile, ed è quello dell'evento distribuito attraverso il disco per la console domestica, che impiega un generatore diverso: il costruttore lo dichiara e rimanda alla propria ricerca inversa invece di fissare un valore.

## 3. La deviazione, che era il ramo mancante, e l'errore di metodo che l'ha nascosta

Il vettore che per una giornata non si è riprodotto appartiene alla distribuzione del decennale, e il suo scarto era di due unità nella metà bassa del valore di personalità: il seme dichiarato produce un valore che finisce per `0x3B0E`, mentre accanto ad esso è scritto un valore che finisce per `0x3B10`. Accanto a quello scarto stava un secondo fatto, cioè che i valori individuali del medesimo esemplare, calcolati dal medesimo seme, tornavano esatti.

Da quei due fatti questa nota aveva tratto la conclusione sbagliata, e la conclusione era che la voce del corpus fosse internamente incoerente: il seme giusto, il modello giusto, e il valore di personalità scritto accanto impossibile. Il ragionamento era che se i valori individuali tornano allora il seme è confermato, e se il seme è confermato allora ciò che quel seme non produce è errato. La premessa nascosta, mai enunciata perché sembrava non esserci, è che il valore di personalità dipenda dal solo seme.

Non ne dipende. Il confronto con il codice della implementazione di riferimento, eseguito il giorno seguente, ha mostrato che la lucentezza non è un vincolo da soddisfare cercando un seme fortunato ma un ramo dell'algoritmo, e che il ramo a lucentezza negata calcola il valore di personalità nel modo ordinario e poi, se il risultato sarebbe cromatico, gli somma otto e azzera i tre bit meno significativi. Sul vettore in questione il valore ordinario ha i tre bit bassi pari a sei, quindi la mutazione lo sposta di esattamente due, ed essa non consuma estrazioni, quindi i valori individuali restano intatti. Entrambi i fatti che sembravano rendere la voce incoerente sono conseguenze della sola formula che mancava.

La prova non è che ora il vettore torni, perché un modello si può sempre allargare fino a includere un caso. La prova è che la mutazione scatti su un esemplare solo dei duecentonove del corpus, e sia proprio quello: un ramo aggiunto per far tornare un conto avrebbe cambiato molti valori, mentre questo cambia uno.

Resta la lezione, ed è di metodo e non di calcolo. Una deviazione inspiegata è anzitutto un'ipotesi sul proprio modello, non un difetto della fonte, e quando i conti tornano su duecentotto casi su duecentonove la probabilità che sbagli il caso solo è più bassa di quella che sbagli il modello. L'errore più grave, però, non è stato diagnosticare male: è stato scrivere quella diagnosi come una virtù, cioè come il caso deviante che il modello sa spiegare. Un modello non spiega ciò che dichiara incoerente, lo esclude, e chiamare spiegazione una esclusione mette una prova a difesa dell'ignoranza invece che della conoscenza. Il controllo negativo che questa nota si vantava di avere scritto, quello secondo cui riprodurre quel vettore sarebbe stato il segno di un codice piegato, era esattamente un presidio contro la scoperta.

## 4. Gli altri quattro confronti, e i due difetti trovati nel costruttore

Sulla tabella delle ventiquattro permutazioni delle sottostrutture l'accordo è esatto su tutte le righe. Le due derivazioni sono indipendenti, poiché la nostra viene dalla macro del disassemblato del gioco e la loro dal proprio modulo, e l'accordo su una tabella che decide dove si trovano i byte è la conferma più economica che il progetto potesse ottenere.

Sull'inventario delle distribuzioni, congiunto sulla coppia formata dal nome dell'allenatore e dall'identificativo, le chiavi in comune sono trentacinque, l'accordo sul metodo di generazione è su venticinque casi su venticinque confrontabili, e l'accordo sulla derivazione del sesso è su diciannove su diciannove. Va notato un errore di lettura commesso e corretto in corso d'opera, perché è del genere che si ripete: il costruttore tiene il proprio inventario in due posti, un file di moduli e un corpus curato a mano che carica a tempo di esecuzione, e leggerne uno solo produceva sedici assenze che sembravano lacune sue mentre erano lacune nostre.

Sul vocabolario dei metodi il costruttore copre tutto ciò che il nostro catalogo usa tranne uno, cioè il metodo ordinario delle uova di una campagna dei negozi, e non implementa una delle derivazioni del sesso, quella che la fonte stessa dichiara di non verificare con la logica ordinaria. Sono lacune dichiarate e non difetti.

I difetti trovati sono due, e il primo ha una conseguenza operativa immediata.

Il primo sta nella tabella dei caratteri. Il costruttore colloca i trentotto caratteri accentati in un blocco contiguo che va da `0x80` a `0xA9`, e dichiara nel proprio commento di averla tratta dalla documentazione di dominio. Il sorgente del gioco, a cui la gerarchia delle fonti di questo progetto assegna la precedenza e da cui la nostra tabella è generata a un commit fissato, li colloca nella fascia bassa da `0x01` a `0x29`, con i salti che impone dove il byte è occupato da un altro segno, e nella fascia che il costruttore usa colloca i sillabari giapponesi e le cifre. La prova che non dipende dalla nostra fonte è interna al costruttore: la sua stessa tabella assegna a quei byte anche i segni giusti, quindi contiene due caratteri per byte e non è invertibile. La conseguenza pratica è che un soprannome o un nome di allenatore contenente una lettera accentata, scritto con quello strumento, non produce l'accento ma il segno che occupa davvero quel byte. Per il caso di questo progetto la conseguenza è nulla, perché l'allenatore della distribuzione italiana del decennale è composto di sole maiuscole e cifre, e su maiuscole e cifre l'accordo è esatto; ma un soprannome italiano con un accento sarebbe scritto male, e questo è il genere di difetto che si scopre in gioco e non prima.

Il secondo è la voce incoerente della sezione tre.

## 5. La verifica esterna, eseguita il 2026-09-01

Le sezioni precedenti stabiliscono che le formule riproducono un corpus conservato. Questa sezione riporta un esito di grado superiore, perché non è più un confronto fra i nostri numeri e quelli di un archivio ma il giudizio di una implementazione di riferimento su un esemplare che il progetto ha costruito da zero. È il passo che il progetto aveva dichiarato aperto il 2026-08-28.

L'esemplare sottoposto è un Pikachu della distribuzione italiana del decennale, composto da `tools/genera-evento-gen3.py` a partire dal solo seme 0x00009DF6 e dai metadati dell'evento. Il verificatore impiegato è PKHeX nella versione del 26 agosto 2026.

### Che cosa il verificatore ha confermato

Il risultato che conta più di ogni altro è che il verificatore ha ricostruito il seme. Accanto all'esemplare esso dichiara un tipo di valore di personalità della famiglia BACD e un seme di origine pari a 0x00009DF6, cioè esattamente il seme da cui l'esemplare è stato generato e che il file non contiene in alcuna forma. Ne segue che la ricostruzione inversa di quella implementazione, partendo dal solo valore di personalità e dai valori individuali, arriva al medesimo seme da cui noi eravamo partiti: le formule della sezione 1 non sono soltanto compatibili con un archivio, sono le stesse che il riferimento impiega.

Sono inoltre confermati per lettura diretta il livello, i quattro valori individuali che il verificatore mostra, la natura, e le quattro mosse. La natura merita una nota perché non è un campo del dato ma una funzione di esso: il verificatore la dichiara Mite, e il valore di personalità ridotto modulo venticinque vale sedici, che è l'indice di quella natura. Anche l'indice di abilità coincide con il bit meno significativo del valore di personalità, che è la regola ordinaria.

Nessuna obiezione è stata sollevata sui due campi che il rapporto di provenienza del generatore marcava come i più debolmente fondati, cioè il contenitore di cattura e l'esperienza calcolata dalla formula del gruppo di crescita. Il fatto va registrato come informazione e non come conferma definitiva: significa che quei due valori sono compatibili con ciò che il verificatore controlla, non che siano stati verificati sul disassemblato.

### L'unica obiezione, e perché è il risultato migliore

Il verificatore ha contestato un campo solo, con la formula che il contrassegno dell'incontro fatidico non dovrebbe essere attivo.

Quel campo è esattamente quello che il rapporto di provenienza del generatore aveva marcato, prima di qualunque verifica, come internamente contraddittorio nella fonte: il corpus del costruttore dichiara il contrassegno attivo, il suo codice lo disattiva con un caso speciale dedicato a questo evento, e le due parti non concordavano. Il verificatore ha detto quale delle due ha ragione, ed è il codice contro il corpus.

Vale enunciare perché questo è l'esito migliore fra quelli possibili, e non un difetto. Il criterio con cui il generatore è stato costruito, cioè dichiarare la provenienza di ciascun campo insieme al suo grado di verifica, esisteva per una ragione dichiarata: un'obiezione è utile soltanto se si può attribuire. Alla prima corsa l'unica obiezione è caduta sull'unico campo che il rapporto segnalava come non attribuibile a una fonte coerente, e la sua risoluzione non ha richiesto alcuna indagine perché il rapporto aveva già nominato le due parti in conflitto. Se il rapporto non ci fosse stato, la medesima obiezione avrebbe richiesto di rileggere due fonti per capire da dove venisse il valore.

La correzione è ora registrata nel generatore in una tavola che porta accanto a ciascuna voce l'autorità che la impone e la data, cosicché nessun campo si allontani dalla propria fonte in silenzio. È la prima voce di quella tavola.

### Il punto che resta aperto

Il verificatore classifica il valore di personalità come BACD nella variante a seme non ristretto, mentre la tabella di quella medesima implementazione dichiara per questo evento la variante a seme ristretto a sedici bit con anti-lucentezza additiva. Le due cose non sono in contraddizione sul dato, poiché il seme impiegato è di sedici bit e l'esemplare non è cromatico, e la spiegazione più probabile è che la classificazione riporti la variante minima che spiega l'osservazione anziché quella dichiarata dall'evento. Resta però una discrepanza fra ciò che il verificatore riconosce e ciò che la sua stessa tabella prescrive, e finché non è spiegata va tenuta come punto aperto e non come dettaglio.

Va inoltre osservato che il verificatore ha ricondotto l'esemplare a un incontro della famiglia dei doni di evento nominando fra parentesi una specie diversa da quella composta. Il fatto non ha prodotto obiezioni e non è stato indagato; è registrato perché una corrispondenza di incontro che nomina un'altra specie merita di essere capita prima di essere ignorata.

## 6. La derivazione, bit per bit, sul caso del decennale

Le sezioni precedenti enunciano le formule e riportano che tornano. Questa le esegue su un caso, e lo fa in binario, perché su un formato dove i campi condividono le parole la sola forma che non lascia dubbi è la disposizione dei bit. Il caso è il Pikachu della distribuzione italiana del decennale dal seme `0x00009DF6`, cioè l'esemplare che il verificatore esterno ha giudicato.

I numeri che seguono non sono trascritti ma calcolati, e si rifanno con un comando invece di essere creduti: `python tools/genera-evento-gen3.py --derivazione --seme 0x9DF6 --soglia-sesso 127 --ace <percorso> --evento 10ANNI`.

### I cinque stati, e perché si scarta la metà bassa

Il generatore è la ricorrenza `s(n+1) = (0x41C64E6D * s(n) + 0x6073) mod 2^32`. Dal seme si ottengono cinque stati, e di ciascuno il gioco impiega la sola metà alta.

```
s1 = 0xD2A89631   1101001010101000 1001011000110001   metà alta 0xD2A8
s2 = 0xAA714150   1010101001110001 0100000101010000   metà alta 0xAA71
s3 = 0xE7FF8F83   1110011111111111 1000111110000011   metà alta 0xE7FF
s4 = 0xE7DC653A   1110011111011100 0110010100111010   metà alta 0xE7DC
s5 = 0xE48B2625   1110010010001011 0010011000100101   metà alta 0xE48B
```

Che la metà bassa sia inservibile non è una convenzione ma una proprietà di questa famiglia di generatori: il bit di posizione `k` ha periodo `2^(k+1)`, quindi i bit più bassi si ripetono dopo pochissimi passi. Sui primi otto avanzamenti dal medesimo seme si vede a occhio.

```
bit 0: 1 0 1 0 1 0 1 0    periodo 2
bit 1: 0 0 1 1 0 0 1 1    periodo 4
bit 2: 0 0 0 0 1 1 1 1    periodo 8
```

Un generatore i cui bit bassi hanno periodo due non è un generatore difettoso: è un generatore da cui si prende la metà alta, e la struttura del gioco lo fa.

### Il valore di personalità, e l'inversione che è la firma

Le prime due metà alte compongono il valore di personalità, e in un esemplare da evento le due assegnazioni sono scambiate rispetto a un incontro ordinario.

```
A, prima estrazione   = 0xD2A8 = 1101001010101000
B, seconda estrazione = 0xAA71 = 1010101001110001

evento:    (A << 16) | B = 0xD2A8AA71   1101001010101000 1010101001110001
ordinario: (B << 16) | A = 0xAA71D2A8   1010101001110001 1101001010101000
```

Le due composizioni non differiscono soltanto nell'aspetto: poiché natura, sesso, abilità e lucentezza si calcolano tutte da quel valore, esse producono un esemplare diverso in ogni campo derivato. È questa la ragione per cui l'inversione è la firma di una provenienza da evento e non un dettaglio di ordinamento.

### I valori individuali, tre campi da cinque bit per parola

La terza e la quarta metà alta portano tre valori individuali ciascuna, cinque bit per campo a partire dal bit meno significativo. Il bit di posizione quindici resta fuori e non entra in alcun campo.

```
terza estrazione = 0xE7FF
  bit   1 11001 11111 11111
        ^   ^     ^     ^
        |   |     |     bit 0-4   PS            = 11111 = 31
        |   |     bit 5-9         Attacco       = 11111 = 31
        |   bit 10-14             Difesa        = 11001 = 25
        bit 15, inutilizzato, vale 1

quarta estrazione = 0xE7DC
  bit   1 11001 11110 11100
        |   |     |     bit 0-4   Velocità      = 11100 = 28
        |   |     bit 5-9         Att. speciale = 11110 = 30
        |   bit 10-14             Dif. speciale = 11001 = 25
        bit 15, inutilizzato, vale 1
```

Il fatto che il bit quindici valga uno in entrambe le parole e non serva a nulla è precisamente il genere di dettaglio che una ricreazione ignora senza conseguenze e che una lettura deve conoscere per non attribuirgli un significato.

### I quattro campi che non si memorizzano

Natura, abilità e sesso non sono campi del dato: sono funzioni del valore di personalità, e il gioco li ricalcola ogni volta. Ometterli da una ricreazione non è possibile, e sbagliarli non è possibile: discendono.

```
natura  = PID mod 25 = 16          che è l'indice della natura Mite
abilità = PID and 1  = 1

byte basso del PID = 0x71 = 113 = 01110001
soglia di sesso di Pikachu = 127
113 < 127, quindi femmina
```

La lucentezza è la quarta, e si calcola come somma esclusiva di quattro parole da sedici bit: i due identificativi dell'allenatore e le due metà del valore di personalità. L'esemplare è cromatico se il risultato è minore di otto, cioè se i tredici bit alti sono tutti nulli.

```
TID  = 0x1853 = 0001100001010011
SID  = 0x0000 = 0000000000000000
PIDh = 0xD2A8 = 1101001010101000
PIDl = 0xAA71 = 1010101001110001
                ----------------
xor  = 0x608A = 0110000010001010 = 24714

24714 non è minore di 8, quindi non cromatico
```

Il valore ventiquattromilasettecentoquattordici va guardato per quello che dice: la probabilità che quel confronto cada sotto otto è di otto su sessantacinquemilacinquecentotrentasei, cioè uno su ottomilacentonovantadue, che è la probabilità di lucentezza della terza generazione ricavata dalla struttura invece che da una tabella.

### Il sesso dell'allenatore, e il numero cinque

```
quinta estrazione = 0xE48B = 1110010010001011
                                     ^
                                     bit di posizione 7 = 1
1 negato = 0, quindi maschio
```

Due dettagli di questa formula non sono deducibili e vanno fissati. Il numero cinque discende dal fatto che le prime quattro estrazioni sono già consumate, dal valore di personalità e dai valori individuali, quindi la quinta è quella che decide questo campo. E la negazione va conservata così com'è: senza di essa la formula sbaglia esattamente tutti i casi invece di metà, che è il modo in cui un errore di questo genere si nasconde meglio, perché produce un esito sistematico e non casuale e può passare per una convenzione di segno.

## 7. Il secondo giudizio, dopo la correzione

L'esemplare corretto è stato sottoposto di nuovo al verificatore, e il rapporto completo cambia il quadro della sezione 5 in tre punti. Va premesso il contesto, perché due delle sue voci dipendono da esso: il verificatore aveva caricato un salvataggio vuoto di un titolo della nona generazione, quindi ha giudicato un esemplare di terza generazione con i criteri che valgono per quel titolo.

### Che cosa il secondo giudizio conferma

Il contrassegno dell'incontro fatidico non è più contestato: la correzione registrata nella tavola ha funzionato.

La classificazione del metodo è cambiata e ha chiuso il punto che la sezione 5 lasciava aperto. Prima il verificatore dichiarava la variante priva di restrizione sul seme; adesso dichiara esattamente la variante che la sua tabella prescrive per questo evento, cioè seme ristretto a sedici bit con anti-lucentezza additiva. Ne segue che la classificazione precedente non era una discrepanza della tabella ma una conseguenza del campo sbagliato: con il contrassegno errato il verificatore riconduceva l'esemplare a un incontro più generico, e con il campo corretto lo riconduce a quello giusto. Il punto aperto si chiude, e la lezione è che una classificazione riportata da un verificatore descrive l'incontro che esso ha saputo far corrispondere, non una proprietà intrinseca del dato.

Per la medesima ragione si chiude il fatto minore che la sezione 5 registrava come non capito: la corrispondenza di incontro nominava fra parentesi una specie diversa da quella composta, e adesso nomina la specie giusta.

Il seme ricostruito resta identico a quello di partenza.

Sono inoltre dichiarati validi, uno per uno, campi che la sezione 5 non poteva enumerare perché la vista sintetica non li mostrava: il soprannome uguale al nome della specie, il livello non inferiore al livello di incontro, i riconoscimenti tutti contabilizzati, l'abilità corrispondente al proprio indice, la forma e il suo argomento, la corrispondenza fra sesso e valore di personalità, quella fra natura e valore di personalità, e infine il contenitore di cattura, dichiarato corretto per il tipo di incontro.

Quest'ultimo merita una riga a sé perché rovescia una previsione. Il rapporto di provenienza del generatore marcava il contenitore come il campo con la provenienza peggiore fra tutti, poiché il file da cui il valore proviene dichiara nel proprio commento di essere una mappatura provvisoria da confermare. Il verificatore lo dichiara corretto. Il valore era dunque giusto pur venendo da una fonte che si dichiarava incerta, e la conclusione da trarre non è che la fonte fosse affidabile ma che su questo campo ha indovinato: la provenienza dichiarata resta quella, e il campo passa da non verificato a verificato da un giudizio esterno.

### Le due voci che dipendono dal contesto, e non dall'esemplare

Il rapporto dichiara mancante il codice di monitoraggio del deposito in rete, e la voce va letta con attenzione perché è la conferma sperimentale di ciò che gli studi dell'altro track hanno stabilito per testimonianza. Quel codice è il tracciatore: il verificatore lo cerca perché, nel contesto di un titolo della nona generazione, un esemplare originario della terza non può essere arrivato là senza essere transitato dal deposito, e quindi deve portarne uno. Il nostro non lo porta, ed è corretto che non lo porti, perché non è transitato da nulla.

La conseguenza è la più concreta che il progetto abbia ottenuto su quel meccanismo, e va enunciata: il tracciatore non è un campo che si possa lasciare in bianco senza che si noti, perché la sua assenza è essa stessa un'obiezione. Ciò conferma per via strumentale l'affermazione delle due fonti indipendenti secondo cui il tracciatore non è falsificabile, e vi aggiunge il verso opposto, cioè che non è nemmeno omettibile dove il contesto lo richiede. Vale osservare che la voce non sarebbe comparsa in un contesto di terza generazione, dove nessun tracciatore è atteso, e che verificare l'esemplare in quel contesto è il passo che resta.

Il rapporto segnala inoltre come sospetta, e non come non valida, la lingua dell'ultimo allenatore. È della medesima natura: in un titolo della nona generazione un esemplare trasferito porta i campi dell'ultimo allenatore, e il nostro non li ha perché non è stato trasferito da nessuno. Non è un difetto dell'esemplare ma una proprietà del contesto in cui è stato letto.

Va infine registrato un dettaglio che mostra quanto il contesto pesi: le quattro mosse sono dichiarate valide, ma con la motivazione che sono mosse apprese per aumento di livello nel titolo della nona generazione, ai livelli venticinque, trenta, trentacinque e quaranta. Il verificatore le ha validate secondo le regole di quel titolo e non secondo l'insieme fissato dall'evento, e passano perché coincidono. È una validazione che vale meno di quanto sembri, e la sua sostituzione con quella corretta è il secondo motivo per rifare la prova nel contesto giusto.

## 8. Che cosa succede se lo si mette in un salvataggio che parla con la nona generazione

La domanda è dell'utente e va riportata nei suoi termini, perché è la domanda operativa del track e la sua risposta non è quella che la formulazione suggerisce: se genero questo esemplare e lo metto in un salvataggio che parla con la nona generazione, quando il servizio di deposito della console a doppio schermo sarà dismesso non potrò più averlo.

La risposta è che l'operazione descritta non funziona, e non funziona adesso, indipendentemente da qualunque scadenza. La scadenza riguarda una via diversa. Conviene separare le tre cose, perché confonderle porta a temere la data sbagliata.

### Perché scrivere l'esemplare in un salvataggio di nona generazione non funziona

Un esemplare di terza generazione non arriva in un salvataggio di nona generazione per alcuna via di gioco: fra i due non esiste alcun collegamento, e la catena che li congiunge passa necessariamente dal deposito in rete. Scriverlo là dentro con un editor è quindi possibile come operazione sui byte e non è il caso di cui la catena parla: produce un esemplare che si trova in un posto in cui non poteva arrivare.

Che questo sia rilevabile non è una congettura, ed è la parte che il giudizio della sezione 7 ha dimostrato per via strumentale. Il verificatore, leggendo il nostro esemplare nel contesto di un titolo della nona generazione, ha dichiarato mancante il codice di monitoraggio del deposito. Lo ha cercato perché in quel contesto è atteso: un esemplare originario della terza generazione che si trovi là deve avere transitato dal deposito, e transitandovi avrebbe ricevuto quel codice. Il nostro non lo porta ed è corretto che non lo porti, poiché non è transitato da nulla.

Ne segue il punto che chiude la questione. Quel codice non è un campo che si possa completare, perché non è un dato dell'esemplare ma un riferimento a un archivio che sta presso il servizio: le fonti lette il 2026-09-01, due indipendenti fra loro, dichiarano che un identificativo scritto a mano viene rilevato come falso proprio perché il servizio non lo ha mai emesso. E la sezione 7 aggiunge il verso opposto, che nessuna delle due fonti enunciava: non è nemmeno omettibile, perché la sua assenza è essa stessa un'obiezione.

La conclusione va scritta senza attenuazioni. La via che consiste nello scrivere un esemplare di terza generazione dentro un salvataggio di nona generazione è chiusa in entrambi i sensi: con il codice non si può, perché non lo si può fabbricare; senza il codice non si può, perché la sua assenza si vede. Non è una via che scade, è una via che non c'è.

### Le vie che esistono, e la scadenza di ciascuna

L'esemplare va messo dove appartiene, cioè in un salvataggio di terza generazione, e da là esistono due porte verso il deposito in rete. Hanno scadenze diverse, e questo è il punto che la domanda cercava.

La prima è la catena storica, cioè dalla terza alla quarta generazione con il parco di migrazione, dalla quarta alla quinta con il trasferimento senza fili, poi il programma di trasferimento, poi il servizio di deposito, poi il deposito in rete. Di questa catena muore il solo tratto finale, il 26 febbraio 2027: i due passaggi interni sono funzioni locali dei giochi e continuano a operare dopo quella data, come `poke-ace/STUDIO-01` stabilisce. Chi impiega questa via ha quindi una scadenza vera, e riguarda l'ultimo tratto.

La seconda è la porta che si apre a ottobre 2026, cioè il collegamento diretto fra la riedizione per console moderna dei due titoli della terza generazione e il deposito in rete. Non dipende dal servizio in chiusura e non ha, per quanto se ne sappia, alcuna scadenza. Per impiegarla l'esemplare deve trovarsi dentro un salvataggio di quei due titoli, e le due strade per portarvelo sono documentate: ricostruirlo là dentro con l'esecuzione di codice, che è la via attribuita nell'altro track, oppure trasferirvelo per scambio in rete locale, che è il track dello scambio. In entrambi i casi l'esemplare entra nel deposito da una porta vera e riceve un codice di monitoraggio autentico, perché il servizio glielo assegna in quel momento.

### Il campo che rende la seconda porta praticabile o incerta, e che va scelto

Qui il rapporto del verificatore contiene un dettaglio che vale più di quanto sembri, ed è la riga che dichiara il gioco di origine dell'esemplare che abbiamo prodotto: Rubino.

Il valore veniva dal corpus del costruttore, che per questo evento lo propone come valore per difetto e non come vincolo, poiché l'evento non dichiara alcun insieme di giochi ammessi. La scelta però non è indifferente rispetto alla seconda porta, perché quella porta appartiene ai due titoli della riedizione. Un esemplare che dichiari Rubino dovrebbe quindi trovarsi in un salvataggio di quei due, e su quella condizione precisa entrambi gli studi registrano un punto aperto: non è noto se il servizio accetti un esemplare di provenienza dichiarata Rubino, Zaffiro o Smeraldo che si trovi in un salvataggio della riedizione, e la medesima domanda è stata posta nel server della comunità senza ricevere risposta.

Ne discende una mossa che elimina l'incognita invece di aggirarla: dichiarare come gioco di origine uno dei due titoli della riedizione. Il generatore ha adesso l'opzione per farlo, e la variante è stata prodotta. Non è una furbizia sul campo ma la scelta corretta fra valori tutti ammessi dalla fonte: se la porta che si intende usare appartiene a quei due titoli, l'esemplare dichiari quei due titoli.

Resta da verificare che il verificatore accetti la variante, ed è la prova successiva. Se l'accetta, il progetto ha un esemplare compatibile con la porta che esisterà; se la rifiuta, si è appresa una restrizione che il corpus non dichiarava, e la si registra.

### La risposta, in tre righe

Scrivere l'esemplare in un salvataggio di nona generazione non funziona oggi e non funzionerà dopo: non è questione di scadenze.

Metterlo in un salvataggio di terza generazione e usare la catena storica funziona, e ha per scadenza il 26 febbraio 2027 sul tratto finale.

Metterlo in un salvataggio di terza generazione e usare la porta di ottobre 2026 funziona per quanto si sa, non ha scadenza nota, e conviene dichiararvi come gioco di origine uno dei due titoli a cui quella porta appartiene.

Va ripetuto, perché il resto di questa nota tratta un caso di prova e non un oggetto da collezione: l'esemplare in questione è un caso di prova, e la decisione di perimetro sull'impiego di queste vie per la collezione resta aperta e non è presa qui.

## 9. Che cosa questa nota cambia per la scelta fra le due vie

La domanda che ha motivato la verifica era se la ricreazione della distribuzione originale e la scrittura diretta dei byte producano lo stesso esemplare. La risposta è che sui dati concordano: le due parti usano la medesima tabella di permutazione, attribuiscono a ciascun evento il medesimo metodo, e la formula che il progetto ha ora verificato è quella che il corpus del costruttore incorpora. Non esiste un vantaggio tecnico della via lenta sul piano dei valori.

Ne segue che il confronto ha fatto esattamente ciò per cui era stato scelto: ha eliminato una delle due ragioni possibili per preferire la via lenta, e ha lasciato l'altra intatta. Ciò che distingue le due vie non è più un'ipotesi sui dati ma soltanto la provenienza, che è la grandezza su cui il track dell'esecuzione di codice ha già stabilito che il servizio di destinazione tiene un proprio archivio e appone un marchio visibile. La decisione fra le due vie è dunque interamente una decisione di provenienza, e non ha più alcuna componente tecnica su cui rimandarla.

Un guadagno collaterale va registrato perché è del progetto e non della comparazione. Il modulo scritto per la verifica non serve solo a essa: implementa anche la ricerca inversa, cioè l'insieme dei semi a sedici bit che producono un dato valore di personalità e dati valori individuali. La restrizione a sedici bit che molti metodi da evento dichiarano rende quella ricerca esaustiva e non euristica, perché sono sessantacinquemilacinquecentotrentasei possibilità e si percorrono tutte. È lo strumento che servirà quando il lettore arriverà e gli esemplari del decennale saranno estratti dalla cartuccia: da un esemplare autentico si ricaverà il seme che lo ha generato, e quello è il modo di verificare che una ricreazione sia fedele a un originale posseduto invece che soltanto conforme a una tabella.
## 10. Gli eventi dello scostamento, chiusi: quattro rami invece di uno

Il 2026-09-01 il catalogo contava dieci metodi di generazione, di cui il programma sapeva produrre quattro e ne dichiarava sei come scostamenti da colmare. La descrizione era corretta nella conclusione e sbagliata nella causa, e la differenza ha cambiato il costo del lavoro: quei metodi non differivano per un parametro ma per due cose distinte, cioè quale ramo compone il valore di personalità e quale trasformazione subisce il seme prima di entrare nel generatore. Averle separate è ciò che ha permesso di chiuderle quasi tutte in una giornata.

I rami della composizione sono quattro, e l'ordine con cui si scelgono è significativo perché il primo caso è più specifico del secondo.

Il primo si applica alla lucentezza negata sul solo metodo a seme non ristretto, e compone il valore di personalità per somma esclusiva fra l'identificativo e la metà bassa, pescando di nuovo la prima estrazione finché i suoi bit oltre il terzo non sono tutti nulli: un valore in cui lo fossero produrrebbe per costruzione un esemplare cromatico, che è ciò che il ramo deve evitare. È il solo ramo che consuma un numero variabile di estrazioni.

Il secondo si applica alla lucentezza negata in tutti gli altri casi, ed è la composizione invertita seguita dalla mutazione descritta nella sezione 3.

Il terzo si applica alla lucentezza garantita, ed è quello che rende sbagliata la vecchia impostazione. Consuma tre estrazioni e scarta la seconda; la metà alta del valore di personalità è la prima estrazione, la metà bassa è la somma esclusiva fra identificativo e metà alta nei tredici bit superiori, e i tre bit inferiori vengono dalla terza estrazione. Che i tredici bit siano proprio quelli è la definizione di cromatico letta al contrario, poiché la somma esclusiva delle quattro parole sta sotto otto se e solo se quei tredici bit si annullano. La conseguenza pratica è che su un evento a lucentezza garantita nessun seme, con la composizione invertita, produce un valore che il verificatore accetti: la lucentezza si scrive, non si cerca.

Il quarto si applica al metodo delle uova, ed è la composizione ordinaria, cioè quella degli incontri non da evento, seguita da una estrazione consumata e non usata. Di BACD quel metodo porta il nome per comodità di catalogazione e non la sostanza.

Va detto che nessuno dei centoquattro esemplari già prodotti era interessato dall'errore del terzo ramo, perché nel catalogo le voci a lucentezza garantita appartengono tutte a metodi che il programma allora rifiutava. È fortuna e non merito, e per questo la prova che fissa il ramo è un controllo negativo: verifica che con la composizione invertita, su tutti i duecentoquattordici semi ammessi di quel metodo, nessun valore sia cromatico.

## 11. La trasformazione del seme, e la tabella che è una formula

Fra il numero di partenza e la generazione stanno cinque casi, il cui ordine è quello della fonte e non va riordinato.

Quattro voci restringono il seme a un intervallo di duecentoquattordici valori, e la ragione non è arbitraria: quel seme non è un numero qualunque ma la somma delle cifre di un'ora scritta in decimale codificato in binario, letta dall'orologio della cartuccia, quindi il suo massimo è duecentotredici.

Undici voci consultano prima una tabella di otto doni, e il fatto che le rende poco costose è che la tabella non è un elenco di dati ma una funzione aritmetica. Le otto voci hanno peso uguale, cioè centoventicinque su mille, e specie, insieme di mosse e lucentezza si ricavano dividendo il peso estratto: la specie dal quoziente per duecentocinquanta, la presenza della mossa del desiderio dalla parità del quoziente per centoventicinque, e la lucentezza dal resto, che la concede a una sola delle quattro specie e solo quando cade negli ultimi venticinque valori del suo intervallo. Anche l'indice della specie si ottiene per via aritmetica e non da un elenco, perché i quattro identificativi hanno i bit secondo e terzo distinti e in ordine. Il seme che quella tabella accetta viene poi avanzato di due passi, che sono le estrazioni che la consultazione consuma, e da lì si genera: è la ragione per cui un verificatore, per riconoscere questi esemplari, torna indietro di due passi prima di cercare il seme fra gli ammessi.

Una voce fra le undici è un caso a sé e va detto perché sembra un'eccezione e non lo è: per il Jirachi della stella dei desideri tutte le voci della tabella danno il medesimo dono, quindi consultarla è indistinguibile dal saltarla e restano le sole due estrazioni consumate.

Una voce cerca il seme in un elenco di ottantasei valori, e questo è il solo dato di tutta la catena che non discende da una formula: sono i semi che l'organizzatore di quell'evento ha effettivamente distribuito, cioè un fatto storico. Si legge dalla fonte invece di trascriverlo, e se ne esclude quello che la fonte dichiara distribuito in una sola delle sue cinque varianti, perché produrre una variante diversa darebbe un esemplare mai esistito.

Due derivazioni del sesso, infine, non lo derivano ma lo dichiarano, e la fonte tiene comunque il seme coerente con la derivazione, cercandone uno la cui quinta estrazione produca il bit dichiarato. Il presidio serve a un verificatore che ricalcoli: un valore dichiarato che non combaci con quello calcolabile è una contraddizione interna.

## 12. Il collo di bottiglia vero, che non era il generatore

Chiuso lo scostamento sui metodi, il programma è passato da centoquattro esemplari a centoventidue su centosettantatre, e ciò che restava non era più una lacuna del generatore. Due limiti sono rimasti, e sono di natura diversa fra loro.

Il primo era la codifica dei caratteri, e la diagnosi che questo progetto ne aveva dato andava corretta in un punto. La nota precedente affermava che la nostra tabella non mancasse di nulla, coprendo duecentocinquanta byte su duecentocinquantasei con i sei mancanti di controllo, e che servisse una seconda tabella perché il medesimo byte rende un glifo diverso secondo la lingua del gioco. La seconda metà era giusta, la prima fuorviante: è vero che la tabella non ha buchi, ma è la tabella internazionale, e nella direzione che serve a scrivere, cioè dal carattere al byte, essa non contiene i caratteri giapponesi le cui posizioni la versione internazionale assegna a lettere accentate. Non erano due caratteri come la nota diceva ma almeno otto fra quelli osservati, e la prova più netta è che il byte 0x52 rende una sillaba katakana su un gioco giapponese e una sillaba katakana diversa su uno internazionale: non un accento contro una sillaba, ma due sillabe che si scambiano.

Quel limite è stato chiuso lo stesso giorno, estraendo la tabella giapponese dalla fonte invece di trascriverla. La sua provenienza va dichiarata perché è di rango diverso da quella delle altre tabelle del progetto: non viene da un disassemblato, che per questa generazione il progetto possiede nella sola versione internazionale, ma dal codice della implementazione di riferimento. Per questo scopo è la scelta giusta e non un ripiego, e la ragione è che quella è anche la tabella con cui gli esemplari verranno letti quando saranno giudicati: se il verificatore leggerà i nostri byte con la sua tabella, la tabella con cui li scriviamo deve essere la sua.

L'estrazione ha aperto una porta e ne ha chiusa un'altra, e vale registrarlo perché è il genere di conseguenza che si scopre dopo. Con la tabella giusta i nomi giapponesi degli allenatori si scrivono, ma è diventato visibile un difetto che era rimasto coperto: il soprannome che il programma scriveva era il nome inglese della specie, anche sulle voci giapponesi. Un esemplare giapponese con il nome inglese della specie porta un soprannome che il gioco giapponese non avrebbe mai scritto, quindi cinque esemplari fra i centoquattro erano difettosi in un campo che nessuno aveva guardato. La correzione è stata leggere i nomi delle specie nella lingua della voce, e la fonte dichiara anche il fatto che rende la lettura corretta e non approssimata, cioè che nella terza generazione lo spagnolo e l'italiano impiegano i nomi inglesi, cosicché per quelle due lingue la tabella inglese è la tabella giusta e non un ripiego.

Il secondo limite riguarda cinquanta voci su centosettantatre, ed è che sono uova. Per esse il generatore pseudocasuale è pronto e provato, ma un uovo non è un esemplare con un contrassegno in più: il soprannome e la lingua sono imposti dalla sua condizione, e il campo dell'amicizia porta il conto delle incubazioni, che è un dato per specie e che un verificatore controlla. Quel dato il progetto non lo ha ancora estratto, e la sua assenza vale cinquanta voci: è il lavoro singolo più redditizio che resti su questo fronte, e il posto dove si trova è il campo delle incubazioni nella tabella delle statistiche di base del disassemblato.

Resta infine una voce sola che non si tenta e non si tenterà con questa strada, ed è quella distribuita attraverso il canale televisivo: impiega un generatore pseudocasuale differente, quello dei titoli per la console domestica, e per essa il progetto ha già registrato che la via di produzione in volume non è obbligata a essere la nostra.
