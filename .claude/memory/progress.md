# Work log

Registro append-only in ordine cronologico inverso: la voce piu' recente sta in cima. La fonte di verita' su cosa e' fatto e' questo file insieme a `index.md`, non le spunte del diario privato.

Le voci datate prima del 2026-08-24 sono antecedenti all'adozione del sistema e alla nascita del repository git: sono ricostruite dalle date dichiarate negli handoff, non da commit, e sono marcate come tali.

## 2026-08-25 Formato dati verificato sul sorgente, registro delle fonti, percorso di studio

Chiusa la fase di conoscenza del track del ponte fra generazioni. Scritta la referenza `DATA-FORMATS_Gen1-Gen2-Gen3.md`, che documenta byte per byte le strutture, i salvataggi, le codifiche di testo, gli indici di specie, il problema della conversione e il protocollo del cavo per tutte e tre le generazioni.

Metodo che ha fatto la differenza: invece di fidarsi delle fonti secondarie, sei repository sono stati clonati in superficie e cercati nel codice, cioe' i tre disassemblati pret coinvolti, il PCCS, Poke Transporter GB e Pokemon-Gen3-to-Gen-X. Ne sono uscite quattro correzioni su affermazioni che sarebbero finite in codice. Le tabelle caratteri erano sbagliate in entrambe le generazioni, cifre a 0xF0 invece di 0xF6 e maiuscole a 0xC1 invece di 0xBB. Il checksum di Gen 3 e' una somma di parole da 16 bit e non di byte, e sbagliarlo trasforma un Pokemon in Uovo Difettoso. Il blocco di scambio Gen 1 misura 424 byte sul filo e 418 di dati, il che spiega il conflitto fra le due cifre in circolazione. Il PCCS documenta quattro metodi di conversione nel README e nel codice ne implementa uno, quindi la conversione fedele delle statistiche non esiste in nessuna implementazione pubblica.

Chiusi undici punti che erano aperti o dubbi, fra cui l'ordine dei nibble dei DV, il ruolo dell'ID segreto come variabile libera per la lucentezza, che era una deduzione e ora e' verificato nel codice del PCCS, e il modo in cui Poke Transporter GB ottiene l'esecuzione di codice, che avviene mandando un payload Z80 sul cavo al posto della squadra e non richiede alcun setup lato giocatore. Scoperto che pokecrystal contiene una `red_party_struct` per il Time Capsule, cioe' la conversione fra formati esiste gia' dentro il gioco. Precisato che l'impossibilita' di emulare riguarda il ponte fra Game Boy e Game Boy Advance e non il collegamento fra due Game Boy, che si collauda su BGB via TCP.

Scritto `SOURCES.md` alla radice, registro delle fonti a cinque livelli di affidabilita' con la colonna del sottoprogetto servito da ciascuna voce, esteso a tutti e quattro i track su richiesta esplicita. Limiti dichiarati: Reddit non e' raggiungibile dagli strumenti di sessione e YouTube restituisce una pagina di consenso, quindi quelle voci indicano dove cercare e non sono state lette.

Scritti i primi due strumenti. `extract_charmaps.py` genera le tabelle caratteri dai charmap dei disassemblati e si rifiuta di scrivere se otto sentinelle non tornano, cosi' che l'errore di trascrizione non possa ripetersi: alla corsa corrente sono 147 corrispondenze fra le due codifiche e 53 caratteri senza destinazione. `emerald_bag_decode.py` legge un salvataggio Gen 3, valida le sezioni, sceglie lo slot piu' recente e smaschera lo zaino, e il suo collaudo su un salvataggio sintetico con cinque anomalie deliberate ha trovato un difetto vero, cioe' che uno slot vuoto in una tasca mascherata non ha quantita' zero ma contiene la chiave. Da quel difetto e' nata una verifica incrociata gratuita sulla chiave.

Creato il percorso di studio sotto `docs/`, sedici note collegate fra loro con wikilink e leggibili come vault Obsidian, su tre livelli piu' una coda sul codice. Ritirato l'handoff del ponte, la cui conoscenza e' interamente assorbita fra la referenza e le note, per ADR-013.

