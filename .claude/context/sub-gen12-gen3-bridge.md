---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - pokemon-gen12-gen3-bridge-original-hardware/
last-verified-commit: d08a011
stato: decisione aperta, lavoro comune avviabile
---

# Sottoprogetto: ponte Pokemon da Gen 1 e 2 verso Gen 3 su hardware originale

Lo stato canonico di questo track e' questo file, insieme alla riga che lo riguarda in `memory/index.md`. L'handoff di ricerca non esiste piu': la sua conoscenza e' stata verificata sul sorgente e assorbita nella referenza `DATA-FORMATS_Gen1-Gen2-Gen3.md` e nel percorso di studio sotto `docs/`, per ADR-013.

Obiettivo: costruire un tool che trasferisca Pokemon dalle generazioni 1 e 2 alla generazione 3 su hardware originale, un ponte che ufficialmente non esiste perche' Nintendo non lo ha mai fornito.

## Dove siamo

Il formato dei dati delle tre generazioni e' documentato byte per byte e verificato sul disassemblato, non sull'enciclopedia, in `DATA-FORMATS_Gen1-Gen2-Gen3.md`. Sono chiusi undici punti che erano aperti o dubbi, fra cui l'ordine dei nibble dei DV, l'algoritmo del checksum di Gen 3, la dimensione del blocco di scambio e il modo in cui Poke Transporter GB ottiene l'esecuzione di codice, che avviene sul cavo e non richiede alcun setup lato giocatore. Due affermazioni dell'handoff di ricerca risultano corrette solo in parte: il PCCS documenta quattro metodi di conversione ma nel codice ne implementa uno, e l'impossibilita' di emulare riguarda il ponte fra Game Boy e Game Boy Advance, non il collegamento fra due Game Boy, che si collauda su BGB via TCP. Esiste il codice del lato Game Boy, in `pokebridge/`: primitivi, lettori e scrittori di generazione 1 e 2 per box, squadra e liste di squadra, e transcodifica del testo sulle tabelle generate. Sessantatre prove passano, la portante essendo la simmetria fra lettura e riscrittura su buffer casuali con seme fissato. Scrivere il codice ha fatto emergere un errore in piu' nella referenza, cioe' la dimensione della lista della squadra Gen 1, che e' 404 byte e non 194: la fonte aveva letto 0x194 come decimale.

Questo e' l'unico dei quattro sottoprogetti destinato a diventare software vero. Quando lo diventera' si riapre il gate del server MCP code-context, e diventa sensato un `CLAUDE.md` annidato in questa cartella con le sole convenzioni di build, lint e test, senza stato.

## Prossimo passo concreto

Il lettore e scrittore della struttura di generazione 3, che e' l'unica delle tre a essere cifrata, permutata e protetta da un checksum il cui errore trasforma il Pokemon in un Uovo Difettoso. L'ordine di costruzione e' vincolato e va rispettato nel codice: il valore di personalita' si decide per primo, perche' e' anche chiave di cifratura e selettore della permutazione. Il lato Game Boy e' fatto e collaudato, e resta comune a tutte e quattro le opzioni di ADR-008. La discovery hardware serve solo all'ultimo tratto e la lista delle domande sta in `docs/10-multiboot-hardware.md`.

## Decisione aperta, registrata come ADR-008

Le quattro opzioni sono ancora tutte in piedi e nessuna e' stata scelta, ma il loro costo relativo e' cambiato ed e' analizzato in `docs/30-opzioni-implementative.md`. Il punto nuovo e' che l'opzione A non e' piu' a costo zero di sviluppo, perche' la conversione fedele delle statistiche non esiste in nessuna implementazione pubblica e va scritta comunque, e che gli strati di formato e conversione sono identici in tutte e quattro, quindi si possono costruire prima della decisione.

## Limite noto delle prove attuali

La prova di simmetria fra lettura e riscrittura e' forte ma invariante rispetto a una permutazione di etichette: se due campi della stessa larghezza fossero scambiati fra loro, per esempio tipo 1 con tipo 2 o due delle cinque Stat Experience, la simmetria continuerebbe a valere. Le difese attuali sono parziali, cioe' un caso costruito a mano che verifica alcuni offset e il fatto che gli offset vengano dal disassemblato. La difesa che chiude il cerchio e' il confronto con un dato reale, e il controllo che costa meno e' aprire un salvataggio con `PKHeX` e confrontare campo per campo con cio' che dichiara `pokebridge`. Il ragionamento completo, con l'inventario di cio' che non e' stato verificato, sta in `docs/23-prove-eseguite.md`.

## Avvertenze da non perdere

Il backup dei salvataggi e' obbligatorio prima di qualsiasi tentativo. Il trasferimento e' a senso unico e distruttivo sulla sorgente, cioe' il Pokemon viene rimosso dal gioco di partenza, e modifica entrambi i salvataggi. Le cartucce bootleg causano la perdita dei Pokemon trasferiti, e la ragione tecnica e' che il payload contiene indirizzi assoluti tarati su una ROM precisa. La verifica finale del ponte richiede hardware reale, mentre il protocollo del cavo fra due Game Boy si collauda su emulatore.
