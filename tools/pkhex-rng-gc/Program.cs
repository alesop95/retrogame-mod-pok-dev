// Produce gli esemplari delle voci di `pokedex-home-completo/rng-comunita-2.json` che EncounterCriteria non sa costruire,
// perche' richiedono una ricerca del seme e, per i cromatici, la scelta di una coppia ID/ID segreto compatibile con il PID.
// Voci trattate: C12 Jirachi di Pokemon Channel, C13 Jirachi WISHMKR, C15-C21 Pokemon ombra di Colosseum, C24 Metang della
// Zona Safari di HeartGold. Per ogni candidato risale dagli IV ai semi con le funzioni di reversal della libreria, ricava il
// PID, sceglie l'ID segreto (o la coppia) per la cromaticita', costruisce l'esemplare dall'incontro della libreria e lo
// accetta solo se LegalityAnalysis lo giudica conforme.
//
// Uso: dotnet run --project tools/pkhex-rng-gc -c Release -- <rng-comunita-2.json> <allenatore.json> <cartella-uscita>
using System.Security.Cryptography;
using System.Text.Encodings.Web;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length < 3) { Console.WriteLine("uso: <lista.json> <allenatore.json> <cartella>"); return 1; }
var voci = new HashSet<string> { "C12", "C13", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C24" };
var al = JsonNode.Parse(File.ReadAllText(args[1]))!;
ushort tidP = (ushort)(int)al["tid"]!, sidP = (ushort)(int)al["sid"]!;
string nomeP = (string)al["nome"]!;
var dir = Directory.CreateDirectory(args[2]).FullName;
var esiti = new JsonArray();

foreach (var c in JsonNode.Parse(File.ReadAllText(args[0]))!.AsArray())
{
    string id = (string)c!["id"]!;
    if (!voci.Contains(id)) continue;
    var specie = Enum.Parse<Species>((string)c["specie"]!);
    var ver = Enum.Parse<GameVersion>((string)c["gioco"]!);
    var iv = c["iv"]!.AsArray().Select(x => (int)x!).ToArray(); // PS, Att, Dif, AttSp, DifSp, Vel
    string? natura = (string?)c["natura"];
    bool cromatico = (bool?)c["cromatico"] ?? false;
    string ot = (string?)c["ot"] ?? nomeP;
    int lingua = (string?)c["lingua"] == "en" ? (int)LanguageID.English : (int)LanguageID.Italian;
    var esito = new JsonObject
    {
        ["id"] = id, ["specie"] = specie.ToString(), ["gioco"] = ver.ToString(), ["ot"] = ot, ["tid"] = null, ["sid"] = null,
        ["pid"] = null, ["natura"] = null, ["iv"] = null, ["cromatico"] = false, ["file"] = null, ["sha256"] = null,
        ["esito"] = null, ["fonte"] = (string?)c["fonte"], ["storia"] = (string?)c["storia"],
    };
    esiti.Add(esito);
    string motivo;
    try
    {
        motivo = id switch
        {
            "C12" => Channel(esito, specie, iv, natura, cromatico, lingua),
            "C13" => Wishmkr13(esito, specie, iv, natura, cromatico, lingua),
            "C24" => Safari(id, esito, specie, iv, natura, cromatico, lingua, ot),
            _ => Ombra(id, esito, specie, iv, natura, cromatico, lingua, ot),
        };
    }
    catch (Exception ex) { motivo = "errore: " + ex.GetType().Name + " " + ex.Message; }
    if (motivo.Length > 0) esito["esito"] = "non prodotto: " + motivo;
    Console.WriteLine($"{id} {specie}: {esito["esito"]} IV {esito["iv"]} {esito["natura"]} ID {esito["tid"]}/{esito["sid"]} cromatico {esito["cromatico"]}");
}
File.WriteAllText(Path.Combine(dir, "rapporto.json"), new JsonObject { ["esiti"] = esiti }
    .ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = JavaScriptEncoder.UnsafeRelaxedJsonEscaping }));
return 0;

