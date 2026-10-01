// Gli incontri di ogni specie e forma nei giochi per Switch, con la libreria del verificatore compilata dal clone in
// _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il 2026-10-01 il proprietario ha una Switch 2 e vuole sapere, per ogni voce della lista completa, in
// quale gioco per Switch e come si ottiene. Il dataset di PokePC dice in quali giochi una voce si ottiene, ma non
// distingue la versione di un'esclusiva, il contenuto scaricabile, il luogo o il metodo. La libreria li conosce, perche'
// sono gli stessi incontri con cui giudica la legalita' di un esemplare: e' la fonte piu' precisa che il progetto abbia.
//
// Che cosa fa. Per ogni gioco (Scarlatto, Violetto, Spada, Scudo, Diamante Lucente, Perla Splendente, Leggende Arceus,
// Let's Go Pikachu e Eevee, Leggende Z-A), per ogni specie e forma presente nel gioco, chiede alla libreria gli incontri
// che la producono, evoluzioni comprese, e scrive in JSON per ciascuno: gioco, classe d'incontro, specie e forma di
// partenza, livello, luogo, se e' cromatico bloccato, e il nome lungo della libreria. I doni segreti si marcano come
// evento, perche' sono distribuzioni a tempo.
//
// Uso:  dotnet run -c Release -- USCITA.json
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

var it = GameInfo.GetStrings("it");
var en = GameInfo.GetStrings("en");
var giochi = new (GameVersion v, string nome, Func<PKM> nuovo, IPersonalTable pt, EntityContext ctx, byte gen)[]
{
    (GameVersion.ZA, "Leggende Pokémon Z-A", () => new PA9(), PersonalTable.ZA, EntityContext.Gen9a, 9),
    (GameVersion.SL, "Scarlatto", () => new PK9(), PersonalTable.SV, EntityContext.Gen9, 9),
    (GameVersion.VL, "Violetto", () => new PK9(), PersonalTable.SV, EntityContext.Gen9, 9),
    (GameVersion.SW, "Spada", () => new PK8(), PersonalTable.SWSH, EntityContext.Gen8, 8),
    (GameVersion.SH, "Scudo", () => new PK8(), PersonalTable.SWSH, EntityContext.Gen8, 8),
    (GameVersion.BD, "Diamante Lucente", () => new PB8(), PersonalTable.BDSP, EntityContext.Gen8b, 8),
    (GameVersion.SP, "Perla Splendente", () => new PB8(), PersonalTable.BDSP, EntityContext.Gen8b, 8),
    (GameVersion.PLA, "Leggende Pokémon Arceus", () => new PA8(), PersonalTable.LA, EntityContext.Gen8a, 8),
    (GameVersion.GP, "Let's Go Pikachu", () => new PB7(), PersonalTable.GG, EntityContext.Gen7b, 7),
    (GameVersion.GE, "Let's Go Eevee", () => new PB7(), PersonalTable.GG, EntityContext.Gen7b, 7),
};
var voci = new JsonArray();
foreach (var (v, nome, nuovo, pt, ctx, gen) in giochi)
{
    var tr = new SimpleTrainerInfo(v) { OT = "PROVA", Language = (int)LanguageID.English, Generation = gen, Context = ctx };
    int conto = 0;
    for (ushort s = 1; s <= 1025; s++)
    {
        if (s > pt.MaxSpeciesID) break;
        var info = pt[s];
        for (byte f = 0; f < Math.Max((byte)1, info.FormCount); f++)
        {
            if (!pt.IsPresentInGame(s, f)) continue;
            if (FormInfo.IsBattleOnlyForm(s, f, gen)) continue;
            var pk = nuovo();
            pk.Species = s; pk.Form = f; pk.Language = (int)LanguageID.English;
            pk.Gender = pt[s, f].RandomGender();
            List<IEncounterable> trovati;
            try { trovati = EncounterMovesetGenerator.GenerateEncounters(pk, tr, ReadOnlyMemory<ushort>.Empty, v).ToList(); }
            catch { continue; }
            var forme = FormConverter.GetFormList(s, en.types, en.forms, GameInfo.GenderSymbolASCII, ctx);
            foreach (var e in trovati.DistinctBy(e => (e.GetType().Name, e.Species, e.Form, e.LongName)))
            {
                // La libreria come giudice: si genera l'esemplare dall'incontro, gli si dà la specie e la forma cercate,
                // e si tiene l'esito dell'analisi di legalita'. Il generatore d'incontri cerca per specie e non garantisce
                // che quella forma, li', sia legale: il caso che lo ha mostrato e' il Vivillon Motivo Poke Ball.
                bool legale; string motivo = "";
                try
                {
                    var g = e.ConvertToPKM(tr);
                    if (g.Species != s || g.Form != f)
                    {
                        g.Species = s; g.Form = f;
                        if (g.CurrentLevel < 100 && e.Species != s) g.CurrentLevel = 100;
                        g.RefreshAbility(g.AbilityNumber >> 1);
                        g.SetDefaultNickname();
                    }
                    g.RefreshChecksum();
                    var la = new LegalityAnalysis(g);
                    legale = la.Valid;
                    if (!legale) motivo = la.Results.FirstOrDefault(r => !r.Valid).Identifier.ToString();
                }
                catch (Exception ex) { legale = false; motivo = ex.GetType().Name; }
                string luogo = "";
                if (e is ILocation l) luogo = l.GetEncounterLocation(gen, v) ?? "";
                var classe = e.GetType().Name;
                voci.Add(new JsonObject
                {
                    ["gioco"] = nome,
                    ["versione"] = v.ToString(),
                    ["numero"] = s,
                    ["forma"] = f,
                    ["forma_en"] = f < forme.Length ? forme[f] : "",
                    ["specie"] = it.specieslist[s],
                    ["classe"] = classe,
                    ["evento"] = e is MysteryGift,
                    ["uovo"] = e.IsEgg,
                    ["da_specie"] = e.Species == s ? "" : it.specieslist[e.Species],
                    ["da_forma"] = e.Form,
                    ["livello"] = e.LevelMin == e.LevelMax ? e.LevelMin.ToString() : $"{e.LevelMin}-{e.LevelMax}",
                    ["luogo"] = luogo,
                    ["cromatico"] = e.Shiny.ToString(),
                    ["nome_lungo"] = e.LongName,
                    ["legale"] = legale,
                    ["motivo"] = motivo,
                });
                conto++;
            }
        }
    }
    Console.WriteLine($"{nome}: {conto} incontri");
}
File.WriteAllText(args[0], new JsonObject { ["fonte"] = "EncounterMovesetGenerator di PKHeX.Core, tramite tools/pkhex-incontri-switch", ["incontri"] = voci }.ToJsonString(new JsonSerializerOptions { WriteIndented = false }));
return 0;
