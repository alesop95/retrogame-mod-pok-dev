# Catalogo delle distribuzioni di evento di generazione 3

Questo file è generato da `tools/catalogo-eventi-gen3.py` e non si modifica a mano: si rigenera. La fonte è la tabella `PKHeX.Core/Legality/Encounters/Data/Gen3/EncountersWC3.cs` di `PKHeX`, con il vocabolario dei metodi preso da `PKHeX.Core/Legality/RNG/PIDType.cs` dello stesso repository. Il comando è `python tools/catalogo-eventi-gen3.py --pkhex <percorso del clone>`, e il clone non è una dipendenza di questo repository: si passa sulla riga di comando, come per i disassemblati.

Il catalogo serve a una domanda operativa del sottoprogetto: quali eventi sono esistiti e con quale metodo di generazione, perché è il metodo e non il campo visibile a distinguere una ricreazione fedele da un dato costruito a mano. Chi ha bisogno del ragionamento, e non dell'elenco, legga `STUDIO-02-metodi-di-generazione.md`.

Due avvertenze sul contenuto. La prima è che le date degli eventi non compaiono, perché la fonte le porta soltanto in alcuni commenti di blocco e indovinare le altre sarebbe peggio che ometterle: dove il blocco le dichiara, il titolo del blocco le riporta. La seconda è che il nome della specie viene dal commento di riga della fonte, e dove il commento manca resta il numero interno, che è comunque il dato con cui si cerca.

## Che cosa contiene, in numeri

Le voci sono 177, divise nei quattro insiemi in cui la fonte le tiene separate.

| Insieme | Voci | Perché è separato |
|---|---|---|
| `Common` | 3 | voci consultate più spesso, tenute separate dalla fonte per comodità |
| `Japan` | 23 | distribuzioni giapponesi |
| `International` | 97 | distribuzioni internazionali, divise per lingua dove la lingua cambia il nome dell'allenatore |
| `Eggs` | 54 | distribuzioni consegnate come uova, dove l'allenatore è il ricevente |

## I metodi di generazione, e quanto pesano

La colonna della descrizione riporta la dichiarazione della fonte in inglese e non una sua traduzione, perché è la definizione del metodo e una parafrasi non sarebbe citabile. La sigla BACD nomina l'ordine con cui le quattro estrazioni del generatore compongono il valore di personalità e i valori individuali, ed è invertito rispetto a quello degli incontri ordinari: è questa inversione, e non un algoritmo diverso, la firma di un esemplare da evento.

| Metodo | Voci | Che cosa dichiara la fonte |
|---|---|---|
| `BACD_R_A` | 114 | Event Reversed Order PID restricted to 16bit Origin Seed, anti-shiny. |
| `Method_2` | 25 | Method 2. Generatore: LCRNG. |
| `BACD_R` | 16 | Event Reversed Order PID restricted to 16bit Origin Seed |
| `BACD_TA` | 9 | Event Reversed Order PID restricted to 16bit Origin Seed, consuming 2 calls select the event gift index, anti-shiny. |
| `BACD_RBCD` | 4 | Event Reversed Order PID restricted to [0,213] Origin Seed, shiny (Binary Coded Decimal hh:mm:ss timestamp digit sum from RTC). |
| `BACD_U` | 4 | Event Reversed Order PID without Origin Seed restrictions |
| `BACD_TS` | 2 | Event Reversed Order PID restricted to 16bit Origin Seed, consuming 2 calls select the event gift index, force-shiny. |
| `BACD_M` | 1 | Event Reversed Order PID with Origin Seed restrictions, only using the Mystry Mew table. |
| `BACD_U_AX` | 1 | Event Reversed Order PID without Origin Seed restrictions, anti-shiny (xor) |
| `Channel` | 1 | Generation 3 Pokémon Channel Jirachi. Generatore: XDRNG. |

Restano nell'enumerazione, e nessuna voce li usa, i metodi `BACD`, `BACD_A`, `BACD_AX`, `BACD_EA`, `BACD_EAX`, `BACD_ES`, `BACD_S`. Il fatto va registrato perché è un risultato negativo e non una lacuna: la fonte dichiara accanto a due di essi che nessun evento li ha mai generati, e conservarli documenta lo spazio delle possibilità invece dei soli casi occorsi.

## Le derivazioni del sesso dell'allenatore di provenienza

La fonte le tiene in un'enumerazione propria e dichiara che, quando è casuale, il sesso è determinato dopo il valore di personalità e i valori individuali, e in un caso dopo l'oggetto tenuto. Sono la parte del formato che una ricreazione sbaglia più facilmente, perché non è visibile in gioco.

