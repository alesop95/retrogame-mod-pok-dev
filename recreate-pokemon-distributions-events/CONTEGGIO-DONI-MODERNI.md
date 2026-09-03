# Conteggio dei doni segreti dalla quarta alla nona generazione

> Documento generato da `tools/conteggio-doni-moderni.py`. Non si modifica a mano. Conta le voci della base dati dei doni segreti che la fonte porta come file binari, e dal 2026-09-03 anche le specie che quelle voci portano. Le due grandezze differiscono di molto, perché la stessa distribuzione compare come voce distinta per ogni regione e ogni lingua in cui fu fatta, e perché le generazioni distribuirono in gran parte le medesime specie: il conto delle voci misura il lavoro di trasferimento, quello delle specie distinte misura il contributo alla collezione, e i due non si confondono.

| Gen | Titoli | File | Voci | Esemplari | Specie distinte | Voci specie e forma | Sotto scadenza | Lunghezza del record |
|---|---|---|---|---|---|---|---|---|
| 4 | Diamante, Perla, Platino, HeartGold e SoulSilver | `wc4.pkl` | 590 | 247 | 43 | 43 | sì | PCD.Size |
| 5 | Bianco, Nero e i loro seguiti | `pgf.pkl` | 709 | 700 | 98 | 98 | sì | PGF.Size piu' il byte di restrizione |
| 6 | X, Y, Rubino Omega e Zaffiro Alpha | `wc6full.pkl`, `wc6.pkl` | 836 | 787 | 129 | 145 | sì | WC6Full.Size e WC6.Size |
| 7 | Sole, Luna, UltraSole e UltraLuna | `wc7full.pkl`, `wc7.pkl` | 937 | 611 | 99 | 106 | sì | WC7Full.Size e WC7.Size |
| 7 | Let's Go Pikachu ed Eevee | `wb7full.pkl` | 16 | 15 | 9 | 9 | no | WB7.Size |
| 8 | Spada e Scudo | `wc8.pkl` | 949 | non letti | non letti | non letti | no | WC8.Size |
| 8 | Leggende Arceus | `wa8.pkl` | 19 | non letti | non letti | non letti | no | WA8.Size |
| 8 | Diamante Lucente e Perla Splendente | `wb8.pkl` | 18 | non letti | non letti | non letti | no | WB8.Size |
| 9 | Scarlatto e Violetto | `wc9.pkl` | 228 | non letti | non letti | non letti | no | WC9.Size |
| 9 | Leggende Z-A | `wa9.pkl` | 16 | non letti | non letti | non letti | no | WA9.Size |

Le celle che dicono non letti non sono zeri, e la distinzione è la stessa che questo progetto ha già pagato altrove: uno zero non misurato e uno zero misurato hanno lo stesso aspetto e significato opposto. Le famiglie di cui non si sanno ancora leggere i campi sono Spada e Scudo, Leggende Arceus, Diamante Lucente e Perla Splendente, Scarlatto e Violetto, Leggende Z-A, e sono tutte senza scadenza, quindi la loro assenza non tocca alcun conto sotto scadenza.

Le specie distinte portate dai doni sotto scadenza sono 252, quelle portate dai doni senza scadenza 9, e la loro unione 257. La somma dei conti per generazione vale invece 378, e il confronto fra quella somma e l'unione misura quanto la sovrapposizione pesi: le generazioni distribuirono in gran parte le medesime specie, e sommare i conti per generazione produrrebbe un numero privo di significato. È lo stesso motivo per cui questo progetto ha dovuto passare dal contare al censire.

Le voci sotto scadenza, cioè quelle delle generazioni che per arrivare al deposito dipendono dalla banca, sono 3072. Quelle senza scadenza, cioè l'ottava, la nona e i due titoli di Let's Go, che parlano al deposito direttamente, sono 1246. Il totale è 4318.

Il confronto con la terza generazione dice l'ordine di grandezza del problema che resta: quella generazione ha centosettantasette voci di catalogo e le ha richieste settimane di studio, perché la sua tabella vive nel codice e il suo generatore pseudocasuale andava ricostruito. Le quattro generazioni sotto scadenza che la seguono ne hanno 3072, cioè quasi venti volte tanto, e non richiedono alcuna ricostruzione: la fonte porta ciascun dono come record binario e il lavoro è di conteggio, catalogazione e misura della campagna. Ne segue che il vincolo su queste generazioni non è la conoscenza ma il tempo di trasferimento, ed è la ragione per cui il numero da misurare per primo resta il tasso del primo anello della catena.

## Prima e seconda generazione

Nella medesima cartella la fonte tiene le tabelle degli esemplari da evento di prima e seconda generazione. Non sono doni segreti, che in quelle generazioni non esistevano: sono tabelle di incontro, e fino al 2026-09-02 questo programma ne riferiva soltanto l'esistenza e la dimensione. Il 2026-09-03 il loro formato è stato letto ed è il più semplice di tutti, cioè record di lunghezza fissa con i campi in chiaro, otto byte in prima generazione e dodici in seconda, che portano specie, livello, quattro mosse, restrizione di lingua e tipo di allenatore.

| File | Byte | Voci | Esemplari | Specie distinte |
|---|---|---|---|---|
| `event1.pkl` | 88 | 11 | 11 | 10 |
| `event2.pkl` | 1884 | 157 | 157 | 107 |

Le specie distinte fra le due generazioni sono 109. Ne discende il fatto che per la roadmap vale più di qualunque conteggio: in quelle generazioni non esiste alcun valore di personalità e non esiste alcun generatore pseudocasuale da ricostruire, perché natura, sesso e caratteristiche non derivano da un seme. Produrre un esemplare da evento di prima o seconda generazione significa dunque scrivere la struttura con i campi che la tabella dichiara, che è esattamente ciò che `pokebridge` sa già fare e ha verificato su prove proprie. Fra le sei generazioni con eventi sotto scadenza, queste due sono le meno costose e non le più costose, contro ogni intuizione.

