// Gli esemplari per le sfide della scheda Pokemon dell'app di HOME che si chiudono con i giochi del 3DS, cioe' prima
// della chiusura di Bank: sfere, condizioni di gara e lucentezza al massimo, Ditto. Nasce il 2026-11-26 per il giro 17
// di ADR-142, dai contatori letti nelle schermate del proprietario (pokedex-home-completo/data/sfide-home-app-*.json).
//
// Il conto. Per ogni sfida si produce la differenza fra la soglia del livello d'oro e il contatore dell'app. Un esemplare
// conta per tutte le sfide che soddisfa, quindi le tre famiglie si sovrappongono invece di sommarsi:
//   condizioni  i dieci esemplari con le cinque condizioni e la lucentezza a 255 stanno in sfere di terza generazione
//               che hanno ancora un bisogno, e chiudono insieme le sei sfide di gara;
//   Ditto       stanno nelle sfere che hanno il bisogno piu' alto, e chiudono la sfida dei 30 Ditto;
//   sfere       il resto, una specie diversa per esemplare finche' ce ne sono.
//
// Le origini, scelte dalla libreria e non a mano. La lucentezza si accumula soltanto con i Pokemelle di terza
// generazione e i Poffin di quarta: Rubino Omega e Zaffiro Alpha danno condizioni ma non lucentezza
// (`ContestStatVerifier.cs`, `ContestStatInfo.GetContestStatRestriction`: origine 5 e 6 NoSheen, origine 3 e 4 Mixed
// dopo la sesta generazione). Gli esemplari delle condizioni sono quindi catture di Smeraldo. Le sfere: le catture
// selvatiche di Ultrasole e Ultraluna ammettono tutte le sfere di HeartGold e SoulSilver piu' la UC Ball
// (`BallUseLegality.cs`, WildPokeballs7), ma non la Gara Ball, che si ottiene soltanto dalla Gara Pigliamosche di
// HeartGold e SoulSilver: quelle sono catture della gara. Ogni esemplare e' mai cromatico, ha l'allenatore del progetto
// (recreate-pokemon-distributions-events/allenatore.json, ADR-099) ed e' accettato soltanto se LegalityAnalysis lo
// giudica conforme; quelli di terza generazione si giudicano anche convertiti alla settima, che e' cio' che la copia
// per HOME conterra'.
//
// Riproducibilita'. La libreria estrae i numeri casuali da Random.Shared: due lanci danno esemplari diversi e
// ugualmente legali. Il risultato sono i file, e il rapporto porta l'impronta SHA-256 di ciascuno.
//
// Uso:  pkhex-sfide-app SFIDE.json CARTELLA_DI_USCITA
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Text.RegularExpressions;
using PKHeX.Core;

if (args.Length != 2)
{
    Console.Error.WriteLine("uso: pkhex-sfide-app SFIDE.json CARTELLA_DI_USCITA");
    return 2;
}
var sfide = JsonNode.Parse(File.ReadAllText(args[0]))!["sfide"]!.AsArray();
var uscita = Directory.CreateDirectory(args[1]).FullName;
if (Directory.EnumerateFiles(uscita).Any())
{
    Console.Error.WriteLine("la cartella di uscita non e' vuota: " + uscita);
    return 2;
}

var progetto = AllenatoreDelProgetto();
ushort tidProgetto = (ushort)(int)progetto["tid"]!, sidProgetto = (ushort)(int)progetto["sid"]!;
byte sessoProgetto = (string)progetto["sesso"]! == "maschio" ? (byte)0 : (byte)1;
SimpleTrainerInfo Allenatore(GameVersion v, byte gen, EntityContext ctx) =>
    new(v) { OT = (string)progetto["nome"]!, TID16 = tidProgetto, SID16 = sidProgetto, Gender = sessoProgetto, Language = (int)progetto["lingua"]!, Generation = gen, Context = ctx };
var trE = Allenatore(GameVersion.E, 3, EntityContext.Gen3);
var trUS = Allenatore(GameVersion.US, 7, EntityContext.Gen7);
var trUM = Allenatore(GameVersion.UM, 7, EntityContext.Gen7);
var trHG = Allenatore(GameVersion.HG, 4, EntityContext.Gen4);
var trSS = Allenatore(GameVersion.SS, 4, EntityContext.Gen4);
var it = GameInfo.GetStrings("it");
var en = GameInfo.GetStrings("en");
var criteri = EncounterCriteria.Unrestricted with { Shiny = Shiny.Never };

