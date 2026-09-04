# Ottenibilità nei titoli a via diretta

> Documento generato da `tools/ottenibilita-titoli.py`. Non si modifica a mano: si rigenera. La fonte sono le tabelle degli incontri, delle statistiche e delle evoluzioni di PKHeX, lette dal clone passato sulla riga di comando.

Questo documento sostituisce una risposta che il progetto dava da giorni e che era un limite inferiore travestito da risultato. La domanda è quali specie la chiusura della banca porti via, e fino al 2026-09-04 la risposta veniva dal contrassegno di presenza delle tabelle delle statistiche, cioè dall'affermazione che una specie esiste nei dati di un gioco. La presenza però non è l'ottenibilità: un gioco moderno porta i dati di una specie anche soltanto perché il deposito gliela possa mandare, e quella specie si può allenare e mostrare ma non prendere. Contarla fra le raggiungibili per via diretta significa dichiarare raggiungibile senza banca qualcosa che per entrare in quel gioco dalla banca deve passare.

Qui la presenza è sostituita dall'incontro. Per ciascun titolo si leggono le tabelle dei luoghi selvatici, degli incontri fissi, dei doni, degli scambi interni e delle incursioni, e se ne ricava l'insieme delle specie che quel gioco sa consegnare da sé. L'insieme viene poi chiuso rispetto alle evoluzioni del titolo, nei due versi: in avanti perché chi prende un Bulbasaur ottiene anche Venusaur senza che alcuna tabella lo dichiari, e all'indietro perché dalla riproduzione si ottiene la forma base di una linea, che è il modo in cui si prendono i cuccioli che nessuno incontra. La chiusura si ferma su ciò che il titolo dichiara presente, poiché un'evoluzione verso una specie che il gioco non conosce non avviene.

## Il conto per titolo

| Sigla | Titolo | Presenti nei dati | Con un incontro | Ottenibili dopo la chiusura |
|---|---|---|---|---|
| LGPE | Let's Go Pikachu ed Eevee | 809 | 165 | 225 |
| SwSh | Spada e Scudo | 664 | 630 | 651 |
| BDSP | Diamante Lucente e Perla Splendente | 493 | 325 | 489 |
| PLA | Leggende Arceus | 242 | 242 | 242 |
| SV | Scarlatto e Violetto | 733 | 664 | 698 |
| Z-A | Leggende Z-A | 377 | 357 | 365 |

A questi si aggiungono le 130 specie consegnate come dono nelle generazioni che parlano al deposito direttamente, cioè l'ottava, la nona e i due titoli di Let's Go. Vanno contate, e la ragione va detta perché il primo tentativo di questa misura le aveva dimenticate: un dono non è un incontro e nessuna tabella degli incontri lo dichiara, ma un esemplare consegnato in quelle generazioni arriva al deposito senza toccare la banca. Che la distribuzione sia chiusa da anni lo rende difficile da procurarsi, non lo rende vincolato dalla scadenza, e le due cose non si confondono.

L'unione delle specie presenti nei dati dei sei titoli è 1025 su 1025, ed è il numero da cui veniva il risultato vecchio. L'unione delle specie ottenibili in gioco è 1021, e con i doni a via diretta sale a 1025. La differenza fra la presenza e l'ottenibilità è 0: sono le specie che esistono nei dati di un gioco moderno senza che quel gioco le sappia consegnare in alcun modo.

## Le specie che la scadenza vincola davvero

Sono 0, e sono quelle che nessun titolo a via diretta sa consegnare da sé: per arrivare al deposito devono passare dalla banca, quindi entro il 26 febbraio 2027 o mai più.

Nessuna. Il risultato precedente regge anche alla misura severa, e ora è un risultato misurato invece di un limite inferiore: la differenza non è nel numero ma in ciò che il numero significa.

## Le specie che nessun gioco moderno sa far prendere

