# Fonti web non recuperabili automaticamente

> Regola modulare. Stabilisce cosa fare quando una fonte esiste ed e' rilevante ma non si riesce a recuperarla con gli strumenti di sessione, cosi' che il progetto non degradi silenziosamente una fonte a nota a margine. Vale per qualunque dominio, e usa Reddit come caso studiato perche' e' quello che si incontra piu' spesso.

## Il principio

Una fonte che non si riesce a leggere non e' una fonte inaffidabile: e' una fonte non letta, ed e' una distinzione che va scritta ogni volta. Il rischio, altrimenti, e' che il registro delle fonti si riempia di voci che sembrano consultate e non lo sono, e che un'affermazione poggi su un titolo di thread invece che sul suo contenuto.

Da qui la regola in due parti. La prima e' che ogni voce non letta va etichettata come tale nel registro, con il motivo. La seconda e' che, prima di etichettarla, si tenta il recupero per le vie documentate qui sotto, in ordine di costo crescente, invece di arrendersi al primo errore.

## Le vie, in ordine di costo crescente

La prima via e' il recupero locale con `curl` dal Bash tool. Vale la pena provarla sempre, perche' e' indipendente dal crawler del modello: sono due agenti diversi, con due indirizzi diversi e due reputazioni diverse, e capita spesso che un dominio blocchi l'uno e non l'altro. Molti siti rispondono a `curl` solo con uno user agent da browser.

La seconda via e' l'automazione del browser reale dell'utente, cioe' la skill `claude-in-chrome` dove e' disponibile. E' la via che funziona su quasi tutto, perche' e' un browser vero con la sessione dell'utente, e per questo va usata con misura: apre schede nel browser della persona e richiede che i permessi per quel sito siano concessi nell'estensione. Si chiede prima, non si fa e poi si dice.

La terza via e' l'API ufficiale del servizio, quando esiste, con credenziali dell'utente. E' la piu' solida e la piu' costosa da allestire, e ha senso solo per le fonti che il progetto consulta ripetutamente. Le credenziali stanno in `.env`, che il `.gitignore` esclude, e non entrano mai in un file tracciato ne' in una chat.

Un dettaglio operativo che vale registrare, perche' altrimenti sembra una dimenticanza: l'agente non puo' creare ne' leggere alcun file che corrisponda a `.env*`, nemmeno il modello `.env.example`, perche' le regole di permesso del progetto lo negano per protezione. Il modello va quindi creato a mano dall'utente, e le variabili che servono sono documentate nel docstring dello strumento che le consuma. E' una limitazione voluta e non va aggirata.

Se nessuna delle tre e' praticabile, resta l'ultima, che non e' una sconfitta: si chiede all'utente di incollare il contenuto. E' la stessa logica della regola sugli screenshot, cioe' quando l'agente non puo' vedere una cosa la chiede invece di inventarla, e la richiesta va fatta mirata su un contenuto preciso e non come lamentela generica.

## Il caso Reddit, verificato il 2026-08-25

Reddit merita una scheda propria perche' e' una fonte tecnica di prima qualita' su hardware retro, modding e reverse engineering, e perche' la sua indisponibilita' e' facile da attribuire alla causa sbagliata. Non e' un problema di configurazione del progetto ne' del template: e' la somma di due fatti indipendenti, entrambi fuori dal controllo di chi lavora.

| Via tentata | Esito |
|---|---|
| `WebFetch` su `reddit.com` | rifiutato: il dominio non e' accessibile allo user agent di Anthropic |
| `WebSearch` con `allowed_domains` su reddit.com | rifiutato allo stesso modo, con rimando alla pagina di supporto |
| `curl` locale su `www.reddit.com`, con e senza user agent da browser | HTTP 403 |
| `curl` locale sull'endpoint JSON di `old.reddit.com` | HTTP 302 verso la pagina di login |
| frontend alternativi, per esempio istanze redlib | HTTP 403 in un caso, sfida JavaScript di verifica del browser nell'altro |
| proxy di lettura `r.jina.ai` | HTTP 403 |

