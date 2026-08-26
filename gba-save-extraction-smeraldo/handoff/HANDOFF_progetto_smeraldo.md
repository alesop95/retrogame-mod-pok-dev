# HANDOFF - Progetto correzione bug tasca "Strumenti Base" (Pokémon Smeraldo)

> Documento di passaggio completo, pensato per essere letto/ripreso dentro una sessione Claude Code. Contiene: contesto del problema, ogni decisione tecnica presa e perché, ogni fonte verificata, lo stato esatto di avanzamento, e i prossimi passi operativi nel dettaglio. Nessuna sintesi è stata fatta a scapito dei dettagli tecnici: dove un dato è stato verificato con web search in sessione, è segnalato come tale.

**Ultimo aggiornamento:** 18/08/2026  
**Stato generale:** hardware acquistato, in fase di setup software su Windows 11 - primo step (driver CH340/CH341) guidato, in attesa di conferma esito dall'utente.

---

## 0. Allegati / artifact prodotti finora

| File | Contenuto | Percorso |
|---|---|---|
| `progetto_smeraldo_contesto.md` | Log di sessione precedente, versione precursore di questo handoff (mantenuto per storico) | `gba-save-extraction-smeraldo/handoff/progetto_smeraldo_contesto.md` |
| `HANDOFF_progetto_smeraldo.md` | Questo file - versione definitiva e completa | `gba-save-extraction-smeraldo/handoff/HANDOFF_progetto_smeraldo.md` |

File di progetto originali, percorsi relativi alla radice del repository:
- `gba-save-extraction-smeraldo/2026-08-16-analisi-action-replay/2026-08-16-note-analisi-action-replay.txt` - chat log originale con i codici Action Replay e le fonti
- `_notes/media/gba-save-extraction-smeraldo/2026-08-16-analisi-action-replay/bug-tasca-strumenti-base-smeraldo.pdf` - PDF di 7 pagine, screenshot del bug originale nella tasca Strumenti Base (contenuto visivo, non testo estraibile); non tracciato, per la politica sui media
- Il chat log della giornata del 17 agosto sulla ricerca hardware non è stato salvato: il file era vuoto ed è stato rimosso. Il suo contenuto è ricostruito nella sezione 3 di questo handoff.
- `source1.url` → `source8.url` - 8 shortcut Windows alle fonti usate nell'analisi Action Replay del 16/08

---

## 1. Il problema di partenza

Bug nell'inventario di Pokémon Smeraldo: oggetti rari sono finiti nella tasca sbagliata ("Strumenti Base") a causa di un bug di gioco (probabilmente un errore di categorizzazione ID oggetto lato codice del gioco, non un errore dell'utente). Obiettivo: correggere l'inventario del salvataggio senza rovinare il resto della partita né invalidare il salvataggio.

Due strade sono state esplorate, in ordine cronologico.

---

## 2. Percorso A - Action Replay (16-17/08/2026) - **CHIUSO, non più attivo**

### 2.1 Cosa è stato trovato e perché è affidabile

Un Master Code funzionante per la versione FR (French/francese) di Pokémon Smeraldo era già disponibile e verificato:

```
D8BAE4D9
4864DCE5
A7308156
808311D9
```

Analizzando il codice a 8 righe fornito inizialmente, si è capito che in realtà erano **due codici distinti concatenati**, entrambi necessari su hardware GBA reale (non emulatore):
- Le prime 4 righe = Master Code
- Le ultime 4 righe = **Anti-DMA**, un codice complementare che su console vera serve quasi sempre insieme al master code, perché molti altri codici AR (oggetti, soldi, incontri) non si attivano correttamente senza di esso:

```
A57E2EDE
A5AFF3E4
1C7B3231
B494738C
```

**Perché questo è tecnicamente rilevante:** il Master Code su Action Replay serve a "sbloccare" l'accettazione di codici cheat aggiuntivi da parte del gioco (bypassa il checksum/protezione anti-cheat del gioco). L'Anti-DMA gestisce invece i conflitti di accesso alla memoria durante il DMA transfer (Direct Memory Access) della GBA - motivo per cui su hardware reale, dove il timing dell'accesso a memoria è reale e non emulato, serve quasi sempre; su emulatore molti codici funzionano anche senza, perché l'emulazione del DMA è spesso semplificata o assente.

### 2.2 Fonti incrociate (verificate/multiple, per questo il Master+Anti-DMA è stato considerato affidabile)
- tecnocino.it
- nanotec2009.it
- poketown.net (due thread distinti)
- forum.pokemoncentral.it
- regnodellepassioni.forumattivo.com
- pokemontrash.com (fonte separata, in francese, che ha confermato indipendentemente lo stesso codice)

### 2.3 Perché la strada è stata abbandonata

Per i codici specifici della tasca Strumenti Base (Detector, Ami, Bici e altri strumenti base) **non è stata trovata nessuna fonte verificata** compatibile con questa combinazione Master+Anti-DMA. Continuare la ricerca in questa direzione avrebbe significato **indovinare indirizzi di memoria** per costruire codici AR custom - esattamente il tipo di operazione rischiosa che ha causato il bug originale nell'inventario. Si è quindi deciso di **fermarsi consapevolmente** piuttosto che fornire codici non testati, per evitare di introdurre un secondo bug o corrompere ulteriormente il salvataggio.

### 2.4 Alternativa raccolta dalla community (il seme del Percorso B)

Nella stessa community pokemontrash.com, in un thread separato, qualcuno chiedeva come rimuovere oggetti rari finiti per errore nel sacco. La risposta ricevuta, valutata come la più sensata, indicava che la via corretta è **agire direttamente sul file di salvataggio con un editor** (non altri codici AR): aprire il salvataggio ed editare/eliminare gli oggetti direttamente nell'inventario. Questo ha impostato la direzione del Percorso B.

---

## 3. Percorso B - Estrazione fisica del .sav + editor di salvataggio (17-18/08/2026) - **ATTIVO, in corso**

### 3.1 Perché questo approccio è tecnicamente superiore all'Action Replay per questo caso specifico

L'Action Replay agisce in **runtime**, iniettando valori in indirizzi di memoria RAM mentre il gioco gira: è preciso solo se si conosce l'indirizzo esatto della struttura dati interessata, e un errore può corrompere altre aree di memoria. Lavorare invece direttamente sul **file di salvataggio (.sav)** con un editor dedicato (PKHeX) è più sicuro perché l'editor conosce la struttura dati ufficiale del gioco (formati Pokémon, struttura inventario, checksum) e valida le modifiche prima di scriverle, riducendo drasticamente il rischio di corruzione rispetto a un indirizzo di memoria indovinato a mano.

### 3.2 Pipeline concordata (end-to-end)

```
Cartuccia Pokémon Smeraldo (fisica)
  → GBxCart RW 1.4 Pro (InsideGadgets)   [hardware reader/writer]
  → connessione USB-C
  → FlashGBX (software PC)               [legge la cartuccia, esegue il backup del save]
  → file .sav (copia locale su PC)
  → PKHeX (software PC)                  [ispezione, verifica legalità dati, editing mirato]
  → file .sav modificato
  → FlashGBX (restore/scrittura)
  → GBxCart RW
  → cartuccia (save riscritto)
```

Non servono, e sono stati esclusi consapevolmente: Action Replay, flashcart GBA, batteria nuova della cartuccia, saldature - perché l'operazione avviene interamente sul file di salvataggio, non sull'hardware della cartuccia in sé (a parte lettura/scrittura del chip di memoria save, che è non invasiva).

### 3.3 Scelta hardware - GBxCart RW 1.4 Pro (InsideGadgets)

**Alternative valutate:**
- **GBxCart RW 1.4 Pro** (InsideGadgets) - scelto
- **GB Operator** (Epilogue) - scartato dopo confronto su una discussione Reddit (r/Gameboy) trovata durante la ricerca, risultato meno documentato del GBxCart

**Motivazione della scelta (dichiarata esplicitamente dall'utente, verificata tecnicamente):** Non è stata una scelta di "sicurezza superiore" - è stata una scelta di **massimo controllo sull'operazione senza pagare funzionalità superflue**, basata su: hardware molto documentato, supporto esplicito a GBA e a tutti i tipi di memoria save GBA (SRAM/Flash/EEPROM), uso di FlashGBX come software, e supporto esplicito e documentato a backup/restore dei salvataggi.

**Specifiche tecniche confermate (verificate via web fetch diretto sulla pagina del produttore):**
- Solo la versione **v1.4 Pro (USB-C)** è attualmente in vendita (la v1.3 non è più in produzione)
- Prezzo: $33.00-$37.00 a seconda di colore/cavo incluso
- Miglioramenti della v1.4 Pro rispetto alle precedenti: più veloce, controllo dello stato di alimentazione via pulsante o software (non serve scollegare USB per cambiare cartuccia), 2 LED di stato aggiuntivi (Completed & Error)
- La variante "Pro" permette anche di alloggiare il GBxCart dentro un guscio di riproduzione cartuccia GBA (non incluso, richiede lima); nessuna differenza funzionale rispetto alla versione non-Pro
- Auto-detect del tipo di memoria save (rilevante: Pokémon Smeraldo usa memoria **Flash**)
- Compatibilità dichiarata dal produttore: Windows, macOS, Linux

**Canale d'acquisto:**
- Shop ufficiale: `https://shop.insidegadgets.com/product/gbxcart-rw/`
- Distributori autorizzati dichiarati dal produttore: Retro Game Repair Shop (USA), ZedLabz (UK/EU), Retro Modding (Canada), Mod in France
- ⚠️ eBay **non** è un canale ufficiale dichiarato dal produttore - segnalato come attenzione, non come blocco
- **Manuale ufficiale** (fermo alla revisione 1.3, non è stata trovata una versione aggiornata specifica per 1.4): `https://www.gbxcart.com/wp-content/uploads/2019/10/GBxCart-RW-Manual-Rev43.pdf`

**STATO: ✅ ACQUISTO COMPLETATO - 18/08/2026**  
Colore acquistato: **blu**. Confermato dall'utente dopo verifica diretta della pagina prodotto in sessione.

### 3.4 Scelta software

**FlashGBX** - https://github.com/lesserkuma/FlashGBX
- Comunica col GBxCart RW via porta seriale virtuale, esegue backup/restore del file .sav e dump della ROM
- Windows: **GUI ufficiale** - dalla versione 4 in poi include il runtime Python incorporato (non serve installare Python separatamente)
- Linux/macOS: versione ufficiale a riga di comando (Console Interface) - supportata, ma meno immediata della GUI Windows
- **Correzione fatta in sessione:** inizialmente si era indicato erroneamente che servisse anche il Microsoft Visual C++ Redistributable. Verificato che questo requisito valeva per il **vecchio** software GUI di InsideGadgets (2018), non per FlashGBX. FlashGBX non lo richiede.

**PKHeX** - https://github.com/kwsch/PKHeX
- Editor/verificatore di file di salvataggio Pokémon
- È un'applicazione **.NET Windows Forms**: nativamente Windows-only
- **Verificato in sessione:** dal 2023 PKHeX ha abbandonato definitivamente qualunque supporto a Mono/Wine - non esiste più una via ufficiale Linux/macOS. Su Linux, tentare di farlo girare via Mono produce crash noti (riferimenti trovati: GitHub issue #3059, #229, discussion #3977 del repo PKHeX), e le alternative (Wine + .NET Framework datato installato manualmente) sono workaround non ufficiali, non garantiti stabili nel tempo
- **Requisito software confermato:** PKHeX nella versione corrente richiede **.NET 9 Desktop Runtime** (scaricabile da dotnet.microsoft.com, link diretto presente anche nella pagina release di PKHeX su GitHub). Senza questo runtime installato, l'eseguibile non si avvia.
- Formato di distribuzione: portable, .zip - non serve un vero e proprio installer, basta estrarre e lanciare `PKHeX.exe`

### 3.5 Scelta del sistema operativo - Windows 11 (RACCOMANDAZIONE MOTIVATA E CONFERMATA)

Questo è stato un punto di decisione esplicito richiesto dall'utente fin dall'inizio del Percorso B ("consigliami fin dal principio se è meglio Windows 11 o Linux").

**Analisi tecnica:**
- FlashGBX da solo non genera una preferenza: gira ufficialmente bene sia su Windows (GUI) sia su Linux/macOS (CLI)
- **Il fattore decisivo è PKHeX**: essendo nativo solo Windows e avendo abbandonato ogni supporto Mono/Wine dal 2023, su Linux la sua esecuzione è instabile e non ufficialmente supportata
- Su Windows 11, l'intera pipeline (FlashGBX + PKHeX) gira nativamente, senza livelli di compatibilità aggiuntivi, con il solo overhead dell'installazione dei driver USB (CH340/CH341) e del runtime .NET 9

**Conclusione:** Windows 11 per l'intera operazione. Se il sistema principale dell'utente fosse stato Linux, la raccomandazione sarebbe stata una VM Windows 11 o un dual boot dedicato, per evitare di rincorrere soluzioni Wine/Mono fragili solo per PKHeX.

**STATO:** confermato dall'utente ("posso utilizzare windows 11 senza problemi"). Nessun problema di compatibilità aperto su questo fronte.

---

## 4. Setup software su Windows 11 - sequenza operativa completa

Sequenza concordata, in 7 passaggi macro (il dettaglio tecnico-didattico di ciascuno è nella sezione 5):

1. Installare driver CH340/CH341 per Windows - **IN CORSO, step attuale**
2. Scaricare e installare FlashGBX (Windows Setup 64-bit) da `github.com/lesserkuma/FlashGBX/releases/latest`
3. Collegare GBxCart RW via USB-C (senza cartuccia inserita), verificare che FlashGBX lo riconosca
4. Inserire la cartuccia di Pokémon Smeraldo, leggere le info cartuccia in FlashGBX (Logo Check OK, tipo di memoria save auto-rilevato - atteso: Flash)
5. **Backup del file .sav originale** - passaggio critico e non negoziabile, da fare con doppia copia in cartelle/drive separati, PRIMA di qualunque editing
6. Installare .NET 9 Desktop Runtime, poi PKHeX (versione portable .zip da GitHub)
7. Aprire il backup in PKHeX **solo in lettura** (ispezione tasca oggetti, legality checker) per fotografare l'entità esatta del bug prima di qualunque modifica

---

## 5. Dettaglio tecnico-didattico dello step attuale - Driver CH340/CH341

### 5.1 Perché serve (spiegazione tecnica completa)

Il GBxCart RW non comunica col PC via un chip USB nativo per trasferimento dati generico: internamente usa un collegamento **seriale (UART)**, e per convertire questo segnale seriale in un segnale USB standard utilizza un **chip ponte USB-to-Serial** della famiglia **CH340/CH341**, prodotto da WCH (Nanjing Qinheng Microelectronics).

Windows non include questo driver di serie ("out of the box"). Al primo collegamento del dispositivo, senza driver installato, Windows lo rileva come:
- dispositivo sconosciuto, oppure
- "USB 2.0 Serial Device" con punto esclamativo giallo in Gestione Dispositivi

Una volta installato correttamente il driver CH340/CH341, Windows espone il dispositivo come **porta COM virtuale** (es. COM5, COM7...) sotto "Porte (COM e LPT)" in Gestione Dispositivi. **È proprio questa porta COM che FlashGBX userà** per inviare comandi al GBxCart RW (leggi info cartuccia, esegui backup save, scrivi save, ecc.). Se questo passaggio fallisce o è incompleto, nessuno step successivo della pipeline può funzionare: FlashGBX non avrà nulla a cui collegarsi a livello di sistema operativo.

### 5.2 Fonte scelta per il download (verificata in sessione)

È stata scartata la scelta di scaricare il driver da uno dei tanti siti aggregatori/mirror di terze parti (comuni per questo tipo di driver, e spesso poco affidabili), a favore della **fonte ufficiale del produttore del chip**:

`https://www.wch-ic.com/downloads/CH341SER_EXE.html`

Motivazione: è il sito diretto di WCH (Nanjing Qinheng Microelectronics), produttore del chip CH340/CH341. Il pacchetto scaricato da qui è **certificato Microsoft WHQL** (Windows Hardware Quality Labs) e firmato digitalmente - garanzia superiore rispetto a mirror di terze parti.

### 5.3 Procedura operativa (fornita all'utente, in attesa di riscontro)

1. Scaricare il pacchetto `CH341SER.EXE` da `https://www.wch-ic.com/downloads/CH341SER_EXE.html`
2. Eseguirlo come amministratore (tasto destro → "Esegui come amministratore")
3. Nella finestra dell'installer, premere il pulsante **INSTALL** (non UNINSTALL)
4. Attendere il messaggio di conferma di installazione riuscita
5. **Non collegare ancora il GBxCart RW** durante questa fase - il driver va installato prima di collegare l'hardware, non dopo
6. Solo a installazione completata, collegare il GBxCart RW blu via USB-C

### 5.4 Verifica dell'esito (criterio di successo per chiudere questo step)

Aprire **Gestione Dispositivi** (tasto destro sul menu Start → Gestione Dispositivi) e controllare sotto la categoria **"Porte (COM e LPT)"**:
- **Successo:** compare una voce tipo *"USB-SERIAL CH340 (COMx)"*, senza punto esclamativo giallo
- Da annotare: il numero della porta COM assegnata (es. COM5) - può servire in seguito se FlashGBX non rileva il dispositivo automaticamente e serve selezionare la porta manualmente

**STATO ATTUALE:** procedura fornita all'utente, **in attesa di conferma dell'esito** prima di passare allo step 2 (installazione FlashGBX).

---

## 6. Cosa NON è stato ancora fatto (elenco esplicito per evitare di saltare passaggi)

- [ ] Conferma installazione driver CH340/CH341 e verifica porta COM (step corrente)
- [ ] Download e installazione FlashGBX
- [ ] Primo collegamento GBxCart RW e verifica di riconoscimento in FlashGBX
- [ ] Inserimento cartuccia e lettura info (Logo Check, tipo memoria save)
- [ ] Backup del .sav originale (doppia copia)
- [ ] Installazione .NET 9 Desktop Runtime
- [ ] Installazione PKHeX
- [ ] Apertura del backup in PKHeX in sola lettura per fotografare l'entità del bug
- [ ] Editing mirato del bug tasca Strumenti Base (da pianificare nel dettaglio quando si arriva a questo punto - non ancora discusso nello specifico di quali oggetti/slot vadano corretti)
- [ ] Restore del .sav modificato su cartuccia via FlashGBX
- [ ] Verifica in game su hardware reale

## 7. Note aperte / rischi da tenere presenti più avanti (non ancora risolte)

- Non è stata trovata una versione del manuale ufficiale specifica per la revisione 1.4 (l'unico manuale reperito è fermo alla rev 1.3/rev 43) - possibili micro-differenze nell'interfaccia software non documentate
- Da confermare a hardware in mano: che FlashGBX rilevi correttamente il tipo di memoria save di Pokémon Smeraldo (Flash) in auto-detect, senza bisogno di forzare manualmente il tipo
- Non ancora pianificato nel dettaglio: quali oggetti/slot esatti della tasca Strumenti Base andranno corretti in PKHeX una volta aperto il salvataggio - questo verrà definito nello step 7 della sequenza operativa (ispezione in sola lettura), quando si potrà vedere l'esatto stato corrotto dell'inventario

---

## 8. Come riprendere da qui

Se questa sessione viene ripresa in Claude Code (o in una nuova sessione Claude), il prossimo messaggio utile dall'utente è la conferma dell'esito dell'installazione del driver CH340/CH341 (sezione 5.4). Da lì si procede con lo step 2 (installazione FlashGBX), mantenendo lo stesso livello di dettaglio tecnico-didattico per ogni passaggio, e aggiornando questo stesso file ad ogni step completato.
