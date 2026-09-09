# Studio 07: gli scambi in gioco e gli incontri che una condizione sblocca

Nota di studio del 2026-09-09, aperta da una direttiva dell'utente che chiede di estendere l'analisi a due classi che il progetto nominava senza contarle, con la dichiarazione che con esse la ricerca sulle classi dovrebbe essere al completo. Le due classi hanno in comune ciò che le rende collezionabili distinti e non doppioni: un esemplare che vi appartiene porta nel proprio dato una traccia della via da cui viene, e quella traccia non è riproducibile da una cattura ordinaria.

## Che cosa unisce le due classi, e perché non è la rarità

Vale fissarlo prima dei numeri, perché è il criterio che ha guidato l'enumerazione. Non conta la difficoltà di ottenere un esemplare, che è tempo speso e non una proprietà del dato; conta che il dato porti un campo il cui valore, per quella specie, non si ottiene per altra via. In uno scambio in gioco quel campo è l'allenatore di provenienza, con il suo identificativo e nella maggior parte dei casi un soprannome fissato dal gioco. In un incontro condizionato quel campo è la terna fra luogo d'incontro, tipo di casella e specie, che esiste soltanto se una circostanza si è verificata.

## Gli scambi in gioco, contati sulla fonte di primo livello

La classe era nominata da due enumerazioni della comunità lette il 2026-09-08, che la contavano da fuori: duecentotrentotto voci in una e ottocentouno fra scambi e doni nell'altra. Ora è contata sulla fonte di primo livello, cioè le tabelle del verificatore, con `tools/censimento-scambi.py` e il documento `CENSIMENTO-SCAMBI.md`.

Le voci di tabella sono duecentotrentotto e quelle distinte duecentotrentatre, su centocinquantadue specie diverse. I due numeri differiscono perché le tabelle di una coppia di titoli si sovrappongono per costruzione, cioè esiste una tabella comune alla coppia e accanto una tabella per versione, e la stessa voce compare in entrambe; la deduplicazione è dichiarata nel programma e non lasciata implicita. Va notato per onestà che il duecentotrentotto della fonte comunitaria e il nostro coincidono, ma la coincidenza non è ancora un accordo: le due enumerazioni non sono state confrontate riga per riga, e finché non lo saranno il numero uguale può nascere da insiemi diversi.

| Generazione | Voci | Con valore di personalità fissato | Specie distinte |
|---|---|---|---|
| 1 | 26 | 0 | 23 |
| 2 | 11 | 0 | 11 |
| 3 | 23 | 19 | 22 |
| 4 | 38 | 16 | 37 |
| 5 | 40 | 7 | 26 |
| 6 | 12 | 0 | 12 |
| 7 | 24 | 0 | 24 |
| 8 | 26 | 4 | 24 |
| 9 | 38 | 0 | 37 |

Il dato che decide la producibilità è la colonna centrale, e va letto insieme a ciò che il progetto ha già stabilito sulle altre classi. Dove la fonte scrive il valore di personalità, come nelle diciannove voci di terza generazione e nelle sedici di quarta, l'esemplare è riproducibile byte per byte senza alcuna ricerca di semi, perché il valore che determina identità, sesso, abilità e cromaticità è un dato della tabella e non un'estrazione. Dove il valore manca perché il gioco lo genera al momento della consegna, come in sesta, settima e nona generazione, la fedeltà torna indecidibile nello stesso senso già registrato per i doni moderni. In prima e seconda generazione il valore non esiste affatto, quindi la legittimità è banale e la fedeltà si esaurisce nei valori individuali, che la fonte scrive per tutte e undici le voci di seconda generazione.

Due osservazioni valgono più del conto. La prima è che la tabella dei doni del Ranch, cioè `RanchGifts` con le sue ventidue voci, sta nella fonte fra le tabelle di scambio e non fra i doni: la classe a via chiusa che lo Studio 06 aveva trovato attraverso una fonte comunitaria è dunque enumerabile dalla fonte di primo livello, e con essa il valore di personalità di ciascuna voce. La seconda è che quattro voci di terza generazione stanno nella tabella degli scambi del gioco da console fissa, cioè lo scambio dell'avamposto e i tre della città mineraria, con allenatore Hordel e Duking: sono scambi in gioco a tutti gli effetti e la loro via richiede un titolo che l'utente non possiede.

