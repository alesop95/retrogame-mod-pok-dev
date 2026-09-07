# Schede tecniche degli esemplari da evento di quarta generazione

> Documento generato da `tools/schede-esemplari-gen4.py`. Non si modifica a mano, e non legge i file prodotti: ricalcola gli esemplari dalle sorgenti con il medesimo codice che li scrive.

Un giudizio di conformità riguarda una configurazione precisa di byte e non una categoria: vale per quel valore di personalità, quei valori individuali, quel nome e quella data. Questo documento è dunque l'inventario delle caratteristiche univoche di ciascun esemplare, accanto allo stato del suo giudizio.

La quarta generazione ha una particolarità che le prime tre non hanno, e va letta prima delle schede perché cambia il senso di due righe di ciascuna. Il dono di quarta generazione non contiene l'esemplare ma il suo modello: il valore di personalità è dichiarato su 128 voci e assente sulle altre 119, dove il modello porta il segnale che ordina di generarne uno non cromatico, e i valori individuali sono assenti su tutte e 247. Le righe che dicono composto da noi non denunciano quindi una licenza che ci siamo presi, ma il fatto che quei bit non esistevano prima della consegna e li tirava la console di chi riceveva.

Stato: 247 voci prodotte, di cui 0 giudicate da un verificatore indipendente al momento dell'ultima generazione di questo documento. Le voci giudicate portano la dicitura accanto al titolo.

### 000 Pikachu  `TCGWC`

**Insegna TCGWC, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `TCGWC`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 0 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x246E13AF` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 15 PS / 7 Att / 23 Dif / 16 Vel / 22 Asp / 4 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `TCGWC` | dichiarato dal modello |
| identificativo, segreto | 8107, 20846 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Surf, Fulmine, Schermoluce, Attacco Rapido | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|0\|246E13AF\|8107\|20846\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|0\|246E13AF\|8107\|20846\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `825d90b19bbf0110d544a8d4b1fa5777510b680cd13821effce23d719e6b046b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 001 Manaphy  `TRU`

**Insegna TRU, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `TRU`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 1 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xD12E8810` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 93 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 22 Att / 19 Dif / 23 Vel / 26 Asp / 5 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `TRU` | dichiarato dal modello |
| identificativo, segreto | 9297, 60303 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 490, `MANAPHY` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Cuorbaratto, Idropulsar, Mulinello, Scudo Acido | dichiarate dal modello |
| oggetto tenuto | 260 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|1\|00000001\|9297\|60303\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|1\|00000001\|9297\|60303\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `269c4d28ad55921c0dd430ae64fe969cb5831c625d097bfcd77484a78a1131b9` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 002 Manaphy  `NWS`

**Insegna NWS, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `NWS`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 2 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x646093B9` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Cauta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 93 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 24 PS / 22 Att / 9 Dif / 29 Vel / 12 Asp / 19 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `NWS` | dichiarato dal modello |
| identificativo, segreto | 10017, 16757 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 490, `MANAPHY` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Cuorbaratto, Idropulsar, Mulinello, Scudo Acido | dichiarate dal modello |
| oggetto tenuto | 260 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|2\|00000001\|10017\|16757\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|2\|00000001\|10017\|16757\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e364f56bd5515c835b814b928309da9b7f51b5293aa5fd39a1da900edc58fdea` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 003 Manaphy  `JBHF`

**Insegna JBHF, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `JBHF`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 3 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7D7749F6` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 93 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 0 Att / 6 Dif / 28 Vel / 11 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `JBHF` | dichiarato dal modello |
| identificativo, segreto | 11077, 40919 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 490, `MANAPHY` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Cuorbaratto, Idropulsar, Mulinello, Scudo Acido | dichiarate dal modello |
| oggetto tenuto | 260 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|3\|00000001\|11077\|40919\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|3\|00000001\|11077\|40919\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `794c06a739dec4ed3f0f71291991e183834f03dad572ea2faabaedc5f93f6e86` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 004 Manaphy  `E4ALL`

**Insegna E4ALL, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `E4ALL`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 4 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x64AB62F9` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 93 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 12 Att / 27 Dif / 9 Vel / 15 Asp / 3 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `E4ALL` | dichiarato dal modello |
| identificativo, segreto | 10187, 36666 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 490, `MANAPHY` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Cuorbaratto, Idropulsar, Mulinello, Scudo Acido | dichiarate dal modello |
| oggetto tenuto | 260 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|4\|00000001\|10187\|36666\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|4\|00000001\|10187\|36666\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5c2f39753540449bdf56a6931d9caeccea616b87cfc293ec4715d2953d90ad7c` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 005 Darkrai  `ALAMOS`

**Insegna ALAMOS, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ALAMOS`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 5 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xC5A85700` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Vivace | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 31 Att / 0 Dif / 0 Vel / 28 Asp / 16 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ALAMOS` | dichiarato dal modello |
| identificativo, segreto | 5318, 10413 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fragortempo, Fendispazio, Incubo, Ipnosi | dichiarate dal modello |
| oggetto tenuto | 208 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|5\|00000001\|5318\|10413\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|5\|00000001\|5318\|10413\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `88b8787e4d86794ca6ca61ec8e7c6138baaaf8f5f0c1c3b23aa026f91023090b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 006 Deoxys  `Gamestp`

**Insegna Gamestp, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Gamestp`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 6 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x125D5ED9` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 22 Att / 21 Dif / 6 Vel / 25 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Gamestp` | dichiarato dal modello |
| identificativo, segreto | 6218, 31630 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Elettrocannone, Ferroscudo, Extrarapido | dichiarate dal modello |
| oggetto tenuto | 246 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|6\|00000001\|6218\|31630\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|6\|00000001\|6218\|31630\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e345af63c4ac9ee73abf5575505d1ff860fcb85df859909b5879544dadc4dfe8` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 007 Darkrai  `ALAMOS`

**Insegna ALAMOS, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ALAMOS`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 7 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xB1715A2C` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Fiacca | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 5 Att / 26 Dif / 28 Vel / 14 Asp / 5 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ALAMOS` | dichiarato dal modello |
| identificativo, segreto | 7038, 45156 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fragortempo, Fendispazio, Incubo, Ipnosi | dichiarate dal modello |
| oggetto tenuto | 208 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|7\|00000001\|7038\|45156\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|7\|00000001\|7038\|45156\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `4939708bd1a78d0d8139f2302257d9ce4e9bb06922fda2fa2acb060014563dce` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 008 Darkrai  `ALAMOS`

**Insegna ALAMOS, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ALAMOS`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 8 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xA69301D6` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 1 Att / 2 Dif / 21 Vel / 31 Asp / 22 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ALAMOS` | dichiarato dal modello |
| identificativo, segreto | 7038, 22261 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fragortempo, Fendispazio, Incubo, Ipnosi | dichiarate dal modello |
| oggetto tenuto | 208 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|8\|00000001\|7038\|22261\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|8\|00000001\|7038\|22261\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `8c57dd540c4abdbdac3911690e403a871302f1e2548b641ec392db764a66fa2f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 009 Darkrai  `ALAMOS`

**Insegna ALAMOS, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ALAMOS`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 9 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0E0C171F` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 12 Att / 13 Dif / 21 Vel / 4 Asp / 2 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ALAMOS` | dichiarato dal modello |
| identificativo, segreto | 10308, 61209 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fragortempo, Fendispazio, Incubo, Ipnosi | dichiarate dal modello |
| oggetto tenuto | 208 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|9\|00000001\|10308\|61209\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|9\|00000001\|10308\|61209\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6b44451133189b016ce4caf54a6b80a5ddc5f35f67145f1cfa1f14adbde14d76` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 010 Dragonite  `TRU`

**Insegna TRU, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `TRU`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 10 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0E2CFBFC` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Mite | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 39 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 27 Att / 26 Dif / 1 Vel / 3 Asp / 28 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `TRU` | dichiarato dal modello |
| identificativo, segreto | 11088, 47337 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 149, `DRAGONITE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Dragobolide, Fulmine, Oltraggio, Dragodanza | dichiarate dal modello |
| oggetto tenuto | 188 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|10\|0E2CFBFC\|11088\|47337\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|10\|0E2CFBFC\|11088\|47337\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `d2a1c80185685f355f18564429f9269a72850c5c0ecf938b35b288f050ac70a1` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 011 Pikachu  `Nzone`

**Insegna Nzone, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Nzone`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 11 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x21ACDA5A` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 3 Att / 25 Dif / 14 Vel / 11 Asp / 1 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Nzone` | dichiarato dal modello |
| identificativo, segreto | 10278, 59322 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 20, 8000 | dichiarati dal modello |
| mosse | Regalino, Attacco Rapido, Tuonoshock, Colpocoda | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|11\|21ACDA5A\|10278\|59322\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|11\|21ACDA5A\|10278\|59322\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `fd957e7a4ce20c77525de978fe78628aee2dcfa4a116e1fb1e0a991f0569f346` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 012 Shaymin  `TRU`

**Insegna TRU, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `TRU`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 12 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xAD9AFFE3` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 31 PS / 0 Att / 28 Dif / 26 Vel / 1 Asp / 4 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `TRU` | dichiarato dal modello |
| identificativo, segreto | 2089, 14103 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Infuriaseme, Aromaterapia, Sostituto, Energipalla | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|12\|00000001\|2089\|14103\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|12\|00000001\|2089\|14103\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `63f68689d36c6df69613dbc543d93c50773b47b29dff41118b3db4c44f511ff4` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 013 Regigigas  `TRU`

**Insegna TRU, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `TRU`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 13 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xE1F63215` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Audace | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 112 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 27 Att / 14 Dif / 14 Vel / 5 Asp / 23 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `TRU` | dichiarato dal modello |
| identificativo, segreto | 3089, 29347 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 486, `REGIGIGAS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Metaltestata, Frana, Ventogelato, Sbriciolmano | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|13\|00000001\|3089\|29347\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|13\|00000001\|3089\|29347\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3985700effd3460ef6e0e78a58f933d24a3dd2d3c6a1d0addd62306e188bd7b9` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 014 Shaymin  `Movie11`

**Insegna Movie11, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Movie11`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 14 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xE656B962` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Fiacca | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 28 Att / 29 Dif / 5 Vel / 18 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Movie11` | dichiarato dal modello |
| identificativo, segreto | 4019, 49952 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Infuriaseme, Aromaterapia, Sostituto, Energipalla | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|14\|00000001\|4019\|49952\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|14\|00000001\|4019\|49952\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f96f55f0486466a8579ecfd123b3ecfe807771142729d4c3bd7deab0fb0fc038` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 018 Arceus  `Michina`

**Insegna Michina, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Michina`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 18 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xF0D7D6CF` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Gentile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 121 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 27 Att / 0 Dif / 19 Vel / 4 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Michina` | dichiarato dal modello |
| identificativo, segreto | 11059, 29950 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 493, `ARCEUS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Giudizio, Fragortempo, Fendispazio, Oscurotuffo | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|18\|00000001\|11059\|29950\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|18\|00000001\|11059\|29950\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `d63b484031ecbfb6e741c5f8c7c478b9a7228d01d28c2d1dc9dbfc8817d24334` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 019 Arceus  `TRU`

**Insegna TRU, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `TRU`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 19 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x24B75773` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Schiva | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 121 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 15 Att / 22 Dif / 0 Vel / 22 Asp / 29 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `TRU` | dichiarato dal modello |
| identificativo, segreto | 11079, 62276 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 493, `ARCEUS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Giudizio, Fragortempo, Fendispazio, Oscurotuffo | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|19\|00000001\|11079\|62276\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|19\|00000001\|11079\|62276\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `937e86f65795ad4daf957f7bfe4f856e4b836dc7fa397ff58dad576a1a89fdf4` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 020 Arceus  `MICHINA`

**Insegna MICHINA, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `MICHINA`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 20 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2AAB07A8` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 121 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 31 Att / 18 Dif / 21 Vel / 7 Asp / 10 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `MICHINA` | dichiarato dal modello |
| identificativo, segreto | 2010, 31930 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 493, `ARCEUS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Giudizio, Fragortempo, Fendispazio, Oscurotuffo | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|20\|00000001\|2010\|31930\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|20\|00000001\|2010\|31930\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `11dc776d0767e3f04b61f09eff7a496eb960fb60c713db9cec22fa912e3e687e` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 022 Pichu  `SPR2010`

**Insegna SPR2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `SPR2010`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 22 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2812FD84` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 31 PS / 18 Att / 28 Dif / 20 Vel / 24 Asp / 1 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `SPR2010` | dichiarato dal modello |
| identificativo, segreto | 3050, 56955 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 172, `PICHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Sottocarica, Locomovolt, Rimonta, Resistenza | dichiarate dal modello |
| oggetto tenuto | 229 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|22\|2812FD84\|3050\|56955\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|22\|2812FD84\|3050\|56955\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f65ea0f745722ea4707017bd5bd45b90a1255e61c01eb47e55b6375d926fced2` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 023 Pichu  `GAMESTP`

**Insegna GAMESTP, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `GAMESTP`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 23 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x450E8DEA` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 14 PS / 13 Att / 3 Dif / 22 Vel / 8 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `GAMESTP` | dichiarato dal modello |
| identificativo, segreto | 1300, 52721 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 172, `PICHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Sottocarica, Locomovolt, Rimonta, Resistenza | dichiarate dal modello |
| oggetto tenuto | 229 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|23\|450E8DEA\|1300\|52721\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|23\|450E8DEA\|1300\|52721\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `be6d696b3b205e061dbd0714ac98bf9ac22af5e0323e53ac8180127ac1394810` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 024 Darkrai  `Almia`

**Insegna Almia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Almia`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 24 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2FE6F6F4` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Audace | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 21 Att / 4 Dif / 14 Vel / 30 Asp / 10 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Almia` | dichiarato dal modello |
| identificativo, segreto | 3208, 46999 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Vuototetro, Neropulsar, Palla Ombra, Doppioteam | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|24\|00000001\|3208\|46999\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|24\|00000001\|3208\|46999\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `579650962ebc2ab20eba8b42a3cda08e4a3576a535be7ff8484f3e8ebe69bb63` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 025 Riolu  `Kyle`

**Insegna Kyle, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Kyle`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 25 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x06A6D188` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 80 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 31 Att / 10 Dif / 8 Vel / 19 Asp / 1 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Kyle` | dichiarato dal modello |
| identificativo, segreto | 3208, 64847 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 447, `RIOLU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Sferapulsar, Ombrartigli, Pugnoscarica, Assorbipugno | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|25\|06A6D188\|3208\|64847\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|25\|06A6D188\|3208\|64847\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `83806760c05ecdc5ae37d857a2ec74501ab9ce6c075f7cd43f2e04d593c8c24f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 026 Jirachi  `GAMESTP`

**Insegna GAMESTP, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `GAMESTP`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 26 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x66CC22FC` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 14 PS / 23 Att / 14 Dif / 24 Vel / 17 Asp / 10 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `GAMESTP` | dichiarato dal modello |
| identificativo, segreto | 2270, 54369 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 385, `JIRACHI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo, Dragobolide | dichiarate dal modello |
| oggetto tenuto | 201 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|26\|00000001\|2270\|54369\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|26\|00000001\|2270\|54369\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e40851333d7fdee426b4a3289f87a537e3b7152cb4c53d68d26a11c1e6004db9` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 027 Jirachi  `PKLATAM`

**Insegna PKLATAM, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKLATAM`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 27 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x5E80029A` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 16 PS / 24 Att / 11 Dif / 12 Vel / 14 Asp / 8 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKLATAM` | dichiarato dal modello |
| identificativo, segreto | 3010, 32238 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 385, `JIRACHI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo, Dragobolide | dichiarate dal modello |
| oggetto tenuto | 201 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|27\|00000001\|3010\|32238\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|27\|00000001\|3010\|32238\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5aeaff6b30cdb5ee401e39ae2b083995fdd09dc72e86ede46913b8d7f4843482` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 028 Jirachi  `SMR2010`

**Insegna SMR2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `SMR2010`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 28 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x9F528796` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 19 Att / 8 Dif / 22 Vel / 7 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `SMR2010` | dichiarato dal modello |
| identificativo, segreto | 6030, 36733 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 385, `JIRACHI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo, Dragobolide | dichiarate dal modello |
| oggetto tenuto | 201 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|28\|00000001\|6030\|36733\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|28\|00000001\|6030\|36733\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `d335813ad6a6faf4de6b0dbeea03a23cb3da3ca1f6d50a4014c068461f45e78f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 029 Jirachi  `SMR2010`

**Insegna SMR2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `SMR2010`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 29 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xE6FA8EEE` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Calma | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 18 Att / 2 Dif / 31 Vel / 9 Asp / 20 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `SMR2010` | dichiarato dal modello |
| identificativo, segreto | 6260, 48628 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 385, `JIRACHI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo, Dragobolide | dichiarate dal modello |
| oggetto tenuto | 201 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|29\|00000001\|6260\|48628\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|29\|00000001\|6260\|48628\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `98d3ca4c5834ea19f9b8b5999fe49f8fd833e2b3238d8922bc7b2224619ef556` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 032 Eevee  `VGC10`

**Insegna VGC10, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `VGC10`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 32 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x5FEF8D69` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 91 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 22 PS / 9 Att / 5 Dif / 21 Vel / 15 Asp / 22 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `VGC10` | dichiarato dal modello |
| identificativo, segreto | 5080, 49497 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 133, `EEVEE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Codacciaio, Asso, Flagello, Attacco Rapido | dichiarate dal modello |
| oggetto tenuto | 275 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|32\|5FEF8D69\|5080\|49497\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|32\|5FEF8D69\|5080\|49497\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `899f8d8d4b628e96c55651f7f0ee2d342dc8e4477ddef24076becaac0a9e2ca1` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 033 Mew  `FAL2010`

**Insegna FAL2010, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `FAL2010`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 33 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x536DB64E` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Vivace | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 16 Att / 11 Dif / 10 Vel / 29 Asp / 16 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `FAL2010` | dichiarato dal modello |
| identificativo, segreto | 10160, 39598 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 151, `MEW` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 135 | dichiarati dal modello |
| mosse | Botta | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|33\|00000001\|10160\|39598\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|33\|00000001\|10160\|39598\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `1c6a4c3606b040c0d0caa4b39903ed4401b7b5c7ff8b94d7bff3e67728f8c866` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 035 Raikou  `GAMESTP`

**Insegna GAMESTP, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `GAMESTP`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 35 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x36D46750` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 6 Att / 25 Dif / 17 Vel / 11 Asp / 30 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `GAMESTP` | dichiarato dal modello |
| identificativo, segreto | 1031, 21889 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Elettrocannone, Sferapulsar, Extrarapido, Palla Clima | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|35\|36D46750\|1031\|21889\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|35\|36D46750\|1031\|21889\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `0ae5498b170fd748fda7122f90e00119f3dc20f081516ff24cb55351793c696d` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 036 Raikou  `WIN2011`

