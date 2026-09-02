# Studio 04: il tracciatore, e la campagna di trasferimento entro il 26 febbraio 2027

Questa nota nasce da tre domande dell'utente poste insieme, e conviene tenerle insieme perché la risposta alla terza dipende dalle prime due: che cosa sia il tracciatore di Pokemon Home, se lo si possa scrivere da sé, e se il problema sia risolvibile dato che il piano è iniettare molti esemplari in salvataggi e farli passare da Pokemon Bank prima della chiusura, avendo a disposizione una console modificata.

Va detto in apertura ciò che le note precedenti non dicevano con chiarezza sufficiente, perché una loro lettura affrettata scoraggia dal piano giusto. Il tracciatore non è un ostacolo per il piano dell'utente. È un ostacolo per una cosa diversa, che il piano dell'utente non fa.

## 1. Che cos'è il tracciatore

È un identificativo che Pokemon Home assegna a un esemplare nel momento in cui esso tocca il servizio per la prima volta, sia che vi arrivi per trasferimento sia che provenga dal gioco per dispositivo mobile. Le due fonti indipendenti lette il 2026-09-01 lo descrivono nei medesimi termini: assegnato una volta, non cambia più, e segue quell'esemplare attraverso tutti i giochi in cui esso passerà, indipendentemente da qualunque modifica successiva.

Sul piano del formato è un campo che nelle strutture delle generazioni recenti esiste e in quelle antiche no: una struttura di terza generazione non ha alcun posto dove metterlo, e il campo compare quando la struttura viene convertita nel formato di una generazione che lo prevede. È la ragione per cui il verificatore, leggendo il nostro esemplare nel contesto di un titolo della nona generazione, ne ha dichiarato l'assenza: la conversione aveva creato il campo, e il campo era vuoto.

Il servizio lo impiega per tre cose dichiarate: distinguere gli esemplari individuali, rilevare i caricamenti duplicati provenienti da più account, e ricostruire lo stato di un esemplare gioco per gioco quando esso si sposta fra titoli.

## 2. Perché non si può scriverlo da sé, e perché è una impossibilità di natura diversa dalle altre

La domanda se lo si possa scrivere ha una risposta negativa, e la ragione va capita perché non somiglia a nessuna delle altre impossibilità che questo progetto ha incontrato.

Tutti gli altri campi di un esemplare sono calcolabili. Il checksum è una somma che si ricalcola; il valore di personalità è una parola che si compone; i valori individuali si impaccano cinque bit per volta; natura, sesso, abilità e lucentezza discendono per formula dal valore di personalità. Per ciascuno di essi esiste una regola, e chi conosce la regola può soddisfarla: è precisamente ciò che il generatore di questo progetto fa, e il verificatore esterno lo ha confermato campo per campo.

Il tracciatore non ha una regola da soddisfare. Non è un valore derivato dai dati dell'esemplare e non è verificabile da chi lo legge: è una chiave che rimanda a un archivio che sta presso il servizio, e il servizio la valuta cercandola nel proprio archivio e confrontando ciò che vi trova con l'esemplare che ha davanti. Le fonti lo dicono nella forma più utile: un identificativo scritto a mano viene rilevato come falso perché il servizio non lo ha mai emesso, e non perché sia mal formato.

Ne segue la formulazione che il progetto adotta e che vale ripetere ogni volta che la domanda si ripresenta. Non si tratta di un calcolo che non sappiamo fare, ma di una consultazione che non possiamo fare: non esiste alcun algoritmo da scoprire, perché non c'è un algoritmo, c'è una base di dati che non possediamo. Un campo così non si falsifica per definizione e non per difficoltà, e nessun progresso tecnico lo rende falsificabile.

Il verso opposto, che nessuna delle due fonti enunciava e che il giudizio del verificatore ha reso visibile, completa il quadro: non lo si può nemmeno lasciare in bianco dove il contesto lo attende, perché la sua assenza è essa stessa un'obiezione.

## 3. Perché tutto questo non riguarda il piano dell'utente

Qui sta il punto che le note precedenti lasciavano implicito e che va scritto per esteso.

Il tracciatore lo assegna Home, e lo assegna a qualunque esemplare che entri per una via che Home riconosce. Il piano dell'utente è precisamente quello: iniettare gli esemplari in salvataggi di giochi che appartengono alla catena, percorrere la catena ufficiale, e depositarli in Home attraverso Pokemon Bank. In quel momento Home assegna il tracciatore, come lo assegna a qualunque altro esemplare che arrivi da Bank. Non c'è nulla da falsificare, perché non c'è nulla da aggirare: la porta è quella vera.

Il caso in cui il tracciatore è un ostacolo è un altro, e va tenuto distinto perché è quello che il turno precedente aveva esaminato: scrivere un esemplare di terza generazione direttamente dentro un salvataggio della nona generazione. Là il tracciatore serve perché in quel posto un esemplare della terza generazione non può essere arrivato senza essere transitato da Home, e non essendovi transitato non ce l'ha. Quella non è una via che scade: è una via che non esiste, e nessuno la percorre nel piano dell'utente.

La risposta alla terza domanda è dunque affermativa. Il problema è risolvibile, la via è quella ufficiale, e il tracciatore non è la difficoltà. Le difficoltà sono altre due, e sono il resto di questa nota: la coerenza degli esemplari, e il tempo.

