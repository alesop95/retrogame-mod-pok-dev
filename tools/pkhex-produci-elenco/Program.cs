// Produce gli esemplari dell'elenco unico di produzione, `pokedex-home-completo/ELENCO-PRODUZIONE.md`, con la libreria
// del verificatore compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il 2026-11-04 il proprietario ha chiesto di produrre le 1867 voci e le 184 mosse dell'elenco, che
// `tools/elenco-produzione.py` fonde in esemplari: uno per riga, ciascuno con i vincoli delle voci che chiude (specie,
// forma, giochi d'origine, sfera, cromatico, sesso, abilita', classe d'incontro, livello massimo). Come
// `tools/pkhex-genera`, la libreria sa gia' costruire un esemplare legale da ogni voce delle sue tabelle, e lo stesso
// codice lo giudica: qui la si usa invece di imitarla.
//
// Che cosa fa. Per ogni esemplare cerca, nei giochi ammessi e in un ordine che preferisce la settima e la sesta
// generazione, gli incontri che la libreria dichiara per quella specie e forma; tiene quelli della classe richiesta e
// sotto il livello massimo; costruisce l'esemplare con l'allenatore del progetto (`allenatore.json`) e i criteri di
// cromatico, sesso e abilita'; prova la sfera richiesta; e lo accetta soltanto se LegalityAnalysis lo giudica conforme
// nel suo formato d'origine. La conversione verso Rubino Omega o Ultrasole e il giudizio nel contesto del salvataggio li
// fa poi `tools/pkhex-scrivi-salvataggio`, come per tutte le copie. Il Fiocco Maestro si costruisce dall'Ombra di XD
// con i fiocchi fino alla settima generazione che RibbonVerifier accetta. Le voci che la libreria non sa costruire
// restano nel rapporto con il motivo: nessun esemplare si forza.
//
// Le mosse si producono a parte, con --mosse: per ciascuna si cerca la prima specie che la impara in un incontro dei
// giochi fino alla settima generazione, e si raccolgono fino a quattro mosse nello stesso esemplare quando la stessa
// specie le impara tutte. Le mosse Z non si imparano e restano fuori, con il motivo.
//
// Gli esemplari della cartuccia di Smeraldo non si generano: si estraggono dal salvataggio con --cartuccia, i soli
// conformi, nel loro formato.
//
// Riproducibilita'. La libreria estrae i numeri casuali da Random.Shared, quindi due lanci danno esemplari diversi e
// ugualmente legali. Il risultato sono i file, e il rapporto porta l'impronta SHA-256 di ciascuno.
//
// Uso:  dotnet run -c Release -- ELENCO.json ALLENATORE.json CARTELLA_DI_USCITA
//       dotnet run -c Release -- --mosse ELENCO.json ALLENATORE.json CARTELLA_DI_USCITA
//       dotnet run -c Release -- --cartuccia SALVATAGGIO CARTELLA_DI_USCITA
//       dotnet run -c Release -- --prova SPECIE GIOCO    diagnosi: quanti incontri la libreria da' per una specie
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

var testi = GameInfo.GetStrings("it");
var inglese = GameInfo.GetStrings("en");

if (args[0] == "--prova")
{
    // diagnosi: quanti incontri la libreria restituisce per una specie in un gioco, con modelli di formato diverso
    var sp = ushort.Parse(args[1]); var ver = Enum.Parse<GameVersion>(args[2]);
    var t0 = new SimpleTrainerInfo(ver) { OT = "Alessio", TID16 = 42317, SID16 = 58164, Language = (int)LanguageID.Italian };
    foreach (byte f in new byte[] { 3, 6, 7, 8, 9 })
    {
        var m0 = EntityBlank.GetBlank(f); m0.Species = sp; m0.Language = 8;
        var l0 = EncounterMovesetGenerator.GenerateEncounters(m0, t0, ReadOnlyMemory<ushort>.Empty, ver).ToList();
        Console.WriteLine($"modello PK{f}: {l0.Count} incontri {string.Join(", ", l0.Take(3).Select(x => x.GetType().Name))}");
    }
    return 0;
}
if (args[0] == "--kyogre")
    return Kyogre(args[1], args[2]);
if (args[0] == "--cartuccia")
    return Cartuccia(args[1], args[2]);

bool mosse = args[0] == "--mosse";
var a = mosse ? args[1..] : args;
var elenco = JsonNode.Parse(File.ReadAllText(a[0]))!;
var allenatore = JsonNode.Parse(File.ReadAllText(a[1]))!;
var uscita = Directory.CreateDirectory(a[2]).FullName;

