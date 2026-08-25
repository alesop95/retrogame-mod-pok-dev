---
tipo: nota di studio
livello: codice
tags: [prove, verifica, onesta, falsificabilita]
up: "[[index]]"
vedi_anche: ["[[21-collaudo]]", "[[22-strumenti]]", "[[20-architettura-codice]]", "[[SOURCES]]"]
---

# Che cosa e' stato verificato davvero, con che cosa, e che cosa no

Questa nota esiste perche' la domanda giusta, davanti a un progetto che dichiara di aver verificato molte cose, e' sempre la stessa: verificato come, e con che cosa. Senza una risposta scritta, la parola verificato si degrada in fretta fino a significare letto da qualche parte. Qui c'e' l'inventario preciso, compreso l'elenco di cio' che non e' stato verificato affatto, che e' la parte piu' utile.

Una precisazione di vocabolario da fare subito, perche' evita un fraintendimento serio. Nulla di quanto segue e' una simulazione nel senso dell'emulazione: non e' stato lanciato nessun emulatore, non e' stato eseguito nessun gioco, non e' stato letto nessun salvataggio reale e non e' stata toccata nessuna console. Le verifiche sono di due tipi soltanto: lettura del codice sorgente dei giochi, e prove di programma su dati costruiti a tavolino.

## Il primo tipo: lettura del sorgente

Il metodo e' stato clonare in superficie i repository che contano e cercare nel codice, invece di leggere sintesi. Il comando e' sempre lo stesso, e la ragione per cui il clone batte la lettura via web e' che permette di cercare, di seguire una costante fino alla sua definizione e di contare i campi di una struttura.

```
git clone --depth 1 https://github.com/pret/pokered
git clone --depth 1 https://github.com/pret/pokecrystal
git clone --depth 1 https://github.com/pret/pokeemerald
git clone --depth 1 https://github.com/Striaton-Lab-Team/Pokemon-Community-Conversion-Standard
git clone --depth 1 https://github.com/Striaton-Lab-Team/Poke_Transporter_GB
git clone --depth 1 https://github.com/Lorenzooone/Pokemon-Gen3-to-Gen-X
```

Da qui vengono tutte le affermazioni di [[DATA-FORMATS_Gen1-Gen2-Gen3]]. La tabella seguente dice quale file ha risposto a quale domanda, perche' un'affermazione senza il suo punto di origine non si puo' ricontrollare.

| Domanda | File che ha risposto |
|---|---|
| forma delle strutture Gen 1 | `pokered/macros/ram.asm`, macro `box_struct` e `party_struct` |
| lunghezze dichiarate | `pokered/constants/pokemon_data_constants.asm`, `constants/text_constants.asm` |
| ordine dei nibble dei DV e derivazione del quinto | `pokecrystal/engine/pokemon/move_mon.asm`, routine `CalcMonStatC` |
| tabella caratteri Gen 1 e 2 | `pokecrystal/constants/charmap.asm` |
| strutture di invio Gen 2, native e Time Capsule | `pokecrystal/ram/wram.asm` |
| costanti del protocollo seriale | `pokered/constants/serial_constants.asm` |
| dimensione del blocco di scambio | `pokered/engine/link/cable_club.asm`, somma di costanti passata a `Serial_ExchangeBytes` |
| meccanismo della lista di correzione | `pokered/engine/link/cable_club.asm`, ramo `.checkPlayerDataByte` |
| struttura Gen 3 e sottostrutture | `pokeemerald/include/pokemon.h` |
| cifratura e checksum del Pokemon | `pokeemerald/src/pokemon.c`, `EncryptBoxMon` e `CalculateBoxMonChecksum` |
| tabella caratteri Gen 3 | `pokeemerald/charmap.txt` |
| settori del salvataggio, firma e checksum | `pokeemerald/include/save.h`, `src/save.c`, funzione `CalculateChecksum` |
| chiave di cifratura e offset dello zaino | `pokeemerald/include/global.h`, `src/item.c` |
| generazione del valore di personalita' | `PCCS/source/GBPokemon.cpp`, ciclo di campionamento con rifiuto |
| uso dell'ID segreto per la lucentezza | `PCCS/source/GBPokemon.cpp`, `convertShininess` |
| metodi PCCS realmente implementati | ricerca dei quattro nomi su tutto il repository: solo nel README |
| come Poke Transporter GB esegue codice | `Poke_Transporter_GB/source/gameboy_colour.cpp`, `exchange_parties` |

