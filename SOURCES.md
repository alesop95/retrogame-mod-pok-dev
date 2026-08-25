# Registro delle fonti

Questo file e' il registro unico delle fonti tecniche del progetto, condiviso da tutti i sottoprogetti. Nasce dal lavoro sul ponte fra generazioni, che e' il track che ha richiesto la ricerca piu' profonda, ma non gli appartiene: i disassemblati dei giochi, la documentazione dell'hardware, i formati di salvataggio e gli editor servono anche alla correzione dell'inventario di Smeraldo, al modding del 3DS e allo scambio con la Switch, e tenerli in un posto solo evita che ogni handoff riscopra le stesse cose.

## Come si usa

Ogni voce dichiara che cosa la fonte documenta in modo autorevole, non solo che esiste, perche' il valore di una fonte sta in cio' su cui la si puo' citare. La colonna dei track usa le sigle BRI per il ponte fra generazioni, SME per la correzione del salvataggio di Smeraldo, 3DS per il modding della console e il dump delle cartucce, LDN per lo scambio fra GBA e Switch, e TUTTI quando serve trasversalmente.

Le fonti sono ordinate per affidabilita' decrescente, e l'ordine e' normativo quando due fonti si contraddicono. Il livello 1 e' il codice del gioco e la documentazione dell'hardware ricostruita e verificata dalla community: e' la verita' operativa. Il livello 2 e' la documentazione di dominio, wiki e riferimenti, accurata ma non infallibile. Il livello 3 sono le implementazioni di riferimento, cioe' codice di terzi che funziona sul campo e quindi incorpora conoscenza verificata dall'uso, ma anche scelte arbitrarie che non vanno confuse con specifiche. Il livello 4 sono articoli, blog e video, preziosi per capire il perche' e inaffidabili per gli offset. Il livello 5 sono forum e community, che rispondono a domande senza risposta scritta e non sono citabili finche' non si verifica.

La gerarchia non e' un formalismo, e vale la pena registrare cosa ha prodotto in concreto durante la stesura di `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`. Il livello 2 sbagliava la tabella caratteri di generazione 1, collocando le cifre a 0xF0 invece di 0xF6, e quella di generazione 3, collocando le maiuscole a 0xC1 invece di 0xBB. Sbagliava il calcolo del checksum di generazione 3, descrivendolo byte per byte invece che per parole da 16 bit, che e' un errore capace di distruggere un Pokemon. Dava due cifre in conflitto sulla dimensione del blocco di scambio, 415 e 424, mentre la somma di costanti nel disassemblato dice 424 sul filo e 418 di dati. E il livello 3 si e' rivelato in disaccordo con la propria documentazione, perche' il PCCS documenta quattro metodi di conversione nel README e nel codice ne implementa uno. In tutti i casi ha vinto il livello 1.

Quando una sessione futura trova una fonte nuova che serve, la aggiunge qui con la sua riga e la sua colonna dei track, invece di lasciarla dentro il proprio handoff: gli handoff citano il registro, il registro non duplica gli handoff.

Nota operativa sul recupero automatico, che serve a non ripetere tentativi inutili. I file grezzi di GitHub e le pagine di Bulbapedia si recuperano bene, e per i repository conviene comunque un clone superficiale con `git clone --depth 1`, perche' permette di cercare nel codice invece di leggere riassunti. Il dominio `glitchcity.wiki` respinge le richieste automatiche con un errore 403 e va letto dal mirror statico di Ninty Conservation o a mano dal browser. Reddit non e' raggiungibile in alcun modo dagli strumenti di questa sessione: i thread elencati piu' sotto provengono dai risultati di ricerca e non sono stati letti, quindi valgono come indicazione di dove cercare e non come fonte verificata. YouTube restituisce una pagina di consenso invece del contenuto, quindi i canali sono identificati per URL ma i video non sono stati guardati.

## Livello 1: disassemblati, decompilazioni e documentazione dell'hardware

Sono la fonte autorevole su ogni offset, ogni campo di bit, ogni formula e ogni tabella. Un dato letto qui non ha bisogno di conferma; un dato che li contraddice e' sbagliato.

