# STUDIO-04. Il Parco Lotta, i sette simboli d'oro, e la squadra che li vince

> Aperto il 2026-09-21 in attuazione di ADR-067. Riguarda la stessa cartuccia reale di Pokemon Smeraldo italiano, allenatore ALEX, identificativo 45761, identificativo segreto 56446, su cui `STUDIO-01` ha corretto l'inventario e `STUDIO-03` ha scritto i flag delle isole. Non tratta il salvataggio ma ciò che ci si vuole fare dentro, ed è quindi il primo studio di questa cartuccia il cui esito non è una scrittura ma una partita: la scrittura viene dopo, e serve soltanto a mettere in mano al giocatore gli esemplari che la partita richiede.
>
> Questo documento è aperto e incompleto per dichiarazione. Alla data di apertura sono state lette le sole fonti di primo livello, cioè le nove pagine Bulbapedia e il database dello strumento `DomeAssistantWeb`; le circa trenta fonti Smogon registrate in `SOURCES.md` non sono state lette, e ciò che ne discenderà non è ancora qui. Le sezioni che seguono dichiarano ciascuna su quale fonte poggiano, così che la parte misurata resti distinguibile da quella ancora da misurare.

## 1. L'obiettivo, e perché non è un obiettivo solo

L'utente ha dichiarato un obiettivo in forma breve, i sette simboli d'oro, che a leggerlo come una cosa sola produce il piano sbagliato. I sette edifici del Parco Lotta non sono sette gradini della stessa scala: sono sette giochi diversi che condividono il solo vincolo di iscrizione, e in tre di essi la squadra che si porta conta meno di quanto si creda. Alla Fabbrica Lotta non si porta nulla, perché si combatte con esemplari presi in prestito; al Palazzo Lotta si porta una squadra ma non si scelgono le sue mosse, che le sceglie la natura; alla Piccozza Lotta si combatte contro ciò che le stanze estraggono a sorte, e il criterio di sopravvivenza non è la potenza ma la resistenza a un ventaglio di effetti.

Ne segue che l'unità di lavoro non è la squadra ma la coppia edificio-squadra, e che una squadra sola per tutti e sette è un'ipotesi da verificare invece che un punto di partenza. La sezione 5 raccoglie i vincoli che valgono ovunque, che sono pochi; le sezioni successive raccolgono quelli specifici, che sono molti e divergenti.

## 2. Che cosa è stato letto, e che cosa no

La lettura delle fonti segue la disclosure progressiva prescritta da `token-economy.md`, quindi non tutto ciò che è stato scaricato è stato letto, e la distinzione va tenuta.

Le nove pagine Bulbapedia sul Parco Lotta sono state scaricate per intero il 2026-09-21 con `tools/fetch-bulbapedia.py`, per la via dell'API MediaWiki, che è il canale programmatico che il servizio espone senza credenziali. Sono 7120 righe di wikitesto, con lo scheletro di Livello 1 in `_notes/fonti/bulbapedia-parco-lotta-2026-09-21/_INDEX.md` e il grezzo accanto, ciascuna pagina con la propria revisione e il momento della lettura nell'intestazione. Di queste, alla data di apertura dello studio, sono state lette in profondità le sezioni sui vincoli generali, sulle soglie degli Assi, sul comportamento per natura del Palazzo Lotta e sul calcolo delle statistiche alla Fabbrica Lotta. Il resto è su disco e non in questo documento.

Il database dello strumento `DomeAssistantWeb`, licenza MIT, è stato scaricato dal suo deposito GitHub nella sola parte dei dati, cioè gli otto file sotto `data/`, in `_notes/fonti/domeassistant-2026-09-21/grezzo/`. Vale più della pagina Bulbapedia degli allenatori perché non è una descrizione degli avversari ma la loro tabella: 888 insiemi distinti di esemplare, con natura, strumento, quattro mosse e distribuzione dei punti base, su 376 specie, distribuiti in 130 formazioni fra 302 allenatori. È il materiale su cui si progetta contro un avversario reale invece che contro un'idea di avversario, e non è ancora stato spogliato.

Il foglio `EmeraldBattleFrontierComplete.xlsx` è stato letto nello stesso giorno, dopo una diagnosi sbagliata che vale registrare perché è il genere di errore che manda a chiedere una cosa a una persona invece di andarsela a prendere. L'indirizzo registrato in `SOURCES.md` restituiva la pagina di accesso al servizio, e la deduzione fu che gli mancasse il parametro `rlkey` che i collegamenti recenti di quel servizio richiedono: plausibile e falsa. Risalendo al post Smogon che lo pubblica, che è leggibile senza credenziali, l'indirizzo vero è risultato di forma diversa e con un identificativo diverso, cioè un collegamento inesistente e non un collegamento monco. La regola che ne discende vale oltre il caso: quando un collegamento non risponde, prima di dedurre che cosa gli manchi si torna al documento che lo pubblica.

