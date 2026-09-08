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

## Quelli che nessun nostro esemplare porta (69 su 76)

E' la lista di lavoro dell'asse, e va letta sapendo che comprende cose di natura molto diversa: fiocchi di gara che si conquistano giocando, fiocchi di ricordo che un gioco assegna una volta sola, e fiocchi che soltanto una distribuzione conferiva. Il passo successivo e' classificarli per via di conferimento, che e' l'informazione che decide quali siano perduti con la chiusura.

| Fiocco | Nome umano |
|---|---|
| RibbonChampionSinnoh | Sinnoh Champion |
| RibbonAbility | Ability |
| RibbonAbilityGreat | Great Ability |
| RibbonAbilityDouble | Double Ability |
| RibbonAbilityMulti | Multi Ability |
| RibbonAbilityPair | Pair Ability |
| RibbonAbilityWorld | World Ability |
| RibbonAlert | Alert |
| RibbonShock | Shock |
| RibbonDowncast | Downcast |
| RibbonCareless | Careless |
| RibbonRelax | Relax |
| RibbonSnooze | Snooze |
| RibbonSmile | Smile |
| RibbonGorgeous | Gorgeous |
| RibbonRoyal | Royal |
| RibbonGorgeousRoyal | Gorgeous Royal |
| RibbonFootprint | Footprint |
| RibbonRecord | Record |
| RibbonLegend | Legend |
| RibbonChampionWorld | World Champion |
| RibbonSpecial | Special |
| RibbonG3Cool | Cool (G3) |
| RibbonG3CoolSuper | Cool Super |
| RibbonG3CoolHyper | Cool Hyper |
| RibbonG3CoolMaster | Cool Master |
| RibbonG3Beauty | Beauty (G3) |
| RibbonG3BeautySuper | Beauty Super |
| RibbonG3BeautyHyper | Beauty Hyper |
| RibbonG3BeautyMaster | Beauty Master |
| RibbonG3Cute | Cute (G3) |
| RibbonG3CuteSuper | Cute Super |
| RibbonG3CuteHyper | Cute Hyper |
| RibbonG3CuteMaster | Cute Master |
| RibbonG3Smart | Smart (G3) |
| RibbonG3SmartSuper | Smart Super |
| RibbonG3SmartHyper | Smart Hyper |
| RibbonG3SmartMaster | Smart Master |
| RibbonG3Tough | Tough (G3) |
| RibbonG3ToughSuper | Tough Super |
| RibbonG3ToughHyper | Tough Hyper |
| RibbonG3ToughMaster | Tough Master |
| RibbonChampionG3 | Champion (Gen3) |
| RibbonWinning | Winning |
| RibbonVictory | Victory |
| RibbonArtist | Artist |
| RibbonEffort | Effort |
| RibbonChampionRegional | Regional Champion |
| RibbonChampionNational | National Champion |
| RibbonCountry | Country |
| RibbonNational | National |
| RibbonEarth | Earth |
| RibbonWorld | World |
| RibbonG4Cool | Cool (G4) |
| RibbonG4CoolGreat | Cool Great |
| RibbonG4CoolUltra | Cool Ultra |
| RibbonG4CoolMaster | Cool Master |
| RibbonG4Beauty | Beauty (G4) |
| RibbonG4BeautyGreat | Beauty Great |
| RibbonG4BeautyUltra | Beauty Ultra |
| RibbonG4BeautyMaster | Beauty Master |
| RibbonG4Cute | Cute (G4) |
| RibbonG4CuteGreat | Cute Great |
| RibbonG4CuteUltra | Cute Ultra |
| RibbonG4CuteMaster | Cute Master |
| RibbonG4Smart | Smart (G4) |
| RibbonG4SmartGreat | Smart Great |
| RibbonG4SmartUltra | Smart Ultra |
| RibbonG4SmartMaster | Smart Master |
