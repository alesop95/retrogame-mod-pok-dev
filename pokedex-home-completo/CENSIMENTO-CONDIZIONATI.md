# Censimento degli incontri che una condizione sblocca

> Documento generato da `tools/censimento-condizionati.py` dalle tabelle degli incontri selvatici del verificatore. Non si modifica a mano: si rigenera. Copre dalla prima alla quinta generazione, cioe' i titoli la cui via verso il deposito passa dalla banca.

I due criteri sono dichiarati nel docstring del programma e vanno letti prima dei numeri. Il primo e' il tipo di casella, dove alcuni tipi sono essi stessi una condizione, divisi fra condizione di evento e condizione di metodo. Il secondo e' il luogo dedicato, cioe' un luogo che in tutto il titolo ospita una sola specie: la sua presenza sul dato di un esemplare identifica quell'incontro e nessun altro.

Il limite da tenere presente e' che qui stanno le sole vie selvatiche: incontri fissi, doni e scambi stanno in altre tabelle, quindi una specie che risulti ottenibile solo da una condizione lo e' fra le vie selvatiche e non necessariamente in assoluto.

## Quadro d'insieme

| Titolo | Gen | Aree | Specie selvatiche | Aree condizionate | Specie solo da condizione | Aree monospecie esclusive | Luoghi dedicati |
|---|---|---|---|---|---|---|---|
| Rosso | 1 | 84 | 86 | 0 | 0 | 0 | 0 |
| Blu | 1 | 84 | 86 | 0 | 0 | 0 | 0 |
| Giallo | 1 | 91 | 85 | 0 | 0 | 0 | 2 |
| Oro | 2 | 641 | 137 | 73 | 10 | 1 | 1 |
| Argento | 2 | 641 | 137 | 73 | 10 | 1 | 1 |
| Cristallo | 2 | 643 | 147 | 73 | 8 | 1 | 0 |
| Rubino | 3 | 236 | 113 | 6 | 3 | 3 | 1 |
| Zaffiro | 3 | 237 | 113 | 6 | 3 | 3 | 1 |
| Smeraldo | 3 | 248 | 133 | 7 | 3 | 5 | 3 |
| Rosso Fuoco | 3 | 279 | 105 | 9 | 2 | 1 | 9 |
| Verde Foglia | 3 | 279 | 105 | 9 | 2 | 1 | 9 |
| sciami di Hoenn | 3 | 5 | 2 | 5 | 2 | 1 | 5 |
| Diamante | 4 | 295 | 252 | 18 | 6 | 1 | 1 |
| Perla | 4 | 292 | 253 | 18 | 6 | 1 | 1 |
| Platino | 4 | 294 | 259 | 18 | 6 | 1 | 1 |
| Oro HeartGold | 4 | 437 | 244 | 109 | 80 | 1 | 0 |
| Argento SoulSilver | 4 | 436 | 244 | 109 | 80 | 1 | 0 |
| Nero | 5 | 355 | 231 | 17 | 17 | 22 | 2 |
| Bianco | 5 | 357 | 264 | 17 | 17 | 22 | 2 |
| Nero 2 | 5 | 503 | 286 | 20 | 48 | 22 | 2 |
| Bianco 2 | 5 | 502 | 286 | 20 | 48 | 22 | 2 |

## Le specie che fra le vie selvatiche vengono solo da una condizione

E' la parte che pesa per la collezione, perche' un esemplare di queste specie porta necessariamente la traccia della condizione che lo ha prodotto.

### Oro

| Specie | Dex | Condizione |
|---|---|---|
| Weedle | 13 | gara di scarabei |
| Kakuna | 14 | gara di scarabei |
| Beedrill | 15 | gara di scarabei |
| Exeggcute | 102 | colpo di testa; colpo di testa su albero speciale |
| Scyther | 123 | gara di scarabei |
| Pinsir | 127 | gara di scarabei |
| Aipom | 190 | colpo di testa; colpo di testa su albero speciale |
| Pineco | 204 | colpo di testa su albero speciale |
| Shuckle | 213 | spaccaroccia |
| Heracross | 214 | colpo di testa su albero speciale |

### Argento

