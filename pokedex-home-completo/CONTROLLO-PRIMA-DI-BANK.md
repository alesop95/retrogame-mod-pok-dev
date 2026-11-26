# Controllo prima della chiusura di Bank: che cosa è in HOME e che cosa deve ancora passare

> Documento generato da `tools/controllo-prima-di-bank.py --scrivi`. Non si modifica a mano: si rigenera dopo ogni giro. Conta i soli esemplari passati a HOME, letti dal giudizio `dopo-20261125-zaffiro.json` attraverso `tools/in_home.py`: 7856 esemplari in 16 gruppi (DIAMANTE1, GIAPPONE2, HOME1, HOME10, HOME2, HOME3, HOME4, HOME5, HOME6, HOME7, HOME8, HOME9, RIDATA1, RIDATA2, VERDEFOGLIA1, ZAFFIRO1). Il totale dell'app, 7892 il 2026-11-25, comprende anche i 34 che erano in HOME prima del giro 1 e quelli arrivati da GO, che i giudizi non leggono, e i 996 vecchi da liberare, che hanno un sostituto identico salvo la data.

## Il verdetto

Prima del 2027-02-26 deve passare da Bank un altro giro, il 17, con 662 esemplari: 310 varianti d'allenatore dei doni di terza generazione dei Pokémon Center giapponesi e di New York che ADR-118 vuole tutte, e 352 esemplari che chiudono le sfide dell'app di HOME raggiungibili con i giochi del 3DS, meno delle 425 mancanze perché un esemplare conta per tutte le sfide che soddisfa (`tools/pkhex-sfide-app`). Tutte le altre misure sono complete. Resta un lavoro che dipende da Bank e che il proprietario ha rimandato il 2026-11-26 alla fine, se avanza tempo (ADR-143): ridatare i 1964 esemplari di terza e quarta generazione già in HOME con la data del 2026 (ADR-128); dopo la chiusura non si potrà più.

## Le misure complete

| Misura | Esito | Strumento |
|---|---|---|
| Caselle di specie e forma fino alla settima generazione | caselle che chiedono un esemplare: 936, coperte 936, mancanti 0 (specie 0, forme 0) | `tools/copertura-lotti.py` |
| Sfide di HOME che dipendono da Bank | 47 sfide controllate, 0 non coperte dalle sole copie per HOME:; Non controllabile dai dati: «Move Pokémon from Pokémon Bank», già fatta il 2026-11-03. | `tools/sfide-bank.py` |
| Sfere e fiocchi che si perdono con Bank | sfere: 82 coppie perse dall'eredità, 82 già nelle copie; 14 coppie precise del foglio, 13 già nelle copie; fiocchi: 63 che si ottengono giocando solo fino alla settima generazione, 27 che restano ottenibili; Fiocco Maestro dalla purificazione: 36 voci, da 18 specie Ombra | `tools/fiocchi-e-sfere-prima-di-bank.py` |
| Eventi che la libreria PKHeX conosce fino alla settima generazione | 1654 gruppi, 1350 riconosciuti negli esemplari in HOME; dei 304 scoperti, 155 sono in HOME sotto una carta gemella con dati identici, 148 sono doni dell'epoca Game Boy, 1 prodotti e non in HOME, 0 mai prodotti | `pkhex-produci-elenco --carte` |
| Eventi dell'Eventdex di Serebii dell'epoca di Bank | in HOME 1463; in HOME, non tutte le varianti d'allenatore 95; in HOME con una differenza di trascrizione 33 | questo strumento |

I doni dell'epoca Game Boy non passano da Bank per costruzione: esistono solo su cartuccia e il Trasportatore non li riceve, e vanno sulle cartucce dopo la sostituzione della pila (ADR-117).

Gruppi della libreria prodotti e non in HOME, o mai prodotti:

- EncountersWC3.Encounter_WC3 Event Gift Skitty ポケパーク 50318 (R): prodotto, non in HOME.

Lo Skitty dell'uovo del PokéPark (allenatore ポケパーク, ID 50318, con Rollout) è in HOME, HOME1 box 6 posto 10, dal lotto degli eventi di terza generazione: la libreria lo attribuisce a una voce gemella della stessa tabella, quindi la sua voce risulta scoperta ma l'esemplare c'è.

## Le varianti d'allenatore di terza generazione, da produrre