| Fonte | URL | Autorevole su | Track |
|---|---|---|---|
| pret/pokered | https://github.com/pret/pokered | strutture, salvataggio, protocollo di scambio e costanti seriali di Rosso e Blu; `macros/ram.asm`, `ram/wram.asm`, `constants/serial_constants.asm`, `engine/link/cable_club.asm` | BRI |
| pret/pokeyellow | https://github.com/pret/pokeyellow | le stesse cose per Giallo, incluse le differenze di offset | BRI |
| pret/pokegold | https://github.com/pret/pokegold | strutture e salvataggio di Oro e Argento | BRI |
| pret/pokecrystal | https://github.com/pret/pokecrystal | ordine dei nibble dei DV in `engine/pokemon/move_mon.asm`, tabella caratteri in `constants/charmap.asm`, strutture di invio native e Time Capsule in `ram/wram.asm` | BRI |
| pret/pokeruby | https://github.com/pret/pokeruby | strutture e salvataggio di Rubino e Zaffiro, e le differenze rispetto a Smeraldo | BRI, SME |
| pret/pokeemerald | https://github.com/pret/pokeemerald | struttura cifrata Gen 3 e checksum in `src/pokemon.c`, chiave di cifratura e offset dello zaino in `include/global.h`, maschera delle quantita' in `src/item.c`, settori del salvataggio in `include/save.h` e `src/save.c` | BRI, SME |
| pret/pokefirered | https://github.com/pret/pokefirered | le stesse cose per Rosso Fuoco e Verde Foglia, che sono i giochi dello scambio LDN | BRI, LDN |
| Documentazione pokeemerald | https://pret-pokeemerald.mintlify.app/ | guida navigabile alla decompilazione di Smeraldo, comoda per orientarsi prima di aprire il sorgente | BRI, SME |
| Pan Docs | https://gbdev.io/pandocs/ | riferimento tecnico completo dell'hardware Game Boy, compreso il trasferimento seriale via cavo Link | BRI |
| Pan Docs, sorgente | https://github.com/gbdev/pandocs | la stessa cosa in Markdown, diffabile e citabile per revisione | BRI |
| GBATEK | https://problemkaputt.de/gbatek.htm | riferimento tecnico dell'hardware Game Boy Advance | BRI, SME, LDN |
| GBATEK, multiboot | https://problemkaputt.de/gbatek-bios-multi-boot-single-game-pak.htm | protocollo di avvio di un programma in RAM ricevuto dal cavo, cioe' il meccanismo su cui poggia il ponte | BRI |
| GBATEK, porte di comunicazione | https://problemkaputt.de/gbatek-gba-communication-ports.htm | modalita' normale, multiplayer, UART e JOY Bus della porta seriale GBA | BRI, LDN |
| rgbds | https://github.com/gbdev/rgbds | assemblatore necessario per compilare i disassemblati Game Boy | BRI |
| devkitPro e libtonc | https://github.com/devkitPro/libtonc | toolchain e libreria C per compilare homebrew GBA | BRI |
| 3dbrew | https://www.3dbrew.org | documentazione tecnica dell'hardware e del software di sistema del 3DS, compreso il formato dei salvataggi | 3DS |

## Livello 2: wiki e riferimenti di dominio

Vale la pena elencare le pagine singole e non solo i domini, perche' una wiki grande e' inutilizzabile come citazione mentre una pagina precisa e' una fonte.

