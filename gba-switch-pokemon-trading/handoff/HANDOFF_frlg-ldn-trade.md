# HANDOFF TECNICO-DIDATTICO
## Progetto: Trading locale wireless (LDN) PC ⇄ Nintendo Switch - Pokémon FireRed/LeafGreen

**Data handoff:** 24 agosto 2026  
**Scopo del documento:** trasferire in modo completo, senza omissioni, tutto il contesto raccolto in questa conversazione, in una forma leggibile e riutilizzabile all'interno di una sessione **Claude Code**. Il documento è organizzato per essere consultato sia come riferimento rapido (indice, comandi, requisiti) sia come materiale didattico (spiegazione dei concetti tecnici sottostanti, senza dare nulla per scontato).

---

## 0. Indice

1. Contesto generale e obiettivo del progetto
2. Fonti raccolte nella chat (materiale grezzo, nessuna omissione)
3. Glossario tecnico (spiegato da zero)
4. Architettura concettuale: come funziona il trading LDN
5. Repository di riferimento: `kinnay/LDN`
6. Repository di riferimento: `tornadus/frlg-ldn-trade`
7. Requisiti hardware e software completi
8. Procedura operativa passo-passo (setup + esecuzione)
9. Comandi Bash raccolti (annotati riga per riga)
10. Strumenti collaterali (PKHeX-Web, GBxCart)
11. Rischi, limiti, cause di crash e troubleshooting
12. Considerazioni legali/etiche
13. Stato del materiale: cosa manca, cosa va verificato in una sessione di lavoro
14. Prompt di ripartenza suggerito per Claude Code

---

## 1. Contesto generale e obiettivo del progetto

Il materiale raccolto in questa chat documenta un **progetto amatoriale/proof-of-concept** che dimostra la possibilità di far comunicare un **computer (Linux)** con una **console Nintendo Switch (o Switch 2)** tramite il protocollo di rete locale wireless proprietario Nintendo chiamato **LDN** ("Local Data Network" / "Local Wireless"), per eseguire uno **scambio (trade) di Pokémon** tra:

- un "emulatore" o simulatore software lato PC (che finge di essere una seconda console), e
- una copia reale del gioco **Pokémon FireRed/LeafGreen (FRLG)** in esecuzione su hardware Switch reale (presumibilmente tramite un port/emulazione della generazione 3 su Switch, dato che FRLG è un titolo Game Boy Advance).

L'obiettivo dichiarato dagli autori del proof-of-concept (vedi sezione 6) è **puramente dimostrativo**: provare che l'interazione è tecnicamente possibile, nella speranza che la comunità costruisca strumenti più completi (es. un GTS non ufficiale, battaglie online) partendo da questa base.

Il documento "Parti descrizione video" presente nel materiale suggerisce che la conversazione originale era finalizzata a **preparare la descrizione di un video YouTube** che documenta/dimostra questa procedura, con tanto di link alle risorse, requisiti hardware elencati per il pubblico, e comandi bash da copiare.

---

## 2. Fonti raccolte nella chat (materiale grezzo, nessuna omissione)

Di seguito il contenuto **integrale** dei quattro file di progetto presenti nel contesto, riportato senza tagli, così da non perdere nulla nell'handoff.

### 2.1 - File: `Video_youtube_principale`
```
https://www.youtube.com/watch?app=desktop&v=Ld2YphF-HVI&t=1s
```
Link al video YouTube principale che presumibilmente mostra la dimostrazione pratica del trade PC→Switch. Non è stato possibile (in questa sessione) estrarne trascrizione o descrizione testuale: è un semplice URL. **Da verificare/recuperare manualmente se serve il contenuto del video stesso** (titolo, descrizione attuale, eventuali timestamp).

### 2.2 - File: `Proof_of_concept_che_è_possibile_farlo__a_data_21082026_`
```
https://github.com/tornadus/frlg-ldn-trade
```
Repository GitHub dell'utente **tornadus**, intitolato *"Proof-of-concept: a computer trading in FRLG with a real Switch/Switch 2 over local wireless (LDN)"*. Contenuto dettagliato riportato in sezione 6.

### 2.3 - File: `Python_package_for_local_wireless_communication_with_a_Nintendo_Switch`
```
https://github.com/kinnay/LDN
```
Repository GitHub dell'utente **kinnay**, libreria Python di basso livello che implementa il protocollo LDN. È la libreria su cui si basa il proof-of-concept di tornadus. Contenuto dettagliato riportato in sezione 5.

