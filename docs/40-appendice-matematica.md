---
tags: [appendice, matematica, teoria-informazione, probabilita, algebra, codici, quantizzazione, crittografia]
---

# Appendice matematica: le nozioni che l'analisi quantitativa impiega

Questa nota esiste per una ragione dichiarata: l'analisi quantitativa di [[12-analisi-quantitativa]] impiega nozioni di teoria dell'informazione, di probabilità, di algebra, di combinatoria, di geometria discreta, di teoria dei codici, di teoria del segnale e di crittografia, e le impiega dandole per note. Qui non sono date per note. Ogni voce enuncia la nozione, dice perché la nozione esiste, la mostra su un esempio svolto fino al risultato, e rimanda al punto preciso del progetto in cui viene usata.

Il criterio con cui la nota è stata riempita è meccanico e va dichiarato, perché è ciò che la rende verificabile invece che arbitraria: si percorre la nota quantitativa e ogni nozione che vi compare senza essere definita nel progetto diventa una voce di questa appendice. Non è quindi un glossario, che il progetto ha già in [[31-glossario]] e che dà definizioni brevi di termini di dominio: è un testo che si legge, dove una nozione matematica viene spiegata a chi non la conosce, con l'esempio svolto che è la parte che fa la differenza fra una definizione consultabile e una definizione compresa.

Una avvertenza sulla notazione. Le formule stanno in blocchi monospazio e in forma lineare, con `log2` per il logaritmo in base due, `^` per l'elevamento a potenza, `*` per il prodotto e `somma su x di` per la sommatoria: è la stessa convenzione di [[12-analisi-quantitativa]], adottata perché una nota Markdown deve restare leggibile in un editor di testo e in un vault Obsidian senza un compositore tipografico. Nel documento composto le medesime formule compaiono nella notazione matematica ordinaria.

Sull'attribuzione dei concetti vale quanto già scritto nella nota quantitativa: l'entropia e l'informazione mutua vengono da Shannon, la sicurezza perfetta dal suo lavoro del 1949, il cifrario a chiave scorrevole da Vernam, i codici ciclici da Peterson e Brown, la quantizzazione da Gray e Neuhoff, il campionamento con rifiuto da von Neumann e da Devroye, il sistema numerico fattoriale da Knuth, la trasparenza a byte dalla RFC 1662, il ripiegamento del riporto dalla RFC 1071. Le voci stanno nell'elenco `RIFERIMENTI_TEORICI` di `tools/build-source-map.py` e in bibliografia sotto l'intestazione che dichiara che sono citate per attribuzione e non come fonti lette.

## 1. Teoria dell'informazione

### 1.1 Il bit come unità di informazione

Il bit, in questa appendice e nella nota quantitativa, non è la cella di memoria che vale zero o uno: è l'unità con cui si misura l'incertezza. Un bit di informazione è la quantità che si acquisisce osservando l'esito di un esperimento con due esiti equiprobabili, per esempio il lancio di una moneta non truccata. La distinzione fra le due accezioni va tenuta ferma perché la nota quantitativa le usa entrambe nella stessa pagina: quando dice che un campo occupa quattro bit parla di memoria, e quando dice che la chiave di cifratura ha un deficit di 352 bit parla di informazione.

La nozione esiste perché senza un'unità di misura non si possono confrontare due incertezze. Dire che una chiave a 32 bit è più forte di una a 16 non richiede alcuna teoria; dire quanta parte della forza nominale di una chiave a 32 bit resta quando quella chiave viene riusata dodici volte richiede di misurare l'informazione, e la misura ha bisogno di un'unità.

L'esempio svolto è il ponte fra le due accezioni. Un campo di memoria di `b` bit ammette `2^b` configurazioni distinte; se tutte sono equiprobabili, l'incertezza sul suo contenuto è esattamente `b` bit di informazione, come la voce 1.3 dimostra. La coincidenza numerica fra le due accezioni vale soltanto sotto l'ipotesi di equiprobabilità, e la nota quantitativa mostra due casi in cui quell'ipotesi cade: la chiave di cifratura di generazione 3, dove la sorgente ha meno entropia dei bit che occupa, e il valore di personalità estratto per modulo, dove la distribuzione non è esattamente uniforme.

Si impiega nella premessa di teoria dell'informazione di [[12-analisi-quantitativa]] e in tutta la sezione sulla cifratura.

### 1.2 Variabile aleatoria discreta, in breve

La definizione completa sta nella voce 2.1, e va anticipata qui perché l'entropia si definisce su una variabile aleatoria e non su un numero. Per gli scopi di questa sezione basta sapere che una variabile aleatoria discreta è un oggetto che assume uno fra un numero finito di valori, ciascuno con una probabilità nota, e che la somma di quelle probabilità vale uno.

### 1.3 Entropia

L'entropia di una variabile aleatoria discreta `X` che assume valori in un insieme finito è definita come la somma, cambiata di segno, dei prodotti fra la probabilità di ciascun valore e il logaritmo in base due della medesima probabilità.

```
H(X) = - somma su x di p(x) * log2 p(x)
```

La nozione esiste per rispondere a una domanda operativa e non filosofica: quanti bit servono, in media, per comunicare l'esito di `X` a chi non lo conosce. Shannon ha mostrato che quella quantità è esattamente `H(X)`, e che nessuna codifica può fare meglio. Da qui segue l'interpretazione che questa appendice adotta: l'entropia è la quantità di incertezza che l'osservazione di `X` rimuove, misurata in bit.

L'esempio svolto è il caso uniforme, che è quello che ricorre in tutto il progetto. Se `p(x) = 1/n` per ognuno degli `n` valori possibili, ogni termine della somma vale `(1/n) * log2(1/n)`, cioè `-(1/n) * log2 n`; i termini sono `n`, quindi la somma cambiata di segno vale `n * (1/n) * log2 n = log2 n`. Con `n = 2^b` si ottiene `H(X) = b`, che è il ponte con la voce 1.1. Un secondo esempio, meno ovvio e istruttivo, è il caso degenere: se un valore ha probabilità uno e tutti gli altri zero, il solo termine non nullo vale `1 * log2 1 = 0`, dunque `H(X) = 0`, cioè un esito certo non porta informazione.

Le due proprietà che la nota quantitativa impiega sono la non negatività, che segue dal fatto che `log2 p(x)` non è mai positivo per `p(x)` compreso fra zero e uno, e il limite superiore `H(X) <= log2 n`, con uguaglianza se e solo se la distribuzione è uniforme. La seconda è la ragione per cui l'entropia di una sorgente si confronta sempre con il logaritmo del numero di valori: la differenza fra i due è il deficit, cioè quanto la sorgente è meno incerta di quanto la sua dimensione consentirebbe.

Si impiega nella premessa e nella sezione sulla cifratura di [[12-analisi-quantitativa]], dove il deficit di 352 bit della chiave è precisamente quella differenza.

### 1.4 Entropia condizionata

L'entropia condizionata `H(X | Y)` misura l'incertezza che resta su `X` dopo che `Y` è stato osservato. Si definisce come la media, pesata sulle probabilità dei valori di `Y`, delle entropie della distribuzione di `X` condizionata a ciascuno di essi.

```
H(X | Y) = somma su y di p(y) * H(X | Y = y)
```

La nozione esiste perché l'informazione non è una proprietà di un dato ma di un dato rispetto a ciò che si sa già. La medesima chiave di cifratura è imprevedibile per chi non ha visto nulla e completamente determinata per chi ha visto il testo in chiaro accanto al cifrato, e nessuna grandezza che dipenda dalla sola `X` può esprimere questa differenza.

L'esempio svolto è il caso che il progetto usa due volte. Se `X` è una funzione deterministica di `Y`, cioè `X = f(Y)`, allora per ogni valore osservato di `Y` la distribuzione di `X` è concentrata su un solo valore, dunque `H(X | Y = y) = 0` per ogni `y` per la voce 1.3, e la media di quantità tutte nulle è nulla: `H(X | Y) = 0`. È il caso della permutazione delle sottostrutture di generazione 3, che è una funzione del valore di personalità: nota la personalità, la permutazione non porta alcuna incertezza aggiuntiva, e questo è il motivo per cui la nota quantitativa afferma che la permutazione non aggiunge sicurezza.

Si impiega nella sezione sulla cifratura di [[12-analisi-quantitativa]], nella sottosezione sulla permutazione.

### 1.5 Informazione mutua

L'informazione mutua fra due variabili aleatorie è la riduzione di incertezza su una che si ottiene osservando l'altra.

```
I(X; Y) = H(X) - H(X | Y)
```

La nozione esiste perché serve una misura simmetrica di dipendenza che non presupponga alcuna forma funzionale del legame. Il coefficiente di correlazione misura quanto due grandezze si dispongano lungo una retta e vale zero per legami non lineari perfettamente deterministici; l'informazione mutua vale zero se e solo se le due variabili sono indipendenti, qualunque sia la forma del legame.

L'esempio svolto è il completamento della voce precedente. Se `X = f(Y)` si ha `H(X | Y) = 0`, dunque `I(X; Y) = H(X)`: `Y` porta tutta l'informazione di `X`. Il caso opposto è l'indipendenza, dove `H(X | Y) = H(X)` e l'informazione mutua è nulla. La simmetria della definizione, cioè `I(X; Y) = I(Y; X)`, si ottiene sostituendo la scomposizione dell'entropia congiunta e non è dimostrata qui perché il progetto non la impiega.

Si impiega nella premessa di [[12-analisi-quantitativa]] e implicitamente nell'argomento dell'attacco per sovrapposizione, dove la ripetizione della chiave rende una porzione di testo cifrato informativa su un'altra.

### 1.6 Disuguaglianza di elaborazione dei dati

La disuguaglianza afferma che nessuna elaborazione può creare informazione. Se `Z` è ottenuto da `Y` per una trasformazione che non consulta `X`, cioè se `X`, `Y` e `Z` formano una catena in cui `Z` dipende da `X` solo attraverso `Y`, allora l'informazione che `Z` porta su `X` non supera quella che `Y` porta su `X`.

```
I(X; Z) <= I(X; Y)
```