| Fonte | URL | Autorevole su | Track |
|---|---|---|---|
| Bulbapedia, struttura dati Gen 1 | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_I) | offset dei 44 e 33 byte, impaccamento dei PP | BRI |
| Bulbapedia, struttura dati Gen 2 | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_II) | offset dei 48 e 32 byte, dati di cattura di Cristallo, Pokerus | BRI |
| Bulbapedia, struttura dati Gen 3 | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_III) | intestazione in chiaro ed estensione di squadra | BRI, SME, LDN |
| Bulbapedia, sottostrutture Gen 3 | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_substructures_(Generation_III) | tabella delle 24 permutazioni e campi di bit delle quattro sottostrutture | BRI, SME, LDN |
| Bulbapedia, salvataggio Gen 1 | https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_I) | banchi, offset di squadra e box, checksum | BRI |
| Bulbapedia, salvataggio Gen 2 | https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_II) | offset per gioco e lingua, doppio checksum, copia di backup | BRI |
| Bulbapedia, salvataggio Gen 3 | https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_III) | sezioni da 4096 byte, firma, scelta dello slot | SME, BRI, LDN |
| Bulbapedia, valore di personalita' | https://bulbapedia.bulbagarden.net/wiki/Personality_value | formule di natura, sesso, abilita', lucentezza, lettera di Unown | BRI |
| Bulbapedia, valori individuali | https://bulbapedia.bulbagarden.net/wiki/Individual_values | derivazione del DV dei punti salute, lucentezza da DV in Gen 2 | BRI |
| Bulbapedia, codifica caratteri Gen 1 | https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_I) | tabella caratteri; sbagliata sulle cifre, usare il charmap del disassemblato | BRI |
| Bulbapedia, codifica caratteri Gen 3 | https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_III) | codici di controllo 0xFC, 0xFD e 0xFE; sbagliata sulle maiuscole | BRI, SME |
| Bulbapedia, indici Gen 1 | https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_index_number_(Generation_I) | mappatura da indice interno a numero nazionale e posizioni di MissingNo | BRI |
| Bulbapedia, indici Gen 3 | https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_index_number_(Generation_III) | numerazione interna e ordinamento delle specie di Hoenn | BRI |
| Bulbapedia, esecuzione di codice arbitrario | https://bulbapedia.bulbagarden.net/wiki/Arbitrary_code_execution | inquadramento enciclopedico della tecnica e della sua storia | BRI |
| Glitch City Wiki | https://glitchcity.wiki | catalogo dell'esecuzione di codice arbitrario e dei glitch di Gen 1 e 2; respinge il recupero automatico | BRI |
| Glitch City, mirror statico | https://nintyconservation.github.io/glitchcity.wiki/glitchcity.wiki/Arbitrary_code_execution.html | la stessa conoscenza in forma recuperabile automaticamente | BRI |
| Glitch City, esecuzione remota | https://glitchcity.wiki/wiki/Remote_code_execution | il vettore che passa dal cavo Link, cioe' quello che usa il ponte | BRI |
| Glitch City, cart-swap | https://glitchcity.wiki/wiki/Cart-swap_arbitrary_code_execution | esecuzione di codice sfruttando cio' che resta in RAM dopo uno scambio di cartuccia | BRI |
| Data Crystal, Gen 3 | https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_3rd_Generation | mappe di RAM e ROM dei giochi Gen 3, utili nella diagnosi di un salvataggio corrotto | SME, BRI |
| Data Crystal, mappa RAM di Cristallo | https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_Crystal/RAM_map | indirizzi in RAM di Gen 2, complementari al disassemblato | BRI |
| Data Crystal, mappa RAM di Rosso e Blu | https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_Red_and_Blue/RAM_map | indirizzi in RAM di Gen 1, utili per capire dove cade un payload | BRI |
| Hacks Guide Wiki, 3DS | https://wiki.hacks.guide/wiki/3DS:Dump_titles_and_game_cartridges | procedura di dump di titoli e cartucce, versione wiki e aggiornata della guida | 3DS |
| Hacks Guide Wiki, esportazione salvataggi | https://wiki.hacks.guide/wiki/3DS:Export_saves | estrazione dei salvataggi dalla console | 3DS |
| ConsoleMods Wiki, backup di gioco | https://consolemods.org/wiki/3DS:Creating_Game_Backups | seconda fonte indipendente sulla procedura di dump | 3DS |
| ConsoleMods Wiki, backup dei salvataggi | https://consolemods.org/wiki/3DS:Creating_Game_Save_Backups | seconda fonte indipendente sui backup dei salvataggi | 3DS |
| DS-Homebrew Wiki | https://wiki.ds-homebrew.com/godmode9i/ | GodMode9i, il gestore di file di basso livello del lato DS | 3DS |
| dumping.guide | https://dumping.guide/carts/nintendo/ds | procedura di dump delle cartucce DS orientata alla conservazione | 3DS |
| GameBrew | https://www.gamebrew.org/wiki/3DS_Save_File_Extraction_Tools | censimento degli strumenti di estrazione dei salvataggi 3DS | 3DS |
| PokeAPI | https://pokeapi.co | dati di specie, mosse e abilita' via API, alternativa alla lettura da ROM per un tool su PC | BRI |
| Serebii | https://www.serebii.net | dati di gioco enciclopedici, utile come controprova rapida | TUTTI |
| Smogon, guide RNG | https://www.smogon.com/ingame/rng/ | comportamento del generatore pseudocasuale dei giochi | BRI |

