# Lezioni per il template

> Le lezioni nate in questo progetto che valgono oltre il progetto, cioè che passano le due domande della sezione 16 di `.claude/PROJECT-SYSTEM.md`: restano vere tolti i nomi propri, e non sono già nella testa di chi lavora bene. Una voce per lezione, creata con `python .claude/templates/tools/lezioni-template.py nuova` nel giro di lavoro in cui la lezione nasce. Lo stato non si scrive qui: una lezione è recepita quando il template la elenca in `.claude/templates/lezioni-recepite.json`, che arriva con l'allineamento.

Adottato il: 2026-11-03

## L-001 - 2026-11-03 - Una risoluzione registrata senza il file fuso maschera la fusione persa

Un file fuso a mano durante un allineamento si registra in `.claude/allineamento-risolti.json` con la sola testa del template contro cui è stato risolto, e da quel momento `allinea-dal-template.py` lo dichiara ADATTATO con la nota «risolto a mano, testa invariata» senza guardare il contenuto locale. Se la fusione non arriva al commit, il registro copre un file che la fusione non contiene più. Caso osservato il 2026-11-03: il commit di allineamento del 2026-10-29 ha versionato la voce di risoluzione di `.claude/templates/anonymization/rules/anonymization.md` e la norma `norme/anonymization.md` a cui la regola fusa rimanda, ma non la regola fusa, rimasta nell'albero come modifica non committata. La sessione successiva ha visto un file modificato senza storia, lo ha scartato come residuo di un allineamento a metà, e la misura dello strumento ha continuato a dire zero conflitti, perché la voce di risoluzione bastava a chiudere il caso. La fusione è stata ricostruita dalle sei righe della testa più il paragrafo locale.

Ne seguono due prescrizioni per lo strumento. La voce di risoluzione registra anche l'impronta del contenuto locale fuso, e quando l'impronta del file non coincide più l'esito non è ADATTATO ma una ricomparsa del caso, da rimisurare. E l'allineamento, prima di registrare una risoluzione, controlla che il file fuso sia nello stesso insieme di file che il commit di allineamento porterà, perché una voce di registro versionata senza il file che descrive è lo stato in cui il registro afferma una cosa falsa.

Una lezione per chi riprende: un file modificato che un allineamento ha lasciato nell'albero si confronta con la sua voce in `allineamento-risolti.json` prima di decidere se scartarlo, perché la voce può dire che è proprio quello il contenuto voluto.

## L-002 - 2026-11-04 - Una skill nuova del pacchetto GRC committata senza il suo marcatore md-unwrap-ignore

Il commit 54db4c5 del template ha aggiunto la skill soc2 del pacchetto GRC senza il file .md-unwrap-ignore che le altre nove skill hanno: nel template il marcatore esiste solo nell'albero di lavoro. L'allineamento, che legge il template da HEAD, porta nei progetti le pagine della skill senza il marcatore, e il controllo md-unwrap di chiudi si ferma su due file copiati alla lettera da una fonte esterna. Il controllo che manca nel template è che ogni cartella di skill importata alla lettera abbia il suo marcatore nello stesso commit delle pagine.

## L-003 - 2026-11-05 - Una misura di copertura su un catalogo con voci gemelle non si chiude contando gli identificatori

Una misura che confronta un catalogo con ciò che si possiede, contando le voci per identificatore, resta sotto il cento per cento per sempre se il catalogo contiene voci con dati identici e identificatori diversi: prodotta la voce mancante, il verificatore la attribuisce alla gemella già coperta e la voce resta scoperta. Caso osservato: 146 carte evento su 299 scoperte erano gemelle di carte già coperte. La copertura si misura quindi attraverso l'attribuzione dello stesso verificatore: si produce la voce, la si giudica, e se l'attribuzione cade su una voce già coperta la si dichiara gemella invece di continuare a produrre o di contarla mancante.

## L-004 - 2026-11-05 - Il codice con barre rovesciate non passa da una stringa Python dentro un heredoc

Uno script di sostituzione scritto in un heredoc di Bash e passato a Python trasforma le sequenze di escape del testo nuovo: una regex con barra rovesciata e b diventa un carattere di backspace, una barra rovesciata e n un a capo, e il file risulta scritto senza errori ma con codice rotto. Un apice non bilanciato nel testo fa fallire l'intero heredoc prima di scrivere. Caso osservato tre volte nella stessa sessione. Il codice che contiene barre rovesciate si modifica con lo strumento di modifica dell'agente, oppure si scrive lo script in un file con lo strumento di scrittura e lo si lancia per percorso; dopo ogni sostituzione da script si cercano nel file i caratteri di controllo, per esempio il byte 0x08.

## L-005 - 2026-11-05 - Un subagent fermato dal limite d'uso si riprende con un messaggio e non si rilancia

Quando un subagent in background si ferma perché la quota d'uso è esaurita, il suo lavoro fatto resta nel suo contesto: lanciarne uno nuovo con lo stesso mandato rifà tutto da capo e consuma di nuovo la quota. Caso osservato: un confronto su 809 pagine si è fermato a metà, ed è stato ripreso con un messaggio dopo il ripristino della quota; ha concluso in 4 chiamate invece di ricominciare. Alla notifica del limite si annota l'ora di ripristino e si riprende lo stesso agente con un messaggio che dice da dove ripartire.
