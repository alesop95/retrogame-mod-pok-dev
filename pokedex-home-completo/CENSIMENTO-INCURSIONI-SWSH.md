# Censimento delle incursioni di evento di Spada e Scudo

> Documento generato da `tools/censimento-incursioni-swsh.py` dal dump di `tools/pkhex-incursioni-swsh` (`_notes/incursioni-swsh.json`), dal rapporto del lotto `_notes/lotti/lotto-incursioni-evento-swsh/` e dal registro `recreate-pokemon-distributions-events/giudizi-pkhex-core.json`. Non si modifica a mano: si rigenera. Per ADR-097 gli esemplari delle tane di distribuzione delle Wild Area News, cromatici e Gigantamax compresi, contano come esemplari da distribuzione; non scadono con la banca, perché Spada e Scudo parlano con HOME direttamente, e si portano in gioco per la via di `STRATEGIA-SWITCH.md`.

## Che cosa si conta

La fonte sono le tabelle interne `Dist_SW` e `Dist_SH` di `Encounters8Nest` nella libreria PKHeX.Core compilata dal clone in `_notes/fonti/cloni/pkhex`, classe `EncounterStatic8ND`, lette per riflessione. Una riga è un incontro distinto, cioè indice dell'evento, specie, forma, livello, livello Dynamax, fattore Gigantamax, stato del cromatico, abilità, IV perfetti e mosse; una chiave di collezione è specie, forma, Gigantamax (`G`) e cromatico garantito (`S`), ed è l'unità con cui la collezione conta questi esemplari.

Righe di tabella: 1171 in Spada e 1179 in Scudo; righe distinte 1286, di cui 107 solo in Spada e 115 solo in Scudo, su 68 indici di evento. Chiavi di collezione: 359, che si riducono a 323 contando solo specie, forma e Gigantamax e a 298 contando solo specie e forma; 41 portano il fattore Gigantamax e 36 il cromatico garantito.

Fuori dagli eventi, letto dalle altre tabelle di `Encounters8` e `Encounters8Nest` per specie, forma e Gigantamax: 320 chiavi esistono anche nelle tane ordinarie, 22 soltanto in altri incontri (statici, grotte di cristallo, avventure Dynamax, selvatici, scambi), 5 si ottengono per allevamento o evoluzione da un altro incontro, 12 soltanto nelle incursioni di evento. Per una chiave senza fattore Gigantamax il confronto guarda anche la stessa specie con il fattore, perché il fattore non si eredita e la Zuppa Dynamax lo toglie, e gli altri membri della famiglia evolutiva nella stessa forma: le pre-evoluzioni, che si fanno evolvere, e le evoluzioni di una specie che si alleva, da cui nasce un uovo. Per una chiave con il fattore il confronto resta sulla sola terna, perché il fattore non viene da un uovo. Il confronto ignora il cromatico garantito, perché nessuna tana ordinaria lo garantisce.

Prova di ogni riga: il generatore costruisce un esemplare da ciascuna con l'allenatore del progetto e lo giudica con `LegalityAnalysis`. Righe legali 1286 su 1286; righe che la libreria riconosce come tana di distribuzione, e non come tana ordinaria o come un'altra riga con un diverso stato del cromatico, 1152; chiavi con almeno una riga riconosciuta 342. Il riconoscimento dipende dal seme casuale e varia di qualche unità fra una corsa e l'altra.

## Il cromatico garantito, e il suo opposto

Nelle tane la lucentezza viene dal seme: la libreria non forza il cromatico su una riga che lo garantisce, e un esemplare non cromatico nato da quella riga non vi si accorda. Il generatore chiede quindi il cromatico sulle righe che lo garantiscono e il non cromatico su tutte le altre, sia su quelle con il blocco, dove la libreria lo impone da sé, sia su quelle libere, dove un seme cromatico capita una volta su 4096 e darebbe all'esemplare la chiave sbagliata. Dopo la generazione lo stato ottenuto si confronta con quello atteso e un esemplare che non vi corrisponde non si scrive. Esito su questo lotto: 36 chiavi a cromatico garantito generate, 36 cromatiche; 0 esemplari cromatici fra le 25 chiavi senza garanzia.

Un limite della libreria va detto perché tocca proprio questi esemplari. Per un esemplare cromatico di tana la libreria non verifica la correlazione con il seme, e attribuisce l'esemplare al primo incontro compatibile che trova, spesso una tana ordinaria con la stessa specie: l'esemplare è conforme, ma il verificatore non sa dire che venga da un evento. Fra i generati sono 13, elencati nella tabella delle chiavi con l'incontro che la libreria riconosce.

## Copertura e generazione

I lotti esistenti si leggono tutti, `.pk8` per `.pk8` (5154 file letti, escluse le uscite di questo strumento, la cui cartella comincia con `lotto-incursioni-`); un file copre la chiave dell'esemplare quando la libreria lo riconosce come tana di distribuzione, oppure quando è nato da una tana di distribuzione e la libreria lo attribuisce a una tana ordinaria (462 file in questo caso). Chiavi coperte da `lotto-eventi-switch-scelta`, il lotto destinato a HOME: 298. Chiavi coperte da qualunque lotto: 323. Chiavi coperte soltanto da `lotto-eventi-switch-completo`: 25. Chiavi non coperte da alcun lotto: 36, tutte a cromatico garantito, perché `pkhex-eventi-switch` generava senza chiedere il cromatico.

Il generatore produce un esemplare per ogni chiave che il lotto destinato a HOME non copre, con l'allenatore del progetto per i soli campi che l'evento lasciava a chi riceveva, preferendo la riga riconosciuta come distribuzione, poi quella presente in entrambe le versioni, poi Spada, poi il livello più alto. Generati 61, non generabili 0; conformi nel registro dei giudizi, con la stessa impronta e giudicati con un salvataggio vuoto della versione del file, 61 su 61.

