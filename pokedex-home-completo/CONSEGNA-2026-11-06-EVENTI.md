# La consegna del 2026-11-06: i 46 eventi senza carta, le varianti, le fonti da leggere

> Documento autorato il 2026-11-06 dall'agente, su richiesta del proprietario, per assorbire il file di lavoro che il proprietario ha compilato a mano evento per evento e poi cancellato dal desktop. La copia integrale del file sta nel livello privato, `_notes/fonti/consegne/2026-11-06-retrogame/RETROGAME.txt`, SHA-256 `1642aa34c78ee04c8bc55e5973496c83c71fc6b59cbaddd43d711844e939857b`, 2691 righe, 172.983 byte, identica byte per byte all'originale prima della cancellazione. Le decisioni stanno in ADR-118, il lavoro aperto in `.claude/memory/pending.md`, voce «CONSEGNA DEL 2026-11-06», e le fonti nuove in `SOURCES.md`, sezione «Le consegne del proprietario del 2026-11-06».

## L'esito al 2026-11-07, direttiva per direttiva (ADR-119)

Il proprietario ha chiesto il 2026-11-06 di fare tutto in un giro solo. Questa tabella dice che cosa è stato fatto di ciascuna direttiva della sezione più sotto e su quale misura poggia; le sezioni che seguono restano come registrazione della consegna.

| N. | Direttiva | Esito |
|---|---|---|
| 1 | Le fonti della consegna lette e registrate | Fatto: 69 indirizzi in `SOURCES.md` con lo stato di lettura reale, nessuno non letto; più le raccolte intere di Bulbapedia, Pokémon Historian e PocketMonsters.net |
| 2 | I 46 eventi verificati e prodotti | Fatto: 20 erano già nelle copie, 22 mancavano e sono prodotti, 4 avevano un ID di Serebii sbagliato (Pachirisu 05165 e Garchomp 07226 in tutte le lingue, già nelle copie) o sconosciuto alla libreria (Darkrai 6281); i 12 di JEREMY sono riprodotti sugli esemplari documentati da Bulbapedia; il Natale 2013 consegnava Haunter e Scyther, già nelle copie (carta 7) |
| 3 | Le varianti per allenatore o ID tutte | Fatto per tutte quelle che la libreria conosce: 104 doni del Ranch in cinque lingue; il Jirachi del Daisuki Club 07078 non esiste nella libreria né nell'archivio delle carte, solo 07077 |
| 4 | Il Daisuki Club oltre ai 46 | Fatto: 29 esemplari dello staff (Magikarp di San Valentino 5, Daisuki Club Party 2, GTS Act 1 4, GTS09 12, Psyduck dei creatori 3, Heracross di Nintendo of America 3); non riproducibili: il Milotic di ナナ, perché la libreria costruisce un Feebas e il verificatore non accetta il Milotic che ne deriva, e per ID mancante o parziale alla fonte il Garchomp di のりっく e il Magnezone e il Sableye di Goruchan |
| 5 | Pokémon Historian per intero | Fatto: 501 pagine, 498 lette, 982 voci, confrontate con le copie |
| 6 | L'archivio di Project Pokémon per intero | Fatto attraverso la libreria, che ne contiene le carte: tutte le carte fino alla settima generazione sono nelle copie, salvo 144 carte gemelle (già presenti una per carta, ADR-117) e 148 doni dell'epoca Game Boy (per le cartucce); 14 varianti di terza generazione mancavano e sono prodotte |
| 7 | PocketMonsters.net per intero | Fatto: 1447 schede su 1447; dopo il confronto per specie, livello e mosse restano solo eventi già prodotti oggi o il cui allenatore è quello del giocatore |
| 8 | Bulbapedia per intero | Fatto dalla Wayback Machine: 103 pagine su 108, 802 schede; nelle copie di sesta e settima generazione l'archivio porta i soli titoli, e vale il confronto con le carte della libreria |
| 9 | Il filo di PokéCommunity | Letto: lista di scambio personale del 2008, nessun Pokémon della consegna |
| 10 | Le controparti WCS 2014 | Confermate tutte e sei |
| 11 | Il Latios tedesco nel lotto del decimo anniversario | Confermato, ID 06227 come nel codice di PKHeX |
| 12 | Contribuire a PKHeX | Risposto nel recap del 2026-11-07: sì, con prove documentate, per gli eventi senza carta che oggi il verificatore accetta solo come incontri normali |
| 13 | Serebii spulciato a fondo | Fatto: i 1591 eventi confrontati per specie e allenatore; nessuna lacuna oltre a quelle prodotte oggi |
| 14 | Ciò che resta fuori dai lotti, nella fase Switch | Registrato in `pending.md`, dopo Bank |
| 15 | Solo originali, non sostituti | Fatto: il Jirachi di Channel Sicuro 31/19/30/31/30/31 del video di blisy è prodotto dal suo seme, non cromatico come il seme impone; il WISHMKR Allegro cromatico non esiste fra i 65536 semi e non si produce |
| 16 | Storia per ogni riga del pedigree, e il conto dei 7000 | Fatto: 6206 righe, 6206 con la storia; il conto è spiegato in testa a `ROADMAP.md` |
| 17 | Tutte le copie per HOME pronte, roadmap senza «da fare» | Fatto: undici giri in tabella in `ROADMAP.md`, tutte le copie conformi, nessuna da scrivere |
| 18 | Le pendenze del 2026-11-05 | Vedi la voce in `pending.md`; Electivire 15 e Magmortar 14, Anistar, foglio FRLG Seeds e storie giapponesi hanno l'esito scritto lì |
| 19 | Varianti cromatiche dopo Bank, per la fase Switch | Registrato; il Magikarp di Hiroshima, che è per HOME, è prodotto cromatico: la carta 95 ha la cromaticità casuale |
| 20 | Lo spazio di HOME | 2600 su 9000 oggi; 6105 a giri finiti, 6226 con il gruppo FINALE |

