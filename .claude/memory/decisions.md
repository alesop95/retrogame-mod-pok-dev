# Decisioni

Registro append-only in forma ADR-lite. Una decisione registrata non si riscrive: se cambia, si aggiunge una voce nuova che supera la precedente e si annota il rimando.

Nota di onestà sulla provenienza. Questo progetto non aveva storia git al momento dell'adozione del sistema, quindi le decisioni non sono state ricostruite dai commit come prevede la procedura di allineamento. Le voci da ADR-006 in avanti sono ricostruite leggendo gli handoff esistenti, con il riferimento puntuale alla sezione da cui provengono, e le loro date sono quelle dichiarate nei documenti, non date di commit.

## ADR-001 Adozione del sistema di progetto portabile

Data: 2026-08-24. Stato: accettata.

Il progetto adotta lo standard del bundle in `E:\template-claude-developing`. Il caso è ibrido fra i due previsti: esiste contenuto ma non esiste storia git, e la repository remota era già creata e vuota. Ne segue che si applicano l'inventario e la clausola di riconciliare invece di duplicare dalla procedura di allineamento, mentre la ricostruzione della memoria dalla storia e la scansione dei segreti sulla storia sono sostituite dalle rispettive operazioni sul solo working tree, e i frontmatter nascono con il segnaposto PENDING-FIRST-COMMIT come in un progetto greenfield.

## ADR-002 Architettura mono-radice con schede verticali

Data: 2026-08-24. Stato: accettata.

Il template ha un'anatomia mono-radice e non prevede il caso multi-sottoprogetto. Si tiene un'unica anatomia e si aggiunge una famiglia di schede sub-slug sotto `context/`, una per sottoprogetto, ciascuna con `covers-paths` limitato alla propria cartella. Le sei schede canoniche restano e diventano l'asse trasversale.

Respinta l'ipotesi di replicare l'anatomia dentro ogni sottoprogetto: produrrebbe quattro `memory/index.md` senza un punto d'ingresso unico, e `sync-context` scopre le schede con un Glob sulla sola `context/` di radice, quindi non funzionerebbe. Respinta anche l'ipotesi di appoggiarsi a `CLAUDE.md` annidati come portante primario, per tre ragioni: il caricamento è opportunistico e dipende da quali file la sessione tocca, un `CLAUDE.md` annidato non porta il frontmatter di riconciliazione e quindi accumula drift senza rilevatore, e aggiungerebbe un terzo luogo dove vive lo stesso stato.

Resta un trigger di revisione per quella seconda ipotesi, in forma ristretta: quando il sottoprogetto del ponte inizierà a produrre codice con comandi propri di build, lint e test, un `CLAUDE.md` annidato che contenga soltanto quelle convenzioni imperative, e nessuno stato, sarà la casa corretta, perché sono istruzioni e non stato.

Il `covers-paths` si scrive come prefisso di cartella con lo slash finale e non come glob, perché il confronto di `sync-context` è un pathspec git, dove la semantica dei wildcard non coincide con quella di `.gitignore`, e il prefisso di cartella è la forma meno ambigua e identica fra Windows e POSIX.

## ADR-003 Handoff in loco, coperti invece che duplicati

Data: 2026-08-24. Stato: accettata, con deviazione dichiarata.

I tre handoff esistenti restano nelle cartelle dei rispettivi sottoprogetti e restano tracciati. Non migrano sotto `.claude/`, perché hanno riferimenti relativi a file fratelli che si romperebbero, perché `.claude/` è il namespace del comportamento dell'agente e non l'archivio dei documenti di progetto, e perché la richiesta esplicita dell'utente che ogni sottoprogetto abbia il suo handoff è soddisfatta solo se l'handoff resta l'artefatto del sottoprogetto.

Il frontmatter di riconciliazione si mette sulla scheda del sottoprogetto e non sull'handoff, e il `covers-paths` della scheda include la cartella del sottoprogetto, quindi copre anche l'handoff. Quando l'handoff cambia, il diff sui `covers-paths` lo restituisce, la scheda risulta stale e si aggiornano le sole righe di stato.

La deviazione rispetto alla lettera del prompt di allineamento, che dice di dotare di frontmatter il documento esistente, è voluta: l'alternativa raddoppierebbe i `last-verified-commit` da aggiornare per ogni singola modifica. Nella sostanza la clausola è rispettata, perché l'handoff non viene duplicato ma coperto.

La divisione di competenza è netta. L'handoff è conoscenza: procedura, troubleshooting, fonti, log e motivazione delle scelte. La scheda è stato: dove siamo, prossimo passo, decisioni aperte, evidenze. Copiare un paragrafo dall'uno all'altra è il segnale che la divisione è stata violata.

## ADR-004 Identificatori in ASCII e date in ISO

Data: 2026-08-24. Stato: accettata.

Nomi di file e di cartelle in ASCII puro, e date negli identificatori in formato YYYY-MM-DD. Le cartelle scritte con l'accento grave sono state portate ad ASCII, e non alla forma con l'accento acuto che sarebbe quella ortograficamente corretta in prosa, perché anche quella è non-ASCII e risolverebbe l'ortografia lasciando intatto il problema tecnico: git memorizza i path come byte grezzi e la stessa stringa si normalizza in modo diverso fra Windows e macOS, producendo rename spuri su un clone; inoltre quei nomi finiscono dentro i `covers-paths`, cioè dentro un pathspec git.

La rinomina di una delle cartelle ha eliminato anche spazi, parentesi e un punto interno al nome, che sono gli elementi che rendono un nome fragile davanti a qualunque pattern e a qualunque riga di comando.

La normalizzazione si applica solo agli identificatori. La prosa non si tocca, quindi una data scritta come 18/08/2026 dentro un handoff resta com'è.

La cartella del sottoprogetto Smeraldo è stata rinominata da action-replay-filesavextraction a gba-save-extraction-smeraldo perché il nome era factualmente superato: il percorso Action Replay è chiuso e quello attivo è l'estrazione fisica del salvataggio.

## ADR-005 Politica sui binari e sui media

Data: 2026-08-24. Stato: accettata.

Dump di cartucce e backup di salvataggio non si versionano mai, indipendentemente dalla dimensione, e sono esclusi per estensione prima ancora di esistere. Il materiale di chiave console-unica è escluso come categoria di segreti, non di binari.

Foto, video e screenshot non si versionano: sono evidenza personale e non conoscenza tecnica. Restano sul disco accanto alle note che li citano, mentre ciò che documentano si registra in prosa nella scheda del sottoprogetto, dove diventa diffabile. Gli screenshot con dati personali sono stati portati in `_notes/media-riservati/` prima del primo commit, che era l'unica finestra in cui l'operazione costava zero.

Git LFS è stato valutato e respinto per il video da diciotto megabyte: consuma la quota gratuita di storage e di banda, obbliga a un client su ogni clone, e non si disfa senza riscrivere la storia.

Il PDF che documenta il bug dell'inventario segue la politica sui media perché è un bundle di sette foto, pur non contenendo dati personali. La riga di eccezione per tracciarlo esiste già, commentata, nel `.gitignore`.

Si escludono le estensioni e mai le cartelle contenitore, perché `.gitignore` non permette di re-includere un file se una cartella genitore è esclusa: questo tiene aperta la possibilità di un'eccezione curata in futuro.

## ADR-006 Smeraldo, Action Replay chiuso ed estrazione fisica attiva

Data: 18/08/2026, ricostruita dalle sezioni 2.3 e 3.1 dell'handoff. Stato: accettata.

Il percorso Action Replay è abbandonato. Master Code e Anti-DMA erano verificati su più fonti indipendenti, ma per i codici specifici della tasca Strumenti Base non esisteva alcuna fonte affidabile, e si è scelto di non indovinare indirizzi di memoria su un salvataggio irripetibile. Il percorso attivo è l'estrazione fisica con GBxCart RW, FlashGBX e PKHeX, su Windows 11 perché PKHeX è un'applicazione .NET Windows Forms e il supporto a Mono e Wine è stato abbandonato dal 2023.

## ADR-007 3DS, MSET9 come punto di ingresso del custom firmware

Data: ricostruita dalla sezione 4.1 dell'handoff. Stato: accettata, eseguita.

MSET9 è stato scelto come exploit di installazione di boot9strap sul firmware 11.17.0-50E, per le ragioni documentate nella sezione 4.1 dell'handoff del sottoprogetto 3DS. La procedura è stata eseguita e MSET9 è stato rimosso a fine installazione.

## ADR-008 Ponte fra generazioni, decisione aperta

Data: 2026-08-24. Stato: proposta, non decisa.

Questa voce registra una decisione che non è stata presa, e la registra perché un'opzione lasciata implicita si perde. Le quattro strade sono: usare o contribuire a Poke Transporter GB così come è; costruire un tool software offline su PC che applichi PCCS su dump della SRAM; riprodurre da zero il ponte hardware con devkitARM; costruire un bridge su microcontrollore.

La scelta è bloccata su una discovery hardware, che l'handoff raccomanda esplicitamente perché la disponibilità di console, flashcart, cavo Link e capacità di saldare cambia radicalmente lo stack. Finché la discovery non è fatta, nessuna delle quattro è preferibile sulla carta.

## ADR-009 Deviazioni dichiarate dall'anatomia canonica

Data: 2026-08-24. Stato: accettata.

Due adattamenti al caso multi-track, dichiarati invece che introdotti di soppiatto. In `context/current-work.md` il campo di stato diventa un aggregato e il corpo si apre con una tabella dei track invece di descrivere una sola feature attiva. In `memory/index.md` la tabella di verifica prende una colonna che attribuisce ogni scheda al suo sottoprogetto, e il punto di ripresa diventa un blocco di righe preceduto da una riga che nomina il track attivo.

La regola di precedenza che ne consegue: la riga del fuoco corrente è la fonte di verità unica su cosa è attivo adesso, mentre `current-work.md` tiene il dettaglio di tutti i track. Questo conserva il requisito che una sessione nuova abbia un solo punto di ingresso deterministico.

## ADR-010 MCP rimandato

Data: 2026-08-24. Stato: accettata, con trigger di revisione.

Il gate del server MCP è stato aperto come prevede la procedura, e la risposta è no per ora. Il server consigliato in allineamento estrae struttura e simboli del codice con tree-sitter, e su un corpus fatto di documenti Markdown, note di testo e collegamenti non ha nulla da estrarre. Va riproposto nel momento esatto in cui il sottoprogetto del ponte scaffolda il primo modulo.

## ADR-011 Media raccolti sotto _notes/media, materiale con dati personali eliminato

Data: 2026-08-24. Stato: accettata. Raffina ADR-005, che resta valido nella sostanza.

ADR-005 stabiliva che i media non si versionano e restano sul disco accanto alle note che li citano. La pratica ha mostrato il difetto di quella seconda metà: media sparsi in sette cartelle diverse, invisibili a git ma visibili a chi apre il progetto, e un albero che sembra misto mentre è di sola conoscenza tecnica. Tutti i media sono stati quindi raccolti sotto `_notes/media/`, che rispecchia la struttura del progetto, cartella di sottoprogetto e cartella-data comprese, così il percorso di un media resta deducibile da dove sta la nota che lo cita. L'albero tracciato è ora solo testo.

Due cartelle-data del sottoprogetto Smeraldo contenevano soltanto media e sono sparite dall'albero di progetto: esistono ora solo dentro `_notes/media/`, dove conservano il loro nome.

Gli undici screenshot con dati personali sono stati eliminati dal disco, non solo tolti da git. Non erano mai entrati nella storia, quindi la loro presenza era una scelta e non un'eredità, e conservare indirizzo di casa, numero di telefono e il cognome di un terzo senza una ragione operativa è un rischio senza contropartita. Il fatto tecnico che documentavano, cioè l'ordine del 18 agosto 2026 e la configurazione acquistata, era già scritto in prosa e senza dati personali nella scheda del sottoprogetto, che è esattamente lo scopo per cui la politica dei media impone di scrivere in prosa ciò che un media mostra. Una copia sopravvive nel backup pre-bonifica fuori dal repository, finché quel backup esiste.

La regola che ne discende, scritta nel README di `_notes/media-riservati/`: quel percorso è una zona di transito, non un archivio. Il materiale con dati personali ci passa, il fatto tecnico si scrive nella scheda, il file si elimina.

## ADR-012 Definito l'obiettivo del quarto track: trading LDN fra PC e Switch

Data: 2026-08-24. Stato: accettata. Chiude la lacuna dichiarata in `sub-gba-switch-trading.md` alla creazione dell'anatomia.

Il sottoprogetto che era stato aperto come cartella vuota e senza obiettivo ha ora un handoff proprio, `HANDOFF_frlg-ldn-trade.md`. L'obiettivo è far comunicare un PC Linux con una Nintendo Switch attraverso LDN, il protocollo wireless locale proprietario di Nintendo, per scambiare Pokemon con una copia di FireRed o LeafGreen sulla console, appoggiandosi a `kinnay/LDN` e a `tornadus/frlg-ldn-trade`.

L'obiettivo ribalta l'ipotesi con cui il track era stato registrato. Quando la cartella era vuota si era supposto che potesse essere una via verso Pokemon Home e quindi una possibile sovrapposizione con il sottoprogetto 3DS. Non lo è: è lavoro di rete e di reverse engineering, autonomo, ed è il secondo track destinato a produrre software vero accanto al ponte fra generazioni. Resta una sovrapposizione hardware non documentata, perché il lettore GBxCart RW del track Smeraldo compare fra i requisiti senza che sia spiegato in quale fase entri.

Tre conseguenze sull'infrastruttura, registrate qui perché nessuna era prevista.

La prima è di sicurezza ed è stata sanata subito. Le `prod.keys` della Switch sono materiale di chiave console-unica con le stesse proprietà di `movable.sed`, e il blocco dei segreti del `.gitignore` copriva solo il 3DS. È stato esteso alle chiavi della Switch e ai file di dati Pokemon esportati, prima che il nuovo handoff venisse committato.

La seconda è una tensione di piattaforma non risolta: questo track richiede Linux, mentre il track Smeraldo richiede Windows 11 per PKHeX. Come farli convivere, in dual boot o su supporto avviabile, è una decisione aperta che non è urgente finché il track resta in ricerca.

La terza è che i track destinati a produrre codice sono ora due, non uno. Questo avvicina i due trigger di revisione già registrati: il gate del server MCP di lettura del codice, rimandato per ADR-010, e il `CLAUDE.md` annidato con le sole convenzioni di build previsto da ADR-002. Nessuno dei due scatta adesso, perché in locale non esiste ancora una riga di codice.

## ADR-013 Handoff del ponte ritirato, conoscenza assorbita

Data: 2026-08-25. Stato: accettata. Raffina ADR-003, che resta valido per gli altri tre sottoprogetti.

ADR-003 stabiliva che gli handoff restano nelle cartelle dei rispettivi sottoprogetti, coperti dal `covers-paths` della scheda invece di essere duplicati. Quella decisione vale ancora per i tre track che sono runbook su hardware fisico, dove l'handoff è la procedura e non esiste nulla che lo sostituisca. Non vale più per il ponte fra generazioni, dove l'handoff era un documento di ricerca: la sua conoscenza è stata verificata sul disassemblato, e la verifica ne ha corretto quattro affermazioni e chiuso undici punti dubbi.

Un documento di ricerca superato che resta accanto a un documento verificato non è storia, è una seconda risposta alla stessa domanda, e in una sessione futura sarebbe una fonte di errore. Il file `HANDOFF_Pokemon_Gen1-2_to_Gen3_Bridge.md` è stato quindi rimosso, dopo aver trasferito tutto ciò che conteneva e che non era superato: il formato dati in `DATA-FORMATS_Gen1-Gen2-Gen3.md`, il meccanismo e i concetti nelle note di `docs/`, le quattro opzioni implementative e i fatti sul progetto di riferimento in `docs/30-opzioni-implementative.md`, il glossario in `docs/31-glossario.md`, e i link in `SOURCES.md`. La cronologia delle release non è stata trasferita perché si rilegge su GitHub, tranne i due punti che confermano dall'esterno la ricostruzione fatta sul codice.

Resta recuperabile dalla storia git, dove vive fino al commit cdb09e2. La sua rimozione è quindi reversibile, che è la ragione per cui non serve conservarne una copia inerte nel working tree.

La stessa domanda, posta su tutti i sottoprogetti, ha prodotto tre rimozioni ulteriori e sette conferme. Sono stati rimossi `3ds-related/handoff/Notes.txt`, sei righe di appunti grezzi di conversazione il cui contenuto è interamente nella sezione 7 dell'handoff in forma ordinata; `3ds-related/handoff/flusso-3ds.html`, una pagina HTML generata che disegnava il flusso verso i servizi in rete, superata dalla stessa sezione e dal fatto che quel percorso è fuori perimetro, e comunque un artefatto non testuale in un albero che per ADR-005 è di solo testo; e `gba-save-extraction-smeraldo/handoff/progetto_smeraldo_contesto.md`, la cui struttura di sezioni è un sottoinsieme stretto dell'handoff che lo ha sostituito.

