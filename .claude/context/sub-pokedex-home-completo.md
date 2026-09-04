---
generated-from-commit: e692a02b8a46ab119e0389449d61327384841236
generated-from-branch: main
generated-date: 2026-09-02
covers-paths:
  - pokedex-home-completo/
last-verified-commit: 0f72ba487040b9198c78e3d9512285f45b55c1c8
stato: attivo, asse degli eventi da tre fonti con 6244 voci di cui 3095 sotto scadenza e 433 specie distinte, ottenibilita misurata, terza generazione chiusa a 386 su 386
---

# Sottoprogetto: Pokedex completo in Pokemon Home

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`.

Obiettivo: la collezione completa in Pokemon Home, cioè una voce per ogni specie e per ogni forma che il deposito possa contenere. È l'obiettivo principale del progetto, e gli altri sottoprogetti possono concorrervi restando ciascuno autonomo con uno scopo proprio.

## Dove siamo

Aperto il 2026-09-02 con una consegna dell'utente e con una verifica indipendente che ha già prodotto il risultato che governa la pianificazione di tutto il progetto: la chiusura della banca non vincola il completamento del Pokedex, né a livello di specie né a livello di forma. Il risultato regge, ma fino al 2026-09-04 poggiava sul contrassegno di presenza delle tabelle delle statistiche, cioè era un limite inferiore e non una misura: da quella data è misurato sugli incontri reali e la sezione in fondo a questa scheda lo riporta nella forma corretta. Tutte e milleventicinque le specie sono raggiungibili per la via diretta, e le dodici voci-forma che soltanto la via indiretta dichiara sono escluse da un filtro letto dalla fonte, cioè dieci forme totemiche che al trasferimento tornano alla forma base o non si trasferiscono affatto, e due forme di sola battaglia che non possono stare in una scatola. Il conto lo esegue `tools/disponibilita-titoli.py` e si rifà a comando.

Ne segue che i giorni fino al 26 febbraio 2027 non si spendono qui ma sugli esemplari la cui identità richiede una provenienza anteriore all'ottava generazione, che sono materia del track delle distribuzioni e delle cartucce possedute.

## Aggiunta del 2026-09-02: la raccolta di salvataggi esterni

L'utente ha consegnato trenta file in `_notes/salvataggi/`, provenienti dalla categoria dei salvataggi contribuiti di Project Pokemon e da tre forum italiani, con una lista che per ciascuno dichiara provenienza e contenuto. Sono tutti e trenta verificati integri e identificati dal gioco che dichiarano, e il censimento generato è `CENSIMENTO-SALVATAGGI.md`; la nota che lo interpreta, con il metodo di identificazione e le tre domande che un salvataggio esterno pone, è `STUDIO-02-salvataggi-esterni-e-che-cosa-provano.md`.

Il numero che serve a questo track è la copertura: l'unione delle specie presenti come esemplare nella raccolta copre trecentottantacinque delle trecentottantasei voci nazionali di terza generazione, e manca soltanto Poochyena. Va letto con la precisione che merita, cioè che riguarda ciò che sta nei depositi e non le caselle del Pokedex, che sono un dato diverso e non ancora letto.

Le quattro fonti sono in `SOURCES.md` al livello cinque, come ADR-024 prescrive. Il perimetro dell'uso resta quello di ADR-024 per gli esemplari, mentre ADR-029 aggiunge la distinzione fra importare uno stato di avanzamento, che è ammesso per sbloccare il Parco Amici a tre condizioni, e importare un esemplare, che resta subordinato al giudizio del verificatore.

## Aggiunta del 2026-09-03: la catena risponde, e la lista di spunta esiste

L'ultimo anello della catena verso il deposito finale non è più un'ipotesi: la voce che sposta gli esemplari esiste, risponde, e su un deposito vuoto dichiara di non avere nulla da spostare. Lo stato è documentato in `STUDIO-03-la-catena-e-viva-e-la-lista-di-spunta.md`, che in apertura dichiara la distinzione richiesta da ADR-030, cioè che si registra lo stato della catena e non la procedura del deposito intermedio, sul quale il limite di perimetro resta intero.

Quattro vincoli numerici sono entrati nei conti e nessuno li avevamo. Il deposito intermedio tiene tremila posizioni, quindi è un condotto e non un magazzino. Rimuove gli oggetti tenuti al deposito, il che tocca il nostro lotto perché alcune voci del catalogo portano un oggetto che fa parte della loro identità storica. L'identificativo di rete si lega a una sola console, quindi parallelizzare i trasferimenti su una seconda console è escluso per costruzione. E un periodo di prova ha un conto alla rovescia già cominciato, il cui numero di giorni va riletto sulla console perché nelle fotografie la prima cifra non è leggibile.

La lista di spunta è `CHECKLIST-COMPLETA.md`, generata da `tools/checklist-pokedex.py`. Il codice interno è la coppia fra numero del Dex e indice di forma, scritta `PKD-####-##`, e serve perché il numero del Dex identifica una specie e non un esemplare da ottenere: non cambia per il sesso, per una variante regionale o per una forma. Al 2026-09-03 la lista dice milleventicinque voci di specie tutte per via diretta, trecentottantacinque con una fonte già nel progetto, e seicentoquaranta senza alcuna fonte: quest'ultimo è il numero che misura la campagna e il solo che scende quando si lavora.

