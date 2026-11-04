// Quale esemplare legale raccoglie piu' fiocchi in tutta la sua vita, misurato con il verificatore dei fiocchi della
// libreria. Nasce il 2026-11-04 su richiesta del proprietario, che dall'elenco di PokeOS (159 voci, 106 fiocchi e 53
// emblemi) vuole almeno un Pokemon che possa averli tutti, nel senso gia' discusso: nato legalmente il piu' indietro
// possibile e passato da tutte le generazioni.
//
// Il metodo. Per ogni Pokemon Ombra di Colosseum, dell'e-Reader giapponese e di XD (la sola origine che da' il fiocco
// Nazionale) e per ogni sua evoluzione presente in Scarlatto e Violetto, si costruisce l'esemplare dall'incontro della
// libreria, lo si purifica come fa il gioco quando lo scambia al portatile, lo si porta in avanti fino al formato della
// nona generazione attraverso HOME, e gli si accendono tutti i fiocchi e gli emblemi, con i contatori del Ricordo al
// massimo. Poi si chiede a RibbonVerifier quali non puo' avere e li si spegne, finche' nessuno resta contestato; i
// fiocchi che il verificatore dichiara mancanti si accendono. Quello che resta e' l'insieme massimo che la libreria
// ritiene legale per quella storia. Il controllo riguarda i soli fiocchi: le altre righe del giudizio dipendono da
// campi che questa costruzione non rifinisce, e non entrano nella misura. Il tracciatore di HOME invece si assegna,
// perche' e' da esso che la libreria deduce le visite ai giochi per Switch.
//
// Uso:  dotnet run -c Release -- USCITA.json
using System.Reflection;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

EntityConverter.AllowIncompatibleConversion = EntityCompatibilitySetting.DisallowIncompatible;
var testi = GameInfo.GetStrings("it");
var asm = typeof(PKM).Assembly;
IEnumerable<IEncounterable> Ombre(string tipo, string campo) =>
    ((Array)asm.GetType(tipo)!.GetField(campo, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null)!)
    .Cast<IEncounterable>();
var incontri = Ombre("PKHeX.Core.Encounters3Colo", "Shadow").Select(e => (E: e, G: "Colosseum"))
    .Concat(Ombre("PKHeX.Core.Encounters3Colo", "EReader").Select(e => (E: e, G: "Colosseum, e-Reader giapponese")))
    .Concat(Ombre("PKHeX.Core.Encounters3XD", "Shadow").Select(e => (E: e, G: "XD"))).ToList();
var tr = new SimpleTrainerInfo(GameVersion.CXD) { OT = "Alessio", TID16 = 42317, SID16 = 58164, Language = (int)LanguageID.Italian };

var nomi = typeof(PK9).GetProperties().Where(p => p.Name.StartsWith("Ribbon") && p.PropertyType == typeof(bool) && p.CanWrite)
    .Select(p => p.Name).ToArray();