| Specie | Dex | Condizione |
|---|---|---|
| Caterpie | 10 | gara di scarabei |
| Metapod | 11 | gara di scarabei |
| Butterfree | 12 | gara di scarabei |
| Exeggcute | 102 | colpo di testa; colpo di testa su albero speciale |
| Scyther | 123 | gara di scarabei |
| Pinsir | 127 | gara di scarabei |
| Aipom | 190 | colpo di testa; colpo di testa su albero speciale |
| Pineco | 204 | colpo di testa su albero speciale |
| Shuckle | 213 | spaccaroccia |
| Heracross | 214 | colpo di testa su albero speciale |

### Cristallo

| Specie | Dex | Condizione |
|---|---|---|
| Beedrill | 15 | colpo di testa; gara di scarabei |
| Exeggcute | 102 | colpo di testa; colpo di testa su albero speciale |
| Scyther | 123 | gara di scarabei |
| Pinsir | 127 | gara di scarabei |
| Aipom | 190 | colpo di testa; colpo di testa su albero speciale |
| Pineco | 204 | colpo di testa; colpo di testa su albero speciale |
| Shuckle | 213 | spaccaroccia |
| Heracross | 214 | colpo di testa su albero speciale |

### Rubino

| Specie | Dex | Condizione |
|---|---|---|
| Graveler | 75 | spaccaroccia |
| Nosepass | 299 | spaccaroccia |
| Feebas | 349 | sciame in acqua |

### Zaffiro

| Specie | Dex | Condizione |
|---|---|---|
| Graveler | 75 | spaccaroccia |
| Nosepass | 299 | spaccaroccia |
| Feebas | 349 | sciame in acqua |

### Smeraldo

| Specie | Dex | Condizione |
|---|---|---|
| Shuckle | 213 | spaccaroccia |
| Nosepass | 299 | spaccaroccia |
| Feebas | 349 | sciame in acqua |

### Rosso Fuoco

| Specie | Dex | Condizione |
|---|---|---|
| Graveler | 75 | spaccaroccia |
| Magcargo | 219 | spaccaroccia |

### Verde Foglia

| Specie | Dex | Condizione |
|---|---|---|
| Graveler | 75 | spaccaroccia |
| Magcargo | 219 | spaccaroccia |

### sciami di Hoenn

| Specie | Dex | Condizione |
|---|---|---|
| Surskit | 283 | sciame nell'erba |
| Skitty | 300 | sciame nell'erba |

### Diamante

| Specie | Dex | Condizione |
|---|---|---|
| Aipom | 190 | albero del miele |
| Heracross | 214 | albero del miele |
| Burmy | 412 | albero del miele |
| Combee | 415 | albero del miele |
| Cherubi | 420 | albero del miele |
| Munchlax | 446 | albero del miele |

### Perla

| Specie | Dex | Condizione |
|---|---|---|
| Aipom | 190 | albero del miele |
| Heracross | 214 | albero del miele |
| Burmy | 412 | albero del miele |
| Combee | 415 | albero del miele |
| Cherubi | 420 | albero del miele |
| Munchlax | 446 | albero del miele |

### Platino

| Specie | Dex | Condizione |
|---|---|---|
| Aipom | 190 | albero del miele |
| Heracross | 214 | albero del miele |
| Burmy | 412 | albero del miele |
| Combee | 415 | albero del miele |
| Cherubi | 420 | albero del miele |
| Munchlax | 446 | albero del miele |

### Oro HeartGold

