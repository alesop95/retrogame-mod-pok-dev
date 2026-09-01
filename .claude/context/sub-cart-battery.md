---
generated-from-commit: a427431
generated-from-branch: main
generated-date: 2026-09-01
covers-paths:
  - cart-battery-restoration/
last-verified-commit: a427431
stato: runbook scritto; diagnosi conclusa il 2026-09-01, i due salvataggi sono perduti e l'operazione diventa di rischio basso
---

# Sottoprogetto: conservazione del supporto e sostituzione della batteria

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`.

Obiettivo: sostituire la batteria tampone delle cartucce di prima e seconda generazione, conservando il salvataggio dove ce n'è ancora uno. È l'unico track del progetto la cui scadenza non è annunciata da nessuno: è la carica residua di una pila saldata negli anni Novanta, e quando finisce il salvataggio non si degrada ma cessa di esistere. Su Rosso e Argento, che erano il punto di partenza, quella scadenza è già passata.

## Dove siamo

Il track nasce il 2026-09-01. Il runbook è in `cart-battery-restoration/STUDIO-01-batteria-e-ritenzione.md` ed è completo in dieci sezioni: come muore un salvataggio, la differenza fra le due generazioni, il segnale d'allarme della seconda, le due prove di diagnosi, il trabocchetto di tensione, l'estrazione, la sostituzione, il ripristino con il seguito sull'orologio, ciò che resta aperto, e la diagnosi su Rosso e Argento che chiude una parte del track lo stesso giorno in cui è nato.

La risposta alla domanda che ha aperto il track è no, e non è negoziabile: un salvataggio perduto per esaurimento della pila non si recupera, perché la memoria è volatile e i bit non sono danneggiati ma assenti. Tutto ciò che si può fare va fatto prima, e la finestra si chiude senza preavviso. Su queste due cartucce si è chiusa, e la risposta è passata da avvertimento a constatazione.

Il risultato più importante della giornata è però un altro, e riguarda il rischio invece della procedura. Il lettore impiegato da questo progetto, nella revisione in cui la tensione è controllata dal software, parte in modalità a tre virgola tre volt, e una testimonianza del canale del produttore riferisce che inserire una cartuccia di seconda generazione in quella condizione cancella il salvataggio, anche senza premere il pulsante di connessione. È un modo di perdere il dato prima di avere fatto alcun backup, il rimedio è una sequenza documentata, e va conosciuto prima di collegare qualunque cosa.

## La diagnosi, arrivata il 2026-09-01

L'utente riferisce che entrambe le cartucce, all'accensione, offrono soltanto la voce per una partita nuova e non conservano il salvataggio che si crea. È la firma completa della pila esaurita: l'assenza della voce di continuazione dice che il gioco non trova un salvataggio valido, e la mancata sopravvivenza di un salvataggio nuovo è la prova di ritenzione già eseguita con esito negativo. I due salvataggi non esistono più e non sono recuperabili.

La diagnosi chiude due delle domande aperte del track e sposta la priorità. Su queste cartucce non c'è nulla da estrarre, quindi l'ordine che imponeva l'estrazione prima della saldatura non si applica e l'operazione passa da rischio alto a rischio basso: resta il solo rischio meccanico della saldatura, che non è irreversibile sul dato perché il dato non c'è. Per la cartuccia di seconda generazione il seguito sull'orologio si riduce al primo dei tre passi, perché una partita nuova fissa da sé lo scostamento dell'ora.

## Prossimo passo concreto

Applicare la prova di ritenzione della sezione 4 del runbook a ogni altra cartuccia di prima o seconda generazione che esista, se ne esistono, perché quelle sono le sole che abbiano ancora una finestra e non si sa quanto sia larga. Su una cartuccia il cui salvataggio interessi, la prima operazione non è la prova ma l'estrazione, e attende il lettore.

Su Rosso e Argento resta la sostituzione, che non ha più fretta e può essere fatta quando conviene. Prima conviene leggere il valore stampato sulla pila dentro ciascuna, che va letto e non dedotto da una guida.

## Decisioni aperte

Se la saldatura la faccia l'utente o un servizio della comunità. Nella comunità del lettore la sostituzione con prova e spedizione di ritorno costa dell'ordine dei venti dollari, cioè meno di una cartuccia di quei titoli, e su una cartuccia di vent'anni l'errore non è un file ma una piazzola staccata. L'assistenza dell'agente finisce dove comincia il saldatore.

Chiusa il 2026-09-01: si monta un porta-pila. La decisione è dell'utente e la ragione va scritta perché guiderà anche le cartucce future. Saldare le linguette di una pila nuova risolve una volta e riporta il problema fra quindici anni nella medesima forma, cioè con un saldatore su una scheda che nel frattempo è invecchiata di altri quindici anni; un porta-pila sposta la saldatura una volta sola e rende ogni sostituzione successiva un gesto a mani nude. Su un progetto il cui obiettivo dichiarato è una collezione da tenere per tutta la vita, la scelta che riduce il numero di interventi futuri sul rame è quella giusta, e il costo è qualche minuto in più adesso.

Ne discende una conseguenza sull'acquisto che va detta prima di ordinare, perché altrimenti si ordina la cosa sbagliata: con il porta-pila la variante a linguette non serve più, e servono invece pile nude del formato corretto, che sono anche quelle che si trovano in qualunque negozio. Il formato si legge comunque sulla pila che sta dentro la cartuccia, e su questo la decisione non cambia nulla.

Resta aperto un solo punto subordinato, e non è una decisione ma una verifica: che il porta-pila scelto stia nello spazio disponibile dentro il guscio della cartuccia. Va confrontata l'altezza del supporto con lo spazio che la pila attuale occupa, prima dell'acquisto e non dopo.

## Evidenze e materiale locale

Nessun salvataggio entra nel repository, per ADR-005. Le due copie di backup prescritte dalla regola dell'hardware stanno su due percorsi distinti del disco locale.

Le testimonianze su cui il runbook poggia vengono dall'esportazione del canale di assistenza del produttore del lettore, che sta in `_notes/fonti/dce/` con i suoi estratti filtrati per parola chiave, non versionata e sacrificabile per ADR-016 ora che la sintesi con l'attribuzione è nel runbook.
