# Confronto fra la nostra enumerazione e quella di PokePC Classic

> I dati vengono dal deposito `pokepc/dataset`, che dal 2026-09-22 alimenta il servizio dopo la chiusura del tracciatore classico, al commit 3933759 2026-10-13, disposizione `modern/home/fully-sorted`.

> Documento generato da `tools/confronta-livingdex-pokepc.py`. Non si modifica a mano: si rigenera. Non fonde le due enumerazioni e non decide chi abbia ragione; le mette una accanto all'altra e classifica le divergenze per contrassegno.

PokePC Classic, già SuperEffective.gg, è un tracciatore di living dex che pubblica i propri dati come JSON sotto licenza MIT. È la terza enumerazione indipendente che il progetto possiede, dopo la propria e quella del foglio comunitario, e serve a rompere la parità fra le prime due: due misure che divergono dicono che una sbaglia e non quale. Resta una fonte di terzo livello, cioè l'implementazione di un autore, e vale come controprova e non come autorità.

Ciò che si confronta non è una lista di specie ma una disposizione in scatole, cioè l'elenco delle caselle che quel tracciatore ritiene si debbano riempire perché un deposito sia completo. È esattamente la domanda che la nostra lista di spunta dichiara indeterminata, cioè quali forme il deposito conti come casella separata.

## Il conto delle due enumerazioni

| Misura | PokePC | Nostra |
|---|---|---|
| voci totali da possedere | 1387 | 1395 |
| numeri di catalogo distinti | 1025 | 1025 |
| voci oltre la specie base | 362 | 370 |
| specie su cui le due concordano | 896 | 896 |

Lo scarto complessivo è di 8 voci, e come nel confronto con il foglio va letto nelle due direzioni separatamente, perché sono scarti di natura diversa che si compensano in parte. PokePC conta più di noi su 97 specie, per 151 voci in eccesso; noi contiamo più di PokePC su 32 specie, per 159 voci.

## Che cosa PokePC colloca in una casella, per classe

Il conto seguente riguarda le sole voci oltre la specie base, e le classi vengono dai contrassegni del dato e non da una nostra lettura. Una voce cade in una classe sola, quindi le classi si sommano al totale.

| Classe | Voci |
|---|---|
| forma cosmetica, cioè una variante che il campo della forma non separa | 157 |
| forma femminile, cioè una differenza di sesso resa come voce propria | 103 |
| altra forma, cioè una variante che il campo della forma separa | 102 |

## Le disposizioni sorelle, che non concordano fra loro

Le disposizioni del deposito sono 13, e la prima stesura di questo programma assumeva che differissero per il solo ordinamento. Non è vero, e la verifica lo dice: si raggruppano per insieme di voci collocate in 9 insiemi distinti. La differenza non è un difetto del dato ma una scelta di chi lo ha scritto, cioè se dare una casella propria alla forma gigamax di una specie che ne ha una.

| Voci collocate | Disposizioni |
|---|---|
| 1388 | grouped-region, species-first |
| 1387 | fully-sorted, grouped-balanced, sorted-species |
| 1373 | fully-sorted-minimal, sorted-species-minimal |
| 682 | gift-sv |
| 584 | gift-swsh |
| 364 | gift-lza |
| 242 | gift-la |
| 153 | gift-lgpe |
| 151 | gift-bdsp |

Il confronto usa `fully-sorted`, che appartiene al gruppo intermedio: conta le forme regionali e le differenze di sesso, non duplica una specie per la sua forma gigamax, e non applica la compattazione delle due dichiarate minime. La scelta va dichiarata perché cambia il totale di trentotto voci in un verso e di quattordici nell'altro.

## Dove PokePC conta più di noi

Sono 97 specie. La classe prevalente dice la natura della nostra cecità: ciò che il campo della forma non separa, come le differenze di sesso e le varianti cosmetiche, non entra nella nostra enumerazione perché la leggiamo dalla struttura del dato e non da un catalogo di collezionabili.