| Sigla | Che cosa fa | Voci |
|---|---|---|
| `Recipient` | copiato dal ricevente | 1 |
| `Only0` | sempre 0 | 33 |
| `Only1` | sempre 1 | 6 |
| `RandAlgo` | algoritmo proprio, che la fonte dichiara di non verificare con la logica ordinaria | 1 |
| `RandD3` | divisione per 3 | 5 |
| `RandS3` | scorrimento di 3 | 2 |
| `RandS7` | scorrimento di 7 | 97 |
| `RandSG15` | scorrimento di 15, dopo l'oggetto | 3 |
| `RandD3_0` | divisione per 3, obbligata a 0, evento a due allenatori | 2 |
| `RandD3_1` | divisione per 3, obbligata a 1, evento a due allenatori | 2 |

## Le voci, per insieme e per blocco

### Insieme `Common`


Blocco: senza intestazione nella fonte

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Mew | 10 | `MYSTRY` | English | 06930 | `BACD_M` | Never | `RandD3` | incontro fatidico |
| specie 385 | 05 | `WISHMKR` | English | 20043 | `BACD_R` | Random | `Only0` |  |
| specie 385 | 05 | `CHANNEL` |  | 40122 | `Channel` | Random | `RandAlgo` |  |

### Insieme `Japan`


Blocco: senza intestazione nella fonte

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Berry Fix Ruby | 05 | `ルビー` | Japanese | 21121 | `BACD_RBCD` | Always | `RandD3_1` |  |
| Berry Fix Sapphire | 05 | `サファイア` | Japanese | 21121 | `BACD_RBCD` | Always | `RandD3_0` |  |
| Negai Boshi Jirachi | 05 | `ネガイボシ` | Japanese | 30719 | `BACD_TA` | Never | `Only0` |  |
| Negai Boshi Jirachi (Match Recipient) | 05 | `ネガイボシ` | Japanese | 30719 | `BACD_U_AX` | Never | `Recipient` |  |
| Tanabata Jirachi (2004) | 05 | `タナバタ` | Japanese | 40707 | `BACD_R_A` | Never | `Only1` |  |
| ANA Pikachu | 10 | `ＡＮＡ` | Japanese | 41205 | `BACD_R_A` | Never | `Only0` |  |
| PokéPark Meowth | 05 | `ポケパーク` | Japanese | 50318 | `BACD_R_A` | Never | `Only0` |  |
| Yokohama Pikachu | 10 | `ヨコハマ` | Japanese | 50319 | `BACD_R_A` | Never | `Only0` |  |
| Hadou Mew | 10 | `ハドウ` | Japanese | 50716 | `BACD_R_A` | Never | `RandD3` | incontro fatidico |
| GW Pikachu | 10 | `ＧＷ` | Japanese | 50425 | `BACD_R_A` | Never | `RandS3` |  |
| Sapporo Pikachu | 10 | `サッポロ` | Japanese | 50701 | `BACD_R_A` | Never | `Only0` |  |
| Tanabata Jirachi (2005) | 05 | `タナバタ` | Japanese | 50707 | `BACD_R_A` | Never | `Only1` |  |
| Festa Metang | 30 | `フェスタ` | Japanese | 02005 | `BACD_R_A` | Never | `Only0` | nastro nazionale |
| Sunday Wobbuffet | 05 | `サンデー` | Japanese | 50701 | `BACD_R_A` | Never | `RandS3` |  |
| Regirock | 40 | `ハドウ` | Japanese | 50901 | `BACD_R_A` | Never | `RandSG15` |  |
| Regice | 40 | `ハドウ` | Japanese | 50901 | `BACD_R_A` | Never | `RandSG15` |  |
| Registeel | 40 | `ハドウ` | Japanese | 50901 | `BACD_R_A` | Never | `RandSG15` |  |
| PokéPark Mew | 30 | `ポケパーク` | Japanese | 60510 | `BACD_R_A` | Never | `RandD3` | incontro fatidico |
| PokéPark Celebi | 30 | `ポケパーク` | Japanese | 60623 | `BACD_R_A` | Never | `RandS7` |  |
| Tanabata Jirachi (2006) | 05 | `タナバタ` | Japanese | 60707 | `BACD_R_A` | Never | `RandS7` |  |
| Mitsurin Celebi (2006) | 10 | `ミツリン` | Japanese | 60720 | `BACD_R_A` | Never | `RandS7` |  |
| PokéPark Jirachi (2006) | 30 | `ポケパーク` | Japanese | 60731 | `BACD_R_A` | Never | `RandD3` |  |
| PokéPark Jirachi (2006) | 30 | `ポケパーク` | Japanese | 60830 | `BACD_R_A` | Never | `RandD3` |  |

