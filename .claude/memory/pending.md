# Registro delle cose in sospeso

Questo file esiste perche' l'utente non deve essere il sistema di memoria del progetto. Tutto cio' che e' iniziato e non finito, atteso da qualcun altro, o rimandato a una condizione futura, sta qui: se una cosa non e' scritta qui, per il progetto non e' in sospeso.

A differenza di `progress.md` e `decisions.md`, che sono append-only, questo file si modifica: una voce chiusa si cancella, e la sua storia resta nel work log. Va letto a inizio sessione insieme a `index.md`, e le voci pertinenti al lavoro in corso vanno ricordate all'utente senza che le chieda. Le voci marcate come da ricordare sempre si ripetono a ogni sessione anche quando non sono pertinenti, perche' cosi' e' stato chiesto.

## In attesa dell'utente: materiale da procurare

La consegna avviene salvando i file in `_notes/fonti/`, secondo la convenzione di `.claude/rules/web-sources-not-fetchable.md`. Ogni riga dice a quale domanda serve, perche' chiedere una fonte senza dire cosa si cerca produce lavoro inutile.

Tutte le voci che stavano qui sono state consegnate. Il 2026-08-26 sono arrivati come screenshot il tutorial di GBAtemp, le ricerche nei canali di Pokemon Multiplayer Research con cinque filtri, quelle nel canale del Glitch City Research Institute con tre filtri, e quelle su GBAdev e PRET; il contenuto e' stato letto e trasferito in `SOURCES.md`, nelle note di `docs/fonti/` e nelle note di studio, e il materiale grezzo e' stato eliminato secondo la regola della fonte unica. Non resta materiale atteso.

Delle domande a cui quel materiale doveva rispondere, due hanno avuto risposta e una no. Sulle schede Wi-Fi la risposta e' arrivata e ha corretto una premessa sbagliata del progetto, registrata in `sub-gba-switch-trading.md`. Sui difetti sfruttabili di generazione 3 la resa e' stata molto oltre l'atteso, ed e' in `docs/09-esecuzione-codice.md`. Sulla formula da Stat Experience a Effort Value la risposta non c'e', perche' il canale dei disassemblati discute la modifica dei giochi e non la conversione fra generazioni; da un dato trovato la' e' stata pero' ricavata una derivazione, che sta in `docs/07-conversione-vincoli.md` etichettata come tale e da verificare.

Restano due domande nuove per cui il materiale non basta, e per entrambe la via non e' un altro screenshot.

| Domanda aperta | Come si chiude |
|---|---|
| quale chip monta l'adattatore Archer T2U Nano in mano all'utente | collegandolo e leggendone l'identificatore USB: il filtro `8811` nel canale non da' alcun risultato, quindi la testimonianza non esiste e la misura sostituisce la ricerca |
| se la derivazione da Stat Experience a Effort Value coincida con cio' che fa un'implementazione reale | confrontandola con il comportamento del PCCS sul suo sorgente, oppure con `PKHeX` su un caso costruito; e' lavoro di lettura e non di raccolta |

## In attesa dell'utente: credenziali e abilitazioni

