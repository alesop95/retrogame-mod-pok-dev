---
tipo: nota di studio
livello: codice
tags: [strumenti, script, riproducibilità]
up: "[[index]]"
vedi_anche: ["[[05-testo-e-charmap]]", "[[04-cifratura-gen3]]", "[[21-collaudo]]", "[[SOURCES]]"]
---

# Gli strumenti del progetto

Questa nota documenta gli strumenti che esistono, che cosa fanno e come si rilanciano. Sono pochi e deliberatamente piccoli: rispondono al principio, registrato nella regola di token economy del progetto, di spingere su codice deterministico tutto ciò che non richiede comprensione semantica, e di conservarne l'esito come stato ispezionabile su disco invece che come risposta in una conversazione.

## Il presupposto comune: i disassemblati in locale

Due dei tre strumenti leggono dai disassemblati, che non stanno nel repository e non devono starci. Si ottengono con cloni superficiali, che bastano perché serve solo lo stato corrente.

```
git clone --depth 1 https://github.com/pret/pokecrystal
git clone --depth 1 https://github.com/pret/pokeemerald
git clone --depth 1 https://github.com/pret/pokered
```

Conviene tenerli fuori dal repository, per esempio in una cartella di lavoro temporanea. Il vantaggio del clone rispetto alla lettura via web è che permette di cercare nel codice invece di leggere riassunti, ed è precisamente così che sono state trovate le quattro correzioni registrate in [[SOURCES]].

## Dove vivono gli strumenti esterni, e perché non nel repository

Questo documento descrive due famiglie di strumenti che vanno tenute distinte, perché la loro collocazione segue regole opposte. Gli strumenti di questo progetto sono programmi brevi sulla sola libreria standard, vivono in `tools/`, sono versionati e si leggono come si legge il resto del repository. Gli strumenti esterni sono binari di terzi da decine di megabyte, e non entrano nel repository in alcuna forma.

I tre posti candidati sono tre e due sono sbagliati, e vale enunciare perché, perché la ragione del secondo errore non è evidente ed è stata scoperta ragionandoci sopra il 2026-09-01.

Dentro `tools/` è sbagliato perché quella cartella è tracciata. Un binario di terzi vi finirebbe in un commit, e il caso peggiore non è la dimensione: alcuni di quegli strumenti scrivono accanto a sé, e ciò che il verificatore di conformità scrive sono copie di riserva di salvataggi, cioè esattamente la categoria che ADR-005 esclude dal version control senza eccezioni. In una cartella tracciata quelle copie starebbero a un `git add -A` di distanza dall'essere pubblicate.

Dentro `_notes/` è sbagliato per una ragione diversa e meno visibile. Quella cartella è esclusa in blocco, quindi il rischio del commit non c'è; l'esclusione però protegge dal commit e non dalla cancellazione, e la pulizia profonda di git, che è un gesto di manutenzione ordinaria, elimina proprio i file ignorati. Uno strumento collocato là viene distrutto da un comando che si dà per rimettere in ordine un albero di lavoro, e con esso spariscono le copie di riserva che ha scritto accanto a sé. Sono le sole copie che non si possono riscaricare.

Il posto giusto è fuori dal repository, in una cartella condivisa fra i progetti che ne hanno bisogno, per esempio `E:\tools\pkhex` e `E:\tools\dce`. Ne discendono tre proprietà che nessuna delle altre due collocazioni ha: lo strumento non interagisce con git in alcun modo, sopravvive a qualunque operazione sul repository, ed è condiviso con gli altri progetti che nasceranno dal template invece di essere scaricato una volta per ciascuno. Il prezzo è che il percorso è specifico della macchina e va comunicato allo strumento che lo invoca, e i nostri lo prevedono già: si passa con l'opzione dedicata oppure si mette in una variabile d'ambiente.

## extract_charmaps.py

Sta in `pokemon-gen12-gen3-bridge-original-hardware/tools/` e genera le tabelle di codifica dei caratteri leggendo i charmap dei disassemblati.

```
python tools/extract_charmaps.py --pokecrystal PATH --pokeemerald PATH --out data
```

Produce tre file in `data/`. Il primo è la tabella di generazione 1 e 2, il secondo quella di generazione 3, ciascuna con i caratteri stampabili separati dai token di controllo e con l'indicazione del commit da cui provengono. Il terzo è la traduzione diretta fra i due spazi di codifica, che è il file che un convertitore usa davvero, e che elenca a parte i caratteri privi di destinazione.

Alla corsa corrente le cifre sono duecento caratteri stampabili per generazione 1 e 2, duecentoquarantotto per generazione 3, centoquarantasette corrispondenze e cinquantatre caratteri senza destinazione.

La proprietà importante di questo strumento non è cosa produce ma cosa si rifiuta di produrre. Prima di scrivere verifica un insieme di sentinelle, cioè i byte del terminatore, dello spazio, di A, Z, a, z, 0 e 9 in entrambe le tabelle, e se anche una sola non corrisponde non scrive nulla e riferisce lo scostamento. Se un giorno il formato dei charmap a monte cambia, il fallimento è rumoroso invece che silenzioso, che è esattamente il contrario di come si comportava la trascrizione a mano descritta in [[05-testo-e-charmap]].

## emerald_bag_decode.py

Sta in `gba-save-extraction-smeraldo/tools/` e legge un salvataggio di generazione 3 per diagnosticare lo zaino.

```
python tools/emerald_bag_decode.py PERCORSO.sav
python tools/emerald_bag_decode.py PERCORSO.sav --game frlg --json rapporto.json
```

Non scrive nulla sul salvataggio: legge, valida e riferisce. La sequenza è quella descritta in [[03-integrita-checksum]] e [[04-cifratura-gen3]], cioè individua i due slot, valida la firma e il checksum di ciascuna sezione, sceglie lo slot più recente secondo la regola del contatore, ricompone il blocco di salvataggio dalle sezioni, identifica il gioco, legge la chiave di cifratura al suo offset e smaschera le quantità dello zaino lasciando in chiaro quelle del deposito PC.

L'identificazione del gioco non si fida di un parametro: lo verifica. Il motivo viene da un caso reale documentato su Project Pokemon, dove un editor aveva identificato un salvataggio di Smeraldo come Rubino o Zaffiro e gli oggetti sono finiti negli slot sbagliati, il che è esattamente ciò che accade se si applica la maschera sbagliata, dato che Smeraldo maschera le quantità e Rubino e Zaffiro no. Lo strumento assegna un punteggio a ciascun candidato sulla base di prove indipendenti, cioè la plausibilità del conteggio della squadra al suo offset, il denaro smascherato entro il tetto, e la chiave dedotta da uno slot vuoto, e stampa le prove di tutti e tre invece di dichiarare solo il vincitore. Se due candidati pareggiano si ferma e chiede di indicare il gioco a mano, perché un'identificazione ambigua è un'informazione e non un dettaglio da risolvere tirando a sorte.

Riferisce poi le anomalie che sa riconoscere: un identificatore di oggetto fuori intervallo, una quantità nulla su uno slot occupato, una quantità oltre il tetto della tasca, uno slot popolato dopo un buco, e un identificatore duplicato nella stessa tasca. Sono cinque classi di anomalia che coprono i sintomi tipici di uno zaino manipolato da codici trucco.

Ha due verifiche incrociate che valgono più del resto. La prima è che il denaro, smascherato con la stessa chiave, deve stare sotto il suo tetto: se non ci sta, la chiave o l'offset sono sbagliati, e lo strumento lo dice invece di produrre numeri senza senso. La seconda è che uno slot vuoto in una tasca mascherata contiene la chiave stessa, quindi la chiave si ricava per una seconda via indipendente e le due si confrontano.

