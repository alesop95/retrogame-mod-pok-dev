---
generated-from-commit: a427431
generated-from-branch: main
generated-date: 2026-09-01
covers-paths:
  - cart-battery-restoration/
last-verified-commit: a427431
stato: runbook scritto e verificato sulle fonti; bloccato sull'arrivo del lettore e su due misure
---

# Sottoprogetto: conservazione del supporto e sostituzione della batteria

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`.

Obiettivo: sostituire la batteria tampone delle cartucce di prima e seconda generazione, cominciando da Rosso e Argento, conservando il salvataggio che vi si trova. È l'unico track del progetto la cui scadenza non è annunciata da nessuno: è la carica residua di una pila saldata nel 1998, e quando finisce il salvataggio non si degrada ma cessa di esistere.

## Dove siamo

Il track nasce il 2026-09-01. Il runbook è in `cart-battery-restoration/STUDIO-01-batteria-e-ritenzione.md` ed è completo sulle nove sezioni che servono: come muore un salvataggio, la differenza fra le due generazioni, il segnale d'allarme della seconda, le due prove di diagnosi, il trabocchetto di tensione, l'estrazione, la sostituzione, il ripristino con il seguito sull'orologio, e ciò che resta aperto.

La risposta alla domanda che ha aperto il track è no, e non è negoziabile: un salvataggio perduto per esaurimento della pila non si recupera, perché la memoria è volatile e i bit non sono danneggiati ma assenti. Tutto ciò che si può fare va fatto prima, e la finestra si chiude senza preavviso.

Il risultato più importante della giornata è però un altro, e riguarda il rischio invece della procedura. Il lettore impiegato da questo progetto, nella revisione in cui la tensione è controllata dal software, parte in modalità a tre virgola tre volt, e una testimonianza del canale del produttore riferisce che inserire una cartuccia di seconda generazione in quella condizione cancella il salvataggio, anche senza premere il pulsante di connessione. È un modo di perdere il dato prima di avere fatto alcun backup, il rimedio è una sequenza documentata, e va conosciuto prima di collegare qualunque cosa.

## Prossimo passo concreto

Due misure che non richiedono il lettore e che vanno fatte nell'ordine. La prima è accendere la console con la cartuccia di seconda generazione e guardare se il salvataggio esista ancora e se compaia il messaggio sull'esaurimento della batteria: è l'unica operazione che non consuma nulla e decide l'urgenza di tutto il resto. La seconda è aprire le due cartucce e leggere il valore stampato sulla pila, che va letto e non dedotto da una guida, perché le revisioni di scheda differiscono.

Se la seconda prova si fa con un multimetro, si misura anche la tensione senza rimuovere la pila: tre volt e qualcosa è sana, poco più di due è alla fine della finestra, sotto due è fuori specifica.

Poi si attende il lettore, perché l'estrazione precede la saldatura e non viceversa.

## Decisioni aperte

Se la saldatura la faccia l'utente o un servizio della comunità. Nella comunità del lettore la sostituzione con prova e spedizione di ritorno costa dell'ordine dei venti dollari, cioè meno di una cartuccia di quei titoli, e su una cartuccia di vent'anni l'errore non è un file ma una piazzola staccata. L'assistenza dell'agente finisce dove comincia il saldatore.

Se montare un porta-pila invece di saldare le linguette della pila nuova. Costa un poco più di lavoro adesso e rende la sostituzione successiva un gesto senza saldatore, quindi su cartucce che si vogliono conservare a vita è probabilmente la scelta giusta; non è stata presa.

## Evidenze e materiale locale

Nessun salvataggio entra nel repository, per ADR-005. Le due copie di backup prescritte dalla regola dell'hardware stanno su due percorsi distinti del disco locale.

Le testimonianze su cui il runbook poggia vengono dall'esportazione del canale di assistenza del produttore del lettore, che sta in `_notes/fonti/dce/` con i suoi estratti filtrati per parola chiave, non versionata e sacrificabile per ADR-016 ora che la sintesi con l'attribuzione è nel runbook.
