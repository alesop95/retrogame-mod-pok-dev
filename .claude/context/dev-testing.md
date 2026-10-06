---
generated-from-commit: 8cc1798
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
  - tools/
  - scripts/
last-verified-commit: 90adea9
---

# Sviluppo e verifica

Il protocollo di verifica di questo progetto ha due metà che funzionano in modo opposto, e vale la pena dirle separate perché confonderle porta a fidarsi della metà sbagliata. La prima è software e dà un riscontro immediato e ripetibile: il pacchetto `pokebridge` del sottoprogetto del ponte ha una suite di prove automatiche, quindi l'affermazione che questo progetto non abbia test, vera fino al 2026-08-25, non lo è più. La seconda è hardware, dove l'errore è irreversibile, il feedback non è istantaneo e nessun test automatico esiste né potrà esistere: quella metà è un protocollo scritto da rispettare a mano, ed è la ragione per cui questa scheda esiste.

## Il principio

Una operazione su hardware si considera riuscita solo quando è stata riletta, non quando il software dice che è andata bene. Questo vale a ogni livello: un dump si verifica confrontando la dimensione attesa e riaprendo il file, una scrittura su cartuccia si verifica rileggendola e confrontando i byte, una modifica al salvataggio si verifica accendendo la console e guardando lo stato del gioco. Le tre verifiche non sono ridondanti perché falliscono in modi diversi.

## Verifica automatica del codice del ponte

Le prove del pacchetto `pokebridge` si lanciano con `python tests/run_tests.py` dalla cartella `pokemon-gen12-gen3-bridge-original-hardware/`, non richiedono nulla di installato oltre la libreria standard e girano in una frazione di secondo. Alla verifica del 2026-09-09 sono 206 e passano tutte, cresciute da 114 con i moduli degli eventi e dello strato del salvataggio. Il numero va riletto dall'esecuzione e non copiato da qui: una scheda che dichiara un conteggio più alto di quello reale nasconde esattamente ciò che dovrebbe segnalare. Riletto il 2026-09-29 con `python -m unittest discover -s tests`: 206 prove, tutte verdi, in 0,6 secondi.

La prova portante è la simmetria fra lettura e riscrittura, verificata su cinquecento buffer casuali con seme fissato per ciascuna delle sei forme di struttura, cioè box, squadra e lista di squadra per entrambe le generazioni. È una sola proprietà e cattura un intero genere di errori, perché un offset sbagliato, un ordine di byte invertito, un nibble letto dalla metà sbagliata o un campo dimenticato la rompono tutti. Il ragionamento sta in `docs/21-collaudo.md`.

Va dichiarato anche ciò che quella prova non copre, perché è il punto in cui la fiducia va calibrata. La simmetria è invariante rispetto a una permutazione di etichette: se due campi della stessa larghezza fossero scambiati fra loro, per esempio i due tipi o due delle cinque Stat Experience, continuerebbe a valere identica. Le difese attuali sono parziali, cioè un caso costruito a mano che verifica alcuni offset e il fatto che gli offset vengano dal disassemblato e non da una fonte secondaria. La difesa che chiude il cerchio è il confronto con un dato reale, e il controllo che costa meno è aprire un salvataggio con `PKHeX` e confrontare campo per campo con ciò che `pokebridge` dichiara. L'inventario di ciò che non è stato verificato sta in `docs/23-prove-eseguite.md`.

Il generatore delle tabelle di codifica dei caratteri porta la sua verifica dentro di sé e va citato qui perché è il modello da imitare: `pokemon-gen12-gen3-bridge-original-hardware/tools/extract_charmaps.py` si rifiuta di scrivere se le sentinelle di controllo non tornano, quindi una tabella sbagliata non arriva mai su disco. Le tabelle in `data/` non si correggono a mano, si rigenerano.

## Protocollo per il sottoprogetto Smeraldo

Prima di qualunque scrittura si fa il backup del salvataggio in doppia copia su due percorsi distinti (dischi fisicamente diversi, non due cartelle dello stesso disco), e si verifica che le due copie coincidano byte per byte sull'hash SHA-256. Il file di backup si diagnostica in sola lettura con `gba-save-extraction-smeraldo/tools/emerald_bag_decode.py`, che smaschera la tasca (le quantità sono in XOR con una chiave specifica del salvataggio) e riferisce le anomalie con il loro offset. La correzione si applica con uno script Python deterministico, mai a mano in un editor. Gli script sono cinque e ciascuno fa una sola famiglia di cose: `gba-save-extraction-smeraldo/tools/emerald_bag_fix.py` e `gba-save-extraction-smeraldo/tools/emerald_bag_fix_round2.py` per i due giri sullo zaino e sulla squadra, `gba-save-extraction-smeraldo/tools/emerald_key_item_add.py` per la sola aggiunta di un oggetto chiave, `gba-save-extraction-smeraldo/tools/emerald_event_flags_fix.py` per accendere i flag di abilitazione delle isole e `gba-save-extraction-smeraldo/tools/emerald_encounter_flags_fix.py` per spegnere quelli che dichiarano già avvenuti gli incontri. I due sui flag si leggono in sola lettura con `gba-save-extraction-smeraldo/tools/emerald_event_flags_decode.py`, che è al secondo strumento di diagnosi quello che `emerald_bag_decode.py` è al primo. Due di questi portano una precondizione che va conosciuta perché è deliberata e simmetrica: quello che accende i flag rifiuta se l'oggetto non è in tasca, e quello che li spegne rifiuta se l'isola non è raggiungibile. Vale per tutti la stessa disciplina: lo script produce un file nuovo, mai sovrascrive il backup in ingresso, e il file prodotto si rilegge con lo stesso decodificatore per confermare zero anomalie nuove e con un confronto byte per byte contro l'originale per confermare che nessun byte fuori dalle sezioni dichiarate sia stato toccato. Solo allora si scrive sulla cartuccia vera con FlashGBX, e subito dopo, senza disconnettere, se ne rilegge il contenuto per un secondo confronto byte per byte indipendente dalla dichiarazione di successo del software. L'ultimo passo, mai saltato, è il controllo visivo in gioco con una checklist scritta prima di accendere la console, non improvvisata guardando lo schermo.

