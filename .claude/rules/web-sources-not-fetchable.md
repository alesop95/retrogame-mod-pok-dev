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

Le due vie che funzionano restano la seconda e la terza. Per la terza, l'API ufficiale di Reddit ha un flusso a sole credenziali applicative, senza account collegato, che basta per leggere contenuto pubblico: si registra una applicazione di tipo script, si ottengono identificativo e segreto, e si scambia il segreto per un token temporaneo. Lo strumento che implementa questo flusso e' `tools/fetch-reddit.py`, che legge le credenziali dall'ambiente o da `.env` e degrada in un messaggio con le istruzioni quando non le trova.

## Come si annota una fonte non letta

Nel registro delle fonti, la voce resta, perche' sapere che esiste ha valore. Cambia la descrizione, che deve dire che non e' stata letta e perche'. La formula da usare e' quella del registro attuale, cioe' indicare il dominio come luogo dove cercare e non come fonte verificata, e questa distinzione va ripetuta nella sezione che separa le fonti consultate da quelle catalogate.

Quando una fonte prima non leggibile diventa leggibile, per esempio perche' sono state configurate le credenziali, l'etichetta va rimossa e la voce va aggiornata con cio' che la fonte documenta davvero. Una etichetta di indisponibilita' che sopravvive alla sua causa e' peggio della sua assenza, perche' scoraggia dal riprovare.
