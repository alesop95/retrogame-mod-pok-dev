# Runbook del giro sulla cartuccia del Rubino: identificativo segreto e Pokédex

> Documento autorato, scritto il 2026-10-07. Descrive una sola scrittura sulla cartuccia del Rubino di prova che attua insieme due decisioni del proprietario: ADR-099, che porta a 58164 l'identificativo segreto dei 101 esemplari di origine Smeraldo del complemento, e ADR-089, che registra nel Pokédex come viste e catturate le specie presenti nella cartuccia. Vale la regola `.claude/rules/hardware-and-perimeter.md`: nessuna scrittura senza doppia copia verificata e senza rilettura confrontata byte per byte. I passi con la cartuccia in mano sono del proprietario; la composizione del file e le verifiche sono dell'agente.

## Che cosa cambia e che cosa no

Lo strumento è `tools/pkhex-allinea-gen3`. Cambia soltanto due cose. La prima sono i due byte del SID, all'offset 6 dell'intestazione, degli esemplari con TID 42317 e SID 0: la libreria li cifra di nuovo, perché la chiave di cifratura della terza generazione dipende dall'identificativo, ma i dati decifrati restano identici, e PID e cromaticità non cambiano, perché negli incontri di Smeraldo il SID entra solo nella cromaticità. La seconda sono i contrassegni del Pokédex delle specie presenti in squadra e nei box: «visto» nelle tre copie che Rubino confronta, `gSaveBlock2.pokedex.seen`, `gSaveBlock1.dexSeen2` e `dexSeen3`, e «catturato» in `gSaveBlock2.pokedex.owned`, secondo `GetSetPokedexFlag` di pokeruby (`src/pokedex.c` riga 3986); più la personalità di Unown, se Unown è presente e non ancora registrato. Non tocca la squadra, lo zaino, l'allenatore, gli eventi, i nomi e gli sfondi dei box, né lo slot di salvataggio inattivo; non sblocca il Pokédex nazionale.

Prova a secco del 2026-10-07 sull'ultima rilettura, `rubino/01-2026-09-28-complemento/…-2026-09-28-READBACK.sav`, con il file prodotto nello scratchpad e mai scritto sulla cartuccia:

| Misura | Valore |
|---|---|
| esemplari con SID corretto da 0 a 58164 | 101 |
| specie presenti fra squadra e box | 286 |
| specie catturate e viste prima | 6 e 8 |
| specie accese | 280, di cui 128 del Pokédex di Hoenn |
| Pokédex di Hoenn dopo | 134 catturati, 135 visti |
| Pokédex nazionale dopo, non visibile | 286 catturati, 287 visti |
| esemplari conformi alla libreria, prima e dopo | 376 su 376 nei box |
| verifica indipendente con `pokebridge`, senza la libreria | slot inattivo e coda del file identici; nella sezione piccola 102 byte diversi, tutti nel Pokédex; nella grande 98, tutti nelle due copie dei visti; nel deposito 101 posti cambiati solo ai byte 6 e 7 con i dati decifrati identici, nessun byte cambiato fuori dai record; squadra identica; indice di salvataggio invariato |

I numeri della scrittura vera saranno diversi, perché il proprietario ha giocato dopo il 2026-09-28: l'agente li ricalcola sull'estrazione nuova e li scrive qui prima della scrittura.

## Decisione da prendere prima

Il Pokédex nazionale. Le specie fuori da Hoenn vengono registrate comunque, ma restano invisibili finché il Pokédex nazionale non è sbloccato, e sbloccarlo cambia la progressione della partita. Lo strumento non lo sblocca. Se il proprietario lo vuole, è una decisione a sé, da prendere prima della scrittura per non scrivere la cartuccia due volte.

## Passi

