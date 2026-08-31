# Sottoprogetto: ricreazione delle distribuzioni e degli eventi Pokemon

Ricreare, su hardware originale e su cartucce possedute, le distribuzioni di eventi della terza generazione, cioè i Pokemon che nei primi anni Duemila si ottenevano soltanto portando la propria copia del gioco in un luogo fisico, e che dopo la fine dell'evento non sono più ottenibili in alcun modo. Il track nasce il 2026-08-28 su richiesta dell'utente e serve un obiettivo più grande di sé, dichiarato nella sezione seguente.

## L'obiettivo finale, e perché ha una scadenza

L'obiettivo dichiarato non è ricreare una distribuzione: è completare la collezione, cioè avere in Pokemon Home tutte le 1025 specie e anche le forme alternative, e tenere quella collezione come lavoro di una vita. La ricreazione delle distribuzioni è la gamba mancante di quell'obiettivo, perché una parte delle specie e delle forme non è mai stata ottenibile per gioco normale: esisteva soltanto dentro un evento a tempo, e per la terza generazione quell'evento passava da un cavo, da una ROM di distribuzione o da una macchina in un negozio.

La scadenza è esterna, verificata su fonte ufficiale il 2026-08-28 e non negoziabile. Pokemon Bank chiude il 26 febbraio 2027 alle 12:00 JST, cioè il 25 febbraio 2027 alle 19:00 PST, e con Bank cessa la funzione che trasferisce verso Pokemon Home. Bank e Poke Transporter erano rimasti gli unici servizi in linea del Nintendo 3DS dopo la chiusura generale del 9 aprile 2024, e questa eccezione finisce là. Nintendo dichiara di spostare in Home ciò che si vuole conservare prima di quella data e non annuncia alcun periodo di tolleranza.

Da qui segue il fatto operativo che governa tutto il track: qualunque esemplare della prima, seconda, terza, quarta e quinta generazione che debba finire in Home deve avere completato l'intera catena di trasferimenti prima di quella data, perché dopo quella data non esiste più alcun ingresso per i giochi che non parlano direttamente con Home. Il tempo utile, dalla nascita di questo track, è di diciotto mesi.

## Che cosa c'è in questa cartella

La cartella contiene tre documenti e uno di essi è generato. `STUDIO-01-distribuzioni-gen3-e-ricreazione.md` è il primo studio tecnico: descrive che cosa erano le distribuzioni, come è fatta una ROM di distribuzione, quali sono le quattro ROM preservate e le tre categorie di evento, che cosa la comunità ha ricreato e con quale metodo, quali sono le quattro vie per far entrare un evento in una cartuccia vera, e quali punti restano aperti. È scritto dalle quattro fonti video registrate in `SOURCES.md` con la sigla EVT, lette per trascrizione il 2026-08-28.

`STUDIO-02-metodi-di-generazione.md` è il secondo studio, scritto il 2026-08-29 su fonti di livello superiore, ed è quello da leggere per primo su qualunque questione di dato: spiega che cosa sia la sigla BACD e perché l'ordine invertito delle estrazioni del generatore sia la firma di un esemplare da evento, conferma quattro affermazioni del primo studio nominandone i metodi, chiude il punto che il primo lasciava aperto sulla derivazione del sesso dell'allenatore, distingue i due canali di distribuzione che il primo confondeva, e riporta il fatto più notevole della ricerca, cioè che il metodo di generazione dipende da un'interruzione hardware e non soltanto dal codice.

`EVENTI-GEN3.md` è il catalogo delle distribuzioni, con 177 voci, ed è generato da `tools/catalogo-eventi-gen3.py` a partire dalla tabella di `PKHeX`: non si modifica a mano, si rigenera. Dice per ciascun evento la specie, il livello, l'allenatore di provenienza, la lingua, l'identificativo, il metodo di generazione, la lucentezza ammessa e la derivazione del sesso dell'allenatore. È l'inventario da cui il track lavora, e la riga che riguarda gli esemplari che l'utente possiede è nel blocco italiano.

