# Lista di spunta del Pokedex completo

> Documento generato da `tools/checklist-pokedex.py`. Non si modifica a mano: la colonna delle fonti si aggiorna rigenerando, e la spunta di ciò che è stato effettivamente ottenuto va tenuta altrove, perché questo file si riscrive.

Il codice interno è la coppia fra numero del Dex Nazionale e indice di forma, scritta come `PKD-####-##`. Esiste perché il numero del Dex identifica una specie e non un esemplare da ottenere: non cambia per il sesso, non cambia per una variante regionale, non cambia per una forma, quindi chi spunta per numero del Dex non sa alla fine che cosa gli manchi. Il codice è stabile, poiché non dipende da alcuna numerazione interna di alcuna implementazione, è ordinabile, poiché l'ordine lessicografico coincide con quello del Dex, ed è totale, poiché esiste per ogni voce anche quando il nome della forma non è noto.

La colonna della via dice se quella voce si raggiunga da un titolo che parla al deposito direttamente, e quindi senza scadenza, oppure se dipenda dalla banca, e quindi dal 26 febbraio 2027. La colonna delle fonti dice quali fra i materiali che il progetto possiede sappiano già fornire quella specie, e tiene distinte le fonti per natura: il lotto degli eventi è prodotto da noi e verificato, i depositi dei salvataggi esterni sono materiale di terzi il cui impiego è soggetto al perimetro di ADR-024, e confonderli farebbe apparire come nostro ciò che non lo è.

## Che cosa dice il conto

Le voci di specie sono 1025. Di queste, 385 hanno già una fonte dentro il progetto e 640 non ne hanno ancora alcuna: quest'ultimo è il numero che misura la campagna, e l'unico che scende quando si lavora.

La ripartizione per fonte, che non si somma perché una specie può avere più fonti, è la seguente. Da salvataggio esterno, 385 voci. Da archivio esterno, 385 voci. Da evento Gen 3 producibile, 59 voci.

Le voci di forma enumerate sono 522, e per la maggior parte il loro valore ai fini del completamento è indeterminato: nessuna fonte di primo livello dichiara quali forme il deposito conti come casella separata. L'elenco le enumera e marca l'indeterminatezza invece di decidere, perché decidere sarebbe inventare.

## Voci di specie

