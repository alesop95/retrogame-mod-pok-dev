# Studio 01: la batteria tampone, la ritenzione, e la finestra che si chiude in silenzio

Questa nota è un runbook e non uno studio, e la differenza è che ogni sua affermazione deve essere eseguibile o scartata. È scritta il 2026-09-01 e le sue fonti sono di due tipi: la documentazione del produttore del lettore per la parte di procedura, e la testimonianza di campo del canale di assistenza di quel produttore per la parte di diagnosi e di trabocchetti, che nessuna documentazione scrive perché nessun produttore documenta i modi in cui il proprio strumento distrugge un dato. Quel canale è stato esportato il 2026-08-31 e conta cinquantaquattromilasettecentocinquantuno messaggi; le testimonianze citate qui sono state selezionate per filtro e sono attribuite al loro autore, secondo la disciplina che il progetto si è data sul materiale di terzi.

## 1. Che cosa tiene in vita un salvataggio, e perché muore

Una cartuccia di prima e seconda generazione conserva il salvataggio in una memoria statica ad accesso casuale, che è volatile: mantiene il contenuto soltanto mentre è alimentata. Quando la console è accesa l'alimentazione viene dalla console; quando è spenta viene da una pila al litio a bottone saldata sulla scheda della cartuccia. Non c'è nulla di ridondante e non c'è nulla di persistente: quella pila è l'unica cosa che sta fra un salvataggio di vent'anni e il nulla.

Ne discende il modo in cui la perdita avviene, e va enunciato con precisione perché la parola sbagliata suggerisce una speranza che non esiste. Il salvataggio non si corrompe e non si degrada progressivamente: la memoria ha una tensione minima di ritenzione, e quando la pila scende sotto quella soglia il contenuto cessa di esistere. I bit non sono danneggiati, sono assenti. Nessuno strumento li ricostruisce, nessun servizio di recupero dati li estrae, e la risposta alla domanda se si possa riprendere un salvataggio dopo il guasto della batteria è no.

Sulla soglia esiste una testimonianza numerica, e vale citarla perché trasforma una nozione in una misura: la tensione di ritenzione tipica dei chip impiegati sta fra 1,8 e 2 volt, e chi la riporta aggiunge che oltre quel punto si opera fuori specifica e che conviene sostituire la pila già quando la si misura sui due volt e qualcosa (AlexiG, canale del produttore). Una pila nuova di quel tipo dà circa tre volt. Il margine fra tre e due volt è tutta la finestra, e non si consuma in modo lineare né prevedibile.

## 2. La differenza fra la prima e la seconda generazione, che decide l'ordine delle operazioni

Le due cartucce che questo track deve trattare non sono nella stessa condizione, e trattarle nello stesso ordine sarebbe un errore.

In prima generazione la pila alimenta soltanto la memoria. Il consumo è quello della ritenzione, che è minuscolo, ed è la ragione per cui esistono cartucce del 1998 il cui salvataggio è ancora là: una testimonianza del canale riferisce esattamente questo caso, un salvataggio d'infanzia sopravvissuto perché la pila ha tenuto (JstKillMe).

In seconda generazione la stessa pila alimenta anche l'orologio in tempo reale, che è un carico attivo e non una ritenzione. La conseguenza è che quelle cartucce si scaricano molto più in fretta, e la testimonianza del canale lo dice nella forma più utile, cioè come diagnosi a distanza: se una cartuccia di seconda generazione non ha mai avuto la pila sostituita, è probabile che sia già finita per via dell'orologio e che il salvataggio sia già perduto (NightmareJoker2).

Ne segue l'ordine operativo, che è l'unica raccomandazione di priorità di questa nota: si comincia dalla cartuccia di seconda generazione, perché è quella la cui finestra è più vicina alla chiusura, e non da quella di prima, che statisticamente ne ha di più.

## 3. Il segnale d'allarme della seconda generazione, e come non leggerlo male

I giochi di seconda generazione mostrano un messaggio quando il controllo sull'orologio in tempo reale fallisce, e la dicitura dice che la batteria interna si è esaurita, che il gioco si può giocare ma che gli eventi legati al tempo non avverranno più.

Quel messaggio va trattato come un allarme e non come un verdetto, e le due letture sbagliate sono simmetriche. Non è la prova che il salvataggio sia perduto, perché l'orologio è un carico maggiore della ritenzione e può cedere prima; e non è la prova che il salvataggio sia al sicuro, perché la tensione è un continuo e non un interruttore. La sola conclusione corretta è operativa: se quel messaggio compare, la finestra è nella sua fase terminale e l'estrazione va fatta subito, prima di qualunque altra cosa, compresa la lettura del resto di questa nota.

## 4. La diagnosi, in due prove che costano nulla

La prima prova non richiede alcuno strumento e viene da chi assiste su quel canale (Lesserkuma). Si crea un salvataggio nuovo sulla cartuccia, si spegne, si attende almeno cinque minuti, si riaccende e si guarda se il salvataggio c'è ancora. Se non c'è, la pila è finita. La ragione per cui l'attesa deve essere di minuti e non di secondi è che una pila agonizzante mantiene il contenuto per un tempo breve dopo lo spegnimento, e una prova fatta in dieci secondi darebbe un falso rassicurante.