## Gli incontri condizionati, e una correzione all'esempio da cui il lavoro è nato

L'esempio dato dall'utente era il Wynaut dell'Isola Miraggio, che conserva come luogo d'incontro quello dell'isola. La verifica sulle tabelle corregge la premessa, e la correzione va scritta perché altrimenti sarebbe finita nei documenti come un fatto.

L'isola non ha un luogo d'incontro proprio. Nella fonte è l'area d'erba del luogo quarantacinque, che è la rotta che l'isola affaccia, e quel medesimo luogo porta accanto le proprie aree d'acqua e di pesca con Tentacool, Wingull, Pelipper, Magikarp e Sharpedo. Un Wynaut catturato là registra dunque la rotta, non l'isola. Ciò che lo rende comunque irripetibile è un fatto diverso e più preciso: in quel luogo l'erba ospita quella specie sola, e quella specie non compare in nessun'altra area del titolo. La traccia sul dato è quindi la terna fra luogo, tipo di casella e specie, e non il nome del luogo.

Da questa correzione discende il criterio, che è meccanico e sta in `tools/censimento-condizionati.py` con il documento `CENSIMENTO-CONDIZIONATI.md`. Il programma applica tre prove distinte a tutte le tabelle selvatiche dalla prima alla quinta generazione, cioè ventuno archivi.

La prima prova è il tipo di casella, perché la fonte classifica ogni area e alcuni tipi sono essi stessi una condizione. Sono dichiarati nel programma e divisi in due famiglie: condizione di evento, cioè lo sciame annunciato alla televisione in terza e quinta generazione, la grotta nascosta di quinta, la gara di scarabei, l'albero del miele e le aree della zona safari; e condizione di metodo, cioè spaccaroccia e colpo di testa, che chiedono al giocatore un modo di cercare invece di un fatto avvenuto. Le specie che fra le sole vie selvatiche vengono da una condizione sono centotrentasette, contate come unione sui titoli.

La seconda prova è l'area monospecie esclusiva, ed è quella che coglie il caso dell'isola: un'area che ospita una specie sola, la quale non compare in nessun'altra area del titolo. Sono quarantanove specie, e fra esse stanno i casi che la comunità nomina da vent'anni, cioè il Wynaut della rotta centotrenta in Rubino, Zaffiro e Smeraldo, il Feebas del luogo trentaquattro come sciame in acqua, lo Smeargle della grotta degli artisti in Smeraldo, gli Unown delle rovine in seconda generazione e lo Shuckle che si ottiene solo spaccando una roccia.

La terza prova è il luogo dedicato, cioè un luogo che ospita una sola specie contando tutte le sue aree. È il criterio più stretto, dà dodici specie, e la sua utilità è che non richiede di guardare il tipo di casella: quando c'è, il solo luogo scritto sul dato basta a stabilire la provenienza.

| Titolo | Aree | Specie selvatiche | Specie solo da condizione | Aree monospecie esclusive |
|---|---|---|---|---|
| Rosso e Blu | 84 | 86 | 0 | 0 |
| Giallo | 91 | 85 | 0 | 0 |
| Oro e Argento | 641 | 137 | 10 | 1 |
| Cristallo | 643 | 147 | 8 | 1 |
| Rubino e Zaffiro | 236 | 113 | 3 | 3 |
| Smeraldo | 248 | 133 | 3 | 5 |
| Rosso Fuoco e Verde Foglia | 279 | 105 | 2 | 1 |
| Diamante, Perla e Platino | 294 | 259 | 6 | 1 |
| Oro HeartGold e Argento SoulSilver | 437 | 244 | 80 | 1 |
| Nero e Bianco | 355 | 231 | 17 | 22 |
| Nero 2 e Bianco 2 | 503 | 286 | 48 | 22 |

