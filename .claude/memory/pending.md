# Registro delle cose in sospeso

Questo file esiste perche' l'utente non deve essere il sistema di memoria del progetto. Tutto cio' che e' iniziato e non finito, atteso da qualcun altro, o rimandato a una condizione futura, sta qui: se una cosa non e' scritta qui, per il progetto non e' in sospeso.

A differenza di `progress.md` e `decisions.md`, che sono append-only, questo file si modifica: una voce chiusa si cancella, e la sua storia resta nel work log. Va letto a inizio sessione insieme a `index.md`, e le voci pertinenti al lavoro in corso vanno ricordate all'utente senza che le chieda. Le voci marcate come da ricordare sempre si ripetono a ogni sessione anche quando non sono pertinenti, perche' cosi' e' stato chiesto.

## In attesa dell'utente: materiale da procurare

La consegna avviene salvando i file in `_notes/fonti/`, secondo la convenzione di `.claude/rules/web-sources-not-fetchable.md`. Ogni riga dice a quale domanda serve, perche' chiedere una fonte senza dire cosa si cerca produce lavoro inutile.

Delle sei voci che stavano qui, cinque sono state consegnate il 2026-08-26 come screenshot e sono ora nel registro delle fonti con cio' che hanno dato; la sesta, la pagina di Ryujinx su LDN3, e' stata eliminata come fonte perche' il dominio non risolve nemmeno dall'utente. Resta questa.

| Fonte | Link | Formato atteso | Domanda a cui serve |
|---|---|---|---|
| GBAtemp, tutorial sui problemi di salvataggio | https://gbatemp.net/threads/tutorial-fix-all-save-problems-for-pokemon-games-vc-gba.433266/ | screenshot o pagina salvata | e' la guida che il thread sul salvataggio fallito indica come riferimento quando compare il messaggio di corruzione; serve prima di toccare la cartuccia di Smeraldo |
| Discord, canale di supporto di Pokemon Multiplayer Research | https://discord.gg/nBnTrv3UMn | messaggi copiati a mano in un file di testo sotto `_notes/fonti/` | la testimonianza sulle schede Wi-Fi per esteso, cioe' quale adattatore, quale sistema operativo, quale driver e quale versione di emulatore, perche' oggi il progetto ne ha solo il riassunto |
| Discord, canali dei disassemblati su PRET | https://discordapp.com/invite/vdTW48Q | idem, dal canale del gioco pertinente | la formula di conversione da Stat Experience a Effort Value, che nessuna implementazione pubblica pubblica |

## In attesa dell'utente: credenziali e abilitazioni

| Cosa | Stato | Che cosa sblocca |
|---|---|---|
| App Reddit di tipo script | il form si compila e il reCAPTCHA si spunta, ma alla pressione di create app la pagina si ricarica identica, cioe' un rifiuto lato server senza messaggio. Verificata la documentazione ufficiale il 2026-08-26: per l'uso gratuito e non commerciale NON esiste alcun modulo di registrazione preventiva, quindi quella ipotesi cade e il modulo di contatto serve solo alle richieste commerciali, aziendali, accademiche o di superamento dei limiti. Resta la prima causa, cioe' l'ammissibilita' dell'account: l'email verificata, e su un account collegato a Google anche l'esistenza di una password propria, che il pannello di modifica dell'email richiede | l'utente deve verificare l'email dalle impostazioni, impostando prima una password se l'account non ne ha una, e poi ritentare la creazione |
| Token utente di Discord | deciso il 2026-08-26 di NON usarlo: il rischio di essere riconosciuti come self-bot e vedersi chiudere l'account non e' accettabile. La via resta la copia manuale dei messaggi pertinenti in un file di testo sotto `_notes/fonti/`, che `tools/read-chat-export.py` digerisce comunque | nulla: e' una decisione chiusa, e cio' che resta e' materiale da procurare |
| Adattatore Wi-Fi USB per il track LDN | deciso il 2026-08-26 di partire con l'Archer T2U Nano che l'utente ha gia', accettando la riserva sul chip RTL8811AU, dove la modalita' monitor passa da un driver fuori albero; se non regge si acquista l'AC600 che la testimonianza di campo dichiara funzionante. Non e' bloccante finche' il resto del track e' in lettura | serve la prova sul campo, cioe' verificare se l'adattatore entra in modalita' monitor e vede i frame di annuncio |

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
| serve una trascrizione di un video senza sottotitoli automatici | il progetto `E:\local-audio-transcriptor`, ora funzionante perche' `deno` e' installato | riconoscimento vocale locale con marcatura temporale; verificato il 2026-08-26 che i due video arretrati, cioe' il primo di Goppier e quello sullo scambio locale su Switch, non hanno sottotitoli di alcun tipo, quindi questa e' l'unica via |
| l'utente produce un export di un canale Discord o di una chat Telegram | `tools/read-chat-export.py` | converte in Markdown filtrato per parola chiave, intervallo di date e lunghezza minima, e lo mette fra le fonti procurate a mano |
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

La pipeline funzionante e' quella descritta in `STACK.md`, cioe' scaricare i sottotitoli automatici con `yt-dlp` e ripulirli con `tools/vtt-to-text.py`, senza toccare l'audio. Il lavoro e' mio e non serve nulla dall'utente. Il `deno` che serviva al percorso alternativo e' installato, quindi anche il riconoscimento vocale locale e' disponibile.

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
