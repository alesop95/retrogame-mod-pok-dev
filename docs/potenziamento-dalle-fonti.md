---
tipo: nota di lavoro
livello: strumenti
tags: [strumenti, fonti, potenziamento, ADR-100]
up: "[[index]]"
vedi_anche: ["[[22-strumenti]]", "[[strumenti-dal-web]]", "[[strumenti-interattivi]]", "[[censimento-fonti-codice]]"]
---

# Il potenziamento degli strumenti dalle fonti con codice

> Documento autorato, aperto il 2026-10-07 per ADR-100: il codice del progetto si potenzia su tutte le fonti tecniche e con codice, e ogni potenziamento entra in [[22-strumenti]], in [[strumenti-dal-web]] e nella tesi. La parte deterministica del censimento è [[censimento-fonti-codice]], generato da `tools/censimento-fonti-codice.py`; qui sta il giudizio, una fonte alla volta, e ogni giudizio dice se poggia su una lettura del codice o soltanto sulla riga del registro.

## Che cosa è già fatto

Gli strumenti interattivi delle fonti, cioè le applicazioni web e i calcolatori che il residuo del corpus lasciava come «saltati», sono stati studiati il 2026-10-05 in [[strumenti-interattivi]]: per diciannove indirizzi c'è una decisione, e l'unico da ereditare, il convertitore della Console Virtuale di `inject.sigkill.tech`, è diventato `tools/converti-salvataggio-vc.py`. Restano da fare le fonti con codice di `SOURCES.md`.

## La misura

Il 2026-10-07 `tools/censimento-fonti-codice.py` ha trovato nelle righe di tabella di `SOURCES.md` 110 repository di codice distinti. Di questi 98 sono nominati da qualche parte del progetto e 43 dal codice, cioè da uno strumento in `tools/` o in un sottoprogetto; 67 non sono usati da alcuno strumento, e di questi 12 non sono nominati da nessun file fuori dal registro. La colonna dell'esito scritto conta 55 repository senza un esito nella riga, che sono quasi tutti nelle sezioni del corpus della collezione, dove l'esito sta nel residuo del corpus e non nella riga: per lo strumento `tools/conta-letti.py` quelle righe sono chiuse.

## La triage dei 67 non usati dal codice

La triage che segue poggia sulla riga del registro e sul nome del repository, non sulla lettura del codice, salvo dove è detto: è un'ipotesi su dove valga la pena leggere, e ogni riga si promuove a decisione solo dopo la lettura.

Il primo gruppo è quello che può aggiungere qualcosa al fuoco corrente, cioè a generare, giudicare, convertire o verificare gli esemplari della collezione. In ordine di quanto se ne aspetta:

