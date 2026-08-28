# Prompt di ripresa - stato al 2026-08-28, seconda revisione della giornata

> Questo file esiste per una ragione precisa: la sessione che lo ha prodotto ha lavorato su sette repository, ha portato la tesi da due a venticinque capitoli, ha corretto tre difetti degli strumenti tipografici e ha aperto sei pendenze. Nulla di questo è ricostruibile dai soli commit, perché i commit dicono che cosa è cambiato e non perché, né che cosa era stato deciso di non fare. Si legge dall'inizio alla fine prima di toccare qualunque cosa, e si aggiorna a ogni passo del lavoro: una voce obsoleta qui è peggio della sua assenza, perché induce a fidarsi di uno stato che non esiste più.

## 0. Come si riprende, in ordine

Prima si legge `.claude/memory/index.md`, che è la fonte di verità sullo stato dei sei sottoprogetti, poi `.claude/memory/pending.md`, che è il registro di tutto ciò che è in sospeso. Poi si legge questo file per intero. Poi, e solo poi, si apre la scheda del sottoprogetto su cui si lavora.

Il fuoco corrente è cambiato nel corso della giornata del 2026-08-28 e va letto in `index.md`, che ora dichiara `distributions-events`: l'utente ha aperto un sesto sottoprogetto, la ricreazione delle distribuzioni di eventi, e con esso ha dichiarato per la prima volta un obiettivo che sta sopra i singoli track, cioè avere in Pokemon Home tutte le 1025 specie e le forme alternative come collezione di una vita. La sezione 3.2 di questo file racconta cosa è stato fatto e cosa resta. I due task sulla tesi restano aperti e non sono stati eseguiti: le appendici matematiche della sezione 4.1 e la versione inglese della sezione 4.2.

## 1. Le tre discipline che governano ogni sessione

Queste tre non sono preferenze e non si negoziano, perché l'utente le ha dichiarate esplicitamente e ripetutamente. Vengono prima di qualunque decisione tecnica.

### 1.1 Ogni riga di ogni `.md` finisce nel PDF

**Ogni singola riga di ogni file `.md` del progetto deve finire nel PDF**, riorganizzata e scritta in forma accademica. Non esiste un mapping uno a uno fra un documento e un capitolo, e l'organizzazione in parti, capitoli e sezioni è libera; ciò che non è libero è la copertura.

L'invariante è meccanizzato in `tools/check-thesis-coverage.py`, che confronta le sezioni dei documenti da coprire con le dichiarazioni `% copre:` in testa a ciascun capitolo, alla granularità della sezione. La conseguenza operativa è che **quando si aggiunge contenuto a un `.md` la copertura scende sotto il cento per cento e va riportata a cento aggiungendolo al documento**. Il verso corretto è sempre questo, cioè prima il `.md` e poi il capitolo, perché l'utente lo ha dichiarato dicendo che i layer degli `.md` documentano e tracciano, e che da quelli si aggiungono contenuti alla tesi.

Le esenzioni deliberate si dichiarano in `tesi/non-coperti.txt` con il motivo, e un'esenzione senza motivo viene rifiutata dallo strumento. Al momento contiene una sola voce, `docs/31-glossario.md`, che confluisce nella premessa.

### 1.2 Ogni micro passo si documenta, si spiega e si dimostra

L'utente ha chiesto che il proseguimento del progetto e il suo contenuto siano aggiornati **ogni volta e a ogni micro passo**, e che tutto sia spiegato in modo tecnico-didattico e dimostrato. Questo si traduce in tre obblighi concreti a ogni sessione.

Il primo è che una modifica al codice o a un dato va accompagnata dalla sua ragione nel documento che la ospita, non in un commento di commit. Il secondo è che una affermazione tecnica va dimostrata o marcata come da verificare, con la disciplina che il capitolo sulla conversione ha stabilito: il blocco `daverificare` in LaTeX e la citazione fra virgolette angolari nei `.md`. Il terzo è che un numero va calcolato da uno strumento riproducibile e non stimato a mente, e lo strumento va lasciato nel repository: è la ragione per cui esiste `tools/analisi-quantitativa.py`.

Questo file, `resume-prompt.md`, è parte di quell'obbligo: si aggiorna a ogni passo del lavoro e non alla fine.

### 1.3 Le lingue

**Per il momento la lingua del documento è l'italiano**, e in parallelo va generata sempre anche la versione inglese, come documento prodotto insieme all'altro e non dopo. Lo spagnolo resta escluso.

**I file `.md` restano in italiano**: sono il layer che documenta e traccia, e non vanno tradotti. La traduzione riguarda il solo documento composto, cioè i capitoli in `tesi/capitoli/` e il materiale di contorno del frontespizio e della premessa.

## 2. Lo stato del documento, in numeri verificati

Alla chiusura della sessione, misurato e non stimato:

