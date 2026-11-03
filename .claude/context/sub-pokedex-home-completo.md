---
generated-from-commit: 7ab335d9b2ae3dc8eefd9c9bd8a64a7ed0a911ef
generated-from-branch: main
generated-date: 2026-09-02
covers-paths:
  - pokedex-home-completo/
last-verified-commit: ef2ff17
stato: attivo ed è il fuoco corrente; produzione sotto scadenza chiusa, 3272 esemplari per HOME in cinque copie scritte e rilette (ADR-099, ADR-103), 121 per la decisione finale, 14 giapponesi da provare a parte; trasferimento verso banca e deposito non cominciato, confermato dal proprietario il 2026-11-03, che ha il 3DS con sé; si comincia a fonti tutte lette (ADR-105)
---

# Sottoprogetto: Pokedex completo in Pokemon Home

Lo stato canonico di questo track è questo file insieme alla riga che lo riguarda in `memory/index.md`, che porta il racconto per aggiunte datate. Questa scheda è stata potata il 2026-09-09: il racconto che occupava ventimila byte viveva qui e nei documenti del track insieme, e la duplicazione è precisamente ciò che una scheda di stato non deve essere. Ciò che è stato tolto non è andato perduto, perché sta nei documenti elencati sotto e nel work log.

Obiettivo: la collezione completa nel deposito, cioè una voce per ogni specie, per ogni forma che il deposito conti a parte e per ogni esemplare la cui provenienza sia essa stessa un collezionabile. È l'obiettivo dichiarato del progetto, e gli altri track vi concorrono restando autonomi. La scadenza è il 26 febbraio 2027 alle 12:00 del fuso giapponese.

## Dove siamo, in cinque righe

Aggiornamento del 2026-11-03, riconciliato con `sync-context` su 29 file cambiati in `pokedex-home-completo/` da `6ee3543`, che prevale su tutto ciò che segue. La sequenza vigente è la sezione «La roadmap al 2026-10-05» di `ROADMAP.md`, e le copie da portare sulla console sono quelle della prima tabella di `COPIE-PER-HOME.md`. Per HOME sono 3272 esemplari: `oras-giro-1-fin2` 930, `oras-giro-2-mn-fin2` 721 con i 36 a macchina nascosta, `oras-giro-3-fin3` 915 con il Manaphy di Ranger, `luna-giro-1-fin` 93 e `ultraluna-giro-1-scambi-fin2` 613 con i 26 scambi in gioco di sesta e settima generazione e i 12 statici di Ohana. Tutti hanno l'identificativo segreto unico 58164 di ADR-099. A parte restano i 121 eventi da cartuccia per la decisione finale e i 14 esemplari giapponesi di Game Boy in `luna-giappone-14`. Le 40 voci da periferiche sono prodotte dal 2026-09-30, quindi la coda del primo tempo è chiusa. Il Pokédex nazionale del Rubino non è sbloccato (ADR-103) e non tocca il deposito. Mancano 115 giorni alla chiusura della banca, contati dal 2026-11-03 al 26 febbraio 2027.

Il risultato che governa la pianificazione regge ed è misurato e non assunto: nessuna specie e nessuna voce di forma dipendono dalla via indiretta, quindi la chiusura non vincola il completamento del catalogo. Ciò che scade sono gli esemplari la cui identità richiede una provenienza anteriore all'ottava generazione.

Gli assi sono sei più tre. Specie, forme, esemplari da distribuzione, mosse che nessun titolo moderno insegna più, fiocchi conferiti da vie chiuse, sfide interne al deposito; dal 2026-09-09 gli scambi in gioco e gli incontri che una condizione sblocca, enumerati sulla fonte di primo livello; e dal 2026-09-12 i marchi, che sono cinquantatré in sei famiglie ed è ADR-058. I marchi non sono una sottofamiglia dei fiocchi benché il formato li tenga negli stessi byte, perché un fiocco si conferisce per un merito e un marchio per una circostanza dell'incontro, e nessuno di essi è sotto la scadenza.