### Insieme `International`


Blocco: EBGames/GameStop (March 1, 2004, to April 22, 2007), also via multi-game discs

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Berry Fix Ruby | 5 | `RUBY` | English | 30317 | `BACD_RBCD` | Always | `RandD3_1` |  |
| Berry Fix Sapphire | 5 | `SAPHIRE` | English | 30317 | `BACD_RBCD` | Always | `RandD3_0` |  |

Blocco: English

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Charizard | 70 | `10ANNIV` | English | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Pikachu | 70 | `10ANNIV` | English | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Articuno | 70 | `10ANNIV` | English | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Raikou | 70 | `10ANNIV` | English | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Entei | 70 | `10ANNIV` | English | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Suicune | 70 | `10ANNIV` | English | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Lugia | 70 | `10ANNIV` | English | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Ho-Oh | 70 | `10ANNIV` | English | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Latias | 70 | `10ANNIV` | English | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Latios | 70 | `10ANNIV` | English | 06227 | `BACD_R_A` | Never | `RandS7` |  |

Blocco: French

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Charizard | 70 | `10ANNIV` | French | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Pikachu | 70 | `10ANNIV` | French | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Articuno | 70 | `10ANNIV` | French | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Raikou | 70 | `10ANNIV` | French | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Entei | 70 | `10ANNIV` | French | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Suicune | 70 | `10ANNIV` | French | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Lugia | 70 | `10ANNIV` | French | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Ho-Oh | 70 | `10ANNIV` | French | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Latias | 70 | `10ANNIV` | French | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Latios | 70 | `10ANNIV` | French | 06227 | `BACD_R_A` | Never | `RandS7` |  |

Blocco: German

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Charizard | 70 | `10JAHRE` | German | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Pikachu | 70 | `10JAHRE` | German | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Articuno | 70 | `10JAHRE` | German | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Raikou | 70 | `10JAHRE` | German | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Entei | 70 | `10JAHRE` | German | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Suicune | 70 | `10JAHRE` | German | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Lugia | 70 | `10JAHRE` | German | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Ho-Oh | 70 | `10JAHRE` | German | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Latias | 70 | `10JAHRE` | German | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Latios | 70 | `10JAHRE` | German | 06227 | `BACD_R_A` | Never | `RandS7` |  |

Blocco: Italian

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Charizard | 70 | `10ANNI` | Italian | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Pikachu | 70 | `10ANNI` | Italian | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Articuno | 70 | `10ANNI` | Italian | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Raikou | 70 | `10ANNI` | Italian | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Entei | 70 | `10ANNI` | Italian | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Suicune | 70 | `10ANNI` | Italian | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Lugia | 70 | `10ANNI` | Italian | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Ho-Oh | 70 | `10ANNI` | Italian | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Latias | 70 | `10ANNI` | Italian | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Latios | 70 | `10ANNI` | Italian | 06227 | `BACD_R_A` | Never | `RandS7` |  |

Blocco: Spanish

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Charizard | 70 | `10ANIV` | Spanish | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Pikachu | 70 | `10ANIV` | Spanish | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Articuno | 70 | `10ANIV` | Spanish | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Raikou | 70 | `10ANIV` | Spanish | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Entei | 70 | `10ANIV` | Spanish | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Suicune | 70 | `10ANIV` | Spanish | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Lugia | 70 | `10ANIV` | Spanish | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Ho-Oh | 70 | `10ANIV` | Spanish | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Latias | 70 | `10ANIV` | Spanish | 06227 | `BACD_R_A` | Never | `RandS7` |  |
| Latios | 70 | `10ANIV` | Spanish | 06227 | `BACD_R_A` | Never | `RandS7` |  |

Blocco: Aura Mew

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Mew | 10 | `Aura` |  | 20078 | `BACD_R_A` | Never | `RandS7` | incontro fatidico |

Blocco: English Events

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Metang | 30 | `ROCKS` | English | 02005 | `BACD_R_A` | Never | `Only0` | nastro nazionale |
| Deoxys | 70 | `DOEL` | English | 28606 | `BACD_R_A` | Never | `RandS7` | incontro fatidico |
| Deoxys | 70 | `SPACE C` | English | 00010 | `BACD_R_A` | Never | `RandS7` | incontro fatidico |

Blocco: Party of the Decade

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Bulbasaur | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Charizard | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Blastoise | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Pikachu (Fly) | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Alakazam | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Articuno | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Zapdos | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Moltres | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Dragonite | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Typhlosion | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Espeon | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Umbreon | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Raikou | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Entei | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Suicune | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Tyranitar | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Blaziken | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Absol | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Latias | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |
| Latios | 70 | `10 ANIV` | English | 06808 | `BACD_R_A` | Never | `RandS7` |  |

