# Passo 2: i giri 2, 3 e 4 di Rubino Omega, 721, 915 e 929 esemplari

> Documento autorato, scritto il 2026-11-04 su richiesta del proprietario, nella stessa forma di `RUNBOOK-PASSO-1.md`, che resta il riferimento per il perché di ogni punto. Applica `rules/hardware-and-perimeter.md`: prima di ogni scrittura sulla console una copia di riserva in due copie su due percorsi distinti e verificata, e dopo ogni scrittura una rilettura confrontata sui byte. I passi segnati «agente» li esegue l'agente, con la scheda SD inserita nel PC. Il tratto da Pokémon Bank in poi resta del proprietario e fuori dall'assistenza, come dice la stessa regola: questo documento si ferma prima della banca e riprende con la verifica in HOME. I due giri si fanno uno dopo l'altro, e il secondo comincia solo quando il primo è registrato in HOME.

## Che cosa si porta e in che stato è

Le due copie sono di Rubino Omega (versione OR), pesano 483.328 byte ciascuna e sono giudicate tutte conformi il 2026-11-04 con la libreria 26.10.18 nel contesto del salvataggio, in `_notes/lavoro/giudizi-copie/dopo-bfe89c7-pedigree.json`; il pedigree di ogni esemplare sta in `pokedex-home-completo/pedigree/HOME2.md` e `HOME3.md` e nei PDF di `_notes/stampa/pedigree/`.

| Giro | Copia | Esemplari | Box | SHA-256, inizio | Controllo a vista |
|---|---|---|---|---|---|
| 2 | `_notes/salvataggi/prove/per-home/oras-giro-2-mn-fin2/main` | 721 | da 1 a 24 pieni, box 25 con il solo posto 1 | `425e6045ee34e638` | box 1 posto 1 Pikachu livello 100, allenatore SMR2012; box 1 posto 2 Genesect livello 15, allenatore Plasma; box 25 posto 1 Suicune livello 40, allenatore Alessio |
| 3 | `_notes/salvataggi/prove/per-home/oras-giro-3-fin3/main` | 915 | da 1 a 30 pieni, box 31 con i posti da 1 a 15 | `4662a6a66ad07063` | box 1 posto 1 Garchomp livello 48, allenatore XY; box 1 posto 2 Pikachu livello 10, allenatore Satay King; box 31 posto 15 Manaphy livello 1, allenatore Alessio |

Sulla console Rubino Omega porta oggi ciò che è rimasto del giro 1 dopo il passaggio alla banca. La partita vera del proprietario, `20260821-backsic`, non si tocca e torna sulla console soltanto al passo 6. HOME mostrava 964 esemplari dopo il giro 1: dopo il giro 2 deve mostrarne 1685, dopo il giro 3 2600.

## Giro 2

Stato al 2026-11-04: punti da 1 a 15 FATTI. La copia `20261104-giro2` è stata scritta sulla SD e riletta identica; il proprietario ha fatto i punti da 5 a 12 con i controlli del punto 9 tutti giusti e le fotografie delle tre schede, uguali campo per campo al pedigree; la rilettura `20261104-rilett2` è identica alla copia (`425e6045ee34e638`), 721 Pokémon, 721 conformi, nessuna differenza di box, posto o impronta (`_notes/lavoro/giudizi-copie/rilettura-passo2-giro2.json`); rilettura e riserva `20261104-prima2` sono in `_notes/salvataggi/console/sd-checkpoint-2026-11-04/` e in `J:/backup-sd-3ds/2026-11-04/`. Punti 16 e 17 FATTI il 2026-11-04: il primo invio a Bank è caduto con il codice 006-0105, il secondo è riuscito, e HOME mostra 1685; il punto 18 è registrato in `COPIE-PER-HOME.md` e nel pedigree, dove HOME2 è «in HOME». Il giro 2 è CHIUSO e si può cominciare il giro 3.

### A. Con la scheda SD nel PC

1. Proprietario: spegni il 3DS del tutto, tenendo premuto il tasto di accensione e scegliendo Spegni, non la modalità riposo.
2. Proprietario: togli la scheda SD, inseriscila nel lettore del PC e dimmi la lettera di unità che Windows le assegna.
3. Agente: copio l'intera cartella `/3ds/Checkpoint/saves/` della SD in due posti distinti, `E:\retrogame-mod-pok-dev\_notes\salvataggi\console\sd-checkpoint-<data>\` e `J:\backup-sd-3ds\<data>\`, calcolo lo SHA-256 di ogni file sulla SD e nelle due copie, e mi fermo se un'impronta non coincide.
4. Agente: creo sulla SD la cartella `/3ds/Checkpoint/saves/0x011C4 Pokémon Omega Ruby/<data>-giro2/` e ci copio la copia del giro 2 con il nome `main`. Rileggo il file dalla SD e verifico che lo SHA-256 cominci con `425e6045ee34e638`.
5. Proprietario: espelli la SD in sicurezza da Windows, con l'icona «Rimozione sicura dell'hardware», poi rimettila nel 3DS.

### B. Sulla console

6. Proprietario: accendi il 3DS e avvia Checkpoint dal menu HOME.
7. Proprietario: scegli Pokémon Omega Ruby e fai prima di tutto una copia di riserva dello stato attuale: premi Backup e dai il nome `<data>-prima2`.
8. Proprietario: nell'elenco delle copie di Pokémon Omega Ruby seleziona `<data>-giro2`, premi Restore e conferma.
9. Proprietario: esci da Checkpoint e avvia Rubino Omega. Carica la partita e, senza giocare né salvare, apri il PC dei box. Controlla: box 1 posto 1 Pikachu livello 100, box 1 posto 2 Genesect livello 15, box 25 posto 1 Suicune livello 40; i box da 1 a 24 pieni, il box 25 con un solo Pokémon. Se una cosa non torna, fermati e dimmelo.
10. Proprietario: esci dal gioco senza salvare, dal menu HOME, chiudendo il software.
11. Proprietario: avvia di nuovo Checkpoint, scegli Pokémon Omega Ruby, premi Backup e dai il nome `<data>-rilett2`.

### C. La verifica, di nuovo con la SD nel PC

12. Proprietario: spegni il 3DS del tutto, metti la SD nel PC e dimmi la lettera di unità.
13. Agente: confronto lo SHA-256 di `<data>-rilett2/main` con quello della copia del giro 2; devono coincidere byte per byte. Se la differenza sta solo nei campi che il gioco riscrive all'apertura, la misuro e te la dico prima di andare avanti.
14. Agente: giudico `<data>-rilett2/main` con `tools/pkhex-elenco-copie`: devono risultare 721 esemplari, 721 conformi, negli stessi box e posti del giudizio del 2026-11-04. Copio la rilettura e la riserva `<data>-prima2` nelle due cartelle di riserva del punto 3.
15. Proprietario: espelli la SD in sicurezza e rimettila nel 3DS.

### D. Il tratto tuo, e la verifica in HOME

16. Proprietario: il passaggio dalla console a Pokémon Bank, il controllo in banca e il passaggio a Pokémon HOME sono tuoi, e l'assistenza non li copre. Se la banca o HOME rifiutano o segnalano un Pokémon, fermati e non ripetere: dimmi quale e con quale messaggio, e lo confronto con il giudizio di PKHeX.
17. Proprietario, in HOME, dall'app per Switch o per telefono, senza spostare nulla: il totale del deposito deve passare da 964 a 1685. Se dall'app per Switch vedi i box, il primo nuovo deve cominciare con Pikachu livello 100, allenatore SMR2012, e Genesect livello 15, allenatore Plasma; l'ultimo nuovo deve avere il solo Suicune livello 40, allenatore Alessio. Se un Pokémon mostra un'icona o un messaggio insolito, fotografa la schermata e dimmi box e posto.
18. Agente: registro l'esito in `COPIE-PER-HOME.md` e nel pedigree, dove il gruppo HOME2 passa da «in copia» a «in HOME». Solo allora si comincia il giro 3.

## Giro 3

Scritto per intero il 2026-11-05 su richiesta del proprietario, con gli stessi passaggi del giro 2 e i nomi già pronti. La data nei nomi è `20261105`: se il giro si fa un altro giorno, si usa la data di quel giorno, sempre nella forma anno, mese, giorno. La copia è `_notes/salvataggi/prove/per-home/oras-giro-3-fin3/main`, 915 esemplari, SHA-256 che comincia con `4662a6a66ad07063`, giudicata 915 conformi. Prima di cominciare, il giro 2 deve essere registrato in HOME, ed è fatto: HOME mostra 1685. Stato al 2026-11-05: punti 3 e 4 FATTI dall'agente, riserva in due copie con 19 file uguali e `20261105-giro3/main` sulla SD con l'impronta giusta; tocca al proprietario dal punto 5. Stato al 2026-11-06: punti da 5 a 14 FATTI. Il proprietario ha fatto i punti da 5 a 12 il 2026-11-05 (riserva `20261105-prima3` alle 17:39, rilettura `20261105-rilett3` alle 17:50); la rilettura è identica byte per byte alla copia (`4662a6a66ad07063`), e il giudizio con la libreria 26.10.18 dà 915 esemplari, 915 conformi, 0 differenze di box, posto, specie, forma, livello, allenatore, identificativo e impronta rispetto alla copia, con Garchomp 48 XY in 1-1, Pikachu 10 Satay King in 1-2 e Manaphy 1 Alessio in 31-15 (`_notes/lavoro/giudizi-copie/rilettura-passo2-giro3.json`). Giro 3, prima3 e rilett3 sono nelle due riserve con impronte uguali alla SD. Punti 15, 16 e 17 FATTI dal proprietario il 2026-11-06: un'eccezione di Luma3DS nel processo mint prima del passaggio (dump da leggere alla prossima SD), poi Bank riavviato, salvataggio riuscito e HOME a 2600; cinque schede uguali al pedigree. Punto 18 FATTO dall'agente il 2026-11-07: HOME3 «in HOME» nel pedigree e in `COPIE-PER-HOME.md`. Il giro 3 è CHIUSO; i giri successivi sono nella tabella in testa a `ROADMAP.md`, con questa stessa procedura.

### A. Con la scheda SD nel PC

1. Proprietario: spegni il 3DS del tutto, tenendo premuto il tasto di accensione e scegliendo Spegni, non la modalità riposo.
2. Proprietario: togli la scheda SD, inseriscila nel lettore del PC e dimmi la lettera di unità che Windows le assegna.
3. Agente: copio l'intera cartella `/3ds/Checkpoint/saves/` della SD in due posti distinti, `E:\retrogame-mod-pok-dev\_notes\salvataggi\console\sd-checkpoint-20261105\` e `J:\backup-sd-3ds\20261105\`, calcolo lo SHA-256 di ogni file sulla SD e nelle due copie, e mi fermo se un'impronta non coincide. La cartella comprende le copie di riserva `20261104-prima2` e `20261104-rilett2` del giro 2.
4. Agente: creo sulla SD la cartella `/3ds/Checkpoint/saves/0x011C4 Pokémon Omega Ruby/20261105-giro3/` e ci copio la copia del giro 3 con il nome `main`. Rileggo il file dalla SD e verifico che lo SHA-256 cominci con `4662a6a66ad07063`.
5. Proprietario: espelli la SD in sicurezza da Windows, con l'icona «Rimozione sicura dell'hardware», poi rimettila nel 3DS.

### B. Sulla console

