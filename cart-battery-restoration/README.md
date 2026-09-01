# Sottoprogetto: conservazione del supporto e sostituzione della batteria

Sostituire la batteria tampone delle cartucce di prima e seconda generazione, cominciando da Rosso e Argento, conservando il salvataggio che vi si trova. Il track nasce il 2026-09-01 su richiesta dell'utente e serve l'obiettivo dichiarato del progetto per una via che nessuno degli altri track copre: gli altri spostano un esemplare, questo evita che l'esemplare scompaia prima che qualcuno lo sposti.

## Perché è un track a sé, e perché ha una scadenza che non si legge sul calendario

Gli altri sette track hanno una scadenza esterna o nessuna. Questo ne ha una che non è annunciata da nessuno e non è la stessa per due cartucce diverse: la carica residua di una pila al litio saldata dentro una cartuccia nel 1998. Quando finisce, il salvataggio non si degrada e non si corrompe: cessa di esistere, e nessuno strumento lo recupera. Il track esiste perché quella è la sola perdita, fra tutte quelle che questo progetto affronta, che non si può rimediare dopo.

La sua materia non è un formato di dati e non è un protocollo, ed è la ragione per cui non sta dentro un altro track. È il supporto fisico: una memoria statica volatile, una pila che la tiene alimentata quando la console è spenta, e due saldature. Il ponte fra generazioni legge quei salvataggi, la correzione di Smeraldo li scrive, e nessuno dei due si occupa di ciò che li tiene in vita.

## La domanda dell'utente, e la risposta

La domanda era se si possa riprendere un salvataggio dopo il guasto della batteria. La risposta è no, e va data senza attenuazioni perché una speranza mal fondata fa perdere il tempo che serve alla sola azione utile. Il salvataggio vive in una memoria che perde il contenuto quando perde l'alimentazione: quando la pila non tiene più la tensione di ritenzione, i bit non sono danneggiati ma assenti, e non esiste strumento, servizio o laboratorio che li ricostruisca.

Ciò che si può fare è tutto prima, e la finestra si chiude in silenzio. Le tre cose che contano stanno in `STUDIO-01-batteria-e-ritenzione.md`: come sapere quanta finestra resta, come estrarre il salvataggio finché c'è, e come rimetterlo dentro dopo la sostituzione. Su una delle due cartucce, quella di seconda generazione, esiste anche un segnale d'allarme che il gioco stesso mostra, e riconoscerlo è la differenza fra arrivare in tempo e non arrivare.

## Che cosa c'è in questa cartella

`STUDIO-01-batteria-e-ritenzione.md` è il documento da leggere, ed è un runbook e non uno studio: contiene la diagnosi dello stato della pila, la procedura di estrazione con il lettore, il trabocchetto di tensione che può cancellare il salvataggio prima che si sia fatto alcun backup, la sostituzione, e il ripristino con il seguito specifico della seconda generazione.

Non c'è codice. Gli strumenti sono quelli che il progetto ha già, cioè il lettore di cartucce con il suo software, e per la parte di seconda generazione l'editor di salvataggi che il registro delle fonti già elenca.

## Il punto che governa il track

L'operazione è irreversibile due volte, e vale distinguerle perché si prevengono in modi diversi. La prima irreversibilità è quella comune a tutto il progetto, cioè che una scrittura sbagliata sovrascrive. La seconda è propria di questo track e non ha analogo altrove: staccare la pila mentre la memoria dipende da essa cancella il contenuto nell'istante in cui il contatto si apre, e nessun backup fatto dopo serve a nulla. Da qui l'ordine dei passi, che non è una preferenza ma un vincolo: prima si estrae, poi si verifica ciò che si è estratto, poi si tocca il ferro.

## Perimetro

Vale tutto ciò che `.claude/rules/hardware-and-perimeter.md` prescrive, e in particolare il backup in doppia copia su percorsi distinti prima di ogni scrittura, e il read-back verificato dopo.

Un punto è specifico di questo track e va dichiarato qui. La saldatura è un'operazione manuale che l'agente non può eseguire né osservare, e su una cartuccia posseduta da vent'anni l'errore non è un file da riscrivere ma una piazzola di rame staccata. La procedura dichiara dove finisce l'assistenza tecnica e dove comincia una decisione dell'utente fra farlo da sé e affidarlo a chi lo fa di mestiere, che nella comunità del lettore è un servizio corrente e costa meno di una cartuccia.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| la diagnosi, l'estrazione, la sostituzione e il ripristino | `STUDIO-01-batteria-e-ritenzione.md`, in questa cartella |
| il formato dei salvataggi che si estraggono, byte per byte | `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`, sezioni 3 e 4 |
| il lettore, i driver e la porta seriale | `.claude/context/sub-smeraldo-save-fix.md` e `docs/22-strumenti.md` |
| il protocollo di verifica su hardware reale | `.claude/context/dev-testing.md` |
| le fonti di questo track, con il livello di affidabilità | `SOURCES.md` alla radice, colonna BAT |
| a che punto è il track e qual è il prossimo passo | `.claude/context/sub-cart-battery.md` |

Lo stato canonico del track vive nella scheda, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`. Questo file dice cos'è il sottoprogetto; quelli dicono a che punto è.
