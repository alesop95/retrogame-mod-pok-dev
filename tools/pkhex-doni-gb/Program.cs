// Doni di Game Boy che il lotto di prima e seconda generazione non copriva, generati con la libreria del verificatore
// compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il lotto `_notes/lotti/lotto-gb/` e' nato da `tools/genera-evento-gb.py`, prima di ADR-081, e porta i
// doni di Pokemon Stadium nella sola variante italiana, STADIO con identificativo 2000. I video consegnati il
// 2026-09-29 (`zUv9dZ7B2Ks`, `rl31AqSOhto`, `R4oebXZTVo4`, `r0qoepkcdYY` in SOURCES.md) hanno fatto notare due cose che
// il lotto non ha: la variante giapponese degli stessi doni, allenatore スタジアム con identificativo 1999, che e' un
// esemplare di provenienza diversa; e l'Uovo Strano di Cristallo, quattordici voci fra normali e cromatiche. La
// libreria le conosce tutte: `EncounterGift1` con `TrainerType.Stadium`, `EncounterGift2` con
// `TrainerType.GiftStadiumJPN`, e l'elenco interno `Encounters2.StaticOddEggC`, raggiunto dagli incontri pubblici.
//
// Che cosa fa. Nell'epoca delle cartucce, chiede alla libreria gli incontri di ogni specie da 1 a 251 nelle versioni
// di prima e seconda generazione e tiene: i doni di Stadium, generati con un allenatore giapponese; le uova dell'Uovo
// Strano, generate con un allenatore italiano di Cristallo, dato che la variante giapponese la libreria la ammette solo
// con un salvataggio da cartuccia giapponese. Genera, giudica e scrive ciascun esemplare. La libreria estrae i numeri
// casuali da Random.Shared, quindi due lanci danno esemplari diversi e ugualmente legali: il risultato sono i file.
//
// Uso:  dotnet run -c Release -- CARTELLA_DI_USCITA
using PKHeX.Core;

if (args.Length != 1)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- CARTELLA_DI_USCITA");
    return 2;
}
var uscita = Directory.CreateDirectory(args[0]).FullName;
ParseSettings.AllowEraCartGB = true;
var nomi = GameInfo.GetStrings("en").Species;

var giapponese1 = new SimpleTrainerInfo(GameVersion.BU) { OT = "アレシオ", TID16 = 42317, Language = (int)LanguageID.Japanese, Generation = 1, Context = EntityContext.Gen1 };
var giapponese2 = new SimpleTrainerInfo(GameVersion.C) { OT = "アレシオ", TID16 = 42317, Language = (int)LanguageID.Japanese, Generation = 2, Context = EntityContext.Gen2 };
var italiano2 = new SimpleTrainerInfo(GameVersion.C) { OT = "Alessio", TID16 = 42317, Language = (int)LanguageID.Italian, Generation = 2, Context = EntityContext.Gen2 };
var visti = new HashSet<IEncounterable>(ReferenceEqualityComparer.Instance);
int scritti = 0, illegali = 0;

void Scrivi(IEncounterable enc, ITrainerInfo tr, string classe)
{
    if (!visti.Add(enc))
        return;
    var pk = enc.ConvertToPKM(tr);
    var la = new LegalityAnalysis(pk);
    var dati = new byte[pk.SIZE_STORED];
    pk.WriteDecryptedDataStored(dati);
    var cromatico = pk.IsShiny ? "-cromatico" : "";
    var nome = $"GB-{classe}-{pk.Species:000}-{nomi[pk.Species]}{cromatico}-{scritti:00}.{pk.Extension}";
    File.WriteAllBytes(Path.Combine(uscita, nome), dati);
    scritti++;
    Console.WriteLine($"{nome}: allenatore {pk.OriginalTrainerName}, identificativo {pk.TID16}, livello {pk.CurrentLevel}, uovo {pk.IsEgg}, legale {la.Valid}");
    if (!la.Valid) { illegali++; Console.WriteLine(la.Report()); }
}

for (ushort s = 1; s <= 251; s++)
{
    if (s <= 151)
    {
        var m1 = new PK1 { Species = s, Language = (int)LanguageID.Japanese };
        foreach (var enc in EncounterMovesetGenerator.GenerateEncounters(m1, giapponese1, ReadOnlyMemory<ushort>.Empty, GameVersion.RD, GameVersion.GN, GameVersion.BU, GameVersion.YW))
            if (enc is EncounterGift1 { Trainer: EncounterGift1.TrainerType.Stadium })
                Scrivi(enc, giapponese1, "stadium-jp");
            // Il Mew delle manifestazioni giapponesi, EVT-1-0010, allenatore マクハリ: aggiunto il 2026-09-30 dal secondo tempo.
            else if (enc is EncounterGift1 { Trainer: EncounterGift1.TrainerType.JapanTour })
                Scrivi(enc, giapponese1, "tour-jp");
    }
    var m2 = new PK2 { Species = s, Language = (int)LanguageID.Japanese };
    foreach (var enc in EncounterMovesetGenerator.GenerateEncounters(m2, giapponese2, ReadOnlyMemory<ushort>.Empty, GameVersion.GD, GameVersion.SI, GameVersion.C))
        if (enc is EncounterGift2 { Trainer: EncounterGift2.TrainerType.GiftStadiumJPN })
            Scrivi(enc, giapponese2, "stadium2-jp");
}
// L'elenco dell'Uovo Strano e' interno alla libreria: si riconosce fra gli incontri pubblici di Cristallo come uovo
// statico che porta Stordipugno, la mossa che nessun'altra uova di quelle specie conosce.
foreach (ushort s in new ushort[] { 172, 173, 174, 236, 238, 239, 240 })
{
    var m = new PK2 { Species = s, Language = (int)LanguageID.Italian };
    foreach (var enc in EncounterMovesetGenerator.GenerateEncounters(m, italiano2, ReadOnlyMemory<ushort>.Empty, GameVersion.C))
        if (enc is EncounterStatic2 { IsEgg: true } st && st.Moves.Contains((ushort)Move.DizzyPunch))
            Scrivi(enc, italiano2, "uovo-strano");
}

Console.WriteLine($"scritti {scritti}, illegali {illegali}");
return illegali == 0 ? 0 : 1;