Il foglio vale l'insistenza, perché non duplica il database dello strumento ma lo completa su tre colonne che quello non ha. Porta le abilità possibili di ciascun insieme, le statistiche già calcolate sia a livello 100 sia a livello 50, che è il livello a cui questa squadra si progetta, e i punti individuali fissi dei soli Assi del Parco. Sta in `_notes/fonti/smogon-maxstats-2026-09-21/`, con accanto la versione in testo semplice dello stesso contenuto, 1228 righe su due tabelle.

## 3. I vincoli di iscrizione, verificati due volte

I vincoli che valgono in tutti e sette gli edifici sono tre, e vanno fissati prima di qualunque scelta perché scartano squadre intere.

Nessun esemplare iscritto può appartenere alla stessa specie di un altro, e nessuno può tenere lo stesso strumento di un altro. Gli strumenti dello zaino non si usano durante la lotta, con la sola eccezione della Piramide Lotta, dove si attinge a una borsa dedicata raccolta dentro l'edificio stessa. Le lotte non assegnano esperienza né denaro, e ogni strumento guadagnato o perduto durante la sfida viene ripristinato alla fine.

L'elenco delle specie escluse è chiuso e conta dieci voci più l'uovo: Mewtwo, Mew, Lugia, Ho-Oh, Celebi, Kyogre, Groudon, Rayquaza, Jirachi e Deoxys. Il fatto è verificato due volte per vie indipendenti, ed è la ragione per cui si può dare per fermo: Bulbapedia lo elenca nella sezione dei vincoli della pagina generale, e `STUDIO-02` sezione 5 lo aveva già verificato sul sorgente di `pret/pokeemerald`, dove `src/frontier_util.c` dichiara l'array `gFrontierBannedSpecies[]` con esattamente quelle dieci specie. Le due liste coincidono voce per voce.

Ne discendono due conseguenze pratiche che vale enunciare perché toccano il lavoro appena chiuso e quello che si sta aprendo. La prima è che Mew, Lugia e Ho-Oh, resi incontrabili sulla cartuccia dal quinto giro di `STUDIO-03` e verificati in gioco dall'utente, sono per costruzione inutilizzabili qui: sono due lavori che non si toccano. La seconda è che Latios e Latias non sono nell'elenco, quindi il Latios che l'utente ha già scelto per la propria squadra è iscrivibile, e lo sono anche i tre cani leggendari e i tre Regi, come `STUDIO-02` aveva già osservato distinguendo Rayquaza da Entei e Suicune.

## 4. Il calendario degli Assi, cioè quanto costa ciascun simbolo

L'Asso di ciascun edificio compare due volte, e il simbolo d'oro è la seconda. Le soglie sono state estratte dalle schede informative delle sette pagine con `gba-save-extraction-smeraldo/tools/parco_lotta_estrai_tabelle.py`, e stanno in `_notes/fonti/bulbapedia-parco-lotta-2026-09-21/derivato/assi-soglie.json`. Si leggono come numero di serie vinte prima della comparsa, dove una serie vale sette lotte in tutti gli edifici tranne il Torneo Lotta, che ne vale quattro.

| Edificio | Asso | Simbolo | Serie per l'argento | Serie per l'oro |
|---|---|---|---|---|
| Fabbrica Lotta | Factory Head Noland | Conoscenza | 3 | 6 |
| Arena Lotta | Arena Tycoon Greta | Tenacia | 4 | 8 |
| Torneo Lotta | Dome Ace Tucker | Tattica | 5 | 10 |
| Piccozza Lotta | Pike Queen Lucy | Fortuna | 2 | 10 |
| Palazzo Lotta | Palace Maven Spenser | Spirito | 3 | 6 |
| Piramide Lotta | Pyramid King Brandon | Coraggio | 3 | 10 |
| Torre Lotta | Salon Maiden Anabel | Abilità | 5 | 10 |

Il dato che questa tabella rende visibile, e che una lettura a edificio per edificio non avrebbe fatto emergere, è che i sette simboli non costano lo stesso e che la distanza fra argento e oro varia molto. Alla Piccozza Lotta l'argento arriva prestissimo, dopo due sole serie, e l'oro otto serie dopo: è l'edificio con il divario più ampio fra i due, ed è anche quello dove l'utente ha già l'argento, perché il quarto giro di correzione ha riportato il simbolo da oro ad argento apposta per riconquistarlo legittimamente, come registrato in `STUDIO-02` sezione 5. Fabbrica e Palazzo sono invece i due più economici in assoluto, sei serie all'oro, e sono anche i due in cui la squadra costruita conta meno: alla Fabbrica non si porta, al Palazzo non si comanda. È un ordine di attacco suggerito dai numeri, non una preferenza.

