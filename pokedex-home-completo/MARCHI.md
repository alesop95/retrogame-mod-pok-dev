# L'asse dei marchi: enumerazione, famiglie e rapporto con la scadenza

> Documento generato da `tools/marchi.py`. Non si modifica a mano: si rigenera. Le posizioni dei bit sono lette dal formato del deposito e non trascritte, per la ragione già pagata due volte da questo progetto su tabelle lunghe.

Il formato del deposito dichiara 53 marchi distinti, distribuiti su 8 byte dell'esemplare. Un marchio non è un fiocco, e la differenza è di significato e non di rappresentazione, perché i due vivono nella stessa regione di byte e chi guarda i byte non vede alcun confine: un fiocco si conferisce per un merito, cioè per qualcosa che il giocatore ha fatto e che può rifare, mentre un marchio si conferisce per una circostanza dell'incontro, cioè per qualcosa che era vero nel momento in cui l'esemplare è stato trovato.

Va detto subito ciò che questa misura non dice, perché è la domanda che verrà subito dopo. Non dice quante voci di collezione l'asse produca: un marchio non si moltiplica per le specie, si misura, come il progetto ha già stabilito per i cromatici e per le sfere. Un marchio meteorologico è comune e si riottiene aspettando il tempo giusto; quello del titano appartiene a sei incontri e basta; quello del più forte appartiene a una lista di edizioni chiuse che va contata sulla fonte e non dedotta dal bit.

## Il rapporto con la scadenza, che è il risultato principale

Nessun marchio è sotto la scadenza del 26 febbraio 2027, e la ragione è strutturale invece che fortunata: i marchi nascono con l'ottava generazione e vivono nell'ottava e nella nona, che sono titoli per console corrente e parlano al deposito per via diretta. La chiusura della banca non tocca alcuna via che li conferisca. L'asse allarga quindi l'ampiezza della collezione e non la sua urgenza, e va pianificato dopo ciò che scade.

Ne discende anche il verso opposto, e va enunciato perché è il difetto tipico di un asse nuovo: la copertura di questo asse sui nostri lotti non è zero, è indefinita. I lotti arrivano alla quinta generazione, dove queste posizioni non esistono e i medesimi byte appartengono ad altri campi, quindi puntarvele contro non darebbe una misura bassa ma una misura priva di senso. La prima stesura di questo programma lo ha fatto e ha riferito quattordicimila marchi accesi su millequattrocentottantasette esemplari, che è esattamente il genere di numero plausibile e sbagliato contro cui il resto del programma è scritto. La colonna della copertura conta perciò soltanto file del formato del deposito, e in loro assenza riporta zero esemplari esaminati.

## Le famiglie

| Famiglia | Marchi | Di cui dell'insieme della nona |
|---|---|---|
| momento del giorno | 4 | 0 |
| tempo atmosferico | 8 | 0 |
| modo della cattura | 6 | 3 |
| rarità dell'incontro | 5 | 3 |
| taglia dell'esemplare | 2 | 2 |
| indole dell'esemplare | 28 | 0 |
| totale | 53 | 8 |

## L'elenco, con la posizione nel formato del deposito

La colonna dell'insieme dice se il marchio appartenga a quello che il verificatore della nona generazione tratta a parte, cioè i marchi nati dopo Spada e Scudo, oppure all'insieme originario. La colonna della copertura conta gli esemplari dei nostri lotti che lo portano, su 0 esaminati.

