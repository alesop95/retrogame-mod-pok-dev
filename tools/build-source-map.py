#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la mappa relazionale delle fonti come note collegate, leggibili in Obsidian.

Perche' esiste
--------------
`SOURCES.md` e' un registro: dice che una fonte esiste, a cosa serve e a quale
sottoprogetto. Non dice perche' e' stata salvata, ne' come si lega alle altre, e una
tabella non produce un grafo. Questo strumento genera una nota per fonte sotto
`docs/fonti/`, ciascuna con un abstract, il motivo per cui e' in archivio, il punto
esatto del progetto che serve, e le relazioni verso le altre fonti. Aprendo la radice
del repository come vault Obsidian, quelle relazioni diventano il grafo.

La scelta di generarle invece di scriverle a mano segue lo stesso principio delle
tabelle caratteri: i dati stanno in un posto solo, la forma e' uniforme, e una modifica
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

# Vocabolario delle relazioni, tenuto piccolo perche' un grafo con venti tipi di arco
# non si legge. Ogni arco dice cosa una fonte fa a un'altra.
RELAZIONI = {
    "conferma": "conferma in modo indipendente",
    "corregge": "corregge un'affermazione di",
    "deriva-da": "e' derivato o discende da",
    "usa": "usa come dipendenza o base",
    "documenta": "documenta il funzionamento di",
    "alternativa-a": "e' un'alternativa a",
}

