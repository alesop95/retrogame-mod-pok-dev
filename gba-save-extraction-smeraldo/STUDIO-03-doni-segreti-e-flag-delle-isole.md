# STUDIO-03. I biglietti delle isole, il Dono Segreto, e perché un oggetto nello zaino non basta

> Aperto il 2026-09-18 da un riscontro in gioco dell'utente. Riguarda la cartuccia reale di Pokemon Smeraldo italiano, allenatore ALEX, identificativo 45761, la stessa su cui `STUDIO-01` ha eseguito due giri di correzione dell'inventario. Non tratta lo zaino ma gli eventi di distribuzione, che sono un'altra cosa e hanno un'altra causa.

## 1. Il riscontro che ha aperto lo studio

Il 2026-09-18 l'utente ha verificato in gioco, sulla console vera, i quattro punti della checklist del secondo giro di correzione, che sono confermati e sono registrati in `STUDIO-01` sezione 21. Nello stesso giro ha fatto una prova che la checklist non chiedeva: è andato al porto di Selcepoli e al porto di Alghepoli per vedere se il gioco riconoscesse il Biglietto Eone, che era nello zaino da prima, e il Biglietto Aurora e la Mappa Stinta, che il secondo giro di correzione vi aveva inserito. Il marinaio non ha mai offerto alcuna isola. Ad Alghepoli le voci erano Porto Selcepoli, Parco Lotta e Annulla; a Selcepoli erano Porto Alghepoli, Parco Lotta e Annulla.

L'ipotesi dell'utente era che il Dono Segreto si fosse corrotto, e la ragione per cui l'ha formulata è solida: l'estate precedente aveva tentato di ottenere quegli stessi oggetti per la via ufficiale, cioè iniettando gli eventi Nintendo con l'homebrew NDSEventTool.nds su una scheda di flash, e il Dono Segreto non gli aveva consegnato nulla. Due fallimenti sullo stesso fronte suggeriscono una causa comune, e la causa comune sembrava essere il Dono Segreto stesso.

La misura dice un'altra cosa. Il Dono Segreto di questa cartuccia non è corrotto ed è perfettamente abilitato. Quello che manca è un'altra cosa, e non è un difetto del salvataggio: è la metà di una consegna che non è mai avvenuta.

## 2. La regola del gioco, sul sorgente

Il menu del marinaio non elenca le isole in base a ciò che si ha nello zaino. Le elenca in base a una congiunzione fra l'oggetto e un flag di evento, e i due termini della congiunzione sono indipendenti.

```c
// pret/pokeemerald, src/script_menu.c, CreateLilycoveSSTidalMultichoice
if (CheckBagHasItem(ITEM_EON_TICKET, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_SOUTHERN_ISLAND) == TRUE)
if (CheckBagHasItem(ITEM_MYSTIC_TICKET, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_NAVEL_ROCK) == TRUE)
if (CheckBagHasItem(ITEM_AURORA_TICKET, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_BIRTH_ISLAND) == TRUE)
if (CheckBagHasItem(ITEM_OLD_SEA_MAP, 1) == TRUE && FlagGet(FLAG_ENABLE_SHIP_FARAWAY_ISLAND) == TRUE)
```

Il flag non si accende mettendo l'oggetto nella tasca, e nessuna routine del gioco lo deduce dalla presenza dell'oggetto. Ad accenderlo è lo script di consegna del Dono Segreto, che fa le due cose nello stesso punto e nello stesso ordine, come si legge senza ambiguità nella consegna del Biglietto Aurora.

```
@ pret/pokeemerald, data/scripts/gift_aurora_ticket.inc
	giveitem ITEM_AURORA_TICKET
	setflag FLAG_ENABLE_SHIP_BIRTH_ISLAND
	setflag FLAG_RECEIVED_AURORA_TICKET
```

La consegna della Mappa Stinta in `gift_old_sea_map.inc` e quella del Biglietto Magico in `gift_mystic_ticket.inc` hanno la stessa forma con i flag corrispondenti. Il Biglietto Eone fa eccezione e merita il suo paragrafo, perché in Smeraldo non è un Dono Segreto ma un evento che viaggia fra due partite: `data/scripts/cable_club.inc` lo consegna durante la mescolanza dei registri, e anche là `giveitem ITEM_EON_TICKET` è seguito immediatamente da `setflag FLAG_ENABLE_SHIP_SOUTHERN_ISLAND`; la stessa coppia ricompare in `src/record_mixing.c`, dove `ReceiveGiftItem` accende il flag quando l'oggetto ricevuto è proprio il Biglietto Eone.

