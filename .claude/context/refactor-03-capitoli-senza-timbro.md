# Refactor 03. Un controllo che saltava ciò che non sapeva misurare

> Scheda di dettaglio della voce 3 di `studio-didattico-master.md`. Entra nel codice di `tools/check-thesis-coverage.py` prima e dopo il 2026-10-07, e nella misura del debito della tesi che la correzione ha reso visibile (ADR-101).

## Che cosa promette lo strumento

`check-thesis-coverage.py` garantisce che ogni sezione dei documenti Markdown del progetto finisca in un capitolo della tesi o in un'esenzione motivata. Un capitolo reclama un documento intero o una sua sezione con un commento in testa, e dichiara il commit al quale è stato riletto.

```latex
% copre: docs/22-strumenti.md
% verificato-al-commit: ff9fb3e
```

Le due dichiarazioni rispondono a domande diverse. `copre` dice dove è finito il contenuto; `verificato-al-commit` dice fino a quando quel contenuto è stato confrontato con il documento. Una sezione reclamata conta come coperta, e il drift, cioè il documento cambiato dopo il timbro, si misura con `git diff --name-only <timbro>..HEAD` sui percorsi reclamati.

## Il difetto, nel codice

Il ciclo del drift cominciava così, fino al 2026-10-07.

```python
stale = []
for c in capitoli:
    if not c["commit"] or head is None:
        continue
```

Un capitolo senza timbro veniva saltato. Ma la sua dichiarazione `copre` restava valida per il conteggio della copertura, quindi le sezioni che reclamava risultavano coperte per sempre, qualunque cosa accadesse al documento. Su 39 capitoli, 19 dichiaravano coperture senza timbro. Il caso più grande è `24-strumenti.tex`, che reclama per intero `docs/22-strumenti.md`: il documento è cresciuto a 53 sezioni e circa 19000 parole, con tutta la famiglia di strumenti su PKHeX.Core nata dal 2026-09-25, mentre il capitolo ha circa 5200 parole e, misurando sul nome dello strumento nel titolo di ciascuna sezione, ne cita 3. Lo strumento dava quelle 53 sezioni per coperte.

Il difetto è istruttivo perché nessuna riga è sbagliata in sé. Saltare un capitolo senza timbro nel ciclo del drift è corretto, perché senza un commit di partenza non c'è un diff da calcolare. L'errore sta nel non dire che lo si è saltato: un controllo che non sa misurare un caso e lo tace finisce per dichiararlo in regola, che è il contrario di ciò che ha misurato.

## La correzione

```python
senza_timbro = [c for c in capitoli if not c["commit"] and (c["interi"] or c["sezioni"])]
...
if senza_timbro:
    print("CAPITOLI SENZA TIMBRO, dichiarano coperture ma nessun commit di verifica, "
          "quindi il loro drift non si vede:")
    ...
    errori.append("%d capitoli senza timbro" % len(senza_timbro))
```

Un capitolo che reclama qualcosa senza timbro è ora un errore elencato con le coperture che dichiara. La condizione esclude i capitoli che non reclamano nulla, come la premessa di un'appendice, perché per loro il drift non ha oggetto.

La correzione non mette timbri. Mettere `verificato-al-commit: HEAD` sui 19 capitoli farebbe tacere l'errore in un minuto e trasformerebbe un punto cieco in una dichiarazione falsa, che è peggio: il punto cieco almeno non afferma nulla. Il timbro si mette capitolo per capitolo, dopo averlo riletto contro il documento che reclama, ed è il lavoro che ADR-101 apre.

## Come si è verificato che la correzione misuri il difetto

Prima della correzione la corsa a HEAD `0f82fcb` chiudeva con «1 problemi: 10 capitoli in drift», e `24-strumenti.tex` non compariva da nessuna parte. Dopo, la stessa corsa chiude con «2 problemi: 10 capitoli in drift; 19 capitoli senza timbro», e l'elenco dei 19 comprende `24-strumenti.tex` con `docs/22-strumenti.md`. I capitoli in drift sono gli stessi 10 di prima: la correzione aggiunge una classe di errore e non altera quella esistente.

## Come estendere il pattern

È la stessa famiglia del `covers-paths` di una scheda di contesto che non segue l'aggiunta di un sottoprogetto, descritto nel `CLAUDE.md`: un'area dichiarata coperta senza un modo di vedere che invecchia. La regola generale è che un controllo stampa sempre ciò che non ha potuto controllare, con il motivo, e lo conta fra gli esiti invece di lasciarlo fuori dal totale. Un «tutto in regola» vale solo quanto il perimetro su cui è stato calcolato, ed è il perimetro a dover essere scritto accanto all'esito.
