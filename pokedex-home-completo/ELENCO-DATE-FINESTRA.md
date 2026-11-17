# Date di incontro dei doni da carta rispetto alla finestra dell'evento

> Documento generato da `tools/finestre-eventi.py` dai pedigree e dalle liste di distribuzione di Bulbapedia salvate il 2026-11-07. Non si modifica a mano. I dati per esemplare, con le finestre e le liste abbinate, stanno in `pokedex-home-completo/data/finestre-eventi.json`.

Le righe sono quelle dei pedigree il cui Evento porta il numero di una carta, con gioco d'origine di quinta, sesta o settima generazione: per la terza e la quarta HOME mostra per forza la data di Poké Transfer (`DATE-INCONTRO.md`). Ogni riga si abbina alle schede delle liste per ID e allenatore, anche quando l'esemplare si è evoluto, oppure per specie e livello di incontro quando la carta dà l'allenatore del giocatore; un allenatore «(Various)» vale solo con la stessa specie. Le finestre di tutte le schede abbinate, di ogni regione, valgono insieme.

Le stesse liste dicono quale data è plausibile. In quinta e sesta generazione la data è quella del sistema quando si riceve la carta, quindi deve stare nella finestra. In settima è quella in cui si ritira il dono dal fattorino, quindi può stare dopo la finestra ma non prima. Nel 2026 nessuna di queste carte si riceve più.

## Totali per generazione e classe

| Generazione | dentro | prima | dopo | fra due finestre | scheda senza finestra | senza scheda | totale |
|---|---|---|---|---|---|---|---|
| 5 | 645 | 20 | 85 | 2 | 20 | 27 | 799 |
| 6 | 740 | 23 | 526 | 0 | 0 | 0 | 1289 |
| 7 | 599 | 3 | 552 | 0 | 0 | 38 | 1192 |

## Gruppi di decisione

| Gruppo | Nome | Quinta | Sesta | Settima | Totale | Criterio |
|---|---|---|---|---|---|---|
| A | impossibile per il gioco | 0 | 0 | 0 | 0 | data anteriore all'uscita del gioco d'origine, oppure del 2026 in quinta o sesta generazione, oppure fuori dalle finestre di oltre 60 giorni in quinta e sesta, oppure prima della finestra in settima |
| B | possibile ma fuori dalla finestra | 0 | 0 | 4 | 4 | settima generazione con data successiva alla finestra o del 2026: il dono si può ritirare dal fattorino dopo l'evento |
| C | storica vicina alla finestra | 0 | 0 | 0 | 0 | data di una carta reale a meno di 60 giorni dalle finestre elencate: fuso orario, luogo o giorno non elencati |
| D | storica senza finestra | 0 | 0 | 21 | 21 | data storica senza una scheda o una finestra abbinata |
| E | dentro la finestra | 799 | 860 | 600 | 2259 | nessuna azione: data di incontro dentro la finestra, oppure, secondo `tools/pkhex-ridata`, data dell'uovo dentro la finestra o data di ricezione reale della stessa distribuzione |
| F | sostituito | 0 | 429 | 567 | 996 | esemplare già rigenerato con la data dentro la finestra nelle copie RIDATA (ADR-126), da liberare in HOME secondo l'elenco da liberare di `python tools/elenco-da-liberare.py --stampa` |

Box e posto sono quelli della copia del gruppo. L'etichetta di HOME è un'inferenza da verificare su un esemplare: i conteggi delle etichette «Bank N» sono compatibili con un'etichetta per box di Bank, cioè per box della copia.

## Gruppo A, impossibile per il gioco

Esemplari: 0.

| Gruppo | Box | Posto | Etichetta presunta | Specie | Cromatico | Lingua | Allenatore | ID | Data | Finestre |
|---|---|---|---|---|---|---|---|---|---|---|

## Gruppo B, possibile ma fuori dalla finestra

Esemplari: 4.

