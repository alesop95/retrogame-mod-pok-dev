# Le fonti con codice, scheda per scheda

> Documento generato da `tools/schede-fonti-codice.py` dalle schede scritte leggendo README e metadati di ciascun repository, raccolti da `tools/raccogli-fonti-codice.py`. Non si modifica a mano: si correggono le schede e si rigenera. Il censimento con i dati di uso è `docs/censimento-fonti-codice.md`, il giudizio su che cosa ciascuna fonte può aggiungere agli strumenti è `docs/potenziamento-dalle-fonti.md`.

Repository descritti: 109, raggruppati per il primo track del progetto che li cita; quelli che il registro non associa a un track stanno in fondo. La riga dei metadati dice linguaggio, licenza, data dell'ultimo aggiornamento e stato, letti dall'API di GitHub il giorno della raccolta. Una scheda dice su che cosa poggia, e ciò che non ha potuto accertare è scritto, non taciuto.

## Pokédex completo in HOME (PKD)

### `architdate/PKHeX-Plugins`

https://github.com/architdate/PKHeX-Plugins · C# · licenza MIT · aggiornato 2024-05-08 · attivo · track EVT, PKD · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Plugin per PKHeX in C#, fra cui l'Auto Legality Mod, che automatizza la creazione di Pokémon legali.

Come funziona. Usa `PKHeX.Core` e l'interfaccia `IPlugin` di PKHeX; si compila con .NET 8.0 e le DLL (per esempio `AutoModPlugins.dll`) vanno copiate nella cartella `plugins` accanto a `PKHeX.exe`. Esiste anche una modalità di build con `PKHeX.Core` compilato dai sorgenti più recenti.

Relazione con il progetto. Riferimento per i track EVT e PKD su generazione e giudizio di legalità di esemplari con `PKHeX.Core`; secondo parere possibile sul nostro uso della libreria, che non lo usa direttamente.

Da verificare. L'ultimo push dichiarato nei metadati risale al 2024-05-08: lo stato di manutenzione rispetto alle versioni recenti di PKHeX non è accertato.

### `itsjavi/supereffective`

https://github.com/itsjavi/supereffective · TypeScript · licenza MIT · aggiornato 2026-09-22 · attivo · track PKD · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Sito web per tenere traccia del Pokédex e organizzare i box del Living Dex, ora PokéPC Classic, in modalità di bassa manutenzione.

Come funziona. Applicazione in TypeScript con Next.js 14 e React 18, gestita con pnpm e Turborepo, che richiede Docker per database e posta locali. Il README indica che i dati stanno in `src/lib/data-client` e che il sito sarà ritirato nel 2027 a favore di pokepc.net.

Relazione con il progetto. Fonte primaria per PKD sui dati di specie e forme del Living Dex e sull'organizzazione dei box; il progetto la usa già (`nel_codice` vero).

Da verificare. Il README non descrive il formato dei dati in `src/lib/data-client`.

### `kristopheles/monarium`

https://github.com/kristopheles/monarium · TypeScript · licenza MIT · aggiornato 2026-04-17 · attivo · track PKD · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Generatore e tracciatore di Pokédex personalizzabili, da ospitare in proprio, per tutti i giochi principali da Rosso/Blu a Legends Z-A più Pokémon HOME.

Come funziona. Scritto in TypeScript con Next.js e Drizzle, installabile come PWA e con funzionamento offline-first. Lo stato locale sta in IndexedDB, la sincronizzazione fra dispositivi usa un registro di operazioni con orologi di Lamport e una pipeline a eventi `SSE`. Offre un creatore guidato, oltre quindici filtri, tracciamento degli shiny ed esportazione JSON per Pokédex.

Relazione con il progetto. Strumento già usato dal progetto (nel_codice vero) per il track PKD, come tracciatore del completamento del Pokédex in HOME.

Da verificare. Ho letto solo le prime 45 righe del README: modello dei dati e istruzioni di installazione non sono stati accertati.

### `kwsch/PKHeX`

https://github.com/kwsch/PKHeX · C# · licenza NOASSERTION · aggiornato 2026-10-07 · attivo · track BRI, EVT, PKD, SME, TUTTI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Editor di salvataggi e di file di singoli Pokémon per i giochi principali della serie, con libreria di classi (`PKHeX.Core`) e interfaccia Windows Forms.

Come funziona. Scritto in C# per .NET 10, compilabile con qualunque compilatore C# 14 e senza codice specifico di piattaforma. Legge salvataggi (`*.sav`, `*.dsv`, `*.dat`, `*.gci`, `*.bin`), memory card GameCube, file di entità (`.pk*`, `*.ck3`, `*.xk3`, `*.pb7`, `*.sk2`, `*.bk4`, `*.rk4`) e Mystery Gift (`*.pgt`, `*.pcd`, `*.pgf`, `.wc*`), con conversione fra generazioni; importa ed esporta set di Pokémon Showdown e codici QR. Si aspetta salvataggi non cifrati con chiavi legate alla console. La licenza è la GNU GPL: lo dice il file `LICENSE` del repository, che l'API di GitHub classifica come `NOASSERTION` soltanto perché non ne riconosce il formato (verificato il 2026-10-07).

Relazione con il progetto. Strumento usato dal progetto (nel_codice vero): la libreria PKHeX.Core serve alla generazione e al giudizio di esemplari per PKD e EVT, e a lettura e verifica dei salvataggi per SME e BRI.

### `pokepc/classic.pokepc.net`

https://github.com/pokepc/classic.pokepc.net · TypeScript · licenza MIT · aggiornato 2026-09-22 · attivo · track PKD · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Sito web open source per tracciare il Pokédex e organizzare le box del living dex, già noto come SuperEffective.gg, ora in modalità di bassa manutenzione perché sostituito da pokepc.net.

Come funziona. Applicazione in TypeScript con Next.js 14 e React 18, autenticazione Next Auth, Prisma e PostgreSQL (Neon.tech) per i dati dei dex, ambiente locale con Docker; i dati statici sono un dataset JSON ospitato su GitHub, indicato nel README nella cartella `src/lib/data-client` del repository principale. Il README annuncia il ritiro di Classic nel corso del 2027. Licenza MIT.

Relazione con il progetto. Fonte già usata nel codice del progetto, per il track PKD: riferimento per l'organizzazione del living dex e per i dati delle specie e delle forme da completare in HOME.

Da verificare. Il README non descrive il contenuto né lo schema del dataset JSON; la scheda non dice quali campi il nostro strumento ne prenda.

### `pokepc/dataset`

https://github.com/pokepc/dataset · TypeScript · licenza MIT · aggiornato 2026-10-05 · attivo · track PKD · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Raccolta di dati statici JSON su Pokémon, giochi, Pokédex, mosse e abilità, con helper TypeScript e schemi Zod.

Come funziona. Pacchetto npm `@pokepc/dataset`: file JSON per Pokémon, testi per lingua sotto `data/i18n/`, schemi, descrizione OpenAPI e API statica su GitHub Pages in più versioni (v6, v7, v8). Licenza MIT.

Relazione con il progetto. Track PKD, già usato nel codice del progetto (nel_codice vero): fonte di dati su specie e Pokédex da confrontare con PKHeX.Core.

Da verificare. Il README non dice come siano stati ottenuti i dati: accuratezza non accertata.

### `pret/pokeruby`

https://github.com/pret/pokeruby · C · licenza - · aggiornato 2026-09-29 · attivo · track BRI, PKD, SME · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Decompilazione di Pokémon Rubino e Zaffiro per Game Boy Advance, del gruppo pret, in C.

Come funziona. Il repository ricostruisce il codice sorgente dei giochi e compila le ROM `pokeruby.gba` e `pokesapphire.gba`, con gli hash sha1 dichiarati nel README per verificare la corrispondenza byte per byte. Metadati: linguaggio C, argomenti decompilation, gameboy-advance, reverse-engineering.

Relazione con il progetto. Fonte primaria di strutture dati e layout della generazione 3 per i track BRI, PKD e SME, ed è già usata da uno strumento del progetto (nel_codice).

Da verificare. Il README è molto breve e rimanda a `INSTALL.md`: i formati trattati vanno cercati nel sorgente, non sono descritti qui.

### `sofianeelhor/PKForge`

https://github.com/sofianeelhor/PKForge · C# · licenza NOASSERTION · aggiornato 2026-10-04 · attivo · track PKD · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Editor di salvataggi Pokémon e banca multi-gioco per Android, pensato per console portatili a doppio schermo come l'AYN Thor, scritto in C# con MAUI e SkiaSharp.

Come funziona. È costruito su `PKHeX.Core` con l'Auto Legality Mod integrato, così la legalizzazione dei Pokémon avviene offline sul dispositivo. Apre salvataggi da emulatori collegati o da file singoli, sposta Pokémon fra giochi dalla generazione 1 alla 9 con anteprima delle modifiche e verdetto di legalità, e mantiene una Banca con tracciamento del living dex di 1025 specie.

Relazione con il progetto. Per il track PKD è un secondo parere possibile: realizza su Android funzioni vicine a quelle del completamento del Pokédex (living dex, legalizzazione, distribuzioni di eventi da database Mystery Gift incluso); non è usato dal nostro codice.

Da verificare. La licenza risulta NOASSERTION nei metadati mentre il README mostra un badge GPLv3: da accertare.

## Distribuzioni di eventi (EVT)

### `claydolwithexplosion/017f1784deebcd118b61d3ad917edb3c`

https://gist.github.com/claydolwithexplosion/017f1784deebcd118b61d3ad917edb3c · Assembly, Markdown · licenza - · aggiornato 2026-09-19 · gist · track ACE, EVT · non usato dal codice del progetto · scheda da solo metadati

Che cosa è. Gist di documentazione intitolato Pokemon Emerald ACE, sull'esecuzione arbitraria di codice in Pokémon Smeraldo per GBA.

Come funziona. Il gist contiene quattro file: `ace.md` (circa 69 KB), `creating_codes.md`, `techniques.md` e `legacy-base64.s` (assembly). Dai nomi si ricavano documentazione e tecniche per creare codici, ma il contenuto non è stato letto.

Relazione con il progetto. Fonte per i track ACE ed EVT sull'esecuzione di codice nei giochi e sulla generazione di esemplari o eventi per questa via; nessuno strumento del progetto lo usa ancora.

Da verificare. Nessun README nella cartella e i quattro file del gist non sono stati aperti: tecniche, formati e affidabilità non sono accertati.

### `Goppier/Gen3DistributionRoms`

https://github.com/Goppier/Gen3DistributionRoms · - · licenza - · aggiornato 2024-08-07 · attivo · track EVT · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Insieme di patch `.bps` per ricreare ROM di distribuzione di eventi per GBA, chiamato Project Wonder (JoySpot Update).

Come funziona. Contiene 10 patch da applicare con Flips a una ROM non modificata del Biglietto Aurora, per distribuire oggetti evento della generazione 3 (Biglietto Aurora, Biglietto Mistico e altri) e alcuni eventi nuovi. Funziona con due GBA e due adattatori wireless, o in emulatore, con una copia di Rosso Fuoco, Verde Foglia o Smeraldo; supporta sei lingue e le uova distribuite sono casuali.

Relazione con il progetto. Fonte primaria per EVT sulla ricreazione delle distribuzioni di eventi della generazione 3; il progetto la usa già (`nel_codice` vero).

Da verificare. Metadati senza descrizione, linguaggio e licenza. Il README non spiega il formato delle ROM né i dati degli eventi.

### `projectpokemon/EventsGallery`

https://github.com/projectpokemon/EventsGallery · - · licenza - · aggiornato 2026-09-06 · attivo · track EVT · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Galleria di eventi Pokémon raccolta dalla comunità di Project Pokémon: carte regalo e file di Pokémon di distribuzione.

Come funziona. È un archivio di file senza linguaggio di programmazione, da estrarre in una cartella `mgdb` accanto a `PKHeX.exe` o `SysBot.exe` per il controllo di legalità. Contiene wondercard e file di Pokémon, anche di Gen 3 e Gen 4 (con PGT convertiti in wondercard con dati segnaposto), e dati BCAT di Switch per Gen 8 e 9 come eventi raid e focolai di massa.

Relazione con il progetto. Fonte primaria per il track EVT sul catalogo degli eventi e per i dati di legalità di PKHeX, già usata dagli strumenti del progetto (nel_codice vero).

Da verificare. Licenza assente dai metadati. Il README non dice quanti eventi siano coperti né quali manchino, a parte il rimando a un elenco esterno per i wondercard di Gen 4.

### `superguideguy/gen-iii-event-patcher`

https://github.com/superguideguy/gen-iii-event-patcher · Java · licenza MIT · aggiornato 2021-02-12 · attivo · track BRI, EVT · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Programma Java che trasforma una ROM di generazione 3 in una ROM di distribuzione per eventi, o applica script di evento a un salvataggio.

