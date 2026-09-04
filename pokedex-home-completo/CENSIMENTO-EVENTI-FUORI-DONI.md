# Censimento degli esemplari da evento fuori dalla base dei doni segreti

> Documento generato da `tools/censimento-eventi-tabelle.py`. Non si modifica a mano: si rigenera. La fonte sono le tabelle degli incontri di PKHeX, che il programma legge dal clone passato sulla riga di comando.

Questo censimento esiste perché l'asse degli eventi della lista di spunta nasce da due sole fonti, cioè la tabella delle carte meraviglia di terza generazione e i file binari della base dei doni segreti, ed è cieco su tutto ciò che il verificatore tiene altrove. Il difetto è di copertura e non di lettura, quindi non produce alcun errore e non si manifesta da sé: una distribuzione che nessuna tabella letta dichiara semplicemente non compare, e la lista sembra completa.

Le classi restano separate, e non è una precauzione formale. Una distribuzione in cui il dono era un oggetto è un evento a tutti gli effetti, e la sola ragione per cui sfugge è che il verificatore la tiene fra gli incontri statici; un esemplare di Colosseum non è invece una distribuzione ma un incontro ordinario di un gioco diverso, irripetibile altrove; un dono condizionato di ottava generazione pretende il salvataggio di un altro gioco e non una consegna. Sommarle darebbe un totale grande e inutilizzabile, e deciderebbe al posto di chi colleziona quale sia l'ambito.

## Il conto per gruppo

| Classe | Gen | Gruppo | Voci | Specie distinte | Sotto scadenza |
|---|---|---|---|---|---|
| oggetto-distribuito | varie | Distribuzioni in cui il dono era un oggetto | 15 | 9 | sì |
| disco-bonus | 3 | Colosseum, disco bonus, solo Giappone | 2 | 2 | sì |
| periferica | 4 | My Pokemon Ranch | 22 | 22 | sì |
| periferica | 5 | Dream Radar | 26 | 26 | sì |
| periferica | 4 | Pokewalker | 162 | 118 | sì |
| spinoff | 3 | Colosseum, premio del Monte Lotta | 1 | 1 | sì |
| spinoff | 3 | Colosseum, iniziali | 2 | 2 | sì |
| spinoff | 3 | Colosseum, doni | 1 | 1 | sì |
| spinoff | 3 | Colosseum, ombra | 80 | 48 | sì |
| spinoff | 3 | XD, doni | 4 | 4 | sì |
| spinoff | 3 | XD, scambi | 4 | 4 | sì |
| spinoff | 3 | XD, ombra | 90 | 83 | sì |
| condizionato | 8 | Leggende Arceus, doni fatidici | 6 | 5 | no |
| condizionato | 8 | Diamante Lucente e Perla Splendente, doni fatidici | 6 | 5 | no |
| condizionato | 8 | Spada e Scudo, doni fatidici | 1 | 1 | no |
| incursione | 8 | Spada e Scudo, incursioni delle grotte di cristallo | 13 | 13 | no |
| incursione | 8 | Spada, incursioni da distribuzione | 1171 | 273 | no |
| incursione | 8 | Scudo, incursioni da distribuzione | 1179 | 273 | no |
| incursione | 8 | Spada e Scudo, avventure Dynamax nei sotterranei | 273 | 262 | no |
| incursione | 9 | Scarlatto e Violetto, incursioni da distribuzione | 174 | 53 | no |
| incursione | 9 | Scarlatto e Violetto, esemplari di potere | 56 | 50 | no |
| porta-permanente | 8 | Pokemon GO verso il deposito | 1164 | 948 | no |
| porta-permanente | 7 | Pokemon GO verso Let's Go | 170 | 152 | no |

Le voci censite sono 4622 e portano 980 specie distinte; quelle sotto scadenza sono 409 e portano 251 specie distinte. Fino al 2026-09-04 nessuna di esse compariva nella lista di spunta, che le ignorava tutte: da quella data `tools/checklist-pokedex.py` invoca questo programma e le voci entrano nel suo asse degli eventi con la classe dichiarata e il codice `EVT-T-`. Il numero da guardare per misurare quanto pesassero è quello delle specie distinte sotto scadenza, perché è la parte che il primo tempo della coda deve coprire e che prima non sapeva di dover coprire.

## Le voci che nessuna fonte dichiara distribuite

Vanno scritte perché la loro assenza dal censimento è un risultato e non una lacuna: chi le cercasse senza questa sezione concluderebbe che il censimento sia incompleto, e cercherebbe per giorni una distribuzione che non è mai avvenuta.

| Gen | Oggetto | Luogo | Dex | Perché non c'è |
|---|---|---|---|---|
| 4 | Flauto Azzurro | Colonna Lancia | 493 | il verificatore non porta alcuna voce per questo incontro, cioe' non fu mai distribuito per via ufficiale in alcuna regione |
| 4 | Lettera di Oak | Giardino Floreale | 492 | in Diamante e Perla la voce esiste nella fonte ma e' commentata come non distribuita: la ebbe soltanto Platino |

## Che cosa questo censimento non copre

Nessuna, fra le classi che il verificatore porta. Il 2026-09-04 questa sezione elencava tre classi non lette, cioè le incursioni da distribuzione di ottava e di nona generazione e i trasferimenti da Pokemon GO, e nella stessa giornata sono state lette tutte e tre: la dichiarazione di non lettura era onesta, ma era un debito e non una conclusione. Resta vero, e va ripetuto qui perché è il limite di questo documento, che il censimento copre ciò che il verificatore sa: una distribuzione che nessuna sua tabella conosce non comparirebbe, e non avremmo modo di accorgercene da dentro.

## Distribuzioni in cui il dono era un oggetto

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 380 | 0 | Biglietto Eone, Isola del Sud, Rubino, livello 50 | `Encounters3RSE.cs StaticR` |
| 381 | 0 | Biglietto Eone, Isola del Sud, Zaffiro, livello 50 | `Encounters3RSE.cs StaticS` |
| 380 | 0 | Biglietto Eone, Isola del Sud, Smeraldo, livello 50 | `Encounters3RSE.cs StaticE` |
| 381 | 0 | Biglietto Eone, Isola del Sud, Smeraldo, livello 50 | `Encounters3RSE.cs StaticE` |
| 151 | 0 | Carta Mare Antica, Isola Lontana, Smeraldo, livello 30 | `Encounters3RSE.cs StaticE, la fonte annota che fuori dal Giappone non fu distribuita` |
| 249 | 0 | Biglietto Mistico, Rocca Ombelico, Smeraldo, livello 70 | `Encounters3RSE.cs StaticE` |
| 250 | 0 | Biglietto Mistico, Rocca Ombelico, Smeraldo, livello 70 | `Encounters3RSE.cs StaticE` |
| 386 | 3 | Biglietto Aurora, Isola Nascita, Smeraldo, livello 30 | `Encounters3RSE.cs StaticE, forma Velocita'` |
| 249 | 0 | Biglietto Mistico, Rocca Ombelico, Rosso Fuoco e Verde Foglia, livello 70 | `Encounters3FRLG.cs` |
| 250 | 0 | Biglietto Mistico, Rocca Ombelico, Rosso Fuoco e Verde Foglia, livello 70 | `Encounters3FRLG.cs` |
| 386 | 1 | Biglietto Aurora, Isola Nascita, Rosso Fuoco, livello 30 | `Encounters3FRLG.cs StaticFR, forma Attacco` |
| 386 | 2 | Biglietto Aurora, Isola Nascita, Verde Foglia, livello 30 | `Encounters3FRLG.cs StaticLG, forma Difesa` |
| 491 | 0 | Tessera Membro, Isola Lunanova, Platino, livello 50 | `Encounters4DPPt.cs, in Diamante e Perla la voce e' commentata come non distribuita` |
| 492 | 0 | Lettera di Oak, Giardino Floreale, Platino, livello 30 | `Encounters4DPPt.cs, in Diamante e Perla la voce e' commentata come non distribuita` |
| 494 | 0 | Passo Liberta', Giardino Liberta', Nero e Bianco, livello 15 | `Encounters5BW.cs, la fonte dichiara che non puo' essere cromatico` |

## Colosseum, disco bonus, solo Giappone

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 25 | 0 | Colosseum Pikachu bonus gift | `Gen3/Encounters3RSE.cs ColoGiftsR` |
| 251 | 0 | Ageto Celebi bonus gift | `Gen3/Encounters3RSE.cs ColoGiftsR` |

## My Pokemon Ranch

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 25 | 0 | Pikachu | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 37 | 0 | Vulpix | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 77 | 0 | Ponyta | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 108 | 0 | Lickitung | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 114 | 0 | Tangela | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 133 | 0 | Eevee | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 142 | 0 | Aerodactyl | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 193 | 0 | Yanma | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 241 | 0 | Miltank | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 285 | 0 | Shroomish | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 320 | 0 | Wailmer | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 360 | 0 | Wynaut | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 397 | 0 | Staravia | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 415 | 0 | Combee | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 417 | 0 | Pachirisu | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 422 | 1 | Shellos | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 427 | 0 | Buneary | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 453 | 0 | Croagunk | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 456 | 0 | Finneon | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 459 | 0 | Snover | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 50 | 0 | Mew | `Gen4/Encounters4DPPt.cs RanchGifts` |
| 1 | 0 | Phione | `Gen4/Encounters4DPPt.cs RanchGifts` |

## Dream Radar

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 79 | 0 | Slowpoke | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 120 | 0 | Staryu | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 137 | 0 | Porygon | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 163 | 0 | Hoothoot | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 174 | 0 | Igglybuff | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 175 | 0 | Togepi | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 213 | 0 | Shuckle | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 238 | 0 | Smoochum | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 249 | 0 | Lugia (SoulSilver cart) | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 250 | 0 | Ho-Oh (HeartGold cart) | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 280 | 0 | Ralts | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 333 | 0 | Swablu | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 374 | 0 | Beldum | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 425 | 0 | Drifloon | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 436 | 0 | Bronzor | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 442 | 0 | Spiritomb | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 447 | 0 | Riolu | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 479 | 0 | Rotom (no HA) | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 483 | 0 | Dialga (Diamond cart) | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 484 | 0 | Palkia (Pearl cart) | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 487 | 0 | Giratina (Platinum cart) | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 517 | 0 | Munna | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 561 | 0 | Sigilyph | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 641 | 0 | Therian Tornadus | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 642 | 0 | Therian Thundurus | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |
| 645 | 0 | Therian Landorus | `Gen5/Encounters5DR.cs Encounter_DreamRadar` |

