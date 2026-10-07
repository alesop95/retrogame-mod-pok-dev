# Refactor 06. Una scrittura verificata da chi non l'ha fatta, e un nome di file conteso

> Scheda di dettaglio della voce 6 di `studio-didattico-master.md`. Entra nello strumento nuovo `tools/pkhex-allinea-gen3`, nella verifica scritta con `pokebridge`, nel runbook `gba-save-extraction-smeraldo/RUNBOOK-RUBINO-SID-POKEDEX.md`, e in tre punti di pokeruby e della libreria PKHeX.Core.

## Il contesto

La cartuccia del Rubino doveva ricevere due correzioni, ADR-099 sull'identificativo segreto di 101 esemplari e ADR-089 sul Pokédex, e una cartuccia si scrive una volta sola quando si può. La regola del progetto vuole una verifica prima della scrittura che dimostri che nessun byte fuori da quelli dichiarati cambia.

## Che cosa dice il gioco

Prima di scrivere si è letta la regola sul sorgente di Rubino, perché la voce di `pending.md` lo chiedeva e perché un errore qui non produce un messaggio: il gioco cancella in silenzio.

```c
case FLAG_GET_SEEN:
    if (gSaveBlock2.pokedex.seen[index] & mask)
    {
        if ((gSaveBlock2.pokedex.seen[index] & mask) == (gSaveBlock1.dexSeen2[index] & mask)
         && (gSaveBlock2.pokedex.seen[index] & mask) == (gSaveBlock1.dexSeen3[index] & mask))
            retVal = 1;
        else
        {
            gSaveBlock2.pokedex.seen[index] &= ~mask;
            gSaveBlock1.dexSeen2[index] &= ~mask;
            gSaveBlock1.dexSeen3[index] &= ~mask;
            retVal = 0;
        }
    }
```

È `GetSetPokedexFlag` di `src/pokedex.c`, riga 3986 del clone `5784633`. Uno strumento che accendesse la sola copia di SaveBlock2, che è quella che PKHeX mostra e che la misura del 2026-09-28 aveva letto, otterrebbe che il gioco spenga tutto alla prima lettura del Pokédex. La libreria accende le tre copie (`SAV3.cs` righe 555-562), agli stessi offset (`SaveBlock3LargeRS.cs` righe 22 e 171: 0x938 e 0x3A8C), e lo strumento la usa.

## La verifica che non si fida dello strumento

`pkhex-allinea-gen3` rilegge il proprio file e controlla specie, PID, SID e le tre copie dei visti per tutte le 386 specie. È una buona verifica, ma ha un limite di principio: usa la stessa libreria che ha scritto, quindi se la libreria interpretasse male un indirizzo leggerebbe nello stesso posto sbagliato e direbbe che va tutto bene. La seconda verifica è scritta con `pokebridge`, il pacchetto del progetto che legge i salvataggi di terza generazione senza la libreria, e fa una sola cosa: dice quali byte sono cambiati.

```python
ds = diff(a.small(), b.small()); dl = diff(a.large(), b.large())
print('small', zone(ds, [(0x1C, 0x24), (0x28, 0x90)]))
print('large', zone(dl, [(0x938, 0x938 + 52), (0x3A8C, 0x3A8C + 52)]))
```

Le zone ammesse sono scritte dal sorgente di pokeruby, non dalla libreria. Esito sulla prova a secco: 102 byte cambiati nella sezione piccola e 98 nella grande, nessuno fuori dalle zone; slot inattivo e coda del file identici; nel deposito 101 posti cambiati solo ai byte 6 e 7, con i dati decifrati identici benché la parte cifrata cambi, perché la chiave è PID xor identificativo; nessun byte cambiato nel deposito fuori dai record; squadra identica; indice di salvataggio invariato.

Durante la stessa verifica un controllo è stato sbagliato e lo si dice: cercare Spinda con l'indice interno 327 non trovava nulla, perché dopo Celebi la terza generazione numera le specie in modo diverso dal Pokédex nazionale. Il controllo giusto, fatto sul numero nazionale letto dalla libreria, dice che Spinda non c'è sul Rubino, e quindi che la sua personalità a 0 è corretta.

## Il nome di file conteso

La prima versione dello strumento scriveva il proprio rapporto come `<uscita>.rapporto.json`. Al giudizio di tutti gli esemplari con `pkhex-elenco-copie` lo strumento si è fermato con un'eccezione:

```
System.NullReferenceException ... at Program.<Main>$ ... Program.cs:line 41
```

Alla riga 41 `pkhex-elenco-copie` legge `<salvataggio>.rapporto.json` come rapporto di `pkhex-scrivi-salvataggio` e cerca il campo `voci`, che il rapporto nuovo non ha. Due strumenti avevano adottato la stessa convenzione di nome per due formati diversi, e il primo che li ha incontrati entrambi l'ha scoperto. Il rapporto nuovo si chiama `<uscita>.allineamento.json`, e il motivo è scritto nel commento in testa allo strumento e in `docs/22-strumenti.md`.

## Come estendere il pattern

Una verifica vale per quanto non condivide con ciò che verifica. Quando lo strumento che scrive e quello che rilegge sono lo stesso, si aggiunge un controllo indipendente che non interpreta i dati ma dice soltanto quali byte sono cambiati, e le zone ammesse si prendono da una fonte diversa da quella che ha guidato la scrittura. E un nome di file usato come convenzione fra strumenti è un'interfaccia: chi ne adotta uno lo cerca prima fra quelli già in uso.
