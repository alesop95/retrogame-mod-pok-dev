# Registro delle cose in sospeso

Questo file esiste perché l'utente non deve essere il sistema di memoria del progetto. Tutto ciò che è iniziato e non finito, atteso da qualcun altro, o rimandato a una condizione futura, sta qui: se una cosa non è scritta qui, per il progetto non è in sospeso.

A differenza di `progress.md` e `decisions.md`, che sono append-only, questo file si modifica: una voce chiusa si cancella, e la sua storia resta nel work log. Va letto a inizio sessione insieme a `index.md`, e le voci pertinenti al lavoro in corso vanno ricordate all'utente senza che le chieda. Le voci marcate come da ricordare sempre si ripetono a ogni sessione anche quando non sono pertinenti, perché così è stato chiesto.

## In attesa dell'utente: materiale da procurare

La consegna avviene salvando i file in `_notes/fonti/`, secondo la convenzione di `.claude/rules/web-sources-not-fetchable.md`. Ogni riga dice a quale domanda serve, perché chiedere una fonte senza dire cosa si cerca produce lavoro inutile.

Tutte le voci che stavano qui sono state consegnate. Il 2026-08-26 sono arrivati come screenshot il tutorial di GBAtemp, le ricerche nei canali di Pokemon Multiplayer Research con cinque filtri, quelle nel canale del Glitch City Research Institute con tre filtri, e quelle su GBAdev e PRET; il contenuto è stato letto e trasferito in `SOURCES.md`, nelle note di `docs/fonti/` e nelle note di studio, e il materiale grezzo è stato eliminato secondo la regola della fonte unica. Non resta materiale atteso.

Delle domande a cui quel materiale doveva rispondere, due hanno avuto risposta e una no. Sulle schede Wi-Fi la risposta è arrivata e ha corretto una premessa sbagliata del progetto, registrata in `sub-gba-switch-trading.md`. Sui difetti sfruttabili di generazione 3 la resa è stata molto oltre l'atteso, ed è in `docs/09-esecuzione-codice.md`. Sulla formula da Stat Experience a Effort Value la risposta non c'è, perché il canale dei disassemblati discute la modifica dei giochi e non la conversione fra generazioni; da un dato trovato là è stata però ricavata una derivazione, che sta in `docs/07-conversione-vincoli.md` etichettata come tale e da verificare.

È arrivata invece una voce nuova il 2026-08-28. Il thread di r/PokemonHome indicato dall'utente come contesto dell'obiettivo di collezione, cioè `https://www.reddit.com/r/PokemonHome/s/DrfatG6MJW`, non è leggibile da alcuno strumento di sessione per la ragione già documentata, e il titolo di un thread non è il suo contenuto. Serve il testo, e la domanda a cui deve rispondere è quale sia oggi il consenso della comunità sulla via più economica per completare la collezione prima della chiusura di Bank, perché quella risposta pesa su una delle due decisioni di perimetro aperte. Le vie sono la consegna manuale del testo in `_notes/fonti/` oppure l'automazione del browser dell'utente.

Restano due domande nuove per cui il materiale non basta, e per entrambe la via non è un altro screenshot.

| Domanda aperta | Come si chiude |
| se gli amministratori dei quattro server di community accettino un bot di archiviazione in sola lettura | verificato il 2026-08-31 che l'utente non ha il permesso di gestione su nessuno dei quattro, cioè che la tendina della schermata di invito elenca il solo server di prova: la via dell'autoinvito non esiste e la domanda resta interamente aperta. Si chiude chiedendo, dichiarando a che cosa serve e quali permessi si chiedono; è gratuito, e un no è un esito legittimo dopo il quale resta la copia manuale. L'ordine consigliato è GBAdev e Hex Maniac Advance per primi, perché sono community di sviluppo abituate agli strumenti, e Pokemon Multiplayer Research come terzo perché è quello di iscrizione più recente e con la domanda più circoscritta; PRET per ultimo, e con una richiesta stretta, perché la sua conoscenza autorevole sta nei disassemblati e negli issue, che sono già accessibili |
|---|---|
| quale chip monta l'adattatore Archer T2U Nano in mano all'utente | collegandolo e leggendone l'identificatore USB: il filtro `8811` nel canale non dà alcun risultato, quindi la testimonianza non esiste e la misura sostituisce la ricerca |
| se la derivazione da Stat Experience a Effort Value coincida con ciò che fa un'implementazione reale | confrontandola con il comportamento del PCCS sul suo sorgente, oppure con `PKHeX` su un caso costruito; è lavoro di lettura e non di raccolta |