Come funziona. Agisce su Rosso Fuoco, Verde Foglia e Smeraldo tramite Mystery Gift e su file di patch `.g3ep` (compreso `ultimate.g3ep`); include il pacchetto `g3sc`, un compilatore di script di evento. Per Rubino e Zaffiro il README dice che non è stato eseguito alcun test.

Relazione con il progetto. Track BRI ed EVT, già usato nel codice del progetto (nel_codice vero): fonte per la ricreazione di distribuzioni di eventi di Gen 3.

Da verificare. Il README stesso dice che parte della documentazione è stata cancellata e che la segnalazione errori è minima. Ultimo aggiornamento nel 2021.

### `Tyrrrz/DiscordChatExporter`

https://github.com/Tyrrrz/DiscordChatExporter · C# · licenza MIT · aggiornato 2026-10-02 · attivo · track BRI, EVT, LDN · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Programma che esporta la cronologia dei canali Discord in file, con interfaccia grafica e a riga di comando.

Come funziona. Scritto in C#, multipiattaforma. Si autentica con un token utente o di bot ed esporta in HTML, TXT, CSV e JSON, con markdown, allegati, incorporamenti ed emoji; ammette intervalli di date, filtri e suddivisione dei file. Il README avverte che automatizzare account utente viola i termini di Discord.

Relazione con il progetto. Strumento di acquisizione per le fonti conservate in canali Discord citate da BRI, EVT e LDN; il progetto lo usa già (`nel_codice` vero).

Da verificare. Il README non parla di Pokémon: l'uso specifico nel progetto non è accertabile da questa scheda.

## Salvataggio di Smeraldo (SME)

### `aarant/gen3tools`

https://github.com/aarant/gen3tools · Python · licenza - · aggiornato 2021-03-08 · attivo · track BRI, SME · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Raccolta di strumenti e appunti per TAS e analisi dei dati dei giochi Pokémon di terza generazione.

Come funziona. Contiene un editor grafico e uno strumento per l'RNG in Python con PyQt5, una libreria RNG (`seed.py`), strutture dati Python dei Pokémon (`pokemon.py`), script Lua per TAS e documenti con codici ACE per Smeraldo giapponese (`jpn.md`) e inglese (`us.md`). Il README stesso la definisce in gran parte disorganizzata.

Relazione con il progetto. Fonte per BRI e SME su struttura dei dati, RNG e codici ACE della generazione 3; non è usata da uno strumento del progetto (`nel_codice` falso) e può servire da confronto con i nostri.

Da verificare. Licenza assente nei metadati; ultimo push nel 2021. Il contenuto dei documenti ACE non è stato verificato.

### `ads04r/Gen3Save`

https://github.com/ads04r/Gen3Save · Python · licenza Unlicense · aggiornato 2019-10-09 · attivo · track BRI, SME · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Libreria Python per leggere un file di salvataggio Pokémon di generazione 3 (Game Boy Advance).

Come funziona. È in sola lettura, con le classi `Gen3Save` e `Gen3Pokemon`: espone `team`, `boxes` e proprietà come `name`, `level`, `species`, `nature`, `moves`, `exp`, e `data` con i dati decifrati salvabili come `.pkm`. Si basa sulle pagine di Bulbapedia sulla struttura dei dati di Gen 3.

Relazione con il progetto. Track BRI e SME, non usata nel codice (nel_codice falso): possibile secondo parere sul nostro lettore di salvataggi Gen 3.

Da verificare. La proprietà `ivs` è dichiarata incompiuta dall'autore. Ultimo aggiornamento nel 2019.

### `binarycounter/PkSploit`

https://github.com/binarycounter/PkSploit · Python · licenza MIT · aggiornato 2017-11-24 · attivo · track BRI, SME · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Suite di strumenti in Python e per Arduino che sfrutta un difetto di Pokémon Gen 1 per eseguire codice e fare dump di ROM e SRAM, e scrittura di SRAM, su cartucce Game Boy e Game Boy Color tramite cavo link.

Come funziona. Un microcontrollore Arduino compatibile finge di essere un secondo Game Boy in scambio e invia dati della squadra corrotti, che la console esegue come codice: circa 192 byte che riaprono il collegamento seriale e danno accesso in lettura e scrittura alla memoria. Eseguendo in WRAM, con lo scambio della cartuccia si può leggere o scrivere un'altra cartuccia; il README descrive anche la riscrittura della ROM su bootleg con memoria flash tramite i comandi della flash. Richiede Python 2.7, PySerial, l'IDE Arduino e RGBDS, ed è basato su un exploit e un codice Arduino di vaguilar/pokemon-red-cable-club-hack. Licenza MIT.

Relazione con il progetto. Fonte già usata nel codice del progetto, per i track BRI e SME: riferimento principale per l'esecuzione di codice via cavo link in Gen 1 e per il protocollo seriale con un microcontrollore al posto di una seconda console.

Da verificare. Il README si dichiara in forte sviluppo, con la funzione di flash dei bootleg poco provata e la sezione di costruzione hardware ancora da scrivere; la scheda non ha verificato il protocollo seriale effettivo.

### `crumblingstatue/rgen3`

https://github.com/crumblingstatue/rgen3 · Rust · licenza MIT · aggiornato 2025-03-22 · attivo · track BRI, SME · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Suite di librerie e utilità in Rust per manipolare i giochi Pokémon di generazione 3 (Rosso Fuoco, Verde Foglia, Rubino, Zaffiro, Smeraldo).

Come funziona. Comprende `rgen3-save`, una libreria per leggere e modificare i salvataggi (con un esempio `fill-pc.rs` che riempie i box di Pokémon casuali), e `rgen3-string`, che codifica e decodifica il formato di stringhe proprietario della generazione 3. Il README dichiara come fonte quasi esclusiva la pagina di Bulbapedia sulla struttura dei dati di salvataggio.

Relazione con il progetto. Secondo parere possibile sui nostri strumenti di lettura dei salvataggi di generazione 3 per i track BRI e SME; nessuno strumento del progetto lo usa.

### `E-Sh4rk/PokeGlitzer`

https://github.com/E-Sh4rk/PokeGlitzer · C# · licenza - · aggiornato 2025-04-26 · attivo · track ACE, SME · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Editor di salvataggi di generazione 3 in C# per chi lavora con i glitch, con modifica dei dati grezzi.

Come funziona. Gira su .NET 8 (Windows consigliato, anche Linux e macOS). Legge e modifica squadra, box e nomi dei box per Smeraldo, Rubino e Zaffiro, Rosso Fuoco e Verde Foglia, e può sincronizzarsi con Bizhawk tramite uno script Lua (`Misc/bizhawk_synchronize_*.lua`, solo Windows, script per Smeraldo US e JP).

Relazione con il progetto. Track ACE e SME, non usato nel codice (nel_codice falso): possibile secondo parere sulla struttura dei dati di Gen 3 e sul comportamento dei box.

Da verificare. Nei metadati non c'è licenza. Il README stesso rimanda a PKHeX per l'editing ordinario.

### `haven1433/HexManiacAdvance`

https://github.com/haven1433/HexManiacAdvance · C# · licenza MIT · aggiornato 2026-08-30 · attivo · track BRI, SME · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Editor per i giochi Pokémon GBA, con editor esadecimale e strumenti dedicati a tabelle, testi, script, immagini, mappe e Pokédex.

Come funziona. Programma in C# che riconosce in modo specifico le edizioni inglesi di Rubino, Zaffiro, Rosso Fuoco, Verde Foglia e Smeraldo, e con altri file offre un insieme ridotto di funzioni. Oltre alle funzioni di un editor esadecimale (visualizzazione, modifica, copia, confronto) offre modifica di Pokémon, allenatori, mosse e strumenti, di mappe, testi con riposizionamento automatico dei puntatori, immagini, script di evento e codice thumb, esportazione di backup e creazione di patch `.ips` e `.ups`. Licenza MIT.

Relazione con il progetto. Non usato nel codice del progetto; per i track BRI e SME è un possibile secondo parere sulla struttura dei dati nelle ROM e nei salvataggi Gen 3, da confrontare con i nostri strumenti.

Da verificare. Il README parla di ROM e dati di gioco, non dichiara in modo esplicito la lettura dei file di salvataggio; non verificato.

### `lesserkuma/FlashGBX`

https://github.com/lesserkuma/FlashGBX · Python · licenza GPL-3.0 · aggiornato 2026-09-08 · attivo · track BRI, SME · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Programma in Python per leggere e scrivere cartucce Game Boy e Game Boy Advance, con interfaccia per Windows, Linux e macOS.

Come funziona. Esegue backup e ripristino dei salvataggi (inclusi i registri RTC), backup delle ROM e scrittura su flashcart, con rilevamento automatico di molte cartucce e interrogazione dei chip flash tramite Common Flash Interface. Supporta lettori come GBxCart RW, GBFlash, Joey Jr e Game Bub e numerosi mapper (MBC1, MBC2, MBC3, MBC5 e altri).

Relazione con il progetto. Strumento usato dal track SME per estrarre il salvataggio di Smeraldo dalla cartuccia posseduta, e rilevante anche per BRI; è già usato dal progetto (nel_codice).

### `mrhappyasthma/NDSEventTool.nds`

https://github.com/mrhappyasthma/NDSEventTool.nds · C++ · licenza GPL-2.0 · aggiornato 2020-01-28 · fork · track SME · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Homebrew per Nintendo DS, fork di un progetto precedente, che inietta eventi ufficiali Nintendo (mystery gift) nei salvataggi dei giochi Pokémon per GBA presenti nella cartuccia.

Come funziona. Scritto in C++ con la toolchain devkitPro e compilato con `make`; deriva da nds-savegame-manager di Pokedoc, strumento homebrew per estrarre e ripristinare i salvataggi di giochi DS e GBA. Il README dichiara che lavora sulle cartucce GBA inserite nella console e raccomanda un backup preventivo con lo strumento originale; non descrive il formato dei dati degli eventi. Licenza GPL-2.0.

Relazione con il progetto. Strumento già usato nel codice del progetto, per il track SME: fonte primaria su come scrivere un evento nel salvataggio di una cartuccia GBA agendo da una console DS.

Da verificare. Il README non dice quali giochi e quali eventi siano supportati né come sia codificato l'evento nel salvataggio.

### `ncorgan/pksav`

https://github.com/ncorgan/pksav · C · licenza MIT · aggiornato 2021-11-15 · archiviato · track BRI, SME · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Libreria C per leggere e manipolare i file di salvataggio dei Pokémon, archiviata.

Come funziona. Scritta in C puro senza dipendenze esterne, pensata come nucleo interno di librerie più grandi e richiamabile da C++, Objective-C, C# o Java. Supporta solo salvataggi americani. Lo stato dichiarato nel README, aggiornato al 2018-03-25, è completo per Generazione I, II e GBA, e in corso per le Generazioni IV, V, VI e VII. I test usano il framework Unity.

Relazione con il progetto. Nessuno strumento del progetto la usa (nel_codice falso): è un secondo parere possibile sul layout dei salvataggi Gen 1-3 per i track BRI e SME.

Da verificare. Il repository è archiviato e fermo al 2021, e copre solo salvataggi americani: lo stato attuale delle generazioni indicate come in corso non è accertato.

### `pret/pokeemerald`

https://github.com/pret/pokeemerald · C · licenza - · aggiornato 2026-10-01 · attivo · track BRI, SME · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Decompilazione di Pokémon Smeraldo per Game Boy Advance, mantenuta dal progetto pret.

Come funziona. Il repository è scritto in C e ricostruisce la ROM `pokeemerald.gba`, di cui il README indica lo sha1 di riferimento. Le istruzioni di preparazione dell'ambiente stanno in `INSTALL.md`, che non è stato letto.

Relazione con il progetto. Fonte primaria di riferimento sul codice del gioco per i track SME e BRI, e già usata dagli strumenti del progetto (nel_codice vero).

Da verificare. Il README è molto breve: struttura delle cartelle, layout del salvataggio e formati di dati non sono descritti e non sono stati accertati. Licenza assente dai metadati.

### `pret/pokeemerald.wiki`

https://github.com/pret/pokeemerald.wiki · non raccolto · licenza - · aggiornato - · - · track BRI, SME · non usato dal codice del progetto · scheda da clone locale

Che cosa è. Wiki di documentazione del progetto di decompilazione `pokeemerald` (Pokémon Smeraldo), con guide, tutorial e spiegazioni del motore di gioco della terza generazione.

Come funziona. Raccolta di pagine Markdown, non codice. La pagina principale indica sezioni sul funzionamento del motore della generazione 3 (`How the Game Works`), tutorial per modificare o estendere il gioco, strumenti di modding utili e rami di funzionalità. Nel clone locale il working tree risulta vuoto e le pagine sono leggibili solo dalla storia di git.

Relazione con il progetto. Riferimento tecnico per SME e BRI sul funzionamento interno del gioco della generazione 3; non è usato da uno strumento del progetto (`nel_codice` falso).

