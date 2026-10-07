// Allenatore, identificativi, PID e stato cromatico degli esemplari di lotti e salvataggi, letti con la libreria del
// verificatore compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perché esiste. ADR-099 del 2026-10-06 fissa un solo identificativo segreto, 58164, per l'allenatore del progetto, e la
// sua verifica va ripetuta tre volte: sui lotti rigenerati, sulle copie per HOME rifatte e sulla cartuccia del Rubino. Il
// registro dei giudizi non basta, perché descrive l'identificativo nel formato che il gioco mostra: per la settima
// generazione il numero a sei cifre che mescola TID e SID, per le generazioni precedenti il solo TID. L'indagine del
// 2026-10-06 aveva letto 33858 file con script di sessione, che non sono rimasti; questo strumento è la stessa misura
// in forma ripetibile.
//
// Che cosa fa. Per ogni argomento, che può essere una cartella di esemplari, un singolo file di esemplare o un
// salvataggio, legge ogni esemplare e ne scrive in JSON l'origine (percorso del file, oppure salvataggio, box e posto),
// specie, formato, allenatore originale, TID16, SID16, PID e stato cromatico secondo la libreria. A video stampa per
// ogni argomento i conteggi per terna allenatore, TID e SID, così che un identificativo fuori posto si veda senza aprire
// il JSON. Con --tid N limita il JSON e i conteggi agli esemplari con quel TID, cioè all'allenatore del progetto.
// Non scrive e non modifica nulla oltre al file di uscita.
//
// Uso:  dotnet run -c Release -- USCITA.json [--tid N] PERCORSO [PERCORSO ...]
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

var argomenti = args.ToList();
if (argomenti.Count < 2)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- USCITA.json [--tid N] PERCORSO [PERCORSO ...]");
    return 2;
}
var uscita = argomenti[0];
argomenti.RemoveAt(0);
int? soloTid = null;
var i = argomenti.IndexOf("--tid");
if (i >= 0)
{
    soloTid = int.Parse(argomenti[i + 1]);
    argomenti.RemoveRange(i, 2);
}

var estensioni = new HashSet<string>(StringComparer.OrdinalIgnoreCase)
{
    ".pk1", ".pk2", ".pk3", ".pk4", ".pk5", ".pk6", ".pk7", ".pk8", ".pk9",
    ".ck3", ".xk3", ".bk4", ".rk4", ".pb7", ".pb8", ".pa8", ".pa9",
};
var nomi = GameInfo.GetStrings("en").Species;
var risultato = new JsonArray();
foreach (var percorso in argomenti)
{
    var voci = new List<(string Origine, PKM Pk)>();
    if (Directory.Exists(percorso))
    {
        foreach (var f in Directory.EnumerateFiles(percorso).Order(StringComparer.Ordinal))
            if (estensioni.Contains(Path.GetExtension(f)) && FileUtil.TryGetPKM(File.ReadAllBytes(f), out var pk, Path.GetExtension(f)))
                voci.Add((Path.GetFileName(f), pk));
    }
    else if (estensioni.Contains(Path.GetExtension(percorso)))
    {
        if (FileUtil.TryGetPKM(File.ReadAllBytes(percorso), out var pk, Path.GetExtension(percorso)))
            voci.Add((Path.GetFileName(percorso), pk));
    }
    else if (SaveUtil.TryGetSaveFile(percorso, out var sav))
    {
        for (int s = 0; s < sav.SlotCount; s++)
        {
            var pk = sav.GetBoxSlotAtIndex(s);
            if (pk.Species != 0)
                voci.Add(($"box {s / sav.BoxSlotCount + 1} posto {s % sav.BoxSlotCount + 1}", pk));
        }
    }
    else
    {
        Console.Error.WriteLine($"non letto, né cartella né esemplare né salvataggio: {percorso}");
        return 1;
    }

    var esemplari = new JsonArray();
    var conteggi = new SortedDictionary<string, int>(StringComparer.Ordinal);
    foreach (var (origine, pk) in voci)
    {
        if (soloTid is { } t && pk.TID16 != t)
            continue;
        esemplari.Add(new JsonObject
        {
            ["origine"] = origine,
            ["specie"] = pk.Species,
            ["nome"] = pk.Species < nomi.Count ? nomi[pk.Species] : "?",
            ["formato"] = pk.GetType().Name,
            ["allenatore"] = pk.OriginalTrainerName,
            ["tid"] = pk.TID16,
            ["sid"] = pk.SID16,
            ["pid"] = pk.PID,
            ["cromatico"] = pk.IsShiny,
        });
        var chiave = $"{pk.OriginalTrainerName} {pk.TID16} {pk.SID16}";
        conteggi[chiave] = conteggi.GetValueOrDefault(chiave) + 1;
    }
    Console.WriteLine($"{percorso}: {esemplari.Count} esemplari");
    foreach (var (chiave, n) in conteggi)
        Console.WriteLine($"  {n,5}  {chiave}");
    risultato.Add(new JsonObject { ["percorso"] = percorso, ["esemplari"] = esemplari });
}
File.WriteAllText(uscita, new JsonObject { ["formato"] = 1, ["letture"] = risultato }
    .ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
return 0;