## Tracciamento della spedizione del lettore di cartucce

Questa sezione è temporanea per costruzione e va cancellata il giorno in cui il lettore arriva, perché da quel momento non è più una pendenza ma un fatto. È qui e non nella scheda di un singolo track perché il lettore serve a tre track, cioè la correzione dello zaino di Smeraldo, la produzione delle strutture di partenza per il ponte e per lo scambio LDN, e tre delle quattro vie di iniezione di un evento del track delle distribuzioni.

| Cosa | Riferimento | Stato |
|---|---|---|
| GBxCart RW v1.4 Pro USB-C, ordinato il 18 agosto 2026 da insideGadgets | codice di tracciamento `CF173291165AU`, pagina https://parcelsapp.com/it/tracking/CF173291165AU | deciso il 2026-08-29: lo stato non si recupera dagli strumenti di sessione e non si insiste. Verificato il 2026-08-28 che la pagina è un'applicazione a pagina singola priva di dati nel documento servito, che l'interfaccia programmatica di quel servizio pretende una chiave, e che l'interfaccia del corriere presunto non conosce il codice; il suffisso `AU` rende probabile Australia Post ma è un'inferenza. La via è che l'agente chieda lo stato all'utente quando serve, cioè quando un passo dipende dall'arrivo del lettore, e l'utente lo procuri a mano. Da ricordare senza attendere che lo chieda |

## In attesa dell'utente: credenziali e abilitazioni

| Cosa | Stato | Che cosa sblocca |
|---|---|---|
| App Reddit di tipo script | chiusa il 2026-08-26 con esito negativo, e la voce resta solo per non far ripetere il tentativo. Entrambe le cause ipotizzate sono cadute: l'account ha una password propria e non dipende dal solo accesso via Google, l'email è stata verificata e il pannello vecchio la mostra come tale, e la documentazione ufficiale dice che per l'uso gratuito e non commerciale non esiste alcun modulo di registrazione preventiva. Con nome semplice, tipo script e reCAPTCHA spuntato il rifiuto persiste identico. Non è del tutto silenzioso: accanto al pulsante compare il rimando alla Responsible Builder Policy, quindi il rifiuto è legato all'ammissibilità secondo quella politica e non al contenuto del form. Un'ipotesi non verificata resta l'età o il punteggio dell'account | nulla da fare: la terza via della regola sulle fonti non recuperabili non è disponibile su questo account, e le fonti Reddit si leggono per la seconda o la quarta via |
| Token utente di Discord | riaperta e decisa il 2026-08-31 con ADR-019, in senso opposto alla decisione del 2026-08-26: l'utente ha scelto di usarlo con DiscordChatExporter sui server dove il bot non può essere invitato, accettando esplicitamente il rischio di sospensione dopo che gli era stato esposto tre volte, con la cadenza di poche esportazioni all'anno. Il token non si scrive in alcun file, nemmeno in `.env`, e si incolla nel comando al momento dell'uso | sblocca la lettura dei quattro server di community senza attendere il consenso degli amministratori. Resta valida e preferibile la via del bot dove il consenso si ottenga, perché non mette a rischio nulla; l'agente non ripropone l'obiezione, per la prescrizione scritta nella regola |
| Bot account Discord ufficiale | fatto il 2026-08-31: applicazione `lettore-fonti-retrogaming`, Message Content Intent abilitato, Public Bot spento, invito con i soli due permessi di lettura, token in `.env`, e catena provata da un capo all'altro su un server di prova creato dall'utente. Lo strumento `tools/fetch-discord.py` è quindi provato contro il servizio e non soltanto contro il proprio trasporto finto | resta da fare il passo che non è tecnico, cioè chiedere agli amministratori dei quattro server di community: dei quattro nessuno è dell'utente, quindi senza il loro sì la via resta disponibile solo sui server propri |
| Adattatore Wi-Fi USB per il track LDN | deciso il 2026-08-26 di partire con l'Archer T2U Nano che l'utente ha già. La riserva registrata prima poggiava su una premessa sbagliata: la testimonianza positiva riguarda l'Archer T2U Plus, il cui utente dichiara `driver: rtw_8821cu`, cioè un chip RTL8821CU servito dal driver in albero `rtw88` senza alcun driver custom, e non l'RTL8811AU che si era supposto. Il filtro `8811` nel canale non dà risultati, quindi su quel chip non esiste testimonianza. Non è bloccante finché il resto del track è in lettura | il primo passo non è comprare né cercare ma misurare: collegare l'adattatore e leggerne l'identificatore USB, da cui si ricavano chip e driver. Se cade nella famiglia `rtw88` la strada è aperta, altrimenti conviene uno dei modelli dichiarati affidabili |

