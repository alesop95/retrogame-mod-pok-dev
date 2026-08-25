---
tipo: glossario
tags: [glossario, riferimento]
up: "[[index]]"
vedi_anche: ["[[index]]", "[[DATA-FORMATS_Gen1-Gen2-Gen3]]", "[[SOURCES]]"]
---

# Glossario

Termini che ricorrono in tutto il progetto, con il rimando alla nota che li tratta per esteso.

| Termine | Significato |
|---|---|
| ACE | Arbitrary Code Execution, esecuzione di codice arbitrario: far eseguire a un programma codice non previsto dai suoi autori, sfruttando un difetto. Vedi [[09-esecuzione-codice]] |
| big-endian | ordine dei byte in cui il piu' significativo viene per primo; e' quello delle generazioni 1 e 2. Vedi [[02-numeri-e-bit]] |
| campo di bit | numero che occupa un intervallo di bit non allineato al byte, tecnica usata per impaccare piu' valori in una parola. Vedi [[02-numeri-e-bit]] |
| checksum | valore calcolato dai dati e memorizzato accanto a essi, che il gioco verifica per decidere se accettarli. Vedi [[03-integrita-checksum]] |
| DV | Determinant Values, i valori individuali delle generazioni 1 e 2: quattro, da 0 a 15, con il quinto derivato. Vedi [[06-identita-pokemon]] |
| EV | Effort Values, i punti di allenamento dalla generazione 3: sei, da 0 a 255, con tetto complessivo di 510. Vedi [[06-identita-pokemon]] |
| flash | memoria non volatile usata per il salvataggio in generazione 3, che si scrive a blocchi e non ha bisogno di batteria. Vedi [[01-fondamenta-salvataggio]] |
| ID segreto | i 16 bit alti dell'identificatore dell'allenatore in generazione 3, che in generazione 1 e 2 non esistono e che il convertitore usa per decidere la lucentezza. Vedi [[07-conversione-vincoli]] |
| IV | Individual Values, i valori individuali dalla generazione 3: sei, da 0 a 31, memorizzati in un campo proprio. Vedi [[06-identita-pokemon]] |
| little-endian | ordine dei byte in cui il meno significativo viene per primo; e' quello della generazione 3. Vedi [[02-numeri-e-bit]] |
| lista di correzione | elenco delle posizioni in cui un byte non trasmissibile e' stato sostituito, inviato insieme ai dati sul cavo. Vedi [[08-cavo-link]] |
| lucentezza | proprieta' estetica di un Pokemon; in generazione 2 e' un pattern di DV, in generazione 3 una condizione sullo XOR di identificatori e valore di personalita'. Vedi [[07-conversione-vincoli]] |
| MissingNo | cio' che il gioco mostra quando un indice di specie di generazione 1 cade in una delle posizioni non assegnate. Vedi [[06-identita-pokemon]] |
| multiboot | modalita' del Game Boy Advance che riceve un programma dal cavo e lo esegue in RAM, senza cartuccia. Vedi [[10-multiboot-hardware]] |
| nibble | meta' di un byte, quattro bit, valore da 0 a 15. Vedi [[02-numeri-e-bit]] |
| PCCS | Pokemon Community Conversion Standard, specifica comunitaria della conversione fra generazioni; documenta quattro metodi e ne implementa uno. Vedi [[07-conversione-vincoli]] |
| Pal Park | meccanismo ufficiale che porta i Pokemon dalla generazione 3 alla 4, citato come modello di design dai progetti di ponte. Vedi [[30-opzioni-implementative]] |
| preambolo | sequenza di byte 0xFD che delimita l'inizio di un blocco sul cavo Link. Vedi [[08-cavo-link]] |
| red_party_struct | macro del disassemblato di generazione 2 che descrive la struttura di generazione 1, usata per il Time Capsule. Vedi [[08-cavo-link]] |
| RTC | Real Time Clock, l'orologio interno alimentato dalla batteria in Rubino, Zaffiro e Smeraldo. Vedi [[01-fondamenta-salvataggio]] |
| sezione | blocco da 4096 byte del salvataggio di generazione 3, con identificatore, checksum, firma e contatore in coda. Vedi [[03-integrita-checksum]] |
| SRAM | Static Random Access Memory, la memoria volatile della cartuccia tenuta viva da una batteria. Vedi [[01-fondamenta-salvataggio]] |
| Stat Experience | l'antenato degli EV nelle generazioni 1 e 2: un valore per statistica fino a 65535, senza tetto complessivo. Vedi [[06-identita-pokemon]] |
| Time Capsule | l'unico meccanismo ufficiale di trasferimento fra generazione 1 e 2, e per questo progetto il precedente piu' utile perche' e' una conversione di formato leggibile nel disassemblato. Vedi [[08-cavo-link]] |
| Uovo Difettoso | cio' in cui la generazione 3 trasforma un Pokemon il cui checksum non torna. Vedi [[04-cifratura-gen3]] |
| valore di personalita' | numero da 32 bit introdotto in generazione 3, da cui derivano natura, sesso, abilita', forma e lucentezza, e che serve anche da chiave di cifratura. Vedi [[06-identita-pokemon]] |
| Unown | specie le cui ventotto forme condividono un solo indice, con la lettera determinata dal valore di personalita'. Vedi [[06-identita-pokemon]] |