// verifica e scrittura di un esemplare accettato; restituisce "" se prodotto, altrimenti il motivo
string Chiudi(string id, Species specie, JsonObject esito, PKM pk, LegalityAnalysis la)
{
    int[] v = { pk.IV_HP, pk.IV_ATK, pk.IV_DEF, pk.IV_SPA, pk.IV_SPD, pk.IV_SPE };
    esito["tid"] = pk.TID16; esito["sid"] = pk.SID16; esito["pid"] = pk.PID.ToString("X8");
    esito["natura"] = pk.Nature.ToString(); esito["iv"] = string.Join("/", v); esito["cromatico"] = pk.IsShiny;
    if (!la.Valid)
        return "il verificatore non accetta: " + string.Join(" | ", la.Report().Replace("\r", "").Split('\n').Where(x => x.Contains("Invalid")).Take(3));
    var dati = new byte[pk.SIZE_STORED]; pk.WriteDecryptedDataStored(dati);
    var file = $"{id}-{specie}{(pk.IsShiny ? "-cromatico" : "")}.{pk.Extension}";
    File.WriteAllBytes(Path.Combine(dir, file), dati);
    esito["file"] = file; esito["sha256"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant();
    esito["esito"] = "prodotto";
    return "";
}

bool IvOk(int[] iv, PKM pk) { int[] v = { pk.IV_HP, pk.IV_ATK, pk.IV_DEF, pk.IV_SPA, pk.IV_SPD, pk.IV_SPE }; return Enumerable.Range(0, 6).All(i => iv[i] < 0 || iv[i] == v[i]); }

// C12: Jirachi di Pokemon Channel. L'ID segreto esce dal seme (l'ID e' fisso, 40122), quindi la cromaticita' e' una
// proprieta' del seme: si cercano fra i semi che danno gli IV quelli che la libreria ritiene possibili (ChannelJirachi).
string Channel(JsonObject esito, Species specie, int[] iv, string? natura, bool cromatico, int lingua)
{
    var tr = new SimpleTrainerInfo(GameVersion.S) { OT = nomeP, TID16 = tidP, SID16 = sidP, Language = lingua };
    var modello = EntityBlank.GetBlank(3); modello.Species = (ushort)specie; modello.Language = lingua;
    var enc = EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, GameVersion.S)
        .OfType<EncounterGift3>().FirstOrDefault(g => g.Method == PIDType.Channel);
    if (enc is null) return "nessun dono di Pokemon Channel nella libreria";
    var semi = new uint[XDRNG.MaxCountSeedsChannel];
    int k = XDRNG.GetSeedsChannel(semi, (uint)iv[0], (uint)iv[1], (uint)iv[2], (uint)iv[3], (uint)iv[4], (uint)iv[5]);
    int possibili = 0, cromatici = 0, naturaOk = 0;
    var crit = EncounterCriteria.Unrestricted with { IV_HP = (sbyte)iv[0], IV_ATK = (sbyte)iv[1], IV_DEF = (sbyte)iv[2], IV_SPA = (sbyte)iv[3], IV_SPD = (sbyte)iv[4], IV_SPE = (sbyte)iv[5],
        Nature = natura is null ? Nature.Random : Enum.Parse<Nature>(natura), Shiny = cromatico ? Shiny.Always : Shiny.Never };
    bool trovato = false;
    var elenco = new List<string>();
    for (int i = 0; i < k; i++)
    {
        var s = new PK3(); EncounterGift3.SetValuesFromSeedChannel(s, semi[i]);
        bool poss = ChannelJirachi.IsPossible(semi[i]);
        elenco.Add($"{semi[i]:X8}:{s.Nature}:{(s.IsShiny ? "cromatico" : "no")}:{(poss ? "possibile" : "impossibile nel Channel")}");
        if (!poss) continue;
        possibili++;
        if (s.IsShiny) cromatici++;
        if (natura is not null && s.Nature.ToString() != natura) continue;
        naturaOk++;
        if (s.IsShiny == cromatico) trovato = true;
    }
    esito["semi_misurati"] = $"{k} semi per gli IV, {possibili} possibili per il Channel, {cromatici} cromatici, {naturaOk} con la natura: " + string.Join(", ", elenco);
    if (!trovato) return "nessun seme del Channel con questi IV, questa natura e questa cromaticita': " + esito["semi_misurati"];
    var pk = enc.ConvertToPKM(tr, crit);
    pk.RefreshChecksum();
    esito["ot"] = pk.OriginalTrainerName;
    var r = Chiudi("C12", specie, esito, pk, new LegalityAnalysis(pk));
    if (r.Length == 0) esito["incontro"] = "Pokemon Channel Jirachi (EncounterGift3, Method Channel); l'allenatore e' CHANNEL con ID 40122 e ID segreto dal seme, non blisy";
    return r;
}

