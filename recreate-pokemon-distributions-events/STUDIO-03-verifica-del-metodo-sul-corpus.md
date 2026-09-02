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

Sono inoltre confermati per lettura diretta il livello, i quattro valori individuali che il verificatore mostra, la natura, e le quattro mosse. La natura merita una nota perché non è un campo del dato ma una funzione di esso: il verificatore la dichiara Mite, e il valore di personalità ridotto modulo venticinque vale sedici, che è l'indice di quella natura.

Una frase che stava qui è stata rimossa il 2026-09-02 e la rimozione va dichiarata, perché era un errore di metodo e non di contenuto. Essa affermava che anche l'indice di abilità risultava confermato, coincidendo con il bit meno significativo del valore di personalità secondo la regola ordinaria. Il verificatore non ha confermato nulla di simile: non ha detto niente su quel campo, e da un silenzio era stata ricavata una conferma. La sezione 15 racconta che quella regola è sbagliata su questa specie, che il campo era in effetti errato, e che il silenzio andava trattato come un'assenza di informazione.

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
## 13. Come si sottopone un esemplare, e l'errore che sembra un difetto del file

Sottoporre un esemplare al verificatore richiede che nel programma sia caricato un salvataggio della generazione giusta, e ometterlo produce un messaggio che accusa il file. Il caso è stato osservato il 2026-09-02 aprendo i primi due esemplari del lotto: il programma ha risposto che si trattava del caricamento di una tipologia o grandezza di file non supportata, e che il Pokemon poteva essere di una generazione diversa non supportata dal salvataggio corrente, oppure il file poteva essere corrotto. La barra del titolo dichiarava un salvataggio vuoto di nona generazione.

Il messaggio nomina due cause e non sa distinguerle, e vale registrare come si è stabilito quale delle due fosse, perché il metodo è generale: si è letto il codice che lo emette invece di interpretare il testo. La sequenza è che il programma classifica il file per dimensione, e ottanta byte è la dimensione dichiarata di un esemplare immagazzinato di terza generazione, quindi il file viene riconosciuto; poi tenta di convertirlo nel tipo del salvataggio caricato, e la conversione da terza a nona generazione non esiste; la conversione restituisce nulla, il caricamento riferisce di non avere gestito il file, e la funzione che sceglie il messaggio, non trovando una estensione di salvataggio nel percorso, sceglie proprio quella dicitura. Il file non è mai stato messo in dubbio da alcun controllo di integrità.

Che i file siano integri è stato verificato a parte, e in modo indipendente dal programma: sui centoventidue esemplari prodotti si sono ricalcolate le tre cose che il verificatore controlla per accettare il file, cioè la dimensione di ottanta byte, il contrassegno di presenza nel byte a 0x13 e la somma di controllo a sedici bit sui byte da 0x20 a 0x50, e nessuno dei tre diverge in nessun file. Vale annotare perché la somma di controllo torna in entrambe le forme del dato, cioè sia permutata e cifrata sia decifrata a ordine fisso: la permutazione sposta blocchi di dodici byte, che sono un numero intero di parole da sedici bit, e una somma è indifferente all'ordine degli addendi.

Il modo di caricare il contesto giusto è uno di due, e il primo è preferibile perché non chiede di scegliere nulla. Se il file viene passato al programma all'avvio, cioè trascinandolo sull'eseguibile o aprendolo con esso, il programma costruisce da sé un salvataggio vuoto della generazione dell'esemplare, ricavando la versione dal contesto del file e prendendo perfino il nome dell'allenatore e la lingua da quelli scritti nel file. Il secondo è cambiare la versione predefinita del salvataggio vuoto nelle impostazioni di avvio, e ha un dettaglio che vale conoscere perché evita un riavvio inutile: alla chiusura della finestra delle impostazioni il programma ricarica immediatamente il salvataggio vuoto nella versione appena scelta.

Un ultimo punto riguarda ciò che quel caricamento fallito ha comunque insegnato, e vale come esempio del fatto che un tentativo interrotto non è un tentativo inutile. Guardando quale file l'utente aveva aperto è emerso che l'esemplare dell'evento del desiderio uscivamo senza il suo oggetto tenuto. Il generatore contava già l'estrazione dedicata a quell'oggetto, perché senza contarla avrebbe letto il sesso dell'allenatore nella posizione sbagliata, ma ne buttava il valore. La formula che sceglie fra le due bacche è la medesima riduzione a un bit della derivazione del sesso per divisione per tre, applicata a un altro campo, e ora l'oggetto viene scritto. Non era un campo vincolato, quindi il verificatore probabilmente non lo avrebbe contestato: era una differenza dall'originale, che è una cosa peggiore da lasciare in piedi in una collezione che vuole essere fedele.
## 14. Il secondo esemplare sottoposto, e il seme che il verificatore ha ritrovato in un elenco

Il 2026-09-02, caricato il contesto nel modo che la sezione precedente descrive, il verificatore ha aperto il primo esemplare del lotto e lo ha dichiarato conforme. È il secondo esemplare che questo progetto sottopone e il primo prodotto dal lotto, ed è stato scelto dal caso e non dalla convenienza, essendo semplicemente il primo in ordine alfabetico.

Il primo fatto da registrare non riguarda l'esemplare ma il programma, e conferma per osservazione ciò che la sezione precedente aveva ricavato dal codice. Ricevuto il file all'avvio, il verificatore ha costruito un salvataggio vuoto di terza generazione nella versione Smeraldo e ne ha intestato l'allenatore a MYSTRY, che è il nome scritto dentro il file: il contesto non è stato scelto da chi provava ma ricavato dall'esemplare stesso.

