---
tipo: nota di studio
livello: avanzato
tags: [conversione, vincoli, pccs, valore-di-personalita]
up: "[[index]]"
vedi_anche: ["[[06-identita-pokemon]]", "[[04-cifratura-gen3]]", "[[20-architettura-codice]]", "[[30-opzioni-implementative]]"]
---

# La conversione come problema di soddisfacimento di vincoli

Questa e' la nota centrale del progetto. Tutto il resto e' meccanica: offset da leggere, checksum da ricalcolare, tabelle da tradurre. Qui invece c'e' un problema che non ha una soluzione unica, e capire perche' non ce l'ha e' il modo per scegliere consapevolmente la propria.

## L'enunciato

Un Pokemon di generazione 3 richiede campi che in generazione 1 e 2 non esistono. Non e' un problema di formato, e' un problema di informazione: la natura di un Pokemon catturato in Rosso non e' registrata da nessuna parte, perche' in Rosso il concetto di natura non era stato inventato. Serve quindi inventarla.

Il problema e' che questi campi non sono indipendenti. Derivano tutti dallo stesso numero da 32 bit, il valore di personalita', secondo formule fissate dal gioco che nessun tool puo' cambiare. La natura e' il valore modulo 25. Il sesso confronta il byte meno significativo con la soglia della specie. Lo slot di abilita' e' il bit meno significativo. La lettera di Unown compone i due bit meno significativi di ciascuno dei quattro byte e prende il modulo 28. La lucentezza si ha quando lo XOR fra ID visibile, ID segreto e le due meta' del valore di personalita' e' minore di 8.

Quindi non si scelgono i campi: si scegli un numero, e i campi ne conseguono. E poiche' alcuni di quei campi devono corrispondere a proprieta' del Pokemon originale, per esempio il sesso, che in generazione 2 dipende dal DV di Attacco, e la lettera di Unown, che dipende dai DV, il numero non e' libero. Va cercato.

## Come lo risolve l'implementazione di riferimento

Il PCCS lo risolve nel modo piu' diretto che esista, cioe' campionamento con rifiuto: estrae un candidato dal generatore pseudocasuale, calcola cio' che ne deriva, e lo scarta se non corrisponde, ripetendo finche' non trova un valore che soddisfa tutti i vincoli insieme.

```cpp
    do
    {
        seedA = newPkmn->getNextRand_u16();
        seedB = newPkmn->getNextRand_u16();
        pid = seedA | (seedB << 16);
        newPkmn->setPersonalityValue(pid);
    } while (!(
        newPkmn->getAbilityFromPersonalityValue() == newPkmn->internalAbility &&
        newPkmn->getUnownLetter() == newPkmn->internalUnownLetter &&
        newPkmn->getNature() == newPkmn->internalNature &&
        newPkmn->getGender() == newPkmn->internalGender &&
        newPkmn->getSize() == newPkmn->internalSize));
```

E' inefficiente in senso teorico e perfettamente adeguato in pratica, perche' i vincoli sono pochi e poco correlati, quindi la probabilita' che un candidato passi e' abbastanza alta perche' il ciclo termini in fretta. Vale la pena notare che questa e' anche la soluzione piu' robusta: costruire il valore per bit, soddisfacendo un vincolo per volta, sarebbe piu' veloce e molto piu' facile da sbagliare, perche' i vincoli si sovrappongono sugli stessi bit.

## Il vincolo che manca dalla lista, e la sua eleganza

Nella condizione del ciclo la lucentezza non compare, e questa e' la parte piu' istruttiva di tutto il meccanismo.

L'ID dell'allenatore in generazione 1 e 2 e' a 16 bit. In generazione 3 e' a 32, cioe' un ID visibile piu' un ID segreto. L'ID segreto e' quindi un valore che la conversione deve inventare in ogni caso, perche' nella sorgente non esiste. E poiche' la condizione di lucentezza dipende dallo XOR di quattro mezzi valori, di cui tre sono ormai fissati, l'ID segreto e' esattamente la variabile che decide la lucentezza a valle di tutto il resto.

