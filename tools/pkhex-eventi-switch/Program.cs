// Gli eventi dei giochi per Switch, tutti, generati dai doni e dai raid di distribuzione della libreria del verificatore,
// compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il proprietario ha stabilito il 2026-10-01 che i lotti degli eventi vanno completi fino alla nona
// generazione, in base alle fonti e non per parti: un evento scaduto resta da avere legittimo, perche' HOME non ha la
// scadenza della banca e una console modificata potra' un giorno iniettarlo. La fonte e' la base degli eventi della
// libreria, cioe' le carte ufficiali dei doni (WB7 per Let's Go, WC8 per Spada e Scudo, WB8 per Diamante Lucente e Perla
// Splendente, WA8 per Leggende Arceus, WC9 per Scarlatto e Violetto, WA9 per Leggende Z-A) e gli incontri di
// distribuzione (tane di Spada e Scudo, raid Teracristal, raid a sette stelle, focolai di distribuzione).
//
// Che cosa fa. Per ogni carta che porta un Pokemon prova i giochi della sua famiglia nell'ordine dato, costruisce
// l'esemplare con l'allenatore del progetto, letto da recreate-pokemon-distributions-events/allenatore.json, che vale
// soltanto per i campi che la carta lasciava a chi riceveva, lo giudica, e tiene il primo esito conforme. Per gli
// incontri di distribuzione percorre specie e forme di Spada, Scudo, Scarlatto e Violetto e genera ogni incontro distinto
// di quelle classi. Scrive i conformi nella cartella data e un rapporto JSON con ogni voce, conforme o no, con il motivo.
//
// Uso:  dotnet run -c Release -- ALLENATORE.json CARTELLA_USCITA
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

var all = JsonNode.Parse(File.ReadAllText(args[0]))!;
var uscita = Directory.CreateDirectory(args[1]).FullName;
var nomi = GameInfo.GetStrings("it").specieslist;
var rapporto = new JsonArray();
int scritti = 0, rifiutati = 0;

SimpleTrainerInfo Allenatore(GameVersion v, EntityContext ctx, byte gen) => new(v)
{
    OT = (string)all["nome"]!, TID16 = (ushort)(int)all["tid"]!, SID16 = (ushort)(int)all["sid"]!,
    Gender = (string)all["sesso"]! == "maschio" ? (byte)0 : (byte)1, Language = (int)all["lingua"]!,
    Generation = gen, Context = ctx,
};

