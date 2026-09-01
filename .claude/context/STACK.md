---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
  - pokemon-gen12-gen3-bridge-original-hardware/
  - gba-switch-pokemon-trading/
  - poke-automation-study/
  - recreate-pokemon-distributions-events/
  - poke-ace/
  - generation-from-switch/
last-verified-commit: 7696c46
---

# Stack

Questo progetto non ha ancora uno stack software nel senso consueto, e la parte più importante di questa scheda resta un inventario di hardware e di toolchain, perché è lì che stanno i vincoli reali e le scelte che sarebbe costoso rifare. Il codice però non è più un'ipotesi: dal 2026-08-25 esiste il pacchetto `pokebridge` del sottoprogetto del ponte, con i suoi moduli e la sua suite di prove, e la sezione delle dipendenze qui sotto lo tratta come esistente. Ciò che ancora manca è quanto fa di un insieme di moduli uno stack dichiarato, cioè un manifesto di dipendenze e una pipeline di build, e non manca per dimenticanza: il pacchetto sta deliberatamente sulla sola libreria standard. Quando il ponte sceglierà fra le quattro opzioni di ADR-008 questa scheda si sdoppierà con un profilo di stack vero e proprio, perché è quella decisione a introdurre una toolchain.

## Hardware

La console è un Old 3DS XL con seriale che inizia per SEH, partito dal firmware 11.17.0-50E, oggi su custom firmware, con una scheda SD da 32 GB formattata FAT32. Il lettore di cartucce Game Boy e Game Boy Advance è un GBxCart RW v1.4 Pro nella variante USB-C, colore blu, ordinato il 18 agosto 2026 con il cavo USB-A verso USB-C. Il gioco su cui si interviene per il bug dell'inventario gira su Game Boy Advance SP.

Il sesto track, cioè la ricreazione delle distribuzioni di eventi, aggiunge a questo inventario un fabbisogno che non è ancora accertato e che va accertato prima di pianificare qualunque cosa. La catena di trasferimento verso Pokemon Home richiede al primo passaggio un Nintendo DS o un DS Lite, perché il passaggio dalla terza alla quarta generazione avviene con la cartuccia Game Boy Advance inserita nello slot dedicato, che il 3DS non ha; al secondo passaggio richiede due apparecchi della famiglia DS accesi contemporaneamente, di cui uno può essere il 3DS. L'utente ha dichiarato il 2026-08-28 di possedere una console DS della prima o seconda revisione, quindi quel passaggio non è bloccato dall'hardware e la domanda materiale che il track aveva aperto è chiusa; il modello esatto non è registrato e non serve, perché entrambe le revisioni hanno lo slot. Resta invece da verificare la lingua delle cartucce, perché ogni passaggio della catena pretende la stessa lingua ai due capi e una discordanza si scopre al momento del trasferimento. Le vie di iniezione di un evento richiedono in alternativa un e-Reader, una scheda riprogrammabile o una cartuccia riscrivibile, oppure il solo lettore di cartucce già ordinato; esiste inoltre una via che passa da un GameCube con Game Boy Player e la sua interfaccia alternativa, hardware di cui non è registrata la disponibilità.

Per il sottoprogetto del ponte fra generazioni l'inventario hardware non è ancora stato fatto, ed è esattamente il motivo per cui quel track è fermo: quante console Game Boy Advance esistono, se c'è un GameCube o un Wii modificato, se c'è una flashcart, se c'è un cavo Link per Game Boy Color e se c'è la capacità di saldare sono le domande che decidono lo stack di quel sottoprogetto.

Il track del trading LDN aggiunge una console Nintendo Switch e un requisito che non ha equivalenti negli altri sottoprogetti: una scheda Wi-Fi capace di modalità monitor. È il fattore critico dichiarato, non un dettaglio, perché le schede USB esterne di fascia adatta risultano affidabili nei test degli autori del proof of concept, mentre alcune schede interne moderne sono fino alla metà più lente e possono andare in deadlock. Quale scheda ci sia su questa macchina non è ancora stato accertato, e da quella risposta dipende se il track sia praticabile. Lo stesso lettore GBxCart RW del track Smeraldo compare fra i requisiti, ma il materiale non spiega in quale fase entri.

## Toolchain

Sulla console vivono boot9strap come punto di ingresso del custom firmware, Luma3DS nella versione 13.4 come firmware, e GodMode9 come strumento di dump e di gestione dei file. MSET9 è stato usato una volta sola come exploit di installazione ed è stato rimosso a fine procedura. SEEDconv è servito a generare il file di seed necessario a decrittare le cartucce 3DS pubblicate dopo il 2014. Checkpoint è presente per la gestione dei salvataggi.

Sul PC, che è una macchina Windows 11, la catena del sottoprogetto Smeraldo è composta dai driver seriali CH340 e CH341, da FlashGBX per leggere e scrivere il salvataggio, dal runtime .NET 9 Desktop e da PKHeX come editor. La scelta di Windows non è una preferenza: PKHeX è un'applicazione .NET Windows Forms e il supporto a Mono e Wine è stato abbandonato dal 2023, quindi le alternative non sono equivalenti.