## Che cosa contiene la consegna

Il file ha tre parti. La prima riprende uno per uno i 46 eventi dell'Eventdex di Serebii che il 2026-11-05 erano risultati senza una carta della libreria con la stessa specie e lo stesso ID (`_notes/lavoro/serebii-senza-carta-2026-11-05.txt`, ADR-117), e per ciascuno porta una scheda con allenatore, ID, livello, natura, abilità, oggetto, sfera e mosse, più i collegamenti a Serebii, a Bulbapedia e, per alcuni, a Project Pokémon. La seconda è una sequenza di domande e direttive del proprietario, scritte in mezzo alle schede. La terza riguarda la ricerca del seme del Jirachi di Pokémon Channel, il pedigree e le pendenze del 2026-11-05.

Le schede non sono fonti primarie. Gran parte del testo è la risposta della sintesi automatica di un motore di ricerca, che il file stesso marca con «Le risposte dell'AI potrebbero contenere errori», e una parte viene da un altro assistente. Il proprietario le ha raccolte come traccia per la verifica, e lo scrive. Qui le si tratta così: ogni campo di una scheda è un'affermazione da riscontrare sulla pagina che la scheda cita, e la pagina, una volta letta, prevale sulla scheda.

## Le contraddizioni dentro le schede

Le schede si contraddicono fra loro o con la riga di Serebii in undici punti, e sono i punti in cui la verifica deve guardare per primi. Il Pikachu di «Pokémon with You» ha ID 201803 nella riga di Serebii, mentre la scheda dà 201703 e attribuisce 201803 alla campagna del 2018. Il Jirachi del Tanabata del 2016 ha ID 08076 nella prima scheda e 08016 nella seconda e nella riga di Serebii, e le due schede assegnano gli allenatori おりひめ e ひこぼし ai giochi in modo opposto. Il Jirachi del Tanabata del 2018 ha ID 180801 nella prima scheda e 180811 nella seconda e in Serebii. Il Pachirisu di Sejun Park britannico ha ID 5655 nella riga di Serebii, mentre la scheda dice 05165 per l'Europa e 05655 per il Nord America. Il Garchomp di Camilla ha ID 7225 in Serebii, e la scheda attribuisce 07226 alla variante occidentale. Il Pinsir del WCSK14 è dato per Pokémon X, Allegro, con Danzaspada, mentre l'estratto di Serebii nello stesso file dice Y, Adamant, X-Forbice. Due richieste di dettagli, quella sull'Oddish e quella sul Pachirisu, hanno ricevuto la scheda del Charizard di Target, che non c'entra. Il Charizard di Target porta «DanzaSpada (Dragon Dance)», nome italiano e inglese di due mosse diverse; il Tyranitar porta «Terremoto (Sand Stream)», e il Jirachi del Daisuki Club porta «Baccasalak (Salac Berry)» in una scheda e «Baccasalak (Ganlon Berry)» in un'altra. Infine il Mew del Ranch americano ha tre mosse nella prima scheda e quattro nella seconda.

## Il primo riscontro: 24 dei 46 sono già nelle copie