Il secondo fatto è il giudizio, e vale enumerare che cosa esso copre, perché un contrassegno verde dice poco se non si sa che cosa abbia attraversato. Il verificatore ha riconosciuto l'incontro come dono di evento della specie giusta, ha collocato il luogo di provenienza fra le occasioni speciali, e ha classificato il valore di personalità come appartenente al metodo a elenco di semi, che è uno dei metodi implementati quel medesimo giorno. Accanto ha dichiarato il seme di origine, e il seme dichiarato è il secondo dell'elenco degli ottantasei che questo progetto ha estratto dalla fonte poche ore prima: il verificatore, partendo dal solo valore di personalità e dai valori individuali, ha ricostruito per via inversa un numero che nel file non è scritto in alcuna forma, e lo ha ritrovato nell'elenco.

Il terzo fatto è che il confronto campo per campo con ciò che il nostro codice ha scritto non mostra alcuna divergenza: valore di personalità, natura derivata dal suo resto per venticinque, numero della abilità dal suo bit meno significativo, i sei valori individuali nell'ordine del generatore, luogo e livello di incontro, assenza di oggetto tenuto, lingua, e contrassegno dell'incontro fatidico, che questo evento dichiara attivo al contrario di quello del decennale. Il soprannome inoltre non risulta marcato come soprannome, che è il modo in cui il programma dice che il nome coincide esattamente con quello canonico della specie nella lingua dell'esemplare, e conferma quindi per via indiretta il lavoro sui nomi localizzati.

Un guadagno collaterale merita una riga perché chiude un punto che il progetto teneva dichiarato come non verificato. Le sei formule dell'esperienza per gruppo di crescita erano state trascritte dalla loro forma corrente e il docstring del generatore dichiarava esplicitamente che il verificatore esterno sarebbe stato lo strumento per giudicarle. Su questo esemplare la formula del gruppo medio lento al livello dieci produce cinquecentosessanta, il verificatore mostra cinquecentosessanta e non obietta, quindi quella dichiarazione di incertezza si può ritirare per il gruppo impiegato qui.

Che cosa il giudizio non copre va detto con la stessa precisione. Due esemplari su centoventidue sono stati giudicati, e i rami dell'algoritmo che questi due esercitano sono la composizione invertita con mutazione antilucente e il metodo a elenco di semi. Restano non provati dal verificatore il ramo a lucentezza garantita, che è quello su cui il vecchio codice era erroneo e non soltanto incompleto, il ramo antilucente a estrazioni variabili, la trasformazione del seme per la tabella dei doni, la tabella dei caratteri giapponese e l'oggetto tenuto dell'evento del desiderio. I quattro esemplari che li esercitano sono nominati nella scheda delle pendenze, e provarli è il passo che resta.
## 15. La regola del bit dell'abilità, trovata da una obiezione su cinquantanove esemplari

Il 2026-09-02 l'utente ha aperto un secondo esemplare del lotto, il Pikachu della distribuzione di una compagnia aerea giapponese, e il verificatore lo ha dichiarato non valido con una formula sola: il bit dell'abilità non corrisponde al numero dell'abilità. È la prima obiezione che il progetto riceve su un campo che nessuna fonte gli aveva segnalato, e il difetto che essa ha scoperto riguardava cinquantanove esemplari su centoventidue.

### Che cos'è quel bit, dallo zero

Ogni specie della terza generazione porta due caselle di abilità. Alcune specie hanno due abilità distinte, e in quel caso ciascun esemplare ne ha una delle due; molte altre ne hanno una sola, e la seconda casella è vuota. Quale delle due caselle valga per un esemplare determinato non è memorizzato come nome né come numero dell'abilità, ma come un bit solo, che vale zero per la prima casella e uno per la seconda, e che vive nel bit di posizione trentuno della parola dei valori individuali, cioè accanto al contrassegno che dichiara l'esemplare un uovo.

La regola che il progetto applicava era quella nota e corretta per il caso generale: il bit è il bit meno significativo del valore di personalità. Da un esemplare non si scelgono né la natura né l'abilità, si leggono dal valore di personalità, e questa è la ragione per cui due esemplari con la medesima personalità hanno necessariamente la medesima abilità.

### La regola vera, e perché l'eccezione esiste

Il verificatore applica una regola in due parti, e la seconda parte il progetto non la conosceva. Se la specie ha due abilità distinte, il bit è il bit meno significativo del valore di personalità, come si credeva. Se la specie ha una sola abilità distinta, il bit deve restare a zero, qualunque cosa dica il valore di personalità.

La ragione è semplice quando si guarda al gioco e non al formato: la seconda casella non esiste, quindi il gioco non ha nessun motivo per puntarvi e non lo fa mai. Un esemplare che vi punti dichiara di avere una abilità che la sua specie non possiede, e nessuna partita reale può produrlo. Non è quindi una convenzione arbitraria ma un fatto sul comportamento del gioco.

Esiste un'eccezione all'eccezione, e va conosciuta perché senza di essa la regola scarterebbe esemplari legittimi. Tre specie hanno davvero due caselle piene, contenenti la medesima abilità: per esse il bit segue il valore di personalità come per tutte le altre. Gli identificativi interni delle tre sono 210, 333 e 334, e vanno verificati e non dedotti, perché per la prima l'identificativo interno coincide con il numero nazionale e per le altre due no.

### Come è stato trovato il dato, e la trappola nella fonte

La tabella delle abilità per specie viene dal costruttore della comunità, e leggerla ha richiesto di non credere alla sua intestazione. Il commento in testa al file dichiara le chiavi in ordine di numero nazionale; i dati dicono altro, perché la chiave 407 porta Latias, il cui numero nazionale è 380, e la chiave 380 porta Zangoose. Le chiavi sono dunque identificativi interni. Confondere le due numerazioni su questo dato significa attribuire a un esemplare le abilità di un'altra specie, quindi la lettura verifica se stessa su quelle due specie di controllo invece di fidarsi di una riga di commento. È lo stesso presidio che il progetto applica alla corrispondenza fra le due numerazioni, e la sua utilità è ora dimostrata su un caso in cui la fonte si contraddice.

