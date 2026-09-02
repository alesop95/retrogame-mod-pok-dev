# Che cosa la chiusura della banca vincola davvero

Questa nota risponde a una domanda sola, e la risposta cambia come si spendono i giorni che restano: quali specie e quali forme il completamento del Pokedex in Pokemon Home non possa ottenere se non passando dalla banca, che cessa il 26 febbraio 2027.

## 1. Perché la domanda non è quella che sembra

La lettura ingenua del vincolo di tempo è che la scadenza riguardi la collezione. Non è così, perché il deposito accetta esemplari per due vie con proprietà temporali opposte. La via diretta dei titoli dell'ottava e della nona generazione versa in Home senza passare da alcun servizio in dismissione e non ha scadenza. La via della banca cessa a quella data.

Ne segue che il vincolo di tempo riguarda l'insieme differenza, cioè ciò che nessun titolo a via diretta produce, e che la grandezza di quell'insieme è il numero che governa la pianificazione. Se fosse grande, i giorni andrebbero spesi sul Pokedex; se fosse piccolo o vuoto, andrebbero spesi su altro. Fino al 2026-09-02 il progetto non lo sapeva.

## 2. La consegna dell'utente, e che cosa afferma

Il 2026-09-01 l'utente ha consegnato una ricerca propria, conservata verbatim accanto a questa nota, che affronta la medesima domanda e la risponde con un metodo dichiarato: clonare il verificatore di conformità e leggere le tabelle binarie delle statistiche di base dei sette titoli, più il file che dichiara le forme di sola battaglia, incrociando i nomi con una fonte terza.

Quella ricerca porta un controllo di validità esplicito, e va apprezzato perché è la parte che la rende verificabile: il suo parsing di una delle tabelle restituisce seicentosessantaquattro specie, cifra che coincide con il totale noto di quel titolo con entrambe le sue espansioni. Dichiara inoltre due limiti propri, e sono i due giusti: che non può confermare quali forme il deposito conti come voci separate, e che il contrassegno di presenza dice che una forma esiste nei dati e non che sia ottenibile.

La sua conclusione operativa è che la scadenza riguardi nove voci, cioè le forme totemiche di una regione, e che quelle restino irrecuperabili dopo la chiusura.

## 3. La verifica indipendente

La conclusione è stata verificata invece di essere accolta, e il modo conta: non rileggendo la ricerca ma rifacendo il conto con un programma proprio, `tools/disponibilita-titoli.py`, che legge le medesime tabelle senza sapere che risultato attendersi.

Il primo esito è che i numeri di controllo si riproducono esattamente. Le specie con il contrassegno di presenza sono seicentosessantaquattro nel primo titolo, quattrocentonovantatre nel secondo e ottocentosette nel terzo, cioè le tre cifre che la ricerca dichiarava. Il suo parsing era corretto.

Il secondo esito è al livello delle specie, e non era nella ricerca: l'unione dei titoli a via diretta copre tutte e millleventicinque le specie del Dex Nazionale, quindi le specie che la scadenza vincola sono zero.

Il terzo esito è al livello delle voci-forma, e differisce dalla ricerca in un modo che si spiega interamente. Le voci che soltanto la via indiretta dichiara sono dodici e non nove. Le tre in più sono la variante di un travestimento, una forma di fusione e una forma legata a una abilità speciale, e sono escluse dal medesimo filtro che la ricerca dichiarava di avere applicato: due sono forme di sola battaglia, e la terza è la variante rotta di una forma totemica. Con quel filtro applicato le voci diventano nove, cioè esattamente il numero della ricerca.

## 4. La correzione che cambia la conclusione

Il quarto esito è una correzione, e riguarda non il conto ma il significato di quelle nove voci.

