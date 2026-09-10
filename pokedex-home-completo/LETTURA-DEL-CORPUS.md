# La lettura del corpus, cluster per cluster

Registro della lettura integrale del corpus della collezione, chiesta dall'utente il 2026-09-09 con la prescrizione che tutto vada letto prima di aprire altro lavoro di produzione. Non è un censimento generato: è un documento autorato che cresce a lotti, e ogni voce dice che cosa il cluster ha aggiunto, che cosa ha corretto e che cosa resta non letto con il motivo.

La misura del compito, fissata all'inizio perché serve a valutare l'avanzamento: il corpus scaricato è di duecentonovantadue documenti per sei milioni e duecentomila byte, distribuiti su quarantadue cluster più il preambolo e i commenti al post di raccolta. Il conto delle fonti registrate è centosettantuno, e le pagine non scaricate restano dichiarate come tali nel censimento generato.

## Lo stato, aggiornato a ogni lotto

| Cluster | Fonti | Stato | Dove sta l'esito |
|---|---|---|---|
| 2) What are we loosing with Pokemon Bank | 6 | letto il 2026-09-08 | `STUDIO-05` e `INDICE-FOGLI-ESTERNI.md` |
| 1) Dex completions / Overall lists for multiple generations | 10 | letto il 2026-09-08 | `STUDIO-06` |
| 9) RNG Manipulation and Glitches / RNG Manipulation - the best sources to start, 9) RNG Manipulation and Glitches / Item Printer Gen 9, 9) RNG Manipulation and Glitches / Glitches, 9) RNG Manipulation and Glitches / 8F for Gen 1 games, 9) RNG Manipulation and Glitches / Coin Case Glitch for Gen 2 games, 9) RNG Manipulation and Glitches / ACE coding in Gen 2 & Gen 3 | 17 | letto il 2026-09-09 | `STUDIO-08` |
| 6) How to still get Bank and other games/ 3DS modding | 4 | letto il 2026-09-09 | `STUDIO-09` e questa nota |
| 5) Other lists and spreadsheets | 6 | letto il 2026-09-09, due voci non recuperabili | `ID-NOTEVOLI.md` e questa nota |
| 4) Ribbon Master | 3 | letto il 2026-09-09, il manuale resta da recuperare | questa nota |
| 3) Collections of one Pokemon species | 6 | letto il 2026-09-09 | questa nota |
| 1) Dex completions / Gen 1, 1) Dex completions / Gen 2, 1) Dex completions / Gen 3 | 16 | letti il 2026-09-09, meno le tre voci in forma di video | questa nota |
| 1) Dex completions / Gen 4 | 7 | letto il 2026-09-09 nelle voci decisive, e chiude il punto sulle rovine di Sinjoh | questa nota e `pending.md` |
| 1) Dex completions / Pokemon Collection Trackers | 7 | letto il 2026-09-10, cinque voci su sette | `CONFRONTO-LIVINGDEX-POKEPC.md` e questa nota |
| 1) Dex completions, 1) Dex completions / Reddit | 5 | letti il 2026-09-10, meno le due voci in forma di video e la pagina non scaricata | questa nota |

Il nome di un cluster in questa tabella deve essere esattamente quello del censimento, e più nomi si separano con la virgola: è la chiave con cui `tools/indice-fonti-unico.py` porta lo stato di lettura dentro il registro delle fonti, e un nome che non corrisponde non produce un errore ma una riga senza stato, che il blocco generato elenca fra i buchi. I cluster che non compaiono qui sono da leggere, e il loro conto sta nel blocco generato invece che in una riga di prosa che invecchia.

## Lotto del 2026-09-09: i cluster 6, 5, 4 e 3

### Che cosa ha aggiunto il cluster sull'accesso alla banca

La voce più importante era la spiegazione tecnica del tracciatore, ed è già in `STUDIO-09` perché cambia la pianificazione. Le altre tre voci del cluster aggiungono meno di quanto il titolo promettesse: la guida al modding della console è quella che il progetto già segue, la tabella della connettività è un file su un servizio di condivisione che non si scarica senza credenziali, e la guida alla console definitiva è una procedura di allestimento per chi parte da zero, quindi utile a chi deve comprare l'hardware e non a chi lo ha già.

Vale però registrare una cosa che quella guida dice e che il progetto non aveva scritto in forma esplicita: la catena richiede due console fisiche nello stesso momento per il passaggio dalla quarta alla quinta generazione, perché quel trasferimento avviene fra due apparecchi in comunicazione locale e non dentro una console sola. È un vincolo materiale e non una comodità, e il progetto lo ha implicitamente soddisfatto ma non lo aveva enunciato.

