---
covers-paths: []
last-verified-commit: d770a37
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
| 2 | Una chiave che sapeva solo l'ultima cartella | 2026-10-07 | `refactor-02-chiave-del-lotto.md` |
| 3 | Un controllo che saltava ciò che non sapeva misurare | 2026-10-07 | `refactor-03-capitoli-senza-timbro.md` |

## 1. Un elenco di specie letto come un elenco di forme

Contesto. Il 2026-09-29 tre video consegnati dal proprietario nominavano il Greninja con Morfosi della demo di Sole e Luna come un esemplare da portare nel deposito prima della chiusura della banca. La checklist del progetto lo dichiarava invece «forma di sola battaglia: non può stare in una scatola», cioè fuori dall'obiettivo. Una delle due affermazioni era sbagliata, e interrogare la libreria del verificatore ha detto quale.

Com'era e perché era fragile. `tools/checklist-pokedex.py` costruiva l'insieme delle forme di battaglia leggendo dal sorgente di PKHeX i due elenchi `BattleMegas` e `BattleForms` di `Legality/Tables/FormInfo.cs`, che sono elenchi di specie, e poi marcava di sola battaglia ogni forma non base di una specie presente in quegli elenchi. Nella libreria quei due elenchi sono soltanto un filtro d'ingresso: la decisione vera sta in due espressioni che, specie per specie, separano le forme di battaglia dalle altre, per esempio Greninja è di battaglia solo nella forma 2, Minior solo sotto la 7, Ogerpon solo dalla 4. Lo strumento aveva quindi un perimetro implicito sbagliato, e l'errore non produceva alcun sintomo: 29 forme che si depositano, fra cui Raichu di Alola, Floette, Zygarde 10%, Necrozma, le maschere di Ogerpon e il Greninja con Morfosi, sparivano dall'obiettivo con una motivazione plausibile scritta accanto.

Il salto senior e perché è meglio. Quando la regola vive nel codice di un'altra base e non in una tabella, non la si imita leggendone il sorgente: la si fa valutare a quella base. `tools/pkhex-forme-battaglia` chiede a `FormInfo.IsBattleOnlyForm` la risposta per ogni specie e ogni indice di forma, la scrive in JSON con il commit del clone, e la checklist la legge per coppia. La verifica che la correzione misuri davvero il difetto è il diff della checklist rigenerata: cambiano esattamente le 29 righe attese, più Spinda corretta nello stesso giro, e nient'altro. Il compromesso dichiarato è una dipendenza in più, un file generato da un programma C#, che la checklist legge da `_notes/forme-di-battaglia.json` e che va rigenerato quando il clone si aggiorna.

Dove leggere il dettaglio: `refactor-01-forme-di-battaglia.md`.

## 2. Una chiave che sapeva solo l'ultima cartella

Contesto. Il registro unico dei giudizi della libreria, `recreate-pokemon-distributions-events/giudizi-pkhex-core.json`, è ciò su cui la checklist decide se una voce è «prodotta e conforme»: cerca il file del lotto, ne calcola l'impronta e la confronta con quella giudicata. Il 2026-10-06 si è visto che le 376 voci del complemento del Rubino avevano chiave `esemplari/...`, senza il nome del lotto.

Com'era e perché era fragile. `tools/pkhex-giudica` costruiva la chiave con il solo ultimo componente del percorso della cartella giudicata. Per i lotti di primo livello l'ultimo componente è il nome del lotto e la chiave è univoca; per un lotto che tiene i file in una sottocartella è il nome della sottocartella, e `esemplari` è anche la sottocartella di `lotto-parco-lotta`. La stessa ricetta era ripetuta in tre altri punti, `tools/checklist-pokedex.py`, `tools/pkhex-scrivi-salvataggio` e `tools/stampa-collezione.py`, in due linguaggi e senza una dichiarazione comune: cambiarla in un punto solo avrebbe fatto risultare 179 voci della checklist da rigiudicare, senza alcun errore.

Il salto senior e perché è meglio. La chiave diventa il percorso relativo alla cartella `lotti`, con barre in avanti, calcolato da una funzione con lo stesso nome nei due strumenti C# e da `os.path.relpath` nella checklist; ogni punto che ripete la regola elenca gli altri nel proprio commento. Per i lotti di primo livello la chiave non cambia, quindi solo le 376 voci annidate vanno rinominate, e lo si fa sul testo del registro per non riscriverne la serializzazione .NET. La prova che distingue è la versione vecchia della checklist letta sul registro rinominato, che perde le 179 voci: senza di essa l'uguaglianza byte per byte della checklist rigenerata non direbbe nulla. Il compromesso dichiarato è una compatibilità temporanea in `stampa-collezione.py` con la forma breve, scritta come debito con la condizione che la estingue, cioè le copie per HOME rifatte con ADR-099.

Dove leggere il dettaglio: `refactor-02-chiave-del-lotto.md`.

## 3. Un controllo che saltava ciò che non sapeva misurare

Contesto. Il 2026-10-07 il proprietario ha chiesto che tutto il lavoro arrivi alla tesi, con le fonti e con la documentazione tecnica e didattica (ADR-101). Misurare quanto la tesi fosse indietro ha mostrato che lo strumento che doveva dirlo non lo diceva.

Com'era e perché era fragile. `tools/check-thesis-coverage.py` misura il drift di un capitolo dal commit dichiarato nel suo timbro, e saltava i capitoli senza timbro; la loro dichiarazione di copertura però restava valida, quindi le sezioni reclamate contavano come coperte per sempre. I capitoli così erano 19 su 39, fra cui `24-strumenti.tex`, che reclama per intero `docs/22-strumenti.md` e non nomina nessuno degli strumenti su PKHeX.Core nati dal 2026-09-25. Nessuna riga era sbagliata in sé: saltare era corretto, tacere di aver saltato no.

Il salto senior e perché è meglio. Un capitolo che dichiara coperture senza timbro è ora un errore elencato, accanto ai capitoli in drift, e la corsa a HEAD `0f82fcb` passa da 1 a 2 problemi senza cambiare i 10 capitoli in drift di prima. La correzione non mette timbri: un timbro messo per far tacere il controllo trasforma un punto cieco in una dichiarazione falsa, e il timbro si mette solo dopo aver riletto il capitolo. Il principio generale è che un controllo conta fra i propri esiti ciò che non ha potuto controllare, invece di lasciarlo fuori dal totale.

Dove leggere il dettaglio: `refactor-03-capitoli-senza-timbro.md`.