La ricerca le dichiara irrecuperabili dopo la chiusura della banca, che implica che siano recuperabili prima. Non lo sono. Il verificatore dei trasferimenti dell'implementazione di riferimento contiene una regola esplicita per gli incontri della settima generazione che siano totemici, e quella regola dice due cose: quattro specie non si trasferiscono affatto all'ottava generazione, e per tutte le altre l'esemplare trasferito deve portare la forma base e non quella totemica, altrimenti il trasferimento è invalido. La funzione che calcola quella forma base porta nel proprio commento la ragione, cioè che serve quando la forma totemica viene riportata alla base al trasferimento.

Ne segue che nessuna forma totemica può esistere nel deposito, né prima né dopo il 26 febbraio 2027. Non sono voci in attesa di scadenza: sono voci irraggiungibili per costruzione, e la loro assenza dalla collezione non è un costo della chiusura della banca ma una proprietà permanente del formato.

L'esito complessivo è dunque che le voci che la chiusura della banca vincola sono zero, sia al livello delle specie sia al livello delle forme.

## 5. La sola eccezione possibile, e perché lo strumento non la vede

Resta un punto su cui il verdetto potrebbe cambiare per una specie, e va tenuto in evidenza perché è l'unico.

Il materiale consegnato afferma che Spinda, pur essendo presente nei dati del solo titolo a via diretta che lo contiene, non possa essere depositato nel deposito da quel titolo per un difetto della sua implementazione, e che vada quindi procurato per la via della banca oppure per uno scambio. Aggiunge che quella specie è indispensabile a un dono che il deposito consegna al completamento del Dex Nazionale.

Lo strumento non può vedere un difetto di quel genere, e la ragione va enunciata perché delimita ciò che esso dimostra. Esso legge se una voce esista nei dati di un titolo, non se la via che parte da quel titolo funzioni: la prima è una proprietà di una tabella, la seconda è una proprietà di un servizio in rete. Ne segue che ogni affermazione della forma "quella via è rotta" è fuori dalla sua portata e va verificata altrove.

Se l'affermazione è vera, Spinda è l'unica specie con una scadenza reale, e va procurata prima del 26 febbraio 2027. La verifica di quella affermazione è il primo punto aperto di questo sottoprogetto.

## 6. Che cosa la scadenza vincola davvero

Fuori dal Pokedex resta l'insieme che la scadenza vincola per intero, e sono i singoli esemplari la cui identità richiede una provenienza anteriore all'ottava generazione. Non si contano in voci di Dex perché non sono specie: sono esemplari.

La distinzione è quella fra la specie e l'esemplare, e questo progetto la conosce bene perché vi ha lavorato per giorni. Un Charizard si ottiene oggi in un titolo recente; il Charizard della distribuzione del decennale no, e nessuna via moderna lo produce, perché ciò che lo distingue non è la specie ma il nome dell'allenatore, il suo identificativo, il luogo di incontro e il contrassegno dell'incontro fatidico, che sono campi irreversibili. Vale con più forza per gli esemplari che l'utente possiede su cartuccia, che oltre a essere irriproducibili sono anche suoi.

Ne segue la priorità del progetto nei giorni che restano, e non è quella che l'obiettivo suggerisce a prima vista: prima gli esemplari, perché sono irrimediabili e perché la loro macchina esiste già; poi il Pokedex, che non ha scadenza e si completa con calma.

## 7. Che cosa questa nota non ha stabilito

Tre cose, elencate perché una nota che tace i propri limiti vale meno di una che li dichiara.

Non ha stabilito quali forme il deposito conti come voci separate del proprio Pokedex. Il conto è di forme esistenti nei dati dei giochi, e la corrispondenza fra quelle e le caselle del deposito non è documentata da alcuna fonte di primo livello. È il medesimo limite che la ricerca consegnata dichiarava, e resta aperto.

Non ha stabilito che una voce presente nei dati sia ottenibile in gioco. Il contrassegno di presenza dice che la forma esiste nella tabella di quel titolo, e una forma esistente ma non catturabile risulterebbe raggiungibile mentre non lo è. La verifica di una voce sospetta è però possibile e a basso costo, componendo un esemplare con quella provenienza e chiedendo il giudizio del verificatore, che è lo stesso presidio che il progetto usa per gli esemplari da evento.