### Che cosa ha aggiunto il cluster delle altre liste, ed è la misura di una nostra cecità

La voce che ha prodotto lavoro è l'elenco enciclopedico degli identificativi di allenatore notevoli, che il crawler non aveva scaricato e che una richiesta locale ha restituito al primo tentativo. È una tabella di ottocentonovantasei righe utili, ciascuna con l'identificativo, il nome dell'allenatore e l'evento a cui appartiene, e serve a rispondere a una domanda che il progetto non poteva porsi da solo: quante coppie fra allenatore e identificativo siano documentate al di fuori delle nostre liste.

Lo strumento è `tools/censimento-id-notevoli.py`, il documento è `ID-NOTEVOLI.md`, e la misura è nei due versi come ADR-044 prescrive. Quattrocentosettantatre righe trovano corrispondenza esatta nelle nostre liste sulla coppia fra allenatore e identificativo. Trecentouno corrispondono sul solo identificativo, e la coincidenza è dichiarata debole perché due eventi diversi possono condividere un numero. Tre righe la fonte stessa le dichiara non appartenenti ad alcun esemplare da collezione, cioè gli identificativi dei Pokemon da noleggio e quello che il catalogo di un gioco usa internamente. Restano centodiciannove righe non coperte, e quella è la nostra cecità.

Guardate una per una, le centodiciannove hanno una spiegazione che conferma per via indipendente una decisione già presa: la grande maggioranza sono distribuzioni coreane e giapponesi, con il nome dell'allenatore in hangul o in katakana, cioè precisamente la classe che ADR-040 aveva escluso per la barriera della lingua. Le poche restanti sono eventi in gioco che nessuna carta ha lasciato, come il Floette del fiore eterno con identificativo zerozerozerozerozerouno, e distribuzioni locali di piccola scala. Ne segue che la copertura del progetto sulle distribuzioni documentate è buona e che il buco è dove il progetto ha deciso che fosse.

Due voci del cluster non si recuperano e sono catalogate con il motivo. Il foglio delle sfere abbinate, che sarebbe la fonte comunitaria dell'asse fra specie e sfera, sta su un servizio di condivisione che risponde con un rifiuto sia all'esportazione sia allo scaricamento diretto, perché è un file caricato e non un documento nativo. La tabella della connettività è nella stessa condizione. Entrambe sono materiale che l'utente può scaricare dal browser in un minuto, e stanno in `pending.md` con la domanda a cui servono.

### Che cosa ha aggiunto il cluster dei fiocchi

Poco in contenuto e una cosa in metodo. Il manuale comunitario dei fiocchi è ospitato su un servizio che rende le pagine nel browser, quindi il crawler ne ha salvato il solo guscio: mille e duecento byte di intestazione e nessun testo. Ciò che quel guscio porta è però significativo, perché è l'unica riga di testo che il servizio scrive nel documento iniziale, ed è un avviso: la banca chiude il 26 febbraio 2027, chi vuole completare la settima generazione lo faccia prima, ed esiste una pagina di preparazione d'emergenza per chi voglia chiudere un fiocco master entro la scadenza. Ne segue che quel manuale è una fonte da recuperare e non da archiviare, perché ha una pagina dedicata esattamente al nostro problema, e il recupero richiede il percorso giusto delle sue sotto-pagine oppure la consegna manuale.

### Che cosa ha aggiunto il cluster delle collezioni di una sola specie

È il cluster che documenta gli assi che il progetto chiama minori e che ADR-041 prescrive di misurare invece di moltiplicare. Le sue voci sono pagine dell'archivio enciclopedico sulle distribuzioni di una specie sola, cioè Pikachu, Genesect, Deoxys e Keldeo, e pagine sui contrassegni e sulle condizioni meteorologiche di ottava generazione.

La voce che serve al nostro lavoro è quella sui livelli minimi per sfera, che per ciascuna specie dichiara il livello più basso a cui la si può avere in ciascuna sfera, distinguendo fra l'esemplare cresciuto e quello selvatico. È esattamente la tavola che serve a comporre una coppia fra specie e sfera che il verificatore accetti, e va dichiarato un limite nostro: l'estrattore che ha ridotto quella pagina a testo ha perso le intestazioni delle colonne e conservato i numeri, quindi la tavola è oggi illeggibile nel derivato mentre il grezzo, che sta accanto, la contiene ancora.

