# Prompt di ripresa - le discipline e il modo di lavorare

> Questo file esiste per una ragione precisa: i commit dicono che cosa è cambiato e non perché, né che cosa era stato deciso di non fare. Si legge dopo l'indice e le pendenze, e si aggiorna a ogni passo del lavoro: una voce obsoleta qui è peggio della sua assenza, perché induce a fidarsi di uno stato che non esiste più. La versione precedente di questo file era ferma al 2026-08-31 e dichiarava sei track, centottantuno pagine di tesi e un lettore di cartucce non ancora arrivato: tutte e tre le cose erano false il giorno in cui sono state rilette, ed è la ragione per cui la riscrittura è stata fatta invece di rattoppare.

Dal 2026-09-10 la divisione del lavoro con il file locale è dichiarata, perché tenerne due senza dichiararla è il modo di farli divergere. Questo file, che è tracciato, porta le discipline, il modo di lavorare e gli errori di metodo, cioè ciò che cambia di rado ed è utile anche a un clone. Lo stato volatile della ripresa, cioè il fuoco, i numeri del giorno, i lotti e le decisioni in attesa, sta in `_notes/RESUME_PROMPT.md`, che git esclude e che si riscrive alla fine di ogni giro sostanziale per il presidio della regola sulla persistenza. Chi riprende legge quello per primo e questo subito dopo.

## 0. Come si riprende, in ordine

Prima si verifica l'account con `/status`, perché il legame fra directory di configurazione e account non è garantito stabile e un riavvio può averlo cambiato in silenzio. Poi si legge `.claude/memory/index.md`, che è la fonte di verità sullo stato dei dieci sottoprogetti e porta il commit di riferimento. Poi `.claude/memory/pending.md` per intero, che è il registro di tutto ciò che è in sospeso. Poi questo file. Poi, e solo poi, la scheda del sottoprogetto su cui si lavora.

Il fuoco corrente è `pokedex-home-completo`, cioè la collezione completa nel deposito prima che la banca chiuda. La scadenza è il 26 febbraio 2027 alle 12:00 del fuso giapponese, e al 2026-09-09 restano centosettanta giorni. L'obiettivo governa gli altri track invece di affiancarli: la ricreazione delle distribuzioni produce ciò che quella collezione richiede, il ponte fra generazioni scrive i salvataggi che la trasportano, e i track su hardware fisico aprono la catena che la porta a destinazione.

## 1. Le quattro discipline che governano ogni sessione

Non sono preferenze e non si negoziano, perché l'utente le ha dichiarate esplicitamente e ripetutamente. Vengono prima di qualunque decisione tecnica.

### 1.1 Ogni riga di ogni `.md` finisce nel PDF

Ogni singola riga di ogni file `.md` del progetto deve finire nella tesi, riorganizzata e scritta in forma accademica. Non esiste un mapping uno a uno fra un documento e un capitolo, e l'organizzazione in parti, capitoli e sezioni è libera; ciò che non è libero è la copertura.

L'invariante è meccanizzato in `tools/check-thesis-coverage.py`, che confronta le sezioni dei documenti da coprire con le dichiarazioni `% copre:` in testa a ciascun capitolo, alla granularità della sezione. La conseguenza operativa è che quando si aggiunge contenuto a un `.md` la copertura scende sotto il cento per cento e va riportata a cento aggiungendolo al documento. Il verso corretto è sempre questo, cioè prima il `.md` e poi il capitolo, perché i layer degli `.md` documentano e tracciano e da quelli si aggiungono contenuti alla tesi.

Le esenzioni deliberate si dichiarano in `tesi/non-coperti.txt` con il motivo, e un'esenzione senza motivo viene rifiutata dallo strumento. Il criterio con cui si sceglie fra esentare e coprire è quello già applicato: un elenco generato di righe di dati si esenta dichiarandolo, mentre la prosa, la tassonomia e le misure di un documento generato si rendono in un capitolo. Al 2026-09-09 le esenzioni coprono le schede di pedigree delle prime quattro generazioni, la lista di spunta, il catalogo degli eventi, il censimento delle fonti del corpus e le enumerazioni per titolo dei due censimenti nuovi.

