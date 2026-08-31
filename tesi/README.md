# La tesi

Documento lungo che spiega, partendo dallo zero assoluto, come si trasporta un dato strutturato fra due sistemi digitali che non sono stati progettati per parlarsi, usando i sottoprogetti di questo repository come casi di studio. Non è un documento sui Pokemon: è un documento su rappresentazione, integrità, trasmissione e conversione dell'informazione, dove quei giochi sono il laboratorio.

Questo file è stato riscritto il 2026-08-29, e la ragione va detta perché è essa stessa un insegnamento sul modo in cui la documentazione invecchia. La versione precedente era stata scritta quando il documento aveva due capitoli su ventitré previsti, e descriveva quindi un piano: dichiarava una copertura al dieci per cento, elencava ventinove documenti da distribuire e marcava tutti i capitoli come da scrivere. Quando il documento è arrivato a ventisei capitoli e otto appendici con copertura al cento per cento, quel testo è diventato falso in ogni sua cifra, e nessuno strumento lo ha segnalato: il controllo di copertura verifica che il contenuto dei documenti finisca nel PDF, e questo file non è un documento da coprire ma un file che parla della tesi. Era un punto cieco della stessa specie di quello che `CLAUDE.md` descrive per le schede senza `covers-paths`, e la lezione è che un file tracciato che riporta numeri di stato va scritto per non invecchiare, oppure va sottoposto a un controllo.

La misura adottata è la prima delle due. Da qui in avanti questo file non riporta più alcun numero di stato: dice dove sono i numeri e con quale comando si ottengono, così che non possano divergere dalla realtà. La struttura dei capitoli non viene ripetuta qui, perché è già scritta in `tesi.tex`, che la contiene per costruzione, e nelle dichiarazioni `% copre:` in testa a ciascun capitolo, che sono la sola fonte di verità sulla corrispondenza fra capitoli e documenti.

## Come si compila

```
python tools/build-bibliography.py
latexmk -pdf tesi.tex
```

Il primo comando serve solo se la tabella delle fonti è cambiata, e il secondo va lanciato dalla cartella `tesi/`. Non serve BibTeX né biber: la bibliografia è un ambiente `thebibliography` generato, e `\cite` funziona con il solo nucleo di LaTeX. La ragione di questa scelta è scritta nel docstring del generatore, ed è che la TinyTeX di questa macchina è minimale e non installa pacchetti.

Due avvertenze operative valgono la riga, perché entrambe sono state pagate. Un visualizzatore di PDF aperto sul file tiene il file bloccato e la compilazione si interrompe con un errore che parla di impossibilità di scrivere: si chiude il visualizzatore, oppure si compila con un nome di lavoro diverso passando `-jobname`. E la verifica di ciò che è stato composto si fa sui byte del PDF e non su una schermata, perché quel medesimo visualizzatore mostra la versione in cache: la data composta sul frontespizio è il modo più rapido di accorgersene.

## Dove sono i numeri

```
python tools/check-thesis-coverage.py
python tools/check-thesis-coverage.py --scoperte
python tools/check-thesis-coverage.py --verbose
```

Il primo comando stampa il numero dei capitoli, il numero dei documenti da coprire, le righe di contenuto e quelle coperte con la percentuale, le sezioni scoperte, il conteggio della bibliografia e delle citazioni, l'elenco dei capitoli in drift e le citazioni orfane. È la fonte di verità sullo stato del documento, e per questo qui non se ne trascrive l'esito.

Il numero delle pagine e la pulizia della composizione si leggono dal registro della compilazione, cercandovi le righe di errore, i riferimenti irrisolti e gli sbordi di riga.

## Come si garantisce che nel PDF finisca tutto

È il vincolo che governa la struttura, ed è meccanico invece di essere una buona intenzione. Il requisito è che ogni riga dei documenti Markdown del progetto finisca da qualche parte nel PDF; l'organizzazione in parti, capitoli e paragrafi è invece libera. Un capitolo può raccogliere pezzi di documenti diversi e un documento può finire spezzato fra più capitoli: non serve alcuna corrispondenza uno a uno.

