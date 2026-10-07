# Refactor 08. Una fusione senza conflitti che spegneva una prova

> Scheda di dettaglio della voce 8 di `studio-didattico-master.md`. Entra nell'allineamento al template del 2026-10-07: lo strumento `allinea-dal-template.py` del template, i file `.conflitto` che lascia, `git merge-file`, e il caso di `tools/Test-Anonymization.py`.

## Il contesto

Il progetto doveva ricevere dal template la regola `documenti-personali.md` e gli strumenti resi robusti per ADR-100. La misura a vuoto dell'allineamento ha dato 14 file nuovi, 32 vecchi, uno spostato e 8 conflitti, cioè file modificati sia qui sia nel template in modi che lo strumento non sapeva fondere. Con `--applica` lo strumento ha scritto tutto il resto e ha lasciato accanto a ogni conflitto un file `.conflitto`.

## Il primo errore: che cosa c'è in un file `.conflitto`

La prima fusione a tre vie è stata fatta prendendo il `.conflitto` come versione del template. Ha dato zero conflitti su otto file, e il controllo delle righe perse diceva «zero righe del template perse». Era falso, e lo ha mostrato la lettura del risultato per `tools/chiudi-sessione.ps1`: mancava `verifica-schede.py`, che il template ha. Il `.conflitto` non è la versione del template ma la fusione che lo strumento ha tentato e scartato proprio perché perdeva righe del template; usato come «testa», porta dentro le stesse perdite e le rende invisibili, perché il controllo confrontava il risultato con il file che già le conteneva. Rifatte le fusioni con la testa presa dal template (`git show HEAD:<percorso>`), i conflitti veri erano 9 blocchi in 6 file.

La base di ciascuna fusione è il blob che `.claude/allineamento-risolti.json` registra per i file risolti a mano il 2026-09-29, e il template al commit `065d0b5` per gli altri.

## Il secondo errore, quello che non dà segni: due funzioni con lo stesso nome

`tools/Test-Anonymization.py` aveva nel progetto una prova propria, `--autotest`, sulle forme degli identificativi di console (ADR-097); il template ne ha aggiunta un'altra con lo stesso nome, su IBAN e carte (ADR-100). Le due funzioni stavano in punti diversi del file, quindi la fusione a tre vie le ha tenute entrambe senza alcun conflitto:

```python
def autotest():          # riga 234, identificativi di console, del progetto
    ...
def autotest():          # riga 461, IBAN e carte, del template
    ...
```

In Python la seconda definizione sostituisce la prima quando il modulo si carica, senza avvisi. `--autotest` avrebbe eseguito soltanto la prova del template: verde, con la prova del progetto spenta e nessun segno. La correzione rinomina le due funzioni e ne aggiunge una che le esegue entrambe:

```python
def autotest():
    return max(autotest_console(), autotest_bancari())
```

e il controllo dopo l'installazione stampa le due righe di esito, 15 controlli sulle console e 20 casi bancari, che è la prova che entrambe girano. Nello stesso file le due liste delle categorie bloccanti erano in conflitto vero, e si sono unite: «ID CONSOLE» del progetto e «CARTA DI PAGAMENTO» del template.

## Le altre risoluzioni

In `git-commands-format.md` il template aggiungeva la sesta e la settima causa, e il progetto aveva la propria frase sulla cartella e sul ramo: si tengono entrambe, con il rimando alla regola spostata riscritto verso la skill `identita-git`. In `fonti-non-recuperabili/RIFERIMENTO.md` i due lati portavano paragrafi diversi e non versioni dello stesso: si tengono tutti, togliendo dal lato del template il paragrafo sulla copia manuale che il file aveva già. In `chiudi-sessione.ps1` resta `lint-memoria.py` del progetto, entrano `verifica-schede.py` e la condizione di `lint-didattica.py` del template, e si tolgono due voci doppie. In `export-discord.py` resta il testo del progetto, che racconta il caso proprio con le sue date. Le otto risoluzioni sono registrate con `--risolto --applica`, e la misura successiva dà zero conflitti, zero file nuovi e zero vecchi.

Un dettaglio di strumento: `--risolto` senza `--applica` stampa «prova a vuoto» e non registra nulla.

## Come estendere il pattern

Prima di fondere si stabilisce che cosa contiene ciascuno dei tre file, perché un nome come `.conflitto` non lo dice. E una fusione senza conflitti non è una fusione corretta: si cercano nel risultato le definizioni con lo stesso nome, e si esegue ciò che il file deve fare, controllando nell'uscita che ogni parte attesa abbia parlato, non solo che il codice di uscita sia zero.
