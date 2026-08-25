---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - pokemon-gen12-gen3-bridge-original-hardware/
stato: documento di conoscenza, non di stato
---

# Formato dei dati Pokemon nelle generazioni 1, 2 e 3

Questo documento copre il buco tecnico che l'handoff di ricerca aveva lasciato aperto: il formato dei dati byte per byte, che e' l'unica base su cui si puo' scrivere un parser, un writer o un convertitore, in qualunque delle quattro opzioni implementative registrate in ADR-008 si decida di andare. Non e' uno stato di avanzamento: e' conoscenza, e come tale non va aggiornato quando il progetto avanza, ma solo quando una fonte corregge un fatto.

Tutto cio' che segue e' stato verificato sul disassemblato e sulla decompilazione dei giochi, non sull'enciclopedia. Dove le due si contraddicono ha vinto il sorgente, e la contraddizione e' annotata sul posto perche' e' informazione utile: dice dove non fidarsi della wiki. Le fonti stanno nel registro `SOURCES.md` nella radice del repository, condiviso con gli altri sottoprogetti. Il percorso di studio guidato di questi stessi concetti sta in `docs/`, con il suo indice in `docs/index.md`.

## 1. Tre invarianti da fissare prima di leggere qualsiasi offset

Il primo invariante e' l'ordine dei byte. Le generazioni 1 e 2 girano su un processore Sharp LR35902 e scrivono i campi multibyte in *big-endian*, quindi l'esperienza a tre byte e le statistiche a due byte si leggono dal byte piu' significativo. La generazione 3 gira su ARM7TDMI e scrive tutto in *little-endian*. Un convertitore che sbaglia questo punto produce numeri plausibili ma errati, ed e' l'errore piu' facile da non notare, perche' un livello 100 letto al contrario resta un numero valido.

Il secondo invariante e' la distinzione fra struttura di box e struttura di squadra. In tutte e tre le generazioni la struttura conservata nel deposito e' un prefisso di quella della squadra: i campi in eccesso della squadra sono valori derivati, cioe' livello, statistiche calcolate e punti salute correnti, che il gioco ricalcola quando il Pokemon esce dal box. Un convertitore che scrive nel box non deve calcolare quei campi, un convertitore che scrive nella squadra deve calcolarli tutti e correttamente, e il secondo caso e' molto piu' rischioso.

Il terzo invariante e' che il soprannome del Pokemon e il nome dell'allenatore originale non stanno dentro la struttura nelle generazioni 1 e 2. Stanno in array paralleli, esterni alla struttura, indicizzati dalla posizione nella lista, insieme a una lista separata degli indici di specie. In generazione 3 sono invece dentro la struttura del singolo Pokemon. E' una differenza architetturale, non un dettaglio di offset, e cambia la forma del codice: in Gen 1 e 2 si parsifica una lista con quattro array paralleli, in Gen 3 si parsifica un array di record autocontenuti.

## 2. Generazione 1: struttura del Pokemon

La struttura di box occupa 33 byte, quella di squadra 44, e le due costanti sono dichiarate nel disassemblato come `BOXMON_STRUCT_LENGTH EQU $21` e `PARTYMON_STRUCT_LENGTH EQU $2c`. La forma canonica e' la macro `box_struct` di `pret/pokered`, che riporto verbatim perche' e' la definizione autorevole, e la macro `party_struct` che la estende.

```
box_struct:                      party_struct:
    \1Species::    db              box_struct \1
    \1HP::         dw              \1Level::      db
    \1BoxLevel::   db              \1Stats::
    \1Status::     db              \1MaxHP::      dw
    \1Type1::      db              \1Attack::     dw
    \1Type2::      db              \1Defense::    dw
    \1CatchRate::  db              \1Speed::      dw
    \1Moves::      ds NUM_MOVES    \1Special::    dw
    \1OTID::       dw
    \1Exp::        ds 3
    \1HPExp::      dw
    \1AttackExp::  dw
    \1DefenseExp:: dw
    \1SpeedExp::   dw
    \1SpecialExp:: dw
    \1DVs::        dw
    \1PP::         ds NUM_MOVES
```

Tradotta in offset assoluti, la struttura e' la seguente. Gli offset della Stat Experience sono confermati in modo indipendente dalla tabella `hpStatExp`, `atkStatExp`, `defStatExp`, `speStatExp` e `spcStatExp` del PCCS, che li dichiara a 0x11, 0x13, 0x15, 0x17 e 0x19 per la generazione 1.

| Offset | Dim. | Campo | Nota |
|---|---|---|---|
| 0x00 | 1 | Indice di specie | indice interno, non numero del Pokedex, vedi sezione 8 |
| 0x01 | 2 | Punti salute correnti | big-endian |
| 0x03 | 1 | Livello di box | ridondante con 0x21 nella struttura di squadra |
| 0x04 | 1 | Condizione di stato | campo di bit |
| 0x05 | 1 | Tipo 1 | copia denormalizzata del dato di specie |
| 0x06 | 1 | Tipo 2 | idem |
| 0x07 | 1 | Tasso di cattura | in Gen 2 questo byte diventa l'oggetto tenuto |
| 0x08 | 4 | Mosse 1 a 4 | un byte di indice per mossa |
| 0x0C | 2 | ID dell'allenatore originale | 16 bit, non 32 come in Gen 3 |
| 0x0E | 3 | Esperienza | intero a 24 bit big-endian |
| 0x11 | 10 | Stat Experience | cinque campi da 2 byte: PS, Attacco, Difesa, Velocita', Speciale |
| 0x1B | 2 | DV | quattro nibble, vedi sotto |
| 0x1D | 4 | PP delle quattro mosse | PP correnti e PP Up nello stesso byte |
| 0x21 | 1 | Livello | solo struttura di squadra |
| 0x22 | 10 | Statistiche calcolate | PS massimi, Attacco, Difesa, Velocita', Speciale |

