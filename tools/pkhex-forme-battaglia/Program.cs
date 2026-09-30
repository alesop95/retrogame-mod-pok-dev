// Le forme di sola battaglia secondo la libreria del verificatore, compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. La checklist marcava di sola battaglia ogni forma non base di una specie che ne avesse almeno
// una, perche' leggeva dal sorgente i due elenchi di specie `BattleMegas` e `BattleForms` di
// `Legality/Tables/FormInfo.cs`, e non le due espressioni che dentro quelle specie separano le forme di
// battaglia dalle altre. Il 2026-09-29, interrogando `FormInfo.IsBattleOnlyForm` sulle 170 forme cosi' marcate,
// 29 sono risultate depositabili, fra cui il Greninja con Morfosi, che scade con la banca. Quelle espressioni
// sono codice C# e non una tabella, quindi non si leggono in modo affidabile da Python: le valuta la libreria.
//
// Che cosa fa. Per ogni specie del Dex Nazionale e ogni indice di forma da 1 a 31, chiede a `FormInfo.IsBattleOnlyForm` se la forma sia di sola battaglia, e scrive in JSON le coppie
// che lo sono, con il commit del clone da cui la risposta viene.
//
// Uso:  dotnet run -c Release -- USCITA.json
using System.Text.Json;
using PKHeX.Core;

if (args.Length != 1)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- USCITA.json");
    return 2;
}

var coppie = new List<int[]>();
for (ushort s = 1; s <= 1025; s++)
{
    // La regola della libreria e' pura: si interroga su ogni indice di forma possibile, e una forma che non
    // esiste non entra mai nella checklist, che ricava le forme dalle tabelle dei titoli.
    int quante = 32;
    for (byte f = 1; f < quante; f++)
    {
        if (FormInfo.IsBattleOnlyForm(s, f, 9))
            coppie.Add([s, f]);
    }
}

var clone = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, "..", "..", "..", "..", "..", "_notes", "fonti", "cloni", "pkhex"));
string commit = "?";
try
{
    var git = System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo("git", $"-C \"{clone}\" rev-parse --short HEAD") { RedirectStandardOutput = true });
    commit = git!.StandardOutput.ReadToEnd().Trim();
    git.WaitForExit();
}
catch { }

var esito = new Dictionary<string, object>
{
    ["fonte"] = "FormInfo.IsBattleOnlyForm di PKHeX.Core, formato 9, tramite tools/pkhex-forme-battaglia",
    ["commit_clone"] = commit,
    ["indici_di_forma_esaminati"] = "da 1 a 31 per ogni specie",
    ["coppie"] = coppie,
};
File.WriteAllText(args[0], JsonSerializer.Serialize(esito, new JsonSerializerOptions { WriteIndented = false }));
Console.WriteLine($"{coppie.Count} coppie di sola battaglia, clone {commit}");
return 0;