### 2.4 - File: `Parti_descrizione_video` (testo integrale)
```
Kinnay's LDN Github: https://github.com/kinnay/LDN

Plesse suport those who have discovered HOW TO TRADE FROM YOUR PC TO YOUR SWITCH!
It's insane that we are this close to being able to TRADE FROM EMULATOR TO SWITCH with ease!

PKHeX for Web: https://pkhex-web.github.io/

Requirements:
Linux with Python 3.12.3+
Compatible Wifi Card *OR* USB Wifi Adapter
Switch or Switch 2 with FRLG
At least 2 .pk3 files
Switch prod.keys

PCIe card used in this video:
RTL8821CE 802.11ac PCIe Wireless Network Adapter

Linux Distro - Mint 22.3: https://linuxmint.com/edition.php?id=326
Rufus Bootable Media Creator: https://rufus.ie/en/

GBxCart Purchase & Software: https://www.gbxcart.com/

BASH COMMANDS:
sudo -E ./venv/bin/python frlgtrade.py --live --verbose --keys .switch/prod.keys -o output.pk3 PARTY1.pk3 PARTY2.pk3

USB Permissions for GBX -
chmod a+x GBX.AppImage
pkexec chmod 0666 /dev/ttyUSB0
QT_QPA_PLATFORM=xcb ./GBX.AppImage

WIFI Card Commands:
pkexec apt update
pkexec apt install iw
sudo systemctl stop NetworkManager

IF CRASH:
sudo killall python3 python python3.12
```
Questo è il file più ricco: contiene bozza testuale per la descrizione del video YouTube, con link, requisiti hardware/software, e tutti i comandi bash necessari per riprodurre la procedura. Nota: il testo originale contiene un refuso ("Plesse suport" invece di "Please support"), riportato qui fedelmente perché parte del materiale originale dell'utente.

---

## 3. Glossario tecnico (spiegato da zero, senza dare nulla per scontato)

| Termine | Spiegazione |
|---|---|
| **LDN (Local Data Network)** | Nome interno del protocollo wireless proprietario usato da Nintendo Switch per il multiplayer locale (es. modalità "wireless locale" nei giochi, comunicazione tra più Switch nella stessa stanza). Non è Wi-Fi Direct standard: è un protocollo custom costruito sopra 802.11, con un proprio schema di autenticazione/associazione. |
| **FRLG** | Abbreviazione di *FireRed/LeafGreen*, la coppia di remake per Game Boy Advance (generazione 3) dei primissimi giochi Pokémon Rosso/Blu/Verde. Nel contesto di questo progetto, "FRLG su Switch" implica che il gioco viene eseguito sulla console Switch (verosimilmente tramite un port/emulatore ufficiale o non ufficiale - il materiale non specifica quale, va verificato). |
| **.pk3 / .ek3** | Formati file che rappresentano un singolo Pokémon salvato della generazione 3 (Ruby/Sapphire/Emerald/FireRed/LeafGreen). `.pk3` è la rappresentazione "decriptata/leggibile" usata da strumenti come PKHeX; `.ek3` è la forma "criptata" così come starebbe nella memoria di gioco. Questi file vengono usati come "merce di scambio" - cioè i Pokémon fittizi che il PC usa per impersonare un secondo giocatore. |
| **prod.keys** | File contenente le chiavi crittografiche di produzione della Switch, necessarie per decriptare/interpretare vari contenuti del sistema (firmware, giochi, salvataggi). Si trova tipicamente in `~/.switch/prod.keys` quando si usano strumenti dell'ecosistema di emulazione/homebrew Switch (es. hactool, Ryujinx, ecc.). **Nota etico-legale:** l'estrazione delle prod.keys richiede accesso proprio a una console Switch modificata (hackerata); la loro distribuzione è vietata perché contengono materiale coperto da copyright Nintendo. |
| **CAP_NET_ADMIN** | Una "capability" del kernel Linux che concede a un processo privilegi di amministrazione della rete (es. mettere una scheda in modalità monitor, iniettare pacchetti raw). È il motivo per cui gli script vanno eseguiti con `sudo`. |
| **Modalità monitor** | Modalità operativa di una scheda Wi-Fi in cui essa può ricevere (e in alcuni casi inviare) frame 802.11 grezzi, non associati a una specifica rete, invece del traffico IP "normale". Necessaria per intercettare/costruire manualmente i frame del protocollo LDN. |
| **Modalità AP (Access Point)** | Modalità in cui la scheda Wi-Fi si comporta da router/hotspot, accettando connessioni da altri dispositivi (in questo caso, dalla Switch). |
| **NetworkManager** | Servizio di sistema su molte distribuzioni Linux (incluso Linux Mint) che gestisce automaticamente le connessioni di rete. Va fermato durante l'uso di LDN perché altrimenti interferisce con la scheda Wi-Fi, che deve essere controllata manualmente e a basso livello dallo script Python. |
| **venv (virtual environment)** | Ambiente Python isolato che permette di installare pacchetti (dipendenze) specifici per un progetto senza interferire con l'installazione di sistema. |
| **pkexec** | Strumento che, come `sudo`, permette di eseguire comandi con privilegi elevati, tipicamente tramite un dialogo grafico di autenticazione (PolicyKit). |
| **GBxCart RW** | Dispositivo hardware di terze parti (GBxCart, di Insride Gadgets / gbxcart.com) usato per leggere/scrivere cartucce Game Boy/GBA/GBC fisiche via USB. Nel contesto di questo progetto sembra essere uno strumento collaterale, forse per dumping/scrittura di salvataggi da cartucce fisiche verso file `.pk3`. |
| **AppImage** | Formato di distribuzione software per Linux che impacchetta un'applicazione e le sue dipendenze in un unico file eseguibile, senza bisogno di installazione. |
| **PKHeX** | Editor di salvataggi Pokémon molto diffuso nella community, che permette di creare/modificare file `.pk3` (e analoghi per altre generazioni). "PKHeX for Web" è una versione eseguita interamente nel browser. |
| **prodkeys / phy (physical wireless device)** | In Linux, ogni scheda Wi-Fi fisica è identificata a basso livello da un identificativo "phy" (es. `phy0`, `phy1`), usato dagli strumenti come `iw` per selezionare quale scheda controllare quando ce n'è più di una nel sistema. |

