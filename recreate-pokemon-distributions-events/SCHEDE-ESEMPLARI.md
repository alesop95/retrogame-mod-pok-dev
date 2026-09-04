# Schede tecniche degli esemplari producibili

> Documento generato da `tools/schede-esemplari.py`. Non si modifica a mano, e non legge i file prodotti: ricalcola gli esemplari dalle sorgenti con il medesimo codice che li scrive.

Un giudizio di conformità riguarda una configurazione precisa di byte e non una categoria: vale per quel valore di personalità, quei valori individuali, quel nome e quel seme. Registrare soltanto che un esemplare è conforme perde l'informazione che serve, cioè che cosa esattamente sia stato dichiarato conforme, e senza quella non si può né riprodurre il caso né riconoscere che una modifica successiva lo ha cambiato. Questo documento è dunque l'inventario delle caratteristiche univoche di ciascun esemplare, accanto allo stato del suo giudizio.

Che il documento sia ricalcolato e non letto dal disco ha una conseguenza che vale dichiarare: esso è anche una verifica del determinismo della produzione. Se due corse dessero schede diverse, la scelta del seme non sarebbe riproducibile, e il difetto si manifesterebbe come una modifica del documento senza che nulla sia stato modificato a mano.

Stato: 172 voci producibili, di cui 172 dichiarate conformi da un verificatore indipendente al momento dell'ultima generazione di questo documento. Le voci conformi portano la dicitura accanto al titolo; le altre non sono state giudicate oppure lo sono state con rilievi, e il registro dei giudizi in `giudizi-esterni.json` dice quale dei due casi.

### 000 Mew  (giudizio: conforme, 2026-09-04)

**Mystery Mew.** Quando: 30 settembre 2006. Dove: negozi Toys "R" Us degli Stati Uniti. Come: distribuzione senza fili in un'unica finestra di tre ore, dalle dodici alle quindici. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nell'elenco | 1 | l'elenco degli ottantacinque semi storicamente distribuiti, percorso a partire dall'indice della voce |
| seme di origine | `0x00000932` | il valore dell'elenco a quella posizione, che è ciò che il verificatore ricostruisce |
| valore di personalità | `0xD17DA4AE` | prime estrazioni, secondo il ramo del metodo |
| natura | Brave | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 21 Att / 21 Dif / 11 Asp / 26 Dsp / 13 Vel | due estrazioni, cinque bit per campo |
| allenatore | `MYSTRY` | dichiarato dalla tabella |
| identificativo, segreto | 6930, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandD3 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 151, `MEW` | numero nazionale 151, nome nella lingua della voce |
| livello, esperienza | 10, 560 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 1, 144 | dichiarate dalla tabella |
| punti potenza | 35, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | sì | dichiarato dalla tabella |
| metodo, lucentezza | BACD_M, Never | dichiarati dalla tabella |
| impronta del file prodotto | `31300d2e5400765fa4207ec93eee8def31e4da45786c8e64b8f58cdb2da2f049` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 001 WISHMKR  (giudizio: conforme, 2026-09-04)

**Jirachi della stella dei desideri, edizione occidentale.** Quando: non ancora documentate con certezza. Dove: non ancora documentato con certezza. Come: disco allegato al titolo per la console domestica, secondo la conoscenza comune, da verificare. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0002` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x838C6EC3` | prime estrazioni, secondo il ramo del metodo |
| natura | Mild | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 27 Att / 20 Dif / 13 Asp / 3 Dsp / 29 Vel | due estrazioni, cinque bit per campo |
| allenatore | `WISHMKR` | dichiarato dalla tabella |
| identificativo, segreto | 20043, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 409, `JIRACHI` | numero nazionale 385, nome nella lingua della voce |
| livello, esperienza | 5, 156 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 273, 93, 156 | dichiarate dalla tabella |
| punti potenza | 10, 25, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | 170 | derivato dalla quinta estrazione |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, Random | dichiarati dalla tabella |
| impronta del file prodotto | `cbe666d261f4776b72e18ebc635daec43ab20224d26f5f46e4b1c5e9558f80c4` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 003 Berry Fix Ruby  (giudizio: conforme, 2026-09-04)

**Berry Program Update Zigzagoon, edizione giapponese con allenatore Rubino.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0004` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x07195598` | prime estrazioni, secondo il ramo del metodo |
| natura | Quirky | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 14 Att / 26 Dif / 6 Asp / 15 Dsp / 7 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ルビー` | dichiarato dalla tabella |
| identificativo, segreto | 21121, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandD3_1 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 288, `ジグザグマ` | numero nazionale 263, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 33, 45, 39 | dichiarate dalla tabella |
| punti potenza | 35, 40, 30 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_RBCD, Always | dichiarati dalla tabella |
| impronta del file prodotto | `8e3c3db5a89278ef5d149fb2437722a38a6db3e4c0b4f52f13e368e11649e99a` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 004 Berry Fix Sapphire  (giudizio: conforme, 2026-09-04)

**Berry Program Update Zigzagoon, edizione giapponese con allenatore Zaffiro.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0005` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x48DF1A5D` | prime estrazioni, secondo il ramo del metodo |
| natura | Naughty | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 30 Att / 21 Dif / 3 Asp / 10 Dsp / 8 Vel | due estrazioni, cinque bit per campo |
| allenatore | `サファイア` | dichiarato dalla tabella |
| identificativo, segreto | 21121, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandD3_0 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 288, `ジグザグマ` | numero nazionale 263, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 33, 45, 39 | dichiarate dalla tabella |
| punti potenza | 35, 40, 30 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_RBCD, Always | dichiarati dalla tabella |
| impronta del file prodotto | `c744bba8e10cad1b0e3cb9a2cde9a18410c12dee06a71c4d84518fbccc7d5d91` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 005 Negai Boshi Jirachi  (giudizio: conforme, 2026-09-04)

**Jirachi della stella dei desideri, edizione giapponese.** Quando: durante il Pokémon Festa 2003, giorno preciso non ancora documentato. Dove: sedi del Pokémon Festa 2003, Giappone. Come: distribuzione senza fili alla manifestazione. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0006` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| seme effettivo | `0x794E19E0` | il seme di origine avanzato di due passi dalla consultazione della tabella dei doni; il verificatore lo dichiara accanto al seme di origine, fra parentesi |
| valore di personalità | `0x5563C5D7` | prime estrazioni, secondo il ramo del metodo |
| natura | Gentle | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 0 Att / 5 Dif / 15 Asp / 22 Dsp / 22 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ネガイボシ` | dichiarato dalla tabella |
| identificativo, segreto | 30719, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 409, `ジラーチ` | numero nazionale 385, nome nella lingua della voce |
| livello, esperienza | 5, 156 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 273, 93, 156 | dichiarate dalla tabella |
| punti potenza | 10, 25, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_TA, Never | dichiarati dalla tabella |
| impronta del file prodotto | `796303bfadc0ceb50249ec0806354d065566c054cdbce1c7bc1c57a4b9e3299e` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 006 Negai Boshi Jirachi (Match Recipient)  (giudizio: conforme, 2026-09-04)

**Jirachi della stella dei desideri, edizione giapponese.** Quando: durante il Pokémon Festa 2003, giorno preciso non ancora documentato. Dove: sedi del Pokémon Festa 2003, Giappone. Come: distribuzione senza fili alla manifestazione. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_U_AX, la lucentezza Never e la lingua Japanese.

### 007 Tanabata Jirachi (2004)  (giudizio: conforme, 2026-09-04)

**Jirachi della festa delle stelle, edizione 2004.** Quando: luglio 2004, giorni precisi non ancora documentati. Dove: Pokémon Center giapponesi. Come: distribuzione senza fili nei negozi. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0008` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x0E32FE93` | prime estrazioni, secondo il ramo del metodo |
| natura | Calm | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 31 PS / 18 Att / 21 Dif / 15 Asp / 8 Dsp / 4 Vel | due estrazioni, cinque bit per campo |
| allenatore | `タナバタ` | dichiarato dalla tabella |
| identificativo, segreto | 40707, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione Only1 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 409, `ジラーチ` | numero nazionale 385, nome nella lingua della voce |
| livello, esperienza | 5, 156 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 273, 93, 156 | dichiarate dalla tabella |
| punti potenza | 10, 25, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ac50f92420fbb7b1942239b8e4521fa8743faeff25bbbb3f8c98189a66298b3e` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 008 ANA Pikachu  (giudizio: conforme, 2026-09-04)

**Pikachu della compagnia aerea.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0009` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x4FF9C135` | prime estrazioni, secondo il ramo del metodo |
| natura | Naive | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 22 Att / 21 Dif / 31 Asp / 3 Dsp / 11 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ＡＮＡ` | dichiarato dalla tabella |
| identificativo, segreto | 41205, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 19, 84, 39, 86 | dichiarate dalla tabella |
| punti potenza | 15, 30, 30, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `9e0afbc71c4a5d1e0598315ce00e01e71efe2ebf6b0ee28db91f3930e7425f2c` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 009 PokéPark Meowth  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x000A` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x91BF83D8` | prime estrazioni, secondo il ramo del metodo |
| natura | Careful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 26 Att / 21 Dif / 15 Asp / 31 Dsp / 17 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 52, `ニャース` | numero nazionale 52, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 10, 45 | dichiarate dalla tabella |
| punti potenza | 35, 40 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `115023425bf87f3c60e16e84284b390518e7134ec8fad5a99098291e0a5872e7` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 010 Yokohama Pikachu  (giudizio: conforme, 2026-09-04)

**Pikachu di Yokohama.** Quando: 19 marzo - 3 aprile 2005. Dove: Pokémon Center di Tokyo, Osaka, Nagoya, Fukuoka e Yokohama. Come: distribuzione senza fili nei negozi. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x000B` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xD385467B` | prime estrazioni, secondo il ramo del metodo |
| natura | Relaxed | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 24 PS / 30 Att / 21 Dif / 31 Asp / 26 Dsp / 24 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ヨコハマ` | dichiarato dalla tabella |
| identificativo, segreto | 50319, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 84, 45, 86, 57 | dichiarate dalla tabella |
| punti potenza | 30, 40, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `85016ba199b72caad98ca06f39cfed6d9e66984b1907551ff281657fe213ed96` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 011 Hadou Mew  (giudizio: conforme, 2026-09-04)