## 4. Che cosa controlla ciascun anello, e perché la coerenza è l'unica cosa che conta

La catena non è un tubo trasparente: ogni anello applica i propri controlli, e un esemplare incoerente viene fermato là dove il controllo lo rileva e non alla fine. Ne segue che l'unico lavoro che paga è produrre esemplari coerenti, e che verificarli prima costa infinitamente meno che scoprire a metà catena che non passano.

Il progetto ha già gli strumenti per questo, e il 2026-09-01 li ha visti funzionare. Il generatore compone l'esemplare dalle formule verificate e dichiara la provenienza di ogni campo; il verificatore esterno giudica il risultato e, sul nostro primo caso, ha contestato un campo solo, quello che il rapporto di provenienza segnalava già come contraddittorio nella fonte. La procedura è quindi stabilita: si genera, si verifica, si corregge ciò che il verificatore contesta, si registra la correzione con la sua autorità, e soltanto allora si inietta.

Vale ricordare che il verificatore va interrogato nel contesto della generazione giusta. Il primo giudizio è stato dato nel contesto di un titolo della nona generazione, e tre delle sue voci dipendevano da quel contesto invece che dall'esemplare: verificare un esemplare di terza generazione nel contesto della terza generazione non è un dettaglio di comodità ma la condizione perché il giudizio significhi qualcosa.

## 5. Dove iniettare, e la decisione che ne dipende

La catena ha quattro tratti e quindi quattro punti in cui si potrebbe entrare, e la scelta non è indifferente perché determina quanto lavoro manuale resta.

Entrare in terza generazione significa percorrere tutto: il parco di migrazione verso la quarta, che impone sei esemplari per volta e pretende la medesima lingua ai due capi, il trasferimento senza fili verso la quinta, che richiede due apparecchi accesi insieme, poi il programma di trasferimento, poi il servizio di deposito. È il percorso più lungo e quello che produce il dato più simile a un dato reale, perché ogni trasformazione la compie il gioco.

Entrare in quinta generazione significa saltare i due passaggi interni e restare con il solo tratto finale, cioè il programma di trasferimento e poi il servizio di deposito. È il percorso più corto, e la questione che apre è se il dato che ne risulta sia il medesimo. Le trasformazioni dei due passaggi interni sono deterministiche, e l'editor della comunità le implementa quando converte una struttura da un formato a un altro: la conversione dovrebbe quindi produrre ciò che la catena avrebbe prodotto. Il verbo dovrebbe va conservato, perché il progetto non lo ha verificato, e la verifica è possibile e costa poco: si prende un esemplare reale che abbia percorso la catena, si prende la conversione del medesimo esemplare fatta dall'editor, e si confrontano i byte.

La decisione fra i due percorsi è dell'utente e dipende dal tempo, che è la sezione seguente. Ciò che il progetto può dire è il criterio: il percorso lungo costa tempo e non pone domande, il percorso corto costa una verifica e le pone tutte in un punto solo. Con centosettantotto giorni e molti esemplari, il percorso corto è quello che va verificato per primo, perché se regge cambia l'ordine di grandezza del lavoro.

Va aggiunto un vincolo che nessuno dei due percorsi elimina e che va conosciuto prima di pianificare: il trasferimento dal servizio di deposito verso Home richiede il piano a pagamento di Home, mentre il servizio in chiusura è gratuito, e il piano gratuito di Home conserva trenta esemplari. Una catena completata fino al servizio in chiusura non è una collezione al sicuro.

## 6. Il tempo, contato

La chiusura è il 26 febbraio 2027 alle dodici del fuso giapponese. Misurato il 2026-09-01, il tempo residuo è di centosettantotto giorni.

Va scritto così, cioè come conteggio a una data e non come durata, perché una durata invecchia in silenzio e nessuno la ricalcola. Il progetto lo ha appena imparato nel modo peggiore: tre file tracciati dichiaravano diciotto mesi, e diciotto mesi era sbagliato per un fattore tre nel verso che rassicura. La correzione non è di margine ma di piano, perché sei mesi impongono di scegliere ciò che diciotto avrebbero permesso di completare.

Su quanto ci sia da fare il progetto ha una cifra e non l'ha verificata: l'autore degli strumenti della comunità dichiara in quattrocento gli esemplari da distribuzione di cui tenere traccia, e accompagna la cifra con l'osservazione che non si finisce prima della chiusura. La cifra è di quinto livello e la conseguenza non dipende dalla sua esattezza: l'insieme completo non è raggiungibile nel tempo residuo, quindi una selezione è necessaria.

Ne discende la sola raccomandazione di questa nota, e riguarda l'ordine e non la quantità. Ciò che ha una scadenza va prima di ciò che non l'ha. Gli esemplari che possono raggiungere Home soltanto attraverso il servizio in chiusura sono quelli della prima, della seconda, della quarta e della quinta generazione, e per essi il 26 febbraio 2027 è assoluto. Gli esemplari di terza generazione hanno una seconda porta, che si apre a ottobre 2026 e non dipende da Bank: pianificare come se non esistesse è prudente, ma spendere i centosettantotto giorni su di essi mentre le altre quattro generazioni aspettano sarebbe spendere il tempo scarso sulla sola generazione che ne ha anche un altro.