Sul lato Rosso Fuoco e Verde Foglia lo strumento è onesto sui propri limiti: legge la chiave al suo offset e la riferisce, ma non pretende di elencare le tasche, perché i loro offset non sono stati verificati sul disassemblato di quel gioco in questa revisione.

## Il pacchetto pokebridge

Non è uno strumento ma la prima parte del software vero, e sta in `pokemon-gen12-gen3-bridge-original-hardware/pokebridge/`. Copre gli strati dal primo al terzo della stratificazione descritta in [[20-architettura-codice]], cioè i dati generati, i modelli e i lettori e scrittori, per il solo lato Game Boy. Non ha dipendenze esterne.

I primitivi stanno in `gb.py`, e sono il posto dove vive la conoscenza che non appartiene a una generazione sola: interi a 16 e 24 bit big-endian, scomposizione dei nibble dei DV con la derivazione del quinto, byte dei PP diviso sei più due bit, e il pattern di DV che in generazione 2 significa lucentezza. I lettori e scrittori stanno in `gen1.py` e `gen2.py`, uno per generazione perché fra le due c'è un riordino e non un'estensione, e in `gen3.py`, che porta la struttura cifrata con la sua permutazione e il suo checksum: è il modulo più grande dei tre perché il valore di personalità è immutabile per costruzione e ogni copia che lo cambia passa da `with_personality`, come richiede il vincolo di ordine di `20-architettura-codice`. La transcodifica sta in `charmap.py`, che legge le tabelle generate e non contiene alcun valore scritto a mano.

Le prove si lanciano con `python tests/run_tests.py` dalla cartella del sottoprogetto, usano solo `unittest` della libreria standard e oggi sono centoquattordici. Vale la pena sapere che la prima esecuzione ne ha fatta fallire una, e che il difetto era nella prova e non nel codice: avevo scritto a mano il byte 0xA4 credendo fosse la lettera a, che invece è 0xA0. La prova ora ricava i byte dalla tabella invece di dichiararli, ed è la stessa lezione dello strumento qui sopra applicata ai test.

## catalogo-eventi-gen3.py

Genera `recreate-pokemon-distributions-events/EVENTI-GEN3.md`, cioè l'inventario delle 177 distribuzioni di evento di generazione 3, dalla tabella `EncountersWC3.cs` di `PKHeX` e dall'enumerazione `PIDType.cs` dello stesso repository. Il percorso del clone si passa sulla riga di comando, esattamente come `extract_charmaps.py` riceve quello dei disassemblati: quel clone non è una dipendenza di questo repository e non viene scaricato dallo strumento.

La ragione per cui il catalogo si genera invece di essere scritto è la stessa delle tabelle di codifica dei caratteri. Quei dati vivono nel codice di chi verifica e non in un documento, perché, come dichiara il commento della tabella stessa, i dati di quella generazione non sono mai stati conservati in forma binaria uniforme e sono scritti a mano uno per uno; trascriverli qui garantirebbe che le due copie divergano alla prima correzione a monte. Lo strumento ha un `--check` che dice se il catalogo è ancora allineato alla fonte, ed è il controllo da lanciare quando il clone viene aggiornato.

Ciò che lo strumento non fa va dichiarato: non giudica la legittimità di alcun esemplare e non ricostruisce alcun metodo, riporta ciò che la fonte dichiara. Le date degli eventi compaiono soltanto dove la fonte le porta nei commenti di blocco, e dove non le porta restano assenti invece di essere indovinate.

## genera-evento-gen3.py

Compone un esemplare da evento di terza generazione e lo scrive nelle due forme del dato. È il passo che il progetto aveva dichiarato aperto il 2026-08-28 e non aveva mai eseguito, cioè costruire un esemplare con il proprio codice e sottoporlo a un verificatore di conformità indipendente. Non richiede hardware, non tocca alcun account, e non produce nulla destinato a una collezione: produce un caso di prova.

La parte che discende dal seme non è scelta ed è quella su cui il grado di fiducia è alto: valore di personalità, sei valori individuali e sesso dell'allenatore di provenienza vengono dalle formule di `pokebridge.eventi`, verificate su duecentonove esemplari conservati. Tutto il resto è metadato dell'evento e viene da fonti di grado diverso, e qui sta la scelta di progetto che rende utile questo programma: esso stampa un rapporto campo per campo con la provenienza di ciascuno, compresi i due che nel codice d'origine portano la parola segnaposto. La ragione è che l'esperimento consiste nel far dire al verificatore quali campi sono sbagliati, e un campo la cui provenienza non sia dichiarata non insegna nulla quando viene contestato.

```powershell
python tools/genera-evento-gen3.py --self-test
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --elenco
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --evento 10ANNI --specie Pikachu --seme 0x9DF6 --lingua ITA --gioco rossofuoco --out _notes/prova
python tools/genera-evento-gen3.py --derivazione --seme 0x9DF6 --soglia-sesso 127 --ace _notes/fonti/ace-builder --evento 10ANNI
```

```bash
python tools/genera-evento-gen3.py --self-test
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --elenco
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --evento 10ANNI --specie Pikachu --seme 0x9DF6 --lingua ITA --gioco rossofuoco --out _notes/prova
python tools/genera-evento-gen3.py --derivazione --seme 0x9DF6 --soglia-sesso 127 --ace _notes/fonti/ace-builder --evento 10ANNI
```

I due file prodotti hanno estensione `.pk3` e `.ek3`. Il primo è la forma decifrata a ordine fisso, che è quella che gli strumenti della comunità accettano in ingresso; il secondo è la forma che il salvataggio contiene, cioè permutata secondo il valore di personalità e cifrata. Contengono gli stessi dati e la conversione fra le due è esatta nei due versi, ed è stata aggiunta a `pokebridge.gen3` come `to_canonical_bytes` e `from_canonical_bytes`, con sei prove nella suite fra cui il controllo negativo che verifica che le due forme differiscano davvero nei quarantotto byte centrali.

Dal 2026-09-01 il programma legge anche la tabella del verificatore invece del solo corpus del costruttore, e la differenza è di copertura: diciassette eventi contro centosettantatre voci su centosettantasette. Le quattro che restano fuori impiegano una forma del costruttore che il lettore non copre, e appartengono all'insieme giapponese, dove serve comunque una codifica dei caratteri che il progetto non ha ancora estratto.

```powershell
python tools/genera-evento-gen3.py --elenco --pkhex _notes/fonti/pkhex
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --indice 59 --seme 0x9DF6 --out _notes/prova
```

```bash
python tools/genera-evento-gen3.py --elenco --pkhex _notes/fonti/pkhex
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --indice 59 --seme 0x9DF6 --out _notes/prova
```

Dal medesimo giorno esiste il modo a lotto, che produce in una corsa tutti gli esemplari producibili e dichiara con la ragione quelli che non lo sono. Il seme non si passa più: si cerca fra i sessantacinquemilacinquecentotrentasei ammessi verificando i vincoli che la tabella dichiara, cioè la lucentezza e, dove la derivazione è implementata, il sesso dell'allenatore; e la ricerca riparte da dove si era fermata, cosicché due esemplari del medesimo evento non ricevano il medesimo valore di personalità.

```powershell
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --lotto _notes/lotto-eventi
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --lotto _notes/lotto-eventi --solo-ot 10ANNI
```

```bash
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --lotto _notes/lotto-eventi
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --lotto _notes/lotto-eventi --solo-ot 10ANNI
```

