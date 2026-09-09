# Censimento degli scambi in gioco, tutte le generazioni

> Documento generato da `tools/censimento-scambi.py` dalle tabelle del verificatore. Non si modifica a mano: si rigenera. Enumera la classe degli esemplari consegnati da un personaggio in cambio di un altro, che portano allenatore e soprannome altrui e non sono riproducibili da una cattura propria.

Le voci di tabella sono 238 e quelle distinte 233, su 152 specie diverse. I due numeri differiscono perche' le tabelle di una coppia di titoli si sovrappongono per costruzione: c'e' una tabella comune e accanto una tabella per versione, e la stessa voce compare in entrambe. Due voci sono contate come una quando concordano su specie, livello, identificativo dell'allenatore e forma.

Di 46 voci la fonte scrive il valore di personalita', quindi quegli esemplari sono riproducibili byte per byte senza alcuna ricerca di semi. Sulle altre la fedelta' va discussa come per le altre classi, perche' il valore lo genera il gioco al momento della consegna.

Controlli: nessuna voce discorda dal commento che la fonte le scrive accanto. Tutti i tipi di voce hanno le posizioni dichiarate.

## Generazione 1

### TradeGift_RB, da `Encounters1.cs`

Tipo di voce `EncounterTrade1`, 10 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Mr. Mime | 122 | 6 | - | - | Mr. Mime - Abra |
| Nidoran♀ | 29 | 2 | - | - | Nidoran♀ - Nidoran♂ (International) |
| Nidoran♂ | 32 | 2 | - | - | Nidoran♂ - Nidoran♀ (Japanese) |
| Nidorina | 30 | 16 | - | - | Nidorina - Nidorino |
| Lickitung | 108 | 15 | - | - | Lickitung - Slowbro |
| Jynx | 124 | 15 | - | - | Jynx - Poliwhirl |
| Farfetch’d | 83 | 2 | - | - | Farfetch’d - Spearow |
| Electrode | 101 | 3 | - | - | Electrode - Raichu |
| Tangela | 114 | 13 | - | - | Tangela - Venonat |
| Seel | 86 | 28 | - | - | Seel - Ponyta |

### TradeGift_YW, da `Encounters1.cs`

Tipo di voce `EncounterTrade1`, 7 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Mr. Mime | 122 | 8 | - | - | Mr. Mime - Clefairy |
| Machoke | 67 | 16 | - | - | Machoke - Cubone |
| Dugtrio | 51 | 15 | - | - | Dugtrio - Lickitung |
| Parasect | 47 | 13 | - | - | Parasect - Tangel |
| Rhydon | 112 | 15 | - | - | Rhydon - Golduck |
| Dewgong | 87 | 15 | - | - | Dewgong - Growlithe |
| Muk | 89 | 25 | - | - | Muk - Kangaskhan |

### TradeGift_BU, da `Encounters1.cs`

Tipo di voce `EncounterTrade1`, 9 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Mr. Mime | 122 | 3 | - | - | Mr. Mime - Jigglypuff |
| Poliwag | 60 | 2 | - | - | Poliwag - Rattata |
| Kangaskhan | 115 | 15 | - | - | Kangaskhan - Rhydon |
| Tauros | 128 | 28 | - | - | Tauros - Persian |
| Haunter | 93 | 28 | - | - | Haunter - Machop->Machoke |
| Farfetch’d | 83 | 2 | - | - | Farfetch’d - Wild Pidgey |
| Graveler | 75 | 16 | - | - | Graveler - Abra->Kadabra |
| Slowpoke | 79 | 22 | - | - | Slowpoke - Seel |
| Krabby | 98 | 15 | - | - | Krabby - Growlithe |

## Generazione 2

### TradeGift_GSC, da `Encounters2.cs`

