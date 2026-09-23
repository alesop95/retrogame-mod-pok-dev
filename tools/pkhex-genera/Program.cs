// Prova della fase F0 di ADR-080: la libreria del verificatore costruisce da una voce delle sue tabelle
// un esemplare con l'allenatore dato, e lo stesso verificatore lo giudica.
using PKHeX.Core;

var casi = new (ushort Specie, GameVersion Gioco, string Nome)[]
{
    (250, GameVersion.S, "Ho-Oh del Monte Lotta, verso Zaffiro"),
    (249, GameVersion.CXD, "Lugia Ombra di XD"),
    (385, GameVersion.S, "Jirachi di Pokémon Channel"),
};
foreach (var (specie, gioco, nome) in casi)
{
    var allenatore = new SimpleTrainerInfo(gioco is GameVersion.XD or GameVersion.COLO or GameVersion.CXD ? GameVersion.E : gioco) { OT = "Alessio", TID16 = 42317, SID16 = 1, Language = (int)LanguageID.Italian };
    var modello = EntityBlank.GetBlank(3);
    modello.Species = specie;
    var trovati = 0;
    foreach (var enc in EncounterMovesetGenerator.GenerateEncounters(modello, allenatore, ReadOnlyMemory<ushort>.Empty, gioco))
    {
        var pk = enc.ConvertToPKM(allenatore);
        var la = new LegalityAnalysis(pk);
        Console.WriteLine($"{nome}: {enc.GetType().Name} {enc.LongName} -> {(la.Valid ? "LEGALE" : "non legale")} OT={pk.OriginalTrainerName} TID={pk.TID16} PID={pk.PID:X8}");
        if (!la.Valid)
            Console.WriteLine(la.Report());
        if (++trovati >= 2) break;
    }
    if (trovati == 0) Console.WriteLine($"{nome}: nessuna voce trovata");
}