L'unità su cui il controllo lavora è la sezione, cioè un'intestazione Markdown con il testo che le sta sotto. Contare le righe sarebbe illusorio, perché una riga riscritta per un lettore diverso non ha lo stesso testo e nessun confronto meccanico potrebbe dire se il contenuto è passato. La sezione è abbastanza piccola da rendere il controllo utile e abbastanza stabile da poter essere nominata.

Ogni capitolo dichiara in testa che cosa reclama, con il commit a cui la dichiarazione è stata verificata.

```
% copre: docs/03-integrita-checksum.md
% copre: docs/01-fondamenta-salvataggio.md#il-supporto-fisico
% verificato-al-commit: f41fd4c
```

Da qui `check-thesis-coverage.py` ricava quattro verifiche. La copertura, cioè quali sezioni nessuno reclama, con il conteggio delle righe che restano fuori. Il drift, cioè quali capitoli dichiarano un commit anteriore all'ultima modifica dei documenti che coprono. Le citazioni orfane, cioè i riferimenti senza voce in bibliografia. E le fonti che nessun capitolo cita, che sono un avviso e non un errore, perché dicono che il documento dichiara di conoscere una fonte e non la usa.

Una quinta verifica nasce dalla forma della dichiarazione: se un titolo di sezione viene riscritto, il suo slug cambia e la dichiarazione che lo nominava risulta sconosciuta. Non è un falso allarme, è il segnale che quel capitolo va riletto.

Quando una sezione risulta reclamata il controllo non garantisce che il suo contenuto sia stato reso fedelmente: quello resta lavoro umano. Garantisce che nessuna sezione sia stata dimenticata, che è il modo in cui il contenuto si perde davvero.

Sul bump del checkpoint vale una regola che non è scritta nello strumento e va rispettata a mano: il commit dichiarato si aggiorna quando il capitolo è stato riletto contro i documenti che copre, non per far tacere la segnalazione. Un checkpoint bumpato senza rilettura trasforma un avviso utile in una menzogna silenziosa, che è precisamente il difetto che questo file aveva.

## Le esenzioni, e quando sono legittime

Le omissioni deliberate si dichiarano in `non-coperti.txt`, per documento intero o per singola sezione, sempre con il motivo dopo un cancelletto; un'esenzione senza motivo viene rifiutata dallo strumento.

Le esenzioni oggi presenti sono di due specie, e la distinzione è quella che rende la pratica onesta invece di comoda. La prima è il glossario, che confluisce nella premessa: il suo contenuto è nel PDF, semplicemente non come sezione propria. La seconda sono gli elenchi generati del catalogo degli eventi, dove la tesi rende le misure e la tassonomia, che sono conoscenza, e non le righe di dati, che sono un inventario da consultare; è la medesima ragione per cui le note di `docs/fonti/` non entrano fra i documenti da coprire, essendo generate dalla stessa tabella da cui nasce la bibliografia.

Una esenzione non è legittima quando serve a evitare di scrivere un capitolo. Il criterio pratico è questo: si esenta ciò che nel PDF sarebbe una copia, non ciò che nel PDF mancherebbe.

## Le appendici

Le appendici raccolgono le nozioni matematiche che i capitoli impiegano dandole per note, e sono generate a partire da un unico documento sorgente sotto `docs/`, secondo il medesimo verso che vale per i capitoli: prima il Markdown, poi la composizione. Il criterio con cui sono state riempite è meccanico e va conservato da chi le estenderà: si percorre il capitolo che impiega gli strumenti e ogni nozione che vi compare senza essere definita nel documento diventa una voce.

Ogni voce ha quattro parti, e sono la differenza fra un'appendice che si consulta e una che si legge: l'enunciato, la ragione per cui la nozione esiste, un esempio svolto fino al risultato numerico, e il rimando al punto del lavoro che la impiega.

Le dichiarazioni `% copre:` delle appendici non si scrivono a mano ma si generano, perché uno slug trascritto prima o poi non corrisponde e uno slug che non corrisponde viene segnalato come sezione sconosciuta.

## Che cosa si versiona

Il `.tex` è la fonte e si versiona, come il preambolo, questo README, le esenzioni e la bibliografia generata. Il PDF e tutti gli ausiliari sono derivati e sono esclusi dal `.gitignore`, per la politica sui binari di ADR-005: si rigenerano con `latexmk`.