## Pokewalker

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 115 | 0 | corso Prato Ristoro, livello 8, corso in dotazione | `encounter_walker4.pkl, corso Prato Ristoro` |
| 84 | 0 | corso Prato Ristoro, livello 8, corso in dotazione | `encounter_walker4.pkl, corso Prato Ristoro` |
| 29 | 0 | corso Prato Ristoro, livello 5, corso in dotazione | `encounter_walker4.pkl, corso Prato Ristoro` |
| 32 | 0 | corso Prato Ristoro, livello 5, corso in dotazione | `encounter_walker4.pkl, corso Prato Ristoro` |
| 16 | 0 | corso Prato Ristoro, livello 5, corso in dotazione | `encounter_walker4.pkl, corso Prato Ristoro` |
| 161 | 0 | corso Prato Ristoro, livello 5, corso in dotazione | `encounter_walker4.pkl, corso Prato Ristoro` |
| 202 | 0 | corso Bosco Rumoroso, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Bosco Rumoroso` |
| 69 | 0 | corso Bosco Rumoroso, livello 8, corso in dotazione | `encounter_walker4.pkl, corso Bosco Rumoroso` |
| 48 | 0 | corso Bosco Rumoroso, livello 6, corso in dotazione | `encounter_walker4.pkl, corso Bosco Rumoroso` |
| 46 | 0 | corso Bosco Rumoroso, livello 6, corso in dotazione | `encounter_walker4.pkl, corso Bosco Rumoroso` |
| 43 | 0 | corso Bosco Rumoroso, livello 5, corso in dotazione | `encounter_walker4.pkl, corso Bosco Rumoroso` |
| 21 | 0 | corso Bosco Rumoroso, livello 5, corso in dotazione | `encounter_walker4.pkl, corso Bosco Rumoroso` |
| 240 | 0 | corso Strada Sconnessa, livello 9, corso in dotazione | `encounter_walker4.pkl, corso Strada Sconnessa` |
| 95 | 0 | corso Strada Sconnessa, livello 9, corso in dotazione | `encounter_walker4.pkl, corso Strada Sconnessa` |
| 66 | 0 | corso Strada Sconnessa, livello 7, corso in dotazione | `encounter_walker4.pkl, corso Strada Sconnessa` |
| 77 | 0 | corso Strada Sconnessa, livello 7, corso in dotazione | `encounter_walker4.pkl, corso Strada Sconnessa` |
| 163 | 0 | corso Strada Sconnessa, livello 6, corso in dotazione | `encounter_walker4.pkl, corso Strada Sconnessa` |
| 74 | 0 | corso Strada Sconnessa, livello 8, corso in dotazione | `encounter_walker4.pkl, corso Strada Sconnessa` |
| 54 | 0 | corso Bella Spiaggia, livello 10, corso in dotazione | `encounter_walker4.pkl, corso Bella Spiaggia` |
| 120 | 0 | corso Bella Spiaggia, livello 10, corso in dotazione | `encounter_walker4.pkl, corso Bella Spiaggia` |
| 79 | 0 | corso Bella Spiaggia, livello 8, corso in dotazione | `encounter_walker4.pkl, corso Bella Spiaggia` |
| 60 | 0 | corso Bella Spiaggia, livello 8, corso in dotazione | `encounter_walker4.pkl, corso Bella Spiaggia` |
| 191 | 0 | corso Bella Spiaggia, livello 6, corso in dotazione | `encounter_walker4.pkl, corso Bella Spiaggia` |
| 194 | 0 | corso Bella Spiaggia, livello 6, corso in dotazione | `encounter_walker4.pkl, corso Bella Spiaggia` |
| 239 | 0 | corso Zona Suburbana, livello 11, corso in dotazione | `encounter_walker4.pkl, corso Zona Suburbana` |
| 81 | 0 | corso Zona Suburbana, livello 11, corso in dotazione | `encounter_walker4.pkl, corso Zona Suburbana` |
| 81 | 0 | corso Zona Suburbana, livello 8, corso in dotazione | `encounter_walker4.pkl, corso Zona Suburbana` |
| 198 | 0 | corso Zona Suburbana, livello 11, corso in dotazione | `encounter_walker4.pkl, corso Zona Suburbana` |
| 163 | 0 | corso Zona Suburbana, livello 7, corso in dotazione | `encounter_walker4.pkl, corso Zona Suburbana` |
| 19 | 0 | corso Zona Suburbana, livello 7, corso in dotazione | `encounter_walker4.pkl, corso Zona Suburbana` |
| 238 | 0 | corso Grotta Buia, livello 12, corso in dotazione | `encounter_walker4.pkl, corso Grotta Buia` |
| 92 | 0 | corso Grotta Buia, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Grotta Buia` |
| 92 | 0 | corso Grotta Buia, livello 10, corso in dotazione | `encounter_walker4.pkl, corso Grotta Buia` |
| 95 | 0 | corso Grotta Buia, livello 10, corso in dotazione | `encounter_walker4.pkl, corso Grotta Buia` |
| 41 | 0 | corso Grotta Buia, livello 8, corso in dotazione | `encounter_walker4.pkl, corso Grotta Buia` |
| 66 | 0 | corso Grotta Buia, livello 8, corso in dotazione | `encounter_walker4.pkl, corso Grotta Buia` |
| 147 | 0 | corso Lago Blu, livello 10, corso in dotazione | `encounter_walker4.pkl, corso Lago Blu` |
| 60 | 0 | corso Lago Blu, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Lago Blu` |
| 98 | 0 | corso Lago Blu, livello 12, corso in dotazione | `encounter_walker4.pkl, corso Lago Blu` |
| 90 | 0 | corso Lago Blu, livello 12, corso in dotazione | `encounter_walker4.pkl, corso Lago Blu` |
| 118 | 0 | corso Lago Blu, livello 9, corso in dotazione | `encounter_walker4.pkl, corso Lago Blu` |
| 72 | 0 | corso Lago Blu, livello 9, corso in dotazione | `encounter_walker4.pkl, corso Lago Blu` |
| 63 | 0 | corso Periferia, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Periferia` |
| 100 | 0 | corso Periferia, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Periferia` |
| 109 | 0 | corso Periferia, livello 13, corso in dotazione | `encounter_walker4.pkl, corso Periferia` |
| 88 | 0 | corso Periferia, livello 13, corso in dotazione | `encounter_walker4.pkl, corso Periferia` |
| 19 | 0 | corso Periferia, livello 16, corso in dotazione | `encounter_walker4.pkl, corso Periferia` |
| 162 | 0 | corso Periferia, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Periferia` |
| 300 | 0 | corso Prato di Hoenn, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Prato di Hoenn` |
| 264 | 0 | corso Prato di Hoenn, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Prato di Hoenn` |
| 314 | 0 | corso Prato di Hoenn, livello 25, corso in dotazione | `encounter_walker4.pkl, corso Prato di Hoenn` |
| 313 | 0 | corso Prato di Hoenn, livello 25, corso in dotazione | `encounter_walker4.pkl, corso Prato di Hoenn` |
| 263 | 0 | corso Prato di Hoenn, livello 17, corso in dotazione | `encounter_walker4.pkl, corso Prato di Hoenn` |
| 265 | 0 | corso Prato di Hoenn, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Prato di Hoenn` |
| 320 | 0 | corso Spiaggia Calda, livello 31, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Calda` |
| 298 | 0 | corso Spiaggia Calda, livello 20, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Calda` |
| 116 | 0 | corso Spiaggia Calda, livello 20, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Calda` |
| 318 | 0 | corso Spiaggia Calda, livello 26, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Calda` |
| 118 | 0 | corso Spiaggia Calda, livello 22, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Calda` |
| 129 | 0 | corso Spiaggia Calda, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Calda` |
| 218 | 0 | corso Via del Vulcano, livello 31, corso in dotazione | `encounter_walker4.pkl, corso Via del Vulcano` |
| 307 | 0 | corso Via del Vulcano, livello 32, corso in dotazione | `encounter_walker4.pkl, corso Via del Vulcano` |
| 228 | 0 | corso Via del Vulcano, livello 27, corso in dotazione | `encounter_walker4.pkl, corso Via del Vulcano` |
| 111 | 0 | corso Via del Vulcano, livello 25, corso in dotazione | `encounter_walker4.pkl, corso Via del Vulcano` |
| 77 | 0 | corso Via del Vulcano, livello 19, corso in dotazione | `encounter_walker4.pkl, corso Via del Vulcano` |
| 74 | 0 | corso Via del Vulcano, livello 29, corso in dotazione | `encounter_walker4.pkl, corso Via del Vulcano` |
| 352 | 0 | corso Casa sull Albero, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Casa sull Albero` |
| 351 | 0 | corso Casa sull Albero, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Casa sull Albero` |
| 203 | 0 | corso Casa sull Albero, livello 28, corso in dotazione | `encounter_walker4.pkl, corso Casa sull Albero` |
| 234 | 0 | corso Casa sull Albero, livello 28, corso in dotazione | `encounter_walker4.pkl, corso Casa sull Albero` |
| 44 | 0 | corso Casa sull Albero, livello 14, corso in dotazione | `encounter_walker4.pkl, corso Casa sull Albero` |
| 70 | 0 | corso Casa sull Albero, livello 13, corso in dotazione | `encounter_walker4.pkl, corso Casa sull Albero` |
| 105 | 0 | corso Grotta Spaventosa, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Grotta Spaventosa` |
| 128 | 0 | corso Grotta Spaventosa, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Grotta Spaventosa` |
| 42 | 0 | corso Grotta Spaventosa, livello 33, corso in dotazione | `encounter_walker4.pkl, corso Grotta Spaventosa` |
| 177 | 0 | corso Grotta Spaventosa, livello 24, corso in dotazione | `encounter_walker4.pkl, corso Grotta Spaventosa` |
| 66 | 0 | corso Grotta Spaventosa, livello 13, corso in dotazione | `encounter_walker4.pkl, corso Grotta Spaventosa` |
| 92 | 0 | corso Grotta Spaventosa, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Grotta Spaventosa` |
| 439 | 0 | corso Prato di Sinnoh, livello 29, corso in dotazione | `encounter_walker4.pkl, corso Prato di Sinnoh` |
| 415 | 0 | corso Prato di Sinnoh, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Prato di Sinnoh` |
| 403 | 0 | corso Prato di Sinnoh, livello 33, corso in dotazione | `encounter_walker4.pkl, corso Prato di Sinnoh` |
| 406 | 0 | corso Prato di Sinnoh, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Prato di Sinnoh` |
| 399 | 0 | corso Prato di Sinnoh, livello 13, corso in dotazione | `encounter_walker4.pkl, corso Prato di Sinnoh` |
| 401 | 0 | corso Prato di Sinnoh, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Prato di Sinnoh` |
| 459 | 0 | corso Strada Ghiacciata, livello 31, corso in dotazione | `encounter_walker4.pkl, corso Strada Ghiacciata` |
| 361 | 0 | corso Strada Ghiacciata, livello 28, corso in dotazione | `encounter_walker4.pkl, corso Strada Ghiacciata` |
| 215 | 0 | corso Strada Ghiacciata, livello 28, corso in dotazione | `encounter_walker4.pkl, corso Strada Ghiacciata` |
| 436 | 0 | corso Strada Ghiacciata, livello 20, corso in dotazione | `encounter_walker4.pkl, corso Strada Ghiacciata` |
| 220 | 0 | corso Strada Ghiacciata, livello 16, corso in dotazione | `encounter_walker4.pkl, corso Strada Ghiacciata` |
| 179 | 0 | corso Strada Ghiacciata, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Strada Ghiacciata` |
| 357 | 0 | corso Grande Foresta, livello 35, corso in dotazione | `encounter_walker4.pkl, corso Grande Foresta` |
| 438 | 0 | corso Grande Foresta, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Grande Foresta` |
| 114 | 0 | corso Grande Foresta, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Grande Foresta` |
| 400 | 0 | corso Grande Foresta, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Grande Foresta` |
| 179 | 0 | corso Grande Foresta, livello 19, corso in dotazione | `encounter_walker4.pkl, corso Grande Foresta` |
| 102 | 0 | corso Grande Foresta, livello 17, corso in dotazione | `encounter_walker4.pkl, corso Grande Foresta` |
| 433 | 0 | corso Lago Bianco, livello 22, corso in dotazione | `encounter_walker4.pkl, corso Lago Bianco` |
| 200 | 0 | corso Lago Bianco, livello 32, corso in dotazione | `encounter_walker4.pkl, corso Lago Bianco` |
| 93 | 0 | corso Lago Bianco, livello 25, corso in dotazione | `encounter_walker4.pkl, corso Lago Bianco` |
| 418 | 0 | corso Lago Bianco, livello 28, corso in dotazione | `encounter_walker4.pkl, corso Lago Bianco` |
| 223 | 0 | corso Lago Bianco, livello 19, corso in dotazione | `encounter_walker4.pkl, corso Lago Bianco` |
| 170 | 0 | corso Lago Bianco, livello 17, corso in dotazione | `encounter_walker4.pkl, corso Lago Bianco` |
| 456 | 0 | corso Spiaggia Tempestosa, livello 26, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Tempestosa` |
| 422 | 0 | corso Spiaggia Tempestosa, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Tempestosa` |
| 129 | 0 | corso Spiaggia Tempestosa, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Tempestosa` |
| 86 | 0 | corso Spiaggia Tempestosa, livello 27, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Tempestosa` |
| 54 | 0 | corso Spiaggia Tempestosa, livello 22, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Tempestosa` |
| 90 | 0 | corso Spiaggia Tempestosa, livello 20, corso in dotazione | `encounter_walker4.pkl, corso Spiaggia Tempestosa` |
| 417 | 0 | corso Villaggio Turistico, livello 33, corso in dotazione | `encounter_walker4.pkl, corso Villaggio Turistico` |
| 25 | 0 | corso Villaggio Turistico, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Villaggio Turistico` |
| 39 | 0 | corso Villaggio Turistico, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Villaggio Turistico` |
| 35 | 0 | corso Villaggio Turistico, livello 31, corso in dotazione | `encounter_walker4.pkl, corso Villaggio Turistico` |
| 183 | 0 | corso Villaggio Turistico, livello 25, corso in dotazione | `encounter_walker4.pkl, corso Villaggio Turistico` |
| 187 | 0 | corso Villaggio Turistico, livello 25, corso in dotazione | `encounter_walker4.pkl, corso Villaggio Turistico` |
| 442 | 0 | corso Grotta Silente, livello 31, corso in dotazione | `encounter_walker4.pkl, corso Grotta Silente` |
| 446 | 0 | corso Grotta Silente, livello 33, corso in dotazione | `encounter_walker4.pkl, corso Grotta Silente` |
| 433 | 0 | corso Grotta Silente, livello 26, corso in dotazione | `encounter_walker4.pkl, corso Grotta Silente` |
| 349 | 0 | corso Grotta Silente, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Grotta Silente` |
| 164 | 0 | corso Grotta Silente, livello 30, corso in dotazione | `encounter_walker4.pkl, corso Grotta Silente` |
| 42 | 0 | corso Grotta Silente, livello 33, corso in dotazione | `encounter_walker4.pkl, corso Grotta Silente` |
| 120 | 0 | corso Oltre il Mare, livello 18, corso in dotazione | `encounter_walker4.pkl, corso Oltre il Mare` |
| 224 | 0 | corso Oltre il Mare, livello 19, corso in dotazione | `encounter_walker4.pkl, corso Oltre il Mare` |
| 116 | 0 | corso Oltre il Mare, livello 15, corso in dotazione | `encounter_walker4.pkl, corso Oltre il Mare` |
| 222 | 0 | corso Oltre il Mare, livello 16, corso in dotazione | `encounter_walker4.pkl, corso Oltre il Mare` |
| 223 | 0 | corso Oltre il Mare, livello 14, corso in dotazione | `encounter_walker4.pkl, corso Oltre il Mare` |
| 170 | 0 | corso Oltre il Mare, livello 12, corso in dotazione | `encounter_walker4.pkl, corso Oltre il Mare` |
| 35 | 0 | corso Confine del Cielo, livello 8, corso in dotazione | `encounter_walker4.pkl, corso Confine del Cielo` |
| 39 | 0 | corso Confine del Cielo, livello 10, corso in dotazione | `encounter_walker4.pkl, corso Confine del Cielo` |
| 41 | 0 | corso Confine del Cielo, livello 9, corso in dotazione | `encounter_walker4.pkl, corso Confine del Cielo` |
| 163 | 0 | corso Confine del Cielo, livello 6, corso in dotazione | `encounter_walker4.pkl, corso Confine del Cielo` |
| 74 | 0 | corso Confine del Cielo, livello 5, corso in dotazione | `encounter_walker4.pkl, corso Confine del Cielo` |
| 95 | 0 | corso Confine del Cielo, livello 5, corso in dotazione | `encounter_walker4.pkl, corso Confine del Cielo` |
| 25 | 0 | corso Foresta Gialla, livello 15, corso distribuito | `encounter_walker4.pkl, corso Foresta Gialla` |
| 25 | 0 | corso Foresta Gialla, livello 14, corso distribuito | `encounter_walker4.pkl, corso Foresta Gialla` |
| 25 | 0 | corso Foresta Gialla, livello 13, corso distribuito | `encounter_walker4.pkl, corso Foresta Gialla` |
| 25 | 0 | corso Foresta Gialla, livello 12, corso distribuito | `encounter_walker4.pkl, corso Foresta Gialla` |
| 25 | 0 | corso Foresta Gialla, livello 10, corso distribuito | `encounter_walker4.pkl, corso Foresta Gialla` |
| 25 | 0 | corso Foresta Gialla, livello 10, corso distribuito | `encounter_walker4.pkl, corso Foresta Gialla` |
| 441 | 0 | corso Raduno, livello 15, corso distribuito | `encounter_walker4.pkl, corso Raduno` |
| 302 | 0 | corso Raduno, livello 15, corso distribuito | `encounter_walker4.pkl, corso Raduno` |
| 25 | 0 | corso Raduno, livello 10, corso distribuito | `encounter_walker4.pkl, corso Raduno` |
| 453 | 0 | corso Raduno, livello 10, corso distribuito | `encounter_walker4.pkl, corso Raduno` |
| 427 | 0 | corso Raduno, livello 5, corso distribuito | `encounter_walker4.pkl, corso Raduno` |
| 417 | 0 | corso Raduno, livello 5, corso distribuito | `encounter_walker4.pkl, corso Raduno` |
| 255 | 0 | corso Gita, livello 10, corso distribuito | `encounter_walker4.pkl, corso Gita` |
| 133 | 0 | corso Gita, livello 10, corso distribuito | `encounter_walker4.pkl, corso Gita` |
| 279 | 0 | corso Gita, livello 15, corso distribuito | `encounter_walker4.pkl, corso Gita` |
| 61 | 0 | corso Gita, livello 15, corso distribuito | `encounter_walker4.pkl, corso Gita` |
| 52 | 0 | corso Gita, livello 10, corso distribuito | `encounter_walker4.pkl, corso Gita` |
| 25 | 0 | corso Gita, livello 8, corso distribuito | `encounter_walker4.pkl, corso Gita` |
| 446 | 0 | corso Via del Vincitore, livello 5, corso distribuito | `encounter_walker4.pkl, corso Via del Vincitore` |
| 374 | 0 | corso Via del Vincitore, livello 5, corso distribuito | `encounter_walker4.pkl, corso Via del Vincitore` |
| 116 | 0 | corso Via del Vincitore, livello 5, corso distribuito | `encounter_walker4.pkl, corso Via del Vincitore` |
| 355 | 0 | corso Via del Vincitore, livello 5, corso distribuito | `encounter_walker4.pkl, corso Via del Vincitore` |
| 129 | 0 | corso Via del Vincitore, livello 5, corso distribuito | `encounter_walker4.pkl, corso Via del Vincitore` |
| 436 | 0 | corso Via del Vincitore, livello 5, corso distribuito | `encounter_walker4.pkl, corso Via del Vincitore` |
| 239 | 0 | corso Prato Amicizia, livello 5, corso distribuito | `encounter_walker4.pkl, corso Prato Amicizia` |
| 240 | 0 | corso Prato Amicizia, livello 5, corso distribuito | `encounter_walker4.pkl, corso Prato Amicizia` |
| 238 | 0 | corso Prato Amicizia, livello 5, corso distribuito | `encounter_walker4.pkl, corso Prato Amicizia` |
| 440 | 0 | corso Prato Amicizia, livello 5, corso distribuito | `encounter_walker4.pkl, corso Prato Amicizia` |
| 174 | 0 | corso Prato Amicizia, livello 5, corso distribuito | `encounter_walker4.pkl, corso Prato Amicizia` |
| 173 | 0 | corso Prato Amicizia, livello 5, corso distribuito | `encounter_walker4.pkl, corso Prato Amicizia` |

## Colosseum, premio del Monte Lotta

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 250 | 0 | Ho-oh @ Mt. Battle | `Gen3/Encounters3RSE.cs ColoGiftsS` |

## Colosseum, iniziali

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 196 | 0 | Espeon | `Gen3/Encounters3Colo.cs Starters` |
| 197 | 0 | Umbreon (Bite) | `Gen3/Encounters3Colo.cs Starters` |

## Colosseum, doni

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 311 | 0 | Plusle @ In-game Trade | `Gen3/Encounters3Colo.cs Gifts` |

## Colosseum, ombra

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 296 | 0 | Makuhita: Miror B.Peon Trudly @ Phenac City | `Gen3/Encounters3Colo.cs Shadow` |
| 153 | 0 | Bayleef: Cipher Peon Verde @ Phenac City | `Gen3/Encounters3Colo.cs Shadow` |
| 153 | 0 | Bayleef: Cipher Peon Verde @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 153 | 0 | Bayleef: Cipher Peon Verde @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 153 | 0 | Bayleef: Cipher Peon Verde @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 156 | 0 | Quilava: Cipher Peon Rosso @ Phenac City | `Gen3/Encounters3Colo.cs Shadow` |
| 156 | 0 | Quilava: Cipher Peon Rosso @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 156 | 0 | Quilava: Cipher Peon Rosso @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 156 | 0 | Quilava: Cipher Peon Rosso @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 159 | 0 | Croconaw: Cipher Peon Bluno @ Phenac City | `Gen3/Encounters3Colo.cs Shadow` |
| 159 | 0 | Croconaw: Cipher Peon Bluno @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 159 | 0 | Croconaw: Cipher Peon Bluno @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 159 | 0 | Croconaw: Cipher Peon Bluno @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 164 | 0 | Noctowl: Rider Nover @ Pyrite Town | `Gen3/Encounters3Colo.cs Shadow` |
| 180 | 0 | Flaaffy: St.Performer Diogo @ Pyrite Town | `Gen3/Encounters3Colo.cs Shadow` |
| 188 | 0 | Skiploom: Rider Leba @ Pyrite Town | `Gen3/Encounters3Colo.cs Shadow` |
| 195 | 0 | Quagsire: Bandana Guy Divel @ Pyrite Town | `Gen3/Encounters3Colo.cs Shadow` |
| 200 | 0 | Misdreavus: Rider Vant @ Pyrite Town | `Gen3/Encounters3Colo.cs Shadow` |
| 193 | 0 | Yanma: Cipher Peon Nore @ Pyrite Bldg | `Gen3/Encounters3Colo.cs Shadow` |
| 193 | 0 | Yanma: Cipher Peon Nore @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 162 | 0 | Furret: Rogue Cail @ Pyrite Town | `Gen3/Encounters3Colo.cs Shadow` |
| 218 | 0 | Slugma: Roller Boy Lon @ Pyrite Town | `Gen3/Encounters3Colo.cs Shadow` |
| 223 | 0 | Remoraid: Miror B.Peon Reath @ Pyrite Bldg | `Gen3/Encounters3Colo.cs Shadow` |
| 223 | 0 | Remoraid: Miror B.Peon Reath @ Pyrite Cave | `Gen3/Encounters3Colo.cs Shadow` |
| 226 | 0 | Mantine: Miror B.Peon Ferma @ Pyrite Bldg | `Gen3/Encounters3Colo.cs Shadow` |
| 226 | 0 | Mantine: Miror B.Peon Ferma @ Pyrite Cave | `Gen3/Encounters3Colo.cs Shadow` |
| 211 | 0 | Qwilfish: Hunter Doken @ Pyrite Bldg | `Gen3/Encounters3Colo.cs Shadow` |
| 307 | 0 | Meditite: Rider Twan @ Pyrite Cave | `Gen3/Encounters3Colo.cs Shadow` |
| 206 | 0 | Dunsparce: Rider Sosh @ Pyrite Cave | `Gen3/Encounters3Colo.cs Shadow` |
| 333 | 0 | Swablu: Hunter Zalo @ Pyrite Cave | `Gen3/Encounters3Colo.cs Shadow` |
| 185 | 0 | Sudowoodo: Cipher Admin Miror B. @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 185 | 0 | Sudowoodo: Cipher Admin Miror B. @ Deep Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 185 | 0 | Sudowoodo: Cipher Admin Miror B. @ Pyrite Cave | `Gen3/Encounters3Colo.cs Shadow` |
| 237 | 0 | Hitmontop: Cipher Peon Skrub @ Agate Village | `Gen3/Encounters3Colo.cs Shadow` |
| 237 | 0 | Hitmontop: Cipher Peon Skrub @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 237 | 0 | Hitmontop: Cipher Peon Skrub @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 244 | 0 | Entei: Cipher Admin Dakim @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 244 | 0 | Entei: Cipher Admin Dakim @ Deep Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 244 | 0 | Entei: Cipher Admin Dakim @ Mt. Battle | `Gen3/Encounters3Colo.cs Shadow` |
| 166 | 0 | Ledian: Cipher Peon Kloak @ The Under | `Gen3/Encounters3Colo.cs Shadow` |
| 166 | 0 | Ledian: Cipher Peon Kloak @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 245 | 0 | Suicune (Surf): Cipher Admin Venus @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 245 | 0 | Suicune (Hydro Pump): Cipher Admin Venus @ Deep Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 245 | 0 | Suicune (Surf): Cipher Admin Venus @ The Under | `Gen3/Encounters3Colo.cs Shadow` |
| 207 | 0 | Gligar: Hunter Frena @ The Under Subway | `Gen3/Encounters3Colo.cs Shadow` |
| 207 | 0 | Gligar: Hunter Frena @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 234 | 0 | Stantler: Chaser Liaks @ The Under Subway | `Gen3/Encounters3Colo.cs Shadow` |
| 234 | 0 | Stantler: Chaser Liaks @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 221 | 0 | Piloswine: Bodybuilder Lonia @ The Under Subway | `Gen3/Encounters3Colo.cs Shadow` |
| 221 | 0 | Piloswine: Bodybuilder Lonia @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 215 | 0 | Sneasel: Rider Nelis @ The Under Subway | `Gen3/Encounters3Colo.cs Shadow` |
| 215 | 0 | Sneasel: Rider Nelis @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 190 | 0 | Aipom: Cipher Peon Cole @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 198 | 0 | Murkrow: Cipher Peon Lare @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 198 | 0 | Murkrow: Cipher Peon Lare @ Shadow PKMN Lab (Trainer drops from ceiling: can lose during play-through, rematch later) | `Gen3/Encounters3Colo.cs Shadow` |
| 205 | 0 | Forretress: Cipher Peon Vana @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 210 | 0 | Granbull: Cipher Peon Tanie @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 329 | 0 | Vibrava: Cipher Peon Remil @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 168 | 0 | Ariados: Cipher Peon Lesar @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 243 | 0 | Raikou: Cipher Admin Ein @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 243 | 0 | Raikou: Cipher Admin Ein @ Deep Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 243 | 0 | Raikou: Cipher Admin Ein @ Shadow PKMN Lab | `Gen3/Encounters3Colo.cs Shadow` |
| 192 | 0 | Sunflora: Cipher Peon Baila @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 192 | 0 | Sunflora: Cipher Peon Baila @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 225 | 0 | Delibird: Cipher Peon Arton @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 225 | 0 | Delibird: Cipher Peon Arton @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 214 | 0 | Heracross: Cipher Peon Dioge @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 214 | 0 | Heracross: Cipher Peon Dioge @ Snagem Hideout (Trainer drops from ceiling: can lose during play-through, rematch later) | `Gen3/Encounters3Colo.cs Shadow` |
| 227 | 0 | Skarmory: Snagem Head Gonzap @ Realgam Tower | `Gen3/Encounters3Colo.cs Shadow` |
| 227 | 0 | Skarmory: Snagem Head Gonzap @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 241 | 0 | Miltank: Bodybuilder Jomas @ Tower Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 359 | 0 | Absol: Rider Delan @ Tower Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 229 | 0 | Houndoom: Cipher Peon Nella @ Tower Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 357 | 0 | Tropius: Cipher Peon Ston @ Tower Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 376 | 0 | Metagross: Cipher Nascour @ Tower Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 248 | 0 | Tyranitar: Cipher Head Evice @ Tower Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 235 | 0 | Smeargle: Team Snagem Biden @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 217 | 0 | Ursaring: Team Snagem Agrev @ Snagem Hideout | `Gen3/Encounters3Colo.cs Shadow` |
| 213 | 0 | Shuckle: Deep King Agnol @ Deep Colosseum | `Gen3/Encounters3Colo.cs Shadow` |
| 176 | 0 | Togetic: Cipher Peon Fein @ Outskirt Stand | `Gen3/Encounters3Colo.cs Shadow` |

## XD, doni

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 133 | 0 | Eevee (Bite) | `Gen3/Encounters3XD.cs Gifts` |
| 152 | 0 | Chikorita | `Gen3/Encounters3XD.cs Gifts` |
| 155 | 0 | Cyndaquil | `Gen3/Encounters3XD.cs Gifts` |
| 158 | 0 | Totodile | `Gen3/Encounters3XD.cs Gifts` |

## XD, scambi

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 239 | 0 | Elekid @ Snagem Hideout | `Gen3/Encounters3XD.cs Trades` |
| 307 | 0 | Meditite @ Pyrite Town | `Gen3/Encounters3XD.cs Trades` |
| 213 | 0 | Shuckle @ Pyrite Town | `Gen3/Encounters3XD.cs Trades` |
| 246 | 0 | Larvitar @ Pyrite Town | `Gen3/Encounters3XD.cs Trades` |

## XD, ombra

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 216 | 0 | Teddiursa: Cipher Peon Naps @ Pokémon HQ Lab -- treat as Gift as it can only be captured in a Poké Ball | `Gen3/Encounters3XD.cs Shadow` |
| 37 | 0 | Vulpix: Cipher Peon Mesin @ ONBS Building | `Gen3/Encounters3XD.cs Shadow` |
| 363 | 0 | Spheal: Cipher Peon Blusix @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 363 | 0 | Spheal: Cipher Peon Blusix  @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 343 | 0 | Baltoy: Cipher Peon Browsix @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 343 | 0 | Baltoy: Cipher Peon Browsix  @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 179 | 0 | Mareep: Cipher Peon Yellosix @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 179 | 0 | Mareep: Cipher Peon Yellosix @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 316 | 0 | Gulpin: Cipher Peon Purpsix @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 316 | 0 | Gulpin: Cipher Peon Purpsix @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 273 | 0 | Seedot: Cipher Peon Greesix @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 273 | 0 | Seedot: Cipher Peon Greesix @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 167 | 0 | Spinarak: Cipher Peon Nexir @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 322 | 0 | Numel: Cipher Peon Solox @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 318 | 0 | Carvanha: Cipher Peon Cabol @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 315 | 0 | Roselia: Cipher Peon Fasin @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 301 | 0 | Delcatty: Cipher Admin Lovrina @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 299 | 0 | Nosepass: Wanderer Miror B. @ Poké Spots | `Gen3/Encounters3XD.cs Shadow` |
| 228 | 0 | Houndour: Cipher Peon Resix  @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 228 | 0 | Houndour: Cipher Peon Resix @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 296 | 0 | Makuhita: Cipher Peon Torkin @ ONBS Building | `Gen3/Encounters3XD.cs Shadow` |
| 355 | 0 | Duskull: Cipher Peon Lobar @ ONBS Building | `Gen3/Encounters3XD.cs Shadow` |
| 280 | 0 | Ralts: Cipher Peon Feldas @ ONBS Building | `Gen3/Encounters3XD.cs Shadow` |
| 303 | 0 | Mawile: Cipher Cmdr Exol @ ONBS Building | `Gen3/Encounters3XD.cs Shadow` |
| 361 | 0 | Snorunt: Cipher Peon Exinn @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 204 | 0 | Pineco: Cipher Peon Gonrap @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 220 | 0 | Swinub: Cipher Peon Greck @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 177 | 0 | Natu: Cipher Peon Eloin @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 285 | 0 | Shroomish: Cipher R&D Klots @ Cipher Lab | `Gen3/Encounters3XD.cs Shadow` |
| 52 | 0 | Meowth: Cipher Peon Fostin @ Phenac City | `Gen3/Encounters3XD.cs Shadow` |
| 21 | 0 | Spearow: Cipher Peon Ezin @ Phenac Stadium | `Gen3/Encounters3XD.cs Shadow` |
| 88 | 0 | Grimer: Cipher Peon Faltly @ Phenac Stadium | `Gen3/Encounters3XD.cs Shadow` |
| 86 | 0 | Seel: Cipher Peon Egrog @ Phenac Stadium | `Gen3/Encounters3XD.cs Shadow` |
| 337 | 0 | Lunatone: Cipher Admin Snattle @ Phenac Stadium | `Gen3/Encounters3XD.cs Shadow` |
| 100 | 0 | Voltorb: Wanderer Miror B. @ Cave Poké Spot | `Gen3/Encounters3XD.cs Shadow` |
| 335 | 0 | Zangoose: Thug Zook @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 58 | 0 | Growlithe: Cipher Peon Humah @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 46 | 0 | Paras: Cipher Peon Humah @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 90 | 0 | Shellder: Cipher Peon Gorog @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 15 | 0 | Beedrill: Cipher Peon Lok @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 17 | 0 | Pidgeotto: Cipher Peon Lok @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 12 | 0 | Butterfree: Cipher Peon Targ @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 114 | 0 | Tangela: Cipher Peon Targ @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 20 | 0 | Raticate: Chaser Furgy @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 49 | 0 | Venomoth: Cipher Peon Angic @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 70 | 0 | Weepinbell: Cipher Peon Angic @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 24 | 0 | Arbok: Cipher Peon Smarton @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 57 | 0 | Primeape: Cipher Admin Gorigan @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 97 | 0 | Hypno: Cipher Admin Gorigan @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 55 | 0 | Golduck: Navigator Abson @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 302 | 0 | Sableye: Navigator Abson @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 82 | 0 | Magneton: Cipher Peon Snidle @ Cipher Key Lair | `Gen3/Encounters3XD.cs Shadow` |
| 85 | 0 | Dodrio: Chaser Furgy @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 83 | 0 | Farfetch'd: Cipher Admin Lovrina @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 334 | 0 | Altaria: Cipher Admin Lovrina @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 115 | 0 | Kangaskhan: Cipher Peon Litnar @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 354 | 0 | Banette: Cipher Peon Litnar @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 126 | 0 | Magmar: Cipher Peon Grupel @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 127 | 0 | Pinsir: Cipher Peon Grupel @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 219 | 0 | Magcargo: Cipher Peon Kolest @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 78 | 0 | Rapidash: Cipher Peon Kolest @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 107 | 0 | Hitmonchan: Cipher Peon Karbon @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 106 | 0 | Hitmonlee: Cipher Peon Petro @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 108 | 0 | Lickitung: Cipher Peon Geftal @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 123 | 0 | Scyther: Cipher Peon Leden @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 113 | 0 | Chansey: Cipher Peon Leden @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 113 | 0 | Chansey: Cipher Peon Leden @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 338 | 0 | Solrock: Cipher Admin Snattle @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 121 | 0 | Starmie: Cipher Admin Snattle @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 125 | 0 | Electabuzz: Cipher Admin Ardos @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 277 | 0 | Swellow: Cipher Admin Ardos @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 143 | 0 | Snorlax: Cipher Admin Ardos @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 62 | 0 | Poliwrath: Cipher Admin Gorigan @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 122 | 0 | Mr. Mime: Cipher Admin Gorigan @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 51 | 0 | Dugtrio: Cipher Peon Kolax @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 310 | 0 | Manectric: Cipher Admin Eldes @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 373 | 0 | Salamence: Cipher Admin Eldes @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 105 | 0 | Marowak: Cipher Admin Eldes @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 131 | 0 | Lapras: Cipher Admin Eldes @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 249 | 0 | Lugia: Grand Master Greevil @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 145 | 0 | Zapdos: Grand Master Greevil @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 146 | 0 | Moltres: Grand Master Greevil @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 144 | 0 | Articuno: Grand Master Greevil @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 128 | 0 | Tauros: Grand Master Greevil @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 112 | 0 | Rhydon: Grand Master Greevil @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 103 | 0 | Exeggutor: Grand Master Greevil @ Citadark Isle | `Gen3/Encounters3XD.cs Shadow` |
| 149 | 0 | Dragonite: Wanderer Miror B. @ Gateon Port | `Gen3/Encounters3XD.cs Shadow` |
| 175 | 0 | Togepi: Pokémon Trainer Hordel @ Outskirt Stand | `Gen3/Encounters3XD.cs Shadow` |
| 261 | 0 | Poochyena: Bodybuilder Kilen @ Gateon Port | `Gen3/Encounters3XD.cs Shadow` |
| 165 | 0 | Ledyba: Casual Guy Cyle @ Gateon Port | `Gen3/Encounters3XD.cs Shadow` |

## Leggende Arceus, doni fatidici

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 493 | 0 | Arceus | `Gen8/Encounters8a.cs incontri fatidici` |
| 489 | 0 | Phione | `Gen8/Encounters8a.cs incontri fatidici` |
| 490 | 0 | Manaphy | `Gen8/Encounters8a.cs incontri fatidici` |
| 491 | 0 | Darkrai | `Gen8/Encounters8a.cs incontri fatidici` |
| 492 | 0 | Shaymin | `Gen8/Encounters8a.cs incontri fatidici` |
| 491 | 0 | Darkrai (Lonely Spring) | `Gen8/Encounters8a.cs incontri fatidici` |

## Diamante Lucente e Perla Splendente, doni fatidici

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 151 | 0 | Mew | `Gen8/Encounters8b.cs incontri fatidici` |
| 385 | 0 | Jirachi | `Gen8/Encounters8b.cs incontri fatidici` |
| 491 | 0 | Darkrai | `Gen8/Encounters8b.cs incontri fatidici` |
| 492 | 0 | Shaymin | `Gen8/Encounters8b.cs incontri fatidici` |
| 493 | 0 | Arceus (Brilliant Diamond) | `Gen8/Encounters8b.cs incontri fatidici` |
| 493 | 0 | Arceus (Shining Pearl) | `Gen8/Encounters8b.cs incontri fatidici` |

## Spada e Scudo, doni fatidici

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 647 | 1 | Keldeo-1 at Ballimere Lake | `Gen8/Encounters8.cs incontri fatidici` |

## Spada e Scudo, incursioni delle grotte di cristallo

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 782 | 0 | ★And458 Jangmo-o | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 246 | 0 | ★And15 Larvitar | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 823 | 0 | ★And337 Gigantamax Corviknight | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 875 | 0 | ★And603 Eiscue | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 874 | 0 | ★And390 Stonjourner | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 879 | 0 | ★Sgr6879 Gigantamax Copperajah | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 851 | 0 | ★Sgr6859 Gigantamax Centiskorch | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 842 | 0 | ★Sgr6913 Gigantamax Appletun | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 841 | 0 | ★Sgr6913 Gigantamax Flapple | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 844 | 0 | ★Sgr7348 Gigantamax Sandaconda | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 884 | 0 | ★Sgr7121 Gigantamax Duraludon | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 25 | 0 | ★Sgr6746 Gigantamax Pikachu | `Gen8/Encounters8Nest.cs Crystal_SWSH` |
| 133 | 0 | ★Sgr7194 Gigantamax Eevee | `Gen8/Encounters8Nest.cs Crystal_SWSH` |

## Spada, incursioni da distribuzione

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 1 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 1 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 1 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 2 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 2 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 2 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 3 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 3 | 0 | livello 80 | `Gen8/encounter_sw_dist.pkl` |
| 3 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 3 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 3 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 3 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 4 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 4 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 4 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 4 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 4 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 5 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 5 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 5 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 6 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 6 | 0 | livello 80 | `Gen8/encounter_sw_dist.pkl` |
| 6 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 6 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 6 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 6 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 6 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 7 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 7 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 7 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 8 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 9 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 9 | 0 | livello 80 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 12 | 0 | livello 70 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 26 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 26 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 26 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 26 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 26 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 26 | 1 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 26 | 1 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 26 | 1 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 26 | 1 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 26 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 36 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 36 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 36 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 36 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 36 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 36 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 37 | 1 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 37 | 1 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 37 | 1 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 37 | 1 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 37 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 37 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 40 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 40 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 40 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 40 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 40 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 43 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 43 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 44 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 45 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 45 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 45 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 45 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 45 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 45 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 45 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 45 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 1 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 1 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 1 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 1 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 2 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 2 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 2 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 2 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 2 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 2 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 52 | 2 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 60 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 60 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 60 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 60 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 60 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 60 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 61 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 66 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 67 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 67 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 68 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 68 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 68 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 68 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 68 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 68 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 68 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 68 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 68 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 68 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 77 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 77 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 77 | 1 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 77 | 1 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 78 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 78 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 78 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 78 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 90 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 92 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 92 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 93 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 93 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 93 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 94 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 95 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 95 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 95 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 95 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 95 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 98 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 98 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 98 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 99 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 109 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 109 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 109 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 109 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 109 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 109 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 109 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 110 | 1 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 110 | 1 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 110 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 111 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 111 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 112 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 118 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 118 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 119 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 119 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 119 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 121 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 121 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 121 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 121 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 121 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 124 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 124 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 124 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 124 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 124 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 127 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 127 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 127 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 127 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 127 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 128 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 128 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 128 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 128 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 128 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 128 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 129 | 0 | livello 70 | `Gen8/encounter_sw_dist.pkl` |
| 131 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 131 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 131 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 131 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 131 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 132 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 132 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 132 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 132 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 132 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 133 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 134 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 134 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 134 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 135 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 135 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 135 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 136 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 136 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 136 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 138 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 138 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 138 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 138 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 138 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 138 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 140 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 140 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 140 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 140 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 140 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 142 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 142 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 142 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 142 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 142 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 70 | `Gen8/encounter_sw_dist.pkl` |
| 143 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 172 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 172 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 172 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 172 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 172 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 172 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 173 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 175 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 175 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 176 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 182 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 182 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 182 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 182 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 182 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 182 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 182 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 183 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 183 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 183 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 183 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 183 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 183 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 183 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 184 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 184 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 184 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 184 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 184 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 185 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 185 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 185 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 186 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 186 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 186 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 186 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 194 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 195 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 195 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 195 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 195 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 195 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 195 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 195 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 195 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 195 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 196 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 196 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 196 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 197 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 197 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 197 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 202 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 202 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 202 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 202 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 202 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 208 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 208 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 208 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 208 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 208 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 213 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 213 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 213 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 213 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 213 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 214 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 214 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 214 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 214 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 214 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 222 | 1 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 222 | 1 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 222 | 1 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 223 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 223 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 224 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 224 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 224 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 225 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 225 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 225 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 225 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 225 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 225 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 225 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 225 | 0 | livello 70 | `Gen8/encounter_sw_dist.pkl` |
| 226 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 226 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 226 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 236 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 241 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 241 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 241 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 241 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 241 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 246 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 247 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 248 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 248 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 248 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 280 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 281 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 282 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 282 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 282 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 290 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 290 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 291 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 291 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 291 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 291 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 291 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 291 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 291 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 291 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 302 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 302 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 302 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 302 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 302 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 318 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 319 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 319 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 319 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 319 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 320 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 320 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 321 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 321 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 321 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 321 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 330 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 330 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 330 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 330 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 330 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 333 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 333 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 334 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 334 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 334 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 337 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 337 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 337 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 337 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 337 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 337 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 338 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 338 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 338 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 338 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 338 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 338 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 349 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 349 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 350 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 350 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 350 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 355 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 355 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 360 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 363 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 363 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 363 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 363 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 363 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 406 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 420 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 420 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 420 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 420 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 420 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 420 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 421 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 421 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 421 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 421 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 422 | 1 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 423 | 1 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 423 | 1 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 423 | 1 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 423 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 425 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 425 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 426 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 426 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 426 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 426 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 426 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 426 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 426 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 426 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 427 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 428 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 428 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 428 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 428 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 438 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 438 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 438 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 439 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 446 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 446 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 446 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 447 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 447 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 447 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 448 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 448 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 448 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 449 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 449 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 450 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 450 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 450 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 453 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 453 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 453 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 453 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 453 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 453 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 453 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 454 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 454 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 454 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 458 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 458 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 458 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 461 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 461 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 461 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 461 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 461 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 464 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 464 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 468 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 468 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 468 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 470 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 470 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 470 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 471 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 471 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 471 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 477 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 477 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 477 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 1 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 1 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 1 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 1 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 4 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 4 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 4 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 4 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 4 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 5 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 5 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 5 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 5 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 479 | 5 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 518 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 518 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 518 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 518 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 518 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 529 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 529 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 530 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 530 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 530 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 535 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 536 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 537 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 537 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 537 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 546 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 546 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 547 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 547 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 547 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 547 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 547 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 547 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 547 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 549 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 554 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 554 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 555 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 555 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 555 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 562 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 563 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 563 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 563 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 563 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 564 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 564 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 565 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 565 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 565 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 566 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 566 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 567 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 567 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 567 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 568 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 568 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 568 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 568 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 569 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 569 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 569 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 569 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 569 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 569 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 570 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 571 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 571 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 571 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 571 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 571 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 572 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 572 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 573 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 573 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 573 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 573 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 573 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 573 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 573 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 573 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 573 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 574 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 574 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 575 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 576 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 576 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 577 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 577 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 578 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 579 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 579 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 582 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 582 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 583 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 584 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 584 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 588 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 589 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 590 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 590 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 591 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 591 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 591 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 592 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 592 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 593 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 593 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 593 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 597 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 597 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 598 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 598 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 598 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 607 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 607 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 607 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 607 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 608 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 609 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 609 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 609 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 609 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 609 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 609 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 610 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 610 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 611 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 612 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 612 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 615 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 615 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 615 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 615 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 615 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 616 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 617 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 623 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 623 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 623 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 623 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 623 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 626 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 626 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 626 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 626 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 626 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 627 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 627 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 628 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 628 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 628 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 630 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 633 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 633 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 633 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 634 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 635 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 659 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 660 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 660 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 660 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 660 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 686 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 686 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 687 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 687 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 687 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 695 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 695 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 695 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 695 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 695 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 696 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 696 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 697 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 697 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 697 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 697 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 698 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 698 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 699 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 699 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 699 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 700 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 700 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 700 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 704 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 704 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 705 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 706 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 706 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 709 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 709 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 709 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 709 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 709 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 710 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 710 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 711 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 711 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 711 | 1 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 711 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 711 | 2 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 711 | 2 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 711 | 3 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 711 | 3 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 712 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 712 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 713 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 713 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 713 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 722 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 722 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 722 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 722 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 722 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 725 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 725 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 725 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 725 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 725 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 728 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 728 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 728 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 728 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 728 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 753 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 753 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 754 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 754 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 754 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 755 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 756 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 756 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 756 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 756 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 759 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 759 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 760 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 760 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 760 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 764 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 764 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 764 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 764 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 764 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 765 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 767 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 767 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 767 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 767 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 767 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 771 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 771 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 771 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 771 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 771 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 771 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 771 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 771 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 771 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 771 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 776 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 776 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 776 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 776 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 776 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 778 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 778 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 778 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 778 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 778 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 819 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 819 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 819 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 819 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 819 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 819 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 820 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 820 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 820 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 820 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 820 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 821 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 822 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 823 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 823 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 823 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 823 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 823 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 823 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 823 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 823 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 824 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 825 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 825 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 826 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 826 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 826 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 826 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 826 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 826 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 826 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 826 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 827 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 828 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 828 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 828 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 828 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 829 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 830 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 830 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 830 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 830 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 831 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 831 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 831 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 831 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 831 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 831 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 831 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 831 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 832 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 832 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 832 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 832 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 832 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 832 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 832 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 833 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 833 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 833 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 833 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 70 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 834 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 835 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 836 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 836 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 836 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 836 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 837 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 837 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 837 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 838 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 838 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 838 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 839 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 839 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 839 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 839 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 839 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 839 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 839 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 839 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 839 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 840 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 840 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 840 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 841 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 841 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 841 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 841 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 841 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 841 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 841 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 841 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 841 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 841 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 842 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 842 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 842 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 842 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 842 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 842 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 843 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 843 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 843 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 843 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 843 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 843 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 844 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 844 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 844 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 844 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 844 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 844 | 0 | livello 70 | `Gen8/encounter_sw_dist.pkl` |
| 844 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 844 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 844 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 844 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 845 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 848 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 848 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 1 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 1 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 1 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 849 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 850 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 850 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 851 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 851 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 851 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 851 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 851 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 851 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 851 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 851 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 851 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 851 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 852 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 852 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 853 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 853 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 853 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 853 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 855 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 855 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 855 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 855 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 855 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 856 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 856 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 857 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 858 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 858 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 858 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 859 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 859 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 859 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 859 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 859 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 859 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 859 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 859 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 860 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 860 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 860 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 860 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 861 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 861 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 861 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 861 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 861 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 861 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 861 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 861 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 861 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 861 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 863 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 863 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 863 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 863 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 868 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 869 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 869 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 869 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 869 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 869 | 1 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 869 | 2 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 869 | 3 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 869 | 4 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 869 | 5 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 869 | 6 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 870 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 870 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 870 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 870 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 870 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 871 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 871 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 871 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 871 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 871 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 871 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 871 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 871 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 871 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 872 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 872 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 872 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 872 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 872 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 872 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 873 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 873 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 873 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 873 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 873 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 875 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 875 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 875 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 875 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 875 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 875 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 876 | 1 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 876 | 1 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 876 | 1 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 876 | 1 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 876 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 876 | 1 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 877 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 877 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 877 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 877 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 877 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 878 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 878 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 878 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 878 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 878 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 878 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 879 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 879 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 879 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 879 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 879 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 879 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 879 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 879 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 879 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 879 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 884 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 884 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 884 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 884 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 884 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 884 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |
| 884 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 884 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 884 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 884 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 885 | 0 | livello 17 | `Gen8/encounter_sw_dist.pkl` |
| 886 | 0 | livello 30 | `Gen8/encounter_sw_dist.pkl` |
| 887 | 0 | livello 40 | `Gen8/encounter_sw_dist.pkl` |
| 887 | 0 | livello 50 | `Gen8/encounter_sw_dist.pkl` |
| 887 | 0 | livello 60 | `Gen8/encounter_sw_dist.pkl` |

## Scudo, incursioni da distribuzione

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 1 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 1 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 1 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 2 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 2 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 2 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 3 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 3 | 0 | livello 80 | `Gen8/encounter_sh_dist.pkl` |
| 3 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 3 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 3 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 3 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 4 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 4 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 4 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 4 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 4 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 5 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 5 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 5 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 6 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 6 | 0 | livello 80 | `Gen8/encounter_sh_dist.pkl` |
| 6 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 6 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 6 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 6 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 6 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 6 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 6 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 7 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 7 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 7 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 8 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 9 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 9 | 0 | livello 80 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 12 | 0 | livello 70 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 25 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 26 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 26 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 26 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 26 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 26 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 26 | 1 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 26 | 1 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 26 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 26 | 1 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 26 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 36 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 36 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 36 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 36 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 36 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 36 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 37 | 1 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 37 | 1 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 37 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 37 | 1 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 37 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 37 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 40 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 40 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 40 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 40 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 40 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 43 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 43 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 44 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 45 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 45 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 45 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 45 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 45 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 45 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 45 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 45 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 1 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 1 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 1 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 2 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 2 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 2 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 2 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 2 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 2 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 52 | 2 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 60 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 60 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 60 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 60 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 60 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 60 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 61 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 66 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 67 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 67 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 68 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 68 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 68 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 68 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 68 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 68 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 68 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 68 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 68 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 68 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 77 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 77 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 78 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 78 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 78 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 83 | 1 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 83 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 90 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 92 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 92 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 93 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 93 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 93 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 94 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 95 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 95 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 95 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 95 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 95 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 98 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 98 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 99 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 99 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 99 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 109 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 109 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 109 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 109 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 109 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 109 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 109 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 110 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 110 | 1 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 110 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 111 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 111 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 112 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 118 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 118 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 119 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 119 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 119 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 121 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 121 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 121 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 121 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 121 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 124 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 124 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 124 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 124 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 124 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 127 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 127 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 127 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 127 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 127 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 128 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 128 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 128 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 128 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 128 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 128 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 129 | 0 | livello 70 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 131 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 132 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 132 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 132 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 132 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 132 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 133 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 134 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 134 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 134 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 135 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 135 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 135 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 136 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 136 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 136 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 138 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 138 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 138 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 138 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 138 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 138 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 140 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 140 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 140 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 140 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 140 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 142 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 142 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 142 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 142 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 142 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 70 | `Gen8/encounter_sh_dist.pkl` |
| 143 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 172 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 172 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 172 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 172 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 172 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 172 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 173 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 175 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 175 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 176 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 182 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 182 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 182 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 182 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 182 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 182 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 182 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 183 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 183 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 183 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 183 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 183 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 183 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 183 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 184 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 184 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 184 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 184 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 184 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 185 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 185 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 185 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 186 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 186 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 186 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 186 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 194 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 195 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 195 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 195 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 195 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 195 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 195 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 195 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 195 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 195 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 196 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 196 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 196 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 197 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 197 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 197 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 202 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 202 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 202 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 202 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 202 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 208 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 208 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 208 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 208 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 208 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 213 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 213 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 213 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 213 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 213 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 214 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 214 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 214 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 214 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 214 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 223 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 223 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 224 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 224 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 224 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 225 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 225 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 225 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 225 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 225 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 225 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 225 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 225 | 0 | livello 70 | `Gen8/encounter_sh_dist.pkl` |
| 226 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 226 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 226 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 236 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 241 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 241 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 241 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 241 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 241 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 246 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 247 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 248 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 248 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 248 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 280 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 281 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 282 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 282 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 282 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 290 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 290 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 291 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 291 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 291 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 291 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 291 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 291 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 291 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 291 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 302 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 302 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 302 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 302 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 302 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 318 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 319 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 319 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 319 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 319 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 320 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 320 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 321 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 321 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 321 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 321 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 330 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 330 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 330 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 330 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 330 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 333 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 333 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 334 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 334 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 334 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 337 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 337 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 337 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 337 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 337 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 337 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 338 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 338 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 338 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 338 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 338 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 338 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 349 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 349 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 350 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 350 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 350 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 355 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 355 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 360 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 363 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 363 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 363 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 363 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 363 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 406 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 420 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 420 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 420 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 420 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 420 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 420 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 421 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 421 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 421 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 421 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 422 | 1 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 423 | 1 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 423 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 423 | 1 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 423 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 425 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 425 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 426 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 426 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 426 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 426 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 426 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 426 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 426 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 426 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 427 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 428 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 428 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 428 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 428 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 438 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 438 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 438 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 439 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 446 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 446 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 446 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 447 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 447 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 447 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 448 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 448 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 448 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 449 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 449 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 450 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 450 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 450 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 453 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 453 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 453 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 453 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 453 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 453 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 453 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 454 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 454 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 454 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 458 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 458 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 458 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 461 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 461 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 461 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 461 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 461 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 464 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 464 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 468 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 468 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 468 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 470 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 470 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 470 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 471 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 471 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 471 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 477 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 477 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 477 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 2 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 2 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 2 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 2 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 2 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 2 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 4 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 4 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 4 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 4 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 4 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 5 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 5 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 5 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 5 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 479 | 5 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 518 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 518 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 518 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 518 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 518 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 529 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 529 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 530 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 530 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 530 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 535 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 536 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 537 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 537 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 537 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 546 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 546 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 547 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 547 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 547 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 547 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 547 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 547 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 547 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 549 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 554 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 554 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 554 | 1 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 554 | 1 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 554 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 555 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 555 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 555 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 562 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 563 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 563 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 563 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 563 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 564 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 564 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 565 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 565 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 565 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 566 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 566 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 567 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 567 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 567 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 568 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 568 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 568 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 568 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 569 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 569 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 569 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 569 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 569 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 569 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 569 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 569 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 570 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 571 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 571 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 571 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 571 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 571 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 572 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 572 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 573 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 573 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 573 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 573 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 573 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 573 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 573 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 573 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 573 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 574 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 574 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 575 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 576 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 576 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 577 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 577 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 578 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 579 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 579 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 582 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 582 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 583 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 584 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 584 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 588 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 589 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 590 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 590 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 591 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 591 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 591 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 592 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 592 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 593 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 593 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 593 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 597 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 597 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 598 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 598 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 598 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 607 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 607 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 607 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 607 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 608 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 609 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 609 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 609 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 609 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 609 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 609 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 610 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 610 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 611 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 612 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 612 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 615 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 615 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 615 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 615 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 615 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 616 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 617 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 623 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 623 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 623 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 623 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 623 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 626 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 626 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 626 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 626 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 626 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 627 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 627 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 628 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 628 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 628 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 628 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 633 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 633 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 633 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 634 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 635 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 659 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 660 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 660 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 660 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 660 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 686 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 686 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 687 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 687 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 687 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 695 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 695 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 695 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 695 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 695 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 696 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 696 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 697 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 697 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 697 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 697 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 698 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 698 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 699 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 699 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 699 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 700 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 700 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 700 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 704 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 704 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 705 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 706 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 706 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 709 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 709 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 709 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 709 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 709 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 710 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 710 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 711 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 711 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 711 | 1 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 711 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 711 | 2 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 711 | 2 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 711 | 3 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 711 | 3 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 712 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 712 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 713 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 713 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 713 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 722 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 722 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 722 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 722 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 722 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 725 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 725 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 725 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 725 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 725 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 728 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 728 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 728 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 728 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 728 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 753 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 753 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 754 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 754 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 754 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 755 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 756 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 756 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 756 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 756 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 759 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 759 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 760 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 760 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 760 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 764 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 764 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 764 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 764 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 764 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 766 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 767 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 767 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 767 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 767 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 767 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 771 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 771 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 771 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 771 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 771 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 771 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 771 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 771 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 771 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 771 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 776 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 776 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 776 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 776 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 776 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 778 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 778 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 778 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 778 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 778 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 819 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 819 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 819 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 819 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 819 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 819 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 820 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 820 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 820 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 820 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 820 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 821 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 821 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 821 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 821 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 822 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 822 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 822 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 822 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 70 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 823 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 824 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 825 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 825 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 825 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 826 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 827 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 828 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 828 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 828 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 828 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 829 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 830 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 830 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 830 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 830 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 831 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 831 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 831 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 831 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 831 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 831 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 831 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 831 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 832 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 832 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 832 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 832 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 832 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 832 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 832 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 833 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 833 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 834 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 834 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 834 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 834 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 834 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 834 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 834 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 835 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 836 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 836 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 836 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 836 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 837 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 838 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 839 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 839 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 839 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 839 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 840 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 840 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 840 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 841 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 841 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 841 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 841 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 841 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 841 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 842 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 842 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 842 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 842 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 842 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 842 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 842 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 842 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 842 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 843 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 843 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 844 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 844 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 844 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 844 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 845 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 848 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 848 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 1 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 1 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 1 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 849 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 850 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 850 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 850 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 850 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 850 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 850 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 70 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 851 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 852 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 852 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 853 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 853 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 853 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 853 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 855 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 855 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 855 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 855 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 855 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 856 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 856 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 856 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 856 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 857 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 857 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 858 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 858 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 858 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 858 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 858 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 858 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 859 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 859 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 859 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 859 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 859 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 859 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 860 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 860 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 860 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 861 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 861 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 861 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 861 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 861 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 861 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 863 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 863 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 863 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 863 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 865 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 868 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 869 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 869 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 869 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 869 | 2 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 869 | 3 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 869 | 4 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 869 | 7 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 869 | 8 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 870 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 870 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 870 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 870 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 870 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 871 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 871 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 871 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 871 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 871 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 871 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 871 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 871 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 871 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 872 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 872 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 872 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 872 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 872 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 872 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 873 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 873 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 873 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 873 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 873 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 875 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 875 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 875 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 875 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 875 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 875 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 876 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 876 | 1 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 876 | 1 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 876 | 1 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 876 | 1 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 876 | 1 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 877 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 877 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 877 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 877 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 877 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 878 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 878 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 878 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 878 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 878 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 878 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 879 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 879 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 879 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 879 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 879 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 879 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 879 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 879 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 879 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 879 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 884 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 884 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 884 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 884 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 884 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 884 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |
| 884 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 884 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 884 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 884 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 885 | 0 | livello 17 | `Gen8/encounter_sh_dist.pkl` |
| 886 | 0 | livello 30 | `Gen8/encounter_sh_dist.pkl` |
| 887 | 0 | livello 40 | `Gen8/encounter_sh_dist.pkl` |
| 887 | 0 | livello 50 | `Gen8/encounter_sh_dist.pkl` |
| 887 | 0 | livello 60 | `Gen8/encounter_sh_dist.pkl` |

## Spada e Scudo, avventure Dynamax nei sotterranei

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 2 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 5 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 8 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 12 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 26 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 26 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 28 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 28 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 31 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 34 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 35 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 36 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 39 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 40 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 44 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 45 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 51 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 51 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 53 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 53 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 55 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 62 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 64 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 67 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 73 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 80 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 82 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 93 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 99 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 103 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 105 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 105 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 106 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 107 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 108 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 110 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 110 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 112 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 113 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 114 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 115 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 117 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 119 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 121 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 122 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 122 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 123 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 124 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 125 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 126 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 128 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 132 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 134 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 135 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 136 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 137 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 144 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 145 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 146 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 148 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 150 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 164 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 171 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 176 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 178 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 182 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 184 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 185 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 186 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 195 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 199 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 206 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 211 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 215 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 221 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 224 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 226 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 227 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 237 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 241 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 243 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 244 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 245 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 249 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 250 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 253 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 254 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 256 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 257 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 259 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 260 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 264 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 264 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 279 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 291 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 295 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 305 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 310 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 315 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 319 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 320 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 324 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 330 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 334 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 340 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 342 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 344 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 346 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 348 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 356 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 359 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 362 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 364 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 369 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 375 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 380 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 381 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 382 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 383 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 384 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 405 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 416 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 421 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 423 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 426 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 428 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 435 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 437 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 446 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 452 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 460 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 478 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 479 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 480 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 481 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 482 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 483 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 484 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 485 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 487 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 488 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 508 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 510 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 518 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 521 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 525 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 528 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 531 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 533 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 536 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 537 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 545 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 547 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 549 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 550 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 550 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 553 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 556 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 558 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 561 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 563 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 569 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 573 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 583 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 587 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 589 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 591 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 593 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 596 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 600 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 601 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 606 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 608 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 611 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 614 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 615 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 617 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 618 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 618 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 620 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 621 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 623 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 625 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 626 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 631 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 632 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 641 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 642 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 643 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 644 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 645 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 646 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 660 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 663 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 675 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 680 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 687 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 689 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 695 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 697 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 699 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 701 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 702 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 707 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 709 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 711 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 716 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 717 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 718 | 3 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 737 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 738 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 743 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 745 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 745 | 1 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 750 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 752 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 754 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 756 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 758 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 760 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 763 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 764 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 765 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 766 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 770 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 771 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 777 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 778 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 785 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 786 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 787 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 788 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 791 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 792 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 793 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 794 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 795 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 796 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 797 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 798 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 799 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 800 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 805 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 806 | 0 | livello 70 | `Gen8/encounter_swsh_underground.pkl` |
| 820 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 826 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 828 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 830 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 832 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 834 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 836 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 838 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 839 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 844 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 845 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 847 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 849 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 851 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 853 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 855 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 858 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 861 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 862 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 863 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 869 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 870 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 871 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 873 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 876 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 877 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 879 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 884 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |
| 886 | 0 | livello 65 | `Gen8/encounter_swsh_underground.pkl` |

## Scarlatto e Violetto, incursioni da distribuzione

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 94 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 94 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 94 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 94 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 103 | 1 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 130 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 130 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 130 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 132 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 132 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 132 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 132 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 133 | 0 | livello 12 | `Gen9/encounter_dist_paldea.pkl` |
| 133 | 0 | livello 20 | `Gen9/encounter_dist_paldea.pkl` |
| 133 | 0 | livello 35 | `Gen9/encounter_dist_paldea.pkl` |
| 133 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 133 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 133 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 184 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 212 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 212 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 225 | 0 | livello 12 | `Gen9/encounter_dist_paldea.pkl` |
| 225 | 0 | livello 20 | `Gen9/encounter_dist_paldea.pkl` |
| 225 | 0 | livello 35 | `Gen9/encounter_dist_paldea.pkl` |
| 225 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 225 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 225 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 225 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 225 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 225 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 225 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 242 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 248 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 248 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 248 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 370 | 0 | livello 35 | `Gen9/encounter_dist_paldea.pkl` |
| 370 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 373 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 373 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 373 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 384 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 426 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 426 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 426 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 429 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 429 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 429 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 429 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 437 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 437 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 437 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 445 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 445 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 445 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 448 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 448 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 448 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 483 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 484 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 635 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 635 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 635 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 635 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 635 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 671 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 671 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 700 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 700 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 700 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 778 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 778 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 823 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 858 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 858 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 861 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 861 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 868 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 874 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 874 | 0 | livello 35 | `Gen9/encounter_dist_paldea.pkl` |
| 875 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 875 | 0 | livello 35 | `Gen9/encounter_dist_paldea.pkl` |
| 887 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 887 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 887 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 924 | 0 | livello 12 | `Gen9/encounter_dist_paldea.pkl` |
| 924 | 0 | livello 20 | `Gen9/encounter_dist_paldea.pkl` |
| 924 | 0 | livello 35 | `Gen9/encounter_dist_paldea.pkl` |
| 924 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 924 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 924 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 936 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 936 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 936 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 936 | 0 | livello 35 | `Gen9/encounter_dist_paldea.pkl` |
| 937 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 937 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 937 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 937 | 0 | livello 35 | `Gen9/encounter_dist_paldea.pkl` |
| 939 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 979 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 980 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 983 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 984 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 984 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 984 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 984 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 984 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 985 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 985 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 985 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 986 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 986 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 986 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 986 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 987 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 987 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 987 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 987 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 988 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 988 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 988 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 988 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 989 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 989 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 989 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 989 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 990 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 990 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 990 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 990 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 990 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 991 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 991 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 991 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 992 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 992 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 992 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 992 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 993 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 993 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 993 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 993 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 994 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 994 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 994 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 994 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 995 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 995 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 995 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 995 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 999 | 0 | livello 12 | `Gen9/encounter_dist_paldea.pkl` |
| 999 | 0 | livello 20 | `Gen9/encounter_dist_paldea.pkl` |
| 999 | 0 | livello 35 | `Gen9/encounter_dist_paldea.pkl` |
| 999 | 0 | livello 45 | `Gen9/encounter_dist_paldea.pkl` |
| 999 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 1009 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 1009 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 1010 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |
| 1010 | 0 | livello 75 | `Gen9/encounter_dist_paldea.pkl` |

## Scarlatto e Violetto, esemplari di potere

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 3 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 6 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 9 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 25 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 25 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 129 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 133 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 149 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 150 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 154 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 157 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 157 | 1 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 160 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 233 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 248 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 254 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 257 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 260 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 373 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 376 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 389 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 392 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 395 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 445 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 497 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 500 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 503 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 503 | 1 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 635 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 652 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 655 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 658 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 706 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 724 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 724 | 1 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 727 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 730 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 784 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 812 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 815 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 818 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 887 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 908 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 911 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 914 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 970 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 977 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 979 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 981 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 983 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 991 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 998 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 1005 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 1005 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 1006 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |
| 1006 | 0 | livello 100 | `Gen9/encounter_might_paldea.pkl` |

## Pokemon GO verso il deposito

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 1 | 0 | 41 finestre temporali | `encounter_go_home.pkl` |
| 2 | 0 | 47 finestre temporali | `encounter_go_home.pkl` |
| 3 | 0 | 66 finestre temporali | `encounter_go_home.pkl` |
| 4 | 0 | 45 finestre temporali | `encounter_go_home.pkl` |
| 5 | 0 | 48 finestre temporali | `encounter_go_home.pkl` |
| 6 | 0 | 75 finestre temporali | `encounter_go_home.pkl` |
| 7 | 0 | 40 finestre temporali | `encounter_go_home.pkl` |
| 8 | 0 | 42 finestre temporali | `encounter_go_home.pkl` |
| 9 | 0 | 60 finestre temporali | `encounter_go_home.pkl` |
| 10 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 11 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 12 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 13 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 14 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 15 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 16 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 17 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 18 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 19 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 19 | 1 | 12 finestre temporali | `encounter_go_home.pkl` |
| 20 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 20 | 1 | 14 finestre temporali | `encounter_go_home.pkl` |
| 21 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 22 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 23 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 24 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 25 | 0 | 105 finestre temporali | `encounter_go_home.pkl` |
| 26 | 0 | 111 finestre temporali | `encounter_go_home.pkl` |
| 26 | 1 | 45 finestre temporali | `encounter_go_home.pkl` |
| 27 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 27 | 1 | 30 finestre temporali | `encounter_go_home.pkl` |
| 28 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 28 | 1 | 30 finestre temporali | `encounter_go_home.pkl` |
| 29 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 30 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 31 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 32 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 33 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 34 | 0 | 37 finestre temporali | `encounter_go_home.pkl` |
| 35 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 36 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 37 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 37 | 1 | 36 finestre temporali | `encounter_go_home.pkl` |
| 38 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 38 | 1 | 38 finestre temporali | `encounter_go_home.pkl` |
| 39 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 40 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 41 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 42 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 43 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 44 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 45 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 46 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 47 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 48 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 49 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 50 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 50 | 1 | 15 finestre temporali | `encounter_go_home.pkl` |
| 51 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 51 | 1 | 19 finestre temporali | `encounter_go_home.pkl` |
| 52 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 52 | 1 | 24 finestre temporali | `encounter_go_home.pkl` |
| 52 | 2 | 20 finestre temporali | `encounter_go_home.pkl` |
| 53 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 53 | 1 | 24 finestre temporali | `encounter_go_home.pkl` |
| 54 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 55 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 56 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 57 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 58 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 58 | 1 | 19 finestre temporali | `encounter_go_home.pkl` |
| 59 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 59 | 1 | 19 finestre temporali | `encounter_go_home.pkl` |
| 60 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 61 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 62 | 0 | 29 finestre temporali | `encounter_go_home.pkl` |
| 63 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 64 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 65 | 0 | 46 finestre temporali | `encounter_go_home.pkl` |
| 66 | 0 | 31 finestre temporali | `encounter_go_home.pkl` |
| 67 | 0 | 34 finestre temporali | `encounter_go_home.pkl` |
| 68 | 0 | 66 finestre temporali | `encounter_go_home.pkl` |
| 69 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 70 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 71 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 72 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 73 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 74 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 74 | 1 | 18 finestre temporali | `encounter_go_home.pkl` |
| 75 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 75 | 1 | 31 finestre temporali | `encounter_go_home.pkl` |
| 76 | 0 | 54 finestre temporali | `encounter_go_home.pkl` |
| 76 | 1 | 31 finestre temporali | `encounter_go_home.pkl` |
| 77 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 77 | 1 | 28 finestre temporali | `encounter_go_home.pkl` |
| 78 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 78 | 1 | 30 finestre temporali | `encounter_go_home.pkl` |
| 79 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 79 | 1 | 16 finestre temporali | `encounter_go_home.pkl` |
| 80 | 0 | 35 finestre temporali | `encounter_go_home.pkl` |
| 80 | 2 | 16 finestre temporali | `encounter_go_home.pkl` |
| 81 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 82 | 0 | 47 finestre temporali | `encounter_go_home.pkl` |
| 83 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 83 | 1 | 22 finestre temporali | `encounter_go_home.pkl` |
| 84 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 85 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 86 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 87 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 88 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 88 | 1 | 22 finestre temporali | `encounter_go_home.pkl` |
| 89 | 0 | 29 finestre temporali | `encounter_go_home.pkl` |
| 89 | 1 | 25 finestre temporali | `encounter_go_home.pkl` |
| 90 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 91 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 92 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 93 | 0 | 30 finestre temporali | `encounter_go_home.pkl` |
| 94 | 0 | 71 finestre temporali | `encounter_go_home.pkl` |
| 95 | 0 | 36 finestre temporali | `encounter_go_home.pkl` |
| 96 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 97 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 98 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 99 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 100 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 100 | 1 | 32 finestre temporali | `encounter_go_home.pkl` |
| 101 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 101 | 1 | 32 finestre temporali | `encounter_go_home.pkl` |
| 102 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 103 | 0 | 26 finestre temporali | `encounter_go_home.pkl` |
| 103 | 1 | 52 finestre temporali | `encounter_go_home.pkl` |
| 104 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 105 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 105 | 1 | 59 finestre temporali | `encounter_go_home.pkl` |
| 106 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 107 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 108 | 0 | 26 finestre temporali | `encounter_go_home.pkl` |
| 109 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 110 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 110 | 1 | 50 finestre temporali | `encounter_go_home.pkl` |
| 111 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 112 | 0 | 40 finestre temporali | `encounter_go_home.pkl` |
| 113 | 0 | 37 finestre temporali | `encounter_go_home.pkl` |
| 114 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 115 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 116 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 117 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 118 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 119 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 120 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 121 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 122 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 122 | 1 | 16 finestre temporali | `encounter_go_home.pkl` |
| 123 | 0 | 53 finestre temporali | `encounter_go_home.pkl` |
| 124 | 0 | 26 finestre temporali | `encounter_go_home.pkl` |
| 125 | 0 | 34 finestre temporali | `encounter_go_home.pkl` |
| 126 | 0 | 36 finestre temporali | `encounter_go_home.pkl` |
| 127 | 0 | 40 finestre temporali | `encounter_go_home.pkl` |
| 128 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 128 | 1 | 4 finestre temporali | `encounter_go_home.pkl` |
| 128 | 2 | 5 finestre temporali | `encounter_go_home.pkl` |
| 128 | 3 | 5 finestre temporali | `encounter_go_home.pkl` |
| 129 | 0 | 29 finestre temporali | `encounter_go_home.pkl` |
| 130 | 0 | 57 finestre temporali | `encounter_go_home.pkl` |
| 131 | 0 | 56 finestre temporali | `encounter_go_home.pkl` |
| 132 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 133 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 134 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 135 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 136 | 0 | 30 finestre temporali | `encounter_go_home.pkl` |
| 137 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 138 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 139 | 0 | 30 finestre temporali | `encounter_go_home.pkl` |
| 140 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 141 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 142 | 0 | 47 finestre temporali | `encounter_go_home.pkl` |
| 143 | 0 | 46 finestre temporali | `encounter_go_home.pkl` |
| 144 | 0 | 56 finestre temporali | `encounter_go_home.pkl` |
| 144 | 1 | 2 finestre temporali | `encounter_go_home.pkl` |
| 145 | 0 | 43 finestre temporali | `encounter_go_home.pkl` |
| 145 | 1 | 2 finestre temporali | `encounter_go_home.pkl` |
| 146 | 0 | 38 finestre temporali | `encounter_go_home.pkl` |
| 146 | 1 | 2 finestre temporali | `encounter_go_home.pkl` |
| 147 | 0 | 39 finestre temporali | `encounter_go_home.pkl` |
| 148 | 0 | 39 finestre temporali | `encounter_go_home.pkl` |
| 149 | 0 | 70 finestre temporali | `encounter_go_home.pkl` |
| 150 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 151 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 152 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 153 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 154 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 155 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 156 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 157 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 157 | 1 | 10 finestre temporali | `encounter_go_home.pkl` |
| 158 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 159 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 160 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 161 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 162 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 163 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 164 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 165 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 166 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 167 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 168 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 169 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 170 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 171 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 172 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 173 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 174 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 175 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 176 | 0 | 46 finestre temporali | `encounter_go_home.pkl` |
| 177 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 178 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 179 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 180 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 181 | 0 | 41 finestre temporali | `encounter_go_home.pkl` |
| 182 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 183 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 184 | 0 | 40 finestre temporali | `encounter_go_home.pkl` |
| 185 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 186 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 187 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 188 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 189 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 190 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 191 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 192 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 193 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 194 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 194 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 195 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 196 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 197 | 0 | 36 finestre temporali | `encounter_go_home.pkl` |
| 198 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 199 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 199 | 1 | 16 finestre temporali | `encounter_go_home.pkl` |
| 200 | 0 | 36 finestre temporali | `encounter_go_home.pkl` |
| 201 | 0 | 31 finestre temporali | `encounter_go_home.pkl` |
| 201 | 1 | 19 finestre temporali | `encounter_go_home.pkl` |
| 201 | 2 | 12 finestre temporali | `encounter_go_home.pkl` |
| 201 | 3 | 24 finestre temporali | `encounter_go_home.pkl` |
| 201 | 4 | 25 finestre temporali | `encounter_go_home.pkl` |
| 201 | 5 | 10 finestre temporali | `encounter_go_home.pkl` |
| 201 | 6 | 20 finestre temporali | `encounter_go_home.pkl` |
| 201 | 7 | 23 finestre temporali | `encounter_go_home.pkl` |
| 201 | 8 | 29 finestre temporali | `encounter_go_home.pkl` |
| 201 | 9 | 9 finestre temporali | `encounter_go_home.pkl` |
| 201 | 10 | 5 finestre temporali | `encounter_go_home.pkl` |
| 201 | 11 | 25 finestre temporali | `encounter_go_home.pkl` |
| 201 | 12 | 14 finestre temporali | `encounter_go_home.pkl` |
| 201 | 13 | 38 finestre temporali | `encounter_go_home.pkl` |
| 201 | 14 | 33 finestre temporali | `encounter_go_home.pkl` |
| 201 | 15 | 10 finestre temporali | `encounter_go_home.pkl` |
| 201 | 16 | 7 finestre temporali | `encounter_go_home.pkl` |
| 201 | 17 | 35 finestre temporali | `encounter_go_home.pkl` |
| 201 | 18 | 31 finestre temporali | `encounter_go_home.pkl` |
| 201 | 19 | 29 finestre temporali | `encounter_go_home.pkl` |
| 201 | 20 | 36 finestre temporali | `encounter_go_home.pkl` |
| 201 | 21 | 11 finestre temporali | `encounter_go_home.pkl` |
| 201 | 22 | 9 finestre temporali | `encounter_go_home.pkl` |
| 201 | 23 | 10 finestre temporali | `encounter_go_home.pkl` |
| 201 | 24 | 14 finestre temporali | `encounter_go_home.pkl` |
| 201 | 25 | 8 finestre temporali | `encounter_go_home.pkl` |
| 201 | 26 | 18 finestre temporali | `encounter_go_home.pkl` |
| 201 | 27 | 12 finestre temporali | `encounter_go_home.pkl` |
| 202 | 0 | 34 finestre temporali | `encounter_go_home.pkl` |
| 203 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 204 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 205 | 0 | 31 finestre temporali | `encounter_go_home.pkl` |
| 206 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 207 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 208 | 0 | 44 finestre temporali | `encounter_go_home.pkl` |
| 209 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 210 | 0 | 39 finestre temporali | `encounter_go_home.pkl` |
| 211 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 211 | 1 | 23 finestre temporali | `encounter_go_home.pkl` |
| 212 | 0 | 64 finestre temporali | `encounter_go_home.pkl` |
| 213 | 0 | 36 finestre temporali | `encounter_go_home.pkl` |
| 214 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 215 | 0 | 74 finestre temporali | `encounter_go_home.pkl` |
| 215 | 1 | 27 finestre temporali | `encounter_go_home.pkl` |
| 216 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 217 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 218 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 219 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 220 | 0 | 31 finestre temporali | `encounter_go_home.pkl` |
| 221 | 0 | 69 finestre temporali | `encounter_go_home.pkl` |
| 222 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 222 | 1 | 9 finestre temporali | `encounter_go_home.pkl` |
| 223 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 224 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 225 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 226 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 227 | 0 | 39 finestre temporali | `encounter_go_home.pkl` |
| 228 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 229 | 0 | 51 finestre temporali | `encounter_go_home.pkl` |
| 230 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 231 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 232 | 0 | 29 finestre temporali | `encounter_go_home.pkl` |
| 233 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 234 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 235 | 0 | 37 finestre temporali | `encounter_go_home.pkl` |
| 236 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 237 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 238 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 239 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 240 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 241 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 242 | 0 | 37 finestre temporali | `encounter_go_home.pkl` |
| 243 | 0 | 34 finestre temporali | `encounter_go_home.pkl` |
| 244 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 245 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 246 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 247 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 248 | 0 | 69 finestre temporali | `encounter_go_home.pkl` |
| 249 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 250 | 0 | 26 finestre temporali | `encounter_go_home.pkl` |
| 251 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 252 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 253 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 254 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 255 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 256 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 257 | 0 | 36 finestre temporali | `encounter_go_home.pkl` |
| 258 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 259 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 260 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 261 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 262 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 263 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 263 | 1 | 26 finestre temporali | `encounter_go_home.pkl` |
| 264 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 264 | 1 | 27 finestre temporali | `encounter_go_home.pkl` |
| 265 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 266 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 267 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 268 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 269 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 270 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 271 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 272 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 273 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 274 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 275 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 276 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 277 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 278 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 279 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 280 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 281 | 0 | 52 finestre temporali | `encounter_go_home.pkl` |
| 282 | 0 | 72 finestre temporali | `encounter_go_home.pkl` |
| 283 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 284 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 285 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 286 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 287 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 288 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 289 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 290 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 291 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 292 | 0 | 26 finestre temporali | `encounter_go_home.pkl` |
| 293 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 294 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 295 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 296 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 297 | 0 | 31 finestre temporali | `encounter_go_home.pkl` |
| 298 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 299 | 0 | 29 finestre temporali | `encounter_go_home.pkl` |
| 300 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 301 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 302 | 0 | 49 finestre temporali | `encounter_go_home.pkl` |
| 303 | 0 | 72 finestre temporali | `encounter_go_home.pkl` |
| 304 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 305 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 306 | 0 | 53 finestre temporali | `encounter_go_home.pkl` |
| 307 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 308 | 0 | 44 finestre temporali | `encounter_go_home.pkl` |
| 309 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 310 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 311 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 312 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 313 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 314 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 315 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 316 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 317 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 318 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 319 | 0 | 44 finestre temporali | `encounter_go_home.pkl` |
| 320 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 321 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 322 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 323 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 324 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 325 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 326 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 328 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 329 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 330 | 0 | 31 finestre temporali | `encounter_go_home.pkl` |
| 331 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 332 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 333 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 334 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 335 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 336 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 337 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 338 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 339 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 340 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 341 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 342 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 343 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 344 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 345 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 346 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 347 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 348 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 349 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 350 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 351 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 352 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 353 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 354 | 0 | 37 finestre temporali | `encounter_go_home.pkl` |
| 355 | 0 | 36 finestre temporali | `encounter_go_home.pkl` |
| 356 | 0 | 42 finestre temporali | `encounter_go_home.pkl` |
| 357 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 358 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 359 | 0 | 56 finestre temporali | `encounter_go_home.pkl` |
| 360 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 361 | 0 | 32 finestre temporali | `encounter_go_home.pkl` |
| 362 | 0 | 46 finestre temporali | `encounter_go_home.pkl` |
| 363 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 364 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 365 | 0 | 39 finestre temporali | `encounter_go_home.pkl` |
| 366 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 367 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 368 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 369 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 370 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 371 | 0 | 26 finestre temporali | `encounter_go_home.pkl` |
| 372 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 373 | 0 | 51 finestre temporali | `encounter_go_home.pkl` |
| 374 | 0 | 34 finestre temporali | `encounter_go_home.pkl` |
| 375 | 0 | 44 finestre temporali | `encounter_go_home.pkl` |
| 376 | 0 | 65 finestre temporali | `encounter_go_home.pkl` |
| 377 | 0 | 37 finestre temporali | `encounter_go_home.pkl` |
| 378 | 0 | 40 finestre temporali | `encounter_go_home.pkl` |
| 379 | 0 | 39 finestre temporali | `encounter_go_home.pkl` |
| 380 | 0 | 39 finestre temporali | `encounter_go_home.pkl` |
| 381 | 0 | 40 finestre temporali | `encounter_go_home.pkl` |
| 382 | 0 | 30 finestre temporali | `encounter_go_home.pkl` |
| 383 | 0 | 31 finestre temporali | `encounter_go_home.pkl` |
| 384 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 385 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 386 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 386 | 1 | 15 finestre temporali | `encounter_go_home.pkl` |
| 386 | 2 | 17 finestre temporali | `encounter_go_home.pkl` |
| 386 | 3 | 13 finestre temporali | `encounter_go_home.pkl` |
| 387 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 388 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 389 | 0 | 26 finestre temporali | `encounter_go_home.pkl` |
| 390 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 391 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 392 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 393 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 394 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 395 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 396 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 397 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 398 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 399 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 400 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 401 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 402 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 403 | 0 | 63 finestre temporali | `encounter_go_home.pkl` |
| 404 | 0 | 65 finestre temporali | `encounter_go_home.pkl` |
| 405 | 0 | 70 finestre temporali | `encounter_go_home.pkl` |
| 406 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 407 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 408 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 409 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 410 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 411 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 412 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 412 | 1 | 6 finestre temporali | `encounter_go_home.pkl` |
| 412 | 2 | 7 finestre temporali | `encounter_go_home.pkl` |
| 413 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 413 | 1 | 6 finestre temporali | `encounter_go_home.pkl` |
| 413 | 2 | 7 finestre temporali | `encounter_go_home.pkl` |
| 414 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 415 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 416 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 417 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 418 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 419 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 420 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 421 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 422 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 422 | 1 | 5 finestre temporali | `encounter_go_home.pkl` |
| 423 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 423 | 1 | 5 finestre temporali | `encounter_go_home.pkl` |
| 424 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 425 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 426 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 427 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 428 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 429 | 0 | 36 finestre temporali | `encounter_go_home.pkl` |
| 430 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 431 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 432 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 433 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 434 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 435 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 436 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 437 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 438 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 439 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 440 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 441 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 442 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 443 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 444 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 445 | 0 | 30 finestre temporali | `encounter_go_home.pkl` |
| 446 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 447 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 448 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 449 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 450 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 451 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 452 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 453 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 454 | 0 | 35 finestre temporali | `encounter_go_home.pkl` |
| 455 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 456 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 457 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 458 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 459 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 460 | 0 | 35 finestre temporali | `encounter_go_home.pkl` |
| 461 | 0 | 76 finestre temporali | `encounter_go_home.pkl` |
| 462 | 0 | 47 finestre temporali | `encounter_go_home.pkl` |
| 463 | 0 | 26 finestre temporali | `encounter_go_home.pkl` |
| 464 | 0 | 40 finestre temporali | `encounter_go_home.pkl` |
| 465 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 466 | 0 | 37 finestre temporali | `encounter_go_home.pkl` |
| 467 | 0 | 36 finestre temporali | `encounter_go_home.pkl` |
| 468 | 0 | 47 finestre temporali | `encounter_go_home.pkl` |
| 469 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 470 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 471 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 472 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 473 | 0 | 71 finestre temporali | `encounter_go_home.pkl` |
| 474 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 475 | 0 | 60 finestre temporali | `encounter_go_home.pkl` |
| 476 | 0 | 29 finestre temporali | `encounter_go_home.pkl` |
| 477 | 0 | 42 finestre temporali | `encounter_go_home.pkl` |
| 478 | 0 | 32 finestre temporali | `encounter_go_home.pkl` |
| 479 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 479 | 1 | 4 finestre temporali | `encounter_go_home.pkl` |
| 479 | 2 | 8 finestre temporali | `encounter_go_home.pkl` |
| 479 | 3 | 2 finestre temporali | `encounter_go_home.pkl` |
| 479 | 4 | 5 finestre temporali | `encounter_go_home.pkl` |
| 479 | 5 | 5 finestre temporali | `encounter_go_home.pkl` |
| 480 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 481 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 482 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 483 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 484 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 485 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 486 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 487 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 487 | 1 | 11 finestre temporali | `encounter_go_home.pkl` |
| 488 | 0 | 26 finestre temporali | `encounter_go_home.pkl` |
| 491 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 492 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 492 | 1 | - | `encounter_go_home.pkl` |
| 494 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 495 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 496 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 497 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 498 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 499 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 500 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 501 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 502 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 503 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 503 | 1 | 10 finestre temporali | `encounter_go_home.pkl` |
| 504 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 505 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 506 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 507 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 508 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 509 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 510 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 511 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 512 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 513 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 514 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 515 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 516 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 517 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 518 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 519 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 520 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 521 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 522 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 523 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 524 | 0 | 26 finestre temporali | `encounter_go_home.pkl` |
| 525 | 0 | 34 finestre temporali | `encounter_go_home.pkl` |
| 526 | 0 | 35 finestre temporali | `encounter_go_home.pkl` |
| 527 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 528 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 529 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 530 | 0 | 36 finestre temporali | `encounter_go_home.pkl` |
| 531 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 532 | 0 | 53 finestre temporali | `encounter_go_home.pkl` |
| 533 | 0 | 56 finestre temporali | `encounter_go_home.pkl` |
| 534 | 0 | 56 finestre temporali | `encounter_go_home.pkl` |
| 535 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 536 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 537 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 538 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 539 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 540 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 541 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 542 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 543 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 544 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 545 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 546 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 547 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 548 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 549 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 549 | 1 | 5 finestre temporali | `encounter_go_home.pkl` |
| 550 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 550 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 550 | 2 | 4 finestre temporali | `encounter_go_home.pkl` |
| 551 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 552 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 553 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 554 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 554 | 1 | 28 finestre temporali | `encounter_go_home.pkl` |
| 555 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 555 | 2 | 28 finestre temporali | `encounter_go_home.pkl` |
| 556 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 557 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 558 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 559 | 0 | 42 finestre temporali | `encounter_go_home.pkl` |
| 560 | 0 | 42 finestre temporali | `encounter_go_home.pkl` |
| 561 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 562 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 562 | 1 | 15 finestre temporali | `encounter_go_home.pkl` |
| 563 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 564 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 565 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 566 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 567 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 568 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 569 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 570 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 570 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 571 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 571 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 572 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 573 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 574 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 575 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 576 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 577 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 578 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 579 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 580 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 581 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 582 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 583 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 584 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 585 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 585 | 1 | 15 finestre temporali | `encounter_go_home.pkl` |
| 585 | 2 | 17 finestre temporali | `encounter_go_home.pkl` |
| 585 | 3 | 16 finestre temporali | `encounter_go_home.pkl` |
| 586 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 586 | 1 | 15 finestre temporali | `encounter_go_home.pkl` |
| 586 | 2 | 17 finestre temporali | `encounter_go_home.pkl` |
| 586 | 3 | 16 finestre temporali | `encounter_go_home.pkl` |
| 587 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 588 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 589 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 590 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 591 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 592 | 0 | 39 finestre temporali | `encounter_go_home.pkl` |
| 593 | 0 | 39 finestre temporali | `encounter_go_home.pkl` |
| 594 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 595 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 596 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 597 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 598 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 599 | 0 | 61 finestre temporali | `encounter_go_home.pkl` |
| 600 | 0 | 61 finestre temporali | `encounter_go_home.pkl` |
| 601 | 0 | 61 finestre temporali | `encounter_go_home.pkl` |
| 602 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 603 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 604 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 605 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 606 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 607 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 608 | 0 | 28 finestre temporali | `encounter_go_home.pkl` |
| 609 | 0 | 29 finestre temporali | `encounter_go_home.pkl` |
| 610 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 611 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 612 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 613 | 0 | 34 finestre temporali | `encounter_go_home.pkl` |
| 614 | 0 | 35 finestre temporali | `encounter_go_home.pkl` |
| 615 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 616 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 617 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 618 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 618 | 1 | 23 finestre temporali | `encounter_go_home.pkl` |
| 619 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 620 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 621 | 0 | 33 finestre temporali | `encounter_go_home.pkl` |
| 622 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 623 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 624 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 625 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 626 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 627 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 628 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 628 | 1 | 19 finestre temporali | `encounter_go_home.pkl` |
| 629 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 630 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 631 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 632 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 633 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 634 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 635 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 636 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 637 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 638 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 639 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 640 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 641 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 641 | 1 | 12 finestre temporali | `encounter_go_home.pkl` |
| 642 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 642 | 1 | 10 finestre temporali | `encounter_go_home.pkl` |
| 643 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 644 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 645 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 645 | 1 | 12 finestre temporali | `encounter_go_home.pkl` |
| 646 | 0 | 25 finestre temporali | `encounter_go_home.pkl` |
| 647 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 647 | 1 | - | `encounter_go_home.pkl` |
| 648 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 649 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 649 | 1 | 7 finestre temporali | `encounter_go_home.pkl` |
| 649 | 2 | 7 finestre temporali | `encounter_go_home.pkl` |
| 649 | 3 | 7 finestre temporali | `encounter_go_home.pkl` |
| 649 | 4 | 7 finestre temporali | `encounter_go_home.pkl` |
| 650 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 651 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 652 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 653 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 654 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 655 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 656 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 657 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 658 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 659 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 660 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 661 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 662 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 663 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 664 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 2 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 3 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 4 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 5 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 6 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 7 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 8 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 9 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 10 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 11 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 12 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 13 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 14 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 15 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 16 | 3 finestre temporali | `encounter_go_home.pkl` |
| 664 | 17 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 2 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 3 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 4 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 5 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 6 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 7 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 8 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 9 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 10 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 11 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 12 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 13 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 14 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 15 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 16 | 3 finestre temporali | `encounter_go_home.pkl` |
| 665 | 17 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 2 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 3 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 4 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 5 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 6 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 7 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 8 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 9 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 10 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 11 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 12 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 13 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 14 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 15 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 16 | 3 finestre temporali | `encounter_go_home.pkl` |
| 666 | 17 | 3 finestre temporali | `encounter_go_home.pkl` |
| 667 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 668 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 669 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 669 | 1 | 2 finestre temporali | `encounter_go_home.pkl` |
| 669 | 2 | 2 finestre temporali | `encounter_go_home.pkl` |
| 669 | 3 | 2 finestre temporali | `encounter_go_home.pkl` |
| 669 | 4 | 2 finestre temporali | `encounter_go_home.pkl` |
| 670 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 670 | 1 | 2 finestre temporali | `encounter_go_home.pkl` |
| 670 | 2 | 2 finestre temporali | `encounter_go_home.pkl` |
| 670 | 3 | 2 finestre temporali | `encounter_go_home.pkl` |
| 670 | 4 | 2 finestre temporali | `encounter_go_home.pkl` |
| 671 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 671 | 1 | 2 finestre temporali | `encounter_go_home.pkl` |
| 671 | 2 | 2 finestre temporali | `encounter_go_home.pkl` |
| 671 | 3 | 2 finestre temporali | `encounter_go_home.pkl` |
| 671 | 4 | 2 finestre temporali | `encounter_go_home.pkl` |
| 672 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 673 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 674 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 675 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 676 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 676 | 1 | - | `encounter_go_home.pkl` |
| 676 | 2 | - | `encounter_go_home.pkl` |
| 676 | 3 | - | `encounter_go_home.pkl` |
| 676 | 4 | - | `encounter_go_home.pkl` |
| 676 | 5 | - | `encounter_go_home.pkl` |
| 676 | 6 | - | `encounter_go_home.pkl` |
| 676 | 7 | - | `encounter_go_home.pkl` |
| 676 | 8 | - | `encounter_go_home.pkl` |
| 676 | 9 | - | `encounter_go_home.pkl` |
| 677 | 0 | 42 finestre temporali | `encounter_go_home.pkl` |
| 678 | 0 | 42 finestre temporali | `encounter_go_home.pkl` |
| 678 | 1 | 42 finestre temporali | `encounter_go_home.pkl` |
| 679 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 680 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 681 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 682 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 683 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 684 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 685 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 686 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 687 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 688 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 689 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 690 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 691 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 692 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 693 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 694 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 695 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 696 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 697 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 698 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 699 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 700 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 701 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 702 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 703 | 0 | 30 finestre temporali | `encounter_go_home.pkl` |
| 704 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 705 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 706 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 707 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 708 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 709 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 710 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 710 | 1 | 7 finestre temporali | `encounter_go_home.pkl` |
| 710 | 2 | 6 finestre temporali | `encounter_go_home.pkl` |
| 710 | 3 | 6 finestre temporali | `encounter_go_home.pkl` |
| 711 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 711 | 1 | 7 finestre temporali | `encounter_go_home.pkl` |
| 711 | 2 | 6 finestre temporali | `encounter_go_home.pkl` |
| 711 | 3 | 6 finestre temporali | `encounter_go_home.pkl` |
| 712 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 713 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 713 | 1 | 12 finestre temporali | `encounter_go_home.pkl` |
| 714 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 715 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 716 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 717 | 0 | 22 finestre temporali | `encounter_go_home.pkl` |
| 719 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 720 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 720 | 1 | 6 finestre temporali | `encounter_go_home.pkl` |
| 721 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 722 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 723 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 724 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 724 | 1 | 11 finestre temporali | `encounter_go_home.pkl` |
| 725 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 726 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 727 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 728 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 729 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 730 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 731 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 732 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 733 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 734 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 735 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 736 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 737 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 738 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 739 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 740 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 741 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 741 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 741 | 2 | 3 finestre temporali | `encounter_go_home.pkl` |
| 741 | 3 | 3 finestre temporali | `encounter_go_home.pkl` |
| 742 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 743 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 744 | 0 | 35 finestre temporali | `encounter_go_home.pkl` |
| 744 | 1 | 14 finestre temporali | `encounter_go_home.pkl` |
| 745 | 0 | 35 finestre temporali | `encounter_go_home.pkl` |
| 745 | 1 | 35 finestre temporali | `encounter_go_home.pkl` |
| 745 | 2 | 14 finestre temporali | `encounter_go_home.pkl` |
| 747 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 748 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 749 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 750 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 751 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 752 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 753 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 754 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 755 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 756 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 757 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 758 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 759 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 760 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 761 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 762 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 763 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 764 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 765 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 766 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 767 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 768 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 769 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 770 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 775 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 776 | 0 | 46 finestre temporali | `encounter_go_home.pkl` |
| 777 | 0 | 8 finestre temporali | `encounter_go_home.pkl` |
| 778 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 779 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 780 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 781 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 782 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 783 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 784 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 785 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 786 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 787 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 788 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 789 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 790 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 791 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 792 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 793 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 794 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 795 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 796 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 797 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 798 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 799 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 800 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 802 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 803 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 804 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 805 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 806 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 807 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 808 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 809 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 810 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 811 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 812 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 813 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 814 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 815 | 0 | 16 finestre temporali | `encounter_go_home.pkl` |
| 816 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 817 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 818 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 819 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 820 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 821 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 822 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 823 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 824 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 825 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 826 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 827 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 828 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 829 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 830 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 831 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 832 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 835 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 836 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 837 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 838 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 839 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 840 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 841 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 842 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 843 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 844 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 848 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 849 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 849 | 1 | 12 finestre temporali | `encounter_go_home.pkl` |
| 850 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 851 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 852 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 853 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 854 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 854 | 1 | 14 finestre temporali | `encounter_go_home.pkl` |
| 855 | 0 | 14 finestre temporali | `encounter_go_home.pkl` |
| 855 | 1 | 14 finestre temporali | `encounter_go_home.pkl` |
| 856 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 857 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 858 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 859 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 860 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 861 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 862 | 0 | 29 finestre temporali | `encounter_go_home.pkl` |
| 863 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 864 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 865 | 0 | 23 finestre temporali | `encounter_go_home.pkl` |
| 866 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 867 | 0 | 15 finestre temporali | `encounter_go_home.pkl` |
| 870 | 0 | 19 finestre temporali | `encounter_go_home.pkl` |
| 872 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 873 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 874 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 876 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 876 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 877 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 884 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 885 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 886 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 887 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 888 | 0 | 17 finestre temporali | `encounter_go_home.pkl` |
| 889 | 0 | 18 finestre temporali | `encounter_go_home.pkl` |
| 891 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 892 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 892 | 1 | 1 finestre temporali | `encounter_go_home.pkl` |
| 893 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 894 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 895 | 0 | 13 finestre temporali | `encounter_go_home.pkl` |
| 899 | 0 | 11 finestre temporali | `encounter_go_home.pkl` |
| 900 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 901 | 0 | 20 finestre temporali | `encounter_go_home.pkl` |
| 903 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 904 | 0 | 24 finestre temporali | `encounter_go_home.pkl` |
| 905 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 905 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 906 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 907 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 908 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 909 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 910 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 911 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 912 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 913 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 914 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 915 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 916 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 916 | 1 | 2 finestre temporali | `encounter_go_home.pkl` |
| 917 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 918 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 919 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 920 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 921 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 922 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 923 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 924 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 925 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 925 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 926 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 927 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 928 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 929 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 930 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 931 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 931 | 1 | 1 finestre temporali | `encounter_go_home.pkl` |
| 931 | 2 | 1 finestre temporali | `encounter_go_home.pkl` |
| 931 | 3 | 1 finestre temporali | `encounter_go_home.pkl` |
| 932 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 933 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 934 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 935 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 936 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 937 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 938 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 939 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 940 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 941 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 944 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 945 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 948 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 949 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 950 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 955 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 956 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 957 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 958 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 959 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 960 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 961 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 962 | 0 | 21 finestre temporali | `encounter_go_home.pkl` |
| 965 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 966 | 0 | 7 finestre temporali | `encounter_go_home.pkl` |
| 968 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 969 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 970 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 971 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 972 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 973 | 0 | 2 finestre temporali | `encounter_go_home.pkl` |
| 974 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 975 | 0 | 5 finestre temporali | `encounter_go_home.pkl` |
| 977 | 0 | 6 finestre temporali | `encounter_go_home.pkl` |
| 978 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 978 | 1 | 4 finestre temporali | `encounter_go_home.pkl` |
| 978 | 2 | 4 finestre temporali | `encounter_go_home.pkl` |
| 979 | 0 | 27 finestre temporali | `encounter_go_home.pkl` |
| 980 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 982 | 0 | 3 finestre temporali | `encounter_go_home.pkl` |
| 982 | 1 | 3 finestre temporali | `encounter_go_home.pkl` |
| 983 | 0 | 12 finestre temporali | `encounter_go_home.pkl` |
| 996 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 997 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 998 | 0 | 9 finestre temporali | `encounter_go_home.pkl` |
| 999 | 1 | 4 finestre temporali | `encounter_go_home.pkl` |
| 1000 | 0 | 4 finestre temporali | `encounter_go_home.pkl` |
| 1011 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |
| 1012 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 1012 | 1 | 10 finestre temporali | `encounter_go_home.pkl` |
| 1013 | 0 | 10 finestre temporali | `encounter_go_home.pkl` |
| 1013 | 1 | 10 finestre temporali | `encounter_go_home.pkl` |
| 1019 | 0 | 1 finestre temporali | `encounter_go_home.pkl` |

## Pokemon GO verso Let's Go

| Dex | Forma | Descrizione | Riferimento nella fonte |
|---|---|---|---|
| 1 | 0 | 33 finestre temporali | `encounter_go_lgpe.pkl` |
| 2 | 0 | 35 finestre temporali | `encounter_go_lgpe.pkl` |
| 3 | 0 | 54 finestre temporali | `encounter_go_lgpe.pkl` |
| 4 | 0 | 37 finestre temporali | `encounter_go_lgpe.pkl` |
| 5 | 0 | 40 finestre temporali | `encounter_go_lgpe.pkl` |
| 6 | 0 | 67 finestre temporali | `encounter_go_lgpe.pkl` |
| 7 | 0 | 33 finestre temporali | `encounter_go_lgpe.pkl` |
| 8 | 0 | 34 finestre temporali | `encounter_go_lgpe.pkl` |
| 9 | 0 | 52 finestre temporali | `encounter_go_lgpe.pkl` |
| 10 | 0 | 8 finestre temporali | `encounter_go_lgpe.pkl` |
| 11 | 0 | 10 finestre temporali | `encounter_go_lgpe.pkl` |
| 12 | 0 | 19 finestre temporali | `encounter_go_lgpe.pkl` |
| 13 | 0 | 5 finestre temporali | `encounter_go_lgpe.pkl` |
| 14 | 0 | 5 finestre temporali | `encounter_go_lgpe.pkl` |
| 15 | 0 | 13 finestre temporali | `encounter_go_lgpe.pkl` |
| 16 | 0 | 4 finestre temporali | `encounter_go_lgpe.pkl` |
| 17 | 0 | 4 finestre temporali | `encounter_go_lgpe.pkl` |
| 18 | 0 | 24 finestre temporali | `encounter_go_lgpe.pkl` |
| 19 | 0 | 2 finestre temporali | `encounter_go_lgpe.pkl` |
| 20 | 0 | 9 finestre temporali | `encounter_go_lgpe.pkl` |
| 21 | 0 | 3 finestre temporali | `encounter_go_lgpe.pkl` |
| 22 | 0 | 7 finestre temporali | `encounter_go_lgpe.pkl` |
| 23 | 0 | 10 finestre temporali | `encounter_go_lgpe.pkl` |
| 24 | 0 | 12 finestre temporali | `encounter_go_lgpe.pkl` |
| 25 | 0 | 105 finestre temporali | `encounter_go_lgpe.pkl` |
| 26 | 0 | 111 finestre temporali | `encounter_go_lgpe.pkl` |
| 27 | 0 | 9 finestre temporali | `encounter_go_lgpe.pkl` |
| 28 | 0 | 17 finestre temporali | `encounter_go_lgpe.pkl` |
| 29 | 0 | 3 finestre temporali | `encounter_go_lgpe.pkl` |
| 30 | 0 | 3 finestre temporali | `encounter_go_lgpe.pkl` |
| 31 | 0 | 17 finestre temporali | `encounter_go_lgpe.pkl` |
| 32 | 0 | 7 finestre temporali | `encounter_go_lgpe.pkl` |
| 33 | 0 | 12 finestre temporali | `encounter_go_lgpe.pkl` |
| 34 | 0 | 28 finestre temporali | `encounter_go_lgpe.pkl` |
| 35 | 0 | 19 finestre temporali | `encounter_go_lgpe.pkl` |
| 36 | 0 | 24 finestre temporali | `encounter_go_lgpe.pkl` |
| 37 | 0 | 18 finestre temporali | `encounter_go_lgpe.pkl` |
| 38 | 0 | 25 finestre temporali | `encounter_go_lgpe.pkl` |
| 39 | 0 | 16 finestre temporali | `encounter_go_lgpe.pkl` |
| 40 | 0 | 28 finestre temporali | `encounter_go_lgpe.pkl` |
| 41 | 0 | 4 finestre temporali | `encounter_go_lgpe.pkl` |
| 42 | 0 | 8 finestre temporali | `encounter_go_lgpe.pkl` |
| 43 | 0 | 3 finestre temporali | `encounter_go_lgpe.pkl` |
| 44 | 0 | 6 finestre temporali | `encounter_go_lgpe.pkl` |
| 45 | 0 | 16 finestre temporali | `encounter_go_lgpe.pkl` |
| 46 | 0 | 10 finestre temporali | `encounter_go_lgpe.pkl` |
| 47 | 0 | 14 finestre temporali | `encounter_go_lgpe.pkl` |
| 48 | 0 | 4 finestre temporali | `encounter_go_lgpe.pkl` |
| 49 | 0 | 8 finestre temporali | `encounter_go_lgpe.pkl` |
| 50 | 0 | 15 finestre temporali | `encounter_go_lgpe.pkl` |
| 51 | 0 | 17 finestre temporali | `encounter_go_lgpe.pkl` |
| 52 | 0 | 12 finestre temporali | `encounter_go_lgpe.pkl` |
| 53 | 0 | 13 finestre temporali | `encounter_go_lgpe.pkl` |
| 54 | 0 | 15 finestre temporali | `encounter_go_lgpe.pkl` |
| 55 | 0 | 20 finestre temporali | `encounter_go_lgpe.pkl` |
| 56 | 0 | 13 finestre temporali | `encounter_go_lgpe.pkl` |
| 57 | 0 | 23 finestre temporali | `encounter_go_lgpe.pkl` |
| 58 | 0 | 7 finestre temporali | `encounter_go_lgpe.pkl` |
| 59 | 0 | 20 finestre temporali | `encounter_go_lgpe.pkl` |
| 60 | 0 | 4 finestre temporali | `encounter_go_lgpe.pkl` |
| 61 | 0 | 8 finestre temporali | `encounter_go_lgpe.pkl` |
| 62 | 0 | 22 finestre temporali | `encounter_go_lgpe.pkl` |
| 63 | 0 | 14 finestre temporali | `encounter_go_lgpe.pkl` |
| 64 | 0 | 17 finestre temporali | `encounter_go_lgpe.pkl` |
| 65 | 0 | 38 finestre temporali | `encounter_go_lgpe.pkl` |
| 66 | 0 | 21 finestre temporali | `encounter_go_lgpe.pkl` |
| 67 | 0 | 24 finestre temporali | `encounter_go_lgpe.pkl` |
| 68 | 0 | 56 finestre temporali | `encounter_go_lgpe.pkl` |
| 69 | 0 | 4 finestre temporali | `encounter_go_lgpe.pkl` |
| 70 | 0 | 9 finestre temporali | `encounter_go_lgpe.pkl` |
| 71 | 0 | 17 finestre temporali | `encounter_go_lgpe.pkl` |
| 72 | 0 | 4 finestre temporali | `encounter_go_lgpe.pkl` |
| 73 | 0 | 9 finestre temporali | `encounter_go_lgpe.pkl` |
| 74 | 0 | 9 finestre temporali | `encounter_go_lgpe.pkl` |
| 75 | 0 | 13 finestre temporali | `encounter_go_lgpe.pkl` |
| 76 | 0 | 47 finestre temporali | `encounter_go_lgpe.pkl` |
| 77 | 0 | 10 finestre temporali | `encounter_go_lgpe.pkl` |
| 78 | 0 | 14 finestre temporali | `encounter_go_lgpe.pkl` |
| 79 | 0 | 21 finestre temporali | `encounter_go_lgpe.pkl` |
| 80 | 0 | 32 finestre temporali | `encounter_go_lgpe.pkl` |
| 81 | 0 | 15 finestre temporali | `encounter_go_lgpe.pkl` |
| 82 | 0 | 39 finestre temporali | `encounter_go_lgpe.pkl` |
| 83 | 0 | 5 finestre temporali | `encounter_go_lgpe.pkl` |
| 84 | 0 | 9 finestre temporali | `encounter_go_lgpe.pkl` |
| 85 | 0 | 10 finestre temporali | `encounter_go_lgpe.pkl` |
| 86 | 0 | 8 finestre temporali | `encounter_go_lgpe.pkl` |
| 87 | 0 | 21 finestre temporali | `encounter_go_lgpe.pkl` |
| 88 | 0 | 14 finestre temporali | `encounter_go_lgpe.pkl` |
| 89 | 0 | 22 finestre temporali | `encounter_go_lgpe.pkl` |
| 90 | 0 | 10 finestre temporali | `encounter_go_lgpe.pkl` |
| 91 | 0 | 22 finestre temporali | `encounter_go_lgpe.pkl` |
| 92 | 0 | 20 finestre temporali | `encounter_go_lgpe.pkl` |
| 93 | 0 | 26 finestre temporali | `encounter_go_lgpe.pkl` |
| 94 | 0 | 67 finestre temporali | `encounter_go_lgpe.pkl` |
| 95 | 0 | 32 finestre temporali | `encounter_go_lgpe.pkl` |
| 96 | 0 | 9 finestre temporali | `encounter_go_lgpe.pkl` |
| 97 | 0 | 14 finestre temporali | `encounter_go_lgpe.pkl` |
| 98 | 0 | 17 finestre temporali | `encounter_go_lgpe.pkl` |
| 99 | 0 | 21 finestre temporali | `encounter_go_lgpe.pkl` |
| 100 | 0 | 11 finestre temporali | `encounter_go_lgpe.pkl` |
| 101 | 0 | 15 finestre temporali | `encounter_go_lgpe.pkl` |
| 102 | 0 | 4 finestre temporali | `encounter_go_lgpe.pkl` |
| 103 | 0 | 20 finestre temporali | `encounter_go_lgpe.pkl` |
| 104 | 0 | 10 finestre temporali | `encounter_go_lgpe.pkl` |
| 105 | 0 | 18 finestre temporali | `encounter_go_lgpe.pkl` |
| 106 | 0 | 15 finestre temporali | `encounter_go_lgpe.pkl` |
| 107 | 0 | 15 finestre temporali | `encounter_go_lgpe.pkl` |
| 108 | 0 | 26 finestre temporali | `encounter_go_lgpe.pkl` |
| 109 | 0 | 7 finestre temporali | `encounter_go_lgpe.pkl` |
| 110 | 0 | 12 finestre temporali | `encounter_go_lgpe.pkl` |
| 111 | 0 | 9 finestre temporali | `encounter_go_lgpe.pkl` |
| 112 | 0 | 39 finestre temporali | `encounter_go_lgpe.pkl` |
| 113 | 0 | 37 finestre temporali | `encounter_go_lgpe.pkl` |
| 114 | 0 | 17 finestre temporali | `encounter_go_lgpe.pkl` |
| 115 | 0 | 13 finestre temporali | `encounter_go_lgpe.pkl` |
| 116 | 0 | 6 finestre temporali | `encounter_go_lgpe.pkl` |
| 117 | 0 | 10 finestre temporali | `encounter_go_lgpe.pkl` |
| 118 | 0 | 3 finestre temporali | `encounter_go_lgpe.pkl` |
| 119 | 0 | 3 finestre temporali | `encounter_go_lgpe.pkl` |
| 120 | 0 | 10 finestre temporali | `encounter_go_lgpe.pkl` |
| 121 | 0 | 19 finestre temporali | `encounter_go_lgpe.pkl` |
| 122 | 0 | 6 finestre temporali | `encounter_go_lgpe.pkl` |
| 123 | 0 | 41 finestre temporali | `encounter_go_lgpe.pkl` |
| 124 | 0 | 26 finestre temporali | `encounter_go_lgpe.pkl` |
| 125 | 0 | 26 finestre temporali | `encounter_go_lgpe.pkl` |
| 126 | 0 | 28 finestre temporali | `encounter_go_lgpe.pkl` |
| 127 | 0 | 33 finestre temporali | `encounter_go_lgpe.pkl` |
| 128 | 0 | 5 finestre temporali | `encounter_go_lgpe.pkl` |
| 129 | 0 | 24 finestre temporali | `encounter_go_lgpe.pkl` |
| 130 | 0 | 52 finestre temporali | `encounter_go_lgpe.pkl` |
| 131 | 0 | 49 finestre temporali | `encounter_go_lgpe.pkl` |
| 132 | 0 | 7 finestre temporali | `encounter_go_lgpe.pkl` |
| 133 | 0 | 15 finestre temporali | `encounter_go_lgpe.pkl` |
| 134 | 0 | 27 finestre temporali | `encounter_go_lgpe.pkl` |
| 135 | 0 | 28 finestre temporali | `encounter_go_lgpe.pkl` |
| 136 | 0 | 30 finestre temporali | `encounter_go_lgpe.pkl` |
| 137 | 0 | 12 finestre temporali | `encounter_go_lgpe.pkl` |
| 138 | 0 | 18 finestre temporali | `encounter_go_lgpe.pkl` |
| 139 | 0 | 23 finestre temporali | `encounter_go_lgpe.pkl` |
| 140 | 0 | 14 finestre temporali | `encounter_go_lgpe.pkl` |
| 141 | 0 | 22 finestre temporali | `encounter_go_lgpe.pkl` |
| 142 | 0 | 41 finestre temporali | `encounter_go_lgpe.pkl` |
| 143 | 0 | 38 finestre temporali | `encounter_go_lgpe.pkl` |
| 144 | 0 | 34 finestre temporali | `encounter_go_lgpe.pkl` |
| 145 | 0 | 28 finestre temporali | `encounter_go_lgpe.pkl` |
| 146 | 0 | 28 finestre temporali | `encounter_go_lgpe.pkl` |
| 147 | 0 | 28 finestre temporali | `encounter_go_lgpe.pkl` |
| 148 | 0 | 28 finestre temporali | `encounter_go_lgpe.pkl` |
| 149 | 0 | 59 finestre temporali | `encounter_go_lgpe.pkl` |
| 150 | 0 | 20 finestre temporali | `encounter_go_lgpe.pkl` |
| 808 | 0 | 12 finestre temporali | `encounter_go_lgpe.pkl` |
| 809 | 0 | 12 finestre temporali | `encounter_go_lgpe.pkl` |
| 19 | 1 | 9 finestre temporali | `encounter_go_lgpe.pkl` |
| 20 | 1 | 11 finestre temporali | `encounter_go_lgpe.pkl` |
| 26 | 1 | 45 finestre temporali | `encounter_go_lgpe.pkl` |
| 27 | 1 | 26 finestre temporali | `encounter_go_lgpe.pkl` |
| 28 | 1 | 26 finestre temporali | `encounter_go_lgpe.pkl` |
| 37 | 1 | 34 finestre temporali | `encounter_go_lgpe.pkl` |
| 38 | 1 | 36 finestre temporali | `encounter_go_lgpe.pkl` |
| 50 | 1 | 14 finestre temporali | `encounter_go_lgpe.pkl` |
| 51 | 1 | 18 finestre temporali | `encounter_go_lgpe.pkl` |
| 52 | 1 | 24 finestre temporali | `encounter_go_lgpe.pkl` |
| 53 | 1 | 24 finestre temporali | `encounter_go_lgpe.pkl` |
| 74 | 1 | 15 finestre temporali | `encounter_go_lgpe.pkl` |
| 75 | 1 | 28 finestre temporali | `encounter_go_lgpe.pkl` |
| 76 | 1 | 28 finestre temporali | `encounter_go_lgpe.pkl` |
| 88 | 1 | 20 finestre temporali | `encounter_go_lgpe.pkl` |
| 89 | 1 | 23 finestre temporali | `encounter_go_lgpe.pkl` |
| 103 | 1 | 45 finestre temporali | `encounter_go_lgpe.pkl` |
| 105 | 1 | 51 finestre temporali | `encounter_go_lgpe.pkl` |

