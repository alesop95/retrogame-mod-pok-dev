# STUDIO-05. Le squadre del Parco Lotta, l'ordine in cui affrontarlo, e lo spazio che serve nei box

> Aperto il 2026-09-21 in attuazione di ADR-068, subito dopo che la lettura integrale delle fonti ha chiuso il debito documentale descritto in `STUDIO-04`. È il primo documento di questo fronte il cui esito non è una misura ma una proposta: le squadre qui sotto sono scelte, e una scelta si discute. Il catalogo in forma di dati è `squadre-parco-lotta.json`, la sua verifica meccanica la fa `tools/parco_lotta_valida_squadre.py`, e il piano dei box che ne esce è `PIANO-BOX.md`, rigenerato e non scritto a mano.
>
> Il rapporto fra i tre documenti va tenuto fermo perché è la ragione per cui esistono separati. `STUDIO-04` dice contro che cosa si combatte e con quali regole, ed è misura. Questo dice che cosa portare, ed è scelta. Il file di dati è la scelta in forma verificabile, cosicché una modifica fatta fra sei mesi non possa violare in silenzio un vincolo che nessuno ricorda più.

## 1. L'ordine di attacco, che viene dai difetti e non dalle preferenze

I sette simboli non si affrontano nell'ordine in cui l'obiettivo li elenca, e nemmeno in quello del costo in lotte. L'ordine discende da tre fatti verificati sul sorgente e registrati nella sezione 12 di `STUDIO-04`, e due di essi sono vincoli di sequenza, cioè scelte che non si recuperano dopo.

La Cupola Lotta va per prima. I suoi avversari hanno tre punti individuali su ogni statistica a qualunque punto della serie, per il difetto di `CreateDomeOpponentMon`; si vede la squadra avversaria prima di scegliere quali due dei tre iscritti mandare in campo; e il simbolo costa quaranta lotte, il minimo del Parco. Tre ragioni indipendenti che convergono sullo stesso edificio, ed è raro.

L'Azienda Lotta va subito dopo, e la ragione è un vincolo che si perde una volta sola. I punti individuali dei suoi avversari non dipendono dalla serie all'Azienda ma dalla serie corrente alla Torre Lotta a livello 50: finché quella resta bassa, all'Azienda si affrontano avversari al primo gradino; se si costruisce prima una serie lunga alla Torre, all'Azienda si trovano avversari a trentuno punti individuali dalla prima serie. Poiché l'Azienda non chiede alcun esemplare generato, perché vi si combatte con esemplari in prestito, i primi due simboli d'oro si possono cominciare prima che la pipeline di generazione esista.

Gli altri cinque seguono in ordine di costo crescente e di rischio crescente, cioè Torre, Dojo, Palazzo, Serpe e Piramide. Non è un ordine obbligato come i primi due e si può cambiare; è però l'ordine in cui la squadra costruita si mette alla prova su regole sempre più divergenti da quelle ordinarie, il che è un modo sensato di scoprire un difetto di composizione prima che costi una serie lunga.

## 2. Perché otto esemplari e non trentatré, e la proposta di emendare ADR-068

ADR-068 stabilisce una squadra per edificio e, alla Piramide Lotta, una per giro. Applicata alla lettera, quella decisione chiede cinque squadre di tre più fino a undici squadre di tre per la Piramide, cioè quarantotto esemplari e novantasei slot considerando la doppia copia. La lettura delle fonti ha mostrato che il fabbisogno vero è molto minore, e la ragione è di merito e non di economia: sarebbe stato sbagliato generare trentatré esemplari per la Piramide anche se lo spazio fosse stato infinito.

La guida di chi ha completato tutti e sette i simboli affronta i dieci giri della Piramide con tre esemplari soli, e ciò che cambia da un giro all'altro non è la composizione ma la conduzione, cioè quale dei tre mandare per primo e a quale piano sostituirlo. La ragione sta nel bestiario: i venti gruppi della Piramide sono tematici, e un tema si batte scegliendo quale dei propri esemplari gli è avvantaggiato, non costruendone uno nuovo. Contro il giro del tipo Roccia si conduce lo Swampert e si passa al Metagross dal terzo piano; contro il giro del tipo Psico si conduce il Latios e si passa al Metagross dal secondo. La tabella completa dei dieci ordini sta nel catalogo e in `PIANO-BOX.md`.

La proposta è quindi di emendare ADR-068 sul solo punto della Piramide: non dieci squadre ma una squadra e dieci ordini di conduzione, dichiarati. È una decisione dell'utente e non dell'agente, perché restringe l'ambito che l'utente aveva fissato, e qui si segnala invece di essere applicata in silenzio. Il resto di ADR-068 resta intatto: gli altri sei edifici hanno ciascuno la propria squadra, e il Palazzo Lotta in particolare ne ha una che non condivide alcun esemplare con le altre.

Ne segue il numero: otto esemplari distinti, sedici slot con la doppia copia, meno di un box su quattordici. Contro i novantasei della lettura letterale.

## 3. Le sei squadre, con la fonte di ciascuna scelta