Ne segue il punto che questo studio esiste per fissare. Un oggetto scritto nello zaino da fuori, che sia con un Action Replay o con uno script deterministico come i due giri di `STUDIO-01`, ottiene la prima metà della consegna e non la seconda. Il risultato in gioco è un biglietto che esiste, si può guardare, ha la sua descrizione corretta, e non apre nulla. È esattamente ciò che l'utente ha osservato, e non è una corruzione: è l'aspetto normale di una consegna incompleta.

Vale registrare anche un dettaglio operativo che la prova dell'utente ha toccato senza saperlo. Le isole compaiono soltanto dal porto di Alghepoli, mai da quello di Selcepoli: la funzione che costruisce il menu con le isole è invocata dalle sole due righe di `data/maps/LilycoveCity_Harbor/scripts.inc`, e i testi di consegna del Dono Segreto lo dicono in chiaro ("It appears to be for use at the LILYCOVE CITY port"). La visita a Selcepoli non poteva quindi produrre nulla in nessun caso, e la sua assenza di isole non è un secondo indizio ma il comportamento atteso.

## 3. Lo strumento di misura, e gli offset con cui legge

Lo strumento è `tools/emerald_event_flags_decode.py`, scritto in questo giro di lavoro. Non scrive nulla: legge lo slot più recente, ricompone SaveBlock1 dalle sezioni con identificativo da 1 a 4, e riferisce lo stato dei flag pertinenti insieme all'elenco delle voci che il menu del porto costruirebbe con quello stato.

I flag di gioco stanno dentro SaveBlock1 a partire da 0x1270, un bit ciascuno, come dichiara `include/global.h` di `pret/pokeemerald` nel campo `flags[NUM_FLAG_BYTES]`; le variabili seguono a 0x139C. Il flag di identificativo n sta quindi nel byte 0x1270 più n diviso otto, al bit n modulo otto, e gli identificativi vengono da `include/constants/flags.h`, dove i flag di sistema si contano a partire da `SYSTEM_FLAGS`, che vale 0x860 perché è definito come `TRAINER_FLAGS_END + 1`.

Questa aritmetica non è stata data per buona sulla sola decompilazione, perché è quella su cui poggia ogni conclusione di questo studio. La conferma indipendente viene dal sorgente di NDSEventTool.nds 1.0, che è l'homebrew di cui parla la sezione 6 e che non ha alcun rapporto con il progetto pret. In `arm9/source/poke.cpp` quel programma verifica che il Dono Segreto sia abilitato leggendo `sav[0x40B + 0x1000 * sec[2]] & 0x8`, e verifica il Mistery Event leggendo `sav[0x405 + 0x1000 * sec[2]] & 0x10`. Poiché la sezione con identificativo 2 contiene i byte di SaveBlock1 da 3968 a 7935, il primo dei due indirizzi corrisponde a SaveBlock1 0x138B bit 3, che per l'aritmetica qui sopra è il flag 0x8DB, cioè `FLAG_SYS_MYSTERY_GIFT_ENABLE`; il secondo corrisponde a SaveBlock1 0x1385 bit 4, cioè il flag 0x8AC, `FLAG_SYS_MYSTERY_EVENT_ENABLE`. Le due fonti coincidono senza che nessuna sia stata usata per ricavare l'altra, e la coincidenza copre anche un terzo punto: l'indirizzo `sec[2] + 0x49A` che quel programma tocca per il Biglietto Eone di Smeraldo corrisponde a SaveBlock1 0x141A, che nella regione delle variabili è l'indice 63, cioè `VAR_DISTRIBUTE_EON_TICKET`, esattamente la variabile che `data/scripts/cable_club.inc` azzera dopo aver consegnato quel biglietto.

Una quarta coincidenza vale citarla perché chiude il cerchio sulla struttura. Quel programma scrive la Carta Meravigliosa a `sec[4] + 0x56C`, il suo script a `sec[4] + 0x8A8` e il dono da mescolanza dei registri a `sec[4] + 0xC94`, che tradotti in offset di SaveBlock1 sono 0x33EC, 0x3728 e 0x3B14: il secondo e il terzo sono esattamente `ramScript` e `recordMixingGift` come dichiarati da `include/global.h`, e il primo cade dentro `mysteryGift`, che comincia a 0x322C. Due fonti indipendenti concordano quindi su quattro strutture, ed è la ragione per cui questi offset si possono usare su una cartuccia vera invece che su una copia di prova.

Un'ultima verifica riguarda gli identificativi degli oggetti, che in `include/constants/items.h` sono un enumerato senza valori espliciti e vanno quindi numerati. Il Biglietto Eone risulta 275, il Biglietto Magico 370, il Biglietto Aurora 371 e la Mappa Stinta 376. I due di mezzo coincidono con quelli che `tools/emerald_bag_fix_round2.py` aveva già usato per inserire il Biglietto Aurora e la Mappa Stinta nella tasca, e la coincidenza vale da controllo incrociato perché quei valori erano stati ricavati in un'altra sessione e per un altro scopo.

