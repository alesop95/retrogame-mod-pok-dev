---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
  - pokemon-gen12-gen3-bridge-original-hardware/
  - gba-switch-pokemon-trading/
  - poke-automation-study/
  - recreate-pokemon-distributions-events/
  - poke-ace/
  - generation-from-switch/
  - cart-battery-restoration/
  - pokedex-home-completo/
last-verified-commit: 80fac1f
stato: adozione conclusa; dieci track, fuoco corrente sul completamento del Pokedex nel deposito
---

# Lavoro in corso

La fonte di verità su cosa è fatto resta `memory/index.md`, non le spunte di questo file. Questo progetto ha più track paralleli invece di una sola feature attiva, quindi il campo di stato qui sopra è un aggregato e il dettaglio sta nella tabella: la riga "Fuoco corrente" di `memory/index.md` dice su quale track si sta lavorando adesso, mentre questa tabella dice cosa sono tutti gli altri. Il dettaglio di ciascun track vive nella sua scheda `sub-*.md`.

## Stato dei track

| Sottoprogetto | Stato | Prossima azione concreta | Bloccato da |
|---|---|---|---|
| pokedex-completo | attivo ed è il fuoco corrente; dal 2026-09-16 il trasferimento terza-quarta generazione si sintetizza in software (203 esemplari già prodotti, `_notes/lotto-parco-amici-gen4/`), la checklist copre 685 specie su 1025, il generatore Gen3 copre 176 voci su 177 | estendere la stessa sintesi software all'uscita di prima/seconda generazione, far giudicare dall'esterno gli scambi di quarta e quinta generazione già composti, proseguire la lettura del corpus (oltre cento post residui) | nulla di tecnico; restano le decisioni già registrate su Alcremie/asse del sesso, il profilo di collezione, e le sei voci con macchina nascosta escluse dalla sintesi Parco Amici |
| distributions-events | attivo; sei lotti Gen3 prodotti (176 distribuzioni, 14 incontri, 19 scambi), più i primi scambi di quarta (16) e quinta (7) generazione, tutti in attesa di giudizio salvo i 19 già conformi | il pedigree delle voci di quarta generazione, e le sei voci con macchina nascosta escluse dalla sintesi del Parco Amici che attendono una decisione | nulla su questi passi; le 28 voci coreane attendono ADR-040 |
| gen12-gen3-bridge | attivo; le tre generazioni e lo strato del salvataggio da 128 KiB sono scritti e collaudati, 206 prove; dal 2026-09-16 il pacchetto sintetizza in software anche il passaggio Parco Amici verso la quarta generazione | il confronto del salvataggio sintetico con il contenitore che il verificatore genera; estendere la sintesi del Parco Amici all'uscita di prima/seconda generazione | nulla sul lavoro comune: ADR-008 e la discovery hardware pesano solo sull'ultimo tratto |
| smeraldo-save-fix | attivo; due giri di correzione scritti sulla cartuccia vera il 2026-09-17 e verificati con read-back a hash identico (zaino, squadra, simbolo e record della Battle Pike) | il controllo visivo in gioco del secondo giro (checklist in `STUDIO-01`, sezione 20), poi il censimento di legalità del resto del box e la squadra del Parco Lotta | nulla di tecnico; resta da produrre la squadra del Parco Lotta tutta insieme, decisione già presa ma non ancora eseguita |
| cart-battery | diagnosi conclusa e negativa su Rosso e Argento; il runbook è scritto e verificato sulle fonti | provare le eventuali altre cartucce di prima e seconda generazione, che sono le sole con una finestra ancora aperta | nulla; la saldatura si fa quando conviene, perché su quelle due non c'è più nulla da perdere |
| 3ds-modding | attivo | dump delle cinque cartucce DS rimanenti: Diamante, Perla, Platino, Nera 2, SoulSilver | nulla |
| poke-ace | attivo, tre studi scritti; il confronto fra il costruttore e il metodo ricostruito è fatto e concorda | resta una decisione dell'utente sulla produzione per vie che non siano una partita giocata, e la sua estensione | la verifica pratica è impossibile prima di ottobre 2026 |
| gba-switch-trading | in ricerca, fonti portanti lette | leggere l'identificatore USB dell'adattatore che l'utente ha già, che è una misura e non un acquisto, e leggere il codice dei due repository | nulla: il track non richiede più Linux per ADR-015 |
| generation-from-switch | il meno sviluppato dei dieci; il canale è stato letto su consegna di una schermata | riscrivere lo studio con lo stato corrente del servizio, cioè su quali titoli operi oggi e quali specie copra | materiale che l'utente può procurare, perché quella pagina non si recupera con una richiesta locale |
| poke-automation | studio cominciato | studiare confronto di immagini e riconoscimento ottico dei caratteri, che è la parte trasferibile | una decisione di scopo: il perimetro del progetto di riferimento risulta compatibile con le nostre regole |

## Feature: adozione del sistema di progetto portabile

Cosa fa: porta il repository dallo stato di quattro cartelle indipendenti senza version control a un progetto unico allineato allo standard, con anatomia canonica, motore di riconciliazione e una scheda di stato per sottoprogetto.

Definition of done:

- [x] igiene dell'account verificata, auto-memory disattivata, nessun residuo
- [x] inventario e scansione dei dati personali sul working tree
- [x] bonifica pre-commit: quarantena, rinomine ASCII e ISO, deduplica, percorsi stale
- [x] `git init`, identità locale, remoto sull'alias SSH, `.gitignore` verificato con `check-ignore`
- [x] anatomia canonica e schede verticali istanziate
- [x] primo commit e primo push, manuali (storia poi collassata, vedi ADR-014)
- [x] ancoraggio con `sync-context`, secondo commit in consegna

Domande aperte:

Il PDF che documenta il bug dell'inventario è escluso dal version control per la politica sui media, essendo un bundle di sette foto, ma non contiene dati personali ed è evidenza tecnica: la riga di eccezione è già pronta e commentata nel `.gitignore`, basta deciderlo.

## Riconciliazione

Ultima verifica: 2026-09-09 al commit ee0f52b, limitata alle schede che questa sezione nomina; le schede trasversali `STACK.md`, `design-and-security.md` e `roadmap.md` restano al 2026-08-26 e vanno rilette, perché i loro percorsi coperti hanno centoquattro file cambiati da allora. La corsa del 2026-09-09 ha riscritto la scheda del fuoco corrente, che era arrivata a ventimila byte duplicando i documenti del track, ha aggiornato quella del ponte, dove lo strato del salvataggio era dichiarato come prossimo passo ed è invece scritto e collaudato, e ha esteso il `covers-paths` di `dev-testing.md` ai due track che gli mancavano, cioè lo scambio locale e l'automazione: è di nuovo il difetto strutturale che la riga seguente descrive, ricomparso su due track invece che su uno.

Verifica precedente: 2026-08-26 al commit 7696c46. La corsa di `sync-context` di quella data ha trovato un drift quasi tutto contabile, perché le schede erano state aggiornate a mano nei commit successivi senza che nessuno bumpasse il loro `last-verified-commit`, e tre difetti sostanziali: `dev-testing.md` dichiarava che non esistono test automatici mentre 63 prove passano, l'apertura di `STACK.md` negava l'esistenza del codice che la sua stessa sezione delle dipendenze descriveva, e il conteggio dei track era fermo a quattro. Il difetto strutturale che li rendeva possibili era il `covers-paths` delle schede trasversali, che non seguiva l'aggiunta di un sottoprogetto: è stato esteso, e la procedura di aggiunta ha ora un quarto passo che lo impone.