| Codice | Dex | Specie | Via | Fonti nel progetto |
|---|---|---|---|---|
| `PKD-0001-00` | 1 | Bulbasaur | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0002-00` | 2 | Ivysaur | diretta | salvataggio esterno, archivio esterno |
| `PKD-0003-00` | 3 | Venusaur | diretta | salvataggio esterno, archivio esterno |
| `PKD-0004-00` | 4 | Charmander | diretta | salvataggio esterno, archivio esterno |
| `PKD-0005-00` | 5 | Charmeleon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0006-00` | 6 | Charizard | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0007-00` | 7 | Squirtle | diretta | salvataggio esterno, archivio esterno |
| `PKD-0008-00` | 8 | Wartortle | diretta | salvataggio esterno, archivio esterno |
| `PKD-0009-00` | 9 | Blastoise | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0010-00` | 10 | Caterpie | diretta | salvataggio esterno, archivio esterno |
| `PKD-0011-00` | 11 | Metapod | diretta | salvataggio esterno, archivio esterno |
| `PKD-0012-00` | 12 | Butterfree | diretta | salvataggio esterno, archivio esterno |
| `PKD-0013-00` | 13 | Weedle | diretta | salvataggio esterno, archivio esterno |
| `PKD-0014-00` | 14 | Kakuna | diretta | salvataggio esterno, archivio esterno |
| `PKD-0015-00` | 15 | Beedrill | diretta | salvataggio esterno, archivio esterno |
| `PKD-0016-00` | 16 | Pidgey | diretta | salvataggio esterno, archivio esterno |
| `PKD-0017-00` | 17 | Pidgeotto | diretta | salvataggio esterno, archivio esterno |
| `PKD-0018-00` | 18 | Pidgeot | diretta | salvataggio esterno, archivio esterno |
| `PKD-0019-00` | 19 | Rattata | diretta | salvataggio esterno, archivio esterno |
| `PKD-0020-00` | 20 | Raticate | diretta | salvataggio esterno, archivio esterno |
| `PKD-0021-00` | 21 | Spearow | diretta | salvataggio esterno, archivio esterno |
| `PKD-0022-00` | 22 | Fearow | diretta | salvataggio esterno, archivio esterno |
| `PKD-0023-00` | 23 | Ekans | diretta | salvataggio esterno, archivio esterno |
| `PKD-0024-00` | 24 | Arbok | diretta | salvataggio esterno, archivio esterno |
| `PKD-0025-00` | 25 | Pikachu | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0026-00` | 26 | Raichu | diretta | salvataggio esterno, archivio esterno |
| `PKD-0027-00` | 27 | Sandshrew | diretta | salvataggio esterno, archivio esterno |
| `PKD-0028-00` | 28 | Sandslash | diretta | salvataggio esterno, archivio esterno |
| `PKD-0029-00` | 29 | Nidoran♀ | diretta | salvataggio esterno, archivio esterno |
| `PKD-0030-00` | 30 | Nidorina | diretta | salvataggio esterno, archivio esterno |
| `PKD-0031-00` | 31 | Nidoqueen | diretta | salvataggio esterno, archivio esterno |
| `PKD-0032-00` | 32 | Nidoran♂ | diretta | salvataggio esterno, archivio esterno |
| `PKD-0033-00` | 33 | Nidorino | diretta | salvataggio esterno, archivio esterno |
| `PKD-0034-00` | 34 | Nidoking | diretta | salvataggio esterno, archivio esterno |
| `PKD-0035-00` | 35 | Clefairy | diretta | salvataggio esterno, archivio esterno |
| `PKD-0036-00` | 36 | Clefable | diretta | salvataggio esterno, archivio esterno |
| `PKD-0037-00` | 37 | Vulpix | diretta | salvataggio esterno, archivio esterno |
| `PKD-0038-00` | 38 | Ninetales | diretta | salvataggio esterno, archivio esterno |
| `PKD-0039-00` | 39 | Jigglypuff | diretta | salvataggio esterno, archivio esterno |
| `PKD-0040-00` | 40 | Wigglytuff | diretta | salvataggio esterno, archivio esterno |
| `PKD-0041-00` | 41 | Zubat | diretta | salvataggio esterno, archivio esterno |
| `PKD-0042-00` | 42 | Golbat | diretta | salvataggio esterno, archivio esterno |
| `PKD-0043-00` | 43 | Oddish | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0044-00` | 44 | Gloom | diretta | salvataggio esterno, archivio esterno |
| `PKD-0045-00` | 45 | Vileplume | diretta | salvataggio esterno, archivio esterno |
| `PKD-0046-00` | 46 | Paras | diretta | salvataggio esterno, archivio esterno |
| `PKD-0047-00` | 47 | Parasect | diretta | salvataggio esterno, archivio esterno |
| `PKD-0048-00` | 48 | Venonat | diretta | salvataggio esterno, archivio esterno |
| `PKD-0049-00` | 49 | Venomoth | diretta | salvataggio esterno, archivio esterno |
| `PKD-0050-00` | 50 | Diglett | diretta | salvataggio esterno, archivio esterno |
| `PKD-0051-00` | 51 | Dugtrio | diretta | salvataggio esterno, archivio esterno |
| `PKD-0052-00` | 52 | Meowth | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0053-00` | 53 | Persian | diretta | salvataggio esterno, archivio esterno |
| `PKD-0054-00` | 54 | Psyduck | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0055-00` | 55 | Golduck | diretta | salvataggio esterno, archivio esterno |
| `PKD-0056-00` | 56 | Mankey | diretta | salvataggio esterno, archivio esterno |
| `PKD-0057-00` | 57 | Primeape | diretta | salvataggio esterno, archivio esterno |
| `PKD-0058-00` | 58 | Growlithe | diretta | salvataggio esterno, archivio esterno |
| `PKD-0059-00` | 59 | Arcanine | diretta | salvataggio esterno, archivio esterno |
| `PKD-0060-00` | 60 | Poliwag | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0061-00` | 61 | Poliwhirl | diretta | salvataggio esterno, archivio esterno |
| `PKD-0062-00` | 62 | Poliwrath | diretta | salvataggio esterno, archivio esterno |
| `PKD-0063-00` | 63 | Abra | diretta | salvataggio esterno, archivio esterno |
| `PKD-0064-00` | 64 | Kadabra | diretta | salvataggio esterno, archivio esterno |
| `PKD-0065-00` | 65 | Alakazam | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0066-00` | 66 | Machop | diretta | salvataggio esterno, archivio esterno |
| `PKD-0067-00` | 67 | Machoke | diretta | salvataggio esterno, archivio esterno |
| `PKD-0068-00` | 68 | Machamp | diretta | salvataggio esterno, archivio esterno |
| `PKD-0069-00` | 69 | Bellsprout | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0070-00` | 70 | Weepinbell | diretta | salvataggio esterno, archivio esterno |
| `PKD-0071-00` | 71 | Victreebel | diretta | salvataggio esterno, archivio esterno |
| `PKD-0072-00` | 72 | Tentacool | diretta | salvataggio esterno, archivio esterno |
| `PKD-0073-00` | 73 | Tentacruel | diretta | salvataggio esterno, archivio esterno |
| `PKD-0074-00` | 74 | Geodude | diretta | salvataggio esterno, archivio esterno |
| `PKD-0075-00` | 75 | Graveler | diretta | salvataggio esterno, archivio esterno |
| `PKD-0076-00` | 76 | Golem | diretta | salvataggio esterno, archivio esterno |
| `PKD-0077-00` | 77 | Ponyta | diretta | salvataggio esterno, archivio esterno |
| `PKD-0078-00` | 78 | Rapidash | diretta | salvataggio esterno, archivio esterno |
| `PKD-0079-00` | 79 | Slowpoke | diretta | salvataggio esterno, archivio esterno |
| `PKD-0080-00` | 80 | Slowbro | diretta | salvataggio esterno, archivio esterno |
| `PKD-0081-00` | 81 | Magnemite | diretta | salvataggio esterno, archivio esterno |
| `PKD-0082-00` | 82 | Magneton | diretta | salvataggio esterno, archivio esterno |
| `PKD-0083-00` | 83 | Farfetch’d | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0084-00` | 84 | Doduo | diretta | salvataggio esterno, archivio esterno |
| `PKD-0085-00` | 85 | Dodrio | diretta | salvataggio esterno, archivio esterno |
| `PKD-0086-00` | 86 | Seel | diretta | salvataggio esterno, archivio esterno |
| `PKD-0087-00` | 87 | Dewgong | diretta | salvataggio esterno, archivio esterno |
| `PKD-0088-00` | 88 | Grimer | diretta | salvataggio esterno, archivio esterno |
| `PKD-0089-00` | 89 | Muk | diretta | salvataggio esterno, archivio esterno |
| `PKD-0090-00` | 90 | Shellder | diretta | salvataggio esterno, archivio esterno |
| `PKD-0091-00` | 91 | Cloyster | diretta | salvataggio esterno, archivio esterno |
| `PKD-0092-00` | 92 | Gastly | diretta | salvataggio esterno, archivio esterno |
| `PKD-0093-00` | 93 | Haunter | diretta | salvataggio esterno, archivio esterno |
| `PKD-0094-00` | 94 | Gengar | diretta | salvataggio esterno, archivio esterno |
| `PKD-0095-00` | 95 | Onix | diretta | salvataggio esterno, archivio esterno |
| `PKD-0096-00` | 96 | Drowzee | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0097-00` | 97 | Hypno | diretta | salvataggio esterno, archivio esterno |
| `PKD-0098-00` | 98 | Krabby | diretta | salvataggio esterno, archivio esterno |
| `PKD-0099-00` | 99 | Kingler | diretta | salvataggio esterno, archivio esterno |
| `PKD-0100-00` | 100 | Voltorb | diretta | salvataggio esterno, archivio esterno |
| `PKD-0101-00` | 101 | Electrode | diretta | salvataggio esterno, archivio esterno |
| `PKD-0102-00` | 102 | Exeggcute | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0103-00` | 103 | Exeggutor | diretta | salvataggio esterno, archivio esterno |
| `PKD-0104-00` | 104 | Cubone | diretta | salvataggio esterno, archivio esterno |
| `PKD-0105-00` | 105 | Marowak | diretta | salvataggio esterno, archivio esterno |
| `PKD-0106-00` | 106 | Hitmonlee | diretta | salvataggio esterno, archivio esterno |
| `PKD-0107-00` | 107 | Hitmonchan | diretta | salvataggio esterno, archivio esterno |
| `PKD-0108-00` | 108 | Lickitung | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0109-00` | 109 | Koffing | diretta | salvataggio esterno, archivio esterno |
| `PKD-0110-00` | 110 | Weezing | diretta | salvataggio esterno, archivio esterno |
| `PKD-0111-00` | 111 | Rhyhorn | diretta | salvataggio esterno, archivio esterno |
| `PKD-0112-00` | 112 | Rhydon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0113-00` | 113 | Chansey | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0114-00` | 114 | Tangela | diretta | salvataggio esterno, archivio esterno |
| `PKD-0115-00` | 115 | Kangaskhan | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0116-00` | 116 | Horsea | diretta | salvataggio esterno, archivio esterno |
| `PKD-0117-00` | 117 | Seadra | diretta | salvataggio esterno, archivio esterno |
| `PKD-0118-00` | 118 | Goldeen | diretta | salvataggio esterno, archivio esterno |
| `PKD-0119-00` | 119 | Seaking | diretta | salvataggio esterno, archivio esterno |
| `PKD-0120-00` | 120 | Staryu | diretta | salvataggio esterno, archivio esterno |
| `PKD-0121-00` | 121 | Starmie | diretta | salvataggio esterno, archivio esterno |
| `PKD-0122-00` | 122 | Mr. Mime | diretta | salvataggio esterno, archivio esterno |
| `PKD-0123-00` | 123 | Scyther | diretta | salvataggio esterno, archivio esterno |
| `PKD-0124-00` | 124 | Jynx | diretta | salvataggio esterno, archivio esterno |
| `PKD-0125-00` | 125 | Electabuzz | diretta | salvataggio esterno, archivio esterno |
| `PKD-0126-00` | 126 | Magmar | diretta | salvataggio esterno, archivio esterno |
| `PKD-0127-00` | 127 | Pinsir | diretta | salvataggio esterno, archivio esterno |
| `PKD-0128-00` | 128 | Tauros | diretta | salvataggio esterno, archivio esterno |
| `PKD-0129-00` | 129 | Magikarp | diretta | salvataggio esterno, archivio esterno |
| `PKD-0130-00` | 130 | Gyarados | diretta | salvataggio esterno, archivio esterno |
| `PKD-0131-00` | 131 | Lapras | diretta | salvataggio esterno, archivio esterno |
| `PKD-0132-00` | 132 | Ditto | diretta | salvataggio esterno, archivio esterno |
| `PKD-0133-00` | 133 | Eevee | diretta | salvataggio esterno, archivio esterno |
| `PKD-0134-00` | 134 | Vaporeon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0135-00` | 135 | Jolteon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0136-00` | 136 | Flareon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0137-00` | 137 | Porygon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0138-00` | 138 | Omanyte | diretta | salvataggio esterno, archivio esterno |
| `PKD-0139-00` | 139 | Omastar | diretta | salvataggio esterno, archivio esterno |
| `PKD-0140-00` | 140 | Kabuto | diretta | salvataggio esterno, archivio esterno |
| `PKD-0141-00` | 141 | Kabutops | diretta | salvataggio esterno, archivio esterno |
| `PKD-0142-00` | 142 | Aerodactyl | diretta | salvataggio esterno, archivio esterno |
| `PKD-0143-00` | 143 | Snorlax | diretta | salvataggio esterno, archivio esterno |
| `PKD-0144-00` | 144 | Articuno | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0145-00` | 145 | Zapdos | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0146-00` | 146 | Moltres | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0147-00` | 147 | Dratini | diretta | salvataggio esterno, archivio esterno |
| `PKD-0148-00` | 148 | Dragonair | diretta | salvataggio esterno, archivio esterno |
| `PKD-0149-00` | 149 | Dragonite | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0150-00` | 150 | Mewtwo | diretta | salvataggio esterno, archivio esterno |
| `PKD-0151-00` | 151 | Mew | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0152-00` | 152 | Chikorita | diretta | salvataggio esterno, archivio esterno |
| `PKD-0153-00` | 153 | Bayleef | diretta | salvataggio esterno, archivio esterno |
| `PKD-0154-00` | 154 | Meganium | diretta | salvataggio esterno, archivio esterno |
| `PKD-0155-00` | 155 | Cyndaquil | diretta | salvataggio esterno, archivio esterno |
| `PKD-0156-00` | 156 | Quilava | diretta | salvataggio esterno, archivio esterno |
| `PKD-0157-00` | 157 | Typhlosion | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0158-00` | 158 | Totodile | diretta | salvataggio esterno, archivio esterno |
| `PKD-0159-00` | 159 | Croconaw | diretta | salvataggio esterno, archivio esterno |
| `PKD-0160-00` | 160 | Feraligatr | diretta | salvataggio esterno, archivio esterno |
| `PKD-0161-00` | 161 | Sentret | diretta | salvataggio esterno, archivio esterno |
| `PKD-0162-00` | 162 | Furret | diretta | salvataggio esterno, archivio esterno |
| `PKD-0163-00` | 163 | Hoothoot | diretta | salvataggio esterno, archivio esterno |
| `PKD-0164-00` | 164 | Noctowl | diretta | salvataggio esterno, archivio esterno |
| `PKD-0165-00` | 165 | Ledyba | diretta | salvataggio esterno, archivio esterno |
| `PKD-0166-00` | 166 | Ledian | diretta | salvataggio esterno, archivio esterno |
| `PKD-0167-00` | 167 | Spinarak | diretta | salvataggio esterno, archivio esterno |
| `PKD-0168-00` | 168 | Ariados | diretta | salvataggio esterno, archivio esterno |
| `PKD-0169-00` | 169 | Crobat | diretta | salvataggio esterno, archivio esterno |
| `PKD-0170-00` | 170 | Chinchou | diretta | salvataggio esterno, archivio esterno |
| `PKD-0171-00` | 171 | Lanturn | diretta | salvataggio esterno, archivio esterno |
| `PKD-0172-00` | 172 | Pichu | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0173-00` | 173 | Cleffa | diretta | salvataggio esterno, archivio esterno |
| `PKD-0174-00` | 174 | Igglybuff | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0175-00` | 175 | Togepi | diretta | salvataggio esterno, archivio esterno |
| `PKD-0176-00` | 176 | Togetic | diretta | salvataggio esterno, archivio esterno |
| `PKD-0177-00` | 177 | Natu | diretta | salvataggio esterno, archivio esterno |
| `PKD-0178-00` | 178 | Xatu | diretta | salvataggio esterno, archivio esterno |
| `PKD-0179-00` | 179 | Mareep | diretta | salvataggio esterno, archivio esterno |
| `PKD-0180-00` | 180 | Flaaffy | diretta | salvataggio esterno, archivio esterno |
| `PKD-0181-00` | 181 | Ampharos | diretta | salvataggio esterno, archivio esterno |
| `PKD-0182-00` | 182 | Bellossom | diretta | salvataggio esterno, archivio esterno |
| `PKD-0183-00` | 183 | Marill | diretta | salvataggio esterno, archivio esterno |
| `PKD-0184-00` | 184 | Azumarill | diretta | salvataggio esterno, archivio esterno |
| `PKD-0185-00` | 185 | Sudowoodo | diretta | salvataggio esterno, archivio esterno |
| `PKD-0186-00` | 186 | Politoed | diretta | salvataggio esterno, archivio esterno |
| `PKD-0187-00` | 187 | Hoppip | diretta | salvataggio esterno, archivio esterno |
| `PKD-0188-00` | 188 | Skiploom | diretta | salvataggio esterno, archivio esterno |
| `PKD-0189-00` | 189 | Jumpluff | diretta | salvataggio esterno, archivio esterno |
| `PKD-0190-00` | 190 | Aipom | diretta | salvataggio esterno, archivio esterno |
| `PKD-0191-00` | 191 | Sunkern | diretta | salvataggio esterno, archivio esterno |
| `PKD-0192-00` | 192 | Sunflora | diretta | salvataggio esterno, archivio esterno |
| `PKD-0193-00` | 193 | Yanma | diretta | salvataggio esterno, archivio esterno |
| `PKD-0194-00` | 194 | Wooper | diretta | salvataggio esterno, archivio esterno |
| `PKD-0195-00` | 195 | Quagsire | diretta | salvataggio esterno, archivio esterno |
| `PKD-0196-00` | 196 | Espeon | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0197-00` | 197 | Umbreon | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0198-00` | 198 | Murkrow | diretta | salvataggio esterno, archivio esterno |
| `PKD-0199-00` | 199 | Slowking | diretta | salvataggio esterno, archivio esterno |
| `PKD-0200-00` | 200 | Misdreavus | diretta | salvataggio esterno, archivio esterno |
| `PKD-0201-00` | 201 | Unown | diretta | salvataggio esterno, archivio esterno |
| `PKD-0202-00` | 202 | Wobbuffet | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0203-00` | 203 | Girafarig | diretta | salvataggio esterno, archivio esterno |
| `PKD-0204-00` | 204 | Pineco | diretta | salvataggio esterno, archivio esterno |
| `PKD-0205-00` | 205 | Forretress | diretta | salvataggio esterno, archivio esterno |
| `PKD-0206-00` | 206 | Dunsparce | diretta | salvataggio esterno, archivio esterno |
| `PKD-0207-00` | 207 | Gligar | diretta | salvataggio esterno, archivio esterno |
| `PKD-0208-00` | 208 | Steelix | diretta | salvataggio esterno, archivio esterno |
| `PKD-0209-00` | 209 | Snubbull | diretta | salvataggio esterno, archivio esterno |
| `PKD-0210-00` | 210 | Granbull | diretta | salvataggio esterno, archivio esterno |
| `PKD-0211-00` | 211 | Qwilfish | diretta | salvataggio esterno, archivio esterno |
| `PKD-0212-00` | 212 | Scizor | diretta | salvataggio esterno, archivio esterno |
| `PKD-0213-00` | 213 | Shuckle | diretta | salvataggio esterno, archivio esterno |
| `PKD-0214-00` | 214 | Heracross | diretta | salvataggio esterno, archivio esterno |
| `PKD-0215-00` | 215 | Sneasel | diretta | salvataggio esterno, archivio esterno |
| `PKD-0216-00` | 216 | Teddiursa | diretta | salvataggio esterno, archivio esterno |
| `PKD-0217-00` | 217 | Ursaring | diretta | salvataggio esterno, archivio esterno |
| `PKD-0218-00` | 218 | Slugma | diretta | salvataggio esterno, archivio esterno |
| `PKD-0219-00` | 219 | Magcargo | diretta | salvataggio esterno, archivio esterno |
| `PKD-0220-00` | 220 | Swinub | diretta | salvataggio esterno, archivio esterno |
| `PKD-0221-00` | 221 | Piloswine | diretta | salvataggio esterno, archivio esterno |
| `PKD-0222-00` | 222 | Corsola | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0223-00` | 223 | Remoraid | diretta | salvataggio esterno, archivio esterno |
| `PKD-0224-00` | 224 | Octillery | diretta | salvataggio esterno, archivio esterno |
| `PKD-0225-00` | 225 | Delibird | diretta | salvataggio esterno, archivio esterno |
| `PKD-0226-00` | 226 | Mantine | diretta | salvataggio esterno, archivio esterno |
| `PKD-0227-00` | 227 | Skarmory | diretta | salvataggio esterno, archivio esterno |
| `PKD-0228-00` | 228 | Houndour | diretta | salvataggio esterno, archivio esterno |
| `PKD-0229-00` | 229 | Houndoom | diretta | salvataggio esterno, archivio esterno |
| `PKD-0230-00` | 230 | Kingdra | diretta | salvataggio esterno, archivio esterno |
| `PKD-0231-00` | 231 | Phanpy | diretta | salvataggio esterno, archivio esterno |
| `PKD-0232-00` | 232 | Donphan | diretta | salvataggio esterno, archivio esterno |
| `PKD-0233-00` | 233 | Porygon2 | diretta | salvataggio esterno, archivio esterno |
| `PKD-0234-00` | 234 | Stantler | diretta | salvataggio esterno, archivio esterno |
| `PKD-0235-00` | 235 | Smeargle | diretta | salvataggio esterno, archivio esterno |
| `PKD-0236-00` | 236 | Tyrogue | diretta | salvataggio esterno, archivio esterno |
| `PKD-0237-00` | 237 | Hitmontop | diretta | salvataggio esterno, archivio esterno |
| `PKD-0238-00` | 238 | Smoochum | diretta | salvataggio esterno, archivio esterno |
| `PKD-0239-00` | 239 | Elekid | diretta | salvataggio esterno, archivio esterno |
| `PKD-0240-00` | 240 | Magby | diretta | salvataggio esterno, archivio esterno |
| `PKD-0241-00` | 241 | Miltank | diretta | salvataggio esterno, archivio esterno |
| `PKD-0242-00` | 242 | Blissey | diretta | salvataggio esterno, archivio esterno |
| `PKD-0243-00` | 243 | Raikou | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0244-00` | 244 | Entei | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0245-00` | 245 | Suicune | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0246-00` | 246 | Larvitar | diretta | salvataggio esterno, archivio esterno |
| `PKD-0247-00` | 247 | Pupitar | diretta | salvataggio esterno, archivio esterno |
| `PKD-0248-00` | 248 | Tyranitar | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0249-00` | 249 | Lugia | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0250-00` | 250 | Ho-Oh | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0251-00` | 251 | Celebi | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0252-00` | 252 | Treecko | diretta | salvataggio esterno, archivio esterno |
| `PKD-0253-00` | 253 | Grovyle | diretta | salvataggio esterno, archivio esterno |
| `PKD-0254-00` | 254 | Sceptile | diretta | salvataggio esterno, archivio esterno |
| `PKD-0255-00` | 255 | Torchic | diretta | salvataggio esterno, archivio esterno |
| `PKD-0256-00` | 256 | Combusken | diretta | salvataggio esterno, archivio esterno |
| `PKD-0257-00` | 257 | Blaziken | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0258-00` | 258 | Mudkip | diretta | salvataggio esterno, archivio esterno |
| `PKD-0259-00` | 259 | Marshtomp | diretta | salvataggio esterno, archivio esterno |
| `PKD-0260-00` | 260 | Swampert | diretta | salvataggio esterno, archivio esterno |
| `PKD-0261-00` | 261 | Poochyena | diretta | nessuna |
| `PKD-0262-00` | 262 | Mightyena | diretta | salvataggio esterno, archivio esterno |
| `PKD-0263-00` | 263 | Zigzagoon | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0264-00` | 264 | Linoone | diretta | salvataggio esterno, archivio esterno |
| `PKD-0265-00` | 265 | Wurmple | diretta | salvataggio esterno, archivio esterno |
| `PKD-0266-00` | 266 | Silcoon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0267-00` | 267 | Beautifly | diretta | salvataggio esterno, archivio esterno |
| `PKD-0268-00` | 268 | Cascoon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0269-00` | 269 | Dustox | diretta | salvataggio esterno, archivio esterno |
| `PKD-0270-00` | 270 | Lotad | diretta | salvataggio esterno, archivio esterno |
| `PKD-0271-00` | 271 | Lombre | diretta | salvataggio esterno, archivio esterno |
| `PKD-0272-00` | 272 | Ludicolo | diretta | salvataggio esterno, archivio esterno |
| `PKD-0273-00` | 273 | Seedot | diretta | salvataggio esterno, archivio esterno |
| `PKD-0274-00` | 274 | Nuzleaf | diretta | salvataggio esterno, archivio esterno |
| `PKD-0275-00` | 275 | Shiftry | diretta | salvataggio esterno, archivio esterno |
| `PKD-0276-00` | 276 | Taillow | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0277-00` | 277 | Swellow | diretta | salvataggio esterno, archivio esterno |
| `PKD-0278-00` | 278 | Wingull | diretta | salvataggio esterno, archivio esterno |
| `PKD-0279-00` | 279 | Pelipper | diretta | salvataggio esterno, archivio esterno |
| `PKD-0280-00` | 280 | Ralts | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0281-00` | 281 | Kirlia | diretta | salvataggio esterno, archivio esterno |
| `PKD-0282-00` | 282 | Gardevoir | diretta | salvataggio esterno, archivio esterno |
| `PKD-0283-00` | 283 | Surskit | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0284-00` | 284 | Masquerain | diretta | salvataggio esterno, archivio esterno |
| `PKD-0285-00` | 285 | Shroomish | diretta | salvataggio esterno, archivio esterno |
| `PKD-0286-00` | 286 | Breloom | diretta | salvataggio esterno, archivio esterno |
| `PKD-0287-00` | 287 | Slakoth | diretta | salvataggio esterno, archivio esterno |
| `PKD-0288-00` | 288 | Vigoroth | diretta | salvataggio esterno, archivio esterno |
| `PKD-0289-00` | 289 | Slaking | diretta | salvataggio esterno, archivio esterno |
| `PKD-0290-00` | 290 | Nincada | diretta | salvataggio esterno, archivio esterno |
| `PKD-0291-00` | 291 | Ninjask | diretta | salvataggio esterno, archivio esterno |
| `PKD-0292-00` | 292 | Shedinja | diretta | salvataggio esterno, archivio esterno |
| `PKD-0293-00` | 293 | Whismur | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0294-00` | 294 | Loudred | diretta | salvataggio esterno, archivio esterno |
| `PKD-0295-00` | 295 | Exploud | diretta | salvataggio esterno, archivio esterno |
| `PKD-0296-00` | 296 | Makuhita | diretta | salvataggio esterno, archivio esterno |
| `PKD-0297-00` | 297 | Hariyama | diretta | salvataggio esterno, archivio esterno |
| `PKD-0298-00` | 298 | Azurill | diretta | salvataggio esterno, archivio esterno |
| `PKD-0299-00` | 299 | Nosepass | diretta | salvataggio esterno, archivio esterno |
| `PKD-0300-00` | 300 | Skitty | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0301-00` | 301 | Delcatty | diretta | salvataggio esterno, archivio esterno |
| `PKD-0302-00` | 302 | Sableye | diretta | salvataggio esterno, archivio esterno |
| `PKD-0303-00` | 303 | Mawile | diretta | salvataggio esterno, archivio esterno |
| `PKD-0304-00` | 304 | Aron | diretta | salvataggio esterno, archivio esterno |
| `PKD-0305-00` | 305 | Lairon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0306-00` | 306 | Aggron | diretta | salvataggio esterno, archivio esterno |
| `PKD-0307-00` | 307 | Meditite | diretta | salvataggio esterno, archivio esterno |
| `PKD-0308-00` | 308 | Medicham | diretta | salvataggio esterno, archivio esterno |
| `PKD-0309-00` | 309 | Electrike | diretta | salvataggio esterno, archivio esterno |
| `PKD-0310-00` | 310 | Manectric | diretta | salvataggio esterno, archivio esterno |
| `PKD-0311-00` | 311 | Plusle | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0312-00` | 312 | Minun | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0313-00` | 313 | Volbeat | diretta | salvataggio esterno, archivio esterno |
| `PKD-0314-00` | 314 | Illumise | diretta | salvataggio esterno, archivio esterno |
| `PKD-0315-00` | 315 | Roselia | diretta | salvataggio esterno, archivio esterno |
| `PKD-0316-00` | 316 | Gulpin | diretta | salvataggio esterno, archivio esterno |
| `PKD-0317-00` | 317 | Swalot | diretta | salvataggio esterno, archivio esterno |
| `PKD-0318-00` | 318 | Carvanha | diretta | salvataggio esterno, archivio esterno |
| `PKD-0319-00` | 319 | Sharpedo | diretta | salvataggio esterno, archivio esterno |
| `PKD-0320-00` | 320 | Wailmer | diretta | salvataggio esterno, archivio esterno |
| `PKD-0321-00` | 321 | Wailord | diretta | salvataggio esterno, archivio esterno |
| `PKD-0322-00` | 322 | Numel | diretta | salvataggio esterno, archivio esterno |
| `PKD-0323-00` | 323 | Camerupt | diretta | salvataggio esterno, archivio esterno |
| `PKD-0324-00` | 324 | Torkoal | diretta | salvataggio esterno, archivio esterno |
| `PKD-0325-00` | 325 | Spoink | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0326-00` | 326 | Grumpig | diretta | salvataggio esterno, archivio esterno |
| `PKD-0327-00` | 327 | Spinda | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0328-00` | 328 | Trapinch | diretta | salvataggio esterno, archivio esterno |
| `PKD-0329-00` | 329 | Vibrava | diretta | salvataggio esterno, archivio esterno |
| `PKD-0330-00` | 330 | Flygon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0331-00` | 331 | Cacnea | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0332-00` | 332 | Cacturne | diretta | salvataggio esterno, archivio esterno |
| `PKD-0333-00` | 333 | Swablu | diretta | salvataggio esterno, archivio esterno |
| `PKD-0334-00` | 334 | Altaria | diretta | salvataggio esterno, archivio esterno |
| `PKD-0335-00` | 335 | Zangoose | diretta | salvataggio esterno, archivio esterno |
| `PKD-0336-00` | 336 | Seviper | diretta | salvataggio esterno, archivio esterno |
| `PKD-0337-00` | 337 | Lunatone | diretta | salvataggio esterno, archivio esterno |
| `PKD-0338-00` | 338 | Solrock | diretta | salvataggio esterno, archivio esterno |
| `PKD-0339-00` | 339 | Barboach | diretta | salvataggio esterno, archivio esterno |
| `PKD-0340-00` | 340 | Whiscash | diretta | salvataggio esterno, archivio esterno |
| `PKD-0341-00` | 341 | Corphish | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0342-00` | 342 | Crawdaunt | diretta | salvataggio esterno, archivio esterno |
| `PKD-0343-00` | 343 | Baltoy | diretta | salvataggio esterno, archivio esterno |
| `PKD-0344-00` | 344 | Claydol | diretta | salvataggio esterno, archivio esterno |
| `PKD-0345-00` | 345 | Lileep | diretta | salvataggio esterno, archivio esterno |
| `PKD-0346-00` | 346 | Cradily | diretta | salvataggio esterno, archivio esterno |
| `PKD-0347-00` | 347 | Anorith | diretta | salvataggio esterno, archivio esterno |
| `PKD-0348-00` | 348 | Armaldo | diretta | salvataggio esterno, archivio esterno |
| `PKD-0349-00` | 349 | Feebas | diretta | salvataggio esterno, archivio esterno |
| `PKD-0350-00` | 350 | Milotic | diretta | salvataggio esterno, archivio esterno |
| `PKD-0351-00` | 351 | Castform | diretta | salvataggio esterno, archivio esterno |
| `PKD-0352-00` | 352 | Kecleon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0353-00` | 353 | Shuppet | diretta | salvataggio esterno, archivio esterno |
| `PKD-0354-00` | 354 | Banette | diretta | salvataggio esterno, archivio esterno |
| `PKD-0355-00` | 355 | Duskull | diretta | salvataggio esterno, archivio esterno |
| `PKD-0356-00` | 356 | Dusclops | diretta | salvataggio esterno, archivio esterno |
| `PKD-0357-00` | 357 | Tropius | diretta | salvataggio esterno, archivio esterno |
| `PKD-0358-00` | 358 | Chimecho | diretta | salvataggio esterno, archivio esterno |
| `PKD-0359-00` | 359 | Absol | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0360-00` | 360 | Wynaut | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0361-00` | 361 | Snorunt | diretta | salvataggio esterno, archivio esterno |
| `PKD-0362-00` | 362 | Glalie | diretta | salvataggio esterno, archivio esterno |
| `PKD-0363-00` | 363 | Spheal | diretta | salvataggio esterno, archivio esterno |
| `PKD-0364-00` | 364 | Sealeo | diretta | salvataggio esterno, archivio esterno |
| `PKD-0365-00` | 365 | Walrein | diretta | salvataggio esterno, archivio esterno |
| `PKD-0366-00` | 366 | Clamperl | diretta | salvataggio esterno, archivio esterno |
| `PKD-0367-00` | 367 | Huntail | diretta | salvataggio esterno, archivio esterno |
| `PKD-0368-00` | 368 | Gorebyss | diretta | salvataggio esterno, archivio esterno |
| `PKD-0369-00` | 369 | Relicanth | diretta | salvataggio esterno, archivio esterno |
| `PKD-0370-00` | 370 | Luvdisc | diretta | salvataggio esterno, archivio esterno |
| `PKD-0371-00` | 371 | Bagon | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0372-00` | 372 | Shelgon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0373-00` | 373 | Salamence | diretta | salvataggio esterno, archivio esterno |
| `PKD-0374-00` | 374 | Beldum | diretta | salvataggio esterno, archivio esterno |
| `PKD-0375-00` | 375 | Metang | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0376-00` | 376 | Metagross | diretta | salvataggio esterno, archivio esterno |
| `PKD-0377-00` | 377 | Regirock | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0378-00` | 378 | Regice | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0379-00` | 379 | Registeel | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0380-00` | 380 | Latias | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0381-00` | 381 | Latios | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0382-00` | 382 | Kyogre | diretta | salvataggio esterno, archivio esterno |
| `PKD-0383-00` | 383 | Groudon | diretta | salvataggio esterno, archivio esterno |
| `PKD-0384-00` | 384 | Rayquaza | diretta | salvataggio esterno, archivio esterno |
| `PKD-0385-00` | 385 | Jirachi | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0386-00` | 386 | Deoxys | diretta | evento Gen 3 producibile, salvataggio esterno, archivio esterno |
| `PKD-0387-00` | 387 | Turtwig | diretta | nessuna |
| `PKD-0388-00` | 388 | Grotle | diretta | nessuna |
| `PKD-0389-00` | 389 | Torterra | diretta | nessuna |
| `PKD-0390-00` | 390 | Chimchar | diretta | nessuna |
| `PKD-0391-00` | 391 | Monferno | diretta | nessuna |
| `PKD-0392-00` | 392 | Infernape | diretta | nessuna |
| `PKD-0393-00` | 393 | Piplup | diretta | nessuna |
| `PKD-0394-00` | 394 | Prinplup | diretta | nessuna |
| `PKD-0395-00` | 395 | Empoleon | diretta | nessuna |
| `PKD-0396-00` | 396 | Starly | diretta | nessuna |
| `PKD-0397-00` | 397 | Staravia | diretta | nessuna |
| `PKD-0398-00` | 398 | Staraptor | diretta | nessuna |
| `PKD-0399-00` | 399 | Bidoof | diretta | nessuna |
| `PKD-0400-00` | 400 | Bibarel | diretta | nessuna |
| `PKD-0401-00` | 401 | Kricketot | diretta | nessuna |
| `PKD-0402-00` | 402 | Kricketune | diretta | nessuna |
| `PKD-0403-00` | 403 | Shinx | diretta | nessuna |
| `PKD-0404-00` | 404 | Luxio | diretta | nessuna |
| `PKD-0405-00` | 405 | Luxray | diretta | nessuna |
| `PKD-0406-00` | 406 | Budew | diretta | nessuna |
| `PKD-0407-00` | 407 | Roserade | diretta | nessuna |
| `PKD-0408-00` | 408 | Cranidos | diretta | nessuna |
| `PKD-0409-00` | 409 | Rampardos | diretta | nessuna |
| `PKD-0410-00` | 410 | Shieldon | diretta | nessuna |
| `PKD-0411-00` | 411 | Bastiodon | diretta | nessuna |
| `PKD-0412-00` | 412 | Burmy | diretta | nessuna |
| `PKD-0413-00` | 413 | Wormadam | diretta | nessuna |
| `PKD-0414-00` | 414 | Mothim | diretta | nessuna |
| `PKD-0415-00` | 415 | Combee | diretta | nessuna |
| `PKD-0416-00` | 416 | Vespiquen | diretta | nessuna |
| `PKD-0417-00` | 417 | Pachirisu | diretta | nessuna |
| `PKD-0418-00` | 418 | Buizel | diretta | nessuna |
| `PKD-0419-00` | 419 | Floatzel | diretta | nessuna |
| `PKD-0420-00` | 420 | Cherubi | diretta | nessuna |
| `PKD-0421-00` | 421 | Cherrim | diretta | nessuna |
| `PKD-0422-00` | 422 | Shellos | diretta | nessuna |
| `PKD-0423-00` | 423 | Gastrodon | diretta | nessuna |
| `PKD-0424-00` | 424 | Ambipom | diretta | nessuna |
| `PKD-0425-00` | 425 | Drifloon | diretta | nessuna |
| `PKD-0426-00` | 426 | Drifblim | diretta | nessuna |
| `PKD-0427-00` | 427 | Buneary | diretta | nessuna |
| `PKD-0428-00` | 428 | Lopunny | diretta | nessuna |
| `PKD-0429-00` | 429 | Mismagius | diretta | nessuna |
| `PKD-0430-00` | 430 | Honchkrow | diretta | nessuna |
| `PKD-0431-00` | 431 | Glameow | diretta | nessuna |
| `PKD-0432-00` | 432 | Purugly | diretta | nessuna |
| `PKD-0433-00` | 433 | Chingling | diretta | nessuna |
| `PKD-0434-00` | 434 | Stunky | diretta | nessuna |
| `PKD-0435-00` | 435 | Skuntank | diretta | nessuna |
| `PKD-0436-00` | 436 | Bronzor | diretta | nessuna |
| `PKD-0437-00` | 437 | Bronzong | diretta | nessuna |
| `PKD-0438-00` | 438 | Bonsly | diretta | nessuna |
| `PKD-0439-00` | 439 | Mime Jr. | diretta | nessuna |
| `PKD-0440-00` | 440 | Happiny | diretta | nessuna |
| `PKD-0441-00` | 441 | Chatot | diretta | nessuna |
| `PKD-0442-00` | 442 | Spiritomb | diretta | nessuna |
| `PKD-0443-00` | 443 | Gible | diretta | nessuna |
| `PKD-0444-00` | 444 | Gabite | diretta | nessuna |
| `PKD-0445-00` | 445 | Garchomp | diretta | nessuna |
| `PKD-0446-00` | 446 | Munchlax | diretta | nessuna |
| `PKD-0447-00` | 447 | Riolu | diretta | nessuna |
| `PKD-0448-00` | 448 | Lucario | diretta | nessuna |
| `PKD-0449-00` | 449 | Hippopotas | diretta | nessuna |
| `PKD-0450-00` | 450 | Hippowdon | diretta | nessuna |
| `PKD-0451-00` | 451 | Skorupi | diretta | nessuna |
| `PKD-0452-00` | 452 | Drapion | diretta | nessuna |
| `PKD-0453-00` | 453 | Croagunk | diretta | nessuna |
| `PKD-0454-00` | 454 | Toxicroak | diretta | nessuna |
| `PKD-0455-00` | 455 | Carnivine | diretta | nessuna |
| `PKD-0456-00` | 456 | Finneon | diretta | nessuna |
| `PKD-0457-00` | 457 | Lumineon | diretta | nessuna |
| `PKD-0458-00` | 458 | Mantyke | diretta | nessuna |
| `PKD-0459-00` | 459 | Snover | diretta | nessuna |
| `PKD-0460-00` | 460 | Abomasnow | diretta | nessuna |
| `PKD-0461-00` | 461 | Weavile | diretta | nessuna |
| `PKD-0462-00` | 462 | Magnezone | diretta | nessuna |
| `PKD-0463-00` | 463 | Lickilicky | diretta | nessuna |
| `PKD-0464-00` | 464 | Rhyperior | diretta | nessuna |
| `PKD-0465-00` | 465 | Tangrowth | diretta | nessuna |
| `PKD-0466-00` | 466 | Electivire | diretta | nessuna |
| `PKD-0467-00` | 467 | Magmortar | diretta | nessuna |
| `PKD-0468-00` | 468 | Togekiss | diretta | nessuna |
| `PKD-0469-00` | 469 | Yanmega | diretta | nessuna |
| `PKD-0470-00` | 470 | Leafeon | diretta | nessuna |
| `PKD-0471-00` | 471 | Glaceon | diretta | nessuna |
| `PKD-0472-00` | 472 | Gliscor | diretta | nessuna |
| `PKD-0473-00` | 473 | Mamoswine | diretta | nessuna |
| `PKD-0474-00` | 474 | Porygon-Z | diretta | nessuna |
| `PKD-0475-00` | 475 | Gallade | diretta | nessuna |
| `PKD-0476-00` | 476 | Probopass | diretta | nessuna |
| `PKD-0477-00` | 477 | Dusknoir | diretta | nessuna |
| `PKD-0478-00` | 478 | Froslass | diretta | nessuna |
| `PKD-0479-00` | 479 | Rotom | diretta | nessuna |
| `PKD-0480-00` | 480 | Uxie | diretta | nessuna |
| `PKD-0481-00` | 481 | Mesprit | diretta | nessuna |
| `PKD-0482-00` | 482 | Azelf | diretta | nessuna |
| `PKD-0483-00` | 483 | Dialga | diretta | nessuna |
| `PKD-0484-00` | 484 | Palkia | diretta | nessuna |
| `PKD-0485-00` | 485 | Heatran | diretta | nessuna |
| `PKD-0486-00` | 486 | Regigigas | diretta | nessuna |
| `PKD-0487-00` | 487 | Giratina | diretta | nessuna |
| `PKD-0488-00` | 488 | Cresselia | diretta | nessuna |
| `PKD-0489-00` | 489 | Phione | diretta | nessuna |
| `PKD-0490-00` | 490 | Manaphy | diretta | nessuna |
| `PKD-0491-00` | 491 | Darkrai | diretta | nessuna |
| `PKD-0492-00` | 492 | Shaymin | diretta | nessuna |
| `PKD-0493-00` | 493 | Arceus | diretta | nessuna |
| `PKD-0494-00` | 494 | Victini | diretta | nessuna |
| `PKD-0495-00` | 495 | Snivy | diretta | nessuna |
| `PKD-0496-00` | 496 | Servine | diretta | nessuna |
| `PKD-0497-00` | 497 | Serperior | diretta | nessuna |
| `PKD-0498-00` | 498 | Tepig | diretta | nessuna |
| `PKD-0499-00` | 499 | Pignite | diretta | nessuna |
| `PKD-0500-00` | 500 | Emboar | diretta | nessuna |
| `PKD-0501-00` | 501 | Oshawott | diretta | nessuna |
| `PKD-0502-00` | 502 | Dewott | diretta | nessuna |
| `PKD-0503-00` | 503 | Samurott | diretta | nessuna |
| `PKD-0504-00` | 504 | Patrat | diretta | nessuna |
| `PKD-0505-00` | 505 | Watchog | diretta | nessuna |
| `PKD-0506-00` | 506 | Lillipup | diretta | nessuna |
| `PKD-0507-00` | 507 | Herdier | diretta | nessuna |
| `PKD-0508-00` | 508 | Stoutland | diretta | nessuna |
| `PKD-0509-00` | 509 | Purrloin | diretta | nessuna |
| `PKD-0510-00` | 510 | Liepard | diretta | nessuna |
| `PKD-0511-00` | 511 | Pansage | diretta | nessuna |
| `PKD-0512-00` | 512 | Simisage | diretta | nessuna |
| `PKD-0513-00` | 513 | Pansear | diretta | nessuna |
| `PKD-0514-00` | 514 | Simisear | diretta | nessuna |
| `PKD-0515-00` | 515 | Panpour | diretta | nessuna |
| `PKD-0516-00` | 516 | Simipour | diretta | nessuna |
| `PKD-0517-00` | 517 | Munna | diretta | nessuna |
| `PKD-0518-00` | 518 | Musharna | diretta | nessuna |
| `PKD-0519-00` | 519 | Pidove | diretta | nessuna |
| `PKD-0520-00` | 520 | Tranquill | diretta | nessuna |
| `PKD-0521-00` | 521 | Unfezant | diretta | nessuna |
| `PKD-0522-00` | 522 | Blitzle | diretta | nessuna |
| `PKD-0523-00` | 523 | Zebstrika | diretta | nessuna |
| `PKD-0524-00` | 524 | Roggenrola | diretta | nessuna |
| `PKD-0525-00` | 525 | Boldore | diretta | nessuna |
| `PKD-0526-00` | 526 | Gigalith | diretta | nessuna |
| `PKD-0527-00` | 527 | Woobat | diretta | nessuna |
| `PKD-0528-00` | 528 | Swoobat | diretta | nessuna |
| `PKD-0529-00` | 529 | Drilbur | diretta | nessuna |
| `PKD-0530-00` | 530 | Excadrill | diretta | nessuna |
| `PKD-0531-00` | 531 | Audino | diretta | nessuna |
| `PKD-0532-00` | 532 | Timburr | diretta | nessuna |
| `PKD-0533-00` | 533 | Gurdurr | diretta | nessuna |
| `PKD-0534-00` | 534 | Conkeldurr | diretta | nessuna |
| `PKD-0535-00` | 535 | Tympole | diretta | nessuna |
| `PKD-0536-00` | 536 | Palpitoad | diretta | nessuna |
| `PKD-0537-00` | 537 | Seismitoad | diretta | nessuna |
| `PKD-0538-00` | 538 | Throh | diretta | nessuna |
| `PKD-0539-00` | 539 | Sawk | diretta | nessuna |
| `PKD-0540-00` | 540 | Sewaddle | diretta | nessuna |
| `PKD-0541-00` | 541 | Swadloon | diretta | nessuna |
| `PKD-0542-00` | 542 | Leavanny | diretta | nessuna |
| `PKD-0543-00` | 543 | Venipede | diretta | nessuna |
| `PKD-0544-00` | 544 | Whirlipede | diretta | nessuna |
| `PKD-0545-00` | 545 | Scolipede | diretta | nessuna |
| `PKD-0546-00` | 546 | Cottonee | diretta | nessuna |
| `PKD-0547-00` | 547 | Whimsicott | diretta | nessuna |
| `PKD-0548-00` | 548 | Petilil | diretta | nessuna |
| `PKD-0549-00` | 549 | Lilligant | diretta | nessuna |
| `PKD-0550-00` | 550 | Basculin | diretta | nessuna |
| `PKD-0551-00` | 551 | Sandile | diretta | nessuna |
| `PKD-0552-00` | 552 | Krokorok | diretta | nessuna |
| `PKD-0553-00` | 553 | Krookodile | diretta | nessuna |
| `PKD-0554-00` | 554 | Darumaka | diretta | nessuna |
| `PKD-0555-00` | 555 | Darmanitan | diretta | nessuna |
| `PKD-0556-00` | 556 | Maractus | diretta | nessuna |
| `PKD-0557-00` | 557 | Dwebble | diretta | nessuna |
| `PKD-0558-00` | 558 | Crustle | diretta | nessuna |
| `PKD-0559-00` | 559 | Scraggy | diretta | nessuna |
| `PKD-0560-00` | 560 | Scrafty | diretta | nessuna |
| `PKD-0561-00` | 561 | Sigilyph | diretta | nessuna |
| `PKD-0562-00` | 562 | Yamask | diretta | nessuna |
| `PKD-0563-00` | 563 | Cofagrigus | diretta | nessuna |
| `PKD-0564-00` | 564 | Tirtouga | diretta | nessuna |
| `PKD-0565-00` | 565 | Carracosta | diretta | nessuna |
| `PKD-0566-00` | 566 | Archen | diretta | nessuna |
| `PKD-0567-00` | 567 | Archeops | diretta | nessuna |
| `PKD-0568-00` | 568 | Trubbish | diretta | nessuna |
| `PKD-0569-00` | 569 | Garbodor | diretta | nessuna |
| `PKD-0570-00` | 570 | Zorua | diretta | nessuna |
| `PKD-0571-00` | 571 | Zoroark | diretta | nessuna |
| `PKD-0572-00` | 572 | Minccino | diretta | nessuna |
| `PKD-0573-00` | 573 | Cinccino | diretta | nessuna |
| `PKD-0574-00` | 574 | Gothita | diretta | nessuna |
| `PKD-0575-00` | 575 | Gothorita | diretta | nessuna |
| `PKD-0576-00` | 576 | Gothitelle | diretta | nessuna |
| `PKD-0577-00` | 577 | Solosis | diretta | nessuna |
| `PKD-0578-00` | 578 | Duosion | diretta | nessuna |
| `PKD-0579-00` | 579 | Reuniclus | diretta | nessuna |
| `PKD-0580-00` | 580 | Ducklett | diretta | nessuna |
| `PKD-0581-00` | 581 | Swanna | diretta | nessuna |
| `PKD-0582-00` | 582 | Vanillite | diretta | nessuna |
| `PKD-0583-00` | 583 | Vanillish | diretta | nessuna |
| `PKD-0584-00` | 584 | Vanilluxe | diretta | nessuna |
| `PKD-0585-00` | 585 | Deerling | diretta | nessuna |
| `PKD-0586-00` | 586 | Sawsbuck | diretta | nessuna |
| `PKD-0587-00` | 587 | Emolga | diretta | nessuna |
| `PKD-0588-00` | 588 | Karrablast | diretta | nessuna |
| `PKD-0589-00` | 589 | Escavalier | diretta | nessuna |
| `PKD-0590-00` | 590 | Foongus | diretta | nessuna |
| `PKD-0591-00` | 591 | Amoonguss | diretta | nessuna |
| `PKD-0592-00` | 592 | Frillish | diretta | nessuna |
| `PKD-0593-00` | 593 | Jellicent | diretta | nessuna |
| `PKD-0594-00` | 594 | Alomomola | diretta | nessuna |
| `PKD-0595-00` | 595 | Joltik | diretta | nessuna |
| `PKD-0596-00` | 596 | Galvantula | diretta | nessuna |
| `PKD-0597-00` | 597 | Ferroseed | diretta | nessuna |
| `PKD-0598-00` | 598 | Ferrothorn | diretta | nessuna |
| `PKD-0599-00` | 599 | Klink | diretta | nessuna |
| `PKD-0600-00` | 600 | Klang | diretta | nessuna |
| `PKD-0601-00` | 601 | Klinklang | diretta | nessuna |
| `PKD-0602-00` | 602 | Tynamo | diretta | nessuna |
| `PKD-0603-00` | 603 | Eelektrik | diretta | nessuna |
| `PKD-0604-00` | 604 | Eelektross | diretta | nessuna |
| `PKD-0605-00` | 605 | Elgyem | diretta | nessuna |
| `PKD-0606-00` | 606 | Beheeyem | diretta | nessuna |
| `PKD-0607-00` | 607 | Litwick | diretta | nessuna |
| `PKD-0608-00` | 608 | Lampent | diretta | nessuna |
| `PKD-0609-00` | 609 | Chandelure | diretta | nessuna |
| `PKD-0610-00` | 610 | Axew | diretta | nessuna |
| `PKD-0611-00` | 611 | Fraxure | diretta | nessuna |
| `PKD-0612-00` | 612 | Haxorus | diretta | nessuna |
| `PKD-0613-00` | 613 | Cubchoo | diretta | nessuna |
| `PKD-0614-00` | 614 | Beartic | diretta | nessuna |
| `PKD-0615-00` | 615 | Cryogonal | diretta | nessuna |
| `PKD-0616-00` | 616 | Shelmet | diretta | nessuna |
| `PKD-0617-00` | 617 | Accelgor | diretta | nessuna |
| `PKD-0618-00` | 618 | Stunfisk | diretta | nessuna |
| `PKD-0619-00` | 619 | Mienfoo | diretta | nessuna |
| `PKD-0620-00` | 620 | Mienshao | diretta | nessuna |
| `PKD-0621-00` | 621 | Druddigon | diretta | nessuna |
| `PKD-0622-00` | 622 | Golett | diretta | nessuna |
| `PKD-0623-00` | 623 | Golurk | diretta | nessuna |
| `PKD-0624-00` | 624 | Pawniard | diretta | nessuna |
| `PKD-0625-00` | 625 | Bisharp | diretta | nessuna |
| `PKD-0626-00` | 626 | Bouffalant | diretta | nessuna |
| `PKD-0627-00` | 627 | Rufflet | diretta | nessuna |
| `PKD-0628-00` | 628 | Braviary | diretta | nessuna |
| `PKD-0629-00` | 629 | Vullaby | diretta | nessuna |
| `PKD-0630-00` | 630 | Mandibuzz | diretta | nessuna |
| `PKD-0631-00` | 631 | Heatmor | diretta | nessuna |
| `PKD-0632-00` | 632 | Durant | diretta | nessuna |
| `PKD-0633-00` | 633 | Deino | diretta | nessuna |
| `PKD-0634-00` | 634 | Zweilous | diretta | nessuna |
| `PKD-0635-00` | 635 | Hydreigon | diretta | nessuna |
| `PKD-0636-00` | 636 | Larvesta | diretta | nessuna |
| `PKD-0637-00` | 637 | Volcarona | diretta | nessuna |
| `PKD-0638-00` | 638 | Cobalion | diretta | nessuna |
| `PKD-0639-00` | 639 | Terrakion | diretta | nessuna |
| `PKD-0640-00` | 640 | Virizion | diretta | nessuna |
| `PKD-0641-00` | 641 | Tornadus | diretta | nessuna |
| `PKD-0642-00` | 642 | Thundurus | diretta | nessuna |
| `PKD-0643-00` | 643 | Reshiram | diretta | nessuna |
| `PKD-0644-00` | 644 | Zekrom | diretta | nessuna |
| `PKD-0645-00` | 645 | Landorus | diretta | nessuna |
| `PKD-0646-00` | 646 | Kyurem | diretta | nessuna |
| `PKD-0647-00` | 647 | Keldeo | diretta | nessuna |
| `PKD-0648-00` | 648 | Meloetta | diretta | nessuna |
| `PKD-0649-00` | 649 | Genesect | diretta | nessuna |
| `PKD-0650-00` | 650 | Chespin | diretta | nessuna |
| `PKD-0651-00` | 651 | Quilladin | diretta | nessuna |
| `PKD-0652-00` | 652 | Chesnaught | diretta | nessuna |
| `PKD-0653-00` | 653 | Fennekin | diretta | nessuna |
| `PKD-0654-00` | 654 | Braixen | diretta | nessuna |
| `PKD-0655-00` | 655 | Delphox | diretta | nessuna |
| `PKD-0656-00` | 656 | Froakie | diretta | nessuna |
| `PKD-0657-00` | 657 | Frogadier | diretta | nessuna |
| `PKD-0658-00` | 658 | Greninja | diretta | nessuna |
| `PKD-0659-00` | 659 | Bunnelby | diretta | nessuna |
| `PKD-0660-00` | 660 | Diggersby | diretta | nessuna |
| `PKD-0661-00` | 661 | Fletchling | diretta | nessuna |
| `PKD-0662-00` | 662 | Fletchinder | diretta | nessuna |
| `PKD-0663-00` | 663 | Talonflame | diretta | nessuna |
| `PKD-0664-00` | 664 | Scatterbug | diretta | nessuna |
| `PKD-0665-00` | 665 | Spewpa | diretta | nessuna |
| `PKD-0666-00` | 666 | Vivillon | diretta | nessuna |
| `PKD-0667-00` | 667 | Litleo | diretta | nessuna |
| `PKD-0668-00` | 668 | Pyroar | diretta | nessuna |
| `PKD-0669-00` | 669 | Flabébé | diretta | nessuna |
| `PKD-0670-00` | 670 | Floette | diretta | nessuna |
| `PKD-0671-00` | 671 | Florges | diretta | nessuna |
| `PKD-0672-00` | 672 | Skiddo | diretta | nessuna |
| `PKD-0673-00` | 673 | Gogoat | diretta | nessuna |
| `PKD-0674-00` | 674 | Pancham | diretta | nessuna |
| `PKD-0675-00` | 675 | Pangoro | diretta | nessuna |
| `PKD-0676-00` | 676 | Furfrou | diretta | nessuna |
| `PKD-0677-00` | 677 | Espurr | diretta | nessuna |
| `PKD-0678-00` | 678 | Meowstic | diretta | nessuna |
| `PKD-0679-00` | 679 | Honedge | diretta | nessuna |
| `PKD-0680-00` | 680 | Doublade | diretta | nessuna |
| `PKD-0681-00` | 681 | Aegislash | diretta | nessuna |
| `PKD-0682-00` | 682 | Spritzee | diretta | nessuna |
| `PKD-0683-00` | 683 | Aromatisse | diretta | nessuna |
| `PKD-0684-00` | 684 | Swirlix | diretta | nessuna |
| `PKD-0685-00` | 685 | Slurpuff | diretta | nessuna |
| `PKD-0686-00` | 686 | Inkay | diretta | nessuna |
| `PKD-0687-00` | 687 | Malamar | diretta | nessuna |
| `PKD-0688-00` | 688 | Binacle | diretta | nessuna |
| `PKD-0689-00` | 689 | Barbaracle | diretta | nessuna |
| `PKD-0690-00` | 690 | Skrelp | diretta | nessuna |
| `PKD-0691-00` | 691 | Dragalge | diretta | nessuna |
| `PKD-0692-00` | 692 | Clauncher | diretta | nessuna |
| `PKD-0693-00` | 693 | Clawitzer | diretta | nessuna |
| `PKD-0694-00` | 694 | Helioptile | diretta | nessuna |
| `PKD-0695-00` | 695 | Heliolisk | diretta | nessuna |
| `PKD-0696-00` | 696 | Tyrunt | diretta | nessuna |
| `PKD-0697-00` | 697 | Tyrantrum | diretta | nessuna |
| `PKD-0698-00` | 698 | Amaura | diretta | nessuna |
| `PKD-0699-00` | 699 | Aurorus | diretta | nessuna |
| `PKD-0700-00` | 700 | Sylveon | diretta | nessuna |
| `PKD-0701-00` | 701 | Hawlucha | diretta | nessuna |
| `PKD-0702-00` | 702 | Dedenne | diretta | nessuna |
| `PKD-0703-00` | 703 | Carbink | diretta | nessuna |
| `PKD-0704-00` | 704 | Goomy | diretta | nessuna |
| `PKD-0705-00` | 705 | Sliggoo | diretta | nessuna |
| `PKD-0706-00` | 706 | Goodra | diretta | nessuna |
| `PKD-0707-00` | 707 | Klefki | diretta | nessuna |
| `PKD-0708-00` | 708 | Phantump | diretta | nessuna |
| `PKD-0709-00` | 709 | Trevenant | diretta | nessuna |
| `PKD-0710-00` | 710 | Pumpkaboo | diretta | nessuna |
| `PKD-0711-00` | 711 | Gourgeist | diretta | nessuna |
| `PKD-0712-00` | 712 | Bergmite | diretta | nessuna |
| `PKD-0713-00` | 713 | Avalugg | diretta | nessuna |
| `PKD-0714-00` | 714 | Noibat | diretta | nessuna |
| `PKD-0715-00` | 715 | Noivern | diretta | nessuna |
| `PKD-0716-00` | 716 | Xerneas | diretta | nessuna |
| `PKD-0717-00` | 717 | Yveltal | diretta | nessuna |
| `PKD-0718-00` | 718 | Zygarde | diretta | nessuna |
| `PKD-0719-00` | 719 | Diancie | diretta | nessuna |
| `PKD-0720-00` | 720 | Hoopa | diretta | nessuna |
| `PKD-0721-00` | 721 | Volcanion | diretta | nessuna |
| `PKD-0722-00` | 722 | Rowlet | diretta | nessuna |
| `PKD-0723-00` | 723 | Dartrix | diretta | nessuna |
| `PKD-0724-00` | 724 | Decidueye | diretta | nessuna |
| `PKD-0725-00` | 725 | Litten | diretta | nessuna |
| `PKD-0726-00` | 726 | Torracat | diretta | nessuna |
| `PKD-0727-00` | 727 | Incineroar | diretta | nessuna |
| `PKD-0728-00` | 728 | Popplio | diretta | nessuna |
| `PKD-0729-00` | 729 | Brionne | diretta | nessuna |
| `PKD-0730-00` | 730 | Primarina | diretta | nessuna |
| `PKD-0731-00` | 731 | Pikipek | diretta | nessuna |
| `PKD-0732-00` | 732 | Trumbeak | diretta | nessuna |
| `PKD-0733-00` | 733 | Toucannon | diretta | nessuna |
| `PKD-0734-00` | 734 | Yungoos | diretta | nessuna |
| `PKD-0735-00` | 735 | Gumshoos | diretta | nessuna |
| `PKD-0736-00` | 736 | Grubbin | diretta | nessuna |
| `PKD-0737-00` | 737 | Charjabug | diretta | nessuna |
| `PKD-0738-00` | 738 | Vikavolt | diretta | nessuna |
| `PKD-0739-00` | 739 | Crabrawler | diretta | nessuna |
| `PKD-0740-00` | 740 | Crabominable | diretta | nessuna |
| `PKD-0741-00` | 741 | Oricorio | diretta | nessuna |
| `PKD-0742-00` | 742 | Cutiefly | diretta | nessuna |
| `PKD-0743-00` | 743 | Ribombee | diretta | nessuna |
| `PKD-0744-00` | 744 | Rockruff | diretta | nessuna |
| `PKD-0745-00` | 745 | Lycanroc | diretta | nessuna |
| `PKD-0746-00` | 746 | Wishiwashi | diretta | nessuna |
| `PKD-0747-00` | 747 | Mareanie | diretta | nessuna |
| `PKD-0748-00` | 748 | Toxapex | diretta | nessuna |
| `PKD-0749-00` | 749 | Mudbray | diretta | nessuna |
| `PKD-0750-00` | 750 | Mudsdale | diretta | nessuna |
| `PKD-0751-00` | 751 | Dewpider | diretta | nessuna |
| `PKD-0752-00` | 752 | Araquanid | diretta | nessuna |
| `PKD-0753-00` | 753 | Fomantis | diretta | nessuna |
| `PKD-0754-00` | 754 | Lurantis | diretta | nessuna |
| `PKD-0755-00` | 755 | Morelull | diretta | nessuna |
| `PKD-0756-00` | 756 | Shiinotic | diretta | nessuna |
| `PKD-0757-00` | 757 | Salandit | diretta | nessuna |
| `PKD-0758-00` | 758 | Salazzle | diretta | nessuna |
| `PKD-0759-00` | 759 | Stufful | diretta | nessuna |
| `PKD-0760-00` | 760 | Bewear | diretta | nessuna |
| `PKD-0761-00` | 761 | Bounsweet | diretta | nessuna |
| `PKD-0762-00` | 762 | Steenee | diretta | nessuna |
| `PKD-0763-00` | 763 | Tsareena | diretta | nessuna |
| `PKD-0764-00` | 764 | Comfey | diretta | nessuna |
| `PKD-0765-00` | 765 | Oranguru | diretta | nessuna |
| `PKD-0766-00` | 766 | Passimian | diretta | nessuna |
| `PKD-0767-00` | 767 | Wimpod | diretta | nessuna |
| `PKD-0768-00` | 768 | Golisopod | diretta | nessuna |
| `PKD-0769-00` | 769 | Sandygast | diretta | nessuna |
| `PKD-0770-00` | 770 | Palossand | diretta | nessuna |
| `PKD-0771-00` | 771 | Pyukumuku | diretta | nessuna |
| `PKD-0772-00` | 772 | Tipo Zero | diretta | nessuna |
| `PKD-0773-00` | 773 | Silvally | diretta | nessuna |
| `PKD-0774-00` | 774 | Minior | diretta | nessuna |
| `PKD-0775-00` | 775 | Komala | diretta | nessuna |
| `PKD-0776-00` | 776 | Turtonator | diretta | nessuna |
| `PKD-0777-00` | 777 | Togedemaru | diretta | nessuna |
| `PKD-0778-00` | 778 | Mimikyu | diretta | nessuna |
| `PKD-0779-00` | 779 | Bruxish | diretta | nessuna |
| `PKD-0780-00` | 780 | Drampa | diretta | nessuna |
| `PKD-0781-00` | 781 | Dhelmise | diretta | nessuna |
| `PKD-0782-00` | 782 | Jangmo-o | diretta | nessuna |
| `PKD-0783-00` | 783 | Hakamo-o | diretta | nessuna |
| `PKD-0784-00` | 784 | Kommo-o | diretta | nessuna |
| `PKD-0785-00` | 785 | Tapu Koko | diretta | nessuna |
| `PKD-0786-00` | 786 | Tapu Lele | diretta | nessuna |
| `PKD-0787-00` | 787 | Tapu Bulu | diretta | nessuna |
| `PKD-0788-00` | 788 | Tapu Fini | diretta | nessuna |
| `PKD-0789-00` | 789 | Cosmog | diretta | nessuna |
| `PKD-0790-00` | 790 | Cosmoem | diretta | nessuna |
| `PKD-0791-00` | 791 | Solgaleo | diretta | nessuna |
| `PKD-0792-00` | 792 | Lunala | diretta | nessuna |
| `PKD-0793-00` | 793 | Nihilego | diretta | nessuna |
| `PKD-0794-00` | 794 | Buzzwole | diretta | nessuna |
| `PKD-0795-00` | 795 | Pheromosa | diretta | nessuna |
| `PKD-0796-00` | 796 | Xurkitree | diretta | nessuna |
| `PKD-0797-00` | 797 | Celesteela | diretta | nessuna |
| `PKD-0798-00` | 798 | Kartana | diretta | nessuna |
| `PKD-0799-00` | 799 | Guzzlord | diretta | nessuna |
| `PKD-0800-00` | 800 | Necrozma | diretta | nessuna |
| `PKD-0801-00` | 801 | Magearna | diretta | nessuna |
| `PKD-0802-00` | 802 | Marshadow | diretta | nessuna |
| `PKD-0803-00` | 803 | Poipole | diretta | nessuna |
| `PKD-0804-00` | 804 | Naganadel | diretta | nessuna |
| `PKD-0805-00` | 805 | Stakataka | diretta | nessuna |
| `PKD-0806-00` | 806 | Blacephalon | diretta | nessuna |
| `PKD-0807-00` | 807 | Zeraora | diretta | nessuna |
| `PKD-0808-00` | 808 | Meltan | diretta | nessuna |
| `PKD-0809-00` | 809 | Melmetal | diretta | nessuna |
| `PKD-0810-00` | 810 | Grookey | diretta | nessuna |
| `PKD-0811-00` | 811 | Thwackey | diretta | nessuna |
| `PKD-0812-00` | 812 | Rillaboom | diretta | nessuna |
| `PKD-0813-00` | 813 | Scorbunny | diretta | nessuna |
| `PKD-0814-00` | 814 | Raboot | diretta | nessuna |
| `PKD-0815-00` | 815 | Cinderace | diretta | nessuna |
| `PKD-0816-00` | 816 | Sobble | diretta | nessuna |
| `PKD-0817-00` | 817 | Drizzile | diretta | nessuna |
| `PKD-0818-00` | 818 | Inteleon | diretta | nessuna |
| `PKD-0819-00` | 819 | Skwovet | diretta | nessuna |
| `PKD-0820-00` | 820 | Greedent | diretta | nessuna |
| `PKD-0821-00` | 821 | Rookidee | diretta | nessuna |
| `PKD-0822-00` | 822 | Corvisquire | diretta | nessuna |
| `PKD-0823-00` | 823 | Corviknight | diretta | nessuna |
| `PKD-0824-00` | 824 | Blipbug | diretta | nessuna |
| `PKD-0825-00` | 825 | Dottler | diretta | nessuna |
| `PKD-0826-00` | 826 | Orbeetle | diretta | nessuna |
| `PKD-0827-00` | 827 | Nickit | diretta | nessuna |
| `PKD-0828-00` | 828 | Thievul | diretta | nessuna |
| `PKD-0829-00` | 829 | Gossifleur | diretta | nessuna |
| `PKD-0830-00` | 830 | Eldegoss | diretta | nessuna |
| `PKD-0831-00` | 831 | Wooloo | diretta | nessuna |
| `PKD-0832-00` | 832 | Dubwool | diretta | nessuna |
| `PKD-0833-00` | 833 | Chewtle | diretta | nessuna |
| `PKD-0834-00` | 834 | Drednaw | diretta | nessuna |
| `PKD-0835-00` | 835 | Yamper | diretta | nessuna |
| `PKD-0836-00` | 836 | Boltund | diretta | nessuna |
| `PKD-0837-00` | 837 | Rolycoly | diretta | nessuna |
| `PKD-0838-00` | 838 | Carkol | diretta | nessuna |
| `PKD-0839-00` | 839 | Coalossal | diretta | nessuna |
| `PKD-0840-00` | 840 | Applin | diretta | nessuna |
| `PKD-0841-00` | 841 | Flapple | diretta | nessuna |
| `PKD-0842-00` | 842 | Appletun | diretta | nessuna |
| `PKD-0843-00` | 843 | Silicobra | diretta | nessuna |
| `PKD-0844-00` | 844 | Sandaconda | diretta | nessuna |
| `PKD-0845-00` | 845 | Cramorant | diretta | nessuna |
| `PKD-0846-00` | 846 | Arrokuda | diretta | nessuna |
| `PKD-0847-00` | 847 | Barraskewda | diretta | nessuna |
| `PKD-0848-00` | 848 | Toxel | diretta | nessuna |
| `PKD-0849-00` | 849 | Toxtricity | diretta | nessuna |
| `PKD-0850-00` | 850 | Sizzlipede | diretta | nessuna |
| `PKD-0851-00` | 851 | Centiskorch | diretta | nessuna |
| `PKD-0852-00` | 852 | Clobbopus | diretta | nessuna |
| `PKD-0853-00` | 853 | Grapploct | diretta | nessuna |
| `PKD-0854-00` | 854 | Sinistea | diretta | nessuna |
| `PKD-0855-00` | 855 | Polteageist | diretta | nessuna |
| `PKD-0856-00` | 856 | Hatenna | diretta | nessuna |
| `PKD-0857-00` | 857 | Hattrem | diretta | nessuna |
| `PKD-0858-00` | 858 | Hatterene | diretta | nessuna |
| `PKD-0859-00` | 859 | Impidimp | diretta | nessuna |
| `PKD-0860-00` | 860 | Morgrem | diretta | nessuna |
| `PKD-0861-00` | 861 | Grimmsnarl | diretta | nessuna |
| `PKD-0862-00` | 862 | Obstagoon | diretta | nessuna |
| `PKD-0863-00` | 863 | Perrserker | diretta | nessuna |
| `PKD-0864-00` | 864 | Cursola | diretta | nessuna |
| `PKD-0865-00` | 865 | Sirfetch’d | diretta | nessuna |
| `PKD-0866-00` | 866 | Mr. Rime | diretta | nessuna |
| `PKD-0867-00` | 867 | Runerigus | diretta | nessuna |
| `PKD-0868-00` | 868 | Milcery | diretta | nessuna |
| `PKD-0869-00` | 869 | Alcremie | diretta | nessuna |
| `PKD-0870-00` | 870 | Falinks | diretta | nessuna |
| `PKD-0871-00` | 871 | Pincurchin | diretta | nessuna |
| `PKD-0872-00` | 872 | Snom | diretta | nessuna |
| `PKD-0873-00` | 873 | Frosmoth | diretta | nessuna |
| `PKD-0874-00` | 874 | Stonjourner | diretta | nessuna |
| `PKD-0875-00` | 875 | Eiscue | diretta | nessuna |
| `PKD-0876-00` | 876 | Indeedee | diretta | nessuna |
| `PKD-0877-00` | 877 | Morpeko | diretta | nessuna |
| `PKD-0878-00` | 878 | Cufant | diretta | nessuna |
| `PKD-0879-00` | 879 | Copperajah | diretta | nessuna |
| `PKD-0880-00` | 880 | Dracozolt | diretta | nessuna |
| `PKD-0881-00` | 881 | Arctozolt | diretta | nessuna |
| `PKD-0882-00` | 882 | Dracovish | diretta | nessuna |
| `PKD-0883-00` | 883 | Arctovish | diretta | nessuna |
| `PKD-0884-00` | 884 | Duraludon | diretta | nessuna |
| `PKD-0885-00` | 885 | Dreepy | diretta | nessuna |
| `PKD-0886-00` | 886 | Drakloak | diretta | nessuna |
| `PKD-0887-00` | 887 | Dragapult | diretta | nessuna |
| `PKD-0888-00` | 888 | Zacian | diretta | nessuna |
| `PKD-0889-00` | 889 | Zamazenta | diretta | nessuna |
| `PKD-0890-00` | 890 | Eternatus | diretta | nessuna |
| `PKD-0891-00` | 891 | Kubfu | diretta | nessuna |
| `PKD-0892-00` | 892 | Urshifu | diretta | nessuna |
| `PKD-0893-00` | 893 | Zarude | diretta | nessuna |
| `PKD-0894-00` | 894 | Regieleki | diretta | nessuna |
| `PKD-0895-00` | 895 | Regidrago | diretta | nessuna |
| `PKD-0896-00` | 896 | Glastrier | diretta | nessuna |
| `PKD-0897-00` | 897 | Spectrier | diretta | nessuna |
| `PKD-0898-00` | 898 | Calyrex | diretta | nessuna |
| `PKD-0899-00` | 899 | Wyrdeer | diretta | nessuna |
| `PKD-0900-00` | 900 | Kleavor | diretta | nessuna |
| `PKD-0901-00` | 901 | Ursaluna | diretta | nessuna |
| `PKD-0902-00` | 902 | Basculegion | diretta | nessuna |
| `PKD-0903-00` | 903 | Sneasler | diretta | nessuna |
| `PKD-0904-00` | 904 | Overqwil | diretta | nessuna |
| `PKD-0905-00` | 905 | Enamorus | diretta | nessuna |
| `PKD-0906-00` | 906 | Sprigatito | diretta | nessuna |
| `PKD-0907-00` | 907 | Floragato | diretta | nessuna |
| `PKD-0908-00` | 908 | Meowscarada | diretta | nessuna |
| `PKD-0909-00` | 909 | Fuecoco | diretta | nessuna |
| `PKD-0910-00` | 910 | Crocalor | diretta | nessuna |
| `PKD-0911-00` | 911 | Skeledirge | diretta | nessuna |
| `PKD-0912-00` | 912 | Quaxly | diretta | nessuna |
| `PKD-0913-00` | 913 | Quaxwell | diretta | nessuna |
| `PKD-0914-00` | 914 | Quaquaval | diretta | nessuna |
| `PKD-0915-00` | 915 | Lechonk | diretta | nessuna |
| `PKD-0916-00` | 916 | Oinkologne | diretta | nessuna |
| `PKD-0917-00` | 917 | Tarountula | diretta | nessuna |
| `PKD-0918-00` | 918 | Spidops | diretta | nessuna |
| `PKD-0919-00` | 919 | Nymble | diretta | nessuna |
| `PKD-0920-00` | 920 | Lokix | diretta | nessuna |
| `PKD-0921-00` | 921 | Pawmi | diretta | nessuna |
| `PKD-0922-00` | 922 | Pawmo | diretta | nessuna |
| `PKD-0923-00` | 923 | Pawmot | diretta | nessuna |
| `PKD-0924-00` | 924 | Tandemaus | diretta | nessuna |
| `PKD-0925-00` | 925 | Maushold | diretta | nessuna |
| `PKD-0926-00` | 926 | Fidough | diretta | nessuna |
| `PKD-0927-00` | 927 | Dachsbun | diretta | nessuna |
| `PKD-0928-00` | 928 | Smoliv | diretta | nessuna |
| `PKD-0929-00` | 929 | Dolliv | diretta | nessuna |
| `PKD-0930-00` | 930 | Arboliva | diretta | nessuna |
| `PKD-0931-00` | 931 | Squawkabilly | diretta | nessuna |
| `PKD-0932-00` | 932 | Nacli | diretta | nessuna |
| `PKD-0933-00` | 933 | Naclstack | diretta | nessuna |
| `PKD-0934-00` | 934 | Garganacl | diretta | nessuna |
| `PKD-0935-00` | 935 | Charcadet | diretta | nessuna |
| `PKD-0936-00` | 936 | Armarouge | diretta | nessuna |
| `PKD-0937-00` | 937 | Ceruledge | diretta | nessuna |
| `PKD-0938-00` | 938 | Tadbulb | diretta | nessuna |
| `PKD-0939-00` | 939 | Bellibolt | diretta | nessuna |
| `PKD-0940-00` | 940 | Wattrel | diretta | nessuna |
| `PKD-0941-00` | 941 | Kilowattrel | diretta | nessuna |
| `PKD-0942-00` | 942 | Maschiff | diretta | nessuna |
| `PKD-0943-00` | 943 | Mabosstiff | diretta | nessuna |
| `PKD-0944-00` | 944 | Shroodle | diretta | nessuna |
| `PKD-0945-00` | 945 | Grafaiai | diretta | nessuna |
| `PKD-0946-00` | 946 | Bramblin | diretta | nessuna |
| `PKD-0947-00` | 947 | Brambleghast | diretta | nessuna |
| `PKD-0948-00` | 948 | Toedscool | diretta | nessuna |
| `PKD-0949-00` | 949 | Toedscruel | diretta | nessuna |
| `PKD-0950-00` | 950 | Klawf | diretta | nessuna |
| `PKD-0951-00` | 951 | Capsakid | diretta | nessuna |
| `PKD-0952-00` | 952 | Scovillain | diretta | nessuna |
| `PKD-0953-00` | 953 | Rellor | diretta | nessuna |
| `PKD-0954-00` | 954 | Rabsca | diretta | nessuna |
| `PKD-0955-00` | 955 | Flittle | diretta | nessuna |
| `PKD-0956-00` | 956 | Espathra | diretta | nessuna |
| `PKD-0957-00` | 957 | Tinkatink | diretta | nessuna |
| `PKD-0958-00` | 958 | Tinkatuff | diretta | nessuna |
| `PKD-0959-00` | 959 | Tinkaton | diretta | nessuna |
| `PKD-0960-00` | 960 | Wiglett | diretta | nessuna |
| `PKD-0961-00` | 961 | Wugtrio | diretta | nessuna |
| `PKD-0962-00` | 962 | Bombirdier | diretta | nessuna |
| `PKD-0963-00` | 963 | Finizen | diretta | nessuna |
| `PKD-0964-00` | 964 | Palafin | diretta | nessuna |
| `PKD-0965-00` | 965 | Varoom | diretta | nessuna |
| `PKD-0966-00` | 966 | Revavroom | diretta | nessuna |
| `PKD-0967-00` | 967 | Cyclizar | diretta | nessuna |
| `PKD-0968-00` | 968 | Orthworm | diretta | nessuna |
| `PKD-0969-00` | 969 | Glimmet | diretta | nessuna |
| `PKD-0970-00` | 970 | Glimmora | diretta | nessuna |
| `PKD-0971-00` | 971 | Greavard | diretta | nessuna |
| `PKD-0972-00` | 972 | Houndstone | diretta | nessuna |
| `PKD-0973-00` | 973 | Flamigo | diretta | nessuna |
| `PKD-0974-00` | 974 | Cetoddle | diretta | nessuna |
| `PKD-0975-00` | 975 | Cetitan | diretta | nessuna |
| `PKD-0976-00` | 976 | Veluza | diretta | nessuna |
| `PKD-0977-00` | 977 | Dondozo | diretta | nessuna |
| `PKD-0978-00` | 978 | Tatsugiri | diretta | nessuna |
| `PKD-0979-00` | 979 | Annihilape | diretta | nessuna |
| `PKD-0980-00` | 980 | Clodsire | diretta | nessuna |
| `PKD-0981-00` | 981 | Farigiraf | diretta | nessuna |
| `PKD-0982-00` | 982 | Dudunsparce | diretta | nessuna |
| `PKD-0983-00` | 983 | Kingambit | diretta | nessuna |
| `PKD-0984-00` | 984 | Grandizanne | diretta | nessuna |
| `PKD-0985-00` | 985 | Codaurlante | diretta | nessuna |
| `PKD-0986-00` | 986 | Fungofurioso | diretta | nessuna |
| `PKD-0987-00` | 987 | Crinealato | diretta | nessuna |
| `PKD-0988-00` | 988 | Alirasenti | diretta | nessuna |
| `PKD-0989-00` | 989 | Peldisabbia | diretta | nessuna |
| `PKD-0990-00` | 990 | Solcoferreo | diretta | nessuna |
| `PKD-0991-00` | 991 | Saccoferreo | diretta | nessuna |
| `PKD-0992-00` | 992 | Manoferrea | diretta | nessuna |
| `PKD-0993-00` | 993 | Colloferreo | diretta | nessuna |
| `PKD-0994-00` | 994 | Falenaferrea | diretta | nessuna |
| `PKD-0995-00` | 995 | Spineferree | diretta | nessuna |
| `PKD-0996-00` | 996 | Frigibax | diretta | nessuna |
| `PKD-0997-00` | 997 | Arctibax | diretta | nessuna |
| `PKD-0998-00` | 998 | Baxcalibur | diretta | nessuna |
| `PKD-0999-00` | 999 | Gimmighoul | diretta | nessuna |
| `PKD-1000-00` | 1000 | Gholdengo | diretta | nessuna |
| `PKD-1001-00` | 1001 | Wo-Chien | diretta | nessuna |
| `PKD-1002-00` | 1002 | Chien-Pao | diretta | nessuna |
| `PKD-1003-00` | 1003 | Ting-Lu | diretta | nessuna |
| `PKD-1004-00` | 1004 | Chi-Yu | diretta | nessuna |
| `PKD-1005-00` | 1005 | Lunaruggente | diretta | nessuna |
| `PKD-1006-00` | 1006 | Eroeferreo | diretta | nessuna |
| `PKD-1007-00` | 1007 | Koraidon | diretta | nessuna |
| `PKD-1008-00` | 1008 | Miraidon | diretta | nessuna |
| `PKD-1009-00` | 1009 | Acquecrespe | diretta | nessuna |
| `PKD-1010-00` | 1010 | Fogliaferrea | diretta | nessuna |
| `PKD-1011-00` | 1011 | Dipplin | diretta | nessuna |
| `PKD-1012-00` | 1012 | Poltchageist | diretta | nessuna |
| `PKD-1013-00` | 1013 | Sinistcha | diretta | nessuna |
| `PKD-1014-00` | 1014 | Okidogi | diretta | nessuna |
| `PKD-1015-00` | 1015 | Munkidori | diretta | nessuna |
| `PKD-1016-00` | 1016 | Fezandipiti | diretta | nessuna |
| `PKD-1017-00` | 1017 | Ogerpon | diretta | nessuna |
| `PKD-1018-00` | 1018 | Archaludon | diretta | nessuna |
| `PKD-1019-00` | 1019 | Hydrapple | diretta | nessuna |
| `PKD-1020-00` | 1020 | Vampeaguzze | diretta | nessuna |
| `PKD-1021-00` | 1021 | Furiatonante | diretta | nessuna |
| `PKD-1022-00` | 1022 | Massoferreo | diretta | nessuna |
| `PKD-1023-00` | 1023 | Capoferreo | diretta | nessuna |
| `PKD-1024-00` | 1024 | Terapagos | diretta | nessuna |
| `PKD-1025-00` | 1025 | Pecharunt | diretta | nessuna |

