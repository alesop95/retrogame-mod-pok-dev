# Controllo prima della chiusura di Bank: che cosa è in HOME e che cosa deve ancora passare

> Documento generato da `tools/controllo-prima-di-bank.py --scrivi`. Non si modifica a mano: si rigenera dopo ogni giro. Conta i soli esemplari passati a HOME, letti dal giudizio `dopo-20261126-giro17.json` attraverso `tools/in_home.py`: 8521 esemplari in 17 gruppi (DIAMANTE1, GIAPPONE2, GIRO17, HOME1, HOME10, HOME2, HOME3, HOME4, HOME5, HOME6, HOME7, HOME8, HOME9, RIDATA1, RIDATA2, VERDEFOGLIA1, ZAFFIRO1). Il totale dell'app, 8557 il 2026-11-26 dopo il giro 17, comprende anche i 34 che erano in HOME prima del giro 1 e quelli arrivati da GO, che i giudizi non leggono, e i 996 vecchi da liberare, che hanno un sostituto identico salvo la data.

## Il verdetto

Tutte le misure di questo documento sono complete sugli esemplari in HOME: caselle di specie e forma, sfide di Bank, fiocchi e sfere, voci del foglio «Bank Closing», statici, doni e uova, mosse e abilità, cromatici bloccati, Kyogre di blisy, marchio Game Boy, eventi della libreria contati sia per carta sia per allenatore e ID, varianti di terza generazione, Eventdex di Serebii e sfide della scheda Pokémon dell'app. La tabella «Gli obblighi delle decisioni» dice, per ogni decisione che ha chiesto di produrre qualcosa prima di Bank, quale misura la verifica. Restano fuori dalle misure, e sono scritte sotto: le sfide della scheda «Trades» dell'app, registrate il 2026-11-26 e non ancora misurate contro HOME; la ridatazione dei 1964 esemplari di terza e quarta generazione già in HOME con la data del 2026 (ADR-128), che il proprietario ha rimandato il 2026-11-26 alla fine, se avanza tempo (ADR-143), e che dopo la chiusura non si potrà più fare. Una misura vede soltanto ciò per cui è scritta: il 2026-11-25 le varianti di terza generazione erano sfuggite a ogni misura che contava per carta, e il 2026-11-26 si è aggiunta quella per allenatore e ID delle generazioni successive.

## Le misure complete