Il confronto del 2026-11-05 cercava una carta con la stessa specie e lo stesso ID, ed è stato il punto debole: quando l'ID di Serebii differisce da quello della carta, l'evento risultava mancante anche se l'esemplare c'era. Il 2026-11-06 l'agente ha cercato ogni evento nei pedigree generati (`pokedex-home-completo/pedigree/HOME*.md`, 5253 righe, tutte le copie) per numero di specie e nome dell'allenatore, preso dalle schede della consegna, senza guardare l'ID. Lo script è nello scratchpad della sessione e l'uscita è riportata qui sotto per intero. È un riscontro e non un giudizio: dice che un esemplare con quella specie e quell'allenatore esiste nelle copie, non che sia la stessa distribuzione. Quando l'ID differisce, va stabilito sulla fonte primaria se si tratta di un errore di Serebii o di una distribuzione distinta.

| Specie | Evento secondo Serebii | ID Serebii | Nelle copie, per allenatore | Esito del riscontro |
|---|---|---|---|---|
| 6 Charizard | I Choose You, Pop-Up Store coreano, 2017 | 170715 | 지우, ID 171215, HOME5 | presente, ID diverso da verificare |
| 23 Ekans | Toys 'R' Us, JEREMY, 2004 | 24680 | nessuno | assente |
| 25 Pikachu | Pokémon with You, Giappone | 201803 | トウホク１８, ID 201803, HOME5; anche トウホク 201703 e altri tre | presente |
| 25 Pikachu | Pokémon Ranch, USA | 1000 | Hayley, ID 1000, HOME6 | presente (ADR-117) |
| 27 Sandshrew | Toonverse, Corea, 2017 | 170503 | 썬문, ID 170502, HOME4 | presente, ID diverso da verificare |
| 27 Sandshrew | Toys 'R' Us, JEREMY, 2004 | 13579 | nessuno con JEREMY | assente |
| 37 Vulpix | Toys 'R' Us, JEREMY, 2004 | 13579 | nessuno | assente |
| 43 Oddish | Toys 'R' Us, JEREMY, 2004 | 24680 | nessuno | assente |
| 54 Psyduck | Toys 'R' Us, JEREMY, 2004 | 24680 | nessuno | assente |
| 58 Growlithe | Toys 'R' Us, JEREMY, 2004 | 24680 | nessuno | assente |
| 67 Machoke | Toys 'R' Us, JEREMY, 2004 | 24680 | nessuno | assente |
| 68 Machamp | Campionati nazionali nordamericani, 2016 | 7016 | ScreenPeekaz, ID 5146, HOME2 e HOME3 | presente, ID diverso da verificare |
| 79 Slowpoke | Toys 'R' Us, JEREMY, 2004 | 13579 | nessuno | assente |
| 90 Shellder | Toys 'R' Us, JEREMY, 2004 | 24680 | nessuno | assente |
| 93 Haunter | Toys 'R' Us, JEREMY, 2004 | 24680 | nessuno | assente |
| 94 Gengar | Natale del Pokémon Center e di Toys 'R' Us, Giappone, 2013 | 12213 | nessuno con クリスマス | assente |
| 120 Staryu | Toys 'R' Us, JEREMY, 2004 | 13579 | nessuno | assente |
| 127 Pinsir | Qualificazioni coreane WCS 2014 | 7064 | WCS14K, ID 7054, HOME3 | presente, ID diverso da verificare |
| 128 Tauros | Toys 'R' Us, JEREMY, 2004 | 13579 | nessuno | assente |
| 129 Magikarp | Daisuki Club, 2007 | 1256 | nessuno | assente |
| 129 Magikarp | Daisuki Club, 2007 | 2226 | nessuno | assente |
| 129 Magikarp | Daisuki Club, 2007 | 3126 | nessuno | assente |
| 129 Magikarp | Daisuki Club, 2007 | 7076 | nessuno | assente |
| 129 Magikarp | Daisuki Club, 2007 | 12226 | nessuno | assente |
| 133 Eevee | Lalaport Toyosu, 2013 | 7133 | キヨ, ID 37379, HOME2 e HOME8 | presente, ID diverso da verificare |
| 151 Mew | Pokémon Ranch, USA | 1000 | Hayley, ID 1000, HOME6 | presente (ADR-117) |
| 151 Mew | Pokémon Ranch, Giappone | 1000 | ユカリ, ID 1000, HOME6 | presente (ADR-117) |
| 212 Scizor | Natale del Pokémon Center e di Toys 'R' Us, Giappone, 2013 | 12213 | nessuno con クリスマス | assente |
| 248 Tyranitar | Qualificazioni coreane WCS 2014 | 7064 | WCS14K, ID 7054, HOME3 | presente, ID diverso da verificare |
| 310 Manectric | Qualificazioni coreane WCS 2014 | 7064 | WCS14K, ID 7054, HOME3 | presente, ID diverso da verificare |
| 381 Latios | Decimo anniversario, Germania, 2006 | 6277 | 10JAHRE, ID 6227, HOME1 | presente, ID diverso da verificare |
| 385 Jirachi | Tanabata di Tohoku, 2018 | 180811 | たなばた, ID 180801, HOME5 e HOME7 | presente, ID come nella prima scheda |
| 385 Jirachi | Tanabata di Tohoku, 2016, Rubino Omega e Zaffiro Alpha | 8016 | おりひめ e ひこぼし, ID 8076, HOME3 | presenti tutte e due le varianti, ID come nella prima scheda |
| 385 Jirachi | Tanabata di Tohoku, 2016, X e Y | 8016 | come sopra | presenti tutte e due le varianti |
| 385 Jirachi | Daisuki Club, 2007 | 7078 | タナバタ, ID 7077, HOME1, due esemplari; nessuno con 7078 | variante 7077 presente, variante 7078 assente |
| 396 Starly | Daisuki Club Party, 2008 | 8311 | nessuno | assente |
| 399 Bidoof | Daisuki Club Party, 2008 | 17336 | nessuno | assente |
| 417 Pachirisu | Sejun Park, Nord America, 2015 | 5655 | 박세준, ID 5165, HOME2 e HOME3; anche ID 4045 e 11154 | ID 5655 assente, da stabilire se esiste |
| 417 Pachirisu | Sejun Park, Regno Unito, 2015 | 5655 | come sopra | come sopra |
| 445 Garchomp | Sinnoh Classic, Giappone, 2016 | 7225 | シロナ, ID 7226, HOME3 | ID 7225 assente, da stabilire se esiste |
| 489 Phione | Pokémon Ranch, USA | 1000 | Hayley, ID 1000, HOME6 | presente (ADR-117) |
| 489 Phione | Pokémon Ranch, Giappone | 1000 | ユカリ, ID 1000, HOME6 | presente (ADR-117) |
| 491 Darkrai | Toys 'R' Us e Nintendo World, USA, 2008 | 6281 | ALAMOS con ID 5318, 7038 (sei esemplari) e 10308, HOME1 | ID 6281 assente, da stabilire se esiste |
| 700 Sylveon | Prevendita del film, Corea, 2014 | 4124 | 이브이하우스, ID 12013, HOME3 | presente, ID diverso da verificare |
| 716 Xerneas | XY&Z, Corea, 2016 | 4206 | XY&Z, ID 3226, HOME3 | presente, ID diverso da verificare |
| 788 Tapu Fini | Campionati giapponesi 2019 | 190419 | ポニ, ID 190419, HOME5; anche Poni 190524 | presente |