```
26 capitoli numerati più 7 appendici, cioè 33 file in tesi/capitoli/, più frontespizio e premessa
171 pagine
0 errori di compilazione, 0 sbordi di riga, 0 riferimenti irrisolti
copertura del contenuto: 2117 righe su 2117, cioè 100,0%
bibliografia: 72 voci, tutte citate (53 fonti di dominio + 19 riferimenti teorici)
suite del ponte: 114 prove, OK
```

I numeri sono cambiati due volte il 2026-08-28. La prima con l'apertura del sesto track, che ha portato due documenti nuovi da coprire, un capitolo nuovo e sei fonti nuove. La seconda con le appendici matematiche della sezione 4.1, che hanno portato un documento nuovo e sette appendici, numerate da A a G perché `\appendix` commuta la numerazione dei capitoli in lettere. La misura è stata rifatta dopo ciascuna delle due e non stimata.

I comandi che riproducono queste misure, dalla radice del repository:

```powershell
cd tesi; pdflatex -interaction=nonstopmode tesi.tex; pdflatex -interaction=nonstopmode tesi.tex; cd ..
python tools/check-thesis-coverage.py
python pokemon-gen12-gen3-bridge-original-hardware/tests/run_tests.py
python tools/test-tipografia.py
python tools/analisi-quantitativa.py
```

La struttura in sei parti e la corrispondenza fra capitoli e documenti coperti:

| Capitolo | Etichetta | Copre |
|---|---|---|
| Premessa | non numerata | `docs/31-glossario.md`, `SOURCES.md#come-si-usa`, `#due-file-due-scopi` |
| 1 Bit e numeri | `cap:bit` | `docs/02-numeri-e-bit.md` |
| 2 Supporto e salvataggio | `cap:supporto` | `docs/01-fondamenta-salvataggio.md` |
| 3 Integrità e checksum | `cap:integrita` | `docs/03-integrita-checksum.md`, DATA-FORMATS sez. 3 e 6 |
| 4 Testo e charmap | `cap:testo` | `docs/05-testo-e-charmap.md` |
| 5 Identità del dato | `cap:identita` | `docs/06-identita-pokemon.md` |
| 6 Strutture Gen 1 | `cap:gen1` | DATA-FORMATS intestazione, sez. 1, 2, 8 |
| 7 Strutture Gen 2 | `cap:gen2` | DATA-FORMATS sez. 4 |
| 8 Cifratura Gen 3 | `cap:cifratura` | DATA-FORMATS sez. 5, `docs/04-cifratura-gen3.md` |
| 9 Conversione | `cap:conversione` | `docs/07-conversione-vincoli.md`, DATA-FORMATS sez. 9 |
| 10 Cavo Link | `cap:cavo` | `docs/08-cavo-link.md` |
| 11 Esecuzione di codice | `cap:esecuzione` | `docs/09-esecuzione-codice.md`, DATA-FORMATS sez. 10 |
| 12 Multiboot | `cap:multiboot` | `docs/10-multiboot-hardware.md` |
| 13 Wireless LDN | `cap:ldn` | `docs/11-wireless-locale-e-ponte-switch.md` |
| 14 Caso Smeraldo | `cap:smeraldo` | handoff e README di `gba-save-extraction-smeraldo/` |
| 15 Caso 3DS | `cap:3ds` | handoff e README di `3ds-related/` |
| 16 Caso LDN trading | `cap:ldn-trading` | handoff e README di `gba-switch-pokemon-trading/` |
| 17 Caso automazione | `cap:automazione` | README e STUDIO-01 di `poke-automation-study/` |
| 18 Caso ponte | `cap:ponte` | README del ponte, `docs/20-architettura-codice.md` |
| 19 Caso distribuzioni | `cap:distribuzioni` | README e STUDIO-01 di `recreate-pokemon-distributions-events/` |
| 20 Collaudo | `cap:collaudo` | `docs/21-collaudo.md`, `docs/23-prove-eseguite.md`, DATA-FORMATS sez. 11 |
| 21 Opzioni | `cap:opzioni` | `docs/30-opzioni-implementative.md`, DATA-FORMATS sez. 12 |
| 22 Fonti | `cap:fonti` | `SOURCES.md`, `docs/24-fonti-di-community.md` |
| 23 Strumenti | `cap:strumenti` | `docs/22-strumenti.md`, DATA-FORMATS sez. 7 |
| 24 Perimetro | `cap:perimetro` | le regole normative di `.claude/rules/` |
| 25 Analisi quantitativa | `cap:analisi` | `docs/12-analisi-quantitativa.md` |
| A Teoria dell'informazione | `app:informazione` | `docs/40-appendice-matematica.md`, titolo e sezione 1 |
| B Probabilità | `app:probabilita` | idem, sezione 2 |
| C Algebra e combinatoria | `app:algebra` | idem, sezione 3 |
| D Geometria discreta | `app:geometria` | idem, sezione 4 |
| E Teoria dei codici | `app:codici` | idem, sezione 5 |
| F Segnale e telecomunicazioni | `app:segnale` | idem, sezione 6 |
| G Crittografia | `app:crittografia` | idem, sezione 7 |

