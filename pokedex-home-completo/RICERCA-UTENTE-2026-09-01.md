# Pokédex HOME — Elenco completo di specie e forme collezionabili

**Data di generazione:** 1 settembre 2026  
**Riferimento:** Pokémon HOME e giochi ad esso collegati alla data indicata

---

## 0. Come è stato costruito questo documento — e cosa è verificato

Questo elenco **non** è scritto a memoria. È stato generato leggendo direttamente due sorgenti dati:

| Sorgente | Cosa fornisce | Stato |
|---|---|---|
| `PKHeX` (kwsch/PKHeX, `master`, clone del 01/09/2026) — tabelle `personal_gg`, `personal_uu`, `personal_swsh`, `personal_bdsp`, `personal_la`, `personal_sv`, `personal_za` | Presenza della specie nel gioco (`IsPresentInGame`) e numero di forme (`FormCount`) per **ogni** titolo | **Verificato** — dati binari estratti dal repository |
| `PKHeX/Legality/Tables/FormInfo.cs` e `IGigantamaxReadOnly.cs` | Elenco esatto delle forme **solo-battaglia** (Mega, Primal, Zen, ecc.) e delle specie Gigantamax | **Verificato** |
| `smogon/pokemon-showdown` — `data/pokedex.ts` (`master`, 01/09/2026) | Nomi delle forme, `formeOrder`, `cosmeticFormes` | **Verificato** — contiene già le Mega di Legends: Z-A |

**Controllo di validità superato:** il parsing di `personal_swsh` restituisce **664 specie** presenti — cifra che coincide con il totale noto di Spada/Scudo + Isola dell'Armatura + Terre Innevate della Corona. `personal_gg` restituisce 153 (151 di Kanto + Meltan + Melmetal), `personal_bdsp` 493, `personal_uu` 807.

### Cosa NON è verificato in questo documento

- **[Non verificato]** Non posso confermare quali forme Pokémon HOME conti come *voci separate* nel suo Pokédex. HOME potrebbe accorpare o separare forme cosmetiche in modo diverso dalle tabelle interne dei giochi. I conteggi qui riportati sono conteggi di **forme esistenti nei giochi**, non di caselle del Pokédex di HOME.
- **[Non verificato]** L'assegnazione nome↔indice di forma è dedotta dall'ordine `formeOrder` di Showdown. Per 906 specie su 1025 il numero di forme concorda con PKHeX; le discordanze sono quasi tutte imputabili alle forme solo-battaglia (che PKHeX esclude correttamente).
- **La mia base di conoscenze non contiene** un elenco ufficiale delle voci del Pokédex di HOME pubblicato da The Pokémon Company. Non esiste, a mia conoscenza, una fonte primaria consultabile.
- **[Non verificato]** Compatibilità di *Pokémon Champions*, *Pokémon Winds and Waves* e delle versioni Switch di *Rosso Fuoco/Verde Foglia* (aggiornamento HOME 4.1.0 annunciato per ottobre 2026): non incluse nei conteggi perché non presenti nelle tabelle PKHeX analizzate.

---

## 1. Numeri di sintesi

