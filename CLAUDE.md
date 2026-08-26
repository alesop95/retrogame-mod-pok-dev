# retrogame-mod-pok-dev

## Cos'e' questo progetto

Un progetto unico che raccoglie piu' sottoprogetti paralleli di retrogaming e modding, quasi tutti legati ai Pokemon. Non sono fasi di una sequenza: sono obiettivi diversi che avanzano in parallelo, ciascuno con il proprio handoff, e il progetto e' pensato per accoglierne di nuovi nel tempo.

Oggi i track sono cinque. Il modding di un Nintendo 3DS con dump delle cartucce possedute. La correzione di un inventario corrotto sulla cartuccia di Pokemon Smeraldo, agendo sul salvataggio estratto fisicamente. Un ponte software fra le generazioni 1 e 2 e la generazione 3 su hardware originale, che e' il primo a essere diventato vero codice e oggi ha un pacchetto con la sua suite di prove. Uno scambio fra GBA e Switch, in ricerca e destinato anch'esso a produrre codice. E lo studio dell'automazione dei giochi su Switch, aggiunto il 2026-08-26 e ancora da definire nel suo scopo.

Tre dei cinque sono runbook operativi su hardware fisico, dove gli errori sono irreversibili: e' la ragione per cui `rules/hardware-and-perimeter.md` esiste ed e' normativa.

## Procedura di ripresa in una sessione nuova

Leggi `.claude/memory/index.md` per primo. La riga del fuoco corrente dice su quale sottoprogetto si sta lavorando adesso, e il blocco sotto dice a che punto e' ciascuno degli altri. E' la fonte di verita' unica: se una scheda o un handoff dicono altro, vale l'indice.

Subito dopo leggi `.claude/memory/pending.md`, che e' il registro di tutto cio' che e' in sospeso: materiale atteso dall'utente, credenziali da configurare, fonti in sospeso da ricordare a ogni sessione, strumenti da richiamare quando si verifica una condizione, debito di lettura, punti tecnici aperti e blocchi materiali. L'utente non deve essere il sistema di memoria del progetto: le voci pertinenti al lavoro in corso si ricordano senza attendere che le chieda, e quelle marcate come da ricordare sempre si ripetono comunque.

Poi leggi la scheda `.claude/context/sub-<slug>.md` del solo sottoprogetto pertinente, che sta sotto le trenta righe e contiene stato, prossimo passo e decisioni aperte. Apri l'handoff del sottoprogetto soltanto se ti serve la procedura, il troubleshooting o le fonti: l'handoff e' conoscenza e non stato, ed e' lungo.

Se il lavoro tocca piu' track o l'infrastruttura, leggi `.claude/context/current-work.md`. La conoscenza tecnica invece non e' stato e non si rilegge a ogni sessione: le fonti stanno in `SOURCES.md` e il percorso di studio in `docs/index.md`, e si aprono quando servono al task. Prima di dare per buona una scheda, se ci sono stati commit dall'ultima verifica, invoca `sync-context`.

## Indice dei file satellite tracciati

Memoria e stato:

```
.claude/memory/index.md       snapshot, fuoco corrente e stato di verifica delle schede
.claude/memory/progress.md    work log append-only, cronologico inverso
.claude/memory/decisions.md   decisioni in forma ADR-lite, append-only
.claude/memory/pending.md     tutto cio' che e' in sospeso, modificabile e non append-only
```

Schede trasversali, cioe' cio' che vale per tutto il progetto:

```
.claude/context/STACK.md                inventario di hardware e toolchain, e alternative escluse
.claude/context/design-and-security.md  segreti non ruotabili, dati personali, perimetro, rischi
.claude/context/dev-testing.md          protocollo di verifica su hardware reale
.claude/context/deployment.md           non applicabile allo stato attuale, covers-paths vuoto
.claude/context/current-work.md         tabella dei track paralleli e feature in corso
.claude/context/roadmap.md              cosa sblocca cosa, e come si aggiunge un sottoprogetto
```

Schede verticali, una per sottoprogetto:

```
.claude/context/sub-3ds-modding.md         modding 3DS e dump delle cartucce
.claude/context/sub-smeraldo-save-fix.md   correzione dell'inventario di Pokemon Smeraldo
.claude/context/sub-gen12-gen3-bridge.md   ponte fra generazioni su hardware originale
.claude/context/sub-gba-switch-trading.md  scambio fra GBA e Switch, non iniziato
.claude/context/sub-poke-automation.md     studio dell'automazione su Switch, non iniziato
```

Fuori da `.claude/`, alla radice e nelle cartelle dei sottoprogetti, stanno la conoscenza tecnica e gli strumenti. Sono materiale di riferimento e non di stato, quindi non entrano nel ciclo di verifica delle schede.

