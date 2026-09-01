# Snapshot di sincronizzazione

Da leggere per primo a inizio sessione. Fotografa lo stato del progetto al commit di riferimento e mappa ogni scheda al suo stato di verifica. È la fonte di verità su cosa è fatto, non le spunte del diario.

Questo progetto ha più sottoprogetti paralleli, oggi otto, quindi il punto di ripresa è un blocco di righe invece che una sola. La riga "Fuoco corrente" è la fonte di verità unica su quale track è attivo adesso: task paralleli non significa nessun default, significa un default dichiarato più N tracce leggibili.

## Stato

```
Branch attivo:         main
Commit di riferimento: 3439cc8
Data snapshot:         2026-08-31
```

## Stato di verifica delle schede

| Scheda | Sottoprogetto | last-verified | Stato |
|---|---|---|---|
| STACK.md | trasversale | 7696c46 | covers-paths esteso agli otto track il 2026-08-31; il corpo non è stato riletto da quella data |
| design-and-security.md | trasversale | 7696c46 | covers-paths esteso agli otto track il 2026-08-31; la sezione sulle tensioni di perimetro va estesa ai due track nuovi |
| deployment.md | trasversale | d08a011 | non applicabile, covers-paths vuoto per scelta |
| dev-testing.md | trasversale | 7696c46 | copre il ponte e dichiara le prove automatiche; covers-paths esteso agli otto track il 2026-08-31 |
| current-work.md | trasversale | 7696c46 | tabella dei track e covers-paths portati a otto il 2026-08-31 |
| roadmap.md | trasversale | 7696c46 | riscritta il 2026-08-31 con l'obiettivo che sta sopra i track e la correzione alla scadenza |
| sub-3ds-modding.md | 3ds-related | 7696c46 | aggiornata |
| sub-smeraldo-save-fix.md | gba-save-extraction-smeraldo | 7696c46 | aggiornata |
| sub-gen12-gen3-bridge.md | pokemon-gen12-gen3-bridge | 7696c46 | aggiornata |
| sub-gba-switch-trading.md | gba-switch-pokemon-trading | 7696c46 | aggiornata |
| sub-poke-automation.md | poke-automation-study | 7696c46 | aggiornata |
| sub-distributions-events.md | recreate-pokemon-distributions-events | 319226b | aggiornata il 2026-08-29 con la ricerca sui metodi di generazione |
| sub-poke-ace.md | poke-ace | a427431 | nuova, scritta il 2026-08-31 e aggiornata lo stesso giorno con il secondo studio |
| sub-generation-from-switch.md | generation-from-switch | 809289a | nuova, scritta il 2026-08-31; il track meno sviluppato degli otto |

Le cose in sospeso non stanno qui ma in `pending.md`, che va letto subito dopo questo file: materiale atteso, credenziali, fonti in sospeso, strumenti da richiamare a una condizione, debito di lettura, punti aperti e blocchi materiali.

## Punto di ripresa

```
Fuoco corrente: poke-ace, e con esso la domanda che decide l'obiettivo di collezione
```

Il 2026-08-31 il fuoco si è mosso due volte nella stessa giornata, e vale registrare entrambi i movimenti perché il primo è concluso e il secondo è quello attivo.

Il primo è stato l'infrastruttura, cioè l'accesso automatico ai canali di community che il progetto aveva chiuso con un no il 2026-08-26. Il no ignorava una terza via, il bot account ufficiale, ed è ADR-018 con lo strumento `tools/fetch-discord.py`; quella via però richiede l'autorizzazione di chi amministra i server, che non sono dell'utente. Su decisione esplicita dell'utente si è quindi adottata la via che il progetto aveva scartato per prudenza, cioè l'esportazione con lo strumento della comunità e il proprio token, ed è ADR-019: lo strumento di orchestrazione è `tools/export-discord.py`, la tabella dei canali copre trenta canali su quattro livelli di priorità, la procedura completa sta in `docs/22-strumenti.md` e il pacchetto per il template è `community-sources`. Il primo livello di esportazione è in corso sulla macchina dell'utente.