Le parti sono: I fondamenti (1-5), Le strutture dati (6-9), La trasmissione (10-13), I casi di studio (14-19), Il metodo (20-25), e le appendici da A a G dopo `\appendix`. I sei file della parte del metodo sono stati rinominati per far posto al capitolo 19, e le etichette non sono cambiate: un `\ref` non si è rotto perché nessun riferimento cita il numero del file.

## 3. Che cosa contiene l'analisi quantitativa, e che cosa ha corretto

Il layer sorgente è `docs/12-analisi-quantitativa.md`, il capitolo è il 24, e i numeri li produce `tools/analisi-quantitativa.py`. I risultati dimostrati, che vanno conosciuti perché quattro di essi hanno cambiato conclusioni del progetto:

Il checksum additivo è **invariante per permutazione**: settecentodiciannove alterazioni del blocco passano con probabilità uno, non con probabilità due alla meno sedici, perché la somma è commutativa. È la medesima cecità della prova di simmetria fra lettura e scrittura, e da qui segue che la terza difesa di collaudo, cioè il confronto con un'implementazione indipendente, non è ridondante.

Il deficit di entropia della chiave di cifratura è di **352 bit**, non un fattore dodici: il fattore dodici è il tasso di chiave, cioè il riuso, e sono due grandezze diverse che rispondono a domande diverse. Una versione precedente della nota le confondeva.

La tabella delle ventiquattro permutazioni **è il codice di Lehmer**, verificato esaustivamente su tutti gli indici, con dimostrazione dell'unicità della rappresentazione in base fattoriale per conteggio.

La **fedeltà delle statistiche è impossibile per cardinalità**: due alla ottanta configurazioni in ingresso contro 22 858 382 491 812 punti interi del politopo di arrivo, cioè 44,38 bit, con perdita di 35,62 bit imposta dalla destinazione e non dalla formula.

Il quantizzatore **partiziona esattamente** lo spazio: 63 504 più 2 032 fa 65 536, verificato con l'identità della somma dei numeri dispari.

Esiste un **bias del modulo** che nessuna fonte segnala: due alla trentadue non è divisibile per venticinque, dunque la natura non è esattamente uniforme, con deviazione relativa di 9,3 per dieci alla meno dieci. Irrilevante in pratica, ma calcolato e non assunto.

Fra sesso e abilità **l'indipendenza non vale**, perché entrambi dipendono dal medesimo byte: vanno contati congiuntamente e non moltiplicati.

Lo **stuffing è strutturalmente inammissibile** su un canale sincrono a scambio simultaneo, perché annunciare una lunghezza variabile richiederebbe a sua volta uno scambio di lunghezza concordata e la ricorsione non termina.

La **terna di canali 1, 6, 11 è forzata** e non convenzionale: servono ventidue megahertz di distanza, i canali distano cinque, e nell'intervallo utile di sessanta ne stanno tre.

Su un orizzonte lungo **l'errore dell'automazione è certo**: per tenere la probabilità sotto l'uno per cento su otto ore a sessanta fotogrammi al secondo servirebbe una probabilità di errore per fotogramma inferiore a 5,82 per dieci alla meno nove.

### 3.1 I riferimenti teorici, e perché stanno in un elenco separato

`tools/build-source-map.py` contiene due elenchi. `FONTI` ha quarantasette voci, che sono fonti di dominio consultate, ciascuna con la dichiarazione se è stata letta. `RIFERIMENTI_TEORICI` ha diciannove voci, che sono la letteratura canonica dei concetti impiegati: Shannon 1948 e 1949, Vernam 1926, Cover e Thomas, Katz e Lindell, Peterson e Brown, Lin e Costello, RFC 1071, RFC 1662, RFC 3927, Tanenbaum e Wetherall, Proakis e Salehi, Gray e Neuhoff, Feller, von Neumann 1951, Devroye, Knuth volumi 2 e 3, IEEE 802.11.

La separazione va mantenuta. Se quelle voci stessero in `FONTI`, che per ciascuna dichiara se è stata letta, il conteggio delle fonti lette di `SOURCES.md` si gonfierebbe di diciannove voci che nessuno ha aperto. In bibliografia compaiono sotto un'intestazione che dichiara la loro natura, cioè citate per attribuzione del concetto. **I numeri di pagina non sono riportati perché non sono stati verificati in sessione**, e aggiungerne di inventati violerebbe la regola sull'onestà del contenuto.

### 3.2 Il sesto track, l'obiettivo di collezione, e la data che li governa

Questa sottosezione è la novità della seconda metà del 2026-08-28 e va letta prima di toccare qualunque cosa, perché cambia il senso di tre track che esistevano già.

L'utente ha creato la cartella di un sesto sottoprogetto e ha indicato quattro fonti video; con il messaggio successivo ha dichiarato l'obiettivo a cui quel lavoro serve, cioè avere in Pokemon Home tutte le 1025 specie e anche le forme alternative, e portare avanti quella collezione per tutta la vita. Ha chiesto inoltre di tracciare temporaneamente nel progetto la spedizione del lettore di cartucce, perché serve agli altri task.

