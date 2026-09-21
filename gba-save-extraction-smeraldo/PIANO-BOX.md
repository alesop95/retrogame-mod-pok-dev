# Il piano dei box, e la verifica del catalogo delle squadre

> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_valida_squadre.py` a partire da `gba-save-extraction-smeraldo/squadre-parco-lotta.json`. Non si modifica a mano: si modifica il catalogo e si rigenera. Il ragionamento che giustifica ogni scelta sta in `STUDIO-05`.

## L'esito della verifica

Problemi bloccanti: 0. Avvisi: 0.

- nessun rilievo

Che cosa e' stato controllato: le dieci specie escluse da ogni struttura, l'unicita' della specie e dello strumento dentro ciascuna squadra, l'assenza di strumenti alla Piramide Lotta, l'assenza di mosse di stato al Palazzo Lotta, l'esistenza di ogni chiave citata, e il livello reale minimo imposto dalle mosse che si imparano oltre il cinquanta. Che cosa non e' stato controllato, e va saputo: se ciascuna mossa sia imparabile dalla propria specie, perche' la tabella degli insiemi di mosse non e' ancora su disco in questo progetto e dichiararlo fatto sarebbe peggio che non farlo.

## Quanti esemplari servono, e quanto spazio

Esemplari distinti da generare: 8. Copie per esemplare: 2, perche' una delle due e' destinata a uno scambio gia' concordato. Slot dei box necessari: **16**, cioe' 1 box da 30 su quattordici disponibili.

| Esemplare | Specie | Natura | Edifici in cui entra |
|---|---|---|---|
| blissey-bold | Blissey | Bold | Serpe Lotta |
| latios-hasty | Latios | Hasty | Palazzo Lotta |
| latios-timid | Latios | Timid | Cupola Lotta, Dojo Lotta, Piramide Lotta, Serpe Lotta, Torre Lotta |
| metagross-adamant | Metagross | Adamant | Cupola Lotta, Dojo Lotta, Piramide Lotta, Serpe Lotta, Torre Lotta |
| metagross-sassy | Metagross | Sassy | Palazzo Lotta |
| slaking-adamant | Slaking | Adamant | Cupola Lotta |
| swampert-brave | Swampert | Brave | Palazzo Lotta |
| swampert-relaxed | Swampert | Relaxed | Dojo Lotta, Piramide Lotta, Torre Lotta |

## Le squadre, edificio per edificio, nell'ordine di attacco

### 1. Cupola Lotta

i suoi avversari hanno tre punti individuali su ogni statistica a qualunque punto della serie, per il difetto verificato in src/battle_dome.c; si vede inoltre la squadra avversaria prima di scegliere quali due dei tre mandare in campo

| Esemplare | Strumento | Natura | Mosse |
|---|---|---|---|
| Latios | Lum Berry | Timid | Calm Mind, Psychic, Dragon Claw, Thunderbolt |
| Metagross | Leftovers | Adamant | Meteor Mash, Earthquake, Shadow Ball, Explosion |
| Slaking | Choice Band | Adamant | Return, Earthquake, Shadow Ball, Hyper Beam |

### 2. Azienda Lotta

non si porta alcuna squadra, si combatte con esemplari in prestito; va pero' affrontata prima di costruire una serie lunga alla Torre Lotta, perche' i punti individuali dei suoi avversari dipendono da quella

Nessuna squadra da iscrivere.

### 3. Torre Lotta

e' il calendario piu' lungo del Parco insieme a quello della Piramide, e non aggiunge alcuna regola ai vincoli generali

| Esemplare | Strumento | Natura | Mosse |
|---|---|---|---|
| Latios | Lum Berry | Timid | Calm Mind, Psychic, Dragon Claw, Thunderbolt |
| Swampert | Leftovers | Relaxed | Earthquake, Surf, Ice Beam, Counter |
| Metagross | Choice Band | Adamant | Meteor Mash, Earthquake, Shadow Ball, Explosion |

### 4. Dojo Lotta

stessi tre esemplari della Torre: il criterio di giudizio premia le mosse che infliggono danno e penalizza Protezione, Individua e Resistenza, che questa squadra non porta

| Esemplare | Strumento | Natura | Mosse |
|---|---|---|---|
| Latios | Lum Berry | Timid | Calm Mind, Psychic, Dragon Claw, Thunderbolt |
| Metagross | Choice Band | Adamant | Meteor Mash, Earthquake, Shadow Ball, Explosion |
| Swampert | Leftovers | Relaxed | Earthquake, Surf, Ice Beam, Counter |

### 5. Palazzo Lotta

e' la sola squadra con nature diverse, perche' al Palazzo la natura sceglie le mosse; e porta sole mosse d'attacco per la ragione della sezione 12 di STUDIO-04

| Esemplare | Strumento | Natura | Mosse |
|---|---|---|---|
| Metagross | Choice Band | Sassy | Meteor Mash, Earthquake |
| Latios | Lum Berry | Hasty | Psychic, Dragon Claw, Thunderbolt, Surf |
| Swampert | Leftovers | Brave | Earthquake, Surf, Ice Beam, Rock Slide |

### 6. Serpe Lotta

Metagross e' di tipo Acciaio e quindi immune all'iperavvelenamento, che e' l'alterazione piu' probabile della stanza di stato con il trentacinque per cento

| Esemplare | Strumento | Natura | Mosse |
|---|---|---|---|
| Latios | Lum Berry | Timid | Calm Mind, Psychic, Dragon Claw, Thunderbolt |
| Metagross | Choice Band | Adamant | Meteor Mash, Earthquake, Shadow Ball, Explosion |
| Blissey | Leftovers | Bold | Seismic Toss, Toxic, Soft-Boiled, Sing |

### 7. Piramide Lotta

nessun esemplare entra tenendo uno strumento, perche' il gioco glieli toglie all'ingresso; i dieci giri non richiedono dieci squadre ma dieci ordini di conduzione della stessa, secondo la guida al completamento

| Esemplare | Strumento | Natura | Mosse |
|---|---|---|---|
| Latios | nessuno | Timid | Calm Mind, Psychic, Dragon Claw, Thunderbolt |
| Swampert | nessuno | Relaxed | Earthquake, Surf, Ice Beam, Protect |
| Metagross | nessuno | Adamant | Meteor Mash, Earthquake, Shadow Ball, Brick Break |

I dieci giri non chiedono dieci squadre ma dieci ordini di conduzione della stessa.

| Giro | Tema del bestiario | Primo in campo | Cambio |
|---|---|---|---|
| 1 | mosse che paralizzano | Latios | nessuno |
| 2 | mosse che avvelenano | Latios | nessuno |
| 3 | mosse che scottano | Latios | nessuno |
| 4 | consumo dei punti potere | Metagross | nessuno |
| 5 | abilita' Levitazione | Metagross | Latios dal quarto piano |
| 6 | abilita' che intrappolano | Metagross | Latios dal quarto piano |
| 7 | tipo Ghiaccio | Metagross | Latios dal quinto piano |
| 8 | Autodistruzione ed Esplosione | Latios | Swampert dal quarto piano |
| 9 | tipo Psico | Latios | Metagross dal secondo piano |
| 10 | tipo Roccia | Swampert | Metagross dal terzo piano |

