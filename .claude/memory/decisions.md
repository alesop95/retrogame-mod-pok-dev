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