Ritirati tre file superati oltre all'handoff del ponte, dopo averli esaminati uno per uno: gli appunti grezzi e la pagina HTML del flusso nel track 3DS, e la versione precedente dell'handoff Smeraldo. Confermati invece i quattro handoff dei track su hardware fisico e i due file di passo del 3DS, perche' sono procedura e non ricerca. Aggiunto un `README.md` a ciascuno dei tre sottoprogetti che non ne aveva uno, con la tabella di instradamento verso la conoscenza pertinente, e una tabella per scopo in `docs/index.md`: la conoscenza c'era ma non era navigabile partendo da un sottoprogetto.

Registrata come da verificare una discrepanza notata di passaggio: la sezione 7 dell'handoff 3DS colloca l'arrivo di Rosso Fuoco e Verde Foglia su Switch a ottobre 2026, mentre le fonti trovate indicano il 27 febbraio 2026. Tocca il presupposto del track LDN e non e' stata risolta su fonte primaria.

Seconda passata di bonifica, che ha trovato cio' che la prima aveva mancato: due riferimenti testuali sopravvissuti, una cartella tracciata con il collegamento su come scaricare Bank e Transporter, tre file che puntavano a comunita' di condivisione di ROM in contraddizione con la regola di perimetro, due prompt iniziali della stessa natura del `PROMPT MASTER.txt` gia' cancellato dall'utente, e sei occorrenze del nome e cognome in chiaro dentro due trascrizioni incollate come testo. La lezione, registrata in ADR-014: uno scrub si verifica cercando i termini identificanti e non le frasi ricordate, e si verifica anche sui nomi di file e cartelle.

Bonificati sei file tracciati dalla circostanza personale su Bank e Transporter, che non ha ragione di stare in un repository pubblico: il limite operativo resta dichiarato, la motivazione e' passata in `_notes/`, che il `.gitignore` esclude. Registrato ADR-014, con il caveat che il testo resta nella storia git gia' pubblicata e che rimuoverlo davvero richiede una riscrittura della storia.

## 2026-08-25 Primo codice: il lato Game Boy, con la prova di simmetria

Scritto il pacchetto `pokebridge` nel sottoprogetto del ponte, senza dipendenze esterne. Copre gli strati dei dati generati, dei modelli e dei lettori e scrittori per il solo lato Game Boy: primitivi in `gb.py`, generazione 1 in `gen1.py`, generazione 2 in `gen2.py`, transcodifica del testo in `charmap.py` sulle tabelle prodotte dal generatore. Scelto Python con sola libreria standard, per coerenza con gli strumenti gia' nel repository e perche' `docs/20-architettura-codice.md` prevede che i casi di prova siano dati e non codice, cosi' una riscrittura in C per devkitARM resta economica.

Sessantatre prove passano, lanciabili con `python tests/run_tests.py`. La portante e' la simmetria: leggere una struttura e riscriverla deve restituire byte identici, verificata su cinquecento buffer casuali con seme fissato per ciascuna delle sei forme, cioe' box mon, party mon e lista di squadra per entrambe le generazioni. Accanto ci sono prove esaustive dove lo spazio lo permette: tutti i duecentocinquantasei byte di PP, tutte le sessantacinquemila combinazioni dei due byte di cattura, e il conteggio dei DV lucenti che torna a otto su sessantacinquemila, cioe' la probabilita' documentata di uno su ottomilacentonovantadue.

Scrivere il codice ha prodotto due correzioni. La prima e' nella referenza: la lista della squadra di generazione 1 misura 404 byte e non 194, perche' la fonte secondaria aveva letto la dimensione esadecimale 0x194 come decimale, e il conto dei campi lo dimostra. Ora c'e' un'asserzione che lo verifica in entrambe le basi. La seconda e' in una mia prova, che dichiarava a mano il byte 0xA4 credendolo la lettera a, che invece e' 0xA0: la prova ora ricava i byte dalla tabella generata invece di scriverli, che e' la stessa lezione del generatore applicata ai test.

Prossimo passo dichiarato: il lettore e scrittore di generazione 3, dove l'ordine di costruzione e' vincolato perche' il valore di personalita' e' anche chiave di cifratura e selettore della permutazione, e dove un checksum sbagliato non produce un Pokemon strano ma un Uovo Difettoso.