Un difetto dello strumento è stato corretto lo stesso giorno e va conosciuto perché nascondeva proprio il lavoro da fare: `--scoperte` si arrestava con un errore di codifica sul primo titolo contenente un carattere fuori dalla tabella della console, quindi l'elenco delle sezioni da distribuire era inaccessibile su Windows. La correzione è la riconfigurazione dello standard output in UTF-8 con sostituzione, che è l'idioma già usato dagli altri strumenti del progetto.

### 1.2 Ogni micro passo si documenta, si spiega e si dimostra

Una modifica al codice o a un dato va accompagnata dalla sua ragione nel documento che la ospita, non in un messaggio di commit. Una affermazione tecnica va dimostrata o marcata come da verificare, con il blocco `daverificare` in LaTeX e la citazione fra virgolette angolari nei `.md`. Un numero va calcolato da uno strumento riproducibile e non stimato a mente, e lo strumento resta nel repository.

### 1.3 La chat non è memoria

Regola nuova del 2026-09-09, in `.claude/rules/chat-non-e-memoria.md`. Nessun contenuto sostanziale resta nella sola conversazione, e i file si aggiornano nello stesso giro di lavoro in cui il contenuto nasce, non alla fine della sessione. Il presidio è che alla fine di ogni giro di lavoro sostanziale l'agente dichiara in una riga quali file ha scritto. Il vincolo di team resta intatto: `context/` e `memory/` non si toccano di propria iniziativa, ma l'utente ha dato la richiesta in forma generale il 2026-09-09, quindi il delta si applica e si dichiara.

### 1.4 Le lingue

La lingua del documento è l'italiano, e in parallelo va generata anche la versione inglese, come documento prodotto insieme all'altro e non dopo. Lo spagnolo resta escluso. I file `.md` restano in italiano: sono il layer che documenta e traccia, e non vanno tradotti. Il task è ancora aperto e la sua forma proposta sta nella sezione 4.

## 2. Lo stato del documento, in numeri verificati il 2026-09-09

```
40 file di capitolo in tesi/capitoli/, cioè 32 numerati più 8 appendici, oltre a frontespizio e premessa
300 pagine
0 errori di compilazione, 0 riferimenti irrisolti, 0 citazioni orfane
copertura del contenuto: 36830 righe su 36830, cioè 100,0%, con 81 documenti da coprire
bibliografia: 106 voci, tutte citate, cioè 87 fonti di dominio più 19 riferimenti teorici
mappa delle fonti: 87 note sotto docs/fonti/, con 51 relazioni
suite del ponte: 206 prove, OK
```

I comandi che riproducono queste misure, dalla radice del repository, uno per riga perché una riga spezzata a mano diventa due comandi rotti:

```powershell
cd tesi; pdflatex -interaction=nonstopmode tesi.tex; pdflatex -interaction=nonstopmode tesi.tex; cd ..
python tools/check-thesis-coverage.py
python tools/check-thesis-pdf.py
python tools/build-source-map.py --check
python tools/build-bibliography.py --check
python pokemon-gen12-gen3-bridge-original-hardware/tests/run_tests.py
python tools/test-tipografia.py
```

Una avvertenza sulla compilazione, pagata il 2026-08-29: un visualizzatore di PDF aperto sul file lo tiene bloccato, e `pdflatex` si arresta con un errore che parla di impossibilità di scrivere. Si chiude il visualizzatore, oppure si compila con `-jobname` diverso per verificare senza toccare il file buono.

I quattro capitoli nuovi del 2026-09-09 sono il 28 sulla catena di trasferimento e le porte che restano, il 29 sugli assi della collezione e su come si enumerano, il 30 sul produrre dentro il gioco invece che intorno, e il 31 sul leggere un corpus e pianificare con ciò che se ne ricava. Il 14 ha ricevuto la sezione sulla prima sessione con il lettore e il 23 due sezioni nuove, cioè la crescita del registro delle fonti di un ordine di grandezza e la correzione sul recupero da Reddit, che dal 2026-09-07 funziona per una via che cambia il capo invece del tragitto.

## 3. La mappatura delle fonti, e il difetto che aveva