## Fonti in sospeso, da ricordare sempre

Queste non hanno una via di recupero e non ne avranno: si consultano solo entrandoci di persona. Vanno ricordate a ogni sessione, come richiesto, così che la decisione di usarle o no sia presa e non dimenticata.

| Community | Link | Ambito |
|---|---|---|
| PRET | https://discordapp.com/invite/vdTW48Q | disassemblati e decompilazioni |
| Glitch City Research Institute | https://discord.com/invite/EA7jxJ6 | glitch ed esecuzione di codice in Gen 1 e 2 |
| GBAdev | https://discord.gg/ctGSNxRkg2 | sviluppo homebrew GBA e toolchain |
| Hex Maniac Advance Development | https://discord.com/invite/x9eQuBg | editing di ROM GBA |

## Strumenti da invocare quando si verifica una condizione

Questa è la tabella che l'agente deve consultare da sé: ogni riga dice quando ricordare uno strumento all'utente, invece di attendere che se lo ricordi lui.

| Condizione che si verifica | Strumento da ricordare | Che cosa se ne ottiene |
|---|---|---|
| esiste un salvataggio Gen 3 su cui iniettare un evento | `Gen3-WCTool` di Project Pokemon, e la sua avvertenza | inietta una carta meraviglia in un salvataggio estratto; se una carta è già presente va esportata e conservata prima di sovrascrivere, perché può essere un evento non ancora preservato dalla comunità |
| si valuta come portare in Home un esemplare di generazione 3 | la catena Parco Amico, Trasferitore, Poke Transporter e Bank, e il calendario | serve un Nintendo DS o DS Lite per il primo passaggio, due apparecchi DS per il secondo, e tutto va completato prima del 26 febbraio 2027; ogni passaggio è irreversibile e pretende la stessa lingua ai due capi |
| esiste per la prima volta un dump di salvataggio Gen 3 | `gba-save-extraction-smeraldo/tools/emerald_bag_decode.py` | validazione delle sezioni, identificazione del gioco, smascheramento dello zaino, cinque classi di anomalia |
| esiste un dump di qualunque generazione | `PKHeX`, anche nella versione web | confronto campo per campo con `pokebridge`, che falsifica le permutazioni di etichette |
| serve scrivere un salvataggio sintetico da confrontare | `pokebridge` più `PKHeX` | la prova di conformità descritta in `docs/23-prove-eseguite.md`, che non richiede hardware |
| arriva il lettore GBxCart RW | `FlashGBX` | lettura e scrittura di cartucce e salvataggi |
| esiste una ROM Game Boy dumpata legittimamente | `BGB` con il cavo su TCP, oppure `mGBA` | collaudo del protocollo del cavo contro un gioco vero |
| serve ispezionare una ROM GBA | `HexManiacAdvance` | mappe dei dati e modifica esadecimale guidata |
| serve la trascrizione di un video | `yt-dlp`, installato su questa macchina | sottotitoli automatici senza passare dall'interfaccia |
| serve condensare una fonte molto lunga senza consumare contesto | il modello su Ollama a `http://192.168.20.58:11500` | sintesi locale di testo, con i limiti dichiarati in `STACK.md` |
| serve sapere con quale metodo un evento di generazione 3 è stato generato | `tools/catalogo-eventi-gen3.py`, con il percorso di un clone di PKHeX | il catalogo delle 177 distribuzioni con specie, livello, allenatore, lingua, identificativo, metodo, lucentezza e derivazione del sesso; si rigenera invece di modificarlo, e `--check` dice se è allineato alla fonte |
| un passo dipende dall'arrivo del lettore di cartucce | chiedere all'utente lo stato della spedizione | il codice è `CF173291165AU`; lo stato non si recupera dagli strumenti di sessione, quindi lo procura l'utente a mano, e la richiesta va fatta senza attendere che se lo ricordi |
| si aggiungono o si rigenerano tabelle di dati | `pokemon-gen12-gen3-bridge-original-hardware/tools/extract_charmaps.py` | tabelle caratteri rigenerate dai charmap, con verifica delle sentinelle |
| prima di ogni commit | `python tools/md-unwrap.py --check .` e `python tools/lint-md-commands.py .` | conformità alla convenzione Markdown e ai comandi su riga singola |
| dopo commit che toccano i `covers-paths` delle schede | la skill `sync-context` | rilevamento del drift e bump del checkpoint |
| si chiude una milestone | un report in LaTeX sotto `reports/`, con `latexmk -pdf` | documento datato che fotografa risultati, metodo e limiti, con taglio da telecomunicazioni |
| serve una trascrizione di un video senza sottotitoli automatici | il progetto `E:\local-audio-transcriptor`, che però non è installato | riconoscimento vocale locale con marcatura temporale; verificato il 2026-08-26 che i due video arretrati, cioè il primo di Goppier e quello sullo scambio locale su Switch, non hanno sottotitoli di alcun tipo, quindi questa è l'unica via. Attenzione allo stato reale, verificato il 2026-08-26: `deno` c'è, nella versione 2.9.5, ma il comando `transcribe` non è sul PATH e `uv tool list` non riporta alcuno strumento installato, quindi il progetto è su disco e non è allestito. Prima di usarlo va installato con lo script che porta con sé, e quella è una decisione dell'utente perché scarica i modelli di riconoscimento vocale, che pesano |
| esiste un bot account Discord invitato in un server | `tools/fetch-discord.py`, provato contro il servizio il 2026-08-31 | legge la cronologia di un canale con impaginazione, cursore per il solo delta e filtri; il token si legge da `.env`, il presidio rifiuta un token che non sia di un bot, e gli identificativi vanno passati come numeri perché il servizio non dice quale campo sia sbagliato |
| serve esportare in blocco un canale con i suoi allegati, o rileggere una discussione lunga in forma comoda | `DiscordChatExporter` con il bot token, poi `tools/read-chat-export.py` sul JSON prodotto | esportazione in HTML, testo, JSON o CSV, con `--media` per gli allegati; la portata è quella del bot, cioè i soli server dove è stato invitato, quindi non sostituisce la richiesta agli amministratori |
| l'utente produce un export di un canale Discord o di una chat Telegram | `tools/read-chat-export.py` | converte in Markdown filtrato per parola chiave, intervallo di date e lunghezza minima, e lo mette fra le fonti procurate a mano |
| si collega per la prima volta un adattatore Wi-Fi USB destinato al track LDN | la lettura del suo identificatore USB, e la tabella di compatibilità in `SOURCES.md` | dice subito se il chip cade in una famiglia con driver in albero capace di modalità monitor, che è ciò che decide la praticabilità del track |
| si vuole provare il track LDN senza installare Linux | il demone `ldnd` con Zadig e l'archivio `linux-firmware` | esecuzione su Windows senza macchina virtuale, con la procedura descritta in `docs/11-wireless-locale-e-ponte-switch.md`; ricordare che dopo la riassegnazione a WinUSB quell'adattatore non fa più da scheda di rete |
| il ponte ha prodotto il primo modulo di codice, condizione verificata il 2026-08-25 | il gate del server MCP code-context, rimandato per ADR-010 | estrazione di simboli e riferimenti da `pokebridge/` senza versare i file in contesto; la proposta va rifatta perché la condizione che la rimandava non vale più, e resta la facoltà di rimandarla ancora |
| il ponte ha un comando di test, condizione verificata il 2026-08-25 | un `CLAUDE.md` annidato in `pokemon-gen12-gen3-bridge-original-hardware/` | dichiarazione dei soli comandi di build, lint e test di quella cartella, cioè `python tests/run_tests.py`; mai stato, che resta nella scheda del sottoprogetto |