Dal 2026-09-02 il seme di partenza della ricerca dipende dall'indice della voce e non da quanto è accaduto alle voci precedenti, e la ragione è pratica prima che estetica. Con il cursore a scorrimento che il programma usava prima, una correzione su una voce spostava il seme di tutte quelle che venivano dopo di essa, quindi ogni esemplare già sottoposto a giudizio andava sottoposto di nuovo: il lavoro di verifica fatto a mano si perdeva a ogni correzione. Con la partenza legata all'indice una correzione cambia i soli esemplari che quella correzione riguarda. Lo scopo per cui il cursore esisteva resta soddisfatto, cioè che due voci del medesimo evento non ricevano il medesimo valore di personalità, perché due indici distinti partono da punti distinti, e il controllo che nessuno dei centoventidue esemplari condivida il valore di personalità con un altro è stato eseguito.

Sulla tabella intera l'esito al 2026-09-01, dopo la chiusura dei metodi, è di centoventidue esemplari prodotti e cinquantuno non producibili, e l'inventario delle ragioni con il loro costo sta nella sezione 10 di `recreate-pokemon-distributions-events/STUDIO-04`. Delle cinquantuno che restano, cinquanta sono uova e una impiega un generatore pseudocasuale diverso: nessuna voce è più bloccata dal metodo di generazione né dalla codifica dei caratteri. Il programma non produce nulla per una voce che non sappia fare, e la scelta va difesa perché è la sola sicura: un generatore che produca qualcosa per ogni voce è peggio di uno che si rifiuti, poiché un esemplare sbagliato in mezzo a centosettanta giusti non si trova guardando.

Alcune voci non fissano il nome dell'allenatore, l'identificativo o il sesso, e quella non è una lacuna della tabella ma una istruzione: quegli eventi prendono i tre campi dal salvataggio in cui vengono riscattati. Si passano quindi al programma con `--allenatore`, nella forma `nome:identificativo:segreto:sesso`, e senza di esso quelle voci vengono dichiarate non producibili invece di ricevere un valore inventato. La ragione non è formale: un esemplare con un allenatore inventato porterebbe per sempre il nome di uno sconosciuto dentro la collezione.

```powershell
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --lotto _notes/lotto-eventi --allenatore "MARIO:31121:5432:maschio"
```

```bash
python tools/genera-evento-gen3.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --lotto _notes/lotto-eventi --allenatore "MARIO:31121:5432:maschio"
```

Due dati che il programma legge dalla fonte meritano una nota, perché sono i soli che non discendono da una formula e perché la loro lettura porta un controllo del conteggio. Il primo è l'elenco degli ottantasei semi dell'unico evento distribuito per semi noti, dal quale se ne esclude uno che la fonte dichiara distribuito in una sola delle sue cinque varianti. Il secondo è la tabella dei caratteri giapponese, che il progetto ha estratto lo stesso giorno da `PKHeX.Core/PKM/Strings/StringConverter3.cs` e che vive in `data/charmap-gen3-jp.json`. Su entrambi il controllo del conteggio non è una formalità: una lettura che perdesse una parte dell'elenco non produrrebbe un errore ma un insieme più povero dal quale si continuerebbe a generare esemplari validi, e una tabella letta con uno scostamento di una posizione produrrebbe nomi plausibili e sbagliati. Per questo l'estrazione della tabella verifica anche tre byte di cui si conosce il valore atteso, scelti fra quelli su cui la tabella internazionale dice altro.

L'elenco stampa le voci raggruppate per allenatore e identificativo con l'intervallo di indici di ciascun gruppo, e la composizione di una voce sola si chiede per indice. Serve comunque il sorgente del costruttore, perché da esso vengono tre dati che la tabella non porta, cioè la corrispondenza fra numerazione nazionale e identificativi interni di specie, i gruppi di crescita e i punti potenza delle mosse.

Un esito di questo doppio percorso vale registrare, perché è una verifica che nessuno aveva cercato. Il medesimo esemplare composto dalle due fonti indipendenti risulta identico byte per byte: un errore nella conversione fra le numerazioni, nella correzione registrata o nelle formule avrebbe prodotto una differenza, e non ce n'è. Due strade per lo stesso punto valgono una autorità esterna e costano meno.

Il passo successivo non è del programma: si apre il file `.pk3` con lo strumento di conformità e si legge che cosa esso obietta, confrontando ogni obiezione con la colonna della provenienza. È quella colonna a dire se un difetto sia nostro o dei dati di terzi, e senza di essa l'esito dell'esperimento sarebbe un elenco di errori senza responsabile.

Due difetti di questo programma valgono la menzione perché sono lo stesso difetto in due posti, e nessuno dei due produce un errore. Il costruttore indicizza gli eventi per sigla e le mosse per etichetta leggibile, e cercare per sigla nella tabella delle mosse restituisce zero risultati invece di un errore: l'esemplare esce senza mosse e sembra una lacuna della fonte. Il file delle mosse è la conversione di un foglio di calcolo e la colonna dell'identificativo ha per nome la stringa vuota, quindi cercare una chiave chiamata `id` restituisce un dizionario vuoto e i punti potenza restano a zero. Il principio che ne discende, e che vale oltre questi due casi, è che una ricerca per chiave dentro un dato di terzi va corredata di un controllo sul fatto che abbia trovato qualcosa, perché il silenzio di un dizionario vuoto è indistinguibile da un dato assente.

## PKHeX, il verificatore di conformità: dove si prende e come si usa

È lo strumento con cui si sottopone a giudizio esterno un esemplare prodotto da questo progetto, ed è la seconda metà dell'esperimento che `genera-evento-gen3.py` prepara. Il registro delle fonti lo elenca fra le implementazioni di riferimento; qui sta la procedura, perché una procedura che vive in una conversazione è perduta alla sessione successiva.

Sul dove prenderlo va detto il punto che fa perdere tempo, verificato il 2026-09-01. La pagina dei rilasci sul servizio di repository non contiene alcun binario: i soli due allegati del rilascio sono l'archivio del codice sorgente nelle due forme consuete, e quella pagina serve a leggere il registro delle modifiche e a sapere quale sia la versione corrente. Il binario si scarica dal sito della comunità che lo ospita, cioè `https://projectpokemon.org/home/files/file/1-pkhex/`.

Sul requisito, il file di presentazione del progetto dichiara che si tratta di un'applicazione Windows Forms che richiede la decima versione dell'ambiente di esecuzione. Serve quindi il pacchetto denominato Desktop Runtime nella variante a sessantaquattro bit, e non l'insieme di sviluppo né la variante per applicazioni web: in sua assenza il programma si avvia e termina subito, oppure il sistema propone da sé il download.

Due dettagli di primo avvio non sono deducibili dalla documentazione.

Il primo è che il programma propone di creare una cartella di riserva accanto al proprio eseguibile, dove conserverà una copia dei salvataggi che apre. La risposta corretta per questo progetto è affermativa, e non è una preferenza: la regola sull'hardware pretende un backup prima di ogni scrittura, e uno strumento che lo faccia da sé è un presidio in più e non un ingombro. Proprio perché quella cartella conterrà copie di salvataggi, l'eseguibile va collocato dove la sezione iniziale di questo documento prescrive, cioè fuori dal repository: le copie di riserva sono la ragione più forte di quella regola, perché sono irriproducibili e una pulizia profonda del repository le eliminerebbe insieme a tutto ciò che è ignorato.

Il secondo è che il programma si avvia caricando un salvataggio vuoto di una generazione recente, e questo determina il formato con cui l'editor lavora. Ne segue che per esaminare un esemplare di terza generazione conviene prima portare l'editor in quel contesto, creando un salvataggio vuoto della generazione giusta dal menu dei file, e soltanto dopo trascinare il file dell'esemplare sulla finestra. Trascinandolo mentre è caricato un salvataggio di un'altra generazione, il programma tenta una conversione di formato che non è ciò che si vuole misurare: l'esperimento chiede se l'esemplare sia conforme come esemplare di terza generazione, non se sia convertibile.

