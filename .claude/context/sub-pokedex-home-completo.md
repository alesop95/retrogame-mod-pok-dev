---
generated-from-commit: e692a02b8a46ab119e0389449d61327384841236
generated-from-branch: main
generated-date: 2026-09-02
covers-paths:
  - pokedex-home-completo/
last-verified-commit: 80fac1f
stato: attivo ed è il fuoco corrente; dal 2026-09-16 il trasferimento verso la quarta generazione si può sintetizzare in software (203 esemplari già prodotti in `_notes/lotto-parco-amici-gen4/`), la checklist copre 685 specie su 1025, e restano aperte solo le decisioni di profilo già registrate
---

# Sottoprogetto: Pokedex completo in Pokemon Home

Lo stato canonico di questo track è questo file insieme alla riga che lo riguarda in `memory/index.md`, che porta il racconto per aggiunte datate. Questa scheda è stata potata il 2026-09-09: il racconto che occupava ventimila byte viveva qui e nei documenti del track insieme, e la duplicazione è precisamente ciò che una scheda di stato non deve essere. Ciò che è stato tolto non è andato perduto, perché sta nei documenti elencati sotto e nel work log.

Obiettivo: la collezione completa nel deposito, cioè una voce per ogni specie, per ogni forma che il deposito conti a parte e per ogni esemplare la cui provenienza sia essa stessa un collezionabile. È l'obiettivo dichiarato del progetto, e gli altri track vi concorrono restando autonomi. La scadenza è il 26 febbraio 2027 alle 12:00 del fuso giapponese.

## Dove siamo, in cinque righe

Il risultato che governa la pianificazione regge ed è misurato e non assunto: nessuna specie e nessuna voce di forma dipendono dalla via indiretta, quindi la chiusura non vincola il completamento del catalogo. Ciò che scade sono gli esemplari la cui identità richiede una provenienza anteriore all'ottava generazione.

Gli assi sono sei più tre. Specie, forme, esemplari da distribuzione, mosse che nessun titolo moderno insegna più, fiocchi conferiti da vie chiuse, sfide interne al deposito; dal 2026-09-09 gli scambi in gioco e gli incontri che una condizione sblocca, enumerati sulla fonte di primo livello; e dal 2026-09-12 i marchi, che sono cinquantatré in sei famiglie ed è ADR-058. I marchi non sono una sottofamiglia dei fiocchi benché il formato li tenga negli stessi byte, perché un fiocco si conferisce per un merito e un marchio per una circostanza dell'incontro, e nessuno di essi è sotto la scadenza.

Il collo di bottiglia sul trasferimento si è spezzato in due il 2026-09-16: per la terza generazione verso la quarta non serve più hardware né emulazione DS, perché `pokebridge/parco_amici.py` sintetizza in software la trasformazione del Parco Amici, verificata contro l'osservazione umana in `PKHeX` e applicata a tutte le 209 voci Gen3 già prodotte (203 riuscite, sei escluse per macchina nascosta e da decidere). Il resto della catena, dalla quarta generazione in su, resta hardware o emulazione DS come descritto in `CATENA-DI-TRASFERIMENTO.md`. Sei lotti Gen3 sono prodotti: il sesto, chiuso il 2026-09-14, sono i diciannove scambi in gioco conformi su diciannove al quarto giudizio esterno, il primo lotto composto senza alcuna ricerca di semi perché la fonte ne scrive ogni campo. Il 2026-09-16 il generatore di terza generazione è salito da 172 a 176 su 177 voci (mancava il metodo `BACD_U`, corretto), e la sua stabilità di riproduzione è ora garantita per identità di voce e non per posizione nell'elenco, dopo che l'aggiunta delle quattro voci nuove aveva rotto la corrispondenza byte per byte di diciotto esemplari già su una cartuccia vera (corretto, verificato zero divergenze). Sono stati inoltre prodotti, e attendono giudizio, i primi scambi in gioco di quarta (16) e quinta (7) generazione.

## Prossimo passo

