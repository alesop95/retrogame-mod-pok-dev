---
generated-from-commit: e692a02b8a46ab119e0389449d61327384841236
generated-from-branch: main
generated-date: 2026-09-02
covers-paths:
  - pokedex-home-completo/
last-verified-commit: e692a02b8a46ab119e0389449d61327384841236
stato: attivo
---

# Sottoprogetto: Pokedex completo in Pokemon Home

Lo stato canonico di questo track è questo file, insieme alla riga che lo riguarda in `memory/index.md`.

Obiettivo: la collezione completa in Pokemon Home, cioè una voce per ogni specie e per ogni forma che il deposito possa contenere. È l'obiettivo principale del progetto, e gli altri sottoprogetti possono concorrervi restando ciascuno autonomo con uno scopo proprio.

## Dove siamo

Aperto il 2026-09-02 con una consegna dell'utente e con una verifica indipendente che ha già prodotto il risultato che governa la pianificazione di tutto il progetto: la chiusura della banca non vincola il completamento del Pokedex, né a livello di specie né a livello di forma. Tutte e millleventicinque le specie sono raggiungibili per la via diretta, e le dodici voci-forma che soltanto la via indiretta dichiara sono escluse da un filtro letto dalla fonte, cioè dieci forme totemiche che al trasferimento tornano alla forma base o non si trasferiscono affatto, e due forme di sola battaglia che non possono stare in una scatola. Il conto lo esegue `tools/disponibilita-titoli.py` e si rifà a comando.

Ne segue che i giorni fino al 26 febbraio 2027 non si spendono qui ma sugli esemplari la cui identità richiede una provenienza anteriore all'ottava generazione, che sono materia del track delle distribuzioni e delle cartucce possedute.

## Prossimo passo concreto

Verificare l'unica affermazione che potrebbe dare una scadenza a una specie, cioè che Spinda non possa essere depositato nel deposito dal solo titolo a via diretta che lo contiene, per un difetto di quella implementazione. Criterio di successo: una fonte che dichiari il difetto, oppure la sua smentita. Lo strumento non può deciderlo, perché legge le tabelle dei dati e non il comportamento di un servizio in rete.

## Decisioni aperte

Che cosa significhi completo, cioè se la collezione comprenda ogni forma e ogni variante cosmetica oppure una voce per specie. L'utente ha indicato la lettura estesa, e resta da stabilire quali forme il deposito conti come voci separate, che nessuna fonte di primo livello documenta.

Quali titoli recenti acquistare e quando. L'utente non ne possiede alcuno e li compra all'occorrenza; la verifica dice che non sono urgenti, quindi è una decisione di spesa e non di tempo.

Il piano a pagamento del deposito, che l'utente attiverà soltanto quando tutto il resto sarà pronto, e che oggi non è attivo.

## Evidenze e materiale locale

La consegna che ha aperto il sottoprogetto sta in `_notes/fonti/2026-09-01-consegna-pokedex-e-collezione-theslayer.txt`, locale e non versionata. La ricerca dell'utente è conservata verbatim in `pokedex-home-completo/RICERCA-UTENTE-2026-09-01.md`, che è tracciata perché è una fonte con provenienza e non materiale effimero.
