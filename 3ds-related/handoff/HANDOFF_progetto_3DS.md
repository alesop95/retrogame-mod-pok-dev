# HANDOFF — Progetto Modding Nintendo 3DS (CFW + Dump Cartucce Originali)

> Documento di passaggio completo, pensato per essere letto/consultato in una sessione Claude Code. Riassume tutto ciò che è stato fatto, perché, con quali strumenti, e cosa resta da fare. Nessun dettaglio tecnico è stato omesso rispetto alla conversazione originale.

---

## 1. Obiettivo del progetto

Modding legittimo di un **Nintendo Old 3DS XL** di proprietà dell'utente, per:
1. Installare un Custom Firmware (CFW) che sblocchi homebrew
2. Dumpare (fare backup digitali) di cartucce fisiche **possedute** (3DS e DS)
3. Giocare a quei backup direttamente sulla console (via installazione CIA) e/o su emulatore PC (Azahar — non ancora iniziato)
4. Obiettivo collaterale iniziale: valutare un percorso per portare Pokémon di vecchie generazioni su Pokémon Home (vedi §7 — risultato: **non praticabile** nella maggior parte dei casi)

## 2. Perimetro etico/legale del progetto (vincolante)

Stabilito fin dall'inizio e rispettato per tutta la conversazione:
- ✅ **Dentro perimetro**: dump di cartucce fisiche possedute dall'utente, CFW sulla propria console, emulazione locale dei propri dump, backup/trasferimento dei propri salvataggi
- ❌ **Fuori perimetro**: ROM/software scaricati da fonti terze non autorizzate, condivisione di link a materiale piratato, installazione di software Nintendo protetto da copyright ottenuto senza licenza legittima

**Limite dichiarato**: l'assistenza tecnica di questo progetto non copre Pokémon Bank e Pokémon Transporter su questa console, né alcun file `.cia` di provenienza non chiarita: nessuna guida, nessun troubleshooting, nessuna documentazione. Il limite vale anche per le sessioni future e non va riaperto implicitamente. La circostanza che lo ha originato è personale e sta fuori dal version control, in `_notes/perimetro-bank-transporter.md`.

## 3. Hardware identificato

| Parametro | Valore |
|---|---|
| Modello | Nintendo **Old 3DS XL** (rosso), retro con dicitura "NINTENDO 3DS XL" (senza "New") |
| Identificazione modello | 2 soli tasti dorsali (L/R), nessun C-Stick, nessun sensore NFC integrato — a differenza dei modelli "New" |
| Seriale | Prefisso **SEH** (famiglia Old 3DS XL, distribuzione Europa — nota: SEH è XL, i 2DS EU userebbero AXH) |
| Firmware alla partenza | **11.17.0-50E** (Europa) |
| SD utilizzata | 32GB (29,8GB reali), formattata **FAT32**, unità di allocazione 32KB |

---

## 4. STEP 02 — Installazione CFW (boot9strap + Luma3DS) — ✅ COMPLETATO

**Metodo usato**: MSET9 (di zoogie, Aven, DannyAAM, thepikachugamer), unico exploit software funzionante per Old 3DS/2DS su firmware 11.8.0–11.17.0 (BannerBomb3 risulta patchato su questa versione).

**Fonti ufficiali**:
- Selettore modello/firmware: `https://3ds.hacks.guide/get-started.html`
- Guida metodo (CLI/PC): `https://3ds.hacks.guide/installing-boot9strap-(mset9-cli).html`
- Finalizzazione: `https://3ds.hacks.guide/finalizing-setup.html`
- Repository MSET9: `https://github.com/hacks-guide/MSET9/releases/latest`

### 4.1 Perché MSET9 nello specifico
Sfrutta un difetto nel modo in cui System Settings interpreta il nome di una cartella **ID1** (identificativo legato al profilo/Mii della console) presente sulla SD, dentro la struttura `Nintendo 3DS/[ID0]/[ID1]/`. Un nome di cartella appositamente malformato manda in confusione il parser di System Settings quando si accede a Data Management → Extra Data, ottenendo l'esecuzione di codice arbitrario a livello ARM9. Da lì si installa **boot9strap** (bootloader di basso livello, "sighax"), che a sua volta carica **Luma3DS** (il CFW vero e proprio) a ogni accensione.