## Il confronto con la Wild Area News del 2021

La pagina Bulbapedia delle Wild Area News del 2021, nel testo recuperato in `_notes/fonti/corpus-residuo/recuperati-2026-10-05/wan2021.txt`, elenca 27 eventi, di cui 27 con una tabella di incontri, e 206 voci distinte per evento contate su specie, forma, Gigantamax e cromatico. Di queste 205 hanno la chiave nella libreria e 200 stanno nell'indice della libreria che ha più specie in comune con l'evento, misurato con l'indice di Jaccard sulle coppie di specie e forma. Le voci assenti dalla libreria sono 1.

- Cinderace (Gigantamax), evento «April 2 to 4, 2021», chiave `0815-0-G`: la pagina la descrive come incursione non catturabile, quindi la libreria correttamente non la porta.

| Evento | Indice | Somiglianza | Voci | Nella libreria | Nell'indice |
|---|---|---|---|---|---|
| December 17 to 26, 2021 | 93 | 1 | 4 | 4 | 4 |
| November 19 to 28, 2021 | 91 | 1 | 11 | 11 | 11 |
| October 29 to 31, 2021 | 89 | 1 | 11 | 11 | 11 |
| October 1 to 3, 2021 | 87 | 1 | 3 | 3 | 3 |
| September 17 to 19, 2021 | 85 | 1 | 4 | 4 | 4 |
| September 3 to 5, 2021 | 83 | 1 | 6 | 6 | 6 |
| August 20 to 22, 2021 | 81 | 1 | 9 | 9 | 9 |
| August 6 to 8, 2021 | 79 | 1 | 11 | 11 | 11 |
| July 23 to 25, 2021 | 77 | 1 | 4 | 4 | 4 |
| July 9 to 11, 2021 | 75 | 1 | 9 | 9 | 9 |
| June 25 to 27, 2021 | 73 | 1 | 7 | 7 | 7 |
| June 4 to 6, 2021 | 71 | 1 | 11 | 11 | 11 |
| May 21 to 23, 2021 | 69 | 1 | 3 | 3 | 3 |
| April 30 to May 2, 2021 | 67 | 1 | 5 | 5 | 4 |
| April 23 to 25, 2021 | 65 | 1 | 2 | 2 | 2 |
| April 5, 2021 to November 1, 2022 | 64 | 0.818 | 11 | 11 | 9 |
| April 2 to 4, 2021 | 63 | 0.857 | 8 | 7 | 7 |
| April 1, 2021 | 95 | 0.25 | 1 | 1 | 1 |
| March 26 to 28, 2021 | 60 | 1 | 10 | 10 | 10 |
| March 1 to 31, 2021 | 59 | 0.857 | 14 | 14 | 12 |
| February 27 to 28, 2021 | 58 | 1 | 15 | 15 | 15 |
| February 11 to 14, 2021 | 56 | 1 | 2 | 2 | 2 |
| February 4 to 8, 2021 | 54 | 1 | 6 | 6 | 6 |
| February 1 to 28, 2021 | 58 | 0.929 | 13 | 13 | 13 |
| January 22 to 24, 2021 | 51 | 1 | 4 | 4 | 4 |
| January 8 to 11, 2021 | 49 | 1 | 9 | 9 | 9 |
| January 1 to 31, 2021 | 48 | 1 | 13 | 13 | 13 |

L'evento del primo aprile 2021 portava soltanto Magikarp non catturabili, e la somiglianza bassa con il suo indice migliore lo riflette: la chiave di Magikarp esiste nella libreria per altri eventi.

## Le chiavi

Una riga per chiave di collezione. Versioni e indici sono quelli delle righe della libreria con quella chiave; «Copertura» nomina i lotti che la coprono, oppure il file generato in `lotto-incursioni-evento-swsh` con l'esito nel registro; «Incontro riconosciuto» è quello che la libreria attribuisce all'esemplare generato.

