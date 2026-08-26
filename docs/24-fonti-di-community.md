# 24. Le community come fonte, e come si leggono

Alcune informazioni di cui questo progetto ha bisogno esistono documentate in un solo posto al mondo, e quel posto e' una chat. Non un articolo, non un wiki, non un repository con un README: un canale Discord dove qualcuno, in un pomeriggio di due anni fa, ha scritto tre messaggi che spiegano perche' un approccio funziona e un altro no. Il caso concreto che ha reso necessaria questa nota e' la testimonianza sulle schede Wi-Fi capaci di modalita' monitor per il track dello scambio con la Switch: la lista ufficiale del progetto di riferimento indica tre modelli, il canale di supporto di una community ne indica un quarto che costa una frazione, e quell'informazione non e' scritta in nessun altro luogo.

Ne nasce un problema di metodo, perche' una chat non e' raggiungibile ne' dal crawler del modello ne' da una richiesta HTTP. Le pagine di Discord sono un'applicazione a pagina singola dietro autenticazione e il contenuto non e' indicizzato, quindi non esiste la via del recupero diretto e nemmeno quella dell'archivio pubblico. L'unica via e' un export prodotto da chi e' membro del server, cioe' dall'utente, ed e' la stessa struttura di consegna che `.claude/rules/web-sources-not-fetchable.md` descrive per Reddit e per i forum che rispondono 403.

## Il costo di quella via, dichiarato prima di tutto il resto

Lo strumento maturo per l'export e' `DiscordChatExporter`, che esiste in versione grafica e a riga di comando. Per esportare un canale di un server di cui si e' membri, senza essere un bot, richiede il token utente dell'account, perche' e' l'unica credenziale che identifica un account personale verso l'API.

Le condizioni d'uso di Discord non consentono l'accesso automatizzato con un account personale, che nella loro terminologia e' un self-bot, e la conseguenza prevista e' la sospensione dell'account. Va detto senza ambiguita', perche' e' una decisione di rischio e non un dettaglio di configurazione: la sospensione colpirebbe l'account e con esso l'appartenenza a tutti i server, non il file esportato. Il progetto non decide al posto dell'utente; cio' che il progetto impone e' che il token non entri mai in un file tracciato, mai in una conversazione con l'agente, e che l'uso resti puntuale su un canale e un intervallo di date invece di diventare continuativo.

Esiste una via che quel rischio non lo corre, ed e' il copia-incolla manuale della porzione di conversazione rilevante in un file di testo. E' peggiore in efficienza e migliore in tutto il resto, e per il volume di cui questo progetto ha bisogno, cioe' qualche decina di messaggi su tre o quattro discussioni, e' probabilmente la scelta giusta. Il lettore descritto sotto accetta comunque il formato di export, e un file di testo consegnato a mano va trattato come qualunque altra fonte procurata fuori banda.

## Dove si prende il token, se si decide di prenderlo

La procedura appartiene all'utente e non all'agente, che il token non lo vede mai. Si apre Discord nel browser, non nell'applicazione desktop, si aprono gli strumenti di sviluppo e nella scheda della rete si osserva una richiesta qualunque verso l'API: l'intestazione `Authorization` porta il token. Il token e' equivalente alla password piu' il secondo fattore, quindi va incollato solo nel campo dello strumento e in nessun altro luogo, e la sua revoca si ottiene cambiando la password dell'account, cosa che invalida i token esistenti.

L'identificativo del canale si ottiene attivando la modalita' sviluppatore nelle impostazioni avanzate di Discord, che aggiunge la voce di copia dell'identificativo nel menu contestuale del canale.

## L'invocazione dell'export

La versione a riga di comando sta in `E:\[TBC] discord-chat-exporter`. L'esportazione di un canale in JSON, che e' il formato che il lettore preferisce perche' conserva i metadati, si fa con il comando seguente, dove l'intervallo di date serve a non scaricare anni di conversazione quando interessa una settimana.

```powershell
DiscordChatExporter.Cli.exe export -t "<token>" -c "<id del canale>" -f Json --after "2024-01-01" -o "E:\retrogame-mod-pok-dev\_notes\fonti\discord-<server>-<canale>.json"
```

La destinazione e' `_notes/fonti/`, che e' ignorato da git: il contenuto di una chat non entra nel repository, esattamente come non vi entra un dump di cartuccia. Cio' che entra e' la sintesi in `SOURCES.md` e nella nota della fonte, con l'attribuzione a chi ha scritto il messaggio.

## Il lato del progetto, che il token non lo tocca

`tools/read-chat-export.py` lavora su un file gia' prodotto e non parla con nessun servizio. Converte l'export in Markdown tenendo autore, momento, testo, allegati e indicazione delle risposte, e scarta il resto, che in un export e' la maggior parte del volume, cioe' reazioni, incorporamenti e identificativi interni.

I tre filtri sono il modo per far entrare in contesto una conversazione senza farvi entrare il rumore. Il filtro per parola chiave, ripetibile, tiene solo i messaggi che contengono almeno uno dei termini. Il filtro per intervallo di date restringe al periodo in cui si sa che la discussione e' avvenuta. Il filtro per lunghezza minima elimina le risposte di una parola, che in un canale di supporto sono circa la meta' dei messaggi e non contengono informazione tecnica.

```powershell
python tools\read-chat-export.py "_notes\fonti\discord-pmr-supporto.json" --grep "monitor mode" --grep "adapter" --min-length 80 -o "_notes\fonti\pmr-schede-wifi.md"
```

Il riconoscimento del formato guarda la forma del documento e non l'estensione, perche' l'estensione e' `.json` in entrambi i casi: la presenza di una chiave di canale o di gilda accanto ai messaggi indica Discord, la presenza di un nome o di un tipo indica l'export di Telegram Desktop. Per Telegram c'e' una complicazione che vale la pena conoscere, cioe' che il testo di un messaggio con formattazione non e' una stringa ma una lista di frammenti, dove le parti in grassetto e i collegamenti sono oggetti: il lettore li ricompone in ordine, altrimenti meta' dei messaggi risulterebbe vuota.

## Perche' questo strumento non e' specifico di questo progetto

Il lettore non sa nulla di Pokemon, di Game Boy e di salvataggi: legge un formato di export e produce Markdown filtrato. E' quindi candidato a uscire da qui ed entrare nel template come strumento disponibile a ogni progetto nuovo, insieme al recupero da Reddit, alla ripulitura dei sottotitoli e al generatore della mappa delle fonti. Il passaggio si fa con un handoff, come e' stato fatto per la regola sulle fonti non recuperabili, e non copiando i file a mano: cio' che va propagato non e' soltanto lo script, ma anche la convenzione di consegna in `_notes/fonti/` e l'avvertenza sul token, che senza il suo contesto diventerebbe un invito implicito a violare le condizioni d'uso di un servizio.

## Dove sta il resto

| Cosa cerchi | Dove sta |
|---|---|
| la scala di escalation per una fonte non raggiungibile | `.claude/rules/web-sources-not-fetchable.md` |
| i cinque server e cosa ci si cerca | `SOURCES.md`, sezione delle community |
| la testimonianza sulle schede Wi-Fi | `.claude/context/sub-gba-switch-trading.md` |
| lo stato dello strumento e la decisione aperta sul token | `.claude/memory/pending.md` |
