// Il passaggio del Parco Amici sulla libreria del verificatore, compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il lotto del 2026-09-16 era prodotto dalla sintesi in Python di pokebridge/parco_amici.py e
// il 2026-09-24, al primo giudizio, aveva 148 esemplari contestati su 203; gli stessi esemplari di terza
// generazione convertiti con PK3.ConvertToPK4() della libreria erano 203 conformi su 203. Per ADR-082 il
// lotto si genera con la libreria, come ADR-081 aveva gia' deciso per la generazione.
//
// Che cosa fa. Legge in sola lettura le cartelle di terza generazione ricevute, che sono i lotti gia'
// giudicati conformi; esclude, senza correggerle, le voci che conoscono una macchina nascosta di terza
// generazione, perche' il Parco Amici le rifiuta e togliere la mossa e' una decisione del proprietario; fa
// schiudere in terza generazione le uova, come farebbe il gioco prima del passaggio; converte con
// ConvertToPK4; giudica il risultato nel contesto di un salvataggio vuoto di SoulSilver con la lingua
// dell'esemplare, come fa tools/pkhex-giudica; e scrive il .pk4 in chiaro da 136 byte con lo stesso nome
// del file di origine, piu' un manifesto con impronta ed esito di ogni voce. Non scrive in una cartella
// che contenga gia' file di esemplare, cosi' che un lotto precedente non venga sovrascritto per errore.
//
// Riproducibilita'. La conversione e la schiusa sono deterministiche tranne la data di incontro, che la
// libreria prende dall'orologio: due corse in giorni diversi danno file diversi e ugualmente conformi, e il
// manifesto porta l'impronta di ciascuno.
//
// Uso:  dotnet run -c Release -- DESTINAZIONE ORIGINE [ORIGINE ...]
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length < 2)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- DESTINAZIONE ORIGINE [ORIGINE ...]");
    return 2;
}
var destinazione = Directory.CreateDirectory(args[0]).FullName;
if (Directory.EnumerateFiles(destinazione, "*.pk4").Any())
{
    Console.Error.WriteLine($"rifiuto: {destinazione} contiene gia' file .pk4; spostare prima il lotto precedente");
    return 1;
}

// Le macchine nascoste di terza generazione, per numero di mossa: le stesse di MN_TERZA in
// tools/checklist-pokedex.py.
var macchineNascoste = new Dictionary<ushort, string>
{
    [15] = "Taglio", [19] = "Volo", [57] = "Surf", [70] = "Forza",
    [127] = "Cascata", [148] = "Flash", [249] = "Spaccaroccia", [291] = "Sub",
};

var voci = new JsonObject();
var escluse = new JsonArray();
var errori = new JsonArray();
int conformi = 0, contestati = 0;
var radiceProgetto = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, "..", "..", "..", "..", ".."));

foreach (var origine in args.Skip(1))
{
    var cartella = Path.GetFullPath(origine);
    var relativa = Path.GetRelativePath(radiceProgetto, cartella).Replace('\\', '/');
    foreach (var percorso in Directory.EnumerateFiles(cartella, "*.pk3").Order(StringComparer.Ordinal))
    {
        var nome = Path.GetFileName(percorso);
        try
        {
            var pk3 = new PK3(File.ReadAllBytes(percorso));
            var mn = pk3.Moves.Where(macchineNascoste.ContainsKey).Select(m => macchineNascoste[m]).ToArray();
            if (mn.Length > 0)
            {
                escluse.Add(new JsonObject { ["file"] = nome, ["cartella"] = relativa, ["mossa"] = string.Join(", ", mn) });
                continue;
            }
            var daUovo = pk3.IsEgg;
            if (daUovo)
            {
                var allenatore = BlankSaveFile.Get(GameVersion.E, pk3.OriginalTrainerName, (LanguageID)pk3.Language);
                pk3.ForceHatchPKM(allenatore);
            }
            var pk4 = pk3.ConvertToPK4();
            var salvataggio = BlankSaveFile.Get(GameVersion.SS, pk4.OriginalTrainerName, (LanguageID)pk4.Language);
            ParseSettings.InitFromSaveFileData(salvataggio);
            var la = new LegalityAnalysis(pk4);

            var dati = new byte[pk4.SIZE_STORED];
            pk4.WriteDecryptedDataStored(dati);
            var nomeUscita = Path.ChangeExtension(nome, ".pk4");
            File.WriteAllBytes(Path.Combine(destinazione, nomeUscita), dati);

            var voce = new JsonObject
            {
                ["da"] = nome,
                ["cartella_origine"] = relativa,
                ["da_uovo"] = daUovo,
                ["specie"] = pk4.Species,
                ["luogo"] = pk4.MetLocation,
                ["sha256"] = Convert.ToHexStringLower(SHA256.HashData(dati)),
                ["esito"] = la.Valid ? "conforme" : "contestato",
            };
            if (la.Valid)
                conformi++;
            else
            {
                contestati++;
                var righe = la.Report("en").Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
                voce["rilievi"] = new JsonArray(righe.Select(r => (JsonNode)r).ToArray());
            }
            voci[nomeUscita] = voce;
        }
        catch (Exception e)
        {
            errori.Add(new JsonObject { ["file"] = nome, ["cartella"] = relativa, ["errore"] = e.Message });
        }
    }
}

var manifesto = new JsonObject
{
    ["fonte"] = "PK3.ConvertToPK4 della libreria PKHeX.Core compilata dal clone in _notes/fonti/cloni/pkhex, tramite tools/pkhex-parco-amici (ADR-082)",
    ["stato"] = contestati == 0 && errori.Count == 0
        ? "prodotto e giudicato conforme con la libreria, contesto SoulSilver vuoto con la lingua dell'esemplare"
        : "prodotto, con esemplari contestati: vedere le voci",
    ["conteggi"] = new JsonObject { ["conformi"] = conformi, ["contestati"] = contestati, ["escluse"] = escluse.Count, ["errori"] = errori.Count },
    ["errori"] = errori,
    ["escluse_macchina_nascosta"] = escluse,
    ["voci"] = voci,
};
File.WriteAllText(Path.Combine(destinazione, "manifesto.json"),
    manifesto.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
Console.WriteLine($"{conformi} conformi, {contestati} contestati, {escluse.Count} escluse per macchina nascosta, {errori.Count} errori; scritto {destinazione}");
return contestati == 0 && errori.Count == 0 ? 0 : 1;