// Dalla settima alla prima generazione: le copie di destinazione sono di Ultrasole e di Rubino Omega, e un esemplare
// nato tardi richiede meno conversioni.
GameVersion[] ordine = [GameVersion.US, GameVersion.UM, GameVersion.SN, GameVersion.MN, GameVersion.OR, GameVersion.AS,
    GameVersion.X, GameVersion.Y, GameVersion.B2, GameVersion.W2, GameVersion.B, GameVersion.W, GameVersion.HG, GameVersion.SS,
    GameVersion.Pt, GameVersion.D, GameVersion.P, GameVersion.E, GameVersion.FR, GameVersion.LG, GameVersion.R, GameVersion.S,
    GameVersion.CXD, GameVersion.C, GameVersion.GD, GameVersion.SI, GameVersion.YW, GameVersion.RD, GameVersion.BU, GameVersion.GN];
var allenatori = new Dictionary<GameVersion, SimpleTrainerInfo>();
SimpleTrainerInfo Allenatore(GameVersion v)
{
    if (allenatori.TryGetValue(v, out var t)) return t;
    var (tid, sid) = ((ushort)(int)allenatore["tid"]!, (ushort)(int)allenatore["sid"]!);
    // In Rubino, Zaffiro, Colosseum e XD l'identificativo esce dal generatore del gioco a inizio partita: si prende la
    // prima coppia, a partire da quella del progetto, che il verificatore ricostruisce, come in tools/pkhex-genera.
    Func<ushort, ushort, bool>? valida = v switch
    {
        GameVersion.R or GameVersion.S => (x, y) => MethodH.TryGetSeedTrainerID(x, y, out _),
        GameVersion.CXD => (x, y) => MethodCXD.TryGetSeedTrainerID(x, y, out _),
        _ => null,
    };
    if (valida is not null)
    {
        bool trovata = false;
        for (int giro = 0; giro < 16 && !trovata; giro++)
            for (int passo = 0; passo < 65536 && !trovata; passo++)
                if (valida((ushort)(tid + giro), (ushort)(sid + passo))) { (tid, sid) = ((ushort)(tid + giro), (ushort)(sid + passo)); trovata = true; }
    }
    t = new SimpleTrainerInfo(v == GameVersion.CXD ? GameVersion.E : v)
    {
        OT = (string)allenatore["nome"]!, TID16 = tid, SID16 = sid, Gender = 0,
        // la Verde esiste solo in giapponese, e i suoi scambi hanno soprannomi giapponesi
        Language = v == GameVersion.GN ? (int)LanguageID.Japanese : (int)LanguageID.Italian,
    };
    allenatori[v] = t;
    return t;
}

var esiti = new JsonArray();
int riuscite = 0, n = 0;
var personalita = new HashSet<uint>();
if (mosse)
    Mosse();
else
    foreach (var e in elenco["esemplari"]!.AsArray())
    {
        n++;
        var cat = (string)e!["categoria"]!;
        var voci = e["voci"]!.AsArray().Select(x => (string)x!).ToArray();
        var esito = new JsonObject { ["n"] = n, ["categoria"] = cat, ["voci"] = new JsonArray(voci.Select(x => (JsonNode)x).ToArray()) };
        if (cat == "Smeraldo")
        {
            esito["esito"] = "da estrarre"; esito["motivo"] = "esemplare della cartuccia: si estrae con --cartuccia, non si genera";
            esiti.Add(esito); continue;
        }
        if (e["numero"] is null && cat != "Fiocco Maestro")
        {
            esito["esito"] = "contestato"; esito["motivo"] = "la voce del foglio non nomina una specie riconosciuta";
            esiti.Add(esito); continue;
        }
        PKM? pk; string voce, motivo;
        if (cat == "Fiocco Maestro") (pk, voce, motivo) = FioccoMaestro();
        else (pk, voce, motivo) = Genera(e);
        if (pk is not null)
        {
            Scrivi(pk, $"{n:0000}-{testi.specieslist[pk.Species]}", esito);
            esito["incontro"] = voce;
            riuscite++;
        }
        else { esito["esito"] = "contestato"; esito["motivo"] = motivo; }
        esiti.Add(esito);
        Console.WriteLine($"{(pk is null ? "NO " : "ok ")} {n,4} {cat,-20} {voci[0]}{(pk is null ? "  " + motivo : "  " + voce)}");
    }

File.WriteAllText(Path.Combine(uscita, "rapporto.json"), new JsonObject {
    ["libreria"] = typeof(PKM).Assembly.GetName().Version?.ToString(), ["riuscite"] = riuscite, ["richieste"] = esiti.Count,
    ["esiti"] = esiti }.ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"riuscite {riuscite} su {esiti.Count}");
return 0;