Verificato su due giri completi, entrambi scritti e riletti con hash identico il 2026-09-17: il metodo tiene, e i soli difetti trovati sono stati assunzioni sbagliate nella diagnosi (un ordine di enumerazione copiato da un'enciclopedia invece che dal sorgente, una specie duplicata contata come singola), mai un errore dello script o della scrittura fisica.

Aggiornato il 2026-09-29. Il protocollo ha retto su tutte le scritture successive, registrate con impronte e percorsi in `_notes/salvataggi/cartucce/LEGGIMI.md`: i flag degli eventi il 2026-09-18, biglietti e isole il 2026-09-21, il riordino del deposito e la cartuccia completa il 2026-09-23, con il giro12 come stato attuale, e il complemento del Rubino il 2026-09-28. Gli script sotto `gba-save-extraction-smeraldo/tools/` sono ora trenta, elencati per famiglia in `STACK.md`, e la disciplina di sopra vale per ognuno. Fra la rilettura del file prodotto e la scrittura si è aggiunto un passo, nato dai difetti che solo un giudice esterno vedeva: il file si apre in PKHeX, se ne esporta il dump dei box, e si scrive solo se il rapporto di legittimità è pulito. I dump sono in `_notes/salvataggi/cartucce/smeraldo/dump-pkhex/`, dal `round 1` al `round 6`, e l'ultimo ha dato 423 legali su 423 sul giro12; il Rubino ha avuto lo stesso passo, 382 legali su 382. Il giudizio dei lotti prima della loro composizione si fa invece senza interfaccia con `tools/pkhex-giudica` sulla libreria PKHeX.Core, che scrive `recreate-pokemon-distributions-events/giudizi-pkhex-core.json`: al 2026-09-25 dà 2010 conformi su 2010, con la riserva, dichiarata nel file, che il giudizio si fa su un salvataggio vuoto e non contiene i controlli che dipendono dal salvataggio ricevente. Dopo ogni giudizio positivo il lotto si rilegge con la libreria del progetto, perché il caso dei formati di Colosseum e XD in `pokedex-home-completo/STUDIO-10` ha mostrato che un giudizio riguarda l'oggetto giudicato e non quello scritto (ADR-081).

## Protocollo per la ricreazione delle distribuzioni

Vale il protocollo dello Smeraldo, perché l'operazione è la stessa, cioè scrivere sul salvataggio di una cartuccia originale, e vi si aggiungono due passi propri di questo track. Il primo precede ogni scrittura e viene da una fonte: se il salvataggio contiene già una carta meraviglia, quella va esportata e conservata prima di sovrascrivere qualunque cosa, perché può essere un evento che la comunità non ha ancora preservato, e in quel caso la sovrascrittura distrugge un dato unico invece di un dato ricostruibile. Il secondo segue la scrittura e riguarda la fedeltà: un esemplare ricreato si verifica confrontandone i campi con quelli documentati per l'evento originale, e la verifica utile è quella di un verificatore di legittimità indipendente, perché è l'unico controllo capace di dire se il metodo di generazione sia stato riprodotto e non soltanto il risultato.

## Controlli automatici della documentazione e della memoria

Aggiunta del 2026-09-29. Oltre alla suite del ponte, il progetto ha controlli deterministici sulla documentazione, e `tools/chiudi-sessione.ps1`, cioè `chiudi`, li esegue tutti prima di un commit e si ferma se uno fallisce. Qui, dove `chiudi` cerca soltanto in `tools/`, sono nove: `md-unwrap.py --check --only-tracked`, `lint-md-commands.py`, `misura-istruzioni.py`, i tre correttori tipografici in `--check`, e dal 2026-09-29 `lint-memoria.py`, `lint-didattica.py` e `Test-Anonymization.py` (ADR-091). Altri due si lanciano a mano prima dei comandi git, come dice il `CLAUDE.md`: `aggiorna-readme.py --check` e `build-source-map.py --check`; `lint-prosa.py` segnala sui file di prosa cambiati senza bloccare. Al 2026-09-29 i tre tipografici falliscono sul debito della voce PRIMO di `pending.md`, e per questo `chiudi` è ancora bloccato. `tools/test-tipografia.py` è la prova che i correttori non tocchino gli identificatori di un file composto.

## Protocollo per il sottoprogetto 3DS

Un dump si considera completato quando il file esiste in `/gm9/out/` sulla SD, ha una dimensione coerente con la cartuccia, ed è stato trasferito sul disco del PC. Per le cartucce 3DS pubblicate dopo il 2014 la decrittazione richiede un file di seed generato con SEEDconv, e il sintomo di un seed mancante è un errore esplicito di decrittazione, già incontrato e risolto su Omega Ruby: è documentato nella sezione 5.4 dell'handoff e non va ridiagnosticato da zero.

## Riscontri visivi

Diversi passaggi di questo progetto sono verificabili solo guardando lo schermo di una console, che l'agente non può osservare. La regola `rules/manual-screenshots.md` copre il caso: quando serve un riscontro visivo lo si chiede esplicitamente e lo si legge. Gli screenshot che ne risultano restano in `_notes/`, non tracciati, per la politica sui media.
