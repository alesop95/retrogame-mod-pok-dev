# L'elenco unico di produzione prima della chiusura di Bank

> Documento generato da `tools/elenco-produzione.py --scrivi`. Non si modifica a mano: si rigenera dopo ogni copia nuova e dopo ogni decisione che aggiunge voci. Mette insieme le voci di ADR-108, ADR-109, ADR-110 e ADR-111, toglie quelle che le copie per HOME coprono già (`tools/pkhex-elenco-copie`, PKHeX 26.10.18) e stima quanti esemplari servono. Lo stato di ciascuna voce e il suo perché stanno nei documenti di dettaglio citati in `DA-PORTARE-PRIMA-DI-BANK.md`; qui sta l'elenco da produrre.

## Il conto

| Categoria | Voci | Coperte dalle copie per HOME | Da produrre |
|---|---|---|---|
| caselle | 374 | 0 | 374 |
| sfide | 39 | 0 | 39 |
| cromatici | 8 | 0 | 8 |
| abilità | 2 | 0 | 2 |
| sfere | 81 | 0 | 81 |
| coppie precise | 11 | 0 | 11 |
| Fiocco Maestro | 1 | 0 | 1 |
| Smeraldo | 213 | 0 | 213 |
| asse origine | 479 | 212 | 267 |
| asse sesso e forma | 187 | 26, e 83 voci senza misura possibile | 161 |
| asse scambi | 345 | 93 | 252 |
| asse altri unici | 202 | 82 | 120 |
| asse stelle | 237 | 0, e 237 voci senza misura possibile | 237 |
| asse livelli minimi | 101 | 0 | 101 |
| mosse senza specie | 184 | 0 | 184, da assegnare a un esemplare che le impari |

Voci da produrre: 1867, più 184 mosse. Esemplari stimati con la fusione delle voci compatibili: 1464. Tetto, una voce un esemplare e una mossa un esemplare: 2051. La stima non chiede alla libreria se una fusione sia legale, e può quindi essere ottimista; il tetto non lo è.

I posti di HOME sono 9000. Con le 3407 copie già fatte e il tetto di 2371 statici di ADR-106, che si sovrappone in parte agli altri esemplari unici e alle sfide, la stima porta a 7242 posti e il tetto a 7829. Restano rispettivamente 1758 e 1171 posti per il lavoro su Switch dopo Bank.

Le coperture degli assi sono misurate sul gioco d'origine, sull'incontro di scambio, su un incontro non selvatico, sul livello, sul sesso e sulla forma di Alola, secondo l'asse. Le altre forme dell'asse del sesso e della forma, scritte in inglese nel foglio, e le stelle del Master Dex non hanno un campo corrispondente nelle copie e sono contate tutte da produrre.

## Gli esemplari da produrre, con le voci che ciascuno chiude

