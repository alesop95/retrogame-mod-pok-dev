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
// La modalita' lotto. Con --lotto legge le richieste scritte da `tools/checklist-pokedex.py --richieste-doni`,
// cioe' le voci del primo tempo da doni di sesta e settima generazione. Per ciascuna prende la carta nella
// posizione indicata fra i soli esemplari della base, e la rifiuta se specie o forma non coincidono con la
// richiesta, perche' la corrispondenza fra le due numerazioni e' un'ipotesi che va controllata voce per voce.
// Genera poi l'esemplare con i salvataggi di contesto nell'ordine dato, seguiti da salvataggi vuoti delle
// altre versioni della generazione con lo stesso allenatore, e tiene il primo esito conforme: una carta di
// Rubino Omega non e' ricevibile in un salvataggio di Y. Scrive EVT-<gen>-<numero>-<specie>.pkN, con il
// numero del codice della checklist, e un manifesto con il contesto usato.
//
// Uso:  dotnet run -c Release -- SALVATAGGIO CARTELLA_USCITA SPECIE[/FORMA] [--copia-salvataggio PERCORSO]
//       dotnet run -c Release -- --lotto RICHIESTE.json CARTELLA_USCITA SALVATAGGIO_G6 SALVATAGGIO_G7
//       dotnet run -c Release -- --descrivi RICHIESTE.json USCITA.json SALVATAGGIO_G6 SALVATAGGIO_G7
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length == 5 && args[0] == "--descrivi")
    return Descrivi.Esegui(args[1], args[2], args[3], args[4]);
if (args.Length == 5 && args[0] == "--lotto")
    return Lotto.Esegui(args[1], args[2], args[3], args[4]);
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

static class Lotto
{
    static readonly JsonSerializerOptions Opzioni = new() { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping };

    public static int Esegui(string richieste, string cartella, string salvataggio6, string salvataggio7)
    {
        var uscita = Directory.CreateDirectory(cartella).FullName;
        var reali = new Dictionary<int, SaveFile>();
        foreach (var (gen, percorso) in new[] { (6, salvataggio6), (7, salvataggio7) })
        {
            if (!SaveUtil.TryGetSaveFile(percorso, out var s) || s.Generation != gen)
            {
                Console.Error.WriteLine($"salvataggio di generazione {gen} non valido: {percorso}");
                return 2;
            }
            reali[gen] = s;
        }
        var altreVersioni = new Dictionary<int, GameVersion[]>
        {
            [6] = [GameVersion.X, GameVersion.Y, GameVersion.OR, GameVersion.AS],
            [7] = [GameVersion.SN, GameVersion.MN, GameVersion.US, GameVersion.UM],
        };
        var basi = new Dictionary<int, MysteryGift[]>
        {
            [6] = EncounterEvent.MGDB_G6.Where(g => g.IsEntity && g.Species != 0).ToArray<MysteryGift>(),
            [7] = EncounterEvent.MGDB_G7.Where(g => g.IsEntity && g.Species != 0).ToArray<MysteryGift>(),
        };
        var voci = new JsonObject();
        var conteggi = new Dictionary<string, int>();
        foreach (var r in JsonNode.Parse(File.ReadAllText(richieste))!["voci"]!.AsArray())
        {
            var codice = (string)r!["codice"]!;
            int gen = (int)r["generazione"]!, ordinale = (int)r["ordinale"]!, specie = (int)r["specie"]!, forma = (int)r["forma"]!;
            var voce = new JsonObject { ["codice"] = codice, ["specie"] = specie, ["forma"] = forma };
            string esito;
            var base_ = basi[gen];
            if (ordinale >= base_.Length || base_[ordinale].Species != specie || base_[ordinale].Form != forma)
            {
                esito = "carta non corrispondente";
                voce["trovata"] = ordinale < base_.Length ? $"{base_[ordinale].Species}/{base_[ordinale].Form}" : "fuori dalla base";
            }
            else
            {
                var carta = base_[ordinale];
                voce["carta"] = carta.CardID;
                voce["titolo"] = carta.CardTitle;
                var reale = reali[gen];
                var contesti = new List<SaveFile> { reale };
                contesti.AddRange(altreVersioni[gen].Where(v => v != reale.Version)
                    .Select(v => BlankSaveFile.Get(v, reale.OT, (LanguageID)reale.Language)));
                esito = "contestato in ogni contesto";
                var tentati = new JsonArray();
                foreach (var contesto in contesti)
                {
                    ParseSettings.InitFromSaveFileData(contesto);
                    PKM pk;
                    try { pk = carta.ConvertToPKM(contesto); }
                    catch (Exception e) { tentati.Add($"{contesto.Version}: errore {e.Message}"); continue; }
                    var la = new LegalityAnalysis(pk);
                    // Un uovo ricevuto da un dono si fa schiudere prima di trasferirlo, come farebbe il gioco;
                    // la libreria contesta alle uova non schiuse la data d'incontro, e la schiusa la assegna.
                    if (!la.Valid && pk.IsEgg)
                    {
                        pk.ForceHatchPKM(contesto);
                        la = new LegalityAnalysis(pk);
                        voce["schiuso"] = true;
                    }
                    if (!la.Valid)
                    {
                        var prima = la.Report("en").Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).FirstOrDefault(x => x.Contains("Invalid")) ?? "contestato";
                        tentati.Add($"{contesto.Version}: {prima}");
                        continue;
                    }
                    var dati = new byte[pk.SIZE_STORED];
                    pk.WriteDecryptedDataStored(dati);
                    var nome = $"{codice}-{pk.Species:000}.{pk.Extension}";
                    File.WriteAllBytes(Path.Combine(uscita, nome), dati);
                    voce["file"] = nome;
                    voce["sha256"] = Convert.ToHexStringLower(SHA256.HashData(dati));
                    voce["contesto"] = $"{contesto.Version} {(LanguageID)contesto.Language}{(ReferenceEquals(contesto, reale) ? "" : ", salvataggio vuoto")}";
                    voce["allenatore"] = pk.OriginalTrainerName;
                    esito = "conforme";
                    break;
                }
                if (tentati.Count > 0)
                    voce["tentativi_scartati"] = tentati;
            }
            voce["esito"] = esito;
            conteggi[esito] = conteggi.GetValueOrDefault(esito) + 1;
            voci[codice] = voce;
        }
        var manifesto = new JsonObject
        {
            ["fonte"] = "EncounterEvent.MGDB_G6 e MGDB_G7 di PKHeX.Core, tramite tools/pkhex-dono --lotto (ADR-081)",
            ["richieste"] = Path.GetFileName(richieste),
            ["contesti_reali"] = new JsonObject { ["6"] = $"{reali[6].Version} {(LanguageID)reali[6].Language}", ["7"] = $"{reali[7].Version} {(LanguageID)reali[7].Language}" },
            ["conteggi"] = JsonSerializer.SerializeToNode(conteggi),
            ["voci"] = voci,
        };
        File.WriteAllText(Path.Combine(uscita, "manifesto.json"), manifesto.ToJsonString(Opzioni) + "\n");
        Console.WriteLine(string.Join(", ", conteggi.Select(kv => $"{kv.Key} {kv.Value}")) + $"; scritto {uscita}");
        return 0;
    }
}
