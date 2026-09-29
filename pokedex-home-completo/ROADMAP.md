# Roadmap cronologica del completamento del deposito

> Documento autorato del 2026-09-08. Nasce da una richiesta esplicita: avere in un posto solo l'ordine in cui le cose vanno fatte, non l'elenco di ciò che è aperto. L'elenco di ciò che è aperto sta in `.claude/memory/pending.md` e non si duplica qui; qui c'è la sequenza, con le dipendenze che la impongono e la dichiarazione di chi esegue ciascun passo.

## Come leggere questo documento

Ogni passo dichiara tre cose che di solito restano implicite e che, restando implicite, fanno perdere tempo. Chi lo esegue, perché alcuni passi sono lavoro di sessione e altri richiedono una persona davanti a una console. Che cosa lo sblocca, perché un passo eseguito prima della sua dipendenza va rifatto. E che cosa il suo esito cambia, perché un passo il cui esito non cambia nulla è un passo che si può rimandare per sempre.

L'ordine non è quello dell'importanza ma quello del rendimento. Un passo che costa poco e che, comunque vada, elimina un'incertezza su cui altri passi poggiano, viene prima di un passo importante e isolato.

## La roadmap al 2026-09-29, che prevale sulle sezioni sotto

Le sezioni che seguono sono la roadmap del 2026-09-08 e restano come storico: dove dicono che un passo è da fare, vale lo stato scritto qui. Alla chiusura di Pokemon Bank, il 26 febbraio 2027 alle 12:00 del fuso giapponese, mancano 150 giorni contati dal 2026-09-29.

Il quadro è cambiato in un punto che decide tutto: la produzione è quasi chiusa e il trasferimento, per quanto il progetto sa, non è cominciato. I lotti su disco sono 2010, tutti conformi al giudizio della libreria del verificatore (ADR-081); la coda del primo tempo, `CODA-PRIMO-TEMPO.md`, conta 433 voci, di cui 333 prodotte e conformi, 60 producibili e verificate, e 40 da periferiche non ancora producibili. La collezione di terza generazione è chiusa su due cartucce (ADR-082, ADR-088). Nella memoria del progetto non risulta alcun esemplare trasferito verso il deposito, cosa da confermare con il proprietario, e il tratto finale, cioè il Trasferitore e la banca su questa console, resta del proprietario e fuori dall'assistenza (ADR-081).

Dei passi del 2026-09-08 sono chiusi A1, perché gli incontri da biglietto sono giudicati conformi, A2 e A3, perché la lettura del corpus è chiusa dal 2026-09-16. Restano aperti B1 e B2 sul servizio ricostruito e sulla barriera coreana, C1 e C3, che sono la stessa coda delle 19 distribuzioni senza carta e delle 14 specie che solo l'archivio conosce (`EVENTI-SENZA-CARTA.md`), C2 sul confronto fra un esemplare ricevuto e il suo gemello, e tutta la fase D del trasferimento.

L'ordine di oggi, per rendimento e per scadenza:

**Passo 0. Le fonti nuove del proprietario.** Annunciate il 2026-09-29. Si ricevono, si registrano in `SOURCES.md` e si passano con gli strumenti del progetto prima di qualunque produzione nuova, perché possono cambiare la strada. Lo eseguono entrambi.

**Passo 1. Le 40 voci da periferiche.** Le eseguo io: 29 dal Pokewalker, 8 da My Pokemon Ranch e 3 dal Dream Radar, con la libreria se i loro incontri sanno costruire un esemplare, poi il giudizio, i lotti in `LOTTI_PER_CODICE` di `tools/checklist-pokedex.py` e la rigenerazione di censimento, checklist, coda e schede. Prima, le pagine del Ranch e del Dream Radar per via d'archivio. Con questo passo la coda del primo tempo è prodotta per intero, salvo ciò che il passo 0 aggiunga.

**Passo 2. Il calendario del trasferimento.** Lo eseguo io, ed è il passo che manca a questa roadmap da quando il collo di bottiglia è diventato il trasferimento. Dai lotti e dai vincoli di `CATENA-DI-TRASFERIMENTO.md` si ricava quante sessioni servono per ciascuna catena, cioè nessuna per la quinta generazione, che si sposta a scatole intere, una ogni sei esemplari per la quarta, due ogni sei per la terza, e quanti giorni costano con i 150 disponibili. Due misure del proprietario lo rendono affidabile: la conferma del Pokédex nazionale sui tre salvataggi di quinta generazione (D1) e il cronometraggio di una sessione del Parco Amici (D2).

