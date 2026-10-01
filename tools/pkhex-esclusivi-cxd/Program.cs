// Le specie di terza generazione ottenibili soltanto da Colosseum e XD, o soltanto dai giochi portatili, con la
// libreria del verificatore compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il proprietario ha chiesto il 2026-09-22 se esistano specie ottenibili o trasferibili soltanto da
// Colosseum e XD, oppure soltanto verso di essi: e' una domanda di completezza sull'enumerazione delle specie, da porre
// prima di dichiarare chiusa la fascia di terza generazione della catena. La risposta la danno gli incontri della
// libreria, che sono gli stessi con cui si giudica la legalita'.
//
// Che cosa fa. Per ogni specie da 1 a 386 chiede alla libreria gli incontri che la producono, evoluzioni comprese,
// nei giochi portatili (Rubino, Zaffiro, Smeraldo, Rosso Fuoco, Verde Foglia) e in Colosseum e XD, e scrive in JSON le
// specie con incontri da una parte sola, con il nome della classe d'incontro trovata.
//
// Uso:  dotnet run -c Release -- USCITA.json
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

var nomi = GameInfo.GetStrings("it").specieslist;
ParseSettings.AllowEraCartGB = true;
var tr = new SimpleTrainerInfo(GameVersion.E) { OT = "PROVA", Language = (int)LanguageID.English, Generation = 3, Context = EntityContext.Gen3 };
GameVersion[] portatili = [GameVersion.R, GameVersion.S, GameVersion.E, GameVersion.FR, GameVersion.LG];
var soloCxd = new JsonArray(); var soloPortatili = new JsonArray(); var nessuno = new JsonArray();
for (ushort s = 1; s <= 386; s++)
{
    var m = new PK3 { Species = s, Language = (int)LanguageID.English };
    var inPortatili = EncounterMovesetGenerator.GenerateEncounters(m, tr, ReadOnlyMemory<ushort>.Empty, portatili).Select(e => e.GetType().Name).Distinct().ToList();
    var inCxd = EncounterMovesetGenerator.GenerateEncounters(m, tr, ReadOnlyMemory<ushort>.Empty, GameVersion.CXD).Select(e => e.GetType().Name).Distinct().ToList();
    var voce = new JsonObject { ["numero"] = s, ["specie"] = nomi[s] };
    if (inPortatili.Count == 0 && inCxd.Count > 0) { voce["classi_cxd"] = new JsonArray(inCxd.Select(x => (JsonNode)x).ToArray()); soloCxd.Add(voce); }
    else if (inPortatili.Count > 0 && inCxd.Count == 0) soloPortatili.Add(voce);
    else if (inPortatili.Count == 0 && inCxd.Count == 0) nessuno.Add(voce);
}
var esito = new JsonObject { ["fonte"] = "EncounterMovesetGenerator di PKHeX.Core, tramite tools/pkhex-esclusivi-cxd", ["solo_colosseum_xd"] = soloCxd, ["solo_portatili"] = soloPortatili, ["in_nessuno"] = nessuno };
File.WriteAllText(args[0], esito.ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"solo Colosseum e XD {soloCxd.Count}, solo portatili {soloPortatili.Count}, in nessuno {nessuno.Count}");
foreach (var v in soloCxd) Console.WriteLine($"  solo CXD: {v!["numero"]} {v["specie"]} {v["classi_cxd"]!.ToJsonString()}");
foreach (var v in nessuno) Console.WriteLine($"  nessuno: {v!["numero"]} {v["specie"]}");
return 0;