La nozione esiste perché è la formulazione precisa di un principio che si invoca spesso in modo vago, cioè che non si può recuperare ciò che è stato perso. Ed è quel principio a rendere definitive certe conclusioni del progetto: se un dato è stato quantizzato perdendo informazione, nessuna elaborazione successiva, per ingegnosa che sia, potrà ricostruirlo.

L'esempio svolto è la conversione dell'allenamento fra generazioni. Il valore di partenza è `X`, la sua conversione nel formato di arrivo è `Y`, e qualunque post-elaborazione del valore convertito è `Z`. Poiché la conversione perde 35,62 bit per cardinalità, come mostra la sezione sulla quantizzazione di [[12-analisi-quantitativa]], nessuna funzione applicata al risultato può riportarli: la perdita appartiene al formato di destinazione e non alla formula. È la ragione per cui quella sezione conclude che la fedeltà è impossibile e non soltanto difficile.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]] e nella discussione dei vincoli di conversione di [[07-conversione-vincoli]].

## 2. Probabilità

### 2.1 Variabile aleatoria discreta

Una variabile aleatoria discreta è una funzione che associa a ogni esito di un esperimento un valore, in modo che i valori possibili siano in numero finito o numerabile e che a ciascuno sia associata una probabilità. L'insieme delle coppie fra valore e probabilità è la distribuzione della variabile, e le probabilità sono non negative e sommano a uno.

La nozione esiste perché permette di parlare di una grandezza incerta come di un oggetto matematico, e quindi di farne medie, varianze ed entropie. Senza di essa non si può nemmeno enunciare la domanda a cui la nota quantitativa risponde più spesso, cioè quanto vale in media una certa quantità e quanto si disperde attorno a quella media.

L'esempio svolto è il valore di personalità di generazione 3, che è la variabile aleatoria più usata in questo progetto: assume `2^32` valori interi, e sotto l'ipotesi che il generatore del gioco sia uniforme ciascuno ha probabilità `1 / 2^32`. Da questa sola dichiarazione seguono, nelle sezioni successive della nota quantitativa, la probabilità di lucentezza, il numero atteso di iterazioni del campionamento con rifiuto e il bias del modulo.

Si impiega in tutta [[12-analisi-quantitativa]] e in [[06-identita-pokemon]].

### 2.2 Distribuzione uniforme

Una variabile aleatoria discreta ha distribuzione uniforme su un insieme di `n` valori quando ciascun valore ha probabilità `1/n`. È la distribuzione che formalizza l'assenza di preferenza fra gli esiti.

La nozione esiste come ipotesi di lavoro e va trattata come tale, non come una verità. Tutti i calcoli di questo progetto sui generatori pseudocasuali dei giochi assumono l'uniformità, e l'assunzione va dichiarata ogni volta perché è falsa in almeno un caso misurato: l'estrazione della natura per resto della divisione per venticinque non è uniforme, perché `2^32` non è divisibile per venticinque, e la deviazione relativa vale `9,3 * 10^-10`.

L'esempio svolto è quel calcolo, ridotto a numeri piccoli perché il meccanismo si veda. Si estragga un valore uniforme fra 0 e 9, dunque dieci valori equiprobabili, e si prenda il resto della divisione per tre. Il resto 0 si ottiene dai quattro valori `0, 3, 6, 9`, il resto 1 dai tre valori `1, 4, 7`, il resto 2 dai tre valori `2, 5, 8`: le probabilità sono `4/10`, `3/10` e `3/10`, e non `1/3` ciascuna, perché dieci non è divisibile per tre e i valori in eccesso favoriscono i resti più piccoli. La distorsione è tanto minore quanto più il numero di valori estratti è grande rispetto al modulo, ed è esattamente ciò che rende trascurabile ma non nullo il caso reale, dove si estrae fra `2^32` valori e si divide per venticinque.

Si impiega nella premessa e nella sezione sul campionamento con rifiuto di [[12-analisi-quantitativa]].

### 2.3 Indipendenza

Due eventi sono indipendenti quando la probabilità che si verifichino entrambi è il prodotto delle rispettive probabilità. Due variabili aleatorie sono indipendenti quando ogni coppia di eventi definiti sull'una e sull'altra è indipendente.

La nozione esiste perché l'indipendenza è l'ipotesi che consente di moltiplicare le probabilità, e moltiplicare è ciò che si fa quasi sempre per contare le configurazioni di un sistema con più parti. Il costo dell'ipotesi è che quando è falsa il risultato non è approssimato ma sbagliato di un fattore che non si conosce.

L'esempio svolto è il caso in cui il progetto ha dovuto correggere se stesso. Sesso e abilità di un esemplare di generazione 3 dipendono entrambi dal medesimo byte del valore di personalità: il sesso dal confronto fra il byte basso e la soglia della specie, l'abilità dal bit meno significativo. Non sono indipendenti, dunque contare le combinazioni come prodotto delle due cardinalità sovrastima il risultato, e la nota quantitativa le conta congiuntamente enumerando i 256 valori possibili del byte. La forma generale dell'errore è questa: due grandezze derivate dalla medesima sorgente non sono indipendenti anche quando sembrano semanticamente estranee.

Si impiega nella sezione sul campionamento con rifiuto di [[12-analisi-quantitativa]], nella sottosezione sull'indipendenza.

### 2.4 Distribuzione geometrica, valore atteso e varianza

Si ripeta un esperimento con due esiti, successo con probabilità `p` e insuccesso con probabilità `1 - p`, in modo indipendente, fino al primo successo. Il numero di prove necessarie è una variabile aleatoria con distribuzione geometrica, e la probabilità che servano esattamente `k` prove è il prodotto fra `k - 1` insuccessi e un successo.

```
P(K = k) = (1 - p)^(k-1) * p
valore atteso  E[K] = 1 / p
varianza       Var[K] = (1 - p) / p^2
```

La nozione esiste perché descrive il costo di ogni procedura del tipo prova e riprova, che in questo progetto è il campionamento con rifiuto: si estrae un valore di personalità, si controlla se soddisfa il vincolo, e se non lo soddisfa si ricomincia.

L'esempio svolto è il caso più sfavorevole fra quelli reali. Per una specie con rapporto di sesso di una femmina su otto esemplari, la probabilità che un valore estratto dia il sesso desiderato quando si cerca il più raro vale `p = 31/256`, cioè circa `0,121`; il numero atteso di estrazioni è dunque `1 / 0,121`, cioè circa `8,3`, e la deviazione standard, radice quadrata della varianza, vale circa `7,8`. La seconda cifra è quella che conta per un progetto che deve dichiarare un limite e non una media: una dispersione dello stesso ordine della media significa che il numero di iterazioni non è concentrato, quindi un limite superiore fissato al valore atteso viene superato spesso.

La derivazione del valore atteso è breve e vale mostrarla, perché è l'unico passaggio dove questa appendice usa una serie: `E[K] = somma su k da 1 a infinito di k * (1-p)^(k-1) * p`, e riconoscendo la derivata della serie geometrica si ottiene `E[K] = p * 1/p^2 = 1/p`.

Si impiega nella sezione sul campionamento con rifiuto di [[12-analisi-quantitativa]].

### 2.5 Distribuzione binomiale

Si ripeta un esperimento con probabilità di successo `p` per `n` volte in modo indipendente. Il numero di successi ottenuti è una variabile aleatoria con distribuzione binomiale, e la probabilità di ottenerne esattamente `k` combina il numero di modi in cui i `k` successi possono disporsi fra le `n` prove, dato dal coefficiente binomiale della voce 3.7, con la probabilità di una singola disposizione.

```
P(K = k) = C(n, k) * p^k * (1 - p)^(n - k)
valore atteso  E[K] = n * p
```

La nozione esiste perché la domanda operativa non è quasi mai se un evento raro si verifichi, ma quante volte si verifichi in un numero grande di occasioni. È la forma di ogni domanda sull'affidabilità di un processo ripetuto.

L'esempio svolto è quello dell'automazione. Se un programma compie una decisione per fotogramma a sessanta fotogrammi al secondo per otto ore, le prove sono `n = 60 * 3600 * 8 = 1 728 000`. Se la probabilità di errore per fotogramma è `q`, il numero atteso di errori è `n * q`, e la probabilità di non commettere alcun errore è `(1 - q)^n`. Volendo tenere quest'ultima sopra il novantanove per cento occorre `(1 - q)^n >= 0,99`, da cui, passando ai logaritmi e approssimando `ln(1 - q)` con `-q` per `q` piccolo, si ottiene `q <= -ln(0,99) / n`, cioè `q <= 5,82 * 10^-9`. È la cifra che la nota quantitativa riporta, ed è il modo in cui si dimostra che su un orizzonte lungo l'errore è praticamente certo per qualunque riconoscitore realistico.

Si impiega nella sezione sull'automazione di [[12-analisi-quantitativa]] e nel caso di studio corrispondente.

### 2.6 Approssimazione di Poisson, con il criterio di validità

Quando in una distribuzione binomiale il numero di prove `n` è grande e la probabilità di successo `p` è piccola, la distribuzione del numero di successi è ben approssimata da una distribuzione di Poisson di parametro `lambda = n * p`, la cui probabilità di `k` successi è la seguente.

```
P(K = k) = (lambda^k * e^(-lambda)) / k!
P(K = 0) = e^(-lambda)
```

La nozione esiste per una ragione di calcolo e una di comprensione. Di calcolo, perché il coefficiente binomiale su un milione di prove è ingestibile mentre l'esponenziale non lo è. Di comprensione, perché nella forma di Poisson il risultato dipende solo dal prodotto `n * p`, e questo rende immediato il fatto che raddoppiare la durata dell'esperimento e raddoppiare la probabilità di errore abbiano lo stesso effetto.

Il criterio di validità va dichiarato perché un'approssimazione senza criterio è un'affermazione non verificabile: l'approssimazione si considera buona quando `n` è grande, indicativamente sopra il centinaio, e `p` è piccola in modo che `lambda = n * p` resti moderato, indicativamente sotto la decina. Nell'esempio dell'automazione si ha `n = 1 728 000` e `lambda` dell'ordine dell'unità, dunque il criterio è soddisfatto con ampio margine.