| Specie | Dex | Condizione |
|---|---|---|
| Weedle | 13 | gara di scarabei |
| Kakuna | 14 | gara di scarabei |
| Beedrill | 15 | gara di scarabei |
| Ekans | 23 | zona safari, erba |
| Arbok | 24 | zona safari, erba |
| Exeggcute | 102 | colpo di testa; colpo di testa su albero speciale |
| Weezing | 110 | zona safari, erba |
| Rhydon | 112 | zona safari, erba |
| Scyther | 123 | gara di scarabei |
| Pinsir | 127 | gara di scarabei |
| Lapras | 131 | zona safari, acqua |
| Jumpluff | 189 | zona safari, acqua; zona safari, erba |
| Aipom | 190 | colpo di testa |
| Pineco | 204 | colpo di testa |
| Shuckle | 213 | spaccaroccia; zona safari, erba |
| Heracross | 214 | colpo di testa; colpo di testa su albero speciale |
| Houndoom | 229 | zona safari, erba |
| Wurmple | 265 | colpo di testa; colpo di testa su albero speciale; gara di scarabei |
| Silcoon | 266 | gara di scarabei |
| Beautifly | 267 | gara di scarabei |
| Cascoon | 268 | gara di scarabei |
| Dustox | 269 | gara di scarabei |
| Lotad | 270 | zona safari, erba |
| Lombre | 271 | zona safari, erba |
| Seedot | 273 | colpo di testa; zona safari, erba |
| Nuzleaf | 274 | zona safari, erba |
| Taillow | 276 | colpo di testa su albero speciale |
| Surskit | 283 | zona safari, erba |
| Masquerain | 284 | zona safari, acqua |
| Shroomish | 285 | colpo di testa; zona safari, erba |
| Breloom | 286 | zona safari, erba |
| Slakoth | 287 | colpo di testa su albero speciale |
| Vigoroth | 288 | zona safari, erba |
| Nincada | 290 | gara di scarabei |
| Azurill | 298 | zona safari, erba |
| Nosepass | 299 | zona safari, erba |
| Aron | 304 | zona safari, erba |
| Lairon | 305 | zona safari, erba |
| Medicham | 308 | zona safari, erba |
| Electrike | 309 | zona safari, erba |
| Manectric | 310 | zona safari, erba |
| Volbeat | 313 | gara di scarabei; zona safari, erba |
| Illumise | 314 | gara di scarabei; zona safari, erba |
| Roselia | 315 | zona safari, erba |
| Torkoal | 324 | zona safari, erba |
| Trapinch | 328 | zona safari, erba |
| Vibrava | 329 | zona safari, erba |
| Cacnea | 331 | zona safari, erba |
| Cacturne | 332 | zona safari, erba |
| Zangoose | 335 | zona safari, erba |
| Seviper | 336 | zona safari, erba |
| Lunatone | 337 | zona safari, erba |
| Solrock | 338 | zona safari, erba |
| Barboach | 339 | zona safari, canna super |
| Corphish | 341 | zona safari, canna buona; zona safari, canna super |
| Shuppet | 353 | zona safari, erba |
| Banette | 354 | zona safari, erba |
| Duskull | 355 | zona safari, acqua; zona safari, erba |
| Dusclops | 356 | zona safari, erba |
| Chimecho | 358 | zona safari, erba |
| Spheal | 363 | zona safari, erba |
| Sealeo | 364 | zona safari, erba |
| Bagon | 371 | zona safari, erba |
| Shelgon | 372 | zona safari, erba |
| Beldum | 374 | zona safari, erba |
| Metang | 375 | zona safari, erba |
| Starly | 396 | colpo di testa su albero speciale |
| Kricketune | 402 | gara di scarabei |
| Luxio | 404 | zona safari, erba |
| Burmy | 412 | colpo di testa su albero speciale |
| Combee | 415 | colpo di testa; colpo di testa su albero speciale; gara di scarabei |
| Pachirisu | 417 | zona safari, erba |
| Floatzel | 419 | zona safari, erba |
| Cherubi | 420 | colpo di testa su albero speciale |
| Bronzong | 437 | zona safari, erba |
| Gible | 443 | zona safari, erba |
| Riolu | 447 | zona safari, erba |
| Hippopotas | 449 | zona safari, erba |
| Skorupi | 451 | zona safari, erba |
| Croagunk | 453 | zona safari, erba |

### Argento SoulSilver