**Insegna WIN2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WIN2011`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 36 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x74550788` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 29 Att / 1 Dif / 5 Vel / 28 Asp / 4 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WIN2011` | dichiarato dal modello |
| identificativo, segreto | 2071, 31693 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Elettrocannone, Sferapulsar, Extrarapido, Palla Clima | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|36\|74550788\|2071\|31693\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|36\|74550788\|2071\|31693\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `2a9c6d369f3566783c5dd6f22e6e094075f1e4aa9a01dd87b6cf05124f932a7c` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 037 Entei  `GAMESTP`

**Insegna GAMESTP, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `GAMESTP`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 37 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7D5BB510` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 25 Att / 14 Dif / 24 Vel / 17 Asp / 14 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `GAMESTP` | dichiarato dal modello |
| identificativo, segreto | 1171, 52447 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Fuococarica, Gridodilotta, Extrarapido, Tritartigli | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|37\|7D5BB510\|1171\|52447\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|37\|7D5BB510\|1171\|52447\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `188828a7b3ca8681507617528fa93637409ea6266ea0ecee06ddf8207e89884f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 038 Entei  `WIN2011`

**Insegna WIN2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WIN2011`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 38 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1382179C` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 31 PS / 31 Att / 4 Dif / 10 Vel / 29 Asp / 15 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WIN2011` | dichiarato dal modello |
| identificativo, segreto | 2141, 3136 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Fuococarica, Gridodilotta, Extrarapido, Tritartigli | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|38\|1382179C\|2141\|3136\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|38\|1382179C\|2141\|3136\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `bc933d1920af2cfc9cb9918c52999b19b1a9ab5bf4d6f01217a514fc49d33b71` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 039 Suicune  `GAMESTP`

**Insegna GAMESTP, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `GAMESTP`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 39 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x42FCBC7E` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 24 Att / 16 Dif / 13 Vel / 16 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `GAMESTP` | dichiarato dal modello |
| identificativo, segreto | 1311, 64410 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Purogelo, Eterelama, Extrarapido, Acquanello | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|39\|42FCBC7E\|1311\|64410\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|39\|42FCBC7E\|1311\|64410\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `ec3e6da1882951df9d8130fd0f0b8108dfe979a9cc6f04f8d17a5a454b5fa367` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 040 Suicune  `WIN2011`

**Insegna WIN2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WIN2011`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 40 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7AE975F0` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 11 Att / 17 Dif / 22 Vel / 8 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WIN2011` | dichiarato dal modello |
| identificativo, segreto | 2211, 1980 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Purogelo, Eterelama, Extrarapido, Acquanello | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|40\|7AE975F0\|2211\|1980\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|40\|7AE975F0\|2211\|1980\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f3aae020cd6b64dfaee1598a8ea1f7a64be5093180740efeea5d0c060dd3bb46` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 041 Celebi  `GAMESTP`

**Insegna GAMESTP, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `GAMESTP`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 41 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xF9335186` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 28 Att / 19 Dif / 26 Vel / 20 Asp / 23 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `GAMESTP` | dichiarato dal modello |
| identificativo, segreto | 2271, 10415 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 251, `CELEBI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Verdebufera, Ripresa, Congiura, Curardore | dichiarate dal modello |
| oggetto tenuto | 211 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|41\|00000001\|2271\|10415\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|41\|00000001\|2271\|10415\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `c04608d757b605bee5461b20636cee6d4e0b200e1917082e8131d29a2ed013c1` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 042 Celebi  `WIN2011`

**Insegna WIN2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WIN2011`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 42 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x171FD8F4` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Furba | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 31 PS / 30 Att / 9 Dif / 29 Vel / 3 Asp / 12 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WIN2011` | dichiarato dal modello |
| identificativo, segreto | 1211, 18581 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 251, `CELEBI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Verdebufera, Ripresa, Congiura, Curardore | dichiarate dal modello |
| oggetto tenuto | 211 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|42\|00000001\|1211\|18581\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|42\|00000001\|1211\|18581\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `2d02fa09a89bf3ebe4100a120b48939ebc736646b2b40c4bca7a12c84abb3c28` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 043 Celebi  `WIN2011`

**Insegna WIN2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WIN2011`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 43 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x10753E6A` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Gentile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 1 Att / 19 Dif / 11 Vel / 28 Asp / 1 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WIN2011` | dichiarato dal modello |
| identificativo, segreto | 2211, 20073 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 251, `CELEBI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Verdebufera, Ripresa, Congiura, Curardore | dichiarate dal modello |
| oggetto tenuto | 211 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|43\|00000001\|2211\|20073\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|43\|00000001\|2211\|20073\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `080ccfaad7a53da84695bdbb334b5d228a3ffac4c807357710d0b01e596e58d0` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 044 Pikachu  `Ash`

**Insegna Ash, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Ash`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 44 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x37A47A8A` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Birbona | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 13 Att / 18 Dif / 31 Vel / 15 Asp / 0 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Ash` | dichiarato dal modello |
| identificativo, segreto | 1301, 35254 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Locomovolt, Codacciaio, Attacco Rapido, Fulmine | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|44\|37A47A8A\|1301\|35254\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|44\|37A47A8A\|1301\|35254\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `b8fdc2c586856b0f73d19e0169a5569a5d2a98d72e5a84cf5f27850789d239e7` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 045 Crobat  `WORLD10`

**Insegna WORLD10, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WORLD10`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 45 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x65490588` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 39 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 7 Att / 25 Dif / 9 Vel / 22 Asp / 22 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WORLD10` | dichiarato dal modello |
| identificativo, segreto | 8150, 15269 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 169, `CROBAT` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Ondacalda, Eterelama, Superzanna, Fangobomba | dichiarate dal modello |
| oggetto tenuto | 270 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|45\|65490588\|8150\|15269\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|45\|65490588\|8150\|15269\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `a27000b99c2de1ad903636ca602233f2b1ac18e60f340ea07859469ac2d9c808` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 046 Pikachu  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua inglese, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 46 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x19D97C13` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 24 PS / 30 Att / 14 Dif / 26 Vel / 10 Asp / 3 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 6257, 44870 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | dichiarati dal modello |
| mosse | Locomovolt, Surf, Colpocoda, Tuononda | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|46\|19D97C13\|6257\|44870\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|46\|19D97C13\|6257\|44870\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `29d499b6f03c208ee85a158d48e1b2dea62848fbf092aac71ceced1ec8537abd` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 047 Electivire  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua inglese, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 47 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0D7345A6` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 78 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 8 Att / 1 Dif / 21 Vel / 28 Asp / 8 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 6257, 47618 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 466, `ELECTIVIRE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Tuonopugno, Gelopugno, Incrocolpo, Terremoto | dichiarate dal modello |
| oggetto tenuto | 242 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|47\|0D7345A6\|6257\|47618\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|47\|0D7345A6\|6257\|47618\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `56a491797b1196508e27c87b86e228128f2632ebc672d8c63e80d2da5c8dae7f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 048 Magmortar  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua inglese, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 48 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0D71BF12` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 49 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 10 Att / 27 Dif / 0 Vel / 28 Asp / 2 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 6257, 2565 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 467, `MAGMORTAR` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Lanciafiamme, Psichico, Iper Raggio, Solarraggio | dichiarate dal modello |
| oggetto tenuto | 249 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|48\|0D71BF12\|6257\|2565\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|48\|0D71BF12\|6257\|2565\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `16f2cd74d235ecc035286de4458a181d90311b11c4815a713ca772a4f77fff2c` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 049 Lucario  `WORLD08`

**Insegna WORLD08, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WORLD08`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 49 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x00A589BF` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 39 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 7 Att / 20 Dif / 18 Vel / 27 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WORLD08` | dichiarato dal modello |
| identificativo, segreto | 8178, 6406 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 448, `LUCARIO` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Palmoforza, Ossoraffica, Giornodisole, Calciardente | dichiarate dal modello |
| oggetto tenuto | 234 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|49\|00A589BF\|8178\|6406\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|49\|00A589BF\|8178\|6406\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `c17926c8d1124b406fed6a6237ff46724b48aecee94cedbbb9edd5cdb0c210e9` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 050 Milotic  `VGC09`

**Insegna VGC09, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `VGC09`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 50 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2A0F0ED6` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 63 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 7 Att / 14 Dif / 23 Vel / 0 Asp / 18 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `VGC09` | dichiarato dal modello |
| identificativo, segreto | 5099, 14128 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 350, `MILOTIC` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Pioggiadanza, Ripresa, Idropompa, Ventogelato | dichiarate dal modello |
| oggetto tenuto | 273 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|50\|2A0F0ED6\|5099\|14128\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|50\|2A0F0ED6\|5099\|14128\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6d3e80add897d7cfa5a8700719b0473d7fa181dbc0accbd8dded8716bbdada67` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 051 Milotic  `VGC09`

**Insegna VGC09, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `VGC09`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 51 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x25408DF3` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 63 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 11 Att / 12 Dif / 0 Vel / 18 Asp / 8 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `VGC09` | dichiarato dal modello |
| identificativo, segreto | 5309, 48136 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 350, `MILOTIC` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Pioggiadanza, Ripresa, Idropompa, Ventogelato | dichiarate dal modello |
| oggetto tenuto | 273 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|51\|25408DF3\|5309\|48136\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|51\|25408DF3\|5309\|48136\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `cfc8371382f38344f68033a2c2db359a00998de7061b10381190c21109f4cccb` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 052 Regigigas  `EUSMR09`

**Insegna EUSMR09, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `EUSMR09`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 52 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x434FBAF9` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 112 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 26 Att / 1 Dif / 31 Vel / 19 Asp / 22 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `EUSMR09` | dichiarato dal modello |
| identificativo, segreto | 7189, 21084 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 486, `REGIGIGAS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Metaltestata, Frana, Ventogelato, Sbriciolmano | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|52\|00000001\|7189\|21084\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|52\|00000001\|7189\|21084\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `2580ec17796ddc6ad5210cb2a80dff4f4e02b202db3d7791329fcee43199c58d` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 053 Weavile  `WORLD09`

**Insegna WORLD09, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WORLD09`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 53 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x14B93A87` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 9 Att / 7 Dif / 20 Vel / 18 Asp / 4 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WORLD09` | dichiarato dal modello |
| identificativo, segreto | 8159, 46299 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 461, `WEAVILE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Bruciapelo, Geloscheggia, Nottesferza, Breccia | dichiarate dal modello |
| oggetto tenuto | 275 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|53\|14B93A87\|8159\|46299\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|53\|14B93A87\|8159\|46299\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3b718cdc544e6c236b23890b5037a01b4038e1e3a2e99d9b593df8f2d3543b64` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 054 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 54 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x6BA909A1` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Lesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 26 Att / 19 Dif / 13 Vel / 3 Asp / 12 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 1859 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Meteorpugno, Troppoforte, Iper Raggio | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|54\|00000001\|3060\|1859\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|54\|00000001\|3060\|1859\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `720bcc2f073e07de633861306a2811d593f7f519dfe941aafbb58bf62f98a2cd` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 055 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 55 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0E16636A` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Mite | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 11 Att / 27 Dif / 4 Vel / 15 Asp / 0 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 19353 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Individua, Contrattacco, Specchiovelo | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|55\|00000001\|3060\|19353\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|55\|00000001\|3060\|19353\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `7abcf6588b20fa4229dc818f6f2ff3b517c74ecdc42051eb51d9ff8ec1521c0d` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 056 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 56 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x59C9D47A` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Birbona | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 12 Att / 19 Dif / 16 Vel / 22 Asp / 11 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 31003 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Fulmisguardo, Avvolgibotta, Ombra Notturna | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|56\|00000001\|3060\|31003\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|56\|00000001\|3060\|31003\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `4f827ca767dd6e40536a54651f6ae9fd269778270f1b1fd0c8a32b12f4860356` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 057 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 57 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x291BB5FC` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Mite | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 24 Att / 18 Dif / 9 Vel / 20 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 56906 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Comete, Doppioteam, Extrarapido | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|57\|00000001\|3060\|56906\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|57\|00000001\|3060\|56906\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `91a47fb9a6b3ca492cd3d73eb12d3866b444ed2dd7fb7d7f7f1fe57b47653808` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 058 Heatran  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 58 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x3F89B3E4` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 18 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 30 Att / 12 Dif / 15 Vel / 19 Asp / 12 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 4100 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 485, `HEATRAN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Eruzione, Magmaclisma, Geoforza, Forzantica | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|58\|3F89B3E4\|3060\|4100\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|58\|3F89B3E4\|3060\|4100\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f0f3b334845ec96c383e9d3f548c189f7444aeaf5ee195f81a7d659866f6795e` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 059 Shaymin  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua inglese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 59 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x092AC744` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 9 Att / 8 Dif / 31 Vel / 30 Asp / 31 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 15911 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Crescita, Fogliamagica, Parassiseme, Sintesi | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|59\|00000001\|3060\|15911\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|59\|00000001\|3060\|15911\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `019b2f8ca46a4d05bc68c870f66a4c33a82e8b9b2e38fe4d6d18dd69f234f5c0` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 060 Darkrai  `ALAMOS`

**Insegna ALAMOS, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ALAMOS`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 60 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x32E2B754` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 14 Att / 22 Dif / 22 Vel / 6 Asp / 4 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ALAMOS` | dichiarato dal modello |
| identificativo, segreto | 7038, 44409 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fragortempo, Fendispazio, Incubo, Ipnosi | dichiarate dal modello |
| oggetto tenuto | 208 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|60\|00000001\|7038\|44409\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|60\|00000001\|7038\|44409\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `24c8eb7c935756075ef6b14a886148baaba6d490618eb550b8c577bc75bdcff5` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 061 Shaymin  `Film11`

**Insegna Film11, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Film11`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 61 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x97FA4C4C` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Cauta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 15 Att / 22 Dif / 17 Vel / 6 Asp / 31 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Film11` | dichiarato dal modello |
| identificativo, segreto | 4019, 45671 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Infuriaseme, Aromaterapia, Sostituto, Energipalla | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|61\|00000001\|4019\|45671\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|61\|00000001\|4019\|45671\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `63de28427c24e85d8e09357e42e32e599f8fb30448abeba634e2c731bfeb0000` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 064 Arceus  `MICHINA`

**Insegna MICHINA, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `MICHINA`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 64 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x847C554B` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Lesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 121 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 7 Att / 22 Dif / 13 Vel / 1 Asp / 5 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `MICHINA` | dichiarato dal modello |
| identificativo, segreto | 2010, 22297 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 493, `ARCEUS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Giudizio, Fragortempo, Fendispazio, Oscurotuffo | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|64\|00000001\|2010\|22297\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|64\|00000001\|2010\|22297\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `a54de36bff604802eefa5f47c45e334570871a236fe4d81dc35756d9243d7662` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 066 Pichu  `PRI2010`

**Insegna PRI2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PRI2010`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 66 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x65BF5CF4` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 1 Att / 4 Dif / 0 Vel / 12 Asp / 1 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PRI2010` | dichiarato dal modello |
| identificativo, segreto | 3050, 12961 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 172, `PICHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Sottocarica, Locomovolt, Rimonta, Resistenza | dichiarate dal modello |
| oggetto tenuto | 229 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|66\|65BF5CF4\|3050\|12961\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|66\|65BF5CF4\|3050\|12961\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `ae37e31e6cfa645b142c5101f6c9615f8d6bc893697af2524fe92096ca0f2a97` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 067 Darkrai  `Almia`

**Insegna Almia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Almia`, la carta è in lingua francese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 67 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xD363FB94` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 16 Att / 15 Dif / 24 Vel / 8 Asp / 12 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Almia` | dichiarato dal modello |
| identificativo, segreto | 3208, 21867 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Vuototetro, Neropulsar, Palla Ombra, Doppioteam | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|67\|00000001\|3208\|21867\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|67\|00000001\|3208\|21867\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `102dcdc91c0647010eacb99d05744b84da04c88aa1aeab010d7b3a4d75b918c8` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 068 Riolu  `Karel`

**Insegna Karel, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Karel`, la carta è in lingua francese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 68 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x06A6D188` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 80 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 20 Att / 24 Dif / 17 Vel / 9 Asp / 7 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Karel` | dichiarato dal modello |
| identificativo, segreto | 3208, 16165 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 447, `RIOLU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Sferapulsar, Ombrartigli, Pugnoscarica, Assorbipugno | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|68\|06A6D188\|3208\|16165\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|68\|06A6D188\|3208\|16165\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `c0c02ce2d9e8f3acb1ab4303c1e645135ab7923a551dfd6abfab2171f0f844ba` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 069 Jirachi  `ETE2010`

**Insegna ETE2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ETE2010`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 69 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x99782741` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 12 Att / 5 Dif / 23 Vel / 22 Asp / 15 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ETE2010` | dichiarato dal modello |
| identificativo, segreto | 6260, 49062 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 385, `JIRACHI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo, Dragobolide | dichiarate dal modello |
| oggetto tenuto | 201 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|69\|00000001\|6260\|49062\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|69\|00000001\|6260\|49062\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5d10c28e2febbd31998e82d0edbd173f4c76140b00917da4ab311a405a80deb2` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 072 Eevee  `VGC10`

**Insegna VGC10, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `VGC10`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 72 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x241ACEB1` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 91 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 7 Att / 26 Dif / 21 Vel / 10 Asp / 31 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `VGC10` | dichiarato dal modello |
| identificativo, segreto | 5080, 63860 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 133, `EVOLI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Codacciaio, Asso, Flagello, Attacco Rapido | dichiarate dal modello |
| oggetto tenuto | 275 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|72\|241ACEB1\|5080\|63860\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|72\|241ACEB1\|5080\|63860\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6786ace1a912df1d0b5c8994a894011f28f4b46f3ebd53a045ef60b0876dd724` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 073 Mew  `AUT2010`

**Insegna AUT2010, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `AUT2010`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 73 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xFFC48402` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Sicura | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 4 Att / 25 Dif / 18 Vel / 4 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `AUT2010` | dichiarato dal modello |
| identificativo, segreto | 10160, 49582 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 151, `MEW` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 135 | dichiarati dal modello |
| mosse | Botta | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|73\|00000001\|10160\|49582\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|73\|00000001\|10160\|49582\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `9d7ef32600d3134a2373110da65b5ca4f80bf6a1074ce5cf40609222fa04e5b9` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 075 Raikou  `HVR2011`

**Insegna HVR2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `HVR2011`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 75 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x4112985E` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 24 Att / 17 Dif / 12 Vel / 9 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `HVR2011` | dichiarato dal modello |
| identificativo, segreto | 2071, 53596 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Elettrocannone, Sferapulsar, Extrarapido, Palla Clima | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|75\|4112985E\|2071\|53596\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|75\|4112985E\|2071\|53596\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `c27953830fe4d016da7b1b5168949fe9bc7294c7cb2e132693c09898efdfa557` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 076 Entei  `HVR2011`

