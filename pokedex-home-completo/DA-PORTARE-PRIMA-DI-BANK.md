# Che cosa va portato prima della chiusura di Bank, e a che punto siamo

> Documento autorato, nato il 2026-11-03 su richiesta del proprietario, che vuole lo stato sempre leggibile per sapere il passo successivo. Si aggiorna a ogni giro e a ogni copia nuova. Regola il lavoro di ADR-106, ADR-107 e ADR-108: ciò che le copie già in HOME non coprono e che dopo la chiusura di Bank, il 26 febbraio 2027, non si potrà più ottenere si genera con esemplari dedicati, da mettere nei lotti dei giri successivi. Il giro 1, 930 esemplari, è già in HOME e non si tocca.

## Le misure, e da dove vengono

Le misure sono prese il 2026-11-03 sulle sette copie giudicate con `tools/pkhex-elenco-copie`, libreria PKHeX 26.10.18, in `_notes/lavoro/giudizi-copie/dopo-bfe89c7-mosse.json`. Lo stesso giorno lo strumento ha imparato a estrarre le mosse e l'abilità di ogni esemplare. Le fonti degli elenchi sono cinque, tutte registrate in `SOURCES.md`; la quinta, letta per ultima, è la più completa: l'articolo di Bulbapedia «Challenge (HOME)», revisione 4643183, con 269 sfide, 204 Pokémon, 60 di scambio e 5 altre. La prima è il post di r/PokemonHome `1voa411`, del 2026-08-14. La seconda è la pagina delle sfide di Serebii. La terza è il foglio comunitario «Bank Closing all possible things checklist V0.5», con le schede «Home Challenges from bank» e «Locked Shinies». La quarta è il foglio del post `1bwr0l1`, con le sezioni «HOME Challenges» e «What to transfer up from the 3DS before Bank Closes». Le sezioni dei fogli sono estratte in `_notes/fonti/raccolte/fogli-sfide-bank-2026-11-03/home-tasks/`.

## Lo stato per voce

| Voce | Totale | Coperte dalle copie per HOME | Da generare | Dove sta il dettaglio |
|---|---|---|---|---|
| Sfide di HOME che dipendono da Bank | 47 | 23 | 24 | `SFIDE-BANK.md`, generato da `tools/sfide-bank.py --scrivi` |
| Mosse registrabili solo da giochi passati da Bank | 63 | 51 | 12 | qui sotto |
| Abilità registrabili solo da giochi passati da Bank | 3 | 3 | 0 | Battle Bond, Soul-Heart, Victory Star |
| Cromatici bloccati, ottenibili solo da Bank | 8 | 3 | 5 | qui sotto |
| Specie che il foglio del 2024 dava «solo tramite GO» | 9 | 2 | 0 | qui sotto |

Le 24 sfide da generare chiedono quasi tutte una specie con un gioco d'origine preciso: i leggendari di Diamante, Perla e Platino, di Rubino Omega e Zaffiro Alpha, di Rubino, Zaffiro e Smeraldo, di HeartGold e SoulSilver, di Sole e Luna e di Nero 2 e Bianco 2. Ci sono poi gli starter di Rubino Omega e Zaffiro Alpha e di Diamante, Perla e Platino con le loro evoluzioni, Cosmog e Cosmoem, gli starter e Pikachu della Console Virtuale di prima generazione, e Litwick passato con Poké Transporter. Sono statici, doni e starter dei giochi, quindi la loro produzione è la prima parte di quella di ADR-106.

Le 12 mosse da generare, cioè quelle che nessun esemplare delle copie per HOME conosce, sono Heal Block, Heal Order, Ion Deluge, Mirror Shot, Powder, Rototiller, Sky Drop, Spotlight, Steamroller, Synchronoise, Telekinesis e Hyperspace Fury. Servono alle sfide del Pokédex delle mosse di HOME, e dopo Bank non si registrano più. Per ciascuna si genera un esemplare legale che la conosca, giudicato dalla libreria.

I 5 cromatici bloccati da generare sono Mew, Celebi, Spinda, Tipo Zero e Naganadel; Pikachu, Silvally e Poipole cromatici sono già nelle copie.

Delle 9 specie che il foglio del 2024 dava ottenibili dopo Bank solo con Pokémon GO, Pansage e Simisear sono già nelle copie. Le altre 7 sono Patrat, Watchog, Simisage, Pansear, Panpour, Simipour e Furfrou: secondo la libreria si trovano in Leggende Z-A, e due guide lette il 2026-11-03 lo confermano, Thonky e Gamer Guides. Quindi hanno una via dopo Bank, Z-A verso HOME, e non richiedono esemplari dedicati. Il foglio del 2024 è anteriore a Z-A, che è del 2025.

Le altre 281 specie dalla 1 alla 809 assenti dalle copie per HOME hanno, secondo le tabelle della libreria, almeno un gioco per Switch che le contiene, quindi non dipendono da Bank. L'elenco è in `_notes/lavoro/giudizi-copie/specie-assenti-presenza-switch.tsv`.

## Che cosa resta aperto

La sfida «Register Pulverizing Snorlax» è identificata su Bulbapedia, uno Snorlax da evento, ed è coperta dallo Snorlax di Nihonbashi della copia di Ultraluna. Le sfide di Rosso Fuoco e Verde Foglia «for Nintendo Switch», cioè Caterpie e la sua serie, Chansey e Tauros, Lapras e Porygon, chiedono l'origine Switch: non dipendono da Bank e vanno nel lavoro su Switch. «Register 100 different species of Pokémon that live in the Alola Region» risulta coperta con 121 specie d'origine Alola, ma va confermato che almeno 100 siano nel Pokédex di Alola. Il 2026-11-03 sono stati letti l'annuncio ufficiale e l'articolo di Dexerto su ciò che si perde con la chiusura. L'annuncio dice «26 febbraio 2027 alle 10:00» senza fuso. RPG Site riporta l'annuncio americano, 25 febbraio alle 19:00 PST, cioè le 04:00 italiane del 26 febbraio, che coincide con la data del progetto. Notebookcheck dà il 27. Vale la più prudente: i passaggi si chiudono entro la sera del 25 febbraio. Dexerto aggiunge tre categorie che questo controllo non copre ancora. La prima sono i fiocchi ottenibili solo da giochi vecchi: Artist, Legend, National, Earth, Contest Memory e Battle Memory, i fiocchi dei Campioni di Kalos, Hoenn e Alola, Training, Skillful e Expert Battler, Battle Royal Master, i due della Battle Tree, il Campione di terza generazione, Country, World e Battle Champion. Vanno confrontati con l'asse dei fiocchi di `FIOCCHI.md`, estraendo i fiocchi degli esemplari dalle copie. La seconda sono alcune voci cromatiche del Pokédex di HOME (Victini, Vivillon Motivo Poké Ball, Floette Fiore Eterno, Hoopa), riportate da una sintesi automatica e da verificare sulla pagina prima di produrle. La terza è il premio Time Travel di Diamante Lucente e Perla Splendente, che chiede un Pokémon originario di Diamante, Perla o Platino: le copie per HOME ne hanno 172, quindi è coperto.

## Il passo successivo

L'agente scrive l'elenco di produzione dei giri dedicati: le 24 sfide, le 12 mosse e i 5 cromatici, con un esemplare legale per voce, generato con la libreria e giudicato. Poi li scrive in una copia nuova, che entra nel calendario dopo i giri 2 e 3 di Rubino Omega e prima del passo 3. Il proprietario intanto prosegue con il passo 2, i giri 2 e 3, che non dipendono da questo lavoro.
