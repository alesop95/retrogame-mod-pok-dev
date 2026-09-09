# Mappa dei documenti del progetto

> Documento autorato del 2026-09-08. Nasce da una constatazione dell'utente, cioè che i file di testo sono diventati troppi per orientarsi. Non aggiunge contenuto: dice che cosa è ciascun file, chi lo scrive, e se qualcuno lo debba ancora aprire. È l'unico documento del progetto il cui scopo sia parlare degli altri documenti.

## Il criterio che governa tutto, e che spiega la maggior parte della confusione

I trecentoquarantacinque file Markdown tracciati non sono trecentoquarantacinque cose da leggere, e la ragione è che appartengono a cinque categorie che si comportano in modo opposto. Confonderle è ciò che rende il progetto illeggibile, perché induce ad aprire un file di novecentomila byte credendo che qualcuno lo abbia scritto.

I file **generati** si rigenerano con un comando e non si modificano mai a mano: contengono un elenco, e il loro valore è di essere completi e coerenti con la fonte, non di essere letti dall'inizio alla fine. Sono i più grossi del progetto e sono la ragione per cui la cartella sembra ingestibile. Ciascuno dichiara nella propria seconda riga da quale strumento nasce.

I file **autorati** sono scritti da qualcuno, si leggono e si citano. Sono molto più piccoli e molto meno numerosi.

I file **normativi** vincolano il comportamento e vanno letti prima di agire nell'area che governano.

I file **di stato** dicono a che punto è il progetto e si leggono a inizio sessione.

I file **del template** stanno sotto `.claude/templates/` e non sono contenuto di questo progetto: sono il pacchetto di sistema da cui il progetto è istanziato. Sono centotrentaquattro, cioè quasi il quaranta per cento del totale, e nessuno di essi va aperto lavorando ai Pokémon.

## Da dove si comincia, se si è persi

Tre file, in quest'ordine, e nient'altro.

`.claude/memory/index.md` dice qual è il fuoco corrente e a che punto è ogni sottoprogetto. `.claude/memory/pending.md` dice tutto ciò che è in sospeso. La scheda `.claude/context/sub-<slug>.md` del solo sottoprogetto su cui si lavora dice stato e prossimo passo in meno di trenta righe.

Tutto il resto si apre quando serve, e questa mappa dice quando serve.

## Lo stato, quattro file che si leggono a inizio sessione

| File | Che cos'è | Quando si apre |
|---|---|---|
| `.claude/memory/index.md` | snapshot, fuoco corrente, stato di verifica delle schede | sempre, per primo |
| `.claude/memory/pending.md` | tutto ciò che è in sospeso, modificabile | sempre, subito dopo |
| `.claude/memory/progress.md` | registro di lavoro, append-only, cronologico inverso | quando serve sapere perché una cosa è come è; si legge dalla cima e mai per intero |
| `.claude/memory/decisions.md` | le decisioni in forma ADR, append-only | quando una decisione va richiamata o contestata |

I due append-only sono grossi per costruzione e continueranno a crescere: non è un difetto da correggere, ed è la ragione per cui non si leggono mai per intero.

## Le regole, che vincolano e non informano

Stanno tutte in `.claude/rules/` e si leggono prima di agire nell'area che governano, non a inizio sessione. Sono otto: la disciplina dell'hardware e il perimetro, che è la sola specifica di questo progetto ed è normativa su ogni operazione fisica; lo stile di interazione e di documentazione; le fonti web non recuperabili; il formato dei comandi git; l'identità git e il bootstrap del repository; gli screenshot per i passi manuali; la sicurezza e i permessi; l'economia dei token.

`CLAUDE.md` alla radice le indicizza e descrive il progetto; `CLAUDE.local.md` non è tracciato.

## Le schede di contesto

Sedici file sotto `.claude/context/`, di cui sei trasversali e dieci verticali, una per sottoprogetto. Una scheda verticale sta sotto le trenta righe e contiene stato, prossimo passo e decisioni aperte: è il terzo file da aprire e quasi sempre l'ultimo che serve.

Va detto che una di esse non lo rispetta più: `sub-pokedex-home-completo.md` è arrivata a diciottomila byte, cioè sei volte il previsto, perché quel track è cresciuto molto in una settimana. Va potata riportando la conoscenza nei documenti del track e lasciando nella scheda il solo stato.

## Il percorso di studio, ventuno file sotto `docs/`

Sono conoscenza tecnica autorata, numerati per ordine di lettura e non per importanza: dalle fondamenta del salvataggio fino alle opzioni implementative, più il glossario e l'appendice matematica. Non sono stato e non si rileggono a ogni sessione. `docs/index.md` è il loro indice.

Due sono molto più grossi degli altri e vale sapere perché prima di aprirli: `docs/22-strumenti.md` è il catalogo di tutti gli strumenti con le loro procedure, e `docs/40-appendice-matematica.md` raccoglie le dispense che finiscono in appendice alla tesi. Si consultano per punti, non si leggono in sequenza.

Sotto `docs/fonti/` stanno centotré note, di cui la stragrande maggioranza generata: `index-fonti.md` è la mappa relazionale curata a mano, e `collezione/` sono le quarantatre note del corpus della collezione, generate da `tools/censimento-fonti-reddit.py`. Aprendo la radice come vault Obsidian diventano un grafo.

## I file generati, che nessuno scrive

Sono i più grossi del progetto e la causa principale del senso di ingestibilità. Ciascuno dichiara il proprio strumento nella seconda riga, e la regola è sempre la stessa: si rigenerano, non si modificano.