Restano invece i quattro handoff dei tre track su hardware fisico, più i due file di passo del track 3DS, e la ragione non è prudenza. Sono runbook di procedure irreversibili, non documenti di ricerca: `step03_dump_cartucce.md` è la procedura del passo attivo, `HANDOFF_progetto_smeraldo.md` contiene il dettaglio dello step corrente sui driver, `HANDOFF_frlg-ldn-trade.md` è l'unica cosa che definisce un track non ancora iniziato, e `step02_cfw_mset9.md` è il resoconto di come è stato modificato questo specifico esemplare di console, cioè materiale di troubleshooting non sostituibile da una guida generale. Cancellarli perderebbe procedura, non ridondanza.

A compensazione della rimozione, ogni sottoprogetto ha ora un `README.md` come punto di ingresso, che dichiara lo scopo di quella cartella e instrada verso la conoscenza pertinente, e `docs/index.md` porta la tabella che associa ciascuno dei quattro scopi alle note che gli servono. Era la lacuna vera: la conoscenza tecnica era stata scritta ma non era navigabile partendo da un sottoprogetto.

## ADR-014 Circostanza personale fuori dai file tracciati

Data: 2026-08-25. Stato: accettata.

Sei file tracciati registravano, come motivazione di un limite di perimetro, una circostanza personale su come Pokemon Bank e Pokemon Transporter sono arrivati su questa console. Il repository è pubblico su GitHub e riconducibile a una persona identificabile, quindi quella motivazione non ha ragione di stare in un file tracciato: ciò che serve a una sessione futura è il limite, non il perché.

I sei file sono stati riscritti conservando il limite in forma neutra e rimandando a `_notes/perimetro-bank-transporter.md`, fuori dal version control per la riga 6 del `.gitignore`. Sono la regola `hardware-and-perimeter.md`, le schede `design-and-security.md`, `sub-3ds-modding.md` e `roadmap.md`, e le sezioni 2, 5.8 e 7 dell'handoff 3DS più il suo `step03_dump_cartucce.md`. Dalla sezione 7 dell'handoff è stata conservata l'analisi di dominio, che è pubblica e utile, cioè il prerequisito dell'NNID e la chiusura del servizio, ed è stato rimosso soltanto il riferimento alla situazione dell'utente e alla richiesta rifiutata.

La prima passata era incompleta, e vale la pena registrarlo perché è il tipo di errore che si ripete. Una seconda passata, fatta cercando i termini identificanti invece delle frasi, ha trovato altro. Due riferimenti testuali sopravvissuti, uno in `sub-3ds-modding.md` che nominava la procedura e il percorso della cartella dei media, e uno dentro un ADR precedente. Una cartella tracciata il cui nome e quello del collegamento che conteneva dicevano dove scaricare quel software. Tre file tracciati che puntavano a fonti di ROM, cioè un collegamento e una raccolta di link a due comunità di condivisione, in contraddizione diretta con la sezione sul solo hardware posseduto della regola di perimetro. Due file di prompt iniziale, della stessa natura del `PROMPT MASTER.txt` che l'utente aveva già cancellato. E sei occorrenze del nome e cognome dell'utente in chiaro, dentro due trascrizioni di conversazione incollate come testo, che la scansione dei dati personali fatta all'adozione del sistema aveva mancato perché guardava le immagini.

Tutto questo è stato rimosso o neutralizzato, e ne discende una regola operativa: uno scrub si verifica cercando i termini che identificano, non le frasi che si ricorda di aver scritto, e si verifica su tutto l'albero tracciato compresi i nomi dei file e delle cartelle, non solo sul contenuto.

Il caveat va registrato perché è la parte che la bonifica non risolve: il testo originale resta nei commit da d1e1a3a in avanti, che sono già sul remoto pubblico. Rimuoverlo davvero richiede una riscrittura della storia con `git filter-repo` e un push forzato, e anche allora GitHub conserva i commit orfani raggiungibili per hash finché non fa garbage collection, mentre eventuali fork o cache di terze parti non si riscrivono affatto. La decisione se procedere resta dell'utente e non è presa qui.

## ADR-015 La tensione fra Windows e Linux decade: il track LDN gira su Windows

Data: 2026-08-26. Stato: accettata.

Il progetto aveva registrato come decisione aperta il modo di far convivere due sistemi operativi obbligati da track diversi: Windows per il sottoprogetto dello Smeraldo, perché PKHeX è un'applicazione .NET Windows Forms il cui supporto a Mono e Wine è stato abbandonato dal 2023, e Linux per il track dello scambio con la Switch, perché la libreria del protocollo di rete locale richiede la modalità monitor dello stack wireless del kernel. Le alternative in campo erano il dual boot e il supporto avviabile.

La lettura del canale di Pokemon Multiplayer Research e del sorgente del demone `ldnd`, fatta il 2026-08-26, mostra che quella scelta non è necessaria. Esiste una seconda implementazione che gira su Windows senza macchina virtuale: collega il kernel Linux come libreria statica tramite LKL dentro un eseguibile costruito con MinGW, riceve l'adattatore wireless USB attraverso WinUSB e gli fa caricare i driver e i file di `linux-firmware`. Lo stack wireless di Linux non viene riscritto né emulato: viene portato dentro il processo.

La decisione è quindi di considerare Windows la piattaforma di riferimento per entrambi i track e di chiudere la decisione aperta, con tre riserve dichiarate. La prima è che la via Windows funziona soltanto con adattatori wireless USB, mai con schede interne, perché WinUSB può prendere soltanto un dispositivo USB; su Linux va bene anche una scheda interna se il suo driver collabora. La seconda è che, dopo la riassegnazione del dispositivo a WinUSB, quello non funziona più come scheda di rete ordinaria, quindi la macchina ha bisogno di un altro accesso a internet. La terza è che le due implementazioni non hanno la stessa compatibilità hardware, verificato sul campo, e in caso di guasto inspiegabile la via Linux resta un'alternativa da provare e non una strada abbandonata.

Non si acquista nulla e non si installa nulla in conseguenza di questa decisione: il primo passo resta leggere l'identificatore USB dell'adattatore che l'utente ha già.

## ADR-016 La fonte unica vale anche per il materiale procurato a mano

Data: 2026-08-26. Stato: accettata.

La cartella `_notes/fonti/` era stata istituita come luogo dove l'utente consegna il materiale che l'agente non riesce a recuperare da sé. La regola della fonte unica, scritta nel registro delle fonti, dice che quel materiale è una cache di contenuto grezzo e non un archivio, e che ciò che documenta va trasferito in prosa nel registro con la profondità necessaria a citarlo senza riaprirlo.

Si decide di applicare quella regola fino in fondo e di svuotare la cartella una volta compiuto il trasferimento, invece di lasciarvi il materiale già assorbito. La ragione è che due copie della stessa conoscenza, una citabile e una grezza, producono il dubbio su quale sia quella buona, e il dubbio costa più di quanto valga la copia. Il 2026-08-26 la cartella è stata svuotata dall'utente dopo la conferma che tutto il materiale, comprese le sei trascrizioni video, era confluito nelle fonti e nelle note di studio.

Ne segue un obbligo per l'agente, che è la parte vincolante di questa decisione: il trasferimento va fatto con la profondità che rende il file grezzo sacrificabile, e non con un riassunto che costringerebbe a riaprirlo. Quando ciò non è possibile, per esempio perché la fonte è una tabella lunga da citare per intero, il materiale resta e la voce del registro lo dichiara.

## ADR-017 Sesto sottoprogetto: la ricreazione delle distribuzioni, e l'obiettivo di collezione

Data: 2026-08-28. Stato: accettata per la parte di adozione, con due questioni di perimetro dichiarate aperte.

Il progetto accoglie un sesto sottoprogetto, `recreate-pokemon-distributions-events/`, con l'obiettivo di ricreare su hardware originale e su cartucce possedute le distribuzioni di eventi di terza generazione. La richiesta dell'utente dichiara anche il fine a cui quel lavoro serve, e va registrata perché cambia la lettura di tutto il progetto: avere in Pokemon Home tutte le 1025 specie e le forme alternative, come collezione da portare avanti per tutta la vita.

Ne discendono tre conseguenze che questa decisione mette per iscritto.

La prima è che il progetto acquisisce una scadenza esterna e verificata, cioè la chiusura di Pokemon Bank il 26 febbraio 2027 alle 12:00 JST, con la fine contestuale del trasferimento verso Home. Fino a oggi la scheda della direzione dichiarava quella data irrilevante, perché la strada che vi passa era considerata chiusa; da oggi è il vincolo del sesto track, e la scheda è stata corretta di conseguenza. Il fatto tecnico che la rende vincolante è che Poke Transporter accetta come sorgente soltanto la quinta generazione e le riedizioni su Virtual Console della prima e della seconda, quindi un esemplare di terza generazione deve attraversare quattro passaggi irreversibili e il primo di essi richiede una console con lo slot Game Boy Advance.

La seconda è che il nome della cartella è stato reso conforme alla convenzione del progetto. L'utente l'aveva creata come `recreate-pokèmon-distributions-events`, con una lettera accentata, mentre `CLAUDE.md` prescrive nomi in ASCII puro per le cartelle dei sottoprogetti e `pending.md` registra già una violazione analoga come debito. La cartella era vuota, quindi il costo della conformità era nullo e il rinvio avrebbe prodotto un percorso che compare in un `covers-paths`, in un pathspec git e in una dichiarazione di copertura della tesi: tre luoghi dove un carattere non ASCII è un difetto che si manifesta tardi. La decisione è reversibile e il rinominare resta una scelta dell'utente.

La terza è che due questioni di perimetro restano aperte e non vengono decise qui, perché non sono tecniche. La prima è che l'ultimo tratto della catena passa da Pokemon Bank e Pokemon Transporter su questa console, cioè dai due titoli su cui l'assistenza è esclusa dalla regola sull'hardware e sul perimetro: la contraddizione fra quella norma e l'obiettivo dichiarato è reale, non ha soluzione tecnica, e va decisa dall'utente con un ADR proprio. La seconda è che tre delle quattro vie di iniezione di un evento richiedono materiale di terze parti, cioè una ROM di distribuzione o un salvataggio precostituito per l'e-Reader, mentre la regola esclude i salvataggi scaricati da internet; la norma non si applica in modo automatico, perché non si tratta di importare il salvataggio di un gioco Pokemon, e proprio per questo la decisione va presa e non dedotta. Fino ad allora il track lavora su ricerca, verifica di legittimità e preparazione, che è la parte maggiore del lavoro.

## ADR-018 Le fonti Discord si leggono con un bot account, non con il token personale

Data: 2026-08-31. Stato: accettata. Sostituisce parzialmente la decisione del 2026-08-26 sul token utente, che resta valida per ciò che decideva.

Il 2026-08-26 il progetto ha deciso di non usare il token del proprio account Discord per gli export, perché automatizzare un account personale è vietato dalle condizioni d'uso e la sanzione dichiarata è la terminazione dell'account. Quella decisione era corretta e non viene riaperta. Era però incompleta, e vale registrare in che modo, perché è un errore di forma che si ripete: aveva valutato l'unica via che il progetto conosceva, l'aveva trovata inaccettabile, e aveva concluso che il problema non avesse soluzione. Le vie sono tre.

La terza è un bot account creato nel portale per sviluppatori di Discord, e si decide di adottarla. La distinzione dal self-bot non è una sfumatura interpretativa e poggia su fatti verificabili: il tipo di token è diverso e la documentazione ufficiale descrive il bot account come dedicato all'automazione; l'accesso a un server passa da un invito che chi amministra autorizza esplicitamente scegliendo i permessi e potendoli revocare; il bot porta un contrassegno visibile a tutti, quindi non finge di essere una persona; l'API è pubblica e documentata, con limiti di frequenza pensati per traffico automatico; e il rischio in caso di uso scorretto ricade sull'applicazione e non sull'account personale dell'utente.

Lo strumento è `tools/fetch-discord.py`, che parla direttamente con l'API ufficiale invece di passare da un server MCP, e la scelta va motivata perché il materiale che ha aperto la questione raccomandava l'MCP. Quella raccomandazione è corretta nel contesto per cui era scritta, cioè un agente residente che deve poter chiamare quel tool in conversazione; qui il lavoro è deterministico e la regola sull'economia dei token prescrive di tenerlo su codice, quindi un programma sulla sola libreria standard evita una dipendenza su Node, un pacchetto di terze parti a cui affidare un token, e uno strato di protocollo fra noi e una richiesta HTTP. Le due vie non si escludono, perché usano il medesimo bot account.

Il presidio contro l'uso accidentale del token personale è parte della decisione e non un dettaglio di implementazione: lo strumento invia sempre l'intestazione nella forma prevista per i bot e verifica che l'account autenticato sia dichiarato tale prima di qualunque lettura, con un controllo negativo nella sua suite a dimostrare che il presidio non è dichiarato ma operante. Il principio generale che ne discende, e che vale oltre questo caso, è che una distinzione normativa diventa effettiva soltanto quando è resa meccanica nel punto in cui potrebbe essere violata per distrazione.

Va registrato il limite, perché è la parte che nessuna configurazione risolve. Il meccanismo di consenso che rende lecita la terza via la rende inapplicabile dove il consenso non si ottiene: dei quattro server che il progetto consulta nessuno appartiene all'utente, quindi per tutti e quattro serve l'autorizzazione di chi li amministra. La prescrizione è chiedere, dichiarando a che cosa serve e quali permessi si chiedono, e accettare che un no sia un esito dopo il quale resta la copia manuale. Una via lecita non è una via disponibile.

L'esportazione dello strumento e della sezione di regola verso il template è prevista e non è fatta qui: è registrata fra le pendenze, perché la regola sulle fonti non recuperabili è già nel template e vi va aggiornata insieme allo strumento, con la stessa procedura usata per gli strumenti tipografici.

## ADR-019 Il token personale di Discord si usa, con DiscordChatExporter e con cadenza rara

Data: 2026-08-31. Stato: accettata. Rovescia la decisione del 2026-08-26 e non sostituisce ADR-018.

Il 2026-08-26 il progetto aveva deciso di non usare il token del proprio account Discord per le esportazioni. Il 2026-08-31, dopo che la via del bot account ufficiale era stata trovata, allestita, provata contro il servizio e irrobustita, si è constatato che essa non copre i server dove serve: dei quattro server di community consultati nessuno appartiene all'utente, la schermata di invito elenca il solo server di prova, e l'invito richiede il consenso di chi amministra, che va chiesto e può essere negato.

L'utente ha deciso di usare comunque il token personale con DiscordChatExporter, e la decisione si registra con i suoi termini reali. I fatti gli sono stati esposti tre volte e non in forma attenuata: che automatizzare un account utente è vietato dalle condizioni d'uso, che la sanzione dichiarata è la terminazione dell'account, che il rilevamento è probabilistico e non certo, che un indirizzo aziendale è un segnale peggiore e non migliore di uno residenziale, e che l'autore stesso di quello strumento consiglia nel proprio README di usare un bot dove possibile. Ha riaffermato la scelta dichiarando di accettare il rischio, e ha precisato la cadenza: poche esportazioni all'anno, non un presidio continuo.

La decisione è sua perché il rischio ricade sul suo account, e la cadenza dichiarata è precisamente il fattore che abbassa la probabilità di rilevamento, poiché ciò che la piattaforma cerca sono schemi di traffico anomali. Vale registrare che si tratta di una violazione di condizioni contrattuali e non di un illecito, che il materiale letto è quello che l'utente vede già come membro legittimo di quei server, e che l'archivio è personale e non redistribuito.

Ne discendono quattro conseguenze operative. Il token non entra in alcun file, nemmeno in `.env`, e si incolla nel comando al momento dell'uso: un token in un file è un token che prima o poi finisce in un commit, e la cadenza rara rende il costo di incollarlo nullo. Gli export vivono sotto `_notes/fonti/dce/`, escluso dal version control, e restano locali perché sono contenuto di terzi. La via del bot resta preferibile e non viene abbandonata dove il consenso si ottenga, perché non mette a rischio nulla e produce aggiornamenti incrementali che una esportazione periodica non dà. E i quattro accorgimenti sul materiale di terzi restano invariati, perché non dipendono dalla via con cui il materiale è stato ottenuto: identificativo dell'autore conservato accanto al contenuto, luogo unico, eliminazione del grezzo quando la sintesi lo ha reso superfluo, e nessuna redistribuzione.

