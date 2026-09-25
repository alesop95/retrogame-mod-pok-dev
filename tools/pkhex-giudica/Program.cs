// Giudice del progetto sulla libreria del verificatore, compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Fino al 2026-09-24 il giudizio di conformita' di un lotto era una prova eseguita da una
// persona: si aprivano i file nell'interfaccia di PKHeX e se ne trascriveva l'esito in
// recreate-pokemon-distributions-events/giudizi-esterni.json. Quel registro dice che cosa e' stato visto un
// giorno, ma non dice se i file che stanno oggi sul disco siano quelli visti. La libreria compilata per
// ADR-080 contiene lo stesso LegalityAnalysis dell'interfaccia, quindi il giudizio si puo' ripetere a ogni
// corsa e legare all'impronta del file giudicato.
//
// Che cosa fa. Per ogni file di esemplare nelle cartelle date, riconosciuto dall'estensione (.pk1 ... .pk9,
// .ck3, .xk3, .bk4, .rk4), costruisce l'entita', la giudica fuori da qualunque salvataggio e scrive una voce
// con l'impronta SHA-256, la specie, la forma, l'esito e, se non e' conforme, le righe del rapporto del
// verificatore in inglese.
//
// Il contesto, che va detto perche' cambia l'esito. La libreria giudica alcune regole in funzione del
// salvataggio attivo: senza salvataggio applica quelle della Virtual Console, e rifiuta per esempio le mosse
// degli eventi dell'epoca delle cartucce Game Boy. Il giudice riproduce quindi cio' che l'interfaccia fa
// quando riceve un file all'avvio, cioe' StartupArguments.GetBlank: un salvataggio vuoto del gioco
// predefinito per il contesto dell'esemplare, intestato a chi lo detiene e con la sua lingua, attivato con
// ParseSettings.InitFromSaveFileData. E' la procedura con cui sono stati scritti i giudizi di
// giudizi-esterni.json. Una cartella scritta come CARTELLA=VERSIONE usa invece un salvataggio vuoto di
// quella versione, per esempio lotto=B2 per un lotto di quinta generazione destinato a Nero 2.
//
// Il limite. Un salvataggio vuoto non e' il salvataggio che ricevera' l'esemplare: i controlli che dipendono
// dal gioco reale, come la barriera fra giochi coreani e internazionali di quarta generazione (ADR-040),
// valgono per quel gioco e vanno giudicati con quella versione e quella lingua.
//
// Uso:  dotnet run -c Release -- USCITA.json CARTELLA[=VERSIONE] [CARTELLA[=VERSIONE] ...]
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length < 2)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- USCITA.json CARTELLA[=VERSIONE] [CARTELLA[=VERSIONE] ...]");
    return 2;
}

var estensioni = new HashSet<string>(StringComparer.OrdinalIgnoreCase)
{
    ".pk1", ".pk2", ".pk3", ".pk4", ".pk5", ".pk6", ".pk7", ".pk8", ".pk9",
    ".ck3", ".xk3", ".bk4", ".rk4", ".pb7", ".pb8", ".pa8", ".pa9",
};
var nomiSpecie = GameInfo.GetStrings("en").Species;
// I nomi di luoghi, sfere, giochi e mosse in italiano, per le schede che descrivono gli esemplari.
var testi = GameInfo.GetStrings("it");
var voci = new JsonObject();
int conformi = 0, contestati = 0, illeggibili = 0;