| Misura | Esito | Strumento |
|---|---|---|
| Caselle di specie e forma fino alla settima generazione | caselle che chiedono un esemplare: 936, coperte 936, mancanti 0 (specie 0, forme 0) | `tools/copertura-lotti.py` |
| Sfide di HOME che dipendono da Bank | 47 sfide controllate, 0 non coperte dalle sole copie per HOME:; Non controllabile dai dati: «Move Pokémon from Pokémon Bank», già fatta il 2026-11-03. | `tools/sfide-bank.py` |
| Sfere e fiocchi che si perdono con Bank | sfere: 82 coppie perse dall'eredità, 82 già nelle copie; 14 coppie precise del foglio, 13 già nelle copie; fiocchi: 63 che si ottengono giocando solo fino alla settima generazione, 27 che restano ottenibili; Fiocco Maestro dalla purificazione: 36 voci, da 18 specie Ombra | `tools/fiocchi-e-sfere-prima-di-bank.py` |
| Voci del foglio comunitario «Bank Closing» per origine, scambi, sesso e forma, livelli minimi, stelle | voci: 1792, coperte dalle copie per HOME: 1788, da produrre: 4; mosse senza specie: 50; delle 4 voci rimaste, il Mew in Cura Ball non esiste (ADR-116); Electivire al livello 15 e Magmortar al 14 di quarta generazione restano aperte perché nessun Electabuzz o Magmar di quarta generazione arriva a quei livelli nella libreria (ADR-116); la voce dell'anziano di Batikopoli in X e Y, troncata nel foglio («requests that you give him a Pokémon for him to take»), non nomina un incontro che il generatore possa costruire; le 50 mosse sono quelle che sul 3DS non si imparano e vanno alla fase Switch (`ELENCO-PRODUZIONE.md`) | `tools/elenco-produzione.py` |
| Eventi che la libreria PKHeX conosce fino alla settima generazione | 1654 gruppi, 1350 riconosciuti negli esemplari in HOME; dei 304 scoperti, 155 sono in HOME sotto una carta gemella con dati identici, 148 sono doni dell'epoca Game Boy, 1 prodotti e non in HOME, 0 mai prodotti | `pkhex-produci-elenco --carte` |
| Varianti d'allenatore e ID delle carte dalla quarta alla settima generazione (ADR-045, ADR-118) | 1528 varianti su 1135 carte, 157 con più varianti: presenti 1528, mancanti 0 | `pkhex-produci-elenco --varianti-carte` |
| Statici, doni e uova fino alla settima generazione (ADR-106, ADR-119) | 1460 gruppi: 1193 riconosciuti dalla libreria negli esemplari in HOME, 133 in HOME sotto un incontro gemello (stessa specie, gioco e livello), 112 doni dell'epoca Game Boy, 22 esclusi (Let's Go, che va in HOME da Switch, e il Pichu dalle orecchie a punta, che non si trasferisce (ADR-119)), residuo 0 | `pkhex-produci-elenco --statici` |
| Mosse del Pokédex delle mosse fino alla settima generazione (ADR-108) | 50 assenti dalle 184 che il 2026-11-03 nessuna copia conosceva: 34 mosse Z e Struggle, Light of Ruin, Zippy Zap, Splishy Splash, Floaty Fall, Pika Papow, Bouncy Bubble, Buzzy Buzz, Sizzly Slide, Glitzy Glow, Baddy Bad, Sappy Seed, Freezy Frost, Sparkly Swirl, Veevee Volley, Double Iron Bash, che sul 3DS non si imparano | questo strumento, sul giudizio |
| Abilità Galvanize e Power of Alchemy (ADR-108) | Galvanize sì, Power of Alchemy sì | questo strumento, sul giudizio |
| Cromatici bloccati e Deoxys, Manaphy, Darkrai cromatici (ADR-108) | Mew 5, Celebi 1, Spinda 5, Tipo Zero 1, Naganadel 2, Pikachu 12, Silvally 16, Poipole 14, Deoxys 2, Manaphy 1, Darkrai 1 | questo strumento, sul giudizio |
| Kyogre cromatico 6 IV di blisy (ADR-113, ADR-114) | 1 | questo strumento, sul giudizio |
| Marchio Game Boy che si perde con Bank (ADR-120) | Raichu di Alola 1, Exeggutor di Alola 1, Marowak di Alola 1, Meowth 1, Butterfree 1, Dunsparce con la costante multipla di 100 1 | questo strumento, sul giudizio |
| Eventi dell'Eventdex di Serebii dell'epoca di Bank | in HOME 1510; in HOME, non tutte le varianti d'allenatore 49; in HOME con una differenza di trascrizione 32 | questo strumento |

I doni dell'epoca Game Boy non passano da Bank per costruzione: esistono solo su cartuccia e il Trasportatore non li riceve, e vanno sulle cartucce dopo la sostituzione della pila (ADR-117).

Gruppi della libreria prodotti e non in HOME, o mai prodotti:

- EncountersWC3.Encounter_WC3 Event Gift Skitty ポケパーク 50318 (R): prodotto, non in HOME.

Lo Skitty dell'uovo del PokéPark (allenatore ポケパーク, ID 50318, con Rollout) è in HOME, HOME1 box 6 posto 10, dal lotto degli eventi di terza generazione: la libreria lo attribuisce a una voce gemella della stessa tabella, quindi la sua voce risulta scoperta ma l'esemplare c'è.

