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
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Azione (33), Ruggito (45) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 22 e 3 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 21, atk 11, def 11, spd 11, spc 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d9bd2041439c7524bffe560a427ea7b6e11c292341b8c866bc439bdb6bd5b18b` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-1-0001 Charmander

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 4 | tabella degli eventi |
| identificativo interno | 176 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Graffio (10), Ruggito (45) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 20 e 20 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 20, atk 11, def 10, spd 13, spc 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `5d0a665978c9f686024d13e0d04452987def09ecd6018e8bb80afadba860de28` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-1-0002 Squirtle

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 7 | tabella degli eventi |
| identificativo interno | 177 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Azione (33), Colpocoda (39) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 21 e 21 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 20, atk 11, def 13, spd 10, spc 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `f6cfd483666098c726c39651e5eff2f9b197b3cbd869c5b332d9eb9f7df89edc` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-1-0003 Psyduck

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 54 | tabella degli eventi |
| identificativo interno | 47 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello dichiarato | 15 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 15 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 15 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Graffio (10), Amnesia (133) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20 | tabella dei punti potenza di base |
| esperienza | 3375 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 21 e 21 | tabella delle statistiche di base |
| tasso di cattura | 190 | tabella delle statistiche di base |
| statistiche | max_hp 44, atk 25, def 23, spd 26, spc 24 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d87ca944cd53231fc4363eb50b14c8122506f955b246428b3a05ff5c7269732b` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-1-0004 Hitmonlee

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 106 | tabella degli eventi |
| identificativo interno | 43 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello dichiarato | 20 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 20 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 20 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Doppiocalcio (24), Meditazione (96) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 40 | tabella dei punti potenza di base |
| esperienza | 8000 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 1 e 1 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 56, atk 59, def 32, spd 45, spc 25 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `0d2433cda6213b25ec4df05bb31a2a6476d8b9652b9c229fcb00cb521f0eef65` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-1-0005 Hitmonchan

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 107 | tabella degli eventi |
| identificativo interno | 44 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello dichiarato | 20 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 20 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 20 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Cometapugno (4), Agilità (97) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 30 | tabella dei punti potenza di base |
| esperienza | 8000 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 1 e 1 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 56, atk 53, def 42, spd 41, spc 25 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `a31d35378208b3bd525736426937bb388ad966a46db89096b344bd28b548c7da` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-1-0006 Eevee

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 133 | tabella degli eventi |
| identificativo interno | 102 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello dichiarato | 25 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 25 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 25 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Azione (33), Colpocoda (39) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30 | tabella dei punti potenza di base |
| esperienza | 15625 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 0 e 0 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 70, atk 40, def 37, spd 40, spc 45 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `6249868c90a4797d06fb4edaebbe29a66fd7e8cbfe4f1b17743462b2c627cf80` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-1-0007 Omanyte

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 138 | tabella degli eventi |
| identificativo interno | 98 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello dichiarato | 20 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 20 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 20 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Pistolacqua (55), Ritirata (110) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 40 | tabella dei punti potenza di base |
| esperienza | 8000 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 5 e 21 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 50, atk 27, def 51, spd 25, spc 47 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `6134348220866952421dbfb319c53b0ca6f0bfb4fc1c7d43fff17a867749d998` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-1-0008 Kabuto

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 140 | tabella degli eventi |
| identificativo interno | 90 | corrispondenza fra numerazione del Dex e numerazione interna di prima generazione |
| livello dichiarato | 20 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 20 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 20 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Graffio (10), Rafforzatore (106) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30 | tabella dei punti potenza di base |
| esperienza | 8000 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| tipi | 5 e 21 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 48, atk 43, def 47, spd 33, spc 29 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | STADIO, identificativo 2000 | nome e identificativo fissati dalla fonte per la lingua italiana, cioè STADIO con identificativo 2000 per le versioni non giapponesi |
| restrizione di lingua | qualunque | tabella degli eventi |
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `80f7bada53dcd42f9d98ce1fa756f6a610ba09f90a13cf72089d309235b0bf95` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

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
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Botta (1) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 10, difesa 1, velocità 12, speciale 5, punti salute 5 | fissati dalla fonte |
| tipi | 24 e 24 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 25, atk 16, def 15, spd 16, spc 15 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | YOSHIRA, identificativo 6000 | la fonte accetta diciannove nomi per il tour europeo e non fissa alcun identificativo: si sceglie il primo dell'elenco, e l'identificativo è una scelta nostra dichiarata e non un dato |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Mew dei tour internazionali | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `ada3f4b9827431cce9976eb37cc4a821c650a04713105df643baad0e38f7dc34` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

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
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Botta (1) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 10, difesa 1, velocità 12, speciale 5, punti salute 5 | fissati dalla fonte |
| tipi | 24 e 24 | tabella delle statistiche di base |
| tasso di cattura | 45 | tabella delle statistiche di base |
| statistiche | max_hp 25, atk 16, def 15, spd 16, spc 15 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | マクハリ, identificativo 6000 | nome dello Space World '99 di Makuhari, primo dell'elenco giapponese della fonte; l'identificativo è una scelta nostra |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Mew delle manifestazioni giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | non calcolata | l'impronta si calcola sui byte scritti, quindi esiste soltanto quando le schede si generano insieme al lotto: se manca su tutte le voci la corsa è stata di sole schede, se manca su alcune quelle voci non sono state scritte e il motivo è dichiarato nell'elenco delle non scritte |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

## Uova misteriose dei Pokemon Center giapponesi

Generazione 2, donatore dichiarato dalla fonte come destinatario. Il gruppo porta 15 voci e 12 specie distinte.

Quando: 15 dicembre 2001 - 14 gennaio 2002, 16 marzo - 7 aprile 2002, 27 aprile - 12 maggio 2002. Dove: negozi Pokemon Center di Tokyo e Osaka. Come: consegnata al negozio, una sola per visitatore e con la specie estratta a sorte, con il nome e l'identificativo di chi la riceve.