Sui menu vale registrare ciò che è stato verificato sulle schermate del 2026-09-01, perché una indicazione sbagliata costa tempo e io ne avevo data una. Il menu dei file non contiene alcuna voce per creare un salvataggio vuoto: ha soltanto l'apertura, il salvataggio di un esemplare, l'esportazione del salvataggio e la chiusura. Le tre voci utili stanno altrove. Sotto gli strumenti, nel sottomenu dei dati, ci sono il caricamento e l'esportazione delle scatole, un rapporto sul contenuto di una scatola, tre basi di dati e un editore a lotti; sotto la risoluzione dei problemi c'è il caricamento forzato di un salvataggio, che serve quando il programma non riconosce il formato; e sotto il sottomenu dedicato al formato testuale delle squadre c'è l'importazione di un insieme dagli appunti.

Delle tre basi di dati va corretta una affermazione che questo documento ha portato per poche ore, perché era sbagliata e la verifica costava una esportazione. Avevo scritto che la base di dati dei doni segreti contenesse la medesima tabella da cui `catalogo-eventi-gen3.py` genera il nostro catalogo. Non è così, e la prova è l'esportazione integrale di quella base fatta il 2026-09-01: ottocentosettantuno file, nessuno dei quali di terza generazione. Le estensioni presenti coprono dalla quarta alla nona generazione, cioè ottantaquattro carte di quarta, duecentoquattro di quinta, trecentosessantadue e centoventiquattro delle due successive, e il resto delle ultime.

La ragione è nella natura del dato e la conosciamo già: la terza generazione non ha mai avuto un formato binario uniforme per i doni, e la sua tabella vive nel codice del verificatore invece che in file distribuibili, come il commento della tabella stessa dichiara e come il nostro catalogo riporta. Ne segue che gli eventi di terza generazione non stanno nella base dei doni segreti ma in quella degli incontri, che espone i modelli di incontro fra cui i doni di quella generazione.

L'esportazione ha però un valore che non era il suo scopo, ed è maggiore di quello cercato. Ottocentosettantuno carte di dono dalla quarta alla nona generazione sono il materiale della campagna di trasferimento per le generazioni che hanno una porta sola: una carta iniettata in un salvataggio di quarta o quinta generazione si riscatta dentro il gioco, e l'esemplare lo genera il gioco. È la medesima logica per cui la ricreazione della distribuzione di terza generazione è coerente per costruzione, e su quelle due generazioni è la via più fedele che esista.

Il giudizio si legge dall'indicatore di conformità che il programma mostra accanto all'immagine dell'esemplare, in alto a sinistra: cliccandolo si apre il rapporto. Quel rapporto è il risultato dell'esperimento, e va confrontato voce per voce con la colonna delle provenienze che `genera-evento-gen3.py` stampa, perché è quella a dire se un difetto contestato sia nostro o dei dati di terzi da cui i metadati provengono.

## confronta-ace-builder.py

Confronta il costruttore di esemplari della comunità con ciò che questo progetto ha verificato, e serve a una domanda che era aperta: se ricreare la distribuzione originale e scrivere direttamente i byte producano lo stesso esemplare. Esegue cinque confronti, in ordine di durezza decrescente per i primi quattro e con il quinto di natura diversa.

I primi quattro mettono a paragone due dichiarazioni scritte in codice: la tabella delle ventiquattro permutazioni delle sottostrutture, la tabella dei caratteri della terza generazione sull'intersezione dei caratteri che entrambe dichiarano, il vocabolario dei metodi come confronto fra insiemi, e l'inventario delle distribuzioni congiunto sulla coppia formata dal nome dell'allenatore e dall'identificativo. Il quinto esegue il nostro `pokebridge.eventi` sul corpus di esemplari conservati che il costruttore porta con sé, e verifica che riproduca valore di personalità, valori individuali e sesso dell'allenatore a partire dal solo seme.

```powershell
python tools/confronta-ace-builder.py --scarica _notes/fonti/ace-builder
python tools/confronta-ace-builder.py --ace _notes/fonti/ace-builder
python tools/confronta-ace-builder.py --ace _notes/fonti/ace-builder --verbose
```

```bash
python tools/confronta-ace-builder.py --scarica _notes/fonti/ace-builder
python tools/confronta-ace-builder.py --ace _notes/fonti/ace-builder
python tools/confronta-ace-builder.py --ace _notes/fonti/ace-builder --verbose
```

Il primo comando scarica il sorgente seguendo il grafo degli import a partire dal modulo di ingresso, e prende a parte il corpus, che il costruttore carica a tempo di esecuzione e che quindi il grafo non raggiunge. Il sorgente non è una dipendenza di questo repository e non vi entra: vive sotto `_notes/`, come i disassemblati e gli export delle chat.

Due dettagli di implementazione valgono la menzione perché sono lezioni e non scelte. Il filtro sui riferimenti degli import rifiuta ciò che contiene caratteri non ammessi in un percorso, e non è pedanteria: senza di esso l'espressione regolare aggancia le stringhe dentro i commenti, e la prima versione ha spedito al servizio un percorso che conteneva un blocco di codice intero. E l'uscita è riconfigurata in UTF-8, perché i nomi degli allenatori giapponesi non passano dalla codifica predefinita della console di Windows e senza quella riga il programma muore alla stampa finale dopo avere eseguito tutti i confronti, che è il modo peggiore di fallire.

L'esito registrato il 2026-09-01 sta in `recreate-pokemon-distributions-events/STUDIO-03-verifica-del-metodo-sul-corpus.md`, e il codice verificato sta in `pokebridge/eventi.py` con `tests/test_eventi.py`.

## fetch-discord.py

Legge la cronologia di un canale Discord attraverso un bot account ufficiale, con impaginazione, un cursore che permette di leggere soltanto il delta fra due corse, e gli stessi tre filtri di `read-chat-export.py`, cioè parola chiave, lunghezza minima e data, per non avere due grammatiche di filtro nello stesso progetto.

Sette difese sono state aggiunte il 2026-08-31, dopo che il collaudo su un server di prova aveva mostrato quanto poco un canale vuoto eserciti. Il limite di frequenza è gestito in due modi e non in uno: quello reattivo attende ciò che il servizio dichiara nel rifiuto, prendendo il maggiore fra il valore dell'intestazione e quello del corpo perché attendere di più è sicuro e attendere di meno rifiuta ancora; quello preventivo legge a ogni risposta quante richieste restano nella finestra e fra quanto si azzera, e attende quando sono esaurite, cioè evita il rifiuto invece di reagirvi. Un guasto di rete, un timeout o un errore del servizio non fermano una cronologia a metà ma fanno riprovare con attesa raddoppiata fino a un tetto, e dopo i tentativi dichiarati si abbandona riferendo l'ultimo esito invece di un messaggio generico. Le discussioni e i post di forum sono canali con un identificativo proprio e nelle community di sviluppo sono il posto dove sta la conoscenza: l'elenco dei canali le include leggendo l'endpoint dedicato, e la lettura funziona su un loro identificativo come su quello di un canale. Il contenuto che non è testo, cioè i blocchi incorporati e la citazione del messaggio a cui una risposta si riferisce, entra nella resa e nei filtri, perché ignorarlo renderebbe vuoti messaggi che di contenuto ne hanno e scarterebbe per lunghezza proprio quelli. Il testo di terzi che apre con un cancelletto viene protetto, perché altrimenti forgerebbe un'intestazione e spezzerebbe la nota, e dentro un blocco di codice recintato non si tocca nulla. La data del filtro viene verificata nella forma, perché una data scritta con le barre passerebbe senza errore e scarterebbe tutto o nulla. E si può aggiungere in coda a un file invece di sovrascriverlo, con l'intestazione scritta una volta sola.