Che cosa è stato fatto. La cartella è stata creata con nome in ASCII puro, `recreate-pokemon-distributions-events`, perché quella dell'utente portava una lettera accentata e la convenzione del progetto lo vieta per un percorso che finisce in un `covers-paths`, in un pathspec git e in una dichiarazione di copertura; la cartella accentata era vuota ed è stata rimossa, e la scelta è registrata in ADR-017 come reversibile. Le quattro fonti sono state trascritte con `yt-dlp` più `tools/vtt-to-text.py` e lette per intero, e la conoscenza sta nello studio della cartella, che è il documento da leggere. Il track è registrato nei quattro posti che la procedura di `CLAUDE.md` prescrive, `covers-paths` delle schede trasversali compreso, e il capitolo 19 della tesi lo copre riportando la copertura a cento.

I due fatti verificati che valgono più di tutto il resto. Pokemon Bank chiude il 26 febbraio 2027 alle 12:00 JST, cioè il 25 febbraio alle 19:00 PST, verificato sulla comunicazione ufficiale del supporto Nintendo e non sulla stampa, e con esso cessa il trasferimento verso Home senza alcun periodo di tolleranza. Poke Transporter accetta come sorgente soltanto la quinta generazione e le riedizioni su Virtual Console della prima e della seconda, quindi la terza generazione non entra in Bank e un esemplare nato su cartuccia deve attraversare quattro passaggi irreversibili. Il primo di essi, il Parco Amico, richiede un Nintendo DS o DS Lite, perché il 3DS non ha lo slot per le cartucce Game Boy Advance: la domanda è stata posta e l'utente ha dichiarato il 2026-08-28 di possedere quella console, quindi il passaggio è praticabile e il requisito residuo è la corrispondenza di lingua fra i titoli ai due capi di ogni passaggio. Le cartucce DS del track 3DS coprono invece gli anelli intermedi, perché quattro sono di quarta generazione e Nera 2 è di quinta.

Le due decisioni che restano all'utente e che nessuna sessione deve prendere al suo posto. La prima è se l'obiettivo riapra il perimetro su Pokemon Bank e Pokemon Transporter, dato che l'ultimo tratto della catena passa da quei due titoli e l'assistenza su di essi è esclusa dalla regola dell'hardware per una motivazione che sta in `_notes/perimetro-bank-transporter.md`. Non esiste alternativa tecnica: quella è l'unica porta. La seconda è se le vie di iniezione che richiedono materiale di terze parti, cioè una ROM di distribuzione o un salvataggio precostituito per l'e-Reader, siano dentro il perimetro, dato che la regola esclude i salvataggi scaricati; la norma non si applica in automatico perché non si tratta del salvataggio di un gioco Pokemon, e proprio per questo va decisa. Entrambe stanno in `pending.md` e in ADR-017.

Sulla spedizione lo stato non è stato ottenuto e va detto senza attenuazioni: la pagina di parcelsapp non porta dati nel documento servito, la sua interfaccia programmatica pretende una chiave, e l'interfaccia di Australia Post, che il suffisso del codice rende probabile, risponde che il codice non è fra i suoi. Il tracciamento è registrato in una sezione temporanea di `pending.md`, da cancellare quando il lettore arriva. Le vie che restano sono l'automazione del browser dell'utente, da chiedere prima di usarla, o la consegna manuale dello stato.

Le cose non chiuse del track, tutte registrate in `pending.md`: se un verificatore di legittimità accetti una ricreazione fedele, che è il prossimo passo e non richiede hardware; se la funzione di BIOS numero 11 citata dalla fonte sia la decompressione LZ77; se la posta stia nella sezione quattro del salvataggio; se una collezione completa resti possibile dopo febbraio 2027, affermazione di fonti secondarie non verificata; e il contenuto del thread di r/PokemonHome indicato dall'utente, non leggibile dagli strumenti di sessione.

## 4. I task aperti, in ordine di priorità

### 4.1 Le appendici matematiche, eseguite il 2026-08-28

Questo task è stato eseguito e questa sottosezione resta come resoconto, perché il criterio con cui è stato riempito serve a chi lo estenderà. Il layer sorgente è `docs/40-appendice-matematica.md`, con quarantasette voci in sette aree, e le appendici composte sono i sette file `tesi/capitoli/A1-...` fino a `A7-...`, collegati dopo `\appendix` in `tesi.tex` e numerati da A a G. Ogni voce ha la forma richiesta, cioè enunciato, ragione per cui la nozione esiste, esempio svolto fino al risultato numerico e rimando al punto del lavoro che la impiega, e ciascuna appendice dichiara le sezioni che copre con gli slug calcolati dallo strumento invece che trascritti a mano. La copertura è tornata a cento e la compilazione è pulita.