## Livello 3: implementazioni di riferimento

Codice che funziona sul campo. Va letto come prova di fattibilita' e come repertorio di soluzioni, mai come specifica: dove una di queste implementazioni fa una scelta, la scelta e' sua e non del formato.

| Fonte | URL | Che cosa offre | Track |
|---|---|---|---|
| Poke Transporter GB | https://github.com/Striaton-Lab-Team/Poke_Transporter_GB | il ponte di riferimento: homebrew GBA in multiboot, cavo GBC, licenza MIT; `source/gameboy_colour.cpp` mostra che il payload Z80 viaggia sul cavo al posto della squadra, e `tools/payload-generator` lo costruisce per lingua e variante di ROM | BRI |
| PCCS | https://github.com/Striaton-Lab-Team/Pokemon-Community-Conversion-Standard | specifica dei quattro metodi di conversione nel README e implementazione del solo ORIGINAL nel codice; `source/GBPokemon.cpp` contiene il campionamento con rifiuto del valore di personalita' e l'uso dell'ID segreto per la lucentezza | BRI |
| Pokemon-Gen3-to-Gen-X | https://github.com/Lorenzooone/Pokemon-Gen3-to-Gen-X | homebrew GBA che scambia fra Gen 3 e Gen 1 e 2 usando il protocollo normale e non exploit, piu' gestione dell'orologio di Rubino, Zaffiro e Smeraldo | BRI |
| PokemonGB_Online_Trades | https://github.com/Lorenzooone/PokemonGB_Online_Trades | implementazione in Python del protocollo di scambio Gen 1, 2 e 3 su adattatore USB o su BGB, con multiboot per il lato Gen 3; e' la dimostrazione che il lato Game Boy si collauda su emulatore | BRI, LDN |
| PkSploit | https://github.com/binarycounter/PkSploit | esecuzione di codice su Gen 1 da un Arduino che si finge un Game Boy sul cavo, con dump della ROM e lettura e scrittura della SRAM in circa 192 byte di payload; licenza MIT | BRI |
| Phasip/PokemonLinkHack | https://github.com/Phasip/PokemonLinkHack | variante indipendente della stessa tecnica di esecuzione di codice dal cavo | BRI |
| pokerom-trader | https://github.com/savaughn/pokerom-trader | scambio fra due file di salvataggio Gen 1 e Gen 2 su PC, in C con la libreria PKSav, con ricalcolo dei checksum | BRI |
| arduino-poke-gen2 | https://github.com/stevenchaulk/arduino-poke-gen2 | protocollo seriale Gen 2 su microcontrollore, riferimento per l'opzione D di ADR-008 | BRI |
| MrCheeze/pokestadium-ace | https://github.com/MrCheeze/pokestadium-ace | esecuzione di codice arbitrario su Pokemon Stadium, prior art sulle tecniche | BRI |
| Goppier/GEN3PokemonDistributions | https://github.com/Goppier/GEN3PokemonDistributions | dati di distribuzione Gen 3 dell'autore del primo ponte fra Gen 2 e Gen 3 | BRI |
| PKHeX | https://github.com/kwsch/PKHeX | riferimento di fatto sul formato di salvataggio di tutte le generazioni e sulle regole di legalita' | TUTTI |
| PKHeX web | https://pkhex-web.github.io/ | la stessa cosa nel browser, comoda per un'ispezione rapida senza installare | SME, 3DS |
| PKSav | https://github.com/ncorgan/pksav | libreria C per leggere e scrivere salvataggi Gen 1, 2 e 3, base di pokerom-trader; archiviata in sola lettura dal 2023, quindi da leggere e non da cui dipendere | BRI, SME |
| HexManiacAdvance | https://github.com/haven1433/HexManiacAdvance | editor esadecimale con le mappe dei dati delle ROM GBA | BRI, SME |
| rgen3 | https://github.com/crumblingstatue/rgen3 | libreria e utilita' Rust per i salvataggi Gen 3, inclusa la codifica delle stringhe | BRI, SME |
| ads04r/Gen3Save | https://github.com/ads04r/Gen3Save | parser Python di un salvataggio Gen 3 | BRI, SME |
| aarant/gen3tools | https://github.com/aarant/gen3tools | strutture dati Python ed editor grafico per Gen 3 | BRI, SME |
| RNGReporter | https://github.com/Admiral-Fish/RNGReporter | analisi del generatore pseudocasuale | BRI |
| Gen3-WCTool | https://github.com/projectpokemon/Gen3-WCTool | strumenti per le Wonder Card e gli eventi Gen 3 | BRI |
| gba-link-connection | https://github.com/afska/gba-link-connection | libreria per la comunicazione seriale via cavo Link su GBA | BRI |
| gba-link-cable-rom-sender | https://github.com/FIX94/gba-link-cable-rom-sender | invio di un programma multiboot alla GBA da GameCube o Wii | BRI |
| usb-gba-multiboot | https://github.com/tangrs/usb-gba-multiboot | invio di un programma multiboot da un PC via USB, alternativa senza GameCube | BRI |
| BGB | https://bgb.bircd.org/ | emulatore Game Boy con cavo Link esposto su TCP e protocollo documentato, cioe' il banco di collaudo del lato Game Boy | BRI |
| mGBA | https://mgba.io/ | emulatore con supporto multiplayer locale, seconda via per il collaudo del lato Game Boy | BRI |
| FlashGBX | https://github.com/lesserkuma/FlashGBX | lettura e scrittura di cartucce e salvataggi con il lettore GBxCart RW | SME, BRI |
| Checkpoint | https://github.com/BernardoGiordano/Checkpoint | gestore di backup dei salvataggi per 3DS e Switch, quello installato su questa console | 3DS |
| MSET9 | https://github.com/hacks-guide/MSET9/releases/latest | exploit di ingresso usato per l'installazione del custom firmware | 3DS |
| Luma3DS | https://wiki.hacks.guide/wiki/3DS:Luma3DS | firmware personalizzato installato sulla console | 3DS |
| SEEDconv | https://github.com/d0k3/SEEDconv/releases | conversione dei seed; produce materiale console-unico da trattare come segreto | 3DS |
| Azahar | https://azahar-emu.org/ | emulatore 3DS, per la verifica dei dump fuori dalla console | 3DS |
| kinnay/LDN | https://github.com/kinnay/LDN | documentazione del protocollo di rete locale della Switch | LDN |
| tornadus/frlg-ldn-trade | https://github.com/tornadus/frlg-ldn-trade | scambio fra Rosso Fuoco e Verde Foglia su Switch e un PC via LDN | LDN |
| ldn_mitm | https://github.com/spacemeowx2/ldn_mitm | sysmodule che intercetta il servizio di rete locale della Switch e lo espone come rete LAN | LDN |
| ryu_ldn_nx | https://github.com/Ethiquema/ryu_ldn_nx | evoluzione dello stesso approccio, con macchina a stati del servizio e tunneling dei socket | LDN |
| awesome-gbadev | https://github.com/gbadev-org/awesome-gbadev | elenco curato di risorse per lo sviluppo GBA | BRI |
| awesome-gbdev | https://github.com/gbdev/awesome-gbdev | l'equivalente per il Game Boy, punto di ingresso a strumenti e documentazione | BRI |