## Debito di lettura

Ciò che è raggiungibile e non ancora letto. Il debito si chiude leggendo, non aspettando.

| Fonte | Stato |
|---|---|
| `pokeyellow` e `pokegold` | disassemblati non ancora clonati; servono per le differenze di offset di Giallo e di Oro e Argento |
| Data Crystal, mappe RAM di Rosso e Blu e di Cristallo | non lette; la pagina di Gen 3 è stata letta e ha reso poco |
| Bulbapedia, pagina sull'esecuzione di codice arbitrario | non letta; l'argomento è coperto dal mirror di Glitch City e dal dev log |
| `3dbrew` | non letto; serve al track 3DS quando si toccheranno i salvataggi delle cartucce dumpate |
| documentazione navigabile di pokeemerald | non letta; il sorgente clonato la rende poco necessaria |
| `gameboy-spoof` | citato come antenato di `arduino-boy` ma non trovato: il proprietario indovinato dà 404, va cercato il repository giusto |
| `REONTeam/trade-corner` e `REONTeam/libmobile` | l'organizzazione è stata letta ma questi due repository no, e riguardano lo scambio e il protocollo dell'adattatore mobile |
| riferimento delle classi di `ldn.readthedocs.io` | letta la pagina di ingresso, non il riferimento delle interfacce |