| Specie | Forma | Giochi d'origine | Sfera | Cromatico | Voci chiuse |
|---|---|---|---|---|---|
| 1 Bulbasaur |  | YW |  |  | Bulbasaur, Bronze, Yellow: ★1: Cerulean City. Gift. |
| 3 Venusaur |  | E |  |  | Venusaur della cartuccia, box 13 posto 18 |
| 3 Venusaur |  | BU, GN, RD, YW |  |  | Venusaur, per «Register Venusaur from the good ol' Kanto Region!» |
| 4 Charmander |  | YW |  |  | Charmander, Bronze, Yellow: ★1: Route 24. Gift. |
| 6 Charizard |  | BU, GN, RD, YW |  |  | Charizard, per «Register Charizard from the good ol' Kanto Region!» |
| 7 Squirtle |  | YW |  |  | Squirtle, Bronze, Yellow: ★1: Vermilion City. Gift. |
| 9 Blastoise |  | BU, GN, RD, YW |  |  | Blastoise, per «Register Blastoise from the good ol' Kanto Region!» |
| 12 Butterfree |  | E |  |  | Butterfree della cartuccia, box 9 posto 20 |
| 16 Pidgey |  | E |  |  | Pidgey della cartuccia, box 9 posto 1 |
| 19 Rattata |  | E |  |  | Rattata della cartuccia, box 8 posto 17 |
| 19 Rattata |  | E |  |  | Rattata della cartuccia, box 9 posto 23 |
| 19 Rattata |  | qualunque | Safari Ball |  | Rattata in Safari Ball |
| 19 Rattata |  | qualunque | Dream Ball |  | Rattata in Dream Ball |
| 19 Rattata |  | qualunque | UC Ball |  | Rattata in UC Ball |
| 19 Rattata | Alola | MN, SN, UM, US | Safari Ball |  | casella Rattata Alola; Rattata Alola in Safari Ball; Rattata Alolan Form, origine SMUSUM |
| 19 Rattata | Alola | qualunque | Rete Ball |  | Rattata Alola in Rete Ball |
| 19 Rattata | Alola | qualunque | Sub Ball |  | Rattata Alola in Sub Ball |
| 19 Rattata | Alola | qualunque | Minor Ball |  | Rattata Alola in Minor Ball |
| 19 Rattata | Alola | qualunque | Bis Ball |  | Rattata Alola in Bis Ball |
| 19 Rattata | Alola | qualunque | Timer Ball |  | Rattata Alola in Timer Ball |
| 19 Rattata | Alola | qualunque | Chic Ball |  | Rattata Alola in Chic Ball |
| 19 Rattata | Alola | qualunque | Scuro Ball |  | Rattata Alola in Scuro Ball |
| 19 Rattata | Alola | qualunque | Cura Ball |  | Rattata Alola in Cura Ball |
| 19 Rattata | Alola | qualunque | Velox Ball |  | Rattata Alola in Velox Ball |
| 19 Rattata | Alola | qualunque | Rapid Ball |  | Rattata Alola in Rapid Ball |
| 19 Rattata | Alola | qualunque | Level Ball |  | Rattata Alola in Level Ball |
| 19 Rattata | Alola | qualunque | Esca Ball |  | Rattata Alola in Esca Ball |
| 19 Rattata | Alola | qualunque | Peso Ball |  | Rattata Alola in Peso Ball |
| 19 Rattata | Alola | qualunque | Love Ball |  | Rattata Alola in Love Ball |
| 19 Rattata | Alola | qualunque | Friend Ball |  | Rattata Alola in Friend Ball |
| 19 Rattata | Alola | qualunque | Luna Ball |  | Rattata Alola in Luna Ball |
| 19 Rattata | Alola | qualunque | Dream Ball |  | Rattata Alola in Dream Ball |
| 19 Rattata | Alola | qualunque | UC Ball |  | Rattata Alola in UC Ball |
| 20 Raticate |  | UM, US |  |  | Raticate, Silver, USUM: ★13: Totem Variant. |
| 20 Raticate |  | C |  |  | Raticate al livello 6.0, Crystal |
| 20 Raticate |  | UM, US |  |  | Raticate al livello 17.0, USUM |
| 20 Raticate | Alola | MN, SN, UM, US | Rete Ball |  | casella Raticate Alola; Raticate Alola in Rete Ball; Raticate Alolan Form, origine SMUSUM |
| 20 Raticate | Alola | qualunque | Sub Ball |  | Raticate Alola in Sub Ball |
| 20 Raticate | Alola | qualunque | Minor Ball |  | Raticate Alola in Minor Ball |
| 20 Raticate | Alola | qualunque | Bis Ball |  | Raticate Alola in Bis Ball |
| 20 Raticate | Alola | qualunque | Timer Ball |  | Raticate Alola in Timer Ball |
| 20 Raticate | Alola | qualunque | Chic Ball |  | Raticate Alola in Chic Ball |
| 20 Raticate | Alola | qualunque | Scuro Ball |  | Raticate Alola in Scuro Ball |
| 20 Raticate | Alola | qualunque | Cura Ball |  | Raticate Alola in Cura Ball |
| 20 Raticate | Alola | qualunque | Velox Ball |  | Raticate Alola in Velox Ball |
| 21 Spearow |  | E |  |  | Spearow della cartuccia, box 4 posto 6 |
| 21 Spearow |  | E |  |  | Spearow della cartuccia, box 9 posto 18 |
| 21 Spearow |  | C, GD, SI |  |  | Spearow «KENYA» di RANDY/Your ID, GSC |
| 21 Spearow |  | qualunque | Safari Ball |  | Spearow in Safari Ball |
| 21 Spearow |  | qualunque | Dream Ball |  | Spearow in Dream Ball |
| 21 Spearow |  | qualunque | UC Ball |  | Spearow in UC Ball |
| 22 Fearow |  | E |  |  | Fearow della cartuccia, box 4 posto 5; casella Fearow |
| 22 Fearow |  | C, GD, SI |  |  | Fearow «KENYA» di RANDY/Your ID, GSC |
| 22 Fearow |  | HG, SS |  |  | Fearow «Kenya» di Webster/01001, HGSS |
| 23 Ekans |  | E |  |  | Ekans della cartuccia, box 8 posto 24; casella Ekans |
| 23 Ekans |  | GD, SI |  |  | Ekans, GS: Goldenrod game Corner |
| 23 Ekans |  | HG |  |  | Ekans, HG: Goldenrod Game Corner |
| 24 Arbok |  | SS |  |  | Arbok al livello 10.0, SC SS |
| 25 Pikachu |  | E |  |  | Pikachu della cartuccia, box 7 posto 1 |
| 25 Pikachu |  | E |  |  | Pikachu della cartuccia, box 9 posto 29 |
| 25 Pikachu |  | qualunque |  |  | Pikachu Partner Cap, origine Any |
| 25 Pikachu |  | CXD |  |  | Pikachu «» di コロシアム/31121, Colosseum |
| 25 Pikachu |  | BU |  |  | Pikachu, Blue (Jp): Game Corner Prize; Pikachu, per «Register Pikachu from the good ol' Kanto Region!» |
| 25 Pikachu |  | C |  |  | Pikachu, C: Celadon Game Corner |
| 25 Pikachu |  | YW |  |  | Pikachu, Bronze, Yellow: ★1: Pallet Town. Gift. |
| 25 Pikachu |  | HG, SS |  |  | Pikachu, Bronze, HGSS: ★55: Saffron City. Trade. |
| 25 Pikachu |  | D, P, Pt |  |  | Pikachu, Gold, Battle Revolution: ★28 |
| 26 Raichu |  | E |  |  | Raichu della cartuccia, box 9 posto 30; casella Raichu |
| 26 Raichu |  | CXD |  |  | Raichu «» di コロシアム/31121, Colosseum |
| 26 Raichu |  | HG, SS |  |  | Raichu «Volty» di Surge/33038, HGSS |
| 26 Raichu |  | HG, SS |  |  | Raichu «Volty» di Surge/33038, HGSS |
| 26 Raichu |  | D, P, Pt |  |  | Raichu «» di PKTOPIA/44870, Battle Revolution |
| 26 Raichu |  | D, P, Pt |  |  | Raichu «» di PKTOPIA/44870, Battle Revolution |
| 26 Raichu |  | D, P, Pt |  |  | Raichu «» di Hayley/01000, My Pokémon Ranch |
| 26 Raichu |  | BU, GN, RD, YW |  |  | Raichu, Bronze, RBY: ★2: Alolan Form. |
| 26 Raichu |  | UM, US |  |  | Raichu, Silver, USUM: ★14: Heahea City. Gift. Kantonian Form. |
| 26 Raichu | Alola | MN, SN, UM, US |  |  | casella Raichu Alola; Raichu Alolan Form, origine SMUSUM |
| 27 Sandshrew |  | GD, SI |  |  | Sandshrew, GS: Goldenrod game Corner |
| 27 Sandshrew |  | SS |  |  | Sandshrew, SS: Goldenrod Game Corner |
| 28 Sandslash |  | E |  |  | Sandslash della cartuccia, box 8 posto 25 |
| 28 Sandslash |  | GD, HG |  |  | Sandslash al livello 10.0, G HG |
| 28 Sandslash | Alola | MN, SN, UM, US |  |  | casella Sandslash Alola; Sandslash Alolan Form, origine SMUSUM |
| 29 Nidoran♀ |  | BU, GN, RD |  |  | Nidoran♀ «SPOT» di TRAINER/random ID, RB |
| 30 Nidorina |  | BU, GN, RD |  |  | Nidorina «SPOT» di TRAINER/random ID, RB |
| 30 Nidorina |  | BU, GN, RD |  |  | Nidorina «TERRY» di TRAINER/random ID, RB |
| 30 Nidorina |  | BU, GN, RD |  |  | Nidorina, RB: Game Corner Prize |
| 30 Nidorina |  | HG, SS |  |  | Nidorina al livello 15.0, HGSS |
| 31 Nidoqueen |  | BU, GN, RD |  |  | Nidoqueen «SPOT» di TRAINER/random ID, RB |
| 31 Nidoqueen |  | BU, GN, RD |  |  | Nidoqueen «TERRY» di TRAINER/random ID, RB |
| 31 Nidoqueen |  | FR |  |  | Nidoqueen «MS. NIDO» di SAIGE/63184, FR |
| 31 Nidoqueen |  | FR |  |  | Nidoqueen «NINA» di TURNER/13637, FR |
| 31 Nidoqueen |  | HG, SS |  |  | Nidoqueen al livello 15.0, HGSS |
| 32 Nidoran♂ |  | GN, RD |  |  | Nidoran♂ «チャッピー Chappy» di TRAINERトレーナ /random ID, RG |
| 33 Nidorino |  | GN, RD |  |  | Nidorino «チャッピー Chappy» di TRAINERトレーナ /random ID, RG |
| 33 Nidorino |  | BU, GN, RD |  |  | Nidorino, RB: Game Corner Prize |
| 33 Nidorino |  | HG, SS |  |  | Nidorino al livello 15.0, HGSS |
| 34 Nidoking |  | GN, RD |  |  | Nidoking «チャッピー Chappy» di TRAINERトレーナ /random ID, RG |
| 34 Nidoking |  | LG |  |  | Nidoking «MR. NIDO» di SAIGE/63184, LG |
| 34 Nidoking |  | LG |  |  | Nidoking «NINO» di TURNER/13637, LG |
| 34 Nidoking |  | HG, SS |  |  | Nidoking al livello 15.0, HGSS |
| 35 Clefairy |  | BU, GN, RD |  |  | Clefairy, RB: Game Corner Prize |
| 35 Clefairy |  | qualunque |  |  | Clefairy, Bronze, Pokéwalker: ★59: Night Sky's Edge. |
| 36 Clefable |  | BU |  |  | Clefable, Blue (Jp): Game Corner Prize |
| 37 Vulpix |  | YW |  |  | Vulpix, Yellow: Game Corner Prize |
| 38 Ninetales |  | E |  |  | Ninetales della cartuccia, box 8 posto 21 |
| 38 Ninetales |  | D, P, Pt |  |  | Ninetales «» di Hayley/01000, My Pokémon Ranch |
| 38 Ninetales | Alola | MN, SN, UM, US |  |  | casella Ninetales Alola; Ninetales Alolan Form, origine SMUSUM |
| 39 Jigglypuff |  | E |  |  | Jigglypuff della cartuccia, box 7 posto 6 |
| 39 Jigglypuff |  | E |  |  | Jigglypuff della cartuccia, box 9 posto 13 |
| 39 Jigglypuff |  | E |  |  | Jigglypuff della cartuccia, box 9 posto 15 |
| 39 Jigglypuff |  | qualunque |  |  | Jigglypuff, Bronze, Pokéwalker: ★60: Night Sky's Edge. |
| 40 Wigglytuff |  | E |  |  | Wigglytuff della cartuccia, box 9 posto 5; casella Wigglytuff |
| 40 Wigglytuff |  | YW |  |  | Wigglytuff, Yellow: Game Corner Prize |
| 42 Golbat |  | Pt |  |  | Golbat al livello 10.0, Pt |
| 44 Gloom |  | GD |  |  | Gloom al livello 14.0, Gold |
| 45 Vileplume |  | E |  |  | Vileplume della cartuccia, box 7 posto 28; casella Vileplume |
| 45 Vileplume |  | C, HG, SS |  |  | Vileplume al livello 14.0, C HGSS |
| 46 Paras |  | qualunque | Safari Ball |  | Paras in Safari Ball |
| 46 Paras |  | qualunque | Gara Ball |  | Paras in Gara Ball |
| 46 Paras |  | qualunque | Dream Ball |  | Paras in Dream Ball |
| 46 Paras |  | qualunque | UC Ball |  | Paras in UC Ball |
| 47 Parasect |  | E |  |  | Parasect della cartuccia, box 8 posto 6; casella Parasect |
| 47 Parasect |  | YW |  |  | Parasect «SPIKE» di TRAINER/random ID, Yellow |
| 47 Parasect |  | C, GD, SI, YW |  |  | Parasect al livello 5.0, GSC + Y |
| 49 Venomoth |  | HG, SS |  |  | Venomoth al livello 8.0, HGSS |
| 50 Diglett |  | E |  |  | Diglett della cartuccia, box 9 posto 24; casella Diglett |
| 51 Dugtrio |  | YW |  |  | Dugtrio «GURIO» di TRAINER/random ID, Yellow |
| 51 Dugtrio |  | C, GD, SI, YW |  |  | Dugtrio al livello 5.0, GSC + Y |
| 51 Dugtrio | Alola | MN, SN, UM, US |  |  | casella Dugtrio Alola; Dugtrio Alolan Form, origine SMUSUM |
| 52 Meowth |  | E |  |  | Meowth della cartuccia, box 4 posto 12 |
| 52 Meowth |  | B, B2, W, W2 |  |  | Meowth «» di Yancy/10303, BWB2W2 |
| 52 Meowth | Alola | MN, SN, UM, US |  |  | casella Meowth Alola; Meowth Alolan Form, origine SMUSUM |
| 53 Persian |  | E |  |  | Persian della cartuccia, box 4 posto 2; casella Persian |
| 53 Persian |  | E |  |  | Persian «MEOWOW» di ISIS/25945, E |
| 53 Persian |  | B, B2, W, W2 |  |  | Persian «» di Yancy/10303, BWB2W2 |
| 53 Persian | Alola | MN, SN, UM, US |  |  | casella Persian Alola; Persian Alolan Form, origine SMUSUM |
| 55 Golduck |  | E |  |  | Golduck della cartuccia, box 8 posto 26 |
| 55 Golduck |  | C, GD, SI |  |  | Golduck al livello 10.0, GSC |
| 56 Mankey |  | B, B2, W, W2 |  |  | Mankey «» di Curtis/54118, BWB2W2 |
| 57 Primeape |  | B, B2, W, W2 |  |  | Primeape «» di Curtis/54118, BWB2W2 |
| 57 Primeape |  | GD, HG |  |  | Primeape al livello 15.0, G HG |
| 59 Arcanine |  | E |  |  | Arcanine della cartuccia, box 13 posto 4 |
| 60 Poliwag |  | E |  |  | Poliwag della cartuccia, box 9 posto 16 |
| 60 Poliwag |  | BU |  |  | Poliwag «ロモたん
Romo-tan» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 61 Poliwhirl |  | BU |  |  | Poliwhirl «ロモたん
Romo-tan» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 62 Poliwrath |  | BU |  |  | Poliwrath «ロモたん
Romo-tan» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 62 Poliwrath |  | MN, SN |  |  | Poliwrath «Whirly» di Laule'a/590916, SM |
| 63 Abra |  | BU, GN, RD, YW |  |  | Abra, RBY: Game Corner Prize |
| 63 Abra |  | C, GD, SI |  |  | Abra, GSC: Goldenrod game Corner |
| 64 Kadabra |  | MN, SN |  |  | Kadabra al livello 11.0, SM |
| 65 Alakazam |  | E |  |  | Alakazam della cartuccia, box 1 posto 29 |
| 65 Alakazam |  | E |  |  | Alakazam della cartuccia, box 13 posto 8 |
| 65 Alakazam |  | B, B2, W, W2 |  |  | Alakazam «Beardy» di Diana/17074, BWB2W2 |
| 65 Alakazam |  | MN, SN |  |  | Alakazam al livello 11.0, SM |
| 66 Machop |  | C, GD, SI |  |  | Machop «MUSCLE» di MIKE/37460, GSC |
| 67 Machoke |  | C, GD, SI |  |  | Machoke «MUSCLE» di MIKE/37460, GSC |
| 67 Machoke |  | HG, SS |  |  | Machoke «Muscle» di Jose/37460, HGSS |
| 67 Machoke |  | MN, SN |  |  | Machoke «Macho» di Hila/000410, SM |
| 67 Machoke |  | GD, HG, SI, SS |  |  | Machoke al livello 14.0, GS HGSS |
| 68 Machamp |  | E |  |  | Machamp della cartuccia, box 1 posto 28 |
| 68 Machamp |  | E |  |  | Machamp della cartuccia, box 8 posto 8 |
| 68 Machamp |  | E |  |  | Machamp della cartuccia, box 14 posto 9 |
| 68 Machamp |  | YW |  |  | Machamp «RICKY» di TRAINER/random ID, Yellow |
| 68 Machamp |  | C, GD, SI |  |  | Machamp «MUSCLE» di MIKE/37460, GSC |
| 68 Machamp |  | HG, SS |  |  | Machamp «Muscle» di Jose/37460, HGSS |
| 68 Machamp |  | MN, SN |  |  | Machamp «Macho» di Hila/000410, SM |
| 68 Machamp |  | C, GD, SI, YW |  |  | Machamp al livello 5.0, GSC + Y |
| 69 Bellsprout |  | E |  |  | Bellsprout della cartuccia, box 7 posto 2 |
| 70 Weepinbell |  | HG, SS |  |  | Weepinbell al livello 10.0, HGSS |
| 71 Victreebel |  | E |  |  | Victreebel della cartuccia, box 11 posto 12; casella Victreebel |
| 71 Victreebel |  | HG, SS |  |  | Victreebel al livello 10.0, HGSS |
| 72 Tentacool |  | HG, SS |  |  | Tentacool, Silver, HGSS: ★6: Cianwood City. Gift. |
| 73 Tentacruel |  | E |  |  | Tentacruel della cartuccia, box 7 posto 21; casella Tentacruel |
| 73 Tentacruel |  | E |  |  | Tentacruel della cartuccia, box 12 posto 2 |
| 74 Geodude | Alola | MN, SN, UM, US |  |  | casella Geodude Alola; Geodude di Alola con Galvanize; Geodude Alolan Form, origine SMUSUM |
| 75 Graveler |  | E |  |  | Graveler della cartuccia, box 7 posto 9 |
| 75 Graveler |  | HG, SS |  |  | Graveler al livello 16.0, HGSS |
| 75 Graveler | Alola | MN, SN, UM, US |  |  | casella Graveler Alola; Graveler Alolan Form, origine SMUSUM |
| 76 Golem |  | E |  |  | Golem della cartuccia, box 11 posto 24; casella Golem |
| 76 Golem |  | E |  |  | Golem della cartuccia, box 12 posto 4 |
| 76 Golem |  | BU |  |  | Golem «さぶろう
Saburō» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 76 Golem |  | HG, SS |  |  | Golem al livello 16.0, HGSS |
| 78 Rapidash |  | GD, SI |  |  | Rapidash «RUNNY» di CHRIS/15616, GS |
| 78 Rapidash |  | D, P, Pt |  |  | Rapidash «» di Hayley/01000, My Pokémon Ranch |
| 78 Rapidash |  | GD, SI, YW |  |  | Rapidash al livello 14.0, GS + Y |
| 79 Slowpoke |  | BU |  |  | Slowpoke «オスカル
Oscar» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 80 Slowbro |  | BU |  |  | Slowbro «オスカル
Oscar» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 80 Slowbro |  | YW |  |  | Slowbro al livello 15.0, Yellow |
| 81 Magnemite |  | E |  |  | Magnemite della cartuccia, box 11 posto 3 |
| 82 Magneton |  | C |  |  | Magneton «MAGGIE» di FOREST/50082, C |
| 82 Magneton |  | C, YW |  |  | Magneton al livello 5.0, C + Y |
| 83 Farfetch’d |  | BU, GN, RD |  |  | Farfetch’d «DUX» di TRAINER/random ID, RB |
| 83 Farfetch’d |  | BU |  |  | Farfetch’d «アッカ
Akka» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 85 Dodrio |  | E |  |  | Dodrio della cartuccia, box 8 posto 30 |
| 85 Dodrio |  | C |  |  | Dodrio «DORIS» di EMY/00283, C |
| 85 Dodrio |  | C |  |  | Dodrio al livello 10.0, Crystal |
| 86 Seel |  | BU, GN, RD |  |  | Seel «SAILOR» di TRAINER/random ID, RB |
| 87 Dewgong |  | BU, GN, RD |  |  | Dewgong «SAILOR» di TRAINER/random ID, RB |
| 87 Dewgong |  | YW |  |  | Dewgong «CEZANNE» di TRAINER/random ID, Yellow |
| 87 Dewgong |  | FR, LG |  |  | Dewgong «SEELOR» di GARETT/09853, FRLG |
| 87 Dewgong |  | C, GD, SI, YW |  |  | Dewgong al livello 5.0, GSC + Y |
| 88 Grimer | Alola | qualunque |  |  | Grimer di Alola con Power of Alchemy |
| 89 Muk |  | YW |  |  | Muk «STICKY» di TRAINER/random ID, Yellow |
| 89 Muk |  | C, GD, SI, YW |  |  | Muk al livello 5.0, GSC + Y |
| 89 Muk | Alola | MN, SN, UM, US |  |  | casella Muk Alola; Muk Alolan Form, origine SMUSUM |
| 91 Cloyster |  | E |  |  | Cloyster della cartuccia, box 6 posto 1 |
| 91 Cloyster |  | E |  |  | Cloyster della cartuccia, box 6 posto 7 |
| 91 Cloyster |  | E |  |  | Cloyster della cartuccia, box 9 posto 19 |
| 91 Cloyster |  | E |  |  | Cloyster della cartuccia, box 13 posto 1 |
| 92 Gastly |  | UM, US |  |  | Gastly, USUM: At night, if you go to the Trainer School you will see a girl and her Drifloon.  |
| 93 Haunter |  | C |  |  | Haunter al livello 15.0, Crystal |
| 94 Gengar |  | E |  |  | Gengar della cartuccia, box 1 posto 30 |
| 94 Gengar |  | BU |  |  | Gengar «ゴーすけ
Ghosuke» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 94 Gengar |  | D, P, Pt |  |  | Gengar, Silver, DPPt: ★4: Old Chateau. Dual-Slot. Caught as Gengar. |
| 94 Gengar |  | C |  |  | Gengar al livello 15.0, Crystal |
| 95 Onix |  | C, GD, SI |  |  | Onix «ROCKY» di KYLE/48926, GSC |
| 97 Hypno |  | UM, US |  |  | Hypno x3, USUM: After completion of the Akala Grand Trial, when you speak to Ilima in the Hau'ol |
| 97 Hypno |  | GD, HG, SI, SS |  |  | Hypno al livello 16.0, GS HGSS |
| 98 Krabby |  | E |  |  | Krabby della cartuccia, box 11 posto 15 |
| 98 Krabby |  | BU |  |  | Krabby «どうらく
Dōraku» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 99 Kingler |  | BU |  |  | Kingler «どうらく
Dōraku» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 99 Kingler |  | YW |  |  | Kingler al livello 15.0, Yellow |
| 100 Voltorb |  | C, GD, SI |  |  | Voltorb «VOLTY» di TIM/29189, GSC |
| 100 Voltorb |  | BU, GN, RD, YW |  |  | Voltorb, RBY: Interactable, Power plant. |
| 100 Voltorb |  | AS, OR |  |  | Voltorb, ORAS: Interactable, New Mawville. |
| 101 Electrode |  | E |  |  | Electrode della cartuccia, box 8 posto 9 |
| 101 Electrode |  | BU, GN, RD |  |  | Electrode «DORIS» di TRAINER/random ID, RB |
| 101 Electrode |  | C, GD, SI |  |  | Electrode «VOLTY» di TIM/29189, GSC |
| 101 Electrode |  | HG, SS |  |  | Electrode «Billy» di Richard/29189, HGSS |
| 101 Electrode |  | BU, GN, RD, YW |  |  | Electrode, RBY: Interactable, Power plant. |
| 101 Electrode |  | C, GD, SI |  |  | Electrode, GSC: Interactable, Mahogany Town Rocket Hideout |
| 101 Electrode |  | HG, SS |  |  | Electrode, HGSS: Interactable, Mahogany Town Rocket Hideout |
| 101 Electrode |  | AS, OR |  |  | Electrode, ORAS: Interactable, Team Hideouts |
| 101 Electrode |  | UM, US |  |  | Electrode, USUM: During the Team Rainbow Rocket takeover of the Aether Foundation, you will find  |
| 101 Electrode |  | BU, GN, RD |  |  | Electrode al livello 3.0, RB |
| 103 Exeggutor |  | BU, GN, RD, YW |  |  | Exeggutor, Bronze, RBY: ★3: Alolan Form. |
| 104 Cubone |  | C |  |  | Cubone, C: Goldenrod game Corner |
| 105 Marowak |  | E |  |  | Marowak della cartuccia, box 8 posto 20 |
| 105 Marowak |  | BU, GN, RD, YW |  |  | Marowak, Bronze, RBY: ★4: Alolan Form. |
| 105 Marowak |  | C |  |  | Marowak al livello 12.0, Crystal |
| 105 Marowak | Alola | MN, SN, UM, US |  |  | casella Marowak Alola; Marowak Alolan Form, origine SMUSUM |
| 106 Hitmonlee |  | E |  |  | Hitmonlee della cartuccia, box 4 posto 28 |
| 106 Hitmonlee |  | FR, LG |  |  | Hitmonlee, FRLG: Fighting Dojo. |
| 107 Hitmonchan |  | E |  |  | Hitmonchan della cartuccia, box 4 posto 26 |
| 107 Hitmonchan |  | FR, LG |  |  | Hitmonchan, FRLG: Fighting Dojo. |
| 108 Lickitung |  | BU, GN, RD |  |  | Lickitung «MARC» di TRAINER/random ID, RB |
| 110 Weezing |  | E |  |  | Weezing della cartuccia, box 8 posto 14 |
| 110 Weezing |  | BU, GN, RD, YW |  |  | Weezing, Bronze, RBY: ★5: Galarian Form. |
| 111 Rhyhorn |  | E |  |  | Rhyhorn della cartuccia, box 4 posto 7 |
| 111 Rhyhorn |  | B, B2, W, W2 |  |  | Rhyhorn «» di Yancy/10303, BWB2W2 |
| 111 Rhyhorn |  | B, B2, W, W2 |  |  | Rhyhorn «» di Curtis/54118, BWB2W2 |
| 112 Rhydon |  | YW |  |  | Rhydon «BUFFY» di TRAINER/random ID, Yellow |
| 112 Rhydon |  | GD, SI |  |  | Rhydon «DON» di EMY/00283, GS |
| 112 Rhydon |  | HG, SS |  |  | Rhydon «Hornlette» di Brock/06845, HGSS |
| 112 Rhydon |  | B, B2, W, W2 |  |  | Rhydon «» di Yancy/10303, BWB2W2 |
| 112 Rhydon |  | B, B2, W, W2 |  |  | Rhydon «» di Curtis/54118, BWB2W2 |
| 112 Rhydon |  | YW |  |  | Rhydon al livello 10.0, Yellow |
| 113 Chansey |  | MN, SN |  |  | Chansey «Happini» di Momoe/010913, SM |
| 113 Chansey |  | BU, GN, RD, YW |  |  | Chansey, Gold, RBY: ★1: Safari Zone. |
| 114 Tangela |  | BU, GN, RD |  |  | Tangela «CRINKLES» di TRAINER/random ID, RB |
| 115 Kangaskhan |  | E |  |  | Kangaskhan della cartuccia, box 1 posto 13 |
| 115 Kangaskhan |  | BU |  |  | Kangaskhan «ロダン
Rodan» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 116 Horsea |  | E |  |  | Horsea della cartuccia, box 7 posto 7 |
| 116 Horsea |  | BU |  |  | Horsea, Blue (Jp): Game Corner Prize |
| 117 Seadra |  | E |  |  | Seadra «SEASOR» di SKYLAR/46285, E |
| 119 Seaking |  | C, GD, SI |  |  | Seaking al livello 10.0, GSC |
| 121 Starmie |  | E |  |  | Starmie della cartuccia, box 9 posto 3 |
| 122 Mr. Mime |  | BU, GN, RD |  |  | Mr. Mime «MARCEL» di TRAINER/random ID, RB |
| 122 Mr. Mime |  | BU |  |  | Mr. Mime «まさる
Masaru» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 122 Mr. Mime |  | YW |  |  | Mr. Mime «MILES» di TRAINER/random ID, Yellow |
| 122 Mr. Mime |  | GD, SI |  |  | Mr. Mime, GS: Celadon Game Corner |
| 122 Mr. Mime |  | HG, SS |  |  | Mr. Mime, HGSS: Celadon Game Corner |
| 122 Mr. Mime |  | D, P, Pt |  |  | Mr. Mime, Bronze, DPPt: ★51: Galarian Form. |
| 123 Scyther |  | BU, GN, RD, YW |  |  | Scyther, RBY: Game Corner Prize |
| 123 Scyther |  | FR, LG |  |  | Scyther, FRLG: Game Corner Prize |
| 123 Scyther |  | HG, SS |  |  | Scyther, Bronze, HGSS: ★56: Bug-Catching Contest. |
| 124 Jynx |  | E |  |  | Jynx della cartuccia, box 2 posto 24 |
| 124 Jynx |  | BU, GN, RD |  |  | Jynx «LOLA» di TRAINER/random ID, RB |
| 124 Jynx |  | UM, US |  |  | Jynx al livello 9.0, USUM |
| 125 Electabuzz |  | CXD |  |  | Electabuzz «ZAPRONG» di HORDEL/41400, XD: Gale of Darkness |
| 125 Electabuzz |  | E, FR, LG, R, S |  |  | Electabuzz al livello 10.0, FRLG RSE |
| 126 Magmar |  | E, FR, LG, R, S |  |  | Magmar al livello 10.0, FRLG RSE |
| 127 Pinsir |  | E |  |  | Pinsir della cartuccia, box 2 posto 1 |
| 127 Pinsir |  | BU, GN, RD, YW |  |  | Pinsir, RBY: Game Corner Prize |
| 127 Pinsir |  | UM, US |  |  | Pinsir x3, USUM: On Exeggutor Island, when you first arrive, you'll find something affecting the  |
| 127 Pinsir |  | HG, SS |  |  | Pinsir, Bronze, HGSS: ★57: Bug-Catching Contest. |
| 128 Tauros |  | BU |  |  | Tauros «ぎゅうた
Gyūta» di TRAINERトレーナ
/random ID, Blue (Jp) |
| 129 Magikarp |  | E |  |  | Magikarp della cartuccia, box 9 posto 2 |
| 129 Magikarp |  | E |  |  | Magikarp della cartuccia, box 9 posto 21 |
| 129 Magikarp |  | BU, GN, RD, YW |  |  | Magikarp, RBY: Route 4 PKMN Center. |
| 129 Magikarp |  | B2, W2 |  |  | Magikarp, Platinum, B2W2: ★9: Nature Preserve. Caught as Level 1. |
| 129 Magikarp |  | B2, W2 |  |  | Magikarp, Platinum, B2W2: ★10: Nature Preserve. Caught as Level 100. |
| 129 Magikarp |  | X, Y |  |  | Magikarp, Bronze, XY: ★83: Hotel. Trade. |
| 130 Gyarados |  | E |  |  | Gyarados della cartuccia, box 7 posto 17 |
| 130 Gyarados |  | E |  |  | Gyarados della cartuccia, box 9 posto 22 |
| 130 Gyarados |  | E |  |  | Gyarados della cartuccia, box 13 posto 3 |
| 130 Gyarados |  | E |  |  | Gyarados della cartuccia, box 13 posto 19 |
| 130 Gyarados |  | X, Y |  |  | Gyarados «Carpe Diem» di Caveat/44285, XY |
| 130 Gyarados |  | C, GD, SI |  |  | Gyarados, Bronze, GSC: ★29: Lake of Rage. Guaranteed Shiny. |
| 130 Gyarados |  | B2, W2 |  |  | Gyarados al livello 1.0, B2W2 |
| 131 Lapras |  | E |  |  | Lapras della cartuccia, box 1 posto 24 |
| 131 Lapras |  | E |  |  | Lapras della cartuccia, box 3 posto 18 |
| 131 Lapras |  | BU, GN, RD, YW |  |  | Lapras, RBY: Silph Co. |
| 131 Lapras |  | C, GD, SI |  |  | Lapras, GSC: Interactable, Union Cave, every Friday. |
| 131 Lapras |  | FR, LG |  |  | Lapras, FRLG: Silph Co. |
| 131 Lapras |  | HG, SS |  |  | Lapras, HGSS: Interactable, Union Cave, every Friday. |
| 131 Lapras |  | X, Y |  |  | Lapras, XY: Route 12, near the gate of the route. |
| 132 Ditto |  | UM, US |  |  | Ditto x5, USUM: After completion of the Akala Grand Trial, when you speak to the policeman in Ro |
| 133 Eevee |  | C, GD, SI |  |  | Eevee, GSC: Given by Bill in his home in Goldenrod City, after interacting with him in Ecrut |
| 133 Eevee |  | GD, SI |  |  | Eevee, GS: Celadon Game Corner |
| 133 Eevee |  | B2, W2 |  |  | Eevee, B2W2: Castelia City, on the third floor of the builing to the left in the street of th |
| 134 Vaporeon |  | D, P, Pt |  |  | Vaporeon «» di Hayley/01000, My Pokémon Ranch |
| 134 Vaporeon |  | X, Y |  |  | Vaporeon «Stevie» di Elena/29294, XY |
| 135 Jolteon |  | D, P, Pt |  |  | Jolteon «» di Hayley/01000, My Pokémon Ranch |
| 135 Jolteon |  | X, Y |  |  | Jolteon «Stevie» di Elena/29294, XY |
| 136 Flareon |  | D, P, Pt |  |  | Flareon «» di Hayley/01000, My Pokémon Ranch |
| 136 Flareon |  | X, Y |  |  | Flareon «Stevie» di Elena/29294, XY |
| 137 Porygon |  | BU, GN, RD, YW |  |  | Porygon, RBY: Game Corner Prize |
| 137 Porygon |  | C, GD, SI |  |  | Porygon, GSC: Celadon Game Corner |
| 137 Porygon |  | Pt |  |  | Porygon, Pt: Given by a Poké fan in Veilstone City. |
| 137 Porygon |  | HG, SS |  |  | Porygon, HGSS: Celadon Game Corner |
| 137 Porygon |  | MN, SN |  |  | Porygon, SM: Aether House in Route 15, after beating the Elite 4. |
| 137 Porygon |  | UM, US |  |  | Porygon, USUM: Aether House in Route 15, after defeating Team Rainbow Rocket. |
| 142 Aerodactyl |  | C, GD, SI |  |  | Aerodactyl «AEROY» di KIM/26491, GSC |
| 143 Snorlax |  | B, W |  |  | Snorlax «Gorge» di Ander/40217, BW |
| 143 Snorlax |  | B, B2, W, W2 |  |  | Snorlax «» di Yancy/10303, BWB2W2 |
| 143 Snorlax |  | B, B2, W, W2 |  |  | Snorlax «» di Curtis/54118, BWB2W2 |
| 143 Snorlax |  | BU, GN, RD, YW |  |  | Snorlax, RBY: Interactable, Route 12, Route 16. |
| 143 Snorlax |  | C, GD, SI |  |  | Snorlax, GSC: Interactable, Vermillion City. |
| 143 Snorlax |  | HG, SS |  |  | Snorlax, HGSS: Interactable, Vermillion City. |
| 143 Snorlax |  | X, Y |  |  | Snorlax, XY: Interactable, Route 7. |
| 144 Articuno |  | E |  |  | Articuno della cartuccia, box 3 posto 6 |
| 144 Articuno |  | E |  |  | Articuno della cartuccia, box 3 posto 12 |
| 144 Articuno |  | BU, GN, RD, YW |  |  | Articuno, Platinum, RBY: ★1: Seaform Islands. Shiny. |
| 144 Articuno |  | X, Y |  |  | Articuno, Silver, XY: ★10 |
| 145 Zapdos |  | E |  |  | Zapdos della cartuccia, box 3 posto 11 |
| 145 Zapdos |  | BU, GN, RD, YW |  |  | Zapdos, Platinum, RBY: ★1: Power Plant. Shiny. |
| 145 Zapdos |  | X, Y |  |  | Zapdos, Silver, XY: ★10 |
| 146 Moltres |  | E |  |  | Moltres della cartuccia, box 3 posto 4 |
| 146 Moltres |  | E |  |  | Moltres della cartuccia, box 3 posto 10 |
| 146 Moltres |  | BU, GN, RD, YW |  |  | Moltres, Platinum, RBY: ★1: Victory Road. Shiny. |
| 146 Moltres |  | X, Y |  |  | Moltres, Silver, XY: ★10 |
| 147 Dratini |  | BU, GN, RD |  |  | Dratini, RB: Game Corner Prize |
| 147 Dratini |  | GD, SI |  |  | Dratini, GS: Goldenrod game Corner |
| 147 Dratini |  | C |  |  | Dratini, Bronze, Crystal: ★30: Dragon's Den. ExtremeSpeed. Gift. |
| 147 Dratini |  | qualunque |  |  | Dratini, Gold, White 2: ★6: Flocessy Town. |
| 148 Dragonair |  | C, GD, SI |  |  | Dragonair al livello 10.0, GSC |
| 149 Dragonite |  | E |  |  | Dragonite della cartuccia, box 14 posto 24 |
| 149 Dragonite |  | E |  |  | Dragonite della cartuccia, box 14 posto 29 |
| 149 Dragonite |  | CXD |  |  | Dragonite, Gold, XD: Gale of Darkness: ★26 |
| 150 Mewtwo |  | E |  |  | Mewtwo della cartuccia, box 3 posto 15 |
| 150 Mewtwo |  | E |  |  | Mewtwo della cartuccia, box 3 posto 16 |
| 150 Mewtwo |  | BU, GN, RD, YW |  |  | Mewtwo, Platinum, RBY: ★1: Cerulean Cave. Shiny. |
| 151 Mew |  | qualunque | Premier Ball |  | Mew in Premier Ball, da Rosso Fuoco e Verde Foglia giapponesi |
| 151 Mew |  | qualunque | Cura Ball |  | Mew in Cura Ball, da Rosso Fuoco e Verde Foglia giapponesi |
| 151 Mew |  | qualunque | Sub Ball | sì | Mew cromatico in Sub Ball, da Rosso Fuoco e Verde Foglia giapponesi |
| 151 Mew |  | qualunque | Mega Ball | sì | Mew cromatico in Mega Ball, da Rosso Fuoco e Verde Foglia giapponesi |
| 151 Mew |  | qualunque | Poké Ball | sì | Mew cromatico in Poké Ball, da Rosso Fuoco e Verde Foglia giapponesi |
| 151 Mew |  | D, P, Pt |  |  | Mew, Platinum, My Pokémon Ranch: ★18 |
| 151 Mew |  | qualunque |  | sì | Mew cromatico |
| 152 Chikorita |  | E |  |  | Chikorita, Platinum, Emerald: ★4: Littleroot Town. Gift. |
| 152 Chikorita |  | CXD |  |  | Chikorita, Platinum, XD: Gale of Darkness: ★17 |
| 152 Chikorita |  | C, GD, HG, SI, SS |  |  | Chikorita con origine GSC HGSS |
| 153 Bayleef |  | C, GD, HG, SI, SS |  |  | Bayleef con origine GSC HGSS |
| 154 Meganium |  | C, GD, HG, SI, SS |  |  | Meganium ♀, origine GSC HGSS |
| 155 Cyndaquil |  | E |  |  | Cyndaquil, Platinum, Emerald: ★4: Littleroot Town. Gift. |
| 155 Cyndaquil |  | CXD |  |  | Cyndaquil, Platinum, XD: Gale of Darkness: ★17 |
| 156 Quilava |  | C, GD, HG, SI, SS |  |  | Quilava con origine GSC HGSS |
| 157 Typhlosion |  | C, GD, SI |  |  | Typhlosion, Bronze, GSC: ★31: Hisuian Form. |
| 158 Totodile |  | E |  |  | Totodile, Platinum, Emerald: ★4: Littleroot Town. Gift. |
| 158 Totodile |  | CXD |  |  | Totodile, Platinum, XD: Gale of Darkness: ★17 |
| 158 Totodile |  | C, GD, HG, SI, SS |  |  | Totodile con origine GSC HGSS |
| 159 Croconaw |  | C, GD, HG, SI, SS |  |  | Croconaw con origine GSC HGSS |
| 161 Sentret |  | E |  |  | Sentret della cartuccia, box 4 posto 3 |
| 161 Sentret |  | E |  |  | Sentret della cartuccia, box 4 posto 4 |
| 162 Furret |  | C, GD, HG, SI, SS |  |  | Furret al livello 6.0, GSC HGSS |
| 164 Noctowl |  | E |  |  | Noctowl della cartuccia, box 11 posto 2 |
| 164 Noctowl |  | C |  |  | Noctowl al livello 4.0, Crystal |
| 165 Ledyba |  | C, GD, HG, SI, SS | Safari Ball |  | Ledyba in Safari Ball; Ledyba con origine GSC HGSS; Ledyba ♂, origine GSC HGSS |
| 165 Ledyba |  | C, GD, HG, SI, SS | Dream Ball |  | Ledyba in Dream Ball; Ledyba ♀, origine GSC HGSS |
| 165 Ledyba |  | qualunque | UC Ball |  | Ledyba in UC Ball |
| 166 Ledian |  | E |  |  | Ledian della cartuccia, box 7 posto 24 |
| 166 Ledian |  | SS |  |  | Ledian al livello 5.0, SS; Ledian con origine GSC HGSS; Ledian ♂, origine GSC HGSS |
| 166 Ledian |  | C, GD, HG, SI, SS |  |  | Ledian ♀, origine GSC HGSS |
| 167 Spinarak |  | C, GD, HG, SI, SS |  |  | Spinarak con origine GSC HGSS |
| 168 Ariados |  | E |  |  | Ariados della cartuccia, box 7 posto 22 |
| 168 Ariados |  | HG |  |  | Ariados al livello 5.0, HG; Ariados con origine GSC HGSS |
| 169 Crobat |  | E |  |  | Crobat della cartuccia, box 13 posto 13 |
| 169 Crobat |  | BU, GN, RD, YW |  |  | Crobat, Bronze, RBY: ★6 |
| 169 Crobat |  | Pt |  |  | Crobat al livello 10.0, Pt + PLA |
| 171 Lanturn |  | E |  |  | Lanturn della cartuccia, box 8 posto 11; casella Lanturn |
| 171 Lanturn |  | UM, US |  |  | Lanturn al livello 10.0, USUM |
| 171 Lanturn |  | C, GD, HG, SI, SS |  |  | Lanturn con origine GSC HGSS |
| 172 Pichu |  | E |  |  | Pichu della cartuccia, box 9 posto 28 |
| 172 Pichu |  | C |  |  | Pichu, Platinum, Crystal: ★2: Odd Egg. Shiny. |
| 172 Pichu |  | qualunque |  |  | Pichu, Platinum, Box Ruby & Sapphire: ★16 |
| 173 Cleffa |  | C |  |  | Cleffa, Platinum, Crystal: ★2: Odd Egg. Shiny. |
| 174 Igglybuff |  | C |  |  | Igglybuff, Platinum, Crystal: ★2: Odd Egg. Shiny. |
| 175 Togepi |  | B, B2, W, W2 |  |  | Togepi «» di Yancy/10303, BWB2W2 |
| 175 Togepi |  | B, B2, W, W2 |  |  | Togepi «» di Curtis/54118, BWB2W2 |
| 175 Togepi |  | C, GD, SI |  |  | Togepi, GSC: Elm's Aide in Violet City Poké Mart.; Togepi con origine GSC HGSS |
| 175 Togepi |  | Pt |  |  | Togepi, Pt: Egg Given by Cynthia in Eterna City. |
| 175 Togepi |  | AS, OR |  |  | Togepi, ORAS: Egg, Lavaridge Town, after defeating Groudon/Kyogre. |
| 175 Togepi |  | CXD |  |  | Togepi, Platinum, Colosseum: ★19: Card e Room. |
| 176 Togetic |  | B, B2, W, W2 |  |  | Togetic «» di Yancy/10303, BWB2W2 |
| 176 Togetic |  | B, B2, W, W2 |  |  | Togetic «» di Curtis/54118, BWB2W2 |
| 176 Togetic |  | CXD |  |  | Togetic, Silver, Colosseum: ★44: Outskirt Stand. |
| 176 Togetic |  | C, GD, HG, SI, SS |  |  | Togetic con origine GSC HGSS |
| 177 Natu |  | E |  |  | Natu della cartuccia, box 7 posto 5 |
| 177 Natu |  | E |  |  | Natu della cartuccia, box 11 posto 10 |
| 178 Xatu |  | E |  |  | Xatu della cartuccia, box 8 posto 27 |
| 178 Xatu |  | C |  |  | Xatu «PAUL» di CHRIS/15616, C; Xatu ♀, origine GSC HGSS |
| 178 Xatu |  | C |  |  | Xatu al livello 15.0, Crystal |
| 179 Mareep |  | E |  |  | Mareep della cartuccia, box 11 posto 26 |
| 179 Mareep |  | CXD |  |  | Mareep, Platinum, Colosseum: ★19: Card e Room. |
| 179 Mareep |  | HG, SS |  |  | Mareep, Bronze, HGSS: ★58: Violet City. Egg. Gift. |
| 180 Flaaffy |  | UM, US |  |  | Flaaffy al livello 11.0, USUM |
| 180 Flaaffy |  | C, GD, HG, SI, SS |  |  | Flaaffy con origine GSC HGSS |
| 181 Ampharos |  | C, GD, HG, SI, SS |  |  | Ampharos con origine GSC HGSS |
| 182 Bellossom |  | E |  |  | Bellossom della cartuccia, box 8 posto 22; casella Bellossom |
| 182 Bellossom |  | BU, GN, RD, YW |  |  | Bellossom, Bronze, RBY: ★7 |
| 182 Bellossom |  | C, HG, SS |  |  | Bellossom al livello 14.0, C HGSS; Bellossom con origine GSC HGSS |
| 183 Marill |  | E |  |  | Marill della cartuccia, box 4 posto 14 |
| 183 Marill |  | E |  |  | Marill della cartuccia, box 9 posto 26 |
| 184 Azumarill |  | E |  |  | Azumarill della cartuccia, box 9 posto 27; casella Azumarill |
| 184 Azumarill |  | B2, W2 |  |  | Azumarill al livello 5.0, B2W2 |
| 184 Azumarill |  | C, GD, HG, SI, SS |  |  | Azumarill con origine GSC HGSS |
| 185 Sudowoodo |  | E |  |  | Sudowoodo della cartuccia, box 3 posto 19 |
| 185 Sudowoodo |  | E |  |  | Sudowoodo della cartuccia, box 3 posto 20 |
| 185 Sudowoodo |  | E |  |  | Sudowoodo della cartuccia, box 4 posto 16 |
| 185 Sudowoodo |  | HG, SS |  |  | Sudowoodo, HGSS: Interactable, Route 36.; Sudowoodo ♀, origine GSC HGSS |
| 185 Sudowoodo |  | E |  |  | Sudowoodo, Silver, Emerald: ★1: Battle Frontier. |
| 186 Politoed |  | C, GD, HG, SI, SS |  |  | Politoed «ロモたん
Romo-tan» di TRAINERトレーナ
/random ID, Blue (Jp) + gen 2 & up; Politoed con origine GSC HGSS; Politoed ♂, origine GSC HGSS |
| 186 Politoed |  | MN, SN |  |  | Politoed «Whirly» di Laule'a/590916, SM |
| 186 Politoed |  | BU, GN, RD, YW |  |  | Politoed, Bronze, RBY: ★8 |
| 186 Politoed |  | C, GD, HG, SI, SS |  |  | Politoed ♀, origine GSC HGSS |
| 188 Skiploom |  | C, GD, HG, SI, SS |  |  | Skiploom con origine GSC HGSS |
| 189 Jumpluff |  | C, GD, HG, SI, SS |  |  | Jumpluff con origine GSC HGSS |
| 190 Aipom |  | C, GD, HG, SI, SS |  |  | Aipom con origine GSC HGSS; Aipom ♂, origine GSC HGSS |
| 190 Aipom |  | C, GD, HG, SI, SS |  |  | Aipom ♀, origine GSC HGSS |
| 191 Sunkern |  | E |  |  | Sunkern della cartuccia, box 4 posto 10 |
| 192 Sunflora |  | E |  |  | Sunflora della cartuccia, box 8 posto 23 |
| 192 Sunflora |  | C, GD, HG, SI, SS |  |  | Sunflora con origine GSC HGSS |
| 194 Wooper |  | HG, SS |  |  | Wooper, Bronze, HGSS: ★58: Violet City. Egg. Gift.; Wooper ♀, origine GSC HGSS |
| 195 Quagsire |  | E |  |  | Quagsire della cartuccia, box 7 posto 8 |
| 195 Quagsire |  | HG, SS |  |  | Quagsire al livello 10.0, HGSS; Quagsire con origine GSC HGSS; Quagsire ♂, origine GSC HGSS |
| 195 Quagsire |  | C, GD, HG, SI, SS |  |  | Quagsire ♀, origine GSC HGSS |
| 196 Espeon |  | D, P, Pt |  |  | Espeon «» di Hayley/01000, My Pokémon Ranch |
| 196 Espeon |  | X, Y |  |  | Espeon «Stevie» di Elena/29294, XY |
| 196 Espeon |  | BU, GN, RD, YW |  |  | Espeon, Bronze, RBY: ★9 |
| 196 Espeon |  | C, GD, HG, SI, SS |  |  | Espeon con origine GSC HGSS |
| 197 Umbreon |  | D, P, Pt |  |  | Umbreon «» di Hayley/01000, My Pokémon Ranch |
| 197 Umbreon |  | X, Y |  |  | Umbreon «Stevie» di Elena/29294, XY |
| 197 Umbreon |  | BU, GN, RD, YW |  |  | Umbreon, Bronze, RBY: ★10 |
| 197 Umbreon |  | C, GD, HG, SI, SS |  |  | Umbreon con origine GSC HGSS |
| 198 Murkrow |  | C, GD, HG, SI, SS |  |  | Murkrow ♂, origine GSC HGSS |
| 199 Slowking |  | C, GD, HG, SI, SS |  |  | Slowking «オスカル
Oscar» di TRAINERトレーナ
/random ID, Blue (Jp) + gen 2 & up; Slowking con origine GSC HGSS |
| 199 Slowking |  | BU, GN, RD, YW |  |  | Slowking, Bronze, RBY: ★11 |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown A Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown B Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown C Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown D Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown E Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown F Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown G Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown H Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown I Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown J Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown K Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown L Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown M Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown N Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown O Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown P Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown Q Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown R Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown S Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown T Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown U Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown V Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown W Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown X Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown Y Form, origine GSC HGSS |
| 201 Unown |  | C, GD, HG, SI, SS |  |  | Unown Z Form, origine GSC HGSS |
| 201 Unown |  | HG, SS |  |  | Unown ! Form, origine HGSS |
| 201 Unown |  | HG, SS |  |  | Unown ? Form, origine HGSS |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: A Form.; Unown con origine GSC HGSS |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: B Form. |
| 201 Unown |  | C, GD, SI |  |  | Unown, Gold, GSC: ★2: C Form. |
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
| 201 Unown |  | FR, LG |  |  | Unown, Silver, FRLG: ★2: ! Form. |
| 201 Unown |  | FR, LG |  |  | Unown, Silver, FRLG: ★2: ? Form. |
| 202 Wobbuffet |  | E |  |  | Wobbuffet della cartuccia, box 4 posto 13 |
| 202 Wobbuffet |  | D, P, Pt |  |  | Wobbuffet «» di Hayley/01000, My Pokémon Ranch |
| 202 Wobbuffet |  | B, B2, W, W2 |  |  | Wobbuffet «» di Yancy/10303, BWB2W2 |
| 202 Wobbuffet |  | B, B2, W, W2 |  |  | Wobbuffet «» di Curtis/54118, BWB2W2 |
| 202 Wobbuffet |  | C, GD, HG, SI, SS |  |  | Wobbuffet ♂, origine GSC HGSS |
| 203 Girafarig |  | E |  |  | Girafarig della cartuccia, box 4 posto 11 |
| 203 Girafarig |  | C, GD, HG, SI, SS |  |  | Girafarig ♂, origine GSC HGSS |
| 205 Forretress |  | X, Y |  |  | Forretress al livello 30.0, XY |
| 205 Forretress |  | C, GD, HG, SI, SS |  |  | Forretress con origine GSC HGSS |
| 206 Dunsparce |  | C, GD, HG, SI, SS |  |  | Dunsparce con origine GSC HGSS |
| 207 Gligar |  | C, GD, HG, SI, SS |  |  | Gligar ♀, origine GSC HGSS |
| 208 Steelix |  | C, GD, SI |  |  | Steelix «ROCKY» di KYLE/48926, GSC; Steelix ♀, origine GSC HGSS |
| 208 Steelix |  | AS, OR |  |  | Steelix «» di Orlando/Random ID, ORAS |
| 208 Steelix |  | BU, GN, RD, YW |  |  | Steelix, Bronze, RBY: ★12 |
| 208 Steelix |  | AS, OR |  |  | Steelix, Gold, JP ORAS Demo: ★33 |
| 209 Snubbull |  | C, GD, HG, SI, SS |  |  | Snubbull con origine GSC HGSS |
| 210 Granbull |  | C |  |  | Granbull al livello 15.0, Crystal; Granbull con origine GSC HGSS |
| 211 Qwilfish |  | C, GD, HG, SI, SS |  |  | Qwilfish con origine GSC HGSS |
| 212 Scizor |  | E |  |  | Scizor della cartuccia, box 3 posto 23 |
| 212 Scizor |  | BU, GN, RD, YW |  |  | Scizor, Bronze, RBY: ★13 |
| 212 Scizor |  | CXD |  |  | Scizor, Platinum, Colosseum: ★19: Card e Room. |
| 212 Scizor |  | C, GD, HG, SI, SS |  |  | Scizor ♀, origine GSC HGSS |
| 213 Shuckle |  | E |  |  | Shuckle della cartuccia, box 3 posto 30 |
| 213 Shuckle |  | E |  |  | Shuckle della cartuccia, box 11 posto 16 |
| 213 Shuckle |  | C, GD, SI |  |  | Shuckle «SHUCKIE» di MANIA/00518, GSC |
| 214 Heracross |  | E |  |  | Heracross della cartuccia, box 13 posto 15 |
| 214 Heracross |  | C, GD, HG, SI, SS |  |  | Heracross con origine GSC HGSS; Heracross ♂, origine GSC HGSS |
| 214 Heracross |  | C, GD, HG, SI, SS |  |  | Heracross ♀, origine GSC HGSS |
| 215 Sneasel |  | C, GD, HG, SI, SS |  |  | Sneasel ♀, origine GSC HGSS |
| 216 Teddiursa |  | B, B2, W, W2 |  |  | Teddiursa «» di Yancy/10303, BWB2W2 |
| 216 Teddiursa |  | B2, W2 |  |  | Teddiursa, Gold, B2W2: ★7: Nimbasa City. Trade. |
| 217 Ursaring |  | B, B2, W, W2 |  |  | Ursaring «» di Yancy/10303, BWB2W2 |
| 217 Ursaring |  | C |  |  | Ursaring al livello 25.0, Crystal; Ursaring con origine GSC HGSS; Ursaring ♂, origine GSC HGSS |
| 217 Ursaring |  | C, GD, HG, SI, SS |  |  | Ursaring ♀, origine GSC HGSS |
| 218 Slugma |  | HG, SS |  |  | Slugma, Bronze, HGSS: ★58: Violet City. Egg. Gift. |
| 219 Magcargo |  | E |  |  | Magcargo della cartuccia, box 8 posto 7 |
| 219 Magcargo |  | C, GD, HG, SI, SS |  |  | Magcargo con origine GSC HGSS |
| 221 Piloswine |  | C, GD, HG, SI, SS |  |  | Piloswine con origine GSC HGSS; Piloswine ♂, origine GSC HGSS |
| 221 Piloswine |  | C, GD, HG, SI, SS |  |  | Piloswine ♀, origine GSC HGSS |
| 222 Corsola |  | E |  |  | Corsola della cartuccia, box 9 posto 4 |
| 224 Octillery |  | UM, US |  |  | Octillery al livello 10.0, USUM |
| 224 Octillery |  | C, GD, HG, SI, SS |  |  | Octillery ♂, origine GSC HGSS |
| 225 Delibird |  | C, GD, HG, SI, SS |  |  | Delibird con origine GSC HGSS |
| 226 Mantine |  | C, GD, HG, SI, SS |  |  | Mantine con origine GSC HGSS |
| 227 Skarmory |  | E |  |  | Skarmory della cartuccia, box 7 posto 16 |
| 227 Skarmory |  | C, GD, HG, SI, SS |  |  | Skarmory con origine GSC HGSS |
| 229 Houndoom |  | E |  |  | Houndoom della cartuccia, box 13 posto 14 |
| 229 Houndoom |  | C, GD, HG, SI, SS |  |  | Houndoom con origine GSC HGSS; Houndoom ♂, origine GSC HGSS |
| 229 Houndoom |  | C, GD, HG, SI, SS |  |  | Houndoom ♀, origine GSC HGSS |
| 230 Kingdra |  | E |  |  | Kingdra «SEASOR» di SKYLAR/46285, E |
| 230 Kingdra |  | BU, GN, RD, YW |  |  | Kingdra, Bronze, RBY: ★14 |
| 230 Kingdra |  | C, GD, HG, SI, SS |  |  | Kingdra con origine GSC HGSS |
| 231 Phanpy |  | E |  |  | Phanpy della cartuccia, box 4 posto 1; casella Phanpy |
| 231 Phanpy |  | B, B2, W, W2 |  |  | Phanpy «» di Curtis/54118, BWB2W2 |
| 231 Phanpy |  | B2, W2 |  |  | Phanpy, Gold, B2W2: ★8: Nimbasa City. Trade. |
| 231 Phanpy |  | C, GD, HG, SI, SS |  |  | Phanpy con origine GSC HGSS |
| 232 Donphan |  | B, B2, W, W2 |  |  | Donphan «» di Curtis/54118, BWB2W2 |
| 232 Donphan |  | C, GD, HG, SI, SS |  |  | Donphan con origine GSC HGSS; Donphan ♂, origine GSC HGSS |
| 232 Donphan |  | C, GD, HG, SI, SS |  |  | Donphan ♀, origine GSC HGSS |
| 233 Porygon2 |  | E |  |  | Porygon2 della cartuccia, box 3 posto 13; casella Porygon2 |
| 233 Porygon2 |  | E |  |  | Porygon2 della cartuccia, box 3 posto 14 |
| 233 Porygon2 |  | BU, GN, RD, YW |  |  | Porygon2, Bronze, RBY: ★15 |
| 233 Porygon2 |  | C, GD, HG, SI, SS |  |  | Porygon2 con origine GSC HGSS |
| 235 Smeargle |  | E |  |  | Smeargle, E: Artisan Cave, Battle Frontier |
| 235 Smeargle |  | C, GD, HG, SI, SS |  |  | Smeargle con origine GSC HGSS |
| 236 Tyrogue |  | C |  |  | Tyrogue, Platinum, Crystal: ★2: Odd Egg. Shiny. |
| 237 Hitmontop |  | E |  |  | Hitmontop della cartuccia, box 4 posto 27 |
| 237 Hitmontop |  | C, GD, HG, SI, SS |  |  | Hitmontop con origine GSC HGSS |
| 238 Smoochum |  | C |  |  | Smoochum, Platinum, Crystal: ★2: Odd Egg. Shiny. |
| 239 Elekid |  | C |  |  | Elekid, Platinum, Crystal: ★2: Odd Egg. Shiny. |
| 240 Magby |  | C |  |  | Magby, Platinum, Crystal: ★2: Odd Egg. Shiny. |
| 241 Miltank |  | C, GD, HG, SI, SS |  |  | Miltank con origine GSC HGSS |
| 242 Blissey |  | MN, SN |  |  | Blissey «Happini» di Momoe/010913, SM; casella Blissey |
| 242 Blissey |  | BU, GN, RD, YW |  |  | Blissey, Bronze, RBY: ★16 |
| 242 Blissey |  | C, GD, HG, SI, SS |  |  | Blissey con origine GSC HGSS |
| 243 Raikou |  | E |  |  | Raikou della cartuccia, box 3 posto 9 |
| 243 Raikou |  | FR, LG |  |  | Raikou, Silver, FRLG: ★3 |
| 244 Entei |  | E |  |  | Entei della cartuccia, box 3 posto 8 |
| 244 Entei |  | FR, LG |  |  | Entei, Silver, FRLG: ★3 |
| 245 Suicune |  | E |  |  | Suicune della cartuccia, box 3 posto 7 |
| 245 Suicune |  | E |  |  | Suicune della cartuccia, box 6 posto 25 |
| 245 Suicune |  | E |  |  | Suicune della cartuccia, box 6 posto 26 |
| 245 Suicune |  | FR, LG |  |  | Suicune, Silver, FRLG: ★3 |
| 246 Larvitar |  | E |  |  | Larvitar della cartuccia, box 14 posto 23 |
| 246 Larvitar |  | C |  |  | Larvitar, C: Celadon Game Corner; Larvitar con origine GSC HGSS |
| 247 Pupitar |  | CXD |  |  | Pupitar «» di DUKING/37149, XD: Gale of Darkness |
| 247 Pupitar |  | C, GD, HG, SI, SS |  |  | Pupitar con origine GSC HGSS |
| 248 Tyranitar |  | E |  |  | Tyranitar della cartuccia, box 1 posto 15 |
| 248 Tyranitar |  | E |  |  | Tyranitar della cartuccia, box 2 posto 4 |
| 248 Tyranitar |  | E |  |  | Tyranitar della cartuccia, box 2 posto 8 |
| 248 Tyranitar |  | E |  |  | Tyranitar della cartuccia, box 3 posto 17 |
| 248 Tyranitar |  | E |  |  | Tyranitar della cartuccia, box 6 posto 9 |
| 248 Tyranitar |  | E |  |  | Tyranitar della cartuccia, box 6 posto 19 |
| 248 Tyranitar |  | E |  |  | Tyranitar della cartuccia, box 6 posto 20 |
| 248 Tyranitar |  | E |  |  | Tyranitar della cartuccia, box 14 posto 30 |
| 248 Tyranitar |  | CXD |  |  | Tyranitar «» di DUKING/37149, XD: Gale of Darkness |
| 248 Tyranitar |  | C, GD, HG, SI, SS |  |  | Tyranitar con origine GSC HGSS |
| 249 Lugia |  | E |  |  | Lugia della cartuccia, box 3 posto 22 |
| 249 Lugia |  | CXD |  |  | Lugia, Gold, XD: Gale of Darkness: ★27 |
| 249 Lugia |  | B2, W2 |  |  | Lugia, Silver, Dream Radar: ★47 |
| 249 Lugia |  | HG, SS |  |  | Lugia, per «Register Lugia from Pokémon HeartGold or Pokémon SoulSilver» |
| 250 Ho-Oh |  | E |  |  | Ho-Oh della cartuccia, box 3 posto 21 |
| 250 Ho-Oh |  | CXD |  |  | Ho-Oh «» di MATTLE/10048, Colosseum |
| 250 Ho-Oh |  | CXD |  |  | Ho-Oh, Gold, Colosseum: ★23 |
| 250 Ho-Oh |  | B2, W2 |  |  | Ho-Oh, Silver, Dream Radar: ★48 |
| 250 Ho-Oh |  | HG, SS |  |  | Ho-Oh, per «Register Ho-Oh from Pokémon HeartGold or Pokémon SoulSilver!» |
| 251 Celebi |  | CXD |  |  | Celebi «Ageto Celebi» di アゲト/31121, Colosseum |
| 251 Celebi |  | C |  |  | Celebi, Gold, Crystal: ★3 |
| 251 Celebi |  | CXD |  |  | Celebi, Gold, JP Colosseum Bonus Disc: ★24 |
| 251 Celebi |  | qualunque |  | sì | Celebi cromatico |
| 252 Treecko |  | AS, OR |  |  | Treecko, per «Register Treecko, Grovyle and Sceptile from Pokémon Omega Ruby or Pokémon Alpha Sapphire!»; Treecko, per «Register Treecko, Torchic, and Mudkip from Pokémon Omega Ruby or Pokémon Alpha Sapphire!» |
| 253 Grovyle |  | AS, OR |  |  | Grovyle, per «Register Treecko, Grovyle and Sceptile from Pokémon Omega Ruby or Pokémon Alpha Sapphire!» |
| 254 Sceptile |  | E |  |  | Sceptile della cartuccia, box 3 posto 24; Sceptile con origine RSE ORAS |
| 254 Sceptile |  | E |  |  | Sceptile della cartuccia, box 7 posto 27 |
| 254 Sceptile |  | AS, OR |  |  | Sceptile, per «Register Treecko, Grovyle and Sceptile from Pokémon Omega Ruby or Pokémon Alpha Sapphire!» |
| 255 Torchic |  | AS, OR |  |  | Torchic, per «Register Torchic, Combusken and Blaziken from Pokémon Omega Ruby or Pokémon Alpha Sapphire!»; Torchic, per «Register Treecko, Torchic, and Mudkip from Pokémon Omega Ruby or Pokémon Alpha Sapphire!»; Torchic ♀, origine RSE ORAS |
| 256 Combusken |  | AS, OR |  |  | Combusken, per «Register Torchic, Combusken and Blaziken from Pokémon Omega Ruby or Pokémon Alpha Sapphire!»; Combusken ♀, origine RSE ORAS |
| 257 Blaziken |  | E |  |  | Blaziken della cartuccia, box 1 posto 14; Blaziken ♀, origine RSE ORAS |
| 257 Blaziken |  | E |  |  | Blaziken della cartuccia, box 9 posto 17 |
| 257 Blaziken |  | AS, OR |  |  | Blaziken, per «Register Torchic, Combusken and Blaziken from Pokémon Omega Ruby or Pokémon Alpha Sapphire!» |
| 258 Mudkip |  | E |  |  | Mudkip della cartuccia, box 4 posto 17; casella Mudkip; Mudkip con origine RSE ORAS |
| 258 Mudkip |  | AS, OR |  |  | Mudkip, per «Register Mudkip, Marshtomp and Swampert from Pokémon Omega Ruby or Pokémon Alpha Sapphire!»; Mudkip, per «Register Treecko, Torchic, and Mudkip from Pokémon Omega Ruby or Pokémon Alpha Sapphire!» |
| 259 Marshtomp |  | AS, OR |  |  | Marshtomp, per «Register Mudkip, Marshtomp and Swampert from Pokémon Omega Ruby or Pokémon Alpha Sapphire!» |
| 260 Swampert |  | E |  |  | Swampert della cartuccia, box 13 posto 16; Swampert con origine RSE ORAS |
| 260 Swampert |  | E |  |  | Swampert della cartuccia, box 13 posto 24 |
| 260 Swampert |  | E |  |  | Swampert della cartuccia, box 14 posto 2 |
| 260 Swampert |  | AS, OR |  |  | Swampert, per «Register Mudkip, Marshtomp and Swampert from Pokémon Omega Ruby or Pokémon Alpha Sapphire!» |
| 261 Poochyena |  | AS, E, OR, R, S |  |  | Poochyena con origine RSE ORAS |
| 262 Mightyena |  | E |  |  | Mightyena della cartuccia, box 7 posto 18; Mightyena con origine RSE ORAS |
| 262 Mightyena |  | E |  |  | Mightyena della cartuccia, box 11 posto 17 |
| 263 Zigzagoon |  | E |  |  | Zigzagoon della cartuccia, box 11 posto 1 |
| 264 Linoone |  | E |  |  | Linoone della cartuccia, box 3 posto 26 |
| 264 Linoone |  | E |  |  | Linoone della cartuccia, box 3 posto 27 |
| 264 Linoone |  | E |  |  | Linoone della cartuccia, box 3 posto 28 |
| 264 Linoone |  | E |  |  | Linoone della cartuccia, box 3 posto 29 |
| 264 Linoone |  | E |  |  | Linoone della cartuccia, box 12 posto 5 |
| 264 Linoone |  | HG, SS |  |  | Linoone al livello 3.0, HGSS |
| 265 Wurmple |  | AS, E, OR, R, S | Gara Ball |  | Wurmple in Gara Ball; Wurmple con origine RSE ORAS |
| 265 Wurmple |  | qualunque | Dream Ball |  | Wurmple in Dream Ball |
| 266 Silcoon |  | AS, OR |  |  | Silcoon al livello 2.0, ORAS |
| 267 Beautifly |  | E |  |  | Beautifly della cartuccia, box 8 posto 18; casella Beautifly; Beautifly con origine RSE ORAS; Beautifly ♂, origine RSE ORAS |
| 267 Beautifly |  | AS, E, OR, R, S |  |  | Beautifly ♀, origine RSE ORAS |
| 268 Cascoon |  | E |  |  | Cascoon della cartuccia, box 9 posto 14; casella Cascoon; Cascoon con origine RSE ORAS |
| 268 Cascoon |  | AS, OR |  |  | Cascoon al livello 2.0, ORAS |
| 269 Dustox |  | E |  |  | Dustox della cartuccia, box 7 posto 14; casella Dustox; Dustox con origine RSE ORAS; Dustox ♂, origine RSE ORAS |
| 269 Dustox |  | AS, E, OR, R, S |  |  | Dustox ♀, origine RSE ORAS |
| 270 Lotad |  | E |  |  | Lotad della cartuccia, box 2 posto 19 |
| 270 Lotad |  | E |  |  | Lotad della cartuccia, box 2 posto 20 |
| 271 Lombre |  | AS |  |  | Lombre al livello 12.0, AS |
| 272 Ludicolo |  | E |  |  | Ludicolo della cartuccia, box 13 posto 20; Ludicolo con origine RSE ORAS; Ludicolo ♂, origine RSE ORAS |
| 272 Ludicolo |  | AS |  |  | Ludicolo al livello 12.0, AS; Ludicolo ♀, origine RSE ORAS |
| 273 Seedot |  | E |  |  | Seedot della cartuccia, box 2 posto 22 |
| 274 Nuzleaf |  | E |  |  | Nuzleaf «DOTS» di KOBE/38726, E; Nuzleaf ♀, origine RSE ORAS |
| 274 Nuzleaf |  | OR |  |  | Nuzleaf al livello 7.0, OR |
| 275 Shiftry |  | E |  |  | Shiftry «DOTS» di KOBE/38726, E; Shiftry ♂, origine RSE ORAS |
| 275 Shiftry |  | OR |  |  | Shiftry al livello 7.0, OR |
| 276 Taillow |  | E |  |  | Taillow della cartuccia, box 13 posto 26 |
| 276 Taillow |  | qualunque | Dream Ball |  | Taillow in Dream Ball |
| 276 Taillow |  | qualunque | UC Ball |  | Taillow in UC Ball |
| 277 Swellow |  | E |  |  | Swellow della cartuccia, box 11 posto 14; Swellow con origine RSE ORAS |
| 279 Pelipper |  | E |  |  | Pelipper della cartuccia, box 7 posto 13; Pelipper con origine RSE ORAS |
| 279 Pelipper |  | E |  |  | Pelipper della cartuccia, box 12 posto 3 |
| 280 Ralts |  | E |  |  | Ralts della cartuccia, box 2 posto 23 |
| 280 Ralts |  | B, B2, W, W2 |  |  | Ralts «» di Yancy/10303, BWB2W2 |
| 280 Ralts |  | B, B2, W, W2 |  |  | Ralts «» di Curtis/54118, BWB2W2 |
| 281 Kirlia |  | B, B2, W, W2 |  |  | Kirlia «» di Yancy/10303, BWB2W2 |
| 281 Kirlia |  | B, B2, W, W2 |  |  | Kirlia «» di Curtis/54118, BWB2W2 |
| 281 Kirlia |  | X, Y |  |  | Kirlia «Ralts» di Diantha/37110, XY |
| 282 Gardevoir |  | E |  |  | Gardevoir della cartuccia, box 13 posto 7; Gardevoir con origine RSE ORAS |
| 282 Gardevoir |  | B, B2, W, W2 |  |  | Gardevoir «» di Yancy/10303, BWB2W2 |
| 282 Gardevoir |  | B, B2, W, W2 |  |  | Gardevoir «» di Curtis/54118, BWB2W2 |
| 282 Gardevoir |  | X, Y |  |  | Gardevoir «Ralts» di Diantha/37110, XY |
| 284 Masquerain |  | AS, OR |  |  | Masquerain al livello 21.0, ORAS |
| 285 Shroomish |  | E |  |  | Shroomish della cartuccia, box 13 posto 25; Shroomish con origine RSE ORAS |
| 286 Breloom |  | E |  |  | Breloom della cartuccia, box 1 posto 4; casella Breloom; Breloom con origine RSE ORAS |
| 286 Breloom |  | E |  |  | Breloom della cartuccia, box 14 posto 7 |
| 286 Breloom |  | D, P, Pt |  |  | Breloom «» di Hayley/01000, My Pokémon Ranch |
| 289 Slaking |  | AS, E, OR, R, S |  |  | Slaking con origine RSE ORAS |
| 292 Shedinja |  | E, R, S |  |  | Shedinja, Bronze, RSE: ★44: Baton Pass. |
| 294 Loudred |  | AS, OR |  |  | Loudred al livello 16.0, ORAS |
| 297 Hariyama |  | R, S |  |  | Hariyama «MAKIT» di ELYSSA/49562, RS |
| 297 Hariyama |  | AS, OR |  |  | Hariyama «Makit» di Darrell/30724, ORAS |
| 297 Hariyama |  | qualunque |  |  | Hariyama, Bronze, White 2: ★61: Pinwheel Forest. |
| 297 Hariyama |  | X, Y |  |  | Hariyama al livello 22.0, XY |
| 300 Skitty |  | qualunque | Dream Ball |  | Skitty in Dream Ball |
| 301 Delcatty |  | E |  |  | Delcatty della cartuccia, box 8 posto 28; Delcatty con origine RSE ORAS |
| 301 Delcatty |  | R, S |  |  | Delcatty «SKITIT» di DARRELL/02259, RS |
| 301 Delcatty |  | AS, OR |  |  | Delcatty «Skitit» di Elyssa/03239, ORAS |
| 302 Sableye |  | B, B2, W, W2 |  |  | Sableye «» di Curtis/54118, BWB2W2 |
| 303 Mawile |  | B, B2, W, W2 |  |  | Mawile «» di Yancy/10303, BWB2W2 |
| 306 Aggron |  | E |  |  | Aggron della cartuccia, box 13 posto 21; Aggron con origine RSE ORAS |
| 307 Meditite |  | AS, E, OR, R, S |  |  | Meditite con origine RSE ORAS; Meditite ♂, origine RSE ORAS |
| 307 Meditite |  | AS, E, OR, R, S |  |  | Meditite ♀, origine RSE ORAS |
| 308 Medicham |  | E |  |  | Medicham della cartuccia, box 7 posto 3; casella Medicham; Medicham con origine RSE ORAS; Medicham ♂, origine RSE ORAS |
| 308 Medicham |  | CXD |  |  | Medicham «» di DUKING/37149, XD: Gale of Darkness |
| 308 Medicham |  | AS, E, OR, R, S |  |  | Medicham, Bronze, Black 2: ★62: Pinwheel Forest.; Medicham ♀, origine RSE ORAS |
| 308 Medicham |  | AS, OR |  |  | Medicham al livello 34.0, ORAS |
| 310 Manectric |  | E |  |  | Manectric della cartuccia, box 7 posto 29; Manectric con origine RSE ORAS |
| 311 Plusle |  | CXD |  |  | Plusle «» di DUKING/37149, Colosseum |
| 312 Minun |  | E |  |  | Minun della cartuccia, box 11 posto 13 |
| 313 Volbeat |  | E |  |  | Volbeat della cartuccia, box 8 posto 3 |
| 314 Illumise |  | E |  |  | Illumise della cartuccia, box 8 posto 2; Illumise con origine RSE ORAS |
| 315 Roselia |  | E |  |  | Roselia della cartuccia, box 7 posto 4; Roselia con origine RSE ORAS; Roselia ♂, origine RSE ORAS |
| 315 Roselia |  | AS, E, OR, R, S |  |  | Roselia ♀, origine RSE ORAS |
| 316 Gulpin |  | AS, E, OR, R, S |  |  | Gulpin con origine RSE ORAS; Gulpin ♂, origine RSE ORAS |
| 316 Gulpin |  | AS, E, OR, R, S |  |  | Gulpin ♀, origine RSE ORAS |
| 317 Swalot |  | E |  |  | Swalot della cartuccia, box 8 posto 16; casella Swalot; Swalot con origine RSE ORAS; Swalot ♂, origine RSE ORAS |
| 317 Swalot |  | AS, E, OR, R, S |  |  | Swalot ♀, origine RSE ORAS |
| 318 Carvanha |  | AS, E, OR, R, S |  |  | Carvanha con origine RSE ORAS |
| 319 Sharpedo |  | E |  |  | Sharpedo della cartuccia, box 7 posto 19 |
| 319 Sharpedo |  | MN, SN |  |  | Sharpedo al livello 10.0, SM |
| 321 Wailord |  | E |  |  | Wailord della cartuccia, box 8 posto 1; casella Wailord; Wailord con origine RSE ORAS |
| 321 Wailord |  | D, P, Pt |  |  | Wailord «» di Hayley/01000, My Pokémon Ranch |
| 321 Wailord |  | MN, SN |  |  | Wailord al livello 10.0, SM |
| 322 Numel |  | AS, E, OR, R, S |  |  | Numel con origine RSE ORAS; Numel ♂, origine RSE ORAS |
| 322 Numel |  | AS, E, OR, R, S |  |  | Numel ♀, origine RSE ORAS |
| 323 Camerupt |  | E |  |  | Camerupt della cartuccia, box 8 posto 4; Camerupt ♀, origine RSE ORAS |
| 324 Torkoal |  | E |  |  | Torkoal della cartuccia, box 7 posto 20; casella Torkoal; Torkoal con origine RSE ORAS |
| 326 Grumpig |  | X, Y |  |  | Grumpig al livello 30.0, XY |
| 327 Spinda |  | qualunque | Minor Ball | sì | Spinda cromatico in Minor Ball, da qualunque gioco dalla terza alla settima generazione |
| 327 Spinda |  | qualunque | Safari Ball | sì | Spinda cromatico in Safari Ball, da HeartGold e SoulSilver |
| 327 Spinda |  | qualunque | Friend Ball | sì | Spinda cromatico in Friend Ball, da HeartGold e SoulSilver, Sole e Luna |
| 327 Spinda |  | qualunque | Premier Ball | sì | Spinda cromatico in Premier Ball, da qualunque gioco dalla terza alla settima generazione |
| 327 Spinda |  | E |  |  | Spinda della cartuccia, box 7 posto 15 |
| 327 Spinda |  | B, B2, W, W2 |  |  | Spinda «» di Yancy/10303, BWB2W2 |
| 327 Spinda |  | B, B2, W, W2 |  |  | Spinda «» di Curtis/54118, BWB2W2 |
| 327 Spinda |  | qualunque | Ultra Ball | sì | Spinda cromatico; Spinda in Ultra Ball |
| 327 Spinda |  | qualunque | Mega Ball |  | Spinda in Mega Ball |
| 327 Spinda |  | qualunque | Safari Ball |  | Spinda in Safari Ball |
| 327 Spinda |  | qualunque | Rete Ball |  | Spinda in Rete Ball |
| 327 Spinda |  | qualunque | Sub Ball |  | Spinda in Sub Ball |
| 327 Spinda |  | qualunque | Minor Ball |  | Spinda in Minor Ball |
| 327 Spinda |  | qualunque | Bis Ball |  | Spinda in Bis Ball |
| 327 Spinda |  | qualunque | Timer Ball |  | Spinda in Timer Ball |
| 327 Spinda |  | qualunque | Chic Ball |  | Spinda in Chic Ball |
| 327 Spinda |  | qualunque | Premier Ball |  | Spinda in Premier Ball |
| 327 Spinda |  | qualunque | Scuro Ball |  | Spinda in Scuro Ball |
| 327 Spinda |  | qualunque | Cura Ball |  | Spinda in Cura Ball |
| 327 Spinda |  | qualunque | Velox Ball |  | Spinda in Velox Ball |
| 327 Spinda |  | qualunque | Rapid Ball |  | Spinda in Rapid Ball |
| 327 Spinda |  | qualunque | Level Ball |  | Spinda in Level Ball |
| 327 Spinda |  | qualunque | Esca Ball |  | Spinda in Esca Ball |
| 327 Spinda |  | qualunque | Peso Ball |  | Spinda in Peso Ball |
| 327 Spinda |  | qualunque | Love Ball |  | Spinda in Love Ball |
| 327 Spinda |  | qualunque | Friend Ball |  | Spinda in Friend Ball |
| 327 Spinda |  | qualunque | Luna Ball |  | Spinda in Luna Ball |
| 327 Spinda |  | qualunque | Dream Ball |  | Spinda in Dream Ball |
| 327 Spinda |  | qualunque | UC Ball |  | Spinda in UC Ball |
| 329 Vibrava |  | AS, E, OR, R, S |  |  | Vibrava con origine RSE ORAS |
| 330 Flygon |  | E |  |  | Flygon della cartuccia, box 11 posto 19; Flygon con origine RSE ORAS |
| 332 Cacturne |  | AS, E, OR, R, S |  |  | Cacturne ♂, origine RSE ORAS |
| 333 Swablu |  | AS, E, OR, R, S |  |  | Swablu con origine RSE ORAS |
| 334 Altaria |  | E |  |  | Altaria della cartuccia, box 8 posto 10; Altaria con origine RSE ORAS |
| 334 Altaria |  | E |  |  | Altaria della cartuccia, box 11 posto 20 |
| 335 Zangoose |  | E |  |  | Zangoose della cartuccia, box 6 posto 21; Zangoose con origine RSE ORAS |
| 335 Zangoose |  | E |  |  | Zangoose della cartuccia, box 6 posto 22 |
| 335 Zangoose |  | E |  |  | Zangoose della cartuccia, box 6 posto 23 |
| 336 Seviper |  | E |  |  | Seviper della cartuccia, box 11 posto 21 |
| 337 Lunatone |  | E |  |  | Lunatone della cartuccia, box 9 posto 25; Lunatone con origine RSE ORAS |
| 338 Solrock |  | E |  |  | Solrock della cartuccia, box 7 posto 25 |
| 338 Solrock |  | E |  |  | Solrock della cartuccia, box 8 posto 12 |
| 340 Whiscash |  | E |  |  | Whiscash della cartuccia, box 8 posto 13; Whiscash con origine RSE ORAS |
| 340 Whiscash |  | UM, US |  |  | Whiscash «Babo» di Yuichi/590916, USUM |
| 340 Whiscash |  | HG, SS |  |  | Whiscash al livello 10.0, HGSS |
| 342 Crawdaunt |  | E |  |  | Crawdaunt della cartuccia, box 4 posto 8; casella Crawdaunt; Crawdaunt con origine RSE ORAS |
| 342 Crawdaunt |  | UM, US |  |  | Crawdaunt al livello 10.0, USUM |
| 343 Baltoy |  | E |  |  | Baltoy della cartuccia, box 4 posto 9; Baltoy con origine RSE ORAS |
| 346 Cradily |  | E |  |  | Cradily della cartuccia, box 4 posto 15; casella Cradily; Cradily con origine RSE ORAS |
| 348 Armaldo |  | E |  |  | Armaldo della cartuccia, box 13 posto 5; casella Armaldo; Armaldo con origine RSE ORAS |
| 349 Feebas |  | E |  |  | Feebas della cartuccia, box 10 posto 1 |
| 349 Feebas |  | E, R, S |  |  | Feebas, Gold, RSE: ★4: Route 119. |
| 349 Feebas |  | D, P, Pt |  |  | Feebas, Bronze, DPPt: ★52: Mt. Coronet. |
| 350 Milotic |  | AS, E, OR, R, S |  |  | Milotic con origine RSE ORAS; Milotic ♂, origine RSE ORAS |
| 350 Milotic |  | AS, E, OR, R, S |  |  | Milotic ♀, origine RSE ORAS |
| 351 Castform |  | AS, OR |  |  | Castform, ORAS: Given at the Weather Institute. |
| 351 Castform |  | qualunque | Dream Ball |  | Castform in Dream Ball |
| 351 Castform |  | qualunque | UC Ball |  | Castform in UC Ball |
| 352 Kecleon |  | E |  |  | Kecleon della cartuccia, box 8 posto 5 |
| 352 Kecleon |  | AS, OR |  |  | Kecleon, ORAS: 1) Route 119;
2) Route 120;
3) Lavaridge Town (after beating Groudon/Kyogre);
4) |
| 354 Banette |  | E |  |  | Banette della cartuccia, box 8 posto 15 |
| 356 Dusclops |  | E |  |  | Dusclops della cartuccia, box 12 posto 6; casella Dusclops; Dusclops con origine RSE ORAS |
| 356 Dusclops |  | E |  |  | Dusclops della cartuccia, box 12 posto 28 |
| 356 Dusclops |  | Pt |  |  | Dusclops al livello 16.0, Pt |
| 357 Tropius |  | E |  |  | Tropius della cartuccia, box 8 posto 19; Tropius con origine RSE ORAS |
| 359 Absol |  | E |  |  | Absol della cartuccia, box 11 posto 6 |
| 359 Absol |  | E |  |  | Absol della cartuccia, box 11 posto 22 |
| 360 Wynaut |  | D, P, Pt |  |  | Wynaut «» di Hayley/01000, My Pokémon Ranch |
| 360 Wynaut |  | AS, OR |  |  | Wynaut, ORAS: Egg, Lavaridge Town. |
| 360 Wynaut |  | E, R, S |  |  | Wynaut, Platinum, RSE: ★5: Mirage Island. |
| 361 Snorunt |  | E, R, S |  |  | Snorunt, Bronze, RSE: ★45: Shoal Cave.; Snorunt con origine RSE ORAS |
| 362 Glalie |  | AS, OR |  |  | Glalie «» di Orlando/Random ID, ORAS |
| 362 Glalie |  | AS, OR |  |  | Glalie, Gold, ORAS Demo: ★34 |
| 363 Spheal |  | AS, E, OR, R, S |  |  | Spheal con origine RSE ORAS |
| 365 Walrein |  | E |  |  | Walrein della cartuccia, box 4 posto 29; Walrein con origine RSE ORAS |
| 365 Walrein |  | E |  |  | Walrein della cartuccia, box 4 posto 30 |
| 366 Clamperl |  | qualunque | Dream Ball |  | Clamperl in Dream Ball |
| 366 Clamperl |  | qualunque | UC Ball |  | Clamperl in UC Ball |
| 369 Relicanth |  | AS, E, OR, R, S |  |  | Relicanth ♀, origine RSE ORAS |
| 371 Bagon |  | HG, SS |  |  | Bagon, Silver, HGSS: ★7: Safari Zone. |
| 372 Shelgon |  | MN, SN, UM, US |  |  | Shelgon al livello 15.0, SMUSUM |
| 373 Salamence |  | E |  |  | Salamence della cartuccia, box 1 posto 2; Salamence con origine RSE ORAS |
| 373 Salamence |  | MN, SN, UM, US |  |  | Salamence, Platinum, SMUSUM: ★13: Route 3. Caught as Salamence. |
| 373 Salamence |  | MN, SN, UM, US |  |  | Salamence al livello 9.0, SMUSUM |
| 374 Beldum |  | AS, OR |  |  | Beldum, ORAS: Mossdeep City, in Steven's house, after the Delta Episode. |
| 375 Metang |  | HG, SS |  |  | Metang «Iron» di Steven/23478, HGSS |
| 375 Metang |  | HG, SS |  |  | Metang, Silver, HGSS: ★8: Safari Zone. Caught as Metang. |
| 376 Metagross |  | E |  |  | Metagross della cartuccia, box 1 posto 16; Metagross con origine RSE ORAS |
| 376 Metagross |  | E |  |  | Metagross della cartuccia, box 2 posto 3 |
| 376 Metagross |  | E |  |  | Metagross della cartuccia, box 6 posto 2 |
| 376 Metagross |  | E |  |  | Metagross della cartuccia, box 13 posto 9 |
| 376 Metagross |  | HG, SS |  |  | Metagross «Iron» di Steven/23478, HGSS |
| 377 Regirock |  | E |  |  | Regirock della cartuccia, box 3 posto 1 |
| 377 Regirock |  | B2, W2 |  |  | Regirock, Bronze, B2W2: ★63 |
| 378 Regice |  | E |  |  | Regice della cartuccia, box 3 posto 3 |
| 378 Regice |  | qualunque |  |  | Regice, Bronze, Black 2: ★63 |
| 379 Registeel |  | E |  |  | Registeel della cartuccia, box 3 posto 2 |
| 379 Registeel |  | qualunque |  |  | Registeel, Bronze, White 2: ★63 |
| 380 Latias |  | E |  |  | Latias della cartuccia, box 1 posto 23 |
| 380 Latias |  | E |  |  | Latias, Platinum, Ruby, Emerald: ★6: Southern Island. |
| 380 Latias |  | qualunque |  |  | Latias, Bronze, Omega Ruby: ★88: Southern Island. |
| 381 Latios |  | E |  |  | Latios della cartuccia, box 2 posto 5 |
| 381 Latios |  | E |  |  | Latios della cartuccia, box 14 posto 3 |
| 381 Latios |  | E |  |  | Latios della cartuccia, box 14 posto 4 |
| 381 Latios |  | E |  |  | Latios della cartuccia, box 14 posto 5 |
| 381 Latios |  | E |  |  | Latios, Platinum, Sapphire, Emerald: ★6: Southern Island. |
| 381 Latios |  | qualunque |  |  | Latios, Bronze, Alpha Sapphire: ★88: Southern Island. |
| 382 Kyogre |  | E |  |  | Kyogre della cartuccia, box 6 posto 3 |
| 382 Kyogre |  | AS, OR |  |  | Kyogre, per «Register Groudon and Kyogre from Pokémon Omega Ruby or Pokémon Alpha Sapphire»; Kyogre, per «Register Kyogre from Pokémon Omega Ruby or Pokémon Alpha Sapphire» |
| 383 Groudon |  | AS, OR |  |  | Groudon, per «Register Groudon and Kyogre from Pokémon Omega Ruby or Pokémon Alpha Sapphire»; Groudon, per «Register Groudon from Pokémon Omega Ruby or Pokémon Alpha Sapphire» |
| 384 Rayquaza |  | E |  |  | Rayquaza della cartuccia, box 2 posto 2; Rayquaza, per «Register Rayquaza from Pokémon Ruby, Pokémon Sapphire, or Pokémon Emerald» |
| 384 Rayquaza |  | E |  |  | Rayquaza della cartuccia, box 6 posto 8 |
| 384 Rayquaza |  | HG, SS |  |  | Rayquaza, Platinum, HGSS: ★8 |
| 385 Jirachi |  | CXD |  |  | Jirachi «Wishmaker Jirachi» di WISHMKR/20043, Colosseum |
| 385 Jirachi |  | qualunque |  |  | Jirachi «» di CHANNEL/40122, Channel |
| 385 Jirachi |  | qualunque |  |  | Jirachi, Gold, Channel: ★22 |
| 385 Jirachi |  | CXD |  |  | Jirachi, Gold, Colosseum Bonus Disc: ★25 |
| 386 Deoxys |  | qualunque |  |  | Deoxys Attack Forme, origine Any |
| 386 Deoxys |  | qualunque |  |  | Deoxys Defense Forme, origine Any |
| 386 Deoxys |  | qualunque |  |  | Deoxys Speed Forme, origine Any |
| 386 Deoxys |  | AS, OR |  |  | Deoxys, Gold, ORAS: ★11 |
| 386 Deoxys |  | qualunque |  | sì | Deoxys cromatico, dal video yyIa9611uZk, legalità da verificare con la libreria |
| 387 Turtwig |  | D, P, Pt |  |  | casella Turtwig; Turtwig, per «Register Turtwig, Chimchar and Piplup from Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum» |
| 388 Grotle |  | qualunque |  |  | casella Grotle |
| 391 Monferno |  | qualunque |  |  | casella Monferno |
| 393 Piplup |  | D, P, Pt |  |  | Piplup, per «Register Turtwig, Chimchar and Piplup from Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum» |
| 394 Prinplup |  | qualunque |  |  | casella Prinplup |
| 396 Starly |  | qualunque |  |  | casella Starly |
| 397 Staravia |  | D, P |  |  | Staravia al livello 4.0, DP |
| 398 Staraptor |  | D, P, Pt |  |  | Staraptor «» di Hayley/01000, My Pokémon Ranch; casella Staraptor |
| 399 Bidoof |  | qualunque | Safari Ball |  | Bidoof in Safari Ball |
| 399 Bidoof |  | qualunque | Dream Ball |  | Bidoof in Dream Ball |
| 400 Bibarel |  | D, P |  |  | Bibarel al livello 4.0, DP |
| 402 Kricketune |  | qualunque |  |  | casella Kricketune |
| 404 Luxio |  | qualunque |  |  | casella Luxio |
| 405 Luxray |  | qualunque |  |  | casella Luxray |
| 407 Roserade |  | E, R, S |  |  | Roserade, Bronze, RSE: ★46; casella Roserade |
| 408 Cranidos |  | B, B2, W, W2 |  |  | Cranidos «» di Curtis/54118, BWB2W2 |
| 408 Cranidos |  | D, P, Pt |  |  | Cranidos, Silver, DPPt: ★5: Fossil obtained in Platinum. |
| 409 Rampardos |  | B, B2, W, W2 |  |  | Rampardos «» di Curtis/54118, BWB2W2; casella Rampardos |
| 410 Shieldon |  | B, B2, W, W2 |  |  | Shieldon «» di Yancy/10303, BWB2W2 |
| 410 Shieldon |  | D, P, Pt |  |  | Shieldon, Silver, DPPt: ★5: Fossil obtained in Platinum. |
| 411 Bastiodon |  | B, B2, W, W2 |  |  | Bastiodon «» di Yancy/10303, BWB2W2; casella Bastiodon |
| 412 Burmy |  | qualunque | Dream Ball |  | casella Burmy; Burmy in Dream Ball |
| 412 Burmy | Sabbia | qualunque | Dream Ball |  | casella Burmy Sabbia; Burmy Sabbia in Dream Ball |
| 412 Burmy | Scarti | qualunque | Dream Ball |  | casella Burmy Scarti; Burmy Scarti in Dream Ball |
| 413 Wormadam |  | qualunque |  |  | casella Wormadam |
| 413 Wormadam | Sabbia | qualunque |  |  | casella Wormadam Sabbia |
| 413 Wormadam | Scarti | qualunque |  |  | casella Wormadam Scarti |
| 414 Mothim |  | qualunque |  |  | casella Mothim |
| 416 Vespiquen |  | D, P, Pt |  |  | Vespiquen «» di Hayley/01000, My Pokémon Ranch; casella Vespiquen |
| 419 Floatzel |  | B2, W2 |  |  | Floatzel al livello 10.0, B2W2; casella Floatzel |
| 420 Cherubi |  | qualunque |  |  | casella Cherubi |
| 421 Cherrim |  | qualunque |  |  | casella Cherrim |
| 422 Shellos |  | B, B2, W, W2 |  |  | Shellos «» di Yancy/10303, BWB2W2 |
| 422 Shellos |  | B, B2, W, W2 |  |  | Shellos «» di Curtis/54118, BWB2W2 |
| 423 Gastrodon |  | D, P, Pt |  |  | Gastrodon «» di Hayley/01000, My Pokémon Ranch |
| 423 Gastrodon |  | B, B2, W, W2 |  |  | Gastrodon «» di Yancy/10303, BWB2W2 |
| 423 Gastrodon |  | B, B2, W, W2 |  |  | Gastrodon «» di Curtis/54118, BWB2W2 |
| 423 Gastrodon |  | UM, US |  |  | Gastrodon «Solle» di Kumu/610503, USUM |
| 423 Gastrodon | Est | qualunque |  |  | casella Gastrodon Est |
| 424 Ambipom |  | B, B2, W, W2 |  |  | Ambipom «Ambidexter» di Diana/17074, BWB2W2; casella Ambipom |
| 424 Ambipom |  | C, GD, SI |  |  | Ambipom, Bronze, GSC: ★32 |
| 425 Drifloon |  | D, P, Pt |  |  | Drifloon, DPPt: Interactable, 	Valley Windworks, every Friday. |
| 425 Drifloon |  | UM, US |  |  | Drifloon, USUM: At night, if you go to the Trainer School you will see a girl and her Drifloon.  |
| 426 Drifblim |  | MN, SN |  |  | Drifblim al livello 11.0, SM; casella Drifblim |
| 428 Lopunny |  | D, P, Pt |  |  | Lopunny «» di Hayley/01000, My Pokémon Ranch; casella Lopunny |
| 429 Mismagius |  | C, GD, SI |  |  | Mismagius, Bronze, GSC: ★33; casella Mismagius |
| 429 Mismagius |  | MN, SN |  |  | Mismagius, Silver, SM: ★11: Poké Pelago. |
| 430 Honchkrow |  | C, GD, SI |  |  | Honchkrow, Bronze, GSC: ★34 |
| 430 Honchkrow |  | UM, US |  |  | Honchkrow, Silver, USUM: ★15: Poké Pelago. |
| 431 Glameow |  | B2, W2 |  |  | Glameow, B2W2: Interactable, Through the Funfest Mission "Quiet Hidden Grottoes!", in White 2.; casella Glameow |
| 431 Glameow |  | qualunque | Dream Ball |  | Glameow in Dream Ball |
| 432 Purugly |  | qualunque |  |  | casella Purugly |
| 434 Stunky |  | B2, W2 |  |  | Stunky, B2W2: Interactable, Through the Funfest Mission "Noisy Hidden Grottoes!", in Black 2.; casella Stunky |
| 435 Skuntank |  | qualunque |  |  | casella Skuntank |
| 437 Bronzong |  | qualunque |  |  | casella Bronzong |
| 440 Happiny |  | D, P |  |  | Happiny, DP: Egg Given by a Hiker in Hearthome City. |
| 440 Happiny |  | B2, W2 |  |  | Happiny, B2W2: Egg, Nacrene City gate. |
| 441 Chatot |  | qualunque | Dream Ball |  | Chatot in Dream Ball |
| 442 Spiritomb |  | B, B2, W, W2 |  |  | Spiritomb «» di Yancy/10303, BWB2W2 |
| 442 Spiritomb |  | B, B2, W, W2 |  |  | Spiritomb «» di Curtis/54118, BWB2W2 |
| 442 Spiritomb |  | AS, OR |  |  | Spiritomb, ORAS: After you have confronted Primal Groudon/Kyogre, when you get to Room 4 in Sea M |
| 442 Spiritomb |  | qualunque |  |  | Spiritomb, Silver, Pokéwalker: ★9 |
| 442 Spiritomb |  | D, P, Pt |  |  | Spiritomb, Gold, DPPt: ★5: Route 209. |
| 443 Gible |  | qualunque |  |  | Gible, Gold, Black 2: ★9: Flocessy Town.; casella Gible |
| 444 Gabite |  | qualunque |  |  | casella Gabite |
| 446 Munchlax |  | D, P, Pt |  |  | Munchlax, Platinum, DPPt: ★7: Honey Tree. |
| 449 Hippopotas |  | qualunque |  |  | casella Hippopotas |
| 450 Hippowdon |  | qualunque |  |  | casella Hippowdon |
| 451 Skorupi |  | qualunque |  |  | casella Skorupi |
| 452 Drapion |  | qualunque |  |  | casella Drapion |
| 454 Toxicroak |  | D, P, Pt |  |  | Toxicroak «» di Hayley/01000, My Pokémon Ranch; casella Toxicroak |
| 455 Carnivine |  | qualunque | Safari Ball |  | casella Carnivine; Carnivine in Safari Ball |
| 455 Carnivine |  | qualunque | Dream Ball |  | Carnivine in Dream Ball |
| 457 Lumineon |  | D, P, Pt |  |  | Lumineon «» di Hayley/01000, My Pokémon Ranch; casella Lumineon |
| 458 Mantyke |  | qualunque |  |  | casella Mantyke |
| 460 Abomasnow |  | D, P, Pt |  |  | Abomasnow «» di Hayley/01000, My Pokémon Ranch; casella Abomasnow |
| 461 Weavile |  | C, GD, SI |  |  | Weavile, Bronze, GSC: ★35 |
| 462 Magnezone |  | C |  |  | Magnezone «MAGGIE» di FOREST/50082, C + Gen 4 & Up; casella Magnezone |
| 462 Magnezone |  | HG, SS |  |  | Magnezone «Maggie» di Lorenzo/50082, HGSS |
| 462 Magnezone |  | BU, GN, RD, YW |  |  | Magnezone, Bronze, RBY: ★17 |
| 462 Magnezone |  | BU, C, GN, RD |  |  | Magnezone al livello 5.0, C+RB+SwSh-IoA |
| 463 Lickilicky |  | BU, GN, RD |  |  | Lickilicky «MARC» di TRAINER/random ID, RB + Gen4 & up; casella Lickilicky |
| 463 Lickilicky |  | FR, LG |  |  | Lickilicky «MARC» di HADEN/01239, FRLG |
| 463 Lickilicky |  | D, P, Pt |  |  | Lickilicky «» di Hayley/01000, My Pokémon Ranch |
| 463 Lickilicky |  | BU, GN, RD, YW |  |  | Lickilicky, Bronze, RBY: ★18 |
| 464 Rhyperior |  | YW |  |  | Rhyperior «BUFFY» di TRAINER/random ID, Yellow + Gen 4 & Up; casella Rhyperior |
| 464 Rhyperior |  | GD, SI |  |  | Rhyperior «DON» di EMY/00283, GS + Gen 4 & Up |
| 464 Rhyperior |  | HG, SS |  |  | Rhyperior «Hornlette» di Brock/06845, HGSS |
| 464 Rhyperior |  | B, B2, W, W2 |  |  | Rhyperior «» di Yancy/10303, BWB2W2 |
| 464 Rhyperior |  | B, B2, W, W2 |  |  | Rhyperior «» di Curtis/54118, BWB2W2 |
| 464 Rhyperior |  | BU, GN, RD, YW |  |  | Rhyperior, Bronze, RBY: ★19 |
| 464 Rhyperior |  | GD, SI, UM, US |  |  | Rhyperior al livello 10.0, GS + USUM |
| 465 Tangrowth |  | BU, GN, RD |  |  | Tangrowth «CRINKLES» di TRAINER/random ID, RB + Gen4 & up |
| 465 Tangrowth |  | FR, LG |  |  | Tangrowth «TANGENY» di NORMA/60042, FRLG |
| 465 Tangrowth |  | D, P, Pt |  |  | Tangrowth «» di Hayley/01000, My Pokémon Ranch |
| 465 Tangrowth |  | B, B2, W, W2 |  |  | Tangrowth «Tangles» di Slick/27658, BWB2W2 |
| 465 Tangrowth |  | BU, GN, RD, YW |  |  | Tangrowth, Bronze, RBY: ★20 |
| 466 Electivire |  | CXD |  |  | Electivire «ZAPRONG» di HORDEL/41400, XD: Gale of Darkness |
| 466 Electivire |  | D, P, Pt |  |  | Electivire «» di PKTOPIA/06257, Battle Revolution |
| 466 Electivire |  | BU, GN, RD, YW |  |  | Electivire, Bronze, RBY: ★21 |
| 466 Electivire |  | D, P, Pt |  |  | Electivire, Silver, Battle Revolution: ★45 |
| 466 Electivire |  | D, P, Pt |  |  | Electivire al livello 15.0, DPPt  |
| 467 Magmortar |  | D, P, Pt |  |  | Magmortar «» di PKTOPIA/06257, Battle Revolution |
| 467 Magmortar |  | BU, GN, RD, YW |  |  | Magmortar, Bronze, RBY: ★22 |
| 467 Magmortar |  | D, P, Pt |  |  | Magmortar, Silver, Battle Revolution: ★46 |
| 467 Magmortar |  | D, P, Pt |  |  | Magmortar al livello 14.0, DPPt  |
| 468 Togekiss |  | B, B2, W, W2 |  |  | Togekiss «» di Yancy/10303, BWB2W2; casella Togekiss |
| 468 Togekiss |  | B, B2, W, W2 |  |  | Togekiss «» di Curtis/54118, BWB2W2 |
| 468 Togekiss |  | C, GD, SI |  |  | Togekiss, Bronze, GSC: ★36 |
| 469 Yanmega |  | D, P, Pt |  |  | Yanmega «» di Hayley/01000, My Pokémon Ranch; casella Yanmega |
| 469 Yanmega |  | C, GD, SI |  |  | Yanmega, Bronze, GSC: ★37 |
| 470 Leafeon |  | D, P, Pt |  |  | Leafeon «» di Hayley/01000, My Pokémon Ranch |
| 470 Leafeon |  | X, Y |  |  | Leafeon «Stevie» di Elena/29294, XY |
| 470 Leafeon |  | BU, GN, RD, YW |  |  | Leafeon, Bronze, RBY: ★23 |
| 471 Glaceon |  | D, P, Pt |  |  | Glaceon «» di Hayley/01000, My Pokémon Ranch |
| 471 Glaceon |  | X, Y |  |  | Glaceon «Stevie» di Elena/29294, XY |
| 471 Glaceon |  | BU, GN, RD, YW |  |  | Glaceon, Bronze, RBY: ★24 |
| 472 Gliscor |  | C, GD, SI |  |  | Gliscor, Bronze, GSC: ★38; casella Gliscor |
| 473 Mamoswine |  | C, GD, SI |  |  | Mamoswine, Bronze, GSC: ★39 |
| 474 Porygon-Z |  | BU, GN, RD, YW |  |  | Porygon-Z, Bronze, RBY: ★25; casella Porygon-Z |
| 475 Gallade |  | B, B2, W, W2 |  |  | Gallade «» di , BWB2W2; casella Gallade |
| 475 Gallade |  | B, B2, W, W2 |  |  | Gallade «» di , BWB2W2 |
| 475 Gallade |  | E, R, S |  |  | Gallade, Bronze, RSE: ★47 |
| 476 Probopass |  | E, R, S |  |  | Probopass, Bronze, RSE: ★48; casella Probopass |
| 477 Dusknoir |  | E, R, S |  |  | Dusknoir, Bronze, RSE: ★49; casella Dusknoir |
| 477 Dusknoir |  | Pt |  |  | Dusknoir al livello 16.0, Pt BDSP |
| 478 Froslass |  | E, R, S |  |  | Froslass, Bronze, RSE: ★50; casella Froslass |
| 479 Rotom |  | D, P, Pt |  |  | Rotom, DPPt: Old Chateau, after beating the Elite 4. |
| 479 Rotom | Calore | qualunque |  |  | casella Rotom Calore |
| 479 Rotom | Lavaggio | qualunque |  |  | casella Rotom Lavaggio |
| 479 Rotom | Gelo | qualunque |  |  | casella Rotom Gelo |
| 479 Rotom | Vortice | qualunque |  |  | casella Rotom Vortice |
| 479 Rotom | Taglio | qualunque |  |  | casella Rotom Taglio |
| 480 Uxie |  | qualunque |  |  | casella Uxie |
| 481 Mesprit |  | qualunque |  |  | casella Mesprit |
| 482 Azelf |  | qualunque |  |  | casella Azelf |
| 483 Dialga |  | HG, SS |  |  | Dialga, HGSS: Sinjoh Ruins. Requires having Arceus in party to access the area. The Dialga/Pal |
| 483 Dialga |  | B2, W2 |  |  | Dialga, Silver, Dream Radar: ★49 |
| 483 Dialga |  | D, P, Pt |  |  | Dialga, per «Register Dialga from Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum!»; Dialga, per «Register Dialga, Palkia and Giratina from the Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum» |
| 484 Palkia |  | HG, SS |  |  | Palkia, HGSS: Sinjoh Ruins. Requires having Arceus in party to access the area. The Dialga/Pal |
| 484 Palkia |  | B2, W2 |  |  | Palkia, Silver, Dream Radar: ★50 |
| 484 Palkia |  | D, P, Pt |  |  | Palkia, per «Register Palkia from Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum»; Palkia, per «Register Dialga, Palkia and Giratina from the Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum» |
| 486 Regigigas |  | qualunque |  |  | Regigigas, Bronze, Platinum: ★53 |
| 487 Giratina |  | HG, SS |  |  | Giratina, HGSS: Sinjoh Ruins. Requires having Arceus in party to access the area. The Dialga/Pal |
| 487 Giratina |  | B2, W2 |  |  | Giratina, Silver, Dream Radar: ★51 |
| 487 Giratina |  | D, P, Pt |  |  | Giratina, per «Register Giratina from Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum!»; Giratina, per «Register Dialga, Palkia and Giratina from the Pokémon Diamond, Pokémon Pearl, or Pokémon Platinum» |
| 489 Phione |  | D, P, Pt |  |  | Phione, Gold, My Pokémon Ranch: ★29 |
| 490 Manaphy |  | qualunque |  |  | Manaphy, Platinum, Ranger Series: ★20 |
| 490 Manaphy |  | qualunque |  | sì | Manaphy cromatico, dal video yyIa9611uZk, legalità da verificare con la libreria |
| 491 Darkrai |  | qualunque |  | sì | Darkrai cromatico, dal video yyIa9611uZk, legalità da verificare con la libreria |
| 494 Victini |  | qualunque | Bis Ball |  | Victini in Bis Ball, da Nero e Bianco |
| 494 Victini |  | qualunque | Cura Ball |  | Victini in Cura Ball, da Nero e Bianco |
| 496 Servine |  | B, B2, W, W2 |  |  | casella Servine; Servine con origine BWB2W2 |
| 498 Tepig |  | B, B2, W, W2 |  |  | casella Tepig; Tepig con origine BWB2W2 |
| 499 Pignite |  | B, B2, W, W2 |  |  | casella Pignite; Pignite con origine BWB2W2 |
| 501 Oshawott |  | B, B2, W, W2 |  |  | casella Oshawott; Oshawott con origine BWB2W2 |
| 502 Dewott |  | B, B2, W, W2 |  |  | casella Dewott; Dewott con origine BWB2W2 |
| 503 Samurott |  | B, B2, W, W2 |  |  | Samurott, Bronze, BWB2W2: ★64: Hisuian Form. |
| 504 Patrat |  | B, B2, W, W2 |  |  | casella Patrat; Patrat con origine BWB2W2 |
| 505 Watchog |  | B, B2, W, W2 |  |  | casella Watchog; Watchog con origine BWB2W2 |
| 506 Lillipup |  | B, B2, W, W2 |  |  | casella Lillipup; Lillipup con origine BWB2W2 |
| 507 Herdier |  | B2, W2 |  |  | Herdier al livello 10.0, B2W2; casella Herdier; Herdier con origine BWB2W2 |
| 508 Stoutland |  | B, B2, W, W2 |  |  | casella Stoutland; Stoutland con origine BWB2W2 |
| 509 Purrloin |  | B, B2, W, W2 |  |  | Purrloin «» di N/00002, BWB2W2; casella Purrloin; Purrloin con origine BWB2W2 |
| 509 Purrloin |  | B2, W2 |  |  | Purrloin, Bronze, B2W2: ★65: N's. |
| 510 Liepard |  | B, B2, W, W2 |  |  | Liepard «» di N/00002, BWB2W2 |
| 512 Simisage |  | B, B2, W, W2 |  |  | casella Simisage; Simisage con origine BWB2W2 |
| 513 Pansear |  | B, W |  |  | Pansear, BW: Dreamyard. Get type which is weak against your starter.; casella Pansear; Pansear con origine BWB2W2 |
| 514 Simisear |  | B, B2, W, W2 |  |  | Simisear con origine BWB2W2 |
| 515 Panpour |  | B, W |  |  | Panpour, BW: Dreamyard. Get type which is weak against your starter.; casella Panpour; Panpour con origine BWB2W2 |
| 516 Simipour |  | B, B2, W, W2 |  |  | casella Simipour; Simipour con origine BWB2W2 |
| 518 Musharna |  | B, W |  |  | Musharna, BW: Interactable, Postgame, Dreamyard.; casella Musharna; Musharna con origine BWB2W2 |
| 519 Pidove |  | B, B2, W, W2 |  |  | Pidove «» di N/00002, BWB2W2 |
| 519 Pidove |  | B2, W2 |  |  | Pidove, Bronze, B2W2: ★66: N's. |
| 520 Tranquill |  | B, B2, W, W2 |  |  | Tranquill «» di N/00002, BWB2W2; casella Tranquill; Tranquill con origine BWB2W2 |
| 521 Unfezant |  | B, B2, W, W2 |  |  | Unfezant «» di N/00002, BWB2W2; casella Unfezant; Unfezant con origine BWB2W2; Unfezant ♂, origine BWB2W2 |
| 521 Unfezant |  | B, B2, W, W2 |  |  | Unfezant ♀, origine BWB2W2 |
| 522 Blitzle |  | B, B2, W, W2 |  |  | casella Blitzle; Blitzle con origine BWB2W2 |
| 523 Zebstrika |  | B, B2, W, W2 |  |  | casella Zebstrika; Zebstrika con origine BWB2W2 |
| 524 Roggenrola |  | B, B2, W, W2 |  |  | casella Roggenrola; Roggenrola con origine BWB2W2 |
| 525 Boldore |  | B, B2, W, W2 |  |  | Boldore «» di N/00002, BWB2W2; casella Boldore; Boldore con origine BWB2W2 |
| 525 Boldore |  | B2, W2 |  |  | Boldore, Bronze, B2W2: ★67: N's. |
| 526 Gigalith |  | B, B2, W, W2 |  |  | Gigalith «» di Manny/11195, BWB2W2; casella Gigalith; Gigalith con origine BWB2W2 |
| 526 Gigalith |  | B, B2, W, W2 |  |  | Gigalith «» di N/00002, BWB2W2 |
| 527 Woobat |  | B, B2, W, W2 |  |  | Woobat «» di N/00002, BWB2W2; casella Woobat; Woobat con origine BWB2W2 |
| 527 Woobat |  | B2, W2 |  |  | Woobat, Bronze, B2W2: ★68: N's. |
| 528 Swoobat |  | B, B2, W, W2 |  |  | Swoobat «» di N/00002, BWB2W2; casella Swoobat; Swoobat con origine BWB2W2 |
| 529 Drilbur |  | B, B2, W, W2 |  |  | casella Drilbur; Drilbur con origine BWB2W2 |
| 530 Excadrill |  | B, B2, W, W2 |  |  | casella Excadrill; Excadrill con origine BWB2W2 |
| 532 Timburr |  | B, B2, W, W2 |  |  | Timburr «» di N/00002, BWB2W2; casella Timburr; Timburr con origine BWB2W2 |
| 532 Timburr |  | B2, W2 |  |  | Timburr, Bronze, B2W2: ★69: N's. |
| 533 Gurdurr |  | B, B2, W, W2 |  |  | Gurdurr «» di N/00002, BWB2W2; casella Gurdurr; Gurdurr con origine BWB2W2 |
| 534 Conkeldurr |  | B, B2, W, W2 |  |  | Conkeldurr «» di N/00002, BWB2W2; casella Conkeldurr; Conkeldurr con origine BWB2W2 |
| 535 Tympole |  | B, B2, W, W2 |  |  | Tympole «» di N/00002, BWB2W2; casella Tympole; Tympole con origine BWB2W2 |
| 535 Tympole |  | B2, W2 |  |  | Tympole, Bronze, B2W2: ★70: N's. |
| 536 Palpitoad |  | B, B2, W, W2 |  |  | Palpitoad «» di N/00002, BWB2W2; casella Palpitoad; Palpitoad con origine BWB2W2 |
| 537 Seismitoad |  | B, B2, W, W2 |  |  | Seismitoad «» di N/00002, BWB2W2; casella Seismitoad; Seismitoad con origine BWB2W2 |
| 537 Seismitoad |  | B, W |  |  | Seismitoad al livello 15.0, BW |
| 538 Throh |  | B, B2, W, W2 |  |  | casella Throh; Throh con origine BWB2W2 |
| 539 Sawk |  | B, B2, W, W2 |  |  | casella Sawk; Sawk con origine BWB2W2 |
| 540 Sewaddle |  | B, B2, W, W2 |  |  | casella Sewaddle; Sewaddle con origine BWB2W2 |
| 541 Swadloon |  | B, B2, W, W2 |  |  | casella Swadloon; Swadloon con origine BWB2W2 |
| 542 Leavanny |  | B2, W2 |  |  | Leavanny al livello 20.0, B2W2; casella Leavanny; Leavanny con origine BWB2W2 |
| 543 Venipede |  | B, B2, W, W2 |  |  | casella Venipede; Venipede con origine BWB2W2 |
| 544 Whirlipede |  | B, B2, W, W2 |  |  | casella Whirlipede; Whirlipede con origine BWB2W2 |
| 545 Scolipede |  | B, B2, W, W2 |  |  | casella Scolipede; Scolipede con origine BWB2W2 |
| 546 Cottonee |  | W2 |  |  | Cottonee «Fluffee» di Cotton/05720, W2 |
| 547 Whimsicott |  | W |  |  | Whimsicott «Fluffee» di Dye/39922, W |
| 547 Whimsicott |  | W2 |  |  | Whimsicott «Fluffee» di Cotton/05720, W2 |
| 548 Petilil |  | B2 |  |  | Petilil «Petulia» di Calla/65217, B2 |
| 549 Lilligant |  | B |  |  | Lilligant «Lillil» di Dye/39922, B; casella Lilligant; Lilligant con origine BWB2W2 |
| 549 Lilligant |  | B |  |  | Lilligant «Lillil» di Dye/39922, B + PLA |
| 549 Lilligant |  | B2 |  |  | Lilligant «Petulia» di Calla/65217, B2 |
| 549 Lilligant |  | B2 |  |  | Lilligant «Petulia» di Calla/65217, B2 + PLA |
| 549 Lilligant |  | B, B2, W, W2 |  |  | Lilligant, Bronze, BWB2W2: ★71: Hisuian Form. |
| 550 Basculin |  | B, B2, W, W2 |  |  | Basculin Red-Striped Form, origine BWB2W2 |
| 550 Basculin |  | B, B2, W, W2 |  |  | Basculin Blue-Striped Form, origine BWB2W2 |
| 551 Sandile |  | B, B2, W, W2 |  |  | Sandile «» di N/00002, BWB2W2; casella Sandile; Sandile con origine BWB2W2 |
| 551 Sandile |  | B2, W2 |  |  | Sandile, Bronze, B2W2: ★72: N's. |
| 552 Krokorok |  | B, B2, W, W2 |  |  | Krokorok «» di N/00002, BWB2W2; casella Krokorok; Krokorok con origine BWB2W2 |
| 553 Krookodile |  | B, B2, W, W2 |  |  | Krookodile «» di N/00002, BWB2W2; Krookodile con origine BWB2W2 |
| 554 Darumaka |  | B, B2, W, W2 |  |  | Darumaka «» di N/00002, BWB2W2; casella Darumaka; Darumaka con origine BWB2W2 |
| 554 Darumaka |  | B2, W2 |  |  | Darumaka, Bronze, B2W2: ★73: N's. |
| 555 Darmanitan |  | B, B2, W, W2 |  |  | Darmanitan «» di N/00002, BWB2W2; Darmanitan con origine BWB2W2 |
| 555 Darmanitan |  | B, B2, W, W2 |  |  | Darmanitan «» di N/00002, BWB2W3 |
| 555 Darmanitan |  | B, W |  |  | Darmanitan, BW: Interactable, Desert Resort. Need RageCandyBar to awaken them. |
| 555 Darmanitan |  | B2, W2 |  |  | Darmanitan, Bronze, B2W2: ★74: N's. |
| 555 Darmanitan |  | AS, OR |  |  | Darmanitan al livello 32.0, ORAS |
| 556 Maractus |  | B, B2, W, W2 |  |  | casella Maractus; Maractus con origine BWB2W2 |
| 557 Dwebble |  | B, B2, W, W2 |  |  | casella Dwebble; Dwebble con origine BWB2W2 |
| 558 Crustle |  | B2, W2 |  |  | Crustle, B2W2: Interactable, Seaside Cave, with Colress Machine.; casella Crustle; Crustle con origine BWB2W2 |
| 559 Scraggy |  | B, B2, W, W2 |  |  | Scraggy «» di N/00002, BWB2W2 |
| 559 Scraggy |  | B2, W2 |  |  | Scraggy, Bronze, B2W2: ★75: N's. |
| 560 Scrafty |  | B, B2, W, W2 |  |  | Scrafty «» di N/00002, BWB2W2 |
| 561 Sigilyph |  | B, B2, W, W2 |  |  | Sigilyph «» di N/00002, BWB2W2 |
| 561 Sigilyph |  | B2, W2 |  |  | Sigilyph, Bronze, B2W2: ★76: N's. |
| 562 Yamask |  | B, B2, W, W2 |  |  | casella Yamask; Yamask con origine BWB2W2 |
| 563 Cofagrigus |  | AS, OR |  |  | Cofagrigus al livello 32.0, ORAS |
| 563 Cofagrigus |  | B, B2, W, W2 |  |  | Cofagrigus con origine BWB2W2 |
| 565 Carracosta |  | B, B2, W, W2 |  |  | casella Carracosta; Carracosta con origine BWB2W2 |
| 567 Archeops |  | B, B2, W, W2 |  |  | casella Archeops; Archeops con origine BWB2W2 |
| 568 Trubbish |  | B, B2, W, W2 |  |  | casella Trubbish; Trubbish con origine BWB2W2 |
| 569 Garbodor |  | B, B2, W, W2 |  |  | Garbodor forma, origine BWB2W2 |
| 569 Garbodor |  | B, B2, W, W2 |  |  | casella Garbodor; Garbodor con origine BWB2W2 |
| 570 Zorua |  | B, B2, W, W2 |  |  | Zorua «N's Zorua» di N/00002, BWB2W2; casella Zorua; Zorua con origine BWB2W2 |
| 570 Zorua |  | B, W |  |  | Zorua, BW: Castelia City, in one of the buildings, with event Celebi in party. |
| 570 Zorua |  | B2, W2 |  |  | Zorua, Bronze, B2W2: ★77: N's. |
| 571 Zoroark |  | B, B2, W, W2 |  |  | Zoroark «» di N/00002, BWB2W2 |
| 572 Minccino |  | B2, W2 |  |  | Minccino, B2W2: Interactable, Route 5, Hidden Grotto w/ Bianca.; casella Minccino; Minccino con origine BWB2W2 |
| 573 Cinccino |  | B, B2, W, W2 |  |  | casella Cinccino; Cinccino con origine BWB2W2 |
| 574 Gothita |  | B, B2, W, W2 |  |  | casella Gothita; Gothita con origine BWB2W2 |
| 575 Gothorita |  | B, B2, W, W2 |  |  | casella Gothorita; Gothorita con origine BWB2W2 |
| 576 Gothitelle |  | B, B2, W, W2 |  |  | casella Gothitelle; Gothitelle con origine BWB2W2 |
| 577 Solosis |  | B, B2, W, W2 |  |  | casella Solosis; Solosis con origine BWB2W2 |
| 578 Duosion |  | B, B2, W, W2 |  |  | casella Duosion; Duosion con origine BWB2W2 |
| 579 Reuniclus |  | B, B2, W, W2 |  |  | casella Reuniclus; Reuniclus con origine BWB2W2 |
| 580 Ducklett |  | B, B2, W, W2 |  |  | casella Ducklett; Ducklett con origine BWB2W2 |
| 581 Swanna |  | X, Y |  |  | Swanna al livello 30.0, XY; casella Swanna |
| 581 Swanna |  | B, B2, W, W2 |  |  | Swanna con origine BWB2W2 |
| 582 Vanillite |  | B, B2, W, W2 |  |  | casella Vanillite; Vanillite con origine BWB2W2 |
| 583 Vanillish |  | B, B2, W, W2 |  |  | casella Vanillish; Vanillish con origine BWB2W2 |
| 584 Vanilluxe |  | B, B2, W, W2 |  |  | casella Vanilluxe; Vanilluxe con origine BWB2W2 |
| 585 Deerling |  | B, B2, W, W2 |  |  | Deerling Spring Form, origine BWB2W2 |
| 585 Deerling |  | B, B2, W, W2 |  |  | Deerling Summer Form, origine BWB2W2 |
| 585 Deerling |  | B, B2, W, W2 |  |  | Deerling Autumn Form, origine BWB2W2 |
| 585 Deerling |  | B, B2, W, W2 |  |  | Deerling Winter Form, origine BWB2W2 |
| 585 Deerling |  | B2, W2 |  |  | Deerling, B2W2: Weather Institute in Route 6.; casella Deerling; Deerling con origine BWB2W2 |
| 585 Deerling | Estate | qualunque |  |  | casella Deerling Estate |
| 585 Deerling | Autunno | qualunque |  |  | casella Deerling Autunno |
| 585 Deerling | Inverno | qualunque |  |  | casella Deerling Inverno |
| 586 Sawsbuck |  | B, B2, W, W2 |  |  | Sawsbuck Spring Form, origine BWB2W2 |
| 586 Sawsbuck |  | B, B2, W, W2 |  |  | Sawsbuck Summer Form, origine BWB2W2 |
| 586 Sawsbuck |  | B, B2, W, W2 |  |  | Sawsbuck Autumn Form, origine BWB2W2 |
| 586 Sawsbuck |  | B, B2, W, W2 |  |  | Sawsbuck Winter Form, origine BWB2W2 |
| 586 Sawsbuck |  | X, Y |  |  | Sawsbuck al livello 30.0, XY; casella Sawsbuck |
| 586 Sawsbuck |  | B, B2, W, W2 |  |  | Sawsbuck con origine BWB2W2 |
| 586 Sawsbuck | Estate | qualunque |  |  | casella Sawsbuck Estate |
| 586 Sawsbuck | Autunno | qualunque |  |  | casella Sawsbuck Autunno |
| 586 Sawsbuck | Inverno | qualunque |  |  | casella Sawsbuck Inverno |
| 589 Escavalier |  | B, B2, W, W2 |  |  | casella Escavalier; Escavalier con origine BWB2W2 |
| 590 Foongus |  | B, W |  |  | Foongus, BW: Interactable, 	Route 6, Route 10.; casella Foongus; Foongus con origine BWB2W2 |
| 590 Foongus |  | B2, W2 |  |  | Foongus, B2W2: Interactable, Route 6, Route 7. |
| 591 Amoonguss |  | B, W |  |  | Amoonguss, BW: Interactable, Route 10.; casella Amoonguss; Amoonguss con origine BWB2W2 |
| 591 Amoonguss |  | B2, W2 |  |  | Amoonguss, B2W2: Interactable, Route 22. |
| 592 Frillish |  | UM, US |  |  | Frillish, USUM: In the ruins in the water on Route 14, you will see a group of Frillish attackin; casella Frillish |
| 592 Frillish |  | B, B2, W, W2 |  |  | Frillish con origine BWB2W2; Frillish ♂, origine BWB2W2 |
| 592 Frillish |  | B, B2, W, W2 |  |  | Frillish ♀, origine BWB2W2 |
| 593 Jellicent |  | B, W |  |  | Jellicent al livello 5.0, BW; casella Jellicent; Jellicent con origine BWB2W2; Jellicent ♂, origine BWB2W2 |
| 593 Jellicent |  | B, B2, W, W2 |  |  | Jellicent ♀, origine BWB2W2 |
| 594 Alomomola |  | B, B2, W, W2 |  |  | casella Alomomola; Alomomola con origine BWB2W2 |
| 595 Joltik |  | B, B2, W, W2 |  |  | Joltik «» di N/00002, BWB2W2; casella Joltik; Joltik con origine BWB2W2 |
| 595 Joltik |  | B2, W2 |  |  | Joltik, Bronze, B2W2: ★78: N's. |
| 596 Galvantula |  | B, B2, W, W2 |  |  | Galvantula «» di N/00002, BWB2W2; casella Galvantula; Galvantula con origine BWB2W2 |
| 597 Ferroseed |  | B, B2, W, W2 |  |  | Ferroseed «» di N/00002, BWB2W2; casella Ferroseed; Ferroseed con origine BWB2W2 |
| 597 Ferroseed |  | B2, W2 |  |  | Ferroseed, Bronze, B2W2: ★79: N's. |
| 598 Ferrothorn |  | B, B2, W, W2 |  |  | Ferrothorn «» di N/00002, BWB2W2; casella Ferrothorn; Ferrothorn con origine BWB2W2 |
| 599 Klink |  | B, B2, W, W2 |  |  | Klink «» di N/00002, BWB2W2; casella Klink; Klink con origine BWB2W2 |
| 599 Klink |  | B2, W2 |  |  | Klink, Bronze, B2W2: ★80: N's. |
| 600 Klang |  | B, B2, W, W2 |  |  | Klang «» di N/00002, BWB2W2; casella Klang; Klang con origine BWB2W2 |
| 601 Klinklang |  | B, B2, W, W2 |  |  | Klinklang «» di N/00002, BWB2W2; casella Klinklang; Klinklang con origine BWB2W2 |
| 602 Tynamo |  | B, B2, W, W2 |  |  | casella Tynamo; Tynamo con origine BWB2W2 |
| 603 Eelektrik |  | B, B2, W, W2 |  |  | casella Eelektrik; Eelektrik con origine BWB2W2 |
| 604 Eelektross |  | B, B2, W, W2 |  |  | casella Eelektross; Eelektross con origine BWB2W2 |
| 605 Elgyem |  | B, B2, W, W2 |  |  | casella Elgyem; Elgyem con origine BWB2W2 |
| 606 Beheeyem |  | B, B2, W, W2 |  |  | casella Beheeyem; Beheeyem con origine BWB2W2 |
| 607 Litwick |  | B, B2, W, W2 |  |  | casella Litwick; Litwick, per «Register Litwick brought over using Poké Transporter!»; Litwick con origine BWB2W2 |
| 608 Lampent |  | B, B2, W, W2 |  |  | casella Lampent; Lampent con origine BWB2W2 |
| 611 Fraxure |  | B, B2, W, W2 |  |  | casella Fraxure; Fraxure con origine BWB2W2 |
| 612 Haxorus |  | B2, W2 |  |  | Haxorus, Gold, B2W2: ★10: Nature Preserve. Guaranteed Shiny. |
| 614 Beartic |  | B, B2, W, W2 |  |  | casella Beartic; Beartic con origine BWB2W2 |
| 615 Cryogonal |  | B, B2, W, W2 |  |  | casella Cryogonal; Cryogonal con origine BWB2W2 |
| 617 Accelgor |  | B, B2, W, W2 |  |  | casella Accelgor; Accelgor con origine BWB2W2 |
| 618 Stunfisk |  | B, B2, W, W2 |  |  | casella Stunfisk; Stunfisk con origine BWB2W2 |
| 619 Mienfoo |  | B, B2, W, W2 |  |  | casella Mienfoo; Mienfoo con origine BWB2W2 |
| 620 Mienshao |  | B, B2, W, W2 |  |  | Mienshao con origine BWB2W2 |
| 622 Golett |  | B, B2, W, W2 |  |  | casella Golett; Golett con origine BWB2W2 |
| 624 Pawniard |  | B, B2, W, W2 |  |  | casella Pawniard; Pawniard con origine BWB2W2 |
| 625 Bisharp |  | B, B2, W, W2 |  |  | Bisharp con origine BWB2W2 |
| 626 Bouffalant |  | B, B2, W, W2 |  |  | Bouffalant con origine BWB2W2 |
| 627 Rufflet |  | B, B2, W, W2 |  |  | casella Rufflet; Rufflet con origine BWB2W2 |
| 628 Braviary |  | W2 |  |  | Braviary, W2: Interactable, Route 4, White 2, Mondays.; casella Braviary; Braviary con origine BWB2W2 |
| 628 Braviary |  | B, B2, W, W2 |  |  | Braviary, Bronze, BWB2W2: ★81: Hisuian Form. |
| 629 Vullaby |  | B, B2, W, W2 |  |  | casella Vullaby; Vullaby con origine BWB2W2 |
| 630 Mandibuzz |  | B2 |  |  | Mandibuzz, B2: Interactable, Route 4, Black 2, Thursdays.; casella Mandibuzz; Mandibuzz con origine BWB2W2 |
| 631 Heatmor |  | B, B2, W, W2 |  |  | casella Heatmor; Heatmor con origine BWB2W2 |
| 632 Durant |  | B, B2, W, W2 |  |  | casella Durant; Durant con origine BWB2W2 |
| 634 Zweilous |  | B, B2, W, W2 |  |  | casella Zweilous; Zweilous con origine BWB2W2 |
| 636 Larvesta |  | B, W |  |  | Larvesta, BW: Egg, Route 18, inside a house.; casella Larvesta; Larvesta con origine BWB2W2 |
| 637 Volcarona |  | UM, US |  |  | Volcarona, Platinum, USUM: ★14: Lush Jungle. Caught as Volcarona. |
| 638 Cobalion |  | B, B2, W, W2 |  |  | casella Cobalion; Cobalion con origine BWB2W2 |
| 639 Terrakion |  | B, B2, W, W2 |  |  | casella Terrakion; Terrakion con origine BWB2W2 |
| 640 Virizion |  | B, B2, W, W2 |  |  | casella Virizion; Virizion con origine BWB2W2 |
| 641 Tornadus |  | B, B2, W, W2 |  |  | Tornadus Therian Forme, origine BWB2W2 |
| 641 Tornadus |  | B2, W2 |  |  | Tornadus, Gold, Dream Radar: ★30 |
| 642 Thundurus |  | B, B2, W, W2 |  |  | Thundurus Therian Forme, origine BWB2W2 |
| 642 Thundurus |  | B2, W2 |  |  | Thundurus, Gold, Dream Radar: ★31 |
| 643 Reshiram |  | B2, W2 |  |  | Reshiram, Platinum, Black: ★11: Dragonspiral Tower.; Reshiram, per «Register Reshiram and Kyurem from Pokémon Black 2 or Pokémon White 2» |
| 644 Zekrom |  | B2, W2 |  |  | Zekrom, Platinum, White: ★11: Dragonspiral Tower.; Zekrom, per «Register Zekrom and Kyurem from Pokémon Black 2 or Pokémon White 2» |
| 645 Landorus |  | B, B2, W, W2 |  |  | Landorus Therian Forme, origine BWB2W2 |
| 645 Landorus |  | B2, W2 |  |  | Landorus, Gold, Dream Radar: ★32 |
| 646 Kyurem |  | B2, W2 |  |  | Kyurem, per «Register Reshiram and Kyurem from Pokémon Black 2 or Pokémon White 2»; Kyurem, per «Register Zekrom and Kyurem from Pokémon Black 2 or Pokémon White 2»; Kyurem con origine BWB2W2 |
| 647 Keldeo |  | qualunque |  |  | Keldeo Resolute Forme, origine Any |
| 647 Keldeo | Risoluta | qualunque |  |  | casella Keldeo Risoluta |
| 651 Quilladin |  | X, Y |  |  | Quilladin «Chester» di Shauna/00037, XY; casella Quilladin |
| 652 Chesnaught |  | X, Y |  |  | Chesnaught «Chester» di Shauna/00037, XY; casella Chesnaught |
| 654 Braixen |  | X, Y |  |  | Braixen «Kinniekins» di Shauna/00037, XY; casella Braixen |
| 655 Delphox |  | X, Y |  |  | Delphox «Kinniekins» di Shauna/00037, XY; casella Delphox |
| 657 Frogadier |  | X, Y |  |  | Frogadier «Froabble» di Shauna/00037, XY; casella Frogadier |
| 658 Greninja |  | X, Y |  |  | Greninja «Froabble» di Shauna/00037, XY |
| 658 Greninja |  | MN, SN |  |  | Greninja «Ash Greninja» di Ash/131017, SM |
| 658 Greninja |  | MN, SN |  |  | Greninja, Gold, SM Demo: ★37 |
| 659 Bunnelby |  | qualunque |  |  | casella Bunnelby |
| 660 Diggersby |  | qualunque |  |  | casella Diggersby |
| 661 Fletchling |  | qualunque |  |  | casella Fletchling |
| 662 Fletchinder |  | UM, US |  |  | Fletchinder al livello 16.0, USUM; casella Fletchinder |
| 664 Scatterbug |  | qualunque |  |  | casella Scatterbug |
| 665 Spewpa |  | qualunque |  |  | casella Spewpa |
| 666 Vivillon |  | qualunque |  |  | Vivillon Archipelago Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Continental Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Elegant Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Garden Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon High Plains Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Icy Snow Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Jungle Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Marine Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Meadow Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Modern Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Monsoon Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Ocean Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Polar Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon River Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Sandstorm Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Savanna Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Sun Form, origine Any |
| 666 Vivillon |  | qualunque |  |  | Vivillon Tundra Form, origine Any |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Archipelago Form.; casella Vivillon |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Continental Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Elegant Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Garden Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: High Plains Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Icy Snow Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Jungle Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Marine Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Meadow Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Modern Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Monsoon Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Ocean Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Polar Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: River Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Sandstorm Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Savanna Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Sun Form. |
| 666 Vivillon |  | X, Y |  |  | Vivillon, Platinum, XY: ★12: Tundra Form. |
| 666 Vivillon | Nordico | qualunque |  |  | casella Vivillon Nordico |
| 666 Vivillon | Manto di Neve | qualunque |  |  | casella Vivillon Manto di Neve |
| 666 Vivillon | Continentale | qualunque |  |  | casella Vivillon Continentale |
| 666 Vivillon | Prato | qualunque |  |  | casella Vivillon Prato |
| 666 Vivillon | Eleganza | qualunque |  |  | casella Vivillon Eleganza |
| 666 Vivillon | Giardinfiore | qualunque |  |  | casella Vivillon Giardinfiore |
| 666 Vivillon | Trendy | qualunque |  |  | casella Vivillon Trendy |
| 666 Vivillon | Marino | qualunque |  |  | casella Vivillon Marino |
| 666 Vivillon | Arcipelago | qualunque |  |  | casella Vivillon Arcipelago |
| 666 Vivillon | Deserto | qualunque |  |  | casella Vivillon Deserto |
| 666 Vivillon | Sabbia | qualunque |  |  | casella Vivillon Sabbia |
| 666 Vivillon | Fluviale | qualunque |  |  | casella Vivillon Fluviale |
| 666 Vivillon | Pluviale | qualunque |  |  | casella Vivillon Pluviale |
| 666 Vivillon | Savana | qualunque |  |  | casella Vivillon Savana |
| 666 Vivillon | Solare | qualunque |  |  | casella Vivillon Solare |
| 666 Vivillon | Oceanico | qualunque |  |  | casella Vivillon Oceanico |
| 666 Vivillon | Giungla | qualunque |  |  | casella Vivillon Giungla |
| 667 Litleo |  | qualunque |  |  | casella Litleo |
| 668 Pyroar |  | X, Y |  |  | Pyroar al livello 30.0, XY |
| 669 Flabébé |  | qualunque |  |  | casella Flabébé |
| 669 Flabébé | Giallo | qualunque |  |  | casella Flabébé Giallo |
| 669 Flabébé | Arancione | qualunque |  |  | casella Flabébé Arancione |
| 669 Flabébé | Blu | qualunque |  |  | casella Flabébé Blu |
| 669 Flabébé | Bianco | qualunque |  |  | casella Flabébé Bianco |
| 670 Floette |  | qualunque |  |  | casella Floette |
| 670 Floette | Giallo | qualunque |  |  | casella Floette Giallo |
| 670 Floette | Arancione | qualunque |  |  | casella Floette Arancione |
| 670 Floette | Blu | qualunque |  |  | casella Floette Blu |
| 670 Floette | Bianco | qualunque |  |  | casella Floette Bianco |
| 671 Florges |  | qualunque |  |  | casella Florges |
| 671 Florges | Giallo | qualunque |  |  | casella Florges Giallo |
| 671 Florges | Arancione | qualunque |  |  | casella Florges Arancione |
| 671 Florges | Blu | qualunque |  |  | casella Florges Blu |
| 671 Florges | Bianco | qualunque |  |  | casella Florges Bianco |
| 672 Skiddo |  | qualunque |  |  | casella Skiddo |
| 673 Gogoat |  | X, Y |  |  | Gogoat al livello 30.0, XY; casella Gogoat |
| 675 Pangoro |  | qualunque |  |  | casella Pangoro |
| 676 Furfrou |  | qualunque |  |  | casella Furfrou |
| 677 Espurr |  | qualunque |  |  | casella Espurr |
| 678 Meowstic |  | qualunque |  |  | casella Meowstic |
| 678 Meowstic | F | qualunque |  |  | casella Meowstic F |
| 679 Honedge |  | qualunque |  |  | casella Honedge |
| 680 Doublade |  | qualunque |  |  | casella Doublade |
| 682 Spritzee |  | qualunque |  |  | casella Spritzee |
| 684 Swirlix |  | qualunque |  |  | casella Swirlix |
| 685 Slurpuff |  | qualunque |  |  | casella Slurpuff |
| 688 Binacle |  | qualunque |  |  | casella Binacle |
| 689 Barbaracle |  | qualunque |  |  | casella Barbaracle |
| 690 Skrelp |  | qualunque |  |  | casella Skrelp |
| 691 Dragalge |  | qualunque |  |  | casella Dragalge |
| 692 Clauncher |  | qualunque |  |  | casella Clauncher |
| 693 Clawitzer |  | qualunque |  |  | casella Clawitzer |
| 694 Helioptile |  | qualunque |  |  | casella Helioptile |
| 695 Heliolisk |  | qualunque |  |  | casella Heliolisk |
| 697 Tyrantrum |  | qualunque |  |  | casella Tyrantrum |
| 699 Aurorus |  | qualunque |  |  | casella Aurorus |
| 700 Sylveon |  | D, P, Pt |  |  | Sylveon «» di Hayley/01000, My Pokémon Ranch |
| 700 Sylveon |  | X, Y |  |  | Sylveon «Stevie» di Elena/29294, XY |
| 700 Sylveon |  | BU, GN, RD, YW |  |  | Sylveon, Bronze, RBY: ★26 |
| 702 Dedenne |  | qualunque |  |  | casella Dedenne |
| 703 Carbink |  | qualunque |  |  | casella Carbink |
| 705 Sliggoo |  | X, Y |  |  | Sliggoo, Bronze, XY: ★84: Hisuian Form.; casella Sliggoo |
| 706 Goodra |  | X, Y |  |  | Goodra, Bronze, XY: ★85: Hisuian Form.; casella Goodra |
| 707 Klefki |  | qualunque |  |  | casella Klefki |
| 708 Phantump |  | qualunque |  |  | casella Phantump |
| 710 Pumpkaboo |  | qualunque |  |  | casella Pumpkaboo |
| 710 Pumpkaboo | Mini | qualunque |  |  | casella Pumpkaboo Mini |
| 710 Pumpkaboo | Grande | qualunque |  |  | casella Pumpkaboo Grande |
| 711 Gourgeist |  | qualunque |  |  | casella Gourgeist |
| 711 Gourgeist | Mini | qualunque |  |  | casella Gourgeist Mini |
| 711 Gourgeist | Grande | qualunque |  |  | casella Gourgeist Grande |
| 711 Gourgeist | Maxi | qualunque |  |  | casella Gourgeist Maxi |
| 712 Bergmite |  | qualunque |  |  | casella Bergmite |
| 713 Avalugg |  | X, Y |  |  | Avalugg, Bronze, XY: ★86: Hisuian Form.; casella Avalugg |
| 715 Noivern |  | UM, US |  |  | Noivern «Noinoi» di Kihei/610507, USUM; casella Noivern |
| 718 Zygarde |  | MN, SN, UM, US |  |  | Zygarde 10% Forme, origine SMUSUM |
| 718 Zygarde |  | X, Y |  |  | Zygarde, Bronze, XY: ★87: 10% Forme. |
| 718 Zygarde |  | MN, SN |  |  | Zygarde, Silver, SM: ★12: Made using 100 Cells/Cores found in SM. |
| 718 Zygarde | 10% | qualunque |  |  | casella Zygarde 10% |
| 720 Hoopa |  | qualunque |  |  | Hoopa Unbound Form, origine Any |
| 722 Rowlet |  | MN, SN, UM, US |  |  | casella Rowlet; Rowlet con origine SMUSUM |
| 723 Dartrix |  | MN, SN, UM, US |  |  | casella Dartrix; Dartrix con origine SMUSUM |
| 724 Decidueye |  | MN, SN, UM, US |  |  | Decidueye, Bronze, SMUSUM: ★89: Hisuian Form. |
| 725 Litten |  | MN, SN, UM, US |  |  | casella Litten; Litten con origine SMUSUM |
| 726 Torracat |  | MN, SN, UM, US |  |  | casella Torracat; Torracat con origine SMUSUM |
| 728 Popplio |  | MN, SN, UM, US |  |  | casella Popplio; Popplio con origine SMUSUM |
| 729 Brionne |  | MN, SN, UM, US |  |  | casella Brionne; Brionne con origine SMUSUM |
| 731 Pikipek |  | MN, SN, UM, US |  |  | casella Pikipek; Pikipek con origine SMUSUM |
| 732 Trumbeak |  | MN, SN, UM, US |  |  | casella Trumbeak; Trumbeak con origine SMUSUM |
| 733 Toucannon |  | MN, SN, UM, US |  |  | Toucannon al livello 26.0, SMUSUM; casella Toucannon; Toucannon con origine SMUSUM |
| 734 Yungoos |  | MN, SN, UM, US |  |  | casella Yungoos; Yungoos con origine SMUSUM |
| 735 Gumshoos |  | UM, US |  |  | Gumshoos, Silver, USUM: ★16: Totem Variant.; casella Gumshoos |
| 735 Gumshoos |  | UM, US |  |  | Gumshoos al livello 17.0, USUM |
| 736 Grubbin |  | MN, SN, UM, US |  |  | casella Grubbin; Grubbin con origine SMUSUM |
| 737 Charjabug |  | MN, SN, UM, US |  |  | casella Charjabug; Charjabug con origine SMUSUM |
| 738 Vikavolt |  | UM, US |  |  | Vikavolt, Silver, USUM: ★17: Totem Variant.; casella Vikavolt |
| 739 Crabrawler |  | MN, SN, UM, US |  |  | casella Crabrawler; Crabrawler con origine SMUSUM |
| 740 Crabominable |  | MN, SN, UM, US |  |  | casella Crabominable; Crabominable con origine SMUSUM |
| 741 Oricorio |  | MN, SN, UM, US |  |  | Oricorio Baile Style Form, origine SMUSUM |
| 741 Oricorio |  | MN, SN, UM, US |  |  | Oricorio Pom-Pom Style Form, origine SMUSUM |
| 741 Oricorio |  | MN, SN, UM, US |  |  | Oricorio Pa'u Style Form, origine SMUSUM |
| 741 Oricorio |  | MN, SN, UM, US |  |  | Oricorio Sensu Style Form, origine SMUSUM |
| 741 Oricorio |  | MN, SN, UM, US |  |  | casella Oricorio; Oricorio con origine SMUSUM |
| 741 Oricorio | Cheerdance | qualunque |  |  | casella Oricorio Cheerdance |
| 741 Oricorio | Hula | qualunque |  |  | casella Oricorio Hula |
| 741 Oricorio | Buyō | qualunque |  |  | casella Oricorio Buyō |
| 742 Cutiefly |  | MN, SN, UM, US |  |  | casella Cutiefly; Cutiefly con origine SMUSUM |
| 743 Ribombee |  | qualunque |  |  | casella Ribombee |
| 744 Rockruff |  | qualunque |  |  | casella Rockruff |
| 745 Lycanroc |  | MN, SN, UM, US |  |  | Lycanroc Midday Form, origine SMUSUM |
| 745 Lycanroc |  | MN, SN, UM, US |  |  | Lycanroc Midnight Form, origine SMUSUM |
| 745 Lycanroc |  | UM, US |  |  | Lycanroc Dusk Form, origine USUM |
| 745 Lycanroc |  | qualunque |  |  | casella Lycanroc |
| 745 Lycanroc | Forma Crepuscolo | qualunque |  |  | casella Lycanroc Forma Crepuscolo |
| 746 Wishiwashi |  | MN, SN, UM, US |  |  | casella Wishiwashi; Wishiwashi con origine SMUSUM |
| 748 Toxapex |  | MN, SN, UM, US |  |  | casella Toxapex; Toxapex con origine SMUSUM |
| 749 Mudbray |  | MN, SN, UM, US |  |  | casella Mudbray; Mudbray con origine SMUSUM |
| 750 Mudsdale |  | MN, SN, UM, US |  |  | casella Mudsdale; Mudsdale con origine SMUSUM |
| 751 Dewpider |  | MN, SN, UM, US |  |  | casella Dewpider; Dewpider con origine SMUSUM |
| 752 Araquanid |  | qualunque |  |  | casella Araquanid |
| 753 Fomantis |  | MN, SN, UM, US |  |  | casella Fomantis; Fomantis con origine SMUSUM |
| 754 Lurantis |  | UM, US |  |  | Lurantis, Silver, USUM: ★18: Totem Variant.; casella Lurantis |
| 755 Morelull |  | MN, SN, UM, US |  |  | casella Morelull; Morelull con origine SMUSUM |
| 756 Shiinotic |  | MN, SN, UM, US |  |  | casella Shiinotic; Shiinotic con origine SMUSUM |
| 757 Salandit |  | MN, SN, UM, US |  |  | casella Salandit; Salandit con origine SMUSUM |
| 758 Salazzle |  | UM, US |  |  | Salazzle, Silver, USUM: ★19: Totem Variant. |
| 758 Salazzle |  | UM, US |  |  | Salazzle al livello 16.0, USUM |
| 759 Stufful |  | MN, SN, UM, US |  |  | casella Stufful; Stufful con origine SMUSUM |
| 760 Bewear |  | UM, US |  |  | Bewear, USUM: After completion of the Akala Grand Trial, when you go to the Hau'oli City Shopp |
| 763 Tsareena |  | MN, SN |  |  | Tsareena «Bouncee» di Kihei/610507, SM; casella Tsareena; Tsareena con origine SMUSUM |
| 763 Tsareena |  | MN, SN |  |  | Tsareena «Stena» di Kumu/610503, SM |
| 767 Wimpod |  | MN, SN, UM, US |  |  | casella Wimpod; Wimpod con origine SMUSUM |
| 768 Golisopod |  | MN, SN, UM, US |  |  | casella Golisopod; Golisopod con origine SMUSUM |
| 769 Sandygast |  | UM, US |  |  | Sandygast, USUM: When on Route 15 in Ultra Moon, you will find a youngster who asks if you want t; casella Sandygast; Sandygast con origine SMUSUM |
| 770 Palossand |  | MN, SN, UM, US |  |  | casella Palossand; Palossand con origine SMUSUM |
| 771 Pyukumuku |  | MN, SN, UM, US |  |  | casella Pyukumuku; Pyukumuku con origine SMUSUM |
| 772 Tipo Zero |  | MN, SN, UM, US |  | sì | casella Tipo Zero; Tipo Zero cromatico; Tipo Zero con origine SMUSUM |
| 774 da scegliere |  | MN, SN, UM, US |  |  | Minior Red Core Form, origine SMUSUM |
| 774 da scegliere |  | MN, SN, UM, US |  |  | Minior Orange Core Form, origine SMUSUM |
| 774 da scegliere |  | MN, SN, UM, US |  |  | Minior Yellow Core Form, origine SMUSUM |
| 774 da scegliere |  | MN, SN, UM, US |  |  | Minior Green Core Form, origine SMUSUM |
| 774 da scegliere |  | MN, SN, UM, US |  |  | Minior Blue Core Form, origine SMUSUM |
| 774 da scegliere |  | MN, SN, UM, US |  |  | Minior Indigo Core Form, origine SMUSUM |
| 774 da scegliere |  | MN, SN, UM, US |  |  | Minior Violet Core Form, origine SMUSUM |
| 774 da scegliere |  | MN, SN, UM, US |  |  | Minior con origine SMUSUM |
| 774 da scegliere | N-Rosso | qualunque |  |  | casella Minior N-Rosso |
| 774 da scegliere | N-Arancione | qualunque |  |  | casella Minior N-Arancione |
| 774 da scegliere | N-Giallo | qualunque |  |  | casella Minior N-Giallo |
| 774 da scegliere | N-Verde | qualunque |  |  | casella Minior N-Verde |
| 774 da scegliere | N-Azzurro | qualunque |  |  | casella Minior N-Azzurro |
| 774 da scegliere | N-Indaco | qualunque |  |  | casella Minior N-Indaco |
| 774 da scegliere | N-Violetto | qualunque |  |  | casella Minior N-Violetto |
| 775 Komala |  | MN, SN, UM, US |  |  | casella Komala; Komala con origine SMUSUM |
| 777 Togedemaru |  | qualunque |  |  | casella Togedemaru |
| 778 Mimikyu |  | UM, US |  |  | Mimikyu, Silver, USUM: ★20: Totem Variant. |
| 779 Bruxish |  | MN, SN, UM, US |  |  | casella Bruxish; Bruxish con origine SMUSUM |
| 781 Dhelmise |  | MN, SN, UM, US |  |  | casella Dhelmise; Dhelmise con origine SMUSUM |
| 782 Jangmo-o |  | MN, SN, UM, US |  |  | casella Jangmo-o; Jangmo-o con origine SMUSUM |
| 783 Hakamo-o |  | MN, SN, UM, US |  |  | casella Hakamo-o; Hakamo-o con origine SMUSUM |
| 784 Kommo-o |  | UM |  |  | Kommo-o, Silver, UM: ★21: Totem Variant.; casella Kommo-o |
| 789 Cosmog |  | MN, SN |  |  | Cosmog, SM: Lake of the Sunne/Moone, with Solgaleo/Lunala in party.; casella Cosmog; Cosmog, per «Register Cosmog, Cosmoem, Solgaleo and Lunala from the Alola Region»; Cosmog con origine SMUSUM |
| 789 Cosmog |  | UM, US |  |  | Cosmog, USUM: Lake of the Sunne/Moone, w/ Solgaleo/Lunala in party. |
| 790 Cosmoem |  | MN, SN, UM, US |  |  | casella Cosmoem; Cosmoem, per «Register Cosmog, Cosmoem, Solgaleo and Lunala from the Alola Region»; Cosmoem con origine SMUSUM |
| 792 Lunala |  | MN, SN |  |  | Lunala, per «Register Lunala from Pokémon Sun or Pokémon Moon» |
| 793 Nihilego |  | MN, SN, UM, US |  |  | casella Nihilego; Nihilego con origine SMUSUM |
| 794 Buzzwole |  | MN, SN, UM, US |  |  | casella Buzzwole; Buzzwole con origine SMUSUM |
| 795 Pheromosa |  | MN, SN, UM, US |  |  | casella Pheromosa; Pheromosa con origine SMUSUM |
| 796 Xurkitree |  | MN, SN, UM, US |  |  | casella Xurkitree; Xurkitree con origine SMUSUM |
| 797 Celesteela |  | MN, SN, UM, US |  |  | casella Celesteela; Celesteela con origine SMUSUM |
| 798 Kartana |  | MN, SN, UM, US |  |  | casella Kartana; Kartana con origine SMUSUM |
| 799 Guzzlord |  | UM, US |  |  | Guzzlord, Silver, USUM: ★22; casella Guzzlord; Guzzlord con origine SMUSUM |
| 801 Magearna |  | qualunque |  |  | Magearna Original Color Form, origine Any |
| 801 Magearna |  | MN, SN |  |  | Magearna, SM: Scan QR code in-game. The codes outside of Japan never expired. |
| 801 Magearna |  | MN, SN, UM, US |  |  | Magearna, Bronze, SMUSUM: ★90 |
| 804 Naganadel |  | UM, US |  | sì | casella Naganadel; Naganadel cromatico; Naganadel con origine USUM |
| 805 Stakataka |  | UM, US |  |  | casella Stakataka; Stakataka con origine USUM |
| 806 Blacephalon |  | UM, US |  |  | casella Blacephalon; Blacephalon con origine USUM |
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
| da scegliere |  | CXD |  |  | Fiocco Maestro da una specie Ombra di Colosseum o XD, `FIOCCHI-PRIMA-DI-BANK.md` |
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

