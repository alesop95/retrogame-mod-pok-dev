# Studio 10: la libreria del verificatore come generatore

## Perché questo studio esiste

Per un mese il progetto ha generato esemplari scrivendo in Python, una classe d'incontro alla volta, la logica che il gioco usa per crearli: il primo metodo e le sue varianti per i selvatici, la correlazione di Colosseum per Suicune e Raikou, le formule degli eventi verificate su un corpus di duecentonove esemplari, la catena dei selvatici di Smeraldo per il Lotad e il Seedot più grandi possibili. Ogni generatore nuovo è stato poi giudicato da PKHeX, e ogni giro di giudizio ha rivelato qualcosa che il generatore ignorava. Il 2026-09-23 la collezione completa di terza generazione di ADR-080 ha chiesto circa trecentocinquanta esemplari da sette giochi, compresi i Pokémon Ombra di XD con i loro vincoli di squadra, e riscrivere quei metodi avrebbe voluto dire riscrivere il verificatore.

L'osservazione che ha cambiato il metodo è semplice, ed è del proprietario: la libreria del verificatore sa già costruire un esemplare legale da ogni voce delle proprie tabelle, e lo stesso codice poi lo giudica. Usarla come generatore invece di imitarla elimina alla radice la classe di difetti che i giri di giudizio hanno scoperto uno per uno, cioè le differenze fra ciò che il progetto credeva facesse il gioco e ciò che il verificatore sa che il gioco fa.

## Come è fatto

Gli strumenti sono due, uno per ciascun lato del confine fra deterministico e linguistico che `token-economy.md` prescrive. `tools/manifesto-complemento-rubino.py` decide che cosa generare. Legge il deposito di Smeraldo dai byte della cartuccia e dal dump di PKHeX, usa le funzioni di `tools/verifica-terza-generazione.py` perché le due misure non possano divergere, e scrive una richiesta per ogni cosa che manca, con specie, giochi ammessi, classe d'incontro, luogo, mosse, fiocchi e livello. `tools/pkhex-genera` esegue le richieste. È un programma .NET che usa `PKHeX.Core` compilato dal clone in `_notes/fonti/pkhex`, cioè esattamente il codice del verificatore che si usa per il giudizio.

Il cuore del generatore è una chiamata della libreria, `EncounterMovesetGenerator.GenerateEncounters`, che dato un modello di esemplare, un allenatore, le mosse volute e un gioco elenca le voci delle tabelle da cui quell'esemplare può nascere. Per ciascuna voce che rispetta classe e luogo il generatore chiama `ConvertToPKM`, rifinisce l'esemplare (evoluzione, mosse, fiocchi, livello) e lo accetta soltanto se `LegalityAnalysis` lo giudica legale.

```csharp
foreach (var enc in EncounterMovesetGenerator.GenerateEncounters(modello, tr, mosse, gioco))
{
    var pk = enc.ConvertToPKM(tr, criteri);
    if (pk is CK3 ck) pk = ck.ConvertToPK3();
    else if (pk is XK3 xk) pk = xk.ConvertToPK3();
    Rifinisci(pk, bersaglio, mosse, fiocchi, livello);
    if (new LegalityAnalysis(pk).Valid && !pk.IsShiny && personalita.Add(pk.PID))
        return pk;
}
```

## Gli inciampi, e che cosa ciascuno insegna

Il primo inciampo è stato il clone. Era parziale per scelta, con solo le cartelle che servivano a leggere le tabelle, 1349 file C# su 1815, e la prima compilazione ha dato 1030 errori, tutti tipi non trovati. Si è completato con `git sparse-checkout disable` sullo stesso commit `e15d246`, perché cambiare commit avrebbe cambiato il verificatore. Una lettura parziale di un sorgente va bene per consultarlo e non per compilarlo, e il prezzo di scoprirlo tardi è stato solo di tre minuti perché l'errore era evidente.

Il secondo inciampo è stato l'identificativo dell'allenatore. Al primo lancio 56 esemplari su 355 sono stati respinti con «Trainer ID is not obtainable from any RNG seed», tutti di Rubino, Zaffiro, Colosseum e XD. In quei giochi l'identificativo esce dal generatore pseudocasuale all'inizio della partita, e `TrainerIDVerifier.cs` lo ricostruisce con `MethodH` e `MethodCXD`: una coppia scelta a piacere non è ottenibile. Il generatore parte ora dalla coppia del manifesto e cerca, in ordine, la prima che quei metodi accettano. Il vincolo non esiste in Smeraldo, Rosso Fuoco e Verde Foglia, dove la coppia del manifesto passa così com'è.