Il track del trading LDN ha due catene alternative, e la scoperta del 2026-08-26 è che la seconda cancella una tensione che il progetto considerava una decisione da prendere. La catena Linux, con Linux Mint come distribuzione suggerita anche solo da chiavetta avviabile, richiede Python in ambiente virtuale, l'utility di sistema per la gestione delle interfacce wireless, e le librerie `kinnay/LDN` e `frlg-ldn-trade`. La catena Windows richiede il demone `ldnd`, l'utilità Zadig per riassegnare l'adattatore al driver WinUSB, e l'archivio `linux-firmware` da tenere accanto all'eseguibile; non richiede alcuna macchina virtuale, perché `ldnd` si porta dietro il kernel Linux come libreria. Il progetto non ha quindi due sistemi operativi obbligati in tensione fra loro: il track LDN può stare sulla stessa macchina Windows del track Smeraldo, e la decisione fra dual boot e supporto avviabile decade. Il prezzo, che va tenuto presente, è che la via Windows funziona solo con adattatori USB e che dopo la riassegnazione a WinUSB quell'adattatore non fa più da scheda di rete.

Se il ponte fra generazioni prendesse la strada dell'hardware servirebbe devkitARM, mentre la strada del tool offline su PC porterebbe a Python, C# o Rust. Nessuna delle due è ancora stata scelta. I sottoprogetti destinati a produrre software sono ora due, il ponte e il trading LDN, ed è il segnale che rende sensato riaprire prima o poi il gate del server MCP di lettura del codice, oggi rimandato per ADR-010.

## Alternative deliberatamente escluse

Il percorso Action Replay per correggere l'inventario di Smeraldo è stato abbandonato dopo averlo studiato a fondo. Il Master Code e l'Anti-DMA erano verificati su più fonti indipendenti, ma per i codici della tasca Strumenti Base non esisteva alcuna fonte affidabile, e la scelta è stata di non indovinare indirizzi di memoria su un salvataggio irripetibile.

MSET9 è stato preferito ad altri punti di ingresso per il custom firmware per ragioni documentate nella sezione 4.1 dell'handoff del sottoprogetto 3DS, legate al firmware di partenza della console.

L'emulazione è esclusa per costruzione dal sottoprogetto del ponte, perché nessun emulatore replica fedelmente l'interazione elettrica fra Game Boy e Game Boy Advance, che è proprio il meccanismo su cui il ponte si regge. Per il sottoprogetto 3DS l'emulatore Azahar non è escluso ma solo rimandato: l'orientamento attuale è portare i file fisicamente via SD.

## Dipendenze di sviluppo aggiunte il 2026-08-25

Il progetto non aveva dipendenze esterne e ne ha ora una, dichiarata qui perché una dipendenza non scritta è una dipendenza che si riscopre rompendosi.

`yt-dlp`, installato con `python -m pip install --user yt-dlp`, versione 2026.08.19 alla prima installazione. Serve a scaricare i sottotitoli automatici dei video, che sono l'unica forma in cui una fonte video diventa citabile. La ragione per cui serve uno strumento dedicato invece di una richiesta HTTP è documentata in `.claude/rules/web-sources-not-fetchable.md`: la pagina del video si scarica, ma l'endpoint che serve i sottotitoli restituisce zero byte a qualunque richiesta che non provenga dal lettore vero. Si aggiorna con lo stesso comando e non ha configurazione.

Le due dipendenze implicite restano il Python di sistema, oggi 3.13, e `git`. Il pacchetto `pokebridge` e i suoi test non dipendono da nulla oltre alla libreria standard, ed è una scelta da mantenere.

## Macchina con GPU raggiungibile in rete locale

Esiste un secondo computer con GPU che espone Ollama all'indirizzo `http://192.168.20.58:11500`, raggiungibile direttamente in HTTP dalla rete locale senza tunnel. I modelli presenti alla verifica del 2026-08-25 sono `qwen3:14b`, `llama3.1:8b-instruct-q4_K_M`, `llama3.2:latest` e `bge-m3:latest`.

Va detto con precisione cosa quella macchina può e non può fare, perché il malinteso è facile. Non può trascrivere audio: nessuno dei modelli presenti è un riconoscitore vocale, e Ollama serve modelli di linguaggio, non modelli acustici. La trascrizione dei video resta compito di `yt-dlp`, che scarica i sottotitoli che YouTube ha già generato, e servirebbe un modello di famiglia Whisper soltanto per un audio senza sottotitoli.

Ciò che quella macchina può fare, ed è allineato alla regola di token economy del progetto, è condensare localmente fonti molto lunghe prima che entrino in conversazione: una trascrizione da un'ora di video o un thread di forum di duecento messaggi si riducono a una sintesi densa senza consumare contesto né pagare token. Il modello `bge-m3` è un modello di embedding, quindi abilita anche la ricerca semantica locale su tutto il corpus di `_notes/fonti/`, che diventerà utile quando quella cartella sarà cresciuta.

Nessuna di queste due cose è ancora implementata: sono possibilità registrate, e stanno fra le voci di `pending.md`.

## Pipeline di trascrizione delle fonti video

