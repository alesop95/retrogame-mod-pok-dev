# Snapshot di sincronizzazione

Da leggere per primo a inizio sessione. Fotografa lo stato del progetto al commit di riferimento e mappa ogni scheda al suo stato di verifica. È la fonte di verità su cosa è fatto, non le spunte del diario.

Questo progetto ha più sottoprogetti paralleli, oggi dieci, quindi il punto di ripresa è un blocco di righe invece che una sola. La riga "Fuoco corrente" è la fonte di verità unica su quale track è attivo adesso: task paralleli non significa nessun default, significa un default dichiarato più N tracce leggibili.

## Stato

```
Branch attivo:         main
Commit di riferimento: 8620f4a, Allineamento dal template al commit 071db2e
Data snapshot:         2026-11-23: contatti di Verde Foglia puliti con l'alcol, la cartuccia si avvia ancora sul GBA SP; lettura nel GBxCart da rifare con il runbook. Al 2026-11-20: giro 14 DIAMANTE1 IN HOME dal 2026-11-17 (7466 prima della liberazione dei 996, 6470 dopo); nessun lotto in attesa della banca; Smeraldo e Rubino scritti e chiusi; i 578 pedigree senza data chiusi; Verde Foglia dopo la pulizia della settimana prossima. Correzione del 2026-11-20: i recap del 2026-11-18 e 2026-11-20 dicevano «245 di Diamante in attesa della banca», copiando questa riga che era rimasta indietro
```

## Stato di verifica delle schede

