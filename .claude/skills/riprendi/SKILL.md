---
name: riprendi
description: >
  Riapre una sessione partendo da `_notes/resume-prompt.md` e verificando prima di fidarsene
  che descriva davvero il presente. Confronta l'impronta registrata a fine sessione con lo
  stato reale di git, individua che cosa una sessione caduta a metà (crash, compattazione,
  limite di utilizzo) non ha scritto, e solo dopo ricostruisce il punto di ripresa leggendo
  `.claude/memory/index.md` e `.claude/memory/pending.md`. Si esegue come primo atto di ogni
  sessione nuova. È di sola lettura sul codice e non esegue mai git add, commit o push.
disable-model-invocation: true
---

## Contesto (best-effort, pre-iniettato)

!`git log -1 --format="%h %ad %s" --date=short` !`git status --short`

## Il problema, che non è la perdita del lavoro

La procedura di ripresa di questo progetto parte da `_notes/resume-prompt.md`, che l'agente riscrive per intero alla fine di ogni sessione con lo stato raggiunto e con il prompt da incollare (`chat-non-e-memoria.md`). Quella procedura presuppone una cosa che non sempre è vera: che la sessione precedente sia arrivata alla fine. Una sessione che cade a metà, per limite di utilizzo, per un crash o perché la finestra è stata chiusa, lascia il progetto in uno stato che il file di ripresa non descrive più correttamente, tipico il caso osservato il 2026-09-21: il resume-prompt dichiarava un commit "non ancora fatto" quando quel commit era già HEAD.

Il danno non è la perdita del lavoro, che sta su disco e in git. È più sottile, e per questo peggiore: la sessione nuova legge il file di ripresa, lo prende per lo stato corrente, e costruisce sopra una premessa falsa, per esempio riproponendo comandi git già eseguiti. Nessuno se ne accorge, perché un file di ripresa vecchio ha esattamente lo stesso aspetto di uno aggiornato. Questa skill esiste per rendere meccanica quella distinzione invece di affidarla al ricordo di come sia finita l'ultima volta.

## Passo 1 - Verificare prima di leggere

Il primo comando non legge il file di ripresa: verifica che si possa credergli.

```
python tools/verifica-ripresa.py
```

Lo strumento confronta l'impronta registrata a fine sessione, cioè commit HEAD e stato dell'albero in quel momento (`_notes/lavoro/stato/impronta-sessione.json`, non tracciato), con lo stato reale di adesso. Esce con codice diverso da zero quando qualcosa diverge, e dice che cosa in ordine di quanto conta: i commit comparsi dopo l'ultima registrazione, con il loro messaggio, perché sono il lavoro che una sessione ha prodotto senza chiudersi; l'albero di lavoro diverso da quello registrato, cioè i file che quella sessione stava toccando quando è caduta o che restano da committare; e se nessuna impronta esiste ancora, lo dichiara invece di fallire in silenzio.

Se l'impronta manca (prima esecuzione di questa skill, o sessione più vecchia della sua adozione), la stessa domanda si pone a mano confrontando il commit dichiarato nelle righe di `.claude/memory/index.md` con `HEAD` e guardando `git status --short`. È meno preciso e va detto quando lo si fa, perché senza impronta non si distingue un albero sporco lasciato di proposito da uno lasciato da una caduta.

## Passo 2 - Che cosa fare di una divergenza

Una divergenza non è un difetto da correggere in silenzio: è materiale da riportare all'utente prima di qualunque altra cosa, perché solo lui sa che cosa stava facendo. La forma è breve e in ordine di gravità.

Per i commit comparsi dopo la registrazione si guarda che cosa hanno toccato, con `git show --stat`, e si dice in una riga che cosa risulta fatto. Non si assume che il work-log lo sappia: si confronta con `.claude/memory/progress.md`, e se l'ultima voce non copre quei commit lo si dichiara, perché è esattamente il lavoro che `chat-non-e-memoria.md` chiede di scrivere e che quella sessione non ha scritto.

Per i file rimasti nell'albero di lavoro si chiede, non si decide. Un file a metà può essere un lavoro da riprendere o uno da buttare, e la differenza non si legge dal contenuto.

I documenti di memoria arretrati si aggiornano subito, nello stesso giro, come vuole `rules/chat-non-e-memoria.md`, e si dichiara quali file sono stati scritti così che l'utente li rilegga nel diff prima del commit.

E per ciò che si sospetta perduto ma non si vede, cioè una decisione presa a voce nella sessione caduta, si dice chiaramente che non è ricostruibile da qui e si chiede se ce ne fosse una.

## Passo 3 - Ricostruire il punto di ripresa

Solo quando lo stato è chiaro si segue la procedura ordinaria descritta in `CLAUDE.md`, che non va duplicata qui: si legge `.claude/memory/index.md` per il fuoco corrente, poi `.claude/memory/pending.md`, poi la sola scheda `.claude/context/sub-<slug>.md` pertinente, si invoca `sync-context` se ci sono stati commit dall'ultima verifica, e si apre l'handoff del sottoprogetto solo se serve la procedura.

Il file di ripresa si legge dopo, non prima, e con la consapevolezza di quanto sia attendibile: se la verifica non ha trovato divergenze descrive il presente, e allora il prompt che contiene si può eseguire così com'è; se ne ha trovate, il file resta utile per il contesto ma il punto di ripresa vero è quello ricostruito adesso.

## Passo 4 - Il recap, e poi fermarsi

Si consegna un recap conciso in quattro righe: dove siamo, che cosa risulta fatto, che cosa la verifica ha trovato di non scritto, e il prossimo passo concreto. Poi ci si ferma e si aspetta, senza cominciare il lavoro: una sessione che riprende e si mette subito a fare toglie all'utente l'unico momento in cui può correggere una premessa sbagliata.

## Chiudere la sessione, che è la metà che rende utile l'altra

Questa skill funziona solo se qualcuno registra l'impronta, e registrarla è l'ultimo atto di una sessione, non il primo della successiva.

```
python tools/verifica-ripresa.py --registra
```

Va fatto insieme alla riscrittura di `_notes/resume-prompt.md`, cioè dopo aver scritto lo stato raggiunto e il prossimo passo, e dopo che l'utente ha fatto i propri commit, perché l'impronta fotografa lo stato in quel momento. Se si registra prima dei commit, la sessione successiva troverà una divergenza che non è una caduta ma una registrazione fatta troppo presto, e quel falso positivo insegna a ignorare il controllo, che è il modo in cui un presidio muore.

Il modo ordinario di farlo è `tools/chiudi-sessione.ps1`, che l'utente lancia dopo aver chiuso la sessione e che registra solo dopo aver verificato che il commit sia arrivato al remoto; all'agente resta di aggiornare il file di ripresa e di scrivere in `_notes/COMMIT-MSG.txt` il messaggio di commit proposto.

Una sessione che finisce senza registrare non produce un danno: produce esattamente la situazione che questa skill sa riconoscere, cioè un file di ripresa che non descrive il presente. È il comportamento voluto, ed è la ragione per cui l'impronta si registra e non si deduce.