Accanto ai cloni sono stati recuperati documenti dal web, e la loro affidabilita' e' stratificata nel registro [[SOURCES]]. Le pagine enciclopediche sono servite a orientarsi e in quattro casi si sono rivelate sbagliate; i blog tecnici sono serviti a capire il perche'; i risultati di ricerca sono serviti a scoprire l'esistenza di progetti come `PkSploit` e la possibilita' di collaudo su BGB.

Due limiti dichiarati sul recupero web, gia' registrati in [[SOURCES]] ma che vale ripetere qui perche' riguardano l'onesta' delle fonti. YouTube restituisce una pagina di consenso invece del contenuto, quindi nessuno dei video e' stato guardato: i canali sono identificati, non consultati. Reddit non e' stato letto, e la ragione e' stata indagata invece che assunta: cinque vie tentate e tutte fallite, per un blocco che sta a monte e non nel progetto, con le due vie praticabili e lo strumento che le implementa descritti in `.claude/rules/web-sources-not-fetchable.md`.

## Il secondo tipo: prove di programma

Sono tre esecuzioni distinte, e conviene distinguerle perche' hanno forza diversa.

La prima e' la generazione delle tabelle caratteri. Lo strumento ha letto i due charmap dai cloni e ha prodotto tre file JSON, verificando otto sentinelle prima di scrivere, cioe' terminatore, spazio, A, Z, a, z, 0 e 9 in entrambe le codifiche. Questa non e' una prova di logica: e' una prova che i dati a monte sono stati letti correttamente, ed e' forte perche' i dati a monte sono la definizione autorevole. Esito: duecento caratteri stampabili per Gen 1 e 2, duecentoquarantotto per Gen 3, centoquarantasette corrispondenze fra le due e cinquantatre caratteri privi di destinazione.

La seconda e' la diagnostica dello zaino di Smeraldo, eseguita su un salvataggio sintetico costruito a tavolino: 128 KiB, uno slot valido con quattordici settori dai piedi corretti, una chiave di cifratura nota, un denaro noto e mascherato, e cinque anomalie deliberate. Ha trovato tutte e cinque le anomalie, ma il valore vero e' stato un difetto trovato nel codice diagnostico stesso: considerava vuoto uno slot con quantita' zero, mentre in una tasca mascherata uno slot vuoto non ha quantita' zero, contiene la chiave. Da quel difetto e' nata una verifica incrociata gratuita, perche' la chiave si ricava da qualunque slot vuoto e si confronta con quella letta al suo offset.

La terza e' la suite del pacchetto `pokebridge`, sessantatre prove ripartite cosi'.

| Modulo | Prove | Che cosa copre |
|---|---|---|
| `test_gb.py` | 17 | interi big-endian, nibble dei DV, derivazione del quinto DV, byte dei PP, array di nomi |
| `test_gen1.py` | 15 | strutture di box e squadra, lista della squadra, caso costruito a mano, percorsi di errore |
| `test_gen2.py` | 16 | le stesse cose, piu' dati di cattura, Pokerus, oggetto tenuto, lucentezza da DV |
| `test_charmap.py` | 15 | sentinelle delle tabelle, decodifica, codifica, traduzione fra le due codifiche |

Dentro quelle prove ci sono tre livelli di copertura, e la distinzione conta.

Esaustive, cioe' su tutto lo spazio possibile: i duecentocinquantasei byte di PP, le sessantacinquemilacinquecentotrentasei coppie di byte dei dati di cattura di Cristallo, e le sessantacinquemilacinquecentotrentasei combinazioni dei quattro DV per contare quante producano un Pokemon lucente in generazione 2. Quest'ultima non verifica il codice ma la comprensione della regola: il conteggio torna a otto, e sessantacinquemilacinquecentotrentasei diviso otto fa ottomilacentonovantadue, cioe' la probabilita' documentata. Se avessi frainteso la regola, quel numero non tornerebbe.

Campionate con passo primo, dove lo spazio e' troppo grande: gli interi a 16 bit con passo novantasette, quelli a 24 bit con passo novemilanovecentosettantatre. Il passo primo evita di provare soltanto valori con la stessa struttura binaria.

Casuali con seme fissato, per la prova portante: cinquecento buffer per ciascuna delle quattro forme di struttura e cinquanta per ciascuna delle due liste di squadra. Il seme e' dichiarato nel codice, quindi un fallimento e' riproducibile e non capriccioso.

## Che cosa dimostra la prova di simmetria, e che cosa non dimostra