## Le varianti d'allenatore di terza generazione, da produrre

La libreria conosce 108 doni dei Pokémon Center giapponesi («Gotta Catch 'Em All», 2005-2006) e del Pokémon Center di New York (2003-2005), con 424 combinazioni di dono e nome d'allenatore valido: in Giappone il nome è la città del negozio (Sapporo esclusa dalla sesta distribuzione), a New York la macchina, PCNYb, PCNYc o PCNYd secondo la settimana (`Distribution3JPN.cs`, `Distribution3NY.cs`; PCNYa non è mai esistito). Le copie ne avevano 422, perché la libreria genera questi doni con un nome solo. ADR-118 vuole tutte le varianti che differiscono per allenatore: ne mancano 0, elencate una per riga in `_notes/lavoro/controllo-prima-di-bank/varianti-gen3.json`.

| Distribuzione | Varianti mancanti |
|---|---|

## Le sfide dell'app di HOME che si chiudono con i giochi del 3DS

I contatori dell'app coincidono con gli esemplari delle copie in HOME nella stessa sfera: l'app conta anche i Pokémon arrivati da Bank, un deposito per esemplare. Le sfide sotto si chiudono quindi con esemplari prodotti nei giochi dalla quarta alla settima generazione e portati con il giro 17. Fonte dei contatori: le schermate del proprietario del 2026-11-25; soglie da Bulbapedia, «Challenge (HOME)».

| Sfida | Nell'app | Nelle copie in HOME | Soglia d'oro | Da aggiungere |
|---|---|---|---|---|
| Deposit Pokémon in a Dive Ball! | 30 | 29 | 30 | 0 |
| Deposit Pokémon in a Luxury Ball! | 30 | 28 | 30 | 0 |
| Deposit Pokémon in a Timer Ball! | 30 | 30 | 30 | 0 |
| Deposit Pokémon in a Net Ball! | 30 | 28 | 30 | 0 |
| Deposit Pokémon in a Premier Ball! | 30 | 27 | 30 | 0 |
| Deposit Pokémon in a Repeat Ball! | 30 | 30 | 30 | 0 |
| Deposit Pokémon in a Beast Ball! | 30 | 30 | 30 | 0 |
| Deposit Pokémon in a Heal Ball! | 30 | 30 | 30 | 0 |
| Deposit Pokémon in a Quick Ball! | 30 | 28 | 30 | 0 |
| Deposit Pokémon in a Nest Ball! | 30 | 29 | 30 | 0 |
| Deposit Pokémon in a Fast Ball! | 30 | 30 | 30 | 0 |
| Deposit Pokémon in a Friend Ball! | 30 | 29 | 30 | 0 |
| Deposit Pokémon in a Heavy Ball! | 30 (stima dalla barra) | 30 | 30 | 0 |
| Deposit Pokémon in a Level Ball! | 30 (stima dalla barra) | 30 | 30 | 0 |
| Deposit Pokémon in a Love Ball! | 30 (stima dalla barra) | 30 | 30 | 0 |
| Deposit Pokémon in a Lure Ball! | 30 (stima dalla barra) | 30 | 30 | 0 |
| Deposit Pokémon in a Moon Ball! | 30 (stima dalla barra) | 30 | 30 | 0 |
| Deposit Pokémon in a Sport Ball! | 30 (stima dalla barra) | 30 | 30 | 0 |
| Deposit Pokémon that embody the ultimate in beauty! | 10 |  | 10 | 0 |
| Deposit Pokémon that embody the ultimate in coolness! | 10 |  | 10 | 0 |
| Deposit Pokémon that embody the ultimate in cuteness! | 10 |  | 10 | 0 |
| Deposit Pokémon that embody the ultimate in cleverness! | 10 |  | 10 | 0 |
| Deposit Pokémon that embody the ultimate in toughness! | 10 |  | 10 | 0 |
| Deposit 30 Ditto! | 30 | 30 | 30 | 0 |
| Deposit Pokémon that show off the ultimate sheen! | 10 |  | 10 | 0 |

Totale delle mancanze: 0. Un esemplare conta per tutte le sfide che soddisfa, quindi `tools/pkhex-sfide-app` mette i Ditto e gli esemplari con le condizioni al massimo dentro le sfere che hanno ancora un bisogno, e dà a dieci esemplari tutte e cinque le condizioni e la lucentezza a 255, che chiudono insieme le sei sfide di gara. La lucentezza si accumula soltanto con i Pokémelle di terza generazione e i Poffin di quarta (`ContestStatInfo.GetContestStatRestriction` della libreria), quindi quei dieci sono catture di Smeraldo; la sfida della lucentezza è aperta per il proprietario (2026-11-26) e il contatore, non fotografato, si prende a zero. Il lotto prodotto ne contiene 352.

Si chiudono solo su Switch, e restano alla fase Switch: Deposit a Pokémon that has the Mightiest Mark!; Deposit a Roaming Form Gimmighoul that was caught in Pokémon GO!; Deposit Caterpie, Weedle, Metapod, Kakuna, and Pikachu from Pokémon FireRed or Pokémon LeafGreen for Nintendo Switch!; Deposit Chansey and Tauros from Pokémon FireRed or Pokémon LeafGreen for Nintendo Switch!; Deposit Lapras from Pokémon FireRed or Pokémon LeafGreen for Nintendo Switch!; Deposit Porygon from Pokémon FireRed or Pokémon LeafGreen for Nintendo Switch!; Deposit Pokémon in a Feather, Gigaton, Great, Heavy, Jet, Leaden, Poké, Wing or Ultra Ball crafted in the Hisui region! (9 sfide); Deposit Pokémon that have the Jumbo Mark and the Mini Mark!; Fill in your Blueberry, Crown Tundra, Galar, Hisui, Hyperspace, Isle of Armor, Kanto (GBA), Kanto (Let's Go), Kitakami, Lumiose, Mega Evolution, Paldea and Sinnoh (BDSP) Pokédex (13 sfide); Register 10 forms of Furfrou!; Register 2 forms of Dudunsparce!; Register 2 forms of Maushold!; Register 3 varieties of Paldean Tauros!; Register 4 colors of Squawkabilly!; Register 4 different Ruinous Pokémon!; Register Alcremie's forms!; Register all the first partner Pokémon that Trainers can choose in Galar!; Register Applin and its 4 Evolutions!; Register Arceus from Pokémon Legends: Arceus!; Register Darkrai from Pokémon Legends: Z-A!; Register Dialga from Pokémon Brilliant Diamond or Pokémon Shining Pearl!; Register Eevee from Pokémon: Let's Go, Pikachu! or Pokémon: Let's Go, Eevee!; Register Eternal Flower Floette from Pokémon Legends: Z-A!; Register Galarian Articuno, Galarian Zapdos, and Galarian Moltres!; Register Hisuian Decidueye, Hisuian Typhlosion, and Hisuian Samurott!; Register Iron Bundle, Iron Hands, Iron Jugulis, and Iron Thorns!; Register Iron Leaves, Iron Boulder, and Iron Crown!; Register Ogerpon!; Register Okidogi, Munkidori, and Fezandipiti!; Register Palkia from Pokémon Brilliant Diamond or Pokémon Shining Pearl!; Register Pecharunt!; Register Pikachu from Pokémon: Let's Go, Pikachu! or Pokémon: Let's Go, Eevee!; Register Pokémon that have the Twinkling Star Ribbon!; Register Pokémon with all their effort levels maxed!; Register Scream Tail, Brute Bonnet, Flutter Mane, and Sandy Shocks!; Register Staraptor, Bidoof, and Bibarel from Pokémon Brilliant Diamond or Pokémon Shining Pearl!; Register Terapagos!; Register Torterra, Infernape, and Empoleon from Pokémon Brilliant Diamond or Pokémon Shining Pearl!; Register Ursaluna and Bloodmoon Ursaluna!; Register Walking Wake, Gouging Fire, and Raging Bolt!; Register Zacian from Pokémon Sword or Pokémon Shield!; Register Zamazenta from Pokémon Sword or Pokémon Shield!; Register Zygarde from Pokémon Legends: Z-A!.

## Eventi di Serebii con una differenza di trascrizione

Il confronto per specie, allenatore e ID manca 32 eventi; la sonda li ritrova tutti in HOME con una differenza nella trascrizione di Serebii, salvo quelli segnati da verificare.

| Specie | Evento | Allenatore e ID di Serebii | Esito |
|---|---|---|---|
| 6 Charizard | Pokémon I Choose You - Pokémon Pop-Up Store Distribution | 지우 170715 | stessa specie e allenatore, ID diverso da quello trascritto |
| 6 Charizard | Pokémon Mega Battle Festival Gift | メガトウキョー 08085 | stessa specie e allenatore, ID diverso da quello trascritto |
| 18 Pidgeot | Pokémon Game Show - Blue's Pidgeot | ブルー 02276 | stessa specie e ID, allenatore scritto in un'altra lingua o grafia |
| 25 Pikachu | Pokémon with You - Donation Gift | トウホク2018 201803 | stessa specie e ID, allenatore scritto in un'altra lingua o grafia |
| 27 Sandshrew | Toonverse & Pokémon Sun & Moon Collaboration - Code: 2ALOLAFORM7 | 썬문 170503 | stessa specie e allenatore, ID diverso da quello trascritto |
| 67 Machoke | Toys 'R' Us | JEREMY 24680 | stesso allenatore e ID su un'altra specie: evoluzione per scambio o voce sulla forma evoluta |
| 68 Machamp | Pokémon National Championships Distribution | ScreenPeekaz 07016 | stessa specie e allenatore, ID diverso da quello trascritto |
| 93 Haunter | Toys 'R' Us | JEREMY 24680 | stesso allenatore e ID su un'altra specie: evoluzione per scambio o voce sulla forma evoluta |
| 94 Gengar | Pokémon Center/Toys 'R' Us Christmas Event | クリスマス 12213 | stesso allenatore e ID su un'altra specie: evoluzione per scambio o voce sulla forma evoluta |
| 127 Pinsir | Pokémon World Championship Qualifier Gift | WCSK14 07064 | in HOME con allenatore WCS14K e ID 07054, HOME3 box 23: Serebii scrive WCSK14 07064 per tutti e sei i doni coreani del WCS 2014, la libreria (carte di sesta generazione) ne ha tre con 07064 e tre con 07054, e gli esemplari sono conformi |
| 129 Magikarp | Daisuki Club | ルイルイθ 02226 | stessa specie e ID, allenatore scritto in un'altra lingua o grafia |
| 133 Eevee | Extremespeed Genesect: Mewtwo Awakens - Event @ Lalaport Toyosu Mall | キヨ 07133 | stessa specie e allenatore, ID diverso da quello trascritto |
| 151 Mew | Pokémon World Championships 2017 Qualifier Gift | 170505 WCSK17 | stessa specie e ID, allenatore scritto in un'altra lingua o grafia |
| 212 Scizor | Pokémon Center/Toys 'R' Us Christmas Event | クリスマス 12213 | stesso allenatore e ID su un'altra specie: evoluzione per scambio o voce sulla forma evoluta |
| 214 Heracross | Pokémon World Championship Qualifier Gift | WCSK14 07064 | stessa specie e ID, allenatore scritto in un'altra lingua o grafia |
| 229 Houndoom | Pokémon World Championship Qualifier Gift | WCSK14 07064 | stessa specie e ID, allenatore scritto in un'altra lingua o grafia |
| 248 Tyranitar | Pokémon World Championship Qualifier Gift | WCSK14 07064 | in HOME con allenatore WCS14K e ID 07054, HOME3 box 23: Serebii scrive WCSK14 07064 per tutti e sei i doni coreani del WCS 2014, la libreria (carte di sesta generazione) ne ha tre con 07064 e tre con 07054, e gli esemplari sono conformi |
| 306 Aggron | Pokémon World Championship Qualifier Gift | WCSK14 07064 | stessa specie e ID, allenatore scritto in un'altra lingua o grafia |
| 310 Manectric | Pokémon World Championship Qualifier Gift | WCSK14 07064 | in HOME con allenatore WCS14K e ID 07054, HOME3 box 23: Serebii scrive WCSK14 07064 per tutti e sei i doni coreani del WCS 2014, la libreria (carte di sesta generazione) ne ha tre con 07064 e tre con 07054, e gli esemplari sono conformi |
| 381 Latios | 10th Anniversary | 10JAHRE 06277 | stessa specie e allenatore, ID diverso da quello trascritto |
| 385 Jirachi | Pokémon Center Tohoku - Tanabata Festival | たなばた 180811 | stessa specie e allenatore, ID diverso da quello trascritto |
| 385 Jirachi | Pokémon Center Tohoku - Tanabata Festival Gift | おりひめ 08016 | stessa specie e allenatore, ID diverso da quello trascritto |
| 385 Jirachi | Pokémon Center Tohoku - Tanabata Festival Gift | ひこぼし 08016 | stessa specie e allenatore, ID diverso da quello trascritto |
| 385 Jirachi | Daisuki Club | タナバタ 07078 | stessa specie e allenatore, ID diverso da quello trascritto |
| 417 Pachirisu | Pokémon National Championships - Sejun Park's Pachirisu | 박세준 05655 | stessa specie e allenatore, ID diverso da quello trascritto |
| 417 Pachirisu | Pokémon National Championships - Sejun Park's Pachisiu | 박세준 05655 | stessa specie e allenatore, ID diverso da quello trascritto |
| 445 Garchomp | Pokémon ORAS - Sinnoh Classic Entry Distribution Gift | シロナ 07225 | stessa specie e allenatore, ID diverso da quello trascritto |
| 491 Darkrai | Toys R Us & Nintendo World | ALAMOS 06281 | stessa specie e allenatore, ID diverso da quello trascritto |
| 571 Zoroark | EB Games/GAME/Toys 'R' Us | EVENT011 09161 | stessa specie e ID, allenatore scritto in un'altra lingua o grafia |
| 700 Sylveon | Pokémon Diamond & The Cocoon of Destruction - Prebooking Gift | 이브이하우스 04124 | stessa specie e allenatore, ID diverso da quello trascritto |
| 716 Xerneas | Pokémon XY & Z Tie-in Distribution. Code: POKEMONXYZ | XY&Z 04206 | stessa specie e allenatore, ID diverso da quello trascritto |
| 788 Tapu Fini | Japan Championships 2019 - Entry Gift | Poni 190419 | stessa specie e allenatore, ID diverso da quello trascritto |

## Eventi di Serebii con più nomi d'allenatore

49 eventi hanno in HOME solo una parte dei nomi che Serebii elenca. Per la terza generazione le varianti vere sono quelle della libreria, contate sopra: Serebii elenca anche PCNYa, che non è mai esistito, e Sapporo nella sesta distribuzione. Per le generazioni successive la misura per allenatore e ID delle carte della libreria, qui sopra, dice se manca una variante vera; i nomi che seguono non sono carte della libreria, ma grafie di Serebii di carte che in HOME ci sono (per esempio «ふめやすみ» per la carta «ふゆやすみ» 12270, «ETE2012» per «ÉTÉ2012», «Sunset» e «Moonset» per «Eclipse» 100419). Fino al 2026-11-26 questa frase diceva che ADR-045 conta un nome tradotto come un allenatore solo: era sbagliata, perché ADR-118 vuole tutte le varianti che differiscono per allenatore o per ID.

- 150 Mewtwo, Black & White - 1st Anniversary - European Games: mancano SPR2012 05012.
- 491 Darkrai, ANA & StoreGiveaway: mancano ふめやすみ 12270.
- 647 Keldeo, GAME, GameStop (UK): mancano ETE2012 08272.
- 788 Tapu Fini, 2019 International Challenge May - Entry Gift: mancano ポニ 190524.
- 791 Solgaleo, Cosmic Eclipse Tie In: mancano Sunset 100419.
- 791 Solgaleo, Cosmic Eclipse Tie In: mancano Sunset 100419.
- 792 Lunala, Cosmic Eclipse Tie In: mancano Moonset 100419.
- 792 Lunala, Cosmic Eclipse Tie In: mancano Moonset 100419.

## Gli obblighi delle decisioni, e la misura che li verifica

Ogni decisione che ha chiesto di produrre qualcosa prima di Bank, e dove si misura. Ricognizione del 2026-11-26 sulle decisioni da ADR-106 ad ADR-145 (ADR-146).

| Decisione | Che cosa chiede | Misura |
|---|---|---|
| ADR-106, ADR-119 | statici tipici, doni, vaganti, premi e uova | statici, doni e uova |
| ADR-107 | tutte le sfide di HOME | sfide di Bank; sfide della scheda Pokémon dell'app; sfide degli scambi, da misurare |
| ADR-108 | ciò che Bank porta con sé: mosse, abilità, cromatici bloccati | mosse; abilità; cromatici bloccati |
| ADR-109 | ogni casella di specie e forma fino alla settima generazione | caselle di specie e forma |
| ADR-110 | sfere, fiocchi, abilità, mosse, esemplari della cartuccia | sfere e fiocchi; voci del foglio (Smeraldo) |
| ADR-111 | i sei assi da collezionista del foglio «Bank Closing» | voci del foglio «Bank Closing» |
| ADR-113, ADR-114 | il Kyogre di blisy | Kyogre |
| ADR-115, ADR-116, ADR-117 | eventi della libreria, comunità RNG, pre-evoluzioni, livelli del Flauto Bianco | eventi della libreria; voci del foglio (pre-evoluzioni, livelli minimi); comunità RNG chiusa da ADR-117: 8 prodotti, 2 che non esistono con la specifica |
| ADR-118 | eventi senza carta e varianti per allenatore o ID | Eventdex di Serebii; varianti di terza generazione; varianti delle carte |
| ADR-120 | il marchio Game Boy | marchio Game Boy |
| ADR-121, ADR-122 | i 117 di FINALE in HOME | eventi della libreria (HOME10); i doni dell'epoca Game Boy vanno sulle cartucce dopo Bank (ADR-117) |
| ADR-126, ADR-128 | date d'incontro nelle finestre; giorno di Poké Transfer | ADR-126 fatta (giri 12 e 13); ADR-128 sui 1964 già in HOME rimandata dal proprietario (ADR-143) |
| ADR-141 | il Training Ribbon | fiocchi |
| ADR-142, ADR-143, ADR-144 | varianti di terza generazione, sfide dell'app, i tre di ウッツー | varianti di terza generazione; sfide dell'app; giro 17 in HOME |
| ADR-145 | le sfide degli scambi | da misurare: sezione qui sotto |

## Le sfide degli scambi dell'app, da misurare

Le sfide della scheda «Trades» dell'app di HOME, mai misurate prima del 2026-11-26. Elenco da Bulbapedia, «Challenge (HOME)», copia del 2026-11-03 (`_notes/fonti/raccolte/bulbapedia-home-2026-11-03/challenge.wiki`, righe 1321-1667); stato dalle foto 4-9 del proprietario del 2026-11-26 (privato, `_notes/fonti/consegne/2026-11-26-home-giro17-e-scambi/`). Come si completa una sfida «Trade X and Y!» non lo dice né Bulbapedia né Serebii (letta il 2026-11-26): se basta scambiare via uno X e uno Y, o se serve uno scambio di X contro Y, non lo dice nemmeno il dettaglio della sfida nell'app (il proprietario, 2026-11-26): il giro 18 porta quindi entrambe le metà di ogni coppia del 3DS, che bastano per entrambe le letture. Ogni scambio dà via il Pokémon per sempre: per gli scambi servono esemplari in più, non quelli della collezione.

| Sfida | Soglie | Stato il 2026-11-26 |
|---|---|---|
| Trade using the GTS! | 5/25/50 | 29/50, detto dal proprietario il 2026-11-26: mancano 21 |
| Trade using the Wonder Box! | 5/25/50 | 30/50, detto dal proprietario il 2026-11-26: mancano 20 |
| Trade using a Room Trade! | 5/25/50 | non cominciata, barra vuota nella foto 8 |
| Host Room Trades! | 1/5/20 | non cominciata, barra vuota; chiede il piano Premium |
| Have a Room Trade with 20 people in it! | una volta | non fatta; chiede una stanza piena, cioè la comunità |
| Deposit 10 Pokémon at once in the Wonder Box! | una volta | fatta, icona colorata nella foto 4 |

Coppie con entrambe le metà nei giochi del 3DS (20): Cranidos e Shieldon; Electivire e Magmortar; Gardevoir e Gallade; Glalie e Froslass; Hitmonlee e Hitmonchan; Latias e Latios; Lunatone e Solrock; Meowstic maschio e femmina; Nidoqueen e Nidoking; Nidorino e Gengar; Pikachu e Mimikyu; Pinsir e Heracross; Plusle e Minun; Staryu e Luvdisc; Throh e Sawk; Voltorb e Foongus; Vulpix e Vulpix di Alola; Gastrodon Mare Ovest e Mare Est; Zangoose e Seviper; lo stesso Pokémon due volte.

Coppie con una sola metà nei giochi del 3DS (24), l'altra su Switch: Arcanine (con Arcanine di Hisui); Avalugg (con Avalugg di Hisui); Braviary (con Braviary di Hisui); Corsola (con Corsola di Galar); Darmanitan (con Darmanitan di Galar); Dugtrio (con Wugtrio); Electrode (con Electrode di Hisui); Farfetch'd (con Farfetch'd di Galar); Goodra (con Goodra di Hisui); Lilligant (con Lilligant di Hisui); Linoone (con Linoone di Galar); Meowth (con Meowth di Galar); Mr. Mime (con Mr. Mime di Galar); Quagsire (con Clodsire); Qwilfish (con Qwilfish di Hisui); Rapidash (con Rapidash di Galar); Scizor (con Kleavor); Slowking (con Slowking di Galar); Stunfisk (con Stunfisk di Galar); Tentacruel (con Toedscruel); Weavile (con Sneasler); Weezing (con Weezing di Galar); Yamask (con Yamask di Galar); Zoroark (con Zoroark di Hisui).

Coppie della sola Switch (7): Armarouge e Ceruledge; Great Tusk e Iron Treads; Koraidon e Miraidon; Basculegion maschio e femmina; Polteageist e Sinistcha; Roaring Moon e Iron Valiant; Slither Wing e Iron Moth.

## Che cosa resta fuori da Bank, per scelta o perché non esiste fino al 3DS

Gli eventi di Scarlatto e Violetto, che il proprietario non ha, si recuperano scambiando con la comunità dopo la chiusura di Bank, a cominciare dal Dragapult con il marchio dell'Imbattibile; le sfide della sola Switch qui sopra; le forme e i fiocchi che si prendono solo giocando su Switch (`COPERTURA-LOTTI.md`, `FIOCCHI-PRIMA-DI-BANK.md`). La loro sorte è in `pending.md`, nelle voci da ricordare sempre.