6. Proprietario: accendi il 3DS e avvia Checkpoint dal menu HOME.
7. Proprietario: scegli Pokémon Omega Ruby e fai prima di tutto una copia di riserva dello stato attuale: premi Backup e dai il nome `20261105-prima3`.
8. Proprietario: nell'elenco delle copie di Pokémon Omega Ruby seleziona `20261105-giro3`, premi Restore e conferma.
9. Proprietario: esci da Checkpoint e avvia Rubino Omega. Carica la partita e, senza giocare né salvare, apri il PC dei box. Controlla: box 1 posto 1 Garchomp livello 48, allenatore XY; box 1 posto 2 Pikachu livello 10, allenatore Satay King; box 31 posto 15 Manaphy livello 1, allenatore Alessio; i box da 1 a 30 pieni, il box 31 con i posti da 1 a 15. Se una cosa non torna, fermati e dimmelo.
10. Proprietario: esci dal gioco senza salvare, dal menu HOME, chiudendo il software.
11. Proprietario: avvia di nuovo Checkpoint, scegli Pokémon Omega Ruby, premi Backup e dai il nome `20261105-rilett3`.

### C. La verifica, di nuovo con la SD nel PC

12. Proprietario: spegni il 3DS del tutto, metti la SD nel PC e dimmi la lettera di unità.
13. Agente: confronto lo SHA-256 di `20261105-rilett3/main` con quello della copia del giro 3; devono coincidere byte per byte. Se la differenza sta solo nei campi che il gioco riscrive all'apertura, la misuro e te la dico prima di andare avanti.
14. Agente: giudico `20261105-rilett3/main` con `tools/pkhex-elenco-copie`: devono risultare 915 esemplari, 915 conformi, negli stessi box e posti del giudizio del 2026-11-04. Copio la rilettura e la riserva `20261105-prima3` nelle due cartelle di riserva del punto 3.
15. Proprietario: espelli la SD in sicurezza e rimettila nel 3DS.

### D. Il tratto tuo, e la verifica in HOME

16. Proprietario: il passaggio dalla console a Pokémon Bank, il controllo in banca e il passaggio a Pokémon HOME sono tuoi, e l'assistenza non li copre. Se la banca o HOME rifiutano o segnalano un Pokémon, fermati e non ripetere: dimmi quale e con quale messaggio, e lo confronto con il giudizio di PKHeX.
17. Proprietario, in HOME, dall'app per Switch o per telefono, senza spostare nulla: il totale del deposito deve passare da 1685 a 2600. Fotografa il totale e tre schede a caso, con la schermata dei dati e quella delle note dell'allenatore, come per il giro 2. Se un Pokémon mostra un'icona o un messaggio insolito, fotografa la schermata e dimmi box e posto.
18. Agente: registro l'esito in `COPIE-PER-HOME.md` e nel pedigree, dove il gruppo HOME3 passa da «in copia» a «in HOME». Solo allora si comincia il passo 3.

## Giro 4