L'esempio svolto è il controllo dell'approssimazione sul medesimo caso: con `lambda = 0,01` la probabilità di zero errori vale `e^(-0,01) = 0,99005`, contro il valore esatto `(1 - q)^n` che con `q = 5,79 * 10^-9` dà `0,99005`; le due cifre coincidono alle cinque decimali, che è la verifica che l'uso dell'approssimazione non ha cambiato la conclusione.

Si impiega nella sezione sull'automazione di [[12-analisi-quantitativa]].

### 2.7 Deviazione standard

La varianza di una variabile aleatoria è il valore atteso del quadrato dello scarto dalla media, e la deviazione standard è la sua radice quadrata. La seconda si preferisce alla prima quando si vuole un numero confrontabile con la media, perché ha la stessa unità di misura.

```
Var[X] = E[(X - E[X])^2]
sigma  = radice di Var[X]
```

La nozione esiste perché una media senza una misura di dispersione è una informazione incompleta, e in un progetto che deve dichiarare limiti operativi è l'informazione più fuorviante fra quelle disponibili. Due procedure con lo stesso costo medio, una che varia poco e una che varia molto, richiedono decisioni diverse.

L'esempio svolto è quello della voce 2.4: valore atteso `8,3` iterazioni e deviazione standard `7,8` iterazioni. Il rapporto fra le due è quasi uno, che per una distribuzione geometrica è la regola e non l'eccezione, dato che `sigma / E[K] = radice di (1 - p)` tende a uno per `p` piccolo. La lettura operativa è che per quella specie il campionamento con rifiuto ha un costo tipico di poche iterazioni ma una coda lunga, quindi il codice deve avere un limite di iterazioni e un comportamento dichiarato quando lo raggiunge, invece di confidare nella media.

Si impiega nella sezione sul campionamento con rifiuto di [[12-analisi-quantitativa]] e nella nota di architettura del codice.

## 3. Algebra e combinatoria

### 3.1 Fattoriale

Il fattoriale di un intero non negativo `n`, scritto `n!`, è il prodotto di tutti gli interi da uno a `n`, con la convenzione `0! = 1`. Conta il numero di modi in cui `n` oggetti distinti possono essere disposti in fila.

La nozione esiste perché il fattoriale è la cardinalità di base di ogni conteggio di disposizioni, e perché la sua crescita, più rapida di qualunque esponenziale, è la ragione per cui certi spazi si esplorano per intero e certi altri no.

L'esempio svolto è quello che serve al progetto: `4! = 1 * 2 * 3 * 4 = 24`, che è il numero di ordinamenti possibili delle quattro sottostrutture di un esemplare di generazione 3, e quindi il numero di righe della tabella di permutazione. La convenzione `0! = 1` non è un'arbitrarietà: è ciò che rende vera la formula del coefficiente binomiale nei casi estremi, e serve alla decodifica del codice di Lehmer della voce 3.11.

Si impiega nella sezione sulla cifratura di [[12-analisi-quantitativa]] e nella sezione 5 di [[DATA-FORMATS_Gen1-Gen2-Gen3]].

### 3.2 Permutazione

Una permutazione di un insieme finito è una funzione biiettiva dall'insieme in se stesso, cioè un riordinamento che non perde né duplica elementi. Le permutazioni di `n` elementi sono `n!` per la voce precedente, e si compongono fra loro come funzioni.

La nozione esiste perché distingue una trasformazione che riorganizza da una che altera. Una permutazione è sempre invertibile, dunque non distrugge informazione, e questo è il fatto che la nota quantitativa impiega due volte in direzioni opposte: la permutazione delle sottostrutture non aggiunge sicurezza perché non aggiunge incertezza, e la permutazione dei blocchi non viene rilevata dal checksum perché la somma non dipende dall'ordine.

L'esempio svolto è la permutazione delle quattro sottostrutture, che il gioco sceglie in funzione del resto della divisione del valore di personalità per ventiquattro. Se il resto vale zero l'ordine è quello di riferimento; se vale uno le ultime due sottostrutture si scambiano; e così via secondo la tabella. Poiché la funzione è biiettiva, chi conosce il resto ricostruisce l'ordine originale applicando la permutazione inversa, e la lettura è simmetrica alla scrittura.

Si impiega nella sezione sulla cifratura di [[12-analisi-quantitativa]] e in [[04-cifratura-gen3]].

### 3.3 Gruppo abeliano, e la commutatività da cui segue l'invarianza del checksum

Un gruppo è un insieme con un'operazione associativa che ha un elemento neutro e in cui ogni elemento ha un inverso. Il gruppo si dice abeliano, o commutativo, quando l'ordine degli operandi non cambia il risultato, cioè quando `a + b = b + a` per ogni coppia di elementi.

La nozione esiste perché nomina esattamente la proprietà responsabile di un difetto di sicurezza reale, e nominarla trasforma un'osservazione empirica in una dimostrazione. Il checksum additivo di generazione 3 somma parole in un gruppo abeliano, cioè gli interi modulo `2^16` con l'addizione; la somma di un insieme di addendi in un gruppo abeliano non dipende dall'ordine in cui gli addendi sono presi; dunque una permutazione dei blocchi produce la medesima somma. Non con alta probabilità: sempre.

L'esempio svolto è minimo e si verifica a mente. Si prendano le parole `0x1234` e `0x5678`: la somma vale `0x68AC` in un ordine e `0x68AC` nell'altro. Il caso reale è la tabella delle ventiquattro permutazioni, dove le settecentodiciannove alterazioni che consistono in un riordinamento delle sottostrutture passano il controllo con probabilità uno, contro la probabilità `2^-16` che si attribuirebbe a un'alterazione generica. È la ragione per cui la nota quantitativa conclude che il confronto con un'implementazione indipendente non è ridondante rispetto alla verifica di simmetria.

Si impiega nella sezione sul checksum di [[12-analisi-quantitativa]] e nel protocollo di verifica di [[21-collaudo]].

### 3.4 Anello dei resti modulo n

L'insieme dei resti della divisione per `n`, cioè `{0, 1, ..., n-1}`, con l'addizione e la moltiplicazione definite prendendo il resto del risultato ordinario, forma una struttura chiamata anello dei resti modulo `n`. Ogni operazione resta dentro l'insieme, e questo è precisamente ciò che fa un registro di larghezza fissa quando trabocca.

La nozione esiste perché il traboccamento non è un errore da evitare ma un'operazione ben definita di cui conoscere le regole. Un'addizione a 16 bit che trabocca non produce un valore indefinito: produce la somma modulo `2^16`, e i checksum del progetto si appoggiano su questo fatto invece di combatterlo.

L'esempio svolto è il checksum di generazione 3, che somma parole da 16 bit e conserva i soli 16 bit bassi: è la somma nell'anello dei resti modulo `2^16`. Poiché `65535 + 3 = 65538` e `65538 modulo 65536 = 2`, la somma di `0xFFFF` e `0x0003` vale `0x0002`. Il caso di generazione 1 è diverso e vale il confronto: là il checksum è a 8 bit e la somma è nell'anello modulo `2^8`, dunque il numero di valori distinti che il controllo può assumere è 256 e non 65 536, ed è per questo che la sua capacità di rilevazione è di due ordini di grandezza inferiore.

Si impiega in [[03-integrita-checksum]] e nella sezione sul checksum di [[12-analisi-quantitativa]].

### 3.5 Aritmetica modulo due, e lo XOR come somma

L'aritmetica modulo due ha due soli elementi, zero e uno, e in essa l'addizione coincide con l'operazione logica di or esclusivo, perché `1 + 1 = 0`. Ogni elemento è il proprio opposto, dunque sommare due volte la stessa quantità la annulla.

La nozione esiste perché spiega in una riga tutte le proprietà del cifrario a chiave scorrevole e della mascheratura delle quantità: la cifratura e la decifratura sono la medesima operazione, e ciò non è una comodità di implementazione ma una conseguenza algebrica dell'essere ogni elemento il proprio opposto.

L'esempio svolto è la mascheratura dello zaino di Smeraldo. La quantità in chiaro `q` viene scritta come `q XOR k`, con `k` la chiave di sicurezza; leggendo si applica di nuovo la chiave e si ottiene `(q XOR k) XOR k = q XOR (k XOR k) = q XOR 0 = q`. Da questa medesima proprietà segue il difetto misurato nella sezione sulla cifratura di [[12-analisi-quantitativa]]: se due dati diversi sono mascherati con la stessa chiave, il loro or esclusivo elimina la chiave e lascia l'or esclusivo dei due dati, cioè una relazione fra i chiari che non richiede di conoscere `k`.

Si impiega in [[04-cifratura-gen3]], in [[22-strumenti]] e nella sezione sulla cifratura di [[12-analisi-quantitativa]].

### 3.6 Teorema cinese del resto

Il teorema afferma che se si conoscono i resti di un numero rispetto a moduli a due a due primi fra loro, il numero è determinato in modo unico modulo il prodotto dei moduli. La forma che interessa qui è la sua conseguenza negativa: se i moduli non sono primi fra loro, la determinazione non è unica e l'informazione dei due resti si sovrappone.

La nozione esiste perché dice quando due vincoli su resti diversi sono indipendenti e quando invece si intralciano. È esattamente la domanda che si pone chi voglia costruire un valore di personalità che soddisfi contemporaneamente più condizioni.

L'esempio svolto è quello del progetto. Il sesso dipende dal byte basso del valore di personalità, cioè dal resto modulo 256, la natura dal resto modulo 25, e la permutazione dal resto modulo 24. I moduli 256 e 25 sono primi fra loro, perché il primo è una potenza di due e il secondo una potenza di cinque, dunque i due vincoli sono indipendenti e per il teorema esiste un valore che li soddisfa entrambi, unico modulo `6400`. I moduli 256 e 24 non sono primi fra loro, perché condividono il fattore otto, dunque quei due vincoli non sono indipendenti e alcune combinazioni sono irrealizzabili. Questa è la ragione per cui il risolutore di vincoli della conversione non può trattare i vincoli come una lista da soddisfare uno alla volta.

