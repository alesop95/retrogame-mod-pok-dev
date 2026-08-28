# Prompt di ripresa - sessione del 2026-08-27 e 28

> Questo file esiste per una ragione precisa: la sessione che lo ha prodotto ha lavorato su sette repository, ha portato la tesi da due a venticinque capitoli, ha corretto tre difetti degli strumenti tipografici e ha aperto quattro pendenze. Nulla di questo è ricostruibile dai soli commit, perché i commit dicono che cosa è cambiato e non perché, né che cosa era stato deciso di non fare. Si legge dall'inizio alla fine prima di toccare qualunque cosa. Quando una voce di questo file diventa obsoleta, si aggiorna qui e non si lascia invecchiare.

## 0. Come si riprende, in ordine

Prima si legge `.claude/memory/index.md`, che è la fonte di verità sullo stato dei cinque sottoprogetti, poi `.claude/memory/pending.md`, che è il registro di tutto ciò che è in sospeso. Poi si legge questo file per intero. Poi, e solo poi, si apre la scheda del sottoprogetto su cui si lavora.

Il fuoco corrente non è un sottoprogetto ma il documento: la tesi in `tesi/`. Il prossimo task dichiarato dall'utente è la traduzione inglese, descritta nella sezione 5.

## 1. Lo stato del documento, in numeri verificati

Alla chiusura della sessione, misurato e non stimato:

```
25 capitoli in tesi/capitoli/, più frontespizio e premessa
138 pagine, 925 029 byte
0 errori di compilazione, 0 sbordi di riga, 0 riferimenti irrisolti
copertura del contenuto: 1794 righe su 1794, cioè 100,0%
bibliografia: 66 voci, tutte citate (47 fonti di dominio + 19 riferimenti teorici)
suite del ponte: 114 prove, OK
```

I comandi che riproducono queste misure, da lanciare dalla radice del repository:

```powershell
cd tesi; pdflatex -interaction=nonstopmode tesi.tex; pdflatex -interaction=nonstopmode tesi.tex; cd ..
python tools/check-thesis-coverage.py
python pokemon-gen12-gen3-bridge-original-hardware/tests/run_tests.py
python tools/test-tipografia.py
python tools/analisi-quantitativa.py
```

## 2. L'invariante che governa il documento, e che non va rotto

L'utente ha stabilito una regola che vale sopra ogni altra decisione sul documento: **ogni singola riga di ogni file `.md` del progetto deve finire nel PDF**, riorganizzata e scritta in forma accademica. Non esiste un mapping uno a uno fra un documento e un capitolo, e l'organizzazione in parti, capitoli e sezioni è libera; ciò che non è libero è la copertura.

L'invariante è meccanizzato in `tools/check-thesis-coverage.py`, che confronta le sezioni dei documenti da coprire con le dichiarazioni `% copre:` in testa a ciascun capitolo, alla granularità della sezione. La conseguenza operativa da tenere presente in ogni sessione futura è la seguente: **quando si aggiunge contenuto a un `.md`, la copertura scende sotto il 100% e va riportata a 100% aggiungendolo al documento.** Il verso corretto è sempre questo, cioè prima il `.md` e poi il capitolo: l'utente lo ha dichiarato esplicitamente dicendo che i layer degli `.md` documentano e tracciano, e che da quelli si aggiungono contenuti alla tesi.

Le esenzioni deliberate si dichiarano in `tesi/non-coperti.txt` con il motivo, e un'esenzione senza motivo viene rifiutata dallo strumento. Al momento contiene una sola voce, `docs/31-glossario.md`, che confluisce nella premessa.

## 3. Che cosa è stato fatto in questa sessione

### 3.1 La tesi, da due a venticinque capitoli

La struttura in sei parti, con l'indicazione di che cosa ciascun capitolo copre:

