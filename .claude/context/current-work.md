---
generated-from-commit: 8cc1798
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
last-verified-commit: 90adea9
stato: adozione conclusa; dieci track, fuoco corrente sul completamento del Pokedex nel deposito
---

# Lavoro in corso

La fonte di verità su cosa è fatto resta `memory/index.md`, non le spunte di questo file. Questo progetto ha più track paralleli invece di una sola feature attiva, quindi il campo di stato qui sopra è un aggregato e il dettaglio sta nella tabella: la riga "Fuoco corrente" di `memory/index.md` dice su quale track si sta lavorando adesso, mentre questa tabella dice cosa sono tutti gli altri. Il dettaglio di ciascun track vive nella sua scheda `sub-*.md`.

## Stato dei track

| Sottoprogetto | Stato | Prossima azione concreta | Bloccato da |
|---|---|---|---|
| pokedex-completo | attivo ed è il fuoco corrente; al 2026-09-29 la terza generazione è chiusa (Smeraldo e Rubino scritti, ADR-082, ADR-088), la libreria PKHeX.Core produce e giudica i lotti (ADR-081), 2010 conformi su 2010; la coda del primo tempo conta 333 voci prodotte, 60 producibili e 40 da periferiche su 433; la checklist copre 685 specie su 1025 | produrre le 40 voci da periferiche (29 Pokewalker, 8 Ranch, 3 Dream Radar), voce SECONDO di `pending.md`, dopo il debito tipografico della voce PRIMO; poi le fonti del Ranch e del Dream Radar, voce TERZO | nulla di tecnico; restano le decisioni registrate su Alcremie e sull'asse del sesso, il profilo di collezione, e le sei voci con macchina nascosta |
| distributions-events | attivo; i lotti di tutte le generazioni prodotte sono conformi al giudizio della libreria (2010 su 2010, 2026-09-25), il Parco Amici di quarta è rigenerato con la libreria (203 su 203, ADR-082), i 23 scambi di quarta e quinta sono ricostruiti e conformi, i doni di sesta e settima del primo tempo sono 84 su 84 | la produzione residua si governa dalla coda del track del Pokedex | le 28 voci coreane attendono ADR-040, che il giudizio con salvataggio vuoto non chiude |
| gen12-gen3-bridge | attivo; le tre generazioni e lo strato del salvataggio da 128 KiB sono scritti e collaudati, 206 prove verdi il 2026-09-29; il modulo `parco_amici.py` non produce più lotti dal 2026-09-24 (ADR-082) e resta come descrizione della trasformazione | il confronto del salvataggio sintetico con il contenitore che il verificatore genera; decidere se correggere `parco_amici.py` o dichiararlo superato | nulla sul lavoro comune: ADR-008 e la discovery hardware pesano solo sull'ultimo tratto |
| smeraldo-save-fix | concluso sul piano delle scritture: Smeraldo porta dal 2026-09-23 la collezione completa di terza generazione (giro12, 423 legali su 423) e il Rubino dal 2026-09-28 il complemento di 376 esemplari (ADR-088); il Parco Lotta ha guida, squadre e fonti verificate sul sorgente | studiare sul sorgente i contrassegni del Pokédex e sanare le cartucce, che non registrano gli esemplari scritti nel deposito (ADR-089, da ricordare sempre); alla prossima scrittura togliere la Roccia di Re doppia dalla tasca Oggetti | nulla di tecnico; l'orologio è rimandato per la pila esaurita, la Grotta Mutevole è rimandata al track del Pokedex, lo sblocco del Pokédex nazionale sul Rubino è una scelta del proprietario |
| cart-battery | diagnosi conclusa e negativa su Rosso e Argento; il runbook è scritto e verificato sulle fonti | provare le eventuali altre cartucce di prima e seconda generazione, che sono le sole con una finestra ancora aperta | nulla; la saldatura si fa quando conviene, perché su quelle due non c'è più nulla da perdere |
| 3ds-modding | attivo; la copia della SD del 2026-09-03 è in `J:\3DS - 03092026\`, con il salvataggio di Y del 2026-08-23 che serve al Vivillon | dump delle cinque cartucce DS rimanenti: Diamante, Perla, Platino, Nera 2, SoulSilver | nulla |
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

Ultima verifica: 2026-09-29 al commit `90adea9`, con `sync-context` in cinque blocchi su tutte le diciassette schede, confermati uno per volta dal proprietario. Il racconto sta nel work log, dalla terza alla nona parte del 2026-09-29. Le righe della tabella sopra riscritte in quella corsa sono cinque, cioè Pokedex, distribuzioni, ponte, Smeraldo e 3DS, e il loro testo precedente resta nella storia git. La corsa ha trovato il medesimo difetto strutturale delle due precedenti in una forma nuova: `STACK.md` e `dev-testing.md` descrivevano `tools/` senza dichiararlo fra i percorsi coperti, e da oggi lo dichiarano insieme a `scripts/`. Ne ha trovato anche un secondo, che il confronto per cartelle non può vedere: una decisione registrata fuori dall'area di una scheda, come ADR-082 per il ponte, la rende falsa senza che nessun file coperto cambi.

Ultima verifica: 2026-09-09 al commit 7bfd11b, limitata alle schede che questa sezione nomina; le schede trasversali `STACK.md`, `design-and-security.md` e `roadmap.md` restano al 2026-08-26 e vanno rilette, perché i loro percorsi coperti hanno centoquattro file cambiati da allora. La corsa del 2026-09-09 ha riscritto la scheda del fuoco corrente, che era arrivata a ventimila byte duplicando i documenti del track, ha aggiornato quella del ponte, dove lo strato del salvataggio era dichiarato come prossimo passo ed è invece scritto e collaudato, e ha esteso il `covers-paths` di `dev-testing.md` ai due track che gli mancavano, cioè lo scambio locale e l'automazione: è di nuovo il difetto strutturale che la riga seguente descrive, ricomparso su due track invece che su uno.

Verifica precedente: 2026-08-26 al commit 7c36ad4. La corsa di `sync-context` di quella data ha trovato un drift quasi tutto contabile, perché le schede erano state aggiornate a mano nei commit successivi senza che nessuno bumpasse il loro `last-verified-commit`, e tre difetti sostanziali: `dev-testing.md` dichiarava che non esistono test automatici mentre 63 prove passano, l'apertura di `STACK.md` negava l'esistenza del codice che la sua stessa sezione delle dipendenze descriveva, e il conteggio dei track era fermo a quattro. Il difetto strutturale che li rendeva possibili era il `covers-paths` delle schede trasversali, che non seguiva l'aggiunta di un sottoprogetto: è stato esteso, e la procedura di aggiunta ha ora un quarto passo che lo impone.
