# Decisioni

Registro append-only in forma ADR-lite. Una decisione registrata non si riscrive: se cambia, si aggiunge una voce nuova che supera la precedente e si annota il rimando.

Nota di onesta' sulla provenienza. Questo progetto non aveva storia git al momento dell'adozione del sistema, quindi le decisioni non sono state ricostruite dai commit come prevede la procedura di allineamento. Le voci da ADR-006 in avanti sono ricostruite leggendo gli handoff esistenti, con il riferimento puntuale alla sezione da cui provengono, e le loro date sono quelle dichiarate nei documenti, non date di commit.

## ADR-001 Adozione del sistema di progetto portabile

Data: 2026-08-24. Stato: accettata.

Il progetto adotta lo standard del bundle in `E:\template-claude-developing`. Il caso e' ibrido fra i due previsti: esiste contenuto ma non esiste storia git, e la repository remota era gia' creata e vuota. Ne segue che si applicano l'inventario e la clausola di riconciliare invece di duplicare dalla procedura di allineamento, mentre la ricostruzione della memoria dalla storia e la scansione dei segreti sulla storia sono sostituite dalle rispettive operazioni sul solo working tree, e i frontmatter nascono con il segnaposto PENDING-FIRST-COMMIT come in un progetto greenfield.

## ADR-002 Architettura mono-radice con schede verticali

Data: 2026-08-24. Stato: accettata.

Il template ha un'anatomia mono-radice e non prevede il caso multi-sottoprogetto. Si tiene un'unica anatomia e si aggiunge una famiglia di schede sub-slug sotto `context/`, una per sottoprogetto, ciascuna con `covers-paths` limitato alla propria cartella. Le sei schede canoniche restano e diventano l'asse trasversale.

Respinta l'ipotesi di replicare l'anatomia dentro ogni sottoprogetto: produrrebbe quattro `memory/index.md` senza un punto d'ingresso unico, e `sync-context` scopre le schede con un Glob sulla sola `context/` di radice, quindi non funzionerebbe. Respinta anche l'ipotesi di appoggiarsi a `CLAUDE.md` annidati come portante primario, per tre ragioni: il caricamento e' opportunistico e dipende da quali file la sessione tocca, un `CLAUDE.md` annidato non porta il frontmatter di riconciliazione e quindi accumula drift senza rilevatore, e aggiungerebbe un terzo luogo dove vive lo stesso stato.

Resta un trigger di revisione per quella seconda ipotesi, in forma ristretta: quando il sottoprogetto del ponte iniziera' a produrre codice con comandi propri di build, lint e test, un `CLAUDE.md` annidato che contenga soltanto quelle convenzioni imperative, e nessuno stato, sara' la casa corretta, perche' sono istruzioni e non stato.

Il `covers-paths` si scrive come prefisso di cartella con lo slash finale e non come glob, perche' il confronto di `sync-context` e' un pathspec git, dove la semantica dei wildcard non coincide con quella di `.gitignore`, e il prefisso di cartella e' la forma meno ambigua e identica fra Windows e POSIX.

## ADR-003 Handoff in loco, coperti invece che duplicati

Data: 2026-08-24. Stato: accettata, con deviazione dichiarata.

I tre handoff esistenti restano nelle cartelle dei rispettivi sottoprogetti e restano tracciati. Non migrano sotto `.claude/`, perche' hanno riferimenti relativi a file fratelli che si romperebbero, perche' `.claude/` e' il namespace del comportamento dell'agente e non l'archivio dei documenti di progetto, e perche' la richiesta esplicita dell'utente che ogni sottoprogetto abbia il suo handoff e' soddisfatta solo se l'handoff resta l'artefatto del sottoprogetto.

Il frontmatter di riconciliazione si mette sulla scheda del sottoprogetto e non sull'handoff, e il `covers-paths` della scheda include la cartella del sottoprogetto, quindi copre anche l'handoff. Quando l'handoff cambia, il diff sui `covers-paths` lo restituisce, la scheda risulta stale e si aggiornano le sole righe di stato.

La deviazione rispetto alla lettera del prompt di allineamento, che dice di dotare di frontmatter il documento esistente, e' voluta: l'alternativa raddoppierebbe i `last-verified-commit` da aggiornare per ogni singola modifica. Nella sostanza la clausola e' rispettata, perche' l'handoff non viene duplicato ma coperto.