Non ha stabilito nulla sui costi. Il verdetto è che il Pokedex non ha scadenza, non che sia gratuito: richiede titoli che l'utente non possiede ancora e un piano a pagamento del deposito che non è attivo. Il verdetto dice quando spendere, non quanto.
## 8. Il controllo incrociato su una fonte indipendente, e la domanda che essa non può rispondere

Il conto sulle tabelle del verificatore è stato confrontato con una base dati indipendente, quella che serve il simulatore di battaglie della comunità, letta il 2026-09-02. Il confronto ha dato un accordo e una discrepanza, e la discrepanza è la parte istruttiva.

L'accordo è sul numero delle specie. Quella base dati porta millleventicinque voci base con numero da uno a millleventicinque e nessun numero mancante, cioè esattamente il conto che le tabelle del verificatore danno e quello che la ricerca consegnata dichiarava. Tre ricostruzioni indipendenti, fatte da persone diverse su materiali diversi, concordano sul medesimo numero: è il grado di conferma più alto che questa domanda possa ricevere senza una pubblicazione ufficiale.

La discrepanza è sul numero delle forme, e non è un errore di nessuna delle due parti: le due fonti contano cose diverse. Quella base dati serve il gioco competitivo, quindi enumera le forme che cambiano il comportamento di un esemplare in battaglia e omette quelle puramente estetiche, mentre le tabelle del verificatore enumerano tutto ciò che esiste nei dati dei giochi, comprese le decine di varianti che differiscono per il solo aspetto. Le sue trecentocinquantacinque forme non base, di cui centoquarantatre senza marca di non standard, non sono dunque un conteggio alternativo delle nostre millecinquecentotrentacinque voci-forma: sono il conteggio di un altro insieme.

Ne segue una conclusione sull'uso delle fonti che vale oltre questo caso. Una fonte non è semplicemente attendibile o inattendibile: è attendibile su certe domande e muta su altre, e la sua utilità dipende dal sapere quali. Questa base dati è lo strumento giusto per confermare il numero delle specie ed è lo strumento sbagliato per contare le forme, e chi la usasse per la seconda domanda otterrebbe un numero preciso, ricavato correttamente, e non pertinente. Porta inoltre centotrentasette voci inventate dalla comunità competitiva, riconoscibili dal numero non positivo, che vanno filtrate prima di qualunque conto.

## 9. L'organizzazione delle scatole, che è una decisione e non un dato

L'utente ha consegnato tre criteri per disporre la collezione nel deposito, e vanno registrati qui perché sono una decisione di prodotto e il posto di una decisione è accanto al suo oggetto.

Il primo è l'ordine numerico del Dex Nazionale come base di partenza. Il secondo è che le forme regionali stiano in posizioni consecutive accanto alla specie che le origina, cosicché la consultazione non richieda di cercare in due punti. Il terzo è lasciare qualche posizione libera alla fine di ciascuna scatola, per accogliere le forme che i titoli futuri introdurranno.

Il terzo criterio merita una nota perché è il più facile da trascurare e il più costoso da rimediare. Una collezione disposta senza spazi va riordinata per intero quando una specie nuova si inserisce nel mezzo, e il riordino di centinaia di posizioni nel deposito è lavoro manuale che non si automatizza. Lasciare spazio è quindi una decisione sul costo di manutenzione e non una preferenza estetica, ed è il medesimo ragionamento per cui un formato di dati riserva campi non usati.

Va aggiunto un fatto che il progetto conosce e che rende il terzo criterio più rilevante di quanto sembri: il numero massimo del Dex Nazionale è un dato che i titoli futuri alzeranno, e lo strumento che calcola la disponibilità lo porta come costante da aggiornare. Quando quel numero cresce, cresce anche la collezione, e le posizioni lasciate libere sono ciò che rende l'aggiornamento un inserimento invece di un rifacimento.