La tabella `FONTI` dentro `tools/build-source-map.py` è la fonte unica da cui nascono sia le note di `docs/fonti/` sia la bibliografia della tesi. Il 2026-09-09 si è scoperto che dieci voci vivevano nella sola bibliografia, cioè erano state scritte a mano dentro un file che dichiara in testa di essere generato: sarebbero sparite alla prima rigenerazione, portandosi via le citazioni che vi puntavano. Sono state riportate nella tabella, e con esse sono entrate diciotto fonti nuove che il registro aveva e la mappa no, cioè quelle dei tre cluster del corpus letti fra il 7 e il 9 settembre.

Da qui una regola operativa che vale oltre il caso: quando un file dichiara di essere generato, la correzione si fa nella tabella e mai nel file, e la prova che la disciplina regga è che `--check` di entrambi gli strumenti passi prima del commit.

## 4. I task aperti, in ordine di priorità

### 4.1 La lettura del corpus

È la voce più grossa del debito di lettura e l'utente ha chiesto di leggere tutto prima di produrre altro lavoro. Il corpus scaricato è di duecentonovantadue documenti per sei milioni e duecentomila byte su quarantadue cluster: sono letti i tre cluster prioritari più i cluster 6, 5, 4 e 3 e i cataloghi per generazione dalla prima alla quarta. L'ordine dei restanti è quello di ADR-052, cioè la scadenza, e la sintesi entra in `pokedex-home-completo/LETTURA-DEL-CORPUS.md` a lotti invece di restare in conversazione.

### 4.2 Il lavoro tecnico che ADR-051 apre

Estendere il generatore agli scambi in gioco, agli incontri condizionati e agli statici ordinari delle prime cinque generazioni; aggiungere all'asse degli eventi il Mew ufficiale con allenatore GF e identificativo 22796, che il lotto di prima generazione non contiene; e rigenerare la lista di spunta con i tre cambi recenti, cioè le sessantatre configurazioni di Alcremie, le centodue specie dell'asse del sesso e le due classi nuove.

### 4.3 La versione inglese, generata sempre in parallelo

Non ancora realizzata. La forma proposta è una cartella di capitoli per lingua con il medesimo schema di nomi, un solo `tesi.tex` che scelga il percorso da una macro iniettata dalla riga di comando, e uno script che produca i due PDF in una passata. Il controllo va esteso in due punti, e sono la parte che rende il parallelismo verificabile invece che dichiarato: le due cartelle devono contenere gli stessi file con le stesse dichiarazioni `% copre:`, e il controllo di copertura deve girare su entrambe le lingue. Resta una decisione aperta, cioè se tradurre anche i blocchi da verificare e gli abstract bibliografici; la proposta è tradurre tutto il testo di autore e lasciare in italiano i soli abstract, che sono generati dalla tabella delle fonti.

### 4.4 La prima sessione con il lettore

Il lettore GBxCart RW v1.4 Pro è arrivato il 2026-09-09 e resta un solo cancello prima di collegare qualcosa, cioè i driver CH340 con il criterio della sezione 5.4 dell'handoff del track Smeraldo. La sequenza sta in `gba-save-extraction-smeraldo/RUNBOOK-PRIMA-SESSIONE.md` e il suo principio è che l'ordine è quello del rischio e non quello dell'interesse: prima i salvataggi delle cartucce di prima e seconda generazione la cui pila tenga ancora, perché è la sola finestra che si chiude da sé; poi Smeraldo, che sta in memoria non volatile; poi le ROM che servono al ponte.

### 4.5 Le pendenze minori che restano

Il sottotitolo del frontespizio porta ancora tre righe spezzate a mano con lunghezze disuguali, ed è una decisione dell'utente. Il repository `prova` ha un commit locale senza remoto configurato. Il `research-vault` di `thesis` non è un repository git e una passata non annullabile sugli strumenti tipografici non è stata fatta deliberatamente. Restano i file duplicati sotto `.claude/templates/`, un file con una lettera accentata nel nome e undici file con spazi nel nome.

## 5. Gli altri progetti di `E:\`, stato dichiarato al 2026-08-31 e non riverificato

