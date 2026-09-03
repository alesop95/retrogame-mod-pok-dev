# Studio 02: i salvataggi di provenienza esterna, e che cosa provano davvero

> Nota di studio del 2026-09-02. Nasce da una raccolta di trenta file consegnata dall'utente, scaricata da un archivio di salvataggi contribuiti dagli utenti e da tre forum italiani, e messa in `_notes/salvataggi/`, che non entra nel controllo di versione. L'inventario generato accanto a questa nota è `CENSIMENTO-SALVATAGGI.md`, e si rigenera con `tools/verifica-salvataggi.py`.

## 1. Le tre domande, e perché tenerle separate

Un salvataggio scaricato da terzi pone tre domande, e la confusione fra loro è il modo tipico di sbagliare su questo materiale.

La prima è se il file sia strutturalmente un salvataggio funzionante del gioco che dichiara di essere. È una domanda su byte e somme di controllo, ha una risposta binaria, e si risponde con un programma.

La seconda è che cosa contenga, cioè quali esemplari porti e quindi quali specie contribuirebbe all'obiettivo di questo progetto. È una domanda di censimento, ha una risposta numerica, e si risponde con lo stesso programma.

La terza è se sia lecito usarlo. Non è una domanda tecnica, non ha una risposta che un programma possa dare, e la sua sede è `.claude/rules/hardware-and-perimeter.md`, che su questo materiale è normativa e restrittiva. Uno strumento che rispondesse anche a questa nasconderebbe una decisione dentro un calcolo, ed è la ragione per cui `tools/verifica-salvataggi.py` chiude ogni sua corsa dichiarando esplicitamente ciò che il proprio esito non dice.

## 2. Il pericolo, e perché la rassicurazione comune è quella sbagliata

L'utente ha passato la raccolta a un antivirus, con esito pulito, e vale spiegare perché quell'esito, benché rassicurante, non è la rassicurazione che serve.

Un salvataggio è dato e non codice. Non viene eseguito da nulla: viene letto da un gioco che ne interpreta i campi, oppure da un editor. Non può quindi contenere un programma dannoso nel senso in cui lo contiene un allegato eseguibile, e un antivirus su questi file non trova nulla perché non c'è nulla del genere da trovare. L'esito pulito è la conferma di una cosa che era già vera per costruzione, non l'esclusione del rischio effettivo.

I rischi effettivi sono altri tre, e nessuno dei tre è visibile a un antivirus.

Il primo è un file malformato, che il gioco rifiuta all'avvio oppure accetta e poi corrompe. Si esclude verificando le somme di controllo che ciascun formato porta, ed è precisamente ciò che lo strumento fa: le trenta voci della raccolta sono state tutte riconosciute e tutte hanno le somme che tornano, quindi questo rischio è chiuso per tutte e trenta.

Il secondo è un esemplare costruito per innescare un difetto del gioco, di cui la cosiddetta Uovo Peste è l'esemplare classico. Si riconosce dai campi incoerenti, e lo strumento censisce e segnala il bit che il gioco stesso usa per marcare una struttura corrotta; nessuna delle strutture lette lo porta. Va detto con precisione che questa non è una verifica di legittimità, che resta di PKHeX: è un controllo di coerenza strutturale, che è meno.

Il terzo non è tecnico, ed è il più importante dei tre: usare esemplari di altri sul proprio account. Ne parla la sezione 5.

## 3. Come si identifica un salvataggio senza credere al nome del file

Il nome di un file scaricato è una dichiarazione di chi lo ha caricato, non un dato. Lo strumento non gli crede, e procede in due passi che vale descrivere perché sono il medesimo metodo già usato in questo progetto per identificare il gioco di un salvataggio di terza generazione.

La dimensione restringe la famiglia, perché ogni supporto ha la propria: trentaduemila byte per la prima generazione su Game Boy, centotrentunomila per la terza su Game Boy Advance, cinquecentoventiquattromila per il Nintendo DS, e tre valori distinti per i salvataggi decifrati di Nintendo 3DS. Dentro la famiglia si prova ciascun candidato con il predicato che la fonte usa per distinguerli, e si riferisce quale ha risposto e quali no.

