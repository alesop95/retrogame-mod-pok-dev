// I doni segreti sulla libreria del verificatore, compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Per ADR-081 gli esemplari legali si generano con la libreria e non con imitazioni scritte
// a mano. Per i doni di sesta e settima generazione la libreria ha gia' tutto: la base delle carte ufficiali
// (EncounterEvent.MGDB_G6 e MGDB_G7) e, per ciascuna, ConvertToPKM, che costruisce l'esemplare come lo
// avrebbe ricevuto il gioco del salvataggio dato.
//
// Che cosa fa. Carica un salvataggio, che fornisce l'allenatore, la lingua e il contesto di giudizio; cerca
// nella base dei doni della sua generazione le carte che portano la specie, ed eventualmente la forma,
// richiesta; per ciascuna genera l'esemplare, lo giudica con quel salvataggio attivo e lo scrive come
// DONO-<gen>-<carta>-<posizione>-<specie>-<forma>.pkN con un rapporto JSON. Con --copia-salvataggio scrive il primo
// esemplare conforme nel primo posto libero del deposito di una COPIA del salvataggio, salva la copia, la
// ricarica e confronta byte per byte il posto riletto con quello scritto, poi rigiudica l'esemplare riletto.
// Il salvataggio di partenza non viene mai modificato.
//
// Il perimetro. Lo strumento lavora sul PC. Per `rules/hardware-and-perimeter.md` un salvataggio preso da
// internet non si importa sulla console: su quei salvataggi lo strumento serve a provare la procedura, e la
// copia modificata resta sul disco.
//
// Uso:  dotnet run -c Release -- SALVATAGGIO CARTELLA_USCITA SPECIE[/FORMA] [--copia-salvataggio PERCORSO]
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length < 3)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- SALVATAGGIO CARTELLA_USCITA SPECIE[/FORMA] [--copia-salvataggio PERCORSO]");
    return 2;
}
if (!SaveUtil.TryGetSaveFile(args[0], out var sav))
{
    Console.Error.WriteLine($"salvataggio non riconosciuto: {args[0]}");
    return 2;
}
var uscita = Directory.CreateDirectory(args[1]).FullName;
var richiesta = args[2].Split('/');
var specie = ushort.Parse(richiesta[0]);
byte? forma = richiesta.Length > 1 ? byte.Parse(richiesta[1]) : null;
string? copia = null;
for (int i = 3; i < args.Length - 1; i++)
    if (args[i] == "--copia-salvataggio")
        copia = args[i + 1];

ParseSettings.InitFromSaveFileData(sav);
IEnumerable<MysteryGift> base_ = sav.Generation switch
{
    6 => EncounterEvent.MGDB_G6,
    7 => EncounterEvent.MGDB_G7,
    _ => throw new NotSupportedException($"generazione {sav.Generation} non ancora gestita"),
};
var carte = base_.Where(g => g.IsEntity && g.Species == specie && (forma is null || g.Form == forma)).ToList();
Console.WriteLine($"salvataggio: {sav.Version}, lingua {(LanguageID)sav.Language}, generazione {sav.Generation}; carte trovate: {carte.Count}");

var esiti = new JsonArray();
PKM? primoConforme = null;
// Una stessa carta esiste in piu' lingue con lo stesso numero, quindi il nome del file porta anche la
// posizione della carta nell'elenco, cosi' che le versioni non si sovrascrivano a vicenda.
for (int posizione = 0; posizione < carte.Count; posizione++)
{
    var carta = carte[posizione];
    var voce = new JsonObject { ["carta"] = carta.CardID, ["titolo"] = carta.CardTitle, ["forma"] = carta.Form, ["lingua_carta"] = carta is WC6 w6 ? $"{(LanguageID)w6.Language}, limite {(LanguageID)w6.RestrictLanguage}" : carta is WC7 w7 ? $"{(LanguageID)w7.Language}, limite {(LanguageID)w7.RestrictLanguage}" : "?" };
    try
    {
        var pk = carta.ConvertToPKM(sav);
        var la = new LegalityAnalysis(pk);
        var dati = new byte[pk.SIZE_STORED];
        pk.WriteDecryptedDataStored(dati);
        var nome = $"DONO-{sav.Generation}-{carta.CardID:0000}-{posizione:00}-{pk.Species:000}-{pk.Form:00}.{pk.Extension}";
        File.WriteAllBytes(Path.Combine(uscita, nome), dati);
        voce["file"] = nome;
        voce["sha256"] = Convert.ToHexStringLower(SHA256.HashData(dati));
        voce["lingua"] = ((LanguageID)pk.Language).ToString();
        voce["esito"] = la.Valid ? "conforme" : "contestato";
        if (!la.Valid)
            voce["rilievi"] = new JsonArray(la.Report("en").Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(r => (JsonNode)r).ToArray());
        else
            primoConforme ??= pk;
    }
    catch (Exception e)
    {
        voce["esito"] = "errore";
        voce["errore"] = e.Message;
    }
    esiti.Add(voce);
}

var rapporto = new JsonObject
{
    ["salvataggio"] = Path.GetFileName(Path.GetDirectoryName(Path.GetFullPath(args[0]))) + "/" + Path.GetFileName(args[0]),
    ["versione"] = sav.Version.ToString(),
    ["lingua"] = ((LanguageID)sav.Language).ToString(),
    ["richiesta"] = args[2],
    ["esiti"] = esiti,
};

if (copia is not null && primoConforme is not null)
{
    // Il primo posto libero del deposito: nessun esemplare esistente viene toccato.
    int indice = Enumerable.Range(0, sav.SlotCount).FirstOrDefault(i => sav.GetBoxSlotAtIndex(i).Species == 0, -1);
    if (indice < 0)
        rapporto["copia"] = new JsonObject { ["esito"] = "nessun posto libero nel deposito" };
    else
    {
        sav.SetBoxSlotAtIndex(primoConforme, indice);
        var scritto = sav.GetBoxSlotAtIndex(indice);
        var byteScritti = new byte[scritto.SIZE_STORED];
        scritto.WriteDecryptedDataStored(byteScritti);
        File.WriteAllBytes(copia, sav.Write().ToArray());

        SaveUtil.TryGetSaveFile(copia, out var riletto);
        var letto = riletto!.GetBoxSlotAtIndex(indice);
        var byteLetti = new byte[letto.SIZE_STORED];
        letto.WriteDecryptedDataStored(byteLetti);
        ParseSettings.InitFromSaveFileData(riletto);
        var laLetto = new LegalityAnalysis(letto);
        rapporto["copia"] = new JsonObject
        {
            ["file"] = Path.GetFileName(copia),
            ["posto"] = $"scatola {indice / sav.BoxSlotCount + 1}, posto {indice % sav.BoxSlotCount + 1}",
            ["rilettura_identica"] = byteScritti.AsSpan().SequenceEqual(byteLetti),
            ["esito_riletto"] = laLetto.Valid ? "conforme" : "contestato",
            ["sha256_salvataggio"] = Convert.ToHexStringLower(SHA256.HashData(File.ReadAllBytes(copia))),
        };
    }
}

File.WriteAllText(Path.Combine(uscita, "rapporto.json"),
    rapporto.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
Console.WriteLine(rapporto.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }));
return 0;