Tectonic Rage, Cut, Jump Kick, Rolling Kick, Horn Drill, Egg Bomb, Bone Club, Spike Cannon, Kinesis, Barrage, Struggle, Thief, Mach Punch, Rock Smash, Spit Up, Torment, Memento, Nature Power, Role Play, Magic Coat, Recycle, Grudge, Dive, Doom Desire, Pluck, Acupressure, Heal Block, Power Trick, Gastro Acid, Guard Swap, Toxic Spikes, Vacuum Wave, Switcheroo, Psycho Cut, Mirror Shot, Rock Climb, Rock Wrecker, Charge Beam, Attack Order, Defend Order, Heal Order, Lunar Dance, Guard Split, Wonder Room, Venoshock, Rage Powder, Telekinesis, Magic Room, Storm Throw, Synchronoise, Soak, Coil, Acid Spray, Entrainment, After You, Clear Smog, Shell Smash, Sky Drop, Circle Throw, Quash, Reflect Type, Retaliate, Final Gambit, Bulldoze, Electroweb, Drill Run, Heat Crash, Leaf Tornado, Steamroller, Cotton Guard, Night Daze, Tail Slap, Gear Grind, Secret Sword, Freeze Shock, Ice Burn, Flying Press, Belch, Rototiller, Sticky Web, Fell Stinger, Ion Deluge, Parabolic Charge, Petal Blizzard, Crafty Shield, Flower Shield, Grassy Terrain, Misty Terrain, Electrify, Boomburst, Fairy Lock, Mystical Fire, Spiky Shield, Eerie Impulse, Powder, Magnetic Flux, Electric Terrain, Infestation, Thousand Waves, Light of Ruin, Hyperspace Fury, Shore Up, First Impression, Baneful Bunker, Spirit Shackle, Sparkling Aria, Ice Hammer, Floral Healing, High Horsepower, Strength Sap, Solar Blade, Leafage, Spotlight, Toxic Thread, Laser Focus, Gear Up, Pollen Puff, Anchor Shot, Lunge, Fire Lash, Power Trip, Speed Swap, Smart Strike, Purify, Revelation Dance, Core Enforcer, Trop Kick, Beak Blast, Clanging Scales, Dragon Hammer, Psychic Fangs, Shadow Bone, Accelerock, Liquidation, Tearful Look, Mind Blown, Photon Geyser, Clangorous Soulblaze, Zippy Zap, Splishy Splash, Floaty Fall, Pika Papow, Bouncy Bubble, Buzzy Buzz, Sizzly Slide, Glitzy Glow, Baddy Bad, Sappy Seed, Freezy Frost, Sparkly Swirl, Veevee Volley, Double Iron Bash, Breakneck Blitz, Continental Crush, Subzero Slammer, Corkscrew Crash, Devastating Drake, Never-Ending Nightmare, Acid Downpour, Black Hole Eclipse, Shattered Psyche, Twinkle Tackle, Pulverizing Pancake, Bloom Doom, Extreme Evoboost, Sinister Arrow Raid, Malicious Moonsault, Oceanic Operetta, Catastropika, 10,000,000 Volt Thunderbolt, Stoked Sparksurfer, Splintered Stormshards, Inferno Overdrive, Genesis Supernova, Guardian of Alola, Soul-Stealing 7-Star Strike, Searing Sunraze Smash, Menacing Moonraze Maelstrom, Light That Burns the Sky, Hydro Vortex, Gigavolt Havoc, Supersonic Skystrike, All-Out Pummeling, Savage Spin-Out.
