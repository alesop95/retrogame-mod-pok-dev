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
if (args[0] == "--comunita")
    return Comunita(args[1], args[2], args[3]);
if (args[0] == "--serebii")
    return Serebii(args[1], args[2]);
if (args[0] == "--carte")
    return Carte(args[1], args.Skip(2).TakeWhile(x => x != "--produci" && x != "--traccia" && x != "--epoca-cartucce").ToArray());
if (args[0] == "--cartuccia")
    return Cartuccia(args[1], args[2]);
// --carte-specie NUMERO: elenca le carte della libreria di una specie, con titolo, allenatore, ID e regola di cromaticita' (ADR-119)
if (args[0] == "--carte-specie")
{
    var n0 = ushort.Parse(args[1]);
    foreach (var g in EncounterEvent.GetAllEvents(false).Where(g => g.Species == n0 && g.Generation <= 7))
        Console.WriteLine($"G{g.Generation} carta {g.CardID} {g.CardTitle} | {g.OriginalTrainerName} {g.TID16:00000} | lv {g.Level} | cromatico {g.Shiny}");
    return 0;
}
if (args[0] == "--statici")
    return Statici(args[1], args[2], args[3], args.Skip(4).ToArray());

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
        // ADR-120: una voce puo' chiedere la costante di cifratura multipla di un numero, come Dunsparce, che su Scarlatto e
        // Violetto diventa Dudunsparce a tre segmenti se la costante e' multipla di 100. La costante nasce con il trasferimento
        // verso la settima generazione, quindi l'esemplare passa prima in quel formato; il giudizio si rifa' dopo.
        if (pk is not null && e["ec_multiplo"] is { } em)
        {
            var m = (uint)(int)em;
            if (pk.Format < 7)
            {
                var conv = EntityConverter.ConvertToType(pk, typeof(PK7), out var rc);
                if (conv is null) { motivo = "conversione per la costante non riuscita: " + rc; pk = null; }
                else pk = conv;
            }
            if (pk is not null)
            {
                pk.EncryptionConstant = pk.EncryptionConstant / m * m;
                if (pk.EncryptionConstant == 0) pk.EncryptionConstant = m;
                pk.RefreshChecksum();
                var laEc = new LegalityAnalysis(pk);
                if (!laEc.Valid) { motivo = "costante multipla di " + m + " non conforme: " + laEc.Report(); pk = null; }
            }
        }
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
            // Il Flauto Bianco di Rubino Omega e Zaffiro Alpha abbassa il livello dei selvatici fino a 4 (EncounterSlot6AO,
            // IEncounterDownlevel): i livelli minimi della guida degli esemplari sottolivellati vengono da li' (ADR-116)
            byte minimo = enc is IEncounterDownlevel dl ? dl.GetDownleveledMin() : enc.LevelMin;
            if (minimo > livelloMax) continue;
            bool flauto = enc is IEncounterDownlevel && enc.LevelMin > livelloMax;
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
                if (flauto) { pk.MetLevel = (byte)livelloMax; pk.CurrentLevel = (byte)livelloMax; }
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

