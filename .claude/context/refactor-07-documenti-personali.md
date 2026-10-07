# Refactor 07. Una regola dichiarata sempre attiva, e tre modi in cui non lo era

> Scheda di dettaglio della voce 7 di `studio-didattico-master.md`. Entra nel template `E:/template-claude-developing`, nella regola `.claude/rules/documenti-personali.md` e nei due strumenti che la attuano, `anonymization/tools/Test-Anonymization.py` e `doc-ingest/doc-ingest.py`, prima e dopo il 2026-10-07. Il commit nel template è del proprietario.

## Il punto di partenza

ADR-100 chiedeva che la regola sui documenti personali, cioè i dati privati del proprietario come quelli bancari, fosse sempre attiva nel template, «con molta attenzione alla robustezza»: caricata in ogni sessione, con controlli che coprano le forme reali di quei dati, e con una prova che lo dimostri. In un'altra sessione la regola era già stata dichiarata sempre attiva, e `check-raggiungibilita.py` era verde. La verifica delle tre richieste ha trovato tre lacune, nessuna delle quali faceva fallire un controllo.

## Prima lacuna: la regola non c'era dove si lavorava

All'avvio di una sessione in questo progetto Claude Code carica le regole di `.claude/rules/`. Il 2026-10-07 ne ha caricate otto, e `documenti-personali.md` non era fra queste: il progetto non era stato allineato dopo la modifica del template. «Sempre attiva» valeva nel template e non nel progetto. Non si corregge con codice, perché l'allineamento è un gesto del proprietario (`allinea-tutti.ps1 -Applica`), ma va scritto nella regola stessa e ricordato nel registro delle pendenze.

## Seconda lacuna: la forma in cui un IBAN si scrive

Il riconoscitore dell'IBAN era questo:

```python
IBAN = re.compile(r"\bIT\d{2}[A-Z0-9]{20,25}\b")
```

Trova un IBAN italiano scritto tutto attaccato e in maiuscolo. Su un estratto conto, su un modulo, in una mail l'IBAN è scritto a gruppi di quattro separati da spazi, ed è spesso estero; e i numeri di carta non erano cercati affatto. Il riconoscitore nuovo accetta spazi e minuscole e qualunque paese, ma tiene un candidato solo se supera due prove che una stringa a caso non supera: la lunghezza prevista per il paese e la cifra di controllo modulo 97 della norma ISO 13616.

```python
IBAN_CANDIDATO = re.compile(r"\b[A-Za-z]{2}\d{2}(?: ?[A-Za-z0-9]){10,32}\b")

def iban_valido(testo):
    s = re.sub(r"\s", "", testo).upper()
    n = LUNGHEZZE_IBAN.get(s[:2])
    if not n or len(s) < n:
        return None
    s = s[:n]
    numero = "".join(str(int(c, 36)) for c in s[4:] + s[:4])
    return s if int(numero) % 97 == 1 else None
```

Il troncamento a `n` caratteri serve perché il candidato, ammettendo spazi, può proseguire nelle parole che seguono l'IBAN. Per le carte la validazione è Luhn più prefissi e lunghezze dei circuiti.

La misura sui file reali ha trovato subito un falso allarme: l'identificativo di un canale Discord, diciotto cifre attaccate che cominciano per 4 e passano Luhn, come capita a un numero su dieci. Due vincoli lo tolgono senza perdere carte vere: le lunghezze ammesse da ciascun circuito (Visa 13, 16 o 19, non 18) e, oltre le sedici cifre, la scrittura a gruppi, che le carte hanno e gli identificativi dei social mai. Dopo la correzione, sui file di testo versionati del template e di questo progetto, 385 e 880, zero riscontri.

## Terza lacuna: il trattino basso

L'elenco di esempio delle esclusioni di `doc-ingest` usava il confine di parola delle espressioni regolari:

```
\bIBAN\b
\bF24\b
\bISEE\b
```

Per le espressioni regolari il trattino basso è un carattere di parola, quindi fra `_` e `I` non c'è confine, e `coordinate_IBAN.pdf` o `modello_F24_2025.pdf` non venivano esclusi. I nomi di file con il trattino basso sono la forma più comune. I confini sono ora «nessuna lettera o cifra accanto»:

```
(?<![a-z0-9])IBAN(?![a-z0-9])
```

e si sono aggiunti conto corrente, carte, mutui, prestiti e rendiconti, che mancavano. Nella correzione stessa il difetto si è ripresentato in un'altra forma: lo script passato dalla shell ha trasformato la barra rovesciata seguita da `b` nel carattere backspace, e nessuna riga è stata convertita mentre il commento in testa prendeva caratteri di controllo. Rifatta da uno script scritto in un file, con il carattere composto dal codice (`chr(92)`) e una verifica che non resti alcun carattere sotto il 32.

## La prova, e la prova che la prova misura

Ognuno dei due strumenti ha ora un `--autotest`. In `Test-Anonymization.py` i valori di prova sono quelli pubblicati come esempio dalla norma e dai circuiti, composti a pezzi nel sorgente perché lo strumento non li trovi in se stesso, e ogni positivo ha un negativo che differisce per una proprietà sola; i numeri che devono passare Luhn senza essere carte si costruiscono al volo. In `doc-ingest.py` l'albero di prova ha nomi nelle forme reali e un controllo di sanità: senza elenco i file devono esserci tutti, perché una prova in cui non si trova nessun file passerebbe senza misurare nulla. Quel controllo ha colto subito un errore della prova stessa, un caso scritto come `.md`, estensione che lo strumento non converte.

La prova che la prova misura è la mutazione: con il riconoscitore vecchio dell'IBAN e quello delle carte spento, la prova fallisce in 8 casi su 17, esattamente i positivi nuovi; con l'elenco di esclusioni di prima fallisce su 5 file su 21. `chiudi` esegue le prove a ogni commit, nel template con `tools/test-documenti-personali.py`, che controlla anche che la regola esista e si dichiari da caricare sempre.

## Come estendere il pattern

«Sempre attiva» è una proprietà di dove la regola si carica, non di come è scritta, e va verificata dove si lavora. Un riconoscitore di dati personali si collauda sulle forme in cui quei dati si scrivono davvero, non sulla forma canonica, e si misura sui file reali per i falsi allarmi prima di renderlo bloccante. E il confine di parola `\b` non è un confine per i nomi di file.
