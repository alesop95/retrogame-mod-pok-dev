# Studio 04: la via del nome di dominio, e un servizio in rete che qualcuno ha rianimato

> Nota di studio del 2026-09-08. Nasce dallo spoglio del corpus di centosettantuno fonti descritto in `SOURCES.md` alla sezione sul corpus della collezione, e riguarda la scoperta che pesa di più fra quelle che il corpus ha portato. Non decide nulla: espone che cosa la via sarebbe, che cosa è verificato e che cosa non lo è, e quali decisioni di questo progetto essa rimetterebbe in discussione.

## Che cosa è stato trovato

Fra i rinvii del post di raccolta stanno due voci che il progetto non conosceva e che descrivono la stessa cosa da due lati. La prima è un articolo redazionale del 2018 che spiega come riaprire i doni segreti nei giochi di quarta e quinta generazione cambiando il nome del server dei nomi sulla console. La seconda è il sito di un servizio non ufficiale che oggi fornisce il sistema di scambio globale, i video delle lotte e altri servizi in rete per quelle stesse due generazioni, e che dichiara di funzionare in combinazione con due progetti di emulazione della connessione senza fili originale.

La sostanza è che i servizi in rete di quei giochi, chiusi nel 2014, sono stati ricostruiti da terzi e sono raggiungibili cambiando un solo parametro sulla console. Ne discendono due capacità distinte, e vanno tenute separate perché hanno peso diverso per questo progetto.

La prima è la consegna dei doni segreti. Un utente che ha percorso la via nel 2020 elenca ciò che ha ricevuto su cinque giochi, ed è un elenco lungo: Jirachi, Celebi, Milotic cromatico, i tre cani cromatici, Pichu cromatico, il Pikachu dell'anime, Crobat, Regigigas, Deoxys, Arceus, tre Manaphy, Weavile, Lucario, Dragonite, quattro Darkrai, Shaymin, e fra gli oggetti la carta di iscrizione, la lettera del professore e il flauto azzurro, che internazionalmente non fu mai distribuito. La consegna è casuale e richiede tentativi ripetuti, e produce duplicati.

La seconda è il sistema di scambio globale, che l'articolo dichiara pienamente funzionante in quarta generazione.

## Perché questa via non è come quelle che stiamo percorrendo

La differenza non è di comodità ma di provenienza, ed è la ragione per cui vale scriverne uno studio invece di una riga.

Tutto ciò che questo progetto ha prodotto finora è composto: un programma scrive i byte di un esemplare secondo il modello che il verificatore impiega per giudicare, e la sua legittimità è una proprietà della somiglianza al modello. La via del nome di dominio non compone nulla. Il gioco riceve una carta vera attraverso il proprio canale di consegna, la riscatta con il proprio codice, e l'esemplare che ne esce è generato dal gioco stesso: la correlazione fra valore di personalità e valori individuali non va imitata perché non è imitata, e nessun campo è scritto da noi.

È lo stesso salto di categoria che separa un esemplare catturato da uno assemblato, e questo progetto lo ha già incontrato dal lato opposto quando ha stabilito, leggendo la guida della comunità sul riconoscimento, che l'unica prova positiva di legittimità è un contrassegno che noi non potremo mai avere. Qui la prova positiva non c'è comunque, ma la cosa da provare cambia: non è più se un file somigli a un esemplare, è se un esemplare vero sia stato ottenuto per una via che il servizio non prevedeva.

## Che cosa è verificato e che cosa no

Va detto con precisione, perché due delle tre fonti sono vecchie e in questo dominio sei anni sono molti.

Verificato da noi il 2026-09-08, leggendo la pagina del servizio nel momento in cui la si scarica: il servizio è vivo. La pagina dichiara i propri contatori aggiornati, cioè settecentottantotto esemplari offerti e ventunmiladuecentosessantadue video di lotte, che sono dati di esercizio e non testo redazionale. L'indirizzo del server dei nomi che pubblica coincide con uno dei tre che le fonti più vecchie indicano.

Non verificato da noi, e va trattato come tale finché qualcuno non lo misura: che quel servizio distribuisca oggi i doni segreti. La sua pagina nomina il sistema di scambio globale, i video delle lotte e servizi generici, e non nomina i doni. La consegna dei doni, nelle fonti più vecchie, viene dai progetti di emulazione generale della connessione e non da questo servizio, che vi si appoggia. Sono due funzioni distinte servite da due strati distinti, e concluderne che chi fornisce l'una fornisca anche l'altra sarebbe esattamente il genere di inferenza che questo progetto marca e non promuove.

