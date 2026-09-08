# Spoglio del corpus: che cosa le fonti nominano e noi non abbiamo

> Documento generato da `tools/spoglio-corpus.py`. Non si modifica a mano: si rigenera. Nasce dalla richiesta di leggere tutte le fonti del corpus come controllo incrociato, eseguita con il metodo del predicato invece che con la lettura in sequenza.

Sono stati spogliati 292 documenti scaricati. Il riconoscimento e' sui vocabolari chiusi del dominio, cioe' i nomi inglesi di specie, mosse e fiocchi letti dalle tabelle del verificatore. Due limiti vanno dichiarati perche' si vedono nell'esito: i nomi corti o ambigui sono esclusi per non produrre falsi positivi, e un nome scritto in una lingua diversa dall'inglese non viene riconosciuto affatto.

La direzione che interessa e' una sola, cioe' cio' che il corpus nomina e i nostri lotti non contengono. La direzione opposta non e' un difetto e non si riferisce, perche' il corpus non pretende di essere completo.

## Specie

Il corpus nomina 1000 specie distinte. I nostri lotti ne contengono 166, e 835 delle nominate non vi compaiono. L'assenza non e' di per se' una lacuna, perche' un lotto di distribuzioni non ha ragione di contenere ogni specie del gioco: e' una lista di controllo, e le voci che pesano sono quelle che compaiono in molti documenti.

| Specie | Documenti che la nominano | Uno dei documenti |
|---|---|---|
| Ditto | 39 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Gyarados | 32 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Raichu | 30 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Unown | 28 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Gengar | 27 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Snorlax | 26 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Togepi | 26 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Dratini | 24 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Growlithe | 23 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Heracross | 21 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Vulpix | 21 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Latios | 20 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Pidgey | 20 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Abra | 19 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Mr. Mime | 19 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Porygon | 19 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Quagsire | 19 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Ekans | 18 | esterni/bluemoonfalls.com/03abf808-dv-breeding-for-shinies-blue-moon-falls.md |
| Greninja | 18 | esterni/serebii.net/905c290f-pok-mon-scarlet-violet-tera-raid-battle-events.md |
| Hitmonlee | 18 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Mareep | 18 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Zorua | 18 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Blissey | 17 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Butterfree | 17 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Lapras | 17 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Persian | 17 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Tentacool | 17 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Arbok | 16 | esterni/bluemoonfalls.com/03abf808-dv-breeding-for-shinies-blue-moon-falls.md |
| Chikorita | 16 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Clefairy | 16 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Electrode | 16 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Latias | 16 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Shuckle | 16 | esterni/buriedrelic.neocities.org/1514790c-shiny-hunting-in-gale-of-darkness-buried-relic.md |
| Slowbro | 16 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Sudowoodo | 16 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Teddiursa | 16 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Venusaur | 16 | esterni/glitchcity.wiki/6f028319-coin-case-glitches-glitch-city-wiki.md |
| Vivillon | 16 | esterni/raw.githubusercontent.com/c5b82a3e-https-raw-githubusercontent-com-wiki-flagbrew-pk.md |
| Zigzagoon | 16 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Cyndaquil | 15 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Hitmonchan | 15 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Jynx | 15 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Machamp | 15 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Mankey | 15 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Mantine | 15 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Marill | 15 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Onix | 15 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Torchic | 15 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Treecko | 15 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Voltorb | 15 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Wooper | 15 | esterni/buriedrelic.neocities.org/1514790c-shiny-hunting-in-gale-of-darkness-buried-relic.md |
| Wurmple | 15 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Dunsparce | 14 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Gligar | 14 | esterni/buriedrelic.neocities.org/1514790c-shiny-hunting-in-gale-of-darkness-buried-relic.md |
| Hoopa | 14 | esterni/raw.githubusercontent.com/c5b82a3e-https-raw-githubusercontent-com-wiki-flagbrew-pk.md |
| Jolteon | 14 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Kadabra | 14 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Ponyta | 14 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Regice | 14 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Regirock | 14 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Remoraid | 14 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Spinda | 14 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Steelix | 14 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Aipom | 13 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Beedrill | 13 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Beldum | 13 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Diglett | 13 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Dodrio | 13 | esterni/bluemoonfalls.com/03abf808-dv-breeding-for-shinies-blue-moon-falls.md |
| Doduo | 13 | esterni/bluemoonfalls.com/03abf808-dv-breeding-for-shinies-blue-moon-falls.md |
| Elekid | 13 | esterni/buriedrelic.neocities.org/1514790c-shiny-hunting-in-gale-of-darkness-buried-relic.md |
| Furfrou | 13 | esterni/github.com/27d4d333-releases-ajarmar-universal-pokemon-randomizer-zx.md |
| Gallade | 13 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Gible | 13 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Golduck | 13 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Landorus | 13 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Machop | 13 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Magnemite | 13 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Parasect | 13 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Pinsir | 13 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Ralts | 13 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Rattata | 13 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Registeel | 13 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Rhydon | 13 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Rhyhorn | 13 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Sandshrew | 13 | esterni/buriedrelic.neocities.org/1514790c-shiny-hunting-in-gale-of-darkness-buried-relic.md |
| Sneasel | 13 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Tangela | 13 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Tyrogue | 13 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Ursaring | 13 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Yanma | 13 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Delibird | 12 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Geodude | 12 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Glalie | 12 | esterni/raw.githubusercontent.com/c5b82a3e-https-raw-githubusercontent-com-wiki-flagbrew-pk.md |
| Graveler | 12 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Hippowdon | 12 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Marowak | 12 | esterni/buriedrelic.neocities.org/6a500f94-utility-pok-mon-buried-relic.md |
| Murkrow | 12 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Phanpy | 12 | esterni/buriedrelic.neocities.org/1514790c-shiny-hunting-in-gale-of-darkness-buried-relic.md |
| Phione | 12 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Qwilfish | 12 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Togetic | 12 | esterni/buriedrelic.neocities.org/1514790c-shiny-hunting-in-gale-of-darkness-buried-relic.md |
| Vaporeon | 12 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Wigglytuff | 12 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Zubat | 12 | esterni/buriedrelic.neocities.org/1514790c-shiny-hunting-in-gale-of-darkness-buried-relic.md |
| Absol | 11 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Altaria | 11 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Azumarill | 11 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Breloom | 11 | esterni/buriedrelic.neocities.org/6a500f94-utility-pok-mon-buried-relic.md |
| Clefable | 11 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Exeggutor | 11 | esterni/serebii.net/905c290f-pok-mon-scarlet-violet-tera-raid-battle-events.md |
| Jigglypuff | 11 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Koffing | 11 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Magearna | 11 | esterni/raw.githubusercontent.com/c5b82a3e-https-raw-githubusercontent-com-wiki-flagbrew-pk.md |
| Mesprit | 11 | esterni/bepis.io/777ed253-pok-mon-platinum-national-dex-guide.md |
| Nidorina | 11 | esterni/bluemoonfalls.com/03abf808-dv-breeding-for-shinies-blue-moon-falls.md |
| Poliwhirl | 11 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Seel | 11 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Shroomish | 11 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Stantler | 11 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Staryu | 11 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |

## Mosse

Il corpus nomina 397 mosse distinte fra quelle riconoscibili. I nostri lotti ne contengono 330, e 173 delle nominate non vi compaiono.

| Mossa | Documenti | Uno dei documenti |
|---|---|---|
| Strength | 7 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Guillotine | 5 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Jump Kick | 5 | esterni/buriedrelic.neocities.org/70987763-old-gen-shiny-hunter-manual-generation-3-buried.md |
| Reversal | 5 | esterni/buriedrelic.neocities.org/1514790c-shiny-hunting-in-gale-of-darkness-buried-relic.md |
| Rock Throw | 5 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Waterfall | 5 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Assurance | 4 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Dizzy Punch | 4 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Ingrain | 4 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Sand Attack | 4 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Blizzard | 3 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Comet Punch | 3 | esterni/buriedrelic.neocities.org/70987763-old-gen-shiny-hunter-manual-generation-3-buried.md |
| Conversion | 3 | esterni/bluemoonfalls.com/8d31cd92-generation-1-shiny-hunting-blue-moon-falls.md |
| Copycat | 3 | esterni/bluemoonfalls.com/03abf808-dv-breeding-for-shinies-blue-moon-falls.md |
| Fissure | 3 | esterni/buriedrelic.neocities.org/70987763-old-gen-shiny-hunter-manual-generation-3-buried.md |
| Heal Block | 3 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Lucky Chant | 3 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Magnitude | 3 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Meditate | 3 | esterni/buriedrelic.neocities.org/70987763-old-gen-shiny-hunter-manual-generation-3-buried.md |
| Minimize | 3 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Mud Shot | 3 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Quick Guard | 3 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Relic Song | 3 | esterni/raw.githubusercontent.com/c5b82a3e-https-raw-githubusercontent-com-wiki-flagbrew-pk.md |
| Secret Sword | 3 | esterni/www.serebii.net/afa1b172-pok-mon-black-2-pok-mon-white-2-in-game-events.md |
| Skill Swap | 3 | esterni/www.serebii.net/8386f43d-serebii-net-eventdex-0386-deoxys.md |
| Tailwind | 3 | esterni/github.com/d0aeda8a-github-kristopheles-monarium-customizable-pok-de.md |
| Trick Room | 3 | esterni/raw.githubusercontent.com/c5b82a3e-https-raw-githubusercontent-com-wiki-flagbrew-pk.md |
| Twister | 3 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Aeroblast | 2 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Bulk Up | 2 | esterni/buriedrelic.neocities.org/70987763-old-gen-shiny-hunter-manual-generation-3-buried.md |
| Charge Beam | 2 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Double Hit | 2 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Double-Edge | 2 | esterni/buriedrelic.neocities.org/70987763-old-gen-shiny-hunter-manual-generation-3-buried.md |
| Electroweb | 2 | esterni/www.serebii.net/0097a7d7-pok-mon-black-2-pok-mon-white-2-n-s-pok-mon.md |
| Explosion | 2 | esterni/buriedrelic.neocities.org/1b151d0a-shiny-shadow-hunting-guide-buried-relic.md |
| Extrasensory | 2 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Happy Hour | 2 | esterni/www.serebii.net/e2c5c5a7-serebii-net-eventdex-0025-pikachu.md |
| Heart Stamp | 2 | esterni/www.serebii.net/e2c5c5a7-serebii-net-eventdex-0025-pikachu.md |
| Hold Hands | 2 | esterni/www.serebii.net/e2c5c5a7-serebii-net-eventdex-0025-pikachu.md |
| Lovely Kiss | 2 | esterni/buriedrelic.neocities.org/23519345-old-gen-shiny-hunter-manual-generations-1-2-buri.md |
| Mat Block | 2 | posts/175qgyy-pokemon-to-transfer-before-bank-shuts-down.md |
| Memento | 2 | esterni/buriedrelic.neocities.org/6a500f94-utility-pok-mon-buried-relic.md |
| Moonblast | 2 | esterni/www.smogon.com/f3a26eaa-metagame-lgpe-overused-smogon-forums.md |
| Poison Jab | 2 | esterni/www.smogon.com/f3a26eaa-metagame-lgpe-overused-smogon-forums.md |
| Power Gem | 2 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Psycho Cut | 2 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Rapid Spin | 2 | esterni/www.serebii.net/b936abbd-pok-mon-scarlet-violet-titan-pok-mon.md |
| Rock Smash | 2 | esterni/www.serebii.net/b936abbd-pok-mon-scarlet-violet-titan-pok-mon.md |
| Rolling Kick | 2 | esterni/buriedrelic.neocities.org/70987763-old-gen-shiny-hunter-manual-generation-3-buried.md |
| Sacred Fire | 2 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Secret Power | 2 | esterni/github.com/27d4d333-releases-ajarmar-universal-pokemon-randomizer-zx.md |
| Shell Smash | 2 | esterni/www.smogon.com/f3a26eaa-metagame-lgpe-overused-smogon-forums.md |
| Sleep Powder | 2 | esterni/www.smogon.com/f3a26eaa-metagame-lgpe-overused-smogon-forums.md |
| Sonic Boom | 2 | esterni/buriedrelic.neocities.org/70987763-old-gen-shiny-hunter-manual-generation-3-buried.md |
| Stealth Rock | 2 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Struggle | 2 | esterni/www.smogon.com/60b0cb5e-gen-iii-battle-frontier-discussion-and-records-s.md |
| Tri Attack | 2 | esterni/www.serebii.net/630733a6-pok-mon-let-s-go-pikachu-let-s-go-eevee-gift-pok.md |
| Wide Guard | 2 | esterni/buriedrelic.neocities.org/929f884e-old-gen-shiny-hunter-manual-generation-5-buried.md |
| Barrage | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Blood Moon | 1 | posts/f3uaxj-pokemon-home-complete-living-dex-list.md |
| Bone Club | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Bouncy Bubble | 1 | esterni/www.smogon.com/f3a26eaa-metagame-lgpe-overused-smogon-forums.md |
| Burn Up | 1 | esterni/www.smogon.com/01421172-guide-to-ultra-space-in-pok-mon-ultra-sun-and-mo.md |
| Buzzy Buzz | 1 | esterni/www.smogon.com/f3a26eaa-metagame-lgpe-overused-smogon-forums.md |
| Camouflage | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Catastropika | 1 | esterni/www.serebii.net/60777b72-pok-mon-ultra-sun-ultra-moon-alola-photo-club.md |
| Chip Away | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Continental Crush | 1 | posts/18sbp6k-any-advice-for-the-battle-tree-i-m-about-to-give.md |
| Corkscrew Crash | 1 | posts/18sbp6k-any-advice-for-the-battle-tree-i-m-about-to-give.md |
| Dazzling Gleam | 1 | esterni/www.smogon.com/f3a26eaa-metagame-lgpe-overused-smogon-forums.md |
| Diamond Storm | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Double Iron Bash | 1 | esterni/www.smogon.com/f3a26eaa-metagame-lgpe-overused-smogon-forums.md |
| Dragon Cheer | 1 | posts/hhlm8k-a-guide-to-underleveled-pokemon.md |
| Dragon Tail | 1 | esterni/www.smogon.com/f3a26eaa-metagame-lgpe-overused-smogon-forums.md |
| Dream Eater | 1 | esterni/buriedrelic.neocities.org/1deef27f-old-gen-shiny-hunter-manual-generation-4-buried.md |
| Drill Run | 1 | esterni/www.smogon.com/f3a26eaa-metagame-lgpe-overused-smogon-forums.md |
| Dynamic Punch | 1 | esterni/buriedrelic.neocities.org/1514790c-shiny-hunting-in-gale-of-darkness-buried-relic.md |
| Egg Bomb | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Electric Terrain | 1 | esterni/www.serebii.net/e2a4222e-pok-mon-sword-shield-weather.md |
| Entrainment | 1 | posts/18sbp6k-any-advice-for-the-battle-tree-i-m-about-to-give.md |

