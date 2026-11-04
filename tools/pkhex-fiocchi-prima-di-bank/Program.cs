// Due misure sui fiocchi, prese dalla libreria del verificatore, chieste dal proprietario il 2026-11-04 perche' si
// aggiungono all'ultimo lotto prima della chiusura di Bank.
//
// La prima: quali specie possono diventare il Fiocco Maestro piu' ricco, cioe' partire da un esemplare Ombra di
// Colosseum o di XD (che dopo la purificazione porta il fiocco Nazionale, ottenibile solo li') e passare da tutti i
// giochi che conferiscono fiocchi, compresi quelli per Switch che accettano solo le specie del proprio Pokedex. Per
// ogni specie Ombra, e per ogni sua evoluzione, si guarda la presenza nelle tabelle personali di Spada e Scudo,
// Diamante Lucente e Perla Splendente, Leggende Arceus e Scarlatto e Violetto.
//
// La seconda: i fiocchi dono, che si ottengono solo dentro le distribuzioni. Per ogni carta della base dei doni
// segreti, dalla quarta alla nona generazione, si leggono i fiocchi che porta, e si costruisce per scelta golosa un
// insieme piccolo di carte che li copre tutti. Le carte di terza generazione non stanno in questa base e i loro
// fiocchi si trattano a parte nel documento.
//
// Uso:  dotnet run -c Release -- USCITA.json
using System.Reflection;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

var testi = GameInfo.GetStrings("it");
var asm = typeof(PKM).Assembly;
IEnumerable<IEncounterTemplate> Ombre(string tipo, string campo) =>
    ((Array)asm.GetType(tipo)!.GetField(campo, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null)!)
    .Cast<IEncounterTemplate>();
var ombre = Ombre("PKHeX.Core.Encounters3Colo", "Shadow").Select(e => (e.Species, Gioco: "Colosseum"))
    .Concat(Ombre("PKHeX.Core.Encounters3Colo", "EReader").Select(e => (e.Species, Gioco: "Colosseum, e-Reader giapponese")))
    .Concat(Ombre("PKHeX.Core.Encounters3XD", "Shadow").Select(e => (e.Species, Gioco: "XD"))).Distinct().ToList();

var giochi = new (string Nome, IPersonalTable T)[] {
    ("Spada e Scudo", PersonalTable.SWSH), ("Diamante Lucente e Perla Splendente", PersonalTable.BDSP),
    ("Leggende Arceus", PersonalTable.LA), ("Scarlatto e Violetto", PersonalTable.SV) };
var evo = EvolutionTree.Evolves8;
var maestri = new JsonArray();
foreach (var (sp, gioco) in ombre.OrderBy(o => o.Species))
{
    // La specie Ombra e tutte le sue evoluzioni possibili, ricavate dalla rete della settima generazione.
    var famiglia = new List<ushort> { sp };
    for (int i = 0; i < famiglia.Count; i++)
        foreach (var (s, _) in EvolutionTree.Evolves7.Forward.GetForward(famiglia[i], 0).Span.ToArray().Select(x => (x.Species, x.Form)))
            if (!famiglia.Contains(s)) famiglia.Add(s);
    foreach (var s in famiglia)
    {
        var assenti = giochi.Where(g => !g.T.IsPresentInGame(s, 0)).Select(g => (JsonNode)g.Nome).ToArray();
        maestri.Add(new JsonObject { ["ombra"] = testi.specieslist[sp], ["origine"] = gioco, ["specie"] = testi.specieslist[s],
            ["numero"] = s, ["giochi_switch_assenti"] = new JsonArray(assenti) });
    }
}

// I fiocchi dono e le carte che li portano.
string[] nomi = ["RibbonClassic", "RibbonWishing", "RibbonPremier", "RibbonEvent", "RibbonBirthday", "RibbonSpecial",
    "RibbonChampionWorld", "RibbonSouvenir", "RibbonChampionBattle", "RibbonChampionRegional", "RibbonChampionNational",
    "RibbonCountry", "RibbonWorld", "RibbonEarth", "RibbonNational"];
var carte = new List<(MysteryGift G, HashSet<string> R)>();
IEnumerable<MysteryGift> tutte = EncounterEvent.MGDB_G4.Cast<MysteryGift>().Concat(EncounterEvent.MGDB_G5).Concat(EncounterEvent.MGDB_G6)
    .Concat(EncounterEvent.MGDB_G7).Concat(EncounterEvent.MGDB_G8).Concat(EncounterEvent.MGDB_G8B).Concat(EncounterEvent.MGDB_G9);
foreach (var g in tutte)
{
    if (!g.IsEntity) continue;
    object o = g is PCD pcd ? pcd.Gift.PK : g;
    var r = nomi.Where(n => o.GetType().GetProperty(n) is { } p && p.PropertyType == typeof(bool) && (bool)p.GetValue(o)!).ToHashSet();
    if (r.Count > 0) carte.Add((g, r));
}
var perFiocco = new JsonObject();
foreach (var n in nomi)
    perFiocco[n] = carte.Count(c => c.R.Contains(n));
// Copertura golosa: a ogni passo la carta che aggiunge piu' fiocchi non ancora coperti; a parita', la generazione
// piu' bassa, perche' una carta piu' vecchia passa da piu' giochi con fiocchi.
var restano = carte.SelectMany(c => c.R).ToHashSet();
var scelte = new JsonArray();
while (restano.Count > 0)
{
    var best = carte.OrderByDescending(c => c.R.Count(restano.Contains)).ThenByDescending(c => c.G.CardID > 0 && c.G.CardTitle.Trim().Length > 0).ThenBy(c => c.G.Generation).ThenBy(c => c.G.CardID).First();
    var nuovi = best.R.Where(restano.Contains).ToList();
    scelte.Add(new JsonObject { ["generazione"] = best.G.Generation, ["carta"] = best.G.CardID, ["titolo"] = best.G.CardTitle.Trim(),
        ["specie"] = testi.specieslist[best.G.Species], ["fiocchi_nuovi"] = new JsonArray(nuovi.Select(x => (JsonNode)x).ToArray()),
        ["fiocchi_tutti"] = new JsonArray(best.R.Select(x => (JsonNode)x).ToArray()) });
    restano.ExceptWith(nuovi);
}
File.WriteAllText(args[0], new JsonObject { ["maestri"] = maestri, ["carte_per_fiocco"] = perFiocco, ["copertura_dono"] = scelte }
    .ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"specie Ombra: {ombre.Select(o => o.Species).Distinct().Count()}, voci di famiglia: {maestri.Count}, carte con fiocchi dono: {carte.Count}, carte nella copertura: {scelte.Count}");
return 0;