### Perché il difetto era invisibile, in numeri

Il difetto non colpiva un esemplare su cento ma uno su due, e tuttavia era passato attraverso una verifica esterna. La ragione è aritmetica e vale scriverla, perché descrive una classe di difetti e non solo questo.

Degli esemplari prodotti, centoventi su centoventidue appartengono a specie con una sola abilità distinta. Non è un caso: gli esemplari da evento sono in grande maggioranza leggendari e iniziali, e nella terza generazione quelle specie hanno tipicamente una abilità sola. Su ciascuno di quei centoventi il bit era sbagliato se e solo se il valore di personalità era dispari, cioè con probabilità un mezzo, poiché il bit meno significativo di un valore prodotto dal generatore è equiprobabile. Gli esemplari da correggere sono risultati cinquantanove; il valore atteso è sessanta, e lo scarto vale meno di un quinto di deviazione standard di una binomiale con centoventi prove. L'accordo non dimostra nulla sul difetto, dimostra che il modello della sua incidenza è giusto, ed è questo che permette l'affermazione seguente.

Se l'incidenza è un mezzo, la probabilità che un singolo esemplare provato dall'esterno non manifesti il difetto è un mezzo, e quella che k esemplari indipendenti lo nascondano tutti è due elevato a meno k. Con una sola prova la probabilità di non accorgersene era dunque del cinquanta per cento, che è il caso peggiore possibile per un controllo a campione: un difetto raro si trova mai, un difetto sistematico si trova sempre, e uno che si presenta metà delle volte è quello che sopravvive più a lungo, perché una prova che passa sembra una conferma.

### Il conto che non torna, e l'esperimento che lo decide

Qui il registro del progetto ha una contraddizione che va dichiarata invece di essere lasciata dove sta. Il primo esemplare mai sottoposto, il Pikachu del decennale italiano, ha valore di personalità 0xD2A8AA71, che è dispari, e appartiene alla medesima specie a una sola abilità. Portava dunque quel bit attivo, e la obiezione ricevuta dal secondo Pikachu doveva valere anche per lui. Non è comparsa.

Le spiegazioni possibili sono due e si escludono. La prima è che il rapporto di allora contenesse più di una obiezione e che ne sia stata registrata una sola, e in questo caso il registro del progetto sovrastima la qualità di quel primo esito e va corretto. La seconda è che i due casi differiscano per qualche cosa che non abbiamo individuato, e in questo caso c'è una regola in più da capire.

L'esperimento che decide è un confronto a variabile singola, e sta in `_notes/prova-abilita`: due file del medesimo esemplare, identici in ogni byte tranne quel bit e la somma di controllo che ne dipende, cioè i byte di posizione 29 e 75. Se il verificatore contesta il primo e non il secondo, la spiegazione è la prima. L'esperimento è stato eseguito il 2026-09-02 e la sezione 16 riporta la risposta, che è la prima delle due spiegazioni.
## 16. L'esperimento a variabile singola, e la risposta

L'esperimento predisposto nella sezione precedente è stato eseguito il 2026-09-02 e ha risposto senza ambiguità. Il file con il bit dell'abilità attivo riceve la contestazione su quel campo; il file identico in tutto tranne quel bit, e la somma di controllo che ne dipende, viene dichiarato conforme. In entrambi i casi il verificatore ricostruisce il medesimo seme di origine e riconosce il medesimo evento, quindi la sola variabile che cambia il verdetto è quel bit.

Ne segue la prima delle due spiegazioni possibili, cioè che il rapporto del 2026-09-01 contenesse più di un rilievo e che ne sia stato registrato uno solo. Il registro del progetto sopravvalutava quel primo esito e la sezione 5 porta ora la dichiarazione corrispondente.

Sul come sia potuto accadere esiste una spiegazione che vale conoscere, perché riguarda lo strumento e non la distrazione di chi guardava. Il riquadro informativo che il verificatore mostra accanto a un esemplare riporta una sola riga di contestazione, non l'elenco. Un esemplare con due difetti appare quindi identico a uno con un difetto, e la seconda contestazione diventa visibile soltanto quando la prima è stata corretta. Il 2026-09-01 l'esemplare aveva due difetti, cioè il contrassegno dell'incontro fatidico e il bit dell'abilità, e il riquadro ne mostrava uno. L'elenco completo si ottiene dal rapporto di legittimità, che è una finestra separata, e da qui in avanti è quello a fare fede: la conseguenza operativa è che una sola riga di contestazione non significa un solo difetto, e chiedere il rapporto completo costa un clic.

## 17. I quattro rami messi alla prova, e i due difetti che hanno trovato

Il medesimo giorno sono stati sottoposti quattro esemplari scelti perché ciascuno esercitava un ramo del codice che nessun giudizio esterno aveva ancora toccato. Due sono stati dichiarati conformi e due hanno prodotto una contestazione, e le due contestazioni hanno scoperto difetti di natura completamente diversa.

### I due conformi, e che cosa il verificatore ha mostrato di sapere

Il Jirachi della stella dei desideri, in edizione giapponese, è conforme. Accanto a esso il verificatore scrive due numeri invece di uno, cioè il seme effettivo e, fra parentesi quadre, il valore da cui esso discende, che è esattamente il seme a sedici bit da cui il nostro programma era partito. È la conferma osservativa della trasformazione descritta nella sezione 11: quel metodo consuma due estrazioni per consultare la tabella dei doni, e il verificatore per riconoscerlo torna indietro di due passi e cerca il risultato fra i valori ammessi. Con esso sono confermate due cose che erano state costruite quel giorno stesso, cioè la tabella dei caratteri giapponese, poiché il nome dell'allenatore e il soprannome della specie sono scritti in katakana e vengono riletti correttamente, e la selezione del nome della specie nella lingua della voce.

