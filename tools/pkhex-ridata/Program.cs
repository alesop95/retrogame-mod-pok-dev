// La riscrittura della data dei doni da carta dentro la finestra dell'evento, sulla libreria del verificatore compilata
// dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il 2026-11-16 il proprietario ha deciso di rigenerare ogni dono da carta la cui data di incontro sta
// fuori dalla finestra dell'evento, con un giorno diverso per ciascuno (`pending.md`, voce «AL 2026-11-16, terza
// parte»). `tools/piano-ridata.py` sceglie la finestra di ogni esemplare; questo strumento legge l'esemplare dalla copia
// che e' gia' passata a HOME, cambia soltanto cio' che serve e lo giudica, cosi' che l'esemplare rigenerato sia lo
// stesso salvo la data: stesso PID, stessa EC, stessi IV, stesse mosse, stessa storia.
//
// Che cosa fa. Per ogni voce del piano carica la copia, prende l'esemplare dal suo box e posto e ne confronta
// l'impronta (SHA-256 dei byte decifrati, come `tools/pkhex-elenco-copie`). Il campo da riscrivere e' la data
// dell'uovo se l'esemplare e' nato da un uovo, perche' per un dono in forma d'uovo la data dell'evento e' quella in cui
// l'uovo si riceve, e la data d'incontro e' la schiusa; altrimenti la data d'incontro. Se il campo sta gia' in una delle
// finestre e il gioco d'origine non cambia, l'esemplare resta com'e'. Altrimenti il giorno nuovo si sceglie in una delle
// finestre con un numero derivato dall'impronta, quindi diverso da esemplare a esemplare e uguale a ogni corsa; una
// finestra senza fine vale per un anno dal suo inizio. Per un uovo la schiusa si pone da zero a sei giorni dopo. Se il
// piano lo chiede, il gioco d'origine diventa quello precedente della stessa generazione. L'esemplare si giudica nel
// contesto della copia, e si tiene solo se resta conforme e se la libreria vi riconosce ancora la stessa carta.
//
// Scrive gli esemplari tenuti in USCITA/pk6 e USCITA/pk7, secondo il formato, con il nome GRUPPO-bBOX-pPOSTO-SPECIE, e
// USCITA/manifesto.json con ogni voce, data vecchia e nuova, campo, finestra, esito e motivo. La cartella di uscita non
// deve contenere esemplari. Le copie non vengono mai modificate.
//
// Uso:  dotnet run -c Release -- PIANO.json USCITA
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length != 2)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- PIANO.json USCITA");
    return 2;
}
var uscita = Directory.CreateDirectory(args[1]).FullName;
if (Directory.EnumerateFiles(uscita, "*.pk?", SearchOption.AllDirectories).Any())
{
    Console.Error.WriteLine($"rifiuto: {uscita} contiene gia' file di esemplare");
    return 1;
}
var piano = JsonNode.Parse(File.ReadAllText(args[0]))!.AsArray();
var copie = new Dictionary<string, SaveFile>();
var manifesto = new JsonArray();
var conti = new Dictionary<string, int>();
void Conta(string esito) => conti[esito] = conti.GetValueOrDefault(esito) + 1;

static uint Numero(string impronta, int da) => Convert.ToUInt32(impronta.Substring(da, 8), 16);