I predicati sono letti dal sorgente di PKHeX il 2026-09-02 e non inventati, e la distinzione conta: un predicato inventato che per caso funzioni su un file è indistinguibile da uno giusto, e la differenza si vede soltanto sul file successivo. Per la quarta generazione la prova è che nel piede del blocco generale il campo della dimensione coincida con la dimensione del blocco e che la parola seguente sia una delle due magie note, e poiché la dimensione del blocco generale differisce fra Diamante e Perla, Platino, e i due giochi di Johto, la prova identifica anche il gioco. Per la quinta è il CRC a sedici bit del piede, con due lunghezze diverse per i due gruppi di titoli. Per la sesta e la settima è una firma di coda comune, e a distinguere i titoli resta la dimensione. Per la prima generazione sono due liste di Pokemon a offset noti, di cui si verifica che il contatore stia entro il massimo e che il byte successivo sia il terminatore, con offset diversi per le versioni internazionali e per quelle giapponesi: è così che i quattro salvataggi giapponesi della raccolta si sono identificati come tali, e uno dei quattro come versione Giallo.

Un caso vale segnalare perché è un'ambiguità reale e non un dettaglio. Rubino Omega e Zaffiro Alpha su Nintendo 3DS hanno esattamente la dimensione di Pokemon Box su GameCube, cioè 483328 byte. I due si distinguono perché il secondo, nella raccolta, arriva dentro un file di scheda di memoria con la propria intestazione di sessantaquattro byte, e perché porta la propria somma di controllo dove l'altro porta la firma di coda: lo strumento verifica entrambe le cose, invece di decidere sulla dimensione.

## 4. Che cosa la raccolta contiene, in numeri

Il censimento sta in `CENSIMENTO-SALVATAGGI.md`, che è generato. Qui stanno i tre fatti che ne discendono e che contano per la roadmap.

Il primo è che la raccolta è integra e identificata: trenta file su trenta riconosciuti, con le somme di controllo che tornano, e ciascuno del gioco che dichiarava di essere. Nessuna discrepanza fra il nome del file e il suo contenuto.

Il secondo è la copertura, ed è il numero che serve all'obiettivo. L'unione delle specie presenti come esemplare in questa raccolta copre trecentottantacinque delle trecentottantasei voci nazionali di terza generazione. Manca una voce sola, ed è Poochyena, numero nazionale 261. La verifica dell'assenza è stata fatta due volte, perché una lacuna su una specie comune di Hoenn è più facilmente un difetto della corrispondenza fra le numerazioni che un dato: l'identificativo interno di Poochyena è 286, gli identificativi 285 e 287 sono presenti, il 286 no. L'assenza è reale.

Il terzo riguarda proprio quella verifica, e ha prodotto un difetto nel nostro codice che va raccontato perché è di una specie che questo progetto ha imparato a temere. Vedi la sezione 6.

## 5. La questione di perimetro, esposta una volta

La regola del progetto è che i salvataggi scaricati da internet non si importano su questa console, e la motivazione dichiarata è che sono la causa principale dei ban quando poi vengono usati online o depositati sul servizio di deposito, con il rischio che ricade sull'account e sulla console e non sul file. La regola prevede anche la sua eccezione, e la prevede in una forma precisa: se un giorno servisse importarne uno, la decisione va presa esplicitamente e registrata come ADR, non fatta scivolare dentro un altro lavoro.

Il lavoro corrente incontra quella eccezione in tre punti distinti, che è utile tenere separati perché hanno pesi diversi.

Il primo è lo sbloccaggio del Parco Amici. L'utente ha già indicato questa direzione, cioè iniettare in una cartuccia di quarta generazione un salvataggio che abbia il Parco Amici già disponibile, per non dover completare tre giochi prima di poter cominciare a trasferire. Ciò che entra nel percorso, in questo caso, non è alcun esemplare: è uno stato di avanzamento. Nessun Pokemon di terzi arriva a destinazione.