**Insegna HVR2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `HVR2011`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 76 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7A0AEB6A` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 8 Att / 22 Dif / 13 Vel / 5 Asp / 0 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `HVR2011` | dichiarato dal modello |
| identificativo, segreto | 2141, 39226 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Fuococarica, Gridodilotta, Extrarapido, Tritartigli | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|76\|7A0AEB6A\|2141\|39226\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|76\|7A0AEB6A\|2141\|39226\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `0851fab0e25f52f97c1186cdbd0a5036d2a247e6b29838c2b8c8f685870c5aab` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 077 Suicune  `HVR2011`

**Insegna HVR2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `HVR2011`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 77 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x19B5925A` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 29 Att / 24 Dif / 20 Vel / 27 Asp / 14 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `HVR2011` | dichiarato dal modello |
| identificativo, segreto | 2211, 33614 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Purogelo, Eterelama, Extrarapido, Acquanello | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|77\|19B5925A\|2211\|33614\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|77\|19B5925A\|2211\|33614\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `d7cf2d690a630b14d2a818c9ff0e8a6b437dc3916db10c4cff965777f9624805` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 078 Celebi  `HVR2011`

**Insegna HVR2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `HVR2011`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 78 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xDAEE17AF` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 19 Att / 2 Dif / 3 Vel / 12 Asp / 15 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `HVR2011` | dichiarato dal modello |
| identificativo, segreto | 1211, 30170 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 251, `CELEBI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Verdebufera, Ripresa, Congiura, Curardore | dichiarate dal modello |
| oggetto tenuto | 211 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|78\|00000001\|1211\|30170\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|78\|00000001\|1211\|30170\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `1baf4b198d6467d82fe23154fade569527b9573b3d20f9e0752de321e8de01ed` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 079 Pikachu  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua francese, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 79 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x19D97C13` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 7 Att / 27 Dif / 24 Vel / 13 Asp / 12 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 2384 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | dichiarati dal modello |
| mosse | Locomovolt, Surf, Colpocoda, Tuononda | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|79\|19D97C13\|12077\|2384\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|79\|19D97C13\|12077\|2384\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `c507452181e9ee5da72242d40e5650059b7d51bc547fb9f1f6dc82c5073ff2ef` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 080 Electivire  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua francese, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 80 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0D7345A6` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 78 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 15 PS / 5 Att / 15 Dif / 22 Vel / 13 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 31297 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 466, `ELEKABLE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Tuonopugno, Gelopugno, Incrocolpo, Terremoto | dichiarate dal modello |
| oggetto tenuto | 242 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|80\|0D7345A6\|12077\|31297\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|80\|0D7345A6\|12077\|31297\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `1ee4d3dfa7a8b982ca55106550f87a782373225796b66347994897815e3eefd2` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 081 Magmortar  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua francese, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 81 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0D71BF12` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 49 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 8 Att / 19 Dif / 19 Vel / 14 Asp / 25 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 12473 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 467, `MAGANON` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Lanciafiamme, Psichico, Iper Raggio, Solarraggio | dichiarate dal modello |
| oggetto tenuto | 249 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|81\|0D71BF12\|12077\|12473\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|81\|0D71BF12\|12077\|12473\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `cde3be721971238eafdf2fa256bc793854e027ec8ea9f9f61e49575a8131c7d7` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 082 Milotic  `VGC09`

**Insegna VGC09, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `VGC09`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 82 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x44B72ED0` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 63 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 29 PS / 25 Att / 24 Dif / 18 Vel / 18 Asp / 12 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `VGC09` | dichiarato dal modello |
| identificativo, segreto | 5309, 32473 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 350, `MILOBELLUS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Pioggiadanza, Ripresa, Idropompa, Ventogelato | dichiarate dal modello |
| oggetto tenuto | 273 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|82\|44B72ED0\|5309\|32473\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|82\|44B72ED0\|5309\|32473\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f17e442c88fcc276fe22a94769a7626e1bf8ddaddd80d4aaeb5daaaa2d88e1ab` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 083 Regigigas  `EUETE09`

**Insegna EUETE09, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `EUETE09`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 83 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xA6B429F8` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Sicura | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 112 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 11 Att / 21 Dif / 29 Vel / 9 Asp / 13 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `EUETE09` | dichiarato dal modello |
| identificativo, segreto | 7189, 50753 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 486, `REGIGIGAS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Metaltestata, Frana, Ventogelato, Sbriciolmano | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|83\|00000001\|7189\|50753\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|83\|00000001\|7189\|50753\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `21e44ad32cf459665ff2ec0e6107d5e88038e896a9d12573c5878ae46df7527c` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 084 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua francese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 84 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xD19807C0` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 8 Att / 19 Dif / 29 Vel / 15 Asp / 1 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 28479 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Meteorpugno, Troppoforte, Iper Raggio | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|84\|00000001\|3060\|28479\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|84\|00000001\|3060\|28479\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `56602121cb0cc9b1f474961355611f93dc5527b79167224916362423937b03f3` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 085 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua francese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 85 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x070C0029` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 31 PS / 0 Att / 21 Dif / 14 Vel / 6 Asp / 10 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 16395 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Individua, Contrattacco, Specchiovelo | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|85\|00000001\|3060\|16395\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|85\|00000001\|3060\|16395\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `121af907851b3c01b0fc428ebbf9185448d0f1b6fc5c60db8b13648f5e5d334f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 086 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua francese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 86 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xA8CAD500` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 14 Att / 27 Dif / 27 Vel / 20 Asp / 14 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 21534 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Fulmisguardo, Avvolgibotta, Ombra Notturna | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|86\|00000001\|3060\|21534\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|86\|00000001\|3060\|21534\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e577e18b425038eb494250d6133b0d1a9b6aa15b4ea17e295f355088991c1fad` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 087 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua francese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 87 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xB91FE79C` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 12 Att / 6 Dif / 18 Vel / 7 Asp / 14 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 14457 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Comete, Doppioteam, Extrarapido | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|87\|00000001\|3060\|14457\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|87\|00000001\|3060\|14457\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `b54a9d5a94c988279d7780647ecf4210fd15ff53f8107a69983c71ed33959f45` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 088 Heatran  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua francese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 88 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x541107F4` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 18 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 26 Att / 27 Dif / 25 Vel / 13 Asp / 30 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 6817 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 485, `HEATRAN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Eruzione, Magmaclisma, Geoforza, Forzantica | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|88\|541107F4\|3060\|6817\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|88\|541107F4\|3060\|6817\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `4bd03a7d86c1920ddf3673128d062bf8889081561465f75deec5addcfcaba2cf` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 089 Shaymin  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua francese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 89 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xE4517F16` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Cauta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 29 PS / 9 Att / 21 Dif / 13 Vel / 16 Asp / 21 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 33587 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Crescita, Fogliamagica, Parassiseme, Sintesi | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|89\|00000001\|3060\|33587\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|89\|00000001\|3060\|33587\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3c0612293897b1558a6cac0c068b2c96c0b1419e0052695f2715abdb2e6fdbdd` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 090 Pikachu  `NZone`

**Insegna NZone, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `NZone`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 90 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x5AEFB558` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 9 PS / 0 Att / 9 Dif / 5 Vel / 23 Asp / 3 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `NZone` | dichiarato dal modello |
| identificativo, segreto | 7310, 922 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 20, 8000 | dichiarati dal modello |
| mosse | Regalino, Attacco Rapido, Tuonoshock, Colpocoda | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|90\|5AEFB558\|7310\|922\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|90\|5AEFB558\|7310\|922\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `76f2657cb72a21c9db073bb0f403d3a4f31da6e357c74dbd62b02fbf4b73e39f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 091 Darkrai  `ALAMOS`

**Insegna ALAMOS, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ALAMOS`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 91 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xF38941A0` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Calma | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 26 Att / 3 Dif / 8 Vel / 13 Asp / 22 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ALAMOS` | dichiarato dal modello |
| identificativo, segreto | 7038, 30791 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fragortempo, Fendispazio, Incubo, Ipnosi | dichiarate dal modello |
| oggetto tenuto | 208 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|91\|00000001\|7038\|30791\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|91\|00000001\|7038\|30791\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5687842c79e9f4ae14287096f00a5e78eba4f8a10b6e3ca4a6771641045cd8d8` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 092 Shaymin  `Film11`

**Insegna Film11, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Film11`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 92 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1CACEB73` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 19 Att / 21 Dif / 3 Vel / 3 Asp / 27 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Film11` | dichiarato dal modello |
| identificativo, segreto | 4019, 45671 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Infuriaseme, Aromaterapia, Sostituto, Energipalla | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|92\|00000001\|4019\|45671\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|92\|00000001\|4019\|45671\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `cbf4dc398bf3d771aca3f3efc1106ac4910e4210602f97c6a6b900cb5cc20800` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 095 Arceus  `MICHINA`

**Insegna MICHINA, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `MICHINA`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 95 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7FEAC15B` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Sicura | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 121 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 6 PS / 24 Att / 7 Dif / 15 Vel / 8 Asp / 24 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `MICHINA` | dichiarato dal modello |
| identificativo, segreto | 2010, 58750 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 493, `ARCEUS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Giudizio, Fragortempo, Fendispazio, Oscurotuffo | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|95\|00000001\|2010\|58750\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|95\|00000001\|2010\|58750\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `1873ccc4af84eb9a53ecda02437f16f3564238192ec59d0bd18c465693feb8ae` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 097 Pichu  `FRü2010`

**Insegna FRü2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `FRü2010`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 97 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x4379979A` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 14 PS / 11 Att / 9 Dif / 29 Vel / 6 Asp / 15 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `FRü2010` | dichiarato dal modello |
| identificativo, segreto | 3050, 57103 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 172, `PICHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Sottocarica, Locomovolt, Rimonta, Resistenza | dichiarate dal modello |
| oggetto tenuto | 229 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|97\|4379979A\|3050\|57103\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|97\|4379979A\|3050\|57103\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `98b2d6ddca90ff122753d81c90c8f87cbcf893d8a30f5708c561211961f012cf` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 098 Darkrai  `Almia`

**Insegna Almia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Almia`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 98 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xA5A93B41` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 9 Att / 23 Dif / 9 Vel / 10 Asp / 25 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Almia` | dichiarato dal modello |
| identificativo, segreto | 3208, 11046 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Vuototetro, Neropulsar, Palla Ombra, Doppioteam | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|98\|00000001\|3208\|11046\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|98\|00000001\|3208\|11046\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f81c1341e25e169be49a0c4b79a5580c934c1303b189adb98b289c14773fc173` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 099 Riolu  `Kyle`

**Insegna Kyle, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Kyle`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 99 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x06A6D188` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 80 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 27 Att / 0 Dif / 23 Vel / 15 Asp / 31 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Kyle` | dichiarato dal modello |
| identificativo, segreto | 3208, 33861 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 447, `RIOLU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Sferapulsar, Ombrartigli, Pugnoscarica, Assorbipugno | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|99\|06A6D188\|3208\|33861\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|99\|06A6D188\|3208\|33861\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `685d85b2a608ce04ee7bb70b7411e2ea4d54689703b037c863b74e2134517c62` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 100 Jirachi  `SO2010`

**Insegna SO2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `SO2010`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 100 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xFF94A438` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Cauta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 11 Att / 1 Dif / 29 Vel / 9 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `SO2010` | dichiarato dal modello |
| identificativo, segreto | 6260, 55068 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 385, `JIRACHI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo, Dragobolide | dichiarate dal modello |
| oggetto tenuto | 201 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|100\|00000001\|6260\|55068\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|100\|00000001\|6260\|55068\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6cd002c51ef6dd76b3af38a7b5cfb95bbafe447a860fcc80ada34e8a54026740` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 103 Eevee  `VGC10`

**Insegna VGC10, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `VGC10`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 103 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7E2B3E8B` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 91 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 18 Att / 6 Dif / 20 Vel / 4 Asp / 2 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `VGC10` | dichiarato dal modello |
| identificativo, segreto | 5080, 21368 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 133, `EVOLI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Codacciaio, Asso, Flagello, Attacco Rapido | dichiarate dal modello |
| oggetto tenuto | 275 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|103\|7E2B3E8B\|5080\|21368\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|103\|7E2B3E8B\|5080\|21368\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `298473c7bed92375f3d7fcb4c290e240401a46a98c8262ae40f85a59e5efab29` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 104 Mew  `HRB2010`

**Insegna HRB2010, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `HRB2010`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 104 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x114AB384` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 12 Att / 29 Dif / 16 Vel / 24 Asp / 0 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `HRB2010` | dichiarato dal modello |
| identificativo, segreto | 10160, 60070 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 151, `MEW` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 135 | dichiarati dal modello |
| mosse | Botta | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|104\|00000001\|10160\|60070\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|104\|00000001\|10160\|60070\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `055f90504db228b16d42020e0a8ec8dc2cf742b6c161e43552f62e971cd6c15e` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 106 Raikou  `WIN2011`

**Insegna WIN2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WIN2011`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 106 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x5551B96C` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 9 PS / 1 Att / 17 Dif / 16 Vel / 20 Asp / 12 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WIN2011` | dichiarato dal modello |
| identificativo, segreto | 2071, 58408 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Elettrocannone, Sferapulsar, Extrarapido, Palla Clima | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|106\|5551B96C\|2071\|58408\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|106\|5551B96C\|2071\|58408\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `b701583401f118f5527375ed436aa5a68397972b97d4dc735105867ca6f1d57f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 107 Entei  `WIN2011`

**Insegna WIN2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WIN2011`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 107 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x3E8B7294` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 20 Att / 18 Dif / 10 Vel / 12 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WIN2011` | dichiarato dal modello |
| identificativo, segreto | 2141, 17474 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Fuococarica, Gridodilotta, Extrarapido, Tritartigli | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|107\|3E8B7294\|2141\|17474\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|107\|3E8B7294\|2141\|17474\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `252ac209122df013c3ef68f1f0d3a4823af81352161e914e7b937831706fcd8c` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 108 Suicune  `WIN2011`

**Insegna WIN2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WIN2011`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 108 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x5670BA6C` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 17 Att / 0 Dif / 9 Vel / 29 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WIN2011` | dichiarato dal modello |
| identificativo, segreto | 2211, 58555 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Purogelo, Eterelama, Extrarapido, Acquanello | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|108\|5670BA6C\|2211\|58555\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|108\|5670BA6C\|2211\|58555\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `19139247ca28903c72b5282662b4cd95bb9608a0a31e3df03f1ce9b012d5d3ac` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 109 Celebi  `WIN2011`

**Insegna WIN2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `WIN2011`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 109 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x4DEFD36A` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Scaltra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 17 Att / 4 Dif / 28 Vel / 31 Asp / 16 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `WIN2011` | dichiarato dal modello |
| identificativo, segreto | 1211, 7356 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 251, `CELEBI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Verdebufera, Ripresa, Congiura, Curardore | dichiarate dal modello |
| oggetto tenuto | 211 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|109\|00000001\|1211\|7356\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|109\|00000001\|1211\|7356\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3c324b45ead318c5179e0dcf35b4b74e6495bd828a26432b735a950084b582f4` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 110 Pikachu  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua tedesco, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 110 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x19D97C13` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 10 Att / 18 Dif / 22 Vel / 17 Asp / 18 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 33009 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | dichiarati dal modello |
| mosse | Locomovolt, Surf, Colpocoda, Tuononda | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|110\|19D97C13\|12077\|33009\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|110\|19D97C13\|12077\|33009\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `01fd9f92cab1838ed5f3888c3bb269c60fdc8e5fe3a38f82453009df27535c33` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 111 Electivire  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua tedesco, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 111 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0D7345A6` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 78 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 11 Att / 18 Dif / 5 Vel / 4 Asp / 16 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 41731 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 466, `ELEVOLTEK` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Tuonopugno, Gelopugno, Incrocolpo, Terremoto | dichiarate dal modello |
| oggetto tenuto | 242 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|111\|0D7345A6\|12077\|41731\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|111\|0D7345A6\|12077\|41731\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `cc319cbbf0645eca92dca4c434517a8f6baf483913b7f2d2736f1f895b7d6c1e` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 112 Magmortar  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua tedesco, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 112 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0D71BF12` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 49 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 26 Att / 4 Dif / 6 Vel / 27 Asp / 12 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 20088 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 467, `MAGBRANT` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Lanciafiamme, Psichico, Iper Raggio, Solarraggio | dichiarate dal modello |
| oggetto tenuto | 249 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|112\|0D71BF12\|12077\|20088\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|112\|0D71BF12\|12077\|20088\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `0f3398790d6b7b25c03e3283ac8774f97f0e3576db8f8aaa4bb2bf10dea9504c` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 113 Milotic  `VGC09`

**Insegna VGC09, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `VGC09`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 113 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7A35E5B0` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 63 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 30 Att / 19 Dif / 9 Vel / 20 Asp / 19 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `VGC09` | dichiarato dal modello |
| identificativo, segreto | 5309, 35642 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 350, `MILOTIC` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Pioggiadanza, Ripresa, Idropompa, Ventogelato | dichiarate dal modello |
| oggetto tenuto | 273 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|113\|7A35E5B0\|5309\|35642\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|113\|7A35E5B0\|5309\|35642\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6913f1be7154087b7e5f7c540fbe9a494eadf3d49f930f5144089a5c28528c99` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 114 Regigigas  `EUSMR09`