## 4. Lo stato misurato della cartuccia

Misurato sul file che è oggi, byte per byte, il contenuto della cartuccia reale, cioè `Pokemon - Versione Smeraldo (Italy) - ALEX-45761-788h44m-2026-09-17-CORRETTO.sav`, slot con contatore 3598, quattordici sezioni valide su quattordici.

| Isola | Oggetto | Nello zaino | Flag di abilitazione | Voce al porto |
|---|---|---|---|---|
| Isola Remota | Biglietto Eone (275) | si | `FLAG_ENABLE_SHIP_SOUTHERN_ISLAND` (0x8B3): no | non compare |
| Monte Cordone | Biglietto Magico (370) | no | `FLAG_ENABLE_SHIP_NAVEL_ROCK` (0x8E0): no | non compare |
| Isola Materna | Biglietto Aurora (371) | si | `FLAG_ENABLE_SHIP_BIRTH_ISLAND` (0x8D5): no | non compare |
| Isola Suprema | Mappa Stinta (376) | si | `FLAG_ENABLE_SHIP_FARAWAY_ISLAND` (0x8D6): no | non compare |

Il menu che il porto di Alghepoli costruirebbe adesso è quindi Porto Selcepoli, Parco Lotta e Annulla, che è esattamente ciò che la fotografia mostra. La misura riproduce l'osservazione senza scarti, ed è il motivo per cui la diagnosi si può considerare chiusa e non probabile.

I flag di contorno dicono il resto. `FLAG_SYS_MYSTERY_GIFT_ENABLE` è acceso, quindi la voce Dono Segreto compare regolarmente nel menu iniziale e il canale delle Carte Meravigliose è funzionante; `FLAG_SYS_MYSTERY_EVENT_ENABLE` è spento, quindi il canale del Mistery Event, che è un'altra cosa, non è mai stato abilitato su questa partita. `FLAG_SYS_GAME_CLEAR` è acceso e la nave esiste, `FLAG_MET_SCOTT_ON_SS_TIDAL` è acceso ed è la ragione per cui il Parco Lotta compare fra le destinazioni, `FLAG_LANDMARK_SOUTHERN_ISLAND` è acceso e l'Isola Remota è segnata sulla mappa. Nessuno dei tre flag `FLAG_RECEIVED_*` dei doni è acceso, e nessuno dei quattro `FLAG_SHOWN_*` lo è: il gioco non ha mai consegnato nessuno di questi biglietti, e nessuno di essi è mai stato mostrato al marinaio. `VAR_DISTRIBUTE_EON_TICKET` vale zero, quindi questa partita non è configurata nemmeno per passare il Biglietto Eone a un'altra durante la mescolanza dei registri.

Le aree di salvataggio legate alla distribuzione sono coerenti con questo quadro. `recordMixingGift` a 0x3B14 è interamente a zero, e così `externalEventData` a 0x31B3 e `externalEventFlags` a 0x31C7, che sono le aree in cui i dischi di Colosseum e XD depositerebbero i propri dati; `mysteryGift` a 0x322C ha 221 byte non nulli su 876 con i primi sedici a zero, e `ramScript` a 0x3728 ha 428 byte non nulli su 1004. Nessuna di queste aree è stata interpretata campo per campo, perché interpretare una struttura di cui non si è verificato il formato è precisamente il modo in cui nascono le affermazioni che questo progetto evita: ciò che se ne ricava è soltanto che non sono aree vergini, il che è normale su una partita di 788 ore.

## 5. Il Biglietto Eone era già così, e questo esclude che l'abbiamo rotto noi

La domanda che segue naturalmente è se i due giri di correzione di `STUDIO-01` abbiano spento qualcosa. La risposta è no, ed è verificata su tutti e quattro i salvataggi conservati.

| Salvataggio | Biglietto Eone in zaino | Flag Isola Remota |
|---|---|---|
| `788h36m-2026-09-17.sav`, dump originale mai toccato | si | no |
| `788h36m-2026-09-17-CORRETTO.sav`, primo giro | si | no |
| `788h44m-2026-09-17.sav`, secondo dump | si | no |
| `788h44m-2026-09-17-READBACK.sav`, riletto dalla cartuccia dopo il secondo giro | si | no |