Si impiega in [[07-conversione-vincoli]] e nella sezione sulla lucentezza di [[12-analisi-quantitativa]].

### 3.7 Coefficiente binomiale

Il coefficiente binomiale `C(n, k)` conta i sottoinsiemi di `k` elementi che si possono estrarre da un insieme di `n` elementi distinti, senza riguardo all'ordine, e vale il fattoriale di `n` diviso per il prodotto dei fattoriali di `k` e di `n - k`.

```
C(n, k) = n! / (k! * (n - k)!)
```

La nozione esiste perché separa il conteggio delle scelte dal conteggio delle disposizioni: quando l'ordine non conta, contare le disposizioni sovrastima di un fattore `k!`, e il coefficiente binomiale è la correzione di quel fattore.

L'esempio svolto è un caso minimo verificabile a mano, `C(4, 2) = 24 / (2 * 2) = 6`, cioè i sei modi di scegliere due sottostrutture su quattro. Nel progetto il coefficiente serve nella distribuzione binomiale della voce 2.5 e nel conteggio dei punti interi con vincoli superiori della voce 4.3, dove compare nella forma delle combinazioni con ripetizione della voce seguente.

Si impiega nelle sezioni sull'automazione e sulla quantizzazione di [[12-analisi-quantitativa]].

### 3.8 Combinazioni con ripetizione

Il numero di modi in cui si possono distribuire `s` unità indistinguibili fra `d` contenitori distinti, ammettendo che un contenitore ne riceva zero, vale il coefficiente binomiale seguente.

```
N(s, d) = C(s + d - 1, d - 1)
```

La nozione esiste perché è il conteggio delle soluzioni intere non negative di un'equazione a somma fissata, ed è quindi il conteggio delle configurazioni di ogni sistema in cui una risorsa totale si ripartisce fra più campi. La dimostrazione classica è l'argomento delle barre e delle stelle: si scrivono le `s` unità in fila e si inseriscono `d - 1` separatori, e ogni disposizione dei separatori fra i `s + d - 1` posti individua una ripartizione.

L'esempio svolto è la forma che serve al progetto. La somma dei sei valori di allenamento di un esemplare di generazione 3 non può superare 510, e ciascuno non può superare 252: il conteggio delle configurazioni ammissibili parte da `N(s, 6)` per ogni somma `s` da 0 a 510 e sottrae quelle che violano il tetto individuale, con il metodo della voce 4.3. Il risultato, `22 858 382 491 812` punti, è il numero di configurazioni distinte di arrivo, cioè `44,38` bit.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]].

### 3.9 Principio di inclusione ed esclusione

Il principio calcola la cardinalità di un'unione di insiemi sommando le cardinalità dei singoli, sottraendo quelle di tutte le intersezioni a due, aggiungendo quelle a tre, e così via alternando i segni. Nella forma che serve qui viene usato al contrario, cioè per contare gli elementi che non violano alcun vincolo, sottraendo dal totale le violazioni con la medesima alternanza.

La nozione esiste perché sommare le violazioni le conta più volte quando due violazioni possono coesistere, e il principio è la contabilità esatta di quella sovrapposizione.

L'esempio svolto è il conteggio della voce precedente. Le configurazioni con somma `s` sono `N(s, 6)`; quelle in cui un campo specifico supera 252 si contano ponendo `253` unità in quel campo e ripartendo il resto, cioè `N(s - 253, 6)`; poiché i campi sono sei si sottraggono sei volte quel termine; poiché due campi possono superare il tetto contemporaneamente quando `s >= 506`, si riaggiungono i `C(6,2) = 15` termini `N(s - 506, 6)`. Con `s` che arriva a 510 non esistono terne violanti, perché servirebbero almeno 759 unità, dunque la somma alternata si arresta al secondo termine. È questa chiusura anticipata a rendere il calcolo esatto invece che approssimato.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]].

### 3.10 Principio dei cassetti

Il principio afferma che se si collocano `n` oggetti in `m` contenitori con `n > m`, almeno un contenitore riceve più di un oggetto. Nella forma quantitativa, almeno un contenitore riceve almeno il rapporto `n/m` arrotondato per eccesso.

La nozione esiste perché è la dimostrazione più economica di impossibilità che esista: non richiede di esaminare la funzione, solo di contare gli insiemi. Ed è la forma di tutte le dimostrazioni di perdita di informazione di questo progetto.

L'esempio svolto è la conversione dell'allenamento. Le configurazioni di partenza sono `2^80`, i punti di arrivo `22 858 382 491 812`, cioè meno di `2^45`: qualunque funzione dalla partenza all'arrivo manda almeno `2^35` configurazioni distinte nello stesso punto, dunque nessuna funzione può essere iniettiva e la fedeltà è impossibile. La conclusione non dipende dalla formula scelta, e questo è il punto: il principio dei cassetti dimostra un limite del formato e non un difetto dell'implementazione.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]] e in [[07-conversione-vincoli]].

### 3.11 Sistema numerico fattoriale e codice di Lehmer

Nel sistema numerico fattoriale la cifra di posizione `i`, contando da destra a partire da uno, ha peso `i!` e può assumere valori da zero a `i`. Ogni intero non negativo minore di `n!` ha una e una sola rappresentazione in questo sistema con `n - 1` cifre. Il codice di Lehmer è la corrispondenza che ne segue fra gli interi da `0` a `n! - 1` e le permutazioni di `n` elementi: si legge la prima cifra come l'indice dell'elemento da estrarre dalla lista ordinata, si rimuove quell'elemento, e si procede con la cifra successiva sulla lista rimasta.

La nozione esiste perché fornisce una numerazione canonica delle permutazioni, cioè un modo di passare da un indice a una permutazione senza tabelle. Riconoscere che una tabella incorpora questa numerazione significa poter sostituire la tabella con un algoritmo, e soprattutto poter verificare la tabella invece di fidarsene.

L'esempio svolto è la verifica che il progetto ha compiuto. Per `n = 4` gli indici vanno da 0 a 23. Si prenda l'indice 7: la divisione per `3! = 6` dà quoziente 1 e resto 1, dunque la prima cifra è 1 e si estrae il secondo elemento della lista ordinata, cioè `B`; il resto 1 diviso `2! = 2` dà quoziente 0 e resto 1, dunque si estrae il primo elemento rimasto, cioè `A`; il resto 1 diviso `1! = 1` dà quoziente 1, dunque si estrae il secondo elemento rimasto, cioè `D`; resta `C`. La permutazione è `B A D C`, che è esattamente la riga di indice 7 della tabella del gioco. La verifica è stata condotta su tutti i ventiquattro indici, e l'unicità della rappresentazione si dimostra per conteggio: le rappresentazioni possibili sono `1 * 2 * 3 * ... * n = n!`, tante quante le permutazioni, e la corrispondenza è iniettiva per costruzione, dunque è biiettiva.

Si impiega nella sezione sulla cifratura di [[12-analisi-quantitativa]] e nella sezione 5 di [[DATA-FORMATS_Gen1-Gen2-Gen3]].

## 4. Geometria discreta

### 4.1 Che cos'è un politopo

Un politopo è l'insieme dei punti di uno spazio a `d` dimensioni che soddisfano un numero finito di disuguaglianze lineari. In due dimensioni è un poligono convesso, in tre un poliedro convesso, e in `d` dimensioni conserva le medesime proprietà: è convesso, cioè contiene il segmento che unisce due suoi punti qualunque, ed è delimitato da facce piatte.

La nozione esiste perché è la forma geometrica di un insieme di vincoli lineari, e permette di ragionare su quei vincoli con l'intuizione dello spazio invece che con la manipolazione algebrica. Un insieme di tetti su singole grandezze e un tetto sulla loro somma non è un elenco di regole: è un solido, e la domanda su quante configurazioni ammetta diventa la domanda su quanti punti a coordinate intere quel solido contenga.

L'esempio svolto è il politopo dell'allenamento. Le sei grandezze sono le coordinate di uno spazio a sei dimensioni; i vincoli sono che ciascuna coordinata sia non negativa e non superi 252, e che la loro somma non superi 510. I primi dodici vincoli definiscono un ipercubo di lato 252, il tredicesimo lo taglia con un iperpiano, e la regione ammissibile è l'intersezione fra il cubo e il semispazio, che è un politopo. La forma spiega perché il conteggio non sia banale: il taglio interseca il cubo, dunque il numero di punti non è né quello del cubo né quello del simplesso, e va calcolato correggendo l'uno con l'altro.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]] e in [[07-conversione-vincoli]].

### 4.2 I punti interi di un politopo

Un punto intero di un politopo è un punto del politopo le cui coordinate sono tutte numeri interi. Il loro numero è una grandezza discreta che non si ricava dal volume, e la differenza fra i due può essere grande: il volume misura la regione, il conteggio misura le configurazioni realizzabili.

La nozione esiste perché in un sistema informatico le grandezze sono intere. Un valore di allenamento non può valere `12,5`, dunque la cardinalità che interessa non è il volume del politopo ma il numero dei suoi punti interi, e quel numero è la vera dimensione dell'insieme di arrivo di una conversione.

L'esempio svolto è il risultato del progetto. Il politopo dell'allenamento contiene `22 858 382 491 812` punti interi, e il logaritmo in base due di quel numero vale `44,38`, dunque la destinazione di una conversione non porta più di 44,38 bit di informazione, qualunque sia la formula. Per confronto, il volume dell'ipercubo di lato 252 in sei dimensioni sarebbe `253^6`, cioè circa `2,6 * 10^14`, un numero dello stesso ordine ma diverso: il taglio della somma rimuove una parte non trascurabile delle configurazioni, e usare la cardinalità del cubo al posto di quella del politopo sovrastimerebbe la capacità del formato.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]].

### 4.3 Contare i punti interi in presenza di vincoli superiori

Il conteggio dei punti interi di un politopo definito da vincoli di non negatività e da un vincolo sulla somma è immediato, perché coincide con le combinazioni con ripetizione della voce 3.8. L'aggiunta di un tetto su ciascuna coordinata rompe quell'immediatezza, e la si recupera con l'inclusione ed esclusione della voce 3.9: si conta come se il tetto non ci fosse, si sottrae per ciascuna coordinata il numero di configurazioni in cui quella coordinata lo supera, e si riaggiunge per ciascuna coppia il numero di quelle in cui due coordinate lo superano insieme.

