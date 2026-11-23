# Controllo dei lotti contro il foglio delle specie precedenti a Switch

> Documento autorato del 2026-11-23, su richiesta del proprietario. È un controllo dei lotti già in HOME, per vedere se manca ancora qualcosa. Le fonti sono registrate in `SOURCES.md`, nella sezione «Le fonti del 2026-11-23».

## La domanda e il perimetro

Il foglio di community di Tezzeret_the_Lemur, derivato da «List of Pokémon by availability» di Bulbapedia, tiene una riga per ogni specie da 1 a 807 e per alcune forme. Lo scopo dichiarato dall'autore è avere in HOME un esemplare senza marchio d'origine, cioè nato in un gioco precedente a Switch. La domanda per questo progetto è se i nostri lotti diano almeno un esemplare d'origine pre-Switch a ogni riga del foglio.

Il confronto si è fatto con uno script di sessione, sul `.xlsx` esportato il 2026-11-23. Da una parte la scheda «Origin Mark Tracking», con numero, nome e forma. Dall'altra tutte le righe dei pedigree in `pokedex-home-completo/pedigree/*.md`, cioè 7575 righe con FINALE, che è escluso. FINALE va nelle cartucce Game Boy dopo la chiusura di Bank e non in HOME. Le righe sono confrontate per numero di specie e per la colonna «Forma». La colonna «Gioco d'origine» dei pedigree contiene solo giochi dalla prima alla settima generazione, Colosseum e XD; il più frequente è Ultrasole con 1013 righe. Quindi ogni esemplare dei lotti è d'origine pre-Switch. Il controllo non guarda le mosse, che l'autore stesso esclude, né il luogo d'incontro nella regione d'origine. Conta i pedigree, non gli esemplari visti in HOME: i 996 vecchi da liberare hanno ciascuno un sostituto della stessa specie, quindi non spostano l'esito.

## L'esito

Le specie sono tutte coperte. Il foglio ha 806 numeri, perché nella scheda di tracciamento manca Hawlucha (701), che pure compare nella tabella di Bulbapedia incollata accanto: è una svista dell'autore. I pedigree coprono tutti i numeri da 1 a 807, Hawlucha compreso.

Delle 56 righe di forme, solo tre non hanno un corrispondente nei pedigree, e nessuna è una lacuna dei lotti:

- Pichu dalle orecchie a punta: non si trasferisce fuori dalla quarta generazione per nessuna via, come già scritto in `CATENA-DI-TRASFERIMENTO.md` alla riga 60.
- Magearna Colore Originale: è un dono di HOME, già aperto come voce della fase Switch (riga 103 dell'archivio del registro, in `.claude/memory/pending.md`).
- Pikachu con il berretto «World Cap»: è un evento di Spada e Scudo, quindi non pre-Switch, anche se il foglio lo elenca.

Le altre forme del foglio ci sono tutte nei pedigree: le 18 forme di Alola, Shellos e Gastrodon Est, Basculin Lineablu, le quattro stagioni di Deerling e Sawsbuck, i 20 motivi di Vivillon (il motivo «Icy Snow» del foglio è la forma 0, che nei pedigree non porta etichetta), Greninja di Ash, Meowstic femmina, le tre forme di Lycanroc e i berretti Originale e Compagni di Pikachu.

## Che cosa non dice

Il foglio enumera specie e poche forme, non le forme da collezione che il progetto conta, come Unown, Spinda, i fiocchi, le sfere e i doni. Per quelle valgono `CHECKLIST-COMPLETA.md`, `CONFRONTO-FOGLIO-LIVINGDEX.md` e `CONFRONTO-LIVINGDEX-POKEPC.md`. Un esito pulito qui vuol dire che nessuna specie precedente a Switch è rimasta senza un esemplare dei lotti. Non vuol dire che la collezione sia completa.
