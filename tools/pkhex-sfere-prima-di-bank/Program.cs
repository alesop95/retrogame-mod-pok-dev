// Le combinazioni di specie e Poke Ball che esistono soltanto nei giochi fino alla settima generazione, cioe' quelle
// che dopo la chiusura di Bank (2027-02-26) nessuno potra' piu' creare da capo. Nasce il 2026-11-04 su richiesta del
// proprietario, che legge di collezionisti che cercano coppie specie e sfera precise e vuole sapere quali si perdono.
//
// Il criterio, tutto preso dalla libreria del verificatore e non da un elenco della comunita':
//   prima di Bank  una sfera e' possibile per una specie allevabile se la tabella di eredita' della settima
//                  generazione (BallContext7) la permette, cioe' se esisteva una catena di giochi fino al 3DS che
//                  la portava;
//   dopo Bank      la stessa sfera resta ottenibile se la specie, o una sua pre-evoluzione, e' presente nella tabella
//                  personale di almeno un gioco per Switch collegato a HOME e l'insieme delle sfere selvatiche di quel
//                  gioco (BallUseLegality.GetWildBalls, interno alla libreria e letto per riflessione) la contiene.
// La differenza e' cio' che si perde. Le specie non allevabili (leggendari, misteriosi, Pokemon senza gruppo uova) non
// passano dall'eredita' e restano fuori da questa misura: le loro coppie dipendono da incontri precisi, che il
// documento elenca dalle fonti.
//
// Uso:  dotnet run -c Release -- USCITA.json
using System.Reflection;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

var getWild = typeof(PKM).Assembly.GetType("PKHeX.Core.BallUseLegality")!
    .GetMethod("GetWildBalls", BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static)!;
ulong Wild(byte gen, GameVersion v) => (ulong)getWild.Invoke(null, [gen, v])!;

var switchGames = new (string Nome, IPersonalTable T, byte Gen, GameVersion V)[] {
    ("Spada e Scudo", PersonalTable.SWSH, 8, GameVersion.SW),
    ("Diamante Lucente e Perla Splendente", PersonalTable.BDSP, 8, GameVersion.BD),
    ("Leggende Arceus", PersonalTable.LA, 8, GameVersion.PLA),
    ("Scarlatto e Violetto", PersonalTable.SV, 9, GameVersion.SL),
    ("Leggende Z-A", PersonalTable.ZA, 9, GameVersion.ZA),
    ("Let's Go", PersonalTable.GG, 7, GameVersion.GP),
};
var testi = GameInfo.GetStrings("it");
var inglese = GameInfo.GetStrings("en");
var evo = EvolutionTree.Evolves7;
Ball[] sfere = Enum.GetValues<Ball>().Where(b => b is > Ball.None and <= Ball.Beast and not Ball.Master and not Ball.Cherish).ToArray();

var voci = new JsonArray();
int coppie = 0;
for (ushort s = 1; s <= 809; s++)
{
    var forme = FormConverter.GetFormList(s, testi.Types, testi.forms, GameInfo.GenderSymbolASCII, EntityContext.Gen7);
    int n = Math.Max(1, forme.Length);
    for (byte f = 0; f < n; f++)
    {
        if (!PersonalTable.USUM.IsPresentInGame(s, f) && !PersonalTable.AO.IsPresentInGame(s, f))
            continue;
        if (FormInfo.IsBattleOnlyForm(s, f, 7) || FormInfo.IsTotemForm(s, f, EntityContext.Gen7))
            continue;
        var pi = PersonalTable.USUM.GetFormEntry(s, f);
        if (pi.EggGroup1 == 15 || pi.EggGroup2 == 15) // gruppo Sconosciuto, non allevabile
            continue;
        // La specie e le sue pre-evoluzioni, fino alla radice.
        var famiglia = new List<(ushort S, byte F)> { (s, f) };
        var cur = (s, f);
        for (int i = 0; i < 4; i++)
        {
            var b = evo.GetBaseSpeciesForm(cur.Item1, cur.Item2);
            if (b == cur) break;
            famiglia.Add(b); cur = b;
        }
        var perse = new JsonArray();
        foreach (var ball in sfere)
        {
            if (!BallContext7.Instance.CanBreedWithBall(s, f, ball))
                continue;
            // Spinda non si sposta fra HOME e Diamante Lucente e Perla Splendente (tabella di connettivita' di HOME,
            // `pokedex-home-completo/CONNETTIVITA-HOME.md`): uno Spinda di quei giochi non arriva in HOME.
            var dove = switchGames.Where(g => !(s == (int)Species.Spinda && g.T == PersonalTable.BDSP))
                                  .Where(g => famiglia.Any(m => g.T.IsPresentInGame(m.S, m.F))
                                          && BallUseLegality_IsPermitted(Wild(g.Gen, g.V), (byte)ball)).Select(g => g.Nome).ToList();
            if (dove.Count == 0)
            {
                perse.Add(testi.balllist[(int)ball]);
                coppie++;
            }
        }
        if (perse.Count == 0) continue;
        var presente = switchGames.Where(g => g.T.IsPresentInGame(s, f)).Select(g => (JsonNode)g.Nome).ToArray();
        voci.Add(new JsonObject {
            ["numero"] = s, ["forma_n"] = f, ["specie"] = testi.specieslist[s], ["forma"] = f < forme.Length ? forme[f] : "",
            ["sfere_perse"] = perse, ["giochi_switch_con_la_specie"] = new JsonArray(presente) });
    }
}
File.WriteAllText(args[0], new JsonObject { ["coppie_perse"] = coppie, ["voci"] = voci }
    .ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"specie e forme con sfere perse: {voci.Count}, coppie specie e sfera perse: {coppie}");
return 0;

static bool BallUseLegality_IsPermitted(ulong permit, byte ball) => ball < 64 && (permit & (1ul << ball)) != 0;