La nozione esiste perché il passaggio dal conteggio libero al conteggio vincolato è il punto in cui una stima diventa un calcolo. Sottrarre le violazioni senza riaggiungere le sovrapposizioni è l'errore tipico, e produce un numero più piccolo del vero.

L'esempio svolto è quello già introdotto, con i numeri. Per una somma `s` le configurazioni libere sono `C(s + 5, 5)`; le violazioni di un campo si contano ponendovi 253 unità e ripartendo le rimanenti, cioè `C(s - 253 + 5, 5)`, e i campi sono sei; le violazioni doppie richiedono `506` unità, dunque compaiono solo per `s >= 506`, e sono `15` volte `C(s - 506 + 5, 5)`; le violazioni triple richiederebbero `759` unità e non esistono per `s <= 510`. Sommando su `s` da 0 a 510 la somma alternata si ottiene il totale della voce precedente, e la chiusura della serie al secondo termine è ciò che rende il risultato esatto.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]].
## 5. Teoria dei codici

### 5.1 Codice rilevatore d'errore

Un codice rilevatore d'errore è una regola che associa a un messaggio un'informazione ridondante, calcolata dal messaggio stesso, in modo che il destinatario possa ricalcolarla e confrontarla. Se il confronto fallisce, il messaggio è stato alterato; se riesce, il messaggio è probabilmente intatto. La differenza fra un codice rilevatore e un codice correttore è che il primo segnala l'alterazione e il secondo la ripara, al prezzo di una ridondanza molto maggiore.

La nozione esiste perché ogni canale e ogni supporto alterano i dati, e un'alterazione non rilevata è peggiore di un guasto dichiarato: un salvataggio corrotto che il gioco carica senza protestare produce danni che nessuno sa attribuire. La rilevazione trasforma un errore silenzioso in un errore visibile, che è tutto ciò che serve quando esiste una copia di riserva.

L'esempio svolto è il confronto fra le tre generazioni. Generazione 1 usa una somma a 8 bit con complemento, generazione 2 due somme a 16 bit su regioni diverse, generazione 3 una somma di parole a 16 bit per settore. La capacità di rilevazione di un codice di questo tipo, sotto l'ipotesi che un'alterazione produca un valore di controllo uniformemente distribuito, è pari a `1 - 2^-b` con `b` la larghezza del controllo: `1 - 2^-8`, cioè il `99,61` per cento, per generazione 1, e `1 - 2^-16`, cioè il `99,9985` per cento, per generazione 3. L'ipotesi va dichiarata perché è precisamente quella che la voce 3.3 mostra falsa per la classe di alterazioni che permutano i blocchi.

Si impiega in [[03-integrita-checksum]] e nella sezione sul checksum di [[12-analisi-quantitativa]].

### 5.2 Sindrome

La sindrome è il risultato del calcolo di verifica compiuto dal destinatario, o equivalentemente la differenza fra il valore di controllo ricevuto e quello ricalcolato. Vale zero quando non si rileva alcun errore, e un valore non nullo identifica una classe di alterazioni compatibili con ciò che si osserva.

La nozione esiste perché separa ciò che il destinatario osserva da ciò che è accaduto. Il destinatario non vede l'errore: vede la sindrome, e da essa deduce. In un codice rilevatore la deduzione si ferma alla presenza dell'errore; in un codice correttore la sindrome individua anche la posizione, ed è per questo che nella teoria dei codici la sindrome è l'oggetto centrale e non un dettaglio di implementazione.

L'esempio svolto mostra perché una sindrome non nulla non dice quale errore sia avvenuto. Su un checksum additivo a 16 bit, una sindrome pari a `+1` è compatibile con l'incremento di una parola qualunque fra quelle sommate, e le parole sono migliaia: la sindrome individua una classe di alterazioni di dimensione grande, non un colpevole. È la ragione per cui la diagnosi di `tools/emerald_bag_decode.py` non si limita al checksum ma cerca la coerenza fra gli identificativi e le tasche che li contengono: il checksum dice che qualcosa non torna, l'analisi di dominio dice che cosa.

Si impiega in [[03-integrita-checksum]] e in [[22-strumenti]].

### 5.3 Distanza di Hamming

La distanza di Hamming fra due sequenze della medesima lunghezza è il numero di posizioni in cui differiscono. La distanza minima di un codice è la minima distanza fra due parole valide distinte, e da essa segue la capacità del codice: un codice con distanza minima `d` rileva fino a `d - 1` errori e ne corregge fino alla parte intera di `(d - 1) / 2`.

La nozione esiste perché traduce la robustezza di un codice in una grandezza geometrica: le parole valide sono punti in uno spazio, e la distanza minima è quanto sono lontane fra loro. Un codice è robusto quando le sue parole valide sono isolate, cioè quando alterare pochi bit porta necessariamente in un punto non valido.

L'esempio svolto è il caso limite che riguarda questo progetto. Il checksum additivo aggiunge alle parole di dati un controllo, e la sua distanza minima è due: esiste una coppia di configurazioni valide che differiscono in due posizioni, cioè un dato incrementato di uno e il suo controllo incrementato di uno. Ne segue che rileva ogni errore singolo, cioè su un solo bit di un solo campo, e non garantisce nulla su errori doppi, ed è esattamente il comportamento che la voce 3.3 descrive con la permutazione: una permutazione altera molte posizioni contemporaneamente e resta dentro l'insieme delle configurazioni valide.

Si impiega nella sezione sul checksum di [[12-analisi-quantitativa]].

### 5.4 Errore a raffica

Un errore a raffica è un'alterazione che colpisce un insieme di bit consecutivi invece di bit isolati. La lunghezza della raffica è la distanza fra il primo e l'ultimo bit alterato.

La nozione esiste perché i guasti reali non sono indipendenti. Un settore di memoria che cede non altera un bit qua e uno là: altera una regione contigua, e lo stesso vale per un disturbo su un collegamento seriale, che dura un certo tempo e quindi colpisce un certo numero di bit consecutivi. Un codice progettato contro errori indipendenti può comportarsi molto peggio del previsto contro raffiche, e viceversa.

L'esempio svolto è la casistica reale della cartuccia di Smeraldo di questo progetto: gli oggetti della tasca degli strumenti sono sostituiti da sfere a partire da un certo slot in avanti, cioè l'alterazione ha un punto di inizio e una coda contigua. È una raffica, e la forma dell'alterazione è essa stessa un'informazione diagnostica, perché distingue una scrittura che ha invaso una regione da un offset da una corruzione sparsa. È la ragione per cui lo strumento di diagnosi, oltre a elencare le anomalie, cerca il punto di rottura e dichiara se la corruzione abbia un inizio.

Si impiega in [[22-strumenti]] e nella sezione sul checksum di [[12-analisi-quantitativa]], dove la superiorità di un CRC su una somma riguarda proprio le raffiche.

### 5.5 Divisione polinomiale in aritmetica binaria

Una sequenza di bit si può leggere come i coefficienti di un polinomio, dove il bit di posizione `i` è il coefficiente di `x^i` e i coefficienti stanno nell'aritmetica modulo due della voce 3.5. In quell'aritmetica la divisione fra polinomi si esegue come la divisione in colonna ordinaria, con la differenza che le sottrazioni sono or esclusivi e non richiedono prestiti.

La nozione esiste perché è il meccanismo su cui poggia il CRC della voce seguente, e perché la sua struttura algebrica è ciò che dà al CRC le proprietà che una somma non ha. In una somma il contributo di un byte non dipende dalla sua posizione; in una divisione polinomiale sì, perché la posizione è l'esponente.

L'esempio svolto è minimo e va seguito con la penna. Si divida `1101` per `101`. Il primo passo allinea `101` sotto i primi tre bit `110` e ne fa l'or esclusivo, ottenendo `011`; si abbassa il bit successivo ottenendo `111`; si allinea di nuovo `101` e l'or esclusivo dà `010`. Il resto è `10`, e quel resto è il valore di controllo. Ripetendo con la sequenza alterata in una qualunque posizione, il resto cambia: è la dipendenza dalla posizione che la somma non ha.

Si impiega nella sezione sul checksum di [[12-analisi-quantitativa]], nella sottosezione che confronta somma e CRC.

### 5.6 CRC

Un CRC, cioè un controllo di ridondanza ciclica, è il resto della divisione polinomiale del messaggio, moltiplicato per l'opportuna potenza di `x`, per un polinomio generatore fissato. Il destinatario ripete la divisione sul messaggio con il resto in coda e verifica che il resto sia nullo.

La nozione esiste perché un CRC rileva classi di errori che una somma non rileva, e le rileva con garanzia e non con probabilità. Con un generatore di grado `g` scelto opportunamente, un CRC rileva tutti gli errori singoli, tutti i doppi, tutti quelli di peso dispari se il generatore ha il fattore `x + 1`, e tutte le raffiche di lunghezza fino a `g`. Sono garanzie deterministiche, e la differenza rispetto al `99,9985` per cento di una somma a 16 bit non è nella cifra ma nella natura dell'affermazione.

L'esempio svolto è la ragione per cui i giochi non lo usano, che questo progetto ha calcolato invece di supporre. Su un processore a `4,194` MHz senza tabella precalcolata, un CRC a 16 bit costa un ordine di grandezza più cicli di una somma sui medesimi byte, e il calcolo sui `2938` byte coperti dal checksum di generazione 2 mostra un costo incompatibile con il tempo di salvataggio di allora. La scelta della somma non era ignoranza: era il compromesso corretto per quel bilancio di risorse, e la tabella che lo dimostra sta nella nota quantitativa.

Si impiega nella sezione sul checksum di [[12-analisi-quantitativa]] e in [[03-integrita-checksum]].

## 6. Segnale, quantizzazione e trasmissione

### 6.1 Quantizzatore scalare

