# L'elenco unico di produzione prima della chiusura di Bank

> Documento generato da `tools/elenco-produzione.py --scrivi`. Non si modifica a mano: si rigenera dopo ogni copia nuova e dopo ogni decisione che aggiunge voci. Mette insieme le voci di ADR-108, ADR-109, ADR-110 e ADR-111, toglie quelle che le copie per HOME coprono già (`tools/pkhex-elenco-copie`, PKHeX 26.10.18) e stima quanti esemplari servono. Lo stato di ciascuna voce e il suo perché stanno nei documenti di dettaglio citati in `DA-PORTARE-PRIMA-DI-BANK.md`; qui sta l'elenco da produrre.

## Il conto

| Categoria | Voci | Coperte dalle copie per HOME | Da produrre |
|---|---|---|---|
| caselle | 6 | 0 | 6 |
| coppie precise | 1 | 0 | 1 |
| Fiocco Maestro | 1 | 1 | 0 |
| Smeraldo | 213 | 213 | 0 |
| asse origine | 479 | 477 | 2 |
| asse sesso e forma | 187 | 186, e 83 voci senza misura possibile | 1 |
| asse scambi | 345 | 282 | 63 |
| asse altri unici | 202 | 176 | 26 |
| asse stelle | 237 | 195, e 237 voci senza misura possibile | 42 |
| asse livelli minimi | 101 | 84 | 17 |
| mosse senza specie | 50 | 0 | 50, da assegnare a un esemplare che le impari |

Voci da produrre: 158, più 50 mosse. Esemplari stimati con la fusione delle voci compatibili: 157. Tetto, una voce un esemplare e una mossa un esemplare: 208. La stima non chiede alla libreria se una fusione sia legale, e può quindi essere ottimista; il tetto non lo è.

I posti di HOME sono 9000. Con le 4818 copie già fatte e il tetto di 2371 statici di ADR-106, che si sovrappone in parte agli altri esemplari unici e alle sfide, la stima porta a 7346 posti e il tetto a 7397. Restano rispettivamente 1654 e 1603 posti per il lavoro su Switch dopo Bank.

Le coperture degli assi sono misurate sul gioco d'origine, sull'incontro di scambio, su un incontro non selvatico, sul livello, sul sesso e sulla forma di Alola, secondo l'asse. Le altre forme dell'asse del sesso e della forma, scritte in inglese nel foglio, e le stelle del Master Dex non hanno un campo corrispondente nelle copie e sono contate tutte da produrre.

## Gli esemplari da produrre, con le voci che ciascuno chiude

