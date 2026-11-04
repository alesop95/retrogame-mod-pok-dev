# L'elenco unico di produzione prima della chiusura di Bank

> Documento generato da `tools/elenco-produzione.py --scrivi`. Non si modifica a mano: si rigenera dopo ogni copia nuova e dopo ogni decisione che aggiunge voci. Mette insieme le voci di ADR-108, ADR-109, ADR-110 e ADR-111, toglie quelle che le copie per HOME coprono già (`tools/pkhex-elenco-copie`, PKHeX 26.10.18) e stima quanti esemplari servono. Lo stato di ciascuna voce e il suo perché stanno nei documenti di dettaglio citati in `DA-PORTARE-PRIMA-DI-BANK.md`; qui sta l'elenco da produrre.

## Il conto

| Categoria | Voci | Coperte dalle copie per HOME | Da produrre |
|---|---|---|---|
| coppie precise | 1 | 0 | 1 |
| Fiocco Maestro | 1 | 1 | 0 |
| Smeraldo | 213 | 213 | 0 |
| asse origine | 479 | 477 | 2 |
| asse sesso e forma | 187 | 186, e 83 voci senza misura possibile | 1 |
| asse scambi | 345 | 333 | 12 |
| asse altri unici | 202 | 190 | 12 |
| asse stelle | 237 | 219, e 237 voci senza misura possibile | 18 |
| asse livelli minimi | 101 | 84 | 17 |
| mosse senza specie | 50 | 0 | 50, da assegnare a un esemplare che le impari |

Voci da produrre: 63, più 50 mosse. Esemplari stimati con la fusione delle voci compatibili: 63. Tetto, una voce un esemplare e una mossa un esemplare: 113. La stima non chiede alla libreria se una fusione sia legale, e può quindi essere ottimista; il tetto non lo è.

I posti di HOME sono 9000. Con le 4902 copie già fatte e il tetto di 2371 statici di ADR-106, che si sovrappone in parte agli altri esemplari unici e alle sfide, la stima porta a 7336 posti e il tetto a 7386. Restano rispettivamente 1664 e 1614 posti per il lavoro su Switch dopo Bank.

Le coperture degli assi sono misurate sul gioco d'origine, sull'incontro di scambio, su un incontro non selvatico, sul livello, sul sesso e sulla forma di Alola, secondo l'asse. Le altre forme dell'asse del sesso e della forma, scritte in inglese nel foglio, e le stelle del Master Dex non hanno un campo corrispondente nelle copie e sono contate tutte da produrre.

## Gli esemplari da produrre, con le voci che ciascuno chiude