Un quantizzatore scalare è una funzione che manda un insieme di valori, tipicamente grande o continuo, in un insieme di valori di uscita in numero finito, associando a ciascun valore di ingresso quello di uscita che lo rappresenta. La quantizzazione è irreversibile per costruzione, perché più ingressi condividono la stessa uscita.

La nozione esiste perché nomina correttamente un'operazione che nel progetto si sarebbe potuta chiamare conversione, e il nome corretto porta con sé una teoria. Chiamandola conversione si cerca la formula migliore; chiamandola quantizzazione si sa in anticipo che una perdita esiste, che è misurabile, e che dipende dalla cardinalità dell'insieme di arrivo prima che dalla formula.

L'esempio svolto è la conversione dell'allenamento fra la seconda e la terza generazione. Gli ingressi sono le sei grandezze di allenamento di generazione 2, ciascuna su 16 bit; le uscite sono i sei valori di generazione 3, ciascuno limitato a 252 con un tetto complessivo di 510. La funzione che porta dagli uni agli altri è un quantizzatore, e la voce 3.10 dimostra per conteggio che nessuna sua variante può essere iniettiva.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]] e in [[07-conversione-vincoli]].

### 6.2 Regione di quantizzazione

La regione di quantizzazione associata a un valore di uscita è l'insieme dei valori di ingresso che vengono mandati in quel valore. Le regioni sono a due a due disgiunte e la loro unione è l'intero insieme di ingresso: costituiscono cioè una partizione.

La nozione esiste perché la verifica che le regioni partizionino lo spazio è il controllo di correttezza di un quantizzatore, e un controllo che si può fare per conteggio senza esaminare il codice. Se le regioni si sovrapponessero la funzione non sarebbe ben definita; se lasciassero scoperto un valore, quel valore non avrebbe immagine.

L'esempio svolto è la verifica compiuta dal progetto sul quantizzatore reale, ed è elegante perché usa un'identità elementare. Le regioni non di saturazione contengono `63 504` valori di ingresso e la regione di saturazione ne contiene `2032`, e la somma vale esattamente `65 536`, cioè l'intero insieme dei valori a 16 bit. La verifica del primo numero si ottiene dall'identità per cui la somma dei primi `n` numeri dispari vale `n^2`, con `252^2 = 63 504`: le regioni hanno ampiezza crescente in progressione dispari, perché il valore di uscita è la radice quadrata dell'ingresso, e la radice quadrata ha inversa quadratica.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]].

### 6.3 Quantizzatore uniforme e non uniforme

Un quantizzatore è uniforme quando tutte le sue regioni hanno la medesima ampiezza, e non uniforme altrimenti. Un quantizzatore non uniforme si progetta quando l'errore che conta non è quello assoluto ma quello relativo, cioè quando sbagliare di dieci su un valore piccolo è più grave che sbagliare di dieci su un valore grande.

La nozione esiste perché la scelta fra i due tipi non è una preferenza ma la conseguenza di quale grandezza porti l'informazione utile. Nella trasmissione della voce si usa un quantizzatore non uniforme perché l'orecchio percepisce rapporti e non differenze; nel progetto si trova un quantizzatore non uniforme per una ragione diversa e altrettanto precisa.

L'esempio svolto è il quantizzatore dell'allenamento, che non è uniforme perché la funzione che lo definisce è una radice quadrata: le regioni corrispondenti ai valori di uscita piccoli sono strette e quelle corrispondenti ai valori grandi sono larghe, con ampiezze in progressione dispari come mostra la voce precedente. La conseguenza pratica è che l'errore di conversione non è costante sull'intervallo: due esemplari con allenamento basso restano distinguibili, due con allenamento alto vengono spesso confusi.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]].

### 6.4 Saturazione

La saturazione è il comportamento di un quantizzatore quando l'ingresso eccede l'intervallo rappresentabile in uscita: tutti i valori oltre il limite vengono mandati nel valore massimo. La regione di saturazione è dunque una regione di ampiezza grande, e all'interno di essa l'informazione sull'ingresso è perduta interamente.

La nozione esiste perché distingue due perdite di natura diversa che una misura complessiva confonde. Nella zona non satura la perdita è graduale e la distinzione fra ingressi vicini si degrada; nella zona satura non c'è degrado ma azzeramento, perché tutti gli ingressi diventano indistinguibili fra loro.

L'esempio svolto è il caso reale, con i suoi numeri: la regione di saturazione contiene `2032` dei `65 536` valori di ingresso, cioè il `3,1` per cento. La lettura corretta di quella cifra è che per il `96,9` per cento degli ingressi la conversione è una quantizzazione graduata, e per il restante `3,1` per cento è una cancellazione. Un esemplare allenato al massimo e un esemplare allenato molto oltre il necessario diventano lo stesso dato, e questa è una perdita che nessuna formula alternativa può evitare, perché il formato di arrivo non ha valori per rappresentarla.

Si impiega nella sezione sulla quantizzazione di [[12-analisi-quantitativa]].

### 6.5 Canale sincrono e canale asincrono

Un canale è sincrono quando mittente e destinatario condividono un segnale di temporizzazione, cioè un clock, che stabilisce quando ogni bit va letto. È asincrono quando quel segnale non esiste e il destinatario deve ricostruire la temporizzazione dal flusso stesso, tipicamente da un bit di inizio e da una velocità concordata in anticipo.

La nozione esiste perché la scelta fra i due determina l'intera struttura del protocollo. Su un canale sincrono ogni impulso di clock produce uno scambio, e chi fornisce il clock decide quando; su un canale asincrono i due capi devono accordarsi prima sulla velocità e tollerare uno scostamento.

L'esempio svolto è il cavo Link del Game Boy, che è sincrono e a scambio simultaneo: a ogni impulso di clock un bit esce e un bit entra, e i due capi si scambiano dati contemporaneamente. Da questa proprietà seguono due fatti che il progetto impiega. Il primo è favorevole: poiché chi fornisce il clock decide quando, un microcontrollore può fermarsi a pensare fra un bit e l'altro senza rompere nulla, ed è il fatto che rende praticabile l'opzione con hardware intermedio. Il secondo è sfavorevole ed è la voce 6.10.

Si impiega in [[08-cavo-link]], in [[30-opzioni-implementative]] e nella sezione sul cavo di [[12-analisi-quantitativa]].

### 6.6 Velocità di simbolo

La velocità di simbolo è il numero di simboli trasmessi nell'unità di tempo e si misura in baud. Coincide con il numero di bit al secondo solo quando ogni simbolo porta un bit, che è il caso di tutti i collegamenti trattati in questo progetto ma non il caso generale.

La nozione esiste perché la distinzione fra velocità di simbolo e velocità di informazione è la sede di un genere di errore ricorrente: un collegamento che trasmette quattro bit per simbolo ha una velocità di informazione quattro volte la sua velocità di simbolo, e confonderle porta a dimensionare male un canale.

L'esempio svolto è il calcolo del tempo di scambio su cavo. Con clock interno a `8192` Hz e un bit per impulso, la velocità è `8192` bit al secondo, cioè `1024` byte al secondo. I `424` byte del blocco di scambio di generazione 1 richiedono dunque circa `0,41` secondi per direzione, e poiché il canale è a scambio simultaneo le due direzioni non si sommano. Con il clock più rapido del Game Boy Color, `524 288` Hz, il medesimo blocco richiede circa `6,5` millisecondi, e il confronto fra le due cifre è ciò che spiega perché la scelta della velocità sia un parametro di progetto e non un dettaglio.

Si impiega nella sezione sul cavo di [[12-analisi-quantitativa]].

### 6.7 Occupazione di banda

L'occupazione di banda è la porzione dello spettro che un segnale utilizza. Per un collegamento numerico è legata alla velocità di simbolo, e per un collegamento radio determina quante trasmissioni possono coesistere senza interferire.

La nozione esiste perché su un canale condiviso l'interferenza non è un guasto ma la conseguenza prevedibile di una scelta di piano. Sapere quanta banda occupa una trasmissione è ciò che permette di dire quante ne stanno in un intervallo, e quindi di dedurre un piano dei canali invece di prenderlo per convenzione.

L'esempio svolto è la terna di canali della banda a 2,4 GHz, che il progetto ha dimostrato forzata e non convenzionale. Una trasmissione occupa circa `22` MHz; i canali numerati distano `5` MHz l'uno dall'altro; nell'intervallo utile di circa `60` MHz stanno dunque `60 / 22`, cioè tre trasmissioni non sovrapposte, e i canali che le realizzano sono quelli distanti almeno `22 / 5`, cioè cinque numeri: 1, 6 e 11. La terna non è una scelta ma l'unica soluzione, e questa è la differenza fra sapere una convenzione e conoscerne la ragione.

Si impiega nella sezione sul wireless locale di [[12-analisi-quantitativa]] e in [[11-wireless-locale-e-ponte-switch]].

### 6.8 Ciclo di lavoro

Il ciclo di lavoro è la frazione del tempo in cui un dispositivo trasmette effettivamente, rispetto al tempo totale. Un ciclo di lavoro basso significa che il canale resta libero per gli altri nella maggior parte del tempo.

La nozione esiste perché il costo di una trasmissione periodica non si misura dalla sua frequenza ma dal prodotto fra frequenza e durata. Due sistemi che trasmettono con la stessa cadenza possono occupare il canale in misura completamente diversa.

L'esempio svolto è l'annuncio del protocollo di rete locale della console, che invia una trama ogni `100` millisecondi. Se la trama dura una frazione di millisecondo, il ciclo di lavoro è dell'ordine di qualche millesimo, cioè il canale è libero per oltre il `99` per cento del tempo. La conseguenza operativa registrata dal progetto è che l'annuncio è compatibile con la presenza di altre reti sul medesimo canale, e che il collo di bottiglia del track non è la banda ma la modalità monitor dell'adattatore.

Si impiega nella sezione sul wireless locale di [[12-analisi-quantitativa]].

### 6.9 Trama e delimitazione di trama

Una trama è l'unità di dati che un protocollo trasmette come un tutto. La delimitazione di trama è il meccanismo con cui il destinatario riconosce dove una trama comincia e dove finisce, e può essere realizzata con un valore riservato che segna il confine, con una lunghezza dichiarata in testa, oppure con una lunghezza fissa concordata.