(PKM?, string, string) Genera(JsonNode e)
{
    var specie = (ushort)(int)e["numero"]!;
    var forma = e["forma_n"] is { } fn ? (byte)(int)fn : (byte)0;
    var conForma = e["forma_n"] is not null;
    var giochi = e["giochi"] is JsonArray g ? g.Select(x => Enum.Parse<GameVersion>((string)x!)).ToHashSet() : null;
    // un gruppo di giochi della libreria, come RBY per la Console Virtuale di prima generazione, si passa cosi' com'e'
    var versioni = giochi is not null && giochi.Contains(GameVersion.RBY) ? [GameVersion.RBY]
        : ordine.Where(v => giochi is null || giochi.Contains(v)).ToArray();
    var sfera = e["sfera"] is { } sf ? Array.IndexOf(testi.balllist, (string)sf!) : -1;
    var cromatico = (bool?)e["cromatico"];
    var sesso = (string?)e["sesso"];
    var abilita = (string?)e["abilita"];
    var classe = (string?)e["classe"];
    var livelloMax = e["livello_max"] is { } lm ? (int)lm : 100;
    // Le specie di un solo sesso, come Gallade e Froslass, e Meowstic, la cui forma e' il sesso, chiedono il sesso giusto
    // gia' alla costruzione, perche' l'evoluzione lo eredita.
    var pi = PersonalTable.SM.GetFormEntry(specie, forma);
    if (sesso is null && pi.OnlyMale) sesso = "M";
    if (sesso is null && pi.OnlyFemale) sesso = "F";
    bool formaSesso = specie == (ushort)Species.Meowstic;
    if (formaSesso && sesso is null) sesso = forma == 1 ? "F" : "M";
    var criteri = EncounterCriteria.Unrestricted with
    {
        Shiny = cromatico == true ? Shiny.Always : Shiny.Never,
        Gender = sesso == "M" ? Gender.Male : sesso == "F" ? Gender.Female : Gender.Random,
        Ability = abilita is not null ? AbilityPermission.OnlyHidden : AbilityPermission.Any12H,
    };
    string motivo = "nessun incontro della libreria nei giochi ammessi";
    foreach (var v in versioni)
    {
        var tr = Allenatore(v);
        // Il modello e' nel formato della settima generazione, che contiene tutte le specie fino a 809: un modello di
        // formato piu' vecchio tronca la specie, e un modello vuoto non dichiara la propria generazione.
        var modello = EntityBlank.GetBlank(7);
        // per la Console Virtuale alcuni doni, come gli starter di Giallo, si trovano solo con un modello del formato del gioco
        if (v is GameVersion.RD or GameVersion.GN or GameVersion.BU or GameVersion.YW or GameVersion.RBY && specie <= 151) modello = EntityBlank.GetBlank(1);
        else if (v is GameVersion.GD or GameVersion.SI or GameVersion.C && specie <= 251) modello = EntityBlank.GetBlank(2);
        modello.Species = specie;
        modello.Form = forma;
        modello.Language = tr.Language;
        // il modello vuoto e' maschio: per una specie solo femmina, come Wormadam o Froslass, la libreria non restituirebbe
        // nessun incontro
        if (sesso == "F") modello.Gender = 1;
        IEnumerable<IEncounterable> incontri;
        try { incontri = EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, v).ToList(); }
        catch (Exception ex) { motivo = "la libreria non enumera gli incontri in " + v + ": " + ex.Message; continue; }
        foreach (var enc in incontri)
        {
            var tipo = enc.GetType().Name;
            // la forma si pretende solo sull'incontro della specie stessa: quella di Raichu e Marowak di Alola o di Lycanroc
            // Crepuscolo la decide l'evoluzione, non la pre-evoluzione
            if (conForma && enc.Species == specie && enc.Form != forma && !FormInfo.IsFormChangeable(specie, enc.Form, forma, enc.Context, enc.Context)
                && !(specie == (ushort)Species.Unown && enc.Generation <= 2)) continue;
            // Il foglio chiama «scambio con un altro allenatore» ogni esemplare il cui allenatore originale non e' il
            // giocatore: oltre agli scambi in gioco, i Pokemon di N, i doni dei dischi bonus, di Ranch e di Battle
            // Revolution, che la libreria tiene come doni o incontri fissi con l'allenatore fissato.
            bool allenatoreFisso = tipo.Contains("Trade") || enc is IFixedTrainer { IsFixedTrainer: true } || enc is MysteryGift;
            if (classe == "scambio" && !allenatoreFisso) continue;
            // gli «altri esemplari unici» del foglio sono incontri precisi, doni, premi o selvatici rari, mai un uovo
            if (classe == "non-uovo" && (tipo.Contains("Egg") || enc is MysteryGift)) continue;
            if (classe == "fisso" && !(tipo.Contains("Static") || tipo.Contains("Gift") || allenatoreFisso)) continue;
            if (enc.LevelMin > livelloMax) continue;
            for (int tentativo = 0; tentativo < 4; tentativo++)
            {
                PKM pk;
                try
                {
                    pk = enc.ConvertToPKM(tr, tentativo == 0 ? criteri : criteri with { Nature = (Nature)Random.Shared.Next(25) });
                }
                catch (Exception ex) { motivo = "costruzione non riuscita: " + ex.Message; break; }
                if (pk is CK3 ck) pk = ck.ConvertToPK3();
                else if (pk is XK3 xk) pk = xk.ConvertToPK3();
                // anche una forma regionale che nasce con l'evoluzione, come Raichu di Alola, si ottiene solo evolvendo nei
                // giochi di Alola: l'esemplare passa prima nel formato della settima generazione
                if (pk.Species != specie && (specie > pk.MaxSpeciesID || (conForma && forma > 0 && pk.Format < 7)))
                {
                    // un'evoluzione nata dopo il gioco d'origine, come Weavile da Oro e Argento: si porta l'esemplare nel
                    // formato della settima generazione, dove la specie esiste, e lo si fa evolvere li'
                    var conv = EntityConverter.ConvertToType(pk, typeof(PK7), out var rc);
                    if (conv is null) { motivo = "conversione per l'evoluzione non riuscita: " + rc; break; }
                    pk = conv;
                }
                if (pk.Species != specie) // un'evoluzione: la si porta alla specie richiesta al livello piu' basso utile
                {
                    var indiceAbilita = pk.AbilityNumber >> 1;
                    pk.Species = specie;
                    pk.CurrentLevel = Math.Max(pk.CurrentLevel, (byte)Math.Min(100, livelloMax));
                    // il soprannome di uno scambio resta dopo l'evoluzione, come nel gioco; il nome di specie si aggiorna
                    if (!pk.IsNicknamed)
                    {
                        // la prima e la seconda generazione internazionali hanno i nomi inglesi, che il gioco italiano usa
                        var nome = SpeciesName.GetSpeciesNameGeneration(specie, pk.Language, pk.Format);
                        pk.Nickname = nome.Length > 0 ? nome : SpeciesName.GetSpeciesNameGeneration(specie, (int)LanguageID.English, pk.Format);
                    }
                    if (conForma) pk.Form = forma; // la forma prima dell'abilita', che ne dipende
                    if (pk.Format >= 3)
                        pk.RefreshAbility(indiceAbilita);
                }
                if (conForma) pk.Form = forma;
                // Il disegno di Vivillon viene dal paese della console su cui l'uovo o lo Scatterbug nasce: si sceglie il
                // primo paese e la prima area che danno il disegno chiesto, in una regione della console che lo ammette.
                if (conForma && specie is >= 664 and <= 666 && pk is IRegionOrigin ro && Paese(forma) is var (cr, pa, ar) && pa != 0)
                    (ro.ConsoleRegion, ro.Country, ro.Region) = (cr, pa, ar);
                if (sfera > 0) pk.Ball = (byte)sfera;
                // un formato senza la sfera, come la prima e la seconda generazione, non soddisfa una voce che la chiede
                if (sfera > 0 && pk.Ball != sfera) { motivo = "il formato d'origine non porta la sfera richiesta"; break; }
                // in seconda generazione il criterio non basta: la lucentezza viene dai valori individuali
                if (cromatico == true && !pk.IsShiny) pk.SetShiny();
                if (abilita is not null && inglese.abilitylist[pk.Ability] != abilita) { motivo = "abilità diversa da " + abilita; continue; }
                if (pk.CurrentLevel > livelloMax) { motivo = "livello oltre il massimo"; continue; }
                pk.RefreshChecksum();
                var la = new LegalityAnalysis(pk);
                // Un'evoluzione per scambio, come Slurpuff o Gourgeist, chiede che l'esemplare sia passato per un altro
                // allenatore: lo si registra come detentore, che e' cio' che lo scambio lascia; il salvataggio che lo riceve
                // ne diventa poi il detentore con AdaptToSaveFile.
                if (!la.Valid && pk.Format >= 6 && la.Report().Contains("trade evolution"))
                {
                    pk.HandlingTrainerName = "Marta"; pk.HandlingTrainerGender = 1; pk.CurrentHandler = 1;
                    if (pk is IHandlerLanguage hl) hl.HandlingTrainerLanguage = (byte)LanguageID.Italian;
                    pk.RefreshChecksum();
                    la = new LegalityAnalysis(pk);
                }
                // Le mosse e le mosse ricordabili si ricalcolano con i suggerimenti della libreria quando un'evoluzione o
                // un livello diverso da quello dell'incontro le rende contestate.
                if (!la.Valid && la.Report().Contains("Move"))
                {
                    pk.SetRelearnMoves(la);
                    var mosseLegali = new ushort[4];
                    new LegalityAnalysis(pk).GetMoveSet(mosseLegali, false);
                    pk.SetMoves(mosseLegali);
                    pk.HealPP();
                    pk.RefreshChecksum();
                    la = new LegalityAnalysis(pk);
                }
                // Un'abilita' fissata dall'incontro, come quella di Giratina a Sinjoh o dei Pokemon del Dream Radar, si cerca
                // provando le tre posizioni.
                if (!la.Valid && la.Report().Contains("Ability") && pk.Format >= 3)
                {
                    for (int ab = 0; ab < 3 && !la.Valid; ab++)
                    {
                        pk.RefreshAbility(ab); pk.RefreshChecksum();
                        la = new LegalityAnalysis(pk);
                    }
                }
                // In quarta generazione la sfera sta in due byte, quello di Diamante e Perla e quello di HeartGold e
                // SoulSilver, e MiscVerifierG4 vuole il secondo a zero o uguale al primo secondo l'origine: si provano i due.
                if (!la.Valid && pk is G4PKM p4 && la.Report().Contains("HG/SS"))
                {
                    foreach (var b in new[] { (byte)0, p4.BallDPPt })
                    {
                        p4.BallHGSS = b; p4.RefreshChecksum();
                        la = new LegalityAnalysis(pk);
                        if (la.Valid) break;
                    }
                }
                // Un esemplare di Game Boy arriva in HOME solo da Poke Transporter, che lo porta in settima generazione con la
                // regione della console: si prova quella conversione, verso una console europea, e se il risultato non e'
                // conforme l'esemplare non serve. Fanno eccezione le voci che il foglio vuole giapponesi, che vanno in una
                // copia di console giapponese (--regione-giappone di tools/pkhex-scrivi-salvataggio).
                bool giapponese = voceGiapponese(e);
                if (la.Valid && pk.Format <= 2 && !ProvaTransporter(pk, giapponese)) { motivo = $"{tipo} ({v}): non conforme dopo Poke Transporter verso una console " + (giapponese ? "giapponese" : "europea"); continue; }
                if (la.Valid && (cromatico is null || pk.IsShiny == cromatico) && personalita.Add(Impronta(pk)))
                    return (pk, $"{tipo} {enc.LongName} ({v})", "");
                motivo = $"{tipo} ({v}): " + string.Join(" | ", la.Report().Replace("\r", "").Split('\n').Where(x => x.Contains("Invalid")).Take(2));
            }
        }
    }
    return (null, "", motivo);
}