Il doppio campo di livello a 0x03 e 0x21 e' una trappola concreta: il gioco usa quello di squadra e ricalcola quello di box al deposito, quindi un writer che ne aggiorna solo uno produce un Pokemon che cambia livello quando entra o esce dal box. Il byte a 0x07 e' l'altro punto sensibile, perche' in Gen 1 e' il tasso di cattura, dato di specie che non ha senso conservare, mentre nella stessa posizione Gen 2 mette l'oggetto tenuto: e' esattamente questo riuso il motivo per cui il Time Capsule ufficiale fa comparire oggetti apparentemente casuali sui Pokemon che salgono da Gen 1.

I DV[^1] sono impaccati in due byte come quattro nibble. L'ordine e' verificato sul sorgente, nella routine `CalcMonStatC` di `engine/pokemon/move_mon.asm` in `pret/pokecrystal`: il primo byte porta l'Attacco nel nibble alto e la Difesa nel nibble basso, il secondo porta la Velocita' nel nibble alto e lo Speciale nel nibble basso. Il DV dei punti salute non e' memorizzato e la sua derivazione e' scritta come commento nel disassemblato stesso, che vale piu' di qualsiasi parafrasi.

```
; DV_HP = (DV_ATK & 1) << 3 | (DV_DEF & 1) << 2 | (DV_SPD & 1) << 1 | (DV_SPC & 1)
```

Questa derivazione ha una conseguenza pesante sulla conversione: il DV dei punti salute non e' un grado di liberta' indipendente, quindi qualunque manipolazione dei DV in conversione trascina anche i punti salute. La stessa routine mostra un secondo fatto strutturale, cioe' che sia l'Attacco Speciale sia la Difesa Speciale saltano al medesimo ramo `.Special`: in Gen 2 le due statistiche sono separate ma condividono un solo DV e una sola Stat Experience.

Ogni byte di PP contiene due informazioni: i sei bit meno significativi sono i PP correnti, da 0 a 63, e i due bit piu' significativi sono il numero di PP Up applicati, da 0 a 3. In Gen 3 il numero di PP Up si sposta in un campo dedicato dentro la sottostruttura Growth, quindi la conversione deve smontare questo byte e distribuirlo su due posti diversi.

La lista della squadra e' un record composto da un contatore a un byte, sette byte di indici di specie terminati da 0xFF, poi sei strutture da 44 byte, poi sei nomi di allenatore originale da 11 byte, poi sei soprannomi da 11 byte. La lista di un box ha la stessa forma con venti elementi e strutture da 33 byte. Il terminatore 0xFF nella lista di specie non e' decorativo: e' la condizione di uscita dei cicli del gioco, e la sua assenza e' precisamente la primitiva su cui si costruisce l'esecuzione di codice arbitrario descritta nella sezione 10.

## 3. Generazione 1: struttura del salvataggio

Il salvataggio e' la SRAM[^2] della cartuccia, 32 KiB divisi in quattro banchi da 8 KiB. Gli offset che contano per un tool sono i seguenti, e valgono identici fra Rosso, Blu e Giallo per tutto cio' che riguarda i Pokemon.

| Offset | Contenuto |
|---|---|
| 0x2598 | inizio dell'area coperta dal checksum principale |
| 0x25A3 | nome del giocatore, 11 byte |
| 0x2F2C | lista della squadra, 404 byte cioe' 0x194 |
| 0x30C0 | box corrente, 1122 byte |
| 0x3523 | checksum principale, 1 byte |
| 0x4000 | box da 1 a 6, passo 0x462 |
| 0x5A4C | checksum aggregato dei box del banco 2, seguito da 6 checksum singoli |
| 0x6000 | box da 7 a 12, passo 0x462 |
| 0x7A4C | checksum aggregato dei box del banco 3, seguito da 6 checksum singoli |

Sulla dimensione della lista della squadra c'e' una trappola che vale segnalare, perche' l'ho trovata scrivendo il codice e non leggendo: la fonte secondaria riporta 194 byte, ma il conto dei campi da' 1 contatore piu' 7 di lista specie piu' sei strutture da 44 piu' due array di sei nomi da 11, cioe' 404 byte, che in esadecimale e' 0x194. La fonte ha letto la dimensione esadecimale come decimale. Il valore corretto e' 404, ed e' verificato da un'asserzione nei test.

Il checksum principale e' il complemento a uno della somma dei byte da 0x2598 a 0x3522, equivalentemente si parte da 255 e si sottrae ogni byte. Se non torna, il gioco dichiara i dati distrutti e riparte da zero, quindi qualunque scrittura su un salvataggio Gen 1 deve ricalcolare il checksum, e questo vale sia per un tool che lavora su un dump sia per una routine che scrive in SRAM da dentro il gioco.

## 4. Generazione 2: struttura del Pokemon

La struttura di box passa a 32 byte e quella di squadra a 48. Il cambiamento non e' un'estensione: e' un riordino, quindi non si puo' riusare il parser di Gen 1 con un offset diverso. Anche qui gli offset della Stat Experience sono confermati dalla tabella del PCCS, che per la generazione 2 li dichiara a 0x0B, 0x0D, 0x0F, 0x11 e 0x13.

| Offset | Dim. | Campo | Nota |
|---|---|---|---|
| 0x00 | 1 | Indice di specie | qui coincide con il numero del Pokedex nazionale |
| 0x01 | 1 | Oggetto tenuto | stessa posizione del tasso di cattura di Gen 1 |
| 0x02 | 4 | Mosse 1 a 4 | |
| 0x06 | 2 | ID dell'allenatore originale | |
| 0x08 | 3 | Esperienza | 24 bit big-endian |
| 0x0B | 10 | Stat Experience | PS, Attacco, Difesa, Velocita', Speciale |
| 0x15 | 2 | DV | stesso impaccamento di Gen 1, quattro nibble |
| 0x17 | 4 | PP delle quattro mosse | stesso schema a 6 piu' 2 bit |
| 0x1B | 1 | Amicizia, oppure cicli di cova se e' un uovo | campo nuovo, non esiste in Gen 1 |
| 0x1C | 1 | Pokerus | nibble alto ceppo, nibble basso giorni residui |
| 0x1D | 2 | Dati di cattura | popolato solo da Cristallo |
| 0x1F | 1 | Livello | fine della struttura di box |
| 0x20 | 1 | Condizione di stato | inizio dei campi di sola squadra |
| 0x22 | 2 | Punti salute correnti | |
| 0x24 | 12 | Statistiche calcolate | PS massimi, Attacco, Difesa, Velocita', Att. Speciale, Dif. Speciale |