// I Pokémon specifici della comunità RNG (`_notes/lavoro/rng-comunita-2026-11-04.md`, ADR-115): leggendari e doni fissi di
// terza e quarta generazione, tutti del Metodo 1, con gli IV, la natura, la sfera e la cromaticità dichiarati dal video o dal
// post che li ha resi noti. Per ciascun candidato si risale dagli IV ai semi con LCRNGReversal (un IV a -1 e' libero e si
// prova da 0 a 31), oppure, se la fonte pubblica il seme iniziale e il fotogramma, si rifa' la manipolazione da li' e si cerca
// il fotogramma entro cinque di distanza. La cromaticita' dipende dall'ID segreto: se l'allenatore del candidato non ne fissa
// uno, lo strumento prende quello che rende cromatico il PID trovato e lo scrive nel rapporto, come per il Kyogre di blisy.
int Comunita(string listaJson, string allenatoreJson, string cartella)
{
    var al = JsonNode.Parse(File.ReadAllText(allenatoreJson))!;
    ushort tidP = (ushort)(int)al["tid"]!, sidP = (ushort)(int)al["sid"]!;
    var dir = Directory.CreateDirectory(cartella).FullName;
    var esiti = new JsonArray();
    var semi = new uint[8];
    foreach (var c in JsonNode.Parse(File.ReadAllText(listaJson))!.AsArray())
    {
        string id = (string)c!["id"]!;
        var specie = Enum.Parse<Species>((string)c["specie"]!);
        var ver = Enum.Parse<GameVersion>((string)c["gioco"]!);
        var iv = c["iv"]!.AsArray().Select(x => (int)x!).ToArray(); // PS, Attacco, Difesa, Att. Sp., Dif. Sp., Velocita'
        string? natura = (string?)c["natura"];
        bool cromatico = (bool?)c["cromatico"] ?? false;
        string ot = (string?)c["ot"] ?? (string)al["nome"]!;
        ushort tid = c["tid"] is { } t ? (ushort)(int)t : tidP;
        ushort? sidFisso = c["sid"] is { } s ? (ushort)(int)s : null;
        int lingua = (string?)c["lingua"] switch { "ja" => (int)LanguageID.Japanese, "en" => (int)LanguageID.English, "fr" => (int)LanguageID.French,
            "de" => (int)LanguageID.German, "es" => (int)LanguageID.Spanish, "ko" => (int)LanguageID.Korean, _ => (int)LanguageID.Italian };
        var esito = new JsonObject { ["id"] = id, ["specie"] = specie.ToString(), ["gioco"] = ver.ToString(), ["ot"] = ot, ["tid"] = tid,
            ["fonte"] = (string?)c["fonte"], ["storia"] = (string?)c["storia"] };
        esiti.Add(esito);
        // un candidato prodotto da un'altra modalita', come il Kyogre di --kyogre: resta nel rapporto per la sua storia
        if (c["gia_prodotto"] is { } gp) { esito["esito"] = "già prodotto in " + (string)gp!; esito["pid"] = (string?)c["pid"]; continue; }
        // Un PID calcolato fuori dallo strumento (2026-11-09): il Rayquaza di Pokémon Box viene dal Metodo 4, che la libreria
        // ammette per gli statici di Rubino e Zaffiro proprio perché Pokémon Box li emula. Si prende l'incontro che la libreria
        // costruisce, si mettono PID, ID segreto, IV e sfera dati, e decide il verificatore.
        if ((string?)c["metodo"] == "pid")
        {
            uint pidDato = Convert.ToUInt32((string)c["pid"]!, 16);
            var trp = new SimpleTrainerInfo(ver) { OT = ot, TID16 = tid, SID16 = sidFisso ?? sidP, Language = lingua };
            var mp = EntityBlank.GetBlank(3); mp.Species = (ushort)specie; mp.Language = lingua;
            string ultimoP = "nessun incontro";
            foreach (var e0 in EncounterMovesetGenerator.GenerateEncounters(mp, trp, ReadOnlyMemory<ushort>.Empty, ver))
            {
                var pk = e0.ConvertToPKM(trp);
                pk.PID = pidDato; pk.SID16 = sidFisso ?? sidP;
                pk.IV_HP = iv[0]; pk.IV_ATK = iv[1]; pk.IV_DEF = iv[2]; pk.IV_SPA = iv[3]; pk.IV_SPD = iv[4]; pk.IV_SPE = iv[5];
                if (c["sfera"] is { } sfp) pk.Ball = (byte)Enum.Parse<Ball>((string)sfp!);
                pk.RefreshAbility(pk.AbilityNumber >> 1);
                pk.RefreshChecksum();
                var lap = new LegalityAnalysis(pk);
                if (!lap.Valid) { ultimoP = e0.LongName + ": " + lap.Report(); continue; }
                var datiP = new byte[pk.SIZE_STORED]; pk.WriteDecryptedDataStored(datiP);
                var fileP = $"{id}-{specie}{(pk.IsShiny ? "-cromatico" : "")}.{pk.Extension}";
                File.WriteAllBytes(Path.Combine(dir, fileP), datiP);
                esito["esito"] = "prodotto"; esito["file"] = fileP; esito["sha256"] = Convert.ToHexString(SHA256.HashData(datiP)).ToLowerInvariant();
                esito["pid"] = pk.PID.ToString("X8"); esito["natura"] = pk.Nature.ToString(); esito["iv"] = string.Join("/", iv);
                esito["sid"] = pk.SID16; esito["cromatico"] = pk.IsShiny; esito["incontro"] = e0.LongName;
                break;
            }
            esito["esito"] ??= "non prodotto: " + ultimoP;
            Console.WriteLine($"{id} {specie} {ver}: {esito["esito"]} {esito["pid"]}");
            continue;
        }
        // Fuori dal Metodo 1 (ADR-116): Colosseum, i doni dei dischi, la quarta, sesta e settima generazione e la Console
        // Virtuale. Si chiedono alla libreria gli IV, la natura e la cromaticita' come criteri, e la libreria cerca da se' il
        // seme dove il metodo lo prevede; si tiene il primo incontro che li rispetta e che il verificatore accetta.
        if ((string?)c["metodo"] == "criteri")
        {
            byte g0 = ver switch { GameVersion.RD or GameVersion.BU or GameVersion.GN or GameVersion.YW => 1, GameVersion.GD or GameVersion.SI or GameVersion.C => 2,
                GameVersion.D or GameVersion.P or GameVersion.Pt or GameVersion.HG or GameVersion.SS => 4, GameVersion.X or GameVersion.Y or GameVersion.OR or GameVersion.AS => 6,
                GameVersion.SN or GameVersion.MN or GameVersion.US or GameVersion.UM => 7, _ => 3 };
            var crit = EncounterCriteria.Unrestricted with { Gender = c["sesso"] is { } gx ? (Gender)(int)gx! : Gender.Random, IV_HP = (sbyte)iv[0], IV_ATK = (sbyte)iv[1], IV_DEF = (sbyte)iv[2], IV_SPA = (sbyte)iv[3], IV_SPD = (sbyte)iv[4], IV_SPE = (sbyte)iv[5],
                Nature = natura is null ? Nature.Random : Enum.Parse<Nature>(natura), Shiny = cromatico ? Shiny.Always : Shiny.Never };
            var trc = new SimpleTrainerInfo(ver == GameVersion.CXD ? GameVersion.E : ver) { OT = ot, TID16 = tid, SID16 = sidFisso ?? sidP, Language = lingua };
            var m0 = EntityBlank.GetBlank(g0); m0.Species = (ushort)specie; m0.Language = lingua;
            if (c["forma"] is { } fm) m0.Form = (byte)(int)fm!;
            string filtro = (string?)c["incontro"] ?? "";
            string ultimo = "nessun incontro";
            foreach (var e0 in EncounterMovesetGenerator.GenerateEncounters(m0, trc, ReadOnlyMemory<ushort>.Empty, ver))
            {
                if (filtro.Length > 0 && !(e0.LongName + " " + e0.GetType().Name).Contains(filtro)) continue;
                if (c["carta"] is { } cartaN && !(e0 is MysteryGift mgc && mgc.CardID == (int)cartaN!)) continue;
                for (int tent = 0; tent < (c["sesso"] is null ? (cromatico ? 20000 : 3) : 12); tent++)
                {
                    PKM pk;
                    try { pk = e0.ConvertToPKM(trc, crit); } catch (Exception ex) { ultimo = ex.Message; continue; }
                    if (pk is CK3 ck3) pk = ck3.ConvertToPK3(); else if (pk is XK3 xk3) pk = xk3.ConvertToPK3();
                    // Dal 2026-11-07 (ADR-119): un esemplare documentato si riproduce con il suo livello e luogo d'incontro,
                    // le sue mosse e il suo sesso, come i Pokemon di JEREMY del Trade and Battle Day; il verificatore decide.
                    if (c["livello"] is { } lvN)
                    {
                        int lv = (int)lvN!;
                        if (lv < e0.LevelMin || lv > e0.LevelMax) { ultimo = e0.LongName + ": livello " + lv + " fuori da " + e0.LevelMin + "-" + e0.LevelMax; break; }
                        pk.MetLevel = (byte)lv; pk.CurrentLevel = (byte)lv;
                    }
                    // il livello attuale di un esemplare allenato dopo l'incontro (ADR-119): l'incontro resta quello che la libreria sceglie
                    if (c["livello_attuale"] is { } laN)
                    {
                        int la1 = (int)laN!;
                        if (la1 < pk.MetLevel) { ultimo = e0.LongName + ": livello d'incontro " + pk.MetLevel + " sopra " + la1; continue; }
                        pk.CurrentLevel = (byte)la1;
                    }
                    if (c["luogo"] is { } lu)
                    {
                        var nl = inglese.GetLocationName(false, pk.MetLocation, pk.Format, pk.Generation, pk.Version);
                        if (!nl.Contains((string)lu!, StringComparison.OrdinalIgnoreCase)) { ultimo = e0.LongName + ": luogo " + nl; break; }
                    }
                    if (c["mosse"] is JsonArray ma)
                    {
                        var ids = new ushort[4];
                        for (int k = 0; k < ma.Count && k < 4; k++) ids[k] = (ushort)Array.FindIndex(inglese.movelist.ToArray(), x => string.Equals(x.Replace(" ", ""), ((string)ma[k]!).Replace(" ", ""), StringComparison.OrdinalIgnoreCase));
                        pk.SetMoves(ids); pk.HealPP();
                    }
                    if (c["sesso"] is { } sx && pk.Gender != (int)sx!) { ultimo = e0.LongName + ": sesso"; continue; }
                    // Dal 2026-11-07 (ADR-119): la libreria costruisce la specie dell'incontro, che puo' essere una pre-evoluzione
                    // di quella chiesta (Machoke per Machamp, Feebas per Milotic). Si evolve nella specie chiesta, come avrebbe
                    // fatto chi lo riceveva, e decide il verificatore; una specie diversa non si accetta mai.
                    if (pk.Species != (ushort)specie)
                    {
                        pk.Species = (ushort)specie;
                        pk.RefreshAbility(pk.AbilityNumber >> 1);
                        if (!pk.IsNicknamed) pk.SetDefaultNickname();
                        pk.RefreshChecksum();
                        esito["evoluto_da"] = testi.specieslist[e0.Species];
                    }
                    if (cromatico && !pk.IsShiny) { ultimo = e0.LongName + ": non cromatico"; continue; }
                    if (!cromatico && pk.IsShiny && pk.Format >= 3) { pk.SetPIDGender(pk.Gender); if (pk.IsShiny) { ultimo = e0.LongName + ": cromatico non chiesto"; continue; } }
                    if (natura is not null && pk.Nature.ToString() != natura && pk.Format >= 3) { ultimo = e0.LongName + ": natura diversa"; continue; }
                    int[] v = { pk.IV_HP, pk.IV_ATK, pk.IV_DEF, pk.IV_SPA, pk.IV_SPD, pk.IV_SPE };
                    if (pk.Format >= 3 && Enumerable.Range(0, 6).Any(i => iv[i] >= 0 && iv[i] != v[i])) { ultimo = e0.LongName + ": IV diversi " + string.Join("/", v); continue; }
                    if (c["sfera"] is { } sf0) pk.Ball = (byte)Enum.Parse<Ball>((string)sf0!);
                    pk.RefreshChecksum();
                    var la0 = new LegalityAnalysis(pk);
                    if (!la0.Valid) { ultimo = e0.LongName + ": " + la0.Report(); continue; }
                    var dati0 = new byte[pk.SIZE_STORED]; pk.WriteDecryptedDataStored(dati0);
                    var file0 = $"{id}-{specie}{(pk.IsShiny ? "-cromatico" : "")}.{pk.Extension}";
                    File.WriteAllBytes(Path.Combine(dir, file0), dati0);
                    esito["esito"] = "prodotto"; esito["file"] = file0; esito["sha256"] = Convert.ToHexString(SHA256.HashData(dati0)).ToLowerInvariant();
                    esito["pid"] = pk.PID.ToString("X8"); esito["natura"] = pk.Nature.ToString(); esito["iv"] = string.Join("/", v);
                    esito["sid"] = pk.SID16; esito["cromatico"] = pk.IsShiny; esito["incontro"] = e0.LongName;
                    break;
                }
                if (esito["file"] is not null) break;
            }
            esito["esito"] ??= "non prodotto: " + ultimo;
            Console.WriteLine($"{id} {specie} {ver}: {esito["esito"]} {esito["iv"]} {esito["natura"]}");
            continue;
        }
        var tr = new SimpleTrainerInfo(ver) { OT = ot, TID16 = tid, SID16 = sidFisso ?? sidP, Language = lingua };
        byte gen = ver is GameVersion.D or GameVersion.P or GameVersion.Pt or GameVersion.HG or GameVersion.SS ? (byte)4 : (byte)3;
        var modello = EntityBlank.GetBlank(gen); modello.Species = (ushort)specie; modello.Language = lingua;
        var enc = EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, ver)
            .FirstOrDefault(x => x.GetType().Name.Contains("Static") && !x.LongName.Contains("Roam"));
        if (enc is null) { esito["esito"] = "nessun incontro fisso nella libreria"; continue; }
        esito["incontro"] = enc.LongName;
        // i semi candidati: quelli del fotogramma pubblicato, oppure quelli risaliti dagli IV
        var candidati = new List<(uint seme, int fotogramma)>();
        if (c["seme_iniziale"] is { } si && c["fotogramma"] is { } fo)
        {
            uint s0 = Convert.ToUInt32((string)si!, 16);
            for (int f = (int)fo - 5; f <= (int)fo + 5; f++)
            {
                uint r0 = LCRNG.Advance(s0, f), r1 = LCRNG.Next(r0), r2 = LCRNG.Next(r1), r3 = LCRNG.Next(r2), r4 = LCRNG.Next(r3);
                uint a1 = r3 >> 16, a2 = r4 >> 16;
                int[] v = { (int)(a1 & 31), (int)((a1 >> 5) & 31), (int)((a1 >> 10) & 31), (int)((a2 >> 5) & 31), (int)((a2 >> 10) & 31), (int)(a2 & 31) };
                if (Enumerable.Range(0, 6).All(i => iv[i] < 0 || iv[i] == v[i])) candidati.Add((r2, f));
            }
        }
        else
        {
            var liberi = Enumerable.Range(0, 6).Where(i => iv[i] < 0).ToArray();
            for (int comb = 0; comb < 1 << (5 * liberi.Length); comb++)
            {
                var v = (int[])iv.Clone();
                for (int j = 0; j < liberi.Length; j++) v[liberi[j]] = (comb >> (5 * j)) & 31;
                int k = LCRNGReversal.GetSeedsIVs(semi, (uint)v[0], (uint)v[1], (uint)v[2], (uint)v[3], (uint)v[4], (uint)v[5]);
                for (int i = 0; i < k; i++) candidati.Add((semi[i], -1));
            }
        }
        esito["semi_provati"] = candidati.Count;
        foreach (var (seme, fotogramma) in candidati)
        {
            uint alto = seme >> 16, basso = LCRNG.Prev(seme) >> 16, pid = (alto << 16) | basso;
            if (natura is not null && ((Nature)(pid % 25)).ToString() != natura) continue;
            ushort sid = sidFisso ?? sidP;
            if (cromatico && (tid ^ sid ^ alto ^ basso) >= 8)
            {
                if (sidFisso is not null) continue;
                // l'ID segreto che rende cromatico questo PID; in Rubino e Zaffiro deve essere una coppia che MethodH ammette
                bool trovato = false;
                for (int x = 0; x < 8 && !trovato; x++)
                {
                    var cand = (ushort)(tid ^ alto ^ basso ^ x);
                    if (ver is not (GameVersion.R or GameVersion.S) || MethodH.TryGetSeedTrainerID(tid, cand, out _)) { sid = cand; trovato = true; }
                }
                if (!trovato) continue;
            }
            var pk = enc.ConvertToPKM(new SimpleTrainerInfo(ver) { OT = ot, TID16 = tid, SID16 = sid, Language = lingua }, EncounterCriteria.Unrestricted);
            pk.SID16 = sid;
            pk.PID = pid;
            uint i1 = LCRNG.Next(seme) >> 16, i2 = LCRNG.Next(LCRNG.Next(seme)) >> 16;
            pk.IV_HP = (int)(i1 & 31); pk.IV_ATK = (int)((i1 >> 5) & 31); pk.IV_DEF = (int)((i1 >> 10) & 31);
            pk.IV_SPE = (int)(i2 & 31); pk.IV_SPA = (int)((i2 >> 5) & 31); pk.IV_SPD = (int)((i2 >> 10) & 31);
            pk.RefreshAbility((int)(pid & 1));
            if (c["sfera"] is { } sf) pk.Ball = (byte)Enum.Parse<Ball>((string)sf!);
            if (pk.Species == (ushort)Species.Giratina && pk.Form == 1) pk.HeldItem = 112; // la Grigiosfera tiene la forma Origine
            if (c["pv_tipo"] is { } pt && (pk.HPType != (int)pt || pk.HPPower != (int)c["pv_potenza"]!)) continue;
            pk.RefreshChecksum();
            var la = new LegalityAnalysis(pk);
            if (!la.Valid) { esito["rapporto"] = la.Report(); continue; }
            esito.Remove("rapporto");
            var dati = new byte[pk.SIZE_STORED]; pk.WriteDecryptedDataStored(dati);
            var file = $"{id}-{specie}{(pk.IsShiny ? "-cromatico" : "")}.{pk.Extension}";
            File.WriteAllBytes(Path.Combine(dir, file), dati);
            esito["esito"] = "prodotto"; esito["file"] = file; esito["sha256"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant();
            esito["seme"] = seme.ToString("X8"); esito["pid"] = pid.ToString("X8"); esito["natura"] = ((Nature)(pid % 25)).ToString();
            esito["iv"] = $"{pk.IV_HP}/{pk.IV_ATK}/{pk.IV_DEF}/{pk.IV_SPA}/{pk.IV_SPD}/{pk.IV_SPE}";
            esito["sid"] = sid; esito["cromatico"] = pk.IsShiny; esito["sfera"] = ((Ball)pk.Ball).ToString();
            if (fotogramma >= 0) esito["fotogramma"] = fotogramma;
            break;
        }
        esito["esito"] ??= "nessun seme conforme alla specifica";
        Console.WriteLine($"{id} {specie} {ver}: {esito["esito"]} {esito["iv"]} {esito["natura"]} sid {esito["sid"]} {esito["fotogramma"]}");
    }
    File.WriteAllText(Path.Combine(dir, "rapporto.json"), new JsonObject { ["esiti"] = esiti }
        .ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }));
    return 0;
}

