# Refactor 12. Un generatore che scrive deve sapere che cosa toglie

> Scheda di dettaglio della voce 12 di `studio-didattico-master.md`. Entra nel modo in cui i tre generatori delle fonti scrivono i loro file, nel difetto che questo modo ha prodotto l'11 novembre 2026 e nella funzione comune che lo sostituisce.

## Il caso

La tabella `FONTI` di `tools/build-source-map.py` è la sorgente unica delle fonti, e tre programmi ne derivano una vista: `build-source-map.py` scrive una nota per fonte in `docs/mappa-fonti/`, `build-bibliography.py` scrive `tesi/bibliografia.tex`, `indice-fonti-unico.py` riscrive il blocco fra due commenti dentro `SOURCES.md`. Chi vuole cambiare una vista cambia la tabella e rigenera. Il contratto regge finché nessuno scrive a mano dentro una vista, e in un progetto che cresce per mesi qualcuno lo fa.

## Com'era

Tutti e tre scrivevano il file intero. Il blocco di `SOURCES.md`, per esempio:

```python
vecchio = io.open(REGISTRO, encoding="utf-8").read()
nuovo = inserisci(vecchio, blocco)
...
io.open(REGISTRO, "w", encoding="utf-8", newline="\n").write(nuovo)
```

dove `inserisci` sostituisce tutto ciò che sta fra `INIZIO` e `FINE`. Sette sezioni autorate, aggiunte in coda al file fra ottobre e novembre, stavano dopo `INIZIO` e prima del titolo del blocco: per il programma erano blocco, e la rigenerazione le ha tolte. Il controllo `--check` confrontava soltanto `vecchio != nuovo` e stampava «disallineato: il blocco va rigenerato», cioè chiedeva proprio il gesto che le cancellava.

Nella bibliografia lo stesso schema aveva due casi: la voce `\bibitem{pkhex-core-libreria}`, scritta a mano il 2026-10-07, e una frase aggiunta all'abstract di `pokeruby`, che portava anche un carattere di tabulazione al posto di `\t`, perché uno strumento di scrittura aveva letto `\texttt` come sequenza di escape.

## Com'è

`tools/rigenera_sicuro.py` espone `scrivi(percorso, nuovo, schema, forza)`. Prima di sovrascrivere copia i byte attuali in `_notes/archivio/rigenerazioni/<data-ora>-<nome>` e li rilegge; poi calcola le righe del vecchio che il nuovo non contiene, come multinsieme, e se fra esse ce n'è una che corrisponde a `schema` si ferma:

```python
perse = perdite_strutturali(vecchio, nuovo, schema)
if perse and not forza:
    print("FERMO: la rigenerazione di %s toglierebbe %d righe strutturali ..." % (...))
    return 1
```

I chiamanti dichiarano che cosa è strutturale: `^#{1,6} ` per le note e per il blocco di `SOURCES.md`, `^\\bibitem\{` per la bibliografia. Il `--check` di bibliografia e indice stampa anche `avviso(...)`, cioè quante righe la rigenerazione toglierebbe e quali fra esse sono strutturali. `--forza` resta per il caso voluto, e anche allora l'archivio conserva la versione precedente.

## Perché due difese e non una

Lo schema strutturale ferma i casi grossi, una sezione o una voce intera, ma non vede una frase aggiunta a una riga che il generatore produce comunque: la riga cambia, non sparisce un titolo. Quel caso lo copre l'archivio, che non decide niente e conserva tutto. Una difesa sola avrebbe lasciato scoperto uno dei due casi dell'11 novembre.

## La prova

`python tools/rigenera_sicuro.py --autotest` copre scrittura, file invariato, fermo su un titolo, file intatto dopo il fermo, `--forza` con archivio, voce bibliografica tolta, conteggio a multinsieme. I due casi reali sono stati rieseguiti su copie dei file com'erano: il blocco di `SOURCES.md` al commit `3a9020a` si ferma elencando i sette titoli e resta identico byte per byte; la bibliografia di prima della correzione, rigenerata dalla tabella di allora, si ferma su `\bibitem{pkhex-core-libreria}`.

## Che cosa resta

`chiudi` non esegue i `--check` dei tre generatori, ed è il motivo per cui la bibliografia era disallineata con i controlli verdi: lo script viene dal template, e la mancanza è registrata come lezione per il template. Finché non cambia, l'agente li esegue prima di proporre un commit, come prescrive il `CLAUDE.md` del progetto.
