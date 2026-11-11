# Refactor 11. Un giudizio di conformità vale nel formato in cui si legge il dato

> Scheda di dettaglio della voce 11 di `studio-didattico-master.md`. Entra nel codice di PKHeX.Core che produce il rifiuto di trasferimento e nella regola `resta_in_console` di `tools/stampa-collezione.py`. I fatti stanno in `pokedex-home-completo/COPIE-PER-HOME.md`, sezioni del 2026-11-09, del 2026-11-10 e del 2026-11-11.

## Il caso

Il protocollo di un giro, in `pokedex-home-completo/RUNBOOK-PASSO-2.md`, verifica sui byte tutto ciò che si può leggere: la copia scritta sulla SD, la rilettura dopo il ripristino, il giudizio della rilettura con la libreria. Sul tratto dalla banca a HOME, che non si osserva, l'unica misura è il totale del deposito. Due volte il totale è salito meno del previsto: al giro 6 di 689 invece di 695, al giro 8 di 609 invece di 613. Gli esemplari mancanti sono rimasti nei box della partita, e il loro posto li ha identificati nel giudizio della copia.

## Dove stava la regola

Il Pikachu Cosplay, in `PKHeX.Core/Legality/Verifiers/FormVerifier.cs`:

```csharp
case Pikachu when enc.Generation == 6: // Cosplay
    if (form != 0 && pk.Format != 6) // Regular Pikachu, OK.
        return GetInvalid(TransferBad); // Can't transfer.
    break;
```

La condizione `pk.Format != 6` è il punto: in un file di sesta generazione il controllo passa sempre, e il giudizio delle copie si fa proprio lì. I totem, in `EncounterStatic7.cs` riga 40 e `TransferVerifier.cs` righe 149-157:

```csharp
public bool IsTotemNoTransfer => Species is (int)Core.Species.Marowak or (int)Core.Species.Araquanid
    or (int)Core.Species.Togedemaru or (int)Core.Species.Ribombee;

if (enc is EncounterStatic7 { IsTotem: true } s)
{
    if (s.IsTotemNoTransfer || pk.Form != s.GetTotemBaseForm())
    {
        data.AddLine(GetInvalid(TransferBad));
        return;
    }
}
```

Il blocco sta dentro il ramo che verifica un esemplare nato prima dell'ottava generazione e letto in un formato successivo. Gli altri sette totem passano la prima condizione e, tornati alla forma base, anche la seconda: è ciò che HOME ha fatto.

## La prima correzione, e perché non bastava

Dopo il giro 6 `tools/stampa-collezione.py` ha guadagnato `resta_in_console`, che riconosceva il Cosplay; dopo il giro 8 ha guadagnato la tabella dei totem:

```python
TOTEM_NON_TRASFERIBILI = {105: 2, 752: 1, 777: 1, 743: 1}

def resta_in_console(e):
    if e.get("generazione") == 7 and TOTEM_NON_TRASFERIBILI.get(e["numero"]) == e.get("forma_n", 0):
        return ("DSstatoincopia", "resta in Ultraluna", ...)
    if e["numero"] == 25 and e.get("generazione") == 6 and e.get("forma_n", 0) in range(1, 7):
        return ("DSstatoincopia", "resta in Rubino Omega", ...)
    return None
```

È una regola corretta per il pedigree, che deve dire perché un esemplare non è in HOME. Come controllo preventivo è invece un elenco che cresce di un caso per volta, e ogni caso costa un giro con un esemplare rimasto in console. La stessa cosa vale per il controllo delle copie restanti fatto il 2026-11-10, che cercava categorie scelte a mano: trova soltanto ciò che chi lo scrive sapeva già di dover cercare.

## L'elenco chiuso

La domanda giusta è quali regole della libreria possano rifiutare un trasferimento, e la libreria la rende enumerabile perché il rifiuto ha un codice solo. Cercando `TransferBad` nel clone a `bfe89c7` escono sei punti: `FormVerifier.cs` riga 47 (Cosplay), `MiscVerifierPK7.cs` riga 21 (stato d'evento del resort al massimo), `TransferVerifier.cs` righe 154 (totem), 170 (dimensioni nulle, solo per i formati che le hanno, dall'ottavo in poi) e 186 (specie o forma assente dal gioco di destinazione, che riguarda i giochi e non il deposito), `MiscVerifierPK9.cs` riga 75 (formato 9). Accanto, `TradeRestrictions.cs` dichiara intrasferibili il Pichu Spunzorecchio, i Compagni di Let's Go nel formato 7, le forme fuse e quelle di sola lotta, e in settima generazione i cristalli Z tenuti. Sul giudizio `dopo-20261109b.json` le copie HOME7, HOME10 e GIAPPONE2 non hanno esemplari in nessuna di queste regole; lo stato del resort non è nel giudizio salvato, e la sua assenza resta un'inferenza dai giri 7 e 8.

## Che cosa resta da fare

Leggere sei punti è meglio di un elenco scelto a mano, ma resta lettura umana: una versione nuova della libreria con una regola nuova non entra nel controllo finché qualcuno non rifà la ricerca. Il controllo che non dipende dalla lettura è far porre la seconda domanda a `tools/pkhex-elenco-copie`, cioè giudicare ogni esemplare anche dopo averlo convertito nel formato di arrivo, e segnare a parte quelli che diventano non validi per trasferimento. È scritto in `pending.md` come lavoro dell'agente; prima di farlo va misurato quanti falsi rifiuti produce la conversione verso un formato di Switch per specie che quel gioco non contiene, perché il deposito non è un gioco e la regola della riga 186 non vale per lui.