| Specie | Dex | Condizione |
|---|---|---|
| Caterpie | 10 | gara di scarabei |
| Metapod | 11 | gara di scarabei |
| Butterfree | 12 | gara di scarabei |
| Sandshrew | 27 | zona safari, erba |
| Sandslash | 28 | zona safari, erba |
| Exeggcute | 102 | colpo di testa; colpo di testa su albero speciale |
| Weezing | 110 | zona safari, erba |
| Rhydon | 112 | zona safari, erba |
| Scyther | 123 | gara di scarabei |
| Pinsir | 127 | gara di scarabei |
| Lapras | 131 | zona safari, acqua |
| Jumpluff | 189 | zona safari, acqua; zona safari, erba |
| Aipom | 190 | colpo di testa |
| Pineco | 204 | colpo di testa |
| Shuckle | 213 | spaccaroccia; zona safari, erba |
| Heracross | 214 | colpo di testa; colpo di testa su albero speciale |
| Houndoom | 229 | zona safari, erba |
| Wurmple | 265 | colpo di testa; colpo di testa su albero speciale; gara di scarabei |
| Silcoon | 266 | gara di scarabei |
| Beautifly | 267 | gara di scarabei |
| Cascoon | 268 | gara di scarabei |
| Dustox | 269 | gara di scarabei |
| Lotad | 270 | zona safari, erba |
| Lombre | 271 | zona safari, erba |
| Seedot | 273 | colpo di testa; zona safari, erba |
| Nuzleaf | 274 | zona safari, erba |
| Taillow | 276 | colpo di testa su albero speciale |
| Surskit | 283 | zona safari, erba |
| Masquerain | 284 | zona safari, acqua |
| Shroomish | 285 | colpo di testa; zona safari, erba |
| Breloom | 286 | zona safari, erba |
| Slakoth | 287 | colpo di testa su albero speciale |
| Vigoroth | 288 | zona safari, erba |
| Nincada | 290 | gara di scarabei |
| Azurill | 298 | zona safari, erba |
| Nosepass | 299 | zona safari, erba |
| Aron | 304 | zona safari, erba |
| Lairon | 305 | zona safari, erba |
| Medicham | 308 | zona safari, erba |
| Electrike | 309 | zona safari, erba |
| Manectric | 310 | zona safari, erba |
| Volbeat | 313 | gara di scarabei; zona safari, erba |
| Illumise | 314 | gara di scarabei; zona safari, erba |
| Roselia | 315 | zona safari, erba |
| Torkoal | 324 | zona safari, erba |
| Trapinch | 328 | zona safari, erba |
| Vibrava | 329 | zona safari, erba |
| Cacnea | 331 | zona safari, erba |
| Cacturne | 332 | zona safari, erba |
| Zangoose | 335 | zona safari, erba |
| Seviper | 336 | zona safari, erba |
| Lunatone | 337 | zona safari, erba |
| Solrock | 338 | zona safari, erba |
| Barboach | 339 | zona safari, canna super |
| Corphish | 341 | zona safari, canna buona; zona safari, canna super |
| Shuppet | 353 | zona safari, erba |
| Banette | 354 | zona safari, erba |
| Duskull | 355 | zona safari, acqua; zona safari, erba |
| Dusclops | 356 | zona safari, erba |
| Chimecho | 358 | zona safari, erba |
| Spheal | 363 | zona safari, erba |
| Sealeo | 364 | zona safari, erba |
| Bagon | 371 | zona safari, erba |
| Shelgon | 372 | zona safari, erba |
| Beldum | 374 | zona safari, erba |
| Metang | 375 | zona safari, erba |
| Starly | 396 | colpo di testa su albero speciale |
| Kricketune | 402 | gara di scarabei |
| Luxio | 404 | zona safari, erba |
| Burmy | 412 | colpo di testa su albero speciale |
| Combee | 415 | colpo di testa; colpo di testa su albero speciale; gara di scarabei |
| Pachirisu | 417 | zona safari, erba |
| Floatzel | 419 | zona safari, erba |
| Cherubi | 420 | colpo di testa su albero speciale |
| Bronzong | 437 | zona safari, erba |
| Gible | 443 | zona safari, erba |
| Riolu | 447 | zona safari, erba |
| Hippopotas | 449 | zona safari, erba |
| Skorupi | 451 | zona safari, erba |
| Croagunk | 453 | zona safari, erba |

### Nero

