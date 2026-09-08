# L'asse dei fiocchi: enumerazione e copertura

> Documento generato da `tools/fiocchi.py`. Non si modifica a mano: si rigenera. Le posizioni dei bit sono lette dal sorgente del verificatore e non trascritte, per la ragione gia' pagata due volte da questo progetto su tabelle lunghe.

Il formato di quarta e quinta generazione dichiara 76 fiocchi distinti, distribuiti in 10 byte dell'esemplare. La terza generazione ne tiene trentadue in una parola sola dentro la propria sottostruttura varia.

Va detto subito cio' che questa misura non dice, perche' e' la domanda che verra' subito dopo: dice quali fiocchi i nostri lotti portano, non quali siano ancora ottenibili oggi. Un fiocco assente dai lotti puo' essere ancora conferito da un gioco corrente oppure essere perduto con la chiusura, e distinguere i due casi richiede le regole di conferimento e non le posizioni dei bit.

## Terza generazione, i trentadue della parola dei meriti

Sui 186 esemplari dei due lotti di terza generazione.

| Fiocco | Esemplari che lo portano |
|---|---|
| RibbonCountG3Cool | 0 |
| RibbonCountG3Beauty | 0 |
| RibbonCountG3Cute | 0 |
| RibbonCountG3Smart | 0 |
| RibbonCountG3Tough | 0 |
| RibbonChampionG3 | 0 |
| RibbonWinning | 0 |
| RibbonVictory | 0 |
| RibbonArtist | 0 |
| RibbonEffort | 0 |
| RibbonChampionBattle | 0 |
| RibbonChampionRegional | 0 |
| RibbonChampionNational | 0 |
| RibbonCountry | 0 |
| RibbonNational | 2 |
| RibbonEarth | 0 |
| RibbonWorld | 0 |

## Quarta e quinta generazione

Sui 247 esemplari di quarta e 700 di quinta. La colonna del nome umano viene dalla tabella dei testi, unita alle posizioni sulla chiave e mai sulla posizione, perche' le due tabelle non hanno lo stesso ordine ne' la stessa cardinalita'.

