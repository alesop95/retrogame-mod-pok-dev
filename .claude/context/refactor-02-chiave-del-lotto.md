# Refactor 02. Una chiave che sapeva solo l'ultima cartella

> Scheda di dettaglio della voce 2 di `studio-didattico-master.md`. Entra nel codice di `tools/pkhex-giudica/Program.cs`, `tools/pkhex-scrivi-salvataggio/Program.cs`, `tools/checklist-pokedex.py` e `tools/stampa-collezione.py` prima e dopo il commit `0f82fcb` del 2026-10-07.

## Il difetto, nel codice

Il registro unico dei giudizi, `recreate-pokemon-distributions-events/giudizi-pkhex-core.json`, associa a ogni file di esemplare il giudizio di `LegalityAnalysis` della libreria PKHeX.Core e l'impronta SHA-256 del file giudicato. La chiave della voce la costruiva `pkhex-giudica` così, alla riga 70 del commit `035b8ed`.

```csharp
var nomeCartella = Path.GetFileName(radice.TrimEnd(Path.DirectorySeparatorChar));
...
var chiave = nomeCartella + "/" + Path.GetFileName(percorso);
```

`Path.GetFileName` applicato a una cartella restituisce l'ultimo componente del percorso. Per un lotto che tiene i file direttamente nella propria cartella, come `_notes/lotti/lotto-gb/`, l'ultimo componente è il nome del lotto e la chiave è `lotto-gb/EVT-2-0146-Phanpy.pk2`, cioè univoca. Il complemento del Rubino invece tiene i file in una sottocartella, `_notes/lotti/lotto-complemento-rubino/esemplari/`, e l'ultimo componente è `esemplari`: le sue 376 voci avevano chiave `esemplari/001-statico.pk3` e così via. La stessa forma sarebbe toccata ai file di `_notes/lotti/lotto-parco-lotta/esemplari/`, e poiché `tools/unisci-giudizi.py` rifiuta una chiave già presente mentre una corsa unica di `pkhex-giudica` su entrambe le cartelle avrebbe sovrascritto la prima con la seconda, il difetto non sarebbe stato un errore ma una perdita silenziosa di 376 giudizi.

La regola non viveva in un punto solo. `checklist-pokedex.py` cercava il giudizio con la stessa ricetta, alla riga 567.

```python
giudizio = giudizi.get("%s/%s" % (os.path.basename(cartella), nome))
```

`pkhex-scrivi-salvataggio` la ripeteva per l'origine che scrive nei rapporti delle copie per HOME, e `stampa-collezione.py` costruiva a mano le chiavi `"esemplari/" + nome` per riconoscere quelle origini. Quattro copie di una stessa regola, in due linguaggi, senza una dichiarazione comune: cambiare la chiave in uno solo dei quattro punti avrebbe fatto risultare le 179 voci della checklist prodotte dal complemento come «giudizio da rifare», senza alcun errore.

## La correzione

La chiave diventa il percorso della cartella relativo alla cartella `lotti` che la contiene. In C# la funzione è la stessa nei due strumenti.

```csharp
static string ChiaveDelLotto(string radice)
{
    var cartella = radice.TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
    for (var antenato = Path.GetDirectoryName(cartella); antenato != null; antenato = Path.GetDirectoryName(antenato))
        if (Path.GetFileName(antenato).Equals("lotti", StringComparison.OrdinalIgnoreCase))
            return Path.GetRelativePath(antenato, cartella).Replace(Path.DirectorySeparatorChar, '/');
    return Path.GetFileName(cartella);
}
```

Il ciclo risale gli antenati finché ne trova uno di nome `lotti`, e da lì calcola il percorso relativo con barre in avanti, così che la chiave sia la stessa su Windows e su un sistema POSIX. Se nessun antenato si chiama `lotti`, per esempio quando si giudica una cartella dello scratchpad, la funzione ricade sulla regola vecchia: è una scelta voluta, perché una cartella fuori dai lotti non ha un percorso canonico da cui partire. La proprietà che rende la correzione economica è che per ogni lotto di primo livello la chiave nuova coincide con quella vecchia, quindi le altre 3305 voci del registro non cambiano.

In Python la stessa regola è una riga, nella checklist.

```python
lotto = os.path.relpath(cartella, os.path.join(RADICE, "_notes", "lotti")).replace(os.sep, "/")
```

Le 376 voci esistenti non sono state rigiudicate ma rinominate sul testo del registro, sostituendo `"esemplari/` con `"lotto-complemento-rubino/esemplari/` dopo aver verificato che le occorrenze fossero esattamente 376, perché il registro è serializzato da .NET con fine riga CRLF e caratteri escapati, e riscriverlo con `json` di Python avrebbe prodotto un diff di decine di migliaia di righe. Prima di scrivere si è controllato che ciascuna delle 376 impronte coincidesse con il file su disco.

`stampa-collezione.py` accetta entrambe le forme per un periodo dichiarato: i rapporti delle copie scritti prima del 2026-10-07 portano ancora `esemplari/...` e non si rigenerano finché le copie non sono rifatte con ADR-099. Una compatibilità del genere è debito, e la si scrive come tale nel commento, con la condizione che la estingue.

## Come si è verificato che la correzione misuri il difetto

Le prove sono quattro, e la terza è quella che distingue. Il complemento rigiudicato con il giudice ricompilato, nel contesto `E` in cui era stato giudicato, produce 376 voci identiche campo per campo a quelle rinominate: la regola nuova in C# e la rinomina sul testo arrivano allo stesso risultato per vie indipendenti. La checklist e la coda rigenerate sono identiche byte per byte a quelle tracciate, con 2926 voci «prodotta e conforme». La versione della checklist di HEAD, cioè quella con `os.path.basename`, letta sul registro rinominato dà 2747 conformi e 179 «giudizio da rifare»: senza questa terza prova la seconda non direbbe nulla, perché un'uguaglianza si ottiene anche quando il codice cambiato non viene mai esercitato. Infine `stampa-collezione.py` dà descrizioni identiche alla versione di HEAD su tutti i 3351 esemplari di `_notes/stampa/collezione.json`, sia con l'origine vecchia sia con quella nuova simulata.

## Come estendere il pattern

Quando una chiave identifica un file, la si costruisce dal percorso relativo a una radice dichiarata e non da un frammento del percorso, perché un frammento è univoco solo finché la struttura delle cartelle resta piatta, e nessuno si accorge del giorno in cui smette di esserlo. E quando la stessa regola deve vivere in più strumenti, i punti che la ripetono si elencano nel commento di ciascuno, come fa ora la testa di `pkhex-giudica`: è il solo modo di sapere, cambiandone uno, quali altri vanno cambiati.
