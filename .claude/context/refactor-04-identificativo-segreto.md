# Refactor 04. Lo stesso identificativo, corretto in due modi

> Scheda di dettaglio della voce 4 di `studio-didattico-master.md`. Entra nel codice di `tools/pkhex-periferiche/Program.cs`, `tools/pkhex-scambi-gen67/Program.cs` e `tools/manifesto-complemento-rubino.py` prima e dopo il 2026-10-07, nei due strumenti nati quel giorno, `tools/pkhex-identificativi` e `tools/pkhex-correggi-sid`, e nelle tre righe della libreria PKHeX.Core che decidono quale correzione serve.

## Il difetto, nel codice

L'allenatore del progetto è definito in `recreate-pokemon-distributions-events/allenatore.json`, con TID 42317 e SID 58164, e quel file esiste proprio perché «il medesimo dato scritto in due posti diverge senza che nessuno se ne accorga», come dice la sua nota. Tre programmi non lo leggevano. In `pkhex-periferiche`, alla riga 50 del commit `3cf1f21`:

```csharp
SimpleTrainerInfo Allenatore(GameVersion v, byte gen, EntityContext ctx) =>
    new(v) { OT = "Alessio", TID16 = 42317, SID16 = 5147, Gender = 0, Language = (int)LanguageID.Italian, Generation = gen, Context = ctx };
```

La stessa terna era ripetuta alla riga 78 per il corso giapponese del Pokéwalker e alla riga 60 di `pkhex-scambi-gen67`. Nel manifesto del complemento del Rubino, invece, Smeraldo aveva SID 0:

```python
if gioco == "E":
    fuori[gioco] = {"OT": "Alessio", "TID16": 42317, "SID16": 0}
```

Il 5147 non ha fonte né motivo in nessun documento del progetto. Nessuno dei due valori produceva un errore, perché un identificativo segreto qualunque genera esemplari legali: il difetto era una proprietà della collezione, cioè tre identità diverse per lo stesso allenatore, e la si vede solo leggendo il campo in tutti i file.

## La misura, e perché serviva uno strumento

Il registro dei giudizi non mostra il SID: per le generazioni fino alla sesta la descrizione porta il solo TID, e per la settima il numero a sei cifre che il gioco mostra, che mescola i due. `pkhex-identificativi` legge il campo direttamente e conta le terne allenatore, TID e SID per cartella:

```
lotto-periferiche:                 29  Alessio 42317 5147      3  アレシオ 42317 5147
lotto-periferiche-secondo-tempo:  141  Alessio 42317 5147     15  アレシオ 42317 5147
lotto-statici-gen7:                12  Alessio 42317 5147
lotto-oggetti-gen5:                 1  Alessio 42317 5147
lotto-complemento-rubino/esemplari: 101  Alessio 42317 0
```

I totali, 201 e 101, coincidono con l'indagine del 2026-10-06, che però era stata fatta con script di sessione non conservati. Una misura che si deve ripetere tre volte, sui lotti, sulle copie e sulla cartuccia, non può dipendere da un programma che non esiste più.

## Le due correzioni, e la riga di codice che le separa

La correzione sembra la stessa ovunque, cioè scrivere 58164 al posto del valore sbagliato. Non lo è, e la differenza sta nel modo in cui ciascun formato deriva il PID. Nella libreria, per il Pokéwalker:

```csharp
public static uint GetPID(ushort TID16, ushort SID16, uint nature, byte gender, byte genderRatio)
```

alla riga 280 di `PKHeX.Core/Legality/RNG/ClassicEra/Gen4/PokewalkerRNG.cs`: il PID è funzione degli identificativi. Per la quinta generazione, alle righe 14-25 di `MonochromeRNG.cs`:

```csharp
public static uint GetBitXor<T>(T tr) where T : ITrainerID32ReadOnly => ((uint)tr.TID16 ^ tr.SID16) & 1;
public static uint GetBitXor(uint pid, ushort tid, ushort sid) => GetBitXor(tid, sid) ^ (pid & 1) ^ (pid >> 31);
```

Il bit alto del PID è vincolato alla parità di TID xor SID. 42317 e 5147 sono dispari, quindi la loro somma esclusiva è pari; 58164 è pari, quindi con 42317 dà una somma esclusiva dispari. Ogni esemplare di quinta generazione con i soli byte del SID cambiati violerebbe il vincolo. Per i 201 la correzione è dunque la rigenerazione, con lo strumento che ora legge il file: 223 file rigenerati, 223 conformi negli stessi contesti di prima, 201 su 201 con SID 58164.

In terza generazione invece:

```csharp
public override ushort SID16 { get => ReadUInt16LittleEndian(Data[0x06..]); ... }
private ushort CalculateChecksum() => Checksums.Add16(Data[0x20..PokeCrypto.SIZE_3STORED]);
```

alle righe 56 e 204 di `PK3.cs`: il SID sta nell'intestazione, la somma di controllo copre solo i dati da 0x20, e negli incontri di Smeraldo il PID viene dal generatore pseudocasuale, non dagli identificativi. Cambiare il SID non tocca né il PID né la somma di controllo. Quei 101 esemplari erano già sulla cartuccia del Rubino, e rigenerarli avrebbe prodotto individui nuovi: per ADR-082 si corregge il difetto e non si rifà la collezione. `pkhex-correggi-sid` cambia i due byte e rifiuta di scrivere se il file di partenza non è nel formato che lo strumento riscrive, se cambiano PID o cromaticità, o se la libreria contesta l'esemplare.

## Come si è verificato che la correzione misuri il difetto

Per la rigenerazione: `pkhex-identificativi` prima e dopo, con 201 esemplari passati da 5147 a 58164, stessi nomi di file, stesse specie, stessi allenatori, nessun cromatico prima né dopo; `pkhex-giudica` con 223 conformi nei contesti di prima; il registro con 235 righe cambiate, cioè le 223 impronte più i 12 identificativi a sei cifre della settima generazione, passati da 356109 a 878221. Per la correzione dei byte la verifica decisiva è esterna allo strumento: un confronto in Python, scritto senza la libreria, trova in tutti i 101 file differenze solo agli offset 6 e 7, e ricalcola da sé la somma di controllo. Se lo strumento avesse cambiato altro, per esempio per una riserializzazione diversa, quel confronto l'avrebbe mostrato.

## Come estendere il pattern

Prima di correggere un campo di un dato derivato si cerca nel codice del formato chi legge quel campo per calcolarne altri. Se nessuno lo legge, la correzione è una scrittura di byte, che conserva l'identità di tutto il resto; se qualcuno lo legge, la correzione è una rigenerazione, e i byte vecchi vanno buttati con tutto ciò che ne derivava. Lo si stabilisce sul codice e non sull'aspetto del dato, perché nulla nell'esemplare dice da quali campi il suo PID è stato calcolato. E un valore che deve essere uguale in più programmi si legge da un file solo, che i programmi cercano da sé, così che i comandi già documentati non cambino.
