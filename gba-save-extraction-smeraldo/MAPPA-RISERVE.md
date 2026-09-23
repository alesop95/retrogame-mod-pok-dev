# Mappa delle riserve agli edifici, la misura

> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_mappa_riserve.py` sul catalogo `squadre-parco-lotta.json` e sulle 268 squadre estratte dai thread in `_notes/fonti/smogon-parco-lotta-2026-09-21/squadre.json`. Non si modifica a mano: si rigenera. E' la misura su cui si scrive la scelta, non la scelta, e le tre avvertenze del docstring dello strumento valgono per ogni numero qui sotto: i thread nominano la specie e non la natura, registrano soprattutto chi ha fatto una serie buona, e la Torre Lotta pesa quanto tutti gli altri edifici insieme.

Squadre per edificio nel campione: Cupola Lotta 19, Torre Lotta 97, Dojo Lotta 26, Palazzo Lotta 38, Serpe Lotta 20, Piramide Lotta 8, Azienda Lotta 5, edificio non dichiarato 55.

## Per esemplare: in quali edifici e con quale serie

Ogni cella dice in quante squadre dei thread la specie compare in quell'edificio, e fra parentesi la serie piu' lunga dichiarata. Le specie con due esemplari nel lotto, cioe' Latios, Metagross e Swampert, condividono la riga.

| Esemplari | Ruolo | Cup | Tor | Doj | Pal | Ser | Pir | Azi | n.d. | Compagni piu' frequenti |
|---|---|---|---|---|---|---|---|---|---|---|
| metagross-adamant, metagross-sassy | titolare | 8 (100) | 22 (378) | 4 (186) | 11 (224) | 9 (560) | 2 (70) |  | 3 | Latios 21, Swampert 13, Salamence 12 |
| latios-hasty, latios-timid | titolare | 7 (133) | 15 (268) | 8 (143) | 10 (224) | 5 (420) | 2 (70) | 3 (62) | 6 (63) | Metagross 21, Swampert 10, Suicune 7 |
| blissey-bold | titolare | 2 (17) | 11 (163) |  | 4 (178) | 6 (560) | 4 (70) |  | 2 (140) | Metagross 9, Salamence 8, Starmie 4 |
| slaking-adamant | titolare | 7 (30) | 8 (281) |  | 4 (154) |  | 4 (70) |  | 3 (222) | Milotic 6, Gengar 6, Metagross 5 |
| swampert-brave, swampert-relaxed | titolare |  | 12 (268) | 1 (40) | 7 (224) |  | 1 (70) |  | 1 | Metagross 13, Latios 10, Salamence 5 |
| salamence-adamant | riserva | 2 (17) | 13 (280) | 1 (40) | 8 (84) | 4 (78) | 2 (70) | 1 (56) | 8 (140) | Starmie 12, Metagross 12, Suicune 9 |
| suicune-bold | riserva | 5 (80) | 17 (343) | 3 (135) | 4 (154) | 2 |  | 1 (62) | 4 (168) | Salamence 9, Latios 7, Snorlax 6 |
| starmie-timid | riserva | 1 (12) | 7 (117) | 2 (75) | 9 (178) | 7 (78) | 2 (70) | 1 (56) | 3 | Salamence 12, Metagross 11, Heracross 6 |
| milotic-bold | riserva | 5 (28) | 6 | 3 (200) | 3 (84) | 3 (100) |  |  | 5 (140) | Metagross 6, Slaking 6, Salamence 5 |
| latias-calm | riserva | 3 | 10 (378) | 1 (56) |  | 3 (347) | 1 |  | 2 | Metagross 6, Latios 5, Slaking 4 |
| snorlax-careful | riserva |  | 7 (281) | 2 (40) | 1 (57) | 1 |  |  | 8 (222) | Salamence 7, Suicune 6, Latios 5 |
| gengar-timid | riserva | 4 (100) | 8 (281) | 2 (40) |  |  |  |  | 4 (222) | Slaking 6, Metagross 4, Snorlax 4 |
| zapdos-modest | riserva |  | 7 (461) |  | 3 (140) | 1 |  |  | 2 (63) | Kingdra 3, Metagross 3, Tyranitar 3 |
| registeel-careful | riserva |  | 7 (343) | 1 |  |  | 1 (70) |  | 3 | Latios 4, Salamence 3, Latias 3 |
| tauros-jolly | riserva | 3 (133) | 6 (139) |  | 1 (140) | 1 (420) |  |  |  | Latios 6, Milotic 2, Gengar 2 |
| flygon-jolly | riserva |  | 2 (155) |  | 4 (178) | 1 | 1 (70) |  | 2 | Starmie 5, Scizor 3, Gyarados 2 |
| raikou-timid | riserva |  | 7 (215) |  | 1 (42) |  |  |  | 2 | Aerodactyl 3, Blissey 3, Slaking 1 |
| gyarados-adamant | riserva |  | 3 | 1 (143) | 2 (40) |  | 1 (70) |  | 2 | Flygon 2, Metagross 2, Swampert 2 |
| heracross-jolly | riserva | 1 (12) | 4 (98) | 1 (56) |  | 1 (347) | 1 | 1 (56) |  | Starmie 6, Salamence 3, Regice 2 |
| aerodactyl-adamant | riserva |  | 6 (137) |  |  |  |  |  | 2 (63) | Blissey 3, Raikou 3, Slaking 2 |
| moltres-timid | riserva |  | 4 (210) |  |  | 1 |  |  | 3 | Registeel 3, Latios 3, Entei 1 |
| articuno-calm | riserva |  | 3 (155) |  |  |  |  |  | 3 | Suicune 2, Lapras 1, Swampert 1 |
| magneton-modest | riserva |  | 2 (56) |  | 2 (84) |  |  |  | 2 | Aggron 2, Gengar 2, Starmie 2 |
| regice-modest | riserva | 2 (12) | 2 (110) | 1 (143) | 1 (43) |  |  |  |  | Heracross 2, Latios 2, Suicune 1 |
| scizor-adamant | riserva |  |  | 1 | 4 (178) |  |  |  | 1 | Flygon 3, Starmie 3, Armaldo 1 |
| dusclops-bold | riserva |  | 2 (137) |  | 1 (28) |  |  |  | 2 | Misdreavus 1, Duskull 1, Shiftry 1 |
| steelix-adamant | riserva |  | 2 |  | 1 |  |  |  | 2 | Quagsire 2, Suicune 1, Latios 1 |
| marowak-jolly | riserva |  | 1 (280) |  | 1 (147) | 1 |  |  |  | Suicune 2, Salamence 1, Snorlax 1 |
| regirock-adamant | riserva |  | 1 |  |  |  |  |  |  | nessuno |

## Per sostituzione: chi ha giocato accanto agli altri due

Per ogni squadra e per ogni posto, le riserve del lotto che nei thread compaiono accanto ai due titolari che restano. La prima cifra conta le squadre con entrambi, la seconda quelle con almeno uno, la terza quelle con almeno uno nello stesso edificio. L'Azienda Lotta non compare perche' vi si combatte con esemplari in prestito.

| Edificio | Esce | Restano | Candidati: entrambi / almeno uno / stesso edificio |
|---|---|---|---|
| Cupola Lotta | latios-timid | Metagross, Slaking | Salamence 2/15/1; Starmie 1/13/1; Milotic 1/11/5; Gengar 1/9/4 |
| Cupola Lotta | metagross-adamant | Latios, Slaking | Salamence 1/5/1; Starmie 1/5/0; Suicune 0/10/2; Gengar 0/9/4 |
| Cupola Lotta | slaking-adamant | Latios, Metagross | Starmie 2/12/1; Gengar 2/5/3; Salamence 1/12/0; Latias 1/10/0 |
| Torre Lotta | latios-timid | Metagross, Swampert | Salamence 3/14/4; Starmie 2/11/2; Latias 1/7/5; Gyarados 1/3/2 |
| Torre Lotta | swampert-relaxed | Latios, Metagross | Starmie 2/12/3; Gengar 2/5/1; Salamence 1/12/3; Latias 1/10/4 |
| Torre Lotta | metagross-adamant | Latios, Swampert | Salamence 1/5/3; Starmie 1/4/2; Suicune 0/8/4; Latias 0/7/2 |
| Dojo Lotta | latios-timid | Metagross, Swampert | Salamence 3/14/0; Starmie 2/11/1; Latias 1/7/0; Gyarados 1/3/0 |
| Dojo Lotta | metagross-adamant | Latios, Swampert | Salamence 1/5/0; Starmie 1/4/1; Suicune 0/8/1; Latias 0/7/0 |
| Dojo Lotta | swampert-relaxed | Latios, Metagross | Starmie 2/12/1; Gengar 2/5/1; Salamence 1/12/0; Latias 1/10/0 |
| Palazzo Lotta | metagross-sassy | Latios, Swampert | Salamence 1/5/1; Starmie 1/4/0; Suicune 0/8/1; Latias 0/7/0 |
| Palazzo Lotta | latios-hasty | Metagross, Swampert | Salamence 3/14/4; Starmie 2/11/2; Latias 1/7/0; Gyarados 1/3/0 |
| Palazzo Lotta | swampert-brave | Latios, Metagross | Starmie 2/12/2; Gengar 2/5/0; Salamence 1/12/3; Latias 1/10/0 |
| Serpe Lotta | latios-timid | Blissey, Metagross | Salamence 3/17/4; Starmie 2/13/5; Milotic 1/8/0; Latias 1/7/2 |
| Serpe Lotta | metagross-adamant | Blissey, Latios | Latias 1/6/3; Tauros 1/6/1; Heracross 1/2/1; Salamence 0/9/1 |
| Serpe Lotta | blissey-bold | Latios, Metagross | Starmie 2/12/4; Gengar 2/5/0; Salamence 1/12/3; Latias 1/10/3 |
| Piramide Lotta | latios-timid | Metagross, Swampert | Salamence 3/14/1; Starmie 2/11/1; Latias 1/7/1; Gyarados 1/3/1 |
| Piramide Lotta | swampert-relaxed | Latios, Metagross | Starmie 2/12/1; Gengar 2/5/0; Salamence 1/12/1; Latias 1/10/1 |
| Piramide Lotta | metagross-adamant | Latios, Swampert | Salamence 1/5/1; Starmie 1/4/1; Suicune 0/8/0; Latias 0/7/0 |

