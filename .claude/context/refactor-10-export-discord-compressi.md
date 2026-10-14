# Refactor 10. Una fonte non recuperabile si comprime solo insieme alla prova che non è cambiata

> Scheda di dettaglio della voce 10 di `studio-didattico-master.md`. Entra nel formato di DiscordChatExporter, nella patch a `tools/read-chat-export.py` e nel nuovo `tools/verifica-integrita-export.py`. La decisione corrispondente è ADR-104.

## Il caso

La cartella `_notes/fonti/discord/dce/` conteneva 2,58 GB in 49 export di canali Discord. Nessuno di quei canali si riscarica: la norma in `.claude/skills/fonti-non-recuperabili/RIFERIMENTO.md` li classifica fra le fonti che richiedono un passaggio manuale, e l'export di un server a cui non si appartiene più non si rifà affatto. Allo stesso tempo `_notes/` è ignorato da git, quindi su quei file non esiste storia, non esiste `git checkout` e non esiste rete di protezione. Sono dati preziosi e insieme fragili, ed è questa combinazione, non il loro peso, a determinare la forma dell'intervento.

La domanda di partenza era perché pesassero tanto. La risposta si ottiene contando i byte per chiave invece di indovinarla, ed è stata misurata su `pret-pokered.json`, 294,4 MB e 278.289 messaggi, classificando ogni riga del file secondo la chiave JSON che apre. Il formato è indentato a due spazi e una chiave per riga, quindi la classificazione è esatta e non campionaria.

| voce | peso | quota |
|---|---|---|
| `avatarUrl` | 39,8 MB | 13,5% |
| `content`, cioè il testo dei messaggi | 28,9 MB | 9,8% |
| `id` | 28,5 MB | 9,7% |
| `name`, `nickname`, `discriminator`, `color`, `isBot` | 50,6 MB | 17,1% |
| `timestamp`, `timestampEdited`, `callEndedTimestamp` | 34,0 MB | 11,5% |
| liste sempre vuote: `embeds`, `stickers`, `mentions`, `inlineEmojis`, `roles` | 32,6 MB | 11,0% |

Il dato che orienta tutto il resto è il secondo: il testo delle conversazioni, cioè l'unica cosa per cui quei file esistono, è il 9,8% del file. Il restante novanta per cento è impalcatura, e l'impalcatura è *ripetuta*, che è la proprietà che rende la compressione la risposta giusta invece di una toppa.

## Perché il formato pesa, in concreto

DiscordChatExporter serializza ogni messaggio come un oggetto completo e indipendente, e dentro ogni messaggio riserializza per intero la scheda del suo autore. Non esiste una tabella degli autori a cui i messaggi rimandino: il nome, il soprannome, il discriminatore, il colore del ruolo e l'indirizzo completo dell'immagine del profilo ricompaiono per esteso sotto ogni singola riga di chat. Ecco un messaggio reale di due parole, riportato per intero come sta nel file:

```json
{
  "id": "505603262775296023",
  "type": "Default",
  "timestamp": "2018-10-27T06:46:51.5+02:00",
  "timestampEdited": null,
  "callEndedTimestamp": null,
  "isPinned": false,
  "content": "oh no",
  "author": {
    "id": "347682143159320577",
    "name": "<autore>",
    "discriminator": "0000",
    "nickname": "<Autore>",
    "color": null,
    "isBot": false,
    "roles": [],
    "avatarUrl": "https://cdn.discordapp.com/avatars/347682143159320577/e4420b1476d5286cce41f00d89343596.png?size=512"
  },
  "attachments": [],
  "embeds": [],
  "stickers": [],
  "reactions": [],
  "mentions": [],
  "inlineEmojis": []
}
```

Cinque byte di conversazione dentro circa settecento byte di file. In un canale dove poche decine di persone scrivono centinaia di migliaia di messaggi, la stessa scheda d'autore e lo stesso indirizzo di avatar si ripetono decine di migliaia di volte, identici carattere per carattere. Un compressore a dizionario come *DEFLATE*, che è l'algoritmo dentro gzip, è costruito esattamente per questo: la seconda occorrenza di una sequenza già vista non si riscrive, si cita come distanza e lunghezza. Un file la cui ridondanza è così regolare non si comprime del dieci o del venti per cento, si comprime di un ordine di grandezza, ed è ciò che la misura conferma.

