---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
  - pokemon-gen12-gen3-bridge-original-hardware/
  - gba-switch-pokemon-trading/
  - poke-automation-study/
last-verified-commit: 7696c46
---

# Direzione

I cinque sottoprogetti sono task paralleli e non fasi di una sequenza, quindi questa scheda non è un ordine di esecuzione ma una mappa di cosa sblocca cosa. Il progetto è pensato per accoglierne altri: aggiungerne uno significa creare la cartella, istanziare una scheda da `templates/context/sub-subproject.md`, aggiungere una riga in tre posti, cioè la tabella di verifica e il punto di ripresa in `memory/index.md` e la tabella dei track in `current-work.md`, e come quarto passo estendere il `covers-paths` delle schede trasversali che parlano di quel track. Quest'ultimo passo è quello che si dimentica, e dimenticarlo non produce un errore visibile: produce un punto cieco, perché `sync-context` non segnalerà mai un drift su un'area che nessuna scheda dichiara di coprire.

## Cosa sblocca cosa

Il sottoprogetto 3DS è l'unico che può procedere senza dipendere da nulla: le cinque cartucce DS rimanenti si dumpano quando c'è tempo. È anche l'unico che tocca una scadenza esterna reale, perché Pokemon Bank chiude il 25 o 26 febbraio 2027, ma quella strada è già dichiarata chiusa per questo progetto, quindi la scadenza non impone urgenza.

Il sottoprogetto Smeraldo è bloccato su due fatti fisici, l'arrivo del lettore ordinato il 18 agosto e la conferma dei driver, e non su lavoro da fare. Quando si sblocca, procede in sette step già scritti fino alla verifica in gioco.

Il ponte fra generazioni non è bloccato come lo era alla stesura di questa scheda, e la differenza conta. La decisione di ADR-008 resta aperta e resta a valle di un inventario hardware, ma gli strati di formato e di conversione sono identici in tutte e quattro le opzioni, quindi si costruiscono prima della decisione, ed è ciò che sta avvenendo: il lato Game Boy è scritto e collaudato. È il track a più alto valore e a più alto costo, e la scelta fra le quattro opzioni cambia radicalmente soltanto l'ultimo tratto, cioè come i byte arrivano da una console all'altra.

Lo scambio fra PC e Switch ha ora un obiettivo scritto, ed è un track autonomo: non è la via verso Pokemon Home che si era ipotizzata quando la cartella era vuota, ma un lavoro di rete e reverse engineering sul protocollo LDN. Il fatto materiale su cui era bloccato ha ora una risposta e non è quella che si aspettava: questa macchina non ha alcuna interfaccia Wi-Fi, quindi l'adattatore non va accertato ma procurato, e la scelta è registrata fra le pendenze. Resta una tensione di piattaforma, perché richiede Linux mentre lo Smeraldo richiede Windows.

Lo studio dell'automazione su Switch è il quinto track e non è bloccato da nulla di materiale, perché oggi è lettura: è bloccato da una decisione di scopo, cioè se resti studio, se diventi il riuso della parte su microcontrollore in comune con l'opzione D del ponte, o se sia automazione vera come obiettivo indipendente. Non sblocca nessuno degli altri quattro e nessuno lo blocca, ma tocca due volte il resto del progetto: condivide il microcontrollore con l'opzione D del ponte e condivide un titolo con il track LDN, perché fra i giochi automatizzati compaiono Rosso Fuoco e Verde Foglia nella versione Switch. La visione artificiale che quel progetto usa è invece una capacità che nessun altro track ha.

## Conseguenze sull'infrastruttura

Sul ponte fra generazioni esiste ora un ordine di lavoro che non dipende dall'hardware, dettagliato in `docs/30-opzioni-implementative.md`: conformità con `PKHeX` su salvataggi sintetici, tabella degli indici di specie generata dal disassemblato, strutture di generazione 3, tabelle di dati per la conversione, strato di conversione con il risolutore di vincoli, e vettori di prova esternalizzati. Il lettore di cartucce blocca la prova da un capo all'altro su dati reali, e blocca anche il collaudo del protocollo del cavo su emulatore, perché quello richiede una ROM e la ROM richiede di dumpare una cartuccia propria.

Due decisioni erano rimandate a quando il ponte avesse prodotto codice, e quella condizione si è verificata il 2026-08-25, quindi vanno riaperte invece di restare al futuro. Il server MCP code-context andava riproposto al primo modulo scaffoldato: i moduli sono cinque più sei file di prove, quindi ora c'è del codice da cui estrarre e la proposta va rifatta, ferma restando la facoltà di rimandarla ancora. Un `CLAUDE.md` annidato nella cartella del ponte andava scritto quando ci fossero stati comandi di build, lint e test da dichiarare: il comando di test esiste, cioè `python tests/run_tests.py`, e conterrà solo quel genere di cosa, mai stato, che resta nella scheda. Entrambe le condizioni sono ora registrate in `pending.md`, perché una condizione verificata scritta solo qui è una condizione che nessuno ricorda.

L'architettura a schede verticali regge comodamente fino a una dozzina di sottoprogetti. Oltre, la tabella di `memory/index.md` smette di leggersi a occhio e diventa sensata una skill di roll-up dello stato, che oggi sarebbe prematura.