## Livello 4: articoli, blog e ricerca applicata

Ottimi per capire il ragionamento e il contesto, non citabili per un offset.

| Fonte | URL | Che cosa spiega | Track |
|---|---|---|---|
| Dev log di Poke Transporter GB | https://www.austinthomasweber.com/poke-transporter-gb | dieci articoli sul processo di reverse engineering e sulle scelte implementative del ponte | BRI |
| GBPlay, emulare uno scambio | https://blog.gbplay.io/2021/05/11/Emulating-a-Pokemon-Trade-with-Generated-Link-Cable-Data.html | negoziazione dei ruoli, selezione della modalita' e sequenza dello scambio Gen 1 | BRI |
| nitwhiz, falsificare uno scambio | https://blog.nitwhiz.dev/posts/002-pokemon-red-trade/ | i tre blocchi dello scambio e il preambolo 0xFD; da leggere sapendo che sulle dimensioni non concorda con il disassemblato | BRI |
| vaguilar, ACE in Pokemon Rosso | https://vaguilar.com/2015/05/26/arbitrary-code-execution-in-pokemon-red/ | come una lista di specie senza terminatore porta all'esecuzione di codice, con indirizzi concreti | BRI |
| vaguilar, Mew su hardware reale | https://vaguilar.com/2026/02/18/how-i-obtained-mew-in-pokemon-red-on-a-real-game-boy/ | la stessa tecnica portata a termine su console vera con un microcontrollore | BRI |
| Hackaday, il ponte impossibile | https://hackaday.com/2021/12/07/bridging-game-worlds-with-the-impossible-pokemon-trade/ | il circuito stampato di Goppier con microcontrollore ARM fra i due cavi | BRI |
| RetroReversing, Game Boy | https://www.retroreversing.com/gameboy | hub di risorse di reverse engineering per Game Boy | BRI |
| RetroReversing, GBA | https://www.retroreversing.com/gba | hub di risorse di reverse engineering per Game Boy Advance | BRI, SME |
| RetroReversing, Rosso e Blu | https://www.retroreversing.com/pokemonredblue | raccolta di strumenti e materiali su Gen 1 | BRI |
| Ryujinx, introduzione a LDN3 | https://blog.ryujinx.org/introducing-ldn3/ | come l'emulatore e le console modificate sono arrivati a parlarsi sulla stessa rete | LDN |
| Helix Chamber | https://helixchamber.com/2019/02/16/what-dreams-may-come/ | materiale di prototipazione di Gen 1, contesto storico sui dati interni | BRI |
| Reverse engineering di FireRed | https://betterprogramming.pub/low-level-explorations-reverse-engineering-pokemon-firered-through-rom-hacking-54edfb4426 | racconto didattico di un primo approccio al ROM hacking su Gen 3 | BRI, LDN |
| Guida al trading locale su Switch | https://www.dtgre.com/2026/03/fire-red-leafgreen-switch-local-wireless-guide.html | come funziona lo scambio locale nella versione Switch di Rosso Fuoco e Verde Foglia | LDN |

