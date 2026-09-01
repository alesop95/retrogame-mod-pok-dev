---
generated-from-commit: 809289a
generated-from-branch: main
generated-date: 2026-08-31
covers-paths:
  - poke-ace/
last-verified-commit: 809289a
stato: due studi scritti; bloccato su una decisione, e la verifica pratica resta impossibile prima di ottobre 2026
---

# Sottoprogetto: esecuzione di codice arbitrario come via di generazione

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`.

Obiettivo: impiegare l'esecuzione di codice arbitrario nei giochi di terza generazione per scrivere dati di esemplari direttamente nel salvataggio, come via per ottenere ciò che nessuna via di gioco può più dare, al servizio dell'obiettivo dichiarato di una collezione completa in Pokemon Home.

## Dove siamo

Il track nasce il 2026-08-31 e ha due studi. Il primo, `poke-ace/STUDIO-01-ace-e-legalita-in-home.md`, contiene l'inventario degli strumenti della comunità con la funzione di ciascuno, undici voci fra generatori, convertitori, guide ed editor, nessuno eseguito e la maggior parte non aperti. La tecnica in sé il progetto la documenta già in `docs/09-esecuzione-codice.md`, dove serve al ponte fra generazioni: la novità è il suo uso come strumento di generazione invece che di trasferimento.

Il secondo, `poke-ace/STUDIO-02-marchi-di-origine-e-che-cosa-conta-una-collezione.md`, chiude con dati un punto che il primo lasciava aperto, ed è stato prodotto sondando per costanti il fascio JavaScript compilato della lista di controllo indicata dall'utente, che nessuna richiesta HTTP restituisce. Due esiti. L'informazione di provenienza è categorica e visibile all'utente, cioè un marchio scelto in un insieme di undici, e la riedizione della terza generazione ne ha uno proprio che il codice tratta come non ancora ottenibile: un esemplare entrato dalla porta nuova sarà quindi distinguibile a occhio da uno passato per la catena storica, che non porta alcun marchio. E la lista di controllo non è una lista ma un insieme parametrico con quindici profili, la cui cardinalità differisce di un ordine di grandezza, il che rende malposta la domanda se sia completa e impone di precisare l'obiettivo del progetto scegliendo un profilo.

Il punto che governa il track è una domanda con risposta verificata in tre parti. I byte prodotti possono essere identici a quelli autentici. Home però conserva sul proprio lato la via da cui un esemplare è entrato, quindi a parità di dati la storia differisce. E la politica ufficiale sui dati alterati elenca fra le sanzioni la sospensione dell'accesso a Home, a discrezione del titolare e senza rimborso. La verifica pratica è impossibile prima di ottobre 2026, perché la compatibilità che la renderebbe testabile non esiste ancora.

## Prossimo passo concreto

Non è tecnico ed è una decisione dell'utente: se impiegare la tecnica sull'account che custodisce la collezione, sapendo che la sanzione dichiarata è la sospensione dell'accesso a quel medesimo account. Lo studio espone i termini reali e non li ammorbidisce, e dal secondo studio viene un elemento nuovo che la decisione deve includere: la provenienza non resta interna al servizio ma è stampata sull'esemplare, quindi non esiste la variante prudente in cui l'esito passa inosservato. Finché la decisione non è presa, il track resta studio.

Esiste un passo che non richiede la decisione e che conviene fare prima: confrontare i dati che il costruttore di esemplari produce per una distribuzione di evento con quelli che il track delle distribuzioni ricostruisce dal metodo di generazione. È un confronto fattibile senza hardware e senza toccare alcun account, e falsificherebbe o confermerebbe entrambe le vie in un colpo.

## Decisioni aperte

Se impiegare la tecnica, e su quale account. La differenza rispetto alle altre decisioni di rischio già prese in questo progetto è che l'oggetto esposto non è un account accessorio ma il contenitore dell'obiettivo dichiarato.

Se, ammesso che si usi, la si usi soltanto per ciò che nessuna via legittima può dare, che è il caso in cui il track ha senso, oppure anche per ciò che si potrebbe ottenere giocando o trasferendo. La prima lettura è quella che lo studio raccomanda.

Quale profilo di collezione sia l'obiettivo. È una decisione nuova, aperta dal secondo studio, e non è del solo track: fra il profilo minimo e quello che conta una casella per specie e per marchio di origine la cardinalità differisce di un ordine di grandezza, quindi finché non è presa non si sa quale lavoro sia necessario e quale superfluo. Va decisa nominando le dimensioni, cioè quali marchi, quali collezioni, quali forme, quali differenze di sesso e quali livelli di reperibilità.

## Evidenze e materiale locale

Nessun salvataggio, nessun dump e nessuna ROM entra nel repository. La trascrizione del video sta in `_notes/fonti/`, non versionata, ed è sacrificabile per ADR-016 ora che il suo contenuto è nello studio e nel registro delle fonti.

Il server di community da cui viene l'inventario degli strumenti va aggiunto alla tabella dei canali di `tools/export-discord.py`: il suo canale `ace-links` è la fonte, e l'inventario è stato consegnato a mano dall'utente.
