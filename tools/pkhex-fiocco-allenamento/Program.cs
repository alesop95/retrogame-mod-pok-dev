// Il Training Ribbon di sesta generazione su un esemplare di una copia per HOME, conforme per il verificatore.
//
// Perche' esiste. Dei 63 fiocchi che dopo la chiusura di Bank non si ottengono piu' giocando, l'unico che nessun
// esemplare in HOME porta e' il Training Ribbon (misura del 2026-11-24 sul giudizio dopo il giro 15). In Rubino Omega
// e Zaffiro Alpha lo da' Bluruvia al primo della squadra quando ha finito il Super Allenamento segreto. Il 2026-11-25
// il proprietario ha scelto di farlo produrre invece di giocarlo, e di metterlo nel giro di Zaffiro.
//
// Che cosa fa. Apre la copia, cerca nei box l'esemplare con la specie e il PID richiesti, e gli scrive lo stato che
// il gioco lascia dopo il Super Allenamento completo: tutte le medaglie dei regimi normali e segreti, i due indicatori
// del Super Allenamento segreto, punti base a 510 come chiede lo sblocco dei regimi segreti, e il fiocco. Lo accetta
// soltanto se LegalityAnalysis lo giudica conforme, e rilegge lo slot dopo la scrittura. La regola del verificatore e'
// RibbonRules.IsRibbonValidSuperTraining: fiocco valido se l'esemplare e' passato dalla sesta generazione e le
// medaglie sono tutte accese.
//
// Uso:  pkhex-fiocco-allenamento COPIA_DI_PARTENZA COPIA_DI_USCITA SPECIE PID_ESADECIMALE HP ATK DEF SPE SPA SPD
using PKHeX.Core;

if (args.Length != 10) { Console.Error.WriteLine("uso: PARTENZA USCITA SPECIE PID HP ATK DEF SPE SPA SPD"); return 2; }
var (partenza, uscita) = (args[0], args[1]);
if (Path.GetFullPath(partenza) == Path.GetFullPath(uscita)) { Console.Error.WriteLine("la copia di uscita deve essere un file diverso"); return 2; }
var specie = ushort.Parse(args[2]);
var pid = Convert.ToUInt32(args[3], 16);
var ev = args.Skip(4).Select(int.Parse).ToArray(); // HP ATK DEF SPE SPA SPD, l'ordine di PKHeX
if (ev.Sum() != 510 || ev.Any(v => v is < 0 or > 252)) { Console.Error.WriteLine("i punti base devono sommare 510, ciascuno fra 0 e 252"); return 2; }
if (!SaveUtil.TryGetSaveFile(partenza, out var sav)) { Console.Error.WriteLine("salvataggio non letto"); return 1; }
var posto = Enumerable.Range(0, sav.SlotCount).FirstOrDefault(i => { var p = sav.GetBoxSlotAtIndex(i); return p.Species == specie && p.PID == pid; }, -1);
if (posto < 0) { Console.Error.WriteLine("esemplare non trovato"); return 1; }
if (sav.GetBoxSlotAtIndex(posto) is not PK6 pk) { Console.Error.WriteLine("l'esemplare non e' in formato PK6"); return 1; }
var prima = new LegalityAnalysis(pk);
if (!prima.Valid) { Console.Error.WriteLine("l'esemplare era gia' contestato:\n" + prima.Report()); return 1; }
pk.SetEVs(ev);
pk.SuperTrainBitFlags = RibbonRules.SetSuperTrainSupremelyTrained(pk.SuperTrainBitFlags);
pk.SecretSuperTrainingUnlocked = true;
pk.SuperTrainSupremelyTrained = true;
pk.RibbonTraining = true;
pk.RefreshChecksum();
var la = new LegalityAnalysis(pk);
if (!la.Valid) { Console.Error.WriteLine("contestato dopo il fiocco:\n" + la.Report()); return 1; }
sav.SetBoxSlotAtIndex(pk, posto);
var letto = sav.GetBoxSlotAtIndex(posto);
if (!letto.Data.SequenceEqual(pk.Data) || !new LegalityAnalysis(letto).Valid) { Console.Error.WriteLine("rilettura diversa o contestata"); return 1; }
File.WriteAllBytes(uscita, sav.Write().ToArray());
Console.WriteLine($"box {posto / 30 + 1} posto {posto % 30 + 1}: {GameInfo.GetStrings("it").specieslist[specie]} PID {pid:X8}, fiocco e medaglie scritti, conforme; scritto {uscita}");
return 0;