| Metrica | Valore |
|---|---|
| Specie distinte (#1–1025) raggiungibili da almeno un gioco collegato a HOME | **1025 / 1025** |
| Voci-forma **conservabili** totali (unione di tutti i titoli, escluse le forme solo-battaglia) | **1355** |
| Specie #1–1025 non raggiungibili da nessun titolo collegato a HOME | **0** |

Aggiunte da contare a parte (non sono forme nelle tabelle `personal`):

- **Alcremie: 63 combinazioni** (9 creme × 7 decorazioni). Verificato da `Zukan8.cs`, che scrive le voci 0–62 (`deco = 7`, `forms = 9`).
- **Fattore Gigantamax: 32 specie** con interruttore attivabile + **Eternatus** (forma Gmax non attivabile). In Spada/Scudo il Gigantamax è un **flag** sul Pokémon, non una forma. Urshifu ne ha 2 (una per forma).

## 2. Copertura per titolo

| Titolo | Specie presenti | Voci-forma conservabili | Note |
|---|---|---|---|
| Let's Go Pikachu / Eevee | 153 | 182 | Solo Kanto #1–151 + Meltan/Melmetal (regola verificata in `PersonalTable7GG.IsSpeciesInGame`) |
| Ultra Sun / Ultra Moon (→ Bank) | 807 | 1045 | Dex Nazionale #1–807 completo — **unica via per Gen 1–7 non presenti su Switch** |
| Spada / Scudo | 664 | 770 | Base + Isola dell'Armatura + Terre Innevate della Corona |
| Diamante Lucente / Perla Splendente | 493 | 555 | #1–493 |
| Leggende: Arceus | 242 | 317 | Forme di Hisui |
| Scarlatto / Violetto | 733 | 957 | Base + Maschera Turchese + Disco Indaco |
| Leggende: Z-A | 364 | 490 | Base + DLC Mega Dimension (specie max: Gholdengo #1000) |

---
## 3. Enumerazione nominale di tutte le forme non-base

Nomi come compaiono nel dataset Showdown. `#` = numero del Dex Nazionale.

### 3.1 Forme di Alola — 19 voci

| # | Forma |
|---|---|
| 19 | Rattata-Alola |
| 20 | Raticate-Alola |
| 25 | Pikachu-Alola |
| 26 | Raichu-Alola |
| 27 | Sandshrew-Alola |
| 28 | Sandslash-Alola |
| 37 | Vulpix-Alola |
| 38 | Ninetales-Alola |
| 50 | Diglett-Alola |
| 51 | Dugtrio-Alola |
| 52 | Meowth-Alola |
| 53 | Persian-Alola |
| 74 | Geodude-Alola |
| 75 | Graveler-Alola |
| 76 | Golem-Alola |
| 88 | Grimer-Alola |
| 89 | Muk-Alola |
| 103 | Exeggutor-Alola |
| 105 | Marowak-Alola |

### 3.2 Forme di Galar — 20 voci

| # | Forma |
|---|---|
| 52 | Meowth-Galar |
| 77 | Ponyta-Galar |
| 78 | Rapidash-Galar |
| 79 | Slowpoke-Galar |
| 80 | Slowbro-Galar |
| 83 | Farfetch\u2019d-Galar |
| 110 | Weezing-Galar |
| 122 | Mr. Mime-Galar |
| 144 | Articuno-Galar |
| 145 | Zapdos-Galar |
| 146 | Moltres-Galar |
| 199 | Slowking-Galar |
| 222 | Corsola-Galar |
| 263 | Zigzagoon-Galar |
| 264 | Linoone-Galar |
| 554 | Darumaka-Galar |
| 555 | Darmanitan-Galar |
| 555 | Darmanitan-Galar-Zen |
| 562 | Yamask-Galar |
| 618 | Stunfisk-Galar |

### 3.3 Forme di Hisui — 16 voci

| # | Forma |
|---|---|
| 58 | Growlithe-Hisui |
| 59 | Arcanine-Hisui |
| 100 | Voltorb-Hisui |
| 101 | Electrode-Hisui |
| 157 | Typhlosion-Hisui |
| 211 | Qwilfish-Hisui |
| 215 | Sneasel-Hisui |
| 503 | Samurott-Hisui |
| 549 | Lilligant-Hisui |
| 570 | Zorua-Hisui |
| 571 | Zoroark-Hisui |
| 628 | Braviary-Hisui |
| 705 | Sliggoo-Hisui |
| 706 | Goodra-Hisui |
| 713 | Avalugg-Hisui |
| 724 | Decidueye-Hisui |

### 3.4 Forme di Paldea — 4 voci

| # | Forma |
|---|---|
| 128 | Tauros-Paldea-Combat |
| 128 | Tauros-Paldea-Blaze |
| 128 | Tauros-Paldea-Aqua |
| 194 | Wooper-Paldea |

### 3.5 Mega Evoluzioni e forme Archeo — 93 voci

**Non conservabili**: esistono solo in battaglia. Servono però per il *Mega Evolution Pokédex* di HOME. Include le nuove Mega introdotte da Leggende: Z-A.

| # | Forma |
|---|---|
| 3 | Venusaur-Mega |
| 6 | Charizard-Mega-X |
| 6 | Charizard-Mega-Y |
| 9 | Blastoise-Mega |
| 15 | Beedrill-Mega |
| 18 | Pidgeot-Mega |
| 26 | Raichu-Mega-X |
| 26 | Raichu-Mega-Y |
| 36 | Clefable-Mega |
| 65 | Alakazam-Mega |
| 71 | Victreebel-Mega |
| 80 | Slowbro-Mega |
| 94 | Gengar-Mega |
| 115 | Kangaskhan-Mega |
| 121 | Starmie-Mega |
| 127 | Pinsir-Mega |
| 130 | Gyarados-Mega |
| 142 | Aerodactyl-Mega |
| 149 | Dragonite-Mega |
| 150 | Mewtwo-Mega-X |
| 150 | Mewtwo-Mega-Y |
| 154 | Meganium-Mega |
| 160 | Feraligatr-Mega |
| 181 | Ampharos-Mega |
| 208 | Steelix-Mega |
| 212 | Scizor-Mega |
| 214 | Heracross-Mega |
| 227 | Skarmory-Mega |
| 229 | Houndoom-Mega |
| 248 | Tyranitar-Mega |
| 254 | Sceptile-Mega |
| 257 | Blaziken-Mega |
| 260 | Swampert-Mega |
| 282 | Gardevoir-Mega |
| 302 | Sableye-Mega |
| 303 | Mawile-Mega |
| 306 | Aggron-Mega |
| 308 | Medicham-Mega |
| 310 | Manectric-Mega |
| 319 | Sharpedo-Mega |
| 323 | Camerupt-Mega |
| 334 | Altaria-Mega |
| 354 | Banette-Mega |
| 358 | Chimecho-Mega |
| 359 | Absol-Mega |
| 359 | Absol-Mega-Z |
| 362 | Glalie-Mega |
| 373 | Salamence-Mega |
| 376 | Metagross-Mega |
| 380 | Latias-Mega |
| 381 | Latios-Mega |
| 382 | Kyogre-Primal |
| 383 | Groudon-Primal |
| 384 | Rayquaza-Mega |
| 398 | Staraptor-Mega |
| 428 | Lopunny-Mega |
| 445 | Garchomp-Mega |
| 445 | Garchomp-Mega-Z |
| 448 | Lucario-Mega |
| 448 | Lucario-Mega-Z |
| 460 | Abomasnow-Mega |
| 475 | Gallade-Mega |
| 478 | Froslass-Mega |
| 485 | Heatran-Mega |
| 491 | Darkrai-Mega |
| 500 | Emboar-Mega |
| 530 | Excadrill-Mega |
| 531 | Audino-Mega |
| 545 | Scolipede-Mega |
| 560 | Scrafty-Mega |
| 604 | Eelektross-Mega |
| 609 | Chandelure-Mega |
| 623 | Golurk-Mega |
| 652 | Chesnaught-Mega |
| 655 | Delphox-Mega |
| 658 | Greninja-Mega |
| 668 | Pyroar-Mega |
| 670 | Floette-Mega |
| 687 | Malamar-Mega |
| 689 | Barbaracle-Mega |
| 691 | Dragalge-Mega |
| 701 | Hawlucha-Mega |
| 718 | Zygarde-Mega |
| 719 | Diancie-Mega |
| 740 | Crabominable-Mega |
| 768 | Golisopod-Mega |
| 780 | Drampa-Mega |
| 801 | Magearna-Mega |
| 807 | Zeraora-Mega |
| 870 | Falinks-Mega |
| 952 | Scovillain-Mega |
| 970 | Glimmora-Mega |
| 998 | Baxcalibur-Mega |

### 3.6 Forme Gigantamax — 34 voci

In Spada/Scudo il Gigantamax è un **flag** sul Pokémon, non una forma conservabile separata.

| # | Forma |
|---|---|
| 3 | Venusaur-Gmax |
| 6 | Charizard-Gmax |
| 9 | Blastoise-Gmax |
| 12 | Butterfree-Gmax |
| 25 | Pikachu-Gmax |
| 52 | Meowth-Gmax |
| 68 | Machamp-Gmax |
| 94 | Gengar-Gmax |
| 99 | Kingler-Gmax |
| 131 | Lapras-Gmax |
| 133 | Eevee-Gmax |
| 143 | Snorlax-Gmax |
| 569 | Garbodor-Gmax |
| 809 | Melmetal-Gmax |
| 812 | Rillaboom-Gmax |
| 815 | Cinderace-Gmax |
| 818 | Inteleon-Gmax |
| 823 | Corviknight-Gmax |
| 826 | Orbeetle-Gmax |
| 834 | Drednaw-Gmax |
| 839 | Coalossal-Gmax |
| 841 | Flapple-Gmax |
| 842 | Appletun-Gmax |
| 844 | Sandaconda-Gmax |
| 849 | Toxtricity-Gmax |
| 849 | Toxtricity-Low-Key-Gmax |
| 851 | Centiskorch-Gmax |
| 858 | Hatterene-Gmax |
| 861 | Grimmsnarl-Gmax |
| 869 | Alcremie-Gmax |
| 879 | Copperajah-Gmax |
| 884 | Duraludon-Gmax |
| 892 | Urshifu-Gmax |
| 892 | Urshifu-Rapid-Strike-Gmax |

### 3.7 Forme cosmetiche (varianti puramente estetiche)

| # | Specie | Varianti | Elenco |
|---|---|---|---|
| 201 | Unown | 28 | Unown, Unown-B, Unown-C, Unown-D, Unown-E, Unown-F, Unown-G, Unown-H, Unown-I, Unown-J, Unown-K, Unown-L, Unown-M, Unown-N, Unown-O, Unown-P, Unown-Q, Unown-R, Unown-S, Unown-T, Unown-U, Unown-V, Unown-W, Unown-X, Unown-Y, Unown-Z, Unown-Exclamation, Unown-Question |
| 412 | Burmy | 3 | Burmy, Burmy-Sandy, Burmy-Trash |
| 422 | Shellos | 2 | Shellos, Shellos-East |
| 423 | Gastrodon | 2 | Gastrodon, Gastrodon-East |
| 585 | Deerling | 4 | Deerling, Deerling-Summer, Deerling-Autumn, Deerling-Winter |
| 586 | Sawsbuck | 4 | Sawsbuck, Sawsbuck-Summer, Sawsbuck-Autumn, Sawsbuck-Winter |
| 666 | Vivillon | 18 | Vivillon, Vivillon-Archipelago, Vivillon-Continental, Vivillon-Elegant, Vivillon-Garden, Vivillon-High Plains, Vivillon-Icy Snow, Vivillon-Jungle, Vivillon-Marine, Vivillon-Modern, Vivillon-Monsoon, Vivillon-Ocean, Vivillon-Polar, Vivillon-River, Vivillon-Sandstorm, Vivillon-Savanna, Vivillon-Sun, Vivillon-Tundra |
| 669 | Flabébé | 5 | Flabébé, Flabébé-Blue, Flabébé-Orange, Flabébé-White, Flabébé-Yellow |
| 670 | Floette | 5 | Floette, Floette-Blue, Floette-Orange, Floette-White, Floette-Yellow |
| 671 | Florges | 5 | Florges, Florges-Blue, Florges-Orange, Florges-White, Florges-Yellow |
| 676 | Furfrou | 10 | Furfrou, Furfrou-Dandy, Furfrou-Debutante, Furfrou-Diamond, Furfrou-Heart, Furfrou-Kabuki, Furfrou-La Reine, Furfrou-Matron, Furfrou-Pharaoh, Furfrou-Star |
| 774 | Minior | 7 | Minior, Minior-Orange, Minior-Yellow, Minior-Green, Minior-Blue, Minior-Indigo, Minior-Violet |
| 869 | Alcremie | 9 | Alcremie, Alcremie-Ruby-Cream, Alcremie-Matcha-Cream, Alcremie-Mint-Cream, Alcremie-Lemon-Cream, Alcremie-Salted-Cream, Alcremie-Ruby-Swirl, Alcremie-Caramel-Swirl, Alcremie-Rainbow-Swirl |
| 869 | Alcremie | **63** | 9 creme × 7 decorazioni (Fragolina, Bacca, Amore, Stella, Trifoglio, Fiore, Nastro) |

### 3.8 Altre forme alternative (regionali escluse) — 167 voci

Comprende forme permanenti conservabili **e** forme solo-battaglia non-Mega. La colonna *Solo battaglia* indica quelle che non possono esistere fuori dal combattimento.

| # | Forma | Solo battaglia |
|---|---|---|
| 25 | Pikachu-Belle | — |
| 25 | Pikachu-Cosplay | — |
| 25 | Pikachu-Hoenn | — |
| 25 | Pikachu-Kalos | — |
| 25 | Pikachu-Libre | — |
| 25 | Pikachu-Original | — |
| 25 | Pikachu-Partner | — |
| 25 | Pikachu-PhD | — |
| 25 | Pikachu-Pop-Star | — |
| 25 | Pikachu-Rock-Star | — |
| 25 | Pikachu-Sinnoh | — |
| 25 | Pikachu-Starter | — |
| 25 | Pikachu-Unova | — |
| 25 | Pikachu-World | — |
| 133 | Eevee-Starter | — |
| 172 | Pichu-Spiky-eared | — |
| 351 | Castform-Rainy | sì |
| 351 | Castform-Snowy | sì |
| 351 | Castform-Sunny | sì |
| 386 | Deoxys-Attack | — |
| 386 | Deoxys-Defense | — |
| 386 | Deoxys-Speed | — |
| 413 | Wormadam-Sandy | — |
| 413 | Wormadam-Trash | — |
| 421 | Cherrim-Sunshine | sì |
| 479 | Rotom-Fan | — |
| 479 | Rotom-Frost | — |
| 479 | Rotom-Heat | — |
| 479 | Rotom-Mow | — |
| 479 | Rotom-Wash | — |
| 483 | Dialga-Origin | — |
| 484 | Palkia-Origin | — |
| 487 | Giratina-Origin | — |
| 492 | Shaymin-Sky | — |
| 493 | Arceus-Bug | — |
| 493 | Arceus-Dark | — |
| 493 | Arceus-Dragon | — |
| 493 | Arceus-Electric | — |
| 493 | Arceus-Fairy | — |
| 493 | Arceus-Fighting | — |
| 493 | Arceus-Fire | — |
| 493 | Arceus-Flying | — |
| 493 | Arceus-Ghost | — |
| 493 | Arceus-Grass | — |
| 493 | Arceus-Ground | — |
| 493 | Arceus-Ice | — |
| 493 | Arceus-Poison | — |
| 493 | Arceus-Psychic | — |
| 493 | Arceus-Rock | — |
| 493 | Arceus-Steel | — |
| 493 | Arceus-Water | — |
| 550 | Basculin-Blue-Striped | — |
| 550 | Basculin-White-Striped | — |
| 555 | Darmanitan-Zen | sì |
| 641 | Tornadus-Therian | — |
| 642 | Thundurus-Therian | — |
| 645 | Landorus-Therian | — |
| 646 | Kyurem-Black | — |
| 646 | Kyurem-White | — |
| 647 | Keldeo-Resolute | — |
| 648 | Meloetta-Pirouette | sì |
| 649 | Genesect-Burn | — |
| 649 | Genesect-Chill | — |
| 649 | Genesect-Douse | — |
| 649 | Genesect-Shock | — |
| 658 | Greninja-Ash | sì |
| 658 | Greninja-Bond | — |
| 666 | Vivillon-Fancy | — |
| 666 | Vivillon-Pokeball | — |
| 670 | Floette-Eternal | — |
| 678 | Meowstic-F | — |
| 678 | Meowstic-F-Mega | sì |
| 678 | Meowstic-M-Mega | sì |
| 681 | Aegislash-Blade | sì |
| 710 | Pumpkaboo-Large | — |
| 710 | Pumpkaboo-Small | — |
| 710 | Pumpkaboo-Super | — |
| 711 | Gourgeist-Large | — |
| 711 | Gourgeist-Small | — |
| 711 | Gourgeist-Super | — |
| 716 | Xerneas-Neutral | — |
| 718 | Zygarde-10% | — |
| 718 | Zygarde-Complete | sì |
| 720 | Hoopa-Unbound | — |
| 735 | Gumshoos-Totem | — |
| 738 | Vikavolt-Totem | — |
| 741 | Oricorio-Pa'u | — |
| 741 | Oricorio-Pom-Pom | — |
| 741 | Oricorio-Sensu | — |
| 743 | Ribombee-Totem | — |
| 744 | Rockruff-Dusk | — |
| 745 | Lycanroc-Dusk | — |
| 745 | Lycanroc-Midnight | — |
| 746 | Wishiwashi-School | sì |
| 752 | Araquanid-Totem | — |
| 754 | Lurantis-Totem | — |
| 758 | Salazzle-Totem | — |
| 773 | Silvally-Bug | — |
| 773 | Silvally-Dark | — |
| 773 | Silvally-Dragon | — |
| 773 | Silvally-Electric | — |
| 773 | Silvally-Fairy | — |
| 773 | Silvally-Fighting | — |
| 773 | Silvally-Fire | — |
| 773 | Silvally-Flying | — |
| 773 | Silvally-Ghost | — |
| 773 | Silvally-Grass | — |
| 773 | Silvally-Ground | — |
| 773 | Silvally-Ice | — |
| 773 | Silvally-Poison | — |
| 773 | Silvally-Psychic | — |
| 773 | Silvally-Rock | — |
| 773 | Silvally-Steel | — |
| 773 | Silvally-Water | — |
| 774 | Minior-Meteor | sì |
| 777 | Togedemaru-Totem | — |
| 778 | Mimikyu-Busted | sì |
| 778 | Mimikyu-Busted-Totem | sì |
| 778 | Mimikyu-Totem | — |
| 784 | Kommo-o-Totem | — |
| 800 | Necrozma-Dawn-Wings | — |
| 800 | Necrozma-Dusk-Mane | — |
| 800 | Necrozma-Ultra | sì |
| 801 | Magearna-Original | — |
| 801 | Magearna-Original-Mega | sì |
| 845 | Cramorant-Gorging | sì |
| 845 | Cramorant-Gulping | sì |
| 849 | Toxtricity-Low-Key | — |
| 854 | Sinistea-Antique | — |
| 855 | Polteageist-Antique | — |
| 875 | Eiscue-Noice | sì |
| 876 | Indeedee-F | — |
| 877 | Morpeko-Hangry | sì |
| 888 | Zacian-Crowned | sì |
| 889 | Zamazenta-Crowned | sì |
| 890 | Eternatus-Eternamax | — |
| 892 | Urshifu-Rapid-Strike | — |
| 893 | Zarude-Dada | — |
| 898 | Calyrex-Ice | — |
| 898 | Calyrex-Shadow | — |
| 901 | Ursaluna-Bloodmoon | — |
| 902 | Basculegion-F | — |
| 905 | Enamorus-Therian | — |
| 916 | Oinkologne-F | — |
| 925 | Maushold-Four | — |
| 931 | Squawkabilly-Blue | — |
| 931 | Squawkabilly-White | — |
| 931 | Squawkabilly-Yellow | — |
| 964 | Palafin-Hero | sì |
| 978 | Tatsugiri-Curly-Mega | sì |
| 978 | Tatsugiri-Droopy | — |
| 978 | Tatsugiri-Droopy-Mega | sì |
| 978 | Tatsugiri-Stretchy | — |
| 978 | Tatsugiri-Stretchy-Mega | sì |
| 982 | Dudunsparce-Three-Segment | — |
| 999 | Gimmighoul-Roaming | — |
| 1012 | Poltchageist-Artisan | — |
| 1013 | Sinistcha-Masterpiece | — |
| 1017 | Ogerpon-Cornerstone | — |
| 1017 | Ogerpon-Cornerstone-Tera | sì |
| 1017 | Ogerpon-Hearthflame | — |
| 1017 | Ogerpon-Hearthflame-Tera | sì |
| 1017 | Ogerpon-Teal-Tera | sì |
| 1017 | Ogerpon-Wellspring | — |
| 1017 | Ogerpon-Wellspring-Tera | sì |
| 1024 | Terapagos-Stellar | sì |
| 1024 | Terapagos-Terastal | sì |

---
## 4. Tabella completa — Dex Nazionale #1–1025

Legenda colonne titolo: numero di **voci-forma conservabili** presenti in quel titolo (`—` = specie assente).  
`Forme` elenca le forme permanenti diverse dalla base; Mega, Gigantamax e forme solo-battaglia sono escluse (vedi §3).

| # | Specie | Forme cons. | Forme permanenti alternative | LGPE | USUM | SwSh | BDSP | PLA | SV | Z-A |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Bulbasaur | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 2 | Ivysaur | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 3 | Venusaur | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 4 | Charmander | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 5 | Charmeleon | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 6 | Charizard | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 7 | Squirtle | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 8 | Wartortle | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 9 | Blastoise | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 10 | Caterpie | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 11 | Metapod | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 12 | Butterfree | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 13 | Weedle | 1 | — | 1 | 1 | — | 1 | — | — | 1 |
| 14 | Kakuna | 1 | — | 1 | 1 | — | 1 | — | — | 1 |
| 15 | Beedrill | 1 | — | 1 | 1 | — | 1 | — | — | 1 |
| 16 | Pidgey | 1 | — | 1 | 1 | — | 1 | — | — | 1 |
| 17 | Pidgeotto | 1 | — | 1 | 1 | — | 1 | — | — | 1 |
| 18 | Pidgeot | 1 | — | 1 | 1 | — | 1 | — | — | 1 |
| 19 | Rattata | 2 | Rattata-Alola | 2 | 2 | — | 1 | — | — | — |
| 20 | Raticate | 3 | Raticate-Alola | 3 | 3 | — | 1 | — | — | — |
| 21 | Spearow | 1 | — | 1 | 1 | — | 1 | — | — | — |
| 22 | Fearow | 1 | — | 1 | 1 | — | 1 | — | — | — |
| 23 | Ekans | 1 | — | 1 | 1 | — | 1 | — | 1 | 1 |
| 24 | Arbok | 1 | — | 1 | 1 | — | 1 | — | 1 | 1 |
| 25 | Pikachu | 10 | Pikachu-Original, Pikachu-Hoenn, Pikachu-Sinnoh, Pikachu-Unova, Pikachu-Kalos, Pikachu-Alola, Pikachu-Partner, Pikachu-World, Pikachu-Rock-Star, Pikachu-Belle, Pikachu-Pop-Star, Pikachu-PhD, Pikachu-Libre, Pikachu-Cosplay | 9 | 8 | 9 | 1 | 1 | 9 | 1 |
| 26 | Raichu | 2 | Raichu-Alola | 2 | 2 | 2 | 1 | 1 | 2 | 2 |
| 27 | Sandshrew | 2 | Sandshrew-Alola | 2 | 2 | 2 | 1 | — | 2 | — |
| 28 | Sandslash | 2 | Sandslash-Alola | 2 | 2 | 2 | 1 | — | 2 | — |
| 29 | Nidoran♀ | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 30 | Nidorina | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 31 | Nidoqueen | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 32 | Nidoran♂ | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 33 | Nidorino | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 34 | Nidoking | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 35 | Clefairy | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 36 | Clefable | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 37 | Vulpix | 2 | Vulpix-Alola | 2 | 2 | 2 | 1 | 2 | 2 | — |
| 38 | Ninetales | 2 | Ninetales-Alola | 2 | 2 | 2 | 1 | 2 | 2 | — |
| 39 | Jigglypuff | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 40 | Wigglytuff | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 41 | Zubat | 1 | — | 1 | 1 | 1 | 1 | 1 | — | 1 |
| 42 | Golbat | 1 | — | 1 | 1 | 1 | 1 | 1 | — | 1 |
| 43 | Oddish | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 44 | Gloom | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 45 | Vileplume | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 46 | Paras | 1 | — | 1 | 1 | — | 1 | 1 | — | — |
| 47 | Parasect | 1 | — | 1 | 1 | — | 1 | 1 | — | — |
| 48 | Venonat | 1 | — | 1 | 1 | — | 1 | — | 1 | — |
| 49 | Venomoth | 1 | — | 1 | 1 | — | 1 | — | 1 | — |
| 50 | Diglett | 2 | Diglett-Alola | 2 | 2 | 2 | 1 | — | 2 | — |
| 51 | Dugtrio | 2 | Dugtrio-Alola | 2 | 2 | 2 | 1 | — | 2 | — |
| 52 | Meowth | 3 | Meowth-Alola, Meowth-Galar | 2 | 2 | 3 | 1 | — | 3 | 3 |
| 53 | Persian | 2 | Persian-Alola | 2 | 2 | 2 | 1 | — | 2 | 2 |
| 54 | Psyduck | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 55 | Golduck | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 56 | Mankey | 1 | — | 1 | 1 | — | 1 | — | 1 | 1 |
| 57 | Primeape | 1 | — | 1 | 1 | — | 1 | — | 1 | 1 |
| 58 | Growlithe | 2 | Growlithe-Hisui | 1 | 1 | 1 | 1 | 1 | 2 | — |
| 59 | Arcanine | 3 | Arcanine-Hisui | 1 | 1 | 1 | 1 | 2 | 2 | — |
| 60 | Poliwag | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 61 | Poliwhirl | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 62 | Poliwrath | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 63 | Abra | 1 | — | 1 | 1 | 1 | 1 | 1 | — | 1 |
| 64 | Kadabra | 1 | — | 1 | 1 | 1 | 1 | 1 | — | 1 |
| 65 | Alakazam | 1 | — | 1 | 1 | 1 | 1 | 1 | — | 1 |
| 66 | Machop | 1 | — | 1 | 1 | 1 | 1 | 1 | — | 1 |
| 67 | Machoke | 1 | — | 1 | 1 | 1 | 1 | 1 | — | 1 |
| 68 | Machamp | 1 | — | 1 | 1 | 1 | 1 | 1 | — | 1 |
| 69 | Bellsprout | 1 | — | 1 | 1 | — | 1 | — | 1 | 1 |
| 70 | Weepinbell | 1 | — | 1 | 1 | — | 1 | — | 1 | 1 |
| 71 | Victreebel | 1 | — | 1 | 1 | — | 1 | — | 1 | 1 |
| 72 | Tentacool | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 73 | Tentacruel | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 74 | Geodude | 2 | Geodude-Alola | 2 | 2 | — | 1 | 1 | 2 | — |
| 75 | Graveler | 2 | Graveler-Alola | 2 | 2 | — | 1 | 1 | 2 | — |
| 76 | Golem | 2 | Golem-Alola | 2 | 2 | — | 1 | 1 | 2 | — |
| 77 | Ponyta | 2 | Ponyta-Galar | 1 | 1 | 2 | 1 | 1 | — | — |
| 78 | Rapidash | 2 | Rapidash-Galar | 1 | 1 | 2 | 1 | 1 | — | — |
| 79 | Slowpoke | 2 | Slowpoke-Galar | 1 | 1 | 2 | 1 | — | 2 | 2 |
| 80 | Slowbro | 2 | Slowbro-Galar | 1 | 1 | 2 | 1 | — | 2 | 2 |
| 81 | Magnemite | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 82 | Magneton | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 83 | Farfetch’d | 2 | Farfetch\u2019d-Galar | 1 | 1 | 2 | 1 | — | — | 2 |
| 84 | Doduo | 1 | — | 1 | 1 | — | 1 | — | 1 | — |
| 85 | Dodrio | 1 | — | 1 | 1 | — | 1 | — | 1 | — |
| 86 | Seel | 1 | — | 1 | 1 | — | 1 | — | 1 | — |
| 87 | Dewgong | 1 | — | 1 | 1 | — | 1 | — | 1 | — |
| 88 | Grimer | 2 | Grimer-Alola | 2 | 2 | — | 1 | — | 2 | — |
| 89 | Muk | 2 | Muk-Alola | 2 | 2 | — | 1 | — | 2 | — |
| 90 | Shellder | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 91 | Cloyster | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 92 | Gastly | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 93 | Haunter | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 94 | Gengar | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 95 | Onix | 1 | — | 1 | 1 | 1 | 1 | 1 | — | 1 |
| 96 | Drowzee | 1 | — | 1 | 1 | — | 1 | — | 1 | — |
| 97 | Hypno | 1 | — | 1 | 1 | — | 1 | — | 1 | — |
| 98 | Krabby | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 99 | Kingler | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 100 | Voltorb | 2 | Voltorb-Hisui | 1 | 1 | — | 1 | 1 | 2 | — |
| 101 | Electrode | 3 | Electrode-Hisui | 1 | 1 | — | 1 | 2 | 2 | — |
| 102 | Exeggcute | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 103 | Exeggutor | 2 | Exeggutor-Alola | 2 | 2 | 2 | 1 | — | 2 | — |
| 104 | Cubone | 1 | — | 1 | 1 | 1 | 1 | — | — | 1 |
| 105 | Marowak | 3 | Marowak-Alola | 3 | 3 | 2 | 1 | — | — | 2 |
| 106 | Hitmonlee | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 107 | Hitmonchan | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 108 | Lickitung | 1 | — | 1 | 1 | 1 | 1 | 1 | — | — |
| 109 | Koffing | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 110 | Weezing | 2 | Weezing-Galar | 1 | 1 | 2 | 1 | — | 2 | — |
| 111 | Rhyhorn | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 112 | Rhydon | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 113 | Chansey | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 114 | Tangela | 1 | — | 1 | 1 | 1 | 1 | 1 | — | — |
| 115 | Kangaskhan | 1 | — | 1 | 1 | 1 | 1 | — | — | 1 |
| 116 | Horsea | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 117 | Seadra | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 118 | Goldeen | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 119 | Seaking | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 120 | Staryu | 1 | — | 1 | 1 | 1 | 1 | — | — | 1 |
| 121 | Starmie | 1 | — | 1 | 1 | 1 | 1 | — | — | 1 |
| 122 | Mr. Mime | 2 | Mr. Mime-Galar | 1 | 1 | 2 | 1 | 1 | — | 2 |
| 123 | Scyther | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 124 | Jynx | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 125 | Electabuzz | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 126 | Magmar | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 127 | Pinsir | 1 | — | 1 | 1 | 1 | 1 | — | — | 1 |
| 128 | Tauros | 4 | Tauros-Paldea-Combat, Tauros-Paldea-Blaze, Tauros-Paldea-Aqua | 1 | 1 | 1 | 1 | — | 4 | — |
| 129 | Magikarp | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 130 | Gyarados | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 131 | Lapras | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 132 | Ditto | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 133 | Eevee | 2 | — | 2 | 1 | 1 | 1 | 1 | 1 | 1 |
| 134 | Vaporeon | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 135 | Jolteon | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 136 | Flareon | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 137 | Porygon | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 138 | Omanyte | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 139 | Omastar | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 140 | Kabuto | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 141 | Kabutops | 1 | — | 1 | 1 | 1 | 1 | — | — | — |
| 142 | Aerodactyl | 1 | — | 1 | 1 | 1 | 1 | — | — | 1 |
| 143 | Snorlax | 1 | — | 1 | 1 | 1 | 1 | 1 | 1 | — |
| 144 | Articuno | 2 | Articuno-Galar | 1 | 1 | 2 | 1 | — | 2 | — |
| 145 | Zapdos | 2 | Zapdos-Galar | 1 | 1 | 2 | 1 | — | 2 | — |
| 146 | Moltres | 2 | Moltres-Galar | 1 | 1 | 2 | 1 | — | 2 | — |
| 147 | Dratini | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 148 | Dragonair | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 149 | Dragonite | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 150 | Mewtwo | 1 | — | 1 | 1 | 1 | 1 | — | 1 | 1 |
| 151 | Mew | 1 | — | 1 | 1 | 1 | 1 | — | 1 | — |
| 152 | Chikorita | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 153 | Bayleef | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 154 | Meganium | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 155 | Cyndaquil | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 156 | Quilava | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 157 | Typhlosion | 2 | Typhlosion-Hisui | — | 1 | — | 1 | 1 | 2 | — |
| 158 | Totodile | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 159 | Croconaw | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 160 | Feraligatr | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 161 | Sentret | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 162 | Furret | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 163 | Hoothoot | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 164 | Noctowl | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 165 | Ledyba | 1 | — | — | 1 | — | 1 | — | — | — |
| 166 | Ledian | 1 | — | — | 1 | — | 1 | — | — | — |
| 167 | Spinarak | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 168 | Ariados | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 169 | Crobat | 1 | — | — | 1 | 1 | 1 | 1 | — | 1 |
| 170 | Chinchou | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 171 | Lanturn | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 172 | Pichu | 1 | Pichu-Spiky-eared | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 173 | Cleffa | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 174 | Igglybuff | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 175 | Togepi | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 176 | Togetic | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 177 | Natu | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 178 | Xatu | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 179 | Mareep | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 180 | Flaaffy | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 181 | Ampharos | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 182 | Bellossom | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 183 | Marill | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 184 | Azumarill | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 185 | Sudowoodo | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 186 | Politoed | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 187 | Hoppip | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 188 | Skiploom | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 189 | Jumpluff | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 190 | Aipom | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 191 | Sunkern | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 192 | Sunflora | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 193 | Yanma | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 194 | Wooper | 2 | Wooper-Paldea | — | 1 | 1 | 1 | — | 2 | — |
| 195 | Quagsire | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 196 | Espeon | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 197 | Umbreon | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 198 | Murkrow | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 199 | Slowking | 2 | Slowking-Galar | — | 1 | 2 | 1 | — | 2 | 2 |
| 200 | Misdreavus | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 201 | Unown | 28 | Unown-B, Unown-C, Unown-D, Unown-E, Unown-F, Unown-G, Unown-H, Unown-I, Unown-J, Unown-K, Unown-L, Unown-M, Unown-N, Unown-O, Unown-P, Unown-Q, Unown-R, Unown-S, Unown-T, Unown-U, Unown-V, Unown-W, Unown-X, Unown-Y, Unown-Z, Unown-Exclamation, Unown-Question | — | 28 | — | 28 | 28 | — | — |
| 202 | Wobbuffet | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 203 | Girafarig | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 204 | Pineco | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 205 | Forretress | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 206 | Dunsparce | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 207 | Gligar | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 208 | Steelix | 1 | — | — | 1 | 1 | 1 | 1 | — | 1 |
| 209 | Snubbull | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 210 | Granbull | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 211 | Qwilfish | 2 | Qwilfish-Hisui | — | 1 | 1 | 1 | 1 | 2 | 2 |
| 212 | Scizor | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 213 | Shuckle | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 214 | Heracross | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 215 | Sneasel | 2 | Sneasel-Hisui | — | 1 | 1 | 1 | 2 | 2 | — |
| 216 | Teddiursa | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 217 | Ursaring | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 218 | Slugma | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 219 | Magcargo | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 220 | Swinub | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 221 | Piloswine | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 222 | Corsola | 2 | Corsola-Galar | — | 1 | 2 | 1 | — | — | — |
| 223 | Remoraid | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 224 | Octillery | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 225 | Delibird | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 226 | Mantine | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 227 | Skarmory | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 228 | Houndour | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 229 | Houndoom | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 230 | Kingdra | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 231 | Phanpy | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 232 | Donphan | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 233 | Porygon2 | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 234 | Stantler | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 235 | Smeargle | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 236 | Tyrogue | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 237 | Hitmontop | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 238 | Smoochum | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 239 | Elekid | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 240 | Magby | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 241 | Miltank | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 242 | Blissey | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 243 | Raikou | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 244 | Entei | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 245 | Suicune | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 246 | Larvitar | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 247 | Pupitar | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 248 | Tyranitar | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 249 | Lugia | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 250 | Ho-Oh | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 251 | Celebi | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 252 | Treecko | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 253 | Grovyle | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 254 | Sceptile | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 255 | Torchic | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 256 | Combusken | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 257 | Blaziken | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 258 | Mudkip | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 259 | Marshtomp | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 260 | Swampert | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 261 | Poochyena | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 262 | Mightyena | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 263 | Zigzagoon | 2 | Zigzagoon-Galar | — | 1 | 2 | 1 | — | — | — |
| 264 | Linoone | 2 | Linoone-Galar | — | 1 | 2 | 1 | — | — | — |
| 265 | Wurmple | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 266 | Silcoon | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 267 | Beautifly | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 268 | Cascoon | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 269 | Dustox | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 270 | Lotad | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 271 | Lombre | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 272 | Ludicolo | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 273 | Seedot | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 274 | Nuzleaf | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 275 | Shiftry | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 276 | Taillow | 1 | — | — | 1 | — | 1 | — | — | — |
| 277 | Swellow | 1 | — | — | 1 | — | 1 | — | — | — |
| 278 | Wingull | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 279 | Pelipper | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 280 | Ralts | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 281 | Kirlia | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 282 | Gardevoir | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 283 | Surskit | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 284 | Masquerain | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 285 | Shroomish | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 286 | Breloom | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 287 | Slakoth | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 288 | Vigoroth | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 289 | Slaking | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 290 | Nincada | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 291 | Ninjask | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 292 | Shedinja | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 293 | Whismur | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 294 | Loudred | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 295 | Exploud | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 296 | Makuhita | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 297 | Hariyama | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 298 | Azurill | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 299 | Nosepass | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 300 | Skitty | 1 | — | — | 1 | — | 1 | — | — | — |
| 301 | Delcatty | 1 | — | — | 1 | — | 1 | — | — | — |
| 302 | Sableye | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 303 | Mawile | 1 | — | — | 1 | 1 | 1 | — | — | 1 |
| 304 | Aron | 1 | — | — | 1 | 1 | 1 | — | — | 1 |
| 305 | Lairon | 1 | — | — | 1 | 1 | 1 | — | — | 1 |
| 306 | Aggron | 1 | — | — | 1 | 1 | 1 | — | — | 1 |
| 307 | Meditite | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 308 | Medicham | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 309 | Electrike | 1 | — | — | 1 | 1 | 1 | — | — | 1 |
| 310 | Manectric | 1 | — | — | 1 | 1 | 1 | — | — | 1 |
| 311 | Plusle | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 312 | Minun | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 313 | Volbeat | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 314 | Illumise | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 315 | Roselia | 1 | — | — | 1 | 1 | 1 | 1 | — | 1 |
| 316 | Gulpin | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 317 | Swalot | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 318 | Carvanha | 1 | — | — | 1 | 1 | 1 | — | — | 1 |
| 319 | Sharpedo | 1 | — | — | 1 | 1 | 1 | — | — | 1 |
| 320 | Wailmer | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 321 | Wailord | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 322 | Numel | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 323 | Camerupt | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 324 | Torkoal | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 325 | Spoink | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 326 | Grumpig | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 327 | Spinda | 1 | — | — | 1 | — | 1 | — | — | — |
| 328 | Trapinch | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 329 | Vibrava | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 330 | Flygon | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 331 | Cacnea | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 332 | Cacturne | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 333 | Swablu | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 334 | Altaria | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 335 | Zangoose | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 336 | Seviper | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 337 | Lunatone | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 338 | Solrock | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 339 | Barboach | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 340 | Whiscash | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 341 | Corphish | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 342 | Crawdaunt | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 343 | Baltoy | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 344 | Claydol | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 345 | Lileep | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 346 | Cradily | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 347 | Anorith | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 348 | Armaldo | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 349 | Feebas | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 350 | Milotic | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 351 | Castform | 1 | — | — | 1 | — | 1 | — | — | — |
| 352 | Kecleon | 1 | — | — | 1 | — | 1 | — | — | 1 |
| 353 | Shuppet | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 354 | Banette | 1 | — | — | 1 | — | 1 | — | 1 | 1 |
| 355 | Duskull | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 356 | Dusclops | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 357 | Tropius | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 358 | Chimecho | 1 | — | — | 1 | — | 1 | 1 | 1 | 1 |
| 359 | Absol | 1 | — | — | 1 | 1 | 1 | — | — | 1 |
| 360 | Wynaut | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 361 | Snorunt | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 362 | Glalie | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 363 | Spheal | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 364 | Sealeo | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 365 | Walrein | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 366 | Clamperl | 1 | — | — | 1 | — | 1 | — | — | — |
| 367 | Huntail | 1 | — | — | 1 | — | 1 | — | — | — |
| 368 | Gorebyss | 1 | — | — | 1 | — | 1 | — | — | — |
| 369 | Relicanth | 1 | — | — | 1 | 1 | 1 | — | — | — |
| 370 | Luvdisc | 1 | — | — | 1 | — | 1 | — | 1 | — |
| 371 | Bagon | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 372 | Shelgon | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 373 | Salamence | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 374 | Beldum | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 375 | Metang | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 376 | Metagross | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 377 | Regirock | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 378 | Regice | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 379 | Registeel | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 380 | Latias | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 381 | Latios | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 382 | Kyogre | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 383 | Groudon | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 384 | Rayquaza | 1 | — | — | 1 | 1 | 1 | — | 1 | 1 |
| 385 | Jirachi | 1 | — | — | 1 | 1 | 1 | — | 1 | — |
| 386 | Deoxys | 4 | Deoxys-Attack, Deoxys-Defense, Deoxys-Speed | — | 4 | — | 4 | — | 4 | — |
| 387 | Turtwig | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 388 | Grotle | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 389 | Torterra | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 390 | Chimchar | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 391 | Monferno | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 392 | Infernape | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 393 | Piplup | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 394 | Prinplup | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 395 | Empoleon | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 396 | Starly | 1 | — | — | 1 | — | 1 | 1 | 1 | 1 |
| 397 | Staravia | 1 | — | — | 1 | — | 1 | 1 | 1 | 1 |
| 398 | Staraptor | 1 | — | — | 1 | — | 1 | 1 | 1 | 1 |
| 399 | Bidoof | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 400 | Bibarel | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 401 | Kricketot | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 402 | Kricketune | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 403 | Shinx | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 404 | Luxio | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 405 | Luxray | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 406 | Budew | 1 | — | — | 1 | 1 | 1 | 1 | — | 1 |
| 407 | Roserade | 1 | — | — | 1 | 1 | 1 | 1 | — | 1 |
| 408 | Cranidos | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 409 | Rampardos | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 410 | Shieldon | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 411 | Bastiodon | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 412 | Burmy | 3 | Burmy-Sandy, Burmy-Trash | — | 3 | — | 3 | 3 | — | — |
| 413 | Wormadam | 3 | Wormadam-Sandy, Wormadam-Trash | — | 3 | — | 3 | 3 | — | — |
| 414 | Mothim | 3 | — | — | 3 | — | 3 | 3 | — | — |
| 415 | Combee | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 416 | Vespiquen | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 417 | Pachirisu | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 418 | Buizel | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 419 | Floatzel | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 420 | Cherubi | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 421 | Cherrim | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 422 | Shellos | 2 | Shellos-East | — | 2 | 2 | 2 | 2 | 2 | — |
| 423 | Gastrodon | 2 | Gastrodon-East | — | 2 | 2 | 2 | 2 | 2 | — |
| 424 | Ambipom | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 425 | Drifloon | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 426 | Drifblim | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 427 | Buneary | 1 | — | — | 1 | 1 | 1 | 1 | — | 1 |
| 428 | Lopunny | 1 | — | — | 1 | 1 | 1 | 1 | — | 1 |
| 429 | Mismagius | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 430 | Honchkrow | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 431 | Glameow | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 432 | Purugly | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 433 | Chingling | 1 | — | — | 1 | — | 1 | 1 | 1 | 1 |
| 434 | Stunky | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 435 | Skuntank | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 436 | Bronzor | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 437 | Bronzong | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 438 | Bonsly | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 439 | Mime Jr. | 1 | — | — | 1 | 1 | 1 | 1 | — | 1 |
| 440 | Happiny | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 441 | Chatot | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 442 | Spiritomb | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 443 | Gible | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 444 | Gabite | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 445 | Garchomp | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 446 | Munchlax | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 447 | Riolu | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 448 | Lucario | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 449 | Hippopotas | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 450 | Hippowdon | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 451 | Skorupi | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 452 | Drapion | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 453 | Croagunk | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 454 | Toxicroak | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 455 | Carnivine | 1 | — | — | 1 | — | 1 | 1 | — | — |
| 456 | Finneon | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 457 | Lumineon | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 458 | Mantyke | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 459 | Snover | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 460 | Abomasnow | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 461 | Weavile | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 462 | Magnezone | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 463 | Lickilicky | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 464 | Rhyperior | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 465 | Tangrowth | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 466 | Electivire | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 467 | Magmortar | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 468 | Togekiss | 1 | — | — | 1 | 1 | 1 | 1 | — | — |
| 469 | Yanmega | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 470 | Leafeon | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 471 | Glaceon | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 472 | Gliscor | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 473 | Mamoswine | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 474 | Porygon-Z | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 475 | Gallade | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 476 | Probopass | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 477 | Dusknoir | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 478 | Froslass | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 479 | Rotom | 6 | Rotom-Heat, Rotom-Wash, Rotom-Frost, Rotom-Fan, Rotom-Mow | — | 6 | 6 | 6 | 6 | 6 | 6 |
| 480 | Uxie | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 481 | Mesprit | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 482 | Azelf | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 483 | Dialga | 2 | Dialga-Origin | — | 1 | 1 | 1 | 2 | 2 | — |
| 484 | Palkia | 2 | Palkia-Origin | — | 1 | 1 | 1 | 2 | 2 | — |
| 485 | Heatran | 1 | — | — | 1 | 1 | 1 | 1 | 1 | 1 |
| 486 | Regigigas | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 487 | Giratina | 2 | Giratina-Origin | — | 2 | 2 | 2 | 2 | 2 | — |
| 488 | Cresselia | 1 | — | — | 1 | 1 | 1 | 1 | 1 | — |
| 489 | Phione | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 490 | Manaphy | 1 | — | — | 1 | — | 1 | 1 | 1 | — |
| 491 | Darkrai | 1 | — | — | 1 | — | 1 | 1 | 1 | 1 |
| 492 | Shaymin | 2 | Shaymin-Sky | — | 2 | — | 2 | 2 | 2 | — |
| 493 | Arceus | 19 | Arceus-Fighting, Arceus-Flying, Arceus-Poison, Arceus-Ground, Arceus-Rock, Arceus-Bug, Arceus-Ghost, Arceus-Steel, Arceus-Fire, Arceus-Water, Arceus-Grass, Arceus-Electric, Arceus-Psychic, Arceus-Ice, Arceus-Dragon, Arceus-Dark, Arceus-Fairy | — | 18 | — | 18 | 19 | 18 | — |
| 494 | Victini | 1 | — | — | 1 | 1 | — | — | — | — |
| 495 | Snivy | 1 | — | — | 1 | — | — | — | 1 | — |
| 496 | Servine | 1 | — | — | 1 | — | — | — | 1 | — |
| 497 | Serperior | 1 | — | — | 1 | — | — | — | 1 | — |
| 498 | Tepig | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 499 | Pignite | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 500 | Emboar | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 501 | Oshawott | 1 | — | — | 1 | — | — | 1 | 1 | — |
| 502 | Dewott | 1 | — | — | 1 | — | — | 1 | 1 | — |
| 503 | Samurott | 2 | Samurott-Hisui | — | 1 | — | — | 1 | 2 | — |
| 504 | Patrat | 1 | — | — | 1 | — | — | — | — | 1 |
| 505 | Watchog | 1 | — | — | 1 | — | — | — | — | 1 |
| 506 | Lillipup | 1 | — | — | 1 | 1 | — | — | — | — |
| 507 | Herdier | 1 | — | — | 1 | 1 | — | — | — | — |
| 508 | Stoutland | 1 | — | — | 1 | 1 | — | — | — | — |
| 509 | Purrloin | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 510 | Liepard | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 511 | Pansage | 1 | — | — | 1 | — | — | — | — | 1 |
| 512 | Simisage | 1 | — | — | 1 | — | — | — | — | 1 |
| 513 | Pansear | 1 | — | — | 1 | — | — | — | — | 1 |
| 514 | Simisear | 1 | — | — | 1 | — | — | — | — | 1 |
| 515 | Panpour | 1 | — | — | 1 | — | — | — | — | 1 |
| 516 | Simipour | 1 | — | — | 1 | — | — | — | — | 1 |
| 517 | Munna | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 518 | Musharna | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 519 | Pidove | 1 | — | — | 1 | 1 | — | — | — | — |
| 520 | Tranquill | 1 | — | — | 1 | 1 | — | — | — | — |
| 521 | Unfezant | 1 | — | — | 1 | 1 | — | — | — | — |
| 522 | Blitzle | 1 | — | — | 1 | — | — | — | 1 | — |
| 523 | Zebstrika | 1 | — | — | 1 | — | — | — | 1 | — |
| 524 | Roggenrola | 1 | — | — | 1 | 1 | — | — | — | — |
| 525 | Boldore | 1 | — | — | 1 | 1 | — | — | — | — |
| 526 | Gigalith | 1 | — | — | 1 | 1 | — | — | — | — |
| 527 | Woobat | 1 | — | — | 1 | 1 | — | — | — | — |
| 528 | Swoobat | 1 | — | — | 1 | 1 | — | — | — | — |
| 529 | Drilbur | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 530 | Excadrill | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 531 | Audino | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 532 | Timburr | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 533 | Gurdurr | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 534 | Conkeldurr | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 535 | Tympole | 1 | — | — | 1 | 1 | — | — | — | — |
| 536 | Palpitoad | 1 | — | — | 1 | 1 | — | — | — | — |
| 537 | Seismitoad | 1 | — | — | 1 | 1 | — | — | — | — |
| 538 | Throh | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 539 | Sawk | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 540 | Sewaddle | 1 | — | — | 1 | — | — | — | 1 | — |
| 541 | Swadloon | 1 | — | — | 1 | — | — | — | 1 | — |
| 542 | Leavanny | 1 | — | — | 1 | — | — | — | 1 | — |
| 543 | Venipede | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 544 | Whirlipede | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 545 | Scolipede | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 546 | Cottonee | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 547 | Whimsicott | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 548 | Petilil | 1 | — | — | 1 | 1 | — | 1 | 1 | — |
| 549 | Lilligant | 3 | Lilligant-Hisui | — | 1 | 1 | — | 2 | 2 | — |
| 550 | Basculin | 3 | Basculin-Blue-Striped, Basculin-White-Striped | — | 2 | 2 | — | 1 | 3 | — |
| 551 | Sandile | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 552 | Krokorok | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 553 | Krookodile | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 554 | Darumaka | 2 | Darumaka-Galar | — | 1 | 2 | — | — | — | — |
| 555 | Darmanitan | 2 | Darmanitan-Galar | — | 1 | 2 | — | — | — | — |
| 556 | Maractus | 1 | — | — | 1 | 1 | — | — | — | — |
| 557 | Dwebble | 1 | — | — | 1 | 1 | — | — | — | — |
| 558 | Crustle | 1 | — | — | 1 | 1 | — | — | — | — |
| 559 | Scraggy | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 560 | Scrafty | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 561 | Sigilyph | 1 | — | — | 1 | 1 | — | — | — | — |
| 562 | Yamask | 2 | Yamask-Galar | — | 1 | 2 | — | — | — | 2 |
| 563 | Cofagrigus | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 564 | Tirtouga | 1 | — | — | 1 | 1 | — | — | — | — |
| 565 | Carracosta | 1 | — | — | 1 | 1 | — | — | — | — |
| 566 | Archen | 1 | — | — | 1 | 1 | — | — | — | — |
| 567 | Archeops | 1 | — | — | 1 | 1 | — | — | — | — |
| 568 | Trubbish | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 569 | Garbodor | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 570 | Zorua | 2 | Zorua-Hisui | — | 1 | 1 | — | 1 | 2 | — |
| 571 | Zoroark | 2 | Zoroark-Hisui | — | 1 | 1 | — | 1 | 2 | — |
| 572 | Minccino | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 573 | Cinccino | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 574 | Gothita | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 575 | Gothorita | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 576 | Gothitelle | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 577 | Solosis | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 578 | Duosion | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 579 | Reuniclus | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 580 | Ducklett | 1 | — | — | 1 | — | — | — | 1 | — |
| 581 | Swanna | 1 | — | — | 1 | — | — | — | 1 | — |
| 582 | Vanillite | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 583 | Vanillish | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 584 | Vanilluxe | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 585 | Deerling | 4 | Deerling-Summer, Deerling-Autumn, Deerling-Winter | — | 4 | — | — | — | 4 | — |
| 586 | Sawsbuck | 4 | Sawsbuck-Summer, Sawsbuck-Autumn, Sawsbuck-Winter | — | 4 | — | — | — | 4 | — |
| 587 | Emolga | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 588 | Karrablast | 1 | — | — | 1 | 1 | — | — | — | — |
| 589 | Escavalier | 1 | — | — | 1 | 1 | — | — | — | — |
| 590 | Foongus | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 591 | Amoonguss | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 592 | Frillish | 1 | — | — | 1 | 1 | — | — | — | — |
| 593 | Jellicent | 1 | — | — | 1 | 1 | — | — | — | — |
| 594 | Alomomola | 1 | — | — | 1 | — | — | — | 1 | — |
| 595 | Joltik | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 596 | Galvantula | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 597 | Ferroseed | 1 | — | — | 1 | 1 | — | — | — | — |
| 598 | Ferrothorn | 1 | — | — | 1 | 1 | — | — | — | — |
| 599 | Klink | 1 | — | — | 1 | 1 | — | — | — | — |
| 600 | Klang | 1 | — | — | 1 | 1 | — | — | — | — |
| 601 | Klinklang | 1 | — | — | 1 | 1 | — | — | — | — |
| 602 | Tynamo | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 603 | Eelektrik | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 604 | Eelektross | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 605 | Elgyem | 1 | — | — | 1 | 1 | — | — | — | — |
| 606 | Beheeyem | 1 | — | — | 1 | 1 | — | — | — | — |
| 607 | Litwick | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 608 | Lampent | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 609 | Chandelure | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 610 | Axew | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 611 | Fraxure | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 612 | Haxorus | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 613 | Cubchoo | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 614 | Beartic | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 615 | Cryogonal | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 616 | Shelmet | 1 | — | — | 1 | 1 | — | — | — | — |
| 617 | Accelgor | 1 | — | — | 1 | 1 | — | — | — | — |
| 618 | Stunfisk | 2 | Stunfisk-Galar | — | 1 | 2 | — | — | — | 2 |
| 619 | Mienfoo | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 620 | Mienshao | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 621 | Druddigon | 1 | — | — | 1 | 1 | — | — | — | — |
| 622 | Golett | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 623 | Golurk | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 624 | Pawniard | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 625 | Bisharp | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 626 | Bouffalant | 1 | — | — | 1 | 1 | — | — | — | — |
| 627 | Rufflet | 1 | — | — | 1 | 1 | — | 1 | 1 | — |
| 628 | Braviary | 2 | Braviary-Hisui | — | 1 | 1 | — | 1 | 2 | — |
| 629 | Vullaby | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 630 | Mandibuzz | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 631 | Heatmor | 1 | — | — | 1 | 1 | — | — | — | — |
| 632 | Durant | 1 | — | — | 1 | 1 | — | — | — | — |
| 633 | Deino | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 634 | Zweilous | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 635 | Hydreigon | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 636 | Larvesta | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 637 | Volcarona | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 638 | Cobalion | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 639 | Terrakion | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 640 | Virizion | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 641 | Tornadus | 2 | Tornadus-Therian | — | 2 | 2 | — | 2 | 2 | — |
| 642 | Thundurus | 2 | Thundurus-Therian | — | 2 | 2 | — | 2 | 2 | — |
| 643 | Reshiram | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 644 | Zekrom | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 645 | Landorus | 2 | Landorus-Therian | — | 2 | 2 | — | 2 | 2 | — |
| 646 | Kyurem | 3 | Kyurem-White, Kyurem-Black | — | 3 | 3 | — | — | 3 | — |
| 647 | Keldeo | 2 | Keldeo-Resolute | — | 2 | 2 | — | — | 2 | 2 |
| 648 | Meloetta | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 649 | Genesect | 5 | Genesect-Douse, Genesect-Shock, Genesect-Burn, Genesect-Chill | — | 5 | 5 | — | — | — | 5 |
| 650 | Chespin | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 651 | Quilladin | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 652 | Chesnaught | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 653 | Fennekin | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 654 | Braixen | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 655 | Delphox | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 656 | Froakie | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 657 | Frogadier | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 658 | Greninja | 2 | Greninja-Bond | — | 2 | — | — | — | 2 | 2 |
| 659 | Bunnelby | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 660 | Diggersby | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 661 | Fletchling | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 662 | Fletchinder | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 663 | Talonflame | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 664 | Scatterbug | 20 | — | — | 20 | — | — | — | 20 | 20 |
| 665 | Spewpa | 20 | — | — | 20 | — | — | — | 20 | 20 |
| 666 | Vivillon | 20 | Vivillon-Polar, Vivillon-Tundra, Vivillon-Continental, Vivillon-Garden, Vivillon-Elegant, Vivillon, Vivillon-Modern, Vivillon-Marine, Vivillon-Archipelago, Vivillon-High Plains, Vivillon-Sandstorm, Vivillon-River, Vivillon-Monsoon, Vivillon-Savanna, Vivillon-Sun, Vivillon-Ocean, Vivillon-Jungle, Vivillon-Fancy, Vivillon-Pokeball | — | 20 | — | — | — | 20 | 20 |
| 667 | Litleo | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 668 | Pyroar | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 669 | Flabébé | 5 | Flabébé-Yellow, Flabébé-Orange, Flabébé-Blue, Flabébé-White | — | 5 | — | — | — | 5 | 5 |
| 670 | Floette | 6 | Floette-Yellow, Floette-Orange, Floette-Blue, Floette-White, Floette-Eternal | — | 6 | — | — | — | 5 | 6 |
| 671 | Florges | 5 | Florges-Yellow, Florges-Orange, Florges-Blue, Florges-White | — | 5 | — | — | — | 5 | 5 |
| 672 | Skiddo | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 673 | Gogoat | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 674 | Pancham | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 675 | Pangoro | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 676 | Furfrou | 10 | Furfrou-Heart, Furfrou-Star, Furfrou-Diamond, Furfrou-Debutante, Furfrou-Matron, Furfrou-Dandy, Furfrou-La Reine, Furfrou-Kabuki, Furfrou-Pharaoh | — | 10 | — | — | — | — | 10 |
| 677 | Espurr | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 678 | Meowstic | 2 | Meowstic-F | — | 2 | 2 | — | — | 2 | 2 |
| 679 | Honedge | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 680 | Doublade | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 681 | Aegislash | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 682 | Spritzee | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 683 | Aromatisse | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 684 | Swirlix | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 685 | Slurpuff | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 686 | Inkay | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 687 | Malamar | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 688 | Binacle | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 689 | Barbaracle | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 690 | Skrelp | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 691 | Dragalge | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 692 | Clauncher | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 693 | Clawitzer | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 694 | Helioptile | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 695 | Heliolisk | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 696 | Tyrunt | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 697 | Tyrantrum | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 698 | Amaura | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 699 | Aurorus | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 700 | Sylveon | 1 | — | — | 1 | 1 | — | 1 | 1 | 1 |
| 701 | Hawlucha | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 702 | Dedenne | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 703 | Carbink | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 704 | Goomy | 1 | — | — | 1 | 1 | — | 1 | 1 | 1 |
| 705 | Sliggoo | 2 | Sliggoo-Hisui | — | 1 | 1 | — | 1 | 2 | 2 |
| 706 | Goodra | 2 | Goodra-Hisui | — | 1 | 1 | — | 1 | 2 | 2 |
| 707 | Klefki | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 708 | Phantump | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 709 | Trevenant | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 710 | Pumpkaboo | 4 | Pumpkaboo-Small, Pumpkaboo-Large, Pumpkaboo-Super | — | 4 | 4 | — | — | — | 4 |
| 711 | Gourgeist | 4 | Gourgeist-Small, Gourgeist-Large, Gourgeist-Super | — | 4 | 4 | — | — | — | 4 |
| 712 | Bergmite | 1 | — | — | 1 | 1 | — | 1 | 1 | 1 |
| 713 | Avalugg | 3 | Avalugg-Hisui | — | 1 | 1 | — | 2 | 2 | 2 |
| 714 | Noibat | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 715 | Noivern | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 716 | Xerneas | 1 | Xerneas | — | 1 | 1 | — | — | — | 1 |
| 717 | Yveltal | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 718 | Zygarde | 4 | Zygarde-10%, Zygarde-10%, Zygarde | — | 4 | 4 | — | — | — | 4 |
| 719 | Diancie | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 720 | Hoopa | 2 | Hoopa-Unbound | — | 2 | — | — | — | 2 | 2 |
| 721 | Volcanion | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 722 | Rowlet | 1 | — | — | 1 | 1 | — | 1 | 1 | — |
| 723 | Dartrix | 1 | — | — | 1 | 1 | — | 1 | 1 | — |
| 724 | Decidueye | 2 | Decidueye-Hisui | — | 1 | 1 | — | 1 | 2 | — |
| 725 | Litten | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 726 | Torracat | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 727 | Incineroar | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 728 | Popplio | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 729 | Brionne | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 730 | Primarina | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 731 | Pikipek | 1 | — | — | 1 | — | — | — | 1 | — |
| 732 | Trumbeak | 1 | — | — | 1 | — | — | — | 1 | — |
| 733 | Toucannon | 1 | — | — | 1 | — | — | — | 1 | — |
| 734 | Yungoos | 1 | — | — | 1 | — | — | — | 1 | — |
| 735 | Gumshoos | 2 | — | — | 2 | — | — | — | 1 | — |
| 736 | Grubbin | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 737 | Charjabug | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 738 | Vikavolt | 2 | — | — | 2 | 1 | — | — | 1 | — |
| 739 | Crabrawler | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 740 | Crabominable | 1 | — | — | 1 | — | — | — | 1 | 1 |
| 741 | Oricorio | 4 | Oricorio-Pom-Pom, Oricorio-Pa'u, Oricorio-Sensu | — | 4 | — | — | — | 4 | — |
| 742 | Cutiefly | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 743 | Ribombee | 2 | — | — | 2 | 1 | — | — | 1 | — |
| 744 | Rockruff | 2 | Rockruff-Dusk | — | 2 | 2 | — | — | 2 | — |
| 745 | Lycanroc | 3 | Lycanroc-Midnight, Lycanroc-Dusk | — | 3 | 3 | — | — | 3 | — |
| 746 | Wishiwashi | 1 | — | — | 1 | 1 | — | — | — | — |
| 747 | Mareanie | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 748 | Toxapex | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 749 | Mudbray | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 750 | Mudsdale | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 751 | Dewpider | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 752 | Araquanid | 2 | — | — | 2 | 1 | — | — | 1 | — |
| 753 | Fomantis | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 754 | Lurantis | 2 | — | — | 2 | 1 | — | — | 1 | — |
| 755 | Morelull | 1 | — | — | 1 | 1 | — | — | — | — |
| 756 | Shiinotic | 1 | — | — | 1 | 1 | — | — | — | — |
| 757 | Salandit | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 758 | Salazzle | 2 | — | — | 2 | 1 | — | — | 1 | — |
| 759 | Stufful | 1 | — | — | 1 | 1 | — | — | — | — |
| 760 | Bewear | 1 | — | — | 1 | 1 | — | — | — | — |
| 761 | Bounsweet | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 762 | Steenee | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 763 | Tsareena | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 764 | Comfey | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 765 | Oranguru | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 766 | Passimian | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 767 | Wimpod | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 768 | Golisopod | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 769 | Sandygast | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 770 | Palossand | 1 | — | — | 1 | 1 | — | — | 1 | 1 |
| 771 | Pyukumuku | 1 | — | — | 1 | 1 | — | — | — | — |
| 772 | Type: Null | 1 | — | — | 1 | 1 | — | — | — | — |
| 773 | Silvally | 18 | Silvally-Fighting, Silvally-Flying, Silvally-Poison, Silvally-Ground, Silvally-Rock, Silvally-Bug, Silvally-Ghost, Silvally-Steel, Silvally-Fire, Silvally-Water, Silvally-Grass, Silvally-Electric, Silvally-Psychic, Silvally-Ice, Silvally-Dragon, Silvally-Dark, Silvally-Fairy | — | 18 | 18 | — | — | — | — |
| 774 | Minior | 7 | Minior-Meteor, Minior-Meteor, Minior-Meteor, Minior-Meteor, Minior-Meteor, Minior-Meteor, Minior, Minior-Orange, Minior-Yellow, Minior-Green, Minior-Blue, Minior-Indigo, Minior-Violet | — | 7 | — | — | — | 7 | — |
| 775 | Komala | 1 | — | — | 1 | — | — | — | 1 | — |
| 776 | Turtonator | 1 | — | — | 1 | 1 | — | — | — | — |
| 777 | Togedemaru | 2 | — | — | 2 | 1 | — | — | — | — |
| 778 | Mimikyu | 2 | — | — | 2 | 1 | — | — | 1 | 1 |
| 779 | Bruxish | 1 | — | — | 1 | — | — | — | 1 | — |
| 780 | Drampa | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 781 | Dhelmise | 1 | — | — | 1 | 1 | — | — | — | — |
| 782 | Jangmo-o | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 783 | Hakamo-o | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 784 | Kommo-o | 2 | — | — | 2 | 1 | — | — | 1 | — |
| 785 | Tapu Koko | 1 | — | — | 1 | 1 | — | — | — | — |
| 786 | Tapu Lele | 1 | — | — | 1 | 1 | — | — | — | — |
| 787 | Tapu Bulu | 1 | — | — | 1 | 1 | — | — | — | — |
| 788 | Tapu Fini | 1 | — | — | 1 | 1 | — | — | — | — |
| 789 | Cosmog | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 790 | Cosmoem | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 791 | Solgaleo | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 792 | Lunala | 1 | — | — | 1 | 1 | — | — | 1 | — |
| 793 | Nihilego | 1 | — | — | 1 | 1 | — | — | — | — |
| 794 | Buzzwole | 1 | — | — | 1 | 1 | — | — | — | — |
| 795 | Pheromosa | 1 | — | — | 1 | 1 | — | — | — | — |
| 796 | Xurkitree | 1 | — | — | 1 | 1 | — | — | — | — |
| 797 | Celesteela | 1 | — | — | 1 | 1 | — | — | — | — |
| 798 | Kartana | 1 | — | — | 1 | 1 | — | — | — | — |
| 799 | Guzzlord | 1 | — | — | 1 | 1 | — | — | — | — |
| 800 | Necrozma | 3 | Necrozma-Dusk-Mane, Necrozma-Dawn-Wings | — | 3 | 3 | — | — | 3 | — |
| 801 | Magearna | 2 | Magearna-Original | — | 2 | 2 | — | — | 2 | 2 |
| 802 | Marshadow | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 803 | Poipole | 1 | — | — | 1 | 1 | — | — | — | — |
| 804 | Naganadel | 1 | — | — | 1 | 1 | — | — | — | — |
| 805 | Stakataka | 1 | — | — | 1 | 1 | — | — | — | — |
| 806 | Blacephalon | 1 | — | — | 1 | 1 | — | — | — | — |
| 807 | Zeraora | 1 | — | — | 1 | 1 | — | — | — | 1 |
| 808 | Meltan | 1 | — | 1 | — | 1 | — | — | — | 1 |
| 809 | Melmetal | 1 | — | 1 | — | 1 | — | — | — | 1 |
| 810 | Grookey | 1 | — | — | — | 1 | — | — | 1 | — |
| 811 | Thwackey | 1 | — | — | — | 1 | — | — | 1 | — |
| 812 | Rillaboom | 1 | — | — | — | 1 | — | — | 1 | — |
| 813 | Scorbunny | 1 | — | — | — | 1 | — | — | 1 | — |
| 814 | Raboot | 1 | — | — | — | 1 | — | — | 1 | — |
| 815 | Cinderace | 1 | — | — | — | 1 | — | — | 1 | — |
| 816 | Sobble | 1 | — | — | — | 1 | — | — | 1 | — |
| 817 | Drizzile | 1 | — | — | — | 1 | — | — | 1 | — |
| 818 | Inteleon | 1 | — | — | — | 1 | — | — | 1 | — |
| 819 | Skwovet | 1 | — | — | — | 1 | — | — | 1 | — |
| 820 | Greedent | 1 | — | — | — | 1 | — | — | 1 | — |
| 821 | Rookidee | 1 | — | — | — | 1 | — | — | 1 | 1 |
| 822 | Corvisquire | 1 | — | — | — | 1 | — | — | 1 | 1 |
| 823 | Corviknight | 1 | — | — | — | 1 | — | — | 1 | 1 |
| 824 | Blipbug | 1 | — | — | — | 1 | — | — | — | — |
| 825 | Dottler | 1 | — | — | — | 1 | — | — | — | — |
| 826 | Orbeetle | 1 | — | — | — | 1 | — | — | — | — |
| 827 | Nickit | 1 | — | — | — | 1 | — | — | — | 1 |
| 828 | Thievul | 1 | — | — | — | 1 | — | — | — | 1 |
| 829 | Gossifleur | 1 | — | — | — | 1 | — | — | — | — |
| 830 | Eldegoss | 1 | — | — | — | 1 | — | — | — | — |
| 831 | Wooloo | 1 | — | — | — | 1 | — | — | — | — |
| 832 | Dubwool | 1 | — | — | — | 1 | — | — | — | — |
| 833 | Chewtle | 1 | — | — | — | 1 | — | — | 1 | — |
| 834 | Drednaw | 1 | — | — | — | 1 | — | — | 1 | — |
| 835 | Yamper | 1 | — | — | — | 1 | — | — | — | — |
| 836 | Boltund | 1 | — | — | — | 1 | — | — | — | — |
| 837 | Rolycoly | 1 | — | — | — | 1 | — | — | 1 | — |
| 838 | Carkol | 1 | — | — | — | 1 | — | — | 1 | — |
| 839 | Coalossal | 1 | — | — | — | 1 | — | — | 1 | — |
| 840 | Applin | 1 | — | — | — | 1 | — | — | 1 | — |
| 841 | Flapple | 1 | — | — | — | 1 | — | — | 1 | — |
| 842 | Appletun | 1 | — | — | — | 1 | — | — | 1 | — |
| 843 | Silicobra | 1 | — | — | — | 1 | — | — | 1 | — |
| 844 | Sandaconda | 1 | — | — | — | 1 | — | — | 1 | — |
| 845 | Cramorant | 1 | — | — | — | 1 | — | — | 1 | — |
| 846 | Arrokuda | 1 | — | — | — | 1 | — | — | 1 | — |
| 847 | Barraskewda | 1 | — | — | — | 1 | — | — | 1 | — |
| 848 | Toxel | 1 | — | — | — | 1 | — | — | 1 | 1 |
| 849 | Toxtricity | 2 | Toxtricity-Low-Key | — | — | 2 | — | — | 2 | 2 |
| 850 | Sizzlipede | 1 | — | — | — | 1 | — | — | — | — |
| 851 | Centiskorch | 1 | — | — | — | 1 | — | — | — | — |
| 852 | Clobbopus | 1 | — | — | — | 1 | — | — | — | 1 |
| 853 | Grapploct | 1 | — | — | — | 1 | — | — | — | 1 |
| 854 | Sinistea | 2 | Sinistea-Antique | — | — | 2 | — | — | 2 | — |
| 855 | Polteageist | 2 | Polteageist-Antique | — | — | 2 | — | — | 2 | — |
| 856 | Hatenna | 1 | — | — | — | 1 | — | — | 1 | — |
| 857 | Hattrem | 1 | — | — | — | 1 | — | — | 1 | — |
| 858 | Hatterene | 1 | — | — | — | 1 | — | — | 1 | — |
| 859 | Impidimp | 1 | — | — | — | 1 | — | — | 1 | — |
| 860 | Morgrem | 1 | — | — | — | 1 | — | — | 1 | — |
| 861 | Grimmsnarl | 1 | — | — | — | 1 | — | — | 1 | — |
| 862 | Obstagoon | 1 | — | — | — | 1 | — | — | — | — |
| 863 | Perrserker | 1 | — | — | — | 1 | — | — | 1 | 1 |
| 864 | Cursola | 1 | — | — | — | 1 | — | — | — | — |
| 865 | Sirfetch’d | 1 | — | — | — | 1 | — | — | — | 1 |
| 866 | Mr. Rime | 1 | — | — | — | 1 | — | — | — | 1 |
| 867 | Runerigus | 1 | — | — | — | 1 | — | — | — | 1 |
| 868 | Milcery | 1 | — | — | — | 1 | — | — | 1 | — |
| 869 | Alcremie | 9 | Alcremie-Ruby-Cream, Alcremie-Matcha-Cream, Alcremie-Mint-Cream, Alcremie-Lemon-Cream, Alcremie-Salted-Cream, Alcremie-Ruby-Swirl, Alcremie-Caramel-Swirl, Alcremie-Rainbow-Swirl | — | — | 9 | — | — | 9 | — |
| 870 | Falinks | 1 | — | — | — | 1 | — | — | 1 | 1 |
| 871 | Pincurchin | 1 | — | — | — | 1 | — | — | 1 | — |
| 872 | Snom | 1 | — | — | — | 1 | — | — | 1 | — |
| 873 | Frosmoth | 1 | — | — | — | 1 | — | — | 1 | — |
| 874 | Stonjourner | 1 | — | — | — | 1 | — | — | 1 | — |
| 875 | Eiscue | 1 | — | — | — | 1 | — | — | 1 | — |
| 876 | Indeedee | 2 | Indeedee-F | — | — | 2 | — | — | 2 | 2 |
| 877 | Morpeko | 1 | — | — | — | 1 | — | — | 1 | 1 |
| 878 | Cufant | 1 | — | — | — | 1 | — | — | 1 | — |
| 879 | Copperajah | 1 | — | — | — | 1 | — | — | 1 | — |
| 880 | Dracozolt | 1 | — | — | — | 1 | — | — | — | — |
| 881 | Arctozolt | 1 | — | — | — | 1 | — | — | — | — |
| 882 | Dracovish | 1 | — | — | — | 1 | — | — | — | — |
| 883 | Arctovish | 1 | — | — | — | 1 | — | — | — | — |
| 884 | Duraludon | 1 | — | — | — | 1 | — | — | 1 | — |
| 885 | Dreepy | 1 | — | — | — | 1 | — | — | 1 | — |
| 886 | Drakloak | 1 | — | — | — | 1 | — | — | 1 | — |
| 887 | Dragapult | 1 | — | — | — | 1 | — | — | 1 | — |
| 888 | Zacian | 1 | — | — | — | 1 | — | — | 1 | — |
| 889 | Zamazenta | 1 | — | — | — | 1 | — | — | 1 | — |
| 890 | Eternatus | 1 | — | — | — | 1 | — | — | 1 | — |
| 891 | Kubfu | 1 | — | — | — | 1 | — | — | 1 | — |
| 892 | Urshifu | 2 | Urshifu-Rapid-Strike | — | — | 2 | — | — | 2 | — |
| 893 | Zarude | 2 | Zarude-Dada | — | — | 2 | — | — | 2 | — |
| 894 | Regieleki | 1 | — | — | — | 1 | — | — | 1 | — |
| 895 | Regidrago | 1 | — | — | — | 1 | — | — | 1 | — |
| 896 | Glastrier | 1 | — | — | — | 1 | — | — | 1 | — |
| 897 | Spectrier | 1 | — | — | — | 1 | — | — | 1 | — |
| 898 | Calyrex | 3 | Calyrex-Ice, Calyrex-Shadow | — | — | 3 | — | — | 3 | — |
| 899 | Wyrdeer | 1 | — | — | — | — | — | 1 | 1 | — |
| 900 | Kleavor | 2 | — | — | — | — | — | 2 | 1 | 1 |
| 901 | Ursaluna | 2 | Ursaluna-Bloodmoon | — | — | — | — | 1 | 2 | — |
| 902 | Basculegion | 2 | Basculegion-F | — | — | — | — | 2 | 2 | — |
| 903 | Sneasler | 1 | — | — | — | — | — | 1 | 1 | — |
| 904 | Overqwil | 1 | — | — | — | — | — | 1 | 1 | 1 |
| 905 | Enamorus | 2 | Enamorus-Therian | — | — | — | — | 2 | 2 | — |
| 906 | Sprigatito | 1 | — | — | — | — | — | — | 1 | — |
| 907 | Floragato | 1 | — | — | — | — | — | — | 1 | — |
| 908 | Meowscarada | 1 | — | — | — | — | — | — | 1 | — |
| 909 | Fuecoco | 1 | — | — | — | — | — | — | 1 | — |
| 910 | Crocalor | 1 | — | — | — | — | — | — | 1 | — |
| 911 | Skeledirge | 1 | — | — | — | — | — | — | 1 | — |
| 912 | Quaxly | 1 | — | — | — | — | — | — | 1 | — |
| 913 | Quaxwell | 1 | — | — | — | — | — | — | 1 | — |
| 914 | Quaquaval | 1 | — | — | — | — | — | — | 1 | — |
| 915 | Lechonk | 1 | — | — | — | — | — | — | 1 | — |
| 916 | Oinkologne | 2 | Oinkologne-F | — | — | — | — | — | 2 | — |
| 917 | Tarountula | 1 | — | — | — | — | — | — | 1 | — |
| 918 | Spidops | 1 | — | — | — | — | — | — | 1 | — |
| 919 | Nymble | 1 | — | — | — | — | — | — | 1 | — |
| 920 | Lokix | 1 | — | — | — | — | — | — | 1 | — |
| 921 | Pawmi | 1 | — | — | — | — | — | — | 1 | — |
| 922 | Pawmo | 1 | — | — | — | — | — | — | 1 | — |
| 923 | Pawmot | 1 | — | — | — | — | — | — | 1 | — |
| 924 | Tandemaus | 1 | — | — | — | — | — | — | 1 | — |
| 925 | Maushold | 2 | Maushold-Four | — | — | — | — | — | 2 | — |
| 926 | Fidough | 1 | — | — | — | — | — | — | 1 | 1 |
| 927 | Dachsbun | 1 | — | — | — | — | — | — | 1 | 1 |
| 928 | Smoliv | 1 | — | — | — | — | — | — | 1 | — |
| 929 | Dolliv | 1 | — | — | — | — | — | — | 1 | — |
| 930 | Arboliva | 1 | — | — | — | — | — | — | 1 | — |
| 931 | Squawkabilly | 4 | Squawkabilly-Blue, Squawkabilly-Yellow, Squawkabilly-White | — | — | — | — | — | 4 | 4 |
| 932 | Nacli | 1 | — | — | — | — | — | — | 1 | 1 |
| 933 | Naclstack | 1 | — | — | — | — | — | — | 1 | 1 |
| 934 | Garganacl | 1 | — | — | — | — | — | — | 1 | 1 |
| 935 | Charcadet | 1 | — | — | — | — | — | — | 1 | 1 |
| 936 | Armarouge | 1 | — | — | — | — | — | — | 1 | 1 |
| 937 | Ceruledge | 1 | — | — | — | — | — | — | 1 | 1 |
| 938 | Tadbulb | 1 | — | — | — | — | — | — | 1 | — |
| 939 | Bellibolt | 1 | — | — | — | — | — | — | 1 | — |
| 940 | Wattrel | 1 | — | — | — | — | — | — | 1 | — |
| 941 | Kilowattrel | 1 | — | — | — | — | — | — | 1 | — |
| 942 | Maschiff | 1 | — | — | — | — | — | — | 1 | 1 |
| 943 | Mabosstiff | 1 | — | — | — | — | — | — | 1 | 1 |
| 944 | Shroodle | 1 | — | — | — | — | — | — | 1 | 1 |
| 945 | Grafaiai | 1 | — | — | — | — | — | — | 1 | 1 |
| 946 | Bramblin | 1 | — | — | — | — | — | — | 1 | — |
| 947 | Brambleghast | 1 | — | — | — | — | — | — | 1 | — |
| 948 | Toedscool | 1 | — | — | — | — | — | — | 1 | — |
| 949 | Toedscruel | 1 | — | — | — | — | — | — | 1 | — |
| 950 | Klawf | 1 | — | — | — | — | — | — | 1 | — |
| 951 | Capsakid | 1 | — | — | — | — | — | — | 1 | 1 |
| 952 | Scovillain | 1 | — | — | — | — | — | — | 1 | 1 |
| 953 | Rellor | 1 | — | — | — | — | — | — | 1 | — |
| 954 | Rabsca | 1 | — | — | — | — | — | — | 1 | — |
| 955 | Flittle | 1 | — | — | — | — | — | — | 1 | — |
| 956 | Espathra | 1 | — | — | — | — | — | — | 1 | — |
| 957 | Tinkatink | 1 | — | — | — | — | — | — | 1 | 1 |
| 958 | Tinkatuff | 1 | — | — | — | — | — | — | 1 | 1 |
| 959 | Tinkaton | 1 | — | — | — | — | — | — | 1 | 1 |
| 960 | Wiglett | 1 | — | — | — | — | — | — | 1 | — |
| 961 | Wugtrio | 1 | — | — | — | — | — | — | 1 | — |
| 962 | Bombirdier | 1 | — | — | — | — | — | — | 1 | — |
| 963 | Finizen | 1 | — | — | — | — | — | — | 1 | — |
| 964 | Palafin | 1 | — | — | — | — | — | — | 1 | — |
| 965 | Varoom | 1 | — | — | — | — | — | — | 1 | — |
| 966 | Revavroom | 1 | — | — | — | — | — | — | 1 | — |
| 967 | Cyclizar | 1 | — | — | — | — | — | — | 1 | 1 |
| 968 | Orthworm | 1 | — | — | — | — | — | — | 1 | — |
| 969 | Glimmet | 1 | — | — | — | — | — | — | 1 | 1 |
| 970 | Glimmora | 1 | — | — | — | — | — | — | 1 | 1 |
| 971 | Greavard | 1 | — | — | — | — | — | — | 1 | 1 |
| 972 | Houndstone | 1 | — | — | — | — | — | — | 1 | 1 |
| 973 | Flamigo | 1 | — | — | — | — | — | — | 1 | 1 |
| 974 | Cetoddle | 1 | — | — | — | — | — | — | 1 | — |
| 975 | Cetitan | 1 | — | — | — | — | — | — | 1 | — |
| 976 | Veluza | 1 | — | — | — | — | — | — | 1 | — |
| 977 | Dondozo | 1 | — | — | — | — | — | — | 1 | 1 |
| 978 | Tatsugiri | 3 | Tatsugiri-Droopy, Tatsugiri-Stretchy | — | — | — | — | — | 3 | 3 |
| 979 | Annihilape | 1 | — | — | — | — | — | — | 1 | 1 |
| 980 | Clodsire | 1 | — | — | — | — | — | — | 1 | — |
| 981 | Farigiraf | 1 | — | — | — | — | — | — | 1 | — |
| 982 | Dudunsparce | 2 | Dudunsparce-Three-Segment | — | — | — | — | — | 2 | — |
| 983 | Kingambit | 1 | — | — | — | — | — | — | 1 | — |
| 984 | Great Tusk | 1 | — | — | — | — | — | — | 1 | — |
| 985 | Scream Tail | 1 | — | — | — | — | — | — | 1 | — |
| 986 | Brute Bonnet | 1 | — | — | — | — | — | — | 1 | — |
| 987 | Flutter Mane | 1 | — | — | — | — | — | — | 1 | — |
| 988 | Slither Wing | 1 | — | — | — | — | — | — | 1 | — |
| 989 | Sandy Shocks | 1 | — | — | — | — | — | — | 1 | — |
| 990 | Iron Treads | 1 | — | — | — | — | — | — | 1 | — |
| 991 | Iron Bundle | 1 | — | — | — | — | — | — | 1 | — |
| 992 | Iron Hands | 1 | — | — | — | — | — | — | 1 | — |
| 993 | Iron Jugulis | 1 | — | — | — | — | — | — | 1 | — |
| 994 | Iron Moth | 1 | — | — | — | — | — | — | 1 | — |
| 995 | Iron Thorns | 1 | — | — | — | — | — | — | 1 | — |
| 996 | Frigibax | 1 | — | — | — | — | — | — | 1 | 1 |
| 997 | Arctibax | 1 | — | — | — | — | — | — | 1 | 1 |
| 998 | Baxcalibur | 1 | — | — | — | — | — | — | 1 | 1 |
| 999 | Gimmighoul | 2 | Gimmighoul-Roaming | — | — | — | — | — | 2 | 2 |
| 1000 | Gholdengo | 1 | — | — | — | — | — | — | 1 | 1 |
| 1001 | Wo-Chien | 1 | — | — | — | — | — | — | 1 | — |
| 1002 | Chien-Pao | 1 | — | — | — | — | — | — | 1 | — |
| 1003 | Ting-Lu | 1 | — | — | — | — | — | — | 1 | — |
| 1004 | Chi-Yu | 1 | — | — | — | — | — | — | 1 | — |
| 1005 | Roaring Moon | 1 | — | — | — | — | — | — | 1 | — |
| 1006 | Iron Valiant | 1 | — | — | — | — | — | — | 1 | — |
| 1007 | Koraidon | 5 | — | — | — | — | — | — | 5 | — |
| 1008 | Miraidon | 5 | — | — | — | — | — | — | 5 | — |
| 1009 | Walking Wake | 1 | — | — | — | — | — | — | 1 | — |
| 1010 | Iron Leaves | 1 | — | — | — | — | — | — | 1 | — |
| 1011 | Dipplin | 1 | — | — | — | — | — | — | 1 | — |
| 1012 | Poltchageist | 2 | Poltchageist-Artisan | — | — | — | — | — | 2 | — |
| 1013 | Sinistcha | 2 | Sinistcha-Masterpiece | — | — | — | — | — | 2 | — |
| 1014 | Okidogi | 1 | — | — | — | — | — | — | 1 | — |
| 1015 | Munkidori | 1 | — | — | — | — | — | — | 1 | — |
| 1016 | Fezandipiti | 1 | — | — | — | — | — | — | 1 | — |
| 1017 | Ogerpon | 4 | Ogerpon-Wellspring, Ogerpon-Hearthflame, Ogerpon-Cornerstone | — | — | — | — | — | 4 | — |
| 1018 | Archaludon | 1 | — | — | — | — | — | — | 1 | — |
| 1019 | Hydrapple | 1 | — | — | — | — | — | — | 1 | — |
| 1020 | Gouging Fire | 1 | — | — | — | — | — | — | 1 | — |
| 1021 | Raging Bolt | 1 | — | — | — | — | — | — | 1 | — |
| 1022 | Iron Boulder | 1 | — | — | — | — | — | — | 1 | — |
| 1023 | Iron Crown | 1 | — | — | — | — | — | — | 1 | — |
| 1024 | Terapagos | 1 | — | — | — | — | — | — | 1 | — |
| 1025 | Pecharunt | 1 | — | — | — | — | — | — | 1 | — |

---
## 5. Voci-forma ESCLUSIVE di un singolo titolo

Queste sono le voci che **non** puoi ottenere da nessun altro gioco collegato a HOME. Se salti quel titolo, la voce è irrecuperabile. Calcolate per differenza sulle tabelle `personal`.

| Titolo | Voci-forma esclusive |
|---|---|
| LGPE | **2** |
| USUM | **9** |
| SwSh | **24** |
| BDSP | **0** |
| PLA | **6** |
| SV | **109** |
| Z-A | **0** |

### 5.1 Esclusive di LGPE — 2 voci

#25 Pikachu (forma 8), #133 Eevee (forma 1)

### 5.2 Esclusive di USUM — 9 voci

#735 Gumshoos (forma 1), #738 Vikavolt (forma 1), #743 Ribombee (forma 1), #752 Araquanid (forma 1), #754 Lurantis (forma 1), #758 Salazzle (forma 1), #777 Togedemaru (forma 1), #778 Mimikyu (forma 2), #784 Kommo-o (forma 1)

### 5.3 Esclusive di SwSh — 24 voci

#77 Ponyta (forma 1), #78 Rapidash (forma 1), #222 Corsola (forma 1), #263 Zigzagoon (forma 1), #264 Linoone (forma 1), #554 Darumaka (forma 1), #555 Darmanitan (forma 2), #824 Blipbug, #825 Dottler, #826 Orbeetle, #829 Gossifleur, #830 Eldegoss, #831 Wooloo, #832 Dubwool, #835 Yamper, #836 Boltund, #850 Sizzlipede, #851 Centiskorch, #862 Obstagoon, #864 Cursola, #880 Dracozolt, #881 Arctozolt, #882 Dracovish, #883 Arctovish

### 5.5 Esclusive di PLA — 6 voci

#59 Arcanine (forma 2), #101 Electrode (forma 2), #493 Arceus (forma 18), #549 Lilligant (forma 2), #713 Avalugg (forma 2), #900 Kleavor (forma 1)

### 5.6 Esclusive di SV — 109 voci

#128 Tauros (forma 1), #128 Tauros (forma 2), #128 Tauros (forma 3), #194 Wooper (forma 1), #901 Ursaluna (forma 1), #906 Sprigatito, #907 Floragato, #908 Meowscarada, #909 Fuecoco, #910 Crocalor, #911 Skeledirge, #912 Quaxly, #913 Quaxwell, #914 Quaquaval, #915 Lechonk, #916 Oinkologne, #916 Oinkologne (forma 1), #917 Tarountula, #918 Spidops, #919 Nymble, #920 Lokix, #921 Pawmi, #922 Pawmo, #923 Pawmot, #924 Tandemaus, #925 Maushold, #925 Maushold (forma 1), #928 Smoliv, #929 Dolliv, #930 Arboliva, #938 Tadbulb, #939 Bellibolt, #940 Wattrel, #941 Kilowattrel, #946 Bramblin, #947 Brambleghast, #948 Toedscool, #949 Toedscruel, #950 Klawf, #953 Rellor, #954 Rabsca, #955 Flittle, #956 Espathra, #960 Wiglett, #961 Wugtrio, #962 Bombirdier, #963 Finizen, #964 Palafin, #965 Varoom, #966 Revavroom, #968 Orthworm, #974 Cetoddle, #975 Cetitan, #976 Veluza, #980 Clodsire, #981 Farigiraf, #982 Dudunsparce, #982 Dudunsparce (forma 1), #983 Kingambit, #984 Great Tusk, #985 Scream Tail, #986 Brute Bonnet, #987 Flutter Mane, #988 Slither Wing, #989 Sandy Shocks, #990 Iron Treads, #991 Iron Bundle, #992 Iron Hands, #993 Iron Jugulis, #994 Iron Moth, #995 Iron Thorns, #1001 Wo-Chien, #1002 Chien-Pao, #1003 Ting-Lu, #1004 Chi-Yu, #1005 Roaring Moon, #1006 Iron Valiant, #1007 Koraidon, #1007 Koraidon (forma 1), #1007 Koraidon (forma 2), #1007 Koraidon (forma 3), #1007 Koraidon (forma 4), #1008 Miraidon, #1008 Miraidon (forma 1), #1008 Miraidon (forma 2), #1008 Miraidon (forma 3), #1008 Miraidon (forma 4), #1009 Walking Wake, #1010 Iron Leaves, #1011 Dipplin, #1012 Poltchageist, #1012 Poltchageist (forma 1), #1013 Sinistcha, #1013 Sinistcha (forma 1), #1014 Okidogi, #1015 Munkidori, #1016 Fezandipiti, #1017 Ogerpon, #1017 Ogerpon (forma 1), #1017 Ogerpon (forma 2), #1017 Ogerpon (forma 3), #1018 Archaludon, #1019 Hydrapple, #1020 Gouging Fire, #1021 Raging Bolt, #1022 Iron Boulder, #1023 Iron Crown, #1024 Terapagos, #1025 Pecharunt

---

## 6. Conclusione operativa

Il calcolo dà un risultato che corregge un'idea diffusa:

- **LGPE, USUM, SwSh, PLA e SV sono obbligatori.** Ognuno possiede voci-forma che nessun altro titolo può fornire.
- **BDSP e Leggende: Z-A hanno 0 voci-forma esclusive.** Nessuna specie o forma richiede questi due giochi per il **Dex Nazionale**.
- BDSP e Z-A restano necessari per i **Pokédex per gioco di origine** di HOME (e per i relativi premi: Manaphy cromatico da BDSP, Volcanion cromatico da Z-A), perché quelle voci richiedono un Pokémon con marchio d'origine di quel titolo — condizione che nessun altro gioco soddisfa.

**[Non verificato]** Non posso confermare che il Pokédex di HOME consideri “completo” esattamente questo insieme: HOME potrebbe contare forme cosmetiche o il fattore Gigantamax come voci proprie. Per la verifica finale l'unica fonte attendibile è il Pokédex di HOME stesso, confrontato voce per voce.

### Scadenza

Le 9 voci esclusive di **Ultra Sun/Ultra Moon** (tutte forme Totem di Alola) passano obbligatoriamente per Pokémon Bank, il cui servizio termina il **26 febbraio 2027**. Dopo quella data diventano irraggiungibili con mezzi ufficiali.

### Avvertenza sui possibili falsi positivi

**[Inferenza]** Il flag `IsPresentInGame` delle tabelle `personal` indica che la forma esiste nei dati del gioco, non necessariamente che sia catturabile e conservabile dal giocatore. Almeno un caso nell'elenco §5.5 è sospetto: **Kleavor forma 1** corrisponde con buona probabilità a una forma "Nobile/Signore" di Leggende: Arceus, non ottenibile. Verifica caso per caso con il controllo di legalità di PKHeX prima di considerare una voce come mancante.