| Cosa | Stato | Che cosa sblocca |
|---|---|---|
| App Reddit di tipo script | chiusa il 2026-08-26 con esito negativo, e la voce resta solo per non far ripetere il tentativo. Entrambe le cause ipotizzate sono cadute: l'account ha una password propria e non dipende dal solo accesso via Google, l'email e' stata verificata e il pannello vecchio la mostra come tale, e la documentazione ufficiale dice che per l'uso gratuito e non commerciale non esiste alcun modulo di registrazione preventiva. Con nome semplice, tipo script e reCAPTCHA spuntato il rifiuto persiste identico. Non e' del tutto silenzioso: accanto al pulsante compare il rimando alla Responsible Builder Policy, quindi il rifiuto e' legato all'ammissibilita' secondo quella politica e non al contenuto del form. Un'ipotesi non verificata resta l'eta' o il punteggio dell'account | nulla da fare: la terza via della regola sulle fonti non recuperabili non e' disponibile su questo account, e le fonti Reddit si leggono per la seconda o la quarta via |
| Token utente di Discord | deciso il 2026-08-26 di NON usarlo: il rischio di essere riconosciuti come self-bot e vedersi chiudere l'account non e' accettabile. La via resta la copia manuale dei messaggi pertinenti in un file di testo sotto `_notes/fonti/`, che `tools/read-chat-export.py` digerisce comunque | nulla: e' una decisione chiusa, e cio' che resta e' materiale da procurare |
| Adattatore Wi-Fi USB per il track LDN | deciso il 2026-08-26 di partire con l'Archer T2U Nano che l'utente ha gia'. La riserva registrata prima poggiava su una premessa sbagliata: la testimonianza positiva riguarda l'Archer T2U Plus, il cui utente dichiara `driver: rtw_8821cu`, cioe' un chip RTL8821CU servito dal driver in albero `rtw88` senza alcun driver custom, e non l'RTL8811AU che si era supposto. Il filtro `8811` nel canale non da' risultati, quindi su quel chip non esiste testimonianza. Non e' bloccante finche' il resto del track e' in lettura | il primo passo non e' comprare ne' cercare ma misurare: collegare l'adattatore e leggerne l'identificatore USB, da cui si ricavano chip e driver. Se cade nella famiglia `rtw88` la strada e' aperta, altrimenti conviene uno dei modelli dichiarati affidabili |

## Fonti in sospeso, da ricordare sempre

Queste non hanno una via di recupero e non ne avranno: si consultano solo entrandoci di persona. Vanno ricordate a ogni sessione, come richiesto, cosi' che la decisione di usarle o no sia presa e non dimenticata.

| Community | Link | Ambito |
|---|---|---|
| PRET | https://discordapp.com/invite/vdTW48Q | disassemblati e decompilazioni |
| Glitch City Research Institute | https://discord.com/invite/EA7jxJ6 | glitch ed esecuzione di codice in Gen 1 e 2 |
| GBAdev | https://discord.gg/ctGSNxRkg2 | sviluppo homebrew GBA e toolchain |
| Hex Maniac Advance Development | https://discord.com/invite/x9eQuBg | editing di ROM GBA |

## Strumenti da invocare quando si verifica una condizione

Questa e' la tabella che l'agente deve consultare da se': ogni riga dice quando ricordare uno strumento all'utente, invece di attendere che se lo ricordi lui.