**Insegna EUSMR09, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `EUSMR09`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 114 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1B355471` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 112 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 6 PS / 22 Att / 19 Dif / 17 Vel / 9 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `EUSMR09` | dichiarato dal modello |
| identificativo, segreto | 7189, 24304 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 486, `REGIGIGAS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Metaltestata, Frana, Ventogelato, Sbriciolmano | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|114\|00000001\|7189\|24304\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|114\|00000001\|7189\|24304\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `35c676c14e43fa3111fbab7eb244b24a608a70b83375e66abf71726cbf586af1` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 115 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 115 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x37BEEA2D` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 26 Att / 10 Dif / 12 Vel / 13 Asp / 8 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 21463 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Meteorpugno, Troppoforte, Iper Raggio | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|115\|00000001\|3060\|21463\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|115\|00000001\|3060\|21463\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `d5a96bdd160376f37eaa2bcb36fa48a9a4d2d645d514c3d3c69289120ceb7617` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 116 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 116 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xAE7E3ED1` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Schiva | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 17 Att / 23 Dif / 9 Vel / 23 Asp / 7 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 9379 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Individua, Contrattacco, Specchiovelo | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|116\|00000001\|3060\|9379\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|116\|00000001\|3060\|9379\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `4943ba1699e19a23585671c9efc83f32f78e7e94cf04ca87675b23693fb16f7b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 117 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 117 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0AA1D8EB` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 13 Att / 17 Dif / 8 Vel / 19 Asp / 14 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 38281 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Fulmisguardo, Avvolgibotta, Ombra Notturna | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|117\|00000001\|3060\|38281\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|117\|00000001\|3060\|38281\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `d73e89d4fa2296126492b7eb577b486fd2a8264ede8fac2a0e40bfdbe9e6f82a` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 118 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 118 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xEB14B7E1` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 19 Att / 0 Dif / 8 Vel / 27 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 60379 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Comete, Doppioteam, Extrarapido | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|118\|00000001\|3060\|60379\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|118\|00000001\|3060\|60379\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `984522c7eeb49d4bcaaa9b5f6d4ccf58e35758a36b30389c2b871e29ef286020` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 119 Heatran  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 119 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x63EE7AD0` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 18 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 30 Att / 7 Dif / 7 Vel / 25 Asp / 16 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 41818 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 485, `HEATRAN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Eruzione, Magmaclisma, Geoforza, Forzantica | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|119\|63EE7AD0\|3060\|41818\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|119\|63EE7AD0\|3060\|41818\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `93c912a8948835f80710351d7650436c6ba9c78e79428ecba2ec2573a751e9a2` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 120 Shaymin  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua tedesco, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 120 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x15BD0461` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Lesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 16 Att / 21 Dif / 23 Vel / 5 Asp / 18 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 54140 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | tedesco | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Crescita, Fogliamagica, Parassiseme, Sintesi | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|120\|00000001\|3060\|54140\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|120\|00000001\|3060\|54140\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `d10bafe1d5c9a9eb31ecf31cad703d759c755344120b09948f38d085b15e607b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 121 Darkrai  `ALAMOS`

**Insegna ALAMOS, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ALAMOS`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 121 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xD146BF18` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Fiacca | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 26 Att / 3 Dif / 14 Vel / 22 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ALAMOS` | dichiarato dal modello |
| identificativo, segreto | 7038, 22857 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fragortempo, Fendispazio, Incubo, Ipnosi | dichiarate dal modello |
| oggetto tenuto | 208 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|121\|00000001\|7038\|22857\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|121\|00000001\|7038\|22857\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f27768b7cc2a4aada1e8815503e6e9e5f382f91efc36465c9cc246ba72c48bee` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 122 Shaymin  `Film11`

**Insegna Film11, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Film11`, la carta è in lingua francese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 122 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7442C4B8` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 30 Att / 7 Dif / 4 Vel / 14 Asp / 31 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Film11` | dichiarato dal modello |
| identificativo, segreto | 4019, 45671 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | francese | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Infuriaseme, Aromaterapia, Sostituto, Energipalla | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|122\|00000001\|4019\|45671\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|122\|00000001\|4019\|45671\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `0b25b8f3357ef719b8043fe8ec7f511eb7550404d0b5f48bb0b62a19617ae0a2` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 125 Arceus  `MICHINA`

**Insegna MICHINA, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `MICHINA`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 125 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xA16B3E9C` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 121 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 6 Att / 20 Dif / 30 Vel / 25 Asp / 13 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `MICHINA` | dichiarato dal modello |
| identificativo, segreto | 2010, 25598 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 493, `ARCEUS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Giudizio, Fragortempo, Fendispazio, Oscurotuffo | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|125\|00000001\|2010\|25598\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|125\|00000001\|2010\|25598\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `a6e93d0c38cc32aed23bce62a0a930be623ad78344ea5e83f8f217fcd1f31e2f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 127 Pichu  `PRI2010`

**Insegna PRI2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PRI2010`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 127 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0F036ACC` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 30 Att / 14 Dif / 19 Vel / 29 Asp / 11 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PRI2010` | dichiarato dal modello |
| identificativo, segreto | 3050, 28194 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 172, `PICHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Sottocarica, Locomovolt, Rimonta, Resistenza | dichiarate dal modello |
| oggetto tenuto | 229 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|127\|0F036ACC\|3050\|28194\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|127\|0F036ACC\|3050\|28194\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `0ab126fdde971b04ba7bc6214c73ff5932a77024457a17685e02605702db749b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 128 Darkrai  `Almia`

**Insegna Almia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Almia`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 128 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xFA65F998` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 0 Att / 0 Dif / 2 Vel / 12 Asp / 13 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Almia` | dichiarato dal modello |
| identificativo, segreto | 3208, 26945 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Vuototetro, Neropulsar, Palla Ombra, Doppioteam | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|128\|00000001\|3208\|26945\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|128\|00000001\|3208\|26945\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `01412912d3c19856be94ac35058ef469844333a0d1c87a78b1eb52557ee409f3` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 129 Riolu  `Carlo`

**Insegna Carlo, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Carlo`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 129 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x06A6D188` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 80 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 6 PS / 14 Att / 4 Dif / 25 Vel / 5 Asp / 22 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Carlo` | dichiarato dal modello |
| identificativo, segreto | 3208, 45450 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 447, `RIOLU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Sferapulsar, Ombrartigli, Pugnoscarica, Assorbipugno | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|129\|06A6D188\|3208\|45450\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|129\|06A6D188\|3208\|45450\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `bc01c30abadfba409b9c86f506b793209ee360cac3faf64cb095bce77a466ee6` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 130 Jirachi  `EST2010`

**Insegna EST2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `EST2010`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 130 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xBA70F2FC` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 24 PS / 24 Att / 14 Dif / 17 Vel / 25 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `EST2010` | dichiarato dal modello |
| identificativo, segreto | 6260, 43570 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 385, `JIRACHI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo, Dragobolide | dichiarate dal modello |
| oggetto tenuto | 201 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|130\|00000001\|6260\|43570\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|130\|00000001\|6260\|43570\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `9d035248a96e242aad55adc4bec8fcc24db78c8622b08de7da820bcb91b9a911` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 133 Mew  `AUT2010`

**Insegna AUT2010, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `AUT2010`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 133 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0E6CA2A1` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Calma | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 28 Att / 16 Dif / 9 Vel / 16 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `AUT2010` | dichiarato dal modello |
| identificativo, segreto | 10160, 51954 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 151, `MEW` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 135 | dichiarati dal modello |
| mosse | Botta | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|133\|00000001\|10160\|51954\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|133\|00000001\|10160\|51954\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5be23bd8fd5618bffe5d8748427ef83d663bf4ef78dc4bf52390050054d8d81b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 135 Raikou  `INV2011`

**Insegna INV2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `INV2011`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 135 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x4BF05658` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 16 Att / 17 Dif / 8 Vel / 17 Asp / 10 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `INV2011` | dichiarato dal modello |
| identificativo, segreto | 2071, 5562 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Elettrocannone, Sferapulsar, Extrarapido, Palla Clima | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|135\|4BF05658\|2071\|5562\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|135\|4BF05658\|2071\|5562\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `7314f3ee794943498ea948566974dda5f59eeed860ef18cc252e2551926ef3fe` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 136 Entei  `INV2011`

**Insegna INV2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `INV2011`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 136 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x6A03ED02` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 20 Att / 8 Dif / 6 Vel / 14 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `INV2011` | dichiarato dal modello |
| identificativo, segreto | 2141, 36700 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Fuococarica, Gridodilotta, Extrarapido, Tritartigli | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|136\|6A03ED02\|2141\|36700\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|136\|6A03ED02\|2141\|36700\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `883f963d957525934aff0715fb672d07371b544a6dfdfee3c9337407e6c33107` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 137 Suicune  `INV2011`

**Insegna INV2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `INV2011`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 137 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x498F3C6A` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 24 Att / 2 Dif / 15 Vel / 12 Asp / 11 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `INV2011` | dichiarato dal modello |
| identificativo, segreto | 2211, 32065 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Purogelo, Eterelama, Extrarapido, Acquanello | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|137\|498F3C6A\|2211\|32065\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|137\|498F3C6A\|2211\|32065\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `0fa6a166747f1f5407344a82f9d7f0750b3fb4b97d481558a62c20536a2162c3` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 138 Celebi  `INV2011`

**Insegna INV2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `INV2011`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 138 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x5C1D4C94` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Calma | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 19 Att / 13 Dif / 28 Vel / 4 Asp / 20 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `INV2011` | dichiarato dal modello |
| identificativo, segreto | 1211, 26546 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 251, `CELEBI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Verdebufera, Ripresa, Congiura, Curardore | dichiarate dal modello |
| oggetto tenuto | 211 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|138\|00000001\|1211\|26546\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|138\|00000001\|1211\|26546\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `ef7fc990b4785b6f4b861098bc12d74058ba0787009217bcadd4ff11c6642b30` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 139 Pikachu  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua italiano, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 139 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x19D97C13` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 30 Att / 9 Dif / 15 Vel / 20 Asp / 14 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 31209 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | dichiarati dal modello |
| mosse | Locomovolt, Surf, Colpocoda, Tuononda | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|139\|19D97C13\|12077\|31209\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|139\|19D97C13\|12077\|31209\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f7a7c051dc6d9aff5ec9a7b04d27b6aef3b18ec4479408da2ac96e42700e01ab` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 140 Electivire  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua italiano, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 140 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0D7345A6` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 78 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 22 PS / 9 Att / 7 Dif / 25 Vel / 12 Asp / 5 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 57173 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 466, `ELECTIVIRE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Tuonopugno, Gelopugno, Incrocolpo, Terremoto | dichiarate dal modello |
| oggetto tenuto | 242 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|140\|0D7345A6\|12077\|57173\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|140\|0D7345A6\|12077\|57173\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e690ec487d3513acc60c2bf5b429679a855f3a627f089ed1d253f19a4c4f1d74` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 141 Magmortar  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua italiano, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 141 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0D71BF12` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 49 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 21 Att / 18 Dif / 3 Vel / 3 Asp / 0 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 57092 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 467, `MAGMORTAR` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Lanciafiamme, Psichico, Iper Raggio, Solarraggio | dichiarate dal modello |
| oggetto tenuto | 249 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|141\|0D71BF12\|12077\|57092\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|141\|0D71BF12\|12077\|57092\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `1c913b019e29f67606708c6ac47c057ee0275ee8e5015e244c7b00604eda2a3f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 142 Regigigas  `ESTEU09`

**Insegna ESTEU09, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ESTEU09`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 142 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2A327D9B` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Audace | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 112 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 14 PS / 7 Att / 26 Dif / 0 Vel / 18 Asp / 10 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ESTEU09` | dichiarato dal modello |
| identificativo, segreto | 7189, 26575 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 486, `REGIGIGAS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Metaltestata, Frana, Ventogelato, Sbriciolmano | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|142\|00000001\|7189\|26575\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|142\|00000001\|7189\|26575\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e74753751c9779351a288666a547a0255ab2c8c0038bf9a4ebbe9ab86e96a0ec` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 143 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 143 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xF94112F9` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 6 Att / 3 Dif / 31 Vel / 24 Asp / 28 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 22392 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Meteorpugno, Troppoforte, Iper Raggio | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|143\|00000001\|3060\|22392\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|143\|00000001\|3060\|22392\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `21a32363aaaa03233e43fe55fd58052fc9d832810eb0dbcdcd593dfd9e968496` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 144 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 144 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xD8256DB7` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 9 PS / 30 Att / 18 Dif / 20 Vel / 0 Asp / 25 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 33647 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Individua, Contrattacco, Specchiovelo | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|144\|00000001\|3060\|33647\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|144\|00000001\|3060\|33647\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `8fa37bc193c31e27df72709a6e731c6cb7aafa241ee5a888fa58b562293850da` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 145 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 145 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xE59BCF54` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Calma | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 26 Att / 18 Dif / 26 Vel / 21 Asp / 24 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 14518 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Fulmisguardo, Avvolgibotta, Ombra Notturna | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|145\|00000001\|3060\|14518\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|145\|00000001\|3060\|14518\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5c3751c0a30ade35cb5802b6b7fe2740e8ceacca8e3e96b6880327d9113b3009` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 146 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 146 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xD9434E7D` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Audace | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 4 Att / 7 Dif / 19 Vel / 17 Asp / 19 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 253 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Comete, Doppioteam, Extrarapido | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|146\|00000001\|3060\|253\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|146\|00000001\|3060\|253\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `ccfa17bb961351403ccabeb928d7bccc068e815d283f1353d40767c8c66e1344` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 147 Heatran  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 147 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x06640AEC` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 18 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 16 PS / 8 Att / 20 Dif / 13 Vel / 15 Asp / 20 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 14167 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 485, `HEATRAN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Eruzione, Magmaclisma, Geoforza, Forzantica | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|147\|06640AEC\|3060\|14167\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|147\|06640AEC\|3060\|14167\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `bebcd4c0460f1bc5ff4793fe83a2d54bd75e6407f95425d8b1677e6df765aed4` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 148 Shaymin  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua italiano, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 148 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xA9087353` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 27 PS / 15 Att / 0 Dif / 6 Vel / 27 Asp / 15 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 52283 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | italiano | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Crescita, Fogliamagica, Parassiseme, Sintesi | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|148\|00000001\|3060\|52283\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|148\|00000001\|3060\|52283\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `02e6da6a80bf3d9a93071f554ed0a5637c3298639a75b73ba798c40269867364` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 149 Slaking  `あきやま`

**Insegna あきやま, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `あきやま`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 149 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x19000D96` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 54 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 16 PS / 14 Att / 13 Dif / 9 Vel / 8 Asp / 7 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `あきやま` | dichiarato dal modello |
| identificativo, segreto | 1069, 20866 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 289, `ジョン` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Gigaimpatto, Ritorno, Ombrartigli, Aeroassalto | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|149\|19000D96\|1069\|20866\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|149\|19000D96\|1069\|20866\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `8c0c2af538a29f316ce56a4a15d1fbb57bb5dc307b46568aabc22c945add09e8` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 150 Octillery  `ごるこ`

**Insegna ごるこ, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ごるこ`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 150 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x00018134` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 21 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 14 Att / 16 Dif / 15 Vel / 21 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ごるこ` | dichiarato dal modello |
| identificativo, segreto | 5138, 43569 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 224, `オクタン` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Octazooka, Geloraggio, Segnoraggio, Iper Raggio | dichiarate dal modello |
| oggetto tenuto | 230 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|150\|00018134\|5138\|43569\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|150\|00018134\|5138\|43569\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3efb3497fe6bc9a9f53124dfc193c66061cae61e44eaba3636dfe7fdb4e0b845` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 151 Flygon  `ばば`

**Insegna ばば, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ばば`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 151 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x00003FD3` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ingenua | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 26 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 4 Att / 22 Dif / 30 Vel / 20 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ばば` | dichiarato dal modello |
| identificativo, segreto | 7018, 718 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 330, `ババイゴン` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Dragobolide, Retromarcia, Terremoto, Dragartigli | dichiarate dal modello |
| oggetto tenuto | 188 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|151\|00003FD3\|7018\|718\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|151\|00003FD3\|7018\|718\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `a40af0d783ec974d22e7409932dd97691b4fe72e64742e14638845b6b536376a` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 152 Meowth  `ゆっきーな`

**Insegna ゆっきーな, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ゆっきーな`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 152 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x092D211A` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 53 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 1 Att / 17 Dif / 3 Vel / 4 Asp / 27 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ゆっきーな` | dichiarato dal modello |
| identificativo, segreto | 12098, 20362 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 52, `ニャース` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 21, 9261 | dichiarati dal modello |
| mosse | Morso, Bruciapelo, Sfuriate, Stridio | dichiarate dal modello |
| oggetto tenuto | 262 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|152\|092D211A\|12098\|20362\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|152\|092D211A\|12098\|20362\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f0814c48ebe540942ade40d04141dadb3f30eca88954f094f709e81c44b3b382` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 153 Metagross  `レッド`

**Insegna レッド, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `レッド`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 153 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x074951B0` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Audace | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 29 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 16 PS / 6 Att / 29 Dif / 15 Vel / 14 Asp / 12 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `レッド` | dichiarato dal modello |
| identificativo, segreto | 2109, 30574 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 376, `ホームラン` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 62, 297910 | dichiarati dal modello |
| mosse | Pugnoscarica, Meteorpugno, Martelpugno, Cozzata Zen | dichiarate dal modello |
| oggetto tenuto | 184 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|153\|074951B0\|2109\|30574\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|153\|074951B0\|2109\|30574\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `12575033b2ac73dcd6fc20c61614025e19ea52f572e47a719795af3c5e95b024` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 154 Chatot  `コンサート`

**Insegna コンサート, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `コンサート`, la carta è in lingua giapponese, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 154 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x012221AF` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 51 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 4 Att / 15 Dif / 27 Vel / 1 Asp / 15 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `コンサート` | dichiarato dal modello |
| identificativo, segreto | 10286, 57436 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 441, `ペラップ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 25, 11735 | dichiarati dal modello |
| mosse | Speculmossa, Furia, Schiamazzo, Provocazione | dichiarate dal modello |
| oggetto tenuto | 218 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|154\|012221AF\|10286\|57436\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|154\|012221AF\|10286\|57436\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3410baefc43ca85f3e139662bee541eed380dad129b0630cd540b3401efcccdb` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 155 Electabuzz  `フェスタ`

**Insegna フェスタ, luogo 3029.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `フェスタ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 155 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0591AB80` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Birbona | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 20 Att / 19 Dif / 31 Vel / 9 Asp / 21 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `フェスタ` | dichiarato dal modello |
| identificativo, segreto | 11256, 25152 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 125, `エレブー` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Colpo Basso, Ondashock, Schermoluce, Tuonopugno | dichiarate dal modello |
| oggetto tenuto | 322 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3029, luogo 3029 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3029 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|155\|0591AB80\|11256\|25152\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|155\|0591AB80\|11256\|25152\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `2cd25dab35fff0ac2c49f24d983e09bb2be38f579556b411ad98fdf4cdc4a539` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 156 Magmar  `フェスタ`

**Insegna フェスタ, luogo 3029.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `フェスタ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 156 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x00C06C52` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 49 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 26 Att / 20 Dif / 10 Vel / 8 Asp / 1 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `フェスタ` | dichiarato dal modello |
| identificativo, segreto | 11256, 18298 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 126, `ブーバー` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Muro di Fumo, Turbofuoco, Stordiraggio, Fuocopugno | dichiarate dal modello |
| oggetto tenuto | 323 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3029, luogo 3029 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3029 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|156\|00C06C52\|11256\|18298\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|156\|00C06C52\|11256\|18298\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `4af31c0dcce4ac3a31a65db092a2d31c40aaa2ba7fc2044a8fc7b9a91a995fb8` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 157 Manaphy  `みずのたみ`

**Insegna みずのたみ, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `みずのたみ`, la carta è in lingua giapponese, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 157 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x373EC967` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Gentile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 93 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 0 Att / 19 Dif / 2 Vel / 25 Asp / 11 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `みずのたみ` | dichiarato dal modello |
| identificativo, segreto | 12226, 7700 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 490, `マナフィ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Codadiluce, Bolla, Docciascudo | dichiarate dal modello |
| oggetto tenuto | 221 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|157\|00000001\|12226\|7700\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|157\|00000001\|12226\|7700\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `fb04e76b6dedfea33b8f2b848bb64257c2fd92211cd0b02b29f58100cb76ad19` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 158 Tropius  `しょこたん`

**Insegna しょこたん, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `しょこたん`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 158 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x246E146B` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 34 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 20 Att / 10 Dif / 0 Vel / 12 Asp / 14 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `しょこたん` | dichiarato dal modello |
| identificativo, segreto | 2027, 62861 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 357, `トロピウス` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 53, 186096 | dichiarati dal modello |
| mosse | Eterelama, Sintesi, Giornodisole, Solarraggio | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|158\|246E146B\|2027\|62861\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|158\|246E146B\|2027\|62861\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `387ae9b501558170d657023c66842c88d4b9d001ce5e9caab4f0fefcebe18133` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 159 Darkrai  `えいがかん`