Le voci sono le seguenti. Area A, teoria dell'informazione: bit come unità, entropia con le sue due proprietà, entropia condizionata, informazione mutua, disuguaglianza di elaborazione dei dati. Area B, probabilità: variabile aleatoria discreta, distribuzione uniforme con la dimostrazione del bias del modulo su numeri piccoli, indipendenza, geometrica con derivazione del valore atteso, binomiale con il conto dei fotogrammi, approssimazione di Poisson con il criterio di validità e la sua verifica, deviazione standard. Area C, algebra e combinatoria: fattoriale, permutazione, gruppo abeliano come origine dell'invarianza del checksum, anello dei resti, aritmetica modulo due, teorema cinese del resto applicato ai tre moduli del valore di personalità, coefficiente binomiale, combinazioni con ripetizione, inclusione ed esclusione, principio dei cassetti, sistema fattoriale e codice di Lehmer con la decodifica dell'indice sette svolta per intero. Area D, geometria discreta: politopo, punti interi, conteggio con vincoli superiori con la formula esplicita. Area E, teoria dei codici: codice rilevatore, sindrome, distanza di Hamming, errore a raffica, divisione polinomiale svolta a mano, controllo ciclico. Area F, segnale: quantizzatore scalare, regione di quantizzazione con la verifica della partizione, uniforme e non uniforme, saturazione, canale sincrono e asincrono, velocità di simbolo, occupazione di banda, ciclo di lavoro, trama e delimitazione, trasparenza a byte con la dimostrazione di inammissibilità. Area G, crittografia: cifrario, sicurezza perfetta con la distinzione fra deficit e tasso di chiave, cifrario di Vernam e chiave monouso, attacco a testo cifrato noto con la sovrapposizione.

Un errore di metodo è stato commesso e va registrato perché era già scritto in questo file al primo posto della sezione 7: la riga che apre le appendici è stata scritta passando uno script per l'input standard, e la sequenza di escape si è persa producendo un carattere di controllo al posto della macro. Il documento compilava con un errore e numerava le appendici come capitoli 26 a 32 invece che da A a G. La riparazione è stata fatta con uno script scritto su file, che è precisamente la regola che quella sezione prescrive.

La richiesta originale dell'utente era in questi termini: la matematica deve includere in appendice **la definizione di entropia, che cos'è un politopo, e tutte le definizioni necessarie a comprendere la matematica dei capitoli principali senza dare nulla per scontato**.

Il criterio di completezza da adottare è meccanico e va applicato così: si percorre il capitolo 24 e ogni nozione che vi compare senza essere definita nel documento diventa una voce di appendice. Dall'inventario fatto in sessione, le voci necessarie sono le seguenti.

Dalla teoria dell'informazione: entropia di una variabile discreta, entropia condizionata, informazione mutua, disuguaglianza di elaborazione dei dati, e la nozione di bit come unità di misura dell'informazione. La definizione di entropia compare già in forma compatta in apertura del capitolo 24 e in appendice va estesa con l'interpretazione, le proprietà e un esempio svolto.

Dalla probabilità: variabile aleatoria discreta, distribuzione uniforme, indipendenza, distribuzione geometrica con valore atteso e varianza, distribuzione binomiale, approssimazione di Poisson con il criterio di validità, e la nozione di deviazione standard come misura di dispersione.

Dall'algebra e dalla combinatoria: gruppo abeliano e la proprietà commutativa da cui segue l'invarianza del checksum, anello dei resti modulo n, aritmetica modulo due e lo XOR come somma in quel campo, teorema cinese del resto, coefficiente binomiale, combinazioni con ripetizione, principio di inclusione ed esclusione, principio dei cassetti, permutazione, sistema numerico fattoriale e codice di Lehmer, e la funzione fattoriale.

Dalla geometria discreta: **che cos'è un politopo**, che cosa sono i suoi punti interi, e perché contarli richiede l'inclusione ed esclusione quando ci sono vincoli superiori sulle coordinate.

Dalla teoria dei codici: codice rilevatore d'errore, sindrome, distanza di Hamming, errore a raffica, divisione polinomiale in aritmetica binaria e CRC.

Dalla teoria del segnale e delle telecomunicazioni: quantizzatore scalare, regione di quantizzazione, quantizzatore uniforme e non uniforme, saturazione, canale sincrono e asincrono, velocità di simbolo, occupazione di banda, ciclo di lavoro, trama e delimitazione di trama, trasparenza a byte.

Dalla crittografia: cifrario, sicurezza perfetta, cifrario di Vernam, chiave monouso, e il concetto di attacco a testo cifrato noto.

Il vincolo della sezione 1.1 vale anche qui: le appendici vanno prima scritte come `.md` sotto `docs/`, per esempio `docs/40-appendice-matematica.md`, e poi trasportate in appendice LaTeX con la dichiarazione `% copre:` corrispondente. In LaTeX le appendici si aprono con `\appendix` dopo l'ultimo capitolo e prima della bibliografia.

Una avvertenza di stile che vale in particolare qui. Le definizioni non vanno scritte come un glossario di voci brevi, perché il progetto ha già un glossario e la richiesta è diversa: vanno scritte in modo che chi non conosce la nozione la comprenda, cioè con l'enunciato, il motivo per cui la nozione esiste, un esempio svolto e il rimando al punto del documento in cui viene impiegata. È la differenza fra un'appendice che si consulta e una che si legge.

