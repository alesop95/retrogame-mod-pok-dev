# Pokémon retro: formati, salvataggi e trasferimenti

Questo repository raccoglie ricerca tecnica, codice e procedure per leggere, verificare e trasformare dati Pokémon fra console e generazioni diverse. I sottoprogetti avanzano in parallelo: alcuni producono software, altri documentano operazioni su cartucce e console possedute. La collezione in Pokémon Home è l'obiettivo che li collega, mentre ogni sottoprogetto ha un risultato tecnico autonomo.

## La parte tecnica

| Tema | Cosa si trova qui |
|---|---|
| Formati delle generazioni 1, 2 e 3 | La [referenza byte per byte](pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md) distingue strutture di box e squadra, codifiche dei nomi, checksum, cifratura e protocollo del cavo Link. Le [tabelle dei caratteri](pokemon-gen12-gen3-bridge-original-hardware/data/) sono estratte dai disassemblati. |
| Libreria e verifiche | [pokebridge](pokemon-gen12-gen3-bridge-original-hardware/README.md) legge e scrive strutture e salvataggi delle prime tre generazioni. Le [prove](pokemon-gen12-gen3-bridge-original-hardware/tests/) includono simmetria byte per byte e casi di formato; il modulo `parco_amici.py` sintetizza il passaggio dei dati dalla terza alla quarta generazione. |
| Salvataggi su cartuccia | Il [caso Smeraldo](gba-save-extraction-smeraldo/README.md) documenta checksum delle sezioni, ricomposizione degli slot, quantità dello zaino mascherate e verifica della scrittura tramite rilettura. I salvataggi e i dump personali restano fuori da Git. |
| Distribuzioni ed eventi | Il [track degli eventi](recreate-pokemon-distributions-events/README.md) separa il dato meccanico della distribuzione dalla sua provenienza storica. Cataloghi e schede sono generati da strumenti riproducibili e confrontati con un verificatore indipendente. |
| Catena verso Home | Il [track della collezione](pokedex-home-completo/README.md) collega ottenibilità, forme, eventi, vincoli di trasferimento e lotti prodotti. Le tabelle CSV sono in [`data/`](pokedex-home-completo/data/) e i documenti generati dichiarano il programma che li produce. |

Il [percorso di studio](docs/index.md) spiega i meccanismi in ordine didattico; la [tesi](tesi/README.md) li compone in un documento unico. Il [catalogo dei documenti](MAPPA-DOCUMENTI.md) distingue materiale autorato, generato, normativo e di stato.

## Fonti e tracciabilità

Il [registro unico delle fonti](SOURCES.md) indica per ciascuna fonte che cosa documenta, il livello di affidabilità e i sottoprogetti che la usano. Il suo indice generato collega fonti, documenti e capitoli della tesi. La [mappa relazionale](docs/fonti/index-fonti.md) rende navigabili abstract e collegamenti; il [registro delle prove](docs/23-prove-eseguite.md) dice quali verifiche sono state eseguite davvero. Per i formati, le note sui disassemblati di [Rosso](docs/fonti/pokered.md), [Cristallo](docs/fonti/pokecrystal.md) e [Smeraldo](docs/fonti/pokeemerald.md) sono punti di ingresso concreti.

Una fonte catalogata e una fonte letta sono stati diversi. Le note indicano la differenza e le affermazioni di formato vengono confrontate con codice o documentazione primaria prima di entrare nella referenza.

<!-- indice-pubblico:inizio -->
## Sottoprogetti

| Area | Punto di ingresso |
|---|---|
| `3ds-related/` | [modding del Nintendo 3DS e dump delle cartucce possedute](3ds-related/README.md) |
| `cart-battery-restoration/` | [conservazione del supporto e sostituzione della batteria](cart-battery-restoration/README.md) |
| `gba-save-extraction-smeraldo/` | [correzione dell'inventario corrotto di Pokemon Smeraldo](gba-save-extraction-smeraldo/README.md) |
| `gba-switch-pokemon-trading/` | [trading wireless locale fra PC e Nintendo Switch](gba-switch-pokemon-trading/README.md) |
| `generation-from-switch/` | [generazione e scambio dai giochi su console moderna](generation-from-switch/README.md) |
| `poke-ace/` | [esecuzione di codice arbitrario come via di generazione](poke-ace/README.md) |
| `poke-automation-study/` | [studio dell'automazione dei giochi Pokemon](poke-automation-study/README.md) |
| `pokedex-home-completo/` | [Pokedex completo in Pokemon Home](pokedex-home-completo/README.md) |
| `pokemon-gen12-gen3-bridge-original-hardware/` | [ponte Pokemon da Gen 1 e 2 verso Gen 3 su hardware originale](pokemon-gen12-gen3-bridge-original-hardware/README.md) |
| `recreate-pokemon-distributions-events/` | [ricreazione delle distribuzioni e degli eventi Pokemon](recreate-pokemon-distributions-events/README.md) |
<!-- indice-pubblico:fine -->

## Riprodurre e mantenere

Dalla radice del repository, `python pokemon-gen12-gen3-bridge-original-hardware/tests/run_tests.py` esegue le prove della libreria senza dipendenze esterne. `python tools/check-thesis-coverage.py` controlla la copertura dei documenti nella tesi. `python tools/indice-fonti-unico.py --check` controlla l'indice delle fonti e `python tools/build-source-map.py --check` le note della mappa relazionale. `python tools/aggiorna-readme.py` aggiorna l'indice dei sottoprogetti qui sopra dai README presenti, e `python tools/aggiorna-readme.py --check` ne verifica l'allineamento e i collegamenti locali. Il testo tecnico introduttivo si aggiorna quando cambiano i risultati del progetto; l'indice viene rigenerato nello stesso giro.