Questa e' la parte che rende la nota utile, perche' e' la sola cosa che nessun rapporto entusiasta scrive.

La prova di simmetria dice che leggere e riscrivere restituisce byte identici. Ne segue che il lettore e lo scrittore sono l'uno l'inverso dell'altro, che nessun campo viene perso, che nessun bit viene troncato, che l'ordine dei byte e' coerente fra le due direzioni e che i campi non dichiarati, come il byte inutilizzato a 0x21 in generazione 2, sopravvivono al viaggio. Su un writer che dovra' scrivere su una cartuccia, questa e' una garanzia che vale.

Non dice nulla sull'identita' dei campi. Se avessi scambiato fra loro due campi della stessa larghezza, per esempio tipo 1 con tipo 2, oppure due delle cinque Stat Experience, la simmetria continuerebbe a valere perfettamente: leggo il tipo 1 nella posizione del tipo 2, lo riscrivo nella stessa posizione, e i byte tornano identici. La prova e' invariante rispetto a una permutazione di etichette, e questo e' un limite strutturale, non una dimenticanza.

Contro quel limite ci sono due difese, entrambe parziali. La prima e' il caso costruito a mano nelle prove di generazione 1, che assegna valori distinti e riconoscibili a offset specifici e verifica che escano dai campi giusti: copre gli offset che ho scritto a mano nella prova, non tutti. La seconda e' che gli offset provengono dal disassemblato e non da una fonte secondaria, quindi l'errore dovrebbe essere di trascrizione mia e non della fonte.

La difesa che manca e' il confronto con un'implementazione indipendente, e qui va corretta una cosa che avevo detto in modo troppo pessimistico: non serve un salvataggio reale. Serve un salvataggio, e un salvataggio lo produce il nostro stesso scrittore. Si sintetizza un salvataggio con `pokebridge`, con campi scelti in modo che ciascuno abbia un valore distinto e riconoscibile, si apre con `PKHeX` e si confronta campo per campo cio' che dichiara lui con cio' che abbiamo scritto noi. Se due campi della stessa larghezza sono scambiati, `PKHeX` mostra i valori invertiti e la permutazione salta all'occhio.

E' una prova di conformita' contro un'implementazione indipendente, costa un'ora e non richiede alcun hardware, quindi va prima e non dopo il resto. Resta un'incognita dichiarata: `PKHeX` valida il salvataggio prima di aprirlo, e un salvataggio sintetico potrebbe essere rifiutato per campi che non abbiamo popolato, per esempio l'identificazione del gioco. Se accadesse, la via di riserva e' popolare quei campi finche' il file passa la validazione, che e' comunque informazione utile su cosa il formato richiede davvero.

Il confronto con un salvataggio reale resta l'ultima parola, perche' e' il solo che verifica anche le assunzioni che condividiamo con noi stessi, ma non e' un prerequisito.

## Che cosa non e' stato verificato per niente

L'elenco e' importante quanto quello di sopra, e va tenuto aggiornato invece che dimenticato.

| Area | Stato |
|---|---|
| lettura di un salvataggio reale, di qualsiasi generazione | mai fatta, manca il lettore hardware |
| confronto dell'interpretazione dei campi con `PKHeX` o `PKSav` | mai fatto, ed e' il prossimo controllo che costa meno |
| protocollo del cavo Link in esecuzione | mai provato; il codice non esiste ancora |
| collaudo su BGB via TCP | mai fatto; e' possibile e documentato, ma nessun emulatore e' stato lanciato |
| payload di esecuzione di codice | mai costruito ne' provato |
| multiboot e scambio a caldo della cartuccia | mai provati, richiedono hardware |
| strutture Gen 3 in lettura e scrittura | codice non ancora scritto |
| offset dello zaino per Rosso Fuoco e Verde Foglia | dichiarati non verificati nello strumento stesso |
| offset dei salvataggi Gen 2 per lingue diverse dall'inglese | fuori dalla portata dei disassemblati pret |

## Il metodo, in una riga

Le prove di programma verificano la coerenza interna di cio' che ho scritto; la lettura del sorgente verifica che cio' che ho scritto corrisponda al gioco; e nessuna delle due sostituisce il confronto con un dato reale, che resta l'unica prova che chiude il cerchio. Tenere separate le tre cose e' quello che permette di dire verificato senza doverci mettere un asterisco.

## Cosa leggere dopo

[[21-collaudo]] spiega la strategia di collaudo per strati, e [[20-architettura-codice]] risponde alla domanda su dove questo codice girera' davvero.