### 4.2 La versione inglese, generata sempre in parallelo

L'utente ha chiesto che l'inglese sia un documento **generato sempre in parallelo**, non una traduzione fatta una volta. I `.md` restano in italiano.

Il meccanismo di `E:\my-cv`, studiato in sessione, è il seguente: un solo `main.tex` produce tre PDF con suffisso di lingua; `\providecommand{\CVlanguage}{en}` fissa il default, e `scripts/build-multilang.ps1` e `.sh` iniettano la definizione sulla riga di comando di pdflatex prima di `\input{main.tex}`; il confronto avviene per definizione, cioè `\def\CVlangIT{it}` seguito da `\ifx\CVlanguage\CVlangIT`, per aggirare un difetto documentato di `\ifdefstring`, che non è sicuro rispetto a `\edef`.

**La valutazione fatta in sessione è che quel meccanismo non si trasferisca a un documento di centotrentotto pagine**, perché dentro un `\ifx` a livello di paragrafo il sorgente diventa illeggibile e ogni modifica va fatta due volte nel medesimo file. La forma proposta, non ancora realizzata, è una cartella di capitoli per lingua con il medesimo schema di nomi, per esempio `tesi/capitoli/it/` e `tesi/capitoli/en/`, un solo `tesi.tex` che scelga il percorso da una macro iniettata dalla riga di comando, e uno script di costruzione che produca i due PDF in una passata.

Il controllo va esteso in due punti, e sono la parte che rende il parallelismo verificabile invece che dichiarato. Il primo è che le due cartelle devono contenere gli stessi file con le stesse dichiarazioni `% copre:`, cosicché un capitolo tradotto in ritardo diventi un errore dello strumento e non una scoperta tardiva. Il secondo è che il controllo di copertura deve girare su entrambe le lingue, perché la copertura è una proprietà del documento e non della sua lingua.

Resta una decisione aperta, che l'utente non ha ancora preso: se la versione inglese debba tradurre anche i blocchi `daverificare` e le citazioni bibliografiche, oppure se questi ultimi restino in italiano essendo descrizioni di fonti. La proposta è tradurre tutto il testo di autore e lasciare in italiano i soli abstract delle voci bibliografiche, che sono generati dalla tabella unica e servono a chi consulta il registro.

### 4.3 Il sottotitolo del frontespizio

Il blocco dei cinque casi di studio è stato ricomposto in questa sessione come `minipage` di larghezza misurata, e la copertina è stata verificata su schermata. Il **sottotitolo sopra lo sprite** porta però ancora tre righe spezzate a mano con lunghezze disuguali, cioè il medesimo difetto appena corretto sotto. L'utente ne è stato informato e la decisione è sua.

### 4.4 `prova` non ha un remote

Il push del 2026-08-27 è fallito con `fatal: No configured push destination`. Il commit locale esiste. Va aggiunto un remote secondo la regola `.claude/rules/git-identity-and-repo.md`, cioè con l'alias SSH `github-personal`, oppure va deciso che quel progetto resti locale.

### 4.5 Il `research-vault` di `thesis`

Duecentottantadue file su duecentottantatré di quella cartella risultano da correggere secondo gli strumenti tipografici, e **`thesis` non è un repository git**: una passata non annullabile su quel materiale non è stata fatta deliberatamente. Prima conviene un `git init` là. Una copia di sicurezza di ciò che è stato toccato sta in `E:\thesis\_notes\backup-tipografia-2026-08-27`.

### 4.6 Le pendenze precedenti

I centottantotto file duplicati di `.claude/templates/`, e gli ottantatré analoghi in harmony-book. Il file `pokèmon automation.url` che viola la convenzione di nome in ASCII puro. Gli undici file `.txt` con spazi nel nome. Le due condizioni verificate registrate in `pending.md`, cioè il gate del server MCP code-context e il `CLAUDE.md` annidato nella cartella del ponte. In `harmony-book` restano ventisei file non conformi a `md-unwrap` e in `prova` cinque, tutti preesistenti e deliberatamente non toccati.

## 5. I sette progetti di `E:\`, e il loro stato

| Progetto | LaTeX | Stato |
|---|---|---|
| `retrogame-mod-pok-dev` | sì | questo progetto, riferimento della propagazione |
| `template-claude-developing` | no | strumenti e regola aggiornati, committato e pushato |
| `harmony-book` | sì | strumenti e regola aggiornati, committato e pushato |
| `my-cv` | sì | strumenti, regola, 86 sostituzioni in `main.tex`, tre PDF verificati, committato |
| `prova` | sì | strumenti, regola, 120 file corretti, compila, commit locale senza push |
| `rodrainaudio-reverse-eng` | sì | strumenti, regola, 112 file corretti, compila, committato e pushato |
| `thesis` | no | strumenti e regola, 42 file corretti; non è un repository git |

## 6. I tre difetti degli strumenti tipografici, e la loro causa comune

