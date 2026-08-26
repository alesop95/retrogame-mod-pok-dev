---
tipo: nota di studio
livello: avanzato
tags: [conversione, vincoli, pccs, valore-di-personalita]
up: "[[index]]"
vedi_anche: ["[[06-identita-pokemon]]", "[[04-cifratura-gen3]]", "[[20-architettura-codice]]", "[[30-opzioni-implementative]]"]
---

# La conversione come problema di soddisfacimento di vincoli

Questa è la nota centrale del progetto. Tutto il resto è meccanica: offset da leggere, checksum da ricalcolare, tabelle da tradurre. Qui invece c'è un problema che non ha una soluzione unica, e capire perché non ce l'ha è il modo per scegliere consapevolmente la propria.

## L'enunciato

Un Pokemon di generazione 3 richiede campi che in generazione 1 e 2 non esistono. Non è un problema di formato, è un problema di informazione: la natura di un Pokemon catturato in Rosso non è registrata da nessuna parte, perché in Rosso il concetto di natura non era stato inventato. Serve quindi inventarla.

Il problema è che questi campi non sono indipendenti. Derivano tutti dallo stesso numero da 32 bit, il valore di personalità, secondo formule fissate dal gioco che nessun tool può cambiare. La natura è il valore modulo 25. Il sesso confronta il byte meno significativo con la soglia della specie. Lo slot di abilità è il bit meno significativo. La lettera di Unown compone i due bit meno significativi di ciascuno dei quattro byte e prende il modulo 28. La lucentezza si ha quando lo XOR fra ID visibile, ID segreto e le due metà del valore di personalità è minore di 8.

Quindi non si scelgono i campi: si scegli un numero, e i campi ne conseguono. E poiché alcuni di quei campi devono corrispondere a proprietà del Pokemon originale, per esempio il sesso, che in generazione 2 dipende dal DV di Attacco, e la lettera di Unown, che dipende dai DV, il numero non è libero. Va cercato.

## Come lo risolve l'implementazione di riferimento

Il PCCS lo risolve nel modo più diretto che esista, cioè campionamento con rifiuto: estrae un candidato dal generatore pseudocasuale, calcola ciò che ne deriva, e lo scarta se non corrisponde, ripetendo finché non trova un valore che soddisfa tutti i vincoli insieme.

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

È inefficiente in senso teorico e perfettamente adeguato in pratica, perché i vincoli sono pochi e poco correlati, quindi la probabilità che un candidato passi è abbastanza alta perché il ciclo termini in fretta. Vale la pena notare che questa è anche la soluzione più robusta: costruire il valore per bit, soddisfacendo un vincolo per volta, sarebbe più veloce e molto più facile da sbagliare, perché i vincoli si sovrappongono sugli stessi bit.

## Il vincolo che manca dalla lista, e la sua eleganza

Nella condizione del ciclo la lucentezza non compare, e questa è la parte più istruttiva di tutto il meccanismo.

L'ID dell'allenatore in generazione 1 e 2 è a 16 bit. In generazione 3 è a 32, cioè un ID visibile più un ID segreto. L'ID segreto è quindi un valore che la conversione deve inventare in ogni caso, perché nella sorgente non esiste. E poiché la condizione di lucentezza dipende dallo XOR di quattro mezzi valori, di cui tre sono ormai fissati, l'ID segreto è esattamente la variabile che decide la lucentezza a valle di tutto il resto.

```cpp
    u16 shinyTest = TID ^ (PV & 0xFFFF) ^ (PV >> 16);
    if (getIsShiny())        newPkmn->setSecretID(shinyTest);   // XOR nullo, lucente
    else if (shinyTest < 8)  newPkmn->setSecretID(51691);       // era lucente per caso, si rompe
    else                     newPkmn->setSecretID(0);
```

C'è una lezione generale, oltre al fatto tecnico. Un problema di vincoli sovradeterminato non si risolve rendendo il solutore più furbo: si risolve trovando il grado di libertà che nessuno aveva contato. Qui il grado di libertà era nascosto in un campo che si sarebbe potuto riempire con uno zero senza che nessuno protestasse.

## La circostanza fortunata

