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

## Il Pokédex nazionale, deciso

Non si sblocca (ADR-103). Le specie fuori da Hoenn vengono registrate comunque e il proprietario le vedrà quando sbloccherà il nazionale giocando. Il Pokédex di Hoenn non risulterà completo: sulla prova a secco le specie di Hoenn presenti sul Rubino sono 134 su 202, perché le altre 68 la collezione le tiene su Smeraldo (ADR-080), e lo strumento registra solo le specie presenti.

## Giro del 2026-11-20, che prevale sui passi sotto dove li contraddice

Il proprietario ha portato il Rubino il 2026-11-20, subito dopo la chiusura di Smeraldo. Il giro aggiunge a ADR-099 e ADR-089 gli otto incontri della Grotta Mutevole di ADR-134, terza modifica, cioè i file di `_notes/lotti/lotto-grotta-mutevole/`: entrano nei posti liberi del deposito, sono contestati da PKHeX perché l'evento non è mai stato distribuito, e non vanno mai in HOME. Prima di comporre, l'agente misura sull'estrazione che cos'altro manca al Rubino, con lo stesso metodo usato per Smeraldo, e lo propone al proprietario prima di scrivere. La cartella è `_notes/salvataggi/cartucce/rubino/02-20261120-estrazione/`, che sostituisce il nome `02-<data>-sid-pokedex` del passo 1; la copia sull'altro disco va in `J:/backup salvataggi pokèmon/rubino-02-20261120-estrazione/`. I passi della lettura, tutti di sola lettura, sono questi.

1. In FlashGBX clicca «Disconnect» se è collegato, poi stacca il cavo USB dal lettore.
2. Inserisci il Rubino nella fessura per Game Boy Advance, dritto e fino in fondo, nello stesso verso di Smeraldo.
3. Ricollega il cavo nella porta frontale sinistra del PC.
4. In FlashGBX clicca «Game Boy Advance» e controlla che il LED «Mode» sia blu.
5. Clicca «Refresh» e controlla che a sinistra compaia Pokemon - Versione Rubino con «Save Type» 1M FLASH (128 KiB).
6. Clicca «Backup Save Data», vai nella cartella `02-20261120-estrazione`, scrivi `lettura1.sav` e premi Salva. Aspetta la fine.
7. Di nuovo «Backup Save Data», stessa cartella, `lettura2.sav`.
8. «Disconnect», stacca il cavo, poi togli la cartuccia.
9. Agente: controlla che i due file siano di 131072 byte e identici, li rinomina per esteso e li copia su J: con lo SHA-256; poi misura e propone.

In questo giro i pulsanti di scrittura non si toccano: «Write Save Data», «Erase cartridge save data» e «Write ROM» restano vietati fino al file composto e approvato.

Esito della lettura, 2026-11-20: due letture identiche di 131072 byte, SHA-256 `0c2be593…3717a98`, con allenatore ALESSIO 49107 a 6 ore e 24 minuti, nessuna medaglia; rinominate per esteso e copiate su J: in `backup salvataggi pokèmon/rubino-02-20261120-estrazione/` con lo stesso SHA-256. Rispetto alla rilettura del 2026-09-28 la partita ha 10 minuti e un salvataggio in più: soldi da 3428 a 127228, caramelle rare rabboccate, e un Seedot di livello 43 catturato giocando nel box 13, posto 25. PKHeX giudica conformi tutti i 377 esemplari, cioè i 376 del complemento e il Seedot; 43 posti liberi.

Composizione, 2026-11-20 (ADR-135). Primo passo, `tools/pkhex-allinea-gen3` come al passo 3 sotto: 101 SID da 0 a 58164, 286 specie presenti, 280 accese nel Pokédex, nazionale non sbloccato. Secondo passo, `gba-save-extraction-smeraldo/tools/rubino_ultimo_giro.py`: gli otto della Grotta Mutevole nel box 13, posti 17-24 (Mareep, Pineco, Houndour, Teddiursa, Aipom, Shuckle, Stantler, Smeargle), il Biglietto Eone nel primo posto della tasca Oggetti Chiave e `FLAG_SYS_HAS_EON_TICKET`. Verifiche sul file finale: PKHeX 385 esemplari, 377 conformi e i soli otto della grotta contestati, come atteso; 101 esemplari di ALESSIO 42317 con SID 58164; Pokédex 286 catturati e 287 visti, con le tre copie dei visti uguali e nessuna specie dei box non catturata; di Hoenn 134 catturati e 135 visti; rispetto al passo intermedio cambiano soltanto i byte dei posti 17-24 del box 13, del posto 1 della tasca Oggetti Chiave, del contrassegno e delle intestazioni delle tre sezioni toccate; entrambi gli slot hanno 14 sezioni valide. Il file da scrivere sta in `E:/retrogame-mod-pok-dev/_notes/salvataggi/cartucce/rubino/03-20261120-scrittura/` con «DA SCRIVERE» nel nome, SHA-256 `77667946…6c85a9f75`, copiato su J: in `backup salvataggi pokèmon/rubino-03-20261120-scrittura/`. Mappa `MAPPA-BOX-RUBINO.md` e stampa `MAPPA-BOX-COLLEZIONE.pdf` rigenerate da questo file, con la grotta e la cattura in legenda.

Scrittura. Solo i passi 13-16 scrivono.

10. Inserisci il Rubino a cavo staccato, poi collega il cavo nella porta frontale sinistra.
11. In FlashGBX clicca «Game Boy Advance» e controlla che il LED «Mode» sia blu.
12. Clicca «Refresh» e controlla che compaia Pokemon - Versione Rubino con «Save Type» 1M FLASH (128 KiB).
13. Clicca la freccia di «Write Save Data» e scegli «Restore from save data file». Mai «Erase cartridge save data».
14. Vai nella cartella `03-20261120-scrittura` e seleziona il file con «DA SCRIVERE» nel nome. Controlla il nome prima di premere «Apri»: FlashGBX non chiede conferma e comincia subito a scrivere.
15. Aspetta senza toccare cavo e cartuccia, fino a «The save data was written and verified successfully!».
16. Clicca «Backup Save Data» e salva nella stessa cartella come `rilettura.sav`.
17. «Disconnect», stacca il cavo, poi togli la cartuccia.
18. Agente: confronta byte per byte `rilettura.sav` con il file scritto, la rinomina per esteso, copia su J: con lo SHA-256 e aggiorna i registri.
19. Proprietario, quando gioca: nella tasca Oggetti Chiave c'è il Biglietto Eone; il Pokédex di Hoenn dice 135 visti e 134 catturati; nel box 13 i posti 17-24 hanno gli otto della grotta e il 25 il Seedot; il Voltorb del box 1, posto 16, mostra ancora l'ID 42317. L'Isola Remota si raggiunge dal porto di Porto Alghepoli solo dopo la Lega.

Esito della scrittura, 2026-11-20: scritta dal proprietario con «Restore from save data file»; la rilettura è identica byte per byte al file scritto, SHA-256 `77667946…6c85a9f75`, rinominata per esteso («rilettura dopo la scrittura, identica byte per byte al file scritto») e copiata su J: in `backup salvataggi pokèmon/rubino-03-20261120-scrittura/` con lo stesso SHA-256. Mappa e stampa erano già generate da quel file. ADR-099, ADR-089, ADR-134 e ADR-135 sono attuati sul Rubino; resta il passo 19 in gioco.

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
