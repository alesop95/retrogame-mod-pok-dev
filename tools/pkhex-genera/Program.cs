// Generatore del progetto sulla libreria del verificatore, compilata dal clone in _notes/fonti/cloni/pkhex.
//
// Perche' esiste. ADR-080 chiede circa trecentocinquanta esemplari di terza generazione da sette giochi,
// Ombra di XD compresi, e riscrivere in Python la generazione di ciascuna classe d'incontro vorrebbe dire
// riscrivere il verificatore. La libreria di PKHeX sa gia' costruire un esemplare legale da ogni voce delle
// sue tabelle, e lo stesso codice lo giudica: qui la si usa invece di imitarla.
//
// Che cosa fa. Legge le richieste scritte da tools/manifesto-complemento-rubino.py. Per ciascuna cerca, fra
// le voci che la libreria dichiara per quella specie e quei giochi, una della classe e del luogo richiesti;
// costruisce l'esemplare con l'allenatore del gioco, mai cromatico; lo fa evolvere se la richiesta lo
// chiede, gli insegna le mosse richieste, gli assegna i fiocchi e il livello; e lo accetta soltanto se
// LegalityAnalysis lo giudica legale. Scrive il file .pk3 da ottanta byte, cioe' la forma dei lotti gia'
// esistenti, e un rapporto con l'esito di ogni richiesta.
//
// Riproducibilita'. La libreria estrae i numeri casuali da Random.Shared, che non si puo' fissare, quindi
// due lanci danno esemplari diversi e ugualmente legali. Come per gli altri lotti, il risultato sono i file,
// e il rapporto porta l'impronta SHA-256 di ciascuno.
//
// Uso:  dotnet run -c Release -- RICHIESTE.json CARTELLA_DI_USCITA
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

var richieste = JsonNode.Parse(File.ReadAllText(args[0]))!;
var uscita = Directory.CreateDirectory(args[1]).FullName;
var giochi = new Dictionary<string, GameVersion>
{
    ["R"] = GameVersion.R, ["S"] = GameVersion.S, ["E"] = GameVersion.E,
    ["FR"] = GameVersion.FR, ["LG"] = GameVersion.LG, ["COLO"] = GameVersion.CXD, ["XD"] = GameVersion.CXD,
};
var allenatori = new Dictionary<string, SimpleTrainerInfo>();
foreach (var (sigla, dati) in richieste["allenatori"]!.AsObject())
{
    // Colosseum e XD si cercano come un solo gioco; l'allenatore si costruisce su un portatile, perche'
    // la libreria non ha un contesto per la sigla congiunta.
    var base_ = sigla is "COLO" or "XD" ? GameVersion.E : giochi[sigla];
    // In Rubino, Zaffiro, Colosseum e XD l'identificativo esce dal generatore del gioco a inizio partita, e il
    // verificatore lo ricostruisce con MethodH e MethodCXD: una coppia qualunque non e' ottenibile. Si parte
    // dalla coppia del manifesto e si prende la prima che quei metodi accettano, in ordine, cosi' che il
    // risultato resti deterministico.
    var (tid, sid) = ((ushort)(int)dati!["TID16"]!, (ushort)(int)dati["SID16"]!);
    Func<ushort, ushort, bool>? valida = sigla switch
    {
        "R" or "S" => (t, s2) => MethodH.TryGetSeedTrainerID(t, s2, out _),
        "COLO" or "XD" => (t, s2) => MethodCXD.TryGetSeedTrainerID(t, s2, out _),
        _ => null,
    };
    if (valida is not null)
    {
        var trovata = false;
        for (int giro = 0; giro < 16 && !trovata; giro++)
        {
            var t = (ushort)(tid + giro);
            for (int passo = 0; passo < 65536; passo++)
            {
                var ss = (ushort)(sid + passo);
                if (valida(t, ss)) { (tid, sid) = (t, ss); trovata = true; break; }
            }
        }
        if (!trovata) throw new InvalidOperationException("nessun identificativo valido per " + sigla);
    }
    allenatori[sigla] = new SimpleTrainerInfo(base_)
    {
        OT = (string)dati["OT"]!, TID16 = tid, SID16 = sid, Gender = 0, Language = (int)LanguageID.Italian,
    };
}
var criteri = EncounterCriteria.Unrestricted with { Shiny = Shiny.Never };
var esiti = new JsonArray();
int riuscite = 0;
var personalita = new HashSet<uint>();
// le personalita' gia' presenti nel deposito di Smeraldo, se il manifesto le porta, non si ripetono nemmeno fra le due cartucce
if (richieste["personalita_escluse"] is { } escluse)
    foreach (var x in escluse.AsArray()) personalita.Add(Convert.ToUInt32((string)x!, 16));