Resta da spiegare perché tutto questo sia possibile, perché non era garantito. In generazione 3 i valori individuali sono memorizzati in un campo proprio e non derivano dal valore di personalità. Dalla generazione 4 in poi il legame fra i due passa per il generatore pseudocasuale del metodo di incontro, e una coppia arbitraria di valore di personalità e valori individuali diventa riconoscibile come impossibile, cioè illegale agli occhi di qualsiasi verificatore.

In generazione 3 quel legame nel dato salvato non c'è. Un convertitore può quindi scegliere i valori individuali per conservare le statistiche e il valore di personalità per conservare sesso, lucentezza e forma, in modo indipendente. È precisamente questa indipendenza a rendere fattibile una conversione fedele, ed è la ragione tecnica per cui il ponte esiste verso la generazione 3 e non verso una successiva.

## Cosa il codice pubblicato fa davvero, e cosa non fa

Qui c'è una scoperta che vale la pena tenere in evidenza, perché cambia la stima del lavoro residuo. Il README del PCCS documenta quattro metodi di conversione, chiamati ORIGINAL, FAITHFUL, LEGAL e VIRTUAL, con una tabella campo per campo che descrive come ciascuno tratta ogni dato. Nel codice sorgente della release corrente i nomi di quei quattro metodi non compaiono affatto, e il comportamento implementato è quello del solo ORIGINAL: i valori individuali sono generati casualmente e gli EV sono azzerati.

La tabella dei quattro metodi è quindi una specifica, non la descrizione di codice esistente. Chi vuole la conversione fedele delle statistiche, cioè il raddoppio dei DV in IV e la conversione della Stat Experience in EV entro il tetto di 510, deve implementarla, in qualunque delle quattro opzioni implementative si scelga di lavorare. Non è un pezzo che si eredita adottando una libreria.

## La Stat Experience verso gli EV, e una derivazione che non è una citazione

Questa sezione va letta con l'etichetta che porta: ciò che segue è una derivazione fatta qui, fondata su un dato di fonte e su come sono scritte le due formule, e non è la trascrizione di una formula che qualcuno abbia pubblicato. Resta da verificare contro un'implementazione, e finché non lo è non entra in codice.

Il problema è quello dichiarato aperto in `pending.md`: le generazioni 1 e 2 misurano l'allenamento con la Stat Experience, un valore a 16 bit per statistica, mentre la generazione 3 lo misura con gli Effort Value, un valore a 8 bit per statistica con un tetto individuale di 252 e un tetto complessivo di 510. Che nessuna implementazione pubblica converta l'una negli altri non è più un'affermazione ricavata da una lettura d'insieme: il 2026-08-26 è stata verificata puntualmente sul sorgente della libreria di conversione della community, al suo stato del 22 agosto 2026. La funzione esiste, si chiama `convertEVs`, e il suo corpo è un ciclo che scrive zero in tutti e sei i campi.

```cpp
bool GBPokemon::convertEVs(Gen3Pokemon *newPkmn)
{
    for (int i = 0; i < 6; i++)
    {
        newPkmn->setEV((Stat)i, 0);
    }
    return true;
};
```

Accanto a essa, `convertContestConditions` azzera le cinque statistiche da gara e la lucentezza estetica, che è l'unica cosa sensata perché quei dati non esistono a monte, mentre `convertPokerus` copia ceppo e giorni residui, quindi il Pokerus attraversa la conversione. La citazione di `convertEVs` chiude la questione meglio di qualunque ricerca: la conversione non è implementata da nessuno, e chi la vuole la scrive. La ricerca nel canale dei disassemblati e quella su Reddit, entrambe del 2026-08-26, non hanno trovato la formula, e nel secondo caso si è anche visto che la domanda era stata posta pubblicamente sotto l'annuncio del tool senza ricevere risposta.

Ha trovato però il dato da cui la conversione si deduce, ed è un'affermazione precisa di un partecipante che stava ottimizzando la funzione di radice quadrata di un disassemblato: per raggiungere il massimo di 63 punti di statistica al livello 100 non serve arrivare a 65535 di Stat Experience, perché bastano 63 per 4 tutto al quadrato, cioè 63504, e per come il calcolo è realizzato ne bastano in pratica 63002.

Il numero 63504 è quello che chiude il ragionamento, perché la sua radice quadrata è 252. Da qui la struttura si vede.