Il Biglietto Eone stava nello zaino senza il suo flag già nel dump originale, prelevato dalla cartuccia prima di qualunque nostra scrittura. La coppia rotta è quindi anteriore a questo progetto, ed è la firma tipica di un oggetto inserito con un Action Replay: l'apparecchio scrive lo slot dell'oggetto e non ha alcun modo di sapere che esiste un flag da accendere insieme. Che questa cartuccia abbia una storia di Action Replay è già registrato altrove nel sottoprogetto, quindi l'ipotesi non è nuova, ma questa è la prima misura che la conferma su un dato indipendente dagli esemplari nel deposito.

Per il Biglietto Aurora e la Mappa Stinta la coppia è rotta per una ragione diversa e nostra, e va detta con chiarezza: li ha inseriti il secondo giro di correzione su richiesta esplicita dell'utente, registrata in ADR-063, e quello script scriveva lo slot della tasca senza toccare i flag, per la buona ragione che nessuno sapeva ancora che esistessero. L'effetto è lo stesso dell'Action Replay, la causa no.

## 6. Perché il tentativo dell'estate scorsa non aveva funzionato, e che cosa quell'homebrew può davvero fare

L'homebrew a cui l'utente si riferisce è NDSEventTool.nds, una modifica di nds-savegame-manager di Pokedoc firmata da mrhappyasthma, distribuita come release 1.0 e accompagnata dal sorgente completo. Gira su un Nintendo DS con una scheda di flash nello slot superiore e la cartuccia Game Boy Advance in quello inferiore, legge il salvataggio della cartuccia, vi inietta un evento Nintendo ufficiale e lo riscrive. Il sorgente è stato letto per intero in questo giro di lavoro, ed è la fonte da cui vengono le conferme incrociate della sezione 3.

Quel programma distingue due canali, e la distinzione è la chiave di tutto. Il primo è la Carta Meravigliosa, che la funzione `wc_inject` scrive nell'area `mysteryGift`, e che per procedere pretende che `FLAG_SYS_MYSTERY_GIFT_ENABLE` sia acceso, rifiutandosi altrimenti con il messaggio "Mistery Gift is not enabled in savegame!". Il secondo è il Mistery Event, che la funzione `me_inject` scrive nell'area `ramScript`, e che pretende invece che `FLAG_SYS_MYSTERY_EVENT_ENABLE` sia acceso, rifiutandosi con "Mistery Event is not enabled in savegame!".

Su questa cartuccia il primo flag è acceso e il secondo è spento, come dice la sezione 4. Ne segue una previsione verificabile sul comportamento del programma, che è la spiegazione più probabile del fallimento dell'estate scorsa e che va marcata come tale, cioè come inferenza coerente con i dati e non come fatto osservato: sulla via delle Carte Meravigliose il programma avrebbe dovuto procedere, mentre sulla via del Mistery Event si sarebbe fermato con un rifiuto. Quale delle due vie l'utente avesse tentato non è ricostruibile a distanza di mesi, e va chiesto a lui invece di essere dedotto.

Va aggiunto che i due flag non si accendono da fuori nel gioco normale, ma da un evento in gioco che pochi giocatori incontrano per caso: `data/scripts/questionnaire.inc` mostra che entrambi si accendono compilando il questionario nel negozio con una frase precisa costruita con le parole facili, una frase per il Mistery Event e una per il Dono Segreto, e che in entrambi i casi serve avere già il Pokedex. Su questa partita il questionario del Dono Segreto è stato evidentemente compilato, perché il flag è acceso; quello del Mistery Event no.

Resta da registrare che cosa quel programma offra davvero su una cartuccia di Smeraldo italiana, perché il menu non è lo stesso per tutte le lingue e la differenza conta. Il programma riconosce la lingua dal quarto carattere del codice di gioco nell'intestazione della ROM, che per Smeraldo italiano è la I di `BPEI`, e in quel ramo il numero massimo di opzioni per Smeraldo è uno, cioè due voci. Le due voci sono il Biglietto Aurora nella Carta Meravigliosa italiana ufficiale e il Biglietto Magico in quella inglese. Non c'è alcuna Mappa Stinta per Smeraldo fuori dal ramo giapponese, dove esiste come distribuzione ufficiale, e il ramo inglese ne offre una esplicitamente marcata `unofficial_old_sea_map_E_eng`, cioè ricostruita e non originale. Non c'è nemmeno un Biglietto Eone per Smeraldo in quel menu, perché in Smeraldo il Biglietto Eone non è una Carta Meravigliosa ma l'evento fra partite descritto alla sezione 2.

Ne segue una conseguenza che decide le opzioni della sezione 9: per questa cartuccia, e con questa versione di questo strumento, esiste una via ufficiale documentata per il solo Biglietto Aurora in italiano e per il Biglietto Magico in inglese. Per la Mappa Stinta non esiste, e per il Biglietto Eone la via passa da un'altra partita.

