# Strategia Switch: che cosa comprare, che cosa catturare, che cosa generare

> Documento autorato del 2026-10-01. I numeri vengono da `STUDIO-SWITCH.md`, generato da `tools/studio-switch.py` sugli incontri di `tools/pkhex-incontri-switch` (clone PKHeX `e15d246`) e sul dataset `pokepc/dataset` (`5fd44c1`): se cambiano, si rigenera quello e si rilegge questo.

## Perché esiste

Il 2026-10-01 il proprietario ha a disposizione una Switch 2, con il solo Leggende Pokémon Z-A, e ha chiesto due cose. La prima è uno studio per avere tutte le voci della lista completa giocando sulle console moderne, cioè in quali giochi e come si ottengono. La seconda, detta subito dopo, è che tutto ciò che si riesce va comunque anche generato con la libreria come proveniente in modo legittimo da quel gioco, perché lo strumento c'è e non usarlo sarebbe uno spreco. Le due richieste hanno risposte diverse, e questo documento le tiene separate.

## Il perimetro della misura

Le voci sono quelle di `LISTA-COMPLETA.md` senza le forme da oggetto tenuto, 1393, con le forme femminili e cosmetiche distinte. Un incontro conta se è permanente, cioè giocabile oggi: i doni segreti, i raid e i focolai di distribuzione e i raid a sette stelle sono esclusi, perché le loro finestre sono chiuse. Ogni incontro è stato giudicato dalla libreria rigenerando l'esemplare con la specie e la forma cercate, e scartato se non è legale. Questo controllo ha tolto dal conto il Vivillon Motivo Poké Ball selvatico in Scarlatto, che il solo generatore d'incontri dava per buono, e le combinazioni di lettere di Unown con le stanze sbagliate. Cinque evoluzioni con una condizione che la simulazione non riproduce (Huntail, Gorebyss, Dudunsparce a tre segmenti, Gholdengo, Hydrapple) sono accettate con la condizione scritta e da verificare in gioco. I contenuti scaricabili si riconoscono dal luogo dell'incontro e contano come prodotti a parte.

## L'ordine di acquisto

Con i giochi in quest'ordine si coprono 1358 voci su 1393. Leggende Z-A, già posseduto, ne dà 437. Scarlatto con il DLC Il tesoro dell'Area Zero ne aggiunge 625, ed è l'acquisto che conta più di tutti gli altri insieme. Scudo con il DLC dell'Isola dell'armatura e delle Terre innevate della corona ne aggiunge 206. Diamante Lucente ne aggiunge 75, soprattutto le forme e le specie di Sinnoh che altrove non si catturano, fra cui Spinda. Leggende Pokémon Arceus ne aggiunge 11, Violetto 3 e Spada 1: queste ultime due sono le esclusive di versione, e si possono evitare scambiando con un'altra persona, perché Leggende Arceus e le seconde versioni costano un gioco intero per una manciata di voci. I due Let's Go non aggiungono nulla.

La scelta fra le versioni non è indifferente e va detta. L'ordine sceglie Scarlatto e Scudo perché con quelli il guadagno è massimo, ma il margine sulla versione opposta è di poche voci: chi preferisce Violetto o Spada perde le esclusive dell'altra e le recupera allo stesso modo, per scambio.

## Le 35 voci che nessun gioco per Switch dà

Ventinove di queste hanno comunque una via aperta. I berretti di Pikachu (Alola, Hoenn, Sinnoh, Unima, Kalos, Originale, Compagni), Celebi, Deoxys, Victini, Hoopa e Magearna sono già nelle copie per HOME preparate dal progetto; le forme Attacco, Difesa e Velocità di Deoxys e Hoopa Libero si ottengono poi per cambio di forma con gli oggetti chiave dei giochi per Switch, a partire dall'esemplare base. Pokémon GO, gratuito, dà il Rattata e il Raticate di Alola, il Pikachu Berretto Giramondo, i nove tagli di Furfrou e il Gimmighoul Errante, oltre a Celebi, Deoxys e Victini.

Sei voci non hanno oggi nessuna via legittima aperta: Floette Fiore Eterno, Magearna Colore Antico, Zarude e Zarude Papà, Acquecrespe e Fogliaferrea. Sono tutte eventi chiusi dell'era Switch o regali di HOME a tempo, e per loro le sole vie sono lo scambio con chi le possiede o la generazione di cui si parla sotto.

## La generazione per i giochi per Switch

