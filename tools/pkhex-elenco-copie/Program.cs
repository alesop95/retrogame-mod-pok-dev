// Elenca i box delle copie dei salvataggi per HOME, per il catalogo stampabile della collezione, con la libreria del
// verificatore compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il proprietario vuole, a lotti completi, un PDF stampabile di tutta la collezione. Il registro dei
// giudizi descrive i file dei lotti, non gli esemplari come stanno nelle copie: nelle copie le uova sono schiuse e il
// detentore e' l'allenatore del salvataggio. Il catalogo si costruisce quindi leggendo le copie, che sono cio' che
// arriva in HOME, e il legame con il lotto e con il codice della checklist viene dal rapporto accanto a ciascuna.
//
// Che cosa fa. Per ogni copia data come GRUPPO=PERCORSO legge i box, e per ogni esemplare scrive in JSON box, posto,
// specie e forma in italiano, livello, sesso, cromatico, allenatore originale e identificativo, lingua, gioco d'origine,
// luogo d'incontro, sfera e giudizio nel contesto del salvataggio, piu' l'origine presa dal rapporto.
// `tools/stampa-collezione.py` ne fa il documento.
//
// Uso:  dotnet run -c Release -- USCITA.json GRUPPO=PERCORSO [GRUPPO=PERCORSO ...]
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length < 2)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- USCITA.json GRUPPO=PERCORSO [GRUPPO=PERCORSO ...]");
    return 2;
}
var testi = GameInfo.GetStrings("it");
var inglese = GameInfo.GetStrings("en");
var copie = new JsonArray();
foreach (var arg in args.Skip(1))
{
    var parti = arg.Split('=', 2);
    var (gruppo, percorso) = (parti[0], parti[1]);
    if (!SaveUtil.TryGetSaveFile(percorso, out var sav))
    {
        Console.Error.WriteLine($"salvataggio non letto: {percorso}");
        return 1;
    }
    ParseSettings.InitFromSaveFileData(sav);
    // L'origine di ciascun posto dal rapporto scritto da tools/pkhex-scrivi-salvataggio.
    var origini = new Dictionary<(int, int), string>();
    var rapporto = percorso + ".rapporto.json";
    if (File.Exists(rapporto))
        foreach (var v in JsonNode.Parse(File.ReadAllText(rapporto))!["voci"]!.AsArray())
            origini[((int)v!["box"]!, (int)v["posto"]!)] = (string)v["origine"]!;
    var voci = new JsonArray();
    for (int i = 0; i < sav.SlotCount; i++)
    {
        var pk = sav.GetBoxSlotAtIndex(i);
        if (pk.Species == 0)
            continue;
        int box = i / sav.BoxSlotCount + 1, posto = i % sav.BoxSlotCount + 1;
        var forme = FormConverter.GetFormList(pk.Species, testi.Types, testi.forms, GameInfo.GenderSymbolASCII, pk.Context);
        var formeEn = FormConverter.GetFormList(pk.Species, inglese.Types, inglese.forms, GameInfo.GenderSymbolASCII, pk.Context);
        // L'evento come lo riconosce la libreria: il titolo e il numero della carta per un dono segreto, altrimenti il nome
        // dell'incontro. Dal 2026-10-01, per il catalogo, che il proprietario vuole ordinato per tipo di evento.
        var la = new LegalityAnalysis(pk);
        var enc = la.EncounterMatch;
        string evento = enc is MysteryGift mg && mg.CardID > 0
            ? $"{mg.CardTitle.Replace('　', ' ').Trim()} (carta {mg.CardID})"
            : enc.LongName;
        voci.Add(new JsonObject
        {
            ["box"] = box, ["posto"] = posto,
            ["specie"] = testi.specieslist[pk.Species], ["numero"] = pk.Species,
            ["forma"] = pk.Form > 0 && pk.Form < forme.Length ? forme[pk.Form] : "",
            ["livello"] = pk.CurrentLevel, ["sesso"] = pk.Gender switch { 0 => "M", 1 => "F", _ => "" },
            ["cromatico"] = pk.IsShiny,
            ["allenatore"] = pk.OriginalTrainerName, ["id"] = pk.DisplayTID,
            ["lingua"] = ((LanguageID)pk.Language).ToString(),
            ["gioco"] = pk.Version.ToString(),
            ["luogo"] = testi.GetLocationName(false, pk.MetLocation, pk.Format, pk.Generation, pk.Version),
            ["sfera"] = testi.balllist[pk.Ball],
            ["conforme"] = la.Valid,
            ["forma_en"] = pk.Form > 0 && pk.Form < formeEn.Length ? formeEn[pk.Form] : "",
            ["generazione"] = pk.Generation,
            ["evento"] = evento,
            ["origine"] = origini.TryGetValue((box, posto), out var o) ? o : "",
        });
    }
    copie.Add(new JsonObject { ["gruppo"] = gruppo, ["copia"] = percorso, ["gioco"] = sav.Version.ToString(), ["esemplari"] = voci });
    Console.WriteLine($"{gruppo}: {voci.Count} esemplari");
}
File.WriteAllText(args[0], new JsonObject { ["copie"] = copie }.ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
return 0;
