// Confronta due salvataggi posto per posto sui byte decifrati degli esemplari, con la libreria del verificatore compilata
// dal clone in _notes/fonti/cloni/pkhex.
//
// Perché esiste. Il 2026-10-07, rifacendo le copie per HOME per ADR-099, si è misurato che `tools/pkhex-scrivi-salvataggio`
// non è deterministico: due corse identiche hanno dato 215 esemplari diversi su 245 scritti. La causa sta nella libreria
// ed è voluta, perché `PK5.ConvertToPK6` assegna al ricordo del detentore un sentimento casuale con `Random.Shared`
// (`PKHeX.Core/PKM/PK5.cs` riga 479, `MemoryContext6.GetRandomFeeling6`), come fa il trasferimento vero. Ne segue che
// due copie non si confrontano con un'impronta del file, e che serve uno strumento che dica, per ogni posto, se
// l'esemplare è lo stesso a meno di quel campo. Serve a due verifiche: che una modifica allo strumento di scrittura non
// cambi ciò che scrive, e che una copia rifatta differisca da quella di prima soltanto negli esemplari voluti.
//
// Che cosa fa. Carica i due salvataggi, che devono avere lo stesso numero di posti, e per ogni posto classifica:
// vuoto in entrambi; uguale, byte per byte decifrati; uguale salvo il sentimento del ricordo del detentore, cioè il solo
// campo `HandlingTrainerMemoryFeeling` di `IMemoryHT`; diverso; presente in uno solo. Se accanto a ciascun salvataggio
// c'è il rapporto di `pkhex-scrivi-salvataggio`, riporta l'origine del posto nei due rapporti. Scrive tutto in JSON e a
// video stampa i conteggi e i posti diversi. Esce con 0 se nessun posto è diverso o presente in uno solo.
//
// Uso:  dotnet run -c Release -- SALVATAGGIO_A SALVATAGGIO_B USCITA.json
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length != 3)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- SALVATAGGIO_A SALVATAGGIO_B USCITA.json");
    return 2;
}
if (!SaveUtil.TryGetSaveFile(args[0], out var a) || !SaveUtil.TryGetSaveFile(args[1], out var b))
{
    Console.Error.WriteLine("salvataggio non riconosciuto");
    return 2;
}
if (a.SlotCount != b.SlotCount)
{
    Console.Error.WriteLine($"numero di posti diverso: {a.SlotCount} e {b.SlotCount}");
    return 2;
}

Dictionary<(int, int), string> Origini(string salvataggio)
{
    var o = new Dictionary<(int, int), string>();
    var r = salvataggio + ".rapporto.json";
    if (File.Exists(r))
        foreach (var v in JsonNode.Parse(File.ReadAllText(r))!["voci"]!.AsArray())
            o[((int)v!["box"]!, (int)v["posto"]!)] = (string)v["origine"]!;
    return o;
}
byte[] Byte(PKM pk)
{
    var d = new byte[pk.SIZE_STORED];
    pk.WriteDecryptedDataStored(d);
    return d;
}
var (origA, origB) = (Origini(args[0]), Origini(args[1]));
var conteggi = new SortedDictionary<string, int>(StringComparer.Ordinal);
var posti = new JsonArray();
for (int i = 0; i < a.SlotCount; i++)
{
    var (pa, pb) = (a.GetBoxSlotAtIndex(i), b.GetBoxSlotAtIndex(i));
    string esito;
    if (pa.Species == 0 && pb.Species == 0)
        esito = "vuoto in entrambi";
    else if (pa.Species == 0 || pb.Species == 0)
        esito = "presente in uno solo";
    else if (Byte(pa).AsSpan().SequenceEqual(Byte(pb)))
        esito = "uguale";
    else
        esito = CampiDiConversione(pa, pb) is { } campi ? "uguale salvo " + campi : "diverso";
    conteggi[esito] = conteggi.GetValueOrDefault(esito) + 1;
    if (esito == "vuoto in entrambi")
        continue;
    var chiave = (i / a.BoxSlotCount + 1, i % a.BoxSlotCount + 1);
    var voce = new JsonObject
    {
        ["box"] = chiave.Item1, ["posto"] = chiave.Item2, ["esito"] = esito,
        ["specie_a"] = pa.Species, ["specie_b"] = pb.Species,
        ["origine_a"] = origA.GetValueOrDefault(chiave), ["origine_b"] = origB.GetValueOrDefault(chiave),
    };
    // Per un posto diverso, gli offset dei byte decifrati che differiscono, in esadecimale: dicono quali campi cambiano.
    if (esito == "diverso")
    {
        var (da, db) = (Byte(pa), Byte(pb));
        voce["offset_diversi"] = string.Join(" ", Enumerable.Range(0, Math.Min(da.Length, db.Length)).Where(k => da[k] != db[k]).Select(k => k.ToString("X2")));
    }
    posti.Add(voce);
}
foreach (var (esito, n) in conteggi)
    Console.WriteLine($"  {n,5}  {esito}");
foreach (var p in posti.Where(p => (string)p!["esito"]! is "diverso" or "presente in uno solo"))
    Console.WriteLine($"  box {p!["box"]} posto {p["posto"]}: {p["esito"]}, {p["origine_a"]} -> {p["origine_b"]}{(p["offset_diversi"] is { } o ? ", offset " + o : "")}");
File.WriteAllText(args[2], new JsonObject { ["formato"] = 1, ["a"] = args[0], ["b"] = args[1], ["posti"] = posti }
    .ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
return conteggi.ContainsKey("diverso") || conteggi.ContainsKey("presente in uno solo") ? 1 : 0;

// Se B coincide con A dopo avergli dato i campi che la conversione assegna da sé, restituisce quali campi è servito
// copiare; altrimenti null. I campi sono due, misurati il 2026-10-07: il sentimento del ricordo del detentore, che
// `PK5.ConvertToPK6` sceglie a caso (`PK5.cs` riga 479), e la data d'incontro, che `PK3.ConvertToPK4` pone uguale al
// giorno della conversione come il Parco Amici (`PK3.cs` riga 255). La stessa regola sta in `pkhex-scrivi-salvataggio`,
// funzione `CampiDiConversione`, e non si cambia qui senza cambiarla là.
static string? CampiDiConversione(PKM a, PKM b)
{
    static byte[] Dati(PKM pk) { var d = new byte[pk.SIZE_STORED]; pk.WriteDecryptedDataStored(d); return d; }
    var copia = b.Clone();
    var campi = new List<string>();
    if (a is IMemoryHT ma && copia is IMemoryHT mc && ma.HandlingTrainerMemoryFeeling != mc.HandlingTrainerMemoryFeeling)
    {
        mc.HandlingTrainerMemoryFeeling = ma.HandlingTrainerMemoryFeeling;
        campi.Add("il sentimento del ricordo");
    }
    if (a.MetDate != copia.MetDate)
    {
        copia.MetDate = a.MetDate;
        campi.Add("la data d'incontro");
    }
    copia.RefreshChecksum();
    return campi.Count > 0 && Dati(a).AsSpan().SequenceEqual(Dati(copia)) ? string.Join(" e ", campi) : null;
}