Va detto con precisione che cosa questo implica e che cosa no. La compressione non toglie nulla dal file: ogni campo, compreso l'indirizzo dell'avatar che a questo progetto non serve, resta recuperabile bit per bit. Rimuovere davvero i campi inutili, riscrivendo gli export in una forma snella con gli autori deduplicati in tabella, darebbe un file ancora leggibile a occhio e otto volte e mezzo più piccolo, e in più risolverebbe un secondo problema di cui si dirà in chiusura. Non è stato fatto in questo giro perché cambia il contenuto della fonte, e una fonte non recuperabile non si riscrive nello stesso intervento in cui la si comprime: la reversibilità bit per bit è ciò che rende questo intervento sicuro, e vale più dei megabyte in più.

## Perché gzip e non zstd, che comprime meglio

La misura su tutta la cartella, con zstd al livello 12, dà 2,37 GB che diventano 119 MB, cioè un fattore venti. Il rapporto per file va da 10,5x sui canali piccoli, dove il dizionario non fa in tempo a riempirsi, a 34,4x su `GlitchCity-gen-2-glitches.json`. Gzip al livello 9, misurato dopo sugli stessi file, si ferma a 186 MB, cioè un fattore 13,9: oltre il cinquanta per cento di spazio in più, e vale la pena dire che è peggio di quanto avessi previsto prima di misurarlo, perché la stima fatta estrapolando da un file solo dava centocinquantacinque megabyte. Nonostante il divario la scelta è caduta su gzip, e la ragione non ha a che vedere con la compressione.

L'interprete di questa macchina è Python 3.13, e Python 3.13 non sa leggere zstd. Il pacchetto `zstandard` va installato con pip e non è fra le dipendenze del progetto; il modulo `compression.zstd` entra nella libreria standard solo con Python 3.14. Un export compresso con zstd richiederebbe quindi, per essere riaperto, il binario esterno `zstd` presente nel PATH: una dipendenza fuori dal repository, necessaria per aprire una fonte che il repository stesso dichiara non recuperabile. Chi clonasse il progetto su una macchina pulita si troverebbe dei file che non sa aprire, e lo scoprirebbe nel momento peggiore, cioè quando gli serve la fonte.

Gzip invece sta nella libreria standard di ogni Python da sempre, e la patch necessaria allo strumento di lettura è una funzione di sei righe. I sessantasette megabyte di differenza si pagano volentieri: la cartella scende comunque da 2,58 GB a 188 MB contando anche i ventidue file lasciati in chiaro, e la differenza fra centottantotto e centoventi megabyte non cambia nessuna decisione, mentre la differenza fra aprire e non aprire un file le cambia tutte.

## Il codice, prima e dopo

Lo strumento di lettura apriva l'export in un modo solo, e la riga era questa:

```python
    with io.open(args.export, encoding="utf-8", errors="replace") as fh:
        payload = json.load(fh)
```

La tentazione è di aggiungere un ramo sull'estensione del nome, cioè di controllare se il percorso finisca in `.gz`. È la soluzione fragile, e lo è per una ragione che lo strumento stesso aveva già scritto nella propria documentazione a proposito di un altro problema: «Il formato viene riconosciuto dalla forma del file, non dall'estensione». Quella frase, scritta per distinguere un export Discord da uno Telegram, vale identica per la compressione. Un file rinominato a mano, un export salvato senza estensione, un `.gz` dentro una cartella il cui nome è stato sistemato dopo: in tutti questi casi il nome mente e il contenuto no.

La forma nuova guarda i primi due byte, che per ogni flusso gzip sono `1f 8b`, e decide da quelli:

```python
# I due byte con cui si apre ogni flusso gzip. Si guarda il contenuto e non il nome del file
# perche' un export rinominato a mano resta leggibile, mentre un gzip salvato senza la sua
# estensione, se ci si fidasse del nome, non lo sarebbe.
MAGICO_GZIP = b"\x1f\x8b"


def apri_export(path):
    """Apre l'export in lettura testo, decomprimendolo al volo se e' un gzip.

    Ritorna un flusso di testo gia' decodificato in UTF-8, con gli errori sostituiti come fa
    l'apertura in chiaro: chi chiama non deve sapere se il file su disco sia compresso.
    """
    with io.open(path, "rb") as fh:
        magico = fh.read(2)
    if magico == MAGICO_GZIP:
        return io.TextIOWrapper(gzip.open(path, "rb"), encoding="utf-8", errors="replace")
    return io.open(path, encoding="utf-8", errors="replace")
```

