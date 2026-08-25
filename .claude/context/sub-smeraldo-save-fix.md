---
generated-from-commit: d1e1a3a
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - gba-save-extraction-smeraldo/
last-verified-commit: effc2e0
stato: attivo, bloccato su riscontro hardware
---

# Sottoprogetto: correzione del bug inventario di Pokemon Smeraldo

Lo stato canonico di questo track e' questo file, insieme alla riga che lo riguarda in `memory/index.md`. La sezione 8 dell'handoff, "Come riprendere da qui", e' un prompt scritto per una chat e resta come storico.

Obiettivo: correggere un inventario corrotto della cartuccia di Pokemon Smeraldo, dove oggetti rari sono finiti nella tasca Strumenti Base, agendo sul salvataggio senza invalidarlo.

## Dove siamo

Il percorso basato su Action Replay e' chiuso. Il Master Code e l'Anti-DMA erano stati verificati su piu' fonti indipendenti, ma per i codici specifici della tasca Strumenti Base non esisteva alcuna fonte affidabile, e indovinare indirizzi di memoria e' stato giudicato inaccettabile. Il percorso attivo e' l'estrazione fisica del salvataggio: cartuccia verso GBxCart RW 1.4 Pro via USB-C, backup del file con FlashGBX, editing mirato con PKHeX, riscrittura sulla cartuccia e verifica in gioco. Il sistema operativo scelto e' Windows 11, perche' PKHeX e' un'applicazione .NET Windows Forms e il supporto Mono e Wine e' stato abbandonato dal 2023.

Il lettore GBxCart RW v1.4 Pro USB-C blu, insieme al cavo USB-A verso USB-C, e' stato ordinato il 18 agosto 2026 presso insideGadgets. Il setup software e' fermo al primo dei sette step: l'installazione dei driver CH340 e CH341 scaricati da wch-ic.com.

## Prossimo passo concreto

Confermare l'esito dell'installazione dei driver. Il criterio di successo, dalla sezione 5.4 dell'handoff, e' che in Gestione Dispositivi, sotto "Porte (COM e LPT)", compaia una voce del tipo USB-SERIAL CH340 seguita dal numero di porta, senza punto esclamativo giallo, annotando quale porta COM viene assegnata. Finche' questo riscontro manca il track e' bloccato, e non e' lavoro da fare ma una verifica che spetta a te sulla macchina.

## Decisioni aperte

Quali slot e quali oggetti esatti della tasca Strumenti Base vadano corretti non e' ancora deciso, e non e' decidibile prima di aver aperto il salvataggio in sola lettura: e' lo step 7 della sequenza. Resta da confermare a hardware in mano che FlashGBX riconosca in auto-detect il tipo di memoria di Smeraldo, che e' Flash. Il manuale ufficiale reperibile e' fermo alla revisione 1.3, quindi sono possibili micro-differenze non documentate rispetto alla 1.4.

## Scoperta trasversale da usare nella diagnosi

In Smeraldo le quantita' degli oggetti nello zaino e il denaro non stanno in chiaro: sono in XOR con una chiave di sicurezza a 32 bit che sta nella sezione 0 del salvataggio all'offset 0x00AC. Le quantita' del deposito PC invece sono in chiaro, e Rubino e Zaffiro non mascherano nulla. La verifica viene dal sorgente di `pret/pokeemerald`, dove `GetBagItemQuantity` applica la maschera e `GetPCItemQuantity` no. Ne segue che una quantita' assurda letta in chiaro dallo zaino non e' una prova di corruzione ma l'aspetto normale di un dato mascherato, mentre una quantita' assurda nel deposito PC e' un'anomalia vera. Lo strumento che applica la distinzione a un dump e' `tools/emerald_bag_decode.py`, che valida le sezioni, sceglie lo slot piu' recente, smaschera lo zaino e riferisce cinque classi di anomalia, senza scrivere nulla.

## Vincolo non negoziabile

Il backup del salvataggio originale si fa in doppia copia prima di qualsiasi scrittura, e nessuna scrittura sulla cartuccia avviene senza un read-back verificato. La regola completa sta in `rules/hardware-and-perimeter.md`.

## Evidenze e materiale locale

Gli screenshot del checkout contenevano dati personali, non sono mai entrati in git e sono stati eliminati dal disco il 24 agosto 2026: quanto documentavano, cioe' l'ordine del 18 agosto e la configurazione acquistata, e' scritto qui sopra senza alcun dato personale. Il PDF di sette pagine che fotografa lo stato corrotto dell'inventario e le foto delle sessioni stanno in `_notes/media/gba-save-extraction-smeraldo/`, che rispecchia le cartelle-data del sottoprogetto: presenti sul disco, mai tracciati. Il chat log della giornata del 17 agosto non e' mai stato salvato: il file era vuoto ed e' stato rimosso.
