# Sottoprogetto: generazione e scambio dai giochi su console moderna

Studiare le vie con cui un esemplare entra nella collezione passando dai giochi per console moderna invece che dalle cartucce, e in particolare i bot di scambio automatico che la comunità ospita. Il track nasce il 2026-08-31 su richiesta dell'utente e serve, come gli altri, l'obiettivo dichiarato del progetto, cioè la collezione più completa possibile in Pokemon Home.

## Perché è un track a sé, e non una parte degli altri

Il progetto ha ormai tre track che convergono sul medesimo obiettivo per vie diverse, e vale distinguerli perché confonderli porta a scegliere lo strumento sbagliato per il problema che si ha.

La ricreazione delle distribuzioni prende un evento passato e fa rifare al gioco ciò che il gioco faceva allora, su hardware proprio. L'esecuzione di codice arbitrario scrive i byte dell'esemplare dentro un salvataggio proprio. Questo track non produce nulla di locale: **riceve un esemplare da qualcun altro**, attraverso lo scambio, che è il meccanismo di gioco previsto per farlo.

La differenza è sostanziale sul piano che a questo progetto interessa, cioè la provenienza. Nei primi due casi chi ottiene l'esemplare è anche chi lo ha prodotto; qui no, e le condizioni d'uso del servizio distinguono esplicitamente i due casi, dichiarando che non vi sono restrizioni per chi possieda dati alterati senza intenzione, per esempio ricevendoli in uno scambio senza saperlo. Questa distinzione va capita bene prima di trarne conclusioni, e lo studio la esamina invece di usarla come scorciatoia.

## Che cosa c'è in questa cartella

`STUDIO-01-scambio-automatico-e-provenienza.md` è lo studio, ed è il documento da leggere. Contiene che cosa sono i bot di scambio, che cosa la comunità ne dichiara, la questione della provenienza con la clausola che la riguarda, e l'inventario di ciò che resta da verificare prima che il track possa diventare operativo.

Allo stato attuale il track è ricerca, e il materiale di partenza è un canale della comunità e un articolo di terze parti, entrambi registrati in `SOURCES.md`. Nessuno strumento è stato eseguito e nessun servizio è stato contattato.

## Il punto che governa il track

Un esemplare ricevuto in uno scambio da un bot non è un esemplare che la partita ha prodotto: è un esemplare che qualcuno ha costruito e messo in circolazione. Dal punto di vista dei dati vale quindi tutto ciò che questo progetto ha già stabilito sulla differenza fra un dato coerente per costruzione e un dato coerente rispetto ai controlli conosciuti dal costruttore.

Dal punto di vista della responsabilità la situazione è diversa da quella degli altri due track, e la differenza è dichiarata dal titolare del servizio, non inferita. Ma trattarla come una assoluzione sarebbe leggerla male: la clausola parla di chi possiede dati alterati **senza intenzione**, e chi si rivolge deliberatamente a un servizio di generazione sa che cosa sta ricevendo. Lo studio espone i termini; la decisione, come per gli altri track, è dell'utente e va registrata come tale.

## Perimetro

Vale `.claude/rules/hardware-and-perimeter.md`, e in particolare la sezione sui salvataggi di terze parti, che questo track tocca da vicino: la regola esclude i salvataggi scaricati perché il rischio ricade sull'account e sulla console, e un esemplare ricevuto da un bot è materiale di terze parti anche quando arriva attraverso il meccanismo di gioco.

La regola non si applica in modo automatico, perché non si tratta di importare un salvataggio, e proprio per questo la decisione va presa e non dedotta. È registrata come aperta in `.claude/memory/pending.md`.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| lo studio, la provenienza e ciò che resta da verificare | `STUDIO-01-scambio-automatico-e-provenienza.md`, in questa cartella |
| l'altra via che passa dalla console moderna, cioè lo scambio dal calcolatore | `gba-switch-pokemon-trading/` |
| la via che scrive i byte in locale | `poke-ace/` |
| la via che ricrea l'evento originale | `recreate-pokemon-distributions-events/` |
| la catena di trasferimento verso Home, la sua scadenza e la porta nuova di ottobre 2026 | `poke-ace/STUDIO-01-ace-e-legalita-in-home.md`, sezione 2 |
| le fonti di questo track | `SOURCES.md` alla radice, colonna GEN |
| a che punto è il track e qual è il prossimo passo | `.claude/context/sub-generation-from-switch.md` |

Lo stato canonico del track vive nella scheda, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`.
