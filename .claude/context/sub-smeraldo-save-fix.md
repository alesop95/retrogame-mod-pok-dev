---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - gba-save-extraction-smeraldo/
last-verified-commit: 80fac1f
stato: attivo, convalida hardware sulla cartuccia di prova CONCLUSA il 2026-09-15 (205 esemplari scritti e confermati byte per byte e in gioco), porta COM5; il prossimo collegamento del lettore e' per Smeraldo
---

# Sottoprogetto: correzione del bug inventario di Pokemon Smeraldo

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`. La sezione 8 dell'handoff, "Come riprendere da qui", è un prompt scritto per una chat e resta come storico.

Obiettivo: correggere un inventario corrotto della cartuccia di Pokemon Smeraldo, dove oggetti rari sono finiti nella tasca Strumenti Base, agendo sul salvataggio senza invalidarlo.

## Dove siamo

Il percorso basato su Action Replay è chiuso. Il Master Code e l'Anti-DMA erano stati verificati su più fonti indipendenti, ma per i codici specifici della tasca Strumenti Base non esisteva alcuna fonte affidabile, e indovinare indirizzi di memoria è stato giudicato inaccettabile. Il percorso attivo è l'estrazione fisica del salvataggio: cartuccia verso GBxCart RW 1.4 Pro via USB-C, backup del file con FlashGBX, editing mirato con PKHeX, riscrittura sulla cartuccia e verifica in gioco. Il sistema operativo scelto è Windows 11, perché PKHeX è un'applicazione .NET Windows Forms e il supporto Mono e Wine è stato abbandonato dal 2023.

Il lettore GBxCart RW v1.4 Pro USB-C blu, insieme al cavo USB-A verso USB-C, era stato ordinato il 18 agosto 2026 presso insideGadgets ed è arrivato il 2026-09-09. Collegato il 2026-09-15: il cancello dei driver è superato, e non nel modo previsto da questa scheda. Non è servito il download manuale da wch-ic.com indicato al passo 1 dei sette: Windows ha riconosciuto il dispositivo come "USB Serial" senza driver (codice 28, VID 1A86 PID 7523), poi in circa quaranta secondi lo ha risolto da sé tramite Windows Update, che ha scaricato ed eseguito il pacchetto driver del produttore "wch.cn - Ports" versione 3.9.2024.9, installando il servizio in modalità kernel `CH341SER_A64` (file `CH341S64.SYS`, avvio su richiesta). L'evento 20003 di Microsoft-Windows-UserPnp conferma il legame fra quel servizio e l'istanza di dispositivo `USB\VID_1A86&PID_7523\6&D596480&0&1` con stato 0. Il dispositivo compare ora sotto Porte COM e LPT come "USB-SERIAL CH340 (COM5)", produttore wch.cn, stato "il dispositivo funziona correttamente": nessun punto esclamativo giallo, nessuna azione manuale richiesta. La porta assegnata è **COM5**, che serve a FlashGBX; non è una porta riservata in modo permanente a questo dispositivo, ma alla stessa combinazione di cavo e presa USB tende a riassegnarsi.

## Installazione di FlashGBX, verificata il 2026-09-15

FlashGBX non risultava installato. L'ultima versione è la 5.1, pubblicata il 2026-08-29, e il pacchetto "Windows Setup" (`FlashGBX-5.1_Windows-x64_Setup.zip`, contenente `FlashGBX-5.1_Windows-x64_Setup.exe`) è stato aggiunto il 2026-09-08: è quello indicato dall'handoff alla sezione 3.4 ("Windows Setup 64-bit"). Scaricato dalla release ufficiale `github.com/Lesserkuma/FlashGBX/releases/tag/5.1` e verificato byte per byte sul digest SHA-256 dichiarato dall'API di GitHub prima di consegnarlo all'installazione. Il suo `README.md` dichiara che la variante Setup include anche i driver di dispositivo: può quindi riproporre l'installazione di CH340/CH341, che è già avvenuta tramite Windows Update ed è innocua da ripetere.

## I campi Save Type, Profile e ROM Size in FlashGBX

Verificato il 2026-09-15 esplorando i menu a tendina prima di collegare qualunque cartuccia: "Profile" elenca centinaia di chip flash specifici, e serve solo per le flashcart/cartucce di riproduzione dove il rilevamento automatico è ambiguo; "Save Type" e "ROM Size" sono gli stessi campi che il rilevamento automatico riempie da sé leggendo l'intestazione. Su una cartuccia originale come Rubino o Smeraldo, licenziata e catalogata nel database di FlashGBX, nessuno dei tre va impostato a mano: si lasciano su "Generic ROM Cartridge" prima dell'inserimento, e dopo la lettura mostreranno il valore rilevato. Il tipo di salvataggio atteso per la terza generazione, "1M FLASH (128 KiB)", è nell'elenco e coincide con quanto `pokebridge/save3.py` già assume.

## Prima lettura riuscita, 2026-09-15

Il Rubino di prova è stato letto correttamente da FlashGBX in modalità Game Boy Advance: `AGB-AXVI-0` (il suffisso `I` confermando su hardware reale che le cartucce possedute sono italiane, coerente con quanto già registrato), ROM riconosciuta nel database (No-Intro) con checksum valido, tipo di salvataggio rilevato in automatico `1M FLASH (128 KiB)`, coerente con quanto `pokebridge/save3.py` già assume per la terza generazione. Nessun campo (Save Type, ROM Size, Profile) ha richiesto intervento manuale. È la prima conferma su dati reali, non dedotta, e vale da precedente per la sessione su Smeraldo.

## Comportamento dell'interfaccia da ricordare

Verificato il 2026-09-15: il Platform Mode di FlashGBX non si mantiene fra una connessione e l'altra. Ogni volta che il lettore si disconnette e si ricollega, l'interfaccia torna a "Ready. Please select Platform Mode." con nessuna delle due modalità selezionata, anche se la connessione precedente era su Game Boy Advance: va riselezionata a mano prima di ogni lettura, e solo dopo va verificato il LED.

## Prossimo passo concreto

La convalida sulla cartuccia di prova è conclusa il 2026-09-15, con un margine ben oltre il minimo previsto: non un solo esemplare di controllo ma 205 (un Pikachu il 2026-09-15 mattina, poi un lotto di 204 lo stesso pomeriggio, cioè tutto ciò che il progetto aveva prodotto e giudicato conforme in formato di terza generazione), con backup in doppia copia verificato per hash prima di ogni scrittura, read-back per hash dopo, e un controllo visivo su un video della console vera che mostra i box coerenti con l'atteso (compresi i cinquanta esemplari del gruppo "con mossa" che risultano Uova non ancora schiuse, con il testo di dono speciale corretto) e il gioco che torna regolare al menu dopo l'uscita dai box. La catena hardware-driver-software (FlashGBX su COM5, modalità terza generazione a 3,3 V verificata sul LED, backup doppio, scrittura, read-back) è quindi validata anche su un lotto grande e non solo su un singolo esemplare.

Il prossimo collegamento del lettore è per Smeraldo, secondo la sequenza già stabilita in `RUNBOOK-PRIMA-SESSIONE.md`, che ordina le operazioni per irreversibilità e non per interesse: le cartucce di prima e seconda generazione la cui pila potesse ancora tenere erano l'unica finestra che si chiude da sé, e la diagnosi del 2026-09-01 le ha già escluse in negativo (nessun salvataggio recuperabile su nessuna delle due), quindi non restano passi intermedi prima di Smeraldo. Prima di intervenire, l'utente ha segnalato che la cartuccia porta danni pregressi dai tentativi con codici Action Replay: il primo passo su Smeraldo resta comunque il backup in doppia copia previsto dallo step 1 del runbook, seguito da un controllo di sola lettura con `gba-save-extraction-smeraldo/tools/emerald_bag_decode.py` prima di qualunque ipotesi sulla causa o di qualunque scrittura, esattamente come il runbook già prescriveva indipendentemente da questa segnalazione.

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