Tipo di voce `EncounterTrade2`, 11 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Onix | 95 | 3 | - | - | Onix @ Violet City for Bellsprout [wild] |
| Machop | 66 | 5 | - | - | Machop @ Goldenrod City for Drowzee [wild 9, hatched egg 5] |
| Voltorb | 100 | 5 | - | - | Voltorb @ Olivine City for Krabby [egg] |
| Rhydon | 112 | 10 | - | - | Rhydon @ Blackthorn City for Dragonair [wild] |
| Aerodactyl | 142 | 5 | - | - | Aerodactyl @ Route 14 for Chansey [egg] |
| Rapidash | 78 | 14 | - | - | Rapidash @ Pewter City for Gloom [wild] |
| Dodrio | 85 | 10 | - | - | Dodrio @ Blackthorn City for Dragonair [wild] |
| Xatu | 178 | 15 | - | - | Xatu @ Pewter City for Haunter [wild] |
| Magneton | 82 | 5 | - | - | Magneton @ Power Plant for Dugtrio [traded for Lickitung] |
| Spearow | 21 | 10 | - | - | Spearow @ Goldenrod City for free |
| Shuckle | 213 | 15 | - | - | Shuckle @ Cianwood City for free |

## Generazione 3

### TradeGift_FRLG, da `Encounters3FRLG.cs`

Tipo di voce `EncounterTrade3`, 6 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Mr. Mime | 122 | 5 | 0x00009CAE | 01985 | Abra (Level 5 Breeding) -> Mr. Mime |
| Jynx | 124 | 20 | 0x498A2E1D | 36728 | Poliwhirl (Level 20) -> Jynx |
| Farfetch’d | 83 | 3 | 0x151943D7 | 08810 | Spearow (Level 3 Capture) -> Farfetch'd |
| Electrode | 101 | 3 | 0x06341016 | 50298 | Raichu (Level 3) -> Electrode |
| Tangela | 114 | 5 | 0x5C77ECFA | 60042 | Venonat (Level 5 Breeding) -> Tangela |
| Seel | 86 | 5 | 0x482CAC89 | 09853 | Ponyta (Level 5 Breeding) -> Seel * |

### TradeGift_FR, da `Encounters3FRLG.cs`

Tipo di voce `EncounterTrade3`, 3 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Nidoran♀ | 29 | 5 | 0x4C970B89 | 63184 | Nidoran♀ |
| Nidorina | 30 | 16 | 0x00EECA15 | 13637 | Nidorina * |
| Lickitung | 108 | 25 | 0x451308AB | 01239 | Golduck (Level 25) -> Lickitung  * |

### TradeGift_LG, da `Encounters3FRLG.cs`

Tipo di voce `EncounterTrade3`, 3 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Nidoran♂ | 32 | 5 | 0x4C970B9E | 63184 | Nidoran♂ * |
| Nidorino | 33 | 16 | 0x00EECA19 | 13637 | Nidorino  * |
| Lickitung | 108 | 25 | 0x451308AB | 01239 | Slowbro (Level 25) -> Lickitung  * |

### TradeGift_RS, da `Encounters3RSE.cs`

Tipo di voce `EncounterTrade3`, 3 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Makuhita | 296 | 5 | 0x00009C40 | 49562 | Slakoth (Level 5 Breeding) -> Makuhita |
| Skitty | 300 | 3 | 0x498A2E17 | 02259 | Pikachu (Level 3 Viridian Forest) -> Skitty |
| Corsola | 222 | 21 | 0x4C970B7F | 50183 | Bellossom (Level 21 Oddish -> Gloom -> Bellossom) -> Corsola |

### TradeGift_E, da `Encounters3RSE.cs`

Tipo di voce `EncounterTrade3`, 4 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Seedot | 273 | 4 | 0x00000084 | 38726 | Ralts (Level 4 Route 102) -> Seedot |
| Plusle | 311 | 5 | 0x0000006F | 08460 | Volbeat (Level 5 Breeding) -> Plusle |
| Horsea | 116 | 5 | 0x0000007F | 46285 | Bagon (Level 5 Breeding) -> Horsea* |
| Meowth | 52 | 3 | 0x0000008B | 25945 | Skitty (Level 3 Trade)-> Meowth* |

### Trades, da `Encounters3XD.cs`

Tipo di voce `EncounterTrade3XD`, 4 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Elekid | 239 | 20 | - | 41400 | Elekid @ Snagem Hideout |
| Meditite | 307 | 20 | - | 37149 | Meditite @ Pyrite Town |
| Shuckle | 213 | 20 | - | 37149 | Shuckle @ Pyrite Town |
| Larvitar | 246 | 20 | - | 37149 | Larvitar @ Pyrite Town |