Esiste un progetto separato su questa macchina, `E:\local-audio-transcriptor`, che risolve il problema delle fonti video meglio di `yt-dlp` da solo e va usato al suo posto quando serve una trascrizione vera. È uno strumento locale basato su WhisperX con backend faster-whisper, con `yt-dlp` e ffmpeg già integrati, rilevamento automatico di GPU o CPU, diarizzazione di chi parla, indicizzazione a testo pieno su SQLite, risposta a domande sul corpus con citazioni, e sintesi strutturata via un endpoint compatibile con Ollama.

La forma d'uso prevista sarebbe una riga, `transcribe youtube "<url>" --summarize`, ma la prova del 2026-08-25 ha mostrato che il download dell'audio da YouTube risponde 403. La causa è dichiarata da yt-dlp stesso: manca un runtime JavaScript, che le versioni recenti richiedono per ricavare i formati audio, e senza quello alcuni formati non sono raggiungibili. Si risolverebbe installando `deno`, che è il runtime abilitato per default, ed è una decisione dell'utente perché aggiunge un componente alla macchina.

La via che invece funziona, provata e adottata, non tocca l'audio affatto, perché i sottotitoli automatici di YouTube sono già il risultato di un riconoscimento vocale fatto a monte. Sono due comandi.

```
python -m yt_dlp --skip-download --write-auto-subs --sub-langs "en.*" -o "%(id)s" URL
python tools/vtt-to-text.py ID.en.vtt --wrap 6 --out _notes/fonti/data-fonte.txt
```

Il secondo comando serve perché i sottotitoli automatici arrivano in forma scorrevole, dove ogni blocco ripete quasi interamente il precedente: convertiti ingenuamente producono un file tre o quattro volte più lungo del parlato. Lo strumento ricostruisce il testo una volta sola cercando la sovrapposizione fra blocchi consecutivi. Sul primo video provato, centosedici kilobyte di sottotitoli sono diventati dodici kilobyte di testo, cioè 2294 parole per dodici minuti di parlato.

Il progetto locale di trascrizione resta necessario per i video che non hanno sottotitoli automatici, e in quel caso fa il lavoro vero con il riconoscimento vocale sulla GPU.

Per la sintesi si punta l'endpoint alla macchina con GPU descritta sopra, configurando `TRANSCRIBE_LLM_BASE_URL` a `http://192.168.20.58:11500/v1` e `TRANSCRIBE_LLM_MODEL` a uno dei modelli presenti, per esempio `qwen3:14b`. In questo modo la trascrizione e la sua sintesi avvengono interamente in rete locale, e in conversazione entra la sintesi invece della trascrizione grezza: è l'applicazione diretta del principio di disclosure progressiva della regola di token economy.

Resta vero quanto scritto sopra sui limiti di Ollama, e questa pipeline lo conferma dividendo i compiti: il riconoscimento vocale lo fa WhisperX o YouTube a monte, la sintesi la fa il modello di linguaggio, e sono due mestieri diversi.

Sulla qualità di quella sintesi serve una calibrazione, ricavata dalla prima prova reale. Il modello locale ha condensato duemilatrecento parole di trascrizione in venti punti tecnici in pochi secondi, ed è stato utile per orientarsi, ma ha prodotto anche due affermazioni non sostenute dal testo, confondendo un numero di versioni e attribuendo al tool una portata che non ha. Ne segue una regola d'uso: l'uscita del modello locale vale come livello 4 nella gerarchia di `SOURCES.md`, cioè orienta e non si cita, e quando un suo punto conta va verificato sul testo originale, che resta su disco proprio per questo.

## Lettura delle chat di community

Le community su Discord sono, per alcune tecniche, la sola documentazione esistente, e un canale non è recuperabile né dal crawler del modello né da una richiesta HTTP. La via praticabile è l'export prodotto dall'utente, e su questa macchina lo strumento è `DiscordChatExporter` nella sua versione a riga di comando, che sta in `E:\[TBC] discord-chat-exporter`.

Va detto chiaramente il costo di quella via, perché è una decisione e non un dettaglio tecnico. Per esportare un canale di un server di cui si è membri, senza essere un bot, quello strumento richiede il token utente dell'account. Le condizioni d'uso di Discord non consentono l'uso automatizzato di un account personale, e l'esposizione è la sospensione dell'account. La scelta resta dell'utente; ciò che il progetto impone è che il token non entri mai in un file tracciato né in una conversazione, e che l'uso sia puntuale e non continuativo.

Il lato di questo progetto è `tools/read-chat-export.py`, che non tocca il token e lavora su un file già prodotto. Converte l'export in Markdown tenendo solo autore, momento, testo, allegati e indicazione delle risposte, e filtra per parola chiave, intervallo di date e lunghezza minima, che è il modo per togliere il rumore delle conversazioni brevi. Riconosce due formati dalla forma del documento e non dall'estensione: il JSON di DiscordChatExporter e il `result.json` dell'export di Telegram Desktop, dove il testo può essere una lista di frammenti formattati e viene ricomposto. L'esito va in `_notes/fonti/` come qualunque fonte procurata a mano, e da là si legge o si condensa con il modello locale.
