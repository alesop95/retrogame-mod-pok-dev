---
generated-from-commit: 0529162
generated-from-branch: main
generated-date: 2026-08-28
covers-paths:
  - recreate-pokemon-distributions-events/
last-verified-commit: 0529162
stato: attivo in ricerca, con una scadenza esterna al 26 febbraio 2027
---

# Sottoprogetto: ricreazione delle distribuzioni e degli eventi

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`.

Obiettivo: ricreare su hardware originale e su cartucce possedute le distribuzioni di eventi di generazione 3, come gamba mancante di un obiettivo dichiarato più grande, cioè avere in Pokemon Home tutte le 1025 specie e le forme alternative, e portare avanti quella collezione come lavoro di una vita.

## Dove siamo

Il track nasce il 2026-08-28. Le quattro fonti video indicate dall'utente sono state lette per trascrizione lo stesso giorno e la conoscenza sta in `recreate-pokemon-distributions-events/STUDIO-01-distribuzioni-gen3-e-ricreazione.md`: il canale è il multiboot, la difesa della ROM di distribuzione è un checksum additivo aggiustabile, i parametri dell'esemplare si impostano per indice e l'indice si può sostituire, e la comunità ha già ricreato l'intero corpus inglese, giapponese e da GameCube, lasciando aperti tre casi che dichiara tali. Le quattro vie di iniezione in una cartuccia vera sono documentate, e tre delle quattro passano dal backup e dal ripristino del salvataggio.

La scadenza è verificata su fonte ufficiale e non è del progetto: Pokemon Bank chiude il 26 febbraio 2027, e con essa l'unico ingresso verso Home per tutto ciò che precede l'ottava generazione. Restano diciotto mesi.

## Prossimo passo concreto

Verificare se un verificatore di legittimità accetti un esemplare prodotto da una ricreazione fedele, costruendone uno con `pokebridge` e sottoponendolo a PKHeX. È il controllo che decide se il track raggiunga il suo obiettivo o produca esemplari inutilizzabili in Home, costa poco e non richiede hardware.

## Decisioni aperte

La contraddizione fra l'obiettivo e il perimetro è reale e va decisa dall'utente, non aggirata: l'ultimo tratto della catena passa da Pokemon Bank e Pokemon Transporter su questa console, e l'assistenza su quei due titoli è esclusa dalla regola `hardware-and-perimeter.md` per una motivazione che sta fuori dal version control. Fino a quella decisione il track lavora su tutto ciò che precede quel tratto. La voce sta in `pending.md`.

Resta da decidere quali eventi ricreare e in quale ordine, perché il corpus è vasto e il criterio non è ovvio: le specie e le forme che mancano alla collezione non coincidono con gli eventi più facili da ricreare.

## Evidenze e materiale locale

Le trascrizioni delle quattro fonti stanno in `_notes/fonti/`, non versionate, e sono sacrificabili una volta che ADR-016 è soddisfatto, cioè ora. Nessun dump, nessun salvataggio e nessuna ROM entra nel repository.
