---
generated-from-commit: e692a02b8a46ab119e0389449d61327384841236
generated-from-branch: main
generated-date: 2026-09-02
covers-paths:
  - pokedex-home-completo/
last-verified-commit: 6b2dc05
stato: attivo ed è il fuoco corrente; due linee parallele dal 2026-09-10, cioè lettura del corpus e produzione dei lotti; sei assi più le due classi nuove, criterio di produzione in ADR-049 come modificato da ADR-050 e ADR-051, coda ordinata per scadenza per ADR-052
---

# Sottoprogetto: Pokedex completo in Pokemon Home

Lo stato canonico di questo track è questo file insieme alla riga che lo riguarda in `memory/index.md`, che porta il racconto per aggiunte datate. Questa scheda è stata potata il 2026-09-09: il racconto che occupava ventimila byte viveva qui e nei documenti del track insieme, e la duplicazione è precisamente ciò che una scheda di stato non deve essere. Ciò che è stato tolto non è andato perduto, perché sta nei documenti elencati sotto e nel work log.

Obiettivo: la collezione completa nel deposito, cioè una voce per ogni specie, per ogni forma che il deposito conti a parte e per ogni esemplare la cui provenienza sia essa stessa un collezionabile. È l'obiettivo dichiarato del progetto, e gli altri track vi concorrono restando autonomi. La scadenza è il 26 febbraio 2027 alle 12:00 del fuso giapponese.

## Dove siamo, in cinque righe

Il risultato che governa la pianificazione regge ed è misurato e non assunto: nessuna specie e nessuna voce di forma dipendono dalla via indiretta, quindi la chiusura non vincola il completamento del catalogo. Ciò che scade sono gli esemplari la cui identità richiede una provenienza anteriore all'ottava generazione.

Gli assi sono sei più due. Specie, forme, esemplari da distribuzione, mosse che nessun titolo moderno insegna più, fiocchi conferiti da vie chiuse, sfide interne al deposito; e dal 2026-09-09 gli scambi in gioco e gli incontri che una condizione sblocca, enumerati sulla fonte di primo livello.

Il collo di bottiglia non è più la produzione ma il trasferimento: cinque lotti sono prodotti e giudicati, la catena ha i suoi vincoli misurati anello per anello, e la regola di ammissione del deposito è nota e non aggirabile.

## Prossimo passo

Due linee in parallelo, per direttiva dell'utente del 2026-09-10: la sola lettura consumerebbe il tempo che serve alla produzione, e 2686 voci non si compongono in una settimana. La prima linea è la lettura del corpus, a undici cluster su quarantadue, e il prossimo lotto è la coda delle liste di completamento per generazione, cioè dalla quinta alla nona più gli spinoff; i quaranta documenti sulla caccia ai cromatici restano per ultimi perché servono soltanto se il profilo scelto comprende i cromatici. La seconda linea è la produzione nell'ordine per scadenza di ADR-052, cioè il lavoro che ADR-051 apre: estendere il generatore agli scambi in gioco, agli incontri condizionati e agli statici ordinari, aggiungere all'asse degli eventi il Mew ufficiale con allenatore GF e identificativo 22796, e rigenerare la lista di spunta con Alcremie a sessantatre, le centodue specie del sesso e le due classi nuove.

Sulla produzione pesa una domanda aperta dal 2026-09-10 e da risolvere prima di comporre ciò che si potrebbe ricevere: il servizio ricostruito distribuisce ancora i doni di quarta e quinta generazione alle cartucce vere, e un esemplare ricevuto è preferibile a uno composto su ogni dimensione. La voce sta in `pending.md` fra i punti tecnici aperti.

## Decisioni aperte

Restano dell'utente l'ambito delle sfide del deposito, per cui servono le schermate delle due schede non fotografate, e la scelta del profilo di collezione fra i quindici che lo strumento della comunità distingue. Le altre sono state prese e stanno in `decisions.md` da ADR-049 a ADR-054.

## Dove sta la conoscenza di questo track

```
README.md                     l'instradamento, con l'elenco di ogni file della cartella
ROADMAP.md                    la sequenza, con dipendenze e chi esegue ciascun passo
CATENA-DI-TRASFERIMENTO.md    i vincoli di ogni anello, la via in emulazione, la regola del deposito
LETTURA-DEL-CORPUS.md         il registro della lettura integrale, cluster per cluster
CONFRONTO-LIVINGDEX-POKEPC.md la terza enumerazione indipendente, e il confronto con la nostra
STUDIO-01 .. STUDIO-09        le nove note di studio, dalla scadenza alla regola del tracciatore
CHECKLIST-COMPLETA.md         la lista di spunta generata, con il codice interno PKD-####-##
```

I censimenti generati e i loro strumenti sono elencati in `MAPPA-DOCUMENTI.md` alla radice, che dice per ciascuno chi lo genera; la tesi li rende nei capitoli da 28 a 31.

## Evidenze e materiale locale

La consegna che ha aperto il track e la ricerca dell'utente stanno in `_notes/fonti/`, e quella conservata verbatim con la sua provenienza è tracciata come `RICERCA-UTENTE-2026-09-01.md`. La raccolta di trenta salvataggi esterni vive in `_notes/salvataggi/` con la lista delle provenienze scritta dall'utente, e non entra in git per due vincoli indipendenti: ne entra soltanto il censimento generato. Le fotografie delle sfide e le cartelle di calcolo della comunità stanno in `_notes/spreadsheets e passaggi home/`.