| Condizione che si verifica | Strumento da ricordare | Che cosa se ne ottiene |
|---|---|---|
| esiste per la prima volta un dump di salvataggio Gen 3 | `gba-save-extraction-smeraldo/tools/emerald_bag_decode.py` | validazione delle sezioni, identificazione del gioco, smascheramento dello zaino, cinque classi di anomalia |
| esiste un dump di qualunque generazione | `PKHeX`, anche nella versione web | confronto campo per campo con `pokebridge`, che falsifica le permutazioni di etichette |
| serve scrivere un salvataggio sintetico da confrontare | `pokebridge` piu' `PKHeX` | la prova di conformita' descritta in `docs/23-prove-eseguite.md`, che non richiede hardware |
| arriva il lettore GBxCart RW | `FlashGBX` | lettura e scrittura di cartucce e salvataggi |
| esiste una ROM Game Boy dumpata legittimamente | `BGB` con il cavo su TCP, oppure `mGBA` | collaudo del protocollo del cavo contro un gioco vero |
| serve ispezionare una ROM GBA | `HexManiacAdvance` | mappe dei dati e modifica esadecimale guidata |
| serve la trascrizione di un video | `yt-dlp`, installato su questa macchina | sottotitoli automatici senza passare dall'interfaccia |
| serve condensare una fonte molto lunga senza consumare contesto | il modello su Ollama a `http://192.168.20.58:11500` | sintesi locale di testo, con i limiti dichiarati in `STACK.md` |
| si aggiungono o si rigenerano tabelle di dati | `pokemon-gen12-gen3-bridge-original-hardware/tools/extract_charmaps.py` | tabelle caratteri rigenerate dai charmap, con verifica delle sentinelle |
| prima di ogni commit | `python tools/md-unwrap.py --check .` e `python tools/lint-md-commands.py .` | conformita' alla convenzione Markdown e ai comandi su riga singola |
| dopo commit che toccano i `covers-paths` delle schede | la skill `sync-context` | rilevamento del drift e bump del checkpoint |
| si chiude una milestone | un report in LaTeX sotto `reports/`, con `latexmk -pdf` | documento datato che fotografa risultati, metodo e limiti, con taglio da telecomunicazioni |
| serve una trascrizione di un video senza sottotitoli automatici | il progetto `E:\local-audio-transcriptor`, che pero' non e' installato | riconoscimento vocale locale con marcatura temporale; verificato il 2026-08-26 che i due video arretrati, cioe' il primo di Goppier e quello sullo scambio locale su Switch, non hanno sottotitoli di alcun tipo, quindi questa e' l'unica via. Attenzione allo stato reale, verificato il 2026-08-26: `deno` c'e', nella versione 2.9.5, ma il comando `transcribe` non e' sul PATH e `uv tool list` non riporta alcuno strumento installato, quindi il progetto e' su disco e non e' allestito. Prima di usarlo va installato con lo script che porta con se', e quella e' una decisione dell'utente perche' scarica i modelli di riconoscimento vocale, che pesano |
| l'utente produce un export di un canale Discord o di una chat Telegram | `tools/read-chat-export.py` | converte in Markdown filtrato per parola chiave, intervallo di date e lunghezza minima, e lo mette fra le fonti procurate a mano |
| si collega per la prima volta un adattatore Wi-Fi USB destinato al track LDN | la lettura del suo identificatore USB, e la tabella di compatibilita' in `SOURCES.md` | dice subito se il chip cade in una famiglia con driver in albero capace di modalita' monitor, che e' cio' che decide la praticabilita' del track |
| si vuole provare il track LDN senza installare Linux | il demone `ldnd` con Zadig e l'archivio `linux-firmware` | esecuzione su Windows senza macchina virtuale, con la procedura descritta in `docs/11-wireless-locale-e-ponte-switch.md`; ricordare che dopo la riassegnazione a WinUSB quell'adattatore non fa piu' da scheda di rete |
| il ponte ha prodotto il primo modulo di codice, condizione verificata il 2026-08-25 | il gate del server MCP code-context, rimandato per ADR-010 | estrazione di simboli e riferimenti da `pokebridge/` senza versare i file in contesto; la proposta va rifatta perche' la condizione che la rimandava non vale piu', e resta la facolta' di rimandarla ancora |
| il ponte ha un comando di test, condizione verificata il 2026-08-25 | un `CLAUDE.md` annidato in `pokemon-gen12-gen3-bridge-original-hardware/` | dichiarazione dei soli comandi di build, lint e test di quella cartella, cioe' `python tests/run_tests.py`; mai stato, che resta nella scheda del sottoprogetto |

## Debito di lettura

Cio' che e' raggiungibile e non ancora letto. Il debito si chiude leggendo, non aspettando.

| Fonte | Stato |
|---|---|
| `pokeyellow` e `pokegold` | disassemblati non ancora clonati; servono per le differenze di offset di Giallo e di Oro e Argento |
| Data Crystal, mappe RAM di Rosso e Blu e di Cristallo | non lette; la pagina di Gen 3 e' stata letta e ha reso poco |
| Bulbapedia, pagina sull'esecuzione di codice arbitrario | non letta; l'argomento e' coperto dal mirror di Glitch City e dal dev log |
| `3dbrew` | non letto; serve al track 3DS quando si toccheranno i salvataggi delle cartucce dumpate |
| documentazione navigabile di pokeemerald | non letta; il sorgente clonato la rende poco necessaria |
| `gameboy-spoof` | citato come antenato di `arduino-boy` ma non trovato: il proprietario indovinato da' 404, va cercato il repository giusto |
| `REONTeam/trade-corner` e `REONTeam/libmobile` | l'organizzazione e' stata letta ma questi due repository no, e riguardano lo scambio e il protocollo dell'adattatore mobile |
| riferimento delle classi di `ldn.readthedocs.io` | letta la pagina di ingresso, non il riferimento delle interfacce |

