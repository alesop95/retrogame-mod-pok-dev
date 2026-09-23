# Guida operativa agli esemplari del Parco Lotta di Smeraldo

> Da tenere accanto al gioco. Dice dove sta ogni esemplare, come si prepara una sfida e come la si gioca fino al simbolo d'oro. Le meccaniche sono verificate sul sorgente di `pret/pokeemerald` e spiegate per esteso in `STUDIO-04`; le scelte di squadra sono motivate in `STUDIO-05`. Dove un consiglio è una deduzione e non un fatto verificato, lo dice.
>
> Manutenzione: la prosa è scritta a mano; le tabelle fra i marcatori `generato da`, le figure sotto `figure/` e la copia `GUIDA-PARCO-LOTTA.docx` le rigenera `tools/parco_lotta_percorso_oro.py`. Dentro i marcatori non si scrive a mano; `--check` dice se la guida è rimasta indietro rispetto al catalogo. Figure e `.docx` non entrano in git, perché il `.gitignore` esclude i media per ADR-005: su un clone nuovo compaiono al primo lancio dello strumento.

## Avvio rapido

![Il lotto nel box 14 e nelle ultime due posizioni del box 13, disposizione di ADR-078](figure/box-13-14.png)

| Passo | Che cosa fare | Perché |
|---|---|---|
| 1 | Scegli l'edificio seguendo l'ordine della sezione 2 | due passi dell'ordine sono vincoli, non preferenze |
| 2 | Apri il PC, box 14, e preleva i tre esemplari della figura dell'edificio | gli otto titolari stanno tutti nella prima riga e mezza del box 14 |
| 3 | Mettili in squadra nell'ordine del numero sulla figura | il primo della squadra è il primo a scendere in campo |
| 4 | Controlla lo strumento di ciascuno con la tabella dell'edificio, e scambia dove la tabella dice "scambiarlo in gioco" | ogni file porta lo strumento della prima squadra in cui l'esemplare compare |
| 5 | Al banco scegli Livello 50 e formato singolo | le squadre sono composte per quella modalità; al Livello Aperto gli avversari e il loro catalogo cambiano |
| 6 | Vinci di fila le serie che dice il calendario | una sconfitta azzera la serie |

## 1. Tre regole che non si violano

| Regola | Perché |
|---|---|
| Questi 32 esemplari non combattono mai fuori dal Parco, non stanno in squadra mentre esplori, non ricevono Caramelle Rare | sei di loro, cioè i due Latios, Latias, Zapdos, Moltres e Articuno, sono a un solo punto di esperienza dal livello 51, perché per essere legali portano il massimo che il livello 50 consente: una lotta qualsiasi fuori dal Parco li porta al 51, e al 51 non si iscrivono più alla modalità Livello 50, per sempre, perché il livello non si abbassa. Gli altri hanno migliaia di punti di margine, che non sono infiniti. Nel Parco le lotte non danno esperienza, quindi lì il margine non si consuma |
| Le mosse non si toccano, tranne i due cambi della Piramide | in terza generazione una MT si consuma all'uso e la mossa sovrascritta non torna gratis |
| Questi esemplari non si scambiano | ognuno è in copia unica: le copie per lo scambio sono uscite dal deposito con ADR-077, e un esemplare scambiato lascia l'edificio senza titolare finché non lo si rigenera e riscrive sulla cartuccia |

Che cosa c'è nei box: 32 esemplari in copia unica, tutti al livello 50 e tutti legali per PKHeX, giudicati nel dump `round 4` del deposito intero il 2026-09-23. Chiudono il deposito, per ADR-078: il box 14 è tutto del lotto, dalla prima all'ultima posizione, e le due riserve meno usate, Marowak e Regirock, stanno nelle ultime due posizioni del box 13. I posti blu del box 14 sono gli 8 titolari, dalla prima riga fino alla seconda colonna della seconda riga; da lì cominciano le 24 riserve, in ordine di frequenza nelle squadre dei thread. Fino al settimo giro il lotto era in doppia copia nei box 12, 13 e 14: questa disposizione è quella del file di `giro11`, e vale sulla cartuccia da quando quel file vi è scritto. Il resto del deposito, cioè la collezione, gli eventi, gli incontri da biglietto, gli scambi in gioco e i due giganti, occupa i box da 1 a 13 senza buchi, e `MAPPA-BOX-SMERALDO.md` dice che cosa c'è in ciascuna delle 420 posizioni. Le copie di ciascun esemplare, finché erano due, erano gemelle, cioè con le stesse statistiche e la stessa abilità, e la causa delle differenze del sesto giro con la correzione è in `STUDIO-05` sezione 16. Quasi tutti hanno come allenatore ALEX, perché nascono da uova o da incontri di Smeraldo e di Rosso Fuoco; Suicune e Raikou hanno WES, perché vengono da Colosseum come esemplari Ombra purificati, e per il gioco sono scambiati, ma con tutte le medaglie obbediscono a qualunque livello. Nomi di nature, abilità, mosse e strumenti sono quelli del gioco italiano, letti dal dump di PKHeX e non tradotti a memoria: Hasty è Lesta, Fire Punch è Fuocopugno.

## 2. Ordine degli edifici e calendario

![Serie di fila che servono all'argento e all'oro, per edificio](figure/calendario.png)

