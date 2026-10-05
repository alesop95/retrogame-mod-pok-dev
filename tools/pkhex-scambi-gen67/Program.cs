// Scambi in gioco di sesta e settima generazione, generati con la libreria del verificatore compilata dal clone in
// _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il proprietario ha deciso il 2026-10-05 che gli scambi in gioco di X e Y, Rubino Omega e Zaffiro
// Alpha, Sole e Luna, Ultrasole e Ultraluna entrino nella collezione: quegli esemplari arrivano al deposito soltanto
// attraverso la banca, che chiude il 2027-02-26, e portano allenatore e soprannome altrui, quindi non si ottengono da
// una cattura propria. Il censimento `pokedex-home-completo/CENSIMENTO-SCAMBI.md` li elenca dalle stesse tabelle; per
// ADR-081 gli esemplari si generano dalla libreria invece di scriverli a mano. Gli scambi di Let's Go restano fuori,
// perche' quei giochi si collegano al deposito senza passare dalla banca.
//
// Che cosa fa. Legge le quattro tabelle di scambio della libreria, `Encounters6XY.TradeGift_XY`,
// `Encounters6AO.TradeGift_AO`, `Encounters7SM.TradeGift_SM` e `Encounters7USUM.TradeGift_USUM`, che sono interne
// e si raggiungono per riflessione. Per ogni voce genera un esemplare con `ConvertToPKM` e un allenatore italiano
// della prima versione del gruppo della voce (o della sola versione, se la voce e' esclusiva), mai cromatico, e lo
// giudica con un salvataggio vuoto di quella versione intestato all'allenatore che lo riceve, come fa
// `tools/pkhex-giudica`. Se la tabella non porta i nomi in italiano usa la lingua predefinita della libreria. Scrive
// soltanto i conformi, come SCB-<gen>-<gruppo>-<nn>-<numero>.pkN, e un rapporto.json con gioco, specie, forma,
// soprannome, allenatore, identificativo, esito e impronta SHA-256. I numeri casuali vengono da Random.Shared,
// quindi due lanci danno esemplari diversi e ugualmente legali: il risultato sono i file.
//
// Uso:  dotnet run -c Release -- CARTELLA_DI_USCITA
using System.Reflection;
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length != 1)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- CARTELLA_DI_USCITA");
    return 2;
}
var uscita = Directory.CreateDirectory(args[0]).FullName;
if (Directory.EnumerateFiles(uscita).Any(f => f.EndsWith(".pk6") || f.EndsWith(".pk7")))
{
    Console.Error.WriteLine("la cartella di uscita contiene gia' esemplari: spostarli prima");
    return 2;
}
var nomiEn = GameInfo.GetStrings("en").Species;
var nomiIt = GameInfo.GetStrings("it").Species;
var libreria = typeof(LegalityAnalysis).Assembly;

IEncounterable[] Tabella(string classe, string campo)
{
    var f = libreria.GetType("PKHeX.Core." + classe)?.GetField(campo, BindingFlags.NonPublic | BindingFlags.Public | BindingFlags.Static)
        ?? throw new InvalidOperationException($"tabella {classe}.{campo} non trovata nella libreria");
    return ((Array)f.GetValue(null)!).Cast<IEncounterable>().ToArray();
}

// Gruppo, generazione, versione predefinita del gruppo, tabella.
var tabelle = new (string Gruppo, byte Gen, GameVersion Predefinita, IEncounterable[] Voci)[]
{
    ("XY", 6, GameVersion.X, Tabella("Encounters6XY", "TradeGift_XY")),
    ("AO", 6, GameVersion.OR, Tabella("Encounters6AO", "TradeGift_AO")),
    ("SM", 7, GameVersion.SN, Tabella("Encounters7SM", "TradeGift_SM")),
    ("USUM", 7, GameVersion.US, Tabella("Encounters7USUM", "TradeGift_USUM")),
};

SimpleTrainerInfo Allenatore(GameVersion v, byte gen, LanguageID lingua) =>
    new(v) { OT = "Alessio", TID16 = 42317, SID16 = 5147, Gender = 0, Language = (int)lingua, Generation = gen, Context = gen == 6 ? EntityContext.Gen6 : EntityContext.Gen7 };