## 2026-08-25 Inventario delle verifiche e chiarimento su dove girera' il codice

Due domande hanno prodotto altrettanta documentazione, ed entrambe erano il tipo di domanda che scopre una imprecisione invece di un errore.

La prima riguardava un'affermazione sbrigativa fatta scegliendo Python, cioe' che sarebbe un prototipo in attesa di riscrittura in C con devkitARM. E' vero solo per l'opzione C di ADR-008: nelle opzioni B e D il Python e' il linguaggio definitivo della logica, perche' nell'opzione D il microcontrollore fa solo il protocollo seriale e tutto il resto resta sul PC, che e' la forma di `PkSploit` e di `PokemonGB_Online_Trades`. La correzione e' in `docs/20-architettura-codice.md`, con la tabella delle quattro forme e l'osservazione che l'opzione D renderebbe superfluo anche il lettore di cartucce. Nella stessa sezione e' registrato il debito tecnico che ne discende: le prove sono metodi Python e non vettori su file, quindi oggi non sarebbero riusabili da un'implementazione in C, e conviene trasformarle in dati prima che la suite cresca.

La seconda chiedeva conto delle prove eseguite e degli strumenti usati. Ne e' nata `docs/23-prove-eseguite.md`, che distingue i due soli tipi di verifica fatti, cioe' lettura del sorgente e prove di programma su dati costruiti a tavolino, e chiarisce che nulla e' stato simulato nel senso dell'emulazione: nessun emulatore lanciato, nessun gioco eseguito, nessun salvataggio reale letto, nessuna console toccata. La nota porta la tabella che associa ciascuna affermazione della referenza al file di sorgente che ha risposto, la ripartizione delle sessantatre prove con i tre livelli di copertura, e l'elenco di cio' che non e' stato verificato affatto.

Il contributo piu' utile di quella nota e' un limite che nessun rapporto entusiasta scrive: la prova di simmetria e' invariante rispetto a una permutazione di etichette, quindi due campi della stessa larghezza scambiati fra loro la supererebbero. La difesa che chiude il cerchio e' il confronto con un dato reale, e il controllo piu' economico e' aprire un salvataggio con `PKHeX` e confrontare campo per campo. Registrato nella scheda del track come limite noto.

Aggiunta a `SOURCES.md` la sezione che distingue le fonti effettivamente consultate da quelle catalogate, perche' l'ampiezza di un registro non e' la profondita' di una verifica: sei repository clonati e cercati nel codice, sedici pagine enciclopediche lette, quattro articoli, zero thread di forum, zero video, zero strumenti eseguiti e zero hardware.

## 2026-08-25 Storia git collassata in un commit radice unico

Eseguita la riscrittura decisa in ADR-014. La storia precedente, sette commit da `d1e1a3a` a `9296c2c`, e' stata collassata in un unico commit radice, `d08a011`, generato dall'albero gia' bonificato. Il metodo e' stato scelto per verificabilita': con un commit solo, la prova che nulla di sensibile sia rimasto e' una ricerca su `HEAD`, mentre una sostituzione di testo commit per commit avrebbe richiesto espressioni regolari capaci di funzionare anche sulle versioni precedenti alla normalizzazione Markdown, dove l'a capo dei paragrafi era diverso. Prima della riscrittura e' stato prodotto un bundle di tutta la storia fuori dal repository, come rete di sicurezza.

Conseguenza da conoscere: gli hash citati nelle voci di diario e negli ADR precedenti a questa data non risolvono piu'. Sono stati lasciati come sono, perche' descrivono correttamente cio' che era vero quando sono stati scritti e questo file e' append-only; `memory/index.md` lo dichiara esplicitamente. Sono state invece ri-ancorate a `d08a011` tutte le schede di `context/`, la referenza del formato dati e la tabella di verifica dell'indice, perche' quelli sono puntatori e non narrazione.

Il repository pubblico e' stato mantenuto invece di essere ricreato: dopo il push forzato i vecchi commit non sono raggiungibili da alcun ramo e restano accessibili solo a chi possieda gia' il loro hash completo, fino al passaggio del garbage collector di GitHub. E' una scelta consapevole, registrata qui perche' e' l'unico residuo noto della bonifica.