L'ordine è Cupola, Azienda, Torre, Dojo, Palazzo, Serpe, Piramide, e tre passi sono vincoli. La Cupola va per prima: è il simbolo più economico e i suoi avversari restano deboli fino alla fine. L'Azienda va chiusa prima di allungare la serie alla Torre a livello 50, perché per un difetto del gioco i punti individuali degli avversari dell'Azienda dipendono dalla serie corrente della Torre. La Piramide va per ultima, perché chiede di cambiare due mosse con le MT. Torre, Dojo, Palazzo e Serpe si possono permutare. L'Asso compare due volte, e la seconda dà l'oro.

Vincoli di iscrizione, validi ovunque: nessuna specie ripetuta, nessuno strumento ripetuto, e nessuna delle dieci specie escluse, cioè Mewtwo, Mew, Lugia, Ho-Oh, Celebi, Kyogre, Groudon, Rayquaza, Jirachi e Deoxys. Latios, Latias, i tre cani e i tre Regi sono ammessi. Lo zaino non si usa in lotta, tranne la borsa propria della Piramide.

<!-- generato da parco_lotta_percorso_oro.py: calendario, inizio -->

| Edificio | Asso | Argento | Oro | Serie di fila per l'oro |
|---|---|---|---|---|
| Cupola Lotta | Astro Cupola Tolomeo | finale del torneo 5 | finale del torneo 10 | 10 tornei da 4 incontri |
| Azienda Lotta | Boss Azienda Savino | alla lotta 21, cioe' serie 3, lotta 7 di 7 | alla lotta 42, cioe' serie 6, lotta 7 di 7 | 6 serie da 7 lotte |
| Torre Lotta | Dama Torre Alberta | alla lotta 35, cioe' serie 5, lotta 7 di 7 | alla lotta 70, cioe' serie 10, lotta 7 di 7 | 10 serie da 7 lotte |
| Dojo Lotta | Maestra Dojo Valentina | alla lotta 28, cioe' serie 4, lotta 7 di 7 | alla lotta 56, cioe' serie 8, lotta 7 di 7 | 8 serie da 7 lotte |
| Palazzo Lotta | Sire Palazzo Spartaco | alla lotta 21, cioe' serie 3, lotta 7 di 7 | alla lotta 42, cioe' serie 6, lotta 7 di 7 | 6 serie da 7 lotte |
| Serpe Lotta | Regina Serpe Fortunata | alla sala 28, cioe' serie 2, sala 14 di 14 | alla sala 140, cioe' serie 10, sala 14 di 14 | 10 serie da 14 sale |
| Piramide Lotta | Re Piramide Baldo | al piano 22, cioe' serie 4, piano 1 di 7 | al piano 71, cioe' serie 11, piano 1 di 7 | 11 serie da 7 piani |

<!-- generato da parco_lotta_percorso_oro.py: calendario, fine -->

## 3. Cupola Lotta, Simbolo Tattica

![Cupola Lotta: i tre da prelevare](figure/squadra-cupola.png)

<!-- generato da parco_lotta_percorso_oro.py: squadra Cupola Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 14, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Metagross Decisa | box 14, riga 1, colonna 2 | Avanzi | Meteorpugno, Terremoto, Palla Ombra, Esplosione |
| 3 | Slaking Decisa | box 14, riga 1, colonna 3 | Bendascelta | Ritorno, Terremoto, Palla Ombra, Iper Raggio |

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 10 e quindi non ancora una scelta: al posto di Latios, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5); al posto di Metagross, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5); al posto di Slaking, Starmie (box 14, riga 2, colonna 5), Gengar (box 14, riga 3, colonna 3).

<!-- generato da parco_lotta_percorso_oro.py: squadra Cupola Lotta, fine -->

| Situazione | Che cosa fare |
|---|---|
| Prima di ogni incontro vedi la squadra avversaria | scegli due dei tre: ogni incontro è due contro due, quattro incontri per torneo, sedici concorrenti |
| Avversari deboli per tutti e dieci i tornei | è un difetto del gioco verificato nel sorgente, per cui hanno tre punti individuali su ogni statistica. È la ragione per cui Slaking gioca qui e solo qui: chiude l'incontro prima che il turno perso da Pigrone si paghi |
| Stai per usare Esplosione con il Metagross | alla Cupola un pareggio non è una sconfitta: avanza la testa di serie migliore, calcolata sui totali delle statistiche base, e questa squadra si piazza quasi sempre prima. Usala se sei certo di essere piazzato meglio, perché è una condizione e non una certezza |
| Scegli chi iscrivere | l'avversario sceglie i suoi due guardando i tuoi tre, con un criterio offensivo o difensivo estratto a sorte: la squadra iscritta è anche un'informazione che gli dai |

## 4. Azienda Lotta, Simbolo Sapienza

Non si porta nulla dal PC: si combatte con esemplari in prestito, e dopo ogni vittoria se ne può scambiare uno con uno dell'avversario appena battuto. È l'unico simbolo che non dipende dai box.

| Situazione | Che cosa fare |
|---|---|
| Prima di cominciare | tieni bassa la serie corrente alla Torre a livello 50 finché l'Azienda non è all'oro: così gli avversari dell'Azienda restano al gradino più basso, mentre i tuoi esemplari in prestito crescono con la serie, da tre punti individuali alla prima fino a trentuno dalla settima |
| Un avversario ha "Ritorno" | all'Azienda è in realtà Frustrazione, che colpisce più forte quanto meno l'esemplare è affezionato |
| Qualcuno ti suggerisce di riposare, salvare e ricaricare per migliorare i punti individuali | non farlo: è un effetto letto su un'enciclopedia e non verificato sul sorgente |

## 5. Torre Lotta, Simbolo Abilità

![Torre Lotta: i tre da prelevare](figure/squadra-torre.png)