foreach (var argomento in args.Skip(1))
{
    var parti = argomento.Split('=', 2);
    GameVersion? versioneImposta = parti.Length == 2 ? Enum.Parse<GameVersion>(parti[1], true) : null;
    var radice = Path.GetFullPath(parti[0]);
    var nomeCartella = Path.GetFileName(radice.TrimEnd(Path.DirectorySeparatorChar));
    foreach (var percorso in Directory.EnumerateFiles(radice).Order(StringComparer.Ordinal))
    {
        var estensione = Path.GetExtension(percorso);
        if (!estensioni.Contains(estensione))
            continue;
        var byte_ = File.ReadAllBytes(percorso);
        var chiave = nomeCartella + "/" + Path.GetFileName(percorso);
        var voce = new JsonObject { ["sha256"] = Convert.ToHexStringLower(SHA256.HashData(byte_)) };
        if (!FileUtil.TryGetPKM(byte_, out var pk, estensione))
        {
            voce["esito"] = "illeggibile";
            illeggibili++;
            voci[chiave] = voce;
            continue;
        }
        var salvataggio = SalvataggioVuoto(pk, versioneImposta);
        ParseSettings.InitFromSaveFileData(salvataggio);
        var la = new LegalityAnalysis(pk);
        voce["specie"] = pk.Species;
        voce["nome"] = pk.Species < nomiSpecie.Count ? nomiSpecie[pk.Species] : "?";
        voce["forma"] = pk.Form;
        voce["formato"] = pk.GetType().Name;
        voce["contesto"] = $"{salvataggio.Version} {(LanguageID)salvataggio.Language}";
        voce["descrizione"] = new JsonObject
        {
            ["specie_it"] = testi.Species[pk.Species],
            ["livello"] = pk.CurrentLevel,
            ["soprannome"] = pk.IsNicknamed ? pk.Nickname : null,
            ["allenatore"] = pk.OriginalTrainerName,
            ["id_allenatore"] = pk.DisplayTID,
            ["lingua"] = ((LanguageID)pk.Language).ToString(),
            ["gioco_di_origine"] = pk.Version.ToString(),
            ["luogo"] = testi.GetLocationName(false, pk.MetLocation, pk.Format, pk.Generation, pk.Version),
            ["luogo_uovo"] = pk.EggLocation != 0 ? testi.GetLocationName(true, pk.EggLocation, pk.Format, pk.Generation, pk.Version) : null,
            ["sfera"] = pk.Ball < testi.balllist.Length ? testi.balllist[pk.Ball] : pk.Ball.ToString(),
            ["mosse"] = new JsonArray(pk.Moves.Where(m => m != 0).Select(m => (JsonNode)testi.Move[m]).ToArray()),
            ["incontro"] = la.EncounterMatch.LongName,
        };
        voce["esito"] = la.Valid ? "conforme" : "contestato";
        if (la.Valid)
            conformi++;
        else
        {
            contestati++;
            var righe = la.Report("en").Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
            voce["rilievi"] = new JsonArray(righe.Select(r => (JsonNode)r).ToArray());
        }
        voci[chiave] = voce;
    }
}

var uscita = new JsonObject
{
    ["formato"] = 1,
    ["nota"] = "Generato da tools/pkhex-giudica. Giudizio di LegalityAnalysis con un salvataggio vuoto attivo, come l'interfaccia all'avvio: il campo contesto dice quale. Non contiene i controlli che dipendono dal salvataggio reale che ricevera' l'esemplare.",
    ["verificatore"] = new JsonObject
    {
        ["libreria"] = "PKHeX.Core",
        ["versione"] = typeof(LegalityAnalysis).Assembly.GetName().Version?.ToString(),
    },
    ["conteggi"] = new JsonObject { ["conformi"] = conformi, ["contestati"] = contestati, ["illeggibili"] = illeggibili },
    ["voci"] = voci,
};
File.WriteAllText(args[0], uscita.ToJsonString(new JsonSerializerOptions { WriteIndented = true }) + "\n");
Console.WriteLine($"{conformi} conformi, {contestati} contestati, {illeggibili} illeggibili; scritto {args[0]}");
return 0;

// La stessa scelta di StartupArguments.GetBlank nella libreria, con la versione eventualmente imposta.
static SaveFile SalvataggioVuoto(PKM pk, GameVersion? imposta)
{
    var versione = imposta ?? pk.Context.GetSingleGameVersion();
    if (imposta is null && pk is { Format: 1, Japanese: true })
        versione = GameVersion.BU;
    // Il salvataggio attivo e' quello del gioco che contiene l'esemplare, quindi il suo allenatore e' chi lo
    // detiene: l'allenatore originale se l'esemplare non ha cambiato mano, altrimenti l'ultimo detentore. Un
    // dono di sesta generazione ha come allenatore originale la sigla dell'evento e come detentore chi lo ha
    // ricevuto, e un salvataggio vuoto intestato alla sigla fa contestare a ogni dono il detentore.
    var nome = pk is { Format: >= 6, CurrentHandler: 1 } && !string.IsNullOrEmpty(pk.HandlingTrainerName)
        ? pk.HandlingTrainerName : pk.OriginalTrainerName;
    return BlankSaveFile.Get(versione, nome, (LanguageID)pk.Language);
}