La libreria conosce 108 doni dei Pokémon Center giapponesi («Gotta Catch 'Em All», 2005-2006) e del Pokémon Center di New York (2003-2005), con 424 combinazioni di dono e nome d'allenatore valido: in Giappone il nome è la città del negozio (Sapporo esclusa dalla sesta distribuzione), a New York la macchina, PCNYb, PCNYc o PCNYd secondo la settimana (`Distribution3JPN.cs`, `Distribution3NY.cs`; PCNYa non è mai esistito). Le copie ne avevano 112, perché la libreria genera questi doni con un nome solo. ADR-118 vuole tutte le varianti che differiscono per allenatore: ne mancano 310, elencate una per riga in `_notes/lavoro/controllo-prima-di-bank/varianti-gen3.json`.

| Distribuzione | Varianti mancanti |
|---|---|
| PCJP Fifth | 77 |
| PCJP First | 15 |
| PCJP Fourth | 15 |
| PCJP Second | 15 |
| PCJP Sixth | 56 |
| PCJP Third | 94 |
| PCNY Box | 4 |
| PCNY Colosseum | 2 |
| PCNY Dragon | 9 |
| PCNY EXDragon | 5 |
| PCNY Evolution | 3 |
| PCNY Halloween | 8 |
| PCNY Monster | 4 |
| PCNY UnknownSpring | 3 |

## Le sfide dell'app di HOME che si chiudono con i giochi del 3DS

I contatori dell'app coincidono con gli esemplari delle copie in HOME nella stessa sfera: l'app conta anche i Pokémon arrivati da Bank, un deposito per esemplare. Le sfide sotto si chiudono quindi con esemplari prodotti nei giochi dalla quarta alla settima generazione e portati con il giro 17. Fonte dei contatori: le schermate del proprietario del 2026-11-25; soglie da Bulbapedia, «Challenge (HOME)».

| Sfida | Nell'app | Nelle copie in HOME | Soglia d'oro | Da aggiungere |
|---|---|---|---|---|
| Deposit Pokémon in a Dive Ball! | 15 | 14 | 30 | 15 |
| Deposit Pokémon in a Luxury Ball! | 15 | 13 | 30 | 15 |
| Deposit Pokémon in a Timer Ball! | 22 | 22 | 30 | 8 |
| Deposit Pokémon in a Net Ball! | 25 | 23 | 30 | 5 |
| Deposit Pokémon in a Premier Ball! | 20 | 17 | 30 | 10 |
| Deposit Pokémon in a Repeat Ball! | 27 | 27 | 30 | 3 |
| Deposit Pokémon in a Beast Ball! | 9 | 9 | 30 | 21 |
| Deposit Pokémon in a Heal Ball! | 14 | 14 | 30 | 16 |
| Deposit Pokémon in a Quick Ball! | 10 | 8 | 30 | 20 |
| Deposit Pokémon in a Nest Ball! | 13 | 12 | 30 | 17 |
| Deposit Pokémon in a Fast Ball! | 2 | 2 | 30 | 28 |
| Deposit Pokémon in a Friend Ball! | 4 | 3 | 30 | 26 |
| Deposit Pokémon in a Heavy Ball! | 2 (stima dalla barra) | 2 | 30 | 28 |
| Deposit Pokémon in a Level Ball! | 2 (stima dalla barra) | 2 | 30 | 28 |
| Deposit Pokémon in a Love Ball! | 2 (stima dalla barra) | 2 | 30 | 28 |
| Deposit Pokémon in a Lure Ball! | 2 (stima dalla barra) | 2 | 30 | 28 |
| Deposit Pokémon in a Moon Ball! | 2 (stima dalla barra) | 2 | 30 | 28 |
| Deposit Pokémon in a Sport Ball! | 2 (stima dalla barra) | 2 | 30 | 28 |
| Deposit Pokémon that embody the ultimate in beauty! | 7 |  | 10 | 3 |
| Deposit Pokémon that embody the ultimate in coolness! | 1 |  | 10 | 9 |
| Deposit Pokémon that embody the ultimate in cuteness! | 0 |  | 10 | 10 |
| Deposit Pokémon that embody the ultimate in cleverness! | 1 |  | 10 | 9 |
| Deposit Pokémon that embody the ultimate in toughness! | 1 |  | 10 | 9 |
| Deposit 30 Ditto! | 7 | 7 | 30 | 23 |
| Deposit Pokémon that show off the ultimate sheen! | 0 |  | 10 | 10 |

Totale delle mancanze: 425. Un esemplare conta per tutte le sfide che soddisfa, quindi `tools/pkhex-sfide-app` mette i Ditto e gli esemplari con le condizioni al massimo dentro le sfere che hanno ancora un bisogno, e dà a dieci esemplari tutte e cinque le condizioni e la lucentezza a 255, che chiudono insieme le sei sfide di gara. La lucentezza si accumula soltanto con i Pokémelle di terza generazione e i Poffin di quarta (`ContestStatInfo.GetContestStatRestriction` della libreria), quindi quei dieci sono catture di Smeraldo; la sfida della lucentezza è aperta per il proprietario (2026-11-26) e il contatore, non fotografato, si prende a zero. Il lotto prodotto ne contiene 352.

Si chiudono solo su Switch, e restano alla fase Switch: Deposit a Pokémon that has the Mightiest Mark!; Deposit a Roaming Form Gimmighoul that was caught in Pokémon GO!; Deposit Caterpie, Weedle, Metapod, Kakuna, and Pikachu from Pokémon FireRed or Pokémon LeafGreen for Nintendo Switch!; Deposit Chansey and Tauros from Pokémon FireRed or Pokémon LeafGreen for Nintendo Switch!; Deposit Lapras from Pokémon FireRed or Pokémon LeafGreen for Nintendo Switch!; Deposit Porygon from Pokémon FireRed or Pokémon LeafGreen for Nintendo Switch!; Deposit Pokémon in a Feather, Gigaton, Great, Heavy, Jet, Leaden, Poké, Wing or Ultra Ball crafted in the Hisui region! (9 sfide); Deposit Pokémon that have the Jumbo Mark and the Mini Mark!; Fill in your Blueberry, Crown Tundra, Galar, Hisui, Hyperspace, Isle of Armor, Kanto (GBA), Kanto (Let's Go), Kitakami, Lumiose, Mega Evolution, Paldea and Sinnoh (BDSP) Pokédex (13 sfide); Register 10 forms of Furfrou!; Register 2 forms of Dudunsparce!; Register 2 forms of Maushold!; Register 3 varieties of Paldean Tauros!; Register 4 colors of Squawkabilly!; Register 4 different Ruinous Pokémon!; Register Alcremie's forms!; Register all the first partner Pokémon that Trainers can choose in Galar!; Register Applin and its 4 Evolutions!; Register Arceus from Pokémon Legends: Arceus!; Register Darkrai from Pokémon Legends: Z-A!; Register Dialga from Pokémon Brilliant Diamond or Pokémon Shining Pearl!; Register Eevee from Pokémon: Let's Go, Pikachu! or Pokémon: Let's Go, Eevee!; Register Eternal Flower Floette from Pokémon Legends: Z-A!; Register Galarian Articuno, Galarian Zapdos, and Galarian Moltres!; Register Hisuian Decidueye, Hisuian Typhlosion, and Hisuian Samurott!; Register Iron Bundle, Iron Hands, Iron Jugulis, and Iron Thorns!; Register Iron Leaves, Iron Boulder, and Iron Crown!; Register Ogerpon!; Register Okidogi, Munkidori, and Fezandipiti!; Register Palkia from Pokémon Brilliant Diamond or Pokémon Shining Pearl!; Register Pecharunt!; Register Pikachu from Pokémon: Let's Go, Pikachu! or Pokémon: Let's Go, Eevee!; Register Pokémon that have the Twinkling Star Ribbon!; Register Pokémon with all their effort levels maxed!; Register Scream Tail, Brute Bonnet, Flutter Mane, and Sandy Shocks!; Register Staraptor, Bidoof, and Bibarel from Pokémon Brilliant Diamond or Pokémon Shining Pearl!; Register Terapagos!; Register Torterra, Infernape, and Empoleon from Pokémon Brilliant Diamond or Pokémon Shining Pearl!; Register Ursaluna and Bloodmoon Ursaluna!; Register Walking Wake, Gouging Fire, and Raging Bolt!; Register Zacian from Pokémon Sword or Pokémon Shield!; Register Zamazenta from Pokémon Sword or Pokémon Shield!; Register Zygarde from Pokémon Legends: Z-A!.

## Eventi di Serebii con una differenza di trascrizione

Il confronto per specie, allenatore e ID manca 33 eventi; la sonda li ritrova tutti in HOME con una differenza nella trascrizione di Serebii, salvo quelli segnati da verificare.

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
| 129 Magikarp | Daisuki Club | ウッツ－ 01256 | stessa specie e ID, allenatore scritto in un'altra lingua o grafia |
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

95 eventi hanno in HOME solo una parte dei nomi che Serebii elenca. Per la terza generazione le varianti vere sono quelle della libreria, contate sopra: Serebii elenca anche PCNYa, che non è mai esistito, e Sapporo nella sesta distribuzione. Per le generazioni successive i nomi mancanti sono lo stesso allenatore tradotto per un'altra edizione, o scritto diversamente da Serebii, che ADR-045 conta come un allenatore solo:

- 150 Mewtwo, Black & White - 1st Anniversary - European Games: mancano SPR2012 05012.
- 491 Darkrai, ANA & StoreGiveaway: mancano ふめやすみ 12270.
- 647 Keldeo, GAME, GameStop (UK): mancano ETE2012 08272.
- 788 Tapu Fini, 2019 International Challenge May - Entry Gift: mancano ポニ 190524.
- 791 Solgaleo, Cosmic Eclipse Tie In: mancano Sunset 100419.
- 791 Solgaleo, Cosmic Eclipse Tie In: mancano Sunset 100419.
- 792 Lunala, Cosmic Eclipse Tie In: mancano Moonset 100419.
- 792 Lunala, Cosmic Eclipse Tie In: mancano Moonset 100419.

## Che cosa resta fuori da Bank, per scelta o perché non esiste fino al 3DS

Gli eventi di Scarlatto e Violetto, che il proprietario non ha, si recuperano scambiando con la comunità dopo la chiusura di Bank, a cominciare dal Dragapult con il marchio dell'Imbattibile; le sfide della sola Switch qui sopra; le forme e i fiocchi che si prendono solo giocando su Switch (`COPERTURA-LOTTI.md`, `FIOCCHI-PRIMA-DI-BANK.md`). La loro sorte è in `pending.md`, nelle voci da ricordare sempre.