## 7. Che cosa il progetto sa generare, e che cosa no

La domanda va risposta separando tre cose che il piano tiene insieme, perché su una di esse la risposta è negativa e conviene saperlo prima di contarci.

### Gli esemplari da evento della terza generazione: si

Il progetto li genera e la generazione è verificata. Il modulo `pokebridge/eventi.py` porta le formule che dal seme producono il valore di personalità, i sei valori individuali e il sesso dell'allenatore di provenienza; `pokebridge/gen3.py` compone la struttura, la cifra, la permuta, ne calcola il checksum e la scrive nelle due forme di scambio; `tools/genera-evento-gen3.py` mette insieme le due cose con i metadati dell'evento e dichiara la provenienza di ciascun campo. Il verificatore esterno ha giudicato il risultato e, dopo la correzione di un campo, dichiara validi uno per uno tutti i campi enumerabili.

Va precisato un punto che l'espressione generare un evento nasconde. Il generatore parte da un seme, e il seme non deve essere quello storico dell'esemplare che qualcuno ricevette nel 2006: poiché il metodo restringe il seme a sedici bit, qualunque valore in quello spazio produce un esemplare coerente, e la coerenza è tutto ciò che un verificatore misura. Il seme storico serve a una cosa diversa e più ristretta, cioè riprodurre un esemplare specifico che qualcuno possiede, e su quel caso il progetto ha lo strumento inverso, che dal valore di personalità e dai valori individuali ricava il seme.

### Qualunque altro esemplare: no, e conviene non implementarlo

Il generatore è specifico degli eventi, e non è una limitazione temporanea. Un esemplare non da evento nasce per un metodo diverso, con altre relazioni fra le estrazioni, e la sua conformità dipende da cose che un evento non ha: la casella di incontro del luogo dichiarato, il livello ammesso in quel luogo, la compatibilità della sequenza di mosse con il livello, e nel caso delle uova un insieme di regole proprio. Implementare tutto questo sarebbe riscrivere il verificatore, che esiste, è mantenuto, e per di più è l'autorità con cui misuriamo noi stessi.

Va aggiunto che quel lavoro non servirebbe all'obiettivo. Gli esemplari ordinari si ottengono giocando, oppure per le generazioni recenti dai servizi documentati nell'altro track; la gamba che nessuna via ordinaria copre è quella degli eventi, ed è esattamente quella che il progetto ha coperto.

### Metterli dentro un salvataggio: si, ma non con il nostro codice

Il progetto produce l'esemplare e non il salvataggio che lo contiene: lo strato del salvataggio da centoventotto kibibyte, cioè la sezione 6 della referenza, non è scritto ed è il prossimo passo tecnico dichiarato del track del ponte. Operativamente la cosa non blocca nulla, perché l'editor della comunità apre un salvataggio, accetta un esemplare in una scatola e lo riscrive: la scrittura nel salvataggio è quindi coperta da uno strumento esistente, e duplicarla sarebbe lavoro sprecato.

Ciò che manca per arrivare alla cartuccia non è software ma il lettore, che deve ancora arrivare. Fino a quel momento la catena è percorribile sui salvataggi e non sull'hardware.

## 8. La via di produzione in volume, che non è il nostro generatore

Questa sezione corregge un'aspettativa che il resto della nota potrebbe indurre, e va scritta perché cambia il piano nel verso di renderlo praticabile.

Il nostro generatore compone un esemplare per volta a partire da un evento presente nel corpus del costruttore della comunità, e quel corpus contiene diciassette eventi. Il catalogo che il progetto genera dalla tabella del verificatore ne contiene centosettantasette. La differenza non è un difetto del corpus, che dichiara di raccogliere gli esemplari conservati e non tutti gli eventi esistiti, ma segna il limite della nostra via di produzione: per centosessanta eventi il progetto conosce metodo, allenatore, identificativo, livello e mosse dal proprio catalogo, e non ha un corpus da cui partire.

Questa sezione portava una affermazione sbagliata per poche ore, e la correzione insegna quanto costi poco verificare. Avevo scritto che il verificatore esponesse la medesima tabella come propria base di dati dei doni segreti, e che quella fosse la via di produzione in volume. L'esportazione integrale di quella base, fatta il medesimo giorno, contiene ottocentosettantuno file e nessuno di terza generazione: la ragione la conoscevamo già, cioè che quella generazione non ha mai avuto un formato binario uniforme per i doni e che la sua tabella vive nel codice, come il commento della tabella dichiara e come il nostro catalogo riporta. Bastava rileggere il nostro documento prima di affermare.

La via di produzione in volume per la terza generazione è quindi il nostro generatore, e dal 2026-09-01 esso legge direttamente la tabella del verificatore invece del corpus del costruttore. La copertura passa da diciassette eventi a centosettantatré voci su centosettantasette, e le quattro che restano fuori impiegano una forma del costruttore che il lettore non copre e appartengono all'insieme giapponese. Il guadagno non è soltanto di numero: la tabella è l'autorità su campi che il corpus dichiarava male, e il contrassegno dell'incontro fatidico ne è l'esempio migliore, perché la tabella lo dichiara su trentuno voci su centosettantasette e non sulla nostra. La correzione che avevamo registrato sulla scorta del giudizio del verificatore passa così da constatazione empirica a lettura di fonte, che è un grado di prova superiore.