Va detto quando questa prova si può fare e quando no, perché è il genere di dettaglio che rovina tutto. Si può fare soltanto su una cartuccia il cui salvataggio non interessa, oppure dopo che il salvataggio che interessa è già stato estratto e verificato. Creare un salvataggio nuovo su una cartuccia che porta il salvataggio da salvare significa sovrascriverlo, e su una cartuccia agonizzante è anche l'ultima operazione che quella pila vedrà.

La seconda prova richiede un multimetro e si fa a cartuccia aperta, misurando la tensione ai capi della pila. Tre volt e qualche centesimo è una pila sana; poco più di due volt è una pila alla fine della sua finestra; sotto i due volt si è già fuori specifica e ciò che è dentro la memoria è già perduto o lo sarà a breve. La misura va fatta senza rimuovere la pila, perché rimuoverla è precisamente l'operazione che cancella.

## 5. Il trabocchetto di tensione, che è il pericolo maggiore di tutta la procedura

Questa sezione va letta prima di collegare qualunque cosa, perché descrive un modo di perdere il salvataggio che avviene prima che si sia fatto alcun backup e senza che si sia premuto alcun pulsante.

Le cartucce di prima e seconda generazione funzionano a cinque volt, quelle della generazione successiva a tre virgola tre. Sul lettore di cartucce impiegato da questo progetto, nella revisione in cui la tensione è controllata dal software, l'interfaccia grafica parte in modalità della generazione successiva, cioè a tre virgola tre volt. Una testimonianza del canale riferisce che inserire una cartuccia di seconda generazione mentre il lettore è in quella modalità cancella il salvataggio, e aggiunge il dettaglio che rende il fatto pericoloso: avviene anche senza premere il pulsante di connessione (Reclaimer Shawn). La medesima testimonianza osserva l'asimmetria, cioè che la tensione della generazione precedente non danneggia i salvataggi della successiva mentre il contrario sì.

Il rimedio riferito dalla stessa fonte è una sequenza e non un'impostazione: si connette in modalità prima generazione con il lettore vuoto, si disconnette, si inserisce la cartuccia, e solo allora si connette.

La documentazione del produttore, citata sul canale nella sua formulazione originale, prescrive indipendentemente lo stesso ordine e aggiunge due regole che vanno rispettate insieme a quella. La prima è di selezionare la tensione corretta prima di inserire la cartuccia, e di verificare con il diodo luminoso dedicato che sia effettivamente quella. La seconda è di scollegare il cavo dal dispositivo prima di rimuovere la cartuccia, e non dopo. Da un intervento di chi produce il lettore risulta inoltre che sostituire una cartuccia con l'altra a dispositivo collegato non è raccomandato e può danneggiare il lettore stesso, e che questo sta nel manuale in una sezione che quasi nessuno legge (riferito da EchelonPrime).

Il criterio che ne discende, e che vale oltre questo caso, è che su un dispositivo dove la tensione è scelta dal software il valore predefinito non è mai una garanzia: si verifica sull'indicatore fisico, perché è l'unico testimone che non dipende dallo stesso software che potrebbe avere sbagliato.

## 6. L'estrazione, e la verifica di ciò che si è estratto

L'estrazione del salvataggio è l'operazione che apre la finestra invece di chiuderla, e va fatta per prima. La sequenza, che incorpora la sezione precedente, è questa.

Si collega il lettore al calcolatore e si porta l'interfaccia nella modalità della prima generazione, verificando l'accensione del diodo corrispondente. Si disconnette. Si inserisce la cartuccia. Si connette e si legge il salvataggio.

Sulla verifica di ciò che si è ottenuto vale la regola generale del progetto, cioè che un'operazione riuscita secondo il software non è un'operazione verificata, e in questo caso esiste un modo diretto di verificarla che una testimonianza del canale illustra per contrasto: chi ha estratto un salvataggio di duecentocinquantasei byte da una cartuccia giocata per vent'anni ha sospettato correttamente che non fosse il suo salvataggio, e ha chiesto prima di sovrascrivere qualcosa (Sonofskywalker3). La verifica giusta è quindi in due parti. La prima è la dimensione, che deve corrispondere a quella attesa per quel titolo e non a un frammento. La seconda è aprire il file estratto in un emulatore, o negli strumenti di questo progetto, e riconoscervi la propria partita: il nome dell'allenatore, il numero di medaglie, ciò che si ricorda di avere avuto in squadra.

Il salvataggio verificato va poi in doppia copia su due percorsi distinti, secondo la norma del progetto, e questo è il momento in cui la parte irreversibile della procedura diventa sicura. Nessuna delle due copie entra nel repository.

## 7. La sostituzione, e dove finisce l'assistenza tecnica