## Aggiunta del 2026-09-03, seconda: il terzo asse e la roadmap

La lista ha ora tre assi, perché la collezione non è l'insieme delle specie ma quello delle specie più le forme che il deposito conta a parte più tutti gli esemplari da distribuzione: un esemplare da distribuzione è un collezionabile distinto anche quando la sua specie è coperta altrove. Le voci da evento enumerate sono 2701, di cui 2686 sotto scadenza con 336 specie distinte, e sono il solo insieme della lista che il 26 febbraio 2027 chiude davvero.

La sorpresa che decide l'ordine di lavoro è che prima e seconda generazione sono le meno costose e non le più costose: non hanno doni segreti ma tabelle di incontro con i campi in chiaro, e in quelle generazioni non esiste alcun valore di personalità né alcun generatore pseudocasuale da ricostruire, quindi 168 voci sono alla portata di `pokebridge` come è oggi. Il costo per voce non cresce con l'età ma con la presenza di un seme, e quella comincia e finisce con la terza generazione. La roadmap in quattro tempi sta nella sezione 9 di `STUDIO-03`.

Una correzione dichiarata e non ancora fatta: il conto che dice zero specie vincolate dalla scadenza poggia sul contrassegno di presenza delle tabelle delle statistiche, e la presenza non è l'ottenibilità. Zero è un limite inferiore e non la risposta; la risposta richiede le tabelle degli incontri. La voce è in `pending.md` ed è il lavoro più grosso fra quelli aperti su questo track.

La scadenza è definitiva e verificata su fonte ufficiale già presente nel registro dal 2026-08-28: 26 febbraio 2027 alle 12:00 del fuso giapponese, cioè le 04:00 in ora italiana di un venerdì, che nel fuso del Pacifico è giovedì 25 alle 19:00, il medesimo istante.

## Aggiunta del 2026-09-03, terza: il primo tempo è eseguito

Centosessantotto voci composte e centosessantacinque scritte con `tools/genera-evento-gb.py`, con le schede in `SCHEDE-EVENTI-GB.md` raggruppate per evento e la provenienza in `provenienze-eventi-gb.json`. Le tre non scritte hanno il nome del donatore in caratteri giapponesi e mancano della tabella dei caratteri di quelle generazioni; quindici portano un allenatore segnaposto perché lo prendono da chi riceve.

Il risultato di metodo vale più del lotto ed è speculare alla terza generazione: là un valore a trentadue bit determina identità e valori individuali, quindi la fedeltà è decidibile per confronto di semi e la legittimità era difficile; qui quel valore non esiste, quindi la legittimità è banale e la fedeltà è impossibile per difetto di informazione. Le sole voci su cui la fedeltà torna verificabile sono le due dei tour, dove la fonte fissa i valori individuali, e le sedici cromatiche, dove la cromaticità li vincola.

Il lotto NON è ancora stato giudicato dal verificatore, e finché non lo è nessuna voce va considerata conforme.

## Aggiunta del 2026-09-03, quarta: il giudizio sul lotto GB e la decisione sull'ambito

Il giudizio esterno ha prodotto tre difetti, tutti corretti con un presidio: il tasso di cattura dei premi di Stadium, che non è quello della specie ma l'identificativo della scatola in cui il premio veniva consegnato; l'ordine dei valori individuali dichiarati per i Mew dei tour, che comincia dai punti salute; e il nome dell'allenatore segnaposto, che eccedeva i sette caratteri del formato. La forma nuova di difetto va ricordata: una voce legale può nascondere un errore che si manifesta soltanto sulle voci vicine, perché il verificatore le assegna un incontro alternativo e la dichiara legale con la provenienza sbagliata.

La prova va completata con due contenitori: i dieci file di prima generazione in un salvataggio di prima e i centocinquantacinque di seconda in un salvataggio di seconda. Il caricamento in blocco in un salvataggio di prima generazione converte i secondi e li invalida per una ragione che non è nostra.

