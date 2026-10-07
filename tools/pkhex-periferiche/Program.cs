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
// Due dispositivi non sono periferiche ma incontri statici, raccolti qui perche' la procedura e' la stessa:
// `statico5`, dal 2026-09-30, per gli incontri di Nero e Bianco sbloccati da un oggetto distribuito, e
// `statico7`, dal 2026-10-05, per i doni di Ultrasole e Ultraluna (`EncounterStatic7`), cioe' il Pikachu di
// Ohana e i doni di taglia totem della spiaggia di Ohana. Per `statico7` la voce si sceglie per luogo, forma
// e livello, perche' la spiaggia (luogo 202) consegna specie diverse in forme totem diverse, e l'allenatore
// prende la versione dell'incontro quando questo e' esclusivo di Ultrasole o di Ultraluna.
//
// Il dispositivo `ranger`, dal 2026-10-06 per decisione del proprietario, genera l'uovo di Manaphy che Pokémon Ranger
// consegnava a Diamante e Perla. La libreria non lo tiene fra le carte di MGDB_G4 ma come una carta a parte,
// `EncounterGenerator4.RangerManaphy` (riga 14), che l'enumeratore propone prima delle carte per ogni Manaphy
// (`EncounterPossible4.cs` riga 84) e riconosce con `PGT.IsRangerManaphy`: specie 490, lingua non coreana, luogo
// dell'uovo Ranger4 (3001) o Scambio (2002). L'allenatore è quello del progetto di
// `recreate-pokemon-distributions-events/allenatore.json`, con lo stesso identificativo segreto dei lotti di quarta
// generazione composti da `genera-evento-gen4.py` e `genera-incontro-gen4.py`, e il gioco è Diamante, che è anche il
// gioco che la libreria sceglie da sé quando l'allenatore non è di quarta generazione. L'uovo si giudica, poi si fa
// schiudere nello stesso gioco, come farebbe chi lo riceve: il Trasferimento verso la quinta generazione non accetta
// uova, e un uovo convertito non è più un uovo di Ranger per la libreria, perché `IsRangerManaphy` ammette un uovo solo
// nel formato di quarta generazione. Si scrive l'esemplare schiuso, e il rapporto porta anche l'esito dell'uovo.
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

var progetto = AllenatoreDelProgetto();
ushort tidProgetto = (ushort)(int)progetto["tid"]!, sidProgetto = (ushort)(int)progetto["sid"]!;
byte sessoProgetto = (string)progetto["sesso"]! == "maschio" ? (byte)0 : (byte)1;
SimpleTrainerInfo Allenatore(GameVersion v, byte gen, EntityContext ctx) =>
    new(v) { OT = (string)progetto["nome"]!, TID16 = tidProgetto, SID16 = sidProgetto, Gender = sessoProgetto, Language = (int)progetto["lingua"]!, Generation = gen, Context = ctx };
