---
tipo: nota di studio
livello: codice
tags: [collaudo, test, emulatore, hardware]
up: "[[index]]"
vedi_anche: ["[[20-architettura-codice]]", "[[08-cavo-link]]", "[[10-multiboot-hardware]]", "[[22-strumenti]]"]
---

# Collaudo: che cosa si prova su dati, che cosa su emulatore, che cosa solo su ferro

Il progetto ha una scheda dedicata al protocollo di verifica su hardware reale, `.claude/context/dev-testing.md`, e una regola normativa che pretende backup e read-back. Questa nota sta un passo prima: dice quanto lavoro si puo' verificare senza arrivare all'hardware, perche' ogni difetto trovato prima e' un difetto che non si paga su una cartuccia.

## Tre livelli, e il criterio per collocare una prova

Il criterio e' semplice: una prova va eseguita al livello piu' economico che la puo' falsificare. Salire di livello senza necessita' non aggiunge fiducia, aggiunge rischio e tempo.

Il primo livello e' il collaudo su dati sintetici, che non richiede nulla se non un interprete. Copre tutto lo strato di lettura e scrittura e tutto lo strato di conversione, cioe' la maggior parte del codice. Il secondo e' il collaudo su emulatore, che copre il protocollo del cavo contro un gioco vero. Il terzo e' il collaudo su hardware, che copre soltanto cio' che gli altri due non possono raggiungere.

## Primo livello: dati sintetici, e la prova che vale piu' di tutte

La prova piu' forte per uno strato di lettura e scrittura e' la simmetria: si legge una struttura, si riscrive, e i byte devono coincidere esattamente con quelli di partenza. Questa singola proprieta' cattura un intero genere di errori, perche' un offset sbagliato, un ordine di byte invertito, un campo di bit letto dalla finestra sbagliata o un checksum calcolato nel momento sbagliato la rompono tutti.

Il collaudo dello strumento per lo zaino di Smeraldo, descritto in [[22-strumenti]], e' un esempio di quanto renda questo livello. Il salvataggio di prova e' stato costruito a mano, con una chiave nota, un denaro noto e cinque anomalie deliberate, e la prima esecuzione ha rivelato un difetto vero: lo strumento considerava vuoto uno slot con quantita' zero, mentre in una tasca mascherata uno slot vuoto non ha quantita' zero, ha la chiave. Nessuna quantita' di lettura del codice lo avrebbe fatto emergere, e su un salvataggio reale si sarebbe presentato come una tasca piena di voci inesistenti.

Da quello stesso difetto e' venuta una diagnostica in piu': se uno slot vuoto contiene la chiave, allora la chiave si puo' ricavare da qualunque slot vuoto e confrontare con quella letta al suo offset. Due vie indipendenti per lo stesso valore sono una verifica gratuita, e questo e' il genere di cosa che si trova solo collaudando.

Per la conversione, il primo livello ha una forma diversa, perche' la conversione ha scelte discutibili e non esiste un risultato unico corretto. La prova utile e' allora la coerenza interna: dopo la conversione, la natura del risultato deve corrispondere a quella richiesta, il sesso a quello dell'originale, la lucentezza a quella dell'originale, e la struttura deve superare la propria verifica di checksum. Sono le stesse condizioni che il campionamento con rifiuto descritto in [[07-conversione-vincoli]] impone in scrittura, usate qui come asserzioni in lettura.

## Secondo livello: l'emulatore, che copre piu' di quanto si crede

L'avvertenza ripetuta in tutta la documentazione della community e' che il ponte non si emula, ed e' vera. Ma copre uno scenario piu' stretto di quanto la formulazione suggerisca: cio' che non si emula e' l'interazione fra Game Boy e Game Boy Advance.

Il collegamento fra due Game Boy invece si emula bene. BGB espone il cavo Link su una connessione TCP con un protocollo documentato a pacchetti di otto byte, e `PokemonGB_Online_Trades` implementa gli scambi di generazione 1, 2 e 3 esattamente su quella interfaccia. Ne segue che si puo' collaudare, contro un gioco vero e senza console, tutta la negoziazione dei ruoli, la selezione della modalita', la sequenza dei tre blocchi, il preambolo, la lista di correzione e la validazione dei dati ricevuti.

Una dipendenza non ovvia va detta subito, perche' altrimenti questo livello sembra disponibile quando non lo e'. Contro un gioco vero significa che serve la ROM di quel gioco, e ottenerla dentro il perimetro dichiarato dal progetto significa dumpare una cartuccia di proprieta', che richiede il lettore. Finche' il lettore non c'e', il protocollo si puo' scrivere e provare soltanto per auto-consistenza, cioe' facendo parlare due istanze della nostra implementazione: verifica che il codice sia coerente con se' stesso, non che sia conforme al gioco, ed e' una prova debole che va chiamata con il suo nome.

Quando la ROM ci sara', il guadagno sara' grosso, perche' quello e' anche lo strato dove il debug su hardware sarebbe piu' doloroso: su emulatore si possono registrare tutti i byte scambiati e confrontarli con quelli attesi, cosa che su due console vere richiede un analizzatore logico.

## Terzo livello: il ferro, e come ci si arriva

Resta all'hardware cio' che nessuno dei due livelli precedenti raggiunge: il multiboot, lo scambio a caldo della cartuccia, e la scrittura vera sul salvataggio di generazione 3. La disciplina e' quella della regola normativa, e vale la pena ripeterne il senso invece della lettera. Il backup in doppia copia esiste perche' l'operazione ha una finestra di rischio reale, non perche' sia prudente in astratto. Il read-back verificato esiste perche' una scrittura dichiarata riuscita dal software puo' non essere rimasta sul chip, e il confronto si fa sui byte e non sulla schermata di gioco.

C'e' un ordine sensato anche dentro questo livello, e conviene rispettarlo. Prima si verifica di poter leggere, cioe' si dumpa il salvataggio e lo si confronta con una seconda lettura. Poi si verifica di poter scrivere qualcosa di innocuo e rileggerlo. Solo dopo si prova il trasferimento. Chi comincia dal trasferimento sta collaudando tre cose insieme e non sapra' quale ha fallito.

## Che cosa non collaudare

Un'ultima nota su un errore di metodo facile da commettere. Non ha senso collaudare la logica di conversione contro l'output di un tool esistente, per esempio confrontando i propri risultati con quelli del PCCS. Un'implementazione di riferimento incorpora scelte arbitrarie, come il caso speciale su impronte hash descritto in [[07-conversione-vincoli]], e un test che pretende identita' con essa non verifica la correttezza: verifica la conformita' a scelte di qualcun altro. Il confronto e' utile come indagine, non come asserzione.

## Cosa leggere dopo

[[22-strumenti]] documenta gli strumenti esistenti e come si rilanciano.
