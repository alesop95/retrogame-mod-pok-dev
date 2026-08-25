---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
last-verified-commit: d08a011
---

# Sviluppo e verifica

Non esistono test automatici perche' non esiste codice. Quello che esiste, e che vale la pena scrivere una volta invece di riscoprirlo a ogni sessione, e' un protocollo di verifica su hardware reale, dove l'errore e' irreversibile e il feedback non e' istantaneo.

## Il principio

Una operazione su hardware si considera riuscita solo quando e' stata riletta, non quando il software dice che e' andata bene. Questo vale a ogni livello: un dump si verifica confrontando la dimensione attesa e riaprendo il file, una scrittura su cartuccia si verifica rileggendola e confrontando i byte, una modifica al salvataggio si verifica accendendo la console e guardando lo stato del gioco. Le tre verifiche non sono ridondanti perche' falliscono in modi diversi.

## Protocollo per il sottoprogetto Smeraldo

Prima di qualunque scrittura si fa il backup del salvataggio in doppia copia su due percorsi distinti, e si verifica che entrambe le copie si aprano. Si registra il checksum del file originale, perche' e' l'unico riferimento che permette dopo di dire se la cartuccia e' tornata allo stato di partenza. Si apre il backup in PKHeX in sola lettura, per fotografare l'entita' del bug prima di decidere cosa correggere: e' lo step in cui si stabilisce quali slot e quali oggetti della tasca Strumenti Base vanno toccati, decisione oggi non presa perche' non presa e' l'unica risposta onesta finche' nessuno ha visto il contenuto. Si modifica, si riscrive, si rilegge, si confronta, e solo alla fine si accende il gioco.

Il criterio di successo dello step corrente e' piu' semplice e va chiuso prima di tutto il resto: in Gestione Dispositivi, sotto "Porte (COM e LPT)", deve comparire una voce USB-SERIAL CH340 con il suo numero di porta, senza punto esclamativo giallo.

## Protocollo per il sottoprogetto 3DS

Un dump si considera completato quando il file esiste in `/gm9/out/` sulla SD, ha una dimensione coerente con la cartuccia, ed e' stato trasferito sul disco del PC. Per le cartucce 3DS pubblicate dopo il 2014 la decrittazione richiede un file di seed generato con SEEDconv, e il sintomo di un seed mancante e' un errore esplicito di decrittazione, gia' incontrato e risolto su Omega Ruby: e' documentato nella sezione 5.4 dell'handoff e non va ridiagnosticato da zero.

## Riscontri visivi

Diversi passaggi di questo progetto sono verificabili solo guardando lo schermo di una console, che l'agente non puo' osservare. La regola `rules/manual-screenshots.md` copre il caso: quando serve un riscontro visivo lo si chiede esplicitamente e lo si legge. Gli screenshot che ne risultano restano in `_notes/`, non tracciati, per la politica sui media.
