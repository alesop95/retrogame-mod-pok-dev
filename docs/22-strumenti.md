---
tipo: nota di studio
livello: codice
tags: [strumenti, script, riproducibilita]
up: "[[index]]"
vedi_anche: ["[[05-testo-e-charmap]]", "[[04-cifratura-gen3]]", "[[21-collaudo]]", "[[SOURCES]]"]
---

# Gli strumenti del progetto

Questa nota documenta gli strumenti che esistono, che cosa fanno e come si rilanciano. Sono pochi e deliberatamente piccoli: rispondono al principio, registrato nella regola di token economy del progetto, di spingere su codice deterministico tutto cio' che non richiede comprensione semantica, e di conservarne l'esito come stato ispezionabile su disco invece che come risposta in una conversazione.

## Il presupposto comune: i disassemblati in locale

Due dei tre strumenti leggono dai disassemblati, che non stanno nel repository e non devono starci. Si ottengono con cloni superficiali, che bastano perche' serve solo lo stato corrente.

```
git clone --depth 1 https://github.com/pret/pokecrystal
git clone --depth 1 https://github.com/pret/pokeemerald
git clone --depth 1 https://github.com/pret/pokered
```

Conviene tenerli fuori dal repository, per esempio in una cartella di lavoro temporanea. Il vantaggio del clone rispetto alla lettura via web e' che permette di cercare nel codice invece di leggere riassunti, ed e' precisamente cosi' che sono state trovate le quattro correzioni registrate in [[SOURCES]].

## extract_charmaps.py

Sta in `pokemon-gen12-gen3-bridge-original-hardware/tools/` e genera le tabelle di codifica dei caratteri leggendo i charmap dei disassemblati.

```
python tools/extract_charmaps.py --pokecrystal PATH --pokeemerald PATH --out data
```

Produce tre file in `data/`. Il primo e' la tabella di generazione 1 e 2, il secondo quella di generazione 3, ciascuna con i caratteri stampabili separati dai token di controllo e con l'indicazione del commit da cui provengono. Il terzo e' la traduzione diretta fra i due spazi di codifica, che e' il file che un convertitore usa davvero, e che elenca a parte i caratteri privi di destinazione.

Alla corsa corrente le cifre sono duecento caratteri stampabili per generazione 1 e 2, duecentoquarantotto per generazione 3, centoquarantasette corrispondenze e cinquantatre caratteri senza destinazione.

La proprieta' importante di questo strumento non e' cosa produce ma cosa si rifiuta di produrre. Prima di scrivere verifica un insieme di sentinelle, cioe' i byte del terminatore, dello spazio, di A, Z, a, z, 0 e 9 in entrambe le tabelle, e se anche una sola non corrisponde non scrive nulla e riferisce lo scostamento. Se un giorno il formato dei charmap a monte cambia, il fallimento e' rumoroso invece che silenzioso, che e' esattamente il contrario di come si comportava la trascrizione a mano descritta in [[05-testo-e-charmap]].

## emerald_bag_decode.py

Sta in `gba-save-extraction-smeraldo/tools/` e legge un salvataggio di generazione 3 per diagnosticare lo zaino.

```
python tools/emerald_bag_decode.py PERCORSO.sav
python tools/emerald_bag_decode.py PERCORSO.sav --game frlg --json rapporto.json
```

Non scrive nulla sul salvataggio: legge, valida e riferisce. La sequenza e' quella descritta in [[03-integrita-checksum]] e [[04-cifratura-gen3]], cioe' individua i due slot, valida la firma e il checksum di ciascuna sezione, sceglie lo slot piu' recente secondo la regola del contatore, ricompone il blocco di salvataggio dalle sezioni, legge la chiave di cifratura al suo offset e smaschera le quantita' dello zaino lasciando in chiaro quelle del deposito PC.