I due byte dei dati di cattura, presenti solo in Cristallo, sono impaccati cosi': nel primo byte i due bit alti sono il momento della giornata, con 1 mattina, 2 giorno e 3 notte, e i sei bit bassi sono il livello di cattura; nel secondo byte il bit alto e' il sesso dell'allenatore, con 0 maschio e 1 femmina, e i sette bit bassi sono l'indice del luogo. Questo e' il solo posto in tutte le generazioni 1 e 2 dove esista un dato di provenienza, e per questo il PCCS puo' conservare il sesso dell'allenatore soltanto da Cristallo e deve inventarlo, di norma maschio, per ogni altro gioco sorgente.

La lucentezza in Gen 2 non e' un flag ma un pattern di DV: un Pokemon e' lucente se e solo se i DV di Difesa, Velocita' e Speciale valgono tutti 10 e il DV di Attacco vale 2, 3, 6, 7, 10, 11, 14 o 15. In Gen 3 la lucentezza e' invece una proprieta' del valore di personalita' e dell'ID dell'allenatore, quindi conservare la lucentezza in conversione non e' copiare un bit: e' un vincolo da soddisfare, e la sezione 9 mostra con quale variabile libera il PCCS lo soddisfa.

Gli offset del salvataggio Gen 2 dipendono dal gioco e dalla lingua. Per le versioni inglesi la lista della squadra sta a 0x288A in Oro e Argento e a 0x2865 in Cristallo, i box da 1 a 7 partono da 0x4000 e quelli da 8 a 14 da 0x6000, con venti Pokemon per box e strutture da 32 byte. Il checksum principale sta a 0x2D69 in Oro e Argento, calcolato sui byte da 0x2009 a 0x2D68, e a 0x2D0D in Cristallo, calcolato da 0x2009 a 0x2B82; esiste in entrambi i casi una copia di backup con un secondo checksum, contigua in Cristallo e frammentata in Oro e Argento.

## 5. Generazione 3: la struttura cifrata

Qui cambia la natura del problema. La struttura di box e' 80 byte e quella di squadra 100, ma i 48 byte centrali sono cifrati e permutati, e la loro integrita' e' protetta da un checksum che, se non torna, trasforma il Pokemon in un Uovo Difettoso, cioe' lo distrugge in modo visibile e definitivo. Un writer che sbaglia un solo passo di questa catena non produce un Pokemon strano: produce un Uovo Difettoso.

L'intestazione in chiaro e' questa, e viene dalla struttura `BoxPokemon` di `pret/pokeemerald`.

| Offset | Dim. | Campo |
|---|---|---|
| 0x00 | 4 | Valore di personalita' |
| 0x04 | 4 | ID dell'allenatore originale, 32 bit: 16 bit visibili piu' 16 bit di ID segreto |
| 0x08 | 10 | Soprannome |
| 0x12 | 1 | Lingua |
| 0x13 | 1 | Flag: uovo difettoso, ha specie, e' uovo, blocco box RS |
| 0x14 | 7 | Nome dell'allenatore originale |
| 0x1B | 1 | Marcature |
| 0x1C | 2 | Checksum dei 48 byte cifrati |
| 0x1E | 2 | Sconosciuto, riempimento |
| 0x20 | 48 | Quattro sottostrutture da 12 byte, cifrate e permutate |

La cifratura e' verificata sul sorgente e sta in `EncryptBoxMon` di `src/pokemon.c`, dove il blocco e' visto come `u32 raw[12]` e ogni parola viene messa in XOR prima con il valore di personalita' e poi con l'ID dell'allenatore, cioe' in XOR con la loro combinazione. La decifratura e' la stessa operazione nell'ordine inverso, che e' la stessa cosa.

```c
static void EncryptBoxMon(struct BoxPokemon *boxMon)
{
    u32 i;
    for (i = 0; i < ARRAY_COUNT(boxMon->secure.raw); i++)
    {
        boxMon->secure.raw[i] ^= boxMon->personality;
        boxMon->secure.raw[i] ^= boxMon->otId;
    }
}
```

La permutazione e' determinata dal valore di personalita' modulo 24 e stabilisce in quale dei quattro slot da 12 byte si trovi ciascuna sottostruttura, secondo la tabella seguente, dove G sta per Growth, A per Attacks, E per EV e condizione, M per Miscellaneous.

| PV mod 24 | Ordine | PV mod 24 | Ordine | PV mod 24 | Ordine | PV mod 24 | Ordine |
|---|---|---|---|---|---|---|---|
| 0 | GAEM | 6 | AGEM | 12 | EGAM | 18 | MGAE |
| 1 | GAME | 7 | AGME | 13 | EGMA | 19 | MGEA |
| 2 | GEAM | 8 | AEGM | 14 | EAGM | 20 | MAGE |
| 3 | GEMA | 9 | AEMG | 15 | EAMG | 21 | MAEG |
| 4 | GMAE | 10 | AMGE | 16 | EMGA | 22 | MEGA |
| 5 | GMEA | 11 | AMEG | 17 | EMAG | 23 | MEAG |

Sul checksum le fonti secondarie sbagliano, e l'errore e' del tipo che distrugge un Pokemon: una pagina enciclopedica descrive la somma come byte per byte. Il sorgente dice altro. In `include/pokemon.h` la sottostruttura e' una unione che espone anche `u16 raw[NUM_SUBSTRUCT_BYTES / 2]`, cioe' sei parole da 16 bit, e `CalculateBoxMonChecksum` somma quelle parole in un accumulatore `u16`, per tutte e quattro le sottostrutture, lasciando che l'aritmetica tronchi naturalmente a 16 bit.

```c
static u16 CalculateBoxMonChecksum(struct BoxPokemon *boxMon)
{
    u16 checksum = 0;
    /* quattro chiamate a GetSubstruct, una per sottostruttura */
    for (i = 0; i < (s32)ARRAY_COUNT(substruct0->raw); i++)
        checksum += substruct0->raw[i];
    /* idem per substruct1, substruct2, substruct3 */
    return checksum;
}
```

