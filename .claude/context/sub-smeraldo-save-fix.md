---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - gba-save-extraction-smeraldo/
last-verified-commit: 7696c46
stato: attivo, bloccato su riscontro hardware
---

# Sottoprogetto: correzione del bug inventario di Pokemon Smeraldo

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`. La sezione 8 dell'handoff, "Come riprendere da qui", è un prompt scritto per una chat e resta come storico.

Obiettivo: correggere un inventario corrotto della cartuccia di Pokemon Smeraldo, dove oggetti rari sono finiti nella tasca Strumenti Base, agendo sul salvataggio senza invalidarlo.

## Dove siamo

Il percorso basato su Action Replay è chiuso. Il Master Code e l'Anti-DMA erano stati verificati su più fonti indipendenti, ma per i codici specifici della tasca Strumenti Base non esisteva alcuna fonte affidabile, e indovinare indirizzi di memoria è stato giudicato inaccettabile. Il percorso attivo è l'estrazione fisica del salvataggio: cartuccia verso GBxCart RW 1.4 Pro via USB-C, backup del file con FlashGBX, editing mirato con PKHeX, riscrittura sulla cartuccia e verifica in gioco. Il sistema operativo scelto è Windows 11, perché PKHeX è un'applicazione .NET Windows Forms e il supporto Mono e Wine è stato abbandonato dal 2023.

Il lettore GBxCart RW v1.4 Pro USB-C blu, insieme al cavo USB-A verso USB-C, è stato ordinato il 18 agosto 2026 presso insideGadgets. Il setup software è fermo al primo dei sette step: l'installazione dei driver CH340 e CH341 scaricati da wch-ic.com.

## Prossimo passo concreto

Confermare l'esito dell'installazione dei driver. Il criterio di successo, dalla sezione 5.4 dell'handoff, è che in Gestione Dispositivi, sotto "Porte (COM e LPT)", compaia una voce del tipo USB-SERIAL CH340 seguita dal numero di porta, senza punto esclamativo giallo, annotando quale porta COM viene assegnata. Finché questo riscontro manca il track è bloccato, e non è lavoro da fare ma una verifica che spetta a te sulla macchina.

## Decisioni aperte

Quali slot e quali oggetti esatti della tasca Strumenti Base vadano corretti non è ancora deciso, e non è decidibile prima di aver aperto il salvataggio in sola lettura: è lo step 7 della sequenza. Resta da confermare a hardware in mano che FlashGBX riconosca in auto-detect il tipo di memoria di Smeraldo, che è Flash. Il manuale ufficiale reperibile è fermo alla revisione 1.3, quindi sono possibili micro-differenze non documentate rispetto alla 1.4.

## Scoperta trasversale da usare nella diagnosi

In Smeraldo le quantità degli oggetti nello zaino e il denaro non stanno in chiaro: sono in XOR con una chiave di sicurezza a 32 bit che sta nella sezione 0 del salvataggio all'offset 0x00AC. Le quantità del deposito PC invece sono in chiaro, e Rubino e Zaffiro non mascherano nulla. La verifica viene dal sorgente di `pret/pokeemerald`, dove `GetBagItemQuantity` applica la maschera e `GetPCItemQuantity` no. Ne segue che una quantità assurda letta in chiaro dallo zaino non è una prova di corruzione ma l'aspetto normale di un dato mascherato, mentre una quantità assurda nel deposito PC è un'anomalia vera. Lo strumento che applica la distinzione a un dump è `tools/emerald_bag_decode.py`, che valida le sezioni, sceglie lo slot più recente, identifica il gioco confrontando le prove di tre candidati, smaschera lo zaino e riferisce cinque classi di anomalia, senza scrivere nulla. L'identificazione automatica nasce da un caso reale letto su Project Pokemon: un editor che prende un salvataggio di Smeraldo per uno di Rubino o Zaffiro applica la maschera sbagliata e fa finire gli oggetti negli slot sbagliati. Dalla stessa fonte viene una seconda lezione per la diagnosi: su una cartuccia contraffatta il salvataggio dell'utente non era corrotto ma assente, quindi corruzione e perdita vanno distinte prima di scegliere una procedura.

## La casistica esatta di questa cartuccia

Registrata il 2026-08-26 su indicazione dell'utente, ed è il dato che mancava per orientare la diagnosi. Nella tasca degli strumenti base, da un certo punto in avanti, gli oggetti ordinari sono stati rimpiazzati da Poke Ball. Non è una tasca disordinata: è una sostituzione che comincia a un certo slot e prosegue.

Questa forma dice qualcosa di preciso, e vale distinguerlo da ciò che sembra. In generazione 3 la tasca che contiene un oggetto è determinata dalla regione del salvataggio in cui il suo slot si trova, non dal suo identificativo, e il gioco disegna l'oggetto in base all'identificativo qualunque sia la tasca che lo ospita. Vedere Poke Ball fra gli strumenti base significa quindi che nella regione della tasca degli strumenti sono scritti identificativi appartenenti all'intervallo delle Ball, che su `pret/pokeemerald` va da 1 a 12. Non è un difetto di visualizzazione e non è una tasca da riordinare: sono i dati a essere sbagliati.

Il fatto che la sostituzione cominci a un certo slot e prosegua fino alla fine restringe ulteriormente le ipotesi. Una corruzione casuale colpirebbe slot sparsi; una che ha un punto di inizio e una coda somiglia a una scrittura che ha invaso la regione a partire da un offset, per esempio perché un indice ha sforato la capienza della tasca, oppure perché una routine ha scritto con l'offset di base sbagliato. Le due ipotesi si distinguono guardando che cosa c'è immediatamente prima dello slot di rottura e se la tasca delle Ball risulta a sua volta alterata: se le Ball che compaiono fra gli strumenti sono le stesse che sono sparite dalla loro tasca, si tratta di uno spostamento; se ci sono in entrambi i posti, di una duplicazione.

Nessuna di queste è verificabile prima di avere il dump, e nessuna va data per buona adesso. Ciò che si è fatto è preparare lo strumento a rispondere: `tools/emerald_bag_decode.py` ha ora un controllo di categoria che confronta l'intervallo di ciascun identificativo con la tasca che lo contiene, per le tre categorie che occupano un intervallo contiguo verificato sul sorgente, cioè Ball da 1 a 12, bacche da 133 a 175 e macchine da 289 a 346. Oltre a elencare i casi singoli, cerca il punto di rottura e dichiara se la corruzione ha un inizio invece di essere sparsa, perché quella è l'informazione che indirizza la ricerca della causa. Gli oggetti ordinari e quelli chiave non sono verificabili per intervallo, perché i loro identificativi sono sparsi, e su quelli il controllo tace invece di indovinare.

## Vincolo non negoziabile

Il backup del salvataggio originale si fa in doppia copia prima di qualsiasi scrittura, e nessuna scrittura sulla cartuccia avviene senza un read-back verificato. La regola completa sta in `rules/hardware-and-perimeter.md`.

## Evidenze e materiale locale

Gli screenshot del checkout contenevano dati personali, non sono mai entrati in git e sono stati eliminati dal disco il 24 agosto 2026: quanto documentavano, cioè l'ordine del 18 agosto e la configurazione acquistata, è scritto qui sopra senza alcun dato personale. Il PDF di sette pagine che fotografa lo stato corrotto dell'inventario e le foto delle sessioni stanno in `_notes/media/gba-save-extraction-smeraldo/`, che rispecchia le cartelle-data del sottoprogetto: presenti sul disco, mai tracciati. Il chat log della giornata del 17 agosto non è mai stato salvato: il file era vuoto ed è stato rimosso.