// C13: Jirachi WISHMKR. Il seme del disco e' a 16 bit e solo nove danno un Jirachi cromatico (Wishmkr.All9), uno per natura.
string Wishmkr13(JsonObject esito, Species specie, int[] iv, string? natura, bool cromatico, int lingua)
{
    var tr = new SimpleTrainerInfo(GameVersion.S) { OT = nomeP, TID16 = tidP, SID16 = sidP, Language = lingua };
    var modello = EntityBlank.GetBlank(3); modello.Species = (ushort)specie; modello.Language = lingua;
    EncounterGift3? enc = null;
    foreach (var gv in new[] { GameVersion.R, GameVersion.S, GameVersion.E, GameVersion.FR, GameVersion.LG })
    {
        enc = EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, gv)
            .OfType<EncounterGift3>().FirstOrDefault(g => g.ID32 == Wishmkr.TrainerID);
        if (enc is not null) break;
    }
    if (enc is null) return "nessun dono WISHMKR nella libreria";
    var misure = new List<string>();
    bool trovato = false;
    foreach (var seme in Wishmkr.All9)
    {
        var s = new PK3(); EncounterGift3.GenerateWishmkr(s, seme);
        s.ID32 = Wishmkr.TrainerID;
        misure.Add($"{seme:X4}:{s.Nature}:{s.IV_HP}/{s.IV_ATK}/{s.IV_DEF}/{s.IV_SPA}/{s.IV_SPD}/{s.IV_SPE}");
        if ((natura is null || s.Nature.ToString() == natura) && IvOk(iv, s)) trovato = true;
    }
    esito["semi_misurati"] = "i 9 semi cromatici del disco (seme:natura:IV): " + string.Join(", ", misure);
    if (!trovato) return "nessuno dei 9 semi WISHMKR cromatici ha natura " + natura + " e PS/Att/Vel a 31: " + esito["semi_misurati"];
    var crit = EncounterCriteria.Unrestricted with { Nature = natura is null ? Nature.Random : Enum.Parse<Nature>(natura), Shiny = Shiny.Always };
    var pk = enc.ConvertToPKM(tr, crit);
    pk.RefreshChecksum();
    esito["ot"] = pk.OriginalTrainerName;
    return Chiudi("C13", specie, esito, pk, new LegalityAnalysis(pk));
}

// C24: Metang della Zona Safari di HeartGold, Metodo K. La libreria trova da se' il seme dagli IV (SetFromIVsK) ma non
// guarda la cromaticita': in quarta generazione ogni PID e' cromatico con un ID segreto adatto, quindi lo si sceglie dopo.
string Safari(string id, JsonObject esito, Species specie, int[] iv, string? natura, bool cromatico, int lingua, string ot)
{
    var tr = new SimpleTrainerInfo(GameVersion.HG) { OT = ot, TID16 = tidP, SID16 = sidP, Language = lingua };
    var modello = EntityBlank.GetBlank(4); modello.Species = (ushort)specie; modello.Language = lingua;
    var slot = EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, GameVersion.HG)
        .OfType<EncounterSlot4>().Where(s => s.IsSafariHGSS).ToList();
    if (slot.Count == 0) return "nessuno slot della Zona Safari per questa specie nella libreria";
    var crit = EncounterCriteria.Unrestricted with { IV_HP = (sbyte)iv[0], IV_ATK = (sbyte)iv[1], IV_DEF = (sbyte)iv[2], IV_SPA = (sbyte)iv[3], IV_SPD = (sbyte)iv[4], IV_SPE = (sbyte)iv[5],
        Nature = natura is null ? Nature.Random : Enum.Parse<Nature>(natura) };
    string ultimo = "";
    foreach (var s in slot)
    {
        var pk = s.ConvertToPKM(tr, EncounterCriteria.Unrestricted);
        if (!s.SetFromIVsK(pk, PersonalTable.HGSS[(ushort)specie], crit, out var origine)) { ultimo = $"{s.LongName}: nessun seme del Metodo K con questi IV e questa natura"; continue; }
        if (cromatico)
        {
            uint ph = pk.PID >> 16, pl = pk.PID & 0xFFFF;
            pk.SID16 = (ushort)(pk.TID16 ^ ph ^ pl); // xor 0: cromatico a stella
        }
        pk.RefreshChecksum();
        esito["seme"] = origine.ToString("X8"); esito["incontro"] = s.LongName + " (" + s.Type + ")";
        var r = Chiudi(id, specie, esito, pk, new LegalityAnalysis(pk));
        esito["sfera"] = ((Ball)pk.Ball).ToString();
        if (r.Length == 0) return r;
        ultimo = s.LongName + ": " + r;
        esito["file"] = null; esito["sha256"] = null; esito["esito"] = null;
    }
    return ultimo;
}