**Insegna えいがかん, luogo 3005.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `えいがかん`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 159 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xB8D73C45` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 30 Att / 20 Dif / 22 Vel / 20 Asp / 30 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `えいがかん` | dichiarato dal modello |
| identificativo, segreto | 7147, 29045 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 491, `ダークライ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fragortempo, Fendispazio, Incubo, Ipnosi | dichiarate dal modello |
| oggetto tenuto | 208 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3005, luogo 3005 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3005 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|159\|00000001\|7147\|29045\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|159\|00000001\|7147\|29045\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `721297c089fe51621201af64e068a2b26ea22b168f03d71b854f86bd5b012389` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 160 Whiscash  `やまもと`

**Insegna やまもと, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `やまもと`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 160 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2FC99D42` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Gentile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 12 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 1 Att / 7 Dif / 17 Vel / 22 Asp / 4 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `やまもと` | dichiarato dal modello |
| identificativo, segreto | 3217, 51799 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 340, `ナマズン` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 51, 132651 | dichiarati dal modello |
| mosse | Terremoto, Idrondata, Cozzata Zen, Gigaimpatto | dichiarate dal modello |
| oggetto tenuto | 187 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|160\|2FC99D42\|3217\|51799\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|160\|2FC99D42\|3217\|51799\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `829eed5b4a968945abe20d86088556628cfe0e7a23c72eb70fb501bfb331f60f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 161 Manaphy  `パルシティ`

**Insegna パルシティ, luogo 3062.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `パルシティ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 161 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x246E1477` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 93 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 10 Att / 20 Dif / 11 Vel / 27 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `パルシティ` | dichiarato dal modello |
| identificativo, segreto | 7157, 41056 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 490, `マナフィ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Idropulsar, Mulinello, Scudo Acido, Cuorbaratto | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3062, luogo 3062 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3062 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|161\|246E1477\|7157\|41056\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|161\|246E1477\|7157\|41056\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `1c18c31f1ade9bf464c2b172dd4880e1e93cf404cd3303686c0913dad1152439` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 162 Manaphy  `パルシティ`

**Insegna パルシティ, luogo 3062.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `パルシティ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 162 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7CEAC9FC` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Mite | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 93 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 15 Att / 6 Dif / 26 Vel / 22 Asp / 20 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `パルシティ` | dichiarato dal modello |
| identificativo, segreto | 7157, 6367 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 490, `マナフィ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Cuorbaratto, Idropulsar, Mulinello, Scudo Acido | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3062, luogo 3062 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3062 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|162\|00000001\|7157\|6367\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|162\|00000001\|7157\|6367\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3c2505194c7d2070f1c22b6a5e25dab53ef618816088016883843587a15ef01f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 163 Mew  `パルシティ`

**Insegna パルシティ, luogo 3062.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `パルシティ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 163 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x246E1476` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Furba | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 10 Att / 9 Dif / 20 Vel / 7 Asp / 7 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `パルシティ` | dichiarato dal modello |
| identificativo, segreto | 7157, 33606 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 151, `ミュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Trasformazione, Metronomo, Teletrasporto, Sferapulsar | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3062, luogo 3062 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3062 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|163\|246E1476\|7157\|33606\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|163\|246E1476\|7157\|33606\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `550c285327418b8c15bd814ae7daeaad79ff8fc431a8ca009acd802760d31361` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 164 Mew  `パルシティ`

**Insegna パルシティ, luogo 3062.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `パルシティ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 164 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xE5FBEF8E` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Schiva | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 27 Att / 31 Dif / 23 Vel / 10 Asp / 30 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `パルシティ` | dichiarato dal modello |
| identificativo, segreto | 7157, 49168 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 151, `ミュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Megapugno, Metronomo, Teletrasporto, Sferapulsar | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3062, luogo 3062 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3062 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|164\|00000001\|7157\|49168\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|164\|00000001\|7157\|49168\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `bfd1efadc2ef09ee8c94e8a6d9467b7ad5052dca3a91d74bbed1b679266690ca` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 165 Mew  `パルシティ`

**Insegna パルシティ, luogo 3062.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `パルシティ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 165 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xC0C787C0` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 20 Att / 2 Dif / 26 Vel / 5 Asp / 7 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `パルシティ` | dichiarato dal modello |
| identificativo, segreto | 7157, 13805 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 151, `ミュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Psichico, Metronomo, Teletrasporto, Sferapulsar | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3062, luogo 3062 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3062 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|165\|00000001\|7157\|13805\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|165\|00000001\|7157\|13805\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3c10a088e4053fbf54c16ec4a8be3e9016b00ceea4da0580228c0e8a6909fc5b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 166 Mew  `パルシティ`

**Insegna パルシティ, luogo 3062.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `パルシティ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 166 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xC423A306` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Sicura | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 15 PS / 24 Att / 17 Dif / 14 Vel / 21 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `パルシティ` | dichiarato dal modello |
| identificativo, segreto | 7157, 61127 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 151, `ミュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Forzantica, Metronomo, Teletrasporto, Sferapulsar | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3062, luogo 3062 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3062 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|166\|00000001\|7157\|61127\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|166\|00000001\|7157\|61127\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `d0b887befbd3ac79c461753393dc0f4dc8682abeb45ab271442c0e275e65baa0` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 167 Mew  `パルシティ`

**Insegna パルシティ, luogo 3062.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `パルシティ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 167 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x64029D0A` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Furba | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 23 Att / 1 Dif / 0 Vel / 0 Asp / 29 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `パルシティ` | dichiarato dal modello |
| identificativo, segreto | 7157, 43910 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 151, `ミュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Amnesia, Metronomo, Teletrasporto, Sferapulsar | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3062, luogo 3062 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3062 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|167\|00000001\|7157\|43910\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|167\|00000001\|7157\|43910\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `09cecbd802ea2a9145b2c53230fd15558029b31e502dce2a3e6e7141e3fd1a28` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 168 Mew  `パルシティ`

**Insegna パルシティ, luogo 3062.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `パルシティ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 168 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x4AB53922` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Schiva | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 27 Att / 19 Dif / 28 Vel / 7 Asp / 13 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `パルシティ` | dichiarato dal modello |
| identificativo, segreto | 7157, 45830 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 151, `ミュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Barriera, Metronomo, Teletrasporto, Sferapulsar | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3062, luogo 3062 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3062 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|168\|00000001\|7157\|45830\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|168\|00000001\|7157\|45830\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `252503ed9cd18c572f66ea8f52afd118c806329a4ac99da2847eed7076e21aa9` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 169 Lucario  `PALCITY`

**Insegna PALCITY, luogo 3062.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PALCITY`, la carta è in lingua inglese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 169 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x246E1486` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 80 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 22 PS / 2 Att / 27 Dif / 31 Vel / 4 Asp / 13 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PALCITY` | dichiarato dal modello |
| identificativo, segreto | 7157, 56541 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | inglese | dichiarata dal modello |
| specie interna, soprannome | 448, `LUCARIO` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Sferapulsar, Neropulsar, Dragopulsar, Idropulsar | dichiarate dal modello |
| oggetto tenuto | 233 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3062, luogo 3062 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3062 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|169\|246E1486\|7157\|56541\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|169\|246E1486\|7157\|56541\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `32649730ce73e2a6c6db067bef9c71c9ff146ebc4e03a2317a49ad8b22b2046d` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 171 Deoxys  `１０ｔｈ`

**Insegna １０ｔｈ, luogo 3005.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `１０ｔｈ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 171 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1D85A021` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Calma | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 31 Att / 19 Dif / 21 Vel / 14 Asp / 20 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `１０ｔｈ` | dichiarato dal modello |
| identificativo, segreto | 7147, 47015 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 386, `デオキシス` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Elettrocannone, Ferroscudo, Extrarapido | dichiarate dal modello |
| oggetto tenuto | 246 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3005, luogo 3005 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3005 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|171\|00000001\|7147\|47015\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|171\|00000001\|7147\|47015\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5150c698a006be87cd6ce2bcc186575ab5e2de995491a9754c210c50788bf46f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 172 Jirachi  `タナバタ`

**Insegna タナバタ, luogo 3074.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `タナバタ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 172 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x29397463` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 2 Att / 1 Dif / 18 Vel / 20 Asp / 5 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `タナバタ` | dichiarato dal modello |
| identificativo, segreto | 7077, 41928 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 385, `ジラーチ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo | dichiarate dal modello |
| oggetto tenuto | 202 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3074, luogo 3074 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3074 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|172\|00000001\|7077\|41928\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|172\|00000001\|7077\|41928\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `431b38dd1ce58d03970e8bca631de9b281fe7967ee1e6b0ce6582cc7c54e46d8` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 173 Jirachi  `タナバタ`

**Insegna タナバタ, luogo 3074.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `タナバタ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 173 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xBDA09657` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Gentile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 5 PS / 22 Att / 26 Dif / 7 Vel / 24 Asp / 9 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `タナバタ` | dichiarato dal modello |
| identificativo, segreto | 7077, 28320 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 385, `ジラーチ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo | dichiarate dal modello |
| oggetto tenuto | 203 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3074, luogo 3074 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3074 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|173\|00000001\|7077\|28320\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|173\|00000001\|7077\|28320\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `4f65c13582f603062cb748d850ba7c688f55898888aba7ceda9d9f49c016cb25` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 174 Charmander  `トウキョー`

**Insegna トウキョー, luogo 3053.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `トウキョー`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 174 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0A2B1E99` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Mite | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 66 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 9 PS / 16 Att / 28 Dif / 4 Vel / 3 Asp / 28 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `トウキョー` | dichiarato dal modello |
| identificativo, segreto | 7207, 12105 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 4, `ヒトカゲ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 40, 56660 | dichiarati dal modello |
| mosse | Ritorno, Introforza, Attacco Rapido, Gridodilotta | dichiarate dal modello |
| oggetto tenuto | 231 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3053, luogo 3053 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3053 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|174\|0A2B1E99\|7207\|12105\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|174\|0A2B1E99\|7207\|12105\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `bf2ecf0e11eebbc94ceafb423d5edfe71591a8511a469d61b8af6751cf2e30f0` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 175 Octillery  `ごるこ`

**Insegna ごるこ, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ごるこ`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 175 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x00018134` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 21 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 21 Att / 20 Dif / 17 Vel / 13 Asp / 28 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ごるこ` | dichiarato dal modello |
| identificativo, segreto | 10147, 31254 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 224, `オクタン` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Octazooka, Geloraggio, Segnoraggio, Iper Raggio | dichiarate dal modello |
| oggetto tenuto | 230 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|175\|00018134\|10147\|31254\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|175\|00018134\|10147\|31254\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6f9b61dc84bf0231ede64dad6b927f2596356f14352ccaf28aa6e245389a7b43` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 176 Electivire  `さいきょう`

**Insegna さいきょう, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `さいきょう`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 176 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1F26A1E8` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 78 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 29 Att / 19 Dif / 28 Vel / 12 Asp / 2 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `さいきょう` | dichiarato dal modello |
| identificativo, segreto | 11157, 31946 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 466, `エレキブル` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Schermoluce, Tuonopugno, Scarica, Fulmine | dichiarate dal modello |
| oggetto tenuto | 242 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|176\|1F26A1E8\|11157\|31946\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|176\|1F26A1E8\|11157\|31946\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5e75f96715cab9c1144d92ac20a32e3a8579d3fe249a486dab834436cb473f79` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 177 Magmortar  `さいきょう`

**Insegna さいきょう, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `さいきょう`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 177 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1F26A1F5` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 49 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 17 Att / 12 Dif / 28 Vel / 4 Asp / 24 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `さいきょう` | dichiarato dal modello |
| identificativo, segreto | 12017, 17582 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 467, `ブーバーン` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Stordiraggio, Fuocopugno, Lavasbuffo, Lanciafiamme | dichiarate dal modello |
| oggetto tenuto | 249 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|177\|1F26A1F5\|12017\|17582\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|177\|1F26A1F5\|12017\|17582\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `aae6025f451bf10e0058c15cb09ee97650aaad033b9701feb32a9536d0b45945` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 178 Milotic  `さいきょう`

**Insegna さいきょう, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `さいきょう`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 178 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0E2ED12E` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Sicura | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 63 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 22 Att / 14 Dif / 8 Vel / 29 Asp / 11 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `さいきょう` | dichiarato dal modello |
| identificativo, segreto | 12157, 37705 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 350, `ミロカロス` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Pioggiadanza, Ripresa, Idropompa, Geloraggio | dichiarate dal modello |
| oggetto tenuto | 273 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|178\|0E2ED12E\|12157\|37705\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|178\|0E2ED12E\|12157\|37705\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `2d947c416d9b2b606976f90957b20f174827b3c08d8f895f4ce4b2c2d0f98e5a` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 179 Dragonite  `さいきょう`

**Insegna さいきょう, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `さいきょう`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 179 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0E2CFBFC` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Mite | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 39 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 24 PS / 12 Att / 26 Dif / 19 Vel / 10 Asp / 27 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `さいきょう` | dichiarato dal modello |
| identificativo, segreto | 1158, 11342 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 149, `カイリュー` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Dragobolide, Fulmine, Oltraggio, Dragodanza | dichiarate dal modello |
| oggetto tenuto | 188 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|179\|0E2CFBFC\|1158\|11342\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|179\|0E2CFBFC\|1158\|11342\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `958e2ca57053ae3d1758d3b232fae2576e6939b2508266d5d8e96d96c9704cbc` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 180 Salamence  `さいきょう`

**Insegna さいきょう, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `さいきょう`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 180 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0E2CFBF0` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Birbona | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 22 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 24 Att / 17 Dif / 21 Vel / 18 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `さいきょう` | dichiarato dal modello |
| identificativo, segreto | 2158, 12900 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 373, `ボーマンダ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Idropompa, Pietrataglio, Fuocobomba, Dragartigli | dichiarate dal modello |
| oggetto tenuto | 250 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|180\|0E2CFBF0\|2158\|12900\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|180\|0E2CFBF0\|2158\|12900\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f0dcf6029152add0f441a50533c3b111ca77da9efb95689dd52d611a2c25f357` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 181 Darkrai  `アルミア`

**Insegna アルミア, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `アルミア`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 181 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x86676B69` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Furba | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 24 PS / 3 Att / 24 Dif / 0 Vel / 14 Asp / 30 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `アルミア` | dichiarato dal modello |
| identificativo, segreto | 3208, 28204 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 491, `ダークライ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Vuototetro, Neropulsar, Palla Ombra, Doppioteam | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|181\|00000001\|3208\|28204\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|181\|00000001\|3208\|28204\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f520ea0c86aef42ea56609f15322684c40644838295e4697a24d75511eaf8457` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 182 Riolu  `カイト`

**Insegna カイト, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `カイト`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 182 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x06A6D188` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 80 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 22 PS / 1 Att / 18 Dif / 21 Vel / 11 Asp / 5 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `カイト` | dichiarato dal modello |
| identificativo, segreto | 3208, 17806 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 447, `リオル` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Sferapulsar, Ombrartigli, Pugnoscarica, Assorbipugno | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|182\|06A6D188\|3208\|17806\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|182\|06A6D188\|3208\|17806\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `a9dc63933fa67ec70f5c01dcb6fe3fac9e893dd7c75a842ceedf3528befb8891` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 183 Regigigas  `テンイむら`

**Insegna テンイむら, luogo 3006.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `テンイむら`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 183 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xC0687BDE` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Schiva | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 112 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 4 Att / 13 Dif / 15 Vel / 10 Asp / 10 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `テンイむら` | dichiarato dal modello |
| identificativo, segreto | 7198, 29382 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 486, `レジギガス` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Metaltestata, Frana, Ventogelato, Sbriciolmano | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3006, luogo 3006 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3006 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|183\|00000001\|7198\|29382\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|183\|00000001\|7198\|29382\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e3bde663b396730ab06eeddc501a764595627b1fb9360009cc318f857b4454da` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 184 Shaymin  `えいがかん`

**Insegna えいがかん, luogo 3006.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `えいがかん`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 184 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x27834AC3` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Birbona | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 10 Att / 12 Dif / 16 Vel / 29 Asp / 24 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `えいがかん` | dichiarato dal modello |
| identificativo, segreto | 7198, 50784 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 492, `シェイミ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Infuriaseme, Aromaterapia, Sostituto, Energipalla | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3006, luogo 3006 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3006 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|184\|00000001\|7198\|50784\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|184\|00000001\|7198\|50784\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `b1e64244fbc1eff85d2d71106be7f5b8511eb78836aaf8640c8d835a8ec31bb1` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 185 Pikachu  `マック`

**Insegna マック, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `マック`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 185 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x21ACDA5A` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 28 PS / 17 Att / 23 Dif / 28 Vel / 11 Asp / 23 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `マック` | dichiarato dal modello |
| identificativo, segreto | 5308, 7501 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 20, 8000 | dichiarati dal modello |
| mosse | Attacco Rapido, Tuonoshock, Colpocoda, Regalino | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|185\|21ACDA5A\|5308\|7501\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|185\|21ACDA5A\|5308\|7501\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `129fdaa9a4276d00e8797deea1de64b3a7eb2ad6eaab51a59ac86e7560cc7307` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 186 Charmander  `トウキョー`

**Insegna トウキョー, luogo 3053.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `トウキョー`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 186 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0A2B1E97` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ingenua | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 66 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 24 Att / 19 Dif / 13 Vel / 10 Asp / 3 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `トウキョー` | dichiarato dal modello |
| identificativo, segreto | 7208, 27372 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 4, `ヒトカゲ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 40, 56660 | dichiarati dal modello |
| mosse | Ritorno, Introforza, Attacco Rapido, Gridodilotta | dichiarate dal modello |
| oggetto tenuto | 231 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3053, luogo 3053 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3053 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|186\|0A2B1E97\|7208\|27372\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|186\|0A2B1E97\|7208\|27372\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `b9f4f830ad70c89885082f4bfc9464f6d48c706dd0bf44c1a48056a67b82e0fa` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 187 Arceus  `えいがかん`

**Insegna えいがかん, luogo 3007.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `えいがかん`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 187 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1C0001A3` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 121 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 3 Att / 22 Dif / 29 Vel / 31 Asp / 18 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `えいがかん` | dichiarato dal modello |
| identificativo, segreto | 7189, 2831 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 493, `アルセウス` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Giudizio, Fragortempo, Fendispazio, Oscurotuffo | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3007, luogo 3007 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3007 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|187\|00000001\|7189\|2831\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|187\|00000001\|7189\|2831\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `1095fa4dcf63d0abfb20f2ca7103dd9b927e990b8d73dbca8aad5c7f776ad4f6` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 188 Jirachi  `タナバタ`

**Insegna タナバタ, luogo 3074.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `タナバタ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 188 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x4BECC6F9` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Scaltra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 10 Att / 10 Dif / 16 Vel / 22 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `タナバタ` | dichiarato dal modello |
| identificativo, segreto | 8188, 41454 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 385, `ジラーチ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo | dichiarate dal modello |
| oggetto tenuto | 211 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3074, luogo 3074 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3074 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|188\|00000001\|8188\|41454\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|188\|00000001\|8188\|41454\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `577af79e8be1150665163037071e47cc88828dc76c442f475c35625a7c203786` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 189 Pikachu  `ヨコハマ`

