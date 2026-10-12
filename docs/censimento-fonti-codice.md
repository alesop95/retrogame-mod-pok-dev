# Censimento dei repository di codice citati dalle fonti

> Documento generato da `tools/censimento-fonti-codice.py`. Non si modifica a mano: si rigenera. È la parte deterministica del censimento chiesto da ADR-100; il giudizio su che cosa ciascun repository possa aggiungere agli strumenti del progetto sta in `docs/potenziamento-dalle-fonti.md`.

Perimetro: gli indirizzi di repository di codice nelle righe di tabella di `SOURCES.md`; l'uso nel progetto si cerca per nome del repository nei file Python, C#, PowerShell e Markdown tracciati, esclusi `SOURCES.md`, la memoria e i modelli del template. Repository distinti: 110; nominati dal progetto: 98, di cui nominati dal codice in `tools/` e nei sottoprogetti: 43; mai nominati fuori dal registro: 12.

Metadati letti con `tools/raccogli-fonti-codice.py` dall'API di GitHub: 107 repository su 110; per gli altri la colonna dice «non raccolto».

| Repository | Linguaggio | Licenza | Ultimo aggiornamento | Stato | Righe del registro | Track | Esito scritto | Nel codice | Nominato nel progetto in |
|---|---|---|---|---|---|---|---|---|---|
| `pret/pokeemerald` | C | - | 2026-10-01 | attivo | 91, 92, 93, 134, 135, 136 e altre | BRI, SME | letto 11 | sì | `.claude/context/sub-gen12-gen3-bridge.md`, `.claude/context/sub-smeraldo-save-fix.md`, `README.md`, `docs/03-integrita-checksum.md` e altri 41 |
| `kwsch/PKHeX` | C# | NOASSERTION | 2026-10-07 | attivo | 340, 341, 730, 760, 778, 779 e altre | BRI, EVT, PKD, SME, TUTTI | letto 6, senza esito scritto 2 | sì | `.claude/context/STACK.md`, `.claude/context/current-work.md`, `.claude/context/dev-testing.md`, `.claude/context/refactor-01-forme-di-battaglia.md` e altri 143 |
| `projectpokemon/EventsGallery` | - | - | 2026-09-06 | attivo | 783, 1657, 1658, 1659, 1660 | EVT | senza esito scritto 4, letto 1 | sì | `docs/mappa-fonti/eventsgallery.md`, `docs/mappa-fonti/index-fonti.md`, `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md`, `tools/build-source-map.py` |
| `pokepc/classic.pokepc.net` | TypeScript | MIT | 2026-09-22 | attivo | 343, 344, 787, 794 | PKD | letto 4 | sì | `docs/mappa-fonti/collezione/1- Dex completions - Pokemon Collection Trackers.md`, `docs/mappa-fonti/collezione/collezione-indice.md`, `docs/mappa-fonti/pokepc-dati.md`, `docs/strumenti-dal-web.md` e altri 5 |
| `kristopheles/monarium` | TypeScript | MIT | 2026-04-17 | attivo | 789, 795, 1616 | PKD | senza esito scritto 3 | sì | `docs/mappa-fonti/index-fonti.md`, `docs/mappa-fonti/monarium.md`, `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md`, `pokedex-home-completo/SPOGLIO-CORPUS.md` e altri 1 |
| `pret/pokered` | Assembly | - | 2026-10-06 | attivo | 610, 1656 | BRI | senza esito scritto 2 | sì | `README.md`, `docs/22-strumenti.md`, `docs/23-prove-eseguite.md`, `docs/mappa-fonti/cable-link.md` e altri 12 |
| `adanscotney/gameboy-spoof` | non raccolto | - | - | - | 334 | BRI | senza esito scritto 1 | sì | `docs/22-strumenti.md`, `docs/mappa-fonti/arduino-boy.md`, `knowledge/sources/notes/debito-tecnico-2026-10-01.md`, `tools/build-source-map.py` |
| `afska/gba-link-connection` | C++ | MIT | 2026-08-01 | attivo | 739 | BRI | letto 1 | sì | `docs/mappa-fonti/gba-link-connection.md`, `docs/mappa-fonti/index-fonti.md`, `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`, `tools/build-source-map.py` |
| `binarycounter/PkSploit` | Python | MIT | 2017-11-24 | attivo | 703 | BRI, SME | letto 1 | sì | `docs/01-fondamenta-salvataggio.md`, `docs/09-esecuzione-codice.md`, `docs/20-architettura-codice.md`, `docs/23-prove-eseguite.md` e altri 6 |
| `CableClub/cable-link` | XSLT | NOASSERTION | 2021-09-06 | attivo | 709 | BRI | letto 1 | sì | `docs/08-cavo-link.md`, `docs/30-opzioni-implementative.md`, `docs/mappa-fonti/cable-link.md`, `docs/mappa-fonti/index-fonti.md` e altri 3 |
| `FIX94/gba-link-cable-rom-sender` | C | MIT | 2018-12-15 | attivo | 744 | BRI | letto 1 | sì | `docs/mappa-fonti/rom-sender.md`, `tools/build-source-map.py` |
| `gbdev/pandocs` | Markdown | CC0-1.0 | 2026-10-02 | attivo | 619 | BRI | letto 1 | sì | `docs/mappa-fonti/index-fonti.md`, `docs/mappa-fonti/pandocs.md`, `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`, `tools/build-source-map.py` e altri 1 |
| `Goppier/Gen3DistributionRoms` | - | - | 2024-08-07 | attivo | 782 | EVT | letto 1 | sì | `docs/mappa-fonti/project-wonder.md`, `tools/build-source-map.py` |
| `Goppier/GEN3PokemonDistributions` | - | - | 2025-12-01 | attivo | 716 | BRI | letto 1 | sì | `docs/mappa-fonti/gen3distributions.md`, `tools/build-source-map.py` |
| `itsjavi/supereffective` | TypeScript | MIT | 2026-09-22 | attivo | 788 | PKD | letto 1 | sì | `docs/mappa-fonti/collezione/1- Dex completions - Pokemon Collection Trackers.md`, `docs/mappa-fonti/pokepc-dati.md`, `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md`, `pokedex-home-completo/CONFRONTO-LIVINGDEX-POKEPC.md` e altri 3 |
| `kinnay/NintendoClients` | Python | MIT | 2026-10-03 | attivo | 710 | LDN | letto 1 | sì | `.claude/context/sub-gba-switch-trading.md`, `docs/11-wireless-locale-e-ponte-switch.md`, `docs/mappa-fonti/kinnay-ldn.md`, `gba-switch-pokemon-trading/README.md` e altri 2 |
| `lesserkuma/FlashGBX` | Python | GPL-3.0 | 2026-09-08 | attivo | 748 | BRI, SME | senza esito scritto 1 | sì | `.claude/context/STACK.md`, `.claude/context/dev-testing.md`, `.claude/context/roadmap.md`, `.claude/context/sub-cart-battery.md` e altri 18 |
| `Lorenzooone/Pokemon-Gen3-to-Gen-X` | C | MIT | 2026-08-30 | attivo | 701 | BRI | clonato 1 | sì | `docs/23-prove-eseguite.md`, `docs/mappa-fonti/gen3togenx.md`, `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`, `tools/build-source-map.py` |
| `Lorenzooone/PokemonGB_Online_Trades` | Python | MIT | 2026-08-28 | attivo | 702 | BRI, LDN | letto 1 | sì | `docs/08-cavo-link.md`, `docs/20-architettura-codice.md`, `docs/21-collaudo.md`, `docs/mappa-fonti/pokemongb-online.md` e altri 2 |
| `MrCheeze/pokestadium-ace` | Python | - | 2018-09-02 | attivo | 715 | BRI | letto 1 | sì | `docs/mappa-fonti/stadium-ace.md`, `tools/build-source-map.py` |
| `mrhappyasthma/NDSEventTool.nds` | C++ | GPL-2.0 | 2020-01-28 | fork | 94 | SME | letto 1 | sì | `gba-save-extraction-smeraldo/STUDIO-03-doni-segreti-e-flag-delle-isole.md`, `gba-save-extraction-smeraldo/tools/emerald_event_flags_decode.py`, `gba-save-extraction-smeraldo/tools/emerald_event_flags_fix.py` |
| `pepijndevos/arduino-boy` | Arduino | NOASSERTION | 2020-06-11 | attivo | 714 | BRI | letto 1 | sì | `docs/mappa-fonti/arduino-boy.md`, `docs/mappa-fonti/arduino-poke-gen2.md`, `docs/mappa-fonti/index-fonti.md`, `knowledge/sources/notes/debito-tecnico-2026-10-01.md` e altri 1 |
| `Phasip/PokemonLinkHack` | Python | - | 2023-01-09 | attivo | 705 | BRI | letto 1 | sì | `docs/mappa-fonti/linkhack.md`, `tools/build-source-map.py` |
| `pokepc/dataset` | TypeScript | MIT | 2026-10-05 | attivo | 786 | PKD | letto 1 | sì | `docs/22-strumenti.md`, `docs/strumenti-dal-web.md`, `docs/strumenti-interattivi.md`, `pokedex-home-completo/CONFRONTO-LIVINGDEX-POKEPC.md` e altri 10 |
| `pret/pokecrystal` | Assembly | - | 2026-10-06 | attivo | 613 | BRI | letto 1 | sì | `README.md`, `docs/06-identita-pokemon.md`, `docs/08-cavo-link.md`, `docs/22-strumenti.md` e altri 11 |
| `pret/pokefirered` | C | - | 2026-09-26 | attivo | 616 | BRI, LDN, SME | clonato 1 | sì | `.claude/context/sub-gba-switch-trading.md`, `docs/08-cavo-link.md`, `docs/mappa-fonti/frlg-ldn-trade.md`, `docs/mappa-fonti/index-fonti.md` e altri 6 |
| `pret/pokegold` | Assembly | - | 2026-10-06 | attivo | 612 | BRI | clonato 1 | sì | `docs/mappa-fonti/index-fonti.md`, `docs/mappa-fonti/pokegold.md`, `knowledge/sources/notes/debito-tecnico-2026-10-01.md`, `tools/build-source-map.py` |
| `pret/pokeruby` | C | - | 2026-09-29 | attivo | 614 | BRI, PKD, SME | clonato 1 | sì | `.claude/context/refactor-06-verifica-indipendente.md`, `.claude/context/studio-didattico-master.md`, `docs/22-strumenti.md`, `docs/mappa-fonti/index-fonti.md` e altri 8 |
| `pret/pokeyellow` | Assembly | - | 2026-09-02 | attivo | 611 | BRI | clonato 1 | sì | `docs/mappa-fonti/index-fonti.md`, `docs/mappa-fonti/pokeyellow.md`, `knowledge/sources/notes/debito-tecnico-2026-10-01.md`, `tools/build-source-map.py` |
| `savaughn/pokerom-trader` | C | MIT | 2025-02-17 | attivo | 707 | BRI | clonato 1 | sì | `docs/mappa-fonti/index-fonti.md`, `docs/mappa-fonti/pokerom-trader.md`, `tools/build-source-map.py` |
| `spacemeowx2/ldn_mitm` | C++ | GPL-2.0 | 2026-08-24 | attivo | 757 | LDN | letto 1 | sì | `docs/mappa-fonti/ldn-mitm.md`, `tools/build-source-map.py` |
| `spacemeowx2/switch-lan-play` | C | GPL-3.0 | 2025-03-21 | attivo | 758 | LDN | letto 1 | sì | `docs/mappa-fonti/index-fonti.md`, `docs/mappa-fonti/ldn-mitm.md`, `docs/mappa-fonti/switch-lan-play.md`, `tools/build-source-map.py` |
| `stevenchaulk/arduino-poke-gen2` | C | NOASSERTION | 2016-09-23 | attivo | 713 | BRI | letto 1 | sì | `docs/mappa-fonti/arduino-poke-gen2.md`, `docs/mappa-fonti/index-fonti.md`, `tools/build-source-map.py` |
| `Striaton-Lab-Team/Poke_Transporter_GB` | BitBake | MIT | 2026-10-03 | attivo | 697 | BRI | clonato 1 | sì | `docs/23-prove-eseguite.md`, `docs/mappa-fonti/ptgb.md`, `tools/build-source-map.py` |
| `Striaton-Lab-Team/Pokemon-Community-Conversion-Standard` | C++ | - | 2026-10-02 | attivo | 698 | BRI | clonato 1 | sì | `docs/23-prove-eseguite.md`, `docs/mappa-fonti/pccs.md`, `tools/build-source-map.py` |
| `superguideguy/gen-iii-event-patcher` | Java | MIT | 2021-02-12 | attivo | 781 | BRI, EVT | letto 1 | sì | `docs/mappa-fonti/gen-iii-event-patcher.md`, `docs/mappa-fonti/index-fonti.md`, `recreate-pokemon-distributions-events/STUDIO-02-metodi-di-generazione.md`, `tools/build-source-map.py` |
| `tangrs/usb-gba-multiboot` | C | - | 2012-07-11 | attivo | 745 | BRI | letto 1 | sì | `docs/mappa-fonti/index-fonti.md`, `docs/mappa-fonti/usb-gba-multiboot.md`, `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`, `tools/build-source-map.py` |
| `taxicat1/DomeAssistantWeb` | HTML | MIT | 2024-09-13 | attivo | 140 | SME | letto 1 | sì | `docs/mappa-fonti/domeassistant.md`, `docs/mappa-fonti/smogon-maxstats-frontiera.md`, `gba-save-extraction-smeraldo/STUDIO-04-parco-lotta-simboli-oro.md`, `gba-save-extraction-smeraldo/tools/parco_lotta_piramide_ordine.py` e altri 2 |
| `tornadus/frlg-ldn-trade` | Python | AGPL-3.0 | 2026-09-03 | attivo | 756 | LDN | letto 1 | sì | `.claude/context/STACK.md`, `.claude/context/sub-gba-switch-trading.md`, `docs/mappa-fonti/frlg-ldn-trade.md`, `docs/mappa-fonti/index-fonti.md` e altri 5 |
| `Tyrrrz/DiscordChatExporter` | C# | MIT | 2026-10-02 | attivo | 729 | BRI, EVT, LDN | letto 1 | sì | `.claude/context/STACK.md`, `.claude/skills/fonti-non-recuperabili/RIFERIMENTO.md`, `docs/22-strumenti.md`, `docs/24-fonti-di-community.md` e altri 3 |
| `unlimitedcoder2/frlg-ldn-trade` | Python | AGPL-3.0 | 2026-09-09 | fork | 755 | LDN | letto 1 | sì | `.claude/context/STACK.md`, `.claude/context/sub-gba-switch-trading.md`, `docs/mappa-fonti/frlg-ldn-trade.md`, `docs/mappa-fonti/index-fonti.md` e altri 5 |
| `unlimitedcoder2/ldnd` | C | GPL-2.0 | 2026-09-01 | attivo | 711 | LDN | letto 1 | sì | `docs/mappa-fonti/ldnd.md`, `tools/build-source-map.py` |
| `vaguilar/pokemon-red-cable-club-hack` | Python | Apache-2.0 | 2020-08-07 | fork | 704 | BRI | letto 1 | sì | `docs/mappa-fonti/cableclubhack.md`, `tools/build-source-map.py` |
| `FlagBrew/PKSM` | C++ | GPL-3.0 | 2026-09-08 | attivo | 1600, 1601, 1602, 1603, 1628, 1629 e altre | - | senza esito scritto 10 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `Ajarmar/universal-pokemon-randomizer-zx` | Java | GPL-3.0 | 2024-11-23 | fork | 1596, 1597 | - | senza esito scritto 2 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md`, `pokedex-home-completo/SPOGLIO-CORPUS.md` |
| `claydolwithexplosion/017f1784deebcd118b61d3ad917edb3c` | Assembly, Markdown | - | 2026-09-19 | gist | 720, 1018 | ACE, EVT | letto 1, senza esito scritto 1 | no | `docs/mappa-fonti/collezione/1- Dex completions - Gen 3.md`, `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `concreted/3DSync` | C++ | - | 2022-06-05 | fork | 1613, 1645 | - | senza esito scritto 2 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `DS-Homebrew/nds-bootstrap` | C | GPL-3.0 | 2026-10-07 | attivo | 1599, 1626 | - | senza esito scritto 2 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `DS-Homebrew/TWiLightMenu` | C++ | GPL-3.0 | 2026-10-07 | attivo | 1624, 1625 | - | senza esito scritto 2 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `kuroppoi/entralinked` | Java | MIT | 2026-05-13 | attivo | 1617, 1649 | - | senza esito scritto 2 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `lifehackerhansol/YANBF` | C | GPL-2.0 | 2024-01-03 | attivo | 1651, 1652 | - | senza esito scritto 2 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `MechanicalDragon0687/NDSForwarder` | C++ | GPL-3.0 | 2025-05-19 | attivo | 1607, 1608 | - | senza esito scritto 2 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `RiiConnect24/DNS-Server` | Python | MIT | 2024-05-21 | fork | 1609, 2392 | - | senza esito scritto 2 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `YANBForwarder/YANBF` | C | GPL-2.0 | 2024-01-03 | attivo | 1641, 1642 | - | senza esito scritto 2 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `Admiral-Fish/RNGReporter` | C# | GPL-2.0 | 2018-09-23 | archiviato | 737 | BRI | letto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `andrewbenington/OpenHome` | Rust | GPL-3.0 | 2026-10-07 | attivo | 1612 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md`, `pokedex-home-completo/SPOGLIO-CORPUS.md` |
| `BernardoGiordano/Checkpoint` | C++ | GPL-3.0 | 2026-08-30 | attivo | 749 | 3DS | senza esito scritto 1 | no | `.claude/context/STACK.md`, `.claude/context/sub-3ds-modding.md`, `.claude/skills/sync-context/SKILL.md`, `3ds-related/README.md` e altri 7 |
| `Bl4ckSh4rk/256ed3b857c9677310837d5180121f35` | Text | - | 2026-01-22 | gist | 2174 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `christianhaitian/retroarch-cores` | Shell | - | 2026-09-07 | fork | 1644 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `d0k3/SEEDconv` | C | - | 2016-10-19 | archiviato | 752 | 3DS | senza esito scritto 1 | no | `.claude/context/STACK.md`, `.claude/context/dev-testing.md`, `.claude/context/sub-3ds-modding.md`, `3ds-related/handoff/HANDOFF_progetto_3DS.md` e altri 1 |
| `DS-Homebrew/GodMode9i` | C | GPL-3.0 | 2026-10-05 | attivo | 1598 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `figgyc/0d31b77fc6e4e8f9a49399d392740d46` | Markdown | - | 2026-07-26 | gist | 2175 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `FlagBrew/PKSM-Scripts` | C | - | 2026-10-02 | attivo | 1627 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `francesco265/RtcPwalker` | C++ | GPL-3.0 | 2026-01-08 | attivo | 1614 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `gdkchan/Ohana3DS-Rebirth` | C# | - | 2022-09-17 | attivo | 1646 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `Gericom/GBARunner2` | C | - | 2023-05-08 | attivo | 1634 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `ghnr/sneakpeekbot` | Python | - | 2021-11-26 | attivo | 1615 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `hacks-guide/MSET9` | C | - | 2026-09-25 | fork | 750 | 3DS | senza esito scritto 1 | no | `.claude/context/STACK.md`, `.claude/context/sub-3ds-modding.md`, `3ds-related/README.md`, `3ds-related/handoff/HANDOFF_progetto_3DS.md` e altri 3 |
| `hax0kartik/wumiibo` | C++ | GPL-3.0 | 2025-08-01 | attivo | 1647 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `InternalLoss/DLS1-Files` | - | - | 2023-04-26 | attivo | 1604 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `joel16/3DShell` | C | - | 2026-08-14 | attivo | 1648 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `KernelEquinox/8F-Helper` | C | - | 2016-12-21 | attivo | 1605 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `kinnay/LDN` | Python | GPL-3.0 | 2026-10-02 | attivo | 754 | LDN | letto 1 | no | `.claude/context/STACK.md`, `.claude/context/sub-gba-switch-trading.md`, `gba-switch-pokemon-trading/handoff/HANDOFF_frlg-ldn-trade.md` |
| `LumaTeam/Luma3DS` | C | GPL-3.0 | 2026-09-04 | attivo | 1606 | - | senza esito scritto 1 | no | `.claude/context/STACK.md`, `.claude/context/sub-3ds-modding.md`, `3ds-related/handoff/HANDOFF_progetto_3DS.md`, `3ds-related/handoff/step02_cfw_mset9.md` e altri 2 |
| `mamba2410/reverse-pokewalker` | C++ | MIT | 2024-10-16 | archiviato | 1653 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `masterfeizz/DaedalusX64-3DS` | C++ | GPL-2.0 | 2022-10-23 | attivo | 1654 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `MersenneTwister-Lab/TinyMT` | C++ | NOASSERTION | 2024-09-25 | attivo | 1635 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `mtheall/ftpd` | C++ | GPL-3.0 | 2025-11-19 | attivo | 1618 | - | senza esito scritto 1 | no | `docs/strumenti-interattivi.md`, `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `ncorgan/pksav` | C | MIT | 2021-11-15 | archiviato | 732 | BRI, SME | letto 1 | no | `docs/23-prove-eseguite.md` |
| `Olmectron/Simple-Web-App-GUI-for-YANBF-Generator` | JavaScript | CC0-1.0 | 2022-03-11 | attivo | 1636 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `polaris-/dwc_network_server_emulator` | Python | AGPL-3.0 | 2024-08-02 | attivo | 1655 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `pret/pokeemerald.wiki` | non raccolto | - | - | - | 335 | BRI, SME | clonato 1 | no | `docs/22-strumenti.md`, `knowledge/sources/notes/debito-tecnico-2026-10-01.md` |
| `projectpokemon/Gen3-WCTool` | C# | - | 2019-03-22 | attivo | 738 | BRI | letto 1 | no | `.claude/context/roadmap.md` |
| `REONTeam/libmobile` | C | LGPL-3.0 | 2026-03-17 | attivo | 741 | BRI | letto 1 | no | `knowledge/sources/notes/debito-tecnico-2026-10-01.md` |
| `REONTeam/trade-corner` | C# | AGPL-3.0 | 2026-04-18 | attivo | 742 | BRI | letto 1 | no | `knowledge/sources/notes/debito-tecnico-2026-10-01.md` |
| `RocketRobz/NTR_Forwarder` | C | - | 2026-05-23 | fork | 1637 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `semaj14/Multi-PokemonFramework` | C++ | GPL-3.0 | 2024-02-18 | attivo | 1619 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `suloku/BW_tool` | C# | GPL-3.0 | 2023-10-23 | attivo | 1620 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `TheLevelUp/pos-tls-patcher` | PowerShell | Apache-2.0 | 2024-01-24 | attivo | 1638 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `TurdPooCharger/GBAVCSM` | - | GPL-3.0 | 2020-04-09 | attivo | 1610 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `TuxSH/TWLSaveTool` | C++ | GPL-2.0 | 2024-09-24 | attivo | 1611 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `Universal-Team/Universal-Updater` | C++ | GPL-3.0 | 2026-10-01 | attivo | 1639 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `Watchful1/RemindMeBot` | Python | - | 2026-10-06 | attivo | 1640 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `wiki/FlagBrew` | non raccolto | - | - | - | 2391 | - | senza esito scritto 1 | no | `docs/22-strumenti.md`, `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md`, `pokedex-home-completo/SPOGLIO-CORPUS.md` |
| `YANBForwarder/assets` | Python | CC0-1.0 | 2025-09-21 | attivo | 1643 | - | senza esito scritto 1 | no | `docs/strumenti-interattivi.md`, `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `yuhasem/FeebasFinder` | JavaScript | MIT | 2024-05-12 | attivo | 1621 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `yuhasem/poc_utils` | Python | - | 2026-08-30 | attivo | 1622 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `zaksabeast/DreamRadarCartRedirect` | Assembly | GPL-3.0 | 2025-05-13 | attivo | 1623 | - | senza esito scritto 1 | no | `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` |
| `aarant/gen3tools` | Python | - | 2021-03-08 | attivo | 736 | BRI, SME | letto 1 | no | mai |
| `ads04r/Gen3Save` | Python | Unlicense | 2019-10-09 | attivo | 735 | BRI, SME | letto 1 | no | mai |
| `architdate/PKHeX-Plugins` | C# | MIT | 2024-05-08 | attivo | 763 | EVT, PKD | letto 1 | no | mai |
| `crumblingstatue/rgen3` | Rust | MIT | 2025-03-22 | attivo | 734 | BRI, SME | letto 1 | no | mai |
| `devkitPro/libtonc` | C | - | 2025-05-12 | attivo | 627 | BRI | senza esito scritto 1 | no | mai |
| `E-Sh4rk/PokeGlitzer` | C# | - | 2025-04-26 | attivo | 724 | ACE, SME | letto 1 | no | mai |
| `Ethiquema/ryu_ldn_nx` | C++ | GPL-2.0 | 2026-10-04 | attivo | 759 | LDN | letto 1 | no | mai |
| `gbadev-org/awesome-gbadev` | - | NOASSERTION | 2026-01-30 | attivo | 784 | BRI | senza esito scritto 1 | no | mai |
| `gbdev/awesome-gbdev` | - | GPL-3.0 | 2026-10-03 | attivo | 785 | BRI | senza esito scritto 1 | no | mai |
| `gbdev/rgbds` | C++ | MIT | 2026-10-04 | attivo | 626 | BRI | senza esito scritto 1 | no | mai |
| `haven1433/HexManiacAdvance` | C# | MIT | 2026-08-30 | attivo | 733 | BRI, SME | letto 1 | no | mai |
| `sofianeelhor/PKForge` | C# | NOASSERTION | 2026-10-04 | attivo | 368 | PKD | non letto 1 | no | mai |