| Fiocco | Nome umano | Byte | Bit | Quarta | Quinta |
|---|---|---|---|---|---|
| RibbonChampionSinnoh | Sinnoh Champion | 0x24 | 0 | 0 | 0 |
| RibbonAbility | Ability | 0x24 | 1 | 0 | 0 |
| RibbonAbilityGreat | Great Ability | 0x24 | 2 | 0 | 0 |
| RibbonAbilityDouble | Double Ability | 0x24 | 3 | 0 | 0 |
| RibbonAbilityMulti | Multi Ability | 0x24 | 4 | 0 | 0 |
| RibbonAbilityPair | Pair Ability | 0x24 | 5 | 0 | 0 |
| RibbonAbilityWorld | World Ability | 0x24 | 6 | 0 | 0 |
| RibbonAlert | Alert | 0x24 | 7 | 0 | 0 |
| RibbonShock | Shock | 0x25 | 0 | 0 | 0 |
| RibbonDowncast | Downcast | 0x25 | 1 | 0 | 0 |
| RibbonCareless | Careless | 0x25 | 2 | 0 | 0 |
| RibbonRelax | Relax | 0x25 | 3 | 0 | 0 |
| RibbonSnooze | Snooze | 0x25 | 4 | 0 | 0 |
| RibbonSmile | Smile | 0x25 | 5 | 0 | 0 |
| RibbonGorgeous | Gorgeous | 0x25 | 6 | 0 | 0 |
| RibbonRoyal | Royal | 0x25 | 7 | 0 | 0 |
| RibbonGorgeousRoyal | Gorgeous Royal | 0x26 | 0 | 0 | 0 |
| RibbonFootprint | Footprint | 0x26 | 1 | 0 | 0 |
| RibbonRecord | Record | 0x26 | 2 | 0 | 0 |
| RibbonEvent | Event | 0x26 | 3 | 0 | 81 |
| RibbonLegend | Legend | 0x26 | 4 | 0 | 0 |
| RibbonChampionWorld | World Champion | 0x26 | 5 | 0 | 0 |
| RibbonBirthday | Birthday | 0x26 | 6 | 0 | 20 |
| RibbonSpecial | Special | 0x26 | 7 | 0 | 0 |
| RibbonSouvenir | Souvenir | 0x27 | 0 | 0 | 268 |
| RibbonWishing | Wishing | 0x27 | 1 | 0 | 75 |
| RibbonClassic | Classic | 0x27 | 2 | 194 | 199 |
| RibbonPremier | Premier | 0x27 | 3 | 7 | 7 |
| RibbonG3Cool | Cool (G3) | 0x3C | 0 | 0 | 0 |
| RibbonG3CoolSuper | Cool Super | 0x3C | 1 | 0 | 0 |
| RibbonG3CoolHyper | Cool Hyper | 0x3C | 2 | 0 | 0 |
| RibbonG3CoolMaster | Cool Master | 0x3C | 3 | 0 | 0 |
| RibbonG3Beauty | Beauty (G3) | 0x3C | 4 | 0 | 0 |
| RibbonG3BeautySuper | Beauty Super | 0x3C | 5 | 0 | 0 |
| RibbonG3BeautyHyper | Beauty Hyper | 0x3C | 6 | 0 | 0 |
| RibbonG3BeautyMaster | Beauty Master | 0x3C | 7 | 0 | 0 |
| RibbonG3Cute | Cute (G3) | 0x3D | 0 | 0 | 0 |
| RibbonG3CuteSuper | Cute Super | 0x3D | 1 | 0 | 0 |
| RibbonG3CuteHyper | Cute Hyper | 0x3D | 2 | 0 | 0 |
| RibbonG3CuteMaster | Cute Master | 0x3D | 3 | 0 | 0 |
| RibbonG3Smart | Smart (G3) | 0x3D | 4 | 0 | 0 |
| RibbonG3SmartSuper | Smart Super | 0x3D | 5 | 0 | 0 |
| RibbonG3SmartHyper | Smart Hyper | 0x3D | 6 | 0 | 0 |
| RibbonG3SmartMaster | Smart Master | 0x3D | 7 | 0 | 0 |
| RibbonG3Tough | Tough (G3) | 0x3E | 0 | 0 | 0 |
| RibbonG3ToughSuper | Tough Super | 0x3E | 1 | 0 | 0 |
| RibbonG3ToughHyper | Tough Hyper | 0x3E | 2 | 0 | 0 |
| RibbonG3ToughMaster | Tough Master | 0x3E | 3 | 0 | 0 |
| RibbonChampionG3 | Champion (Gen3) | 0x3E | 4 | 0 | 0 |
| RibbonWinning | Winning | 0x3E | 5 | 0 | 0 |
| RibbonVictory | Victory | 0x3E | 6 | 0 | 0 |
| RibbonArtist | Artist | 0x3E | 7 | 0 | 0 |
| RibbonEffort | Effort | 0x3F | 0 | 0 | 0 |
| RibbonChampionBattle | Battle Champion | 0x3F | 1 | 0 | 2 |
| RibbonChampionRegional | Regional Champion | 0x3F | 2 | 0 | 0 |
| RibbonChampionNational | National Champion | 0x3F | 3 | 0 | 0 |
| RibbonCountry | Country | 0x3F | 4 | 0 | 0 |
| RibbonNational | National | 0x3F | 5 | 0 | 0 |
| RibbonEarth | Earth | 0x3F | 6 | 0 | 0 |
| RibbonWorld | World | 0x3F | 7 | 0 | 0 |
| RibbonG4Cool | Cool (G4) | 0x60 | 0 | 0 | 0 |
| RibbonG4CoolGreat | Cool Great | 0x60 | 1 | 0 | 0 |
| RibbonG4CoolUltra | Cool Ultra | 0x60 | 2 | 0 | 0 |
| RibbonG4CoolMaster | Cool Master | 0x60 | 3 | 0 | 0 |
| RibbonG4Beauty | Beauty (G4) | 0x60 | 4 | 0 | 0 |
| RibbonG4BeautyGreat | Beauty Great | 0x60 | 5 | 0 | 0 |
| RibbonG4BeautyUltra | Beauty Ultra | 0x60 | 6 | 0 | 0 |
| RibbonG4BeautyMaster | Beauty Master | 0x60 | 7 | 0 | 0 |
| RibbonG4Cute | Cute (G4) | 0x61 | 0 | 0 | 0 |
| RibbonG4CuteGreat | Cute Great | 0x61 | 1 | 0 | 0 |
| RibbonG4CuteUltra | Cute Ultra | 0x61 | 2 | 0 | 0 |
| RibbonG4CuteMaster | Cute Master | 0x61 | 3 | 0 | 0 |
| RibbonG4Smart | Smart (G4) | 0x61 | 4 | 0 | 0 |
| RibbonG4SmartGreat | Smart Great | 0x61 | 5 | 0 | 0 |
| RibbonG4SmartUltra | Smart Ultra | 0x61 | 6 | 0 | 0 |
| RibbonG4SmartMaster | Smart Master | 0x61 | 7 | 0 | 0 |