I contrassegni e il meteo di ottava generazione non toccano la scadenza, perché quella generazione parla direttamente col deposito, e restano registrati come materia dell'asse dei contrassegni.

## Una correzione che viene dall'utente e non dalle fonti

Il vincolo di calendario che `STUDIO-09` aveva sollevato sul piano a pagamento è già soddisfatto: l'utente ha il piano attivo, e la banca è gratuita dal 2023, quando chiuse il negozio in rete della console portatile. Il contatore di giorni che l'applicazione della banca mostra è il residuo di quella gratuità e non un abbonamento da rinnovare, ed era già stato registrato il 2026-09-03 come artefatto privo di significato per la nostra pianificazione. Resta della sezione di `STUDIO-09` la sola parte che conta, cioè la capienza: seimila posizioni, novemila da ottobre 2026, e il tetto va contato nel piano perché il perimetro che ADR-051 apre è più grande di quella cifra.

## Lotto del 2026-09-09, secondo: i cataloghi per generazione dalla prima alla terza, e la quarta

L'ordine è quello di ADR-052, cioè la scadenza: questi sono i cluster delle generazioni la cui via verso il deposito passa dalla banca. La fonte portante sono le tre guide al catalogo per regione d'origine di electroswingmix, aggiornate rispettivamente al novembre 2025 per le prime due e al 15 agosto 2026 per la terza, cioè dopo l'annuncio della chiusura.

### Che cosa vincola la prima generazione

Il fatto che tocca il nostro lotto più di ogni altro riguarda la cromaticità: in prima generazione un esemplare selvatico non può essere legalmente cromatico, mentre lo possono essere i doni, gli scambi in gioco e gli incontri fissi. È un vincolo di legalità e non una probabilità, quindi qualunque voce cromatica che il progetto componga per quella generazione deve appartenere a una di quelle tre classi, e le nostre sedici voci cromatiche vanno riviste con questo criterio.

La guida conferma per via indipendente la verifica sui premi di Stadium chiusa poche ore prima, e aggiunge un dettaglio che la rende più precisa: non esiste modo legale di trasferirli perché la riedizione per Console Virtuale non ha mai avuto la connessione con la console fissa, e per iniezione passano tutti tranne il Farfetch'd che conosce Staffetta, perché quella mossa su quella specie il verificatore del trasferimento non la ammette. Il nostro lotto contiene quella voce, quindi va marcata come non trasferibile nemmeno per iniezione.

Sugli esclusivi di versione la guida enumera ciò che il progetto non aveva scritto: Lickitung e Jynx selvatici nella sola versione giapponese Blu, undici specie nella versione internazionale Rossa, undici nella coppia Verde giapponese e Blu internazionale, Farfetch'd e Lickitung selvatici in Giallo, e tredici specie che in Giallo non si ottengono affatto. Ne segue che il catalogo di prima generazione richiede tre versioni e non una, cosa che il progetto sapeva per la terza generazione e non aveva enunciato per la prima.

I nove scambi di Rosso e Blu e i sette di Giallo sono elencati con il loro soprannome, e coincidono con il nostro censimento degli scambi tranne per una voce, che è lo scambio del Nidoran differente fra versione internazionale e giapponese: la nostra tabella lo porta come due voci e la guida come una.

### Che cosa vincola la seconda generazione

La guida enuncia un limite che il progetto deve conoscere prima di comporre: in nessun gioco di seconda generazione si ottengono legittimamente gli iniziali di prima, i fossili di prima esclusa Aerodactyl, i tre uccelli leggendari, Mewtwo e Mew. Sono quindi voci che la seconda generazione non può dare, e chi le volesse con provenienza di quella regione deve passare per la prima.

Sull'asse delle forme arriva un dato preciso che tocca una sfida del deposito: in seconda generazione Unown esiste nelle sole ventisei lettere, mentre le due forme con il punto esclamativo e il punto interrogativo compaiono per la prima volta in terza generazione, nelle versioni di Kanto rifatto. La sfida che chiede ventotto forme di Unown non è dunque soddisfacibile con la sola seconda generazione, e questo spiega perché la nostra enumerazione delle forme trovasse ventotto valori dove la generazione d'origine ne ha ventisei.

Celebi è ottenibile legittimamente soltanto in Cristallo, ed è la sola generazione in cui si possa cercarlo cromatico. Gli esclusivi di versione e le tre linee che Cristallo non dà, cioè Mareep, Girafarig e Remoraid, completano il quadro.