Alla Cupola Lotta si portano Latios, Metagross e Slaking. Lo Slaking entra qui e in nessun altro edificio, ed è la conseguenza diretta del difetto dei punti individuali: contro avversari fermi a tre, la sua potenza arriva a termine prima che il turno perso dall'abilità Pigrizia si paghi, e la scelta è corroborata dal fatto che Slaking compare sette volte nelle diciannove squadre da Cupola estratte dai thread. La natura è Adamant e non Allegra come nel materiale di partenza, perché contro avversari deboli la velocità vale meno della potenza.

Alla Torre Lotta e al Dojo Lotta si portano gli stessi tre, cioè Latios, Swampert e Metagross, che è la squadra della guida al completamento ed è anche il nucleo che ricorre in testa a tutte e quattro le liste per edificio ricavate dai thread. Al Dojo il vincolo aggiuntivo è negativo invece che positivo: il criterio di giudizio sottrae un punto a Protezione, Individua e Resistenza, quindi lo Swampert vi porta Contatore e non Protezione. È una sostituzione di mossa sullo stesso esemplare e non un esemplare diverso, e lo strumento di verifica la modella così apposta, perché trattarla come un esemplare nuovo raddoppierebbe lo spazio nei box senza alcuna ragione.

Al Palazzo Lotta si porta la sola squadra che non condivide alcun esemplare con le altre, ed è anche la sola ragione per cui gli esemplari distinti sono otto e non cinque. Le nature sono Sassy per il Metagross, Precipitosa per il Latios e Brave per lo Swampert, che sono le tre con le quote d'attacco più alte fra quelle utilizzabili su quelle specie, e la squadra è quella dichiarata a duecentoventiquattro da tre persone diverse. Il Metagross porta due mosse sole, entrambe d'attacco, e non è una dimenticanza: al Palazzo la quota della categoria mancante torna per metà come attacco, quindi togliere le mosse di stato aumenta la frequenza con cui si infligge danno. È il terzo difetto della sezione 12 di `STUDIO-04`, ed è il punto in cui la progettazione ovvia sbaglia con più sicurezza.

Alla Serpe Lotta si porta Blissey al posto dello Swampert, ed è la sola specie di tutto il catalogo che non veniva dal materiale dell'utente. Compare nelle due serie più lunghe dichiarate per quell'edificio, cioè cinquecentosessanta e quattrocentoventi sale, e la ragione è la natura della sfida: là non si vince infliggendo danno ma sopravvivendo a quattordici sale di cui una sola classe è pericolosa, cioè quella delle alterazioni di stato. Il Metagross vi resta perché è di tipo Acciaio e quindi immune all'iperavvelenamento, che con il trentacinque per cento è l'alterazione più probabile di quella stanza.

Alla Piramide Lotta si portano gli stessi tre della Torre senza alcuno strumento, perché il gioco glieli toglie all'ingresso, e con due sostituzioni di mossa: Protezione al posto di Contatore sullo Swampert, e Breccia al posto di Autodistruzione sul Metagross, che in un edificio dove i punti salute non si ripristinano fra un piano e l'altro è una mossa che si usa una volta sola.

## 4. Lo spazio nei box, e che cosa va deciso prima di generare

Sedici slot su quattrocentoventi non sono un problema di capienza, e la domanda sulla riorganizzazione dei box, aperta in `pending.md` dal 2026-09-17, si ridimensiona di conseguenza: non serve liberare spazio in generale, serve destinare un box a questo scopo e sapere quale. Resta però da leggere quanto i box di questa cartuccia siano occupati oggi e se esista già un box quasi vuoto, perché la scrittura che ADR-067 prevede è la prima di questo progetto che tocca la struttura di un esemplare e conviene che atterri dove non c'è nulla da spostare.

Due cose vanno invece decise prima di generare, e sono dell'utente.

La prima è il criterio di legittimità a livello 50, che `pending.md` tiene aperto da settembre e che questo studio non chiude perché non gli compete: questi esemplari non attraverseranno mai Pokemon Home, come ADR-067 stabilisce, ma il criterio con cui si dichiarano legittimi sulla cartuccia resta una scelta dichiarata.

La seconda è se emendare ADR-068 sul punto della Piramide, come la sezione 2 propone.

## 5. Che cosa resta aperto, e che cosa questo documento non verifica

Lo strumento di verifica controlla i vincoli del Parco e non la legalità del gioco: non sa se una mossa sia imparabile dalla specie a cui è attribuita, perché la tabella degli insiemi di mosse per specie non è ancora su disco in questo progetto. Dichiararlo fatto sarebbe peggio che non farlo, quindi il controllo si lascia alla fase di generazione, dove quella tabella serve comunque. L'unico caso già noto è registrato come eccezione esplicita nello strumento, cioè Megahorn su Heracross, che in Smeraldo non è una macchina ma una mossa di livello appresa al cinquantatre; Heracross non entra in nessuna delle sei squadre qui proposte, quindi il vincolo oggi non morde, ma resta scritto per quando lo farà.

Restano fuori dal catalogo, e non per dimenticanza, gli esemplari del materiale di partenza che nessuna delle sei squadre impiega: Milotic, Starmie, Gengar, Salamence, Suicune, Snorlax e Heracross. Non sono scelte sbagliate ed è verosimile che alcuni rientrino quando una serie si rompe e la squadra va corretta; semplicemente non c'è ragione di generarli adesso, e generarli adesso significherebbe scrivere nei box sedici esemplari in più senza sapere se serviranno. Il catalogo è un file di dati proprio perché aggiungerne uno domani costi una riga.