## 5. Il Palazzo Lotta, dove la natura è il giocatore

Il Palazzo Lotta merita una sezione propria prima degli altri edifici perché è il solo punto del Parco in cui la natura di un esemplare smette di essere una modifica alle statistiche e diventa il suo comportamento, e perché è il vincolo che una squadra copiata da un forum viola quasi sempre senza accorgersene, essendo quelle squadre pensate per la Torre.

La meccanica è questa. Ogni mossa appartiene a una di tre categorie. Sono di difesa tutte quelle che bersagliano chi le usa, la propria metà del campo o il campo intero, con l'esclusione delle mosse che ne richiamano altre; sono di supporto tutte quelle che non infliggono danno e non sono di difesa, più Contatore e Zuffa; sono di attacco tutte le altre. A ogni turno il gioco sceglie prima una categoria, con proporzioni che dipendono dalla natura, e solo dopo sceglie una mossa dentro quella categoria. Le proporzioni cambiano quando i punti salute scendono sotto la metà. Se l'esemplare non possiede alcuna mossa della categoria estratta, ne sceglie una a caso fra le proprie, ma con probabilità una su due non fa nulla per quel turno, e il gioco lo dichiara incapace di usare la propria forza.

Le proporzioni delle venticinque nature sono state estratte dal wikitesto con lo stesso strumento e stanno in `_notes/fonti/bulbapedia-parco-lotta-2026-09-21/derivato/palazzo-nature.json`, con la verifica che ciascuna sommi a cento sopra e sotto la metà dei punti salute. Vale registrare l'inciampo dell'estrazione perché è il genere di difetto che passa una revisione a video: l'ultima riga della tabella, quella della natura Vivace, porta nel wikitesto lo stile che arrotonda l'angolo del riquadro e si presenta quindi in una forma diversa dalle altre ventiquattro. Un lettore che riconoscesse la sola forma nuda perderebbe esattamente una natura, in silenzio, sull'ultima riga, cioè dove nessuno controlla; il primo giro dell'estrattore ne ha infatti restituite ventiquattro. Il presidio adottato non è aver corretto l'espressione regolare ma aver trasformato il conteggio in un'asserzione che ferma lo strumento, perché la correzione vale per questa forma della tabella e l'asserzione vale per tutte le altre.

Due letture di quei numeri cambiano la progettazione. La prima è che la natura migliore per attaccare al Palazzo non è nessuna di quelle che si userebbero altrove: è Precipitosa, che sceglie l'attacco il cinquantotto per cento delle volte sopra la metà dei punti salute e l'ottantotto sotto, cioè l'unica che migliora invece di peggiorare quando le cose vanno male. Sassy sceglie l'attacco l'ottantotto per cento delle volte sopra la metà ma crolla al ventidue sotto, che è il profilo opposto e molto peggiore, perché la seconda metà della lotta è quella che si perde. La seconda è che sei nature si comportano in modo identico sopra e sotto la metà, cioè Ardita, Docile, Ingenua, Quieta, Timida nel senso di Bashful e Vivace, e fra queste Ardita è la più aggressiva con il sessantuno per cento costante: sono le nature prevedibili, che è una qualità qui e non altrove.

Applicate alla squadra che l'utente ha già indicato in `pending.md`, queste proporzioni danno un esito che va detto adesso invece che dopo averla costruita. Lo Slaking di natura Allegra sceglie una mossa d'attacco il trentacinque per cento delle volte sopra la metà dei punti salute e il trentacinque sotto, con il sessanta per cento speso in difesa quando è ferito: al Palazzo è quasi inservibile, e non per debolezza propria ma perché rifiuta di attaccare. Il Milotic Ardito sta al trenta e al trentadue, il Metagross Deciso al trentotto e al settanta, il Latios e lo Starmie Timidi al sessantadue e al trenta. Ne segue che la squadra dell'utente, così com'è, è una squadra per la Torre e per l'Arena, non per il Palazzo, e che il Palazzo richiede una seconda selezione con nature scelte per il proprio comportamento. Non è una critica alla squadra ma la conferma che l'unità di lavoro è la coppia edificio-squadra.

## 6. La Fabbrica Lotta, dove la squadra non si porta

Alla Fabbrica Lotta non si iscrive la propria squadra: si sceglie fra esemplari in prestito, e si può scambiare un proprio esemplare in prestito con uno dell'avversario appena battuto. Il valore del proprio deposito è quindi nullo qui, e ciò che conta è il criterio di scelta e di scambio. La conseguenza per questo progetto è che la Fabbrica è l'unico dei sette simboli d'oro che non dipende in alcun modo dalla scrittura nei box, e che può quindi essere affrontato subito, prima che qualunque generatore esista.