## Voci da evento

L'asse degli eventi nasce da tre fonti e non da una, e la distinzione va letta prima dei numeri perché fino al 2026-09-04 le fonti erano due e la terza mancava del tutto. La prima è la tabella delle carte meraviglia di terza generazione, che vive nel codice del verificatore; la seconda sono i file binari della base dei doni segreti, che coprono la prima e la seconda generazione con le loro tabelle di incontro e poi dalla quarta alla nona con i doni veri e propri; la terza sono le tabelle degli incontri del verificatore, dove stanno le distribuzioni in cui il dono era un oggetto, le periferiche, i giochi da console fissa e i doni interni condizionati. Le prime due erano cieche sulla terza, ed è un difetto di copertura e non di lettura: non produceva alcun errore, e la lista sembrava completa mentre mancavano 422 voci. La colonna della classe dice da quale delle tre viene ciascuna voce, e i codici delle voci della terza cominciano con `EVT-T-` invece che con la generazione, perché una sola numerazione le attraversa tutte.

La ripartizione per classe è la seguente: dono segreto 2615, periferica 210, spinoff 182, carta meraviglia 173, tabella di incontro 168, oggetto-distribuito 15, condizionato 13, disco-bonus 2.

Una voce da evento è un collezionabile distinto anche quando la sua specie è già coperta altrove, e la ragione è che porta un nome di allenatore, un identificativo e una data che nessun incontro selvatico produce: chi possiede il secondo non possiede il primo. La colonna della resa dice a che punto siamo su quella voce, e tiene distinte tre condizioni che non vanno confuse, cioè una voce che il progetto sa produrre e ha fatto verificare, una che sa soltanto leggere, e una la cui struttura è alla portata di codice che già esiste.

Le voci enumerate sono 3378, di cui 3095 sotto scadenza, e queste ultime portano 433 specie distinte. Sono il solo insieme di questa lista che il 26 febbraio 2027 chiude davvero: le voci di specie e di forma sono tutte raggiungibili per via diretta, mentre un esemplare da distribuzione di una generazione anteriore all'ottava non ha altra strada che la banca.

L'ordine della tabella non è quello della fonte, ed è una scelta che va dichiarata perché cambia che cosa si legge per primo. La fonte raggruppa le voci per evento, cioè nell'ordine in cui le distribuzioni avvennero; la decisione di ambito è invece la collezione completa in due tempi, con prima una voce per ciascuna specie distinta e poi i gemelli. La colonna che dice se una voce sia la prima della propria specie porta dunque in testa le 433 voci del primo tempo, e lascia in coda le 2662 del secondo; dentro ciascuno dei due blocchi l'ordine per evento è conservato, perché è l'informazione utile a chi produce. La prima voce di una specie è scelta nell'ordine della fonte e non per merito: dove più voci portano la medesima specie, la marcatura non dice quale sia la più desiderabile ma soltanto quale basti a coprire la specie.