// Gli eventi dell'Eventdex di Serebii che le copie non hanno (`_notes/lavoro/serebii-eventdex-confronto-2026-11-04.md`): per
// ciascuno con allenatore e ID noti si chiede alla libreria se conosce una carta della stessa specie con lo stesso ID, fra le
// carte di quarta, quinta, sesta e settima generazione e i doni di terza. Solo un evento che la libreria conosce si produce
// conforme; gli altri esistono nella storia delle distribuzioni ma il verificatore li contesterebbe.
int Serebii(string mancantiJson, string uscita)
{
    var carte = EncounterEvent.GetAllEvents(false).Where(g => g.Generation is >= 4 and <= 7 && g is not WB7).ToList();
    var gen3 = new[] { GameVersion.R, GameVersion.S, GameVersion.E, GameVersion.FR, GameVersion.LG };
    var esiti = new JsonArray();
    int trovati = 0, confrontati = 0;
    foreach (var m in JsonNode.Parse(File.ReadAllText(mancantiJson))!.AsArray())
    {
        if (!((bool?)m!["confrontabile"] ?? false)) continue;
        confrontati++;
        int numero = (int)m["numero"]!;
        var ids = (m["id"] is JsonArray a ? a.Select(x => (string)x!) : new[] { (string)m["id"]! })
            .Select(x => int.TryParse(x, out var v) ? v : -1).Where(v => v >= 0).ToHashSet();
        var corrispondenze = new List<string>();
        var incontri = new List<(IEncounterable enc, GameVersion v)>();
        foreach (var g in carte.Where(g => g.Species == numero && ids.Contains(g.TID16)))
        {
            corrispondenze.Add($"G{g.Generation} {g.CardTitle} {g.OriginalTrainerName} {g.TID16:00000}{(g.IsEgg ? " uovo" : "")}");
            incontri.Add((g, g.Generation switch { 4 => GameVersion.HG, 5 => GameVersion.B2, 6 => GameVersion.OR, _ => GameVersion.US }));
        }
        string giochi = m["giochi"] is JsonArray ga ? string.Join(",", ga.Select(x => (string)x!)) : (string?)m["giochi"] ?? "";
        if (corrispondenze.Count == 0 && System.Text.RegularExpressions.Regex.IsMatch(giochi, "Ruby|Sapphire|Emerald|FireRed|LeafGreen"))
        {
            var modello = EntityBlank.GetBlank(3); modello.Species = (ushort)numero;
            foreach (var v in gen3)
            {
                var tr = new SimpleTrainerInfo(v) { OT = "Alessio", TID16 = 42317, SID16 = 58164, Language = (int)LanguageID.Japanese };
                foreach (var enc in EncounterMovesetGenerator.GenerateEncounters(modello, tr, ReadOnlyMemory<ushort>.Empty, v))
                {
                    if (!enc.GetType().Name.Contains("Gift")) continue;
                    // la libreria schiude da se' gli uovi di terza generazione con l'allenatore della sua cache, PKHeX per difetto (ADR-119)
                    RecentTrainerCache.SetRecentTrainer(tr);
                    var pk = enc.ConvertToPKM(tr, EncounterCriteria.Unrestricted);
                    if (ids.Contains(pk.TID16)) { corrispondenze.Add($"G3 {enc.LongName} {pk.OriginalTrainerName} {pk.TID16:00000} ({v})"); incontri.Add((enc, v)); }
                }
            }
        }
        var voce = new JsonObject { ["numero"] = numero, ["specie"] = (string?)m["specie"], ["evento"] = (string?)m["evento"],
            ["regione"] = (string?)m["regione"], ["data_inizio"] = (string?)m["data_inizio"], ["giochi"] = giochi,
            ["id"] = string.Join(",", ids), ["url"] = (string?)m["url"],
            ["in_libreria"] = corrispondenze.Count > 0, ["carte"] = new JsonArray(corrispondenze.Distinct().Select(x => (JsonNode?)JsonValue.Create(x)).ToArray()) };
        if (corrispondenze.Count > 0) trovati++;
        esiti.Add(voce);
        int ip = Array.IndexOf(args, "--produci");
        if (ip < 0 || incontri.Count == 0) continue;
        // si produce dal primo incontro che, con una delle lingue e una delle versioni provate, esce conforme
        var dir = Directory.CreateDirectory(args[ip + 1]).FullName;
        var lingue = new[] { LanguageID.Japanese, LanguageID.Korean, LanguageID.English, LanguageID.Italian, LanguageID.French, LanguageID.German, LanguageID.Spanish, LanguageID.ChineseS, LanguageID.ChineseT };
        foreach (var (enc, v0) in incontri)
        {
            var versioni = enc is MysteryGift mg0 ? (mg0.Generation switch
                { 4 => new[] { GameVersion.HG, GameVersion.SS, GameVersion.Pt, GameVersion.D, GameVersion.P },
                  5 => new[] { GameVersion.B2, GameVersion.W2, GameVersion.B, GameVersion.W },
                  6 => new[] { GameVersion.OR, GameVersion.AS, GameVersion.X, GameVersion.Y },
                  _ => new[] { GameVersion.US, GameVersion.UM, GameVersion.SN, GameVersion.MN } }) : new[] { v0 };
            PKM? buono = null;
            foreach (var v in versioni)
            foreach (var lg in lingue)
            {
                if (buono is not null) break;
                if (v is GameVersion.US or GameVersion.UM or GameVersion.SN or GameVersion.MN or GameVersion.OR or GameVersion.AS or GameVersion.X or GameVersion.Y)
                    if (lg is LanguageID.ChineseS or LanguageID.ChineseT && v is not (GameVersion.US or GameVersion.UM or GameVersion.SN or GameVersion.MN)) continue;
                if (lg is LanguageID.ChineseS or LanguageID.ChineseT && v is not (GameVersion.US or GameVersion.UM or GameVersion.SN or GameVersion.MN)) continue;
                var tr = new SimpleTrainerInfo(v) { OT = lg is LanguageID.Japanese ? "アレッシオ" : "Alessio", TID16 = 42317, SID16 = 58164, Language = (int)lg };
                var pk = enc.ConvertToPKM(tr, EncounterCriteria.Unrestricted);
                if (new LegalityAnalysis(pk).Valid) buono = pk;
            }
            if (buono is null) continue;
            var dati = new byte[buono.SIZE_STORED]; buono.WriteDecryptedDataStored(dati);
            var nome = $"{esiti.Count:000}-{(string?)m["specie"]}.{buono.Extension}";
            foreach (var c in Path.GetInvalidFileNameChars()) nome = nome.Replace(c, '_');
            File.WriteAllBytes(Path.Combine(dir, nome), dati);
            voce["file"] = nome; voce["pid"] = buono.PID.ToString("X8"); voce["sha256"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant();
            voce["storia"] = $"{(string?)m["evento"]}, {(string?)m["regione"]}, dal {(string?)m["data_inizio"]}: allenatore {buono.OriginalTrainerName}, ID {buono.TID16:00000}, nei giochi {giochi}.";
            voce["fonte"] = (string?)m["url"];
            break;
        }
    }
    File.WriteAllText(uscita, new JsonObject { ["confrontati"] = confrontati, ["nella_libreria"] = trovati, ["voci"] = esiti }
        .ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }));
    Console.WriteLine($"eventi confrontabili {confrontati}, con una carta della libreria {trovati}");
    return 0;
}