Una prescrizione riguarda l'agente e sta anche nella regola, perché è la parte che rende la decisione operativa invece di litigiosa: il fatto va esposto una volta, con i suoi termini e senza ammorbidirlo né gonfiarlo, e dopo la riaffermazione dell'utente si procede e si registra, senza riproporre l'obiezione a ogni passo. Riproporla è inutile per chi ha già deciso e trasforma una avvertenza in un ostacolo.

La procedura d'uso completa, dai file da scaricare al token ai comandi alla catena verso il registro delle fonti, sta in `docs/22-strumenti.md`, e non in una conversazione: una procedura che vive in chat è perduta alla sessione successiva.
## ADR-020 Settimo e ottavo sottoprogetto, e una sola decisione di perimetro per entrambi

Data: 2026-08-31. Stato: accettata quanto all'apertura dei track; la decisione di perimetro che essi aprono è dichiarata aperta e non è presa qui.

Il progetto accoglie due sottoprogetti nuovi, `poke-ace` e `generation-from-switch`. Il primo impiega l'esecuzione di codice arbitrario nei giochi di terza generazione per scrivere i dati di un esemplare direttamente nel salvataggio. Il secondo studia le vie con cui un esemplare entra nella collezione passando dai giochi per console moderna, e in particolare i bot di scambio automatico che la comunità ospita.

Vale dire perché non sono un unico track e perché non sono un ampliamento di quelli esistenti, dato che entrambe le letture erano disponibili. Non sono un track solo perché la tecnica, l'hardware e la comunità di riferimento non hanno nulla in comune: uno scrive byte in un salvataggio proprio con un difetto del motore di testo, l'altro riceve un esemplare da un servizio di terzi attraverso lo scambio in rete. E non sono un ampliamento del ponte fra generazioni, che pure documenta già la medesima tecnica in `docs/09-esecuzione-codice.md`, perché là essa serve a trasferire un esemplare che esiste, e qui a produrne uno che non esiste: è la differenza fra un canale e una sorgente, e confonderla porterebbe a valutare con i criteri del trasferimento un problema che è di provenienza.

La ragione per cui nascono adesso non è tecnica ma è l'obiettivo dichiarato dall'utente, cioè avere in Pokemon Home la collezione più completa possibile e tenerla come lavoro di una vita. Quell'obiettivo, registrato in ADR-017 e ora scritto in `roadmap.md` sopra i singoli track, rende pertinente ogni via che produca un esemplare, e ne rende pertinente anche il costo.

La parte sostanziale di questa decisione è che la questione di perimetro che i due track aprono è una sola, non due, e va decisa insieme. Le due vie differiscono per tecnica e coincidono in ciò che conta: entrambe mettono in Home un esemplare la cui provenienza non è una partita giocata, entrambe cadono sotto la medesima politica ufficiale sui dati alterati, ed entrambe espongono il medesimo account alla medesima sanzione dichiarata, cioè la sospensione dell'accesso a Home, temporanea o indefinita a discrezione del titolare e senza rimborso. Deciderle separatamente produrrebbe la contraddizione di accettare il rischio per una via e rifiutarlo per l'altra a parità di esposizione.

La decisione resta aperta e la sua istruttoria è chiusa, cioè non manca conoscenza per prenderla ma manca la scelta. Ciò che si sa è scritto e verificato: i byte prodotti possono essere identici a quelli autentici, Home conserva sul proprio lato la via da cui un esemplare è entrato, quindi a parità di dati la storia differisce, e l'eccezione della politica per chi possiede dati alterati senza intenzione non copre chi li produce o li richiede consapevolmente. Ciò che non si sa, e non si può sapere prima di ottobre 2026, è quali controlli il servizio applicherà, perché la compatibilità che li renderebbe osservabili non esiste ancora.

Ne discende la prescrizione operativa. Fino alla decisione i due track producono conoscenza e non esemplari, e questo va scritto nelle loro schede invece di lasciarli con l'aspetto di essere in corso. Esiste un passo che non richiede la decisione e che va fatto prima, perché è quello che ha il maggiore potere di falsificazione a costo nullo: confrontare i dati che il costruttore di esemplari della comunità produce per una distribuzione di evento con quelli che il track delle distribuzioni ricostruisce dal metodo di generazione originale. È fattibile senza hardware e senza toccare alcun account, e il suo esito ricade su entrambe le vie, perché se i due risultati coincidono la via lenta perde la sua unica giustificazione tecnica e resta soltanto quella di provenienza, mentre se divergono la via rapida è falsificata sui dati e non sulle congetture.

Il registro delle fonti porta le due sigle nuove, `ACE` e `GEN`, e gli undici strumenti della comunità sono inventariati con la funzione di ciascuno e con lo stato di lettura dichiarato voce per voce, perché la maggior parte non è stata aperta e il registro non deve far sembrare consultato ciò che non lo è.

## ADR-021 La porta di ottobre 2026 corregge la scadenza ma non la pianificazione

Data: 2026-08-31. Stato: accettata. Corregge un fatto su cui poggiavano ADR-017 e la roadmap, senza rovesciarne le conclusioni operative.

Il progetto ha dichiarato per tre giorni che la chiusura di Pokemon Bank del 26 febbraio 2027 fosse la scadenza oltre la quale nessun esemplare anteriore all'ottava generazione potesse raggiungere Pokemon Home. L'affermazione era corretta quando è stata scritta e non lo è più: un annuncio ufficiale del 13 agosto 2026, letto il 2026-08-31, dice che le versioni per console moderna di Rosso Fuoco e Verde Foglia si collegheranno a Home a ottobre 2026 con l'aggiornamento 4.1.0 del servizio. Per la terza generazione si apre quindi una seconda porta che non dipende da Bank.

La correzione va registrata come decisione e non come nota, perché cambia che cosa è urgente. La scadenza resta assoluta per la prima, la seconda, la quarta e la quinta generazione, la cui catena verso Home passa necessariamente da Bank e da Poke Transporter. I due passaggi interni, dalla terza alla quarta generazione con il Parco Amico e dalla quarta alla quinta con il Trasferitore, sono funzioni locali dei giochi e sopravvivono alla chiusura del servizio: la corsa contro il tempo riguarda quindi il solo tratto finale, e non l'intera catena come la pianificazione precedente assumeva.

La parte che si decide, e che è il motivo per cui questa non è una semplice rettifica, è che la porta nuova non entra nella pianificazione come se funzionasse. Non si sa quali controlli il servizio applicherà a un esemplare che entri da là, la stessa fonte che ne annuncia l'apertura raccomanda di trasferire per la via ufficiale ciò che si può trasferire ora invece di attendere un aggiramento, e il trasferimento verso quei giochi è dichiarato a senso unico. Si decide quindi di continuare a pianificare sulla catena storica per tutto ciò che essa può portare, di trattare la porta nuova come una possibilità da provare su materiale sacrificabile quando esisterà, e di non rimandare alcun passaggio già possibile in attesa di essa. Il costo di questa prudenza è nullo se la porta funziona, mentre il costo dell'assunzione opposta, se non funziona, è la perdita definitiva di tutto ciò che sarebbe passato da Bank.

Va registrato inoltre un fatto che il progetto non aveva e che pesa sulla pianificazione più di quanto sembri: il trasferimento da Bank a Home richiede il piano a pagamento di Home, mentre Bank in chiusura è gratuito, e il piano gratuito di Home conserva trenta esemplari. Una catena completata fino a Bank non è quindi una collezione al sicuro, e il piano a pagamento va messo nel conto del tratto finale invece di scoprirlo là.
## ADR-022 Nono sottoprogetto: la conservazione del supporto, e la sola priorità dichiarata del progetto

Data: 2026-09-01. Stato: accettata.

Il progetto accoglie un nono sottoprogetto, `cart-battery-restoration`, il cui oggetto è sostituire la batteria tampone delle cartucce di prima e seconda generazione conservando il salvataggio che vi si trova. Nasce da una richiesta dell'utente su due cartucce precise, Rosso e Argento, accompagnata da una domanda: se un salvataggio si possa riprendere dopo il guasto della batteria.

La risposta a quella domanda è no, ed è la prima cosa che questa decisione registra perché una speranza mal fondata consuma il tempo che serve alla sola azione utile. Il salvataggio vive in una memoria statica volatile alimentata, a console spenta, da una pila al litio saldata sulla scheda; quando la pila scende sotto la tensione di ritenzione il contenuto cessa di esistere. I bit non sono danneggiati ma assenti, e nessuno strumento, servizio o laboratorio li ricostruisce.

Vale dire perché è un track a sé e non una sezione di un altro, dato che entrambe le letture erano disponibili. Non sta nel track del ponte fra generazioni, che legge quei salvataggi ma non si occupa di ciò che li tiene in vita, e non sta nel track di Smeraldo, che è di terza generazione e ha un problema diverso. La sua materia non è un formato né un protocollo ma il supporto fisico, e il progetto non aveva alcun luogo dove quella materia stesse.

La parte sostanziale di questa decisione è una priorità, ed è la sola che la roadmap contenga. Quel track precede gli altri otto. La ragione non è che sia più importante ma che è il solo la cui scadenza non è annunciata da nessuno: le altre scadenze del progetto stanno su un calendario e si possono pianificare, questa è la carica residua di una pila saldata nel 1998 e si consuma in silenzio. Tutto il resto è rimandabile senza perdita definitiva; questo no. Ne segue anche un ordine interno al track, cioè che la cartuccia di seconda generazione precede quella di prima, perché la sua pila alimenta anche l'orologio in tempo reale, che è un carico attivo, e si scarica molto più in fretta.

Una conseguenza operativa va registrata qui e non soltanto nel runbook, perché è un rischio e non una procedura. Il lettore che questo progetto impiega, nella revisione in cui la tensione è controllata dal software, avvia l'interfaccia nella modalità della terza generazione, cioè a tre virgola tre volt; una testimonianza del canale di assistenza del produttore riferisce che inserire una cartuccia di seconda generazione in quella condizione cancella il salvataggio, e aggiunge il dettaglio che rende il fatto pericoloso, cioè che avviene anche senza premere il pulsante di connessione. È un modo di perdere il dato prima di avere fatto alcun backup, il rimedio è una sequenza e non un'impostazione, e la regola generale che ne discende entra nel patrimonio del progetto: su un dispositivo dove la tensione è scelta dal software, il valore predefinito non è una garanzia e si verifica sull'indicatore fisico, perché è il solo testimone che non dipende dallo stesso software che potrebbe avere sbagliato.

Il perimetro del track dichiara dove finisce l'assistenza. La saldatura è manuale, l'agente non la esegue e non la osserva, e su una cartuccia di vent'anni l'errore non è un file da riscrivere ma una piazzola di rame staccata. Nella comunità del lettore esiste un servizio di sostituzione con prova e spedizione di ritorno per una cifra dell'ordine dei venti dollari, cioè meno di quanto costi una cartuccia di quei titoli: la scelta fra farlo da sé e affidarlo è dell'utente ed è registrata come aperta. Ciò che non è una scelta è l'ordine dei passi, perché prima si estrae e si verifica, e solo dopo si tocca il ferro.

## ADR-023 Il confronto sul corpus chiude la componente tecnica della scelta fra le vie di generazione

Data: 2026-09-01. Stato: accettata. Chiude il passo che ADR-020 dichiarava di maggior valore fra quelli disponibili.

ADR-020 aveva individuato, fra le verifiche possibili, quella con il maggiore potere di falsificazione a costo nullo: confrontare i dati che il costruttore di esemplari della comunità produce per una distribuzione di evento con quelli che il track delle distribuzioni ricostruisce dal metodo di generazione originale. Il confronto è stato eseguito e ha prodotto un esito e uno strumento.

L'esito è che le due vie concordano sui dati. La tabella delle ventiquattro permutazioni delle sottostrutture coincide su tutte le righe, e le due derivazioni sono indipendenti perché la nostra viene dalla macro del disassemblato del gioco. Sull'inventario delle distribuzioni le chiavi in comune sono trentacinque, con accordo sul metodo di generazione su venticinque casi confrontabili su venticinque e sulla derivazione del sesso dell'allenatore su diciannove su diciannove. E sul corpus di esemplari conservati che il costruttore porta con sé, il modulo scritto per questa verifica riproduce i valori individuali su duecentonove vettori su duecentonove, il valore di personalità su duecentotto, e il sesso dell'allenatore su cento su cento per la derivazione a scorrimento di sette, sbagliando con la frequenza del caso sulle altre, che è la controprova che la formula è una formula e non una coincidenza.

Ne discende la decisione, che è di chiudere una questione e non di aprirne una. La scelta fra ricreare la distribuzione originale su hardware proprio e scrivere i byte dell'esemplare non ha più alcuna componente tecnica: non esiste un vantaggio della prima via sul piano dei valori, perché i valori sono gli stessi. Ciò che le distingue è soltanto la provenienza, che è la grandezza su cui il progetto ha già stabilito, in `poke-ace/STUDIO-02`, che il servizio di destinazione tiene un archivio proprio e appone un marchio visibile. La decisione fra le due vie diventa dunque interamente una decisione di perimetro dell'utente, e non è più rimandabile in attesa di una verifica tecnica, perché la verifica tecnica è stata fatta.

Il guadagno collaterale è codice, e va registrato perché resta al progetto anche se la decisione andasse nel senso di non usare mai la via rapida. Il modulo `pokebridge/eventi.py` porta le formule verificate e la ricerca inversa dei semi a sedici bit, che è esaustiva e non euristica perché lo spazio ha sessantacinquemilacinquecentotrentasei elementi; `tests/test_eventi.py` la collauda con undici prove, fra cui un controllo negativo sul vettore deviante del corpus; e `tools/confronta-ace-builder.py` rende il confronto ripetibile invece che aneddotico. Da un esemplare autentico del decennale, quando il lettore arriverà, si ricaverà il seme che lo ha generato: è il modo di verificare che una ricreazione sia fedele a un originale posseduto e non soltanto conforme a una tabella.

Due difetti trovati nel costruttore vanno registrati perché uno ha conseguenza operativa. La sua tabella dei caratteri colloca gli accentati nella fascia che il sorgente del gioco riserva ai sillabari giapponesi e alle cifre, dichiarando nel proprio commento di derivare dalla documentazione di dominio, e la sua stessa tabella assegna due caratteri al medesimo byte, il che la rende non invertibile indipendentemente da qualunque confronto: un soprannome con una lettera accentata scritto con quello strumento non produce l'accento. Per l'allenatore della distribuzione italiana del decennale la conseguenza è nulla, perché è di sole maiuscole e cifre. L'altro difetto è una voce del corpus il cui valore di personalità il proprio seme non produce, mentre i valori individuali dallo stesso seme tornano esatti: la voce è internamente incoerente, ed è conservata nella nostra suite come controllo negativo perché un modello che spiega anche il caso deviante è di natura diversa da uno che ha avuto fortuna.
## ADR-024 I salvataggi di terze parti si impiegano, con l'obbligo di controllarli

Data: 2026-09-01. Stato: accettata. Riapre esplicitamente la sezione sui salvataggi di terze parti di `rules/hardware-and-perimeter.md`, che prescriveva questa forma di decisione.

La regola sull'hardware escludeva i salvataggi scaricati da internet, con la motivazione che sono la causa principale delle sanzioni quando poi vengono impiegati in linea o depositati, e che il rischio ricade sull'account e sulla console e non sul file. La medesima regola prevedeva che, se un giorno servisse importarne uno, la decisione fosse presa esplicitamente e registrata come ADR invece di essere fatta scivolare dentro un altro lavoro. È il caso che si è presentato.

Il fatto è stato esposto una volta, nei suoi termini e senza attenuarlo, nella sezione dedicata di `recreate-pokemon-distributions-events/STUDIO-04-campagna-di-trasferimento-e-il-tracciatore.md`. L'utente ha riaffermato la scelta aggiungendo una condizione propria, cioè la consapevolezza che quei salvataggi vanno controllati. La condizione entra nella decisione e non è un commento: è la parte che la rende diversa da un uso incauto.

Ne discende la decisione in quattro punti.

Il primo è che i salvataggi procurati in rete si possono impiegare, e che l'uso preferito resta la lettura. Aprire un salvataggio sul calcolatore per ricavarne i valori di campo non tocca la console né l'account, e per i circa centosessanta eventi che il catalogo del progetto elenca senza disporre di un corpus di esemplari conservati, un archivio letto è la sola fonte dei valori storici. Da un esemplare letto la ricerca inversa ricava il seme, e da quel seme il progetto rigenera l'esemplare con il proprio codice: ciò che entra in un salvataggio proprio è allora prodotto qui, e la questione dell'importazione non si pone nemmeno.

Il secondo è che l'importazione, dove serva, è ammessa e subordinata al controllo. Nessun esemplare di provenienza altrui entra nella catena senza essere prima passato dal verificatore di conformità nel contesto della propria generazione. La procedura è quella già stabilita e provata il 2026-09-01: si apre, si giudica, si corregge ciò che il verificatore contesta, si registra la correzione con la sua autorità, e soltanto allora si prosegue. Un esemplare che il verificatore rifiuti e che non si sappia correggere non entra: è la forma operativa della condizione posta dall'utente.