Dalla medesima tabella viene anche la risposta a una domanda che io stesso avevo posto male. Avevo proposto di generare l'esemplare dichiarando come gioco di origine uno dei due titoli della riedizione, per rimuovere l'incognita sulla porta di ottobre. La tabella lo esclude: tutte e cinquanta le voci di quell'evento dichiarano Rubino, e un esemplare che dichiarasse un titolo diverso porterebbe una combinazione che la tabella non prevede. L'incognita non si rimuove scegliendo il campo, e resta quella che gli studi registrano, cioè se il servizio accetti un esemplare di provenienza dichiarata Rubino che si trovi in un salvataggio della riedizione. Il criterio generale che avevo enunciato resta valido dove un campo non è vincolato dalla fonte; qui era vincolato e non lo avevo verificato.

Il collegamento fra la tabella e la composizione ha prodotto una verifica che non era stata cercata e che vale più di entrambe le fonti. Il medesimo esemplare, cioè il Pikachu del blocco italiano del decennale dal seme 0x00009DF6, è stato composto due volte: una dai metadati del corpus del costruttore, con la correzione del contrassegno fatidico applicata sulla scorta del giudizio del verificatore, e una dai metadati della tabella del verificatore. I due file risultano identici byte per byte, tutti e ottanta.

Va detto perché questo conta più di una coincidenza. Le due fonti sono indipendenti: una è un corpus curato a mano da una comunità che raccoglie esemplari conservati, l'altra è la tabella di legalità di una implementazione di riferimento, e i loro campi sono organizzati in modo diverso, con numerazioni di specie diverse e un contrassegno dichiarato in modo opposto. Che la composizione converga sui medesimi ottanta byte significa che i due percorsi di lettura, la conversione fra le numerazioni, la correzione registrata e le formule sono tutti corretti insieme: un errore in uno qualunque di essi avrebbe prodotto una differenza. È la forma più economica di verifica che il progetto abbia ottenuto, perché non ha richiesto alcuna autorità esterna ma soltanto due strade per lo stesso punto.

L'esportazione, però, ha prodotto un valore maggiore di quello cercato, e riguarda le generazioni che hanno una porta sola. Ottocentosettantuno carte di dono dalla quarta alla nona generazione sono materiale della campagna: una carta iniettata in un salvataggio di quarta o quinta generazione si riscatta dentro il gioco, e l'esemplare lo genera il gioco. È la medesima logica per cui la ricreazione della distribuzione di terza generazione è coerente per costruzione anziché rispetto ai controlli noti, e su quarta e quinta generazione è la via più fedele che esista: non si costruisce un esemplare, si consegna al gioco il dono che lo produceva.

Va detto allora a che cosa serve il lavoro di questo progetto, perché la conclusione precedente potrebbe farlo sembrare superfluo e non lo è. Esso serve a tre cose che quella via non dà. La prima è la comprensione: le formule sono scritte, svolte bit per bit e verificate, quindi il progetto sa perché un esemplare è conforme invece di constatare che lo è. La seconda è la verifica incrociata: due implementazioni indipendenti che concordano valgono più di una, e il confronto ha trovato due difetti reali nel costruttore della comunità proprio perché esisteva un secondo punto di vista. La terza è la ricerca inversa: dato un esemplare autentico posseduto, il progetto ne ricava il seme, e quello è l'unico modo di stabilire che una ricreazione sia fedele a un originale e non soltanto conforme a una tabella. Quando il lettore arriverà e gli esemplari del decennale saranno estratti dalla cartuccia, sarà quello lo strumento che conta.

La divisione del lavoro è dunque questa: la produzione in volume la fa il verificatore dalla propria base di dati, la comprensione e la verifica le fa il progetto, e il confronto fra le due vie resta disponibile ogni volta che un esemplare vale la pena di essere guardato due volte.

## 9. I salvataggi procurati dal web, e la distinzione che riduce la questione

La richiesta di cominciare a impiegare salvataggi trovati in rete è arrivata il 2026-09-01, e la regola sull'hardware prescrive che il fatto sia esposto una volta e che la decisione, se presa, sia registrata come ADR invece di scivolare dentro un altro lavoro. Questa sezione fa la prima cosa; la seconda spetta all'utente.

Il fatto, nei suoi termini e senza attenuarlo. La regola dice che i salvataggi scaricati da internet non si importano su questa console, e la motivazione scritta è che sono la causa principale delle sanzioni quando poi vengono impiegati in linea o depositati, e che il rischio ricade sull'account e sulla console e non sul file. Quella motivazione non è cambiata.

Esiste però una distinzione che nessuna sezione precedente aveva enunciato e che riduce la questione invece di aggirarla, perché separa due usi che la parola importare confonde.

Il primo uso è leggere. Un salvataggio scaricato si apre sul calcolatore con l'editor della comunità e se ne guardano i campi: nulla tocca la console, nulla tocca l'account, e nessun esemplare di provenienza altrui entra in alcuna cartuccia. Il valore di quest'uso è concreto e riguarda proprio la gamba che il progetto persegue: gli archivi di conservazione della comunità contengono esemplari da evento con i loro campi autentici, e per i centosessanta eventi che il nostro catalogo elenca senza avere un corpus da cui partire, un archivio letto è la sola fonte dei valori storici. Da un esemplare letto il progetto ricava il seme con la ricerca inversa, e da quel seme rigenera l'esemplare con il proprio codice: ciò che entra nel salvataggio proprio è allora un esemplare prodotto qui, non un esemplare altrui.

