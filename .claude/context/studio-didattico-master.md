---
covers-paths: []
last-verified-commit: 7a8bdae
---

# Studio didattico master - come e perché retrogame-mod-pok-dev è stato costruito

> Documento didattico principale ed evolutivo. Cresce a ogni modifica di codice significativa, e il suo scopo è far capire, rileggendolo, come il progetto è stato costruito e perché, mettendo sempre a confronto due cose: com'era stata scritta la prima stesura e come è stata migliorata. L'enfasi sta nella contrapposizione, perché è lì che si impara: non basta vedere il codice buono, serve vedere accanto quello che sostituisce e capire che cosa lo rendeva fragile.
>
> Come si legge. Questo file è l'indice narrativo e il confronto ad alto livello: si legge per il quadro e per il perché. Ogni voce rimanda a una scheda di dettaglio `refactor-NN-<slug>.md` nella stessa cartella, che entra nel codice riga per riga.
>
> Come si aggiorna. A ogni refactor o scelta di qualità non ovvia si aggiunge qui una voce con la struttura fissa in quattro parti, in fondo e senza toccare le voci precedenti, e si crea la scheda di dettaglio corrispondente. Il work-log `.claude/memory/progress.md` resta il registro sintetico dei fatti; questo file è il racconto del perché. I due non si sostituiscono: il fatto sopravvive al ragionamento che lo ha prodotto, ed è il ragionamento che si perde per primo.
>
> Il numero di una voce non si riusa mai, nemmeno quando una scheda viene superata: una scheda superata si marca come tale e resta, perché il rimando che qualcuno ha scritto altrove deve continuare a puntare a qualcosa.

## Indice delle voci

Nessuna voce ancora. La pratica è adottata dal 2026-09-29, al gate dei pacchetti dell'allineamento al template (pacchetto `documentazione-didattica`); le voci nascono dalla prima scelta non ovvia successiva, e non si ricostruiscono a posteriori per il lavoro precedente, che resta raccontato in `memory/progress.md`, in `memory/decisions.md` e nella tesi. Il controllo è `python tools/lint-didattica.py`, e la procedura è la skill `studio-didattico`.
