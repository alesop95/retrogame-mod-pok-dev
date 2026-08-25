---
tipo: nota di studio
livello: intermedio
tags: [cifratura, gen3, checksum]
up: "[[index]]"
vedi_anche: ["[[03-integrita-checksum]]", "[[06-identita-pokemon]]", "[[07-conversione-vincoli]]", "[[DATA-FORMATS_Gen1-Gen2-Gen3]]"]
---

# La cifratura della generazione 3, e perche' non e' sicurezza

I 48 byte centrali di un Pokemon di generazione 3 sono cifrati e permutati. E' l'unico caso di offuscamento in tutto il materiale che questo progetto tocca, e la prima cosa da capire e' che non e' crittografia nel senso della sicurezza: la chiave e' scritta in chiaro nella stessa struttura, due campi piu' su. Chi ha il dato ha la chiave, sempre.

Allora perche' esiste. La ragione plausibile, e va detto che e' una ricostruzione ragionevole e non una dichiarazione degli autori, e' rendere fragile la manomissione invece che impedirla. Un dato cifrato con una chiave derivata dall'identita' del Pokemon, e coperto da un checksum, non si modifica con un editor esadecimale a caso: qualunque byte cambiato senza ricalcolare tutto produce un Uovo Difettoso, cioe' un fallimento immediato e visibile invece di un Pokemon leggermente alterato che circola per anni. Il formato non nasconde i dati, li rende scomodi da falsificare a mano.

## Le tre operazioni, nell'ordine giusto

Leggere un Pokemon Gen 3 richiede tre passi, e riscriverlo richiede gli stessi tre nell'ordine inverso. Sbagliare l'ordine e' l'errore piu' comune.

Il primo passo e' la decifratura. La chiave e' il valore di personalita' messo in XOR con l'ID dell'allenatore a 32 bit, e si applica in XOR a ciascuna delle dodici parole da 32 bit del blocco. Il codice del gioco lo fa in due passaggi successivi, che e' la stessa cosa.

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

Poiche' lo XOR e' la propria inversa, cifrare e decifrare sono la stessa funzione, e questo ha una conseguenza pratica utile: un tool ha bisogno di una sola routine, e un errore di verso non esiste.

Il secondo passo e' la permutazione. Il blocco decifrato contiene quattro sottostrutture da 12 byte, ma il loro ordine non e' fisso: e' una delle ventiquattro permutazioni possibili, scelta dal valore di personalita' modulo 24. Non e' offuscamento aggiuntivo in senso stretto, ma ha lo stesso effetto: senza conoscere il valore di personalita' non si sa nemmeno quale campo si stia guardando.

Il terzo passo e' il checksum, che si calcola sul blocco decifrato e si confronta con quello memorizzato in chiaro nell'intestazione. Su questo punto le fonti secondarie sbagliano, e l'errore e' del tipo che distrugge un Pokemon: una pagina enciclopedica descrive la somma come byte per byte. Il sorgente dice altro. La sottostruttura e' una unione che espone anche `u16 raw[6]`, cioe' sei parole da 16 bit, e `CalculateBoxMonChecksum` somma quelle parole per tutte e quattro le sottostrutture in un accumulatore a 16 bit, lasciando che l'aritmetica tronchi.

In scrittura l'ordine e' quindi: comporre le quattro sottostrutture, calcolarne il checksum, scriverlo nell'intestazione, permutare secondo il valore di personalita', cifrare. Chi calcola il checksum dopo aver cifrato ottiene un numero che non c'entra nulla, e il gioco produce un Uovo Difettoso.

## Il vincolo nascosto: il valore di personalita' decide troppe cose

C'e' una conseguenza architetturale che va vista subito, perche' condiziona il modo in cui si scrive un writer. Il valore di personalita' non e' solo un identificatore: e' anche la chiave di cifratura, insieme all'ID dell'allenatore, ed e' anche il selettore della permutazione. Cambiarlo dopo aver composto la struttura significa che il blocco va ripermutato e ricifrato da zero.

Ne segue che l'ordine corretto di costruzione di un Pokemon Gen 3 e': prima si decide il valore di personalita', e solo dopo si comincia a scrivere. E poiche' quel valore, come mostra [[06-identita-pokemon]], determina anche natura, sesso, abilita', lucentezza e forma, la sua scelta e' il primo passo di tutta la conversione, non l'ultimo. E' il motivo per cui [[07-conversione-vincoli]] tratta la generazione del valore di personalita' come un problema a se' stante.

## Un secondo uso della stessa idea, nel salvataggio

Vale la pena notare che la generazione 3 usa la stessa tecnica anche fuori dai Pokemon, e in Smeraldo la usa sullo zaino. Le quantita' degli oggetti nello zaino e il denaro sono in XOR con una chiave di sicurezza specifica di quel salvataggio, mentre le quantita' del deposito PC sono in chiaro. Anche qui non e' sicurezza, e' fragilita' voluta: un codice trucco che scrive un numero in chiaro nel posto giusto produce una quantita' assurda invece del valore desiderato.

Questa asimmetria fra zaino e deposito PC e' la ragione per cui il sottoprogetto Smeraldo ha uno strumento dedicato: una quantita' assurda nello zaino letto in chiaro non prova nulla, mentre una quantita' assurda nel deposito PC e' un'anomalia vera. Lo strumento e' in [[22-strumenti]].

## Cosa leggere dopo

[[06-identita-pokemon]] mostra che cosa contengono le quattro sottostrutture e come si identifica un Pokemon, e [[07-conversione-vincoli]] affronta la scelta del valore di personalita'.
