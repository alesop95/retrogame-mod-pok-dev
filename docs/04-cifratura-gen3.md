---
tipo: nota di studio
livello: intermedio
tags: [cifratura, gen3, checksum]
up: "[[index]]"
vedi_anche: ["[[03-integrita-checksum]]", "[[06-identita-pokemon]]", "[[07-conversione-vincoli]]", "[[DATA-FORMATS_Gen1-Gen2-Gen3]]"]
---

# La cifratura della generazione 3, e perché non è sicurezza

I 48 byte centrali di un Pokemon di generazione 3 sono cifrati e permutati. È l'unico caso di offuscamento in tutto il materiale che questo progetto tocca, e la prima cosa da capire è che non è crittografia nel senso della sicurezza: la chiave è scritta in chiaro nella stessa struttura, due campi più su. Chi ha il dato ha la chiave, sempre.

Allora perché esiste. La ragione plausibile, e va detto che è una ricostruzione ragionevole e non una dichiarazione degli autori, è rendere fragile la manomissione invece che impedirla. Un dato cifrato con una chiave derivata dall'identità del Pokemon, e coperto da un checksum, non si modifica con un editor esadecimale a caso: qualunque byte cambiato senza ricalcolare tutto produce un Uovo Difettoso, cioè un fallimento immediato e visibile invece di un Pokemon leggermente alterato che circola per anni. Il formato non nasconde i dati, li rende scomodi da falsificare a mano.

## Le tre operazioni, nell'ordine giusto

Leggere un Pokemon Gen 3 richiede tre passi, e riscriverlo richiede gli stessi tre nell'ordine inverso. Sbagliare l'ordine è l'errore più comune.

Il primo passo è la decifratura. La chiave è il valore di personalità messo in XOR con l'ID dell'allenatore a 32 bit, e si applica in XOR a ciascuna delle dodici parole da 32 bit del blocco. Il codice del gioco lo fa in due passaggi successivi, che è la stessa cosa.

```c
static void EncryptBoxMon(struct BoxPokemon *boxMon)
{
    u32 i;
    for (i = 0; i < ARRAY_COUNT(boxMon->secure.raw); i++)
    {
        boxMon->secure.raw[i] ^= boxMon->personality;
        boxMon->secure.raw[i] ^= boxMon->otId;
    }
}
```

Poiché lo XOR è la propria inversa, cifrare e decifrare sono la stessa funzione, e questo ha una conseguenza pratica utile: un tool ha bisogno di una sola routine, e un errore di verso non esiste.

Il secondo passo è la permutazione. Il blocco decifrato contiene quattro sottostrutture da 12 byte, ma il loro ordine non è fisso: è una delle ventiquattro permutazioni possibili, scelta dal valore di personalità modulo 24. Non è offuscamento aggiuntivo in senso stretto, ma ha lo stesso effetto: senza conoscere il valore di personalità non si sa nemmeno quale campo si stia guardando.

Il terzo passo è il checksum, che si calcola sul blocco decifrato e si confronta con quello memorizzato in chiaro nell'intestazione. Su questo punto le fonti secondarie sbagliano, e l'errore è del tipo che distrugge un Pokemon: una pagina enciclopedica descrive la somma come byte per byte. Il sorgente dice altro. La sottostruttura è una unione che espone anche `u16 raw[6]`, cioè sei parole da 16 bit, e `CalculateBoxMonChecksum` somma quelle parole per tutte e quattro le sottostrutture in un accumulatore a 16 bit, lasciando che l'aritmetica tronchi.

In scrittura l'ordine è quindi: comporre le quattro sottostrutture, calcolarne il checksum, scriverlo nell'intestazione, permutare secondo il valore di personalità, cifrare. Chi calcola il checksum dopo aver cifrato ottiene un numero che non c'entra nulla, e il gioco produce un Uovo Difettoso.

## Il vincolo nascosto: il valore di personalità decide troppe cose

C'è una conseguenza architetturale che va vista subito, perché condiziona il modo in cui si scrive un writer. Il valore di personalità non è solo un identificatore: è anche la chiave di cifratura, insieme all'ID dell'allenatore, ed è anche il selettore della permutazione. Cambiarlo dopo aver composto la struttura significa che il blocco va ripermutato e ricifrato da zero.

Ne segue che l'ordine corretto di costruzione di un Pokemon Gen 3 è: prima si decide il valore di personalità, e solo dopo si comincia a scrivere. E poiché quel valore, come mostra [[06-identita-pokemon]], determina anche natura, sesso, abilità, lucentezza e forma, la sua scelta è il primo passo di tutta la conversione, non l'ultimo. È il motivo per cui [[07-conversione-vincoli]] tratta la generazione del valore di personalità come un problema a sé stante.

## Un secondo uso della stessa idea, nel salvataggio

Vale la pena notare che la generazione 3 usa la stessa tecnica anche fuori dai Pokemon, e in Smeraldo la usa sullo zaino. Le quantità degli oggetti nello zaino e il denaro sono in XOR con una chiave di sicurezza specifica di quel salvataggio, mentre le quantità del deposito PC sono in chiaro. Anche qui non è sicurezza, è fragilità voluta: un codice trucco che scrive un numero in chiaro nel posto giusto produce una quantità assurda invece del valore desiderato.

Questa asimmetria fra zaino e deposito PC è la ragione per cui il sottoprogetto Smeraldo ha uno strumento dedicato: una quantità assurda nello zaino letto in chiaro non prova nulla, mentre una quantità assurda nel deposito PC è un'anomalia vera. Lo strumento è in [[22-strumenti]].

## Cosa leggere dopo

[[06-identita-pokemon]] mostra che cosa contengono le quattro sottostrutture e come si identifica un Pokemon, e [[07-conversione-vincoli]] affronta la scelta del valore di personalità.