Il medesimo Jirachi nella variante che copia il sesso dell'allenatore da chi riceve è conforme. Il verificatore classifica il suo valore di personalità nel ramo antilucente a estrazioni variabili e ricostruisce il seme. Sono confermati insieme il ramo che pesca di nuovo la prima estrazione finché i suoi bit oltre il terzo non siano tutti nulli, e il passaggio dell'allenatore di destinazione al programma, che è la via con cui le voci prive di quel dato diventano producibili.

### Il primo difetto: un valore dichiarato che va comunque derivato

Lo Zigzagoon della correzione dell'orologio delle bacche è stato contestato con la formula che la correlazione fra valore di personalità e valori individuali non corrisponde a quanto previsto per il tipo di incontro. La contestazione è informativa perché arriva accompagnata da due dati che la restringono: il verificatore ha ricostruito il seme, e lo ha ricostruito uguale al nostro, e ha riconosciuto l'esemplare come cromatico. Il ramo a lucentezza garantita, quindi, funziona: ciò che manca è un vincolo ulteriore.

Il vincolo sta in una funzione del verificatore che il progetto non aveva letto, e la sua esistenza contraddice il generatore della medesima implementazione. Le due derivazioni che dichiarano il sesso dell'allenatore invece di calcolarlo, cioè quelle che valgono per questo evento, sono trattate dal generatore restituendo il valore dichiarato; il verificatore invece ricalcola quel bit dalla prima estrazione successiva ai valori individuali e pretende che coincida con il valore memorizzato. Il generatore vincola il seme a produrre quel bit soltanto per i metodi che cadono nel ramo predefinito del suo albero di scelta, e il metodo a orologio esce dall'albero prima di arrivarci: ne segue che quel generatore può produrre un esemplare che quel verificatore rifiuta.

Davanti a una contraddizione interna alla fonte il progetto ha una regola, che è attendere un giudizio esterno; qui il giudizio esterno è la fonte stessa nella sua veste di verificatore, e quella veste vince, per la ragione semplice che è essa a giudicare. Il vincolo è stato quindi implementato nella ricerca del seme: fra i duecentoquattordici valori ammessi si accettano solo quelli la cui estrazione dedicata produce il bit dichiarato. Interessa le quattro voci del catalogo che impiegano quel metodo, e la prova che lo fissa verifica anche che il vincolo escluda qualcosa, perché un vincolo che non esclude nulla non è un vincolo.

Vale isolare il principio, perché è generale. Un campo che sia insieme dichiarato dall'evento e derivabile dal seme è ridondante, e la ridondanza è sempre un controllo: due strade portano allo stesso valore e devono concordare. Chi costruisce un esemplare può scegliere di scrivere il valore dichiarato oppure di calcolarlo, e le due scelte coincidono soltanto se il seme è vincolato. Trattare la parola dichiarato come sinonimo di libero è l'errore che il progetto ha commesso, ed è un errore che si ripresenta ogni volta che un formato contiene informazione ridondante.

### Il secondo difetto: un byte riservato a un terminatore che non serviva

Il Jirachi dell'evento del desiderio è stato contestato con la formula che è impossibile trovare una corrispondenza fra questo esemplare e i doni conosciuti. La causa si legge nella barra del titolo della finestra, dove il verificatore riporta il nome dell'allenatore che ha letto nel file: sei caratteri invece dei sette che quell'evento porta. Nessun dono conosciuto ha quel nome, quindi nessuna corrispondenza esiste.

Il difetto stava nella funzione che scrive un nome dentro un campo di lunghezza fissa, e la sua forma era plausibile: riservava sempre un byte al terminatore, e quindi accettava al massimo un carattere in meno della capienza del campo. La regola vera è che il terminatore si scrive soltanto se dopo i caratteri resta almeno un byte libero, e un nome che riempie esattamente il campo non ne porta alcuno. È corretto così perché la lunghezza del campo è già nota a chi legge: un terminatore serve a chi non sa dove finisca una stringa, e in un campo di lunghezza fissa quella informazione è fuori dalla stringa.

Il difetto era invisibile per tre ragioni che si sommano, e vale enumerarle perché insieme descrivono una classe. La prima è che colpisce soltanto i nomi che riempiono esattamente il campo, quindi la maggior parte dei casi funziona. La seconda è che il nome troncato resta una parola plausibile: nel catalogo produceva la forma italiana del nome del decennale al posto di quella inglese, cioè un nome che esiste per davvero, appartiene a un altro evento della medesima campagna, e non fa sospettare nulla a chi lo guardi. La terza è che il progetto aveva una prova su quel confine, e quella prova passava: era scritta sull'attesa sbagliata, cioè misurava l'implementazione invece del formato, ed è la seconda volta in due giorni che questo progetto trova una prova di quel genere.

L'estensione del difetto è la più ampia trovata finora: settantacinque voci del catalogo su centosettantatre portano un nome di allenatore lungo esattamente sette caratteri, e nel lotto prodotto sono settantaquattro esemplari su centoventidue. Vi si aggiungono cinque esemplari il cui nome di specie è lungo dieci caratteri, cioè la capienza del campo del soprannome, e che subivano lo stesso taglio.

La correzione ha rotto una prova esistente della prima e della seconda generazione, e come si è deciso va scritto perché modificare una prova è il momento in cui si può nascondere un errore. La regola è stata riletta nel codice della implementazione di riferimento per quelle generazioni, ed è la medesima: taglia alla lunghezza del campo e scrive il terminatore solo se avanza spazio. La vecchia attesa era dunque sbagliata anche là. Va aggiunto il motivo per cui là il difetto non si è mai manifestato: in quelle generazioni il gioco limita i nomi a sette caratteri per le versioni occidentali e a cinque per quelle giapponesi, su un campo di undici byte, quindi il terminatore ci sta sempre e il caso limite non si presenta con i nomi reali.

### Che cosa questo passaggio insegna sul metodo