Il punto di qualità non è la funzione ma il suo contratto, dichiarato nella docstring: restituisce un flusso di testo già decodificato, uguale nei due casi, così che chi la chiama non sappia e non debba sapere se il file su disco sia compresso. Il corpo di `main()` cambia di una riga sola, e nessun'altra parte dello strumento viene toccata.

```python
    with apri_export(args.export) as fh:
        payload = json.load(fh)
```

Lo stesso intervento è stato applicato alle due copie dello strumento, quella operativa in `tools/` e quella del pacchetto in `.claude/templates/community-sources/tools/`, perché le due differivano prima soltanto per cinque righe di docstring localizzate al progetto ospite e devono continuare a differire soltanto per quelle. Una patch applicata a una sola delle due avrebbe prodotto uno scostamento funzionale fra pacchetto e progetto, che è precisamente ciò che il controllo di allineamento esiste per impedire.

## Lo strumento che produce la prova

Comprimere è un comando. Comprimere una fonte non recuperabile è un comando più una dimostrazione, perché se la compressione perde qualcosa non esiste l'originale da cui riprovare, e soprattutto perché una perdita silenziosa non si manifesta il giorno in cui avviene ma il giorno, mesi dopo, in cui si cerca una risposta dentro quella fonte e non la si trova. Il nuovo `tools/verifica-integrita-export.py` esiste per rendere impossibile quella perdita silenziosa, e lavora in tre modi che vanno eseguiti in ordine.

Il modo `manifesto` percorre la cartella e calcola l'impronta SHA-256 di ogni export, scrivendo in `MANIFEST-integrita.txt` una riga per file con impronta, dimensione e percorso relativo. L'impronta è quella del contenuto *non compresso*, ed è questa scelta a far funzionare tutto il resto: resta valida dopo la compressione, quindi lo stesso manifesto che fotografa il prima serve a verificare il dopo, senza bisogno di conservare due elenchi e di tenerli allineati.

Il modo `comprimi` legge il manifesto, scrive accanto a ogni export il suo `.gz`, poi *rilegge il compresso decomprimendolo* e confronta l'impronta ottenuta con quella attesa. Se non corrispondono, il compresso viene rimosso e l'originale resta intatto. Nessun originale viene cancellato in questo modo, qualunque opzione si passi.

Il modo `verifica` rilegge ogni file della cartella, decomprimendo quelli compressi e leggendo direttamente quelli rimasti in chiaro, e confronta tutto con il manifesto. È questo, e solo questo, il modo che sa cancellare gli originali, quando lo si invoca con `--elimina-originali`, e lo fa a una condizione sola: che la verifica appena eseguita sia risultata verde su ogni file della cartella, non sui soli file che sarebbero da cancellare. La collocazione non è un dettaglio di comodo ma il principio intorno a cui lo strumento è costruito, ed è scritto nel codice accanto alla riga che cancella:

```python
    # La cancellazione sta qui e non nella compressione per una ragione di ordine: il modo che
    # distrugge dev'essere lo stesso che ha appena dimostrato di poter fare a meno di ciò che
    # distrugge. Si cancella solo a verifica interamente verde, mai per i soli file passati.
```

La prima stesura aveva l'opzione `--elimina-originali` sul modo `comprimi`, ed era sbagliata per un motivo che si vede solo provando: dovendo rilanciare la compressione su una cartella già compressa, i file con il `.gz` accanto venivano saltati, e saltati significa che l'opzione di cancellazione non li avrebbe raggiunti mai. Una funzione distruttiva irraggiungibile è meno grave di una troppo facile da raggiungere, ma è comunque una funzione che non fa ciò che il suo nome promette.

Il modo `verifica` si rilancia in qualunque momento, anche fra un anno, e risponde alla domanda che conta: questa cartella contiene ancora, bit per bit, ciò che conteneva il giorno della compressione. Il codice di uscita è zero se ogni impronta corrisponde, uno se almeno una non corrisponde, due se l'invocazione è malformata o il manifesto manca.

