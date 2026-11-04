// Le caselle di specie e forma che esistono nei giochi fino alla settima generazione, cioe' quelle che i lotti
// devono gia' coprire prima della chiusura di Bank (direttiva del proprietario, ribadita il 2026-11-03): la Switch
// serve solo per cio' che in quei giochi non esiste. La fonte e' la libreria del verificatore, non un elenco a mano:
// per ogni specie da 1 a 809 e ogni forma si guarda in quali tabelle personali dei giochi fino a Ultrasole e Ultraluna
// la coppia e' presente. Si escludono le forme che HOME non puo' depositare: quelle da sola battaglia, quelle fuse e
// quelle totem, che il deposito riporta alla forma base.
//
// Uso:  dotnet run -c Release -- USCITA.json
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

var tabelle = new (string Nome, IPersonalTable T)[] {
    ("USUM", PersonalTable.USUM), ("SM", PersonalTable.SM), ("AO", PersonalTable.AO), ("XY", PersonalTable.XY),
    ("B2W2", PersonalTable.B2W2), ("BW", PersonalTable.BW), ("HGSS", PersonalTable.HGSS), ("Pt", PersonalTable.Pt),
    ("DP", PersonalTable.DP), ("E", PersonalTable.E), ("FR", PersonalTable.FR), ("LG", PersonalTable.LG),
    ("RS", PersonalTable.RS), ("C", PersonalTable.C), ("GS", PersonalTable.GS), ("Y", PersonalTable.Y), ("RB", PersonalTable.RB) };
var testi = GameInfo.GetStrings("it");
var voci = new JsonArray();
for (ushort s = 1; s <= 809; s++)
{
    var forme = FormConverter.GetFormList(s, testi.Types, testi.forms, GameInfo.GenderSymbolASCII, EntityContext.Gen7);
    int n = Math.Max(1, forme.Length);
    for (byte f = 0; f < n; f++)
    {
        var giochi = tabelle.Where(t => t.T.IsPresentInGame(s, f)).Select(t => t.Nome).ToList();
        if (giochi.Count == 0) continue;
        if (FormInfo.IsBattleOnlyForm(s, f, 7) || FormInfo.IsFusedForm(s, f, 7) || FormInfo.IsTotemForm(s, f, EntityContext.Gen7)) continue;
        voci.Add(new JsonObject { ["numero"] = s, ["forma_n"] = f, ["specie"] = testi.specieslist[s],
            ["forma"] = f < forme.Length ? forme[f] : "", ["giochi"] = new JsonArray(giochi.Select(g => (JsonNode)g).ToArray()) });
    }
}
File.WriteAllText(args[0], voci.ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"caselle di specie e forma fino alla settima generazione: {voci.Count}");
