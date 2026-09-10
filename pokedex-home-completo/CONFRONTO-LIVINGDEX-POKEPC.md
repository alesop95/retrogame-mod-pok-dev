# Confronto fra la nostra enumerazione e quella di PokePC Classic

> Documento generato da `tools/confronta-livingdex-pokepc.py`. Non si modifica a mano: si rigenera. Non fonde le due enumerazioni e non decide chi abbia ragione; le mette una accanto all'altra e classifica le divergenze per contrassegno.

PokePC Classic, gia' SuperEffective.gg, e' un tracciatore di living dex che pubblica i propri dati come JSON sotto licenza MIT. E' la terza enumerazione indipendente che il progetto possiede, dopo la propria e quella del foglio comunitario, e serve a rompere la parita' fra le prime due: due misure che divergono dicono che una sbaglia e non quale. Resta una fonte di terzo livello, cioe' l'implementazione di un autore, e vale come controprova e non come autorita'.

Cio' che si confronta non e' una lista di specie ma una disposizione in scatole, cioe' l'elenco delle caselle che quel tracciatore ritiene si debbano riempire perche' un deposito sia completo. E' esattamente la domanda che la nostra lista di spunta dichiara indeterminata, cioe' quali forme il deposito conti come casella separata.

## Il conto delle due enumerazioni

| Misura | PokePC | Nostra |
|---|---|---|
| voci totali da possedere | 1387 | 1367 |
| numeri di catalogo distinti | 1025 | 1025 |
| voci oltre la specie base | 362 | 342 |
| specie su cui le due concordano | 893 | 893 |

Lo scarto complessivo e' di 20 voci, e come nel confronto con il foglio va letto nelle due direzioni separatamente, perche' sono scarti di natura diversa che si compensano in parte. PokePC conta piu' di noi su 105 specie, per 170 voci in eccesso; noi contiamo piu' di PokePC su 27 specie, per 150 voci.

## Che cosa PokePC colloca in una casella, per classe

Il conto seguente riguarda le sole voci oltre la specie base, e le classi vengono dai contrassegni del dato e non da una nostra lettura. Una voce cade in una classe sola, quindi le classi si sommano al totale.

| Classe | Voci |
|---|---|
| forma cosmetica, cioe' una variante che il campo della forma non separa | 157 |
| forma femminile, cioe' una differenza di sesso resa come voce propria | 103 |
| altra forma, cioe' una variante che il campo della forma separa | 103 |

## Le disposizioni sorelle, che non concordano fra loro

Le disposizioni del deposito sono 7, e la prima stesura di questo programma assumeva che differissero per il solo ordinamento. Non e' vero, e la verifica lo dice: si raggruppano per insieme di voci collocate in 3 insiemi distinti. La differenza non e' un difetto del dato ma una scelta di chi lo ha scritto, cioe' se dare una casella propria alla forma gigamax di una specie che ne ha una.

| Voci collocate | Disposizioni |
|---|---|
| 1425 | grouped-region, species-first |
| 1387 | fully-sorted, grouped-balanced, sorted-species |
| 1373 | fully-sorted-minimal, sorted-species-minimal |

Il confronto usa `fully-sorted`, che appartiene al gruppo intermedio: conta le forme regionali e le differenze di sesso, non duplica una specie per la sua forma gigamax, e non applica la compattazione delle due dichiarate minime. La scelta va dichiarata perche' cambia il totale di trentotto voci in un verso e di quattordici nell'altro.

## Dove PokePC conta piu' di noi

Sono 105 specie. La classe prevalente dice la natura della nostra cecita': cio' che il campo della forma non separa, come le differenze di sesso e le varianti cosmetiche, non entra nella nostra enumerazione perche' la leggiamo dalla struttura del dato e non da un catalogo di collezionabili.