Il terzo è che la provenienza della fonte va distinta e scritta, perché la parola scaricato copre cose che non si somigliano. Un archivio di conservazione mantenuto da un progetto della comunità, che il registro delle fonti di questo lavoro elenca già fra le implementazioni di riferimento, e un salvataggio anonimo trovato in un forum hanno verificabilità diverse: il primo è citabile e il secondo no. La regola come era scritta non faceva la distinzione, e questa decisione la introduce senza applicarla in silenzio. Ogni salvataggio impiegato va registrato in `SOURCES.md` con la propria provenienza e il proprio livello, come qualunque altra fonte.

Il quarto è il perimetro che resta chiuso, e va detto perché una decisione che non dichiari i propri limiti li perde. Nessun salvataggio di terze parti viene ridistribuito, nessuno entra nel version control, e gli esemplari che ne provengono non si scambiano con altri presentandoli come propri. Il rischio residuo resta quello che la politica ufficiale dichiara, e la clausola che due fonti indipendenti ripetono, cioè che la valutazione corrente potrebbe cambiare, resta valida: il tracciatore rende ciò che entra identificabile in modo persistente, e questa decisione non lo cambia.

Va registrato per onestà che questa decisione riguarda l'importazione e non risolve la decisione più grande, che resta aperta: se impiegare esemplari la cui provenienza non è una partita giocata dentro l'account che custodisce la collezione. Quella è registrata in `pending.md` dal 2026-08-31 e non viene presa qui.
## ADR-025: la tabella dei caratteri giapponese viene dal verificatore e non dal disassemblato

Data: 2026-09-01. Stato: accettata.

Contesto. Il progetto ha una regola che non ha mai violato, cioè che le tabelle di dati non si trascrivono ma si generano da un disassemblato, e la regola è nata da un difetto concreto: le fonti secondarie sbagliavano la tabella dei caratteri in due punti, con un errore che produce nomi plausibili invece di un fallimento visibile. Per la tabella giapponese della terza generazione quella via non è disponibile, perché il disassemblato che il progetto clona è quello della versione internazionale e la sua tabella è quella internazionale. Senza la tabella giapponese cinquanta voci del catalogo degli eventi e il soprannome di ogni uovo restano non scrivibili.

Decisione. La tabella giapponese si estrae dal codice della implementazione di riferimento, cioè dal verificatore di conformità che la comunità usa, e la sua provenienza si dichiara dentro il file di dati come di rango diverso da quella delle altre tabelle. L'estrazione resta programmatica e non manuale, quindi la regola sul non trascrivere è rispettata; ciò che cambia è il rango della fonte, e cambiarlo in silenzio sarebbe stato il difetto.

Conseguenze. La scelta è difendibile per una ragione che vale enunciare perché è più forte della necessità: quella tabella non è soltanto la migliore disponibile, è anche la tabella con cui i nostri esemplari verranno letti quando saranno giudicati. Se il verificatore leggerà i nostri byte con la sua tabella, la tabella con cui li scriviamo deve essere la sua, e in questo caso specifico una fonte di rango inferiore è preferibile a una di rango superiore che descriva un'altra edizione del gioco. Resta aperto che se un giorno il progetto clonasse un disassemblato della versione giapponese, la tabella andrebbe rigenerata da quello e le due andrebbero confrontate: una divergenza fra loro sarebbe informazione, non un fastidio.

## ADR-026: il completamento del Pokedex in Home è l'obiettivo principale, e diventa un sottoprogetto

Data: 2026-09-02. Stato: accettata.

Contesto. Il progetto nasce come raccolta di sottoprogetti paralleli, e il `CLAUDE.md` li descrive esplicitamente come obiettivi diversi che avanzano in parallelo e non come fasi di una sequenza. L'obiettivo del completamento della collezione in Pokemon Home era invece dichiarato nella prosa di più track senza avere una casa propria, e la sua assenza produceva due difetti. Il primo è che le decisioni che lo riguardano finivano nella scheda del track degli eventi, che non dichiara fra i propri percorsi coperti nulla che riguardi le altre generazioni, cioè il punto cieco esatto contro cui il `CLAUDE.md` mette in guardia. Il secondo è che senza una casa nessuno misurava la sua grandezza, e il progetto pianificava il tempo su una stima invece che su un numero.

Decisione. Il completamento del Pokedex in Home diventa un sottoprogetto, `pokedex-home-completo/`, con la sua scheda di contesto, la sua riga nella tabella di verifica, la sua riga nel blocco del punto di ripresa e la sua riga nella tabella dei track, e con il quarto passo della procedura eseguito, cioè l'estensione del `covers-paths` delle schede trasversali. Nello stesso tempo esso è dichiarato obiettivo principale: gli altri sottoprogetti possono concorrervi e restano ciascuno autonomo, con uno scopo proprio che vale anche se questo non si completasse.

Conseguenze. La prima è che il numero si è potuto misurare, e la misura ha cambiato il piano: la chiusura della banca non vincola il Pokedex, né al livello delle specie né a quello delle forme. La seconda è che la relazione fra i track diventa dichiarata invece di implicita, e questo ha un effetto sulle priorità che vale enunciare: un track può essere prioritario per il proprio scopo autonomo pur non essendolo per l'obiettivo principale, e viceversa. La terza è che la parola completo resta da definire, ed è ora una decisione aperta con un posto dove stare.

## ADR-027: la disponibilità per titolo si genera, e la deroga dichiarata poche ore prima si ritira

Data: 2026-09-02. Stato: accettata, e sostituisce una dichiarazione della medesima giornata.

Contesto. La sezione 12 di `recreate-pokemon-distributions-events/STUDIO-04`, scritta poche ore prima, dichiarava che la tabella di disponibilità per specie e per gioco sarebbe stata autorata da fonti e non generata, in deroga alla regola del progetto, e ne dava la ragione: l'implementazione di riferimento tiene i propri dati di legittimità in duecento file binari compressi con struttura diversa per generazione, e leggerli avrebbe richiesto di riscriverne i lettori uno per generazione.

Decisione. La deroga si ritira, perché era fondata su un errore di ricognizione. La domanda sulla disponibilità non richiede i dati degli incontri ma quelli di presenza, che stanno altrove e in forma molto più semplice: le tabelle delle statistiche di base sono array di record a dimensione fissa, un record per voce, con un contrassegno di presenza in un bit noto, e si leggono in cinquanta righe senza riscrivere alcun lettore. La tabella si genera dunque, e `tools/disponibilita-titoli.py` la genera.

Conseguenze. La prima è che la regola del progetto resta intatta e non ha eccezioni su questo dato. La seconda è una lezione sul metodo che vale registrare, perché l'errore è del genere che si ripete: avevo guardato l'insieme dei file che *nomina* la cosa cercata, cioè gli incontri, e avevo concluso dalla loro difficoltà che la cosa fosse difficile. La domanda giusta non era quali incontri esistano in un titolo ma quali voci quel titolo contenga, che è un dato diverso e più vicino. Prima di dichiarare una deroga a una regola conviene chiedersi se la difficoltà stia nel dato o nella formulazione della domanda.

## ADR-028: fra il generatore e il verificatore della fonte vince il verificatore

Data: 2026-09-02. Stato: accettata. Promuove a criterio una osservazione fatta due volte.

Contesto. L'implementazione di riferimento che questo progetto impiega come fonte contiene due parti che possono contraddirsi: un generatore, che compone un esemplare da un incontro, e un verificatore, che giudica se un esemplare sia legittimo. Nei due giorni fra il 2026-09-01 e il 2026-09-02 le due parti si sono contraddette due volte. La prima sul vincolo che lega il seme al bit del sesso dichiarato, dove il generatore scrive il valore dichiarato e il verificatore pretende che il seme lo produca. La seconda sul nome dell'allenatore di un uovo, dove il generatore, incontrando un carattere che la tabella della lingua non contiene, interrompe la scrittura e lascia il campo vuoto, mentre il verificatore rifiuta un nome di lunghezza nulla con una regola esplicita.

Decisione. Dove il generatore e il verificatore della fonte divergono, si segue il verificatore. La ragione non è di gerarchia fra le due parti ma di funzione: è il verificatore a giudicare gli esemplari che questo progetto produce, quindi è la sua nozione di correttezza a determinare se un esemplare sarà accettato.

Conseguenze. La prima è che un difetto del generatore della fonte non è nostro da correggere, e adeguarsi a esso significherebbe ereditarlo. La seconda è un vincolo su come si legge quella fonte: osservare che cosa il suo generatore faccia in un caso limite non stabilisce quale sia il comportamento corretto, perché ciò che un programma fa in un caso che non ha previsto è soltanto ciò che accade. La terza, che è la più utile, è che le due parti della fonte formano insieme un presidio più forte di ciascuna: quando divergono, la divergenza stessa segnala un caso limite che vale studiare, ed è esattamente così che sono stati trovati i due difetti.

## ADR-029: iniettare uno stato di avanzamento non è importare un esemplare

Data: 2026-09-02. Stato: accettata. Introduce una distinzione che ADR-024 non faceva e che il lavoro corrente ha reso necessaria.

Contesto. Il collo di bottiglia della catena verso il deposito è il primo passaggio, cioè il Parco Amici, che muove sei esemplari per sessione e ha un limite giornaliero. Per usarlo serve un salvataggio di quarta generazione in cui il Parco Amici sia disponibile, e questo richiede di avere completato la storia principale di quel gioco. L'utente possiede tre cartucce di quarta generazione, più una quarta di Johto che ha dichiarato il 2026-09-02, e ha indicato la via di iniettare in quelle non completate un salvataggio che abbia già il Parco Amici disponibile, invece di completare tre giochi prima di poter cominciare.

ADR-024 aveva deciso che i salvataggi di terze parti si possono impiegare, con l'obbligo di controllarli, e aveva subordinato l'importazione al giudizio del verificatore esemplare per esemplare. Quella decisione parlava però di esemplari, e questo caso non ne muove nessuno: ciò che entra è uno stato di avanzamento, cioè un insieme di bandiere di evento che dicono che una storia è stata completata.

Decisione. Importare uno stato di avanzamento è ammesso e non richiede la procedura esemplare per esemplare, a tre condizioni. La prima è che il deposito e la squadra del salvataggio importato siano svuotati prima dell'uso, cosicché nessun esemplare di terzi resti nel percorso: se il salvataggio serve a sbloccare il Parco Amici, gli esemplari che ci sono dentro non servono a nulla e la loro presenza è solo un rischio. La seconda è che il salvataggio sia verificato integro e della lingua giusta prima di essere scritto, perché ogni passaggio della catena pretende la stessa lingua ai due capi e l'utente possiede cartucce italiane. La terza è che valga comunque il vincolo generale della regola sull'hardware, cioè il backup in doppia copia del salvataggio originale della cartuccia e il read-back verificato dopo la scrittura: qui non si sta importando un file, si sta sovrascrivendo una cartuccia.

Conseguenze. La prima è che il rischio dichiarato da ADR-024, cioè la sanzione legata a esemplari di provenienza altrui usati in linea o depositati, non si applica a questo caso, perché nessun esemplare di provenienza altrui arriva a destinazione. Resta il rischio proprio della scrittura su cartuccia, che è di natura diversa e che la regola sull'hardware già governa. La seconda è che questa decisione non tocca la questione grande che ADR-024 lasciava aperta e che resta aperta: se impiegare esemplari la cui provenienza non è una partita giocata dentro l'account che custodisce la collezione. La terza è che la distinzione fra stato ed esemplare va tenuta anche in avanti, perché ricorrerà: sbloccare una funzione, ottenere un oggetto necessario a un evento, avere una medaglia sono tutti stati, e nessuno di essi porta con sé la questione della provenienza degli esemplari.

Una nota sulla ridondanza, che è la ragione per cui questa decisione costa poco. La raccolta verificata il 2026-09-02 contiene sei salvataggi di quarta generazione, cioè due di Sinnoh in versione Diamante o Perla, uno di Platino e tre di Johto. Sono più di quelli che servono, quindi la scelta di quale usare si può fare sul criterio della lingua e dello stato invece di essere imposta dalla scarsità.
## ADR-030: sullo stato della catena si scrive, sulla procedura del deposito intermedio no

Data: 2026-09-03. Stato: accettata. Non modifica il limite di perimetro sul deposito intermedio: ne definisce il confine su un caso che si è presentato e che il limite, come era scritto, non distingueva.

Contesto. Il progetto porta un limite dichiarato in quattro file tracciati e motivato in una nota locale fuori dal controllo di versione: l'assistenza tecnica non copre l'installazione e l'uso del deposito intermedio e del suo strumento di trasferimento su questa console, e il limite non si riapre implicitamente dentro un altro lavoro. Il 2026-09-03 l'utente ha collegato quel deposito da sé e ha consegnato settantanove fotografie della sequenza, chiedendo che i passaggi fossero registrati.

La richiesta cade esattamente sul confine. Una parte di ciò che quelle fotografie contengono è procedura, cioè come si arriva a far partire quel software; un'altra parte è stato del progetto e vincoli che la catena impone al piano, cioè capienza del deposito, sorte degli oggetti tenuti, legame fra identificativo di rete e console, e un conto alla rovescia in corso. Il limite come era scritto non distingueva le due, e senza una distinzione scritta sarebbe eroso dalla prima richiesta che le mescola.

Decisione. Si registra lo stato e si tacciono le procedure. Entrano nei file tracciati i fatti che servono a pianificare e non a operare: che l'ultimo anello della catena risponde, quali vincoli numerici impone, quali conseguenze quei vincoli hanno sul lotto che il progetto produce. Non entrano, in nessuna forma e in nessun file, le istruzioni per ottenere, installare o far funzionare quel software, né il troubleshooting dei suoi errori. Un codice di errore incontrato si può nominare come fatto accaduto quando serve a spiegare perché un requisito esista; non si può accompagnare con la sua soluzione.

Conseguenze. La prima è che le fotografie restano materiale locale e non entrano nel repository, come già prescrive la regola sugli screenshot, e la nota di studio che ne discende dichiara in apertura la distinzione invece di applicarla in silenzio. La seconda è che una circostanza della motivazione del limite va aggiornata senza che il limite cada: quella motivazione poggiava fra l'altro sull'assenza di un identificativo di rete anteriore alla chiusura del negozio digitale, e un identificativo è stato creato il 2026-09-03; poiché non produce alcuna cronologia di acquisti anteriore, la via ufficiale per ottenere quel software resta inesistente e la ragione del limite è intatta. È cambiato un presupposto tecnico e non il motivo. La terza è che questa decisione non autorizza nulla di nuovo: descrive dove passa una linea che esisteva già, cosicché la prossima sessione non debba ricavarla da capo e non rischi di spostarla senza accorgersene.
## ADR-031: l'ambito è tutti gli esemplari da distribuzione, e le classi restano separate

Data: 2026-09-04. Stato: accettata.

L'utente ha deciso che la collezione comprende tutti gli esemplari da distribuzione esistenti, senza eccezione e senza selezione, e che la ricerca deve andare a cercarli ovunque siano invece di fermarsi alle fonti che il progetto già leggeva. La decisione supera l'ambito registrato il 2026-09-03, che parlava di 2686 voci: quel numero veniva da due sole fonti e non era l'insieme.

Ne discende la struttura dell'asse degli eventi, che nasce ora da tre fonti e non da una. La prima è la tabella delle carte meraviglia di terza generazione, che vive nel codice del verificatore. La seconda sono i file binari della base dei doni segreti, dalla prima alla nona generazione. La terza sono le tabelle degli incontri del verificatore, dove stanno le distribuzioni in cui il dono era un oggetto, le periferiche, i giochi da console fissa, i doni interni condizionati e le incursioni da distribuzione.

Le classi restano dichiarate e separate nell'uscita, e questa è la parte della decisione che vale più del numero. Una distribuzione in cui il dono era un oggetto è un evento a tutti gli effetti, e la sola ragione per cui sfuggiva è che il verificatore la tiene fra gli incontri statici; un esemplare di Colosseum non è invece una distribuzione ma un incontro ordinario di un gioco diverso, irripetibile altrove; un dono condizionato di ottava generazione pretende il salvataggio di un altro gioco e non una consegna. Sommarle in un totale unico darebbe un numero grande e inutilizzabile, e toglierebbe a chi colleziona la possibilità di ridiscutere l'ambito senza rifare la misura.

Una classe resta fuori dall'asse per scelta motivata, ed è quella dei trasferimenti da Pokemon GO. Non sono esemplari da distribuzione ma una porta di ingresso permanente: dire che una specie è ottenibile da quel gioco è un'affermazione sulla sua reperibilità, cioè la materia dell'asse delle specie, e non un collezionabile in più con un allenatore e una data propri. Sono contati e visibili nel censimento, dove la loro classe dice che cosa sono, e non entrano nel conto che misura la coda di produzione. Non sono nemmeno entrati fra le fonti dell'asse delle specie, e la ragione è diversa: quella colonna dichiara i materiali che il progetto possiede, e un account di quel gioco con quelle specie non lo possediamo.

