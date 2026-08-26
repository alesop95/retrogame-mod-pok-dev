---
tipo: nota di studio
livello: codice
tags: [collaudo, test, emulatore, hardware]
up: "[[index]]"
vedi_anche: ["[[20-architettura-codice]]", "[[08-cavo-link]]", "[[10-multiboot-hardware]]", "[[22-strumenti]]"]
---

# Collaudo: che cosa si prova su dati, che cosa su emulatore, che cosa solo su ferro

Il progetto ha una scheda dedicata al protocollo di verifica su hardware reale, `.claude/context/dev-testing.md`, e una regola normativa che pretende backup e read-back. Questa nota sta un passo prima: dice quanto lavoro si può verificare senza arrivare all'hardware, perché ogni difetto trovato prima è un difetto che non si paga su una cartuccia.

## Tre livelli, e il criterio per collocare una prova

Il criterio è semplice: una prova va eseguita al livello più economico che la può falsificare. Salire di livello senza necessità non aggiunge fiducia, aggiunge rischio e tempo.

Il primo livello è il collaudo su dati sintetici, che non richiede nulla se non un interprete. Copre tutto lo strato di lettura e scrittura e tutto lo strato di conversione, cioè la maggior parte del codice. Il secondo è il collaudo su emulatore, che copre il protocollo del cavo contro un gioco vero. Il terzo è il collaudo su hardware, che copre soltanto ciò che gli altri due non possono raggiungere.

## Primo livello: dati sintetici, e la prova che vale più di tutte

La prova più forte per uno strato di lettura e scrittura è la simmetria: si legge una struttura, si riscrive, e i byte devono coincidere esattamente con quelli di partenza. Questa singola proprietà cattura un intero genere di errori, perché un offset sbagliato, un ordine di byte invertito, un campo di bit letto dalla finestra sbagliata o un checksum calcolato nel momento sbagliato la rompono tutti.

Il collaudo dello strumento per lo zaino di Smeraldo, descritto in [[22-strumenti]], è un esempio di quanto renda questo livello. Il salvataggio di prova è stato costruito a mano, con una chiave nota, un denaro noto e cinque anomalie deliberate, e la prima esecuzione ha rivelato un difetto vero: lo strumento considerava vuoto uno slot con quantità zero, mentre in una tasca mascherata uno slot vuoto non ha quantità zero, ha la chiave. Nessuna quantità di lettura del codice lo avrebbe fatto emergere, e su un salvataggio reale si sarebbe presentato come una tasca piena di voci inesistenti.

Da quello stesso difetto è venuta una diagnostica in più: se uno slot vuoto contiene la chiave, allora la chiave si può ricavare da qualunque slot vuoto e confrontare con quella letta al suo offset. Due vie indipendenti per lo stesso valore sono una verifica gratuita, e questo è il genere di cosa che si trova solo collaudando.

Per la conversione, il primo livello ha una forma diversa, perché la conversione ha scelte discutibili e non esiste un risultato unico corretto. La prova utile è allora la coerenza interna: dopo la conversione, la natura del risultato deve corrispondere a quella richiesta, il sesso a quello dell'originale, la lucentezza a quella dell'originale, e la struttura deve superare la propria verifica di checksum. Sono le stesse condizioni che il campionamento con rifiuto descritto in [[07-conversione-vincoli]] impone in scrittura, usate qui come asserzioni in lettura.

## Secondo livello: l'emulatore, che copre più di quanto si crede

L'avvertenza ripetuta in tutta la documentazione della community è che il ponte non si emula, ed è vera. Ma copre uno scenario più stretto di quanto la formulazione suggerisca: ciò che non si emula è l'interazione fra Game Boy e Game Boy Advance.

Il collegamento fra due Game Boy invece si emula bene. BGB espone il cavo Link su una connessione TCP con un protocollo documentato a pacchetti di otto byte, e `PokemonGB_Online_Trades` implementa gli scambi di generazione 1, 2 e 3 esattamente su quella interfaccia. Ne segue che si può collaudare, contro un gioco vero e senza console, tutta la negoziazione dei ruoli, la selezione della modalità, la sequenza dei tre blocchi, il preambolo, la lista di correzione e la validazione dei dati ricevuti.

Una dipendenza non ovvia va detta subito, perché altrimenti questo livello sembra disponibile quando non lo è. Contro un gioco vero significa che serve la ROM di quel gioco, e ottenerla dentro il perimetro dichiarato dal progetto significa dumpare una cartuccia di proprietà, che richiede il lettore. Finché il lettore non c'è, il protocollo si può scrivere e provare soltanto per auto-consistenza, cioè facendo parlare due istanze della nostra implementazione: verifica che il codice sia coerente con sé stesso, non che sia conforme al gioco, ed è una prova debole che va chiamata con il suo nome.

Quando la ROM ci sarà, il guadagno sarà grosso, perché quello è anche lo strato dove il debug su hardware sarebbe più doloroso: su emulatore si possono registrare tutti i byte scambiati e confrontarli con quelli attesi, cosa che su due console vere richiede un analizzatore logico.

## Terzo livello: il ferro, e come ci si arriva

Resta all'hardware ciò che nessuno dei due livelli precedenti raggiunge: il multiboot, lo scambio a caldo della cartuccia, e la scrittura vera sul salvataggio di generazione 3. La disciplina è quella della regola normativa, e vale la pena ripeterne il senso invece della lettera. Il backup in doppia copia esiste perché l'operazione ha una finestra di rischio reale, non perché sia prudente in astratto. Il read-back verificato esiste perché una scrittura dichiarata riuscita dal software può non essere rimasta sul chip, e il confronto si fa sui byte e non sulla schermata di gioco.

C'è un ordine sensato anche dentro questo livello, e conviene rispettarlo. Prima si verifica di poter leggere, cioè si dumpa il salvataggio e lo si confronta con una seconda lettura. Poi si verifica di poter scrivere qualcosa di innocuo e rileggerlo. Solo dopo si prova il trasferimento. Chi comincia dal trasferimento sta collaudando tre cose insieme e non saprà quale ha fallito.

## Che cosa non collaudare

Un'ultima nota su un errore di metodo facile da commettere. Non ha senso collaudare la logica di conversione contro l'output di un tool esistente, per esempio confrontando i propri risultati con quelli del PCCS. Un'implementazione di riferimento incorpora scelte arbitrarie, come il caso speciale su impronte hash descritto in [[07-conversione-vincoli]], e un test che pretende identità con essa non verifica la correttezza: verifica la conformità a scelte di qualcun altro. Il confronto è utile come indagine, non come asserzione.

## Cosa leggere dopo

[[22-strumenti]] documenta gli strumenti esistenti e come si rilanciano.