Il secondo è l'uso di questi salvataggi come banco di prova. Un salvataggio integro di ciascun gioco della catena è materiale di verifica di prima qualità, perché permette di provare la lettura e la scrittura di un formato senza toccare le cartucce dell'utente, che sono irreversibili, e senza attendere il lettore. Anche qui nessun esemplare di terzi va da nessuna parte.

Il terzo è l'unico che tocca davvero la regola: prendere esemplari da questi salvataggi e farli arrivare nel deposito. Su questo va detta una distinzione che il progetto ha già costruito per altri fini e che qui serve intera. Il progetto distingue legale da legittimo; questo caso introduce un terzo asse, cioè proprio. Un esemplare di un salvataggio altrui può essere perfettamente legittimo, nel senso che un verificatore non ha nulla da contestargli, e restare non proprio, nel senso che porta il nome e l'identificativo di un altro allenatore e nel gioco figura come ricevuto in scambio. I due assi sono indipendenti, e l'obiettivo dichiarato di questo progetto, cioè una collezione con la cronologia possibile, riguarda il secondo almeno quanto il primo.

Ne segue una raccomandazione, che resta una raccomandazione e non una decisione, perché la decisione è dell'utente. Le prime due vie sono compatibili con l'obiettivo e non richiedono alcuna eccezione alla regola, perché non fanno entrare esemplari. La terza è una scelta sul significato della collezione prima che sul rischio, e va decisa come tale, cioè per ADR e con la sua motivazione scritta.

## 6. Il difetto di Nidoran, cioè una normalizzazione che cancella ciò che distingue

Censendo i depositi, una specie su trecentottantacinque risultava priva di corrispondenza fra la numerazione interna e quella nazionale. La causa non era nei salvataggi.

La funzione che costruisce la corrispondenza confronta i nomi delle specie fra due fonti, e per confrontarli li normalizza togliendo tutto ciò che non sia lettera o cifra. Fra i caratteri così rimossi ci sono i due segni di sesso, che nei nomi di due specie della prima generazione non sono decorazione ma identità: Nidoran femmina e Nidoran maschio diventano la medesima chiave, il primo dei due vince, e il numero nazionale 32 finisce a puntare sull'identificativo interno di Nidoran femmina.

La gravità va misurata per ciò che è. Non è un errore di arrotondamento: è attribuire a un numero nazionale la specie sbagliata, che su questo dato è il difetto peggiore possibile, ed è esattamente quello contro cui il commento di quella stessa funzione metteva in guardia citando il caso di Latias. La funzione aveva dentro il difetto da cui dichiarava di proteggere.

Va altresì detto con precisione che il lotto dei centosettantadue esemplari prodotti non ne è stato toccato, e non per fortuna nostra ma per un fatto verificabile: nessuna voce del catalogo degli eventi di terza generazione è un Nidoran, quindi quella riga della corrispondenza non è mai stata interrogata dal generatore. Un difetto che non ha ancora colpito resta un difetto, e la ragione per cui va corretto subito è che la corrispondenza non appartiene al generatore: appartiene al progetto, e il primo uso nuovo che se ne è fatto lo ha attivato.

La correzione è in due parti, e la seconda vale più della prima. La prima è tradurre i due segni in lettere distinte invece di cancellarli, così che le chiavi restino due. La seconda è controllare le due proprietà che la corrispondenza deve avere e che nessuno controllava: che due nomi diversi non producano la medesima chiave, e che due numeri nazionali non finiscano sul medesimo identificativo interno. Sono due righe, entrambe fanno arrestare il programma con la ragione scritta, ed entrambe avrebbero colto questo difetto il giorno in cui fu introdotto. La corrispondenza oggi porta trecentottantasei numeri nazionali su trecentottantasei identificativi interni distinti, e la iniettività è verificata a ogni corsa invece di essere sperata.