---

## 4. Architettura concettuale: come funziona il trading LDN

Spiegazione end-to-end del meccanismo, ricostruita dal materiale raccolto (README di `kinnay/LDN` e di `tornadus/frlg-ldn-trade`):

1. **Livello fisico/driver:** il protocollo LDN non è HTTP/TCP-IP "normale": opera direttamente a livello di **frame 802.11** (data link layer). Per questo la libreria `kinnay/LDN` richiede accesso a basso livello alla scheda Wi-Fi (capability `CAP_NET_ADMIN`), non semplice connettività di rete.

2. **Problema architetturale scoperto da kinnay:** per **unirsi** a una rete LDN esistente (fatta da una Switch) è sufficiente una scheda in modalità client normale. Ma per **ospitare** (fare da host/Access Point) una rete LDN compatibile con la Switch, la libreria ha dovuto risolvere un problema non banale:
   - la modalità AP pura non riceve frame broadcast (`ff:ff:ff:ff:ff:ff`), che vengono scartati dal kernel/driver;
   - la modalità IBSS (ad-hoc) non funziona perché la Switch scarta le richieste di associazione in quella modalità;
   - **soluzione adottata:** un'interfaccia in **modalità AP** gestisce i frame di management (probe request, association request, ecc.), mentre una **seconda interfaccia in modalità monitor** (spesso la stessa scheda fisica, due interfacce virtuali) riceve/invia i frame dati, inclusi i broadcast. I frame dati vengono poi decriptati e scritti su un'**interfaccia TAP** virtuale, in modo che Linux li tratti come traffico di rete "normale" per il resto dello stack.

3. **Ruolo del pacchetto `kinnay/LDN`:** fornisce le primitive Python per scansionare reti LDN vicine, unirsi ad esse, oppure ospitarne una propria - cioè l'infrastruttura di trasporto/rete grezza.