La divisione di competenza e' netta. L'handoff e' conoscenza: procedura, troubleshooting, fonti, log e motivazione delle scelte. La scheda e' stato: dove siamo, prossimo passo, decisioni aperte, evidenze. Copiare un paragrafo dall'uno all'altra e' il segnale che la divisione e' stata violata.

## ADR-004 Identificatori in ASCII e date in ISO

Data: 2026-08-24. Stato: accettata.

Nomi di file e di cartelle in ASCII puro, e date negli identificatori in formato YYYY-MM-DD. Le cartelle scritte con l'accento grave sono state portate ad ASCII, e non alla forma con l'accento acuto che sarebbe quella ortograficamente corretta in prosa, perche' anche quella e' non-ASCII e risolverebbe l'ortografia lasciando intatto il problema tecnico: git memorizza i path come byte grezzi e la stessa stringa si normalizza in modo diverso fra Windows e macOS, producendo rename spuri su un clone; inoltre quei nomi finiscono dentro i `covers-paths`, cioe' dentro un pathspec git.

La rinomina di una delle cartelle ha eliminato anche spazi, parentesi e un punto interno al nome, che sono gli elementi che rendono un nome fragile davanti a qualunque pattern e a qualunque riga di comando.

La normalizzazione si applica solo agli identificatori. La prosa non si tocca, quindi una data scritta come 18/08/2026 dentro un handoff resta com'e'.

La cartella del sottoprogetto Smeraldo e' stata rinominata da action-replay-filesavextraction a gba-save-extraction-smeraldo perche' il nome era factualmente superato: il percorso Action Replay e' chiuso e quello attivo e' l'estrazione fisica del salvataggio.

## ADR-005 Politica sui binari e sui media

Data: 2026-08-24. Stato: accettata.

Dump di cartucce e backup di salvataggio non si versionano mai, indipendentemente dalla dimensione, e sono esclusi per estensione prima ancora di esistere. Il materiale di chiave console-unica e' escluso come categoria di segreti, non di binari.

Foto, video e screenshot non si versionano: sono evidenza personale e non conoscenza tecnica. Restano sul disco accanto alle note che li citano, mentre cio' che documentano si registra in prosa nella scheda del sottoprogetto, dove diventa diffabile. Gli screenshot con dati personali sono stati portati in `_notes/media-riservati/` prima del primo commit, che era l'unica finestra in cui l'operazione costava zero.

Git LFS e' stato valutato e respinto per il video da diciotto megabyte: consuma la quota gratuita di storage e di banda, obbliga a un client su ogni clone, e non si disfa senza riscrivere la storia.

Il PDF che documenta il bug dell'inventario segue la politica sui media perche' e' un bundle di sette foto, pur non contenendo dati personali. La riga di eccezione per tracciarlo esiste gia', commentata, nel `.gitignore`.

Si escludono le estensioni e mai le cartelle contenitore, perche' `.gitignore` non permette di re-includere un file se una cartella genitore e' esclusa: questo tiene aperta la possibilita' di un'eccezione curata in futuro.

## ADR-006 Smeraldo, Action Replay chiuso ed estrazione fisica attiva

Data: 18/08/2026, ricostruita dalle sezioni 2.3 e 3.1 dell'handoff. Stato: accettata.

Il percorso Action Replay e' abbandonato. Master Code e Anti-DMA erano verificati su piu' fonti indipendenti, ma per i codici specifici della tasca Strumenti Base non esisteva alcuna fonte affidabile, e si e' scelto di non indovinare indirizzi di memoria su un salvataggio irripetibile. Il percorso attivo e' l'estrazione fisica con GBxCart RW, FlashGBX e PKHeX, su Windows 11 perche' PKHeX e' un'applicazione .NET Windows Forms e il supporto a Mono e Wine e' stato abbandonato dal 2023.

## ADR-007 3DS, MSET9 come punto di ingresso del custom firmware

Data: ricostruita dalla sezione 4.1 dell'handoff. Stato: accettata, eseguita.