```cpp
    u16 shinyTest = TID ^ (PV & 0xFFFF) ^ (PV >> 16);
    if (getIsShiny())        newPkmn->setSecretID(shinyTest);   // XOR nullo, lucente
    else if (shinyTest < 8)  newPkmn->setSecretID(51691);       // era lucente per caso, si rompe
    else                     newPkmn->setSecretID(0);
```

C'e' una lezione generale, oltre al fatto tecnico. Un problema di vincoli sovradeterminato non si risolve rendendo il solutore piu' furbo: si risolve trovando il grado di liberta' che nessuno aveva contato. Qui il grado di liberta' era nascosto in un campo che si sarebbe potuto riempire con uno zero senza che nessuno protestasse.

## La circostanza fortunata

Resta da spiegare perche' tutto questo sia possibile, perche' non era garantito. In generazione 3 i valori individuali sono memorizzati in un campo proprio e non derivano dal valore di personalita'. Dalla generazione 4 in poi il legame fra i due passa per il generatore pseudocasuale del metodo di incontro, e una coppia arbitraria di valore di personalita' e valori individuali diventa riconoscibile come impossibile, cioe' illegale agli occhi di qualsiasi verificatore.

In generazione 3 quel legame nel dato salvato non c'e'. Un convertitore puo' quindi scegliere i valori individuali per conservare le statistiche e il valore di personalita' per conservare sesso, lucentezza e forma, in modo indipendente. E' precisamente questa indipendenza a rendere fattibile una conversione fedele, ed e' la ragione tecnica per cui il ponte esiste verso la generazione 3 e non verso una successiva.

## Cosa il codice pubblicato fa davvero, e cosa non fa

Qui c'e' una scoperta che vale la pena tenere in evidenza, perche' cambia la stima del lavoro residuo. Il README del PCCS documenta quattro metodi di conversione, chiamati ORIGINAL, FAITHFUL, LEGAL e VIRTUAL, con una tabella campo per campo che descrive come ciascuno tratta ogni dato. Nel codice sorgente della release corrente i nomi di quei quattro metodi non compaiono affatto, e il comportamento implementato e' quello del solo ORIGINAL: i valori individuali sono generati casualmente e gli EV sono azzerati.

La tabella dei quattro metodi e' quindi una specifica, non la descrizione di codice esistente. Chi vuole la conversione fedele delle statistiche, cioe' il raddoppio dei DV in IV e la conversione della Stat Experience in EV entro il tetto di 510, deve implementarla, in qualunque delle quattro opzioni implementative si scelga di lavorare. Non e' un pezzo che si eredita adottando una libreria.

## La Stat Experience verso gli EV, e una derivazione che non e' una citazione

Questa sezione va letta con l'etichetta che porta: cio' che segue e' una derivazione fatta qui, fondata su un dato di fonte e su come sono scritte le due formule, e non e' la trascrizione di una formula che qualcuno abbia pubblicato. Resta da verificare contro un'implementazione, e finche' non lo e' non entra in codice.

Il problema e' quello dichiarato aperto in `pending.md`: le generazioni 1 e 2 misurano l'allenamento con la Stat Experience, un valore a 16 bit per statistica, mentre la generazione 3 lo misura con gli Effort Value, un valore a 8 bit per statistica con un tetto individuale di 252 e un tetto complessivo di 510. Nessuna implementazione pubblica converte l'una negli altri, e la ricerca nel canale dei disassemblati fatta il 2026-08-26 non ha trovato la formula, perche' quel canale discute la modifica dei giochi e non la conversione fra generazioni.

Ha trovato pero' il dato da cui la conversione si deduce, ed e' un'affermazione precisa di un partecipante che stava ottimizzando la funzione di radice quadrata di un disassemblato: per raggiungere il massimo di 63 punti di statistica al livello 100 non serve arrivare a 65535 di Stat Experience, perche' bastano 63 per 4 tutto al quadrato, cioe' 63504, e per come il calcolo e' realizzato ne bastano in pratica 63002.

Il numero 63504 e' quello che chiude il ragionamento, perche' la sua radice quadrata e' 252. Da qui la struttura si vede.