### La testimonianza dell'utente, che conferma il meccanismo e contraddice la lettura del menu

Il 2026-09-18, mentre questo studio veniva scritto, l'utente ha riferito un fatto che va registrato per intero perché è una prova sul campo e perché è in tensione con il paragrafo precedente: su una seconda cartuccia di Smeraldo, diversa da questa, ha usato lo strumento del video ed è arrivato davvero all'Isola Suprema a prendere Mew con la Mappa Stinta.

Sul meccanismo la testimonianza conferma e non smentisce, ed è la parte che conta di più. Se l'isola si è aperta, il flag `FLAG_ENABLE_SHIP_FARAWAY_ISLAND` si è acceso, e si è acceso perché la consegna del Dono Segreto è avvenuta davvero in gioco eseguendo `giveitem` e `setflag` insieme. È esattamente il modello descritto alla sezione 2, osservato dal lato dell'esito invece che da quello del codice, e alza la diagnosi di questo studio da coerente a corroborata dall'esterno.

Sul menu, invece, la testimonianza è in tensione con quanto il sorgente della release 1.0 dice, e la tensione va dichiarata invece di essere appianata. In quel sorgente il ramo italiano per Smeraldo ha `maxoptions` a uno, e le due voci corrispondenti sono il Biglietto Aurora italiano e il Biglietto Magico inglese: nessuna Mappa Stinta. La Mappa Stinta per Smeraldo compare soltanto nel ramo giapponese, come distribuzione ufficiale, e nel ramo inglese come voce dichiarata non ufficiale dal nome della variabile stessa. Poiché la lingua non si sceglie da un menu ma viene letta dal quarto carattere del codice di gioco nell'intestazione della ROM, cioè dalla cartuccia inserita, la spiegazione più economica è che quella seconda cartuccia non fosse italiana ma inglese, dove la voce esiste all'indice 2. Le altre due spiegazioni possibili sono che lo strumento usato allora fosse una versione o una derivazione diversa dalla 1.0 qui letta, oppure che si trattasse di un altro strumento ancora.

Non si sceglie fra le tre per deduzione, perché tutte e tre sono compatibili con ciò che si sa, e la domanda da porre all'utente è una sola e semplice: di quale lingua è la seconda cartuccia. Fino a quella risposta resta stabilito soltanto ciò che il sorgente dice della release 1.0 su una cartuccia italiana, e resta stabilito, perché è stato letto e non ipotizzato.

Vale infine osservare che questa tensione non tocca la decisione presa alla sezione 10, e non la tocca per una ragione che non dipende da quale delle tre spiegazioni sia vera: la via ufficiale su questa cartuccia era comunque bloccata dal trabocchetto della sezione 7, che è indipendente dal menu dello strumento.

## 7. Il trabocchetto che renderebbe inefficace la via ufficiale adesso

Se si scegliesse di iniettare la Carta Meravigliosa ufficiale del Biglietto Aurora e di riceverla in gioco, il risultato con lo zaino nello stato attuale sarebbe nullo, e la ragione sta nella prima riga dello script di consegna.

```
@ pret/pokeemerald, data/scripts/gift_aurora_ticket.inc
	vgoto_if_set FLAG_RECEIVED_AURORA_TICKET, AuroraTicket_Obtained
	vgoto_if_set FLAG_BATTLED_DEOXYS, AuroraTicket_Obtained
	checkitem ITEM_AURORA_TICKET
	vgoto_if_eq VAR_RESULT, TRUE, AuroraTicket_Obtained
```

Il ramo `AuroraTicket_Obtained` si limita a ringraziare e non accende alcun flag. Poiché il Biglietto Aurora è già nella tasca, il terzo controllo sarebbe vero e la consegna verrebbe saltata, lasciando la situazione identica a prima. Peggio: il secondo controllo guarda `FLAG_BATTLED_DEOXYS`, che su questa cartuccia risulta acceso, quindi la consegna verrebbe saltata comunque anche a zaino vuoto. Lo stesso vale per la Mappa Stinta, il cui script salta la consegna se `FLAG_CAUGHT_MEW` è acceso, e anche quello risulta acceso.

Per far funzionare la via ufficiale del Biglietto Aurora occorrerebbe quindi, prima di riceverla, togliere l'oggetto dalla tasca e spegnere `FLAG_BATTLED_DEOXYS`, che sono due scritture sul salvataggio: la via ufficiale, su questa cartuccia, non è più raggiungibile senza prima manipolare il salvataggio, che è precisamente ciò che si voleva evitare passando dalla via ufficiale. Vale la pena scriverlo perché è un caso pulito di una situazione che questo progetto incontra spesso, cioè una via legittima resa inapplicabile dallo stato in cui la partita si trova.