MSET9 e' stato scelto come exploit di installazione di boot9strap sul firmware 11.17.0-50E, per le ragioni documentate nella sezione 4.1 dell'handoff del sottoprogetto 3DS. La procedura e' stata eseguita e MSET9 e' stato rimosso a fine installazione.

## ADR-008 Ponte fra generazioni, decisione aperta

Data: 2026-08-24. Stato: proposta, non decisa.

Questa voce registra una decisione che non e' stata presa, e la registra perche' un'opzione lasciata implicita si perde. Le quattro strade sono: usare o contribuire a Poke Transporter GB cosi' come e'; costruire un tool software offline su PC che applichi PCCS su dump della SRAM; riprodurre da zero il ponte hardware con devkitARM; costruire un bridge su microcontrollore.

La scelta e' bloccata su una discovery hardware, che l'handoff raccomanda esplicitamente perche' la disponibilita' di console, flashcart, cavo Link e capacita' di saldare cambia radicalmente lo stack. Finche' la discovery non e' fatta, nessuna delle quattro e' preferibile sulla carta.

## ADR-009 Deviazioni dichiarate dall'anatomia canonica

Data: 2026-08-24. Stato: accettata.

Due adattamenti al caso multi-track, dichiarati invece che introdotti di soppiatto. In `context/current-work.md` il campo di stato diventa un aggregato e il corpo si apre con una tabella dei track invece di descrivere una sola feature attiva. In `memory/index.md` la tabella di verifica prende una colonna che attribuisce ogni scheda al suo sottoprogetto, e il punto di ripresa diventa un blocco di righe preceduto da una riga che nomina il track attivo.

La regola di precedenza che ne consegue: la riga del fuoco corrente e' la fonte di verita' unica su cosa e' attivo adesso, mentre `current-work.md` tiene il dettaglio di tutti i track. Questo conserva il requisito che una sessione nuova abbia un solo punto di ingresso deterministico.

## ADR-010 MCP rimandato

Data: 2026-08-24. Stato: accettata, con trigger di revisione.

Il gate del server MCP e' stato aperto come prevede la procedura, e la risposta e' no per ora. Il server consigliato in allineamento estrae struttura e simboli del codice con tree-sitter, e su un corpus fatto di documenti Markdown, note di testo e collegamenti non ha nulla da estrarre. Va riproposto nel momento esatto in cui il sottoprogetto del ponte scaffolda il primo modulo.

## ADR-011 Media raccolti sotto _notes/media, materiale con dati personali eliminato

Data: 2026-08-24. Stato: accettata. Raffina ADR-005, che resta valido nella sostanza.

ADR-005 stabiliva che i media non si versionano e restano sul disco accanto alle note che li citano. La pratica ha mostrato il difetto di quella seconda meta': media sparsi in sette cartelle diverse, invisibili a git ma visibili a chi apre il progetto, e un albero che sembra misto mentre e' di sola conoscenza tecnica. Tutti i media sono stati quindi raccolti sotto `_notes/media/`, che rispecchia la struttura del progetto, cartella di sottoprogetto e cartella-data comprese, cosi' il percorso di un media resta deducibile da dove sta la nota che lo cita. L'albero tracciato e' ora solo testo.

Due cartelle-data del sottoprogetto Smeraldo contenevano soltanto media e sono sparite dall'albero di progetto: esistono ora solo dentro `_notes/media/`, dove conservano il loro nome.

Gli undici screenshot con dati personali sono stati eliminati dal disco, non solo tolti da git. Non erano mai entrati nella storia, quindi la loro presenza era una scelta e non un'eredita', e conservare indirizzo di casa, numero di telefono e il cognome di un terzo senza una ragione operativa e' un rischio senza contropartita. Il fatto tecnico che documentavano, cioe' l'ordine del 18 agosto 2026 e la configurazione acquistata, era gia' scritto in prosa e senza dati personali nella scheda del sottoprogetto, che e' esattamente lo scopo per cui la politica dei media impone di scrivere in prosa cio' che un media mostra. Una copia sopravvive nel backup pre-bonifica fuori dal repository, finche' quel backup esiste.

La regola che ne discende, scritta nel README di `_notes/media-riservati/`: quel percorso e' una zona di transito, non un archivio. Il materiale con dati personali ci passa, il fatto tecnico si scrive nella scheda, il file si elimina.

