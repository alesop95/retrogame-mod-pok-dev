using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

// La modalita' descrittiva: per ciascuna richiesta scrive i campi della carta come la libreria li legge,
// senza generare esemplari su disco. Serve alle schede delle voci, che devono dire da dove viene un dono e
// che cosa lo rende quello e non un altro, e che non possono ricavarlo dal solo titolo della carta. Per le
// carte con un uovo prova anche la conversione nel salvataggio dato e riporta le date che ne escono,
// perche' e' la' che la libreria contesta le uova del 2026-09-24.
static class Descrivi
{
    static readonly string[] Proprieta =
    [
        "CardID", "CardTitle", "OriginalTrainerName", "TID16", "SID16", "Level", "IsEgg", "Ball", "HeldItem",
        "Location", "EggLocation", "Nature", "AbilityType", "PIDType", "RestrictLanguage", "RestrictVersion",
        "Language", "IsShiny", "Date", "Day", "Month", "Year",
    ];

    public static int Esegui(string richieste, string uscita, string salvataggio6, string salvataggio7)
    {
        var salvataggi = new Dictionary<int, SaveFile>();
        foreach (var (gen, percorso) in new[] { (6, salvataggio6), (7, salvataggio7) })
            if (SaveUtil.TryGetSaveFile(percorso, out var s))
                salvataggi[gen] = s;
        var strings = GameInfo.GetStrings("it");
        var basi = new Dictionary<int, MysteryGift[]>
        {
            [6] = EncounterEvent.MGDB_G6.Where(g => g.IsEntity && g.Species != 0).ToArray<MysteryGift>(),
            [7] = EncounterEvent.MGDB_G7.Where(g => g.IsEntity && g.Species != 0).ToArray<MysteryGift>(),
        };
        var fuori = new JsonObject();
        foreach (var r in JsonNode.Parse(File.ReadAllText(richieste))!["voci"]!.AsArray())
        {
            var codice = (string)r!["codice"]!;
            int gen = (int)r["generazione"]!, ordinale = (int)r["ordinale"]!;
            var carta = basi[gen][ordinale];
            var voce = new JsonObject { ["specie"] = carta.Species, ["nome_specie"] = strings.Species[carta.Species] };
            foreach (var nome in Proprieta)
            {
                var p = carta.GetType().GetProperty(nome);
                if (p is null) continue;
                try { voce[nome] = p.GetValue(carta)?.ToString(); } catch { }
            }
            voce["mosse"] = new JsonArray(new[] { carta.Moves.Move1, carta.Moves.Move2, carta.Moves.Move3, carta.Moves.Move4 }.Where(m => m != 0).Select(m => (JsonNode)strings.Move[m]).ToArray());
            if (carta.IsEgg && salvataggi.TryGetValue(gen, out var sav))
            {
                ParseSettings.InitFromSaveFileData(sav);
                var pk = carta.ConvertToPKM(sav);
                var la = new LegalityAnalysis(pk);
                voce["prova_uovo"] = new JsonObject
                {
                    ["data_incontro"] = pk.MetDate?.ToString("yyyy-MM-dd"),
                    ["data_uovo"] = pk.EggMetDate?.ToString("yyyy-MM-dd"),
                    ["luogo_uovo"] = pk.EggLocation,
                    ["luogo"] = pk.MetLocation,
                    ["e_uovo"] = pk.IsEgg,
                    ["esito"] = la.Valid ? "conforme" : "contestato",
                };
            }
            fuori[codice] = voce;
        }
        File.WriteAllText(uscita, fuori.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
        Console.WriteLine($"descritte {fuori.Count} carte; scritto {uscita}");
        return 0;
    }
}
