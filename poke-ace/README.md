# Sottoprogetto: esecuzione di codice arbitrario come via di generazione

Studiare e, se la decisione lo consentirà, impiegare l'esecuzione di codice arbitrario nei giochi di terza generazione per scrivere dati di Pokemon direttamente nel salvataggio, come via per ottenere ciò che nessuna via di gioco può più dare. Il track nasce il 2026-08-31 su richiesta dell'utente e serve l'obiettivo dichiarato del progetto, cioè la collezione più completa possibile in Pokemon Home.

## Che problema risolve, e in che rapporto sta con gli altri track

L'obiettivo di collezione ha una gamba che nessuna quantità di gioco può coprire: gli anni in cui non si è giocato, e gli eventi a tempo passati. Il progetto ha già un track che affronta quella gamba per una via, cioè `recreate-pokemon-distributions-events/`, che ricrea il meccanismo originale di distribuzione e lo esegue su hardware proprio. Questo track ne affronta un'altra: scrivere i byte dell'esemplare direttamente nel salvataggio, facendo eseguire al gioco codice che il gioco non prevedeva.

La distinzione fra le due vie non è di comodità ma di provenienza, e il capitolo di questo progetto sulla legittimità la enuncia con precisione: un dato prodotto attraverso il percorso previsto è coerente per costruzione, un dato costruito a posteriori è coerente soltanto rispetto ai controlli che il costruttore conosceva. Le due vie producono spesso i medesimi byte e non la medesima storia, e la differenza conta per la ragione che la sezione seguente spiega.

La tecnica in sé non è nuova per il progetto: `docs/09-esecuzione-codice.md` la documenta già, perché il ponte fra generazioni la usa per rimuovere un esemplare dal salvataggio di partenza. Ciò che questo track aggiunge è l'uso di quella tecnica come strumento di generazione invece che di trasferimento.

## Che cosa c'è in questa cartella

`STUDIO-01-ace-e-legalita-in-home.md` è lo studio principale, ed è il documento da leggere per primo. Contiene l'inventario degli strumenti della comunità con la funzione di ciascuno, la risposta verificata alla domanda che decide se questo track sia percorribile, cioè se un esemplare così prodotto sopravviva ai controlli di Pokemon Home, e la notizia del 13 agosto 2026 che cambia il calendario dell'intero progetto.

`STUDIO-02-marchi-di-origine-e-che-cosa-conta-una-collezione.md` chiude con dati uno dei punti che il primo lasciava aperti, cioè la forma dell'informazione di provenienza: è categorica e visibile all'utente, e la terza generazione avrà un marchio proprio per la porta nuova, distinto dall'assenza di marchio che porta un esemplare passato per la catena storica. La medesima nota stabilisce che la lista di controllo indicata dall'utente non è una lista ma un insieme parametrico, con quindici profili la cui cardinalità differisce di un ordine di grandezza, e che l'obiettivo del progetto va quindi precisato scegliendo un profilo invece di essere enunciato come superlativo.

Non c'è codice e probabilmente non ce ne sarà: gli strumenti che servono esistono, sono mantenuti dalla comunità, e riscriverli sarebbe lavoro sprecato. Ciò che questo track produce è conoscenza e procedura.

## Il punto che governa tutto

La domanda non è se la tecnica funzioni, perché funziona ed è documentata. La domanda è se un esemplare prodotto così, portato in Pokemon Home, venga accettato come legittimo, e la risposta verificata è che **nessuno lo sa ancora e lo si potrà sapere solo da ottobre 2026**.

Il rischio dichiarato dal titolare del servizio non è la cancellazione dell'esemplare ma la sospensione dell'accesso a Pokemon Home, temporanea o indefinita a sua discrezione. Ne segue che una decisione va presa esplicitamente prima di usare la tecnica sull'account che custodisce la collezione, e non dentro un altro lavoro. Lo studio espone i termini reali di quella decisione; la decisione è dell'utente.

## Perimetro

Vale tutto ciò che `.claude/rules/hardware-and-perimeter.md` prescrive, e la sezione sui salvataggi di terze parti va riletta prima di procurare qualunque materiale.

Un punto è specifico di questo track e va dichiarato qui perché è la ragione per cui lo studio precede l'uso: la tecnica opera sui dati di un salvataggio proprio, quindi non tocca il perimetro dell'hardware posseduto, ma il suo esito attraversa un servizio in linea di terzi le cui condizioni d'uso vietano i dati alterati. Il confine fra ciò che è lecito sulla propria cartuccia e ciò che è lecito su un servizio in linea non coincide, ed è il confine che questo track deve tenere presente.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| lo studio, gli strumenti e la risposta sulla legittimità | `STUDIO-01-ace-e-legalita-in-home.md`, in questa cartella |
| i marchi di origine, e che cosa conta come collezione completa | `STUDIO-02-marchi-di-origine-e-che-cosa-conta-una-collezione.md`, in questa cartella |
| la risposta della comunità, le tre severità e il tracciatore di Home | `STUDIO-03-la-risposta-della-comunita-e-le-due-severita.md`, in questa cartella |
| come si arriva a far eseguire codice a un gioco del 2004 | `docs/09-esecuzione-codice.md` |
| la struttura del dato che si scrive, byte per byte | `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`, sezioni 5 e 6 |
| l'altra via verso gli stessi esemplari, cioè la ricreazione della distribuzione | `recreate-pokemon-distributions-events/` |
| la catena di trasferimento verso Home e la sua scadenza | `recreate-pokemon-distributions-events/STUDIO-01-distribuzioni-gen3-e-ricreazione.md`, sezione 10 |
| le fonti di questo track, con il livello di affidabilità | `SOURCES.md` alla radice, colonna ACE |
| a che punto è il track e qual è il prossimo passo | `.claude/context/sub-poke-ace.md` |

Lo stato canonico del track vive nella scheda, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`. Questo file dice cos'è il sottoprogetto; quelli dicono a che punto è.