### Che cosa cambia nella terza generazione, e riguarda la scadenza

La guida è aggiornata dopo l'annuncio della chiusura e porta il fatto che sposta un risultato del progetto: la versione per console corrente di Rosso Fuoco e Verde Foglia include l'evento dell'Isola Nascita, quindi Deoxys si ottiene là, si può cercare cromatico, e registra come regione Kanto invece di Hoenn. Deoxys era una delle quattro specie che ADR-032 aveva trovato prive di qualunque incontro nei giochi moderni, insieme a Celebi, Victini e Zarude: se la fonte è esatta, quella riga va corretta perché da ottobre esiste un incontro moderno, con la conseguenza che una specie in meno dipende dalla catena storica.

Il resto della guida completa l'asse delle uova con quattro voci che il progetto aveva registrato senza il loro dettaglio tecnico. Le uova del deposito per console fissa di terza generazione portano ciascuna una mossa esclusiva: Swablu con Falsofinale, Zigzagoon con Extrarapido, Skitty con Giornopaga e Pichu con Surf. E soltanto Pichu deve dimenticare la propria mossa per essere trasferito, il che significa che le altre tre la conservano fino al deposito e sono quindi collezionabili con una proprietà che nessun'altra via riproduce.

Sui due giochi da console fissa la guida chiarisce una cosa che il nostro censimento non diceva: non contengono specie esclusive, ma gli esemplari che vi si ottengono portano fiocchi e luoghi d'incontro esclusivi, e ogni esemplare catturabile vi si può cercare cromatico a probabilità piena. Il disco supplementare giapponese aggiunge Celebi e Pikachu, e tre carte per il lettore esterno sbloccano Togepi, Mareep e Scizor ombra catturabili.

### La quarta generazione, e una voce che si chiude

Il punto in sospeso sulle rovine di Sinjoh si chiude con la procedura, che la guida dedicata descrive passo per passo. Il terzetto del tempo e dello spazio al livello uno si ottiene portando un Arceus di quarta generazione in una riedizione di seconda, tenendolo come solo esemplare in squadra, entrando nelle rovine di Alph e scegliendo uno dei tre cerchi: quello a sinistra dà Dialga, quello a destra Palkia, quello in alto Giratina, ciascuno al livello uno. Ne segue che la voce non è sbloccata da un oggetto ma dal possesso di un Arceus, e che l'Arceus a sua volta viene dal flauto mai distribuito ufficialmente oppure dalla distribuzione di un rivenditore, che il servizio in rete ricostruito rende di nuovo ottenibile: è la via del nome di dominio già studiata in `STUDIO-04`, con la procedura completa del menu dei doni misteriosi e la domanda a due risposte che lo sblocca nei titoli di Sinnoh.


## Lotto del 2026-09-10: i tracciatori, e la terza enumerazione

### Perché questo cluster prima degli altri

Il cluster dei tracciatori è stato scelto per primo fra quelli rimasti perché serve la decisione aperta sul profilo di collezione, che è dell'utente e che blocca la pianificazione: finché non si sa quale collezione si vuole non si sa quale lavoro sia necessario e quale superfluo. Il criterio di scelta è quindi l'utilità per una decisione in attesa, non l'ordine del post.

### La terza enumerazione, che rompe la parità

Il risultato principale del lotto è che PokePC Classic, già SuperEffective.gg, pubblica sotto licenza permissiva i dati che lo alimentano: un'anagrafica di millecinquecentonovantanove voci con i contrassegni che dicono che cosa ciascuna sia, e sette disposizioni in scatole per il deposito. Non è una lista di specie ma un elenco di caselle da riempire, cioè precisamente la domanda che la nostra lista di spunta dichiara indeterminata.

Il confronto è `CONFRONTO-LIVINGDEX-POKEPC.md`, generato da `tools/confronta-livingdex-pokepc.py`, e il numero che conta non è lo scarto ma la sua forma. Le due enumerazioni esterne, scritte da autori diversi con metodi diversi, distano fra loro due voci su quasi millequattrocento, cioè milletrecentottantasette contro milletrecentottantanove, mentre la nostra dista da entrambe una ventina, con milletrecentosessantasette. Una convergenza di quel genere non dimostra che le due esterne abbiano ragione, ma sposta l'onere della prova su di noi.

