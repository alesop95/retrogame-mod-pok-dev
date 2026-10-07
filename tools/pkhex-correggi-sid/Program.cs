// Corregge il solo identificativo segreto di esemplari in cui non entra nel PID, e li rigiudica, con la libreria del
// verificatore compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perché esiste. ADR-099 del 2026-10-06 porta a 58164 l'identificativo segreto dei 101 esemplari di origine Smeraldo
// del complemento del Rubino, che `tools/manifesto-complemento-rubino.py` aveva generato con SID 0 scritto a mano.
// Quei 101 sono già sulla cartuccia del Rubino, e ADR-082 ammette di correggere solo un difetto concreto e misurato su
// esemplari precisi: rigenerarli darebbe individui nuovi, con PID e valori individuali diversi da quelli scritti.
// Negli incontri di terza generazione il PID e i valori individuali vengono dal generatore pseudocasuale e non dagli
// identificativi, che entrano soltanto nel calcolo della cromaticità; basta quindi cambiare i due byte del SID e
// ricalcolare la somma di controllo. Non vale per il Pokéwalker né per la quinta generazione, dove il PID dipende dal
// SID: per quei lotti ADR-099 ha rigenerato con `tools/pkhex-periferiche`.
//
// Che cosa fa. Legge gli esemplari di CARTELLA, tiene quelli con il TID e il SID dati, imposta il SID nuovo, ricalcola
// la somma di controllo e controlla tre cose: che il PID non sia cambiato, che la cromaticità non sia cambiata, e che
// `LegalityAnalysis` con un salvataggio vuoto della versione data, intestato all'allenatore dell'esemplare, lo giudichi
// conforme. Se una sola delle tre fallisce su un solo esemplare non scrive nulla e lo dice. Altrimenti scrive gli
// esemplari corretti, con lo stesso nome, in USCITA, che deve essere vuota, e un `rapporto.json` con impronta vecchia e
// nuova di ciascuno. L'originale non si modifica mai: la sostituzione nel lotto è un passo a parte, dopo il confronto.
//
// Uso:  dotnet run -c Release -- CARTELLA USCITA --tid N --da SID --a SID --versione VERSIONE
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

string? Opzione(string nome) { var i = Array.IndexOf(args, nome); return i >= 0 && i + 1 < args.Length ? args[i + 1] : null; }
if (args.Length < 2 || Opzione("--tid") is not { } tidTesto || Opzione("--da") is not { } daTesto
    || Opzione("--a") is not { } aTesto || Opzione("--versione") is not { } versioneTesto)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- CARTELLA USCITA --tid N --da SID --a SID --versione VERSIONE");
    return 2;
}
var (cartella, uscita) = (Path.GetFullPath(args[0]), Path.GetFullPath(args[1]));
ushort tid = ushort.Parse(tidTesto), da = ushort.Parse(daTesto), a = ushort.Parse(aTesto);
var versione = Enum.Parse<GameVersion>(versioneTesto, true);
if (Directory.Exists(uscita) && Directory.EnumerateFileSystemEntries(uscita).Any())
{
    Console.Error.WriteLine($"la cartella di uscita non è vuota: {uscita}");
    return 2;
}

var corretti = new List<(string Nome, byte[] Dati, string Prima, string Dopo)>();
var esiti = new JsonArray();
int rifiutati = 0, altri = 0;
foreach (var percorso in Directory.EnumerateFiles(cartella).Order(StringComparer.Ordinal))
{
    var estensione = Path.GetExtension(percorso);
    var byte_ = File.ReadAllBytes(percorso);
    if (!estensione.StartsWith(".pk", StringComparison.OrdinalIgnoreCase) || !FileUtil.TryGetPKM(byte_, out var pk, estensione))
        continue;
    if (pk.TID16 != tid || pk.SID16 != da)
    {
        altri++;
        continue;
    }
    var (pid, cromatico) = (pk.PID, pk.IsShiny);
    // L'esemplare riserializzato prima della correzione deve coincidere con il file: così la sola differenza fra il
    // file vecchio e il nuovo è il SID con la sua somma di controllo, e non un cambio di formato della scrittura.
    var originale = new byte[pk.SIZE_STORED];
    pk.WriteDecryptedDataStored(originale);
    var stessoFormato = originale.AsSpan().SequenceEqual(byte_);
    pk.SID16 = a;
    pk.RefreshChecksum();
    var salvataggio = BlankSaveFile.Get(versione, pk.OriginalTrainerName, (LanguageID)pk.Language);
    ParseSettings.InitFromSaveFileData(salvataggio);
    var la = new LegalityAnalysis(pk);
    var problemi = new List<string>();
    if (!stessoFormato) problemi.Add("il file non è nel formato decifrato da archivio che lo strumento scrive");
    if (pk.PID != pid) problemi.Add("PID cambiato");
    if (pk.IsShiny != cromatico) problemi.Add("cromaticità cambiata");
    if (!la.Valid) problemi.Add("contestato: " + la.Report().ReplaceLineEndings(" "));
    var dati = new byte[pk.SIZE_STORED];
    pk.WriteDecryptedDataStored(dati);
    var nome = Path.GetFileName(percorso);
    var prima = Convert.ToHexStringLower(SHA256.HashData(byte_));
    var dopo = Convert.ToHexStringLower(SHA256.HashData(dati));
    esiti.Add(new JsonObject
    {
        ["file"] = nome, ["specie"] = pk.Species, ["pid"] = pid.ToString("X8"), ["cromatico"] = cromatico,
        ["sha256_prima"] = prima, ["sha256_dopo"] = dopo,
        ["esito"] = problemi.Count == 0 ? "corretto e conforme" : string.Join("; ", problemi),
    });
    if (problemi.Count > 0)
    {
        rifiutati++;
        Console.WriteLine($"{nome}: {string.Join("; ", problemi)}");
        continue;
    }
    corretti.Add((nome, dati, prima, dopo));
}
Console.WriteLine($"{corretti.Count} corretti e conformi, {rifiutati} rifiutati, {altri} con un altro allenatore o identificativo lasciati fuori");
if (rifiutati > 0)
{
    Console.WriteLine("nessun file scritto");
    return 1;
}
Directory.CreateDirectory(uscita);
foreach (var (nome, dati, _, _) in corretti)
    File.WriteAllBytes(Path.Combine(uscita, nome), dati);
var rapporto = new JsonObject
{
    ["fonte"] = "PKHeX.Core tramite tools/pkhex-correggi-sid (ADR-099)",
    ["cartella"] = cartella.Replace('\\', '/'), ["tid"] = tid, ["sid_prima"] = da, ["sid_dopo"] = a,
    ["versione_del_giudizio"] = versione.ToString(), ["corretti"] = corretti.Count, ["esiti"] = esiti,
};
File.WriteAllText(Path.Combine(uscita, "rapporto.json"),
    rapporto.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
Console.WriteLine($"scritti {corretti.Count} file e rapporto.json in {uscita}");
return 0;