La nozione esiste perché un flusso di byte senza delimitazione non è interpretabile: il destinatario non sa dove tagliare. Ogni protocollo deve risolvere il problema, e le tre soluzioni hanno costi diversi in banda, in complessità e in robustezza.

L'esempio svolto è la lista di correzione dello scambio di generazione 1, che usa la terza soluzione, cioè la lunghezza fissa. Il progetto ha dimostrato che le altre due non sono disponibili su quel canale, e la dimostrazione è nella voce seguente.

Si impiega in [[08-cavo-link]] e nella sezione sul cavo di [[12-analisi-quantitativa]].

### 6.10 Trasparenza a byte, e perché lo stuffing è inammissibile su quel canale

La trasparenza a byte è la proprietà per cui un protocollo può trasmettere qualunque valore di byte, compresi quelli che usa come delimitatori, senza che il destinatario li confonda con i delimitatori stessi. Si ottiene con il byte stuffing, cioè sostituendo ogni occorrenza del valore riservato dentro i dati con una sequenza di scampo di due byte, come prescrive la RFC 1662.

La nozione esiste perché il byte stuffing è la soluzione standard al problema della delimitazione, e sapere perché una soluzione standard non si applica è più utile che sapere quale soluzione si è adottata.

L'esempio svolto è la dimostrazione che il progetto ha compiuto, e che vale riportare per esteso perché conclude con una impossibilità e non con una preferenza. Lo stuffing produce trame di lunghezza variabile, poiché il numero di sostituzioni dipende dai dati. Su un canale sincrono a scambio simultaneo, però, i due capi si scambiano un byte a ogni impulso di clock, dunque nessuno dei due può inviare più byte dell'altro: una trama di lunghezza variabile richiederebbe di annunciare in anticipo la propria lunghezza, e quell'annuncio sarebbe a sua volta uno scambio di lunghezza da concordare, il che rimanda il problema a se stesso senza terminare. La lunghezza fissa non è quindi una scelta conservativa: è l'unica soluzione compatibile con la natura del canale, ed è la ragione per cui la lista di correzione degli scambi ha una dimensione costante indipendente dal suo contenuto.

Si impiega nella sezione sul cavo di [[12-analisi-quantitativa]] e in [[08-cavo-link]].

## 7. Crittografia

### 7.1 Cifrario

Un cifrario è una coppia di funzioni, cifratura e decifratura, parametrizzate da una chiave, tali che la decifratura con la chiave corretta restituisce il testo in chiaro di partenza. La sicurezza di un cifrario non è una proprietà delle sue funzioni ma della difficoltà di risalire al chiaro senza la chiave.

La nozione esiste perché permette di distinguere la riservatezza dall'offuscamento, distinzione che nel dominio di questo progetto è essenziale e spesso confusa. La cifratura di generazione 3 è un cifrario nel senso pieno della definizione, ma il suo scopo non era proteggere un segreto da un avversario: era rendere costosa la manomissione con dispositivi di alterazione della memoria.

L'esempio svolto è la struttura di generazione 3, dove la chiave è l'or esclusivo fra il valore di personalità e l'identificativo dell'allenatore, e la cifratura è l'or esclusivo di quella chiave con ciascuna parola dei dati. Entrambi i termini della chiave sono presenti in chiaro nella medesima struttura, dunque chi possiede il dato possiede anche la chiave: il cifrario non protegge da chi legge il salvataggio, e questa non è una debolezza dell'implementazione ma la conseguenza del suo scopo dichiarato.

Si impiega in [[04-cifratura-gen3]] e nella sezione sulla cifratura di [[12-analisi-quantitativa]].

### 7.2 Sicurezza perfetta

Un cifrario ha sicurezza perfetta, nel senso di Shannon, quando il testo cifrato non porta alcuna informazione sul testo in chiaro, cioè quando l'informazione mutua fra i due è nulla. La condizione necessaria che ne segue è che l'entropia della chiave sia almeno pari a quella del messaggio.

La nozione esiste perché fornisce un criterio assoluto e non comparativo. Non dice che un cifrario è più forte di un altro: dice se soddisfa o non soddisfa una condizione dimostrabile, e la dimostrazione è un conteggio di entropie e non un'analisi di attacchi noti.

L'esempio svolto è la misura compiuta dal progetto. La chiave della cifratura di generazione 3 ha `32` bit, e i dati cifrati ne hanno `384`, cioè le quarantotto parole delle quattro sottostrutture; la condizione richiede almeno `384` bit di chiave, dunque il deficit vale `384 - 32 = 352` bit e la sicurezza perfetta non è raggiunta. Va tenuta distinta da questa la grandezza chiamata tasso di chiave, cioè il rapporto `384 / 32 = 12`, che dice quante volte la chiave viene riusata: le due grandezze rispondono a domande diverse, e una versione precedente della nota le confondeva.

Si impiega nella sezione sulla cifratura di [[12-analisi-quantitativa]].

### 7.3 Cifrario di Vernam e chiave monouso

Il cifrario di Vernam combina il testo in chiaro con una chiave della medesima lunghezza mediante or esclusivo. Prende il nome di chiave monouso quando la chiave è casuale, lunga quanto il messaggio e usata una sola volta, e sotto quelle tre condizioni raggiunge la sicurezza perfetta della voce precedente.

La nozione esiste perché è l'unico cifrario di cui la sicurezza sia dimostrata invece che congetturata, e perché le sue tre condizioni sono il metro con cui si misura ogni cifrario a chiave scorrevole reale. Ciascuna delle tre, violata, apre un attacco specifico e noto.

L'esempio svolto è la violazione che riguarda questo progetto. La cifratura di generazione 3 soddisfa la forma del cifrario di Vernam ma viola la seconda e la terza condizione, perché la chiave è dodici volte più corta del messaggio e viene riusata su ciascuna parola. Ne segue l'attacco della voce seguente, che non richiede di indovinare la chiave.

Si impiega nella sezione sulla cifratura di [[12-analisi-quantitativa]].

### 7.4 Attacco a testo cifrato noto, e la sovrapposizione

Un attacco a testo cifrato noto è quello condotto da chi possiede soltanto il cifrato, senza alcun chiaro corrispondente. È il modello di avversario più debole e quindi il più realistico, e un cifrario che ceda contro di esso non offre alcuna protezione pratica.

La nozione esiste perché la robustezza di un cifrario si dichiara sempre rispetto a un modello di avversario, e omettere il modello rende l'affermazione priva di contenuto. Un cifrario può essere solido contro chi possiede solo il cifrato e cedere contro chi possiede una coppia di chiaro e cifrato.

L'esempio svolto è l'attacco per sovrapposizione che la nota quantitativa espone in tre passaggi, e che qui si riassume nella sua struttura logica. Se due parole di dati `d1` e `d2` sono cifrate con la medesima chiave `k`, l'attaccante che osserva `c1 = d1 XOR k` e `c2 = d2 XOR k` calcola `c1 XOR c2 = d1 XOR d2` per la voce 3.5, ottenendo una relazione fra i chiari senza conoscere `k`. Poiché molte parole delle sottostrutture sono nulle o assumono valori prevedibili, quella relazione rivela direttamente il contenuto delle parole non note. Il difetto non sta nell'or esclusivo, che è la forma corretta del cifrario di Vernam, ma nel riuso della chiave, che è la seconda condizione violata della voce precedente.

Si impiega nella sezione sulla cifratura di [[12-analisi-quantitativa]].

## 8. Generatori pseudocasuali, e ricostruzione del loro stato

Quest'area è stata aggiunta il 2026-08-29, dopo che la ricerca sui metodi di generazione degli eventi di terza generazione ha reso necessario un vocabolario che l'appendice non aveva. Il criterio è lo stesso delle altre sette: ogni nozione che il progetto impiega senza averla definita diventa una voce. Ciò che la rende diversa è che qui la matematica non serve a misurare un meccanismo già descritto, ma a capire come si ricostruisce un dato che nessuno ha documentato, che è il lavoro di `recreate-pokemon-distributions-events/STUDIO-02-metodi-di-generazione.md`.

I numeri di quest'area sono verificati per calcolo e non trascritti da una fonte. Le due costanti dei generatori sono quelle che il dominio usa, e gli inversi moltiplicativi riportati sono stati calcolati e provati con un giro di andata e ritorno.

### 8.1 Generatore lineare congruenziale

Un generatore lineare congruenziale produce una successione di interi a partire da un valore iniziale, chiamato seme, applicando ripetutamente una funzione affine seguita da una riduzione per modulo.

```
s(n+1) = (a * s(n) + c) modulo m
```

La nozione esiste perché è il generatore più semplice che produca una successione di aspetto casuale con una sola moltiplicazione e una sola addizione, e per questo è il generatore di ogni sistema con poche risorse: un processore a pochi megahertz senza moltiplicatore veloce non può permettersi di più. Le tre costanti sono il moltiplicatore, l'incremento e il modulo, e la scelta del modulo come potenza di due rende la riduzione gratuita, perché coincide con il troncamento del registro descritto nella voce 3.4.

L'esempio svolto è il generatore dei giochi di terza generazione, dove il modulo è due alla trentaduesima, il moltiplicatore vale `0x41C64E6D` e l'incremento vale `0x6073`. Il generatore della console domestica della stessa epoca ha la medesima forma e costanti diverse, cioè moltiplicatore `0x343FD` e incremento `0x269EC3`, e la differenza fra i due è la ragione per cui una distribuzione proveniente da quella console richiede un metodo proprio: il meccanismo è identico, la successione non lo è.

Si impiega in `STUDIO-02-metodi-di-generazione.md` e in [[06-identita-pokemon]].

### 8.2 Il periodo, e le condizioni che lo rendono massimo

Il periodo di un generatore è il numero di passi dopo i quali la successione si ripete. Per un generatore lineare congruenziale con modulo potenza di due il periodo è al più il modulo stesso, e lo raggiunge se e solo se l'incremento è dispari e il moltiplicatore diminuito di uno è divisibile per quattro.