## 8. Le anomalie di contorno, marcate come da verificare

Leggendo i flag sono emerse tre cose che questo studio non ha chiesto e che non vanno né nascoste né promosse a conclusione.

`FLAG_CAUGHT_MEW`, `FLAG_BATTLED_DEOXYS` e `FLAG_ARRIVED_AT_NAVEL_ROCK` sono accesi, mentre `FLAG_DEFEATED_DEOXYS`, `FLAG_DEFEATED_MEW` e `FLAG_ARRIVED_ON_FARAWAY_ISLAND` sono spenti. Sono flag che una partita accende visitando luoghi ai quali questa partita, per quanto la sezione 4 dimostra, non ha mai potuto accedere, perché nessuno dei biglietti ha mai avuto il suo flag di abilitazione e nessuno è mai stato mostrato al marinaio.

Il controllo incrociato sul Pokedex non discrimina e va detto perché sarebbe facile prenderlo per una conferma: Mew, Deoxys, Lugia, Ho-Oh, Jirachi e Celebi risultano tutti visti e catturati, ma il Pokedex di questa partita è completo e un Pokedex completo è compatibile sia con una storia di catture sia con una scrittura da Action Replay. Nel deposito, per il censimento del primo giro, Mew e Deoxys non ci sono, mentre Lugia e Ho-Oh ci sono ma provengono dalla distribuzione italiana "10ANNI" su Rubino, cioè da uno scambio e non dal Monte Cordone.

L'ipotesi più economica è che anche questi flag vengano dalla stessa origine del Biglietto Eone senza il suo flag, cioè da una manipolazione con Action Replay fatta anni fa, e che il loro effetto pratico oggi sia quello descritto alla sezione 7, cioè bloccare le consegne ufficiali di due doni su tre. Resta un'ipotesi e va marcata come tale: nessuna fonte interna al salvataggio può distinguere un flag acceso da un apparecchio da un flag acceso dal gioco, perché il salvataggio conserva il bit e non la sua storia.

## 9. Le tre vie da qui, con quello che ciascuna costa

Nessuna di queste va intrapresa senza una decisione esplicita dell'utente, e per due di esse la decisione tocca la legittimità della collezione e non solo la tecnica, quindi va registrata come ADR.

La prima via è accendere i tre flag di abilitazione direttamente sul salvataggio, con uno script deterministico dello stesso tipo dei due giri di `STUDIO-01`, riverificato prima e dopo la scrittura fisica e accompagnato dal read-back. Costa tre bit e una scrittura sulla cartuccia. Rende immediatamente raggiungibili l'Isola Remota, l'Isola Materna e l'Isola Suprema, con i loro esemplari. È la via tecnicamente più semplice e la più coerente con quanto già deciso in ADR-063, che aveva ammesso l'inserimento dei due biglietti mai ricevuti registrandoli come prodotti e mai come corruzione restituita: accendere i flag completa quella stessa decisione invece di aprirne una nuova, ma va detto che la completa nel senso di renderla efficace, il che è un fatto nuovo e merita il suo ADR.

La seconda via è la via ufficiale, cioè iniettare le Carte Meravigliose originali con NDSEventTool e farsele consegnare dal gioco. Ha il pregio che il flag lo accende il gioco stesso e che l'esemplare ottenuto porta le circostanze di incontro che il gioco gli assegna, il che conta per un progetto che distingue legale da legittimo. Ha tre costi. Il primo è che serve l'hardware, cioè un Nintendo DS o DS Lite con slot per cartucce Game Boy Advance e una scheda di flash funzionante. Il secondo è che, come dice la sezione 7, non funzionerebbe nello stato attuale senza prima togliere l'oggetto dalla tasca e spegnere due flag, quindi comporta comunque una manipolazione del salvataggio. Il terzo è che copre il solo Biglietto Aurora in italiano e il Biglietto Magico in inglese, e non copre né la Mappa Stinta né il Biglietto Eone.

La terza via è non fare nulla su questa cartuccia e procurarsi altrove gli esemplari che le isole avrebbero dato. Va nominata perché è una scelta reale e perché il track `pokedex-home-completo` ha già una catena che porta esemplari di terza generazione fino al deposito: se l'obiettivo è la specie nel deposito e non l'evento sulla cartuccia, questa via non tocca affatto il salvataggio reale e quindi non ha alcun rischio.

Una quarta possibilità va nominata solo per escluderla, così che nessuno la riapra credendola inesplorata: mescolare i registri con una seconda partita che abbia il Biglietto Eone e la variabile di distribuzione impostata trasferirebbe davvero il biglietto con il suo flag, per la via che la sezione 2 documenta, ma richiede una seconda cartuccia di terza generazione in quello stato e un cavo di collegamento, e produce il solo Biglietto Eone. Non è sbagliata, è sproporzionata.