Resta dichiarato il limite che nessuna di queste scelte può togliere: il censimento copre ciò che il verificatore sa. Una distribuzione che nessuna sua tabella conosce non comparirebbe, e da dentro non avremmo modo di accorgercene. Il rimedio non è tecnico ma di metodo, cioè il confronto con elenchi indipendenti, e il primo è stato fatto lo stesso giorno con il deposito di Pokemon Box.

## ADR-032: l'ottenibilità sostituisce la presenza, e il risultato precedente era un limite inferiore

Data: 2026-09-04. Stato: accettata. Supera in parte il risultato registrato con ADR-026 e nella scheda del track.

Il progetto rispondeva alla domanda su quali specie la chiusura della banca porti via usando il contrassegno di presenza delle tabelle delle statistiche, cioè l'affermazione che una specie esiste nei dati di un gioco. Da lì veniva il risultato per cui tutte e milleventicinque le specie sono raggiungibili per via diretta e nessuna è vincolata dal 26 febbraio 2027.

La presenza non è però l'ottenibilità. Un gioco moderno porta i dati di una specie anche soltanto perché il deposito gliela possa mandare: la specie esiste nel gioco, si può allenare e mostrare, e non si può prendere. Contarla fra le raggiungibili per via diretta significa dichiarare raggiungibile senza banca qualcosa che per entrare in quel gioco dalla banca deve passare, che è il contrario del vero.

Si adotta quindi la misura per incontro. Per ciascun titolo a via diretta si leggono le tabelle dei luoghi selvatici, degli incontri fissi, dei doni, degli scambi interni e delle incursioni, e l'insieme si chiude rispetto alle evoluzioni di quel titolo nei due versi, perché chi prende la forma base ottiene le evolute e dalla riproduzione si ottiene la forma base di una linea. Ai risultati si aggiungono le specie consegnate come dono nelle generazioni che parlano al deposito direttamente, perché un dono non è un incontro e nessuna tabella degli incontri lo dichiara, ma un esemplare consegnato in quelle generazioni arriva al deposito senza toccare la banca.

L'esito numerico non cambia, cioè zero specie vincolate dalla scadenza, e il cambiamento non è nel numero ma in ciò che il numero significa: prima era un limite inferiore, ora è una misura. L'esito nuovo è che quattro specie non hanno alcun incontro in alcun gioco moderno, cioè Celebi, Deoxys, Victini e Zarude: non sono vincolate dalla scadenza perché un dono di ottava generazione le consegna, ma non si prendono giocando, quindi stanno sull'asse degli eventi e chi pianificasse di catturarle perderebbe tempo.

Si accetta infine che la misura sbagli in due versi opposti e che vadano dichiarati entrambi, perché una prima stesura ne dichiarava uno solo e concludeva che l'errore fosse tutto prudente. Il verso prudente è che le tabelle lette non sono tutte, e dove una fonte manca la specie che solo quella consegnerebbe risulta non ottenibile. Il verso rischioso è che gli incontri scritti in codice si leggono con una regola generosa che potrebbe raccogliere un numero che specie non è, e allora una specie risulterebbe ottenibile senza esserlo. Il presidio contro il secondo non è automatico ed è un campione fatto a mano sulle voci più sospette: chi tocchi quella regola rifaccia il campione.

## ADR-033: i gate di igiene si leggono nel testo dello strumento e non nel suo codice di uscita

Data: 2026-09-04. Stato: accettata.

Per un'intera sessione il codice di uscita di `tools/fix-accents.py --check` è stato usato come gate di igiene, e quel programma esce sempre a zero riferendo le sostituzioni nel testo e non nello stato. Ne è seguita una serie di dichiarazioni di igiene a zero che erano vere per quattro controlli su cinque e non stabilite per il quinto, mentre cinque file tracciati portavano seicentoquaranta forme non accentate.

Si stabilisce quindi che per gli strumenti della famiglia tipografica il gate è il testo prodotto e non il codice di uscita, e che il controllo si fa sui soli file per cui la convenzione vale, cioè i file Markdown tracciati: i sorgenti e gli script portano prosa in forma ASCII per scelta e non vanno contati.

Si stabilisce inoltre che una violazione trovata in un documento generato si corregge nella stringa del programma che lo genera e mai nel documento, perché correggere l'uscita di un programma la fa tornare sbagliata alla corsa successiva. È lo stesso principio per cui i documenti generati portano in testa l'avvertenza di non modificarli a mano.

## ADR-034: la fedeltà di un esemplare ricreato si misura sui campi che il verificatore incrocia

Data: 2026-09-04. Stato: accettata.

Il giudizio esterno sul lotto di prima e seconda generazione ha prodotto in tre giri consecutivi tre difetti che appartengono a una sola famiglia: campi distinti che sembrano lo stesso campo. La tabella degli eventi di seconda generazione porta due livelli e ne usavamo uno; il livello di incontro di un uovo non è quello dichiarato ma uno; la fase del giorno deve essere nulla per un dono e vera per un uovo già schiuso, cioè il contrario di come verrebbe da scriverla.

Nessuno dei tre era rilevabile dall'interno. Le prove interne verificavano che i campi fossero scritti dove la struttura li vuole, ed erano verdi mentre tutti e tre erano presenti; il difetto non stava nella scrittura ma nella scelta di quale valore scrivere, che è una domanda a cui solo il verificatore risponde perché è lui a incrociare i campi fra loro.

Si stabilisce quindi che per ogni gruppo di esemplari ricreati il criterio di conformità non è la suite interna ma il giudizio esterno su tutto il gruppo e non su un campione, e che ogni difetto trovato dal verificatore va chiuso con una funzione dedicata e una prova, invece che con una correzione in linea: una funzione si può provare, un'espressione sparsa in mezzo al codice no. Le cinque prove aggiunte in questa occasione, che portano il self-test da quindici a ventidue controlli, sono la forma che questo presidio prende.

## ADR-035: che cosa conta come forma alternativa, e perché la domanda non ha una risposta di fatto

Data: 2026-09-04. Stato: accettata. Chiude la questione che la scheda del track del Pokedex teneva aperta come indeterminatezza su 342 voci.

Il progetto ha cercato per giorni una risposta di fatto alla domanda su quali forme il deposito conti, e la risposta di fatto è arrivata il 2026-09-04 dalle schermate dell'applicazione: il Pokedex mostra una casella per specie. Alcremie compare come `No. 0869` con una sola silhouette, e non con nove caselle né con sessantatré. Il Pokedex Nazionale si ferma inoltre a 807, perché quel catalogo fu ritirato dopo la settima generazione, e tutto ciò che segue è ripartito fra i Pokedex per regione della scheda Giochi.

Ne segue che ai fini del completamento del Pokedex le forme non contano affatto, e che non esiste una singola percentuale da inseguire ma un insieme di contatori per regione. Questo però risponde a una domanda che non è la nostra, e la distinzione è il contenuto di questa decisione: l'obiettivo dichiarato del progetto è la collezione, cioè possedere gli esemplari, non accendere le caselle. Un Alcremie alla panna di fragola con la fragola sopra è un oggetto che si possiede o non si possiede, e che il catalogo non lo distingua dal suo gemello al latte non lo rende il medesimo oggetto.

La domanda su che cosa conti come forma non ha quindi una risposta di fatto, perché nessuna autorità la definisce per la collezione, e va decisa. Le definizioni candidate sono tre e portano numeri diversi.

La prima è la forma come indice del dato, cioè ciò che i giochi memorizzano nel campo della forma. Su questa base il progetto enumera 522 voci di forma e Alcremie ne porta nove, che sono le creme.

La seconda è la variante visibile, cioè ciò che un collezionatore distingue guardando. Su questa base Alcremie porta sessantatré combinazioni di crema e decorazione, e la discussione della comunità consultata il 2026-09-04 ne registra sette come aspetti cromatici distinguibili, il che dà la misura di quanto la definizione cambi il conto sulla medesima specie.

La terza è la voce ottenibile e conservabile, cioè la coppia di specie e forma che può esistere dentro una scatola. Su questa base si escludono le 170 voci di forma di sola battaglia, che nel deposito non possono esistere, e le 10 forme totemiche, che al trasferimento tornano alla forma base o non si trasferiscono affatto.

Si adotta la terza definizione, e il bersaglio dell'asse delle forme diventa quindi 342 voci: sono le 522 enumerate meno le 170 di sola battaglia e le 10 totemiche. Quelle 342 erano marcate come indeterminate proprio perché non si sapeva se il deposito le contasse; ora si sa che non le conta come caselle, e si decide che la collezione le conta come oggetti.

La decorazione di Alcremie resta fuori, e la ragione va scritta perché è il caso su cui la scelta pesa di più. Il campo che la porta non è il campo della forma: è un campo separato, come lo sono il fiocco o l'oggetto tenuto, e chiamare forma un parametro che il formato tiene altrove significherebbe cambiare la definizione per una specie sola. Alcremie contribuisce dunque con nove voci e non con sessantatré. Chi volesse le sessantatré perseguirebbe un obiettivo diverso e più grande, e la differenza su quella sola specie è di cinquantaquattro esemplari, cioè più di quanto pesino le forme di molte generazioni intere: è precisamente il genere di scelta che va fatta esplicitamente prima e non per accumulo dopo.

Resta dichiarato un limite di questa decisione. Essa non stabilisce che il deposito conservi le 342 come voci distinte nel proprio archivio, che è un fatto che nessuna schermata mostra: stabilisce che il progetto le persegue come oggetti. Se un giorno si scoprisse che il deposito le fonde, la decisione non cambierebbe, perché l'oggetto resterebbe distinto anche se il catalogo non lo mostrasse.
## ADR-036: una prova di simmetria non coglie un errore simmetrico

Data: 2026-09-04. Stato: accettata.

Il lettore dei depositi di sesta generazione decifra ciascun esemplare e ne rimette in ordine i quattro blocchi secondo una permutazione scelta dalla costante di cifratura. La direzione della permutazione era invertita: la tabella dice, per ogni posizione logica, quale blocco del dato cifrato la occupa, e il programma faceva l'opposto.

Il difetto non si è manifestato come un errore per due ragioni concorrenti, ed è la coppia a renderlo istruttivo. La prima è che la somma di controllo del formato somma parole a sedici bit ed è quindi invariante rispetto all'ordine dei blocchi: ogni struttura risultava valida e una parte di esse portava semplicemente campi presi dal blocco sbagliato, cioè numeri leciti nel posto sbagliato. La seconda è che il self-test verificava che cifrare e decifrare si annullassero, e passava: le due funzioni erano sbagliate nello stesso modo, e la loro composizione restava l'identità.

Se ne trae la regola che questa decisione registra. Una prova che verifichi la composizione di due funzioni inverse non stabilisce nulla sulla correttezza di ciascuna, perché un errore applicato in andata e disfatto al ritorno la lascia verde. Una prova di simmetria è quindi una prova di coerenza interna e non di correttezza, e va accompagnata da almeno un ancoraggio esterno: un valore atteso letto dalla fonte, un conto confrontato con quello del verificatore, un vettore noto. Nel caso presente il difetto è stato trovato soltanto confrontando il numero di esemplari letti dal nostro lettore con quello elencato dal rapporto del verificatore, cioè da fuori, ed era del dieci per cento su tutti e tre i file provati.

Ne discende una prescrizione operativa per i lettori di formato che questo progetto scrive. Ogni lettore deve avere, oltre alla prova di simmetria dove ha senso, almeno un controllo il cui valore atteso non venga dal lettore stesso: il conto delle voci confrontato con quello di una implementazione indipendente, il tetto di specie della generazione, la dimensione attesa di una tabella. È lo stesso principio per cui il progetto ha stabilito che le prove interne vanno dove il fallimento è visibile e il giudizio esterno dove non lo è, applicato al caso in cui il fallimento non è visibile nemmeno a una prova che sembra completa.

## ADR-037: i salvataggi esterni si valutano per provenienza, e i tre dei forum non sono una fonte di esemplari

Data: 2026-09-04. Stato: accettata. Precisa l'ambito di ADR-024 sull'uso dei salvataggi di terzi.

I cinque salvataggi di 3DS della raccolta sono stati sottoposti al verificatore uno per uno, con il rapporto sui box che ne dichiara la legittimità riga per riga. L'esito separa i cinque in due gruppi che coincidono esattamente con la loro provenienza, senza eccezioni.

I due che vengono dalla raccolta contribuita di Project Pokemon sono partite vere: Rubino Omega porta settecentotrentasette esemplari legali su settecentosessantanove, Y ne porta seicentoquarantasei su seicentosettantacinque con cinquecentosei specie distinte. Sono fonti utilizzabili.

I tre che vengono dai forum italiani sono costruiti: Rubino Omega B porta un esemplare legale su quattrocentosessantadue, X uno su quattrocentocinquantuno, UltraSole due su cinquecentocinquantotto, e in tutti e tre i punti allenamento superano il tetto su quasi ogni esemplare. La descrizione che il forum stesso dava di essi, cioè partite complete con valori individuali e punti allenamento al massimo, era esatta e ne descriveva la costruzione.

Su uno di quei tre la riparazione automatica è stata provata fino in fondo, correggendo punti allenamento, geolocalizzazione, data e luogo di incontro su centinaia di esemplari: il conto dei legali è passato da uno a uno. Se ne conclude che il difetto non stia nei campi che si possono riscrivere ma nel fatto che quegli esemplari non hanno una storia che stia in piedi, e che rimettergliela significherebbe rigenerarli, cioè fare per la sesta generazione ciò che il progetto fa per le prime tre. Non è una riparazione ed è un progetto a sé.

Si stabilisce quindi che i tre salvataggi dei forum restano nella raccolta come veicoli, cioè come partite avanzate su cui girare quando serva uno stato di avanzamento secondo ADR-029, e non come fonti di esemplari; e che i due di Project Pokemon sono fonti di esemplari a tutti gli effetti, con l'obbligo di verifica che ADR-024 già impone.

Si stabilisce inoltre un criterio di triage per i salvataggi futuri, che costa un solo rapporto sui box e sostituisce ore di lavoro: prima di studiare o riparare un salvataggio esterno se ne legge il rapporto e se ne conta la quota di legali. Sotto una quota bassa il file non è una fonte e nessuna riparazione lo renderà tale, quindi non vi si spende altro tempo.

## ADR-038: una struttura di dono è un modello e non un esemplare, e la differenza si misura sui valori

Data: 2026-09-04. Stato: accettata. Ritira l'affermazione che la quarta generazione fosse quasi gratis.

Il progetto aveva stabilito, guardando la forma della base dei doni di quarta generazione, che quella generazione non richiedesse alcuna ricostruzione del generatore pseudocasuale, perché la carta porta al proprio interno una struttura di esemplare completa e in chiaro. Il lotto prodotto su quella premessa è stato rifiutato dal verificatore in blocco, duecentoquarantasette voci su duecentoquarantasette.

La premessa era falsa e il modo in cui lo era va enunciato come regola, perché non riguarda soltanto quella base dati. La struttura era ben formata e insieme incompleta: somma di controllo corretta, specie nell'intervallo, livello ed esperienza coerenti, allenatore storico presente, e tuttavia i trenta bit dei valori individuali a zero su tutte e duecentoquarantasette le voci e il valore di personalità pari a uno su centodiciannove di esse, che nella convenzione della fonte non è un valore ma l'ordine di generarne uno non cromatico. Il dono non conteneva l'esemplare: conteneva la sua descrizione più il procedimento per completarla, e i bit mancanti erano 11218, forniti al momento della riscossione dalla console di chi riceveva.

Se ne trae la prescrizione che questa decisione registra. La completezza di una struttura non si stabilisce dalla sua forma ma dai suoi valori, e il controllo da fare prima di dichiarare che un dato è utilizzabile è statistico e non sintattico: si conta quante voci portino un campo interamente nullo e quante portino un valore che il formato riserva come segnale. Un campo nullo su tutte le voci non è un caso, è una dichiarazione di assenza; un valore piccolo e ricorrente in un campo che dovrebbe essere uniforme non è un valore, è un codice. Nessuna somma di controllo può dirlo, perché una somma verifica che i byte siano quelli che qualcuno ha scritto e non che siano tutti quelli che servono.

Ne discende anche la revisione di un giudizio di costo. La quarta generazione non è più economica della terza per la parte che conta, cioè la composizione dell'individuo: è la medesima classe di problema, con la differenza, reale ma di grado, che il modello fissa già specie, mosse, livello, palla, allenatore, lingua e fiocchi.