La libreria genera e giudica anche i formati dei giochi per Switch: PK9 per Scarlatto e Violetto, PA9 per Leggende Z-A, PK8 per Spada e Scudo, PB8 per Diamante Lucente e Perla Splendente, PA8 per Leggende Arceus. Ogni voce di `STUDIO-SWITCH.md` con un incontro permanente si può quindi produrre come proveniente da quell'incontro, con lo stesso criterio di generatore e giudice dei lotti per il 3DS, e le sei voci da evento chiuso si possono produrre dai doni segreti della libreria.

Il collo di bottiglia non è la generazione ma la scrittura. Sul 3DS il progetto scrive nei salvataggi perché la console è modificata; una Switch 2 oggi non lo permette. Al 2026-10 non esistono firmware personalizzato, homebrew o modchip per la Switch 2: c'è soltanto un exploit di livello utente, pubblicato nel luglio 2026, che gira dentro il recinto di un'applicazione senza accesso al sistema né ai salvataggi, e i termini d'uso della console permettono a Nintendo di disattivare una Switch 2 modificata. Un esemplare generato non può quindi entrare in un gioco della Switch 2 del proprietario per via diretta.

Le vie che restano sono tre, e tutte richiedono una decisione del proprietario.

La prima è una Switch di prima generazione modificabile, cioè un modello che le vulnerabilità note coprono, da tenere sempre scollegata da internet. Su quella si scrive nei salvataggi come sul 3DS, e l'esemplare passa alla Switch 2 con lo scambio locale del gioco, che non usa la rete; dalla Switch 2, non modificata, va poi in HOME. È la via che replica il modello già in uso, e il suo costo è una console in più e la disciplina di non collegarla mai.

La seconda vale soltanto per la terza generazione. Dal 7 ottobre 2026 Rosso Fuoco e Verde Foglia per Switch si collegano a HOME, con la versione 4.1.0 dell'applicazione, che porta anche la capienza del piano a pagamento a 9000. Il track dello scambio GBA-Switch documenta una catena che porta un esemplare da un Game Boy Advance vero, o da un file `.pk3` sul PC, dentro Rosso Fuoco su una Switch 2 non modificata, ed è la stessa via che il progetto usa già per scrivere i salvataggi di terza generazione. Ha però bisogno delle chiavi di una console Switch, che si estraggono solo da una console modificata, quindi presuppone la prima via; e per `rules/hardware-and-perimeter.md` quelle chiavi non si caricano su un servizio di terzi senza averne verificato il sorgente.

La terza sono i servizi di scambio automatico della comunità, studiati nel track della generazione dai giochi su console moderna: consegnano per scambio ordinario un esemplare generato da altri, senza modificare nulla. Resta aperta la decisione di quel track, perché la politica ufficiale sui dati alterati prevede la sospensione dell'accesso a HOME e non esclude chi si rivolge deliberatamente a un servizio di generazione.

## Che cosa fare adesso

Giocare non dipende da nessuna di queste decisioni. Leggende Z-A dà già 437 voci, e Scarlatto con il suo DLC è il primo acquisto. Ciò che si cattura in gioco è legittimo per definizione e non pesa sul rischio dell'account. La generazione per i giochi per Switch resta preparabile sul PC in qualunque momento, perché non tocca la console, ed entra nel lavoro solo dopo che il proprietario avrà scelto una delle tre vie: la decisione è registrata in `.claude/memory/pending.md`.

## Fonti

Gli incontri sono quelli della libreria PKHeX (`_notes/fonti/cloni/pkhex`, `e15d246`), le disponibilità di GO e HOME vengono dal dataset `pokepc/dataset` (`5fd44c1`). Lo stato della modifica della Switch 2 viene da Notebookcheck, «Switch 2: Developer unveils a universal exploit that works entirely offline» (https://www.notebookcheck.net/Switch-2-Developer-unveils-a-universal-exploit-that-works-entirely-offline.1347373.0.html), e dal riepilogo di wayayeo.org dell'agosto 2026 (https://wayayeo.org/nintendo-switch-2-modding-early-homebrew-and-hack-news/), lette solo nell'estratto della ricerca e quindi da rileggere prima di una decisione. Il collegamento di Rosso Fuoco e Verde Foglia a HOME del 7 ottobre 2026 viene da Nintendo Life (https://www.nintendolife.com/news/2026/09/pokemon-home-firered-and-leafgreen-compatibility-update-arrives-next-week) e Nintendo Soup (https://nintendosoup.com/pokemon-home-support-for-pokemon-firered-leafgreen-switch-version-coming-october-7th-2026/), anche queste lette nell'estratto. La catena GBA-Switch è in `.claude/context/sub-gba-switch-trading.md`, la politica sui dati alterati in `.claude/context/sub-generation-from-switch.md`.