| Capitolo | Etichetta | Copre |
|---|---|---|
| Premessa | nessuna, non è un capitolo numerato | `docs/31-glossario.md`, `SOURCES.md#come-si-usa`, `#due-file-due-scopi` |
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
| 19 Collaudo | `cap:collaudo` | `docs/21-collaudo.md`, `docs/23-prove-eseguite.md`, DATA-FORMATS sez. 11 |
| 20 Opzioni | `cap:opzioni` | `docs/30-opzioni-implementative.md`, DATA-FORMATS sez. 12 |
| 21 Fonti | `cap:fonti` | `SOURCES.md`, `docs/24-fonti-di-community.md` |
| 22 Strumenti | `cap:strumenti` | `docs/22-strumenti.md`, DATA-FORMATS sez. 7 |
| 23 Perimetro | `cap:perimetro` | le regole normative di `.claude/rules/` |
| 24 Analisi quantitativa | `cap:analisi` | `docs/12-analisi-quantitativa.md` |

Le parti sono: I fondamenti (1-5), Le strutture dati (6-9), La trasmissione (10-13), I casi di studio (14-18), Il metodo (19-24).

### 3.2 Il capitolo di analisi quantitativa, e la nota che lo alimenta

Su richiesta dell'utente il documento ha acquisito una dimostrazione matematica dei meccanismi, con considerazioni da ingegneria delle telecomunicazioni, ogni concetto attribuito alla propria fonte canonica e la matematica spiegata in ogni passaggio. Il layer sorgente è `docs/12-analisi-quantitativa.md`, il capitolo è il 24, e i numeri li produce `tools/analisi-quantitativa.py`.

I risultati che il capitolo dimostra, e che vanno conosciuti perché tre di essi hanno cambiato conclusioni del progetto:

Il checksum additivo è **invariante per permutazione**: 719 alterazioni del blocco passano con probabilità uno, non con probabilità 2 alla meno 16. È la medesima cecità della prova di simmetria fra lettura e scrittura, e da qui segue che la terza difesa di collaudo, cioè il confronto con un'implementazione indipendente, non è ridondante.

Il deficit di entropia della chiave di cifratura è di **352 bit**, non "un fattore 12": il fattore 12 è il tasso di chiave, cioè il riuso, e sono due grandezze diverse che rispondono a domande diverse. Una versione precedente della nota le confondeva.

La tabella delle 24 permutazioni **è il codice di Lehmer**, verificato esaustivamente su tutti gli indici, con dimostrazione dell'unicità della rappresentazione in base fattoriale per conteggio.

La **fedeltà delle statistiche è impossibile per cardinalità**: 2 alla 80 configurazioni in ingresso contro 22 858 382 491 812 punti interi del politopo di arrivo, cioè 44,38 bit, con perdita di 35,62 bit imposta dalla destinazione e non dalla formula. Il conteggio del politopo è per inclusione ed esclusione e si arresta al terzo termine.

Il quantizzatore **partiziona esattamente** lo spazio: 63 504 più 2 032 fa 65 536, verificato con l'identità della somma dei numeri dispari.

Esiste un **bias del modulo** che nessuna fonte segnala: 2 alla 32 non è divisibile per 25, dunque la natura non è esattamente uniforme, con deviazione relativa di 9,3 per dieci alla meno dieci. Irrilevante in pratica, ma calcolato e non assunto.

Fra sesso e abilità **l'indipendenza non vale**, perché entrambi dipendono dal medesimo byte: vanno contati congiuntamente e non moltiplicati.

Lo **stuffing è strutturalmente inammissibile** su un canale sincrono a scambio simultaneo, perché annunciare una lunghezza variabile richiederebbe a sua volta uno scambio di lunghezza concordata e la ricorsione non termina. I 200 byte della lista sono il prezzo della sincronia.

La **terna di canali 1, 6, 11 è forzata** e non convenzionale: servono 22 MHz di distanza, i canali distano 5 MHz, e nell'intervallo utile di 60 MHz ne stanno tre.

