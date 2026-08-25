---
tipo: nota di studio
livello: fondamenta
tags: [salvataggio, hardware, backup]
up: "[[index]]"
vedi_anche: ["[[02-numeri-e-bit]]", "[[03-integrita-checksum]]", "[[22-strumenti]]"]
---

# Che cos'e' un salvataggio, e dove vive

Un salvataggio di un gioco Game Boy o Game Boy Advance non e' un file: e' il contenuto di un chip di memoria dentro la cartuccia, e diventa un file solo quando qualcuno lo copia fuori. La distinzione sembra pedante e non lo e', perche' spiega tutto il resto: perche' un salvataggio si perde, perche' non si puo' annullare una scrittura, e perche' il progetto ha una regola normativa sul backup invece di una raccomandazione.

Nelle generazioni 1 e 2 il chip e' una SRAM[^1] da 32 KiB, cioe' una memoria volatile che perde il contenuto quando resta senza corrente. Non lo perde perche' dentro la cartuccia c'e' una batteria al litio, saldata, che tiene alimentato quel solo chip anche quando la console e' spenta. Quella batteria e' un componente con una vita finita, tipicamente stimata in quindici o vent'anni, e quando finisce il salvataggio non si degrada: sparisce, tutto insieme, al primo spegnimento. Ogni cartuccia Gen 1 e Gen 2 in circolazione oggi ha superato di molto quella vita nominale.

Nella generazione 3 la situazione cambia, e non in modo uniforme. Rubino, Zaffiro e Smeraldo hanno ancora una batteria, ma non per il salvataggio: quello sta in una memoria flash da 128 KiB che non ha bisogno di alimentazione. La batteria alimenta il *real time clock*, l'orologio interno, che serve alle bacche, alle maree e agli eventi legati all'ora. Quando quella batteria muore il salvataggio resta, ma l'orologio si ferma, e il gioco mostra il messaggio sull'orologio interno che non funziona. Rosso Fuoco e Verde Foglia non hanno orologio e quindi non hanno batteria.

Questo spiega una confusione comune che vale chiarire subito, perche' cambia la diagnosi di un problema: su una cartuccia di Smeraldo una batteria scarica non spiega un salvataggio corrotto, mentre su una cartuccia di Cristallo lo spiega interamente.

## Perche' il backup e' una regola e non un consiglio

Il progetto ha una regola normativa, in `.claude/rules/hardware-and-perimeter.md`, che pretende un backup in doppia copia su due percorsi distinti, verificato leggibile, prima di ogni scrittura. La ragione e' che nessuna delle operazioni di cui si parla e' annullabile.

Quando si scrive sulla SRAM di una cartuccia, il contenuto precedente non e' spostato: e' sovrascritto. Non esiste un cestino, non esiste una cronologia, non esiste una copia di sicurezza fatta dal gioco, con una sola eccezione parziale che si vede in [[03-integrita-checksum]]. E il valore di cio' che si sovrascrive non e' ricostruibile: un salvataggio di vent'anni contiene Pokemon catturati in circostanze che non si ripetono, con dati che nessuna procedura sa rigenerare.

C'e' poi un secondo motivo, meno ovvio e piu' insidioso. Una scrittura puo' riuscire secondo il software e non restare sul chip, per esempio su cartucce con hardware di salvataggio non originale, e il modo di accorgersene non e' guardare la schermata del gioco ma rileggere i byte e confrontarli. Da qui la seconda regola del progetto, quella sul read-back verificato: una scrittura che nessuno ha riletto non e' una scrittura verificata.

## Come un salvataggio diventa un file

Per portare il contenuto della cartuccia su un computer serve un lettore, cioe' un dispositivo che si interpone fra la cartuccia e una porta USB e sa parlare il protocollo del bus della cartuccia. Il progetto usa un GBxCart RW pilotato da FlashGBX, e la scheda `STACK.md` ne registra le scelte e le alternative escluse.

Esistono almeno tre strade alternative, e conviene conoscerle perche' cambiano il perimetro di cio' che e' possibile. La prima e' un lettore commerciale diverso, per esempio il GB Operator, che fa la stessa cosa con un software proprio. La seconda e' una console modificata che legge la cartuccia dall'interno, che e' cio' che il track 3DS fa per le cartucce DS. La terza e' la piu' interessante per questo progetto: si puo' leggere e scrivere la SRAM senza alcun lettore, facendo eseguire codice al gioco stesso attraverso il cavo Link, ed e' esattamente cio' che fa `PkSploit`. Quest'ultima strada e' trattata in [[09-esecuzione-codice]] e non e' un trucco marginale: e' la stessa primitiva su cui poggia il ponte fra generazioni.

Una volta che il contenuto e' un file, il suo nome dipende dal software: `.sav` e `.srm` sono le estensioni piu' comuni e non implicano differenze di formato. La dimensione invece e' informativa: 32 KiB per un salvataggio Gen 1 o Gen 2, 128 KiB per un Gen 3, e una dimensione diversa e' il primo segnale che qualcosa non e' quello che sembra.

## Cosa leggere dopo

Prima di aprire un salvataggio conviene sapere come si leggono i numeri che contiene, e quello e' [[02-numeri-e-bit]]. Subito dopo viene il meccanismo che decide se il gioco accetta quei byte o li dichiara distrutti, cioe' [[03-integrita-checksum]].

[^1]: *SRAM*, Static Random Access Memory - memoria volatile che conserva il contenuto solo finche' e' alimentata, e che nelle cartucce Game Boy e' tenuta viva da una batteria tampone.