## ADR-012 Definito l'obiettivo del quarto track: trading LDN fra PC e Switch

Data: 2026-08-24. Stato: accettata. Chiude la lacuna dichiarata in `sub-gba-switch-trading.md` alla creazione dell'anatomia.

Il sottoprogetto che era stato aperto come cartella vuota e senza obiettivo ha ora un handoff proprio, `HANDOFF_frlg-ldn-trade.md`. L'obiettivo e' far comunicare un PC Linux con una Nintendo Switch attraverso LDN, il protocollo wireless locale proprietario di Nintendo, per scambiare Pokemon con una copia di FireRed o LeafGreen sulla console, appoggiandosi a `kinnay/LDN` e a `tornadus/frlg-ldn-trade`.

L'obiettivo ribalta l'ipotesi con cui il track era stato registrato. Quando la cartella era vuota si era supposto che potesse essere una via verso Pokemon Home e quindi una possibile sovrapposizione con il sottoprogetto 3DS. Non lo e': e' lavoro di rete e di reverse engineering, autonomo, ed e' il secondo track destinato a produrre software vero accanto al ponte fra generazioni. Resta una sovrapposizione hardware non documentata, perche' il lettore GBxCart RW del track Smeraldo compare fra i requisiti senza che sia spiegato in quale fase entri.

Tre conseguenze sull'infrastruttura, registrate qui perche' nessuna era prevista.

La prima e' di sicurezza ed e' stata sanata subito. Le `prod.keys` della Switch sono materiale di chiave console-unica con le stesse proprieta' di `movable.sed`, e il blocco dei segreti del `.gitignore` copriva solo il 3DS. E' stato esteso alle chiavi della Switch e ai file di dati Pokemon esportati, prima che il nuovo handoff venisse committato.

La seconda e' una tensione di piattaforma non risolta: questo track richiede Linux, mentre il track Smeraldo richiede Windows 11 per PKHeX. Come farli convivere, in dual boot o su supporto avviabile, e' una decisione aperta che non e' urgente finche' il track resta in ricerca.

La terza e' che i track destinati a produrre codice sono ora due, non uno. Questo avvicina i due trigger di revisione gia' registrati: il gate del server MCP di lettura del codice, rimandato per ADR-010, e il `CLAUDE.md` annidato con le sole convenzioni di build previsto da ADR-002. Nessuno dei due scatta adesso, perche' in locale non esiste ancora una riga di codice.

## ADR-013 Handoff del ponte ritirato, conoscenza assorbita

Data: 2026-08-25. Stato: accettata. Raffina ADR-003, che resta valido per gli altri tre sottoprogetti.

ADR-003 stabiliva che gli handoff restano nelle cartelle dei rispettivi sottoprogetti, coperti dal `covers-paths` della scheda invece di essere duplicati. Quella decisione vale ancora per i tre track che sono runbook su hardware fisico, dove l'handoff e' la procedura e non esiste nulla che lo sostituisca. Non vale piu' per il ponte fra generazioni, dove l'handoff era un documento di ricerca: la sua conoscenza e' stata verificata sul disassemblato, e la verifica ne ha corretto quattro affermazioni e chiuso undici punti dubbi.

Un documento di ricerca superato che resta accanto a un documento verificato non e' storia, e' una seconda risposta alla stessa domanda, e in una sessione futura sarebbe una fonte di errore. Il file `HANDOFF_Pokemon_Gen1-2_to_Gen3_Bridge.md` e' stato quindi rimosso, dopo aver trasferito tutto cio' che conteneva e che non era superato: il formato dati in `DATA-FORMATS_Gen1-Gen2-Gen3.md`, il meccanismo e i concetti nelle note di `docs/`, le quattro opzioni implementative e i fatti sul progetto di riferimento in `docs/30-opzioni-implementative.md`, il glossario in `docs/31-glossario.md`, e i link in `SOURCES.md`. La cronologia delle release non e' stata trasferita perche' si rilegge su GitHub, tranne i due punti che confermano dall'esterno la ricostruzione fatta sul codice.

Resta recuperabile dalla storia git, dove vive fino al commit cdb09e2. La sua rimozione e' quindi reversibile, che e' la ragione per cui non serve conservarne una copia inerte nel working tree.