Su un orizzonte lungo **l'errore dell'automazione è certo**: per tenere la probabilità sotto l'uno per cento su otto ore a 60 fps servirebbe una probabilità di errore per fotogramma inferiore a 5,82 per dieci alla meno nove.

### 3.3 I riferimenti teorici, e perché stanno in un elenco separato

`tools/build-source-map.py` contiene ora due elenchi. `FONTI` ha 47 voci, che sono fonti di dominio consultate, ciascuna con la dichiarazione se è stata letta. `RIFERIMENTI_TEORICI` ha 19 voci, che sono la letteratura canonica dei concetti impiegati: Shannon 1948 e 1949, Vernam 1926, Cover e Thomas, Katz e Lindell, Peterson e Brown, Lin e Costello, RFC 1071, RFC 1662, RFC 3927, Tanenbaum e Wetherall, Proakis e Salehi, Gray e Neuhoff, Feller, von Neumann 1951, Devroye, Knuth volumi 2 e 3, IEEE 802.11.

La separazione non è formale e va mantenuta. Se quelle voci stessero in `FONTI`, che per ciascuna dichiara se è stata letta, il conteggio delle fonti lette di `SOURCES.md` si gonfierebbe di 19 voci che nessuno ha aperto. In bibliografia compaiono sotto un'intestazione che dichiara la loro natura, cioè citate per attribuzione del concetto e non come fonti consultate. **I numeri di pagina non sono riportati perché non sono stati verificati in sessione**, e aggiungerne di inventati violerebbe la regola sull'onestà del contenuto.

### 3.4 Le otto fonti di dominio che mancavano

Un confronto fra le righe di `SOURCES.md` marcate come lette e la tabella `FONTI` ha rivelato che 32 fonti consultate non avevano voce propria. Di queste, la maggior parte era coperta da aggregazioni dichiarate legittime, come la voce sul dev log che dichiara di aggregare undici articoli e quella su Project Pokemon che dichiara tre discussioni. Otto erano davvero assenti e sono state aggiunte: `pokeyellow`, `pokegold`, `video-goppier`, `video-trascritti`, `gbatemp-smeraldo`, `retroreversing`, `hackaday-ponte`, `pokerom-trader`.

Fra queste, due hanno prodotto contenuto nuovo nel documento. `gbatemp-smeraldo` documenta che su cartuccia genuina il messaggio di salvataggio fallito indica una memoria che sta cedendo, e che la risposta corretta è dumpare immediatamente: è la conferma esterna più forte alla norma sul backup, e sta nel capitolo 14. `pokerom-trader` segnala l'evoluzione da scambio come regola che il progetto non ha ancora considerato, e sta nel capitolo 20.

Il metodo di confronto è riproducibile e conviene rilanciarlo quando si aggiungono fonti: si estraggono da `SOURCES.md` le righe che contengono le parole letto, clonato o trascritto, e si confrontano gli URL con quelli della tabella `FONTI`.

### 3.5 Tre difetti degli strumenti tipografici, corretti alla fonte

Il primo. `fix-missing-accents` accentava le parole dentro gli **identificatori LaTeX**, trasformando `\label{cap:integrita}` in `\label{cap:integrità}`. Il documento ha continuato a compilare per coincidenza, perché etichetta e riferimenti sono stati riscritti nella medesima passata; un solo riferimento rimasto indietro avrebbe prodotto due punti di domanda nel PDF senza segnalazione. Riparate 14 occorrenze in 11 file. La causa è chiusa: i tre strumenti mascherano ora gli argomenti di un insieme chiuso di macro prima di operare, con le funzioni `maschera_identificatori` e `ripristina_identificatori`.

Il secondo. `fix-missing-accents` accentava i tag del **front matter YAML**, trasformando `probabilita` in un tag diverso. Il danno è peggiore del primo perché non rompe niente che compili: fa sparire una relazione dall'indice e dal grafo senza che nulla lo segnali. Corretto in `segmenta_markdown` di `fix-accents` e in `converti_markdown` di `fix-missing-accents`, che ora trattano il front matter come verbatim.