var voci = new JsonArray();
var visti = new HashSet<(ushort, ushort)>();
foreach (var (enc, gioco) in incontri)
{
    var famiglia = new List<ushort> { enc.Species };
    for (int i = 0; i < famiglia.Count; i++)
        foreach (var x in EvolutionTree.Evolves7.Forward.GetForward(famiglia[i], 0).Span.ToArray())
            if (!famiglia.Contains(x.Species)) famiglia.Add(x.Species);
    foreach (var specie in famiglia.Where(s => PersonalTable.SV.IsPresentInGame(s, 0)))
    {
        if (!visti.Add((enc.Species, specie)))
            continue;
        (List<string>, string)? esito;
        try { esito = Misura(enc, specie); }
        catch (Exception ex) { esito = (new List<string>(), "errore della libreria: " + ex.GetType().Name + ", " + ex.Message); }
        if (esito is null) continue;
        var (fiocchi, motivo) = esito.Value;
        voci.Add(new JsonObject {
            ["ombra"] = testi.specieslist[enc.Species], ["origine"] = gioco, ["livello_ombra"] = enc.LevelMin,
            ["specie"] = testi.specieslist[specie], ["numero"] = specie, ["fiocchi"] = fiocchi.Count,
            ["elenco"] = new JsonArray(fiocchi.Select(f => (JsonNode)f).ToArray()), ["nota"] = motivo });
        Console.WriteLine($"{testi.specieslist[enc.Species],-12} ({gioco}) come {testi.specieslist[specie],-12} {fiocchi.Count} fiocchi {motivo}");
    }
}
var ordinate = voci.OrderByDescending(v => (int)v!["fiocchi"]!).ToArray();
File.WriteAllText(args[0], new JsonObject { ["voci"] = new JsonArray(ordinate.Select(v => v!.DeepClone()).ToArray()) }
    .ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
return 0;

(List<string>, string)? Misura(IEncounterable enc, ushort specie)
{
    var pk = enc.ConvertToPKM(tr);
    PK3 p3 = pk switch { CK3 c => c.ConvertToPK3(), XK3 x => x.ConvertToPK3(), PK3 p => p, _ => throw new InvalidOperationException() };
    p3.RibbonNational = true; // purificato prima dello scambio al portatile, come forza la libreria nella conversione
    // Le evoluzioni che esistono in terza generazione avvengono li'; quelle nate dalla quarta, come Mamoswine o Gallade,
    // dopo la conversione, perche' il formato di terza generazione non le conosce.
    if (specie != p3.Species && specie <= 386)
    {
        p3.Species = specie;
        p3.CurrentLevel = 100;
        p3.Nickname = SpeciesName.GetSpeciesNameGeneration(specie, p3.Language, 3);
    }
    var p7 = EntityConverter.ConvertToType(p3, typeof(PK7), out var r7);
    if (p7 is null) return (new List<string>(), "conversione in settima generazione non riuscita: " + r7);
    if (specie != p7.Species)
    {
        p7.Species = specie;
        p7.CurrentLevel = 100;
        p7.Nickname = SpeciesName.GetSpeciesNameGeneration(specie, p7.Language, 7);
    }
    var p9 = EntityConverter.ConvertToType(PKH.ConvertFromPKM(p7), typeof(PK9), out var r9);
    if (p9 is null) return (new List<string>(), "conversione in nona generazione non riuscita: " + r9);
    // Un esemplare arrivato davvero in HOME porta il tracciatore, ed e' da esso che la libreria deduce le visite ai giochi
    // per Switch: senza, la storia si ferma alla settima generazione e tutti i fiocchi di Switch risultano invalidi.
    if (p9 is IHomeTrack h) h.Tracker = 0x0123456789ABCDEFUL;
    foreach (var n in nomi) p9.GetType().GetProperty(n)!.SetValue(p9, true);
    if (p9 is IRibbonSetMemory6 m) { m.RibbonCountMemoryContest = 40; m.RibbonCountMemoryBattle = 8; }
    for (int giro = 0; giro < 8; giro++)
    {
        var la = new LegalityAnalysis(p9);
        Span<RibbonResult> res = stackalloc RibbonResult[RibbonVerifier.MaxRibbonCount];
        int n = RibbonVerifier.GetRibbonResults(new RibbonVerifierArguments(p9, la.EncounterMatch, la.Info.EvoChainsAllGens), res);
        if (n == 0) break;
        foreach (var x in res[..n])
        {
            var prop = p9.GetType().GetProperty(x.PropertyName);
            if (prop is null) continue;
            if (prop.PropertyType == typeof(bool)) prop.SetValue(p9, x.IsMissing);
            else if (prop.PropertyType == typeof(byte)) prop.SetValue(p9, (byte)0);
        }
    }
    // Gli emblemi da Pranzo a Fiacca si ottengono solo alla cattura in natura nei giochi per Switch, e li controlla
    // MarkVerifier, non RibbonVerifier: senza questa regola resterebbero accesi 47 emblemi impossibili.
    var la0 = new LegalityAnalysis(p9);
    if (p9 is IRibbonIndex ri && !MarkRules.IsEncounterMarkAllowed(la0.EncounterOriginal, p9))
        for (var mk = RibbonIndex.MarkLunchtime; mk <= RibbonIndex.MarkSlump; mk++) ri.SetRibbon((int)mk, false);
    var tenuti = nomi.Where(n => (bool)p9.GetType().GetProperty(n)!.GetValue(p9)!).ToList();
    if (p9 is IRibbonSetMemory6 mm)
    {
        if (mm.RibbonCountMemoryContest > 0) tenuti.Add($"RibbonCountMemoryContest:{mm.RibbonCountMemoryContest}");
        if (mm.RibbonCountMemoryBattle > 0) tenuti.Add($"RibbonCountMemoryBattle:{mm.RibbonCountMemoryBattle}");
    }
    var incontro = new LegalityAnalysis(p9).EncounterMatch;
    return (tenuti, incontro is EncounterInvalid ? "ATTENZIONE: nessun incontro riconosciuto nella nona generazione" : "");
}
