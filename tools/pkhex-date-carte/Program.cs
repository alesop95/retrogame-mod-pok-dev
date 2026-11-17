// Le date scritte nelle carte della base dei doni, sulla libreria del verificatore compilata dal clone in
// _notes/fonti/cloni/pkhex.
//
// Perche' esiste. Il 2026-11-16 il proprietario ha deciso che i doni da carta abbiano una data di incontro dentro la
// finestra dell'evento (`pending.md`, voce «AL 2026-11-16»). Le finestre vengono dalle liste di Bulbapedia
// (`tools/finestre-eventi.py`), che non coprono ogni carta. La base dei doni della libreria contiene invece, per molte
// carte, le copie estratte dai salvataggi dei giocatori, ciascuna con la data in cui quel giocatore l'ha ricevuta: un
// insieme di date di ricezione reali, da cui si ricava un intervallo osservato quando la finestra manca.
//
// Che cosa fa. Per ogni carta di quinta (PGF), sesta (WC6) e settima generazione (WC7) che porta un esemplare scrive
// generazione, numero della carta, specie, titolo, allenatore, identificativo e data. Le carte complete del server
// (`WC5Full`, `WC6Full`, `WC7Full`) non hanno una data propria e la libreria da' loro il giorno in cui gira: per queste
// la data si scrive vuota, con `completa` vero.
//
// Uso:  dotnet run -c Release -- USCITA.json
using System.Text.Json;
using System.Text.Json.Nodes;
using PKHeX.Core;

if (args.Length != 1)
{
    Console.Error.WriteLine("uso: dotnet run -c Release -- USCITA.json");
    return 2;
}
var oggi = EncounterDate.GetDate3DS();
var carte = new JsonArray();
int conData = 0, complete = 0;
void Aggiungi(int gen, MysteryGift c, DateOnly? data)
{
    if (!c.IsEntity || c.Species == 0)
        return;
    bool completa = data is null || data == oggi;
    if (completa) complete++; else conData++;
    carte.Add(new JsonObject
    {
        ["generazione"] = gen,
        ["carta"] = c.CardID,
        ["specie"] = c.Species,
        ["titolo"] = c.CardTitle,
        ["allenatore"] = c.OriginalTrainerName,
        ["id"] = c.TID16,
        ["data"] = completa ? null : data!.Value.ToString("yyyy-MM-dd"),
        ["completa"] = completa,
    });
}
foreach (var c in EncounterEvent.MGDB_G5) Aggiungi(5, c, c.Date);
foreach (var c in EncounterEvent.MGDB_G6) Aggiungi(6, c, c.Date);
foreach (var c in EncounterEvent.MGDB_G7) Aggiungi(7, c, c.Date);
File.WriteAllText(args[0], carte.ToJsonString(new JsonSerializerOptions { WriteIndented = true, Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }) + "\n");
Console.WriteLine($"{carte.Count} carte, {conData} con una data di ricezione, {complete} complete senza data; scritto {args[0]}");
return 0;
