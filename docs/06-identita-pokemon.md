---
tipo: nota di studio
livello: intermedio
tags: [identità, dv, iv, valore-di-personalita]
up: "[[index]]"
vedi_anche: ["[[02-numeri-e-bit]]", "[[04-cifratura-gen3]]", "[[07-conversione-vincoli]]", "[[DATA-FORMATS_Gen1-Gen2-Gen3]]"]
---

# Che cosa identifica un Pokemon, e come cambia fra le generazioni

Un Pokemon in un salvataggio è un insieme di campi, ma non tutti i campi hanno lo stesso ruolo. Alcuni sono dati primari, cioè scelti quando il Pokemon è nato o catturato e mai più toccati. Altri sono derivati, cioè calcolati dai primari e ricalcolabili in qualsiasi momento. Distinguere le due categorie è la cosa più utile che si possa fare prima di scrivere un writer, perché i derivati non vanno copiati: vanno ricalcolati, e copiarli è come copiare il risultato di una somma senza gli addendi.

## Il primo asse: la specie

La specie è un numero, e i tre spazi di numerazione delle tre generazioni sono diversi fra loro. In generazione 1 l'indice interno non ha alcuna relazione con il Pokedex: l'indice 1 è Rhydon, che nel Pokedex è il 112, e l'indice 99 è Bulbasaur, che è il primo. Nell'intervallo valido sono sparse trentanove posizioni che non corrispondono a nulla, e sono quelle che il gioco interpreta come MissingNo. In generazione 2 la numerazione coincide con il Pokedex nazionale, ed è l'unica delle tre a comportarsi come uno si aspetterebbe. In generazione 3 le prime duecentocinquantuno posizioni seguono il Pokedex nazionale, poi c'è un intervallo vuoto, e le specie di Hoenn cominciano da 277 in un ordine proprio.

Per un ponte da Gen 1 e 2 verso Gen 3 questa complicazione è fortunatamente benigna, perché tutte le specie sorgente stanno nell'intervallo dove Gen 2 e Gen 3 concordano: serve una sola tabella, quella dall'indice interno Gen 1 al numero nazionale. Ma serve, e va generata dal disassemblato invece di trascritta, per la ragione spiegata in [[05-testo-e-charmap]].

## Il secondo asse: i valori individuali

Ogni Pokemon ha valori che ne determinano il potenziale nelle statistiche, e sono un dato primario puro: si fissano alla nascita e non cambiano.

In generazione 1 e 2 si chiamano DV, sono quattro, valgono da 0 a 15 e occupano due byte come quattro nibble. Il quinto, quello dei punti salute, non è memorizzato: si deriva dai bit meno significativi degli altri quattro, secondo una formula che il disassemblato scrive come commento e che vale la pena guardare perché è la dimostrazione più compatta di quanto quell'epoca fosse avara di memoria.

```
; DV_HP = (DV_ATK & 1) << 3 | (DV_DEF & 1) << 2 | (DV_SPD & 1) << 1 | (DV_SPC & 1)
```

Questa derivazione ha un'implicazione che va capita bene: il DV dei punti salute non è un grado di libertà. Chi modifica un DV per aggiustare una statistica sta modificando anche i punti salute, e non può evitarlo.

In generazione 3 diventano IV, sono sei, valgono da 0 a 31 e occupano un campo di bit dentro una parola da 32 bit insieme al flag di uovo e allo slot di abilità. Il passaggio da quattro a sei non è un raddoppio di precisione ma un cambio di modello: la statistica Speciale, che in generazione 1 era una sola e in generazione 2 si era divisa in due valori calcolati da un solo DV, in generazione 3 ha finalmente due valori individuali indipendenti.

Questa asimmetria è verificabile nel sorgente, perché in `CalcMonStatC` di pokecrystal sia l'Attacco Speciale sia la Difesa Speciale saltano al medesimo ramo che legge il DV Speciale. Ne segue che un DV singolo deve diventare due IV, e non esiste una risposta corretta a come farlo, solo una scelta da documentare.

## Il terzo asse: l'allenamento

Accanto al potenziale c'è il progresso accumulato combattendo, che nelle prime due generazioni si chiama Stat Experience e nella terza EV. Anche qui il cambio non è cosmetico. La Stat Experience è un valore per statistica che sale fino a 65535 e non ha un tetto complessivo; gli EV valgono al massimo 255 per statistica con un tetto di 510 in totale.

Una conversione fra i due modelli non è quindi una scala lineare: è una scala con saturazione e una ridistribuzione dentro un tetto globale, cioè una decisione su quali statistiche sacrificare. L'implementazione di riferimento, come si vede in [[07-conversione-vincoli]], evita il problema azzerando tutto.

## Il quarto asse: il valore di personalità, che in Gen 1 e 2 non esiste

La generazione 3 introduce un numero da 32 bit che non ha alcun equivalente nelle precedenti, e che è la cosa più densa di tutto il formato: da esso derivano la natura, il sesso, lo slot di abilità, la lettera di Unown, la lucentezza in combinazione con l'ID dell'allenatore, e altre proprietà minori come i disegni di Spinda. Serve inoltre da chiave di cifratura e da selettore della permutazione, come descritto in [[04-cifratura-gen3]].

È quindi un dato primario che si comporta come una radice: tutto il resto pende da lui. E poiché in generazione 1 e 2 non esiste, una conversione deve inventarlo, e non può inventarlo a caso perché i valori che ne derivano devono corrispondere a quelli del Pokemon originale. Questo è il problema centrale del ponte, ed è il soggetto di [[07-conversione-vincoli]].

## Riepilogo utile per chi scrive codice

I dati primari da copiare o convertire sono specie, valori individuali, allenamento, esperienza, mosse, PP e bonus PP, oggetto tenuto, identità dell'allenatore, soprannome, amicizia e provenienza. I dati derivati da ricalcolare, mai copiare, sono le statistiche, il livello quando si scrive nella squadra, e in generazione 3 il checksum. I dati inventati, cioè quelli che in origine non esistono, sono in generazione 3 il valore di personalità, l'ID segreto, la natura, l'abilità, la Poke Ball, il luogo di incontro e le statistiche da gara.

## Cosa leggere dopo

[[07-conversione-vincoli]] usa questa classificazione per affrontare il problema difficile.