# slug, nome, url, livello, letto, track, abstract, perche', serve_a, relazioni
FONTI = [
    ("pokered", "pret/pokered", "https://github.com/pret/pokered", 1, True, ["BRI"],
     "Disassemblaggio completo di Pokemon Rosso e Blu che ricompila in una ROM identica all'originale. Contiene le macro delle strutture dati, la mappa della memoria di lavoro, le costanti del protocollo seriale e il codice del Centro Scambi.",
     "E' la definizione autorevole del formato di generazione 1: dove una fonte secondaria e questo repository divergono, ha ragione questo.",
     [("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezioni 2 e 3, struttura e salvataggio Gen 1"),
      ("[[08-cavo-link]]", "costanti del protocollo e dimensione del blocco di scambio"),
      ("[[09-esecuzione-codice]]", "la primitiva del terminatore mancante")],
     [("corregge", "bulbapedia")]),

    ("pokecrystal", "pret/pokecrystal", "https://github.com/pret/pokecrystal", 1, True, ["BRI"],
     "Disassemblaggio di Pokemon Cristallo. Oltre alle strutture di generazione 2 contiene la routine di calcolo delle statistiche, la tabella dei caratteri e le due strutture di invio sul cavo, quella nativa e quella del Time Capsule.",
     "Da qui vengono l'ordine dei nibble dei DV e la derivazione del quinto DV, scritti come commento nel sorgente, e la scoperta che la conversione fra formati Gen 1 e Gen 2 esiste gia' dentro il gioco.",
     [("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezione 4, struttura Gen 2"),
      ("[[06-identita-pokemon]]", "DV e loro derivazione"),
      ("[[08-cavo-link]]", "strutture di invio native e Time Capsule")],
     [("corregge", "bulbapedia")]),

    ("pokeemerald", "pret/pokeemerald", "https://github.com/pret/pokeemerald", 1, True, ["BRI", "SME"],
     "Decompilazione di Pokemon Smeraldo in C e assembly ARM che ricompila in una ROM identica. Contiene la struttura cifrata del Pokemon, il calcolo del checksum, la mappa dei settori del salvataggio, la chiave di cifratura e la maschera sulle quantita' degli oggetti.",
     "E' la fonte di tutto il lato generazione 3 e l'unica su cui il checksum e' verificabile: la sua formula per parole da 16 bit corregge una fonte secondaria che lo descriveva byte per byte, errore che distrugge un Pokemon.",
     [("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezioni 5 e 6, struttura cifrata e salvataggio"),
      ("[[04-cifratura-gen3]]", "cifratura, permutazione e checksum"),
      ("[[03-integrita-checksum]]", "checksum di settore"),
      ("[[22-strumenti]]", "offset e chiave usati dallo strumento di diagnosi")],
     [("corregge", "bulbapedia")]),

    ("pokefirered", "pret/pokefirered", "https://github.com/pret/pokefirered", 1, True, ["BRI", "LDN", "SME"],
     "Decompilazione di Rosso Fuoco e Verde Foglia. Struttura del salvataggio diversa da quella di Smeraldo in ogni offset che conta: chiave di cifratura, conteggio della squadra, denaro e tasche dello zaino.",
     "Ha corretto un errore nel nostro strumento: la chiave sta a 0xF20 dentro un blocco che misura 0xF24, non a 0x0AF8 come riportava la fonte secondaria. Serve anche al track LDN, perche' quelli sono i giochi dello scambio con la Switch.",
     [("[[22-strumenti]]", "offset e capienze delle tasche per quel gioco"),
      ("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezione 6, differenze fra i giochi Gen 3")],
     [("corregge", "bulbapedia")]),

    ("pokeruby", "pret/pokeruby", "https://github.com/pret/pokeruby", 1, True, ["BRI", "SME"],
     "Decompilazione di Rubino e Zaffiro. Non ha alcuna chiave di cifratura, quindi le quantita' degli oggetti sono in chiaro, ed e' l'unico dei tre giochi Gen 3 a comportarsi cosi'.",
     "Serve come controprova: conferma tutti gli offset che il nostro strumento usava per Rubino e Zaffiro, e la sua assenza di maschera e' cio' che rende necessario identificare il gioco prima di leggere lo zaino.",
     [("[[22-strumenti]]", "il candidato senza maschera nel rilevamento del gioco")],
     []),

    ("pandocs", "Pan Docs, trasferimento seriale", "https://gbdev.io/pandocs/Serial_Data_Transfer_(Link_Cable).html", 1, True, ["BRI"],
     "Riferimento tecnico dell'hardware seriale del Game Boy: i registri SB e SC con i loro bit, le frequenze del clock interno, e il comportamento del clock esterno, che il gioco accetta a qualunque velocita' fino a 500 kHz e anche a intervalli irregolari.",
     "Da qui viene il fatto che sblocca l'opzione D: chi fornisce il clock decide quando, quindi un microcontrollore puo' fermarsi a pensare fra un bit e l'altro senza rompere nulla. Blocca il crawler e si scarica con curl locale.",
     [("[[08-cavo-link]]", "sezione sull'hardware sotto il protocollo"),
      ("[[30-opzioni-implementative]]", "costo reale dell'opzione D")],
     [("conferma", "cable-link")]),

    ("gbatek", "GBATEK, multiboot", "https://problemkaputt.de/gbatek-bios-multi-boot-single-game-pak.htm", 1, True, ["BRI"],
     "Specifica del multiboot del Game Boy Advance: la stretta di mano con 0x6200 e la risposta 0x0000, le dimensioni ammesse del programma, gli indirizzi di destinazione in memoria di lavoro, la cifratura del trasferimento e i vincoli di temporizzazione.",
     "E' cio' che va implementato se si scegliesse di costruire il ponte da zero, e dice quanto spazio si ha davvero: al massimo circa 256 kilobyte, con gli indirizzi assoluti riferiti alla memoria di lavoro e non alla cartuccia.",
     [("[[10-multiboot-hardware]]", "la procedura di multiboot")],
     []),

    ("copetti", "Copetti, architettura del GBA", "https://www.copetti.org/writings/consoles/game-boy-advance/", 1, True, ["BRI"],
     "Descrizione architetturale del Game Boy Advance: le due memorie di lavoro con le loro dimensioni e velocita', il bus della cartuccia, il buffer di prefetch e il meccanismo della retrocompatibilita' con il Game Boy.",
     "Spiega perche' un programma multiboot vive nella memoria esterna, che e' fino a sei volte piu' lenta, e quindi perche' i progetti di questo tipo curano la compressione dei dati.",
     [("[[10-multiboot-hardware]]", "la memoria in cui vive il programma")],
     []),

    ("devlog-ptgb", "Dev log di Poke Transporter GB", "https://www.austinthomasweber.com/poke-transporter-gb", 4, True, ["BRI"],
     "Serie di undici articoli in cui l'autore del ponte di riferimento racconta il proprio processo, dall'architettura della console al formato di salvataggio, dal protocollo del cavo alla scoperta dell'exploit, fino all'iniezione dell'evento e alla gestione della grafica.",
     "E' la fonte piu' ricca sul nostro problema perche' il codice dice cosa fa e questi articoli dicono perche'. Da qui vengono la specifica esatta dell'exploit e la scoperta che il Pokemon entra in Gen 3 tramite un evento Dono Segreto.",
     [("[[09-esecuzione-codice]]", "specifica dell'innesco e il lato che scrive"),
      ("[[10-multiboot-hardware]]", "il lato che scrive"),
      ("[[08-cavo-link]]", "voltaggi e temporizzazione del clock")],
     [("documenta", "ptgb")]),

    ("ptgb", "Poke Transporter GB", "https://github.com/Striaton-Lab-Team/Poke_Transporter_GB", 3, True, ["BRI"],
     "Il ponte di riferimento: homebrew per Game Boy Advance in multiboot che trasferisce Pokemon da Gen 1 e 2 a Gen 3 usando il cavo del Game Boy Color, sotto licenza MIT. Contiene un generatore di payload con assemblatore Z80 proprio e tabelle di valori di ROM per lingua.",
     "E' la prova che il ponte e' possibile, ed e' il repertorio delle soluzioni. Il suo codice ha rivelato cio' che il README non dichiara, cioe' che il payload viaggia sul cavo al posto della squadra.",
     [("[[09-esecuzione-codice]]", "che cosa ci fa il ponte"),
      ("[[30-opzioni-implementative]]", "opzione A")],
     [("usa", "pccs")]),

    ("pccs", "PCCS", "https://github.com/Striaton-Lab-Team/Pokemon-Community-Conversion-Standard", 3, True, ["BRI"],
     "Libreria C++ che definisce come convertire un Pokemon da Gen 1 e 2 a Gen 3. Il README documenta quattro metodi campo per campo; il codice della release corrente implementa il comportamento di uno solo.",
     "E' la specifica di riferimento della conversione, e il suo codice contiene il campionamento con rifiuto del valore di personalita' e l'uso dell'ID segreto per la lucentezza, che confermano una deduzione fatta prima di leggerlo.",
     [("[[07-conversione-vincoli]]", "solutore di vincoli e ruolo dell'ID segreto"),
      ("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "sezione 9, cio' che va inventato")],
     []),

    ("gen3togenx", "Pokemon-Gen3-to-Gen-X", "https://github.com/Lorenzooone/Pokemon-Gen3-to-Gen-X", 3, True, ["BRI"],
     "Homebrew per Game Boy Advance che scambia Pokemon fra Gen 3 e Gen 1 e 2 usando il protocollo normale e non exploit, con in piu' la gestione dell'orologio interno di Rubino, Zaffiro e Smeraldo.",
     "E' l'alternativa architetturale al ponte di riferimento: dimostra che si puo' fare senza esecuzione di codice, al prezzo di non replicare l'esperienza dello scambio.",
     [("[[08-cavo-link]]", "le due strategie per il ponte"),
      ("[[30-opzioni-implementative]]", "confronto fra le strade")],
     [("alternativa-a", "ptgb")]),

    ("pokemongb-online", "PokemonGB_Online_Trades", "https://github.com/Lorenzooone/PokemonGB_Online_Trades", 3, True, ["BRI"],
     "Implementazione in Python del protocollo di scambio di Gen 1, 2 e 3, funzionante sia su un adattatore USB per il cavo sia sull'emulatore BGB, con multiboot per il lato Gen 3.",
     "E' la dimostrazione che il lato Game Boy si collauda su emulatore, e quindi che una parte del protocollo si sviluppa senza hardware.",
     [("[[21-collaudo]]", "il secondo livello di collaudo")],
     []),

    ("cable-link", "CableClub/cable-link", "https://github.com/CableClub/cable-link", 3, True, ["BRI"],
     "Circuito stampato in formato KiCad, con gerber pronti alla produzione, e firmware per Raspberry Pi Pico che parla il protocollo di scambio di generazione 1. Apache 2.0, del 2021.",
     "E' il precedente piu' avanzato per l'opzione D, e vale come conferma indipendente: le sue costanti del protocollo coincidono una per una con quelle che avevamo ricavato dal disassemblato, e apre la porta seriale esattamente al mezzo megahertz che Pan Docs dichiara come massimo.",
     [("[[08-cavo-link]]", "la conferma indipendente delle costanti"),
      ("[[30-opzioni-implementative]]", "opzione D, che non parte da zero")],
     [("conferma", "pokered")]),

    ("pksploit", "PkSploit", "https://github.com/binarycounter/PkSploit", 3, True, ["BRI", "SME"],
     "Suite che dumpa ROM e salvataggio e riscrive il salvataggio di qualunque cartuccia Game Boy e Game Boy Color, usando come vettore una cartuccia di generazione 1, un cavo Link e un microcontrollore compatibile Arduino.",
     "Se l'affermazione regge alla prova, un microcontrollore sostituisce il lettore di cartucce per tutto cio' che e' Game Boy, e questo tocca sia il ponte sia il modo di procurarsi i dump. L'autore avverte che e' in sviluppo pesante.",
     [("[[09-esecuzione-codice]]", "il precedente minimale"),
      ("[[30-opzioni-implementative]]", "opzione D senza lettore")],
     [("deriva-da", "cableclubhack")]),

    ("cableclubhack", "vaguilar/pokemon-red-cable-club-hack", "https://github.com/vaguilar/pokemon-red-cable-club-hack", 3, True, ["BRI"],
     "Implementazione originale dell'exploit del Centro Scambi con Arduino e Python. Documenta il cablaggio dei pin, cioe' uscita seriale sul pin 6, ingresso sul 3, clock sul 2 e massa, e contiene il payload in un array dentro un'intestazione Arduino.",
     "E' la base di PkSploit e la fonte del cablaggio, che nessun'altra fonte scriveva. Contiene anche un'implementazione del protocollo dell'emulatore BGB sulla porta 8765, che e' il banco di collaudo che ci serve.",
     [("[[09-esecuzione-codice]]", "il vettore dal cavo"),
      ("[[21-collaudo]]", "il protocollo di BGB e la sua porta")],
     []),

    ("linkhack", "Phasip/PokemonLinkHack", "https://github.com/Phasip/PokemonLinkHack", 3, True, ["BRI"],
     "Catena di exploit che dal buffer overflow del cavo arriva a installare programmi persistenti dentro il deposito Pokemon: un selettore nel primo slot e i programmi nei successivi, sopravvivendo ai riavvii grazie al salvataggio della cartuccia.",
     "E' la strategia opposta a quella del ponte, che usa un payload transitorio. Se un giorno servisse un lanciatore stabile dentro la cartuccia, questa e' la strada, e il suo costo dichiarato e' rinunciare all'uso normale dell'asilo.",
     [("[[09-esecuzione-codice]]", "vie alternative e persistenza")],
     [("deriva-da", "cableclubhack")]),

    ("blog-phasip", "Blog di Phasip", "https://www.sn1.se/posts/pokemon/", 4, True, ["BRI"],
     "Racconto della catena di exploit con i numeri: 198 byte di payload utile, i programmi che risiedono negli slot del deposito, e il limite dichiarato che fuori dal buffer si possono scrivere solo nomi di Pokemon predefiniti.",
     "Da' la misura del payload e il vincolo che determina la forma della catena, cioe' che il primo salto deve passare per dati che il gioco recupera dalla tabella dei nomi.",
     [("[[09-esecuzione-codice]]", "dimensione del payload e vincoli")],
     [("documenta", "linkhack")]),

    ("arduino-poke-gen2", "arduino-poke-gen2", "https://github.com/stevenchaulk/arduino-poke-gen2", 3, True, ["BRI"],
     "Adattamento a generazione 2 di una macchina a stati Arduino per lo scambio, provato su Cristallo, con schema di cablaggio incluso.",
     "Porta un fatto architetturale che semplifica il firmware: in generazione 2 non serve memorizzare nulla, perche' rimandando indietro i byte ricevuti si ottiene la copia della squadra.",
     [("[[30-opzioni-implementative]]", "opzione D, il caso piu' semplice")],
     [("deriva-da", "arduino-boy")]),

    ("arduino-boy", "pepijndevos/arduino-boy", "https://github.com/pepijndevos/arduino-boy", 3, True, ["BRI"],
     "Deposito Pokemon su Arduino per i giochi di generazione 1: memorizza un Pokemon nella memoria non volatile della scheda e lo scambia con la console. Il codice del protocollo deriva a sua volta da un progetto precedente chiamato gameboy-spoof.",
     "E' l'origine della famiglia di implementazioni Arduino del protocollo, quindi il capostipite da leggere per capire da dove viene il codice degli altri.",
     [("[[30-opzioni-implementative]]", "opzione D, genealogia delle implementazioni")],
     []),

    ("gba-link-connection", "gba-link-connection", "https://github.com/afska/gba-link-connection", 3, True, ["BRI"],
     "Libreria C++ per il porto seriale del Game Boy Advance, con moduli separati per la modalita' multiplayer, l'invio di multiboot ad altre console, l'adattatore wireless, il protocollo Joybus verso Wii e GameCube, le carte e-Reader e il Mobile Adapter GB.",
     "Il modulo che conta per noi collega la console a un PC o a un Raspberry Pi usando il cavo del Game Boy Color: e' l'infrastruttura pronta per l'opzione D dal lato Game Boy Advance.",
     [("[[10-multiboot-hardware]]", "vie per il multiboot"),
      ("[[30-opzioni-implementative]]", "opzione D e opzione C")],
     []),

    ("reon", "Progetto REON", "https://github.com/REONTeam", 3, True, ["BRI"],
     "Ricostruzione dell'infrastruttura di rete del Mobile Adapter GB, l'accessorio che dava funzioni online ai giochi Game Boy. Comprende una libreria del protocollo in C, un server, un emulatore per BGB, un adattatore su Arduino e una utilita' dedicata allo scambio nel Trade Corner.",
     "E' un secondo canale storico oltre al cavo, e la sua utilita' per il Trade Corner riguarda direttamente lo scambio di Pokemon. Da valutare se apra una strada alternativa al cavo per il lato generazione 2.",
     [("[[08-cavo-link]]", "canali alternativi al cavo")],
     []),

    ("gen3distributions", "Goppier/GEN3PokemonDistributions", "https://github.com/Goppier/GEN3PokemonDistributions", 3, True, ["BRI"],
     "Raccolta di cartucce di distribuzione per eventi di generazione 3, con la procedura operativa per usarle fra due console.",
     "Da' il dettaglio che al progetto mancava sul multiboot dal lato dell'utente: la console ricevente si accende tenendo premuti start e select finche' il logo Nintendo scompare, con il lato master del cavo nella console che invia.",
     [("[[10-multiboot-hardware]]", "procedura utente del multiboot")],
     []),

    ("stadium-ace", "MrCheeze/pokestadium-ace", "https://github.com/MrCheeze/pokestadium-ace", 3, True, ["BRI"],
     "Esecuzione di codice arbitrario su Pokemon Stadium per Nintendo 64, che passa dal sistema di scambio e presuppone di avere gia' il controllo su un gioco di generazione 1. Documenta gli indirizzi dove i box vengono convertiti dal formato Gen 1 al formato Stadium.",
     "E' il terzo esempio documentato di conversione fra formati Pokemon fatta da software ufficiale, dopo il Time Capsule e il Pal Park, e quindi materiale di studio su come gli autori originali risolvevano il problema.",
     [("[[08-cavo-link]]", "precedenti di conversione fra formati")],
     []),

    ("usb-gba-multiboot", "usb-gba-multiboot", "https://github.com/tangrs/usb-gba-multiboot", 3, True, ["BRI"],
     "Firmware per microcontrollore Teensy e software su PC per caricare un programma nella console via USB, sfruttando il multiboot.",
     "E' la via al multiboot che non richiede ne' GameCube ne' flashcart, e motiva la scelta della modalita' seriale normale perche' e' a 32 bit e riceve mentre invia.",
     [("[[10-multiboot-hardware]]", "vie per il multiboot")],
     [("alternativa-a", "rom-sender")]),

    ("rom-sender", "gba-link-cable-rom-sender", "https://github.com/FIX94/gba-link-cable-rom-sender", 3, True, ["BRI"],
     "Homebrew per GameCube e Wii che invia un programma multiboot alla console collegata, leggendo i file da una cartella sulla scheda di memoria.",
     "E' la via al multiboot che il progetto di riferimento consiglia per prima, e quella che evita lo scambio a caldo della cartuccia se si ha una console adatta.",
     [("[[10-multiboot-hardware]]", "vie per il multiboot")],
     []),

    ("kinnay-ldn", "kinnay, protocollo LDN", "https://github.com/kinnay/NintendoClients/wiki/LDN-Protocol", 1, True, ["LDN"],
     "Specifica del protocollo di rete locale della Nintendo Switch: action frame proprietario trasmesso ogni cento millisecondi, canali radio usati, struttura dell'annuncio campo per campo, tre livelli di cifratura con la derivazione delle chiavi, e sequenza di connessione con assegnazione degli indirizzi.",
     "E' la sola specifica completa del protocollo su cui il track dello scambio con la Switch si basa, e spiega perche' servano le chiavi della console: senza quelle non si derivano le chiavi di sessione.",
     [("[[04-cifratura-gen3]]", "i dati scambiati sono strutture Gen 3")],
     []),

    ("frlg-ldn-trade", "tornadus/frlg-ldn-trade", "https://github.com/tornadus/frlg-ldn-trade", 3, True, ["LDN"],
     "Proof of concept che fa scambiare Pokemon a un PC con Rosso Fuoco e Verde Foglia in esecuzione su Switch, simulando un giocatore che si collega come capo sessione.",
     "E' il punto di partenza del track, e dichiara la lista di compatibilita' delle schede Wi-Fi, che e' la risposta anticipata alla domanda che quel track ha come blocco.",
     [("[[06-identita-pokemon]]", "i formati .pk3 e .ek3 sono strutture Gen 3")],
     [("usa", "kinnay-ldn")]),

    ("ldn-mitm", "ldn_mitm", "https://github.com/spacemeowx2/ldn_mitm", 3, True, ["LDN"],
     "Modulo di sistema per Switch che sostituisce il servizio di rete locale ed emula la scansione delle console vicine usando la rete locale via UDP.",
     "E' l'approccio opposto a quello del proof of concept: invece di parlare il protocollo radio, lo sostituisce con traffico di rete. Utile come piano alternativo se la scheda Wi-Fi non supportasse la modalita' monitor.",
     [("[[06-identita-pokemon]]", "contesto del track LDN")],
     [("usa", "switch-lan-play")]),

    ("switch-lan-play", "switch-lan-play", "https://github.com/spacemeowx2/switch-lan-play", 3, True, ["LDN"],
     "Client e server che intercettano il traffico di rete della console con libpcap e lo incapsulano in un protocollo minimale, per far credere alle console di essere sulla stessa rete locale.",
     "E' la controparte del modulo di sistema, e insieme formano l'alternativa che non richiede hardware radio particolare. Licenza GPL 3.",
     [("[[06-identita-pokemon]]", "contesto del track LDN")],
     []),

    ("bulbapedia", "Bulbapedia, pagine sui formati", "https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_III)", 2, True, ["BRI", "SME", "LDN"],
     "Insieme di pagine enciclopediche sui formati dei dati e dei salvataggi delle tre generazioni, sui valori individuali, sul valore di personalita', sulla codifica dei caratteri e sugli indici di specie.",
     "E' il punto di partenza per orientarsi e la mappa di dove guardare nel disassemblato, ma su cinque punti verificati si e' rivelata sbagliata: cifre di Gen 1, maiuscole di Gen 3, checksum di Gen 3, dimensione del blocco di scambio e chiave di Rosso Fuoco.",
     [("[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "tutte le sezioni, come punto di partenza"),
      ("[[23-prove-eseguite]]", "il caso studio sull'affidabilita' delle fonti")],
     []),

    ("glitchcity", "Glitch City Wiki", "https://glitchcity.wiki", 2, True, ["BRI"],
     "Catalogo della ricerca sui glitch dei giochi di generazione 1 e 2, compresi i metodi di esecuzione di codice raggiungibili giocando e quelli che passano dal cavo.",
     "Serve a orientarsi nel campo e a valutare alternative, ma sul vettore che ci interessa rimanda a fonti esterne. Respinge il recupero automatico e si legge dal mirror statico.",
     [("[[09-esecuzione-codice]]", "vie dal lato del giocatore")],
     []),

    ("pokemon-automation", "Pokemon Automation", "https://pokemonautomation.github.io/", 3, True, ["AUT", "LDN"],
     "Progetto che automatizza le parti ripetitive dei giochi Pokemon su Nintendo Switch con oltre cento programmi. E' un anello di controllo chiuso su un sistema che non espone stato: percepisce il fotogramma video e in alcuni titoli l'audio, attua tramite un controller emulato da un microcontrollore, e decide con un programma per compito. Il perimetro dichiarato e' console non modificate e nessun accesso alla memoria.",
     "E' la fonte fondante del quinto sottoprogetto, che nasce come studio, e la lettura del 2026-08-26 ha prodotto due risultati oltre l'atteso: il perimetro del progetto e' compatibile con le regole di questo, e fra i titoli automatizzati compaiono Rosso Fuoco e Verde Foglia su Switch, che e' il gioco al centro del track dello scambio con la Switch. La visione artificiale resta una capacita' che il progetto non ha in nessun altro track.",
     [("[[30-opzioni-implementative]]", "sovrapposizione di esperienza sul microcontrollore, che e' l'opzione D")],
     []),

    ("gambatte-gamelink", "Gambatte con GameLink su TCP", "https://gbatemp.net/threads/mission-wireless-trading-on-gen1-and-gen2-pokemon-games.632492/", 5, True, ["BRI"],
     "Discussione in cui un membro compila una versione di Gambatte con il collegamento seriale del Game Boy emulato su TCP, funzionante sia come client sia come server, e riferisce di aver scambiato e combattuto nei giochi di generazione 1 e 2 fra dispositivi diversi, Switch compreso.",
     "E' la seconda via di collaudo del protocollo oltre a BGB, e ha due vantaggi: non e' specifica dei Pokemon perche' emula un cavo seriale generico, ed esiste come nucleo libretro, quindi si presta a essere pilotata senza interfaccia grafica.",
     [("[[21-collaudo]]", "il secondo livello di collaudo")],
     [("alternativa-a", "cableclubhack")]),

    ("projectpokemon", "Project Pokemon, discussioni", "https://projectpokemon.org/home/forums/topic/64794-pokemon-emerald-items-are-in-the-right-bag-using-the-app-but-when-i-load-it-into-a-cartridge-they-go-in-the-wrong-slots/", 5, True, ["SME", "BRI"],
     "Tre discussioni lette: una su un dispositivo che fa da sorgente di clock per il protocollo e ha completato scambi via internet, una su un salvataggio assente invece che corrotto su cartuccia contraffatta, e una su un editor che ha identificato male il gioco facendo finire gli oggetti negli slot sbagliati.",
     "La terza ha prodotto codice: il rilevamento automatico del gioco nel nostro strumento di diagnosi nasce da la'. La prima ha rivelato l'esistenza di CableClub.",
     [("[[22-strumenti]]", "perche' lo strumento non si fida del parametro")],
     [("documenta", "cable-link")]),
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
    righe.append("## Perche' e' in archivio")
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
    righe.append("Livello %d di affidabilita' secondo la gerarchia di [[SOURCES]]. Track serviti: %s. La mappa di tutte le fonti e delle loro relazioni e' [[index-fonti]]."
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
    righe.append("Questa cartella contiene una nota per ciascuna fonte che porta peso tecnico, con il suo abstract, il motivo per cui e' in archivio, il punto esatto del progetto che serve e le relazioni verso le altre fonti. Il registro completo, comprese le voci minori e quelle non lette, resta [[SOURCES]]: questa mappa non lo sostituisce, lo rende navigabile.")
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
    print("scritte %d note piu' la mappa in %s" % (len(FONTI), OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
