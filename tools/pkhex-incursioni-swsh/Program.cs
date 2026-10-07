// Le incursioni di evento di Spada e Scudo, cioè le tane di distribuzione delle Wild Area News, censite dalla libreria del
// verificatore compilata dal clone in _notes/fonti/cloni/pkhex, confrontate con la pagina Bulbapedia del 2021 e con i lotti
// già prodotti, e generate dove mancano.
//
// Perché esiste. ADR-097 (2026-10-06): il proprietario ha stabilito che gli esemplari delle incursioni di evento di Spada e
// Scudo, cromatici e Gigantamax compresi, contano come esemplari da distribuzione. Il lotto lotto-eventi-switch-scelta ne
// teneva uno per specie e forma, e quindi non distingueva il Gigantamax né il cromatico garantito, che sono proprio ciò
// che rende peculiare un'incursione di evento.
//
// Che cosa legge. Le tabelle Dist_SW e Dist_SH di Encounters8Nest (classe EncounterStatic8ND), interne alla libreria e
// raggiunte per riflessione: ogni riga porta l'indice dell'evento, specie, forma, abilità, livello, livello Dynamax,
// fattore Gigantamax, blocco o garanzia del cromatico, IV perfetti e mosse. Le grotte di cristallo (EncounterStatic8NC)
// sono incursioni permanenti e stanno nel dump solo come riferimento. Per dire se una voce esiste anche fuori dagli eventi
// legge per riflessione tutte le altre tabelle di Encounters8 e Encounters8Nest: tane ordinarie, statici, cristallo,
// avventure Dynamax, incontri selvatici.
//
// Che cosa fa. Scrive il dump in JSON con ogni riga distinta e le versioni in cui compare. Raggruppa le righe per chiave di
// collezione, specie, forma, Gigantamax e cromatico garantito. Se riceve la pagina della Wild Area News del 2021 ne
// estrae gli eventi e le voci e le confronta con la libreria, indicando per ogni evento l'indice della libreria con più
// specie in comune. Se riceve la cartella dei lotti giudica ogni .pk8 che vi trova (salvo l'uscita) e, se l'incontro
// riconosciuto è una tana di distribuzione, segna la chiave come coperta da quel lotto. Se riceve la cartella di uscita
// genera un esemplare per ogni chiave non coperta da lotto-eventi-switch-scelta, con l'allenatore del progetto, e tiene il
// primo conforme, in una sottocartella per versione così che il giudice lo giudichi con il salvataggio vuoto giusto. La
// sottocartella porta il nome del lotto seguito dalla versione, perché pkhex-giudica chiama ogni voce del registro con la
// cartella che contiene il file, e un nome nudo come SW si confonderebbe con quello di qualunque altro lotto.
//
// Uso:  dotnet run -c Release -- ALLENATORE.json DUMP.json [WAN2021.txt] [CARTELLA_LOTTI] [CARTELLA_USCITA]
//       dotnet run -c Release -- --disponibilità DUMP.json
// La seconda forma ricalcola nel dump esistente il solo confronto con le altre fonti, senza generare né provare.
using System.Reflection;
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Text.RegularExpressions;
using PKHeX.Core;

if (args.Length < 2)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- ALLENATORE.json DUMP.json [WAN2021.txt] [CARTELLA_LOTTI] [CARTELLA_USCITA]");
    return 2;
}
// Con --disponibilità lo strumento non genera e non prova nulla: rilegge il dump esistente e ne ricalcola soltanto il
// confronto con le altre fonti, che è deterministico perché dipende dalle sole tabelle della libreria e non dal seme.
bool soloDisponibilità = args[0] == "--disponibilità";
JsonNode all = soloDisponibilità ? new JsonObject() : JsonNode.Parse(File.ReadAllText(args[0]))!;
string? wanPath = args.Length > 2 ? args[2] : null;
string? lottiPath = args.Length > 3 ? Path.GetFullPath(args[3]) : null;
string? uscitaPath = args.Length > 4 ? Path.GetFullPath(args[4]) : null;
var it = GameInfo.GetStrings("it");
var en = GameInfo.GetStrings("en");

SimpleTrainerInfo Allenatore(GameVersion v) => new(v)
{
    OT = (string)all["nome"]!, TID16 = (ushort)(int)all["tid"]!, SID16 = (ushort)(int)all["sid"]!,
    Gender = (string)all["sesso"]! == "maschio" ? (byte)0 : (byte)1, Language = (int)all["lingua"]!,
    Generation = 8, Context = EntityContext.Gen8,
};