| Marchio | Chiave | Byte | Bit | Famiglia | Insieme | Nei lotti |
|---|---|---|---|---|---|---|
| Lunchtime Mark | RibbonMarkLunchtime | 0x36 | 5 | momento del giorno | ottava | 0 |
| Sleepy-Time Mark | RibbonMarkSleepyTime | 0x36 | 6 | momento del giorno | ottava | 0 |
| Dusk Mark | RibbonMarkDusk | 0x36 | 7 | momento del giorno | ottava | 0 |
| Dawn Mark | RibbonMarkDawn | 0x37 | 0 | momento del giorno | ottava | 0 |
| Cloudy Mark | RibbonMarkCloudy | 0x37 | 1 | tempo atmosferico | ottava | 0 |
| Rainy Mark | RibbonMarkRainy | 0x37 | 2 | tempo atmosferico | ottava | 0 |
| Stormy Mark | RibbonMarkStormy | 0x37 | 3 | tempo atmosferico | ottava | 0 |
| Snowy Mark | RibbonMarkSnowy | 0x37 | 4 | tempo atmosferico | ottava | 0 |
| Blizzard Mark | RibbonMarkBlizzard | 0x37 | 5 | tempo atmosferico | ottava | 0 |
| Dry Mark | RibbonMarkDry | 0x37 | 6 | tempo atmosferico | ottava | 0 |
| Sandstorm Mark | RibbonMarkSandstorm | 0x37 | 7 | tempo atmosferico | ottava | 0 |
| Misty Mark | RibbonMarkMisty | 0x3A | 0 | tempo atmosferico | ottava | 0 |
| Destiny Mark | RibbonMarkDestiny | 0x3A | 1 | modo della cattura | ottava | 0 |
| Fishing Mark | RibbonMarkFishing | 0x3A | 2 | modo della cattura | ottava | 0 |
| Curry Mark | RibbonMarkCurry | 0x3A | 3 | modo della cattura | ottava | 0 |
| Uncommon Mark | RibbonMarkUncommon | 0x3A | 4 | rarità dell'incontro | ottava | 0 |
| Rare Mark | RibbonMarkRare | 0x3A | 5 | rarità dell'incontro | ottava | 0 |
| Rowdy Mark | RibbonMarkRowdy | 0x3A | 6 | indole dell'esemplare | ottava | 0 |
| Absent-Minded Mark | RibbonMarkAbsentMinded | 0x3A | 7 | indole dell'esemplare | ottava | 0 |
| Jittery Mark | RibbonMarkJittery | 0x3B | 0 | indole dell'esemplare | ottava | 0 |
| Excited Mark | RibbonMarkExcited | 0x3B | 1 | indole dell'esemplare | ottava | 0 |
| Charismatic Mark | RibbonMarkCharismatic | 0x3B | 2 | indole dell'esemplare | ottava | 0 |
| Calmness Mark | RibbonMarkCalmness | 0x3B | 3 | indole dell'esemplare | ottava | 0 |
| Intense Mark | RibbonMarkIntense | 0x3B | 4 | indole dell'esemplare | ottava | 0 |
| Zoned-Out Mark | RibbonMarkZonedOut | 0x3B | 5 | indole dell'esemplare | ottava | 0 |
| Joyful Mark | RibbonMarkJoyful | 0x3B | 6 | indole dell'esemplare | ottava | 0 |
| Angry Mark | RibbonMarkAngry | 0x3B | 7 | indole dell'esemplare | ottava | 0 |
| Smiley Mark | RibbonMarkSmiley | 0x3C | 0 | indole dell'esemplare | ottava | 0 |
| Teary Mark | RibbonMarkTeary | 0x3C | 1 | indole dell'esemplare | ottava | 0 |
| Upbeat Mark | RibbonMarkUpbeat | 0x3C | 2 | indole dell'esemplare | ottava | 0 |
| Peeved Mark | RibbonMarkPeeved | 0x3C | 3 | indole dell'esemplare | ottava | 0 |
| Intellectual Mark | RibbonMarkIntellectual | 0x3C | 4 | indole dell'esemplare | ottava | 0 |
| Ferocious Mark | RibbonMarkFerocious | 0x3C | 5 | indole dell'esemplare | ottava | 0 |
| Crafty Mark | RibbonMarkCrafty | 0x3C | 6 | indole dell'esemplare | ottava | 0 |
| Scowling Mark | RibbonMarkScowling | 0x3C | 7 | indole dell'esemplare | ottava | 0 |
| Kindly Mark | RibbonMarkKindly | 0x3D | 0 | indole dell'esemplare | ottava | 0 |
| Flustered Mark | RibbonMarkFlustered | 0x3D | 1 | indole dell'esemplare | ottava | 0 |
| Pumped-Up Mark | RibbonMarkPumpedUp | 0x3D | 2 | indole dell'esemplare | ottava | 0 |
| Zero Energy Mark | RibbonMarkZeroEnergy | 0x3D | 3 | indole dell'esemplare | ottava | 0 |
| Prideful Mark | RibbonMarkPrideful | 0x3D | 4 | indole dell'esemplare | ottava | 0 |
| Unsure Mark | RibbonMarkUnsure | 0x3D | 5 | indole dell'esemplare | ottava | 0 |
| Humble Mark | RibbonMarkHumble | 0x3D | 6 | indole dell'esemplare | ottava | 0 |
| Thorny Mark | RibbonMarkThorny | 0x3D | 7 | indole dell'esemplare | ottava | 0 |
| Vigor Mark | RibbonMarkVigor | 0x3E | 0 | indole dell'esemplare | ottava | 0 |
| Slump Mark | RibbonMarkSlump | 0x3E | 1 | indole dell'esemplare | ottava | 0 |
| Jumbo Mark | RibbonMarkJumbo | 0x3E | 5 | taglia dell'esemplare | nona | 0 |
| Mini Mark | RibbonMarkMini | 0x3E | 6 | taglia dell'esemplare | nona | 0 |
| Itemfinder Mark | RibbonMarkItemfinder | 0x3E | 7 | modo della cattura | nona | 0 |
| Partner Mark | RibbonMarkPartner | 0x3F | 0 | modo della cattura | nona | 0 |
| Gourmand Mark | RibbonMarkGourmand | 0x3F | 1 | modo della cattura | nona | 0 |
| Alpha Mark | RibbonMarkAlpha | 0x3F | 3 | rarità dell'incontro | nona | 0 |
| Mightiest Mark | RibbonMarkMightiest | 0x3F | 4 | rarità dell'incontro | nona | 0 |
| Titan Mark | RibbonMarkTitan | 0x3F | 5 | rarità dell'incontro | nona | 0 |

## Che cosa resta da misurare, e su quale fonte

Il marchio del titano appartiene a sei incontri dichiarati da Serebii, cioè Klawf, Bombirdier, Orthworm, la coppia fra Great Tusk e Iron Treads secondo la versione, e Tatsugiri, tutti con altezza e peso al massimo e trenta in ogni valore individuale. Il marchio del più forte appartiene invece agli incontri a cristallo nero, che sulla stessa fonte contano novantuno edizioni di cui una parte non lo conferisce: il conto esatto va fatto sulla pagina e non stimato, ed è lavoro dichiarato in `pending.md`.

Resta infine da chiarire una cosa che nessuna delle due fonti dice e che riguarda il deposito, cioè se un marchio sopravviva al passaggio attraverso il deposito in entrambi i versi. Per il timbro della banca il progetto ha già una tensione aperta sulla rimozione permanente all'uscita, e la pagina dei titoli di Pokemon Champions ne aggiunge una seconda, perché dichiara che un esemplare che vi guadagni il titolo di rango non torna indietro attraverso il deposito.

