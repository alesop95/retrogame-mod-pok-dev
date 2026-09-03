# Schede degli esemplari da evento di prima e seconda generazione

> Documento generato da `tools/genera-evento-gb.py`. Non si modifica a mano, e non legge i file prodotti: ricalcola gli esemplari dalle tabelle della fonte con il medesimo codice che li scrive.

Il documento porta due cose di natura diversa e le tiene separate. Il racconto di ciascun evento è letto da un file autorato e citato, e dove una fonte non esiste lo dichiara invece di riempire il campo per ipotesi; i dati tecnici di ciascun esemplare sono calcolati dalle tabelle della fonte e dalle formule, e sono verificabili uno per uno. Il racconto sta una volta per gruppo e non una volta per esemplare, perché centotrentasei delle centosessantotto voci vengono dal medesimo luogo e ripeterlo seppellirebbe la parte che varia sotto quella che non varia.

Una avvertenza sui valori individuali, che è un risultato e non un limite dello strumento. In queste due generazioni non esiste alcun valore di personalità: i valori individuali furono estratti dal gioco al momento della consegna e non derivano da nulla che l'esemplare porti con sé. La fedeltà su quel campo non è quindi decidibile nemmeno in principio, al contrario della terza generazione dove il seme la determina. Ogni scheda dichiara se i propri valori individuali siano un dato della fonte, un vincolo della cromaticità dichiarata, oppure una scelta nostra: i primi due casi sono verificabili, il terzo no.

## Esemplari premio di Pokemon Stadium

Generazione 1, donatore dichiarato dalla fonte come Stadium. Il gruppo porta 9 voci e 9 specie distinte.

Quando: legate alla vita commerciale del gioco su console domestica, e non dichiarate come intervallo da alcuna delle due fonti. Dove: Nord America, Europa e Australia per la versione internazionale, Giappone per quella con identificativo millenovecentonovantanove. Come: premio consegnato dal gioco su console domestica alla cartuccia portatile collegata, uno estratto a sorte per ciascuna vittoria sul Castello dei Capipalestra e sui Superquattro.

Sono i nove esemplari che il gioco su console domestica consegnava alla cartuccia collegata: i tre iniziali al livello cinque, i due combattenti di Kanto al venti, un Eevee al venticinque, i due fossili al venti, e un Psyduck al quindici che sta a parte. Otto erano premi del Castello dei Capipalestra, estratti a sorte uno per vittoria; il Psyduck no, ed è il pezzo migliore del gruppo, perché si otteneva riempiendo l'albo dei campioni con tutte e centocinquantuno le specie. Era il premio del Pokedex completo, e conosce Amnesia al livello quindici. Due campi tradiscono la loro provenienza, e il secondo ha la storia migliore. Il primo è l'allenatore, perché è l'unico caso di prima generazione in cui nome e identificativo non appartengono a chi riceve: il nome è quello del gioco tradotto in ciascuna lingua, in italiano STADIO, con identificativo duemila sulle versioni internazionali e millenovecentonovantanove su quella giapponese. Il secondo è il byte che di norma porta il tasso di cattura della specie e che qui porta invece uno di due valori fissi, centosessantasette o centosessantotto, che sono gli identificativi della Scatola Normale e della Scatola Splendida: la confezione in cui il premio veniva consegnato, la prima al primo giro e la seconda al secondo. Il Psyduck pretende la Splendida, cioè il premio più difficile arrivava nella scatola migliore. Quel byte, passando alla seconda generazione, diventa il byte dell'oggetto tenuto: un premio di Stadium arriva in Johto tenendo in mano la propria scatola. Su questo gruppo il progetto ha imparato una cosa a proprie spese il 2026-09-03: avevamo scritto il tasso della specie invece della scatola, e su Bulbasaur il difetto non si vedeva perché esiste un incontro statico che lo accetta e il verificatore ha scelto quello, dichiarando la voce legale con la provenienza sbagliata, mentre sulle sei voci senza alternativa statica non ha trovato corrispondenza. Una voce legale può nascondere un difetto che si manifesta soltanto sulle voci vicine.

Pagina che descrive l'evento: <https://bulbapedia.bulbagarden.net/wiki/List_of_game-based_Pok%C3%A9mon_distributions_in_Generation_I>.