Il secondo uso è importare, cioè portare il salvataggio altrui, o gli esemplari che contiene, dentro una cartuccia propria o sulla console, e da la nella catena. È questo l'uso che la regola esclude, ed è quello a cui la motivazione della regola si applica.

Ne segue una osservazione che il progetto può fare e una decisione che non può prendere. L'osservazione è che il primo uso dà quasi tutto il valore del secondo senza il suo rischio, perché ciò che il progetto ha bisogno di procurarsi non sono salvataggi ma valori di campo, e i valori di campo si leggono. La decisione è se il secondo uso sia dentro il perimetro, resta aperta in `pending.md` dal 2026-08-28, e non viene presa qui.

Va aggiunta una precisazione sulla natura delle fonti, perché la parola scaricato copre cose diverse e la differenza è di merito e non di forma. Un archivio di conservazione mantenuto da un progetto della comunità, che il registro delle fonti di questo lavoro elenca già fra le implementazioni di riferimento, e un salvataggio anonimo trovato in un forum non hanno la medesima provenienza ne la medesima verificabilità. La regola come è scritta non distingue i due casi, e se la decisione dovesse riaprirla la distinzione va scritta nell'ADR invece di essere applicata in silenzio.

### Un salvataggio procurato si impiega come veicolo e non come carico

ADR-024 distingue leggere da importare. Un caso pratico ne aggiunge un terzo che le due parole non coprono, e va enunciato perché è quello che la campagna impiegherà di più.

Un salvataggio completo di un titolo della quinta generazione porta con sé due cose distinte: uno stato di avanzamento, cioè i contrassegni che sbloccano il Dono Segreto e il trasferimento senza fili, e un contenuto, cioè gli esemplari nelle sue scatole. Il valore sta interamente nel primo. Il trasferimento verso la quinta generazione richiede il laboratorio che si apre dopo la vicenda principale, e un salvataggio completo lo ha: significa non dover giocare decine di ore per aprire una porta.

Il contenuto invece non serve e va trattato come non desiderato. Gli esemplari che quel salvataggio contiene sono di provenienza altrui e ignota, e per ADR-024 nessuno di essi entra nella catena senza essere passato dal verificatore. La via più semplice non è verificarli ma non impiegarli: si svuotano le scatole, oppure si ignorano, e vi si mettono soltanto gli esemplari prodotti qui o generati dal gioco riscattando una carta di dono. Il salvataggio è allora un veicolo con le porte già aperte, e ciò che viaggia dentro è nostro.

Ne discende un passo che va fatto prima di qualunque altra cosa su un salvataggio procurato, e che l'editor compie in un momento: sostituire i dati dell'allenatore con i propri, cioè nome, identificativo, identificativo segreto e sesso. La ragione non è estetica. Gli esemplari che si ottengono dentro un salvataggio ereditano l'allenatore di quel salvataggio dove l'evento non ne fissi uno proprio, e senza quella sostituzione una parte della collezione porterebbe per sempre il nome di uno sconosciuto. Con la sostituzione fatta, il veicolo ha la nostra identità e ciò che vi si ottiene è nostro anche nei campi.

Va aggiunta l'avvertenza che discende dal resto di questa nota, e non è un'obiezione ma un dato di pianificazione: gli esemplari già presenti in un salvataggio procurato non hanno mai toccato il deposito, quindi non hanno tracciatore, e portarli avanti nella catena li esporrebbe al medesimo esame di qualunque esemplare costruito. Lasciarli dove sono costa nulla e rimuove la questione.

## 10. Lo stato della produzione, e i limiti che restano nominati uno per uno

Questa sezione è l'inventario di ciò che il progetto sa produrre oggi e di ciò che non sa, con la ragione di ciascuna mancanza. Serve a due cose: sapere quanti esemplari esistono senza contarli, e sapere quale lavoro comprerebbe quanti esemplari.

### Che cosa è stato chiuso il 2026-09-01

Tre limiti sono stati chiusi insieme perché avevano la medesima causa, cioè che il modulo sapeva una derivazione sola e non sapeva verificare ciò che produceva.

Le derivazioni del sesso dell'allenatore sono passate da una a nove, e non sono congetturate: vengono dal codice della implementazione di riferimento, che il clone locale contiene e che le raccoglie in un punto solo. Due di esse hanno una particolarità che una riscrittura più ordinata perderebbe, e le prove la fissano: quella a scorrimento di sette restituisce femmina quando il bit vale zero, cioè porta una negazione che le altre non hanno, e quella a scorrimento di quindici legge la sesta estrazione e non la quinta, perché fra i valori individuali e il sesso si consuma l'oggetto tenuto. Resta fuori la sola derivazione che la fonte stessa dichiara di non verificare con la logica ordinaria, e il modulo si rifiuta invece di scrivere un valore inventato.

La verifica della lucentezza chiude un difetto latente e non una lacuna, e va detto per quello che era. Il generatore scegliva un seme e non controllava che l'esemplare risultante avesse la lucentezza che l'evento dichiara. Su un evento a lucentezza negata, che nel catalogo sono la maggioranza, un seme sfortunato avrebbe prodotto un esemplare cromatico, cioè un esemplare che nessun verificatore accetta, e nulla lo avrebbe segnalato: il primo caso di prova non era cromatico per caso e non per controllo. Adesso il vincolo si verifica.