4. **Ruolo di `frlgtrade.py` (progetto tornadus):** costruito **sopra** la libreria LDN, implementa la **logica applicativa specifica del gioco FRLG**: simula un secondo giocatore ("EMU") che si connette alla Switch che ha aperto una sessione di trading al "Direct Corner" (l'angolo/stanza di gioco dove nei remake FRLG si effettuano gli scambi wireless). Il PC quindi:
   - carica due file `.pk3` (`PARTY1.pk3`, `PARTY2.pk3`) come "squadra" fittizia del giocatore simulato;
   - negozia la connessione LDN con la Switch reale;
   - gestisce il protocollo di trade lato gioco (che richiede reverse engineering del formato dati usato dal port Switch di FRLG, sfruttando come riferimento la decompilazione **pokefirered** - il progetto di decompilazione completa di FireRed/LeafGreen, incluso il port Switch);
   - riceve il Pokémon scambiato e lo scrive come nuovo file `.pk3` (`output.pk3`).

5. **Nota degli autori sull'uso di IA:** il README di tornadus dichiara esplicitamente che strumenti IA (incluso Claude) sono stati usati intensamente nello sviluppo, ma descrive il processo come guidato passo-passo dall'autore umano piuttosto che "vibe coding" autonomo - l'IA ha soprattutto accelerato il lavoro di reverse engineering.

---

## 5. Repository di riferimento: `kinnay/LDN`

**URL:** https://github.com/kinnay/LDN  
**Licenza:** GPL-3.0  
**Popolarità (al 24/08/2026):** 44 stelle, 6 fork, 4 watcher  
**Linguaggio:** Python 100%

### 5.1 Descrizione
Pacchetto Python per comunicazione wireless locale con una Nintendo Switch: permette di scansionare reti LDN nelle vicinanze, unirsi ad esse, e persino ospitarne di proprie.

### 5.2 Installazione
```bash
pip install ldn
```

### 5.3 Documentazione collegata
- Documentazione del protocollo di comunicazione LDN: repository wiki `kinnay/NintendoClients` (pagina "LDN-Protocol")
- Documentazione di classi/funzioni del pacchetto: hostato su Read the Docs (ldn.readthedocs.io)
- Server Discord della community per supporto

### 5.4 Requisiti dichiarati dagli autori
- Sistema Linux
- Python **3.12 o successivo**
- Hardware wireless capace di ricevere/trasmettere action frame in **modalità monitor**

### 5.5 Istruzioni d'uso essenziali
- Il pacchetto richiede privilegi `CAP_NET_ADMIN`; il modo più semplice per ottenerli è eseguire gli script come root: `sudo -E python3 script.py` (il flag `-E` preserva le variabili d'ambiente dell'utente, incluso il path del venv).
- È necessario fermare il servizio NetworkManager prima dell'uso (`sudo service NetworkManager stop`), perché altrimenti interferisce con la gestione a basso livello della scheda. Conseguenza pratica: **durante l'uso del pacchetto non si ha accesso a Internet** tramite quella scheda (a meno di usare una connessione cablata separata). Per ripristinare: `sudo service NetworkManager start`.

### 5.6 Design/architettura (vedi anche sezione 4)
Il repository descrive esplicitamente il problema del "come ospitare una rete LDN" e la soluzione ibrida AP + monitor + interfaccia TAP, dettagliata sopra.

### 5.7 Troubleshooting
Gli autori segnalano che l'uso di LDN è intrinsecamente complesso e rimandano a una pagina wiki dedicata ai problemi comuni ("Common Issues"), suggerendo di aprire una issue su GitHub se il problema persiste.

---

## 6. Repository di riferimento: `tornadus/frlg-ldn-trade`

**URL:** https://github.com/tornadus/frlg-ldn-trade  
**Licenza:** AGPL-3.0  
**Popolarità (al 24/08/2026):** 0 stelle, 0 fork (repository recente/di nicchia)  
**Linguaggio:** Python 100%  
**Struttura del repo:** cartella `frlgsim/`, più i file `frlgtrade.py`, `requirements.txt`, `README.md`, `LICENSE`, `.gitignore`

### 6.1 Descrizione e finalità
Proof-of-concept che dimostra come un computer possa scambiare Pokémon in FRLG con una Switch/Switch 2 reale via rete wireless locale (LDN). Finalità dichiarata: dimostrare la fattibilità tecnica, nella speranza che la community costruisca strumenti più ambiziosi (GTS non ufficiale, battaglie online).

### 6.2 Demo
Il README include un video dimostrativo (`demonstration.mp4`, ospitato su URL firmato/temporaneo di GitHub, quindi **non riportato qui perché scade e non è un riferimento stabile**). La demo è stata registrata con l'adattatore **ALFA AWUS036ACHM**; gli autori notano che la scheda **RZ616** (interna, M.2) è mediamente la metà più lenta e a volte va in stallo (deadlock) prima di terminare correttamente.

### 6.3 Funzionalità
- Trading end-to-end con un gioco reale in esecuzione su una Switch reale
- Input/output nei formati `.pk3` / `.ek3`

### 6.4 Requisiti dichiarati (versione da README ufficiale del repo - leggermente diversa dai requisiti nel file "Parti descrizione video")
- Linux
- **Python 3.9+** (nota: il file di descrizione video indicava invece 3.12.3+, probabilmente per allinearsi al requisito più stringente della libreria `kinnay/LDN`; in caso di dubbio usare la versione più recente, 3.12+)
- Una scheda Wi-Fi compatibile (vedi tabella sotto)
- Una Switch o Switch 2 con FRLG, portato al punto in cui il "Direct Corner" è stato sbloccato (richiede circa 20-40 minuti di gioco)
- Almeno 2 file `.pk3` da usare come squadra/merce di scambio simulata
- Le prod.keys della Switch (percorso di default: `~/.switch/prod.keys`)

### 6.5 Schede Wi-Fi testate
| Modello | Tipo | Driver | Affidabilità |
|---|---|---|---|
| AMD RZ616 | Interna (M.2) | mt7921e | Bassa |
| ALFA AWUS036ACHM | Esterna (USB) | mt76x0u | Alta |

*(Nota: il file "Parti descrizione video" cita invece una **RTL8821CE PCIe** come scheda usata nel video - quindi nella pratica sono state testate/usate almeno tre schede diverse tra i vari materiali raccolti. Andrebbe chiarito in fase di editing del video quale sia la scheda effettivamente mostrata nella demo finale.)*

### 6.6 Comando d'uso base (dal README ufficiale)
```bash
sudo -E ./venv/bin/python frlgtrade.py --live -o output.pk3 PARTY1.pk3 PARTY2.pk3
```

### 6.7 Flag opzionali documentati (lista non esaustiva secondo gli autori)
| Flag | Opzioni | Scopo |
|---|---|---|
| `--verbose` | N/D | Output dettagliato/prolisso, utile per debug |
| `--phy` | `phy#` (es. `phy1`) | Selezione manuale della scheda Wi-Fi fisica da usare, quando il sistema ne ha più di una |
| `--keys` | `/percorso/a/prod.keys` | Percorso non-default per le prod.keys |

Gli autori avvertono che molti flag non documentati sono o incompleti, o sperimentali/interni, o residui di esperimenti falliti - **da non usare** se non si sa esattamente cosa fanno.

### 6.8 Setup (dal README ufficiale)
1. Creare un virtual environment Python e installare le dipendenze elencate in `requirements.txt`.
2. Assicurarsi che la scheda Wi-Fi non sia gestita da NetworkManager (il modo più semplice è fermare il servizio).
3. Assicurarsi di poter ottenere privilegi root: lo script richiede `sudo`.

### 6.9 Procedura d'uso passo-passo (dal README ufficiale - riportata integralmente perché è la sequenza operativa cruciale)
1. Sulla Switch, selezionare il trading al Direct Corner e impostare la propria console come **"Leader"** (host della sessione).
2. Lanciare lo script sul PC. Può richiedere più tentativi prima di connettersi con successo.
3. Approvare sulla Switch la richiesta di join proveniente dal dispositivo simulato, che appare come **"EMU"**.
4. Sulla Switch, spostarsi verso la **SEDIA SINISTRA** ("LEFT CHAIR") nella stanza del trade. Il movimento potrebbe risultare visibilmente in ritardo (lag) a causa della natura del protocollo simulato.
5. Selezionare il Pokémon che si desidera scambiare (cioè cedere).
6. Confermare la proposta di scambio: si riceverà il **secondo** membro simulato della squadra (quello passato come `PARTY2.pk3`).
7. Una volta tornati al menu di trade, annullare (cancel) lo scambio.
8. Uscire dalla stanza.
9. A questo punto: `PARTY2.pk3` sarà presente nella squadra reale sulla Switch, mentre il Pokémon originariamente ceduto dal giocatore si troverà, sul PC, nella cartella di lavoro corrente, come file di output (`output.pk3` o il nome specificato con `-o`).

**Nota didattica importante:** questo passaggio (6-9) implica che il "trade" viene tecnicamente completato e poi **annullato** lato Switch - un dettaglio non ovvio che sfrutta probabilmente un comportamento specifico del client di gioco per catturare comunque il Pokémon in output sul lato PC senza che la Switch perda definitivamente il proprio Pokémon nello scambio reale. Questo va inteso e documentato con attenzione se si vuole spiegare la procedura nel video in modo che l'utente finale non si confonda su "cosa perde e cosa guadagna" durante il trade.

### 6.10 Crediti citati nel README
- **kinnay** - per la libreria LDN e per l'ottima wiki NintendoClients
- **pokefirered** (progetto `pret/pokefirered`) - decompilazione completa di FireRed/LeafGreen, incluso il port Switch, usata come riferimento tecnico fondamentale per capire il funzionamento interno del gioco

---

## 7. Requisiti hardware e software completi (versione consolidata da tutte le fonti)

### 7.1 Software
- Sistema operativo **Linux** (distribuzione consigliata nel materiale: **Linux Mint 22.3** - https://linuxmint.com/edition.php?id=326)
- **Python 3.12.3+** (per compatibilità piena con `kinnay/LDN`; il repo `frlg-ldn-trade` dichiara come minimo 3.9+ ma è più prudente allinearsi al requisito più recente)
- Virtual environment Python (`venv`) con le dipendenze installate da `requirements.txt` del repo `frlg-ldn-trade`
- Pacchetto di sistema `iw` (utility per la gestione di interfacce wireless via `nl80211`), installato con `pkexec apt install iw`
- **prod.keys** della propria Switch (percorso predefinito `~/.switch/prod.keys` / nel materiale scritto anche come `.switch/prod.keys` relativo)

### 7.2 Hardware
- **Scheda Wi-Fi compatibile con modalità monitor**, in una delle forme:
  - scheda PCIe interna (es. **RTL8821CE 802.11ac**, citata nel video)
  - adattatore Wi-Fi USB esterno (es. **ALFA AWUS036ACHM**, citato come il più affidabile nei test ufficiali del repo, con driver `mt76x0u`)
  - **da evitare/usare con cautela**: schede interne M.2 come **AMD RZ616** (driver `mt7921e`), segnalate come meno affidabili e più lente, con possibili deadlock
- **Switch o Switch 2** con **FRLG** installato/eseguibile, portato al punto di sblocco del Direct Corner (~20-40 minuti di gioco)
- Almeno **2 file `.pk3`** validi, da preparare eventualmente con **PKHeX for Web** (https://pkhex-web.github.io/)
- Strumento di scrittura del supporto d'installazione: **Rufus** (https://rufus.ie/en/), per creare eventualmente una chiavetta USB avviabile con Linux Mint
- Facoltativo/collaterale: **GBxCart RW** (https://www.gbxcart.com/) - dispositivo per interfacciarsi con cartucce fisiche Game Boy/GBA via USB

---

## 8. Procedura operativa passo-passo (setup + esecuzione) - versione unificata

Questa sezione fonde le istruzioni del README ufficiale (sezione 6.8-6.9) con i comandi bash annotati nel file "Parti descrizione video" (sezione 2.4), in un'unica sequenza didattica end-to-end.

### Fase A - Preparazione del sistema operativo
1. Scaricare e scrivere Linux Mint 22.3 su una chiavetta USB avviabile usando Rufus (su un PC Windows) oppure uno strumento equivalente.
2. Avviare/installare Linux Mint sul PC che verrà usato per il trading.

### Fase B - Preparazione ambiente Python
3. Verificare/installare **Python 3.12.3+**.
4. Clonare il repository `tornadus/frlg-ldn-trade`.
5. Creare un virtual environment (`venv`) nella cartella del progetto.
6. Installare le dipendenze: `pip install -r requirements.txt` (dentro il venv).

### Fase C - Preparazione scheda Wi-Fi
7. Assicurarsi che la scheda Wi-Fi scelta supporti la modalità monitor (vedi tabella schede testate).
8. Installare il tool `iw`:
   ```bash
   pkexec apt update
   pkexec apt install iw
   ```
9. Fermare NetworkManager, per evitare interferenze con la gestione a basso livello della scheda:
   ```bash
   sudo systemctl stop NetworkManager
   ```
   *(Attenzione didattica: da questo momento il PC perde la connettività Internet tramite quella interfaccia, salvo si usi un secondo adattatore o una connessione cablata separata.)*

### Fase D - Preparazione delle prod.keys e dei file .pk3
10. Ottenere le proprie `prod.keys` (estratte dalla propria console Switch modificata secondo i processi standard della community homebrew - non trattato nel materiale raccolto, va documentato a parte se necessario) e posizionarle in `~/.switch/prod.keys` oppure in un percorso a scelta da passare con `--keys`.
11. Preparare almeno due file `.pk3` (es. tramite PKHeX for Web) da usare come `PARTY1.pk3` e `PARTY2.pk3`.

### Fase E - Esecuzione del trade
12. Sulla Switch: avviare FRLG, recarsi al Direct Corner, avviare una sessione di trade e impostare la propria console come "Leader".
13. Sul PC, dentro la cartella del progetto, lanciare:
    ```bash
    sudo -E ./venv/bin/python frlgtrade.py --live --verbose --keys .switch/prod.keys -o output.pk3 PARTY1.pk3 PARTY2.pk3
    ```
    (versione con logging dettagliato, dal file "Parti descrizione video"; la versione "minima" da README ufficiale omette `--verbose` e usa il percorso di default per le chiavi).
14. Attendere la connessione - può richiedere più tentativi.
15. Sulla Switch, approvare la richiesta di join da "EMU".
16. Sulla Switch, spostarsi sulla sedia sinistra della stanza di trade (movimento potenzialmente laggato).
17. Selezionare il Pokémon da cedere e confermare lo scambio.
18. Una volta tornati al menu, annullare il trade e uscire dalla stanza.
19. Verificare che `PARTY2.pk3` sia ora nella squadra reale sulla Switch, e che sul PC sia comparso il file di output (`output.pk3`) nella cartella di lavoro.

### Fase F - Ripristino del sistema
20. Se necessario, riavviare NetworkManager per ripristinare la normale connettività:
    ```bash
    sudo systemctl start NetworkManager
    ```

---

## 9. Comandi Bash raccolti (annotati riga per riga)

### 9.1 Comando principale di trade
```bash
sudo -E ./venv/bin/python frlgtrade.py --live --verbose --keys .switch/prod.keys -o output.pk3 PARTY1.pk3 PARTY2.pk3
```
- `sudo` → esecuzione con privilegi di root, necessaria per `CAP_NET_ADMIN` (gestione a basso livello della scheda Wi-Fi).
- `-E` → flag di `sudo` che **preserva le variabili d'ambiente** dell'utente originale (incluse eventuali `PATH`, variabili del venv, ecc.), altrimenti perse passando a root.
- `./venv/bin/python` → usa esplicitamente l'interprete Python del virtual environment locale, invece del Python di sistema, garantendo che tutte le dipendenze installate in `requirements.txt` siano disponibili anche sotto `sudo`.
- `frlgtrade.py` → script principale del repository `tornadus/frlg-ldn-trade`.
- `--live` → modalità di esecuzione "live"/reale (verosimilmente distingue da una modalità simulata/dry-run non documentata nel materiale raccolto).
- `--verbose` → attiva log dettagliati, utile in fase di debug/dimostrazione video.
- `--keys .switch/prod.keys` → percorso (qui relativo) del file prod.keys.
- `-o output.pk3` → nome del file di output in cui verrà scritto il Pokémon ricevuto in cambio.
- `PARTY1.pk3 PARTY2.pk3` → argomenti posizionali: i due file `.pk3` che compongono la squadra simulata lato PC.

### 9.2 Permessi USB per GBxCart
```bash
chmod a+x GBX.AppImage
pkexec chmod 0666 /dev/ttyUSB0
QT_QPA_PLATFORM=xcb ./GBX.AppImage
```
- `chmod a+x GBX.AppImage` → rende eseguibile il file AppImage del software GBxCart per tutti gli utenti (`a+x` = "all, add execute").
- `pkexec chmod 0666 /dev/ttyUSB0` → concede permessi di lettura/scrittura a tutti gli utenti sul device seriale USB `/dev/ttyUSB0` (tipico per adattatori seriali-USB come quelli usati dal GBxCart), usando `pkexec` per elevare i privilegi necessari a modificare i permessi di un file di device.
- `QT_QPA_PLATFORM=xcb ./GBX.AppImage` → imposta la variabile d'ambiente `QT_QPA_PLATFORM` a `xcb` prima di lanciare l'AppImage. Questo forza l'applicazione Qt (il software GBxCart è basato su Qt) a usare il backend grafico **XCB** (X11) invece del default, spesso necessario su sistemi Linux dove il backend Wayland nativo causa problemi di rendering con applicazioni Qt più datate o pacchettizzate diversamente.

### 9.3 Setup scheda Wi-Fi
```bash
pkexec apt update
pkexec apt install iw
sudo systemctl stop NetworkManager
```
- `pkexec apt update` → aggiorna gli indici dei pacchetti disponibili (con privilegi elevati via pkexec invece di sudo - equivalenti in questo contesto, con differenza nel meccanismo di autenticazione, tipicamente grafico per pkexec).
- `pkexec apt install iw` → installa il pacchetto `iw`, l'utility standard su Linux per configurare dispositivi wireless tramite l'interfaccia kernel `nl80211` (sostituisce il vecchio `iwconfig`).
- `sudo systemctl stop NetworkManager` → ferma il servizio di gestione automatica della rete, liberando il controllo delle interfacce wireless per lo script Python.

### 9.4 Comando di emergenza in caso di crash
```bash
sudo killall python3 python python3.12
```
- `killall` → termina **tutti** i processi che corrispondono ai nomi indicati.
- `python3 python python3.12` → tenta di terminare processi Python avviati con uno qualsiasi di questi tre nomi eseguibili comuni (differenze dovute a come Python è invocato/symlinkato sul sistema), utile perché uno script LDN bloccato può lasciare la scheda Wi-Fi in uno stato inconsistente (es. ancora in modalità monitor/AP), da cui è necessario liberarsi uccidendo il processo prima di poter ripartire in modo pulito.

---

## 10. Strumenti collaterali

### 10.1 PKHeX for Web
- **URL:** https://pkhex-web.github.io/
- Versione browser dell'editor di salvataggi Pokémon PKHeX. Utile in questo workflow per **creare o modificare** i file `.pk3` usati come `PARTY1.pk3` / `PARTY2.pk3`, senza dover installare l'applicazione desktop.

### 10.2 GBxCart RW
- **URL:** https://www.gbxcart.com/
- Dispositivo hardware di terze parti per leggere/scrivere cartucce Game Boy / Game Boy Color / Game Boy Advance via USB. Nel materiale raccolto compare come strumento collaterale (probabilmente per ottenere salvataggi da cartucce fisiche reali, da convertire poi in `.pk3`), con relative istruzioni di permessi USB (sezione 9.2).

### 10.3 Rufus
- **URL:** https://rufus.ie/en/
- Strumento Windows per creare supporti USB avviabili, usato qui per installare Linux Mint.

### 10.4 Linux Mint 22.3
- **URL:** https://linuxmint.com/edition.php?id=326
- Distribuzione Linux consigliata come ambiente operativo per l'intero workflow.

---

## 11. Rischi, limiti, cause di crash e troubleshooting

Ricostruito e organizzato da tutte le fonti raccolte:

1. **Affidabilità hardware-dipendente:** la scelta della scheda Wi-Fi è critica. Schede interne moderne come la AMD RZ616 possono essere fino alla metà più lente e soggette a **deadlock** (blocco totale del processo, che non termina né in errore né con successo). Le schede USB esterne di fascia "monitor mode friendly" (es. ALFA AWUS036ACHM, driver `mt76x0u`) risultano più affidabili secondo i test ufficiali degli autori.
2. **Connessione non garantita al primo tentativo:** il README stesso segnala che potrebbero servire più tentativi per stabilire la connessione LDN.
3. **Lag nel movimento in-game:** una volta connessi, il movimento del personaggio sulla Switch (per raggiungere la sedia di trade) può presentare lag visibile, per la natura "simulata" del secondo giocatore.
4. **Interferenza di NetworkManager:** se non viene fermato, il servizio di gestione rete di sistema può competere con lo script per il controllo della scheda, causando fallimenti silenziosi o comportamenti imprevedibili.
5. **Perdita di connettività Internet:** conseguenza diretta dello stop di NetworkManager sulla scheda usata per LDN.
6. **Stato "sporco" dopo un crash:** se lo script si blocca o crasha, la scheda Wi-Fi può restare in uno stato intermedio (es. ancora in modalità monitor o AP) che impedisce un riavvio pulito; la soluzione documentata è terminare forzatamente tutti i processi Python (`sudo killall python3 python python3.12`) prima di ritentare.
7. **Complessità intrinseca del protocollo:** gli autori di `kinnay/LDN` descrivono esplicitamente l'uso della libreria come "difficile" (*"Using LDN is hard"*), motivo per cui esiste una pagina wiki dedicata ai problemi comuni.
8. **Flag non documentati/instabili:** il proof-of-concept avverte che, oltre ai tre flag documentati (`--verbose`, `--phy`, `--keys`), esistono altri flag interni non pronti per l'uso pubblico.
9. **Dipendenza da reverse engineering di terzi:** l'intero funzionamento lato-gioco si appoggia alla decompilazione comunitaria `pret/pokefirered`; eventuali aggiornamenti del gioco su Switch potrebbero rompere la compatibilità se cambia il formato dati interno.

---

## 12. Considerazioni legali/etiche (da tenere presenti, non omissibili in un handoff completo)

Questo punto non era esplicitamente discusso nella chat originale, ma è tecnicamente rilevante per completezza dell'handoff, dato che il materiale coinvolge:

- **Estrazione e uso di prod.keys**, che richiede una console Switch modificata ("hackerata") e le cui chiavi non possono essere legalmente redistribuite, poiché derivano dal firmware proprietario Nintendo.
- **Reverse engineering** di un protocollo di rete proprietario (LDN) e del formato dati interno di un gioco commerciale, attività che si colloca in una zona grigia dal punto di vista dei termini di servizio Nintendo, anche se motivata da finalità di interoperabilità/didattiche.
- **Reperimento/possesso della decompilazione `pokefirered`**, un progetto comunitario di reverse engineering completo del codice sorgente di un gioco commerciale.

Questi elementi non compaiono come avvisi nel materiale originale della chat: si aggiungono qui **solo a scopo di completezza documentale**, così che chi riprende il progetto in Claude Code sia consapevole del contesto complessivo, senza che il presente handoff esprima un giudizio in merito.

---

## 13. Stato del materiale: cosa manca, cosa va verificato in una sessione di lavoro

Elenco onesto delle lacune informative rilevate durante la stesura di questo handoff, utile per non dare nulla per scontato nella prossima sessione:

- **Contenuto effettivo del video YouTube** (`https://www.youtube.com/watch?app=desktop&v=Ld2YphF-HVI&t=1s`): non recuperato in questa sessione (nessuna trascrizione/descrizione testuale disponibile via i soli metadati); se serve per completare la descrizione, va aperto/analizzato manualmente.
- **Codice sorgente effettivo** di `frlgtrade.py`, del pacchetto `ldn`, e dell'intera cartella `frlgsim/`: non letto riga per riga in questa sessione (solo README/metadati dei repository), poiché il materiale di partenza in chat conteneva solo i link, non il codice.
- **Discrepanza sui requisiti Python** tra README ufficiale del repo (3.9+) e file di descrizione video (3.12.3+): da chiarire quale sia il requisito reale/consigliato.
- **Discrepanza sulla scheda Wi-Fi usata nel video** (RTL8821CE PCIe secondo il file descrizione video) vs. le schede ufficialmente testate/consigliate nel README (ALFA AWUS036ACHM esterna, sconsigliata la RZ616 interna): da verificare quale sia effettivamente quella mostrata nel video finale.
- **Processo di estrazione delle prod.keys**: non documentato nel materiale raccolto (presupposto come già noto/posseduto dall'utente).
- **Rapporto tra GBxCart e il resto del workflow**: il materiale lo elenca tra i requisiti/comandi ma non spiega esplicitamente in quale fase del processo entri in gioco (probabile uso per ottenere salvataggi da cartucce fisiche, ma non confermato dal testo originale).
- **Versione del gioco FRLG su Switch**: non è chiarito nel materiale se si tratti di un'emulazione, di un port ufficiale, o di altro; questo dettaglio tecnico condiziona fortemente la spiegazione "didattica" del meccanismo di trade e andrebbe verificato prima di pubblicare contenuti definitivi.

---

## 14. Prompt di ripartenza suggerito per Claude Code

Per riprendere il lavoro in una sessione **Claude Code** (dove è disponibile accesso a bash, filesystem, git, ecc.), si suggerisce di iniziare incollando questo file come contesto e, ad esempio, chiedendo:

> "Ho questo handoff (`HANDOFF_frlg-ldn-trade.md`). Clona i repository `kinnay/LDN` e `tornadus/frlg-ldn-trade`, leggi il codice sorgente di `frlgtrade.py` e del pacchetto `ldn`, e aiutami a [scrivere la descrizione definitiva del video / capire il funzionamento interno del trade / preparare un ambiente di test], colmando le lacune elencate nella sezione 13."

---

*Fine documento. Nessuna fonte o dettaglio presente nel contesto della chat originale è stato omesso in questo handoff.*