var asm = typeof(EncounterStatic8ND).Assembly;
var nestType = asm.GetType("PKHeX.Core.Encounters8Nest")!;
var gen8Type = asm.GetType("PKHeX.Core.Encounters8")!;
const BindingFlags Tutti = BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
EncounterStatic8ND[] Tabella(string nome) => (EncounterStatic8ND[])nestType.GetField(nome, Tutti)!.GetValue(null)!;
var distSW = Tabella("Dist_SW");
var distSH = Tabella("Dist_SH");
var crystal = (EncounterStatic8NC[])nestType.GetField("Crystal_SWSH", Tutti)!.GetValue(null)!;

string FormaIt(ushort s, byte f) => FormConverter.GetStringFromForm(s, f, it, EntityContext.Gen8);
string Chiave(ushort s, byte f, bool g, bool c) => $"{s:0000}-{f}{(g ? "-G" : "")}{(c ? "-S" : "")}";
// Una riga a cromatico garantito si genera chiedendo il cromatico: la libreria non lo forza da sé, perché nelle tane
// la lucentezza viene dal seme (RaidRNG.TryApply non tocca il PID quando la riga dice Always), e un esemplare non
// cromatico nato da quella riga non vi si accorda (la libreria lo attribuisce a un'altra riga dello stesso evento o lo
// rifiuta). SetPINGA ritenta i semi finché l'esemplare non è cromatico, fino a centomila tentativi.
// All'opposto, ogni altra riga si genera chiedendo il non cromatico. Per una riga con il blocco (Never) la libreria lo
// impone da sé, perché RaidRNG.TryApply spegne la lucentezza riscrivendo il PID; per una riga libera (Random) un seme
// cromatico capita una volta su 4096, e un esemplare così porterebbe la chiave sbagliata nella collezione, che separa il
// cromatico garantito dal resto. Lo stato ottenuto si confronta comunque con quello atteso dopo la generazione, con
// AccordoCromatico, e un esemplare che non vi corrisponde non si scrive.
EncounterCriteria Criterio(EncounterStatic8ND e) => EncounterCriteria.Unrestricted with { Shiny = e.Shiny == Shiny.Always ? Shiny.Always : Shiny.Never };
bool AccordoCromatico(EncounterStatic8ND e, PKM g) => g.IsShiny == (e.Shiny == Shiny.Always);
string Firma(EncounterStatic8ND e) => $"{e.Index}|{e.Species}|{e.Form}|{e.Level}|{e.DynamaxLevel}|{e.CanGigantamax}|{e.Shiny}|{e.Ability}|{e.FlawlessIVCount}|{e.Moves.Move1},{e.Moves.Move2},{e.Moves.Move3},{e.Moves.Move4}";

// Le altre fonti di Spada e Scudo, per dire se una chiave esiste anche fuori dagli eventi.
var altreFonti = new Dictionary<string, SortedSet<string>>(); // "specie-forma-G" -> nomi delle tabelle
void AggiungiFonte(object o, string tabella)
{
    var t = o.GetType();
    var slots = t.GetProperty("Slots");
    if (slots?.GetValue(o) is System.Collections.IEnumerable figli && o is not string)
    {
        foreach (var x in figli) if (x is not null) AggiungiFonte(x, tabella);
        return;
    }
    if (t.GetProperty("Species")?.GetValue(o) is not ushort s) return;
    var f = t.GetProperty("Form")?.GetValue(o) is byte b ? b : (byte)0;
    var g = t.GetProperty("CanGigantamax")?.GetValue(o) is true;
    var k = $"{s}-{f}-{(g ? "G" : "")}";
    if (!altreFonti.TryGetValue(k, out var set)) altreFonti[k] = set = [];
    set.Add(tabella);
}
foreach (var tipo in new[] { gen8Type, nestType })
    foreach (var campo in tipo.GetFields(Tutti))
    {
        if (campo.Name is "Dist_SW" or "Dist_SH") continue;
        if (campo.GetValue(null) is not Array arr) continue;
        foreach (var o in arr) if (o is not null && o.GetType().Namespace == "PKHeX.Core") AggiungiFonte(o, campo.Name);
    }
// I doni WC8 con il fattore, solo informativi: un dono non è un'incursione.
var doniG = new HashSet<string>();
foreach (var c in EncounterEvent.MGDB_G8) if (c is WC8 w && w.IsEntity && w.CanGigantamax) doniG.Add($"{w.Species}-{w.Form}");