| Scheda | Sottoprogetto | last-verified | Stato |
|---|---|---|---|
| STACK.md | trasversale | 90adea9 | riconciliata il 2026-09-29 con sync-context: strumenti riconteggiati (75 in `tools/`, 30 di Smeraldo, cinque C#), dipendenze esterne da due a cinque, libreria PKHeX.Core, LED del lettore e orologio di Smeraldo; `covers-paths` esteso a `tools/` e `scripts/` |
| design-and-security.md | trasversale | 90adea9 | riconciliata il 2026-09-29 con sync-context: storia pubblica bonificata (ADR-087) e presidio di anonimizzazione (ADR-091), salvataggi di terzi a diciotto, divisione del lavoro sul tratto di Bank (ADR-081), verifica aperta sulle `prod.keys` della via GB-Link |
| deployment.md | trasversale | 8cc1798 | non applicabile, covers-paths vuoto per scelta |
| dev-testing.md | trasversale | 90adea9 | riconciliata il 2026-09-29 con sync-context: suite del ponte riletta a 206, protocollo di Smeraldo esteso alle scritture fino al Rubino con il passo del giudizio di PKHeX, giudizio dei lotti con la libreria, sezione nuova sui controlli di `chiudi`; `covers-paths` esteso a `tools/` e `scripts/` |
| current-work.md | trasversale | 90adea9 | riconciliata il 2026-09-29 con sync-context: righe di Pokedex, distribuzioni, ponte, Smeraldo e 3DS riscritte, paragrafo di riconciliazione nuovo |
| roadmap.md | trasversale | 90adea9 | riconciliata il 2026-09-29 con sync-context: sezione di aggiornamento con cinque affermazioni diventate false e due fatti nuovi, cioè il Pokédex delle cartucce (ADR-089) e la via GB-Link |
| sub-3ds-modding.md | 3ds-related | 90adea9 | riconciliata il 2026-09-29: al blocco 1 era cambiata solo nella forma, e al blocco 5 ha ricevuto il backup della SD in `J:\3DS - 03092026\` detto dal proprietario il 2026-09-28 |
| sub-smeraldo-save-fix.md | gba-save-extraction-smeraldo | 10532eb | riconciliata il 2026-09-29 con sync-context: sezione di stato in testa (Smeraldo concluso, Rubino scritto, Parco Lotta, vincoli, quattro punti aperti), tre frasi superate marcate, prossimo passo e decisioni aperte aggiornati, stato vecchio conservato come storico |
| sub-gen12-gen3-bridge.md | pokemon-gen12-gen3-bridge | 90adea9 | riconciliata il 2026-09-29: al blocco 1 di sync-context era stata data per cambiata solo nella forma, ma diceva ancora che `parco_amici.py` produce 203 record, smentito da ADR-082; corretta nel blocco 5 |
| sub-gba-switch-trading.md | gba-switch-pokemon-trading | 89a13f7 | verificata il 2026-09-29 con sync-context: handoff spostato in `handoff/`, la scheda non lo cita per percorso, nessun cambio |
| sub-poke-automation.md | poke-automation-study | 89a13f7 | verificata il 2026-09-29 con sync-context: `docs/fonti/` rinominata in `docs/mappa-fonti/`, nessun cambio alla scheda |
| sub-distributions-events.md | recreate-pokemon-distributions-events | 6ee3543 | riconciliata il 2026-09-29 con sync-context: aggiunta la sezione sulla libreria che produce e giudica (ADR-081, 2010 su 2010), segnato superato il lotto della sintesi del Parco Amici (ADR-082), riscritto il prossimo passo |
| sub-poke-ace.md | poke-ace | 89a13f7 | verificata il 2026-09-29 con sync-context: nessun file cambiato nell'area |
| sub-generation-from-switch.md | generation-from-switch | 89a13f7 | verificata il 2026-09-29 con sync-context: nessun file cambiato nell'area |
| sub-cart-battery.md | cart-battery-restoration | 89a13f7 | riconciliata il 2026-09-29 con sync-context: rischio di tensione chiuso il 2026-09-15 (LED blu 3,3 V, rosso 5 V) e lettore validato, due delta nella scheda |
| sub-pokedex-home-completo.md | pokedex-home-completo | e22c1e9 | aggiornata il 2026-11-09 (ADR-120): stato e prossimo passo sulla tabella dei giri di `ROADMAP.md`, 6212 esemplari e 6088 conformi, giri 1-3 in HOME, giro 4 sulla SD |
| sub-switch-modding.md | switch-modding | 2d5f940 | creata il 2026-11-17 (ADR-133): studio della Switch usata da modificare, in attesa del modello del proprietario |

Le cose in sospeso non stanno qui ma in `pending.md`, che va letto subito dopo questo file: materiale atteso, credenziali, fonti in sospeso, strumenti da richiamare a una condizione, debito di lettura, punti aperti e blocchi materiali.

## Punto di ripresa

AGGIUNTA DEL 2026-11-20, riordino. Il punto di ripresa era arrivato a 129 KB con le aggiunte dal 2026-08-24. Su richiesta del proprietario l'indice è stato copiato identico in `.claude/memory/archivio/index-fino-al-2026-11-20.md` e qui restano lo stato, la tabella delle schede, le aggiunte dal 2026-11-17 e lo stato di ogni sottoprogetto letto dalla sua scheda. Il resto della storia è nell'archivio, nel work log e in git.

AGGIUNTA DEL 2026-11-23, seconda parte, che prevale su quelle sotto. Dopo la pulizia il lettore ancora non legge Verde Foglia («Header Checksum» «Invalid (0x7F)», titolo vuoto); il salvataggio è intatto, perché il GBA SP lo legge. I rimedi, in ordine, sono in `pending.md`. ADR-136: i 10ANNI veri italiani sostituiscono uno per uno i generati identici, e il totale non cambia. Xerneas di Z-A riscattato. Catture di GO del 21 e 22 novembre lette, 96 esemplari. Voci dell'agente fatte lo stesso giorno. ADR-137: handoff travasati nelle schede e archiviati in `archivio/handoff/`. Il registro dell'archivio è smistato: 77 voci escono, ne restano 19 aperte e 35 indeterminate. La bozza del piano della tesi è in `_notes/lavoro/tesi-riscrittura/`, con quattro domande al proprietario. Il foglio pre-Switch di Reddit è usato come controllo dei lotti: nessuna specie da 1 a 807 manca (`pokedex-home-completo/CONTROLLO-FOGLIO-PRE-SWITCH.md`). Il conto di HOME si tiene per ogni movimento in `pokedex-home-completo/ESEMPLARI-DA-GO.md`.

AGGIUNTA DEL 2026-11-23, ripresa. `/riprendi` ha trovato l'albero pulito e una sola divergenza, il blocco «Stato» fermo a `8d7f949` mentre HEAD era `8620f4a` (allineamento dal template `071db2e`, già nel work log), corretto. Il proprietario riferisce che i contatti di Verde Foglia sono stati puliti con l'alcol e che la cartuccia si avvia ancora sul Game Boy Advance SP: la pulizia non l'ha danneggiata. Prossimo: la lettura nel GBxCart con i passi 1-15 della sezione «Verde Foglia» di `pokedex-home-completo/RUNBOOK-ESTRAZIONI.md`, foto del riquadro all'agente prima del backup. Le fonti vive e le liste di eventi segnalate dagli hook del 2026-11-23 sono state lette e segnate lo stesso giorno, senza lotti nuovi e senza esemplari in HOME da correggere (`_notes/fonti/raccolte/differenze-fonti-vive-2026-11-23/SINTESI.md`). Il gate dei pacchetti è dovuto e si propone dopo la lettura.

AGGIUNTA DEL 2026-11-18. Verde Foglia funziona sul GBA SP; Smeraldo letta nel lettore con sei intestazioni identiche, quindi il lettore è sano e il guasto è il contatto di Verde Foglia (pulizia con alcol il 2026-11-21). Smeraldo estratta in doppia copia (E: e J:). ADR-134: Smeraldo si chiude come lo Smeraldo più completo per un giocatore italiano; il file dell'ultimo giro (Roccia di Re, Plain sui box 10 e 11, 120 decorazioni) è SCRITTO il 2026-11-20 con rilettura identica byte per byte, in doppia copia su E: e J:. Smeraldo è chiusa, resta il controllo in gioco (passo 23 di `pokedex-home-completo/RUNBOOK-ESTRAZIONI.md`). Gli otto della Grotta Mutevole vanno sul Rubino, mai in HOME. Il 2026-11-20 il Rubino è SCRITTO (ADR-135: Pokédex coerente con i box, Biglietto Eone; SID 58164; la grotta nel box 13), con rilettura identica byte per byte in doppia copia; resta il passo 19 in gioco di `gba-save-extraction-smeraldo/RUNBOOK-RUBINO-SID-POKEDEX.md`. PUCCETTO, il primo della squadra di Verde Foglia, è la priorità del giro di Verde Foglia verso HOME.

AGGIUNTA DEL 2026-11-17, sera, terza parte, che prevale su quelle sotto. Giro 14 IN HOME: 7466, cioè 7221 più i 245 di DIAMANTE1, prima di ogni liberazione; punto 18 fatto. ADR-132 toglie il limite su Bank (l'errore era 006-0112); ADR-133 apre `switch-modding/` e somma alla collezione i lotti della fase Switch. Prossimo: il proprietario libera i 996 con l'elenco da 7466 a 6470 cerca una Switch del primo modello usata (non ne ha una) e manda il numero di serie del candidato; l'agente lavora in parallelo (578 pedigree senza data, eventi nuovi, file unico della collezione). Voci «AL 2026-11-17, sera» di `pending.md`.

AGGIUNTA DEL 2026-11-17, sera, ripresa. `/riprendi` ha trovato l'impronta di `chiudi` su `2d5f940` (16:40), albero pulito; unica divergenza il blocco «Stato» qui sopra, fermo a `e231b7a`, corretto. Il punto di ripresa resta quello dell'aggiunta sotto. Novità degli hook di apertura in `pending.md`, voce «AL 2026-11-17, ripresa».

AGGIUNTA DEL 2026-11-17, che prevale su quelle sotto. ADR-129: Verde Foglia e Diamante si estraggono con FlashGBX 5.1 e Checkpoint, senza aggiornamenti, secondo `pokedex-home-completo/RUNBOOK-ESTRAZIONI.md`; lettura di Verde Foglia in corso. Il proprietario libera i 996 vecchi in HOME (da 7221 a 6225) con l'elenco già stampato, che ha le stesse righe. ADR-128: gli esemplari di terza e quarta generazione prodotti da qui in avanti portano un giorno di Poké Transfer fra il 2011-03-04 e il 2013-12-31; DA DECIDERE se ridatare i 1964 già in HOME. Smeraldo: i 213 in HOME sono tutti i conformi dei box dell'estrazione originale; il Rubino non aveva catture nei box; mai portate le due squadre, 10 conformi estratti in `_notes/lotti/lotto-squadre-cartucce/`. Diamante si estrae con Checkpoint sul 3DS. Prossimo: estrazioni di Verde Foglia e Diamante in sola lettura mentre il proprietario libera; poi il giro di Verde Foglia, squadre e Diamante con la data di ADR-128. Voce «AL 2026-11-16, NUOVE RICHIESTE» di `pending.md`. Poi, lo stesso giorno: Diamante estratto con Checkpoint (due letture identiche su E: e J:); lotto dei suoi Pokémon conformi, cromatici e gemelli di Smeraldo compresi (ADR-130); `pkhex-scrivi-salvataggio --data-poke-transfer` attua ADR-128; giro 14 `oras-diamante-1`, 296 conformi con le squadre di Smeraldo e Rubino, sulla SD come `20261117-giro14`, verso HOME dopo la liberazione dei 996. Verde Foglia non risponde al lettore, aspetta Smeraldo come cartuccia di riferimento. ADR-131: fuori cloni dell'epoca, dieci cromatici con lo stesso PID e Floatzel; giro 14 di 245 esemplari; i pedigree di tutte le copie hanno la data vera del lotto.

```
Fuoco corrente: pokedex-home-completo, al 2026-11-23. HOME a 7466 prima della liberazione dei 996 (6470 dopo); nessun lotto in attesa della banca; prossimo lotto: Verde Foglia, contatti puliti, lettura nel GBxCart da rifare; scadenza di Bank il 2027-02-26.
```

Stato di ogni sottoprogetto, dalla prima frase della riga `stato:` della sua scheda (la scheda prevale):

- `sub-3ds-modding.md`: attivo
- `sub-cart-battery.md`: runbook scritto;
- `sub-distributions-events.md`: attivo;
- `sub-gba-switch-trading.md`: in ricerca, nessun ambiente allestito
- `sub-gen12-gen3-bridge.md`: decisione ADR-008 ancora aperta;
- `sub-generation-from-switch.md`: debito di lettura chiuso il 2026-09-01, entrambe le fonti lette;
- `sub-poke-ace.md`: tre studi scritti;
- `sub-poke-automation.md`: studio cominciato, scopo del track da decidere
- `sub-pokedex-home-completo.md`: attivo ed è il fuoco corrente;
- `sub-smeraldo-save-fix.md`: AL 2026-11-20 SMERALDO CHIUSA, ultimo giro di ADR-134 scritto (Roccia di Re, sfondi 10-11, 120 decorazioni) con rilettura identica byte per byte, in doppia copia;
- `sub-switch-modding.md`: attivo, il proprietario cerca una Switch del primo modello usata