var giochi = new Dictionary<string, (GameVersion[] Versioni, SimpleTrainerInfo Tr)>
{
    ["pokewalker"] = ([GameVersion.HG, GameVersion.SS], Allenatore(GameVersion.HG, 4, EntityContext.Gen4)),
    ["ranch"] = ([GameVersion.D, GameVersion.P, GameVersion.Pt], Allenatore(GameVersion.Pt, 4, EntityContext.Gen4)),
    ["radar"] = ([GameVersion.B2, GameVersion.W2], Allenatore(GameVersion.B2, 5, EntityContext.Gen5)),
    // Gli incontri sbloccati da un oggetto distribuito, come il Victini del Passo Liberta', dal 2026-09-30.
    ["statico5"] = ([GameVersion.B, GameVersion.W], Allenatore(GameVersion.B, 5, EntityContext.Gen5)),
    // I doni statici di Ultrasole e Ultraluna, dal 2026-10-05: Pikachu di Ohana e doni di taglia totem.
    ["statico7"] = ([GameVersion.US, GameVersion.UM], Allenatore(GameVersion.US, 7, EntityContext.Gen7)),
    // L'uovo di Manaphy di Pokémon Ranger, dal 2026-10-06, con l'allenatore del progetto dei lotti di quarta generazione.
    ["ranger"] = ([GameVersion.D, GameVersion.P], Allenatore(GameVersion.D, 4, EntityContext.Gen4)),
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
        tr = new SimpleTrainerInfo(GameVersion.HG) { OT = "アレシオ", TID16 = tidProgetto, SID16 = sidProgetto, Gender = sessoProgetto, Language = (int)LanguageID.Japanese, Generation = 4, Context = EntityContext.Gen4 };
    PKM modello = dispositivo switch { "radar" or "statico5" => new PK5(), "statico7" => new PK7(), _ => new PK4() };
    modello.Species = specie;
    modello.Language = tr.Language;
    // le forme totem sono forme a se', e la libreria restituisce soltanto le voci della forma del modello
    if (dispositivo == "statico7")
        modello.Form = (byte)(int)r["forma"]!;

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
            "statico7" => enc is EncounterStatic7 st7 && (r["luogo"] is null || st7.Location == (ushort)(int)r["luogo"]!)
                          && st7.Form == (byte)(int)r["forma"]! && (livello is null || st7.Level == livello),
            "ranger" => enc is PGT { IsManaphyEgg: true },
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
    // Un dono esclusivo di una delle due versioni si riceve con l'allenatore di quella versione.
    if (scelto is EncounterStatic7 { Version: GameVersion.US or GameVersion.UM } esclusivo)
        tr = Allenatore(esclusivo.Version, 7, EntityContext.Gen7);
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
        // L'uovo di Ranger si giudica com'è consegnato, e anche convertito alla quinta generazione senza schiuderlo, che
        // è ciò che il Trasferimento non permette; poi si fa schiudere nel gioco che l'ha ricevuto.
        if (dispositivo == "ranger" && pk.IsEgg)
        {
            var laUovo = new LegalityAnalysis(pk);
            esito["uovo"] = new JsonObject
            {
                ["esito"] = laUovo.Valid ? "conforme" : "contestato",
                ["incontro"] = laUovo.EncounterMatch.LongName,
                ["luogo_uovo"] = pk.EggLocation,
                ["convertito_pk5"] = EntityConverter.ConvertToType(pk, typeof(PK5), out _) is { } uovo5
                    ? (new LegalityAnalysis(uovo5).Valid ? "conforme" : "contestato") : "conversione rifiutata",
            };
            pk.ForceHatchPKM(tr);
            // La libreria prende l'amicizia dell'uovo dai cicli di schiusa della specie letta prima di scriverla, cioè della
            // specie 0, e la schiusa la lascia a zero: si scrive il valore che il gioco dà a ogni esemplare appena nato.
            pk.OriginalTrainerFriendship = EggStateLegality.GetEggHatchFriendship(pk.Context);
            pk.RefreshChecksum();
        }
        var la = new LegalityAnalysis(pk);
        analisi = la;
        if (la.Valid && (dispositivo != "ranger" || la.EncounterMatch is PGT { IsManaphyEgg: true })) accettato = pk;
    }
    esito["incontro"] = scelto.LongName;
    if (dispositivo == "ranger" && accettato is not null)
    {
        esito["incontro_riconosciuto"] = analisi!.EncounterMatch.LongName;
        esito["luogo"] = accettato.MetLocation;
        esito["luogo_uovo"] = accettato.EggLocation;
        esito["schiuso"] = !accettato.IsEgg;
    }
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
    esito["forma"] = accettato.Form;
    esito["livello"] = accettato.MetLevel;
    esito["gioco"] = accettato.Version.ToString();
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

// L'allenatore del progetto da recreate-pokemon-distributions-events/allenatore.json, cercato risalendo dalla cartella
// corrente, così che i comandi documentati restino quelli di prima. Fino al 2026-10-07 nome e identificativi erano
// scritti qui a mano, con un identificativo segreto, 5147, senza fonte né motivo, diverso dal 58164 del file (ADR-099).
static JsonNode AllenatoreDelProgetto()
{
    for (var d = new DirectoryInfo(Directory.GetCurrentDirectory()); d != null; d = d.Parent)
    {
        var f = Path.Combine(d.FullName, "recreate-pokemon-distributions-events", "allenatore.json");
        if (File.Exists(f))
            return JsonNode.Parse(File.ReadAllText(f))!;
    }
    throw new FileNotFoundException("allenatore.json non trovato risalendo dalla cartella corrente");
}