L'utente ha deciso l'ambito: la collezione delle distribuzioni, cioè 2686 voci sotto scadenza e non 336, con esecuzione in due tempi, prima una voce per specie e poi i gemelli. La coda di produzione va quindi ordinata per specie e non per gruppo di evento.

## Aggiunta del 2026-09-03, quinta: il tetto del Parco Amico non esiste sul veicolo che possediamo

È il fatto che decide l'ambito di tutta la campagna, ed era nel registro delle fonti dal 2026-08-28: il limite di sei esemplari ogni ventiquattro ore vale per Diamante, Perla e Platino, mentre HeartGold e SoulSilver lo rimuovono. L'utente possiede un Argento SoulSilver italiano, quindi il collo di bottiglia è sei per sessione senza tetto giornaliero, e le 2686 voci sotto scadenza richiedono circa 448 sessioni: una questione di pazienza e non di calendario. Il tetto di circa mille esemplari su cui il progetto ha pianificato per giorni era quello di un veicolo che non siamo obbligati a usare.

Il gruppo di prima generazione del lotto GB è ora pulito nel verificatore, con Bulbasaur che dichiara tasso di cattura centosessantasette. Gli otto contrassegni residui sono esemplari di seconda generazione letti come di prima per effetto del contenitore sbagliato, e non un difetto nostro: le dimensioni dei file prodotti sono quelle attese e il Mew cromatico del medesimo gruppo, letto come di seconda generazione, è legale.

Tutti e otto i gruppi di evento di prima e seconda generazione hanno ora una provenienza storica con collegamento alla pagina che la descrive, verificata su una seconda fonte indipendente. L'ultimo gruppo senza provenienza è chiuso: erano le uova misteriose dei Pokemon Center di Tokyo e Osaka in tre campagne fra il dicembre 2001 e il maggio 2002, e ciascuna delle quindici voci è attribuita alla propria campagna con il marcatore che la distingue.

## Prossimo passo concreto

Ordinare la coda per specie, cioè aggiungere alla lista di spunta la colonna che dice se una voce da evento sia la prima della propria specie e l'ordinamento che mette prima tutte le prime. È la traduzione operativa della decisione dell'utente e costa poche righe.

Poi completare il giudizio del lotto GB con i due contenitori giusti. Due formule restano trascritte e non verificate sul disassemblato, cioè le statistiche delle prime due generazioni e l'esperienza, e il verificatore è lo strumento che dirà se sono giuste.

Poi, proiettare sulla lista di spunta le fonti che ancora non vi sono proiettate, in ordine di resa: le tremilasettantadue voci di dono delle generazioni moderne, i depositi dei salvataggi di quarta, quinta, sesta e settima generazione, e il deposito di Pokemon Box. Ciascuna è oggi un conto che vive da solo e diventerà una colonna, e le seicentoquaranta voci senza fonte scenderanno di conseguenza. Pokemon Box resta la più interessante per la domanda di completezza, perché il suo caricamento dichiara di contenere tutto ciò che in terza generazione si può ancora ottenere legittimamente; il formato del suo deposito differisce da quello delle cartucce e va letto su `PKHeX.Core/Saves/SAV3RSBox.cs` prima di essere scritto.

Il passo che segue, e che vale di più per la pianificazione, è contare e catalogare gli eventi di quarta, quinta, sesta e settima generazione con il metodo usato per la terza. La base dei doni segreti del verificatore contiene i file per tutte e quattro, cioè `wc4.pkl`, `pgf.pkl`, `wc6.pkl` con il suo complemento e `wc7.pkl` con il suo, quindi non c'è alcun algoritmo da ricostruire: il lavoro è di conteggio, di catalogazione e di misura della campagna.

## Decisioni aperte

Che cosa significhi completo, cioè se la collezione comprenda ogni forma e ogni variante cosmetica oppure una voce per specie. L'utente ha indicato la lettura estesa, e resta da stabilire quali forme il deposito conti come voci separate, che nessuna fonte di primo livello documenta.

Quali titoli recenti acquistare e quando. L'utente non ne possiede alcuno e li compra all'occorrenza; la verifica dice che non sono urgenti, quindi è una decisione di spesa e non di tempo.

Il piano a pagamento del deposito, che l'utente attiverà soltanto quando tutto il resto sarà pronto, e che oggi non è attivo.

## Evidenze e materiale locale

La consegna che ha aperto il sottoprogetto sta in `_notes/fonti/2026-09-01-consegna-pokedex-e-collezione-theslayer.txt`, locale e non versionata. La ricerca dell'utente è conservata verbatim in `pokedex-home-completo/RICERCA-UTENTE-2026-09-01.md`, che è tracciata perché è una fonte con provenienza e non materiale effimero.

