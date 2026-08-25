# Snapshot di sincronizzazione

Da leggere per primo a inizio sessione. Fotografa lo stato del progetto al commit di riferimento e mappa ogni scheda al suo stato di verifica. E' la fonte di verita' su cosa e' fatto, non le spunte del diario.

Questo progetto ha piu' sottoprogetti paralleli, quindi il punto di ripresa e' un blocco di righe invece che una sola. La riga "Fuoco corrente" e' la fonte di verita' unica su quale track e' attivo adesso: task paralleli non significa nessun default, significa un default dichiarato piu' N tracce leggibili.

## Stato

```
Branch attivo:         main
Commit di riferimento: d08a011
Data snapshot:         2026-08-25
```

## Stato di verifica delle schede

| Scheda | Sottoprogetto | last-verified | Stato |
|---|---|---|---|
| STACK.md | trasversale | d08a011 | aggiornata |
| design-and-security.md | trasversale | d08a011 | aggiornata |
| deployment.md | trasversale | d08a011 | non applicabile |
| dev-testing.md | trasversale | d08a011 | aggiornata |
| current-work.md | trasversale | d08a011 | aggiornata |
| roadmap.md | trasversale | d08a011 | aggiornata |
| sub-3ds-modding.md | 3ds-related | d08a011 | aggiornata |
| sub-smeraldo-save-fix.md | gba-save-extraction-smeraldo | d08a011 | aggiornata |
| sub-gen12-gen3-bridge.md | pokemon-gen12-gen3-bridge | d08a011 | aggiornata |
| sub-gba-switch-trading.md | gba-switch-pokemon-trading | d08a011 | aggiornata |

## Punto di ripresa

```
Fuoco corrente: gen12-gen3-bridge, formato dati verificato, si passa ai parser
```

Adozione del sistema: conclusa. La storia git e' stata collassata in un unico commit radice il 2026-08-25 per la bonifica di ADR-014, quindi tutte le schede sono ri-ancorate a `d08a011` e gli hash citati nelle voci di diario precedenti a quella data non risolvono piu'. Convenzione Markdown conforme su tutto il repository, nulla da fare su questo fronte.

3ds-modding: dumpare le cinque cartucce DS rimanenti, Diamante, Perla, Platino, Nera 2 e SoulSilver, poi trasferire i file da `/gm9/out/` al PC. Nessun blocco.

smeraldo-save-fix: confermare che i driver CH340 siano installati e annotare la porta COM assegnata. Bloccato sul riscontro alla macchina e sull'arrivo del lettore ordinato il 18 agosto 2026. Quando il dump arrivera' c'e' gia' lo strumento che lo legge, `tools/emerald_bag_decode.py`, e c'e' una scoperta che cambia l'ipotesi di partenza: le quantita' dello zaino sono mascherate in XOR e vanno smascherate prima di chiamarle corrotte.

gen12-gen3-bridge: scrivere i tre lettori e scrittori delle strutture Pokemon, collaudati con la prova di simmetria su dati sintetici. Il formato dati e' documentato byte per byte e verificato sul disassemblato, con undici punti dubbi chiusi e due affermazioni dell'handoff corrette; l'handoff e' stato ritirato per ADR-013. Non bloccato: il lavoro comune non dipende da ADR-008, e la discovery hardware serve solo all'ultimo tratto.

gba-switch-trading: clonare `kinnay/LDN` e `tornadus/frlg-ldn-trade` e leggere il codice di `frlgtrade.py`, che nessuno ha ancora aperto. Prima di allestire qualsiasi cosa va accertato quale scheda Wi-Fi c'e' su questa macchina e se supporta la modalita' monitor: da quella risposta dipende se il track sia praticabile.