// La disponibilità di una chiave fuori dagli eventi. Fino al 2026-10-06 il confronto cercava soltanto la stessa terna di
// specie, forma e Gigantamax nelle altre tabelle, e dichiarava «solo da incursioni di evento» Bulbasaur e Squirtle senza
// fattore: in Spada e Scudo l'unico loro incontro è il dono del Dojo dell'Isola dell'Armatura (Encounters8.cs righe 39-40,
// luogo 196), che ha il fattore, mentre un esemplare senza fattore nasce da un uovo di quel dono, perché il fattore non si
// eredita, o dalla Zuppa Dynamax che lo toglie. Per una chiave senza fattore si cercano quindi anche la stessa specie e
// forma con il fattore e gli altri membri della famiglia evolutiva nella forma della chiave, cioè le pre-evoluzioni, da
// cui la chiave si ottiene per evoluzione, e le evoluzioni di una specie che si alleva, da cui si ottiene per uovo e poi
// per evoluzione. Una chiave con il fattore resta confrontata alla sola terna: il fattore non si ottiene da un uovo.
(string disponibilità, List<string> fonti, List<string> derivate) Disponibilità(ushort s, byte f, bool g)
{
    var fonti = altreFonti.TryGetValue($"{s}-{f}-{(g ? "G" : "")}", out var fs) ? fs.ToList() : [];
    if (fonti.Any(x => x.StartsWith("Nest_"))) return ("anche da tane ordinarie", fonti, []);
    if (fonti.Count > 0) return ("anche da altri incontri", fonti, []);
    var derivate = new SortedSet<string>(StringComparer.Ordinal);
    if (!g)
    {
        if (altreFonti.TryGetValue($"{s}-{f}-G", out var conG))
            foreach (var t in conG) derivate.Add($"{s}-{f}-G {t}");
        var albero = EvolutionTree.Evolves8;
        var membri = albero.Reverse.GetPreEvolutions(s, f).Select(x => (x.Species, x.Form, uovo: false))
            .Concat(albero.Forward.GetEvolutions(s, f).Select(x => (x.Species, x.Form, uovo: true)));
        foreach (var (ms, mf, uovo) in membri)
        {
            if (uovo)
            {
                var pi = PersonalTable.SWSH.GetFormEntry(ms, mf);
                if (pi.EggGroup1 is (int)EggGroup.Undiscovered or (int)EggGroup.Ditto) continue;
            }
            foreach (var suff in new[] { "", "G" })
                if (altreFonti.TryGetValue($"{ms}-{mf}-{suff}", out var mfs))
                    foreach (var t in mfs) derivate.Add($"{ms}-{mf}-{suff} {t}");
        }
    }
    return derivate.Count > 0
        ? ("anche per allevamento o evoluzione da altri incontri", fonti, derivate.ToList())
        : ("solo da incursioni di evento", fonti, []);
}