La stessa domanda, posta su tutti i sottoprogetti, ha prodotto tre rimozioni ulteriori e sette conferme. Sono stati rimossi `3ds-related/handoff/Notes.txt`, sei righe di appunti grezzi di conversazione il cui contenuto e' interamente nella sezione 7 dell'handoff in forma ordinata; `3ds-related/handoff/flusso-3ds.html`, una pagina HTML generata che disegnava il flusso verso i servizi in rete, superata dalla stessa sezione e dal fatto che quel percorso e' fuori perimetro, e comunque un artefatto non testuale in un albero che per ADR-005 e' di solo testo; e `gba-save-extraction-smeraldo/handoff/progetto_smeraldo_contesto.md`, la cui struttura di sezioni e' un sottoinsieme stretto dell'handoff che lo ha sostituito.

Restano invece i quattro handoff dei tre track su hardware fisico, piu' i due file di passo del track 3DS, e la ragione non e' prudenza. Sono runbook di procedure irreversibili, non documenti di ricerca: `step03_dump_cartucce.md` e' la procedura del passo attivo, `HANDOFF_progetto_smeraldo.md` contiene il dettaglio dello step corrente sui driver, `HANDOFF_frlg-ldn-trade.md` e' l'unica cosa che definisce un track non ancora iniziato, e `step02_cfw_mset9.md` e' il resoconto di come e' stato modificato questo specifico esemplare di console, cioe' materiale di troubleshooting non sostituibile da una guida generale. Cancellarli perderebbe procedura, non ridondanza.

A compensazione della rimozione, ogni sottoprogetto ha ora un `README.md` come punto di ingresso, che dichiara lo scopo di quella cartella e instrada verso la conoscenza pertinente, e `docs/index.md` porta la tabella che associa ciascuno dei quattro scopi alle note che gli servono. Era la lacuna vera: la conoscenza tecnica era stata scritta ma non era navigabile partendo da un sottoprogetto.

## ADR-014 Circostanza personale fuori dai file tracciati

Data: 2026-08-25. Stato: accettata.

Sei file tracciati registravano, come motivazione di un limite di perimetro, una circostanza personale su come Pokemon Bank e Pokemon Transporter sono arrivati su questa console. Il repository e' pubblico su GitHub e riconducibile a una persona identificabile, quindi quella motivazione non ha ragione di stare in un file tracciato: cio' che serve a una sessione futura e' il limite, non il perche'.

I sei file sono stati riscritti conservando il limite in forma neutra e rimandando a `_notes/perimetro-bank-transporter.md`, fuori dal version control per la riga 6 del `.gitignore`. Sono la regola `hardware-and-perimeter.md`, le schede `design-and-security.md`, `sub-3ds-modding.md` e `roadmap.md`, e le sezioni 2, 5.8 e 7 dell'handoff 3DS piu' il suo `step03_dump_cartucce.md`. Dalla sezione 7 dell'handoff e' stata conservata l'analisi di dominio, che e' pubblica e utile, cioe' il prerequisito dell'NNID e la chiusura del servizio, ed e' stato rimosso soltanto il riferimento alla situazione dell'utente e alla richiesta rifiutata.

La prima passata era incompleta, e vale la pena registrarlo perche' e' il tipo di errore che si ripete. Una seconda passata, fatta cercando i termini identificanti invece delle frasi, ha trovato altro. Due riferimenti testuali sopravvissuti, uno in `sub-3ds-modding.md` che nominava la procedura e il percorso della cartella dei media, e uno dentro un ADR precedente. Una cartella tracciata il cui nome e quello del collegamento che conteneva dicevano dove scaricare quel software. Tre file tracciati che puntavano a fonti di ROM, cioe' un collegamento e una raccolta di link a due comunita' di condivisione, in contraddizione diretta con la sezione sul solo hardware posseduto della regola di perimetro. Due file di prompt iniziale, della stessa natura del `PROMPT MASTER.txt` che l'utente aveva gia' cancellato. E sei occorrenze del nome e cognome dell'utente in chiaro, dentro due trascrizioni di conversazione incollate come testo, che la scansione dei dati personali fatta all'adozione del sistema aveva mancato perche' guardava le immagini.