Fonti: [PKHeX, template degli eventi di prima generazione](https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Legality/Encounters/Templates/Gen1/EncounterGift1.cs), letta il 2026-09-03; [Bulbapedia, distribuzioni da gioco in prima generazione](https://bulbapedia.bulbagarden.net/wiki/List_of_game-based_Pok%C3%A9mon_distributions_in_Generation_I), letta il 2026-09-03.

Divergenza fra le fonti: La fonte secondaria attribuisce l'identificativo millenovecentonovantanove alla versione giapponese di Pokemon Stadium 2, che è il gioco uscito in Occidente come primo Stadium: la numerazione dei titoli su console domestica differisce fra i mercati, e chiamarli per numero senza dichiarare quale mercato produce confusione.

### EVT-1-0000 Bulbasaur

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 1 | tabella degli eventi |
| identificativo interno | 153 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 22 e 3 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 21, atk 11, def 11, spd 11, spc 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |

### EVT-1-0001 Charmander

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 4 | tabella degli eventi |
| identificativo interno | 176 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Ruggito (45) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 20 e 20 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 20, atk 11, def 10, spd 13, spc 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |

### EVT-1-0002 Squirtle

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 7 | tabella degli eventi |
| identificativo interno | 177 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Colpocoda (39) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 21 e 21 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 20, atk 11, def 13, spd 10, spc 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |

### EVT-1-0003 Psyduck

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 54 | tabella degli eventi |
| identificativo interno | 47 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 15 | tabella degli eventi |
| mosse | Graffio (10), Amnesia (133) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20 | tabella dei punti potenza di base |
| esperienza | 3375 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 21 e 21 | tabella delle statistiche di base |
| tasso di cattura | 190 | tabella delle statistiche di base |
| statistiche | max_hp 44, atk 25, def 23, spd 26, spc 24 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |

### EVT-1-0004 Hitmonlee

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 106 | tabella degli eventi |
| identificativo interno | 43 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 20 | tabella degli eventi |
| mosse | Doppiocalcio (24), Meditazione (96) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 40 | tabella dei punti potenza di base |
| esperienza | 8000 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 1 e 1 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 56, atk 59, def 32, spd 45, spc 25 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |

### EVT-1-0005 Hitmonchan

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 107 | tabella degli eventi |
| identificativo interno | 44 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 20 | tabella degli eventi |
| mosse | Cometapugno (4), Agilità (97) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 30 | tabella dei punti potenza di base |
| esperienza | 8000 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 1 e 1 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 56, atk 53, def 42, spd 41, spc 25 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |

### EVT-1-0006 Eevee

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 133 | tabella degli eventi |
| identificativo interno | 102 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 25 | tabella degli eventi |
| mosse | Azione (33), Colpocoda (39) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30 | tabella dei punti potenza di base |
| esperienza | 15625 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 0 e 0 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 70, atk 40, def 37, spd 40, spc 45 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |

### EVT-1-0007 Omanyte

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 138 | tabella degli eventi |
| identificativo interno | 98 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 20 | tabella degli eventi |
| mosse | Pistolacqua (55), Ritirata (110) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 40 | tabella dei punti potenza di base |
| esperienza | 8000 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 5 e 21 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 50, atk 27, def 51, spd 25, spc 47 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |

### EVT-1-0008 Kabuto

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 140 | tabella degli eventi |
| identificativo interno | 90 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 20 | tabella degli eventi |
| mosse | Graffio (10), Rafforzatore (106) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30 | tabella dei punti potenza di base |
| esperienza | 8000 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 5 e 21 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 48, atk 43, def 47, spd 33, spc 29 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |

## Mew dei tour internazionali

Generazione 1, donatore dichiarato dalla fonte come tour europeo. Il gruppo porta 1 voci e 1 specie distinte.

Quando: dal novembre 1999 alla primavera 2001, in una dozzina di eventi distinti. Dove: Stati Uniti, Canada, Regno Unito, Irlanda, Danimarca, Norvegia, Svezia, Finlandia, Austria. Come: consegnato sul posto da una macchina di distribuzione, con il nome dell'allenatore che identifica l'evento o la postazione.

Il nome che la fonte tecnica dà a questo gruppo, cioè tour europeo, ne sottostima la portata, e la scoperta vale registrarla perché mostra come si legge una fonte di quel tipo. La verifica dell'autenticità non poggia su un identificativo, che non è fissato, ma sull'appartenenza del nome dell'allenatore a un elenco chiuso di diciannove valori, e quell'elenco è il documento dell'evento. Confrontato con la fonte enciclopedica, l'elenco si scompone in una dozzina di distribuzioni su tre continenti. I nomi con Yoshi e Bowser appartengono ai negozi di giocattoli statunitensi del dicembre 1999 e canadesi del gennaio 2000, e alla rivista ufficiale fra il novembre 1999 e il gennaio 2000. I nomi con Link e Luigi appartengono al tour degli stadi negli Stati Uniti, fra il 5 febbraio e il 9 aprile 2000, e alla sua tappa canadese di marzo. I nomi dei paesi, cioè Svezia, Norvegia, Finlandia, Danimarca, Austria e Regno Unito, appartengono a eventi nazionali fra l'estate 2000 e la primavera 2001, fra cui il campionato britannico e irlandese e il tour norvegese che durò più di sei mesi. Il dettaglio tecnico che li distingue è che i valori individuali non sono liberi: la fonte li fissa, e la fonte enciclopedica riporta gli stessi valori con parole diverse, cioè cinque punti salute, dieci attacco, uno difesa, dodici velocità e cinque speciale. Ne segue che su questo gruppo la fedeltà di una ricreazione è verificabile, che nel resto di queste due generazioni non è vero. Il progetto ha inoltre una conferma incrociata che vale come prova della lettura: in prima generazione il valore dei punti salute non è indipendente ma si ricava dagli altri quattro, e con questa assegnazione il derivato vale cinque, cioè esattamente il valore che entrambe le fonti dichiarano, mentre una lettura diversa dei sei numeri lo farebbe valere dieci.

Pagina che descrive l'evento: <https://bulbapedia.bulbagarden.net/wiki/List_of_European_language_event_Pok%C3%A9mon_distributions_in_Generation_I>.

Fonti: [PKHeX, template degli eventi di prima generazione](https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Legality/Encounters/Templates/Gen1/EncounterGift1.cs), letta il 2026-09-03; [Bulbapedia, distribuzioni in lingue europee in prima generazione](https://bulbapedia.bulbagarden.net/wiki/List_of_European_language_event_Pok%C3%A9mon_distributions_in_Generation_I), letta il 2026-09-03.

Divergenza fra le fonti: La fonte enciclopedica riporta una distribuzione spagnola del luglio 2000 con valori individuali diversi, cioè due, sei, quattro, tre e otto, e nomi di allenatore che comprendono D-J. La tabella tecnica porta un solo insieme di valori individuali per questo tipo, quindi non copre quella variante: un esemplare autentico di quella distribuzione non corrisponderebbe alla voce, e il progetto non lo produce.

### EVT-1-0009 Mew

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 151 | tabella degli eventi |
| identificativo interno | 21 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 10, difesa 1, velocità 12, speciale 5, punti salute 5 | fissati dalla fonte |
| tipi | 24 e 24 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 25, atk 16, def 15, spd 16, spc 15 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | YOSHIRA, identificativo 6000 | la fonte accetta diciannove nomi per il tour europeo e non fissa alcun identificativo: si sceglie il primo dell'elenco, e l'identificativo è una scelta nostra dichiarata e non un dato |
| restrizione di lingua | internazionale | tabella degli eventi |

## Mew delle manifestazioni giapponesi

Generazione 1, donatore dichiarato dalla fonte come tour giapponese. Il gruppo porta 1 voci e 1 specie distinte.

Quando: 22-24 novembre 1997, 7 dicembre 1997 - 15 febbraio 1998, 27-29 agosto 1999. Dove: Makuhari Messe a Chiba, e i palazzetti di Fukuoka, Chiba, Osaka, Sapporo e Nagoya. Come: consegnato sul posto, con il nome dell'allenatore che identifica la manifestazione o la città della tappa.

È il gruppo di cui la fonte tecnica dichiara le date, e le dichiara nei propri commenti accanto ai nomi degli allenatori: tre eventi distinti vivono dentro un solo valore di un byte, e si separano soltanto guardando quali nomi il verificatore accetti. I sei nomi dei personaggi Nintendo, cioè Mario, Bowser, Luigi, Peach, Yoshi e Donkey, appartengono allo Space World del 22-24 novembre 1997, tenuto al Makuhari Messe di Chiba. I cinque nomi di città, cioè Fukuoka, Tokyo, Osaka, Sapporo e Nagoya, appartengono alla coppa itinerante della fiera dell'hobby fra il 7 dicembre 1997 e il 15 febbraio 1998, e la fonte enciclopedica ne dà le tappe una per una: Fukuoka il 7 dicembre, Chiba il 10 e 11 gennaio, Osaka il primo febbraio, Sapporo l'8 e Nagoya il 15. Il nome Makuhari appartiene invece allo Space World dell'agosto 1999, ed è il quartiere di Chiba dove quelle fiere si tenevano. Su quest'ultima attribuzione vale una nota di prudenza, perché la coppa itinerante fece tappa proprio al Makuhari Messe e il nome potrebbe sembrare suo: la fonte enciclopedica non elenca Makuhari fra i nomi di quella coppa, che usa i nomi delle città, e la fonte tecnica lo attribuisce esplicitamente allo Space World del 1999, quindi le due si accordano e l'accordo è la ragione per cui l'attribuzione si può scrivere. I valori individuali sono gli stessi del gruppo internazionale e sono fissati.

Pagina che descrive l'evento: <https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_I>.

Fonti: [PKHeX, template degli eventi di prima generazione](https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Legality/Encounters/Templates/Gen1/EncounterGift1.cs), letta il 2026-09-03; [Bulbapedia, distribuzioni giapponesi in prima generazione](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_I), letta il 2026-09-03.

### EVT-1-0010 Mew

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 151 | tabella degli eventi |
| identificativo interno | 21 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 10, difesa 1, velocità 12, speciale 5, punti salute 5 | fissati dalla fonte |
| tipi | 24 e 24 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 25, atk 16, def 15, spd 16, spc 15 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | マクハリ, identificativo 6000 | nome dello Space World '99 di Makuhari, primo dell'elenco giapponese della fonte; l'identificativo è una scelta nostra |
| restrizione di lingua | giapponese | tabella degli eventi |

## Uova misteriose dei Pokemon Center giapponesi

Generazione 2, donatore dichiarato dalla fonte come destinatario. Il gruppo porta 15 voci e 12 specie distinte.

Quando: 15 dicembre 2001 - 14 gennaio 2002, 16 marzo - 7 aprile 2002, 27 aprile - 12 maggio 2002. Dove: negozi Pokemon Center di Tokyo e Osaka. Come: consegnata al negozio, una sola per visitatore e con la specie estratta a sorte, con il nome e l'identificativo di chi la riceve.

Questo era l'ultimo gruppo di prima e seconda generazione senza provenienza, e il 2026-09-03 è stato chiuso. La fonte tecnica lo classifica come consegnato al destinatario e non dichiara nome, data né luogo; la fonte enciclopedica lo identifica come le uova misteriose distribuite nei negozi Pokemon Center di Tokyo e Osaka in tre campagne fra il dicembre 2001 e il maggio 2002. La conferma non poggia sul nome ma sul conto e sui dettagli: le tre campagne portano rispettivamente sei, sei e cinque specie, le specie coincidono con le nostre, e coincidono anche le mosse, che sono la parte diagnostica. Il visitatore riceveva una sola uova con la specie estratta a sorte, il che spiega perché le voci siano quindici e non tre. Il marcatore che permette di attribuire ciascuna voce alla propria campagna è una mossa: la seconda campagna assegnò Petalodanza a quasi tutte le proprie uova, e quella mossa non compare nelle altre due. Le voci con Petalodanza sono dunque della seconda campagna, quelle con Ripeti, Panciamburo o Metronomo della prima, e quelle con Forzantica, Sgranocchio, Sottomissione e Ombra Notturna della terza; la sezione delle voci di questo file porta l'attribuzione una per una. Due avvertenze sull'accordo fra le due fonti, che non è perfetto e va dichiarato. La prima campagna comprendeva secondo l'enciclopedia anche un Chikorita con due mosse sole, che la tabella tecnica non porta; e il Pichu con Canto compare identico nella prima e nella terza campagna, quindi la nostra voce corrispondente appartiene a entrambe e non è attribuibile a una sola. Ne segue che quindici voci coprono diciassette consegne storiche, perché due coincidono nei byte.

Pagina che descrive l'evento: <https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_(Generation_II)>.

Fonti: [PKHeX, template degli eventi di seconda generazione](https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Legality/Encounters/Templates/Gen2/EncounterGift2.cs), letta il 2026-09-03; [Bulbapedia, distribuzioni giapponesi in seconda generazione](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_(Generation_II)), letta il 2026-09-03.

### EVT-2-0142 Chikorita

Attribuzione di questa voce: seconda campagna, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 152 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 20 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 13, spd 11, satk 11, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0143 Pichu

Attribuzione di questa voce: prima campagna, 15 dicembre 2001 - 14 gennaio 2002, e terza campagna, 27 aprile - 12 maggio 2002. Il marcatore che la distingue è Canto, identico nelle due campagne, quindi la voce appartiene a entrambe e non è attribuibile a una sola.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Tuonoshock (84), Fascino (204), Canto (47) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 20, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 18, atk 10, def 8, spd 12, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0144 Cleffa

Attribuzione di questa voce: prima campagna, 15 dicembre 2001 - 14 gennaio 2002. Il marcatore che la distingue è Ripeti, senza Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 173 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Fascino (204), Ripeti (227), Comete (129) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20, 5, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 9, spd 8, satk 11, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0145 Wooper

Attribuzione di questa voce: prima campagna, 15 dicembre 2001 - 14 gennaio 2002. Il marcatore che la distingue è Panciamburo, che compare in questa sola voce.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 194 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Pistolacqua (55), Colpocoda (39), Panciamburo (187) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 30, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 11, def 11, spd 8, satk 9, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0146 Phanpy

Attribuzione di questa voce: prima campagna, 15 dicembre 2001 - 14 gennaio 2002. Il marcatore che la distingue è Ripeti, senza Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 231 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Ripeti (227) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 5 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 25, atk 12, def 12, spd 10, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0147 Smoochum

Attribuzione di questa voce: prima campagna, 15 dicembre 2001 - 14 gennaio 2002. Il marcatore che la distingue è Metronomo, che compare in questa sola voce.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 238 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Leccata (122), Metronomo (118) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 8, spd 13, satk 15, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0148 Psyduck

Attribuzione di questa voce: seconda campagna, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 54 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Colpocoda (39), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 11, spd 12, satk 13, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0149 Pichu

Attribuzione di questa voce: seconda campagna, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Tuonoshock (84), Fascino (204), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 20, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 18, atk 10, def 8, spd 12, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0150 Cleffa

Attribuzione di questa voce: seconda campagna, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 173 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Fascino (204), Ripeti (227), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20, 5, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 9, spd 8, satk 11, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0151 Igglybuff

Attribuzione di questa voce: seconda campagna, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza, con Ricciolscudo che l'enciclopedia riporta per questa specie.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 174 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Canto (47), Fascino (204), Ricciolscudo (111), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 20, 40, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 25, atk 9, def 8, spd 8, satk 10, sdef 8 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0152 Smoochum

Attribuzione di questa voce: seconda campagna, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 238 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Leccata (122), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 8, spd 13, satk 15, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0153 Bulbasaur

Attribuzione di questa voce: terza campagna, 27 aprile - 12 maggio 2002. Il marcatore che la distingue è Forzantica.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 1 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Forzantica (246) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 5 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 11, spd 11, satk 13, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0154 Charmander

Attribuzione di questa voce: terza campagna, 27 aprile - 12 maggio 2002. Il marcatore che la distingue è Sgranocchio.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 4 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Ruggito (45), Sgranocchio (242) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 15 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 10, spd 13, satk 12, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0155 Totodile

Attribuzione di questa voce: terza campagna, 27 aprile - 12 maggio 2002. Il marcatore che la distingue è Sottomissione.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 158 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Fulmisguardo (43), Sottomissione (66) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 25 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 13, def 12, spd 10, satk 10, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0156 Hoothoot

Attribuzione di questa voce: terza campagna, 27 aprile - 12 maggio 2002. Il marcatore che la distingue è Ombra Notturna.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 163 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Ombra Notturna (101) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 9, def 9, spd 11, satk 10, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| restrizione di lingua | giapponese | tabella degli eventi |

## Esemplari premio di Pokemon Stadium 2, versione giapponese

Generazione 2, donatore dichiarato dalla fonte come Stadium giapponese. Il gruppo porta 2 voci e 2 specie distinte.

Quando: non dichiarate da alcuna delle due fonti. Dove: dentro il gioco, su console domestica, in Giappone. Come: premio consegnato dal gioco su console domestica alla cartuccia portatile collegata.

Due esemplari soli, ed entrambi portano una mossa che la specie non avrebbe. Il primo è un Farfetch'd al livello cinque che conosce Staffetta, Danzaspada, Agilità e Lacerazione, e la fonte enciclopedica segnala che Staffetta era indisponibile a quella specie in seconda generazione: la sola presenza di quella mossa dichiara da dove l'esemplare venga. Il secondo è un Gligar al livello cinque che conosce Terremoto, Contrattacco e Attacco d'Ala, e Terremoto su quella specie era una mossa distribuita di rado. Una mossa impossibile, in questo dominio, è un certificato di origine: non è un difetto dei dati ma la firma dell'evento. Entrambi portano il luogo di cattura centoventisette, che è il valore riservato agli eventi.

Pagina che descrive l'evento: <https://bulbapedia.bulbagarden.net/wiki/List_of_game-based_Pok%C3%A9mon_distributions_in_Generation_II>.

Fonti: [PKHeX, template degli eventi di seconda generazione](https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Legality/Encounters/Templates/Gen2/EncounterGift2.cs), letta il 2026-09-03; [Bulbapedia, distribuzioni da gioco in seconda generazione](https://bulbapedia.bulbagarden.net/wiki/List_of_game-based_Pok%C3%A9mon_distributions_in_Generation_II), letta il 2026-09-03.

Divergenza fra le fonti: La fonte enciclopedica attribuisce al Gligar quattro mosse, cioè Terremoto, Velenospina, Contrattacco e Attacco d'Ala, mentre la tabella tecnica ne porta tre e omette Velenospina. Il progetto segue la tabella tecnica, e la ragione non è una gerarchia astratta fra le due fonti: è che quella tabella appartiene al verificatore che giudicherà i nostri esemplari, quindi è la sua nozione di corretto a determinare se un esemplare sarà accettato. La divergenza resta registrata perché se un giorno il verificatore aggiungesse quella mossa la nostra voce diventerebbe sbagliata senza che nulla lo segnali.

### EVT-2-0000 Farfetch’d

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 83 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Staffetta (226), Danzaspada (14), Agilità (97), Lacerazione (163) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 30, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 21, atk 13, def 12, spd 12, satk 12, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | スタジアム, identificativo 2000 | nome e identificativo fissati dalla fonte per la versione giapponese |
| restrizione di lingua | giapponese | tabella degli eventi |

### EVT-2-0001 Gligar

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 207 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Terremoto (89), Contrattacco (68), Attacco d’Ala (17) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 10, 20, 35 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 17, spd 15, satk 10, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | スタジアム, identificativo 2000 | nome e identificativo fissati dalla fonte per la versione giapponese |
| restrizione di lingua | giapponese | tabella degli eventi |

## Esemplari premio di Pokemon Stadium 2, versione inglese

Generazione 2, donatore dichiarato dalla fonte come Stadium inglese. Il gruppo porta 2 voci e 2 specie distinte.

Quando: non dichiarate da alcuna delle due fonti. Dove: Nord America, Europa e Australia. Come: premio consegnato dal gioco su console domestica alla cartuccia portatile collegata.

Gli stessi due esemplari del gruppo giapponese, con il nome dell'allenatore nella forma inglese e l'identificativo duemila. La ragione per cui la fonte tiene i tre gruppi separati non è il contenuto ma l'identità dell'allenatore, che cambia con la lingua e che il verificatore controlla: un Farfetch'd con il nome giapponese su una cartuccia inglese non è un esemplare più raro ma un esemplare sbagliato.

Pagina che descrive l'evento: <https://bulbapedia.bulbagarden.net/wiki/List_of_game-based_Pok%C3%A9mon_distributions_in_Generation_II>.

Fonti: [PKHeX, template degli eventi di seconda generazione](https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Legality/Encounters/Templates/Gen2/EncounterGift2.cs), letta il 2026-09-03; [Bulbapedia, distribuzioni da gioco in seconda generazione](https://bulbapedia.bulbagarden.net/wiki/List_of_game-based_Pok%C3%A9mon_distributions_in_Generation_II), letta il 2026-09-03.

### EVT-2-0002 Farfetch’d

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 83 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Staffetta (226), Danzaspada (14), Agilità (97), Lacerazione (163) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 30, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 21, atk 13, def 12, spd 12, satk 12, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Stadium, identificativo 2000 | nome e identificativo fissati dalla fonte per la versione inglese |
| restrizione di lingua | inglese | tabella degli eventi |

### EVT-2-0003 Gligar

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 207 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Terremoto (89), Contrattacco (68), Attacco d’Ala (17) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 10, 20, 35 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 17, spd 15, satk 10, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Stadium, identificativo 2000 | nome e identificativo fissati dalla fonte per la versione inglese |
| restrizione di lingua | inglese | tabella degli eventi |

## Esemplari premio di Pokemon Stadium 2, versioni internazionali non inglesi

Generazione 2, donatore dichiarato dalla fonte come Stadium internazionale. Il gruppo porta 2 voci e 2 specie distinte.

Quando: non dichiarate da alcuna delle due fonti. Dove: Europa continentale. Come: premio consegnato dal gioco su console domestica alla cartuccia portatile collegata.

Gli stessi due esemplari, con il nome dell'allenatore tradotto e l'identificativo duemilauno, che è il solo campo a distinguere questo gruppo dal precedente. La fonte elenca le forme francese, tedesca, italiana e spagnola del nome, e quella italiana è Stadio: è il gruppo che interessa direttamente le cartucce di questo progetto, perché sono italiane.

Pagina che descrive l'evento: <https://bulbapedia.bulbagarden.net/wiki/List_of_game-based_Pok%C3%A9mon_distributions_in_Generation_II>.

Fonti: [PKHeX, template degli eventi di seconda generazione](https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Legality/Encounters/Templates/Gen2/EncounterGift2.cs), letta il 2026-09-03; [Bulbapedia, distribuzioni da gioco in seconda generazione](https://bulbapedia.bulbagarden.net/wiki/List_of_game-based_Pok%C3%A9mon_distributions_in_Generation_II), letta il 2026-09-03.

### EVT-2-0004 Farfetch’d

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 83 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Staffetta (226), Danzaspada (14), Agilità (97), Lacerazione (163) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 30, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 21, atk 13, def 12, spd 12, satk 12, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Stadio, identificativo 2001 | nome e identificativo fissati dalla fonte per le versioni internazionali non inglesi, qui in italiano |
| restrizione di lingua | internazionale non inglese | tabella degli eventi |

### EVT-2-0005 Gligar

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 207 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Terremoto (89), Contrattacco (68), Attacco d’Ala (17) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 10, 20, 35 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 17, spd 15, satk 10, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Stadio, identificativo 2001 | nome e identificativo fissati dalla fonte per le versioni internazionali non inglesi, qui in italiano |
| restrizione di lingua | internazionale non inglese | tabella degli eventi |

## Distribuzioni del Pokemon Center di New York

Generazione 2, donatore dichiarato dalla fonte come Pokemon Center New York. Il gruppo porta 136 voci e 106 specie distinte.

Quando: dal 16 novembre 2001, data di apertura del negozio. Dove: Pokemon Center di New York, secondo piano. Come: una macchina distributrice fra quattro, una consegna a settimana per visitatore e non più di una al giorno, inserendo la propria cartuccia.

Centotrentasei voci, cioè l'ottantasei per cento di tutti gli eventi di seconda generazione, tutte dallo stesso luogo: il primo e finora unico negozio Pokemon degli Stati Uniti, aperto il 16 novembre 2001. La fonte tecnica ammette quattro nomi di allenatore, da PCNYa a PCNYd, e il progetto aveva congetturato che fossero quattro postazioni oppure quattro periodi. La fonte enciclopedica lo conferma nel primo senso: al secondo piano c'era una postazione chiamata Gotta catch 'em all Station composta da quattro macchine distributrici, e i quattro nomi sono le quattro macchine. È il genere di dettaglio che trasforma un campo di un byte in un luogo fisico. Le regole della consegna erano una a settimana per visitatore e non più di una al giorno se la macchina veniva riavviata, il che spiega la quantità delle voci: centotrentasei esemplari distinti erano una ragione per tornare al negozio ogni settimana. Due fatti della fonte enciclopedica cambiano come si leggono i nostri dati. Il primo è che tutti gli esemplari tranne gli evoluti, i leggendari e i mitici venivano consegnati come uova. Il secondo è che ciascuna distribuzione aveva una probabilità del quindici per cento di essere cromatica, salvo dichiarazione contraria: ne segue che le voci che la tabella tecnica non marca come cromatiche potevano esserlo, quindi la nostra scelta di produrle non cromatiche è una fra due legittime e non la sola. Le sedici che la tabella marca come cromatiche sono invece quelle in cui la cromaticità era garantita, e su quelle la cromaticità vincola quattro valori individuali su cinque: sono le sole voci di questo gruppo su cui la fedeltà sia in parte verificabile. Il contenuto è la parte notevole, perché fra le prime voci compaiono un Mew cromatico, un Celebi con Parassiseme, Confusione, Rintoccasana e Ripresa, i tre leggendari di Johto cromatici e i tre uccelli di Kanto cromatici, oltre a esemplari comuni con assortimenti di mosse costruiti a mano.

Pagina che descrive l'evento: <https://bulbapedia.bulbagarden.net/wiki/List_of_PCNY_event_Pok%C3%A9mon_distributions_in_Generation_II>.

Fonti: [PKHeX, template degli eventi di seconda generazione](https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Legality/Encounters/Templates/Gen2/EncounterGift2.cs), letta il 2026-09-03; [Bulbapedia, distribuzioni del Pokemon Center di New York in seconda generazione](https://bulbapedia.bulbagarden.net/wiki/List_of_PCNY_event_Pok%C3%A9mon_distributions_in_Generation_II), letta il 2026-09-03.

### EVT-2-0006 Mew

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 151 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 25, atk 16, def 16, spd 16, satk 16, sdef 16 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0007 Celebi

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 251 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Parassiseme (73), Confusione (93), Rintoccasana (215), Ripresa (105) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 10, 25, 5, 20 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 26, atk 16, def 16, spd 16, satk 16, sdef 16 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0008 Raikou

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 243 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Fulmisguardo (43), Tuonoshock (84), Boato (46), Attacco Rapido (98) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 30, 20, 30 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 24, atk 15, def 13, spd 17, satk 17, sdef 16 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0009 Entei

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 244 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Fulmisguardo (43), Braciere (52), Boato (46), Turbofuoco (83) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 25, 20, 15 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 27, atk 18, def 14, spd 16, satk 15, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0010 Suicune

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 245 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Fulmisguardo (43), Pistolacqua (55), Boato (46), Raffica (16) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 25, 20, 35 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 25, atk 14, def 17, spd 14, satk 15, sdef 17 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0011 Articuno

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 144 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Nebbia (54), Agilità (97), Leggimente (170), Geloraggio (58) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 30, 5, 10 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 24, atk 15, def 16, spd 14, satk 15, sdef 18 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0012 Zapdos

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 145 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Tuononda (86), Agilità (97), Individua (197), Perforbecco (65) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 30, 5, 20 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 24, atk 15, def 14, spd 16, satk 18, sdef 15 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0013 Moltres

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 146 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Turbofuoco (83), Agilità (97), Resistenza (203), Lanciafiamme (53) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 30, 10, 15 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 24, atk 16, def 15, spd 15, satk 18, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0014 Venusaur

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 3 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Velenpolvere (77), Sonnifero (79), Foglielama (75), Profumino (230) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 15, 25, 20 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 14, spd 14, satk 16, sdef 16 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0015 Charizard

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 6 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Ira (99), Visotruce (184), Lanciafiamme (53), Attacco d’Ala (17) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 10, 15, 35 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 13, spd 16, satk 16, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0016 Blastoise

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 9 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Pistolacqua (55), Morso (44), Rapigiro (229), Protezione (182) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 25, 40, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 16, spd 13, satk 14, sdef 16 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0017 Mewtwo

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 150 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Psicamisù (244), Divinazione (248), Nebbia (54), Psichico (94) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 10, 15, 30, 10 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 26, atk 17, def 15, spd 19, satk 21, sdef 15 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0018 Ho-Oh

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 250 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Magifuoco (221), Salvaguardia (219), Raffica (16), Ripresa (105) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 5, 25, 35, 20 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 26, atk 19, def 15, spd 15, satk 17, sdef 21 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0019 Lugia

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 249 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Aerocolpo (177), Salvaguardia (219), Raffica (16), Ripresa (105) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 5, 25, 35, 20 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 26, atk 15, def 19, spd 17, satk 15, sdef 21 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0020 Meganium

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 154 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Riflesso (115), Velenpolvere (77), Sintesi (235), Corposcontro (34) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 35, 5, 15 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 16, spd 14, satk 14, sdef 16 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0021 Typhlosion

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 157 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Muro di Fumo (108), Braciere (52), Attacco Rapido (98), Ruotafuoco (172) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 25, 30, 25 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 13, spd 16, satk 16, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0022 Feraligatr

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 160 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Pistolacqua (55), Morso (44), Visotruce (184), Lacerazione (163) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 25, 10, 20 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 24, atk 17, def 16, spd 13, satk 13, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0023 Delibird

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 225 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Regalino (217), Giornopaga (6) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 12, def 11, spd 14, satk 13, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0024 Bulbasaur

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 1 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Forzantica (246) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 5 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 11, spd 11, satk 13, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0025 Charmander

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 4 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Ruggito (45), Sgranocchio (242) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 15 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 10, spd 13, satk 12, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0026 Squirtle

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 7 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Colpocoda (39), Elettrocannone (192) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 5 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 13, spd 10, satk 11, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0027 Chikorita

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 152 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 20 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 13, spd 11, satk 11, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0028 Cyndaquil

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 155 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Fulmisguardo (43), Sdoppiatore (38) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 15 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 10, spd 13, satk 12, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0029 Totodile

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 158 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Fulmisguardo (43), Sottomissione (66) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 25 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 13, def 12, spd 10, satk 10, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0030 Nidoran♀

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 29 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Ruggito (45), Azione (33), Demonbacio (142) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 35, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 11, def 11, spd 10, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0031 Nidoran♀

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 29 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Ruggito (45), Azione (33), Dolcebacio (186) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 35, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 11, def 11, spd 10, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0032 Nidoran♂

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 32 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Fulmisguardo (43), Azione (33), Demonbacio (142) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 35, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 12, def 10, spd 11, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0033 Nidoran♂

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 32 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Fulmisguardo (43), Azione (33), Dolcebacio (186) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 35, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 12, def 10, spd 11, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0034 Bellsprout

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 69 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Frustata (22), Demonbacio (142) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 10, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 14, def 10, spd 10, satk 13, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0035 Bellsprout

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 69 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Frustata (22), Dolcebacio (186) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 10, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 14, def 10, spd 10, satk 13, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0036 Marill

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 183 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ricciolscudo (111), Idropompa (56) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 5 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 8, def 11, spd 10, satk 8, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0037 Yanma

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 193 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Preveggenza (193), Alacciaio (211) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 25 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 13, def 11, spd 16, satk 14, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0038 Dunsparce

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 206 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Ira (99), Ricciolscudo (111), Perforcorno (32) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 40, 5 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 26, atk 13, def 13, spd 11, satk 13, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0039 Snubbull

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 209 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Visotruce (184), Colpocoda (39), Demonbacio (142) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 10, 30, 10 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 14, def 11, spd 9, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0040 Qwilfish

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 211 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Velenospina (40), Sdoppiatore (38) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 35, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 16, def 14, spd 15, satk 12, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0041 Remoraid

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 223 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Pistolacqua (55), Amnesia (133) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 13, def 10, spd 13, satk 13, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0042 Pichu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Tuonoshock (84), Fascino (204), Canto (47) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 20, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 18, atk 10, def 8, spd 12, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0043 Cleffa

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 173 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Fascino (204), Ripeti (227), Comete (129) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20, 5, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 9, spd 8, satk 11, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0044 Igglybuff

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 174 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Canto (47), Fascino (204), Ricciolscudo (111), Mimica (102) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 20, 40, 10 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 25, atk 9, def 8, spd 8, satk 10, sdef 8 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0045 Smoochum

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 238 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Leccata (122), Metronomo (118) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 8, spd 13, satk 15, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0046 Elekid

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 239 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Attacco Rapido (98), Fulmisguardo (43), Inseguimento (228) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 12, def 10, spd 16, satk 13, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0047 Magby

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 240 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Braciere (52), Finta (185) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 14, def 10, spd 14, satk 13, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0048 Psyduck

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 54 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Colpocoda (39), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 11, spd 12, satk 13, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0049 Chikorita

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 152 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 20 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 13, spd 11, satk 11, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0050 Pichu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Tuonoshock (84), Fascino (204), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 20, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 18, atk 10, def 8, spd 12, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0051 Cleffa

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 173 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Fascino (204), Ripeti (227), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20, 5, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 9, spd 8, satk 11, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0052 Igglybuff

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 174 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Canto (47), Fascino (204), Ricciolscudo (111), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 20, 40, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 25, atk 9, def 8, spd 8, satk 10, sdef 8 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0053 Smoochum

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 238 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Leccata (122), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 8, spd 13, satk 15, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0054 Wooper

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 194 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Pistolacqua (55), Colpocoda (39), Panciamburo (187) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 30, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 11, def 11, spd 8, satk 9, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0055 Poliwag

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 60 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Bolla (145), Crescita (74) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 40 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 10, spd 15, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0056 Horsea

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 116 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Bolla (145), Nube (114) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 30 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 19, atk 10, def 13, spd 12, satk 13, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0057 Goldeen

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 118 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Beccata (64), Colpocoda (39), Danzaspada (14) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 30 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 13, def 12, spd 12, satk 10, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0058 Magikarp

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 129 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Splash (150), Contropiede (179) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 15 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 18, atk 7, def 12, spd 14, satk 8, sdef 8 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0059 Marill

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 183 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ricciolscudo (111), Stordipugno (146) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 10 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 8, def 11, spd 10, satk 8, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0060 Psyduck

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 54 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Colpocoda (39), Tripletta (161) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 11, spd 12, satk 13, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0061 Tentacool

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 72 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Velenospina (40), Stordiraggio (109) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 10 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 10, def 10, spd 13, satk 11, sdef 16 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0062 Lapras

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 131 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Pistolacqua (55), Ruggito (45), Morso (44) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 40, 25 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 29, atk 15, def 14, spd 12, satk 15, sdef 16 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0063 Chinchou

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 170 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Bolla (145), Tuononda (86), Supersuono (48), Schermoluce (113) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 20, 20, 30 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 24, atk 10, def 10, spd 13, satk 12, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0064 Remoraid

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 223 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Pistolacqua (55), Nebbia (54) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 30 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 13, def 10, spd 13, satk 13, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0065 Mantine

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 226 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Bolla (145), Raffica (16) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 35 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 10, def 13, spd 13, satk 14, sdef 20 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0066 Nidoran♀

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 29 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Ruggito (45), Azione (33), Lucelunare (236) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 35, 5 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 11, def 11, spd 10, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0067 Nidoran♂

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 32 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Fulmisguardo (43), Azione (33), Mattindoro (234) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 35, 5 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 12, def 10, spd 11, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0068 Chansey

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 113 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Profumino (230) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 41, atk 7, def 7, spd 11, satk 10, sdef 17 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0069 Kangaskhan

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 115 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Cometapugno (4), Finta (185) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 27, atk 16, def 14, spd 15, satk 10, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0070 Tauros

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 128 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Colpocoda (39), Attacco Rapido (98) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 30 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 24, atk 16, def 16, spd 17, satk 10, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0071 Dratini

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 147 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Avvolgibotta (35), Fulmisguardo (43), Idropompa (56) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 30, 5 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 12, def 11, spd 11, satk 11, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0072 Spearow

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 21 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Beccata (64), Ruggito (45), Sonicboom (49) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 12, def 9, spd 13, satk 9, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0073 Farfetch’d

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 83 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Beccata (64), Tagliofuria (210) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 13, def 12, spd 12, satk 12, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0074 Doduo

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 84 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Beccata (64), Ruggito (45), Colpo Basso (67) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 15, def 11, spd 14, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0075 Natu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 177 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Beccata (64), Fulmisguardo (43), Salvaguardia (219) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 25 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 11, spd 13, satk 13, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0076 Murkrow

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 198 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Beccata (64), Picchiaduro (251) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 15, def 10, spd 15, satk 15, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0077 Skarmory

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 227 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Fulmisguardo (43), Beccata (64), Tagliofuria (210) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 35, 20 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 20, spd 13, satk 10, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0078 Pichu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Tuonoshock (84), Fascino (204), Stordipugno (146) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 20, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 18, atk 10, def 8, spd 12, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0079 Magnemite

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 81 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Agilità (97) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 19, atk 10, def 13, spd 11, satk 16, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0080 Elekid

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 239 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Attacco Rapido (98), Fulmisguardo (43), Stordipugno (146) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 30, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 12, def 10, spd 16, satk 13, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0081 Voltorb

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 100 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Agilità (97) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 9, def 11, spd 16, satk 12, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0082 Cleffa

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 173 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Fascino (204), Ripeti (227), Visotruce (184) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20, 5, 10 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 9, spd 8, satk 11, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0083 Igglybuff

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 174 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Canto (47), Fascino (204), Ricciolscudo (111), Visotruce (184) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 20, 40, 10 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 25, atk 9, def 8, spd 8, satk 10, sdef 8 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0084 Marill

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 183 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ricciolscudo (111), Visotruce (184) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 10 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 8, def 11, spd 10, satk 8, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0085 Pichu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Tuonoshock (84), Fascino (204), Visotruce (184) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 20, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 18, atk 10, def 8, spd 12, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0086 Wooper

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 194 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Pistolacqua (55), Colpocoda (39), Visotruce (184) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 30, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 11, def 11, spd 8, satk 9, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0087 Tangela

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 114 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Limitazione (132), Sonnifero (79), Sintesi (235) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 15, 5 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 12, def 18, spd 12, satk 16, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0088 Ponyta

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 77 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Colpo Basso (67) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 15, def 12, spd 15, satk 13, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0089 Misdreavus

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 200 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Ruggito (45), Psiconda (149), Ipnosi (95) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 15, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 12, def 12, spd 15, satk 15, sdef 15 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0090 Larvitar

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 246 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Morso (44), Fulmisguardo (43), Ira (99) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 30, 20 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 12, def 11, spd 10, satk 11, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0091 Staryu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 120 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Rafforzatore (106), Tornado (239) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 20 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 19, atk 11, def 12, spd 15, satk 13, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0092 Krabby

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 98 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Bolla (145), Fulmisguardo (43), Ferrartigli (232) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 30, 35 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 19, atk 17, def 15, spd 11, satk 9, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0093 Onix

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 95 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Stridio (103), Affilatore (159) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 30 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 22, spd 13, satk 9, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0094 Lapras

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 131 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Pistolacqua (55), Ruggito (45), Canto (47), Divinazione (248) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 40, 15, 15 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 29, atk 15, def 14, spd 12, satk 15, sdef 16 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0095 Abra

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 63 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Teletrasporto (100), Preveggenza (193) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 40 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 19, atk 8, def 8, spd 15, satk 17, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0096 Drowzee

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 96 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Botta (1), Ipnosi (95), Amnesia (133) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 11, def 11, spd 10, satk 10, sdef 15 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0097 Exeggcute

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 102 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Sferattacco (140), Ipnosi (95), Profumino (230) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 20, 20 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 10, def 14, spd 10, satk 12, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0098 Mr. Mime

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 122 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Barriera (112), Leggimente (170) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 5 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 13, spd 15, satk 16, sdef 18 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0099 Geodude

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 74 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Rapigiro (229) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 14, def 16, spd 8, satk 9, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0100 Zubat

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 41 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Sanguisuga (141), Flagello (175) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 10, spd 12, satk 9, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0101 Machop

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 66 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Colpo Basso (67), Fulmisguardo (43), Colpo (37) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 30, 20 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 11, spd 10, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0102 Cubone

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 104 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Ruggito (45), Colpocoda (39), Furia (31) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 16, spd 10, satk 10, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0103 Delibird

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 225 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Regalino (217), Punte (191) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 12, def 11, spd 14, satk 13, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0104 Seel

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 86 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Bottintesta (29), Ruggito (45), Flagello (175) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 40, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 11, def 12, spd 11, satk 11, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0105 Swinub

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 220 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Turbine (18) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 10, spd 11, satk 9, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0106 Hoothoot

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 163 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Ombra Notturna (101) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 9, def 9, spd 11, satk 10, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0107 Sneasel

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 215 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Fulmisguardo (43), Lucelunare (236) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 5 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 16, def 12, spd 18, satk 10, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0108 Sunkern

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 191 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Assorbimento (71), Crescita (74), Splash (150) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 40, 40 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 19, atk 9, def 9, spd 9, satk 9, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0109 Paras

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 46 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Sintesi (235) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 5 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 13, def 12, spd 9, satk 11, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0110 Hoppip

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 187 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Splash (150), Sintesi (235), Colpocoda (39), Agilità (97) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 5, 30, 30 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 10, def 10, spd 11, satk 10, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0111 Oddish

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 43 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Assorbimento (71), Parassiseme (73) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 12, spd 9, satk 14, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0112 Sentret

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 161 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ricciolscudo (111), Stordipugno (146) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 9, spd 8, satk 10, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0113 Stantler

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 234 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Salvaguardia (219) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 25 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 16, def 12, spd 15, satk 15, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0114 Miltank

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 241 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Megacalcio (25) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 5 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 26, atk 14, def 17, spd 16, satk 10, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0115 Aipom

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 190 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Colpocoda (39), Mimica (102) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 10 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 13, def 12, spd 15, satk 10, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0116 Lickitung

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 108 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Leccata (122), Doppiasberla (3) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 25, atk 12, def 14, spd 9, satk 12, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0117 Snorlax

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 143 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Splash (150) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 32, atk 17, def 13, spd 9, satk 13, sdef 17 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0118 Machop

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 66 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Colpo Basso (67), Fulmisguardo (43), Falsofinale (206) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 30, 40 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 14, def 11, spd 10, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0119 Magikarp

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 129 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Splash (150), Bolla (145) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 40, 30 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 18, atk 7, def 12, spd 14, satk 8, sdef 8 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0120 Tyrogue

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 236 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ira (99) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 10, def 10, spd 10, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0121 Dunsparce

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 206 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Ira (99), Ricciolscudo (111), Furia (31) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 40, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 26, atk 13, def 13, spd 11, satk 13, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0122 Wobbuffet

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 202 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Specchiovelo (243), Salvaguardia (219), Destinobbligato (194), Mimica (102) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 25, 5, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 35, atk 9, def 12, spd 9, satk 9, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0123 Phanpy

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 231 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Ruggito (45), Assorbimento (71) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 25, atk 12, def 12, spd 10, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0124 Teddiursa

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 216 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Fulmisguardo (43), Profumino (230) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 14, def 11, spd 10, satk 11, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0125 Poliwag

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 60 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Bolla (145), Dolcebacio (186) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 10, spd 15, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0126 Poliwag

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 60 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Bolla (145), Demonbacio (142) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 10 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 10, spd 15, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0127 Snorlax

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 143 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Dolcebacio (186) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 10 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 32, atk 17, def 13, spd 9, satk 13, sdef 17 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0128 Snorlax

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 143 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Demonbacio (142) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 10 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 32, atk 17, def 13, spd 9, satk 13, sdef 17 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0129 Kabuto

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 140 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Graffio (10), Rafforzatore (106), Sassata (88) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 19, atk 14, def 15, spd 12, satk 12, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0130 Omanyte

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 138 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Limitazione (132), Ritirata (110), Sassata (88) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 10, def 16, spd 10, satk 15, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0131 Aerodactyl

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 142 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Attacco d’Ala (17), Sassata (88) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 15 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 24, atk 17, def 13, spd 19, satk 12, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0132 Porygon

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 137 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Conversione (160), Conversione2 (176), Barriera (112) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 30, 30 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 12, def 13, spd 10, satk 15, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0133 Eevee

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 133 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Colpocoda (39), Crescita (74) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 40 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 12, def 11, spd 12, satk 11, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0134 Sudowoodo

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 185 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Sassata (88), Mimica (102), Sostituto (164) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 10, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 16, def 18, spd 9, satk 9, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0135 Scyther

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 123 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Attacco Rapido (98), Fulmisguardo (43), Sonicboom (49) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 17, def 14, spd 17, satk 12, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0136 Heracross

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 214 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Fulmisguardo (43), Movim. Sismico (69) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 20 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 24, atk 19, def 14, spd 15, satk 10, sdef 16 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0137 Pinsir

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 127 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Presa (11), Sassata (88) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 15 | tabella dei punti potenza di base |
| esperienza | 156 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 19, def 16, spd 15, satk 12, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0138 Ledyba

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 165 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Barriera (112) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 8, def 9, spd 12, satk 10, sdef 14 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0139 Spinarak

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 167 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Velenospina (40), Millebave (81), Crescita (74) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 40 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 12, def 10, spd 9, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0140 Yanma

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 193 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Preveggenza (193), Dolcebacio (186) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 23, atk 13, def 11, spd 16, satk 14, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

### EVT-2-0141 Pineco

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 204 | tabella degli eventi |
| livello | 5 | tabella degli eventi |
| mosse | Azione (33), Protezione (182), Sostituto (164) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 10, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 13, def 15, spd 8, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |

