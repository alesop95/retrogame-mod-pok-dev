# Step 03 - Dump cartucce fisiche (3DS / DS) via GodMode9

## Prerequisito
Step 02 completato: boot9strap + Luma3DS v13.4 attivi (confermato "Booted from SD via B9S"). GodMode9 è tipicamente già presente come payload sulla SD, installato insieme al pacchetto MSET9/boot9strap durante lo Step 02.

## Cos'è GodMode9 e perché lo usiamo
GodMode9 è un file manager con accesso a basso livello che gira **prima** del sistema operativo del 3DS (bootato direttamente da Luma3DS come "payload"). A differenza di un'app normale, ha accesso diretto ai controller hardware - incluso quello del carrello cartucce - e può leggere il contenuto grezzo di una cartuccia fisica bit per bit, salvandolo come file `.3ds`/`.nds` sulla SD. Questo è ciò che chiamiamo "dump": una copia di backup digitale di un supporto che possiedi fisicamente.

## Verifica presenza GodMode9

### Procedura
1. Spegni completamente il 3DS
2. Tieni premuto **Start**, e mentre lo tieni premuto, premi anche il tasto **Power**
3. Rilascia entrambi dopo l'accensione dello schermo
4. Se appare direttamente l'interfaccia testuale rossa/gialla di GodMode9 → è già installato, procedi al dump
5. Se appare invece un "chainloader menu" con più opzioni → usa D-Pad per selezionare **GodMode9** e premi A
6. Se non appare nulla di tutto ciò (torna alla Home normale) → GodMode9 non è ancora installato, serve installarlo separatamente (fammelo sapere, ti guido nel passaggio aggiuntivo da `https://3ds.hacks.guide/godmode9-usage.html`)

---

## Dump di una cartuccia 3DS

**Significato tecnico:** il gioco 3DS su cartuccia è cifrato con chiavi legate all'hardware. GodMode9, girando con privilegi di sistema, può leggere il contenuto e produrre un file `.3ds` (formato NCSD) sia in versione cifrata (uguale al contenuto reale della cartuccia) sia in chiaro, a seconda dell'opzione scelta - per uso con Azahar serve la versione **decrittata**.

### Procedura
1. Inserisci la cartuccia 3DS nello slot della console
2. Boot in GodMode9 (Start + Power)
3. Nella schermata principale, seleziona **[C:] GAMECART** (D-Pad + A)
4. Comparirà un file tipo `<TitleID>_<version>.trim.3ds`
5. Selezionalo con A, poi scegli **"NCSD image options..."**
6. Scegli **"Decrypt file (0:/gm9/out)"** (questo è il formato che Azahar può leggere direttamente)
7. Attendi il completamento (dipende dalla dimensione del gioco, da pochi minuti a oltre 30)
8. Premi A per confermare, poi esci da GodMode9 (Home o combinazione di uscita)
9. Il file dumpato si trova ora in **`/gm9/out/`** sulla SD

---

## Dump di una cartuccia DS

**Nota tecnica:** i vecchi giochi DS non usano cifratura NCSD, sono file `.nds` "grezzi" - il dump è quindi più semplice, in pratica una copia diretta del contenuto della cartuccia.

