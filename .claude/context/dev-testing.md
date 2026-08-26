---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
  - pokemon-gen12-gen3-bridge-original-hardware/
last-verified-commit: 7696c46
---

# Sviluppo e verifica

Il protocollo di verifica di questo progetto ha due meta' che funzionano in modo opposto, e vale la pena dirle separate perche' confonderle porta a fidarsi della meta' sbagliata. La prima e' software e da' un riscontro immediato e ripetibile: il pacchetto `pokebridge` del sottoprogetto del ponte ha una suite di prove automatiche, quindi l'affermazione che questo progetto non abbia test, vera fino al 2026-08-25, non lo e' piu'. La seconda e' hardware, dove l'errore e' irreversibile, il feedback non e' istantaneo e nessun test automatico esiste ne' potra' esistere: quella meta' e' un protocollo scritto da rispettare a mano, ed e' la ragione per cui questa scheda esiste.

## Il principio

Una operazione su hardware si considera riuscita solo quando e' stata riletta, non quando il software dice che e' andata bene. Questo vale a ogni livello: un dump si verifica confrontando la dimensione attesa e riaprendo il file, una scrittura su cartuccia si verifica rileggendola e confrontando i byte, una modifica al salvataggio si verifica accendendo la console e guardando lo stato del gioco. Le tre verifiche non sono ridondanti perche' falliscono in modi diversi.

## Verifica automatica del codice del ponte

Le prove del pacchetto `pokebridge` si lanciano con `python tests/run_tests.py` dalla cartella `pokemon-gen12-gen3-bridge-original-hardware/`, non richiedono nulla di installato oltre la libreria standard e girano in una frazione di secondo. Alla verifica del 2026-08-26 sono 63 e passano tutte. Il numero va riletto dall'esecuzione e non copiato da qui: una scheda che dichiara un conteggio piu' alto di quello reale nasconde esattamente cio' che dovrebbe segnalare.

La prova portante e' la simmetria fra lettura e riscrittura, verificata su cinquecento buffer casuali con seme fissato per ciascuna delle sei forme di struttura, cioe' box, squadra e lista di squadra per entrambe le generazioni. E' una sola proprieta' e cattura un intero genere di errori, perche' un offset sbagliato, un ordine di byte invertito, un nibble letto dalla meta' sbagliata o un campo dimenticato la rompono tutti. Il ragionamento sta in `docs/21-collaudo.md`.

Va dichiarato anche cio' che quella prova non copre, perche' e' il punto in cui la fiducia va calibrata. La simmetria e' invariante rispetto a una permutazione di etichette: se due campi della stessa larghezza fossero scambiati fra loro, per esempio i due tipi o due delle cinque Stat Experience, continuerebbe a valere identica. Le difese attuali sono parziali, cioe' un caso costruito a mano che verifica alcuni offset e il fatto che gli offset vengano dal disassemblato e non da una fonte secondaria. La difesa che chiude il cerchio e' il confronto con un dato reale, e il controllo che costa meno e' aprire un salvataggio con `PKHeX` e confrontare campo per campo con cio' che `pokebridge` dichiara. L'inventario di cio' che non e' stato verificato sta in `docs/23-prove-eseguite.md`.

Il generatore delle tabelle di codifica dei caratteri porta la sua verifica dentro di se' e va citato qui perche' e' il modello da imitare: `tools/extract_charmaps.py` si rifiuta di scrivere se le sentinelle di controllo non tornano, quindi una tabella sbagliata non arriva mai su disco. Le tabelle in `data/` non si correggono a mano, si rigenerano.

## Protocollo per il sottoprogetto Smeraldo

Prima di qualunque scrittura si fa il backup del salvataggio in doppia copia su due percorsi distinti, e si verifica che entrambe le copie si aprano. Si registra il checksum del file originale, perche' e' l'unico riferimento che permette dopo di dire se la cartuccia e' tornata allo stato di partenza. Si apre il backup in PKHeX in sola lettura, per fotografare l'entita' del bug prima di decidere cosa correggere: e' lo step in cui si stabilisce quali slot e quali oggetti della tasca Strumenti Base vanno toccati, decisione oggi non presa perche' non presa e' l'unica risposta onesta finche' nessuno ha visto il contenuto. Si modifica, si riscrive, si rilegge, si confronta, e solo alla fine si accende il gioco.

Il criterio di successo dello step corrente e' piu' semplice e va chiuso prima di tutto il resto: in Gestione Dispositivi, sotto "Porte (COM e LPT)", deve comparire una voce USB-SERIAL CH340 con il suo numero di porta, senza punto esclamativo giallo.

## Protocollo per il sottoprogetto 3DS

Un dump si considera completato quando il file esiste in `/gm9/out/` sulla SD, ha una dimensione coerente con la cartuccia, ed e' stato trasferito sul disco del PC. Per le cartucce 3DS pubblicate dopo il 2014 la decrittazione richiede un file di seed generato con SEEDconv, e il sintomo di un seed mancante e' un errore esplicito di decrittazione, gia' incontrato e risolto su Omega Ruby: e' documentato nella sezione 5.4 dell'handoff e non va ridiagnosticato da zero.

## Riscontri visivi

Diversi passaggi di questo progetto sono verificabili solo guardando lo schermo di una console, che l'agente non puo' osservare. La regola `rules/manual-screenshots.md` copre il caso: quando serve un riscontro visivo lo si chiede esplicitamente e lo si legge. Gli screenshot che ne risultano restano in `_notes/`, non tracciati, per la politica sui media.
