---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
  - pokemon-gen12-gen3-bridge-original-hardware/
  - gba-switch-pokemon-trading/
last-verified-commit: d08a011
---

# Direzione

I quattro sottoprogetti sono task paralleli e non fasi di una sequenza, quindi questa scheda non e' un ordine di esecuzione ma una mappa di cosa sblocca cosa. Il progetto e' pensato per accoglierne altri: aggiungerne uno significa creare la cartella, istanziare una scheda da `templates/context/sub-subproject.md` e aggiungere una riga in tre posti, cioe' la tabella di verifica e il punto di ripresa in `memory/index.md` e la tabella dei track in `current-work.md`.

## Cosa sblocca cosa

Il sottoprogetto 3DS e' l'unico che puo' procedere senza dipendere da nulla: le cinque cartucce DS rimanenti si dumpano quando c'e' tempo. E' anche l'unico che tocca una scadenza esterna reale, perche' Pokemon Bank chiude il 25 o 26 febbraio 2027, ma quella strada e' gia' dichiarata chiusa per questo progetto, quindi la scadenza non impone urgenza.

Il sottoprogetto Smeraldo e' bloccato su due fatti fisici, l'arrivo del lettore ordinato il 18 agosto e la conferma dei driver, e non su lavoro da fare. Quando si sblocca, procede in sette step gia' scritti fino alla verifica in gioco.

Il ponte fra generazioni e' bloccato su una decisione che a sua volta e' bloccata su un inventario hardware. E' il track a piu' alto valore e a piu' alto costo, perche' e' l'unico che produrra' software, e la scelta fra le quattro opzioni cambia radicalmente tutto il resto.

Lo scambio fra PC e Switch ha ora un obiettivo scritto, ed e' un track autonomo: non e' la via verso Pokemon Home che si era ipotizzata quando la cartella era vuota, ma un lavoro di rete e reverse engineering sul protocollo LDN. E' bloccato su un fatto materiale, cioe' se la scheda Wi-Fi di questa macchina supporti la modalita' monitor, e su una tensione di piattaforma: richiede Linux mentre lo Smeraldo richiede Windows.

## Conseguenze sull'infrastruttura

Due decisioni sono deliberatamente rimandate a quando il ponte produrra' codice. Il server MCP code-context oggi non ha nulla da estrarre da un corpus di documenti, e va riproposto al primo modulo scaffoldato. Un `CLAUDE.md` annidato nella cartella di quel sottoprogetto avra' senso quando ci saranno comandi di build, lint e test da dichiarare, e conterra' solo quelli: mai stato, che resta nella scheda.

L'architettura a schede verticali regge comodamente fino a una dozzina di sottoprogetti. Oltre, la tabella di `memory/index.md` smette di leggersi a occhio e diventa sensata una skill di roll-up dello stato, che oggi sarebbe prematura.