## ADR-039: la provenienza di un salvataggio è un indizio di priorità, non un criterio di qualità

Data: 2026-09-04. Stato: accettata. Restringe ADR-037, che resta valida nel proprio ambito.

ADR-037 aveva registrato che su cinque salvataggi di 3DS la provenienza predice la qualità senza eccezioni: i due della raccolta contribuita di Project Pokémon sono partite vere e legali quasi al cento per cento, i tre dei forum italiani sono costruiti e legali all'uno per mille. La regolarità era reale sul campione e la conclusione operativa, cioè leggere il rapporto sui box prima di spendere tempo su un file, resta giusta.

L'estensione della regolarità alla quarta generazione è però falsa, e il caso che la smentisce non è marginale. Dei due salvataggi di Argento SoulSilver della raccolta, quello di Project Pokémon porta novantuno esemplari, tutti legali, sessantuno specie e nessun esemplare da evento; quello del forum italiano ne porta quattrocentoquarantanove, di cui quattrocentoquarantacinque legali, trecentocinquantacinque specie distinte e diciassette esemplari da evento fatidici tutti legali con i loro allenatori storici. Il file del forum è il più ricco della raccolta ed è quello che ha fatto da testimone esterno alla correzione del generatore di quarta generazione.

Si stabilisce quindi che la provenienza non entra nel giudizio di qualità di un salvataggio. Entra al più nell'ordine con cui si esaminano i file quando sono molti, e anche là il costo di sbagliare ordine è un minuto. Il criterio resta uno solo ed è il rapporto sui box del verificatore, che va letto su ogni file prima di trarne qualsiasi conclusione, e nessuna regolarità osservata su un campione piccolo lo sostituisce.

Vale enunciare anche la ragione per cui la regolarità reggeva sul primo campione e cade sul secondo. I tre file di sesta generazione erano stati descritti dai forum stessi come partite complete con valori individuali e punti allenamento al massimo, cioè erano costruiti per uno scopo, il gioco competitivo, che impone di riscrivere ogni esemplare. Un salvataggio di quarta generazione di un forum non ha quella spinta, e può essere semplicemente la partita lunga di una persona. La variabile che predice la qualità non è dunque il sito da cui il file viene ma lo scopo per cui è stato costruito, che il sito non dichiara e il rapporto sui box invece rivela.

## ADR-040: le ventotto voci coreane di quarta generazione richiedono un veicolo coreano, e la scelta resta aperta

Data: 2026-09-07. Stato: proposta, con la decisione rinviata all'utente. Discende dal giudizio esterno del medesimo giorno sul lotto di quarta generazione.

Il lotto di quarta generazione è stato giudicato per intero: duecentodiciannove voci su duecentoquarantasette sono conformi, e le ventotto rifiutate sono tutte e sole quelle coreane, con un solo rilievo identico su ciascuna, cioè che il fiocco riservato alle distribuzioni ufficiali non può attraversare il servizio di scambio globale.

La causa è stata letta sul codice della fonte e non supposta, ed è una proprietà del sistema e non dei nostri byte. In quarta generazione i giochi coreani non potevano scambiare direttamente con quelli internazionali, per una ragione di rappresentazione: il coreano usa un blocco di glifi che le versioni internazionali non hanno in tabella. L'unico ponte fra i due mondi era il servizio di scambio globale, che nel passaggio sostituiva il nome dell'allenatore con una traslitterazione presa da un insieme chiuso di quattro nomi. Su quel medesimo ponte agiva però un filtro di contenuto, che rifiutava le uova e gli esemplari con quel fiocco. Ne segue che un esemplare da evento coreano in un salvataggio internazionale di quarta generazione è storicamente impossibile, e che la classe non è rara ma vuota.

Ne discende il punto che rende questa una decisione e non una riparazione. La condizione non è una proprietà dell'esemplare ma della coppia formata dall'esemplare e dal salvataggio che lo ospita: la regola confronta la lingua dell'allenatore attivo con quella dell'esemplare e si attiva soltanto quando le due cadono su lati opposti della barriera. Non c'è nulla da correggere nei byte, e non lo si potrebbe fare in ogni caso senza distruggere l'esemplare: togliere il fiocco lo renderebbe conforme e insieme falso, perché quel fiocco è ciò che dichiara la sua provenienza da una distribuzione ufficiale.

Le vie possibili sono tre e portano costi diversi.

La prima è rinunciare alle ventotto voci. Il costo si misura e vale cinque esemplari, non ventotto: le ventotto coprono ventitré specie e diciotto di esse hanno un gemello in un'altra lingua dentro il medesimo lotto, mentre Arcanine, Feebas, Munchlax, Rayquaza e Tangrowth compaiono fra i doni di quarta generazione soltanto in distribuzioni coreane. Le cinque specie restano ottenibili altrove nei giochi a via diretta, quindi la rinuncia non tocca l'asse del Pokedex; tocca l'asse degli eventi, che è quello sotto scadenza.

La seconda è usare un veicolo coreano di quarta generazione come stazione intermedia, caricandovi le ventotto voci e trasferendole poi in avanti. Richiede un salvataggio coreano di quarta generazione, e va verificato prima di sceglierla se il passaggio verso la quinta generazione, che è un trasferimento e non uno scambio, sia soggetto alla medesima barriera: la regola letta oggi riguarda lo scambio in quarta generazione e non dice nulla sul trasferimento in avanti, e senza quella verifica la via non è dimostrata percorribile.

La terza è cercare le cinque specie mancanti fra le distribuzioni delle generazioni successive, dove la barriera coreana non esiste più, e accettare per le altre diciotto il gemello di un'altra lingua. Costa una lettura della base dei doni di quinta generazione in avanti, che è lavoro già in programma per altre ragioni.

AGGIORNAMENTO del 2026-09-07. La verifica che questa decisione rinviava è stata fatta, e l'esito cambia il costo della seconda via. La barriera è delimitata nel sorgente da due condizioni concordi: il verificatore la applica soltanto quando il formato dell'esemplare è il quarto, e la regola restituisce falso quando la generazione dell'allenatore attivo non è la quarta. Non è quindi una proprietà dell'esemplare ma una condizione valutata su un esemplare di quarta dentro un salvataggio di quarta. Il passaggio verso la quinta è un trasferimento e non uno scambio, e una volta che l'esemplare è di quinta generazione quel controllo non viene eseguito. La seconda via è dunque percorribile e non sposta il problema di un anello: il suo costo è un salvataggio coreano di quarta generazione come stazione di passaggio, attraversata una volta sola, e non la perdita di cinque specie.

Si registra intanto il fatto e la misura, e si rinvia la scelta, perché le tre vie hanno costi che dipendono da materiale e da verifiche non ancora disponibili. Vale però fissare fin d'ora il criterio con cui si sceglierà: la seconda via si adotta soltanto se il trasferimento in avanti risulta libero dalla barriera, perché altrimenti sposterebbe il problema di un anello senza risolverlo, e la terza si adotta soltanto per le cinque specie e non per le diciotto, perché sostituire un gemello quando l'originale è disponibile impoverirebbe la collezione senza guadagno.

## ADR-041: l'asse dei cromatici è un secondo asse e non un fattore, e va misurato invece che moltiplicato

Data: 2026-09-07. Stato: accettata quanto all'ambito, aperta quanto alla misura.

L'utente ha stabilito il 2026-09-07 che la collezione comprende la versione cromatica di ciascuna voce, e che quindi la quantità globale è quasi il doppio. La decisione di ambito si registra come presa; ciò che questa decisione aggiunge è che il quasi non è una cautela di linguaggio ma la sostanza del problema, e che trattare i cromatici come un fattore due sarebbe un errore di misura e non una approssimazione.

Un cromatico non è una forma. La distinzione va enunciata perché governa dove l'informazione sta e come si conta. Una forma è un valore memorizzato in un campo della struttura, e si enumera leggendo quel campo dalle tabelle del gioco. La lucentezza non è memorizzata in alcun campo: discende da una relazione fra il valore di personalità e i due identificativi dell'allenatore, cioè dalla condizione che la somma esclusiva delle quattro parole a sedici bit sia minore di otto. Ne segue che un cromatico ha la medesima specie e la medesima forma del suo gemello ordinario, e che i due si distinguono soltanto per la loro storia di generazione. Per il catalogo sono la stessa casella; per la collezione, che ADR-035 ha stabilito contare oggetti e non caselle, sono due oggetti.

Il fattore non è due, e le ragioni per cui non lo è sono tre. La prima è che alcune specie non possono essere cromatiche per costruzione, perché il gioco lo impedisce nel codice dell'incontro: sono i blocchi che la comunità chiama shiny lock. La seconda è che il blocco non è una proprietà della specie ma dell'incontro, e la medesima specie può essere bloccata in un gioco e libera in un altro, o essere stata bloccata e poi liberata da una distribuzione successiva, come è accaduto ai quattro leggendari disgraziati e ai due di copertina della nona generazione. La terza è che dove il blocco esiste davvero e non è mai stato tolto, la voce cromatica non è difficile da ottenere: non esiste, e contarla nel bersaglio significherebbe fissare un obiettivo irraggiungibile.

Da qui la prescrizione, che è la parte vincolante di questa decisione. Il bersaglio dell'asse dei cromatici non si ottiene moltiplicando per due il bersaglio delle voci, e non si ottiene nemmeno sottraendo un elenco divulgativo. Si ottiene misurando, per ciascuna coppia di specie e forma, se esista almeno un incontro, in un qualsiasi gioco e per una qualsiasi via, la cui definizione ammetta la lucentezza. È la medesima disciplina già applicata all'ottenibilità con lo strumento che ha sostituito la presenza con l'incontro reale, e la fonte è la stessa, cioè gli archivi degli incontri del verificatore, dove ogni incontro statico e ogni dono dichiarano la propria lucentezza ammessa.

Va dichiarato per onestà che la misura non è gratuita e che il verificatore non la offre già fatta. Non esiste nel suo codice un elenco delle specie bloccate: l'informazione è distribuita su ciascun incontro, in nove generazioni di archivi con formati diversi, e ricavarla richiede uno strumento nuovo che li attraversi tutti. Finché quello strumento non esiste, l'elenco enciclopedico consegnato dall'utente vale come indicazione di dove guardare e non come bersaglio, secondo la regola generale del registro delle fonti.

Si stabilisce infine che l'asse dei cromatici non entra nella metà sotto scadenza fino a che la misura non è fatta, e la ragione è dimensionale. La metà sotto scadenza è definita da ciò che la chiusura della banca rende irrecuperabile, e un cromatico di una specie ottenibile in un gioco a via diretta non è in quella categoria; lo è invece il cromatico di un esemplare da evento, che condivide la sorte del suo gemello ordinario. L'asse va quindi partizionato con lo stesso criterio già usato per le voci ordinarie prima di entrare in qualsiasi pianificazione del tempo.

## ADR-042: la decorazione di Alcremie conta, e la definizione di forma alternativa si allarga

Data: 2026-09-07. Stato: accettata. Modifica ADR-035 sul punto che quella decisione aveva dichiarato come il più pesante.

ADR-035 aveva adottato per l'asse delle forme la definizione di voce ottenibile e conservabile, e su quella base aveva escluso la decorazione di Alcremie con un argomento preciso: il campo che porta la decorazione non è il campo della forma ma un campo separato, come lo sono il fiocco o l'oggetto tenuto, e chiamare forma un parametro che il formato tiene altrove avrebbe significato cambiare la definizione per una specie sola. Su quella base Alcremie contribuiva con nove voci, che sono le creme, e non con sessantatré.

La medesima decisione dichiarava però che la scelta pesava cinquantaquattro esemplari su una specie sola, e che era precisamente il genere di questione da decidere esplicitamente prima e non per accumulo dopo. L'utente l'ha decisa il 2026-09-07, e la decisione è per le sessantatré.

Ne segue che la definizione dell'asse cambia, ed è bene enunciarla nella forma nuova invece di lasciarla implicita in una eccezione. La voce da possedere non è più la coppia di specie e forma, cioè ciò che il formato memorizza nel campo della forma, ma la configurazione visibile e conservabile, cioè ogni combinazione di parametri che produca un esemplare distinguibile a occhio e che una scatola possa contenere. Restano fuori, come prima, le forme di sola battaglia e le forme totemiche, perché nessuna scatola le contiene; e restano fuori le megaevoluzioni e il fattore Gigantamax, per la decisione separata dell'utente del medesimo giorno, che poggia sullo stesso criterio, cioè che sono trasformazioni temporanee e non esemplari.

Va registrato che la definizione nuova è meno comoda della vecchia, e vale dire perché. La vecchia si calcolava da sola, perché bastava leggere un campo dalle tabelle del gioco; la nuova no, perché i parametri che concorrono all'aspetto stanno in campi diversi a seconda della specie e nessuna tabella li raccoglie. Ne segue che l'asse delle forme cessa di essere interamente misurabile dal dato e diventa in parte enumerabile solo da fonti di dominio, che è la ragione per cui il confronto con il foglio comunitario e la lettura di Bulbapedia sulle differenze di forma passano da controlli facoltativi a passi necessari.

Il bersaglio si sposta di conseguenza. La base resta il conto del foglio comunitario, cioè 1389 voci, che già comprende le sessantatré configurazioni di Alcremie e le centotre specie distinte nei due sessi; vi si aggiungono le voci che il foglio sottoconta e noi no, per ora le due forme originarie di Dialga e Palkia, da verificare.

## ADR-043: che cosa l'annuncio di ottobre toglie alla metà che scade, e l'istante esatto della chiusura

Data: 2026-09-07. Stato: accettata. Precisa e completa la correzione alla scadenza già registrata il 2026-08-31.

Il progetto sapeva dal 2026-08-31 che le versioni per console moderna di Rosso Fuoco e Verde Foglia si sarebbero collegate al deposito a ottobre 2026, e ne aveva tratto che per la terza generazione la chiusura della banca cessava di essere l'ultima porta. L'annuncio ufficiale è stato letto per intero il 2026-09-07, e il suo corpo porta cinque fatti che nessuna fonte secondaria riportava e che vanno registrati uno per uno.

Il primo è l'istante esatto della chiusura, che il progetto aveva finora come una data. Il servizio termina giovedì 25 febbraio 2027 alle diciannove del fuso del Pacifico, che nell'ora italiana è le quattro del mattino del 26 febbraio. La differenza non è pedanteria: il progetto scriveva 26 febbraio e lavorava implicitamente su una giornata intera che non esiste, perché di quel giorno restano quattro ore notturne. L'ultimo giorno utile pieno è quindi il 25 febbraio.

Il secondo riguarda due specie che il progetto aveva contato fra le quattro prive di qualsiasi incontro nei titoli a via diretta, insieme a Victini e Zarude. Nelle versioni per console moderna, dopo la Sala d'Onore, due biglietti vengono aggiunti automaticamente allo zaino: uno dà l'incontro con Lugia e Ho-Oh, l'altro con Deoxys. Deoxys esce quindi da quell'elenco, e vi esce anche Celebi, che il deposito regala a chi completi il catalogo dei due titoli. Le specie prive di ogni incontro passano da quattro a due.

Il terzo è che il completamento di quel catalogo non richiede di trasferire alcunché: una specie registrata nel catalogo dei due titoli risulta registrata anche nel deposito una volta stabilito il collegamento. È una via che costa gioco e non trasferimenti, e non consuma la capienza del deposito.

Il quarto è la capienza, che il progetto aveva come punto aperto e non misurato. Il piano a pagamento vale oggi seimila esemplari su duecento scatole da trenta, il piano gratuito trenta in una scatola sola, e con la versione 4.1.0 di ottobre 2026 il piano a pagamento sale a novemila senza cambiamento di prezzo. Confrontato con il bersaglio corrente, che con l'asse dei cromatici tende al doppio delle 1389 voci, il vincolo dimensionale non è stringente e non lo sarà.

Il quinto è che gli esemplari catturati con la palla della zona safari nell'applicazione per telefono diventano trasferibili per la prima volta, e che nel passaggio la loro palla diventa una palla estranea. È una via nuova che si apre e va tenuta perché tocca l'enumerazione delle palle, che è un asse che questo progetto non ha ancora aperto.

L'annuncio dichiara infine che la banca non è attualmente scaricabile, il che non è una notizia nuova ma è la conferma primaria di una condizione che il progetto aveva appreso dall'utente: le due voci che richiedono di averla scaricata prima del marzo 2023 restano fuori portata per questa via e vanno prodotte altrimenti.

Si stabilisce quindi che la partizione della lista fra ciò che scade e ciò che non scade va rifatta dopo ottobre e non prima, perché il canale nuovo cambia il denominatore, e che fino ad allora ogni conteggio di voci sotto scadenza va dichiarato provvisorio con questa ragione accanto.

## ADR-044: la completezza non si dichiara, si misura come chiusura, e ciò che manca si stima