<!-- generato da parco_lotta_percorso_oro.py: squadra Torre Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 14, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Swampert Placida | box 14, riga 1, colonna 4 | Avanzi | Terremoto, Surf, Geloraggio, Contrattacco |
| 3 | Metagross Decisa | box 14, riga 1, colonna 2 | Bendascelta (il file porta Avanzi: scambiarlo in gioco) | Meteorpugno, Terremoto, Palla Ombra, Esplosione |

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 10 e quindi non ancora una scelta: al posto di Latios, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5); al posto di Swampert, Starmie (box 14, riga 2, colonna 5), Gengar (box 14, riga 3, colonna 3); al posto di Metagross, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5).

<!-- generato da parco_lotta_percorso_oro.py: squadra Torre Lotta, fine -->

Prima di entrare: dai al Metagross Decisa la Bendascelta presa allo Slaking e lascia allo Slaking gli Avanzi del Metagross. Prima di tornare alla Cupola rifai lo scambio al contrario. È la squadra della guida di chi ha completato tutti e sette i simboli.

| Situazione | Che cosa fare |
|---|---|
| L'ultima lotta di ogni serie è più dura | è voluto: la settima lotta pesca da una tabella di avversari più forti |
| Sei fra la 43ª e la 49ª vittoria | è il tratto dove una serie si perde più spesso: gli avversari hanno già trentuno punti individuali e il bacino da cui vengono pescati più che raddoppia. Dalla 57ª in poi non cambia più |
| L'avversario usa Terremoto | è la mossa più frequente del catalogo, il doppio della seconda: Latios, con Levitazione, ne è immune, ed è una ragione per cui conduce |
| Colpi mancati in fila | Luminpolvere, Rapidartigli, Baccaprugna e Avanzi sono gli strumenti avversari più frequenti, e l'elusione è la seconda categoria di mosse di stato: una serie si perde più spesso per un colpo mancato che per uno subito |

## 6. Dojo Lotta, Simbolo Valore

![Dojo Lotta: i tre da prelevare](figure/squadra-dojo.png)

<!-- generato da parco_lotta_percorso_oro.py: squadra Dojo Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 14, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Metagross Decisa | box 14, riga 1, colonna 2 | Bendascelta (il file porta Avanzi: scambiarlo in gioco) | Meteorpugno, Terremoto, Palla Ombra, Esplosione |
| 3 | Swampert Placida | box 14, riga 1, colonna 4 | Avanzi | Terremoto, Surf, Geloraggio, Contrattacco |

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 10 e quindi non ancora una scelta: al posto di Latios, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5); al posto di Metagross, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5); al posto di Swampert, Starmie (box 14, riga 2, colonna 5), Gengar (box 14, riga 3, colonna 3).

<!-- generato da parco_lotta_percorso_oro.py: squadra Dojo Lotta, fine -->

Stessi tre della Torre, in un altro ordine, con lo stesso scambio di strumenti. Gli esemplari si affrontano uno contro uno in sequenza; se entrambi sopravvivono a tre turni decide un giudizio in tre voci da due punti.

| Voce del giudizio | Che cosa premia |
|---|---|
| Mente | la scelta di una mossa che fa danno, anche se poi la paralisi la impedisce; zero a Contrattacco, Specchiovelen e Pazienza; un punto in meno a Protezione, Individua e Resistenza |
| Tecnica | ogni mossa andata a segno, di più se superefficace; in meno le mosse mancate o fallite |
| Corpo | i punti salute rimasti rispetto a quelli iniziali |

Deduzione, non regola scritta: al Dojo conviene attaccare a ogni turno. Calmamente del Latios e Contrattacco dello Swampert non danno punti di mente, quindi usali solo se l'incontro si chiude prima del giudizio.

## 7. Palazzo Lotta, Simbolo Spirito

![Palazzo Lotta: i tre da prelevare](figure/squadra-palazzo.png)

<!-- generato da parco_lotta_percorso_oro.py: squadra Palazzo Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Metagross Vivace | box 14, riga 1, colonna 5 | Bendascelta | Meteorpugno, Terremoto |
| 2 | Latios Lesta | box 14, riga 1, colonna 6 | Baccaprugna | Psichico, Dragartigli, Fulmine, Surf |
| 3 | Swampert Audace | box 14, riga 2, colonna 1 | Avanzi | Terremoto, Surf, Geloraggio, Frana |

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 10 e quindi non ancora una scelta: al posto di Metagross, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5); al posto di Latios, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5); al posto di Swampert, Starmie (box 14, riga 2, colonna 5), Gengar (box 14, riga 3, colonna 3).

<!-- generato da parco_lotta_percorso_oro.py: squadra Palazzo Lotta, fine -->

Qui non si danno ordini: ogni turno l'esemplare sceglie da sé una categoria fra attacco, difesa e supporto, con proporzioni che dipendono dalla natura e cambiano sotto la metà dei punti salute, e poi una mossa in quella categoria. La squadra esce dal PC con gli strumenti giusti e non condivide esemplari con le altre. L'unica scelta che ti resta è l'ordine, e il primo è il Metagross.

| Esemplare | Quota d'attacco sopra metà PS | Sotto metà PS |
|---|---|---|
| Metagross Vivace | 88% | 22% |
| Latios Lesta | 58% | 88% |
| Swampert Audace | 70%, con 15 di difesa e 15 di supporto, senza distinzione di metà in STUDIO-04 | vedi a sinistra |

Il Metagross porta due sole mosse, Meteorpugno e Terremoto, apposta: quando la categoria estratta non ha mosse, metà di quella quota torna come attacco a caso, quindi togliere le mosse di stato fa attaccare più spesso.