Quattro esemplari scelti per esercitare rami diversi hanno prodotto due difetti, ed entrambi erano invisibili ai controlli interni del progetto. Il primo perché richiedeva di leggere una funzione del verificatore che nessuna descrizione del formato menziona; il secondo perché una prova interna lo copriva con un'attesa sbagliata. La suite di prove del progetto passava al cento per cento in entrambi i casi.

Ne segue la formulazione di un limite che vale enunciare senza attenuarlo: una suite di prove misura la coerenza di un programma con le proprie assunzioni, e non può misurare la correttezza di quelle assunzioni. Per quello serve un'autorità esterna, e l'esperienza di questi due giorni dice quanto: due esemplari giudicati hanno trovato un difetto ciascuno, e i quattro successivi ne hanno trovati altri due. Il tasso di scoperta non sta calando, il che significa che il numero di difetti residui non è ancora stimabile e che sottoporre più esemplari resta il lavoro più redditizio disponibile.
## 18. I due contestati tornano conformi, e i sei rami sono chiusi

Le due correzioni della sezione 17 sono state verificate lo stesso giorno sui medesimi esemplari che le avevano provocate, e entrambi sono ora dichiarati conformi.

Sullo Zigzagoon della correzione delle bacche il verificatore riporta il tipo osservato del valore di personalità e, fra parentesi quadre, il metodo che l'evento dichiara: la presenza del secondo significa che la corrispondenza con il dono è avvenuta, cioè che il vincolo che mancava era l'unico ostacolo. Il seme ricostruito è quello nuovo, spostato di un'unità dal vincolo appena imposto.

Sul Jirachi dell'evento del desiderio la barra del titolo riporta ora il nome dell'allenatore nei suoi sette caratteri e l'esemplare è conforme, con l'oggetto tenuto che era già corretto anche quando la corrispondenza falliva.

Con questi due, ogni ramo dell'algoritmo che il progetto sa produrre è stato giudicato conforme da un'implementazione indipendente. Sono sei: la composizione invertita con seme ristretto, la stessa con la mutazione antilucente, il ramo a lucentezza garantita che scrive i bit dell'identificativo, quello antilucente a estrazioni variabili, la trasformazione del seme per la tabella dei doni, e la selezione del seme da un elenco di valori distribuiti. Restano fuori dal giudizio i due metodi che il progetto non produce, cioè quello delle uova e quello del canale televisivo, e per essi non esiste alcun esemplare da giudicare.

## 19. Che cosa la verifica copre, misurato per dimensione

Sette esemplari giudicati su centoventidue prodotti è un rapporto che non dice nulla, e il modo in cui non dice nulla merita di essere spiegato perché la misura giusta è un'altra.

Gli esemplari non sono intercambiabili: differiscono lungo dimensioni indipendenti fra loro, e un giudizio vale per le dimensioni che quell'esemplare esercita e non per le altre. Le dimensioni si dividono però in due nature, e la distinzione è ciò che rende la misura utile. Il metodo di generazione, il ramo della lucentezza, la derivazione del sesso e la lingua sono dimensioni strutturali, cioè rami di codice: provarne uno lo prova per ogni esemplare che vi passi, e la loro copertura si può chiudere. La specie, il livello e le mosse sono dimensioni di dato, cioè righe di tabella: provarne una prova quella riga e nessun'altra, quindi la copertura completa richiederebbe di provare tutto. Fra le due sta il gruppo di crescita, che è una formula scelta da un dato: le formule sono sei e provarle tutte è fattibile, mentre provare tutte le specie non lo è.

Ne segue la lettura corretta, ed è che sulle dimensioni strutturali la copertura va portata a completa, mentre su quelle di dato resterà sempre parziale e il rischio si riduce per un'altra via: generando i dati da una fonte invece di trascriverli. È esattamente la ragione per cui questo progetto non trascrive tabelle, e la misura di copertura la ripaga rendendola visibile.

Lo strumento `tools/copertura-verifica.py` calcola quella misura dal registro dei giudizi e dalla tabella del verificatore, e per ciascun valore non ancora provato nomina la voce che lo esercita, perché un elenco di valori dice dove sta il rischio e non dice che cosa fare. Al 2026-09-02 l'esito è che il metodo di generazione è coperto su sei valori su sei, la lucentezza su tre su tre, il gruppo di crescita su tre su tre, cioè su tutti quelli che il lotto impiega. Restano scoperte quattro derivazioni del sesso dell'allenatore su nove e quattro lingue su sette, e sono otto esemplari nominati uno per uno: chiuderle è un lavoro di otto prove.

### Quante prove bastano, calcolato e non stimato

Alla domanda su quante prove servano in tutto questo studio aveva dato una risposta imprecisa che va corretta, perché l'imprecisione era di natura logica e non di calcolo. Diceva che il numero minimo di esemplari coincide con la massima delle cardinalità delle dimensioni, cioè nove: quella quantità è un limite inferiore e non il minimo, e confondere le due cose è confondere una condizione necessaria con una sufficiente.

Il limite inferiore si dimostra in una riga: su una dimensione con nove valori ogni esemplare ne copre uno solo, quindi ne servono almeno nove, e nessun'altra dimensione può abbassare quel numero. Che il minimo lo raggiunga richiederebbe però che esistano nove esemplari i quali, oltre a distribuirsi sui nove valori di quella dimensione, coprano anche tutti i valori di tutte le altre: è una condizione di ortogonalità fra le dimensioni, e non c'è ragione perché un catalogo di eventi storici la soddisfi, essendo esso un sottoinsieme arbitrario del prodotto cartesiano delle dimensioni, determinato da quali distribuzioni siano avvenute e non da un criterio combinatorio.

Il problema è quello della copertura di insiemi, che nella forma generale è NP-difficile; qui si risolve in modo esatto perché è piccolo, e due riduzioni lo rendono tale. La prima è che molti esemplari hanno la medesima firma di copertura e uno per firma basta: i centoventidue si riducono a trentaquattro firme distinte. La seconda è che le coppie da coprire sono ventinove, quindi una ricerca in profondità che si diramifichi sull'elemento con meno alternative termina subito.