| Repository | Che cosa si ipotizza possa dare | Come si verificherebbe |
|---|---|---|
| `architdate/PKHeX-Plugins` | la generazione automatica di esemplari legali a partire da una descrizione (Auto Legality Mod), da confrontare con `tools/pkhex-genera` e `tools/pkhex-rigenera`; il registro la dà come letta | leggere come costruisce un esemplare dall'incontro e se copre classi che i nostri strumenti trattano a mano |
| `andrewbenington/OpenHome` | un gestore di collezione aperto con le conversioni fra generazioni scritte indipendentemente da PKHeX: un secondo parere sulle conversioni di `tools/pkhex-scrivi-salvataggio`, come `tools/confronta-ace-builder.py` lo è per i doni | leggere i convertitori e provarli su un campione delle copie per HOME |
| `sofianeelhor/PKForge` | fonte nuova del proprietario del 2026-10-07 (punto 5 dell'ordine di lavoro), collegata a un video; non letta | leggere repository e video, decidere se informativo |
| `kuroppoi/entralinked` | un emulatore del servizio di sincronizzazione della quinta generazione: la via ai contenuti del Dream World, cioè esemplari e oggetti che la collezione oggi non considera | leggere che cosa consegna e verificare con la libreria se gli esemplari risultano legali |
| `polaris-/dwc_network_server_emulator` | l'emulazione del servizio Wi-Fi di quarta e quinta generazione, cioè la via dei doni segreti via rete | leggere quali doni serve e confrontarli con le carte già prodotte da `tools/pkhex-dono` |
| `zaksabeast/DreamRadarCartRedirect`, `mamba2410/reverse-pokewalker`, `francesco265/RtcPwalker` | le periferiche (Dream Radar e Pokéwalker) viste dal lato del codice che le emula o le studia: un controllo indipendente dei lotti di `tools/pkhex-periferiche` | leggere come derivano i valori degli esemplari consegnati |
| `Admiral-Fish/RNGReporter`, `MersenneTwister-Lab/TinyMT`, `yuhasem/poc_utils`, `yuhasem/FeebasFinder` | i generatori pseudocasuali scritti indipendentemente: una verifica dei metodi di PID e valori individuali che oggi si affida soltanto alla libreria | leggere i metodi e rifare la verifica su un campione di lotti |
| `ncorgan/pksav`, `crumblingstatue/rgen3`, `ads04r/Gen3Save`, `aarant/gen3tools`, `haven1433/HexManiacAdvance`, `projectpokemon/Gen3-WCTool` | lettori e scrittori di salvataggi di terza generazione: un secondo parere su `pokebridge` e sugli strumenti di Smeraldo, come la verifica indipendente del giro sul Rubino | leggere la struttura dei salvataggi che assumono e confrontarla con `pokebridge` sulle riletture vere |
| `suloku/BW_tool` | uno strumento di salvataggi di quinta generazione | leggere che cosa modifica |
| `FlagBrew/PKSM`, `FlagBrew/PKSM-Scripts` | il gestore di salvataggi che gira sulla console, con gli script di iniezione degli eventi | leggere gli script; l'uso sulla console resta nel perimetro di `rules/hardware-and-perimeter.md` |

Il secondo gruppo serve ai track dell'hardware e del ponte, non al fuoco corrente: `devkitPro/libtonc`, `gbdev/rgbds`, i due elenchi `awesome-gbdev` e `awesome-gbadev`, `REONTeam/libmobile` e `REONTeam/trade-corner` (letti), `kinnay/LDN` ed `Ethiquema/ryu_ldn_nx` (letti), `E-Sh4rk/PokeGlitzer` (letto, track ACE), `InternalLoss/DLS1-Files`, `TurdPooCharger/GBAVCSM`, `TuxSH/TWLSaveTool`. Si riprendono quando quei track tornano attivi.

Il terzo gruppo non ha niente da dare agli strumenti del progetto, perché sono lanciatori, emulatori, programmi di sistema della console o strumenti di comunità: `nds-bootstrap`, `TWiLightMenu`, `GodMode9i`, `Luma3DS`, `NTR_Forwarder`, `NDSForwarder`, le due copie di `YANBF` con i loro accessori, `Universal-Updater`, `3DShell`, `ftpd`, `3DSync`, `wumiibo`, `DaedalusX64-3DS`, `Ohana3DS-Rebirth`, `GBARunner2`, `retroarch-cores`, `Multi-PokemonFramework`, `pos-tls-patcher`, `RiiConnect24/DNS-Server`, `8F-Helper`, il randomizzatore `universal-pokemon-randomizer-zx`, i due robot di Reddit `sneakpeekbot` e `RemindMeBot`, e i quattro gist. `Checkpoint`, `MSET9` e `SEEDconv` sono strumenti già usati sulla console e documentati negli handoff del 3DS; di Checkpoint resta da leggere la documentazione, voce già aperta in `pending.md`.

## L'ordine di lettura

Un lotto per giro, con una decisione scritta per ciascun repository (ereditare, usare come secondo parere, non serve) e il potenziamento eventuale documentato in [[22-strumenti]], in [[strumenti-dal-web]] e nella tesi. Primo lotto: `PKHeX-Plugins`, `OpenHome`, `PKForge` con il suo video, e la documentazione di Checkpoint. Secondo: i lettori di salvataggi di terza generazione, confrontati con `pokebridge` sulle riletture vere. Terzo: le periferiche e i generatori pseudocasuali. Quarto: `entralinked` e l'emulatore del servizio Wi-Fi, che possono allargare la collezione e quindi chiedono anche una decisione del proprietario.
