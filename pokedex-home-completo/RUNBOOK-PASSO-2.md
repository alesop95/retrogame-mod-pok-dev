# Passo 2: i giri 2 e 3 di Rubino Omega, 721 e 915 esemplari

> Documento autorato, scritto il 2026-11-04 su richiesta del proprietario, nella stessa forma di `RUNBOOK-PASSO-1.md`, che resta il riferimento per il perché di ogni punto. Applica `rules/hardware-and-perimeter.md`: prima di ogni scrittura sulla console una copia di riserva in due copie su due percorsi distinti e verificata, e dopo ogni scrittura una rilettura confrontata sui byte. I passi segnati «agente» li esegue l'agente, con la scheda SD inserita nel PC. Il tratto da Pokémon Bank in poi resta del proprietario e fuori dall'assistenza, come dice la stessa regola: questo documento si ferma prima della banca e riprende con la verifica in HOME. I due giri si fanno uno dopo l'altro, e il secondo comincia solo quando il primo è registrato in HOME.

## Che cosa si porta e in che stato è

Le due copie sono di Rubino Omega (versione OR), pesano 483.328 byte ciascuna e sono giudicate tutte conformi il 2026-11-04 con la libreria 26.10.18 nel contesto del salvataggio, in `_notes/lavoro/giudizi-copie/dopo-bfe89c7-pedigree.json`; il pedigree di ogni esemplare sta in `pokedex-home-completo/pedigree/HOME2.md` e `HOME3.md` e nei PDF di `_notes/stampa/pedigree/`.

| Giro | Copia | Esemplari | Box | SHA-256, inizio | Controllo a vista |
|---|---|---|---|---|---|
| 2 | `_notes/salvataggi/prove/per-home/oras-giro-2-mn-fin2/main` | 721 | da 1 a 24 pieni, box 25 con il solo posto 1 | `425e6045ee34e638` | box 1 posto 1 Pikachu livello 100, allenatore SMR2012; box 1 posto 2 Genesect livello 15, allenatore Plasma; box 25 posto 1 Suicune livello 40, allenatore Alessio |
| 3 | `_notes/salvataggi/prove/per-home/oras-giro-3-fin3/main` | 915 | da 1 a 30 pieni, box 31 con i posti da 1 a 15 | `4662a6a66ad07063` | box 1 posto 1 Garchomp livello 48, allenatore XY; box 1 posto 2 Pikachu livello 10, allenatore Satay King; box 31 posto 15 Manaphy livello 1, allenatore Alessio |

Sulla console Rubino Omega porta oggi ciò che è rimasto del giro 1 dopo il passaggio alla banca. La partita vera del proprietario, `20260821-backsic`, non si tocca e torna sulla console soltanto al passo 6. HOME mostrava 964 esemplari dopo il giro 1: dopo il giro 2 deve mostrarne 1685, dopo il giro 3 2600.

## Giro 2

Stato al 2026-11-04: punti da 1 a 15 FATTI. La copia `20261104-giro2` è stata scritta sulla SD e riletta identica; il proprietario ha fatto i punti da 5 a 12 con i controlli del punto 9 tutti giusti e le fotografie delle tre schede, uguali campo per campo al pedigree; la rilettura `20261104-rilett2` è identica alla copia (`425e6045ee34e638`), 721 Pokémon, 721 conformi, nessuna differenza di box, posto o impronta (`_notes/lavoro/giudizi-copie/rilettura-passo2-giro2.json`); rilettura e riserva `20261104-prima2` sono in `_notes/salvataggi/console/sd-checkpoint-2026-11-04/` e in `J:/backup-sd-3ds/2026-11-04/`. Resta al proprietario il punto 16, il passaggio a Bank e a HOME, e il punto 17, il controllo del totale in HOME, che deve passare da 964 a 1685.

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

Si ripetono i punti da 1 a 18 con questi cambi, e nient'altro.

- Punto 3: la cartella di riserva ha la data del giorno del giro 3, e comprende la copia di riserva `<data>-prima2` e la rilettura del giro 2.
- Punto 4: la cartella sulla SD si chiama `<data>-giro3` e contiene la copia del giro 3; l'impronta deve cominciare con `4662a6a66ad07063`.
- Punto 7: la copia di riserva si chiama `<data>-prima3`.
- Punto 8: si ripristina `<data>-giro3`.
- Punto 9: box 1 posto 1 Garchomp livello 48, box 1 posto 2 Pikachu livello 10, box 31 posto 15 Manaphy livello 1; i box da 1 a 30 pieni, il box 31 con i posti da 1 a 15.
- Punto 11: la rilettura si chiama `<data>-rilett3`.
- Punto 14: devono risultare 915 esemplari, 915 conformi.
- Punto 17: il totale di HOME deve passare da 1685 a 2600. Il primo box nuovo comincia con Garchomp livello 48, allenatore XY, e Pikachu livello 10, allenatore Satay King; l'ultimo finisce al posto 15 con Manaphy livello 1, allenatore Alessio.
- Punto 18: il gruppo HOME3 passa a «in HOME».

## Dopo il passo 2

La partita vera di Rubino Omega, `20260821-backsic`, resta fuori dalla console fino al passo 6. Il passo 3 sono i giri di Luna e di Ultraluna, `luna-giro-1-fin`, 93 esemplari, e `ultraluna-giro-1-scambi-fin2`, 613, e avrà il suo documento quando il passo 2 sarà registrato.