Il primo. `fix-missing-accents` accentava le parole dentro gli **identificatori LaTeX**, trasformando una etichetta in una etichetta diversa. Il documento ha continuato a compilare per coincidenza, perché etichetta e riferimenti sono stati riscritti nella medesima passata; un solo riferimento rimasto indietro avrebbe prodotto due punti di domanda nel PDF senza segnalazione. Riparate quattordici occorrenze in undici file.

Il secondo. Il medesimo strumento accentava i tag del **front matter YAML**, trasformando un tag in un tag diverso. Il danno è peggiore del primo perché non rompe niente che compili: fa sparire una relazione dall'indice e dal grafo senza che nulla lo segnali.

Il terzo, minore. Il report di `fix-accents` stampava un valore nullo per le parole convertite dalla regola dei suffissi, perché cercava la resa soltanto nelle mappe esplicite. La sostituzione era corretta, la stampa no.

La causa dei primi due è la medesima, e la formulazione va conosciuta perché si applicherà di nuovo: **dentro un file convivono due linguaggi, la prosa dove l'accento è obbligatorio e gli identificatori dove l'accento è un errore.** I tre strumenti mascherano ora gli argomenti di un insieme chiuso di macro e il front matter prima di operare, e la regola `.claude/rules/interaction-style.md` porta un paragrafo che lo enuncia, propagato a tutti i progetti.

La prova è `tools/test-tipografia.py`, ed è **discriminante**, verificata in entrambi i versi: disattivando il presidio i controlli falliscono esattamente sui casi reali, riattivandolo passano. I suoi dati di prova sono costruiti per concatenazione di frammenti, perché scritti per intero verrebbero corretti dagli strumenti stessi alla prima passata.

## 7. Gli errori di metodo, da non ripetere

Questa sezione è la più utile del file, perché ciascuno di questi errori è costato tempo e si ripresenterà.

**Gli heredoc corrompono le sequenze di escape.** Uno script Python passato per l'input standard che contenga sequenze come quelle di un nome di macro LaTeX o di un fine riga arriva all'interprete con quei caratteri già interpretati, e la sostituzione produce un file rotto. È accaduto cinque volte. La regola è: **il codice che contiene backslash si scrive in un file con lo strumento di scrittura e poi si esegue**, non si passa per l'input standard.

**`sed` con i backslash non fa quello che sembra.** Una sostituzione su un nome di macro ha prodotto una macro inesistente che arresta la compilazione. Per le sostituzioni che coinvolgono backslash si usa Python.

**Contare i backslash annidati sbaglia.** Quando si genera codice Python che genera LaTeX i livelli di escape sono tre e il conteggio a mano è inaffidabile. La tecnica che funziona è scrivere il blocco con un segnaposto e sostituirlo una sola volta alla fine.

**Un controllo per sottostringa produce falsi positivi sui nomi contenuti in altri nomi.** Il nome di una sezione contiene quello di una sottosezione e viceversa. Il controllo corretto guarda il contesto, con un lookbehind che escluda lettera e backslash.

**Un controllo di idempotenza che cerca il nome di una funzione trova la sua definizione.** Va fatto sull'innesto, non sul nome.

**Un `replace` senza contesto colpisce anche le firme delle funzioni.** Sostituire il nome di un parametro ha rinominato otto occorrenze comprese le definizioni, rompendo lo strumento. Va delimitato alla funzione interessata.

**Gli strumenti correggono i propri dati di prova.** È accaduto quattro volte. I dati di prova si costruiscono per concatenazione di frammenti o da codepoint.

**Un file temporaneo su un volume diverso da quello del repository rompe il calcolo del percorso relativo.** Su Windows un percorso su un volume non è relativizzabile rispetto a una radice su un altro. I file temporanei vanno creati dentro il repository, in `_notes/tmp`, che è ignorato da git.

**Il segno meno matematico non è un trattino.** Nella prima stesura della nota quantitativa ne sono stati usati nove, cioè esattamente il carattere che la regola definisce il più insidioso in un testo tecnico.

**Una schermata può mostrare un file aperto in precedenza.** Il visualizzatore di PDF tiene il file in cache, e una schermata della copertina ha mostrato la composizione del giorno prima insieme alla data vecchia. **La verifica va fatta sui byte del file e non sull'immagine**: gli operatori di testo si estraggono decomprimendo gli stream del PDF, e la data composta da `\today` è il modo più rapido di accorgersi di una cache. La schermata resta necessaria per il giudizio visivo, ma va richiesta dopo avere verificato che il file sul disco sia quello corrente.

**Il comando di rimozione ricorsiva è negato dalle regole del progetto.** La pulizia di una cartella temporanea si fa con Python.

**Passare un percorso assoluto insieme all'opzione di cartella di uscita fa fallire pdflatex** senza un messaggio utile. Si esegue con la cartella di lavoro sulla destinazione e il nome del file relativo.

## 8. I vincoli del progetto che non si negoziano

Sono nelle regole sotto `.claude/rules/`. Qui si ripetono i tre che hanno morso in questa sessione.

