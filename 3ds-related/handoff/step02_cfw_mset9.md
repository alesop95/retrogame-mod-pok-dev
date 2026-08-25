# Step 02 — Installazione CFW (Custom Firmware)

## Console identificata
| Parametro | Valore |
|---|---|
| Modello | Nintendo **Old 3DS XL** (rosso) |
| Riconoscimento | 2 soli tasti dorsali (L/R), nessun C-Stick, nessun NFC integrato |
| Firmware | **11.17.0-50E** (regione Europa) |
| Metodo richiesto | **MSET9** |

## Perché MSET9 e non altri metodi
La versione 11.17 ha patchato BannerBomb3, l'exploit userland precedentemente usato su Old 3DS. Al momento MSET9 (di zoogie) è l'unico metodo software noto che funziona su Old 3DS/2DS in questa versione firmware. Sfrutta una falla nel modo in cui System Settings interpreta il nome di una cartella ID1 sulla SD, per ottenere l'esecuzione di codice arbitrario e installare boot9strap.

Fonte ufficiale (selettore interattivo per modello+firmware): `https://3ds.hacks.guide/get-started.html`

Pagina specifica del metodo: `https://3ds.hacks.guide/installing-boot9strap-(mset9).html`

## Requisiti hardware/software
- Un dispositivo per leggere/scrivere la SD del 3DS: PC Windows/Mac/Linux **oppure** telefono/tablet Android (Android 6.0+) **oppure** iPhone/iPad
- Se via PC: verrà eseguito uno script Python (`mset9.py`)
- Se via Android: app dedicata (metodo "MSET9 Play Store")
- MicroSD ≥ 1.5 GB liberi (per il NAND backup finale servono almeno 1.3 GB)
- Adattatore/lettore per la SD del 3DS

## Nota importante
Durante l'esecuzione, i dati utente (giochi installati, temi, salvataggi) spariscono temporaneamente dalla home del 3DS — è previsto dal processo, e tornano visibili al termine della procedura, a patto di seguire correttamente anche la fase di rimozione dell'exploit alla fine (altrimenti si rischiano crash di System Settings/FBI).