// I bisogni, dalle sfide.
var bisogno = new Dictionary<Ball, int>();
var sfidaDellaSfera = new Dictionary<Ball, string>();
var sfideDiGara = new List<string>();
int gara = 0, ditto = 0;
string sfidaDitto = "";
foreach (var s in sfide)
{
    var testo = (string)s!["sfida"]!;
    int soglia = (int)s["soglia"]!;
    int? app = s["app"] is null ? null : (int)s["app"]!;
    if (s["sfera"] is not null)
    {
        var m = Regex.Match(testo, @"in an? (\w+) Ball");
        var b = Enum.Parse<Ball>(m.Groups[1].Value);
        bisogno[b] = Math.Max(0, soglia - app!.Value);
        sfidaDellaSfera[b] = testo;
    }
    else if (s["condizione"] is not null)
    {
        gara = Math.Max(gara, soglia - (app ?? 0));
        sfideDiGara.Add(testo);
    }
    else if ((int?)s["specie"] == (int)Species.Ditto)
    {
        ditto = Math.Max(0, soglia - (app ?? (int)s["nelle_copie"]!));
        sfidaDitto = testo;
    }
}
int bisognoSfere = bisogno.Values.Sum();
Console.WriteLine($"sfere: {bisogno.Count} sfide, {bisognoSfere} esemplari; condizioni: {gara}; Ditto: {ditto}");

// Il piano: condizioni, poi Ditto, poi il resto delle sfere.
var sfereGen3 = new[] { Ball.Dive, Ball.Luxury, Ball.Timer, Ball.Net, Ball.Premier, Ball.Repeat, Ball.Nest };
var resto = new Dictionary<Ball, int>(bisogno);
Ball Prendi(IEnumerable<Ball> ammesse, Ball riserva)
{
    var scelta = ammesse.Where(b => resto.GetValueOrDefault(b) > 0).OrderByDescending(b => resto[b]).ThenBy(b => (int)b).ToList();
    if (scelta.Count == 0) return riserva;
    resto[scelta[0]]--;
    return scelta[0];
}
var piano = new List<(string Tipo, Ball Sfera)>();
for (int i = 0; i < gara; i++) piano.Add(("condizioni", Prendi(sfereGen3, Ball.Luxury)));
for (int i = 0; i < ditto; i++) piano.Add(("ditto", Prendi(bisogno.Keys.Where(b => b != Ball.Sport), Ball.Poke)));
foreach (var (b, n) in resto.OrderBy(x => (int)x.Key))
    for (int i = 0; i < n; i++) piano.Add(("sfera", b));

// Le voci selvatiche di Ultrasole e Ultraluna, una per specie, e quelle di HeartGold e SoulSilver per la Gara Ball.
PKM Modello(ushort specie, int lingua) { var m = new PK7 { Species = specie, Form = 0, Language = lingua }; return m; }
// Ultraluna prima di Ultrasole, perche' la copia per HOME e' di Ultraluna; Ultrasole resta per le sue esclusive.
IEncounterable? Selvatico7(ushort specie) => EncounterMovesetGenerator
    .GenerateEncounters(Modello(specie, trUM.Language), trUM, ReadOnlyMemory<ushort>.Empty, GameVersion.UM, GameVersion.US)
    .FirstOrDefault(e => e.GetType().Name.StartsWith("EncounterSlot7") && e.Species == specie && e.Form == 0);
IEncounterable? Selvatico3(ushort specie) => EncounterMovesetGenerator
    .GenerateEncounters(Modello(specie, trE.Language), trE, ReadOnlyMemory<ushort>.Empty, GameVersion.E)
    .FirstOrDefault(e => e.GetType().Name.StartsWith("EncounterSlot3") && e.Species == specie && e.Form == 0);
IEnumerable<IEncounterable> Gara4(ushort specie) => EncounterMovesetGenerator
    .GenerateEncounters(Modello(specie, trHG.Language), trHG, ReadOnlyMemory<ushort>.Empty, GameVersion.HG, GameVersion.SS)
    .Where(e => e.GetType().Name.StartsWith("EncounterSlot4") && e.Species == specie);

SimpleTrainerInfo AllenatoreDi(IEncounterable e) => e.Version switch
{
    GameVersion.UM => trUM, GameVersion.US => trUS, GameVersion.SS => trSS, GameVersion.HG => trHG, _ => e.Generation == 7 ? trUS : e.Generation == 4 ? trHG : trE,
};