| Dex | Specie | PokePC | Nostra | Che cosa conta in più |
|---|---|---|---|---|
| 3 | venusaur | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 12 | butterfree | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 19 | rattata | 3 | 2 | 1 forma femminile, cioè una differenza di sesso resa come voce propria; 1 altra forma, cioè una variante che il campo della forma separa |
| 20 | raticate | 3 | 2 | 1 forma femminile, cioè una differenza di sesso resa come voce propria; 1 altra forma, cioè una variante che il campo della forma separa |
| 26 | raichu | 3 | 2 | 1 forma femminile, cioè una differenza di sesso resa come voce propria; 1 altra forma, cioè una variante che il campo della forma separa |
| 41 | zubat | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 42 | golbat | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 44 | gloom | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 45 | vileplume | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 64 | kadabra | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 65 | alakazam | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 84 | doduo | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 85 | dodrio | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 97 | hypno | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 111 | rhyhorn | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 112 | rhydon | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 118 | goldeen | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 119 | seaking | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 123 | scyther | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 129 | magikarp | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 130 | gyarados | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 154 | meganium | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 165 | ledyba | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 166 | ledian | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 178 | xatu | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 185 | sudowoodo | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 186 | politoed | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 190 | aipom | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 194 | wooper | 3 | 2 | 1 forma femminile, cioè una differenza di sesso resa come voce propria; 1 altra forma, cioè una variante che il campo della forma separa |
| 195 | quagsire | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 198 | murkrow | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 202 | wobbuffet | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 203 | girafarig | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 207 | gligar | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 208 | steelix | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 212 | scizor | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 214 | heracross | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 215 | sneasel | 4 | 2 | 2 forma femminile, cioè una differenza di sesso resa come voce propria; 1 altra forma, cioè una variante che il campo della forma separa |
| 217 | ursaring | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 221 | piloswine | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 224 | octillery | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 229 | houndoom | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 232 | donphan | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 255 | torchic | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 256 | combusken | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 257 | blaziken | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 267 | beautifly | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 269 | dustox | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 272 | ludicolo | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 274 | nuzleaf | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 275 | shiftry | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 307 | meditite | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 308 | medicham | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 315 | roselia | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 316 | gulpin | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 317 | swalot | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 322 | numel | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 323 | camerupt | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 332 | cacturne | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 350 | milotic | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 369 | relicanth | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 396 | starly | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 397 | staravia | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 398 | staraptor | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 399 | bidoof | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 400 | bibarel | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 401 | kricketot | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 402 | kricketune | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 403 | shinx | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 404 | luxio | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 405 | luxray | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 407 | roserade | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 415 | combee | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 417 | pachirisu | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 418 | buizel | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 419 | floatzel | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 424 | ambipom | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 443 | gible | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 444 | gabite | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 445 | garchomp | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 449 | hippopotas | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 450 | hippowdon | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 453 | croagunk | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 454 | toxicroak | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 456 | finneon | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 457 | lumineon | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 459 | snover | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 460 | abomasnow | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 461 | weavile | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 464 | rhyperior | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 465 | tangrowth | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 473 | mamoswine | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 521 | unfezant | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 592 | frillish | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 593 | jellicent | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 668 | pyroar | 2 | 1 | 1 forma femminile, cioè una differenza di sesso resa come voce propria |
| 869 | alcremie | 63 | 9 | 62 forma cosmetica, cioè una variante che il campo della forma non separa |

## Dove contiamo più di PokePC

Sono 32 specie. Qui la lettura si rovescia: la nostra enumerazione legge le posizioni di forma dalla tabella del gioco, e quel numero comprende posizioni che non sono oggetti distinti da possedere.

| Dex | Specie | PokePC | Nostra | Perché |
|---|---|---|---|---|
| 59 | arcanine | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 101 | electrode | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 414 | mothim | 1 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 483 | dialga | 1 | 2 | la nostra lista conta 1 posizioni di forma che PokePC non colloca in una casella |
| 484 | palkia | 1 | 2 | la nostra lista conta 1 posizioni di forma che PokePC non colloca in una casella |
| 487 | giratina | 1 | 2 | la nostra lista conta 1 posizioni di forma che PokePC non colloca in una casella |
| 493 | arceus | 1 | 19 | la nostra lista conta 18 posizioni di forma che PokePC non colloca in una casella |
| 549 | lilligant | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 646 | kyurem | 1 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 649 | genesect | 1 | 5 | la nostra lista conta 4 posizioni di forma che PokePC non colloca in una casella |
| 658 | greninja | 1 | 2 | la nostra lista scarta 2 posizioni con la dicitura: forma di sola battaglia: non può stare in una scatola |
| 664 | scatterbug | 1 | 20 | la nostra lista conta 19 posizioni di forma che PokePC non colloca in una casella |
| 665 | spewpa | 1 | 20 | la nostra lista conta 19 posizioni di forma che PokePC non colloca in una casella |
| 713 | avalugg | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 718 | zygarde | 2 | 4 | la nostra lista scarta 2 posizioni con la dicitura: forma di sola battaglia: non può stare in una scatola |
| 744 | rockruff | 1 | 2 | la nostra lista conta 1 posizioni di forma che PokePC non colloca in una casella |
| 773 | silvally | 1 | 18 | la nostra lista conta 17 posizioni di forma che PokePC non colloca in una casella |
| 774 | minior-red | 7 | 8 | la nostra lista scarta 6 posizioni con la dicitura: forma di sola battaglia: non può stare in una scatola |
| 800 | necrozma | 1 | 3 | la nostra lista scarta 1 posizioni con la dicitura: forma di sola battaglia: non può stare in una scatola |
| 898 | calyrex | 1 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 900 | kleavor | 1 | 2 | la nostra lista conta 1 posizioni di forma che PokePC non colloca in una casella |
| 1007 | koraidon | 1 | 5 | la nostra lista conta 4 posizioni di forma che PokePC non colloca in una casella |
| 1008 | miraidon | 1 | 5 | la nostra lista conta 4 posizioni di forma che PokePC non colloca in una casella |
| 1012 | poltchageist | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 1013 | sinistcha | 2 | 3 | la nostra lista conta 2 posizioni di forma che PokePC non colloca in una casella |
| 1017 | ogerpon | 1 | 4 | la nostra lista scarta 4 posizioni con la dicitura: forma di sola battaglia: non può stare in una scatola |
| 1019 | hydrapple | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |
| 1020 | gougingfire | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |
| 1021 | ragingbolt | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |
| 1022 | ironboulder | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |
| 1023 | ironcrown | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |
| 1025 | pecharunt | 1 | 9 | la nostra lista conta 8 posizioni di forma che PokePC non colloca in una casella |