```
<slug>/README.md                              punto di ingresso di ciascun sottoprogetto, con l'instradamento
SOURCES.md                                    registro delle fonti, con il sottoprogetto servito da ciascuna
docs/index.md                                 indice del percorso di studio tecnico, leggibile come vault Obsidian
docs/fonti/index-fonti.md                     mappa relazionale delle fonti, con abstract e grafo
reports/README.md                             report di milestone in LaTeX, uno per traguardo chiuso
pokemon-gen12-gen3-bridge-original-hardware/  referenza byte per byte, tabelle generate e loro generatore
gba-save-extraction-smeraldo/tools/           diagnostica dello zaino su un salvataggio Gen 3
```

Le regole normative stanno sotto `.claude/rules/` e le skill del motore sotto `.claude/skills/`. Fra le regole, `hardware-and-perimeter.md` e' specifica di questo progetto e va letta prima di qualsiasi operazione su hardware, mentre `web-sources-not-fetchable.md` dice cosa fare quando una fonte esiste ma non si riesce a recuperarla, ed e' generale abbastanza da valere fuori da questo progetto.

Gli handoff restano nelle cartelle dei rispettivi sottoprogetti, che e' voluto e motivato in ADR-003: `3ds-related/handoff/` e `gba-save-extraction-smeraldo/handoff/`. Il sottoprogetto del ponte non ha piu' un handoff, perche' la sua conoscenza e' stata verificata sul sorgente e assorbita nella referenza `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md` e nel percorso di studio sotto `docs/`, come registrato in ADR-013.

## Come si aggiunge un sottoprogetto

Si crea la cartella con un nome in ASCII puro, si istanzia una scheda da `.claude/templates/context/sub-subproject.md` con il `covers-paths` sulla nuova cartella, e si aggiunge una riga in tre posti: la tabella di verifica e il blocco del punto di ripresa in `memory/index.md`, e la tabella dei track in `current-work.md`.

C'e' un quarto passo che non va dimenticato, e va detto perche' dimenticarlo non produce alcun errore visibile: il `covers-paths` delle schede trasversali che parlano del nuovo track va esteso alla sua cartella. Una scheda che descrive un'area senza dichiararla fra i percorsi coperti e' un punto cieco permanente, perche' `sync-context` non segnalera' mai un drift su un'area che nessuno dichiara di coprire, e la scheda resta indefinitamente verde mentre invecchia. E' esattamente cio' che era accaduto a `dev-testing.md`, che ha dichiarato per un giorno l'assenza di test automatici mentre 63 prove passavano.

## Apprendimenti recenti

Questa sezione e' un buffer, non un archivio: quando una voce diventa strutturale, migra nella scheda o nell'ADR che le compete e sparisce da qui.

- [2026-08-24] Il `covers-paths` va scritto come prefisso di cartella con lo slash finale e non come glob: e' un pathspec git, dove i wildcard non si comportano come in `.gitignore`.
- [2026-08-24] `user.useConfigOnly` e' true a livello globale su questa macchina, quindi senza identita' locale il commit fallisce con un errore poco chiaro. E' un guard-rail voluto, non un problema.
- [2026-08-24] `core.autocrlf` e' false globalmente, quindi non serve alcun `.gitattributes`; aggiungerne uno con `text=auto` introdurrebbe un problema di riscrittura dei fine riga che oggi non esiste.
- [2026-08-25] Su dati di gioco l'enciclopedia non basta: quattro affermazioni su cui il progetto avrebbe costruito codice erano sbagliate, e sono emerse solo clonando i disassemblati e cercando nel sorgente. Il clone superficiale e' quindi il primo passo di qualsiasi verifica, non l'ultimo.
- [2026-08-25] Reddit non e' raggiungibile dagli strumenti di sessione e YouTube restituisce una pagina di consenso invece del contenuto: si possono elencare come luoghi dove cercare, non citare come fonti lette.

## Vincoli di team

Le operazioni di `git add`, commit e push restano sempre manuali. L'agente prepara i file e consegna i comandi, non committa. Il `settings.json` lo impone anche in negazione.

Ogni paragrafo di prosa nei file Markdown si scrive come una riga sorgente unica, per quanto lunga: l'a capo separa due paragrafi, mai due frasi. Si verifica con `python tools/md-unwrap.py --check .`

Le schede di `context/` e i file di `memory/` non si aggiornano da soli: li aggiorna l'utente, o l'agente su richiesta esplicita, cosi' che il versionamento resti sotto controllo umano.

Nessun dump di cartuccia, nessun backup di salvataggio, nessun materiale di chiave console-unica e nessun media entra in git. Vedi ADR-005 e il blocco di dominio del `.gitignore`.
