---
generated-from-commit: e692a02b8a46ab119e0389449d61327384841236
generated-from-branch: main
generated-date: 2026-09-02
covers-paths:
  - pokedex-home-completo/
last-verified-commit: e692a02b8a46ab119e0389449d61327384841236
stato: attivo, ultimo anello della catena verificato rispondente, lista di spunta completa generata, seicentoquaranta voci di specie senza fonte
---

# Sottoprogetto: Pokedex completo in Pokemon Home

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`.

Obiettivo: la collezione completa in Pokemon Home, cioè una voce per ogni specie e per ogni forma che il deposito possa contenere. È l'obiettivo principale del progetto, e gli altri sottoprogetti possono concorrervi restando ciascuno autonomo con uno scopo proprio.

## Dove siamo

Aperto il 2026-09-02 con una consegna dell'utente e con una verifica indipendente che ha già prodotto il risultato che governa la pianificazione di tutto il progetto: la chiusura della banca non vincola il completamento del Pokedex, né a livello di specie né a livello di forma. Tutte e milleventicinque le specie sono raggiungibili per la via diretta, e le dodici voci-forma che soltanto la via indiretta dichiara sono escluse da un filtro letto dalla fonte, cioè dieci forme totemiche che al trasferimento tornano alla forma base o non si trasferiscono affatto, e due forme di sola battaglia che non possono stare in una scatola. Il conto lo esegue `tools/disponibilita-titoli.py` e si rifà a comando.

Ne segue che i giorni fino al 26 febbraio 2027 non si spendono qui ma sugli esemplari la cui identità richiede una provenienza anteriore all'ottava generazione, che sono materia del track delle distribuzioni e delle cartucce possedute.

## Aggiunta del 2026-09-02: la raccolta di salvataggi esterni

L'utente ha consegnato trenta file in `_notes/salvataggi/`, provenienti dalla categoria dei salvataggi contribuiti di Project Pokemon e da tre forum italiani, con una lista che per ciascuno dichiara provenienza e contenuto. Sono tutti e trenta verificati integri e identificati dal gioco che dichiarano, e il censimento generato è `CENSIMENTO-SALVATAGGI.md`; la nota che lo interpreta, con il metodo di identificazione e le tre domande che un salvataggio esterno pone, è `STUDIO-02-salvataggi-esterni-e-che-cosa-provano.md`.

Il numero che serve a questo track è la copertura: l'unione delle specie presenti come esemplare nella raccolta copre trecentottantacinque delle trecentottantasei voci nazionali di terza generazione, e manca soltanto Poochyena. Va letto con la precisione che merita, cioè che riguarda ciò che sta nei depositi e non le caselle del Pokedex, che sono un dato diverso e non ancora letto.

Le quattro fonti sono in `SOURCES.md` al livello cinque, come ADR-024 prescrive. Il perimetro dell'uso resta quello di ADR-024 per gli esemplari, mentre ADR-029 aggiunge la distinzione fra importare uno stato di avanzamento, che è ammesso per sbloccare il Parco Amici a tre condizioni, e importare un esemplare, che resta subordinato al giudizio del verificatore.

## Aggiunta del 2026-09-03: la catena risponde, e la lista di spunta esiste

L'ultimo anello della catena verso il deposito finale non è più un'ipotesi: la voce che sposta gli esemplari esiste, risponde, e su un deposito vuoto dichiara di non avere nulla da spostare. Lo stato è documentato in `STUDIO-03-la-catena-e-viva-e-la-lista-di-spunta.md`, che in apertura dichiara la distinzione richiesta da ADR-030, cioè che si registra lo stato della catena e non la procedura del deposito intermedio, sul quale il limite di perimetro resta intero.

Quattro vincoli numerici sono entrati nei conti e nessuno li avevamo. Il deposito intermedio tiene tremila posizioni, quindi è un condotto e non un magazzino. Rimuove gli oggetti tenuti al deposito, il che tocca il nostro lotto perché alcune voci del catalogo portano un oggetto che fa parte della loro identità storica. L'identificativo di rete si lega a una sola console, quindi parallelizzare i trasferimenti su una seconda console è escluso per costruzione. E un periodo di prova ha un conto alla rovescia già cominciato, il cui numero di giorni va riletto sulla console perché nelle fotografie la prima cifra non è leggibile.

La lista di spunta è `CHECKLIST-COMPLETA.md`, generata da `tools/checklist-pokedex.py`. Il codice interno è la coppia fra numero del Dex e indice di forma, scritta `PKD-####-##`, e serve perché il numero del Dex identifica una specie e non un esemplare da ottenere: non cambia per il sesso, per una variante regionale o per una forma. Al 2026-09-03 la lista dice milleventicinque voci di specie tutte per via diretta, trecentottantacinque con una fonte già nel progetto, e seicentoquaranta senza alcuna fonte: quest'ultimo è il numero che misura la campagna e il solo che scende quando si lavora.