**Mew dell'aura.** Quando: 25 giugno - 31 agosto 2005. Dove: rivenditori che vendevano i biglietti in prevendita per il film. Come: consegnato con la prevendita del biglietto. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x000C` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x154C091D` | prime estrazioni, secondo il ramo del metodo |
| natura | Bold | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 22 PS / 2 Att / 22 Dif / 15 Asp / 22 Dsp / 30 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ハドウ` | dichiarato dalla tabella |
| identificativo, segreto | 50716, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandD3 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 151, `ミュウ` | numero nazionale 151, nome nella lingua della voce |
| livello, esperienza | 10, 560 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 1, 144 | dichiarate dalla tabella |
| punti potenza | 35, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | sì | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `adb256359af66fa5625240e2748d461e2a586ccdde431549c7bae52bc8c575cd` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 012 GW Pikachu  (giudizio: conforme, 2026-09-04)

**Pikachu della settimana d'oro.** Quando: 25 aprile - 8 maggio 2005. Dove: Pokémon Center di Tokyo, Osaka, Nagoya, Fukuoka e Yokohama. Come: distribuzione senza fili nei negozi. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x000D` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x5712CBC0` | prime estrazioni, secondo il ramo del metodo |
| natura | Hardy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 6 Att / 22 Dif / 0 Asp / 18 Dsp / 5 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ＧＷ` | dichiarato dalla tabella |
| identificativo, segreto | 50425, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS3 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 45, 39, 86, 19 | dichiarate dalla tabella |
| punti potenza | 40, 30, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ea7a6b1e81e4ca1ed4a46d1923b088c774212cb78260ba09906fbfc8dd624818` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 013 Sapporo Pikachu  (giudizio: conforme, 2026-09-04)

**Pikachu di Sapporo.** Quando: 1 luglio - 21 agosto 2005. Dove: Pokémon Center di Sapporo. Come: distribuzione senza fili nel negozio. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x000E` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x98D88E62` | prime estrazioni, secondo il ramo del metodo |
| natura | Impish | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 10 Att / 22 Dif / 16 Asp / 13 Dsp / 11 Vel | due estrazioni, cinque bit per campo |
| allenatore | `サッポロ` | dichiarato dalla tabella |
| identificativo, segreto | 50701, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 45, 39, 86, 19 | dichiarate dalla tabella |
| punti potenza | 40, 30, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `743282f5036bd25701ce065810e1dc77def646a53e289f83d59d02b1d1599138` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 014 Tanabata Jirachi (2005)  (giudizio: conforme, 2026-09-04)

**Jirachi della festa delle stelle, edizione 2005.** Quando: 17 luglio - 21 agosto 2005. Dove: sedi del Pokémon Festa 2005, Giappone. Come: distribuzione senza fili alla manifestazione. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x000F` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xDA9E5105` | prime estrazioni, secondo il ramo del metodo |
| natura | Quiet | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 15 PS / 14 Att / 22 Dif / 0 Asp / 9 Dsp / 18 Vel | due estrazioni, cinque bit per campo |
| allenatore | `タナバタ` | dichiarato dalla tabella |
| identificativo, segreto | 50707, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione Only1 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 409, `ジラーチ` | numero nazionale 385, nome nella lingua della voce |
| livello, esperienza | 5, 156 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 273, 93, 156 | dichiarate dalla tabella |
| punti potenza | 10, 25, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `7d6d01147257052ea2cde94a4b8a767344b2067527660fdef21dfdad2c4aa4d5` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 015 Festa Metang  (giudizio: conforme, 2026-09-04)

**Metang della festa.** Quando: 17 luglio - 21 agosto 2005. Dove: sedi del Pokémon Festa 2005, Giappone. Come: consegnato a chi partecipava alla dimostrazione del titolo per la console domestica. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0010` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x1C6513A8` | prime estrazioni, secondo il ramo del metodo |
| natura | Mild | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 18 Att / 22 Dif / 16 Asp / 4 Dsp / 24 Vel | due estrazioni, cinque bit per campo |
| allenatore | `フェスタ` | dichiarato dalla tabella |
| identificativo, segreto | 2005, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 399, `メタング` | numero nazionale 375, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 36, 93, 232, 287 | dichiarate dalla tabella |
| punti potenza | 20, 25, 35, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x200` | RibbonNational |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `66e607396867bbcd2c2791fdea980f2335c8a991932340072b1839b897e2e725` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 016 Sunday Wobbuffet  (giudizio: conforme, 2026-09-04)

**Wobbuffet della trasmissione domenicale.** Quando: 17 luglio - 21 agosto 2005. Dove: sedi del Pokémon Festa 2005, Giappone. Come: distribuzione senza fili alla manifestazione. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0011` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x5E2BD64A` | prime estrazioni, secondo il ramo del metodo |
| natura | Timid | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 22 Att / 22 Dif / 0 Asp / 0 Dsp / 31 Vel | due estrazioni, cinque bit per campo |
| allenatore | `サンデー` | dichiarato dalla tabella |
| identificativo, segreto | 50701, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS3 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 202, `ソーナンス` | numero nazionale 202, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 68, 243, 219, 194 | dichiarate dalla tabella |
| punti potenza | 20, 20, 25, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `e5204c1ca44b8aee3a48136a82e0014841fca404fe0ad2a400abb6b2461ed84f` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 017 Regirock  (giudizio: conforme, 2026-09-04)

**I tre leggendari dell'aura, cioè Regirock, Regice e Registeel.** Quando: 1-25 settembre 2005. Dove: un cinema 109 nelle vicinanze del PokéPark, Giappone. Come: distribuzione senza fili sul posto, anche attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0012` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x9FF198ED` | prime estrazioni, secondo il ramo del metodo |
| natura | Rash | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 26 Att / 22 Dif / 17 Asp / 27 Dsp / 5 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ハドウ` | dichiarato dalla tabella |
| identificativo, segreto | 50901, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandSG15 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 401, `レジロック` | numero nazionale 377, nome nella lingua della voce |
| livello, esperienza | 40, 80000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 174, 276, 246, 63 | dichiarate dalla tabella |
| punti potenza | 10, 5, 5, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `fd97c208e4480ec71911f4e842bf2c64d5b45c23292f549fbba70e1d8ae727f0` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 018 Regice  (giudizio: conforme, 2026-09-04)

**I tre leggendari dell'aura, cioè Regirock, Regice e Registeel.** Quando: 1-25 settembre 2005. Dove: un cinema 109 nelle vicinanze del PokéPark, Giappone. Come: distribuzione senza fili sul posto, anche attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0013` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xE1B85B8F` | prime estrazioni, secondo il ramo del metodo |
| natura | Jolly | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 6 PS / 30 Att / 22 Dif / 1 Asp / 23 Dsp / 12 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ハドウ` | dichiarato dalla tabella |
| identificativo, segreto | 50901, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandSG15 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 402, `レジアイス` | numero nazionale 378, nome nella lingua della voce |
| livello, esperienza | 40, 80000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 174, 276, 246, 63 | dichiarate dalla tabella |
| punti potenza | 10, 5, 5, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `bc8070af52bf520ddf4f770841e3cf2a3920c7209c10f772b4be77e9bff3503a` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 019 Registeel  (giudizio: conforme, 2026-09-04)

**I tre leggendari dell'aura, cioè Regirock, Regice e Registeel.** Quando: 1-25 settembre 2005. Dove: un cinema 109 nelle vicinanze del PokéPark, Giappone. Come: distribuzione senza fili sul posto, anche attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0014` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x237E1E32` | prime estrazioni, secondo il ramo del metodo |
| natura | Lonely | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 2 Att / 23 Dif / 17 Asp / 18 Dsp / 18 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ハドウ` | dichiarato dalla tabella |
| identificativo, segreto | 50901, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandSG15 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 403, `レジスチル` | numero nazionale 379, nome nella lingua della voce |
| livello, esperienza | 40, 80000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 174, 276, 246, 63 | dichiarate dalla tabella |
| punti potenza | 10, 5, 5, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ee7b044f0c85416debf5daf8583cc52be0c904842abd430af96ef94c60ccd61f` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 020 PokéPark Mew  (giudizio: conforme, 2026-09-04)

**Mew del PokéPark.** Quando: 10 maggio - 4 giugno 2006. Dove: negozi Shin Kong Mitsukoshi, Taiwan. Come: distribuzione senza fili nei negozi. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0015` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x6544E0D5` | prime estrazioni, secondo il ramo del metodo |
| natura | Gentle | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 6 Att / 23 Dif / 1 Asp / 14 Dsp / 25 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 60510, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandD3 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 151, `ミュウ` | numero nazionale 151, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 1, 144, 5, 118 | dichiarate dalla tabella |
| punti potenza | 35, 10, 20, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | sì | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `2d951c03412e547223babcdd74f77a4e3c69af2a16e603b917043c320931f7a0` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 021 PokéPark Celebi  (giudizio: conforme, 2026-09-04)

**Celebi del PokéPark.** Quando: 23 giugno - 24 settembre 2006. Dove: PokéPark, Taiwan. Come: distribuzione senza fili sul posto. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0016` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xA70BA377` | prime estrazioni, secondo il ramo del metodo |
| natura | Modest | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 31 PS / 9 Att / 23 Dif / 17 Asp / 9 Dsp / 31 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 60623, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 251, `セレビィ` | numero nazionale 251, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 215, 219, 246, 248 | dichiarate dalla tabella |
| punti potenza | 5, 25, 5, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `9de3651de82a3bbbe77ddddc69bdf63b975d1bfab2a0e0701e0ea7137ea5bfec` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 022 Tanabata Jirachi (2006)  (giudizio: conforme, 2026-09-04)

**Jirachi della festa delle stelle, edizione 2006.** Quando: 15-31 luglio 2006. Dove: Pokémon Center di Tokyo, Yokohama, Nagoya, Osaka, Fukuoka e Sapporo. Come: distribuzione senza fili nei negozi. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0017` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xE8D1661A` | prime estrazioni, secondo il ramo del metodo |
| natura | Quirky | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 29 PS / 13 Att / 23 Dif / 2 Asp / 5 Dsp / 6 Vel | due estrazioni, cinque bit per campo |
| allenatore | `タナバタ` | dichiarato dalla tabella |
| identificativo, segreto | 60707, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 409, `ジラーチ` | numero nazionale 385, nome nella lingua della voce |
| livello, esperienza | 5, 156 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 273, 93, 156 | dichiarate dalla tabella |
| punti potenza | 10, 25, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `e73479e8a5738a6407c61bbe9fc7b523805779595351ee93851069bef0e27119` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 023 Mitsurin Celebi (2006)  (giudizio: conforme, 2026-09-04)

**Celebi della foresta.** Quando: 20 luglio - 3 settembre 2006. Dove: sedi del giro nella giungla, e Pokémon Center di Nagoya, Osaka, Fukuoka e Sapporo. Come: distribuzione senza fili sul posto. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0018` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x2A9728BC` | prime estrazioni, secondo il ramo del metodo |
| natura | Hasty | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 17 Att / 23 Dif / 18 Asp / 0 Dsp / 12 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ミツリン` | dichiarato dalla tabella |
| identificativo, segreto | 60720, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 251, `セレビィ` | numero nazionale 251, nome nella lingua della voce |
| livello, esperienza | 10, 560 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 73, 105, 215, 219 | dichiarate dalla tabella |
| punti potenza | 10, 20, 5, 25 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `e2009818b12e8cb58b41a63bcc3bc14e09049643a517d2d4858b1b3cb4096ec8` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 024 PokéPark Jirachi (2006)  (giudizio: conforme, 2026-09-04)

**Jirachi del PokéPark, prima finestra.** Quando: 24-31 luglio 2006. Dove: PokéPark, Taiwan. Come: distribuzione senza fili ai vincitori di un'estrazione a premi. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0019` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x6C5EEB5F` | prime estrazioni, secondo il ramo del metodo |
| natura | Quiet | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 24 PS / 21 Att / 23 Dif / 2 Asp / 28 Dsp / 19 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 60731, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandD3 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 409, `ジラーチ` | numero nazionale 385, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 273, 94, 270, 156 | dichiarate dalla tabella |
| punti potenza | 10, 10, 20, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `c666ed165b971c1b83bfd9f7a6d6056349dda52ebff81ebcb6bd9725bc4b1641` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 025 PokéPark Jirachi (2006)  (giudizio: conforme, 2026-09-04)

**Jirachi del PokéPark, seconda finestra.** Quando: 23-30 agosto 2006. Dove: PokéPark, Taiwan. Come: distribuzione senza fili ai vincitori di un'estrazione a premi. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x001A` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xAE24AE02` | prime estrazioni, secondo il ramo del metodo |
| natura | Lonely | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 22 PS / 25 Att / 23 Dif / 18 Asp / 23 Dsp / 25 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 60830, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandD3 |
| lingua | Japanese | dichiarata dalla tabella |
| specie interna, soprannome | 409, `ジラーチ` | numero nazionale 385, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 273, 94, 270, 156 | dichiarate dalla tabella |
| punti potenza | 10, 10, 20, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ecc1e3fe0697646d5411bd091ef5973cae671111a1700ed774cfdc4b895486ed` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 026 Berry Fix Ruby  (giudizio: conforme, 2026-09-04)

