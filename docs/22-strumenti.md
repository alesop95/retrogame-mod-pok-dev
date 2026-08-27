---
tipo: nota di studio
livello: codice
tags: [strumenti, script, riproducibilità]
up: "[[index]]"
vedi_anche: ["[[05-testo-e-charmap]]", "[[04-cifratura-gen3]]", "[[21-collaudo]]", "[[SOURCES]]"]
---

# Gli strumenti del progetto

Questa nota documenta gli strumenti che esistono, che cosa fanno e come si rilanciano. Sono pochi e deliberatamente piccoli: rispondono al principio, registrato nella regola di token economy del progetto, di spingere su codice deterministico tutto ciò che non richiede comprensione semantica, e di conservarne l'esito come stato ispezionabile su disco invece che come risposta in una conversazione.

## Il presupposto comune: i disassemblati in locale

Due dei tre strumenti leggono dai disassemblati, che non stanno nel repository e non devono starci. Si ottengono con cloni superficiali, che bastano perché serve solo lo stato corrente.

```
git clone --depth 1 https://github.com/pret/pokecrystal
git clone --depth 1 https://github.com/pret/pokeemerald
git clone --depth 1 https://github.com/pret/pokered
```

Conviene tenerli fuori dal repository, per esempio in una cartella di lavoro temporanea. Il vantaggio del clone rispetto alla lettura via web è che permette di cercare nel codice invece di leggere riassunti, ed è precisamente così che sono state trovate le quattro correzioni registrate in [[SOURCES]].

## extract_charmaps.py

Sta in `pokemon-gen12-gen3-bridge-original-hardware/tools/` e genera le tabelle di codifica dei caratteri leggendo i charmap dei disassemblati.

```
python tools/extract_charmaps.py --pokecrystal PATH --pokeemerald PATH --out data
```

Produce tre file in `data/`. Il primo è la tabella di generazione 1 e 2, il secondo quella di generazione 3, ciascuna con i caratteri stampabili separati dai token di controllo e con l'indicazione del commit da cui provengono. Il terzo è la traduzione diretta fra i due spazi di codifica, che è il file che un convertitore usa davvero, e che elenca a parte i caratteri privi di destinazione.

Alla corsa corrente le cifre sono duecento caratteri stampabili per generazione 1 e 2, duecentoquarantotto per generazione 3, centoquarantasette corrispondenze e cinquantatre caratteri senza destinazione.

La proprietà importante di questo strumento non è cosa produce ma cosa si rifiuta di produrre. Prima di scrivere verifica un insieme di sentinelle, cioè i byte del terminatore, dello spazio, di A, Z, a, z, 0 e 9 in entrambe le tabelle, e se anche una sola non corrisponde non scrive nulla e riferisce lo scostamento. Se un giorno il formato dei charmap a monte cambia, il fallimento è rumoroso invece che silenzioso, che è esattamente il contrario di come si comportava la trascrizione a mano descritta in [[05-testo-e-charmap]].

## emerald_bag_decode.py

Sta in `gba-save-extraction-smeraldo/tools/` e legge un salvataggio di generazione 3 per diagnosticare lo zaino.

```
python tools/emerald_bag_decode.py PERCORSO.sav
python tools/emerald_bag_decode.py PERCORSO.sav --game frlg --json rapporto.json
```

Non scrive nulla sul salvataggio: legge, valida e riferisce. La sequenza è quella descritta in [[03-integrita-checksum]] e [[04-cifratura-gen3]], cioè individua i due slot, valida la firma e il checksum di ciascuna sezione, sceglie lo slot più recente secondo la regola del contatore, ricompone il blocco di salvataggio dalle sezioni, identifica il gioco, legge la chiave di cifratura al suo offset e smaschera le quantità dello zaino lasciando in chiaro quelle del deposito PC.