## Generazione 4

### RanchGifts, da `Encounters4DPPt.cs`

Tipo di voce `EncounterTrade4RanchGift`, 22 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Pikachu | 25 | 20 | - | - | Pikachu |
| Vulpix | 37 | 30 | - | - | Vulpix |
| Ponyta | 77 | 16 | - | - | Ponyta |
| Lickitung | 108 | 40 | - | - | Lickitung |
| Tangela | 114 | 1 | - | - | Tangela |
| Eevee | 133 | 30 | - | - | Eevee |
| Aerodactyl | 142 | 50 | - | - | Aerodactyl |
| Yanma | 193 | 45 | - | - | Yanma |
| Miltank | 241 | 48 | - | - | Miltank |
| Shroomish | 285 | 45 | - | - | Shroomish |
| Wailmer | 320 | 45 | - | - | Wailmer |
| Wynaut | 360 | 1 | - | - | Wynaut |
| Staravia | 397 | 23 | - | - | Staravia |
| Combee | 415 | 20 | - | - | Combee |
| Pachirisu | 417 | 10 | - | - | Pachirisu |
| Shellos | 422 | 25 | - | - | Shellos |
| Buneary | 427 | 16 | - | - | Buneary |
| Croagunk | 453 | 31 | - | - | Croagunk |
| Finneon | 456 | 35 | - | - | Finneon |
| Snover | 459 | 41 | - | - | Snover |
| Mew | 151 | 50 | - | - | Mew |
| Phione | 489 | 50 | - | - | Phione |

### TradeGift_DPPtIngame, da `Encounters4DPPt.cs`

Tipo di voce `EncounterTrade4PID`, 4 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Abra | 63 | 1 | 0x0000008E | 25643 | Machop -> Abra |
| Chatot | 441 | 1 | 0x00000867 | 44142 | Buizel -> Chatot |
| Haunter | 93 | 35 | 0x00000088 | 19248 | Medicham (35 from Route 217) -> Haunter |
| Magikarp | 129 | 1 | 0x0000045C | 53277 | Finneon -> Magikarp |

### TradeGift_HGSS, da `Encounters4HGSS.cs`