Le quattro sottostrutture, dalle definizioni verbatim di `include/pokemon.h`, sono le seguenti. Growth contiene specie a 16 bit, oggetto tenuto a 16 bit, esperienza a 32 bit, bonus PP a 8 bit, amicizia a 8 bit e due byte di riempimento. Attacks contiene quattro indici di mossa a 16 bit e quattro byte di PP. La sottostruttura degli EV e della condizione contiene sei byte di EV[^4], nell'ordine PS, Attacco, Difesa, Velocita', Att. Speciale, Dif. Speciale, poi cinque byte di statistiche da gara e un byte di lucentezza estetica. Miscellaneous e' quella densa di campi di bit, e vale la pena scriverla per bit.

```
byte 0        Pokerus: bit 0-3 giorni residui, bit 4-7 ceppo
byte 1        Luogo di incontro, indice a 8 bit
byte 2-3      Origini, parola a 16 bit:
                bit 0-6    livello di incontro
                bit 7-10   gioco di origine (1 Zaffiro, 2 Rubino, 3 Smeraldo,
                           4 Rosso Fuoco, 5 Verde Foglia, 15 Colosseum e XD)
                bit 11-14  Poke Ball di cattura
                bit 15     sesso dell'allenatore
byte 4-7      IV, uovo e abilita', parola a 32 bit:
                bit 0-4    IV PS          bit 15-19  IV Velocita'
                bit 5-9    IV Attacco     bit 20-24  IV Att. Speciale
                bit 10-14  IV Difesa      bit 25-29  IV Dif. Speciale
                bit 30     flag uovo
                bit 31     slot di abilita'
byte 8-11     Nastri e obbedienza, parola a 32 bit:
                bit 0-14   cinque nastri da gara, 3 bit ciascuno
                bit 15-26  nastri di merito, 1 bit ciascuno
                bit 31     obbedienza, letto come incontro fatidico
                           dalle generazioni successive
```

I venti byte in piu' della struttura di squadra sono, in ordine, stato a 32 bit, livello a 8 bit, identificatore di posta a 8 bit con 0xFF quando non c'e' posta, e poi sette statistiche a 16 bit, cioe' punti salute correnti, punti salute massimi, Attacco, Difesa, Velocita', Attacco Speciale e Difesa Speciale.

## 6. Generazione 3: struttura del salvataggio

Il salvataggio e' 128 KiB di memoria flash e la sua organizzazione e' completamente diversa da quella lineare delle generazioni precedenti, perche' e' progettata per la scrittura a blocchi tipica della flash e per la resistenza a un'interruzione di corrente a meta' del salvataggio.

| Offset | Dim. | Contenuto |
|---|---|---|
| 0x000000 | 57344 | slot di salvataggio A, 14 sezioni da 4096 byte |
| 0x00E000 | 57344 | slot di salvataggio B, 14 sezioni da 4096 byte |
| 0x01C000 | 8192 | Sala d'Onore |
| 0x01E000 | 4096 | Dono Segreto ed e-Reader |
| 0x01F000 | 4096 | battaglia registrata |

Ogni sezione da 4096 byte ha un piede fisso: identificatore di sezione a 0x0FF4, checksum a 0x0FF6, firma a 0x0FF8 con il valore costante 0x08012025, e indice di salvataggio a 0x0FFC. La firma sbagliata invalida la sezione e con essa l'intero slot. Il checksum si calcola accumulando in una variabile a 32 bit le parole da 32 bit little-endian della sezione, per un numero di byte che dipende dall'identificatore di sezione, poi sommando i 16 bit alti ai 16 bit bassi: il risultato a 16 bit e' il checksum. La scelta dello slot valido segue l'indice di salvataggio, con lo slot A vincente solo se il suo indice e' strettamente maggiore, quindi in caso di parita' vince B.

Le sezioni che interessano un ponte sono la 1, cioe' squadra e oggetti, e le sezioni dalla 5 alla 13, che insieme formano un unico buffer contiguo di 33744 byte per il deposito. Nella sezione 1 il conteggio della squadra e le sei strutture da 100 byte stanno a 0x0234 e 0x0238 in Rubino, Zaffiro e Smeraldo, e a 0x0034 e 0x0038 in Rosso Fuoco e Verde Foglia. Nel buffer del deposito l'indice del box corrente sta a 0x0000, i 420 record da 80 byte partono da 0x0004, i quattordici nomi dei box stanno a 0x8344 con passo 9 byte e gli sfondi a 0x83C2.

Un dettaglio di questa sezione riguarda direttamente il sottoprogetto dell'inventario corrotto di Smeraldo, ed e' verificato sul sorgente invece che riportato. In `include/global.h` di pokeemerald la struttura del blocco di salvataggio 2, che e' la sezione 0, dichiara il campo con il suo offset in commento.

```c
    /*0xA8*/ u32 gcnLinkFlags; // Read by Pokémon Colosseum/XD
    /*0xAC*/ u32 encryptionKey;
```

E in `src/item.c` la quantita' di un oggetto nello zaino non e' mai in chiaro, mentre quella di un oggetto nel deposito PC lo e' sempre.

```c
static u16 GetBagItemQuantity(u16 *quantity)
{
    return gSaveBlock2Ptr->encryptionKey ^ *quantity;
}

static u16 GetPCItemQuantity(u16 *quantity)
{
    return *quantity;
}
```

La conseguenza pratica per la diagnosi e' precisa e va oltre quanto dicono le fonti secondarie: in Smeraldo le quantita' dello zaino sono mascherate in XOR con i 16 bit bassi della chiave, quelle del deposito PC non lo sono, e Rubino e Zaffiro non mascherano nulla. Una quantita' assurda letta in chiaro dallo zaino non e' una prova di corruzione, e' l'aspetto normale di un dato mascherato; una quantita' assurda nel deposito PC invece e' un dato davvero anomalo. Lo strumento che applica questa distinzione a un dump reale e' `gba-save-extraction-smeraldo/tools/emerald_bag_decode.py`.