La raccolta di salvataggi esterni vive in `_notes/salvataggi/`, con la lista delle provenienze scritta dall'utente in `lista.txt` accanto ai file. Non entra in git per due vincoli indipendenti, cioè l'esclusione di tutto `_notes/` e quella di ogni file con estensione di salvataggio, e ne entra soltanto il censimento generato. La cartella contiene sei salvataggi di terza generazione con il deposito popolato, quattro di prima generazione giapponesi, sei di quarta generazione fra Sinnoh, Platino e Johto, tre di quinta, cinque di Nintendo 3DS fra sesta e settima, un salvataggio di Pokemon Box su GameCube, un esemplare singolo e due archivi di esemplari.

## Aggiunta del 2026-09-04: l'ambito allargato, l'ottenibilità misurata e la terza generazione chiusa

L'utente ha deciso che l'ambito è la totalità degli esemplari da distribuzione esistenti, senza selezione, ed è ADR-031. Da quella decisione l'asse degli eventi nasce ora da tre fonti invece che da due e passa da 2701 a 6244 voci, di cui 3095 sotto scadenza con 433 specie distinte contro le 336 precedenti: il primo tempo della coda, cioè una voce per ciascuna specie, cresce quindi di novantasette voci.

La fonte che mancava sono le tabelle degli incontri del verificatore, ed è emersa da una domanda dell'utente sui biglietti di terza generazione. Là dentro stanno le distribuzioni in cui il dono era un oggetto e l'esemplare è un incontro dentro il gioco, cioè i quattro biglietti più la Tessera Membro, la Lettera di Oak e il Passo Libertà; le periferiche, cioè Pokewalker, Dream Radar e Ranch; i giochi da console fissa, cioè Colosseum e XD; i doni interni condizionati di ottava generazione; e le incursioni da distribuzione di ottava e nona. Erano 422 voci per 256 specie distinte che nessuna delle due fonti precedenti dichiarava, e il difetto era di copertura e non di lettura, quindi non produceva alcun errore e la lista sembrava completa. Lo strumento è `tools/censimento-eventi-tabelle.py` e il documento generato è `CENSIMENTO-EVENTI-FUORI-DONI.md`, che tiene le classi separate perché hanno natura diversa e dichiara in un capitolo proprio ciò che non copre.

L'ottenibilità è misurata ed è ADR-032. `tools/ottenibilita-titoli.py` sostituisce il contrassegno di presenza con l'incontro reale: per ciascuno dei sei titoli a via diretta legge luoghi selvatici, incontri fissi, doni, scambi e incursioni, e chiude l'insieme rispetto alle evoluzioni del titolo nei due versi. L'unione delle ottenibili in gioco è 1021 su 1025 e con le 130 specie dei doni delle generazioni a via diretta arriva a 1025, quindi l'esito resta zero specie vincolate dalla scadenza ma ora è una misura. Il risultato nuovo, che nessuna lettura precedente aveva, è che quattro specie non hanno alcun incontro in alcun gioco moderno, cioè Celebi, Deoxys, Victini e Zarude: non sono vincolate dalla scadenza perché un dono di ottava generazione le consegna, ma non si prendono giocando, quindi stanno sull'asse degli eventi e chi pianificasse di catturarle perderebbe tempo. Il documento è `OTTENIBILITA-TITOLI.md` e dichiara i due versi opposti in cui la misura può sbagliare.

La terza generazione è chiusa sull'asse delle specie. `tools/verifica-salvataggi.py` sa ora leggere il deposito di Pokemon Box, che riconosceva e non apriva, e vi trova 674 posizioni occupate con zero strutture rifiutate. L'unione con i salvataggi della raccolta copre 386 specie su 386: il Box manca di Mew e Deoxys, i salvataggi della sola Poochyena, e nessuna specie manca a entrambi. Le due assenti dal Box sono precisamente quelle dei biglietti, il che è una conferma indipendente, da una fonte che non sa nulla del nostro lavoro, che la classe delle distribuzioni consegnate come oggetto esiste ed è la parte più difficile. Il conto della campagna scende quindi da 640 a 639 voci di specie senza fonte.

Resta aperta una sola domanda su questo track, ed è quella delle forme. Il confronto a macchina fra l'elenco consegnato dall'utente e le 1535 voci di forma che il progetto enumera dà 54 concordi e 9 divergenti, e le divergenze non sono errori ma la domanda in forma precisa: Alcremie ha nove forme nei dati contro sessantatré nell'elenco, perché la decorazione sta in un campo separato dalla crema, e la differenza su quella sola specie vale cinquantaquattro caselle. La risposta non è su una fonte ma nell'applicazione che l'utente possiede, e il materiale atteso è registrato in `pending.md`.