## 8. Serpe Lotta, Simbolo Fortuna

![Serpe Lotta: i tre da prelevare](figure/squadra-serpe.png)

<!-- generato da parco_lotta_percorso_oro.py: squadra Serpe Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 14, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Metagross Decisa | box 14, riga 1, colonna 2 | Bendascelta (il file porta Avanzi: scambiarlo in gioco) | Meteorpugno, Terremoto, Palla Ombra, Esplosione |
| 3 | Blissey Sicura | box 14, riga 2, colonna 2 | Avanzi | Movim. Sismico, Tossina, Covauova, Canto |

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 10 e quindi non ancora una scelta: al posto di Latios, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5); al posto di Metagross, Latias (box 14, riga 3, colonna 1), Tauros (box 14, riga 3, colonna 6); al posto di Blissey, Starmie (box 14, riga 2, colonna 5), Gengar (box 14, riga 3, colonna 3).

<!-- generato da parco_lotta_percorso_oro.py: squadra Serpe Lotta, fine -->

Prima di entrare: al Metagross la Bendascelta dello Slaking, come per la Torre. Quattordici sale per serie; in ciascuna tre porte e un indizio che ne nomina una. Gli esiti sono lotte, cure, incontri selvatici, nessun evento e la sala delle alterazioni di stato, che è quella che decide le serie lunghe: un Kirlia o un Dusclops ne tenta una su un esemplare che non ne ha.

| Alterazione | Probabilità | Chi la regge |
|---|---|---|
| Iperavvelenamento | 35% | Metagross, di tipo Acciaio, è immune |
| Congelamento | 25% | la Baccaprugna del Latios la cura; l'Alternacura della Blissey la toglie quando esce dal campo |
| Paralisi | 20% | come sopra |
| Sonno | 10% | come sopra |
| Scottatura | 10% | come sopra |

Le due serie più lunghe dichiarate nei thread per questo edificio, 560 e 420 sale, avevano entrambe una Blissey.

## 9. Piramide Lotta, Simbolo Audacia

![Piramide Lotta: i tre da prelevare](figure/squadra-piramide.png)

| Passo | Prima di entrare |
|---|---|
| 1 | Togli gli strumenti a tutti e tre e lasciali nello zaino: il gioco li toglie comunque all'ingresso |
| 2 | Insegna Protezione (MT17) allo Swampert Placida al posto di Contrattacco |
| 3 | Insegna Breccia (MT31) al Metagross Decisa al posto di Esplosione, che qui si userebbe una volta sola perché i punti salute non si ripristinano fra un piano e l'altro |

<!-- generato da parco_lotta_percorso_oro.py: squadra Piramide Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 14, riga 1, colonna 1 | nessuno (il file porta Baccaprugna: toglierlo) | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Swampert Placida | box 14, riga 1, colonna 4 | nessuno (il file porta Avanzi: toglierlo) | Terremoto, Surf, Geloraggio, Protezione (cambiata per la Piramide: Protezione al posto di Contrattacco) |
| 3 | Metagross Decisa | box 14, riga 1, colonna 2 | nessuno (il file porta Avanzi: toglierlo) | Meteorpugno, Terremoto, Palla Ombra, Breccia (cambiata per la Piramide: Breccia al posto di Esplosione) |

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

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 10 e quindi non ancora una scelta: al posto di Latios, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5); al posto di Swampert, Starmie (box 14, riga 2, colonna 5), Gengar (box 14, riga 3, colonna 3); al posto di Metagross, Salamence (box 14, riga 2, colonna 3), Starmie (box 14, riga 2, colonna 5).

<!-- generato da parco_lotta_percorso_oro.py: squadra Piramide Lotta, fine -->

Ogni serie di sette piani ha un bestiario a tema, sostituito per intero a ogni serie: la squadra resta, cambia chi conduce, come dice la tabella qui sopra, presa dalla guida di chi ha completato i sette simboli. Gli oggetti si raccolgono dentro, in una borsa di dieci scomparti che si conserva da una sfida all'altra solo se la sfida si completa. Baldo, a differenza tua, tiene i suoi strumenti.

## 10. Le riserve

Servono a sostituire un titolare che in un edificio non rende, o a provare una variante. Sotto ogni squadra ci sono le due riserve con più riscontri accanto agli altri due titolari; le tabelle in fondo a questa sezione sono la misura completa sulle 268 squadre dei thread: la prima dice in quali edifici ciascuna specie è stata portata e con quale serie più lunga, la seconda conta per ogni posto di ogni squadra chi ha giocato accanto agli altri due. È una misura, non ancora una scelta, e va letta con tre avvertenze: i thread nominano la specie e quasi mai la natura, quindi un conteggio su Latios vale per entrambi i Latios; scrive soprattutto chi ha fatto una serie buona; la Torre pesa quanto quasi tutti gli altri edifici insieme.

I risultati più solidi: Salamence e Starmie sono i candidati più frequenti per quasi ogni posto; Latias è la sostituta naturale di Latios; al Palazzo le riserve più presenti sono quelle da attacco puro, Starmie, Salamence, Flygon e Scizor.

| Quando sostituisci | Ricorda |
|---|---|
| sempre | le riserve escono dal PC senza strumento: dagliene uno che nessun altro membro tiene |
| al Palazzo | una riserva con mosse di stato peggiora la squadra, per la ragione della sezione 7 |
| sempre | resta valida la prima regola della sezione 1 |