L'identificazione del gioco non si fida di un parametro: lo verifica. Il motivo viene da un caso reale documentato su Project Pokemon, dove un editor aveva identificato un salvataggio di Smeraldo come Rubino o Zaffiro e gli oggetti sono finiti negli slot sbagliati, il che è esattamente ciò che accade se si applica la maschera sbagliata, dato che Smeraldo maschera le quantità e Rubino e Zaffiro no. Lo strumento assegna un punteggio a ciascun candidato sulla base di prove indipendenti, cioè la plausibilità del conteggio della squadra al suo offset, il denaro smascherato entro il tetto, e la chiave dedotta da uno slot vuoto, e stampa le prove di tutti e tre invece di dichiarare solo il vincitore. Se due candidati pareggiano si ferma e chiede di indicare il gioco a mano, perché un'identificazione ambigua è un'informazione e non un dettaglio da risolvere tirando a sorte.

Riferisce poi le anomalie che sa riconoscere: un identificatore di oggetto fuori intervallo, una quantità nulla su uno slot occupato, una quantità oltre il tetto della tasca, uno slot popolato dopo un buco, e un identificatore duplicato nella stessa tasca. Sono cinque classi di anomalia che coprono i sintomi tipici di uno zaino manipolato da codici trucco.

Ha due verifiche incrociate che valgono più del resto. La prima è che il denaro, smascherato con la stessa chiave, deve stare sotto il suo tetto: se non ci sta, la chiave o l'offset sono sbagliati, e lo strumento lo dice invece di produrre numeri senza senso. La seconda è che uno slot vuoto in una tasca mascherata contiene la chiave stessa, quindi la chiave si ricava per una seconda via indipendente e le due si confrontano.

Sul lato Rosso Fuoco e Verde Foglia lo strumento è onesto sui propri limiti: legge la chiave al suo offset e la riferisce, ma non pretende di elencare le tasche, perché i loro offset non sono stati verificati sul disassemblato di quel gioco in questa revisione.

## Il pacchetto pokebridge

Non è uno strumento ma la prima parte del software vero, e sta in `pokemon-gen12-gen3-bridge-original-hardware/pokebridge/`. Copre gli strati dal primo al terzo della stratificazione descritta in [[20-architettura-codice]], cioè i dati generati, i modelli e i lettori e scrittori, per il solo lato Game Boy. Non ha dipendenze esterne.

I primitivi stanno in `gb.py`, e sono il posto dove vive la conoscenza che non appartiene a una generazione sola: interi a 16 e 24 bit big-endian, scomposizione dei nibble dei DV con la derivazione del quinto, byte dei PP diviso sei più due bit, e il pattern di DV che in generazione 2 significa lucentezza. I lettori e scrittori stanno in `gen1.py` e `gen2.py`, uno per generazione perché fra le due c'è un riordino e non un'estensione. La transcodifica sta in `charmap.py`, che legge le tabelle generate e non contiene alcun valore scritto a mano.

Le prove si lanciano con `python tests/run_tests.py` dalla cartella del sottoprogetto, usano solo `unittest` della libreria standard e oggi sono sessantatre. Vale la pena sapere che la prima esecuzione ne ha fatta fallire una, e che il difetto era nella prova e non nel codice: avevo scritto a mano il byte 0xA4 credendo fosse la lettera a, che invece è 0xA0. La prova ora ricava i byte dalla tabella invece di dichiararli, ed è la stessa lezione dello strumento qui sopra applicata ai test.

## Gli strumenti di infrastruttura

Nella cartella `tools/` della radice ci sono i due strumenti che servono al repository e non ai giochi. Il primo, `md-unwrap.py`, attua la convenzione di formattazione Markdown del progetto, cioè un paragrafo per riga sorgente, e ha una modalità di sola verifica per il controllo prima di un commit.

```
python tools/md-unwrap.py .
python tools/md-unwrap.py --check .
```

Il secondo, `lint-md-commands.py`, verifica che i comandi di shell dentro i blocchi recintati non siano spezzati su più righe, perché `md-unwrap` per contratto non tocca il contenuto dei blocchi recintati e quindi un comando spezzato là dentro non lo corregge nessuno.