I risultati di ricerca continuano a restituire URL di Reddit, e quelli sono utili: dicono che una discussione esiste e su cosa. Ma il titolo di un thread non e' il suo contenuto, e va trattato come un puntatore da verificare.

In teoria restano la seconda e la terza via. Per la terza, l'API ufficiale di Reddit ha un flusso a sole credenziali applicative, senza account collegato, che basta per leggere contenuto pubblico: si registra una applicazione di tipo script, si ottengono identificativo e segreto, e si scambia il segreto per un token temporaneo. Lo strumento che implementa questo flusso e' `tools/fetch-reddit.py`, che legge le credenziali dall'ambiente o da `.env` e degrada in un messaggio con le istruzioni quando non le trova. In pratica, come racconta la sottosezione seguente, su questo account la registrazione dell'applicazione e' stata rifiutata anche dopo aver rimosso ogni causa nota, quindi la terza via oggi non e' disponibile e lo strumento resta pronto per il giorno in cui lo fosse.

### La registrazione dell'applicazione, e perche' puo' rifiutare senza dirlo

La registrazione avviene su `https://old.reddit.com/prefs/apps`, dove si compila il form scegliendo il tipo script, un nome qualunque, e come URI di reindirizzamento un valore che non verra' mai usato, per esempio `http://localhost:8080`, perche' il flusso a sole credenziali applicative non fa alcun reindirizzamento. Il campo about url si lascia vuoto.

Esiste un modo di fallire che va documentato perche' consuma tempo e sembra un errore di compilazione: alla pressione del pulsante di creazione la pagina si ricarica con il form ancora compilato e senza alcun errore accanto ai campi. Non e' un problema di reCAPTCHA, che nel caso osservato il 2026-08-26 era stato spuntato correttamente, e non e' un problema di blocco degli annunci, perche' il rifiuto persiste con le estensioni disattivate. E' un rifiuto lato server, e la pagina lo racconta soltanto con una riga accanto al pulsante che rimanda alla Responsible Builder Policy.

Sulle cause il progetto ha una risposta empirica, ed e' negativa. Le due ipotesi che questa regola indicava sono state verificate una per una il 2026-08-26 e sono cadute entrambe. La prima era l'email non verificata: e' stata verificata, e il pannello vecchio delle preferenze la mostra come tale accanto all'indirizzo. La seconda era la registrazione preventiva dell'uso dell'API: la documentazione ufficiale dice che per l'uso gratuito e non commerciale quel modulo non esiste, e serve solo alle richieste commerciali, aziendali, accademiche o di superamento dei limiti. Il tentativo e' stato ripetuto con un nome privo di trattini e caratteri speciali, tipo script e URI di reindirizzamento inutilizzato, e il rifiuto e' rimasto identico.

Ne segue la conclusione onesta, che vale come regola e non come resoconto di un caso: se il rifiuto persiste dopo aver verificato l'email e accertato che nessun modulo preventivo sia richiesto, la terza via non e' disponibile su quell'account e non vale la pena insistere. Il rimando alla Responsible Builder Policy suggerisce che l'ammissibilita' dipenda da requisiti di quella politica, e un'ipotesi plausibile ma non verificata e' che contino l'eta' o l'attivita' dell'account; in ogni caso non e' un ostacolo aggirabile compilando meglio il form. Restano la seconda e la quarta via, cioe' l'automazione del browser reale e la consegna manuale, e la seconda ha nel frattempo dimostrato di funzionare bene: le ricerche interne ai canali consegnate come screenshot il 2026-08-26 hanno prodotto materiale di qualita' superiore a quella che una API avrebbe dato, perche' un filtro applicato da chi conosce la domanda e' piu' selettivo di una richiesta automatica.