## 2026-08-24 Il quarto track prende forma: trading LDN

Aggiunto `gba-switch-pokemon-trading/HANDOFF_frlg-ldn-trade.md`, quattrocentoquarantanove righe, che dota di un obiettivo il sottoprogetto fino a ieri dichiarato non iniziato: trading di Pokemon fra un PC Linux e una Nintendo Switch attraverso il protocollo wireless locale LDN, su FireRed e LeafGreen.

La lettura dell'handoff ha fatto emergere una falla nel `.gitignore`, chiusa prima di committare: il blocco del materiale di chiave console-unica copriva solo il 3DS, mentre questo track richiede le `prod.keys` della Switch, che hanno le identiche proprieta' di `movable.sed`. Il blocco e' stato esteso alle chiavi della Switch, alla cartella che le ospita per convenzione e ai file di dati Pokemon esportati, e la copertura e' stata verificata con `git check-ignore`.

Normalizzato il nuovo handoff alla convenzione Markdown, marcando otto a capo intenzionali fra campi di metadati adiacenti prima di applicare lo strumento, cosi' che unisse solo i paragrafi genuinamente spezzati: cinquemilanovantadue parole prima e dopo.

Riscritte da zero la scheda `sub-gba-switch-trading.md` e il README del sottoprogetto, che dichiaravano l'assenza di un obiettivo. Aggiornate le schede trasversali che il nuovo track cambia nella sostanza: `STACK.md` con la Switch, il requisito della scheda Wi-Fi in modalita' monitor e la tensione fra i due sistemi operativi richiesti; `design-and-security.md` e la regola `hardware-and-perimeter.md` con la seconda categoria di chiavi console; `roadmap.md`, `current-work.md` e `index.md` con lo stato reale del track. Registrato ADR-012.

Correzione di merito rispetto a quanto scritto il giorno prima: l'ipotesi che questo sottoprogetto potesse sovrapporsi al track 3DS come via verso Pokemon Home era sbagliata. E' un track autonomo di rete e reverse engineering. Resta una sovrapposizione hardware non documentata sul lettore GBxCart RW, che compare fra i requisiti senza che sia spiegato in quale fase entri.

## 2026-08-24 Pulizia del materiale e consolidamento dei media

Chiuso il version control con tre commit su origin/main: d1e1a3a di adozione, 8097e5c di ancoraggio, cdb09e2 di normalizzazione Markdown. Quest'ultimo ha fatto risultare stale otto schede, perche' i quattro handoff normalizzati ricadono nei loro covers-paths: verificato che il cambiamento fosse puramente di a capo, con zero parole modificate in tutti e quattro i file, e applicato il bump del checkpoint a cdb09e2 come previsto dal passo 5 di sync-context. Corretta una frase di index.md rimasta indietro da una sostituzione fallita in silenzio durante l'ancoraggio.

Eliminato il bytecode Python rigenerabile. Raccolti tutti i media sotto `_notes/media/`, che rispecchia la struttura del progetto: ventisei file per ventotto megabyte, e l'albero di progetto e' ora di solo testo. Eliminati dal disco gli undici screenshot con dati personali, che non erano mai entrati in git. Aggiornati i riferimenti nelle schede vive e nell'handoff Smeraldo, lasciando invariate le voci append-only di questo work log e di ADR-005, che descrivono correttamente cio' che era vero quando sono state scritte. Corretto il blocco dei media nel `.gitignore`, dove la riga di eccezione per il PDF portava il vecchio nome della cartella ed era comunque diventata inapplicabile. Registrato ADR-011.

Conservati per scelta: il bundle completo di `.claude/templates/`, perche' il gate dei pacchetti lo consulta, e il backup pre-bonifica fuori dal repository, perche' e' l'unica seconda copia dei media che per politica non sono versionati.

## 2026-08-24 Ancoraggio al primo commit

Primo commit reale creato e spinto sul remoto: d1e1a3a, 255 file, 14674 inserzioni, 424 kilobyte trasferiti. Il branch main traccia origin/main.

