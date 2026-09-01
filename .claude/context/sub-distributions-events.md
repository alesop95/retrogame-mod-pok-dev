---
generated-from-commit: 0529162
generated-from-branch: main
generated-date: 2026-08-28
covers-paths:
  - recreate-pokemon-distributions-events/
last-verified-commit: 319226b
stato: attivo, ricerca sui metodi conclusa, in attesa del lettore per la prova su dato autentico
---

# Sottoprogetto: ricreazione delle distribuzioni e degli eventi

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`.

Obiettivo: ricreare su hardware originale e su cartucce possedute le distribuzioni di eventi di generazione 3, come gamba mancante di un obiettivo dichiarato più grande, cioè avere in Pokemon Home tutte le 1025 specie e le forme alternative, e portare avanti quella collezione come lavoro di una vita.

## Dove siamo

Il track nasce il 2026-08-28. Le quattro fonti video indicate dall'utente sono state lette per trascrizione lo stesso giorno e la conoscenza sta in `recreate-pokemon-distributions-events/STUDIO-01-distribuzioni-gen3-e-ricreazione.md`: il canale è il multiboot, la difesa della ROM di distribuzione è un checksum additivo aggiustabile, i parametri dell'esemplare si impostano per indice e l'indice si può sostituire, e la comunità ha già ricreato l'intero corpus inglese, giapponese e da GameCube, lasciando aperti tre casi che dichiara tali. Le quattro vie di iniezione in una cartuccia vera sono documentate, e tre delle quattro passano dal backup e dal ripristino del salvataggio.

Il 2026-08-29 la ricerca è passata dal quarto al terzo livello di affidabilità, e il guadagno è sostanziale. La tabella degli eventi di PKHeX dichiara per ciascuna delle 177 distribuzioni il proprio metodo di generazione, quindi il metodo non è una congettura da ricostruire ma un dato da leggere: il catalogo è `EVENTI-GEN3.md`, generato e non scritto a mano. La seconda nota di studio spiega che la sigla BACD nomina l'ordine invertito con cui le estrazioni compongono valore di personalità e valori individuali, e che quell'inversione è la firma di un esemplare da evento; conferma quattro affermazioni della prima nota, chiude il punto che quella lasciava aperto, distingue i due canali di distribuzione che confondeva, e riporta che il metodo dipende da un'interruzione hardware e non dal solo codice. Gli esemplari che l'utente possiede dal Pokemon Day del 2006 sono identificati con precisione e sono il primo vettore di prova autentico del progetto.

La scadenza è verificata su fonte ufficiale e non è del progetto: Pokemon Bank chiude il 26 febbraio 2027, e con essa l'unico ingresso verso Home per tutto ciò che precede l'ottava generazione. Il tempo residuo va scritto come conteggio a una data e non come durata, perché una durata invecchia in silenzio: al 2026-09-01 restano centosettantotto giorni, cioè meno di sei mesi. La scheda ha dichiarato per quattro giorni diciotto mesi, che era sbagliato per un fattore tre nel verso che rassicura.

## Prossimo passo concreto

Verificare se un verificatore di legittimità accetti un esemplare prodotto da una ricreazione fedele, costruendone uno con `pokebridge` e sottoponendolo a PKHeX. Il passo non è cambiato ma la domanda è diventata più precisa il 2026-08-29: si sa ora che quel verificatore controlla la relazione fra valore di personalità e valori individuali, dichiarata evento per evento come metodo di generazione, quindi la risposta attesa è positiva per una ricreazione che riproduca il metodo. Attesa non è verificata, e la prova costa poco.

Esiste un secondo passo che non richiede hardware e che la ricerca ha reso possibile: leggere l'archivio degli eventi di Project Pokemon per stabilire se i campioni degli eventi dichiarati non chiusi manchino davvero, cioè se il progetto possa contribuire alla conservazione invece di consumarla soltanto.

## Decisioni aperte

La contraddizione fra l'obiettivo e il perimetro è reale e va decisa dall'utente, non aggirata: l'ultimo tratto della catena passa da Pokemon Bank e Pokemon Transporter su questa console, e l'assistenza su quei due titoli è esclusa dalla regola `hardware-and-perimeter.md` per una motivazione che sta fuori dal version control. Fino a quella decisione il track lavora su tutto ciò che precede quel tratto. La voce sta in `pending.md`.

Resta da decidere quali eventi ricreare e in quale ordine, perché il corpus è vasto e il criterio non è ovvio: le specie e le forme che mancano alla collezione non coincidono con gli eventi più facili da ricreare.

## Evidenze e materiale locale

Le trascrizioni delle quattro fonti stanno in `_notes/fonti/`, non versionate, e sono sacrificabili una volta che ADR-016 è soddisfatto, cioè ora. Nessun dump, nessun salvataggio e nessuna ROM entra nel repository.

Il catalogo `EVENTI-GEN3.md` è generato da un clone di PKHeX che vive fuori dal repository: il percorso si passa sulla riga di comando a `tools/catalogo-eventi-gen3.py`, come per i disassemblati, e il comando di verifica è quello stesso strumento con `--check`.

Gli esemplari con allenatore `10ANNI` vivono sulla cartuccia dell'utente e sono il primo dato autentico del progetto. Non entrano in git in nessuna forma; ciò che entra è il confronto fra i loro campi e la riga del catalogo.

## Aggiunta del 2026-09-01: la nota operativa, e la divisione del lavoro

`STUDIO-04-campagna-di-trasferimento-e-il-tracciatore.md` è la nota da leggere quando si opera, e contiene tre cose che le altre non avevano. La prima è che il tracciatore di Pokemon Home non ostacola il piano di iniettare esemplari e percorrere la catena ufficiale, perché il servizio lo assegna a chiunque entri da una porta vera: ostacola una cosa diversa, cioè scrivere un esemplare di terza generazione dentro un salvataggio di nona, che è una via che non esiste e non una via che scade. La seconda è il tempo residuo contato, che al 2026-09-01 è di centosettantotto giorni e non di diciotto mesi come tre file dichiaravano. La terza è la divisione del lavoro fra il nostro codice e il verificatore della comunità.

Quella divisione va tenuta presente perché evita di rifare ciò che esiste. La produzione in volume la fa il verificatore dalla propria base di dati dei doni segreti, che porta le medesime centosettantasette voci del nostro catalogo contro le diciassette del corpus su cui il nostro generatore lavora. Il nostro codice serve a tre cose che quella via non dà: la comprensione, perché le formule sono scritte, svolte bit per bit e verificate; la verifica incrociata, che ha già trovato due difetti reali in una implementazione di terzi; e la ricerca inversa, che dato un esemplare autentico posseduto ne ricava il seme, ed è il solo modo di stabilire che una ricreazione sia fedele a un originale e non soltanto conforme a una tabella. Quest'ultima è quella che conterà quando il lettore arriverà e gli esemplari del decennale saranno estratti dalla cartuccia.