foreach (var v in piano)
{
    var voce = v!.AsObject();
    string gruppo = (string)voce["gruppo"]!, percorso = (string)voce["copia"]!, impronta = (string)voce["impronta"]!;
    int box = (int)voce["box"]!, posto = (int)voce["posto"]!;
    var esito = new JsonObject { ["gruppo"] = gruppo, ["box"] = box, ["posto"] = posto, ["specie"] = (string)voce["specie"]!, ["impronta"] = impronta };
    manifesto.Add(esito);
    if (!copie.TryGetValue(percorso, out var sav))
    {
        if (!SaveUtil.TryGetSaveFile(percorso, out sav))
        {
            Console.Error.WriteLine($"salvataggio non letto: {percorso}");
            return 1;
        }
        copie[percorso] = sav;
    }
    ParseSettings.InitFromSaveFileData(sav);
    var pk = sav.GetBoxSlotAtIndex(box - 1, posto - 1);
    if (Convert.ToHexString(SHA256.HashData(pk.Data)).ToLowerInvariant() != impronta)
    {
        esito["esito"] = "impronta diversa"; Conta("impronta diversa");
        continue;
    }
    var prima = new LegalityAnalysis(pk);
    int cartaPrima = prima.EncounterMatch is MysteryGift g0 ? g0.CardID : -1;
    bool uovo = pk.WasEgg;
    DateOnly? vecchia = uovo ? pk.EggMetDate : pk.MetDate;
    esito["campo"] = uovo ? "data dell'uovo" : "data di incontro";
    esito["data_vecchia"] = vecchia?.ToString("yyyy-MM-dd");
    esito["data_incontro_vecchia"] = pk.MetDate?.ToString("yyyy-MM-dd");
    var finestre = voce["finestre"]!.AsArray()
        .Select(f => (a: DateOnly.Parse((string)f![0]!), b: DateOnly.Parse((string)f[1]!))).ToList();
    var versioneNuova = (string?)voce["versione_nuova"];
    if (finestre.Count == 0)
    {
        esito["esito"] = "senza finestra"; Conta("senza finestra");
        continue;
    }
    // una data uguale alla data di ricezione reale di una copia della stessa carta, estratta da un giocatore, e'
    // autentica anche quando le liste danno una finestra diversa o incompleta
    var reali = voce["date_reali"]?.AsArray().Select(x => DateOnly.Parse((string)x!)).ToHashSet() ?? [];
    bool dentro = vecchia is { } d0 && (finestre.Any(f => f.a <= d0 && d0 <= f.b) || reali.Contains(d0));
    if (dentro && versioneNuova is null)
    {
        esito["esito"] = "gia' dentro"; Conta("gia' dentro");
        continue;
    }
    var nuovo = pk.Clone();
    var (inizio, fine) = finestre[(int)(Numero(impronta, 0) % (uint)finestre.Count)];
    if (fine > inizio.AddDays(365))
        fine = inizio.AddDays(365);
    int ampiezza = fine.DayNumber - inizio.DayNumber + 1;
    var giorno = inizio.AddDays((int)(Numero(impronta, 8) % (uint)ampiezza));
    if (dentro && vecchia is { } d1)
        giorno = d1; // cambia solo il gioco d'origine
    if (uovo)
    {
        nuovo.EggMetDate = giorno;
        nuovo.MetDate = giorno.AddDays((int)(Numero(impronta, 16) % 7));
    }
    else
        nuovo.MetDate = giorno;
    if (versioneNuova is not null)
        nuovo.Version = Enum.Parse<GameVersion>(versioneNuova);
    nuovo.RefreshChecksum();
    var dopo = new LegalityAnalysis(nuovo);
    int cartaDopo = dopo.EncounterMatch is MysteryGift g1 ? g1.CardID : -1;
    esito["data_nuova"] = giorno.ToString("yyyy-MM-dd");
    esito["data_incontro_nuova"] = nuovo.MetDate?.ToString("yyyy-MM-dd");
    esito["finestra"] = new JsonArray(inizio.ToString("yyyy-MM-dd"), fine.ToString("yyyy-MM-dd"));
    esito["versione"] = nuovo.Version.ToString();
    esito["carta_prima"] = cartaPrima;
    esito["carta_dopo"] = cartaDopo;
    if (!dopo.Valid || cartaDopo != cartaPrima)
    {
        esito["esito"] = dopo.Valid ? "carta riconosciuta diversa" : "contestato";
        esito["rapporto"] = dopo.Report();
        Conta((string)esito["esito"]!);
        continue;
    }
    var formato = nuovo.Format == 6 ? "pk6" : "pk7";
    var nome = $"{gruppo}-b{box:00}-p{posto:00}-{nuovo.Species:000}.{formato}";
    var cartella = Directory.CreateDirectory(Path.Combine(uscita, formato)).FullName;
    var dati = new byte[nuovo.SIZE_STORED];
    nuovo.WriteDecryptedDataStored(dati);
    File.WriteAllBytes(Path.Combine(cartella, nome), dati);
    esito["file"] = $"{formato}/{nome}";
    esito["impronta_nuova"] = Convert.ToHexString(SHA256.HashData(nuovo.Data)).ToLowerInvariant();
    esito["esito"] = "riscritto"; Conta("riscritto");
}
File.WriteAllText(Path.Combine(uscita, "manifesto.json"), new JsonObject
{
    ["piano"] = Path.GetFullPath(args[0]),
    ["libreria"] = typeof(SaveFile).Assembly.GetName().Version?.ToString(),
    ["conti"] = new JsonObject(conti.Select(kv => KeyValuePair.Create(kv.Key, (JsonNode?)kv.Value))),
    ["voci"] = manifesto,
}.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
Console.WriteLine(string.Join(", ", conti.OrderByDescending(kv => kv.Value).Select(kv => $"{kv.Key} {kv.Value}")));
return 0;