Non c'è ancora codice, e questo track non è per ora un progetto software: è ricerca e procedura operativa su hardware fisico. Se produrrà codice, il candidato naturale è la costruzione e la verifica delle strutture `.pk3` con `pokebridge`, che il ponte fra generazioni ha già scritto e collaudato.

## Che cosa questo track condivide con gli altri

Il legame più stretto è con la correzione del salvataggio di Smeraldo, e non è tematico ma materiale: la via di iniezione che non richiede né e-Reader né seconda console passa dal backup e dal ripristino del salvataggio, cioè esattamente da GBxCart RW e FlashGBX, lo stesso lettore ordinato il 18 agosto 2026 per quel track. Finché il lettore non arriva, tre delle quattro vie di iniezione restano chiuse.

Il legame con il ponte fra generazioni è la struttura del dato: un Pokemon di evento è una struttura di generazione 3 come le altre, cifrata, permutata e con il suo checksum, e `pokebridge/gen3.py` la sa leggere e scrivere. Ciò che un evento aggiunge è il modo in cui quella struttura viene generata, cioè il metodo pseudocasuale, che è la parte che distingue una ricreazione fedele da un dato costruito a mano.

Il legame con il modding del 3DS è la catena di trasferimento verso Home, che passa dalla quarta e dalla quinta generazione e quindi dalle cartucce DS di quel track, e infine da Bank sulla console. Su quell'ultimo tratto pesa un limite di perimetro dichiarato altrove e non riaperto qui: vedi la sezione seguente.

## Perimetro

Vale tutto ciò che `.claude/rules/hardware-and-perimeter.md` prescrive, e due punti vanno ripetuti qui perché questo track li tocca da vicino.

Il primo è il backup prima di ogni scrittura, in doppia copia su percorsi distinti e verificato leggibile, e il read-back verificato dopo. Ogni via di iniezione di un evento scrive sul salvataggio di una cartuccia di vent'anni: non esiste una seconda occasione, e una fonte fra quelle lette avverte esplicitamente che un salvataggio può contenere un evento non ancora preservato dalla comunità, che va esportato prima di sovrascrivere qualunque cosa.

Il secondo è che l'assistenza tecnica di questo progetto non copre l'installazione e l'uso di Pokemon Bank e Pokemon Transporter su questa console. Il limite è dichiarato nella regola e la sua motivazione sta fuori dal version control. Questo track ha un obiettivo che dipende da quell'ultimo tratto, quindi la contraddizione è reale e va decisa esplicitamente dall'utente invece di essere aggirata dentro un altro lavoro: è registrata come decisione aperta in `.claude/memory/pending.md`.

Sulla legittimità degli esemplari ricreati questo progetto non fa finta di niente. Un evento ricreato fedelmente riproduce il metodo di generazione dell'originale, quindi è coerente rispetto ai controlli che un verificatore sa fare, ma non è l'esemplare distribuito allora: è una copia costruita con la stessa procedura. La distinzione va dichiarata quando un esemplare viene scambiato o mostrato, e la si tiene scritta accanto al dato invece che nella memoria di chi lo ha prodotto.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| lo studio tecnico delle distribuzioni e delle vie di iniezione | `STUDIO-01-distribuzioni-gen3-e-ricreazione.md`, in questa cartella |
| i metodi di generazione, i due canali e la firma di un esemplare da evento | `STUDIO-02-metodi-di-generazione.md`, in questa cartella |
| l'inventario dei 177 eventi con il metodo di ciascuno | `EVENTI-GEN3.md`, generato, in questa cartella |
| la struttura di un Pokemon di generazione 3, byte per byte | `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`, sezioni 5 e 6 |
| perché esistono cifratura e checksum, spiegato | `docs/04-cifratura-gen3.md` e `docs/03-integrita-checksum.md` |
| il multiboot, cioè il canale su cui viaggia una distribuzione | `docs/10-multiboot-hardware.md` |
| le fonti di questo track, con il livello di affidabilità | `SOURCES.md` alla radice, colonna EVT |
| a che punto è il track e qual è il prossimo passo | `.claude/context/sub-distributions-events.md` |

Lo stato canonico del track vive nella scheda, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`. Questo file dice cos'è il sottoprogetto; quelli dicono a che punto è.