Data: 2026-09-07. Stato: accettata. Nasce da una obiezione dell'utente che è fondata e a cui il progetto non aveva una risposta di metodo.

L'obiezione è questa: dopo settimane di ricerca continuano a comparire pezzi nuovi, e se una ricerca è completa deve essere completa. È corretta come osservazione e la risposta non è che i pezzi nuovi siano pochi: è che il progetto ha usato la parola completa in un senso che non poteva reggere, e che va sostituito con un criterio verificabile.

Ciò che il progetto aveva era la completezza rispetto a un archivio, non rispetto al mondo. La distinzione non è sottile ed è la causa strutturale di tutti i pezzi comparsi, perché le fonti che questo lavoro usa hanno coperture che non sono l'una contenuta nell'altra. La base dei doni del verificatore conosce le carte, cioè i file che una distribuzione consegnava, e non può conoscere per costruzione un evento che una carta non l'ha mai lasciata: la consegna fatta da un apparecchio che scriveva nel salvataggio, il biglietto che sbloccava un incontro invece di dare un esemplare, la ricompensa di un gioco della serie derivata. L'archivio di Serebii conosce gli eventi, cioè le cose accadute, e non sempre ne porta il dato tecnico. Il foglio della comunità conosce ciò che un collezionatore deve possedere, comprese le differenze di sesso e le varianti cromatiche che nessun campo del formato separa. Le tabelle del gioco conoscono le forme che il formato sa rappresentare, comprese molte che oggetti non sono. Quattro fonti, quattro coperture diverse, e nessuna che possa dichiarare la propria completezza dall'interno.

Da qui il criterio che questa decisione adotta, ed è verificabile invece che dichiarativo. Una enumerazione si dice chiusa quando una fonte nuova e indipendente non le aggiunge alcuna voce. Non è una proprietà dell'enumerazione ma della coppia formata dall'enumerazione e dalla fonte con cui la si prova, e si misura contando: quante voci la fonte nuova porta che noi non abbiamo, e quante ne portiamo noi che essa non ha. Finché quel primo numero è diverso da zero il lavoro non è finito, e il progetto lo dichiara invece di chiamarsi completo.

C'è però una domanda che il criterio da solo non risponde, ed è quella che l'utente sta ponendo davvero: quanto manca ancora. Anche quella si può stimare invece che temere, e lo strumento è lo stesso che l'ecologia usa per contare una popolazione che non si può censire, cioè la cattura e ricattura. Se una prima fonte porta $n_1$ voci, una seconda ne porta $n_2$, e le voci presenti in entrambe sono $m$, allora la dimensione della popolazione vera si stima come il prodotto delle due diviso per la sovrapposizione. La quantità utile non è la stima in sé ma la sua differenza dall'unione osservata, che è il numero di voci che nessuna delle due fonti ha visto.

Vanno dichiarate le tre ipotesi su cui quella stima poggia, perché due delle tre nel nostro caso non valgono e la conseguenza va conosciuta. La popolazione deve essere chiusa, cioè non deve nascere né sparire nulla mentre la si misura, e questo per noi è quasi vero perché una distribuzione avvenuta non smette di essere avvenuta, salvo le distribuzioni nuove che continuano a nascere. Le due fonti devono essere indipendenti, e questo per noi è falso: chi compila l'una legge l'altra, e le due si guardano. Ogni voce deve avere la medesima probabilità di essere vista da entrambe, e anche questo è falso, perché una distribuzione con una carta è vista dal verificatore per costruzione e una senza carta non lo è mai.

La direzione dell'errore che ne discende è però conoscibile, ed è la ragione per cui la stima resta utile. Quando le due fonti sono correlate positivamente, cioè quando ciò che una vede l'altra tende a vederlo, la sovrapposizione osservata è maggiore di quella che l'indipendenza produrrebbe, e la stima della popolazione risulta perciò minore del vero. Ne segue che il numero di voci mai viste che il metodo restituisce è un limite inferiore e non una previsione: se dice che ne mancano cinquanta, ne mancano almeno cinquanta.

Si stabilisce quindi che ogni documento di enumerazione di questo progetto dichiari in testa, accanto al proprio conto, contro quali fonti sia stato chiuso e con quale residuo, e che la parola completo non compaia senza quella dichiarazione accanto. Si stabilisce inoltre che l'aggiunta di una fonte nuova produca sempre la coppia di numeri della sovrapposizione, perché è quella coppia e non il totale a dire se il lavoro stia convergendo.

## ADR-045: una distribuzione con più allenatori vale un esemplare per allenatore, e il separatore è l'informazione

Data: 2026-09-07. Stato: accettata quanto al criterio, con un limite dichiarato quanto alla sua applicazione meccanica.

L'utente ha deciso il 2026-09-07 che una distribuzione la cui fonte dichiari più nomi di allenatore vale un esemplare per ciascun nome, e non uno solo. La decisione è coerente con il precedente già stabilito per la prima e la seconda generazione, dove le voci con più allenatori dichiarati hanno prodotto una voce ciascuno, ed è coerente con ADR-035, che conta oggetti e non caselle: due esemplari della medesima consegna con nomi di allenatore diversi sono due oggetti distinguibili guardandoli.

Prima di poterla applicare è però stato necessario correggere un difetto di lettura che l'avrebbe falsata in modo grossolano, e che vale registrare perché è la forma più pura di un errore già incontrato più volte in questo lavoro.

L'archivio separa le varianti di un nome con una interruzione di riga. Il nostro lettore, per una funzione di pulizia generale scritta molto prima e usata ovunque, trasformava ogni interruzione di riga in uno spazio prima di consegnare il testo. Il separatore veniva quindi distrutto proprio nel campo in cui portava tutta l'informazione, e il conto che ne discendeva era doppiamente sbagliato: un nome contenente uno spazio, per esempio quello del decennale scritto come due parole, risultava due allenatori; e nulla distingueva quel caso dalle quattro lettere consecutive di un negozio, che allenatori distinti lo sono davvero.

La misura prima e dopo dà l'ordine di grandezza dell'errore. Contando gli spazi, trecentosettantanove distribuzioni sembravano avere più di un allenatore e l'espansione dava tremilasettantasei esemplari; leggendo il separatore vero, quelle con più di una variante sono trecentoquattro e l'espansione ne dà duemilaottocentonovantasette. Non è una differenza marginale, ed è interamente artefatto di lettura.

Se ne trae la regola generale che questa decisione registra, e che vale oltre il caso: quando si estrae un campo da un documento marcato, si stabilisce per primo quale marcatore porti la struttura di quel campo, e lo si preserva prima di applicare qualunque normalizzazione. Una funzione di pulizia scritta per la prosa distrugge la struttura di un campo che non sia prosa, e lo fa senza errore.

Resta un limite che va dichiarato perché la regola non è meccanica e non lo diventerà. Una interruzione di riga separa varianti, ma che cosa una variante sia dipende dalla distribuzione. Quattro lettere consecutive del medesimo negozio sono quattro allenatori distinti; un nome scritto in giapponese e poi in quattro lingue europee è un allenatore solo, tradotto per il pubblico di ciascuna edizione. La regione dichiarata aiuta a distinguerli e non basta, perché esistono distribuzioni di una sola regione i cui due nomi sono manifestamente lo stesso nome in due lingue.

Si stabilisce quindi che l'espansione si applichi caso per caso e non per regola automatica, che ogni documento generato dichiari quale lettura abbia applicato a ciascuna riga, e che il numero complessivo dell'asse degli eventi resti dichiarato come intervallo finché la distinzione non sia stata fatta su tutte le trecentoquattro distribuzioni interessate. L'intervallo corrente è fra millenovecentottanta e duemilaottocentonovantasette esemplari, dove il minimo è la lettura che non espande nulla e il massimo quella che espande tutto.

## ADR-046: gli esemplari che una catena rifiuta si conservano come file e si aspetta una catena diversa

Data: 2026-09-07. Stato: accettata. Chiude in un modo nuovo la questione delle macchine nascoste, che era aperta dal 2026-09-04 sul lotto di terza generazione e si era allargata il 2026-09-07 a quello di quarta.

Il fatto. Il Trasferimento dalla quarta alla quinta generazione rifiuta gli esemplari che conoscano una macchina nascosta, e il Parco Amici dalla terza alla quarta fa lo stesso. Ne restano esclusi cinque esemplari di terza generazione e undici di quarta, cioè dieci Pikachu che conoscono Surf e un Rayquaza che conosce Volo. Per sei Manaphy che conoscono Vortice esiste una via dichiarata dalla fonte, cioè partire da Diamante, Perla o Platino dove quella mossa non è una macchina nascosta, e quei sei sono quindi salvi.

Le due soluzioni finora considerate erano entrambe perdite. Dimenticare la mossa e trasferire significa trasferire un altro esemplare, perché su un Pikachu Surfista la mossa è la ragione per cui quell'esemplare esiste. Non trasferirli significa non averli nel deposito.

La terza via, proposta dall'utente e adottata da questa decisione, è che le due cose non si escludono e che il tempo lavora a favore. Un esemplare rifiutato da una catena si conserva come file, che è una forma di possesso piena per il progetto anche se non lo è per il deposito, e si attende una catena diversa che non abbia quel vincolo. Il progetto ne sta già tracciando una: lo scambio fra hardware di terza generazione e console corrente, che il track dedicato segue dal 2026-08-31 e che il 2026-09-07 ha visto la dimostrazione pubblica di un adattatore funzionante fra una cartuccia vera e l'emulatore ufficiale.

Perché quella catena non ha il vincolo. Il vincolo delle macchine nascoste appartiene al Parco Amici e al Trasferimento, cioè a due passaggi della catena storica, e non è una regola del formato né del deposito. Una catena che porti un esemplare di terza generazione direttamente alle versioni per console corrente, e da lì al deposito attraverso il canale che apre a ottobre 2026, non attraversa né il Parco Amici né il Trasferimento e non incontra quindi quel vincolo. Va detto che questa è una previsione fondata sulla struttura della catena e non un fatto verificato, perché quell'adattatore non è ancora un prodotto e il canale di ottobre non è ancora aperto.

Ne segue la prescrizione, che vale oltre il caso delle macchine nascoste. Quando un esemplare è prodotto e verificato ma una catena lo rifiuta, non lo si degrada e non lo si altera per farlo passare: lo si conserva nella sua forma corretta, si registra quale vincolo lo blocchi e su quale passaggio, e lo si mette in una coda di attesa che venga riesaminata ogni volta che una catena nuova diventa disponibile. Alterare un esemplare per farlo passare è irreversibile; attendere non lo è.

Si stabilisce inoltre che questa coda sia un elenco tracciato e non una nota, perché il suo scopo è essere riletta fra mesi da chi non ricordi perché quelle voci fossero là, e che ogni voce dichiari il vincolo che la blocca e il passaggio su cui esso agisce, cosicché l'apertura di una catena nuova si possa confrontare con la coda invece che con la memoria.

## ADR-047: la forma di terza generazione non è un campo dell'esemplare ma una resa del gioco, e le quattro caselle di Deoxys si riempiono con quattro corpi e tre biglietti

Data: 2026-09-07. Stato: accettata.

Contesto. Studiando gli esemplari sbloccati dai biglietti è emerso che Deoxys ha una forma diversa a seconda del gioco, e la voce di lavoro del medesimo giorno ne ha tratto due conclusioni, una imprecisa e una falsa: che le forme fossero tre, e che il progetto non le contasse. L'utente ha corretto la prima osservando che sono quattro, perché le due versioni di apertura rendono la forma normale; il controllo sui nostri file ha corretto la seconda, perché la lista di spunta porta le quattro voci da quando è stata generata. Resta da fissare la formulazione esatta del fatto, perché da essa dipende quanti esemplari il progetto debba produrre e quali vincoli di origine essi debbano portare.

Il fatto, verificato sul sorgente del verificatore. In terza generazione la forma non è un campo memorizzato. Il lettore del formato la calcola sempre uguale a zero per ogni specie tranne Unown, dove discende dal valore di personalità, e il ramo di scrittura rifiuta di scriverla per ogni altra specie. Un file di terza generazione che contenga un Deoxys non porta dunque alcuna forma, e non esiste alcun campo in cui la si possa scrivere. Ciò che decide l'aspetto è il gioco che apre il file: le due versioni di apertura rendono la forma normale, la riedizione rossa quella d'attacco, la verde quella di difesa e Smeraldo quella di velocità.

Ne discendono due conseguenze che vanno tenute insieme, perché prese una alla volta portano a due conclusioni opposte ed entrambe sbagliate.

La prima è che le tabelle degli incontri registrano tre voci e non quattro, e non è una lacuna: il biglietto dell'aurora uscì per Smeraldo e per le due riedizioni e non per le due versioni di apertura, quindi non esiste alcun incontro che renda la forma normale. Chi ne concludesse che la forma normale è irraggiungibile sbaglierebbe.

La seconda è che dalla quarta generazione in avanti la forma diventa un campo memorizzato, e che questa specie appartiene all'elenco che il verificatore intitola alle specie che cambiano forma qualunque sia la loro origine. Chi ne concludesse che basta un solo esemplare sbaglierebbe altrettanto, perché il deposito conta caselle e una casella la occupa un corpo.

Decisione. Le quattro caselle di Deoxys si riempiono con quattro corpi e tre biglietti. I tre esemplari dell'isola della nascita si producono con i loro tre giochi di origine, che sono un dato dell'incontro e non una scelta; il quarto corpo si ottiene duplicando uno qualsiasi dei tre e portandolo alla forma normale dopo il trasferimento, dove la forma esiste come campo e il cambiamento è lecito qualunque sia l'origine. Non si tenta di produrre un quarto esemplare con un gioco di origine che quel biglietto non ebbe mai.

Si stabilisce inoltre, come regola generale e non come nota su questa specie, che quando una fonte attribuisce a un esemplare una proprietà che il suo formato non memorizza, quella proprietà non è un campo da riprodurre ma una funzione del contesto di lettura, e va registrata come tale nella documentazione. Confondere una resa con un campo produce due difetti opposti e simmetrici: si cerca di scrivere ciò che non si scrive, oppure si conclude che ciò che non si scrive non esiste.

## ADR-048: i lotti restano file completi, e un canale ricostruito vale come oracolo e non come sostituto

Data: 2026-09-08. Stato: accettata.

Contesto. Lo Studio 04 ha stabilito che i servizi in rete di quarta e quinta generazione, chiusi nel 2014, sono stati ricostruiti da terzi e che per quella via un gioco può ricevere doni segreti veri attraverso il proprio canale di consegna. Da quel fatto avevo tratto una conseguenza operativa e l'avevo scritta come regola: se una parte dei doni si può ricevere invece che comporre, quella parte non va composta. L'utente ha risposto che vuole comunque i lotti come file completi e tutti conformi, e ha chiesto se ricevere sia davvero più conveniente che comporre.

La risposta è che non lo è, e la regola che avevo enunciato era sbagliata nel modo peggiore, cioè plausibile. Va corretta con i suoi motivi, perché la stessa tentazione tornerà ogni volta che comparirà un canale nuovo.

Il primo motivo è la copertura. La testimonianza su cui poggia la via elenca una ventina di doni per gioco, non le duecentoquarantasette voci di quarta e le settecento di quinta che abbiamo prodotto. Una via che copre un sottoinsieme non sostituisce una che copre l'insieme.

Il secondo è la selettività, e conta più della copertura. La consegna per quel canale è casuale e produce duplicati: non si chiede una carta, si ricevono carte finché non esce quella che si voleva. Una via che non si può indirizzare non è una via di produzione, è una lotteria con un catalogo.

Il terzo è la dipendenza. Un file su disco non smette di esistere; un servizio non ufficiale sì, e questo progetto nasce esattamente dall'osservazione che un servizio ufficiale con vent'anni di storia sta per chiudere. Fondare la produzione su un secondo servizio, più fragile del primo, contraddice la ragione per cui il progetto esiste.

Il quarto è il più interessante e rovescia del tutto la premessa. Un dono di quinta generazione ricevuto oggi scrive nell'esemplare la data di oggi, e per un evento chiuso nel 2013 quella data è precisamente la firma con cui la comunità riconosce la via del nome di dominio. I nostri settecento esemplari di quinta generazione portano invece centocinquantasette date distinte fra il 2010 e il 2013, cioè quelle storiche dichiarate dalle carte, verificate sui file il 2026-09-07. Sul solo asse che un osservatore esterno guarda per primo, l'esemplare composto da noi è più fedele di quello ricevuto dal canale ricostruito. È il contrario di ciò che l'intuizione suggerisce, e nasce dal fatto che noi possiamo scrivere una data che il gioco, ricevendo oggi, non può.

Decisione. I lotti restano quello che sono, cioè file completi e conformi per ogni voce enumerata, e la loro produzione non si sospende in attesa di alcun canale. La via del canale ricostruito non entra nella produzione.

