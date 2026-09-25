// La rigenerazione di un lotto dall'incontro che la libreria vi riconosce, sulla libreria del verificatore
// compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Gli scambi in gioco di quarta e quinta generazione, prodotti il 2026-09-15 da generatori
// scritti a mano, sono stati contestati per intero al primo giudizio del 2026-09-24: il soprannome era scritto
// tutto in maiuscolo, «SPARVY» invece di «Sparvy», e quattro esemplari avevano una sfera fuori intervallo per
// HeartGold e SoulSilver. La libreria riconosce comunque l'incontro di ciascun file, quindi sa costruirne uno
// corretto: per ADR-081 e' lei a farlo.
//
// Che cosa fa. Per ogni file della cartella di origine chiede a LegalityAnalysis l'incontro riconosciuto, e se
// l'incontro sa costruire un esemplare lo ricostruisce per un salvataggio vuoto della stessa versione,
// intestato all'allenatore e alla lingua dati. Giudica il risultato nello stesso contesto e lo scrive con lo
// stesso nome nella cartella di destinazione, che non deve contenere file di esemplare, con un manifesto.
//
// Uso:  dotnet run -c Release -- ORIGINE DESTINAZIONE ALLENATORE LINGUA
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length != 4)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- ORIGINE DESTINAZIONE ALLENATORE LINGUA");
    return 2;
}
var destinazione = Directory.CreateDirectory(args[1]).FullName;
if (Directory.EnumerateFiles(destinazione, "*.pk?").Any())
{
    Console.Error.WriteLine($"rifiuto: {destinazione} contiene gia' file di esemplare");
    return 1;
}
var lingua = Enum.Parse<LanguageID>(args[3], true);
var voci = new JsonObject();
int conformi = 0, contestati = 0, saltati = 0;
foreach (var percorso in Directory.EnumerateFiles(Path.GetFullPath(args[0])).Order(StringComparer.Ordinal))
{
    var nome = Path.GetFileName(percorso);
    if (!FileUtil.TryGetPKM(File.ReadAllBytes(percorso), out var vecchio, Path.GetExtension(percorso)))
        continue;
    var versione = vecchio.Version;
    var salvataggio = BlankSaveFile.Get(versione, args[2], lingua);
    ParseSettings.InitFromSaveFileData(salvataggio);
    IEncounterable incontro = new LegalityAnalysis(vecchio).EncounterMatch;
    // Se il file e' troppo diverso dall'originale perche' la libreria vi riconosca un incontro, si cerca fra
    // gli incontri che la libreria conosce per quella specie e quella versione uno scambio in gioco, che e'
    // la sola classe di cui questo strumento si occupa oggi.
    if (incontro is EncounterInvalid)
        incontro = EncounterMovesetGenerator.GenerateEncounters(vecchio, salvataggio, ReadOnlyMemory<ushort>.Empty, versione)
            .FirstOrDefault(e => e.GetType().Name.Contains("Trade") && e.Species == vecchio.Species) ?? incontro;
    var voce = new JsonObject { ["da"] = nome, ["incontro"] = incontro.LongName, ["versione"] = versione.ToString() };
    if (incontro is EncounterInvalid || incontro is not IEncounterConvertible convertibile)
    {
        voce["esito"] = "incontro non ricostruibile";
        saltati++;
        voci[nome] = voce;
        continue;
    }
    var pk = convertibile.ConvertToPKM(salvataggio);
    // HeartGold e SoulSilver scrivono, alla creazione di un esemplare, la sfera anche nel campo esteso che solo
    // loro usano; la conversione della libreria lo lascia a zero, e il verificatore della stessa libreria
    // (MiscVerifierG4.IsValidBallHGSS) pretende che sia uguale alla sfera normale. Lo si scrive come il gioco.
    if (pk is G4PKM g4 && g4.HGSS && g4.BallHGSS == 0)
        g4.BallHGSS = g4.BallDPPt;
    var la = new LegalityAnalysis(pk);
    var dati = new byte[pk.SIZE_STORED];
    pk.WriteDecryptedDataStored(dati);
    File.WriteAllBytes(Path.Combine(destinazione, nome), dati);
    voce["soprannome"] = pk.Nickname;
    voce["allenatore_originale"] = pk.OriginalTrainerName;
    voce["sha256"] = Convert.ToHexStringLower(SHA256.HashData(dati));
    voce["esito"] = la.Valid ? "conforme" : "contestato";
    if (la.Valid) conformi++;
    else
    {
        contestati++;
        voce["rilievi"] = new JsonArray(la.Report("en").Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(r => (JsonNode)r).ToArray());
    }
    voci[nome] = voce;
}
var manifesto = new JsonObject
{
    ["fonte"] = "incontro riconosciuto da LegalityAnalysis e ricostruito con ConvertToPKM della libreria PKHeX.Core, tramite tools/pkhex-rigenera",
    ["origine"] = args[0].Replace('\\', '/'),
    ["allenatore"] = args[2],
    ["lingua"] = lingua.ToString(),
    ["conteggi"] = new JsonObject { ["conformi"] = conformi, ["contestati"] = contestati, ["non_ricostruibili"] = saltati },
    ["voci"] = voci,
};
File.WriteAllText(Path.Combine(destinazione, "manifesto.json"), manifesto.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
Console.WriteLine($"{conformi} conformi, {contestati} contestati, {saltati} non ricostruibili; scritto {destinazione}");
return 0;