## Canali e video

Chiedere esplicitamente di battere questo terreno e' stata una buona idea, perche' alcuni di questi canali sono l'unica documentazione esistente di certe tecniche: gli autori pubblicano in video cio' che non hanno mai scritto. Il limite e' l'ovvio, e va tenuto presente: un video non e' citabile per un offset, non e' diffabile, e nessuno di questi e' stato guardato in questa sessione, perche' YouTube restituisce agli strumenti automatici una pagina di consenso invece del contenuto. Cio' che ne emerge va verificato e poi scritto nel documento tecnico.

| Canale o video | URL | Perche' conta | Track |
|---|---|---|---|
| Goppier | https://www.youtube.com/@Goppier | primo a realizzare il ponte fra Gen 2 e Gen 3, con documentazione sulle due versioni del cavo Link | BRI |
| Goppier, aggiornamento di sviluppo | https://www.youtube.com/watch?v=Qcp4vxyaUJc | stato di avanzamento del suo ponte hardware | BRI |
| Lorenzooone | https://www.youtube.com/@Lorenzooone | autore di Pokemon-Gen3-to-Gen-X e di PokemonGB_Online_Trades | BRI |
| im a blisy | https://www.youtube.com/c/imablisy | contributi comunitari citati dal progetto di riferimento | BRI |
| RETIRE | https://www.youtube.com/@RETIREglitch | ricerca sui glitch di Gen 1 e 2 | BRI |
| TheZZAZZGlitch | https://www.youtube.com/@TheZZAZZGlitch | primo a rendere affidabile l'esecuzione di codice arbitrario in Gen 1 e 2, dal 2013 | BRI |
| Retro Game Mechanics Explained | https://www.youtube.com/@RGMechEx | spiegazioni al livello del bit di meccaniche interne di console e giochi | BRI, TUTTI |
| Displaced Gamers | https://www.youtube.com/channel/UCWoSKWs8h6lFdiEDAjuIfpA | la serie Behind the Code, analisi del codice originale dei giochi classici | BRI, TUTTI |
| Poke Transporter GB, dimostrazione | https://www.youtube.com/watch?v=47A6p2hH2gU | il ponte di riferimento in funzione | BRI |
| Poke Transporter GB, sviluppo | https://www.youtube.com/watch?v=9mSkGhEYBkg | racconto del processo di sviluppo da parte dell'autore | BRI |
| Dissezione di un salvataggio di Rosso | https://www.youtube.com/watch?v=VVbRe7wr3G4 | lettura guidata di un salvataggio Gen 1 byte per byte | BRI |
| Cavo Link negli emulatori | https://www.youtube.com/watch?v=jzLISDGrOWo | come si collega il cavo fra due istanze di emulatore, cioe' il banco di collaudo | BRI |
| Scambio locale su Switch in FRLG | https://www.youtube.com/watch?v=epCf87MTLnk | la funzione di scambio locale nella versione Switch, dal lato utente | LDN |
| Sostituzione della batteria di cartuccia | https://www.youtube.com/watch?v=vz05ZT63Jqc | come si cambia la batteria tampone senza perdere il salvataggio | SME |
| Checkpoint su 3DS | https://www.youtube.com/watch?v=aZMVFBRp1xI | uso del gestore di backup dei salvataggi installato su questa console | 3DS |