| File | Byte | Strumento che lo genera |
|---|---|---|
| `pokedex-home-completo/CHECKLIST-COMPLETA.md` | 968k | `tools/checklist-pokedex.py` |
| `recreate-pokemon-distributions-events/SCHEDE-ESEMPLARI-GEN4.md` | 849k | `tools/schede-esemplari-gen4.py` |
| `pokedex-home-completo/SCHEDE-EVENTI-GB.md` | 433k | `tools/genera-evento-gb.py` |
| `recreate-pokemon-distributions-events/SCHEDE-ESEMPLARI.md` | 340k | `tools/schede-esemplari.py` |
| `pokedex-home-completo/CENSIMENTO-EVENTI-FUORI-DONI.md` | 294k | `tools/censimento-eventi-tabelle.py` |
| `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` | 219k | `tools/censimento-fonti-reddit.py` |
| `recreate-pokemon-distributions-events/CATALOGO-EVENTI.md` | 58k | `tools/catalogo-eventi.py` |
| `pokedex-home-completo/CODA-PRIMO-TEMPO.md` | 42k | `tools/checklist-pokedex.py --coda` |
| `pokedex-home-completo/CONFRONTO-FOGLIO-LIVINGDEX.md` | 33k | `tools/confronta-foglio-livingdex.py` |
| `recreate-pokemon-distributions-events/EVENTI-GEN3.md` | 23k | `tools/genera-evento-gen3.py` |
| `pokedex-home-completo/FIOCCHI.md` | 16k | `tools/fiocchi.py` |
| `pokedex-home-completo/DIFFERENZE-DI-SESSO.md` | 12k | `tools/enumera-differenze-sesso.py` |
| `pokedex-home-completo/EVENTI-SENZA-CARTA.md` | 15k | `tools/leggi-serebii-eventi.py --senza-carta` |
| `pokedex-home-completo/MOSSE-PERDUTE.md` | 8k | `tools/mosse-perdute.py` |
| `pokedex-home-completo/INDICE-FOGLI-ESTERNI.md` | 8k | `tools/leggi-foglio-google.py` |
| `pokedex-home-completo/OTTENIBILITA-TITOLI.md` | 7k | `tools/ottenibilita-titoli.py` |
| `recreate-pokemon-distributions-events/CONTEGGIO-DONI-MODERNI.md` | 5k | `tools/conteggio-doni-moderni.py` |
| `pokedex-home-completo/CENSIMENTO-SALVATAGGI.md` | 5k | `tools/verifica-salvataggi.py --censimento` |

Sommano oltre tre megabyte, cioè la quasi totalità del peso testuale del progetto, e nessuno di essi va letto in sequenza.

## Il registro delle fonti

`SOURCES.md` è uno solo, alla radice, e vale la pena dire che cosa è diventato: milleottocento righe di tabella, di cui milleduecentonovantanove dal corpus della collezione. La sua struttura è descritta dentro di esso, nella sezione apposita, e non si riassume qui per non avere due descrizioni della stessa cosa.

## Gli studi e le referenze autorate, che sono i file da leggere

Sono i documenti dove sta il ragionamento, e sono pochi. Per il track del deposito: la catena di trasferimento, la roadmap cronologica, e sei studi numerati. Per le distribuzioni: quattro studi. Per l'esecuzione di codice: tre studi. Per il ponte fra generazioni: la referenza dei formati, che è il documento tecnico più denso del progetto. Più uno studio a testa per la batteria, per la generazione da console corrente e per l'automazione.

Ciascun sottoprogetto ha un `README.md` che elenca i propri file: è quello il posto dove cercare dentro un track, non questa mappa.

## Gli handoff, che sono storia e non stato

Quattro file sotto `3ds-related/handoff/` e `gba-save-extraction-smeraldo/handoff/`, più quello del track dello scambio locale. Contengono procedure e troubleshooting, non stato, e si aprono soltanto quando serve la procedura. Il track del ponte non ne ha più uno perché la sua conoscenza è stata assorbita nella referenza dei formati, come registrato in ADR-013.

## I candidati alla rimozione, con il loro perché

Nessuno di questi è stato cancellato: la decisione è dell'utente e questa sezione esiste per prenderla con i fatti davanti. Tutti restano comunque nella storia del repository.

**`resume-prompt.md`**, cinquantunmila byte alla radice. È il prompt di ripresa scritto il 2026-08-31 per una sessione che aveva lavorato su sette repository. Dichiara nella propria intestazione che una voce obsoleta lì dentro è peggio della sua assenza, perché induce a fidarsi di uno stato che non esiste più: è esattamente la sua condizione oggi, perché è fermo a otto giorni e a più di venti voci di lavoro fa. La funzione che svolgeva è la stessa di `index.md` e `pending.md`, che sono aggiornati. Va cancellato, e la sua storia resta nei commit.

**`.claude/context/deployment.md`**, milleduecento byte. Dichiara di non essere applicabile allo stato attuale e ha il campo dei percorsi coperti vuoto. È parte del pacchetto di schede del template e la sua assenza cambierebbe il conto delle schede: va tenuto, ma sapendo che è un segnaposto e non un documento.

**Le note generate sotto `docs/fonti/`** non vanno cancellate una a una ma rigenerate: se una di esse non corrisponde più alla tabella che la produce, il rimedio è rilanciare lo strumento.

## Che cosa manca a questa mappa, dichiarato

Non copre `.claude/templates/`, che è il pacchetto di sistema e ha un proprio indice in `.claude/templates/PACKAGES.md`. Non copre i file non tracciati sotto `_notes/`, che sono materiale grezzo e locale per costruzione. E non è generata: va aggiornata a mano quando un documento nasce o muore, il che la espone allo stesso invecchiamento che essa imputa al prompt di ripresa. Se un giorno i documenti crescono ancora, la si genera da uno strumento che legga le intestazioni.