## Come si è verificato

La norma in `.claude/skills/prove-che-misurano/RIFERIMENTO.md` chiede, prima di considerare chiusa una correzione, se la prova cadrebbe nel caso in cui il difetto tornasse. Una verifica di integrità è particolarmente esposta a questa domanda, perché una verifica che dice sempre di sì è indistinguibile da una che funziona finché non serve. Il controllo è stato eseguito su dati costruiti apposta, prima di puntare lo strumento sui file veri, in tre forme di guasto diverse.

Alterando un solo carattere dentro un file compresso, e ricomprimendolo in modo che resti un gzip perfettamente valido, la verifica ha risposto `GUASTO`, riportando le due impronte, con uscita 1. Invertendo un byte a metà del flusso compresso, cioè corrompendo il contenitore invece del contenuto, ha risposto `ILLEGGIBILE` con l'errore di CRC di gzip, sempre con uscita 1. Togliendo del tutto un file presente nel manifesto, ha risposto `ASSENTE` con uscita 1. Ripristinata la cartella, la verifica è tornata verde con uscita 0, il che esclude che il rosso dipendesse da uno stato sporco residuo invece che dal guasto.

Allo stesso modo è stata verificata la patch allo strumento di lettura, perché anche lì vale la domanda: che cosa prova che sia la patch a rendere leggibile il compresso, e non qualcos'altro. La versione precedente, recuperata dal commit con `git show HEAD:tools/read-chat-export.py`, messa davanti allo stesso file compresso muore con `json.decoder.JSONDecodeError: Expecting value: line 1 column 1`, perché tenta di interpretare come testo i byte compressi. La versione nuova lo legge. Su un export reale, filtrato per parola chiave, le due uscite prodotte dal file in chiaro e dal suo gemello compresso sono risultate identiche al confronto riga per riga, stesso numero di messaggi tenuti e stesso numero di caratteri scritti.

## L'esecuzione sui file veri

Il manifesto ha registrato 49 export per 2,58 GB. La compressione ne ha trattati 27, lasciando in chiaro i 22 che stanno sotto il megabyte, per un totale di 2,7 MB che non valeva la pena di sottrarre a un `grep`. Il rapporto per file va da 11,5x su `pret-pokered.json` a 27,6x sul canale degli ingressi di un server piccolo, e i canali più tecnici comprimono meno degli altri, il che è coerente con la spiegazione data sopra: dove il testo dei messaggi è lungo e vario la quota di impalcatura ripetuta è minore, quindi c'è meno da guadagnare. La cartella è passata da 2,5 GB a 181 MB misurati sul disco.

| file | prima | dopo | rapporto |
|---|---|---|---|
| `pret-pokeemerald.json` | 444,7 MB | 37,55 MB | 11,8x |
| `pret-pokecrystal.json` | 348,6 MB | 29,04 MB | 12,0x |
| `pret-pokered.json` | 294,4 MB | 25,56 MB | 11,5x |
| `GlitchCity-gen-1-glitches.json` | 206,6 MB | 11,48 MB | 18,0x |
| `pret-gen-3-help.json` | 181,2 MB | 14,16 MB | 12,8x |
| `GlitchCity-gen-3-glitches.json` | 175,8 MB | 10,22 MB | 17,2x |
| tutta la cartella | 2,58 GB | 186 MB | 13,9x |

La verifica indipendente, eseguita dopo la compressione e prima di qualunque cancellazione, ha riletto tutti e 49 gli export, decomprimendo i 27 compressi e leggendo direttamente i 22 in chiaro, e ha trovato ogni impronta uguale a quella del manifesto. Solo a quel punto gli originali sono stati rimossi, liberando 2,58 GB. La verifica rieseguita dopo la cancellazione è rimasta verde, il che è il controllo che conta davvero: significa che la prova non dipendeva dalla presenza degli originali, cioè che resta eseguibile da oggi in avanti.

L'ultima prova è stata di lettura e non di integrità, perché le due cose sono diverse e la seconda non implica la prima. Il file più grande della cartella, che in chiaro pesava 444 MB e ora non esiste più in quella forma, è stato aperto direttamente dal suo `.gz` e filtrato per parola chiave: 147 messaggi tenuti su 421.882 esaminati. Lo strumento non ha ricevuto nessuna opzione nuova e non sa di aver letto un file compresso.

