# 24. Le community come fonte, e come si leggono

Alcune informazioni di cui questo progetto ha bisogno esistono documentate in un solo posto al mondo, e quel posto è una chat. Non un articolo, non un wiki, non un repository con un README: un canale Discord dove qualcuno, in un pomeriggio di due anni fa, ha scritto tre messaggi che spiegano perché un approccio funziona e un altro no. Il caso concreto che ha reso necessaria questa nota è la testimonianza sulle schede Wi-Fi capaci di modalità monitor per il track dello scambio con la Switch: la lista ufficiale del progetto di riferimento indica tre modelli, il canale di supporto di una community ne indica un quarto che costa una frazione, e quell'informazione non è scritta in nessun altro luogo.

Ne nasce un problema di metodo, perché una chat non è raggiungibile né dal crawler del modello né da una richiesta HTTP. Le pagine di Discord sono un'applicazione a pagina singola dietro autenticazione e il contenuto non è indicizzato, quindi non esiste la via del recupero diretto e nemmeno quella dell'archivio pubblico. L'unica via è un export prodotto da chi è membro del server, cioè dall'utente, ed è la stessa struttura di consegna che `.claude/rules/web-sources-not-fetchable.md` descrive per Reddit e per i forum che rispondono 403.

## Il costo di quella via, dichiarato prima di tutto il resto

Lo strumento maturo per l'export è `DiscordChatExporter`, che esiste in versione grafica e a riga di comando. Per esportare un canale di un server di cui si è membri, senza essere un bot, richiede il token utente dell'account, perché è l'unica credenziale che identifica un account personale verso l'API.

Le condizioni d'uso di Discord non consentono l'accesso automatizzato con un account personale, che nella loro terminologia è un self-bot, e la conseguenza prevista è la sospensione dell'account. Va detto senza ambiguità, perché è una decisione di rischio e non un dettaglio di configurazione: la sospensione colpirebbe l'account e con esso l'appartenenza a tutti i server, non il file esportato. Il progetto non decide al posto dell'utente; ciò che il progetto impone è che il token non entri mai in un file tracciato, mai in una conversazione con l'agente, e che l'uso resti puntuale su un canale e un intervallo di date invece di diventare continuativo.

Esiste una via che quel rischio non lo corre, ed è il copia-incolla manuale della porzione di conversazione rilevante in un file di testo. È peggiore in efficienza e migliore in tutto il resto, e per il volume di cui questo progetto ha bisogno, cioè qualche decina di messaggi su tre o quattro discussioni, è probabilmente la scelta giusta. Il lettore descritto sotto accetta comunque il formato di export, e un file di testo consegnato a mano va trattato come qualunque altra fonte procurata fuori banda.

## Dove si prende il token, se si decide di prenderlo

La procedura appartiene all'utente e non all'agente, che il token non lo vede mai. Si apre Discord nel browser, non nell'applicazione desktop, si aprono gli strumenti di sviluppo e nella scheda della rete si osserva una richiesta qualunque verso l'API: l'intestazione `Authorization` porta il token. Il token è equivalente alla password più il secondo fattore, quindi va incollato solo nel campo dello strumento e in nessun altro luogo, e la sua revoca si ottiene cambiando la password dell'account, cosa che invalida i token esistenti.

L'identificativo del canale si ottiene attivando la modalità sviluppatore nelle impostazioni avanzate di Discord, che aggiunge la voce di copia dell'identificativo nel menu contestuale del canale.

## L'invocazione dell'export

La versione a riga di comando sta in `E:\[TBC] discord-chat-exporter`. L'esportazione di un canale in JSON, che è il formato che il lettore preferisce perché conserva i metadati, si fa con il comando seguente, dove l'intervallo di date serve a non scaricare anni di conversazione quando interessa una settimana.

```powershell
DiscordChatExporter.Cli.exe export -t "<token>" -c "<id del canale>" -f Json --after "2024-01-01" -o "E:\retrogame-mod-pok-dev\_notes\fonti\discord-<server>-<canale>.json"
```

La destinazione è `_notes/fonti/`, che è ignorato da git: il contenuto di una chat non entra nel repository, esattamente come non vi entra un dump di cartuccia. Ciò che entra è la sintesi in `SOURCES.md` e nella nota della fonte, con l'attribuzione a chi ha scritto il messaggio.

## Il lato del progetto, che il token non lo tocca

`tools/read-chat-export.py` lavora su un file già prodotto e non parla con nessun servizio. Converte l'export in Markdown tenendo autore, momento, testo, allegati e indicazione delle risposte, e scarta il resto, che in un export è la maggior parte del volume, cioè reazioni, incorporamenti e identificativi interni.

I tre filtri sono il modo per far entrare in contesto una conversazione senza farvi entrare il rumore. Il filtro per parola chiave, ripetibile, tiene solo i messaggi che contengono almeno uno dei termini. Il filtro per intervallo di date restringe al periodo in cui si sa che la discussione è avvenuta. Il filtro per lunghezza minima elimina le risposte di una parola, che in un canale di supporto sono circa la metà dei messaggi e non contengono informazione tecnica.

```powershell
python tools\read-chat-export.py "_notes\fonti\discord-pmr-supporto.json" --grep "monitor mode" --grep "adapter" --min-length 80 -o "_notes\fonti\pmr-schede-wifi.md"
```

Il riconoscimento del formato guarda la forma del documento e non l'estensione, perché l'estensione è `.json` in entrambi i casi: la presenza di una chiave di canale o di gilda accanto ai messaggi indica Discord, la presenza di un nome o di un tipo indica l'export di Telegram Desktop. Per Telegram c'è una complicazione che vale la pena conoscere, cioè che il testo di un messaggio con formattazione non è una stringa ma una lista di frammenti, dove le parti in grassetto e i collegamenti sono oggetti: il lettore li ricompone in ordine, altrimenti metà dei messaggi risulterebbe vuota.

## Perché questo strumento non è specifico di questo progetto

Il lettore non sa nulla di Pokemon, di Game Boy e di salvataggi: legge un formato di export e produce Markdown filtrato. È quindi candidato a uscire da qui ed entrare nel template come strumento disponibile a ogni progetto nuovo, insieme al recupero da Reddit, alla ripulitura dei sottotitoli e al generatore della mappa delle fonti. Il passaggio si fa con un handoff, come è stato fatto per la regola sulle fonti non recuperabili, e non copiando i file a mano: ciò che va propagato non è soltanto lo script, ma anche la convenzione di consegna in `_notes/fonti/` e l'avvertenza sul token, che senza il suo contesto diventerebbe un invito implicito a violare le condizioni d'uso di un servizio.

## Dove sta il resto

| Cosa cerchi | Dove sta |
|---|---|
| la scala di escalation per una fonte non raggiungibile | `.claude/rules/web-sources-not-fetchable.md` |
| i cinque server e cosa ci si cerca | `SOURCES.md`, sezione delle community |
| la testimonianza sulle schede Wi-Fi | `.claude/context/sub-gba-switch-trading.md` |
| lo stato dello strumento e la decisione aperta sul token | `.claude/memory/pending.md` |
