# Date di incontro degli esemplari dei lotti per HOME

> Documento generato da `tools/controlla-date-incontro.py` a partire dai pedigree di `pokedex-home-completo/pedigree/`. Non si modifica a mano: si rilancia lo strumento dopo ogni rigenerazione dei pedigree, e `--check` dice se il file è allineato.

La data di incontro è un campo dell'esemplare e HOME la mostra così com'è nella scheda e nel calendario delle catture. Per i doni di sesta e settima generazione la sceglie PKHeX quando costruisce l'esemplare dalla carta: `WC6.ConvertToPKM` e `WC7.ConvertToPKM` scrivono la data della carta, e la base dei doni della libreria ne ha di due tipi. Le carte complete del server ufficiale non portano una data, e `WC6Full` e `WC7Full` danno loro il giorno in cui la libreria gira, cioè quello di produzione del lotto. Le carte estratte dai salvataggi dei giocatori portano la data in cui quel giocatore le ha ricevute, che in quattro casi è anteriore all'uscita di X e Y perché l'orologio della console era sbagliato. Il giudizio di PKHeX non confronta la data con l'uscita del gioco, quindi nessun controllo del progetto l'aveva vista prima del 2026-11-16.

Le classi, nell'ordine in cui si assegnano: *impossibile* è una data anteriore all'uscita giapponese del gioco d'origine; *anteriore alla finestra* è una data anteriore di oltre 60 giorni alla finestra dell'evento che la colonna Storia attribuisce all'esemplare da Serebii, e siccome quell'abbinamento è euristico è un caso da verificare e non un errore; *produzione* è una data del 2026; *storica* è ogni altra data.

## Totali

| Classe | Esemplari |
|---|---|
| impossibile | 20 |
| anteriore-finestra | 21 |
| produzione | 5509 |
| storica | 3116 |
| totale | 8666 |

## Per gruppo

| Gruppo | Stato | impossibile | anteriore-finestra | produzione | storica |
|---|---|---|---|---|---|
| DIAMANTE1 | in HOME | 0 | 0 | 0 | 245 |
| FINALE | in copia | 0 | 0 | 121 | 0 |
| GIAPPONE | in copia | 0 | 0 | 14 | 0 |
| GIAPPONE2 | in HOME | 0 | 0 | 23 | 0 |
| GIRO17 | in HOME | 0 | 0 | 314 | 351 |
| HOME1 | in HOME | 0 | 3 | 863 | 64 |
| HOME10 | in HOME | 0 | 0 | 380 | 0 |
| HOME2 | in HOME | 1 | 3 | 127 | 590 |
| HOME3 | in HOME | 3 | 3 | 612 | 297 |
| HOME4 | in HOME | 1 | 0 | 89 | 3 |
| HOME5 | in HOME | 8 | 2 | 545 | 58 |
| HOME6 | in HOME | 1 | 0 | 920 | 8 |
| HOME7 | in HOME | 2 | 0 | 640 | 0 |
| HOME8 | in HOME | 4 | 0 | 165 | 87 |
| HOME9 | in HOME | 0 | 0 | 694 | 1 |
| RIDATA1 | in HOME | 0 | 7 | 1 | 422 |
| RIDATA2 | in HOME | 0 | 3 | 1 | 564 |
| VERDEFOGLIA1 | in HOME | 0 | 0 | 0 | 359 |
| ZAFFIRO1 | in HOME | 0 | 0 | 0 | 67 |

## I doni da carta, per generazione d'origine

In HOME la data di un esemplare di terza o quarta generazione non è mai quella originale. La terza generazione non ha un campo per la data: la data nasce al Parco Amici con il giorno della migrazione (`PK3.ConvertToPK4` di PKHeX). Poké Transfer, dalla quarta alla quinta generazione, sostituisce la data con il giorno del trasferimento (Bulbapedia, «Poké Transfer», e Project Pokémon, estratti di ricerca del 2026-11-16 in `SOURCES.md`), e quella data passa invariata alle generazioni successive e a HOME. La data più vecchia che HOME può mostrare per quelle due generazioni è quindi l'uscita di Nero e Bianco, il 2010-09-18. La prima e la seconda generazione prendono il giorno del Pokétrasporto. Per la quinta e la sesta generazione la data è quella del sistema quando si riceve la carta, per la settima quella in cui il dono si ritira dal fattorino: lo dicono le liste di distribuzione di Bulbapedia salvate il 2026-11-07, e il confronto con le finestre sta in `ELENCO-DATE-FINESTRA.md`.

