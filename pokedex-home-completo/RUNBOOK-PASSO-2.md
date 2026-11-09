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

Scritto il 2026-11-09 su richiesta del proprietario, con gli stessi passaggi del giro 3 e i nomi già pronti. La copia è HOME6, `_notes/salvataggi/prove/per-home/oras-giro-4-fin9/main`, 929 esemplari, SHA-256 che comincia con `54fba3a32cd4f48d`, giudicata 929 conformi con la libreria 26.10.18 (`_notes/lavoro/giudizi-copie/dopo-adr120.json`). Il giro 3 è registrato: HOME mostra 2600, e dopo questo giro i posti occupati attesi sono 3529 su 9000. Stato al 2026-11-09: punti da 1 a 14 FATTI (dal 5 al 12 dal proprietario, il 13 e il 14 dall'agente con la SD di nuovo in `I:`); tocca al proprietario dal punto 15. Se durante il passaggio Luma3DS mostra di nuovo un'eccezione nel processo `mint`, è l'applet eShop di sistema e non i dati della copia (ADR-120): si spegne, si riaccende e si riprende dal punto 16, senza ripristinare niente.

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

16. Proprietario: il passaggio dalla console a Pokémon Bank, il controllo in banca e il passaggio a Pokémon HOME sono tuoi, e l'assistenza non li copre. Se la banca o HOME rifiutano o segnalano un Pokémon, fermati e non ripetere: dimmi quale e con quale messaggio, e lo confronto con il giudizio di PKHeX.
17. Proprietario, in HOME, dall'app per Switch o per telefono, senza spostare nulla: il totale del deposito deve passare da 2600 a 3529. Fotografa il totale e tre schede a caso, con la schermata dei dati e quella delle note dell'allenatore. Se un Pokémon mostra un'icona o un messaggio insolito, fotografa la schermata e dimmi box e posto.
18. Agente: registro l'esito in `COPIE-PER-HOME.md` e nel pedigree, dove il gruppo HOME6 passa da «pronta» a «in HOME». Poi il giro 5, HOME8, con la stessa procedura.

## Dopo il giro 4

La partita vera di Rubino Omega, `20260821-backsic`, resta fuori dalla console fino al passo 6. I giri successivi sono nella tabella in testa a `ROADMAP.md`: il 5 (HOME8, `oras-giro-5-carte-mn5`, 256) e il 6 (HOME9, `oras-giro-6-statici-eventi-3`, 694) sono ancora di Rubino Omega e seguono questa procedura con i nomi del giorno; dal 7 si passa a Luna e Ultraluna, e al giro 8, il primo di Ultraluna, la copia di riserva di Checkpoint crea la cartella del gioco.