La lezione generale è la stessa che la campagna di verifica degli eventi aveva già insegnato in un'altra forma. Il difetto non stava dove il problema era difficile, cioè nel confronto fra due fonti che numerano le specie in modo diverso, che era stato studiato e documentato: stava in una riga di normalizzazione del testo, considerata così ovvia da non meritare un controllo. E si è manifestato non come un errore ma come un numero leggermente sbagliato in un rapporto, cioè nella forma che passa una revisione a video.

## 7. A che cosa serve ciascun pezzo della raccolta

Non tutti i trenta file servono alla stessa cosa, e vale scriverlo perché la raccolta è eterogenea e trattarla come un blocco unico sprecherebbe la parte utile.

I sei salvataggi di terza generazione con il deposito popolato sono materiale di confronto per il nostro generatore e per il nostro lettore. Il salvataggio dei quattrocentoventisei Metang in particolare è un banco di prova ideale per la lettura del deposito, perché ha un contenuto noto, omogeneo e in quantità: un lettore che ne conti quattrocentoventi in quattordici scatole ha dimostrato di indirizzare correttamente le nove sezioni del deposito e la struttura da ottanta byte, e un lettore che ne conti quattrocentoventuno o quattrocentodiciannove ha un difetto di un elemento che su un deposito eterogeneo non si sarebbe visto.

L'archivio dei trecentonovanta esemplari cromatici e quello delle ventotto forme di Unown sono la stessa cosa in forma più comoda, cioè esemplari singoli invece che dentro un salvataggio, e sono il riferimento naturale per il confronto con l'elenco delle specie da completare. Le ventotto forme di Unown, in particolare, sono un dato che il nostro catalogo non copre e che riguarda direttamente la questione delle forme alternative nel deposito.

I salvataggi di quarta generazione, cioè i due di Diamante e Perla, i tre di Johto e quello di Platino, sono i candidati per lo sbloccaggio del Parco Amici, e sono sei invece di uno, che è una ridondanza utile perché la lingua di ciascuno va verificata prima dell'uso.

Il salvataggio di Pokemon Box su GameCube è la fonte che l'utente ha indicato per un controllo di completezza sull'elenco delle specie, e la sua descrizione dichiara di contenere tutto ciò che in terza generazione si può ancora ottenere legittimamente, esemplari ombra e distribuzioni comprese. Lo strumento ne verifica la somma di controllo e lo identifica; il censimento del suo deposito non è ancora fatto, perché il formato del deposito di quel gioco differisce da quello delle cartucce e va letto sulla fonte prima di essere scritto.

I cinque salvataggi di Nintendo 3DS coprono X e Y, Rubino Omega e Zaffiro Alpha in due copie ciascuno, e UltraSole. Sono il materiale con cui si potrà provare la lettura dei formati di sesta e settima generazione senza toccare le cartucce che l'utente possiede.

## 8. Che cosa resta da fare su questo materiale

Tre cose, in ordine di resa.

Verificare la lingua di ciascun salvataggio di quarta e quinta generazione, perché ogni passaggio della catena verso il deposito pretende la stessa lingua ai due capi e l'utente possiede cartucce italiane. Lo strumento oggi riferisce soltanto la distinzione fra coreano e non coreano, che è quella che la magia del piede permette; la lingua vera sta altrove nel blocco generale e va letta sulla fonte.

Censire il deposito dei salvataggi di quarta, quinta, sesta e settima generazione, che oggi non è censito. Per la quarta e la quinta la struttura dell'esemplare è nota e documentata, e il lavoro è indirizzare il deposito dentro il blocco di memoria giusto; per la sesta e la settima il deposito è cifrato con un meccanismo diverso e il lavoro è maggiore.

Censire il deposito di Pokemon Box, che è la fonte più interessante delle trenta per la domanda che l'utente ha posto, cioè se il nostro elenco di specie di terza generazione abbia lasciato fuori qualcosa.