Sono 4, e sono il risultato nuovo di questa misura. Non sono vincolate dalla scadenza, perché il dono che le consegna sta in una generazione che parla al deposito direttamente; ma non hanno alcun incontro in alcuno dei sei titoli, quindi l'unica via per averle è un esemplare da distribuzione. Stanno cioè sull'asse degli eventi e non su quello delle specie, e chi pianificasse di prenderle giocando perderebbe il proprio tempo.

| Dex | Specie |
|---|---|
| 251 | Celebi |
| 386 | Deoxys |
| 494 | Victini |
| 893 | Zarude |

## Il verso dell'errore, e come stringere il limite

Questa misura sbaglia in due modi opposti, e vanno detti entrambi perché una prima stesura dichiarava soltanto il primo e concludeva che l'errore fosse tutto prudente. Non lo è.

Il primo verso è prudente. Le tabelle lette sono molte ma non tutte, e dove una fonte non è letta la specie che solo quella consegnerebbe risulta non ottenibile: si finisce per dichiarare vincolata dalla scadenza una specie che invece si prende, cioè si lavora su qualcosa che non serviva. Su una scadenza è il rischio accettabile.

Il secondo verso non lo è. Gli incontri scritti in codice si leggono con una regola generosa, che accetta sia le righe con la specie dichiarata per nome di campo sia quelle il cui costruttore comincia con un numero, perché le tabelle usano entrambe le forme e nessuna copre l'altra. Una lettura generosa può raccogliere un numero che specie non è, e allora una specie risulterebbe ottenibile senza esserlo: quella si perderebbe per sempre. Il presidio non è automatico ma è una verifica fatta a mano il 2026-09-04 sulle cinquanta specie che soltanto quella lettura aggiunge, con sei campionate fra le più sospette, cioè i mitici Keldeo, Genesect, Marshadow, Zeraora, Mew e Manaphy: tutte e sei venivano da righe di incontro vere, in Leggende Z-A le prime quattro, in Diamante Lucente Mew e in Leggende Arceus Manaphy. Chi tocchi quella regola rifaccia il campione.

Il primo verso si stringe aggiungendo tabelle, e quelle lette per ciascun titolo sono elencate qui sotto perché si veda che cosa manchi.

| Sigla | Tabelle lette | Tabelle dichiarate e non trovate |
|---|---|---|
| LGPE | `Gen7/encounter_gp.pkl`, `Gen7/encounter_ge.pkl`, `Gen7/Encounters7GG.cs` | nessuna |
| SwSh | `Gen8/encounter_sw_symbol.pkl`, `Gen8/encounter_sh_symbol.pkl`, `Gen8/encounter_sw_hidden.pkl`, `Gen8/encounter_sh_hidden.pkl`, `Gen8/encounter_sw_dist.pkl`, `Gen8/encounter_sh_dist.pkl`, `Gen8/encounter_sw_nest.pkl`, `Gen8/encounter_sh_nest.pkl`, `Gen8/encounter_swsh_underground.pkl`, `Gen8/Encounters8.cs`, `Gen8/Encounters8Nest.cs` | nessuna |
| BDSP | `Gen8/encounter_bd.pkl`, `Gen8/encounter_sp.pkl`, `Gen8/encounter_bd_underground.pkl`, `Gen8/encounter_sp_underground.pkl`, `Gen8/Encounters8b.cs` | nessuna |
| PLA | `Gen8/encounter_la.pkl`, `Gen8/Encounters8a.cs` | nessuna |
| SV | `Gen9/encounter_wild_paldea.pkl`, `Gen9/encounter_dist_paldea.pkl`, `Gen9/encounter_might_paldea.pkl`, `Gen9/encounter_fixed_paldea.pkl`, `Gen9/encounter_outbreak_paldea.pkl`, `Gen9/encounter_gem_paldea.pkl`, `Gen9/encounter_gem_kitakami.pkl`, `Gen9/encounter_gem_blueberry.pkl`, `Gen9/Encounters9.cs` | nessuna |
| Z-A | `Gen9/encounter_za.pkl`, `Gen9/encounter_hyperspace_za.pkl`, `Gen9/Encounters9a.cs` | nessuna |