## 7. Codifica dei caratteri

Nessuna delle tre generazioni usa ASCII, e le due tabelle sono incompatibili fra loro, quindi la conversione di un soprannome e di un nome di allenatore e' una transcodifica vera, non una copia di byte. Su questo punto le fonti secondarie sbagliano due volte, e l'errore e' silenzioso perche' produce comunque caratteri stampabili: la pagina enciclopedica di Gen 1 colloca le cifre a 0xF0 e quella di Gen 3 colloca le maiuscole a 0xC1. I valori corretti vengono dai charmap dei disassemblati.

| Elemento | Gen 1 e 2 | Gen 3 |
|---|---|---|
| Terminatore | 0x50 | 0xFF |
| Spazio | 0x7F | 0x00 |
| Lettere A a Z | 0x80 a 0x99 | 0xBB a 0xD4 |
| Lettere a a z | 0xA0 a 0xB9 | 0xD5 a 0xEE |
| Cifre 0 a 9 | 0xF6 a 0xFF | 0xA1 a 0xAA |

Perche' l'errore non si ripeta, queste tabelle non vanno ricopiate a mano dentro il codice: si generano dai charmap del disassemblato con `tools/extract_charmaps.py`, che produce `data/charmap-gen12.json` e `data/charmap-gen3.json` e li verifica contro i valori di controllo qui sopra. Il principio e' quello della regola di token economy del progetto, cioe' spingere il lavoro deterministico su codice e conservarne l'esito come stato ispezionabile su disco.

La tabella di Gen 2 e' quasi identica a quella di Gen 1 per tutti i caratteri che il giocatore puo' digitare, ed e' esattamente questa compatibilita' a rendere possibile il Time Capsule senza transcodifica. Verso Gen 3 invece serve una tabella di traduzione esplicita, con due complicazioni. La prima e' che le lunghezze non coincidono: dieci caratteri piu' terminatore in Gen 1 e 2 contro dieci byte per il soprannome e sette per il nome dell'allenatore in Gen 3, quindi un nome di allenatore lungo va troncato. La seconda e' che alcuni codici sono di controllo, e in Gen 3 in particolare 0xFC introduce sequenze di formattazione, 0xFD introduce variabili di testo e 0xFE e' un'interruzione di riga: un byte di questi finito in un soprannome per errore di transcodifica non e' un carattere sbagliato, e' un comando dentro un nome.

## 8. Indici di specie: tre spazi di numerazione diversi

Nessuna delle tre generazioni identifica la specie con il numero del Pokedex nazionale, e le tre numerazioni sono diverse fra loro. Una tabella di mappatura non e' un optional del convertitore: e' il suo cuore.

In Gen 1 l'indice interno non ha alcuna relazione ordinata con il Pokedex. L'indice 1 e' Rhydon, che e' il numero 112, l'indice 99 e' Bulbasaur, che e' il numero 1. Nell'intervallo valido sono sparse 39 posizioni che non corrispondono a nessuna specie e che il gioco interpreta come MissingNo, e l'indice 0 e tutti gli indici da 191 a 255 sono altrettanto invalidi. Un parser deve quindi trattare l'indice di specie come una chiave opaca da risolvere in tabella, e deve avere una politica esplicita per gli indici invalidi.

In Gen 2 l'indice coincide con il numero del Pokedex nazionale, e i Pokemon di Johto seguono in ordine a partire dall'indice 191. E' l'unica delle tre generazioni dove la numerazione e' quella che uno si aspetterebbe.

In Gen 3 gli indici da 1 a 251 seguono il Pokedex nazionale, gli indici da 252 a 276 non contengono specie giocabili, e le specie di Hoenn cominciano dall'indice 277 con Treecko in un ordine proprio che non e' quello del Pokedex nazionale. Tutte le forme di Unown condividono l'indice 201, e la lettera e' determinata dal valore di personalita', il che significa che la lettera di Unown non e' un campo da copiare ma un vincolo sulla generazione del valore di personalita'.

Per un ponte da Gen 1 e 2 verso Gen 3 la conseguenza pratica e' benigna: tutte le specie sorgente stanno nell'intervallo da 1 a 251, dove Gen 2 e Gen 3 concordano. Serve quindi una sola tabella, quella da indice interno Gen 1 a numero nazionale, piu' una politica per MissingNo, che il PCCS risolve mappandolo su Porygon.

## 9. Il problema vero della conversione: ricostruire cio' che non esisteva

Tutto quanto sopra e' meccanica. Il problema difficile e' che Gen 3 richiede campi che in Gen 1 e 2 non esistono, e che non sono indipendenti fra loro perche' derivano tutti dallo stesso valore di personalita' a 32 bit. Le formule sono confermate da due implementazioni indipendenti, il gioco e il PCCS, e in `source/Gen3Pokemon.cpp` si leggono in forma compatta: la natura e' il valore di personalita' modulo 25; il sesso confronta `PV & 0xFF` con la soglia di sesso della specie ed e' maschio se il byte e' maggiore o uguale; lo slot di abilita' e' `PV & 1`; la lettera di Unown compone i due bit meno significativi dei quattro byte e prende il modulo 28; la lucentezza si ha quando lo XOR fra ID visibile, ID segreto, meta' bassa e meta' alta del valore di personalita' e' minore di 8.

Ne segue che generare il valore di personalita' non e' scegliere un numero casuale, e' risolvere un problema di soddisfacimento di vincoli, e il PCCS lo risolve nel modo piu' diretto possibile, cioe' campionamento con rifiuto: estrae un candidato dal generatore pseudocasuale e lo scarta finche' non soddisfa contemporaneamente abilita', lettera di Unown, natura, sesso e taglia richieste.

```cpp
    do
    {
        seedA = newPkmn->getNextRand_u16();
        seedB = newPkmn->getNextRand_u16();
        pid = seedA | (seedB << 16);
        newPkmn->setPersonalityValue(pid);
    } while (!(
        newPkmn->getAbilityFromPersonalityValue() == newPkmn->internalAbility &&
        newPkmn->getUnownLetter() == newPkmn->internalUnownLetter &&
        newPkmn->getNature() == newPkmn->internalNature &&
        newPkmn->getGender() == newPkmn->internalGender &&
        newPkmn->getSize() == newPkmn->internalSize));
```