var esiti = new JsonArray();
int conformi = 0, contestati = 0;
foreach (var (gruppo, gen, predefinita, voci) in tabelle)
{
    for (int i = 0; i < voci.Length; i++)
    {
        var enc = voci[i];
        // Una voce esclusiva di una versione porta quella versione; una voce comune porta il gruppo.
        var versione = enc.Version is GameVersion.X or GameVersion.Y or GameVersion.OR or GameVersion.AS
            or GameVersion.SN or GameVersion.MN or GameVersion.US or GameVersion.UM ? enc.Version : predefinita;
        var lingua = LanguageID.Italian;
        var prova = (PKM)((IEncounterConvertible)enc).ConvertToPKM(Allenatore(versione, gen, lingua));
        if (string.IsNullOrWhiteSpace(prova.OriginalTrainerName) || (prova.IsNicknamed && string.IsNullOrWhiteSpace(prova.Nickname)))
            lingua = (LanguageID)prova.Language == LanguageID.Italian ? LanguageID.English : (LanguageID)prova.Language;
        var tr = Allenatore(versione, gen, lingua);
        var salvataggio = BlankSaveFile.Get(versione, tr.OT, lingua);
        ParseSettings.InitFromSaveFileData(salvataggio);

        PKM? accettato = null;
        PKM ultimo = prova;
        LegalityAnalysis? analisi = null;
        for (int tentativo = 0; tentativo < 8 && accettato is null; tentativo++)
        {
            var pk = (PKM)((IEncounterConvertible)enc).ConvertToPKM(tr, EncounterCriteria.Unrestricted with { Shiny = Shiny.Never });
            ultimo = pk;
            analisi = new LegalityAnalysis(pk);
            if (analisi.Valid && !pk.IsShiny) accettato = pk;
        }
        var pkm = accettato ?? ultimo;
        var esito = new JsonObject
        {
            ["gioco"] = pkm.Version.ToString(),
            ["tabella"] = $"TradeGift_{gruppo}",
            ["indice"] = i,
            // Due voci di settima generazione evolvono durante lo scambio (Graveler di Alola, Phantump): la specie
            // consegnata e' quella dell'esemplare, la specie della tabella resta accanto.
            ["specie_della_tabella"] = enc.Species,
            ["specie"] = pkm.Species,
            ["nome_en"] = nomiEn[pkm.Species],
            ["nome_it"] = nomiIt[pkm.Species],
            ["forma"] = pkm.Form,
            ["livello"] = pkm.MetLevel,
            ["soprannome"] = pkm.Nickname,
            ["allenatore"] = pkm.OriginalTrainerName,
            ["tid"] = pkm.DisplayTID,
            ["lingua"] = ((LanguageID)pkm.Language).ToString(),
            ["contesto_di_giudizio"] = $"{salvataggio.Version} {(LanguageID)salvataggio.Language}",
        };
        if (accettato is null)
        {
            esito["esito"] = "contestato";
            esito["rilievi"] = new JsonArray((analisi?.Report("en") ?? "").Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(r => (JsonNode)r).ToArray());
            contestati++;
            Console.WriteLine($"{gruppo} {i:00} {nomiEn[pkm.Species]}: contestato\n{analisi?.Report("en")}");
            esiti.Add(esito);
            continue;
        }
        var dati = new byte[accettato.SIZE_STORED];
        accettato.WriteDecryptedDataStored(dati);
        var nome = $"SCB-{gen}-{gruppo}-{i + 1:00}-{accettato.Species:000}.{accettato.Extension}";
        File.WriteAllBytes(Path.Combine(uscita, nome), dati);
        esito["file"] = nome;
        esito["esito"] = "conforme";
        esito["sha256"] = Convert.ToHexStringLower(SHA256.HashData(dati));
        conformi++;
        esiti.Add(esito);
        Console.WriteLine($"{nome}: {accettato.Nickname} di {accettato.OriginalTrainerName} ({accettato.DisplayTID}), {(LanguageID)accettato.Language}, conforme");
    }
}
File.WriteAllText(Path.Combine(uscita, "rapporto.json"),
    new JsonObject
    {
        ["fonte"] = "PKHeX.Core tramite tools/pkhex-scambi-gen67 (ADR-081), tabelle TradeGift_XY, TradeGift_AO, TradeGift_SM, TradeGift_USUM",
        ["versione_libreria"] = libreria.GetName().Version?.ToString(),
        ["conformi"] = conformi,
        ["contestati"] = contestati,
        ["esiti"] = esiti,
    }.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
Console.WriteLine($"conformi {conformi}, contestati {contestati}");
return contestati == 0 ? 0 : 1;
