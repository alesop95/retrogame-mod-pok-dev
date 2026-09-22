# Il piano dei box, e la verifica del catalogo delle squadre

> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_valida_squadre.py` a partire da `gba-save-extraction-smeraldo/squadre-parco-lotta.json`. Non si modifica a mano: si modifica il catalogo e si rigenera. Il ragionamento che giustifica ogni scelta sta in `STUDIO-05`.

## L'esito della verifica

Problemi bloccanti: 0. Avvisi: 1.

- avviso: heracross-jolly: Megahorn si impara al livello 53, oltre il tetto di 50 che la modalita' cinquanta impone all'ISCRIZIONE: l'esemplare va quindi ottenuto da due genitori che la conoscono entrambi, secondo la regola di BuildEggMoveset, e non alzando il proprio livello

Che cosa e' stato controllato: le dieci specie escluse da ogni struttura, l'unicita' della specie e dello strumento dentro ciascuna squadra, l'assenza di strumenti alla Piramide Lotta, l'assenza di mosse di stato al Palazzo Lotta, il divieto delle mosse che il criterio di giudizio del Dojo Lotta penalizza, e l'esistenza di ogni chiave citata. In piu', per ogni esemplare, che ciascuna mossa sia imparabile dalla propria specie e per quale via, sulla tabella estratta dal sorgente del gioco. Una mossa che richieda un livello oltre il tetto di cinquanta non e' un errore ma una catena di riproduzione da dichiarare, e compare fra gli avvisi.

## Quanti esemplari servono, e quanto spazio

Esemplari distinti da generare: **15**, cioe' 8 impiegati dalle squadre piu' 7 di riserva, che per decisione dell'utente si generano subito insieme agli altri invece di restare sulla carta. Copie per esemplare: 2, perche' una delle due e' destinata a uno scambio gia' concordato. Slot dei box necessari: **30**, cioe' 1 box da 30 su quattordici disponibili.

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

| Esemplare | Specie | Natura | Ruolo |
|---|---|---|---|
| gengar-timid | Gengar | Timid | riserva, si genera ma non entra in alcuna squadra iniziale |
| heracross-jolly | Heracross | Jolly | riserva, si genera ma non entra in alcuna squadra iniziale |
| milotic-bold | Milotic | Bold | riserva, si genera ma non entra in alcuna squadra iniziale |
| salamence-adamant | Salamence | Adamant | riserva, si genera ma non entra in alcuna squadra iniziale |
| snorlax-careful | Snorlax | Careful | riserva, si genera ma non entra in alcuna squadra iniziale |
| starmie-timid | Starmie | Timid | riserva, si genera ma non entra in alcuna squadra iniziale |
| suicune-bold | Suicune | Bold | riserva, si genera ma non entra in alcuna squadra iniziale |

Le riserve esistono per una ragione operativa e non per completezza: quando una squadra si rompe sul campo, la correzione e' la sostituzione di un esemplare, e averla gia' nella cartuccia significa riprovare la sera stessa invece di aprire una corsa di generazione. Il loro insieme di mosse resta pero' provvisorio, perche' e' stato deciso senza sapere contro che cosa serviranno.

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

I primi dieci giri bastano al simbolo d'oro e vengono dalla guida. Gli altri dieci servono solo a chi punta a una serie lunga oltre i settanta piani, nessuna fonte li copre, e sono calcolati: sui dieci noti il calcolo indica un esemplare che la guida impiega davvero in sette casi su dieci e il conduttore esatto in quattro su dieci.

| Giro | Tema del bestiario | Primo in campo | Cambio | Da dove viene |
|---|---|---|---|---|
| 1 | mosse che paralizzano | Latios | nessuno | guida |
| 2 | mosse che avvelenano | Latios | nessuno | guida |
| 3 | mosse che scottano | Latios | nessuno | guida |
| 4 | consumo dei punti potere | Metagross | nessuno | guida |
| 5 | abilita' Levitazione | Metagross | Latios dal quarto piano | guida |
| 6 | abilita' che intrappolano | Metagross | Latios dal quarto piano | guida |
| 7 | tipo Ghiaccio | Metagross | Latios dal quinto piano | guida |
| 8 | Autodistruzione ed Esplosione | Latios | Swampert dal quarto piano | guida |
| 9 | tipo Psico | Latios | Metagross dal secondo piano | guida |
| 10 | tipo Roccia | Swampert | Metagross dal terzo piano | guida |
| 11 | tipo Lotta | Latios | nessuno | calcolato, da verificare sul campo |
| 12 | mosse che cambiano il tempo | Latios | nessuno | calcolato, da verificare sul campo |
| 13 | tipo Coleottero | Metagross | nessuno | calcolato, da verificare sul campo |
| 14 | tipo Buio | Metagross | nessuno | calcolato, da verificare sul campo |
| 15 | tipo Acqua | Latios | nessuno | calcolato, da verificare sul campo |
| 16 | tipo Spettro | Metagross | nessuno | calcolato, da verificare sul campo |
| 17 | tipo Acciaio | Swampert | nessuno | calcolato, da verificare sul campo |
| 18 | tipi Volante e Drago | Latios | nessuno | calcolato, da verificare sul campo |
| 19 | evoluzioni da pietra, con fuoco acqua ed elettricita' | Swampert | nessuno | calcolato, da verificare sul campo |
| 20 | tipo Normale che conosce Iper Raggio | Metagross | nessuno | calcolato, da verificare sul campo |