Riferisce poi le anomalie che sa riconoscere: un identificatore di oggetto fuori intervallo, una quantita' nulla su uno slot occupato, una quantita' oltre il tetto della tasca, uno slot popolato dopo un buco, e un identificatore duplicato nella stessa tasca. Sono cinque classi di anomalia che coprono i sintomi tipici di uno zaino manipolato da codici trucco.

Ha due verifiche incrociate che valgono piu' del resto. La prima e' che il denaro, smascherato con la stessa chiave, deve stare sotto il suo tetto: se non ci sta, la chiave o l'offset sono sbagliati, e lo strumento lo dice invece di produrre numeri senza senso. La seconda e' che uno slot vuoto in una tasca mascherata contiene la chiave stessa, quindi la chiave si ricava per una seconda via indipendente e le due si confrontano.

Sul lato Rosso Fuoco e Verde Foglia lo strumento e' onesto sui propri limiti: legge la chiave al suo offset e la riferisce, ma non pretende di elencare le tasche, perche' i loro offset non sono stati verificati sul disassemblato di quel gioco in questa revisione.

## Il pacchetto pokebridge

Non e' uno strumento ma la prima parte del software vero, e sta in `pokemon-gen12-gen3-bridge-original-hardware/pokebridge/`. Copre gli strati dal primo al terzo della stratificazione descritta in [[20-architettura-codice]], cioe' i dati generati, i modelli e i lettori e scrittori, per il solo lato Game Boy. Non ha dipendenze esterne.

I primitivi stanno in `gb.py`, e sono il posto dove vive la conoscenza che non appartiene a una generazione sola: interi a 16 e 24 bit big-endian, scomposizione dei nibble dei DV con la derivazione del quinto, byte dei PP diviso sei piu' due bit, e il pattern di DV che in generazione 2 significa lucentezza. I lettori e scrittori stanno in `gen1.py` e `gen2.py`, uno per generazione perche' fra le due c'e' un riordino e non un'estensione. La transcodifica sta in `charmap.py`, che legge le tabelle generate e non contiene alcun valore scritto a mano.

Le prove si lanciano con `python tests/run_tests.py` dalla cartella del sottoprogetto, usano solo `unittest` della libreria standard e oggi sono sessantatre. Vale la pena sapere che la prima esecuzione ne ha fatta fallire una, e che il difetto era nella prova e non nel codice: avevo scritto a mano il byte 0xA4 credendo fosse la lettera a, che invece e' 0xA0. La prova ora ricava i byte dalla tabella invece di dichiararli, ed e' la stessa lezione dello strumento qui sopra applicata ai test.

## Gli strumenti di infrastruttura

Nella cartella `tools/` della radice ci sono i due strumenti che servono al repository e non ai giochi. Il primo, `md-unwrap.py`, attua la convenzione di formattazione Markdown del progetto, cioe' un paragrafo per riga sorgente, e ha una modalita' di sola verifica per il controllo prima di un commit.

```
python tools/md-unwrap.py .
python tools/md-unwrap.py --check .
```

Il secondo, `lint-md-commands.py`, verifica che i comandi di shell dentro i blocchi recintati non siano spezzati su piu' righe, perche' `md-unwrap` per contratto non tocca il contenuto dei blocchi recintati e quindi un comando spezzato la' dentro non lo corregge nessuno.

## Che cosa manca

Il prossimo strumento naturale e' il generatore della tabella dagli indici interni di generazione 1 ai numeri nazionali, che oggi non esiste e che va costruito con lo stesso metodo, cioe' leggendolo dal disassemblato e verificandolo con sentinelle. La referenza tecnica lo elenca fra i punti aperti, ed e' l'ultimo dato costante del progetto che sarebbe tentante trascrivere a mano.

## Cosa leggere dopo

[[20-architettura-codice]] colloca questi strumenti nella stratificazione del software, e [[21-collaudo]] racconta come il collaudo del secondo ha trovato un difetto reale.
