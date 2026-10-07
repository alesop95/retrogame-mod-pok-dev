// Allinea un salvataggio di terza generazione di una cartuccia: l'identificativo segreto degli esemplari dell'allenatore
// del progetto e il Pokédex, con la libreria del verificatore compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perché esiste. Due decisioni toccano la cartuccia del Rubino e si eseguono con una sola scrittura, perché la cartuccia
// si scrive il meno possibile (`rules/hardware-and-perimeter.md`). ADR-099: i 101 esemplari di origine Smeraldo del
// complemento portano SID 0 e vanno a 58164, come nei file del lotto già corretti da `tools/pkhex-correggi-sid`. ADR-089:
// la scrittura diretta nel deposito non accende il Pokédex, e le specie presenti in squadra e nei box vanno registrate
// come viste e catturate.
//
// Su che cosa poggia. Il Pokédex di Rubino e Zaffiro, letto su pokeruby (`src/pokedex.c` riga 3986, `GetSetPokedexFlag`):
// un «visto» vale solo se è acceso in tre copie, `gSaveBlock2.pokedex.seen` e `gSaveBlock1.dexSeen2` e `dexSeen3`,
// altrimenti il gioco le spegne tutte; un «catturato», in `gSaveBlock2.pokedex.owned`, vale solo se coincide con le tre.
// Offset in `include/global.h`: Pokédex a 0x18 di SaveBlock2, catturati a +0x10, visti a +0x44, personalità di Unown a
// +0x04 e di Spinda a +0x08; `dexSeen2` a 0x938 e `dexSeen3` a 0x3A8C di SaveBlock1. La libreria fa lo stesso
// (`SAV3.cs` righe 539-562, `SaveBlock3LargeRS.cs` righe 22 e 171), e lo strumento usa `SetSeen` e `SetCaught` della
// libreria. Le personalità di Unown e Spinda si scrivono solo se la specie non è né vista né catturata, perché il gioco le
// scrive alla prima cattura (`battle_script_commands.c` riga 9525) e la libreria al primo avvistamento: con entrambe
// spente le due regole coincidono. Il Pokédex nazionale non si sblocca: cambia la progressione della partita ed è una
// decisione a sé del proprietario; i contrassegni delle specie fuori da Hoenn si accendono comunque e restano invisibili
// finché non lo sblocca.
//
// Che cosa fa. Legge INGRESSO; per ogni esemplare di squadra e box con il TID e il SID dati imposta il SID nuovo, e
// rifiuta se cambiano PID o cromaticità o se la libreria lo contesta nel contesto del salvataggio; lo riscrive con
// `EntityImportSettings.None`, così che la riscrittura non tocchi il Pokédex. Poi, per ogni specie presente fuori dalle
// uova, accende visto e catturato. Scrive USCITA, che non deve esistere, nello slot attivo (`SAV3.cs` riga 158): l'altro
// slot resta com'era. Ricarica USCITA e verifica: stesse specie e stessi PID in ogni posto, SID cambiato solo dove
// previsto, ogni specie presente vista e catturata, le tre copie dei visti uguali per tutte le 386 specie, e nessuna
// specie accesa che non fosse accesa prima o presente. Se una verifica cade cancella USCITA e lo dice. Scrive accanto a
// USCITA un rapporto JSON, `USCITA.allineamento.json`: non `.rapporto.json`, che `pkhex-elenco-copie` legge come rapporto di scrittura.
//
// Uso:  dotnet run -c Release -- INGRESSO.sav USCITA.sav --tid N --da SID --a SID
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

string? Opzione(string nome) { var i = Array.IndexOf(args, nome); return i >= 0 && i + 1 < args.Length ? args[i + 1] : null; }
if (args.Length < 2 || Opzione("--tid") is not { } tidTesto || Opzione("--da") is not { } daTesto || Opzione("--a") is not { } aTesto)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- INGRESSO.sav USCITA.sav --tid N --da SID --a SID");
    return 2;
}
var (ingresso, uscita) = (args[0], args[1]);
ushort tid = ushort.Parse(tidTesto), da = ushort.Parse(daTesto), a = ushort.Parse(aTesto);
if (File.Exists(uscita))
{
    Console.Error.WriteLine($"l'uscita esiste già, non la sovrascrivo: {uscita}");
    return 2;
}
if (!SaveUtil.TryGetSaveFile(ingresso, out var letto) || letto is not SAV3 sav)
{
    Console.Error.WriteLine($"non è un salvataggio di terza generazione: {ingresso}");
    return 2;
}
ParseSettings.InitFromSaveFileData(sav);
const ushort Specie = 386;