I numeri sono questi. Il limite inferiore vale nove, il minimo esatto quattordici, e il rapporto fra i due, circa uno e cinquantasei, misura quanto il catalogo storico sia lontano dall'ortogonalità. L'algoritmo goloso su questa istanza restituisce anch'esso quattordici, cioè coincide con l'ottimo, mentre la sua garanzia teorica sarebbe quasi quattro volte peggiore: è un caso in cui la garanzia pessimistica non descrive il comportamento osservato, e la ricerca esatta si mantiene non per la qualità della soluzione ma perché sapere che quattordici è il minimo permette di chiudere la questione invece di lasciarla aperta.

Il numero operativamente utile è però un altro, ed è quanti esemplari restino dato ciò che è già stato provato. Esso non si ottiene sottraendo, perché i giudizi già eseguiti non formano necessariamente un sottoinsieme di una soluzione ottima: sono stati scelti per esercitare rami sospetti e non per minimizzare le prove. È una seconda istanza del medesimo problema, sull'universo delle coppie non ancora coperte, e la sua soluzione vale otto. I sette esemplari giudicati coprono ventuno coppie su ventinove, e ciascuno degli otto residui ne copre esattamente una nuova, che è il caso peggiore possibile e conferma quanto le combinazioni disponibili siano rigide.

Ne segue che la strada percorsa costa quindici prove contro le quattordici di quella ottima. La discrepanza va registrata per quello che è, cioè il prezzo di avere scelto le prime prove secondo il sospetto anziché secondo la combinatoria, ed è un prezzo che valeva pagare: quelle prime prove hanno trovato quattro difetti, e una scelta ottima li avrebbe trovati altrettanto bene ma senza indicare dove guardare.

Va aggiunta l'osservazione che rende quel numero interessante e non soltanto amministrativo. Le quattro derivazioni scoperte sono rami di codice mai eseguiti sotto giudizio, e i due difetti trovati il medesimo giorno stavano entrambi in rami che nessun giudizio aveva toccato: la correlazione fra copertura assente e difetto trovato, su questo campione, è totale. Non è una legge, ma è la migliore stima disponibile di dove convenga guardare.

## 20. La via di massa, e il vincolo che la rendeva impraticabile

Provare centoventidue esemplari uno alla volta non è ragionevole, e il verificatore offre una via migliore che vale documentare perché richiede una precauzione non evidente.

La via è caricare una cartella intera dentro le scatole di un salvataggio, con la voce del menu dei dati dedicata al caricamento delle scatole, e poi leggere quali posizioni portino il contrassegno di non conformità che il programma disegna sopra ciascuna. Centoventidue esemplari occupano cinque scatole, quindi cinque schermate sostituiscono centoventidue aperture, e per le sole posizioni contrassegnate si chiede poi il rapporto completo.

La precauzione riguarda le due forme in cui il generatore scrive ciascun esemplare. La forma di scambio e quella che il salvataggio contiene hanno la medesima dimensione di ottanta byte, e il caricamento di massa riconosce un file dalla sua dimensione: tenendole nella medesima cartella si otterrebbero duecentoquarantaquattro voci di cui la metà illeggibile, perché la forma del salvataggio è permutata secondo il valore di personalità e cifrata, e letta come forma di scambio produce byte senza senso. Il generatore scrive quindi la forma cifrata in una sottocartella, e il caricamento di massa non scende nelle sottocartelle: la separazione rende praticabile la via.

Vale notare che la precauzione non è una limitazione del verificatore ma una conseguenza di una scelta di formato di vent'anni fa, cioè che la lunghezza di un esemplare sia fissa e non porti con sé alcuna indicazione di quale delle due forme contenga. È lo stesso principio del terminatore della sezione 17: quando l'informazione su come leggere un dato sta fuori dal dato, chi legge deve procurarsela altrove, e in mancanza tira a indovinare.
## 21. La verifica di massa, e il quinto difetto

La via di massa è stata percorsa il 2026-09-02: centoventidue esemplari caricati in cinque scatole, e il programma lo conferma con un avviso che ne dichiara il numero. La lettura ha prodotto un difetto nuovo, il quinto, e una osservazione sullo strumento che vale registrare perché riduce il lavoro delle volte successive.

### Il difetto: un contrassegno che nessuna partita può aggiungere dopo

Un esemplare della prima scatola porta il contrassegno di non conformità, e il rilievo è che gli manca un fiocco, precisamente quello Nazionale. È il Metang di una manifestazione, e la tabella del verificatore lo dichiara: fra le sue centosettantatre voci, due portano un fiocco dichiarato, e sono le due edizioni di quel medesimo Metang, la giapponese e l'inglese.

Il difetto era nostro e di natura semplice: la lettura della tabella non estraeva quel campo, quindi nessuno dei due esemplari lo portava. Vale però isolare perché un fiocco non è un dettaglio estetico come potrebbe sembrare, e la ragione è la stessa che distingue l'oggetto tenuto dal valore di personalità. Un oggetto tenuto si può togliere, quindi la sua assenza non è mai una prova di illegittimità; un fiocco di merito, invece, non si può aggiungere dopo la consegna, poiché nessuna azione di gioco lo assegna. Ne segue che la sua assenza su un esemplare che lo dovrebbe portare è una contraddizione verificabile, e il verificatore infatti la verifica.

La posizione di un fiocco dentro la parola dei contrassegni non è documentata altrove che nel codice che la legge, una riga per fiocco, e si estrae da là con il consueto controllo sul conteggio: i fiocchi di merito sono dodici e occupano i bit dal quindicesimo al ventiseiesimo, con quello Nazionale al ventiquattresimo, cioè il decimo del campo. Sotto di essi stanno i quindici bit dei cinque livelli di gara, tre per gara, e la nostra struttura li tiene separati: un fiocco di gara passato per errore al campo di merito viene rifiutato invece di essere scritto nel posto sbagliato.