Le sei voci che erano qui e non ci sono più sono state lette il 2026-08-25: il blog di Phasip, `pepijndevos/arduino-boy`, `vaguilar/pokemon-red-cable-club-hack`, il progetto REON a livello di organizzazione, `switch-lan-play` e la pagina di ingresso di `ldn.readthedocs.io`. Ciò che ne è venuto sta nelle rispettive note sotto `docs/fonti/`.

## Trascrizioni da produrre

La pipeline funzionante è quella descritta in `STACK.md`, cioè scaricare i sottotitoli automatici con `yt-dlp` e ripulirli con `tools/vtt-to-text.py`, senza toccare l'audio. Su quella il lavoro è mio e non serve nulla dall'utente. Per i due video che restano quella pipeline non si applica, perché non hanno sottotitoli di alcun tipo, e serve il riconoscimento vocale locale: qui il lavoro non è interamente mio, perché il progetto che lo fa è su disco ma non installato, e installarlo comporta lo scarico dei modelli. È una decisione dell'utente, non un passo da dare per fatto.

Il debito di lettura sulle trascrizioni è chiuso: il 2026-08-26 tutte e sei quelle prodotte sono state lette per intero e ciò che documentano è confluito in `SOURCES.md` con la profondità necessaria a citarle, più tre punti nuovi nella sezione 11 della referenza dei formati, di cui due chiusi lo stesso giorno sul sorgente. Restano due video da trascrivere, e per entrambi è stato verificato il 2026-08-26 che non esistono sottotitoli di alcun tipo, automatici o manuali: l'unica via è il riconoscimento vocale locale.