Delle trecentosessantadue voci che PokePC conta oltre la specie base, centocinquantasette sono forme cosmetiche, centotre forme femminili e centotre forme che il campo della forma separa davvero; megaevoluzioni, forme gigamax e forme di sola battaglia non compaiono affatto, il che corrobora per via indipendente il nostro perimetro. Due voci minori cadono su questioni già decise: le sessantatre configurazioni di Alcremie sono confermate da tre fonti indipendenti oltre alla nostra, e la specie con differenze di sesso in più rispetto alle nostre centodue è una sola, cioè Basculin, che la pagina enciclopedica non nomina affatto e che resta quindi una divergenza non corroborata invece che una correzione.

Un difetto della prima stesura del programma va registrato perché è del genere che produce un numero sbagliato con l'aria di essere esatto: assumeva che le sette disposizioni differissero per il solo ordinamento, mentre due danno una casella propria alla forma gigamax e due si dichiarano minime, e una cella non è sempre un identificativo ma può essere un oggetto con un contrassegno. Identificarla con il solo identificativo faceva sparire trentotto caselle senza che nulla se ne accorgesse.

### Gli altri profili, letti da chi li persegue

Il cluster ha dato le definizioni operative di tre profili, scritte da chi li porta avanti invece che dedotte da una interfaccia. Il profilo dell'arca chiede un esemplare per ciascuno dei due sessi di ogni specie e di ogni forma, uno solo per le specie senza sesso, e la variante cromatica di ciascuno per il caso estremo. Il profilo per regione di origine chiede che ogni esemplare venga dal titolo più antico in cui la sua forma possa esistere, e la sua guida elenca i tredici titoli minimi e le sei console che servono a percorrerlo. Il terzo è un foglio del 2022 che tiene insieme sei tracciatori distinti, cioè catalogo vivente, esemplari di taglia massima, marchi di origine, marchi ordinari, fiocchi e sfere: la coincidenza fra quei sei e i sei assi che questo progetto ha ricostruito quattro anni dopo per conto proprio è la conferma indipendente più forte che l'insieme degli assi sia quello.

Una quarta enumerazione, in forma di documento invece che di foglio, dichiara esplicitamente che cosa include e che cosa esclude, ed è utile proprio per l'elenco delle esclusioni: niente cromatici, niente forme effimere come le megaevoluzioni e le gigamax, niente forme che dipendono da un oggetto tenuto o da un'abilità, niente tosature, niente totem e niente forme mai rilasciate. È il medesimo perimetro del progetto, enunciato da un altro.

### Il risultato che non veniva dal cluster, e che vale più del cluster

Seguendo un rinvio della guida al profilo per regione di origine si è arrivati a una fonte che il censimento aveva scaricato e che nessuno aveva letto, cioè l'elenco dei doni di quarta e quinta generazione che si ricevono collegando la console al servizio ricostruito attraverso una diversa configurazione dei server dei nomi. La fonte è del 2020, ha milletrecentottantaquattro commenti, e due testimonianze indipendenti del 2026-09-07 dichiarano il canale ancora attivo nominando le sole voci che non hanno ottenuto.

Ciò che questo aggiunge al progetto è la risposta parziale al primo dei quattro passi lasciati aperti dal capitolo sulla produzione dentro il gioco: il canale distribuisce doni e non soltanto scambi, e un catalogo di ciò che distribuisce esiste in forma di testimonianza. Ne segue che una parte dell'asse degli eventi potrebbe essere ricevuta invece che composta, il che è preferibile su ogni dimensione che a questo progetto interessi. Due dettagli meritano l'isolamento: il canale serve anche due doni mai distribuiti ufficialmente, fra cui l'oggetto la cui assenza rende non conforme l'esemplare che il progetto aveva registrato come non producibile, e le voci mancate dai due testimoni sono le stesse, il che suggerisce un insieme stabile e quindi misurabile. Ciò che una testimonianza non dà resta intero: nessuna delle due dice nulla sui campi dell'esemplare ricevuto, che sono l'unica cosa che decide se il verificatore lo accetti.

### Che cosa del lotto resta non letto

Del cluster dei tracciatori restano due voci in forma di applicazione che il censimento marca come catalogate e che una richiesta locale non rende, cioè un tracciatore generico e uno dedicato all'applicazione per telefono. Del cluster principale restano la pagina che la corsa non ha scaricato, due voci in forma di video e la guida al profilo alfabetico, che è stata aperta ma non spogliata. Nessuna delle cinque cambia una decisione aperta, che è la ragione per cui il lotto si chiude qui invece di attenderle.