Il secondo movimento è quello attivo e nasce da materiale nuovo consegnato dall'utente: due track nuovi, `poke-ace` e `generation-from-switch`, e con essi una domanda che non è di un track solo ma dell'obiettivo dichiarato del progetto, cioè se un esemplare la cui provenienza non è una partita giocata possa stare in una collezione che si vuole legittima. La risposta verificata è in `poke-ace/STUDIO-01-ace-e-legalita-in-home.md` e il prossimo passo non è tecnico: è una decisione dell'utente.

Adozione del sistema: conclusa. La storia git è stata collassata in un unico commit radice il 2026-08-25 per la bonifica di ADR-014, quindi `d08a011` è il commit radice e gli hash citati nelle voci di diario precedenti a quella data non risolvono più. Le schede sono state riconciliate a `7696c46` il 2026-08-26: il drift era quasi tutto contabile, perché erano state aggiornate a mano senza bumpare il checkpoint, e i tre difetti sostanziali trovati nascevano da un unico punto cieco, cioè `covers-paths` trasversali che non seguivano l'aggiunta di un sottoprogetto. Ora lo seguono, e la procedura di aggiunta in `CLAUDE.md` ha un quarto passo che lo impone. Convenzione Markdown conforme su tutto il repository, nulla da fare su questo fronte.

poke-ace: il track nasce il 2026-08-31 e porta con sé la domanda che decide se l'obiettivo di collezione sia raggiungibile per le vie non ufficiali, cioè se un esemplare prodotto scrivendone i byte sopravviva ai controlli di Pokemon Home. La risposta verificata è che i byte possono essere identici ma che Home conserva la via da cui un esemplare è entrato, e che la politica ufficiale elenca fra le sanzioni la sospensione dell'accesso a Home: la verifica pratica è impossibile prima di ottobre 2026. Lo studio è scritto, gli undici strumenti della comunità sono inventariati, e il prossimo passo non è tecnico ma una decisione dell'utente. Esiste un passo che non la richiede, cioè confrontare ciò che il costruttore di esemplari produce per una distribuzione con ciò che il track degli eventi ricostruisce dal metodo.

Nella stessa giornata il track ha prodotto un secondo studio, che chiude con dati il punto sulla forma dell'informazione di provenienza e apre una decisione nuova. La lista di controllo indicata dall'utente è stata letta sondando il suo fascio JavaScript compilato, poiché nessuna richiesta HTTP ne restituisce il contenuto, e ne vengono due esiti. Il primo è che la provenienza è un marchio categorico e visibile, scelto in un insieme di undici, e che la riedizione della terza generazione ne ha uno proprio trattato nel codice come non ancora ottenibile: un esemplare entrato dalla porta nuova sarà distinguibile a occhio da uno passato per la catena storica, che non porta marchio. Il secondo è che quella lista non è una lista ma un insieme parametrico con quindici profili, quindi l'obiettivo del progetto va precisato scegliendo un profilo, ed è una decisione dell'utente registrata in `pending.md`.

generation-from-switch: aperto il 2026-08-31 ed è il meno sviluppato degli otto, con due fonti registrate e non lette. Il prossimo passo è leggerle e riscrivere lo studio con ciò che dicono davvero.

Correzione alla scadenza, verificata su annuncio ufficiale del 13 agosto 2026 e valida per tutto il progetto: le versioni per console moderna di Rosso Fuoco e Verde Foglia si collegheranno a Pokemon Home a ottobre 2026, quindi per la terza generazione il 26 febbraio 2027 cessa di essere l'ultima porta. Resta l'ultima per prima, seconda, quarta e quinta generazione, la cui catena passa necessariamente da Bank. I due passaggi interni, dalla terza alla quarta e dalla quarta alla quinta, sono funzioni locali dei giochi e sopravvivono alla chiusura.