Tyranitar non c'è: evolve da Pupitar solo al livello 55, quindi al livello 50 non può esistere, e le squadre dei thread che lo portano sono del Livello Aperto.

<!-- generato da parco_lotta_percorso_oro.py: misura delle riserve, inizio -->

Squadre per edificio nel campione: Cupola Lotta 19, Torre Lotta 97, Dojo Lotta 26, Palazzo Lotta 38, Serpe Lotta 20, Piramide Lotta 8, Azienda Lotta 5, edificio non dichiarato 55.

### Per esemplare: in quali edifici e con quale serie

Ogni cella dice in quante squadre dei thread la specie compare in quell'edificio, e fra parentesi la serie piu' lunga dichiarata. Le specie con due esemplari nel lotto, cioe' Latios, Metagross e Swampert, condividono la riga.

| Esemplari | Ruolo | Cup | Tor | Doj | Pal | Ser | Pir | Azi | n.d. | Compagni piu' frequenti |
|---|---|---|---|---|---|---|---|---|---|---|
| metagross-adamant, metagross-sassy | titolare | 8 (100) | 22 (378) | 4 (186) | 11 (224) | 9 (560) | 2 (70) |  | 3 | Latios 21, Swampert 13, Salamence 12 |
| latios-hasty, latios-timid | titolare | 7 (133) | 15 (268) | 8 (143) | 10 (224) | 5 (420) | 2 (70) | 3 (62) | 6 (63) | Metagross 21, Swampert 10, Suicune 7 |
| blissey-bold | titolare | 2 (17) | 11 (163) |  | 4 (178) | 6 (560) | 4 (70) |  | 2 (140) | Metagross 9, Salamence 8, Latios 4 |
| slaking-adamant | titolare | 7 (30) | 8 (281) |  | 4 (154) |  | 4 (70) |  | 3 (222) | Gengar 6, Milotic 6, Metagross 5 |
| swampert-brave, swampert-relaxed | titolare |  | 12 (268) | 1 (40) | 7 (224) |  | 1 (70) |  | 1 | Metagross 13, Latios 10, Salamence 5 |
| salamence-adamant | riserva | 2 (17) | 13 (280) | 1 (40) | 8 (84) | 4 (78) | 2 (70) | 1 (56) | 8 (140) | Metagross 12, Starmie 12, Suicune 9 |
| suicune-bold | riserva | 5 (80) | 17 (343) | 3 (135) | 4 (154) | 2 |  | 1 (62) | 4 (168) | Salamence 9, Latios 7, Snorlax 6 |
| starmie-timid | riserva | 1 (12) | 7 (117) | 2 (75) | 9 (178) | 7 (78) | 2 (70) | 1 (56) | 3 | Salamence 12, Metagross 11, Heracross 6 |
| milotic-bold | riserva | 5 (28) | 6 | 3 (200) | 3 (84) | 3 (100) |  |  | 5 (140) | Metagross 6, Slaking 6, Salamence 5 |
| latias-calm | riserva | 3 | 10 (378) | 1 (56) |  | 3 (347) | 1 |  | 2 | Metagross 6, Latios 5, Slaking 4 |
| snorlax-careful | riserva |  | 7 (281) | 2 (40) | 1 (57) | 1 |  |  | 8 (222) | Salamence 7, Suicune 6, Latios 5 |
| gengar-timid | riserva | 4 (100) | 8 (281) | 2 (40) |  |  |  |  | 4 (222) | Slaking 6, Metagross 4, Snorlax 4 |
| zapdos-modest | riserva |  | 7 (461) |  | 3 (140) | 1 |  |  | 2 (63) | Kingdra 3, Metagross 3, Tyranitar 3 |
| registeel-careful | riserva |  | 7 (343) | 1 |  |  | 1 (70) |  | 3 | Latios 4, Latias 3, Moltres 3 |
| tauros-jolly | riserva | 3 (133) | 6 (139) |  | 1 (140) | 1 (420) |  |  |  | Latios 6, Gengar 2, Milotic 2 |
| flygon-jolly | riserva |  | 2 (155) |  | 4 (178) | 1 | 1 (70) |  | 2 | Starmie 5, Scizor 3, Gyarados 2 |
| raikou-timid | riserva |  | 7 (215) |  | 1 (42) |  |  |  | 2 | Aerodactyl 3, Blissey 3, Machamp 1 |
| gyarados-adamant | riserva |  | 3 | 1 (143) | 2 (40) |  | 1 (70) |  | 2 | Flygon 2, Metagross 2, Swampert 2 |
| heracross-jolly | riserva | 1 (12) | 4 (98) | 1 (56) |  | 1 (347) | 1 | 1 (56) |  | Starmie 6, Salamence 3, Latias 2 |
| aerodactyl-adamant | riserva |  | 6 (137) |  |  |  |  |  | 2 (63) | Blissey 3, Raikou 3, Gengar 2 |
| moltres-timid | riserva |  | 4 (210) |  |  | 1 |  |  | 3 | Latios 3, Registeel 3, Entei 1 |
| articuno-calm | riserva |  | 3 (155) |  |  |  |  |  | 3 | Suicune 2, Flygon 1, Gengar 1 |
| magneton-modest | riserva |  | 2 (56) |  | 2 (84) |  |  |  | 2 | Aggron 2, Gengar 2, Starmie 2 |
| regice-modest | riserva | 2 (12) | 2 (110) | 1 (143) | 1 (43) |  |  |  |  | Heracross 2, Latios 2, Flygon 1 |
| scizor-adamant | riserva |  |  | 1 | 4 (178) |  |  |  | 1 | Flygon 3, Starmie 3, Arcanine 1 |
| dusclops-bold | riserva |  | 2 (137) |  | 1 (28) |  |  |  | 2 | Aerodactyl 1, Arcanine 1, Duskull 1 |
| steelix-adamant | riserva |  | 2 |  | 1 |  |  |  | 2 | Quagsire 2, Flygon 1, Gyarados 1 |
| marowak-jolly | riserva |  | 1 (280) |  | 1 (147) | 1 |  |  |  | Suicune 2, Salamence 1, Snorlax 1 |
| regirock-adamant | riserva |  | 1 |  |  |  |  |  |  | nessuno |