| Video | Link | Perché serve |
|---|---|---|
| Goppier, lo scambio impossibile | https://www.youtube.com/watch?v=inMbtwmVlKQ | è il più importante dei due, perché il video successivo dello stesso autore vi rimanda per la struttura del circuito e per la questione se un GBA possa parlare direttamente il protocollo Gen 2, che è un punto aperto capace di cambiare il confronto fra le quattro opzioni |
| Scambio locale su Switch in FRLG | https://www.youtube.com/watch?v=epCf87MTLnk | serve al track LDN, ed è il presupposto di quel track visto dal lato utente |

I canali senza un video specifico, cioè Goppier, Lorenzooone, im a blisy, RETIRE, TheZZAZZGlitch, Retro Game Mechanics Explained e Displaced Gamers, restano da esplorare per scegliere quali video valga la pena trascrivere: è una decisione da prendere, non una trascrizione da lanciare.

## Punti tecnici aperti

| Punto | Dove è registrato |
|---|---|
| se un verificatore di legittimità accetti un esemplare prodotto da una ricreazione fedele di un evento | `recreate-pokemon-distributions-events/STUDIO-01-distribuzioni-gen3-e-ricreazione.md`; è la domanda che decide se il sesto track raggiunga il suo obiettivo, e si risponde senza hardware costruendo un esemplare con `pokebridge` e sottoponendolo a PKHeX |
| se la funzione di BIOS numero 11 citata dalla fonte sulle distribuzioni sia la decompressione LZ77 verso memoria di lavoro | idem, sezione 4; va confrontata con la tabella delle chiamate di sistema di GBATEK, e la fonte non dichiara la notazione del numero |
| se la posta di generazione 3 stia nella sezione quattro del salvataggio | idem, sezione 5; il numero delle sezioni, la rotazione e la doppia copia sono già verificati sul sorgente, questo dato no |
| se l'archivio degli eventi di Project Pokemon manchi davvero dei campioni degli eventi dichiarati non chiusi | `recreate-pokemon-distributions-events/STUDIO-02-metodi-di-generazione.md`, sezione 8; è la domanda che dice se il progetto possa contribuire alla conservazione invece di consumarla, e si chiude leggendo l'archivio |
| se la sezione di script del salvataggio impiegata dal Dono Segreto sia la stessa che il dev log dello strumento di trasferimento chiama sezione 30 | idem; le due descrizioni coincidono in dimensione e funzione, ma la numerazione non è stata confrontata sul sorgente |
| se una collezione completa in Home resti possibile dopo la chiusura di Bank, dato che si afferma che una specie di terza generazione non sia riproducibile dalle vie moderne | idem, sezione 10; affermazione di fonti secondarie non verificata, e cambia il senso della scadenza da urgenza a irreversibilità |
| quale lingua abbiano le cartucce di quarta e quinta generazione da dumpare, dato che ogni passaggio della catena verso Home pretende la stessa lingua ai due capi | `STACK.md` e `sub-3ds-modding.md`; è una verifica sulle cartucce e non una ricerca, e va fatta prima di pianificare i trasferimenti |
| offset dei salvataggi Gen 2 per lingue diverse dall'inglese | sezione 11 della referenza dei formati |
| dimensione esatta del blocco di posta Gen 2 | idem |
| tabella dagli indici interni Gen 1 ai numeri nazionali, da generare | idem, ed è il prossimo strumento naturale |
| vettori di prova esternalizzati su file invece che dentro i metodi | `docs/20-architettura-codice.md`, dichiarato come debito tecnico |
| conformità di `pokebridge` verificata contro `PKHeX` | `docs/23-prove-eseguite.md`, è il controllo che costa meno e falsifica più cose |
| data di disponibilità di Rosso Fuoco e Verde Foglia su Switch | schede `sub-3ds-modding.md` e `sub-gba-switch-trading.md`, fonti in conflitto |
| se l'Archer T2U Nano, chip RTL8811AU, entri in modalità monitor con il driver fuori albero | scheda `sub-gba-switch-trading.md`; la macchina non ha Wi-Fi integrato e la prova si farà con l'adattatore che l'utente ha già |
| se i programmi di Pokemon Automation per Rosso Fuoco e Verde Foglia su Switch tocchino lo scambio locale | `poke-automation-study/STUDIO-01-architettura-e-perimetro.md`, ed è la domanda che collega il track dell'automazione a quello dello scambio |
| se il canale del Mobile Adapter GB apra una strada alternativa al cavo per il lato Gen 2 | nota `docs/fonti/reon.md`, da valutare |
| se l'affermazione di PkSploit regga alla prova, cioè se un microcontrollore sostituisca il lettore per le cartucce Game Boy | nota `docs/fonti/pksploit.md`, richiede hardware |
| quale politica adottare quando la somma degli EV convertiti sfora il tetto di 510 | `docs/07-conversione-vincoli.md`. Non si tratta più di cercare una formula altrui: verificato il 2026-08-26 sul sorgente che la libreria della community azzera gli EV con una funzione che si chiama `convertEVs`, quindi la conversione va scritta e la politica va decisa, non trovata |
| se la routine di radice quadrata del gioco vada replicata invece che approssimata, dato che la fonte riporta 63002 dove la radice matematica darebbe 63504 | idem, ed è rilevante solo se si vuole fedeltà al margine |
| quale chip monti l'Archer T2U Nano, dato che il nome commerciale AC600 copre chip diversi | `sub-gba-switch-trading.md`; si misura, non si cerca |
| se anche Rubino e Zaffiro su Switch riceveranno il supporto al Wireless Adapter | affermazione di terzi ricavata dall'ispezione del binario dell'emulatore, non verificata |
| se il trasferimento richieda il cavo Link del Game Boy Color e i cavi del Game Boy Advance non funzionino | affermazione trovata il 2026-08-26 in una sintesi di fonti secondarie, non ancora verificata sul sorgente né sul materiale del tool. Se confermata è un requisito hardware che il progetto non aveva registrato, e va nella scheda del ponte prima di qualsiasi acquisto di cavi |