// Gli esemplari di squadra e box, con un modo di leggerli e di riscriverli.
var posti = new List<(string Dove, Func<PKM> Leggi, Action<PKM> Scrivi)>();
for (int i = 0; i < sav.PartyCount; i++)
{
    int k = i;
    posti.Add(($"squadra {k + 1}", () => sav.GetPartySlotAtIndex(k), pk => sav.SetPartySlotAtIndex(pk, k, EntityImportSettings.None)));
}
for (int i = 0; i < sav.SlotCount; i++)
{
    int k = i;
    posti.Add(($"box {k / sav.BoxSlotCount + 1} posto {k % sav.BoxSlotCount + 1}", () => sav.GetBoxSlotAtIndex(k), pk => sav.SetBoxSlotAtIndex(pk, k, EntityImportSettings.None)));
}
var prima = posti.Select(p => p.Leggi()).Select(pk => (pk.Species, pk.PID, pk.TID16, pk.SID16, pk.IsEgg)).ToList();
var catturatiPrima = Enumerable.Range(1, Specie).Select(s => sav.GetCaught((ushort)s)).ToArray();
var vistiPrima = Enumerable.Range(1, Specie).Select(s => sav.GetSeen((ushort)s)).ToArray();

// L'identificativo segreto.
var corretti = new JsonArray();
var rifiuti = new List<string>();
foreach (var (dove, leggi, scrivi) in posti)
{
    var pk = leggi();
    if (pk.Species == 0 || pk.TID16 != tid || pk.SID16 != da)
        continue;
    var (pid, cromatico) = (pk.PID, pk.IsShiny);
    pk.SID16 = a;
    pk.RefreshChecksum();
    var la = new LegalityAnalysis(pk);
    if (pk.PID != pid || pk.IsShiny != cromatico || !la.Valid)
    {
        rifiuti.Add($"{dove}: specie {pk.Species}, PID {(pk.PID == pid ? "uguale" : "cambiato")}, cromaticità {(pk.IsShiny == cromatico ? "uguale" : "cambiata")}, {(la.Valid ? "conforme" : "contestato")}");
        continue;
    }
    scrivi(pk);
    corretti.Add(new JsonObject { ["posto"] = dove, ["specie"] = pk.Species, ["pid"] = pid.ToString("X8") });
}
if (rifiuti.Count > 0)
{
    foreach (var r in rifiuti) Console.WriteLine(r);
    Console.WriteLine($"{rifiuti.Count} esemplari rifiutati, nessun file scritto");
    return 1;
}

// Il Pokédex.
var presenti = posti.Select(p => p.Leggi()).Where(pk => pk.Species is > 0 and <= Specie && !pk.IsEgg).ToList();
var accese = new JsonArray();
foreach (var gruppo in presenti.GroupBy(pk => pk.Species).OrderBy(g => g.Key))
{
    var s = gruppo.Key;
    if (sav.GetCaught(s) && sav.GetSeen(s))
        continue;
    if (!sav.GetSeen(s) && !sav.GetCaught(s))
    {
        if (s == (ushort)Species.Unown) sav.SmallBlock.DexPIDUnown = gruppo.First().PID;
        if (s == (ushort)Species.Spinda) sav.SmallBlock.DexPIDSpinda = gruppo.First().PID;
    }
    sav.SetCaught(s, true);
    sav.SetSeen(s, true);
    accese.Add(s);
}

File.WriteAllBytes(uscita, sav.Write().ToArray());

// La rilettura.
var problemi = new List<string>();
if (!SaveUtil.TryGetSaveFile(uscita, out var r2) || r2 is not SAV3 riletto)
    problemi.Add("l'uscita non si rilegge come salvataggio di terza generazione");
