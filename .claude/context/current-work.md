---
generated-from-commit: d1e1a3a
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
last-verified-commit: effc2e0
stato: adozione conclusa; in corso su 2 track di 4
---

# Lavoro in corso

La fonte di verita' su cosa e' fatto resta `memory/index.md`, non le spunte di questo file. Questo progetto ha piu' track paralleli invece di una sola feature attiva, quindi il campo di stato qui sopra e' un aggregato e il dettaglio sta nella tabella: la riga "Fuoco corrente" di `memory/index.md` dice su quale track si sta lavorando adesso, mentre questa tabella dice cosa sono tutti gli altri. Il dettaglio di ciascun track vive nella sua scheda `sub-*.md`.

## Stato dei track

| Sottoprogetto | Stato | Prossima azione concreta | Bloccato da |
|---|---|---|---|
| 3ds-modding | attivo | dump delle cinque cartucce DS rimanenti: Diamante, Perla, Platino, Nera 2, SoulSilver | nulla |
| smeraldo-save-fix | attivo | confermare l'installazione dei driver CH340 e annotare la porta COM | riscontro sulla macchina, e arrivo del lettore ordinato il 18/08 |
| gen12-gen3-bridge | in attesa di decisione | discovery hardware, poi scelta fra le opzioni A, B, C e D | una decisione, registrata come ADR-008 |
| gba-switch-trading | in ricerca | leggere il codice dei due repository di riferimento | verificare la scheda Wi-Fi disponibile |

## Feature: adozione del sistema di progetto portabile

Cosa fa: porta il repository dallo stato di quattro cartelle indipendenti senza version control a un progetto unico allineato allo standard, con anatomia canonica, motore di riconciliazione e una scheda di stato per sottoprogetto.

Definition of done:

- [x] igiene dell'account verificata, auto-memory disattivata, nessun residuo
- [x] inventario e scansione dei dati personali sul working tree
- [x] bonifica pre-commit: quarantena, rinomine ASCII e ISO, deduplica, percorsi stale
- [x] `git init`, identita' locale, remoto sull'alias SSH, `.gitignore` verificato con `check-ignore`
- [x] anatomia canonica e schede verticali istanziate
- [x] primo commit e primo push, manuali (d1e1a3a)
- [x] ancoraggio con `sync-context`, secondo commit in consegna

Domande aperte:

Il PDF che documenta il bug dell'inventario e' escluso dal version control per la politica sui media, essendo un bundle di sette foto, ma non contiene dati personali ed e' evidenza tecnica: la riga di eccezione e' gia' pronta e commentata nel `.gitignore`, basta deciderlo.

## Riconciliazione

Ultima verifica: 2026-08-24 al commit d1e1a3a, sync report senza drift.