Il collo di bottiglia sul trasferimento si è spezzato in due il 2026-09-16: per la terza generazione verso la quarta non serve più hardware né emulazione DS, perché `pokebridge/parco_amici.py` sintetizza in software la trasformazione del Parco Amici, verificata contro l'osservazione umana in `PKHeX` e applicata a tutte le 209 voci Gen3 già prodotte (203 riuscite, sei escluse per macchina nascosta e da decidere). Il resto della catena, dalla quarta generazione in su, resta hardware o emulazione DS come descritto in `CATENA-DI-TRASFERIMENTO.md`. Sei lotti Gen3 sono prodotti: il sesto, chiuso il 2026-09-14, sono i diciannove scambi in gioco conformi su diciannove al quarto giudizio esterno, il primo lotto composto senza alcuna ricerca di semi perché la fonte ne scrive ogni campo. Il 2026-09-16 il generatore di terza generazione è salito da 172 a 176 su 177 voci (mancava il metodo `BACD_U`, corretto), e la sua stabilità di riproduzione è ora garantita per identità di voce e non per posizione nell'elenco, dopo che l'aggiunta delle quattro voci nuove aveva rotto la corrispondenza byte per byte di diciotto esemplari già su una cartuccia vera (corretto, verificato zero divergenze). Sono stati inoltre prodotti, e attendono giudizio, i primi scambi in gioco di quarta (16) e quinta (7) generazione.

Aggiornamento del 2026-09-29, che supera due affermazioni del paragrafo precedente senza cancellarle. Dal 2026-09-24 il Parco Amici verso la quarta generazione non si fa più con la sintesi di `parco_amici.py` ma con la libreria del verificatore, `tools/pkhex-parco-amici`, perché il giudizio della libreria contestava 148 esemplari su 203 del lotto della sintesi: il lotto rigenerato è 203 conforme su 203, con le stesse sei esclusioni per macchina nascosta (ADR-081, ADR-082). I 23 scambi di quarta e quinta generazione sono stati ricostruiti con `tools/pkhex-rigenera` e sono 23 conformi su 23. Il giudizio di tutti i lotti, in `recreate-pokemon-distributions-events/giudizi-pkhex-core.json`, è 2010 conformi su 2010. La collezione di terza generazione è chiusa e non si riapre per ragioni di metodo (ADR-082): Smeraldo è scritto e riletto dal 2026-09-23, il complemento del Rubino, 376 esemplari, dal 2026-09-28 (ADR-088). La coda del primo tempo, `CODA-PRIMO-TEMPO.md` rigenerata il 2026-09-25, conta 433 voci: 333 prodotte e conformi, 60 producibili e verificate, 40 censite e non ancora producibili, che sono le voci da periferiche.

## Prossimo passo

Aggiornato il 2026-11-03, prevale sui paragrafi sotto. Il prossimo passo sotto scadenza è il passo 1 della roadmap del 2026-10-05, cioè la prova pilota con `oras-giro-1-fin2`, 930 esemplari: ripristino della copia con Checkpoint dopo la copia di riserva della partita vera, controllo dei box, banca, deposito. Lo esegue il proprietario, e il tratto dalla banca in poi resta fuori dall'assistenza (`rules/hardware-and-perimeter.md`). Seguono i giri 2 e 3 di Rubino Omega, poi Luna e Ultraluna con i codici QR, poi la prova dei 14 giapponesi, i 121 della decisione finale e il ripristino delle partite vere. Da sviluppo resta il punto 4 di ADR-100, la lettura del codice delle fonti, che non blocca nessun passaggio.

Aggiornato il 2026-09-29. Il prossimo passo di produzione sono le 40 voci da periferiche della coda, cioè 29 dal Pokewalker, 8 da My Pokemon Ranch e 3 dal Dream Radar, con la libreria se i loro incontri sanno costruire un esemplare, poi il giudizio, i lotti in `LOTTI_PER_CODICE` di `tools/checklist-pokedex.py` e la rigenerazione di censimento, checklist, coda e schede: è la voce SECONDO di `pending.md`, preceduta dal debito tipografico della voce PRIMO. La lettura per via d'archivio delle pagine del Ranch e del Dream Radar è la voce TERZO. Dal fronte della produzione descritto nel paragrafo seguente, il giudizio degli scambi di quarta e quinta generazione e del Parco Amici è chiuso; le sei voci escluse per macchina nascosta restano una decisione del proprietario. Resta da fare anche l'allineamento del Pokédex del Rubino alle specie che contiene (ADR-089), che non tocca HOME ma la cartuccia.