La lucentezza non compare in quella condizione, e la ragione e' la parte piu' elegante di tutto il progetto. L'ID dell'allenatore in Gen 1 e 2 e' a 16 bit, mentre in Gen 3 e' a 32, cioe' ID visibile piu' ID segreto: l'ID segreto e' un valore che la conversione deve inventare comunque, e poiche' la condizione di lucentezza dipende dallo XOR di tutti e quattro i mezzi valori, quell'invenzione e' esattamente la variabile libera che decide la lucentezza a valle di un valore di personalita' gia' fissato. Il PCCS fa precisamente questo: calcola lo XOR parziale dei tre valori noti e assegna all'ID segreto quel risultato per rendere il Pokemon lucente, oppure un valore sicuro per impedirlo.

```cpp
    u16 shinyTest = TID ^ (PV & 0xFFFF) ^ (PV >> 16);
    if (getIsShiny())        newPkmn->setSecretID(shinyTest);   // XOR nullo, lucente
    else if (shinyTest < 8)  newPkmn->setSecretID(51691);       // era lucente per caso, si rompe
    else                     newPkmn->setSecretID(0);
```

C'e' poi una circostanza fortunata che rende trattabile il resto, e va detta esplicitamente perche' non e' ovvia. In Gen 3 gli IV[^3] sono memorizzati in un campo proprio, dentro la sottostruttura Miscellaneous, e non sono derivati dal valore di personalita'. Dalla generazione 4 in poi il legame fra i due passa per il generatore pseudocasuale del metodo di incontro, e una coppia arbitraria di valore di personalita' e IV diventa riconoscibile come impossibile. In Gen 3 quel legame nel dato salvato non c'e', quindi un convertitore puo' scegliere gli IV per conservare le statistiche e il valore di personalita' per conservare sesso, lucentezza e forma, in modo indipendente. E' questa indipendenza a rendere possibile una conversione fedele, e non e' un dettaglio: e' la ragione tecnica per cui il ponte verso Gen 3 e' fattibile con questa fedelta' mentre lo stesso ponte verso una generazione successiva non lo sarebbe.

Restano tre conversioni numeriche non banali, e su queste il codice pubblicato del PCCS dice qualcosa che il suo README non dice. I DV vanno da 0 a 15 e gli IV da 0 a 31, quindi la regola naturale sarebbe il raddoppio, ma `convertIVs` genera sei IV dal generatore pseudocasuale e non li deriva affatto dai DV. Le cinque Stat Experience vanno da 0 a 65535 e i sei EV da 0 a 255 con tetto complessivo di 510, e `convertEVs` li azzera tutti. Il terzo caso e' lo Speciale, che dovrebbe diventare due IV e due EV, e la questione non si pone perche' i primi sono casuali e i secondi nulli.

Ne discende una correzione importante rispetto a quanto l'handoff di ricerca affermava, ed e' il tipo di cosa che si scopre solo leggendo il codice. I quattro metodi PCCS, cioe' ORIGINAL, FAITHFUL, LEGAL e VIRTUAL, compaiono nel repository soltanto dentro il README: nel codice sorgente della release corrente non esiste alcuna occorrenza dei loro nomi, e il comportamento implementato e' quello del solo metodo ORIGINAL. La tabella comparativa dei quattro metodi e' quindi una specifica, non una descrizione di codice esistente, e chi volesse la conversione fedele delle statistiche deve implementarla, non configurarla.

Vale la pena registrare anche un dettaglio minore, perche' insegna qualcosa di generale: in `convertShininess` esiste un caso speciale che, per una specie precisa e per due hash FNV-1a specifici del nome dell'allenatore e del soprannome, forza tutti i DV a 15. E' una scelta arbitraria di quella implementazione, non una regola del formato. Una implementazione di riferimento non e' una specifica, e distinguere le due cose e' esattamente il motivo per cui questo documento cita il gioco e non il tool quando deve stabilire un fatto.

## 10. Il livello di trasporto: protocollo del cavo Link ed esecuzione di codice

Un convertitore che lavora su file di salvataggio non ha bisogno di questa sezione. Un ponte su hardware originale ne ha bisogno tutta, perche' il formato dei dati e' solo meta' del problema: l'altra meta' e' come i byte attraversano il cavo.

Il protocollo seriale del Game Boy e' sincrono e a un byte per volta: un dispositivo fa da master e fornisce il clock, l'altro fa da slave, e ogni trasferimento e' uno scambio simultaneo, perche' il byte in uscita e quello in entrata attraversano lo stesso registro a scorrimento. Le costanti del protocollo sono dichiarate in `constants/serial_constants.asm` e conviene leggerle da la' invece di ricavarle: 0x01 e 0x02 sono i due esiti della negoziazione dei ruoli, il byte di preambolo che delimita ogni blocco e' 0xFD, il byte che significa assenza di dati e' 0xFE, il terminatore di una parte di lista di correzione e' 0xFF, il preambolo e' lungo 6 byte, quello della lista di numeri casuali 7, la lista di numeri casuali 10 e il riempimento finale 3.

La dimensione della struttura di scambio si ricava senza ambiguita' dal codice che la trasmette, in `engine/link/cable_club.asm`, dove il conteggio dei byte e' scritto come somma di costanti.

```
ld bc, SERIAL_PREAMBLE_LENGTH + NAME_LENGTH + 1 + PARTY_LENGTH + 1
        + (PARTYMON_STRUCT_LENGTH + NAME_LENGTH * 2) * PARTY_LENGTH + 3
```

Sostituendo le costanti verificate, cioe' preambolo 6, lunghezza dei nomi 11, squadra 6, struttura di squadra 44 e riempimento 3, si ottiene 6 + 11 + 1 + 6 + 1 + 396 + 3, cioe' 424 byte sul filo e 418 di dati utili senza preambolo. Questo chiude il conflitto fra le fonti secondarie, che davano 415 in un caso e 424 nell'altro: entrambe misuravano una cosa diversa, e la cifra da usare dipende da dove si taglia. La lista di correzione, subito dopo, e' uno scambio di esattamente 200 byte.