Nelle generazioni 1 e 2 il contributo dell'allenamento a una statistica passa per la radice quadrata della Stat Experience divisa per quattro, e satura a 63 punti. Nella generazione 3 il contributo passa per gli EV divisi per quattro, e satura anch'esso a 63 punti perché il tetto per statistica è 252. Le due formule hanno quindi la stessa forma e lo stesso tetto, e differiscono soltanto per il fatto che una prende la radice quadrata del valore memorizzato e l'altra lo prende così com'è. La conversione che conserva il contributo alla statistica è allora la radice quadrata, cioè un EV pari alla parte intera della radice quadrata della Stat Experience, limitato a 252.

La verifica ai bordi torna e vale la pena farla, perché è l'unica prova che si può fare senza codice. Una Stat Experience di 63504 diventa un EV di 252, cioè il massimo diventa il massimo. Una Stat Experience nulla diventa un EV nullo. Una Stat Experience di 65535, che è il massimo rappresentabile e sta sopra la saturazione, darebbe una radice di 255 e viene tagliata a 252, che è corretto perché entrambi i valori corrispondono ai 63 punti di saturazione. Il che significa anche che l'intervallo fra 63504 e 65535 è informazione che la generazione 3 non è in grado di rappresentare, e che quindi si perde: è una perdita reale ma innocua, perché non ha effetto su alcuna statistica.

Resta il vincolo complessivo, e non è un dettaglio. La generazione 3 impone che la somma degli EV non superi 510, mentre le generazioni 1 e 2 non impongono alcun tetto complessivo alla Stat Experience: un esemplare allenato a lungo può avere tutte e cinque le Stat Experience al massimo, che convertite darebbero 252 per cinque, cioè 1260, due volte e mezzo il consentito. La conversione fedele delle statistiche è quindi impossibile in generale, e questo non è un difetto della formula ma una proprietà del problema: la generazione 3 ha deliberatamente reso l'allenamento un gioco a somma zero, dove migliorare una statistica costa un'altra, e le generazioni precedenti no.

Ne segue che la conversione ha bisogno di una politica dichiarata per il caso in cui il totale sfori, e quella politica è una scelta discutibile nel senso preciso in cui questa nota usa la parola, cioè un parametro dello strato di conversione e non una costante sepolta nel codice. Le tre politiche sensate sono ridurre in proporzione conservando i rapporti fra le statistiche, troncare secondo un ordine di priorità dichiarato dall'utente, oppure rifiutare la conversione e chiedere una decisione. La prima conserva la forma dell'esemplare e ne abbassa il livello complessivo di allenamento, la seconda conserva alcune statistiche intatte e sacrifica le altre, la terza non decide al posto di nessuno. Nessuna delle tre è la risposta giusta in assoluto, ed è esattamente il genere di cosa che la tabella dei quattro metodi del PCCS avrebbe dovuto specificare.

Sul dato di partenza va detto un ultimo avvertimento. La cifra 63002 riportata dalla stessa fonte, minore di 63504, indica che l'implementazione reale del calcolo non è esattamente la radice quadrata matematica, presumibilmente per come è scritta la routine di approssimazione nel gioco. La derivazione qui sopra usa la radice quadrata matematica, che è la forma pulita; se un giorno la conversione dovesse essere esatta al punto da riprodurre il comportamento del gioco anche in quel margine, la routine va letta nel disassemblato e replicata invece che approssimata. È registrato fra i punti aperti.

## Un avvertimento sul distinguere le fonti

Nello stesso file c'è un caso speciale che, per una specie precisa e per due impronte hash specifiche del nome dell'allenatore e del soprannome, forza tutti i DV al massimo. È una scelta arbitraria di quella implementazione, probabilmente un omaggio, e non una regola del formato.

È un buon promemoria del perché la gerarchia delle fonti descritta in [[SOURCES]] mette il gioco sopra il tool: un'implementazione di riferimento dimostra che una cosa è possibile, non che sia il modo corretto di farla.

## Cosa leggere dopo

[[20-architettura-codice]] traduce tutto questo in una struttura di moduli, e [[30-opzioni-implementative]] mostra quanto costa ciascuna delle quattro strade alla luce di quanto appena visto.