Questo era l'ultimo gruppo di prima e seconda generazione senza provenienza, e il 2026-09-03 è stato chiuso con tre fonti che concordano. La fonte tecnica lo classifica come consegnato al destinatario e non dichiara nome, data né luogo; le due fonti enciclopediche lo identificano come le uova misteriose distribuite nei negozi Pokemon Center di Tokyo e Osaka in tre campagne, chiamate serie, fra il dicembre 2001 e il maggio 2002. La terza fonte, un evendex francese, è quella decisiva perché enumera le consegne una per una e ne dà i campi: diciassette consegne storiche, sei nella prima serie, sei nella seconda e cinque nella terza, ciascuna con specie, livello cinque, mosse, e la dichiarazione che nome e identificativo dell'allenatore sono quelli del giocatore. L'accordo con la nostra tabella è campo per campo sulle mosse, che sono la parte diagnostica, e conferma una deduzione che il progetto aveva fatto il giorno prima senza poterla provare: quindici voci coprono diciassette consegne perché due coincidono nei byte, cioè il Chikorita della prima serie è identico a quello della seconda e il Pichu della prima è identico a quello della terza. Il marcatore che attribuisce una voce alla propria serie è una mossa, e la sezione delle voci di questo file porta l'attribuzione una per una. Un fatto nuovo dalla terza fonte cambia come si leggono i nostri dati: la consegna era ripetibile per ottenere un esemplare cromatico, quindi la nostra scelta di produrre queste uova non cromatiche è una fra due legittime e non la sola. Va infine registrata una divergenza con la prima fonte enciclopedica, che attribuiva alla prima serie un Chikorita con due mosse sole: la terza fonte gli attribuisce le medesime tre della seconda serie, e la nostra tabella concorda con la terza.

Pagina che descrive l'evento: <https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_(Generation_II)>.

Fonti: [PKHeX, template degli eventi di seconda generazione](https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Legality/Encounters/Templates/Gen2/EncounterGift2.cs), letta il 2026-09-03; [Bulbapedia, distribuzioni giapponesi in seconda generazione](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_(Generation_II)), letta il 2026-09-03.

Divergenza fra le fonti: La prima fonte enciclopedica attribuisce alla prima serie un Chikorita con due mosse sole, mentre la terza fonte e la tabella tecnica gli attribuiscono tre mosse identiche a quelle della seconda serie. Si segue la maggioranza, che è anche la fonte che enumera le consegne una per una. Va inoltre segnalato che l'utente ha portato il 2026-09-03 un elenco di dieci specie per campagna, comprendente Cyndaquil, Tyrogue, Elekid e Magby, con mosse che nessuna delle tre fonti riporta per queste serie. Quelle quattro specie esistono nella tabella tecnica ma nel gruppo del Pokemon Center di New York e non in questo, quindi l'elenco confonde due gruppi distinti; le mosse indicate non corrispondono ad alcuna delle tre fonti e restano non confermate.

### EVT-2-0142 Chikorita

Attribuzione di questa voce: prima serie, 15 dicembre 2001 - 14 gennaio 2002, e seconda serie, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza; la terza fonte attribuisce alle due serie il medesimo Chikorita, quindi questa voce copre due consegne.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 152 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Azione (33), Ruggito (45), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 20 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 13, spd 11, satk 11, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `7c831f600fdb443063f4af2bb903cbde7f1f0356f740a68acc3b7b08b6e5776c` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0143 Pichu

Attribuzione di questa voce: prima serie, 15 dicembre 2001 - 14 gennaio 2002, e terza serie, 27 aprile - 12 maggio 2002. Il marcatore che la distingue è Canto; la terza fonte attribuisce alle due serie il medesimo Pichu, quindi questa voce copre due consegne.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Tuonoshock (84), Fascino (204), Canto (47) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 20, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 18, atk 10, def 8, spd 12, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `754b8967456f9c9898114d6d59be328901103f58b9596f20a36e2337ff193089` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0144 Cleffa

Attribuzione di questa voce: prima serie, 15 dicembre 2001 - 14 gennaio 2002. Il marcatore che la distingue è Comete.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 173 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Botta (1), Fascino (204), Ripeti (227), Comete (129) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20, 5, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 9, spd 8, satk 11, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `1b40ec91363d00230130d32260aa3895cbaa65d6c0866124e5a90c81068b74f4` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0145 Wooper

Attribuzione di questa voce: prima serie, 15 dicembre 2001 - 14 gennaio 2002. Il marcatore che la distingue è Panciamburo.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 194 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Pistolacqua (55), Colpocoda (39), Panciamburo (187) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 30, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 11, def 11, spd 8, satk 9, sdef 9 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `929388fb5f6511c068250cbfa79712afe0c10b28c158dfe2dfe56689151e4837` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0146 Phanpy

Attribuzione di questa voce: prima serie, 15 dicembre 2001 - 14 gennaio 2002. Il marcatore che la distingue è Ripeti.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 231 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Azione (33), Ruggito (45), Ripeti (227) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 5 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 25, atk 12, def 12, spd 10, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `e9752c7e40eb2d8c1f6b6a2f968611518ed78827bb591f3a5cab29bdcd346d73` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0147 Smoochum

Attribuzione di questa voce: prima serie, 15 dicembre 2001 - 14 gennaio 2002. Il marcatore che la distingue è Metronomo.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 238 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Botta (1), Leccata (122), Metronomo (118) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 10 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 8, spd 13, satk 15, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `e82d89e31a3af43aa07c8ececf1b5e5713a48b048badaef96da1c524e745a54f` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0148 Psyduck

Attribuzione di questa voce: seconda serie, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 54 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Graffio (10), Colpocoda (39), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 11, spd 12, satk 13, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `13c161958f9a8be48f0b439d4c875d9041be67480e79dfb0d0ec93f51178a865` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0149 Pichu