Il conto, sul perimetro di questa tabella: 22 righe assenti con certezza, cioè i dodici di JEREMY, il Gengar e lo Scizor di Natale, i cinque Magikarp del Daisuki Club, lo Starly e il Bidoof del Daisuki Club Party e la variante 7078 del Jirachi del Daisuki Club. Quattro righe dipendono da un ID che le copie non hanno e che va confermato sulla fonte prima di produrlo: le due del Pachirisu con 5655, il Garchomp con 7225 e il Darkrai con 6281. Le altre 20 sono presenti; dieci hanno un ID diverso da quello di Serebii, e i tre Jirachi del Tanabata hanno l'ID della prima scheda della consegna invece di quello di Serebii.

Le sei controparti del WCS 2014 coreano su cui il proprietario chiede conferma sono tutte nelle copie, dalle carte della libreria: Pinsir, Tyranitar e Manectric per X, Heracross, Houndoom e Aggron per Y, con allenatore WCS14K, ciascuna in HOME3 e le tre di Y anche in una copia di Rubino Omega in lingua giapponese. Il Latios e il Latias del decimo anniversario ci sono nelle edizioni tedesca (10JAHRE) e italiana (10ANNI), in HOME1. Le due varianti del Jirachi del Tanabata del 2016 ci sono entrambe.

## Le direttive del proprietario contenute nella consegna

