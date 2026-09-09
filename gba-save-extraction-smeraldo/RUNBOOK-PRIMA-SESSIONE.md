# Runbook della prima sessione con il lettore di cartucce

Il lettore GBxCart RW v1.4 Pro è arrivato il 2026-09-09. Questo documento è la sequenza della prima sessione, e serve a una cosa sola: mettere in ordine operazioni che appartengono a tre track diversi, cosicché l'ordine sia quello del rischio e non quello della curiosità. La procedura di dettaglio non si duplica qui: sta nelle sezioni 3.2, 4 e 5 dell'handoff del track, e le norme che governano ogni scrittura stanno in `.claude/rules/hardware-and-perimeter.md`, che è normativa e va riletta prima di collegare qualsiasi cosa.

## Il principio che decide l'ordine

Non si comincia da ciò che interessa di più ma da ciò che si può perdere. Delle cose che il lettore rende possibili, una sola ha una finestra che si chiude da sé: l'estrazione dei salvataggi delle cartucce di prima e seconda generazione, che vivono in una memoria alimentata da una pila saldata nel 1998 e che cessano di esistere quando quella pila finisce. Tutto il resto attende senza degradare. Il salvataggio di Smeraldo sta in memoria flash e non dipende da alcuna pila, quindi domani è come oggi; le ROM sono di sola lettura e non si consumano; il ponte fra generazioni ha bisogno di dati reali ma non ha scadenza propria.

Da qui l'ordine dei quattro tempi, e la ragione per cui il primo non è il track che l'utente segue da più tempo.

## Tempo zero: il cancello dei driver

Non si collega la cartuccia prima che il collegamento del lettore sia dimostrato. Il criterio è quello della sezione 5.4 dell'handoff: in Gestione Dispositivi, sotto Porte COM e LPT, compare una voce del tipo USB-SERIAL CH340 con il numero di porta, senza punto esclamativo giallo, e la porta assegnata va annotata perché FlashGBX la chiede. Se la voce non compare, si installano i driver da wch-ic.com come la sezione 5.2 indica e si ripete la verifica.

Il motivo per cui questo è un cancello e non un passo: un collegamento intermittente durante una lettura produce un dump troncato che sembra valido, e un dump troncato usato come backup è peggio di nessun backup.

## Primo tempo: i salvataggi che hanno una finestra

Si estraggono i salvataggi delle cartucce di prima e seconda generazione, una per volta, cominciando da quelle di seconda perché la loro pila alimenta anche l'orologio e si scarica prima.

Va ricordato ciò che il progetto ha già stabilito il 2026-09-01, per non cercare ciò che non c'è: su Rosso e Argento la diagnosi è conclusa e negativa, perché entrambe offrono all'accensione il solo avvio di una partita nuova e non conservano ciò che si crea, che è la firma della pila esaurita. Quei due salvataggi non esistono più. L'estrazione riguarda quindi le eventuali altre cartucce di quelle generazioni, e il primo passo su ciascuna non è la lettura ma la prova di ritenzione: si accende, si verifica se un salvataggio esista, e solo se esiste si estrae.

Su ogni salvataggio estratto valgono i due presidi della regola. Il backup è in doppia copia su due volumi distinti, verificato leggibile prima di considerare fatta l'operazione. E la lettura si ripete una seconda volta confrontando i byte delle due letture: due letture identiche sono una lettura verificata, una sola lettura è una speranza.

C'è un presidio in più che nasce dal risultato più importante del track della conservazione, e va applicato qui perché riguarda proprio questo hardware: nella revisione in cui la tensione è controllata dal software l'interfaccia parte a tre virgola tre volt, e una testimonianza del canale del produttore riferisce che inserire una cartuccia di seconda generazione in quella condizione cancella il salvataggio, anche senza premere il pulsante di connessione. La sequenza corretta sta nella sezione 5 del runbook della pila, e va eseguita prima di inserire qualunque cartuccia di quelle due generazioni.

## Secondo tempo: Smeraldo, che è il track dell'utente

Si estrae il salvataggio della cartuccia di Smeraldo con FlashGBX, in sola lettura, con la stessa doppia copia e la stessa doppia lettura. Poi, e soltanto poi, si apre il file con gli strumenti che il progetto ha già scritto, che non scrivono nulla.

Il primo è `tools/emerald_bag_decode.py`, che valida le sezioni, sceglie lo slot più recente, identifica il gioco confrontando le prove dei tre candidati, smaschera le quantità dello zaino e riferisce cinque classi di anomalia. La scoperta che governa questa lettura è che in Smeraldo le quantità dello zaino sono in XOR con la chiave di sicurezza a 32 bit della sezione zero: una quantità assurda letta in chiaro non è una prova di corruzione ma l'aspetto normale di un dato mascherato, mentre una quantità assurda nel deposito PC, che non è mascherato, è un'anomalia vera.

Il secondo è `tools/verifica-salvataggi.py`, che dice quali specie il salvataggio contenga nei depositi: serve al track del catalogo e non a quello dello zaino, e conviene farlo nella stessa sessione perché il file è già in mano.

Solo dopo questa lettura si decide che cosa correggere, e la decisione appartiene all'utente: quali slot e quali oggetti della tasca degli strumenti base vadano riportati a che cosa. La forma del difetto è già nota, cioè una sostituzione che comincia a un certo slot e prosegue con identificativi nell'intervallo delle Ball, quindi la correzione è una riscrittura di identificativi e non un riordino della tasca.

Prima di qualunque scrittura sulla cartuccia valgono i due vincoli non negoziabili della regola: il backup deve esistere in doppia copia verificata, e dopo la scrittura si rilegge il contenuto e si confronta con ciò che si intendeva scrivere, byte per byte e non a occhio sulla schermata di gioco. Una scrittura che il software dichiara riuscita e che nessuno ha riletto non è una scrittura verificata.

## Terzo tempo: le ROM, che servono al ponte

Si dumpano le ROM delle cartucce possedute, che è un'operazione di sola lettura e senza rischio per il salvataggio. Servono a due cose che il progetto aveva dichiarato bloccate: il collaudo del protocollo del ponte contro un gioco vero, e la prova da un capo all'altro su dati reali invece che su vettori costruiti.

Le ROM non entrano nel version control per la regola di dominio del `.gitignore`, e la loro collocazione si annota in prosa nella scheda del track come per i salvataggi.

## Quarto tempo: ciò che l'arrivo sblocca e che non si fa in questa sessione

Tre cose diventano possibili e non vanno impastate con la prima sessione, perché ciascuna richiede il proprio allestimento.

Le tre vie di iniezione di un evento che dipendevano dal lettore sono ora percorribili, e la scelta fra esse appartiene al track delle distribuzioni.

Le sessanta voci del lotto che prendono l'identificativo dall'allenatore del salvataggio ricevente vanno rigenerate con l'identificativo reale, che si conosce appena il salvataggio di Smeraldo è stato letto. Cambieranno seme e valore di personalità, e il giudizio già ottenuto resta valido perché esercitava rami di codice e non byte particolari.

L'esecuzione di codice sulle cartucce fisiche resta esclusa da ADR-053 finché non siano soddisfatte le sue tre condizioni. L'arrivo del lettore ne soddisfa la prima; restano il salvataggio estratto in doppia copia verificata, che il primo e il secondo tempo producono, e una prova dell'allestimento condotta su una copia o su una cartuccia sacrificabile. Quando le tre esistono, la decisione di procedere è una decisione nuova.
