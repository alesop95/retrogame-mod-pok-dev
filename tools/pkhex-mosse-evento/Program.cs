// Divide gli esemplari dell'epoca delle cartucce Game Boy fra chi porta una mossa che la Console Virtuale non
// ammette e chi no, e prova per ciascuno la versione senza quella mossa.
//
// Perché esiste. Il gruppo FINALE (121 doni di evento delle cartucce, ADR-109 e la decisione finale del
// proprietario) aspettava una divisione chiesta dalla comunità il 2026-10-06: passa ciò che non ha mosse
// speciali, e un esemplare con una mossa speciale passa solo cancellandola. Il giudizio in contesto di Console
// Virtuale di tools/pkhex-giudica dice che 119 dei 121 hanno una mossa non valida, ma non quale, né se
// l'esemplare torna conforme senza.
//
// Che cosa fa. Per ogni file elencato nel JSON di ingresso (chiavi relative alla cartella _notes/lotti, come
// lotto-gb/EVT-1-0009-Mew.pk1) costruisce l'esemplare, lo giudica con un salvataggio vuoto del suo gioco e con
// l'epoca delle cartucce esclusa, come fa pkhex-giudica con =VC, e annota le mosse non valide. Poi toglie quelle
// mosse, compatta le restanti; se non ne resta nessuna mette la mossa che la libreria suggerisce per l'incontro;
// ripristina i PP e rigiudica. La versione senza mossa si scrive nella cartella di uscita con lo stesso nome del
// file, perchè resti riconoscibile accanto all'originale, che non si tocca.
//
// Uso:  dotnet run -c Release -- ELENCO.json RADICE_LOTTI USCITA.json CARTELLA_VARIANTI
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length < 4)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- ELENCO.json RADICE_LOTTI USCITA.json CARTELLA_VARIANTI");
    return 2;
}
var elenco = JsonSerializer.Deserialize<List<string>>(File.ReadAllText(args[0]))!;
var radice = Path.GetFullPath(args[1]);
Directory.CreateDirectory(args[3]);
var testi = GameInfo.GetStrings("it");
var voci = new JsonArray();
int senzaProblemi = 0, conformiDopo = 0, ancoraNo = 0;

foreach (var chiave in elenco)
{
    var percorso = Path.Combine(radice, chiave.Replace('/', Path.DirectorySeparatorChar));
    var dati = File.ReadAllBytes(percorso);
    if (!FileUtil.TryGetPKM(dati, out var pk, Path.GetExtension(percorso)))
    {
        voci.Add(new JsonObject { ["chiave"] = chiave, ["esito"] = "illeggibile" });
        continue;
    }
    var la = Giudica(pk);
    var nonValide = new List<int>();
    for (int i = 0; i < la.Info.Moves.Length; i++)
        if (pk.GetMove(i) != 0 && !la.Info.Moves[i].Valid)
            nonValide.Add(i);
    var voce = new JsonObject
    {
        ["chiave"] = chiave,
        ["specie"] = testi.Species[pk.Species],
        ["allenatore"] = pk.OriginalTrainerName,
        ["id"] = pk.DisplayTID,
        ["livello"] = pk.CurrentLevel,
        ["mosse"] = Nomi(pk),
        ["mosse_non_valide"] = new JsonArray(nonValide.Select(i => (JsonNode)testi.Move[pk.GetMove(i)]).ToArray()),
        ["conforme_prima"] = la.Valid,
        ["rilievi_prima"] = Rilievi(la),
    };
    if (nonValide.Count == 0)
    {
        voce["classe"] = "senza mossa speciale";
        senzaProblemi++;
        voci.Add(voce);
        continue;
    }
    var copia = pk.Clone();
    foreach (var i in nonValide)
        copia.SetMove(i, 0);
    copia.FixMoves();
    if (copia.Moves.All(m => m == 0))
    {
        Span<ushort> suggerite = stackalloc ushort[4];
        Giudica(copia).GetSuggestedCurrentMoves(suggerite, MoveSourceType.Encounter);
        copia.SetMoves(suggerite);
    }
    copia.HealPP();
    copia.RefreshChecksum();
    var dopo = Giudica(copia);
    voce["classe"] = "con mossa speciale";
    voce["mosse_dopo"] = Nomi(copia);
    voce["conforme_dopo"] = dopo.Valid;
    voce["rilievi_dopo"] = Rilievi(dopo);
    if (dopo.Valid) conformiDopo++; else ancoraNo++;
    var scritti = new byte[copia.SIZE_STORED];
    copia.WriteDecryptedDataStored(scritti);
    File.WriteAllBytes(Path.Combine(args[3], Path.GetFileName(percorso)), scritti);
    voci.Add(voce);
}

var uscita = new JsonObject
{
    ["nota"] = "Generato da tools/pkhex-mosse-evento: giudizio in contesto di Console Virtuale (epoca delle cartucce esclusa), mosse non valide e versione senza di esse.",
    ["libreria"] = typeof(LegalityAnalysis).Assembly.GetName().Version?.ToString(),
    ["conteggi"] = new JsonObject { ["senza_mossa_speciale"] = senzaProblemi, ["conformi_senza_la_mossa"] = conformiDopo, ["non_conformi_anche_senza"] = ancoraNo },
    ["voci"] = voci,
};
File.WriteAllText(args[2], uscita.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
Console.WriteLine($"senza mossa speciale {senzaProblemi}; con mossa speciale: conformi senza la mossa {conformiDopo}, non conformi anche senza {ancoraNo}");
return 0;

LegalityAnalysis Giudica(PKM e)
{
    var versione = e.Context.GetSingleGameVersion();
    if (e is { Format: 1, Japanese: true })
        versione = GameVersion.BU;
    ParseSettings.InitFromSaveFileData(BlankSaveFile.Get(versione, e.OriginalTrainerName, (LanguageID)e.Language));
    ParseSettings.AllowEraCartGB = false;
    return new LegalityAnalysis(e);
}

JsonArray Nomi(PKM e) => new(e.Moves.Where(m => m != 0).Select(m => (JsonNode)testi.Move[m]).ToArray());

JsonArray Rilievi(LegalityAnalysis a) => a.Valid ? new JsonArray()
    : new(a.Report("en").Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(r => (JsonNode)r).ToArray());
