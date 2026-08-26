---
tipo: nota di studio
livello: intermedio
tags: [checksum, integrita, salvataggio]
up: "[[index]]"
vedi_anche: ["[[02-numeri-e-bit]]", "[[04-cifratura-gen3]]", "[[22-strumenti]]", "[[SOURCES]]"]
---

# Integrità: i tre checksum e cosa succede quando non tornano

Un salvataggio non è solo dati: contiene anche le prove della propria integrità. Il gioco, all'avvio, le verifica, e se non tornano non prova a recuperare il possibile: dichiara i dati inutilizzabili. Chi scrive un tool che modifica un salvataggio deve quindi ricalcolare quelle prove, e chi ne scrive uno che lo legge può usarle come diagnostica, perché un checksum che non torna dice esattamente dove guardare.

Le tre generazioni usano tre algoritmi diversi, con tre filosofie diverse, e il salto di qualità fra la prima e la terza è la cosa più interessante da osservare.

## Generazione 1: un byte e il complemento

Il salvataggio Gen 1 protegge la propria area principale con un solo byte, all'offset 0x3523, che è il complemento a uno della somma di tutti i byte da 0x2598 a 0x3522. Equivalentemente si parte da 255 e si sottrae ogni byte, lasciando che l'aritmetica a 8 bit vada in prestito quanto vuole.

È il più debole dei tre e la debolezza si vede a occhio: un solo byte significa che circa un salvataggio corrotto su duecentocinquantasei passa la verifica per caso, e una somma non pesata significa che scambiare due byte fra loro non cambia il risultato. I box hanno una protezione propria, un byte per box più un byte aggregato per banco, con la stessa struttura. Quando non torna, il gioco mostra il messaggio sui dati distrutti e riparte da zero.

## Generazione 2: due copie e due checksum

Gen 2 fa un passo avanti architetturale invece che algoritmico. Il checksum resta una somma, a 16 bit little-endian invece che a 8, ma il salvataggio contiene due copie dei dati del giocatore, ciascuna con il proprio checksum. Se una sola delle due torna, il gioco usa quella e la ricopia sopra l'altra.

È l'unico caso, in tutte e tre le generazioni, in cui esiste qualcosa che somigli a un recupero automatico, e vale la pena sapere che esiste, ma non vale la pena contarci: la copia di backup è contigua in Cristallo e frammentata in Oro e Argento, e in entrambi i casi viene sovrascritta dal salvataggio successivo. Non è una cronologia, è una ridondanza istantanea.

## Generazione 3: sezioni, firma, contatore e due slot

Qui il progetto cambia scala, perché il supporto è cambiato: la flash si scrive a blocchi, un blocco alla volta, e un'interruzione di corrente a metà del salvataggio è uno scenario reale che il formato deve sopravvivere. La risposta è un formato a sezioni indipendenti.

Il salvataggio è diviso in due slot, ciascuno di quattordici sezioni da 4096 byte. Ogni sezione porta in coda quattro campi: il proprio identificatore, il proprio checksum, una firma costante e un contatore di salvataggio. La firma vale 0x08012025 e una firma diversa invalida la sezione e con essa lo slot. Il contatore è lo stesso per tutte e quattordici le sezioni di uno slot, e serve a decidere quale dei due slot è il più recente: vince lo slot A solo se il suo contatore è strettamente maggiore, quindi a parità vince B. Se il più recente ha una sezione che non torna, il gioco usa il precedente.

Il modo in cui il gioco salva sfrutta questa struttura: scrive una sezione per volta, aggiornando lo slot che non è quello in uso, così che un'interruzione lasci intatto lo slot valido. È un doppio buffer, ed è la ragione per cui un salvataggio Gen 3 contiene sempre due stati di gioco diversi e leggermente sfasati nel tempo.

L'algoritmo del checksum, letto da `CalculateChecksum` in `src/save.c` di pokeemerald, è una somma di parole da 32 bit accumulata a 32 bit, poi ripiegata sommando la metà alta alla metà bassa e troncata a 16 bit.

```c
static u16 CalculateChecksum(void *data, u16 size)
{
    u16 i;
    u32 checksum = 0;
    for (i = 0; i < (size / 4); i++)
    {
        checksum += *((u32 *)data);
        data += sizeof(u32);
    }
    return ((checksum >> 16) + checksum);
}
```

C'è un dettaglio che complica la vita a chi scrive un tool: il parametro `size` non è 3968 per tutte le sezioni. Dipende dalla dimensione della struttura di salvataggio che quella sezione ospita, e quelle dimensioni sono valori di compilazione del gioco, quindi non ricavabili leggendo il salvataggio. Lo strumento del progetto risolve empiricamente, cercando quale prefisso di parole riproduce il checksum memorizzato, e riferisce la lunghezza che ha trovato: è una scelta pragmatica che vale la pena conoscere perché è anche una diagnostica, dato che una lunghezza inattesa dice che la sezione non è quella che sembra.

## Il secondo livello di integrità: il singolo Pokemon

Le tre protezioni di cui sopra riguardano il salvataggio nel suo insieme. In generazione 3 esiste un secondo livello, più fine e più feroce: ogni singolo Pokemon ha un proprio checksum a 16 bit che protegge i suoi 48 byte cifrati. Se non torna, il gioco non dichiara il salvataggio corrotto, ma trasforma quel Pokemon in un Uovo Difettoso, cioè un oggetto inerte che non si può usare, spostare o eliminare facilmente.

Questa è la differenza pratica fra sbagliare un checksum di sezione e sbagliare un checksum di Pokemon: nel primo caso il gioco rifiuta il salvataggio e si conserva l'occasione di correggere il file, nel secondo caso accetta il salvataggio e distrugge un Pokemon in modo visibile. La procedura di quel calcolo sta in [[04-cifratura-gen3]], perché è inseparabile dalla cifratura.

## Cosa leggere dopo

[[04-cifratura-gen3]] chiude il discorso sull'integrità del singolo Pokemon, e [[22-strumenti]] descrive lo strumento che applica tutto questo a un salvataggio reale.