## Prossimo passo concreto

Proiettare sulla lista di spunta le fonti che ancora non vi sono proiettate, in ordine di resa: le tremilasettantadue voci di dono delle generazioni moderne, i depositi dei salvataggi di quarta, quinta, sesta e settima generazione, e il deposito di Pokemon Box. Ciascuna è oggi un conto che vive da solo e diventerà una colonna, e le seicentoquaranta voci senza fonte scenderanno di conseguenza. Pokemon Box resta la più interessante per la domanda di completezza, perché il suo caricamento dichiara di contenere tutto ciò che in terza generazione si può ancora ottenere legittimamente; il formato del suo deposito differisce da quello delle cartucce e va letto su `PKHeX.Core/Saves/SAV3RSBox.cs` prima di essere scritto.

Il passo che segue, e che vale di più per la pianificazione, è contare e catalogare gli eventi di quarta, quinta, sesta e settima generazione con il metodo usato per la terza. La base dei doni segreti del verificatore contiene i file per tutte e quattro, cioè `wc4.pkl`, `pgf.pkl`, `wc6.pkl` con il suo complemento e `wc7.pkl` con il suo, quindi non c'è alcun algoritmo da ricostruire: il lavoro è di conteggio, di catalogazione e di misura della campagna.

## Decisioni aperte

Che cosa significhi completo, cioè se la collezione comprenda ogni forma e ogni variante cosmetica oppure una voce per specie. L'utente ha indicato la lettura estesa, e resta da stabilire quali forme il deposito conti come voci separate, che nessuna fonte di primo livello documenta.

Quali titoli recenti acquistare e quando. L'utente non ne possiede alcuno e li compra all'occorrenza; la verifica dice che non sono urgenti, quindi è una decisione di spesa e non di tempo.

Il piano a pagamento del deposito, che l'utente attiverà soltanto quando tutto il resto sarà pronto, e che oggi non è attivo.

## Evidenze e materiale locale

La consegna che ha aperto il sottoprogetto sta in `_notes/fonti/2026-09-01-consegna-pokedex-e-collezione-theslayer.txt`, locale e non versionata. La ricerca dell'utente è conservata verbatim in `pokedex-home-completo/RICERCA-UTENTE-2026-09-01.md`, che è tracciata perché è una fonte con provenienza e non materiale effimero.

La raccolta di salvataggi esterni vive in `_notes/salvataggi/`, con la lista delle provenienze scritta dall'utente in `lista.txt` accanto ai file. Non entra in git per due vincoli indipendenti, cioè l'esclusione di tutto `_notes/` e quella di ogni file con estensione di salvataggio, e ne entra soltanto il censimento generato. La cartella contiene sei salvataggi di terza generazione con il deposito popolato, quattro di prima generazione giapponesi, sei di quarta generazione fra Sinnoh, Platino e Johto, tre di quinta, cinque di Nintendo 3DS fra sesta e settima, un salvataggio di Pokemon Box su GameCube, un esemplare singolo e due archivi di esemplari.