## I difetti trovati eseguendo, e perché vanno raccontati

Quattro difetti sono emersi durante il lavoro, e nessuno sarebbe emerso leggendo il codice.

Il primo è stato nello script che applicava la patch: le sequenze di escape scritte in una stringa Python non raw si sono risolte in byte reali, e nel file è finito un carattere di controllo invisibile al posto del testo `\x1f`. Il risultato era un `SyntaxError` su una riga che a occhio sembrava corretta. Le due copie dello strumento sono tracciate, quindi `git checkout` le ha riportate allo stato committato senza conseguenze, e la patch è stata riscritta con le stringhe raw. La lezione utile è la dissimmetria che questo episodio illustra: lo stesso errore sui file di `_notes/` sarebbe stato irreversibile, perché lì git non c'è.

Il secondo è apparso solo sui dati veri. I canali esportati da un server il cui nome di canale contiene un'emoji producono file il cui nome contiene quell'emoji, e la stampa di quel nome sulla console di Windows, che apre in cp1252, muore con `UnicodeEncodeError` perché in cp1252 non esiste un punto di codice per un trofeo. Il difetto era di sola presentazione, il manifesto si scrive comunque in UTF-8, ma fermava lo strumento a metà cartella, che su quarantanove file significa uno stato parziale. La correzione è riconfigurare i flussi di uscita in UTF-8 all'avvio.

Il terzo è il difetto di collocazione della cancellazione, già descritto sopra. Il quarto è un conteggio: il riepilogo della verifica sommava i file compressi e quelli in chiaro, ma finché l'originale sta accanto al proprio compresso lo stesso export compare in entrambi gli elenchi, e la somma lo contava due volte. Si uniscono gli insiemi di nomi invece di sommare le cardinalità.

C'è poi un quinto episodio che non è un difetto dello strumento ma una sua guardia che ha funzionato. Durante il collaudo avevo lasciato nella cartella di prova una copia di un export reale non registrata nel manifesto; la verifica l'ha segnalata come `IGNOTO`, è fallita, e per effetto della regola sul verde totale ha rifiutato di cancellare qualunque originale. È il comportamento voluto: un file che la verifica non sa spiegare rende sospetta l'intera cartella, non solo sé stesso.

## Come estendere il pattern

Il pattern si riassume in una frase: un'operazione irreversibile su dati non riproducibili si accompagna a un artefatto che permette di dimostrarne l'innocuità anche molto dopo, e quell'artefatto resta nel progetto insieme allo strumento che lo sa leggere. Le tre parti sono tutte necessarie. Il manifesto da solo non serve se nessuno sa rigenerarlo nella stessa forma; lo strumento da solo non serve se il manifesto non è stato scritto prima della prima mutazione; e nessuno dei due serve se l'ordine fra verifica e distruzione non è imposto dal codice invece che dalla disciplina di chi lo lancia.

Applicato altrove nel progetto, questo significa che qualunque futura compressione, deduplicazione o riscrittura di materiale sotto `_notes/` dovrebbe passare per lo stesso schema, e che `tools/verifica-integrita-export.py` è generico abbastanza da reggerlo: lavora su una cartella, non su un formato, e l'unica cosa specifica agli export è la lista delle estensioni in testa al file.

Resta aperto un problema che questo intervento non affronta e che va scritto perché non si perda. Lo strumento di lettura esegue `json.load` sull'intero documento, quindi per aprire `pret-pokeemerald.json`, 444 MB, costruisce in memoria l'intero albero degli oggetti, che costa diversi gigabyte di memoria. La compressione non cambia questo costo, perché il flusso viene comunque decompresso e interpretato per intero. La strada che lo risolverebbe è la stessa che renderebbe i file otto volte più piccoli senza compressione, cioè la riscrittura in forma snella, con gli autori deduplicati e i campi inutili rimossi, possibilmente in forma di una riga JSON per messaggio da leggere in streaming. È una modifica al contenuto della fonte e va decisa a parte, con la stessa prova di equivalenza usata qui, confrontando però le uscite dello strumento di lettura invece delle impronte dei file.