| Specie | Forma | Giochi d'origine | Sfera | Cromatico | Voci chiuse |
|---|---|---|---|---|---|
| 1 Bulbasaur |  | YW |  |  | Bulbasaur, Bronze, Yellow: ★1: Cerulean City. Gift. |
| 4 Charmander |  | YW |  |  | Charmander, Bronze, Yellow: ★1: Route 24. Gift. |
| 7 Squirtle |  | YW |  |  | Squirtle, Bronze, Yellow: ★1: Vermilion City. Gift. |
| 20 Raticate |  | UM, US |  |  | Raticate al livello 17.0, USUM |
| 25 Pikachu |  | CXD |  |  | Pikachu «» di コロシアム/31121, Colosseum |
| 26 Raichu |  | CXD |  |  | Raichu «» di コロシアム/31121, Colosseum |
| 32 Nidoran♂ |  | GN, RD |  |  | Nidoran♂ «チャッピー Chappy» di TRAINERトレーナ /random ID, RG |
| 33 Nidorino |  | GN, RD |  |  | Nidorino «チャッピー Chappy» di TRAINERトレーナ /random ID, RG |
| 34 Nidoking |  | GN, RD |  |  | Nidoking «チャッピー Chappy» di TRAINERトレーナ /random ID, RG |
| 151 Mew |  | qualunque | Cura Ball |  | Mew in Cura Ball, da Rosso Fuoco e Verde Foglia giapponesi |
| 169 Crobat |  | Pt |  |  | Crobat al livello 10.0, Pt + PLA |
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
| 385 Jirachi |  | CXD |  |  | Jirachi «Wishmaker Jirachi» di WISHMKR/20043, Colosseum |
| 385 Jirachi |  | CXD |  |  | Jirachi, Gold, Colosseum Bonus Disc: ★25 |
| 423 Gastrodon |  | D, P, Pt |  |  | Gastrodon «» di Hayley/01000, My Pokémon Ranch |
| 462 Magnezone |  | BU, C, GN, RD |  |  | Magnezone al livello 5.0, C+RB+SwSh-IoA |
| 466 Electivire |  | D, P, Pt |  |  | Electivire al livello 15.0, DPPt  |
| 467 Magmortar |  | D, P, Pt |  |  | Magmortar al livello 14.0, DPPt  |
| 487 Giratina |  | HG, SS |  |  | Giratina, HGSS: Sinjoh Ruins. Requires having Arceus in party to access the area. The Dialga/Pal |
| 555 Darmanitan |  | AS, OR |  |  | Darmanitan al livello 32.0, ORAS |
| 563 Cofagrigus |  | AS, OR |  |  | Cofagrigus al livello 32.0, ORAS |
| 641 Tornadus |  | B2, W2 |  |  | Tornadus, Gold, Dream Radar: ★30 |
| 642 Thundurus |  | B2, W2 |  |  | Thundurus, Gold, Dream Radar: ★31 |
| 645 Landorus |  | B2, W2 |  |  | Landorus, Gold, Dream Radar: ★32 |
| 658 Greninja |  | MN, SN |  |  | Greninja «Ash Greninja» di Ash/131017, SM |
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
| da scegliere |  | HG, SS |  |  | Kanto starters, HGSS: Professor Oak, in Pallet Town, after defeating Red. |
| da scegliere |  | HG, SS |  |  | Hoenn starters, HGSS: Steven, in Silph Co., after defeating Red. |
| da scegliere |  | X, Y |  |  | Kanto starters, XY: From Professor Sycamore, Lumiose City. |
| da scegliere |  | X, Y |  |  | Any Pokémon, XY: In Anistar City, an old man requests that you give him a Pokémon for him to take |
| da scegliere |  | AS, OR |  |  | Johto starters, ORAS: Prof Birch after Hall of Fame, in Route 101. |
| da scegliere |  | AS, OR |  |  | Sinnoh starters, ORAS: Prof Birch after 2nd Hall of Fame, in Route 101. . |
| da scegliere |  | AS, OR |  |  | Unova starters, ORAS: Prof Birch after Delta Episode, in Route 101. . |
| da scegliere |  | MN, SN |  |  | Type:Null, SM: Gladion, Aether Paradise, after beating the Elite 4. |
| da scegliere |  | UM, US |  |  | Type: Null, USUM: Wicke, Ancient Poni Path, after beating the Elite 4. |

## Le mosse da assegnare

Tectonic Rage, Struggle, Light of Ruin, Clangorous Soulblaze, Zippy Zap, Splishy Splash, Floaty Fall, Pika Papow, Bouncy Bubble, Buzzy Buzz, Sizzly Slide, Glitzy Glow, Baddy Bad, Sappy Seed, Freezy Frost, Sparkly Swirl, Veevee Volley, Double Iron Bash, Breakneck Blitz, Continental Crush, Subzero Slammer, Corkscrew Crash, Devastating Drake, Never-Ending Nightmare, Acid Downpour, Black Hole Eclipse, Shattered Psyche, Twinkle Tackle, Pulverizing Pancake, Bloom Doom, Extreme Evoboost, Sinister Arrow Raid, Malicious Moonsault, Oceanic Operetta, Catastropika, 10,000,000 Volt Thunderbolt, Stoked Sparksurfer, Splintered Stormshards, Inferno Overdrive, Genesis Supernova, Guardian of Alola, Soul-Stealing 7-Star Strike, Searing Sunraze Smash, Menacing Moonraze Maelstrom, Light That Burns the Sky, Hydro Vortex, Gigavolt Havoc, Supersonic Skystrike, All-Out Pummeling, Savage Spin-Out.