| Specie | Dex | Condizione |
|---|---|---|
| Mankey | 56 | sciame |
| Farfetch’d | 83 | sciame |
| Doduo | 84 | sciame |
| Exeggcute | 102 | sciame |
| Sentret | 161 | sciame |
| Yanma | 193 | sciame |
| Pineco | 204 | sciame |
| Houndour | 228 | sciame |
| Smeargle | 235 | sciame |
| Tyrogue | 236 | sciame |
| Shroomish | 285 | sciame |
| Plusle | 311 | sciame |
| Volbeat | 313 | sciame |
| Shuppet | 353 | sciame |
| Wynaut | 360 | sciame |
| Hippopotas | 449 | sciame |
| Croagunk | 453 | sciame |

### Bianco

| Specie | Dex | Condizione |
|---|---|---|
| Paras | 46 | sciame |
| Mankey | 56 | sciame |
| Farfetch’d | 83 | sciame |
| Doduo | 84 | sciame |
| Exeggcute | 102 | sciame |
| Sentret | 161 | sciame |
| Yanma | 193 | sciame |
| Pineco | 204 | sciame |
| Smeargle | 235 | sciame |
| Tyrogue | 236 | sciame |
| Poochyena | 261 | sciame |
| Minun | 312 | sciame |
| Illumise | 314 | sciame |
| Shuppet | 353 | sciame |
| Wynaut | 360 | sciame |
| Hippopotas | 449 | sciame |
| Croagunk | 453 | sciame |

### Nero 2

| Specie | Dex | Condizione |
|---|---|---|
| Beedrill | 15 | grotta nascosta |
| Fearow | 22 | sciame |
| Nidoran♀ | 29 | grotta nascosta |
| Nidoran♂ | 32 | grotta nascosta |
| Venonat | 48 | grotta nascosta |
| Slowpoke | 79 | sciame |
| Farfetch’d | 83 | sciame |
| Doduo | 84 | sciame |
| Hypno | 97 | sciame |
| Chansey | 113 | grotta nascosta |
| Pinsir | 127 | grotta nascosta |
| Vaporeon | 134 | grotta nascosta |
| Jolteon | 135 | grotta nascosta |
| Flareon | 136 | grotta nascosta |
| Furret | 162 | sciame |
| Ariados | 168 | sciame |
| Togetic | 176 | grotta nascosta |
| Natu | 177 | sciame |
| Sudowoodo | 185 | sciame |
| Hoppip | 187 | sciame |
| Quagsire | 195 | sciame |
| Espeon | 196 | grotta nascosta |
| Umbreon | 197 | grotta nascosta |
| Murkrow | 198 | grotta nascosta |
| Pineco | 204 | sciame |
| Granbull | 210 | grotta nascosta |
| Lombre | 271 | grotta nascosta |
| Swellow | 277 | sciame |
| Masquerain | 284 | sciame |
| Breloom | 286 | grotta nascosta |
| Hariyama | 297 | grotta nascosta |
| Medicham | 308 | grotta nascosta |
| Manectric | 310 | grotta nascosta |
| Plusle | 311 | sciame |
| Volbeat | 313 | sciame |
| Swalot | 317 | sciame |
| Cacturne | 332 | sciame |
| Bagon | 371 | grotta nascosta |
| Shelgon | 372 | grotta nascosta |
| Bibarel | 400 | grotta nascosta |
| Pachirisu | 417 | grotta nascosta |
| Drifloon | 425 | grotta nascosta |
| Glameow | 431 | grotta nascosta |
| Stunky | 434 | grotta nascosta |
| Chatot | 441 | grotta nascosta |
| Hippowdon | 450 | sciame |
| Leafeon | 470 | grotta nascosta |
| Glaceon | 471 | grotta nascosta |

### Bianco 2