Esiste perché il progetto conosceva due sole vie di accesso a una fonte di quel tipo, il token personale e la copia manuale, e la prima è vietata dalle condizioni d'uso mentre la seconda è manuale per definizione. La terza via, cioè un account dedicato all'automazione creato nel portale per sviluppatori, era ignota al progetto fino al 2026-08-31; la regola `.claude/rules/web-sources-not-fetchable.md` documenta il criterio che la separa dalla prima, e il limite che la rende inapplicabile dove il consenso di chi amministra il canale non si ottiene.

La parte di questo strumento che vale conoscere è il presidio. Invia sempre l'intestazione di autorizzazione nella forma prevista per i bot e, prima di qualunque lettura, verifica che l'account autenticato sia dichiarato tale, arrestandosi con la ragione se non lo è: un token personale inserito per errore nella variabile d'ambiente non produce una lettura riuscita ma un rifiuto. La prova che il presidio funzioni è un controllo negativo dentro `--self-test`, che esercita l'intera logica contro un trasporto finto e non richiede credenziali: sono trentasette controlli, e quattro di essi sono negativi, cioè fallirebbero se un presidio venisse rimosso. Il trasporto finto accetta un programma di risposte, cosicché un rifiuto o un guasto si possano collocare in una posizione precisa della sequenza e si possa verificare non soltanto che la lettura riesca, ma quanto si è atteso e quante richieste sono state fatte.

Il flusso è stato eseguito contro il servizio il 2026-08-31 su un server di prova di proprietà dell'utente, e ha funzionato in ogni passo: elenco dei server, elenco dei canali di testo, lettura della cronologia con il testo dei messaggi presente, filtro per parola chiave che riduce cinque messaggi a due, e cursore che alla corsa successiva riferisce che non c'è nulla di nuovo. Resta non provato sul servizio ciò che un server di prova non può esercitare, cioè l'impaginazione oltre i cento messaggi e l'attesa dopo un rifiuto per eccesso di frequenza: entrambe sono provate contro il trasporto finto e nessuna delle due è stata osservata sul campo.

Due osservazioni vengono da quella corsa e valgono per chi la ripeterà. Fra i messaggi letti compare anche la riga di sistema che annuncia l'ingresso del bot nel canale, perché per il servizio è un messaggio come gli altri, e chi vuole escluderla usa `--min-length`. E il nome predefinito del file di uscita dipende da canale e data, quindi due corse dello stesso giorno sullo stesso canale finiscono sullo stesso file: lo strumento ora avvisa quando sovrascrive, e con `--out` si scrive altrove.

Una scelta di progetto va motivata perché il materiale di partenza suggeriva altro, cioè un server MCP dedicato. In un agente residente che deve poter chiamare quel tool durante una conversazione quella è la scelta giusta; qui il lavoro è deterministico, cioè leggere una fonte e trasferirla nel registro, e la regola sull'economia dei token prescrive di tenerlo su codice invece che su modello. Un programma sulla sola libreria standard fa quel lavoro senza aggiungere una dipendenza su Node, un pacchetto di terze parti da fidare con un token, e uno strato di protocollo fra noi e una richiesta HTTP.

## DiscordChatExporter, e la procedura di esportazione dei canali

Non è uno strumento del progetto ma di terze parti, e sta qui perché la procedura d'uso è parte della conoscenza operativa: una procedura che vive in una conversazione è una procedura perduta alla sessione successiva. La fonte è registrata in `SOURCES.md` al livello 3, la decisione che ne autorizza l'uso in questo progetto è ADR-019, e il criterio che distingue le vie di accesso a un canale sta nella regola `.claude/rules/web-sources-not-fetchable.md`.

### Che cosa fa, e come si colloca rispetto allo strumento proprio

Esporta la cronologia di un canale in HTML, testo semplice, JSON o CSV, scarica gli allegati, e ha comandi per un canale singolo, per un server intero, per i messaggi diretti e per tutto ciò che è accessibile. È maturo e completo, e su tre cose è superiore a `tools/fetch-discord.py`: scarica i media in locale, produce una resa HTML che replica l'interfaccia di Discord ed è quindi il formato migliore per rileggere una discussione lunga, e ha una interfaccia grafica comoda quando si deve girare fra molti server per capire quali canali esistano.

Lo strumento proprio resta per ciò che DCE non fa: il cursore che legge il solo incremento fra due corse senza gestire identificativi a mano, l'uscita già filtrata nella convenzione del progetto, e il presidio sul tipo di token. La divisione naturale è quindi che DCE faccia le esportazioni grosse e periodiche, poche volte l'anno, e che il lettore proprio faccia gli aggiornamenti incrementali dove il bot è stato invitato.

Il ponte fra i due esiste già e non va costruito: `tools/read-chat-export.py` era stato scritto per digerire il JSON di DCE, con le chiavi `guild`, `channel` e `messages`.

### Dove vivono i file

Il programma non entra nel repository e va nella cartella condivisa fuori da esso, secondo la convenzione enunciata in apertura di questo documento: per esempio `E:\tools\dce` per la riga di comando e `E:\tools\dce-gui` per l'interfaccia grafica. Va notato che tenerlo nella cartella dei download del sistema, come è accaduto durante il primo allestimento, è la collocazione peggiore di tutte fra quelle fuori dal repository, perché quella cartella si svuota per abitudine o per strumento di pulizia e il percorso che si è scritto nei comandi smette di esistere senza preavviso. Gli export vanno sotto `_notes/fonti/dce/`, che il `.gitignore` esclude in blocco: restano locali per costruzione, e questo è voluto perché sono contenuto di terzi.

### Il rilascio e i file da scaricare

Il rilascio corrente alla data di questa nota è il 2.48, del 27 agosto 2026, e la pagina che dice sempre quale sia l'ultimo è `https://github.com/Tyrrrz/DiscordChatExporter/releases/latest`. I file sono autonomi e non richiedono di installare alcun runtime.

Per Windows su processore Intel o AMD servono i due archivi con il suffisso `win-x64`: `DiscordChatExporter.Cli.win-x64.zip` per la riga di comando, circa 11 MB, e `DiscordChatExporter.win-x64.zip` per l'interfaccia grafica, circa 48 MB. I suffissi `win-arm64` e `win-x86` sono rispettivamente per i processori ARM e per i sistemi a 32 bit, e non servono qui. Esistono anche gli archivi per Linux e macOS e una immagine Docker, `tyrrrz/discordchatexporter`, che è la via da preferire su una macchina dove non si voglia estrarre nulla.

### Il token, e le tre cose da sapere

DCE accetta sia un bot token sia il token di un account personale, e la scelta determina la portata: con il primo vede i soli canali in cui il bot è stato invitato, con il secondo tutto ciò che vede l'account. Le implicazioni della seconda via, e la decisione del progetto, stanno in ADR-019.

Il token di un account si ottiene con la procedura che DCE stesso documenta. In Discord aperto nel browser, non nell'applicazione desktop, si aprono gli strumenti di sviluppo con la combinazione di tasti per l'ispezione e si va sulla scheda della console; se la console rifiuta di incollare, si scrive `allow pasting` e si conferma, che è una protezione contro le truffe e non un errore. Poi si esegue la riga che la documentazione di DCE riporta, la quale recupera il token dal modulo interno dell'applicazione e lo stampa.

Due inciampi di questa procedura sono stati osservati sul campo il 2026-08-31 e vanno registrati, perché entrambi sembrano un errore di chi esegue e non lo sono. Il primo è che la frase da scrivere per sbloccare l'incollamento va scritta soltanto se il browser la chiede: se non compare alcun avviso, quelle parole vengono interpretate come codice e producono un errore di sintassi, che è innocuo e non impedisce nulla. Il secondo è che, con l'interfaccia degli strumenti di sviluppo in una lingua diversa dall'inglese, la frase richiesta può essere tradotta: va scritta quella che l'avviso indica, non quella riportata in una guida.