Da verificare. Raccolta dell'API assente (nessun `repo.json`): licenza, linguaggio e date non accertati. Letta solo la pagina `Home.md` dalla storia git del clone; il contenuto delle singole pagine non è stato esaminato.

### `pret/pokefirered`

https://github.com/pret/pokefirered · C · licenza - · aggiornato 2026-09-26 · attivo · track BRI, LDN, SME · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Decompilazione in C di Pokémon Rosso Fuoco e Verde Foglia (versione inglese) per Game Boy Advance, mantenuta dal gruppo pret.

Come funziona. Il codice è in C e ricostruisce sei immagini ROM verificate con sha1: le due versioni base, le due `rev1` e le due `switch`. Il README non descrive formati di dati e rimanda a `INSTALL.md` per la compilazione.

Relazione con il progetto. Fonte primaria per i track BRI, LDN e SME su strutture e comportamento di Gen 3 in Rosso Fuoco e Verde Foglia, già usata nel codice del progetto (nel_codice vero).

Da verificare. Il README è molto breve e non parla di salvataggio, multiboot o scambio: la pertinenza ai tre track non deriva dal testo letto. Nessuna licenza dichiarata.

### `taxicat1/DomeAssistantWeb`

https://github.com/taxicat1/DomeAssistantWeb · HTML · licenza MIT · aggiornato 2024-09-13 · attivo · track SME · usato dal codice del progetto · scheda da solo metadati

Che cosa è. Applicazione web in HTML, con licenza MIT, il cui scopo preciso non è dichiarato nei metadati.

Come funziona. Il linguaggio principale indicato è HTML, quindi si tratta di una pagina o di un piccolo sito eseguito nel browser. Metadati e README non dicono altro su formati o tecniche.

Relazione con il progetto. Il track SME lo cita e un nostro strumento lo usa già (nel_codice), ma i metadati non permettono di precisare in che modo serva alla correzione del salvataggio di Smeraldo.

Da verificare. README assente e descrizione vuota: non è accertato che cosa faccia l'applicazione, per quale gioco e con quali dati; va letto il codice sorgente o la pagina pubblicata.

## Ponte fra generazioni su hardware originale (BRI)

### `adanscotney/gameboy-spoof`

https://github.com/adanscotney/gameboy-spoof · non raccolto · licenza - · aggiornato - · - · track BRI · usato dal codice del progetto · scheda da clone locale

Che cosa è. Repository di codice per Game Boy, privo di README e di cartella di raccolta, legato a Pokémon (unico indizio testuale: il file `pokemon.h`).

Come funziona. Il clone contiene una cartella `stellaris` con `gameboy.c`, `pokemon.h`, `startup_gcc.c`, `linker.ld`, `uartstdio.c` e `ustdlib.c`, quindi codice C per una scheda della famiglia Stellaris con script di linker e UART. Contiene anche una cartella `pokemon-maker` con `pom.xml` e `src` (progetto Maven) e il file `example_data_block.txt`.

Relazione con il progetto. Track BRI, già usato nel codice del progetto (nel_codice vero): riferimento per simulare un Game Boy sul cavo link, ma questo scopo non è confermato da alcuna descrizione della fonte.

Da verificare. Mancano README e metadati (cartella di raccolta vuota): scopo, piattaforma esatta e formato di `example_data_block.txt` non sono accertati. Sono stati letti solo l'elenco dei file e il messaggio dell'ultimo commit.

### `Admiral-Fish/RNGReporter`

https://github.com/Admiral-Fish/RNGReporter · C# · licenza GPL-2.0 · aggiornato 2018-09-23 · archiviato · track BRI · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Strumento per Windows sull'RNG dei giochi Pokémon, archiviato, derivato da RNGReporter di mingot, Slashmolder e OmegaDonut.

Come funziona. Scritto in C#. Il README elenca le funzioni aggiunte: calcolatore RTC GameCube, conversione da seed a 16 bit a orario, `GameCubeRNG`, da PID a IV, Pokespot, da IV a frame, ricerca di distribuzioni per Pokémon statici e selvatici di Gen 3 ed uova FRLG. L'autore dichiara di non lavorarci più e rimanda a PokeFinder.

Relazione con il progetto. Nessuno strumento del progetto lo usa (nel_codice falso): è un riferimento possibile per il track BRI sulla manipolazione del generatore di numeri casuali di Gen 3.

Da verificare. Il README è un elenco di funzioni senza spiegazione degli algoritmi. Repository archiviato e fermo al 2018.

### `afska/gba-link-connection`

https://github.com/afska/gba-link-connection · C++ · licenza MIT · aggiornato 2026-08-01 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Insieme di librerie C++ per Game Boy Advance che gestiscono la porta seriale per dare supporto multigiocatore agli homebrew, con binding in C.

Come funziona. Le librerie sono file header (`LinkCable.hpp`, `LinkCableMultiboot.hpp`, `LinkSPI.hpp`, `LinkUART.hpp`, `LinkWireless.hpp`, `LinkCube.hpp` e altri) da copiare nella cartella `lib/` del proprio progetto, compilabili solo con GCC. Coprono la modalità Multi-Play a 16 bit, l'invio di ROM multiboot da 256 KiB, l'adattatore wireless, Joybus verso GameCube e Wii, SPI e UART.

Relazione con il progetto. Fonte per il track BRI su cavo link e multiboot GBA; è già usata da uno strumento del progetto (nel_codice).

### `CableClub/cable-link`

https://github.com/CableClub/cable-link · XSLT · licenza NOASSERTION · aggiornato 2021-09-06 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Progetto di hardware e firmware per un cavo link GB/GBA.

Come funziona. I metadati indicano il linguaggio `XSLT` e i topic `gameboy`, `gba` e `kicad`, il che fa pensare a schemi e circuiti stampati in KiCad. Il README contiene soltanto il titolo e un'immagine.

Relazione con il progetto. Fonte per il track BRI sull'hardware del cavo link, già citata dagli strumenti del progetto (nel_codice vero).

Da verificare. Il README è praticamente vuoto: architettura del firmware, microcontrollore e protocolli non sono accertati. Licenza `NOASSERTION`. Ultimo push nel 2021.

### `devkitPro/libtonc`

https://github.com/devkitPro/libtonc · C · licenza - · aggiornato 2025-05-12 · attivo · track BRI · non usato dal codice del progetto · scheda da solo metadati

Che cosa è. Repository in linguaggio C della famiglia devkitPro; i metadati non danno una descrizione, e la scheda non può dire altro con certezza.

Come funziona. Il solo dato disponibile è il linguaggio principale, C. README, descrizione, argomenti e licenza sono assenti nella raccolta, quindi architettura e formati non sono accertabili.

Relazione con il progetto. Citata per il track BRI e non usata nel codice del progetto: possibile dipendenza o riferimento per codice GBA, da confermare, senza relazione diretta accertata.

Da verificare. README assente e descrizione vuota: scopo, piattaforma di destinazione e licenza non accertati.

### `FIX94/gba-link-cable-rom-sender`

https://github.com/FIX94/gba-link-cable-rom-sender · C · licenza MIT · aggiornato 2018-12-15 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Homebrew per GameCube e Wii che invia ROM `.gba` multiboot a un GBA tramite il cavo link GameCube-GBA.

Come funziona. Scritto in C. Legge i file multiboot `.gba` da una cartella `gba` su SD Gecko (GameCube) o su SD/USB (Wii), con limite di 256 KB, e li trasferisce al GBA collegato alla porta 2 premendo A.

Relazione con il progetto. Fonte per il track BRI sul multiboot GBA via cavo link, già usata dagli strumenti del progetto (nel_codice vero).

Da verificare. Il README non descrive il protocollo di trasferimento: serve leggere il sorgente.

### `gbadev-org/awesome-gbadev`

https://github.com/gbadev-org/awesome-gbadev · - · licenza NOASSERTION · aggiornato 2026-01-30 · attivo · track BRI · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Elenco curato di risorse per lo sviluppo su Game Boy Advance: documentazione, compilatori, toolkit, librerie, emulatori e homebrew.

Come funziona. Documento Markdown con un indice che copre introduzione e comunità, tutorial e articoli, compilatori, toolkit, librerie ed emulatori, sviluppo di emulatori e test, homebrew, e sezioni varie fra cui il dump del BIOS e il reverse engineering. Non contiene codice proprio; ha una versione web su gbadev.net. Licenza indicata come NOASSERTION.

Relazione con il progetto. Non usato nel codice del progetto; indice di riferimento per il track BRI, utile a trovare documentazione e strumenti GBA, senza essere una fonte tecnica diretta.

Da verificare. La scheda non ha seguito i collegamenti dell'elenco, quindi non dice quali risorse servano al track.

### `gbdev/awesome-gbdev`

https://github.com/gbdev/awesome-gbdev · - · licenza GPL-3.0 · aggiornato 2026-10-03 · attivo · track BRI · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Elenco curato di risorse per lo sviluppo Game Boy e Game Boy Color: documentazione, emulatori, assemblatori, compilatori, strumenti e ROM open source.

Come funziona. È un documento Markdown senza codice, organizzato in sezioni (Documentazione, Sviluppo di emulatori, Strumenti, Programmazione in ASM, Hardware, Cartucce e altre). Rimanda a una versione web su `gbdev.github.io/resources`.

Relazione con il progetto. Fonte di consultazione per il track BRI, per trovare documentazione su hardware, porta seriale e cartucce Game Boy; nessuno strumento del progetto lo usa.

### `gbdev/pandocs`

https://github.com/gbdev/pandocs · Markdown · licenza CC0-1.0 · aggiornato 2026-10-02 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Documentazione tecnica di riferimento sull'hardware del Game Boy, mantenuta in Markdown.

Come funziona. Repository di sola documentazione (licenza CC0-1.0), pubblicata su `gbdev.io/pandocs`. Il README riporta che il documento nasce nel 1995 e descrive il processo di contributo e di build locale, ma non elenca gli argomenti trattati.

Relazione con il progetto. Riferimento per BRI su hardware e comportamento del Game Boy, comprese le porte seriali; il progetto lo usa già (`nel_codice` vero).

Da verificare. Il README non elenca i capitoli: la presenza delle porte seriali e del protocollo link non è accertata da README e metadati.

### `gbdev/rgbds`

https://github.com/gbdev/rgbds · C++ · licenza MIT · aggiornato 2026-10-04 · attivo · track BRI · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Pacchetto di assemblatore e linker per Game Boy e Game Boy Color (Rednex Game Boy Development System).

Come funziona. Scritto in C++, si compila con `make` o con `cmake`. È composto da quattro strumenti: `RGBASM` (assemblatore), `RGBLINK` (linker), `RGBFIX` (correzione di checksum e header della ROM) e `RGBGFX` (conversione da PNG a grafica Game Boy). La documentazione è generata dalle pagine man del repository.

Relazione con il progetto. Nessuna relazione diretta con un nostro strumento (nel_codice falso): è la toolchain con cui si ricostruiscono le ROM dei disassemblati pret, quindi serve al track BRI come supporto per costruire e provare codice per Game Boy.

Da verificare. Il README non dice se i disassemblati pret richiedano una versione precisa di RGBDS: va letto `INSTALL.md` di pokegold.

### `Goppier/GEN3PokemonDistributions`

https://github.com/Goppier/GEN3PokemonDistributions · - · licenza - · aggiornato 2025-12-01 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Raccolta di istruzioni per ricevere distribuzioni di Pokémon Gen 3 tramite cavo link fra due GBA, con una cartuccia di distribuzione su flashcard o emulatore.

Come funziona. Il README descrive la procedura: la console ricevente con Rubino, Zaffiro, Smeraldo, Rosso Fuoco o Verde Foglia viene accesa tenendo premuti Start e Select per far partire il trasferimento multiboot, mentre la console mittente porta la cartuccia di distribuzione, con il lato master del cavo sulla console mittente. Servono due GBA, un cavo originale e la lingua della cartuccia coerente con quella della distribuzione. Linguaggio e licenza non risultano dai metadati.

Relazione con il progetto. Fonte già usata nel codice del progetto, per il track BRI: descrive il meccanismo di ricezione di distribuzioni su hardware originale via cavo link, utile al confronto con il nostro ponte.

Da verificare. Il README è una procedura d'uso: non dice quali distribuzioni contenga il repository né i formati dei dati; descrizione e licenza assenti nei metadati.

### `Lorenzooone/Pokemon-Gen3-to-Gen-X`

https://github.com/Lorenzooone/Pokemon-Gen3-to-Gen-X · C · licenza MIT · aggiornato 2026-08-30 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Homebrew per GBA, avviabile da flashcart o in multiboot, che scambia Pokémon fra la generazione 3 (Rubino, Zaffiro, Smeraldo, Rosso Fuoco, Verde Foglia) e i giochi di generazione 1 e 2.

Come funziona. Scritto in C per GBA. Comunica con il Game Boy tramite il cavo link DMG/GB/GBC (non compatibile con quello GBA) e può inviare sé stesso ad altre console con `Send Multiboot`. Il README dice che lo scambio fra generazioni perde dati (per esempio i nastri) e che si può scambiare anche fra GBA con lo stesso software; offre inoltre impostazioni dell'orologio per Rubino, Zaffiro e Smeraldo anche a pila esaurita.