| Progetto | LaTeX | Stato |
|---|---|---|
| `retrogame-mod-pok-dev` | sì | questo progetto, riferimento della propagazione |
| `template-claude-developing` | no | strumenti e regola aggiornati, committato e pushato |
| `harmony-book` | sì | strumenti e regola aggiornati, committato e pushato |
| `my-cv` | sì | strumenti, regola, 86 sostituzioni in `main.tex`, tre PDF verificati, committato |
| `prova` | sì | strumenti, regola, 120 file corretti, compila, commit locale senza push |
| `rodrainaudio-reverse-eng` | sì | strumenti, regola, 112 file corretti, compila, committato e pushato |
| `thesis` | no | strumenti e regola, 42 file corretti; non è un repository git |

Quella colonna dello stato non è stata riverificata dopo il 2026-08-31 e va trattata come tale: prima di dichiarare che un altro progetto è allineato, lo si guarda.

## 6. Gli errori di metodo, da non ripetere

Questa sezione è la più utile del file, perché ciascuno di questi errori è costato tempo e si ripresenterà.

Gli heredoc corrompono le sequenze di escape, e su questa macchina un heredoc multi riga passato al Bash tool si è rotto anche senza escape: il codice e i blocchi di testo lunghi si scrivono in un file con lo strumento di scrittura e poi si eseguono o si concatenano.

`sed` con i backslash non fa quello che sembra, e per le sostituzioni che li coinvolgono si usa Python. Contare i backslash annidati sbaglia quando i livelli di escape sono tre: si scrive il blocco con un segnaposto e lo si sostituisce una volta sola alla fine.

Un controllo per sottostringa produce falsi positivi sui nomi contenuti in altri nomi, e il controllo corretto guarda il contesto. Un controllo di idempotenza che cerca il nome di una funzione trova la sua definizione, quindi va fatto sull'innesto. Un `replace` senza contesto colpisce anche le firme delle funzioni.

Gli strumenti correggono i propri dati di prova, ed è accaduto quattro volte: i dati di prova si costruiscono per concatenazione di frammenti o da codepoint.

Un file temporaneo su un volume diverso da quello del repository rompe il calcolo del percorso relativo su Windows: i file temporanei vanno nella cartella di lavoro della sessione o in `_notes/tmp`, che git ignora.

Il segno meno matematico non è un trattino, ed è il carattere che la regola tipografica definisce il più insidioso in un testo tecnico.

Una schermata può mostrare un file aperto in precedenza, perché il visualizzatore tiene il file in cache: la verifica va fatta sui byte del file e non sull'immagine.

Il codice di uscita di `fix-accents.py --check` è sempre zero, quindi una dichiarazione di igiene fondata su quel controllo non è stabilita: è ADR-033, e il presidio è guardare l'elenco che lo strumento stampa invece del suo esito.

Prima di dichiarare da verificare un fatto esterno si cerca nel registro delle fonti, e prima di dichiarare una lacuna nostra si cerca nei nostri file: sono cinque occorrenze in pochi giorni del medesimo difetto, e due di esse sono costate una voce di lavoro inventata e una pianificazione impostata su un tetto inesistente.

## 7. I vincoli del progetto che non si negoziano

I comandi git restano manuali dell'utente. L'agente prepara i file e consegna i comandi, non committa, e il `settings.json` lo impone anche in negazione. I comandi si consegnano in due blocchi, PowerShell e bash, con una riga per comando e nessun carattere di continuazione.

Le schede di `context/` e i file di `memory/` non si aggiornano di propria iniziativa: li aggiorna l'utente, o l'agente su richiesta, che dal 2026-09-09 esiste in forma generale.

Ogni paragrafo di prosa in un file Markdown sta su una riga sorgente unica, e si verifica con `python tools/md-unwrap.py --check .` insieme a `python tools/lint-md-tables.py .` e `python tools/lint-md-commands.py .`

Nessun dump di cartuccia, nessun backup di salvataggio, nessun materiale di chiave console-unica e nessun media entra in git.

## 8. Il promemoria di chiusura, che vale su questa macchina

Quando si chiude, l'hook `SessionEnd` di account2 esegue il wipe da sé, ma per la pulizia garantita anche sulla coda dell'ultima sessione, dopo aver chiuso Claude si lancia il comando seguente.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\Utente\.claude-account2\hooks\session-end-wipe.ps1"
```

Preserva i progetti, la configurazione, il login, le skill e i plugin.