Il meccanismo della lista di correzione e' piu' fine di come lo descrivono le sintesi. Il gioco scorre i byte della squadra e, quando ne trova uno uguale a 0xFE, lo sostituisce con 0xFF e ne registra l'indice nella lista, cosi' che il ricevente possa rimetterlo a posto. La lista e' spezzata in due parti perche' anche l'indice registrato e' un byte trasmesso, e un indice uguale a 0xFD verrebbe letto come preambolo: quando il contatore raggiunge quel valore, il gioco chiude la prima parte con 0xFF e riparte a contare per la seconda. Non e' quindi una divisione arbitraria, e' l'unica soluzione possibile dato che il protocollo si riserva due valori.

Il lato Gen 2 ha una struttura propria e piu' ricca, dichiarata in `ram/wram.asm` di pokecrystal, e contiene una scoperta che vale per tutto il progetto. Esistono due strutture di invio distinte. La prima, `wLinkSendParty`, e' quella nativa: preambolo, nome, conteggio, lista di specie, terminatore, identificatore del giocatore a 16 bit, sei strutture da 48 byte, sei nomi di allenatore, sei soprannomi e riempimento, per 450 byte sul filo. La seconda, `wLinkSendTimeCapsuleParty`, ha la stessa forma ma usa una macro chiamata `red_party_struct`, che e' la struttura Gen 1 da 44 byte, non ha l'identificatore del giocatore, e misura 424 byte, cioe' esattamente il blocco di Gen 1.

Questo significa che la conversione fra il formato Gen 1 e il formato Gen 2 esiste gia' dentro il gioco Gen 2, scritta da Game Freak per il Time Capsule, ed e' leggibile nel disassemblato. Per un ponte verso Gen 3 e' il precedente piu' utile che ci sia, perche' mostra come gli autori originali hanno risolto lo stesso genere di problema: quali campi hanno lasciato cadere, quali hanno inventato e come hanno gestito il riuso del byte a 0x07. Il lato Gen 2 trasmette inoltre un blocco separato per la posta, con un preambolo proprio e una propria lista di correzione, e questa e' la ragione strutturale per cui i progetti esistenti dichiarano di non poter trasferire un Pokemon che tiene una lettera.

Su questo protocollo esistono due strategie diverse per il ponte, e la scelta fra le due e' architetturale. La prima e' parlare il protocollo normale, cioe' fingersi una console partner legittima e fare uno scambio vero: e' quello che fa `Pokemon-Gen3-to-Gen-X`, che lo dichiara esplicitamente, ed e' anche quello che fa il circuito stampato di Goppier, con un microcontrollore ARM in mezzo ai due cavi. La seconda e' far eseguire codice proprio al gioco Gen 1 o 2.

Su come lo faccia il progetto di riferimento il README non dice nulla, ma il codice lo dice con chiarezza, e la risposta corregge la descrizione che ne dava l'handoff di ricerca. In `source/gameboy_colour.cpp` di Poke Transporter GB, durante la fase di scambio delle squadre, la funzione che risponde al Game Boy non invia una squadra: invia byte per byte un buffer precalcolato.

```cpp
byte exchange_parties(byte curr_in, byte *curr_payload)
{
  int ret = curr_payload[data_counter];
  data_counter += 1;
  return ret;
};
```

Quel buffer e' un programma Z80. Il repository contiene un generatore di payload con un assemblatore Z80 proprio, `tools/payload-generator/src/payloads/z80_asm.cpp`, un generatore di patch binarie e tabelle di valori di ROM per lingua, oggi inglese e francese. Il payload viene estratto da un file per lingua e variante di gioco tramite `payload_file_reader::read_payload`. Il quadro e' quindi questo: il ponte non chiede al giocatore alcun setup dentro il gioco, non richiede oggetti glitch ne' cloni difettosi, e ottiene l'esecuzione di codice interamente dal lato ricevente, mandando al Game Boy una finta squadra che e' in realta' codice. E' esecuzione di codice remota attraverso il cavo, e da qui seguono due conseguenze osservabili che il README elenca senza spiegarle: il supporto e' per lingua e variante di ROM, perche' il payload contiene indirizzi assoluti, e le cartucce contraffatte fanno sparire i Pokemon, perche' hanno una ROM diversa da quella su cui il payload e' tarato.

La stessa tecnica ha un precedente pubblico e minimale che vale come materiale di studio: `PkSploit` ottiene esecuzione di codice su Gen 1 con un Arduino che si finge un Game Boy sul cavo, sfrutta i circa 192 byte utili di payload e li usa per aprire una interfaccia di lettura e scrittura sulla cartuccia, arrivando a dumpare la ROM e a leggere e scrivere la SRAM. Per l'opzione D di ADR-008 e' il riferimento piu' vicino all'obiettivo, e per il progetto in generale e' la dimostrazione che il cavo, da solo, e' un canale di accesso completo alla cartuccia.

Dal lato del giocatore, per completezza, i metodi documentati sono altri: in Gen 1 gli oggetti glitch il cui puntatore di effetto cade nei dati della squadra, cioe' 8F in Rosso e Blu inglesi e ws m in Giallo; in Oro e Argento il glitch del Salvadanaio, che finisce per eseguire dalla echo RAM; in Cristallo un nome non terminato ottenuto con il glitch dei cloni difettosi, con i nomi dei box usati come deposito del codice. Nessuno di questi serve al ponte, ma servono a capire il campo e a valutare alternative.

Il lato Gen 3 ha vincoli hardware precisi. Il cavo deve essere quello del Game Boy Color e non quello del Game Boy Advance, perche' il gioco Gen 1 o 2 parla con l'hardware seriale del Game Boy. Il programma ricevente arriva sulla console via multiboot, cioe' eseguendo in RAM un programma ricevuto dal cavo, e la documentazione autorevole di quel meccanismo e' GBATEK, che gli dedica una pagina propria insieme alle modalita' della porta seriale. La cartuccia Gen 3 va inserita al posto di quella di boot mentre il programma gira, con uno scambio a caldo che puo' resettare la console.