// Tutti gli eventi che la libreria conosce fino alla settima generazione, confrontati con le copie (ADR-116): le carte di
// quarta, quinta, sesta e settima generazione, i doni di terza (internazionali, giapponesi, PCNY, PCJP, Colosseum) e quelli
// del Game Boy. Per ogni esemplare conforme delle copie la libreria dice da quale incontro viene; un evento e' coperto se
// almeno un esemplare viene da lui o da una sua variante della stessa carta in un'altra lingua. Gli eventi scoperti si
// scrivono nel rapporto e, con --produci CARTELLA, si producono dal primo modo che il verificatore accetta.
int Carte(string uscita, string[] copie)
{
    // --epoca-cartucce: i doni del Game Boy si giudicano come su cartuccia, dove esistono, per i lotti da scrivere sulle
    // cartucce di Rosso e Argento dopo la sostituzione della pila (ADR-117); nel contesto della Console Virtuale non esistono
    if (args.Contains("--epoca-cartucce")) ParseSettings.AllowEraCartGB = true;
    var tutti = new List<(IEncounterable enc, string gruppo, string descrizione)>();
    foreach (var g in EncounterEvent.GetAllEvents(false).Where(g => g.Generation is >= 4 and <= 7 && g is not WB7))
        tutti.Add((g, $"G{g.Generation}|{g.CardID}|{g.Species}|{g.Form}", $"G{g.Generation} carta {g.CardID} «{g.CardTitle}» {testi.specieslist[g.Species]} {g.OriginalTrainerName} {g.TID16:00000}{(g.IsEgg ? " uovo" : "")}{(g.IsShiny ? " cromatico" : "")}"));
    var asm = typeof(EncounterEvent).Assembly;
    IEnumerable<object> campo(string tipo, string nome) =>
        (asm.GetType("PKHeX.Core." + tipo)?.GetField(nome, System.Reflection.BindingFlags.Static | System.Reflection.BindingFlags.Public | System.Reflection.BindingFlags.NonPublic)?.GetValue(null) as System.Collections.IEnumerable)?.Cast<object>() ?? [];
    foreach (var (tipo, nome) in new[] { ("EncountersWC3", "Encounter_WC3"), ("EncountersWC3", "PCNY"), ("EncountersWC3", "PCJP"), ("Encounters3Colo", "Gifts"), ("Encounters1GBEra", "Gifts"), ("Encounters2GBEra", "Gifts") })
        foreach (var o in campo(tipo, nome))
            if (o is IEncounterable e)
            {
                string ot = o.GetType().GetProperty("OriginalTrainerName")?.GetValue(o)?.ToString() ?? "";
                string id = o.GetType().GetProperty("TID16")?.GetValue(o)?.ToString() ?? "";
                string mv = o.GetType().GetProperty("Moves")?.GetValue(o)?.ToString() ?? "";
                // dal 2026-11-07 (ADR-119) anche livello e mosse distinguono le varianti: a New York la stessa specie usci'
                // in settimane diverse con livello e mosse diversi, e il raggruppamento di prima le fondeva in una sola
                tutti.Add((e, $"{tipo}.{nome}|{e.Species}|{e.Form}|{ot}|{id}|{e.LongName}|{e.LevelMin}|{mv}", $"{tipo}.{nome} {e.LongName} {testi.specieslist[e.Species]} {ot} {id} ({e.Version})"));
            }
    Console.WriteLine($"eventi della libreria fino alla settima generazione: {tutti.Count}, gruppi {tutti.Select(x => x.gruppo).Distinct().Count()}");
    // gli incontri riconosciuti negli esemplari conformi delle copie
    var visti = new HashSet<object>(ReferenceEqualityComparer.Instance);
    var gruppiVisti = new HashSet<string>();
    var perGruppo = tutti.GroupBy(x => x.enc, ReferenceEqualityComparer.Instance).ToDictionary(g => g.Key!, g => g.First().gruppo, ReferenceEqualityComparer.Instance);
    int esemplari = 0;
    int it = Array.IndexOf(args, "--traccia");
    using var traccia = it >= 0 ? new StreamWriter(args[it + 1]) : null;
    foreach (var c in copie)
    {
        var sav = SaveUtil.GetSaveFile(c) ?? throw new InvalidOperationException("salvataggio non letto: " + c);
        for (int i = 0; i < sav.SlotCount; i++)
        {
            var pk = sav.GetBoxSlotAtIndex(i);
            if (pk.Species == 0) continue;
            var la = new LegalityAnalysis(pk);
            if (!la.Valid) continue;
            esemplari++;
            var enc = la.EncounterMatch;
            visti.Add(enc);
            traccia?.WriteLine($"{c}|{i}|{testi.specieslist[pk.Species]}|{enc.GetType().Name}|{enc.LongName}|{(enc is MysteryGift m0 ? m0.CardID + "|" + m0.Generation : "")}");
            if (perGruppo.TryGetValue(enc, out var gr)) gruppiVisti.Add(gr);
            else if (enc is MysteryGift mg) gruppiVisti.Add($"G{mg.Generation}|{mg.CardID}|{mg.Species}|{mg.Form}");
        }
    }
    var mancanti = tutti.Where(x => !gruppiVisti.Contains(x.gruppo)).GroupBy(x => x.gruppo).ToList();
    Console.WriteLine($"esemplari conformi letti {esemplari}, gruppi coperti {gruppiVisti.Count}, gruppi scoperti {mancanti.Count}");
    var lista = new JsonArray();
    int ip = Array.IndexOf(args, "--produci");
    string? dir = ip >= 0 ? Directory.CreateDirectory(args[ip + 1]).FullName : null;
    var lingue = new[] { LanguageID.Japanese, LanguageID.English, LanguageID.Korean, LanguageID.Italian, LanguageID.French, LanguageID.German, LanguageID.Spanish, LanguageID.ChineseS, LanguageID.ChineseT };
    int prodotti = 0, n = 0;
    foreach (var g in mancanti)
    {
        n++;
        var voce = new JsonObject { ["gruppo"] = g.Key, ["descrizione"] = g.First().descrizione, ["varianti"] = g.Count() };
        lista.Add(voce);
        if (dir is null) continue;
        PKM? buono = null; string rapporto = "";
        foreach (var (enc, _, _) in g)
        {
            byte gen = enc.Generation;
            var versioni = gen switch
            {
                1 => new[] { GameVersion.RD, GameVersion.BU, GameVersion.YW, GameVersion.GN },
                2 => new[] { GameVersion.GD, GameVersion.SI, GameVersion.C },
                // un uovo dono di terza generazione la libreria lo schiude da se' se chi lo riceve non e' di terza generazione
                3 when enc.IsEgg => new[] { GameVersion.Pt, GameVersion.HG },
                3 => new[] { GameVersion.E, GameVersion.R, GameVersion.S, GameVersion.FR, GameVersion.LG, GameVersion.CXD },
                4 => new[] { GameVersion.HG, GameVersion.SS, GameVersion.Pt, GameVersion.D, GameVersion.P },
                5 => new[] { GameVersion.B2, GameVersion.W2, GameVersion.B, GameVersion.W },
                6 => new[] { GameVersion.OR, GameVersion.AS, GameVersion.X, GameVersion.Y },
                _ => new[] { GameVersion.US, GameVersion.UM, GameVersion.SN, GameVersion.MN },
            };
            foreach (var v in versioni)
            foreach (var lg in lingue)
            {
                if (buono is not null) break;
                if (lg is LanguageID.ChineseS or LanguageID.ChineseT && gen != 7) continue;
                if (lg is LanguageID.Korean && gen < 4) continue;
                var tr = new SimpleTrainerInfo(v == GameVersion.CXD ? GameVersion.E : v) { OT = lg is LanguageID.Japanese ? "アレッシオ" : "Alessio", TID16 = 42317, SID16 = 58164, Language = (int)lg };
                try
                {
                    // la libreria schiude da se' gli uovi di terza generazione con l'allenatore della sua cache, PKHeX per difetto (ADR-119)
                    RecentTrainerCache.SetRecentTrainer(tr);
                    var pk = enc.ConvertToPKM(tr, EncounterCriteria.Unrestricted);
                    // un uovo non passa il Trasportatore: si schiude, come farebbe chi lo riceve, e la data deve essere vera
                    if (pk.IsEgg && pk.Format >= 4) pk.ForceHatchPKM(tr);
                    var la = new LegalityAnalysis(pk);
                    if (!la.Valid && la.Report().Contains("Met Date") && pk.Format >= 4)
                    {
                        pk.MetDate = DateOnly.FromDateTime(DateTime.Today);
                        if (pk.WasEgg && pk.EggMetDate is null) pk.EggMetDate = pk.MetDate;
                        la = new LegalityAnalysis(pk);
                    }
                    if (la.Valid) buono = pk; else rapporto = la.Report();
                }
                catch (Exception ex) { rapporto = ex.Message; }
            }
            if (buono is not null) break;
        }
        if (buono is null) { voce["esito"] = "non prodotto"; voce["rapporto"] = rapporto; continue; }
        var dati = new byte[buono.SIZE_STORED]; buono.WriteDecryptedDataStored(dati);
        var nome = $"{n:0000}-{testi.specieslist[buono.Species]}.{buono.Extension}";
        foreach (var ch in Path.GetInvalidFileNameChars()) nome = nome.Replace(ch, '_');
        File.WriteAllBytes(Path.Combine(dir, nome), dati);
        voce["esito"] = "prodotto"; voce["file"] = nome; voce["pid"] = buono.PID.ToString("X8");
        voce["sha256"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant();
        voce["storia"] = g.First().descrizione + ", evento che le copie non avevano, prodotto dalla libreria (ADR-116).";
        prodotti++;
    }
    File.WriteAllText(uscita, new JsonObject { ["eventi"] = tutti.Count, ["gruppi_coperti"] = gruppiVisti.Count, ["gruppi_scoperti"] = mancanti.Count,
        ["prodotti"] = prodotti, ["esemplari_letti"] = esemplari, ["voci"] = lista }
        .ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }));
    Console.WriteLine($"prodotti {prodotti}");
    return 0;
}