| Specie | Forma | Giochi d'origine | Sfera | Cromatico | Voci chiuse |
|---|---|---|---|---|---|
| 1 Bulbasaur |  | YW |  |  | Bulbasaur, Bronze, Yellow: ★1: Cerulean City. Gift. |
| 4 Charmander |  | YW |  |  | Charmander, Bronze, Yellow: ★1: Route 24. Gift. |
| 7 Squirtle |  | YW |  |  | Squirtle, Bronze, Yellow: ★1: Vermilion City. Gift. |
| 20 Raticate |  | UM, US |  |  | Raticate al livello 17.0, USUM |
| 22 Fearow |  | HG, SS |  |  | Fearow «Kenya» di Webster/01001, HGSS |
| 25 Pikachu |  | CXD |  |  | Pikachu «» di コロシアム/31121, Colosseum |
| 26 Raichu |  | CXD |  |  | Raichu «» di コロシアム/31121, Colosseum |
| 26 Raichu |  | HG, SS |  |  | Raichu «Volty» di Surge/33038, HGSS |
| 26 Raichu |  | HG, SS |  |  | Raichu «Volty» di Surge/33038, HGSS |
| 32 Nidoran♂ |  | GN, RD |  |  | Nidoran♂ «チャッピー Chappy» di TRAINERトレーナ /random ID, RG |
| 33 Nidorino |  | GN, RD |  |  | Nidorino «チャッピー Chappy» di TRAINERトレーナ /random ID, RG |
| 34 Nidoking |  | GN, RD |  |  | Nidoking «チャッピー Chappy» di TRAINERトレーナ /random ID, RG |
| 67 Machoke |  | HG, SS |  |  | Machoke «Muscle» di Jose/37460, HGSS |
| 68 Machamp |  | HG, SS |  |  | Machamp «Muscle» di Jose/37460, HGSS |
| 101 Electrode |  | HG, SS |  |  | Electrode «Billy» di Richard/29189, HGSS |
| 112 Rhydon |  | HG, SS |  |  | Rhydon «Hornlette» di Brock/06845, HGSS |
| 122 Mr. Mime |  | GD, SI |  |  | Mr. Mime, GS: Celadon Game Corner |
| 151 Mew |  | qualunque | Cura Ball |  | Mew in Cura Ball, da Rosso Fuoco e Verde Foglia giapponesi |
| 169 Crobat |  | Pt |  |  | Crobat al livello 10.0, Pt + PLA |
| 199 Slowking |  | qualunque |  |  | Slowking «オスカル
Oscar» di TRAINERトレーナ
/random ID, Blue (Jp) + gen 2 & up |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: D Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: E Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: F Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: G Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: H Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: I Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: J Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: K Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: L Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: M Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: N Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: O Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: P Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: Q Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: R Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: S Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: T Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: U Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: V Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: W Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: X Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: Y Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: Z Form. |
| 208 Steelix |  | AS, OR |  |  | Steelix «» di Orlando/Random ID, ORAS |
| 235 Smeargle |  | E |  |  | Smeargle, E: Artisan Cave, Battle Frontier |
| 250 Ho-Oh |  | CXD |  |  | Ho-Oh «» di MATTLE/10048, Colosseum |
| 250 Ho-Oh |  | CXD |  |  | Ho-Oh, Gold, Colosseum: ★23 |
| 251 Celebi |  | CXD |  |  | Celebi «Ageto Celebi» di アゲト/31121, Colosseum |
| 251 Celebi |  | CXD |  |  | Celebi, Gold, JP Colosseum Bonus Disc: ★24 |
| 266 Silcoon |  | AS, OR |  |  | Silcoon al livello 2.0, ORAS |
| 268 Cascoon |  | AS, OR |  |  | Cascoon al livello 2.0, ORAS |
| 271 Lombre |  | AS |  |  | Lombre al livello 12.0, AS |
| 272 Ludicolo |  | AS |  |  | Ludicolo al livello 12.0, AS |
| 274 Nuzleaf |  | OR |  |  | Nuzleaf al livello 7.0, OR |
| 275 Shiftry |  | OR |  |  | Shiftry al livello 7.0, OR |
| 284 Masquerain |  | AS, OR |  |  | Masquerain al livello 21.0, ORAS |
| 294 Loudred |  | AS, OR |  |  | Loudred al livello 16.0, ORAS |
| 308 Medicham |  | AS, OR |  |  | Medicham al livello 34.0, ORAS |
| 311 Plusle |  | CXD |  |  | Plusle «» di DUKING/37149, Colosseum |
| 362 Glalie |  | AS, OR |  |  | Glalie «» di Orlando/Random ID, ORAS |
| 375 Metang |  | HG, SS |  |  | Metang «Iron» di Steven/23478, HGSS |
| 376 Metagross |  | HG, SS |  |  | Metagross «Iron» di Steven/23478, HGSS |
| 385 Jirachi |  | CXD |  |  | Jirachi «Wishmaker Jirachi» di WISHMKR/20043, Colosseum |
| 385 Jirachi |  | qualunque |  |  | Jirachi «» di CHANNEL/40122, Channel |
| 385 Jirachi |  | CXD |  |  | Jirachi, Gold, Colosseum Bonus Disc: ★25 |
| 413 Wormadam |  | qualunque |  |  | casella Wormadam |
| 413 Wormadam | Sabbia | qualunque |  |  | casella Wormadam Sabbia |
| 413 Wormadam | Scarti | qualunque |  |  | casella Wormadam Scarti |
| 416 Vespiquen |  | D, P, Pt |  |  | Vespiquen «» di Hayley/01000, My Pokémon Ranch |
| 423 Gastrodon |  | D, P, Pt |  |  | Gastrodon «» di Hayley/01000, My Pokémon Ranch |
| 462 Magnezone |  | HG, SS |  |  | Magnezone «Maggie» di Lorenzo/50082, HGSS |
| 462 Magnezone |  | BU, C, GN, RD |  |  | Magnezone al livello 5.0, C+RB+SwSh-IoA |
| 464 Rhyperior |  | HG, SS |  |  | Rhyperior «Hornlette» di Brock/06845, HGSS |
| 466 Electivire |  | D, P, Pt |  |  | Electivire «» di PKTOPIA/06257, Battle Revolution |
| 466 Electivire |  | D, P, Pt |  |  | Electivire al livello 15.0, DPPt  |
| 467 Magmortar |  | D, P, Pt |  |  | Magmortar «» di PKTOPIA/06257, Battle Revolution |
| 467 Magmortar |  | D, P, Pt |  |  | Magmortar al livello 14.0, DPPt  |
| 478 Froslass |  | E, R, S |  |  | Froslass, Bronze, RSE: ★50; casella Froslass |
| 487 Giratina |  | HG, SS |  |  | Giratina, HGSS: Sinjoh Ruins. Requires having Arceus in party to access the area. The Dialga/Pal |
| 509 Purrloin |  | B, B2, W, W2 |  |  | Purrloin «» di N/00002, BWB2W2 |
| 510 Liepard |  | B, B2, W, W2 |  |  | Liepard «» di N/00002, BWB2W2 |
| 519 Pidove |  | B, B2, W, W2 |  |  | Pidove «» di N/00002, BWB2W2 |
| 520 Tranquill |  | B, B2, W, W2 |  |  | Tranquill «» di N/00002, BWB2W2 |
| 521 Unfezant |  | B, B2, W, W2 |  |  | Unfezant «» di N/00002, BWB2W2 |
| 525 Boldore |  | B, B2, W, W2 |  |  | Boldore «» di N/00002, BWB2W2 |
| 527 Woobat |  | B, B2, W, W2 |  |  | Woobat «» di N/00002, BWB2W2 |
| 528 Swoobat |  | B, B2, W, W2 |  |  | Swoobat «» di N/00002, BWB2W2 |
| 532 Timburr |  | B, B2, W, W2 |  |  | Timburr «» di N/00002, BWB2W2 |
| 533 Gurdurr |  | B, B2, W, W2 |  |  | Gurdurr «» di N/00002, BWB2W2 |
| 534 Conkeldurr |  | B, B2, W, W2 |  |  | Conkeldurr «» di N/00002, BWB2W2 |
| 535 Tympole |  | B, B2, W, W2 |  |  | Tympole «» di N/00002, BWB2W2 |
| 536 Palpitoad |  | B, B2, W, W2 |  |  | Palpitoad «» di N/00002, BWB2W2 |
| 537 Seismitoad |  | B, B2, W, W2 |  |  | Seismitoad «» di N/00002, BWB2W2 |
| 551 Sandile |  | B, B2, W, W2 |  |  | Sandile «» di N/00002, BWB2W2 |
| 552 Krokorok |  | B, B2, W, W2 |  |  | Krokorok «» di N/00002, BWB2W2 |
| 553 Krookodile |  | B, B2, W, W2 |  |  | Krookodile «» di N/00002, BWB2W2 |
| 554 Darumaka |  | B, B2, W, W2 |  |  | Darumaka «» di N/00002, BWB2W2 |
| 555 Darmanitan |  | B, B2, W, W2 |  |  | Darmanitan «» di N/00002, BWB2W2 |
| 555 Darmanitan |  | B, B2, W, W2 |  |  | Darmanitan «» di N/00002, BWB2W3 |
| 555 Darmanitan |  | AS, OR |  |  | Darmanitan al livello 32.0, ORAS |
| 559 Scraggy |  | B, B2, W, W2 |  |  | Scraggy «» di N/00002, BWB2W2 |
| 560 Scrafty |  | B, B2, W, W2 |  |  | Scrafty «» di N/00002, BWB2W2 |
| 561 Sigilyph |  | B, B2, W, W2 |  |  | Sigilyph «» di N/00002, BWB2W2 |
| 563 Cofagrigus |  | AS, OR |  |  | Cofagrigus al livello 32.0, ORAS |
| 570 Zorua |  | B, B2, W, W2 |  |  | Zorua «N's Zorua» di N/00002, BWB2W2 |
| 571 Zoroark |  | B, B2, W, W2 |  |  | Zoroark «» di N/00002, BWB2W2 |
| 595 Joltik |  | B, B2, W, W2 |  |  | Joltik «» di N/00002, BWB2W2 |
| 596 Galvantula |  | B, B2, W, W2 |  |  | Galvantula «» di N/00002, BWB2W2 |
| 597 Ferroseed |  | B, B2, W, W2 |  |  | Ferroseed «» di N/00002, BWB2W2 |
| 598 Ferrothorn |  | B, B2, W, W2 |  |  | Ferrothorn «» di N/00002, BWB2W2 |
| 599 Klink |  | B, B2, W, W2 |  |  | Klink «» di N/00002, BWB2W2 |
| 600 Klang |  | B, B2, W, W2 |  |  | Klang «» di N/00002, BWB2W2 |
| 601 Klinklang |  | B, B2, W, W2 |  |  | Klinklang «» di N/00002, BWB2W2 |
| 641 Tornadus |  | B2, W2 |  |  | Tornadus, Gold, Dream Radar: ★30 |
| 642 Thundurus |  | B2, W2 |  |  | Thundurus, Gold, Dream Radar: ★31 |
| 645 Landorus |  | B2, W2 |  |  | Landorus, Gold, Dream Radar: ★32 |
| 658 Greninja |  | MN, SN |  |  | Greninja «Ash Greninja» di Ash/131017, SM |
| 678 Meowstic | F | qualunque |  |  | casella Meowstic F |
| 745 Lycanroc | Forma Crepuscolo | qualunque |  |  | casella Lycanroc Forma Crepuscolo |
| 808 da scegliere |  | qualunque |  |  | Meltan con origine Any |
| 809 da scegliere |  | qualunque |  |  | Melmetal Gigantamax Factor, origine Any |
| 809 da scegliere |  | qualunque |  |  | Melmetal con origine Any |
| 866 da scegliere |  | D, P, Pt |  |  | Mr. Rime, Bronze, DPPt: ★54 |
| 899 da scegliere |  | C, GD, SI |  |  | Wyrdeer, Bronze, GSC: ★40 |
| 900 da scegliere |  | BU, GN, RD, YW |  |  | Kleavor, Bronze, RBY: ★27 |
| 901 da scegliere |  | C, GD, SI |  |  | Ursaluna, Bronze, GSC: ★41 |
| 901 da scegliere |  | C |  |  | Ursaluna al livello 25.0, Crystal + PLA |
| 979 da scegliere |  | B, B2, W, W2 |  |  | Annihilape «» di Curtis/54118, BWB2W2 |
| 979 da scegliere |  | BU, GN, RD, YW |  |  | Annihilape, Bronze, RBY: ★28 |
| 981 da scegliere |  | C, GD, SI |  |  | Farigiraf, Bronze, GSC: ★42 |
| 982 da scegliere |  | C, GD, SI |  |  | Dudunsparce, Bronze, GSC: ★43 |
| 982 da scegliere |  | C, GD, SI |  |  | Dudunsparce, Platinum, GSC: ★3: Three-Segment Form. |
| 983 da scegliere |  | X, Y |  |  | Kingambit «Pierce» di Punky/03447, XY |
| 983 da scegliere |  | B, B2, W, W2 |  |  | Kingambit, Bronze, BWB2W2: ★82 |
| da scegliere |  | C |  |  | Wobbuffett, C: Goldenrod game Corner |
| da scegliere |  | qualunque |  |  | Shiny Zigzagoon, GameCube Interactive Multi-Game Demo Disc 14 or 16: Demo discs were released to select stores across U.S. and Japan, so players coul |
| da scegliere |  | HG, SS |  |  | Kanto starters, HGSS: Professor Oak, in Pallet Town, after defeating Red. |
| da scegliere |  | HG, SS |  |  | Hoenn starters, HGSS: Steven, in Silph Co., after defeating Red. |
| da scegliere |  | HG, SS |  |  | Shiny Gyarados, HGSS: Interactable, Lake of Rage. (Gen 2 was covered by Mdex) |
| da scegliere |  | B2 |  |  | Jellicent ♂, B2: Interactable, Undella Bay, Black 2, Mondays. |
| da scegliere |  | W2 |  |  | Jellicent ♀, W2: Interactable, Undella Bay, White 2, Thursdays. |
| da scegliere |  | X, Y |  |  | Kanto starters, XY: From Professor Sycamore, Lumiose City. |
| da scegliere |  | X, Y |  |  | Any Pokémon, XY: In Anistar City, an old man requests that you give him a Pokémon for him to take |
| da scegliere |  | AS, OR |  |  | Johto starters, ORAS: Prof Birch after Hall of Fame, in Route 101. |
| da scegliere |  | AS, OR |  |  | Sinnoh starters, ORAS: Prof Birch after 2nd Hall of Fame, in Route 101. . |
| da scegliere |  | AS, OR |  |  | Unova starters, ORAS: Prof Birch after Delta Episode, in Route 101. . |
| da scegliere |  | MN, SN |  |  | Type:Null, SM: Gladion, Aether Paradise, after beating the Elite 4. |
| da scegliere |  | MN, SN |  |  | Alolan Exeggutor, SM: Story battle when visiting Executtor Island. |
| da scegliere |  | UM, US |  |  | Type: Null, USUM: Wicke, Ancient Poni Path, after beating the Elite 4. |
| da scegliere |  | UM, US |  |  | Zygarde
10% Forme, USUM: Dexio, Route 16, after catching 50% Forme Zygarde in Resolution Cave. |
| da scegliere |  | US |  |  | Gumshoos
Totem-sized, US: Samson Oak, Heahea Beach for all Totems. Collect at least 20 Totem Stickers US. |
| da scegliere |  | UM |  |  | Raticate
Totem-sized, UM: Collect at least 20 Totem Stickers UM. |
| da scegliere |  | US |  |  | Lurantis
Totem-sized, US: Collect at least 50 Totem Stickers US. |
| da scegliere |  | UM |  |  | Salazzle
Totem-sized, UM: Collect at least 50 Totem Stickers UM. |
| da scegliere |  | US |  |  | Vikavolt
Totem-sized, US: Collect at least 70 Totem Stickers US. |
| da scegliere |  | UM, US |  |  | Mimikyu
Totem-sized, USUM: Collect at least 80 Totem Stickers. |
| da scegliere |  | UM |  |  | Kommo-o
Totem-sized, UM: Collect all 100 Totem Stickers UM. |

## Le mosse da assegnare

Tectonic Rage, Struggle, Light of Ruin, Clangorous Soulblaze, Zippy Zap, Splishy Splash, Floaty Fall, Pika Papow, Bouncy Bubble, Buzzy Buzz, Sizzly Slide, Glitzy Glow, Baddy Bad, Sappy Seed, Freezy Frost, Sparkly Swirl, Veevee Volley, Double Iron Bash, Breakneck Blitz, Continental Crush, Subzero Slammer, Corkscrew Crash, Devastating Drake, Never-Ending Nightmare, Acid Downpour, Black Hole Eclipse, Shattered Psyche, Twinkle Tackle, Pulverizing Pancake, Bloom Doom, Extreme Evoboost, Sinister Arrow Raid, Malicious Moonsault, Oceanic Operetta, Catastropika, 10,000,000 Volt Thunderbolt, Stoked Sparksurfer, Splintered Stormshards, Inferno Overdrive, Genesis Supernova, Guardian of Alola, Soul-Stealing 7-Star Strike, Searing Sunraze Smash, Menacing Moonraze Maelstrom, Light That Burns the Sky, Hydro Vortex, Gigavolt Havoc, Supersonic Skystrike, All-Out Pummeling, Savage Spin-Out.
