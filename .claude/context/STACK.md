---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
  - pokemon-gen12-gen3-bridge-original-hardware/
last-verified-commit: d08a011
---

# Stack

Questo progetto non ha uno stack software nel senso consueto: non c'e' codice, non c'e' un manifesto di dipendenze e non c'e' una pipeline di build. Quello che ne fa le veci e' un inventario di hardware e di toolchain, perche' e' li' che stanno i vincoli reali e le scelte che sarebbe costoso rifare. La sola parte destinata a diventare software vero e' il ponte fra generazioni, e quando lo sara' questa scheda si sdoppiera' con un profilo di stack vero e proprio.

## Hardware

La console e' un Old 3DS XL con seriale che inizia per SEH, partito dal firmware 11.17.0-50E, oggi su custom firmware, con una scheda SD da 32 GB formattata FAT32. Il lettore di cartucce Game Boy e Game Boy Advance e' un GBxCart RW v1.4 Pro nella variante USB-C, colore blu, ordinato il 18 agosto 2026 con il cavo USB-A verso USB-C. Il gioco su cui si interviene per il bug dell'inventario gira su Game Boy Advance SP.

Per il sottoprogetto del ponte fra generazioni l'inventario hardware non e' ancora stato fatto, ed e' esattamente il motivo per cui quel track e' fermo: quante console Game Boy Advance esistono, se c'e' un GameCube o un Wii modificato, se c'e' una flashcart, se c'e' un cavo Link per Game Boy Color e se c'e' la capacita' di saldare sono le domande che decidono lo stack di quel sottoprogetto.

Il track del trading LDN aggiunge una console Nintendo Switch e un requisito che non ha equivalenti negli altri sottoprogetti: una scheda Wi-Fi capace di modalita' monitor. E' il fattore critico dichiarato, non un dettaglio, perche' le schede USB esterne di fascia adatta risultano affidabili nei test degli autori del proof of concept, mentre alcune schede interne moderne sono fino alla meta' piu' lente e possono andare in deadlock. Quale scheda ci sia su questa macchina non e' ancora stato accertato, e da quella risposta dipende se il track sia praticabile. Lo stesso lettore GBxCart RW del track Smeraldo compare fra i requisiti, ma il materiale non spiega in quale fase entri.

## Toolchain

Sulla console vivono boot9strap come punto di ingresso del custom firmware, Luma3DS nella versione 13.4 come firmware, e GodMode9 come strumento di dump e di gestione dei file. MSET9 e' stato usato una volta sola come exploit di installazione ed e' stato rimosso a fine procedura. SEEDconv e' servito a generare il file di seed necessario a decrittare le cartucce 3DS pubblicate dopo il 2014. Checkpoint e' presente per la gestione dei salvataggi.

Sul PC, che e' una macchina Windows 11, la catena del sottoprogetto Smeraldo e' composta dai driver seriali CH340 e CH341, da FlashGBX per leggere e scrivere il salvataggio, dal runtime .NET 9 Desktop e da PKHeX come editor. La scelta di Windows non e' una preferenza: PKHeX e' un'applicazione .NET Windows Forms e il supporto a Mono e Wine e' stato abbandonato dal 2023, quindi le alternative non sono equivalenti.

Il track del trading LDN richiede pero' Linux, con Linux Mint come distribuzione suggerita anche solo da chiavetta avviabile, piu' Python in ambiente virtuale, l'utility di sistema per la gestione delle interfacce wireless, e le due librerie `kinnay/LDN` e `tornadus/frlg-ldn-trade`. Il progetto ha quindi due sistemi operativi in tensione fra loro, ciascuno obbligato dal proprio track e per ragioni diverse: come farli convivere, in dual boot o su supporto avviabile, e' una decisione aperta che non e' urgente finche' quel track resta in ricerca.