Su questo punto c'e' una precisazione che cambia il piano di collaudo, e corregge in parte l'avvertenza dell'handoff. Non e' vero che nulla sia emulabile: e' vero che l'interazione fra Game Boy e Game Boy Advance non lo e'. Il collegamento fra due Game Boy invece si emula bene, perche' BGB espone il cavo su una connessione TCP con un protocollo documentato a pacchetti di otto byte, ed e' esattamente su quella interfaccia che `PokemonGB_Online_Trades` implementa gli scambi. Ne segue che l'intera implementazione del protocollo Gen 1 e Gen 2, compreso il campionamento della lista di correzione e la validazione dei blocchi, si puo' sviluppare e collaudare su emulatore, e solo il passaggio finale verso la GBA richiede il ferro.

## 11. Stato delle verifiche

Nessuno dei punti aperti alla prima stesura resta aperto per pigrizia: sono stati chiusi leggendo i sorgenti. Restano aperti tre punti che richiedono materiale che non e' pubblico o che non e' ancora in mano al progetto, e sono dichiarati come tali.

| Punto | Esito |
|---|---|
| Ordine dei nibble dei DV in Gen 1 e 2 | chiuso: `CalcMonStatC` in pokecrystal, Attacco e Difesa nel primo byte, Velocita' e Speciale nel secondo, con la derivazione del DV dei punti salute scritta come commento nel sorgente |
| Somma del checksum Gen 3 | chiuso: `CalculateBoxMonChecksum` somma sei parole da 16 bit per sottostruttura in un accumulatore `u16`, non byte per byte come dice la wiki |
| Chiave di cifratura Gen 3 | chiuso: `EncryptBoxMon` mette in XOR ciascuna delle dodici parole da 32 bit con il valore di personalita' e con l'ID dell'allenatore |
| Dimensione della struttura di scambio Gen 1 | chiuso: 424 byte sul filo, 418 di dati, dalla somma di costanti in `cable_club.asm` |
| Struttura di scambio in Gen 2 | chiuso: 450 byte nativi, piu' una struttura Time Capsule da 424 byte che riusa la macro `red_party_struct`, piu' un blocco separato per la posta |
| Meccanismo della lista di correzione | chiuso: sostituzione di 0xFE con 0xFF e registrazione dell'indice, con divisione in due parti perche' l'indice 0xFD collide con il preambolo |
| Ruolo dell'ID segreto per la lucentezza | chiuso: `convertShininess` del PCCS lo usa esattamente come variabile libera, come ipotizzato |
| Metodi PCCS implementati | chiuso: i quattro nomi esistono solo nel README, il codice implementa il comportamento di ORIGINAL |
| Setup di esecuzione di codice di Poke Transporter GB | chiuso: nessun setup lato giocatore, il payload Z80 viaggia sul cavo al posto della squadra |
| Chiave di sicurezza degli oggetti in Smeraldo | chiuso: `encryptionKey` a 0xAC nel blocco 2, maschera applicata allo zaino e non al deposito PC |
| Offset del salvataggio Gen 2 per lingue diverse dall'inglese | aperto: i disassemblati pret coprono inglese e giapponese, per le altre lingue serve un dump reale |
| Dimensione esatta del blocco di posta Gen 2 | aperto: dipende da `MAIL_LINE_LENGTH`, non calcolata perche' irrilevante finche' la posta resta esclusa dal trasferimento |
| Tabella completa da indice interno Gen 1 a numero nazionale | aperto: da generare dal disassemblato, non trascrivere a mano |
| Dimensione della lista della squadra Gen 1 | chiuso scrivendo il codice: 404 byte, cioe' 0x194, e non 194 come riporta una fonte secondaria |

## 12. Cosa implica tutto questo per la scelta fra le quattro opzioni

La decisione di ADR-008 resta aperta e questo documento non la chiude, ma la informa, perche' ora si vede quanto costa ciascuna opzione in termini di codice da scrivere.

Le sezioni da 2 a 9 sono il carico di lavoro comune a tutte e quattro le opzioni: chi trasferisce un Pokemon da Gen 1 o 2 a Gen 3 deve implementare tre parser, un writer cifrato con checksum, due tabelle di caratteri, una tabella di indici di specie e un risolutore di vincoli per il valore di personalita', e questo vale identico che il codice giri su un PC in Python o su una console in C compilato con devkitARM. La sezione 10 e' il carico aggiuntivo delle sole opzioni A, C e D.

Due fatti nuovi spostano il calcolo rispetto a quello che si sapeva prima. Il primo e' che la conversione fedele delle statistiche non esiste in nessuna implementazione pubblica, perche' il PCCS pubblica quattro metodi e ne implementa uno: se l'obiettivo e' la fedelta', quel pezzo va scritto comunque, in qualunque opzione, e non e' un pezzo che si eredita. Il secondo e' che il protocollo Gen 1 e Gen 2 si collauda su BGB via TCP, quindi la parte di trasporto non e' interamente bloccata dal ferro come si credeva.

Ne segue una raccomandazione pratica, che resta una raccomandazione e non una decisione presa. Le sezioni da 2 a 9 si possono implementare e collaudare oggi, senza hardware, contro dump di salvataggio e con test unitari, e il risultato e' riutilizzabile per intero da qualunque opzione si scelga dopo. Il protocollo della sezione 10 si puo' aggiungere subito dopo, collaudato su emulatore. Cominciare da la' significa non bloccare il progetto sulla discovery hardware e non pagare due volte lo stesso lavoro.

[^1]: *DV*, Determinant Values - i valori individuali delle generazioni 1 e 2, a 4 bit per statistica.

[^2]: *SRAM*, Static Random Access Memory - la memoria della cartuccia, mantenuta da una batteria tampone, dove risiede il salvataggio.

[^3]: *IV*, Individual Values - i valori individuali dalla generazione 3 in poi, a 5 bit per statistica.

[^4]: *EV*, Effort Values - i punti di allenamento della generazione 3 in poi, che sostituiscono la Stat Experience delle generazioni 1 e 2.