### Per sostituzione: chi ha giocato accanto agli altri due

Per ogni squadra e per ogni posto, le riserve del lotto che nei thread compaiono accanto ai due titolari che restano. La prima cifra conta le squadre con entrambi, la seconda quelle con almeno uno, la terza quelle con almeno uno nello stesso edificio. L'Azienda Lotta non compare perche' vi si combatte con esemplari in prestito.

| Edificio | Esce | Restano | Candidati: entrambi / almeno uno / stesso edificio |
|---|---|---|---|
| Cupola Lotta | latios-timid | Metagross, Slaking | Salamence 2/15/1; Starmie 1/13/1; Milotic 1/11/5; Gengar 1/9/4 |
| Cupola Lotta | metagross-adamant | Latios, Slaking | Salamence 1/5/1; Starmie 1/5/0; Suicune 0/10/2; Gengar 0/9/4 |
| Cupola Lotta | slaking-adamant | Latios, Metagross | Starmie 2/12/1; Gengar 2/5/3; Salamence 1/12/0; Latias 1/10/0 |
| Torre Lotta | latios-timid | Metagross, Swampert | Salamence 3/14/4; Starmie 2/11/2; Latias 1/7/5; Gyarados 1/3/2 |
| Torre Lotta | swampert-relaxed | Latios, Metagross | Starmie 2/12/3; Gengar 2/5/1; Salamence 1/12/3; Latias 1/10/4 |
| Torre Lotta | metagross-adamant | Latios, Swampert | Salamence 1/5/3; Starmie 1/4/2; Suicune 0/8/4; Latias 0/7/2 |
| Dojo Lotta | latios-timid | Metagross, Swampert | Salamence 3/14/0; Starmie 2/11/1; Latias 1/7/0; Gyarados 1/3/0 |
| Dojo Lotta | metagross-adamant | Latios, Swampert | Salamence 1/5/0; Starmie 1/4/1; Suicune 0/8/1; Latias 0/7/0 |
| Dojo Lotta | swampert-relaxed | Latios, Metagross | Starmie 2/12/1; Gengar 2/5/1; Salamence 1/12/0; Latias 1/10/0 |
| Palazzo Lotta | metagross-sassy | Latios, Swampert | Salamence 1/5/1; Starmie 1/4/0; Suicune 0/8/1; Latias 0/7/0 |
| Palazzo Lotta | latios-hasty | Metagross, Swampert | Salamence 3/14/4; Starmie 2/11/2; Latias 1/7/0; Gyarados 1/3/0 |
| Palazzo Lotta | swampert-brave | Latios, Metagross | Starmie 2/12/2; Gengar 2/5/0; Salamence 1/12/3; Latias 1/10/0 |
| Serpe Lotta | latios-timid | Blissey, Metagross | Salamence 3/17/4; Starmie 2/13/5; Milotic 1/8/0; Latias 1/7/2 |
| Serpe Lotta | metagross-adamant | Blissey, Latios | Latias 1/6/3; Tauros 1/6/1; Heracross 1/2/1; Salamence 0/9/1 |
| Serpe Lotta | blissey-bold | Latios, Metagross | Starmie 2/12/4; Gengar 2/5/0; Salamence 1/12/3; Latias 1/10/3 |
| Piramide Lotta | latios-timid | Metagross, Swampert | Salamence 3/14/1; Starmie 2/11/1; Latias 1/7/1; Gyarados 1/3/1 |
| Piramide Lotta | swampert-relaxed | Latios, Metagross | Starmie 2/12/1; Gengar 2/5/0; Salamence 1/12/1; Latias 1/10/1 |
| Piramide Lotta | metagross-adamant | Latios, Swampert | Salamence 1/5/1; Starmie 1/4/1; Suicune 0/8/0; Latias 0/7/0 |

<!-- generato da parco_lotta_percorso_oro.py: misura delle riserve, fine -->

## 11. Le schede dei trentadue esemplari

Nell'ordine del lotto, titolari prima. Abilità, luogo e gioco d'incontro sono letti dal dump di PKHeX `round 4` del deposito intero; i punti base usano le sigle del gioco; il margine è quanti punti di esperienza mancano al livello 51, e dove vale uno vale la prima regola della sezione 1. Lo strumento nel file è quello con cui l'esemplare esce dal PC, e per le riserve è nessuno.

<!-- generato da parco_lotta_percorso_oro.py: schede, inizio -->

