# Lezioni per il template

> Le lezioni nate in questo progetto che valgono oltre il progetto, cioè che passano le due domande della sezione 16 di `.claude/PROJECT-SYSTEM.md`: restano vere tolti i nomi propri, e non sono già nella testa di chi lavora bene. Una voce per lezione, creata con `python .claude/templates/tools/lezioni-template.py nuova` nel giro di lavoro in cui la lezione nasce. Lo stato non si scrive qui: una lezione è recepita quando il template la elenca in `.claude/templates/lezioni-recepite.json`, che arriva con l'allineamento.

Adottato il: 2026-11-03

## L-001 - 2026-11-03 - Una risoluzione registrata senza il file fuso maschera la fusione persa

Un file fuso a mano durante un allineamento si registra in `.claude/allineamento-risolti.json` con la sola testa del template contro cui è stato risolto, e da quel momento `allinea-dal-template.py` lo dichiara ADATTATO con la nota «risolto a mano, testa invariata» senza guardare il contenuto locale. Se la fusione non arriva al commit, il registro copre un file che la fusione non contiene più. Caso osservato il 2026-11-03: il commit di allineamento del 2026-10-29 ha versionato la voce di risoluzione di `.claude/templates/anonymization/rules/anonymization.md` e la norma `norme/anonymization.md` a cui la regola fusa rimanda, ma non la regola fusa, rimasta nell'albero come modifica non committata. La sessione successiva ha visto un file modificato senza storia, lo ha scartato come residuo di un allineamento a metà, e la misura dello strumento ha continuato a dire zero conflitti, perché la voce di risoluzione bastava a chiudere il caso. La fusione è stata ricostruita dalle sei righe della testa più il paragrafo locale.

Ne seguono due prescrizioni per lo strumento. La voce di risoluzione registra anche l'impronta del contenuto locale fuso, e quando l'impronta del file non coincide più l'esito non è ADATTATO ma una ricomparsa del caso, da rimisurare. E l'allineamento, prima di registrare una risoluzione, controlla che il file fuso sia nello stesso insieme di file che il commit di allineamento porterà, perché una voce di registro versionata senza il file che descrive è lo stato in cui il registro afferma una cosa falsa.

Una lezione per chi riprende: un file modificato che un allineamento ha lasciato nell'albero si confronta con la sua voce in `allineamento-risolti.json` prima di decidere se scartarlo, perché la voce può dire che è proprio quello il contenuto voluto.
