// Scrive gli esemplari dei lotti nei box di una COPIA di un salvataggio, con la libreria del verificatore compilata
// dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. ADR-092 ha tolto dalla catena il Parco Amici e il Trasferimento: gli esemplari si convertono con la
// libreria nel formato del salvataggio di destinazione, sesta generazione per Rubino Omega e settima per Ultrasole, e
// si scrivono nei suoi box, da cui il proprietario li porta nella banca e nel deposito. La verifica di ADR-092 ha dato
// 1598 conformi su 1598 nel contesto di Rubino Omega, a condizione di rendere l'esemplare proprio del salvataggio con
// `SaveFile.AdaptToSaveFile` dopo `EntityConverter.ConvertToType`, come il gioco fa quando lo riceve.
//
// Che cosa fa. Legge in ordine i file dei lotti indicati, salta i primi DA, e ne prende al massimo quanti ne stanno.
// Per ciascuno: converte, adatta, giudica; esclude e mette a rapporto chi e' contestato e chi, nato prima della sesta
// generazione, conosce una macchina nascosta, perche' ADR-046 lascia quella decisione al proprietario. Scrive i
// conformi in ordine nei posti del deposito, salva la copia, la ricarica, confronta ogni posto byte per byte con cio'
// che si voleva scrivere e rigiudica ogni esemplare riletto. Il salvataggio di partenza non viene mai modificato, e la
// copia non si scrive se esiste gia'. Con --svuota i box della copia si svuotano prima: gli esemplari che il
// salvataggio di partenza conteneva restano soltanto nel file di partenza.
//
// Per `rules/hardware-and-perimeter.md` la copia si porta sulla console solo dopo una copia di riserva del salvataggio
// che la console ha, e dopo la scrittura si rilegge.
//
// Uso:  dotnet run -c Release -- SALVATAGGIO COPIA_DI_USCITA DA [--svuota] [--epoca-cartucce] [--includi-mn] [--solo-mn] [--solo-epoca-cartucce] [--solo-stesso-formato] LOTTO [LOTTO ...]
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

var opzioni = args.Where(a => a.StartsWith("--")).ToHashSet();
var posizionali = args.Where(a => !a.StartsWith("--")).ToArray();
if (posizionali.Length < 4)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- SALVATAGGIO COPIA_DI_USCITA DA [--svuota] [--epoca-cartucce] [--includi-mn] [--solo-mn] [--solo-epoca-cartucce] [--solo-stesso-formato] LOTTO [LOTTO ...]");
    return 2;
}
var partenza = posizionali[0];
var copia = posizionali[1];
int da = int.Parse(posizionali[2]);
var lotti = posizionali.Skip(3).ToArray();
if (File.Exists(copia))
{
    Console.Error.WriteLine($"la copia esiste gia', non la sovrascrivo: {copia}");
    return 2;
}
if (!SaveUtil.TryGetSaveFile(partenza, out var sav))
{
    Console.Error.WriteLine($"salvataggio non riconosciuto: {partenza}");
    return 2;
}
void Contesto(SaveFile s)
{
    ParseSettings.InitFromSaveFileData(s);
    // Gli eventi da cartuccia di prima e seconda generazione la libreria li ammette solo nell'epoca delle cartucce,
    // che e' il caso di un salvataggio di cartuccia portato sulla Console Virtuale (ADR-092).
    if (opzioni.Contains("--epoca-cartucce") || opzioni.Contains("--solo-epoca-cartucce"))
        ParseSettings.AllowEraCartGB = true;
}
Contesto(sav);
var formato = sav.PKMType;

