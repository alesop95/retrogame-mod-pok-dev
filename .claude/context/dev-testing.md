---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
  - pokemon-gen12-gen3-bridge-original-hardware/
  - recreate-pokemon-distributions-events/
  - poke-ace/
  - generation-from-switch/
  - cart-battery-restoration/
  - pokedex-home-completo/
  - gba-switch-pokemon-trading/
  - poke-automation-study/
last-verified-commit: 80fac1f
---

# Sviluppo e verifica

Il protocollo di verifica di questo progetto ha due metà che funzionano in modo opposto, e vale la pena dirle separate perché confonderle porta a fidarsi della metà sbagliata. La prima è software e dà un riscontro immediato e ripetibile: il pacchetto `pokebridge` del sottoprogetto del ponte ha una suite di prove automatiche, quindi l'affermazione che questo progetto non abbia test, vera fino al 2026-08-25, non lo è più. La seconda è hardware, dove l'errore è irreversibile, il feedback non è istantaneo e nessun test automatico esiste né potrà esistere: quella metà è un protocollo scritto da rispettare a mano, ed è la ragione per cui questa scheda esiste.

## Il principio

Una operazione su hardware si considera riuscita solo quando è stata riletta, non quando il software dice che è andata bene. Questo vale a ogni livello: un dump si verifica confrontando la dimensione attesa e riaprendo il file, una scrittura su cartuccia si verifica rileggendola e confrontando i byte, una modifica al salvataggio si verifica accendendo la console e guardando lo stato del gioco. Le tre verifiche non sono ridondanti perché falliscono in modi diversi.

## Verifica automatica del codice del ponte

Le prove del pacchetto `pokebridge` si lanciano con `python tests/run_tests.py` dalla cartella `pokemon-gen12-gen3-bridge-original-hardware/`, non richiedono nulla di installato oltre la libreria standard e girano in una frazione di secondo. Alla verifica del 2026-09-09 sono 206 e passano tutte, cresciute da 114 con i moduli degli eventi e dello strato del salvataggio. Il numero va riletto dall'esecuzione e non copiato da qui: una scheda che dichiara un conteggio più alto di quello reale nasconde esattamente ciò che dovrebbe segnalare.

La prova portante è la simmetria fra lettura e riscrittura, verificata su cinquecento buffer casuali con seme fissato per ciascuna delle sei forme di struttura, cioè box, squadra e lista di squadra per entrambe le generazioni. È una sola proprietà e cattura un intero genere di errori, perché un offset sbagliato, un ordine di byte invertito, un nibble letto dalla metà sbagliata o un campo dimenticato la rompono tutti. Il ragionamento sta in `docs/21-collaudo.md`.

Va dichiarato anche ciò che quella prova non copre, perché è il punto in cui la fiducia va calibrata. La simmetria è invariante rispetto a una permutazione di etichette: se due campi della stessa larghezza fossero scambiati fra loro, per esempio i due tipi o due delle cinque Stat Experience, continuerebbe a valere identica. Le difese attuali sono parziali, cioè un caso costruito a mano che verifica alcuni offset e il fatto che gli offset vengano dal disassemblato e non da una fonte secondaria. La difesa che chiude il cerchio è il confronto con un dato reale, e il controllo che costa meno è aprire un salvataggio con `PKHeX` e confrontare campo per campo con ciò che `pokebridge` dichiara. L'inventario di ciò che non è stato verificato sta in `docs/23-prove-eseguite.md`.

Il generatore delle tabelle di codifica dei caratteri porta la sua verifica dentro di sé e va citato qui perché è il modello da imitare: `tools/extract_charmaps.py` si rifiuta di scrivere se le sentinelle di controllo non tornano, quindi una tabella sbagliata non arriva mai su disco. Le tabelle in `data/` non si correggono a mano, si rigenerano.

## Protocollo per il sottoprogetto Smeraldo

Prima di qualunque scrittura si fa il backup del salvataggio in doppia copia su due percorsi distinti (dischi fisicamente diversi, non due cartelle dello stesso disco), e si verifica che le due copie coincidano byte per byte sull'hash SHA-256. Il file di backup si diagnostica in sola lettura con `tools/emerald_bag_decode.py`, che smaschera la tasca (le quantità sono in XOR con una chiave specifica del salvataggio) e riferisce le anomalie con il loro offset. La correzione si applica con uno script Python deterministico e specifico del giro (`tools/emerald_bag_fix.py` per il primo, `tools/emerald_bag_fix_round2.py` per il secondo), mai a mano in un editor: lo script produce un file nuovo, mai sovrascrive il backup in ingresso, e il file prodotto si rilegge con lo stesso decodificatore per confermare zero anomalie nuove e con un confronto byte per byte contro l'originale per confermare che nessun byte fuori dalle sezioni dichiarate sia stato toccato. Solo allora si scrive sulla cartuccia vera con FlashGBX, e subito dopo, senza disconnettere, se ne rilegge il contenuto per un secondo confronto byte per byte indipendente dalla dichiarazione di successo del software. L'ultimo passo, mai saltato, è il controllo visivo in gioco con una checklist scritta prima di accendere la console, non improvvisata guardando lo schermo.

Verificato su due giri completi, entrambi scritti e riletti con hash identico il 2026-09-17: il metodo tiene, e i soli difetti trovati sono stati assunzioni sbagliate nella diagnosi (un ordine di enumerazione copiato da un'enciclopedia invece che dal sorgente, una specie duplicata contata come singola), mai un errore dello script o della scrittura fisica.

## Protocollo per la ricreazione delle distribuzioni

Vale il protocollo dello Smeraldo, perché l'operazione è la stessa, cioè scrivere sul salvataggio di una cartuccia originale, e vi si aggiungono due passi propri di questo track. Il primo precede ogni scrittura e viene da una fonte: se il salvataggio contiene già una carta meraviglia, quella va esportata e conservata prima di sovrascrivere qualunque cosa, perché può essere un evento che la comunità non ha ancora preservato, e in quel caso la sovrascrittura distrugge un dato unico invece di un dato ricostruibile. Il secondo segue la scrittura e riguarda la fedeltà: un esemplare ricreato si verifica confrontandone i campi con quelli documentati per l'evento originale, e la verifica utile è quella di un verificatore di legittimità indipendente, perché è l'unico controllo capace di dire se il metodo di generazione sia stato riprodotto e non soltanto il risultato.

## Protocollo per il sottoprogetto 3DS

Un dump si considera completato quando il file esiste in `/gm9/out/` sulla SD, ha una dimensione coerente con la cartuccia, ed è stato trasferito sul disco del PC. Per le cartucce 3DS pubblicate dopo il 2014 la decrittazione richiede un file di seed generato con SEEDconv, e il sintomo di un seed mancante è un errore esplicito di decrittazione, già incontrato e risolto su Omega Ruby: è documentato nella sezione 5.4 dell'handoff e non va ridiagnosticato da zero.

## Riscontri visivi

Diversi passaggi di questo progetto sono verificabili solo guardando lo schermo di una console, che l'agente non può osservare. La regola `rules/manual-screenshots.md` copre il caso: quando serve un riscontro visivo lo si chiede esplicitamente e lo si legge. Gli screenshot che ne risultano restano in `_notes/`, non tracciati, per la politica sui media.
