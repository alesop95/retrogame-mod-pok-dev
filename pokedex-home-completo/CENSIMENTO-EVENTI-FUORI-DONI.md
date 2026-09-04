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

Le voci censite sono 422 e portano 256 specie distinte; quelle sotto scadenza sono 409 e portano 251 specie distinte. Il confronto che conta è con le 2686 voci sotto scadenza dell'asse degli eventi della lista di spunta: queste non vi sono comprese, e ciascuna è un collezionabile che il 26 febbraio 2027 chiude come tutti gli altri.

## Le voci che nessuna fonte dichiara distribuite

Vanno scritte perché la loro assenza dal censimento è un risultato e non una lacuna: chi le cercasse senza questa sezione concluderebbe che il censimento sia incompleto, e cercherebbe per giorni una distribuzione che non è mai avvenuta.

| Gen | Oggetto | Luogo | Dex | Perché non c'è |
|---|---|---|---|---|
| 4 | Flauto Azzurro | Colonna Lancia | 493 | il verificatore non porta alcuna voce per questo incontro, cioe' non fu mai distribuito per via ufficiale in alcuna regione |
| 4 | Lettera di Oak | Giardino Floreale | 492 | in Diamante e Perla la voce esiste nella fonte ma e' commentata come non distribuita: la ebbe soltanto Platino |

## Che cosa questo censimento non copre

Un censimento che tacesse le proprie lacune sarebbe peggio di uno dichiarato incompleto, perché chi lo legge conta le voci e conclude di avere l'insieme intero. Queste classi esistono, il programma non le legge, e il motivo è scritto accanto a ciascuna.

| Gen | Classe | Dove sta nella fonte | Perché non è letta |
|---|---|---|---|
| 8 | Incursioni da distribuzione di Spada e Scudo | Gen8/Encounters8Nest.cs, tabelle sw_dist, sh_dist, i sotterranei e le grotte di cristallo | sono risorse binarie con un formato proprio che non abbiamo ancora letto; sono senza scadenza, quindi la loro assenza non tocca alcun conto sotto scadenza |
| 9 | Incursioni da distribuzione di Scarlatto e Violetto | Gen9/Encounters9.cs, tabelle dist_paldea e might_paldea | stessa ragione dell'ottava generazione, e stessa conseguenza |
| 7 | Trasferimenti da Pokemon GO | Live/EncountersGO.cs e le tabelle encounter_go_home.pkl e encounter_go_lgpe.pkl | non sono distribuzioni ma una porta di ingresso permanente e senza scadenza, quindi stanno fuori dall'ambito di questo censimento e non fra le sue lacune |

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