| Codice | Gen | Classe | Dex | Forma | Provenienza | Sotto scadenza | Primo della specie | Resa |
|---|---|---|---|---|---|---|---|---|
| `EVT-3-0000` | 3 | carta meraviglia | 151 | 0 | Mew | sì | sì | producibile e verificata |
| `EVT-3-0001` | 3 | carta meraviglia | 385 | 0 | WISHMKR | sì | sì | producibile e verificata |
| `EVT-3-0003` | 3 | carta meraviglia | 263 | 0 | Berry Fix Ruby | sì | sì | producibile e verificata |
| `EVT-3-0008` | 3 | carta meraviglia | 25 | 0 | ANA Pikachu | sì | sì | producibile e verificata |
| `EVT-3-0009` | 3 | carta meraviglia | 52 | 0 | PokéPark Meowth | sì | sì | producibile e verificata |
| `EVT-3-0015` | 3 | carta meraviglia | 375 | 0 | Festa Metang | sì | sì | producibile e verificata |
| `EVT-3-0016` | 3 | carta meraviglia | 202 | 0 | Sunday Wobbuffet | sì | sì | producibile e verificata |
| `EVT-3-0017` | 3 | carta meraviglia | 377 | 0 | Regirock | sì | sì | producibile e verificata |
| `EVT-3-0018` | 3 | carta meraviglia | 378 | 0 | Regice | sì | sì | producibile e verificata |
| `EVT-3-0019` | 3 | carta meraviglia | 379 | 0 | Registeel | sì | sì | producibile e verificata |
| `EVT-3-0021` | 3 | carta meraviglia | 251 | 0 | PokéPark Celebi | sì | sì | producibile e verificata |
| `EVT-3-0028` | 3 | carta meraviglia | 6 | 0 | Charizard | sì | sì | producibile e verificata |
| `EVT-3-0030` | 3 | carta meraviglia | 144 | 0 | Articuno | sì | sì | producibile e verificata |
| `EVT-3-0031` | 3 | carta meraviglia | 243 | 0 | Raikou | sì | sì | producibile e verificata |
| `EVT-3-0032` | 3 | carta meraviglia | 244 | 0 | Entei | sì | sì | producibile e verificata |
| `EVT-3-0033` | 3 | carta meraviglia | 245 | 0 | Suicune | sì | sì | producibile e verificata |
| `EVT-3-0034` | 3 | carta meraviglia | 249 | 0 | Lugia | sì | sì | producibile e verificata |
| `EVT-3-0035` | 3 | carta meraviglia | 250 | 0 | Ho-Oh | sì | sì | producibile e verificata |
| `EVT-3-0036` | 3 | carta meraviglia | 380 | 0 | Latias | sì | sì | producibile e verificata |
| `EVT-3-0037` | 3 | carta meraviglia | 381 | 0 | Latios | sì | sì | producibile e verificata |
| `EVT-3-0080` | 3 | carta meraviglia | 386 | 0 | Deoxys | sì | sì | producibile e verificata |
| `EVT-3-0082` | 3 | carta meraviglia | 1 | 0 | Bulbasaur | sì | sì | producibile e verificata |
| `EVT-3-0084` | 3 | carta meraviglia | 9 | 0 | Blastoise | sì | sì | producibile e verificata |
| `EVT-3-0086` | 3 | carta meraviglia | 65 | 0 | Alakazam | sì | sì | producibile e verificata |
| `EVT-3-0088` | 3 | carta meraviglia | 145 | 0 | Zapdos | sì | sì | producibile e verificata |
| `EVT-3-0089` | 3 | carta meraviglia | 146 | 0 | Moltres | sì | sì | producibile e verificata |
| `EVT-3-0090` | 3 | carta meraviglia | 149 | 0 | Dragonite | sì | sì | producibile e verificata |
| `EVT-3-0091` | 3 | carta meraviglia | 157 | 0 | Typhlosion | sì | sì | producibile e verificata |
| `EVT-3-0092` | 3 | carta meraviglia | 196 | 0 | Espeon | sì | sì | producibile e verificata |
| `EVT-3-0093` | 3 | carta meraviglia | 197 | 0 | Umbreon | sì | sì | producibile e verificata |
| `EVT-3-0097` | 3 | carta meraviglia | 248 | 0 | Tyranitar | sì | sì | producibile e verificata |
| `EVT-3-0098` | 3 | carta meraviglia | 257 | 0 | Blaziken | sì | sì | producibile e verificata |
| `EVT-3-0099` | 3 | carta meraviglia | 359 | 0 | Absol | sì | sì | producibile e verificata |
| `EVT-3-0123` | 3 | carta meraviglia | 172 | 0 | Pichu with Teeter Dance | sì | sì | producibile e verificata |
| `EVT-3-0127` | 3 | carta meraviglia | 280 | 0 | Ralts with Charm | sì | sì | producibile e verificata |
| `EVT-3-0131` | 3 | carta meraviglia | 371 | 0 | Bagon with Iron Defense | sì | sì | producibile e verificata |
| `EVT-3-0133` | 3 | carta meraviglia | 43 | 0 | Oddish with Leech Seed | sì | sì | producibile e verificata |
| `EVT-3-0135` | 3 | carta meraviglia | 60 | 0 | Poliwag with Sweet Kiss | sì | sì | producibile e verificata |
| `EVT-3-0136` | 3 | carta meraviglia | 69 | 0 | Bellsprout with Teeter Dance | sì | sì | producibile e verificata |
| `EVT-3-0137` | 3 | carta meraviglia | 83 | 0 | Farfetch'd with Wish & Yawn | sì | sì | producibile e verificata |
| `EVT-3-0138` | 3 | carta meraviglia | 96 | 0 | Drowzee with Wish & Belly Drum | sì | sì | producibile e verificata |
| `EVT-3-0139` | 3 | carta meraviglia | 102 | 0 | Exeggcute with Wish & Sweet Scent | sì | sì | producibile e verificata |
| `EVT-3-0140` | 3 | carta meraviglia | 108 | 0 | Lickitung with Wish & Heal Bell | sì | sì | producibile e verificata |
| `EVT-3-0141` | 3 | carta meraviglia | 113 | 0 | Chansey with Wish & Sweet Scent | sì | sì | producibile e verificata |
| `EVT-3-0142` | 3 | carta meraviglia | 115 | 0 | Kangaskhan with Wish & Yawn | sì | sì | producibile e verificata |
| `EVT-3-0143` | 3 | carta meraviglia | 54 | 0 | Psyduck with Mud Sport | sì | sì | producibile e verificata |
| `EVT-3-0145` | 3 | carta meraviglia | 174 | 0 | Igglybuff with Tickle | sì | sì | producibile e verificata |
| `EVT-3-0146` | 3 | carta meraviglia | 222 | 0 | Corsola with Mud Sport | sì | sì | producibile e verificata |
| `EVT-3-0147` | 3 | carta meraviglia | 276 | 0 | Taillow with Feather Dance | sì | sì | producibile e verificata |
| `EVT-3-0148` | 3 | carta meraviglia | 283 | 0 | Surskit with Mud Sport | sì | sì | producibile e verificata |
| `EVT-3-0149` | 3 | carta meraviglia | 293 | 0 | Whismur with Teeter Dance | sì | sì | producibile e verificata |
| `EVT-3-0150` | 3 | carta meraviglia | 300 | 0 | Skitty with Rollout | sì | sì | producibile e verificata |
| `EVT-3-0151` | 3 | carta meraviglia | 311 | 0 | Plusle with Water Sport | sì | sì | producibile e verificata |
| `EVT-3-0152` | 3 | carta meraviglia | 312 | 0 | Minun with Mud Sport | sì | sì | producibile e verificata |
| `EVT-3-0153` | 3 | carta meraviglia | 325 | 0 | Spoink with Uproar | sì | sì | producibile e verificata |
| `EVT-3-0154` | 3 | carta meraviglia | 327 | 0 | Spinda with Sing | sì | sì | producibile e verificata |
| `EVT-3-0155` | 3 | carta meraviglia | 331 | 0 | Cacnea with Encore | sì | sì | producibile e verificata |
| `EVT-3-0156` | 3 | carta meraviglia | 341 | 0 | Corphish with Water Sport | sì | sì | producibile e verificata |
| `EVT-3-0157` | 3 | carta meraviglia | 360 | 0 | Wynaut with Tickle | sì | sì | producibile e verificata |
| `EVT-4-0001` | 4 | dono segreto | 490 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0005` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0012` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0013` | 4 | dono segreto | 486 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0015` | 4 | dono segreto | 493 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0021` | 4 | dono segreto | 447 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0026` | 4 | dono segreto | 133 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0038` | 4 | dono segreto | 169 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0040` | 4 | dono segreto | 466 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0041` | 4 | dono segreto | 467 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0042` | 4 | dono segreto | 448 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0043` | 4 | dono segreto | 350 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0046` | 4 | dono segreto | 461 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0051` | 4 | dono segreto | 485 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0124` | 4 | dono segreto | 289 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0125` | 4 | dono segreto | 224 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0126` | 4 | dono segreto | 330 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0128` | 4 | dono segreto | 376 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0129` | 4 | dono segreto | 441 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0130` | 4 | dono segreto | 125 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0131` | 4 | dono segreto | 126 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0133` | 4 | dono segreto | 357 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0135` | 4 | dono segreto | 340 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0148` | 4 | dono segreto | 4 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0154` | 4 | dono segreto | 373 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0172` | 4 | dono segreto | 390 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0183` | 4 | dono segreto | 212 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0199` | 4 | dono segreto | 384 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0202` | 4 | dono segreto | 465 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0204` | 4 | dono segreto | 59 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0206` | 4 | dono segreto | 446 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-4-0207` | 4 | dono segreto | 349 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | sì | letta, non ancora producibile |
| `EVT-5-0000` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0001` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0004` | 5 | dono segreto | 610 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0005` | 5 | dono segreto | 511 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0006` | 5 | dono segreto | 519 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0007` | 5 | dono segreto | 571 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0009` | 5 | dono segreto | 494 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0010` | 5 | dono segreto | 644 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0012` | 5 | dono segreto | 643 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0014` | 5 | dono segreto | 560 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0015` | 5 | dono segreto | 150 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0016` | 5 | dono segreto | 246 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0017` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0020` | 5 | dono segreto | 649 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0023` | 5 | dono segreto | 648 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0024` | 5 | dono segreto | 91 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0025` | 5 | dono segreto | 272 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0029` | 5 | dono segreto | 483 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0031` | 5 | dono segreto | 484 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0033` | 5 | dono segreto | 487 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0035` | 5 | dono segreto | 235 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0104` | 5 | dono segreto | 613 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0106` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0108` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0110` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0112` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0113` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0317` | 5 | dono segreto | 559 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0322` | 5 | dono segreto | 635 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0323` | 5 | dono segreto | 623 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0334` | 5 | dono segreto | 495 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0342` | 5 | dono segreto | 642 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0343` | 5 | dono segreto | 641 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0346` | 5 | dono segreto | 633 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0347` | 5 | dono segreto | 621 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0348` | 5 | dono segreto | 116 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0349` | 5 | dono segreto | 333 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0350` | 5 | dono segreto | 328 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0372` | 5 | dono segreto | 254 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0373` | 5 | dono segreto | 260 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0376` | 5 | dono segreto | 365 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0377` | 5 | dono segreto | 282 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0380` | 5 | dono segreto | 383 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0381` | 5 | dono segreto | 382 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0449` | 5 | dono segreto | 393 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0452` | 5 | dono segreto | 7 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0455` | 5 | dono segreto | 142 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0456` | 5 | dono segreto | 347 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0457` | 5 | dono segreto | 566 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0458` | 5 | dono segreto | 408 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0459` | 5 | dono segreto | 140 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0460` | 5 | dono segreto | 345 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0461` | 5 | dono segreto | 138 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0462` | 5 | dono segreto | 410 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0463` | 5 | dono segreto | 564 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0465` | 5 | dono segreto | 38 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0466` | 5 | dono segreto | 609 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0467` | 5 | dono segreto | 547 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0470` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0518` | 5 | dono segreto | 129 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0523` | 5 | dono segreto | 395 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0524` | 5 | dono segreto | 497 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0526` | 5 | dono segreto | 389 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0527` | 5 | dono segreto | 392 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0528` | 5 | dono segreto | 500 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0529` | 5 | dono segreto | 503 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0540` | 5 | dono segreto | 612 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0541` | 5 | dono segreto | 637 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0542` | 5 | dono segreto | 18 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0543` | 5 | dono segreto | 442 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0555` | 5 | dono segreto | 479 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0570` | 5 | dono segreto | 302 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0571` | 5 | dono segreto | 186 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0572` | 5 | dono segreto | 230 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0674` | 5 | dono segreto | 237 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0675` | 5 | dono segreto | 488 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-5-0676` | 5 | dono segreto | 510 | 0 | Bianco, Nero e i loro seguiti | sì | sì | letta, non ancora producibile |
| `EVT-6-0001` | 6 | dono segreto | 700 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0002` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0008` | 6 | dono segreto | 721 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0009` | 6 | dono segreto | 473 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0010` | 6 | dono segreto | 681 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0011` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0012` | 6 | dono segreto | 417 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0014` | 6 | dono segreto | 319 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0017` | 6 | dono segreto | 683 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0018` | 6 | dono segreto | 626 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0019` | 6 | dono segreto | 687 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0020` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0043` | 6 | dono segreto | 716 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0045` | 6 | dono segreto | 717 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0047` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0049` | 6 | dono segreto | 68 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0056` | 6 | dono segreto | 696 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0057` | 6 | dono segreto | 698 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0059` | 6 | dono segreto | 225 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0061` | 6 | dono segreto | 241 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0063` | 6 | dono segreto | 555 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0186` | 6 | dono segreto | 136 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0187` | 6 | dono segreto | 471 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0188` | 6 | dono segreto | 135 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0189` | 6 | dono segreto | 470 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0193` | 6 | dono segreto | 134 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0195` | 6 | dono segreto | 686 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0207` | 6 | dono segreto | 130 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0212` | 6 | dono segreto | 303 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0221` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0241` | 6 | dono segreto | 264 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0263` | 6 | dono segreto | 152 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0264` | 6 | dono segreto | 155 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0265` | 6 | dono segreto | 158 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0273` | 6 | dono segreto | 3 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0278` | 6 | dono segreto | 658 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0283` | 6 | dono segreto | 645 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0289` | 6 | dono segreto | 514 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0290` | 6 | dono segreto | 31 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0291` | 6 | dono segreto | 323 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0295` | 6 | dono segreto | 668 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0321` | 6 | dono segreto | 179 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0347` | 6 | dono segreto | 362 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0349` | 6 | dono segreto | 208 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0352` | 6 | dono segreto | 160 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0353` | 6 | dono segreto | 154 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0424` | 6 | dono segreto | 214 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0425` | 6 | dono segreto | 127 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0428` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0437` | 6 | dono segreto | 255 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0440` | 6 | dono segreto | 374 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0527` | 6 | dono segreto | 656 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0535` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0537` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0617` | 6 | dono segreto | 646 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0620` | 6 | dono segreto | 653 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0627` | 6 | dono segreto | 674 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0644` | 6 | dono segreto | 334 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0652` | 6 | dono segreto | 80 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0721` | 6 | dono segreto | 310 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0727` | 6 | dono segreto | 229 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-6-0729` | 6 | dono segreto | 306 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | sì | letta, non ancora producibile |
| `EVT-7-0001` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0002` | 7 | dono segreto | 773 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0004` | 7 | dono segreto | 802 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0008` | 7 | dono segreto | 745 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0009` | 7 | dono segreto | 758 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0013` | 7 | dono segreto | 103 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0062` | 7 | dono segreto | 553 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0063` | 7 | dono segreto | 803 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0064` | 7 | dono segreto | 807 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0066` | 7 | dono segreto | 423 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0068` | 7 | dono segreto | 791 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0069` | 7 | dono segreto | 792 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0071` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0073` | 7 | dono segreto | 778 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0079` | 7 | dono segreto | 786 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0080` | 7 | dono segreto | 787 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0081` | 7 | dono segreto | 788 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0083` | 7 | dono segreto | 517 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0290` | 7 | dono segreto | 764 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0293` | 7 | dono segreto | 37 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0296` | 7 | dono segreto | 780 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0297` | 7 | dono segreto | 704 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0298` | 7 | dono segreto | 747 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0299` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0300` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0301` | 7 | dono segreto | 776 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0302` | 7 | dono segreto | 760 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0323` | 7 | dono segreto | 762 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0332` | 7 | dono segreto | 337 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0333` | 7 | dono segreto | 338 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0344` | 7 | dono segreto | 132 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0360` | 7 | dono segreto | 34 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0362` | 7 | dono segreto | 262 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0363` | 7 | dono segreto | 430 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0364` | 7 | dono segreto | 563 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0365` | 7 | dono segreto | 620 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0367` | 7 | dono segreto | 143 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0373` | 7 | dono segreto | 55 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0381` | 7 | dono segreto | 800 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0395` | 7 | dono segreto | 27 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0396` | 7 | dono segreto | 50 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0397` | 7 | dono segreto | 88 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0539` | 7 | dono segreto | 801 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0541` | 7 | dono segreto | 724 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0542` | 7 | dono segreto | 727 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-7-0545` | 7 | dono segreto | 730 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | sì | letta, non ancora producibile |
| `EVT-T-0021` | 3 | spinoff | 296 | 0 | Colosseum, ombra: Makuhita: Miror B.Peon Trudly @ Phenac City | sì | sì | censita, non ancora producibile |
| `EVT-T-0022` | 3 | spinoff | 153 | 0 | Colosseum, ombra: Bayleef: Cipher Peon Verde @ Phenac City | sì | sì | censita, non ancora producibile |
| `EVT-T-0026` | 3 | spinoff | 156 | 0 | Colosseum, ombra: Quilava: Cipher Peon Rosso @ Phenac City | sì | sì | censita, non ancora producibile |
| `EVT-T-0030` | 3 | spinoff | 159 | 0 | Colosseum, ombra: Croconaw: Cipher Peon Bluno @ Phenac City | sì | sì | censita, non ancora producibile |
| `EVT-T-0034` | 3 | spinoff | 164 | 0 | Colosseum, ombra: Noctowl: Rider Nover @ Pyrite Town | sì | sì | censita, non ancora producibile |
| `EVT-T-0035` | 3 | spinoff | 180 | 0 | Colosseum, ombra: Flaaffy: St.Performer Diogo @ Pyrite Town | sì | sì | censita, non ancora producibile |
| `EVT-T-0036` | 3 | spinoff | 188 | 0 | Colosseum, ombra: Skiploom: Rider Leba @ Pyrite Town | sì | sì | censita, non ancora producibile |
| `EVT-T-0037` | 3 | spinoff | 195 | 0 | Colosseum, ombra: Quagsire: Bandana Guy Divel @ Pyrite Town | sì | sì | censita, non ancora producibile |
| `EVT-T-0038` | 3 | spinoff | 200 | 0 | Colosseum, ombra: Misdreavus: Rider Vant @ Pyrite Town | sì | sì | censita, non ancora producibile |
| `EVT-T-0039` | 3 | spinoff | 193 | 0 | Colosseum, ombra: Yanma: Cipher Peon Nore @ Pyrite Bldg | sì | sì | censita, non ancora producibile |
| `EVT-T-0041` | 3 | spinoff | 162 | 0 | Colosseum, ombra: Furret: Rogue Cail @ Pyrite Town | sì | sì | censita, non ancora producibile |
| `EVT-T-0042` | 3 | spinoff | 218 | 0 | Colosseum, ombra: Slugma: Roller Boy Lon @ Pyrite Town | sì | sì | censita, non ancora producibile |
| `EVT-T-0043` | 3 | spinoff | 223 | 0 | Colosseum, ombra: Remoraid: Miror B.Peon Reath @ Pyrite Bldg | sì | sì | censita, non ancora producibile |
| `EVT-T-0045` | 3 | spinoff | 226 | 0 | Colosseum, ombra: Mantine: Miror B.Peon Ferma @ Pyrite Bldg | sì | sì | censita, non ancora producibile |
| `EVT-T-0047` | 3 | spinoff | 211 | 0 | Colosseum, ombra: Qwilfish: Hunter Doken @ Pyrite Bldg | sì | sì | censita, non ancora producibile |
| `EVT-T-0048` | 3 | spinoff | 307 | 0 | Colosseum, ombra: Meditite: Rider Twan @ Pyrite Cave | sì | sì | censita, non ancora producibile |
| `EVT-T-0049` | 3 | spinoff | 206 | 0 | Colosseum, ombra: Dunsparce: Rider Sosh @ Pyrite Cave | sì | sì | censita, non ancora producibile |
| `EVT-T-0051` | 3 | spinoff | 185 | 0 | Colosseum, ombra: Sudowoodo: Cipher Admin Miror B. @ Realgam Tower | sì | sì | censita, non ancora producibile |
| `EVT-T-0060` | 3 | spinoff | 166 | 0 | Colosseum, ombra: Ledian: Cipher Peon Kloak @ The Under | sì | sì | censita, non ancora producibile |
| `EVT-T-0065` | 3 | spinoff | 207 | 0 | Colosseum, ombra: Gligar: Hunter Frena @ The Under Subway | sì | sì | censita, non ancora producibile |
| `EVT-T-0067` | 3 | spinoff | 234 | 0 | Colosseum, ombra: Stantler: Chaser Liaks @ The Under Subway | sì | sì | censita, non ancora producibile |
| `EVT-T-0069` | 3 | spinoff | 221 | 0 | Colosseum, ombra: Piloswine: Bodybuilder Lonia @ The Under Subway | sì | sì | censita, non ancora producibile |
| `EVT-T-0071` | 3 | spinoff | 215 | 0 | Colosseum, ombra: Sneasel: Rider Nelis @ The Under Subway | sì | sì | censita, non ancora producibile |
| `EVT-T-0073` | 3 | spinoff | 190 | 0 | Colosseum, ombra: Aipom: Cipher Peon Cole @ Shadow PKMN Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0074` | 3 | spinoff | 198 | 0 | Colosseum, ombra: Murkrow: Cipher Peon Lare @ Shadow PKMN Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0076` | 3 | spinoff | 205 | 0 | Colosseum, ombra: Forretress: Cipher Peon Vana @ Shadow PKMN Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0077` | 3 | spinoff | 210 | 0 | Colosseum, ombra: Granbull: Cipher Peon Tanie @ Shadow PKMN Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0078` | 3 | spinoff | 329 | 0 | Colosseum, ombra: Vibrava: Cipher Peon Remil @ Shadow PKMN Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0079` | 3 | spinoff | 168 | 0 | Colosseum, ombra: Ariados: Cipher Peon Lesar @ Shadow PKMN Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0083` | 3 | spinoff | 192 | 0 | Colosseum, ombra: Sunflora: Cipher Peon Baila @ Realgam Tower | sì | sì | censita, non ancora producibile |
| `EVT-T-0089` | 3 | spinoff | 227 | 0 | Colosseum, ombra: Skarmory: Snagem Head Gonzap @ Realgam Tower | sì | sì | censita, non ancora producibile |
| `EVT-T-0098` | 3 | spinoff | 217 | 0 | Colosseum, ombra: Ursaring: Team Snagem Agrev @ Snagem Hideout | sì | sì | censita, non ancora producibile |
| `EVT-T-0099` | 3 | spinoff | 213 | 0 | Colosseum, ombra: Shuckle: Deep King Agnol @ Deep Colosseum | sì | sì | censita, non ancora producibile |
| `EVT-T-0100` | 3 | spinoff | 176 | 0 | Colosseum, ombra: Togetic: Cipher Peon Fein @ Outskirt Stand | sì | sì | censita, non ancora producibile |
| `EVT-T-0105` | 3 | spinoff | 239 | 0 | XD, scambi: Elekid @ Snagem Hideout | sì | sì | censita, non ancora producibile |
| `EVT-T-0109` | 3 | spinoff | 216 | 0 | XD, ombra: Teddiursa: Cipher Peon Naps @ Pokémon HQ Lab -- treat as Gift as it can only be captured in a Poké Ball | sì | sì | censita, non ancora producibile |
| `EVT-T-0111` | 3 | spinoff | 363 | 0 | XD, ombra: Spheal: Cipher Peon Blusix @ Cipher Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0113` | 3 | spinoff | 343 | 0 | XD, ombra: Baltoy: Cipher Peon Browsix @ Cipher Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0117` | 3 | spinoff | 316 | 0 | XD, ombra: Gulpin: Cipher Peon Purpsix @ Cipher Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0119` | 3 | spinoff | 273 | 0 | XD, ombra: Seedot: Cipher Peon Greesix @ Cipher Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0121` | 3 | spinoff | 167 | 0 | XD, ombra: Spinarak: Cipher Peon Nexir @ Cipher Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0124` | 3 | spinoff | 315 | 0 | XD, ombra: Roselia: Cipher Peon Fasin @ Phenac City | sì | sì | censita, non ancora producibile |
| `EVT-T-0125` | 3 | spinoff | 301 | 0 | XD, ombra: Delcatty: Cipher Admin Lovrina @ Cipher Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0126` | 3 | spinoff | 299 | 0 | XD, ombra: Nosepass: Wanderer Miror B. @ Poké Spots | sì | sì | censita, non ancora producibile |
| `EVT-T-0127` | 3 | spinoff | 228 | 0 | XD, ombra: Houndour: Cipher Peon Resix  @ Phenac City | sì | sì | censita, non ancora producibile |
| `EVT-T-0130` | 3 | spinoff | 355 | 0 | XD, ombra: Duskull: Cipher Peon Lobar @ ONBS Building | sì | sì | censita, non ancora producibile |
| `EVT-T-0133` | 3 | spinoff | 361 | 0 | XD, ombra: Snorunt: Cipher Peon Exinn @ Phenac City | sì | sì | censita, non ancora producibile |
| `EVT-T-0134` | 3 | spinoff | 204 | 0 | XD, ombra: Pineco: Cipher Peon Gonrap @ Phenac City | sì | sì | censita, non ancora producibile |
| `EVT-T-0135` | 3 | spinoff | 220 | 0 | XD, ombra: Swinub: Cipher Peon Greck @ Phenac City | sì | sì | censita, non ancora producibile |
| `EVT-T-0136` | 3 | spinoff | 177 | 0 | XD, ombra: Natu: Cipher Peon Eloin @ Phenac City | sì | sì | censita, non ancora producibile |
| `EVT-T-0137` | 3 | spinoff | 285 | 0 | XD, ombra: Shroomish: Cipher R&D Klots @ Cipher Lab | sì | sì | censita, non ancora producibile |
| `EVT-T-0139` | 3 | spinoff | 21 | 0 | XD, ombra: Spearow: Cipher Peon Ezin @ Phenac Stadium | sì | sì | censita, non ancora producibile |
| `EVT-T-0141` | 3 | spinoff | 86 | 0 | XD, ombra: Seel: Cipher Peon Egrog @ Phenac Stadium | sì | sì | censita, non ancora producibile |
| `EVT-T-0143` | 3 | spinoff | 100 | 0 | XD, ombra: Voltorb: Wanderer Miror B. @ Cave Poké Spot | sì | sì | censita, non ancora producibile |
| `EVT-T-0144` | 3 | spinoff | 335 | 0 | XD, ombra: Zangoose: Thug Zook @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0145` | 3 | spinoff | 58 | 0 | XD, ombra: Growlithe: Cipher Peon Humah @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0146` | 3 | spinoff | 46 | 0 | XD, ombra: Paras: Cipher Peon Humah @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0147` | 3 | spinoff | 90 | 0 | XD, ombra: Shellder: Cipher Peon Gorog @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0148` | 3 | spinoff | 15 | 0 | XD, ombra: Beedrill: Cipher Peon Lok @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0149` | 3 | spinoff | 17 | 0 | XD, ombra: Pidgeotto: Cipher Peon Lok @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0150` | 3 | spinoff | 12 | 0 | XD, ombra: Butterfree: Cipher Peon Targ @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0151` | 3 | spinoff | 114 | 0 | XD, ombra: Tangela: Cipher Peon Targ @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0152` | 3 | spinoff | 20 | 0 | XD, ombra: Raticate: Chaser Furgy @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0153` | 3 | spinoff | 49 | 0 | XD, ombra: Venomoth: Cipher Peon Angic @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0154` | 3 | spinoff | 70 | 0 | XD, ombra: Weepinbell: Cipher Peon Angic @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0155` | 3 | spinoff | 24 | 0 | XD, ombra: Arbok: Cipher Peon Smarton @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0156` | 3 | spinoff | 57 | 0 | XD, ombra: Primeape: Cipher Admin Gorigan @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0157` | 3 | spinoff | 97 | 0 | XD, ombra: Hypno: Cipher Admin Gorigan @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0160` | 3 | spinoff | 82 | 0 | XD, ombra: Magneton: Cipher Peon Snidle @ Cipher Key Lair | sì | sì | censita, non ancora producibile |
| `EVT-T-0161` | 3 | spinoff | 85 | 0 | XD, ombra: Dodrio: Chaser Furgy @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0165` | 3 | spinoff | 354 | 0 | XD, ombra: Banette: Cipher Peon Litnar @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0168` | 3 | spinoff | 219 | 0 | XD, ombra: Magcargo: Cipher Peon Kolest @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0169` | 3 | spinoff | 78 | 0 | XD, ombra: Rapidash: Cipher Peon Kolest @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0170` | 3 | spinoff | 107 | 0 | XD, ombra: Hitmonchan: Cipher Peon Karbon @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0171` | 3 | spinoff | 106 | 0 | XD, ombra: Hitmonlee: Cipher Peon Petro @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0177` | 3 | spinoff | 121 | 0 | XD, ombra: Starmie: Cipher Admin Snattle @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0179` | 3 | spinoff | 277 | 0 | XD, ombra: Swellow: Cipher Admin Ardos @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0181` | 3 | spinoff | 62 | 0 | XD, ombra: Poliwrath: Cipher Admin Gorigan @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0182` | 3 | spinoff | 122 | 0 | XD, ombra: Mr. Mime: Cipher Admin Gorigan @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0183` | 3 | spinoff | 51 | 0 | XD, ombra: Dugtrio: Cipher Peon Kolax @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0186` | 3 | spinoff | 105 | 0 | XD, ombra: Marowak: Cipher Admin Eldes @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0187` | 3 | spinoff | 131 | 0 | XD, ombra: Lapras: Cipher Admin Eldes @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0192` | 3 | spinoff | 128 | 0 | XD, ombra: Tauros: Grand Master Greevil @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0193` | 3 | spinoff | 112 | 0 | XD, ombra: Rhydon: Grand Master Greevil @ Citadark Isle | sì | sì | censita, non ancora producibile |
| `EVT-T-0196` | 3 | spinoff | 175 | 0 | XD, ombra: Togepi: Pokémon Trainer Hordel @ Outskirt Stand | sì | sì | censita, non ancora producibile |
| `EVT-T-0197` | 3 | spinoff | 261 | 0 | XD, ombra: Poochyena: Bodybuilder Kilen @ Gateon Port | sì | sì | censita, non ancora producibile |
| `EVT-T-0198` | 3 | spinoff | 165 | 0 | XD, ombra: Ledyba: Casual Guy Cyle @ Gateon Port | sì | sì | censita, non ancora producibile |
| `EVT-T-0201` | 4 | periferica | 77 | 0 | My Pokemon Ranch: Ponyta | sì | sì | censita, non ancora producibile |
| `EVT-T-0209` | 4 | periferica | 320 | 0 | My Pokemon Ranch: Wailmer | sì | sì | censita, non ancora producibile |
| `EVT-T-0211` | 4 | periferica | 397 | 0 | My Pokemon Ranch: Staravia | sì | sì | censita, non ancora producibile |
| `EVT-T-0212` | 4 | periferica | 415 | 0 | My Pokemon Ranch: Combee | sì | sì | censita, non ancora producibile |
| `EVT-T-0214` | 4 | periferica | 422 | 1 | My Pokemon Ranch: Shellos | sì | sì | censita, non ancora producibile |
| `EVT-T-0215` | 4 | periferica | 427 | 0 | My Pokemon Ranch: Buneary | sì | sì | censita, non ancora producibile |
| `EVT-T-0216` | 4 | periferica | 453 | 0 | My Pokemon Ranch: Croagunk | sì | sì | censita, non ancora producibile |
| `EVT-T-0217` | 4 | periferica | 456 | 0 | My Pokemon Ranch: Finneon | sì | sì | censita, non ancora producibile |
| `EVT-T-0218` | 4 | periferica | 459 | 0 | My Pokemon Ranch: Snover | sì | sì | censita, non ancora producibile |
| `EVT-T-0222` | 5 | periferica | 120 | 0 | Dream Radar: Staryu | sì | sì | censita, non ancora producibile |
| `EVT-T-0223` | 5 | periferica | 137 | 0 | Dream Radar: Porygon | sì | sì | censita, non ancora producibile |
| `EVT-T-0224` | 5 | periferica | 163 | 0 | Dream Radar: Hoothoot | sì | sì | censita, non ancora producibile |
| `EVT-T-0228` | 5 | periferica | 238 | 0 | Dream Radar: Smoochum | sì | sì | censita, non ancora producibile |
| `EVT-T-0234` | 5 | periferica | 425 | 0 | Dream Radar: Drifloon | sì | sì | censita, non ancora producibile |
| `EVT-T-0235` | 5 | periferica | 436 | 0 | Dream Radar: Bronzor | sì | sì | censita, non ancora producibile |
| `EVT-T-0243` | 5 | periferica | 561 | 0 | Dream Radar: Sigilyph | sì | sì | censita, non ancora producibile |
| `EVT-T-0261` | 4 | periferica | 84 | 0 | Pokewalker: corso Prato Ristoro, livello 8, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0262` | 4 | periferica | 29 | 0 | Pokewalker: corso Prato Ristoro, livello 5, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0263` | 4 | periferica | 32 | 0 | Pokewalker: corso Prato Ristoro, livello 5, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0264` | 4 | periferica | 16 | 0 | Pokewalker: corso Prato Ristoro, livello 5, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0265` | 4 | periferica | 161 | 0 | Pokewalker: corso Prato Ristoro, livello 5, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0268` | 4 | periferica | 48 | 0 | Pokewalker: corso Bosco Rumoroso, livello 6, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0272` | 4 | periferica | 240 | 0 | Pokewalker: corso Strada Sconnessa, livello 9, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0273` | 4 | periferica | 95 | 0 | Pokewalker: corso Strada Sconnessa, livello 9, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0274` | 4 | periferica | 66 | 0 | Pokewalker: corso Strada Sconnessa, livello 7, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0277` | 4 | periferica | 74 | 0 | Pokewalker: corso Strada Sconnessa, livello 8, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0282` | 4 | periferica | 191 | 0 | Pokewalker: corso Bella Spiaggia, livello 6, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0283` | 4 | periferica | 194 | 0 | Pokewalker: corso Bella Spiaggia, livello 6, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0285` | 4 | periferica | 81 | 0 | Pokewalker: corso Zona Suburbana, livello 11, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0289` | 4 | periferica | 19 | 0 | Pokewalker: corso Zona Suburbana, livello 7, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0291` | 4 | periferica | 92 | 0 | Pokewalker: corso Grotta Buia, livello 15, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0294` | 4 | periferica | 41 | 0 | Pokewalker: corso Grotta Buia, livello 8, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0296` | 4 | periferica | 147 | 0 | Pokewalker: corso Lago Blu, livello 10, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0298` | 4 | periferica | 98 | 0 | Pokewalker: corso Lago Blu, livello 12, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0300` | 4 | periferica | 118 | 0 | Pokewalker: corso Lago Blu, livello 9, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0301` | 4 | periferica | 72 | 0 | Pokewalker: corso Lago Blu, livello 9, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0302` | 4 | periferica | 63 | 0 | Pokewalker: corso Periferia, livello 15, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0304` | 4 | periferica | 109 | 0 | Pokewalker: corso Periferia, livello 13, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0310` | 4 | periferica | 314 | 0 | Pokewalker: corso Prato di Hoenn, livello 25, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0311` | 4 | periferica | 313 | 0 | Pokewalker: corso Prato di Hoenn, livello 25, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0313` | 4 | periferica | 265 | 0 | Pokewalker: corso Prato di Hoenn, livello 15, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0315` | 4 | periferica | 298 | 0 | Pokewalker: corso Spiaggia Calda, livello 20, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0323` | 4 | periferica | 111 | 0 | Pokewalker: corso Via del Vulcano, livello 25, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0326` | 4 | periferica | 352 | 0 | Pokewalker: corso Casa sull Albero, livello 30, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0327` | 4 | periferica | 351 | 0 | Pokewalker: corso Casa sull Albero, livello 30, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0328` | 4 | periferica | 203 | 0 | Pokewalker: corso Casa sull Albero, livello 28, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0330` | 4 | periferica | 44 | 0 | Pokewalker: corso Casa sull Albero, livello 14, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0334` | 4 | periferica | 42 | 0 | Pokewalker: corso Grotta Spaventosa, livello 33, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0338` | 4 | periferica | 439 | 0 | Pokewalker: corso Prato di Sinnoh, livello 29, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0340` | 4 | periferica | 403 | 0 | Pokewalker: corso Prato di Sinnoh, livello 33, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0341` | 4 | periferica | 406 | 0 | Pokewalker: corso Prato di Sinnoh, livello 30, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0342` | 4 | periferica | 399 | 0 | Pokewalker: corso Prato di Sinnoh, livello 13, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0343` | 4 | periferica | 401 | 0 | Pokewalker: corso Prato di Sinnoh, livello 15, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0351` | 4 | periferica | 438 | 0 | Pokewalker: corso Grande Foresta, livello 30, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0353` | 4 | periferica | 400 | 0 | Pokewalker: corso Grande Foresta, livello 30, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0356` | 4 | periferica | 433 | 0 | Pokewalker: corso Lago Bianco, livello 22, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0359` | 4 | periferica | 418 | 0 | Pokewalker: corso Lago Bianco, livello 28, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0361` | 4 | periferica | 170 | 0 | Pokewalker: corso Lago Bianco, livello 17, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0370` | 4 | periferica | 39 | 0 | Pokewalker: corso Villaggio Turistico, livello 30, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0371` | 4 | periferica | 35 | 0 | Pokewalker: corso Villaggio Turistico, livello 31, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0372` | 4 | periferica | 183 | 0 | Pokewalker: corso Villaggio Turistico, livello 25, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0373` | 4 | periferica | 187 | 0 | Pokewalker: corso Villaggio Turistico, livello 25, corso in dotazione | sì | sì | censita, non ancora producibile |
| `EVT-T-0406` | 4 | periferica | 279 | 0 | Pokewalker: corso Gita, livello 15, corso distribuito | sì | sì | censita, non ancora producibile |
| `EVT-T-0407` | 4 | periferica | 61 | 0 | Pokewalker: corso Gita, livello 15, corso distribuito | sì | sì | censita, non ancora producibile |
| `EVT-T-0419` | 4 | periferica | 440 | 0 | Pokewalker: corso Prato Amicizia, livello 5, corso distribuito | sì | sì | censita, non ancora producibile |
| `EVT-T-0421` | 4 | periferica | 173 | 0 | Pokewalker: corso Prato Amicizia, livello 5, corso distribuito | sì | sì | censita, non ancora producibile |
| `EVT-2-0039` | 2 | tabella di incontro | 209 | 0 | tabella di incontro da evento | sì | sì | letta, struttura alla portata di pokebridge |
| `EVT-2-0102` | 2 | tabella di incontro | 104 | 0 | tabella di incontro da evento | sì | sì | letta, struttura alla portata di pokebridge |
| `EVT-2-0120` | 2 | tabella di incontro | 236 | 0 | tabella di incontro da evento | sì | sì | letta, struttura alla portata di pokebridge |
| `EVT-2-0123` | 2 | tabella di incontro | 231 | 0 | tabella di incontro da evento | sì | sì | letta, struttura alla portata di pokebridge |
| `EVT-3-0002` | 3 | carta meraviglia | 385 | 0 | CHANNEL | sì | no | non producibile |
| `EVT-3-0004` | 3 | carta meraviglia | 263 | 0 | Berry Fix Sapphire | sì | no | producibile e verificata |
| `EVT-3-0005` | 3 | carta meraviglia | 385 | 0 | Negai Boshi Jirachi | sì | no | producibile e verificata |
| `EVT-3-0006` | 3 | carta meraviglia | 385 | 0 | Negai Boshi Jirachi (Match Recipient) | sì | no | producibile e verificata |
| `EVT-3-0007` | 3 | carta meraviglia | 385 | 0 | Tanabata Jirachi (2004) | sì | no | producibile e verificata |
| `EVT-3-0010` | 3 | carta meraviglia | 25 | 0 | Yokohama Pikachu | sì | no | producibile e verificata |
| `EVT-3-0011` | 3 | carta meraviglia | 151 | 0 | Hadou Mew | sì | no | producibile e verificata |
| `EVT-3-0012` | 3 | carta meraviglia | 25 | 0 | GW Pikachu | sì | no | producibile e verificata |
| `EVT-3-0013` | 3 | carta meraviglia | 25 | 0 | Sapporo Pikachu | sì | no | producibile e verificata |
| `EVT-3-0014` | 3 | carta meraviglia | 385 | 0 | Tanabata Jirachi (2005) | sì | no | producibile e verificata |
| `EVT-3-0020` | 3 | carta meraviglia | 151 | 0 | PokéPark Mew | sì | no | producibile e verificata |
| `EVT-3-0022` | 3 | carta meraviglia | 385 | 0 | Tanabata Jirachi (2006) | sì | no | producibile e verificata |
| `EVT-3-0023` | 3 | carta meraviglia | 251 | 0 | Mitsurin Celebi (2006) | sì | no | producibile e verificata |
| `EVT-3-0024` | 3 | carta meraviglia | 385 | 0 | PokéPark Jirachi (2006) | sì | no | producibile e verificata |
| `EVT-3-0025` | 3 | carta meraviglia | 385 | 0 | PokéPark Jirachi (2006) | sì | no | producibile e verificata |
| `EVT-3-0026` | 3 | carta meraviglia | 263 | 0 | Berry Fix Ruby | sì | no | producibile e verificata |
| `EVT-3-0027` | 3 | carta meraviglia | 263 | 0 | Berry Fix Sapphire | sì | no | producibile e verificata |
| `EVT-3-0029` | 3 | carta meraviglia | 25 | 0 | Pikachu | sì | no | producibile e verificata |
| `EVT-3-0038` | 3 | carta meraviglia | 6 | 0 | Charizard | sì | no | producibile e verificata |
| `EVT-3-0039` | 3 | carta meraviglia | 25 | 0 | Pikachu | sì | no | producibile e verificata |
| `EVT-3-0040` | 3 | carta meraviglia | 144 | 0 | Articuno | sì | no | producibile e verificata |
| `EVT-3-0041` | 3 | carta meraviglia | 243 | 0 | Raikou | sì | no | producibile e verificata |
| `EVT-3-0042` | 3 | carta meraviglia | 244 | 0 | Entei | sì | no | producibile e verificata |
| `EVT-3-0043` | 3 | carta meraviglia | 245 | 0 | Suicune | sì | no | producibile e verificata |
| `EVT-3-0044` | 3 | carta meraviglia | 249 | 0 | Lugia | sì | no | producibile e verificata |
| `EVT-3-0045` | 3 | carta meraviglia | 250 | 0 | Ho-Oh | sì | no | producibile e verificata |
| `EVT-3-0046` | 3 | carta meraviglia | 380 | 0 | Latias | sì | no | producibile e verificata |
| `EVT-3-0047` | 3 | carta meraviglia | 381 | 0 | Latios | sì | no | producibile e verificata |
| `EVT-3-0048` | 3 | carta meraviglia | 6 | 0 | Charizard | sì | no | producibile e verificata |
| `EVT-3-0049` | 3 | carta meraviglia | 25 | 0 | Pikachu | sì | no | producibile e verificata |
| `EVT-3-0050` | 3 | carta meraviglia | 144 | 0 | Articuno | sì | no | producibile e verificata |
| `EVT-3-0051` | 3 | carta meraviglia | 243 | 0 | Raikou | sì | no | producibile e verificata |
| `EVT-3-0052` | 3 | carta meraviglia | 244 | 0 | Entei | sì | no | producibile e verificata |
| `EVT-3-0053` | 3 | carta meraviglia | 245 | 0 | Suicune | sì | no | producibile e verificata |
| `EVT-3-0054` | 3 | carta meraviglia | 249 | 0 | Lugia | sì | no | producibile e verificata |
| `EVT-3-0055` | 3 | carta meraviglia | 250 | 0 | Ho-Oh | sì | no | producibile e verificata |
| `EVT-3-0056` | 3 | carta meraviglia | 380 | 0 | Latias | sì | no | producibile e verificata |
| `EVT-3-0057` | 3 | carta meraviglia | 381 | 0 | Latios | sì | no | producibile e verificata |
| `EVT-3-0058` | 3 | carta meraviglia | 6 | 0 | Charizard | sì | no | producibile e verificata |
| `EVT-3-0059` | 3 | carta meraviglia | 25 | 0 | Pikachu | sì | no | producibile e verificata |
| `EVT-3-0060` | 3 | carta meraviglia | 144 | 0 | Articuno | sì | no | producibile e verificata |
| `EVT-3-0061` | 3 | carta meraviglia | 243 | 0 | Raikou | sì | no | producibile e verificata |
| `EVT-3-0062` | 3 | carta meraviglia | 244 | 0 | Entei | sì | no | producibile e verificata |
| `EVT-3-0063` | 3 | carta meraviglia | 245 | 0 | Suicune | sì | no | producibile e verificata |
| `EVT-3-0064` | 3 | carta meraviglia | 249 | 0 | Lugia | sì | no | producibile e verificata |
| `EVT-3-0065` | 3 | carta meraviglia | 250 | 0 | Ho-Oh | sì | no | producibile e verificata |
| `EVT-3-0066` | 3 | carta meraviglia | 380 | 0 | Latias | sì | no | producibile e verificata |
| `EVT-3-0067` | 3 | carta meraviglia | 381 | 0 | Latios | sì | no | producibile e verificata |
| `EVT-3-0068` | 3 | carta meraviglia | 6 | 0 | Charizard | sì | no | producibile e verificata |
| `EVT-3-0069` | 3 | carta meraviglia | 25 | 0 | Pikachu | sì | no | producibile e verificata |
| `EVT-3-0070` | 3 | carta meraviglia | 144 | 0 | Articuno | sì | no | producibile e verificata |
| `EVT-3-0071` | 3 | carta meraviglia | 243 | 0 | Raikou | sì | no | producibile e verificata |
| `EVT-3-0072` | 3 | carta meraviglia | 244 | 0 | Entei | sì | no | producibile e verificata |
| `EVT-3-0073` | 3 | carta meraviglia | 245 | 0 | Suicune | sì | no | producibile e verificata |
| `EVT-3-0074` | 3 | carta meraviglia | 249 | 0 | Lugia | sì | no | producibile e verificata |
| `EVT-3-0075` | 3 | carta meraviglia | 250 | 0 | Ho-Oh | sì | no | producibile e verificata |
| `EVT-3-0076` | 3 | carta meraviglia | 380 | 0 | Latias | sì | no | producibile e verificata |
| `EVT-3-0077` | 3 | carta meraviglia | 381 | 0 | Latios | sì | no | producibile e verificata |
| `EVT-3-0078` | 3 | carta meraviglia | 151 | 0 | Mew | sì | no | producibile e verificata |
| `EVT-3-0079` | 3 | carta meraviglia | 375 | 0 | Metang | sì | no | producibile e verificata |
| `EVT-3-0081` | 3 | carta meraviglia | 386 | 0 | Deoxys | sì | no | producibile e verificata |
| `EVT-3-0083` | 3 | carta meraviglia | 6 | 0 | Charizard | sì | no | producibile e verificata |
| `EVT-3-0085` | 3 | carta meraviglia | 25 | 0 | Pikachu (Fly) | sì | no | producibile e verificata |
| `EVT-3-0087` | 3 | carta meraviglia | 144 | 0 | Articuno | sì | no | producibile e verificata |
| `EVT-3-0094` | 3 | carta meraviglia | 243 | 0 | Raikou | sì | no | producibile e verificata |
| `EVT-3-0095` | 3 | carta meraviglia | 244 | 0 | Entei | sì | no | producibile e verificata |
| `EVT-3-0096` | 3 | carta meraviglia | 245 | 0 | Suicune | sì | no | producibile e verificata |
| `EVT-3-0100` | 3 | carta meraviglia | 380 | 0 | Latias | sì | no | producibile e verificata |
| `EVT-3-0101` | 3 | carta meraviglia | 381 | 0 | Latios | sì | no | producibile e verificata |
| `EVT-3-0102` | 3 | carta meraviglia | 1 | 0 | Bulbasaur | sì | no | producibile e verificata |
| `EVT-3-0103` | 3 | carta meraviglia | 6 | 0 | Charizard | sì | no | producibile e verificata |
| `EVT-3-0104` | 3 | carta meraviglia | 9 | 0 | Blastoise | sì | no | producibile e verificata |
| `EVT-3-0105` | 3 | carta meraviglia | 25 | 0 | Pikachu (No Fly) | sì | no | producibile e verificata |
| `EVT-3-0106` | 3 | carta meraviglia | 65 | 0 | Alakazam | sì | no | producibile e verificata |
| `EVT-3-0107` | 3 | carta meraviglia | 144 | 0 | Articuno | sì | no | producibile e verificata |
| `EVT-3-0108` | 3 | carta meraviglia | 145 | 0 | Zapdos | sì | no | producibile e verificata |
| `EVT-3-0109` | 3 | carta meraviglia | 146 | 0 | Moltres | sì | no | producibile e verificata |
| `EVT-3-0110` | 3 | carta meraviglia | 149 | 0 | Dragonite | sì | no | producibile e verificata |
| `EVT-3-0111` | 3 | carta meraviglia | 157 | 0 | Typhlosion | sì | no | producibile e verificata |
| `EVT-3-0112` | 3 | carta meraviglia | 196 | 0 | Espeon | sì | no | producibile e verificata |
| `EVT-3-0113` | 3 | carta meraviglia | 197 | 0 | Umbreon | sì | no | producibile e verificata |
| `EVT-3-0114` | 3 | carta meraviglia | 243 | 0 | Raikou | sì | no | producibile e verificata |
| `EVT-3-0115` | 3 | carta meraviglia | 244 | 0 | Entei | sì | no | producibile e verificata |
| `EVT-3-0116` | 3 | carta meraviglia | 245 | 0 | Suicune | sì | no | producibile e verificata |
| `EVT-3-0117` | 3 | carta meraviglia | 248 | 0 | Tyranitar | sì | no | producibile e verificata |
| `EVT-3-0118` | 3 | carta meraviglia | 251 | 0 | Celebi | sì | no | producibile e verificata |
| `EVT-3-0119` | 3 | carta meraviglia | 257 | 0 | Blaziken | sì | no | producibile e verificata |
| `EVT-3-0120` | 3 | carta meraviglia | 359 | 0 | Absol | sì | no | producibile e verificata |
| `EVT-3-0121` | 3 | carta meraviglia | 380 | 0 | Latias | sì | no | producibile e verificata |
| `EVT-3-0122` | 3 | carta meraviglia | 381 | 0 | Latios | sì | no | producibile e verificata |
| `EVT-3-0124` | 3 | carta meraviglia | 172 | 0 | Pichu with Wish | sì | no | producibile e verificata |
| `EVT-3-0125` | 3 | carta meraviglia | 172 | 0 | Pichu with Teeter Dance | sì | no | producibile e verificata |
| `EVT-3-0126` | 3 | carta meraviglia | 172 | 0 | Pichu with Wish | sì | no | producibile e verificata |
| `EVT-3-0128` | 3 | carta meraviglia | 280 | 0 | Ralts with Wish | sì | no | producibile e verificata |
| `EVT-3-0129` | 3 | carta meraviglia | 359 | 0 | Absol with Spite | sì | no | producibile e verificata |
| `EVT-3-0130` | 3 | carta meraviglia | 359 | 0 | Absol with Wish | sì | no | producibile e verificata |
| `EVT-3-0132` | 3 | carta meraviglia | 371 | 0 | Bagon with Wish | sì | no | producibile e verificata |
| `EVT-3-0134` | 3 | carta meraviglia | 52 | 0 | Meowth with Petal Dance | sì | no | producibile e verificata |
| `EVT-3-0144` | 3 | carta meraviglia | 172 | 0 | Pichu with Follow me | sì | no | producibile e verificata |
| `EVT-3-0158` | 3 | carta meraviglia | 54 | 0 | Psyduck with Mud Sport | sì | no | producibile e verificata |
| `EVT-3-0159` | 3 | carta meraviglia | 172 | 0 | Pichu with Follow Me | sì | no | producibile e verificata |
| `EVT-3-0160` | 3 | carta meraviglia | 174 | 0 | Igglybuff with Tickle | sì | no | producibile e verificata |
| `EVT-3-0161` | 3 | carta meraviglia | 222 | 0 | Corsola with Mud Sport | sì | no | producibile e verificata |
| `EVT-3-0162` | 3 | carta meraviglia | 276 | 0 | Taillow with Feather Dance | sì | no | producibile e verificata |
| `EVT-3-0163` | 3 | carta meraviglia | 283 | 0 | Surskit with Mud Sport | sì | no | producibile e verificata |
| `EVT-3-0164` | 3 | carta meraviglia | 293 | 0 | Whismur with Teeter Dance | sì | no | producibile e verificata |
| `EVT-3-0165` | 3 | carta meraviglia | 300 | 0 | Skitty with Rollout | sì | no | producibile e verificata |
| `EVT-3-0166` | 3 | carta meraviglia | 311 | 0 | Plusle with Water Sport | sì | no | producibile e verificata |
| `EVT-3-0167` | 3 | carta meraviglia | 312 | 0 | Minun with Mud Sport | sì | no | producibile e verificata |
| `EVT-3-0168` | 3 | carta meraviglia | 325 | 0 | Spoink with Uproar | sì | no | producibile e verificata |
| `EVT-3-0169` | 3 | carta meraviglia | 327 | 0 | Spinda with Sing | sì | no | producibile e verificata |
| `EVT-3-0170` | 3 | carta meraviglia | 331 | 0 | Cacnea with Encore | sì | no | producibile e verificata |
| `EVT-3-0171` | 3 | carta meraviglia | 341 | 0 | Corphish with Water Sport | sì | no | producibile e verificata |
| `EVT-3-0172` | 3 | carta meraviglia | 360 | 0 | Wynaut with Tickle | sì | no | producibile e verificata |
| `EVT-4-0000` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0002` | 4 | dono segreto | 490 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0003` | 4 | dono segreto | 490 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0004` | 4 | dono segreto | 490 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0006` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0007` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0008` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0009` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0010` | 4 | dono segreto | 149 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0011` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0014` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0016` | 4 | dono segreto | 493 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0017` | 4 | dono segreto | 493 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0018` | 4 | dono segreto | 172 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0019` | 4 | dono segreto | 172 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0020` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0022` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0023` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0024` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0025` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0027` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0028` | 4 | dono segreto | 243 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0029` | 4 | dono segreto | 243 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0030` | 4 | dono segreto | 244 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0031` | 4 | dono segreto | 244 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0032` | 4 | dono segreto | 245 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0033` | 4 | dono segreto | 245 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0034` | 4 | dono segreto | 251 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0035` | 4 | dono segreto | 251 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0036` | 4 | dono segreto | 251 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0037` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0039` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0044` | 4 | dono segreto | 350 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0045` | 4 | dono segreto | 486 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0047` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0048` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0049` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0050` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0052` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0053` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0054` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0055` | 4 | dono segreto | 493 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0056` | 4 | dono segreto | 172 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0057` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0058` | 4 | dono segreto | 447 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0059` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0060` | 4 | dono segreto | 133 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0061` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0062` | 4 | dono segreto | 243 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0063` | 4 | dono segreto | 244 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0064` | 4 | dono segreto | 245 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0065` | 4 | dono segreto | 251 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0066` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0067` | 4 | dono segreto | 466 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0068` | 4 | dono segreto | 467 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0069` | 4 | dono segreto | 350 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0070` | 4 | dono segreto | 486 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0071` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0072` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0073` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0074` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0075` | 4 | dono segreto | 485 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0076` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0077` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0078` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0079` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0080` | 4 | dono segreto | 493 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0081` | 4 | dono segreto | 172 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0082` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0083` | 4 | dono segreto | 447 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0084` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0085` | 4 | dono segreto | 133 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0086` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0087` | 4 | dono segreto | 243 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0088` | 4 | dono segreto | 244 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0089` | 4 | dono segreto | 245 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0090` | 4 | dono segreto | 251 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0091` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0092` | 4 | dono segreto | 466 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0093` | 4 | dono segreto | 467 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0094` | 4 | dono segreto | 350 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0095` | 4 | dono segreto | 486 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0096` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0097` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0098` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0099` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0100` | 4 | dono segreto | 485 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0101` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0102` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0103` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0104` | 4 | dono segreto | 493 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0105` | 4 | dono segreto | 172 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0106` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0107` | 4 | dono segreto | 447 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0108` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0109` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0110` | 4 | dono segreto | 243 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0111` | 4 | dono segreto | 244 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0112` | 4 | dono segreto | 245 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0113` | 4 | dono segreto | 251 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0114` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0115` | 4 | dono segreto | 466 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0116` | 4 | dono segreto | 467 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0117` | 4 | dono segreto | 486 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0118` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0119` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0120` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0121` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0122` | 4 | dono segreto | 485 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0123` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0127` | 4 | dono segreto | 52 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0132` | 4 | dono segreto | 490 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0134` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0136` | 4 | dono segreto | 490 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0137` | 4 | dono segreto | 490 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0138` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0139` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0140` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0141` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0142` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0143` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0144` | 4 | dono segreto | 448 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0145` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0146` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0147` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0149` | 4 | dono segreto | 224 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0150` | 4 | dono segreto | 466 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0151` | 4 | dono segreto | 467 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0152` | 4 | dono segreto | 350 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0153` | 4 | dono segreto | 149 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0155` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0156` | 4 | dono segreto | 447 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0157` | 4 | dono segreto | 486 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0158` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0159` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0160` | 4 | dono segreto | 4 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0161` | 4 | dono segreto | 493 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0162` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0163` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0164` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0165` | 4 | dono segreto | 350 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0166` | 4 | dono segreto | 133 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0167` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0168` | 4 | dono segreto | 172 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0169` | 4 | dono segreto | 52 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0170` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0171` | 4 | dono segreto | 4 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0173` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0174` | 4 | dono segreto | 133 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0175` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0176` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0177` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0178` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0179` | 4 | dono segreto | 243 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0180` | 4 | dono segreto | 244 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0181` | 4 | dono segreto | 245 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0182` | 4 | dono segreto | 251 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0184` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0185` | 4 | dono segreto | 490 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0186` | 4 | dono segreto | 4 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0187` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0188` | 4 | dono segreto | 390 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0189` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0190` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0191` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0192` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0193` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0194` | 4 | dono segreto | 485 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0195` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0196` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0197` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0198` | 4 | dono segreto | 490 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0200` | 4 | dono segreto | 466 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0201` | 4 | dono segreto | 467 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0203` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0205` | 4 | dono segreto | 486 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0208` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0209` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0210` | 4 | dono segreto | 172 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0211` | 4 | dono segreto | 493 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0212` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0213` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0214` | 4 | dono segreto | 350 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0215` | 4 | dono segreto | 243 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0216` | 4 | dono segreto | 244 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0217` | 4 | dono segreto | 244 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0218` | 4 | dono segreto | 243 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0219` | 4 | dono segreto | 245 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0220` | 4 | dono segreto | 251 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0221` | 4 | dono segreto | 212 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0222` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0223` | 4 | dono segreto | 490 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0224` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0225` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0226` | 4 | dono segreto | 493 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0227` | 4 | dono segreto | 172 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0228` | 4 | dono segreto | 491 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0229` | 4 | dono segreto | 447 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0230` | 4 | dono segreto | 385 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0231` | 4 | dono segreto | 133 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0232` | 4 | dono segreto | 151 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0233` | 4 | dono segreto | 243 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0234` | 4 | dono segreto | 244 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0235` | 4 | dono segreto | 245 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0236` | 4 | dono segreto | 251 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0237` | 4 | dono segreto | 25 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0238` | 4 | dono segreto | 466 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0239` | 4 | dono segreto | 467 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0240` | 4 | dono segreto | 486 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0241` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0242` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0243` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0244` | 4 | dono segreto | 386 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0245` | 4 | dono segreto | 485 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-4-0246` | 4 | dono segreto | 492 | 0 | Diamante, Perla, Platino, HeartGold e SoulSilver | sì | no | letta, non ancora producibile |
| `EVT-5-0002` | 5 | dono segreto | 491 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0003` | 5 | dono segreto | 491 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0008` | 5 | dono segreto | 571 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0011` | 5 | dono segreto | 644 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0013` | 5 | dono segreto | 643 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0018` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0019` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0021` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0022` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0026` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0027` | 5 | dono segreto | 386 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0028` | 5 | dono segreto | 150 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0030` | 5 | dono segreto | 483 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0032` | 5 | dono segreto | 484 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0034` | 5 | dono segreto | 487 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0036` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0037` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0038` | 5 | dono segreto | 491 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0039` | 5 | dono segreto | 571 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0040` | 5 | dono segreto | 571 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0041` | 5 | dono segreto | 494 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0042` | 5 | dono segreto | 644 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0043` | 5 | dono segreto | 643 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0044` | 5 | dono segreto | 560 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0045` | 5 | dono segreto | 150 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0046` | 5 | dono segreto | 246 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0047` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0048` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0049` | 5 | dono segreto | 649 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0050` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0051` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0052` | 5 | dono segreto | 648 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0053` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0054` | 5 | dono segreto | 386 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0055` | 5 | dono segreto | 483 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0056` | 5 | dono segreto | 484 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0057` | 5 | dono segreto | 487 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0058` | 5 | dono segreto | 235 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0059` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0060` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0061` | 5 | dono segreto | 491 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0062` | 5 | dono segreto | 571 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0063` | 5 | dono segreto | 494 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0064` | 5 | dono segreto | 644 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0065` | 5 | dono segreto | 643 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0066` | 5 | dono segreto | 560 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0067` | 5 | dono segreto | 150 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0068` | 5 | dono segreto | 246 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0069` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0070` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0071` | 5 | dono segreto | 649 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0072` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0073` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0074` | 5 | dono segreto | 648 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0075` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0076` | 5 | dono segreto | 386 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0077` | 5 | dono segreto | 483 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0078` | 5 | dono segreto | 484 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0079` | 5 | dono segreto | 487 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0080` | 5 | dono segreto | 235 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0081` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0082` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0083` | 5 | dono segreto | 491 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0084` | 5 | dono segreto | 571 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0085` | 5 | dono segreto | 494 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0086` | 5 | dono segreto | 644 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0087` | 5 | dono segreto | 643 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0088` | 5 | dono segreto | 560 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0089` | 5 | dono segreto | 150 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0090` | 5 | dono segreto | 246 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0091` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0092` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0093` | 5 | dono segreto | 649 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0094` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0095` | 5 | dono segreto | 52 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0096` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0097` | 5 | dono segreto | 648 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0098` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0099` | 5 | dono segreto | 386 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0100` | 5 | dono segreto | 483 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0101` | 5 | dono segreto | 484 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0102` | 5 | dono segreto | 487 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0103` | 5 | dono segreto | 235 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0105` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0107` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0109` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0111` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0114` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0115` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0116` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0117` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0118` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0119` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0120` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0121` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0122` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0123` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0124` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0125` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0126` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0127` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0128` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0129` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0130` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0131` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0132` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0133` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0134` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0135` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0136` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0137` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0138` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0139` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0140` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0141` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0142` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0143` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0144` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0145` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0146` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0147` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0148` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0149` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0150` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0151` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0152` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0153` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0154` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0155` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0156` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0157` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0158` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0159` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0160` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0161` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0162` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0163` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0164` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0165` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0166` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0167` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0168` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0169` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0170` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0171` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0172` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0173` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0174` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0175` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0176` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0177` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0178` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0179` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0180` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0181` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0182` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0183` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0184` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0185` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0186` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0187` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0188` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0189` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0190` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0191` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0192` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0193` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0194` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0195` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0196` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0197` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0198` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0199` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0200` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0201` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0202` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0203` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0204` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0205` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0206` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0207` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0208` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0209` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0210` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0211` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0212` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0213` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0214` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0215` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0216` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0217` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0218` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0219` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0220` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0221` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0222` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0223` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0224` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0225` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0226` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0227` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0228` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0229` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0230` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0231` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0232` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0233` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0234` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0235` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0236` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0237` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0238` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0239` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0240` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0241` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0242` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0243` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0244` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0245` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0246` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0247` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0248` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0249` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0250` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0251` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0252` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0253` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0254` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0255` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0256` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0257` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0258` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0259` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0260` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0261` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0262` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0263` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0264` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0265` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0266` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0267` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0268` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0269` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0270` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0271` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0272` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0273` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0274` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0275` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0276` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0277` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0278` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0279` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0280` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0281` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0282` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0283` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0284` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0285` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0286` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0287` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0288` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0289` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0290` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0291` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0292` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0293` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0294` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0295` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0296` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0297` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0298` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0299` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0300` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0301` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0302` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0303` | 5 | dono segreto | 125 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0304` | 5 | dono segreto | 93 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0305` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0306` | 5 | dono segreto | 67 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0307` | 5 | dono segreto | 126 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0308` | 5 | dono segreto | 123 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0309` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0310` | 5 | dono segreto | 79 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0311` | 5 | dono segreto | 491 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0312` | 5 | dono segreto | 491 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0313` | 5 | dono segreto | 610 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0314` | 5 | dono segreto | 511 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0315` | 5 | dono segreto | 519 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0316` | 5 | dono segreto | 571 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0318` | 5 | dono segreto | 494 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0319` | 5 | dono segreto | 644 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0320` | 5 | dono segreto | 643 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0321` | 5 | dono segreto | 610 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0324` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0325` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0326` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0327` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0328` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0329` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0330` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0331` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0332` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0333` | 5 | dono segreto | 150 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0335` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0336` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0337` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0338` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0339` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0340` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0341` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0344` | 5 | dono segreto | 492 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0345` | 5 | dono segreto | 371 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0351` | 5 | dono segreto | 371 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0352` | 5 | dono segreto | 633 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0353` | 5 | dono segreto | 621 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0354` | 5 | dono segreto | 116 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0355` | 5 | dono segreto | 333 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0356` | 5 | dono segreto | 328 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0357` | 5 | dono segreto | 371 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0358` | 5 | dono segreto | 633 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0359` | 5 | dono segreto | 621 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0360` | 5 | dono segreto | 116 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0361` | 5 | dono segreto | 333 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0362` | 5 | dono segreto | 328 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0363` | 5 | dono segreto | 371 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0364` | 5 | dono segreto | 633 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0365` | 5 | dono segreto | 621 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0366` | 5 | dono segreto | 116 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0367` | 5 | dono segreto | 333 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0368` | 5 | dono segreto | 328 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0369` | 5 | dono segreto | 384 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0370` | 5 | dono segreto | 384 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0371` | 5 | dono segreto | 257 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0374` | 5 | dono segreto | 272 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0375` | 5 | dono segreto | 350 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0378` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0379` | 5 | dono segreto | 373 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0382` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0383` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0384` | 5 | dono segreto | 648 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0385` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0386` | 5 | dono segreto | 257 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0387` | 5 | dono segreto | 254 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0388` | 5 | dono segreto | 260 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0389` | 5 | dono segreto | 272 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0390` | 5 | dono segreto | 350 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0391` | 5 | dono segreto | 365 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0392` | 5 | dono segreto | 282 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0393` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0394` | 5 | dono segreto | 373 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0395` | 5 | dono segreto | 257 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0396` | 5 | dono segreto | 254 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0397` | 5 | dono segreto | 260 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0398` | 5 | dono segreto | 272 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0399` | 5 | dono segreto | 350 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0400` | 5 | dono segreto | 365 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0401` | 5 | dono segreto | 282 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0402` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0403` | 5 | dono segreto | 373 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0404` | 5 | dono segreto | 257 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0405` | 5 | dono segreto | 254 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0406` | 5 | dono segreto | 260 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0407` | 5 | dono segreto | 272 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0408` | 5 | dono segreto | 350 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0409` | 5 | dono segreto | 365 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0410` | 5 | dono segreto | 282 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0411` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0412` | 5 | dono segreto | 373 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0413` | 5 | dono segreto | 257 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0414` | 5 | dono segreto | 254 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0415` | 5 | dono segreto | 260 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0416` | 5 | dono segreto | 272 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0417` | 5 | dono segreto | 350 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0418` | 5 | dono segreto | 365 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0419` | 5 | dono segreto | 282 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0420` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0421` | 5 | dono segreto | 373 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0422` | 5 | dono segreto | 257 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0423` | 5 | dono segreto | 254 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0424` | 5 | dono segreto | 260 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0425` | 5 | dono segreto | 272 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0426` | 5 | dono segreto | 350 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0427` | 5 | dono segreto | 365 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0428` | 5 | dono segreto | 282 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0429` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0430` | 5 | dono segreto | 373 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0431` | 5 | dono segreto | 257 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0432` | 5 | dono segreto | 254 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0433` | 5 | dono segreto | 260 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0434` | 5 | dono segreto | 272 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0435` | 5 | dono segreto | 350 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0436` | 5 | dono segreto | 365 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0437` | 5 | dono segreto | 282 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0438` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0439` | 5 | dono segreto | 373 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0440` | 5 | dono segreto | 257 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0441` | 5 | dono segreto | 254 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0442` | 5 | dono segreto | 260 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0443` | 5 | dono segreto | 272 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0444` | 5 | dono segreto | 350 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0445` | 5 | dono segreto | 365 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0446` | 5 | dono segreto | 282 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0447` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0448` | 5 | dono segreto | 373 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0450` | 5 | dono segreto | 1 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0451` | 5 | dono segreto | 4 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0453` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0454` | 5 | dono segreto | 393 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0464` | 5 | dono segreto | 649 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0468` | 5 | dono segreto | 448 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0469` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0471` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0472` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0473` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0474` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0475` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0476` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0477` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0478` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0479` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0480` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0481` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0482` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0483` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0484` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0485` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0486` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0487` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0488` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0489` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0490` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0491` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0492` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0493` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0494` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0495` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0496` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0497` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0498` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0499` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0500` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0501` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0502` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0503` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0504` | 5 | dono segreto | 383 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0505` | 5 | dono segreto | 382 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0506` | 5 | dono segreto | 52 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0507` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0508` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0509` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0510` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0511` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0512` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0513` | 5 | dono segreto | 531 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0514` | 5 | dono segreto | 494 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0515` | 5 | dono segreto | 386 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0516` | 5 | dono segreto | 649 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0517` | 5 | dono segreto | 386 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0519` | 5 | dono segreto | 150 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0520` | 5 | dono segreto | 649 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0521` | 5 | dono segreto | 385 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0522` | 5 | dono segreto | 133 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0525` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0530` | 5 | dono segreto | 503 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0531` | 5 | dono segreto | 392 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0532` | 5 | dono segreto | 500 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0533` | 5 | dono segreto | 395 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0534` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0535` | 5 | dono segreto | 497 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0536` | 5 | dono segreto | 389 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0537` | 5 | dono segreto | 133 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0538` | 5 | dono segreto | 385 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0539` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0544` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0545` | 5 | dono segreto | 350 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0546` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0547` | 5 | dono segreto | 612 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0548` | 5 | dono segreto | 637 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0549` | 5 | dono segreto | 18 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0550` | 5 | dono segreto | 442 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0551` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0552` | 5 | dono segreto | 350 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0553` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0554` | 5 | dono segreto | 610 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0556` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0557` | 5 | dono segreto | 511 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0558` | 5 | dono segreto | 610 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0559` | 5 | dono segreto | 479 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0560` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0561` | 5 | dono segreto | 511 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0562` | 5 | dono segreto | 610 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0563` | 5 | dono segreto | 479 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0564` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0565` | 5 | dono segreto | 511 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0566` | 5 | dono segreto | 610 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0567` | 5 | dono segreto | 479 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0568` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0569` | 5 | dono segreto | 511 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0573` | 5 | dono segreto | 491 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0574` | 5 | dono segreto | 610 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0575` | 5 | dono segreto | 511 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0576` | 5 | dono segreto | 519 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0577` | 5 | dono segreto | 571 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0578` | 5 | dono segreto | 559 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0579` | 5 | dono segreto | 494 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0580` | 5 | dono segreto | 644 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0581` | 5 | dono segreto | 643 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0582` | 5 | dono segreto | 635 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0583` | 5 | dono segreto | 623 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0584` | 5 | dono segreto | 150 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0585` | 5 | dono segreto | 642 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0586` | 5 | dono segreto | 641 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0587` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0588` | 5 | dono segreto | 648 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0589` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0590` | 5 | dono segreto | 637 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0591` | 5 | dono segreto | 1 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0592` | 5 | dono segreto | 4 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0593` | 5 | dono segreto | 7 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0594` | 5 | dono segreto | 393 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0595` | 5 | dono segreto | 649 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0596` | 5 | dono segreto | 371 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0597` | 5 | dono segreto | 633 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0598` | 5 | dono segreto | 621 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0599` | 5 | dono segreto | 116 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0600` | 5 | dono segreto | 333 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0601` | 5 | dono segreto | 328 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0602` | 5 | dono segreto | 371 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0603` | 5 | dono segreto | 633 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0604` | 5 | dono segreto | 621 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0605` | 5 | dono segreto | 116 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0606` | 5 | dono segreto | 333 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0607` | 5 | dono segreto | 328 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0608` | 5 | dono segreto | 371 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0609` | 5 | dono segreto | 633 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0610` | 5 | dono segreto | 621 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0611` | 5 | dono segreto | 116 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0612` | 5 | dono segreto | 333 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0613` | 5 | dono segreto | 328 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0614` | 5 | dono segreto | 371 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0615` | 5 | dono segreto | 633 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0616` | 5 | dono segreto | 621 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0617` | 5 | dono segreto | 116 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0618` | 5 | dono segreto | 333 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0619` | 5 | dono segreto | 328 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0620` | 5 | dono segreto | 371 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0621` | 5 | dono segreto | 633 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0622` | 5 | dono segreto | 621 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0623` | 5 | dono segreto | 116 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0624` | 5 | dono segreto | 333 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0625` | 5 | dono segreto | 328 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0626` | 5 | dono segreto | 371 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0627` | 5 | dono segreto | 633 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0628` | 5 | dono segreto | 621 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0629` | 5 | dono segreto | 116 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0630` | 5 | dono segreto | 333 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0631` | 5 | dono segreto | 328 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0632` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0633` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0634` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0635` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0636` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0637` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0638` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0639` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0640` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0641` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0642` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0643` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0644` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0645` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0646` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0647` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0648` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0649` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0650` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0651` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0652` | 5 | dono segreto | 149 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0653` | 5 | dono segreto | 445 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0654` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0655` | 5 | dono segreto | 212 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0656` | 5 | dono segreto | 248 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0657` | 5 | dono segreto | 52 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0658` | 5 | dono segreto | 1 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0659` | 5 | dono segreto | 4 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0660` | 5 | dono segreto | 7 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0661` | 5 | dono segreto | 1 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0662` | 5 | dono segreto | 4 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0663` | 5 | dono segreto | 7 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0664` | 5 | dono segreto | 1 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0665` | 5 | dono segreto | 4 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0666` | 5 | dono segreto | 7 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0667` | 5 | dono segreto | 386 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0668` | 5 | dono segreto | 649 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0669` | 5 | dono segreto | 483 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0670` | 5 | dono segreto | 484 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0671` | 5 | dono segreto | 487 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0672` | 5 | dono segreto | 385 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0673` | 5 | dono segreto | 385 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0677` | 5 | dono segreto | 588 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0678` | 5 | dono segreto | 616 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0679` | 5 | dono segreto | 491 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0680` | 5 | dono segreto | 571 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0681` | 5 | dono segreto | 494 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0682` | 5 | dono segreto | 644 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0683` | 5 | dono segreto | 643 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0684` | 5 | dono segreto | 560 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0685` | 5 | dono segreto | 150 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0686` | 5 | dono segreto | 246 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0687` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0688` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0689` | 5 | dono segreto | 649 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0690` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0691` | 5 | dono segreto | 25 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0692` | 5 | dono segreto | 647 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0693` | 5 | dono segreto | 648 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0694` | 5 | dono segreto | 376 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0695` | 5 | dono segreto | 386 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0696` | 5 | dono segreto | 483 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0697` | 5 | dono segreto | 484 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0698` | 5 | dono segreto | 487 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-5-0699` | 5 | dono segreto | 235 | 0 | Bianco, Nero e i loro seguiti | sì | no | letta, non ancora producibile |
| `EVT-6-0000` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0003` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0004` | 6 | dono segreto | 392 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0005` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0006` | 6 | dono segreto | 150 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0007` | 6 | dono segreto | 151 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0013` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0015` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0016` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0021` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0022` | 6 | dono segreto | 571 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0023` | 6 | dono segreto | 571 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0024` | 6 | dono segreto | 151 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0025` | 6 | dono segreto | 251 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0026` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0027` | 6 | dono segreto | 491 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0028` | 6 | dono segreto | 490 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0029` | 6 | dono segreto | 492 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0030` | 6 | dono segreto | 493 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0031` | 6 | dono segreto | 494 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0032` | 6 | dono segreto | 647 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0033` | 6 | dono segreto | 649 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0034` | 6 | dono segreto | 649 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0035` | 6 | dono segreto | 648 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0036` | 6 | dono segreto | 144 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0037` | 6 | dono segreto | 144 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0038` | 6 | dono segreto | 145 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0039` | 6 | dono segreto | 145 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0040` | 6 | dono segreto | 146 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0041` | 6 | dono segreto | 146 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0042` | 6 | dono segreto | 52 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0044` | 6 | dono segreto | 716 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0046` | 6 | dono segreto | 717 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0048` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0050` | 6 | dono segreto | 150 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0051` | 6 | dono segreto | 721 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0052` | 6 | dono segreto | 1 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0053` | 6 | dono segreto | 4 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0054` | 6 | dono segreto | 7 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0055` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0058` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0060` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0062` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0064` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0065` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0066` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0067` | 6 | dono segreto | 683 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0068` | 6 | dono segreto | 626 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0069` | 6 | dono segreto | 687 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0070` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0071` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0072` | 6 | dono segreto | 571 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0073` | 6 | dono segreto | 571 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0074` | 6 | dono segreto | 151 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0075` | 6 | dono segreto | 251 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0076` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0077` | 6 | dono segreto | 491 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0078` | 6 | dono segreto | 490 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0079` | 6 | dono segreto | 492 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0080` | 6 | dono segreto | 493 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0081` | 6 | dono segreto | 494 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0082` | 6 | dono segreto | 647 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0083` | 6 | dono segreto | 649 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0084` | 6 | dono segreto | 649 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0085` | 6 | dono segreto | 648 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0086` | 6 | dono segreto | 144 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0087` | 6 | dono segreto | 144 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0088` | 6 | dono segreto | 145 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0089` | 6 | dono segreto | 145 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0090` | 6 | dono segreto | 146 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0091` | 6 | dono segreto | 146 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0092` | 6 | dono segreto | 52 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0093` | 6 | dono segreto | 716 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0094` | 6 | dono segreto | 716 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0095` | 6 | dono segreto | 717 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0096` | 6 | dono segreto | 717 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0097` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0098` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0099` | 6 | dono segreto | 150 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0100` | 6 | dono segreto | 721 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0101` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0102` | 6 | dono segreto | 696 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0103` | 6 | dono segreto | 698 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0104` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0105` | 6 | dono segreto | 225 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0106` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0107` | 6 | dono segreto | 241 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0108` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0109` | 6 | dono segreto | 555 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0110` | 6 | dono segreto | 473 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0111` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0112` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0113` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0114` | 6 | dono segreto | 683 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0115` | 6 | dono segreto | 626 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0116` | 6 | dono segreto | 687 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0117` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0118` | 6 | dono segreto | 571 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0119` | 6 | dono segreto | 151 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0120` | 6 | dono segreto | 251 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0121` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0122` | 6 | dono segreto | 491 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0123` | 6 | dono segreto | 490 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0124` | 6 | dono segreto | 492 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0125` | 6 | dono segreto | 493 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0126` | 6 | dono segreto | 494 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0127` | 6 | dono segreto | 647 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0128` | 6 | dono segreto | 649 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0129` | 6 | dono segreto | 648 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0130` | 6 | dono segreto | 144 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0131` | 6 | dono segreto | 145 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0132` | 6 | dono segreto | 146 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0133` | 6 | dono segreto | 52 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0134` | 6 | dono segreto | 716 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0135` | 6 | dono segreto | 717 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0136` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0137` | 6 | dono segreto | 150 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0138` | 6 | dono segreto | 721 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0139` | 6 | dono segreto | 696 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0140` | 6 | dono segreto | 698 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0141` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0142` | 6 | dono segreto | 225 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0143` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0144` | 6 | dono segreto | 241 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0145` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0146` | 6 | dono segreto | 555 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0147` | 6 | dono segreto | 473 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0148` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0149` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0150` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0151` | 6 | dono segreto | 683 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0152` | 6 | dono segreto | 626 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0153` | 6 | dono segreto | 687 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0154` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0155` | 6 | dono segreto | 571 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0156` | 6 | dono segreto | 151 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0157` | 6 | dono segreto | 251 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0158` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0159` | 6 | dono segreto | 491 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0160` | 6 | dono segreto | 490 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0161` | 6 | dono segreto | 492 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0162` | 6 | dono segreto | 493 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0163` | 6 | dono segreto | 494 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0164` | 6 | dono segreto | 647 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0165` | 6 | dono segreto | 649 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0166` | 6 | dono segreto | 648 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0167` | 6 | dono segreto | 144 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0168` | 6 | dono segreto | 145 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0169` | 6 | dono segreto | 146 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0170` | 6 | dono segreto | 52 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0171` | 6 | dono segreto | 716 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0172` | 6 | dono segreto | 717 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0173` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0174` | 6 | dono segreto | 150 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0175` | 6 | dono segreto | 721 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0176` | 6 | dono segreto | 696 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0177` | 6 | dono segreto | 698 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0178` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0179` | 6 | dono segreto | 225 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0180` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0181` | 6 | dono segreto | 241 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0182` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0183` | 6 | dono segreto | 555 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0184` | 6 | dono segreto | 133 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0185` | 6 | dono segreto | 196 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0190` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0191` | 6 | dono segreto | 700 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0192` | 6 | dono segreto | 197 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0194` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0196` | 6 | dono segreto | 202 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0197` | 6 | dono segreto | 93 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0198` | 6 | dono segreto | 123 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0199` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0200` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0201` | 6 | dono segreto | 212 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0202` | 6 | dono segreto | 212 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0203` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0204` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0205` | 6 | dono segreto | 491 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0206` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0208` | 6 | dono segreto | 212 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0209` | 6 | dono segreto | 115 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0210` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0211` | 6 | dono segreto | 248 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0213` | 6 | dono segreto | 130 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0214` | 6 | dono segreto | 115 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0215` | 6 | dono segreto | 212 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0216` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0217` | 6 | dono segreto | 303 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0218` | 6 | dono segreto | 248 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0219` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0220` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0222` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0223` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0224` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0225` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0226` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0227` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0228` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0229` | 6 | dono segreto | 479 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0230` | 6 | dono segreto | 133 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0231` | 6 | dono segreto | 196 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0232` | 6 | dono segreto | 136 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0233` | 6 | dono segreto | 471 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0234` | 6 | dono segreto | 135 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0235` | 6 | dono segreto | 470 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0236` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0237` | 6 | dono segreto | 700 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0238` | 6 | dono segreto | 197 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0239` | 6 | dono segreto | 134 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0240` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0242` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0243` | 6 | dono segreto | 1 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0244` | 6 | dono segreto | 4 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0245` | 6 | dono segreto | 7 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0246` | 6 | dono segreto | 716 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0247` | 6 | dono segreto | 717 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0248` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0249` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0250` | 6 | dono segreto | 68 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0251` | 6 | dono segreto | 235 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0252` | 6 | dono segreto | 571 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0253` | 6 | dono segreto | 133 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0254` | 6 | dono segreto | 196 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0255` | 6 | dono segreto | 136 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0256` | 6 | dono segreto | 471 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0257` | 6 | dono segreto | 135 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0258` | 6 | dono segreto | 470 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0259` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0260` | 6 | dono segreto | 700 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0261` | 6 | dono segreto | 197 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0262` | 6 | dono segreto | 134 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0266` | 6 | dono segreto | 151 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0267` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0268` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0269` | 6 | dono segreto | 133 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0270` | 6 | dono segreto | 144 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0271` | 6 | dono segreto | 145 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0272` | 6 | dono segreto | 146 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0274` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0275` | 6 | dono segreto | 9 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0276` | 6 | dono segreto | 150 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0277` | 6 | dono segreto | 721 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0279` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0280` | 6 | dono segreto | 250 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0281` | 6 | dono segreto | 54 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0282` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0284` | 6 | dono segreto | 282 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0285` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0286` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0287` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0288` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0292` | 6 | dono segreto | 319 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0293` | 6 | dono segreto | 461 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0294` | 6 | dono segreto | 635 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0296` | 6 | dono segreto | 133 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0297` | 6 | dono segreto | 196 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0298` | 6 | dono segreto | 136 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0299` | 6 | dono segreto | 471 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0300` | 6 | dono segreto | 135 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0301` | 6 | dono segreto | 470 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0302` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0303` | 6 | dono segreto | 700 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0304` | 6 | dono segreto | 197 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0305` | 6 | dono segreto | 134 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0306` | 6 | dono segreto | 497 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0307` | 6 | dono segreto | 500 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0308` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0309` | 6 | dono segreto | 696 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0310` | 6 | dono segreto | 698 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0311` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0312` | 6 | dono segreto | 225 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0313` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0314` | 6 | dono segreto | 241 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0315` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0316` | 6 | dono segreto | 555 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0317` | 6 | dono segreto | 700 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0318` | 6 | dono segreto | 93 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0319` | 6 | dono segreto | 123 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0320` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0322` | 6 | dono segreto | 716 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0323` | 6 | dono segreto | 717 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0324` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0325` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0326` | 6 | dono segreto | 144 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0327` | 6 | dono segreto | 145 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0328` | 6 | dono segreto | 146 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0329` | 6 | dono segreto | 150 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0330` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0331` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0332` | 6 | dono segreto | 282 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0333` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0334` | 6 | dono segreto | 248 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0335` | 6 | dono segreto | 303 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0336` | 6 | dono segreto | 494 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0337` | 6 | dono segreto | 133 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0338` | 6 | dono segreto | 721 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0339` | 6 | dono segreto | 696 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0340` | 6 | dono segreto | 698 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0341` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0342` | 6 | dono segreto | 225 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0343` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0344` | 6 | dono segreto | 241 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0345` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0346` | 6 | dono segreto | 555 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0348` | 6 | dono segreto | 362 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0350` | 6 | dono segreto | 362 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0351` | 6 | dono segreto | 251 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0354` | 6 | dono segreto | 157 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0355` | 6 | dono segreto | 378 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0356` | 6 | dono segreto | 377 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0357` | 6 | dono segreto | 379 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0358` | 6 | dono segreto | 126 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0359` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0360` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0361` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0362` | 6 | dono segreto | 683 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0363` | 6 | dono segreto | 626 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0364` | 6 | dono segreto | 687 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0365` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0366` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0367` | 6 | dono segreto | 571 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0368` | 6 | dono segreto | 571 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0369` | 6 | dono segreto | 151 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0370` | 6 | dono segreto | 251 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0371` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0372` | 6 | dono segreto | 491 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0373` | 6 | dono segreto | 490 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0374` | 6 | dono segreto | 492 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0375` | 6 | dono segreto | 493 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0376` | 6 | dono segreto | 494 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0377` | 6 | dono segreto | 647 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0378` | 6 | dono segreto | 649 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0379` | 6 | dono segreto | 649 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0380` | 6 | dono segreto | 648 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0381` | 6 | dono segreto | 144 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0382` | 6 | dono segreto | 144 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0383` | 6 | dono segreto | 145 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0384` | 6 | dono segreto | 145 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0385` | 6 | dono segreto | 146 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0386` | 6 | dono segreto | 146 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0387` | 6 | dono segreto | 52 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0388` | 6 | dono segreto | 716 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0389` | 6 | dono segreto | 716 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0390` | 6 | dono segreto | 717 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0391` | 6 | dono segreto | 717 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0392` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0393` | 6 | dono segreto | 718 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0394` | 6 | dono segreto | 150 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0395` | 6 | dono segreto | 721 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0396` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0397` | 6 | dono segreto | 696 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0398` | 6 | dono segreto | 698 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0399` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0400` | 6 | dono segreto | 225 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0401` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0402` | 6 | dono segreto | 241 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0403` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0404` | 6 | dono segreto | 555 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0405` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0406` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0407` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0408` | 6 | dono segreto | 491 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0409` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0410` | 6 | dono segreto | 115 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0411` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0412` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0413` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0414` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0415` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0416` | 6 | dono segreto | 493 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0417` | 6 | dono segreto | 445 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0418` | 6 | dono segreto | 212 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0419` | 6 | dono segreto | 126 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0420` | 6 | dono segreto | 126 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0421` | 6 | dono segreto | 125 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0422` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0423` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0426` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0427` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0429` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0430` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0431` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0432` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0433` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0434` | 6 | dono segreto | 491 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0435` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0436` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0438` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0439` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0441` | 6 | dono segreto | 497 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0442` | 6 | dono segreto | 497 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0443` | 6 | dono segreto | 500 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0444` | 6 | dono segreto | 500 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0445` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0446` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0447` | 6 | dono segreto | 126 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0448` | 6 | dono segreto | 125 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0449` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0450` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0451` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0452` | 6 | dono segreto | 214 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0453` | 6 | dono segreto | 127 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0454` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0455` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0456` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0457` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0458` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0459` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0460` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0461` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0462` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0463` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0464` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0465` | 6 | dono segreto | 255 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0466` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0467` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0468` | 6 | dono segreto | 374 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0469` | 6 | dono segreto | 497 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0470` | 6 | dono segreto | 497 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0471` | 6 | dono segreto | 500 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0472` | 6 | dono segreto | 500 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0473` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0474` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0475` | 6 | dono segreto | 126 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0476` | 6 | dono segreto | 126 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0477` | 6 | dono segreto | 125 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0478` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0479` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0480` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0481` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0482` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0483` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0484` | 6 | dono segreto | 417 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0485` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0486` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0487` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0488` | 6 | dono segreto | 68 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0489` | 6 | dono segreto | 255 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0490` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0491` | 6 | dono segreto | 374 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0492` | 6 | dono segreto | 497 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0493` | 6 | dono segreto | 497 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0494` | 6 | dono segreto | 500 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0495` | 6 | dono segreto | 500 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0496` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0497` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0498` | 6 | dono segreto | 126 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0499` | 6 | dono segreto | 125 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0500` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0501` | 6 | dono segreto | 202 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0502` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0503` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0504` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0505` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0506` | 6 | dono segreto | 417 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0507` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0508` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0509` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0510` | 6 | dono segreto | 68 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0511` | 6 | dono segreto | 255 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0512` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0513` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0514` | 6 | dono segreto | 374 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0515` | 6 | dono segreto | 497 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0516` | 6 | dono segreto | 497 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0517` | 6 | dono segreto | 500 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0518` | 6 | dono segreto | 500 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0519` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0520` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0521` | 6 | dono segreto | 492 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0522` | 6 | dono segreto | 647 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0523` | 6 | dono segreto | 494 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0524` | 6 | dono segreto | 658 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0525` | 6 | dono segreto | 393 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0526` | 6 | dono segreto | 393 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0528` | 6 | dono segreto | 656 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0529` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0530` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0531` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0532` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0533` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0534` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0536` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0538` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0539` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0540` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0541` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0542` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0543` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0544` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0545` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0546` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0547` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0548` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0549` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0550` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0551` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0552` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0553` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0554` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0555` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0556` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0557` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0558` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0559` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0560` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0561` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0562` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0563` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0564` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0565` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0566` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0567` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0568` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0569` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0570` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0571` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0572` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0573` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0574` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0575` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0576` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0577` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0578` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0579` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0580` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0581` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0582` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0583` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0584` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0585` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0586` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0587` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0588` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0589` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0590` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0591` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0592` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0593` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0594` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0595` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0596` | 6 | dono segreto | 493 | 6 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0597` | 6 | dono segreto | 493 | 15 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0598` | 6 | dono segreto | 493 | 12 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0599` | 6 | dono segreto | 493 | 17 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0600` | 6 | dono segreto | 493 | 1 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0601` | 6 | dono segreto | 493 | 9 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0602` | 6 | dono segreto | 493 | 7 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0603` | 6 | dono segreto | 493 | 11 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0604` | 6 | dono segreto | 493 | 4 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0605` | 6 | dono segreto | 493 | 14 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0606` | 6 | dono segreto | 493 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0607` | 6 | dono segreto | 493 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0608` | 6 | dono segreto | 493 | 13 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0609` | 6 | dono segreto | 493 | 5 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0610` | 6 | dono segreto | 493 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0611` | 6 | dono segreto | 493 | 8 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0612` | 6 | dono segreto | 493 | 10 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0613` | 6 | dono segreto | 483 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0614` | 6 | dono segreto | 487 | 1 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0615` | 6 | dono segreto | 383 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0616` | 6 | dono segreto | 382 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0618` | 6 | dono segreto | 484 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0619` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0621` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0622` | 6 | dono segreto | 130 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0623` | 6 | dono segreto | 130 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0624` | 6 | dono segreto | 129 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0625` | 6 | dono segreto | 129 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0626` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0628` | 6 | dono segreto | 249 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0629` | 6 | dono segreto | 381 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0630` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0631` | 6 | dono segreto | 674 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0632` | 6 | dono segreto | 249 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0633` | 6 | dono segreto | 381 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0634` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0635` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0636` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0637` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0638` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0639` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0640` | 6 | dono segreto | 493 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0641` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0642` | 6 | dono segreto | 248 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0643` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0645` | 6 | dono segreto | 334 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0646` | 6 | dono segreto | 531 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0647` | 6 | dono segreto | 531 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0648` | 6 | dono segreto | 448 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0649` | 6 | dono segreto | 448 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0650` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0651` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0653` | 6 | dono segreto | 80 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0654` | 6 | dono segreto | 334 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0655` | 6 | dono segreto | 334 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0656` | 6 | dono segreto | 531 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0657` | 6 | dono segreto | 531 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0658` | 6 | dono segreto | 448 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0659` | 6 | dono segreto | 448 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0660` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0661` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0662` | 6 | dono segreto | 80 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0663` | 6 | dono segreto | 80 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0664` | 6 | dono segreto | 334 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0665` | 6 | dono segreto | 334 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0666` | 6 | dono segreto | 531 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0667` | 6 | dono segreto | 531 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0668` | 6 | dono segreto | 448 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0669` | 6 | dono segreto | 448 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0670` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0671` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0672` | 6 | dono segreto | 80 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0673` | 6 | dono segreto | 80 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0674` | 6 | dono segreto | 334 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0675` | 6 | dono segreto | 334 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0676` | 6 | dono segreto | 531 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0677` | 6 | dono segreto | 531 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0678` | 6 | dono segreto | 448 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0679` | 6 | dono segreto | 448 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0680` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0681` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0682` | 6 | dono segreto | 80 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0683` | 6 | dono segreto | 80 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0684` | 6 | dono segreto | 334 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0685` | 6 | dono segreto | 334 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0686` | 6 | dono segreto | 531 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0687` | 6 | dono segreto | 531 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0688` | 6 | dono segreto | 448 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0689` | 6 | dono segreto | 448 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0690` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0691` | 6 | dono segreto | 302 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0692` | 6 | dono segreto | 80 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0693` | 6 | dono segreto | 80 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0694` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0695` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0696` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0697` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0698` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0699` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0700` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0701` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0702` | 6 | dono segreto | 371 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0703` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0704` | 6 | dono segreto | 318 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0705` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0706` | 6 | dono segreto | 322 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0707` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0708` | 6 | dono segreto | 280 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0709` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0710` | 6 | dono segreto | 333 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0711` | 6 | dono segreto | 255 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0712` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0713` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0714` | 6 | dono segreto | 374 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0715` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0716` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0717` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0718` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0719` | 6 | dono segreto | 214 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0720` | 6 | dono segreto | 214 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0722` | 6 | dono segreto | 310 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0723` | 6 | dono segreto | 248 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0724` | 6 | dono segreto | 248 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0725` | 6 | dono segreto | 127 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0726` | 6 | dono segreto | 127 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0728` | 6 | dono segreto | 229 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0730` | 6 | dono segreto | 306 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0731` | 6 | dono segreto | 385 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0732` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0733` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0734` | 6 | dono segreto | 491 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0735` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0736` | 6 | dono segreto | 417 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0737` | 6 | dono segreto | 647 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0738` | 6 | dono segreto | 492 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0739` | 6 | dono segreto | 264 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0740` | 6 | dono segreto | 264 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0741` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0742` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0743` | 6 | dono segreto | 417 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0744` | 6 | dono segreto | 384 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0745` | 6 | dono segreto | 490 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0746` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0747` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0748` | 6 | dono segreto | 25 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0749` | 6 | dono segreto | 382 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0750` | 6 | dono segreto | 383 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0751` | 6 | dono segreto | 483 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0752` | 6 | dono segreto | 484 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0753` | 6 | dono segreto | 487 | 1 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0754` | 6 | dono segreto | 646 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0755` | 6 | dono segreto | 493 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0756` | 6 | dono segreto | 720 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0757` | 6 | dono segreto | 130 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0758` | 6 | dono segreto | 130 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0759` | 6 | dono segreto | 151 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0760` | 6 | dono segreto | 255 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0761` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0762` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0763` | 6 | dono segreto | 374 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0764` | 6 | dono segreto | 125 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0765` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0766` | 6 | dono segreto | 666 | 19 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0767` | 6 | dono segreto | 214 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0768` | 6 | dono segreto | 127 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0769` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0770` | 6 | dono segreto | 710 | 3 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0771` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0772` | 6 | dono segreto | 94 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0773` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0774` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0775` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0776` | 6 | dono segreto | 6 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0777` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0778` | 6 | dono segreto | 149 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0779` | 6 | dono segreto | 719 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0780` | 6 | dono segreto | 255 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0781` | 6 | dono segreto | 666 | 18 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0782` | 6 | dono segreto | 374 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0783` | 6 | dono segreto | 497 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0784` | 6 | dono segreto | 500 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0785` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-6-0786` | 6 | dono segreto | 503 | 0 | X, Y, Rubino Omega e Zaffiro Alpha | sì | no | letta, non ancora producibile |
| `EVT-7-0000` | 7 | dono segreto | 129 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0003` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0005` | 7 | dono segreto | 802 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0006` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0007` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0010` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0011` | 7 | dono segreto | 6 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0012` | 7 | dono segreto | 59 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0014` | 7 | dono segreto | 802 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0015` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0016` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0017` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0018` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0019` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0020` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0021` | 7 | dono segreto | 773 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0022` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0023` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0024` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0025` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0026` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0027` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0028` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0029` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0030` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0031` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0032` | 7 | dono segreto | 485 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0033` | 7 | dono segreto | 486 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0034` | 7 | dono segreto | 485 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0035` | 7 | dono segreto | 486 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0036` | 7 | dono segreto | 716 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0037` | 7 | dono segreto | 717 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0038` | 7 | dono segreto | 716 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0039` | 7 | dono segreto | 717 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0040` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0041` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0042` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0043` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0044` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0045` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0046` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0047` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0048` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0049` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0050` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0051` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0052` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0053` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0054` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0055` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0056` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0057` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0058` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0059` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0060` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0061` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0065` | 7 | dono segreto | 648 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0067` | 7 | dono segreto | 142 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0070` | 7 | dono segreto | 446 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0072` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0074` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0075` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0076` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0077` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0078` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0082` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0084` | 7 | dono segreto | 745 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0085` | 7 | dono segreto | 758 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0086` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0087` | 7 | dono segreto | 6 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0088` | 7 | dono segreto | 802 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0089` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0090` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0091` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0092` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0093` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0094` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0095` | 7 | dono segreto | 773 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0096` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0097` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0098` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0099` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0100` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0101` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0102` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0103` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0104` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0105` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0106` | 7 | dono segreto | 485 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0107` | 7 | dono segreto | 486 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0108` | 7 | dono segreto | 485 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0109` | 7 | dono segreto | 486 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0110` | 7 | dono segreto | 716 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0111` | 7 | dono segreto | 717 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0112` | 7 | dono segreto | 716 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0113` | 7 | dono segreto | 717 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0114` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0115` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0116` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0117` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0118` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0119` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0120` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0121` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0122` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0123` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0124` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0125` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0126` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0127` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0128` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0129` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0130` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0131` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0132` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0133` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0134` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0135` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0136` | 7 | dono segreto | 803 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0137` | 7 | dono segreto | 807 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0138` | 7 | dono segreto | 791 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0139` | 7 | dono segreto | 792 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0140` | 7 | dono segreto | 446 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0141` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0142` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0143` | 7 | dono segreto | 778 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0144` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0145` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0146` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0147` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0148` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0149` | 7 | dono segreto | 786 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0150` | 7 | dono segreto | 787 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0151` | 7 | dono segreto | 788 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0152` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0153` | 7 | dono segreto | 517 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0154` | 7 | dono segreto | 745 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0155` | 7 | dono segreto | 758 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0156` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0157` | 7 | dono segreto | 802 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0158` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0159` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0160` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0161` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0162` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0163` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0164` | 7 | dono segreto | 773 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0165` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0166` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0167` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0168` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0169` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0170` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0171` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0172` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0173` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0174` | 7 | dono segreto | 485 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0175` | 7 | dono segreto | 486 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0176` | 7 | dono segreto | 485 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0177` | 7 | dono segreto | 486 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0178` | 7 | dono segreto | 716 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0179` | 7 | dono segreto | 717 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0180` | 7 | dono segreto | 716 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0181` | 7 | dono segreto | 717 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0182` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0183` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0184` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0185` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0186` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0187` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0188` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0189` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0190` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0191` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0192` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0193` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0194` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0195` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0196` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0197` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0198` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0199` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0200` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0201` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0202` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0203` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0204` | 7 | dono segreto | 803 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0205` | 7 | dono segreto | 807 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0206` | 7 | dono segreto | 791 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0207` | 7 | dono segreto | 792 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0208` | 7 | dono segreto | 446 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0209` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0210` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0211` | 7 | dono segreto | 778 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0212` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0213` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0214` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0215` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0216` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0217` | 7 | dono segreto | 786 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0218` | 7 | dono segreto | 787 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0219` | 7 | dono segreto | 788 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0220` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0221` | 7 | dono segreto | 517 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0222` | 7 | dono segreto | 745 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0223` | 7 | dono segreto | 758 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0224` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0225` | 7 | dono segreto | 802 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0226` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0227` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0228` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0229` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0230` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0231` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0232` | 7 | dono segreto | 773 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0233` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0234` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0235` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0236` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0237` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0238` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0239` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0240` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0241` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0242` | 7 | dono segreto | 485 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0243` | 7 | dono segreto | 486 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0244` | 7 | dono segreto | 485 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0245` | 7 | dono segreto | 486 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0246` | 7 | dono segreto | 716 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0247` | 7 | dono segreto | 717 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0248` | 7 | dono segreto | 716 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0249` | 7 | dono segreto | 717 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0250` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0251` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0252` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0253` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0254` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0255` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0256` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0257` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0258` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0259` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0260` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0261` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0262` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0263` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0264` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0265` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0266` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0267` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0268` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0269` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0270` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0271` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0272` | 7 | dono segreto | 803 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0273` | 7 | dono segreto | 807 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0274` | 7 | dono segreto | 791 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0275` | 7 | dono segreto | 792 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0276` | 7 | dono segreto | 446 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0277` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0278` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0279` | 7 | dono segreto | 778 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0280` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0281` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0282` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0283` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0284` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0285` | 7 | dono segreto | 786 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0286` | 7 | dono segreto | 787 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0287` | 7 | dono segreto | 788 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0288` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0289` | 7 | dono segreto | 517 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0291` | 7 | dono segreto | 133 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0292` | 7 | dono segreto | 25 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0294` | 7 | dono segreto | 68 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0295` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0303` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0304` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0305` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0306` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0307` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0308` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0309` | 7 | dono segreto | 6 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0310` | 7 | dono segreto | 25 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0311` | 7 | dono segreto | 802 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0312` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0313` | 7 | dono segreto | 196 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0314` | 7 | dono segreto | 136 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0315` | 7 | dono segreto | 471 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0316` | 7 | dono segreto | 135 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0317` | 7 | dono segreto | 470 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0318` | 7 | dono segreto | 700 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0319` | 7 | dono segreto | 197 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0320` | 7 | dono segreto | 134 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0321` | 7 | dono segreto | 494 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0322` | 7 | dono segreto | 385 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0324` | 7 | dono segreto | 776 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0325` | 7 | dono segreto | 37 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0326` | 7 | dono segreto | 151 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0327` | 7 | dono segreto | 151 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0328` | 7 | dono segreto | 6 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0329` | 7 | dono segreto | 393 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0330` | 7 | dono segreto | 448 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0331` | 7 | dono segreto | 773 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0334` | 7 | dono segreto | 776 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0335` | 7 | dono segreto | 762 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0336` | 7 | dono segreto | 37 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0337` | 7 | dono segreto | 6 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0338` | 7 | dono segreto | 448 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0339` | 7 | dono segreto | 393 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0340` | 7 | dono segreto | 151 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0341` | 7 | dono segreto | 778 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0342` | 7 | dono segreto | 25 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0343` | 7 | dono segreto | 778 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0345` | 7 | dono segreto | 25 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0346` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0347` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0348` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0349` | 7 | dono segreto | 490 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0350` | 7 | dono segreto | 648 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0351` | 7 | dono segreto | 720 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0352` | 7 | dono segreto | 479 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0353` | 7 | dono segreto | 493 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0354` | 7 | dono segreto | 764 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0355` | 7 | dono segreto | 133 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0356` | 7 | dono segreto | 25 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0357` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0358` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0359` | 7 | dono segreto | 803 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0361` | 7 | dono segreto | 169 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0366` | 7 | dono segreto | 222 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0368` | 7 | dono segreto | 25 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0369` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0370` | 7 | dono segreto | 492 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0371` | 7 | dono segreto | 25 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0372` | 7 | dono segreto | 807 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0374` | 7 | dono segreto | 385 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0375` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0376` | 7 | dono segreto | 807 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0377` | 7 | dono segreto | 25 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0378` | 7 | dono segreto | 764 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0379` | 7 | dono segreto | 133 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0380` | 7 | dono segreto | 31 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0382` | 7 | dono segreto | 791 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0383` | 7 | dono segreto | 792 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0384` | 7 | dono segreto | 446 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0385` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0386` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0387` | 7 | dono segreto | 778 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0388` | 7 | dono segreto | 786 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0389` | 7 | dono segreto | 787 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0390` | 7 | dono segreto | 788 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0391` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0392` | 7 | dono segreto | 517 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0393` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0394` | 7 | dono segreto | 37 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0398` | 7 | dono segreto | 780 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0399` | 7 | dono segreto | 704 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0400` | 7 | dono segreto | 747 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0401` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0402` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0403` | 7 | dono segreto | 776 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0404` | 7 | dono segreto | 151 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0405` | 7 | dono segreto | 196 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0406` | 7 | dono segreto | 136 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0407` | 7 | dono segreto | 471 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0408` | 7 | dono segreto | 135 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0409` | 7 | dono segreto | 470 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0410` | 7 | dono segreto | 700 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0411` | 7 | dono segreto | 197 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0412` | 7 | dono segreto | 134 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0413` | 7 | dono segreto | 776 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0414` | 7 | dono segreto | 37 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0415` | 7 | dono segreto | 762 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0416` | 7 | dono segreto | 773 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0417` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0418` | 7 | dono segreto | 778 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0419` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0420` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0421` | 7 | dono segreto | 802 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0422` | 7 | dono segreto | 393 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0423` | 7 | dono segreto | 6 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0424` | 7 | dono segreto | 448 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0425` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0426` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0427` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0428` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0429` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0430` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0431` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0432` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0433` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0434` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0435` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0436` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0437` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0438` | 7 | dono segreto | 803 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0439` | 7 | dono segreto | 491 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0440` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0441` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0442` | 7 | dono segreto | 25 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0443` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0444` | 7 | dono segreto | 492 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0445` | 7 | dono segreto | 490 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0446` | 7 | dono segreto | 376 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0447` | 7 | dono segreto | 807 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0448` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0449` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0450` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0451` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0452` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0453` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0454` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0455` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0456` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0457` | 7 | dono segreto | 791 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0458` | 7 | dono segreto | 792 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0459` | 7 | dono segreto | 800 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0460` | 7 | dono segreto | 446 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0461` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0462` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0463` | 7 | dono segreto | 778 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0464` | 7 | dono segreto | 786 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0465` | 7 | dono segreto | 787 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0466` | 7 | dono segreto | 788 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0467` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0468` | 7 | dono segreto | 517 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0469` | 7 | dono segreto | 745 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0470` | 7 | dono segreto | 758 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0471` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0472` | 7 | dono segreto | 6 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0473` | 7 | dono segreto | 802 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0474` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0475` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0476` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0477` | 7 | dono segreto | 25 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0478` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0479` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0480` | 7 | dono segreto | 773 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0481` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0482` | 7 | dono segreto | 251 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0483` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0484` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0485` | 7 | dono segreto | 483 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0486` | 7 | dono segreto | 484 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0487` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0488` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0489` | 7 | dono segreto | 243 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0490` | 7 | dono segreto | 244 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0491` | 7 | dono segreto | 485 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0492` | 7 | dono segreto | 486 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0493` | 7 | dono segreto | 485 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0494` | 7 | dono segreto | 486 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0495` | 7 | dono segreto | 716 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0496` | 7 | dono segreto | 717 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0497` | 7 | dono segreto | 716 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0498` | 7 | dono segreto | 717 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0499` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0500` | 7 | dono segreto | 718 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0501` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0502` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0503` | 7 | dono segreto | 641 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0504` | 7 | dono segreto | 642 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0505` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0506` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0507` | 7 | dono segreto | 383 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0508` | 7 | dono segreto | 382 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0509` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0510` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0511` | 7 | dono segreto | 381 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0512` | 7 | dono segreto | 380 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0513` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0514` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0515` | 7 | dono segreto | 643 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0516` | 7 | dono segreto | 644 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0517` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0518` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0519` | 7 | dono segreto | 250 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0520` | 7 | dono segreto | 249 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0521` | 7 | dono segreto | 803 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0522` | 7 | dono segreto | 807 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0523` | 7 | dono segreto | 791 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0524` | 7 | dono segreto | 792 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0525` | 7 | dono segreto | 446 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0526` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0527` | 7 | dono segreto | 744 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0528` | 7 | dono segreto | 778 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0529` | 7 | dono segreto | 25 | 2 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0530` | 7 | dono segreto | 25 | 3 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0531` | 7 | dono segreto | 25 | 4 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0532` | 7 | dono segreto | 25 | 5 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0533` | 7 | dono segreto | 25 | 6 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0534` | 7 | dono segreto | 786 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0535` | 7 | dono segreto | 787 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0536` | 7 | dono segreto | 788 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0537` | 7 | dono segreto | 785 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0538` | 7 | dono segreto | 517 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0540` | 7 | dono segreto | 25 | 7 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0543` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0544` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0546` | 7 | dono segreto | 658 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0547` | 7 | dono segreto | 801 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0548` | 7 | dono segreto | 25 | 7 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0549` | 7 | dono segreto | 724 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0550` | 7 | dono segreto | 727 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0551` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0552` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0553` | 7 | dono segreto | 730 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0554` | 7 | dono segreto | 658 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0555` | 7 | dono segreto | 801 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0556` | 7 | dono segreto | 25 | 7 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0557` | 7 | dono segreto | 724 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0558` | 7 | dono segreto | 727 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0559` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0560` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0561` | 7 | dono segreto | 730 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0562` | 7 | dono segreto | 658 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0563` | 7 | dono segreto | 801 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0564` | 7 | dono segreto | 25 | 7 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0565` | 7 | dono segreto | 724 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0566` | 7 | dono segreto | 727 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0567` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0568` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0569` | 7 | dono segreto | 730 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0570` | 7 | dono segreto | 658 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0571` | 7 | dono segreto | 801 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0572` | 7 | dono segreto | 25 | 7 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0573` | 7 | dono segreto | 724 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0574` | 7 | dono segreto | 727 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0575` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0576` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0577` | 7 | dono segreto | 730 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0578` | 7 | dono segreto | 658 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0579` | 7 | dono segreto | 801 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0580` | 7 | dono segreto | 25 | 7 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0581` | 7 | dono segreto | 724 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0582` | 7 | dono segreto | 727 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0583` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0584` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0585` | 7 | dono segreto | 730 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0586` | 7 | dono segreto | 658 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0587` | 7 | dono segreto | 801 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0588` | 7 | dono segreto | 25 | 7 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0589` | 7 | dono segreto | 724 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0590` | 7 | dono segreto | 727 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0591` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0592` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0593` | 7 | dono segreto | 730 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0594` | 7 | dono segreto | 658 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0595` | 7 | dono segreto | 801 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0596` | 7 | dono segreto | 25 | 7 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0597` | 7 | dono segreto | 724 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0598` | 7 | dono segreto | 727 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0599` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0600` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0601` | 7 | dono segreto | 730 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0602` | 7 | dono segreto | 658 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0603` | 7 | dono segreto | 801 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0604` | 7 | dono segreto | 25 | 7 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0605` | 7 | dono segreto | 724 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0606` | 7 | dono segreto | 727 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0607` | 7 | dono segreto | 765 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0608` | 7 | dono segreto | 766 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0609` | 7 | dono segreto | 730 | 0 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0610` | 7 | dono segreto | 658 | 1 | Sole, Luna, UltraSole e UltraLuna | sì | no | letta, non ancora producibile |
| `EVT-7-0611` | 7 | dono segreto | 113 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0612` | 7 | dono segreto | 150 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0613` | 7 | dono segreto | 98 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0614` | 7 | dono segreto | 133 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0615` | 7 | dono segreto | 25 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0616` | 7 | dono segreto | 150 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0617` | 7 | dono segreto | 150 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0618` | 7 | dono segreto | 133 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0619` | 7 | dono segreto | 25 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0620` | 7 | dono segreto | 150 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0621` | 7 | dono segreto | 808 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0622` | 7 | dono segreto | 809 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0623` | 7 | dono segreto | 24 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0624` | 7 | dono segreto | 151 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-7-0625` | 7 | dono segreto | 808 | 0 | Let's Go Pikachu ed Eevee | no | no | letta, non ancora producibile |
| `EVT-8-0000` | 8 | dono segreto | 1 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0001` | 8 | dono segreto | 1 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0002` | 8 | dono segreto | 4 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0003` | 8 | dono segreto | 4 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0004` | 8 | dono segreto | 7 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0005` | 8 | dono segreto | 7 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0006` | 8 | dono segreto | 25 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0007` | 8 | dono segreto | 25 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0008` | 8 | dono segreto | 801 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0009` | 8 | dono segreto | 801 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0010` | 8 | dono segreto | 133 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0011` | 8 | dono segreto | 133 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0012` | 8 | dono segreto | 479 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0013` | 8 | dono segreto | 479 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0014` | 8 | dono segreto | 172 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0015` | 8 | dono segreto | 172 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0016` | 8 | dono segreto | 810 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0017` | 8 | dono segreto | 813 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0018` | 8 | dono segreto | 816 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0019` | 8 | dono segreto | 807 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0020` | 8 | dono segreto | 809 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0021` | 8 | dono segreto | 1 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0022` | 8 | dono segreto | 7 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0023` | 8 | dono segreto | 647 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0024` | 8 | dono segreto | 133 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0025` | 8 | dono segreto | 133 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0026` | 8 | dono segreto | 25 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0027` | 8 | dono segreto | 25 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0028` | 8 | dono segreto | 143 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0029` | 8 | dono segreto | 251 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0030` | 8 | dono segreto | 893 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0031` | 8 | dono segreto | 893 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0032` | 8 | dono segreto | 839 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0033` | 8 | dono segreto | 131 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0034` | 8 | dono segreto | 133 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0035` | 8 | dono segreto | 25 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0036` | 8 | dono segreto | 423 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0037` | 8 | dono segreto | 868 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0038` | 8 | dono segreto | 868 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0039` | 8 | dono segreto | 868 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0040` | 8 | dono segreto | 868 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0041` | 8 | dono segreto | 113 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0042` | 8 | dono segreto | 868 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0043` | 8 | dono segreto | 868 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0044` | 8 | dono segreto | 649 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0045` | 8 | dono segreto | 721 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0046` | 8 | dono segreto | 802 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0047` | 8 | dono segreto | 324 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0048` | 8 | dono segreto | 440 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0049` | 8 | dono segreto | 302 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0050` | 8 | dono segreto | 35 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0051` | 8 | dono segreto | 380 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0052` | 8 | dono segreto | 385 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0053` | 8 | dono segreto | 483 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0054` | 8 | dono segreto | 484 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0055` | 8 | dono segreto | 25 | 9 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0056` | 8 | dono segreto | 882 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0057` | 8 | dono segreto | 149 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0058` | 8 | dono segreto | 94 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0059` | 8 | dono segreto | 865 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0060` | 8 | dono segreto | 448 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0061` | 8 | dono segreto | 35 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0062` | 8 | dono segreto | 233 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0063` | 8 | dono segreto | 893 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0064` | 8 | dono segreto | 849 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0065` | 8 | dono segreto | 839 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0066` | 8 | dono segreto | 251 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0067` | 8 | dono segreto | 893 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0068` | 8 | dono segreto | 6 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0069` | 8 | dono segreto | 882 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0070` | 8 | dono segreto | 423 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0071` | 8 | dono segreto | 854 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0072` | 8 | dono segreto | 649 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0073` | 8 | dono segreto | 721 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0074` | 8 | dono segreto | 802 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0075` | 8 | dono segreto | 6 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0076` | 8 | dono segreto | 591 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0077` | 8 | dono segreto | 649 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0078` | 8 | dono segreto | 721 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0079` | 8 | dono segreto | 802 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0080` | 8 | dono segreto | 474 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0081` | 8 | dono segreto | 251 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0082` | 8 | dono segreto | 893 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0083` | 8 | dono segreto | 893 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0084` | 8 | dono segreto | 861 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0085` | 8 | dono segreto | 52 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0086` | 8 | dono segreto | 122 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0087` | 8 | dono segreto | 77 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0088` | 8 | dono segreto | 222 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0089` | 8 | dono segreto | 52 | 2 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0090` | 8 | dono segreto | 25 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0091` | 8 | dono segreto | 25 | 2 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0092` | 8 | dono segreto | 25 | 3 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0093` | 8 | dono segreto | 25 | 4 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0094` | 8 | dono segreto | 25 | 5 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0095` | 8 | dono segreto | 25 | 6 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0096` | 8 | dono segreto | 25 | 7 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0097` | 8 | dono segreto | 25 | 9 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0098` | 8 | dono segreto | 25 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0099` | 8 | dono segreto | 25 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0100` | 8 | dono segreto | 888 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0101` | 8 | dono segreto | 889 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0102` | 8 | dono segreto | 1 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0103` | 8 | dono segreto | 7 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0104` | 8 | dono segreto | 890 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0105` | 8 | dono segreto | 494 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0106` | 8 | dono segreto | 151 | 0 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0107` | 8 | dono segreto | 146 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0108` | 8 | dono segreto | 146 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0109` | 8 | dono segreto | 144 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0110` | 8 | dono segreto | 144 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0111` | 8 | dono segreto | 145 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0112` | 8 | dono segreto | 145 | 1 | Spada e Scudo | no | no | letta, non ancora producibile |
| `EVT-8-0113` | 8 | dono segreto | 722 | 0 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0114` | 8 | dono segreto | 155 | 0 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0115` | 8 | dono segreto | 501 | 0 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0116` | 8 | dono segreto | 905 | 0 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0117` | 8 | dono segreto | 440 | 0 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0118` | 8 | dono segreto | 35 | 0 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0119` | 8 | dono segreto | 393 | 0 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0120` | 8 | dono segreto | 58 | 1 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0121` | 8 | dono segreto | 486 | 0 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0122` | 8 | dono segreto | 393 | 0 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0123` | 8 | dono segreto | 58 | 1 | Leggende Arceus | no | no | letta, non ancora producibile |
| `EVT-8-0124` | 8 | dono segreto | 387 | 0 | Diamante Lucente e Perla Splendente | no | no | letta, non ancora producibile |
| `EVT-8-0125` | 8 | dono segreto | 390 | 0 | Diamante Lucente e Perla Splendente | no | no | letta, non ancora producibile |
| `EVT-8-0126` | 8 | dono segreto | 393 | 0 | Diamante Lucente e Perla Splendente | no | no | letta, non ancora producibile |
| `EVT-8-0127` | 8 | dono segreto | 490 | 0 | Diamante Lucente e Perla Splendente | no | no | letta, non ancora producibile |
| `EVT-8-0128` | 8 | dono segreto | 440 | 0 | Diamante Lucente e Perla Splendente | no | no | letta, non ancora producibile |
| `EVT-8-0129` | 8 | dono segreto | 35 | 0 | Diamante Lucente e Perla Splendente | no | no | letta, non ancora producibile |
| `EVT-8-0130` | 8 | dono segreto | 393 | 0 | Diamante Lucente e Perla Splendente | no | no | letta, non ancora producibile |
| `EVT-8-0131` | 8 | dono segreto | 486 | 0 | Diamante Lucente e Perla Splendente | no | no | letta, non ancora producibile |
| `EVT-8-0132` | 8 | dono segreto | 393 | 0 | Diamante Lucente e Perla Splendente | no | no | letta, non ancora producibile |
| `EVT-8-0133` | 8 | dono segreto | 490 | 0 | Diamante Lucente e Perla Splendente | no | no | letta, non ancora producibile |
| `EVT-9-0000` | 9 | dono segreto | 669 | 3 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0001` | 9 | dono segreto | 669 | 3 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0002` | 9 | dono segreto | 669 | 2 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0003` | 9 | dono segreto | 669 | 2 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0004` | 9 | dono segreto | 669 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0005` | 9 | dono segreto | 669 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0006` | 9 | dono segreto | 669 | 4 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0007` | 9 | dono segreto | 669 | 4 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0008` | 9 | dono segreto | 669 | 1 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0009` | 9 | dono segreto | 669 | 1 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0010` | 9 | dono segreto | 130 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0011` | 9 | dono segreto | 861 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0012` | 9 | dono segreto | 25 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0013` | 9 | dono segreto | 25 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0014` | 9 | dono segreto | 437 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0015` | 9 | dono segreto | 935 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0016` | 9 | dono segreto | 921 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0017` | 9 | dono segreto | 1006 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0018` | 9 | dono segreto | 1005 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0019` | 9 | dono segreto | 986 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0020` | 9 | dono segreto | 987 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0021` | 9 | dono segreto | 992 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0022` | 9 | dono segreto | 993 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0023` | 9 | dono segreto | 995 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0024` | 9 | dono segreto | 985 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0025` | 9 | dono segreto | 143 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0026` | 9 | dono segreto | 663 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0027` | 9 | dono segreto | 133 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0028` | 9 | dono segreto | 130 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0029` | 9 | dono segreto | 647 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0030` | 9 | dono segreto | 893 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0031` | 9 | dono segreto | 386 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0032` | 9 | dono segreto | 924 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0033` | 9 | dono segreto | 812 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0034` | 9 | dono segreto | 987 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0035` | 9 | dono segreto | 591 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0036` | 9 | dono segreto | 926 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0037` | 9 | dono segreto | 934 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0038` | 9 | dono segreto | 915 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0039` | 9 | dono segreto | 964 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0040` | 9 | dono segreto | 59 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0041` | 9 | dono segreto | 978 | 2 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0042` | 9 | dono segreto | 423 | 1 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0043` | 9 | dono segreto | 778 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0044` | 9 | dono segreto | 887 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0045` | 9 | dono segreto | 992 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0046` | 9 | dono segreto | 233 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0047` | 9 | dono segreto | 762 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0048` | 9 | dono segreto | 700 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0049` | 9 | dono segreto | 279 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0050` | 9 | dono segreto | 133 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0051` | 9 | dono segreto | 189 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0052` | 9 | dono segreto | 727 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0053` | 9 | dono segreto | 948 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0054` | 9 | dono segreto | 981 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0055` | 9 | dono segreto | 547 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0056` | 9 | dono segreto | 157 | 1 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0057` | 9 | dono segreto | 172 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0058` | 9 | dono segreto | 437 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0059` | 9 | dono segreto | 423 | 1 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0060` | 9 | dono segreto | 926 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0061` | 9 | dono segreto | 998 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0062` | 9 | dono segreto | 987 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0063` | 9 | dono segreto | 448 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0064` | 9 | dono segreto | 647 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0065` | 9 | dono segreto | 893 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0066` | 9 | dono segreto | 386 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0067` | 9 | dono segreto | 132 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0068` | 9 | dono segreto | 233 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0069` | 9 | dono segreto | 25 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0070` | 9 | dono segreto | 25 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0071` | 9 | dono segreto | 571 | 1 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0072` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0073` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0074` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0075` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0076` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0077` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0078` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0079` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0080` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0081` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0082` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0083` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0084` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0085` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0086` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0087` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0088` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0089` | 9 | dono segreto | 151 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0090` | 9 | dono segreto | 6 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0091` | 9 | dono segreto | 975 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0092` | 9 | dono segreto | 966 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0093` | 9 | dono segreto | 999 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0094` | 9 | dono segreto | 491 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0095` | 9 | dono segreto | 448 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0096` | 9 | dono segreto | 923 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0097` | 9 | dono segreto | 906 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0098` | 9 | dono segreto | 912 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0099` | 9 | dono segreto | 909 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0100` | 9 | dono segreto | 1008 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0101` | 9 | dono segreto | 1007 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0102` | 9 | dono segreto | 1001 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0103` | 9 | dono segreto | 1002 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0104` | 9 | dono segreto | 1003 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0105` | 9 | dono segreto | 1004 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0106` | 9 | dono segreto | 906 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0107` | 9 | dono segreto | 909 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0108` | 9 | dono segreto | 912 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0109` | 9 | dono segreto | 648 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0110` | 9 | dono segreto | 924 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0111` | 9 | dono segreto | 926 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0112` | 9 | dono segreto | 445 | 0 | Scarlatto e Violetto | no | no | letta, non ancora producibile |
| `EVT-9-0113` | 9 | dono segreto | 531 | 0 | Leggende Z-A | no | no | letta, non ancora producibile |
| `EVT-9-0114` | 9 | dono segreto | 79 | 0 | Leggende Z-A | no | no | letta, non ancora producibile |
| `EVT-9-0115` | 9 | dono segreto | 280 | 0 | Leggende Z-A | no | no | letta, non ancora producibile |
| `EVT-9-0116` | 9 | dono segreto | 6 | 0 | Leggende Z-A | no | no | letta, non ancora producibile |
| `EVT-9-0117` | 9 | dono segreto | 152 | 0 | Leggende Z-A | no | no | letta, non ancora producibile |
| `EVT-9-0118` | 9 | dono segreto | 498 | 0 | Leggende Z-A | no | no | letta, non ancora producibile |
| `EVT-9-0119` | 9 | dono segreto | 158 | 0 | Leggende Z-A | no | no | letta, non ancora producibile |
| `EVT-9-0120` | 9 | dono segreto | 721 | 0 | Leggende Z-A | no | no | letta, non ancora producibile |
| `EVT-T-0000` | 3 | oggetto-distribuito | 380 | 0 | Distribuzioni in cui il dono era un oggetto: Biglietto Eone, Isola del Sud, Rubino, livello 50 | sì | no | censita, non ancora producibile |
| `EVT-T-0001` | 3 | oggetto-distribuito | 381 | 0 | Distribuzioni in cui il dono era un oggetto: Biglietto Eone, Isola del Sud, Zaffiro, livello 50 | sì | no | censita, non ancora producibile |
| `EVT-T-0002` | 3 | oggetto-distribuito | 380 | 0 | Distribuzioni in cui il dono era un oggetto: Biglietto Eone, Isola del Sud, Smeraldo, livello 50 | sì | no | censita, non ancora producibile |
| `EVT-T-0003` | 3 | oggetto-distribuito | 381 | 0 | Distribuzioni in cui il dono era un oggetto: Biglietto Eone, Isola del Sud, Smeraldo, livello 50 | sì | no | censita, non ancora producibile |
| `EVT-T-0004` | 3 | oggetto-distribuito | 151 | 0 | Distribuzioni in cui il dono era un oggetto: Carta Mare Antica, Isola Lontana, Smeraldo, livello 30 | sì | no | censita, non ancora producibile |
| `EVT-T-0005` | 3 | oggetto-distribuito | 249 | 0 | Distribuzioni in cui il dono era un oggetto: Biglietto Mistico, Rocca Ombelico, Smeraldo, livello 70 | sì | no | censita, non ancora producibile |
| `EVT-T-0006` | 3 | oggetto-distribuito | 250 | 0 | Distribuzioni in cui il dono era un oggetto: Biglietto Mistico, Rocca Ombelico, Smeraldo, livello 70 | sì | no | censita, non ancora producibile |
| `EVT-T-0007` | 3 | oggetto-distribuito | 386 | 3 | Distribuzioni in cui il dono era un oggetto: Biglietto Aurora, Isola Nascita, Smeraldo, livello 30 | sì | no | censita, non ancora producibile |
| `EVT-T-0008` | 3 | oggetto-distribuito | 249 | 0 | Distribuzioni in cui il dono era un oggetto: Biglietto Mistico, Rocca Ombelico, Rosso Fuoco e Verde Foglia, livello 70 | sì | no | censita, non ancora producibile |
| `EVT-T-0009` | 3 | oggetto-distribuito | 250 | 0 | Distribuzioni in cui il dono era un oggetto: Biglietto Mistico, Rocca Ombelico, Rosso Fuoco e Verde Foglia, livello 70 | sì | no | censita, non ancora producibile |
| `EVT-T-0010` | 3 | oggetto-distribuito | 386 | 1 | Distribuzioni in cui il dono era un oggetto: Biglietto Aurora, Isola Nascita, Rosso Fuoco, livello 30 | sì | no | censita, non ancora producibile |
| `EVT-T-0011` | 3 | oggetto-distribuito | 386 | 2 | Distribuzioni in cui il dono era un oggetto: Biglietto Aurora, Isola Nascita, Verde Foglia, livello 30 | sì | no | censita, non ancora producibile |
| `EVT-T-0012` | 4 | oggetto-distribuito | 491 | 0 | Distribuzioni in cui il dono era un oggetto: Tessera Membro, Isola Lunanova, Platino, livello 50 | sì | no | censita, non ancora producibile |
| `EVT-T-0013` | 4 | oggetto-distribuito | 492 | 0 | Distribuzioni in cui il dono era un oggetto: Lettera di Oak, Giardino Floreale, Platino, livello 30 | sì | no | censita, non ancora producibile |
| `EVT-T-0014` | 5 | oggetto-distribuito | 494 | 0 | Distribuzioni in cui il dono era un oggetto: Passo Liberta', Giardino Liberta', Nero e Bianco, livello 15 | sì | no | censita, non ancora producibile |
| `EVT-T-0015` | 3 | disco-bonus | 25 | 0 | Colosseum, disco bonus, solo Giappone: Colosseum Pikachu bonus gift | sì | no | censita, non ancora producibile |
| `EVT-T-0016` | 3 | disco-bonus | 251 | 0 | Colosseum, disco bonus, solo Giappone: Ageto Celebi bonus gift | sì | no | censita, non ancora producibile |
| `EVT-T-0017` | 3 | spinoff | 250 | 0 | Colosseum, premio del Monte Lotta: Ho-oh @ Mt. Battle | sì | no | censita, non ancora producibile |
| `EVT-T-0018` | 3 | spinoff | 196 | 0 | Colosseum, iniziali: Espeon | sì | no | censita, non ancora producibile |
| `EVT-T-0019` | 3 | spinoff | 197 | 0 | Colosseum, iniziali: Umbreon (Bite) | sì | no | censita, non ancora producibile |
| `EVT-T-0020` | 3 | spinoff | 311 | 0 | Colosseum, doni: Plusle @ In-game Trade | sì | no | censita, non ancora producibile |
| `EVT-T-0023` | 3 | spinoff | 153 | 0 | Colosseum, ombra: Bayleef: Cipher Peon Verde @ Shadow PKMN Lab | sì | no | censita, non ancora producibile |
| `EVT-T-0024` | 3 | spinoff | 153 | 0 | Colosseum, ombra: Bayleef: Cipher Peon Verde @ Realgam Tower | sì | no | censita, non ancora producibile |
| `EVT-T-0025` | 3 | spinoff | 153 | 0 | Colosseum, ombra: Bayleef: Cipher Peon Verde @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0027` | 3 | spinoff | 156 | 0 | Colosseum, ombra: Quilava: Cipher Peon Rosso @ Shadow PKMN Lab | sì | no | censita, non ancora producibile |
| `EVT-T-0028` | 3 | spinoff | 156 | 0 | Colosseum, ombra: Quilava: Cipher Peon Rosso @ Realgam Tower | sì | no | censita, non ancora producibile |
| `EVT-T-0029` | 3 | spinoff | 156 | 0 | Colosseum, ombra: Quilava: Cipher Peon Rosso @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0031` | 3 | spinoff | 159 | 0 | Colosseum, ombra: Croconaw: Cipher Peon Bluno @ Shadow PKMN Lab | sì | no | censita, non ancora producibile |
| `EVT-T-0032` | 3 | spinoff | 159 | 0 | Colosseum, ombra: Croconaw: Cipher Peon Bluno @ Realgam Tower | sì | no | censita, non ancora producibile |
| `EVT-T-0033` | 3 | spinoff | 159 | 0 | Colosseum, ombra: Croconaw: Cipher Peon Bluno @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0040` | 3 | spinoff | 193 | 0 | Colosseum, ombra: Yanma: Cipher Peon Nore @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0044` | 3 | spinoff | 223 | 0 | Colosseum, ombra: Remoraid: Miror B.Peon Reath @ Pyrite Cave | sì | no | censita, non ancora producibile |
| `EVT-T-0046` | 3 | spinoff | 226 | 0 | Colosseum, ombra: Mantine: Miror B.Peon Ferma @ Pyrite Cave | sì | no | censita, non ancora producibile |
| `EVT-T-0050` | 3 | spinoff | 333 | 0 | Colosseum, ombra: Swablu: Hunter Zalo @ Pyrite Cave | sì | no | censita, non ancora producibile |
| `EVT-T-0052` | 3 | spinoff | 185 | 0 | Colosseum, ombra: Sudowoodo: Cipher Admin Miror B. @ Deep Colosseum | sì | no | censita, non ancora producibile |
| `EVT-T-0053` | 3 | spinoff | 185 | 0 | Colosseum, ombra: Sudowoodo: Cipher Admin Miror B. @ Pyrite Cave | sì | no | censita, non ancora producibile |
| `EVT-T-0054` | 3 | spinoff | 237 | 0 | Colosseum, ombra: Hitmontop: Cipher Peon Skrub @ Agate Village | sì | no | censita, non ancora producibile |
| `EVT-T-0055` | 3 | spinoff | 237 | 0 | Colosseum, ombra: Hitmontop: Cipher Peon Skrub @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0056` | 3 | spinoff | 237 | 0 | Colosseum, ombra: Hitmontop: Cipher Peon Skrub @ Shadow PKMN Lab | sì | no | censita, non ancora producibile |
| `EVT-T-0057` | 3 | spinoff | 244 | 0 | Colosseum, ombra: Entei: Cipher Admin Dakim @ Realgam Tower | sì | no | censita, non ancora producibile |
| `EVT-T-0058` | 3 | spinoff | 244 | 0 | Colosseum, ombra: Entei: Cipher Admin Dakim @ Deep Colosseum | sì | no | censita, non ancora producibile |
| `EVT-T-0059` | 3 | spinoff | 244 | 0 | Colosseum, ombra: Entei: Cipher Admin Dakim @ Mt. Battle | sì | no | censita, non ancora producibile |
| `EVT-T-0061` | 3 | spinoff | 166 | 0 | Colosseum, ombra: Ledian: Cipher Peon Kloak @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0062` | 3 | spinoff | 245 | 0 | Colosseum, ombra: Suicune (Surf): Cipher Admin Venus @ Realgam Tower | sì | no | censita, non ancora producibile |
| `EVT-T-0063` | 3 | spinoff | 245 | 0 | Colosseum, ombra: Suicune (Hydro Pump): Cipher Admin Venus @ Deep Colosseum | sì | no | censita, non ancora producibile |
| `EVT-T-0064` | 3 | spinoff | 245 | 0 | Colosseum, ombra: Suicune (Surf): Cipher Admin Venus @ The Under | sì | no | censita, non ancora producibile |
| `EVT-T-0066` | 3 | spinoff | 207 | 0 | Colosseum, ombra: Gligar: Hunter Frena @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0068` | 3 | spinoff | 234 | 0 | Colosseum, ombra: Stantler: Chaser Liaks @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0070` | 3 | spinoff | 221 | 0 | Colosseum, ombra: Piloswine: Bodybuilder Lonia @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0072` | 3 | spinoff | 215 | 0 | Colosseum, ombra: Sneasel: Rider Nelis @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0075` | 3 | spinoff | 198 | 0 | Colosseum, ombra: Murkrow: Cipher Peon Lare @ Shadow PKMN Lab (Trainer drops from ceiling: can lose during play-through, rematch later) | sì | no | censita, non ancora producibile |
| `EVT-T-0080` | 3 | spinoff | 243 | 0 | Colosseum, ombra: Raikou: Cipher Admin Ein @ Realgam Tower | sì | no | censita, non ancora producibile |
| `EVT-T-0081` | 3 | spinoff | 243 | 0 | Colosseum, ombra: Raikou: Cipher Admin Ein @ Deep Colosseum | sì | no | censita, non ancora producibile |
| `EVT-T-0082` | 3 | spinoff | 243 | 0 | Colosseum, ombra: Raikou: Cipher Admin Ein @ Shadow PKMN Lab | sì | no | censita, non ancora producibile |
| `EVT-T-0084` | 3 | spinoff | 192 | 0 | Colosseum, ombra: Sunflora: Cipher Peon Baila @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0085` | 3 | spinoff | 225 | 0 | Colosseum, ombra: Delibird: Cipher Peon Arton @ Realgam Tower | sì | no | censita, non ancora producibile |
| `EVT-T-0086` | 3 | spinoff | 225 | 0 | Colosseum, ombra: Delibird: Cipher Peon Arton @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0087` | 3 | spinoff | 214 | 0 | Colosseum, ombra: Heracross: Cipher Peon Dioge @ Realgam Tower | sì | no | censita, non ancora producibile |
| `EVT-T-0088` | 3 | spinoff | 214 | 0 | Colosseum, ombra: Heracross: Cipher Peon Dioge @ Snagem Hideout (Trainer drops from ceiling: can lose during play-through, rematch later) | sì | no | censita, non ancora producibile |
| `EVT-T-0090` | 3 | spinoff | 227 | 0 | Colosseum, ombra: Skarmory: Snagem Head Gonzap @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0091` | 3 | spinoff | 241 | 0 | Colosseum, ombra: Miltank: Bodybuilder Jomas @ Tower Colosseum | sì | no | censita, non ancora producibile |
| `EVT-T-0092` | 3 | spinoff | 359 | 0 | Colosseum, ombra: Absol: Rider Delan @ Tower Colosseum | sì | no | censita, non ancora producibile |
| `EVT-T-0093` | 3 | spinoff | 229 | 0 | Colosseum, ombra: Houndoom: Cipher Peon Nella @ Tower Colosseum | sì | no | censita, non ancora producibile |
| `EVT-T-0094` | 3 | spinoff | 357 | 0 | Colosseum, ombra: Tropius: Cipher Peon Ston @ Tower Colosseum | sì | no | censita, non ancora producibile |
| `EVT-T-0095` | 3 | spinoff | 376 | 0 | Colosseum, ombra: Metagross: Cipher Nascour @ Tower Colosseum | sì | no | censita, non ancora producibile |
| `EVT-T-0096` | 3 | spinoff | 248 | 0 | Colosseum, ombra: Tyranitar: Cipher Head Evice @ Tower Colosseum | sì | no | censita, non ancora producibile |
| `EVT-T-0097` | 3 | spinoff | 235 | 0 | Colosseum, ombra: Smeargle: Team Snagem Biden @ Snagem Hideout | sì | no | censita, non ancora producibile |
| `EVT-T-0101` | 3 | spinoff | 133 | 0 | XD, doni: Eevee (Bite) | sì | no | censita, non ancora producibile |
| `EVT-T-0102` | 3 | spinoff | 152 | 0 | XD, doni: Chikorita | sì | no | censita, non ancora producibile |
| `EVT-T-0103` | 3 | spinoff | 155 | 0 | XD, doni: Cyndaquil | sì | no | censita, non ancora producibile |
| `EVT-T-0104` | 3 | spinoff | 158 | 0 | XD, doni: Totodile | sì | no | censita, non ancora producibile |
| `EVT-T-0106` | 3 | spinoff | 307 | 0 | XD, scambi: Meditite @ Pyrite Town | sì | no | censita, non ancora producibile |
| `EVT-T-0107` | 3 | spinoff | 213 | 0 | XD, scambi: Shuckle @ Pyrite Town | sì | no | censita, non ancora producibile |
| `EVT-T-0108` | 3 | spinoff | 246 | 0 | XD, scambi: Larvitar @ Pyrite Town | sì | no | censita, non ancora producibile |
| `EVT-T-0110` | 3 | spinoff | 37 | 0 | XD, ombra: Vulpix: Cipher Peon Mesin @ ONBS Building | sì | no | censita, non ancora producibile |
| `EVT-T-0112` | 3 | spinoff | 363 | 0 | XD, ombra: Spheal: Cipher Peon Blusix  @ Phenac City | sì | no | censita, non ancora producibile |
| `EVT-T-0114` | 3 | spinoff | 343 | 0 | XD, ombra: Baltoy: Cipher Peon Browsix  @ Phenac City | sì | no | censita, non ancora producibile |
| `EVT-T-0115` | 3 | spinoff | 179 | 0 | XD, ombra: Mareep: Cipher Peon Yellosix @ Cipher Lab | sì | no | censita, non ancora producibile |
| `EVT-T-0116` | 3 | spinoff | 179 | 0 | XD, ombra: Mareep: Cipher Peon Yellosix @ Phenac City | sì | no | censita, non ancora producibile |
| `EVT-T-0118` | 3 | spinoff | 316 | 0 | XD, ombra: Gulpin: Cipher Peon Purpsix @ Phenac City | sì | no | censita, non ancora producibile |
| `EVT-T-0120` | 3 | spinoff | 273 | 0 | XD, ombra: Seedot: Cipher Peon Greesix @ Phenac City | sì | no | censita, non ancora producibile |
| `EVT-T-0122` | 3 | spinoff | 322 | 0 | XD, ombra: Numel: Cipher Peon Solox @ Cipher Lab | sì | no | censita, non ancora producibile |
| `EVT-T-0123` | 3 | spinoff | 318 | 0 | XD, ombra: Carvanha: Cipher Peon Cabol @ Cipher Lab | sì | no | censita, non ancora producibile |
| `EVT-T-0128` | 3 | spinoff | 228 | 0 | XD, ombra: Houndour: Cipher Peon Resix @ Cipher Lab | sì | no | censita, non ancora producibile |
| `EVT-T-0129` | 3 | spinoff | 296 | 0 | XD, ombra: Makuhita: Cipher Peon Torkin @ ONBS Building | sì | no | censita, non ancora producibile |
| `EVT-T-0131` | 3 | spinoff | 280 | 0 | XD, ombra: Ralts: Cipher Peon Feldas @ ONBS Building | sì | no | censita, non ancora producibile |
| `EVT-T-0132` | 3 | spinoff | 303 | 0 | XD, ombra: Mawile: Cipher Cmdr Exol @ ONBS Building | sì | no | censita, non ancora producibile |
| `EVT-T-0138` | 3 | spinoff | 52 | 0 | XD, ombra: Meowth: Cipher Peon Fostin @ Phenac City | sì | no | censita, non ancora producibile |
| `EVT-T-0140` | 3 | spinoff | 88 | 0 | XD, ombra: Grimer: Cipher Peon Faltly @ Phenac Stadium | sì | no | censita, non ancora producibile |
| `EVT-T-0142` | 3 | spinoff | 337 | 0 | XD, ombra: Lunatone: Cipher Admin Snattle @ Phenac Stadium | sì | no | censita, non ancora producibile |
| `EVT-T-0158` | 3 | spinoff | 55 | 0 | XD, ombra: Golduck: Navigator Abson @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0159` | 3 | spinoff | 302 | 0 | XD, ombra: Sableye: Navigator Abson @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0162` | 3 | spinoff | 83 | 0 | XD, ombra: Farfetch'd: Cipher Admin Lovrina @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0163` | 3 | spinoff | 334 | 0 | XD, ombra: Altaria: Cipher Admin Lovrina @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0164` | 3 | spinoff | 115 | 0 | XD, ombra: Kangaskhan: Cipher Peon Litnar @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0166` | 3 | spinoff | 126 | 0 | XD, ombra: Magmar: Cipher Peon Grupel @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0167` | 3 | spinoff | 127 | 0 | XD, ombra: Pinsir: Cipher Peon Grupel @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0172` | 3 | spinoff | 108 | 0 | XD, ombra: Lickitung: Cipher Peon Geftal @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0173` | 3 | spinoff | 123 | 0 | XD, ombra: Scyther: Cipher Peon Leden @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0174` | 3 | spinoff | 113 | 0 | XD, ombra: Chansey: Cipher Peon Leden @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0175` | 3 | spinoff | 113 | 0 | XD, ombra: Chansey: Cipher Peon Leden @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0176` | 3 | spinoff | 338 | 0 | XD, ombra: Solrock: Cipher Admin Snattle @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0178` | 3 | spinoff | 125 | 0 | XD, ombra: Electabuzz: Cipher Admin Ardos @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0180` | 3 | spinoff | 143 | 0 | XD, ombra: Snorlax: Cipher Admin Ardos @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0184` | 3 | spinoff | 310 | 0 | XD, ombra: Manectric: Cipher Admin Eldes @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0185` | 3 | spinoff | 373 | 0 | XD, ombra: Salamence: Cipher Admin Eldes @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0188` | 3 | spinoff | 249 | 0 | XD, ombra: Lugia: Grand Master Greevil @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0189` | 3 | spinoff | 145 | 0 | XD, ombra: Zapdos: Grand Master Greevil @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0190` | 3 | spinoff | 146 | 0 | XD, ombra: Moltres: Grand Master Greevil @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0191` | 3 | spinoff | 144 | 0 | XD, ombra: Articuno: Grand Master Greevil @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0194` | 3 | spinoff | 103 | 0 | XD, ombra: Exeggutor: Grand Master Greevil @ Citadark Isle | sì | no | censita, non ancora producibile |
| `EVT-T-0195` | 3 | spinoff | 149 | 0 | XD, ombra: Dragonite: Wanderer Miror B. @ Gateon Port | sì | no | censita, non ancora producibile |
| `EVT-T-0199` | 4 | periferica | 25 | 0 | My Pokemon Ranch: Pikachu | sì | no | censita, non ancora producibile |
| `EVT-T-0200` | 4 | periferica | 37 | 0 | My Pokemon Ranch: Vulpix | sì | no | censita, non ancora producibile |
| `EVT-T-0202` | 4 | periferica | 108 | 0 | My Pokemon Ranch: Lickitung | sì | no | censita, non ancora producibile |
| `EVT-T-0203` | 4 | periferica | 114 | 0 | My Pokemon Ranch: Tangela | sì | no | censita, non ancora producibile |
| `EVT-T-0204` | 4 | periferica | 133 | 0 | My Pokemon Ranch: Eevee | sì | no | censita, non ancora producibile |
| `EVT-T-0205` | 4 | periferica | 142 | 0 | My Pokemon Ranch: Aerodactyl | sì | no | censita, non ancora producibile |
| `EVT-T-0206` | 4 | periferica | 193 | 0 | My Pokemon Ranch: Yanma | sì | no | censita, non ancora producibile |
| `EVT-T-0207` | 4 | periferica | 241 | 0 | My Pokemon Ranch: Miltank | sì | no | censita, non ancora producibile |
| `EVT-T-0208` | 4 | periferica | 285 | 0 | My Pokemon Ranch: Shroomish | sì | no | censita, non ancora producibile |
| `EVT-T-0210` | 4 | periferica | 360 | 0 | My Pokemon Ranch: Wynaut | sì | no | censita, non ancora producibile |
| `EVT-T-0213` | 4 | periferica | 417 | 0 | My Pokemon Ranch: Pachirisu | sì | no | censita, non ancora producibile |
| `EVT-T-0219` | 4 | periferica | 50 | 0 | My Pokemon Ranch: Mew | sì | no | censita, non ancora producibile |
| `EVT-T-0220` | 4 | periferica | 1 | 0 | My Pokemon Ranch: Phione | sì | no | censita, non ancora producibile |
| `EVT-T-0221` | 5 | periferica | 79 | 0 | Dream Radar: Slowpoke | sì | no | censita, non ancora producibile |
| `EVT-T-0225` | 5 | periferica | 174 | 0 | Dream Radar: Igglybuff | sì | no | censita, non ancora producibile |
| `EVT-T-0226` | 5 | periferica | 175 | 0 | Dream Radar: Togepi | sì | no | censita, non ancora producibile |
| `EVT-T-0227` | 5 | periferica | 213 | 0 | Dream Radar: Shuckle | sì | no | censita, non ancora producibile |
| `EVT-T-0229` | 5 | periferica | 249 | 0 | Dream Radar: Lugia (SoulSilver cart) | sì | no | censita, non ancora producibile |
| `EVT-T-0230` | 5 | periferica | 250 | 0 | Dream Radar: Ho-Oh (HeartGold cart) | sì | no | censita, non ancora producibile |
| `EVT-T-0231` | 5 | periferica | 280 | 0 | Dream Radar: Ralts | sì | no | censita, non ancora producibile |
| `EVT-T-0232` | 5 | periferica | 333 | 0 | Dream Radar: Swablu | sì | no | censita, non ancora producibile |
| `EVT-T-0233` | 5 | periferica | 374 | 0 | Dream Radar: Beldum | sì | no | censita, non ancora producibile |
| `EVT-T-0236` | 5 | periferica | 442 | 0 | Dream Radar: Spiritomb | sì | no | censita, non ancora producibile |
| `EVT-T-0237` | 5 | periferica | 447 | 0 | Dream Radar: Riolu | sì | no | censita, non ancora producibile |
| `EVT-T-0238` | 5 | periferica | 479 | 0 | Dream Radar: Rotom (no HA) | sì | no | censita, non ancora producibile |
| `EVT-T-0239` | 5 | periferica | 483 | 0 | Dream Radar: Dialga (Diamond cart) | sì | no | censita, non ancora producibile |
| `EVT-T-0240` | 5 | periferica | 484 | 0 | Dream Radar: Palkia (Pearl cart) | sì | no | censita, non ancora producibile |
| `EVT-T-0241` | 5 | periferica | 487 | 0 | Dream Radar: Giratina (Platinum cart) | sì | no | censita, non ancora producibile |
| `EVT-T-0242` | 5 | periferica | 517 | 0 | Dream Radar: Munna | sì | no | censita, non ancora producibile |
| `EVT-T-0244` | 5 | periferica | 641 | 0 | Dream Radar: Therian Tornadus | sì | no | censita, non ancora producibile |
| `EVT-T-0245` | 5 | periferica | 642 | 0 | Dream Radar: Therian Thundurus | sì | no | censita, non ancora producibile |
| `EVT-T-0246` | 5 | periferica | 645 | 0 | Dream Radar: Therian Landorus | sì | no | censita, non ancora producibile |
| `EVT-T-0247` | 8 | condizionato | 493 | 0 | Leggende Arceus, doni fatidici: Arceus | no | no | censita, non ancora producibile |
| `EVT-T-0248` | 8 | condizionato | 489 | 0 | Leggende Arceus, doni fatidici: Phione | no | no | censita, non ancora producibile |
| `EVT-T-0249` | 8 | condizionato | 490 | 0 | Leggende Arceus, doni fatidici: Manaphy | no | no | censita, non ancora producibile |
| `EVT-T-0250` | 8 | condizionato | 491 | 0 | Leggende Arceus, doni fatidici: Darkrai | no | no | censita, non ancora producibile |
| `EVT-T-0251` | 8 | condizionato | 492 | 0 | Leggende Arceus, doni fatidici: Shaymin | no | no | censita, non ancora producibile |
| `EVT-T-0252` | 8 | condizionato | 491 | 0 | Leggende Arceus, doni fatidici: Darkrai (Lonely Spring) | no | no | censita, non ancora producibile |
| `EVT-T-0253` | 8 | condizionato | 151 | 0 | Diamante Lucente e Perla Splendente, doni fatidici: Mew | no | no | censita, non ancora producibile |
| `EVT-T-0254` | 8 | condizionato | 385 | 0 | Diamante Lucente e Perla Splendente, doni fatidici: Jirachi | no | no | censita, non ancora producibile |
| `EVT-T-0255` | 8 | condizionato | 491 | 0 | Diamante Lucente e Perla Splendente, doni fatidici: Darkrai | no | no | censita, non ancora producibile |
| `EVT-T-0256` | 8 | condizionato | 492 | 0 | Diamante Lucente e Perla Splendente, doni fatidici: Shaymin | no | no | censita, non ancora producibile |
| `EVT-T-0257` | 8 | condizionato | 493 | 0 | Diamante Lucente e Perla Splendente, doni fatidici: Arceus (Brilliant Diamond) | no | no | censita, non ancora producibile |
| `EVT-T-0258` | 8 | condizionato | 493 | 0 | Diamante Lucente e Perla Splendente, doni fatidici: Arceus (Shining Pearl) | no | no | censita, non ancora producibile |
| `EVT-T-0259` | 8 | condizionato | 647 | 1 | Spada e Scudo, doni fatidici: Keldeo-1 at Ballimere Lake | no | no | censita, non ancora producibile |
| `EVT-T-0260` | 4 | periferica | 115 | 0 | Pokewalker: corso Prato Ristoro, livello 8, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0266` | 4 | periferica | 202 | 0 | Pokewalker: corso Bosco Rumoroso, livello 15, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0267` | 4 | periferica | 69 | 0 | Pokewalker: corso Bosco Rumoroso, livello 8, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0269` | 4 | periferica | 46 | 0 | Pokewalker: corso Bosco Rumoroso, livello 6, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0270` | 4 | periferica | 43 | 0 | Pokewalker: corso Bosco Rumoroso, livello 5, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0271` | 4 | periferica | 21 | 0 | Pokewalker: corso Bosco Rumoroso, livello 5, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0275` | 4 | periferica | 77 | 0 | Pokewalker: corso Strada Sconnessa, livello 7, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0276` | 4 | periferica | 163 | 0 | Pokewalker: corso Strada Sconnessa, livello 6, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0278` | 4 | periferica | 54 | 0 | Pokewalker: corso Bella Spiaggia, livello 10, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0279` | 4 | periferica | 120 | 0 | Pokewalker: corso Bella Spiaggia, livello 10, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0280` | 4 | periferica | 79 | 0 | Pokewalker: corso Bella Spiaggia, livello 8, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0281` | 4 | periferica | 60 | 0 | Pokewalker: corso Bella Spiaggia, livello 8, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0284` | 4 | periferica | 239 | 0 | Pokewalker: corso Zona Suburbana, livello 11, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0286` | 4 | periferica | 81 | 0 | Pokewalker: corso Zona Suburbana, livello 8, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0287` | 4 | periferica | 198 | 0 | Pokewalker: corso Zona Suburbana, livello 11, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0288` | 4 | periferica | 163 | 0 | Pokewalker: corso Zona Suburbana, livello 7, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0290` | 4 | periferica | 238 | 0 | Pokewalker: corso Grotta Buia, livello 12, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0292` | 4 | periferica | 92 | 0 | Pokewalker: corso Grotta Buia, livello 10, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0293` | 4 | periferica | 95 | 0 | Pokewalker: corso Grotta Buia, livello 10, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0295` | 4 | periferica | 66 | 0 | Pokewalker: corso Grotta Buia, livello 8, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0297` | 4 | periferica | 60 | 0 | Pokewalker: corso Lago Blu, livello 15, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0299` | 4 | periferica | 90 | 0 | Pokewalker: corso Lago Blu, livello 12, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0303` | 4 | periferica | 100 | 0 | Pokewalker: corso Periferia, livello 15, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0305` | 4 | periferica | 88 | 0 | Pokewalker: corso Periferia, livello 13, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0306` | 4 | periferica | 19 | 0 | Pokewalker: corso Periferia, livello 16, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0307` | 4 | periferica | 162 | 0 | Pokewalker: corso Periferia, livello 15, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0308` | 4 | periferica | 300 | 0 | Pokewalker: corso Prato di Hoenn, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0309` | 4 | periferica | 264 | 0 | Pokewalker: corso Prato di Hoenn, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0312` | 4 | periferica | 263 | 0 | Pokewalker: corso Prato di Hoenn, livello 17, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0314` | 4 | periferica | 320 | 0 | Pokewalker: corso Spiaggia Calda, livello 31, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0316` | 4 | periferica | 116 | 0 | Pokewalker: corso Spiaggia Calda, livello 20, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0317` | 4 | periferica | 318 | 0 | Pokewalker: corso Spiaggia Calda, livello 26, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0318` | 4 | periferica | 118 | 0 | Pokewalker: corso Spiaggia Calda, livello 22, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0319` | 4 | periferica | 129 | 0 | Pokewalker: corso Spiaggia Calda, livello 15, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0320` | 4 | periferica | 218 | 0 | Pokewalker: corso Via del Vulcano, livello 31, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0321` | 4 | periferica | 307 | 0 | Pokewalker: corso Via del Vulcano, livello 32, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0322` | 4 | periferica | 228 | 0 | Pokewalker: corso Via del Vulcano, livello 27, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0324` | 4 | periferica | 77 | 0 | Pokewalker: corso Via del Vulcano, livello 19, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0325` | 4 | periferica | 74 | 0 | Pokewalker: corso Via del Vulcano, livello 29, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0329` | 4 | periferica | 234 | 0 | Pokewalker: corso Casa sull Albero, livello 28, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0331` | 4 | periferica | 70 | 0 | Pokewalker: corso Casa sull Albero, livello 13, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0332` | 4 | periferica | 105 | 0 | Pokewalker: corso Grotta Spaventosa, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0333` | 4 | periferica | 128 | 0 | Pokewalker: corso Grotta Spaventosa, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0335` | 4 | periferica | 177 | 0 | Pokewalker: corso Grotta Spaventosa, livello 24, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0336` | 4 | periferica | 66 | 0 | Pokewalker: corso Grotta Spaventosa, livello 13, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0337` | 4 | periferica | 92 | 0 | Pokewalker: corso Grotta Spaventosa, livello 15, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0339` | 4 | periferica | 415 | 0 | Pokewalker: corso Prato di Sinnoh, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0344` | 4 | periferica | 459 | 0 | Pokewalker: corso Strada Ghiacciata, livello 31, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0345` | 4 | periferica | 361 | 0 | Pokewalker: corso Strada Ghiacciata, livello 28, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0346` | 4 | periferica | 215 | 0 | Pokewalker: corso Strada Ghiacciata, livello 28, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0347` | 4 | periferica | 436 | 0 | Pokewalker: corso Strada Ghiacciata, livello 20, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0348` | 4 | periferica | 220 | 0 | Pokewalker: corso Strada Ghiacciata, livello 16, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0349` | 4 | periferica | 179 | 0 | Pokewalker: corso Strada Ghiacciata, livello 15, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0350` | 4 | periferica | 357 | 0 | Pokewalker: corso Grande Foresta, livello 35, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0352` | 4 | periferica | 114 | 0 | Pokewalker: corso Grande Foresta, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0354` | 4 | periferica | 179 | 0 | Pokewalker: corso Grande Foresta, livello 19, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0355` | 4 | periferica | 102 | 0 | Pokewalker: corso Grande Foresta, livello 17, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0357` | 4 | periferica | 200 | 0 | Pokewalker: corso Lago Bianco, livello 32, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0358` | 4 | periferica | 93 | 0 | Pokewalker: corso Lago Bianco, livello 25, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0360` | 4 | periferica | 223 | 0 | Pokewalker: corso Lago Bianco, livello 19, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0362` | 4 | periferica | 456 | 0 | Pokewalker: corso Spiaggia Tempestosa, livello 26, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0363` | 4 | periferica | 422 | 0 | Pokewalker: corso Spiaggia Tempestosa, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0364` | 4 | periferica | 129 | 0 | Pokewalker: corso Spiaggia Tempestosa, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0365` | 4 | periferica | 86 | 0 | Pokewalker: corso Spiaggia Tempestosa, livello 27, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0366` | 4 | periferica | 54 | 0 | Pokewalker: corso Spiaggia Tempestosa, livello 22, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0367` | 4 | periferica | 90 | 0 | Pokewalker: corso Spiaggia Tempestosa, livello 20, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0368` | 4 | periferica | 417 | 0 | Pokewalker: corso Villaggio Turistico, livello 33, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0369` | 4 | periferica | 25 | 0 | Pokewalker: corso Villaggio Turistico, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0374` | 4 | periferica | 442 | 0 | Pokewalker: corso Grotta Silente, livello 31, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0375` | 4 | periferica | 446 | 0 | Pokewalker: corso Grotta Silente, livello 33, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0376` | 4 | periferica | 433 | 0 | Pokewalker: corso Grotta Silente, livello 26, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0377` | 4 | periferica | 349 | 0 | Pokewalker: corso Grotta Silente, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0378` | 4 | periferica | 164 | 0 | Pokewalker: corso Grotta Silente, livello 30, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0379` | 4 | periferica | 42 | 0 | Pokewalker: corso Grotta Silente, livello 33, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0380` | 4 | periferica | 120 | 0 | Pokewalker: corso Oltre il Mare, livello 18, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0381` | 4 | periferica | 224 | 0 | Pokewalker: corso Oltre il Mare, livello 19, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0382` | 4 | periferica | 116 | 0 | Pokewalker: corso Oltre il Mare, livello 15, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0383` | 4 | periferica | 222 | 0 | Pokewalker: corso Oltre il Mare, livello 16, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0384` | 4 | periferica | 223 | 0 | Pokewalker: corso Oltre il Mare, livello 14, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0385` | 4 | periferica | 170 | 0 | Pokewalker: corso Oltre il Mare, livello 12, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0386` | 4 | periferica | 35 | 0 | Pokewalker: corso Confine del Cielo, livello 8, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0387` | 4 | periferica | 39 | 0 | Pokewalker: corso Confine del Cielo, livello 10, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0388` | 4 | periferica | 41 | 0 | Pokewalker: corso Confine del Cielo, livello 9, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0389` | 4 | periferica | 163 | 0 | Pokewalker: corso Confine del Cielo, livello 6, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0390` | 4 | periferica | 74 | 0 | Pokewalker: corso Confine del Cielo, livello 5, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0391` | 4 | periferica | 95 | 0 | Pokewalker: corso Confine del Cielo, livello 5, corso in dotazione | sì | no | censita, non ancora producibile |
| `EVT-T-0392` | 4 | periferica | 25 | 0 | Pokewalker: corso Foresta Gialla, livello 15, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0393` | 4 | periferica | 25 | 0 | Pokewalker: corso Foresta Gialla, livello 14, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0394` | 4 | periferica | 25 | 0 | Pokewalker: corso Foresta Gialla, livello 13, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0395` | 4 | periferica | 25 | 0 | Pokewalker: corso Foresta Gialla, livello 12, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0396` | 4 | periferica | 25 | 0 | Pokewalker: corso Foresta Gialla, livello 10, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0397` | 4 | periferica | 25 | 0 | Pokewalker: corso Foresta Gialla, livello 10, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0398` | 4 | periferica | 441 | 0 | Pokewalker: corso Raduno, livello 15, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0399` | 4 | periferica | 302 | 0 | Pokewalker: corso Raduno, livello 15, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0400` | 4 | periferica | 25 | 0 | Pokewalker: corso Raduno, livello 10, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0401` | 4 | periferica | 453 | 0 | Pokewalker: corso Raduno, livello 10, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0402` | 4 | periferica | 427 | 0 | Pokewalker: corso Raduno, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0403` | 4 | periferica | 417 | 0 | Pokewalker: corso Raduno, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0404` | 4 | periferica | 255 | 0 | Pokewalker: corso Gita, livello 10, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0405` | 4 | periferica | 133 | 0 | Pokewalker: corso Gita, livello 10, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0408` | 4 | periferica | 52 | 0 | Pokewalker: corso Gita, livello 10, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0409` | 4 | periferica | 25 | 0 | Pokewalker: corso Gita, livello 8, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0410` | 4 | periferica | 446 | 0 | Pokewalker: corso Via del Vincitore, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0411` | 4 | periferica | 374 | 0 | Pokewalker: corso Via del Vincitore, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0412` | 4 | periferica | 116 | 0 | Pokewalker: corso Via del Vincitore, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0413` | 4 | periferica | 355 | 0 | Pokewalker: corso Via del Vincitore, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0414` | 4 | periferica | 129 | 0 | Pokewalker: corso Via del Vincitore, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0415` | 4 | periferica | 436 | 0 | Pokewalker: corso Via del Vincitore, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0416` | 4 | periferica | 239 | 0 | Pokewalker: corso Prato Amicizia, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0417` | 4 | periferica | 240 | 0 | Pokewalker: corso Prato Amicizia, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0418` | 4 | periferica | 238 | 0 | Pokewalker: corso Prato Amicizia, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-T-0420` | 4 | periferica | 174 | 0 | Pokewalker: corso Prato Amicizia, livello 5, corso distribuito | sì | no | censita, non ancora producibile |
| `EVT-1-0000` | 1 | tabella di incontro | 1 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-1-0001` | 1 | tabella di incontro | 4 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-1-0002` | 1 | tabella di incontro | 7 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-1-0003` | 1 | tabella di incontro | 54 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-1-0004` | 1 | tabella di incontro | 106 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-1-0005` | 1 | tabella di incontro | 107 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-1-0006` | 1 | tabella di incontro | 133 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-1-0007` | 1 | tabella di incontro | 138 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-1-0008` | 1 | tabella di incontro | 140 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-1-0009` | 1 | tabella di incontro | 151 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-1-0010` | 1 | tabella di incontro | 151 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0000` | 2 | tabella di incontro | 83 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0001` | 2 | tabella di incontro | 207 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0002` | 2 | tabella di incontro | 83 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0003` | 2 | tabella di incontro | 207 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0004` | 2 | tabella di incontro | 83 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0005` | 2 | tabella di incontro | 207 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0006` | 2 | tabella di incontro | 151 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0007` | 2 | tabella di incontro | 251 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0008` | 2 | tabella di incontro | 243 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0009` | 2 | tabella di incontro | 244 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0010` | 2 | tabella di incontro | 245 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0011` | 2 | tabella di incontro | 144 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0012` | 2 | tabella di incontro | 145 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0013` | 2 | tabella di incontro | 146 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0014` | 2 | tabella di incontro | 3 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0015` | 2 | tabella di incontro | 6 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0016` | 2 | tabella di incontro | 9 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0017` | 2 | tabella di incontro | 150 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0018` | 2 | tabella di incontro | 250 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0019` | 2 | tabella di incontro | 249 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0020` | 2 | tabella di incontro | 154 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0021` | 2 | tabella di incontro | 157 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0022` | 2 | tabella di incontro | 160 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0023` | 2 | tabella di incontro | 225 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0024` | 2 | tabella di incontro | 1 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0025` | 2 | tabella di incontro | 4 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0026` | 2 | tabella di incontro | 7 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0027` | 2 | tabella di incontro | 152 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0028` | 2 | tabella di incontro | 155 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0029` | 2 | tabella di incontro | 158 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0030` | 2 | tabella di incontro | 29 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0031` | 2 | tabella di incontro | 29 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0032` | 2 | tabella di incontro | 32 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0033` | 2 | tabella di incontro | 32 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0034` | 2 | tabella di incontro | 69 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0035` | 2 | tabella di incontro | 69 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0036` | 2 | tabella di incontro | 183 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0037` | 2 | tabella di incontro | 193 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0038` | 2 | tabella di incontro | 206 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0040` | 2 | tabella di incontro | 211 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0041` | 2 | tabella di incontro | 223 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0042` | 2 | tabella di incontro | 172 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0043` | 2 | tabella di incontro | 173 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0044` | 2 | tabella di incontro | 174 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0045` | 2 | tabella di incontro | 238 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0046` | 2 | tabella di incontro | 239 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0047` | 2 | tabella di incontro | 240 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0048` | 2 | tabella di incontro | 54 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0049` | 2 | tabella di incontro | 152 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0050` | 2 | tabella di incontro | 172 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0051` | 2 | tabella di incontro | 173 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0052` | 2 | tabella di incontro | 174 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0053` | 2 | tabella di incontro | 238 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0054` | 2 | tabella di incontro | 194 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0055` | 2 | tabella di incontro | 60 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0056` | 2 | tabella di incontro | 116 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0057` | 2 | tabella di incontro | 118 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0058` | 2 | tabella di incontro | 129 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0059` | 2 | tabella di incontro | 183 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0060` | 2 | tabella di incontro | 54 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0061` | 2 | tabella di incontro | 72 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0062` | 2 | tabella di incontro | 131 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0063` | 2 | tabella di incontro | 170 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0064` | 2 | tabella di incontro | 223 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0065` | 2 | tabella di incontro | 226 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0066` | 2 | tabella di incontro | 29 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0067` | 2 | tabella di incontro | 32 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0068` | 2 | tabella di incontro | 113 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0069` | 2 | tabella di incontro | 115 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0070` | 2 | tabella di incontro | 128 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0071` | 2 | tabella di incontro | 147 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0072` | 2 | tabella di incontro | 21 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0073` | 2 | tabella di incontro | 83 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0074` | 2 | tabella di incontro | 84 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0075` | 2 | tabella di incontro | 177 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0076` | 2 | tabella di incontro | 198 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0077` | 2 | tabella di incontro | 227 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0078` | 2 | tabella di incontro | 172 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0079` | 2 | tabella di incontro | 81 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0080` | 2 | tabella di incontro | 239 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0081` | 2 | tabella di incontro | 100 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0082` | 2 | tabella di incontro | 173 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0083` | 2 | tabella di incontro | 174 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0084` | 2 | tabella di incontro | 183 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0085` | 2 | tabella di incontro | 172 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0086` | 2 | tabella di incontro | 194 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0087` | 2 | tabella di incontro | 114 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0088` | 2 | tabella di incontro | 77 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0089` | 2 | tabella di incontro | 200 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0090` | 2 | tabella di incontro | 246 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0091` | 2 | tabella di incontro | 120 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0092` | 2 | tabella di incontro | 98 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0093` | 2 | tabella di incontro | 95 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0094` | 2 | tabella di incontro | 131 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0095` | 2 | tabella di incontro | 63 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0096` | 2 | tabella di incontro | 96 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0097` | 2 | tabella di incontro | 102 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0098` | 2 | tabella di incontro | 122 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0099` | 2 | tabella di incontro | 74 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0100` | 2 | tabella di incontro | 41 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0101` | 2 | tabella di incontro | 66 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0103` | 2 | tabella di incontro | 225 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0104` | 2 | tabella di incontro | 86 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0105` | 2 | tabella di incontro | 220 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0106` | 2 | tabella di incontro | 163 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0107` | 2 | tabella di incontro | 215 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0108` | 2 | tabella di incontro | 191 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0109` | 2 | tabella di incontro | 46 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0110` | 2 | tabella di incontro | 187 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0111` | 2 | tabella di incontro | 43 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0112` | 2 | tabella di incontro | 161 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0113` | 2 | tabella di incontro | 234 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0114` | 2 | tabella di incontro | 241 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0115` | 2 | tabella di incontro | 190 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0116` | 2 | tabella di incontro | 108 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0117` | 2 | tabella di incontro | 143 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0118` | 2 | tabella di incontro | 66 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0119` | 2 | tabella di incontro | 129 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0121` | 2 | tabella di incontro | 206 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0122` | 2 | tabella di incontro | 202 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0124` | 2 | tabella di incontro | 216 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0125` | 2 | tabella di incontro | 60 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0126` | 2 | tabella di incontro | 60 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0127` | 2 | tabella di incontro | 143 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0128` | 2 | tabella di incontro | 143 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0129` | 2 | tabella di incontro | 140 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0130` | 2 | tabella di incontro | 138 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0131` | 2 | tabella di incontro | 142 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0132` | 2 | tabella di incontro | 137 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0133` | 2 | tabella di incontro | 133 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0134` | 2 | tabella di incontro | 185 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0135` | 2 | tabella di incontro | 123 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0136` | 2 | tabella di incontro | 214 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0137` | 2 | tabella di incontro | 127 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0138` | 2 | tabella di incontro | 165 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0139` | 2 | tabella di incontro | 167 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0140` | 2 | tabella di incontro | 193 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0141` | 2 | tabella di incontro | 204 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0142` | 2 | tabella di incontro | 152 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0143` | 2 | tabella di incontro | 172 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0144` | 2 | tabella di incontro | 173 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0145` | 2 | tabella di incontro | 194 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0146` | 2 | tabella di incontro | 231 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0147` | 2 | tabella di incontro | 238 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0148` | 2 | tabella di incontro | 54 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0149` | 2 | tabella di incontro | 172 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0150` | 2 | tabella di incontro | 173 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0151` | 2 | tabella di incontro | 174 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0152` | 2 | tabella di incontro | 238 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0153` | 2 | tabella di incontro | 1 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0154` | 2 | tabella di incontro | 4 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0155` | 2 | tabella di incontro | 158 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |
| `EVT-2-0156` | 2 | tabella di incontro | 163 | 0 | tabella di incontro da evento | sì | no | letta, struttura alla portata di pokebridge |

## Voci di forma

| Codice | Dex | Specie | Forma | Via | Natura |
|---|---|---|---|---|---|
| `PKD-0003-01` | 3 | Venusaur | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0006-01` | 6 | Charizard | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0006-02` | 6 | Charizard | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0009-01` | 9 | Blastoise | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0015-01` | 15 | Beedrill | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0018-01` | 18 | Pidgeot | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0019-01` | 19 | Rattata | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0020-01` | 20 | Raticate | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0020-02` | 20 | Raticate | 2 | diretta | forma totemica: al trasferimento torna alla forma base |
| `PKD-0025-01` | 25 | Pikachu | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0025-02` | 25 | Pikachu | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0025-03` | 25 | Pikachu | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0025-04` | 25 | Pikachu | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0025-05` | 25 | Pikachu | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0025-06` | 25 | Pikachu | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0025-07` | 25 | Pikachu | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0025-08` | 25 | Pikachu | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0025-09` | 25 | Pikachu | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0026-01` | 26 | Raichu | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0026-02` | 26 | Raichu | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0026-03` | 26 | Raichu | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0027-01` | 27 | Sandshrew | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0028-01` | 28 | Sandslash | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0036-01` | 36 | Clefable | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0037-01` | 37 | Vulpix | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0038-01` | 38 | Ninetales | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0050-01` | 50 | Diglett | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0051-01` | 51 | Dugtrio | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0052-01` | 52 | Meowth | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0052-02` | 52 | Meowth | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0053-01` | 53 | Persian | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0058-01` | 58 | Growlithe | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0059-01` | 59 | Arcanine | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0059-02` | 59 | Arcanine | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0065-01` | 65 | Alakazam | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0071-01` | 71 | Victreebel | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0074-01` | 74 | Geodude | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0075-01` | 75 | Graveler | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0076-01` | 76 | Golem | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0077-01` | 77 | Ponyta | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0078-01` | 78 | Rapidash | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0079-01` | 79 | Slowpoke | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0080-01` | 80 | Slowbro | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0080-02` | 80 | Slowbro | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0083-01` | 83 | Farfetch’d | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0088-01` | 88 | Grimer | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0089-01` | 89 | Muk | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0094-01` | 94 | Gengar | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0100-01` | 100 | Voltorb | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0101-01` | 101 | Electrode | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0101-02` | 101 | Electrode | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0103-01` | 103 | Exeggutor | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0105-01` | 105 | Marowak | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0105-02` | 105 | Marowak | 2 | diretta | forma totemica: al trasferimento torna alla forma base |
| `PKD-0110-01` | 110 | Weezing | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0115-01` | 115 | Kangaskhan | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0121-01` | 121 | Starmie | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0122-01` | 122 | Mr. Mime | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0127-01` | 127 | Pinsir | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0128-01` | 128 | Tauros | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0128-02` | 128 | Tauros | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0128-03` | 128 | Tauros | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0130-01` | 130 | Gyarados | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0133-01` | 133 | Eevee | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0142-01` | 142 | Aerodactyl | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0144-01` | 144 | Articuno | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0145-01` | 145 | Zapdos | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0146-01` | 146 | Moltres | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0149-01` | 149 | Dragonite | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0150-01` | 150 | Mewtwo | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0150-02` | 150 | Mewtwo | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0154-01` | 154 | Meganium | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0157-01` | 157 | Typhlosion | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0160-01` | 160 | Feraligatr | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0181-01` | 181 | Ampharos | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0194-01` | 194 | Wooper | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0199-01` | 199 | Slowking | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-01` | 201 | Unown | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-02` | 201 | Unown | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-03` | 201 | Unown | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-04` | 201 | Unown | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-05` | 201 | Unown | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-06` | 201 | Unown | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-07` | 201 | Unown | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-08` | 201 | Unown | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-09` | 201 | Unown | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-10` | 201 | Unown | 10 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-11` | 201 | Unown | 11 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-12` | 201 | Unown | 12 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-13` | 201 | Unown | 13 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-14` | 201 | Unown | 14 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-15` | 201 | Unown | 15 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-16` | 201 | Unown | 16 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-17` | 201 | Unown | 17 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-18` | 201 | Unown | 18 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-19` | 201 | Unown | 19 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-20` | 201 | Unown | 20 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-21` | 201 | Unown | 21 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-22` | 201 | Unown | 22 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-23` | 201 | Unown | 23 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-24` | 201 | Unown | 24 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-25` | 201 | Unown | 25 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-26` | 201 | Unown | 26 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0201-27` | 201 | Unown | 27 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0208-01` | 208 | Steelix | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0211-01` | 211 | Qwilfish | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0212-01` | 212 | Scizor | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0214-01` | 214 | Heracross | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0215-01` | 215 | Sneasel | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0222-01` | 222 | Corsola | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0227-01` | 227 | Skarmory | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0229-01` | 229 | Houndoom | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0248-01` | 248 | Tyranitar | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0254-01` | 254 | Sceptile | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0257-01` | 257 | Blaziken | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0260-01` | 260 | Swampert | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0263-01` | 263 | Zigzagoon | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0264-01` | 264 | Linoone | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0282-01` | 282 | Gardevoir | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0302-01` | 302 | Sableye | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0303-01` | 303 | Mawile | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0306-01` | 306 | Aggron | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0308-01` | 308 | Medicham | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0310-01` | 310 | Manectric | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0319-01` | 319 | Sharpedo | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0323-01` | 323 | Camerupt | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0334-01` | 334 | Altaria | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0351-01` | 351 | Castform | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0351-02` | 351 | Castform | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0351-03` | 351 | Castform | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0354-01` | 354 | Banette | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0358-01` | 358 | Chimecho | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0359-01` | 359 | Absol | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0359-02` | 359 | Absol | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0362-01` | 362 | Glalie | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0373-01` | 373 | Salamence | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0376-01` | 376 | Metagross | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0380-01` | 380 | Latias | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0381-01` | 381 | Latios | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0382-01` | 382 | Kyogre | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0383-01` | 383 | Groudon | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0384-01` | 384 | Rayquaza | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0386-01` | 386 | Deoxys | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0386-02` | 386 | Deoxys | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0386-03` | 386 | Deoxys | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0398-01` | 398 | Staraptor | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0412-01` | 412 | Burmy | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0412-02` | 412 | Burmy | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0413-01` | 413 | Wormadam | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0413-02` | 413 | Wormadam | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0414-01` | 414 | Mothim | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0414-02` | 414 | Mothim | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0421-01` | 421 | Cherrim | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0422-01` | 422 | Shellos | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0423-01` | 423 | Gastrodon | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0428-01` | 428 | Lopunny | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0445-01` | 445 | Garchomp | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0445-02` | 445 | Garchomp | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0448-01` | 448 | Lucario | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0448-02` | 448 | Lucario | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0460-01` | 460 | Abomasnow | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0475-01` | 475 | Gallade | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0478-01` | 478 | Froslass | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0479-01` | 479 | Rotom | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0479-02` | 479 | Rotom | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0479-03` | 479 | Rotom | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0479-04` | 479 | Rotom | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0479-05` | 479 | Rotom | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0483-01` | 483 | Dialga | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0484-01` | 484 | Palkia | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0485-01` | 485 | Heatran | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0487-01` | 487 | Giratina | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0491-01` | 491 | Darkrai | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0492-01` | 492 | Shaymin | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-01` | 493 | Arceus | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-02` | 493 | Arceus | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-03` | 493 | Arceus | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-04` | 493 | Arceus | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-05` | 493 | Arceus | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-06` | 493 | Arceus | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-07` | 493 | Arceus | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-08` | 493 | Arceus | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-09` | 493 | Arceus | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-10` | 493 | Arceus | 10 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-11` | 493 | Arceus | 11 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-12` | 493 | Arceus | 12 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-13` | 493 | Arceus | 13 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-14` | 493 | Arceus | 14 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-15` | 493 | Arceus | 15 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-16` | 493 | Arceus | 16 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-17` | 493 | Arceus | 17 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0493-18` | 493 | Arceus | 18 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0500-01` | 500 | Emboar | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0503-01` | 503 | Samurott | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0530-01` | 530 | Excadrill | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0531-01` | 531 | Audino | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0545-01` | 545 | Scolipede | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0549-01` | 549 | Lilligant | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0549-02` | 549 | Lilligant | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0550-01` | 550 | Basculin | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0550-02` | 550 | Basculin | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0554-01` | 554 | Darumaka | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0555-01` | 555 | Darmanitan | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0555-02` | 555 | Darmanitan | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0555-03` | 555 | Darmanitan | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0560-01` | 560 | Scrafty | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0562-01` | 562 | Yamask | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0570-01` | 570 | Zorua | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0571-01` | 571 | Zoroark | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0585-01` | 585 | Deerling | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0585-02` | 585 | Deerling | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0585-03` | 585 | Deerling | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0586-01` | 586 | Sawsbuck | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0586-02` | 586 | Sawsbuck | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0586-03` | 586 | Sawsbuck | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0604-01` | 604 | Eelektross | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0609-01` | 609 | Chandelure | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0618-01` | 618 | Stunfisk | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0623-01` | 623 | Golurk | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0628-01` | 628 | Braviary | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0641-01` | 641 | Tornadus | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0642-01` | 642 | Thundurus | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0645-01` | 645 | Landorus | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0646-01` | 646 | Kyurem | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0646-02` | 646 | Kyurem | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0647-01` | 647 | Keldeo | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0648-01` | 648 | Meloetta | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0649-01` | 649 | Genesect | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0649-02` | 649 | Genesect | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0649-03` | 649 | Genesect | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0649-04` | 649 | Genesect | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0652-01` | 652 | Chesnaught | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0655-01` | 655 | Delphox | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0658-01` | 658 | Greninja | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0658-02` | 658 | Greninja | 2 | banca | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0658-03` | 658 | Greninja | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0664-01` | 664 | Scatterbug | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-02` | 664 | Scatterbug | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-03` | 664 | Scatterbug | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-04` | 664 | Scatterbug | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-05` | 664 | Scatterbug | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-06` | 664 | Scatterbug | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-07` | 664 | Scatterbug | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-08` | 664 | Scatterbug | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-09` | 664 | Scatterbug | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-10` | 664 | Scatterbug | 10 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-11` | 664 | Scatterbug | 11 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-12` | 664 | Scatterbug | 12 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-13` | 664 | Scatterbug | 13 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-14` | 664 | Scatterbug | 14 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-15` | 664 | Scatterbug | 15 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-16` | 664 | Scatterbug | 16 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-17` | 664 | Scatterbug | 17 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-18` | 664 | Scatterbug | 18 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0664-19` | 664 | Scatterbug | 19 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-01` | 665 | Spewpa | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-02` | 665 | Spewpa | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-03` | 665 | Spewpa | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-04` | 665 | Spewpa | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-05` | 665 | Spewpa | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-06` | 665 | Spewpa | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-07` | 665 | Spewpa | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-08` | 665 | Spewpa | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-09` | 665 | Spewpa | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-10` | 665 | Spewpa | 10 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-11` | 665 | Spewpa | 11 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-12` | 665 | Spewpa | 12 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-13` | 665 | Spewpa | 13 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-14` | 665 | Spewpa | 14 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-15` | 665 | Spewpa | 15 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-16` | 665 | Spewpa | 16 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-17` | 665 | Spewpa | 17 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-18` | 665 | Spewpa | 18 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0665-19` | 665 | Spewpa | 19 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-01` | 666 | Vivillon | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-02` | 666 | Vivillon | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-03` | 666 | Vivillon | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-04` | 666 | Vivillon | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-05` | 666 | Vivillon | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-06` | 666 | Vivillon | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-07` | 666 | Vivillon | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-08` | 666 | Vivillon | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-09` | 666 | Vivillon | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-10` | 666 | Vivillon | 10 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-11` | 666 | Vivillon | 11 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-12` | 666 | Vivillon | 12 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-13` | 666 | Vivillon | 13 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-14` | 666 | Vivillon | 14 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-15` | 666 | Vivillon | 15 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-16` | 666 | Vivillon | 16 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-17` | 666 | Vivillon | 17 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-18` | 666 | Vivillon | 18 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0666-19` | 666 | Vivillon | 19 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0668-01` | 668 | Pyroar | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0669-01` | 669 | Flabébé | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0669-02` | 669 | Flabébé | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0669-03` | 669 | Flabébé | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0669-04` | 669 | Flabébé | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0670-01` | 670 | Floette | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0670-02` | 670 | Floette | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0670-03` | 670 | Floette | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0670-04` | 670 | Floette | 4 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0670-05` | 670 | Floette | 5 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0670-06` | 670 | Floette | 6 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0671-01` | 671 | Florges | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0671-02` | 671 | Florges | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0671-03` | 671 | Florges | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0671-04` | 671 | Florges | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0676-01` | 676 | Furfrou | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0676-02` | 676 | Furfrou | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0676-03` | 676 | Furfrou | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0676-04` | 676 | Furfrou | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0676-05` | 676 | Furfrou | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0676-06` | 676 | Furfrou | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0676-07` | 676 | Furfrou | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0676-08` | 676 | Furfrou | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0676-09` | 676 | Furfrou | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0678-01` | 678 | Meowstic | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0678-02` | 678 | Meowstic | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0678-03` | 678 | Meowstic | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0681-01` | 681 | Aegislash | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0687-01` | 687 | Malamar | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0689-01` | 689 | Barbaracle | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0691-01` | 691 | Dragalge | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0701-01` | 701 | Hawlucha | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0705-01` | 705 | Sliggoo | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0706-01` | 706 | Goodra | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0710-01` | 710 | Pumpkaboo | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0710-02` | 710 | Pumpkaboo | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0710-03` | 710 | Pumpkaboo | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0711-01` | 711 | Gourgeist | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0711-02` | 711 | Gourgeist | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0711-03` | 711 | Gourgeist | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0713-01` | 713 | Avalugg | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0713-02` | 713 | Avalugg | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0716-01` | 716 | Xerneas | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0718-01` | 718 | Zygarde | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0718-02` | 718 | Zygarde | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0718-03` | 718 | Zygarde | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0718-04` | 718 | Zygarde | 4 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0718-05` | 718 | Zygarde | 5 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0719-01` | 719 | Diancie | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0720-01` | 720 | Hoopa | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0724-01` | 724 | Decidueye | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0735-01` | 735 | Gumshoos | 1 | banca | forma totemica: al trasferimento torna alla forma base |
| `PKD-0738-01` | 738 | Vikavolt | 1 | banca | forma totemica: al trasferimento torna alla forma base |
| `PKD-0740-01` | 740 | Crabominable | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0741-01` | 741 | Oricorio | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0741-02` | 741 | Oricorio | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0741-03` | 741 | Oricorio | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0743-01` | 743 | Ribombee | 1 | banca | forma totemica: al trasferimento torna alla forma base |
| `PKD-0744-01` | 744 | Rockruff | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0745-01` | 745 | Lycanroc | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0745-02` | 745 | Lycanroc | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0746-01` | 746 | Wishiwashi | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0752-01` | 752 | Araquanid | 1 | banca | forma totemica: al trasferimento torna alla forma base |
| `PKD-0754-01` | 754 | Lurantis | 1 | banca | forma totemica: al trasferimento torna alla forma base |
| `PKD-0758-01` | 758 | Salazzle | 1 | banca | forma totemica: al trasferimento torna alla forma base |
| `PKD-0768-01` | 768 | Golisopod | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0773-01` | 773 | Silvally | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-02` | 773 | Silvally | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-03` | 773 | Silvally | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-04` | 773 | Silvally | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-05` | 773 | Silvally | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-06` | 773 | Silvally | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-07` | 773 | Silvally | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-08` | 773 | Silvally | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-09` | 773 | Silvally | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-10` | 773 | Silvally | 10 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-11` | 773 | Silvally | 11 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-12` | 773 | Silvally | 12 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-13` | 773 | Silvally | 13 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-14` | 773 | Silvally | 14 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-15` | 773 | Silvally | 15 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-16` | 773 | Silvally | 16 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0773-17` | 773 | Silvally | 17 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0774-01` | 774 | Minior | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-02` | 774 | Minior | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-03` | 774 | Minior | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-04` | 774 | Minior | 4 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-05` | 774 | Minior | 5 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-06` | 774 | Minior | 6 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-07` | 774 | Minior | 7 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-08` | 774 | Minior | 8 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-09` | 774 | Minior | 9 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-10` | 774 | Minior | 10 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-11` | 774 | Minior | 11 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-12` | 774 | Minior | 12 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0774-13` | 774 | Minior | 13 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0777-01` | 777 | Togedemaru | 1 | banca | forma totemica: al trasferimento torna alla forma base |
| `PKD-0778-01` | 778 | Mimikyu | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0778-02` | 778 | Mimikyu | 2 | banca | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0778-03` | 778 | Mimikyu | 3 | banca | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0780-01` | 780 | Drampa | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0784-01` | 784 | Kommo-o | 1 | banca | forma totemica: al trasferimento torna alla forma base |
| `PKD-0800-01` | 800 | Necrozma | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0800-02` | 800 | Necrozma | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0800-03` | 800 | Necrozma | 3 | banca | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0801-01` | 801 | Magearna | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0801-02` | 801 | Magearna | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0801-03` | 801 | Magearna | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0807-01` | 807 | Zeraora | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0845-01` | 845 | Cramorant | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0845-02` | 845 | Cramorant | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0849-01` | 849 | Toxtricity | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0854-01` | 854 | Sinistea | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0855-01` | 855 | Polteageist | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0869-01` | 869 | Alcremie | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0869-02` | 869 | Alcremie | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0869-03` | 869 | Alcremie | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0869-04` | 869 | Alcremie | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0869-05` | 869 | Alcremie | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0869-06` | 869 | Alcremie | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0869-07` | 869 | Alcremie | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0869-08` | 869 | Alcremie | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0870-01` | 870 | Falinks | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0875-01` | 875 | Eiscue | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0876-01` | 876 | Indeedee | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0877-01` | 877 | Morpeko | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0888-01` | 888 | Zacian | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0889-01` | 889 | Zamazenta | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0890-01` | 890 | Eternatus | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0892-01` | 892 | Urshifu | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0893-01` | 893 | Zarude | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0898-01` | 898 | Calyrex | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0898-02` | 898 | Calyrex | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0900-01` | 900 | Kleavor | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0901-01` | 901 | Ursaluna | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0902-01` | 902 | Basculegion | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0905-01` | 905 | Enamorus | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0916-01` | 916 | Oinkologne | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0925-01` | 925 | Maushold | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0931-01` | 931 | Squawkabilly | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0931-02` | 931 | Squawkabilly | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0931-03` | 931 | Squawkabilly | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0952-01` | 952 | Scovillain | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0964-01` | 964 | Palafin | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0970-01` | 970 | Glimmora | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0978-01` | 978 | Tatsugiri | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0978-02` | 978 | Tatsugiri | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0978-03` | 978 | Tatsugiri | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0978-04` | 978 | Tatsugiri | 4 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0978-05` | 978 | Tatsugiri | 5 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0982-01` | 982 | Dudunsparce | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-0998-01` | 998 | Baxcalibur | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-0999-01` | 999 | Gimmighoul | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1007-01` | 1007 | Koraidon | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1007-02` | 1007 | Koraidon | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1007-03` | 1007 | Koraidon | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1007-04` | 1007 | Koraidon | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1008-01` | 1008 | Miraidon | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1008-02` | 1008 | Miraidon | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1008-03` | 1008 | Miraidon | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1008-04` | 1008 | Miraidon | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1012-01` | 1012 | Poltchageist | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1012-02` | 1012 | Poltchageist | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1013-01` | 1013 | Sinistcha | 1 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1013-02` | 1013 | Sinistcha | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1017-01` | 1017 | Ogerpon | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1017-02` | 1017 | Ogerpon | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1017-03` | 1017 | Ogerpon | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1017-04` | 1017 | Ogerpon | 4 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1017-05` | 1017 | Ogerpon | 5 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1017-06` | 1017 | Ogerpon | 6 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1017-07` | 1017 | Ogerpon | 7 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1019-02` | 1019 | Hydrapple | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1019-03` | 1019 | Hydrapple | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1019-04` | 1019 | Hydrapple | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1019-05` | 1019 | Hydrapple | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1019-06` | 1019 | Hydrapple | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1019-07` | 1019 | Hydrapple | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1019-08` | 1019 | Hydrapple | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1019-09` | 1019 | Hydrapple | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1020-02` | 1020 | Vampeaguzze | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1020-03` | 1020 | Vampeaguzze | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1020-04` | 1020 | Vampeaguzze | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1020-05` | 1020 | Vampeaguzze | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1020-06` | 1020 | Vampeaguzze | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1020-07` | 1020 | Vampeaguzze | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1020-08` | 1020 | Vampeaguzze | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1020-09` | 1020 | Vampeaguzze | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1021-02` | 1021 | Furiatonante | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1021-03` | 1021 | Furiatonante | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1021-04` | 1021 | Furiatonante | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1021-05` | 1021 | Furiatonante | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1021-06` | 1021 | Furiatonante | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1021-07` | 1021 | Furiatonante | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1021-08` | 1021 | Furiatonante | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1021-09` | 1021 | Furiatonante | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1022-02` | 1022 | Massoferreo | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1022-03` | 1022 | Massoferreo | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1022-04` | 1022 | Massoferreo | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1022-05` | 1022 | Massoferreo | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1022-06` | 1022 | Massoferreo | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1022-07` | 1022 | Massoferreo | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1022-08` | 1022 | Massoferreo | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1022-09` | 1022 | Massoferreo | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1023-02` | 1023 | Capoferreo | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1023-03` | 1023 | Capoferreo | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1023-04` | 1023 | Capoferreo | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1023-05` | 1023 | Capoferreo | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1023-06` | 1023 | Capoferreo | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1023-07` | 1023 | Capoferreo | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1023-08` | 1023 | Capoferreo | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1023-09` | 1023 | Capoferreo | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1024-01` | 1024 | Terapagos | 1 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1024-02` | 1024 | Terapagos | 2 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1024-03` | 1024 | Terapagos | 3 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1024-04` | 1024 | Terapagos | 4 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1024-05` | 1024 | Terapagos | 5 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1024-06` | 1024 | Terapagos | 6 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1024-07` | 1024 | Terapagos | 7 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1024-08` | 1024 | Terapagos | 8 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1024-09` | 1024 | Terapagos | 9 | diretta | forma di sola battaglia: non puo stare in una scatola |
| `PKD-1025-02` | 1025 | Pecharunt | 2 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1025-03` | 1025 | Pecharunt | 3 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1025-04` | 1025 | Pecharunt | 4 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1025-05` | 1025 | Pecharunt | 5 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1025-06` | 1025 | Pecharunt | 6 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1025-07` | 1025 | Pecharunt | 7 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1025-08` | 1025 | Pecharunt | 8 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |
| `PKD-1025-09` | 1025 | Pecharunt | 9 | diretta | indeterminato: nessuna fonte di primo livello dice se il deposito la conti |