**Berry Program Update Zigzagoon, edizione inglese con allenatore RUBY.** Quando: 1 marzo 2004 - 22 aprile 2007. Dove: negozi EB Games e GameStop, e disco dimostrativo per la console domestica. Come: distribuzione senza fili nei negozi, oppure dal disco dimostrativo a casa. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x001B` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xEFEA9984` | prime estrazioni, secondo il ramo del metodo |
| natura | Careful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 3 Att / 19 Dif / 2 Asp / 26 Dsp / 4 Vel | due estrazioni, cinque bit per campo |
| allenatore | `RUBY` | dichiarato dalla tabella |
| identificativo, segreto | 30317, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandD3_1 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 288, `ZIGZAGOON` | numero nazionale 263, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 33, 45, 39 | dichiarate dalla tabella |
| punti potenza | 35, 40, 30 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_RBCD, Always | dichiarati dalla tabella |
| impronta del file prodotto | `28e9e4b50fc1ca7d1d9620b7bcf444b08ff3563af9fa843d4e1f43d22815792d` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 027 Berry Fix Sapphire  (giudizio: conforme, 2026-09-04)

**Berry Program Update Zigzagoon, edizione inglese con allenatore SAPHIRE.** Quando: 1 marzo 2004 - 22 aprile 2007. Dove: negozi EB Games e GameStop, e disco dimostrativo per la console domestica. Come: distribuzione senza fili nei negozi, oppure dal disco dimostrativo a casa. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x001D` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x7377051F` | prime estrazioni, secondo il ramo del metodo |
| natura | Timid | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 3 Att / 10 Dif / 28 Asp / 15 Dsp / 7 Vel | due estrazioni, cinque bit per campo |
| allenatore | `SAPHIRE` | dichiarato dalla tabella |
| identificativo, segreto | 30317, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandD3_0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 288, `ZIGZAGOON` | numero nazionale 263, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 33, 45, 39 | dichiarate dalla tabella |
| punti potenza | 35, 40, 30 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_RBCD, Always | dichiarati dalla tabella |
| impronta del file prodotto | `2ea950c07f8dbdfa15809a62d65eca8a3e370d8b2340ef2b6a81174602e0e72b` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 028 Charizard  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x001D` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x7377F5E9` | prime estrazioni, secondo il ramo del metodo |
| natura | Brave | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 15 PS / 5 Att / 24 Dif / 3 Asp / 10 Dsp / 13 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 6, `CHARIZARD` | numero nazionale 6, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 17, 163, 82, 83 | dichiarate dalla tabella |
| punti potenza | 35, 20, 10, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ad364b8d7b984c9f6d7f07ba4b6fe3d59973a94ca1de5f0f809b5aac15f2a0c2` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 029 Pikachu  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x001E` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xB53DB88C` | prime estrazioni, secondo il ramo del metodo |
| natura | Hasty | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 9 Att / 24 Dif / 19 Asp / 5 Dsp / 19 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 85, 97, 87, 113 | dichiarate dalla tabella |
| punti potenza | 15, 30, 10, 30 | dal valore base di ciascuna mossa |
| oggetto tenuto | 202 | documentato dalla provenienza storica |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `fc65754189fb0f415aba0702802115eaeab618cfb4dea38b27952d61e6f724c9` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 030 Articuno  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x001F` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xF7037B2F` | prime estrazioni, secondo il ramo del metodo |
| natura | Calm | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 13 Att / 24 Dif / 3 Asp / 1 Dsp / 26 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 144, `ARTICUNO` | numero nazionale 144, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 170, 58, 115 | dichiarate dalla tabella |
| punti potenza | 30, 5, 10, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `8164097a6a003ce2aba5de1f26fc45679e8ec17793c9640c049acdff56f00be6` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 031 Raikou  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0020` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x38CA3DD1` | prime estrazioni, secondo il ramo del metodo |
| natura | Bashful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 17 Att / 24 Dif / 20 Asp / 28 Dsp / 0 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale 243, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 98, 209, 115, 242 | dichiarate dalla tabella |
| punti potenza | 30, 20, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `99b783849bb947380fecc3e24808d99475a526631672477baeb12ac9213f5114` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 032 Entei  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0021` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x7A900074` | prime estrazioni, secondo il ramo del metodo |
| natura | Brave | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 6 PS / 21 Att / 24 Dif / 4 Asp / 24 Dsp / 7 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale 244, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 83, 23, 53, 207 | dichiarate dalla tabella |
| punti potenza | 15, 20, 15, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `00ce011466799056d81b7512dc039582753a25a87275fbc65099459006ff992b` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 033 Suicune  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0022` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xBC56C316` | prime estrazioni, secondo il ramo del metodo |
| natura | Gentle | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 25 Att / 24 Dif / 20 Asp / 19 Dsp / 13 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale 245, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 16, 62, 54, 243 | dichiarate dalla tabella |
| punti potenza | 35, 20, 30, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `0232ebbb7dc2421f8c605700a08f7dc9443cac0e84fa4137072e9976fc04fe68` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 034 Lugia  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0023` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xFE1D85B9` | prime estrazioni, secondo il ramo del metodo |
| natura | Mild | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 29 Att / 24 Dif / 4 Asp / 15 Dsp / 20 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 249, `LUGIA` | numero nazionale 249, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 105, 56, 240, 129 | dichiarate dalla tabella |
| punti potenza | 20, 5, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `9883449bcde623888a917deb73676979fc23c75938ef79516af26f842a0f8009` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 035 Ho-Oh  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0024` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x3FE3485C` | prime estrazioni, secondo il ramo del metodo |
| natura | Naughty | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 31 PS / 0 Att / 25 Dif / 20 Asp / 10 Dsp / 26 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 250, `HO-OH` | numero nazionale 250, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 105, 126, 241, 129 | dichiarate dalla tabella |
| punti potenza | 20, 5, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `235bc4cf91e2bc5251d9d5a6a3f4e6d44197f1b7b491af0b6d8ffa4e1c734ca0` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 036 Latias  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0025` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x81A90AFE` | prime estrazioni, secondo il ramo del metodo |
| natura | Serious | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 29 PS / 4 Att / 25 Dif / 5 Asp / 6 Dsp / 1 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 407, `LATIAS` | numero nazionale 380, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 296, 94, 105, 204 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `31abb39c1c5efec3ea4db68681a91267ac12665a7d7cf63fad20a98a4b8a352b` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 037 Latios  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0026` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xC370CDA1` | prime estrazioni, secondo il ramo del metodo |
| natura | Bashful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 27 PS / 8 Att / 25 Dif / 21 Asp / 1 Dsp / 7 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 408, `LATIOS` | numero nazionale 381, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 295, 94, 105, 349 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `90923f368c3b270257dfd998b6d72eb4ad36dd988fbf2b403bb20d3cd719d027` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 038 Charizard  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0027` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x05369044` | prime estrazioni, secondo il ramo del metodo |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 24 PS / 12 Att / 25 Dif / 5 Asp / 29 Dsp / 14 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | French | dichiarata dalla tabella |
| specie interna, soprannome | 6, `DRACAUFEU` | numero nazionale 6, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 17, 163, 82, 83 | dichiarate dalla tabella |
| punti potenza | 35, 20, 10, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ab258db48209d219da086ce86f935c6cb52aa3b58736c1130fa275cdfb234329` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 039 Pikachu  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0028` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x46FC52E6` | prime estrazioni, secondo il ramo del metodo |
| natura | Naive | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 22 PS / 16 Att / 25 Dif / 21 Asp / 24 Dsp / 20 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | French | dichiarata dalla tabella |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 85, 97, 87, 113 | dichiarate dalla tabella |
| punti potenza | 15, 30, 10, 30 | dal valore base di ciascuna mossa |
| oggetto tenuto | 202 | documentato dalla provenienza storica |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `aa9274813ebf82cd273b745b302d1f0f07e492d1627e280531e75debfb453375` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 040 Articuno  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0029` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x88C21589` | prime estrazioni, secondo il ramo del metodo |
| natura | Careful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 20 Att / 25 Dif / 5 Asp / 20 Dsp / 27 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | French | dichiarata dalla tabella |
| specie interna, soprannome | 144, `ARTIKODIN` | numero nazionale 144, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 170, 58, 115 | dichiarate dalla tabella |
| punti potenza | 30, 5, 10, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `4271c9d72cce0b48ce32d334af4018609ad0e2b11ada7adae0022ba04a5b9158` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 041 Raikou  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x002A` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xCA89D82B` | prime estrazioni, secondo il ramo del metodo |
| natura | Adamant | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 24 Att / 25 Dif / 22 Asp / 15 Dsp / 1 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | French | dichiarata dalla tabella |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale 243, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 98, 209, 115, 242 | dichiarate dalla tabella |
| punti potenza | 30, 20, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `6cd062bb380598f1544447d1967eb4ffbc08d3d8f08c3015f036ca4ef6248de1` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 042 Entei  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x002B` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x0C4F9ACE` | prime estrazioni, secondo il ramo del metodo |
| natura | Mild | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 15 PS / 28 Att / 25 Dif / 6 Asp / 11 Dsp / 8 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | French | dichiarata dalla tabella |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale 244, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 83, 23, 53, 207 | dichiarate dalla tabella |
| punti potenza | 15, 20, 15, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `7697c47ac0b75c8f759111f64aff1509e351c0aba0d84f5e30138e8f70b02b06` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 043 Suicune  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x002C` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x4E155D71` | prime estrazioni, secondo il ramo del metodo |
| natura | Hardy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 0 Att / 26 Dif / 22 Asp / 6 Dsp / 14 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | French | dichiarata dalla tabella |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale 245, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 16, 62, 54, 243 | dichiarate dalla tabella |
| punti potenza | 35, 20, 30, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `b64cbb36691ea161744ac90524df358d929823495876b453620210ba9a9e4b08` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 044 Lugia  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x002D` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x8FDC2013` | prime estrazioni, secondo il ramo del metodo |
| natura | Rash | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 4 Att / 26 Dif / 6 Asp / 2 Dsp / 21 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | French | dichiarata dalla tabella |
| specie interna, soprannome | 249, `LUGIA` | numero nazionale 249, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 105, 56, 240, 129 | dichiarate dalla tabella |
| punti potenza | 20, 5, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `69dc5082272eb91725d21b49d956e2e75a9a5963c92bb33f239c94cee76709bc` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 045 Ho-Oh  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x002E` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xD1A2E2B6` | prime estrazioni, secondo il ramo del metodo |
| natura | Naive | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 9 PS / 8 Att / 26 Dif / 22 Asp / 29 Dsp / 27 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | French | dichiarata dalla tabella |
| specie interna, soprannome | 250, `HO-OH` | numero nazionale 250, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 105, 126, 241, 129 | dichiarate dalla tabella |
| punti potenza | 20, 5, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `4d179060825d0a3534f26634f9acae3073de65ebd76ef633e52d1e8bd350ac0d` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 046 Latias  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x002F` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x1368A558` | prime estrazioni, secondo il ramo del metodo |
| natura | Lonely | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 6 PS / 12 Att / 26 Dif / 7 Asp / 25 Dsp / 2 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | French | dichiarata dalla tabella |
| specie interna, soprannome | 407, `LATIAS` | numero nazionale 380, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 296, 94, 105, 204 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `d48ebcdb8336c6de84807e8fc22bca8075085b438a796f6d0a74b0b83437918d` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 047 Latios  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione inglese.** Quando: da giugno a dicembre 2006, con una prosecuzione norvegese il 30 marzo e il 10-11 maggio 2008. Dove: campionati nazionali del Regno Unito, tappe del giro europeo, manifestazioni Nintendo in Grecia, Repubblica Ceca, Paesi Bassi e Finlandia. Come: distribuzione senza fili alle manifestazioni, e programmi per posta in Svezia e Danimarca. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0030` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x552F67FB` | prime estrazioni, secondo il ramo del metodo |
| natura | Gentle | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 16 Att / 26 Dif / 23 Asp / 20 Dsp / 8 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | French | dichiarata dalla tabella |
| specie interna, soprannome | 408, `LATIOS` | numero nazionale 381, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 295, 94, 105, 349 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `fdb931bf21dae764fe8bb6944cbdf3ca3607bb42cabb7b754a7dd6e4291db043` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 048 Charizard  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione tedesca.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0031` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x96F52A9E` | prime estrazioni, secondo il ramo del metodo |
| natura | Bold | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 20 Att / 26 Dif / 7 Asp / 16 Dsp / 15 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10JAHRE` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | German | dichiarata dalla tabella |
| specie interna, soprannome | 6, `GLURAK` | numero nazionale 6, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 17, 163, 82, 83 | dichiarate dalla tabella |
| punti potenza | 35, 20, 10, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `9c43f7b358ffef1cf59c85d889c8c14933a70657e5ff26a42b49f358def75f49` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 049 Pikachu  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione tedesca.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0032` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xD8BBED40` | prime estrazioni, secondo il ramo del metodo |
| natura | Quirky | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 24 Att / 26 Dif / 23 Asp / 11 Dsp / 21 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10JAHRE` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | German | dichiarata dalla tabella |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 85, 97, 87, 113 | dichiarate dalla tabella |
| punti potenza | 15, 30, 10, 30 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `a86843a1cd497f8fa4554e333a68581328c5f2062f63d7502dc054109815169e` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 050 Articuno  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione tedesca.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0033` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x1A82AFE3` | prime estrazioni, secondo il ramo del metodo |
| natura | Careful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 29 PS / 27 Att / 26 Dif / 7 Asp / 7 Dsp / 28 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10JAHRE` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | German | dichiarata dalla tabella |
| specie interna, soprannome | 144, `ARKTOS` | numero nazionale 144, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 170, 58, 115 | dichiarate dalla tabella |
| punti potenza | 30, 5, 10, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ba15de3eef5b8ed4076e5f63a31996d1032b603d6e55249a113bcd2ed40d70b2` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 051 Raikou  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione tedesca.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0034` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x5C487285` | prime estrazioni, secondo il ramo del metodo |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 27 PS / 31 Att / 26 Dif / 24 Asp / 2 Dsp / 2 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10JAHRE` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | German | dichiarata dalla tabella |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale 243, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 98, 209, 115, 242 | dichiarate dalla tabella |
| punti potenza | 30, 20, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `f83e3fbf640cf90253eaf626dd788740e78257e77e4b052fdb7621466a479d97` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 052 Entei  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione tedesca.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0035` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x9E0E3528` | prime estrazioni, secondo il ramo del metodo |
| natura | Modest | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 3 Att / 27 Dif / 8 Asp / 30 Dsp / 9 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10JAHRE` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | German | dichiarata dalla tabella |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale 244, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 83, 23, 53, 207 | dichiarate dalla tabella |
| punti potenza | 15, 20, 15, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `38ff2be0520751cf96b7773c33632444ed703d39e41eefef3caec4f3df8af217` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 053 Suicune  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione tedesca.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0036` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xDFD4F7CB` | prime estrazioni, secondo il ramo del metodo |
| natura | Timid | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 7 Att / 27 Dif / 24 Asp / 25 Dsp / 15 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10JAHRE` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | German | dichiarata dalla tabella |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale 245, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 16, 62, 54, 243 | dichiarate dalla tabella |
| punti potenza | 35, 20, 30, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `963633df15514bd410517c1cc4e7edac8988f9f0dee5f2770662e74df1a49666` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 054 Lugia  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione tedesca.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0037` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x219BBA6D` | prime estrazioni, secondo il ramo del metodo |
| natura | Impish | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 11 Att / 27 Dif / 8 Asp / 21 Dsp / 22 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10JAHRE` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | German | dichiarata dalla tabella |
| specie interna, soprannome | 249, `LUGIA` | numero nazionale 249, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 105, 56, 240, 129 | dichiarate dalla tabella |
| punti potenza | 20, 5, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `b0202eafbba5598fed3c3959308c9d4582d57caf3cb87f05cf552ae308244024` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 055 Ho-Oh  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione tedesca.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0038` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x63617D10` | prime estrazioni, secondo il ramo del metodo |
| natura | Quiet | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 15 Att / 27 Dif / 24 Asp / 16 Dsp / 28 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10JAHRE` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | German | dichiarata dalla tabella |
| specie interna, soprannome | 250, `HO-OH` | numero nazionale 250, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 105, 126, 241, 129 | dichiarate dalla tabella |
| punti potenza | 20, 5, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ceee18ae0f6be55fe4465e74ea349e07ad95c9946f67f48251c73c9f6d2b0476` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 056 Latias  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione tedesca.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0039` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xA5273FB2` | prime estrazioni, secondo il ramo del metodo |
| natura | Hardy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 16 PS / 19 Att / 27 Dif / 9 Asp / 12 Dsp / 3 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10JAHRE` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | German | dichiarata dalla tabella |
| specie interna, soprannome | 407, `LATIAS` | numero nazionale 380, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 296, 94, 105, 204 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `cb0ce8aff4fba315c48c5c1f96001953fa232fc9feab897305be647888411bf7` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 057 Latios  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione tedesca.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x003A` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xE6EE0255` | prime estrazioni, secondo il ramo del metodo |
| natura | Calm | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 23 Att / 27 Dif / 25 Asp / 7 Dsp / 9 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10JAHRE` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | German | dichiarata dalla tabella |
| specie interna, soprannome | 408, `LATIOS` | numero nazionale 381, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 295, 94, 105, 349 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `dc829333fd7f216d401b505586878b401c3e4230812320c55f1f3f6e360fed49` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 058 Charizard  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione italiana.** Quando: 23-25 giugno 2006. Dove: parco di Mirabilandia, Italia. Come: distribuzione senza fili al parco. Fonte: [List of Italian event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x003B` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x28B4C4F8` | prime estrazioni, secondo il ramo del metodo |
| natura | Rash | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 27 Att / 27 Dif / 9 Asp / 3 Dsp / 16 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNI` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Italian | dichiarata dalla tabella |
| specie interna, soprannome | 6, `CHARIZARD` | numero nazionale 6, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 17, 163, 82, 83 | dichiarate dalla tabella |
| punti potenza | 35, 20, 10, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `7ccc06e4700ed4af00f222da2e4564b03b29d3a7a438c35915ae7ba460c6bee6` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 059 Pikachu  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione italiana.** Quando: 23-25 giugno 2006. Dove: parco di Mirabilandia, Italia. Come: distribuzione senza fili al parco. Fonte: [List of Italian event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x003C` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x6A7A879A` | prime estrazioni, secondo il ramo del metodo |
| natura | Brave | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 9 PS / 31 Att / 27 Dif / 25 Asp / 30 Dsp / 22 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNI` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Italian | dichiarata dalla tabella |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 85, 97, 87, 113 | dichiarate dalla tabella |
| punti potenza | 15, 30, 10, 30 | dal valore base di ciascuna mossa |
| oggetto tenuto | 202 | documentato dalla provenienza storica |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `c124c3c9d064b0c6d3a8bc1c1d479fe21adf4d8d9828f5d74617d561a0dcce25` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 060 Articuno  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione italiana.** Quando: 23-25 giugno 2006. Dove: parco di Mirabilandia, Italia. Come: distribuzione senza fili al parco. Fonte: [List of Italian event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x003D` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xAC414A3D` | prime estrazioni, secondo il ramo del metodo |
| natura | Sassy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 3 Att / 28 Dif / 9 Asp / 26 Dsp / 29 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNI` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Italian | dichiarata dalla tabella |
| specie interna, soprannome | 144, `ARTICUNO` | numero nazionale 144, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 170, 58, 115 | dichiarate dalla tabella |
| punti potenza | 30, 5, 10, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `abc87c551303968edecec9c66ec7d87e0cf68e87f9ca11565567aeb68f21baac` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 061 Raikou  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione italiana.** Quando: 23-25 giugno 2006. Dove: parco di Mirabilandia, Italia. Come: distribuzione senza fili al parco. Fonte: [List of Italian event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x003E` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xEE070CDF` | prime estrazioni, secondo il ramo del metodo |
| natura | Bold | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 7 Att / 28 Dif / 26 Asp / 21 Dsp / 3 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNI` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Italian | dichiarata dalla tabella |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale 243, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 98, 209, 115, 242 | dichiarate dalla tabella |
| punti potenza | 30, 20, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `e4109890990e37064e63fe21ee5e22fa680472bcba8917b6ef0e37249cac168a` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 062 Entei  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione italiana.** Quando: 23-25 giugno 2006. Dove: parco di Mirabilandia, Italia. Come: distribuzione senza fili al parco. Fonte: [List of Italian event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x003F` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x2FCDCF82` | prime estrazioni, secondo il ramo del metodo |
| natura | Naughty | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 11 Att / 28 Dif / 10 Asp / 17 Dsp / 10 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNI` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Italian | dichiarata dalla tabella |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale 244, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 83, 23, 53, 207 | dichiarate dalla tabella |
| punti potenza | 15, 20, 15, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `f01c512e8afa109137709982fb36bae7c6a40cd6b0565c387be73190eef82759` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 063 Suicune  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione italiana.** Quando: 23-25 giugno 2006. Dove: parco di Mirabilandia, Italia. Come: distribuzione senza fili al parco. Fonte: [List of Italian event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0040` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x71939225` | prime estrazioni, secondo il ramo del metodo |
| natura | Jolly | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 15 Att / 28 Dif / 26 Asp / 12 Dsp / 16 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNI` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Italian | dichiarata dalla tabella |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale 245, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 16, 62, 54, 243 | dichiarate dalla tabella |
| punti potenza | 35, 20, 30, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `7dda2b88c8363aae0111081c1f55ea0b67b6c57b02e86a6b9111569c576c64de` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 064 Lugia  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione italiana.** Quando: 23-25 giugno 2006. Dove: parco di Mirabilandia, Italia. Come: distribuzione senza fili al parco. Fonte: [List of Italian event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0041` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xB35A54C7` | prime estrazioni, secondo il ramo del metodo |
| natura | Relaxed | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 18 Att / 28 Dif / 10 Asp / 8 Dsp / 23 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNI` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Italian | dichiarata dalla tabella |
| specie interna, soprannome | 249, `LUGIA` | numero nazionale 249, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 105, 56, 240, 129 | dichiarate dalla tabella |
| punti potenza | 20, 5, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ab634a851deec1444f87df272906d9ce37f308b83dbeb83f639fc22cf5ef1ce6` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 065 Ho-Oh  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione italiana.** Quando: 23-25 giugno 2006. Dove: parco di Mirabilandia, Italia. Come: distribuzione senza fili al parco. Fonte: [List of Italian event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0042` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xF520176A` | prime estrazioni, secondo il ramo del metodo |
| natura | Mild | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 27 PS / 22 Att / 28 Dif / 26 Asp / 3 Dsp / 29 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNI` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Italian | dichiarata dalla tabella |
| specie interna, soprannome | 250, `HO-OH` | numero nazionale 250, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 105, 126, 241, 129 | dichiarate dalla tabella |
| punti potenza | 20, 5, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `5954b1af579183afdcdd8760979c996342436ca5ee38cec3e8bcc367dd6eefe2` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 066 Latias  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione italiana.** Quando: 23-25 giugno 2006. Dove: parco di Mirabilandia, Italia. Come: distribuzione senza fili al parco. Fonte: [List of Italian event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0043` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x36E6DA0C` | prime estrazioni, secondo il ramo del metodo |
| natura | Naive | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 26 Att / 28 Dif / 11 Asp / 31 Dsp / 4 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNI` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Italian | dichiarata dalla tabella |
| specie interna, soprannome | 407, `LATIAS` | numero nazionale 380, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 296, 94, 105, 204 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `9c8b3a72c9bbeb67289cb2b4893a8aa62e39bead1074dcbdfdbd1641ee931e00` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 067 Latios  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione italiana.** Quando: 23-25 giugno 2006. Dove: parco di Mirabilandia, Italia. Come: distribuzione senza fili al parco. Fonte: [List of Italian event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0044` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x78AD9CAF` | prime estrazioni, secondo il ramo del metodo |
| natura | Lax | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 30 Att / 28 Dif / 27 Asp / 26 Dsp / 10 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANNI` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Italian | dichiarata dalla tabella |
| specie interna, soprannome | 408, `LATIOS` | numero nazionale 381, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 295, 94, 105, 349 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `25fc21fcbc8f37d70c7e159584ed06e6f847d1babe4af1eea29ea5067a1a90bf` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 068 Charizard  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione spagnola.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0045` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xBA735F52` | prime estrazioni, secondo il ramo del metodo |
| natura | Bashful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 2 Att / 29 Dif / 11 Asp / 22 Dsp / 17 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Spanish | dichiarata dalla tabella |
| specie interna, soprannome | 6, `CHARIZARD` | numero nazionale 6, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 17, 163, 82, 83 | dichiarate dalla tabella |
| punti potenza | 35, 20, 10, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `d288162ce833427180bc8a972214703731f9ca04e4e31f2686b34c55183bd553` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 069 Pikachu  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione spagnola.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0046` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xFC3921F4` | prime estrazioni, secondo il ramo del metodo |
| natura | Lonely | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 6 Att / 29 Dif / 27 Asp / 17 Dsp / 23 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Spanish | dichiarata dalla tabella |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 85, 97, 87, 113 | dichiarate dalla tabella |
| punti potenza | 15, 30, 10, 30 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `3ec69c5d9b1da0ffa8e3fc36fd44b0544aaa29a3d023579ae0472207a9f5e1b5` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 070 Articuno  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione spagnola.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0047` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x3E00E497` | prime estrazioni, secondo il ramo del metodo |
| natura | Hasty | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 16 PS / 10 Att / 29 Dif / 11 Asp / 13 Dsp / 30 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Spanish | dichiarata dalla tabella |
| specie interna, soprannome | 144, `ARTICUNO` | numero nazionale 144, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 170, 58, 115 | dichiarate dalla tabella |
| punti potenza | 30, 5, 10, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `982573e72c9fe73b9c4150c4369d3d908f28cf484e59cff79756e91518fe16f0` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 071 Raikou  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione spagnola.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0048` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x7FC6A739` | prime estrazioni, secondo il ramo del metodo |
| natura | Rash | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 14 PS / 14 Att / 29 Dif / 28 Asp / 8 Dsp / 4 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Spanish | dichiarata dalla tabella |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale 243, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 98, 209, 115, 242 | dichiarate dalla tabella |
| punti potenza | 30, 20, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `3c1902390a1d7ac94bf712b183d5682198fbefd0703821a5798a01d685e6a8d5` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 072 Entei  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione spagnola.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0049` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xC18C69DC` | prime estrazioni, secondo il ramo del metodo |
| natura | Adamant | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 18 Att / 29 Dif / 12 Asp / 4 Dsp / 11 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Spanish | dichiarata dalla tabella |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale 244, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 83, 23, 53, 207 | dichiarate dalla tabella |
| punti potenza | 15, 20, 15, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `0bb457e53851445214f5b2f8ffda2b0a06b3f5c2fbbb32e0828f029c9c99eea7` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 073 Suicune  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione spagnola.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x004A` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x03532C7F` | prime estrazioni, secondo il ramo del metodo |
| natura | Brave | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 9 PS / 22 Att / 29 Dif / 28 Asp / 31 Dsp / 17 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Spanish | dichiarata dalla tabella |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale 245, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 16, 62, 54, 243 | dichiarate dalla tabella |
| punti potenza | 35, 20, 30, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `4cc2b5aba9aa4fb6a4a95693d2672f6d0d706c0c7bc6c025afb2744ef3c970b2` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 074 Lugia  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione spagnola.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x004B` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x4519EF21` | prime estrazioni, secondo il ramo del metodo |
| natura | Gentle | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 26 Att / 29 Dif / 12 Asp / 27 Dsp / 24 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Spanish | dichiarata dalla tabella |
| specie interna, soprannome | 249, `LUGIA` | numero nazionale 249, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 105, 56, 240, 129 | dichiarate dalla tabella |
| punti potenza | 20, 5, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `152174f2113d7b0c0b837505087e45205212a211eebc51505d6a16c5ec4ee4ec` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 075 Ho-Oh  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione spagnola.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x004C` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x86DFB1C4` | prime estrazioni, secondo il ramo del metodo |
| natura | Bold | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 30 Att / 29 Dif / 28 Asp / 22 Dsp / 30 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Spanish | dichiarata dalla tabella |
| specie interna, soprannome | 250, `HO-OH` | numero nazionale 250, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 105, 126, 241, 129 | dichiarate dalla tabella |
| punti potenza | 20, 5, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `00d3ccaa15a8c0585e0668d2caf4eec6b473748de853102cf248cad278c8d580` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 076 Latias  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione spagnola.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x004D` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xC8A57466` | prime estrazioni, secondo il ramo del metodo |
| natura | Jolly | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 2 Att / 30 Dif / 13 Asp / 18 Dsp / 5 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | Spanish | dichiarata dalla tabella |
| specie interna, soprannome | 407, `LATIAS` | numero nazionale 380, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 296, 94, 105, 204 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ee1ef7d7afd61d4d255db134be99e63ef908b0c575ea90daf3098844b2a1bd23` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 077 Latios  (giudizio: conforme, 2026-09-04)

**Top 10 Distribution Pokémon, edizione spagnola.** Quando: non ancora documentate. Dove: non ancora documentato. Come: distribuzione senza fili. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x004E` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x0A6C3709` | prime estrazioni, secondo il ramo del metodo |
| natura | Serious | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 6 Att / 30 Dif / 29 Asp / 13 Dsp / 11 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6227, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | Spanish | dichiarata dalla tabella |
| specie interna, soprannome | 408, `LATIOS` | numero nazionale 381, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 295, 94, 105, 349 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `447fe4a352c032de20cef240d607ff34640889829dca06766a9c9504f4dc476d` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 078 Mew  (giudizio: conforme, 2026-09-04)

**Aura Mew.** Quando: 2-26 agosto 2007 nel Regno Unito, 25-28 ottobre 2007 in Norvegia, 5 novembre - 14 dicembre 2007 in Svezia, 3-30 gennaio 2008 in Danimarca; 7-8 luglio 2007 in Italia. Dove: negozi Toys "R" Us nel Regno Unito, manifestazioni e distribuzioni per posta nei paesi nordici, parco di Mirabilandia in Italia. Come: distribuzione senza fili alle manifestazioni, e per posta nei due paesi nordici dove non si tenne un evento. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x004F` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x4C32F9AC` | prime estrazioni, secondo il ramo del metodo |
| natura | Relaxed | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 9 Att / 30 Dif / 13 Asp / 9 Dsp / 18 Vel | due estrazioni, cinque bit per campo |
| allenatore | `Aura` | dichiarato dalla tabella |
| identificativo, segreto | 20078, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 151, `MEW` | numero nazionale 151, nome nella lingua della voce |
| livello, esperienza | 10, 560 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 1, 144 | dichiarate dalla tabella |
| punti potenza | 35, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | sì | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `e634412000b7bdca91511f9de34c69dc60d981660a24b5c20c45c24215fa8093` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 079 Metang  (giudizio: conforme, 2026-09-04)

**Pokémon Rocks America 2005 Metang.** Quando: 17 settembre - 22 ottobre 2005. Dove: cinque città degli Stati Uniti, cioè San Jose, Phoenix, Dallas, Chicago e Boston. Come: consegnato a chi completava la dimostrazione del titolo per la console domestica, tramite una tessera. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0050` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x8DF8BC4E` | prime estrazioni, secondo il ramo del metodo |
| natura | Modest | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 13 Att / 30 Dif / 29 Asp / 4 Dsp / 24 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ROCKS` | dichiarato dalla tabella |
| identificativo, segreto | 2005, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 399, `METANG` | numero nazionale 375, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 36, 93, 232, 287 | dichiarate dalla tabella |
| punti potenza | 20, 25, 35, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x200` | RibbonNational |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `213c7e7a8c2397b42fea4d9334b045b158ac130ae25e1179672f3b06a3a3b429` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 080 Deoxys  (giudizio: conforme, 2026-09-04)

**Doel Deoxys.** Quando: 25-28 maggio 2006. Dove: TV Toy Museum nei Paesi Bassi, durante i Pokémon Fan Days 2006. Come: distribuzione senza fili alla manifestazione. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0051` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xCFBF7EF1` | prime estrazioni, secondo il ramo del metodo |
| natura | Timid | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 17 Att / 30 Dif / 13 Asp / 0 Dsp / 31 Vel | due estrazioni, cinque bit per campo |
| allenatore | `DOEL` | dichiarato dalla tabella |
| identificativo, segreto | 28606, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 410, `DEOXYS` | numero nazionale 386, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 322, 105, 354, 63 | dichiarate dalla tabella |
| punti potenza | 20, 20, 5, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | sì | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `572f6c6bce0ff1adc3a471712615f6afcaf64deb8753dfc6e97cd2073709ec12` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 081 Deoxys  (giudizio: conforme, 2026-09-04)

**Space Center Deoxys.** Quando: dal 10 al 19 marzo 2006, e poi ogni sabato e domenica fino al 14 maggio 2006. Dove: Space Center Houston, Stati Uniti. Come: distribuzione senza fili sul posto. Fonte: [List of English event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0052` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x11854193` | prime estrazioni, secondo il ramo del metodo |
| natura | Sassy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 21 Att / 30 Dif / 30 Asp / 27 Dsp / 5 Vel | due estrazioni, cinque bit per campo |
| allenatore | `SPACE C` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 410, `DEOXYS` | numero nazionale 386, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 322, 105, 354, 63 | dichiarate dalla tabella |
| punti potenza | 20, 20, 5, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | sì | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `936625241e16342f4036f85f63582ce7ab3185b132e0b4ef2899c883a4fc9538` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 082 Bulbasaur  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0053` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x534B0436` | prime estrazioni, secondo il ramo del metodo |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 25 Att / 30 Dif / 14 Asp / 23 Dsp / 12 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 1, `BULBASAUR` | numero nazionale 1, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 230, 74, 76, 235 | dichiarate dalla tabella |
| punti potenza | 20, 40, 10, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `13967d86cd21a0d0226e2062bb376aded40f5f056f1834990f30152a7fb8216e` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 083 Charizard  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0054` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x9512C6D9` | prime estrazioni, secondo il ramo del metodo |
| natura | Serious | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 29 Att / 30 Dif / 30 Asp / 18 Dsp / 18 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 6, `CHARIZARD` | numero nazionale 6, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 17, 163, 82, 83 | dichiarate dalla tabella |
| punti potenza | 35, 20, 10, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `fb2fcbdacb6bc245d9c71134bee044e072b0a3c13670a932d6eb154b7d2893ae` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 084 Blastoise  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0055` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xD6D8897B` | prime estrazioni, secondo il ramo del metodo |
| natura | Calm | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 16 PS / 1 Att / 31 Dif / 14 Asp / 14 Dsp / 25 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 9, `BLASTOISE` | numero nazionale 9, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 182, 240, 130, 56 | dichiarate dalla tabella |
| punti potenza | 10, 5, 15, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `1629796710f705705266d8fe28d8b491bd3733258e116f6b41bc02859491c36b` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 085 Pikachu (Fly)  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0056` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x189E4C1E` | prime estrazioni, secondo il ramo del metodo |
| natura | Impish | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 14 PS / 5 Att / 31 Dif / 30 Asp / 9 Dsp / 31 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 85, 87, 113, 19 | dichiarate dalla tabella |
| punti potenza | 15, 10, 30, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `4c88dcb14be753e23fd3260c4bb7506bbdb15d56fdf6828aee0e534c5567f334` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 086 Alakazam  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0057` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x5A650EC0` | prime estrazioni, secondo il ramo del metodo |
| natura | Brave | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 9 Att / 31 Dif / 15 Asp / 5 Dsp / 6 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 65, `ALAKAZAM` | numero nazionale 65, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 248, 347, 94, 271 | dichiarate dalla tabella |
| punti potenza | 15, 20, 10, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `29879c75b80e4487833122984d0e4ed0eec90fca1442ba6b30c30b79f419c7f0` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 087 Articuno  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0058` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x9C2BD163` | prime estrazioni, secondo il ramo del metodo |
| natura | Sassy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 13 Att / 31 Dif / 31 Asp / 0 Dsp / 12 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 144, `ARTICUNO` | numero nazionale 144, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 170, 58, 115 | dichiarate dalla tabella |
| punti potenza | 30, 5, 10, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `a747dc4baec476fdbf60a06bfd54c749b9e6059e5cdc899a889d4299c86f4d85` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 088 Zapdos  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0059` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xDDF19406` | prime estrazioni, secondo il ramo del metodo |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 17 Att / 31 Dif / 15 Asp / 28 Dsp / 19 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 145, `ZAPDOS` | numero nazionale 145, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 197, 65, 268 | dichiarate dalla tabella |
| punti potenza | 30, 5, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `d1d233b0d2106288d518148dbd17eafd08fc50503ce0772f7d6d04ad24555745` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 089 Moltres  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x005A` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x1FB756A8` | prime estrazioni, secondo il ramo del metodo |
| natura | Bashful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 21 Att / 31 Dif / 31 Asp / 23 Dsp / 25 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 146, `MOLTRES` | numero nazionale 146, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 203, 53, 219 | dichiarate dalla tabella |
| punti potenza | 30, 10, 15, 25 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `412edf97ccaeb07b074bca17a9b0579169187bf65efd64f08ef8c6226ced33bf` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 090 Dragonite  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x005B` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x617E194B` | prime estrazioni, secondo il ramo del metodo |
| natura | Jolly | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 25 Att / 31 Dif / 16 Asp / 19 Dsp / 0 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 149, `DRAGONITE` | numero nazionale 149, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 219, 17, 200 | dichiarate dalla tabella |
| punti potenza | 30, 25, 35, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `ac7e17d56c6cb9adcf6df3ed6509a4a08e131169219b74724aaaa5341673b88b` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 091 Typhlosion  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x005C` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xA344DBED` | prime estrazioni, secondo il ramo del metodo |
| natura | Relaxed | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 29 Att / 31 Dif / 0 Asp / 15 Dsp / 6 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 157, `TYPHLOSION` | numero nazionale 157, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 98, 172, 129, 53 | dichiarate dalla tabella |
| punti potenza | 30, 25, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `c241a14afd7b9439c4f9cfefe86340261bda28e602620ad4376846162945e59f` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 092 Espeon  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x005D` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xE50A9E90` | prime estrazioni, secondo il ramo del metodo |
| natura | Mild | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 0 Att / 0 Dif / 16 Asp / 10 Dsp / 13 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 196, `ESPEON` | numero nazionale 196, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 60, 244, 94, 234 | dichiarate dalla tabella |
| punti potenza | 20, 10, 10, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `826f321dae134d1b8b2a922e6777ebf17adef6e50c43722771a5d39a0baa9192` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 093 Umbreon  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x005E` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x26D16133` | prime estrazioni, secondo il ramo del metodo |
| natura | Modest | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 4 Att / 0 Dif / 0 Asp / 6 Dsp / 19 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 197, `UMBREON` | numero nazionale 197, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 185, 212, 103, 236 | dichiarate dalla tabella |
| punti potenza | 20, 5, 40, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `a383e00df616f5e7e30b44a1725766147f93422e91aacd3c04a5645734cb2454` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 094 Raikou  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x005F` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x689723D5` | prime estrazioni, secondo il ramo del metodo |
| natura | Careful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 8 Att / 0 Dif / 16 Asp / 1 Dsp / 26 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale 243, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 98, 209, 115, 242 | dichiarate dalla tabella |
| punti potenza | 30, 20, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `1c0e8dc3ed44253d6d8a6ead2c9f3cd7c8a75cb47cbd2253ed6db674eebab081` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 095 Entei  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0060` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xAA5DE678` | prime estrazioni, secondo il ramo del metodo |
| natura | Bashful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 12 Att / 0 Dif / 1 Asp / 29 Dsp / 0 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale 244, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 83, 23, 53, 207 | dichiarate dalla tabella |
| punti potenza | 15, 20, 15, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `456a1e2c82e4d9114051a4d084ba0836572997f3e412ba061daf4d6f78080153` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 096 Suicune  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0061` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xEC24A91A` | prime estrazioni, secondo il ramo del metodo |
| natura | Serious | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 16 Att / 0 Dif / 17 Asp / 24 Dsp / 7 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale 245, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 16, 62, 54, 243 | dichiarate dalla tabella |
| punti potenza | 35, 20, 30, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `7e18fa7fc87cc1dc39e94fc1900b09f828c1d966b0317e5c834140b4e4b9924e` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 097 Tyranitar  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0062` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x2DEA6BBD` | prime estrazioni, secondo il ramo del metodo |
| natura | Hardy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 20 Att / 0 Dif / 1 Asp / 20 Dsp / 13 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 248, `TYRANITAR` | numero nazionale 248, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 37, 184, 242, 89 | dichiarate dalla tabella |
| punti potenza | 20, 10, 15, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `9bf392ea311227aa6ef99806f64fa5b364deec71bc2d2712918414cbeae99eef` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 098 Blaziken  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0063` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x6FB02E60` | prime estrazioni, secondo il ramo del metodo |
| natura | Lax | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 24 Att / 0 Dif / 17 Asp / 15 Dsp / 20 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 282, `BLAZIKEN` | numero nazionale 257, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 299, 163, 119, 327 | dichiarate dalla tabella |
| punti potenza | 10, 20, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `9724d9b7c9bfa8fcb99f8207a345327b6f2a60fccad4075e1c94f8c7c135895f` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 099 Absol  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0064` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xB177F102` | prime estrazioni, secondo il ramo del metodo |
| natura | Naive | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 14 PS / 28 Att / 0 Dif / 1 Asp / 11 Dsp / 26 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 376, `ABSOL` | numero nazionale 359, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 104, 163, 248, 195 | dichiarate dalla tabella |
| punti potenza | 15, 20, 15, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `06767db60edd90b0761c3975aa8f85c4e94261fcba2e51ce6706271c406ced43` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 100 Latias  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0065` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xF33DB3A5` | prime estrazioni, secondo il ramo del metodo |
| natura | Careful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 0 Att / 1 Dif / 18 Asp / 6 Dsp / 0 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 407, `LATIAS` | numero nazionale 380, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 296, 94, 105, 204 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `678a4e9af5ce57c23a2403ea26ca3b80024db003735659298dabee1caed5de6a` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 101 Latios  (giudizio: conforme, 2026-09-04)

**Festa del decennale, prima serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0066` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x35037648` | prime estrazioni, secondo il ramo del metodo |
| natura | Hasty | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 4 Att / 1 Dif / 2 Asp / 2 Dsp / 7 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 6808, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 408, `LATIOS` | numero nazionale 381, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 295, 94, 105, 349 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `95b859e64e135c6cb774cdba87e7bf25bb2fcf0e37bf17c3e2a08e38a1b24ea8` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 102 Bulbasaur  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0067` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x76C938EA` | prime estrazioni, secondo il ramo del metodo |
| natura | Rash | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 8 Att / 1 Dif / 18 Asp / 29 Dsp / 13 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 1, `BULBASAUR` | numero nazionale 1, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 230, 74, 76, 235 | dichiarate dalla tabella |
| punti potenza | 20, 40, 10, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `a32ccff1679e2fad81bb25591095dd6c8687449617aa718fe2d8052b935cfbf6` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 103 Charizard  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0068` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xB890FB8D` | prime estrazioni, secondo il ramo del metodo |
| natura | Hardy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 12 Att / 1 Dif / 2 Asp / 25 Dsp / 20 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 6, `CHARIZARD` | numero nazionale 6, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 17, 163, 82, 83 | dichiarate dalla tabella |
| punti potenza | 35, 20, 10, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `b527c465ab31cfcc99a7fcf04a873ce425727003bd9be220ecc45a0f23c8b389` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 104 Blastoise  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0069` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xFA56BE2F` | prime estrazioni, secondo il ramo del metodo |
| natura | Impish | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 16 Att / 1 Dif / 18 Asp / 20 Dsp / 26 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 9, `BLASTOISE` | numero nazionale 9, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 182, 240, 130, 56 | dichiarate dalla tabella |
| punti potenza | 10, 5, 15, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `7facdbd78bd1792023fee5ed641439d44899d702f13ccdd77db16e3caef76349` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 105 Pikachu (No Fly)  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x006A` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x3C1C80D2` | prime estrazioni, secondo il ramo del metodo |
| natura | Gentle | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 20 Att / 1 Dif / 3 Asp / 16 Dsp / 1 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale 25, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 85, 97, 87, 113 | dichiarate dalla tabella |
| punti potenza | 15, 30, 10, 30 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `fe03c86d37384e28f0fcd1593fed86afb1e1da0965d93fe2677491ca85e4b152` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 106 Alakazam  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x006B` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x7DE34375` | prime estrazioni, secondo il ramo del metodo |
| natura | Mild | resto per venticinque del valore di personalità |
| bit dell'abilità | 1 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 31 PS / 23 Att / 1 Dif / 19 Asp / 11 Dsp / 7 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 65, `ALAKAZAM` | numero nazionale 65, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 248, 347, 94, 271 | dichiarate dalla tabella |
| punti potenza | 15, 20, 10, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `f4a39c18f4c578dce21e6630bae5bb43c16f4659be97bd7e95b099f16afabea6` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 107 Articuno  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x006C` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xBFA90617` | prime estrazioni, secondo il ramo del metodo |
| natura | Quirky | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 27 Att / 1 Dif / 3 Asp / 7 Dsp / 14 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 144, `ARTICUNO` | numero nazionale 144, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 170, 58, 115 | dichiarate dalla tabella |
| punti potenza | 30, 5, 10, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `4e359d99c9204bf0b09ca32df20fb4c576e0552e93c6d71cd256779ce6b1dd5b` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 108 Zapdos  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x006D` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x016FC8BA` | prime estrazioni, secondo il ramo del metodo |
| natura | Careful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 31 Att / 1 Dif / 19 Asp / 2 Dsp / 20 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 145, `ZAPDOS` | numero nazionale 145, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 197, 65, 268 | dichiarate dalla tabella |
| punti potenza | 30, 5, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `917cc49f563fedd217c2669a59bcb1ba6ab28623ae0b2288c53b82bd62bac40f` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 109 Moltres  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x006E` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x43368B5C` | prime estrazioni, secondo il ramo del metodo |
| natura | Quiet | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 24 PS / 3 Att / 2 Dif / 3 Asp / 30 Dsp / 27 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 146, `MOLTRES` | numero nazionale 146, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 203, 53, 219 | dichiarate dalla tabella |
| punti potenza | 30, 10, 15, 25 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `b53b1230aafab7a0eb5062cfb14653150d922d1d80335fe305863e1d0c7900ea` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 110 Dragonite  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x006F` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x84FC4DFF` | prime estrazioni, secondo il ramo del metodo |
| natura | Lonely | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 22 PS / 7 Att / 2 Dif / 20 Asp / 25 Dsp / 1 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 149, `DRAGONITE` | numero nazionale 149, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 97, 219, 17, 200 | dichiarate dalla tabella |
| punti potenza | 30, 25, 35, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `6bc793ea4ed1aa8dc6ce3655ff950d8c4629d3fbc52c131ae24987f0bc57883c` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 111 Typhlosion  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0070` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xC6C210A2` | prime estrazioni, secondo il ramo del metodo |
| natura | Timid | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 11 Att / 2 Dif / 4 Asp / 21 Dsp / 8 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 157, `TYPHLOSION` | numero nazionale 157, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 98, 172, 129, 53 | dichiarate dalla tabella |
| punti potenza | 30, 25, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `2d0f5b8380a474fc6d714f870fe17efbae654df8ff207500ee0019f80538e598` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 112 Espeon  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0071` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x0888D344` | prime estrazioni, secondo il ramo del metodo |
| natura | Impish | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 15 Att / 2 Dif / 20 Asp / 16 Dsp / 14 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 196, `ESPEON` | numero nazionale 196, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 60, 244, 94, 234 | dichiarate dalla tabella |
| punti potenza | 20, 10, 10, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `9abfcee584a59e40438fa6b4d7310a24abbf6b9aac5972e9fd169ca96acc1742` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 113 Umbreon  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0072` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x4A4F95E7` | prime estrazioni, secondo il ramo del metodo |
| natura | Adamant | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 15 PS / 19 Att / 2 Dif / 4 Asp / 12 Dsp / 21 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 197, `UMBREON` | numero nazionale 197, nome nella lingua della voce |
| livello, esperienza | 70, 343000 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 185, 212, 103, 236 | dichiarate dalla tabella |
| punti potenza | 20, 5, 40, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `6a1e560d270623ed54b672bffba601778561cfb36aa07bb523d15d67f8125790` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 114 Raikou  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0073` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x8C155889` | prime estrazioni, secondo il ramo del metodo |
| natura | Hasty | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 23 Att / 2 Dif / 20 Asp / 7 Dsp / 27 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale 243, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 98, 209, 115, 242 | dichiarate dalla tabella |
| punti potenza | 30, 20, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `1d69ebf938943c1355b8e1f31f6a28acee61922832ff2ae7f3c62dde60b3d067` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 115 Entei  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0074` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xCDDB1B2C` | prime estrazioni, secondo il ramo del metodo |
| natura | Calm | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 27 Att / 2 Dif / 5 Asp / 3 Dsp / 2 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale 244, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 83, 23, 53, 207 | dichiarate dalla tabella |
| punti potenza | 15, 20, 15, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `8df49595641e2a66cfebf7bb57f5e9fc47d807636c1a151e22bea21e7cf6a862` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 116 Suicune  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0075` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x0FA2DDCF` | prime estrazioni, secondo il ramo del metodo |
| natura | Bold | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 31 Att / 2 Dif / 21 Asp / 30 Dsp / 8 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale 245, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 16, 62, 54, 243 | dichiarate dalla tabella |
| punti potenza | 35, 20, 30, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `f42b888a662c2b0d586f257ee1b9823157aba3c3d40fa3ac85ee196fa840d916` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 117 Tyranitar  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0076` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x5168A071` | prime estrazioni, secondo il ramo del metodo |
| natura | Jolly | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 6 PS / 3 Att / 3 Dif / 5 Asp / 26 Dsp / 15 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 248, `TYRANITAR` | numero nazionale 248, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 37, 184, 242, 89 | dichiarate dalla tabella |
| punti potenza | 20, 10, 15, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `3b8b356ee28d47af4a5946d95b78cdcf7c52a384c7c4678a5b8b4a26ca41a376` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 118 Celebi  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0077` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x932E6314` | prime estrazioni, secondo il ramo del metodo |
| natura | Sassy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 7 Att / 3 Dif / 21 Asp / 21 Dsp / 21 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 251, `CELEBI` | numero nazionale 251, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 246, 248, 226, 195 | dichiarate dalla tabella |
| punti potenza | 5, 15, 40, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `1185abad6a6de3bb67d98ec595e5ff95e0261221c3988e45ca78382fb9bcf6ac` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 119 Blaziken  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0078` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xD4F525B6` | prime estrazioni, secondo il ramo del metodo |
| natura | Mild | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 11 Att / 3 Dif / 5 Asp / 17 Dsp / 28 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 282, `BLAZIKEN` | numero nazionale 257, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 299, 163, 119, 327 | dichiarate dalla tabella |
| punti potenza | 10, 20, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `a969d63a7e25eb2e30ed0c1eaf171b23e4a29c8850407cff5df7125a64c473cd` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 120 Absol  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x0079` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x16BBE859` | prime estrazioni, secondo il ramo del metodo |
| natura | Modest | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 31 PS / 14 Att / 3 Dif / 22 Asp / 12 Dsp / 2 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 376, `ABSOL` | numero nazionale 359, nome nella lingua della voce |
| livello, esperienza | 70, 344960 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 104, 163, 248, 195 | dichiarate dalla tabella |
| punti potenza | 15, 20, 15, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `f75d41e3f95713186e485e5968da4d7f3499ed7d4ea07eb1ebc86a5acc354de9` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 121 Latias  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x007A` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x5881AAFC` | prime estrazioni, secondo il ramo del metodo |
| natura | Quirky | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 29 PS / 18 Att / 3 Dif / 6 Asp / 8 Dsp / 9 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | femmina | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 407, `LATIAS` | numero nazionale 380, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 296, 94, 105, 204 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `553406c4e6209c3a3384eb993b68419e59da45d220ff76f5e45871a6ae30f27b` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 122 Latios  (giudizio: conforme, 2026-09-04)

**Festa del decennale, seconda serie.** Quando: non ancora documentate. Dove: non ancora documentato. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x007B` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x9A486D9E` | prime estrazioni, secondo il ramo del metodo |
| natura | Bashful | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 22 Att / 3 Dif / 22 Asp / 3 Dsp / 15 Vel | due estrazioni, cinque bit per campo |
| allenatore | `10 ANIV` | dichiarato dalla tabella |
| identificativo, segreto | 10, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione RandS7 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 408, `LATIOS` | numero nazionale 381, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 295, 94, 105, 349 | dichiarate dalla tabella |
| punti potenza | 5, 10, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R_A, Never | dichiarati dalla tabella |
| impronta del file prodotto | `08754be3796b7df7b032f8737b9420e6e1fa32466d3bee047e3da7013f6c8ca6` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 123 Pichu with Teeter Dance  (giudizio: conforme, 2026-09-04)

**Uova del quinto anniversario del centro Pokémon giapponese.** Quando: non ancora documentate. Dove: centri Pokémon giapponesi. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_TS, la lucentezza Always e la lingua English.

### 124 Pichu with Wish  (giudizio: conforme, 2026-09-04)

**Uova del quinto anniversario del centro Pokémon giapponese.** Quando: non ancora documentate. Dove: centri Pokémon giapponesi. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_TS, la lucentezza Always e la lingua English.

### 125 Pichu with Teeter Dance  (giudizio: conforme, 2026-09-04)

**Uova del quinto anniversario del centro Pokémon giapponese.** Quando: non ancora documentate. Dove: centri Pokémon giapponesi. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_TA, la lucentezza non vincolata e la lingua English.

### 126 Pichu with Wish  (giudizio: conforme, 2026-09-04)

**Uova del quinto anniversario del centro Pokémon giapponese.** Quando: non ancora documentate. Dove: centri Pokémon giapponesi. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_TA, la lucentezza non vincolata e la lingua English.

### 127 Ralts with Charm  (giudizio: conforme, 2026-09-04)

**Uova del quinto anniversario del centro Pokémon giapponese.** Quando: non ancora documentate. Dove: centri Pokémon giapponesi. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_TA, la lucentezza non vincolata e la lingua English.

### 128 Ralts with Wish  (giudizio: conforme, 2026-09-04)

**Uova del quinto anniversario del centro Pokémon giapponese.** Quando: non ancora documentate. Dove: centri Pokémon giapponesi. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_TA, la lucentezza non vincolata e la lingua English.

### 129 Absol with Spite  (giudizio: conforme, 2026-09-04)

**Uova del quinto anniversario del centro Pokémon giapponese.** Quando: non ancora documentate. Dove: centri Pokémon giapponesi. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_TA, la lucentezza non vincolata e la lingua English.

### 130 Absol with Wish  (giudizio: conforme, 2026-09-04)

**Uova del quinto anniversario del centro Pokémon giapponese.** Quando: non ancora documentate. Dove: centri Pokémon giapponesi. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_TA, la lucentezza non vincolata e la lingua English.

### 131 Bagon with Iron Defense  (giudizio: conforme, 2026-09-04)

**Uova del quinto anniversario del centro Pokémon giapponese.** Quando: non ancora documentate. Dove: centri Pokémon giapponesi. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_TA, la lucentezza non vincolata e la lingua English.

### 132 Bagon with Wish  (giudizio: conforme, 2026-09-04)

**Uova del quinto anniversario del centro Pokémon giapponese.** Quando: non ancora documentate. Dove: centri Pokémon giapponesi. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_TA, la lucentezza non vincolata e la lingua English.

### 133 Oddish with Leech Seed  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 134 Meowth with Petal Dance  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 135 Poliwag with Sweet Kiss  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 136 Bellsprout with Teeter Dance  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 137 Farfetch'd with Wish & Yawn  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 138 Drowzee with Wish & Belly Drum  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 139 Exeggcute with Wish & Sweet Scent  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 140 Lickitung with Wish & Heal Bell  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 141 Chansey with Wish & Sweet Scent  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 142 Kangaskhan with Wish & Yawn  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 143 Psyduck with Mud Sport  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 144 Pichu with Follow me  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 145 Igglybuff with Tickle  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 146 Corsola with Mud Sport  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 147 Taillow with Feather Dance  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 148 Surskit with Mud Sport  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 149 Whismur with Teeter Dance  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 150 Skitty with Rollout  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 151 Plusle with Water Sport  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 152 Minun with Mud Sport  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 153 Spoink with Uproar  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 154 Spinda with Sing  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 155 Cacnea with Encore  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 156 Corphish with Water Sport  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 157 Wynaut with Tickle  (giudizio: conforme, 2026-09-04)

**Uova del desiderio del centro Pokémon di New York.** Quando: non ancora documentate. Dove: Pokémon Center di New York. Come: non ancora documentato. Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci precedenti sono dichiarate non documentate e non vanno citate.

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè Method_2, la lucentezza non vincolata e la lingua English.

### 158 Psyduck with Mud Sport  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x009F` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xDA2BCC7C` | prime estrazioni, secondo il ramo del metodo |
| natura | Lax | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 9 PS / 4 Att / 8 Dif / 29 Asp / 1 Dsp / 25 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 54, `PSYDUCK` | numero nazionale 54, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 346, 10, 39, 300 | dichiarate dalla tabella |
| punti potenza | 15, 35, 30, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `08b95d3ff3183cdd5d74fbb37bfbf78d29e6376c140a2c07712ff7d7c83b2be5` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 159 Pichu with Follow Me  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00A0` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x1BF18F1E` | prime estrazioni, secondo il ramo del metodo |
| natura | Gentle | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 8 Att / 8 Dif / 14 Asp / 29 Dsp / 0 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 172, `PICHU` | numero nazionale 172, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 84, 204, 266 | dichiarate dalla tabella |
| punti potenza | 30, 20, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `47082d2e2c9bf2f69fd152bf708dc72a4c0122d5d889adb80171ab7550ab5ee9` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 160 Igglybuff with Tickle  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00A1` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x5DB751C1` | prime estrazioni, secondo il ramo del metodo |
| natura | Bold | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 12 Att / 8 Dif / 30 Asp / 24 Dsp / 6 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 174, `IGGLYBUFF` | numero nazionale 174, nome nella lingua della voce |
| livello, esperienza | 5, 100 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 47, 204, 111, 321 | dichiarate dalla tabella |
| punti potenza | 15, 20, 40, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `bf090b9c32aa81ce404d858b62d22ed570a9a0b3df592cb9e9f8760d8a687ef2` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 161 Corsola with Mud Sport  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00A2` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x9F7E1464` | prime estrazioni, secondo il ramo del metodo |
| natura | Hardy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 16 Att / 8 Dif / 14 Asp / 20 Dsp / 13 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 222, `CORSOLA` | numero nazionale 222, nome nella lingua della voce |
| livello, esperienza | 5, 100 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 33, 300 | dichiarate dalla tabella |
| punti potenza | 35, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `bdb94e914345e37cd667d6082f420795ac850965ce5f41272f547bf897b7d86a` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 162 Taillow with Feather Dance  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00A3` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xE144D706` | prime estrazioni, secondo il ramo del metodo |
| natura | Rash | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 20 Att / 8 Dif / 30 Asp / 15 Dsp / 19 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 304, `TAILLOW` | numero nazionale 276, nome nella lingua della voce |
| livello, esperienza | 5, 135 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 64, 45, 116, 297 | dichiarate dalla tabella |
| punti potenza | 35, 40, 30, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `9cb304084e9b5988466441fd8a847d8504e0d9b2a43fb3cbfd1b03e0f917d3a1` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 163 Surskit with Mud Sport  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00A4` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x230A99A9` | prime estrazioni, secondo il ramo del metodo |
| natura | Relaxed | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 23 Att / 8 Dif / 14 Asp / 11 Dsp / 26 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 311, `SURSKIT` | numero nazionale 283, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 145, 300 | dichiarate dalla tabella |
| punti potenza | 30, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `fea9a883b79d25ad29c3af68c2c1974006e55e243439c7836c6eef4f604b91d2` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 164 Whismur with Teeter Dance  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00A5` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x64D05C4C` | prime estrazioni, secondo il ramo del metodo |
| natura | Mild | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 27 PS / 27 Att / 8 Dif / 31 Asp / 6 Dsp / 0 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 370, `WHISMUR` | numero nazionale 293, nome nella lingua della voce |
| livello, esperienza | 5, 135 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 1, 253, 298 | dichiarate dalla tabella |
| punti potenza | 35, 10, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `5a504accde0004980028c895a5cd89ea9af311bafd7a2ab4abb72162607b9136` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 165 Skitty with Rollout  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00A6` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xA6971EEE` | prime estrazioni, secondo il ramo del metodo |
| natura | Timid | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 31 Att / 8 Dif / 15 Asp / 2 Dsp / 7 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 315, `SKITTY` | numero nazionale 300, nome nella lingua della voce |
| livello, esperienza | 5, 100 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 45, 33, 39, 205 | dichiarate dalla tabella |
| punti potenza | 40, 35, 30, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `4f4b7396c8f9c7249cd4f0fe30a3ee6e808c51619de35066fc789ee4d59ec8e3` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 166 Plusle with Water Sport  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00A7` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xE85DE191` | prime estrazioni, secondo il ramo del metodo |
| natura | Bold | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 3 Att / 9 Dif / 31 Asp / 29 Dsp / 13 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 353, `PLUSLE` | numero nazionale 311, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 45, 86, 346 | dichiarate dalla tabella |
| punti potenza | 40, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `b6d6b5eea186b8deda479c9e00ac319437a583e46c14f56be57e6a60543412d2` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 167 Minun with Mud Sport  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00A8` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x2A23A433` | prime estrazioni, secondo il ramo del metodo |
| natura | Quiet | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 7 Att / 9 Dif / 15 Asp / 25 Dsp / 20 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 354, `MINUN` | numero nazionale 312, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 45, 86, 300 | dichiarate dalla tabella |
| punti potenza | 40, 20, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `2fd0cc7ba6e3ec81406b29a7745104f9f25ce1d058355950f550a497c0404fb2` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 168 Spoink with Uproar  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00A9` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x6BEA66D6` | prime estrazioni, secondo il ramo del metodo |
| natura | Serious | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 11 Att / 9 Dif / 31 Asp / 20 Dsp / 26 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 351, `SPOINK` | numero nazionale 325, nome nella lingua della voce |
| livello, esperienza | 5, 100 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 150, 253 | dichiarate dalla tabella |
| punti potenza | 40, 10 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `f64b6fa2892407a500be1d6185f8217fa3e430f099b3f5941df701b06ef22139` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 169 Spinda with Sing  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00AA` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xADB02979` | prime estrazioni, secondo il ramo del metodo |
| natura | Gentle | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 16 PS / 15 Att / 9 Dif / 16 Asp / 16 Dsp / 1 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 308, `SPINDA` | numero nazionale 327, nome nella lingua della voce |
| livello, esperienza | 5, 100 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 33, 253, 47 | dichiarate dalla tabella |
| punti potenza | 35, 10, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `08f6421632342987cdb4cc4f7f71a38d4f46f23de4ba3189a5323193a4b36a06` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 170 Cacnea with Encore  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00AB` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0xEF76EC1B` | prime estrazioni, secondo il ramo del metodo |
| natura | Modest | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 14 PS / 19 Att / 9 Dif / 0 Asp / 12 Dsp / 7 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 344, `CACNEA` | numero nazionale 331, nome nella lingua della voce |
| livello, esperienza | 5, 135 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 40, 43, 71, 227 | dichiarate dalla tabella |
| punti potenza | 35, 30, 20, 5 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `9d84273e8c5752255cd5926424c6d65c97da5aa2dbd941f8aa4206db73f954bf` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 171 Corphish with Water Sport  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00AC` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x313DAEBE` | prime estrazioni, secondo il ramo del metodo |
| natura | Naive | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 23 Att / 9 Dif / 16 Asp / 7 Dsp / 14 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 326, `CORPHISH` | numero nazionale 341, nome nella lingua della voce |
| livello, esperienza | 5, 65 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 145, 346 | dichiarate dalla tabella |
| punti potenza | 30, 15 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `f35ae368accec110009f8171159cd7a1275ff880310ded3a7571d384967f641e` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 172 Wynaut with Tickle  (giudizio: conforme, 2026-09-04)

**PokéPark Meowth e le uova del PokéPark.** Quando: 18 marzo - 25 settembre 2005 per il Meowth; 12 marzo - 8 maggio 2005 per le uova. Dove: PokéPark, Giappone, e un cinema nelle vicinanze. Come: distribuzione senza fili sul posto, oppure attraverso i punti di accesso pubblici. Fonte: [List of Japanese event Pokémon distributions in Generation III](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III), letta il 2026-09-02. Su questo gruppo le fonti divergono: la voce corrispondente del catalogo riporta la divergenza e l'argomento con cui è stata risolta.

| Campo | Valore | Da dove viene |
|---|---|---|
| seme di origine | `0x00AD` | scelto fra gli ammessi verificando i vincoli, con partenza dall'indice della voce |
| valore di personalità | `0x73037160` | prime estrazioni, secondo il ramo del metodo |
| natura | Sassy | resto per venticinque del valore di personalità |
| bit dell'abilità | 0 | bit meno significativo del valore di personalità, oppure zero se la specie ha una sola abilità |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 9 PS / 27 Att / 9 Dif / 0 Asp / 3 Dsp / 20 Vel | due estrazioni, cinque bit per campo |
| allenatore | `ポケパーク` | dichiarato dalla tabella |
| identificativo, segreto | 50318, 0 | dichiarati dalla tabella |
| sesso dell'allenatore | maschio | derivazione Only0 |
| lingua | English | dichiarata dalla tabella |
| specie interna, soprannome | 360, `WYNAUT` | numero nazionale 360, nome nella lingua della voce |
| livello, esperienza | 5, 125 | livello dichiarato, esperienza dalla formula del gruppo di crescita |
| mosse | 150, 204, 227, 321 | dichiarate dalla tabella |
| punti potenza | 40, 20, 5, 20 | dal valore base di ciascuna mossa |
| oggetto tenuto | nessuno | l'evento non ne dichiara alcuno |
| fiocchi di merito | `0x000` | nessuno dichiarato |
| incontro fatidico | no | dichiarato dalla tabella |
| metodo, lucentezza | BACD_R, non vincolata | dichiarati dalla tabella |
| impronta del file prodotto | `cb4dc35880d1ae4dde7bdafee6f184ef06bcf2caf5fc37acfc8e2d4cb48d1183` | SHA-256 della forma canonica scritta in `_notes/lotto-eventi/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |
