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