Le si assegnano invece tre impieghi distinti, in ordine di valore, e sono impieghi che la produzione per file non può avere.

Il primo è l'oracolo, ed è la ragione principale per cui vale percorrerla. Un esemplare ricevuto davvero dal gioco è verità di riferimento: confrontarlo campo per campo con il nostro gemello composto dice se il nostro modello sia giusto, e lo dice in un modo che nessun verificatore può, perché il verificatore controlla la conformità a un modello mentre questo confronto controlla il modello stesso. Basta un solo esemplare per carta per rendere il confronto informativo, e la quinta generazione è la scelta giusta per la prova perché non richiede il punto di accesso aperto.

Il secondo è il ponte per i ventotto coreani. Là non si tratta di produrre ma di trasportare, e il sistema di scambio globale è l'unico passaggio che la barriera di lingua della quarta generazione ammetta: se quello ricostruito attraversa davvero la barriera, sostituisce una stazione coreana in emulazione con un servizio già in piedi.

Il terzo riguarda ciò che non è un esemplare e che i nostri generatori non producono affatto, cioè gli oggetti chiave e le applicazioni che alcune distribuzioni consegnavano, fra cui uno mai distribuito fuori dal Giappone. Non occupano una casella nel deposito e quindi non toccano l'obiettivo, ma appartengono alla storia delle distribuzioni che il progetto documenta.

Si stabilisce infine la regola generale che questa correzione produce, perché è la parte riusabile. Un canale nuovo non si valuta su quanto sia più autentico di quello in uso, ma su quattro proprietà separate: quante voci copra, se si possa indirizzare a una voce scelta, quanto duri, e quale traccia lasci nell'esemplare. Un canale può essere più autentico e insieme peggiore su tutte e quattro, ed è precisamente questo caso.

### Revisione del 2026-09-08, dopo la misura sul codice del servizio

I passi B1 e B2 della roadmap sono stati eseguiti leggendo il codice invece delle testimonianze, e correggono due dei quattro motivi. La decisione non cambia, ma i motivi sì, e vanno riscritti perché una decisione difesa da un motivo falso cade alla prima obiezione.

Il primo fatto corregge una confusione fra due strati che STUDIO-04 aveva segnalato come da verificare e che era reale. Il servizio che fornisce il sistema di scambio globale dichiara nel proprio README, alla voce su ciò che funziona, il sistema di scambio, i video delle lotte, il vestiario, i caricamenti di scatola, le fotografie dei musical, la torre e la metropolitana, le classifiche e la piazza: i doni segreti non ci sono, e compaiono invece nel proprio documento di prospettiva fra le cose che l'autore vorrebbe avere. Non li distribuisce. Li distribuisce l'altro strato, quello dell'emulazione generale della connessione, che è un progetto diverso.

Il secondo fatto falsifica il motivo della selettività, che era il secondo dei quattro. Avevo scritto che la consegna è casuale e che una via che non si può indirizzare non è produzione ma una lotteria: è falso, e veniva dalla testimonianza di un utente invece che dalla documentazione. Il progetto che distribuisce i doni documenta il contrario: ogni gioco ha una cartella con un elenco numerato dei propri doni, e si sceglie quale ricevere impostando l'orologio della console al giorno dell'anno corrispondente al numero di riga. La via è quindi indirizzabile con precisione.

Il terzo fatto sostituisce quel motivo con uno più forte, e nasce dallo stesso meccanismo che lo ha falsificato. Per scegliere un dono si deve impostare una data arbitraria, quindi l'esemplare che ne esce non porta la data di oggi ma la data che si è dovuta impostare per ottenerlo, cioè un giorno di gennaio o febbraio scelto per il suo numero. Il quarto motivo, che era già il più forte, diventa quindi ancora più netto: non si tratta di una data recente ma di una data priva di senso.

Il quarto fatto è la misura della copertura, che era il primo motivo ed esce confermato oltre le attese. Per le cartucce italiane che il progetto possiede, il catalogo dichiara trentaquattro carte per Diamante, diciotto per Platino e sedici per Argento SoulSilver; le cartelle di Perla, Oro HeartGold e dei quattro titoli di quinta generazione in italiano non esistono affatto, e quella di Bianco esiste ma contiene trecentosettantasette voci fra musical e sfondi e nessuna carta. Ne segue che per la quinta generazione italiana il canale non distribuisce alcun Pokemon, e per la quarta ne distribuisce al più sessantotto contro le duecentoquarantasette che abbiamo prodotto.

I motivi validi restano quindi tre: la copertura, ora misurata e non stimata; la dipendenza da un servizio non ufficiale; e la traccia, che è peggiore di quanto avessi scritto. Il motivo della selettività si ritira.

Gli impieghi assegnati alla via non cambiano, e il primo si rafforza: proprio perché il dono è indirizzabile, l'oracolo diventa praticabile in modo mirato invece che per tentativi, cioè si può chiedere al canale esattamente la carta il cui gemello composto si vuole verificare.

## ADR-049: si produce un esemplare quando la sua sola via non esiste più, e il criterio non è la classe di incontro

Data: 2026-09-08. Stato: accettata dall'utente il medesimo giorno, con due aggiunte registrate in coda.

Contesto, e l'osservazione che la apre. Il generatore degli incontri sbloccati da un oggetto produce, dal punto di vista del codice, esemplari da incontro statico. L'utente ha osservato che nulla nella macchina distingue un incontro statico sbloccato da un evento da uno ordinario del gioco, e che se il criterio diventasse la classe di incontro allora il progetto dovrebbe produrre anche i vaganti e i leggendari di tutte le generazioni. L'osservazione è corretta e il confine va enunciato, perché finora era implicito nella tavola scritta a mano e non in una regola.

La misura che rende concreta la questione. Le tabelle degli incontri del verificatore portano, per le sole generazioni dalla prima alla quinta, milleduecentoquattro voci fra statici, doni e vaganti: sessantuno in prima, sessantanove in seconda, quattrocentosessantuno in terza, centocinquantacinque in quarta e quattrocentocinquantotto in quinta. Adottare la classe di incontro come criterio significherebbe quindi aggiungere circa milleduecento esemplari al perimetro per le sole prime cinque generazioni, senza contare le quattro successive.

### Il criterio sbagliato, e perché è attraente

Il criterio della classe di incontro ha un pregio evidente: è meccanico. Si legge dalla tabella, non richiede giudizio, e produce un perimetro definito senza discussione. È esattamente per questo che va rifiutato: definisce un perimetro sulla proprietà che il progetto sa misurare invece che su quella che al progetto interessa, il che è la forma più comune di scelta sbagliata in un lavoro di enumerazione.

### Il criterio proposto

Si produce un esemplare quando la sua sola via di provenienza non esiste più. Non si produce quando esiste ancora una via che il progetto possa percorrere.

Il criterio è una proprietà della via e non dell'esemplare, ed è verificabile: per ciascuna classe si può dire se il canale che la produceva sia aperto o chiuso, e la risposta non dipende da un giudizio di gusto.

Ne discende la classificazione seguente, che copre tutto ciò che il progetto ha incontrato finora.

Gli esemplari consegnati da un evento si producono, perché il canale che li consegnava è chiuso da anni e i loro esemplari esistono soltanto in mani private. Sono le duemilaseicentottantasei voci sotto scadenza.

Gli esemplari sbloccati da un oggetto distribuito si producono, per la medesima ragione applicata un passo più indietro: senza quell'oggetto il luogo non si apre, e l'oggetto non si distribuisce più. Sono diciotto voci, quattordici in terza generazione, tre in quarta e una in quinta.

Gli esemplari che venivano da un servizio o da un'applicazione dismessa si producono, e questa è la parte che il criterio aggiunge rispetto a ciò che il progetto faceva. L'esempio misurato è il sondatore dei sogni, un'applicazione a pagamento del negozio in rete della console portatile, chiuso: le sue centottantuno voci non sono ottenibili in alcun altro modo, e fra esse stanno i tre spiriti e i leggendari di quarta generazione al livello cinque, che nessuna altra via produce a quel livello.

Gli incontri ordinari dei giochi non si producono. Comprendono i leggendari, i vaganti e ogni statico che il gioco offre a chi lo giochi, e la ragione del rifiuto è doppia e va detta per intero.

### Perché gli incontri ordinari restano fuori

La prima ragione è che non hanno scadenza, ed è un fatto misurato e non una impressione: lo Studio 01 ha stabilito che zero specie e zero voci-forma dipendono dalla via indiretta, perché l'unione dei titoli a via diretta le copre tutte. Un leggendario che si cattura giocando un gioco posseduto sarà catturabile anche dopo il ventisei febbraio 2027, quindi produrlo oggi non compra tempo: consuma tempo.

La seconda ragione è di qualità e pesa più della prima. Un esemplare catturato dal giocatore con il proprio allenatore è migliore di uno composto su ogni asse che a questo progetto interessi, e produrlo significherebbe sostituire una cosa ottenibile bene con una ottenibile male. È il rovescio esatto dell'argomento che ha giustificato i lotti: là si compone perché non c'è altra via, qui ci sarebbe.

Una terza ragione, minore ma non trascurabile, è che quel perimetro non ha chiusura. Milleduecento voci per cinque generazioni sono una parte, non un totale, e un progetto che perda la proprietà di poter finire perde con essa la possibilità di misurare quanto gli manchi.

### Che cosa la decisione cambia in concreto

Se accolta, apre un lavoro nuovo e ne chiude uno mai aperto. Il lavoro nuovo sono le centottantuno voci del sondatore dei sogni, che vanno prima misurate contro le nostre enumerazioni per sapere quante caselle aggiungano davvero, e che vanno prodotte con il ramo senza correlazione della quinta generazione. Il lavoro che si chiude è la produzione dei leggendari e dei vaganti, che non si apre.

Va infine registrato che il criterio si applica anche all'indietro e potrebbe cambiare qualcosa: ogni classe già prodotta va riletta chiedendosi se la sua via sia davvero chiusa, e ogni classe scartata va riletta chiedendosi se la sua via lo sia diventata. È un controllo da rifare quando un servizio chiude o riapre, non una volta sola.

### Il caso che il criterio non decide, e va dichiarato

Restano fuori dalla classificazione i Pokemon di N, che si ottengono collegando un salvataggio di quinta generazione a uno dell'altra coppia con la funzione dei ricordi. Il canale non è chiuso, perché non è un servizio in rete ma una funzione fra due giochi, e il progetto possiede i salvataggi; ma richiede due cartucce e una procedura che il progetto non ha ancora provato. Non si producono, e la voce resta come lavoro di gioco e non di generazione.

### Le due aggiunte dell'utente, del 2026-09-08

La prima è l'accoglimento con una estensione. Il sondatore dei sogni entra nel perimetro, quindi le sue centottantuno voci vanno misurate e prodotte. Gli incontri ordinari restano fuori, come proposto.

La seconda è una politica di produzione che vale per il futuro e che va enunciata con precisione, perché applicata al caso sbagliato farebbe danno. L'utente chiede che un leggendario prodotto sia generato come se fosse stato incontrato legittimamente nella cartuccia della propria versione, e porta l'esempio di Groudon che viene da Rubino anche se potrebbe venire da altre. La richiesta è giusta e va distinta in due casi che si comportano in modo opposto.

Per un esemplare da distribuzione la versione non è una nostra scelta e non va toccata. La carta veniva consegnata a un gruppo di titoli, e l'esemplare porta il titolo di chi la riscattò: un Groudon distribuito ai tre titoli di quarta generazione e riscattato in Diamante è autentico, e riscriverlo come Rubino sarebbe falso due volte, perché Rubino non apparteneva a quel gruppo e perché quella distribuzione non esisteva là. La nostra scelta, dove il gruppo ne ammette più d'uno, è già registrata e resta: il lotto di quarta generazione porta centoquarantadue voci da Diamante e centocinque dalle riedizioni di seconda, che è il primo membro di ciascun gruppo.

Per un esemplare da incontro statico la versione è invece una nostra scelta ogni volta che la tabella ne ammette più d'una, e là la politica si applica: si sceglie la versione in cui quella specie è nativa o esclusiva. È il caso di Groudon, che si prende da Rubino e non da Smeraldo, e di Kyogre, che si prende da Zaffiro. Dove la tabella ammette una sola versione la politica non ha nulla da decidere, ed è il caso di tutti e tre gli esemplari di quarta generazione già prodotti, che esistono soltanto in Platino.

Ne segue una prescrizione per i generatori di incontri: dove la tavola porta più versioni per la medesima specie, la colonna della versione non si compila con la prima disponibile ma con quella nativa, e la scelta si dichiara nella tavola accanto alla voce. Il generatore di terza generazione lo fa già senza che fosse una regola, perché il Biglietto Eone consegna Latias in Rubino e Latios in Zaffiro, cioè in ciascun caso il leggendario che quella versione non fa vagare.

## ADR-050: una via aperta ma impercorribile entro la scadenza si tratta come chiusa, e si produce tutto

Data: 2026-09-09. Stato: accettata, su direttiva esplicita dell'utente nella medesima giornata.

Contesto. ADR-049 aveva fissato il criterio di produzione sulla proprietà della via: si produce quando la sola via di provenienza non esiste più. Le due classi enumerate il 2026-09-09, cioè gli scambi in gioco e gli incontri che una condizione sblocca, hanno mostrato il limite di quel criterio applicato alla lettera: le loro vie esistono, perché le cartucce sono possedute, ma alcune non sono percorribili nei centosettanta giorni che restano. L'Isola Miraggio compare in un giorno su decine di migliaia secondo il valore di personalità di un esemplare posseduto; le caselle del Feebas sono sei su quattrocentonovanta e si spostano a ogni cambio di quelle; la zona safari delle riedizioni di seconda generazione richiede giorni di attesa per ogni blocco disposto; e la stessa aritmetica vale per le duemilaseicentottantasei voci da distribuzione, che a sei esemplari per sessione occupano circa quattrocentoquarantotto sessioni.

La decisione. L'utente ha dichiarato che si produce tutto, e la ragione dichiarata è il tempo. Ne segue la regola: una via che esista ma non sia percorribile entro il 26 febbraio 2027 si tratta, ai fini della produzione, come una via chiusa. Il criterio di ADR-049 resta valido nella sua forma, e questa decisione ne cambia il predicato: da esiste una via a esiste una via percorribile nel tempo residuo.

Ciò che la decisione comporta, detto in numeri e non in principio, perché' il perimetro cresce di un ordine di grandezza. Le voci da distribuzione sotto scadenza sono duemilaseicentottantasei sull'asse degli eventi, dentro un totale enumerato di seimiladuecentoquarantaquattro. Gli scambi in gioco sono duecentotrentotto voci di tabella e duecentotrentatre distinte, di cui centosessantaquattro nelle generazioni la cui via passa dalla banca. Gli incontri condizionati portano centotrentasette specie da un tipo di casella condizionato e quarantanove da un'area monospecie esclusiva. Gli incontri fissi, i doni e i vaganti delle sole prime cinque generazioni sono milleduecentoquattro voci, che ADR-049 aveva escluso e che questa decisione riapre per la parte non percorribile. E restano gli assi delle mosse perdute, dei fiocchi e delle sfide, che non sono esemplari ma condizioni su di essi.

Le conseguenze operative, che sono tre e vanno enunciate perché' cambiano il lavoro e non solo il conto. La prima è che la coda di produzione non si ordina più' per classe ma per costo unitario e per rischio di irreversibilità, perché' con questo perimetro il collo di bottiglia diventa il tempo di macchina e di catena e non la conoscenza. La seconda è che il generatore va esteso alle classi che oggi non copre, cioè' gli scambi in gioco, gli incontri condizionati e gli statici ordinari, e per le prime la fonte scrive il valore di personalità' su quarantasei voci, che sono quindi riproducibili byte per byte senza alcuna ricerca. La terza è che la produzione su hardware reale diventa una via da valutare seriamente e non un'ipotesi, perché' l'esecuzione di codice arbitrario di prima, seconda e terza generazione consegna esemplari ottenuti dentro il gioco invece che scritti in un salvataggio, ed è precisamente la distinzione fra creare e ottenere su cui poggia la trasferibilità secondo la testimonianza registrata in `poke-ace/STUDIO-03`.

Ciò che questa decisione non decide, e va tenuto distinto. Non decide che si produca ciò che è comodamente ottenibile giocando: l'argomento di ADR-049 sulla qualità' superiore di un esemplare catturato dal giocatore resta valido dove il tempo lo consente, e la sua applicazione caso per caso è una scelta di priorità' e non di perimetro. Non decide la questione della legittimità, che resta quella di ADR-023 e degli studi del track sull'esecuzione di codice: legale e legittimo non sono sinonimi, e il progetto persegue il secondo. E non autorizza alcuna operazione su hardware fisico, che resta soggetta alla regola del perimetro e ai suoi presidi.
