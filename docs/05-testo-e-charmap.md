---
tipo: nota di studio
livello: intermedio
tags: [testo, charmap, transcodifica]
up: "[[index]]"
vedi_anche: ["[[02-numeri-e-bit]]", "[[22-strumenti]]", "[[DATA-FORMATS_Gen1-Gen2-Gen3]]"]
---

# Il testo: perché nessuna generazione usa ASCII, e come si transcodifica un nome

Un soprannome dentro un salvataggio non è testo nel senso in cui lo intende un linguaggio di programmazione moderno. È una sequenza di indici in una tabella di caratteri disegnata a mano dagli autori del gioco, ottimizzata per stare dentro la memoria video di quella console, e diversa fra le generazioni. Convertire un nome fra due generazioni è quindi una transcodifica, non una copia, ed è il punto del progetto dove un errore è più facile e meno visibile.

## Perché non ASCII

La ragione è che su queste console un carattere non è un'astrazione: è una piastrella grafica caricata in memoria video, e il codice del carattere è l'indice della piastrella. Gli autori hanno quindi ordinato la tabella secondo come conveniva alla grafica e al motore di testo, non secondo uno standard esterno, e hanno riservato interi intervalli a comandi di formattazione, a nomi variabili come quello del giocatore, e nelle versioni giapponesi a insiemi di caratteri completamente diversi.

Il risultato è che nelle generazioni 1 e 2 le lettere maiuscole cominciano a 0x80, le minuscole a 0xA0, le cifre stanno in fondo a 0xF6, lo spazio è 0x7F e il terminatore di stringa è 0x50. In generazione 3 la tabella è completamente riorganizzata: lo spazio è 0x00, le cifre stanno a 0xA1, le maiuscole a 0xBB, le minuscole a 0xD5 e il terminatore è 0xFF.

## L'errore silenzioso, con un esempio concreto

Questo progetto ha una dimostrazione di prima mano di quanto sia facile sbagliare qui, e vale la pena raccontarla perché è la ragione per cui esiste uno strumento invece di una tabella.

Durante la stesura della referenza tecnica, le fonti enciclopediche consultate collocavano le cifre di generazione 1 a 0xF0 invece di 0xF6, e le maiuscole di generazione 3 a 0xC1 invece di 0xBB. Sono scostamenti di sei byte in entrambi i casi. Un convertitore costruito su quei valori non fallisce: produce nomi in cui ogni lettera è sostituita da un'altra lettera esistente, quindi stampabile, quindi non sospetta a una verifica a occhio. Il tipo di bug che si scopre mesi dopo, guardando un Pokemon e chiedendosi perché si chiami in un modo che nessuno ha scelto.

La verifica è stata fatta leggendo i charmap dei disassemblati, che sono la definizione autorevole perché il gioco stesso viene compilato a partire da quei file, e in entrambi i casi le fonti secondarie avevano torto.

## La soluzione: generare, non trascrivere

La risposta strutturale non è correggere la tabella a mano, perché una tabella corretta a mano può essere sbagliata di nuovo a mano. La risposta è non scrivere mai la tabella: generarla dai charmap del disassemblato, e fare in modo che il generatore si rifiuti di produrre un file se alcuni valori di controllo non tornano.

Lo strumento è `pokemon-gen12-gen3-bridge-original-hardware/tools/extract_charmaps.py`, descritto in [[22-strumenti]], e produce tre file. I primi due sono le due tabelle, byte per carattere, con i token di controllo tenuti separati dai caratteri stampabili e con l'indicazione del commit da cui provengono. Il terzo è quello che il convertitore usa davvero: la traduzione diretta dal byte Gen 1 e 2 al byte Gen 3 che rende lo stesso carattere.

Quel terzo file porta alla luce una decisione che altrimenti resterebbe implicita. Su duecento caratteri stampabili di generazione 1 e 2, centoquarantasette hanno una destinazione in generazione 3 e cinquantatre no: sono caratteri che in generazione 3 semplicemente non esistono, per esempio i kana giapponesi e i caratteri di disegno delle cornici. Che cosa fare di un nome che li contiene non è un problema di codifica, è una decisione di prodotto, e il file la rende visibile invece di lasciarla al primo `KeyError` in produzione.

## Le altre due trappole

La lunghezza non coincide. In generazione 1 e 2 un nome sta in undici byte, cioè dieci caratteri più il terminatore. In generazione 3 il soprannome ha dieci byte e il nome dell'allenatore soltanto sette. Un nome di allenatore lungo va quindi troncato, e il troncamento è un'altra decisione da prendere esplicitamente.

I codici di controllo sono peggio. In generazione 3, 0xFC introduce sequenze di formattazione, 0xFD introduce variabili di testo come il nome del giocatore, e 0xFE è un'interruzione di riga. Un byte di questi finito dentro un soprannome per un errore di transcodifica non è un carattere sbagliato: è un comando dentro un nome, e il gioco lo esegue. Da qui la regola che un writer deve validare l'uscita della transcodifica contro l'insieme dei byte ammessi in un nome, e non fidarsi della tabella.

## Cosa leggere dopo

[[06-identita-pokemon]] tratta gli altri campi che identificano un Pokemon, e [[22-strumenti]] spiega come si rilancia la generazione delle tabelle.
