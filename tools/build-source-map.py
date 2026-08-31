#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la mappa relazionale delle fonti come note collegate, leggibili in Obsidian.

Perché esiste
--------------
`SOURCES.md` è un registro: dice che una fonte esiste, a cosa serve e a quale
sottoprogetto. Non dice perché è stata salvata, né come si lega alle altre, e una
tabella non produce un grafo. Questo strumento genera una nota per fonte sotto
`docs/fonti/`, ciascuna con un abstract, il motivo per cui è in archivio, il punto
esatto del progetto che serve, e le relazioni verso le altre fonti. Aprendo la radice
del repository come vault Obsidian, quelle relazioni diventano il grafo.

La scelta di generarle invece di scriverle a mano segue lo stesso principio delle
tabelle caratteri: i dati stanno in un posto solo, la forma è uniforme, e una modifica
alla struttura si applica a tutte le note insieme.

Uso
---
    python tools/build-source-map.py
    python tools/build-source-map.py --check     verifica senza scrivere
"""

import argparse
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "fonti")

# Vocabolario delle relazioni, tenuto piccolo perché un grafo con venti tipi di arco
# non si legge. Ogni arco dice cosa una fonte fa a un'altra.
RELAZIONI = {
    "conferma": "conferma in modo indipendente",
    "corregge": "corregge un'affermazione di",
    "deriva-da": "è derivato o discende da",
    "usa": "usa come dipendenza o base",
    "documenta": "documenta il funzionamento di",
    "alternativa-a": "è un'alternativa a",
}

# slug, nome, url, livello, letto, track, abstract, perché, serve_a, relazioni
FONTI = [
    ("pokered", "pret/pokered", "https://github.com/pret/pokered", 1, True, ["BRI"],
     "Disassemblaggio completo di Pokemon Rosso e Blu che ricompila in una ROM identica all'originale. Contiene le macro delle strutture dati, la mappa della memoria di lavoro, le costanti del protocollo seriale e il codice del Centro Scambi.",
     "È la definizione autorevole del formato di generazione 1: dove una fonte secondaria e questo repository divergono, ha ragione questo.",
     [("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezioni 2 e 3, struttura e salvataggio Gen 1"),
      ("[[08-cavo-link]]", "costanti del protocollo e dimensione del blocco di scambio"),
      ("[[09-esecuzione-codice]]", "la primitiva del terminatore mancante")],
     [("corregge", "bulbapedia")]),

    ("pokecrystal", "pret/pokecrystal", "https://github.com/pret/pokecrystal", 1, True, ["BRI"],
     "Disassemblaggio di Pokemon Cristallo. Oltre alle strutture di generazione 2 contiene la routine di calcolo delle statistiche, la tabella dei caratteri e le due strutture di invio sul cavo, quella nativa e quella del Time Capsule.",
     "Da qui vengono l'ordine dei nibble dei DV e la derivazione del quinto DV, scritti come commento nel sorgente, e la scoperta che la conversione fra formati Gen 1 e Gen 2 esiste già dentro il gioco.",
     [("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezione 4, struttura Gen 2"),
      ("[[06-identita-pokemon]]", "DV e loro derivazione"),
      ("[[08-cavo-link]]", "strutture di invio native e Time Capsule")],
     [("corregge", "bulbapedia")]),

    ("pokeemerald", "pret/pokeemerald", "https://github.com/pret/pokeemerald", 1, True, ["BRI", "SME"],
     "Decompilazione di Pokemon Smeraldo in C e assembly ARM che ricompila in una ROM identica. Contiene la struttura cifrata del Pokemon, il calcolo del checksum, la mappa dei settori del salvataggio, la chiave di cifratura e la maschera sulle quantità degli oggetti.",
     "È la fonte di tutto il lato generazione 3 e l'unica su cui il checksum è verificabile: la sua formula per parole da 16 bit corregge una fonte secondaria che lo descriveva byte per byte, errore che distrugge un Pokemon.",
     [("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezioni 5 e 6, struttura cifrata e salvataggio"),
      ("[[04-cifratura-gen3]]", "cifratura, permutazione e checksum"),
      ("[[03-integrita-checksum]]", "checksum di settore"),
      ("[[22-strumenti]]", "offset e chiave usati dallo strumento di diagnosi")],
     [("corregge", "bulbapedia")]),

    ("pokefirered", "pret/pokefirered", "https://github.com/pret/pokefirered", 1, True, ["BRI", "LDN", "SME"],
     "Decompilazione di Rosso Fuoco e Verde Foglia. Struttura del salvataggio diversa da quella di Smeraldo in ogni offset che conta: chiave di cifratura, conteggio della squadra, denaro e tasche dello zaino.",
     "Ha corretto un errore nel nostro strumento: la chiave sta a 0xF20 dentro un blocco che misura 0xF24, non a 0x0AF8 come riportava la fonte secondaria. Serve anche al track LDN, perché quelli sono i giochi dello scambio con la Switch.",
     [("[[22-strumenti]]", "offset e capienze delle tasche per quel gioco"),
      ("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezione 6, differenze fra i giochi Gen 3")],
     [("corregge", "bulbapedia")]),

    ("pokeruby", "pret/pokeruby", "https://github.com/pret/pokeruby", 1, True, ["BRI", "SME"],
     "Decompilazione di Rubino e Zaffiro. Non ha alcuna chiave di cifratura, quindi le quantità degli oggetti sono in chiaro, ed è l'unico dei tre giochi Gen 3 a comportarsi così.",
     "Serve come controprova: conferma tutti gli offset che il nostro strumento usava per Rubino e Zaffiro, e la sua assenza di maschera è ciò che rende necessario identificare il gioco prima di leggere lo zaino.",
     [("[[22-strumenti]]", "il candidato senza maschera nel rilevamento del gioco")],
     []),

    ("pandocs", "Pan Docs, trasferimento seriale", "https://gbdev.io/pandocs/Serial_Data_Transfer_(Link_Cable).html", 1, True, ["BRI"],
     "Riferimento tecnico dell'hardware seriale del Game Boy: i registri SB e SC con i loro bit, le frequenze del clock interno, e il comportamento del clock esterno, che il gioco accetta a qualunque velocità fino a 500 kHz e anche a intervalli irregolari.",
     "Da qui viene il fatto che sblocca l'opzione D: chi fornisce il clock decide quando, quindi un microcontrollore può fermarsi a pensare fra un bit e l'altro senza rompere nulla. Blocca il crawler e si scarica con curl locale.",
     [("[[08-cavo-link]]", "sezione sull'hardware sotto il protocollo"),
      ("[[30-opzioni-implementative]]", "costo reale dell'opzione D")],
     [("conferma", "cable-link")]),

    ("gbatek", "GBATEK, multiboot", "https://problemkaputt.de/gbatek-bios-multi-boot-single-game-pak.htm", 1, True, ["BRI"],
     "Specifica del multiboot del Game Boy Advance: la stretta di mano con 0x6200 e la risposta 0x0000, le dimensioni ammesse del programma, gli indirizzi di destinazione in memoria di lavoro, la cifratura del trasferimento e i vincoli di temporizzazione.",
     "È ciò che va implementato se si scegliesse di costruire il ponte da zero, e dice quanto spazio si ha davvero: al massimo circa 256 kilobyte, con gli indirizzi assoluti riferiti alla memoria di lavoro e non alla cartuccia.",
     [("[[10-multiboot-hardware]]", "la procedura di multiboot")],
     []),

    ("copetti", "Copetti, architettura del GBA", "https://www.copetti.org/writings/consoles/game-boy-advance/", 1, True, ["BRI"],
     "Descrizione architetturale del Game Boy Advance: le due memorie di lavoro con le loro dimensioni e velocità, il bus della cartuccia, il buffer di prefetch e il meccanismo della retrocompatibilità con il Game Boy.",
     "Spiega perché un programma multiboot vive nella memoria esterna, che è fino a sei volte più lenta, e quindi perché i progetti di questo tipo curano la compressione dei dati.",
     [("[[10-multiboot-hardware]]", "la memoria in cui vive il programma")],
     []),

    ("devlog-ptgb", "Dev log di Poke Transporter GB", "https://www.austinthomasweber.com/poke-transporter-gb", 4, True, ["BRI"],
     "Serie di undici articoli in cui l'autore del ponte di riferimento racconta il proprio processo, dall'architettura della console al formato di salvataggio, dal protocollo del cavo alla scoperta dell'exploit, fino all'iniezione dell'evento e alla gestione della grafica.",
     "È la fonte più ricca sul nostro problema perché il codice dice cosa fa e questi articoli dicono perché. Da qui vengono la specifica esatta dell'exploit e la scoperta che il Pokemon entra in Gen 3 tramite un evento Dono Segreto.",
     [("[[09-esecuzione-codice]]", "specifica dell'innesco e il lato che scrive"),
      ("[[10-multiboot-hardware]]", "il lato che scrive"),
      ("[[08-cavo-link]]", "voltaggi e temporizzazione del clock")],
     [("documenta", "ptgb")]),

    ("ptgb", "Poke Transporter GB", "https://github.com/Striaton-Lab-Team/Poke_Transporter_GB", 3, True, ["BRI"],
     "Il ponte di riferimento: homebrew per Game Boy Advance in multiboot che trasferisce Pokemon da Gen 1 e 2 a Gen 3 usando il cavo del Game Boy Color, sotto licenza MIT. Contiene un generatore di payload con assemblatore Z80 proprio e tabelle di valori di ROM per lingua.",
     "È la prova che il ponte è possibile, ed è il repertorio delle soluzioni. Il suo codice ha rivelato ciò che il README non dichiara, cioè che il payload viaggia sul cavo al posto della squadra.",
     [("[[09-esecuzione-codice]]", "che cosa ci fa il ponte"),
      ("[[30-opzioni-implementative]]", "opzione A")],
     [("usa", "pccs")]),

    ("pccs", "PCCS", "https://github.com/Striaton-Lab-Team/Pokemon-Community-Conversion-Standard", 3, True, ["BRI"],
     "Libreria C++ che definisce come convertire un Pokemon da Gen 1 e 2 a Gen 3. Il README documenta quattro metodi campo per campo; il codice della release corrente implementa il comportamento di uno solo.",
     "È la specifica di riferimento della conversione, e il suo codice contiene il campionamento con rifiuto del valore di personalità e l'uso dell'ID segreto per la lucentezza, che confermano una deduzione fatta prima di leggerlo.",
     [("[[07-conversione-vincoli]]", "solutore di vincoli e ruolo dell'ID segreto"),
      ("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezione 9, ciò che va inventato")],
     []),

    ("gen3togenx", "Pokemon-Gen3-to-Gen-X", "https://github.com/Lorenzooone/Pokemon-Gen3-to-Gen-X", 3, True, ["BRI"],
     "Homebrew per Game Boy Advance che scambia Pokemon fra Gen 3 e Gen 1 e 2 usando il protocollo normale e non exploit, con in più la gestione dell'orologio interno di Rubino, Zaffiro e Smeraldo.",
     "È l'alternativa architetturale al ponte di riferimento: dimostra che si può fare senza esecuzione di codice, al prezzo di non replicare l'esperienza dello scambio.",
     [("[[08-cavo-link]]", "le due strategie per il ponte"),
      ("[[30-opzioni-implementative]]", "confronto fra le strade")],
     [("alternativa-a", "ptgb")]),

    ("pokemongb-online", "PokemonGB_Online_Trades", "https://github.com/Lorenzooone/PokemonGB_Online_Trades", 3, True, ["BRI"],
     "Implementazione in Python del protocollo di scambio di Gen 1, 2 e 3, funzionante sia su un adattatore USB per il cavo sia sull'emulatore BGB, con multiboot per il lato Gen 3.",
     "È la dimostrazione che il lato Game Boy si collauda su emulatore, e quindi che una parte del protocollo si sviluppa senza hardware.",
     [("[[21-collaudo]]", "il secondo livello di collaudo")],
     []),

    ("cable-link", "CableClub/cable-link", "https://github.com/CableClub/cable-link", 3, True, ["BRI"],
     "Circuito stampato in formato KiCad, con gerber pronti alla produzione, e firmware per Raspberry Pi Pico che parla il protocollo di scambio di generazione 1. Apache 2.0, del 2021.",
     "È il precedente più avanzato per l'opzione D, e vale come conferma indipendente: le sue costanti del protocollo coincidono una per una con quelle che avevamo ricavato dal disassemblato, e apre la porta seriale esattamente al mezzo megahertz che Pan Docs dichiara come massimo.",
     [("[[08-cavo-link]]", "la conferma indipendente delle costanti"),
      ("[[30-opzioni-implementative]]", "opzione D, che non parte da zero")],
     [("conferma", "pokered")]),

    ("pksploit", "PkSploit", "https://github.com/binarycounter/PkSploit", 3, True, ["BRI", "SME"],
     "Suite che dumpa ROM e salvataggio e riscrive il salvataggio di qualunque cartuccia Game Boy e Game Boy Color, usando come vettore una cartuccia di generazione 1, un cavo Link e un microcontrollore compatibile Arduino.",
     "Se l'affermazione regge alla prova, un microcontrollore sostituisce il lettore di cartucce per tutto ciò che è Game Boy, e questo tocca sia il ponte sia il modo di procurarsi i dump. L'autore avverte che è in sviluppo pesante.",
     [("[[09-esecuzione-codice]]", "il precedente minimale"),
      ("[[30-opzioni-implementative]]", "opzione D senza lettore")],
     [("deriva-da", "cableclubhack")]),

    ("cableclubhack", "vaguilar/pokemon-red-cable-club-hack", "https://github.com/vaguilar/pokemon-red-cable-club-hack", 3, True, ["BRI"],
     "Implementazione originale dell'exploit del Centro Scambi con Arduino e Python. Documenta il cablaggio dei pin, cioè uscita seriale sul pin 6, ingresso sul 3, clock sul 2 e massa, e contiene il payload in un array dentro un'intestazione Arduino.",
     "È la base di PkSploit e la fonte del cablaggio, che nessun'altra fonte scriveva. Contiene anche un'implementazione del protocollo dell'emulatore BGB sulla porta 8765, che è il banco di collaudo che ci serve.",
     [("[[09-esecuzione-codice]]", "il vettore dal cavo"),
      ("[[21-collaudo]]", "il protocollo di BGB e la sua porta")],
     []),

    ("linkhack", "Phasip/PokemonLinkHack", "https://github.com/Phasip/PokemonLinkHack", 3, True, ["BRI"],
     "Catena di exploit che dal buffer overflow del cavo arriva a installare programmi persistenti dentro il deposito Pokemon: un selettore nel primo slot e i programmi nei successivi, sopravvivendo ai riavvii grazie al salvataggio della cartuccia.",
     "È la strategia opposta a quella del ponte, che usa un payload transitorio. Se un giorno servisse un lanciatore stabile dentro la cartuccia, questa è la strada, e il suo costo dichiarato è rinunciare all'uso normale dell'asilo.",
     [("[[09-esecuzione-codice]]", "vie alternative e persistenza")],
     [("deriva-da", "cableclubhack")]),

    ("blog-phasip", "Blog di Phasip", "https://www.sn1.se/posts/pokemon/", 4, True, ["BRI"],
     "Racconto della catena di exploit con i numeri: 198 byte di payload utile, i programmi che risiedono negli slot del deposito, e il limite dichiarato che fuori dal buffer si possono scrivere solo nomi di Pokemon predefiniti.",
     "Dà la misura del payload e il vincolo che determina la forma della catena, cioè che il primo salto deve passare per dati che il gioco recupera dalla tabella dei nomi.",
     [("[[09-esecuzione-codice]]", "dimensione del payload e vincoli")],
     [("documenta", "linkhack")]),

    ("arduino-poke-gen2", "arduino-poke-gen2", "https://github.com/stevenchaulk/arduino-poke-gen2", 3, True, ["BRI"],
     "Adattamento a generazione 2 di una macchina a stati Arduino per lo scambio, provato su Cristallo, con schema di cablaggio incluso.",
     "Porta un fatto architetturale che semplifica il firmware: in generazione 2 non serve memorizzare nulla, perché rimandando indietro i byte ricevuti si ottiene la copia della squadra.",
     [("[[30-opzioni-implementative]]", "opzione D, il caso più semplice")],
     [("deriva-da", "arduino-boy")]),

    ("arduino-boy", "pepijndevos/arduino-boy", "https://github.com/pepijndevos/arduino-boy", 3, True, ["BRI"],
     "Deposito Pokemon su Arduino per i giochi di generazione 1: memorizza un Pokemon nella memoria non volatile della scheda e lo scambia con la console. Il codice del protocollo deriva a sua volta da un progetto precedente chiamato gameboy-spoof.",
     "È l'origine della famiglia di implementazioni Arduino del protocollo, quindi il capostipite da leggere per capire da dove viene il codice degli altri.",
     [("[[30-opzioni-implementative]]", "opzione D, genealogia delle implementazioni")],
     []),

    ("gba-link-connection", "gba-link-connection", "https://github.com/afska/gba-link-connection", 3, True, ["BRI"],
     "Libreria C++ per il porto seriale del Game Boy Advance, con moduli separati per la modalità multiplayer, l'invio di multiboot ad altre console, l'adattatore wireless, il protocollo Joybus verso Wii e GameCube, le carte e-Reader e il Mobile Adapter GB.",
     "Il modulo che conta per noi collega la console a un PC o a un Raspberry Pi usando il cavo del Game Boy Color: è l'infrastruttura pronta per l'opzione D dal lato Game Boy Advance.",
     [("[[10-multiboot-hardware]]", "vie per il multiboot"),
      ("[[30-opzioni-implementative]]", "opzione D e opzione C")],
     []),

    ("reon", "Progetto REON", "https://github.com/REONTeam", 3, True, ["BRI"],
     "Ricostruzione dell'infrastruttura di rete del Mobile Adapter GB, l'accessorio che dava funzioni online ai giochi Game Boy. Comprende una libreria del protocollo in C, un server, un emulatore per BGB, un adattatore su Arduino e una utilità dedicata allo scambio nel Trade Corner.",
     "È un secondo canale storico oltre al cavo, e la sua utilità per il Trade Corner riguarda direttamente lo scambio di Pokemon. Da valutare se apra una strada alternativa al cavo per il lato generazione 2.",
     [("[[08-cavo-link]]", "canali alternativi al cavo")],
     []),

    ("gen3distributions", "Goppier/GEN3PokemonDistributions", "https://github.com/Goppier/GEN3PokemonDistributions", 3, True, ["BRI"],
     "Raccolta di cartucce di distribuzione per eventi di generazione 3, con la procedura operativa per usarle fra due console.",
     "Dà il dettaglio che al progetto mancava sul multiboot dal lato dell'utente: la console ricevente si accende tenendo premuti start e select finché il logo Nintendo scompare, con il lato master del cavo nella console che invia.",
     [("[[10-multiboot-hardware]]", "procedura utente del multiboot")],
     []),

    ("stadium-ace", "MrCheeze/pokestadium-ace", "https://github.com/MrCheeze/pokestadium-ace", 3, True, ["BRI"],
     "Esecuzione di codice arbitrario su Pokemon Stadium per Nintendo 64, che passa dal sistema di scambio e presuppone di avere già il controllo su un gioco di generazione 1. Documenta gli indirizzi dove i box vengono convertiti dal formato Gen 1 al formato Stadium.",
     "È il terzo esempio documentato di conversione fra formati Pokemon fatta da software ufficiale, dopo il Time Capsule e il Pal Park, e quindi materiale di studio su come gli autori originali risolvevano il problema.",
     [("[[08-cavo-link]]", "precedenti di conversione fra formati")],
     []),

    ("usb-gba-multiboot", "usb-gba-multiboot", "https://github.com/tangrs/usb-gba-multiboot", 3, True, ["BRI"],
     "Firmware per microcontrollore Teensy e software su PC per caricare un programma nella console via USB, sfruttando il multiboot.",
     "È la via al multiboot che non richiede né GameCube né flashcart, e motiva la scelta della modalità seriale normale perché è a 32 bit e riceve mentre invia.",
     [("[[10-multiboot-hardware]]", "vie per il multiboot")],
     [("alternativa-a", "rom-sender")]),

    ("rom-sender", "gba-link-cable-rom-sender", "https://github.com/FIX94/gba-link-cable-rom-sender", 3, True, ["BRI"],
     "Homebrew per GameCube e Wii che invia un programma multiboot alla console collegata, leggendo i file da una cartella sulla scheda di memoria.",
     "È la via al multiboot che il progetto di riferimento consiglia per prima, e quella che evita lo scambio a caldo della cartuccia se si ha una console adatta.",
     [("[[10-multiboot-hardware]]", "vie per il multiboot")],
     []),

    ("kinnay-ldn", "kinnay, protocollo LDN", "https://github.com/kinnay/NintendoClients/wiki/LDN-Protocol", 1, True, ["LDN"],
     "Specifica del protocollo di rete locale della Nintendo Switch: action frame proprietario trasmesso ogni cento millisecondi, canali radio usati, struttura dell'annuncio campo per campo, tre livelli di cifratura con la derivazione delle chiavi, e sequenza di connessione con assegnazione degli indirizzi.",
     "È la sola specifica completa del protocollo su cui il track dello scambio con la Switch si basa, e spiega perché servano le chiavi della console: senza quelle non si derivano le chiavi di sessione.",
     [("[[04-cifratura-gen3]]", "i dati scambiati sono strutture Gen 3")],
     []),

    ("frlg-ldn-trade", "frlg-ldn-trade", "https://github.com/unlimitedcoder2/frlg-ldn-trade", 3, True, ["LDN"],
     "Proof of concept che fa scambiare Pokemon a un PC con Rosso Fuoco e Verde Foglia in esecuzione su Switch o Switch 2, simulando un giocatore che si collega come capo sessione. Richiede Linux, Python 3.12 o successivo, le chiavi della console, almeno due strutture .pk3 e un gioco portato avanti fino allo sbloccio della sala degli scambi. Licenza AGPLv3.",
     "È il punto di partenza del track, e la sua tabella di compatibilità delle schede Wi-Fi è ciò che decide se il track sia praticabile su una macchina data: affidabili la ALFA AWUS036ACHM con driver mt76x0u e la Realtek RTL8821CE con rtw88_8821ce, inaffidabile la AMD RZ616 con mt7921e, e dichiaratamente problematiche la Intel AX200 con iwlwifi e l Atheros AR9271 con ath9k_htc, entrambe incapaci di ricevere un indirizzo. Il repository dichiara anche che la decompilazione pret/pokefirered comprende il port per Switch, e che il progetto e nato per dimostrare la possibilità di uno scambio non ufficiale.",
     [("[[06-identita-pokemon]]", "i formati .pk3 e .ek3 sono strutture Gen 3"),
      ("[[11-wireless-locale-e-ponte-switch]]", "requisiti hardware e procedura di scambio")],
     [("usa", "kinnay-ldn")]),

    ("ldnd", "unlimitedcoder2/ldnd", "https://github.com/unlimitedcoder2/ldnd", 1, True, ["LDN"],
     "Demone in C, licenza GPL-2.0, che porta lo stack wireless di Linux su Windows: collega il kernel Linux come libreria statica tramite LKL dentro un eseguibile costruito con MinGW, riceve l adattatore USB attraverso WinUSB e gli fa caricare i driver e i file di linux-firmware. Espone il servizio su una pipe con nome, e la sua riga di comando passa parametri di modulo del kernel fra cui rtw88_usb.switch_usb_mode=0.",
     "Ribalta il vincolo di piattaforma che il progetto dava per assodato, perché rende il track eseguibile su Windows e quindi compatibile con il track dello Smeraldo sulla stessa macchina. Ha anche una compatibilità hardware diversa dalla via Linux, verificata sul campo, perché scavalca il gestore di rete e il driver di sistema; in cambio funziona soltanto con adattatori USB e, dopo la riassegnazione a WinUSB, il dispositivo non funziona più come scheda di rete ordinaria.",
     [("[[11-wireless-locale-e-ponte-switch]]", "la via Windows, e il conflitto fra modalità USB 2 e USB 3")],
     [("alternativa-a", "kinnay-ldn")]),

    ("pmr-discord", "Pokemon Multiplayer Research, canali di supporto", "https://discord.gg/nBnTrv3UMn", 4, True, ["LDN", "BRI"],
     "Server della community che sviluppa lo scambio via rete locale sui giochi di generazione 3 su Switch. I canali di supporto e generale contengono la casistica reale degli adattatori wireless, i sintomi dei guasti con le loro cause, e le dichiarazioni degli autori sui limiti del progetto.",
     "È la sola fonte che dice che cosa funziona davvero e perché, e ha corretto tre cose che il progetto dava per certe: che il chip degli adattatori della famiglia AC600 provati con successo e un RTL8821CU servito dal driver in albero e non un RTL8811AU, che il Wireless Adapter del Game Boy Advance non è 802.11 e va quindi emulato con un microcontrollore, e che l emulatore sulla console riproduce quel dispositivo ma non il cavo Link. Contiene inoltre il vincolo del Pokedex nazionale sul giocatore simulato, e la fotografia di una catena funzionante fra Game Boy Advance e Switch.",
     [("[[11-wireless-locale-e-ponte-switch]]", "tutta la nota"),
      ("[[30-opzioni-implementative]]", "conferma indipendente dell opzione D")],
     [("conferma", "frlg-ldn-trade"), ("documenta", "ldnd")]),

    ("ldn-mitm", "ldn_mitm", "https://github.com/spacemeowx2/ldn_mitm", 3, True, ["LDN"],
     "Modulo di sistema per Switch che sostituisce il servizio di rete locale ed emula la scansione delle console vicine usando la rete locale via UDP.",
     "È l'approccio opposto a quello del proof of concept: invece di parlare il protocollo radio, lo sostituisce con traffico di rete. Utile come piano alternativo se la scheda Wi-Fi non supportasse la modalità monitor.",
     [("[[06-identita-pokemon]]", "contesto del track LDN")],
     [("usa", "switch-lan-play")]),

    ("switch-lan-play", "switch-lan-play", "https://github.com/spacemeowx2/switch-lan-play", 3, True, ["LDN"],
     "Client e server che intercettano il traffico di rete della console con libpcap e lo incapsulano in un protocollo minimale, per far credere alle console di essere sulla stessa rete locale.",
     "È la controparte del modulo di sistema, e insieme formano l'alternativa che non richiede hardware radio particolare. Licenza GPL 3.",
     [("[[06-identita-pokemon]]", "contesto del track LDN")],
     []),

    ("bulbapedia", "Bulbapedia, pagine sui formati", "https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_III)", 2, True, ["BRI", "SME", "LDN"],
     "Insieme di pagine enciclopediche sui formati dei dati e dei salvataggi delle tre generazioni, sui valori individuali, sul valore di personalità, sulla codifica dei caratteri e sugli indici di specie.",
     "È il punto di partenza per orientarsi e la mappa di dove guardare nel disassemblato, ma su cinque punti verificati si è rivelata sbagliata: cifre di Gen 1, maiuscole di Gen 3, checksum di Gen 3, dimensione del blocco di scambio e chiave di Rosso Fuoco.",
     [("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "tutte le sezioni, come punto di partenza"),
      ("[[23-prove-eseguite]]", "il caso studio sull'affidabilità delle fonti")],
     []),

    ("gcri-discord", "Glitch City Research Institute, canali", "https://discord.com/invite/EA7jxJ6", 4, True, ["BRI"],
     "Server della community che studia i difetti sfruttabili dei giochi Pokemon. I canali per generazione contengono il lavoro corrente, che il wiki recepisce con ritardo o non recepisce affatto.",
     "Ha portato al progetto tutto cio che sa sull esecuzione di codice in generazione 3, che prima non copriva: il ruolo dei byte 0xFC e 0xFD come codice di controllo e sostituzione di variabile nel motore di stampa del testo, la differenza fra Rubino e Zaffiro, dove quei codici passano da una tabella di puntatori senza controllo dei limiti, e le altre tre versioni, dove passano da un costrutto di scelta multipla che rende inerte un indice fuori intervallo, e la catena completa che parte da una posta difettosa. Dal lato generazione 2 ha portato il vincolo per cui un identificativo dell allenatore contenente il byte 0xFF impedisce il traboccamento della squadra, perché introduce un terminatore dove non era previsto.",
     [("[[09-esecuzione-codice]]", "il lato generazione 3, e il vincolo sul traboccamento"),
      ("[[05-testo-e-charmap]]", "i byte di controllo non sono caratteri")],
     [("conferma", "pokeemerald"), ("documenta", "glitchcity")]),

    ("glitchcity", "Glitch City Wiki", "https://glitchcity.wiki", 2, True, ["BRI"],
     "Catalogo della ricerca sui glitch dei giochi di generazione 1 e 2, compresi i metodi di esecuzione di codice raggiungibili giocando e quelli che passano dal cavo.",
     "Serve a orientarsi nel campo e a valutare alternative, ma sul vettore che ci interessa rimanda a fonti esterne. Respinge il recupero automatico e si legge dal mirror statico.",
     [("[[09-esecuzione-codice]]", "vie dal lato del giocatore")],
     []),

    ("pokemon-automation", "Pokemon Automation", "https://pokemonautomation.github.io/", 3, True, ["AUT", "LDN"],
     "Progetto che automatizza le parti ripetitive dei giochi Pokemon su Nintendo Switch con oltre cento programmi. È un anello di controllo chiuso su un sistema che non espone stato: percepisce il fotogramma video e in alcuni titoli l'audio, attua tramite un controller emulato da un microcontrollore, e decide con un programma per compito. Il perimetro dichiarato è console non modificate e nessun accesso alla memoria.",
     "È la fonte fondante del quinto sottoprogetto, che nasce come studio, e la lettura del 2026-08-26 ha prodotto due risultati oltre l'atteso: il perimetro del progetto è compatibile con le regole di questo, e fra i titoli automatizzati compaiono Rosso Fuoco e Verde Foglia su Switch, che è il gioco al centro del track dello scambio con la Switch. La visione artificiale resta una capacità che il progetto non ha in nessun altro track.",
     [("[[30-opzioni-implementative]]", "sovrapposizione di esperienza sul microcontrollore, che è l'opzione D")],
     []),

    ("gambatte-gamelink", "Gambatte con GameLink su TCP", "https://gbatemp.net/threads/mission-wireless-trading-on-gen1-and-gen2-pokemon-games.632492/", 5, True, ["BRI"],
     "Discussione in cui un membro compila una versione di Gambatte con il collegamento seriale del Game Boy emulato su TCP, funzionante sia come client sia come server, e riferisce di aver scambiato e combattuto nei giochi di generazione 1 e 2 fra dispositivi diversi, Switch compreso.",
     "È la seconda via di collaudo del protocollo oltre a BGB, e ha due vantaggi: non è specifica dei Pokemon perché emula un cavo seriale generico, ed esiste come nucleo libretro, quindi si presta a essere pilotata senza interfaccia grafica.",
     [("[[21-collaudo]]", "il secondo livello di collaudo")],
     [("alternativa-a", "cableclubhack")]),

    ("gbatemp-vc-save", "GBAtemp, correzione dei salvataggi in Virtual Console", "https://gbatemp.net/threads/tutorial-fix-all-save-problems-for-pokemon-games-vc-gba.433266/", 4, True, ["3DS"],
     "Tutorial del 2016 che corregge l impossibilità di salvare nei giochi Pokemon per Game Boy Advance iniettati come Virtual Console su Nintendo 3DS, tramite modifica esadecimale della ROM, e in una seconda parte rimuove il messaggio di salvataggio corrotto con offset specifici per versione e lingua.",
     "Va registrata per quello che è e non per quello che si sperava: riguarda l emulazione su console e non le cartucce fisiche, quindi non serve al sottoprogetto dello Smeraldo per cui era stata cercata, e serve invece al track 3DS se un giorno si iniettassero ROM proprie. Il thread stesso ne mostra i limiti, perché la sequenza di byte dichiarata universale non esiste in Rubino e Zaffiro americani, e per Rosso Fuoco e Verde Foglia gli offset della seconda parte non sono mai stati trovati.",
     [("[[01-fondamenta-salvataggio]]", "che cosa cambia quando il supporto e emulato")],
     []),

    ("projectpokemon", "Project Pokemon, discussioni", "https://projectpokemon.org/home/forums/topic/64794-pokemon-emerald-items-are-in-the-right-bag-using-the-app-but-when-i-load-it-into-a-cartridge-they-go-in-the-wrong-slots/", 5, True, ["SME", "BRI"],
     "Tre discussioni lette: una su un dispositivo che fa da sorgente di clock per il protocollo e ha completato scambi via internet, una su un salvataggio assente invece che corrotto su cartuccia contraffatta, e una su un editor che ha identificato male il gioco facendo finire gli oggetti negli slot sbagliati.",
     "La terza ha prodotto codice: il rilevamento automatico del gioco nel nostro strumento di diagnosi nasce da là. La prima ha rivelato l'esistenza di CableClub.",
     [("[[22-strumenti]]", "perché lo strumento non si fida del parametro")],
     [("documenta", "cable-link")]),

    ("pokeyellow", "pret/pokeyellow", "https://github.com/pret/pokeyellow", 1, True, ["BRI"],
     "Disassemblaggio di Pokemon Giallo, clonato e confrontato campo per campo con quello di Rosso e Blu.",
     "Il confronto ha stabilito che la macro della struttura di box e le costanti di lunghezza sono identiche a quelle di Rosso e Blu, dunque il lettore di generazione 1 copre Giallo senza alcuna modifica. È un risultato negativo, e per questo vale registrarlo: ha eliminato una variante di codice che si sarebbe scritta per precauzione.",
     [("[[12-analisi-quantitativa]]", "i risultati negativi come categoria di risultato")],
     []),

    ("pokegold", "pret/pokegold", "https://github.com/pret/pokegold", 1, True, ["BRI"],
     "Disassemblaggio di Pokemon Oro e Argento, clonato e confrontato con quello di Cristallo.",
     "La macro della struttura di squadra è identica a quella di Cristallo, dunque il lettore di generazione 2 copre Oro e Argento senza modifiche; restano diversi soltanto gli offset del salvataggio, che erano già registrati. Secondo risultato negativo utile, con la stessa funzione del primo.",
     [("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezione 4, e la nota sugli offset per gioco")],
     []),

    ("video-goppier", "Goppier, i due video sul primo ponte", "https://www.youtube.com/watch?v=Qcp4vxyaUJc", 4, True, ["BRI"],
     "Le due sole testimonianze esistenti sul primo ponte fra generazioni: l'aggiornamento di sviluppo, trascritto e letto per intero, e il video precedente che presenta il dispositivo, privo di sottotitoli di qualunque tipo e quindi ancora da trascrivere.",
     "Il primo dei due è la fonte più densa dell'intero quarto livello, e documenta sette circostanze che nessuna altra fonte riporta, fra cui il vincolo di sincronizzazione fra i due protocolli, che è il problema architetturale del ponte, e l'affermazione che una ROM per Game Boy Advance possa dialogare direttamente con i giochi di generazione 2. Il secondo è registrato come il più importante degli arretrati, perché il successivo vi si riferisce più volte.",
     [("[[08-cavo-link]]", "il vincolo di sincronizzazione fra i due lati"),
      ("[[30-opzioni-implementative]]", "il ponte di Goppier e la prova che sposterebbe il confronto")],
     []),

    ("video-trascritti", "Quattro video trascritti su formati, cavo e strumenti", "https://www.youtube.com/watch?v=VVbRe7wr3G4", 4, True, ["BRI", "SME", "3DS", "LDN"],
     "Voce aggregata su quattro video trascritti e letti per intero: la dissezione di un salvataggio di Rosso, il cavo Link negli emulatori, lo scambio locale su Switch in Rosso Fuoco, e due dimostrazioni dello strumento di trasferimento di riferimento. La trascrizione è avvenuta con lo strumento a riga di comando che scarica i sottotitoli automatici, ripuliti dal programma del progetto perché i sottotitoli a scorrimento ripetono ogni riga.",
     "Il bilancio di questa lettura è controintuitivo e vale registrarlo: due dei sei video trascritti sono, su punti specifici, la migliore fonte che il progetto possieda, mentre uno non ha prodotto nulla. Il limite del formato resta quello noto, cioè che un video non è citabile per un offset e non è confrontabile riga per riga, dunque ciò che affermano va verificato sul sorgente prima di entrare in codice.",
     [("[[21-collaudo]]", "il secondo livello di collaudo su emulatore"),
      ("[[24-fonti-di-community]]", "la via di recupero dei sottotitoli")],
     []),

    ("gbatemp-smeraldo", "GBAtemp, due discussioni sulla scrittura del salvataggio", "https://gbatemp.net/threads/save-failed-on-real-pokemon-emerald.645336/", 5, True, ["SME"],
     "Voce aggregata su due discussioni lette dalle schermate consegnate dall'utente, perché il dominio respinge il recupero automatico. La prima riguarda il messaggio di salvataggio fallito su cartuccia genuina, la seconda la scrittura di un salvataggio da centoventotto kibibyte su una cartuccia di riproduzione la cui memoria è di sessantaquattro.",
     "La prima è la discussione più importante per il caso di studio dello Smeraldo: stabilisce che su cartuccia genuina quel messaggio indica una memoria di salvataggio che sta cedendo, perché la schermata compare quando vengono rilevati blocchi difettosi, e che la risposta corretta è produrre il dump immediatamente finché il salvataggio si carica ancora. La seconda contiene una diagnosi indipendente che coincide con il controllo che il nostro strumento compie in una riga, cioè l'assenza della firma attesa nel dump.",
     [("[[01-fondamenta-salvataggio]]", "perché il backup non è negoziabile"),
      ("[[22-strumenti]]", "il controllo della firma e quello della dimensione")],
     []),

    ("retroreversing", "RetroReversing, Game Boy", "https://www.retroreversing.com/gameboy", 4, True, ["BRI"],
     "Raccolta di risorse di reverse engineering sulla piattaforma, letta per individuare strumenti e documentazione che il progetto non conosceva.",
     "Da qui provengono lo strumento che identifica la toolchain con cui una ROM è stata compilata, il progetto sugli stati di salvataggio su hardware originale, gli schemi elettrici ricreati dalla comunità, e il protocollo della stampante con i suoi byte di riconoscimento.",
     [("[[08-cavo-link]]", "altri protocolli sul medesimo collegamento seriale")],
     []),

    ("hackaday-ponte", "Hackaday, il ponte impossibile", "https://hackaday.com/2021/12/07/bridging-game-worlds-with-the-impossible-pokemon-trade/", 4, True, ["BRI"],
     "Articolo divulgativo sul primo ponte fra generazioni, letto per estrarne la descrizione dell'hardware.",
     "Descrive il dispositivo come un circuito stampato semplice con le porte per i due tipi di cavo e un microcontrollore ARM interposto che traduce le strutture, e dichiara di non pubblicare né schemi né sorgenti. È la sola descrizione scritta di quell'hardware, e la sua incompletezza è la ragione per cui la trascrizione del video resta necessaria.",
     [("[[30-opzioni-implementative]]", "il ponte di Goppier per come lo racconta lui")],
     []),

    ("pokerom-trader", "pokerom-trader", "https://github.com/savaughn/pokerom-trader", 3, True, ["BRI"],
     "Strumento che esegue uno scambio fra due file di salvataggio delle prime due generazioni su calcolatore, scritto in C con una libreria di manipolazione dei salvataggi e un'interfaccia grafica propria, con ricalcolo dei checksum e regole di evoluzione da scambio.",
     "È il precedente più prossimo all'opzione che opera interamente su calcolatore, e la sua esistenza dimostra che quella strada arriva a un risultato funzionante; mostra anche che l'evoluzione da scambio, che il nostro progetto non ha ancora considerato, è una regola che un convertitore deve conoscere.",
     [("[[30-opzioni-implementative]]", "l'opzione che opera su file di salvataggio")],
     []),

    ("video-distribuzioni", "Goppier, la ricreazione delle distribuzioni Gen 3", "https://www.youtube.com/watch?v=NKBb-YS34wg", 4, True, ["EVT", "BRI"],
     "Racconto tecnico della ricreazione di tutte le distribuzioni di eventi di terza generazione, inglesi, giapponesi e da GameCube, trascritto e letto per intero il 2026-08-28. Descrive come si trova il multiboot dentro la ROM di distribuzione confrontando i byte che passano sul cavo, come lo si decomprime attraverso la chiamata di sistema del BIOS, come si aggira il checksum additivo che ne difende l'integrità, e come si impostano i parametri dell'esemplare riusando il codice del gioco per indice di parametro.",
     "È la sola fonte esistente sul formato interno di una ROM di distribuzione, e porta due contributi che il progetto non aveva. Il primo è la conferma indipendente, ottenuta per reverse engineering e non dal disassemblato, che il salvataggio di terza generazione ha quattordici sezioni che ruotano fra gli slot e due copie alternate, con la posta nella sezione quattro. Il secondo è la disciplina con cui tratta i casi indeterminati: dei tre non chiusi dichiara l'ipotesi e la sua improbabilità invece di promuoverla a fatto, e su uno chiude la questione per ricerca esaustiva sui 65536 semi possibili, trovando l'unico compatibile.",
     [("[[03-integrita-checksum]]", "il checksum additivo come difesa dalla corruzione e non da un avversario"),
      ("[[10-multiboot-hardware]]", "il multiboot come canale ufficiale delle distribuzioni"),
      ("[[06-identita-pokemon]]", "il valore di personalità visto dal lato di chi genera")],
     [("conferma", "pokeemerald"),
      ("documenta", "gen3distributions")]),

    ("video-ereader-eventi", "im a blisy, gli eventi e-Reader su cartuccia vera", "https://www.youtube.com/watch?v=fK-Actf6kME", 4, True, ["EVT", "SME"],
     "Guida esaustiva alle vie con cui un evento entra in una cartuccia originale, trascritta e letta per intero il 2026-08-28: l'emulatore con due istanze collegate e il BIOS reale, l'e-Reader con un salvataggio precostituito, la scheda riprogrammabile, la stampa delle carte con il codice a punti, e l'iniezione diretta della carta meraviglia nel salvataggio estratto.",
     "È la fonte operativa del track delle distribuzioni, e porta l'avvertimento che questo progetto adotta come regola: se il salvataggio contiene già una carta meraviglia, quella va esportata prima di ogni scrittura, perché può essere un evento non ancora preservato dalla comunità. Distingue inoltre due funzioni del gioco che si somigliano e non coincidono, cioè il Dono Segreto e l'Evento Mistero, e documenta che in Smeraldo la seconda è stata rimossa dai menu e si riapre soltanto attraverso la prima. Cita GBxCart RW fra i lettori raccomandati, che è una conferma indipendente della scelta fatta per il caso dello Smeraldo.",
     [("[[01-fondamenta-salvataggio]]", "il ciclo di estrazione e ripristino di un salvataggio"),
      ("[[22-strumenti]]", "i lettori di cartucce e le loro alternative")],
     [("alternativa-a", "video-distribuzioni")]),

    ("video-pcny", "Hard4Games, la macchina del Pokemon Center di New York", "https://www.youtube.com/watch?v=AVhqlol6k9o", 4, True, ["EVT"],
     "Preservazione dell'hardware e del software di distribuzione del Pokemon Center di New York, trascritta e letta per intero il 2026-08-28. Documenta i due dischi in formato proprietario di sviluppo, le schede di campagna che dichiarano quali esemplari distribuire e in quale finestra temporale, le schede che funzionano da chiave, e le date delle campagne di seconda e terza generazione.",
     "È la fonte storica su un apparecchio che si credeva distrutto, ed è quella che spiega perché gli eventi di quel negozio si possano soltanto ricreare e non riprodurre: il trasferimento avviene attraverso uno scrittore dedicato collegato al GameCube, e la fonte dichiara di aver verificato che con un Game Boy Advance ordinario non funziona. Documenta inoltre due proprietà degli esemplari distribuiti là, cioè l'allenatore originale con l'indicazione della postazione e l'identificativo dell'allenatore incrementato a ogni distribuzione, che la ricreazione per multiboot ha replicato.",
     [("[[24-fonti-di-community]]", "la conservazione come attività di ricerca")],
     [("conferma", "video-distribuzioni")]),

    ("video-gbi-bonus", "SuperrSonic, i contenuti bonus dal Game Boy Player", "https://www.youtube.com/watch?v=GBEMP2kEpPw", 4, True, ["EVT"],
     "Programma per GameCube che applica a un salvataggio di cartuccia i contenuti bonus di diversi giochi, fra cui quelli dei giochi Pokemon di terza generazione, trascritto e letto per intero il 2026-08-28. La via passa dall'interfaccia alternativa del Game Boy Player, che invia un programma multiboot senza cavo perché il collegamento è interno alla console, ed è capace di estrarre BIOS, ROM e salvataggio e di ripristinare il salvataggio modificato.",
     "Apre una strada che nessuna delle altre fonti del track nomina, perché l'intero ciclo di modifica avviene sulla console senza calcolatore e senza lettore esterno. Il contributo più utile all'obiettivo di collezione non è però un esemplare ma un oggetto: il quiz del disco bonus consegnava i biglietti degli eventi e, sul salvataggio di Smeraldo, la mappa marina che porta all'incontro con Mew, cioè oggetti irripetibili che sbloccano l'unico modo legittimo di ottenere quelle specie. L'autore dichiara di aver implementato i checksum leggendo Bulbapedia, che è la fonte su cui questo progetto ha già documentato un errore in quella materia.",
     [("[[12-analisi-quantitativa]]", "il costo di modificare un dato cifrato senza invalidarlo"),
      ("[[10-multiboot-hardware]]", "il multiboot inviato senza cavo")],
     [("alternativa-a", "video-ereader-eventi")]),

    ("bank-fine-servizio", "Nintendo, fine del servizio di Pokemon Bank", "https://en-americas-support.nintendo.com/app/answers/detail/a_id/61543", 2, True, ["EVT", "3DS"],
     "Comunicazione ufficiale del supporto Nintendo sulla chiusura di Pokemon Bank, letta il 2026-08-28: il servizio termina giovedì 25 febbraio 2027 alle 19:00 PST, cioè il 26 febbraio alle 12:00 JST, e con esso cessa la possibilità di trasferire verso Pokemon Home. Chi ha esemplari depositati deve spostarli in Home prima di quella data, e la pagina non annuncia alcun periodo di tolleranza.",
     "È il vincolo temporale esterno del track delle distribuzioni e dell'obiettivo di collezione, e va citato dalla fonte ufficiale e non dalla stampa specializzata, perché la data governa una pianificazione e non una notizia. Bank e Poke Transporter erano rimasti gli ultimi software del Nintendo 3DS con funzioni in linea dopo la chiusura generale del 9 aprile 2024.",
     [("[[11-wireless-locale-e-ponte-switch]]", "le vie che restano verso le piattaforme moderne")],
     []),

    ("bulbapedia-trasferimenti", "Bulbapedia, la catena dei trasferimenti fra generazioni", "https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Bank", 2, True, ["EVT", "3DS"],
     "Le tre pagine che descrivono la catena di trasferimento verso le piattaforme moderne, lette il 2026-08-28: Pokemon Bank con i giochi che Poke Transporter accetta come sorgente, cioè la quinta generazione e le riedizioni su Virtual Console della prima e della seconda; il Parco Amico, che porta dalla terza alla quarta generazione; e il Trasferitore, che porta dalla quarta alla quinta.",
     "Serve a stabilire un fatto che decide la praticabilità dell'obiettivo di collezione: la terza generazione non entra in Bank direttamente, quindi un esemplare nato su cartuccia Game Boy Advance deve attraversare quattro passaggi irreversibili, il primo dei quali richiede un Nintendo DS o DS Lite perché è l'unica console con lo slot per le cartucce Game Boy Advance. Da qui vengono anche i limiti di ciascun passaggio, cioè sei esemplari per volta, la stessa lingua ai due capi, il rifiuto delle uova e degli esemplari che conoscono una mossa macchina nascosta, e il Pokedex nazionale come prerequisito del secondo passaggio.",
     [("[[11-wireless-locale-e-ponte-switch]]", "la catena completa verso le piattaforme moderne")],
     [("conferma", "bank-fine-servizio")]),

    ("pkhex-eventi-gen3", "PKHeX, tabella degli eventi Gen 3 e vocabolario dei metodi", "https://github.com/kwsch/PKHeX", 3, True, ["EVT", "BRI", "SME"],
     "Le due parti di PKHeX che documentano le distribuzioni di terza generazione: la tabella `PKHeX.Core/Legality/Encounters/Data/Gen3/EncountersWC3.cs`, con centosettantasette voci ciascuna corredata del proprio metodo di generazione pseudocasuale, e l'enumerazione `PKHeX.Core/Legality/RNG/PIDType.cs`, che documenta i metodi uno per uno. La tabella vive nel codice e non in un documento perché, come dichiara il suo stesso commento, i dati di quella generazione non sono mai stati conservati in forma binaria uniforme e sono quindi scritti a mano.",
     "È la fonte che ha spostato il track dalla congettura al dato, ed è più affidabile dei video su ogni questione di offset e di metodo. La sigla BACD nomina l'ordine invertito con cui le quattro estrazioni compongono valore di personalità e valori individuali, e quell'inversione è la firma di un esemplare da evento: ne segue che ricreare un evento non è produrre i campi visibili giusti ma produrli attraverso la sequenza corretta. Conferma per via indipendente quattro affermazioni tratte dai video, nominandone i metodi, e ne chiude una che i video dichiaravano aperta, cioè la derivazione del sesso dell'allenatore di provenienza dei tre leggendari del film, che risulta uno scorrimento di quindici bit dopo l'oggetto tenuto e non la divisione congetturata. Porta infine il fatto più notevole della ricerca: nel blocco delle uova dichiara che il gioco riceve un'interruzione di sincronismo verticale fra la generazione della personalità e quella dei valori individuali, e che rimuovendola con una modifica alla ROM i medesimi script producono la correlazione ordinaria, quindi il metodo di generazione dipende da un'interruzione hardware e non soltanto dal codice.",
     [("[[06-identita-pokemon]]", "il valore di personalità visto dal lato di chi genera e di chi verifica"),
      ("[[12-analisi-quantitativa]]", "lo spazio dei semi a sedici bit e la sua esplorazione esaustiva"),
      ("[[23-prove-eseguite]]", "la prova di conformità su un esemplare autentico invece che sintetico")],
     [("corregge", "video-distribuzioni"),
      ("conferma", "video-distribuzioni")]),

    ("bulbapedia-eventi-italia", "Bulbapedia, distribuzioni italiane di eventi in Gen 3", "https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III", 2, True, ["EVT"],
     "Elenco delle distribuzioni italiane della terza generazione con luogo, date e campi di ciascun esemplare, letto il 2026-08-29. Porta la manifestazione del 2006 in un parco di divertimenti, dal ventitré al venticinque giugno, con allenatore di provenienza 10ANNI, identificativo 06227, dieci specie al livello settanta e la facoltà per il partecipante di scegliere tre esemplari, e la manifestazione del 2007 nel medesimo luogo, con un Mew di allenatore Aura e identificativo 20078.",
     "È la fonte che dà luogo e date a ciò che la tabella di PKHeX dà come campi, e serve a un fatto specifico di questo progetto: gli esemplari che l'utente possiede da quella manifestazione sono identificati con precisione, e la loro riga del catalogo diventa il vettore di prova reale che il track del ponte dichiara di non avere. La distinzione fra il nome dell'allenatore italiano e quello delle altre lingue europee, che cambia per la lunghezza consentita, conta per la catena di trasferimento, dove ogni passaggio pretende la stessa lingua ai due capi.",
     [("[[23-prove-eseguite]]", "il primo dato autentico su cui confrontare il lettore di strutture")],
     [("conferma", "pkhex-eventi-gen3")]),

    ("gen-iii-event-patcher", "gen-iii-event-patcher", "https://github.com/superguideguy/gen-iii-event-patcher", 3, True, ["EVT", "BRI"],
     "Strumento in Java che trasforma la ROM di un gioco di terza generazione in una ROM di distribuzione, e che applica uno script di evento a un salvataggio per uso personale. Letto il 2026-08-29 nella descrizione e nella struttura del sorgente, che comprende un compilatore elementare per gli script di evento e un costruttore di checksum.",
     "Documenta il secondo canale di distribuzione, che il primo studio del track confondeva con il primo: il Dono Segreto non attiva una bandiera ma scarica dentro il salvataggio uno script di un kilobyte eseguito più tardi, capace di contenere qualunque istruzione valida compresa quella che porta all'esecuzione di codice arbitrario. È il punto di convergenza più notevole della ricerca, perché è il medesimo meccanismo che il dev log dello strumento di trasferimento fra generazioni descrive dall'altro capo, scoperto in modo indipendente da due progetti con scopi opposti. Dichiara inoltre che Rubino e Zaffiro hanno il precedente Evento Mistero, che è cosa diversa, e che il trasferimento della carta meraviglia passa dall'adattatore senza fili e non dal cavo.",
     [("[[09-esecuzione-codice]]", "la sezione di script eseguibile come porta di servizio del formato"),
      ("[[10-multiboot-hardware]]", "il secondo canale, che non è il multiboot")],
     [("conferma", "devlog-ptgb")]),

    ("project-wonder", "Project Wonder, distribuzioni per applicazione di differenze", "https://github.com/Goppier/Gen3DistributionRoms", 3, True, ["EVT"],
     "Raccolta di dieci differenze da applicare a una ROM di distribuzione preservata, letta il 2026-08-29. Produce distribuzioni degli oggetti di evento, cioè i biglietti, la mappa marina e la grotta alterna, più due eventi costruiti dalla comunità e tre distribuzioni di uova che riproducono quelle dei negozi, con supporto dichiarato a sei lingue fra cui l'italiano.",
     "È la via più pronta all'uso per gli oggetti di evento, che il track considera parte dell'obiettivo di collezione tanto quanto gli esemplari, perché sbloccano gli unici incontri legittimi di alcune specie. Dichiara il proprio fabbisogno di hardware senza attenuazioni, cioè due Game Boy Advance, due adattatori senza fili e una scheda riprogrammabile, e quel fabbisogno va letto insieme a ciò che il track dello scambio con la console moderna ha stabilito, cioè che quell'adattatore è un progetto proprietario e non un dispositivo di rete ordinario.",
     [("[[10-multiboot-hardware]]", "il fabbisogno di hardware delle vie di distribuzione"),
      ("[[11-wireless-locale-e-ponte-switch]]", "l'adattatore senza fili come dispositivo proprietario")],
     [("deriva-da", "gen3distributions")]),

    ("eventsgallery", "Project Pokemon, Events Gallery", "https://github.com/projectpokemon/EventsGallery", 3, False, ["EVT"],
     "Archivio collettivo della conservazione delle informazioni sugli eventi, per tutte le generazioni. Per la terza generazione le carte meraviglia si manipolano con lo strumento dedicato che questo registro già elenca.",
     "È il luogo dove cercare il campione di un evento, ed è la controparte documentale del catalogo che questo repository genera dalla tabella di PKHeX. Non è stato aperto: è la fonte che serve per rispondere alla domanda se il progetto possa contribuire alla conservazione invece di consumarla soltanto, cioè se i campioni degli eventi dichiarati non chiusi manchino davvero.",
     [("[[24-fonti-di-community]]", "la conservazione come attività collettiva")],
     []),

    ("pp-algoritmi-eventi", "Project Pokemon, ricerca sull'algoritmo di generazione degli eventi Gen 3", "https://projectpokemon.org/home/forums/topic/39517-gen-3-event-generation-algorithm-research-10anniv-etc/", 5, True, ["EVT"],
     "Discussione sulla ricostruzione dell'algoritmo di generazione degli esemplari da evento della terza generazione, letta il 2026-08-29. Documenta che la determinazione dei metodi è avvenuta per reverse engineering a partire da campioni raccolti e non da una specifica, e riporta che il metodo di uno degli eventi dei negozi è stato risolto come variante a semi non ristretti in cui la metà alta del valore di personalità è messa in or esclusivo con la metà bassa, con l'identificativo dell'allenatore e con quello segreto.",
     "Serve a una cosa sola e va classificata per quella: dice come la conoscenza dei metodi è stata ottenuta, cioè da campioni e non da un sorgente, il che spiega perché alcuni eventi restino non chiusi e perché la richiesta pubblica di campioni sia il modo in cui quella ricerca progredisce. Sul dettaglio non è citabile e il suo contenuto va verificato sulla tabella di PKHeX, che è la forma consolidata della medesima conoscenza.",
     [("[[24-fonti-di-community]]", "una ricerca che avanza per campioni invece che per sorgente")],
     [("documenta", "pkhex-eventi-gen3")]),
]
# ---------------------------------------------------------------------------------------
# I riferimenti teorici canonici dei concetti impiegati nell'analisi quantitativa.
# Schema: (slug, autori, titolo, sede, anno, per che cosa è citato).
#
# Sono citati per attribuzione del concetto e non come fonti consultate in sessione: la
# distinzione è dichiarata nella sezione che li introduce in bibliografia, e la ragione
# per cui non stanno nella tabella FONTI è che quella tabella dichiara per ogni voce se
# sia stata letta, e mescolarvi la letteratura canonica gonfierebbe quel conteggio.
#
# I numeri di pagina non sono riportati: autore, titolo, sede ed edizione si conoscono con
# certezza, un numero di pagina non verificato in sessione sarebbe un dettaglio inventato.
# ---------------------------------------------------------------------------------------
RIFERIMENTI_TEORICI = [
    ("shannon48", "C. E. Shannon", "A Mathematical Theory of Communication",
     "Bell System Technical Journal, vol. 27, pp. 379-423 e 623-656", "1948",
     "Definizione di entropia di una sorgente discreta, di informazione mutua e di capacità di canale. È il riferimento per ogni misura in bit impiegata in questo lavoro."),

    ("shannon49", "C. E. Shannon", "Communication Theory of Secrecy Systems",
     "Bell System Technical Journal, vol. 28, n. 4, pp. 656-715", "1949",
     "Nozione di sicurezza perfetta e dimostrazione che essa richiede una chiave di entropia almeno pari a quella del messaggio. È il criterio contro cui si misura la cifratura della generazione 3."),

    ("vernam26", "G. S. Vernam", "Cipher Printing Telegraph Systems for Secret Wire and Radio Telegraphic Communications",
     "Journal of the American Institute of Electrical Engineers, vol. 45, pp. 109-115", "1926",
     "Il cifrario a somma modulo due fra messaggio e chiave, di cui la cifratura della generazione 3 è un'istanza con chiave riusata."),

    ("cover-thomas", "T. M. Cover, J. A. Thomas", "Elements of Information Theory, 2ª edizione",
     "Wiley", "2006",
     "Trattazione sistematica di entropia, entropia condizionata e informazione mutua, e della disuguaglianza di elaborazione dei dati, impiegata per stabilire che la permutazione non aggiunge incertezza dato il valore di personalità."),

    ("katz-lindell", "J. Katz, Y. Lindell", "Introduction to Modern Cryptography, 3ª edizione",
     "CRC Press", "2020",
     "Enunciato e dimostrazione moderna del teorema sulla sicurezza perfetta, e trattazione dell'attacco per sovrapposizione su una chiave riusata."),

    ("peterson-brown", "W. W. Peterson, D. T. Brown", "Cyclic Codes for Error Detection",
     "Proceedings of the IRE, vol. 49, n. 1, pp. 228-235", "1961",
     "Introduzione dei codici ciclici per la rilevazione d'errore e delle loro garanzie sugli errori a raffica, che è il termine di confronto per il checksum additivo dei giochi."),

    ("lin-costello", "S. Lin, D. J. Costello", "Error Control Coding, 2ª edizione",
     "Pearson Prentice Hall", "2004",
     "Capacità di rilevazione di un codice in funzione della propria distanza minima, e limite della probabilità di errore non rilevato per un codice a sindrome corta."),

    ("rfc1071", "R. Braden, D. Borman, C. Partridge", "Computing the Internet Checksum, RFC 1071",
     "Internet Engineering Task Force", "1988",
     "La somma a complemento a uno con ripiegamento del riporto, cioè la tecnica che la generazione 3 impiega per ridurre a sedici bit una somma calcolata a trentadue."),

    ("rfc1662", "W. Simpson (a cura di)", "PPP in HDLC-like Framing, RFC 1662",
     "Internet Engineering Task Force", "1994",
     "La trasparenza a byte, cioè il byte stuffing con sequenza di fuga, di cui la lista di correzione del cavo Link è l'alternativa a lunghezza fissa."),

    ("rfc3927", "S. Cheshire, B. Aboba, E. Guttman", "Dynamic Configuration of IPv4 Link-Local Addresses, RFC 3927",
     "Internet Engineering Task Force", "2005",
     "Definizione del blocco di indirizzi link-local 169.254.0.0/16 e della sua autoconfigurazione, impiegato dal protocollo di rete locale della console."),

    ("tanenbaum", "A. S. Tanenbaum, D. J. Wetherall", "Computer Networks, 5ª edizione",
     "Prentice Hall", "2011",
     "Delimitazione di trama e trasparenza dei dati, rilevazione d'errore a livello di collegamento, e assegnazione dei canali nelle reti locali senza filo."),

    ("proakis", "J. G. Proakis, M. Salehi", "Digital Communications, 5ª edizione",
     "McGraw-Hill", "2008",
     "Modello del canale, occupazione di banda e relazione fra velocità di simbolo e larghezza spettrale, impiegati nel calcolo della non sovrapposizione dei canali."),

    ("gray-neuhoff", "R. M. Gray, D. L. Neuhoff", "Quantization",
     "IEEE Transactions on Information Theory, vol. 44, n. 6, pp. 2325-2383", "1998",
     "Teoria della quantizzazione scalare, quantizzatori non uniformi e saturazione, che è la forma esatta della conversione dell'allenamento fra le generazioni."),

    ("feller", "W. Feller", "An Introduction to Probability Theory and Its Applications, vol. 1, 3ª edizione",
     "Wiley", "1968",
     "Distribuzione geometrica con il proprio valore atteso e la propria varianza, e approssimazione di Poisson della binomiale, impiegate per il campionamento con rifiuto e per il conteggio delle occorrenze del byte riservato."),

    ("vonneumann51", "J. von Neumann", "Various Techniques Used in Connection with Random Digits",
     "National Bureau of Standards, Applied Mathematics Series, vol. 12", "1951",
     "Formulazione originale del metodo di campionamento con rifiuto, che è l'algoritmo con cui l'implementazione di riferimento genera il valore di personalità."),

    ("devroye", "L. Devroye", "Non-Uniform Random Variate Generation",
     "Springer-Verlag", "1986",
     "Trattazione sistematica del campionamento con rifiuto, compreso il costo atteso in funzione della probabilità di accettazione."),

    ("knuth2", "D. E. Knuth", "The Art of Computer Programming, vol. 2: Seminumerical Algorithms, 3ª edizione",
     "Addison-Wesley", "1997",
     "Aritmetica modulare e teorema cinese del resto, impiegato per stabilire l'indipendenza fra vincoli che agiscono su moduli coprimi."),

    ("knuth3", "D. E. Knuth", "The Art of Computer Programming, vol. 3: Sorting and Searching, 2ª edizione",
     "Addison-Wesley", "1998",
     "Rappresentazione delle permutazioni mediante tavole di inversione e sistema numerico fattoriale, che è la struttura della tabella di permutazione delle sottostrutture."),

    ("ieee80211", "IEEE", "IEEE Standard 802.11: Wireless LAN Medium Access Control and Physical Layer Specifications",
     "Institute of Electrical and Electronics Engineers", "2020",
     "Struttura dei frame di gestione e di azione, piano dei canali nella banda a 2,4 GHz e occupazione di banda delle portanti, su cui il protocollo di rete locale della console è costruito."),
]



def nota(slug, nome, url, livello, letto, track, abstract, perche, serve_a, relazioni):
    righe = []
    righe.append("---")
    righe.append("tipo: fonte")
    righe.append("livello: %d" % livello)
    righe.append("letto: %s" % ("si" if letto else "no"))
    righe.append("track: [%s]" % ", ".join(track))
    righe.append("url: %s" % url)
    righe.append("tags: [fonte, livello-%d]" % livello)
    if relazioni:
        for tipo, altro in relazioni:
            righe.append("%s: \"[[%s]]\"" % (tipo, altro))
    righe.append("---")
    righe.append("")
    righe.append("# %s" % nome)
    righe.append("")
    righe.append("%s" % url)
    righe.append("")
    righe.append("## Abstract")
    righe.append("")
    righe.append(abstract)
    righe.append("")
    righe.append("## Perché è in archivio")
    righe.append("")
    righe.append(perche)
    righe.append("")
    righe.append("## A quale punto del progetto serve")
    righe.append("")
    for dove, cosa in serve_a:
        righe.append("- %s, %s" % (dove, cosa))
    righe.append("")
    if relazioni:
        righe.append("## Relazioni con altre fonti")
        righe.append("")
        for tipo, altro in relazioni:
            righe.append("- %s [[%s]]" % (RELAZIONI[tipo], altro))
        righe.append("")
    righe.append("## Contesto")
    righe.append("")
    righe.append("Livello %d di affidabilità secondo la gerarchia di [[SOURCES]]. Track serviti: %s. La mappa di tutte le fonti e delle loro relazioni è [[index-fonti]]."
                 % (livello, ", ".join(track)))
    righe.append("")
    return "\n".join(righe)


def hub():
    righe = []
    righe.append("---")
    righe.append("tipo: mappa")
    righe.append("tags: [fonti, mappa, indice]")
    righe.append("up: \"[[index]]\"")
    righe.append("---")
    righe.append("")
    righe.append("# Mappa delle fonti")
    righe.append("")
    righe.append("Questa cartella contiene una nota per ciascuna fonte che porta peso tecnico, con il suo abstract, il motivo per cui è in archivio, il punto esatto del progetto che serve e le relazioni verso le altre fonti. Il registro completo, comprese le voci minori e quelle non lette, resta [[SOURCES]]: questa mappa non lo sostituisce, lo rende navigabile.")
    righe.append("")
    righe.append("Le note sono generate da `tools/build-source-map.py` a partire da una tabella unica, per la stessa ragione per cui le tabelle caratteri sono generate: i dati stanno in un posto solo e la forma resta uniforme. Modificare una nota a mano significa perderla alla rigenerazione successiva; si modifica la tabella.")
    righe.append("")
    righe.append("Aprendo la radice del repository come vault Obsidian, le relazioni dichiarate nel frontmatter e i collegamenti nel corpo diventano il grafo. Il diagramma qui sotto ne mostra la struttura portante per chi legge il file senza Obsidian.")
    righe.append("")
    righe.append("```mermaid")
    righe.append("graph LR")
    for slug, nome, _u, livello, _l, _t, _a, _p, _s, rel in FONTI:
        for tipo, altro in rel:
            righe.append("  %s -- %s --> %s" % (slug, tipo, altro))
    righe.append("```")
    righe.append("")
    righe.append("## Le fonti, per livello")
    righe.append("")
    for lv in (1, 2, 3, 4, 5):
        gruppo = [f for f in FONTI if f[3] == lv]
        if not gruppo:
            continue
        righe.append("### Livello %d" % lv)
        righe.append("")
        righe.append("| Fonte | Track | Serve a |")
        righe.append("|---|---|---|")
        for slug, nome, _u, _lv, _l, track, _a, _p, serve_a, _r in gruppo:
            dove = ", ".join(d for d, _c in serve_a)
            righe.append("| [[%s]] | %s | %s |" % (slug, ", ".join(track), dove))
        righe.append("")
    return "\n".join(righe)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="verifica senza scrivere")
    args = ap.parse_args()

    slugs = [f[0] for f in FONTI]
    problemi = []
    if len(slugs) != len(set(slugs)):
        problemi.append("slug duplicati")
    for slug, _n, _u, _lv, _l, _t, _a, _p, _s, rel in FONTI:
        for tipo, altro in rel:
            if tipo not in RELAZIONI:
                problemi.append("%s: relazione sconosciuta %r" % (slug, tipo))
            if altro not in slugs:
                problemi.append("%s: relazione verso uno slug inesistente %r" % (slug, altro))
    if problemi:
        for p in problemi:
            print("PROBLEMA: " + p, file=sys.stderr)
        return 1

    if args.check:
        print("%d fonti, %d relazioni, nessun problema" %
              (len(FONTI), sum(len(f[9]) for f in FONTI)))
        return 0

    os.makedirs(OUT, exist_ok=True)
    for f in FONTI:
        path = os.path.join(OUT, "%s.md" % f[0])
        with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(nota(*f))
    with io.open(os.path.join(OUT, "index-fonti.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(hub())
    print("scritte %d note più la mappa in %s" % (len(FONTI), OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
