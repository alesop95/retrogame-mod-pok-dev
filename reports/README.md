# Report di milestone

Questa cartella contiene un report tecnico per ciascuna milestone chiusa, in LaTeX, con taglio da ingegneria delle telecomunicazioni. Non e' documentazione di stato ne' di conoscenza: quelle vivono rispettivamente in `.claude/memory/` e in `docs/`. Un report e' un documento datato che fotografa cosa e' stato stabilito, con quale metodo, e cosa resta aperto al momento in cui la milestone si chiude, ed e' il formato giusto per essere letto da fuori o riletto fra sei mesi.

## Che cosa distingue un report dal resto

Le note di `docs/` spiegano un concetto e restano valide finche' non cambia il concetto. Il diario di `progress.md` registra cosa e' stato fatto in una sessione. Un report invece argomenta: parte dall'inquadramento del problema, dichiara il metodo, presenta i risultati con i loro numeri, e chiude con i limiti. E' la forma che rende verificabile un lavoro da parte di chi non lo ha svolto.

Il taglio disciplinare non e' un vezzo. Il ponte fra generazioni e', in buona parte, un problema di comunicazione su un canale seriale sincrono, e trattarlo con il vocabolario delle telecomunicazioni rende visibili cose che il vocabolario del reverse engineering nasconde: la delimitazione delle trame, la trasparenza dei dati, il confronto fra inserimento di byte in banda e correzione fuori banda, la capacita' del canale e il tempo di trasferimento, la rilevazione d'errore e le sue debolezze. Il primo report sviluppa esattamente questo confronto, e ne esce un'osservazione che nessuna fonte consultata faceva.

## Come si compila

Serve una distribuzione TeX con `pdflatex` e `latexmk`. Su questa macchina c'e' TinyTeX, e il percorso dei binari va aggiunto all'ambiente perche' non e' sempre sul PATH della shell.

```
latexmk -pdf milestone-01-formati-e-lato-gameboy.tex
```

L'engine e' fissato a `pdflatex` in `.latexmkrc`, non a LuaLaTeX, e la scelta e' deliberata: il preambolo usa soltanto pacchetti presenti in una TinyTeX minimale, senza font di sistema, cosi' che il report compili anche su una macchina diversa da questa. Dove un pacchetto mancava e non era essenziale e' stato rimosso invece di aggiunto, e dove serviva una macro semplice e' stata definita con `\providecommand` invece di importare un pacchetto intero: le due decisioni sono annotate nel preambolo con la loro motivazione.

## Che cosa e' tracciato

Sono tracciati il sorgente `.tex`, il preambolo condiviso e la configurazione di `latexmk`. Non sono tracciati il PDF, che e' un artefatto rigenerabile ed e' escluso dalla politica sui binari di ADR-005, ne' i file ausiliari, esclusi da un blocco dedicato del `.gitignore`.

## Report esistenti

| Milestone | File | Contenuto |
|---|---|---|
| 1 | `milestone-01-formati-e-lato-gameboy.tex` | caratterizzazione dei formati sulle tre generazioni, il canale seriale trattato come problema di comunicazione, la conversione come soddisfacimento di vincoli, e lo strato di lettura e scrittura del lato Game Boy con la sua verifica; otto pagine |