### Procedura
1. Inserisci la cartuccia DS nello stesso slot cartucce del 3DS (compatibile all'indietro)
2. Boot in GodMode9 (Start + Power)
3. Naviga su **[C:]** (la lettera assegnata al gamecart, DS in questo caso)
4. Individua il file `<TitleID>.nds`
5. Selezionalo con A → scegli **"Copy to 0:/gm9/out"**
6. Attendi il completamento
7. Il file si troverà in **`/gm9/out/`** sulla SD, pronto per essere prelevato

---

## Prelievo dei file dumpati sul PC
1. Spegni il 3DS, estrai la SD
2. Inseriscila nel PC
3. Naviga fino a `[lettera unità]/gm9/out/`
4. Copia i file `.3ds`/`.nds` in una cartella del PC dedicata ai tuoi backup (es. `Documenti\3DS-Backups`)

## Collegamento con lo Step 04 (da flusso-3ds.html)
I file `.3ds` decrittati dumpati qui sono direttamente compatibili con **Azahar** (Step 04) - basta puntare la sua Applications Folder alla cartella dove li hai copiati.

## Log di esecuzione

### 2026-08-23 - Dump cartuccia Omega Ruby: risoluzione problema seed encryption
- Errore iniziale: `Decryption failed` durante decrypt NCSD in GodMode9
- Causa identificata: Omega Ruby usa **seed encryption** (introdotta a fine 2014 per titoli con funzionalità online), richiede `seeddb.bin` non presente di default
- Procedura di risoluzione applicata: generazione seed tramite avvio del gioco con connessione internet attiva → dump del file di sistema dei seed via GodMode9 (System Save Dump, `sysdata/0001000f/00000000`) → conversione con **SEEDconv** (`github.com/d0k3/SEEDconv`) → posizionamento di `seeddb.bin` in `0:/gm9/support/`
- **Nota**: durante il lancio del gioco per generare il seed, comparso un errore Nintendo ufficiale "The SD Card couldn't be recognized" - errore documentato come noto anche su console stock per X/Y e OR/AS (controllo SD particolarmente rigido lato gioco), non necessariamente legato al CFW. Risolto con spegnimento completo, rimozione/pulizia contatti/reinserimento SD.
- Esito: dump completato con successo

### 2026-08-23 - Backup salvataggi via Checkpoint
- Homebrew **Checkpoint v5.0.0** utilizzato per esportare backup del salvataggio di Pokémon Omega Ruby
- Backup multipli creati e verificati (es. `20260821-backsic`, `20260821-testROM`), visibili nell'interfaccia con dimensione (472.0 KB ciascuno)
- **Significato tecnico**: Checkpoint esporta il salvataggio in un formato portabile, salvato in `/3ds/Checkpoint/saves/` sulla SD - indipendente dalla struttura dati privata del sistema (`/Nintendo 3DS/[ID0]/[ID1]/data/`), quindi recuperabile anche in caso di problemi al sistema o cambio SD

### 2026-08-23 - Installazione diretta CIA da GodMode9
- Verificata capacità di GodMode9 di installare direttamente file `.cia` (generati o disponibili sulla SD) senza passare da FBI
- **Nota tecnica sulla gestione file**: una volta installato un gioco come CIA, il sistema crea una copia indipendente cifrata in `/Nintendo 3DS/[ID0]/[ID1]/title/00040000/[titleID]/content/`. Il file sorgente `.3ds` (dump originale della cartuccia) non viene più referenziato dal sistema dopo l'installazione - può essere rimosso dalla SD in sicurezza, **a condizione di conservarne una copia sul PC** come backup sorgente (in caso di necessità di reinstallazione futura, es. SD danneggiata o cambio SD, altrimenti richiederebbe un nuovo dump dalla cartuccia fisica)
- I salvataggi di gioco restano **separati** sia dal file `.3ds` sorgente sia dal file CIA installato: vivono in `/Nintendo 3DS/[ID0]/[ID1]/data/[SaveID]/`, gestiti dal sistema al primo avvio del titolo installato

## Nota di perimetro
Su richiesta specifica, questa documentazione **non copre** l'installazione di Pokémon Bank/Transporter (limite di perimetro, vedi §2 dell'handoff) né la configurazione di Azahar (rimandata a data da destinarsi, l'utente preferisce portare con sé i file `.3ds`).

## Stato
- [x] GodMode9 verificato/installato
- [x] Prima cartuccia 3DS dumpata (titolo: Pokémon Omega Ruby - richiesto seeddb.bin per seed encryption)
- [ ] Prima cartuccia DS dumpata
- [x] File trasferiti dalla SD al PC (parziale - verificare completamento backup)
- [x] Backup salvataggio via Checkpoint (Pokémon Omega Ruby)
- [x] Installazione diretta CIA da GodMode9 verificata funzionante