Esiste una seconda via per il medesimo token, documentata da DCE e utile quando la prima non funziona, e non passa dalla console. Nella scheda della rete si ricarica la pagina, si filtra per il nome dell'endpoint dei messaggi, si apre la voce che compare e si legge il valore dell'intestazione di autorizzazione fra quelle della richiesta.

Il comando si lancia da qualunque cartella, perché il percorso dell'eseguibile è assoluto; su PowerShell un percorso fra apici va preceduto dall'operatore di chiamata, cioè dalla e commerciale, altrimenti la shell tratta la stringa come testo e non la esegue.

Tre cose operative su quel token, e nessuna è una formalità. Non va scritto in alcun file, nemmeno in `.env`: si incolla nel comando al momento dell'uso, perché un token in un file è un token che prima o poi finisce in un commit, e l'esportazione avviene poche volte l'anno. Cambia quando si cambia la password dell'account, quindi dopo un cambio password va ripreso. E dà accesso completo all'account, quindi non va incollato in una conversazione né condiviso in alcuna forma.

### I comandi, nell'ordine in cui si usano

Dalla cartella dove è stata estratta la riga di comando. Su PowerShell il nome dell'eseguibile va prefissato con `.\`, su un prompt tradizionale no, e su Linux o macOS il file si chiama senza estensione.

Il primo comando elenca i server accessibili con il loro identificativo, e serve a sapere su che cosa si sta lavorando: `DiscordChatExporter.Cli.exe guilds -t "TOKEN"`.

Il secondo elenca i canali di un server: `DiscordChatExporter.Cli.exe channels -t "TOKEN" -g ID_DEL_SERVER`. È il passo che non va saltato, perché su un server di sviluppo con decenni di cronologia distribuita su decine di canali l'esportazione totale è inutile prima che costosa: la conoscenza che serve sta in pochi canali, e il resto è rumore che poi va filtrato.

Il terzo esporta un canale: `DiscordChatExporter.Cli.exe export -t "TOKEN" -c ID_CANALE -f Json -o "PERCORSO\%G-%C.json"`. Il formato JSON è quello che il convertitore del progetto digerisce; i segnaposto `%G` e `%C` diventano il nome del server e quello del canale, cosicché i file si riconoscano senza aprirli.

Esistono le varianti per un server intero e per tutto ciò che è accessibile, cioè `exportguild -g ID` e `exportall`, e vanno usate sapendo che producono volumi grandi.

### Le tre opzioni che cambiano il risultato

L'intervallo di date, con `--after 2023-01-01` ed eventualmente `--before`, limita l'esportazione nel tempo. Sulla prima passata di un canale con anni di storia conviene, perché la parte antica di un canale tecnico è spesso superata dal codice che nel frattempo è stato scritto.

Il download degli allegati, con `--media`, porta in locale immagini e file. Su un canale tecnico pieno di schemi elettrici e schermate vale molto, ma moltiplica il volume: non alla prima passata, e poi soltanto sui canali che si è deciso di conservare.

Il formato leggibile, con `-f HtmlDark` oppure `-f HtmlLight`, produce una resa che replica l'interfaccia di Discord. Conviene esportare due volte lo stesso canale, in JSON per la catena automatica e in HTML per la lettura umana, perché sono due usi diversi dello stesso materiale.

Un'ultima nota di comportamento: una esportazione lunga rallenta da sola, perché DCE rispetta i limiti di frequenza dichiarati dal servizio. È il comportamento corretto e va lasciata girare, non interrotta e rilanciata.

### I server piccoli, esportati interi

Dal 2026-08-31 la tabella dei canali ha una compagna, `GUILDS`, che elenca i server da esportare interi invece che canale per canale. Serve al caso in cui la selezione costerebbe più di quanto risparmi, cioè un server piccolo e monotematico di cui il progetto non conosce gli identificativi dei canali, e si appoggia al sottocomando `exportguild` dello strumento, che non richiede alcun identificativo di canale. Il primo server così trattato è quello dedicato all'esecuzione di codice arbitrario in terza generazione.

Vale dire perché questa via esiste accanto all'altra e non al suo posto. Un identificativo di canale inventato produce un errore che non nomina il campo sbagliato, come questa stessa giornata ha mostrato quando un segnaposto è stato incollato alla lettera, quindi dove gli identificativi non si conoscono la scelta corretta non è indovinarli ma cambiare granularità. Dove invece si conoscono, la selezione per canale resta preferibile, perché un archivio di trenta canali scelti è leggibile e uno di un server intero no.

```powershell
python tools/export-discord.py --guilds --dry-run
python tools/export-discord.py --guilds --dce "C:\Users\Utente\Downloads\DiscordChatExporter.Cli.win-x64\DiscordChatExporter.Cli.exe"
```

```bash
python tools/export-discord.py --guilds --dry-run
python tools/export-discord.py --guilds --dce "$HOME/DiscordChatExporter.Cli/DiscordChatExporter.Cli.exe"
```

L'uscita non è un file ma una cartella per server sotto `_notes/fonti/dce/`, perché i nomi dei canali si conoscono soltanto a esportazione avvenuta: lo strumento nomina da sé i file quando riceve una cartella come destinazione. La protezione contro la sovrascrittura è la stessa dell'altra via, cioè una cartella che esiste e non è vuota viene saltata a meno di `--forza`.

### La catena verso il progetto

L'esportazione non è il risultato: il risultato è la sintesi con l'attribuzione nel registro delle fonti. Il passo intermedio è `python tools/read-chat-export.py PERCORSO.json --grep PAROLA --min-length 40`, che riduce il JSON a Markdown filtrato, tenendo autore, momento, testo, allegati e citazioni e scartando la struttura di navigazione.

Da lì vale il flusso che il progetto ha già stabilito, e la ragione per cui vale è che una fonte grezza conservata accanto alla sua sintesi produce il dubbio su quale sia quella buona. Si legge il Markdown filtrato, ciò che documenta entra in `SOURCES.md` in prosa con la profondità che rende il file grezzo sacrificabile, ciò che tocca la referenza dei formati o la tesi entra nei documenti corrispondenti, e il grezzo si elimina quando non porta più informazione che non sia scritta altrove. È ADR-016.

Una avvertenza che vale per il filtro e non per lo strumento: la ricerca per parola chiave sul contenuto di un canale è un filtro cieco alla domanda, mentre la ricerca interna al canale fatta da chi conosce la domanda incorpora la domanda. La regola sulle fonti non recuperabili registra che la seconda ha reso, su un caso reale, più della prima; ne segue che un export in blocco non sostituisce la ricerca mirata ma la precede, e che la lista dei termini da cercare va scelta prima di lanciare il filtro.

## lint-md-tables.py

Verifica la struttura delle tabelle Markdown, e copre un punto cieco che nessun altro strumento del progetto poteva coprire. La convenzione di scrittura vuole ogni paragrafo su una riga sorgente unica e lo strumento che la attua è `md-unwrap`, il quale ha però per contratto di non toccare le tabelle, che conserva riga per riga e senza riallineare: è la scelta giusta, perché in una tabella l'a capo è strutturale, e proprio per questo dentro una tabella non c'è nessuno che guardi.

Due difetti, entrambi osservati sul campo il 2026-09-01 e con in comune di non produrre alcun errore e di superare una revisione a video. Il primo è una riga vuota dentro una cella: chi scrive una cella lunga è tentato di spezzarla in paragrafi, e il risultato è che la tabella si chiude a quella riga vuota, il renderer mette il resto della cella fuori dalla griglia come prosa, e le righe successive escono dalla tabella. Il secondo è una riga con meno colonne dell'intestazione: il renderer non protesta e lascia le celle mancanti vuote, quindi un campo obbligatorio per convenzione può essere assente senza che nessuno lo noti, e due voci del registro delle fonti sono rimaste prive della colonna dei track per un giorno.