Attribuzione di questa voce: seconda serie, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Tuonoshock (84), Fascino (204), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 20, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 18, atk 10, def 8, spd 12, satk 10, sdef 10 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d7cd1c0ee8ba1204a8b0b1efa16c05f1124562e2a3dc04f175015bb27fe1c3bf` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0150 Cleffa

Attribuzione di questa voce: seconda serie, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 173 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Botta (1), Fascino (204), Ripeti (227), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 20, 5, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 9, spd 8, satk 11, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `fa80d2161505c9635d465e70ea7fd746258938de7c39ea62593dd95d4e49b8dc` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0151 Igglybuff

Attribuzione di questa voce: seconda serie, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 174 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Canto (47), Fascino (204), Ricciolscudo (111), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 20, 40, 20 | tabella dei punti potenza di base |
| esperienza | 100 | formula del gruppo di crescita 4, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 25, atk 9, def 8, spd 8, satk 10, sdef 8 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `00e74f63fb7868a84e16a9a8ed85bd22d790a846008e79480c2f3fcfe8d91cec` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0152 Smoochum

Attribuzione di questa voce: seconda serie, 16 marzo - 7 aprile 2002. Il marcatore che la distingue è Petalodanza.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 238 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Botta (1), Leccata (122), Petalodanza (80) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 20 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 9, def 8, spd 13, satk 15, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `4dec7bf41929ec084079c11f46d03207e8b9d01e2e6624eb70e004d45668136c` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0153 Bulbasaur

Attribuzione di questa voce: terza serie, 27 aprile - 12 maggio 2002. Il marcatore che la distingue è Forzantica.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 1 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Azione (33), Ruggito (45), Forzantica (246) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 5 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 11, def 11, spd 11, satk 13, sdef 13 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `a2e48bd1fa1a51e63c9ea8675f293a0fa9cacbf460ec8715bb6d7c7ee671c819` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0154 Charmander

Attribuzione di questa voce: terza serie, 27 aprile - 12 maggio 2002. Il marcatore che la distingue è Sgranocchio.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 4 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Graffio (10), Ruggito (45), Sgranocchio (242) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 15 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 20, atk 11, def 10, spd 13, satk 12, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `6212b6f4c5525a254b43ef69e2eccf72a1f75edf86c9946f36118257f8c31b4e` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0155 Totodile

Attribuzione di questa voce: terza serie, 27 aprile - 12 maggio 2002. Il marcatore che la distingue è Sottomissione.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 158 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Graffio (10), Fulmisguardo (43), Sottomissione (66) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 30, 25 | tabella dei punti potenza di base |
| esperienza | 135 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 21, atk 13, def 12, spd 10, satk 10, sdef 11 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `39609c14b88b8d2e0b91c449ef9e2b5b17630d47eed88e2c097a8bca596c6b2a` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0156 Hoothoot

Attribuzione di questa voce: terza serie, 27 aprile - 12 maggio 2002. Il marcatore che la distingue è Ombra Notturna.

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 163 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
| mosse | Azione (33), Ruggito (45), Ombra Notturna (101) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 40, 15 | tabella dei punti potenza di base |
| esperienza | 125 | formula del gruppo di crescita 0, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 15, velocità 15, speciale 15, punti salute 15 | scelta nostra dichiarata, non un dato |
| cromatico | no | tabella degli eventi |
| uovo | sì, 10 incubazioni | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 0 | tabella degli eventi |
| statistiche | max_hp 22, atk 9, def 9, spd 11, satk 10, sdef 12 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | Alessio, identificativo 42317 | allenatore del progetto, scelto e dichiarato in `recreate-pokemon-distributions-events/allenatore.json`: la fonte dichiara che questa voce prende nome e identificativo da chi riceve la consegna, e chi riceve siamo noi |
| restrizione di lingua | giapponese | tabella degli eventi |
| gruppo di appartenenza | Uova misteriose dei Pokemon Center giapponesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `bdb7abd402121a6c26109d2a1b7a6381802c9e12a2f6e85d53b43939915b8f57` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

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
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium 2, versione giapponese | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | non calcolata | l'impronta si calcola sui byte scritti, quindi esiste soltanto quando le schede si generano insieme al lotto: se manca su tutte le voci la corsa è stata di sole schede, se manca su alcune quelle voci non sono state scritte e il motivo è dichiarato nell'elenco delle non scritte |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0001 Gligar

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 207 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium 2, versione giapponese | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | non calcolata | l'impronta si calcola sui byte scritti, quindi esiste soltanto quando le schede si generano insieme al lotto: se manca su tutte le voci la corsa è stata di sole schede, se manca su alcune quelle voci non sono state scritte e il motivo è dichiarato nell'elenco delle non scritte |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

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
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium 2, versione inglese | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `97911eb7644c2de1a6e611c0c5dde6f04b8531be3894131b4ca621bf270a66e6` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0003 Gligar

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 207 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium 2, versione inglese | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `73f5a2aa3970bf3fa46cbb425a2eba955d7a44cf63773f3be7361d6c73d31841` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

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
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium 2, versioni internazionali non inglesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `fa3504770cb07b14713556e6b916b65be48d9c42457712a36932314543aab1ed` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0005 Gligar

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 207 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Esemplari premio di Pokemon Stadium 2, versioni internazionali non inglesi | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `53fe134910cbb52802eeb933e6fd20ddf8238b754e31050f2e03e41d13338736` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

## Distribuzioni del Pokemon Center di New York

Generazione 2, donatore dichiarato dalla fonte come Pokemon Center New York. Il gruppo porta 136 voci e 106 specie distinte.

Quando: dal 16 novembre 2001, data di apertura del negozio. Dove: Pokemon Center di New York, secondo piano. Come: una macchina distributrice fra quattro, una consegna a settimana per visitatore e non più di una al giorno, inserendo la propria cartuccia.

Centotrentasei voci, cioè l'ottantasei per cento di tutti gli eventi di seconda generazione, tutte dallo stesso luogo: il primo e finora unico negozio Pokemon degli Stati Uniti, aperto il 16 novembre 2001. La fonte tecnica ammette quattro nomi di allenatore, da PCNYa a PCNYd, e il progetto aveva congetturato che fossero quattro postazioni oppure quattro periodi. La fonte enciclopedica lo conferma nel primo senso: al secondo piano c'era una postazione chiamata Gotta catch 'em all Station composta da quattro macchine distributrici, e i quattro nomi sono le quattro macchine. È il genere di dettaglio che trasforma un campo di un byte in un luogo fisico. Le regole della consegna erano una a settimana per visitatore e non più di una al giorno se la macchina veniva riavviata, il che spiega la quantità delle voci: centotrentasei esemplari distinti erano una ragione per tornare al negozio ogni settimana. Due fatti della fonte enciclopedica cambiano come si leggono i nostri dati. Il primo è che tutti gli esemplari tranne gli evoluti, i leggendari e i mitici venivano consegnati come uova. Il secondo è che ciascuna distribuzione aveva una probabilità del quindici per cento di essere cromatica, salvo dichiarazione contraria: ne segue che le voci che la tabella tecnica non marca come cromatiche potevano esserlo, quindi la nostra scelta di produrle non cromatiche è una fra due legittime e non la sola. Le sedici che la tabella marca come cromatiche sono invece quelle in cui la cromaticità era garantita, e su quelle la cromaticità vincola quattro valori individuali su cinque: sono le sole voci di questo gruppo su cui la fedeltà sia in parte verificabile. Il contenuto è la parte notevole, perché fra le prime voci compaiono un Mew cromatico, un Celebi con Parassiseme, Confusione, Rintoccasana e Ripresa, i tre leggendari di Johto cromatici e i tre uccelli di Kanto cromatici, oltre a esemplari comuni con assortimenti di mosse costruiti a mano. Un chiarimento che il 2026-09-03 si è rivelato necessario, perché la descrizione precedente dava un'impressione sbagliata: questo gruppo non è fatto di esemplari con esemplari cromatici notevoli e poche uova, è fatto quasi soltanto di uova. Centodiciannove delle centotrentasei voci sono uova, e diciassette sono esemplari; sommate alle quindici del gruppo giapponese fanno centotrentaquattro uova su centocinquantasette voci di seconda generazione, con ottantanove specie distinte. Ne segue che le uova baby con mossa insolita, che l'utente cercava nel lotto, ci sono e sono la maggioranza: Cyndaquil, Tyrogue, Elekid e Magby stanno qui e non nel gruppo giapponese, ed erano nel lotto dal principio sotto i loro indici.

Pagina che descrive l'evento: <https://bulbapedia.bulbagarden.net/wiki/List_of_PCNY_event_Pok%C3%A9mon_distributions_in_Generation_II>.

Fonti: [PKHeX, template degli eventi di seconda generazione](https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Legality/Encounters/Templates/Gen2/EncounterGift2.cs), letta il 2026-09-03; [Bulbapedia, distribuzioni del Pokemon Center di New York in seconda generazione](https://bulbapedia.bulbagarden.net/wiki/List_of_PCNY_event_Pok%C3%A9mon_distributions_in_Generation_II), letta il 2026-09-03.

### EVT-2-0006 Mew

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 151 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `61b0ca0ac95ecd564f490237391d474ca9429d08210100c665fa4d3ef2b6408a` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0007 Celebi

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 251 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `92031fcc64b8f35b9db46a467d0dd6fcc701337aec96f800af08523f418dfcf3` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0008 Raikou

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 243 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Fulmisguardo (43), Tuonoshock (84), Boato (46), Attacco Rapido (98) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 30, 20, 30 | tabella dei punti potenza di base |
| esperienza | 80000 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 128, atk 85, def 73, spd 105, satk 105, sdef 93 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `a4f500caa5e4aedaa1bd1ffe13967f69d053291c06b1818b6048cd1c4cf987b2` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0009 Entei

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 244 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Fulmisguardo (43), Braciere (52), Boato (46), Turbofuoco (83) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 25, 20, 15 | tabella dei punti potenza di base |
| esperienza | 80000 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 148, atk 109, def 81, spd 93, satk 85, sdef 73 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `ea19ba14c1418484c7248d14b2a5bcae6812255052b3099a81baa36459923b68` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0010 Suicune

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 245 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Fulmisguardo (43), Pistolacqua (55), Boato (46), Raffica (16) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 25, 20, 35 | tabella dei punti potenza di base |
| esperienza | 80000 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 136, atk 77, def 105, spd 81, satk 85, sdef 105 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `298b99e7df38e1b0692070c67b3b993a09e8113eddc09df1d862b3edc7ff3e98` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0011 Articuno

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 144 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 50 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Nebbia (54), Agilità (97), Leggimente (170), Geloraggio (58) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 30, 30, 5, 10 | tabella dei punti potenza di base |
| esperienza | 156250 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 158, atk 105, def 115, spd 100, satk 110, sdef 140 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `f72c205befbf88e454dfe721a8f4e270bcecc676346285c155f0cf82ec634fcf` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0012 Zapdos

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 145 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 50 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Tuononda (86), Agilità (97), Individua (197), Perforbecco (65) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 30, 5, 20 | tabella dei punti potenza di base |
| esperienza | 156250 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 158, atk 110, def 100, spd 115, satk 140, sdef 105 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d11fe19bd00d44a6945a2ae523a5ef4b80579c4698c17f56b0caf07ab5af0825` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0013 Moltres

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 146 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 50 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Turbofuoco (83), Agilità (97), Resistenza (203), Lanciafiamme (53) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 15, 30, 10, 15 | tabella dei punti potenza di base |
| esperienza | 156250 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 158, atk 120, def 105, spd 105, satk 140, sdef 100 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `be0cec290752f05f966778a6cbaa1ce45e966fbd448b00935d2715cd7bf663d6` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0014 Venusaur

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 3 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Velenpolvere (77), Sonnifero (79), Foglielama (75), Profumino (230) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 35, 15, 25, 20 | tabella dei punti potenza di base |
| esperienza | 56660 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 120, atk 82, def 79, spd 77, satk 93, sdef 93 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `5387881f355a2b28f8a10afab1ec8d57f217ae23c91ca7b5ba57b18a1c0d8f69` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0015 Charizard

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 6 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Ira (99), Visotruce (184), Lanciafiamme (53), Attacco d’Ala (17) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 10, 15, 35 | tabella dei punti potenza di base |
| esperienza | 56660 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 118, atk 84, def 75, spd 93, satk 100, sdef 81 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `2c3c59ab0520e96d04bc6cfa784f3a4250c8794ab691c1488870b9eb3152ad4b` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0016 Blastoise

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 9 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Pistolacqua (55), Morso (44), Rapigiro (229), Protezione (182) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 25, 40, 10 | tabella dei punti potenza di base |
| esperienza | 56660 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 119, atk 83, def 93, spd 75, satk 81, sdef 97 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `6dd492e3d8ccc3dfb3d83be6ba7671c2249f30f0d5964beac93ed93cf51e2e49` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0017 Mewtwo

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 150 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 70 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Psicamisù (244), Divinazione (248), Nebbia (54), Psichico (94) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 10, 15, 30, 10 | tabella dei punti potenza di base |
| esperienza | 428750 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 239, atk 180, def 145, spd 201, satk 234, sdef 145 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `bbf3572427803852aa86ec10524d1d2db8bfa34f6d99e2c708f7f4c3d761188d` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0018 Ho-Oh

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 250 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Magifuoco (221), Salvaguardia (219), Raffica (16), Ripresa (105) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 5, 25, 35, 20 | tabella dei punti potenza di base |
| esperienza | 80000 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 141, atk 121, def 85, spd 85, satk 101, sdef 136 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `abf08e86614733c52b50d78a93d44a56383fb0ed9b8e560a8f80299478c0342a` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0019 Lugia

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 249 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Aerocolpo (177), Salvaguardia (219), Raffica (16), Ripresa (105) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 5, 25, 35, 20 | tabella dei punti potenza di base |
| esperienza | 80000 | formula del gruppo di crescita 5, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 141, atk 89, def 117, spd 101, satk 85, sdef 136 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `4fe49d79ca7b43d37e6d09ff0c9323fff4f3f2aca8df0afe87857e689ff5fe43` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0020 Meganium

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 154 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Riflesso (115), Velenpolvere (77), Sintesi (235), Corposcontro (34) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 35, 5, 15 | tabella dei punti potenza di base |
| esperienza | 56660 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 120, atk 82, def 93, spd 77, satk 79, sdef 93 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `f6c5069af06587e6df56e42e867436a5f0f99935f67d77df351e9f5e60e83d82` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0021 Typhlosion

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 157 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Muro di Fumo (108), Braciere (52), Attacco Rapido (98), Ruotafuoco (172) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 20, 25, 30, 25 | tabella dei punti potenza di base |
| esperienza | 56660 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 118, atk 84, def 75, spd 93, satk 100, sdef 81 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `7076376d8bb2abae58868ef90ff0d8eff6e8a52d1db2c591968b5c4efab511ca` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0022 Feraligatr

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 160 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 5 | coincide con quello dichiarato, perché questa voce non è un uovo |
| livello corrente | 40 | tabella degli eventi, campo a sette byte dall'inizio del record: è il livello a cui l'esemplare si trova, mentre quello di incontro resta nei dati di cattura. I due divergono sulle quindici voci del gruppo notevole, e usare il solo livello di incontro le faceva respingere tutte |
| mosse | Pistolacqua (55), Morso (44), Visotruce (184), Lacerazione (163) | tabella degli eventi, con i nomi dalla tabella dei nomi |
| punti potenza | 25, 25, 10, 20 | tabella dei punti potenza di base |
| esperienza | 56660 | formula del gruppo di crescita 3, importata dal generatore di terza generazione |
| valori individuali | attacco 15, difesa 10, velocità 10, speciale 10, punti salute 8 | vincolati dalla cromaticità dichiarata dalla fonte |
| cromatico | sì | tabella degli eventi |
| uovo | no | tabella degli eventi, dove le incubazioni diverse da zero lo dichiarano |
| luogo di cattura | 127 | tabella degli eventi |
| statistiche | max_hp 124, atk 101, def 93, spd 75, satk 76, sdef 79 | formula delle prime due generazioni, con esperienza di statistica nulla |
| allenatore | PCNYa, identificativo 1000 | la fonte accetta quattro nomi per il Pokemon Center di New York, da PCNYa a PCNYd, e non fissa alcun identificativo: si sceglie il primo e l'identificativo è una scelta nostra dichiarata |
| restrizione di lingua | internazionale | tabella degli eventi |
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `345fb8ca06839bd46e3cf83b2611e0e59f698ed4e409954a906392dabe72f7f6` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0023 Delibird

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 225 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `5c79a7b064ee00dc0e5b62e122706416ce8765d15ad0cae4edfd171e505ebf1b` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0024 Bulbasaur

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 1 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `1d8302025d25ebba6ff276458e9660a9f4b7d79fe7c49591888927e151e41be1` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0025 Charmander

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 4 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d388a8bbfc378db5dd709970102182bc41afa55e9350251f262d4dc9cde8f9bc` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0026 Squirtle

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 7 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `ae64625b7576d9f298517a6759f5c9f82c1bcdb4e6fcaa0934640b7c48ed01f8` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0027 Chikorita

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 152 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `43b53a2b041e98d03a677aa9a82948020613c51a7f0e30077b5915867d9d95f4` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0028 Cyndaquil

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 155 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `1accd0a80c60df12ac4066dee789341ac552abea4cc6ccedcc8eb8cc33fed59f` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0029 Totodile

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 158 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `01d5e90b3e1ab794d8ff022b2d4e2c79bba78881800c8e582e6d052ee2493c9d` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0030 Nidoran♀

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 29 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `8dcdb69e7ec6338f99b5d101e401c0352cdfc0d93e52c11a371a19af512dcd59` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0031 Nidoran♀

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 29 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `98dc120fb7ccd3a4ff51af26d96cc305d57de193b6af8a019274fd0362d5d13b` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0032 Nidoran♂

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 32 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `c2cfbe3e4d9bcfb1c965c73969be3b2b9b4a6d2276bd598523064bbe7952570a` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0033 Nidoran♂

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 32 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `3dc0094ce2f701605608f3aaaf560474eebc598066a5dcb591362b91b9ce51ff` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0034 Bellsprout

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 69 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `f023071847f86923386895992dfff24ff9c05f10111bd6ce910d5160769a5af9` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0035 Bellsprout

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 69 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d8bef37507a0defbce6452061deb352c8cd118a23966d46e0a118300cc30be8a` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0036 Marill

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 183 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d69cad6bbd5eff651d7649d3c839f22ed597583a650ddd9df2f69c48b2c27e40` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0037 Yanma

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 193 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `3a079ca7ae3bf40b333727c23d56ed3cac51fa6e4ab61eb52d393b8cfcde3d12` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0038 Dunsparce

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 206 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `39d72b02dfdcb8b294637f6a888e43a75312a3260a5ebb86c9ff0e7d4eaa4ce1` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0039 Snubbull

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 209 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `6c7650b4642fb729e3d3facbda3aae22a625eaba7c3c9d33419c2cb71fcfbaf5` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0040 Qwilfish

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 211 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `cb757e249394ce3c8a34cde24fc5307bf4f63b771ed87ef0b58c5409144a9f61` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0041 Remoraid

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 223 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `fd52966b75b636994d53a15dc55d35d2d6e3313ff18dc790a277e7326427bb25` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0042 Pichu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `17837a9c70ffc7c5370e30a1e003a9899d9399f36cb51d0a81823fea99904133` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0043 Cleffa

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 173 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `9827ede2c9300b7ce3ad5078dbae468410041e343b74e1dc31a03f9737cf46fe` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0044 Igglybuff

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 174 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `84bdebb849c67946bbe7ea7d6828ebca7474ae705ce5b82b8173073b9ed717e4` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0045 Smoochum

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 238 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `333e1b59861a821ae9cf841b07f9901f60127d623704d63110e5ae5a5f537709` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0046 Elekid

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 239 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `cd727dd35560a15ef33611529e3e5d54063e135fc449d62ed020c42c2c85b018` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0047 Magby

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 240 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `5c79e357cca3a6ce69a393ed0b947398fd991bc1f49a8614d605371b839f6ed3` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0048 Psyduck

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 54 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `8ed84c8029f41d936e29dbc56cd539889353cd907d06e54869c0009cd21f3670` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0049 Chikorita

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 152 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `43b53a2b041e98d03a677aa9a82948020613c51a7f0e30077b5915867d9d95f4` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0050 Pichu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `0d8fb0369d25a015ae547bea5d6b0a0e7ba6bf0f2b78b5eb7b5e456a54242775` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0051 Cleffa

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 173 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `ade74575d816f054884ab90000989e5c1e0e3ae769f555e755b292504dbfe19e` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0052 Igglybuff

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 174 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `aa8a9680f1854844743fd3015c39170bebee6fcb96c465b9851c32842cdc6813` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0053 Smoochum

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 238 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `88fce71192d7c3fcd7789b145eeaf3c68335cc1e0e590ec2733704cfd4674578` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0054 Wooper

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 194 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `4252934606662f7672eedcf2bc967672784625978d54bead4590d1b5126e7ae5` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0055 Poliwag

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 60 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `cec49b9956829f347610a08ef28e22f219873a4f2480d140e7a6903354e9cc50` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0056 Horsea

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 116 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `9b4a28e0990607647db86c481e2d19f8234bc0274234d8d0296520ac587f1495` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0057 Goldeen

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 118 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `950a9cd2c528db2a75e86c9c3036d487f255b6bed735fd66f16a273498a381e1` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0058 Magikarp

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 129 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `80d95145d9a0647fc0cd31ab97a7085083efb0b65c0360810d40368e325e5a11` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0059 Marill

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 183 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `b5514edfb09dc6c54828e53ef5f52df130468996f7bb04d92ff279cf8e9d154e` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0060 Psyduck

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 54 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `9c20c8a5350ae7aac67c25f4542ff0614003c7b22e636934b94e2e5dc4566cee` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0061 Tentacool

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 72 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `84a35fdaf6b9317a80550996267b7ca4ef8603153c548d5d1b9486aa74981210` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0062 Lapras

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 131 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `ca54d60d1f9b7a8db08a0bad38b775e0a65c50f9c2d576dc6755c2e8474c11db` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0063 Chinchou

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 170 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `cdd56ecabe5def2ae23117bb161b538cdb795f44951c812f3ee6659c0662086e` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0064 Remoraid

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 223 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `6b2f97f83bcbd27971566e10406ca7c61e51c252eea6f6633aadc36205903cb7` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0065 Mantine

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 226 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `fc19f466f56199e3db02d4c29b4835fa1ca0e507a54d054e6d98f81be2d0a126` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0066 Nidoran♀

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 29 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `70365bb9d6283d6b065e0e262f4807a235559f56a6aec2057a4db773c307dde1` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0067 Nidoran♂

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 32 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `816daf2ecc9dd0375d041f5ea7594b77ec1701fae8d68a40d83c76b4cb1e85cb` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0068 Chansey

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 113 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `527e1932f85c4651a162c82c1a9244e3522d868b713baf43b278298927833da0` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0069 Kangaskhan

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 115 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `ab1672b3b7fca7b07b9afbfa6d125f8ff388d84cf67ea5ffd992383f87f511cd` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0070 Tauros

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 128 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `2f698613fa3e9ea6dd07a9a384208b9573223f08cdd2895c590918a5967eb291` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0071 Dratini

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 147 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `7278e9832c2c16bc24c75253204de6c2f235c353e079a37545334f68b8110684` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0072 Spearow

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 21 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `cb437bc368090ea5c73a0436b72929e5ad720636da6bcb2a877551e63a31b7e4` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0073 Farfetch’d

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 83 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `94975fb350fcf39ce79248577a826ca0621785964a582283833e8543cc3a68f2` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0074 Doduo

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 84 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `5a90ae022ddbea958d35b9baac81c984d60da0c1c898482774600d0254420ada` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0075 Natu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 177 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `a85980c1932bab25e81cb6379924f848320b1149ef7461bfc16896f190034d45` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0076 Murkrow

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 198 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `b4dab390294a1f3e7a6ee4a7e1f5fe65262c8e4739a108f26d8b0856766b1caf` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0077 Skarmory

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 227 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `607c8c78998943efda0cb4ddf59f3b1e26b630c6f23261a5745e3afb6e8309cc` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0078 Pichu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `8d86d3c07f94a88f074955cce0848f25992ca9bf42ef1b61fce2ac433a06bc0b` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0079 Magnemite

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 81 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `30383dfc0239010ac10e54cc7fd8be0678c1a1754759259dac3b82942ccd76df` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0080 Elekid

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 239 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `535042261c7666f6274d3ff61b392eff42d0a084ab25c19c539b81f50182ad5a` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0081 Voltorb

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 100 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `616dedf2432c5c83a56e8100e04c7c22854e88fdc34b56bf1f15537bb16070e6` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0082 Cleffa

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 173 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `7b12aa8ec1bc9b9bbbe529a27c39255a92b6ad18bd764f844116074ed729d147` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0083 Igglybuff

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 174 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `67012fb5e343208a2b4172e698ed02bd614e1168d37bd21dc05ce05579c6a79e` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0084 Marill

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 183 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `4f413eb36fb0782e0610e791ec49814a4d8e14b129fc3025d21956009289b21f` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0085 Pichu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 172 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `660bcef1f2b692950947d0311c25f8b78259292f628551ab28b622e155255d98` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0086 Wooper

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 194 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d0c420f325850c0330de6930a6cc225fd62dbe8ca3714d5a9dd346159bcd9421` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0087 Tangela

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 114 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `66abab5e2f5352a48c6a9615864cd348850b6fc28302605ce45f4364ef5e9efe` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0088 Ponyta

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 77 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d130a2b4d4feee2be1c4ea8d951c53f7f1f8f0f642221017164ce938a837f726` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0089 Misdreavus

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 200 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d46de9d0258eeccce73a3969cbeba603b40769ef7a2239a5990e1545a521f251` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0090 Larvitar

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 246 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `db9fe4026571afd0484bc1fd915c2048156a35568f968b5cb5517bd3155b0235` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0091 Staryu

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 120 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `a0cbffac02ec3d539fdf99a4f83697e0a048ec98ad3339599e99856286257d98` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0092 Krabby

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 98 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `03c936731626ed2a2a485273b5f08f294f3db86aee4f3166b65626e45b0b3e87` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0093 Onix

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 95 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `8cc8c1d7f0788a233fbb25e698484e98b5c482b89d746798e5531353f5030c45` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0094 Lapras

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 131 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `0850fe0d44d5020695f6c435ae8ca5507d47c6f7d35b835d8dd719ff69e9d4f2` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0095 Abra

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 63 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `4f32836ae1eea5f12706c186cdb9668d854e300a50033c4d2c555ce19c16dcc2` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0096 Drowzee

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 96 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `71be579a709a217dec895e2eb5aee66a6d7df576d909f0701fec0dc813ad3b9d` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0097 Exeggcute

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 102 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `a9b568bcdf89452ee94c9a34fd0d0fc1fdabf12d4d18800072811ebeeaa253c3` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0098 Mr. Mime

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 122 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `52d4e61ff93cca271f0f95f6655e588cbd051e16071e05e55a7a6b253bd31421` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0099 Geodude

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 74 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `a1cf148afffecc14dec7e2513b83e223ed85bd9b1d6b1d4d9e8b766fd99039a2` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0100 Zubat

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 41 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `08dc2d196cfb5292bd3086261f99e4161d1864d48e04afd29ddae225a0349923` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0101 Machop

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 66 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d427518a2d4555ea8e56648a1698ff1052cf6812d8330579045c2acc292d1245` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0102 Cubone

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 104 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `77913287e7d166be0827893ca2ca4fcd3b3ff30991558aeac97f92b86fe5ec6a` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0103 Delibird

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 225 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `433eb63f0e45ace7f7f315c254c008b8bff1152247b3f1d44802b931d2b25872` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0104 Seel

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 86 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `9bd6b64a907677112f608f033a093f2f388e516f912901243b68342cd7f2d270` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0105 Swinub

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 220 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `3f9a815bfe2e129080df14bc23d5bedcae826026b387c7e9dc163bdd5e33d4a1` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0106 Hoothoot

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 163 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `21cc1e4dcd3f040f56ecdd9dcd17129fa0b5fd0b5cb831aeb678d3faa7ada040` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0107 Sneasel

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 215 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `094257cdbeb88863a7d74a4c58f5ae61dd42d2b0e2303001277742f9e177a590` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0108 Sunkern

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 191 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `b37cfed0a4ecf0ef40fbc3d25c6e9c4943f3e023353c52f0e68dc11f39b6dc6c` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0109 Paras

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 46 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `43fe76c8d14a87fd034b209f938bc88ab85b39d21abd329dee1548bcb5116cd8` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0110 Hoppip

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 187 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `46850ea4abff3e2c6c6d448da61d6b67eb32e52ffe067e614d75159144e863df` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0111 Oddish

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 43 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `85151b6b66907f26b628ef4e677f6889bce9ee043a231bfeb89863ef78e1c877` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0112 Sentret

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 161 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `53f02fd7c8aed7ec83c8e2f24fa7e64e1310f2fa0e7100062a87806200d00e24` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0113 Stantler

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 234 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `1158dcb7a8190bd322ab285ec80345897fda34afee39d70e6418e16fb0275214` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0114 Miltank

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 241 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `b8df3827d73f1a3041af9b5258fec590c2fde222e2f64ebceb715d08ad995f74` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0115 Aipom

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 190 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `58b73f686aa9d36cf30a5799ebc0b2e3f6717f10e4e30ed9953e12d69c0addbc` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0116 Lickitung

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 108 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `7417bc97ee19ef54c1a7b7f5950a664e740a1bfde76955a1d81c44f21c52900c` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0117 Snorlax

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 143 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `dad6d22b1cfa80b4fbc2d81bb5f81acf432b1848e5adfa94736553d7d544793a` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0118 Machop

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 66 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `b063296e242584184c159bb5f5a3f22ce0e6d8bd47686023d634c90cafd483d2` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0119 Magikarp

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 129 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `8f55835d2ecbe5aa6c8465526baa06c7598aa1e359a5ee50a903b6088d324bad` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0120 Tyrogue

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 236 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `404024e27a9ff1fe782accee80d539c1de8f4ee93c8f9ae8c27b72bfe1c6ac48` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0121 Dunsparce

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 206 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `c97569f25614f260ebda3eac1ae50f1e28a12530ab099bd96d5e6a291d494ac2` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0122 Wobbuffet

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 202 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `64bdc05083642ba18e8394b519126d176985950ae54a231717156700388f88c8` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0123 Phanpy

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 231 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `abb115f6626c5d20df5ea75ee257fed53727450bdd833653d5a922da1c7887de` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0124 Teddiursa

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 216 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `1905673955f2e629ac2d940e28fbe1f6aea109069d2b186b500d0037a258ecc6` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0125 Poliwag

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 60 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `e54038be4ad781e40e0095f5d7651894c3c6ee1d3931f09a68386759c1c1b311` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0126 Poliwag

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 60 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `07c508a427bbdc828e5c564c0d0ebcbd46c4d43fbab6b977e02d8afa49d7d45a` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0127 Snorlax

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 143 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `83cfea4dfaa13e4a9bc462120e45033affa397b3f2fc6a464bdba2b111118934` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0128 Snorlax

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 143 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `ee51a6df7a28e0d912f2a6a0daf76052b8a882289f68e9f6421103664021c54b` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0129 Kabuto

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 140 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `c523d16fcf986fb8ecc381bd37ba22c586a5adc36d6bf0c275af573722fc1e70` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0130 Omanyte

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 138 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `b778f8548a90bb1062c969263bfe08b68e00443a37f91eb70b2d430cfb5a8eb5` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0131 Aerodactyl

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 142 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `5e2a5a5b1a198a68acd9b2b90f2bd0dab607de076441465be3cbcd062536cdfe` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0132 Porygon

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 137 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `bebd57161ae1c4c2fd4204c5b0ff151f59f77d8ffdcc5b0c0700b1025fcba725` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0133 Eevee

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 133 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `d583a6f0e485a0133de0f0490719e823f8f1fc22e6a2e9ea2c94f7eece9235bf` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0134 Sudowoodo

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 185 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `b8dcd10a23f3b36b59248b2ce93287d911a72df5535bc82fbd1e130eda8d08e9` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0135 Scyther

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 123 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `9384fbe5f8997c32b4fc083ee5a2b727003afd6105006e2e27506875be701c49` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0136 Heracross

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 214 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `58401b51ca9d593f51689dd08e93afc0021e3208d1c245972c7427985caf6c8b` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0137 Pinsir

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 127 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `6bf1767e17621b1f14b1decad3af08a3a39a97b340fb5475bf08c0b4e5a1403d` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0138 Ledyba

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 165 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `8574047b4e8b8f76802b5fbcf84e01500100fa823e6d29cf454944c4c107c009` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0139 Spinarak

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 167 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `2d07b289013b7d4840c79ac1ddf1d470fb78aa7559bf5711282a925677bdb829` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0140 Yanma

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 193 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `c66fce0cfc834210251f5af0247d60d93e43284b4f0d8e6500d81a3b10f2b8ee` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

### EVT-2-0141 Pineco

| Campo | Valore | Provenienza |
|---|---|---|
| numero del Dex | 204 | tabella degli eventi |
| livello dichiarato | 5 | tabella degli eventi, campo a un byte dall'inizio del record |
| livello nei dati di cattura | 1 | non è quello dichiarato, perché questa voce è consegnata come uovo: un uovo si riceve a livello uno e schiude a cinque, e i dati di cattura registrano il momento in cui è stato ricevuto. Scrivervi il livello dichiarato faceva respingere tutte e centotrentaquattro le uova del lotto |
| livello corrente | 5 | coincide con quello dichiarato, come nella grande maggioranza delle voci |
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
| gruppo di appartenenza | Distribuzioni del Pokemon Center di New York | il racconto dell'evento, le date, il luogo e le fonti stanno nella sezione di gruppo di questo documento |
| impronta del file prodotto | `bf1b6d190f78429492176fc928869a63e5dd26942058002ee8a791144f418b3d` | SHA-256 dei byte scritti in `_notes/lotto-gb/`, calcolata alla generazione: rigenerare il lotto dalle medesime tabelle deve riprodurla identica, e una differenza segnala che qualcosa è cambiato nelle tabelle o nel programma |
| giudizio del verificatore | conforme, 2026-09-04 | lettura di massa delle nove scatole in un salvataggio vuoto di seconda generazione, dove l'assenza del contrassegno di non conformità su una posizione equivale a un rapporto senza rilievi su quell'esemplare |