## Decisioni aperte

| Decisione | Stato |
|---|---|
| se l'obiettivo di collezione in Pokemon Home riapra il perimetro su Pokemon Bank e Pokemon Transporter | aperta, nata il 2026-08-28 con il sesto track. L'obiettivo dipende in modo essenziale da quei due titoli, perché Poke Transporter è l'unico ingresso verso Home per tutto ciò che precede l'ottava generazione, e l'assistenza su di essi è esclusa dalla regola `hardware-and-perimeter.md` per una motivazione che sta in `_notes/perimetro-bank-transporter.md`. Non esiste via tecnica alternativa, quindi la decisione è dell'utente e va registrata come ADR invece di essere fatta scivolare dentro un altro lavoro. Fino a quel momento il track lavora su tutto ciò che precede l'ultimo tratto |
| se le vie di iniezione che richiedono materiale di terze parti siano dentro il perimetro | aperta, nata il 2026-08-28. Tre delle quattro vie di iniezione di un evento chiedono una ROM di distribuzione da mettere su una scheda riprogrammabile oppure un salvataggio precostituito per l'e-Reader, e la regola esclude i salvataggi scaricati da internet. Va notato che non si tratta di un salvataggio di un gioco Pokemon da importare sulla console, quindi la norma non si applica in modo automatico e la decisione non è ovvia; resta che il perimetro va dichiarato prima di procurare il materiale. La quarta via, cioè l'iniezione diretta nel salvataggio con il lettore, è quella che pone meno domande |
| ADR-008, quale delle quattro opzioni implementative per il ponte | aperta; il costo relativo è cambiato e l'analisi aggiornata sta in `docs/30-opzioni-implementative.md` |
| se cancellare e ricreare il repository su GitHub per certezza sulla bonifica | rimandata; oggi si accetta che i commit orfani restino raggiungibili per hash fino al garbage collector, come registrato in ADR-014 |
| che cosa debba essere il track dell'automazione | parzialmente decisa il 2026-08-26: per ora studio, cominciato con la prima nota nella cartella del sottoprogetto. Resta aperto se diventerà riuso della parte su microcontrollore in comune con l'opzione D del ponte oppure automazione vera come obiettivo indipendente. Sul perimetro c'è una buona notizia, cioè che il progetto di riferimento dichiara console non modificate e nessun accesso alla memoria, quindi il suo perimetro è compatibile con le nostre regole |
| se usare il token utente di Discord per gli export | chiusa il 2026-08-26: no. Il rischio di sospensione dell'account non è accettabile, e le community si leggono copiando a mano i messaggi pertinenti |