| Posizione | Esemplare | Abilita' | Punti base | Mosse | Strumento nel file | Incontro | Margine al 51 |
|---|---|---|---|---|---|---|---|
| box 14, riga 1, colonna 1 | Latios Timida | Levitazione | 4 PS / 252 AttSp / 252 Vel | Calmamente, Psichico, Dragartigli, Fulmine | Baccaprugna | Isola Remota, Smeraldo, livello 50 | 1, ATTENZIONE |
| box 14, riga 1, colonna 2 | Metagross Decisa | Corpochiaro | 252 PS / 252 Att / 4 Vel | Meteorpugno, Terremoto, Palla Ombra, Esplosione | Avanzi | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 14, riga 1, colonna 3 | Slaking Decisa | Pigrone | 4 PS / 252 Att / 252 Vel | Ritorno, Terremoto, Palla Ombra, Iper Raggio | Bendascelta | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 14, riga 1, colonna 4 | Swampert Placida | Acquaiuto | 252 PS / 212 Dif / 44 AttSp | Terremoto, Surf, Geloraggio, Contrattacco | Avanzi | Percorso 117, Smeraldo, livello uovo | 7766 |
| box 14, riga 1, colonna 5 | Metagross Vivace | Corpochiaro | 252 PS / 252 Att / 4 Dif | Meteorpugno, Terremoto | Bendascelta | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 14, riga 1, colonna 6 | Latios Lesta | Levitazione | 4 PS / 252 AttSp / 252 Vel | Psichico, Dragartigli, Fulmine, Surf | Baccaprugna | Isola Remota, Smeraldo, livello 50 | 1, ATTENZIONE |
| box 14, riga 2, colonna 1 | Swampert Audace | Acquaiuto | 252 PS / 252 Att / 4 Dif | Terremoto, Surf, Geloraggio, Frana | Avanzi | Percorso 117, Smeraldo, livello uovo | 7766 |
| box 14, riga 2, colonna 2 | Blissey Sicura | Alternacura | 252 PS / 252 Dif / 4 DifSp | Movim. Sismico, Tossina, Covauova, Canto | Avanzi | Percorso 117, Smeraldo, livello uovo | 6120 |
| box 14, riga 2, colonna 3 | Salamence Decisa | Prepotenza | 4 PS / 252 Att / 252 Vel | Frana, Terremoto, Aeroassalto, Breccia | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 14, riga 2, colonna 4 | Suicune Sicura | Pressione | 252 PS / 252 Dif / 4 AttSp | Surf, Calmamente, Riposo, Sostituto | nessuno | Cupola Torre (C) / Sulfuria (XD) [110], Colosseum/XD, livello 40 | 9563 |
| box 14, riga 2, colonna 5 | Starmie Timida | Alternacura | 4 PS / 252 AttSp / 252 Vel | Psichico, Fulmine, Geloraggio, Surf | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 14, riga 2, colonna 6 | Milotic Sicura | Pelledura | 252 PS / 252 Dif / 4 AttSp | Surf, Geloraggio, Tossina, Ripresa | nessuno | Percorso 117, Smeraldo, livello uovo | 6324 |
| box 14, riga 3, colonna 1 | Latias Calma | Levitazione | 252 PS / 60 Dif / 12 DifSp / 180 Vel | Schermoluce, Riflesso, Tossina, Psichico | nessuno | Isola Remota, Smeraldo, livello 50 | 1, ATTENZIONE |
| box 14, riga 3, colonna 2 | Snorlax Cauta | Grassospesso | 168 PS / 120 Dif / 220 DifSp | Maledizione, Ritorno, Riposo, Terremoto | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 14, riga 3, colonna 3 | Gengar Timida | Levitazione | 4 PS / 252 AttSp / 252 Vel | Fulmine, Gelopugno, Fuocopugno, Destinobbligato | nessuno | Percorso 117, Smeraldo, livello uovo | 7766 |
| box 14, riga 3, colonna 4 | Zapdos Modesta | Pressione | 252 PS / 252 AttSp / 4 DifSp | Fulmine, Perforbecco, Riposo, Sonnolalia | nessuno | Centrale Elett., Rosso Fuoco, livello 50 | 1, ATTENZIONE |
| box 14, riga 3, colonna 5 | Registeel Cauta | Corpochiaro | 252 PS / 244 Att / 4 Dif | Ferrartigli, Sostituto, Maledizione, Amnesia | nessuno | Tomba Antica, Smeraldo, livello 40 | 9563 |
| box 14, riga 3, colonna 6 | Tauros Allegra | Prepotenza | 4 PS / 252 Att / 252 Vel | Ritorno, Terremoto, Sdoppiatore, Codacciaio | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 14, riga 4, colonna 1 | Flygon Allegra | Levitazione | 4 PS / 252 Att / 252 Vel | Terremoto, Frana, Dragartigli, Protezione | nessuno | Percorso 117, Smeraldo, livello uovo | 7766 |
| box 14, riga 4, colonna 2 | Raikou Timida | Pressione | 4 PS / 252 AttSp / 252 Vel | Fulmine, Calmamente, Sostituto, Riposo | nessuno | Cupola Torre (C) / Sulfuria (XD) [113], Colosseum/XD, livello 40 | 9563 |
| box 14, riga 4, colonna 3 | Gyarados Decisa | Prepotenza | 4 PS / 252 Att / 252 Vel | Ritorno, Terremoto, Dragodanza, Riposo | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 14, riga 4, colonna 4 | Heracross Allegra | Aiutinsetto | 4 PS / 252 Att / 252 Vel | Megacorno, Breccia, Frana, Terremoto | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 14, riga 4, colonna 5 | Aerodactyl Decisa | Testadura | 4 PS / 252 Att / 252 Vel | Frana, Terremoto, Aeroassalto, Sdoppiatore | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 14, riga 4, colonna 6 | Moltres Timida | Pressione | 220 PS / 52 Dif / 236 Vel | Lanciafiamme, Tossina, Sostituto, Protezione | nessuno | Monte Brace, Rosso Fuoco, livello 50 | 1, ATTENZIONE |
| box 14, riga 5, colonna 1 | Articuno Calma | Pressione | 220 PS / 60 DifSp / 228 Vel | Geloraggio, Tossina, Sostituto, Protezione | nessuno | Isole Spumarine, Rosso Fuoco, livello 50 | 1, ATTENZIONE |
| box 14, riga 5, colonna 2 | Magneton Modesta | Magnetismo | 80 Dif / 252 AttSp / 176 Vel | Fulmine, Resistenza, Ferrostrido, Introforza | nessuno | Percorso 117, Smeraldo, livello uovo | 7651 |
| box 14, riga 5, colonna 3 | Regice Modesta | Corpochiaro | 168 PS / 148 Dif / 100 AttSp / 92 DifSp | Geloraggio, Fulmine, Riposo, Sonnolalia | nessuno | Grotta Insulare, Smeraldo, livello 40 | 9563 |
| box 14, riga 5, colonna 4 | Scizor Decisa | Aiutinsetto | 20 PS / 236 Att / 252 Vel | Alacciaio, Aeroassalto, Danzaspada, Sostituto | nessuno | Percorso 117, Smeraldo, livello uovo | 7651 |
| box 14, riga 5, colonna 5 | Dusclops Sicura | Pressione | 252 PS / 252 Dif / 4 DifSp | Maledizione, Sostituto, Protezione, Malcomune | nessuno | Percorso 117, Smeraldo, livello uovo | 6120 |
| box 14, riga 5, colonna 6 | Steelix Decisa | Testadura | 132 PS / 252 Att / 120 DifSp / 4 Vel | Terremoto, Esplosione, Tossina, Frana | nessuno | Percorso 117, Smeraldo, livello uovo | 7651 |
| box 13, riga 5, colonna 5 | Marowak Allegra | Testadura | 4 PS / 252 Att / 252 Vel | Terremoto, Frana, Sdoppiatore, Danzaspada | nessuno | Percorso 117, Smeraldo, livello uovo | 7651 |
| box 13, riga 5, colonna 6 | Regirock Decisa | Corpochiaro | 252 PS / 252 Att / 4 Dif | Frana, Terremoto, Maledizione, Esplosione | nessuno | Rovine Sabbiose, Smeraldo, livello 40 | 9563 |