**Passo 1, proprietario.** Estrarre il salvataggio dalla cartuccia del Rubino con FlashGBX, in sola lettura, due volte. Salvare la prima lettura in `_notes/salvataggi/cartucce/rubino/02-<data>-sid-pokedex/` con il nome `Pokemon - Versione Rubino (Italy) - ALESSIO-49107-<ore>-<data>.sav`, e la seconda nella stessa cartella con il suffisso `-LETTURA2`. Copiare la prima anche nella radice di `J:\backup salvataggi pokèmon\`, che è l'altro disco usato per il Rubino il 2026-09-28.

**Passo 2, proprietario, con l'agente che rilegge l'esito.** Verificare che le due letture e la copia sull'altro disco coincidano. In PowerShell:

```powershell
cd "E:/retrogame-mod-pok-dev/_notes/salvataggi/cartucce/rubino/02-<data>-sid-pokedex"
Get-FileHash *.sav, "J:/backup salvataggi pokèmon/Pokemon - Versione Rubino (Italy) - ALESSIO-49107-<ore>-<data>.sav" -Algorithm SHA256
```

In Bash:

```bash
cd "/e/retrogame-mod-pok-dev/_notes/salvataggi/cartucce/rubino/02-<data>-sid-pokedex"
sha256sum *.sav "/j/backup salvataggi pokèmon/Pokemon - Versione Rubino (Italy) - ALESSIO-49107-<ore>-<data>.sav"
```

Le tre impronte devono essere uguali. Se due letture differiscono, il collegamento è intermittente e si ricomincia dal passo 1, perché una lettura troncata sembra valida.

**Passo 3, agente.** Comporre il file nuovo, che non sovrascrive l'estrazione:

```powershell
cd "E:/retrogame-mod-pok-dev/tools/pkhex-allinea-gen3"
dotnet run -c Release -- "<estrazione>.sav" "<estrazione>-CORRETTO.sav" --tid 42317 --da 0 --a 58164
```

```bash
cd "/e/retrogame-mod-pok-dev/tools/pkhex-allinea-gen3"
dotnet run -c Release -- "<estrazione>.sav" "<estrazione>-CORRETTO.sav" --tid 42317 --da 0 --a 58164
```

Lo strumento rifiuta se un solo esemplare cambia PID o cromaticità o viene contestato, rilegge il file e lo cancella se una verifica cade, e scrive accanto `<estrazione>-CORRETTO.sav.allineamento.json`. Poi l'agente ripete la verifica indipendente con `pokebridge` della tabella sopra, giudica tutti gli esemplari prima e dopo con `tools/pkhex-elenco-copie`, ricalcola i numeri e li scrive in questo documento, registra le impronte in `_notes/salvataggi/cartucce/LEGGIMI.md`, e scrive la lista di controllo del passo 6 con i numeri veri.

**Passo 4, proprietario.** Scrivere `<estrazione>-CORRETTO.sav` sulla cartuccia con FlashGBX, e subito dopo, senza scollegare la cartuccia, rileggerla con FlashGBX in un file `<estrazione>-READBACK.sav` nella stessa cartella.

**Passo 5, agente.** Confrontare `-READBACK.sav` con `-CORRETTO.sav` byte per byte: devono essere identici. Se non lo sono, la cartuccia non si usa e si torna all'estrazione del passo 1, che è il backup.

**Passo 6, proprietario.** Il controllo in gioco, con la lista scritta dall'agente al passo 3 prima di accendere la console: il Pokédex di Hoenn con i contatori attesi di visti e catturati; un esemplare di origine Smeraldo del complemento, scelto dall'agente con box e posto, che nel riepilogo mostra lo stesso numero identificativo di prima, perché il gioco mostra solo il TID; la squadra e lo zaino come prima.

## Che cosa non fa questo giro

Non riguarda la cartuccia di Smeraldo, i cui esemplari dell'allenatore del progetto hanno già 58164 e il cui Pokédex è già completo. Non riguarda le copie per HOME, già rifatte il 2026-10-07 come `-fin2`. E non è reversibile se non dall'estrazione del passo 1: per questo le sue due copie verificate sono la condizione per tutto il resto.