Nelle generazioni 1 e 2 il contributo dell'allenamento a una statistica passa per la radice quadrata della Stat Experience divisa per quattro, e satura a 63 punti. Nella generazione 3 il contributo passa per gli EV divisi per quattro, e satura anch'esso a 63 punti perche' il tetto per statistica e' 252. Le due formule hanno quindi la stessa forma e lo stesso tetto, e differiscono soltanto per il fatto che una prende la radice quadrata del valore memorizzato e l'altra lo prende cosi' com'e'. La conversione che conserva il contributo alla statistica e' allora la radice quadrata, cioe' un EV pari alla parte intera della radice quadrata della Stat Experience, limitato a 252.

La verifica ai bordi torna e vale la pena farla, perche' e' l'unica prova che si puo' fare senza codice. Una Stat Experience di 63504 diventa un EV di 252, cioe' il massimo diventa il massimo. Una Stat Experience nulla diventa un EV nullo. Una Stat Experience di 65535, che e' il massimo rappresentabile e sta sopra la saturazione, darebbe una radice di 255 e viene tagliata a 252, che e' corretto perche' entrambi i valori corrispondono ai 63 punti di saturazione. Il che significa anche che l'intervallo fra 63504 e 65535 e' informazione che la generazione 3 non e' in grado di rappresentare, e che quindi si perde: e' una perdita reale ma innocua, perche' non ha effetto su alcuna statistica.

Resta il vincolo complessivo, e non e' un dettaglio. La generazione 3 impone che la somma degli EV non superi 510, mentre le generazioni 1 e 2 non impongono alcun tetto complessivo alla Stat Experience: un esemplare allenato a lungo puo' avere tutte e cinque le Stat Experience al massimo, che convertite darebbero 252 per cinque, cioe' 1260, due volte e mezzo il consentito. La conversione fedele delle statistiche e' quindi impossibile in generale, e questo non e' un difetto della formula ma una proprieta' del problema: la generazione 3 ha deliberatamente reso l'allenamento un gioco a somma zero, dove migliorare una statistica costa un'altra, e le generazioni precedenti no.

Ne segue che la conversione ha bisogno di una politica dichiarata per il caso in cui il totale sfori, e quella politica e' una scelta discutibile nel senso preciso in cui questa nota usa la parola, cioe' un parametro dello strato di conversione e non una costante sepolta nel codice. Le tre politiche sensate sono ridurre in proporzione conservando i rapporti fra le statistiche, troncare secondo un ordine di priorita' dichiarato dall'utente, oppure rifiutare la conversione e chiedere una decisione. La prima conserva la forma dell'esemplare e ne abbassa il livello complessivo di allenamento, la seconda conserva alcune statistiche intatte e sacrifica le altre, la terza non decide al posto di nessuno. Nessuna delle tre e' la risposta giusta in assoluto, ed e' esattamente il genere di cosa che la tabella dei quattro metodi del PCCS avrebbe dovuto specificare.

Sul dato di partenza va detto un ultimo avvertimento. La cifra 63002 riportata dalla stessa fonte, minore di 63504, indica che l'implementazione reale del calcolo non e' esattamente la radice quadrata matematica, presumibilmente per come e' scritta la routine di approssimazione nel gioco. La derivazione qui sopra usa la radice quadrata matematica, che e' la forma pulita; se un giorno la conversione dovesse essere esatta al punto da riprodurre il comportamento del gioco anche in quel margine, la routine va letta nel disassemblato e replicata invece che approssimata. E' registrato fra i punti aperti.

## Un avvertimento sul distinguere le fonti

Nello stesso file c'e' un caso speciale che, per una specie precisa e per due impronte hash specifiche del nome dell'allenatore e del soprannome, forza tutti i DV al massimo. E' una scelta arbitraria di quella implementazione, probabilmente un omaggio, e non una regola del formato.

E' un buon promemoria del perche' la gerarchia delle fonti descritta in [[SOURCES]] mette il gioco sopra il tool: un'implementazione di riferimento dimostra che una cosa e' possibile, non che sia il modo corretto di farla.

## Cosa leggere dopo

[[20-architettura-codice]] traduce tutto questo in una struttura di moduli, e [[30-opzioni-implementative]] mostra quanto costa ciascuna delle quattro strade alla luce di quanto appena visto.