## save-deploy.py, il cancello prima dell'hardware

Tre dei cinque sottoprogetti convergono, presto o tardi, sulla stessa operazione: prendere un file di salvataggio e metterlo su un supporto fisico, cioè una cartuccia tramite il lettore oppure la scheda SD della console modificata. È l'unica operazione irreversibile del progetto, e per questo esiste uno strumento alla radice invece di tre procedure separate dentro i sottoprogetti.

La cosa da capire di questo strumento è che non scrive, e non scriverà finché l'hardware non è presente e collaudato. Ciò che fa è la parte che si può scrivere oggi e che evita i danni. Esamina il file: la dimensione confrontata con quelle che hanno un significato, l'impronta SHA-256 che identifica il contenuto, il numero di settori che portano la firma 0x08012025, il numero di settori il cui checksum torna, l'identificazione del gioco con il margine sul secondo candidato, e i due casi degenerati del file interamente a zero e del file interamente a 0xFF, che è lo stato di una flash cancellata. Poi verifica le precondizioni della destinazione e produce il piano dei passi.

La validazione non è duplicata: lo strumento importa `emerald_bag_decode.py` dal track Smeraldo e usa le sue funzioni di validazione dei settori, di ricostruzione dello slot e di identificazione del gioco. Un secondo esemplare della stessa formula di checksum sarebbe un secondo posto dove sbagliarla.

```
python tools/save-deploy.py check "percorso/salvataggio.sav"
python tools/save-deploy.py targets
python tools/save-deploy.py plan "salvataggio.sav" --target gbxcart --backup "D:/bk1/pre.sav" --backup "E:/bk2/pre.sav"
```

La parte più importante è il cancello dei backup, che mette in atto in codice il vincolo normativo di `.claude/rules/hardware-and-perimeter.md`. Lo strumento pretende due backup dichiarati, verifica che i percorsi siano distinti, che i file esistano e siano leggibili, che la dimensione coincida con quella dell'originale e che le due impronte coincidano fra loro, e rifiuta anche il caso in cui i due backup stiano sullo stesso volume, perché un guasto del supporto li perderebbe insieme. Quando una di queste condizioni manca, il piano non viene stampato affatto: è una scelta deliberata, perché una lista di passi mostrata sotto un elenco di problemi invita a eseguirla comunque.

Il piano, quando esce, ha cinque passi nell'ordine che la regola impone: dump del contenuto attuale del supporto, confronto con i backup dichiarati, scrittura, rilettura confrontata byte per byte, e infine avvio del gioco, che è un controllo diverso dal precedente e non lo sostituisce. Poi lo strumento dichiara che la scrittura non viene tentata e dice cosa manca a quella destinazione: per la cartuccia mancano il lettore e un collaudo su un esemplare sacrificabile, per la scheda SD manca la decisione su quale percorso sia quello giusto per il titolo installato.

Il collaudo è avvenuto su un salvataggio Smeraldo sintetico generato per l'occasione, con quattordici settori firmati e coerenti, e ha verificato i tre casi che contano: il file valido identificato come Smeraldo con punteggio sei contro zero e meno tre, il rifiuto del file interamente a zero e della dimensione non riconosciuta, e il rifiuto del piano nei tre modi in cui i backup possono essere insufficienti, cioè uno solo, inesistente, oppure due sullo stesso volume.

## Che cosa manca

Il prossimo strumento naturale è il generatore della tabella dagli indici interni di generazione 1 ai numeri nazionali, che oggi non esiste e che va costruito con lo stesso metodo, cioè leggendolo dal disassemblato e verificandolo con sentinelle. La referenza tecnica lo elenca fra i punti aperti, ed è l'ultimo dato costante del progetto che sarebbe tentante trascrivere a mano.

## Cosa leggere dopo

[[20-architettura-codice]] colloca questi strumenti nella stratificazione del software, e [[21-collaudo]] racconta come il collaudo del secondo ha trovato un difetto reale.