// C15-C21: Pokemon ombra di Colosseum (XDRNG: IV da due chiamate, poi abilita', poi PID). Per ogni combinazione di IV si
// risale ai semi, si scarta chi non rispetta la natura e i blocchi del PID verso gli allenatori NPC (LockFinder), poi si
// sceglie la coppia ID/ID segreto: per un cromatico una coppia che renda tale il PID e che Colosseum possa generare a inizio
// partita (MethodCXD.TryGetSeedTrainerID); per un non cromatico l'allenatore del progetto, se la libreria lo ammette.
string Ombra(string id, JsonObject esito, Species specie, int[] iv, string? natura, bool cromatico, int lingua, string ot)
{
    var tr = new SimpleTrainerInfo(GameVersion.E) { OT = ot, TID16 = tidP, SID16 = sidP, Language = lingua };
    var modello = EntityBlank.GetBlank(3); modello.Species = (ushort)specie; modello.Language = lingua;
    var incontri = EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, GameVersion.CXD)
        .OfType<EncounterShadow3Colo>().ToList();
    if (incontri.Count == 0) return "nessun incontro ombra di Colosseum per questa specie nella libreria";
    var liberi = Enumerable.Range(0, 6).Where(i => iv[i] < 0).ToArray();
    var tutti = new uint[XDRNG.MaxCountSeedsIV];
    int semiTot = 0, naturaOk = 0, bloccoOk = 0, idOk = 0;
    string ultimo = "";
    foreach (var enc in incontri)
    {
        for (int comb = 0; comb < 1 << (5 * liberi.Length); comb++)
        {
            var v = (int[])iv.Clone();
            for (int j = 0; j < liberi.Length; j++) v[liberi[j]] = (comb >> (5 * j)) & 31;
            uint iv1 = (uint)(v[0] | (v[1] << 5) | (v[2] << 10)), iv2 = (uint)(v[5] | (v[3] << 5) | (v[4] << 10));
            int n = XDRNG.GetSeedsIVs(tutti, iv1 << 16, iv2 << 16);
            for (int q = 0; q < n; q++)
            {
                uint seme = tutti[q]; semiTot++;
                uint s = XDRNG.Next3(seme);
                uint pid = (XDRNG.Next16(ref s) << 16) | XDRNG.Next16(ref s);
                if (natura is not null && ((Nature)(pid % 25)).ToString() != natura) continue;
                naturaOk++;
                int bit = (int)((XDRNG.Next2(seme) >> 16) & 1);
                var scratch = new CK3 { Species = (ushort)specie };
                if (!LockFinder.IsAllShadowLockValid(enc, seme, scratch)) continue;
                bloccoOk++;
                var coppia = TrovaID(pid, cromatico, tidP, sidP);
                if (coppia is null) { ultimo = "nessuna coppia ID/ID segreto valida per Colosseum con cromaticita' " + cromatico; continue; }
                idOk++;
                var tr2 = new SimpleTrainerInfo(GameVersion.E) { OT = ot, TID16 = coppia.Value.tid, SID16 = coppia.Value.sid, Language = lingua };
                var ck = enc.ConvertToPKM(tr2, EncounterCriteria.Unrestricted);
                ck.TID16 = coppia.Value.tid; ck.SID16 = coppia.Value.sid;
                ck.PID = pid;
                ck.IV_HP = v[0]; ck.IV_ATK = v[1]; ck.IV_DEF = v[2]; ck.IV_SPA = v[3]; ck.IV_SPD = v[4]; ck.IV_SPE = v[5];
                ck.RefreshAbility(bit);
                ck.RefreshChecksum();
                var pk = ck.ConvertToPK3();
                var la = new LegalityAnalysis(pk);
                esito["seme"] = seme.ToString("X8"); esito["incontro"] = enc.LongName;
                var r = Chiudi(id, specie, esito, pk, la);
                if (r.Length == 0) { esito["semi_misurati"] = $"{semiTot} semi, {naturaOk} con la natura, {bloccoOk} con i blocchi NPC, {idOk} con coppia valida"; return r; }
                ultimo = r;
                esito["file"] = null; esito["sha256"] = null; esito["esito"] = null;
            }
        }
    }
    return $"{semiTot} semi per gli IV, {naturaOk} con la natura, {bloccoOk} con i blocchi NPC, {idOk} con coppia ID valida; ultimo esito: {ultimo}";
}

// la coppia ID/ID segreto: parte dall'allenatore del progetto e, se il PID deve essere cromatico, cerca l'ID segreto (otto
// possibili per ogni ID) e poi, se Colosseum non puo' generare la coppia, cambia l'ID
(ushort tid, ushort sid)? TrovaID(uint pid, bool cromatico, ushort tid0, ushort sid0)
{
    uint ph = pid >> 16, pl = pid & 0xFFFF;
    if (!cromatico)
    {
        for (int d = 0; d < 65536; d++)
        {
            ushort sid = (ushort)(sid0 + d);
            if (ShinyUtil.GetIsShiny3((uint)sid << 16 | tid0, pid)) continue;
            if (MethodCXD.TryGetSeedTrainerID(tid0, sid, out _)) return (tid0, sid);
        }
        return null;
    }
    for (int dt = 0; dt < 65536; dt++)
    {
        ushort tid = (ushort)(tid0 + dt);
        for (int x = 0; x < 8; x++)
        {
            ushort sid = (ushort)(tid ^ ph ^ pl ^ x);
            if (MethodCXD.TryGetSeedTrainerID(tid, sid, out _)) return (tid, sid);
        }
    }
    return null;
}