Le sei voci che erano qui e non ci sono piu' sono state lette il 2026-08-25: il blog di Phasip, `pepijndevos/arduino-boy`, `vaguilar/pokemon-red-cable-club-hack`, il progetto REON a livello di organizzazione, `switch-lan-play` e la pagina di ingresso di `ldn.readthedocs.io`. Cio' che ne e' venuto sta nelle rispettive note sotto `docs/fonti/`.

## Trascrizioni da produrre

La pipeline funzionante e' quella descritta in `STACK.md`, cioe' scaricare i sottotitoli automatici con `yt-dlp` e ripulirli con `tools/vtt-to-text.py`, senza toccare l'audio. Su quella il lavoro e' mio e non serve nulla dall'utente. Per i due video che restano quella pipeline non si applica, perche' non hanno sottotitoli di alcun tipo, e serve il riconoscimento vocale locale: qui il lavoro non e' interamente mio, perche' il progetto che lo fa e' su disco ma non installato, e installarlo comporta lo scarico dei modelli. E' una decisione dell'utente, non un passo da dare per fatto.

Il debito di lettura sulle trascrizioni e' chiuso: il 2026-08-26 tutte e sei quelle prodotte sono state lette per intero e cio' che documentano e' confluito in `SOURCES.md` con la profondita' necessaria a citarle, piu' tre punti nuovi nella sezione 11 della referenza dei formati, di cui due chiusi lo stesso giorno sul sorgente. Restano due video da trascrivere, e per entrambi e' stato verificato il 2026-08-26 che non esistono sottotitoli di alcun tipo, automatici o manuali: l'unica via e' il riconoscimento vocale locale.

| Video | Link | Perche' serve |
|---|---|---|
| Goppier, lo scambio impossibile | https://www.youtube.com/watch?v=inMbtwmVlKQ | e' il piu' importante dei due, perche' il video successivo dello stesso autore vi rimanda per la struttura del circuito e per la questione se un GBA possa parlare direttamente il protocollo Gen 2, che e' un punto aperto capace di cambiare il confronto fra le quattro opzioni |
| Scambio locale su Switch in FRLG | https://www.youtube.com/watch?v=epCf87MTLnk | serve al track LDN, ed e' il presupposto di quel track visto dal lato utente |

I canali senza un video specifico, cioe' Goppier, Lorenzooone, im a blisy, RETIRE, TheZZAZZGlitch, Retro Game Mechanics Explained e Displaced Gamers, restano da esplorare per scegliere quali video valga la pena trascrivere: e' una decisione da prendere, non una trascrizione da lanciare.

## Punti tecnici aperti

| Punto | Dove e' registrato |
|---|---|
| offset dei salvataggi Gen 2 per lingue diverse dall'inglese | sezione 11 della referenza dei formati |
| dimensione esatta del blocco di posta Gen 2 | idem |
| tabella dagli indici interni Gen 1 ai numeri nazionali, da generare | idem, ed e' il prossimo strumento naturale |
| vettori di prova esternalizzati su file invece che dentro i metodi | `docs/20-architettura-codice.md`, dichiarato come debito tecnico |
| conformita' di `pokebridge` verificata contro `PKHeX` | `docs/23-prove-eseguite.md`, e' il controllo che costa meno e falsifica piu' cose |
| data di disponibilita' di Rosso Fuoco e Verde Foglia su Switch | schede `sub-3ds-modding.md` e `sub-gba-switch-trading.md`, fonti in conflitto |
| se l'Archer T2U Nano, chip RTL8811AU, entri in modalita' monitor con il driver fuori albero | scheda `sub-gba-switch-trading.md`; la macchina non ha Wi-Fi integrato e la prova si fara' con l'adattatore che l'utente ha gia' |
| se i programmi di Pokemon Automation per Rosso Fuoco e Verde Foglia su Switch tocchino lo scambio locale | `poke-automation-study/STUDIO-01-architettura-e-perimetro.md`, ed e' la domanda che collega il track dell'automazione a quello dello scambio |
| se il canale del Mobile Adapter GB apra una strada alternativa al cavo per il lato Gen 2 | nota `docs/fonti/reon.md`, da valutare |
| se l'affermazione di PkSploit regga alla prova, cioe' se un microcontrollore sostituisca il lettore per le cartucce Game Boy | nota `docs/fonti/pksploit.md`, richiede hardware |
| se la derivazione da Stat Experience a Effort Value coincida con un'implementazione reale, e quale politica adottare quando la somma sfora il tetto di 510 | `docs/07-conversione-vincoli.md`, dichiarata come derivazione e non come citazione |
| se la routine di radice quadrata del gioco vada replicata invece che approssimata, dato che la fonte riporta 63002 dove la radice matematica darebbe 63504 | idem, ed e' rilevante solo se si vuole fedelta' al margine |
| quale chip monti l'Archer T2U Nano, dato che il nome commerciale AC600 copre chip diversi | `sub-gba-switch-trading.md`; si misura, non si cerca |
| se anche Rubino e Zaffiro su Switch riceveranno il supporto al Wireless Adapter | affermazione di terzi ricavata dall'ispezione del binario dell'emulatore, non verificata |

