# Sottoprogetto: correzione dell'inventario corrotto di Pokemon Smeraldo

Riparare la tasca oggetti corrotta su una cartuccia originale di Pokemon Smeraldo, agendo sul salvataggio estratto fisicamente dalla cartuccia con un lettore invece che con codici trucco. È un runbook operativo su hardware fisico, dove gli errori sono irreversibili, non un progetto software.

## Che cosa c'è in questa cartella

Il documento di riferimento è `handoff/HANDOFF_progetto_smeraldo.md`: contiene il problema di partenza, la strada dell'Action Replay e le ragioni per cui è stata chiusa, la pipeline attiva basata su GBxCart RW e FlashGBX, le scelte di hardware e software con le loro motivazioni, la sequenza di setup su Windows, il dettaglio dello step corrente sui driver CH340 e l'elenco esplicito di ciò che non è ancora stato fatto.

In `tools/emerald_bag_decode.py` c'è lo strumento di diagnosi, che si usa appena esiste un dump. Non scrive nulla sul salvataggio: valida firma e checksum di ogni sezione, sceglie lo slot più recente, ricompone il blocco di salvataggio, identifica il gioco confrontando le prove di tre candidati, smaschera le quantità dello zaino e riferisce le anomalie che sa riconoscere.

L'identificazione del gioco esiste per una ragione trovata in una discussione di Project Pokemon: un editor che identifica un salvataggio di Smeraldo come Rubino o Zaffiro fa finire gli oggetti negli slot sbagliati, perché applica la maschera sbagliata. Lo strumento quindi non si fida del parametro `--game` e per default lo deduce, stampando le prove di tutti i candidati.

## Il fatto tecnico che cambia la diagnosi

In Smeraldo le quantità degli oggetti nello zaino e il denaro non stanno in chiaro: sono in XOR con una chiave di sicurezza a 32 bit che sta nella sezione 0 del salvataggio all'offset 0x00AC. Le quantità del deposito PC invece sono in chiaro, e Rubino e Zaffiro non mascherano nulla. La verifica viene dal sorgente di `pret/pokeemerald`, dove `GetBagItemQuantity` applica la maschera e `GetPCItemQuantity` no.

Ne segue una conseguenza che va tenuta presente prima di guardare il dump: una quantità assurda letta in chiaro dallo zaino non è una prova di corruzione, è l'aspetto normale di un dato mascherato. Solo dopo lo smascheramento si può dire che cosa sia davvero corrotto.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| la procedura operativa e lo stato del setup | `handoff/HANDOFF_progetto_smeraldo.md` |
| la struttura del salvataggio Gen 3, sezione per sezione | `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`, sezioni 5 e 6 |
| perché esistono checksum e cifratura, spiegato | `docs/03-integrita-checksum.md` e `docs/04-cifratura-gen3.md` |
| come si usa lo strumento di diagnosi | `docs/22-strumenti.md` |
| le fonti, compresi i thread su casi di corruzione reali | `SOURCES.md` alla radice, colonna SME |
| a che punto è il track e qual è il prossimo passo | `.claude/context/sub-smeraldo-save-fix.md` |

Lo stato canonico del track vive nella scheda, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`. Questo file dice cos'è il sottoprogetto; quelli dicono a che punto è.

## L'avvertenza che non si negozia

Nessuna scrittura sulla cartuccia avviene senza un backup del salvataggio originale in doppia copia su due percorsi distinti, verificato leggibile, e nessuna scrittura si considera riuscita senza aver riletto i byte e confrontati con quelli che si intendeva scrivere. È la regola `.claude/rules/hardware-and-perimeter.md`, ed è normativa perché un salvataggio di vent'anni non ha una seconda occasione.