PKM? Produci(IEncounterable enc, Ball sfera, bool condizioni, out string motivo)
{
    motivo = "";
    for (int tentativo = 0; tentativo < 12; tentativo++)
    {
        var pk = enc.ConvertToPKM(AllenatoreDi(enc), criteri);
        if (pk.IsShiny) continue;
        pk.Ball = (byte)sfera;
        // Una cattura di HeartGold e SoulSilver avviene prima del Poke Transfer di ADR-128 (dal 2011-03-04): il giorno sta
        // fra l'uscita europea di HeartGold e SoulSilver, il 2010-03-26, e il 2011-03-03, scelto dal PID. Con la data di
        // oggi lo strumento di scrittura non potrebbe dargli un giorno di Poke Transfer, che viene dopo la cattura.
        if (pk.Format == 4)
        {
            var inizio = new DateOnly(2010, 3, 26);
            var ampiezza = new DateOnly(2011, 3, 3).DayNumber - inizio.DayNumber + 1;
            pk.MetDate = inizio.AddDays((int)(pk.PID % (uint)ampiezza));
        }
        if (condizioni && pk is IContestStats cs)
        {
            cs.ContestCool = cs.ContestBeauty = cs.ContestCute = cs.ContestSmart = cs.ContestTough = 255;
            cs.ContestSheen = 255;
        }
        pk.RefreshChecksum();
        var la = new LegalityAnalysis(pk);
        if (!la.Valid) { motivo = la.Report(); continue; }
        if (pk.Format < 7)
        {
            var pk7 = EntityConverter.ConvertToType(pk, typeof(PK7), out var esitoConv);
            if (pk7 is null) { motivo = "conversione alla settima generazione rifiutata: " + esitoConv; continue; }
            var la7 = new LegalityAnalysis(pk7);
            if (!la7.Valid) { motivo = "contestato dopo la conversione alla settima generazione: " + la7.Report(); continue; }
        }
        return pk;
    }
    return null;
}

var usate = new HashSet<ushort>();
var volte = new Dictionary<ushort, int>();
var esiti = new JsonArray();
int numero = 0, falliti = 0;
string Luogo(PKM pk) => it.GetLocationName(false, pk.MetLocation, pk.Format, pk.Generation, pk.Version);
string Gioco(GameVersion v) => v switch
{
    GameVersion.E => "Smeraldo", GameVersion.US => "Ultrasole", GameVersion.UM => "Ultraluna",
    GameVersion.HG => "HeartGold", GameVersion.SS => "SoulSilver", _ => v.ToString(),
};

void Scrivi(PKM pk, IEncounterable enc, string tipo, Ball sfera, List<string> conta)
{
    numero++;
    var dati = new byte[pk.SIZE_STORED];
    pk.WriteDecryptedDataStored(dati);
    var nome = $"{numero:0000}-{en.Species[pk.Species]}-{sfera}.{pk.Extension}";
    File.WriteAllBytes(Path.Combine(uscita, nome), dati);
    usate.Add(pk.Species);
    volte[pk.Species] = volte.GetValueOrDefault(pk.Species) + 1;
    var sferaIt = it.balllist[(int)sfera];
    string storia = tipo switch
    {
        "condizioni" => $"Catturato in {Gioco(pk.Version)} ({Luogo(pk)}) con una {sferaIt}, nutrito di Pokemelle fino alla lucentezza massima e poi, in Rubino Omega, fino al massimo di tutte e cinque le condizioni.",
        "ditto" => $"Catturato in {Gioco(pk.Version)} ({Luogo(pk)}) con una {sferaIt}, per la sfida dei 30 Ditto e per quella della {sferaIt}.",
        _ when sfera == Ball.Sport => $"Catturato con la {sferaIt} alla Gara Pigliamosche di {Gioco(pk.Version)} ({Luogo(pk)}).",
        _ => $"Catturato in {Gioco(pk.Version)} ({Luogo(pk)}) con una {sferaIt}.",
    };
    esiti.Add(new JsonObject
    {
        ["file"] = nome, ["tipo"] = tipo, ["specie"] = (int)pk.Species, ["nome"] = it.Species[pk.Species],
        ["sfera"] = sfera.ToString(), ["sfera_it"] = sferaIt, ["gioco"] = pk.Version.ToString(), ["livello"] = pk.CurrentLevel,
        ["incontro"] = enc.LongName, ["luogo"] = Luogo(pk), ["pid"] = pk.PID.ToString("X8"),
        ["sha256"] = Convert.ToHexStringLower(SHA256.HashData(dati)), ["storia"] = storia,
        ["sfide"] = new JsonArray(conta.Select(c => (JsonNode)c).ToArray()),
    });
}