| Dex | Specie | PokePC | Nostra | Che cosa conta in piu' |
|---|---|---|---|---|
| 3 | Venusaur | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 12 | Butterfree | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 19 | Rattata | 3 | 2 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria; 1 altra forma, cioe' una variante che il campo della forma separa |
| 20 | Raticate | 3 | 2 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria; 1 altra forma, cioe' una variante che il campo della forma separa |
| 26 | Raichu | 3 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria; 1 altra forma, cioe' una variante che il campo della forma separa |
| 41 | Zubat | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 42 | Golbat | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 44 | Gloom | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 45 | Vileplume | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 64 | Kadabra | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 65 | Alakazam | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 80 | Slowbro | 2 | 1 | 1 altra forma, cioe' una variante che il campo della forma separa |
| 84 | Doduo | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 85 | Dodrio | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 97 | Hypno | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 111 | Rhyhorn | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 112 | Rhydon | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 118 | Goldeen | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 119 | Seaking | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 123 | Scyther | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 129 | Magikarp | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 130 | Gyarados | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 154 | Meganium | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 165 | Ledyba | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 166 | Ledian | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 178 | Xatu | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 185 | Sudowoodo | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 186 | Politoed | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 190 | Aipom | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 194 | Wooper | 3 | 2 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria; 1 altra forma, cioe' una variante che il campo della forma separa |
| 195 | Quagsire | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 198 | Murkrow | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 202 | Wobbuffet | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 203 | Girafarig | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 207 | Gligar | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 208 | Steelix | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 212 | Scizor | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 214 | Heracross | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 215 | Sneasel | 4 | 2 | 2 forma femminile, cioe' una differenza di sesso resa come voce propria; 1 altra forma, cioe' una variante che il campo della forma separa |
| 217 | Ursaring | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 221 | Piloswine | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 224 | Octillery | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 229 | Houndoom | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 232 | Donphan | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 255 | Torchic | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 256 | Combusken | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 257 | Blaziken | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 267 | Beautifly | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 269 | Dustox | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 272 | Ludicolo | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 274 | Nuzleaf | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 275 | Shiftry | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 307 | Meditite | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 308 | Medicham | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 315 | Roselia | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 316 | Gulpin | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 317 | Swalot | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 322 | Numel | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 323 | Camerupt | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 332 | Cacturne | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 350 | Milotic | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 369 | Relicanth | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 396 | Starly | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 397 | Staravia | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 398 | Staraptor | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 399 | Bidoof | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 400 | Bibarel | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 401 | Kricketot | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 402 | Kricketune | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 403 | Shinx | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 404 | Luxio | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 405 | Luxray | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 407 | Roserade | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 415 | Combee | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 417 | Pachirisu | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 418 | Buizel | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 419 | Floatzel | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 424 | Ambipom | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 443 | Gible | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 444 | Gabite | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 445 | Garchomp | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 449 | Hippopotas | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 450 | Hippowdon | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 453 | Croagunk | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 454 | Toxicroak | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 456 | Finneon | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 457 | Lumineon | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 459 | Snover | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 460 | Abomasnow | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 461 | Weavile | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 464 | Rhyperior | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 465 | Tangrowth | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 473 | Mamoswine | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 521 | Unfezant | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 555 | Darmanitan | 2 | 1 | 1 altra forma, cioe' una variante che il campo della forma separa |
| 592 | Frillish | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 593 | Jellicent | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 668 | Pyroar | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 670 | Floette | 6 | 1 | 4 forma cosmetica, cioe' una variante che il campo della forma non separa; 1 altra forma, cioe' una variante che il campo della forma separa |
| 678 | Meowstic | 2 | 1 | 1 forma femminile, cioe' una differenza di sesso resa come voce propria |
| 718 | Zygarde | 2 | 1 | 1 altra forma, cioe' una variante che il campo della forma separa |
| 774 | Minior (Red Core) | 7 | 1 | 6 forma cosmetica, cioe' una variante che il campo della forma non separa; 1 altra forma, cioe' una variante che il campo della forma separa |
| 801 | Magearna | 2 | 1 | 1 forma cosmetica, cioe' una variante che il campo della forma non separa |
| 869 | Alcremie | 63 | 9 | 62 forma cosmetica, cioe' una variante che il campo della forma non separa |
| 978 | Tatsugiri | 3 | 1 | 2 forma cosmetica, cioe' una variante che il campo della forma non separa |

## Dove contiamo piu' di PokePC

Sono 27 specie. Qui la lettura si rovescia: la nostra enumerazione legge le posizioni di forma dalla tabella del gioco, e quel numero comprende posizioni che non sono oggetti distinti da possedere.

| Dex | Specie | PokePC | Nostra | Perche' |
|---|---|---|---|---|
| 59 | Arcanine | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 101 | Electrode | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 414 | Mothim | 1 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 483 | Dialga | 1 | 2 | la nostra lista conta 1 posizioni di forma che PokePC non colloca in una casella |
| 484 | Palkia | 1 | 2 | la nostra lista conta 1 posizioni di forma che PokePC non colloca in una casella |
| 487 | Giratina | 1 | 2 | la nostra lista conta 1 posizioni di forma che PokePC non colloca in una casella |
| 493 | Arceus | 1 | 19 | la nostra lista conta 18 posizioni di forma che PokePC non colloca in una casella |
| 549 | Lilligant | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 646 | Kyurem | 1 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 649 | Genesect | 1 | 5 | la nostra lista conta 4 posizioni di forma che PokePC non colloca in una casella |
| 664 | Scatterbug | 1 | 20 | la nostra lista conta 19 posizioni di forma che PokePC non colloca in una casella |
| 665 | Spewpa | 1 | 20 | la nostra lista conta 19 posizioni di forma che PokePC non colloca in una casella |
| 713 | Avalugg | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 744 | Rockruff | 1 | 2 | la nostra lista conta 1 posizioni di forma che PokePC non colloca in una casella |
| 773 | Silvally | 1 | 18 | la nostra lista conta 17 posizioni di forma che PokePC non colloca in una casella |
| 898 | Calyrex | 1 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 900 | Kleavor | 1 | 2 | la nostra lista conta 1 posizioni di forma che PokePC non colloca in una casella |
| 1007 | Koraidon | 1 | 5 | la nostra lista conta 4 posizioni di forma che PokePC non colloca in una casella |
| 1008 | Miraidon | 1 | 5 | la nostra lista conta 4 posizioni di forma che PokePC non colloca in una casella |
| 1012 | Poltchageist | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 1013 | Sinistcha | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 1019 | Hydrapple | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |
| 1020 | Gouging Fire | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |
| 1021 | Raging Bolt | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |
| 1022 | Iron Boulder | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |
| 1023 | Iron Crown | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |
| 1025 | Pecharunt | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |

