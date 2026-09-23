# Guida all'uso degli esemplari generati per il Parco Lotta di Smeraldo

> Scritta il 2026-09-23, dopo che i sessantaquattro esemplari del lotto sono stati scritti sulla cartuccia vera e verificati byte per byte. È la guida da tenere accanto al gioco, ed è un documento solo per scelta: dice che cosa c'è nei box, che cosa non fare fuori dal Parco, come preparare ogni sfida, come giocarla fino al simbolo d'oro, quali riserve tirare fuori e dove si trova ciascun esemplare. Le meccaniche vengono da `STUDIO-04`, verificate sul sorgente di `pret/pokeemerald`, e le scelte di squadra da `STUDIO-05`. Dove un consiglio è una deduzione e non un fatto verificato, il testo lo dice.
>
> La prosa è scritta a mano. Le tabelle che discendono dal catalogo, cioè il calendario, le squadre posizione per posizione, la misura delle riserve, le schede dei trentadue esemplari e la disposizione nei box, stanno fra coppie di marcatori e le riscrive `tools/parco_lotta_percorso_oro.py`: dentro i marcatori non si scrive a mano, fuori sì. Dopo una modifica al catalogo si rilancia lo strumento, e `--check` dice se la guida è rimasta indietro.

## 1. Che cosa c'è nella cartuccia

I sessantaquattro esemplari stanno nei box 12, 13 e 14, e sono trentadue esemplari distinti in doppia copia. Le due copie di ciascuno sono affiancate: quella a sinistra, la copia 1, è quella da usare, e quella a destra, la copia 2, è la copia destinata allo scambio. I primi sedici posti del box 12 sono gli otto titolari delle squadre, cioè le tre righe in alto più le prime due posizioni della terza; dalla terza riga, quinta colonna, cominciano le ventiquattro riserve, in ordine di frequenza nelle squadre di chi ha giocato, e proseguono nel box 13 fino alle prime quattro posizioni del box 14. I box 10 e 11 sono vuoti, e i box da 1 a 9 contengono il resto del deposito, compattato.

Tutti gli esemplari sono al livello 50, e tutti sono stati giudicati legali da PKHeX al sesto giro di verifica, sessantaquattro su sessantaquattro. Quasi tutti portano come allenatore d'origine ALEX con il tuo identificativo, perché nascono da uova, da incontri di Smeraldo o da incontri di Rosso Fuoco; Suicune e Raikou portano invece WES, cioè il giocatore di Colosseum, perché vengono da là come esemplari Ombra purificati, e per il gioco sono esemplari ricevuti in scambio. Con tutte le medaglie un esemplare scambiato obbedisce a qualunque livello, quindi la differenza non si vede in lotta.

I nomi di nature, abilità, mosse e strumenti in questa guida sono quelli che il gioco italiano mostra, letti dal dump di PKHeX e non tradotti a memoria. Due nomi che i documenti di studio scrivevano in un altro modo sono stati corretti il 2026-09-23: la natura Hasty si chiama Lesta, e la mossa Fire Punch si chiama Fuocopugno.

## 2. Tre regole che valgono fuori dal Parco, prima di tutto il resto

La prima regola è la più importante di tutta la guida, e la sua ragione è aritmetica. Sei esemplari si incontrano in gioco già al livello 50, cioè i due Latios, Latias, Zapdos, Moltres e Articuno, e per essere legali portano l'esperienza massima che il livello 50 consente, cioè un punto sotto la soglia del 51. Basta quindi un solo punto di esperienza per portarli al livello 51, e un esemplare al 51 non si può più iscrivere alla modalità Livello 50, per sempre, perché il livello non si abbassa. Nel Parco le lotte non danno esperienza, quindi lì non c'è rischio; fuori, invece, qualunque lotta a cui l'esemplare partecipi basta. Gli altri ventisei hanno un margine di diverse migliaia di punti, che non è infinito, e la conclusione vale per tutti e trentadue: questi esemplari non si usano mai fuori dal Parco, non si portano in squadra mentre si esplora, e non ricevono mai una Caramella Rara. La colonna del margine nelle schede della sezione 13 dice il numero esatto per ciascuno.

La seconda regola riguarda le mosse. In terza generazione una MT si consuma all'uso, e una mossa sovrascritta non torna gratis: gli insiemi di mosse sono stati scelti per edificio, e l'unico cambio previsto è quello della Piramide, descritto nella sezione 10. Fuori da quel caso le mosse non si toccano.

La terza regola riguarda gli scambi. La copia 2 esiste per essere scambiata, la copia 1 per essere usata: scambiare la copia 1 lascia l'edificio senza il suo titolare, e rigenerarlo vuol dire rifare l'intero ciclo di verifica e di scrittura sulla cartuccia.

## 3. Come si prepara ogni sfida

Tutte le sfide si giocano in modalità Livello 50 e in formato singolo, cioè uno contro uno, che è il formato per cui le squadre sono state composte. Nella prima scelta al banco di ogni edificio va quindi selezionato il Livello 50, e non il Livello Aperto, dove gli avversari salgono di livello con la squadra e il catalogo degli avversari cambia.

Prima di entrare si prelevano dal PC i tre esemplari della squadra, sempre la copia 1, e si mettono in squadra nell'ordine indicato, perché il primo della squadra è il primo a scendere in campo. Valgono per tutti gli edifici tre vincoli di iscrizione verificati due volte: nessuna specie ripetuta, nessuno strumento ripetuto, e nessuna delle dieci specie escluse, cioè Mewtwo, Mew, Lugia, Ho-Oh, Celebi, Kyogre, Groudon, Rayquaza, Jirachi e Deoxys. Latios, Latias, i tre cani e i tre Regi sono ammessi. Gli strumenti dello zaino non si usano durante le lotte, tranne alla Piramide, che ha una borsa propria.

Gli strumenti meritano una parola, perché un esemplare ne tiene uno solo e ogni file porta lo strumento della prima squadra in cui l'esemplare compare. Alla Cupola il Metagross Decisa tiene gli Avanzi e lo Slaking la Bendascelta; alla Torre, al Dojo e alla Serpe lo stesso Metagross vuole invece la Bendascelta, e gli Avanzi li tiene già un altro membro della squadra. Il modo più semplice è uno scambio fra i due: prima di quei tre edifici si dà al Metagross Decisa la Bendascelta presa dallo Slaking e si lasciano allo Slaking gli Avanzi del Metagross, e prima di tornare alla Cupola si rifà lo scambio al contrario. La squadra del Palazzo e quella della Serpe, per il resto, escono già dal PC con gli strumenti giusti.

## 4. L'ordine degli edifici, e perché non è indifferente

L'ordine consigliato è Cupola, Azienda, Torre, Dojo, Palazzo, Serpe e Piramide, e due dei suoi passi sono vincoli e non preferenze. La Cupola va per prima perché è il simbolo più economico e perché i suoi avversari restano deboli fino alla fine, per un difetto del gioco descritto nella sezione 5. L'Azienda va chiusa prima di costruire una serie lunga alla Torre a livello 50, perché i punti individuali degli avversari dell'Azienda dipendono, per un secondo difetto del gioco, dalla serie corrente della Torre: finché quella resta bassa, all'Azienda si affrontano avversari al primo gradino. La Piramide va per ultima perché chiede di cambiare due mosse con le MT, e le mosse sovrascritte non si recuperano gratis. Gli altri tre si possono permutare.

L'Asso di ogni edificio compare due volte, e la seconda dà il simbolo d'oro. Una sconfitta azzera la serie, quindi le serie che servono vanno vinte tutte di fila. Il calendario, dal sorgente e con il conteggio corretto, è questo.

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

## 5. Cupola Lotta, Simbolo Tattica

Si iscrivono Latios Timida, dal box 12 in prima riga e prima colonna, con la Baccaprugna; Metagross Decisa, prima riga e terza colonna, con gli Avanzi; e Slaking Decisa, prima riga e quinta colonna, con la Bendascelta. Il torneo è a eliminazione fra sedici concorrenti, quattro incontri per torneo, e ogni incontro è due contro due: prima di ciascuno si vede la squadra avversaria e si scelgono due dei tre iscritti.

La ragione per cui questo edificio viene per primo è un difetto verificato nel sorgente: la funzione che crea gli avversari della Cupola passa al calcolo dei punti individuali un identificativo sbagliato, e il risultato è che tutti gli avversari hanno tre punti individuali su ogni statistica, fino al decimo torneo compreso. È anche la ragione per cui Slaking entra qui e in nessun altro edificio: contro avversari così deboli la sua potenza chiude l'incontro prima che il turno perso dall'abilità Pigrone si paghi.

Due regole del torneo cambiano il modo di giocare. La prima è il pareggio: se gli ultimi due esemplari cadono nello stesso turno, per esempio con l'Esplosione del Metagross, alla Cupola non si perde, ma avanza la testa di serie migliore, e il piazzamento si calcola sui totali delle statistiche base, per cui questa squadra si piazza quasi sempre prima. È una condizione e non una certezza, quindi l'Esplosione conviene quando si è certi di essere piazzati meglio. La seconda è che l'avversario sceglie i suoi due esemplari guardando i tuoi tre, con un criterio offensivo o difensivo estratto a sorte, quindi la squadra iscritta è anche un'informazione che gli dai.

La squadra, posizione per posizione, con strumenti e mosse come il gioco li mostra.

<!-- generato da parco_lotta_percorso_oro.py: squadra Cupola Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 12, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Metagross Decisa | box 12, riga 1, colonna 3 | Avanzi | Meteorpugno, Terremoto, Palla Ombra, Esplosione |
| 3 | Slaking Decisa | box 12, riga 1, colonna 5 | Bendascelta | Ritorno, Terremoto, Palla Ombra, Iper Raggio |

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 12 e quindi non ancora una scelta: al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Metagross, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Slaking, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5).

<!-- generato da parco_lotta_percorso_oro.py: squadra Cupola Lotta, fine -->

## 6. Azienda Lotta, Simbolo Sapienza

Qui non si porta nulla dal PC: si combatte con esemplari in prestito, e dopo ogni vittoria si può scambiarne uno con uno dell'avversario appena battuto. È l'unico simbolo d'oro che non dipende in alcun modo dai box. I punti individuali degli esemplari in prestito crescono con la serie, da tre alla prima serie fino a trentuno dalla settima, mentre quelli degli avversari restano al gradino basso finché la serie corrente alla Torre a livello 50 resta bassa, che è il motivo dell'ordine.

Due avvertenze vengono dalle fonti. La prima: all'Azienda la mossa che nel catalogo compare come Ritorno è in realtà Frustrazione, quindi un avversario con quella mossa colpisce più forte quanto meno è affezionato. La seconda: circola un effetto per cui riposare, salvare e ricaricare porterebbe tutti i punti individuali al valore di quello di attacco; è letto su un'enciclopedia e non verificato sul sorgente, e questa guida non lo consiglia.

## 7. Torre Lotta, Simbolo Abilità

In squadra, nell'ordine: Latios Timida con la Baccaprugna, Swampert Placida dal box 12 in seconda riga e prima colonna con gli Avanzi, e Metagross Decisa con la Bendascelta. È la squadra della guida di chi ha completato tutti e sette i simboli, e il nucleo che ricorre in testa alle squadre dei thread per ogni edificio.

La Torre non aggiunge regole, ma il suo catalogo degli avversari dice tre cose utili. La settima lotta di ogni serie pesca da una tabella più dura delle prime sei, quindi il salto di difficoltà all'ultimo avversario è voluto dal gioco. Il punto dove una serie si perde più facilmente è la sesta sfida, cioè fra la quarantatreesima e la quarantanovesima vittoria, dove gli avversari hanno già trentuno punti individuali e il bacino da cui vengono pescati più che raddoppia; dalla cinquantasettesima vittoria in poi il bacino non cambia più. E fra le mosse avversarie Terremoto domina, con il doppio delle occorrenze della seconda: Latios, con Levitazione, ne è immune, ed è una delle ragioni per cui conduce. Fra gli strumenti avversari più frequenti ci sono Rapidartigli, Baccaprugna, Avanzi e Luminpolvere, e fra le mosse di stato l'elusione è la seconda categoria per frequenza: una serie lunga si perde più spesso per un colpo mancato che per un colpo subito.

La squadra, posizione per posizione, con strumenti e mosse come il gioco li mostra.

<!-- generato da parco_lotta_percorso_oro.py: squadra Torre Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 12, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Swampert Placida | box 12, riga 2, colonna 1 | Avanzi | Terremoto, Surf, Geloraggio, Contrattacco |
| 3 | Metagross Decisa | box 12, riga 1, colonna 3 | Bendascelta (il file porta Avanzi: scambiarlo in gioco) | Meteorpugno, Terremoto, Palla Ombra, Esplosione |

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 12 e quindi non ancora una scelta: al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Swampert, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5); al posto di Metagross, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3).

<!-- generato da parco_lotta_percorso_oro.py: squadra Torre Lotta, fine -->

## 8. Dojo Lotta, Simbolo Valore

Gli stessi tre della Torre, con gli stessi strumenti, ma in un ordine diverso: Latios Timida, Metagross Decisa, Swampert Placida. Al Dojo gli esemplari si affrontano uno contro uno in sequenza, e se entrambi sopravvivono a tre turni l'incontro si decide a punti.

Il giudizio ha tre voci da due punti. La mente premia la scelta di una mossa che infligge danno, dà zero a Contrattacco, Specchiovelen e Pazienza, e toglie un punto a Protezione, Individua e Resistenza; conta la scelta e non l'esito, quindi anche una mossa impedita dalla paralisi assegna il suo punto. La tecnica premia ogni mossa andata a segno, di più se superefficace, e penalizza quelle mancate. Il corpo confronta i punti salute residui con quelli iniziali. Ne segue, come deduzione e non come regola scritta, che al Dojo conviene attaccare a ogni turno: il Calmamente del Latios e il Contrattacco dello Swampert non danno punti di mente, quindi si usano solo quando la lotta si può chiudere prima del giudizio.

La squadra, posizione per posizione, con strumenti e mosse come il gioco li mostra.

<!-- generato da parco_lotta_percorso_oro.py: squadra Dojo Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 12, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Metagross Decisa | box 12, riga 1, colonna 3 | Bendascelta (il file porta Avanzi: scambiarlo in gioco) | Meteorpugno, Terremoto, Palla Ombra, Esplosione |
| 3 | Swampert Placida | box 12, riga 2, colonna 1 | Avanzi | Terremoto, Surf, Geloraggio, Contrattacco |

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 12 e quindi non ancora una scelta: al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Metagross, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Swampert, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5).

<!-- generato da parco_lotta_percorso_oro.py: squadra Dojo Lotta, fine -->

## 9. Palazzo Lotta, Simbolo Spirito

La squadra è la sola che non condivide esemplari con le altre: Metagross Vivace dal box 12 in seconda riga e terza colonna, con la Bendascelta; Latios Lesta, seconda riga e quinta colonna, con la Baccaprugna; e Swampert Audace, terza riga e prima colonna, con gli Avanzi. Al Palazzo non si danno ordini: ogni turno l'esemplare sceglie da sé prima una categoria fra attacco, difesa e supporto, con proporzioni che dipendono dalla natura e cambiano sotto la metà dei punti salute, e poi una mossa dentro quella categoria.

Le nature sono state scelte per le quote d'attacco, e i loro profili sono diversi. Il Metagross Vivace attacca l'ottantotto per cento delle volte sopra la metà dei punti salute e crolla al ventidue sotto; il Latios Lesta fa il contrario, cinquantotto sopra e ottantotto sotto, cioè migliora quando le cose vanno male; lo Swampert Audace sta al settanta sopra la metà. Il Metagross porta due mosse sole, Meteorpugno e Terremoto, e non è una dimenticanza: quando la categoria estratta non ha mosse, metà di quella quota torna come attacco scelto a caso, quindi togliere le mosse di stato aumenta la frequenza con cui si infligge danno. L'unica decisione che resta al giocatore è l'ordine di squadra, e il primo in campo è il Metagross.

La squadra, posizione per posizione, con strumenti e mosse come il gioco li mostra.

<!-- generato da parco_lotta_percorso_oro.py: squadra Palazzo Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Metagross Vivace | box 12, riga 2, colonna 3 | Bendascelta | Meteorpugno, Terremoto |
| 2 | Latios Lesta | box 12, riga 2, colonna 5 | Baccaprugna | Psichico, Dragartigli, Fulmine, Surf |
| 3 | Swampert Audace | box 12, riga 3, colonna 1 | Avanzi | Terremoto, Surf, Geloraggio, Frana |

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 12 e quindi non ancora una scelta: al posto di Metagross, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Swampert, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5).

<!-- generato da parco_lotta_percorso_oro.py: squadra Palazzo Lotta, fine -->

## 10. Serpe Lotta, Simbolo Fortuna

In squadra: Latios Timida con la Baccaprugna, Metagross Decisa con la Bendascelta, e Blissey Sicura dal box 12 in terza riga e terza colonna con gli Avanzi. La Serpe non è un edificio di lotte ma di sale, quattordici per serie, e in ogni sala si sceglie fra tre porte con un indizio che ne nomina una sola: gli esiti sono lotte, cure, incontri selvatici, nessun evento, e la sala delle alterazioni di stato, che è quella che decide se una serie lunga sopravvive.

In quella sala un Kirlia o un Dusclops tenta di alterare un esemplare che non lo è, e le probabilità dichiarate sono iperavvelenamento il trentacinque per cento, congelamento il venticinque, paralisi il venti, sonno il dieci e scottatura il dieci. La squadra è composta su queste immunità: il Metagross è di tipo Acciaio e non può essere avvelenato, che è l'esito più probabile; la Blissey ha Alternacura, che cura l'alterazione quando esce dal campo; e la Baccaprugna del Latios ne cura una a sua volta. Le due serie più lunghe dichiarate nei thread per questo edificio, cinquecentosessanta e quattrocentoventi sale, avevano entrambe una Blissey.

La squadra, posizione per posizione, con strumenti e mosse come il gioco li mostra.

<!-- generato da parco_lotta_percorso_oro.py: squadra Serpe Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 12, riga 1, colonna 1 | Baccaprugna | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Metagross Decisa | box 12, riga 1, colonna 3 | Bendascelta (il file porta Avanzi: scambiarlo in gioco) | Meteorpugno, Terremoto, Palla Ombra, Esplosione |
| 3 | Blissey Sicura | box 12, riga 3, colonna 3 | Avanzi | Movim. Sismico, Tossina, Covauova, Canto |

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 12 e quindi non ancora una scelta: al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Metagross, Latias (box 12, riga 5, colonna 1), Tauros (box 13, riga 1, colonna 5); al posto di Blissey, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5).

<!-- generato da parco_lotta_percorso_oro.py: squadra Serpe Lotta, fine -->

## 11. Piramide Lotta, Simbolo Audacia

Gli stessi tre della Torre, senza strumenti: il gioco li toglie all'ingresso, e conviene toglierli prima di entrare e tenerli nello zaino, così che non ci sia alcun dubbio su dove finiscano. Prima di entrare vanno insegnate due mosse con le MT: Protezione, MT17, allo Swampert Placida al posto di Contrattacco, e Breccia, MT31, al Metagross Decisa al posto di Esplosione, perché in un edificio dove i punti salute non si ripristinano fra un piano e l'altro l'Esplosione si usa una volta sola. È la ragione per cui la Piramide viene per ultima.

Ogni serie di sette piani ha un bestiario a tema, e il gioco lo sostituisce per intero a ogni serie. Le squadre non cambiano, cambia chi conduce: la tabella delle prime dieci serie, con il tema, il primo in campo e il piano da cui cambiare, sta subito sotto la squadra e viene dalla guida di chi ha completato i sette simboli. Due fatti restano da sapere. Gli oggetti si raccolgono dentro, in una borsa di dieci scomparti che si conserva da una sfida all'altra solo se la sfida si completa. E Baldo, a differenza del giocatore, tiene i propri strumenti.

La squadra, posizione per posizione, con strumenti e mosse come il gioco li mostra.

<!-- generato da parco_lotta_percorso_oro.py: squadra Piramide Lotta, inizio -->

| Posto in squadra | Esemplare | Da prendere nel PC | Strumento | Mosse |
|---|---|---|---|---|
| 1 | Latios Timida | box 12, riga 1, colonna 1 | nessuno (il file porta Baccaprugna: toglierlo) | Calmamente, Psichico, Dragartigli, Fulmine |
| 2 | Swampert Placida | box 12, riga 2, colonna 1 | nessuno (il file porta Avanzi: toglierlo) | Terremoto, Surf, Geloraggio, Protezione (cambiata per la Piramide: Protezione al posto di Contrattacco) |
| 3 | Metagross Decisa | box 12, riga 1, colonna 3 | nessuno (il file porta Avanzi: toglierlo) | Meteorpugno, Terremoto, Palla Ombra, Breccia (cambiata per la Piramide: Breccia al posto di Esplosione) |

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

Riserve con piu' riscontri accanto agli altri due, dalla misura della sezione 12 e quindi non ancora una scelta: al posto di Latios, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3); al posto di Swampert, Starmie (box 12, riga 4, colonna 3), Gengar (box 12, riga 5, colonna 5); al posto di Metagross, Salamence (box 12, riga 3, colonna 5), Starmie (box 12, riga 4, colonna 3).

<!-- generato da parco_lotta_percorso_oro.py: squadra Piramide Lotta, fine -->

## 12. Le riserve, e come si usano

Le ventiquattro riserve servono a una cosa sola: sostituire un titolare quando in un edificio non rende, oppure quando si vuole provare una variante. Le due tabelle in fondo a questa sezione le misurano sulle 268 squadre estratte dai thread: la prima dice in quali edifici ciascuna specie del lotto è stata portata e con quale serie più lunga, la seconda conta, per ogni posto di ogni squadra, quali riserve hanno giocato più spesso accanto agli altri due titolari; sotto ogni squadra delle sezioni precedenti ci sono le due con più riscontri e la loro posizione nel PC. È una misura e non ancora una scelta: dice che cosa hanno fatto altri, non che cosa convenga fare qui, e va letta con tre avvertenze. I thread nominano la specie e quasi mai la natura, quindi un conteggio su Latios vale per entrambi i Latios del lotto. Un thread registra chi ha voluto scrivere, di solito chi ha fatto una serie buona, quindi il campione è sbilanciato verso i successi. E la Torre pesa quanto quasi tutti gli altri edifici insieme, quindi un numero alto alla Torre significa meno di un numero alto al Palazzo. I tre risultati più solidi sono che Salamence e Starmie sono i candidati più frequenti per quasi ogni posto, che Latias è la sostituta naturale di Latios, e che al Palazzo le riserve più presenti sono quelle da attacco puro, cioè Starmie, Salamence, Flygon e Scizor.

Una sostituzione rispetta gli stessi vincoli della squadra, e due di essi si dimenticano facilmente. Le riserve escono dal PC senza strumento, quindi lo strumento va dato prima di entrare, senza ripeterne uno già tenuto da un altro membro. E al Palazzo una riserva con mosse di stato peggiora la squadra per la ragione della sezione 9, anche se altrove sarebbe migliore.

Tyranitar non è fra le riserve: evolve da Pupitar solo al livello 55, quindi un Tyranitar di livello 50 non può esistere e le squadre dei thread che lo portano sono squadre del Livello Aperto.

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

## 13. Le schede dei trentadue esemplari

Una riga per esemplare, nell'ordine dei box. Abilità, luogo e gioco d'incontro sono letti dal dump di PKHeX del sesto giro, quindi nella grafia che il gioco mostra; i punti base usano le sigle del gioco. La colonna del margine dice quanti punti di esperienza mancano al livello 51: dove vale uno vale la prima regola della sezione 2, e nel Parco il margine non si consuma perché le lotte non danno esperienza. Lo strumento nel file è quello con cui l'esemplare esce dal PC, che per le riserve è nessuno.

<!-- generato da parco_lotta_percorso_oro.py: schede, inizio -->