## Come l'utente consegna il materiale, e in che formato

Quando la via resta la quarta, cioe' l'utente procura il contenuto, il modo di consegnarlo non e' incollarlo in chat: e' salvarlo su disco in una cartella concordata, perche' cosi' resta disponibile anche nelle sessioni successive e non consuma contesto due volte. La cartella e' `_notes/fonti/`, locale e non versionata come tutto `_notes/`, e la convenzione di nome e' la data seguita da una parola che identifica la fonte, per esempio `2026-08-25-gbatemp-save-failed.md`.

Sui formati, in ordine di preferenza. Il testo semplice o Markdown e' il migliore, perche' e' cercabile, diffabile e non porta rumore: per una discussione basta il corpo dei messaggi con l'autore e la data, senza la struttura di navigazione del sito. Il salvataggio della pagina come singolo file HTML va bene e si legge, ma va detto che contiene molto rumore. Il PDF e' accettabile e leggibile. Uno screenshot e' l'ultima scelta, perche' non e' cercabile ne' citabile parola per parola, e va riservato ai casi in cui il contenuto e' grafico.

Sulle chat esiste una forma di consegna che vale piu' di tutte le altre e che va chiesta esplicitamente, perche' l'utente non ha motivo di inventarla. Non e' l'esportazione del canale, che e' voluminosa e richiede strumenti discutibili, e non e' la copia di una conversazione scelta a occhio: e' la ricerca interna al canale con un termine concordato, di cui si consegna la lista dei risultati. La prova sul campo del 2026-08-26 e' netta: cinque filtri su un server e tre su un altro hanno prodotto in poche decine di schermate il contenuto che ha corretto tre affermazioni sbagliate del progetto e ne ha aggiunte due nuove, con un rapporto fra segnale e volume che nessuna esportazione integrale avrebbe avuto. La ragione e' che il filtro incorpora la domanda, e chi cerca sa che cosa sta cercando.

Ne segue una prescrizione operativa per chi chiede il materiale. Si concordano i termini di ricerca prima, non il canale; si chiede il conteggio dei risultati insieme alle schermate, perche' sapere che un filtro ha dato zero risultati e' esso stesso un dato, come nel caso del filtro sul numero di un chip che ha dimostrato l'assenza di qualsiasi testimonianza; e si accetta che su un filtro molto generico l'utente si fermi a una parte dei risultati, purche' dichiari dove si e' fermato, cosi' che la copertura parziale resti dichiarata invece di sembrare completa.

Per un video la forma utile non e' il video ma la sua trascrizione. YouTube la espone nell'interfaccia sotto il pulsante che mostra la trascrizione, e da la' si copia; in alternativa `yt-dlp` la scarica da riga di comando, al prezzo di installare un pacchetto. In entrambi i casi il file va nella stessa cartella, con la stessa convenzione di nome, e conviene conservare accanto l'identificativo del video, perche' la trascrizione da sola non dice da dove viene.

Una richiesta di materiale va sempre accompagnata dalla domanda a cui serve rispondere. Chiedere una discussione intera senza dire cosa si cerca produce lavoro inutile per chi la procura e lettura inutile per chi la riceve.

## Come si annota una fonte non letta

Nel registro delle fonti, la voce resta, perche' sapere che esiste ha valore. Cambia la descrizione, che deve dire che non e' stata letta e perche'. La formula da usare e' quella del registro attuale, cioe' indicare il dominio come luogo dove cercare e non come fonte verificata, e questa distinzione va ripetuta nella sezione che separa le fonti consultate da quelle catalogate.

Quando una fonte prima non leggibile diventa leggibile, per esempio perche' sono state configurate le credenziali, l'etichetta va rimossa e la voce va aggiornata con cio' che la fonte documenta davvero. Una etichetta di indisponibilita' che sopravvive alla sua causa e' peggio della sua assenza, perche' scoraggia dal riprovare.