**Insegna ヨコハマ, luogo 3058.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ヨコハマ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 189 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x050CAFCB` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 17 Att / 4 Dif / 25 Vel / 5 Asp / 30 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ヨコハマ` | dichiarato dal modello |
| identificativo, segreto | 10108, 57139 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 40, 64000 | dichiarati dal modello |
| mosse | Surf, Tuono, Protezione | dichiarate dal modello |
| oggetto tenuto | 253 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3058, luogo 3058 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3058 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|189\|050CAFCB\|10108\|57139\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|189\|050CAFCB\|10108\|57139\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3264927e08fcba505fac9ce0c6af053e6ada8d59a7f5d43048533473653195e7` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 190 Pikachu  `ヨコハマ`

**Insegna ヨコハマ, luogo 3058.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ヨコハマ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 190 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x050CAFCB` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 9 PS / 23 Att / 31 Dif / 17 Vel / 27 Asp / 24 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ヨコハマ` | dichiarato dal modello |
| identificativo, segreto | 12268, 7242 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 40, 64000 | dichiarati dal modello |
| mosse | Surf, Tuono, Protezione | dichiarate dal modello |
| oggetto tenuto | 231 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3058, luogo 3058 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3058 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|190\|050CAFCB\|12268\|7242\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|190\|050CAFCB\|12268\|7242\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `483aabae4439dd72c0c7563510ab55adf8fb06945fdc667f027292fd132305b3` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 191 Milotic  `ＷＣＳ`

**Insegna ＷＣＳ, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ＷＣＳ`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 191 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xBC5E879E` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 63 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 0 Att / 24 Dif / 19 Vel / 4 Asp / 23 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ＷＣＳ` | dichiarato dal modello |
| identificativo, segreto | 10128, 7252 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 350, `ミロカロス` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Pioggiadanza, Ripresa, Idropompa, Ventogelato | dichiarate dal modello |
| oggetto tenuto | 273 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|191\|BC5E879E\|10128\|7252\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|191\|BC5E879E\|10128\|7252\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `a5fd3611dccbbb4157ba69bd1c5c6efba94a26ed01c600186d90c71546d9a346` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 193 Eevee  `ブイコレ`

**Insegna ブイコレ, luogo 3052.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ブイコレ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 193 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x04BCCC14` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Schiva | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 91 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 26 Att / 30 Dif / 10 Vel / 8 Asp / 21 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ブイコレ` | dichiarato dal modello |
| identificativo, segreto | 12068, 21977 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 133, `イーブイ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | dichiarati dal modello |
| mosse | Supplica, Morso, Altruismo, Attrazione | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3052, luogo 3052 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3052 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|193\|04BCCC14\|12068\|21977\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|193\|04BCCC14\|12068\|21977\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `0ad5dcc7760a727891f7ced588e7270487f75bbccd68caa89b4faf8d857b8153` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 194 Pikachu  `おねむり`

**Insegna おねむり, luogo 3052.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `おねむり`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 194 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2D98F2D5` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 12 Att / 20 Dif / 31 Vel / 5 Asp / 0 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `おねむり` | dichiarato dal modello |
| identificativo, segreto | 2079, 55619 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Riposo, Sonnolalia, Russare, Sbadiglio | dichiarate dal modello |
| oggetto tenuto | 150 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3052, luogo 3052 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3052 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|194\|2D98F2D5\|2079\|55619\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|194\|2D98F2D5\|2079\|55619\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `960dffb78e7ebe9730e8ebacfc604333668dca2a5004a142fd60214c1da616f5` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 195 Pichu  `しょこたん`

**Insegna しょこたん, luogo 3007.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `しょこたん`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 195 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x3F4F14F1` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 29 Att / 7 Dif / 1 Vel / 26 Asp / 16 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `しょこたん` | dichiarato dal modello |
| identificativo, segreto | 6199, 13193 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 172, `ピチュー` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Sottocarica, Locomovolt, Rimonta, Resistenza | dichiarate dal modello |
| oggetto tenuto | 229 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3007, luogo 3007 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3007 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|195\|3F4F14F1\|6199\|13193\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|195\|3F4F14F1\|6199\|13193\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e12b904ad31f5b1b323c699b4523c0ad0fbeb6218000ae8d28fdade288bdc1f8` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 196 Meowth  `オーサカ`

**Insegna オーサカ, luogo 3052.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `オーサカ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 196 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x213BCAAE` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 53 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 13 Att / 31 Dif / 30 Vel / 28 Asp / 5 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `オーサカ` | dichiarato dal modello |
| identificativo, segreto | 3209, 52529 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 52, `ニャース` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | dichiarati dal modello |
| mosse | Bruciapelo, Giornopaga, Assistente, Graffio | dichiarate dal modello |
| oggetto tenuto | 223 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3052, luogo 3052 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3052 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|196\|213BCAAE\|3209\|52529\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|196\|213BCAAE\|3209\|52529\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `8a2fe294a281d2e57308acf68beea22f33c58c94e6795b15deb1e40fe5ccd4b8` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 199 Jirachi  `NZ`

**Insegna NZ, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `NZ`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 199 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x20B8C63A` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 16 Att / 7 Dif / 31 Vel / 17 Asp / 1 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `NZ` | dichiarato dal modello |
| identificativo, segreto | 6199, 35776 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 385, `ジラーチ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo, Dragobolide | dichiarate dal modello |
| oggetto tenuto | 201 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|199\|00000001\|6199\|35776\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|199\|00000001\|6199\|35776\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `09483c21c039090f41d22403d0416a7d31a1fa8856e3f320376f5f2df26e88cf` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 200 Charmander  `トウキョー`

**Insegna トウキョー, luogo 3053.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `トウキョー`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 200 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x6342E753` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Birbona | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 66 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 27 PS / 1 Att / 4 Dif / 28 Vel / 29 Asp / 31 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `トウキョー` | dichiarato dal modello |
| identificativo, segreto | 7209, 34107 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 4, `ヒトカゲ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 40, 56660 | dichiarati dal modello |
| mosse | Ritorno, Introforza, Attacco Rapido, Gridodilotta | dichiarate dal modello |
| oggetto tenuto | 231 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3053, luogo 3053 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3053 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|200\|6342E753\|7209\|34107\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|200\|6342E753\|7209\|34107\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `61604c0ab0643ef39169d90761fd011b3d60ee7955e935b9a50648590569dc39` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 202 Chimchar  `ナゴヤ`

**Insegna ナゴヤ, luogo 3056.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ナゴヤ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 202 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x07AF0C20` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Mite | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 66 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 9 Att / 3 Dif / 5 Vel / 21 Asp / 16 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ナゴヤ` | dichiarato dal modello |
| identificativo, segreto | 9129, 63029 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 390, `ヒコザル` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 40, 56660 | dichiarati dal modello |
| mosse | Lanciafiamme, Tuonopugno, Laccioerboso, Altruismo | dichiarate dal modello |
| oggetto tenuto | 231 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3056, luogo 3056 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3056 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|202\|07AF0C20\|9129\|63029\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|202\|07AF0C20\|9129\|63029\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `319aa11fb188bff057e527c6cdd984d7ba2d537aaa7f75b043b24d27a15e96c6` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 203 Pikachu  `キョウト`

**Insegna キョウト, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `キョウト`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 203 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x56E5C6C4` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Birbona | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 7 Att / 13 Dif / 9 Vel / 31 Asp / 7 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `キョウト` | dichiarato dal modello |
| identificativo, segreto | 10039, 46553 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Ultimascelta, Regalino, Fulmine, Attacco Rapido | dichiarate dal modello |
| oggetto tenuto | 218 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|203\|56E5C6C4\|10039\|46553\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|203\|56E5C6C4\|10039\|46553\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `fdf58e05fbe01f52b76115046832a957c95efe239c3d0fdf5839dc2643279671` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 205 Eevee  `ＷＣＳ`

**Insegna ＷＣＳ, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ＷＣＳ`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 205 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x324BF1E5` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 91 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 6 Att / 8 Dif / 26 Vel / 6 Asp / 29 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ＷＣＳ` | dichiarato dal modello |
| identificativo, segreto | 1110, 51199 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 133, `イーブイ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Codacciaio, Asso, Flagello, Attacco Rapido | dichiarate dal modello |
| oggetto tenuto | 275 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|205\|324BF1E5\|1110\|51199\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|205\|324BF1E5\|1110\|51199\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `38ef0a8e01c1736f45fb21615b866b5ff5d80a2b3c72f7d2688cb60af26d81eb` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 206 Mew  `ススム`

**Insegna ススム, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ススム`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 206 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x35293640` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 31 Att / 7 Dif / 18 Vel / 16 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ススム` | dichiarato dal modello |
| identificativo, segreto | 11219, 50545 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 151, `ミュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 135 | dichiarati dal modello |
| mosse | Botta | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|206\|00000001\|11219\|50545\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|206\|00000001\|11219\|50545\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `aed9466385d987c11409f2fb1ae048edbe80f038806346f66161890cd008b879` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 207 Mew  `ススム`

**Insegna ススム, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ススム`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 207 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x09E14F71` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 20 Att / 3 Dif / 29 Vel / 4 Asp / 31 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ススム` | dichiarato dal modello |
| identificativo, segreto | 11219, 60403 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 151, `ミュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 135 | dichiarati dal modello |
| mosse | Botta | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|207\|00000001\|11219\|60403\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|207\|00000001\|11219\|60403\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `420a5624d0fc2eff76e7d56c85b06247e8940e1ec8d2f658bafbde94e6e64739` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 210 Pikachu  `アリオ`

**Insegna アリオ, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `アリオ`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 210 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x153F1E54` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 24 Att / 3 Dif / 15 Vel / 14 Asp / 19 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `アリオ` | dichiarato dal modello |
| identificativo, segreto | 11219, 28540 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 20, 8000 | dichiarati dal modello |
| mosse | Regalino, Attacco Rapido, Tuonoshock, Colpocoda | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|210\|153F1E54\|11219\|28540\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|210\|153F1E54\|11219\|28540\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `c0846fe3b700ac501ba00eee976254655e5a9ad7766d29ba565e03cbc1a56d64` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 211 Pikachu  `ヨコハマ`

**Insegna ヨコハマ, luogo 3058.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ヨコハマ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 211 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x34A76BB4` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Mite | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 6 Att / 23 Dif / 27 Vel / 9 Asp / 18 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ヨコハマ` | dichiarato dal modello |
| identificativo, segreto | 12269, 51055 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 40, 64000 | dichiarati dal modello |
| mosse | Surf, Tuono, Protezione | dichiarate dal modello |
| oggetto tenuto | 231 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3058, luogo 3058 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3058 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|211\|34A76BB4\|12269\|51055\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|211\|34A76BB4\|12269\|51055\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `b481b3c32ab6d8362d821ddeaa3026990f75c1b09203d19b7d2c86dedfdfc206` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 213 Raikou  `クラウン`

**Insegna クラウン, luogo 3008.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `クラウン`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 213 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x4627A80C` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 29 PS / 2 Att / 19 Dif / 17 Vel / 27 Asp / 18 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `クラウン` | dichiarato dal modello |
| identificativo, segreto | 6180, 62989 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 243, `ライコウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Elettrocannone, Sferapulsar, Extrarapido, Palla Clima | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3008, luogo 3008 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3008 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|213\|4627A80C\|6180\|62989\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|213\|4627A80C\|6180\|62989\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `84e7ccac4dfecec0eb6e838e887d72dfa7e65014c8c348cb502da4adef60b214` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 214 Entei  `クラウン`

**Insegna クラウン, luogo 3008.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `クラウン`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 214 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x27A055B8` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 6 PS / 2 Att / 15 Dif / 10 Vel / 7 Asp / 23 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `クラウン` | dichiarato dal modello |
| identificativo, segreto | 6180, 27198 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 244, `エンテイ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Fuococarica, Gridodilotta, Extrarapido, Tritartigli | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3008, luogo 3008 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3008 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|214\|27A055B8\|6180\|27198\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|214\|27A055B8\|6180\|27198\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `161a035d33d6e7a65481e497c66fab6cbc0092b7bc566d0a82683393b00633fe` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 215 Suicune  `クラウン`

**Insegna クラウン, luogo 3008.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `クラウン`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 215 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x05E6F8B8` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 22 Att / 0 Dif / 6 Vel / 11 Asp / 20 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `クラウン` | dichiarato dal modello |
| identificativo, segreto | 6180, 58746 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 245, `スイクン` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Purogelo, Eterelama, Extrarapido, Acquanello | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3008, luogo 3008 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3008 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|215\|05E6F8B8\|6180\|58746\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|215\|05E6F8B8\|6180\|58746\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `191859d042ef26b928ed70373710bd3e79126240a3f3e68ae6a7e56c0f0a173d` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 216 Celebi  `えいがかん`

**Insegna えいがかん, luogo 3008.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `えいがかん`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 216 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x078361A4` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Furba | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 25 Att / 16 Dif / 21 Vel / 9 Asp / 8 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `えいがかん` | dichiarato dal modello |
| identificativo, segreto | 7100, 38491 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 251, `セレビィ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Verdebufera, Ripresa, Congiura, Curardore | dichiarate dal modello |
| oggetto tenuto | 211 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3008, luogo 3008 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3008 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|216\|00000001\|7100\|38491\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|216\|00000001\|7100\|38491\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `669c5db367212dce63c4b5a59702d3e0af4b5257c16f1e36cfa329eab27cfa6d` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 217 Scizor  `グーン`

**Insegna グーン, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `グーン`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 217 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0BEE0CD4` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 68 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 21 Att / 14 Dif / 29 Vel / 12 Asp / 4 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `グーン` | dichiarato dal modello |
| identificativo, segreto | 6180, 12346 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 212, `ハッサム` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Forbice X, Danzaspada, Ferroscudo, Agilità | dichiarate dal modello |
| oggetto tenuto | 207 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|217\|0BEE0CD4\|6180\|12346\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|217\|0BEE0CD4\|6180\|12346\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `2568dcd4b772d64972f38b6f121034a1a851e88ef74cb76a6b63dc4342ed7d22` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 219 Pikachu  `サトシ`

**Insegna サトシ, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `サトシ`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 219 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2CE6C9D6` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Birbona | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 12 Att / 22 Dif / 25 Vel / 6 Asp / 18 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `サトシ` | dichiarato dal modello |
| identificativo, segreto | 7150, 50165 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Locomovolt, Codacciaio, Attacco Rapido, Fulmine | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|219\|2CE6C9D6\|7150\|50165\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|219\|2CE6C9D6\|7150\|50165\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `b4811af7536a3e89f27ae4f17a9e3cda80c369648021bdbac1f3918b328b7e54` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 220 Manaphy  `NZ`

**Insegna NZ, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `NZ`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 220 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x04D5919C` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Scaltra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 93 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 23 Att / 21 Dif / 22 Vel / 24 Asp / 23 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `NZ` | dichiarato dal modello |
| identificativo, segreto | 8110, 64718 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 490, `マナフィ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Acquanello, Idropulsar, Docciascudo, Cuorbaratto | dichiarate dal modello |
| oggetto tenuto | 206 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|220\|04D5919C\|8110\|64718\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|220\|04D5919C\|8110\|64718\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `fc4c8b73effb54c289892818e3bc6e6c8f541c03c1bda99fffebd3c4a0dff43c` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 221 Charmander  `トウキョー`

**Insegna トウキョー, luogo 3053.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `トウキョー`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 221 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0F199B50` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 66 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 15 Att / 29 Dif / 2 Vel / 15 Asp / 5 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `トウキョー` | dichiarato dal modello |
| identificativo, segreto | 7200, 58364 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 4, `ヒトカゲ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 40, 56660 | dichiarati dal modello |
| mosse | Ritorno, Introforza, Attacco Rapido, Gridodilotta | dichiarate dal modello |
| oggetto tenuto | 231 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3053, luogo 3053 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3053 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|221\|0F199B50\|7200\|58364\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|221\|0F199B50\|7200\|58364\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `40bf33eeb9dc08d546d53729fa0f337f15bae3e9090e3b3843a43e3a934fc307` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 222 Pikachu  `セブン`

**Insegna セブン, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `セブン`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 222 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1B5F4DC0` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 10 Att / 31 Dif / 21 Vel / 25 Asp / 15 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `セブン` | dichiarato dal modello |
| identificativo, segreto | 8200, 55194 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 20, 8000 | dichiarati dal modello |
| mosse | Regalino, Attacco Rapido, Tuonoshock, Colpocoda | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|222\|1B5F4DC0\|8200\|55194\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|222\|1B5F4DC0\|8200\|55194\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3189a8b6bb3af4744a538e4d85bc6588089e9652ceed4697e07f7b0d88f56dfc` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 223 Chimchar  `ナゴヤ`

**Insegna ナゴヤ, luogo 3056.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ナゴヤ`, la carta è in lingua giapponese, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 223 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x6D3E4E9C` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 66 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 19 Att / 7 Dif / 0 Vel / 1 Asp / 28 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ナゴヤ` | dichiarato dal modello |
| identificativo, segreto | 9120, 11976 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 390, `ヒコザル` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 40, 56660 | dichiarati dal modello |
| mosse | Lanciafiamme, Tuonopugno, Laccioerboso, Altruismo | dichiarate dal modello |
| oggetto tenuto | 231 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3056, luogo 3056 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3056 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|223\|6D3E4E9C\|9120\|11976\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|223\|6D3E4E9C\|9120\|11976\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6834e6951be61390732a57c835568ba1bcea4527569bf6b710d64cbe245696f7` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 224 Pikachu  `ポケトピア`

**Insegna ポケトピア, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ポケトピア`, la carta è in lingua giapponese, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 224 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x19D97C13` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 14 Att / 30 Dif / 15 Vel / 25 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ポケトピア` | dichiarato dal modello |
| identificativo, segreto | 12146, 56585 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 25, `ピカチュウ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | dichiarati dal modello |
| mosse | Locomovolt, Surf, Colpocoda, Tuononda | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|224\|19D97C13\|12146\|56585\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|224\|19D97C13\|12146\|56585\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `0fc761cd9ee3d2bf49aa47e44ba953b76356c604606e939dd0ff3c457bb56f4b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 226 Deoxys  `オブリビア`

**Insegna オブリビア, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `オブリビア`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 226 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xBD6B2B6D` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 30 Att / 12 Dif / 29 Vel / 28 Asp / 31 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `オブリビア` | dichiarato dal modello |
| identificativo, segreto | 3060, 20191 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 386, `デオキシス` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Meteorpugno, Troppoforte, Iper Raggio | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|226\|00000001\|3060\|20191\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|226\|00000001\|3060\|20191\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `fbc9b3c85cddea4636e0460494e55ef77f591a060d98e5194a3a010d5382ac6b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 227 Deoxys  `オブリビア`

