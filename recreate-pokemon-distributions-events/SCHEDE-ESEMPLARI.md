# Schede tecniche degli esemplari producibili

> Documento generato da `tools/schede-esemplari.py`. Non si modifica a mano, e non legge i file prodotti: ricalcola gli esemplari dalle sorgenti con il medesimo codice che li scrive.

Un giudizio di conformità riguarda una configurazione precisa di byte e non una categoria: vale per quel valore di personalità, quei valori individuali, quel nome e quel seme. Registrare soltanto che un esemplare è conforme perde l'informazione che serve, cioè che cosa esattamente sia stato dichiarato conforme, e senza quella non si può né riprodurre il caso né riconoscere che una modifica successiva lo ha cambiato. Questo documento è dunque l'inventario delle caratteristiche univoche di ciascun esemplare, accanto allo stato del suo giudizio.

Che il documento sia ricalcolato e non letto dal disco ha una conseguenza che vale dichiarare: esso è anche una verifica del determinismo della produzione. Se due corse dessero schede diverse, la scelta del seme non sarebbe riproducibile, e il difetto si manifesterebbe come una modifica del documento senza che nulla sia stato modificato a mano.

Stato: 122 voci producibili, di cui 5 dichiarate conformi da un verificatore indipendente al momento dell'ultima generazione di questo documento. Le voci conformi portano la dicitura accanto al titolo; le altre non sono state giudicate oppure lo sono state con rilievi, e il registro dei giudizi in `giudizi-esterni.json` dice quale dei due casi.

### 000 Mew  (giudizio: conforme, riletta dopo le tre correzioni della giornata, 2026-09-02)

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

### 001 WISHMKR  (giudizio: contestato, poi conforme dopo la correzione, 2026-09-02)

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

### 003 Berry Fix Ruby

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

### 004 Berry Fix Sapphire

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

### 005 Negai Boshi Jirachi  (giudizio: conforme, 2026-09-02)

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

### 006 Negai Boshi Jirachi (Match Recipient)  (giudizio: conforme, 2026-09-02)

Questa voce prende dall'allenatore di destinazione uno o più fra nome, identificativo e sesso, quindi le sue caratteristiche derivate dipendono dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che l'evento fissa resta il metodo di generazione, cioè BACD_U_AX, la lucentezza Never e la lingua Japanese.

### 007 Tanabata Jirachi (2004)

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

### 008 ANA Pikachu  (giudizio: contestato, 2026-09-02)

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

### 009 PokéPark Meowth

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

### 010 Yokohama Pikachu

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

### 011 Hadou Mew

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

### 012 GW Pikachu

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

### 013 Sapporo Pikachu

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

### 014 Tanabata Jirachi (2005)

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

### 015 Festa Metang

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

### 016 Sunday Wobbuffet

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

### 017 Regirock

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

### 018 Regice

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

### 019 Registeel

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

### 020 PokéPark Mew

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

### 021 PokéPark Celebi

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

### 022 Tanabata Jirachi (2006)

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

### 023 Mitsurin Celebi (2006)

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

### 024 PokéPark Jirachi (2006)

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

### 025 PokéPark Jirachi (2006)

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

### 026 Berry Fix Ruby  (giudizio: contestato, poi conforme dopo la correzione, 2026-09-02)

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

### 027 Berry Fix Sapphire

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

### 028 Charizard

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

### 029 Pikachu

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

### 030 Articuno

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

### 031 Raikou

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

### 032 Entei

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

### 033 Suicune

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

### 034 Lugia

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

### 035 Ho-Oh

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

### 036 Latias

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

### 037 Latios

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

### 038 Charizard

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

### 039 Pikachu

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

### 040 Articuno

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

### 041 Raikou

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

### 042 Entei

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

### 043 Suicune

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

### 044 Lugia

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

### 045 Ho-Oh

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

### 046 Latias

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

### 047 Latios

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

### 048 Charizard

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

### 049 Pikachu

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

### 050 Articuno

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

### 051 Raikou

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

### 052 Entei

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

### 053 Suicune

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

### 054 Lugia

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

### 055 Ho-Oh

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

### 056 Latias

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

### 057 Latios

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

### 058 Charizard

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

### 059 Pikachu

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

### 060 Articuno

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

### 061 Raikou

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

### 062 Entei

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

### 063 Suicune

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

### 064 Lugia

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

### 065 Ho-Oh

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

### 066 Latias

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

### 067 Latios

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

### 068 Charizard

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

### 069 Pikachu

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

### 070 Articuno

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

### 071 Raikou

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

### 072 Entei

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

### 073 Suicune

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

### 074 Lugia

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

### 075 Ho-Oh

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

### 076 Latias

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

### 077 Latios

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

### 078 Mew

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

### 079 Metang

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

### 080 Deoxys

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

### 081 Deoxys

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

### 082 Bulbasaur

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

### 083 Charizard

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

### 084 Blastoise

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

### 085 Pikachu (Fly)

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

### 086 Alakazam

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

### 087 Articuno

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

### 088 Zapdos

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

### 089 Moltres

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

### 090 Dragonite

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

### 091 Typhlosion

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

### 092 Espeon

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

### 093 Umbreon

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

### 094 Raikou

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

### 095 Entei

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

### 096 Suicune

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

### 097 Tyranitar

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

### 098 Blaziken

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

### 099 Absol

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

### 100 Latias

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

### 101 Latios

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

### 102 Bulbasaur

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

### 103 Charizard

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

### 104 Blastoise

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

### 105 Pikachu (No Fly)

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

### 106 Alakazam

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

### 107 Articuno

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

### 108 Zapdos

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

### 109 Moltres

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

### 110 Dragonite

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

### 111 Typhlosion

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

### 112 Espeon

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

### 113 Umbreon

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

### 114 Raikou

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

### 115 Entei

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

### 116 Suicune

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

### 117 Tyranitar

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

### 118 Celebi

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

### 119 Blaziken

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

### 120 Absol

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

### 121 Latias

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

### 122 Latios

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