## L'asse intero, e la parte che i nostri formati sanno rappresentare

La tabella dei nomi del verificatore elenca 164 fiocchi, ed e' l'asse. Il formato di quarta e quinta generazione ne rappresenta 76, cioe' quelli che esistevano fino alla quinta: gli altri vivono nei formati successivi e nessun nostro lotto puo' portarli, perche' i nostri lotti arrivano alla quinta. Enumerare l'asse dal formato invece che dalla tabella dei nomi e' l'errore che questa sezione esiste per non far commettere: il conto torna e il denominatore e' sbagliato.

## Quelli rappresentabili che nessun nostro esemplare porta (69 su 76)

E' la lista di lavoro dell'asse, e comprende cose di natura molto diversa: fiocchi di gara che si conquistano giocando, fiocchi di ricordo che un gioco assegna una volta sola, e fiocchi che soltanto una distribuzione conferiva. La classificazione per via di conferimento e' quella che decide quali siano perduti con la chiusura, ed e' qui sotto.

La classificazione che segue viene dal raggruppamento che il verificatore stesso fa dei fiocchi in insiemi, uno per generazione: quel raggruppamento e' letto dal sorgente, mentre l'attribuzione di ciascun insieme alla propria generazione e la conseguenza sulla scadenza sono un nostro giudizio, dichiarato dentro il programma. Il criterio e' che un fiocco si perde con la chiusura quando il solo gioco che lo conferisce raggiunge il deposito attraverso la banca; basta invece un solo insieme di console corrente perche' resti conquistabile.

Va dichiarata una approssimazione, perche' rende questo conto un limite superiore e non un numero esatto. Le riedizioni della quarta generazione per console corrente riconferiscono una parte dei fiocchi di quarta, e il verificatore lo esprime dentro condizioni che questo programma non interpreta: alcune voci contate qui come perdute sono quindi riconquistabili la'. Distinguerle richiede di leggere quelle condizioni una per una, ed e' il passo successivo.

| Esito | Quanti |
|---|---|
| perduti con la chiusura, al piu' | 69 |
| conquistabili su console corrente | 0 |
| non trattati da alcun insieme | 0 |

### Perduti con la chiusura, al piu' (69)