## 10. La decisione dell'utente, e la prima via eseguita

L'utente ha scelto la prima via il 2026-09-18, senza esitazione e nella stessa conversazione in cui le tre erano state esposte. La decisione è registrata come ADR-065 e la sua motivazione è quella che la sezione 9 le attribuiva: costa tre bit, completa una decisione già presa in ADR-063 invece di aprirne una nuova, e non dipende da hardware che non c'è.

Vale registrare anche che cosa la decisione non ha scelto, perché in un progetto che distingue legale da legittimo l'alternativa scartata è parte del ragionamento. La via ufficiale avrebbe prodotto esemplari con le circostanze di incontro che il gioco assegna, ma su questa cartuccia era comunque bloccata dal trabocchetto della sezione 7, che avrebbe richiesto di togliere il biglietto dalla tasca e di spegnere `FLAG_BATTLED_DEOXYS`: due scritture sul salvataggio per poter percorrere la via che le scritture voleva evitare. Fra due vie che toccano entrambe il salvataggio, si è presa quella che lo tocca meno.

Il perimetro di ciò che questa scelta produce va detto con precisione, perché è più stretto di quanto sembri. Accendere i flag non fabbrica alcun esemplare e non scrive nulla nel deposito: rende raggiungibili tre luoghi del gioco, dove gli incontri avverranno poi normalmente, con le meccaniche e i valori che il gioco genera in quel momento. Gli esemplari che ne verranno saranno quindi ottenuti giocando, e l'unica cosa prodotta da fuori resta il permesso di salire sulla nave.

## 11. Il terzo giro di correzione: come è stato costruito e verificato

Lo strumento è `tools/emerald_event_flags_fix.py`, scritto lo stesso giorno sullo stampo dei due giri precedenti: non tocca mai il file in ingresso, produce un file nuovo, e rifiuta di procedere se l'output coincide con l'input. Porta una precondizione deliberata che vale descrivere, perché è la simmetrica del difetto che questo giro esiste per riparare: prima di accendere un flag verifica che il suo oggetto sia davvero nella tasca Oggetti Chiave, e si ferma se manca. Senza quel controllo lo strumento potrebbe produrre la stessa coppia rotta nell'altro verso, cioè un flag acceso senza il suo biglietto, che è un difetto meno visibile e non meno reale.

Ciò che non fa è altrettanto deliberato. Non tocca i flag `FLAG_RECEIVED_*`, che dichiarano che un dono è stato consegnato dal Dono Segreto e che su questa partita sono spenti perché quella consegna non è mai avvenuta: accenderli scriverebbe un fatto falso e non servirebbe, perché il menu del porto non li guarda. Non tocca i flag `FLAG_SHOWN_*`, che il gioco accende da sé la prima volta che il biglietto viene mostrato al marinaio. E non tocca `FLAG_ENABLE_SHIP_NAVEL_ROCK`, perché il Biglietto Magico non è nella tasca.

Il file di partenza è `Pokemon - Versione Smeraldo (Italy) - ALEX-45761-788h44m-2026-09-17-READBACK.sav`, cioè il file riletto dalla cartuccia dopo il secondo giro, e non il file che vi era stato scritto: fra i due l'hash coincide, ma il riletto è quello che rappresenta davvero il supporto. La scelta è legittima perché l'utente ha dichiarato di non aver salvato durante la verifica in gioco del 2026-09-18, e in terza generazione il gioco non salva da sé: la cartuccia è quindi ancora a quel contenuto. La dichiarazione va comunque riverificata prima della scrittura, ed è il primo passo della procedura qui sotto.

Il risultato è `Pokemon - Versione Smeraldo (Italy) - ALEX-45761-788h44m-2026-09-18-CORRETTO.sav`, con hash SHA-256 che comincia per `91d22a5a`. Il confronto byte per byte con il file di partenza mostra quattro byte diversi e nessun altro, ed è esattamente il numero atteso.

| Indirizzo nel file | Prima | Dopo | Che cos'è |
|---|---|---|---|
| 0x02406 | 0xF7 | 0xFF | sezione 2, offset 0x406, bit 3: `FLAG_ENABLE_SHIP_SOUTHERN_ISLAND` |
| 0x0240A | 0x1D | 0x7D | sezione 2, offset 0x40A, bit 5 e bit 6: `FLAG_ENABLE_SHIP_BIRTH_ISLAND` e `FLAG_ENABLE_SHIP_FARAWAY_ISLAND` |
| 0x02FF6 | 0xBF | 0x27 | sezione 2, checksum, byte basso |
| 0x02FF7 | 0x6F | 0x70 | sezione 2, checksum, byte alto |

