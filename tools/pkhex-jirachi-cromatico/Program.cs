// I due Jirachi cromatici di terza generazione, sulla libreria del verificatore compilata dal clone in
// _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il filo Reddit `1xo6ud7` del 2026-11-05 indicava il Jirachi cromatico di terza generazione come una
// delle forme che dopo la chiusura di Bank non arrivano piu' a HOME, e nessuna copia ne aveva uno (`pending.md`, voce
// del 2026-11-13). Il 2026-11-16 il proprietario li ha voluti tutti e due, uno per via (ADR-126). La libreria li
// conosce come `EncounterGift3`: il Jirachi del disco bonus di Colosseum (allenatore WISHMKR, ID 20043) e quello di
// Pokemon Channel (allenatore CHANNEL, ID 40122), entrambi con il PID derivato da un seme, per cui un esemplare
// cromatico e' legale solo se il suo seme lo produce. `ConvertToPKM` con il criterio cromatico cerca quel seme.
//
// Che cosa fa. Per ciascuna delle due vie costruisce l'esemplare con l'allenatore di Smeraldo del progetto come
// ricevente, lo giudica e lo scrive come JIRACHI-<ALLENATORE>.pk3, nella forma da ottanta byte dei lotti di terza
// generazione, con un rapporto JSON che porta l'impronta SHA-256 di ciascuno. Si ferma se una delle due vie manca o
// non da' un esemplare cromatico e conforme. La libreria estrae i numeri casuali da Random.Shared: due lanci danno due
// esemplari diversi e ugualmente legali, e il risultato sono i file.
//
// Uso:  dotnet run -c Release -- CARTELLA_DI_USCITA
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length != 1)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- CARTELLA_DI_USCITA");
    return 2;
}
var uscita = Directory.CreateDirectory(args[0]).FullName;
if (Directory.EnumerateFiles(uscita, "*.pk?").Any())
{
    Console.Error.WriteLine($"rifiuto: {uscita} contiene gia' file di esemplare");
    return 1;
}
var tr = new SimpleTrainerInfo(GameVersion.E) { OT = "Alessio", TID16 = 42317, SID16 = 58164, Language = (int)LanguageID.Italian };
var modello = new PK3 { Species = (ushort)Species.Jirachi, Language = (int)LanguageID.Italian };
var incontri = EncounterMovesetGenerator.GenerateEncounters(modello, Array.Empty<ushort>(),
        GameVersion.E, GameVersion.R, GameVersion.S, GameVersion.FR, GameVersion.LG, GameVersion.CXD)
    .OfType<EncounterGift3>().ToList();
var voci = new JsonArray();
foreach (var allenatore in new[] { "WISHMKR", "CHANNEL" })
{
    var enc = incontri.FirstOrDefault(e => e.OriginalTrainerName == allenatore);
    if (enc is null)
    {
        Console.Error.WriteLine($"la libreria non ha il dono di Jirachi con allenatore {allenatore}");
        return 1;
    }
    var pk = enc.ConvertToPKM(tr, new EncounterCriteria { Shiny = Shiny.Always });
    var la = new LegalityAnalysis(pk);
    if (!pk.IsShiny || !la.Valid)
    {
        Console.Error.WriteLine($"{allenatore}: cromatico {pk.IsShiny}, conforme {la.Valid}\n{la.Report()}");
        return 1;
    }
    var dati = new byte[pk.SIZE_STORED];
    pk.WriteDecryptedDataStored(dati);
    var nome = $"JIRACHI-{allenatore}.pk3";
    File.WriteAllBytes(Path.Combine(uscita, nome), dati);
    voci.Add(new JsonObject
    {
        ["file"] = nome, ["allenatore"] = pk.OriginalTrainerName, ["id"] = pk.TID16, ["gioco"] = pk.Version.ToString(),
        ["lingua"] = ((LanguageID)pk.Language).ToString(), ["livello"] = pk.CurrentLevel, ["pid"] = pk.PID.ToString("X8"),
        ["natura"] = pk.Nature.ToString(), ["cromatico"] = pk.IsShiny, ["conforme"] = la.Valid,
        ["impronta"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant(),
    });
    Console.WriteLine($"{nome}: {pk.OriginalTrainerName} {pk.TID16}, {pk.Version}, livello {pk.CurrentLevel}, PID {pk.PID:X8}, cromatico, conforme");
}
File.WriteAllText(Path.Combine(uscita, "rapporto.json"), new JsonObject
{
    ["libreria"] = typeof(SaveFile).Assembly.GetName().Version?.ToString(),
    ["voci"] = voci,
}.ToJsonString(new JsonSerializerOptions { WriteIndented = true }) + "\n");
return 0;