### L'osservazione sullo strumento, che riduce il lavoro futuro

La verifica di massa funziona, e il modo di leggerla merita una precisazione operativa. Il contrassegno di non conformità è disegnato sopra l'immagine di ciascuna posizione nella griglia, quindi una schermata per scatola basta a individuare tutte le posizioni difettose; ma il riquadro informativo che compare al passaggio del puntatore copre una parte della griglia, e una schermata scattata mentre esso è aperto nasconde le posizioni che gli stanno sotto. Perché una scatola sia leggibile per intero occorre quindi che il puntatore sia fuori dalla griglia.

È lo stesso genere di dettaglio del riquadro a una riga, e la sua conseguenza è la medesima: una schermata scattata senza quella precauzione non è sbagliata, è incompleta, e la sua incompletezza non è visibile in essa. Chi la guarda vede una griglia con dei contrassegni e conclude che siano tutti.

## 22. Le schede tecniche, e perché un giudizio va registrato con i suoi byte

Un giudizio di conformità riguarda una configurazione precisa di byte e non una categoria: vale per quel valore di personalità, quei valori individuali, quel nome e quel seme. Registrare soltanto che un esemplare è conforme perde l'informazione che serve, cioè che cosa esattamente sia stato dichiarato conforme, e senza quella non si può né riprodurre il caso né riconoscere che una modifica successiva lo ha cambiato.

Da qui il documento `SCHEDE-ESEMPLARI.md`, generato da `tools/schede-esemplari.py`, che per ciascuna voce producibile porta ogni campo derivato con la propria provenienza: il seme, il valore di personalità con la natura e il bit dell'abilità che ne discendono, la lucentezza, i sei valori individuali, l'allenatore con i suoi due identificativi e il sesso, la lingua, la specie interna con il soprannome nella lingua giusta, il livello con l'esperienza, le mosse con i loro punti potenza, l'oggetto tenuto distinguendo quello derivato da quello storico, i fiocchi, l'incontro fatidico e il metodo. Accanto al titolo di ciascuna scheda sta lo stato del suo giudizio esterno, letto dal registro.

Una scelta di quel programma va difesa perché è controintuitiva: esso non legge i file prodotti ma li ricalcola dalle sorgenti con il medesimo codice che li scrive. Un documento che leggesse i file descriverebbe ciò che si trova sul disco di una macchina, che non è versionato e in un clone non esiste; questo descrive ciò che il progetto produce, e resta vero dove i file non sono stati ancora generati. La scelta ha un effetto collaterale che è essa stessa una verifica: se due corse dessero schede diverse, la scelta del seme non sarebbe riproducibile, e il difetto si manifesterebbe come una modifica del documento senza che nessuno lo abbia toccato.

Un difetto di questo documento è stato trovato e corretto subito dopo la prima generazione, e vale registrarlo perché riguarda la precisione dei nomi. La prima versione chiamava seme di origine, per tutte le voci, il valore da cui la ricerca parte; per il metodo a elenco quel valore non è un seme ma la posizione nell'elenco degli ottantacinque semi distribuiti, e il verificatore per quelle voci dichiara come seme di origine il valore dell'elenco e non la posizione. Chiamare seme entrambe le cose avrebbe reso il documento incomparabile con il rapporto del verificatore proprio sul campo su cui il confronto conta.
## 23. Le uova, e il dato che era nella tabella che leggevamo già

Le cinquanta voci del catalogo che sono uova erano rifiutate dal generatore per la mancanza di un dato per specie, cioè il conto delle incubazioni, che nell'uovo occupa il campo dell'amicizia e che un verificatore controlla. La nota precedente lo dichiarava come il lavoro singolo più redditizio che restasse, e diceva dove trovarlo: il campo delle incubazioni nella tabella delle statistiche di base del disassemblato, da ottenere con un clone superficiale.

Era la risposta giusta alla domanda sbagliata. Quel dato non richiedeva alcun clone nuovo, perché sta nella tabella delle statistiche di base che l'implementazione di riferimento porta per la terza generazione, e che il progetto legge già: un record di ventotto byte per specie, con il conto delle incubazioni a un offset noto. Il costo reale era di trenta righe.

È la seconda volta nella medesima giornata che il progetto sopravvaluta un costo per avere cercato un dato nel posto che lo nomina invece che nel posto che lo contiene, e la prima era la disponibilità per titolo, dove avevo guardato i file degli incontri e concluso che il dato fosse inaccessibile mentre stava nelle tabelle di presenza. La regola che ne discende va scritta perché due occorrenze in un giorno non sono un caso: davanti a un dato apparentemente costoso conviene chiedersi non dove esso sia documentato, ma quale programma lo usi, perché quel programma deve averlo in una forma che si legge.

### Le tre cose che un uovo impone, e la quarta che non si può inventare

Un uovo non è un esemplare con un contrassegno in più, e i campi che la sua condizione governa sono quattro.

Il contrassegno sta in due posti e va scritto in entrambi, cioè nella parola dei valori individuali e nel byte dei contrassegni accanto a quello che dichiara la presenza della specie. Scriverne uno solo produce un esemplare internamente incoerente.

Il soprannome è imposto: l'implementazione di riferimento lo fissa nel momento in cui il contrassegno viene attivato, e vale per ogni lingua la parola giapponese per uovo. La ragione è di gioco e non di localizzazione, cioè che un uovo non mostra la specie che contiene.

La lingua è imposta a giapponese, che è una particolarità nota del formato in questa generazione e non una scelta.

