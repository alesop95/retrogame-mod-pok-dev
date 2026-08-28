---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - 3ds-related/
  - gba-save-extraction-smeraldo/
  - pokemon-gen12-gen3-bridge-original-hardware/
  - gba-switch-pokemon-trading/
  - poke-automation-study/
  - recreate-pokemon-distributions-events/
last-verified-commit: 7696c46
---

# Design e sicurezza

In un progetto software questa scheda descriverebbe superficie di attacco e gestione dei segreti. Qui il perimetro è diverso ma non più leggero: i segreti esistono e non sono ruotabili, i dati personali sono già finiti dentro il materiale di lavoro, e le operazioni distruttive agiscono su hardware fisico. Le norme operative vincolanti stanno in `rules/hardware-and-perimeter.md`; questa scheda spiega perché esistono.

## Le due tensioni di perimetro aperte dal sesto track

Il track della ricreazione delle distribuzioni, nato il 2026-08-28, mette in tensione due norme della regola sull'hardware e sul perimetro, e questa scheda le registra perché la sede di una tensione fra una norma e un obiettivo è qui, mentre la norma resta dove è scritta.

La prima è che l'obiettivo dichiarato, cioè avere in Pokemon Home tutte le specie e le forme prima della chiusura di Bank, dipende in modo essenziale dal suo ultimo tratto, e quel tratto passa da Pokemon Bank e da Pokemon Transporter su questa console, cioè dai due titoli su cui l'assistenza è esclusa. Nessuna via alternativa esiste, perché Poke Transporter è l'unico ingresso verso Home per tutto ciò che precede l'ottava generazione. La contraddizione non si risolve tecnicamente e va decisa dall'utente.

La seconda riguarda il materiale che le vie di iniezione richiedono. La regola esclude i salvataggi scaricati da internet, per il rischio che ricade sull'account e sulla console, e le tre vie di iniezione più economiche di un evento richiedono precisamente materiale di terze parti: una ROM di distribuzione da mettere su una scheda riprogrammabile, oppure un salvataggio precostituito per l'e-Reader. Va notato che non si tratta di un salvataggio di un gioco Pokemon da importare, il che rende la norma non immediatamente applicabile e la decisione non ovvia; resta che il perimetro va dichiarato prima di procurare qualcosa, e non dopo.

## Segreti non ruotabili

Il materiale di chiave console-unica è la categoria più delicata del progetto, e la sua particolarità è che non ammette la mitigazione standard. Quando un segreto ordinario trapela, lo si ruota e l'esposizione finisce. I file `movable.sed`, `boot9.bin`, `boot11.bin`, `otp.bin`, i dump della NAND e i seed di LocalFriendCodeSeed non si possono rigenerare: sono derivati dal silicio di quella specifica console. Chi li ottiene può decrittare la NAND e i salvataggi di quella console per sempre. Per questo sono esclusi dal version control con un blocco dedicato del `.gitignore`, scritto prima che i file esistano invece che dopo, e per questo non vanno incollati in una chat né caricati altrove.

Lo stesso trattamento si applica agli identificatori derivati. Il file `3ds-related/DOVE SI TROVA IL SALVATAGGIO REALE E DIFFERENZA CON CHECKPOINT.txt` contiene, dentro un output di comando, l'identificativo della cartella della SD, che è derivato da `movable.sed` e identifica univocamente la console. Non è una chiave e non permette di decrittare nulla da solo, ma è un identificatore persistente della macchina e va trattato con la stessa riservatezza.

Dal 24 agosto 2026 la stessa categoria comprende le `prod.keys` della Nintendo Switch, che il track del trading LDN richiede. Valgono le identiche proprietà: derivano dal firmware proprietario della console, si estraggono solo da una console modificata, non sono legalmente redistribuibili e non sono rigenerabili. Sono escluse dal `.gitignore` insieme alle altre varianti di file di chiave e alla cartella che le ospita per convenzione. Accanto a loro sono esclusi i file di dati Pokemon esportati, `.pk3` e i formati delle generazioni successive, che sono contenuto di salvataggio e non conoscenza tecnica.

## Dati personali

Il materiale di lavoro conteneva dati personali in chiaro. Undici dei tredici screenshot della sessione di acquisto del 18 agosto 2026 mostravano nome e cognome, due indirizzi civici, CAP, comune, provincia, numero di telefono, indirizzo email e numero d'ordine. Due di essi contenevano anche il cognome di una terza persona, l'etichetta sul campanello citata nelle note di consegna, che è un dato di qualcuno che non ha scelto di comparire in un repository.

La bonifica è stata fatta prima del primo commit, che era l'unica finestra in cui costava zero: senza storia git non c'era nulla da riscrivere. Quel materiale è stato messo in quarantena sotto `_notes/media-riservati/`, quindi non è mai entrato nella storia, e il 24 agosto 2026 è stato eliminato dal disco, perché il fatto tecnico che documentava è registrato in prosa nella scheda del sottoprogetto e conservarlo era un rischio senza contropartita. Nessuna credenziale era leggibile, perché il campo password era mascherato e il form di pagamento era vuoto.

La politica che ne discende, registrata come ADR-005, è più ampia del singolo episodio: foto, video e screenshot non si versionano mai. Sono evidenza personale, non conoscenza tecnica, e ciò che documentano si registra in prosa nella scheda del sottoprogetto, dove diventa leggibile e diffabile.

## Perimetro etico e legale

Il dump si applica soltanto a cartucce possedute. Il perimetro è dichiarato nella sezione 2 dell'handoff del sottoprogetto 3DS e vale per tutte le sessioni. Dalla stessa sezione discende un limite operativo: l'assistenza non copre l'installazione e l'uso di Pokemon Bank e Transporter su questa console, e la motivazione sta fuori dal version control, in `_notes/perimetro-bank-transporter.md`.

Va tenuto presente, quando un giorno si valutasse di rendere pubblico il repository, che questa dichiarazione è testo e resterebbe nella storia git. Oggi la repository è privata e la questione non si pone.

Il track del trading LDN porta un contesto proprio, che il suo handoff dichiara alla sezione 12 senza esprimere giudizio e che qui si registra allo stesso modo. Il lavoro poggia su reverse engineering di un protocollo di rete proprietario e del formato dati interno di un gioco commerciale, e sulla decompilazione comunitaria del gioco stesso; l'uso delle chiavi presuppone una console modificata. Il punto operativo che ne discende, e che è l'unico azionabile qui, è che quelle chiavi non escono da questa macchina e non entrano nel version control.

## Rischi operativi

I salvataggi scaricati da internet sono la causa principale dei ban quando vengono usati online o depositati su Bank, e il rischio ricade sull'account e sulla console. Le cartucce bootleg causano la perdita dei Pokemon trasferiti attraverso un ponte fra generazioni. Ogni scrittura su hardware originale è irreversibile se non esiste un backup, ed è questa la ragione per cui il backup in doppia copia e il read-back verificato sono vincoli senza eccezioni e non buone pratiche.
