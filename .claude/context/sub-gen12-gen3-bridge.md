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

Il formato dei dati delle tre generazioni e' documentato byte per byte e verificato sul disassemblato, non sull'enciclopedia, in `DATA-FORMATS_Gen1-Gen2-Gen3.md`. Sono chiusi undici punti che erano aperti o dubbi, fra cui l'ordine dei nibble dei DV, l'algoritmo del checksum di Gen 3, la dimensione del blocco di scambio e il modo in cui Poke Transporter GB ottiene l'esecuzione di codice, che avviene sul cavo e non richiede alcun setup lato giocatore. Due affermazioni dell'handoff di ricerca risultano corrette solo in parte: il PCCS documenta quattro metodi di conversione ma nel codice ne implementa uno, e l'impossibilita' di emulare riguarda il ponte fra Game Boy e Game Boy Advance, non il collegamento fra due Game Boy, che si collauda su BGB via TCP. Esistono le prime due unita' di codice, il generatore delle tabelle caratteri e le tabelle che produce.

Questo e' l'unico dei quattro sottoprogetti destinato a diventare software vero. Quando lo diventera' si riapre il gate del server MCP code-context, e diventa sensato un `CLAUDE.md` annidato in questa cartella con le sole convenzioni di build, lint e test, senza stato.

## Prossimo passo concreto

I tre lettori e scrittori delle strutture Pokemon, collaudati con la prova di simmetria fra lettura e riscrittura su dati sintetici. E' il lavoro comune a tutte e quattro le opzioni di ADR-008, quindi non dipende dalla decisione e non e' bloccato dalla discovery hardware, che resta da fare e serve solo per l'ultimo tratto. La lista delle domande di discovery sta in `docs/10-multiboot-hardware.md`.

## Decisione aperta, registrata come ADR-008

Le quattro opzioni sono ancora tutte in piedi e nessuna e' stata scelta, ma il loro costo relativo e' cambiato ed e' analizzato in `docs/30-opzioni-implementative.md`. Il punto nuovo e' che l'opzione A non e' piu' a costo zero di sviluppo, perche' la conversione fedele delle statistiche non esiste in nessuna implementazione pubblica e va scritta comunque, e che gli strati di formato e conversione sono identici in tutte e quattro, quindi si possono costruire prima della decisione.

## Avvertenze da non perdere

Il backup dei salvataggi e' obbligatorio prima di qualsiasi tentativo. Il trasferimento e' a senso unico e distruttivo sulla sorgente, cioe' il Pokemon viene rimosso dal gioco di partenza, e modifica entrambi i salvataggi. Le cartucce bootleg causano la perdita dei Pokemon trasferiti, e la ragione tecnica e' che il payload contiene indirizzi assoluti tarati su una ROM precisa. La verifica finale del ponte richiede hardware reale, mentre il protocollo del cavo fra due Game Boy si collauda su emulatore.