**Insegna オブリビア, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `オブリビア`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 227 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x984903D7` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ritrosa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 21 PS / 28 Att / 5 Dif / 30 Vel / 26 Asp / 4 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `オブリビア` | dichiarato dal modello |
| identificativo, segreto | 3060, 10470 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 386, `デオキシス` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Individua, Contrattacco, Specchiovelo | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|227\|00000001\|3060\|10470\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|227\|00000001\|3060\|10470\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6c144e81a38846163a3a863ba557132dce2e65a5e015bf08648477b403abb0c3` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 228 Deoxys  `オブリビア`

**Insegna オブリビア, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `オブリビア`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 228 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x16E2859F` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Calma | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 16 PS / 30 Att / 15 Dif / 5 Vel / 16 Asp / 27 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `オブリビア` | dichiarato dal modello |
| identificativo, segreto | 3060, 55715 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 386, `デオキシス` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Fulmisguardo, Avvolgibotta, Ombra Notturna | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|228\|00000001\|3060\|55715\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|228\|00000001\|3060\|55715\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `d16205777cafacde54072a5b601f0690bc48c3efb5c96dc528a320741a57bfb4` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 229 Deoxys  `オブリビア`

**Insegna オブリビア, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `オブリビア`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 229 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x8ADE4CFB` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 23 Att / 19 Dif / 7 Vel / 22 Asp / 20 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `オブリビア` | dichiarato dal modello |
| identificativo, segreto | 3060, 6159 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 386, `デオキシス` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Comete, Doppioteam, Extrarapido | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|229\|00000001\|3060\|6159\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|229\|00000001\|3060\|6159\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `44539350d9ab87f7ec6655e1b64039ad979e706afc2b491e1fd1436eabe211fa` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 230 Heatran  `オブリビア`

**Insegna オブリビア, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `オブリビア`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 230 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x505E03A0` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 18 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 6 Att / 10 Dif / 25 Vel / 31 Asp / 8 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `オブリビア` | dichiarato dal modello |
| identificativo, segreto | 3060, 63645 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 485, `ヒードラン` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Eruzione, Magmaclisma, Geoforza, Forzantica | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|230\|505E03A0\|3060\|63645\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|230\|505E03A0\|3060\|63645\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f0f9a31bd46b86b495f716a9cc1a07e784cab169155f50c299c43c25380343d3` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 231 Shaymin  `オブリビア`

**Insegna オブリビア, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `オブリビア`, la carta è in lingua giapponese, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 231 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x4FB630E7` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 30 Att / 3 Dif / 3 Vel / 22 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `オブリビア` | dichiarato dal modello |
| identificativo, segreto | 3060, 29324 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | giapponese | dichiarata dal modello |
| specie interna, soprannome | 492, `シェイミ` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Crescita, Fogliamagica, Parassiseme, Sintesi | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|231\|00000001\|3060\|29324\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|231\|00000001\|3060\|29324\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3db323c8dbe5ee32d9adb5293031c1d3dc146d02574e3e2d48d7d9174c44c619` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 232 Darkrai  `한국닌텐도`

**Insegna 한국닌텐도, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `한국닌텐도`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 232 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xC036CE21` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 20 Att / 20 Dif / 29 Vel / 10 Asp / 1 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `한국닌텐도` | dichiarato dal modello |
| identificativo, segreto | 11088, 59899 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 491, `다크라이` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fragortempo, Fendispazio, Incubo, Ipnosi | dichiarate dal modello |
| oggetto tenuto | 208 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|232\|00000001\|11088\|59899\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|232\|00000001\|11088\|59899\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `c6929bafb137634d0234f9929b5aea51562f1455d5b269c5e1efaa9b21567242` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 233 Deoxys  `한국닌텐도`

**Insegna 한국닌텐도, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `한국닌텐도`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 233 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xD47A0618` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 29 PS / 29 Att / 23 Dif / 12 Vel / 10 Asp / 17 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `한국닌텐도` | dichiarato dal modello |
| identificativo, segreto | 8308, 13183 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 386, `테오키스` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Elettrocannone, Ferroscudo, Extrarapido | dichiarate dal modello |
| oggetto tenuto | 202 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|233\|00000001\|8308\|13183\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|233\|00000001\|8308\|13183\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6aa071e72b447a0bfd0f416e6fb8946a548147ce1b2d5ae8cccd8910e390e0aa` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 234 Manaphy  `한국닌텐도`

**Insegna 한국닌텐도, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `한국닌텐도`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 234 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7D569969` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 93 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 11 Att / 31 Dif / 26 Vel / 30 Asp / 29 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `한국닌텐도` | dichiarato dal modello |
| identificativo, segreto | 3298, 52652 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 490, `마나피` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 1, 0 | dichiarati dal modello |
| mosse | Codadiluce, Bolla, Docciascudo | dichiarate dal modello |
| oggetto tenuto | 221 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|234\|00000001\|3298\|52652\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|234\|00000001\|3298\|52652\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `55972e25f8c948f5c56bef13baa6280b7fab097f9dea165692da7ed0c032b0c4` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 235 Rayquaza  `한국닌텐도`

**Insegna 한국닌텐도, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `한국닌텐도`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 235 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0439CB0B` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Calma | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 76 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 28 Att / 3 Dif / 21 Vel / 10 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `한국닌텐도` | dichiarato dal modello |
| identificativo, segreto | 5318, 2526 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 384, `레쿠쟈` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 70, 428750 | dichiarati dal modello |
| mosse | Volo, Extrarapido, Oltraggio, Dragobolide | dichiarate dal modello |
| oggetto tenuto | 235 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|235\|00000001\|5318\|2526\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|235\|00000001\|5318\|2526\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6759426815a461c6f0211d44de1b9f08556516af487a01217b3df76b3ad437b7` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 236 Electivire  `피카츄카페`

**Insegna 피카츄카페, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `피카츄카페`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 236 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1F26A1E8` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 78 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 10 PS / 5 Att / 8 Dif / 13 Vel / 10 Asp / 7 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `피카츄카페` | dichiarato dal modello |
| identificativo, segreto | 6298, 21589 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 466, `에레키블` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Schermoluce, Tuonopugno, Scarica, Fulmine | dichiarate dal modello |
| oggetto tenuto | 242 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|236\|1F26A1E8\|6298\|21589\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|236\|1F26A1E8\|6298\|21589\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `1ae7be4c7857d4566c8d2d00d3f37c6cc2a2f481b03f18aaa3c4ced30ecace27` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 237 Magmortar  `피카츄카페`

**Insegna 피카츄카페, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `피카츄카페`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 237 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1F26A1F5` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 49 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 15 PS / 4 Att / 13 Dif / 29 Vel / 19 Asp / 14 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `피카츄카페` | dichiarato dal modello |
| identificativo, segreto | 6298, 6457 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 467, `마그마번` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Stordiraggio, Fuocopugno, Lavasbuffo, Lanciafiamme | dichiarate dal modello |
| oggetto tenuto | 249 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|237\|1F26A1F5\|6298\|6457\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|237\|1F26A1F5\|6298\|6457\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `255fe6165b219b77974b6fee9ec36b9b1c7a0ee1d216d0e82be79a22d967f4df` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 238 Tangrowth  `피카츄카페`

**Insegna 피카츄카페, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `피카츄카페`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 238 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0BCD9F8E` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Audace | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 102 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 26 PS / 13 Att / 6 Dif / 23 Vel / 0 Asp / 10 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `피카츄카페` | dichiarato dal modello |
| identificativo, segreto | 10038, 61139 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 465, `덩쿠림보` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Giornodisole, Mattindoro, Forzantica, Dononaturale | dichiarate dal modello |
| oggetto tenuto | 204 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|238\|0BCD9F8E\|10038\|61139\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|238\|0BCD9F8E\|10038\|61139\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `7beeceda7013ac49fd63664ebb60b0b065dbe1017b939d9ab9f7554722fcc74b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 239 Mew  `한국닌텐도`

**Insegna 한국닌텐도, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `한국닌텐도`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 239 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xCFBBF06B` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Mite | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 22 PS / 9 Att / 25 Dif / 17 Vel / 0 Asp / 12 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `한국닌텐도` | dichiarato dal modello |
| identificativo, segreto | 3219, 36366 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 151, `뮤` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Metronomo, Psichico, Teletrasporto, Sferapulsar | dichiarate dal modello |
| oggetto tenuto | 203 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|239\|00000001\|3219\|36366\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|239\|00000001\|3219\|36366\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `ce1e9cb0746096c6e34479779332899fb6bf76fe3a2430eeaf06055cbc678077` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 240 Arcanine  `배틀시리즈`

**Insegna 배틀시리즈, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `배틀시리즈`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 240 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x63E77824` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 22 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 13 Att / 16 Dif / 15 Vel / 11 Asp / 14 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `배틀시리즈` | dichiarato dal modello |
| identificativo, segreto | 6069, 55303 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 59, `윈디` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fuococarica, Fulmindenti, Sgranocchio, Extrarapido | dichiarate dal modello |
| oggetto tenuto | 249 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|240\|00000001\|6069\|55303\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|240\|00000001\|6069\|55303\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `bb4ec9dfd685e4b44832dc2870029f7e9d24e851577da06060b43e65904a4b8a` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 241 Regigigas  `한국닌텐도`

**Insegna 한국닌텐도, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `한국닌텐도`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 241 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2D8A6203` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Birbona | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 112 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 1 Att / 9 Dif / 20 Vel / 24 Asp / 3 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `한국닌텐도` | dichiarato dal modello |
| identificativo, segreto | 6209, 15181 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 486, `레지기가스` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Metaltestata, Frana, Ventogelato, Sbriciolmano | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|241\|00000001\|6209\|15181\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|241\|00000001\|6209\|15181\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e82a4932743fe4221701414ad3ee5ace04009de8ccd2302a49e1f909b9f13861` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 242 Munchlax  `신세계`

**Insegna 신세계, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `신세계`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 242 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x15326C17` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 47 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 1 Att / 26 Dif / 10 Vel / 2 Asp / 18 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `신세계` | dichiarato dal modello |
| identificativo, segreto | 7049, 38410 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 446, `먹고자` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Metronomo, Segugio, Azione, Maledizione | dichiarate dal modello |
| oggetto tenuto | 234 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|242\|15326C17\|7049\|38410\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|242\|15326C17\|7049\|38410\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `55729e379d79c6d77f9e48bcc6fc4282b7ef077d45a19fc80962040882eb8af1` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 243 Feebas  `신세계`

**Insegna 신세계, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `신세계`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 243 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2D09EA61` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Calma | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 33 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 31 Att / 30 Dif / 26 Vel / 1 Asp / 8 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `신세계` | dichiarato dal modello |
| identificativo, segreto | 7049, 4277 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 349, `빈티나` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 237 | dichiarati dal modello |
| mosse | Splash, Specchiovelo | dichiarate dal modello |
| oggetto tenuto | 180 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|243\|2D09EA61\|7049\|4277\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|243\|2D09EA61\|7049\|4277\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `14f28df98f67a6c2283d869d4a9f3440e85d1abda3dcedbd452a8cdfd1490010` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 244 Shaymin  `캐릭터페어`

**Insegna 캐릭터페어, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `캐릭터페어`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 244 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1332DF2F` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ingenua | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 0 PS / 24 Att / 13 Dif / 1 Vel / 29 Asp / 27 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `캐릭터페어` | dichiarato dal modello |
| identificativo, segreto | 7249, 58953 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 492, `쉐이미` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Infuriaseme, Aromaterapia, Sostituto, Energipalla | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|244\|00000001\|7249\|58953\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|244\|00000001\|7249\|58953\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `db30677edf93ccf5942594749fb0a353928cea6b83ef7a5ce6286f76e3c6ec31` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 245 Pikachu  `캐릭터페어`

**Insegna 캐릭터페어, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `캐릭터페어`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 245 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2DFEB7BE` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Audace | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 24 Att / 0 Dif / 26 Vel / 15 Asp / 11 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `캐릭터페어` | dichiarato dal modello |
| identificativo, segreto | 7249, 36178 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 25, `피카츄` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Locomovolt, Attacco Rapido, Fulmine, Codacciaio | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|245\|2DFEB7BE\|7249\|36178\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|245\|2DFEB7BE\|7249\|36178\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `7a6b6e2b62dca11e70b338eb0501791eb34ea526f5fb81cb250628502ef9c182` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 248 Pichu  `미케나`

**Insegna 미케나, luogo 3003.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `미케나`, la carta è in lingua coreano, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 248 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x600800D6` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 14 PS / 30 Att / 7 Dif / 21 Vel / 5 Asp / 0 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `미케나` | dichiarato dal modello |
| identificativo, segreto | 12179, 20300 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 172, `피츄` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Sottocarica, Locomovolt, Resistenza, Rimonta | dichiarate dal modello |
| oggetto tenuto | 229 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3003, luogo 3003 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3003 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|248\|600800D6\|12179\|20300\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|248\|600800D6\|12179\|20300\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `0cf6561934e0a0e3cbd613acd61418c6513d026d5d41328f55f26bb00b21a349` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 249 Arceus  `영화관`

**Insegna 영화관, luogo 3003.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `영화관`, la carta è in lingua coreano, e il luogo di incontro dice che via di consegna non riconosciuta.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 249 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x5D112D41` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 121 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 9 Att / 22 Dif / 0 Vel / 25 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `영화관` | dichiarato dal modello |
| identificativo, segreto | 12249, 28562 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 493, `아르세우스` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Giudizio, Fragortempo, Fendispazio, Oscurotuffo | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3003, luogo 3003 | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3003 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|249\|00000001\|12249\|28562\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|249\|00000001\|12249\|28562\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `141629ca9b722245c3a185c2f87d999e52fd7675665249047544384d2008dc6f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 250 Jirachi  `한국닌텐도`

**Insegna 한국닌텐도, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `한국닌텐도`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 250 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xD414070B` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 21 Att / 29 Dif / 31 Vel / 0 Asp / 21 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `한국닌텐도` | dichiarato dal modello |
| identificativo, segreto | 1300, 44886 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 385, `지라치` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo | dichiarate dal modello |
| oggetto tenuto | 201 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|250\|00000001\|1300\|44886\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|250\|00000001\|1300\|44886\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `68ae46299c917ce2a1f07f3df1fa3f63d8c0b06d720c554c152c189d6b259515` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 253 Shaymin  `타임스퀘어`

**Insegna 타임스퀘어, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `타임스퀘어`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 253 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0F79635B` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Docile | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 12 PS / 20 Att / 21 Dif / 8 Vel / 6 Asp / 8 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `타임스퀘어` | dichiarato dal modello |
| identificativo, segreto | 5010, 23655 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 492, `쉐이미` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Crescita, Fogliamagica, Parassiseme, Ritorno | dichiarate dal modello |
| oggetto tenuto | 218 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|253\|00000001\|5010\|23655\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|253\|00000001\|5010\|23655\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `67ad29e90b70c0ff3a1c3dd135c09df8c0a7838a9c97e2640a157b33c85b35f1` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 256 Milotic  `캐릭터페어`

**Insegna 캐릭터페어, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `캐릭터페어`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 256 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x346135A8` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Timida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 63 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 8 Att / 3 Dif / 25 Vel / 31 Asp / 26 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `캐릭터페어` | dichiarato dal modello |
| identificativo, segreto | 7210, 7655 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 350, `밀로틱` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Pioggiadanza, Ripresa, Idropompa, Ventogelato | dichiarate dal modello |
| oggetto tenuto | 273 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|256\|346135A8\|7210\|7655\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|256\|346135A8\|7210\|7655\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `28d7c34e2843d6eeed78e991b9081f820fd04902890f3ac43722ecfc4dc55e20` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 257 Raikou  `크라운시티`

**Insegna 크라운시티, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `크라운시티`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 257 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x1A2C548C` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 9 Att / 31 Dif / 23 Vel / 11 Asp / 29 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `크라운시티` | dichiarato dal modello |
| identificativo, segreto | 9180, 28031 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 243, `라이코` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Elettrocannone, Sferapulsar, Extrarapido, Palla Clima | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|257\|1A2C548C\|9180\|28031\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|257\|1A2C548C\|9180\|28031\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `b7750f5380e5a0b8a3231cc2c036fce18efd2735c1f3c3998964d6ada7ab1162` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 258 Entei  `크라운시티`

**Insegna 크라운시티, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `크라운시티`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 258 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x59DC5E78` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 27 PS / 7 Att / 0 Dif / 4 Vel / 30 Asp / 0 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `크라운시티` | dichiarato dal modello |
| identificativo, segreto | 10300, 12191 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 244, `앤테이` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Fuococarica, Gridodilotta, Extrarapido, Tritartigli | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|258\|59DC5E78\|10300\|12191\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|258\|59DC5E78\|10300\|12191\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `f949554515cb33ccaa0c58d607ab737b59718475b11621b9fa622b546c6d898c` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 259 Entei  `크라운시티`

**Insegna 크라운시티, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `크라운시티`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 259 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x02DAAE36` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 25 Att / 13 Dif / 14 Vel / 3 Asp / 19 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `크라운시티` | dichiarato dal modello |
| identificativo, segreto | 12160, 33647 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 244, `앤테이` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Fuococarica, Gridodilotta, Extrarapido, Tritartigli | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|259\|02DAAE36\|12160\|33647\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|259\|02DAAE36\|12160\|33647\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `8549e781d5a25337b7dc0e97738ba4d672e7ec3815b0ceac610eccee7ca64dc1` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 260 Raikou  `크라운시티`

**Insegna 크라운시티, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `크라운시티`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 260 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x3FABA140` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 4 Att / 1 Dif / 18 Vel / 5 Asp / 14 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `크라운시티` | dichiarato dal modello |
| identificativo, segreto | 12160, 45422 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 243, `라이코` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Elettrocannone, Sferapulsar, Extrarapido, Palla Clima | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|260\|3FABA140\|12160\|45422\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|260\|3FABA140\|12160\|45422\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `6a2e932c4e864d7e4dc24f117d5c4513e9d86f8d903524babbdc3bb052364053` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 261 Suicune  `크라운시티`

**Insegna 크라운시티, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `크라운시티`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 261 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x5BAAA574` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 16 Att / 11 Dif / 28 Vel / 5 Asp / 22 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `크라운시티` | dichiarato dal modello |
| identificativo, segreto | 12160, 53594 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 245, `스이쿤` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Purogelo, Eterelama, Extrarapido, Acquanello | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|261\|5BAAA574\|12160\|53594\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|261\|5BAAA574\|12160\|53594\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `444f5f70aff670c415af7c687a14c899078a1b659ba4413b6d6eeb6711e7280a` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 262 Celebi  `영화관`

**Insegna 영화관, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `영화관`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 262 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xB696D066` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 4 PS / 23 Att / 20 Dif / 23 Vel / 24 Asp / 23 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `영화관` | dichiarato dal modello |
| identificativo, segreto | 12230, 60432 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 251, `세레비` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Verdebufera, Ripresa, Congiura, Curardore | dichiarate dal modello |
| oggetto tenuto | 211 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|262\|00000001\|12230\|60432\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|262\|00000001\|12230\|60432\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `ccaa22912da36e6caeb59afdc70d57ad0d1d69eb23d371ae0ee3c95f873ac6ab` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 263 Scizor  `달건`