static (byte, byte, byte) Paese(byte forma)
{
    for (byte cr = 0; cr <= 6; cr++)
    {
        if (!Vivillon3DS.IsPatternValid(forma, cr)) continue;
        for (int pa = 1; pa < 256; pa++)
            for (int ar = 0; ar < 128; ar++)
                if (Vivillon3DS.GetPattern((byte)pa, (byte)ar) == forma && Vivillon3DS.IsPatternNative(forma, (byte)pa, (byte)ar)
                    && Locale3DS.IsConsoleRegionCountryValid(cr, (byte)pa))
                    return (cr, (byte)pa, (byte)ar);
    }
    return (0, 0, 0);
}

// Due esemplari con la stessa impronta sembrerebbero cloni. In prima e seconda generazione il PID non esiste e vale zero,
// quindi l'impronta e' fatta dai valori individuali (DV); dalla terza e' il PID.
static uint Impronta(PKM pk) => pk.Format <= 2
    ? (uint)(pk.IV_ATK | (pk.IV_DEF << 4) | (pk.IV_SPE << 8) | (pk.IV_SPA << 12)) ^ ((uint)pk.Species << 16) ^ 0x80000000u
    : pk.PID ^ ((uint)pk.Species << 16);

static bool voceGiapponese(JsonNode e) =>
    e["voci"]!.AsArray().Any(x => ((string)x!).Contains("(Jp)") || ((string)x!).Contains("giappones") || ((string)x!).Contains("JP ")
        || ((string)x!).Any(c => c is >= '぀' and <= 'ヿ'));