// Gli statici, i doni e le uova dono della libreria dalla prima alla settima generazione (ADR-106, rimasti da produrre fino al
// 2026-11-07, ADR-119): gli stessi modelli che tools/pkhex-conta-incontri conta, tolti scambi e Ombre gia' prodotti. Un modello
// si considera coperto se un esemplare conforme delle copie per HOME lo ha come incontro riconosciuto; i modelli gemelli fra
// versioni sorelle (stessa classe, generazione, specie, forma, livello, luogo, cromaticita' e sfera fissa) valgono un esemplare
// solo, e un gruppo e' coperto se lo e' uno qualunque dei suoi gemelli. Per gli altri si costruisce l'esemplare con
// l'allenatore del progetto, nella versione del modello, e lo si tiene solo se il verificatore lo giudica conforme.
// Uso: --statici ALLENATORE.json RAPPORTO.json CARTELLA_DI_USCITA COPIA [COPIA ...]
int Statici(string allenatoreJson, string uscita, string cartella, string[] copie)
{
    var al = JsonNode.Parse(File.ReadAllText(allenatoreJson))!;
    ushort tidP = (ushort)(int)al["tid"]!, sidP = (ushort)(int)al["sid"]!;
    string nomeP = (string)al["nome"]!;
    var asm = typeof(PKM).Assembly;
    var modelli = new List<(IEncounterTemplate enc, string classe, string gruppo)>();
    var arrVisti = new HashSet<object>(ReferenceEqualityComparer.Instance);
    object? prop(object o, string n) => o.GetType().GetProperty(n)?.GetValue(o);
    foreach (var t in asm.GetTypes().Where(t => t.IsClass && t.Name.StartsWith("Encounters")))
    foreach (var f in t.GetFields(System.Reflection.BindingFlags.Public | System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Static))
    {
        object? v; try { v = f.GetValue(null); } catch { continue; }
        if (v is not Array arr || arr.Length == 0) continue;
        var el = arr.GetType().GetElementType()!;
        if (!typeof(IEncounterTemplate).IsAssignableFrom(el)) continue;
        string tipo = el.Name;
        if (!(tipo.StartsWith("EncounterStatic") || tipo.StartsWith("EncounterGift") || tipo.StartsWith("EncounterEgg"))) continue;
        if (!arrVisti.Add(arr)) continue;
        foreach (var o in arr)
        {
            var e = (IEncounterTemplate)o!;
            if (e.Generation is < 1 or > 7) continue;
            string classe = tipo.StartsWith("EncounterGift") ? "dono" : tipo.StartsWith("EncounterEgg") ? "uovo" : "statico";
            if (classe == "statico" && tipo.Contains("Gift")) classe = "dono";
            string gruppo = $"{classe}|{tipo}|G{e.Generation}|{e.Species}|{e.Form}|{e.LevelMin}|{prop(o, "Location")}|{prop(o, "Shiny")}|{prop(o, "FixedBall")}|{e.IsEgg}|{prop(o, "Gift")}";
            modelli.Add((e, classe, gruppo));
        }
    }
    Console.WriteLine($"modelli statici, doni e uova fino alla settima generazione: {modelli.Count}, gruppi {modelli.Select(x => x.gruppo).Distinct().Count()}");
    var gruppoDi = new Dictionary<object, string>(ReferenceEqualityComparer.Instance);
    foreach (var m in modelli) gruppoDi[m.enc] = m.gruppo;
    var coperti = new HashSet<string>();
    int letti = 0;
    foreach (var c in copie)
    {
        var sav = SaveUtil.GetSaveFile(c) ?? throw new InvalidOperationException("salvataggio non letto: " + c);
        for (int i = 0; i < sav.SlotCount; i++)
        {
            var pk = sav.GetBoxSlotAtIndex(i);
            if (pk.Species == 0) continue;
            var la = new LegalityAnalysis(pk);
            if (!la.Valid) continue;
            letti++;
            if (gruppoDi.TryGetValue(la.EncounterMatch, out var gr)) coperti.Add(gr);
        }
    }
    var mancanti = modelli.Where(x => !coperti.Contains(x.gruppo)).GroupBy(x => x.gruppo).ToList();
    Console.WriteLine($"esemplari conformi letti {letti}, gruppi coperti {coperti.Count}, gruppi da produrre {mancanti.Count}");
    var dir = Directory.CreateDirectory(cartella).FullName;
    var lista = new JsonArray();
    int prodotti = 0, n = 0;
    GameVersion[] concrete = [GameVersion.RD, GameVersion.GN, GameVersion.BU, GameVersion.YW, GameVersion.GD, GameVersion.SI, GameVersion.C,
        GameVersion.R, GameVersion.S, GameVersion.E, GameVersion.FR, GameVersion.LG, GameVersion.CXD, GameVersion.D, GameVersion.P, GameVersion.Pt,
        GameVersion.HG, GameVersion.SS, GameVersion.B, GameVersion.W, GameVersion.B2, GameVersion.W2, GameVersion.X, GameVersion.Y,
        GameVersion.OR, GameVersion.AS, GameVersion.SN, GameVersion.MN, GameVersion.US, GameVersion.UM];
    foreach (var g in mancanti)
    {
        n++;
        var primo = g.First();
        var voce = new JsonObject { ["gruppo"] = g.Key, ["classe"] = primo.classe, ["specie"] = testi.specieslist[primo.enc.Species],
            ["incontro"] = ((IEncounterable)primo.enc).LongName, ["gemelli"] = g.Count() };
        lista.Add(voce);
        PKM? buono = null; string rapporto = ""; IEncounterTemplate? scelto = null;
        foreach (var (enc, _, _) in g)
        {
            var versioni = concrete.Where(v => enc.Version == v || enc.Version.Contains(v)).ToList();
            if (versioni.Count == 0) versioni.Add(enc.Version);
            foreach (var v in versioni)
            {
                if (buono is not null) break;
                var lingue = v is GameVersion.GN ? new[] { LanguageID.Japanese } : new[] { LanguageID.Italian, LanguageID.English, LanguageID.Japanese };
                foreach (var lg in lingue)
                {
                    if (buono is not null) break;
                    var tr = new SimpleTrainerInfo(v == GameVersion.CXD ? GameVersion.E : v) { OT = lg is LanguageID.Japanese ? "アレッシオ" : nomeP, TID16 = tidP, SID16 = sidP, Language = (int)lg };
                    try
                    {
                        RecentTrainerCache.SetRecentTrainer(tr);
                        var pk = ((IEncounterable)enc).ConvertToPKM(tr, EncounterCriteria.Unrestricted);
                        if (pk is CK3 ck3) pk = ck3.ConvertToPK3(); else if (pk is XK3 xk3) pk = xk3.ConvertToPK3();
                        if (pk.IsEgg && pk.Format >= 4) pk.ForceHatchPKM(tr);
                        var la = new LegalityAnalysis(pk);
                        if (!la.Valid && la.Report().Contains("Met Date") && pk.Format >= 4)
                        {
                            pk.MetDate = DateOnly.FromDateTime(DateTime.Today);
                            if (pk.WasEgg && pk.EggMetDate is null) pk.EggMetDate = pk.MetDate;
                            la = new LegalityAnalysis(pk);
                        }
                        if (la.Valid) { buono = pk; scelto = enc; } else rapporto = la.Report();
                    }
                    catch (Exception ex) { rapporto = ex.Message; }
                }
            }
            if (buono is not null) break;
        }
        if (buono is null) { voce["esito"] = "non prodotto"; voce["rapporto"] = rapporto; continue; }
        var dati = new byte[buono.SIZE_STORED]; buono.WriteDecryptedDataStored(dati);
        var nome = $"{n:0000}-{primo.classe}-G{primo.enc.Generation}-{testi.specieslist[buono.Species]}.{buono.Extension}";
        foreach (var ch in Path.GetInvalidFileNameChars()) nome = nome.Replace(ch, '_');
        File.WriteAllBytes(Path.Combine(dir, nome), dati);
        voce["esito"] = "prodotto"; voce["file"] = nome; voce["pid"] = buono.PID.ToString("X8");
        voce["versione"] = ((GameVersion)buono.Version).ToString(); voce["generazione"] = (int)primo.enc.Generation;
        voce["sha256"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant();
        voce["storia"] = $"{(primo.classe == "statico" ? "Incontro fisso" : primo.classe == "dono" ? "Dono in gioco" : "Uovo dono")} di {testi.specieslist[buono.Species]} in {((GameVersion)buono.Version)} ({((IEncounterable)scelto!).LongName}), livello {primo.enc.LevelMin}, " +
            "con l'allenatore del progetto; prodotto dalla libreria del verificatore come caselle statiche, doni e uova (ADR-106, ADR-119).";
        prodotti++;
        if (n % 100 == 0) Console.WriteLine($"{n}/{mancanti.Count} prodotti {prodotti}");
    }
    File.WriteAllText(uscita, new JsonObject { ["modelli"] = modelli.Count, ["gruppi_coperti"] = coperti.Count, ["gruppi_da_produrre"] = mancanti.Count,
        ["prodotti"] = prodotti, ["esemplari_letti"] = letti, ["esiti"] = lista }
        .ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }));
    Console.WriteLine($"prodotti {prodotti} su {mancanti.Count}");
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
