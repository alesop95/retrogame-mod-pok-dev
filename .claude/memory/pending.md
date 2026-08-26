# Registro delle cose in sospeso

Questo file esiste perche' l'utente non deve essere il sistema di memoria del progetto. Tutto cio' che e' iniziato e non finito, atteso da qualcun altro, o rimandato a una condizione futura, sta qui: se una cosa non e' scritta qui, per il progetto non e' in sospeso.

A differenza di `progress.md` e `decisions.md`, che sono append-only, questo file si modifica: una voce chiusa si cancella, e la sua storia resta nel work log. Va letto a inizio sessione insieme a `index.md`, e le voci pertinenti al lavoro in corso vanno ricordate all'utente senza che le chieda. Le voci marcate come da ricordare sempre si ripetono a ogni sessione anche quando non sono pertinenti, perche' cosi' e' stato chiesto.

## In attesa dell'utente: materiale da procurare

La consegna avviene salvando i file in `_notes/fonti/`, secondo la convenzione di `.claude/rules/web-sources-not-fetchable.md`. Ogni riga dice a quale domanda serve, perche' chiedere una fonte senza dire cosa si cerca produce lavoro inutile.

| Fonte | Link | Formato atteso | Domanda a cui serve |
|---|---|---|---|
| GBAtemp, salvataggio Smeraldo | https://gbatemp.net/threads/save-failed-on-real-pokemon-emerald.645336/ | testo o Markdown, corpo dei messaggi | perche' una scrittura su cartuccia originale puo' non restare |
| GBAtemp, cartuccia senza batteria | https://gbatemp.net/threads/gba-unlicensed-batteryless-sram-cart-pokemon-emerald-save-writing-issues.681601/ | idem | come si riconosce dal dump un hardware di salvataggio non originale |
| GBAtemp, scambio senza fili Gen 1 e 2 | https://gbatemp.net/threads/mission-wireless-trading-on-gen1-and-gen2-pokemon-games.632492/ | idem | quali tentativi di sostituire il cavo esistono e con che hardware |
| GBAtemp, LDN3 su console modificata | https://gbatemp.net/threads/ryujinx-adds-ldn3-feature-allowing-emulator-users-to-play-online-with-cfw-switch-consoles.622169/ | idem | esperienze di campo su schede Wi-Fi in modalita' monitor |
| PokeCommunity, zaino corrotto | https://www.pokecommunity.com/showthread.php?p=8992088 | idem | quali sintomi produce uno zaino corrotto da codici trucco |
| Ryujinx, LDN3 | https://blog.ryujinx.org/introducing-ldn3/ | HTML o Markdown | come e' incapsulato il traffico fra emulatore e console; il dominio non risolve da qui |

## In attesa dell'utente: credenziali e abilitazioni

| Cosa | Stato | Che cosa sblocca |
|---|---|---|
| App Reddit di tipo script | il form e' compilato e manca solo la spunta del reCAPTCHA; poi identificativo e segreto vanno in `.env` insieme a `REDDIT_USER_AGENT` | rende Reddit una fonte di prima classe tramite `tools/fetch-reddit.py`, che oggi non e' mai stato eseguito contro il servizio |
| Verifica dell'API dopo la creazione | da fare al primo uso: se arriva un 401 o un 403 con credenziali valide, serve anche la registrazione all'uso dell'API che il form menziona | chiude la nota di stato dentro lo strumento e le voci di Reddit nel registro delle fonti |

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
| serve una trascrizione di un video senza sottotitoli automatici | il progetto `E:\local-audio-transcriptor`, ora funzionante perche' `deno` e' installato | riconoscimento vocale locale con marcatura temporale |

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

La pipeline funzionante e' quella descritta in `STACK.md`, cioe' scaricare i sottotitoli automatici con `yt-dlp` e ripulirli con `tools/vtt-to-text.py`, senza toccare l'audio. Il primo video e' stato fatto il 2026-08-25 e la sua trascrizione sta in `_notes/fonti/`. Restano gli altri, e sono lavoro mio: non serve nulla dall'utente.

Una decisione dell'utente resta invece aperta su un punto: il download dell'audio risponde 403 perche' manca un runtime JavaScript, e servirebbe installare `deno`. Non e' necessario finche' i video hanno sottotitoli automatici, e lo diventa per quelli che non ne hanno.

| Video | Link | Perche' serve |
|---|---|---|
| Goppier, lo scambio impossibile | https://www.youtube.com/watch?v=inMbtwmVlKQ | idem, ed e' il video che l'articolo di Hackaday cita |
| Goppier, lo scambio impossibile | https://www.youtube.com/watch?v=inMbtwmVlKQ | senza sottotitoli automatici: serve il riconoscimento vocale, ora possibile |
| Scambio locale su Switch in FRLG | https://www.youtube.com/watch?v=epCf87MTLnk | idem; serve al track LDN |

Delle nove trascrizioni in elenco il 2026-08-25 ne sono state prodotte cinque dai sottotitoli automatici, una e' risultata senza parlato perche' e' una dimostrazione muta, e due restano da fare con il riconoscimento vocale. I testi prodotti stanno in `_notes/fonti/` e vanno ancora letti uno per uno: finora sono stati condensati e letti solo quello sul processo di sviluppo e quello di Goppier.

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
| quale scheda Wi-Fi ha questa macchina e se supporta la modalita' monitor | scheda `sub-gba-switch-trading.md`, e ora esiste la lista di compatibilita' |
| se il canale del Mobile Adapter GB apra una strada alternativa al cavo per il lato Gen 2 | nota `docs/fonti/reon.md`, da valutare |
| se l'affermazione di PkSploit regga alla prova, cioe' se un microcontrollore sostituisca il lettore per le cartucce Game Boy | nota `docs/fonti/pksploit.md`, richiede hardware |

## Decisioni aperte

| Decisione | Stato |
|---|---|
| ADR-008, quale delle quattro opzioni implementative per il ponte | aperta; il costo relativo e' cambiato e l'analisi aggiornata sta in `docs/30-opzioni-implementative.md` |
| se cancellare e ricreare il repository su GitHub per certezza sulla bonifica | rimandata; oggi si accetta che i commit orfani restino raggiungibili per hash fino al garbage collector, come registrato in ADR-014 |

## Blocchi materiali

| Blocco | Che cosa impedisce |
|---|---|
| lettore GBxCart RW non ancora arrivato | lettura e scrittura di cartucce, prova da un capo all'altro su dati reali, e indirettamente il collaudo del protocollo contro un gioco vero perche' serve una ROM dumpata |
| discovery hardware non fatta | la scelta fra le quattro opzioni di ADR-008; la lista delle domande sta in `docs/10-multiboot-hardware.md` |
| driver CH340 non confermati e porta COM non annotata | l'uso del lettore quando arrivera'; e' il prossimo passo dichiarato del track Smeraldo |