// Condizioni: catture di Smeraldo, specie diverse, prima quelle con una storia di gara.
ushort[] preferite3 = [349, 300, 327, 333, 311, 312, 278, 270, 273, 263, 276, 280, 298, 183, 285, 296, 303, 307, 309, 315, 318, 320, 322, 325, 331, 335, 337, 338, 339, 341];
var codaGara = new Queue<ushort>(preferite3);
foreach (var (tipo, sfera) in piano.Where(p => p.Tipo == "condizioni"))
{
    PKM? fatto = null; IEncounterable? enc = null; string motivo = "";
    while (fatto is null && codaGara.Count > 0)
    {
        var s = codaGara.Dequeue();
        enc = Selvatico3(s);
        if (enc is null) continue;
        fatto = Produci(enc, sfera, true, out motivo);
        if (fatto is null) Console.WriteLine($"condizioni {en.Species[s]} {sfera}: {motivo.Split('\n').FirstOrDefault()}");
    }
    if (fatto is null) { falliti++; Console.WriteLine($"condizioni {sfera}: nessuna specie accettata"); continue; }
    var conta = new List<string>(sfideDiGara);
    if (sfidaDellaSfera.TryGetValue(sfera, out var t)) conta.Add(t);
    Scrivi(fatto, enc!, tipo, sfera, conta);
}

// Ditto: Monte Hokulani in Ultrasole e Ultraluna.
var encDitto = Selvatico7((ushort)Species.Ditto);
foreach (var (tipo, sfera) in piano.Where(p => p.Tipo == "ditto"))
{
    var fatto = encDitto is null ? null : Produci(encDitto, sfera, false, out var motivo);
    if (fatto is null) { falliti++; Console.WriteLine($"Ditto {sfera}: non accettato"); continue; }
    var conta = new List<string> { sfidaDitto };
    if (sfidaDellaSfera.TryGetValue(sfera, out var t)) conta.Add(t);
    Scrivi(fatto, encDitto!, tipo, sfera, conta);
}

// Sfere: una specie diversa per esemplare, in ordine di numero di Pokedex, finche' ce ne sono; poi le specie gia' usate
// meno volte, cosi' che le ripetizioni si distribuiscano invece di cadere tutte sulla prima specie.
var selvatici7 = new List<(ushort Specie, IEncounterable Enc)>();
for (ushort s = 1; s <= 807; s++)
{
    if (s == (ushort)Species.Ditto) continue;
    var e = Selvatico7(s);
    if (e is not null) selvatici7.Add((s, e));
}
Console.WriteLine($"specie con una voce selvatica in Ultrasole e Ultraluna: {selvatici7.Count}");
var gara4 = new List<(ushort Specie, IEncounterable Enc)>();
foreach (var (tipo, sfera) in piano.Where(p => p.Tipo == "sfera"))
{
    PKM? fatto = null; IEncounterable? enc = null;
    if (sfera == Ball.Sport)
    {
        if (gara4.Count == 0)
            for (ushort s = 1; s <= 493; s++)
                foreach (var e in Gara4(s))
                    if (Produci(e, Ball.Sport, false, out _) is not null) { gara4.Add((s, e)); break; }
        var ordine = gara4.OrderBy(x => volte.GetValueOrDefault(x.Specie)).ThenBy(x => x.Specie).ToList();
        foreach (var (s, e) in ordine)
        {
            fatto = Produci(e, sfera, false, out _);
            if (fatto is not null) { enc = e; break; }
        }
    }
    else
    {
        var ordine = selvatici7.OrderBy(x => volte.GetValueOrDefault(x.Specie)).ThenBy(x => x.Specie);
        foreach (var (s, e) in ordine)
        {
            fatto = Produci(e, sfera, false, out _);
            if (fatto is not null) { enc = e; break; }
        }
    }
    if (fatto is null) { falliti++; Console.WriteLine($"sfera {sfera}: nessuna specie accettata"); continue; }
    Scrivi(fatto, enc!, tipo, sfera, new List<string> { sfidaDellaSfera[sfera] });
}

var rapporto = new JsonObject
{
    ["strumento"] = "tools/pkhex-sfide-app",
    ["sfide"] = Path.GetFileName(args[0]),
    ["bisogni"] = new JsonObject
    {
        ["sfere"] = new JsonObject(bisogno.OrderBy(x => (int)x.Key).Select(x => KeyValuePair.Create(x.Key.ToString(), (JsonNode?)x.Value))),
        ["condizioni_e_lucentezza"] = gara, ["ditto"] = ditto,
    },
    ["prodotti"] = numero, ["falliti"] = falliti,
    ["per_tipo"] = new JsonObject(esiti.GroupBy(e => (string)e!["tipo"]!).Select(g => KeyValuePair.Create(g.Key, (JsonNode?)g.Count()))),
    ["specie_diverse"] = usate.Count,
    ["voci"] = esiti,
};
File.WriteAllText(Path.Combine(uscita, "..", "rapporto.json"), rapporto.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }));
Console.WriteLine($"prodotti {numero} (atteso {bisognoSfere}), falliti {falliti}, specie diverse {usate.Count}");
return falliti == 0 ? 0 : 1;

// L'allenatore del progetto da recreate-pokemon-distributions-events/allenatore.json, cercato risalendo dalla cartella
// corrente, come in tools/pkhex-periferiche (ADR-099).
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
