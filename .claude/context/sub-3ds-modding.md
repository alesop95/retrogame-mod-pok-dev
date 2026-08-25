---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
last-verified-commit: d08a011
stato: attivo
---

# Sottoprogetto: modding 3DS e dump delle cartucce

Lo stato canonico di questo track e' questo file, insieme alla riga che lo riguarda in `memory/index.md`. La sezione "Prossimi passi" dell'handoff resta come testimonianza del punto in cui la sessione precedente si era fermata, ma quando le due divergono vale questa scheda.

Obiettivo: portare un Old 3DS XL su custom firmware e dumpare le cartucce possedute, per giocarle dai backup e valutare un eventuale ponte verso Pokemon Home.

## Dove siamo

Lo step 02, installazione del custom firmware boot9strap piu' Luma3DS v13.4 tramite MSET9 partendo dal firmware 11.17.0-50E, e' completato e verificato. Lo step 03, il dump delle cartucce con GodMode9, e' a meta': tre titoli 3DS sono stati dumpati con successo, Omega Ruby, Y e Moon, tutti e tre soggetti alla seed encryption introdotta dopo il 2014 e quindi risolti generando `seeddb.bin` con SEEDconv. Restano cinque cartucce Nintendo DS, che non hanno cifratura e si dumpano in modo diretto.

## Prossimo passo concreto

Dumpare le cinque cartucce DS rimanenti, cioe' Diamante, Perla, Platino, Nera 2 e SoulSilver, seguendo la procedura della sezione 5.3 dell'handoff, e poi trasferire sistematicamente i file da `/gm9/out/` sulla SD verso il disco del PC.

## Decisioni aperte

La configurazione dell'emulatore Azahar sul PC e' rimandata per scelta, non bloccata: l'orientamento attuale e' portare i file fisicamente via SD invece di emulare. L'uso di PKHeX su salvataggi di terze parti resta escluso finche' non c'e' una ragione precisa, per il rischio documentato nella scheda `design-and-security.md`.

## Da verificare

La sezione 7 dell'handoff colloca l'arrivo di Rosso Fuoco e Verde Foglia su Switch a ottobre 2026, mentre fonti secondarie trovate il 2026-08-25 indicano il 27 febbraio 2026, cioe' una disponibilita' gia' avvenuta. La discrepanza non e' stata risolta su fonte primaria e l'handoff non e' stato corretto. Tocca anche il track dello scambio LDN, che su quei due giochi si basa.

## Perimetro

L'handoff dichiara alla sezione 2 e ribadisce alla 5.8 che l'assistenza tecnica non copre installazione e uso di Pokemon Bank e Transporter su questa console. Il limite vale anche per le sessioni future e non va riaperto implicitamente; la motivazione sta in `_notes/perimetro-bank-transporter.md`, fuori dal version control.

## Evidenze e materiale locale

L'handoff principale e i due documenti di step stanno in `3ds-related/handoff/`. I dump prodotti non sono e non saranno versionati: vivono sulla SD della console e sul disco del PC, per la politica dichiarata in ADR-005. Le foto delle procedure svolte stanno sotto `_notes/media/3ds-related/`, insieme allo screenshot delle impostazioni di Checkpoint: presenti sul disco, mai tracciate.
