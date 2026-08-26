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
last-verified-commit: 7696c46
stato: adozione conclusa; in corso su 3 track di 5
---

# Lavoro in corso

La fonte di verita' su cosa e' fatto resta `memory/index.md`, non le spunte di questo file. Questo progetto ha piu' track paralleli invece di una sola feature attiva, quindi il campo di stato qui sopra e' un aggregato e il dettaglio sta nella tabella: la riga "Fuoco corrente" di `memory/index.md` dice su quale track si sta lavorando adesso, mentre questa tabella dice cosa sono tutti gli altri. Il dettaglio di ciascun track vive nella sua scheda `sub-*.md`.

## Stato dei track

| Sottoprogetto | Stato | Prossima azione concreta | Bloccato da |
|---|---|---|---|
| 3ds-modding | attivo | dump delle cinque cartucce DS rimanenti: Diamante, Perla, Platino, Nera 2, SoulSilver | nulla |
| smeraldo-save-fix | attivo | confermare l'installazione dei driver CH340 e annotare la porta COM | riscontro sulla macchina, e arrivo del lettore ordinato il 18/08 |
| gen12-gen3-bridge | attivo, e' il fuoco corrente | lettore e scrittore della struttura di generazione 3, cifrata, permutata e con checksum | nulla sul lavoro comune: ADR-008 e la discovery hardware pesano solo sull'ultimo tratto |
| gba-switch-trading | in ricerca, fonti portanti lette | provare l'Archer T2U Nano che l'utente ha gia' in modalita' monitor, e leggere il codice di `frlgtrade.py` | nulla: la macchina non ha Wi-Fi integrato, e l'adattatore da provare e' deciso con la sua riserva sul driver fuori albero |
| poke-automation | studio cominciato | studiare confronto di immagini e riconoscimento ottico dei caratteri, che e' la parte trasferibile | una decisione di scopo: il perimetro del progetto di riferimento risulta compatibile con le nostre regole |

## Feature: adozione del sistema di progetto portabile

Cosa fa: porta il repository dallo stato di quattro cartelle indipendenti senza version control a un progetto unico allineato allo standard, con anatomia canonica, motore di riconciliazione e una scheda di stato per sottoprogetto.

Definition of done:

- [x] igiene dell'account verificata, auto-memory disattivata, nessun residuo
- [x] inventario e scansione dei dati personali sul working tree
- [x] bonifica pre-commit: quarantena, rinomine ASCII e ISO, deduplica, percorsi stale
- [x] `git init`, identita' locale, remoto sull'alias SSH, `.gitignore` verificato con `check-ignore`
- [x] anatomia canonica e schede verticali istanziate
- [x] primo commit e primo push, manuali (storia poi collassata, vedi ADR-014)
- [x] ancoraggio con `sync-context`, secondo commit in consegna

Domande aperte:

Il PDF che documenta il bug dell'inventario e' escluso dal version control per la politica sui media, essendo un bundle di sette foto, ma non contiene dati personali ed e' evidenza tecnica: la riga di eccezione e' gia' pronta e commentata nel `.gitignore`, basta deciderlo.

## Riconciliazione

Ultima verifica: 2026-08-26 al commit 7696c46. La corsa di `sync-context` di quella data ha trovato un drift quasi tutto contabile, perche' le schede erano state aggiornate a mano nei commit successivi senza che nessuno bumpasse il loro `last-verified-commit`, e tre difetti sostanziali: `dev-testing.md` dichiarava che non esistono test automatici mentre 63 prove passano, l'apertura di `STACK.md` negava l'esistenza del codice che la sua stessa sezione delle dipendenze descriveva, e il conteggio dei track era fermo a quattro. Il difetto strutturale che li rendeva possibili era il `covers-paths` delle schede trasversali, che non seguiva l'aggiunta di un sottoprogetto: e' stato esteso, e la procedura di aggiunta ha ora un quarto passo che lo impone.