```powershell
python tools/lint-md-tables.py
python tools/lint-md-tables.py SOURCES.md docs
python tools/lint-md-tables.py --self-test
```

```bash
python tools/lint-md-tables.py
python tools/lint-md-tables.py SOURCES.md docs
python tools/lint-md-tables.py --self-test
```

Il criterio con cui la cella spezzata si riconosce merita di essere raccontato, perché le prime due versioni dello strumento lo avevano sbagliato nello stesso modo. Esse guardavano ciò che segue la tabella e sospettavano una cella spezzata quando vi trovavano prosa: la prima sospettava qualunque prosa, la seconda escludeva titoli ed elenchi. Erano entrambe euristiche sul contenuto, e la prosa piana fra due tabelle è legittima, tanto che il catalogo generato degli eventi la impiega per etichettare i propri blocchi e produceva quattordici falsi positivi su sedici segnalazioni.

Il criterio giusto è strutturale e sta dentro la tabella e non fuori di essa: una riga di tabella si chiude con la barra verticale, e una cella tagliata da una riga vuota lascia l'ultima riga del blocco priva di quella barra, perché è stata interrotta a metà. Non ha falsi positivi sulle tabelle del progetto, si applica anche quando dopo la tabella non segue nulla, e non richiede di interpretare la prosa. La generalizzazione vale oltre il caso: quando un controllo richiede di indovinare l'intenzione di un testo, conviene cercare se il medesimo difetto lasci una traccia nella forma, perché la forma si verifica e l'intenzione si congettura.

Va registrata anche una cattiva pratica di cui questo strumento è stato l'occasione, perché è più insidiosa del difetto che cercava. Nella prima versione avevo scritto il caso del titolo fra due tabelle con esito atteso pari a uno, cioè avevo dichiarato il falso positivo come comportamento voluto: la suite passava mentre lo strumento sbagliava. Una prova che si adatta al codice invece di misurarlo è peggio dell'assenza di prove, perché produce fiducia senza fondarla.

## Gli strumenti di infrastruttura

Nella cartella `tools/` della radice ci sono i due strumenti che servono al repository e non ai giochi. Il primo, `md-unwrap.py`, attua la convenzione di formattazione Markdown del progetto, cioè un paragrafo per riga sorgente, e ha una modalità di sola verifica per il controllo prima di un commit.

```
python tools/md-unwrap.py .
python tools/md-unwrap.py --check .
```

Il secondo, `lint-md-commands.py`, verifica che i comandi di shell dentro i blocchi recintati non siano spezzati su più righe, perché `md-unwrap` per contratto non tocca il contenuto dei blocchi recintati e quindi un comando spezzato là dentro non lo corregge nessuno.

## save-deploy.py, il cancello prima dell'hardware

Tre dei cinque sottoprogetti convergono, presto o tardi, sulla stessa operazione: prendere un file di salvataggio e metterlo su un supporto fisico, cioè una cartuccia tramite il lettore oppure la scheda SD della console modificata. È l'unica operazione irreversibile del progetto, e per questo esiste uno strumento alla radice invece di tre procedure separate dentro i sottoprogetti.

La cosa da capire di questo strumento è che non scrive, e non scriverà finché l'hardware non è presente e collaudato. Ciò che fa è la parte che si può scrivere oggi e che evita i danni. Esamina il file: la dimensione confrontata con quelle che hanno un significato, l'impronta SHA-256 che identifica il contenuto, il numero di settori che portano la firma 0x08012025, il numero di settori il cui checksum torna, l'identificazione del gioco con il margine sul secondo candidato, e i due casi degenerati del file interamente a zero e del file interamente a 0xFF, che è lo stato di una flash cancellata. Poi verifica le precondizioni della destinazione e produce il piano dei passi.

La validazione non è duplicata: lo strumento importa `emerald_bag_decode.py` dal track Smeraldo e usa le sue funzioni di validazione dei settori, di ricostruzione dello slot e di identificazione del gioco. Un secondo esemplare della stessa formula di checksum sarebbe un secondo posto dove sbagliarla.

```
python tools/save-deploy.py check "percorso/salvataggio.sav"
python tools/save-deploy.py targets
python tools/save-deploy.py plan "salvataggio.sav" --target gbxcart --backup "D:/bk1/pre.sav" --backup "E:/bk2/pre.sav"
```

La parte più importante è il cancello dei backup, che mette in atto in codice il vincolo normativo di `.claude/rules/hardware-and-perimeter.md`. Lo strumento pretende due backup dichiarati, verifica che i percorsi siano distinti, che i file esistano e siano leggibili, che la dimensione coincida con quella dell'originale e che le due impronte coincidano fra loro, e rifiuta anche il caso in cui i due backup stiano sullo stesso volume, perché un guasto del supporto li perderebbe insieme. Quando una di queste condizioni manca, il piano non viene stampato affatto: è una scelta deliberata, perché una lista di passi mostrata sotto un elenco di problemi invita a eseguirla comunque.

Il piano, quando esce, ha cinque passi nell'ordine che la regola impone: dump del contenuto attuale del supporto, confronto con i backup dichiarati, scrittura, rilettura confrontata byte per byte, e infine avvio del gioco, che è un controllo diverso dal precedente e non lo sostituisce. Poi lo strumento dichiara che la scrittura non viene tentata e dice cosa manca a quella destinazione: per la cartuccia mancano il lettore e un collaudo su un esemplare sacrificabile, per la scheda SD manca la decisione su quale percorso sia quello giusto per il titolo installato.

Il collaudo è avvenuto su un salvataggio Smeraldo sintetico generato per l'occasione, con quattordici settori firmati e coerenti, e ha verificato i tre casi che contano: il file valido identificato come Smeraldo con punteggio sei contro zero e meno tre, il rifiuto del file interamente a zero e della dimensione non riconosciuta, e il rifiuto del piano nei tre modi in cui i backup possono essere insufficienti, cioè uno solo, inesistente, oppure due sullo stesso volume.

## Che cosa manca

Il prossimo strumento naturale è il generatore della tabella dagli indici interni di generazione 1 ai numeri nazionali, che oggi non esiste e che va costruito con lo stesso metodo, cioè leggendolo dal disassemblato e verificandolo con sentinelle. La referenza tecnica lo elenca fra i punti aperti, ed è l'ultimo dato costante del progetto che sarebbe tentante trascrivere a mano.

## Cosa leggere dopo

[[20-architettura-codice]] colloca questi strumenti nella stratificazione del software, e [[21-collaudo]] racconta come il collaudo del secondo ha trovato un difetto reale.
## Il catalogo delle distribuzioni, e perché la provenienza sta in un file a parte

Lo strumento `tools/catalogo-eventi.py` produce `recreate-pokemon-distributions-events/CATALOGO-EVENTI.md`, che è il documento da leggere quando serve sapere non che cosa un esemplare sia ma da dove venga. Esiste perché il generatore scrive file i cui nomi dicono la specie e poco altro, mentre un esemplare da evento è un oggetto storico prima che un dato: è stato consegnato in un luogo, in una finestra che a volte durava tre ore e a volte tre anni, e in un modo che ne spiega la rarità.

La struttura del documento riflette una distinzione che vale enunciare perché è il motivo per cui esistono due file invece di uno. I fatti meccanici, cioè specie, livello, mosse, lingua, metodo di generazione, lucentezza e derivazione del sesso dell'allenatore, vengono dalla tabella del verificatore di conformità, che è codice eseguito, e si rigenerano a ogni corsa: se la tabella cambia, il documento cambia da sé. I fatti storici non stanno in nessuna fonte di primo livello, perché nessun disassemblato sa in quali negozi un dono venne distribuito, e sono quindi autorati in `provenienze-eventi.json` con il collegamento alla fonte e la data di lettura accanto a ciascuna voce.