// Le macchine nascoste, misurate sul passaggio che l'esemplare avrebbe dovuto attraversare, con il criterio di
// `pokedex-home-completo/CATENA-DI-TRASFERIMENTO.md` e di `tools/mosse-mn.py`: per la prima e la seconda generazione il
// Trasferitore dalla Console Virtuale, per la terza il Parco Amici e poi il Trasferimento, per la quarta il
// Trasferimento partendo da Diamante, Perla e Platino oppure da HeartGold e SoulSilver, con l'eccezione di Nebbia e
// Mulinello, che sono macchine nascoste in una sola delle due famiglie. La quinta generazione non ha un blocco
// documentato. ADR-046 lascia la scelta al proprietario, e ADR-092 la riapre per questa via che quei passaggi non li
// attraversa: fino alla decisione le voci si escludono, e con --includi-mn si scrivono.
ushort[] mn1 = [15, 19, 57, 70, 148], mn2 = [15, 19, 57, 70, 148, 250, 127];
ushort[] mn3 = [15, 19, 57, 70, 148, 249, 127, 291];
ushort[] mnDPPt = [15, 19, 57, 70, 432, 249, 127, 431], mnHGSS = [15, 19, 57, 70, 250, 249, 127, 431];
string? Bloccato(PKM pk)
{
    bool Ha(ushort[] l) => pk.Moves.Any(m => l.Contains(m));
    return pk.Generation switch
    {
        1 when Ha(mn1) => "Trasferitore dalla Console Virtuale",
        2 when Ha(mn2) => "Trasferitore dalla Console Virtuale",
        3 when Ha(mn3) => "Parco Amici",
        3 when Ha(mnDPPt) && Ha(mnHGSS) => "Trasferimento",
        4 when Ha(mnDPPt) && Ha(mnHGSS) => "Trasferimento",
        _ => null,
    };
}
var estensioni = new[] { ".pk1", ".pk2", ".pk3", ".pk4", ".pk5", ".pk6", ".pk7", ".ck3", ".xk3" };
var file = lotti.SelectMany(l => Directory.EnumerateFiles(l).Where(f => estensioni.Contains(Path.GetExtension(f).ToLowerInvariant()))
        .Order(StringComparer.Ordinal).Select(f => (Lotto: Path.GetFileName(l.TrimEnd('/', '\\')), File: f)))
    .ToList();

if (opzioni.Contains("--svuota"))
    for (int i = 0; i < sav.SlotCount; i++)
        sav.SetBoxSlotAtIndex(sav.BlankPKM, i);
var liberi = Enumerable.Range(0, sav.SlotCount).Where(i => sav.GetBoxSlotAtIndex(i).Species == 0).ToList();

var scritti = new List<(int Posto, PKM Pk, byte[] Dati, string Origine)>();
var esclusi = new JsonArray();
int indice = 0, considerati = da;
foreach (var (lotto, percorso) in file)
{
    if (indice++ < da) continue;
    if (scritti.Count >= liberi.Count) { indice--; break; }
    considerati = indice;
    var origine = lotto + "/" + Path.GetFileName(percorso);
    if (!FileUtil.TryGetPKM(File.ReadAllBytes(percorso), out var pk, Path.GetExtension(percorso)))
    {
        esclusi.Add(new JsonObject { ["file"] = origine, ["motivo"] = "illeggibile" });
        continue;
    }
    // --solo-stesso-formato scrive soltanto gli esemplari gia' nel formato del salvataggio: un lotto che mescola doni di
    // sesta e settima generazione va in due giochi, e senza questo filtro i doni di sesta sarebbero finiti, convertiti,
    // anche nella copia di settima, doppioni di quelli di Rubino Omega.
    if (opzioni.Contains("--solo-stesso-formato") && pk.GetType() != formato)
        continue;
    // --solo-mn scrive soltanto le voci con macchina nascosta, per il caricamento a parte deciso il 2026-09-30.
    if (opzioni.Contains("--solo-mn") && Bloccato(pk) is null)
        continue;
    if (!opzioni.Contains("--includi-mn") && !opzioni.Contains("--solo-mn") && Bloccato(pk) is { } passaggio)
    {
        esclusi.Add(new JsonObject { ["file"] = origine, ["motivo"] = "macchina nascosta, ADR-046", ["passaggio"] = passaggio });
        continue;
    }
    var convertito = pk.GetType() == formato ? pk.Clone() : EntityConverter.ConvertToType(pk, formato, out var esitoConversione);
    if (convertito is null)
    {
        esclusi.Add(new JsonObject { ["file"] = origine, ["motivo"] = "conversione rifiutata" });
        continue;
    }
    // La libreria giudica l'esemplare e non il gioco che lo riceve: il 2026-09-30 Poipole e Zeraora, specie di
    // Ultrasole e Ultraluna, scritti in una copia di Luna, sono apparsi in gioco come un uovo di livello 43 e uno
    // Zeraora con l'immagine di Bulbasaur. Una specie o una forma che il gioco di destinazione non conosce si esclude.
    if (!sav.Personal.IsPresentInGame(convertito.Species, convertito.Form))
    {
        esclusi.Add(new JsonObject { ["file"] = origine, ["motivo"] = "specie o forma assente nel gioco di destinazione" });
        continue;
    }
    sav.AdaptToSaveFile(convertito, false);
    // --solo-epoca-cartucce scrive soltanto gli esemplari di Game Boy che sono legali nell'epoca delle cartucce e non
    // in quella della Console Virtuale, cioe' gli eventi da cartuccia: PKHeX, aprendo un salvataggio di settima
    // generazione, li giudica nella seconda e li segna come non legali. Sono il secondo caricamento a parte.
    if (opzioni.Contains("--solo-epoca-cartucce"))
    {
        ParseSettings.AllowEraCartGB = false;
        bool legaleInVc = new LegalityAnalysis(convertito).Valid;
        ParseSettings.AllowEraCartGB = true;
        if (legaleInVc)
            continue;
    }
    var la = new LegalityAnalysis(convertito);
    // Un uovo contestato si fa schiudere nel salvataggio che lo riceve, come farebbe il gioco, con la stessa regola di
    // `tools/pkhex-dono`: il 2026-09-30 sessanta doni in uovo di sesta generazione erano contestati in Rubino Omega
    // per il detentore, perche' un uovo non schiuso non ha ancora l'allenatore del salvataggio.
    if (!la.Valid && convertito.IsEgg)
    {
        convertito.ForceHatchPKM(sav);
        sav.AdaptToSaveFile(convertito, false);
        la = new LegalityAnalysis(convertito);
    }
    if (!la.Valid)
    {
        esclusi.Add(new JsonObject { ["file"] = origine, ["motivo"] = "contestato", ["rapporto"] = la.Report() });
        continue;
    }
    var posto = liberi[scritti.Count];
    sav.SetBoxSlotAtIndex(convertito, posto);
    var letto = sav.GetBoxSlotAtIndex(posto);
    var dati = new byte[letto.SIZE_STORED];
    letto.WriteDecryptedDataStored(dati);
    scritti.Add((posto, letto, dati, origine));
}