## Livello 5: forum e community

Rispondono a domande che non hanno una risposta scritta altrove. Una risposta in un thread non e' una fonte finche' non e' verificata, e i thread su Reddit elencati qui non sono stati letti perche' il dominio non e' raggiungibile dagli strumenti di questa sessione.

| Luogo | URL | Ambito | Track |
|---|---|---|---|
| PRET, Discord | https://discordapp.com/invite/vdTW48Q | disassemblati e decompilazioni dei giochi | BRI, SME |
| Glitch City Research Institute, Discord | https://discord.com/invite/EA7jxJ6 | glitch ed esecuzione di codice in Gen 1 e 2 | BRI |
| GBAdev, Discord | https://discord.gg/ctGSNxRkg2 | sviluppo homebrew GBA e toolchain | BRI |
| Hex Maniac Advance, Discord | https://discord.com/invite/x9eQuBg | editing di ROM GBA | BRI, SME |
| Project Pokemon, protocollo Link Gen 1 | https://projectpokemon.org/home/forums/topic/58858-generation-1-link-protocol/ | discussione tecnica sul protocollo seriale | BRI |
| Project Pokemon, salvataggio Smeraldo corrotto | https://projectpokemon.org/home/forums/topic/61118-pok%C3%A9mon-emerald-gba-corrupt-save-file/ | casi reali di corruzione e tentativi di recupero | SME |
| Project Pokemon, oggetti nella tasca sbagliata | https://projectpokemon.org/home/forums/topic/64794-pokemon-emerald-items-are-in-the-right-bag-using-the-app-but-when-i-load-it-into-a-cartridge-they-go-in-the-wrong-slots/ | sintomo vicino a quello del track Smeraldo, con la discussione delle cause | SME |
| PokeCommunity, problema grave dello zaino in Smeraldo | https://www.pokecommunity.com/showthread.php?p=8992088 | discussione su uno zaino corrotto da codici trucco | SME |
| GBAtemp, salvataggio Smeraldo non scrivibile | https://gbatemp.net/threads/save-failed-on-real-pokemon-emerald.645336/ | fallimenti di scrittura su cartuccia originale | SME |
| GBAtemp, scrittura su cartuccia senza batteria | https://gbatemp.net/threads/gba-unlicensed-batteryless-sram-cart-pokemon-emerald-save-writing-issues.681601/ | perche' una scrittura riuscita a video puo' non restare | SME |
| GBAtemp, LDN3 su console modificata | https://gbatemp.net/threads/ryujinx-adds-ldn3-feature-allowing-emulator-users-to-play-online-with-cfw-switch-consoles.622169/ | esperienze di campo sul ponte fra emulatore e console | LDN |
| GBAtemp, scambio senza fili su Gen 1 e 2 | https://gbatemp.net/threads/mission-wireless-trading-on-gen1-and-gen2-pokemon-games.632492/ | tentativi comunitari di sostituire il cavo | BRI |
| insideGadgets | https://shop.insidegadgets.com/product/gbxcart-rw/ | il produttore del lettore usato dal track Smeraldo, con la documentazione del prodotto | SME, BRI |
| reddit r/Gameboy | https://www.reddit.com/r/Gameboy/ | hardware, riparazioni, lettori di cartucce; non leggibile automaticamente | SME, BRI |
| reddit r/3dshacks | https://www.reddit.com/r/3dshacks/ | modding del 3DS e problemi di installazione; non leggibile automaticamente | 3DS |
| reddit r/PokemonROMhacks | https://www.reddit.com/r/PokemonROMhacks/ | ROM hacking e strumenti su Gen 3; non leggibile automaticamente | BRI, SME |
| reddit r/pokemonrng | https://www.reddit.com/r/pokemonrng/ | generatore pseudocasuale, valore di personalita' e legalita'; non leggibile automaticamente | BRI |