Le due righe che saltano all'occhio hanno una spiegazione e non sono un difetto. Le ottanta specie delle riedizioni di seconda generazione vengono dalla zona safari, che in quei titoli è interamente costruita dal giocatore disponendo blocchi e attendendo giorni, quindi la fonte classifica ogni sua area con un tipo proprio e ogni specie che vi si trovi soltanto risulta condizionata. Le quarantotto della seconda coppia di quinta generazione vengono dalle grotte nascoste, che sono il caso più puro della classe: la loro casella si ripopola secondo una condizione e alcune specie non esistono altrove nel gioco.

Il limite di questa misura va dichiarato perché ne cambia la lettura: le tabelle selvatiche non contengono incontri fissi, doni e scambi, quindi la frase unica via nel gioco vale sulle vie selvatiche e non su tutte. Una specie che qui risulta ottenibile solo da una condizione può essere altrove un dono, e il caso è concreto: il Wynaut ha in Rubino, Zaffiro e Smeraldo anche un uovo consegnato al centro termale, che è un incontro fisso e non un'area.

## Che cosa dice ADR-049 su queste due classi, e la domanda che resta all'utente

Il criterio accolto il 2026-09-08 dice che si produce un esemplare quando la sua sola via di provenienza non esiste più. Applicato alla lettera alle due classi, il criterio le esclude quasi tutte, e la ragione è la stessa per entrambe: l'utente possiede le cartucce, quindi la via esiste. Uno scambio in gioco si ottiene giocando il titolo che lo contiene, e un incontro condizionato si ottiene attendendo la condizione.

Le eccezioni che il criterio riconosce subito sono tre, e sono già enumerate. I ventidue scambi del Ranch, la cui applicazione stava nel negozio in rete di una console dismessa. I quattro scambi dei due giochi da console fissa, che richiedono titoli e una console che il progetto non ha, e qui la formulazione onesta è che la via esiste nel mondo ma non per noi, che è una cosa diversa dalla via chiusa e va tenuta distinta. E le voci delle riedizioni per console corrente, che non hanno scadenza affatto.

Resta però una tensione che il criterio non risolve e che va portata all'utente invece di essere decisa qui, perché è una decisione di perimetro. Alcune di queste vie esistono e sono praticamente impercorribili nei centosettanta giorni che restano: l'isola compare in un giorno su decine di migliaia secondo il valore di personalità di un esemplare posseduto, le caselle del Feebas sono sei su quattrocentonovanta e si spostano, la zona safari delle riedizioni di seconda generazione richiede giorni di attesa per ogni blocco disposto. La domanda è se una via aperta ma non percorribile entro la scadenza vada trattata come chiusa ai fini della produzione. Il progetto ha già un precedente utile in senso contrario, cioè la decisione di non produrre i leggendari ordinari perché catturarli è migliore su ogni asse che interessi; e ne ha uno in senso favorevole, cioè che la scadenza è l'unico vincolo che il progetto non controlla. La risposta non è tecnica.

## Che cosa resta da fare su queste due classi

Il confronto riga per riga fra le nostre duecentotrentotto voci di scambio e le duecentotrentotto della fonte comunitaria, che oggi è una coincidenza numerica e non un accordo misurato, e che per il criterio di ADR-044 va misurato nei due versi.

La proiezione delle due classi sulla lista di spunta, che oggi non le contiene: gli scambi sotto scadenza sono le voci dalla prima alla settima generazione escluse quelle delle riedizioni per console corrente, e gli incontri condizionati vanno proiettati con la loro terna invece che con la sola specie, perché è la terna a essere il collezionabile.

L'estensione del censimento condizionato agli incontri fissi e ai doni, che chiuderebbe il limite dichiarato sopra e trasformerebbe la frase unica via selvatica nella frase unica via, che è quella che serve alle decisioni.

E la verifica di una affermazione che tocca direttamente questa materia e che il progetto ha già registrato altrove: nello Studio 03 del track sull'esecuzione di codice sta scritto, su testimonianza dell'autore degli strumenti nel 2024, che gli esemplari dell'Isola Miraggio non si trasferiscono perché non nascono da un evento che li renda legittimi. Va stabilito se quell'affermazione riguardi gli esemplari composti con quella provenienza, che è la lettura più probabile e coerente con il resto di quello studio, oppure anche quelli catturati sull'isola per via di gioco, che sarebbe un fatto sorprendente e cambierebbe il valore dell'intera classe.