**Insegna 달건, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `달건`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 263 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x059BDB9A` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 68 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 0 Att / 23 Dif / 12 Vel / 12 Asp / 29 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `달건` | dichiarato dal modello |
| identificativo, segreto | 1071, 64904 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 212, `핫삼` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Forbice X, Danzaspada, Ferroscudo, Agilità | dichiarate dal modello |
| oggetto tenuto | 207 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|263\|059BDB9A\|1071\|64904\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|263\|059BDB9A\|1071\|64904\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e16ed651a1edae17f4ce316f9c05e8bc5b659174cce4cb58edff28f67de2593e` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 265 Pikachu  `지우`

**Insegna 지우, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `지우`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 265 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x610C74AE` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Birbona | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 18 Att / 14 Dif / 26 Vel / 13 Asp / 13 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `지우` | dichiarato dal modello |
| identificativo, segreto | 2011, 65100 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 25, `피카츄` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Locomovolt, Codacciaio, Attacco Rapido, Fulmine | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|265\|610C74AE\|2011\|65100\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|265\|610C74AE\|2011\|65100\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `e51daac75b784f4e77d802d6ce5ec612aa88255be4786ce74c0c8eebcd40a248` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 266 Manaphy  `포켓몬사랑`

**Insegna 포켓몬사랑, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `포켓몬사랑`, la carta è in lingua coreano, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 266 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x5FEA847A` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Scaltra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 93 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 30 Att / 25 Dif / 23 Vel / 7 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `포켓몬사랑` | dichiarato dal modello |
| identificativo, segreto | 3121, 38778 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | coreano | dichiarata dal modello |
| specie interna, soprannome | 490, `마나피` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Acquanello, Idropulsar, Docciascudo, Cuorbaratto | dichiarate dal modello |
| oggetto tenuto | 206 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|266\|5FEA847A\|3121\|38778\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|266\|5FEA847A\|3121\|38778\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `3fe916a7a9fcd0cca2402f1e3419c44e70f010b021481be290303fc14c94e696` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 267 Darkrai  `ALAMOS`

**Insegna ALAMOS, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `ALAMOS`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 267 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x31F8725D` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ingenua | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 1 Att / 1 Dif / 13 Vel / 26 Asp / 25 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `ALAMOS` | dichiarato dal modello |
| identificativo, segreto | 7038, 20313 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Fragortempo, Fendispazio, Incubo, Ipnosi | dichiarate dal modello |
| oggetto tenuto | 208 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|267\|00000001\|7038\|20313\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|267\|00000001\|7038\|20313\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `ac95701f6dcf3aa7aca6e367181973650337ea7246b0f16805db8e9a1e0b4951` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 268 Shaymin  `Peli11`

**Insegna Peli11, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Peli11`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 268 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xA4AB4119` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Calma | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 6 PS / 2 Att / 13 Dif / 27 Vel / 14 Asp / 0 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Peli11` | dichiarato dal modello |
| identificativo, segreto | 4019, 34011 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Infuriaseme, Aromaterapia, Sostituto, Energipalla | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|268\|00000001\|4019\|34011\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|268\|00000001\|4019\|34011\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `eed49d12f41ce51d3b11aa12596dc8b24f3f57b3e1cf967a7d9963014a96ac17` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 271 Arceus  `MICHINA`

**Insegna MICHINA, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `MICHINA`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 271 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xEDBC606A` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 121 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 18 PS / 21 Att / 20 Dif / 23 Vel / 22 Asp / 10 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `MICHINA` | dichiarato dal modello |
| identificativo, segreto | 2010, 56468 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 493, `ARCEUS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Giudizio, Fragortempo, Fendispazio, Oscurotuffo | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|271\|00000001\|2010\|56468\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|271\|00000001\|2010\|56468\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `bb98b040a4de9b756f9dd4294d9b812edf98521df80483fb9329a7affbe5803a` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 273 Pichu  `PRI2010`

**Insegna PRI2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PRI2010`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 273 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x77D83FE6` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 6 Att / 18 Dif / 28 Vel / 30 Asp / 19 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PRI2010` | dichiarato dal modello |
| identificativo, segreto | 3050, 17366 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 172, `PICHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 27000 | dichiarati dal modello |
| mosse | Sottocarica, Locomovolt, Rimonta, Resistenza | dichiarate dal modello |
| oggetto tenuto | 229 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|273\|77D83FE6\|3050\|17366\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|273\|77D83FE6\|3050\|17366\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `67aa8d89bc4c67e1c5beb6f83687ccd63ca0836444926344076e7e3d4b48d068` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 274 Darkrai  `Almia`

**Insegna Almia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Almia`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 274 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x5EFFA911` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 123 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 30 Att / 11 Dif / 10 Vel / 21 Asp / 25 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Almia` | dichiarato dal modello |
| identificativo, segreto | 3208, 22806 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 491, `DARKRAI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Vuototetro, Neropulsar, Palla Ombra, Doppioteam | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|274\|00000001\|3208\|22806\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|274\|00000001\|3208\|22806\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `81c4c0bc12a416680c1a98b57c3e6b32da1e840788ed71aea0f6c754eb915849` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 275 Riolu  `Kiko`

**Insegna Kiko, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Kiko`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 275 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x06A6D188` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Seria | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 80 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 4 Att / 1 Dif / 24 Vel / 5 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Kiko` | dichiarato dal modello |
| identificativo, segreto | 3208, 23382 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 447, `RIOLU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Sferapulsar, Ombrartigli, Pugnoscarica, Assorbipugno | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|275\|06A6D188\|3208\|23382\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|275\|06A6D188\|3208\|23382\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5314dad0125e60382f8861ea0748f8625e0466337444a3e328fe8706dfd6ebe6` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 276 Jirachi  `VER2010`

**Insegna VER2010, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `VER2010`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 276 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x4F5618A3` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 32 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 9 Att / 15 Dif / 31 Vel / 21 Asp / 9 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `VER2010` | dichiarato dal modello |
| identificativo, segreto | 6260, 30810 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 385, `JIRACHI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 156 | dichiarati dal modello |
| mosse | Desiderio, Confusione, Riposo, Dragobolide | dichiarate dal modello |
| oggetto tenuto | 201 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|276\|00000001\|6260\|30810\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|276\|00000001\|6260\|30810\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `2a1ce5fdc09aeac8416f09953ea273bee1a629a9c17884d20c16851139b9abfd` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 279 Eevee  `VGC10`

**Insegna VGC10, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `VGC10`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 279 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x6EF77993` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 91 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 25 PS / 31 Att / 21 Dif / 3 Vel / 18 Asp / 28 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `VGC10` | dichiarato dal modello |
| identificativo, segreto | 5080, 1211 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 133, `EEVEE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Codacciaio, Asso, Flagello, Attacco Rapido | dichiarate dal modello |
| oggetto tenuto | 275 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|279\|6EF77993\|5080\|1211\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|279\|6EF77993\|5080\|1211\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `89a7c83551a1b8c77e169ffa1864f32eaec837e1cb1e015cde03f610507ae600` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 280 Mew  `OTO2010`

**Insegna OTO2010, Dono Wi-Fi.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `OTO2010`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva sulla rete, dal servizio senza fili della console.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 280 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xA99B2680` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 28 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 20 Att / 20 Dif / 1 Vel / 21 Asp / 7 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `OTO2010` | dichiarato dal modello |
| identificativo, segreto | 10160, 43838 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 151, `MEW` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 5, 135 | dichiarati dal modello |
| mosse | Botta | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3073, Dono Wi-Fi | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3073 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|280\|00000001\|10160\|43838\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|280\|00000001\|10160\|43838\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `c7679ab44080798535dd765f149d5e28b8aecf337ebc4868c007cfb4931bee6b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 282 Raikou  `INV2011`

**Insegna INV2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `INV2011`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 282 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7D5418E2` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardente | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 20 PS / 8 Att / 5 Dif / 11 Vel / 17 Asp / 8 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `INV2011` | dichiarato dal modello |
| identificativo, segreto | 2071, 28071 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 243, `RAIKOU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Elettrocannone, Sferapulsar, Extrarapido, Palla Clima | dichiarate dal modello |
| oggetto tenuto | 209 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|282\|7D5418E2\|2071\|28071\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|282\|7D5418E2\|2071\|28071\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5d3612d7720ce8590caf36a0f31a28ba7e6056378cd84f1fb3874cc2841d2a4b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 283 Entei  `INV2011`

**Insegna INV2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `INV2011`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 283 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x7C382D6C` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 1 PS / 22 Att / 13 Dif / 9 Vel / 19 Asp / 6 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `INV2011` | dichiarato dal modello |
| identificativo, segreto | 2141, 22793 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 244, `ENTEI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Fuococarica, Gridodilotta, Extrarapido, Tritartigli | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|283\|7C382D6C\|2141\|22793\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|283\|7C382D6C\|2141\|22793\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `dfcac9c0c8918754d937298ce29a17c6408d53d90bc1878b3359f7fe8dea6903` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 284 Suicune  `INV2011`

**Insegna INV2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `INV2011`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 284 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x2EC04672` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Placida | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | sì | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 30 PS / 17 Att / 21 Dif / 25 Vel / 14 Asp / 29 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `INV2011` | dichiarato dal modello |
| identificativo, segreto | 2211, 24597 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 245, `SUICUNE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 33750 | dichiarati dal modello |
| mosse | Purogelo, Eterelama, Extrarapido, Acquanello | dichiarate dal modello |
| oggetto tenuto | 212 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 35 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|284\|2EC04672\|2211\|24597\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|284\|2EC04672\|2211\|24597\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `bd576f904b24058ceb62f0fec027c2b62ab6d2548fe67eba360e00d7095ed0b1` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 285 Celebi  `INV2011`

**Insegna INV2011, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `INV2011`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 285 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xDD96908E` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 23 PS / 12 Att / 19 Dif / 16 Vel / 21 Asp / 4 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `INV2011` | dichiarato dal modello |
| identificativo, segreto | 1211, 35349 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 251, `CELEBI` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 117360 | dichiarati dal modello |
| mosse | Verdebufera, Ripresa, Congiura, Curardore | dichiarate dal modello |
| oggetto tenuto | 211 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|285\|00000001\|1211\|35349\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|285\|00000001\|1211\|35349\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `decd3217f5d0230c6f30d1716e502c37b2c58aa59af929aedd517903f22bbfc8` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 286 Pikachu  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua spagnolo, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 286 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x19D97C13` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 9 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 8 PS / 18 Att / 13 Dif / 26 Vel / 0 Asp / 3 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 59606 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 25, `PIKACHU` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 10, 1000 | dichiarati dal modello |
| mosse | Locomovolt, Surf, Colpocoda, Tuononda | dichiarate dal modello |
| oggetto tenuto | 236 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|286\|19D97C13\|12077\|59606\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|286\|19D97C13\|12077\|59606\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `9d57f30131ac58c8500cc4497e33c79dc97277fa96f8a9d098252b677d816f66` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 287 Electivire  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua spagnolo, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 287 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0D7345A6` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Decisa | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 78 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 13 PS / 23 Att / 25 Dif / 26 Vel / 14 Asp / 3 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 23335 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 466, `ELECTIVIRE` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Tuonopugno, Gelopugno, Incrocolpo, Terremoto | dichiarate dal modello |
| oggetto tenuto | 242 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|287\|0D7345A6\|12077\|23335\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|287\|0D7345A6\|12077\|23335\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `fcf026bbebe1ec26506a17d080f416c590f54ca4b144906e13fd076f4bc8bec0` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 288 Magmortar  `PKTOPIA`

**Insegna PKTOPIA, luogo non nominato.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `PKTOPIA`, la carta è in lingua spagnolo, e il luogo di incontro dice che il modello non dichiara alcun luogo, quindi la consegna scrive il primo valore della tabella degli eventi.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 288 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0D71BF12` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Modesta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 49 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 17 PS / 6 Att / 13 Dif / 22 Vel / 31 Asp / 24 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `PKTOPIA` | dichiarato dal modello |
| identificativo, segreto | 12077, 43212 | dichiarati dal modello |
| sesso | femmina | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 467, `MAGMORTAR` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 125000 | dichiarati dal modello |
| mosse | Lanciafiamme, Psichico, Iper Raggio, Solarraggio | dichiarate dal modello |
| oggetto tenuto | 249 | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3000, luogo non nominato | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3000 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 70 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|288\|0D71BF12\|12077\|43212\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|288\|0D71BF12\|12077\|43212\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `79b7976708e0f04761b4ae845d5b1412f1c532cd4c60586e73c8d025fecd10b5` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 289 Regigigas  `EUVER09`

**Insegna EUVER09, Evento Pokémon.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `EUVER09`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna avveniva di persona, all'apparecchio di un negozio o di una manifestazione.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 289 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xC1258183` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 112 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 19 PS / 11 Att / 6 Dif / 16 Vel / 2 Asp / 10 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `EUVER09` | dichiarato dal modello |
| identificativo, segreto | 7189, 38437 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 486, `REGIGIGAS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 100, 1250000 | dichiarati dal modello |
| mosse | Metaltestata, Frana, Ventogelato, Sbriciolmano | dichiarate dal modello |
| oggetto tenuto | 210 | dichiarato dal modello |
| palla | Pregio Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Diamante | dichiarata dal modello |
| luogo di incontro | 3060, Evento Pokémon | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3060 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|289\|00000001\|7189\|38437\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|289\|00000001\|7189\|38437\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `7f8c0cc6458d6874efd1e78c263a91be4bbdbdc48fa5cde22f4fa9bdb9cb165c` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 290 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 290 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xE1E57D36` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Cauta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 14 PS / 6 Att / 17 Dif / 4 Vel / 13 Asp / 22 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 14447 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Meteorpugno, Troppoforte, Iper Raggio | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|290\|00000001\|3060\|14447\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|290\|00000001\|3060\|14447\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `c5d83df66c8f20d387f73f1b98059ea79131147999f7525d9d6f7bdab8a2705b` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 291 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 291 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x68059527` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Audace | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 3 PS / 21 Att / 18 Dif / 25 Vel / 19 Asp / 28 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 57158 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Individua, Contrattacco, Specchiovelo | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|291\|00000001\|3060\|57158\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|291\|00000001\|3060\|57158\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `10e4c7938033733296b0a40d1307b2b40a876ca5316e55ad90213b9a63fd7fc9` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 292 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 292 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xAFFDBDAC` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ingenua | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 7 PS / 29 Att / 11 Dif / 27 Vel / 22 Asp / 13 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 19848 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Fulmisguardo, Avvolgibotta, Ombra Notturna | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|292\|00000001\|3060\|19848\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|292\|00000001\|3060\|19848\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `5aa466576ed0fce05fc3f8074ca5f9c8b0aa06f2ebe05e022702e5d8c74fb67f` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 293 Deoxys  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 293 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0xCCB15D9C` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Ardita | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 46 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 24 PS / 27 Att / 14 Dif / 31 Vel / 18 Asp / 13 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 19282 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 386, `DEOXYS` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Psicoslancio, Comete, Doppioteam, Extrarapido | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 0 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|293\|00000001\|3060\|19282\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|293\|00000001\|3060\|19282\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `20327dc3a3c0a866504f06f17b41a4ce8eaae592e9d4586d3960e360ec3c9247` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 294 Heatran  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 294 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x0A1E9698` | dichiarato dal modello del dono, cioè il valore realmente distribuito |
| natura | Quieta | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 0, numero 18 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 11 PS / 6 Att / 15 Dif / 8 Vel / 9 Asp / 0 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 17615 | dichiarati dal modello |
| sesso | maschio | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 485, `HEATRAN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 50, 156250 | dichiarati dal modello |
| mosse | Eruzione, Magmaclisma, Geoforza, Forzantica | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|294\|0A1E9698\|3060\|17615\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|294\|0A1E9698\|3060\|17615\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `11cf428dbbd9b3fa468fb4971eb8569c27abcee32ca00461d424272cdfd082fd` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

### 295 Shaymin  `Oblivia`

**Insegna Oblivia, Pokémon Ranger.** Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal dato e non da una fonte: l'insegna della distribuzione è `Oblivia`, la carta è in lingua spagnolo, e il luogo di incontro dice che la consegna proveniva da un gioco della serie Ranger, che sbloccava la missione e poi consegnava l'esemplare al gioco principale.

| Campo | Valore | Da dove viene |
|---|---|---|
| posizione nella base dei doni | 295 | l'indice del record nella base dei doni segreti della fonte, che è anche la chiave del seme |
| valore di personalità | `0x57811051` | composto da noi, perché il modello portava il segnale `0x00000001` invece di un valore, cioè l'ordine di generarne uno non cromatico |
| natura | Allegra | resto per venticinque del valore di personalità |
| bit dell'abilità, abilità dichiarata | 1, numero 30 | bit meno significativo del valore di personalità, e numero di abilità che il modello scrive |
| cromatico | no | somma esclusiva delle quattro parole sotto otto |
| valori individuali | 2 PS / 13 Att / 5 Dif / 1 Vel / 31 Asp / 31 Dsp | composti da noi, perché il modello li portava tutti a zero: la console di chi riceveva li tirava al momento della consegna |
| allenatore | `Oblivia` | dichiarato dal modello |
| identificativo, segreto | 3060, 29872 | dichiarati dal modello |
| sesso | asessuato | dichiarato dal modello, e vincolo sulla composizione del valore |
| lingua | spagnolo | dichiarata dal modello |
| specie interna, soprannome | 492, `SHAYMIN` | numero nazionale, nome nella lingua della voce |
| livello, esperienza | 30, 21760 | dichiarati dal modello |
| mosse | Crescita, Fogliamagica, Parassiseme, Sintesi | dichiarate dal modello |
| oggetto tenuto | nessuno | dichiarato dal modello |
| palla | Poké Ball | dichiarata dal modello |
| incontro fatidico | sì | dichiarato dal modello |
| versione di origine | Oro HeartGold | dichiarata dal modello |
| luogo di incontro | 3001, Pokémon Ranger | il luogo che il modello tiene nel campo dell'uovo, spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |
| campo esteso del luogo | 3001 | scritto perché il lotto è composto per essere riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |
| data di incontro | 2026-09-04 | costante dichiarata nel generatore, non il giorno della corsa, perché il lotto deve essere riproducibile |
| cordialità | 100 | valore base della specie, come fa la consegna |
| chiave del seme del valore di personalità | `EVT-4\|295\|00000001\|3060\|29872\|pid` | l'impronta SHA-256 di questa stringa dà i primi quattro byte del seme |
| chiave del seme dei valori individuali | `EVT-4\|295\|00000001\|3060\|29872\|iv` | sale diverso dal precedente, perché la coppia non deve esibire correlazione |
| impronta del file prodotto | `d207b9ed37fcece2bfc43a9e9c59a8c9e4e864b7531bce3b56ff6d551e350d9e` | SHA-256 della forma di scatola scritta in `_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi questa riga è la sola che venga dal disco: è la prova che il file esiste ed è quell'esemplare, non una sua descrizione |