## Flusso operativo (alto livello)
1. Verifica preliminare che non sia già presente un CFW (Sezione I della guida ufficiale: accensione tenendo premuto Select)
2. Formattazione/preparazione SD se necessario
3. Download pacchetto MSET9 dalla pagina ufficiale, estrazione alla radice della SD
4. Esecuzione della sequenza guidata (creazione profilo HOME Menu temporaneo → trigger dell'exploit → ottenimento controllo ARM9)
5. Installazione di **boot9strap** + **Luma3DS**
6. Rimozione dell'exploit temporaneo e ripristino profilo originale (fondamentale, non va saltato)
7. Riavvio con SD inserita → verifica bootup in Luma3DS (schermo con opzioni al posto del normale avvio)

## Collegamento con gli step successivi (da flusso-3ds.html)
- Abilita **Step 03** (Godmode9 → dump cartucce fisiche possedute)
- Abilita **Step 06** (Checkpoint → import save su console)

## Dispositivo di supporto: PC Windows

Fonte: `https://3ds.hacks.guide/installing-boot9strap-(mset9-cli).html`

### Prerequisiti software
- **Python 3.x da python.org** — attenzione: la versione dal Microsoft Store **non funziona** per questa procedura, va scaricata da `https://www.python.org/downloads/`
- Ultima release di MSET9 (file `.zip`): `https://github.com/hacks-guide/MSET9/releases/latest`
- Un lettore SD collegato al PC (non un telefono Android usato come tramite: incompatibile per limiti del protocollo MTP)

### Sezione I — Preparazione (crea profilo temporaneo)
1. SD nel PC → estrarre tutto il contenuto dello zip MSET9 nella radice della SD (sovrascrivere se richiesto)
2. Eseguire lo script: doppio click su `MSET9-Windows.bat`
3. Digitare il numero corrispondente a modello (**Old 3DS/2DS**) e versione (**11.17.0-50E**), Invio
4. Digitare `1` + Invio → avvia creazione dell'ID1 modificato
5. Leggere il disclaimer, digitare `1` + Invio per accettare
6. Attendere messaggio "Created hacked ID1." → Invio per chiudere lo script
   - **Normale**: i dati/app installate spariranno temporaneamente dalla Home
7. SD nella console → accensione
8. Aprire **Mii Maker**, attendere la schermata di benvenuto, uscire e tornare alla Home
9. **System Settings → Data Management → Nintendo 3DS → Software → Reset** (non cancella nulla, resetta solo il database titoli)
10. Spegnere la console
11. SD di nuovo nel PC → rilanciare `MSET9-Windows.bat`
12. Selezionare di nuovo modello+versione → deve comparire stato **"Ready"**
    - Se compare "Not ready": digitare `2` per la diagnosi e seguire le indicazioni prima di ripetere
13. Digitare `0` + Invio per chiudere → SD nella console

### Sezione II — Trigger dell'exploit (attenzione massima)
⚠️ Sequenza da seguire **esattamente**, senza deviazioni:
1. Accendere la console con **System Settings selezionata** nella Home (usare la croce direzionale per evidenziarla, eventualmente spegnere/riaccendere)
2. Premere **A** per aprire System Settings
3. Navigare a **Data Management → Nintendo 3DS → Extra Data**
4. **Non toccare nulla** da qui in poi
5. Con la console ancora accesa e **senza toccare schermo/tasti**, estrarre la SD (il menu segnalerà "nessuna SD" — è previsto)
6. SD nel PC → rilanciare lo script, riselezionare modello+versione
7. Digitare `3` + Invio → deve apparire **"MSET9 successfully injected!"**
8. Invio per chiudere lo script
9. Reinserire la SD nella console **senza toccare nulla**
10. Se l'exploit riesce, la console boota in **SafeB9SInstaller**
    - Schermo rosso o blocco prolungato (>10s) → interrompere e consultare troubleshooting: `https://3ds.hacks.guide/troubleshooting-mset9.html`

### Sezione III — Installazione boot9strap
1. Seguire la combinazione di tasti mostrata sullo schermo superiore quando richiesto
   - Se lo schermo superiore è vuoto ma il basso mostra "Crypto Status - all checks passed": inserire alla cieca la combinazione **Sinistra, Giù, Destra, Su, A**
2. Al completamento (7 righe verdi sullo schermo inferiore), premere **A** per riavviare
3. La console dovrebbe avviarsi nel menu di configurazione **Luma3DS** → lasciare tutte le opzioni sui valori di default
4. Premere **Start** per salvare e riavviare

### Sezione IV — Rimozione di MSET9 (obbligatoria, non saltare)
1. Spegnere la console, SD nel PC
2. Rilanciare lo script, riselezionare modello+versione → stato atteso: **"Injected"**
3. Digitare `4` + Invio → "Removed trigger file."
4. Digitare `5` + Invio → "Successfully removed MSET9!"
5. Invio per chiudere → SD nella console

Da qui la console boota di default in Luma3DS (aspetto identico alla Home normale — se si arriva alla Home, il CFW è attivo).

## Log di esecuzione — Prerequisiti (PC Windows)

### 2026-08-21 — Installazione Python
- Scaricato l'installer ufficiale da python.org: **Python Install Manager** (nuovo sistema che ha sostituito il classico installer `.exe` con checkbox "Add to PATH")
- Editore verificato: Python Software Foundation, origine www.python.org (avviso SmartScreen di Windows è standard per eseguibili scaricati, non un allarme malware)
- Eseguito `py -V` da Prompt dei comandi:
  - Il launcher si è auto-aggiornato a versione 26.3
  - Ha scaricato ed estratto automaticamente il runtime **Python 3.14.7** (firma del pacchetto verificata da python.org)
  - Output finale confermato: `Python 3.14.7`
- **Significato tecnico**: a differenza del vecchio installer, il Python Install Manager non richiede la spunta manuale "Add to PATH" — registra da sé il launcher `py` (e generalmente anche l'alias `python`) nel PATH di sistema, così Windows può trovare l'interprete da qualunque cartella
- **Perché serve nel nostro contesto**: lo script `mset9.py` (che useremo per generare l'ID1 modificato sulla SD e per pilotare il trigger dell'exploit) deve essere eseguibile da riga di comando/da `.bat` — senza un interprete Python funzionante e raggiungibile via PATH, il file batch `MSET9-Windows.bat` fallirebbe silenziosamente o con errore "python non riconosciuto"
- Verifica compatibilità comando `python` (oltre a `py`): **superata** — `python -V` risponde `Python 3.14.7`, identico a `py -V`. Entrambi gli alias sono registrati nel PATH, quindi `MSET9-Windows.bat` (che internamente richiama l'interprete) funzionerà indipendentemente da quale dei due comandi usi.

### 2026-08-21 — Download pacchetto MSET9
- Scaricato da `https://github.com/hacks-guide/MSET9/releases/latest` (release MSET9-v2.1)
- Estratto in: `C:\Users\alesop95\Desktop\MSET9-v2.1`
- Contenuto verificato (10 elementi, corrispondente alle attese):
  - `mset9.py` — lo script Python principale, motore dell'exploit
  - `MSET9-Windows.bat` — wrapper batch che richiama lo script con l'interprete corretto
  - Cartella `boot9strap/` — file del custom firmware da installare sulla console
  - Cartella `config/` — file di configurazione letti dallo script
  - `boot.firm` / `boot.3dsx` — componenti di avvio di Luma3DS (verranno scritti sulla SD)
  - `SafeB9S.bin` — l'installer di boot9strap eseguito lato console durante la Sezione III
  - `b9`, `_INSTRUCTIONS` — file di supporto/istruzioni incluse nel pacchetto
- **Significato tecnico**: questi file, una volta copiati alla radice della SD (prossimo step), costituiscono sia il "trigger" che lo script Python scriverà nell'ID1 modificato, sia il payload (boot9strap) che la console installerà una volta ottenuta l'esecuzione di codice arbitrario tramite la falla di System Settings

### 2026-08-21 — Preparazione fisica della SD
- **Problema iniziale**: lettore SD del PC fisso non rilevava la card (testate 2 SD diverse) — diagnosticato tramite Gestione dispositivi/Gestione disco (`diskmgmt.msc`), poi risolto individuando il percorso corretto
- **Scelta capacità**: SD da **32GB** (29,8GB reali) invece di una da 4GB — necessari per: pacchetto MSET9 + boot9strap + Luma3DS (~1.5GB) + NAND backup di sicurezza da eseguire prima di modificare la console (~1.3GB) + margine per salvataggi/homebrew futuri
- **Formattazione eseguita**: FAT32, unità di allocazione 32KB, formattazione veloce
  - *Perché FAT32 e non exFAT*: file system nativamente supportato da Luma3DS/boot9strap senza configurazioni aggiuntive, standard de facto nella scena homebrew 3DS per SD fino a 32GB
  - Contenuto precedente della SD azzerato dalla formattazione (confermato non necessario)
- **Copia file MSET9**: tutto il contenuto di `MSET9-v2.1` (10 elementi: `mset9.py`, `MSET9-Windows.bat`, cartelle `boot9strap/` e `config/`, `boot.firm`, `boot.3dsx`, `SafeB9S.bin`, ecc.) copiato **alla radice della SD**, non in sottocartelle
  - *Perché alla radice*: lo script gira con percorsi relativi che partono dalla root dell'unità, necessario per scrivere correttamente la cartella ID1 modificata dove System Settings la cercherà

### 2026-08-21 — Esecuzione Sezione I (creazione ID1 modificato)
- **Imprevisto risolto**: primo lancio fallito con "Error 01: Couldn't find Nintendo 3DS folder" — causa: SD formattata da zero sul PC non conteneva ancora la cartella `Nintendo 3DS`/ID1, generata solo dalla console alla prima lettura. Risolto inserendo la SD nel 3DS, accensione/spegnimento, poi ripetendo lo script dal PC.
- Modello/firmware confermato nello script: **Old 3DS/2DS, 11.8.0 to 11.17.0** (opzione 1) — coerente con Old 3DS XL, firmware 11.17.0-50E
- Sequenza completata: disclaimer accettato, `[OK] Created hacked ID1.`
- Verifica stato (opzione 2 dello script) dopo i passaggi su console (Mii Maker + Data Management reset): `Current MSET9 state: Ready` — HOME menu extdata, Mii Maker extdata, Title database tutti `OK`

### 2026-08-21 — Sezione II (trigger) + Sezione III (installazione boot9strap)
- Sequenza System Settings → Data Management → Nintendo 3DS → Extra Data eseguita senza deviazioni, SD estratta a console accesa, reinserita
- Trigger iniettato da PC (opzione 3 dello script): `MSET9 successfully injected!`
- Console avviata in **SafeB9SInstaller v0.0.7**: crypto status "all checks passed", Secret Sector "not required"
- Combinazione tasti d'installazione inserita → **"SigHaxed FIRM install success!"**, Backup Status "backed up & verified", Install Status "install success!"
- Riavvio → **Luma3DS v13.4 configuration** mostrato correttamente, impostazioni lasciate a default, Start per salvare/uscire

### 2026-08-21 — Sezione IV (rimozione MSET9) + verifica finale
- Guida "Finalizing Setup" (`https://3ds.hacks.guide/finalizing-setup.html`) completata (rimozione trigger + rimozione MSET9 dalla SD, ripristino profilo originale)
- **Verifica di successo**: avvio console mostra a schermo **"Booted from SD via B9S"** — conferma che boot9strap+Luma3DS sono correttamente operativi ad ogni accensione

## Esito Step 02: ✅ COMPLETATO
CFW (boot9strap + Luma3DS v13.4) installato con successo su Old 3DS XL, firmware 11.17.0-50E, tramite metodo MSET9 da PC Windows. Sblocca Step 03 (dump cartucce) e Step 06 (Checkpoint) del flusso generale.

## Stato
- [x] Sezione I completata (verifica assenza CFW)
- [x] Sezione II completata (versione firmware confermata: 11.17.0-50E)
- [x] Metodo scelto: MSET9, dispositivo di supporto: **PC Windows**
- [x] Python 3.x da python.org installato (Python Install Manager → runtime 3.14.7, comandi `py` e `python` entrambi verificati)
- [x] MSET9 scaricato ed estratto sul PC (`C:\Users\alesop95\Desktop\MSET9-v2.1`)
- [x] SD 32GB formattata FAT32 e collegata al PC
- [x] Contenuto MSET9 copiato alla radice della SD
- [x] Sezione I (script — creazione ID1 modificato) completata
- [x] Sezione II (trigger) completata
- [x] boot9strap installato
- [x] Luma3DS avviato con successo — conferma "Booted from SD via B9S"
- [x] Sezione IV (rimozione MSET9) completata