Il quarto campo è il nome dell'allenatore, e su esso il progetto ha sbagliato una prima volta prima di leggere la fonte. La prima versione sostituiva al nome vuoto quello dell'allenatore di destinazione, che è la regola corretta per gli esemplari ordinari, e venticinque uova venivano rifiutate perché un nome in caratteri latini non si può scrivere con la tabella giapponese che la loro lingua impone. La fonte risolve la contraddizione in un modo che non avevo previsto: in terza generazione il nome di un uovo resta vuoto, e viene riempito soltanto quando l'uovo schiude su una generazione successiva, prendendolo dal salvataggio che lo fa schiudere. Un uovo di terza generazione non ha ancora un allenatore, e scrivergliene uno significherebbe inventarlo.

### L'esito

Il lotto passa da centoventidue esemplari a centosettantadue su centosettantatre. La sola voce che resta è quella del canale televisivo, che impiega un generatore pseudocasuale differente e che il progetto ha sempre dichiarato fuori portata.

La misura di copertura è stata riallineata, perché escludeva ancora le uova dal conto delle voci producibili e una esclusione che sopravvive alla propria causa falsa la copertura per difetto, dichiarando provate dimensioni che cinquanta voci non hanno esercitato. Con le uova dentro, le dimensioni strutturali passano da ventinove a trentasei coppie da coprire, il minimo assoluto da quattordici a sedici, e gli esemplari ancora da sottoporre da otto a dieci.
## 24. La verifica di massa eseguita, e il sesto difetto

Il 2026-09-02 l'utente ha caricato tutti i centosettantadue esemplari nelle scatole di un salvataggio vuoto di terza generazione e ha fotografato le sei scatole con il puntatore fuori dalla griglia, come la sezione 21 prescrive. La lettura ha dato un quadro netto e un difetto.

Le prime quattro scatole, cioè i centoventidue esemplari che non sono uova, non portano alcun contrassegno di non conformità. Il difetto dei fiocchi è chiuso, e con esso l'ultimo rilievo noto su quella parte del lotto: centoventidue esemplari su centoventidue non contestati in una lettura di massa.

Le due scatole delle uova portano trentacinque contrassegni su cinquanta, e la distribuzione dei contrassegni è essa stessa l'indizio che ha risolto il caso: le quindici uova non contestate sono tutte quelle di una medesima distribuzione, e le trentacinque contestate tutte le altre. Un difetto che colpisca un gruppo intero e ne risparmi un altro intero non è casuale, e la differenza fra i due gruppi va cercata in ciò che la tabella dichiara di essi e non nel codice che li produce.

### Il difetto: un argomento che manca non vale il suo valore predefinito ovvio

Il rilievo del verificatore era che il livello di incontro fosse invalido, e la sua conseguenza visibile era più istruttiva del rilievo stesso: non riconoscendo il dono, il verificatore aveva ricondotto quelle uova a un incontro generico, dichiarando come luogo di incontro un percorso della regione dove gli allevatori consegnano le uova ordinarie, e marcando in rosso una mossa che per un uovo ordinario è illegittima. Un solo campo sbagliato aveva spostato l'intera attribuzione.

La causa sta nel costruttore della tabella, che ha due forme. Quella a tre argomenti pone il livello di incontro uguale al livello. Quella a cinque lo prende dal quinto argomento, e lo lascia a zero quando quell'argomento manca. Il progetto usava il livello per tutte le voci, che è corretto per le forme a tre argomenti e sbagliato per le altre.

Il conto delle voci conferma la diagnosi prima di ogni prova: nel catalogo quindici uova portano il quinto argomento con il valore cinque, e trentacinque non lo portano e valgono dunque zero. Sono esattamente i due gruppi che le schermate distinguono.

### La lezione, che è sui valori predefiniti

L'errore non era nel leggere il dato ma nel supporre quale fosse il suo valore in assenza. Un argomento assente ha un valore predefinito, e quel valore è scritto nella firma del costruttore e non deducibile dal contesto: qui il valore ovvio sarebbe stato il livello, poiché un uovo si riceve a livello cinque, mentre il valore vero è zero, poiché un uovo non è stato incontrato da nessuna parte finché non schiude.

Il difetto era invisibile per la ragione consueta di questa serie: le quindici voci che il quinto argomento porta funzionavano, quindi il campo sembrava trattato bene. Ed è il sesto difetto trovato dal giudizio esterno, dopo il contrassegno dell'incontro fatidico, il bit dell'abilità, il vincolo del sesso derivato, il troncamento del nome e i fiocchi. Cinque dei sei riguardavano campi che nessuna descrizione del formato segnala come problematici, e tutti e sei sono stati trovati da un giudizio e nessuno da una prova interna.

## 25. Spinda, chiuso da due vie invece che da una

Il controllo su Spinda, eseguito con la base dati degli incontri del verificatore, ha dato ventotto incontri per quella specie, e fra essi compare un dono di evento della terza generazione per i titoli di Hoenn e di Kanto, a livello cinque, con le tre mosse che il nostro catalogo dichiara.

Ne segue che il caso è chiuso per due vie indipendenti e nessuna delle due passa dalla banca. La prima è che Spinda è nativa dei titoli di Hoenn, e l'utente possiede una cartuccia di uno di essi. La seconda, che nessuno dei due aveva visto, è che il lotto di questo progetto contiene già due Spinda da evento, l'uovo di una distribuzione statunitense e quello di una giapponese, entrambi prodotti dal 2026-09-02.

Vale registrare come il caso è nato, perché è un esempio di affermazione vera che porta a una conclusione falsa. L'affermazione della fonte era che Spinda non si potesse depositare da un certo titolo per un difetto di quella implementazione, ed è probabilmente vera. La conclusione che ne era stata tratta, cioè che Spinda andasse procurata dalla banca prima della scadenza, non segue: seguirebbe soltanto se quel titolo fosse la sola via, e non lo era. Una via rotta non implica una scadenza se esistono altre vie, e contare le vie è un lavoro diverso dal verificare che una sia rotta.