Relazione con il progetto. Fonte primaria e strumento già in uso per BRI (ponte fra generazioni 1-2 e 3 su hardware originale); il suo trattamento dell'orologio con pila secca è pertinente anche a BAT, ma il campo `track` indica solo BRI.

Da verificare. Il README non descrive il protocollo di link né i formati interni: restano da leggere nel sorgente.

### `Lorenzooone/PokemonGB_Online_Trades`

https://github.com/Lorenzooone/PokemonGB_Online_Trades · Python · licenza MIT · aggiornato 2026-08-28 · attivo · track BRI, LDN · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Programma Python che aggiunge scambi e lotte online a Pokémon Rosso, Blu, Giallo, Oro, Argento e Cristallo, e scambi online a Rubino, Zaffiro, Smeraldo, Rosso Fuoco e Verde Foglia.

Come funziona. Scritto in Python 3.6.1 o successivo, offre due interfacce: un adattatore da cavo link GB a USB (`usb_trade_battle.py`) e l'emulatore BGB (`emulator_trade_battle.py`). Funziona in modalità sincronizzata, con un byte alla volta come il cavo originale, o in modalità con buffer, e applica controlli di sanità sui byte inviati alla console. Per la Gen 3 si appoggia al progetto Pokemon-Gen3-to-GenX, avviato con multiboot.

Relazione con il progetto. Fonte primaria per il track BRI sul protocollo del cavo link e sul multiboot, citata anche da LDN, e già usata dagli strumenti del progetto (nel_codice vero).

Da verificare. Il README non descrive il protocollo server né i formati dei dati scambiati: serve leggere il sorgente.

### `MrCheeze/pokestadium-ace`

https://github.com/MrCheeze/pokestadium-ace · Python · licenza - · aggiornato 2018-09-02 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Note e codice sull'esecuzione di codice arbitrario in Pokémon Stadium per Nintendo 64.

Come funziona. Il README spiega che l'exploit richiede prima l'esecuzione di codice in Pokémon Rosso, Blu o Giallo per manipolare il salvataggio Game Boy, due controller N64 con due Transfer Pak e due giochi, entrambi salvati in un Centro Pokémon. Nello scambio i box vengono convertiti dal formato R/B/Y a quello di Stadium e posti a indirizzi di memoria elencati, con strutture di Pokémon da `0x54` byte i cui campi sono documentati. Il codice è in Python.

Relazione con il progetto. Fonte per il track ACE sulla tecnica di esecuzione di codice e per BRI sul formato dei Pokémon di Gen 1 in Stadium, già usata dagli strumenti del progetto (nel_codice vero).

Da verificare. Ho letto solo le prime 70 righe del README: la parte restante delle strutture e il payload non sono stati accertati. Repository senza licenza e fermo al 2018.

### `pepijndevos/arduino-boy`

https://github.com/pepijndevos/arduino-boy · Arduino · licenza NOASSERTION · aggiornato 2020-06-11 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Sketch Arduino che emula un Game Boy per scambiare un Pokémon memorizzato in EEPROM con un Game Boy reale.

Come funziona. Sketch per Arduino che conserva un solo Pokémon in EEPROM e lo scambia via link con i giochi della prima generazione. Il README dice che il codice deriva in buona parte da `gameboy-spoof` e che dovrebbe funzionare con la maggior parte delle schede Arduino.

Relazione con il progetto. Fonte per BRI sul protocollo di scambio del cavo link emulato da microcontrollore; il progetto la usa già (`nel_codice` vero).

Da verificare. Licenza indicata come `Other`. Il README è molto breve: il protocollo e le generazioni supportate non sono documentati.

### `Phasip/PokemonLinkHack`

https://github.com/Phasip/PokemonLinkHack · Python · licenza - · aggiornato 2023-01-09 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Raccolta di script Python e programmi assembly per comunicare via cavo link con Pokémon Rosso e Blu (generazione 1) su Game Boy classico.