Eseguito il passo di primo ancoraggio della skill sync-context: il segnaposto PENDING-FIRST-COMMIT e' stato sostituito con l'hash di HEAD in trentadue punti, cioe' i campi generated-from-commit e last-verified-commit delle dieci schede di context, piu' il commit di riferimento e le dieci righe della tabella di verifica in memory/index.md. Il segnaposto resta citato in prosa in ADR-001, dove descrive il meccanismo e non e' un valore da sostituire.

Da questo punto il confronto di drift vale normalmente: sync-context confronta i covers-paths di ogni scheda con i commit successivi e segnala quali schede sono diventate stale.

## 2026-08-24 Adozione del sistema di progetto

Verificata l'igiene dell'account: auto-memory disattivata, hook di wipe registrato, nessun residuo di memoria nascosta per questo progetto.

Inventario contro l'anatomia canonica: divario totale, non esisteva nulla, quindi nessuna riconciliazione ma costruzione da zero. Scansione dei dati personali sul working tree, sostitutiva di quella sulla storia perche' la storia non esisteva: trovati dati personali in chiaro in undici dei tredici screenshot della sessione di acquisto, portati in quarantena sotto `_notes/media-riservati/`. Nessuna credenziale leggibile.

Bonifica pre-commit, eseguita nell'unica finestra in cui costava zero: rinominati tre cartelle e due file per togliere i caratteri non-ASCII, rinominata la cartella del sottoprogetto Smeraldo perche' il nome era superato, normalizzate quattro cartelle-data e un file-nota al formato ISO, eliminati due file byte-identici duplicati fra la radice di `3ds-related` e la sua cartella `handoff`, eliminata una nota da zero byte, corretti quattro percorsi stale che puntavano a una vecchia radice e a una sandbox web, creato un README che dichiara il sottoprogetto non iniziato. Backup dell'albero originale fuori dal repository prima di toccare qualsiasi cosa.

Inizializzato il repository su `main` con identita' locale personale, distinta da quella di lavoro che e' il default globale, e remoto sull'alias SSH `github-personal`. Scritto il `.gitignore` prima di creare `_notes/`, con i blocchi di dominio per i dump e per il materiale di chiave console-unica scritti prima che quei file esistano. Verificato con `git check-ignore -v` riga per riga.

Importati lo standard e il motore dal bundle, istanziata l'anatomia canonica, create le sei schede trasversali piu' quattro schede verticali, una per sottoprogetto. Registrate dieci voci ADR.

Risultato: da settantacinque file e ventinove megabyte a trentasette file e centoquarantuno kilobyte di sola conoscenza tecnica tracciata.

## 2026-08-18 Smeraldo, acquisto del lettore

Antecedente al repository, ricostruita dall'handoff. Ordinato il GBxCart RW v1.4 Pro USB-C blu con cavo USB-A verso USB-C. Avviato il setup software su Windows 11, fermo al primo dei sette step, l'installazione dei driver seriali CH340 e CH341.

## 2026-08-17 Smeraldo, studio dell'estrazione del salvataggio

Antecedente al repository, ricostruita dall'handoff. Ricerca sulla catena hardware e software: GBxCart RW, FlashGBX, PKHeX. Il chat log di questa giornata non e' mai stato salvato, il file era vuoto ed e' stato rimosso durante la bonifica.

## 2026-08-16 Smeraldo, analisi Action Replay

Antecedente al repository, ricostruita dall'handoff. Master Code e Anti-DMA verificati su piu' fonti indipendenti. Nessuna fonte affidabile per i codici della tasca Strumenti Base, da cui la decisione di chiudere quel percorso.

## Step 03 in corso, 3DS, dump delle cartucce

Antecedente al repository, senza data precisa negli handoff. Dumpati Omega Ruby, Y e Moon, tutti con seed encryption risolta generando il file di seed con SEEDconv. Restano cinque cartucce Nintendo DS.

## Step 02 completato, 3DS, installazione del custom firmware

Antecedente al repository, senza data precisa negli handoff. Installato boot9strap con Luma3DS v13.4 tramite MSET9, partendo dal firmware 11.17.0-50E. MSET9 rimosso a fine procedura, installazione verificata.
