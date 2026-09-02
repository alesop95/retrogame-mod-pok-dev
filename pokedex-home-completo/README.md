# Pokedex completo in Pokemon Home

Questo sottoprogetto ha per obiettivo la collezione completa in Pokemon Home, cioè una voce per ogni specie e per ogni forma che il deposito possa contenere. Nasce il 2026-09-02 e la sua ragione di esistere separata dagli altri track è di perimetro: riguarda tutte le generazioni e tutti i titoli, mentre gli altri sottoprogetti riguardano ciascuno un pezzo di hardware o una generazione sola.

Il rapporto con gli altri track è doppio e va detto perché governa le priorità. Questo è l'obiettivo principale a cui gli altri possono concorrere, e nello stesso tempo ciascuno di essi resta autonomo e ha uno scopo proprio che vale anche se questo non si completasse. Il ponte fra le generazioni serve il Pokedex e serve anche a se stesso; la ricreazione delle distribuzioni serve il Pokedex e serve anche a possedere quegli esemplari; il modding della console e la correzione del salvataggio corrotto servono il Pokedex e servono anche a far funzionare cose che l'utente possiede.

## Il risultato che cambia il piano, e che va letto prima di tutto

La chiusura di Pokemon Bank, fissata al 26 febbraio 2027, non vincola il completamento del Pokedex. Non lo vincola a livello di specie e non lo vincola a livello di forma, e il conto è stato eseguito e non stimato: lo strumento `tools/disponibilita-titoli.py` legge le tabelle delle statistiche di base che il verificatore di conformità porta per ciascun titolo e riferisce che tutte le millleventicinque specie del Dex Nazionale sono raggiungibili per la via diretta, cioè senza passare dalla banca, e che le dodici voci-forma che soltanto la via indiretta dichiara sono tutte escluse da un filtro letto dalla fonte: dieci sono forme totemiche, che al trasferimento tornano alla forma base o non si trasferiscono affatto, e due sono forme di sola battaglia, che non possono stare in una scatola.

Ne segue che i giorni che restano non si spendono sul Pokedex. Si spendono su ciò che la scadenza vincola davvero, che è un'altra cosa e non si conta in voci di Dex: i singoli esemplari la cui identità richiede una provenienza anteriore all'ottava generazione. Un Charizard si ottiene oggi; il Charizard della distribuzione del decennale no, perché ciò che lo distingue non è la specie ma l'allenatore, l'identificativo, il luogo di incontro e il contrassegno dell'incontro fatidico. Vale con più forza per gli esemplari che l'utente possiede su cartuccia.

Resta una sola eccezione possibile a livello di specie, e va verificata prima di considerare chiuso il discorso. Il materiale consegnato dall'utente afferma che Spinda, pur presente nei dati del titolo che sarebbe la sua via diretta, non possa esservi depositato nel deposito per un difetto di quella implementazione. Lo strumento non può vedere un difetto di quel genere, perché legge se una voce esista nei dati e non se la via funzioni, quindi quella affermazione è l'unico punto su cui il verdetto potrebbe cambiare per una specie.

## I file di questo sottoprogetto

```
README.md                          questo file
RICERCA-UTENTE-2026-09-01.md       la ricerca consegnata dall'utente, verbatim e con provenienza
STUDIO-01-che-cosa-vincola-la-scadenza.md   la verifica indipendente e il suo esito
```

Lo strumento che produce il conto sta fra quelli comuni, in `tools/disponibilita-titoli.py`, perché serve a più di un track: la sua risposta governa la pianificazione del tempo di tutto il progetto e non soltanto di questo sottoprogetto.

## Materiale locale, fuori dal version control

La consegna che ha aperto questo sottoprogetto sta in `_notes/fonti/2026-09-01-consegna-pokedex-e-collezione-theslayer.txt`, che è locale come tutto `_notes/`. Contiene i collegamenti alla collezione di riferimento mantenuta da terzi, le regole operative dichiarate dal suo autore, e le due lacune che quella collezione dichiara.