La scelta del seme è automatica. Prima si passava a mano, che per un esemplare va bene e per centosettantatre è il motivo per cui la produzione in serie non esisteva. La restrizione a sedici bit rende la ricerca esauribile, quindi il seme si cerca fra i sessantacinquemilacinquecentotrentasei ammessi verificando i vincoli, e la ricerca riparte da dove si è fermata la volta precedente, cosicché due esemplari del medesimo evento non ricevano il medesimo valore di personalità e non siano un duplicato riconoscibile.

### Che cosa il lotto produce, in numeri

Sulla tabella intera, centoventidue esemplari prodotti e cinquantuno non producibili. Il numero è stato centoquattro contro sessantanove per una giornata, e la sezione seguente dice che cosa lo ha mosso e a quale prezzo. Il programma non produce nulla per le voci che non sa fare, e le elenca con la ragione: un generatore che produca qualcosa per ogni voce è peggio di uno che si rifiuti, perché un esemplare sbagliato in mezzo a centosettanta giusti non si trova guardando.

Delle cinquantuno che restano, cinquanta sono uova e una impiega un generatore pseudocasuale diverso. Non c'è più nessuna voce bloccata dal metodo di generazione né dalla codifica dei caratteri, e non c'è più nessuna voce bloccata dall'allenatore di destinazione, che si passa al programma quando serve.

### Le due stime di costo che erano sbagliate, e in quale direzione

La versione precedente di questa sezione conteneva due valutazioni di costo che il lavoro ha smentito, e in direzioni opposte. Vale registrarle entrambe, perché una stima sbagliata verso il basso e una sbagliata verso l'alto insegnano cose diverse.

La prima diceva che quindici voci differivano dal nostro metodo per un semplice scostamento e che erano il lavoro più redditizio, perché il codice sarebbe stato il medesimo con un parametro in più. Era sbagliata verso il basso: undici di quelle quindici richiedevano anche la tabella dei doni, e la stima l'aveva contata come un ritardo di due estrazioni quando invece era una funzione da scrivere. Nel momento in cui il difetto è stato riconosciuto la stima corretta era che soltanto cinque voci fossero a costo quasi nullo, e non quindici.

La seconda diceva che venticinque voci impiegavano il metodo ordinario delle uova, che è un algoritmo diverso e non uno scostamento. Era sbagliata verso l'alto: quel metodo è la composizione ordinaria, cioè quella degli incontri non da evento, seguita da una sola estrazione consumata e non usata, ed è il più semplice dei quattro rami. Ciò che quelle venticinque voci hanno di difficile non è il generatore ma il fatto di essere uova, che è un'altra cosa e sta in un altro campo.

Il rimedio a entrambe è stato lo stesso ed è il metodo che questo progetto già conosceva: nessuna delle due stime veniva dal codice della fonte, venivano dai nomi dei metodi nella sua tabella. Un nome è una etichetta di catalogazione, non una specifica.

### I limiti che restano, con il loro costo

Cinquanta voci sono uova, e per esse il generatore pseudocasuale è pronto e provato. Ciò che manca è un dato per specie, cioè il conto delle incubazioni, che nell'uovo occupa il campo dell'amicizia e che un verificatore controlla; con esso vanno il soprannome e la lingua, che nell'uovo non si scelgono ma sono imposti dalla sua condizione. È il lavoro singolo più redditizio che resti su tutto questo fronte, perché un dato solo vale cinquanta esemplari, e il posto dove si trova è il campo delle incubazioni nella tabella delle statistiche di base del disassemblato.

Una voce sola impiega un generatore pseudocasuale differente, quello dei titoli per la console domestica, e per essa vale ciò che la sezione precedente dice: la via di produzione in volume non è obbligata a essere la nostra.

Va detto che nessuno di questi limiti blocca la campagna. Il progetto produce ciò che sa produrre e sa dire che cosa non sa, che è esattamente la condizione per decidere se valga la pena scrivere il resto oppure impiegare per quelle voci lo strumento di terzi.

## 11. Che cosa resta da fare, in ordine

Verificare l'esemplare di prova nel contesto della terza generazione, che è la condizione perché il giudizio significhi qualcosa e che costa una operazione.

Verificare se la conversione dell'editor fra i formati produca ciò che la catena produce, perché da quella risposta dipende l'ordine di grandezza del lavoro. Si fa confrontando i byte di un esemplare reale che ha percorso la catena con quelli della conversione del medesimo esemplare, e non richiede alcun hardware oltre a un salvataggio reale.

Decidere la selezione, cioè quali esemplari perseguire nei centosettantotto giorni. È una decisione dell'utente e non del progetto, e la nota le fornisce il criterio dell'ordine: prima ciò che ha una sola porta.

Registrare la decisione di perimetro che resta aperta, perché tutto questo la presuppone e nessuna sezione di questa nota la prende. L'iniezione di esemplari costruiti dentro salvataggi propri, e il loro deposito in un servizio in linea, ricade nella politica sui dati alterati che gli studi dell'altro track riportano: la valutazione corrente delle fonti è che un esemplare coerente sia accettato, con la clausola, ripetuta da due fonti indipendenti, che questo potrebbe cambiare. Il tracciatore rende quella clausola pesante, perché ciò che entra resta identificabile.
## 12. Il Pokedex completo, e perché la scadenza non vincola tutto