Tutto questo e' stato rimosso o neutralizzato, e ne discende una regola operativa: uno scrub si verifica cercando i termini che identificano, non le frasi che si ricorda di aver scritto, e si verifica su tutto l'albero tracciato compresi i nomi dei file e delle cartelle, non solo sul contenuto.

Il caveat va registrato perche' e' la parte che la bonifica non risolve: il testo originale resta nei commit da d1e1a3a in avanti, che sono gia' sul remoto pubblico. Rimuoverlo davvero richiede una riscrittura della storia con `git filter-repo` e un push forzato, e anche allora GitHub conserva i commit orfani raggiungibili per hash finche' non fa garbage collection, mentre eventuali fork o cache di terze parti non si riscrivono affatto. La decisione se procedere resta dell'utente e non e' presa qui.

## ADR-015 La tensione fra Windows e Linux decade: il track LDN gira su Windows

Data: 2026-08-26. Stato: accettata.

Il progetto aveva registrato come decisione aperta il modo di far convivere due sistemi operativi obbligati da track diversi: Windows per il sottoprogetto dello Smeraldo, perche' PKHeX e' un'applicazione .NET Windows Forms il cui supporto a Mono e Wine e' stato abbandonato dal 2023, e Linux per il track dello scambio con la Switch, perche' la libreria del protocollo di rete locale richiede la modalita' monitor dello stack wireless del kernel. Le alternative in campo erano il dual boot e il supporto avviabile.

La lettura del canale di Pokemon Multiplayer Research e del sorgente del demone `ldnd`, fatta il 2026-08-26, mostra che quella scelta non e' necessaria. Esiste una seconda implementazione che gira su Windows senza macchina virtuale: collega il kernel Linux come libreria statica tramite LKL dentro un eseguibile costruito con MinGW, riceve l'adattatore wireless USB attraverso WinUSB e gli fa caricare i driver e i file di `linux-firmware`. Lo stack wireless di Linux non viene riscritto ne' emulato: viene portato dentro il processo.

La decisione e' quindi di considerare Windows la piattaforma di riferimento per entrambi i track e di chiudere la decisione aperta, con tre riserve dichiarate. La prima e' che la via Windows funziona soltanto con adattatori wireless USB, mai con schede interne, perche' WinUSB puo' prendere soltanto un dispositivo USB; su Linux va bene anche una scheda interna se il suo driver collabora. La seconda e' che, dopo la riassegnazione del dispositivo a WinUSB, quello non funziona piu' come scheda di rete ordinaria, quindi la macchina ha bisogno di un altro accesso a internet. La terza e' che le due implementazioni non hanno la stessa compatibilita' hardware, verificato sul campo, e in caso di guasto inspiegabile la via Linux resta un'alternativa da provare e non una strada abbandonata.

Non si acquista nulla e non si installa nulla in conseguenza di questa decisione: il primo passo resta leggere l'identificatore USB dell'adattatore che l'utente ha gia'.

## ADR-016 La fonte unica vale anche per il materiale procurato a mano

Data: 2026-08-26. Stato: accettata.

La cartella `_notes/fonti/` era stata istituita come luogo dove l'utente consegna il materiale che l'agente non riesce a recuperare da se'. La regola della fonte unica, scritta nel registro delle fonti, dice che quel materiale e' una cache di contenuto grezzo e non un archivio, e che cio' che documenta va trasferito in prosa nel registro con la profondita' necessaria a citarlo senza riaprirlo.

Si decide di applicare quella regola fino in fondo e di svuotare la cartella una volta compiuto il trasferimento, invece di lasciarvi il materiale gia' assorbito. La ragione e' che due copie della stessa conoscenza, una citabile e una grezza, producono il dubbio su quale sia quella buona, e il dubbio costa piu' di quanto valga la copia. Il 2026-08-26 la cartella e' stata svuotata dall'utente dopo la conferma che tutto il materiale, comprese le sei trascrizioni video, era confluito nelle fonti e nelle note di studio.

Ne segue un obbligo per l'agente, che e' la parte vincolante di questa decisione: il trasferimento va fatto con la profondita' che rende il file grezzo sacrificabile, e non con un riassunto che costringerebbe a riaprirlo. Quando cio' non e' possibile, per esempio perche' la fonte e' una tabella lunga da citare per intero, il materiale resta e la voce del registro lo dichiara.