Una data dentro la finestra dell'evento si può quindi chiedere soltanto ai doni da carta di quinta, sesta e settima generazione, ed è obbligata per la quinta e la sesta. La tabella conta le righe dei pedigree il cui Evento porta il numero di una carta, rispetto alla finestra che Serebii dà nella colonna Storia, senza tolleranza; *senza finestra* vuol dire che la colonna non ne riporta una, quindi la finestra va cercata in un'altra fonte.

| Generazione | dentro la finestra | prima della finestra | dopo la finestra, data storica | dopo la finestra, giorno di produzione | senza finestra, data storica | senza finestra, giorno di produzione | totale |
|---|---|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 193 | 0 | 48 | 241 |
| 5 | 396 | 22 | 21 | 0 | 288 | 72 | 799 |
| 6 | 447 | 29 | 90 | 315 | 201 | 207 | 1289 |
| 7 | 150 | 13 | 77 | 235 | 401 | 316 | 1192 |

## Casi

Box e posto sono quelli della copia del gruppo, non quelli di HOME, dove gli esemplari si ritrovano per specie, allenatore e data.

| Classe | Gruppo | Box | Posto | Specie | Evento | Gioco d'origine | Data | Allenatore | Motivo |
|---|---|---|---|---|---|---|---|---|---|
| impossibile | HOME2 | 23 | 14 | 710 Pumpkaboo | Boo! A Pumpkaboo! (carta 523) | Y | 2003-10-19 | Spooky2014, ID 10014, SID 523 | anteriore all'uscita di Y (2013-10-12); sostituito in RIDATA1, box 2, posto 5, data 2014-10-24 (ADR-126) |
| impossibile | HOME3 | 13 | 18 | 384 Rayquaza | A special shiny Rayquaza! (carta 119) | Y | 2011-07-04 | Nintendo HK, ID 9115, SID 119 | anteriore all'uscita di Y (2013-10-12); sostituito in RIDATA1, box 14, posto 13, data 2015-10-29 (ADR-126) |
| impossibile | HOME3 | 20 | 2 | 493 Arceus | アルセウス プレゼント (carta 81) | Y | 2011-01-12 | デセルシティ, ID 3075, SID 81 | anteriore all'uscita di Y (2013-10-12); sostituito in RIDATA1, box 14, posto 14, data 2015-03-07 (ADR-126) |
| impossibile | HOME3 | 25 | 18 | 374 Beldum | ¡Un Beldum variocolor! (carta 1504) | Y | 2011-01-21 | Máximo, ID 11214, SID 1504 | anteriore all'uscita di Y (2013-10-12); sostituito in RIDATA1, box 14, posto 15, data 2014-12-12 (ADR-126) |
| impossibile | HOME4 | 2 | 3 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Elio, ID 771063, SID 1749 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 2, posto 4, data 2018-05-09 (ADR-126) |
| impossibile | HOME5 | 18 | 2 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Elio, ID 771063, SID 1749 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 19, posto 6, data 2018-06-28 (ADR-126) |
| impossibile | HOME5 | 18 | 10 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Elio, ID 771063, SID 1749 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 19, posto 8, data 2018-07-09 (ADR-126) |
| impossibile | HOME5 | 18 | 18 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Elio, ID 771063, SID 1749 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 19, posto 9, data 2018-03-07 (ADR-126) |
| impossibile | HOME5 | 18 | 26 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Elio, ID 771063, SID 1749 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 19, posto 10, data 2018-03-06 (ADR-126) |
| impossibile | HOME5 | 19 | 4 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Elio, ID 771063, SID 1749 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 19, posto 11, data 2018-08-31 (ADR-126) |
| impossibile | HOME5 | 19 | 12 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Elio, ID 771063, SID 1749 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 19, posto 12, data 2018-03-31 (ADR-126) |
| impossibile | HOME5 | 19 | 20 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Elio, ID 771063, SID 1749 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 19, posto 13, data 2018-04-09 (ADR-126) |
| impossibile | HOME5 | 19 | 28 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Elio, ID 771063, SID 1749 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 19, posto 14, data 2018-04-25 (ADR-126) |
| impossibile | HOME6 | 16 | 17 | 711 Gourgeist | Boo! A Pumpkaboo! (carta 523) | Rubino Omega | 2003-10-19 | Spooky2014, ID 10014, SID 523 | anteriore all'uscita di Rubino Omega (2014-11-21); sostituito in RIDATA1, box 14, posto 21, data 2014-10-18 (ADR-126) |
| impossibile | HOME7 | 2 | 11 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Alessio, ID 878221, SID 3811 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 19, posto 17, data 2017-12-07 (ADR-126) |
| impossibile | HOME7 | 7 | 9 | 801 Magearna | evento (WC7) | Ultrasole | 2016-11-26 | Alessio, ID 878221, SID 3811 | anteriore all'uscita di Ultrasole (2017-11-17); sostituito in RIDATA2, box 19, posto 23, data 2018-10-11 (ADR-126) |
| impossibile | HOME8 | 2 | 10 | 214 Heracross | WCS2014 기념! 헤라크로스를 선물! (carta 1006) | Rubino Omega | 2014-07-06 | WCS14K, ID 7064, SID 1006 | anteriore all'uscita di Rubino Omega (2014-11-21); sostituito in RIDATA1, box 14, posto 24, data 2014-07-06 (ADR-126) |
| impossibile | HOME8 | 2 | 16 | 229 Houndoom | WCS2014 기념! 헬가를 선물! (carta 1013) | Rubino Omega | 2014-07-06 | WCS14K, ID 7064, SID 1013 | anteriore all'uscita di Rubino Omega (2014-11-21); sostituito in RIDATA1, box 14, posto 25, data 2014-07-06 (ADR-126) |
| impossibile | HOME8 | 2 | 30 | 306 Aggron | WCS2014 기념! 보스로라를 선물! (carta 1014) | Rubino Omega | 2014-07-06 | WCS14K, ID 7064, SID 1014 | anteriore all'uscita di Rubino Omega (2014-11-21); sostituito in RIDATA1, box 14, posto 26, data 2014-07-06 (ADR-126) |
| impossibile | HOME8 | 8 | 6 | 493 Arceus | アルセウス プレゼント (carta 81) | Rubino Omega | 2011-01-12 | デセルシティ, ID 3075, SID 81 | anteriore all'uscita di Rubino Omega (2014-11-21); sostituito in RIDATA1, box 15, posto 9, data 2015-12-02 (ADR-126) |
| anteriore-finestra | HOME1 | 29 | 30 | 494 Victini | Virtuoso Victini! (carta 32) | Bianco | 2011-12-03 | Movie14, ID 12031, SID 0 | finestra Serebii 2012-06-12, 2012-06-26 |
| anteriore-finestra | HOME1 | 31 | 7 | 246 Larvitar | Préparez-vous à des combats épiques! (carta 61) | Bianco | 2012-03-17 | VGC12, ID 3032, SID 0 | finestra Serebii 2012-06-29, 2012-07-01 |
| anteriore-finestra | HOME1 | 31 | 29 | 246 Larvitar | Freue dich auf großartige Kämpfe! (carta 61) | Bianco | 2012-03-10 | VGC12, ID 3032, SID 0 | finestra Serebii 2012-06-29, 2012-07-01 |
| anteriore-finestra | HOME2 | 1 | 21 | 246 Larvitar | Ti aspettano delle grandi lotte! (carta 61) | Bianco | 2012-04-01 | VGC12, ID 3032, SID 0 | finestra Serebii 2012-06-29, 2012-07-01 |
| anteriore-finestra | HOME2 | 15 | 26 | 386 Deoxys | デオキシス プレゼント (carta 126) | Bianco 2 | 2012-12-15 | マスダ, ID 12152, SID 0 | finestra Serebii 2013-03-20, 2013-05-06 |
| anteriore-finestra | HOME2 | 21 | 17 | 246 Larvitar | ¡Te aguardan grandes combates! (carta 61) | Bianco | 2012-03-24 | VGC12, ID 3032, SID 0 | finestra Serebii 2012-06-29, 2012-07-01 |
| anteriore-finestra | HOME3 | 20 | 30 | 248 Tyranitar | チャンピオンの バンギラス (carta 130) | X | 2014-11-17 | ヤミらみこ, ID 3866, SID 130 | finestra Serebii 2015-11-06, 2015-12-07 |
| anteriore-finestra | HOME3 | 25 | 19 | 497 Serperior | Ecco Serperior! (carta 1505) | Y | 2014-01-31 | Regalo, ID 1225, SID 1505 | finestra Serebii 2015-01-21, 2015-11-30 |
| anteriore-finestra | HOME3 | 25 | 20 | 500 Emboar | Ecco Emboar! (carta 1506) | Y | 2014-01-31 | Regalo, ID 1295, SID 1506 | finestra Serebii 2015-01-29, 2015-11-30 |
| anteriore-finestra | HOME5 | 17 | 28 | 25 Pikachu | evento (WC7) | Ultrasole | 2017-12-30 | Satoshi, ID 170715, SID 2039 | finestra Serebii 2018-04-15, 2018-07-31; sostituito in RIDATA2, box 19, posto 5, data 2018-06-02 (ADR-126) |
| anteriore-finestra | HOME5 | 18 | 3 | 25 Pikachu | evento (WC7) | Ultrasole | 2017-12-30 | Satoshi, ID 170715, SID 2039 | finestra Serebii 2018-04-15, 2018-07-31; sostituito in RIDATA2, box 19, posto 7, data 2018-07-15 (ADR-126) |
| anteriore-finestra | RIDATA1 | 1 | 12 | 720 Hoopa | Wow! It's a Hoopa! (carta 553) | Y | 2015-10-13 | Harry, ID 10235, SID 553 | finestra Serebii 2016-04-06, 2016-04-30 |
| anteriore-finestra | RIDATA1 | 1 | 27 | 666 Vivillon | ボールのもようの ビビヨン (carta 36) | Y | 2014-08-22 | ポケセン, ID 8014, SID 36 | finestra Serebii 2016-05-01, 2016-05-31 |
| anteriore-finestra | RIDATA1 | 3 | 27 | 720 Hoopa | Wow! It's a Hoopa! (carta 553) | Y | 2015-12-10 | Harry, ID 10235, SID 553 | finestra Serebii 2016-04-06, 2016-04-30 |
| anteriore-finestra | RIDATA1 | 5 | 14 | 720 Hoopa | Wow! It's a Hoopa! (carta 553) | Y | 2016-01-31 | Harry, ID 10235, SID 553 | finestra Serebii 2016-04-06, 2016-04-30 |
| anteriore-finestra | RIDATA1 | 6 | 21 | 720 Hoopa | Wow! It's a Hoopa! (carta 553) | Y | 2015-11-24 | Harry, ID 10235, SID 553 | finestra Serebii 2016-04-06, 2016-04-30 |
| anteriore-finestra | RIDATA1 | 8 | 30 | 196 Espeon | おたんじょうび おめでとう！ (carta 48) | Y | 2014-02-10 | ポケセン♪, ID 10014, SID 48 | finestra Serebii 2014-10-01, 2015-09-30 |
| anteriore-finestra | RIDATA1 | 9 | 4 | 470 Leafeon | おたんじょうび おめでとう！ (carta 48) | Y | 2014-04-16 | ポケセン♪, ID 10014, SID 48 | finestra Serebii 2014-10-01, 2015-09-30 |
| anteriore-finestra | RIDATA2 | 2 | 9 | 807 Zeraora | Zero in on Zeraora! (carta 668) | Ultrasole | 2018-10-24 | Fula City, ID 100118, SID 668 | finestra Serebii 2019-05-03, 2019-05-26 |
| anteriore-finestra | RIDATA2 | 2 | 12 | 25 Pikachu | Satoshi's Pikachu (Original Cap) (carta 271) | Luna | 2017-11-09 | Satoshi, ID 970401, SID 271 | finestra Serebii 2018-04-15, 2018-07-31 |
| anteriore-finestra | RIDATA2 | 8 | 19 | 807 Zeraora | Zero in on Zeraora! (carta 668) | Ultrasole | 2018-12-04 | Fula City, ID 100118, SID 668 | finestra Serebii 2019-05-03, 2019-05-26 |