Due linee in parallelo, per direttiva dell'utente del 2026-09-10, restano il criterio. La lettura del corpus è CHIUSA il 2026-09-16: i diciassette cluster che restavano sono stati letti nelle trentaquattro voci scaricate e dichiarati nelle ventiquattro catalogate, quasi tutte video, e tutti e quarantadue i cluster del censimento portano ora uno stato. Ne sono venuti la terza prova indipendente che la prima e la seconda generazione non salgono alla terza, il vincolo del Trasferitore sulla mossa Pugnorapido per gli esemplari dell'uovo misterioso, i due vincoli di ottenibilità dei cromatici in seconda generazione che toccano insieme l'asse delle forme e quello del sesso, e due porte del deposito non contate, cioè Keldeo e Meloetta cromatici come premio per il completamento di Pokedex regionali. La produzione ha due fronti aperti: far giudicare dall'esterno gli scambi di quarta e quinta generazione già composti e il lotto Parco Amici, e le sei voci escluse per macchina nascosta, che attendono una decisione dell'utente su se perdere la mossa-firma o lasciarle come file. Il terzo fronte che questa scheda elencava, cioè estendere `parco_amici.py` all'uscita di `_notes/lotti/lotto-gb/`, è CADUTO il 2026-09-16: quella conversione non esiste e la fonte la rifiuta esplicitamente, come registrato nell'ultima sezione di `pokedex-home-completo/CATENA-DI-TRASFERIMENTO.md`; al suo posto resta proposta la sintesi del Trasferitore verso il formato di settima generazione, che però dipende dalla decisione aperta sul perimetro di Bank. La checklist rigenerata il 2026-09-15 copre 685 specie su 1025 con la nuova fonte degli scambi in gioco Gen3; restano fuori Alcremie a 63 forme e l'asse del sesso (102 specie), che aspettano una decisione su quale fonte prevalga su PKHeX, e gli incontri condizionati, per cui non esiste ancora un generatore.

Sulla produzione pesa ancora la domanda aperta dal 2026-09-10: il servizio ricostruito distribuisce ancora i doni di quarta e quinta generazione alle cartucce vere, e un esemplare ricevuto è preferibile a uno composto su ogni dimensione. La voce sta in `pending.md`. Una seconda domanda, chiusa il 2026-09-16 in negativo, non pesa più: la scappatoia del tracciatore su Pokemon Spada/Scudo, che avrebbe permesso di saltare la catena DS del tutto, non regge al confronto col costo di una console modificata.

Una porta nuova si è aperta il 2026-09-18 dal track `smeraldo-save-fix`, ed è la sola fra quelle registrate che non passa da un lotto composto: con ADR-066 la cartuccia vera di Smeraldo riapre gli incontri delle quattro isole, quindi Deoxys, Mew, Lugia e Ho-Oh diventano catturabili giocando, con il contrassegno di incontro fatidico che il gioco appone da sé. Deoxys e Mew sono le due che contano davvero, perché non stanno nel deposito di quella cartuccia e perché Deoxys è una delle quattro specie prive di qualsiasi incontro nei titoli a via diretta (ADR-032). Lugia e Ho-Oh ci sono già dalla distribuzione italiana "10ANNI" su Rubino, quindi per loro la porta è un di più e non una necessità. Il dettaglio sta in `gba-save-extraction-smeraldo/STUDIO-03-doni-segreti-e-flag-delle-isole.md` dalla sezione 14. Dal 2026-09-24 la porta resta aperta ma non si usa: per ADR-083 Mew e Deoxys su Smeraldo non si catturano e gli incontri restano giocabili, perché i due esemplari esistono già generati e conformi in `_notes/lotti/lotto-incontri-gen3/`, ed è quelli che si portano verso HOME.

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
STUDIO-01 .. STUDIO-10        le dieci note di studio, dalla scadenza alla libreria del verificatore come generatore
CHECKLIST-COMPLETA.md         la lista di spunta generata, con il codice interno PKD-####-##
CODA-PRIMO-TEMPO.md           le 433 voci del primo tempo nell'ordine di produzione, generata
SCHEDE-ESCLUSIVI.md           da dove viene e perché è esclusiva ogni voce speciale, generata
VERIFICA-TERZA-GENERAZIONE.md che cosa la chiusura vincola in terza generazione
COMPLEMENTO-RUBINO.md         i 376 esemplari del complemento, generato
CENSIMENTO-SALVATAGGI.md      i salvataggi esterni letti, generato
data/                         le dodici tabelle da cui gli strumenti leggono
```

I censimenti generati e i loro strumenti sono elencati in `MAPPA-DOCUMENTI.md` alla radice, che dice per ciascuno chi lo genera; la tesi li rende nei capitoli da 28 a 31.

## Evidenze e materiale locale

La consegna che ha aperto il track e la ricerca dell'utente stanno in `_notes/fonti/consegne/`, e quella conservata verbatim con la sua provenienza è tracciata come `RICERCA-UTENTE-2026-09-01.md`. La raccolta di trenta salvataggi esterni, diventati diciotto nel censimento del 2026-09-24 dopo la pulizia di ADR-084, che registra il motivo di ogni scarto, vive in `_notes/salvataggi/terzi/` con la lista delle provenienze scritta dall'utente, e non entra in git per due vincoli indipendenti: ne entra soltanto il censimento generato. Le fotografie delle sfide e le cartelle di calcolo della comunità stanno in `_notes/fonti/consegne/spreadsheets-home/`.