**Passo 3. Il trasferimento, nell'ordine della catena più economica.** Lo esegue il proprietario, e io preparo i salvataggi: prima il lotto di quinta generazione, 700 esemplari, poi la quarta, poi la terza. Il tratto dal Trasferitore in poi resta suo.

**Passo 4. Le decisioni che restano, da prendere prima che il calendario le renda impossibili.** Sono del proprietario: le 28 voci coreane (ADR-040), le sei voci bloccate da una macchina nascosta (ADR-046), il Vivillon Motivo Poke Ball dal salvataggio di Y, il profilo di collezione e l'ambito delle sfide del deposito, e la rigenerazione di `SPOGLIO-CORPUS.md` sul corpus cresciuto.

Due fatti di contorno, che non sono passi ma possono cambiarli. La porta di ottobre 2026, cioè Rosso Fuoco e Verde Foglia per Switch collegati al deposito, apre alla terza generazione una via che non dipende dalla banca, e la variante con GB-Link resta da chiudere sul perimetro delle `prod.keys` (`pending.md`). E il Pokédex delle cartucce, che non registra gli esemplari scritti nel deposito, va sanato secondo ADR-089, ma non tocca il deposito di HOME.

## Il quadro: dove siamo il 2026-09-08

Cinque lotti sono prodotti, e il loro stato di giudizio è diverso. La prima e la seconda generazione contano centosessantacinque esemplari con tre difetti corretti dopo il giudizio esterno. La terza generazione conta centosettantadue voci tutte conformi. La quarta conta duecentoquarantasette esemplari, di cui duecentodiciannove conformi e ventotto rifiutati per la barriera di lingua coreana, che non è un difetto dei byte. La quinta conta settecento esemplari tutti conformi. Gli incontri sbloccati dai biglietti contano dieci esemplari prodotti il 2026-09-07 e non ancora giudicati.

Due lotti sono progettati e non prodotti: i sessantadue esemplari delle distribuzioni che non lasciano una carta, e le quattordici specie che soltanto l'archivio enciclopedico conosce.

Il collo di bottiglia non è più la produzione ma il trasferimento, e la catena con i suoi vincoli sta in `CATENA-DI-TRASFERIMENTO.md`.

## Fase A: chiudere ciò che è già in mano, e che nessuno sta aspettando

Questi passi non dipendono da niente e non richiedono nulla che non sia già su disco. Vanno per primi perché ogni giorno che restano aperti è un giorno in cui qualcun altro passo poggia su un'incertezza evitabile.

**A1. Il giudizio esterno sul lotto degli incontri da biglietto.** Lo esegue l'utente, importando `_notes/lotti/lotto-incontri-gen3/` in un salvataggio di terza generazione ed esportando il rapporto sui box. Non dipende da nulla. Il suo esito decide se il ramo del primo metodo sia corretto, e quel ramo servirà di nuovo per ogni esemplare catturato che il progetto vorrà produrre in futuro, quindi l'esito vale oltre le dieci voci. Due cose vanno guardate per prime nel rapporto, perché sono le sole che il generatore non può verificare da sé: che il tipo di correlazione risulti il primo metodo e non nessuna, e che il Mew giapponese non sia contestato sulla lingua.

**A2. La lettura dei tre cluster prioritari del corpus.** La eseguo io. Dipende dalla ripresa della corsa, che è in esecuzione. I tre cluster sono quello sulla chiusura della banca, quello sulle liste trasversali e quello sulla manipolazione del generatore, e l'ordine con la motivazione sta in `pending.md`. Il suo esito è il confronto fra sei enumerazioni indipendenti di ciò che si perde e la nostra, che finora era sola.

**A3. Il completamento del censimento del corpus.** Lo eseguo io. Dipende dalla ripresa. Rigenera `CENSIMENTO-FONTI-COLLEZIONE.md` con i nodi di profondità due e porta in `SOURCES.md` le fonti nuove. Il suo esito è sapere quanto grande sia davvero il corpus, che oggi conosciamo solo al primo livello.