| N. | Direttiva | Chi agisce | Quando |
|---|---|---|---|
| 1 | Le fonti esistono e vanno conosciute: ogni collegamento della consegna entra nel registro delle fonti, si legge, e le fonti che mancano si aggiungono alla lista completa | agente | prima della prossima produzione |
| 2 | Verificare e produrre conformi i 46 eventi, uno per uno; il proprietario dà per scontato che siano le sole lacune di questo tipo, e l'agente deve confermarlo o smentirlo con una misura | agente | prima di Bank |
| 3 | Le varianti con allenatore o ID diversi si tengono tutte, se c'è spazio: le due del Tanabata del 2016 (ci sono) e le due del Jirachi del Daisuki Club, 07077 e 07078 | agente | prima di Bank |
| 4 | Il Daisuki Club può avere altri eventi oltre a quelli elencati, come Heracross, Bidoof o Shinx: leggere le pagine «minidaisukis», «gamefreak-psyduck», «daisuki-goes-platinum» e «magikarp-of-love» di Pokémon Historian | agente | prima di Bank |
| 5 | Pokémon Historian si esplora per intero, ogni sottosezione che porti a un Pokémon come dato di gioco in una cartuccia, non solo l'indice degli eventi | agente | prima di Bank |
| 6 | Project Pokémon, l'archivio dei file, si analizza per intero | agente | prima di Bank |
| 7 | pocketmonsters.net, l'elenco degli eventi, si spulcia per intero come doppio controllo della completezza | agente | prima di Bank |
| 8 | Bulbapedia si legge per intero nelle sue liste per generazione e per regione | agente | prima di Bank |
| 9 | Il filo di PokéCommunity «My events legit» si valuta come forum storico e fonte di riscontro | agente | prima di Bank |
| 10 | Confermare che le controparti speculari dei WCS 2014 coreani ci sono | agente | fatto il 2026-11-06, sopra |
| 11 | Il Latios tedesco va col lotto del decimo anniversario, dove c'è anche la controparte italiana | agente | fatto il 2026-11-06, sopra |
| 12 | Se generiamo eventi che PKHeX non conosce, possiamo contribuire allo sviluppo di PKHeX? | agente risponde | prossimo giro |
| 13 | Serebii è considerato la fonte più completa: confermare che lo si è spulciato a fondo e che tutti gli eventi destinati a HOME prima di Bank sono censiti | agente | prima di Bank |
| 14 | Ciò che resta fuori dai lotti iniettati sono comunque Pokémon da possedere, e si censisce nella fase Switch | agente | dopo Bank |
| 15 | Il Jirachi di Channel e il WISHMKR: interessano gli esemplari originali distribuibili, non un sostituto potenziato con tappi o menta; l'obiettivo sono tutti i Pokémon mai esistiti | agente | prima di Bank |
| 16 | Ogni riga del pedigree deve avere la storia; spiegare perché le impronte sono 5253 quando il totale dei Pokémon era più di 7000 | agente | prossimo giro |
| 17 | Priorità alle copie per HOME ancora da fare, in ordine, perché il proprietario deve avere tutte le copie disponibili per i giri prima di Bank; la roadmap del fuoco corrente si allinea senza nessun «da fare» rimasto | agente | adesso |
| 18 | Le pendenze del 2026-11-05 (46 eventi, Electivire 15 e Magmortar 14, Anistar, foglio FRLG Seeds, storie degli allenatori giapponesi) si risolvono, senza che il proprietario debba tornarci | agente | prima di Bank |
| 19 | Le varianti cromatiche degli eventi si controllano tutte, ma dopo la chiusura di Bank (direttiva in chat del 2026-11-06) | agente | dopo Bank |
| 20 | Lo spazio totale di HOME si sorveglia a ogni giro (direttiva in chat del 2026-11-06) | agente | sempre |

## Il Magikarp di Hiroshima

Il proprietario ha visto nel giro 3 il Magikarp con Splash, Auguri e Cuccagna. Nelle copie ce ne sono due, HOME3 box 20 posti 13 e 14, dalla carta 95 della libreria («ひろしまの コイキング»), entrambi non cromatici. Resta da stabilire sulla fonte se la versione cromatica sia una distribuzione distinta o la stessa carta con cromaticità libera, e quindi se vada prodotta come esemplare a sé. Il controllo generale delle varianti cromatiche è rinviato a dopo Bank (direttiva 19); questo caso è registrato perché il proprietario lo ha visto in un lotto per HOME.

## Le fonti della consegna

La consegna contiene 69 indirizzi distinti, estratti con un'espressione regolare sul testo e salvati in `_notes/fonti/consegne/2026-11-06-retrogame/url-estratti.txt`. Trentatré erano già nominati nel registro o nei documenti del progetto (ricerca della stringa senza schema in `SOURCES.md`, `docs/`, `pokedex-home-completo/` e `recreate-pokemon-distributions-events/`), per lo più le pagine dell'Eventdex di Serebii; gli altri trentasei sono nuovi. Tutti sono registrati in `SOURCES.md` con lo stato di lettura. Nessuno è stato letto in questo giro, che ha assorbito la consegna e non ha aperto pagine web.