| Chiave | N. | Specie | Forma | G | S | Versioni | Indici di evento | Altrove | Copertura | Incontro riconosciuto |
|---|---|---|---|---|---|---|---|---|---|---|
| 0001-0 | 1 | Bulbasaur | - | - | - | SH SW | 12 | anche per allevamento o evoluzione da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0002-0 | 2 | Ivysaur | - | - | - | SH SW | 12 71 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0003-0 | 3 | Venusaur | - | - | - | SH SW | 71 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-071-SW-0003-0.pk8, conforme | Distribution Raid Den Encounter - 071 |
| 0003-0-G | 3 | Venusaur | - | sì | - | SH SW | 71 98 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0004-0 | 4 | Charmander | - | - | - | SH SW | 12 17 75 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0005-0 | 5 | Charmeleon | - | - | - | SH SW | 12 17 75 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0006-0-G | 6 | Charizard | - | sì | - | SH SW | 16 17 26 75 98 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0007-0 | 7 | Squirtle | - | - | - | SH SW | 12 | anche per allevamento o evoluzione da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0008-0 | 8 | Wartortle | - | - | - | SH SW | 12 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0009-0-G | 9 | Blastoise | - | sì | - | SH SW | 98 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0012-0 | 12 | Butterfree | - | - | - | SH SW | 1 5 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-001-SW-0012-0.pk8, conforme | Distribution Raid Den Encounter - 006 |
| 0012-0-G | 12 | Butterfree | - | sì | - | SH SW | 1 6 26 42 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0025-0 | 25 | Pikachu | - | - | - | SH SW | 34 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-034-SW-0025-0.pk8, conforme | Distribution Raid Den Encounter - 058 |
| 0025-0-G | 25 | Pikachu | - | sì | - | SH SW | 21 58 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0025-0-G-S | 25 | Pikachu | - | sì | sì | SH SW | 58 | anche da altri incontri | generato lotto-incursioni-evento-swsh-SW/Static8ND-058-SW-0025-0-G-S.pk8, conforme | Distribution Raid Den Encounter - 058 |
| 0025-0-S | 25 | Pikachu | - | - | sì | SH SW | 34 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-034-SW-0025-0-S.pk8, conforme | Distribution Raid Den Encounter - 058 |
| 0026-0 | 26 | Raichu | - | - | - | SH SW | 34 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0026-1 | 26 | Raichu | Alola | - | - | SH SW | 34 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0036-0 | 36 | Clefable | - | - | - | SH SW | 37 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0036-0-S | 36 | Clefable | - | - | sì | SH SW | 37 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-037-SW-0036-0-S.pk8, conforme | Stock Raid Den Encounter [032] 3-5★ |
| 0037-1 | 37 | Vulpix | Alola | - | - | SH SW | 46 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0037-1-S | 37 | Vulpix | Alola | - | sì | SH SW | 46 | anche da altri incontri | generato lotto-incursioni-evento-swsh-SW/Static8ND-046-SW-0037-1-S.pk8, conforme | Distribution Raid Den Encounter - 046 |
| 0040-0 | 40 | Wigglytuff | - | - | - | SH SW | 37 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0043-0 | 43 | Oddish | - | - | - | SH SW | 42 60 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0044-0 | 44 | Gloom | - | - | - | SH SW | 37 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0045-0 | 45 | Vileplume | - | - | - | SH SW | 42 60 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0052-0 | 52 | Meowth | - | - | - | SH SW | 95 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0052-0-G | 52 | Meowth | - | sì | - | SH SW | 23 67 | solo da incursioni di evento | generato lotto-incursioni-evento-swsh-SW/Static8ND-067-SW-0052-0-G.pk8, conforme | Distribution Raid Den Encounter - 067 |
| 0052-1 | 52 | Meowth | Alola | - | - | SH SW | 67 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0052-2 | 52 | Meowth | Galar | - | - | SH SW | 27 67 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0052-2-S | 52 | Meowth | Galar | - | sì | SH SW | 67 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-067-SW-0052-2-S.pk8, conforme | Distribution Raid Den Encounter - 067 |
| 0060-0 | 60 | Poliwag | - | - | - | SH SW | 71 109 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0061-0 | 61 | Poliwhirl | - | - | - | SH SW | 71 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0066-0 | 66 | Machop | - | - | - | SH SW | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0067-0 | 67 | Machoke | - | - | - | SH SW | 15 58 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0068-0 | 68 | Machamp | - | - | - | SH SW | 14 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-014-SW-0068-0.pk8, conforme | Distribution Raid Den Encounter - 015 |
| 0068-0-G | 68 | Machamp | - | sì | - | SH SW | 15 26 53 58 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0077-0 | 77 | Ponyta | - | - | - | SH SW | 45 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0077-1 | 77 | Ponyta | Galar | - | - | SW | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0078-0 | 78 | Rapidash | - | - | - | SH SW | 45 | anche per allevamento o evoluzione da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0078-1 | 78 | Rapidash | Galar | - | - | SW | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0083-1 | 83 | Farfetch’d | Galar | - | - | SH | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0090-0 | 90 | Shellder | - | - | - | SH SW | 104 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0090-0-S | 90 | Shellder | - | - | sì | SH SW | 104 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-104-SW-0090-0-S.pk8, conforme | Distribution Raid Den Encounter - 104 |
| 0092-0 | 92 | Gastly | - | - | - | SH SW | 15 81 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0093-0 | 93 | Haunter | - | - | - | SH SW | 15 40 81 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0094-0 | 94 | Gengar | - | - | - | SH SW | 14 81 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-081-SW-0094-0.pk8, conforme | Distribution Raid Den Encounter - 081 |
| 0094-0-G | 94 | Gengar | - | sì | - | SH SW | 15 40 81 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0095-0 | 95 | Onix | - | - | - | SH SW | 27 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0098-0 | 98 | Krabby | - | - | - | SH SW | 12 31 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0099-0 | 99 | Kingler | - | - | - | SH SW | 11 31 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-031-SW-0099-0.pk8, conforme | Stock Raid Den Encounter [041] 3-4★ |
| 0099-0-G | 99 | Kingler | - | sì | - | SH SW | 12 26 31 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0109-0 | 109 | Koffing | - | - | - | SH SW | 59 75 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0110-1 | 110 | Weezing | Galar | - | - | SH SW | 59 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0111-0 | 111 | Rhyhorn | - | - | - | SH SW | 27 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0112-0 | 112 | Rhydon | - | - | - | SH SW | 27 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0118-0 | 118 | Goldeen | - | - | - | SH SW | 79 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0119-0 | 119 | Seaking | - | - | - | SH SW | 79 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0121-0 | 121 | Starmie | - | - | - | SH SW | 93 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0124-0 | 124 | Jynx | - | - | - | SH SW | 46 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0127-0 | 127 | Pinsir | - | - | - | SH SW | 79 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0128-0 | 128 | Tauros | - | - | - | SH SW | 51 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0128-0-S | 128 | Tauros | - | - | sì | SH SW | 51 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-051-SW-0128-0-S.pk8, conforme | Distribution Raid Den Encounter - 051 |
| 0129-0 | 129 | Magikarp | - | - | - | SH SW | 6 95 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0129-0-S | 129 | Magikarp | - | - | sì | SH SW | 6 95 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-095-SW-0129-0-S.pk8, conforme | Distribution Raid Den Encounter - 095 |
| 0131-0 | 131 | Lapras | - | - | - | SH | 8 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SH/Static8ND-008-SH-0131-0.pk8, conforme | Distribution Raid Den Encounter - 117 |
| 0131-0-G | 131 | Lapras | - | sì | - | SH SW | 9 45 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0132-0 | 132 | Ditto | - | - | - | SH SW | 64 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0133-0 | 133 | Eevee | - | - | - | SH SW | 91 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0133-0-G | 133 | Eevee | - | sì | - | SH SW | 22 91 | anche da altri incontri | generato lotto-incursioni-evento-swsh-SW/Static8ND-091-SW-0133-0-G.pk8, conforme | Distribution Raid Den Encounter - 091 |
| 0133-0-S | 133 | Eevee | - | - | sì | SH SW | 91 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-091-SW-0133-0-S.pk8, conforme | Distribution Raid Den Encounter - 091 |
| 0134-0 | 134 | Vaporeon | - | - | - | SH SW | 91 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0135-0 | 135 | Jolteon | - | - | - | SH SW | 91 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0136-0 | 136 | Flareon | - | - | - | SH SW | 91 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0138-0 | 138 | Omanyte | - | - | - | SH SW | 77 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0138-0-S | 138 | Omanyte | - | - | sì | SH SW | 77 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-077-SW-0138-0-S.pk8, conforme | Distribution Raid Den Encounter - 077 |
| 0140-0 | 140 | Kabuto | - | - | - | SH SW | 77 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0142-0 | 142 | Aerodactyl | - | - | - | SH SW | 77 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0143-0 | 143 | Snorlax | - | - | - | SH SW | 5 14 15 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-014-SW-0143-0.pk8, conforme | Distribution Raid Den Encounter - 117 |
| 0143-0-G | 143 | Snorlax | - | sì | - | SH SW | 6 25 26 48 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0172-0 | 172 | Pichu | - | - | - | SH SW | 17 34 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0173-0 | 173 | Cleffa | - | - | - | SH SW | 17 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0175-0 | 175 | Togepi | - | - | - | SH SW | 17 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0176-0 | 176 | Togetic | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0182-0 | 182 | Bellossom | - | - | - | SH SW | 37 60 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0183-0 | 183 | Marill | - | - | - | SH SW | 63 109 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0183-0-S | 183 | Marill | - | - | sì | SH SW | 109 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-109-SW-0183-0-S.pk8, conforme | Distribution Raid Den Encounter - 109 |
| 0184-0 | 184 | Azumarill | - | - | - | SH SW | 63 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0184-0-S | 184 | Azumarill | - | - | sì | SH SW | 63 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-063-SW-0184-0-S.pk8, conforme | Distribution Raid Den Encounter - 063 |
| 0185-0 | 185 | Sudowoodo | - | - | - | SH SW | 102 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0185-0-S | 185 | Sudowoodo | - | - | sì | SH SW | 102 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-102-SW-0185-0-S.pk8, conforme | Stock Raid Den Encounter [002] 3-5★ |
| 0186-0 | 186 | Politoed | - | - | - | SH SW | 71 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0186-0-S | 186 | Politoed | - | - | sì | SH SW | 71 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-071-SW-0186-0-S.pk8, conforme | Stock Raid Den Encounter [132] 5★ |
| 0194-0 | 194 | Wooper | - | - | - | SH SW | 33 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0195-0 | 195 | Quagsire | - | - | - | SH SW | 33 54 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0196-0 | 196 | Espeon | - | - | - | SH SW | 91 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0197-0 | 197 | Umbreon | - | - | - | SH SW | 91 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0202-0 | 202 | Wobbuffet | - | - | - | SH SW | 75 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0208-0 | 208 | Steelix | - | - | - | SH SW | 27 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0213-0 | 213 | Shuckle | - | - | - | SH SW | 42 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0214-0 | 214 | Heracross | - | - | - | SH SW | 79 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0222-1 | 222 | Corsola | Galar | - | - | SW | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0223-0 | 223 | Remoraid | - | - | - | SH SW | 73 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0224-0 | 224 | Octillery | - | - | - | SH SW | 73 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0225-0 | 225 | Delibird | - | - | - | SH SW | 3 46 93 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0225-0-S | 225 | Delibird | - | - | sì | SH SW | 93 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-093-SW-0225-0-S.pk8, conforme | Distribution Raid Den Encounter - 093 |
| 0226-0 | 226 | Mantine | - | - | - | SH SW | 31 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0236-0 | 236 | Tyrogue | - | - | - | SH SW | 17 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0241-0 | 241 | Miltank | - | - | - | SH SW | 51 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0246-0 | 246 | Larvitar | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0247-0 | 247 | Pupitar | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0248-0 | 248 | Tyranitar | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0280-0 | 280 | Ralts | - | - | - | SH SW | 59 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0281-0 | 281 | Kirlia | - | - | - | SH SW | 59 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0282-0 | 282 | Gardevoir | - | - | - | SH SW | 59 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0290-0 | 290 | Nincada | - | - | - | SH SW | 42 79 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0291-0 | 291 | Ninjask | - | - | - | SH SW | 42 79 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0302-0 | 302 | Sableye | - | - | - | SH SW | 89 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0318-0 | 318 | Carvanha | - | - | - | SH SW | 31 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0319-0 | 319 | Sharpedo | - | - | - | SH SW | 31 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0320-0 | 320 | Wailmer | - | - | - | SH SW | 31 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0321-0 | 321 | Wailord | - | - | - | SH SW | 31 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0321-0-S | 321 | Wailord | - | - | sì | SH SW | 31 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-031-SW-0321-0-S.pk8, conforme | Distribution Raid Den Encounter - 031 |
| 0330-0 | 330 | Flygon | - | - | - | SH SW | 54 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0333-0 | 333 | Swablu | - | - | - | SH SW | 83 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0334-0 | 334 | Altaria | - | - | - | SH SW | 83 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0337-0 | 337 | Lunatone | - | - | - | SH SW | 85 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0337-0-S | 337 | Lunatone | - | - | sì | SH SW | 85 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-085-SW-0337-0-S.pk8, conforme | Distribution Raid Den Encounter - 085 |
| 0338-0 | 338 | Solrock | - | - | - | SH SW | 85 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0338-0-S | 338 | Solrock | - | - | sì | SH SW | 85 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-085-SW-0338-0-S.pk8, conforme | Stock Raid Den Encounter [001] 5★ |
| 0349-0 | 349 | Feebas | - | - | - | SH SW | 33 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0350-0 | 350 | Milotic | - | - | - | SH SW | 33 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0355-0 | 355 | Duskull | - | - | - | SH SW | 89 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0360-0 | 360 | Wynaut | - | - | - | SH SW | 17 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0363-0 | 363 | Spheal | - | - | - | SH SW | 109 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0406-0 | 406 | Budew | - | - | - | SH SW | 17 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0420-0 | 420 | Cherubi | - | - | - | SH SW | 49 60 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0421-0 | 421 | Cherrim | Nuvola | - | - | SH SW | 60 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0422-1 | 422 | Shellos | Est | - | - | SH SW | 33 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0423-1 | 423 | Gastrodon | Est | - | - | SH SW | 33 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0425-0 | 425 | Drifloon | - | - | - | SH SW | 40 81 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0426-0 | 426 | Drifblim | - | - | - | SH SW | 40 81 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0427-0 | 427 | Buneary | - | - | - | SH SW | 63 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0428-0 | 428 | Lopunny | - | - | - | SH SW | 63 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0438-0 | 438 | Bonsly | - | - | - | SH SW | 102 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0439-0 | 439 | Mime Jr. | - | - | - | SH SW | 17 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0446-0 | 446 | Munchlax | - | - | - | SH SW | 5 17 48 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0447-0 | 447 | Riolu | - | - | - | SH SW | 17 58 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0448-0 | 448 | Lucario | - | - | - | SH SW | 53 58 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0449-0 | 449 | Hippopotas | - | - | - | SH SW | 33 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0450-0 | 450 | Hippowdon | - | - | - | SH SW | 33 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0453-0 | 453 | Croagunk | - | - | - | SH SW | 42 71 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0454-0 | 454 | Toxicroak | - | - | - | SH SW | 42 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0458-0 | 458 | Mantyke | - | - | - | SH SW | 17 31 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0461-0 | 461 | Weavile | - | - | - | SH SW | 45 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0464-0 | 464 | Rhyperior | - | - | - | SH SW | 27 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0468-0 | 468 | Togekiss | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0470-0 | 470 | Leafeon | - | - | - | SH SW | 91 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0471-0 | 471 | Glaceon | - | - | - | SH SW | 91 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0477-0 | 477 | Dusknoir | - | - | - | SH SW | 89 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0479-1 | 479 | Rotom | Calore | - | - | SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0479-2 | 479 | Rotom | Lavaggio | - | - | SH | 19 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0479-4 | 479 | Rotom | Vortice | - | - | SH SW | 79 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0479-5 | 479 | Rotom | Taglio | - | - | SH SW | 83 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0518-0 | 518 | Musharna | - | - | - | SH SW | 37 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0529-0 | 529 | Drilbur | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0530-0 | 530 | Excadrill | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0535-0 | 535 | Tympole | - | - | - | SH SW | 71 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0536-0 | 536 | Palpitoad | - | - | - | SH SW | 71 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0537-0 | 537 | Seismitoad | - | - | - | SH SW | 71 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0546-0 | 546 | Cottonee | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0547-0 | 547 | Whimsicott | - | - | - | SH SW | 20 37 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0549-0 | 549 | Lilligant | - | - | - | SH SW | 37 60 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0549-0-S | 549 | Lilligant | - | - | sì | SH SW | 60 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-060-SW-0549-0-S.pk8, conforme | Distribution Raid Den Encounter - 060 |
| 0554-0 | 554 | Darumaka | - | - | - | SH SW | 95 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0554-1 | 554 | Darumaka | Galar | - | - | SH | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0555-0 | 555 | Darmanitan | - | - | - | SH SW | 95 | anche per allevamento o evoluzione da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0562-0 | 562 | Yamask | - | - | - | SH SW | 41 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0563-0 | 563 | Cofagrigus | - | - | - | SH SW | 41 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0564-0 | 564 | Tirtouga | - | - | - | SH SW | 100 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0565-0 | 565 | Carracosta | - | - | - | SH SW | 100 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0566-0 | 566 | Archen | - | - | - | SH SW | 100 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0567-0 | 567 | Archeops | - | - | - | SH SW | 100 | anche per allevamento o evoluzione da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0568-0 | 568 | Trubbish | - | - | - | SH SW | 17 42 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0569-0-G | 569 | Garbodor | - | sì | - | SH SW | 16 17 42 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0570-0 | 570 | Zorua | - | - | - | SH SW | 89 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0571-0 | 571 | Zoroark | - | - | - | SH SW | 89 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0571-0-S | 571 | Zoroark | - | - | sì | SH SW | 89 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-089-SW-0571-0-S.pk8, conforme | Distribution Raid Den Encounter - 089 |
| 0572-0 | 572 | Minccino | - | - | - | SH SW | 48 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0573-0 | 573 | Cinccino | - | - | - | SH SW | 48 83 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0573-0-S | 573 | Cinccino | - | - | sì | SH SW | 83 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-083-SW-0573-0-S.pk8, conforme | Stock Raid Den Encounter [038] 5★ |
| 0574-0 | 574 | Gothita | - | - | - | SH SW | 58 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0575-0 | 575 | Gothorita | - | - | - | SH SW | 58 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0576-0 | 576 | Gothitelle | - | - | - | SH SW | 53 58 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0577-0 | 577 | Solosis | - | - | - | SH SW | 58 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0578-0 | 578 | Duosion | - | - | - | SH SW | 58 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0579-0 | 579 | Reuniclus | - | - | - | SH SW | 53 58 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0582-0 | 582 | Vanillite | - | - | - | SH SW | 79 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0583-0 | 583 | Vanillish | - | - | - | SH SW | 79 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0584-0 | 584 | Vanilluxe | - | - | - | SH SW | 79 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0584-0-S | 584 | Vanilluxe | - | - | sì | SH SW | 79 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-079-SW-0584-0-S.pk8, conforme | Distribution Raid Den Encounter - 079 |
| 0588-0 | 588 | Karrablast | - | - | - | SH SW | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0589-0 | 589 | Escavalier | - | - | - | SH SW | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0590-0 | 590 | Foongus | - | - | - | SH SW | 49 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0591-0 | 591 | Amoonguss | - | - | - | SH SW | 43 49 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0592-0 | 592 | Frillish | - | - | - | SH SW | 31 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0593-0 | 593 | Jellicent | - | - | - | SH SW | 31 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0597-0 | 597 | Ferroseed | - | - | - | SH SW | 36 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0598-0 | 598 | Ferrothorn | - | - | - | SH SW | 36 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0607-0 | 607 | Litwick | - | - | - | SH SW | 46 81 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0608-0 | 608 | Lampent | - | - | - | SH SW | 46 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0609-0 | 609 | Chandelure | - | - | - | SH SW | 46 81 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0609-0-S | 609 | Chandelure | - | - | sì | SH SW | 81 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-081-SW-0609-0-S.pk8, conforme | Distribution Raid Den Encounter - 081 |
| 0610-0 | 610 | Axew | - | - | - | SH SW | 48 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0611-0 | 611 | Fraxure | - | - | - | SH SW | 48 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0612-0 | 612 | Haxorus | - | - | - | SH SW | 48 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0615-0 | 615 | Cryogonal | - | - | - | SH SW | 93 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0616-0 | 616 | Shelmet | - | - | - | SH SW | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0617-0 | 617 | Accelgor | - | - | - | SH SW | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0623-0 | 623 | Golurk | - | - | - | SH SW | 54 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0626-0 | 626 | Bouffalant | - | - | - | SH SW | 51 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0627-0 | 627 | Rufflet | - | - | - | SH SW | 59 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0628-0 | 628 | Braviary | - | - | - | SH SW | 15 59 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0630-0 | 630 | Mandibuzz | - | - | - | SW | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0633-0 | 633 | Deino | - | - | - | SH SW | 40 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0634-0 | 634 | Zweilous | - | - | - | SH SW | 40 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0635-0 | 635 | Hydreigon | - | - | - | SH SW | 40 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0659-0 | 659 | Bunnelby | - | - | - | SH SW | 63 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0660-0 | 660 | Diggersby | - | - | - | SH SW | 63 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0686-0 | 686 | Inkay | - | - | - | SH SW | 73 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0687-0 | 687 | Malamar | - | - | - | SH SW | 73 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0695-0 | 695 | Heliolisk | - | - | - | SH SW | 36 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0696-0 | 696 | Tyrunt | - | - | - | SH SW | 100 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0697-0 | 697 | Tyrantrum | - | - | - | SH SW | 100 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0697-0-S | 697 | Tyrantrum | - | - | sì | SH SW | 100 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-100-SW-0697-0-S.pk8, conforme | Distribution Raid Den Encounter - 100 |
| 0698-0 | 698 | Amaura | - | - | - | SH SW | 100 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0699-0 | 699 | Aurorus | - | - | - | SH SW | 100 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0700-0 | 700 | Sylveon | - | - | - | SH SW | 91 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0704-0 | 704 | Goomy | - | - | - | SH SW | 48 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0705-0 | 705 | Sliggoo | - | - | - | SH SW | 48 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0706-0 | 706 | Goodra | - | - | - | SH SW | 48 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0709-0 | 709 | Trevenant | - | - | - | SH SW | 41 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0710-0 | 710 | Pumpkaboo | - | - | - | SH SW | 41 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0711-0 | 711 | Gourgeist | - | - | - | SH SW | 41 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0711-1 | 711 | Gourgeist | Mini | - | - | SH SW | 41 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0711-1-S | 711 | Gourgeist | Mini | - | sì | SH SW | 41 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-041-SW-0711-1-S.pk8, conforme | Distribution Raid Den Encounter - 041 |
| 0711-2 | 711 | Gourgeist | Grande | - | - | SH SW | 41 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0711-3 | 711 | Gourgeist | Maxi | - | - | SH SW | 41 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0711-3-S | 711 | Gourgeist | Maxi | - | sì | SH SW | 41 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-041-SW-0711-3-S.pk8, conforme | Distribution Raid Den Encounter - 041 |
| 0712-0 | 712 | Bergmite | - | - | - | SH SW | 45 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0713-0 | 713 | Avalugg | - | - | - | SH SW | 45 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0722-0 | 722 | Rowlet | - | - | - | SH SW | 87 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0725-0 | 725 | Litten | - | - | - | SH SW | 87 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0728-0 | 728 | Popplio | - | - | - | SH SW | 87 | anche da altri incontri | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0753-0 | 753 | Fomantis | - | - | - | SH SW | 60 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0754-0 | 754 | Lurantis | - | - | - | SH SW | 60 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0755-0 | 755 | Morelull | - | - | - | SH SW | 49 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0756-0 | 756 | Shiinotic | - | - | - | SH SW | 49 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0759-0 | 759 | Stufful | - | - | - | SH SW | 48 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0760-0 | 760 | Bewear | - | - | - | SH SW | 48 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0764-0 | 764 | Comfey | - | - | - | SH SW | 60 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0765-0 | 765 | Oranguru | - | - | - | SW | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0766-0 | 766 | Passimian | - | - | - | SH | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0767-0 | 767 | Wimpod | - | - | - | SH SW | 83 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0771-0 | 771 | Pyukumuku | - | - | - | SH SW | 31 113 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0776-0 | 776 | Turtonator | - | - | - | SH SW | 45 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0778-0 | 778 | Mimikyu | Mascherata | - | - | SH SW | 41 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0819-0 | 819 | Skwovet | - | - | - | SH SW | 49 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0819-0-S | 819 | Skwovet | - | - | sì | SH SW | 49 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-049-SW-0819-0-S.pk8, conforme | Distribution Raid Den Encounter - 049 |
| 0820-0 | 820 | Greedent | - | - | - | SH SW | 49 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0820-0-S | 820 | Greedent | - | - | sì | SH SW | 49 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-049-SW-0820-0-S.pk8, conforme | Distribution Raid Den Encounter - 049 |
| 0821-0 | 821 | Rookidee | - | - | - | SH SW | 1 6 89 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0822-0 | 822 | Corvisquire | - | - | - | SH SW | 1 6 89 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0823-0 | 823 | Corviknight | - | - | - | SH SW | 1 89 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0823-0-G | 823 | Corviknight | - | sì | - | SH SW | 6 26 59 117 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-117-SW-0823-0-G.pk8, conforme | Distribution Raid Den Encounter - 117 |
| 0824-0 | 824 | Blipbug | - | - | - | SH SW | 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0825-0 | 825 | Dottler | - | - | - | SH SW | 12 58 64 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0826-0 | 826 | Orbeetle | - | - | - | SH SW | 11 64 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0826-0-G | 826 | Orbeetle | - | sì | - | SH SW | 10 12 26 53 58 117 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-117-SW-0826-0-G.pk8, conforme | Distribution Raid Den Encounter - 117 |
| 0827-0 | 827 | Nickit | - | - | - | SH SW | 89 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0828-0 | 828 | Thievul | - | - | - | SH SW | 89 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0829-0 | 829 | Gossifleur | - | - | - | SH SW | 36 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0830-0 | 830 | Eldegoss | - | - | - | SH SW | 36 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0831-0 | 831 | Wooloo | - | - | - | SH SW | 64 69 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0831-0-S | 831 | Wooloo | - | - | sì | SH SW | 69 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-069-SW-0831-0-S.pk8, conforme | Distribution Raid Den Encounter - 069 |
| 0832-0 | 832 | Dubwool | - | - | - | SH SW | 64 69 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0833-0 | 833 | Chewtle | - | - | - | SH SW | 1 6 64 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0834-0 | 834 | Drednaw | - | - | - | SH SW | 5 6 64 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-064-SW-0834-0.pk8, conforme | Distribution Raid Den Encounter - 117 |
| 0834-0-G | 834 | Drednaw | - | sì | - | SH SW | 6 33 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0835-0 | 835 | Yamper | - | - | - | SH SW | 36 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0836-0 | 836 | Boltund | - | - | - | SH SW | 36 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0837-0 | 837 | Rolycoly | - | - | - | SH SW | 8 27 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0838-0 | 838 | Carkol | - | - | - | SH SW | 8 27 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0839-0 | 839 | Coalossal | - | - | - | SW | 8 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-008-SW-0839-0.pk8, conforme | Distribution Raid Den Encounter - 117 |
| 0839-0-G | 839 | Coalossal | - | sì | - | SH SW | 9 27 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0840-0 | 840 | Applin | - | - | - | SH SW | 8 36 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0841-0 | 841 | Flapple | - | - | - | SW | 8 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-008-SW-0841-0.pk8, conforme | Distribution Raid Den Encounter - 117 |
| 0841-0-G | 841 | Flapple | - | sì | - | SH SW | 8 9 26 36 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0842-0 | 842 | Appletun | - | - | - | SH | 8 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SH/Static8ND-008-SH-0842-0.pk8, conforme | Distribution Raid Den Encounter - 009 |
| 0842-0-G | 842 | Appletun | - | sì | - | SH SW | 9 26 36 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0843-0 | 843 | Silicobra | - | - | - | SH SW | 1 6 33 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0844-0 | 844 | Sandaconda | - | - | - | SW | 1 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-001-SW-0844-0.pk8, conforme | Distribution Raid Den Encounter - 117 |
| 0844-0-G | 844 | Sandaconda | - | sì | - | SH SW | 3 6 26 33 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0845-0 | 845 | Cramorant | - | - | - | SH SW | 54 59 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0845-0-S | 845 | Cramorant | - | - | sì | SH SW | 54 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-054-SW-0845-0-S.pk8, conforme | Distribution Raid Den Encounter - 054 |
| 0848-0 | 848 | Toxel | - | - | - | SH SW | 17 36 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0849-0 | 849 | Toxtricity | Melodia | - | - | SW | 11 12 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-011-SW-0849-0.pk8, conforme | Distribution Raid Den Encounter - 012 |
| 0849-0-G | 849 | Toxtricity | Melodia | sì | - | SH SW | 10 12 36 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0849-1 | 849 | Toxtricity | Basso | - | - | SH | 11 12 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SH/Static8ND-011-SH-0849-1.pk8, conforme | Distribution Raid Den Encounter - 012 |
| 0849-1-G | 849 | Toxtricity | Basso | sì | - | SH SW | 10 12 36 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0850-0 | 850 | Sizzlipede | - | - | - | SH SW | 1 2 6 64 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0851-0 | 851 | Centiskorch | - | - | - | SH SW | 1 5 6 64 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-064-SW-0851-0.pk8, conforme | Distribution Raid Den Encounter - 117 |
| 0851-0-G | 851 | Centiskorch | - | sì | - | SH SW | 6 26 45 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0852-0 | 852 | Clobbopus | - | - | - | SH SW | 73 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0853-0 | 853 | Grapploct | - | - | - | SH SW | 73 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0853-0-S | 853 | Grapploct | - | - | sì | SH SW | 73 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-073-SW-0853-0-S.pk8, conforme | Stock Raid Den Encounter [009] 5★ |
| 0855-0 | 855 | Polteageist | Contraffatta | - | - | SH SW | 41 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0856-0 | 856 | Hatenna | - | - | - | SH SW | 12 59 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0857-0 | 857 | Hattrem | - | - | - | SH | 12 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SH/Static8ND-012-SH-0857-0.pk8, conforme | Distribution Raid Den Encounter - 012 |
| 0857-0-G | 857 | Hattrem | - | sì | - | SH SW | 59 | solo da incursioni di evento | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0858-0 | 858 | Hatterene | - | - | - | SH | 11 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SH/Static8ND-011-SH-0858-0.pk8, conforme | Distribution Raid Den Encounter - 012 |
| 0858-0-G | 858 | Hatterene | - | sì | - | SH SW | 12 59 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0859-0 | 859 | Impidimp | - | - | - | SH SW | 12 40 111 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0860-0 | 860 | Morgrem | - | - | - | SH SW | 12 40 111 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0861-0 | 861 | Grimmsnarl | - | - | - | SH SW | 11 111 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-111-SW-0861-0.pk8, conforme | Distribution Raid Den Encounter - 111 |
| 0861-0-G | 861 | Grimmsnarl | - | sì | - | SH SW | 12 26 40 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0861-0-S | 861 | Grimmsnarl | - | - | sì | SH SW | 111 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-111-SW-0861-0-S.pk8, conforme | Distribution Raid Den Encounter - 111 |
| 0863-0 | 863 | Perrserker | - | - | - | SH SW | 27 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0865-0 | 865 | Sirfetch’d | - | - | - | SH | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0868-0 | 868 | Milcery | - | - | - | SH SW | 8 75 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0868-0-G | 868 | Milcery | - | sì | - | SH SW | 56 | solo da incursioni di evento | generato lotto-incursioni-evento-swsh-SW/Static8ND-056-SW-0868-0-G.pk8, conforme | Distribution Raid Den Encounter - 056 |
| 0868-0-G-S | 868 | Milcery | - | sì | sì | SH SW | 56 | solo da incursioni di evento | generato lotto-incursioni-evento-swsh-SW/Static8ND-056-SW-0868-0-G-S.pk8, conforme | Distribution Raid Den Encounter - 056 |
| 0869-0-G | 869 | Alcremie | Lattevaniglia | sì | - | SH SW | 8 26 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0869-1-G | 869 | Alcremie | Latterosa | sì | - | SH SW | 8 | solo da incursioni di evento | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0869-2-G | 869 | Alcremie | Lattematcha | sì | - | SH SW | 8 | solo da incursioni di evento | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0869-3-G | 869 | Alcremie | Lattementa | sì | - | SH SW | 8 | solo da incursioni di evento | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0869-4-G | 869 | Alcremie | Lattelimone | sì | - | SH SW | 8 | solo da incursioni di evento | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0869-5-G | 869 | Alcremie | Lattesale | sì | - | SW | 8 | solo da incursioni di evento | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0869-6-G | 869 | Alcremie | Rosamix | sì | - | SW | 8 | solo da incursioni di evento | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0869-7-G | 869 | Alcremie | Caramelmix | sì | - | SH | 8 | solo da incursioni di evento | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0869-8-G | 869 | Alcremie | Triplomix | sì | - | SH | 8 | solo da incursioni di evento | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0870-0 | 870 | Falinks | - | - | - | SH SW | 53 58 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0871-0 | 871 | Pincurchin | - | - | - | SH SW | 15 113 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0872-0 | 872 | Snom | - | - | - | SH SW | 113 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0872-0-S | 872 | Snom | - | - | sì | SH SW | 113 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-113-SW-0872-0-S.pk8, conforme | Distribution Raid Den Encounter - 113 |
| 0873-0 | 873 | Frosmoth | - | - | - | SH SW | 46 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0875-0 | 875 | Eiscue | Gelofaccia | - | - | SH SW | 65 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0875-0-S | 875 | Eiscue | Gelofaccia | - | sì | SH SW | 65 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-065-SW-0875-0-S.pk8, conforme | Distribution Raid Den Encounter - 065 |
| 0876-0 | 876 | Indeedee | ♂ | - | - | SH | 15 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0876-1 | 876 | Indeedee | ♀ | - | - | SH SW | 15 54 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0877-0 | 877 | Morpeko | Panciapiena | - | - | SH SW | 40 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0878-0 | 878 | Cufant | - | - | - | SH SW | 17 27 75 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0879-0-G | 879 | Copperajah | - | sì | - | SH SW | 16 27 75 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0879-0-G-S | 879 | Copperajah | - | sì | sì | SH SW | 75 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-075-SW-0879-0-G-S.pk8, conforme | Distribution Raid Den Encounter - 117 |
| 0884-0 | 884 | Duraludon | - | - | - | SH SW | 17 | anche da tane ordinarie | generato lotto-incursioni-evento-swsh-SW/Static8ND-017-SW-0884-0.pk8, conforme | Distribution Raid Den Encounter - 048 |
| 0884-0-G | 884 | Duraludon | - | sì | - | SH SW | 16 17 48 117 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0885-0 | 885 | Dreepy | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0886-0 | 886 | Drakloak | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
| 0887-0 | 887 | Dragapult | - | - | - | SH SW | 20 | anche da tane ordinarie | lotto-eventi-switch-completo, lotto-eventi-switch-scelta | - |