L'obiettivo dichiarato del progetto è avere in Pokemon Home ogni specie, più copie autentiche degli esemplari di terza generazione che l'utente possedeva. Fin qui il lavoro ha riguardato la seconda metà. Questa sezione riquadra la prima, e la riquadratura cambia il piano, perché la lettura ingenua del vincolo di tempo è sbagliata in un modo che costa lavoro inutile.

### La scadenza si applica a un sottoinsieme, non alla collezione

Il deposito in rete accetta esemplari per due vie con proprietà temporali opposte. La prima è diretta e non ha scadenza: i titoli dell'ottava e della nona generazione, e le riedizioni che vi si collegano, versano in Home senza passare da alcun servizio in dismissione. La seconda passa per la banca e cessa il 26 febbraio 2027, cioè fra centosettantasette giorni contati dal 2026-09-02.

Ne segue che il vincolo di tempo non riguarda la collezione ma soltanto ciò che non ha una via della prima specie. Una specie ottenibile in un titolo dell'ottava o della nona generazione si può portare in Home dopo la chiusura della banca, con tutta la calma che serve, per sempre. Spendere le settimane che restano su quelle specie sarebbe spendere una risorsa scarsa su un problema che non ha scadenza, ed è esattamente l'errore che una lettura affrettata del vincolo produce.

### Le tre categorie che la scadenza vincola davvero

Dentro l'insieme urgente stanno tre cose diverse, e distinguerle serve perché hanno rimedi diversi e priorità diverse.

La prima è l'insieme delle specie e delle forme che nessun titolo dell'ottava o della nona generazione produce. Per esse la banca è la sola porta, quindi la loro finestra si chiude e non si riapre. L'enumerazione di questo insieme è il lavoro che il Pokedex completo deve fare, e non è deducibile: richiede la disponibilità per specie e per gioco, che è un dato.

La seconda è l'insieme degli esemplari la cui identità richiede una provenienza antica anche quando la specie è disponibile dopo, e questa è la categoria su cui il progetto ha lavorato fin qui. Un Charizard si ottiene nella nona generazione; il Charizard della distribuzione del decennale no, e nessuna via moderna lo produce, perché ciò che lo distingue non è la specie ma l'allenatore, l'identificativo, il luogo di incontro e il contrassegno dell'incontro fatidico. Vale la medesima cosa, e con più forza, per gli esemplari che l'utente possiede su cartuccia: la specie è sostituibile, quell'esemplare no.

La terza è l'insieme delle forme e delle varianti che dipendono da un dato che le vie moderne non riproducono. Il progetto ne ha una in sospeso da prima, registrata nella sezione 10 di questa nota come punto di dominio non verificato, e riguarda una specie della terza generazione i cui disegni sul manto discendono dal valore di personalità: se l'affermazione è vera, una collezione che voglia comprendere una configurazione determinata di quei disegni ha una scadenza, mentre una che si accontenti di un esemplare qualunque della specie non ne ha. La distinzione fra le due letture della parola completa non è verbale e va sciolta prima di pianificare.

### La priorità che ne discende

L'ordine è dunque il seguente, e non è quello che l'obiettivo suggerisce a prima vista. Prima la seconda categoria, perché è irrimediabile e perché la sua macchina esiste già, cioè il generatore e la catena su hardware posseduto. Poi la prima, perché richiede un dato da procurare prima di poter agire. La terza si scioglie dove si incontra, ed è anzitutto una questione di definizione dell'obiettivo e non di lavoro tecnico.

### Il dato che manca, e la fonte che non lo dà nella forma che serve

La disponibilità per specie e per gioco non è nel progetto, e la fonte che il progetto già clona non la offre in forma leggibile a basso costo. L'implementazione di riferimento porta duecento file di dati di legittimità, che coprono incontri selvatici, incontri fissi e doni per ogni generazione, ma li tiene in un formato binario compresso proprio, con una struttura diversa per generazione: leggerli richiederebbe di riscrivere i suoi lettori, uno per generazione, che è un lavoro sproporzionato rispetto allo scopo.

Quella conclusione è stata ritirata poche ore dopo averla scritta, ed è ADR-027: la deroga non serviva, perché era fondata su un errore di ricognizione. La domanda sulla disponibilità non richiede i dati degli incontri ma quelli di presenza, che stanno altrove e in forma molto più semplice, cioè array di record a dimensione fissa con un contrassegno in un bit noto, leggibili in cinquanta righe. Lo strumento `tools/disponibilita-titoli.py` li legge e il risultato sta in `pokedex-home-completo/STUDIO-01`. La lezione che resta è sul metodo: avevo guardato l'insieme di file che nomina la cosa cercata e avevo concluso dalla loro difficoltà che la cosa fosse difficile, mentre la domanda giusta era un'altra e più vicina. Segue la formulazione originale, conservata perché la deroga che dichiarava non è più in vigore ma il criterio con cui una deroga va dichiarata resta valido. La dichiarazione ha la stessa forma di quella già presa per la tabella dei caratteri giapponese: si nomina la fonte, si data la lettura, e si accetta che il rango sia inferiore. Va aggiunto un presidio che in quel caso non serviva e qui sì: la disponibilità di una specie in un gioco è una affermazione che il verificatore di conformità sa giudicare, quindi ogni voce dubbia si può mettere alla prova componendo un esemplare con quella provenienza e chiedendo il giudizio. Non è una verifica esaustiva ed è meglio di nessuna.
## 13. L'ambito del lavoro che ha una scadenza, e il numero che lo decide