foreach (var r in richieste["richieste"]!.AsArray())
{
    var id = (string)r!["id"]!;
    var specie = (ushort)(int)r["specie"]!;
    var bersaglio = r["evolvi_a"] is { } e ? (ushort)(int)e : specie;
    var forma = r["forma"] is { } f ? (byte)(int)f : (byte)0;
    var classi = r["classi"]!.AsArray().Select(x => (string)x!).ToHashSet();
    ushort? luogo = r["luogo"] is { } l ? (ushort)(int)l : null;
    var mosse = r["mosse"] is { } m ? m.AsArray().Select(x => (ushort)(int)x!).ToArray() : [];
    var fiocchi = r["fiocchi"] is { } fi ? fi.AsArray().Select(x => (string)x!).ToArray() : [];
    byte? livello = r["livello"] is { } lv ? (byte)(int)lv : null;
    var eventoOT = (string?)r["allenatore_evento"];

    PKM? accettato = null;
    string voce = "", difetto = "nessuna voce della libreria corrisponde";
    foreach (var sigla in r["giochi"]!.AsArray().Select(x => (string)x!))
    {
        var tr = allenatori[sigla];
        var modello = EntityBlank.GetBlank(3);
        modello.Species = bersaglio;
        modello.Form = forma;
        modello.Language = (int)LanguageID.Italian;
        foreach (var enc in EncounterMovesetGenerator.GenerateEncounters(modello, tr, mosse, giochi[sigla]))
        {
            if (classi.Count > 0 && !classi.Contains(enc.GetType().Name))
                continue;
            if (luogo is { } lu && !(enc is ILocation il && il.Location == lu))
                continue;
            if (eventoOT is not null && !(enc is EncounterGift3 g3 && g3.OriginalTrainerName == eventoOT))
                continue;
            // La libreria restituisce le voci selvatiche di tutte le forme, non solo di quella chiesta: senza
            // questo filtro i 28 Unown del primo lotto erano nati tutti nella Sala A-loe, cioe' tutti A. La
            // forma richiesta e il tipo di casella, come Spaccaroccia o i riquadri di Feebas, si pretendono
            // qui sulla voce stessa.
            if (r["forma"] is not null && !(enc is EncounterSlot3 sf && sf.Form == forma))
                continue;
            if (r["tipo_casella"] is { } tc && !(enc is EncounterSlot3 st && (int)st.Type == (int)tc))
                continue;
            // per un'evoluzione si provano livelli crescenti, perche' ogni specie ha la propria soglia
            byte[] livelli = bersaglio != enc.Species && livello is null ? [30, 40, 50, 60, 100] : [0];
            for (int tentativo = 0; tentativo < 6 * livelli.Length && accettato is null; tentativo++)
            {
                // dal secondo tentativo si chiede una natura a caso: alcune voci, come i vaganti di Kanto,
                // la libreria le costruisce altrimenti sempre dallo stesso seme
                var c = tentativo < livelli.Length ? criteri : criteri with { Nature = (Nature)Random.Shared.Next(25) };
                var pk = enc.ConvertToPKM(tr, c);
                // Colosseum e XD restituiscono l'esemplare nel formato dei giochi da tavolo, CK3 e XK3; sul
                // portatile arriva come PK3, e la conversione e' quella che il gioco stesso fa nello scambio
                if (pk is CK3 ck) pk = ck.ConvertToPK3();
                else if (pk is XK3 xk) pk = xk.ConvertToPK3();
                var scelto = livelli[tentativo % livelli.Length];
                Rifinisci(pk, bersaglio, mosse, fiocchi, scelto == 0 ? livello : scelto);
                var la = new LegalityAnalysis(pk);
                // una personalita' gia' usata darebbe due esemplari che sembrano cloni, come i tre vaganti
                // che la libreria costruiva dallo stesso seme
                if (la.Valid && !pk.IsShiny && pk is PK3 && personalita.Add(pk.PID))
                {
                    accettato = pk;
                    voce = $"{enc.GetType().Name} {enc.LongName} ({sigla})";
                }
                else
                {
                    difetto = string.Join(" | ", la.Report().Replace("\r", "").Split('\n').Where(x => x.Contains("Invalid")));
                }
            }
            if (accettato is not null) break;
        }
        if (accettato is not null) break;
    }

    var esito = new JsonObject { ["id"] = id, ["motivo"] = (string)r["motivo"]! };
    if (accettato is not null)
    {
        // la forma memorizzata e in chiaro, ottanta byte, come i .pk3 dei lotti gia' esistenti
        var dati = new byte[accettato.SIZE_STORED];
        accettato.WriteDecryptedDataStored(dati);
        var nome = $"{id}.pk3";
        File.WriteAllBytes(Path.Combine(uscita, nome), dati);
        esito["file"] = nome;
        esito["voce"] = voce;
        esito["specie"] = accettato.Species;
        esito["livello"] = accettato.CurrentLevel;
        esito["personalita"] = accettato.PID.ToString("X8");
        esito["allenatore"] = $"{accettato.OriginalTrainerName} {accettato.TID16}";
        esito["sha256"] = Convert.ToHexString(SHA256.HashData(dati)).ToLowerInvariant();
        riuscite++;
    }
    else
    {
        esito["difetto"] = difetto;
    }
    esiti.Add(esito);
    Console.WriteLine($"{(accettato is null ? "NO " : "ok ")} {id}  {voce}{(accettato is null ? "  " + difetto : "")}");
}