Directory.CreateDirectory(Path.GetDirectoryName(Path.GetFullPath(copia))!);
File.WriteAllBytes(copia, sav.Write().ToArray());

// La rilettura: la copia si ricarica da disco e ogni posto si confronta con cio' che si voleva scrivere.
SaveUtil.TryGetSaveFile(copia, out var riletto);
Contesto(riletto!);
var voci = new JsonArray();
int differenti = 0, contestatiRiletti = 0;
foreach (var (posto, _, dati, origine) in scritti)
{
    var r = riletto!.GetBoxSlotAtIndex(posto);
    var byteLetti = new byte[r.SIZE_STORED];
    r.WriteDecryptedDataStored(byteLetti);
    bool uguali = byteLetti.AsSpan().SequenceEqual(dati);
    bool valido = new LegalityAnalysis(r).Valid;
    if (!uguali) differenti++;
    if (!valido) contestatiRiletti++;
    voci.Add(new JsonObject
    {
        ["box"] = posto / sav.BoxSlotCount + 1, ["posto"] = posto % sav.BoxSlotCount + 1, ["origine"] = origine,
        ["specie"] = r.Species, ["forma"] = r.Form,
        ["sha256"] = Convert.ToHexStringLower(SHA256.HashData(byteLetti)), ["riletto_uguale"] = uguali, ["conforme"] = valido,
    });
}
int prossimo = considerati;
var rapporto = new JsonObject
{
    ["fonte"] = "PKHeX.Core tramite tools/pkhex-scrivi-salvataggio (ADR-092)",
    ["partenza"] = Path.GetFileName(partenza), ["versione"] = sav.Version.ToString(), ["formato"] = formato.Name,
    ["svuotato"] = opzioni.Contains("--svuota"), ["incluse_mn"] = opzioni.Contains("--includi-mn"), ["epoca_cartucce"] = opzioni.Contains("--epoca-cartucce"),
    ["lotti"] = new JsonArray(lotti.Select(l => (JsonNode)Path.GetFileName(l.TrimEnd('/', '\\'))).ToArray()),
    ["da"] = da, ["file_totali"] = file.Count, ["prossimo_da"] = prossimo < file.Count ? prossimo : null,
    ["scritti"] = scritti.Count, ["riletti_diversi"] = differenti, ["riletti_contestati"] = contestatiRiletti,
    ["esclusi"] = esclusi, ["voci"] = voci,
};
File.WriteAllText(copia + ".rapporto.json", rapporto.ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"{formato.Name} in {sav.Version}: scritti {scritti.Count} su {liberi.Count} posti liberi, esclusi {esclusi.Count}, riletti diversi {differenti}, riletti contestati {contestatiRiletti}");
Console.WriteLine(prossimo < file.Count ? $"restano file: il prossimo giro parte da {prossimo}" : "tutti i file dei lotti sono stati considerati");
return differenti == 0 && contestatiRiletti == 0 ? 0 : 1;