Come funziona. Gli script girano su Python 3 e scelgono un backend con un argomento: `pi` (porta SPI di Raspberry Pi), `bp` (Bus Pirate) o `no` (collegamento dell'emulatore BGB). Il README include la piedinatura del cavo link e rimanda a un articolo dell'autore.

Relazione con il progetto. Track BRI, già usato nel codice del progetto (nel_codice vero): riferimento per il collegamento fisico via cavo link da un microcontrollore o da un computer.

Da verificare. Per scelta di prudenza la scheda non riporta il funzionamento delle tecniche descritte nel README: va riletto direttamente se serve.

### `pret/pokecrystal`

https://github.com/pret/pokecrystal · Assembly · licenza - · aggiornato 2026-10-06 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Decompilazione, in forma di disassemblato, di Pokémon Versione Cristallo per Game Boy Color.

Come funziona. Sorgente in assembly per il processore GBZ80, con il progetto che ricostruisce le ROM originali a partire dai sorgenti e ne verifica l'identità tramite hash `sha1`; il README elenca fra le build le versioni UE 1.0 e 1.1, quella australiana e alcune immagini di prototipo. Le istruzioni di installazione stanno in `INSTALL.md`, la documentazione e i simboli in risorse collegate.

Relazione con il progetto. Fonte già usata nel codice del progetto, per il track BRI: riferimento a livello di sorgente per i formati e il comportamento di Gen 2 sul lato del ponte con la Gen 3.

Da verificare. Il README non entra nei formati dei dati di salvataggio o di scambio; per quelli occorre leggere i sorgenti, che questa scheda non ha aperto. Il metadato di licenza risulta assente.

### `pret/pokegold`

https://github.com/pret/pokegold · Assembly · licenza - · aggiornato 2026-10-06 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Disassemblato di Pokémon Oro e Argento per Game Boy Color, mantenuto dal progetto pret.

Come funziona. Il codice è in assembly Game Boy (sm83/gbz80) e ricostruisce le ROM `.gbc` di Oro e Argento, due immagini di debug (`mons2_gld_ps3_debug.bin`, `mons2_slv_ps3_debug.bin`) e due file `.patch`, tutti elencati con sha1 nel README. Rimanda a un ramo `symbols` e agli strumenti di `gb-asm-tools`.

Relazione con il progetto. Fonte primaria sul codice e sui formati di Gen 2 per il track BRI, già usata dagli strumenti del progetto (nel_codice vero).

Da verificare. Il README non descrive i formati di dati né il modo di scambio via cavo: serve leggere il sorgente. Licenza assente dai metadati.

### `pret/pokered`

https://github.com/pret/pokered · Assembly · licenza - · aggiornato 2026-10-06 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Disassemblato di Pokémon Rosso e Blu per Game Boy, mantenuto dal gruppo pret.

Come funziona. Il codice è in assembly (`gbz80`) e ricostruisce le ROM originali, verificate con gli hash sha1 elencati nel README: Red e Blue (UE), la build di debug `BLUEMONS.GB` e due file `.patch`. Il README rimanda a wiki, tutorial, simboli e strumenti (`gb-asm-tools`).

Relazione con il progetto. Fonte primaria per il track BRI sul comportamento e sui formati della generazione 1, già usata nel codice del progetto (nel_codice vero).

Da verificare. Nessuna licenza dichiarata nei metadati.

### `pret/pokeyellow`

https://github.com/pret/pokeyellow · Assembly · licenza - · aggiornato 2026-09-02 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Decompilazione (disassemblato) di Pokémon Giallo per Game Boy Color.

Come funziona. Codice in assembly Game Boy (`gbz80`) che ricostruisce le ROM di `Pokemon Yellow (UE) [C][!].gbc`, della build di debug `YELLMONS.GB` e della patch `Dmgapse0.h08.patch`, verificate con hash SHA-1. Il README rimanda a `INSTALL.md`, a una wiki con tutorial e a un ramo di simboli.

Relazione con il progetto. Fonte primaria per BRI sul formato dei dati e sul protocollo della generazione 1; il progetto la usa già (`nel_codice` vero).

Da verificare. Licenza assente nei metadati. Il README non descrive la struttura dei sorgenti: dettagli sui formati non accertati qui.

### `projectpokemon/Gen3-WCTool`

https://github.com/projectpokemon/Gen3-WCTool · C# · licenza - · aggiornato 2019-03-22 · attivo · track BRI · non usato dal codice del progetto · scheda da solo metadati

Che cosa è. Editor di Wondercard per i giochi Pokémon Gen 3, versione aggiornata dello strumento di Suloku.

Come funziona. Programma in C# secondo i metadati. Il repository non ha README nella raccolta, quindi formato dei dati, giochi supportati e architettura non sono accertabili. Licenza assente nei metadati.

Relazione con il progetto. Non usato nel codice del progetto; citato per il track BRI e pertinente come possibile secondo parere sul formato della Wondercard di Gen 3, da confermare.

Da verificare. README assente: funzioni, formato della Wondercard trattato e giochi supportati non accertati; ultimo aggiornamento del codice nel 2019.

### `REONTeam/libmobile`

https://github.com/REONTeam/libmobile · C · licenza LGPL-3.0 · aggiornato 2026-03-17 · attivo · track BRI · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Libreria C che implementa il protocollo del Mobile Adapter GB, per collegare giochi a server personalizzati.

Come funziona. È scritta in C, progettata per essere integrata in emulatori e progetti hardware; è documentata nell'header `mobile.h`, con `libmobile-bgb` come esempio. Si appoggia alle ricerche pubblicate su Dan Docs. Licenza LGPL-3.0.

Relazione con il progetto. Track BRI, non usata nel codice (nel_codice falso): fonte di riferimento sul protocollo dell'adattatore mobile di Game Boy.

Da verificare. Il README non elenca i comandi del protocollo: vanno letti in `mobile.h`, che non è stato aperto.

### `REONTeam/trade-corner`

https://github.com/REONTeam/trade-corner · C# · licenza AGPL-3.0 · aggiornato 2026-04-18 · attivo · track BRI · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Script cron che esegue gli scambi del Trade Corner in Pokémon Cristallo tramite il server per il Mobile Adapter.

Come funziona. Scritto in C# (.NET), licenza AGPL-3.0, usa un file `config.json` a partire da un esempio. Va lanciato come processo periodico, consigliato una volta all'ora perché il gioco non permette di controllare prima. Si basa sui risultati originali pubblicati su Glitch City.

Relazione con il progetto. Fonte per BRI sul funzionamento del Trade Corner di Cristallo; non è usato da uno strumento del progetto (`nel_codice` falso).

Da verificare. Il README non descrive il protocollo né i formati scambiati.

### `savaughn/pokerom-trader`

https://github.com/savaughn/pokerom-trader · C · licenza MIT · aggiornato 2025-02-17 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Programma desktop con interfaccia grafica per scambiare Pokémon fra due file di salvataggio delle generazioni 1 e 2.

Come funziona. Scritto in C con la libreria grafica raylib e la libreria `PKSav` per leggere e scrivere i salvataggi. Calcola le statistiche dopo l'evoluzione dai valori base, dal livello, dai DV e dagli EV letti dalla SRAM, con la formula di Bulbapedia, e crea un backup prima di scrivere. Non supporta la regione giapponese né la generazione 3 o successive.

Relazione con il progetto. Secondo parere per BRI sulla conversione dei dati e sulle evoluzioni per scambio nei salvataggi delle generazioni 1 e 2; il progetto lo usa già (`nel_codice` vero).

### `stevenchaulk/arduino-poke-gen2`

https://github.com/stevenchaulk/arduino-poke-gen2 · C · licenza NOASSERTION · aggiornato 2016-09-23 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Programma C per Arduino che permette di scambiare Pokémon con sé stessi o di inviare un Pokémon definito in un file, per i giochi di generazione 2.

Come funziona. Il README dice che è una versione modificata della macchina a stati di `pepijndevos/arduino-boy` (generazione 1), adattata ai giochi di generazione 2, e che è provata solo su Pokémon Cristallo.

Relazione con il progetto. Track BRI, già usato nel codice del progetto (nel_codice vero): fonte per il protocollo di scambio di Gen 2 sul cavo link.

Da verificare. Il testo del README letto era troncato: limiti e formato del file del Pokémon non sono accertati. Licenza dichiarata come altra, senza testo.

### `Striaton-Lab-Team/Poke_Transporter_GB`

https://github.com/Striaton-Lab-Team/Poke_Transporter_GB · BitBake · licenza MIT · aggiornato 2026-10-03 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Programma per Game Boy Advance che trasferisce Pokémon dalla generazione 1 e 2 alla generazione 3.

Come funziona. È un programma multiboot per GBA, avviabile da cavo link, flashcart o ROM loader (`Poke_Transporter_GB_mb.gba`, `Poke_Transporter_GB_standalone.gba`), che richiede un cavo link Game Boy Color. Converte i Pokémon con il metodo LEGAL del Pokémon Community Conversion Standard e modifica sia il salvataggio della generazione 3 sia quello della generazione 1 o 2. Supporta cartucce originali e la EZ Flash Omega Definitive Edition.

Relazione con il progetto. Fonte primaria e termine di confronto per il track BRI, che costruisce un ponte software fra le stesse generazioni su hardware originale; è già usato da uno strumento del progetto (nel_codice).

Da verificare. Il linguaggio indicato dai metadati (BitBake) non corrisponde al contenuto descritto nel README; la composizione reale del codice non è accertata.

### `Striaton-Lab-Team/Pokemon-Community-Conversion-Standard`

https://github.com/Striaton-Lab-Team/Pokemon-Community-Conversion-Standard · C++ · licenza - · aggiornato 2026-10-02 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Libreria C++ che definisce modi standard, concordati dalla comunità, per convertire un Pokémon della generazione 1 o 2 in uno della generazione 3.

Come funziona. È scritta in C++. Il README descrive in tabelle, campo per campo (valore di personalità, EXP, IV, EV, abilità, luogo di incontro, gioco di origine, Poké Ball, forme di Unown), quattro metodi: `ORIGINAL` e `LEGAL`, implementati, e `FAITHFUL` e `VIRTUAL`, elencati ma non ancora implementati. Tratta anche i Pokémon mitici e la conversione di Stat Experience in EV.

Relazione con il progetto. Fonte primaria per il track BRI sulle regole di conversione da Gen 1-2 a Gen 3, già usata nel codice del progetto (nel_codice vero).

Da verificare. Nei metadati mancano descrizione e licenza. Il README non mostra l'API della libreria né il formato di ingresso e uscita.

### `tangrs/usb-gba-multiboot`

https://github.com/tangrs/usb-gba-multiboot · C · licenza - · aggiornato 2012-07-11 · attivo · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Progetto per caricare codice homebrew su un Game Boy Advance con il protocollo multiboot, tramite un'interfaccia USB seriale.

Come funziona. Software per PC in C (programma `gbaxfer`) e firmware per un microcontrollore Teensy AVR, che prende 4 byte dal PC, li trasmette al GBA e restituisce 4 byte. Usa la modalità SIO normal a 32 bit, la più veloce e semplice, con il limite di un solo GBA avviabile alla volta; il firmware per la modalità SIO multiplayer a 16 bit, più lenta e half-duplex, è incluso. Il codice caricabile arriva a 256 KB, i dati partono dal byte alto, e con lo schema dei piedini fra GBA e Teensy riportato nel README. Licenza assente nei metadati.

Relazione con il progetto. Strumento già usato nel codice del progetto, per il track BRI: riferimento per il protocollo multiboot del GBA con un microcontrollore che parla la linea seriale del cavo link.

Da verificare. Progetto fermo dal 2012; la scheda non ha verificato la compatibilità con hardware attuale né la licenza.

### `vaguilar/pokemon-red-cable-club-hack`

https://github.com/vaguilar/pokemon-red-cable-club-hack · Python · licenza Apache-2.0 · aggiornato 2020-08-07 · fork · track BRI · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Prova di fattibilità, fork con licenza Apache 2.0, di un buffer overflow nel Cable Club di Pokémon Rosso per Game Boy.

Come funziona. Contiene l'assembly e i dati binari inviati al Game Boy e due modi per spedirli: un Arduino collegato a un cavo link tagliato (pin Serial Out, Serial In, Serial Clock) e uno script Python `bgb_link.py` verso l'emulatore BGB. Il codice viene eseguito nel Trade Center sfruttando il protocollo di scambio del cavo.

Relazione con il progetto. Fonte per il track BRI sul protocollo seriale del cavo link della generazione 1 e per il cablaggio verso un microcontrollore; è già usata da uno strumento del progetto (nel_codice).

## Modding del 3DS (3DS)

### `BernardoGiordano/Checkpoint`

https://github.com/BernardoGiordano/Checkpoint · C++ · licenza GPL-3.0 · aggiornato 2026-08-30 · attivo · track 3DS · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Programma homebrew in C++ per salvare e ripristinare i salvataggi su 3DS e Switch.

Come funziona. Per 3DS gestisce cartucce e titoli digitali, extdata, cartucce DS, DSiWare e GBA Virtual Console; per Switch i titoli giocati. Ha un server FTP in background, trasferimento senza fili fra console e un motore di script. Licenza GPL-3.0.

Relazione con il progetto. Track 3DS, non usato nel codice (nel_codice falso): strumento candidato per copiare i salvataggi dalla console, da usare solo sui nostri esemplari posseduti.

Da verificare. Il README letto è in parte troncato: i formati di backup non sono accertati.

### `d0k3/SEEDconv`

https://github.com/d0k3/SEEDconv · C · licenza - · aggiornato 2016-10-19 · archiviato · track 3DS · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Generatore del file `seeddb.bin` per la console Nintendo 3DS, archiviato.

Come funziona. Scritto in C, è un eseguibile da Windows su cui si trascina il file `nand:/data/(console-unique)/sysdata/0001000f/00000000`, disponibile solo con firmware 9.6 e quindi solo con hardmod. Dalla versione 4 accetta anche altri `seeddb.bin` rinominati e ne unisce i seed unici. Il file prodotto è compatibile con Decrypt9.

Relazione con il progetto. Nessuno strumento del progetto lo usa (nel_codice falso): riguarda il track 3DS, perché tratta materiale legato alla console, da gestire con le cautele della regola sul materiale di chiave.

Da verificare. Non è accertato se serva ancora su firmware recenti. Repository archiviato e fermo al 2016.

### `hacks-guide/MSET9`

https://github.com/hacks-guide/MSET9 · C · licenza - · aggiornato 2026-09-25 · fork · track 3DS · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Exploit primario ARM9 per Nintendo 3DS che si attiva aggiungendo solo nomi di file alla scheda SD, usato per installare boot9strap.

Come funziona. Scritto in C. Sfrutta il fatto che `FSPXI:EnumerateExtSaveData` non controlla l'esito dell'apertura di una directory: un file il cui nome inizia con 8 cifre esadecimali dentro la cartella extdata manda in crash process9, che in un caso salta a una stringa ID1 in memoria ARM9. Il README indica console con firmware 11.4-11.17 di qualunque regione, un lettore USB per SD e un PC o un dispositivo Android.

Relazione con il progetto. Fonte primaria per 3DS sul metodo di installazione di boot9strap; non è usato da uno strumento del progetto (`nel_codice` falso).

Da verificare. Repository marcato come fork e senza licenza nei metadati. La parte del README oltre le prime domande della FAQ non è stata esaminata.

## Scambio fra GBA e Switch (LDN)

### `Ethiquema/ryu_ldn_nx`

https://github.com/Ethiquema/ryu_ldn_nx · C++ · licenza GPL-2.0 · aggiornato 2026-10-04 · attivo · track LDN · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Sysmodule per Atmosphere su Nintendo Switch con firmware personalizzato, che porta il multiplayer locale LDN sui server LDN di Ryujinx (RyuLDN) su TCP.

Come funziona. Codice in C++ che registra tre servizi IPC: un MITM su `ldn:u`, con una macchina a stati che sintetizza i `NetworkInfo` per i giochi, un MITM su `bsd:u` che tunnelizza i socket diretti alla sottorete `10.114.x.x` in pacchetti `ProxyData`, e un servizio `ryu:cfg` per un overlay Tesla. Sostituisce la combinazione ldn_mitm più lan-play. Licenza GPL-2.0.

Relazione con il progetto. Non usato nel codice del progetto; fonte candidata per il track LDN, come implementazione che intercetta il servizio LDN della Switch e come termine di confronto per il suo protocollo.

Da verificare. Il README dichiara il progetto in lavorazione e non pronto al rilascio, con richiesta di non usare i server ufficiali; la scheda non ha verificato lo stato reale del codice.

### `kinnay/LDN`

https://github.com/kinnay/LDN · Python · licenza GPL-3.0 · aggiornato 2026-10-02 · attivo · track LDN · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Pacchetto Python per la comunicazione wireless locale con una Nintendo Switch, che permette di scansionare, unirsi e ospitare reti LDN.

Come funziona. Libreria Python 3.12 o successivo per Linux, installabile con `pip install ldn`, che lavora a livello data link: serve l'hardware WLAN capace di trasmettere e ricevere action frame in modalità monitor, con i privilegi `CAP_NET_ADMIN` e `CAP_NET_RAW`, e NetworkManager va fermato. Il README spiega che il protocollo LDN non è né ad hoc né infrastruttura e che l'access point è realizzato interamente in modalità monitor, con due interfacce monitor, una attiva e una passiva. Licenza GPL-3.0.

Relazione con il progetto. Non usato nel codice del progetto; fonte primaria candidata per il track LDN, perché è l'implementazione del protocollo di rete locale della Switch che lo scambio da GBA richiederebbe di imitare.

Da verificare. Il README non elenca i giochi o i tipi di scambio provati; l'idoneità al caso GBA e Switch non è accertata.

### `kinnay/NintendoClients`

https://github.com/kinnay/NintendoClients · Python · licenza MIT · aggiornato 2026-10-03 · attivo · track LDN · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Pacchetto Python che implementa client per vari server Nintendo di 3DS, Wii U e Switch, accompagnato da una wiki sui protocolli.

Come funziona. Libreria Python 3.12 o successivo, installabile con `pip install nintendoclients`, con script di esempio per Switch (per esempio `system_update.py`, `smm2_level.py`), Wii U, 3DS e un esempio di server personalizzato (`custom/server.py`) con autenticazione e secure server. Il README dichiara il supporto di firmware Switch fino alla 22.5.0 e avverte che Nintendo banna le console con comportamenti sospetti. Documentazione su Read the Docs e sulla wiki. Licenza MIT.

Relazione con il progetto. Fonte già usata nel codice del progetto, per il track LDN: documentazione dei protocolli e dei server Nintendo come base per lo scambio di rete fra GBA e Switch, con il rischio di ban che il README stesso segnala.

Da verificare. Il README non elenca i server supportati, rimandando alla documentazione esterna; la scheda non ha stabilito quali servano al track.

### `spacemeowx2/ldn_mitm`

https://github.com/spacemeowx2/ldn_mitm · C++ · licenza GPL-2.0 · aggiornato 2026-08-24 · attivo · track LDN · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Modulo di sistema (sysmodule) per Nintendo Switch con Atmosphère che permette di giocare in rete, via LAN, ai giochi che usano la rete locale wireless.

Come funziona. Scritto in C++, derivato da `fs_mitm`: sostituisce il servizio `ldn` di sistema, che normalmente chiama il servizio WiFi per cercare e collegarsi alle Switch vicine, e ne emula la scansione con UDP su LAN. Si usa di norma con `switch-lan-play` e il README riporta una tabella di compatibilità fra versioni di ldn_mitm e di Atmosphère. Licenza GPL-2.0.

Relazione con il progetto. Fonte primaria e strumento già in uso per LDN (scambio fra GBA e Switch via rete locale); `nel_codice` vero.

### `spacemeowx2/switch-lan-play`

https://github.com/spacemeowx2/switch-lan-play · C · licenza GPL-3.0 · aggiornato 2025-03-21 · attivo · track LDN · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Client e server per giocare in rete locale simulata su Nintendo Switch.

Come funziona. Scritto in C e compilabile con CMake (Linux con `libpcap`, Windows con MSYS2). Il client gira su un PC collegato allo stesso router della Switch, scambia pacchetti ARP e IPv4 con la console e li inoltra a un server via UDP, con proxy SOCKS5 opzionale per la parte client-server. La Switch richiede un IP statico.

Relazione con il progetto. Fonte per il track LDN sul tunnel dei pacchetti di rete locale fra console, già usata dagli strumenti del progetto (nel_codice vero).

Da verificare. Il README non dice quali giochi o modalità di gioco locale siano compatibili, né come sia incapsulato il protocollo LDN.

### `tornadus/frlg-ldn-trade`

https://github.com/tornadus/frlg-ldn-trade · Python · licenza AGPL-3.0 · aggiornato 2026-09-03 · attivo · track LDN · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Prova di fattibilità in Python che fa scambiare Pokémon a un computer con Rosso Fuoco e Verde Foglia su Switch o Switch 2 via rete locale senza fili (LDN).

Come funziona. Richiede Linux, Python 3.12, una scheda WiFi compatibile non gestita dal sistema, permessi di root e il file `prod.keys` della console. Scambia file `.pk3` ed `.ek3` e il README elenca schede provate e problematiche.

Relazione con il progetto. Track LDN, già usato nel codice del progetto (nel_codice vero): fonte primaria sul protocollo di scambio fra computer e Switch.

Da verificare. Il README letto non descrive il protocollo in dettaglio. Licenza AGPL-3.0. Il file `prod.keys` è materiale riservato.

### `unlimitedcoder2/frlg-ldn-trade`

https://github.com/unlimitedcoder2/frlg-ldn-trade · Python · licenza AGPL-3.0 · aggiornato 2026-09-09 · fork · track LDN · usato dal codice del progetto · scheda da README e metadati

Che cosa è. Prova di fattibilità in Python, fork con licenza AGPL 3.0, di uno scambio fra un computer e Pokémon Rosso Fuoco e Verde Foglia in esecuzione su Switch o Switch 2 via rete locale wireless LDN.

Come funziona. Richiede Linux, Python 3.12 o successivo, una scheda WiFi compatibile (il README elenca modelli provati e problematici) e le `prod.keys` della Switch. Accetta e produce file `.pk3` e `.ek3` e si lancia con `frlgtrade.py --live`, simulando i membri della squadra con almeno due file `.pk3`.

Relazione con il progetto. Fonte primaria per il track LDN sullo scambio via rete locale con Switch; è già usata da uno strumento del progetto (nel_codice). L'uso delle `prod.keys` rientra nel perimetro di `hardware-and-perimeter.md`.

### `unlimitedcoder2/ldnd`

https://github.com/unlimitedcoder2/ldnd · C · licenza GPL-2.0 · aggiornato 2026-09-01 · attivo · track LDN · usato dal codice del progetto · scheda da solo metadati

Che cosa è. Programma in C con licenza GPL 2.0, privo di descrizione, legato dal progetto al track LDN.

Come funziona. I metadati indicano solo il linguaggio C e la licenza. Il nome suggerisce un demone per il protocollo LDN (Local Dispatch Network, la rete locale wireless di Switch), ma non è dichiarato.

Relazione con il progetto. Il track LDN lo cita e un nostro strumento lo usa già (nel_codice), verosimilmente per lo scambio via rete locale fra GBA e Switch.

Da verificare. README assente e descrizione vuota: funzione, piattaforma e formati non sono accertati; l'interpretazione del nome è un'inferenza da verificare sul sorgente.

## Senza track dichiarato nel registro

### `Ajarmar/universal-pokemon-randomizer-zx`

https://github.com/Ajarmar/universal-pokemon-randomizer-zx · Java · licenza GPL-3.0 · aggiornato 2024-11-23 · fork · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Codice sorgente del Universal Pokemon Randomizer ZX, fork di un randomizzatore per giochi Pokémon, che include anche titoli 3DS.

Come funziona. Programma in Java, fork del Universal Pokemon Randomizer di Dabomstew, con contributi di darkeye e cleartonic; il README rimanda a una pagina wiki per la compilazione e alla pagina delle release per il changelog. Non descrive i formati dei dati dei giochi. Licenza GPL-3.0.

Relazione con il progetto. Nessuna relazione diretta dichiarata: il campo track del registro delle fonti è vuoto e il codice non lo usa; potrebbe valere come riferimento per la lettura dei dati dei giochi, ipotesi non verificata.

Da verificare. Il README non dice quali giochi siano supportati né come legga le ROM; relazione con i track non accertata.

### `andrewbenington/OpenHome`

https://github.com/andrewbenington/OpenHome · Rust · licenza GPL-3.0 · aggiornato 2026-10-07 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Applicazione multipiattaforma per archiviare e spostare Pokémon fra salvataggi di giochi diversi in modo quasi senza perdite, sul modello di Pokémon Home, scritta in Rust con Tauri e React.

Come funziona. Usa Tauri, React, Radix UI e Vite e richiede NodeJS e Rust per la compilazione. Permette di spostare Pokémon anche verso generazioni precedenti conservando dati come i nastri (esempio del README: un Sceptile Campione di Kalos spostato da X a Rubino e ritorno). Il README avverte che gli esemplari modificati non sono garantiti legali.

Relazione con il progetto. Nessun track lo cita nel registro delle fonti. Per natura è affine al track PKD, come alternativa a Pokémon Home; non risulta usato da strumenti del progetto.

Da verificare. Il registro delle fonti non gli associa alcun track: l'affinità con PKD è inferita dal confronto con Pokémon Home fatto dal README.

### `Bl4ckSh4rk/256ed3b857c9677310837d5180121f35`

https://gist.github.com/Bl4ckSh4rk/256ed3b857c9677310837d5180121f35 · Text · licenza - · aggiornato 2026-01-22 · gist · track - · non usato dal codice del progetto · scheda da solo metadati

Che cosa è. Gist con l'elenco dei titoli Pokémon per Nintendo 3DS, contenuto in un solo file di testo.

Come funziona. Il gist contiene `Pokemon-3DS-Title-List.txt` (circa 5 KB, tipo Text). Dal nome si ricava un elenco di titoli, probabilmente con identificativi, ma il contenuto non è stato letto.

Relazione con il progetto. Nessun track lo cita nel registro delle fonti. Per natura è un riferimento di consultazione per il track 3DS; non risulta usato da strumenti del progetto.

Da verificare. Nessun README e il file del gist non è stato aperto: il formato dell'elenco e i campi che contiene non sono accertati.

### `christianhaitian/retroarch-cores`

https://github.com/christianhaitian/retroarch-cores · Shell · licenza - · aggiornato 2026-09-07 · fork · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Repository di core libretro già compilati per architetture arm64 e armhf, usati soprattutto da ArkOS e TheRA.

Come funziona. Raccolta di binari `.so` per console portatili con SoC RK3326, gestita con script shell (`addcore`) che richiedono `libarchive-zip-perl`, `rsync` e `zip`. Il README spiega come aggiungere o aggiornare un core e inviare una pull request.

Relazione con il progetto. Nessuna relazione diretta con i track (`track` vuoto, `nel_codice` falso).

Da verificare. Repository marcato come fork e senza licenza. Il README non dice quali core siano presenti.

### `concreted/3DSync`

https://github.com/concreted/3DSync · C++ · licenza - · aggiornato 2022-06-05 · fork · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Programma homebrew in C++ per 3DS e 2DS che sincronizza salvataggi e file con un cloud, un'altra console o un PC.

Come funziona. Una pagina di configurazione produce il file `/3ds/3DSync/3DSync.ini`; legge le cartelle di Checkpoint e JKSM. Il README dice che al momento supporta solo Dropbox. È un fork.

Relazione con il progetto. Nessuna relazione diretta con i track; citata solo nel registro delle fonti (nel_codice falso).

Da verificare. Nei metadati manca la licenza. Ultimo aggiornamento nel 2022.

### `DS-Homebrew/GodMode9i`

https://github.com/DS-Homebrew/GodMode9i · C · licenza GPL-3.0 · aggiornato 2026-10-05 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Esplora file con accesso completo per Nintendo DS, DSi e per la modalità TWL_FIRM del 3DS, scritto in C e ispirato a GodMode9.

Come funziona. Permette di copiare, spostare, eliminare e rinominare file, montare il NitroFS dei file NDS, i salvataggi DSiWare e le immagini FAT. Esegue dump di cartucce GBA su DS e DS Lite, di cartucce DS e DSi su DSi e 3DS, e il ripristino dei salvataggi su cartucce DS e GBA.

Relazione con il progetto. Nessun track lo cita nel registro delle fonti. Per natura potrebbe riguardare il dump di cartucce del track 3DS, ma è un'inferenza e nessuno strumento del progetto lo usa.

Da verificare. Non è accertato se serva davvero a un nostro flusso di lavoro: il registro delle fonti non gli associa alcun track.

### `DS-Homebrew/nds-bootstrap`

https://github.com/DS-Homebrew/nds-bootstrap · C · licenza GPL-3.0 · aggiornato 2026-10-07 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Applicazione homebrew in C che esegue ROM Nintendo DS e DSi dalla scheda SD, senza emulatore.

Come funziona. Funziona su DSi e 3DS con firmware personalizzato e su DS con flashcard (modalità B4DS); legge i parametri da un file `.ini` e ha come frontend TWiLight Menu++ e i forwarder; si compila con devkitARM.

Relazione con il progetto. Nessuna relazione diretta con i track; citata solo nel registro delle fonti (nel_codice falso).

### `DS-Homebrew/TWiLightMenu`

https://github.com/DS-Homebrew/TWiLightMenu · C++ · licenza GPL-3.0 · aggiornato 2026-10-07 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Sostituto del menu DSi, in C++, per DS, DSi, 3DS e 2DS.

Come funziona. Lancia giochi DS, DSi e GBA e, per le ROM DS, usa nds-bootstrap come caricatore; si compila con devkitARM, libnds, grit e mmutil. Licenza GPL-3.0.

Relazione con il progetto. Nessuna relazione diretta con i track; citata solo nel registro delle fonti (nel_codice falso).

### `figgyc/0d31b77fc6e4e8f9a49399d392740d46`

https://gist.github.com/figgyc/0d31b77fc6e4e8f9a49399d392740d46 · Markdown · licenza - · aggiornato 2026-07-26 · gist · track - · non usato dal codice del progetto · scheda da solo metadati

Che cosa è. Gist con una guida all'installazione di romhack su 3DS, in formato Markdown.

Come funziona. I metadati indicano un solo file, `guide.md` (1266 byte, Markdown). Non c'è un README.

Relazione con il progetto. Nessuna relazione diretta con i track; citata solo nel registro delle fonti (nel_codice falso).

Da verificare. Il contenuto della guida non è stato letto: metodo e requisiti non sono accertati.

### `FlagBrew/PKSM`

https://github.com/FlagBrew/PKSM · C++ · licenza GPL-3.0 · aggiornato 2026-09-08 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Gestore ed editor di salvataggi Pokémon portatile per Nintendo 3DS, dalla generazione I alla VIII.

Come funziona. Scritto in C++ per 3DS con firmware custom. Modifica salvataggi di cartucce originali e copie digitali, da Rosso Fuoco, Verde Foglia e Rubino, Zaffiro, Smeraldo fino a Spada e Scudo, esegue script, legge QR code con file `.pkx` e wondercard e contiene un database offline di wondercard. Per verificare e legalizzare i dati serve un server `local-gpss`.

Relazione con il progetto. Nessun track del progetto lo cita (`track` vuoto, `nel_codice` falso); è pertinente per PKD ed EVT come riferimento per il database di wondercard e la legalizzazione.

Da verificare. Il README non descrive i formati interni dei salvataggi.

### `FlagBrew/PKSM-Scripts`

https://github.com/FlagBrew/PKSM-Scripts · C · licenza - · aggiornato 2026-10-02 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Raccolta di script generici per il gestore di salvataggi PKSM su Nintendo 3DS.

Come funziona. Il README descrive come installare gli script (da PKSM 6.0.0 sono già inclusi), avverte che alcuni modificano il salvataggio con valori illegali, per esempio la forma di Vivillon, e rimanda a una sezione sul formato dei file di script. Il linguaggio indicato dai metadati è C.

Relazione con il progetto. Nessun track lo cita (`track` vuoto, `nel_codice` falso); potrebbe servire a PKD come riferimento per le modifiche ai salvataggi legali o illegali.

Da verificare. Licenza assente. Il formato dei file di script non è stato letto.

### `francesco265/RtcPwalker`

https://github.com/francesco265/RtcPwalker · C++ · licenza GPL-3.0 · aggiornato 2026-01-08 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Patch per Pokémon HeartGold e SoulSilver che permette al gioco di comunicare con il Pokéwalker usando il ricetrasmettitore a infrarossi integrato del 3DS.

Come funziona. Scritto in C++, implementato come codice Action Replay da aggiungere a `usrcheat.dat` e attivare in TWiLight Menu++. Usa RTCom, con TWL_FIRM patchato tramite TWPatch, per far comunicare ARM7 con ARM11, che accede ai registri IR; per il protocollo si basa sul lavoro di Dmitry.GR. Il README la dichiara sperimentale, lenta e instabile, testata solo su Old 3DS.

Relazione con il progetto. Nessun track lo cita (`track` vuoto, `nel_codice` falso); è pertinente per 3DS e ACE come esempio di esecuzione di codice su 3DS in un gioco Nintendo DS.

Da verificare. Il README non dice quali versioni del firmware siano necessarie.

### `gdkchan/Ohana3DS-Rebirth`

https://github.com/gdkchan/Ohana3DS-Rebirth · C# · licenza - · aggiornato 2022-09-17 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Strumento in lavorazione per vedere, estrarre e sostituire dati di ROM 3DS decifrate, come modelli, texture e alcune animazioni.

Come funziona. Riscrittura in C# di una versione originale in Visual Basic, da compilare con Visual Studio Community 2015. Non decifra le ROM, che vanno decifrate con altri strumenti.

Relazione con il progetto. Nessuna relazione diretta registrata (track vuoto, nel_codice falso); lavora su ROM 3DS decifrate, quindi è vicino al track 3DS.

Da verificare. Il README non elenca i formati supportati. Repository senza licenza e fermo al 2022.

### `Gericom/GBARunner2`

https://github.com/Gericom/GBARunner2 · C · licenza - · aggiornato 2023-05-08 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Hypervisor che esegue giochi GBA su DS, DSi e 3DS in modalità DS.

Come funziona. Scritto in C, usa FatFS e integra il BIOS open source di Normmatt con piccole modifiche, anche se un BIOS GBA valido migliora la compatibilità. I giochi di norma non richiedono patch SRAM, tranne dove indicato nelle liste di compatibilità. Si apre la cartella `gba` sulla radice della scheda SD.

Relazione con il progetto. Nessuna relazione diretta registrata (track vuoto, nel_codice falso); è un modo di far girare giochi GBA su un 3DS già modificato, vicino al track 3DS.

Da verificare. Licenza assente dai metadati. Il README non descrive l'architettura interna dell'hypervisor.

### `ghnr/sneakpeekbot`

https://github.com/ghnr/sneakpeekbot · Python · licenza - · aggiornato 2021-11-26 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Bot per Reddit scritto in Python.

Come funziona. La descrizione dei metadati è «sneakpeekbot from reddit». Il README contiene soltanto un elenco di cose da fare, come gestire più subreddit, sostituire JSON con un database e dividere la funzione `process_comment`.

Relazione con il progetto. Nessuna relazione diretta con il progetto (track vuoto, nel_codice falso).

Da verificare. Il README non descrive lo scopo del bot né il suo funzionamento: non è accertato perché il progetto lo citi.

### `hax0kartik/wumiibo`

https://github.com/hax0kartik/wumiibo · C++ · licenza GPL-3.0 · aggiornato 2025-08-01 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Homebrew per Nintendo 3DS che emula gli amiibo, riscrivendo il modulo NFC della console.

Come funziona. Codice in C++ compilato con devkitPro, ctrulib e makerom, da usare con Luma3DS aggiornato e con il patching dei giochi attivo, e con un menu richiamabile durante il gioco. Il README segnala che alcuni giochi si bloccano dopo la chiusura del menu e indica un procedimento alternativo passando dal tasto Home. Una guida all'uso e una lista di compatibilità stanno sulla wiki. Licenza GPL-3.0.

Relazione con il progetto. Nessun track assegnato nel registro delle fonti e non usato nel codice; può riguardare il track 3DS come esempio di sostituzione di un modulo di sistema, relazione da confermare.

Da verificare. Il README non dice nulla di Pokémon né di dati di salvataggio; pertinenza al track 3DS non accertata.

### `InternalLoss/DLS1-Files`

https://github.com/InternalLoss/DLS1-Files · - · licenza - · aggiornato 2023-04-26 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Raccolta di file DLS1 per vari giochi Nintendo Wii e DS, fra cui Mystery Gift Pokémon convertiti dall'autore.

Come funziona. È un archivio di file senza linguaggio di programmazione, ospitato sul server DLS1 usato da Wiimmfi, con un mirror su GitLab. Una parte dei file viene da altre fonti, come AltWfc, un'altra è prodotta dall'autore, e i Mystery Gift personalizzati non vengono accettati.

Relazione con il progetto. Nessuna relazione diretta con un track del progetto (track vuoto, nel_codice falso); potrebbe servire solo come materiale di confronto per i Mystery Gift di giochi DS.

Da verificare. Il README non descrive il formato dei file DLS1 né l'elenco dei giochi coperti. Licenza assente. Ultimo push nel 2023.

### `joel16/3DShell`

https://github.com/joel16/3DShell · C · licenza - · aggiornato 2026-08-14 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Gestore di file multiuso per Nintendo 3DS, in C, orientato ai file multimediali e ispirato al gestore di CyanogenMod e LineageOS.

Come funziona. Offre creazione, rinomina, eliminazione, copia e spostamento di file e cartelle, anteprima di immagini (BMP, GIF, JPG, PCX, PNG, PGM, PPM, TGA), estrazione di archivi ZIP, RAR e 7Z, navigazione di CTRNAND, ordinamento degli elenchi e aggiornamento online. Il README distingue il proprio ruolo da FBI, che gestisce i titoli.

Relazione con il progetto. Nessun track lo cita nel registro delle fonti. Per natura serve a esplorare la SD e la CTRNAND del 3DS (track 3DS); non risulta usato da strumenti del progetto.

Da verificare. Il registro delle fonti non gli associa alcun track: il legame con il 3DS è inferito. I metadati non dichiarano alcuna licenza.

### `KernelEquinox/8F-Helper`

https://github.com/KernelEquinox/8F-Helper · C · licenza - · aggiornato 2016-12-21 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Utilità a riga di comando in C che converte assembly e opcode GBZ80 in un elenco di oggetti da usare con l'oggetto 8F di Pokémon Rosso, Blu e Giallo.

Come funziona. Programma in C che usa tabelle di lookup, con gestione minima degli errori e supporto di una sola etichetta per i salti; l'eseguibile si chiama `gbz80aid`. Accetta esadecimale o file e produce formati `asm`, `bgb`, `hex`, `joy` (valori del joypad), `gen1` e `gen2` (codici degli oggetti per ACE in R/B/Y e G/S/C).

Relazione con il progetto. Non usato nel codice del progetto e senza track assegnato; è pertinente al tema dell'esecuzione di codice nei giochi Game Boy (track ACE), come strumento per scrivere payload sotto forma di oggetti, da confermare.

Da verificare. Licenza assente nei metadati; la pertinenza al track ACE è un'inferenza non registrata nel registro delle fonti.

### `kuroppoi/entralinked`

https://github.com/kuroppoi/entralinked · Java · licenza MIT · aggiornato 2026-05-13 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Emulatore autonomo di Game Sync per Pokémon Nero e Bianco e i loro seguiti, che scarica nel gioco Pokémon, strumenti e altri contenuti senza modificare il salvataggio.

Come funziona. Programma in Java 17, compilato con Gradle, con interfaccia grafica e modalità senza interfaccia, che include un server DNS integrato: la DS va configurata con il DNS del computer, indicato in `config.json` se il rilevamento automatico non basta. Scarica Pokémon, strumenti, skin del C-Gear e del Pokédex, musical e, solo in Nero 2 e Bianco 2, i visitatori della Join Avenue, e permette il Memory Link con un salvataggio senza una seconda DS. Licenza MIT.

Relazione con il progetto. Nessun track assegnato nel registro delle fonti e non usato nel codice; riguarda la Gen 5, fuori dai track elencati, ma il meccanismo di consegna di Pokémon da server emulato può interessare il track EVT, da confermare.

Da verificare. Pertinenza al track EVT non registrata nel registro delle fonti; il README non descrive il formato dei Pokémon consegnati.

### `lifehackerhansol/YANBF`

https://github.com/lifehackerhansol/YANBF · C · licenza GPL-2.0 · aggiornato 2024-01-03 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Forwarder per nds-bootstrap in C che parte dalla modalità 3DS, con generatore a riga di comando e interfaccia grafica.

Come funziona. Usa un bootloader `sdcard.nds` e un'applicazione 3DS che lo avvia, evitando il limite di 40 titoli dei forwarder DSiWare. Il README descrive la generazione di file CIA da installare con FBI. Licenza GPL-2.0.

Relazione con il progetto. Nessuna relazione diretta con i track; citata solo nel registro delle fonti (nel_codice falso).

### `LumaTeam/Luma3DS`

https://github.com/LumaTeam/Luma3DS · C · licenza GPL-3.0 · aggiornato 2026-09-04 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Firmware personalizzato (custom firmware) per tutta la famiglia Nintendo 3DS, in C.

Come funziona. Applica patch e reimplementa parti del software di sistema; richiede boot9strap. Offre il menu sovrapposto Rosalina (screenshot, filtri, codici cheat, reindirizzamento dell'input), plugin di gioco in formato 3GX, LayeredFS per il reindirizzamento dei contenuti, sostituzione di moduli di sistema, uno stub GDB e il chainload di altri firmware.

Relazione con il progetto. Nessun track lo cita nel registro delle fonti, ma per natura è la base del modding del 3DS (track 3DS); non risulta usato da strumenti del progetto.

Da verificare. Il registro delle fonti non gli associa alcun track: il legame con il track 3DS è inferito dalla natura del software.

### `mamba2410/reverse-pokewalker`

https://github.com/mamba2410/reverse-pokewalker · C++ · licenza MIT · aggiornato 2024-10-16 · archiviato · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Ricerca di ingegneria inversa sul Pokéwalker, il dispositivo per Pokémon HeartGold e SoulSilver; progetto archiviato.

Come funziona. Linguaggio indicato C++, licenza MIT, archiviato. Il README dice che il lavoro è stato superato dall'articolo di Dmitry.GR, da cui provengono i dump delle ROM interna da 48k ed esterna da 64k, e rimanda a progetti derivati: picowalker, un estrattore di ROM, un editor di EEPROM, un iniettore di percorsi e due emulatori.

Relazione con il progetto. Nessun track lo cita (`track` vuoto, `nel_codice` falso); è pertinente per 3DS e ACE come fonte sul protocollo del Pokéwalker.

Da verificare. Il README rimanda all'articolo di Dmitry.GR e non descrive il protocollo.

### `masterfeizz/DaedalusX64-3DS`

https://github.com/masterfeizz/DaedalusX64-3DS · C++ · licenza GPL-2.0 · aggiornato 2022-10-23 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Port per Nintendo 3DS dell'emulatore Nintendo 64 DaedalusX64.

Come funziona. Scritto in C++ con ricompilatore dinamico per ARM, opera di vari contributori elencati nel README. Si installa estraendo `data.zip` nella radice della scheda SD e mettendo le ROM in `sdmc:/3ds/DaedalusX64/Roms/`.

Relazione con il progetto. Nessuna relazione diretta registrata (track vuoto, nel_codice falso); è un emulatore N64 per 3DS modificato, vicino al track 3DS.

Da verificare. Ho letto solo le prime 45 righe del README: prestazioni e compatibilità con i giochi Pokémon non sono accertate.

### `MechanicalDragon0687/NDSForwarder`

https://github.com/MechanicalDragon0687/NDSForwarder · C++ · licenza GPL-3.0 · aggiornato 2025-05-19 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Applicazione homebrew in C++ per 3DS che crea e installa forwarder di giochi DS nel menu HOME.

Come funziona. Usa come base un modello DSiWare e lavora con il pacchetto forwarder di nds-bootstrap; il README raccomanda ROM complete, non ridotte. Licenza GPL-3.0.

Relazione con il progetto. Nessuna relazione diretta con i track; citata solo nel registro delle fonti (nel_codice falso).

### `MersenneTwister-Lab/TinyMT`

https://github.com/MersenneTwister-Lab/TinyMT · C++ · licenza NOASSERTION · aggiornato 2024-09-25 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Libreria di generatori di numeri pseudocasuali Tiny Mersenne Twister, con periodo 2^127-1, di Mutsuo Saito e Makoto Matsumoto.

Come funziona. Implementazione in C++ (versione 1.1.2) con documentazione generabile con `make doc`; per Visual Studio serve msinttypes. Il README non descrive l'algoritmo oltre al periodo. Licenza BSD a tre clausole nel testo, mentre i metadati la danno come NOASSERTION.

Relazione con il progetto. Nessun track assegnato e non usato nel codice; il generatore è citato in contesti di generazione di valori casuali dei giochi Pokémon, ma il README non lo dice, quindi la relazione resta da accertare.

Da verificare. Il legame con i giochi Pokémon non emerge da README e metadati; relazione con i track non accertata.

### `mtheall/ftpd`

https://github.com/mtheall/ftpd · C++ · licenza GPL-3.0 · aggiornato 2025-11-19 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Server FTP per 3DS, Switch e Linux, in C++.

Come funziona. Gestisce più client simultanei (sul 3DS i socket bastano per 4 o 5 trasferimenti paralleli), supporta MODE Z e usa Dear ImGui come interfaccia grafica. Include un dispositivo emulato `/devZero` per misurare le prestazioni di rete.

Relazione con il progetto. Nessun track lo cita nel registro delle fonti. Per natura può servire a copiare file da e verso la SD di 3DS e Switch, quindi al track 3DS; non risulta usato da strumenti del progetto.

Da verificare. Il registro delle fonti non gli associa alcun track: l'uso nel progetto è solo ipotizzato.

### `Olmectron/Simple-Web-App-GUI-for-YANBF-Generator`

https://github.com/Olmectron/Simple-Web-App-GUI-for-YANBF-Generator · JavaScript · licenza CC0-1.0 · aggiornato 2022-03-11 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Interfaccia grafica web in JavaScript, con licenza CC0, per il generatore YANBF di lifehackerhansol.

Come funziona. È un'app costruita con Polymer Starter Kit e impacchettata con Electron (eseguibili per Windows x64, Linux e macOS) che lancia `generator.py` di YANBF: si aggiungono file NDS e si avvia l'elaborazione. Richiede Python 3 e YANBF già installato.

Relazione con il progetto. Nessun track lo cita nel registro delle fonti. Per natura serve a creare forwarder NDS per il menu HOME del 3DS (track 3DS); non risulta usato da strumenti del progetto.

Da verificare. Il registro delle fonti non gli associa alcun track: il legame con il 3DS è inferito.

### `polaris-/dwc_network_server_emulator`

https://github.com/polaris-/dwc_network_server_emulator · Python · licenza AGPL-3.0 · aggiornato 2024-08-02 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Emulatore di server per il multigiocatore online di Nintendo DS e Wii, che sostituisce il servizio Nintendo Wi-Fi Connection.

Come funziona. Server in Python 2.7 basato su Twisted e zope.interface, con Apache o un altro server HTTP come requisito; il README cita come fonti di riferimento OpenSpy Core e gli strumenti di Luigi Auriemma per la decodifica degli elenchi di server. Istruzioni, lista di compatibilità e contenuti disponibili stanno sulla wiki. Licenza AGPL-3.0.

Relazione con il progetto. Nessun track assegnato nel registro delle fonti e non usato nel codice; riguarda l'online della DS e può interessare il track EVT come via di consegna di distribuzioni, relazione da confermare.

Da verificare. Il README non elenca i giochi Pokémon supportati né le distribuzioni; pertinenza al track EVT non registrata nel registro delle fonti.

### `RiiConnect24/DNS-Server`

https://github.com/RiiConnect24/DNS-Server · Python · licenza MIT · aggiornato 2024-05-21 · fork · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Server DNS locale, in Python, per far collegare una Wii ai server RiiConnect24 quando il provider impedisce di usare un DNS personalizzato.

Come funziona. Scritto in Python con `dnslib` e `requests`, licenza MIT. All'avvio scarica l'elenco degli indirizzi DNS da inoltrare e risponde alla Wii nella stessa rete; sono previste versioni `.exe` e Python, e il README tratta anche Pi-hole.

Relazione con il progetto. Nessuna relazione diretta con i track del progetto (`track` vuoto, `nel_codice` falso); tocca solo l'infrastruttura di servizi di rete per Wii.

Da verificare. Repository marcato come fork. Il README non cita i Pokémon: la ragione per cui compare nel registro non è accertata.

### `RocketRobz/NTR_Forwarder`

https://github.com/RocketRobz/NTR_Forwarder · C · licenza - · aggiornato 2026-05-23 · fork · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Applicazione in C per creare scorciatoie a giochi e applicazioni nel menu HOME di DSi e 3DS.

Come funziona. Il README è molto breve: dice che è il lato lanciatore di NitroHax privo del motore dei trucchi, ricostruito dal sorgente. È un fork.

Relazione con il progetto. Nessuna relazione diretta con i track; citata solo nel registro delle fonti (nel_codice falso).

Da verificare. Il README non descrive uso né formati. Nei metadati manca la licenza.

### `semaj14/Multi-PokemonFramework`

https://github.com/semaj14/Multi-PokemonFramework · C++ · licenza GPL-3.0 · aggiornato 2024-02-18 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Plugin C++ per giochi Pokémon su Nintendo 3DS, generazioni 6 e 7, basato su CTRPluginFramework.

Come funziona. Si installa copiando il pacchetto sulla scheda SD e caricandolo dal menu Rosalina di Luma3DS. Gli argomenti dichiarati includono `3gx`, `actionreplay` e `ctrpf-ar`. Licenza GPL-3.0.

Relazione con il progetto. Nessuna relazione diretta con i track; citata solo nel registro delle fonti (nel_codice falso).

Da verificare. Il README è scarno: le funzioni del plugin non sono descritte.

### `suloku/BW_tool`

https://github.com/suloku/BW_tool · C# · licenza GPL-3.0 · aggiornato 2023-10-23 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Editor di salvataggi per i giochi Pokémon di quinta generazione (Nero, Bianco, Nero 2, Bianco 2).

Come funziona. Scritto in C#, licenza GPL-3.0. Offre editor per la Foresta Link, i dati dell'allenatore, la Prop Case, un estrattore e iniettore di blocchi con cifratura e decifratura dei blocchi noti, e la verifica e correzione dei checksum; per Nero 2 e Bianco 2 modifica anche Join Avenue, chiavi, medaglie e il Memory Link.

Relazione con il progetto. Nessun track lo cita (`track` vuoto, `nel_codice` falso); è un possibile riferimento per PKD sull'iniezione di Pokémon di distribuzione, per esempio PGL, nei salvataggi di quinta generazione.

Da verificare. Ultimo push nel 2023. Del README è stata letta solo la parte iniziale dell'elenco delle funzioni.

### `TheLevelUp/pos-tls-patcher`

https://github.com/TheLevelUp/pos-tls-patcher · PowerShell · licenza Apache-2.0 · aggiornato 2024-01-24 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Installatore che abilita TLS 1.2 su Windows Vista SP2 e successivi.

Come funziona. Scritto in PowerShell, licenza Apache-2.0. Rende le applicazioni .NET 4.x compatibili con TLS 1.2 senza modifiche al codice, agendo sulle chiavi del registro di .NET e di SChannel, e può scaricare .NET 4.6 se manca. Richiede privilegi di amministratore.

Relazione con il progetto. Nessuna relazione diretta con i track (`track` vuoto, `nel_codice` falso).

Da verificare. Il README non cita i Pokémon: la ragione per cui compare nel registro non è accertata.

### `TurdPooCharger/GBAVCSM`

https://github.com/TurdPooCharger/GBAVCSM · - · licenza GPL-3.0 · aggiornato 2020-04-09 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Script per GodMode9 dedicato alla gestione dei salvataggi dei giochi GBA della Virtual Console del 3DS.

Come funziona. I metadati indicano licenza GPL-3.0 e i topic `3ds` e `godmode9`. Il README rimanda a un post del forum GBAtemp per ogni informazione.

Relazione con il progetto. Nessuna relazione diretta registrata (track vuoto, nel_codice falso); l'argomento tocca i salvataggi GBA su 3DS ed è vicino al track 3DS.

Da verificare. Il README non spiega il funzionamento dello script né i formati trattati: servirebbe il post del forum, non letto.

### `TuxSH/TWLSaveTool`

https://github.com/TuxSH/TWLSaveTool · C++ · licenza GPL-2.0 · aggiornato 2024-09-24 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Homebrew per 3DS che legge, scrive e cancella i salvataggi delle cartucce Nintendo DS.

Come funziona. Programma in C++ per Luma3DS, costruito con libctru e devkitARM, con build `3dsx` consigliata e build CIA fornita per ragioni storiche. Il README dichiara compatibili tutti i giochi originali tranne quattro (fra cui Pokémon Typing Adventure) e ringrazia per il lavoro sul comando `PXIDEV:SPIMultiWriteRead`, di cui nota l'uso anche da parte di PokéTransporter. Il progetto non è più mantenuto se non per errori di compilazione. Licenza GPL-2.0.

Relazione con il progetto. Nessun track assegnato nel registro delle fonti e non usato nel codice; potrebbe riguardare il track 3DS per l'estrazione dei salvataggi di cartucce DS possedute, da confermare.

Da verificare. Pertinenza al track 3DS non registrata nel registro delle fonti; il README non dice quali formati di salvataggio incontri.

### `Universal-Team/Universal-Updater`

https://github.com/Universal-Team/Universal-Updater · C++ · licenza GPL-3.0 · aggiornato 2026-10-01 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Applicazione homebrew per Nintendo 3DS che installa e aggiorna altri homebrew.

Come funziona. Scritta in C++ con devkitARM e le librerie `3ds-dev`, `3ds-curl` e `libarchive`. Usa «unistore», cioè repository in formato JSON simili a Cydia, con Universal-DB come predefinito, e installa in background mostrando schermate e note di rilascio.

Relazione con il progetto. Nessuna relazione diretta registrata (track vuoto, nel_codice falso); è uno strumento di utilità per il track 3DS, per installare homebrew sulla console modificata.

Da verificare. Ho letto solo le prime 45 righe del README.

### `Watchful1/RemindMeBot`

https://github.com/Watchful1/RemindMeBot · Python · licenza - · aggiornato 2026-10-06 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Codice del bot di Reddit u/RemindMeBot, che risponde ai commenti con un promemoria e invia un messaggio allo scadere del tempo.

Come funziona. Processo Python in ciclo che legge la casella dei messaggi, salva i promemoria in SQLite con SQLAlchemy e usa PRAW tramite PrawWrapper; le date passano per `dateparser.parse`, poi `search_dates` e parsedatetime. Un processo di acquisizione separato, non incluso nel repository, scrive i commenti corrispondenti in un file SQLite passato con `--ingest_db`. Il README dice che il codice è pubblicato per consultazione, con tutti i diritti riservati.

Relazione con il progetto. Nessuna relazione diretta con i track del progetto: nessun track assegnato e nessun uso nel codice.

Da verificare. Perché la fonte sia citata nel registro non emerge da README e metadati.

### `YANBForwarder/assets`

https://github.com/YANBForwarder/assets · Python · licenza CC0-1.0 · aggiornato 2025-09-21 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Archivio comunitario di banner e suoni personalizzati per i forwarder YANBF.

Come funziona. Il contenuto sta in cartelle `assets/<codice del gioco>`: immagini PNG 256x128 e suoni WAV a 16 bit stereo, sotto 3 secondi. Gli script sono in Python. Licenza CC0-1.0.

Relazione con il progetto. Nessuna relazione diretta con i track; citata solo nel registro delle fonti (nel_codice falso).

### `YANBForwarder/YANBF`

https://github.com/YANBForwarder/YANBF · C · licenza GPL-2.0 · aggiornato 2024-01-03 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Struttura di forwarder per nds-bootstrap in C, eseguibile dalla modalità 3DS.

Come funziona. Un'app in modalità 3DS lancia un bootloader `sdcard.nds`, che esegue la configurazione di nds-bootstrap; i forwarder sono installati come CIA (`bootstrap.cia` in `sd:/cias`) e compaiono come icone nel menu HOME. A differenza dei forwarder DSiWare, il README dichiara che non c'è il limite di 40 titoli.

Relazione con il progetto. Nessun track lo cita nel registro delle fonti. Per natura serve a lanciare giochi NDS dal 3DS (track 3DS); non risulta usato da strumenti del progetto.

Da verificare. Il registro delle fonti non gli associa alcun track: il legame con il 3DS è inferito.

### `yuhasem/FeebasFinder`

https://github.com/yuhasem/FeebasFinder · JavaScript · licenza MIT · aggiornato 2024-05-12 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Strumento web per trovare le caselle d'acqua in cui compare Feebas in Pokémon Rubino, Zaffiro e Smeraldo.

Come funziona. Scritto in JavaScript e pubblicato come pagina web. Il README spiega che all'inizio del gioco, dopo l'animazione di rimpicciolimento del personaggio, vengono impostati TID, SID, il seme di Feebas (FID) e la frase di tendenza, a partire da chiamate consecutive al generatore casuale. Genera cinque coppie di FID e frasi con 16 bit di confronto. Per Rubino e Zaffiro con batteria asciutta i risultati sono rapidi, con batteria scarica o seme non corrispondente richiedono uno o due minuti.

Relazione con il progetto. Nessuna relazione diretta registrata (track vuoto, nel_codice falso); riguarda l'RNG di Gen 3 e la batteria di Rubino e Zaffiro, tema vicino ai track SME e BAT.

Da verificare. Ho letto solo le prime 45 righe del README e il resto dell'algoritmo non è accertato. L'autore avverte che possono esserci errori e che non è stato provato su hardware.

### `yuhasem/poc_utils`

https://github.com/yuhasem/poc_utils · Python · licenza - · aggiornato 2026-08-30 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Raccolta di piccoli script Python usati per pianificare i percorsi delle sfide Professor Oak, da una comunità su Reddit.

Come funziona. Script in Python; il README è di due righe e non descrive struttura, dipendenze né formati. Licenza assente nei metadati.

Relazione con il progetto. Nessuna relazione diretta accertata con i track del progetto: nessun track assegnato e nessun uso nel codice.

Da verificare. README scarno: non si sa che cosa facciano gli script né se trattino dati di gioco; relazione con il track PKD non accertata.

### `zaksabeast/DreamRadarCartRedirect`

https://github.com/zaksabeast/DreamRadarCartRedirect · Assembly · licenza GPL-3.0 · aggiornato 2025-05-13 · attivo · track - · non usato dal codice del progetto · scheda da README e metadati

Che cosa è. Patch in assembly per Dream Radar e Pokémon Transporter del 3DS che reindirizza la lettura e la scrittura della cartuccia NDS verso un file sulla SD.

Come funziona. Le patch si applicano al file `.code` dell'applicazione, ottenuto dal 3DS stesso, con armips e flips (Floating IPS). Il salvataggio viene letto da TWiLightMenu e nds-bootstrap come file sulla SD, così le due applicazioni funzionano senza la cartuccia.

Relazione con il progetto. Nessun track lo cita nel registro delle fonti. Per natura riguarda il track 3DS e il perimetro di `hardware-and-perimeter.md`, che esclude assistenza su Pokémon Bank e Pokémon Transporter; non risulta usato da strumenti del progetto.

Da verificare. Il registro delle fonti non gli associa alcun track: la relazione è inferita e va letta alla luce del limite operativo su Transporter.