if (soloDisponibilità)
{
    var esistente = JsonNode.Parse(File.ReadAllText(args[1]))!;
    int nSolo = 0, nTane = 0, nAltro = 0, nDerivate = 0;
    foreach (var k in esistente["chiavi"]!.AsArray())
    {
        var (disp, fonti, derivate) = Disponibilità((ushort)(int)k!["numero"]!, (byte)(int)k["forma"]!, (bool)k["gigantamax"]!);
        k["disponibilità"] = disp;
        k["altre_fonti"] = new JsonArray(fonti.Select(x => (JsonNode)x).ToArray());
        k["derivata_da"] = new JsonArray(derivate.Select(x => (JsonNode)x).ToArray());
        switch (disp)
        {
            case "anche da tane ordinarie": nTane++; break;
            case "anche da altri incontri": nAltro++; break;
            case "solo da incursioni di evento": nSolo++; break;
            default: nDerivate++; break;
        }
    }
    var cc = esistente["conteggi"]!.AsObject();
    cc["chiavi_solo_da_eventi"] = nSolo; cc["chiavi_anche_tane_ordinarie"] = nTane; cc["chiavi_anche_altri_incontri"] = nAltro;
    cc["chiavi_anche_per_allevamento_o_evoluzione"] = nDerivate;
    File.WriteAllText(args[1], esistente.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
    Console.WriteLine($"disponibilità ricalcolata: {nTane} anche da tane ordinarie, {nAltro} anche da altri incontri, {nDerivate} per allevamento o evoluzione, {nSolo} solo da incursioni di evento");
    return 0;
}

// Le righe distinte, con le versioni in cui compaiono.
var righe = new Dictionary<string, (EncounterStatic8ND e, List<string> versioni)>();
foreach (var (tab, v) in new[] { (distSW, "SW"), (distSH, "SH") })
    foreach (var e in tab)
    {
        var k = Firma(e);
        if (!righe.TryGetValue(k, out var r)) righe[k] = r = (e, []);
        r.versioni.Add(v);
    }

// Le chiavi di collezione.
var chiavi = new SortedDictionary<string, List<(EncounterStatic8ND e, List<string> versioni)>>(StringComparer.Ordinal);
foreach (var r in righe.Values)
{
    var k = Chiave(r.e.Species, r.e.Form, r.e.CanGigantamax, r.e.Shiny == Shiny.Always);
    if (!chiavi.TryGetValue(k, out var l)) chiavi[k] = l = [];
    l.Add(r);
}

// La copertura dei lotti: un .pk8 il cui incontro riconosciuto è una tana di distribuzione copre la sua chiave.
var copertura = new Dictionary<string, SortedSet<string>>();
var indistinti = new List<string>();

// La prova di ogni riga: si genera l'esemplare e si guarda se la libreria lo riconosce come tana di distribuzione o se lo
// attribuisce a un altro incontro, tipicamente una tana ordinaria con gli stessi parametri. Nel secondo caso l'esemplare
// è legale ma non porta nulla che lo distingua come evento.
var prova = new Dictionary<string, (bool valido, bool distinto, string motivo)>();
foreach (var (k0, (e, versioni)) in righe)
{
    var v = versioni[0] == "SW" ? GameVersion.SW : GameVersion.SH;
    try
    {
        ParseSettings.InitFromSaveFileData(new SAV8SWSH { Version = v, Language = (int)all["lingua"]! });
        var g = e.ConvertToPKM(Allenatore(v), Criterio(e));
        var la = new LegalityAnalysis(g);
        if (!AccordoCromatico(e, g)) { prova[k0] = (false, false, "CromaticoNonAccordato"); continue; }
        prova[k0] = la.Valid ? (true, la.EncounterMatch is EncounterStatic8ND m && (m.Shiny == Shiny.Always) == (e.Shiny == Shiny.Always), la.EncounterMatch.LongName) : (false, false, la.Results.First(r => !r.Valid).Identifier.ToString());
    }
    catch (Exception ex) { prova[k0] = (false, false, ex.GetType().Name); }
}
JsonArray Mosse(Moveset m) => new(new[] { m.Move1, m.Move2, m.Move3, m.Move4 }.Where(x => x != 0).Select(x => (JsonNode)it.Move[x]).ToArray());
var dumpRighe = new JsonArray();
foreach (var (e, versioni) in righe.Values.OrderBy(r => r.e.Index).ThenBy(r => r.e.Species).ThenBy(r => r.e.Form).ThenBy(r => r.e.Level))
{
    dumpRighe.Add(new JsonObject
    {
        ["indice_evento"] = e.Index, ["versioni"] = new JsonArray(versioni.Select(x => (JsonNode)x).ToArray()),
        ["numero"] = e.Species, ["specie"] = it.Species[e.Species], ["specie_en"] = en.Species[e.Species],
        ["forma"] = e.Form, ["nome_forma"] = FormaIt(e.Species, e.Form), ["gigantamax"] = e.CanGigantamax,
        ["cromatico"] = e.Shiny.ToString(), ["abilita"] = e.Ability.ToString(), ["livello"] = e.Level,
        ["livello_dynamax"] = e.DynamaxLevel, ["iv_perfetti"] = e.FlawlessIVCount, ["mosse"] = Mosse(e.Moves),
        ["chiave"] = Chiave(e.Species, e.Form, e.CanGigantamax, e.Shiny == Shiny.Always),
        ["legale"] = prova[Firma(e)].valido, ["riconosciuta_come_distribuzione"] = prova[Firma(e)].distinto, ["esito_prova"] = prova[Firma(e)].motivo,
    });
}

int pk8Letti = 0;
string NomeSottocartella(GameVersion v) => Path.GetFileName(uscitaPath!.TrimEnd(Path.DirectorySeparatorChar)) + "-" + v;
const string PrefissoUscite = "lotto-incursioni-";
if (lottiPath is not null)
{
    var vuoto = new SAV8SWSH { Language = (int)all["lingua"]! };
    ParseSettings.InitFromSaveFileData(vuoto);
    foreach (var p in Directory.EnumerateFiles(lottiPath, "*.pk8", SearchOption.AllDirectories))
    {
        var full = Path.GetFullPath(p);
        if (uscitaPath is not null && full.StartsWith(uscitaPath, StringComparison.OrdinalIgnoreCase)) continue;
        // Anche le uscite delle corse precedenti di questo strumento non contano come copertura: sono ciò che il censimento
        // produce, non ciò che trova, e contarle farebbe sembrare coperta una chiave dalla sola corsa che la generava.
        if (Path.GetRelativePath(lottiPath, full).StartsWith(PrefissoUscite, StringComparison.OrdinalIgnoreCase)) continue;
        var dati = File.ReadAllBytes(p);
        if (!FileUtil.TryGetPKM(dati, out var pk, ".pk8")) continue;
        pk8Letti++;
        var la = new LegalityAnalysis(pk);
        if (!la.Valid) continue;
        string k;
        // La chiave è quella dell'esemplare, non dell'incontro: un Alcremie Gigantamax nato da un Milcery di evento con il
        // fattore è un esemplare di incursione di evento nella forma che ha.
        if (la.EncounterMatch is EncounterStatic8ND nd && pk is PK8 q) k = Chiave(pk.Species, pk.Form, q.CanGigantamax, nd.Shiny == Shiny.Always);
        // Un file nato da una tana di distribuzione che la libreria attribuisce a una tana ordinaria copre comunque la sua
        // chiave: è stato generato da quella riga, ma non se ne distingue.
        else if (Path.GetFileName(p).StartsWith("Static8ND") && pk is PK8 p8)
        {
            k = Chiave(pk.Species, pk.Form, p8.CanGigantamax, pk.IsShiny && chiavi.ContainsKey(Chiave(pk.Species, pk.Form, p8.CanGigantamax, true)));
            indistinti.Add(Path.GetRelativePath(lottiPath, full).Replace(Path.DirectorySeparatorChar, '/'));
        }
        else continue;
        var lotto = Path.GetRelativePath(lottiPath, full).Split(Path.DirectorySeparatorChar, '/')[0];
        if (!copertura.TryGetValue(k, out var set)) copertura[k] = set = [];
        set.Add(lotto);
    }
}
const string LottoScelta = "lotto-eventi-switch-scelta";

// La generazione delle chiavi non coperte dal lotto destinato a HOME.
var rapporto = new JsonArray();
int generati = 0, nonGenerati = 0;
var esito = new Dictionary<string, string>();
if (uscitaPath is not null && lottiPath is not null)
{
    Directory.CreateDirectory(uscitaPath);
    // Come gli altri generatori, non si scrive sopra un lotto: file rimasti da una corsa precedente si mescolerebbero ai
    // nuovi e il rapporto non li elencherebbe.
    if (Directory.EnumerateFiles(uscitaPath, "*.pk8", SearchOption.AllDirectories).Any())
    {
        Console.Error.WriteLine($"la cartella di uscita contiene già esemplari: {uscitaPath}");
        return 1;
    }
    foreach (var (k, lista) in chiavi)
    {
        if (copertura.TryGetValue(k, out var c) && c.Contains(LottoScelta)) continue;
        // Si preferisce la riga che la prova riconosce come distribuzione, poi quella presente in entrambe le versioni, poi
        // Spada, poi il livello più alto.
        var candidati = lista.OrderByDescending(r => prova[Firma(r.e)].distinto).ThenByDescending(r => r.versioni.Count).ThenBy(r => r.versioni[0] == "SW" ? 0 : 1).ThenByDescending(r => r.e.Level).ToList();
        string motivo = "";
        bool fatto = false;
        foreach (var (e, versioni) in candidati)
        {
            var v = versioni[0] == "SW" ? GameVersion.SW : GameVersion.SH;
            try
            {
                var vuoto = new SAV8SWSH { Version = v, Language = (int)all["lingua"]! };
                ParseSettings.InitFromSaveFileData(vuoto);
                var g = e.ConvertToPKM(Allenatore(v), Criterio(e));
                var la = new LegalityAnalysis(g);
                if (!AccordoCromatico(e, g)) { motivo = $"cromatico {(g.IsShiny ? "ottenuto" : "mancato")} su una riga {e.Shiny}"; continue; }
                if (!la.Valid) { motivo = la.Results.First(r => !r.Valid).Identifier.ToString(); continue; }
                bool distinto = la.EncounterMatch is EncounterStatic8ND m && (m.Shiny == Shiny.Always) == (e.Shiny == Shiny.Always);
                var dati = new byte[g.SIZE_STORED]; g.WriteDecryptedDataStored(dati);
                var nome = $"Static8ND-{e.Index:000}-{v}-{e.Species:0000}-{e.Form}{(e.CanGigantamax ? "-G" : "")}{(e.Shiny == Shiny.Always ? "-S" : "")}.pk8";
                var cartella = Directory.CreateDirectory(Path.Combine(uscitaPath, NomeSottocartella(v))).FullName;
                File.WriteAllBytes(Path.Combine(cartella, nome), dati);
                rapporto.Add(new JsonObject
                {
                    ["chiave"] = k, ["numero"] = e.Species, ["specie"] = it.Species[e.Species], ["forma"] = e.Form,
                    ["nome_forma"] = FormaIt(e.Species, e.Form), ["gigantamax"] = e.CanGigantamax, ["cromatico"] = g.IsShiny,
                    ["indice_evento"] = e.Index, ["versione"] = v.ToString(), ["livello"] = g.CurrentLevel, ["abilita"] = it.Ability[g.Ability],
                    ["allenatore"] = g.OriginalTrainerName, ["conforme"] = true, ["riconosciuto_come_distribuzione"] = distinto, ["incontro_riconosciuto"] = la.EncounterMatch.LongName, ["file"] = NomeSottocartella(v) + "/" + nome,
                    ["sha256"] = Convert.ToHexStringLower(SHA256.HashData(dati)),
                });
                generati++; fatto = true; esito[k] = "generato";
                break;
            }
            catch (Exception ex) { motivo = ex.GetType().Name + ": " + ex.Message; }
        }
        if (!fatto)
        {
            nonGenerati++; esito[k] = "rifiutato: " + motivo;
            rapporto.Add(new JsonObject { ["chiave"] = k, ["numero"] = lista[0].e.Species, ["specie"] = it.Species[lista[0].e.Species], ["conforme"] = false, ["motivo"] = motivo });
        }
    }
    File.WriteAllText(Path.Combine(uscitaPath, "rapporto.json"), new JsonObject
    {
        ["fonte"] = "PKHeX.Core tramite tools/pkhex-incursioni-swsh",
        ["criterio"] = "un esemplare per chiave di collezione (specie, forma, Gigantamax, cromatico garantito) delle tane di distribuzione di Spada e Scudo non coperta da lotto-eventi-switch-scelta; riga preferita: riconosciuta come distribuzione dalla prova, poi presente in entrambe le versioni, poi Spada, poi il livello più alto; cromatico solo e sempre sulle righe a cromatico garantito",
        ["esemplari"] = rapporto,
    }.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
}

var dumpChiavi = new JsonArray();
int soloEventi = 0, ancheTane = 0, ancheAltro = 0, ancheDerivate = 0;
foreach (var (k, lista) in chiavi)
{
    var e0 = lista[0].e;
    var (disponibilità, fonti, derivate) = Disponibilità(e0.Species, e0.Form, e0.CanGigantamax);
    switch (disponibilità)
    {
        case "anche da tane ordinarie": ancheTane++; break;
        case "anche da altri incontri": ancheAltro++; break;
        case "solo da incursioni di evento": soloEventi++; break;
        default: ancheDerivate++; break;
    }
    var versioni = lista.SelectMany(r => r.versioni).Distinct().Order().ToList();
    dumpChiavi.Add(new JsonObject
    {
        ["chiave"] = k, ["numero"] = e0.Species, ["specie"] = it.Species[e0.Species], ["specie_en"] = en.Species[e0.Species],
        ["forma"] = e0.Form, ["nome_forma"] = FormaIt(e0.Species, e0.Form), ["gigantamax"] = e0.CanGigantamax,
        ["cromatico_garantito"] = e0.Shiny == Shiny.Always,
        ["versioni"] = new JsonArray(versioni.Select(x => (JsonNode)x).ToArray()),
        ["indici_evento"] = new JsonArray(lista.Select(r => (int)r.e.Index).Distinct().Order().Select(x => (JsonNode)x).ToArray()),
        ["livelli"] = new JsonArray(lista.Select(r => (int)r.e.Level).Distinct().Order().Select(x => (JsonNode)x).ToArray()),
        ["righe"] = lista.Count, ["disponibilità"] = disponibilità,
        ["distinguibile_da_tana_ordinaria"] = lista.Any(r => prova[Firma(r.e)].distinto),
        ["righe_legali"] = lista.Count(r => prova[Firma(r.e)].valido),
        ["altre_fonti"] = new JsonArray(fonti.Select(x => (JsonNode)x).ToArray()),
        ["derivata_da"] = new JsonArray(derivate.Select(x => (JsonNode)x).ToArray()),
        ["dono_wc8_con_fattore"] = e0.CanGigantamax && doniG.Contains($"{e0.Species}-{e0.Form}"),
        ["coperta_da"] = new JsonArray((copertura.TryGetValue(k, out var cs) ? cs.ToList() : []).Select(x => (JsonNode)x).ToArray()),
        ["generazione"] = esito.TryGetValue(k, out var es) ? es : null,
    });
}

// Il confronto con la Wild Area News del 2021.
JsonObject? confronto = null;
if (wanPath is not null)
{
    var linee = File.ReadAllLines(wanPath).Select(l => l.Trim()).ToArray();
    var data = new Regex(@"^(January|February|March|April|May|June|July|August|September|October|November|December) \d.*\d{4}$");
    int inizio = Array.FindIndex(linee, l => l == "Contents");
    var toc = new HashSet<string>();
    int i0 = Array.FindIndex(linee, l => l == "(Return to top)");
    for (int i = i0 + 1; i < linee.Length && linee[i] != "References"; i++) toc.Add(linee[i]);
    int corpo = Array.FindIndex(linee, i0 + 1, l => l == "References") + 1;
    var nomiEn = en.Species.Select((n, idx) => (n, idx)).Where(x => x.idx > 0).ToDictionary(x => x.n, x => (ushort)x.idx);
    var eventi = new List<(string titolo, List<(ushort s, byte f, bool g, bool c, string stelle, string testo)> voci)>();
    string stelle = "";
    for (int i = corpo; i < linee.Length && linee[i] != "References"; i++)
    {
        var l = linee[i];
        if (toc.Contains(l) && data.IsMatch(l) && i + 1 < linee.Length && (linee[i + 1].StartsWith("Wild Area News banner") || linee[i + 1].StartsWith("This")))
        { eventi.Add((l, [])); stelle = ""; continue; }
        if (eventi.Count == 0) continue;
        if (l.Length > 0 && l.All(ch => ch == '★')) { stelle = l; continue; }
        if (stelle == "" || !nomiEn.TryGetValue(l, out var s)) continue;
        var prev = linee[i - 1];
        if (!(prev == stelle || prev.EndsWith('%') || prev == "Rate")) continue;
        var mod = new List<string>();
        int j = i + 1;
        while (j < linee.Length && linee[j] is not ("Sw" or "Sh") && j - i < 5) mod.Add(linee[j++]);
        if (j >= linee.Length || linee[j] is not ("Sw" or "Sh")) continue;
        bool g = mod.Any(m => m.StartsWith("Gigantamax"));
        bool c = mod.Contains("Shiny");
        byte f = 0;
        foreach (var m in mod.Where(m => m is not ("Shiny" or "Gigantamax" or "Gigantamax Factor")))
        {
            if (m == "Female") { f = 1; continue; }
            var tok = m.Replace(en.Species[s], "").Replace("Form", "").Replace("Alolan", "Alola").Replace("Galarian", "Galar").Trim();
            var lista = FormConverter.GetFormList(s, en.Types, en.forms, EntityContext.Gen8);
            for (byte x = 0; x < lista.Length; x++) if (tok.Length > 0 && lista[x].Contains(tok, StringComparison.OrdinalIgnoreCase)) { f = x; break; }
        }
        eventi[^1].voci.Add((s, f, g, c, stelle, $"{l}{(mod.Count > 0 ? " (" + string.Join(", ", mod) + ")" : "")}"));
    }
    // Gli insiemi di specie per indice della libreria.
    var perIndice = righe.Values.GroupBy(r => r.e.Index).ToDictionary(gr => gr.Key, gr => gr.Select(r => (r.e.Species, r.e.Form)).ToHashSet());
    var eventiJson = new JsonArray();
    int vociTot = 0, vociTrovate = 0, eventiConVoci = 0;
    foreach (var (titolo, voci) in eventi)
    {
        var insieme = voci.Select(v => (v.s, v.f)).ToHashSet();
        int? migliore = null; double jac = 0;
        foreach (var (idx, set) in perIndice)
        {
            if (insieme.Count == 0) break;
            var inter = set.Intersect(insieme).Count();
            var j2 = (double)inter / set.Union(insieme).Count();
            if (j2 > jac) { jac = j2; migliore = idx; }
        }
        var vj = new JsonArray();
        foreach (var v in voci.DistinctBy(v => (v.s, v.f, v.g, v.c)))
        {
            var k = Chiave(v.s, v.f, v.g, v.c);
            bool inLib = chiavi.ContainsKey(k);
            bool inIdx = migliore is not null && righe.Values.Any(r => r.e.Index == migliore && Chiave(r.e.Species, r.e.Form, r.e.CanGigantamax, r.e.Shiny == Shiny.Always) == k);
            vociTot++; if (inLib) vociTrovate++;
            vj.Add(new JsonObject { ["voce"] = v.testo, ["chiave"] = k, ["nella_libreria"] = inLib, ["nell_indice_migliore"] = inIdx });
        }
        if (voci.Count > 0) eventiConVoci++;
        eventiJson.Add(new JsonObject { ["evento"] = titolo, ["indice_migliore"] = migliore, ["somiglianza"] = Math.Round(jac, 3), ["voci"] = vj });
    }
    confronto = new JsonObject
    {
        ["fonte"] = Path.GetFileName(wanPath), ["eventi"] = eventi.Count, ["eventi_con_tabella"] = eventiConVoci,
        ["voci_distinte"] = vociTot, ["voci_nella_libreria"] = vociTrovate, ["dettaglio"] = eventiJson,
    };
}

var dump = new JsonObject
{
    ["fonte"] = "PKHeX.Core, Encounters8Nest.Dist_SW e Dist_SH (EncounterStatic8ND), tramite tools/pkhex-incursioni-swsh",
    ["nota"] = "Generato. Una riga è un incontro distinto delle tabelle di distribuzione, con le versioni in cui compare. Una chiave è specie, forma, Gigantamax (G) e cromatico garantito (S). Il livello è quello della tana; la libreria ammette anche i livelli ribassati da 20 a 55 a passi di 5 nelle tane condivise.",
    ["conteggi"] = new JsonObject
    {
        ["righe_spada"] = distSW.Length, ["righe_scudo"] = distSH.Length, ["righe_distinte"] = righe.Count,
        ["righe_solo_spada"] = righe.Values.Count(r => r.versioni.SequenceEqual(["SW"])),
        ["righe_solo_scudo"] = righe.Values.Count(r => r.versioni.SequenceEqual(["SH"])),
        ["indici_evento"] = righe.Values.Select(r => r.e.Index).Distinct().Count(),
        ["chiavi"] = chiavi.Count,
        ["chiavi_specie_forma_gigantamax"] = chiavi.Values.Select(l => (l[0].e.Species, l[0].e.Form, l[0].e.CanGigantamax)).Distinct().Count(),
        ["chiavi_specie_forma"] = chiavi.Values.Select(l => (l[0].e.Species, l[0].e.Form)).Distinct().Count(),
        ["chiavi_gigantamax"] = chiavi.Values.Count(l => l[0].e.CanGigantamax),
        ["chiavi_cromatico_garantito"] = chiavi.Values.Count(l => l[0].e.Shiny == Shiny.Always),
        ["chiavi_solo_da_eventi"] = soloEventi, ["chiavi_anche_tane_ordinarie"] = ancheTane, ["chiavi_anche_altri_incontri"] = ancheAltro,
        ["chiavi_anche_per_allevamento_o_evoluzione"] = ancheDerivate,
        ["righe_legali"] = prova.Values.Count(x => x.valido), ["righe_riconosciute_come_distribuzione"] = prova.Values.Count(x => x.distinto),
        ["chiavi_distinguibili"] = chiavi.Values.Count(l => l.Any(r => prova[Firma(r.e)].distinto)),
        ["pk8_letti_nei_lotti"] = pk8Letti, ["file_static8nd_attribuiti_a_tana_ordinaria"] = indistinti.Count,
        ["chiavi_coperte_da_scelta"] = chiavi.Keys.Count(k => copertura.TryGetValue(k, out var c) && c.Contains(LottoScelta)),
        ["chiavi_coperte_da_qualunque_lotto"] = chiavi.Keys.Count(k => copertura.ContainsKey(k)),
        ["generati"] = generati, ["non_generati"] = nonGenerati,
    },
    ["chiavi"] = dumpChiavi,
    ["file_attribuiti_a_tana_ordinaria"] = new JsonArray(indistinti.Order().Select(x => (JsonNode)x).ToArray()),
    ["righe"] = dumpRighe,
    ["cristallo_riferimento"] = new JsonArray(crystal.Select(c => (JsonNode)new JsonObject
    {
        ["numero"] = c.Species, ["specie"] = it.Species[c.Species], ["versione"] = c.Version.ToString(), ["livello"] = c.Level, ["gigantamax"] = c.CanGigantamax,
    }).ToArray()),
    ["wild_area_news_2021"] = confronto,
};
File.WriteAllText(args[1], dump.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
Console.WriteLine(dump["conteggi"]!.ToJsonString());
if (confronto is not null) Console.WriteLine($"WAN 2021: {confronto["eventi"]} eventi, {confronto["voci_distinte"]} voci distinte, {confronto["voci_nella_libreria"]} nella libreria");
return 0;