Un dato misurato che serve al criterio: gli esemplari offerti hanno punti individuali uniformi su tutte le statistiche, e il loro valore dipende dalla serie in corso, salendo per gradi di tre, cioè 3 alla prima serie, 6 alla seconda, 9 alla terza, 12 alla quarta, 15 alla quinta, 21 alla sesta e 31 dalla settima in poi. L'ultimo allenatore di ogni serie, con l'eccezione di Noland, usa una tabella diversa e più generosa: 6, 9, 12, 15, 18 e poi 31 dalla sesta. Bulbapedia registra inoltre un difetto per cui alla nona serie gli esemplari iniziali ricevono punti individuali casuali invece dei 31 attesi, e un secondo effetto per cui scegliere di riposare, salvare e ricaricare porta tutti i punti individuali di ciascun esemplare al valore del suo punto individuale di Attacco. Entrambi sono registrati qui come letti su Bulbapedia e non ancora verificati sul sorgente, e vanno marcati DA VERIFICARE finché non lo saranno, perché il secondo in particolare è azionabile e sarebbe grave usarlo sulla fiducia.

## 7. Gli altri cinque edifici

Sezione aperta e non scritta. Le pagine di Arena, Torneo, Piccozza, Piramide e Torre sono su disco e il loro scheletro è nell'indice di Livello 1; le loro meccaniche non sono ancora state portate qui perché la lettura in profondità di questa prima sessione si è fermata ai vincoli generali, alle soglie e ai due edifici che più cambiano la progettazione della squadra. Dell'Arena Lotta è già stato letto il criterio di giudizio in tre voci, mente, tecnica e corpo, che premia chi sceglie mosse offensive, chi colpisce con efficacia superiore e chi conserva i punti salute, e penalizza Protezione, Individua e Resistenza: è un criterio che riscrive le mosse di una squadra difensiva, e va sviluppato quando si scriverà la sezione.

Della Piccozza Lotta vale ricordare che `STUDIO-02` sezione 5 e sezione 10 hanno già fatto il lavoro di stato, cioè riportare il simbolo ad argento e azzerare il record di serie, e che quel contenuto non va duplicato qui: questo studio lo riprende soltanto per progettare la squadra, non per rifare la diagnosi.

## 8. Le due fasi che ADR-067 prescrive, e dove siamo

La decisione architetturale prevede due fasi. La prima è una pipeline sintetica separata, che riusa `pokebridge/gen3.py` e `parco_amici.py` con i punti potere massimizzati, e che produce gli esemplari in software per poterli studiare. La seconda è la scrittura di una selezione nei box della cartuccia vera, per poterci giocare davvero, ed è un tipo di scrittura mai eseguito finora su questo salvataggio: nessuno degli strumenti esistenti sotto `gba-save-extraction-smeraldo/tools/` scrive la struttura di un esemplare, perché tutti finora hanno scritto flag, voci di inventario o riordini di deposito. Va costruita e verificata da zero, con la stessa disciplina delle altre, cioè backup in doppia copia prima, read-back verificato dopo.

Alla data di apertura di questo studio nessuna delle due fasi è iniziata, e la ragione è dichiarata: si legge abbastanza da sapere cosa generare prima di costruire il generatore. Gli strumenti scritti finora per questo fronte sono soltanto due, e sono di lettura: `tools/fetch-bulbapedia.py` e `gba-save-extraction-smeraldo/tools/parco_lotta_estrai_tabelle.py`.

## 9. Il lavoro aperto, in ordine

Spogliare il database dei 888 insiemi avversari e ricavarne le distribuzioni che contano, cioè quali specie ricorrono di più ai livelli alti, quali strumenti, quali mosse di stato: è il materiale contro cui la squadra va progettata, ed è già su disco in due forme indipendenti, il database dello strumento e il foglio Smogon, che vanno confrontate l'una contro l'altra prima di fidarsi di entrambe.

Leggere in profondità le cinque pagine di edificio rimaste e scrivere la sezione 7.

Leggere le fonti Smogon, che richiedono accesso autenticato e vanno quindi affrontate per la via di `claude-in-chrome` con l'utente che immette le proprie credenziali, o per consegna manuale del contenuto: le credenziali non si scrivono in alcun file di questo progetto.

Decidere, e non assumere, il criterio di legittimità a livello 50 per gli esemplari da generare, che è il dubbio che `pending.md` aveva già lasciato aperto insieme alla riorganizzazione dei box necessaria a far posto alla squadra e alle sue copie doppie.