## Fonti operative dei track su hardware fisico

Queste erano gia' citate dentro i rispettivi handoff e le riporto qui nella parte che ha valore durevole, cioe' guide e strumenti. La coda di discussioni, pagine di codici trucco e thread di assistenza resta negli handoff, dove ha il contesto che la rende comprensibile.

| Fonte | URL | Ambito | Track |
|---|---|---|---|
| 3ds.hacks.guide | https://3ds.hacks.guide/ | procedura canonica di modding del 3DS, incluse le pagine su MSET9 e sull'uso di GodMode9 | 3DS |
| 3ds.hacks.guide, dump | https://3ds.hacks.guide/dumping-titles-and-game-cartridges.html | dump di titoli e cartucce dalla console | 3DS |
| Manuale di GBxCart RW | https://www.gbxcart.com/wp-content/uploads/2019/10/GBxCart-RW-Manual-Rev43.pdf | procedura d'uso del lettore, revisione 43 | SME, BRI |
| Driver CH340 | https://www.wch-ic.com/downloads/CH341SER_EXE.html | driver seriale necessario al lettore su Windows | SME |
| Chiusura di Pokemon Bank | https://www.nintendolife.com/news/2026/08/pokemon-bank-is-shutting-down-in-february-2027 | vincolo temporale esterno che tocca le decisioni di trasferimento | 3DS |

## Cosa non entra in questo registro

Non entrano le fonti che documentano come ottenere materiale coperto dal perimetro dichiarato in `.claude/rules/hardware-and-perimeter.md`, ne' i salvataggi di terze parti, e non entra nulla che contenga o distribuisca materiale di chiave console-unica. Non entrano le pagine effimere, cioe' thread di assistenza e discussioni che valgono per una singola sessione: quelle restano nell'handoff del track che le ha usate. Non entrano i mirror di ROM, che non servono a nessuno degli obiettivi di questo progetto, dato che si lavora su cartucce possedute. E non entrano le pagine di codici trucco, che sono la causa piu' probabile del problema che il track Smeraldo deve risolvere e non la sua soluzione.
