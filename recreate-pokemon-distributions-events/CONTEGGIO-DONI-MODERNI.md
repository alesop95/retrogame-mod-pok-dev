# Conteggio dei doni segreti dalla quarta alla nona generazione

> Documento generato da `tools/conteggio-doni-moderni.py`. Non si modifica a mano. Conta le voci della base dati dei doni segreti che la fonte porta come file binari, e non le specie: le due grandezze differiscono di molto, perché la stessa distribuzione compare come voce distinta per ogni regione e ogni lingua in cui fu fatta. Il censimento delle specie è il passo successivo e non è ancora fatto.

| Gen | Titoli | File | Voci | Sotto scadenza | Lunghezza del record |
|---|---|---|---|---|---|
| 4 | Diamante, Perla, Platino, HeartGold e SoulSilver | `wc4.pkl` | 590 | sì | PCD.Size |
| 5 | Bianco, Nero e i loro seguiti | `pgf.pkl` | 709 | sì | PGF.Size piu' il byte di restrizione |
| 6 | X, Y, Rubino Omega e Zaffiro Alpha | `wc6full.pkl`, `wc6.pkl` | 836 | sì | WC6Full.Size e WC6.Size |
| 7 | Sole, Luna, UltraSole e UltraLuna | `wc7full.pkl`, `wc7.pkl` | 937 | sì | WC7Full.Size e WC7.Size |
| 7 | Let's Go Pikachu ed Eevee | `wb7full.pkl` | 16 | no | WB7.Size |
| 8 | Spada e Scudo | `wc8.pkl` | 949 | no | WC8.Size |
| 8 | Leggende Arceus | `wa8.pkl` | 19 | no | WA8.Size |
| 8 | Diamante Lucente e Perla Splendente | `wb8.pkl` | 18 | no | WB8.Size |
| 9 | Scarlatto e Violetto | `wc9.pkl` | 228 | no | WC9.Size |
| 9 | Leggende Z-A | `wa9.pkl` | 16 | no | WA9.Size |

Le voci sotto scadenza, cioè quelle delle generazioni che per arrivare al deposito dipendono dalla banca, sono 3072. Quelle senza scadenza, cioè l'ottava, la nona e i due titoli di Let's Go, che parlano al deposito direttamente, sono 1246. Il totale è 4318.

Il confronto con la terza generazione dice l'ordine di grandezza del problema che resta: quella generazione ha centosettantasette voci di catalogo e le ha richieste settimane di studio, perché la sua tabella vive nel codice e il suo generatore pseudocasuale andava ricostruito. Le quattro generazioni sotto scadenza che la seguono ne hanno 3072, cioè quasi venti volte tanto, e non richiedono alcuna ricostruzione: la fonte porta ciascun dono come record binario e il lavoro è di conteggio, catalogazione e misura della campagna. Ne segue che il vincolo su queste generazioni non è la conoscenza ma il tempo di trasferimento, ed è la ragione per cui il numero da misurare per primo resta il tasso del primo anello della catena.

## Prima e seconda generazione

Nella medesima cartella la fonte tiene `event1.pkl`, di 88 byte, `event2.pkl`, di 1884 byte. Non sono doni segreti, che in quelle generazioni non esistevano: sono le tabelle degli esemplari da evento allora distribuiti, e il loro formato non è una serie di record di lunghezza fissa, quindi questo programma ne riferisce l'esistenza e la dimensione senza contarle. Servono al progetto perché la via da quelle generazioni al deposito esiste e passa dalla banca, quindi condivide la scadenza.