Il terzo inciampo era silenzioso ed è il più istruttivo. Per gli incontri di Colosseum e XD la libreria restituisce l'esemplare nel formato dei giochi da tavolo, CK3 e XK3, e il generatore ne scriveva i byte come se fossero il formato dei portatili. PKHeX li giudicava legali, perché giudicava l'oggetto giusto. La nostra libreria Python, invece, li leggeva come dati senza senso: 143 file non tornavano identici dopo lettura e riscrittura, e avevano la lingua a zero e personalità minuscole che risultavano ripetute. La correzione è la conversione in PK3 con `ConvertToPK3`, la stessa che il gioco fa quando manda l'esemplare al portatile, prima del giudizio e prima di scrivere. La lezione vale oltre il caso: un giudizio positivo dice che l'oggetto giudicato è legale, non che l'oggetto scritto su disco sia quello. Per questo, dopo il generatore, un controllo indipendente rilegge ogni file con la libreria del progetto.

Il quarto inciampo riguarda l'unicità. La libreria costruiva tre leggendari vaganti, Latias di Zaffiro ed Entei e Suicune di Rosso Fuoco, dallo stesso seme, quindi con la stessa personalità. Anche l'Eevee di XD e gli starter di Colosseum nascono dal seme dell'identificativo, e con un solo identificativo per i due giochi le loro personalità si sovrapponevano. Ora il generatore rifiuta una personalità già usata, nel lotto o nel deposito di Smeraldo, e dal secondo tentativo chiede una natura a caso, che obbliga la libreria a cambiare seme. Colosseum e XD hanno ciascuno il proprio identificativo, come due partite distinte.

L'ultimo inciampo è stato il portatore dei fiocchi. Il primo candidato era un Milotic, per il legame con i concorsi. Il verificatore però non ricollega l'evoluzione da un Feebas generato a un incontro d'origine, mentre accetta tutti e 26 i fiocchi su un Feebas o su un Absol che non si evolvono. Il portatore è diventato l'Absol del Percorso 120 di Smeraldo. La prova è stata fatta con richieste separate, cioè una variante senza fiocchi, una senza evoluzione e una su un'altra specie, così che la causa fosse isolata invece che intuita.

## Che cosa ne è uscito

Il lotto è in `_notes/lotto-complemento-rubino/esemplari/`, e il documento generato `COMPLEMENTO-RUBINO.md` ne è la forma leggibile.
- **Legalità:** 355 esemplari su 355 richieste, tutti legali per la libreria del verificatore.
- **Controllo indipendente:** tutti simmetrici per la libreria del progetto, nessuno cromatico, nessuna personalità ripetuta né nel lotto né rispetto a Smeraldo.
- **Copertura:** con Smeraldo coprono tutte le 386 specie e le 28 forme di Unown.
- **Fiocchi:** portano tutti e 27 i fiocchi di terza generazione che il verificatore accetta. Il Nazionale è su tutti i 129 Pokémon Ombra purificati; i 20 di gara al rango massimo, Campione, Winning, Victory, Artist, Impegno e Terra sono sull'Absol.
- **Mosse perdute:** otto su nove. Incubo non ha portatore perché in terza generazione nessuna specie la impara.
- **Eventi:** entra il Jirachi di Pokémon Channel, che il progetto finora non sapeva produrre perché usa il generatore dei giochi da tavolo.

La riproducibilità ha un limite dichiarato. La libreria estrae i numeri casuali da `Random.Shared`, che non si può fissare, quindi due lanci danno esemplari diversi e ugualmente legali. Come per gli altri lotti, il risultato sono i file, e il rapporto porta l'impronta SHA-256 di ciascuno.

## Perché lo stesso metodo serve all'obiettivo primario

La libreria copre tutte le generazioni, non soltanto la terza, e il generatore non sa nulla della terza generazione: la sua conoscenza sta tutta nelle richieste e nella libreria. Lo stesso programma può quindi generare esemplari legali per i giochi di quarta, quinta, sesta e settima generazione, cioè per i salvataggi da cui la catena porta al deposito. È la ragione di ADR-081.

Due confini vanno detti con la stessa chiarezza. Il primo è di perimetro. L'installazione e l'uso di Pokémon Bank e Pokémon Transporter su questa console restano fuori dall'assistenza, per la ragione registrata in `_notes/perimetro-bank-transporter.md`: il progetto prepara gli esemplari e i salvataggi, e quel tratto resta del proprietario. Il secondo è di sostanza. Un esemplare generato è legale per il verificatore, e il progetto ha sempre distinto il legale dal legittimo. Vale in particolare per i fiocchi di gara e di vittoria sull'Absol, che raccontano concorsi e serie mai giocati, come ADR-080 ha registrato dopo averlo esposto al proprietario.

## Che cosa resta aperto

Resta aperta la scrittura sul Rubino, cioè la fase F5 di ADR-080. Il Rubino di prova contiene oggi 205 esemplari scritti il 2026-09-16, e il primo passo è una lettura nuova della cartuccia con il backup in doppia copia. Poi lo strumento di caricamento sostituisce le scatole con il complemento e lascia intatta la squadra di inizio partita. Prima della scrittura serve anche il giudizio della versione grafica di PKHeX sul file lavorato, cioè un dump dei box come per Smeraldo, perché è il controllo che il proprietario vede e perché il generatore giudica gli esemplari uno per uno e non il salvataggio intero.
