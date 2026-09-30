// Esemplari da periferiche, generati con la libreria del verificatore compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Nella coda del primo tempo, `pokedex-home-completo/CODA-PRIMO-TEMPO.md`, quaranta voci erano
// «censite, non ancora producibili» perche' vengono da una periferica e non da una carta: ventinove dal Pokewalker
// di Oro HeartGold e Argento SoulSilver, otto dagli scambi di Hayley in My Pokemon Ranch, tre dal Dream Radar di
// Nero 2 e Bianco 2. Il progetto non aveva un generatore per queste classi. La libreria le conosce tutte, come
// `EncounterStatic4Pokewalker`, `EncounterTrade4RanchGift` ed `EncounterStatic5Radar`, e per ADR-081 si genera da li'.
//
// Che cosa fa. Legge le richieste scritte in `_notes/lotti/lotto-periferiche/richieste.json` dalla coda e dalla
// checklist. Per ciascuna chiede alla libreria gli incontri della specie nei giochi che ricevono dalla periferica,
// tiene quelli della classe giusta, e per il Pokewalker anche del livello richiesto, perche' la stessa specie compare
// in corsi diversi a livelli diversi. Genera l'esemplare con un allenatore italiano del gioco ricevente, lo giudica,
// e lo scrive come EVT-T-<numero>-<specie>.pkN, con un rapporto JSON. La libreria estrae i numeri casuali da
// Random.Shared, quindi due lanci danno esemplari diversi e ugualmente legali: il risultato sono i file.
//
// Uso:  dotnet run -c Release -- RICHIESTE.json CARTELLA_DI_USCITA
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length != 2)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- RICHIESTE.json CARTELLA_DI_USCITA");
    return 2;
}
var richieste = JsonNode.Parse(File.ReadAllText(args[0]))!["voci"]!.AsArray();
var uscita = Directory.CreateDirectory(args[1]).FullName;

SimpleTrainerInfo Allenatore(GameVersion v, byte gen, EntityContext ctx) =>
    new(v) { OT = "Alessio", TID16 = 42317, SID16 = 5147, Gender = 0, Language = (int)LanguageID.Italian, Generation = gen, Context = ctx };
var giochi = new Dictionary<string, (GameVersion[] Versioni, SimpleTrainerInfo Tr)>
{
    ["pokewalker"] = ([GameVersion.HG, GameVersion.SS], Allenatore(GameVersion.HG, 4, EntityContext.Gen4)),
    ["ranch"] = ([GameVersion.D, GameVersion.P, GameVersion.Pt], Allenatore(GameVersion.Pt, 4, EntityContext.Gen4)),
    ["radar"] = ([GameVersion.B2, GameVersion.W2], Allenatore(GameVersion.B2, 5, EntityContext.Gen5)),
    // Gli incontri sbloccati da un oggetto distribuito, come il Victini del Passo Liberta', dal 2026-09-30.
    ["statico5"] = ([GameVersion.B, GameVersion.W], Allenatore(GameVersion.B, 5, EntityContext.Gen5)),
};

