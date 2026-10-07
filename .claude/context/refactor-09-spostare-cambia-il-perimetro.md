# Refactor 09. Spostare un file cambia il perimetro di un controllo

> Scheda di dettaglio della voce 9 di `studio-didattico-master.md`. Entra nell'esecuzione della mappa di riorganizzazione del 2026-10-07 (`_notes/riorganizzazione/MAPPA.md`), nella configurazione di `tools/verifica-link-progetto.py` e in `tools/conta-letti.py`.

## Il caso

La mappa di riorganizzazione, scritta il 2026-10-05 e approvata il 2026-10-07, prevedeva fra gli spostamenti di materiale locale la voce U5: cinque file di lavoro della verifica delle righe di `SOURCES.md` del 2026-10-05, dalla radice di `_notes/fonti/` a `_notes/fonti/consegne/2026-10-05-righe-sources/`. Per la mappa il rischio era «nullo», perché nessun file del progetto citava quei percorsi. Eseguito lo spostamento, `verifica-link-progetto.py --check --senza-rete` è passato da verde a «15 indirizzi non classificati», con uscita 1.

La causa sta nella configurazione dello strumento, `tools/verifica-link-progetto.json`:

```json
"cartelle_non_tracciate": [
  { "percorso": "_notes", "saltate_in_radice": ["fonti", "lotti", "salvataggi", "media", "tmp"], ... },
  { "percorso": "_notes/fonti/consegne", "saltate": ["testo", "estratti", "sub"], "estensioni": [".md", ".txt", ".url"] }
]
```

Sotto `_notes/fonti/` lo strumento non guarda, salvo che in `consegne/`, dove stanno le consegne del proprietario, che possono citare fonti nuove. I file di righe contenevano indirizzi troncati alla parentesi aperta, cioè frammenti di lavoro e non citazioni: nella radice di `fonti/` erano fuori dal perimetro, in `consegne/` ci sono entrati. La destinazione è stata cambiata in `_notes/fonti/verifiche/2026-10-05-righe-sources/`, che sta sotto `fonti/` e fuori da `consegne/`, e lo scostamento dalla mappa è scritto nella mappa stessa.

## Il secondo caso, nello stesso giro

Lo script `conta-letti.py`, spostato in `tools/` con la voce U1, alla prima corsa ha dato una riga di `SOURCES.md` aperta, mentre il 2026-10-05 erano zero. La riga era letta, ma il suo esito era scritto come «clone superficiale [...] Coincide», e il vocabolario dello strumento conosceva «clonato» e non «clone»:

```python
LET = re.compile(r'\b(lett[oaie]|...|clonat|clone superficiale|verificat|...)', re.I)
```

È lo stesso genere di difetto del primo: lo strumento misurava bene ciò che conosceva, e la sua risposta dipendeva da un perimetro implicito, qui lessicale, che nessuno aveva dichiarato.

## Come si è verificato

Per lo spostamento, il controllo dei collegamenti è tornato a «Tutti gli indirizzi citati sono classificati» con uscita 0 dopo la nuova destinazione. Per lo strumento, l'uscita della copia tracciata è stata confrontata con quella dello script originale prima della correzione (identica, una riga aperta), e dopo la correzione la conta è a zero. Tutti i controlli della sezione 5 della mappa sono verdi, e `md-unwrap --check .` su tutto il disco è passato da 740 file da modificare a zero grazie ai marcatori di U11.

## Come estendere il pattern

Una mappa di riorganizzazione valuta il rischio di uno spostamento cercando chi cita il percorso; va cercato anche chi lo percorre, cioè ogni controllo che ha un perimetro per cartelle, e il percorso di destinazione si confronta con quel perimetro prima di spostare. E dopo ogni riordino si rieseguono tutti i controlli, non solo quelli che il riordino sembra toccare: quello che è caduto qui non aveva nulla a che fare con i file spostati, se non la cartella in cui sono finiti.