Se il ponte fra generazioni prendesse la strada dell'hardware servirebbe devkitARM, mentre la strada del tool offline su PC porterebbe a Python, C# o Rust. Nessuna delle due e' ancora stata scelta. I sottoprogetti destinati a produrre software sono ora due, il ponte e il trading LDN, ed e' il segnale che rende sensato riaprire prima o poi il gate del server MCP di lettura del codice, oggi rimandato per ADR-010.

## Alternative deliberatamente escluse

Il percorso Action Replay per correggere l'inventario di Smeraldo e' stato abbandonato dopo averlo studiato a fondo. Il Master Code e l'Anti-DMA erano verificati su piu' fonti indipendenti, ma per i codici della tasca Strumenti Base non esisteva alcuna fonte affidabile, e la scelta e' stata di non indovinare indirizzi di memoria su un salvataggio irripetibile.

MSET9 e' stato preferito ad altri punti di ingresso per il custom firmware per ragioni documentate nella sezione 4.1 dell'handoff del sottoprogetto 3DS, legate al firmware di partenza della console.

L'emulazione e' esclusa per costruzione dal sottoprogetto del ponte, perche' nessun emulatore replica fedelmente l'interazione elettrica fra Game Boy e Game Boy Advance, che e' proprio il meccanismo su cui il ponte si regge. Per il sottoprogetto 3DS l'emulatore Azahar non e' escluso ma solo rimandato: l'orientamento attuale e' portare i file fisicamente via SD.

## Dipendenze di sviluppo aggiunte il 2026-08-25

Il progetto non aveva dipendenze esterne e ne ha ora una, dichiarata qui perche' una dipendenza non scritta e' una dipendenza che si riscopre rompendosi.

`yt-dlp`, installato con `python -m pip install --user yt-dlp`, versione 2026.08.19 alla prima installazione. Serve a scaricare i sottotitoli automatici dei video, che sono l'unica forma in cui una fonte video diventa citabile. La ragione per cui serve uno strumento dedicato invece di una richiesta HTTP e' documentata in `.claude/rules/web-sources-not-fetchable.md`: la pagina del video si scarica, ma l'endpoint che serve i sottotitoli restituisce zero byte a qualunque richiesta che non provenga dal lettore vero. Si aggiorna con lo stesso comando e non ha configurazione.

Le due dipendenze implicite restano il Python di sistema, oggi 3.13, e `git`. Il pacchetto `pokebridge` e i suoi test non dipendono da nulla oltre alla libreria standard, ed e' una scelta da mantenere.

## Macchina con GPU raggiungibile in rete locale

Esiste un secondo computer con GPU che espone Ollama all'indirizzo `http://192.168.20.58:11500`, raggiungibile direttamente in HTTP dalla rete locale senza tunnel. I modelli presenti alla verifica del 2026-08-25 sono `qwen3:14b`, `llama3.1:8b-instruct-q4_K_M`, `llama3.2:latest` e `bge-m3:latest`.

Va detto con precisione cosa quella macchina puo' e non puo' fare, perche' il malinteso e' facile. Non puo' trascrivere audio: nessuno dei modelli presenti e' un riconoscitore vocale, e Ollama serve modelli di linguaggio, non modelli acustici. La trascrizione dei video resta compito di `yt-dlp`, che scarica i sottotitoli che YouTube ha gia' generato, e servirebbe un modello di famiglia Whisper soltanto per un audio senza sottotitoli.

Cio' che quella macchina puo' fare, ed e' allineato alla regola di token economy del progetto, e' condensare localmente fonti molto lunghe prima che entrino in conversazione: una trascrizione da un'ora di video o un thread di forum di duecento messaggi si riducono a una sintesi densa senza consumare contesto ne' pagare token. Il modello `bge-m3` e' un modello di embedding, quindi abilita anche la ricerca semantica locale su tutto il corpus di `_notes/fonti/`, che diventera' utile quando quella cartella sara' cresciuta.

Nessuna di queste due cose e' ancora implementata: sono possibilita' registrate, e stanno fra le voci di `pending.md`.