3ds-modding: dumpare le cinque cartucce DS rimanenti, Diamante, Perla, Platino, Nera 2 e SoulSilver, poi trasferire i file da `/gm9/out/` al PC. Nessun blocco.

smeraldo-save-fix: confermare che i driver CH340 siano installati e annotare la porta COM assegnata. Bloccato sul riscontro alla macchina e sull'arrivo del lettore ordinato il 18 agosto 2026. Quando il dump arriverà c'è già lo strumento che lo legge, `tools/emerald_bag_decode.py`, e c'è una scoperta che cambia l'ipotesi di partenza: le quantità dello zaino sono mascherate in XOR e vanno smascherate prima di chiamarle corrotte.

gen12-gen3-bridge: la struttura di generazione 3 è scritta e collaudata dal 2026-08-26, in `pokebridge/gen3.py`, con cifratura, permutazione e checksum verificati sul sorgente di pokeemerald; la suite passa 114 prove. Il prossimo passo è lo strato del salvataggio da 128 KiB, cioè la sezione 6 della referenza, oppure il generatore del salvataggio sintetico da confrontare con PKHeX, che chiude il limite noto della prova di simmetria e non richiede hardware. Il formato dati è documentato byte per byte e verificato sul disassemblato, con undici punti dubbi chiusi e due affermazioni dell'handoff corrette; l'handoff è stato ritirato per ADR-013. Non bloccato: il lavoro comune non dipende da ADR-008, e la discovery hardware serve solo all'ultimo tratto.

poke-automation: lo studio è cominciato il 2026-08-26 e la prima nota sta nella cartella del sottoprogetto, quindi il track non è più un semplice collegamento. Resta da decidere se si fermi allo studio, se diventi il riuso della parte su microcontrollore in comune con l'opzione D del ponte, oppure automazione vera su Switch come obiettivo indipendente. Sul perimetro c'è una notizia buona e verificata: il progetto di riferimento dichiara console non modificate e nessun accesso alla memoria, quindi il suo perimetro è compatibile con le regole di questo progetto, e ciò che resta da dichiarare è il nostro.

distributions-events: la ricerca è stata approfondita il 2026-08-29 e ha prodotto tre cose. Un catalogo generato dei 177 eventi con il metodo di generazione di ciascuno, in `EVENTI-GEN3.md`, prodotto da `tools/catalogo-eventi-gen3.py` a partire dalla tabella di PKHeX. Una seconda nota di studio, `STUDIO-02-metodi-di-generazione.md`, che spiega la sigla BACD e perché l'ordine invertito delle estrazioni sia la firma di un esemplare da evento, conferma quattro affermazioni della prima nota nominandone i metodi, chiude il punto che quella lasciava aperto sulla derivazione del sesso dell'allenatore, distingue i due canali di distribuzione che la prima confondeva, e riporta che il metodo di generazione dipende da un'interruzione hardware. E l'identificazione precisa degli esemplari che l'utente possiede dal Pokemon Day del 2006, cioè allenatore `10ANNI`, identificativo 06227, livello 70, metodo `BACD_R_A`: sono il primo vettore di prova autentico che il progetto abbia, e il prossimo passo è confrontarli con il catalogo appena il lettore arriva. Il passo che non richiede hardware resta quello aperto dal 2026-08-28, cioè costruire un esemplare con `pokebridge` e sottoporlo a PKHeX per sapere se una ricreazione fedele passi i controlli di legittimità, e vi si aggiunge il confronto con il costruttore di esemplari del track dell'esecuzione di codice, che produce lo stesso esito per la via opposta. Le due decisioni di perimetro aperte stanno in `pending.md`.

gba-switch-trading: il primo passo è una misura e non un acquisto, cioè collegare l'Archer T2U Nano e leggerne l'identificatore USB, perché il nome commerciale AC600 copre chip diversi e la riserva registrata prima poggiava su una premessa sbagliata. Il track non richiede più Linux, per ADR-015: il demone `ldnd` porta lo stack wireless di Linux su Windows. Resta da clonare i repository e leggere il codice, che nessuno ha ancora aperto.