### 4.2 Prerequisiti software installati
- **Python** installato da fonte ufficiale `python.org` (**mai** dal Microsoft Store — versione sandboxata incompatibile con lo script)
  - Nota tecnica: python.org è passato al nuovo **Python Install Manager** (sostituisce il vecchio installer `.exe` con checkbox "Add to PATH"). Il manager si autoregistra nel PATH sia come comando `py` che come alias `python`.
  - Versione runtime installata: **Python 3.14.7**
  - Verificato con `py -V` e `python -V` da Prompt dei comandi Windows — entrambi funzionanti
- **Pacchetto MSET9-v2.1** scaricato ed estratto in `C:\Users\alesop95\Desktop\MSET9-v2.1`
  - Contenuto: `mset9.py` (script principale), `MSET9-Windows.bat` (wrapper), cartelle `boot9strap/` e `config/`, `boot.firm`/`boot.3dsx` (componenti Luma3DS), `SafeB9S.bin` (installer CFW lato console), `b9`, `_INSTRUCTIONS`

### 4.3 Preparazione SD
- **Problema riscontrato**: lettore SD del PC fisso non rilevava inizialmente la card (testate 2 SD diverse) → diagnosticato/risolto tramite Gestione dispositivi e Gestione disco Windows (`diskmgmt.msc`)
- **Scelta capacità 32GB** invece di 4GB: necessari per pacchetto MSET9+boot9strap+Luma3DS (~1.5GB) + NAND backup di sicurezza (~1.3GB) + margine futuro per salvataggi/homebrew
- **Formattazione**: FAT32 (non exFAT — è lo standard nativo supportato da Luma3DS/boot9strap per SD ≤32GB), allocazione 32KB, formattazione veloce
- Contenuto pacchetto MSET9 copiato **alla radice della SD** (i percorsi relativi dello script partono dalla root, non da sottocartelle)