Due verifiche indipendenti chiudono la costruzione. La prima è che `emerald_event_flags_decode.py`, rilanciato sul file prodotto, riferisce i tre flag accesi e dichiara che il menu del porto di Alghepoli costruirebbe Isola Remota, Isola Materna e Isola Suprema. La seconda è che `emerald_bag_decode.py`, rilanciato sullo stesso file, produce una diagnosi identica riga per riga a quella del file di partenza, comprese le anomalie cosmetiche preesistenti sugli slot vuoti delle tasche Poke Ball e Macchine: nessun effetto collaterale su zaino, squadra, denaro o deposito.

Resta la scrittura fisica, che è un'operazione dell'utente e non dell'agente, e che segue la procedura di sempre. Si ricollega il lettore e si rilegge la cartuccia in un file nuovo; si confronta il suo hash con quello del file di partenza, cioè `e344f3cf`, per accertare che nel frattempo nessun salvataggio in gioco abbia mosso il supporto, e se l'hash non coincide questo giro va rifatto sul dump nuovo invece che scritto com'è. Si verifica che il secondo disco di backup sia montato e che vi stia la copia del file di partenza, perché il vincolo della doppia copia non ammette eccezioni. Si scrive il file `-CORRETTO`, si rilegge in un file `-READBACK` e si confronta l'hash con `91d22a5a`. Solo allora si va al porto di Alghepoli.

## 12. La scrittura sulla cartuccia vera: fatta e verificata il 2026-09-18

L'utente ha eseguito i quattro passi della sezione 11 nella stessa giornata, e le tre verifiche che la procedura prescrive sono tutte positive.

La prima è la datazione dello stato del supporto. Il dump prelevato prima di scrivere ha digest SHA-256 che comincia per `e344f3cf`, identico a quello del file riletto dopo il secondo giro: la cartuccia non era stata mossa da alcun salvataggio in gioco fra il 2026-09-17 e la verifica ai porti del 2026-09-18, il che conferma la dichiarazione dell'utente invece di darla per buona, e rende valido il file già preparato.

La seconda è il vincolo della doppia copia, che al momento della costruzione non era accertabile perché il secondo disco non risultava montato. Montato, contiene la copia del file di partenza a `e344f3cf`, quindi il vincolo era soddisfatto già prima della scrittura. Il nuovo stato è stato copiato a sua volta sul secondo disco e verificato per digest.

La terza è il read-back. Il file riletto dalla cartuccia dopo la scrittura, `Pokemon - Versione Smeraldo (Italy) - ALEX-45761-788h44m-2026-09-18-READBACK.sav`, ha digest che comincia per `91d22a5a`, identico a quello del file scritto: la scrittura è quindi verificata in modo indipendente dal software che l'ha eseguita, come nei due giri precedenti.

Resta un residuo di igiene e non di correttezza: il dump prelevato prima di scrivere è stato nominato fuori dallo schema di ADR-064. Poiché il suo contenuto è identico a quello di un file già presente, è per ADR-064 una copia di verifica ridondante, che non prende un nome proprio e non resta su disco oltre il controllo: va cancellato, e la cancellazione è dell'utente.

Manca il solo controllo in gioco, cioè andare al porto di Alghepoli e vedere se il marinaio offra Isola Remota, Isola Materna e Isola Suprema. L'utente lo ha fatto a sessione chiusa e ne riferirà alla ripresa.

## 13. Che cosa resta aperto, e che cosa non lo è

Resta aperto il solo controllo in gioco, cioè vedere al porto di Alghepoli se il marinaio offra davvero le tre isole: la scrittura fisica è stata fatta e verificata, come racconta la sezione 12.

Resta aperta una domanda che non è un ostacolo ma una chiusura di conoscenza, ed è quella della sezione 6, cioè di quale lingua sia la seconda cartuccia su cui l'utente ha ottenuto Mew con la Mappa Stinta. La risposta decide fra tre spiegazioni tutte compatibili con i fatti noti, e nessuna delle tre cambia alcuna decisione presa qui.

Restano aperte, marcate come da verificare e non azionabili adesso, le tre anomalie di contorno della sezione 8.

Non è aperto nulla sul Dono Segreto, che non è rotto: la voce nel menu iniziale funziona, il canale delle Carte Meravigliose è abilitato, e la domanda che ha aperto questo studio ha una risposta negativa. Non è aperto nulla sullo zaino, che i due giri di `STUDIO-01` hanno chiuso e che il riscontro visivo del 2026-09-18 ha confermato voce per voce. E non è più aperta la scelta fra le tre vie, che la sezione 10 ha chiuso.
