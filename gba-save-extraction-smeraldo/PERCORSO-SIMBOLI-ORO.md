# Il percorso ai sette simboli d'oro, edificio per edificio e posizione per posizione

> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_percorso_oro.py` dal catalogo `squadre-parco-lotta.json`, dal calendario di `src/frontier_util.c` registrato in STUDIO-04 sezione 5, dal glossario delle mosse e dal dump di PKHeX del sesto giro per i nomi italiani degli strumenti. Non si modifica a mano: si rigenera.
>
> Le posizioni nei box sono quelle di DOPO il riordino di ADR-074, che non e' ancora avvenuto: oggi i sessantaquattro esemplari esistono soltanto come file. Tutte le sfide sono nella modalita' Livello 50. La copia 1 di ogni esemplare si usa, la copia 2 accanto e' quella per lo scambio.

## L'ordine degli edifici

L'ordine viene dai difetti del gioco e non dal gusto, ed e' spiegato in STUDIO-05 sezione 1: prima la Cupola, poi l'Azienda, che va chiusa prima di allungare la serie alla Torre, poi Torre, Dojo, Palazzo, Serpe e Piramide. L'Azienda si puo' giocare subito, perche' non chiede nulla dal PC.

## 1. Cupola Lotta, Simbolo Tattica

Torneo a eliminazione di sedici, quattro incontri per torneo, due contro due: si iscrivono tre esemplari e prima di ogni incontro, vista la squadra avversaria, se ne scelgono due. Gli avversari hanno tre punti individuali su ogni statistica fino alla fine, per il difetto di `CreateDomeOpponentMon`. Un pareggio, per esempio con Esplosione, lo vince la testa di serie migliore, e questa squadra si piazza quasi sempre prima.

Si gioca torneo dopo torneo, senza perderne uno. Astro Cupola Tolomeo compare la prima volta nella finale del torneo 5 e da' il simbolo d'argento; la seconda volta nella finale del torneo 10 e da' il simbolo d'oro. In tutto sono dieci tornei e quaranta incontri.

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 12, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Metagross Decisa | box 12, riga 1, colonna 3 | Avanzi | Meteorpugno, Terremoto, Palla Ombra, Esplosione |
| 3 | Slaking Decisa | box 12, riga 1, colonna 5 | Bendascelta | Ritorno, Terremoto, Palla Ombra, Iper Raggio |

Riserve con piu' riscontri accanto agli altri due, dalla misura di `MAPPA-RISERVE.md` e quindi non ancora una scelta: al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Metagross, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Slaking, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5).

## 2. Azienda Lotta, Simbolo Sapienza

Non si porta nulla dal PC: si combatte con esemplari in prestito, e dopo ogni vittoria si puo' scambiarne uno con uno dell'avversario battuto. Va portata all'oro PRIMA di costruire una serie lunga alla Torre Lotta a livello 50, perche' i punti individuali dei suoi avversari dipendono dalla serie corrente della Torre, per il difetto in `src/battle_tower.c`.

Si gioca una serie dopo l'altra senza interruzioni, perche' una sconfitta azzera la serie. Boss Azienda Savino compare la prima volta alla lotta 21, cioe' serie 3, lotta 7 di 7, per l'argento, e la seconda alla lotta 42, cioe' serie 6, lotta 7 di 7, per l'oro: servono 6 serie di fila.

## 3. Torre Lotta, Simbolo Abilita'

Tre contro tre, nessuna regola in piu'. Il primo della squadra e' il primo a scendere in campo.

Si gioca una serie dopo l'altra senza interruzioni, perche' una sconfitta azzera la serie. Dama Torre Alberta compare la prima volta alla lotta 35, cioe' serie 5, lotta 7 di 7, per l'argento, e la seconda alla lotta 70, cioe' serie 10, lotta 7 di 7, per l'oro: servono 10 serie di fila.

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 12, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Swampert Placida | box 12, riga 2, colonna 1 | Avanzi | Terremoto, Surf, Geloraggio, Contrattacco |
| 3 | Metagross Decisa | box 12, riga 1, colonna 3 | Bendascelta (il file porta Avanzi: scambiarlo in gioco) | Meteorpugno, Terremoto, Palla Ombra, Esplosione |

Riserve con piu' riscontri accanto agli altri due, dalla misura di `MAPPA-RISERVE.md` e quindi non ancora una scelta: al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Swampert, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5); al posto di Metagross, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3).

## 4. Dojo Lotta, Simbolo Valore

Tre turni per incontro, poi giudizio a punti: premia le mosse che fanno danno e quelle che vanno a segno, toglie un punto a Protezione, Individua e Resistenza, che questa squadra non porta. Il primo della squadra scende per primo, e l'ordine conta perche' gli esemplari si affrontano uno contro uno in sequenza.

Si gioca una serie dopo l'altra senza interruzioni, perche' una sconfitta azzera la serie. Maestra Dojo Valentina compare la prima volta alla lotta 28, cioe' serie 4, lotta 7 di 7, per l'argento, e la seconda alla lotta 56, cioe' serie 8, lotta 7 di 7, per l'oro: servono 8 serie di fila.

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 12, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Metagross Decisa | box 12, riga 1, colonna 3 | Bendascelta (il file porta Avanzi: scambiarlo in gioco) | Meteorpugno, Terremoto, Palla Ombra, Esplosione |
| 3 | Swampert Placida | box 12, riga 2, colonna 1 | Avanzi | Terremoto, Surf, Geloraggio, Contrattacco |

Riserve con piu' riscontri accanto agli altri due, dalla misura di `MAPPA-RISERVE.md` e quindi non ancora una scelta: al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Metagross, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Swampert, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5).

## 5. Palazzo Lotta, Simbolo Spirito

Non si comanda: ogni esemplare sceglie da se' secondo la propria natura. E' la ragione per cui questa squadra ha nature proprie e solo mosse d'attacco, spiegata in STUDIO-04 sezione 12.

Si gioca una serie dopo l'altra senza interruzioni, perche' una sconfitta azzera la serie. Sire Palazzo Spartaco compare la prima volta alla lotta 21, cioe' serie 3, lotta 7 di 7, per l'argento, e la seconda alla lotta 42, cioe' serie 6, lotta 7 di 7, per l'oro: servono 6 serie di fila.

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Metagross Vivace | box 12, riga 2, colonna 3 | Bendascelta | Meteorpugno, Terremoto |
| 2 | Latios Lesta | box 12, riga 2, colonna 5 | Baccaprugna | Psichico, Dragartigli, Fulmine, Surf |
| 3 | Swampert Audace | box 12, riga 3, colonna 1 | Avanzi | Terremoto, Surf, Geloraggio, Frana |

Riserve con piu' riscontri accanto agli altri due, dalla misura di `MAPPA-RISERVE.md` e quindi non ancora una scelta: al posto di Metagross, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Swampert, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5).

## 6. Serpe Lotta, Simbolo Fortuna

Quattordici sale per serie, tre porte per sala, e solo alcune sale sono lotte. Metagross e' immune all'iperavvelenamento della sala delle alterazioni di stato, che e' la piu' probabile al trentacinque per cento.

Si gioca una serie dopo l'altra senza interruzioni, perche' una sconfitta azzera la serie. Regina Serpe Fortunata compare la prima volta alla sala 28, cioe' serie 2, sala 14 di 14, per l'argento, e la seconda alla sala 140, cioe' serie 10, sala 14 di 14, per l'oro: servono 10 serie di fila.

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 12, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Metagross Decisa | box 12, riga 1, colonna 3 | Bendascelta (il file porta Avanzi: scambiarlo in gioco) | Meteorpugno, Terremoto, Palla Ombra, Esplosione |
| 3 | Blissey Sicura | box 12, riga 3, colonna 3 | Avanzi | Movim. Sismico, Tossina, Covauova, Canto |

Riserve con piu' riscontri accanto agli altri due, dalla misura di `MAPPA-RISERVE.md` e quindi non ancora una scelta: al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Metagross, Latias (box 12, riga 5, colonna 1), Tauros (box 13, riga 1, colonna 5); al posto di Blissey, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5).

## 7. Piramide Lotta, Simbolo Audacia

Gli strumenti vengono tolti all'ingresso, quindi si entra senza. Ogni serie di sette piani ha un bestiario a tema, il giro, e cambia chi conduce. Gli oggetti si raccolgono dentro.

Si gioca una serie dopo l'altra senza interruzioni, perche' una sconfitta azzera la serie. Re Piramide Baldo compare la prima volta al piano 22, cioe' serie 4, piano 1 di 7, per l'argento, e la seconda al piano 71, cioe' serie 11, piano 1 di 7, per l'oro: servono 11 serie di fila.

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 12, riga 1, colonna 1 | nessuno (il file porta Baccaprugna: toglierlo) | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Swampert Placida | box 12, riga 2, colonna 1 | nessuno (il file porta Avanzi: toglierlo) | Terremoto, Surf, Geloraggio, Protezione (cambiata per la Piramide: Protezione al posto di Contrattacco) |
| 3 | Metagross Decisa | box 12, riga 1, colonna 3 | nessuno (il file porta Avanzi: toglierlo) | Meteorpugno, Terremoto, Palla Ombra, Breccia (cambiata per la Piramide: Breccia al posto di Esplosione) |

Le mosse cambiate per questo edificio si insegnano in gioco con le MT prima di entrare. In terza generazione una MT si consuma all'uso, e la mossa sovrascritta non torna gratis: e' una delle ragioni per cui questo edificio viene per ultimo.

Chi conduce, serie per serie. Le prime dieci serie bastano all'oro e vengono dalla guida al completamento; la colonna del calcolo e' il controllo di `parco_lotta_piramide_ordine.py`, che concorda con la guida in sette casi su dieci sul membro impiegato.

| Serie | Piani | Tema del giro | Primo in campo | Cambio | Calcolo |
|---|---|---|---|---|---|
| 1 | 1-7 | mosse che paralizzano | Latios | nessuno | Latios |
| 2 | 8-14 | mosse che avvelenano | Latios | nessuno | Latios |
| 3 | 15-21 | mosse che scottano | Latios | nessuno | Metagross |
| 4 | 22-28 | consumo dei punti potere | Metagross | nessuno | Metagross |
| 5 | 29-35 | abilita' Levitazione | Metagross | Latios dal quarto piano | Swampert |
| 6 | 36-42 | abilita' che intrappolano | Metagross | Latios dal quarto piano | Latios |
| 7 | 43-49 | tipo Ghiaccio | Metagross | Latios dal quinto piano | Metagross |
| 8 | 50-56 | Autodistruzione ed Esplosione | Latios | Swampert dal quarto piano | Metagross |
| 9 | 57-63 | tipo Psico | Latios | Metagross dal secondo piano | Metagross |
| 10 | 64-70 | tipo Roccia | Swampert | Metagross dal terzo piano | Metagross |

Riserve con piu' riscontri accanto agli altri due, dalla misura di `MAPPA-RISERVE.md` e quindi non ancora una scelta: al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Swampert, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5); al posto di Metagross, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3).

## La disposizione completa dei box 12, 13 e 14

| Box | Riga | Colonna | Esemplare | Copia | Ruolo |
|---|---|---|---|---|---|
| 12 | 1 | 1 | Latios Timida | 1 | titolare |
| 12 | 1 | 2 | Latios Timida | 2 | titolare |
| 12 | 1 | 3 | Metagross Decisa | 1 | titolare |
| 12 | 1 | 4 | Metagross Decisa | 2 | titolare |
| 12 | 1 | 5 | Slaking Decisa | 1 | titolare |
| 12 | 1 | 6 | Slaking Decisa | 2 | titolare |
| 12 | 2 | 1 | Swampert Placida | 1 | titolare |
| 12 | 2 | 2 | Swampert Placida | 2 | titolare |
| 12 | 2 | 3 | Metagross Vivace | 1 | titolare |
| 12 | 2 | 4 | Metagross Vivace | 2 | titolare |
| 12 | 2 | 5 | Latios Lesta | 1 | titolare |
| 12 | 2 | 6 | Latios Lesta | 2 | titolare |
| 12 | 3 | 1 | Swampert Audace | 1 | titolare |
| 12 | 3 | 2 | Swampert Audace | 2 | titolare |
| 12 | 3 | 3 | Blissey Sicura | 1 | titolare |
| 12 | 3 | 4 | Blissey Sicura | 2 | titolare |
| 12 | 3 | 5 | Salamence Decisa | 1 | riserva |
| 12 | 3 | 6 | Salamence Decisa | 2 | riserva |
| 12 | 4 | 1 | Suicune Sicura | 1 | riserva |
| 12 | 4 | 2 | Suicune Sicura | 2 | riserva |
| 12 | 4 | 3 | Starmie Timida | 1 | riserva |
| 12 | 4 | 4 | Starmie Timida | 2 | riserva |
| 12 | 4 | 5 | Milotic Sicura | 1 | riserva |
| 12 | 4 | 6 | Milotic Sicura | 2 | riserva |
| 12 | 5 | 1 | Latias Calma | 1 | riserva |
| 12 | 5 | 2 | Latias Calma | 2 | riserva |
| 12 | 5 | 3 | Snorlax Cauta | 1 | riserva |
| 12 | 5 | 4 | Snorlax Cauta | 2 | riserva |
| 12 | 5 | 5 | Gengar Timida | 1 | riserva |
| 12 | 5 | 6 | Gengar Timida | 2 | riserva |
| 13 | 1 | 1 | Zapdos Modesta | 1 | riserva |
| 13 | 1 | 2 | Zapdos Modesta | 2 | riserva |
| 13 | 1 | 3 | Registeel Cauta | 1 | riserva |
| 13 | 1 | 4 | Registeel Cauta | 2 | riserva |
| 13 | 1 | 5 | Tauros Allegra | 1 | riserva |
| 13 | 1 | 6 | Tauros Allegra | 2 | riserva |
| 13 | 2 | 1 | Flygon Allegra | 1 | riserva |
| 13 | 2 | 2 | Flygon Allegra | 2 | riserva |
| 13 | 2 | 3 | Raikou Timida | 1 | riserva |
| 13 | 2 | 4 | Raikou Timida | 2 | riserva |
| 13 | 2 | 5 | Gyarados Decisa | 1 | riserva |
| 13 | 2 | 6 | Gyarados Decisa | 2 | riserva |
| 13 | 3 | 1 | Heracross Allegra | 1 | riserva |
| 13 | 3 | 2 | Heracross Allegra | 2 | riserva |
| 13 | 3 | 3 | Aerodactyl Decisa | 1 | riserva |
| 13 | 3 | 4 | Aerodactyl Decisa | 2 | riserva |
| 13 | 3 | 5 | Moltres Timida | 1 | riserva |
| 13 | 3 | 6 | Moltres Timida | 2 | riserva |
| 13 | 4 | 1 | Articuno Calma | 1 | riserva |
| 13 | 4 | 2 | Articuno Calma | 2 | riserva |
| 13 | 4 | 3 | Magneton Modesta | 1 | riserva |
| 13 | 4 | 4 | Magneton Modesta | 2 | riserva |
| 13 | 4 | 5 | Regice Modesta | 1 | riserva |
| 13 | 4 | 6 | Regice Modesta | 2 | riserva |
| 13 | 5 | 1 | Scizor Decisa | 1 | riserva |
| 13 | 5 | 2 | Scizor Decisa | 2 | riserva |
| 13 | 5 | 3 | Dusclops Sicura | 1 | riserva |
| 13 | 5 | 4 | Dusclops Sicura | 2 | riserva |
| 13 | 5 | 5 | Steelix Decisa | 1 | riserva |
| 13 | 5 | 6 | Steelix Decisa | 2 | riserva |
| 14 | 1 | 1 | Marowak Allegra | 1 | riserva |
| 14 | 1 | 2 | Marowak Allegra | 2 | riserva |
| 14 | 1 | 3 | Regirock Decisa | 1 | riserva |
| 14 | 1 | 4 | Regirock Decisa | 2 | riserva |