Non verificato, e più importante ancora: quali doni siano oggi in distribuzione. L'elenco riportato sopra è la testimonianza di un utente nel 2020, non il catalogo del servizio. Un catalogo che copra le duecentoquarantasette voci di quarta generazione e le settecento di quinta che abbiamo prodotto è molto improbabile, e l'ipotesi ragionevole è che la via copra un sottoinsieme.

## Gli ostacoli pratici, che non sono piccoli

L'ostacolo tecnico principale riguarda la sola quarta generazione ed è l'anzianità della sua radio: quei giochi parlano soltanto con reti senza cifratura o con la cifratura più vecchia, che i punti di accesso moderni non offrono più. La via praticata dalle fonti è un punto di accesso mobile aperto, cioè senza password, il che è una condizione da allestire con cura e per il tempo strettamente necessario. La quinta generazione non ha questo problema perché usa le impostazioni della console.

L'ostacolo di provenienza è la data. Una carta ricevuta oggi scrive nell'esemplare la data di oggi, e per un evento di quinta generazione che si chiuse nel 2013 quella data è precisamente la firma che la comunità usa per riconoscere questa via, come documenta la guida sul riconoscimento già registrata. Non è un difetto nascosto: è visibile a chiunque guardi, ed è il prezzo dichiarato della via. Per la quarta generazione il discorso è diverso e più favorevole, perché quel formato non porta marchio di origine e il deposito ne mostra la data del trasferimento, quindi una data recente non distingue questa via da un trasferimento tardivo legittimo.

L'ostacolo di perimetro non è tecnico e la decisione non è mia. Percorrere questa via significa collegare una console a un servizio non ufficiale che si sostituisce a uno ufficiale dismesso, e ricevere per quella strada contenuti la cui distribuzione era finita. Il progetto ha già una decisione aperta sulla produzione di esemplari, e questa le sta accanto senza coincidervi: là si trattava di scrivere byte, qui di usare un canale ricostruito. Le due vanno decise separatamente perché i fatti che le governano sono diversi.

## Le due decisioni del progetto che questa via rimetterebbe in discussione

La prima riguarda i ventotto esemplari coreani di quarta generazione. ADR-040 ha stabilito che il rifiuto non è un difetto dei nostri byte ma un vincolo storico: i giochi coreani di quarta generazione non si scambiavano direttamente con quelli internazionali, e il solo ponte era il sistema di scambio globale, che era chiuso. Se quel sistema è oggi vivo per la quarta generazione, la premessa su cui poggiava la scelta della stazione coreana in emulazione cambia. Va detto che due condizioni restano da verificare prima di poterlo affermare, cioè che il sistema funzioni davvero fra un gioco coreano e uno internazionale e non solo fra due internazionali, e che esso accetti quelle voci, dato che il ponte rifiutava le uova e gli esemplari con il fiocco classico.

La seconda riguarda l'ordine di produzione. Se una parte dei doni di quarta e quinta generazione si può ricevere invece che comporre, quella parte non va composta, e non per risparmio di lavoro: un esemplare ricevuto dal gioco è migliore di uno composto su ogni dimensione che a questo progetto interessa. La conseguenza operativa è che prima di continuare a comporre conviene sapere che cosa il canale distribuisca, il che è una misura e non una lettura.

## Che cosa fare, in ordine

Il primo passo è misurare che cosa il canale offra oggi, e non costa hardware: il servizio ha un deposito pubblico del proprio codice e un canale di conversazione, entrambi raggiungibili, e il progetto ha già gli strumenti per leggerli. La domanda è stretta e va posta così: se il servizio distribuisca doni segreti oltre al sistema di scambio, e se esista un catalogo di ciò che distribuisce.

Il secondo passo, se il primo è positivo, è confrontare quel catalogo con le nostre due enumerazioni, cioè le duecentoquarantasette voci di quarta e le settecento di quinta, per sapere quante caselle la via coprirebbe. È lavoro da programma e non da lettura, ed è lo stesso confronto già fatto con il foglio di calcolo della comunità.

Il terzo passo è una prova su un solo esemplare, con la quinta generazione perché non richiede il punto di accesso aperto, e con l'esame del risultato nel verificatore di conformità prima di qualunque trasferimento.

Il quarto passo, che riguarda i coreani, è verificare se il sistema di scambio globale ricostruito attraversi davvero la barriera di lingua della quarta generazione. È una domanda a cui il codice del servizio può rispondere, perché quella barriera è una regola del gioco e non del server, e quindi il server la eredita o la ignora a seconda di come è fatto.

Nessuno di questi quattro passi impegna il progetto alla via: il primo e il secondo servono a sapere se valga la pena porsi la domanda di perimetro, che è la sola che non si risolve misurando.
