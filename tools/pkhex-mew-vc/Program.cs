// Il Mew GF della Console Virtuale, generato con la libreria del verificatore compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. HOME accetta un solo Mew di prima generazione, quello che Game Freak consegnava alle edizioni
// per Console Virtuale del 3DS, con allenatore GF e identificativo 22796; il Mew del ponte Pepita non passa il
// Trasferitore. Il progetto lo aveva registrato come da aggiungere il 2026-09-09 e i video del 2026-09-29
// (`zUv9dZ7B2Ks` e `PY0p0zWsRt4` in SOURCES.md) lo hanno riproposto. La libreria lo conosce come
// `Encounters1VC.Gift`, un EncounterGift1 di livello 5, e per ADR-081 lo si genera da li' invece di scriverlo a mano.
//
// Che cosa fa. Chiede alla libreria gli incontri di Mew nelle quattro versioni di prima generazione, nel
// contesto della Console Virtuale, prende il dono, genera un esemplare giapponese e uno internazionale (il
// formato PK1 non distingue altre lingue), li giudica e li scrive. Si rigiudicano con
// `tools/pkhex-giudica` passando la cartella come CARTELLA=VC.
//
// Uso:  dotnet run -c Release -- CARTELLA_DI_USCITA
using PKHeX.Core;

if (args.Length != 1)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- CARTELLA_DI_USCITA");
    return 2;
}
var uscita = Directory.CreateDirectory(args[0]).FullName;
ParseSettings.AllowEraCartGB = false;
var versioni = new[] { GameVersion.RD, GameVersion.GN, GameVersion.BU, GameVersion.YW };
var tr0 = new SimpleTrainerInfo(GameVersion.RD) { OT = "GF", Language = (int)LanguageID.English, Generation = 1, Context = EntityContext.Gen1 };
var dono = EncounterMovesetGenerator.GenerateEncounters(new PK1 { Species = 151 }, tr0, ReadOnlyMemory<ushort>.Empty, versioni)
    .OfType<EncounterGift1>().FirstOrDefault();
if (dono is null)
{
    Console.Error.WriteLine("la libreria non restituisce il dono di Mew della Console Virtuale");
    return 1;
}
int illegali = 0;
foreach (var (lingua, etichetta) in new[] { (LanguageID.Japanese, "Giapponese"), (LanguageID.English, "Internazionale") })
{
    var tr = new SimpleTrainerInfo(GameVersion.RD) { OT = "GF", Language = (int)lingua, Generation = 1, Context = EntityContext.Gen1 };
    var pk = (PK1)dono.ConvertToPKM(tr);
    var la = new LegalityAnalysis(pk);
    var dati = new byte[pk.SIZE_STORED];
    pk.WriteDecryptedDataStored(dati);
    var nome = $"MEW-VC-GF-{etichetta}.pk1";
    File.WriteAllBytes(Path.Combine(uscita, nome), dati);
    Console.WriteLine($"{nome}: allenatore {pk.OriginalTrainerName}, identificativo {pk.TID16}, livello {pk.CurrentLevel}, legale {la.Valid}");
    if (!la.Valid) { illegali++; Console.WriteLine(la.Report()); }
}
return illegali == 0 ? 0 : 1;