La sezione 12 ha stabilito che la scadenza non vincola il Pokedex ma i singoli esemplari la cui identità richiede una provenienza anteriore all'ottava generazione. Ne segue immediatamente una domanda di ambito, posta dall'utente il 2026-09-02 nella forma giusta: se nessun gioco moderno li produce, non si dovrebbero prendere tutti gli esemplari che era possibile possedere e farli passare per la banca, ampliando l'elenco a tutte le generazioni che dopo non parleranno da sole con il deposito.

Il principio è corretto. Ogni esemplare che nasce nelle prime sette generazioni e che si voglia nel deposito con la propria provenienza originale ha quella scadenza, senza eccezioni: le prime due passano per la riedizione virtuale e il trasferitore, la terza per il parco e il trasferitore, la quarta e la quinta per il trasferitore, la sesta e la settima direttamente per la banca. Tutte finiscono nella banca, e la banca chiude.

### I tre insiemi concentrici, e perché vanno tenuti distinti

Ciò che il principio non dice è quanto grande sia l'insieme, e la risposta dipende da una scelta che non è tecnica. Gli insiemi candidati sono tre e stanno uno dentro l'altro.

Il primo è ciò che l'utente possiede: gli esemplari che stanno sulle sue cartucce. Sono irrimediabili nel senso più forte, perché non sono soltanto irriproducibili ma suoi, con il suo allenatore e la sua storia. La loro quantità è fissata da ciò che c'è sulle cartucce e non da una decisione: sono i trecentottantasei di una cartuccia di terza generazione, più ciò che sta sull'altra, più ciò che sta sui giochi della console portatile.

Il secondo è ciò che fu distribuito e non si rifà: gli esemplari da evento di ciascuna generazione. Sono irrimediabili in un senso diverso, cioè che nessun gioco moderno li produce, e la loro quantità è fissata dai cataloghi storici. Per la terza generazione sono centosettantadue e il progetto li produce; per la quarta e la quinta sono le carte del dono segreto, che il progetto ha contato in duecentoquattro e ottantaquattro; per la sesta e la settima esistono e non sono ancora state contate.

Il terzo è un Pokedex il cui marchio di origine sia antico, cioè un esemplare per specie che provenga dalle prime sette generazioni. Questo insieme è facoltativo, ed è di gran lunga il più grande: il suo valore non è di completezza, poiché il Pokedex si completa senza di esso, ma consiste nel far comparire nel deposito il marchio del gioco antico accanto a ciascuna specie. È una scelta di gusto, e va riconosciuta come tale invece di essere confusa con una necessità.

### Il vincolo non è la generazione ma il trasporto

La distinzione che decide l'ambito non è fra questi tre insiemi ma fra due tipi di costo, e va enunciata perché rovescia l'intuizione.

Produrre un esemplare non costa nulla. Il generatore ne fa centosettantadue in una frazione di secondo, e ne farebbe diecimila con lo stesso codice: sul lato della produzione non esiste alcun vincolo di ambito, e chiedersi quanti esemplari produrre è una domanda senza contenuto.

Trasportarli costa. Ogni passaggio della catena è manuale, richiede hardware fisico e non si automatizza, e alcuni passaggi hanno un limite di frequenza imposto dal gioco. Il primo passaggio della catena della terza generazione, quello che porta dalla terza alla quarta generazione, ne muove sei per volta e ha un limite giornaliero: se così è, il tetto della terza generazione è di sei esemplari al giorno, cioè poco più di mille nei giorni che restano.

Quel numero, se confermato, è il numero che decide l'ambito. Con esso i due primi insiemi ci stanno, poiché centosettantadue più trecentottantasei fanno cinquecentocinquantotto; il terzo insieme non ci starebbe, perché richiederebbe di aggiungere un esemplare per ciascuna delle specie che si volesse con marchio antico. E ne segue anche l'ordine con cui riempire il tetto, che è quello della irrimediabilità: prima ciò che è suo, poi ciò che fu distribuito, e il resto se avanza tempo.

### Perché questa nota non decide, e che cosa va misurato

Il limite di sei al giorno è riportato qui come da verificare e non come fatto. Il progetto non lo ha letto su una fonte in questa sessione, e la sua importanza è tale che una stima non basta: da esso dipende se l'ambito sia di cinquecento esemplari o di cinquemila, e quindi se il terzo insieme sia una possibilità o una fantasia.

La misura è però semplice e si esegue in un giorno, e non richiede di avere deciso nulla: si esegue un passaggio, si conta quanti esemplari muove, si tenta di ripeterlo subito e si osserva se il gioco lo consenta. È la medesima raccomandazione che questa nota dà per le carte del dono segreto, cioè misurare un ciclo prima di pianificarne duecento, e la ragione è la stessa: una pianificazione fondata su un tasso non misurato non è una pianificazione ma un augurio.