### 4.4 Esecuzione — Sezione I (creazione ID1 modificato)
- **Imprevisto**: primo lancio fallito con `Error 01: Couldn't find Nintendo 3DS folder!` — causa: SD formattata da zero sul PC non conteneva ancora la cartella `Nintendo 3DS` (creata solo dalla console alla prima lettura, contiene l'ID1 reale legato al profilo). **Risolto**: SD inserita nel 3DS, accensione/spegnimento una volta, poi ripetuto lo script dal PC.
- Selezione nello script: **opzione 1 — "Old 3DS/2DS, 11.8.0 to 11.17.0"** (coerente col hardware)
- Sequenza: menu `1` (Create MSET9 ID1) → disclaimer accettato (`1` di conferma) → `[OK] Created hacked ID1.`
- Passaggi su console: apertura **Mii Maker** (attesa schermata benvenuto) → System Settings → Data Management → Nintendo 3DS → Software → **Reset** (non cancella dati, resetta solo il database titoli)
- Verifica stato (menu `2` — Check MSET9 status): `Current MSET9 state: Ready`, con HOME menu extdata / Mii Maker extdata / Title database tutti `OK`

### 4.5 Esecuzione — Sezione II (trigger) + Sezione III (installazione boot9strap)
Sequenza eseguita **senza deviazioni** (fondamentale per non corrompere lo stato):
1. Accensione con System Settings selezionata nella Home
2. Apertura System Settings → Data Management → Nintendo 3DS → Extra Data
3. SD estratta **a console ancora accesa**, senza toccare altro
4. SD nel PC → menu `3` (Inject trigger file) → `MSET9 successfully injected!`
5. SD reinserita nella console senza toccare nulla
6. Console avviata in **SafeB9SInstaller v0.0.7**: "All input files verified", Crypto Status "all checks passed", Secret Sector "not required"
7. Combinazione tasti d'installazione inserita (Sinistra, Giù, Destra, Su, A) → **"SigHaxed FIRM install success!"**, Backup Status "backed up & verified", Install Status "install success!"
8. Riavvio → schermata **Luma3DS v13.4 configuration** mostrata correttamente, opzioni lasciate a default, Start per salvare/uscire

### 4.6 Esecuzione — Sezione IV (rimozione MSET9) + verifica finale
- Guida "Finalizing Setup" completata: rimozione trigger file (menu `4`) + rimozione completa MSET9 dalla SD (menu `5`) → ripristino profilo/ID1 originale
- **Verifica di successo definitiva**: schermata di avvio mostra **"Booted from SD via B9S"** — conferma che boot9strap + Luma3DS sono operativi a ogni accensione

### 4.7 Esito
✅ **CFW installato con successo.** Sblocca Step 03 (dump cartucce via GodMode9) e Step 06 del flusso generale (Checkpoint per import/export salvataggi).

---

## 5. STEP 03 — Dump cartucce fisiche (3DS/DS) via GodMode9 — 🔶 IN CORSO

### 5.1 Cos'è GodMode9 e perché si usa
File manager a basso livello che gira come "payload" caricato direttamente da Luma3DS, **prima** del sistema operativo normale del 3DS. Ha accesso hardware diretto al controller del carrello cartucce, permettendo di leggere il contenuto grezzo di una cartuccia fisica bit per bit e salvarlo come file `.3ds` (per cartucce 3DS, formato NCSD) o `.nds` (per cartucce DS, non cifrato).

**Accesso**: spegnimento completo → tenere **Start**, premere anche **Power**, rilasciare entrambi. Se non appare l'interfaccia GodMode9 né un chainloader menu, va installato separatamente (non è stato necessario in questo caso — risultava già presente, verosimilmente incluso nel payload package di MSET9/boot9strap).

### 5.2 Procedura dump cartuccia 3DS
1. Cartuccia inserita → boot GodMode9
2. `[C:] GAMECART` → file `<TitleID>_<version>.trim.3ds`
3. Selezione → **NCSD image options → Decrypt file (0:/gm9/out)**
   - Nota: la versione **cifrata** è identica al contenuto reale della cartuccia; la versione **decrittata** è quella necessaria sia per l'uso con emulatori (Azahar) sia come base per un'eventuale conversione CIA
4. Output in `/gm9/out/` sulla SD

### 5.3 Procedura dump cartuccia DS
1. Cartuccia DS nello stesso slot (retrocompatibilità nativa)
2. `[C:]` → file `<TitleID>.nds` → **Copy to 0:/gm9/out**
3. Nessuna decrittazione necessaria (i giochi DS non sono cifrati)

### 5.4 Troubleshooting risolto: "Decryption failed" su Pokémon Omega Ruby

**Causa**: Omega Ruby (e altri titoli 2014+, incluso Pokémon Y e Pokémon Moon dumpati successivamente) usano la **"seed encryption"**, introdotta da Nintendo a fine 2014 per titoli con funzionalità online. GodMode9 non ha di default il file `seeddb.bin` necessario per decifrare questa categoria di titoli.

**Procedura di risoluzione applicata**:
1. Verifica/attivazione connessione WiFi su System Settings
2. Avvio del gioco fisico **con internet attivo**, permanenza sulla schermata titolo/menu per permettere alla console di contattare i server Nintendo e ricevere/salvare il seed univoco per quella cartuccia
   - **Effetto collaterale riscontrato**: durante questo passaggio è comparso l'errore ufficiale Nintendo **"The SD Card couldn't be recognized. Please end the game and start again."** — documentato come errore noto anche su console **stock non moddate** per la serie Pokémon X/Y e OR/AS (controllo SD particolarmente rigido lato gioco, non causato dal CFW). **Risolto** con spegnimento completo, pulizia/verifica contatti SD, reinserimento con console spenta, riaccensione, verifica preventiva in System Settings → Data Management che la SD risultasse riconosciuta a livello di sistema.
3. Boot in GodMode9 → **System Save Dump...** → dump del file di sistema `sysdata/0001000f/00000000` (contiene i seed noti alla console)
4. Sul PC: conversione con **SEEDconv** (`https://github.com/d0k3/SEEDconv/releases`) → trascinamento del file dumpato sull'eseguibile → generazione automatica di `seeddb.bin`
5. `seeddb.bin` copiato in **`0:/gm9/support/`** sulla SD
6. Ripetuta la decrittazione → completata con successo

Questa stessa causa/soluzione si applica retroattivamente a **Pokémon Y** e **Pokémon Moon** (entrambi titoli post-2014, dumpati con successo dall'utente successivamente, presumibilmente riusando lo stesso `seeddb.bin` già generato — il file è cumulativo, contiene i seed di tutti i titoli online giocati almeno una volta con internet attivo).

### 5.5 Installazione diretta CIA da GodMode9 (senza FBI)
Confermato che GodMode9 può installare direttamente file `.cia` presenti sulla SD, rendendo **FBI opzionale** per il flusso base (dump → installazione). FBI resterebbe utile solo per gestione più avanzata (disinstallazioni rapide senza reboot, installazioni da rete/QR, gestione elenco titoli) ma non è necessario per il workflow attuale.

**Comportamento tecnico dopo installazione CIA**:
- Il sistema crea una copia indipendente e cifrata in `/Nintendo 3DS/[ID0]/[ID1]/title/00040000/[titleID]/content/`
- Il file `.3ds`/`.nds` sorgente (il dump originale) **non viene più referenziato** dal sistema una volta installato → può essere cancellato dalla SD in sicurezza, **a patto di averne prima salvato una copia sul PC** (unico modo per reinstallare in futuro senza ridumpare fisicamente la cartuccia, es. in caso di SD danneggiata o sostituita)
- Ogni cartella titolo sotto `title/00040000/` contiene sempre una sottocartella `content/` (dati di gioco); **solo se il titolo è stato avviato almeno una volta** compare anche una sottocartella `data/` — è lì che vive il salvataggio effettivo per un titolo installato come CIA

### 5.6 Chiarimento importante: dove vive davvero un salvataggio, e differenza con Checkpoint
Emerso come punto di confusione dell'utente, chiarito come segue:

| Scenario di gioco | Dove vive il salvataggio "vivo" |
|---|---|
| Si gioca dalla **cartuccia fisica** inserita (anche con CFW attivo) | Su un **chip di memoria dentro la cartuccia stessa** — mai sulla SD |
| Si gioca dalla **versione installata come CIA** (convertita dal dump) | In `/Nintendo 3DS/[ID0]/[ID1]/title/00040000/[titleID]/data/` sulla SD — creato al primo avvio del titolo installato |

**Checkpoint è un livello ulteriore, separato da entrambi**: esporta uno snapshot/backup portabile in `/3ds/Checkpoint/saves/[nome gioco]/` sulla SD. Non è il salvataggio "live" letto/scritto dal gioco durante il gameplay — è una copia di sicurezza indipendente, utile per backup/restore/portabilità tra installazioni diverse, ma va aggiornata manualmente (nuovo "Backup" da Checkpoint) per restare sincronizzata col progresso reale.

**Come identificare a quale titolo corrisponde una cartella ID esadecimale** (es. `0bafe000`, `0011c400`, `000c9b00` — quelle con sottocartella `data/`, cioè titoli avviati almeno una volta): navigare dentro quella cartella da **GodMode9** (mostra il nome reale del titolo via ExHeader alla selezione) oppure consultare **System Settings → Data Management → Nintendo 3DS → Software**, che elenca tutti i titoli installati per nome — più affidabile che dedurre dall'ID esadecimale.

### 5.7 Log cartucce dumpate finora
| Titolo | Piattaforma | Stato dump | Note |
|---|---|---|---|
| Pokémon Omega Ruby | 3DS | ✅ Completato | Richiesto seeddb.bin (seed encryption) |
| Pokémon Y | 3DS | ✅ Completato | Stessa categoria seed encryption di ORAS |
| Pokémon Moon | 3DS | ✅ Completato | Stessa categoria seed encryption di ORAS |
| Pokémon Diamante | DS | ⬜ Da fare | Nessuna cifratura prevista, dump diretto |
| Pokémon Perla | DS | ⬜ Da fare | Nessuna cifratura prevista, dump diretto |
| Pokémon Platino | DS | ⬜ Da fare | Nessuna cifratura prevista, dump diretto |
| Pokémon Nera 2 | DS | ⬜ Da fare | Nessuna cifratura prevista, dump diretto |
| Pokémon SoulSilver | DS | ⬜ Da fare | Nessuna cifratura prevista, dump diretto |

### 5.8 Nota di perimetro esplicita
Su richiesta specifica dell'utente, la documentazione tecnica **non copre**:
- Installazione/uso di Pokémon Bank e Pokémon Transporter su questa console (limite di perimetro — vedi §2 e §7)
- Configurazione di **Azahar** (emulatore PC) — rimandata volutamente, l'utente preferisce per ora portare con sé i file `.3ds` fisicamente via SD/console

---

## 6. Homebrew installati/verificati sulla console
- **Luma3DS v13.4** — CFW principale (bootloader + patch runtime)
- **GodMode9** — file manager di basso livello per dump/gestione file di sistema, presente come payload
- **Checkpoint v5.0.0** — backup/restore salvataggi (confermato funzionante su Pokémon Omega Ruby, backup multipli creati con nomi `20260821-backsic`, `20260821-testROM`, ciascuno 472.0 KB)
- **SafeB9SInstaller v0.0.7** — usato solo durante l'installazione iniziale del CFW (Step 02), non serve più dopo
- **SEEDconv** (tool lato PC, non su console) — usato per generare `seeddb.bin` dal dump del system save dei seed

---

## 7. Percorso Pokémon Bank/Home — analisi svolta (riferimento: `flusso-3ds.html` e `Notes.txt` del progetto)

Ricostruito dai file di progetto (`flusso-3ds.html`, `Notes.txt`) e confermato nella conversazione:

- **Prerequisito assoluto per Bank/Transporter**: NNID (Nintendo Network ID) creato **prima** della chiusura eShop (2023), con quei titoli già presenti nella cronologia acquisti (anche se scaricati gratuitamente a suo tempo)
- **Conseguenza generale**: senza quel prerequisito non esiste cronologia da cui reinstallare, quindi **Bank/Transporter non sono ottenibili oggi per la prima volta in nessun modo legittimo**, indipendentemente da CFW/modding (il blocco è lato server/infrastruttura Nintendo, non aggirabile tecnicamente in modo legittimo)
- **Conseguenza pratica per l'obiettivo "Pokémon vecchi su Home"**:
  - Giochi **Gen 1–7** (cartucce DS/GBA fino a X/Y, OR/AS, Sun/Moon, US/UM): il ponte verso Home tramite Bank resta **chiuso** per questo progetto, e lo sarà definitivamente per chiunque dal **25–26 febbraio 2027** (data di chiusura definitiva del servizio Bank, fonti: VGC, Nintendo Life, TheGamer — vedi sezione Fonti di `flusso-3ds.html`)
  - Giochi **Gen 8+** (Sword/Shield, BD/SP, Legends Arceus, Scarlet/Violet, e da **ottobre 2026** anche FireRed/LeafGreen su Switch): si collegano a Pokémon Home **direttamente**, senza passare da Bank, tramite un **Nintendo Account moderno** (sistema distinto dall'NNID, creabile gratuitamente oggi senza alcun ostacolo)
- **Fuori perimetro in ogni caso**: ottenere Bank/Transporter da uno shop alternativo tramite modding equivarrebbe a distribuzione non autorizzata di software Nintendo protetto da copyright, fuori dal perimetro stabilito al §2, e resta escluso a prescindere da chi lo chieda

---

## 8. Struttura riferimenti/fonti usate in tutta la conversazione

| Argomento | Fonte |
|---|---|
| Guida CFW generale | `https://3ds.hacks.guide/` |
| Metodo MSET9 (CLI/PC) | `https://3ds.hacks.guide/installing-boot9strap-(mset9-cli).html` |
| Repository MSET9 | `https://github.com/hacks-guide/MSET9/releases/latest` |
| Finalizzazione setup | `https://3ds.hacks.guide/finalizing-setup.html` |
| Uso GodMode9 | `https://3ds.hacks.guide/godmode9-usage.html` |
| SEEDconv | `https://github.com/d0k3/SEEDconv/releases` |
| Python (installer ufficiale) | `https://www.python.org/downloads/` |
| Azahar (emulatore, non ancora usato) | `https://azahar-emu.org/` |
| Chiusura Pokémon Bank (annuncio) | VGC, Nintendo Life, TheGamer (vedi `flusso-3ds.html`, sezione Fonti) |
| Errore ufficiale "SD Card couldn't be recognized" | Nintendo Support (en-americas-support.nintendo.com) |

---

## 9. Prossimi passi (TODO aperti)

1. **Dump cartucce DS rimanenti**: Diamante, Perla, Platino, Nera 2, SoulSilver (procedura §5.3, nessuna decrittazione attesa)
2. **Trasferimento sistematico** di tutti i file `.3ds`/`.nds` dumpati da `/gm9/out/` al PC (backup sorgente, cartella consigliata: `Documenti\3DS-Backups`)
3. **Installazione CIA** dei titoli dumpati non ancora installati sul sistema (se desiderato)
4. **Eventuale configurazione Azahar** su PC (rimandata, non ancora iniziata — Step 04 del flusso generale)
5. **Eventuale pulizia PKHeX** se in futuro si vogliono importare salvataggi di terze parti con Checkpoint (avvertenza già data: i save "illegali" scaricati online sono la causa principale di ban se poi usati online o depositati su Bank)

---

## 10. Allegati disponibili in questa sessione
- `step02_cfw_mset9.md` — documentazione tecnica completa e granulare dello Step 02 (CFW), con log di ogni sotto-passaggio eseguito
- `step03_dump_cartucce.md` — documentazione tecnica completa e granulare dello Step 03 (dump cartucce), con log di ogni sotto-passaggio eseguito e troubleshooting
- `flusso-3ds.html` — mappa visuale originale del flusso complessivo (file di progetto dell'utente, riferimento concettuale usato per orientare l'intera conversazione)
- `Notes.txt` — appunti originali dell'utente sull'obiettivo Pokémon Home (file di progetto)