Due linee in parallelo, per direttiva dell'utente del 2026-09-10, restano il criterio. La lettura del corpus è CHIUSA il 2026-09-16: i diciassette cluster che restavano sono stati letti nelle trentaquattro voci scaricate e dichiarati nelle ventiquattro catalogate, quasi tutte video, e tutti e quarantadue i cluster del censimento portano ora uno stato. Ne sono venuti la terza prova indipendente che la prima e la seconda generazione non salgono alla terza, il vincolo del Trasferitore sulla mossa Pugnorapido per gli esemplari dell'uovo misterioso, i due vincoli di ottenibilità dei cromatici in seconda generazione che toccano insieme l'asse delle forme e quello del sesso, e due porte del deposito non contate, cioè Keldeo e Meloetta cromatici come premio per il completamento di Pokedex regionali. La produzione ha due fronti aperti: far giudicare dall'esterno gli scambi di quarta e quinta generazione già composti e il lotto Parco Amici, e le sei voci escluse per macchina nascosta, che attendono una decisione dell'utente su se perdere la mossa-firma o lasciarle come file. Il terzo fronte che questa scheda elencava, cioè estendere `parco_amici.py` all'uscita di `_notes/lotto-gb/`, è CADUTO il 2026-09-16: quella conversione non esiste e la fonte la rifiuta esplicitamente, come registrato nell'ultima sezione di `pokedex-home-completo/CATENA-DI-TRASFERIMENTO.md`; al suo posto resta proposta la sintesi del Trasferitore verso il formato di settima generazione, che però dipende dalla decisione aperta sul perimetro di Bank. La checklist rigenerata il 2026-09-15 copre 685 specie su 1025 con la nuova fonte degli scambi in gioco Gen3; restano fuori Alcremie a 63 forme e l'asse del sesso (102 specie), che aspettano una decisione su quale fonte prevalga su PKHeX, e gli incontri condizionati, per cui non esiste ancora un generatore.

Sulla produzione pesa ancora la domanda aperta dal 2026-09-10: il servizio ricostruito distribuisce ancora i doni di quarta e quinta generazione alle cartucce vere, e un esemplare ricevuto è preferibile a uno composto su ogni dimensione. La voce sta in `pending.md`. Una seconda domanda, chiusa il 2026-09-16 in negativo, non pesa più: la scappatoia del tracciatore su Pokemon Spada/Scudo, che avrebbe permesso di saltare la catena DS del tutto, non regge al confronto col costo di una console modificata.

## Decisioni aperte

Restano dell'utente l'ambito delle sfide del deposito, per cui servono le schermate delle due schede non fotografate, e la scelta del profilo di collezione fra i quindici che lo strumento della comunità distingue. Le altre sono state prese e stanno in `decisions.md` da ADR-049 a ADR-054.

## Dove sta la conoscenza di questo track

```
README.md                     l'instradamento, con l'elenco di ogni file della cartella
ROADMAP.md                    la sequenza, con dipendenze e chi esegue ciascun passo
CATENA-DI-TRASFERIMENTO.md    i vincoli di ogni anello, la via in emulazione, la regola del deposito
LETTURA-DEL-CORPUS.md         il registro della lettura integrale, cluster per cluster
CONFRONTO-LIVINGDEX-POKEPC.md la terza enumerazione indipendente, e il confronto con la nostra
MARCHI.md                     l'asse dei marchi, 53 voci in sei famiglie, nessuna sotto scadenza
STUDIO-01 .. STUDIO-09        le nove note di studio, dalla scadenza alla regola del tracciatore
CHECKLIST-COMPLETA.md         la lista di spunta generata, con il codice interno PKD-####-##
```

I censimenti generati e i loro strumenti sono elencati in `MAPPA-DOCUMENTI.md` alla radice, che dice per ciascuno chi lo genera; la tesi li rende nei capitoli da 28 a 31.

## Evidenze e materiale locale

La consegna che ha aperto il track e la ricerca dell'utente stanno in `_notes/fonti/`, e quella conservata verbatim con la sua provenienza è tracciata come `RICERCA-UTENTE-2026-09-01.md`. La raccolta di trenta salvataggi esterni vive in `_notes/salvataggi/` con la lista delle provenienze scritta dall'utente, e non entra in git per due vincoli indipendenti: ne entra soltanto il censimento generato. Le fotografie delle sfide e le cartelle di calcolo della comunità stanno in `_notes/spreadsheets e passaggi home/`.
