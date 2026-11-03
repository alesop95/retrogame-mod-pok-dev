// Conta i modelli d'incontro non selvatici e non da dono segreto che la libreria del verificatore conosce, per
// generazione e classe: statici, doni, uova, scambi in gioco e Ombre. Nasce il 2026-11-03 per rispondere alla
// condizione del proprietario sugli statici tipici (ADR-106): bastano i posti di HOME? La misura e' un tetto, non
// il numero finale, perche' non toglie i doppioni fra versioni sorelle ne' le voci gia' prodotte come eventi.
// Il primo risultato, con la release 26.10.18: 2718 modelli dalla prima alla settima generazione, 2371 tolti scambi e Ombre.
//
// Uso:  dotnet run -c Release
using System.Reflection;
using PKHeX.Core;
// Conta i modelli d'incontro non selvatici e non da dono segreto che la libreria conosce, per generazione e tipo.
var asm = typeof(PKM).Assembly;
var conti = new SortedDictionary<string, int>();
var visti = new HashSet<object>(ReferenceEqualityComparer.Instance);
foreach (var t in asm.GetTypes().Where(t => t.IsClass && t.Name.StartsWith("Encounters")))
foreach (var f in t.GetFields(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static))
{
    object? v; try { v = f.GetValue(null); } catch { continue; }
    if (v is not Array arr || arr.Length == 0) continue;
    var el = arr.GetType().GetElementType()!;
    if (!typeof(IEncounterTemplate).IsAssignableFrom(el)) continue;
    string tipo = el.Name;
    if (!(tipo.StartsWith("EncounterStatic") || tipo.StartsWith("EncounterGift") || tipo.StartsWith("EncounterTrade") || tipo.StartsWith("EncounterShadow") || tipo.StartsWith("EncounterEgg"))) continue;
    if (!visti.Add(arr)) continue;
    foreach (var o in arr)
    {
        var e = (IEncounterTemplate)o!;
        if (e.Generation is < 1 or > 7) continue;
        string classe = tipo.StartsWith("EncounterTrade") ? "scambio" : tipo.StartsWith("EncounterShadow") ? "ombra" : tipo.StartsWith("EncounterGift") ? "dono" : tipo.StartsWith("EncounterEgg") ? "uovo" : "statico";
        if (classe == "statico" && (o.GetType().GetProperty("FixedBall") is not null) && tipo.Contains("Gift")) classe = "dono";
        var k = $"gen{e.Generation} {classe}";
        conti[k] = conti.GetValueOrDefault(k) + 1;
    }
}
foreach (var (k, n) in conti) Console.WriteLine($"{k}\t{n}");
Console.WriteLine($"totale\t{conti.Values.Sum()}");