Blocco: Journey Across America

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Bulbasaur | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Charizard | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Blastoise | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Pikachu (No Fly) | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Alakazam | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Articuno | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Zapdos | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Moltres | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Dragonite | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Typhlosion | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Espeon | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Umbreon | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Raikou | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Entei | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Suicune | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Tyranitar | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Celebi | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Blaziken | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Absol | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Latias | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |
| Latios | 70 | `10 ANIV` | English | 00010 | `BACD_R_A` | Never | `RandS7` |  |

### Insieme `Eggs`


Blocco: Pokémon Box -- Recipient

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Swablu Egg with False Swipe | 5 | `ＡＺＵＳＡ` |  |  | `BACD_U` |  | `Only1` |  |
| Zigzagoon Egg with Extreme Speed | 5 | `ＡＺＵＳＡ` |  |  | `BACD_U` |  | `Only1` |  |
| Skitty Egg with Pay Day | 5 | `ＡＺＵＳＡ` |  |  | `BACD_U` |  | `Only1` |  |
| Pichu Egg with Surf | 5 | `ＡＺＵＳＡ` |  |  | `BACD_U` |  | `Only1` |  |

Blocco: PCJP - Pokémon Center 5th Anniversary Eggs (April 25 to May 18, 2003)

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Pichu with Teeter Dance | 5 | `PCJPEggTrainerName` |  |  | `BACD_TS` | Always | `Only0` |  |
| Pichu with Wish | 5 | `PCJPEggTrainerName` |  |  | `BACD_TS` | Always | `Only0` |  |
| Pichu with Teeter Dance | 5 | `PCJPEggTrainerName` |  |  | `BACD_TA` |  | `Only0` |  |
| Pichu with Wish | 5 | `PCJPEggTrainerName` |  |  | `BACD_TA` |  | `Only0` |  |
| Ralts with Charm | 5 | `PCJPEggTrainerName` |  |  | `BACD_TA` |  | `Only0` |  |
| Ralts with Wish | 5 | `PCJPEggTrainerName` |  |  | `BACD_TA` |  | `Only0` |  |
| Absol with Spite | 5 | `PCJPEggTrainerName` |  |  | `BACD_TA` |  | `Only0` |  |
| Absol with Wish | 5 | `PCJPEggTrainerName` |  |  | `BACD_TA` |  | `Only0` |  |
| Bagon with Iron Defense | 5 | `PCJPEggTrainerName` |  |  | `BACD_TA` |  | `Only0` |  |
| Bagon with Wish | 5 | `PCJPEggTrainerName` |  |  | `BACD_TA` |  | `Only0` |  |

Blocco: PCJP Egg Pokémon Present Eggs - Wondercard (March 21 to April 4, 2004)

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Oddish with Leech Seed | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Meowth with Petal Dance | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Poliwag with Sweet Kiss | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Bellsprout with Teeter Dance | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |

Blocco: PCNY Wish Eggs - Wondercard (December 16, 2004, to January 2, 2005)

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Farfetch'd with Wish & Yawn | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Drowzee with Wish & Belly Drum | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Exeggcute with Wish & Sweet Scent | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Lickitung with Wish & Heal Bell | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Chansey with Wish & Sweet Scent | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Kangaskhan with Wish & Yawn | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |

Blocco: PokéPark Eggs - Wondercard (March 12 to May 8, 2005)

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Psyduck with Mud Sport | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Pichu with Follow me | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Igglybuff with Tickle | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Corsola with Mud Sport | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Taillow with Feather Dance | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Surskit with Mud Sport | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Whismur with Teeter Dance | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Skitty with Rollout | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Plusle with Water Sport | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Minun with Mud Sport | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Spoink with Uproar | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Spinda with Sing | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Cacnea with Encore | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Corphish with Water Sport | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |
| Wynaut with Tickle | 5 | `M2WishEggOT` |  |  | `Method_2` |  |  | incontro fatidico |

Blocco: PokéPark  Eggs - DS Download Play (March 12 to May 8, 2005)

| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |
|---|---|---|---|---|---|---|---|---|
| Psyduck with Mud Sport | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Pichu with Follow Me | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Igglybuff with Tickle | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Corsola with Mud Sport | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Taillow with Feather Dance | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Surskit with Mud Sport | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Whismur with Teeter Dance | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Skitty with Rollout | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Plusle with Water Sport | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Minun with Mud Sport | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Spoink with Uproar | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Spinda with Sing | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Cacnea with Encore | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Corphish with Water Sport | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
| Wynaut with Tickle | 5 | `ポケパーク` |  | 50318 | `BACD_R` |  | `Only0` |  |