Sul componente il progetto ha una risposta di campo e una regola. La risposta di campo è che le cartucce di questa famiglia usano una pila da tre volt del formato CR2025, e che il formato CR2032, un poco più spesso, funziona ugualmente purché sia della variante con le linguette (orangeglo, makho, sul canale del produttore); su altre famiglie di cartucce compaiono i formati CR1616 e CR1620, e una testimonianza riporta il CR1616 nella scheda tecnica di una cartuccia specifica (Ender). La regola che ne discende è la sola cosa da ricordare: il valore si legge sulla pila che sta dentro la cartuccia, prima di ordinare, e non su una guida, perché le revisioni di scheda differiscono e una guida non sa quale sia la propria.

Sulla variante con le linguette non c'è scelta e la ragione è fisica. Una pila a bottone non si salda sul corpo: il calore necessario la fa sfiatare, e nel caso migliore la si rovina. Si salda sulle linguette, che sono già fissate alla pila da chi l'ha prodotta, oppure si monta un porta-pila e si salda quello, che è la soluzione preferibile perché rende la sostituzione successiva un gesto senza saldatore. Una testimonianza del canale segnala anche che la lega con piombo è più facile da lavorare per chi non lo fa di mestiere, e che il flussante aiuta più di quanto si pensi (xukkorz).

Qui finisce l'assistenza che questo progetto può dare, e va dichiarato invece di essere aggirato. La saldatura è manuale, l'agente non la esegue e non la osserva, e su una cartuccia di vent'anni l'errore non è un file da riscrivere ma una piazzola di rame staccata dalla scheda. Esiste un'alternativa corrente e va nominata perché è ragionevole: nella comunità del lettore il servizio di sostituzione con prova e spedizione di ritorno è offerto per una cifra dell'ordine dei venti dollari (imod.systems, con un commento di Lucy che la giudica un buon prezzo), cioè meno di quanto costi una cartuccia di quei titoli. La scelta fra farlo da sé e affidarlo è dell'utente; ciò che non è una scelta è farlo prima di avere estratto e verificato il salvataggio.

Una testimonianza va riportata come contro-esempio e non come pratica: chi ha rimosso la pila facendo leva e ha fissato la nuova con nastro isolante racconta di averlo fatto e di volerlo rifare come si deve ora che ha gli strumenti (gokumon). Funziona finché il contatto tiene, e il giorno in cui non tiene il salvataggio è perduto senza preavviso.

## 8. Il ripristino, e il seguito che riguarda la sola seconda generazione

Rimessa la pila, la cartuccia è di nuovo in grado di conservare un salvataggio, e il salvataggio estratto si riscrive con lo stesso lettore. Vale la norma del progetto sul read-back: dopo la scrittura si rilegge e si confrontano i byte, e soltanto dopo si accende la console per il controllo di aspetto, che è la terza verifica e non la prima.

Sulla seconda generazione la procedura non finisce qui, e questa è la parte che chi la salta scopre giorni dopo. Con la pila nuova l'orologio in tempo reale riparte, ma il salvataggio conserva l'istante in cui l'orologio si era fermato, e tutto ciò che nel gioco dipende dal tempo trascorso resta ancorato a quell'istante. Una testimonianza descrive il sintomo in modo riconoscibile: l'orologio scorre, ma ricaricando il salvataggio l'ora torna sempre allo stesso valore, che è quello dell'ultimo salvataggio prima del guasto (Cari).

La sequenza completa la riporta un'altra testimonianza del canale, ed è in tre passi con due deroghe dichiarate (FexCollects). Si sostituisce la pila, cosicché l'orologio riparta. Si corregge nel salvataggio, con l'editor che il registro delle fonti già elenca, lo scostamento dell'ora, che il gioco fissa una volta sola all'inizio della partita. Si imposta l'orologio alla data corrente, cosicché gli eventi a durata si aggiornino. Il secondo passo si può omettere se non importa che l'orologio dentro il gioco sia corretto; il terzo si può omettere se non importa degli eventi a durata già avviati, perché quelli nuovi funzionerebbero comunque.

Va registrato che il medesimo problema esiste in terza generazione e che il progetto lo incontrerà sul track di Smeraldo: una testimonianza riferisce che la sostituzione della pila ha alterato i tempi di crescita delle bacche e la definisce un problema comune (Speedy77). Non è una novità di questa nota ma un rinvio: quando quel track arriverà alla scrittura, questa sezione è il posto dove la conoscenza è già.

## 9. Che cosa resta aperto

Se le due cartucce di questo track siano nella condizione che la sezione due descrive per la loro generazione, oppure no. È una misura e non una congettura, e si fa con la seconda prova della sezione quattro: finché non è fatta, tutto il resto di questa nota è preparazione.

Quale sia il valore effettivo della pila dentro ciascuna delle due cartucce. Si legge sulla pila, e va letto prima di ordinare.

Se il salvataggio di seconda generazione esista ancora. La sezione due dà la probabilità e non la risposta, e la risposta si ottiene aprendo il gioco e guardando, che è la sola operazione che non consuma nulla.

Se lo scostamento dell'ora della seconda generazione si corregga con l'editor già in uso nel progetto oppure richieda un passaggio ulteriore. La testimonianza lo dà per fatto con quell'editor; il progetto non l'ha verificato.