Tipo di voce `EncounterTrade4PID`, 12 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Onix | 95 | 1 | 0x000025EF | 48926 | Bellsprout -> Onix |
| Machop | 66 | 1 | 0x00002310 | 37460 | Drowzee -> Machop |
| Voltorb | 100 | 1 | 0x000001DB | 29189 | Krabby -> Voltorb |
| Dodrio | 85 | 15 | 0x0001FC0A | 00283 | Dragonair (15 from DPPt) -> Dodrio |
| Magneton | 82 | 19 | 0x0000D136 | 50082 | Dugtrio (19 from Diglett's Cave) -> Magneton |
| Xatu | 178 | 16 | 0x000034E4 | 15616 | Haunter (16 from Old Château) -> Xatu |
| Pikachu | 25 | 2 | 0x00485876 | 33038 | Pikachu |
| Beldum | 374 | 31 | 0x0012B6D4 | 23478 | Forretress -> Beldum |
| Rhyhorn | 111 | 1 | 0x0012971C | 06845 | Bonsly -> Rhyhorn w/ Thunder Fang |
| Steelix | 208 | 1 | 0x00101596 | 26491 | Any -> Steelix |
| Spearow | 21 | 20 | 0x00006B5E | 01001 | Webster's Spearow |
| Shuckle | 213 | 20 | 0x000214D7 | 04336 | Kirk's Shuckle |

## Generazione 5

### TradeGift_B2W2, da `Encounters5B2W2.cs`

Tipo di voce `EncounterTrade5B2W2`, 31 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Petilil | 548 | 20 | - | 65217 | Petilil |
| Cottonee | 546 | 20 | - | 71256 | Cottonee |
| Gigalith | 526 | 35 | - | 11195 | Gigalith |
| Tangrowth | 465 | 45 | - | 93194 | Tangrowth |
| Rotom | 479 | 60 | - | 54673 | Rotom |
| Ambipom | 424 | 40 | - | 82610 | Ambipom |
| Alakazam | 65 | 40 | - | 82610 | Alakazam |
| Meowth | 52 | 50 | - | YancyTID | Meowth |
| Wobbuffet | 202 | 50 | - | YancyTID | Wobbuffet |
| Ralts | 280 | 50 | - | YancyTID | Ralts |
| Shieldon | 410 | 50 | - | YancyTID | Shieldon |
| Rhyhorn | 111 | 50 | - | YancyTID | Rhyhorn |
| Shellos | 422 | 50 | - | YancyTID | Shellos-West |
| Mawile | 303 | 50 | - | YancyTID | Mawile |
| Spiritomb | 442 | 50 | - | YancyTID | Spiritomb |
| Snorlax | 143 | 50 | - | YancyTID | Snorlax |
| Teddiursa | 216 | 50 | - | YancyTID | Teddiursa |
| Spinda | 327 | 50 | - | YancyTID | Spinda |
| Togepi | 175 | 50 | - | YancyTID | Togepi |
| Mankey | 56 | 50 | - | CurtisTID | Mankey |
| Wobbuffet | 202 | 50 | - | CurtisTID | Wobbuffet |
| Ralts | 280 | 50 | - | CurtisTID | Ralts |
| Cranidos | 408 | 50 | - | CurtisTID | Cranidos |
| Rhyhorn | 111 | 50 | - | CurtisTID | Rhyhorn |
| Shellos | 422 | 50 | - | CurtisTID | Shellos-East |
| Sableye | 302 | 50 | - | CurtisTID | Sableye |
| Spiritomb | 442 | 50 | - | CurtisTID | Spiritomb |
| Snorlax | 143 | 50 | - | CurtisTID | Snorlax |
| Phanpy | 231 | 50 | - | CurtisTID | Phanpy |
| Spinda | 327 | 50 | - | CurtisTID | Spinda |
| Togepi | 175 | 50 | - | CurtisTID | Togepi |

### TradeGift_W2, da `Encounters5B2W2.cs`

Tipo di voce `EncounterTrade5B2W2`, 1 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Cottonee | 546 | 20 | - | 71256 | Cottonee |

### TradeGift_B2, da `Encounters5B2W2.cs`

Tipo di voce `EncounterTrade5B2W2`, 1 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Petilil | 548 | 20 | - | 65217 | Petilil |

### TradeGift_BW, da `Encounters5BW.cs`

Tipo di voce `EncounterTrade5BW`, 3 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Emolga | 587 | 30 | 0xD400007F | 11195 | Emolga |
| Rotom | 479 | 60 | 0x2A000000 | 54673 | Rotom |
| Munchlax | 446 | 60 | 0x6200001F | 40217 | Munchlax |

### TradeGift_B, da `Encounters5BW.cs`

Tipo di voce `EncounterTrade5BW`, 2 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Petilil | 548 | 15 | 0x64000000 | 39922 | Petilil |
| Basculin | 550 | 25 | 0x9400007F | 27646 | Basculin-Red |

### TradeGift_W, da `Encounters5BW.cs`

Tipo di voce `EncounterTrade5BW`, 2 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Cottonee | 546 | 15 | 0x6400007E | 39922 | Cottonee |
| Basculin | 550 | 25 | 0x9400007F | 27646 | Basculin-Blue |

## Generazione 6

### TradeGift_AO, da `Encounters6AO.cs`

Tipo di voce `EncounterTrade6`, 3 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Makuhita | 296 | 9 | - | 30724 | Makuhita |
| Skitty | 300 | 30 | - | 03239 | Skitty |
| Corsola | 222 | 50 | - | 00325 | Corsola |

### TradeGift_XY, da `Encounters6XY.cs`

Tipo di voce `EncounterTrade6`, 9 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Magikarp | 129 | 5 | - | 44285 | Magikarp |
| Eevee | 133 | 5 | - | 29294 | Eevee |
| Farfetch’d | 83 | 10 | - | 00185 | Farfetch'd |
| Steelix | 208 | 20 | - | 19250 | Steelix |
| Bisharp | 625 | 50 | - | 03447 | Bisharp |
| Froakie | 656 | 5 | - | 00037 | Froakie |
| Chespin | 650 | 5 | - | 00037 | Chespin |
| Fennekin | 653 | 5 | - | 00037 | Fennekin |
| Ralts | 280 | 5 | - | 37110 | Ralts |

## Generazione 7

### TradeGift_GG, da `Encounters7GG.cs`

Tipo di voce `EncounterTrade7b`, 6 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Rattata | 19 | 12 | - | 121106 | Rattata @ Cerulean City, AV rand [0-5) |
| Diglett | 50 | 25 | - | 520159 | Diglett @ Lavender Town, AV rand [0-5) |
| Raichu | 26 | 30 | - | 940711 | Raichu @ Saffron City, AV rand [0-10) |
| Marowak | 105 | 38 | - | 102595 | Marowak @ Fuchsia City, AV rand [0-10) |
| Exeggutor | 103 | 46 | - | 060310 | Exeggutor @ Indigo Plateau, AV rand [0-15) |
| Geodude | 74 | 16 | - | 551873 | Geodude @ Vermilion City, AV rand [0-5) |

### TradeGift_GP, da `Encounters7GG.cs`

Tipo di voce `EncounterTrade7b`, 2 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Sandshrew | 27 | 27 | - | 703019 | Sandshrew @ Celadon City, AV rand [0-5) |
| Grimer | 88 | 44 | - | 000219 | Grimer @ Cinnabar Island, AV rand [0-10) |

### TradeGift_GE, da `Encounters7GG.cs`

Tipo di voce `EncounterTrade7b`, 2 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Vulpix | 37 | 27 | - | 703019 | Vulpix @ Celadon City, AV rand [0-5) |
| Meowth | 52 | 44 | - | 000219 | Meowth @ Cinnabar Island, AV rand [0-10) |

### TradeGift_SM, da `Encounters7SM.cs`

Tipo di voce `EncounterTrade7`, 7 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Machop | 66 | 9 | - | 000410 | Machop |
| Bounsweet | 761 | 16 | - | 610507 | Bounsweet |
| Poliwhirl | 61 | 22 | - | 590916 | Poliwhirl |
| Happiny | 440 | 27 | - | 010913 | Happiny |
| Graveler | 75 | 32 | - | 610602 | Graveler-1 |
| Steenee | 762 | 43 | - | 610503 | Steenee |
| Talonflame | 663 | 59 | - | 581022 | Talonflame |

### TradeGift_USUM, da `Encounters7USUM.cs`

Tipo di voce `EncounterTrade7`, 7 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Hawlucha | 701 | 8 | - | 000410 | Hawlucha |
| Noibat | 714 | 19 | - | 610507 | Noibat |
| Barboach | 339 | 21 | - | 590916 | Barboach |
| Arbok | 24 | 22 | - | 010913 | Arbok |
| Phantump | 708 | 33 | - | 610602 | Phantump |
| Shellos | 422 | 44 | - | 610503 | Shellos |
| Tauros | 128 | 59 | - | 581022 | Tauros |

## Generazione 8

### TradeSWSH, da `Encounters8.cs`

Tipo di voce `EncounterTrade8`, 14 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Meowth | 52 | 18 | - | 263455 | Meowth |
| Skwovet | 819 | 10 | - | 648753 | Skwovet |
| Cottonee | 546 | 23 | - | 101154 | Cottonee |
| Togepi | 175 | 25 | - | 109591 | Togepi |
| Yamask | 562 | 35 | - | 102534 | Yamask |
| Mr. Mime | 122 | 40 | - | 891846 | Mr. Mime |
| Duraludon | 884 | 50 | - | 101141 | Duraludon |
| Meowth | 52 | 15 | - | 101141 | Meowth |
| Mr. Mime | 122 | 15 | - | 101141 | Mr. Mime |
| Zigzagoon | 263 | 15 | - | 101141 | Zigzagoon |
| Stunfisk | 618 | 15 | - | 101141 | Stunfisk |
| Weezing | 110 | 15 | - | 101141 | Weezing |
| Exeggutor | 103 | 15 | - | 101141 | Exeggutor-1 |
| Marowak | 105 | 15 | - | 101141 | Marowak-1 |

### TradeSW, da `Encounters8.cs`

Tipo di voce `EncounterTrade8`, 4 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Hatenna | 856 | 30 | - | 101101 | Hatenna |
| Throh | 538 | 37 | - | 768945 | Throh |
| Farfetch’d | 83 | 15 | - | 101141 | Farfetch’d |
| Darumaka | 554 | 15 | - | 101141 | Darumaka |

### TradeSH, da `Encounters8.cs`

Tipo di voce `EncounterTrade8`, 4 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Impidimp | 859 | 30 | - | 256081 | Impidimp |
| Sawk | 539 | 37 | - | 881426 | Sawk |
| Corsola | 222 | 15 | - | 101141 | Corsola |
| Ponyta | 77 | 15 | - | 101141 | Ponyta |

### TradeGift_BDSP, da `Encounters8b.cs`

Tipo di voce `EncounterTrade8b`, 4 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Abra | 63 | 9 | 0xFF50A8F5 | 25643 | Abra |
| Chatot | 441 | 15 | 0x17DAAB19 | 44142 | Chatot |
| Haunter | 93 | 33 | 0xF60AB5BB | 19248 | Haunter |
| Magikarp | 129 | 45 | 0xFCE82F88 | 53277 | Magikarp |

## Generazione 9

### TradeGift_SV, da `Encounters9.cs`

Tipo di voce `EncounterTrade9`, 33 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Wooper | 194 | 18 | - | 033081 | Wooper |
| Haunter | 93 | 25 | - | 016519 | Haunter |
| Magby | 240 | 12 | - | 418071 | Magby |
| Dudunsparce | 982 | 35 | - | 766634 | Dudunsparce |
| Eevee | 133 | 1 | - | 376983 | Eevee |
| Wooper | 194 | 8 | - | 591912 | Wooper-1 |
| Pawmo | 922 | 24 | - | 209896 | Pawmo |
| Cetoddle | 974 | 37 | - | 209896 | Cetoddle |
| Veluza | 976 | 20 | - | 373015 | Veluza |
| Arctibax | 997 | 45 | - | 316242 | Arctibax |
| Combee | 415 | 15 | - | 993663 | Combee |
| Duraludon | 884 | 36 | - | 217978 | Duraludon |
| Meditite | 307 | 28 | - | 137719 | Meditite |
| Sunflora | 192 | 40 | - | 584457 | Sunflora |
| Mareanie | 747 | 20 | - | 158604 | Mareanie |
| Magnemite | 81 | 22 | - | 568659 | Magnemite |
| Tauros | 128 | 50 | - | 933665 | Tauros-1 |
| Skarmory | 227 | 40 | - | 745642 | Skarmory |
| Glimmet | 969 | 5 | - | 661291 | Glimmet |
| Skwovet | 819 | 7 | - | 105971 | Skwovet |
| Tinkatuff | 958 | 25 | - | 949475 | Tinkatuff |
| Greavard | 971 | 10 | - | 275703 | Greavard |
| Gimmighoul | 999 | 30 | - | 361010 | Gimmighoul |
| Flittle | 955 | 32 | - | 149671 | Flittle |
| Hattrem | 857 | 33 | - | 654886 | Hattrem |
| Meowth | 52 | 21 | - | 314512 | Meowth-1 |
| Blitzle | 522 | 20 | - | 390518 | Blitzle |
| Applin | 840 | 15 | - | 184745 | Applin |
| Snubbull | 209 | 18 | - | 816963 | Snubbull |
| Rockruff | 744 | 12 | - | 980975 | Rockruff |
| Poltchageist | 1012 | 30 | - | 704310 | Poltchageist |
| Gulpin | 316 | 17 | - | 134745 | Gulpin |
| Snom | 872 | 10 | - | 050724 | Snom |

### Trades, da `Encounters9a.cs`

Tipo di voce `EncounterTrade9a`, 5 voci.

| Specie | Dex | Livello | Valore di personalita | Identificativo | Nota della fonte |
|---|---|---|---|---|---|
| Heracross | 214 | 12 | - | 797394 | Heracross (sub_tradepoke_heracros) |
| Riolu | 447 | 25 | - | 348226 | Riolu (sub_tradepoke_riolu) |
| Slowpoke | 79 | 30 | - | 934764 | Slowpoke-1 (sub_addpoke_gyadon) |
| Raichu | 26 | 64 | - | 693489 | Raichu-1 (sub_addpoke_araichu) |
| Porygon2 | 233 | 50 | - | 065536 | Porygon2 (sub_tradepoke_poligon2) |