Il terzo, minore. Il report di `fix-accents` stampava `-> None` per le parole convertite dalla regola dei suffissi, perché cercava la resa soltanto nelle mappe esplicite. La sostituzione era corretta, la stampa no.

Entrambi i primi due difetti hanno la medesima causa, e la formulazione va conosciuta perché si applicherà di nuovo: **dentro un file convivono due linguaggi, la prosa dove l'accento è obbligatorio e gli identificatori dove l'accento è un errore.** La regola `.claude/rules/interaction-style.md` porta ora un paragrafo che lo enuncia, propagato a tutti i progetti.

La prova è `tools/test-tipografia.py`, ed è **discriminante**, verificata in entrambi i versi: disattivando la maschera i controlli falliscono esattamente sui casi reali, riattivandola passano. I suoi dati di prova sono costruiti per concatenazione di frammenti, perché scritti per intero verrebbero corretti dagli strumenti stessi alla prima passata: è il medesimo accorgimento degli autotest interni.

### 3.6 I sette progetti di `E:\`, censiti e allineati

| Progetto | LaTeX | Che cosa è stato fatto |
|---|---|---|
| `retrogame-mod-pok-dev` | sì, 30 file | è questo progetto, riferimento della propagazione |
| `template-claude-developing` | no | strumenti aggiornati, regola aggiornata, committato e pushato |
| `harmony-book` | sì, 9 file | strumenti aggiornati, regola aggiornata, committato e pushato |
| `my-cv` | sì, `main.tex` | strumenti, regola portata da 4 a 12 righe, 86 sostituzioni in `main.tex`, tre PDF verificati |
| `prova` | sì, `docs/diploma.tex` | strumenti installati, regola allineata, 120 file corretti, compila |
| `rodrainaudio-reverse-eng` | sì, trattazione | strumenti installati, regola allineata, 112 file corretti, compila |
| `thesis` | no, `.docx` | strumenti installati, regola allineata, 42 file corretti in `.claude`, `tools`, `fonti-normative` |

Su `harmony-book` restano 26 file non conformi a `md-unwrap`, preesistenti, verificati con `git stash` in una sessione precedente e deliberatamente non toccati. Su `prova` restano 5 file `.claude/` non conformi, anch'essi preesistenti.

## 4. Le pendenze aperte, in ordine di priorità

### 4.1 La traduzione inglese della tesi

È il prossimo task dichiarato dall'utente, che lo ha chiesto due volte: la tesi va tradotta in inglese in parallelo, come viene fatto in `E:\my-cv`, e lo spagnolo per il momento è escluso.

Il meccanismo di my-cv, studiato in sessione, è il seguente: un solo `main.tex` produce tre PDF con suffisso `-it`, `-en`, `-es`; `\providecommand{\CVlanguage}{en}` fissa il default, e `scripts/build-multilang.ps1` e `.sh` iniettano `\providecommand\CVlanguage{it}` sulla riga di comando di pdflatex prima di `\input{main.tex}`; il confronto avviene per definizione, cioè `\def\CVlangIT{it}` seguito da `\ifx\CVlanguage\CVlangIT`, per aggirare un difetto documentato di `\ifdefstring`, che non è sicuro rispetto a `\edef`.

**La valutazione fatta in sessione è che quel meccanismo non si trasferisca a un documento di 138 pagine**, perché dentro un `\ifx` a livello di paragrafo il sorgente diventa illeggibile e ogni modifica va fatta due volte nel medesimo file. La forma proposta, non ancora realizzata, è una cartella di capitoli per lingua con il medesimo schema di nomi, un solo `tesi.tex` che scelga il percorso da una macro, e il controllo di copertura esteso a verificare che le due cartelle abbiano gli stessi file e le stesse dichiarazioni `% copre:`, cosicché una traduzione rimasta indietro diventi un errore invece di una scoperta tardiva.

