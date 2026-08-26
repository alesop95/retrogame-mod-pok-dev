---
tipo: nota di studio
livello: fondamenta
tags: [salvataggio, hardware, backup]
up: "[[index]]"
vedi_anche: ["[[02-numeri-e-bit]]", "[[03-integrita-checksum]]", "[[22-strumenti]]"]
---

# Che cos'è un salvataggio, e dove vive

Un salvataggio di un gioco Game Boy o Game Boy Advance non è un file: è il contenuto di un chip di memoria dentro la cartuccia, e diventa un file solo quando qualcuno lo copia fuori. La distinzione sembra pedante e non lo è, perché spiega tutto il resto: perché un salvataggio si perde, perché non si può annullare una scrittura, e perché il progetto ha una regola normativa sul backup invece di una raccomandazione.

Nelle generazioni 1 e 2 il chip è una SRAM[^1] da 32 KiB, cioè una memoria volatile che perde il contenuto quando resta senza corrente. Non lo perde perché dentro la cartuccia c'è una batteria al litio, saldata, che tiene alimentato quel solo chip anche quando la console è spenta. Quella batteria è un componente con una vita finita, tipicamente stimata in quindici o vent'anni, e quando finisce il salvataggio non si degrada: sparisce, tutto insieme, al primo spegnimento. Ogni cartuccia Gen 1 e Gen 2 in circolazione oggi ha superato di molto quella vita nominale.

Nella generazione 3 la situazione cambia, e non in modo uniforme. Rubino, Zaffiro e Smeraldo hanno ancora una batteria, ma non per il salvataggio: quello sta in una memoria flash da 128 KiB che non ha bisogno di alimentazione. La batteria alimenta il *real time clock*, l'orologio interno, che serve alle bacche, alle maree e agli eventi legati all'ora. Quando quella batteria muore il salvataggio resta, ma l'orologio si ferma, e il gioco mostra il messaggio sull'orologio interno che non funziona. Rosso Fuoco e Verde Foglia non hanno orologio e quindi non hanno batteria.

Questo spiega una confusione comune che vale chiarire subito, perché cambia la diagnosi di un problema: su una cartuccia di Smeraldo una batteria scarica non spiega un salvataggio corrotto, mentre su una cartuccia di Cristallo lo spiega interamente.

## Perché il backup è una regola e non un consiglio

Il progetto ha una regola normativa, in `.claude/rules/hardware-and-perimeter.md`, che pretende un backup in doppia copia su due percorsi distinti, verificato leggibile, prima di ogni scrittura. La ragione è che nessuna delle operazioni di cui si parla è annullabile.

Quando si scrive sulla SRAM di una cartuccia, il contenuto precedente non è spostato: è sovrascritto. Non esiste un cestino, non esiste una cronologia, non esiste una copia di sicurezza fatta dal gioco, con una sola eccezione parziale che si vede in [[03-integrita-checksum]]. E il valore di ciò che si sovrascrive non è ricostruibile: un salvataggio di vent'anni contiene Pokemon catturati in circostanze che non si ripetono, con dati che nessuna procedura sa rigenerare.

C'è poi un secondo motivo, meno ovvio e più insidioso. Una scrittura può riuscire secondo il software e non restare sul chip, per esempio su cartucce con hardware di salvataggio non originale, e il modo di accorgersene non è guardare la schermata del gioco ma rileggere i byte e confrontarli. Da qui la seconda regola del progetto, quella sul read-back verificato: una scrittura che nessuno ha riletto non è una scrittura verificata.

## Come un salvataggio diventa un file

Per portare il contenuto della cartuccia su un computer serve un lettore, cioè un dispositivo che si interpone fra la cartuccia e una porta USB e sa parlare il protocollo del bus della cartuccia. Il progetto usa un GBxCart RW pilotato da FlashGBX, e la scheda `STACK.md` ne registra le scelte e le alternative escluse.

Esistono almeno tre strade alternative, e conviene conoscerle perché cambiano il perimetro di ciò che è possibile. La prima è un lettore commerciale diverso, per esempio il GB Operator, che fa la stessa cosa con un software proprio. La seconda è una console modificata che legge la cartuccia dall'interno, che è ciò che il track 3DS fa per le cartucce DS. La terza è la più interessante per questo progetto: si può leggere e scrivere la SRAM senza alcun lettore, facendo eseguire codice al gioco stesso attraverso il cavo Link, ed è esattamente ciò che fa `PkSploit`. Quest'ultima strada è trattata in [[09-esecuzione-codice]] e non è un trucco marginale: è la stessa primitiva su cui poggia il ponte fra generazioni.

Una volta che il contenuto è un file, il suo nome dipende dal software: `.sav` e `.srm` sono le estensioni più comuni e non implicano differenze di formato. La dimensione invece è informativa: 32 KiB per un salvataggio Gen 1 o Gen 2, 128 KiB per un Gen 3, e una dimensione diversa è il primo segnale che qualcosa non è quello che sembra.

## Cosa leggere dopo

Prima di aprire un salvataggio conviene sapere come si leggono i numeri che contiene, e quello è [[02-numeri-e-bit]]. Subito dopo viene il meccanismo che decide se il gioco accetta quei byte o li dichiara distrutti, cioè [[03-integrita-checksum]].

[^1]: *SRAM*, Static Random Access Memory - memoria volatile che conserva il contenuto solo finché è alimentata, e che nelle cartucce Game Boy è tenuta viva da una batteria tampone.