## Fiocchi

Il corpus nomina 30 fiocchi distinti. Il progetto non ha ancora un'enumerazione dell'asse dei fiocchi, quindi qui non c'e' un confronto ma un elenco, ed e' il materiale di partenza per costruirla.

| Fiocco | Documenti | Uno dei documenti |
|---|---|---|
| National | 3 | posts/175qgyy-pokemon-to-transfer-before-bank-shuts-down.md |
| Artist | 2 | esterni/github.com/ee2c80db-github-andrewbenington-openhome-application-for.md |
| Earth | 2 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Effort | 2 | posts/12vvhbk-guide-with-pictures-how-to-tell-if-a-pokemon-is.md |
| Event | 2 | posts/12vvhbk-guide-with-pictures-how-to-tell-if-a-pokemon-is.md |
| Partner | 2 | esterni/www.gamebrew.org/3f09a0c4-pkhex-3ds-gamebrew.md |
| Ability | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Alola Champion | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Battle Memory | 1 | esterni/www.gamebrew.org/3f09a0c4-pkhex-3ds-gamebrew.md |
| Battle Royal Master | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Battle Tree Great | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Battle Tree Master | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Birthday | 1 | posts/pzzqt4-my-guide-on-the-ribbon-master-challenge.md |
| Classic | 1 | esterni/www.serebii.net/0c9d378d-pok-mon-heart-gold-soul-silver-the-wi-fi-events.md |
| Double Ability | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Expert Battler | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Footprint | 1 | posts/pzzqt4-my-guide-on-the-ribbon-master-challenge.md |
| Great Ability | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Kalos Champion | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Legend | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Master Rank | 1 | posts/hhlm8k-a-guide-to-underleveled-pokemon.md |
| Multi Ability | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Pair Ability | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Premier | 1 | esterni/www.serebii.net/0c9d378d-pok-mon-heart-gold-soul-silver-the-wi-fi-events.md |
| Skillful Battler | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Training | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Twinkling Star | 1 | posts/pzzqt4-my-guide-on-the-ribbon-master-challenge.md |
| Victory | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
| Winning | 1 | posts/pzzqt4-my-guide-on-the-ribbon-master-challenge.md |
| World Ability | 1 | posts/1apiuee-pok-mon-bank-exclusives-masterpost.md |
