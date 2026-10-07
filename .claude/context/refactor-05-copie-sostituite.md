# Refactor 05. Rifare una copia senza rifarla, e una prova a vuoto che guardava solo i box

> Scheda di dettaglio della voce 5 di `studio-didattico-master.md`. Entra nel codice di `tools/pkhex-scrivi-salvataggio/Program.cs` prima e dopo il 2026-10-07, nello strumento nuovo `tools/pkhex-confronta-copie`, e in tre righe della libreria PKHeX.Core.

## Il problema

ADR-099 chiedeva di rifare quattro copie per HOME perché contenevano 201 esemplari con SID 5147 e 101 con SID 0. Le copie `-fin` erano nate a catena: ogni passata di `pkhex-scrivi-salvataggio` partiva dalla copia della passata precedente e proseguiva la sequenza dei file da un indice. Il rapporto di ogni copia registra la partenza così:

```json
"partenza": "main",
```

cioè il solo nome del file, che è lo stesso per tutte le copie. Ricostruire la catena voleva dire indovinarla, e rifarla da capo avrebbe cambiato la disposizione dei box già pianificata con il proprietario.

## La scelta: sostituire nello stesso posto

L'opzione `--sostituisci` prende la copia esistente con il suo rapporto e i lotti cambiati, riprepara ogni esemplare che viene da quei lotti e lo rimette nello stesso box e nello stesso posto, ma solo se è davvero diverso. Per poterlo fare senza una seconda copia della regola di preparazione, il corpo del ciclo è stato estratto in una funzione:

```csharp
PKM? Prepara(string percorso, string origine)
{
    if (!FileUtil.TryGetPKM(File.ReadAllBytes(percorso), out var pk, Path.GetExtension(percorso)))
    {
        esclusi.Add(new JsonObject { ["file"] = origine, ["motivo"] = "illeggibile" });
        return null;
    }
    // ... filtri, conversione, adattamento, giudizio, schiusa, geolocalizzazione, invariati ...
    return convertito;
}
```

Gli otto `continue` del ciclo sono diventati `return null`, dopo aver controllato che nel tratto estratto non ci fossero cicli annidati, dove la sostituzione avrebbe cambiato il significato.

## La prima sorpresa: lo strumento non era deterministico

La regressione naturale per un'estrazione è eseguire lo strumento prima e dopo sugli stessi ingressi e confrontare i file. Prima di toccare il codice lo strumento è stato eseguito due volte, e i due salvataggi differivano: 215 esemplari su 245 scritti. La causa sta nella libreria ed è voluta:

```csharp
HandlingTrainerMemoryFeeling = MemoryContext6.GetRandomFeeling6(4, 10),
```

alla riga 479 di `PK5.cs`, dentro `ConvertToPK6`, con `Random.Shared` (`RandUtil.cs` riga 8), che non si può fissare con un seme. Il trasferimento vero fa lo stesso. Ne segue che nessuna copia del progetto è riproducibile byte per byte, e che due copie si confrontano posto per posto ignorando quel campo. Da qui `pkhex-confronta-copie`, e la regressione dell'estrazione: 930 posti su 930 uguali o uguali salvo il sentimento, rapporti identici a meno delle impronte.

## La seconda sorpresa: la prova a vuoto

La prova che distingue una sostituzione corretta è quella a vuoto: si sostituisce con un solo lotto che non è cambiato, e il risultato deve essere identico all'originale. La prima volta ha fallito in due modi, uno dopo l'altro.

Primo: quattro Ombre di Colosseum risultavano diverse agli offset 06, A6 e D6. Lo strumento di confronto, esteso apposta per stampare gli offset, ha permesso di leggerli nel formato: 06 è la somma di controllo, A6 il sentimento, D6 il giorno d'incontro (`PK6.cs` righe 333 e 360). La copia era stata scritta un altro giorno, e `PK3.ConvertToPK4` pone la data d'incontro al giorno della conversione:

```csharp
MetDate = EncounterDate.GetDateNDS(),
```

alla riga 255 di `PK3.cs`, come il Parco Amici. I campi che la conversione assegna da sé sono quindi due, e la funzione `CampiDiConversione`, identica nei due strumenti, li ignora entrambi e dice quale ha dovuto ignorare.

Secondo, e più istruttivo: corretto il primo punto, i 914 esemplari risultavano tutti uguali, ma il file del salvataggio no, all'offset 0x1586B. La prima versione provava l'esemplare ripreparato scrivendolo nel salvataggio vero e, se era lo stesso, rimetteva quello di prima con `EntityImportSettings.None`. Ma la scrittura di prova, con le impostazioni predefinite, aveva già aggiornato il Pokédex (`SaveFile.cs` riga 263, `UpdatePKM` prima di `WriteSlotBox`), e rimettere l'esemplare non lo annullava. Un confronto limitato ai box non l'avrebbe visto mai. La correzione scrive la prova in un clone:

```csharp
var prova = sav.Clone();
prova.SetBoxSlotAtIndex(convertito.Clone(), posto);
var provato = prova.GetBoxSlotAtIndex(posto);
...
if (datiProva.AsSpan().SequenceEqual(prima) || CampiDiConversione(attuale, provato) is not null)
{
    invariati++;
    continue;
}
sav.SetBoxSlotAtIndex(convertito, posto);
```

e da allora la sostituzione a vuoto dà un file identico byte per byte, verificato con `cmp`.

## Come si è verificato il risultato

Sulle quattro copie vere: il confronto fra `-fin` e `-fin2` dà «diverso» in 141, 3, 168 e 12 posti, tutti e soli quelli dei lotti cambiati, e «uguale» byte per byte in tutti gli altri; ogni esemplare sostituito è riletto senza differenze e conforme; `pkhex-identificativi --tid 42317` trova l'allenatore del progetto solo con SID 58164. La prima corsa su `oras-giro-2-mn-fin` si è fermata senza scrivere, perché una voce del complemento ha una macchina nascosta e la preparazione la esclude senza `--includi-mn`: è il comportamento voluto, perché una sostituzione che salta in silenzio una voce lascerebbe nella copia l'esemplare vecchio.

## Come estendere il pattern

Una prova a vuoto si confronta sull'intero prodotto, non sulla parte che si intendeva cambiare: il difetto di una scrittura sta spesso in ciò che la scrittura tocca senza dirlo. E prima di usare l'uguaglianza dei file come prova di una regressione si verifica che lo strumento sia deterministico, eseguendolo due volte; se non lo è, si individua il campo che varia, nel codice e non per tentativi, e il confronto lo ignora per nome invece di diventare tollerante in generale.