### 4.2 Lo screenshot della copertina

Il blocco dei cinque casi di studio nel frontespizio è stato ricomposto come `minipage` di larghezza dichiarata con `\centering` interno e nessuna interruzione di riga manuale. Le coordinate estratte dal PDF prima dell'intervento dimostravano che il blocco era già centrato riga per riga, con spostamenti orizzontali variabili proprio perché il centraggio compensa larghezze diverse; il problema era la disuguaglianza delle lunghezze delle quattro righe spezzate a mano.

**Serve uno screenshot della prima pagina per la conferma visiva**, che è l'unica verifica che l'agente non può compiere da sé. La procedura è quella di `.claude/rules/manual-screenshots.md`: l'utente cattura, l'agente legge l'immagine più recente in `%USERPROFILE%\Pictures\Screenpresso` verificandone l'età.

### 4.3 `prova` non ha un remote

Il push del 2026-08-27 è fallito con `fatal: No configured push destination`. Il commit locale esiste. Va aggiunto un remote secondo la regola `.claude/rules/git-identity-and-repo.md`, cioè con l'alias SSH `github-personal`, oppure va deciso che quel progetto resti locale.

### 4.4 Il `research-vault` di `thesis`

282 file su 283 di quella cartella risultano da correggere secondo gli strumenti tipografici, e **`thesis` non è un repository git**: una passata non annullabile su 282 file di ricerca non è stata fatta deliberatamente. Prima conviene un `git init` là. Una copia di sicurezza di ciò che è stato toccato sta in `E:\thesis\_notes\backup-tipografia-2026-08-27`.

### 4.5 Le pendenze precedenti, ancora aperte

I 188 file duplicati di `.claude/templates/`, e gli 83 analoghi in harmony-book. Il file `pokèmon automation.url` che viola la convenzione di nome in ASCII puro. Gli 11 file `.txt` con spazi nel nome. Le due condizioni verificate registrate in `pending.md`, cioè il gate del server MCP code-context e il `CLAUDE.md` annidato nella cartella del ponte.

## 5. Gli errori di metodo di questa sessione, da non ripetere

Questa sezione è la più utile del file, perché ciascuno di questi errori è costato tempo e si ripresenterà.

**Gli heredoc corrompono le sequenze di escape.** Uno script Python passato a `python - <<'PY'` che contenga `\file`, `\title`, `\r\n` o `\n` arriva all'interprete con quei caratteri già interpretati, e la sostituzione produce un file rotto. È accaduto cinque volte in questa sessione. La regola è: **il codice che contiene backslash si scrive in un file con lo strumento di scrittura e poi si esegue**, non si passa per l'input standard.

**`sed` con i backslash non fa quello che sembra.** Un `sed 's/\\label{a}/\\label{b}/'` ha prodotto `\abel`, cioè una macro inesistente che arresta la compilazione. Per le sostituzioni che coinvolgono backslash si usa Python, non sed.

**Contare i backslash annidati sbaglia.** Quando si genera codice Python che genera LaTeX, i livelli di escape sono tre e il conteggio a mano è inaffidabile. La tecnica che funziona è scrivere il blocco con un segnaposto, per esempio il carattere di sezione, e sostituirlo una sola volta alla fine.

**Un controllo per sottostringa produce falsi positivi sui nomi contenuti in altri nomi.** `\section` contiene `ection`, `\subsection` contiene `section`, `\pageref` contiene `ref`. Il controllo corretto guarda il contesto, cioè che cosa precede il nome, con un lookbehind che escluda lettera e backslash.

**Un controllo di idempotenza che cerca il nome di una funzione trova la sua definizione.** Cercare `maschera_identificatori(testo)` per stabilire se l'innesto fosse già stato fatto ha dato un falso positivo, perché quella stringa compare nel blocco che definisce la funzione. Il controllo va fatto sull'innesto, non sul nome.