var esiti = new JsonArray();
int conformi = 0, falliti = 0;
foreach (var r in richieste)
{
    var codice = (string)r!["codice"]!;
    var specie = (ushort)(int)r["specie"]!;
    var dispositivo = (string)r["dispositivo"]!;
    byte? livello = r["livello"] is { } l ? (byte)(int)l : null;
    var corso = (string?)r["corso"];
    var (versioni, tr) = giochi[dispositivo];
    // Tre corsi del Pokewalker furono distribuiti solo in Giappone, uno anche in Corea, come annota
    // `PokewalkerCourse4.cs`. La libreria non lo impone, ma un gioco italiano quei corsi non poteva riceverli:
    // l'esemplare si genera con un allenatore giapponese.
    if (corso is "Rally" or "Sightseeing" or "AmityMeadow")
        tr = new SimpleTrainerInfo(GameVersion.HG) { OT = "アレシオ", TID16 = 42317, SID16 = 5147, Gender = 0, Language = (int)LanguageID.Japanese, Generation = 4, Context = EntityContext.Gen4 };
    PKM modello = dispositivo is "radar" or "statico5" ? new PK5() : new PK4();
    modello.Species = specie;
    modello.Language = tr.Language;

    IEncounterable? scelto = null;
    foreach (var enc in EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, versioni))
    {
        bool classe = dispositivo switch
        {
            "pokewalker" => enc is EncounterStatic4Pokewalker w && (livello is null || w.Level == livello)
                            && (corso is null || w.Course.ToString() == corso),
            "ranch" => enc is EncounterTrade4RanchGift,
            "radar" => enc is EncounterStatic5Radar,
            "statico5" => enc is EncounterStatic5 st5 && (r["luogo"] is null || st5.Location == (ushort)(int)r["luogo"]!),
            _ => false,
        };
        if (classe) { scelto = enc; break; }
    }
    // Il censimento puo' non conoscere la forma: lo Shellos del Ranch e' di Mare Est, forma 1, nella libreria
    // (`Encounters4DPPt.cs` riga 130). Se la forma chiesta non c'e', si prende quella della libreria e lo si dichiara.
    if (scelto is null && dispositivo == "ranch")
    {
        foreach (byte f in new byte[] { 1, 2, 3 })
        {
            modello.Form = f;
            scelto = EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, versioni)
                .FirstOrDefault(e => e is EncounterTrade4RanchGift);
            if (scelto is not null) break;
        }
    }
    var esito = new JsonObject { ["codice"] = codice, ["specie"] = specie, ["dispositivo"] = dispositivo };
    if (scelto is null)
    {
        esito["esito"] = "nessuna voce della libreria corrisponde";
        falliti++;
        esiti.Add(esito);
        Console.WriteLine($"{codice} {specie}: nessuna voce della libreria corrisponde");
        continue;
    }
    PKM? accettato = null;
    LegalityAnalysis? analisi = null;
    for (int tentativo = 0; tentativo < 8 && accettato is null; tentativo++)
    {
        var pk = scelto.ConvertToPKM(tr, EncounterCriteria.Unrestricted with { Shiny = Shiny.Never });
        var la = new LegalityAnalysis(pk);
        analisi = la;
        if (la.Valid) accettato = pk;
    }
    esito["incontro"] = scelto.LongName;
    if (scelto.Form != (byte)(int)r["forma"]!)
        esito["forma_della_libreria"] = scelto.Form;
    if (accettato is null)
    {
        esito["esito"] = "generato ma contestato";
        esito["rapporto"] = analisi is null ? "" : analisi.Report();
        falliti++;
        Console.WriteLine($"{codice} {specie}: contestato\n{esito["rapporto"]}");
        esiti.Add(esito);
        continue;
    }
    var dati = new byte[accettato.SIZE_STORED];
    accettato.WriteDecryptedDataStored(dati);
    var nome = $"{codice}-{specie:000}.{accettato.Extension}";
    File.WriteAllBytes(Path.Combine(uscita, nome), dati);
    esito["file"] = nome;
    esito["sha256"] = Convert.ToHexStringLower(SHA256.HashData(dati));
    esito["allenatore"] = accettato.OriginalTrainerName;
    esito["livello"] = accettato.MetLevel;
    esito["esito"] = "conforme";
    conformi++;
    esiti.Add(esito);
    Console.WriteLine($"{codice} {specie}/{accettato.Form}: {scelto.LongName}, allenatore {accettato.OriginalTrainerName}, livello {accettato.MetLevel}, conforme");
}
File.WriteAllText(Path.Combine(uscita, "rapporto.json"),
    new JsonObject { ["fonte"] = "PKHeX.Core tramite tools/pkhex-periferiche (ADR-081)", ["conformi"] = conformi, ["falliti"] = falliti, ["esiti"] = esiti }
        .ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"conformi {conformi}, falliti {falliti}");
return falliti == 0 ? 0 : 1;