| Gruppo | Box | Posto | Etichetta presunta | Specie | Cromatico | Lingua | Allenatore | ID | Data | Finestre |
|---|---|---|---|---|---|---|---|---|---|---|
| HOME5 | 19 | 13 | Bank 19 | 25 Pikachu |  | Japanese | サトシ | 170715 | 2017-12-30 | 2017-08-01, 2017-08-28; 2017-08-22, 2017-09-03 |
| RIDATA2 | 1 | 19 | Bank 1 | 747 Mareanie |  | Italian | Elio | 123456 | 2017-05-10 | 2017-03-18, 2017-04-09; 2017-04-29, 2017-05-07 |
| RIDATA2 | 1 | 21 | Bank 1 | 766 Passimian |  | Italian | Elio | 123456 | 2017-05-09 | 2017-03-18, 2017-04-09; 2017-04-29, 2017-05-07 |
| RIDATA2 | 14 | 19 | Bank 14 | 776 Turtonator |  | Italian | Elio | 123456 | 2017-05-10 | 2017-03-18, 2017-04-09; 2017-04-29, 2017-05-07 |

## Gruppo C, storica vicina alla finestra

Esemplari: 0.

| Gruppo | Box | Posto | Etichetta presunta | Specie | Cromatico | Lingua | Allenatore | ID | Data | Finestre |
|---|---|---|---|---|---|---|---|---|---|---|

## Gruppo D, storica senza finestra

Esemplari: 21.

| Gruppo | Box | Posto | Etichetta presunta | Specie | Cromatico | Lingua | Allenatore | ID | Data | Finestre |
|---|---|---|---|---|---|---|---|---|---|---|
| HOME5 | 18 | 11 | Bank 18 | 25 Pikachu |  | English | Ash | 170715 | 2017-12-30 | nessuna |
| HOME5 | 18 | 19 | Bank 18 | 25 Pikachu |  | French | Sacha | 170715 | 2017-12-30 | nessuna |
| HOME5 | 18 | 27 | Bank 18 | 25 Pikachu |  | German | Ash | 170715 | 2017-12-30 | nessuna |
| HOME5 | 19 | 5 | Bank 19 | 25 Pikachu |  | Italian | Ash | 170715 | 2017-12-30 | nessuna |
| HOME5 | 19 | 29 | Bank 19 | 25 Pikachu |  | Spanish | Ash | 170715 | 2017-12-30 | nessuna |
| RIDATA2 | 1 | 1 | Bank 1 | 801 Magearna |  | Italian | Alessio | 878221 | 2017-11-14 | nessuna |
| RIDATA2 | 2 | 4 | Bank 2 | 801 Magearna |  | Italian | Elio | 771063 | 2018-05-09 | nessuna |
| RIDATA2 | 13 | 22 | Bank 13 | 55 Golduck |  | Japanese | ルイ | 180609 | 2018-06-09 | nessuna |
| RIDATA2 | 19 | 5 | Bank 19 | 25 Pikachu |  | ChineseS | Satoshi | 170715 | 2018-06-02 | nessuna |
| RIDATA2 | 19 | 6 | Bank 19 | 801 Magearna |  | Italian | Elio | 771063 | 2018-06-28 | nessuna |
| RIDATA2 | 19 | 7 | Bank 19 | 25 Pikachu |  | ChineseT | Satoshi | 170715 | 2018-07-15 | nessuna |
| RIDATA2 | 19 | 8 | Bank 19 | 801 Magearna |  | Italian | Elio | 771063 | 2018-07-09 | nessuna |
| RIDATA2 | 19 | 9 | Bank 19 | 801 Magearna |  | Italian | Elio | 771063 | 2018-03-07 | nessuna |
| RIDATA2 | 19 | 10 | Bank 19 | 801 Magearna |  | Italian | Elio | 771063 | 2018-03-06 | nessuna |
| RIDATA2 | 19 | 11 | Bank 19 | 801 Magearna |  | Italian | Elio | 771063 | 2018-08-31 | nessuna |
| RIDATA2 | 19 | 12 | Bank 19 | 801 Magearna |  | Italian | Elio | 771063 | 2018-03-31 | nessuna |
| RIDATA2 | 19 | 13 | Bank 19 | 801 Magearna |  | Italian | Elio | 771063 | 2018-04-09 | nessuna |
| RIDATA2 | 19 | 14 | Bank 19 | 801 Magearna |  | Italian | Elio | 771063 | 2018-04-25 | nessuna |
| RIDATA2 | 19 | 17 | Bank 19 | 801 Magearna |  | Italian | Alessio | 878221 | 2017-12-07 | nessuna |
| RIDATA2 | 19 | 18 | Bank 19 | 801 Magearna |  | Italian | Alessio | 878221 | 2017-03-07 | nessuna |
| RIDATA2 | 19 | 23 | Bank 19 | 801 Magearna |  | Italian | Alessio | 878221 | 2018-10-11 | nessuna |