var usati = new JsonObject();
foreach (var (sigla, tr) in allenatori)
    usati[sigla] = new JsonObject { ["OT"] = tr.OT, ["TID16"] = tr.TID16, ["SID16"] = tr.SID16 };
File.WriteAllText(Path.Combine(uscita, "rapporto.json"),
    new JsonObject { ["riuscite"] = riuscite, ["richieste"] = esiti.Count, ["allenatori"] = usati, ["esiti"] = esiti }.ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"riuscite {riuscite} su {esiti.Count}");

// Dopo la costruzione: evoluzione, mosse, fiocchi e livello, nell'ordine in cui il gioco li produrrebbe.
static void Rifinisci(PKM pk, ushort bersaglio, ushort[] mosse, string[] fiocchi, byte? livello)
{
    if (pk.Species != bersaglio)
    {
        // l'evoluzione cambia la specie e il nome, se il nome e' quello della specie di partenza
        var nomeVecchio = SpeciesName.GetSpeciesNameGeneration(pk.Species, pk.Language, 3);
        pk.Species = bersaglio;
        if (pk.Nickname == nomeVecchio)
            pk.Nickname = SpeciesName.GetSpeciesNameGeneration(bersaglio, pk.Language, 3);
    }
    if (livello is { } lv)
        pk.CurrentLevel = lv;
    if (mosse.Length > 0)
    {
        var attuali = pk.Moves.Where(x => x != 0).ToList();
        foreach (var mv in mosse.Where(mv => !attuali.Contains(mv)))
        {
            if (attuali.Count == 4) attuali.RemoveAt(3);
            attuali.Insert(0, mv);
        }
        pk.SetMoves(attuali.ToArray());
        pk.HealPP();
    }
    foreach (var f in fiocchi)
    {
        var parti = f.Split('=');
        var prop = pk.GetType().GetProperty(parti[0]) ?? throw new InvalidOperationException("fiocco sconosciuto " + parti[0]);
        prop.SetValue(pk, parti.Length == 2 ? (object)byte.Parse(parti[1]) : true);
    }
    pk.ResetPartyStats();
    pk.RefreshChecksum();
}
