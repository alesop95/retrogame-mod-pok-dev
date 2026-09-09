---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - pokemon-gen12-gen3-bridge-original-hardware/
last-verified-commit: ee0f52b
stato: decisione ADR-008 ancora aperta; le tre generazioni sono scritte e collaudate e dal 2026-09-09 esiste anche lo strato del salvataggio da 128 KiB
---

# Sottoprogetto: ponte Pokemon da Gen 1 e 2 verso Gen 3 su hardware originale

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`. L'handoff di ricerca non esiste più: la sua conoscenza è stata verificata sul sorgente e assorbita nella referenza `DATA-FORMATS_Gen1-Gen2-Gen3.md` e nel percorso di studio sotto `docs/`, per ADR-013.

Obiettivo: costruire un tool che trasferisca Pokemon dalle generazioni 1 e 2 alla generazione 3 su hardware originale, un ponte che ufficialmente non esiste perché Nintendo non lo ha mai fornito.

## Dove siamo

Il formato dei dati delle tre generazioni è documentato byte per byte e verificato sul disassemblato, non sull'enciclopedia, in `DATA-FORMATS_Gen1-Gen2-Gen3.md`. Sono chiusi undici punti che erano aperti o dubbi, fra cui l'ordine dei nibble dei DV, l'algoritmo del checksum di Gen 3, la dimensione del blocco di scambio e il modo in cui Poke Transporter GB ottiene l'esecuzione di codice, che avviene sul cavo e non richiede alcun setup lato giocatore. Due affermazioni dell'handoff di ricerca risultano corrette solo in parte: il PCCS documenta quattro metodi di conversione ma nel codice ne implementa uno, e l'impossibilità di emulare riguarda il ponte fra Game Boy e Game Boy Advance, non il collegamento fra due Game Boy, che si collauda su BGB via TCP. Esiste il codice del lato Game Boy, in `pokebridge/`: primitivi, lettori e scrittori di generazione 1 e 2 per box, squadra e liste di squadra, e transcodifica del testo sulle tabelle generate. Sessantatre prove passano, la portante essendo la simmetria fra lettura e riscrittura su buffer casuali con seme fissato. Scrivere il codice ha fatto emergere un errore in più nella referenza, cioè la dimensione della lista della squadra Gen 1, che è 404 byte e non 194: la fonte aveva letto 0x194 come decimale.

Questo è l'unico dei quattro sottoprogetti destinato a diventare software vero. Quando lo diventerà si riapre il gate del server MCP code-context, e diventa sensato un `CLAUDE.md` annidato in questa cartella con le sole convenzioni di build, lint e test, senza stato.

## Prossimo passo concreto

Il lettore e scrittore della struttura di generazione 3 è scritto e collaudato dal 2026-08-26, in `pokebridge/gen3.py`, con cifratura, permutazione e checksum verificati sul sorgente di `pret/pokeemerald` invece che su fonte secondaria: le ventiquattro righe della tabella di permutazione sono verbatim dalla macro `SUBSTRUCT_CASE` di `src/pokemon.c`, i confini dei campi di bit vengono dalle dichiarazioni di `include/pokemon.h`, e da là si sono chiusi i quattro bit che la referenza non nominava, cioè i bit 27 a 30 della parola dei nastri, che nel sorgente sono `unusedRibbons`. La suite passa 114 prove. Il valore di personalità è immutabile dopo la costruzione, come prescrive `docs/20-architettura-codice.md`, e chi deve cambiarlo usa `with_personality`, che ricompone la struttura da capo.

Entrambi i candidati che questa sezione elencava sono stati eseguiti il 2026-09-09 e il prossimo passo è quello che ne resta. Lo strato del salvataggio da 128 KiB è `pokebridge/save3.py`: sceglie fra i due slot con la regola che a parità vince B, ricompone i buffer che le quattordici sezioni frammentano prendendo i primi 3968 byte di ciascuna, legge e scrive le posizioni del deposito e della squadra ricalcolando i checksum delle sole sezioni toccate, genera un salvataggio sintetico valido con `crea_vuoto` e converte fra la forma del file dell'editor e quella del salvataggio, che non sono la stessa. La suite passa 206 prove. Il caricatore è `tools/carica-lotto-gen3.py`, provato sul lotto degli incontri con quattordici voci scritte e rilette identiche byte per byte.

La prova che vale più delle altre è quella sul record a cavallo di due sezioni: con 3968 byte di dati per sezione e record da ottanta, la posizione quarantanove comincia dentro una sezione e finisce nella successiva, e scrivere come se il buffer fosse contiguo sovrascriverebbe il piede di una sezione invalidando lo slot senza che nulla se ne accorga fino al caricamento della partita.

Il prossimo passo è quindi il confronto vero, cioè generare il medesimo contenitore con il verificatore esterno e diffare i byte: è la prova che alla simmetria mancava e che il limite noto descritto sotto richiede.

## Decisione aperta, registrata come ADR-008

Le quattro opzioni sono ancora tutte in piedi e nessuna è stata scelta, ma il loro costo relativo è cambiato ed è analizzato in `docs/30-opzioni-implementative.md`. Il punto nuovo è che l'opzione A non è più a costo zero di sviluppo, perché la conversione fedele delle statistiche non esiste in nessuna implementazione pubblica e va scritta comunque, e che gli strati di formato e conversione sono identici in tutte e quattro, quindi si possono costruire prima della decisione.

## Limite noto delle prove attuali

La prova di simmetria fra lettura e riscrittura è forte ma invariante rispetto a una permutazione di etichette: se due campi della stessa larghezza fossero scambiati fra loro, per esempio tipo 1 con tipo 2 o due delle cinque Stat Experience, la simmetria continuerebbe a valere. Le difese attuali sono parziali, cioè un caso costruito a mano che verifica alcuni offset e il fatto che gli offset vengano dal disassemblato. La difesa che chiude il cerchio è il confronto con un dato reale, e il controllo che costa meno è aprire un salvataggio con `PKHeX` e confrontare campo per campo con ciò che dichiara `pokebridge`. Il ragionamento completo, con l'inventario di ciò che non è stato verificato, sta in `docs/23-prove-eseguite.md`.

## Che cosa è arrivato dall'esterno il 2026-08-26

Due letture indipendenti hanno toccato questo track senza essere state fatte per esso, e vale registrarle qui perché cambiano il peso delle opzioni di ADR-008.

Dal canale di Pokemon Multiplayer Research arriva la conferma dell'opzione D da parte di chi ha scritto il codice dell'altro capo: il Wireless Adapter del Game Boy Advance non è 802.11 ma un progetto proprietario, e la via indicata per collegare un Game Boy Advance fisico a una console moderna è un microcontrollore che si finge quel dispositivo. Nel canale compare la fotografia di una catena funzionante. Non è il nostro caso d'uso, perché noi andiamo verso hardware originale e non verso una Switch, ma sposta l'opzione D dal terreno delle ipotesi a quello delle cose fatte da qualcuno. Il ragionamento sta in `docs/11-wireless-locale-e-ponte-switch.md`.

Dal canale del Glitch City Research Institute arriva la conoscenza sull'esecuzione di codice in generazione 3, che il progetto non aveva, con una conferma indiretta preziosa: la catena documentata attraversa i campi della struttura nell'ordine dell'intestazione della sezione 5 della referenza, quindi conferma quel layout da una fonte che lo stava sfruttando e non documentando. Dallo stesso canale arriva un rischio da registrare: scambiare verso un gioco di generazione 3 una struttura che contenga la sequenza di controllo giusta non produce un dato sbagliato, produce un dato che quel gioco esegue. È in `docs/09-esecuzione-codice.md`.

## Avvertenze da non perdere

Il backup dei salvataggi è obbligatorio prima di qualsiasi tentativo. Il trasferimento è a senso unico e distruttivo sulla sorgente, cioè il Pokemon viene rimosso dal gioco di partenza, e modifica entrambi i salvataggi. Le cartucce bootleg causano la perdita dei Pokemon trasferiti, e la ragione tecnica è che il payload contiene indirizzi assoluti tarati su una ROM precisa. La verifica finale del ponte richiede hardware reale, mentre il protocollo del cavo fra due Game Boy si collauda su emulatore.