| Fiocco | Nome umano | Insiemi che lo trattano |
|---|---|---|
| RibbonChampionSinnoh | Sinnoh Champion | comuni di quarta generazione |
| RibbonAbility | Ability | gara e abilita' di quarta generazione |
| RibbonAbilityGreat | Great Ability | gara e abilita' di quarta generazione |
| RibbonAbilityDouble | Double Ability | gara e abilita' di quarta generazione |
| RibbonAbilityMulti | Multi Ability | gara e abilita' di quarta generazione |
| RibbonAbilityPair | Pair Ability | gara e abilita' di quarta generazione |
| RibbonAbilityWorld | World Ability | gara e abilita' di quarta generazione |
| RibbonAlert | Alert | comuni di quarta generazione |
| RibbonShock | Shock | comuni di quarta generazione |
| RibbonDowncast | Downcast | comuni di quarta generazione |
| RibbonCareless | Careless | comuni di quarta generazione |
| RibbonRelax | Relax | comuni di quarta generazione |
| RibbonSnooze | Snooze | comuni di quarta generazione |
| RibbonSmile | Smile | comuni di quarta generazione |
| RibbonGorgeous | Gorgeous | comuni di quarta generazione |
| RibbonRoyal | Royal | comuni di quarta generazione |
| RibbonGorgeousRoyal | Gorgeous Royal | comuni di quarta generazione |
| RibbonFootprint | Footprint | comuni di quarta generazione |
| RibbonRecord | Record | comuni di quarta generazione |
| RibbonLegend | Legend | comuni di quarta generazione |
| RibbonChampionWorld | World Champion | conferiti da distribuzioni di quarta generazione |
| RibbonSpecial | Special | conferiti da distribuzioni di quarta generazione |
| RibbonG3Cool | Cool (G3) | gara e abilita' di quarta generazione |
| RibbonG3CoolSuper | Cool Super | gara e abilita' di quarta generazione |
| RibbonG3CoolHyper | Cool Hyper | gara e abilita' di quarta generazione |
| RibbonG3CoolMaster | Cool Master | gara e abilita' di quarta generazione |
| RibbonG3Beauty | Beauty (G3) | gara e abilita' di quarta generazione |
| RibbonG3BeautySuper | Beauty Super | gara e abilita' di quarta generazione |
| RibbonG3BeautyHyper | Beauty Hyper | gara e abilita' di quarta generazione |
| RibbonG3BeautyMaster | Beauty Master | gara e abilita' di quarta generazione |
| RibbonG3Cute | Cute (G3) | gara e abilita' di quarta generazione |
| RibbonG3CuteSuper | Cute Super | gara e abilita' di quarta generazione |
| RibbonG3CuteHyper | Cute Hyper | gara e abilita' di quarta generazione |
| RibbonG3CuteMaster | Cute Master | gara e abilita' di quarta generazione |
| RibbonG3Smart | Smart (G3) | gara e abilita' di quarta generazione |
| RibbonG3SmartSuper | Smart Super | gara e abilita' di quarta generazione |
| RibbonG3SmartHyper | Smart Hyper | gara e abilita' di quarta generazione |
| RibbonG3SmartMaster | Smart Master | gara e abilita' di quarta generazione |
| RibbonG3Tough | Tough (G3) | gara e abilita' di quarta generazione |
| RibbonG3ToughSuper | Tough Super | gara e abilita' di quarta generazione |
| RibbonG3ToughHyper | Tough Hyper | gara e abilita' di quarta generazione |
| RibbonG3ToughMaster | Tough Master | gara e abilita' di quarta generazione |
| RibbonChampionG3 | Champion (Gen3) | gara e campione di terza generazione |
| RibbonWinning | Winning | unici della terza generazione |
| RibbonVictory | Victory | unici della terza generazione |
| RibbonArtist | Artist | gara e campione di terza generazione |
| RibbonEffort | Effort | gara e campione di terza generazione |
| RibbonChampionRegional | Regional Champion | conferiti da distribuzioni di terza generazione |
| RibbonChampionNational | National Champion | conferiti da distribuzioni di terza generazione |
| RibbonCountry | Country | conferiti da distribuzioni di terza generazione |
| RibbonNational | National | conferiti da distribuzioni di terza generazione |
| RibbonEarth | Earth | conferiti da distribuzioni di terza generazione |
| RibbonWorld | World | esclusivi della terza generazione; conferiti da distribuzioni di quarta generazione |
| RibbonG4Cool | Cool (G4) | gara e abilita' di quarta generazione |
| RibbonG4CoolGreat | Cool Great | gara e abilita' di quarta generazione |
| RibbonG4CoolUltra | Cool Ultra | gara e abilita' di quarta generazione |
| RibbonG4CoolMaster | Cool Master | gara e abilita' di quarta generazione |
| RibbonG4Beauty | Beauty (G4) | gara e abilita' di quarta generazione |
| RibbonG4BeautyGreat | Beauty Great | gara e abilita' di quarta generazione |
| RibbonG4BeautyUltra | Beauty Ultra | gara e abilita' di quarta generazione |
| RibbonG4BeautyMaster | Beauty Master | gara e abilita' di quarta generazione |
| RibbonG4Cute | Cute (G4) | gara e abilita' di quarta generazione |
| RibbonG4CuteGreat | Cute Great | gara e abilita' di quarta generazione |
| RibbonG4CuteUltra | Cute Ultra | gara e abilita' di quarta generazione |
| RibbonG4CuteMaster | Cute Master | gara e abilita' di quarta generazione |
| RibbonG4Smart | Smart (G4) | gara e abilita' di quarta generazione |
| RibbonG4SmartGreat | Smart Great | gara e abilita' di quarta generazione |
| RibbonG4SmartUltra | Smart Ultra | gara e abilita' di quarta generazione |
| RibbonG4SmartMaster | Smart Master | gara e abilita' di quarta generazione |

### Conquistabili su console corrente (0)

| Fiocco | Nome umano | Insiemi che lo trattano |
|---|---|---|

### Non trattati da alcun insieme del verificatore (0)

| Fiocco | Nome umano | Insiemi che lo trattano |
|---|---|---|

## La parte dell'asse fuori dai nostri formati (88)

Sono i fiocchi introdotti dalla sesta generazione in avanti, piu' i contrassegni della nona. Nessun esemplare dei nostri lotti puo' portarli, e non e' una lacuna della produzione ma una proprieta' del perimetro: i lotti arrivano alla quinta generazione. Si ottengono giocando i titoli che li conferiscono, e per quelli di ottava e nona generazione la chiusura non li tocca.

| Insieme che li tratta | Quanti |
|---|---|
| nessun insieme lo tratta | 45 |
| comuni di sesta generazione | 14 |
| contrassegni di nona generazione, su console corrente | 8 |
| comuni di ottava generazione, su console corrente | 5 |
| esclusivi della terza generazione | 5 |
| comuni di settima generazione | 4 |
| gara e abilita' di quarta generazione | 4 |
| comuni di nona generazione, su console corrente | 3 |