## Strumenti da costruire

| Strumento | Stato | Che cosa serve prima |
|---|---|---|
| caricatore di salvataggi verso hardware | scritto e collaudato nella sua parte non distruttiva, cioè `tools/save-deploy.py`: esamina il file, identifica il gioco, pretende i due backup su volumi distinti e produce il piano dei cinque passi. La scrittura non è implementata e lo dichiara | per la cartuccia, il lettore e un collaudo su un esemplare sacrificabile; per la scheda SD, la decisione su quale percorso sia quello giusto per il titolo installato |
| generatore del salvataggio sintetico per il confronto con PKHeX | da scrivere, e non richiede nulla | è il prossimo passo tecnico più utile del ponte |
| generatore della tabella indici di specie | da scrivere, e non richiede nulla | ultimo dato costante ancora trascritto a mano |
| esportazione degli strumenti verso il template | da fare con un handoff, come per la regola sulle fonti non recuperabili | riguarda `read-chat-export.py`, `fetch-reddit.py`, `vtt-to-text.py` e `build-source-map.py`, che non sono specifici di questo dominio |
| esportazione verso il template di `fetch-discord.py` e della regola sulle fonti non recuperabili | fatta il 2026-08-31, dopo l'irrobustimento e il collaudo contro il servizio. Il template non aveva la regola, contrariamente a quanto avevo affermato senza verificarlo, e non aveva nessuno dei quattro strumenti della sua famiglia: l'esportazione è stata quindi la creazione del pacchetto `community-sources` e della regola, non l'aggiornamento di una sezione. Lo strumento è stato generalizzato copiando il file e sostituendo la sola prosa, con verifica che le righe di codice differenti fossero soltanto messaggi e dati di prova, cioè tredici su cinquecentocinquanta e nessuna di logica; il self-test della copia passa trentasette controlli come l'originale | resta da portare nel template il resto della famiglia, cioè `fetch-reddit.py`, `read-chat-export.py` e `vtt-to-text.py`, con lo stesso metodo. `catalogo-eventi-gen3.py` non si esporta, perché è specifico di questo dominio |

## Blocchi materiali

| Blocco | Che cosa impedisce |
|---|---|
| lettore GBxCart RW non ancora arrivato | lettura e scrittura di cartucce, prova da un capo all'altro su dati reali, e indirettamente il collaudo del protocollo contro un gioco vero perché serve una ROM dumpata. Dal 2026-08-28 blocca anche tre delle quattro vie di iniezione di un evento; lo stato della spedizione è nella sezione dedicata di questo file |
| discovery hardware non fatta | la scelta fra le quattro opzioni di ADR-008; la lista delle domande sta in `docs/10-multiboot-hardware.md` |
| driver CH340 non confermati e porta COM non annotata | l'uso del lettore quando arriverà; è il prossimo passo dichiarato del track Smeraldo |
