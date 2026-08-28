# Snapshot di sincronizzazione

Da leggere per primo a inizio sessione. Fotografa lo stato del progetto al commit di riferimento e mappa ogni scheda al suo stato di verifica. È la fonte di verità su cosa è fatto, non le spunte del diario.

Questo progetto ha più sottoprogetti paralleli, oggi sei, quindi il punto di ripresa è un blocco di righe invece che una sola. La riga "Fuoco corrente" è la fonte di verità unica su quale track è attivo adesso: task paralleli non significa nessun default, significa un default dichiarato più N tracce leggibili.

## Stato

```
Branch attivo:         main
Commit di riferimento: 7696c46
Data snapshot:         2026-08-26
```

## Stato di verifica delle schede

| Scheda | Sottoprogetto | last-verified | Stato |
|---|---|---|---|
| STACK.md | trasversale | 7696c46 | aggiornata, apertura corretta e covers-paths esteso a cinque track |
| design-and-security.md | trasversale | 7696c46 | aggiornata, covers-paths esteso a cinque track |
| deployment.md | trasversale | d08a011 | non applicabile, covers-paths vuoto per scelta |
| dev-testing.md | trasversale | 7696c46 | aggiornata, ora copre anche il ponte e dichiara le prove automatiche |
| current-work.md | trasversale | 7696c46 | aggiornata, tabella dei track e covers-paths esteso a cinque track |
| roadmap.md | trasversale | 7696c46 | aggiornata, quinto track e due condizioni verificate |
| sub-3ds-modding.md | 3ds-related | 7696c46 | aggiornata |
| sub-smeraldo-save-fix.md | gba-save-extraction-smeraldo | 7696c46 | aggiornata |
| sub-gen12-gen3-bridge.md | pokemon-gen12-gen3-bridge | 7696c46 | aggiornata |
| sub-gba-switch-trading.md | gba-switch-pokemon-trading | 7696c46 | aggiornata |
| sub-poke-automation.md | poke-automation-study | 7696c46 | aggiornata |
| sub-distributions-events.md | recreate-pokemon-distributions-events | 0529162 | nuova, scritta il 2026-08-28 alla nascita del track |

Le cose in sospeso non stanno qui ma in `pending.md`, che va letto subito dopo questo file: materiale atteso, credenziali, fonti in sospeso, strumenti da richiamare a una condizione, debito di lettura, punti aperti e blocchi materiali.

## Punto di ripresa

```
Fuoco corrente: distributions-events, il sesto track, e con esso l'obiettivo di collezione in Pokemon Home
```

Adozione del sistema: conclusa. La storia git è stata collassata in un unico commit radice il 2026-08-25 per la bonifica di ADR-014, quindi `d08a011` è il commit radice e gli hash citati nelle voci di diario precedenti a quella data non risolvono più. Le schede sono state riconciliate a `7696c46` il 2026-08-26: il drift era quasi tutto contabile, perché erano state aggiornate a mano senza bumpare il checkpoint, e i tre difetti sostanziali trovati nascevano da un unico punto cieco, cioè `covers-paths` trasversali che non seguivano l'aggiunta di un sottoprogetto. Ora lo seguono, e la procedura di aggiunta in `CLAUDE.md` ha un quarto passo che lo impone. Convenzione Markdown conforme su tutto il repository, nulla da fare su questo fronte.

3ds-modding: dumpare le cinque cartucce DS rimanenti, Diamante, Perla, Platino, Nera 2 e SoulSilver, poi trasferire i file da `/gm9/out/` al PC. Nessun blocco.

smeraldo-save-fix: confermare che i driver CH340 siano installati e annotare la porta COM assegnata. Bloccato sul riscontro alla macchina e sull'arrivo del lettore ordinato il 18 agosto 2026. Quando il dump arriverà c'è già lo strumento che lo legge, `tools/emerald_bag_decode.py`, e c'è una scoperta che cambia l'ipotesi di partenza: le quantità dello zaino sono mascherate in XOR e vanno smascherate prima di chiamarle corrotte.

gen12-gen3-bridge: la struttura di generazione 3 è scritta e collaudata dal 2026-08-26, in `pokebridge/gen3.py`, con cifratura, permutazione e checksum verificati sul sorgente di pokeemerald; la suite passa 114 prove. Il prossimo passo è lo strato del salvataggio da 128 KiB, cioè la sezione 6 della referenza, oppure il generatore del salvataggio sintetico da confrontare con PKHeX, che chiude il limite noto della prova di simmetria e non richiede hardware. Il formato dati è documentato byte per byte e verificato sul disassemblato, con undici punti dubbi chiusi e due affermazioni dell'handoff corrette; l'handoff è stato ritirato per ADR-013. Non bloccato: il lavoro comune non dipende da ADR-008, e la discovery hardware serve solo all'ultimo tratto.

poke-automation: lo studio è cominciato il 2026-08-26 e la prima nota sta nella cartella del sottoprogetto, quindi il track non è più un semplice collegamento. Resta da decidere se si fermi allo studio, se diventi il riuso della parte su microcontrollore in comune con l'opzione D del ponte, oppure automazione vera su Switch come obiettivo indipendente. Sul perimetro c'è una notizia buona e verificata: il progetto di riferimento dichiara console non modificate e nessun accesso alla memoria, quindi il suo perimetro è compatibile con le regole di questo progetto, e ciò che resta da dichiarare è il nostro.

distributions-events: il track nasce il 2026-08-28 e ha una scadenza esterna verificata, cioè la chiusura di Pokemon Bank il 26 febbraio 2027, perché l'obiettivo dichiarato dall'utente non è la ricreazione in sé ma avere in Pokemon Home tutte le 1025 specie e le forme alternative, come collezione da portare avanti per tutta la vita. Le quattro fonti video sono lette e la conoscenza sta nello studio della cartella del sottoprogetto. Il prossimo passo non richiede hardware: costruire un esemplare con `pokebridge` e sottoporlo a PKHeX per sapere se una ricreazione fedele passi i controlli di legittimità. Due decisioni di perimetro sono aperte e vanno prese dall'utente prima di procedere sull'ultimo tratto, e stanno in `pending.md`.

gba-switch-trading: il primo passo è una misura e non un acquisto, cioè collegare l'Archer T2U Nano e leggerne l'identificatore USB, perché il nome commerciale AC600 copre chip diversi e la riserva registrata prima poggiava su una premessa sbagliata. Il track non richiede più Linux, per ADR-015: il demone `ldnd` porta lo stack wireless di Linux su Windows. Resta da clonare i repository e leggere il codice, che nessuno ha ancora aperto.