| Specie | Dex | Condizione |
|---|---|---|
| Butterfree | 12 | grotta nascosta |
| Fearow | 22 | sciame |
| Nidoran♀ | 29 | grotta nascosta |
| Nidoran♂ | 32 | grotta nascosta |
| Venonat | 48 | grotta nascosta |
| Slowpoke | 79 | sciame |
| Farfetch’d | 83 | sciame |
| Doduo | 84 | sciame |
| Hypno | 97 | sciame |
| Chansey | 113 | grotta nascosta |
| Mr. Mime | 122 | sciame |
| Vaporeon | 134 | grotta nascosta |
| Jolteon | 135 | grotta nascosta |
| Flareon | 136 | grotta nascosta |
| Furret | 162 | sciame |
| Ledian | 166 | sciame |
| Togetic | 176 | grotta nascosta |
| Natu | 177 | sciame |
| Hoppip | 187 | sciame |
| Quagsire | 195 | sciame |
| Espeon | 196 | grotta nascosta |
| Umbreon | 197 | grotta nascosta |
| Murkrow | 198 | grotta nascosta |
| Pineco | 204 | sciame |
| Granbull | 210 | grotta nascosta |
| Heracross | 214 | grotta nascosta |
| Lombre | 271 | grotta nascosta |
| Swellow | 277 | sciame |
| Masquerain | 284 | sciame |
| Breloom | 286 | grotta nascosta |
| Hariyama | 297 | grotta nascosta |
| Medicham | 308 | grotta nascosta |
| Manectric | 310 | grotta nascosta |
| Minun | 312 | sciame |
| Illumise | 314 | sciame |
| Swalot | 317 | sciame |
| Cacturne | 332 | sciame |
| Bagon | 371 | grotta nascosta |
| Shelgon | 372 | grotta nascosta |
| Bibarel | 400 | grotta nascosta |
| Pachirisu | 417 | grotta nascosta |
| Drifloon | 425 | grotta nascosta |
| Glameow | 431 | grotta nascosta |
| Stunky | 434 | grotta nascosta |
| Chatot | 441 | grotta nascosta |
| Hippowdon | 450 | sciame |
| Leafeon | 470 | grotta nascosta |
| Glaceon | 471 | grotta nascosta |

## Le aree che ospitano una specie sola, e non compare altrove nel titolo

E' il criterio che coglie il caso da cui questo lavoro e' nato, e la sua formulazione e' una correzione a come la classe era stata immaginata. L'Isola Miraggio non ha un luogo proprio: la fonte la tiene come l'area d'erba del luogo che la rotta affaccia, e quel medesimo luogo porta accanto le proprie aree d'acqua ordinarie, quindi cercare un luogo dedicato non la trova mai. Cio' che la distingue e' che la sua area ospita una specie sola e che quella specie non compare in nessun'altra area del titolo: la traccia sul dato e' allora la terna fra luogo, tipo di casella e specie, non il nome del luogo.

### Oro

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 9 | 0, ordinaria | Unown | 201 |

### Argento

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 9 | 0, ordinaria | Unown | 201 |

### Cristallo

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 9 | 0, ordinaria | Unown | 201 |

### Rubino

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 34 | 7, sciame in acqua | Feebas | 349 |
| 45 | 0, ordinaria | Wynaut | 360 |
| 57 | 1, ordinaria | Psyduck | 54 |

### Zaffiro

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 34 | 7, sciame in acqua | Feebas | 349 |
| 45 | 0, ordinaria | Wynaut | 360 |
| 57 | 1, ordinaria | Psyduck | 54 |

### Smeraldo

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 34 | 7, sciame in acqua | Feebas | 349 |
| 45 | 0, ordinaria | Wynaut | 360 |
| 57 | 1, ordinaria | Psyduck | 54 |
| 57 | 5, spaccaroccia | Shuckle | 213 |
| 202 | 0, ordinaria | Smeargle | 235 |

### Rosso Fuoco

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 154 | 0, ordinaria | Dunsparce | 206 |

### Verde Foglia

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 154 | 0, ordinaria | Dunsparce | 206 |

### sciami di Hoenn

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 31 | 6, sciame nell'erba | Skitty | 300 |

### Diamante

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 53 | 0, ordinaria | Unown | 201 |

### Perla

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 53 | 0, ordinaria | Unown | 201 |

### Platino

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 53 | 0, ordinaria | Unown | 201 |

### Oro HeartGold

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 209 | 0, ordinaria | Unown | 201 |

### Argento SoulSilver

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 209 | 0, ordinaria | Unown | 201 |

