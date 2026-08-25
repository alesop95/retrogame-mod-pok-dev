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

## Un avvertimento sul distinguere le fonti

Nello stesso file c'e' un caso speciale che, per una specie precisa e per due impronte hash specifiche del nome dell'allenatore e del soprannome, forza tutti i DV al massimo. E' una scelta arbitraria di quella implementazione, probabilmente un omaggio, e non una regola del formato.

E' un buon promemoria del perche' la gerarchia delle fonti descritta in [[SOURCES]] mette il gioco sopra il tool: un'implementazione di riferimento dimostra che una cosa e' possibile, non che sia il modo corretto di farla.

## Cosa leggere dopo

[[20-architettura-codice]] traduce tutto questo in una struttura di moduli, e [[30-opzioni-implementative]] mostra quanto costa ciascuna delle quattro strade alla luce di quanto appena visto.