## Decisioni aperte

| Decisione | Stato |
|---|---|
| ADR-008, quale delle quattro opzioni implementative per il ponte | aperta; il costo relativo e' cambiato e l'analisi aggiornata sta in `docs/30-opzioni-implementative.md` |
| se cancellare e ricreare il repository su GitHub per certezza sulla bonifica | rimandata; oggi si accetta che i commit orfani restino raggiungibili per hash fino al garbage collector, come registrato in ADR-014 |
| che cosa debba essere il track dell'automazione | parzialmente decisa il 2026-08-26: per ora studio, cominciato con la prima nota nella cartella del sottoprogetto. Resta aperto se diventera' riuso della parte su microcontrollore in comune con l'opzione D del ponte oppure automazione vera come obiettivo indipendente. Sul perimetro c'e' una buona notizia, cioe' che il progetto di riferimento dichiara console non modificate e nessun accesso alla memoria, quindi il suo perimetro e' compatibile con le nostre regole |
| se usare il token utente di Discord per gli export | chiusa il 2026-08-26: no. Il rischio di sospensione dell'account non e' accettabile, e le community si leggono copiando a mano i messaggi pertinenti |

## Strumenti da costruire

| Strumento | Stato | Che cosa serve prima |
|---|---|---|
| caricatore di salvataggi verso hardware | scritto e collaudato nella sua parte non distruttiva, cioe' `tools/save-deploy.py`: esamina il file, identifica il gioco, pretende i due backup su volumi distinti e produce il piano dei cinque passi. La scrittura non e' implementata e lo dichiara | per la cartuccia, il lettore e un collaudo su un esemplare sacrificabile; per la scheda SD, la decisione su quale percorso sia quello giusto per il titolo installato |
| generatore del salvataggio sintetico per il confronto con PKHeX | da scrivere, e non richiede nulla | e' il prossimo passo tecnico piu' utile del ponte |
| generatore della tabella indici di specie | da scrivere, e non richiede nulla | ultimo dato costante ancora trascritto a mano |
| esportazione degli strumenti verso il template | da fare con un handoff, come per la regola sulle fonti non recuperabili | riguarda `read-chat-export.py`, `fetch-reddit.py`, `vtt-to-text.py` e `build-source-map.py`, che non sono specifici di questo dominio |

## Blocchi materiali

| Blocco | Che cosa impedisce |
|---|---|
| lettore GBxCart RW non ancora arrivato | lettura e scrittura di cartucce, prova da un capo all'altro su dati reali, e indirettamente il collaudo del protocollo contro un gioco vero perche' serve una ROM dumpata |
| discovery hardware non fatta | la scelta fra le quattro opzioni di ADR-008; la lista delle domande sta in `docs/10-multiboot-hardware.md` |
| driver CH340 non confermati e porta COM non annotata | l'uso del lettore quando arrivera'; e' il prossimo passo dichiarato del track Smeraldo |