static bool ProvaTransporter(PKM pk, bool giapponese)
{
    var p7 = EntityConverter.ConvertToType(pk, typeof(PK7), out _);
    if (p7 is not PK7 q) return false;
    // Europa, Italia, Marche, come la Luna del proprietario; Giappone e Tokyo per le voci giapponesi
    (q.ConsoleRegion, q.Country, q.Region) = giapponese ? ((byte)0, (byte)1, (byte)2) : ((byte)2, (byte)83, (byte)13);
    q.RefreshChecksum();
    return new LegalityAnalysis(q).Valid;
}

(PKM?, string, string) FioccoMaestro()
{
    // Ralts Ombra di XD al livello 20: la misura di tools/pkhex-fiocco-maestro da' a questa famiglia il massimo, e il livello
    // basso lascia il fiocco Vittoria della Torre Lotta di terza generazione, che chiede un esemplare al livello 50 o meno.
    var tr = Allenatore(GameVersion.CXD);
    var modello = EntityBlank.GetBlank(3); modello.Species = (ushort)Species.Ralts; modello.Language = tr.Language;
    var enc = EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, GameVersion.CXD)
        .FirstOrDefault(x => x.GetType().Name.Contains("Shadow"));
    if (enc is null) return (null, "", "nessun Ralts Ombra di XD nella libreria");
    var p = enc.ConvertToPKM(tr, EncounterCriteria.Unrestricted with { Shiny = Shiny.Never });
    PK3 p3 = p switch { XK3 x => x.ConvertToPK3(), CK3 c => c.ConvertToPK3(), PK3 q => q, _ => throw new InvalidOperationException() };
    p3.RibbonNational = true;
    var pk = EntityConverter.ConvertToType(p3, typeof(PK7), out var r);
    if (pk is null) return (null, "", "conversione in settima generazione non riuscita: " + r);
    foreach (var prop in pk.GetType().GetProperties().Where(x => x.Name.StartsWith("Ribbon") && x.PropertyType == typeof(bool) && x.CanWrite))
        prop.SetValue(pk, true);
    if (pk is IRibbonSetMemory6 m) { m.RibbonCountMemoryContest = 40; m.RibbonCountMemoryBattle = 8; }
    for (int giro = 0; giro < 8; giro++)
    {
        var la0 = new LegalityAnalysis(pk);
        Span<RibbonResult> res = stackalloc RibbonResult[RibbonVerifier.MaxRibbonCount];
        int k = RibbonVerifier.GetRibbonResults(new RibbonVerifierArguments(pk, la0.EncounterMatch, la0.Info.EvoChainsAllGens), res);
        if (k == 0) break;
        foreach (var x in res[..k])
        {
            var prop = pk.GetType().GetProperty(x.PropertyName);
            if (prop?.PropertyType == typeof(bool)) prop.SetValue(pk, x.IsMissing);
            else if (prop?.PropertyType == typeof(byte)) prop.SetValue(pk, (byte)0);
        }
    }
    pk.RefreshChecksum();
    var la = new LegalityAnalysis(pk);
    if (!la.Valid)
        return (null, "", "Ralts Ombra con i fiocchi fino alla settima generazione: " + string.Join(" | ", la.Report().Replace("\r", "").Split('\n').Where(x => x.Contains("Invalid")).Take(3)));
    return (pk, $"{enc.GetType().Name} {enc.LongName} (CXD), fiocchi fino alla settima generazione", "");
}