<!-- generato da parco_lotta_percorso_oro.py: schede, fine -->

## 12. La disposizione completa del lotto nei box 13 e 14

Riga per riga, contando dall'alto a sinistra. Una copia per esemplare; le altre posizioni del box 13 e tutti i box precedenti sono nella mappa `MAPPA-BOX-SMERALDO.md`.

<!-- generato da parco_lotta_percorso_oro.py: disposizione, inizio -->

| Box | Riga | Colonna | Esemplare | Ruolo |
|---|---|---|---|---|
| 13 | 5 | 5 | Marowak Allegra | riserva |
| 13 | 5 | 6 | Regirock Decisa | riserva |
| 14 | 1 | 1 | Latios Timida | titolare |
| 14 | 1 | 2 | Metagross Decisa | titolare |
| 14 | 1 | 3 | Slaking Decisa | titolare |
| 14 | 1 | 4 | Swampert Placida | titolare |
| 14 | 1 | 5 | Metagross Vivace | titolare |
| 14 | 1 | 6 | Latios Lesta | titolare |
| 14 | 2 | 1 | Swampert Audace | titolare |
| 14 | 2 | 2 | Blissey Sicura | titolare |
| 14 | 2 | 3 | Salamence Decisa | riserva |
| 14 | 2 | 4 | Suicune Sicura | riserva |
| 14 | 2 | 5 | Starmie Timida | riserva |
| 14 | 2 | 6 | Milotic Sicura | riserva |
| 14 | 3 | 1 | Latias Calma | riserva |
| 14 | 3 | 2 | Snorlax Cauta | riserva |
| 14 | 3 | 3 | Gengar Timida | riserva |
| 14 | 3 | 4 | Zapdos Modesta | riserva |
| 14 | 3 | 5 | Registeel Cauta | riserva |
| 14 | 3 | 6 | Tauros Allegra | riserva |
| 14 | 4 | 1 | Flygon Allegra | riserva |
| 14 | 4 | 2 | Raikou Timida | riserva |
| 14 | 4 | 3 | Gyarados Decisa | riserva |
| 14 | 4 | 4 | Heracross Allegra | riserva |
| 14 | 4 | 5 | Aerodactyl Decisa | riserva |
| 14 | 4 | 6 | Moltres Timida | riserva |
| 14 | 5 | 1 | Articuno Calma | riserva |
| 14 | 5 | 2 | Magneton Modesta | riserva |
| 14 | 5 | 3 | Regice Modesta | riserva |
| 14 | 5 | 4 | Scizor Decisa | riserva |
| 14 | 5 | 5 | Dusclops Sicura | riserva |
| 14 | 5 | 6 | Steelix Decisa | riserva |

<!-- generato da parco_lotta_percorso_oro.py: disposizione, fine -->

## 13. Che cosa questa guida non sa

Nessuna squadra è ancora stata provata in partita su questa cartuccia: sono composte su ciò che ha funzionato ad altri e su vincoli verificati nel sorgente, che è il massimo che si possa fare prima di giocare. La scelta delle riserve per edificio è ancora da scrivere sopra la misura. Gli ordini di conduzione della Piramide oltre la decima serie sono calcolati e non presi da una fonte, e servono solo oltre il simbolo d'oro. Quando perdi una serie, annota dove e contro chi: è l'informazione che serve per correggere la squadra.