Scritto il 2026-11-09 su richiesta del proprietario, con gli stessi passaggi del giro 3 e i nomi già pronti. La copia è HOME6, `_notes/salvataggi/prove/per-home/oras-giro-4-fin9/main`, 929 esemplari, SHA-256 che comincia con `54fba3a32cd4f48d`, giudicata 929 conformi con la libreria 26.10.18 (`_notes/lavoro/giudizi-copie/dopo-adr120.json`). Il giro 3 è registrato: HOME mostra 2600, e dopo questo giro i posti occupati attesi sono 3529 su 9000. Stato al 2026-11-09: punti da 1 a 14 FATTI (dal 5 al 12 dal proprietario, il 13 e il 14 dall'agente con la SD di nuovo in `I:`); punti da 15 a 18 FATTI: giro 4 in HOME il 2026-11-09, che conta 3529. Se durante il passaggio Luma3DS mostra di nuovo un'eccezione nel processo `mint`, è l'applet eShop di sistema e non i dati della copia (ADR-120): si spegne, si riaccende e si riprende dal punto 16, senza ripristinare niente.

### A. Con la scheda SD nel PC

1. Proprietario: spegni il 3DS del tutto. FATTO.
2. Proprietario: SD nel PC, lettera `I:`. FATTO.
3. Agente: copia di `/3ds/Checkpoint/saves/` in `E:\retrogame-mod-pok-dev\_notes\salvataggi\console\sd-checkpoint-20261109\` e `J:\backup-sd-3ds\20261109\`, SHA-256 di ogni file sulla SD e nelle due copie. FATTO il 2026-11-09: 22 file, 22 uguali, comprese `20261105-prima3` e `20261105-rilett3` del giro 3.
4. Agente: cartella `/3ds/Checkpoint/saves/0x011C4 Pokémon Omega Ruby/20261109-giro4/` con la copia del giro 4 di nome `main`, riletta dalla SD. FATTO il 2026-11-09: SHA-256 `54fba3a32cd4f48d91a94d260a22686a3e3ea65653da446335a4e0e7b7790d35`, uguale alla copia.
5. Proprietario: espelli la SD in sicurezza da Windows, con l'icona «Rimozione sicura dell'hardware», poi rimettila nel 3DS. FATTO il 2026-11-09.

### B. Sulla console

6. Proprietario: accendi il 3DS e avvia Checkpoint dal menu HOME.
7. Proprietario: scegli Pokémon Omega Ruby e fai prima di tutto una copia di riserva dello stato attuale: premi Backup e dai il nome `20261109-prima4`.
8. Proprietario: nell'elenco delle copie di Pokémon Omega Ruby seleziona `20261109-giro4`, premi Restore e conferma.
9. Proprietario: esci da Checkpoint e avvia Rubino Omega. Carica la partita e, senza giocare né salvare, apri il PC dei box. Controlla: box 1 posto 1 Mew livello 30, allenatore ゲーフリ, non cromatico; box 1 posto 2 Mew livello 30, allenatore ゲーフリ, cromatico; box 31 posto 29 Pikachu livello 20, allenatore ユカリ; i box da 1 a 30 pieni, il box 31 con i posti da 1 a 29. Se una cosa non torna, fermati e dimmelo. FATTO il 2026-11-09: le otto foto del proprietario mostrano box 1 posto 1 Mew 30 ゲーフリ non cromatico (Ritrosa, ID 42317) e posto 2 lo stesso cromatico (Gentile); nel box 31 l'ultima riga ha cinque Pokémon, con Pikachu 20 Hayley al posto 28 e Pikachu 20 ユカリ al posto 29, e il sesto posto vuoto, come nel giudizio. Il proprietario li aveva contati al 29 e al 30: è la riga da sei colonne contata con un posto in più, i dati sono quelli attesi.
10. Proprietario: esci dal gioco senza salvare, dal menu HOME, chiudendo il software.
11. Proprietario: avvia di nuovo Checkpoint, scegli Pokémon Omega Ruby, premi Backup e dai il nome `20261109-rilett4`. Punti 6, 7, 8, 10 e 11 FATTI il 2026-11-09: sulla SD ci sono `20261109-prima4` delle 12:49 e `20261109-rilett4` delle 12:54.

### C. La verifica, di nuovo con la SD nel PC

12. Proprietario: spegni il 3DS del tutto, metti la SD nel PC e dimmelo. FATTO il 2026-11-09.
13. Agente: confronto lo SHA-256 di `20261109-rilett4/main` con quello della copia del giro 4; devono coincidere byte per byte. Se la differenza sta solo nei campi che il gioco riscrive all'apertura, la misuro e te la dico prima di andare avanti. FATTO il 2026-11-09: `20261109-rilett4/main` ha SHA-256 `54fba3a32cd4f48d91a94d260a22686a3e3ea65653da446335a4e0e7b7790d35`, identico alla copia del giro 4 e a `20261109-giro4/main`.
14. Agente: giudico `20261109-rilett4/main` con `tools/pkhex-elenco-copie`: devono risultare 929 esemplari, 929 conformi, negli stessi box e posti del giudizio del 2026-11-09. Copio la rilettura e la riserva `20261109-prima4` nelle due cartelle di riserva del punto 3. FATTO il 2026-11-09: `_notes/lavoro/giudizi-copie/rilettura-passo2-giro4.json`, 929 esemplari, 929 conformi, stessi box, posti e impronte del giudizio `dopo-adr120.json`; `20261109-prima4` (SHA-256 che comincia con `edef07097eafcf7c`) giudicata con 0 esemplari nei box, come atteso dopo il passaggio del giro 3; le due copie sono nelle due cartelle di riserva, con le impronte uguali alla SD.
15. Proprietario: espelli la SD in sicurezza e rimettila nel 3DS.

### D. Il tratto tuo, e la verifica in HOME

16. Proprietario: il passaggio dalla console a Pokémon Bank, il controllo in banca e il passaggio a Pokémon HOME sono tuoi, e l'assistenza non li copre. Se la banca o HOME rifiutano o segnalano un Pokémon, fermati e non ripetere: dimmi quale e con quale messaggio, e lo confronto con il giudizio di PKHeX. FERMO il 2026-11-09 al punto 16: il punto 15 è fatto; durante il passaggio la banca ha mostrato «Error Code: 006-0112» mentre comunicava con il server, e al nuovo tentativo «Communication with the server was interrupted during your previous session, so the server has been locked» e «Please wait a short while and then try to connect again». Le foto sono in `_notes/fonti/consegne/2026-11-09-giro4-console/`. Il tratto della banca resta fuori dall'assistenza (`rules/hardware-and-perimeter.md`), quindi nessuna indicazione su come proseguire lì. Dal lato dei dati, l'agente può fare una verifica in sola lettura: una copia di Checkpoint del salvataggio di Rubino Omega come è adesso, `20261109-dopo16`, senza Restore, e la SD nel PC; si giudica quanti dei 929 esemplari restano nei box, confrontandoli con `rilettura-passo2-giro4.json`. Ripreso e FATTO il 2026-11-09: al nuovo tentativo il proprietario ha spostato tutti i 31 box nella banca, che ha risposto «Success! Changes saved.», e poi li ha passati a HOME dall'app per Android, che ha risposto «The move has been completed!».
17. Proprietario, in HOME, dall'app per Switch o per telefono, senza spostare nulla: il totale del deposito deve passare da 2600 a 3529. Fotografa il totale e tre schede a caso, con la schermata dei dati e quella delle note dell'allenatore. Se un Pokémon mostra un'icona o un messaggio insolito, fotografa la schermata e dimmi box e posto. FATTO il 2026-11-09: il totale di HOME è 3529, come atteso; nessuna icona o messaggio insolito. Le schede non sono state fotografate, per scelta del proprietario di andare avanti; le foto mostrano invece le sfide di HOME (per esempio Ripetitore Ball 14 su 15, Premier Ball 11 su 15, Mega Ball 16 su 30). Foto in `_notes/fonti/consegne/2026-11-09-giro4-console/`.
18. Agente: registro l'esito in `COPIE-PER-HOME.md` e nel pedigree, dove il gruppo HOME6 passa da «pronta» a «in HOME». Poi il giro 5, HOME8, con la stessa procedura. FATTO il 2026-11-09: HOME6 «in HOME» in `tools/stampa-collezione.py`, pedigree e PDF rigenerati.

## Giro 5

Scritto il 2026-11-09, con la procedura del giro 4 e i nomi già pronti. La copia è HOME8, `_notes/salvataggi/prove/per-home/oras-giro-5-carte-mn5/main`, 256 esemplari, SHA-256 `85bd95145643e9e1b26dce896206f53b5b027ff41609e0337d0ca48cd0cabeef`, giudicata 256 conformi (`_notes/lavoro/giudizi-copie/dopo-adr120.json`): box da 1 a 8 pieni e box 9 posti da 1 a 16. HOME conta 3529 e dopo questo giro deve contarne 3785. Se Luma3DS mostra un'eccezione nel processo `mint`, si spegne, si riaccende e si riprende dal punto 16 (ADR-120).

### A. Con la scheda SD nel PC

1. Proprietario: spegni il 3DS del tutto. FATTO.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo. FATTO il 2026-11-09.
3. Agente: copia di `/3ds/Checkpoint/saves/` in `_notes/salvataggi/console/sd-checkpoint-20261109b/` e in `J:/backup-sd-3ds/20261109b/`, con lo SHA-256 di ogni file sulla SD e nelle due copie. FATTO il 2026-11-09: 25 file, 25 uguali, comprese `20261109-prima4` e `20261109-rilett4`.
4. Agente: cartella `/3ds/Checkpoint/saves/0x011C4 Pokémon Omega Ruby/20261109-giro5/` con la copia di nome `main`, riletta dalla SD. FATTO il 2026-11-09: SHA-256 `85bd95145643e9e1b26dce896206f53b5b027ff41609e0337d0ca48cd0cabeef`, uguale alla copia.
5. Proprietario: espelli la SD in sicurezza da Windows e rimettila nel 3DS. FATTO.

### B. Sulla console

6. Proprietario: accendi il 3DS e avvia Checkpoint.
7. Proprietario: Pokémon Omega Ruby, Backup, nome `20261109-prima5`.
8. Proprietario: seleziona `20261109-giro5`, Restore, conferma.
9. Proprietario: avvia Rubino Omega senza giocare né salvare e apri il PC. Controlla: box 1 posto 1 Bulbasaur livello 10, allenatore ヨコハマ; box 1 posto 2 Charmander livello 10, allenatore トウキョー; box 9 posto 16 Skitty livello 10, allenatore フクオカ; box da 1 a 8 pieni, box 9 con i posti da 1 a 16 (la riga in alto ha sei posti, quindi il 16 è il quarto della terza riga). Se una cosa non torna, fermati e dimmelo.
10. Proprietario: esci senza salvare, chiudendo il software dal menu HOME.
11. Proprietario: Checkpoint, Pokémon Omega Ruby, Backup, nome `20261109-rilett5`. Punti 6-11 FATTI il 2026-11-09: `20261109-prima5` (0 esemplari nei box, SHA-256 che comincia con `5cd017989abde5ad`) e, al secondo passaggio, `20261109-rilett5`.

### C. La verifica, di nuovo con la SD nel PC

12. Proprietario: spegni il 3DS, SD nel PC, e dimmelo. FATTO.
13. Agente: SHA-256 di `20261109-rilett5/main` uguale a quello della copia. FATTO il 2026-11-09: `85bd9514…`, identico.
14. Agente: giudizio di `20261109-rilett5/main` con `tools/pkhex-elenco-copie`, 256 conformi negli stessi posti; `prima5` e `rilett5` nelle due cartelle di riserva. FATTO il 2026-11-09: `_notes/lavoro/giudizi-copie/rilettura-passo2-giro5.json`, 256 conformi su 256, stessi posti e impronte; riserve con impronte uguali.
15. Proprietario: espelli la SD e rimettila nel 3DS.

### D. Il tratto tuo, e la verifica in HOME

16. Proprietario: il passaggio alla banca e poi a HOME è tuo, fuori dall'assistenza.
17. Proprietario: in HOME il totale deve passare da 3529 a 3785; fotografa il totale. Punti 15-17 FATTI il 2026-11-09: HOME conta 3785.
18. Agente: HOME8 «in HOME» in `tools/stampa-collezione.py`, pedigree, `COPIE-PER-HOME.md`, `ROADMAP.md`; poi il giro 6, HOME9. FATTO il 2026-11-09: HOME8 «in HOME», pedigree e PDF rigenerati.

## Giro 6

Scritto il 2026-11-09 con la stessa procedura del giro 5. La copia è HOME9, `_notes/salvataggi/prove/per-home/oras-giro-6-statici-eventi-4/main`, 695 esemplari (i 694 della copia del 2026-11-07 più il Rayquaza di Pokémon Box), SHA-256 `374e8c502f895b5909b63131df6a0207cc12bff5288a3d237de490cf663db292`, giudicata 695 conformi (`_notes/lavoro/giudizi-copie/dopo-20261109.json`): box da 1 a 23 pieni e box 24 posti da 1 a 5. HOME conta 3785 e dopo questo giro deve contarne 4480.

1. Proprietario: spegni il 3DS del tutto. FATTO.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo. FATTO il 2026-11-09.
3. Agente: copia di `/3ds/Checkpoint/saves/` in `_notes/salvataggi/console/sd-checkpoint-20261109c/` e in `J:/backup-sd-3ds/20261109c/`, con lo SHA-256 di ogni file. FATTO il 2026-11-09: 28 file, 28 uguali.
4. Agente: cartella `20261109-giro6` di Pokémon Omega Ruby con la copia di nome `main`, riletta dalla SD. FATTO il 2026-11-09: SHA-256 `374e8c50…`, uguale alla copia.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: Pokémon Omega Ruby, Backup, nome `20261109-prima6`.
8. Proprietario: seleziona `20261109-giro6`, Restore, conferma.
9. Proprietario: avvia Rubino Omega senza salvare e controlla: box 1 posto 1 Snorlax livello 30, box 1 posto 2 Hypno livello 30, entrambi con allenatore Alessio; box 24 posto 5 Rayquaza livello 70 cromatico; box da 1 a 23 pieni, box 24 con i posti da 1 a 5.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Omega Ruby, Backup, nome `20261109-rilett6`. Punti 5-12 FATTI il 2026-11-09.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `20261109-rilett6/main` uguale a quello della copia. FATTO il 2026-11-09: `374e8c50…`, identico.
14. Agente: giudizio della rilettura, 695 conformi negli stessi posti; `prima6` e `rilett6` nelle due riserve. FATTO il 2026-11-09: `rilettura-passo2-giro6.json`, 695 su 695 negli stessi posti; `prima6` con 0 esemplari nei box; riserve uguali.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME, fuori dall'assistenza.
17. Proprietario: HOME da 3785 a 4480, foto del totale. Punti 15-17 FATTI il 2026-11-09, con un'eccezione: HOME conta 4474, cioè 689 esemplari in più e non 695. I sei rimasti nel box 16 di Rubino Omega, posti da 24 a 29, sono i sei Pikachu Cosplay (Rockstar, Damigella, Confetto, Scienziata, Wrestler e Cosplay), che il gioco non lascia uscire dalla sesta generazione. Il progetto lo sapeva già (`CONNETTIVITA-HOME.md`), ma la copia li conteneva, perché la libreria li giudica conformi in Rubino Omega e nessun controllo della scrittura guardava il passaggio. Restano dove sono, e HOME non registra il Pikachu Cosplay, quindi al Pokédex non manca niente. Le altre copie non ne hanno: le restanti sono tutte di settima generazione.
18. Agente: HOME9 «in HOME», pedigree; poi il giro 7, HOME4, il primo di Luna. FATTO il 2026-11-09: HOME9 «in HOME» in `tools/stampa-collezione.py`, con la nuova regola `resta_in_console` che marca i sei Pikachu Cosplay «resta in Rubino Omega»; pedigree e PDF rigenerati; i totali attesi dei giri successivi scendono di 6.

## Giro 7

Scritto il 2026-11-09 con la stessa procedura, ed è il primo giro su Pokémon Luna. La copia è HOME4, `_notes/salvataggi/prove/per-home/luna-giro-1-fin/main`, 93 esemplari, SHA-256 `48b8afa547b3391f946f4b45c7e40a3bb4d26c1c5e6f0aae64e06d8aaa6e150e`, giudicata 93 conformi (`_notes/lavoro/giudizi-copie/dopo-20261109b.json`): box da 1 a 3 pieni e box 4 posti da 1 a 3. In Checkpoint il gioco è `0x0175E Pokémon Moon`, la cartella che contiene già `20260823-backsicMoo`, la partita vera, che non si tocca. HOME conta 4474 e dopo questo giro deve contarne 4567.

1. Proprietario: spegni il 3DS del tutto. FATTO.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo. FATTO il 2026-11-09.
3. Agente: copia di `/3ds/Checkpoint/saves/` in `_notes/salvataggi/console/sd-checkpoint-20261109d/` e in `J:/backup-sd-3ds/20261109d/`, con lo SHA-256 di ogni file; dentro c'è anche `20261109-giro6` di Rubino Omega, che le riserve precedenti non avevano. FATTO il 2026-11-09: 31 file, 31 uguali; rispetto alla riserva `c` l'unico file in più è `20261109-giro6/main`.
4. Agente: cartella `20261109-giro7` di Pokémon Moon con la copia di nome `main`, riletta dalla SD. Se il giro si fa un altro giorno, la data dei nomi è quella del giorno. FATTO il 2026-11-09: SHA-256 `48b8afa5…`, uguale alla copia, 441856 byte come la partita vera `20260823-backsicMoo`.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: scegli Pokémon Moon, Backup, nome `20261109-prima7`.
8. Proprietario: seleziona `20261109-giro7`, Restore, conferma.
9. Proprietario: avvia Luna senza salvare e controlla: box 1 posto 1 Tapu Koko livello 60 cromatico, allenatore Melemele; box 1 posto 2 Silvally livello 100 cromatico, allenatore エーテル; box 2 posto 10 Psyduck livello 15, allenatore STADIO, con Graffio e Amnesia; box 4 posto 3 Mew livello 5, allenatore GF; box da 1 a 3 pieni, box 4 con i posti da 1 a 3.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Moon, Backup, nome `20261109-rilett7`. Punti 5-12 FATTI il 2026-11-09.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `20261109-rilett7/main` uguale a quello della copia. FATTO il 2026-11-09: `48b8afa5…`, identico.
14. Agente: giudizio della rilettura, 93 conformi negli stessi posti; `prima7` e `rilett7` nelle due riserve. FATTO il 2026-11-09: `rilettura-passo2-giro7.json`, 93 su 93, 0 differenze di box, posto, specie, forma, livello, allenatore, ID e impronta; riserve uguali. `prima7` (`7a48382b…`) è identica a `20260930-luna2`, la copia di prova del 2026-09-30 che stava in Luna: 268 esemplari, 147 conformi, quasi tutti doni della Console Virtuale di una generazione dei lotti precedente, fra cui il Mew YOSHIRA e i due Farfetch'd di Stadium 2 non bonificati. Non era la partita vera, che resta in `20260823-backsicMoo`, e non era destinata a HOME; resta nelle riserve e nella sua cartella sulla SD.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME, fuori dall'assistenza. Da guardare in questo giro: lo Psyduck STADIO del box 2 posto 10. A un utente di r/pokemonhome il Trasferitore ha rifiutato uno Psyduck di Stadium con Amnesia; il nostro è già in Luna, quindi il Trasferitore non lo vede e passa solo dalla banca. Se la banca o HOME lo rifiutano, come per i Pikachu del giro 6, lascialo nel box e dimmi che messaggio compare.
17. Proprietario: HOME da 4474 a 4567, foto del totale; se ne mancano, foto del box di Luna con quelli rimasti. Punti 15-17 FATTI il 2026-11-09: il proprietario riferisce il giro passato in HOME e il totale, scritto «457», cioè 4567 con una cifra persa; nessun rifiuto, Psyduck STADIO compreso.
18. Agente: HOME4 «in HOME», pedigree; poi il giro 8, HOME5, il primo di Ultraluna. FATTO il 2026-11-09: HOME4 «in HOME» in `tools/stampa-collezione.py`, pedigree e PDF rigenerati.

## Giro 8

Scritto il 2026-11-09, ed è il primo giro su Pokémon Ultraluna. La copia è HOME5, `_notes/salvataggi/prove/per-home/ultraluna-giro-1-scambi-fin2/main`, 613 esemplari, 445440 byte, SHA-256 `ef7d80668b6ae4bb26aeeaae6e24ddab1df7c1db5a3c8db6532af6fd70c4da7d`, giudicata 613 conformi (`_notes/lavoro/giudizi-copie/dopo-20261109b.json`): box da 1 a 20 pieni e box 21 posti da 1 a 13. HOME conta 4567 e dopo questo giro deve contarne 5180.

Cambia l'ordine dei primi passi, perché sulla SD Checkpoint non ha ancora una cartella di Ultraluna: la crea la prima copia di riserva fatta in console, con il nome che Checkpoint ricava dal gioco, e l'agente non lo indovina. Quindi la riserva della partita attuale si fa prima, in console, e solo dopo la SD va nel PC. La stessa riserva prova anche che Ultraluna è sulla console: se Checkpoint non la elenca, ci si ferma lì.

0. Proprietario, aggiunto il 2026-11-10 (ADR-124): il gioco è all'inizio e non ha un salvataggio, quindi Checkpoint non lo può elencare. Avvia una partita nuova di Ultraluna, gioca fino al primo momento in cui il menu (tasto X) offre Salva, salva una volta e spegni. La partita nuova non va conservata: la copia HOME5, che è il salvataggio di terzi `main-ultraluna` con i box riempiti, la sostituisce al punto 7.
1. Proprietario: avvia Checkpoint e cerca Pokémon Ultra Moon nell'elenco. Se non c'è, fermati e dimmelo. Aggiunto il 2026-11-10: dopo il punto 0 Checkpoint non la elencava, perché la sua cache dei titoli (`fullsavecache`, `fullextdatacache`, `titles.sha` in `/3ds/Checkpoint/`) era del 2026-11-04, quando Ultraluna, installata sulla SD dal 2026-09-30 come `001b5100`, non aveva ancora un salvataggio. L'agente ha copiato i tre file in `_notes/salvataggi/console/checkpoint-cache-20261110/` e li ha rinominati sulla SD con il suffisso `.vecchia-20261110`, così Checkpoint rifà la scansione al prossimo avvio, più lento del solito.
2. Proprietario: scegli Pokémon Ultra Moon, Backup, nome `20261109-prima8`. Questa è la riserva della tua partita di Ultraluna, e crea la cartella del gioco.
3. Proprietario: spegni il 3DS del tutto, metti la SD nel PC, lettera `I:`, e dimmelo.
4. Agente: copia di `/3ds/Checkpoint/saves/` in `_notes/salvataggi/console/sd-checkpoint-20261109e/` e in `J:/backup-sd-3ds/20261109e/`, con lo SHA-256 di ogni file; controllo che `20261109-prima8/main` sia un salvataggio di Ultraluna della stessa misura della copia e lo giudico, così si sa che cosa c'era nella partita. FATTO il 2026-11-10 con i nomi del giorno: il proprietario ha chiamato la riserva `20261110-prima8`, SHA-256 `4d15853aac14fcb5bbbb07bcb8fae7a28ff57a8626a24b59c6f93592a8c2c421`, 445440 byte come la copia, gioco `UM`, box vuoti (`_notes/lavoro/giudizi-copie/prima8-20261110.json`, lo starter sta in squadra e la libreria legge i soli box); riserve `_notes/salvataggi/console/sd-checkpoint-20261110/` e `J:/backup-sd-3ds/20261110/`, 35 file uguali alla SD. Dal punto 5 i nomi del giorno sono `20261110-giro8` e `20261110-rilett8`.
5. Agente: cartella `20261109-giro8` accanto a `20261109-prima8`, con la copia di nome `main`, riletta dalla SD. FATTO il 2026-11-10 come `20261110-giro8/main`, SHA-256 riletto dalla SD uguale alla copia, `ef7d8066…`.
6. Proprietario: espelli la SD e rimettila nel 3DS.
7. Proprietario: avvia Checkpoint, scegli Pokémon Ultra Moon, seleziona `20261109-giro8`, Restore, conferma.
8. Proprietario: avvia Ultraluna senza salvare e controlla: box 1 posto 1 Poipole livello 40 cromatico, allenatore Ultra; box 1 posto 2 Zeraora livello 50, allenatore Fula City; box 21 posto 13 Pikachu livello 40, allenatore Alessio; box da 1 a 20 pieni, box 21 con i posti da 1 a 13.
9. Proprietario: esci senza salvare.
10. Proprietario: Checkpoint, Pokémon Ultra Moon, Backup, nome `20261109-rilett8`.
11. Proprietario: spegni, SD nel PC, e dimmelo.
12. Agente: SHA-256 di `20261109-rilett8/main` uguale a quello della copia. FATTO il 2026-11-10: il proprietario ha fatto i punti 6-11 con il nome del giorno, `20261110-rilett8/main`, 445440 byte, SHA-256 `ef7d8066…`, uguale alla copia.
13. Agente: giudizio della rilettura, 613 conformi negli stessi posti; `rilett8` nelle due riserve. FATTO il 2026-11-10: `_notes/lavoro/giudizi-copie/rilettura-passo2-giro8.json`, gioco UM, 613 su 613 conformi, 0 differenze di box, posto, specie, forma, livello, allenatore, ID, PID, impronta e giudizio rispetto alla copia; box 1 posto 1 Poipole 40 cromatico di Ultra, box 1 posto 2 Zeraora 50 di Fula City, box 21 posto 13 Pikachu 40 di Alessio. `rilett8` in `sd-checkpoint-20261110` e in `J:/backup-sd-3ds/20261110/`, SHA-256 uguale. Tolte dalla SD le tre copie `.vecchia-20261110` della cache di Checkpoint, che l'ha ricostruita alle 15:49 ed è identica alla riserva in `checkpoint-cache-20261110`.
14. Proprietario: SD nel 3DS.
15. Proprietario: il passaggio alla banca e a HOME, fuori dall'assistenza. Se qualcuno resta nei box, lascialo lì e dimmi box, posto e messaggio.
16. Proprietario: HOME da 4567 a 5180, foto del totale; se ne mancano, foto del box di Ultraluna con quelli rimasti.
17. Agente: HOME5 «in HOME», pedigree; poi il giro 9, HOME7, sempre su Ultraluna, con la procedura dei giri di Rubino Omega, perché la cartella a quel punto c'è.

Punti 14-17 FATTI il 2026-11-10. HOME conta 5176, cioè 4567 più 609: la banca ha lasciato nel box 21 di Ultraluna i posti 3, 5, 7 e 10, che sono i doni di taglia totem di Araquanid, Togedemaru, Marowak e Ribombee, non trasferibili oltre la settima generazione secondo la libreria (`EncounterStatic7.IsTotemNoTransfer`). Restano lì; HOME5 è «in HOME» in `tools/stampa-collezione.py`, con i quattro marcati «resta in Ultraluna», pedigree e PDF rigenerati.

## Giro 9

Scritto il 2026-11-10, ed è il secondo giro su Pokémon Ultraluna, con la procedura del giro 7, perché la cartella di Checkpoint `0x01B51 Pokémon Ultra Moon` adesso esiste. La copia è HOME7, `_notes/salvataggi/prove/per-home/ultraluna-giro-2-fin7/main`, 642 esemplari, 445440 byte, SHA-256 `15526468e27588dfdc76115151f0ab30030db243dc5889ab0cb0aa7c3bfa8d2c`, giudicata 642 conformi (`_notes/lavoro/giudizi-copie/dopo-20261109b.json`): box da 1 a 21 pieni e box 22 posti da 1 a 12. Non contiene esemplari che il gioco non lascia uscire: i due di forma «Grande» sono Pumpkaboo e Gourgeist di taglia grande, non totem. HOME conta 5176 e dopo questo giro deve contarne 5818.

La partita che Ultraluna ha adesso è HOME5 dopo la banca, con i quattro doni di taglia totem rimasti nel box 21, posti 3, 5, 7 e 10. Il Restore del punto 8 la sostituisce: i quattro restano nella riserva `prima9` del punto 7, nelle due riserve del PC e nella copia HOME5, quindi non si perdono, ma dopo il giro 9 non sono più nella partita in console.

Stato al 2026-11-11: punti 1-4 FATTI. La SD è nel PC in `I:`; `/3ds/Checkpoint/saves/` è copiata in `_notes/salvataggi/console/sd-checkpoint-20261111/` e in `J:/backup-sd-3ds/20261111/`, 37 file, ciascuna verificata con `sha256sum -c` contro la SD, tutti uguali; `20261111-giro9/main` è sulla SD, 445440 byte, riletta con SHA-256 `15526468…` uguale a HOME7. I nomi del giorno sono `20261111-prima9` e `20261111-rilett9`. Tocca al proprietario dal punto 5.

Stato al 2026-11-11, più tardi: il proprietario ha fatto i punti 5-7, con la riserva `20261111-prima9`, poi ha aperto Ultraluna prima del Restore e l'ha trovata senza Pokémon nei box che ha guardato. È lo stato atteso, perché dopo il giro 8 la partita ha solo i quattro totem nel box 21: la riserva è giusta e non va cancellata, e il punto 7 adesso lo dice. La SD rimessa nel PC non era visibile da Windows, quindi `prima9` si giudica al punto 14 insieme alla rilettura. Si riprende dal punto 8.

Stato al 2026-11-11, sera: punti 8-14 FATTI. Il proprietario ha fatto il Restore, i controlli del punto 9 e il Backup `20261111-rilett9`. Punto 13: `20261111-rilett9/main` ha SHA-256 `15526468…`, uguale a HOME7. Punto 14: riserve `_notes/salvataggi/console/sd-checkpoint-20261111b/` e `J:/backup-sd-3ds/20261111b/`, 40 file ciascuna, verificate con `sha256sum -c` contro la SD, tutte uguali; elenco delle impronte in `_notes/salvataggi/console/sd-20261111b.sha256` e `J:/backup-sd-3ds/sd-20261111b.sha256`; giudizio in `_notes/lavoro/giudizi-copie/rilettura-passo2-giro9.json`, `rilett9` 642 esemplari, 642 conformi, negli stessi posti di HOME7 e con tutti i campi uguali a `dopo-20261109b.json`, impronte comprese; `prima9` (SHA-256 `694c1546…`) 4 esemplari, i totem Araquanid, Togedemaru, Marowak e Ribombee nel box 21, posti 3, 5, 7 e 10, conformi e identici a quelli della copia HOME5. Tocca al proprietario dal punto 15.

1. Proprietario: spegni il 3DS del tutto.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo.
3. Agente: copia di `/3ds/Checkpoint/saves/` in `_notes/salvataggi/console/sd-checkpoint-<data>/` e in `J:/backup-sd-3ds/<data>/`, con lo SHA-256 di ogni file, dove la data è quella del giorno (con una lettera se nello stesso giorno c'è già una riserva).
4. Agente: cartella `<data>-giro9` di Pokémon Ultra Moon con la copia di nome `main`, riletta dalla SD.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: scegli Pokémon Ultra Moon, Backup, nome `<data>-prima9`. È la partita com'è adesso, prima del giro: box da 1 a 20 vuoti e soltanto i quattro totem nel box 21, posti 3, 5, 7 e 10, quindi è giusto che il gioco sembri vuoto. Non si rifà e non si cancella: i Pokémon del giro arrivano solo con il Restore del punto 8, e i controlli del punto 9 si fanno dopo il Restore.
8. Proprietario: seleziona `<data>-giro9`, Restore, conferma.
9. Proprietario: avvia Ultraluna senza salvare e controlla: box 1 posto 1 Spinda livello 1 cromatico, allenatore Alessio; box 1 posto 25 Zygarde livello 100 cromatico, allenatore 2018 Legends; box 22 posto 1 Ursaring livello 25, allenatore Alessio; box 22 posto 12 Gastrodon Mare Est livello 100, allenatore GIULIA; box da 1 a 21 pieni, box 22 con i posti da 1 a 12.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Ultra Moon, Backup, nome `<data>-rilett9`.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `<data>-rilett9/main` uguale a quello della copia.
14. Agente: giudizio della rilettura, 642 conformi negli stessi posti; `prima9` giudicata, con i quattro totem attesi nel box 21; `prima9` e `rilett9` nelle due riserve.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME, fuori dall'assistenza. Se qualcuno resta nei box, lascialo lì e dimmi box e posto, o mandami la foto del box.
17. Proprietario: HOME da 5176 a 5818, foto del totale; se ne mancano, foto del box di Ultraluna con quelli rimasti.
18. Agente: HOME7 «in HOME», pedigree; poi il giro 10, HOME10, sempre su Ultraluna.

Punti 15-18 FATTI il 2026-11-13. HOME conta 5818, cioè 5176 più tutti i 642 esemplari, letto dalla foto del totale «All Pokémon» mandata dal proprietario; nessuno è rimasto nei box. HOME7 è «in HOME» in `tools/stampa-collezione.py`, pedigree e PDF rigenerati; `tools/sfide-bank.py` dà 47 sfide coperte su 47.

## Giro 10

Scritto il 2026-11-13, ed è il terzo giro su Pokémon Ultraluna, con la stessa procedura del giro 9. La copia è HOME10, `_notes/salvataggi/prove/per-home/ultraluna-giro-3-statici-gb-finale119/main`, 380 esemplari, 445440 byte, SHA-256 `f7fdf3f8ef08a1bdf71f427eb1f7d51cca41a19c112e7796a3344283e2fdfcbc`, giudicata 380 conformi (`_notes/lavoro/giudizi-copie/dopo-20261109b.json`): box da 1 a 12 pieni e box 13 posti da 1 a 20. Contiene il marchio Game Boy dal 2026-11-09 (ADR-120), i 117 di FINALE senza la mossa d'evento (ADR-121) e i 2 Farfetch'd di Stadium 2 bonificati nel box 13, posti 19 e 20 (ADR-122). Nessun esemplare che il gioco non lascia uscire, con la stessa regola del pedigree (`resta_in_console`). HOME conta 5818 e dopo questo giro deve contarne 6198.

La partita che Ultraluna ha adesso è HOME7 dopo la banca, con i box vuoti: è giusto che la riserva `prima10` del punto 7 sembri vuota.

Stato al 2026-11-13: punti 1-4 FATTI. `/3ds/Checkpoint/saves/` è copiata in `_notes/salvataggi/console/sd-checkpoint-20261113/` e in `J:/backup-sd-3ds/20261113/`, 40 file, ciascuna verificata con `sha256sum -c` contro l'elenco preso dalla SD, tutti uguali; l'elenco sta in `_notes/salvataggi/console/sd-20261113.sha256` e `J:/backup-sd-3ds/sd-20261113.sha256`. `20261113-giro10/main` è sulla SD, 445440 byte, riletta con SHA-256 `f7fdf3f8…` uguale a HOME10. I nomi del giorno sono `20261113-prima10` e `20261113-rilett10`. Tocca al proprietario dal punto 5.

Stato al 2026-11-13, più tardi: punti 5-14 FATTI. Il proprietario ha fatto il Backup `20261113-prima10`, il Restore, i controlli del punto 9 e il Backup `20261113-rilett10`. Punto 13: `20261113-rilett10/main` ha SHA-256 `f7fdf3f8…`, uguale a HOME10. Punto 14: riserve `_notes/salvataggi/console/sd-checkpoint-20261113b/` e `J:/backup-sd-3ds/20261113b/`, 43 file ciascuna, verificate con `sha256sum -c` contro l'elenco preso dalla SD (`sd-20261113b.sha256` accanto a ciascuna), tutte uguali; giudizio in `_notes/lavoro/giudizi-copie/rilettura-passo2-giro10.json`, libreria 26.10.18: `rilett10` 380 esemplari, 380 conformi, negli stessi posti di HOME10 e con tutti i campi uguali a `dopo-20261109b.json`, impronte comprese, salvo `origine`, che lo strumento legge dal rapporto della copia e che una rilettura dalla console non ha (vuoto anche in `rilett9`); `prima10` (SHA-256 `4771cd06…`) 0 esemplari nei box, come atteso. Tocca al proprietario dal punto 15.

1. Proprietario: spegni il 3DS del tutto.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo.
3. Agente: copia di `/3ds/Checkpoint/saves/` in `_notes/salvataggi/console/sd-checkpoint-<data>/` e in `J:/backup-sd-3ds/<data>/`, con lo SHA-256 di ogni file, dove la data è quella del giorno (con una lettera se nello stesso giorno c'è già una riserva).
4. Agente: cartella `<data>-giro10` di Pokémon Ultra Moon con la copia di nome `main`, riletta dalla SD.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: scegli Pokémon Ultra Moon, Backup, nome `<data>-prima10`. È la partita com'è adesso, prima del giro, con i box vuoti. Non si rifà e non si cancella.
8. Proprietario: seleziona `<data>-giro10`, Restore, conferma.
9. Proprietario: avvia Ultraluna senza salvare e controlla: box 1 posto 1 Bulbasaur livello 5, allenatore Alessio; box 1 posto 30 Pinsir livello 30, allenatore Alessio; box 13 posto 19 Farfetch'd livello 5, allenatore Stadium; box 13 posto 20 Farfetch'd livello 5, allenatore Stadio; box da 1 a 12 pieni, box 13 con i posti da 1 a 20.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Ultra Moon, Backup, nome `<data>-rilett10`.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `<data>-rilett10/main` uguale a quello della copia.
14. Agente: giudizio della rilettura, 380 conformi negli stessi posti; `prima10` giudicata, con i box vuoti; `prima10` e `rilett10` nelle due riserve.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME, fuori dall'assistenza. Se qualcuno resta nei box, lascialo lì e dimmi box e posto, o mandami la foto del box.
17. Proprietario: HOME da 5818 a 6198, foto del totale; se ne mancano, foto del box di Ultraluna con quelli rimasti.
18. Agente: HOME10 «in HOME», pedigree; poi il giro 11, GIAPPONE2, su Luna con il profilo giapponese.

Punti 15-18 FATTI il 2026-11-13. HOME conta 6198, cioè 5818 più tutti i 380 esemplari, letto dalla foto del totale «All Pokémon» mandata dal proprietario; nessuno è rimasto nei box. HOME10 è «in HOME» in `tools/stampa-collezione.py`, pedigree e PDF rigenerati; `tools/sfide-bank.py` dà 47 sfide coperte su 47.

## Giro 11

Scritto il 2026-11-13 per ADR-125, ed è l'ultimo giro, il secondo su Pokémon Luna, con i 23 esemplari insieme e senza la prova con uno solo che il passo 4 della roadmap prevedeva. La copia è GIAPPONE2, `_notes/salvataggi/prove/per-home/luna-giappone-3/main`, 23 esemplari giapponesi della prima generazione, 441856 byte, SHA-256 `e4eb2dd84366d52d9839750002aa0977e0c233ba85967a67f8915f6e86096288`, giudicata 23 conformi (`_notes/lavoro/giudizi-copie/dopo-20261109b.json`): box 1 posti da 1 a 23. È una copia della Luna del proprietario con la regione di una console giapponese, perché un dono giapponese della Console Virtuale si trasferisce solo da lì; la partita vera di Luna, `20260823-backsicMoo`, non si tocca e torna con il passo 6. In Checkpoint il gioco è `0x0175E Pokémon Moon`. HOME conta 6200, cioè i 6198 del giro 10 più il Cyndaquil e il Melmetal arrivati da GO, e dopo questo giro deve contarne 6223.

La partita che Luna ha adesso è HOME4 dopo la banca del giro 7, con i box vuoti: è giusto che la riserva `prima11` del punto 7 sembri vuota.

Stato al 2026-11-13: punti 1-4 FATTI. `/3ds/Checkpoint/saves/` è copiata in `_notes/salvataggi/console/sd-checkpoint-20261113c/` e in `J:/backup-sd-3ds/20261113c/`, 43 file, ciascuna verificata con `sha256sum -c` contro l'elenco preso dalla SD (`sd-20261113c.sha256` accanto a ciascuna), tutti uguali. `20261113-giro11/main` è nella cartella `0x0175E Pokémon Moon` della SD, 441856 byte, riletta con SHA-256 `e4eb2dd8…` uguale a GIAPPONE2. I nomi del giorno sono `20261113-prima11` e `20261113-rilett11`. Tocca al proprietario dal punto 5.

Stato al 2026-11-13, più tardi: punti 5-14 FATTI. Il proprietario ha fatto il Backup `20261113-prima11`, il Restore, i controlli del punto 9 e il Backup `20261113-rilett11`. Punto 13: `20261113-rilett11/main` ha SHA-256 `e4eb2dd8…`, uguale a GIAPPONE2. Punto 14: riserve `_notes/salvataggi/console/sd-checkpoint-20261113d/` e `J:/backup-sd-3ds/20261113d/`, 46 file ciascuna, verificate con `sha256sum -c` contro l'elenco preso dalla SD (`sd-20261113d.sha256` accanto a ciascuna), tutte uguali; giudizio in `_notes/lavoro/giudizi-copie/rilettura-passo2-giro11.json`, libreria 26.10.18: `rilett11` 23 esemplari, 23 conformi, negli stessi posti di GIAPPONE2 e con tutti i campi uguali a `dopo-20261109b.json`, impronte comprese, salvo `origine`, che una rilettura dalla console non ha; `prima11` (SHA-256 `f32c7e42…`) 0 esemplari nei box, come atteso. Tocca al proprietario dal punto 15.

1. Proprietario: spegni il 3DS del tutto.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo.
3. Agente: copia di `/3ds/Checkpoint/saves/` in `_notes/salvataggi/console/sd-checkpoint-<data>/` e in `J:/backup-sd-3ds/<data>/`, con lo SHA-256 di ogni file, dove la data è quella del giorno (con una lettera se nello stesso giorno c'è già una riserva).
4. Agente: cartella `<data>-giro11` di Pokémon Moon con la copia di nome `main`, riletta dalla SD.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: scegli Pokémon Moon, Backup, nome `<data>-prima11`. È la partita com'è adesso, con i box vuoti. Non si rifà e non si cancella.
8. Proprietario: seleziona `<data>-giro11`, Restore, conferma.
9. Proprietario: avvia Luna senza salvare e controlla: box 1 posto 1 Poliwag livello 2, allenatore トレーナー; box 1 posto 12 Pikachu livello 12, allenatore ゲーフリ; box 1 posto 20 Clefable livello 24, allenatore アレッシオ; box 1 posto 23 Pikachu livello 12, allenatore アレッシオ; box 1 con i posti da 1 a 23 e gli altri box vuoti.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Moon, Backup, nome `<data>-rilett11`.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `<data>-rilett11/main` uguale a quello della copia.
14. Agente: giudizio della rilettura, 23 conformi negli stessi posti; `prima11` giudicata, con i box vuoti; `prima11` e `rilett11` nelle due riserve.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME, fuori dall'assistenza. Se qualcuno resta nei box, lascialo lì e dimmi box e posto, o mandami la foto del box.
17. Proprietario: HOME da 6200 a 6223, foto del totale; se ne mancano, foto del box di Luna con quelli rimasti. Se nel frattempo arrivano Meltan da GO, il totale cresce anche di quelli: dimmi quanti ne hai portati.
18. Agente: GIAPPONE2 «in HOME», pedigree; poi i giri sono finiti e si torna alle pendenze tenute in sospeso.

Punti 15-18 FATTI il 2026-11-13. HOME conta 6223, cioè 6200 più tutti i 23 esemplari, letto dalla foto del totale «All Pokémon» mandata dal proprietario; nessuno è rimasto nei box. GIAPPONE2 è «in HOME» in `tools/stampa-collezione.py`, pedigree e PDF rigenerati; `tools/sfide-bank.py` dà 47 sfide coperte su 47. I giri per HOME sono finiti: undici giri, 6197 esemplari portati, 6187 arrivati, i dieci rimasti spiegati posto per posto. I Meltan da GO il proprietario li porterà tutti insieme, con il loro pedigree in `ESEMPLARI-DA-GO.md`.

## Giro 12

Scritto il 2026-11-16 per ADR-126, ed è il primo dei due giri di sostituzione: porta in HOME i doni da carta di settima generazione, e quelli già in formato di settima, con la data di incontro dentro la finestra dell'evento. La copia è RIDATA2, `_notes/salvataggi/prove/per-home/ultraluna-ridata-2/main`, 568 esemplari, 445440 byte, SHA-256 `fc78be14e203130c9439dad49b8089764937fe47e7f6158dde60cb0ef3bb61d0`, giudicata 568 conformi (`_notes/lavoro/giudizi-copie/ridata-20261116b.json`): box da 1 a 18 pieni e box 19 posti da 1 a 28. Al posto 28 del box 19 c'è il Jirachi cromatico del disco bonus di Colosseum (WISHMKR, ID 20043), voluto dal proprietario il 2026-11-16 e prodotto da `tools/pkhex-jirachi-cromatico`; gli altri 567 sono identici alla prima versione della copia, `ultraluna-ridata-1`, superata. È la copia HOME10 con i box svuotati e riempiti con gli esemplari rigenerati da `tools/pkhex-ridata`, identici ai vecchi salvo la data; i 36 che vengono da HOME4, cioè da Luna, hanno anche l'allenatore di Ultraluna come detentore. HOME conta 6223 e dopo questo giro deve contarne 6791, perché i vecchi si liberano solo dopo (l'elenco da liberare di `python tools/elenco-da-liberare.py --stampa`).

Stato al 2026-11-16: punti 1-4 FATTI. `/3ds/Checkpoint/saves/` è copiata in `_notes/salvataggi/console/sd-checkpoint-20261116/` e in `J:/backup-sd-3ds/20261116/`, 46 file, ciascuna verificata con `sha256sum -c` contro l'elenco preso dalla SD (`sd-20261116.sha256` accanto a ciascuna), tutti uguali. `20261116-giro12/main` è nella cartella `0x01B51 Pokémon Ultra Moon` della SD, 445440 byte, riletta con SHA-256 `fc78be14…` uguale a RIDATA2. I nomi del giorno sono `20261116-prima12` e `20261116-rilett12`. Tocca al proprietario dal punto 5.

Stato al 2026-11-16, più tardi: punti 5-14 FATTI. Il proprietario ha fatto il Backup `20261116-prima12`, il Restore, i controlli del punto 9 e il Backup `20261116-rilett12`. Punto 13: `20261116-rilett12/main` ha SHA-256 `fc78be14…`, uguale a RIDATA2. Punto 14: giudizio in `_notes/lavoro/giudizi-copie/rilettura-passo2-giro12.json`, libreria 26.10.18: `rilett12` 568 esemplari, 568 conformi, negli stessi posti di RIDATA2 e con tutti i campi uguali a `ridata-20261116b.json`, impronte comprese, salvo `origine`; `prima12` (SHA-256 `5194cd9f…`) 0 esemplari nei box, come atteso. Riserve `_notes/salvataggi/console/sd-checkpoint-20261116b/` e `J:/backup-sd-3ds/20261116b/`, 49 file ciascuna, verificate con `sha256sum -c` contro l'elenco preso dalla SD (`sd-20261116b.sha256`), tutte uguali. Tocca al proprietario dal punto 15.

Punti 15-18 FATTI il 2026-11-16. HOME conta 6791, cioè 6223 più tutti i 568 esemplari, letto dalla foto del totale «All Pokémon» mandata dal proprietario; nessuno è rimasto nei box. RIDATA2 è «in HOME» in `tools/stampa-collezione.py`, pedigree e PDF rigenerati. I 567 vecchi che sostituisce restano in HOME fino alla fine del giro 13.

La partita che Ultraluna ha adesso è HOME10 dopo la banca del giro 10, con i box vuoti: è giusto che la riserva `prima12` del punto 7 sembri vuota.

1. Proprietario: spegni il 3DS del tutto.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo.
3. Agente: copia di `/3ds/Checkpoint/saves/` in `_notes/salvataggi/console/sd-checkpoint-<data>/` e in `J:/backup-sd-3ds/<data>/`, con lo SHA-256 di ogni file, dove la data è quella del giorno (con una lettera se nello stesso giorno c'è già una riserva).
4. Agente: cartella `<data>-giro12` di Pokémon Ultra Moon con la copia di nome `main`, riletta dalla SD.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: scegli Pokémon Ultra Moon, Backup, nome `<data>-prima12`. È la partita com'è adesso, prima del giro, con i box vuoti. Non si rifà e non si cancella.
8. Proprietario: seleziona `<data>-giro12`, Restore, conferma.
9. Proprietario: avvia Ultraluna senza salvare e controlla: box 1 posto 1 Magearna livello 50, allenatore Alessio; box 1 posto 30 Mienshao livello 65, allenatore フラダリ; box 19 posto 27 Jirachi livello 15, allenatore たなばた; box 19 posto 28 Jirachi cromatico livello 5, allenatore WISHMKR; box da 1 a 18 pieni, box 19 con i posti da 1 a 28.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Ultra Moon, Backup, nome `<data>-rilett12`.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `<data>-rilett12/main` uguale a quello della copia.
14. Agente: giudizio della rilettura, 568 conformi negli stessi posti; `prima12` giudicata, con i box vuoti; `prima12` e `rilett12` nelle due riserve.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME, fuori dall'assistenza. Se qualcuno resta nei box, lascialo lì e dimmi box e posto, o mandami la foto del box.
17. Proprietario: HOME da 6223 a 6791, foto del totale; se ne mancano, foto del box di Ultraluna con quelli rimasti. Non liberare ancora niente.
18. Agente: RIDATA2 «in HOME», pedigree; poi il giro 13.

## Giro 13

Scritto il 2026-11-16 per ADR-126, ed è il secondo giro di sostituzione: porta in HOME i 429 sostituti di sesta generazione che mancano, così che con i 567 del giro 12 ci siano tutti i 996 prima della liberazione, più il Jirachi cromatico di Pokémon Channel. Verde Foglia viene dopo, in un giro suo, per correzione del proprietario dello stesso giorno. La copia è RIDATA1, `_notes/salvataggi/prove/per-home/oras-ridata-2/main`, 430 esemplari, 483328 byte, SHA-256 `dd52356b39491577ec0b29635159e235f44830efe5839d425f8fe780085d9c8b`, giudicata 430 conformi (`_notes/lavoro/giudizi-copie/ridata-20261116b.json`): box da 1 a 14 pieni e box 15 posti da 1 a 10, con il Jirachi CHANNEL al posto 10. È la copia HOME9 con i box svuotati e riempiti con gli esemplari rigenerati. HOME conta 6791 e dopo questo giro deve contarne 7221.

La partita che Rubino Omega ha adesso è HOME9 dopo la banca del giro 6, con i sei Pikachu Cosplay nel box 16, posti da 24 a 29, che il gioco non lascia uscire: la riserva `prima13` del punto 7 li contiene, e il Restore del punto 8 li toglie dalla partita, come il giro 9 fece con i quattro totem. Restano nella riserva, nelle due copie del PC e nella copia HOME9.

Stato al 2026-11-16: punti 1-4 FATTI. `/3ds/Checkpoint/saves/` è copiata in `_notes/salvataggi/console/sd-checkpoint-20261116c/` e in `J:/backup-sd-3ds/20261116c/`, 49 file, ciascuna verificata con `sha256sum -c` contro l'elenco preso dalla SD (`sd-20261116c.sha256`), tutti uguali. `20261116-giro13/main` è nella cartella `0x011C4 Pokémon Omega Ruby` della SD, 483328 byte, riletta con SHA-256 `dd52356b…` uguale a RIDATA1. I nomi del giorno sono `20261116-prima13` e `20261116-rilett13`. Tocca al proprietario dal punto 5.

Stato al 2026-11-16, più tardi: punti 5-14 FATTI. Punto 13: `20261116-rilett13/main` ha SHA-256 `dd52356b…`, uguale a RIDATA1. Punto 14: giudizio in `_notes/lavoro/giudizi-copie/rilettura-passo2-giro13.json`, libreria 26.10.18: `rilett13` 430 esemplari, 430 conformi, negli stessi posti e con tutti i campi uguali a `ridata-20261116b.json`, impronte comprese, salvo `origine`; `prima13` (SHA-256 `e1d5941f…`) con i soli sei Pikachu Cosplay nel box 16, posti da 24 a 29, come atteso. Riserve `_notes/salvataggi/console/sd-checkpoint-20261116d/` e `J:/backup-sd-3ds/20261116d/`, 52 file ciascuna, verificate con `sha256sum -c` (`sd-20261116d.sha256`). Tocca al proprietario dal punto 15.

Punti 15-18 FATTI il 2026-11-16. HOME conta 7221, cioè 6791 più tutti i 430 esemplari, letto dalla foto del totale mandata dal proprietario. RIDATA1 è «in HOME» in `tools/stampa-collezione.py`, pedigree e PDF rigenerati; i sei Pikachu Cosplay di HOME9 hanno lo stato «fuori da HOME», nella riserva `prima13`. L'elenco da liberare è rigenerato con `--stampa` in `_notes/stampa/da-liberare/`, con i totali da 7221 a 6225: tutti i 996 sostituti sono in HOME e la liberazione può cominciare.

1. Proprietario: spegni il 3DS del tutto.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo.
3. Agente: copia di `/3ds/Checkpoint/saves/` nelle due riserve, con lo SHA-256 di ogni file.
4. Agente: cartella `<data>-giro13` di Pokémon Omega Ruby con la copia di nome `main`, riletta dalla SD.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: scegli Pokémon Omega Ruby, Backup, nome `<data>-prima13`. È la partita com'è adesso, con i sei Pikachu Cosplay nel box 16. Non si rifà e non si cancella.
8. Proprietario: seleziona `<data>-giro13`, Restore, conferma.
9. Proprietario: avvia Rubino Omega senza salvare e controlla: box 1 posto 1 Sylveon livello 10, allenatore XY; box 1 posto 30 Landorus livello 50, allenatore ヒャダイン; box 15 posto 9 Arceus livello 100, allenatore デセルシティ; box 15 posto 10 Jirachi cromatico livello 5, allenatore CHANNEL; box da 1 a 14 pieni, box 15 con i posti da 1 a 10, box 16 vuoto.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Omega Ruby, Backup, nome `<data>-rilett13`.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `<data>-rilett13/main` uguale a quello della copia.
14. Agente: giudizio della rilettura, 430 conformi negli stessi posti; `prima13` giudicata, con i sei Pikachu Cosplay; `prima13` e `rilett13` nelle due riserve.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME, fuori dall'assistenza. Se qualcuno resta nei box, lascialo lì e dimmi box e posto, o mandami la foto del box.
17. Proprietario: HOME da 6791 a 7221, foto del totale. Non liberare ancora niente.
18. Agente: RIDATA1 «in HOME», pedigree, e l'elenco da liberare con `python tools/elenco-da-liberare.py --stampa`; poi la liberazione dei 996, e dopo Verde Foglia.

## Giro 14

Scritto il 2026-11-17 per ADR-130 e ADR-131: i Pokémon veri della cartuccia di Diamante che PKHeX giudica conformi, senza i cloni dell'epoca e senza i dieci cromatici con lo stesso PID, più le squadre di Smeraldo e Rubino. Ogni esemplare ha la data di Poké Transfer di ADR-128, fra il 2011-03-04 e il 2013-12-31, scritta da `tools/pkhex-scrivi-salvataggio` con `--data-poke-transfer`; la data vera è nel pedigree, campo «data nel lotto». La copia è `_notes/salvataggi/prove/per-home/oras-diamante-1/main`, 245 esemplari, 483328 byte, SHA-256 `1cbdd79d09fdee560661f0a49a267db8ad40c863fdf748694a10074a80a47456`, giudicata 245 conformi (`_notes/lavoro/giudizi-copie/diamante-20261117.json`): box da 1 a 8 pieni e box 9 posti da 1 a 5. È la copia RIDATA1 con i box svuotati e riempiti, con `--svuota --regione-dal-salvataggio --includi-mn --data-poke-transfer`. Il passaggio alla banca e a HOME aggiunge 245 al totale di HOME: a liberazione finita 6470.

Stato al 2026-11-17: punti 1-4 FATTI. `/3ds/Checkpoint/saves/` è copiata in `_notes/salvataggi/console/sd-checkpoint-20261117a/` e in `J:/backup-sd-3ds/20261117a/`, 54 file, ciascuna verificata con `sha256sum -c` contro l'elenco preso dalla SD (`sd-20261117a.sha256`). `20261117-giro14/main` è nella cartella `0x011C4 Pokémon Omega Ruby` della SD, riletta con SHA-256 `1cbdd79d…` uguale alla copia; le due versioni precedenti della stessa cartella, con 244 e poi con 296 esemplari, sono state sostituite prima che il proprietario facesse il Restore. Tocca al proprietario dal punto 5.

Stato al 2026-11-17, più tardi: punti 5-14 FATTI. Punto 13: `20261117-rilett14/main` ha SHA-256 `1cbdd79d…`, uguale alla copia. Punto 14: giudizio in `_notes/lavoro/giudizi-copie/rilettura-passo2-giro14.json`: `rilett14` 245 esemplari, 245 conformi, stessi posti e stesse impronte di `diamante-20261117.json`; `prima14` (SHA-256 `52f52f01…`) con i box vuoti. Riserve `_notes/salvataggi/console/sd-checkpoint-20261117b/` e `J:/backup-sd-3ds/20261117b/`, 57 file ciascuna, verificate con `sha256sum -c` (`sd-20261117b.sha256`). Il proprietario ha deciso di non aspettare la fine della liberazione: il deposito Premium tiene 9000 esemplari (`COPIE-PER-HOME.md`), e 7221 più 245 fa 7466. L'elenco da liberare riconosce ogni esemplare per etichetta, specie, sesso, livello, allenatore e data, che i Pokémon di Diamante non condividono con nessuna voce; ai totali attesi dell'elenco si aggiungono 245. Tocca al proprietario dal punto 15.

Stato al 2026-11-17, sera: punti 15-18 FATTI. La banca ha dato due volte l'errore 006-0112, poi il passaggio è riuscito; il totale di HOME nella foto del proprietario è 7466, cioè 7221 più 245, quindi tutti i 245 sono arrivati e nessuno dei 996 era ancora stato liberato. DIAMANTE1 è «in HOME» in `tools/stampa-collezione.py`, pedigree e PDF rigenerati; l'elenco da liberare porta i totali da 7466 a 6470.

1. Proprietario: spegni il 3DS del tutto.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo.
3. Agente: copia di `/3ds/Checkpoint/saves/` nelle due riserve, con lo SHA-256 di ogni file.
4. Agente: cartella `<data>-giro14` di Pokémon Omega Ruby con la copia di nome `main`, riletta dalla SD.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: scegli Pokémon Omega Ruby, Backup, nome `<data>-prima14`. È la partita com'è adesso. Non si rifà e non si cancella.
8. Proprietario: seleziona `<data>-giro14`, Restore, conferma.
9. Proprietario: avvia Rubino Omega senza salvare e controlla: box 1 posto 1 Nidoran♂ livello 24, della squadra di Smeraldo; box 1 posto 30 Unown livello 25; box 9 posto 5 Nidoking livello 45; box da 1 a 8 pieni, box 9 con i posti da 1 a 5, box 10 vuoto.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Omega Ruby, Backup, nome `<data>-rilett14`.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `<data>-rilett14/main` uguale a quello della copia.
14. Agente: giudizio della rilettura, 245 conformi negli stessi posti; `prima14` giudicata; `prima14` e `rilett14` nelle due riserve.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME, fuori dall'assistenza, anche mentre la liberazione dei 996 è in corso. Se qualcuno resta nei box, lascialo lì e dimmi box e posto, o mandami la foto del box.
17. Proprietario: foto del totale di HOME, che è quello di prima più 245: 7466 se non hai ancora liberato niente, 6470 a liberazione finita.
18. Agente: la copia «in HOME» in `tools/stampa-collezione.py`, pedigree e stampabile (ADR-111, ADR-127).

## Giro 15

Scritto il 2026-11-24 per ADR-140: i Pokémon veri della cartuccia di Verde Foglia, estratta il 2026-11-24 con due letture identiche (`RUNBOOK-ESTRAZIONI.md`), che PKHeX giudica conformi, senza i 7 contestati di Smeraldo e senza i 21 identici a un esemplare già in HOME (`_notes/lotti/lotto-verde-foglia/identita-gia-in-home.json`). Prima la squadra, con PUCCETTO al primo posto, poi i box. Ogni esemplare ha la data di Poké Transfer di ADR-128, fra il 2011-03-04 e il 2013-12-31. La copia è `_notes/salvataggi/prove/per-home/oras-verde-foglia-1/main`, 359 esemplari, 483328 byte, SHA-256 `d64212320cfde2ce0a673eb1f5d5ceaeff029d9c7008b6df49ab39849ee82091`, giudicata 359 conformi (`_notes/lavoro/giudizi-copie/verde-foglia-20261124.json`): box da 1 a 11 pieni e box 12 posti da 1 a 29. È la copia del giro 14 con i box svuotati e riempiti, con `--svuota --regione-dal-salvataggio --includi-mn --data-poke-transfer`.

Stato al 2026-11-24: punti 1-4 FATTI. `/3ds/Checkpoint/saves/` è copiata in `_notes/salvataggi/console/sd-checkpoint-20261124/` e in `J:/backup-sd-3ds/20261124/`, 57 file, ciascuna verificata con `sha256sum -c` contro l'elenco preso dalla SD (`sd-20261124.sha256`). `20261124-giro15/main` è nella cartella `0x011C4 Pokémon Omega Ruby` della SD, riletta con SHA-256 `d6421232…` uguale alla copia. Tocca al proprietario dal punto 5.

Stato al 2026-11-24, più tardi: punti 5-14 FATTI. Punto 9: foto del proprietario di PUCCETTO livello 100, Dragonite livello 74 e Deoxys livello 100, e un video dei box; le icone a Poké Ball del video sono i segnaposto che il gioco mostra mentre carica il box, e i fotogrammi successivi mostrano gli stessi box pieni. Punto 13: `20261124-rilett15/main` ha SHA-256 `d6421232…`, uguale alla copia. Punto 14: giudizio in `_notes/lavoro/giudizi-copie/rilettura-passo2-giro15.json`: `rilett15` 359 esemplari, 359 conformi, stessi posti e stessi PID di `verde-foglia-20261124.json`; `prima15` (SHA-256 `64dcd74a…`) con i box vuoti. `prima15` e `rilett15` sono nelle due riserve `sd-checkpoint-20261124` e `J:/backup-sd-3ds/20261124/`, con l'impronta controllata. Foto e video in `_notes/fonti/consegne/2026-11-24-giro15-console/`, originali di Telegram cancellati. Tocca al proprietario dal punto 15.

Stato al 2026-11-24, sera: punti 15-18 FATTI. Il totale di HOME riferito dal proprietario è 7825, cioè 7466 più 359, con i 996 non ancora liberati: tutti i 359 sono arrivati. Giudizio complessivo `_notes/lavoro/giudizi-copie/dopo-20261124-verdefoglia.json`, 17 gruppi, i 16 di prima identici a `dopo-20261120-date-vc.json`; VERDEFOGLIA1 «in HOME» in `tools/stampa-collezione.py`, con l'allenatore della cartuccia coperto da segnaposto nel pedigree tracciato e le storie in `_notes/lotti/lotto-verde-foglia/storie.json`; pedigree `pokedex-home-completo/pedigree/VERDEFOGLIA1.md`, catalogo di HOME a 6793 esemplari; l'elenco da liberare parte ora da 7825 e arriva a 6829.

1. Proprietario: spegni il 3DS del tutto.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo.
3. Agente: copia di `/3ds/Checkpoint/saves/` nelle due riserve, con lo SHA-256 di ogni file.
4. Agente: cartella `20261124-giro15` di Pokémon Omega Ruby con la copia di nome `main`, riletta dalla SD.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: scegli Pokémon Omega Ruby, Backup, nome `20261124-prima15`. È la partita com'è adesso. Non si rifà e non si cancella.
8. Proprietario: seleziona `20261124-giro15`, Restore, conferma.
9. Proprietario: avvia Rubino Omega senza salvare e controlla: box 1 posto 1 Blastoise livello 100, PUCCETTO; box 1 posto 2 Dragonite livello 74; box 12 posto 29 Deoxys livello 100; box da 1 a 11 pieni, box 12 con i posti da 1 a 29, box 13 vuoto.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Omega Ruby, Backup, nome `20261124-rilett15`.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `20261124-rilett15/main` uguale a quello della copia.
14. Agente: giudizio della rilettura, 359 conformi negli stessi posti; `prima15` giudicata; `prima15` e `rilett15` nelle due riserve.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME. Se qualcuno resta nei box, lascialo lì e dimmi box e posto, o mandami la foto del box.
17. Proprietario: foto del totale di HOME, che è quello di prima più 359.
18. Agente: la copia «in HOME» in `tools/stampa-collezione.py`, pedigree e stampabile (ADR-111, ADR-127).

## Giro 16

Scritto il 2026-11-25 per ADR-140 e ADR-141: i Pokémon veri della cartuccia di Zaffiro, estratta il 2026-11-25 con due letture identiche (`RUNBOOK-ESTRAZIONI.md`), tutti conformi per PKHeX (63 nei box, 6 in squadra), senza i 4 identici a un esemplare già in HOME (Lapras, Mewtwo, Zangoose e Suicune 10ANNI, tutti in HOME6) e senza il Tropius che conosce solo mosse MN, escluso dopo la conversione come i Floatzel di ADR-131; più tre esemplari della cartuccia di Smeraldo rimasti fuori da HOME, il Seedot dello sciame del box 1 posto 17, il Wurmple del box 5 posto 15 e il Wynaut dell'Isola Miraggio del box 13 posto 28, estratti dalla rilettura del 2026-11-20. Lo Sceptile della squadra porta il Training Ribbon con il Super Allenamento completo, scritto da `tools/pkhex-fiocco-allenamento` (ADR-141). Prima la squadra, poi i box, poi i tre di Smeraldo. Ogni esemplare ha la data di Poké Transfer di ADR-128, fra il 2011-03-04 e il 2013-12-31. La copia è `_notes/salvataggi/prove/per-home/oras-zaffiro-1/main`, sulla copia del giro 15 svuotata, 67 esemplari, 483328 byte, SHA-256 `e1f70f1e98335961aed21bd89d9127a9513498ffcd044d3be0fda772781e945f`, giudicata 67 conformi (`_notes/lavoro/giudizi-copie/zaffiro-giro16-20261125.json`): box 1 e 2 pieni e box 3 posti da 1 a 7.

Stato al 2026-11-25: punti 1-4 FATTI. `/3ds/Checkpoint/saves/` è copiata in `_notes/salvataggi/console/sd-checkpoint-20261125/` e in `J:/backup-sd-3ds/20261125/`, 60 file, ciascuna verificata con `sha256sum -c` contro l'elenco preso dalla SD (`sd-20261125.sha256`). `20261125-giro16/main` è nella cartella `0x011C4 Pokémon Omega Ruby` della SD, riletta con SHA-256 `e1f70f1e…` uguale alla copia. Tocca al proprietario dal punto 5.

Stato al 2026-11-25, più tardi: punti 5-14 FATTI. Punto 13: `20261125-rilett16/main` ha SHA-256 `e1f70f1e…`, uguale alla copia. Punto 14: giudizio in `_notes/lavoro/giudizi-copie/rilettura-passo2-giro16.json`: `rilett16` 67 esemplari, 67 conformi, stessi posti e stessi PID di `zaffiro-giro16-20261125.json`, Sceptile con RibbonChampionG3 e RibbonTraining; `prima16` (SHA-256 `10de6a52…`) con i box vuoti. `prima16` e `rilett16` sono nelle due riserve `sd-checkpoint-20261125` e `J:/backup-sd-3ds/20261125/`. Tocca al proprietario dal punto 15.

1. Proprietario: spegni il 3DS del tutto.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo.
3. Agente: copia di `/3ds/Checkpoint/saves/` nelle due riserve, con lo SHA-256 di ogni file.
4. Agente: cartella `20261125-giro16` di Pokémon Omega Ruby con la copia di nome `main`, riletta dalla SD.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: scegli Pokémon Omega Ruby, Backup, nome `20261125-prima16`. È la partita com'è adesso. Non si rifà e non si cancella.
8. Proprietario: seleziona `20261125-giro16`, Restore, conferma.
9. Proprietario: avvia Rubino Omega senza salvare e controlla: box 1 posto 1 Dragonite livello 55; box 1 posto 6 Sceptile livello 51, che nei fiocchi ha il Training Ribbon; box 3 posto 7 Wynaut livello 30; box 1 e 2 pieni, box 3 con i posti da 1 a 7, box 4 vuoto.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Omega Ruby, Backup, nome `20261125-rilett16`.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `20261125-rilett16/main` uguale a quello della copia.
14. Agente: giudizio della rilettura, 67 conformi negli stessi posti; `prima16` giudicata; `prima16` e `rilett16` nelle due riserve.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME. Se qualcuno resta nei box, lascialo lì e dimmi box e posto, o mandami la foto del box.
17. Proprietario: foto del totale di HOME, che è quello di prima più 67.
18. Agente: la copia «in HOME» in `tools/stampa-collezione.py`, pedigree e stampabile (ADR-111, ADR-127).

Stato dei punti 15-18, al 2026-11-25: fatti. Il proprietario ha passato i 67 a Bank e a HOME, nessuno è rimasto nei box, e la foto del totale dice 7892, cioè 7825 più 67; lo Sceptile in HOME mostra il Training Ribbon. Punto 18: giudizio `dopo-20261125-zaffiro.json`, ZAFFIRO1 «in HOME», pedigree `pedigree/ZAFFIRO1.md`, catalogo ricomposto, elenco da liberare con i totali da 7892 a 6896.

## Giro 17

Scritto il 2026-11-26 per ADR-142, ADR-143 e ADR-144: l'ultimo giro che deve passare da Bank prima della chiusura del 2027-02-26, misurato da `CONTROLLO-PRIMA-DI-BANK.md`. Porta 310 varianti d'allenatore dei doni di terza generazione dei Pokémon Center giapponesi e di New York (`pkhex-produci-elenco --varianti-gen3 --produci`, lotto `_notes/lotti/lotto-varianti-gen3/`), cioè lo stesso dono con il nome di ogni città o di ogni macchina, e 352 Pokémon per le sfide dell'app di HOME (`tools/pkhex-sfide-app`, lotto `_notes/lotti/lotto-sfide-app/`): 314 catture di Ultraluna e Ultrasole in 17 sfere, 23 Ditto compresi, 28 della Gara Pigliamosche di HeartGold con la Gara Ball e dieci catture di Smeraldo con le cinque condizioni e la lucentezza a 255. In fondo, tre Pokémon del Daisuki Club rifatti (`_notes/lotti/lotto-daisuki-club-c/`, ADR-144): il Magikarp, l'Heracross e il Cherubi dello staff ウッツー, che in HOME portano l'allenatore scritto «ウッツ?» perché la fonte trascrive con un trattino largo che la quarta generazione non conosce; le date di cattura e d'uovo sono quelle degli scambi GTS dello staff, del 2006 e del 2007. I Pokémon di terza e quarta generazione hanno la data di Poké Transfer di ADR-128, fra il 2011-03-04 e il 2013-12-31. I tre vecchi «ウッツ?» (HOME9 box 19 posti 6, 11 e 22) si liberano dopo che i nuovi sono in HOME. Quattro Salamence di New York conoscono una mossa MN ed entrano con `--includi-mn`, come nei giri 2, 5 e 6. La copia è `_notes/salvataggi/prove/per-home/ultraluna-giro-17/main`, sulla copia del giro 12 (`ultraluna-ridata-2`) svuotata, con `--svuota --regione-dal-salvataggio --includi-mn --data-poke-transfer`: 665 Pokémon, 445440 byte, SHA-256 `0d5f5388f6736aca51df23a97c722ee6672159d83e07ab536cb4a15f178251c1`, riletti senza differenze e giudicati 665 conformi, nessun cromatico (`_notes/lavoro/giudizi-copie/giro17-20261126.json`). Box da 1 a 22 pieni e box 23 posti da 1 a 5. La partita che Ultraluna ha adesso è quella del giro 12 dopo il passaggio alla banca, con i box vuoti: è giusto che la riserva `prima17` del punto 7 sembri vuota.

1. Proprietario: spegni il 3DS del tutto.
2. Proprietario: SD nel PC, lettera `I:`, e dimmelo.
3. Agente: copia di `/3ds/Checkpoint/saves/` nelle due riserve, con lo SHA-256 di ogni file.
4. Agente: cartella `20261126-giro17` di Pokémon Ultra Moon con la copia di nome `main`, riletta dalla SD.
5. Proprietario: espelli la SD e rimettila nel 3DS.
6. Proprietario: avvia Checkpoint.
7. Proprietario: scegli Pokémon Ultra Moon, Backup, nome `20261126-prima17`. È la partita com'è adesso. Non si rifà e non si cancella.
8. Proprietario: seleziona `20261126-giro17`, Restore, conferma.
9. Proprietario: avvia Ultraluna senza salvare e controlla: box 1 posto 1 Treecko livello 10, allenatore トウキョー; box 11 posto 11 Feebas livello 20 in una Minor Ball; box 23 posto 2 Jynx livello 9 in una UC Ball; box 23 posto 3 Magikarp livello 5, allenatore ウッツー; box da 1 a 22 pieni, box 23 con i posti da 1 a 5, box 24 vuoto.
10. Proprietario: esci senza salvare.
11. Proprietario: Checkpoint, Pokémon Ultra Moon, Backup, nome `20261126-rilett17`.
12. Proprietario: spegni, SD nel PC, e dimmelo.
13. Agente: SHA-256 di `20261126-rilett17/main` uguale a quello della copia.
14. Agente: giudizio della rilettura, 665 conformi negli stessi posti; `prima17` giudicata; `prima17` e `rilett17` nelle due riserve.
15. Proprietario: SD nel 3DS.
16. Proprietario: il passaggio alla banca e a HOME. Se qualcuno resta nei box, lascialo lì e dimmi box e posto, o mandami la foto del box.
17. Proprietario: foto del totale di HOME, che è quello di prima più 665, e foto delle sfide dell'app delle sfere, delle condizioni, della lucentezza e dei Ditto.
18. Agente: la copia «in HOME» in `tools/stampa-collezione.py`, pedigree e stampabile, che da lì si chiude (ADR-111, ADR-127, ADR-142); i tre vecchi «ウッツ?» nell'elenco da liberare (ADR-144).

Stato al 2026-11-26: punti 1-14 FATTI. Riserve della SD in `sd-checkpoint-20261126` e `J:/backup-sd-3ds/20261126/`. Punto 13: `20261126-rilett17/main` ha SHA-256 `0d5f5388…`, uguale alla copia. Punto 14: giudizio in `_notes/lavoro/giudizi-copie/rilettura-passo2-giro17.json`: `rilett17` 665 esemplari, 665 conformi, nessun cromatico, stessi posti, PID, specie, allenatori e sfere di `giro17-20261126.json`; `prima17` (SHA-256 `e40ff019…`) con i box vuoti. `prima17` e `rilett17` sono nelle due riserve. Punti 15-17 FATTI dal proprietario lo stesso giorno: HOME a 8557 (foto), le sfide delle sfere, delle condizioni, della lucentezza e dei Ditto d'oro; foto in `_notes/fonti/consegne/2026-11-26-home-giro17-e-scambi/`. Punto 18 FATTO: giudizio `dopo-20261126-giro17.json` (19 gruppi, i 18 di prima identici, GIRO17 665 conformi), GIRO17 «in HOME», pedigree `GIRO17.md`, catalogo di 7525 esemplari, elenco da liberare a 999 voci (996 più i tre «ウッツ?»), da 8557 a 7558.

## Dopo il giro 4

La partita vera di Rubino Omega, `20260821-backsic`, resta fuori dalla console fino al passo 6. I giri successivi sono nella tabella in testa a `ROADMAP.md`: il 5 (HOME8, `oras-giro-5-carte-mn5`, 256) e il 6 (HOME9, `oras-giro-6-statici-eventi-4`, 695, di cui 689 in HOME e i sei Pikachu Cosplay rimasti in Rubino Omega) sono ancora di Rubino Omega e seguono questa procedura con i nomi del giorno; dal 7 si passa a Luna e Ultraluna, e al giro 8, il primo di Ultraluna, la copia di riserva di Checkpoint crea la cartella del gioco.
