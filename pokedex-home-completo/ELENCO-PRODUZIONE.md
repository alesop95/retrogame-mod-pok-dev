# L'elenco unico di produzione prima della chiusura di Bank

> Documento generato da `tools/elenco-produzione.py --scrivi`. Non si modifica a mano: si rigenera dopo ogni copia nuova e dopo ogni decisione che aggiunge voci. Mette insieme le voci di ADR-108, ADR-109, ADR-110 e ADR-111, toglie quelle che le copie per HOME coprono già (`tools/pkhex-elenco-copie`, PKHeX 26.10.18) e stima quanti esemplari servono. Lo stato di ciascuna voce e il suo perché stanno nei documenti di dettaglio citati in `DA-PORTARE-PRIMA-DI-BANK.md`; qui sta l'elenco da produrre.

## Il conto

| Categoria | Voci | Coperte dalle copie per HOME | Da produrre |
|---|---|---|---|
| coppie precise | 1 | 0 | 1 |
| Fiocco Maestro | 1 | 1 | 0 |
| Smeraldo | 213 | 213 | 0 |
| asse origine | 479 | 477 | 2 |
| asse sesso e forma | 187 | 186, e 83 voci senza misura possibile | 1 |
| asse scambi | 345 | 342 | 3 |
| asse altri unici | 214 | 213 | 1 |
| asse stelle | 237 | 228, e 237 voci senza misura possibile | 9 |
| asse livelli minimi | 101 | 94 | 7 |
| pre-evoluzioni per Switch | 14 | 14 | 0 |
| mosse senza specie | 50 | 0 | 50, da assegnare a un esemplare che le impari |

Voci da produrre: 5, più 50 mosse. Esemplari stimati con la fusione delle voci compatibili: 5. Tetto, una voce un esemplare e una mossa un esemplare: 55. La stima non chiede alla libreria se una fusione sia legale, e può quindi essere ottimista; il tetto non lo è.

I posti di HOME sono 9000. Con le 5236 copie già fatte e il tetto di 2371 statici di ADR-106, che si sovrappone in parte agli altri esemplari unici e alle sfide, la stima porta a 7612 posti e il tetto a 7662. Restano rispettivamente 1388 e 1338 posti per il lavoro su Switch dopo Bank.

Le coperture degli assi sono misurate sul gioco d'origine, sull'incontro di scambio, su un incontro non selvatico, sul livello, sul sesso e sulla forma di Alola, secondo l'asse. Le altre forme dell'asse del sesso e della forma, scritte in inglese nel foglio, e le stelle del Master Dex non hanno un campo corrispondente nelle copie e sono contate tutte da produrre.

## Gli esemplari da produrre, con le voci che ciascuno chiude

| Specie | Forma | Giochi d'origine | Sfera | Cromatico | Voci chiuse |
|---|---|---|---|---|---|
| 151 Mew |  | qualunque | Cura Ball |  | Mew in Cura Ball, da Rosso Fuoco e Verde Foglia giapponesi |
| 423 Gastrodon |  | D, P, Pt |  |  | Gastrodon «» di Hayley/01000, My Pokémon Ranch |
| 466 Electivire |  | D, P, Pt |  |  | Electivire al livello 15.0, DPPt  |
| 467 Magmortar |  | D, P, Pt |  |  | Magmortar al livello 14.0, DPPt  |
| da scegliere |  | X, Y |  |  | Any Pokémon, XY: In Anistar City, an old man requests that you give him a Pokémon for him to take |

## Le voci che si completano su Switch, dopo Bank (ADR-110)

Esistono solo nei giochi per Switch, o la voce del foglio chiede un'evoluzione che si fa solo lì: nei lotti c'è la pre-evoluzione con l'origine giusta, e l'evoluzione si fa su Switch. Sono 19:

- Meltan con origine Any
- Melmetal con origine Any
- Melmetal Gigantamax Factor, origine Any
- Annihilape «» di Curtis/54118, BWB2W2
- Kingambit «Pierce» di Punky/03447, XY
- Kleavor, Bronze, RBY: ★27
- Annihilape, Bronze, RBY: ★28
- Wyrdeer, Bronze, GSC: ★40
- Ursaluna, Bronze, GSC: ★41
- Farigiraf, Bronze, GSC: ★42
- Dudunsparce, Bronze, GSC: ★43
- Dudunsparce, Platinum, GSC: ★3: Three-Segment Form.
- Mr. Rime, Bronze, DPPt: ★54
- Kingambit, Bronze, BWB2W2: ★82
- Crobat al livello 10.0, Pt + PLA
- Nuzleaf al livello 7.0, SwSh (Rolling Fields; il foglio scrive OR)
- Shiftry al livello 7.0, SwSh (Rolling Fields; il foglio scrive OR)
- Magnezone al livello 5.0, C+RB+SwSh-IoA
- Ursaluna al livello 25.0, Crystal + PLA

## Le mosse che su 3DS non si imparano

Tectonic Rage, Struggle, Light of Ruin, Clangorous Soulblaze, Zippy Zap, Splishy Splash, Floaty Fall, Pika Papow, Bouncy Bubble, Buzzy Buzz, Sizzly Slide, Glitzy Glow, Baddy Bad, Sappy Seed, Freezy Frost, Sparkly Swirl, Veevee Volley, Double Iron Bash, Breakneck Blitz, Continental Crush, Subzero Slammer, Corkscrew Crash, Devastating Drake, Never-Ending Nightmare, Acid Downpour, Black Hole Eclipse, Shattered Psyche, Twinkle Tackle, Pulverizing Pancake, Bloom Doom, Extreme Evoboost, Sinister Arrow Raid, Malicious Moonsault, Oceanic Operetta, Catastropika, 10,000,000 Volt Thunderbolt, Stoked Sparksurfer, Splintered Stormshards, Inferno Overdrive, Genesis Supernova, Guardian of Alola, Soul-Stealing 7-Star Strike, Searing Sunraze Smash, Menacing Moonraze Maelstrom, Light That Burns the Sky, Hydro Vortex, Gigavolt Havoc, Supersonic Skystrike, All-Out Pummeling, Savage Spin-Out.
