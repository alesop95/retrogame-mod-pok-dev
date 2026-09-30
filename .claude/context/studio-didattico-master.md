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

La pratica è adottata dal 2026-09-29, al gate dei pacchetti dell'allineamento al template (pacchetto `documentazione-didattica`); le voci nascono dalla prima scelta non ovvia successiva, e non si ricostruiscono a posteriori per il lavoro precedente, che resta raccontato in `memory/progress.md`, in `memory/decisions.md` e nella tesi. Il controllo è `python tools/lint-didattica.py`, e la procedura è la skill `studio-didattico`.

| Voce | Titolo | Data | Scheda |
|---|---|---|---|
| 1 | Un elenco di specie letto come un elenco di forme | 2026-09-30 | `refactor-01-forme-di-battaglia.md` |

## 1. Un elenco di specie letto come un elenco di forme

Contesto. Il 2026-09-29 tre video consegnati dal proprietario nominavano il Greninja con Morfosi della demo di Sole e Luna come un esemplare da portare nel deposito prima della chiusura della banca. La checklist del progetto lo dichiarava invece «forma di sola battaglia: non può stare in una scatola», cioè fuori dall'obiettivo. Una delle due affermazioni era sbagliata, e interrogare la libreria del verificatore ha detto quale.

Com'era e perché era fragile. `tools/checklist-pokedex.py` costruiva l'insieme delle forme di battaglia leggendo dal sorgente di PKHeX i due elenchi `BattleMegas` e `BattleForms` di `Legality/Tables/FormInfo.cs`, che sono elenchi di specie, e poi marcava di sola battaglia ogni forma non base di una specie presente in quegli elenchi. Nella libreria quei due elenchi sono soltanto un filtro d'ingresso: la decisione vera sta in due espressioni che, specie per specie, separano le forme di battaglia dalle altre, per esempio Greninja è di battaglia solo nella forma 2, Minior solo sotto la 7, Ogerpon solo dalla 4. Lo strumento aveva quindi un perimetro implicito sbagliato, e l'errore non produceva alcun sintomo: 29 forme che si depositano, fra cui Raichu di Alola, Floette, Zygarde 10%, Necrozma, le maschere di Ogerpon e il Greninja con Morfosi, sparivano dall'obiettivo con una motivazione plausibile scritta accanto.

Il salto senior e perché è meglio. Quando la regola vive nel codice di un'altra base e non in una tabella, non la si imita leggendone il sorgente: la si fa valutare a quella base. `tools/pkhex-forme-battaglia` chiede a `FormInfo.IsBattleOnlyForm` la risposta per ogni specie e ogni indice di forma, la scrive in JSON con il commit del clone, e la checklist la legge per coppia. La verifica che la correzione misuri davvero il difetto è il diff della checklist rigenerata: cambiano esattamente le 29 righe attese, più Spinda corretta nello stesso giro, e nient'altro. Il compromesso dichiarato è una dipendenza in più, un file generato da un programma C#, che la checklist legge da `_notes/forme-di-battaglia.json` e che va rigenerato quando il clone si aggiorna.

Dove leggere il dettaglio: `refactor-01-forme-di-battaglia.md`.