### Nero

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 14 | 4, sciame | Farfetch’d | 83 |
| 15 | 4, sciame | Wynaut | 360 |
| 16 | 4, sciame | Volbeat | 313 |
| 17 | 4, sciame | Hippopotas | 449 |
| 18 | 4, sciame | Smeargle | 235 |
| 19 | 4, sciame | Plusle | 311 |
| 20 | 4, sciame | Sentret | 161 |
| 21 | 4, sciame | Croagunk | 453 |
| 22 | 4, sciame | Houndour | 228 |
| 23 | 4, sciame | Tyrogue | 236 |
| 24 | 4, sciame | Shroomish | 285 |
| 25 | 4, sciame | Doduo | 84 |
| 26 | 4, sciame | Shuppet | 353 |
| 27 | 4, sciame | Yanma | 193 |
| 28 | 4, sciame | Mankey | 56 |
| 29 | 4, sciame | Pineco | 204 |
| 31 | 4, sciame | Exeggcute | 102 |
| 35 | 1, ordinaria | Claydol | 344 |
| 39 | 1, ordinaria | Golett | 622 |
| 56 | 1, ordinaria | Litwick | 607 |
| 65 | 1, ordinaria | Ducklett | 580 |
| 68 | 1, ordinaria | Swanna | 581 |

### Bianco

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 14 | 4, sciame | Farfetch’d | 83 |
| 15 | 4, sciame | Wynaut | 360 |
| 16 | 4, sciame | Illumise | 314 |
| 17 | 4, sciame | Hippopotas | 449 |
| 18 | 4, sciame | Smeargle | 235 |
| 19 | 4, sciame | Minun | 312 |
| 20 | 4, sciame | Sentret | 161 |
| 21 | 4, sciame | Croagunk | 453 |
| 22 | 4, sciame | Poochyena | 261 |
| 23 | 4, sciame | Tyrogue | 236 |
| 24 | 4, sciame | Paras | 46 |
| 25 | 4, sciame | Doduo | 84 |
| 26 | 4, sciame | Shuppet | 353 |
| 27 | 4, sciame | Yanma | 193 |
| 28 | 4, sciame | Mankey | 56 |
| 29 | 4, sciame | Pineco | 204 |
| 31 | 4, sciame | Exeggcute | 102 |
| 35 | 1, ordinaria | Claydol | 344 |
| 39 | 1, ordinaria | Golett | 622 |
| 56 | 1, ordinaria | Litwick | 607 |
| 65 | 1, ordinaria | Ducklett | 580 |
| 68 | 1, ordinaria | Swanna | 581 |

### Nero 2

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 14 | 4, sciame | Farfetch’d | 83 |
| 16 | 4, sciame | Volbeat | 313 |
| 18 | 4, sciame | Natu | 177 |
| 19 | 4, sciame | Plusle | 311 |
| 20 | 4, sciame | Furret | 162 |
| 21 | 4, sciame | Quagsire | 195 |
| 22 | 4, sciame | Swalot | 317 |
| 24 | 4, sciame | Masquerain | 284 |
| 25 | 4, sciame | Doduo | 84 |
| 26 | 4, sciame | Swellow | 277 |
| 28 | 4, sciame | Fearow | 22 |
| 29 | 4, sciame | Pineco | 204 |
| 31 | 4, sciame | Hoppip | 187 |
| 32 | 4, sciame | Hypno | 97 |
| 34 | 4, sciame | Hippowdon | 450 |
| 35 | 1, ordinaria | Baltoy | 343 |
| 65 | 1, ordinaria | Ducklett | 580 |
| 68 | 1, ordinaria | Swanna | 581 |
| 70 | 4, sciame | Slowpoke | 79 |
| 125 | 4, sciame | Sudowoodo | 185 |
| 127 | 4, sciame | Ariados | 168 |
| 132 | 4, sciame | Cacturne | 332 |

### Bianco 2

