# Disciplina dell'hardware e perimetro del progetto

Questa regola è normativa e vale su tutti i sottoprogetti. Occupa il posto che in un progetto software avrebbe `stack-profile.md`: qui non esiste uno stack di cui prescrivere le convenzioni, ma esiste un corpo di norme altrettanto vincolanti e altrettanto facili da dimenticare, perché oggi sono scritte in prosa a metà di documenti da venti chilobyte. Le operazioni che governa sono irreversibili su hardware fisico che non si può ricomprare uguale.

## Backup prima di ogni scrittura

Nessuna scrittura su una cartuccia o su una console avviene senza che esista già un backup del salvataggio originale, in doppia copia, su due percorsi distinti, verificato leggibile. Questo vincolo non ha eccezioni e non si negozia per fretta: un salvataggio di vent'anni fa non ha una seconda occasione. Vale per il percorso GBxCart RW verso FlashGBX del sottoprogetto Smeraldo, vale per qualunque tentativo di ponte fra generazioni, vale per i salvataggi sulla SD della console.

## Nessuna scrittura senza read-back verificato

Dopo aver scritto su una cartuccia si rilegge il contenuto e si confronta con quello che si intendeva scrivere. Una scrittura che il software dichiara riuscita ma che nessuno ha riletto non è una scrittura verificata. Il confronto si fa sui byte, non sull'aspetto della schermata di gioco.

## Solo hardware posseduto

Il dump di cartucce e il modding di console si applicano soltanto a esemplari di proprietà. Il perimetro è dichiarato nella sezione 2 dell'handoff del sottoprogetto 3DS ed è vincolante per tutte le sessioni, non solo per quella in cui è stato scritto.

Da quello stesso perimetro discende un limite operativo che resta valido e non va riaperto implicitamente: l'assistenza tecnica non copre l'installazione e l'uso di Pokemon Bank e Pokemon Transporter su questa console. La motivazione è una circostanza personale e sta fuori dal version control, in `_notes/perimetro-bank-transporter.md`, perché un repository pubblico non è il posto dove registrarla. Se una sessione futura si trova a toccare quell'area, il limite va ricordato e la nota locale consultata, invece di ricostruire da capo il perché.

## Salvataggi di terze parti

I salvataggi scaricati da internet non si importano su questa console. Sono la causa principale dei ban quando poi vengono usati online o depositati su Bank, e il rischio ricade sull'account e sulla console, non sul file. Se un giorno servisse davvero importarne uno, la decisione va presa esplicitamente e registrata come ADR, non fatta scivolare dentro un altro lavoro.

## Materiale di chiave console-unica

I file `movable.sed`, `boot9.bin`, `boot11.bin`, `otp.bin`, i dump della NAND e i seed di LocalFriendCodeSeed sono segreti nel senso pieno del termine e stanno nella stessa categoria di un file di credenziali. Chi li ottiene può decrittare la NAND e i salvataggi di quella specifica console, e non sono ruotabili: non esiste modo di rigenerarli. Sono esclusi dal version control dal blocco dedicato del `.gitignore`, e non vanno incollati in una chat, allegati a un messaggio o caricati su un servizio di terze parti.

Vale anche per gli identificatori derivati. L'ID della scheda SD che compare in alcune note del sottoprogetto 3DS è derivato da `movable.sed` e identifica univocamente la console: non è una chiave, ma va trattato con la stessa riservatezza.

Le `prod.keys` della Nintendo Switch, che servono al track del trading LDN, sono nella stessa categoria e per le stesse ragioni: derivate dal firmware proprietario, estraibili solo da una console modificata, non redistribuibili e non rigenerabili. Non si incollano in una chat, non si allegano, non si caricano altrove, e il `.gitignore` le esclude insieme alle altre varianti di file di chiave.

## Dump e salvataggi fuori dal repository

Nessun file di dump e nessun backup di salvataggio entra in git, indipendentemente dalla dimensione. Vivono sul disco locale e sulla SD, e la loro collocazione si annota in prosa nella scheda del sottoprogetto, così che un clone sappia dove cercarli senza contenerli.