void Scrivi(PKM g, string nome, JsonObject voce)
{
    var dati = new byte[g.SIZE_STORED]; g.WriteDecryptedDataStored(dati);
    var cartella = Directory.CreateDirectory(Path.Combine(uscita, (string)voce["base"]!)).FullName;
    File.WriteAllBytes(Path.Combine(cartella, nome + "." + g.Extension), dati);
    voce["file"] = (string)voce["base"]! + "/" + nome + "." + g.Extension;
    voce["sha256"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant();
    scritti++;
}

// Le carte dei doni.
var basi = new (string nome, IEnumerable<MysteryGift> carte, GameVersion[] giochi, EntityContext ctx, byte gen)[]
{
    ("WB7", EncounterEvent.MGDB_G7GG, [GameVersion.GP, GameVersion.GE], EntityContext.Gen7b, 7),
    ("WC8", EncounterEvent.MGDB_G8, [GameVersion.SW, GameVersion.SH], EntityContext.Gen8, 8),
    ("WB8", EncounterEvent.MGDB_G8B, [GameVersion.BD, GameVersion.SP], EntityContext.Gen8b, 8),
    ("WA8", EncounterEvent.MGDB_G8A, [GameVersion.PLA], EntityContext.Gen8a, 8),
    ("WC9", EncounterEvent.MGDB_G9, [GameVersion.SL, GameVersion.VL], EntityContext.Gen9, 9),
    ("WA9", EncounterEvent.MGDB_G9A, [GameVersion.ZA], EntityContext.Gen9a, 9),
};
foreach (var (nomeBase, carte, giochi, ctx, gen) in basi)
{
    int n = 0, ok = 0;
    foreach (var c in carte)
    {
        if (!c.IsEntity) continue;
        n++;
        var voce = new JsonObject { ["base"] = nomeBase, ["carta"] = c.CardID, ["titolo"] = c.CardTitle, ["numero"] = c.Species, ["specie"] = nomi[c.Species], ["forma"] = c.Form };
        string motivo = "";
        foreach (var v in giochi)
        {
            try
            {
                var g = c.ConvertToPKM(Allenatore(v, ctx, gen));
                var la = new LegalityAnalysis(g);
                if (!la.Valid) { motivo = la.Results.First(r => !r.Valid).Identifier.ToString(); continue; }
                voce["versione"] = v.ToString(); voce["allenatore"] = g.OriginalTrainerName; voce["tid"] = g.DisplayTID;
                voce["cromatico"] = g.IsShiny; voce["livello"] = g.CurrentLevel; voce["lingua"] = g.Language; voce["conforme"] = true;
                Scrivi(g, $"{nomeBase}-{c.CardID:0000}-{c.Species:0000}-{c.Form}-{n:0000}", voce);
                motivo = ""; ok++;
                break;
            }
            catch (Exception ex) { motivo = ex.GetType().Name + ": " + ex.Message; }
        }
        if (motivo != "") { voce["conforme"] = false; voce["motivo"] = motivo; rifiutati++; }
        rapporto.Add(voce);
    }
    Console.WriteLine($"{nomeBase}: {n} carte con un Pokemon, {ok} conformi");
}

// Gli incontri di distribuzione: tane di Spada e Scudo, raid Teracristal, raid a sette stelle, focolai distribuiti.
var classi = new HashSet<string> { "EncounterStatic8ND", "EncounterDist9", "EncounterMight9", "EncounterOutbreak9" };
var giochiRaid = new (GameVersion v, Func<PKM> nuovo, IPersonalTable pt, EntityContext ctx, byte gen)[]
{
    (GameVersion.SW, () => new PK8(), PersonalTable.SWSH, EntityContext.Gen8, 8),
    (GameVersion.SH, () => new PK8(), PersonalTable.SWSH, EntityContext.Gen8, 8),
    (GameVersion.SL, () => new PK9(), PersonalTable.SV, EntityContext.Gen9, 9),
    (GameVersion.VL, () => new PK9(), PersonalTable.SV, EntityContext.Gen9, 9),
};
foreach (var (v, nuovo, pt, ctx, gen) in giochiRaid)
{
    var tr = Allenatore(v, ctx, gen);
    int n = 0, ok = 0;
    var visti = new HashSet<string>();
    for (ushort s = 1; s <= pt.MaxSpeciesID; s++)
    {
        for (byte f = 0; f < Math.Max((byte)1, pt[s].FormCount); f++)
        {
            if (!pt.IsPresentInGame(s, f)) continue;
            var pk = nuovo(); pk.Species = s; pk.Form = f; pk.Language = tr.Language;
            List<IEncounterable> trovati;
            try { trovati = EncounterMovesetGenerator.GenerateEncounters(pk, tr, ReadOnlyMemory<ushort>.Empty, v).Where(e => classi.Contains(e.GetType().Name) && e.Species == s && e.Form == f).ToList(); }
            catch { continue; }
            foreach (var e in trovati)
            {
                // Un incontro di distribuzione e' un record: la sua resa testuale porta tutti i campi, quindi distingue
                // due distribuzioni della stessa specie anche quando il nome lungo e' lo stesso.
                if (!visti.Add(e.ToString() ?? "")) continue;
                n++;
                var nomeBase = e.GetType().Name.Replace("Encounter", "");
                var voce = new JsonObject { ["base"] = nomeBase, ["numero"] = s, ["specie"] = nomi[s], ["forma"] = f, ["versione"] = v.ToString(), ["incontro"] = e.LongName, ["livello_incontro"] = e.LevelMin };
                try
                {
                    var g = e.ConvertToPKM(tr);
                    var la = new LegalityAnalysis(g);
                    if (!la.Valid) { voce["conforme"] = false; voce["motivo"] = la.Results.First(r => !r.Valid).Identifier.ToString(); rifiutati++; rapporto.Add(voce); continue; }
                    voce["allenatore"] = g.OriginalTrainerName; voce["cromatico"] = g.IsShiny; voce["livello"] = g.CurrentLevel; voce["conforme"] = true;
                    Scrivi(g, $"{nomeBase}-{v}-{s:0000}-{f}-{n:0000}", voce);
                    ok++;
                }
                catch (Exception ex) { voce["conforme"] = false; voce["motivo"] = ex.GetType().Name + ": " + ex.Message; rifiutati++; }
                rapporto.Add(voce);
            }
        }
    }
    Console.WriteLine($"distribuzioni {v}: {n} incontri distinti, {ok} conformi");
}
File.WriteAllText(Path.Combine(uscita, "rapporto.json"), new JsonObject { ["fonte"] = "PKHeX.Core tramite tools/pkhex-eventi-switch", ["esemplari"] = rapporto }.ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"scritti {scritti} esemplari conformi, {rifiutati} voci non conformi nel rapporto");
return 0;