| Luogo | Tipo di casella | Specie | Dex |
|---|---|---|---|
| 14 | 4, sciame | Farfetch’d | 83 |
| 16 | 4, sciame | Illumise | 314 |
| 18 | 4, sciame | Natu | 177 |
| 19 | 4, sciame | Minun | 312 |
| 20 | 4, sciame | Furret | 162 |
| 21 | 4, sciame | Quagsire | 195 |
| 22 | 4, sciame | Swalot | 317 |
| 24 | 4, sciame | Masquerain | 284 |
| 25 | 4, sciame | Doduo | 84 |
| 26 | 4, sciame | Swellow | 277 |
| 28 | 4, sciame | Fearow | 22 |
| 29 | 4, sciame | Pineco | 204 |
| 31 | 4, sciame | Hoppip | 187 |
| 32 | 4, sciame | Hypno | 97 |
| 34 | 4, sciame | Hippowdon | 450 |
| 35 | 1, ordinaria | Baltoy | 343 |
| 65 | 1, ordinaria | Ducklett | 580 |
| 68 | 1, ordinaria | Swanna | 581 |
| 70 | 4, sciame | Slowpoke | 79 |
| 125 | 4, sciame | Mr. Mime | 122 |
| 127 | 4, sciame | Ledian | 166 |
| 132 | 4, sciame | Cacturne | 332 |

## I luoghi dedicati a una sola specie

Un luogo dedicato e' il criterio piu' stretto: se in tutto il titolo quel numero di luogo ospita una specie sola, contando tutte le sue aree, allora un esemplare che lo porti viene da la' e da nessun altro posto. E' piu' stretto del criterio precedente e non lo sostituisce, perche' un luogo che ospiti anche una sola area d'acqua ordinaria esce da questo elenco pur restando una traccia valida nel precedente.

### Giallo

| Luogo | Specie | Dex |
|---|---|---|
| 89 | Poliwag | 60 |
| 94 | Goldeen | 118 |

### Oro

| Luogo | Specie | Dex |
|---|---|---|
| 71 | Magikarp | 129 |

### Argento

| Luogo | Specie | Dex |
|---|---|---|
| 71 | Magikarp | 129 |

### Rubino

| Luogo | Specie | Dex |
|---|---|---|
| 60 | Whismur | 293 |

### Zaffiro

| Luogo | Specie | Dex |
|---|---|---|
| 60 | Whismur | 293 |

### Smeraldo

| Luogo | Specie | Dex |
|---|---|---|
| 60 | Whismur | 293 |
| 202 | Smeargle | 235 |
| 210 | Zubat | 41 |

### Rosso Fuoco

| Luogo | Specie | Dex |
|---|---|---|
| 154 | Dunsparce | 206 |
| 183 | Zubat | 41 |
| 188 | Unown | 201 |
| 189 | Unown | 201 |
| 190 | Unown | 201 |
| 191 | Unown | 201 |
| 192 | Unown | 201 |
| 193 | Unown | 201 |
| 194 | Unown | 201 |

### Verde Foglia

| Luogo | Specie | Dex |
|---|---|---|
| 154 | Dunsparce | 206 |
| 183 | Zubat | 41 |
| 188 | Unown | 201 |
| 189 | Unown | 201 |
| 190 | Unown | 201 |
| 191 | Unown | 201 |
| 192 | Unown | 201 |
| 193 | Unown | 201 |
| 194 | Unown | 201 |

### sciami di Hoenn

| Luogo | Specie | Dex |
|---|---|---|
| 17 | Surskit | 283 |
| 29 | Surskit | 283 |
| 31 | Skitty | 300 |
| 32 | Surskit | 283 |
| 35 | Surskit | 283 |

### Diamante

| Luogo | Specie | Dex |
|---|---|---|
| 53 | Unown | 201 |

### Perla

| Luogo | Specie | Dex |
|---|---|---|
| 53 | Unown | 201 |

### Platino

| Luogo | Specie | Dex |
|---|---|---|
| 53 | Unown | 201 |

### Nero

| Luogo | Specie | Dex |
|---|---|---|
| 65 | Ducklett | 580 |
| 68 | Swanna | 581 |

### Bianco

| Luogo | Specie | Dex |
|---|---|---|
| 65 | Ducklett | 580 |
| 68 | Swanna | 581 |

### Nero 2

| Luogo | Specie | Dex |
|---|---|---|
| 65 | Ducklett | 580 |
| 68 | Swanna | 581 |

### Bianco 2

| Luogo | Specie | Dex |
|---|---|---|
| 65 | Ducklett | 580 |
| 68 | Swanna | 581 |