**Un `replace` senza contesto colpisce anche le firme delle funzioni.** Sostituire `(testo, fatte, viste)` con `(testo_lavoro, fatte, viste)` ha rinominato il parametro in otto punti, comprese le definizioni, rompendo lo strumento. Va delimitato alla funzione interessata.

**Gli strumenti correggono i propri dati di prova.** È accaduto quattro volte. I dati di prova si costruiscono per concatenazione di frammenti o da codepoint, cosicché la parola non compaia intera nel sorgente.

**Un file di prova su un volume diverso da quello del repository rompe `os.path.relpath`.** Su Windows, un percorso su `C:` non è relativizzabile rispetto a una radice su `E:`. I file temporanei degli strumenti vanno creati dentro il repository, in `_notes/tmp`, che è ignorato da git.

**Il segno meno matematico non è un trattino.** Nella prima stesura della nota quantitativa ne sono stati usati nove, cioè esattamente il carattere che la regola definisce il più insidioso in un testo tecnico. `fix-dashes` li ha corretti, ma la lezione è di scriverli giusti la prima volta.

## 6. I vincoli del progetto che non si negoziano

Sono nelle regole sotto `.claude/rules/` e valgono per ogni sessione. Qui si ripetono i tre che hanno morso in questa sessione.

**I comandi git restano manuali dell'utente.** L'agente prepara i file e consegna i comandi, non committa. Il `settings.json` lo impone anche in negazione. I comandi si consegnano in due blocchi, PowerShell e bash, con una riga per comando e nessun carattere di continuazione, perché una riga spezzata a mano diventa due comandi rotti per chi la incolla.

**Le schede di `context/` e i file di `memory/` non si aggiornano da soli.** Li aggiorna l'utente, o l'agente su richiesta esplicita.

**Ogni paragrafo di prosa in un file Markdown sta su una riga sorgente unica.** Si verifica con `python tools/md-unwrap.py --check .`

## 7. Lo stato dei cinque sottoprogetti, in una riga ciascuno

Il ponte fra generazioni è l'unico che è diventato codice: `pokebridge` copre i lettori e scrittori delle tre generazioni con 114 prove, e il debito tecnico dichiarato è l'esternalizzazione dei vettori di prova su file.

La correzione dell'inventario di Smeraldo attende l'hardware: il lettore è stato acquistato, il passo corrente è la conferma dell'installazione del driver CH340.

Il modding del 3DS ha il firmware alternativo installato e tre cartucce dumpate su otto; restano cinque titoli DS, che non richiedono decrittazione.

Lo scambio fra GBA e Switch è ricerca conclusa e codice non iniziato: il fattore che decide la praticabilità è la scheda wireless, e il criterio è il chip e il driver, non il nome commerciale.

Lo studio dell'automazione è uno studio e non una costruzione, con il perimetro da decidere prima di costruire qualunque cosa.

## 8. I file toccati in questa sessione

Nel repository corrente, oltre ai 23 capitoli nuovi e al frontespizio: `docs/12-analisi-quantitativa.md` e `docs/index.md`; `docs/22-strumenti.md` e `docs/23-prove-eseguite.md`, allineati da 63 a 114 prove; `tools/analisi-quantitativa.py`, `tools/test-tipografia.py`, `tools/prepare-cover-sprite.py`, tutti nuovi; `tools/fix-accents.py`, `tools/fix-missing-accents.py`, `tools/fix-dashes.py`, `tools/check-thesis-coverage.py`, `tools/build-bibliography.py`, `tools/build-source-map.py`, corretti; `tesi/figure/squirtle-sprite.png` con la relativa eccezione dichiarata nel `.gitignore`; `.claude/rules/interaction-style.md`.

Negli altri sei progetti: i quattro strumenti tipografici, il file delle esclusioni dei trattini, e la sezione tipografica della regola.