## Fase B: le due misure che decidono la forma del lavoro seguente

Questi due passi costano poco e cambiano il piano a valle. Vanno prima di qualunque produzione nuova.

**B1. Misurare che cosa il canale ricostruito distribuisca.** Lo eseguo io, leggendo il deposito pubblico del codice di quel servizio e il suo canale di conversazione, che sono raggiungibili con gli strumenti che il progetto ha già. Dipende da nulla. La domanda è stretta e va posta così: se il servizio distribuisca doni segreti oltre al sistema di scambio, e se esista un catalogo di ciò che distribuisce. Il suo esito decide se i passi C2 e C3 abbiano senso.

**B2. Verificare se il ponte ricostruito attraversi la barriera di lingua della quarta generazione.** Lo eseguo io, sullo stesso codice. Dipende da B1. Il suo esito decide se i ventotto coreani si risolvano con un servizio già in piedi invece che con una stazione coreana in emulazione, il che cambia il costo di quel sottoproblema di un ordine di grandezza.

## Fase C: la produzione che resta

**C1. I sessantadue esemplari delle distribuzioni senza carta.** Lo eseguo io. Dipende da A2, perché uno dei cluster prioritari contiene enumerazioni di eventi interni ai giochi che potrebbero coprire in parte quella coda. È il lotto più grosso ancora da produrre e attraversa tre generazioni.

**C2. Il confronto fra un esemplare ricevuto e il suo gemello composto.** Lo esegue l'utente sulla console, e io sul file che ne esce. Dipende da B1 e da una decisione di perimetro che è dell'utente. È il passo di maggior valore conoscitivo di tutta la roadmap e la ragione è in ADR-048: un esemplare ricevuto davvero dal gioco è verità di riferimento, e confrontarlo campo per campo con il nostro gemello dice se il modello sia giusto, cosa che nessun verificatore può dire perché il verificatore controlla la conformità a un modello e non il modello.

**C3. Le quattordici specie che soltanto l'archivio enciclopedico conosce.** Lo eseguo io. Dipende da A3, perché il corpus completo potrebbe portarne la documentazione tecnica che oggi manca.

## Fase D: il trasferimento, che è il collo di bottiglia vero

**D1. La conferma del catalogo nazionale sui tre salvataggi di quinta generazione.** Lo esegue l'utente avviando i giochi. Dipende da nulla ed è il presupposto di ogni trasferimento dalla quarta alla quinta. È già accertato dai byte che tutti e tre hanno battuto la Lega; il catalogo nazionale resta da confermare.

**D2. Il cronometraggio di una sessione del Parco Amici.** Lo esegue l'utente. Dipende da nulla. È il solo dato ignoto del tasso di trasferimento dopo che il limite giornaliero è caduto, e senza di esso il calendario della terza generazione non si può stimare.

**D3. L'allestimento della via in emulazione.** Lo eseguono entrambi. Dipende da B2, perché se il ponte ricostruito funziona la stazione coreana non serve più e resta soltanto quella giapponese per il Mew dell'isola lontana. I sei passi stanno in `CATENA-DI-TRASFERIMENTO.md`.

**D4. Il trasferimento del lotto di quinta generazione.** Lo esegue l'utente. Dipende da D1. È il lotto più grosso e il più economico, settecento esemplari senza alcuna sessione a sei, e per questo va per primo fra i trasferimenti; la capienza impone due passaggi con lo svuotamento delle scatole fra l'uno e l'altro.

## Che cosa resta fuori, e perché

Gli esemplari che una macchina nascosta blocca non entrano in questa roadmap e non è una dimenticanza: ADR-046 stabilisce che si conservano come file e si attende una catena che quel vincolo non ce l'abbia. La loro coda va riesaminata quando una catena nuova diventa disponibile, non a una data.

Il Pichu dalle orecchie a punta non entra perché la questione è chiusa in negativo: il Trasferimento lo rifiuta esplicitamente e nessuna via lo porta al deposito.

Le forme di sola battaglia e quelle totemiche non entrano perché sono irraggiungibili sempre e non per scadenza, come registrato il 2026-09-02.