| Posizione | Esemplare | Abilita' | Punti base | Mosse | Strumento nel file | Incontro | Margine al 51 |
|---|---|---|---|---|---|---|---|
| box 12, riga 1, colonna 1 | Latios Timida | Levitazione | 4 PS / 252 AttSp / 252 Vel | Calmamente, Psichico, Dragartigli, Fulmine | Baccaprugna | Isola Remota, Smeraldo, livello 50 | 1, ATTENZIONE |
| box 12, riga 1, colonna 3 | Metagross Decisa | Corpochiaro | 252 PS / 252 Att / 4 Vel | Meteorpugno, Terremoto, Palla Ombra, Esplosione | Avanzi | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 12, riga 1, colonna 5 | Slaking Decisa | Pigrone | 4 PS / 252 Att / 252 Vel | Ritorno, Terremoto, Palla Ombra, Iper Raggio | Bendascelta | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 12, riga 2, colonna 1 | Swampert Placida | Acquaiuto | 252 PS / 212 Dif / 44 AttSp | Terremoto, Surf, Geloraggio, Contrattacco | Avanzi | Percorso 117, Smeraldo, livello uovo | 7766 |
| box 12, riga 2, colonna 3 | Metagross Vivace | Corpochiaro | 252 PS / 252 Att / 4 Dif | Meteorpugno, Terremoto | Bendascelta | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 12, riga 2, colonna 5 | Latios Lesta | Levitazione | 4 PS / 252 AttSp / 252 Vel | Psichico, Dragartigli, Fulmine, Surf | Baccaprugna | Isola Remota, Smeraldo, livello 50 | 1, ATTENZIONE |
| box 12, riga 3, colonna 1 | Swampert Audace | Acquaiuto | 252 PS / 252 Att / 4 Dif | Terremoto, Surf, Geloraggio, Frana | Avanzi | Percorso 117, Smeraldo, livello uovo | 7766 |
| box 12, riga 3, colonna 3 | Blissey Sicura | Alternacura | 252 PS / 252 Dif / 4 DifSp | Movim. Sismico, Tossina, Covauova, Canto | Avanzi | Percorso 117, Smeraldo, livello uovo | 6120 |
| box 12, riga 3, colonna 5 | Salamence Decisa | Prepotenza | 4 PS / 252 Att / 252 Vel | Frana, Terremoto, Aeroassalto, Breccia | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 12, riga 4, colonna 1 | Suicune Sicura | Pressione | 252 PS / 252 Dif / 4 AttSp | Surf, Calmamente, Riposo, Sostituto | nessuno | Cupola Torre (C) / Sulfuria (XD) [110], Colosseum/XD, livello 40 | 9563 |
| box 12, riga 4, colonna 3 | Starmie Timida | Alternacura | 4 PS / 252 AttSp / 252 Vel | Psichico, Fulmine, Geloraggio, Surf | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 12, riga 4, colonna 5 | Milotic Sicura | Pelledura | 252 PS / 252 Dif / 4 AttSp | Surf, Geloraggio, Tossina, Ripresa | nessuno | Percorso 117, Smeraldo, livello uovo | 6324 |
| box 12, riga 5, colonna 1 | Latias Calma | Levitazione | 252 PS / 60 Dif / 12 DifSp / 180 Vel | Schermoluce, Riflesso, Tossina, Psichico | nessuno | Isola Remota, Smeraldo, livello 50 | 1, ATTENZIONE |
| box 12, riga 5, colonna 3 | Snorlax Cauta | Grassospesso | 168 PS / 120 Dif / 220 DifSp | Maledizione, Ritorno, Riposo, Terremoto | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 12, riga 5, colonna 5 | Gengar Timida | Levitazione | 4 PS / 252 AttSp / 252 Vel | Fulmine, Gelopugno, Fuocopugno, Destinobbligato | nessuno | Percorso 117, Smeraldo, livello uovo | 7766 |
| box 13, riga 1, colonna 1 | Zapdos Modesta | Pressione | 252 PS / 252 AttSp / 4 DifSp | Fulmine, Perforbecco, Riposo, Sonnolalia | nessuno | Centrale Elett., Rosso Fuoco, livello 50 | 1, ATTENZIONE |
| box 13, riga 1, colonna 3 | Registeel Cauta | Corpochiaro | 252 PS / 244 Att / 4 Dif | Ferrartigli, Sostituto, Maledizione, Amnesia | nessuno | Tomba Antica, Smeraldo, livello 40 | 9563 |
| box 13, riga 1, colonna 5 | Tauros Allegra | Prepotenza | 4 PS / 252 Att / 252 Vel | Ritorno, Terremoto, Sdoppiatore, Codacciaio | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 13, riga 2, colonna 1 | Flygon Allegra | Levitazione | 4 PS / 252 Att / 252 Vel | Terremoto, Frana, Dragartigli, Protezione | nessuno | Percorso 117, Smeraldo, livello uovo | 7766 |
| box 13, riga 2, colonna 3 | Raikou Timida | Pressione | 4 PS / 252 AttSp / 252 Vel | Fulmine, Calmamente, Sostituto, Riposo | nessuno | Cupola Torre (C) / Sulfuria (XD) [113], Colosseum/XD, livello 40 | 9563 |
| box 13, riga 2, colonna 5 | Gyarados Decisa | Prepotenza | 4 PS / 252 Att / 252 Vel | Ritorno, Terremoto, Dragodanza, Riposo | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 13, riga 3, colonna 1 | Heracross Allegra | Aiutinsetto | 4 PS / 252 Att / 252 Vel | Megacorno, Breccia, Frana, Terremoto | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 13, riga 3, colonna 3 | Aerodactyl Decisa | Testadura | 4 PS / 252 Att / 252 Vel | Frana, Terremoto, Aeroassalto, Sdoppiatore | nessuno | Percorso 117, Smeraldo, livello uovo | 9563 |
| box 13, riga 3, colonna 5 | Moltres Timida | Pressione | 220 PS / 52 Dif / 236 Vel | Lanciafiamme, Tossina, Sostituto, Protezione | nessuno | Monte Brace, Rosso Fuoco, livello 50 | 1, ATTENZIONE |
| box 13, riga 4, colonna 1 | Articuno Calma | Pressione | 220 PS / 60 DifSp / 228 Vel | Geloraggio, Tossina, Sostituto, Protezione | nessuno | Isole Spumarine, Rosso Fuoco, livello 50 | 1, ATTENZIONE |
| box 13, riga 4, colonna 3 | Magneton Modesta | Magnetismo | 80 Dif / 252 AttSp / 176 Vel | Fulmine, Resistenza, Ferrostrido, Introforza | nessuno | Percorso 117, Smeraldo, livello uovo | 7651 |
| box 13, riga 4, colonna 5 | Regice Modesta | Corpochiaro | 168 PS / 148 Dif / 100 AttSp / 92 DifSp | Geloraggio, Fulmine, Riposo, Sonnolalia | nessuno | Grotta Insulare, Smeraldo, livello 40 | 9563 |
| box 13, riga 5, colonna 1 | Scizor Decisa | Aiutinsetto | 20 PS / 236 Att / 252 Vel | Alacciaio, Aeroassalto, Danzaspada, Sostituto | nessuno | Percorso 117, Smeraldo, livello uovo | 7651 |
| box 13, riga 5, colonna 3 | Dusclops Sicura | Pressione | 252 PS / 252 Dif / 4 DifSp | Maledizione, Sostituto, Protezione, Malcomune | nessuno | Percorso 117, Smeraldo, livello uovo | 6120 |
| box 13, riga 5, colonna 5 | Steelix Decisa | Testadura | 132 PS / 252 Att / 120 DifSp / 4 Vel | Terremoto, Esplosione, Tossina, Frana | nessuno | Percorso 117, Smeraldo, livello uovo | 7651 |
| box 14, riga 1, colonna 1 | Marowak Allegra | Testadura | 4 PS / 252 Att / 252 Vel | Terremoto, Frana, Sdoppiatore, Danzaspada | nessuno | Percorso 117, Smeraldo, livello uovo | 7651 |
| box 14, riga 1, colonna 3 | Regirock Decisa | Corpochiaro | 252 PS / 252 Att / 4 Dif | Frana, Terremoto, Maledizione, Esplosione | nessuno | Rovine Sabbiose, Smeraldo, livello 40 | 9563 |

<!-- generato da parco_lotta_percorso_oro.py: schede, fine -->

## 14. La disposizione completa dei box 12, 13 e 14

Tutte le sessantaquattro posizioni, riga per riga, contando dall'alto a sinistra. La copia 1 si usa, la copia 2 è quella per lo scambio.

<!-- generato da parco_lotta_percorso_oro.py: disposizione, inizio -->

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

<!-- generato da parco_lotta_percorso_oro.py: disposizione, fine -->

## 15. Che cosa questa guida non sa

Nessuna di queste squadre è stata ancora provata in partita su questa cartuccia. Sono composte su ciò che ha funzionato ad altri e su vincoli verificati nel sorgente, che è il massimo che si possa fare prima di giocare. La scelta delle riserve per edificio è ancora da scrivere, sopra la misura che esiste. Gli ordini di conduzione della Piramide oltre la decima serie sono calcolati e non tratti da una fonte, e servono solo oltre il simbolo d'oro. Quando una serie si perde, il punto in cui si è persa e contro chi è l'informazione che serve per correggere la squadra, e vale la pena annotarla.
