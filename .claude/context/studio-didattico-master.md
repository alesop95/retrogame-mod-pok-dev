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
| 4 | Lo stesso identificativo, corretto in due modi | 2026-10-07 | `refactor-04-identificativo-segreto.md` |
| 5 | Rifare una copia senza rifarla, e una prova a vuoto che guardava solo i box | 2026-10-07 | `refactor-05-copie-sostituite.md` |
| 6 | Una scrittura verificata da chi non l'ha fatta, e un nome di file conteso | 2026-10-07 | `refactor-06-verifica-indipendente.md` |

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

## 4. Lo stesso identificativo, corretto in due modi

Contesto. ADR-099 del 2026-10-06 dà all'allenatore del progetto un solo identificativo segreto, 58164, quello di `recreate-pokemon-distributions-events/allenatore.json`. Due strumenti scrivevano a mano 5147, in 201 esemplari, e il manifesto del complemento del Rubino scriveva 0, in 101 esemplari già sulla cartuccia.

Com'era e perché era fragile. Il file dell'allenatore esisteva proprio per non ripetere il dato, ma tre programmi lo ripetevano a mano, con due valori diversi e senza una fonte per nessuno dei due. Nessun valore produceva un errore, perché un SID qualunque genera esemplari legali; il difetto stava nella collezione, con tre identità per lo stesso allenatore, ed era invisibile anche nel registro dei giudizi, che descrive l'identificativo nel formato del gioco e non mostra il SID.

Il salto senior e perché è meglio. I programmi leggono il file, che cercano risalendo dalla cartella corrente così che i comandi documentati non cambino, e uno strumento nuovo, `pkhex-identificativi`, rende ripetibile la misura del campo. La correzione non è una sola. Dove il PID deriva dal SID, cioè nel Pokéwalker (`PokewalkerRNG.cs` riga 280) e nella quinta generazione, dove il bit alto del PID segue la parità di TID xor SID (`MonochromeRNG.cs` righe 14-25) e 5147 e 58164 hanno parità opposta, si rigenera, e 223 file nascono di nuovo conformi. Dove il SID non entra in nessun calcolo, cioè negli incontri di terza generazione, dove sta nell'intestazione fuori dalla somma di controllo (`PK3.cs` righe 56 e 204), si cambiano due byte con `pkhex-correggi-sid`, che conserva gli individui già scritti sulla cartuccia come vuole ADR-082. La scelta si fa leggendo il codice che deriva gli altri campi, perché nulla nell'esemplare la rivela; la prova decisiva è un confronto byte per byte scritto senza la libreria, che trova cambiati solo gli offset 6 e 7.

Dove leggere il dettaglio: `refactor-04-identificativo-segreto.md`.

## 5. Rifare una copia senza rifarla, e una prova a vuoto che guardava solo i box

Contesto. Per ADR-099 quattro copie per HOME andavano rifatte, perché contenevano gli esemplari con l'identificativo segreto sbagliato. Le copie erano nate a catena, da passate che partivano ciascuna dalla precedente, e il rapporto ne registra la partenza solo come `main`.

Com'era e perché era fragile. Lo strumento di scrittura sapeva solo aggiungere esemplari nei posti liberi; rifare una copia voleva dire ricostruire una catena che nessun file descrive. La preparazione di un esemplare stava dentro il ciclo di scrittura, quindi una seconda modalità avrebbe richiesto una seconda copia della regola. Si credeva inoltre che lo strumento fosse deterministico: non lo era, perché la conversione dalla quinta alla sesta generazione sceglie a caso il sentimento del ricordo del detentore (`PK5.cs` riga 479), e quella dalla terza alla quarta pone la data d'incontro al giorno corrente (`PK3.cs` riga 255).

Il salto senior e perché è meglio. La preparazione è una funzione sola, usata dalla scrittura ordinaria e dall'opzione nuova `--sostituisci`, che rimette ogni esemplare dei lotti cambiati nel suo posto solo se è davvero diverso. La regressione non è l'uguaglianza dei file, impossibile, ma un confronto posto per posto che ignora per nome i due campi assegnati dalla conversione, con lo strumento nuovo `pkhex-confronta-copie`. La prova a vuoto, cioè una sostituzione con un lotto non cambiato, ha trovato prima la data d'incontro e poi un difetto più sottile: i box tornavano identici, ma il file no, perché la scrittura di prova aveva aggiornato il Pokédex. La prova ora si scrive in un clone, e la sostituzione a vuoto dà un file identico byte per byte. La lezione è che una prova a vuoto si confronta sul prodotto intero, non sulla parte che si voleva cambiare.

Dove leggere il dettaglio: `refactor-05-copie-sostituite.md`.

## 6. Una scrittura verificata da chi non l'ha fatta, e un nome di file conteso

Contesto. La cartuccia del Rubino riceve in una sola scrittura due correzioni, l'identificativo segreto di 101 esemplari (ADR-099) e il Pokédex delle specie presenti (ADR-089). Lo strumento nuovo `pkhex-allinea-gen3` le compone, e il runbook `RUNBOOK-RUBINO-SID-POKEDEX.md` descrive i passi con la cartuccia in mano.

Com'era e perché era fragile. La misura del 2026-09-28 leggeva i contrassegni del Pokédex in una sola copia, quella di SaveBlock2; il sorgente di Rubino (`src/pokedex.c` riga 3986) mostra che un «visto» vale solo se è acceso in tre copie, e che se non concordano il gioco le spegne tutte. E la verifica che uno strumento fa del proprio file usa la stessa libreria che ha scritto, quindi ne condivide gli eventuali errori di indirizzo.

Il salto senior e perché è meglio. Lo strumento accende le tre copie, come la libreria e come il gioco, e accanto alla sua verifica ce n'è una seconda scritta con `pokebridge`, che non usa la libreria e dice soltanto quali byte sono cambiati, con le zone ammesse prese dal sorgente di pokeruby: tutti i byte cambiati stanno nel Pokédex e nei due byte del SID dei 101 esemplari. Un nome di file usato da due strumenti per due formati, `.rapporto.json`, ha fermato `pkhex-elenco-copie`, e il rapporto nuovo si chiama `.allineamento.json`. La lezione è che una verifica vale per quanto non condivide con ciò che verifica.

Dove leggere il dettaglio: `refactor-06-verifica-indipendente.md`.