void Mosse()
{
    var elencoMosse = elenco["mosse"]!.AsArray().Select(x => (string)x!).ToList();
    var zeta = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
    var restano = new List<ushort>();
    foreach (var nome in elencoMosse)
    {
        int id = Array.IndexOf(inglese.movelist, nome);
        if (id <= 0) { esiti.Add(new JsonObject { ["mossa"] = nome, ["esito"] = "contestato", ["motivo"] = "nome non riconosciuto dalla libreria" }); continue; }
        if (MoveInfo.IsMoveZ((ushort)id)) { esiti.Add(new JsonObject { ["mossa"] = nome, ["esito"] = "fuori", ["motivo"] = "mossa Z: non si impara, la usa un esemplare con il cristallo Z" }); continue; }
        restano.Add((ushort)id);
    }
    var versioni = ordine.Where(v => v.Generation >= 3).ToArray();
    while (restano.Count > 0)
    {
        var prima = restano[0];
        PKM? trovato = null; string voce = "";
        for (ushort s = 1; s <= 809 && trovato is null; s++)
        {
            foreach (var v in versioni)
            {
                var tr = Allenatore(v);
                var modello = EntityBlank.GetBlank(v.Generation); modello.Species = s; modello.Language = tr.Language;
                // la mossa cercata, piu' quante altre ancora da produrre la stessa specie impara insieme, fino a quattro
                var gruppo = new List<ushort> { prima };
                foreach (var altra in restano.Skip(1))
                {
                    if (gruppo.Count == 4) break;
                    var prova = gruppo.Append(altra).ToArray();
                    try { if (EncounterMovesetGenerator.GenerateEncounters(modello, tr, prova, v).Any()) gruppo.Add(altra); } catch { }
                }
                IEncounterable? enc;
                try { enc = EncounterMovesetGenerator.GenerateEncounters(modello, tr, gruppo.ToArray(), v).FirstOrDefault(); }
                catch { enc = null; }
                if (enc is null) continue;
                var pk = enc.ConvertToPKM(tr, EncounterCriteria.Unrestricted with { Shiny = Shiny.Never });
                if (pk is CK3 ck) pk = ck.ConvertToPK3(); else if (pk is XK3 xk) pk = xk.ConvertToPK3();
                if (pk.Species != s) { pk.Species = s; pk.CurrentLevel = 100; pk.Nickname = SpeciesName.GetSpeciesNameGeneration(s, pk.Language, pk.Format); }
                pk.SetMoves(gruppo.ToArray());
                pk.HealPP();
                pk.RefreshChecksum();
                if (!new LegalityAnalysis(pk).Valid) continue;
                trovato = pk; voce = $"{enc.GetType().Name} {enc.LongName} ({v})";
                foreach (var x in gruppo) restano.Remove(x);
                var esito = new JsonObject { ["mosse"] = new JsonArray(gruppo.Select(x => (JsonNode)inglese.movelist[x]).ToArray()), ["incontro"] = voce };
                Scrivi(pk, $"M{esiti.Count + 1:000}-{testi.specieslist[s]}", esito);
                esiti.Add(esito); riuscite++;
                Console.WriteLine($"ok  {string.Join(", ", gruppo.Select(x => inglese.movelist[x]))} su {testi.specieslist[s]}  {voce}");
                break;
            }
        }
        if (trovato is null)
        {
            esiti.Add(new JsonObject { ["mossa"] = inglese.movelist[prima], ["esito"] = "contestato", ["motivo"] = "nessuna specie la impara in un incontro fino alla settima generazione" });
            Console.WriteLine($"NO  {inglese.movelist[prima]}");
            restano.Remove(prima);
        }
    }
}