La nozione esiste perché un generatore con periodo corto è inutilizzabile e la verifica costa due divisioni: è il controllo più economico che si possa fare su un generatore ignoto, e la sua violazione si manifesta come una ripetizione che chi osserva attribuisce di solito a un difetto del proprio codice.

L'esempio svolto è la verifica su entrambe le costanti del dominio. Per il generatore portatile l'incremento `0x6073` è dispari e il moltiplicatore diminuito di uno vale `0x41C64E6C`, che termina con la cifra esadecimale C, cioè dodici, divisibile per quattro: le condizioni sono soddisfatte e il periodo è due alla trentaduesima. Per il generatore della console domestica l'incremento `0x269EC3` è dispari e il moltiplicatore diminuito di uno vale `0x343FC`, anch'esso divisibile per quattro: medesima conclusione. Entrambi i generatori percorrono tutti i valori possibili prima di ripetersi, e nessuno dei due ha un ciclo breve in cui cadere.

Si impiega come verifica preliminare di qualunque ricostruzione, e vale come esempio della differenza fra un controllo che costa due divisioni e una fiducia che costa un progetto.

### 8.3 I bit bassi, e perché il gioco usa la parola alta

Nei generatori lineari congruenziali con modulo potenza di due la qualità dei bit non è uniforme: il bit di posizione k ha periodo al più due alla k più uno, dunque i bit bassi si ripetono molto prima della successione completa. È il difetto strutturale di questa famiglia e non si corregge scegliendo costanti migliori, perché discende dall'aritmetica del modulo.

La nozione esiste perché spiega una scelta di progetto che altrimenti sembra arbitraria, cioè il fatto che il gioco non usi il valore prodotto dal generatore ma i suoi soli sedici bit alti. Non è uno spreco: è la sola parte del valore la cui successione ha periodo lungo.

L'esempio svolto è la misura, fatta sul generatore reale e non argomentata. Il bit di posizione zero ha periodo due, cioè si alterna a ogni passo; il bit uno ha periodo quattro, il bit due periodo otto, il bit tre periodo sedici, e la progressione continua raddoppiando, come il limite teorico prevede. Ne segue che il bit meno significativo di un valore estratto non porta quasi informazione, perché è determinato dalla parità del passo, mentre il bit trentuno ha periodo pari all'intera successione. Un progetto che estraesse una scelta binaria dal bit basso otterrebbe un'alternanza regolare invece di una scelta casuale, e questo è precisamente l'errore che la scelta di usare la parola alta evita.

Vale collegare questa voce alla voce 2.2. Là si mostra che la riduzione per modulo introduce una distorsione quando il modulo non divide il numero di valori; qui si mostra che i bit bassi hanno periodo corto. Sono due difetti indipendenti della stessa operazione, e la pratica corretta li evita entrambi prendendo la parola alta e riducendo quella.

Si impiega in [[06-identita-pokemon]] e in [[12-analisi-quantitativa]], nella sezione sul campionamento con rifiuto.

### 8.4 Reversibilità, e l'inverso moltiplicativo modulo una potenza di due

Un generatore lineare congruenziale è invertibile quando il moltiplicatore è invertibile modulo il modulo, cioè quando esiste un intero che moltiplicato per esso dà uno. Modulo una potenza di due questo accade se e solo se il moltiplicatore è dispari, e in quel caso il passo inverso ha la medesima forma affine del passo diretto.

```
s(n) = (a_inv * s(n+1) + c_inv) modulo m
dove   a_inv * a = 1 modulo m     e     c_inv = -c * a_inv modulo m
```

La nozione esiste perché rende possibile una cosa che sembra impossibile, cioè risalire la successione. Se il generatore fosse a senso unico, ricostruire il seme di origine di un esemplare richiederebbe di provare tutti i semi; essendo invertibile, basta applicare il passo inverso tante volte quante sono le estrazioni consumate.

L'esempio svolto è il calcolo per il generatore portatile, verificato e non citato. L'inverso del moltiplicatore `0x41C64E6D` modulo due alla trentaduesima vale `0xEEB9EB65`, e la costante inversa vale `0x0A3561A1`; per il generatore della console domestica i due valori sono `0xB9B33155` e `0xA170F641`. La verifica è un giro di andata e ritorno: preso un valore arbitrario, si applica il passo diretto e poi quello inverso, e si ritrova il valore di partenza. È il genere di prova che questo progetto preferisce a una citazione, perché non dipende dalla correttezza di chi ha scritto la fonte.

La conseguenza operativa per il track degli eventi è diretta. Un esemplare autentico porta in chiaro il proprio valore di personalità, che è composto da due estrazioni consecutive; invertendo il generatore si risale al valore che le precede, e da quello al seme di origine. È questa proprietà, e non una forzatura, a rendere possibile la determinazione del metodo di un evento a partire da un campione.

Si impiega in `STUDIO-02-metodi-di-generazione.md`.

### 8.5 Salto in avanti, e la distanza fra due stati

Applicare n volte il passo di un generatore lineare congruenziale equivale ad applicare una volta un passo con costanti diverse, calcolabili in un numero di operazioni proporzionale al logaritmo di n. Il moltiplicatore composto è la potenza n-esima del moltiplicatore, e l'incremento composto è il prodotto dell'incremento per la somma dei primi n termini della progressione geometrica del moltiplicatore.

```
a(n) = a^n modulo m
c(n) = c * (a^(n-1) + ... + a + 1) modulo m
```

La nozione esiste perché consente di rispondere a una domanda che si presenta continuamente quando si studia un generatore osservato dall'esterno: quante estrazioni separano due valori noti. Senza il salto in avanti bisognerebbe avanzare uno per uno; con esso si avanza per potenze, e la distanza si cerca per bisezione sull'esponente.

L'esempio svolto, in forma di conteggio, è il costo delle due strade. Stabilire se due valori distino meno di un milione di estrazioni richiede un milione di passi per la via diretta, e circa venti passi composti per la via del salto, perché due alla ventesima supera un milione. Il rapporto fra i due costi è di quattro ordini di grandezza, ed è la ragione per cui gli strumenti che analizzano quel generatore rispondono in un istante a domande che sembrerebbero richiedere una ricerca lunga.

Si impiega nella ricostruzione dei metodi e nella valutazione del costo di una ricerca, cioè nella voce seguente.

### 8.6 Lo spazio dei semi, e quando una ricerca esaustiva è praticabile

Una ricerca esaustiva su uno spazio di N candidati costa N verifiche, e la sua praticabilità non è una questione di ingegno ma di aritmetica: si stabilisce moltiplicando N per il costo di una verifica e confrontando il prodotto con il tempo disponibile.

La nozione esiste perché è la sola dimostrazione di completezza disponibile quando non si conosce la struttura del problema, ed è la forma dell'argomento più forte prodotto dalla ricerca sugli eventi. Va accompagnata dal suo contrario, che è la ragione per cui l'argomento non si applica sempre: raddoppiare la larghezza dello spazio in bit eleva al quadrato il numero dei candidati, e la distanza fra praticabile e impraticabile si attraversa in poche decine di bit.

L'esempio svolto è il confronto fra i due spazi che il dominio presenta. Un seme di origine ristretto a sedici bit ammette 65 536 candidati: al ritmo, prudente per qualunque calcolatore moderno, di un milione di verifiche al secondo, la ricerca completa costa meno di un decimo di secondo, e questo è ciò che ha reso possibile determinare per esaustione l'unico seme compatibile con un campione. Un seme non ristretto ammette 4 294 967 296 candidati, cioè 65 536 volte tanti, e al medesimo ritmo la ricerca completa costa circa settantadue minuti: è ancora praticabile ma non più gratuita, e con una verifica cento volte più costosa diventerebbe di cinque giorni. La restrizione del seme a sedici bit, che una fonte dichiara come parte della definizione del metodo, è quindi ciò che sposta quel problema dalla categoria del calcolo lungo a quella del calcolo immediato.

Vale enunciare la conseguenza generale, perché vale oltre questo caso: quando una ricerca esaustiva è praticabile, l'unicità della soluzione trasforma un'ipotesi in una determinazione, e quella è la sola forma di certezza ottenibile senza la specifica. È la medesima struttura di argomento della voce 3.10 e della verifica della tabella delle permutazioni in [[12-analisi-quantitativa]].

### 8.7 Determinazione dello stato da un'osservazione parziale

Il problema è il seguente: si osservano alcuni bit di alcune estrazioni consecutive e si vuole ricostruire lo stato del generatore. La domanda preliminare è quanti bit servano, e la risposta è di natura contabile: lo stato ha una larghezza fissa in bit, e occorre osservare almeno altrettanti bit informativi, altrimenti i candidati compatibili sono più di uno.

La nozione esiste perché separa i casi in cui la ricostruzione è determinata da quelli in cui restituisce un insieme di candidati, e la distinzione va fatta prima di cercare e non dopo. Cercare uno stato quando le osservazioni non lo vincolano produce molte soluzioni e l'impressione di un errore.

L'esempio svolto è quello del dominio. Lo stato ha trentadue bit. Un esemplare porta in chiaro un valore di personalità di trentadue bit, che proviene però da due estrazioni di cui si sono prese le parole alte, cioè da sedici più sedici bit informativi: i bit osservati sono trentadue e lo stato ne ha trentadue, dunque il problema è al limite della determinazione e ammette in generale un numero piccolo di candidati, non necessariamente uno. Aggiungendo i valori individuali, che provengono da due estrazioni ulteriori e portano quindici bit informativi ciascuna, il vincolo diventa largamente sovrabbondante, e da qui segue che il campione completo di un esemplare determina il suo seme di origine quando il metodo è noto, e permette di distinguere fra metodi quando non lo è. È il fondamento aritmetico della ricerca descritta in `STUDIO-02-metodi-di-generazione.md`.

Va dichiarato il limite di questo conteggio, perché è un conteggio di bit e non una dimostrazione: contare i bit informativi dice quando la ricostruzione non può essere unica, non garantisce che lo sia quando i bit bastano. Le funzioni in gioco non sono iniettive per costruzione, e la garanzia si ottiene enumerando i candidati, cioè con la ricerca della voce precedente.