```powershell
python tools/catalogo-eventi.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex
python tools/catalogo-eventi.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --check
```

```bash
python tools/catalogo-eventi.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex
python tools/catalogo-eventi.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --check
```

Il secondo modo non scrive nulla e riferisce se il documento in repository sia allineato alle fonti, cosicché una modifica alla tabella o alle provenienze che non sia stata rigenerata risulti visibile prima di un commit invece che dopo.

Due scelte del programma vanno difese perché sono il genere di cosa che si toglie per fare pulizia. La prima è che i gruppi senza provenienza documentata non vengono taciuti ma elencati con la dicitura esplicita, e il programma stampa quanti sono: un catalogo che nasconda le proprie lacune è peggio di uno incompleto, perché toglie a chi legge la possibilità di colmarle. La seconda è che le divergenze fra la fonte storica e la tabella si scrivono invece di essere risolte in silenzio, con la regola che sui fatti meccanici vale la tabella e sui fatti storici vale l'enciclopedia, che è la sola a occuparsene.

Il file delle provenienze porta anche l'unico campo meccanico che gli appartiene di diritto, ed è l'oggetto tenuto documentato dalla storia. Nel catalogo esistono due specie di oggetto tenuto con gradi di verità diversi: quello derivato, che l'evento del desiderio estrae dal generatore pseudocasuale e che è quindi una funzione del seme, e quello storico, come la Sfera Luminosa del Pikachu del decennale, che non discende da nessun calcolo. La tabella del verificatore non dichiara il secondo e non lo pretende, perché un oggetto tenuto si può togliere o scambiare e non è un vincolo di legittimità; resta un tratto dell'esemplare originale, e la distinzione fra un esemplare che passa i controlli e uno fedele all'originale passa esattamente per fatti di questo genere.
## La copertura della verifica esterna, e il registro dei giudizi

Lo strumento `tools/copertura-verifica.py` risponde a una domanda che il rapporto fra due numeri non sa affrontare: sapere che sette esemplari su centoventidue sono stati giudicati non dice dove stia il rischio residuo, perché gli esemplari non sono intercambiabili. Esso legge il registro dei giudizi in `recreate-pokemon-distributions-events/giudizi-esterni.json`, che è autorato perché ciascuna voce è il resoconto di una prova eseguita da una persona, e lo confronta con la tabella del verificatore per calcolare la copertura lungo ciascuna dimensione in cui gli esemplari differiscono.

```powershell
python tools/copertura-verifica.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex
```

```bash
python tools/copertura-verifica.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex
```

La distinzione che il programma applica va conosciuta perché cambia come si legge l'esito. Le dimensioni strutturali, cioè metodo di generazione, ramo della lucentezza, derivazione del sesso dell'allenatore e lingua, sono rami di codice: provarne uno lo prova per ogni esemplare che vi passi, quindi la loro copertura si può chiudere e va chiusa. Le dimensioni di dato, cioè specie e livello, sono righe di tabella: provarne una prova quella riga e nessun'altra, quindi la loro copertura resta parziale per costruzione e il rischio si riduce per un'altra via, cioè generando i dati da una fonte invece di trascriverli. Fra le due sta il gruppo di crescita, che è una formula scelta da un dato: le formule sono sei e provarle tutte è fattibile.

Per ciascun valore non ancora provato il programma nomina la voce che lo esercita, con il nome del file che il lotto scrive per essa, perché un elenco di valori dice dove sta il rischio e non dice che cosa fare.

Dal medesimo giorno lo strumento risponde anche alla domanda su quante prove servano, e la risponde in modo esatto invece di stimarla. Il modo `--minimo` formula la questione come problema di copertura di insiemi: l'universo sono le coppie fra dimensione e valore, ciascun esemplare copre esattamente una coppia per dimensione, e si cerca la sottofamiglia di cardinalità minima che copra tutto.

```powershell
python tools/copertura-verifica.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --minimo
```

```bash
python tools/copertura-verifica.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --minimo
```

Due cose vanno conosciute per leggerne l'uscita. La prima è che il massimo delle cardinalità delle dimensioni è un limite inferiore e non il minimo: su una dimensione con nove valori servono almeno nove esemplari perché ciascuno ne copre uno solo, ma che nove bastino richiederebbe che quei nove coprano simultaneamente anche tutti i valori delle altre dimensioni, cioè una condizione di ortogonalità che un catalogo di eventi storici non ha ragione di soddisfare. Al 2026-09-02 il limite inferiore vale nove e il minimo esatto quattordici. La seconda è che il numero utile non è il minimo assoluto ma il minimo residuo, cioè quanti esemplari restino dato ciò che è già stato provato, e non si ottiene sottraendo: i giudizi già eseguiti sono stati scelti per esercitare rami sospetti e non per minimizzare le prove, quindi non formano un sottoinsieme di una soluzione ottima. Il programma risolve quindi una seconda istanza sulle sole coppie residue, e ne stampa gli esemplari da aprire.

Il problema nella forma generale è NP-difficile, e qui si risolve in modo esatto perché è piccolo: le firme di copertura distinte fra i centoventidue esemplari sono trentaquattro, perché molti esemplari coprono le medesime coppie e uno per firma basta, e le coppie da coprire sono ventinove.

## Le due forme in cartelle separate, e la via di massa che ciò rende possibile

Dal 2026-09-02 il modo a lotto scrive la forma di scambio nella cartella indicata e la forma cifrata in una sottocartella. La ragione non è di ordine ma operativa, ed è ciò che rende praticabile la verifica di massa.

Il verificatore offre di caricare una cartella intera dentro le scatole di un salvataggio, e da lì si leggono in poche schermate quali posizioni portino il contrassegno di non conformità: centoventidue esemplari occupano cinque scatole, quindi cinque schermate sostituiscono centoventidue aperture. Quel caricamento però riconosce un file dalla sua dimensione, e le due forme hanno entrambe ottanta byte: tenendole insieme si otterrebbero duecentoquarantaquattro voci di cui la metà illeggibile, perché la forma cifrata letta come forma di scambio produce byte senza senso. Il caricamento di massa non scende nelle sottocartelle, quindi la separazione basta.
## Le schede tecniche degli esemplari

Lo strumento `tools/schede-esemplari.py` produce `recreate-pokemon-distributions-events/SCHEDE-ESEMPLARI.md`, che per ciascuna voce producibile porta ogni campo derivato con la propria provenienza, e accanto al titolo lo stato del suo giudizio esterno.

```powershell
python tools/schede-esemplari.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex
python tools/schede-esemplari.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --check
```

```bash
python tools/schede-esemplari.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex
python tools/schede-esemplari.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex --check
```

La ragione per cui il documento esiste è che un giudizio di conformità riguarda una configurazione precisa di byte e non una categoria: registrare soltanto che un esemplare è conforme perde l'informazione su che cosa esattamente sia stato dichiarato tale, e senza quella non si può né riprodurre il caso né riconoscere che una modifica successiva lo ha cambiato.

Una scelta del programma va conosciuta perché è controintuitiva: esso non legge i file prodotti ma li ricalcola dalle sorgenti con il medesimo codice che li scrive. Un documento che leggesse i file descriverebbe il disco di una macchina, che non è versionato; questo descrive ciò che il progetto produce e resta vero in un clone dove i file non esistono ancora. L'effetto collaterale è una verifica del determinismo: se due corse dessero schede diverse, la scelta del seme non sarebbe riproducibile e il difetto si vedrebbe come una modifica del documento che nessuno ha fatto.