void Scrivi(PKM pk, string nome, JsonObject esito)
{
    var dati = new byte[pk.SIZE_STORED];
    pk.WriteDecryptedDataStored(dati);
    var file = $"{nome}.{pk.Extension}";
    foreach (var c in Path.GetInvalidFileNameChars()) file = file.Replace(c, '_');
    File.WriteAllBytes(Path.Combine(uscita, file), dati);
    esito["esito"] = "conforme";
    esito["file"] = file;
    esito["specie"] = testi.specieslist[pk.Species];
    esito["gioco"] = pk.Version.ToString();
    esito["livello"] = pk.CurrentLevel;
    esito["sfera"] = testi.balllist[pk.Ball];
    esito["cromatico"] = pk.IsShiny;
    esito["sha256"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant();
}

// Il Kyogre del video di blisy (`xxyQFPqltiM`, ADR-113): Zaffiro su GBA, cromatico, 6 IV perfetti, ottenuto manipolando il
// generatore casuale con il dipinto del museo, che riseme il generatore dal contatore dei fotogrammi. Kyogre in Zaffiro e' un
// incontro fisso del Metodo 1: il PID esce da due chiamate del generatore e
// gli IV dalle due successive. Si risale dagli IV tutti a 31 ai semi possibili con LCRNGReversal, se ne ricava il PID, e si
// guarda se e' cromatico per l'allenatore del progetto. Se nessuno lo e', l'ID segreto che lo renderebbe cromatico e' quello
// di un'altra partita di Smeraldo: lo strumento lo dice e non lo usa senza --sid-libero, perche' ADR-099 fissa un solo ID
// segreto per l'allenatore del progetto.
int Kyogre(string allenatoreJson, string cartella)
{
    var al = JsonNode.Parse(File.ReadAllText(allenatoreJson))!;
    ushort tid = (ushort)(int)al["tid"]!, sid = (ushort)(int)al["sid"]!;
    bool sidLibero = args.Contains("--sid-libero");
    Span<uint> semi = stackalloc uint[8];
    int k = LCRNGReversal.GetSeedsIVs(semi, 31, 31, 31, 31, 31, 31);
    // in Rubino e Zaffiro la coppia ID e ID segreto esce dal generatore a inizio partita (MethodH): si parte da quella che
    // tools/pkhex-genera e questo strumento usano gia' per l'allenatore del progetto in Zaffiro
    bool coppia = false;
    for (int giro = 0; giro < 16 && !coppia; giro++)
        for (int passo = 0; passo < 65536 && !coppia; passo++)
            if (MethodH.TryGetSeedTrainerID((ushort)(tid + giro), (ushort)(sid + passo), out _))
            { (tid, sid) = ((ushort)(tid + giro), (ushort)(sid + passo)); coppia = true; }
    Console.WriteLine($"allenatore del progetto in Zaffiro: ID {tid}, ID segreto {sid}");
    // --ot NOME e --inglese: il proprietario ha deciso il 2026-11-04 (ADR-114) che il Kyogre porti l'allenatore blisy, in
    // omaggio all'autore della manipolazione, con l'ID segreto 13181, su una Zaffiro inglese come la sua
    int iot = Array.IndexOf(args, "--ot");
    string ot = iot >= 0 ? args[iot + 1] : (string)al["nome"]!;
    int lingua = args.Contains("--inglese") ? (int)LanguageID.English : (int)LanguageID.Italian;
    var tr = new SimpleTrainerInfo(GameVersion.S) { OT = ot, TID16 = tid, SID16 = sid, Language = lingua };
    var modello = EntityBlank.GetBlank(3); modello.Species = (ushort)Species.Kyogre; modello.Language = tr.Language;
    var enc = EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, GameVersion.S)
        .FirstOrDefault(x => x.GetType().Name.Contains("Static"));
    if (enc is null) { Console.WriteLine("nessun Kyogre fisso in Smeraldo nella libreria"); return 1; }
    Console.WriteLine($"semi con 6 IV perfetti nel Metodo 1: {k}");
    var dir = Directory.CreateDirectory(cartella).FullName;
    var esiti = new JsonArray();
    for (int i = 0; i < k; i++)
    {
        uint seme = semi[i];
        uint alto = seme >> 16, basso = LCRNG.Prev(seme) >> 16;
        uint pid = (alto << 16) | basso;
        int xor = tid ^ sid ^ (int)alto ^ (int)basso;
        bool cromatico = xor < 8;
        // l'ID segreto che lo renderebbe cromatico con lo stesso ID, tra gli otto possibili, purche' MethodH lo ammetta
        ushort sidCromatico = 0; bool trovato = false;
        for (int x = 0; x < 8 && !trovato; x++)
        {
            var c = (ushort)(tid ^ alto ^ basso ^ x);
            if (MethodH.TryGetSeedTrainerID(tid, c, out _)) { sidCromatico = c; trovato = true; }
        }
        Console.WriteLine($"  seme {seme:X8} PID {pid:X8} natura {(Nature)(pid % 25)} cromatico per l'allenatore del progetto: {cromatico}; ID segreto che lo renderebbe cromatico: {(trovato ? sidCromatico.ToString() : "nessuno ammesso da MethodH con questo ID")}");
        if (!cromatico && (!sidLibero || !trovato)) continue;
        int isid = Array.IndexOf(args, "--sid");
        if (isid >= 0 && sidCromatico != ushort.Parse(args[isid + 1])) continue;
        var pk = (PK3)enc.ConvertToPKM(tr, EncounterCriteria.Unrestricted);
        if (!cromatico) { pk.SID16 = sidCromatico; }
        pk.PID = pid;
        pk.IV_HP = pk.IV_ATK = pk.IV_DEF = pk.IV_SPA = pk.IV_SPD = pk.IV_SPE = 31;
        pk.RefreshAbility((int)(pid & 1));
        pk.RefreshChecksum();
        var la = new LegalityAnalysis(pk);
        var esito = new JsonObject { ["seme"] = seme.ToString("X8"), ["pid"] = pid.ToString("X8"), ["natura"] = ((Nature)(pid % 25)).ToString(),
            ["cromatico"] = pk.IsShiny, ["sid"] = pk.SID16, ["conforme"] = la.Valid };
        if (la.Valid && pk.IsShiny)
        {
            var dati = new byte[pk.SIZE_STORED]; pk.WriteDecryptedDataStored(dati);
            var file = $"K{i}-Kyogre-6IV-cromatico.pk3";
            File.WriteAllBytes(Path.Combine(dir, file), dati);
            esito["file"] = file; esito["sha256"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant();
        }
        else esito["rapporto"] = la.Report();
        esiti.Add(esito);
    }
    File.WriteAllText(Path.Combine(dir, "rapporto.json"), new JsonObject { ["incontro"] = enc.LongName, ["esiti"] = esiti }
        .ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
    return 0;
}

int Cartuccia(string salvataggio, string cartella)
{
    var sav = SaveUtil.GetSaveFile(salvataggio) ?? throw new InvalidOperationException("salvataggio non letto: " + salvataggio);
    var dir = Directory.CreateDirectory(cartella).FullName;
    var lista = new JsonArray();
    int conformi = 0;
    for (int i = 0; i < sav.SlotCount; i++)
    {
        var pk = sav.GetBoxSlotAtIndex(i);
        if (pk.Species == 0) continue;
        int box = i / sav.BoxSlotCount + 1, posto = i % sav.BoxSlotCount + 1;
        var la = new LegalityAnalysis(pk);
        var voce = new JsonObject { ["box"] = box, ["posto"] = posto, ["specie"] = testi.specieslist[pk.Species], ["conforme"] = la.Valid };
        if (la.Valid)
        {
            var dati = new byte[pk.SIZE_STORED];
            pk.WriteDecryptedDataStored(dati);
            var file = $"S{box:00}-{posto:00}-{testi.specieslist[pk.Species]}.{pk.Extension}";
            foreach (var c in Path.GetInvalidFileNameChars()) file = file.Replace(c, '_');
            File.WriteAllBytes(Path.Combine(dir, file), dati);
            voce["file"] = file;
            voce["sha256"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant();
            conformi++;
        }
        lista.Add(voce);
    }
    File.WriteAllText(Path.Combine(dir, "rapporto.json"), new JsonObject { ["esemplari"] = lista.Count, ["conformi"] = conformi, ["voci"] = lista }
        .ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
    Console.WriteLine($"esemplari {lista.Count}, conformi estratti {conformi}");
    return 0;
}
