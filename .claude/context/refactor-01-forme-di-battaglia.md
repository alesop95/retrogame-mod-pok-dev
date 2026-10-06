# Refactor 01. Un elenco di specie letto come un elenco di forme

> Scheda di dettaglio della voce 1 di `studio-didattico-master.md`. Entra nel codice di `tools/checklist-pokedex.py` prima e dopo il 2026-09-30, e nella regola della libreria che la correzione interroga.

## Il difetto, nel codice

Fino al 2026-09-30 la checklist costruiva l'insieme delle forme di battaglia così, alla riga 651 del commit `30bdbfb`.

```python
battaglia = (disp.elenco_specie(forme_src, "BattleMegas", per_nome)
             | disp.elenco_specie(forme_src, "BattleForms", per_nome))
```

La funzione `elenco_specie` di `tools/disponibilita-titoli.py` apre `Legality/Tables/FormInfo.cs`, trova la dichiarazione `ReadOnlySpan<ushort> BattleForms` e ne raccoglie i nomi di specie. L'insieme che ne esce è quindi un insieme di numeri di specie, e alla riga 691 veniva usato come se fosse un insieme di forme.

```python
if s in battaglia:
    natura = "forma di sola battaglia: non può stare in una scatola"
```

Il ciclo percorre le coppie specie e forma con forma diversa da zero, quindi ogni forma alternativa di una specie che avesse almeno una forma di battaglia riceveva quella natura.

## Perché la libreria dice un'altra cosa

Nella libreria i due elenchi non decidono: aprono la porta a una seconda domanda. La funzione pubblica è questa.

```csharp
public static bool IsBattleOnlyForm(ushort species, byte form, byte format)
{
    if (BattleMegas.Contains(species) && IsBattleMegaForm(species, form))
        return true;
    if (BattleForms.Contains(species) && IsBattleForm(species, form))
        return true;
    return false;
}
```

La seconda domanda è un'espressione di scelta per specie, di cui basta un estratto.

```csharp
private static bool IsBattleForm(ushort species, byte form) => species switch
{
    (ushort)Darmanitan => (form & 1) == 1, // Zen
    (ushort)Greninja => form == 2, // Ash
    (ushort)Zygarde => form == 4, // Zygarde Complete
    (ushort)Minior => form < 7, // Minior Shields-Down
    (ushort)Ogerpon => form >= 4, // Embody Aspect
    _ => form != 0,
};
```

Il ramo predefinito, `form != 0`, è esattamente il comportamento che la checklist applicava a tutte le specie. Le righe sopra di esso sono le eccezioni, ed erano le eccezioni che la lettura per specie perdeva. Per Greninja la forma 1 è quella con Morfosi, che si deposita, e la 2 è Ash-Greninja, che esiste solo in battaglia: la checklist le trattava allo stesso modo.

Il difetto è istruttivo perché non ha un sintomo. Ogni riga sbagliata portava una motivazione vera per molte altre righe della stessa specie, e una lista che dice «non può stare in una scatola» non invita a ricontrollare. È emerso solo perché una fonte esterna nominava come da ottenere un esemplare che la lista escludeva.

## La correzione

Le espressioni di scelta sono codice C#, e leggerle con espressioni regolari da Python sarebbe la stessa imitazione in forma più elaborata, destinata a rompersi alla prossima eccezione aggiunta a monte. La risposta la dà la libreria: `tools/pkhex-forme-battaglia/Program.cs` percorre le specie da 1 a 1025 e gli indici di forma da 1 a 31, e raccoglie le coppie per cui `FormInfo.IsBattleOnlyForm(s, f, 9)` è vera.

```csharp
for (ushort s = 1; s <= 1025; s++)
{
    int quante = 32;
    for (byte f = 1; f < quante; f++)
    {
        if (FormInfo.IsBattleOnlyForm(s, f, 9))
            coppie.Add([s, f]);
    }
}
```

Interrogare tutti gli indici invece delle sole forme esistenti è una scelta, e ha una storia. Il primo tentativo enumerava le forme con `FormConverter.GetFormList` in nona generazione e perdeva le megaevoluzioni, che in quel contesto non compaiono; il secondo prendeva il massimo fra i contesti e perdeva comunque le forme da 3 a 9 di Terapagos, che una tabella di dati letta dalla checklist dichiara e l'elenco dei nomi no. La regola è pura, cioè non dipende dall'esistenza della forma, quindi interrogarla su indici inesistenti non costa nulla e non sbaglia: una coppia che non esiste non entra mai nella checklist, che ricava le forme dalle tabelle dei titoli.

La checklist legge il risultato per coppia.

```python
with open(a.forme_battaglia, encoding="utf-8") as fb:
    battaglia = {(c[0], c[1]) for c in json.load(fb)["coppie"]}

if (s, f) in battaglia:
    natura = "forma di sola battaglia: non può stare in una scatola"
```

## Come si è verificato che la correzione misuri il difetto

Prima di cambiare la checklist, un programma di sessione aveva interrogato la stessa funzione sulle 170 forme che la vecchia checklist marcava di battaglia: 141 lo erano, 29 no. La correzione è stata accettata solo quando due confronti sono tornati. Il primo, fra l'uscita dello strumento e quel controllo, doveva dare nessuna coppia mancante e nessuna depositabile marcata di battaglia. Il secondo, fra la checklist prima e dopo la rigenerazione, doveva cambiare le sole 29 righe attese: è tornato così, con in più Mimikyu forma 2, che ora risulta correttamente totemica, e Spinda, corretta nello stesso giro per una ragione diversa.

## Come estendere il pattern

Il principio è che una regola che vive nel codice di un'altra base si fa valutare a quella base, e il suo risultato diventa un dato riprodotto con il commit da cui viene. Il progetto lo applica già al giudizio di conformità con `tools/pkhex-giudica` e alla generazione con `tools/pkhex-genera` e `tools/pkhex-dono`. La prossima volta che uno strumento Python legge un elenco dal sorgente di PKHeX, la domanda da farsi è se quell'elenco decida da solo o apra la porta a un'espressione successiva; nel secondo caso l'elenco non basta, e si passa per la libreria.
