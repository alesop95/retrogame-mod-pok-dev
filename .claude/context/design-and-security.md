---
generated-from-commit: d1e1a3a
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
  - pokemon-gen12-gen3-bridge-original-hardware/
last-verified-commit: effc2e0
---

# Design e sicurezza

In un progetto software questa scheda descriverebbe superficie di attacco e gestione dei segreti. Qui il perimetro e' diverso ma non piu' leggero: i segreti esistono e non sono ruotabili, i dati personali sono gia' finiti dentro il materiale di lavoro, e le operazioni distruttive agiscono su hardware fisico. Le norme operative vincolanti stanno in `rules/hardware-and-perimeter.md`; questa scheda spiega perche' esistono.

## Segreti non ruotabili

Il materiale di chiave console-unica e' la categoria piu' delicata del progetto, e la sua particolarita' e' che non ammette la mitigazione standard. Quando un segreto ordinario trapela, lo si ruota e l'esposizione finisce. I file `movable.sed`, `boot9.bin`, `boot11.bin`, `otp.bin`, i dump della NAND e i seed di LocalFriendCodeSeed non si possono rigenerare: sono derivati dal silicio di quella specifica console. Chi li ottiene puo' decrittare la NAND e i salvataggi di quella console per sempre. Per questo sono esclusi dal version control con un blocco dedicato del `.gitignore`, scritto prima che i file esistano invece che dopo, e per questo non vanno incollati in una chat ne' caricati altrove.

Lo stesso trattamento si applica agli identificatori derivati. Il file `3ds-related/DOVE SI TROVA IL SALVATAGGIO REALE E DIFFERENZA CON CHECKPOINT.txt` contiene, dentro un output di comando, l'identificativo della cartella della SD, che e' derivato da `movable.sed` e identifica univocamente la console. Non e' una chiave e non permette di decrittare nulla da solo, ma e' un identificatore persistente della macchina e va trattato con la stessa riservatezza.

Dal 24 agosto 2026 la stessa categoria comprende le `prod.keys` della Nintendo Switch, che il track del trading LDN richiede. Valgono le identiche proprieta': derivano dal firmware proprietario della console, si estraggono solo da una console modificata, non sono legalmente redistribuibili e non sono rigenerabili. Sono escluse dal `.gitignore` insieme alle altre varianti di file di chiave e alla cartella che le ospita per convenzione. Accanto a loro sono esclusi i file di dati Pokemon esportati, `.pk3` e i formati delle generazioni successive, che sono contenuto di salvataggio e non conoscenza tecnica.

## Dati personali

Il materiale di lavoro conteneva dati personali in chiaro. Undici dei tredici screenshot della sessione di acquisto del 18 agosto 2026 mostravano nome e cognome, due indirizzi civici, CAP, comune, provincia, numero di telefono, indirizzo email e numero d'ordine. Due di essi contenevano anche il cognome di una terza persona, l'etichetta sul campanello citata nelle note di consegna, che e' un dato di qualcuno che non ha scelto di comparire in un repository.

La bonifica e' stata fatta prima del primo commit, che era l'unica finestra in cui costava zero: senza storia git non c'era nulla da riscrivere. Quel materiale e' stato messo in quarantena sotto `_notes/media-riservati/`, quindi non e' mai entrato nella storia, e il 24 agosto 2026 e' stato eliminato dal disco, perche' il fatto tecnico che documentava e' registrato in prosa nella scheda del sottoprogetto e conservarlo era un rischio senza contropartita. Nessuna credenziale era leggibile, perche' il campo password era mascherato e il form di pagamento era vuoto.

La politica che ne discende, registrata come ADR-005, e' piu' ampia del singolo episodio: foto, video e screenshot non si versionano mai. Sono evidenza personale, non conoscenza tecnica, e cio' che documentano si registra in prosa nella scheda del sottoprogetto, dove diventa leggibile e diffabile.

## Perimetro etico e legale

Il dump si applica soltanto a cartucce possedute. Il perimetro e' dichiarato nella sezione 2 dell'handoff del sottoprogetto 3DS e vale per tutte le sessioni. Dalla stessa sezione discende un limite operativo: l'assistenza non copre l'installazione e l'uso di Pokemon Bank e Transporter su questa console, e la motivazione sta fuori dal version control, in `_notes/perimetro-bank-transporter.md`.

Va tenuto presente, quando un giorno si valutasse di rendere pubblico il repository, che questa dichiarazione e' testo e resterebbe nella storia git. Oggi la repository e' privata e la questione non si pone.

Il track del trading LDN porta un contesto proprio, che il suo handoff dichiara alla sezione 12 senza esprimere giudizio e che qui si registra allo stesso modo. Il lavoro poggia su reverse engineering di un protocollo di rete proprietario e del formato dati interno di un gioco commerciale, e sulla decompilazione comunitaria del gioco stesso; l'uso delle chiavi presuppone una console modificata. Il punto operativo che ne discende, e che e' l'unico azionabile qui, e' che quelle chiavi non escono da questa macchina e non entrano nel version control.

## Rischi operativi

I salvataggi scaricati da internet sono la causa principale dei ban quando vengono usati online o depositati su Bank, e il rischio ricade sull'account e sulla console. Le cartucce bootleg causano la perdita dei Pokemon trasferiti attraverso un ponte fra generazioni. Ogni scrittura su hardware originale e' irreversibile se non esiste un backup, ed e' questa la ragione per cui il backup in doppia copia e il read-back verificato sono vincoli senza eccezioni e non buone pratiche.
