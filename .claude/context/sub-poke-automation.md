---
generated-from-commit: 8553f95
generated-from-branch: main
generated-date: 2026-08-26
covers-paths:
  - poke-automation-study/
last-verified-commit: 8553f95
stato: non iniziato
---

# Sottoprogetto: studio dell'automazione dei giochi Pokemon

Lo stato canonico di questo track e' questo file, insieme alla riga che lo riguarda in `memory/index.md`.

Obiettivo dichiarato allo stato attuale: studiare il progetto Pokemon Automation, che automatizza le parti ripetitive dei giochi Pokemon su Nintendo Switch pilotando la console con un microcontrollore e leggendo lo schermo con visione artificiale. Il sottoprogetto nasce come studio e non come costruzione: la cartella contiene un solo collegamento, e il primo passo e' capire che cosa di quel progetto sia riusabile qui e che cosa appartenga a un dominio diverso.

## Dove siamo

Lo studio e' cominciato il 2026-08-26 su richiesta dell'utente, per curiosita' e senza impegno di costruzione, e la prima nota e' `poke-automation-study/STUDIO-01-architettura-e-perimetro.md`. Documenta i tre strati della macchina, cioe' attuazione, percezione e decisione, i costi e le difficolta' dichiarate di ogni combinazione di controller, il perimetro che il progetto si da', e le due sovrapposizioni reali con gli altri track. Ne e' uscita una correzione a questa scheda: la sovrapposizione con il track LDN non e' solo la piattaforma, perche' quel progetto automatizza anche Rosso Fuoco e Verde Foglia nella versione Switch, che e' esattamente il gioco al centro di quel track.

La cartella `poke-automation-study/` contiene un collegamento a `https://pokemonautomation.github.io/`, letto il 2026-08-26. Il progetto copre Spada e Scudo, Diamante Lucente e Perla Splendente, Leggende Arceus, Scarlatto e Violetto, Leggende Z-A e Pokemon Casa, con oltre cento programmi di automazione. L'hardware richiesto e' un computer con scheda di acquisizione video piu' un controller costruito su microcontrollore, con ESP32, ESP32-S3 o Raspberry Pi Pico W, collegato via Bluetooth o USB. La documentazione ha sezioni su allestimento, programmi, controller, integrazione Discord e sviluppo, quest'ultima con guide su visione artificiale, riconoscimento dei colori e riconoscimento ottico dei caratteri.

## Prossimo passo concreto

Decidere che cosa questo track deve essere, perche' oggi e' un collegamento e non un obiettivo. Le tre letture possibili sono molto diverse. La prima e' studio puro, cioe' capire come si pilota una console e si legge uno schermo, e fermarsi la'. La seconda e' riuso della parte di controllo su microcontrollore, che ha una sovrapposizione reale con l'opzione D del ponte fra generazioni, dove serve comunque un microcontrollore che parli con una console. La terza e' automazione vera su Switch, che e' un obiettivo indipendente dagli altri quattro track e va dichiarato come tale.

## Che cosa si sa gia' delle sovrapposizioni

Con il track dello scambio fra GBA e Switch la sovrapposizione e' piu' concreta di quanto questa scheda dicesse alla sua stesura, e la nota di studio la corregge: oltre alla piattaforma c'e' il titolo, perche' fra i giochi automatizzati compaiono Rosso Fuoco e Verde Foglia su Switch. Resta vero che i due approcci sono opposti, perche' quel track parla il protocollo di rete locale dal PC e questo pilota il controller e guarda lo schermo, e la domanda aperta e' se i loro programmi per quel titolo tocchino lo scambio locale.

Con il ponte fra generazioni la sovrapposizione e' il microcontrollore, ma i compiti sono diversi: qui emula un controller su Bluetooth o USB, la' parla un protocollo seriale sincrono a livello di bit. Il codice non si riusa, l'esperienza di allestimento e di collaudo si'.

La visione artificiale non ha equivalenti negli altri track e sarebbe una capacita' nuova per il progetto.

## Perimetro da chiarire prima di procedere

L'automazione dei giochi in rete tocca i termini di servizio dei servizi online, e il progetto di riferimento dichiara di volere raccolte legittime. Prima di passare dallo studio alla pratica va deciso e registrato che cosa e' dentro e che cosa e' fuori perimetro per questo progetto, con la stessa esplicitezza con cui e' stato fatto per il modding della console.

## Fonti

Nel registro `SOURCES.md` con la sigla AUT, e la nota di dettaglio e' `docs/fonti/pokemon-automation.md`.
