# Sottoprogetto: studio dell'automazione dei giochi Pokemon

Studiare il progetto Pokemon Automation, che automatizza le parti ripetitive dei giochi Pokemon su Nintendo Switch pilotando la console con un microcontrollore e leggendo lo schermo con visione artificiale. Oggi e' uno studio e non una costruzione: la cartella contiene un collegamento, e il primo passo e' decidere che cosa questo track debba essere.

## Che cosa c'e' in questa cartella

Un collegamento a `https://pokemonautomation.github.io/`, che e' il punto di ingresso della documentazione del progetto. La sua sintesi, letta il 2026-08-26, sta nella nota `docs/fonti/pokemon-automation.md`, con il motivo per cui e' in archivio e i punti del progetto che tocca.

## Che cosa e' quel progetto, in breve

Automatizza oltre cento operazioni sui giochi Pokemon per Nintendo Switch, dalle generazioni ottava e nona fino a Pokemon Casa, facendo girare un bot in continuita' al posto del giocatore. Richiede un computer con scheda di acquisizione video, per vedere lo schermo, e un controller costruito su microcontrollore, con ESP32 o Raspberry Pi Pico W, per premere i tasti. Il riconoscimento degli eventi avviene per visione artificiale, per esempio individuando l'animazione che segnala un incontro raro, e in alcuni titoli anche per riconoscimento audio.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| la sintesi della fonte e perche' e' in archivio | `docs/fonti/pokemon-automation.md` |
| a che punto e' il track e quali sono le tre letture possibili | `.claude/context/sub-poke-automation.md` |
| le fonti, con il livello di affidabilita' di ciascuna | `SOURCES.md` alla radice, colonna AUT |

Lo stato canonico del track vive nella scheda, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`. Questo file dice cos'e' il sottoprogetto; quelli dicono a che punto e'.

## Due avvertenze prima di passare dallo studio alla pratica

L'automazione dei giochi in rete tocca i termini di servizio dei servizi online. Il perimetro di questo track va deciso e registrato prima di costruire qualcosa, con la stessa esplicitezza usata per il modding della console in `.claude/rules/hardware-and-perimeter.md`.

La sovrapposizione con gli altri track e' minore di quanto sembri. Con lo scambio fra GBA e Switch condivide la piattaforma e nient'altro, perche' quello parla un protocollo di rete e questo preme tasti. Con il ponte fra generazioni condivide il microcontrollore, ma la' serve a parlare un protocollo seriale a livello di bit e qui a emulare un controller: il codice non si riusa, l'esperienza di allestimento si'.