**I comandi git restano manuali dell'utente.** L'agente prepara i file e consegna i comandi, non committa. Il `settings.json` lo impone anche in negazione. I comandi si consegnano in due blocchi, PowerShell e bash, con una riga per comando e nessun carattere di continuazione, perché una riga spezzata a mano diventa due comandi rotti per chi la incolla.

**Le schede di `context/` e i file di `memory/` non si aggiornano da soli.** Li aggiorna l'utente, o l'agente su richiesta esplicita.

**Ogni paragrafo di prosa in un file Markdown sta su una riga sorgente unica.** Si verifica con `python tools/md-unwrap.py --check .`

## 9. Lo stato dei cinque sottoprogetti

Il ponte fra generazioni è l'unico che è diventato codice: `pokebridge` copre i lettori e scrittori delle tre generazioni con centoquattordici prove, e il debito tecnico dichiarato è l'esternalizzazione dei vettori di prova su file.

La correzione dell'inventario di Smeraldo attende l'hardware: il lettore è stato acquistato, il passo corrente è la conferma dell'installazione del driver CH340.

Il modding del 3DS ha il firmware alternativo installato e tre cartucce dumpate su otto; restano cinque titoli DS, che non richiedono decrittazione.

Lo scambio fra GBA e Switch è ricerca conclusa e codice non iniziato: il fattore che decide la praticabilità è la scheda wireless, e il criterio è il chip e il driver, non il nome commerciale.

Lo studio dell'automazione è uno studio e non una costruzione, con il perimetro da decidere prima di costruire qualunque cosa.

## 10. I file toccati nella sessione del 27 e 28 agosto

Nel repository corrente, oltre ai ventitré capitoli nuovi e al frontespizio: `docs/12-analisi-quantitativa.md` e `docs/index.md`; `docs/22-strumenti.md` e `docs/23-prove-eseguite.md`, allineati da sessantatré a centoquattordici prove; `tools/analisi-quantitativa.py`, `tools/test-tipografia.py`, `tools/prepare-cover-sprite.py`, tutti nuovi; `tools/fix-accents.py`, `tools/fix-missing-accents.py`, `tools/fix-dashes.py`, `tools/check-thesis-coverage.py`, `tools/build-bibliography.py`, `tools/build-source-map.py`, corretti; `tesi/figure/squirtle-sprite.png` con la relativa eccezione dichiarata nel `.gitignore`; `.claude/rules/interaction-style.md`; questo file.

Negli altri sei progetti: i quattro strumenti tipografici, il file delle esclusioni dei trattini, e la sezione tipografica della regola.

## 11. I file toccati nella seconda parte della sessione del 28 agosto

Nuovi: `recreate-pokemon-distributions-events/README.md` e `recreate-pokemon-distributions-events/STUDIO-01-distribuzioni-gen3-e-ricreazione.md`; `.claude/context/sub-distributions-events.md`; `tesi/capitoli/19-caso-distribuzioni.tex`; le sei note generate sotto `docs/fonti/`.

Rinominati: i sei capitoli della parte del metodo, da `19-collaudo.tex` a `24-analisi-quantitativa.tex`, ora da 20 a 25, con l'intestazione interna aggiornata.

Modificati: `tesi/tesi.tex`, `tesi/bibliografia.tex` e `docs/fonti/index-fonti.md`, questi due ultimi rigenerati; `tools/build-source-map.py` con sei fonti nuove e `tools/check-thesis-coverage.py` con due documenti nuovi; `SOURCES.md`, dove sono state aggiunte otto righe e corretta un'affermazione che diceva che nessun video era stato guardato; `.claude/memory/index.md`, `pending.md`, `decisions.md` con ADR-017 e `progress.md`; le schede `current-work.md`, `roadmap.md`, `STACK.md`, `design-and-security.md` e `dev-testing.md`, che hanno il `covers-paths` esteso e un paragrafo sul nuovo track, e in `dev-testing.md` è stato corretto il conteggio delle prove da 63 a 114, che era il numero vecchio.

Le quattro trascrizioni stanno in `_notes/fonti/` e sono sacrificabili secondo ADR-016, perché il loro contenuto è stato trasferito con la profondità che rende il file grezzo inutile: la cancellazione la fa l'utente, come la volta precedente.

Nella terza parte della sessione, quella delle appendici: nuovi `docs/40-appendice-matematica.md` e i sette file `tesi/capitoli/A1-appendice-informazione.tex` fino ad `A7-appendice-crittografia.tex`; modificati `tesi/tesi.tex` con il blocco `\appendix`, `docs/index.md` con la riga della nota nuova, e questo file.

Una pendenza nuova è stata registrata e non risolta: `tesi/README.md` è gravemente disallineato, perché descrive la tesi come se fosse in fase di pianificazione e dichiara una copertura del dieci per cento su ventinove documenti, con le tabelle dei capitoli tutte marcate da scrivere. È un file tracciato e fuorviante, e non entra nel controllo di copertura perché non è fra i documenti da coprire, quindi nessuno strumento lo segnala. La riscrittura è un lavoro a sé e va decisa.