else
{
    var postiR = new List<PKM>();
    for (int i = 0; i < riletto.PartyCount; i++) postiR.Add(riletto.GetPartySlotAtIndex(i));
    for (int i = 0; i < riletto.SlotCount; i++) postiR.Add(riletto.GetBoxSlotAtIndex(i));
    if (postiR.Count != prima.Count) problemi.Add("numero di posti diverso");
    var dovutiSid = corretti.Select(c => (string)c!["posto"]!).ToHashSet();
    for (int i = 0; i < Math.Min(postiR.Count, prima.Count); i++)
    {
        var (p, q) = (prima[i], postiR[i]);
        var sidAtteso = dovutiSid.Contains(posti[i].Dove) ? a : p.SID16;
        if (q.Species != p.Species || q.PID != p.PID || q.TID16 != p.TID16 || q.SID16 != sidAtteso || q.IsEgg != p.IsEgg)
            problemi.Add($"{posti[i].Dove}: diverso dall'atteso");
    }
    var presentiR = postiR.Where(pk => pk.Species is > 0 and <= Specie && !pk.IsEgg).Select(pk => pk.Species).ToHashSet();
    for (ushort s = 1; s <= Specie; s++)
    {
        bool c = riletto.GetCaught(s), v = riletto.GetSeen(s);
        if (presentiR.Contains(s) && !(c && v)) problemi.Add($"specie {s} presente ma non vista e catturata");
        if (!presentiR.Contains(s) && (c != catturatiPrima[s - 1] || v != vistiPrima[s - 1])) problemi.Add($"specie {s} assente e cambiata nel Pokédex");
        int ofs = (s - 1) >> 3, bit = (s - 1) & 7;
        bool v2 = FlagUtil.GetFlag(riletto.Large, riletto.LargeBlock.SeenOffset2 + ofs, bit);
        bool v3 = FlagUtil.GetFlag(riletto.Large, riletto.LargeBlock.SeenOffset3 + ofs, bit);
        if (v != v2 || v != v3) problemi.Add($"specie {s}: le tre copie dei visti non concordano");
        if (c && !v) problemi.Add($"specie {s}: catturata e non vista, il gioco la spegnerebbe");
    }
}
var rapporto = new JsonObject
{
    ["fonte"] = "PKHeX.Core tramite tools/pkhex-allinea-gen3 (ADR-099, ADR-089)",
    ["ingresso"] = Path.GetFileName(ingresso), ["sha256_ingresso"] = Convert.ToHexStringLower(SHA256.HashData(File.ReadAllBytes(ingresso))),
    ["uscita"] = Path.GetFileName(uscita), ["sha256_uscita"] = File.Exists(uscita) ? Convert.ToHexStringLower(SHA256.HashData(File.ReadAllBytes(uscita))) : null,
    ["tid"] = tid, ["sid_prima"] = da, ["sid_dopo"] = a, ["sid_corretti"] = corretti.Count,
    ["specie_presenti"] = presenti.Select(pk => pk.Species).Distinct().Count(),
    ["catturate_prima"] = catturatiPrima.Count(x => x), ["viste_prima"] = vistiPrima.Count(x => x),
    ["specie_accese"] = accese.Count, ["nazionale_sbloccato"] = sav.NationalDex,
    ["problemi"] = new JsonArray(problemi.Select(p => (JsonNode)p).ToArray()),
    ["corretti"] = corretti, ["accese"] = accese,
};
File.WriteAllText(uscita + ".allineamento.json", rapporto.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
if (problemi.Count > 0)
{
    File.Delete(uscita);
    foreach (var p in problemi.Take(20)) Console.WriteLine(p);
    Console.WriteLine($"{problemi.Count} problemi alla rilettura: uscita cancellata, rapporto conservato");
    return 1;
}
Console.WriteLine($"SID corretti {corretti.Count}; specie presenti {rapporto["specie_presenti"]}, catturate prima {rapporto["catturate_prima"]}, viste prima {rapporto["viste_prima"]}, accese {accese.Count}; nazionale sbloccato: {sav.NationalDex}");
Console.WriteLine($"scritto {uscita}, riletto senza problemi");
return 0;
