# Runbook delle estrazioni di Verde Foglia e Diamante

Scritto il 2026-11-17 su richiesta del proprietario, che vuole ogni passo esplicito perché le due cartucce sono le sue originali. Le due estrazioni sono di sola lettura: non scrivono niente sulla cartuccia. Valgono `.claude/rules/hardware-and-perimeter.md` (doppia copia su due dischi, due letture confrontate sui byte) e la sequenza di inserimento di `cart-battery-restoration/STUDIO-01-batteria-e-ritenzione.md`, sezioni 5 e 6.

## Le fonti dei nomi dei pulsanti

FlashGBX: il sorgente dell'interfaccia, `FlashGBX/FlashGBX_GUI.py` del ramo principale letto il 2026-11-17. Il riquadro «Functions» ha i pulsanti di piattaforma «Game Boy» e «Game Boy Advance», «Refresh», «Backup ROM», «Backup Save Data», «Write ROM» e «Write Save Data»; il menu di quest'ultimo contiene «Restore from save data file» ed «Erase cartridge save data». La verifica dei dati trasferiti è attiva di serie (impostazione «Verify transferred data»). Le stesse etichette, e la verifica attiva di serie, sono nella versione installata, la 5.1 in `C:/Users/Utente/AppData/Local/Programs/FlashGBX`, ricontrollate il 2026-11-17. La 5.2.1 del 2026-11-01 non si installa prima di questa estrazione: porta il firmware L16 del lettore, cambia la temporizzazione di lettura della ROM e la scrittura dei salvataggi flash del Game Boy Advance, e segue di un giorno la 5.2 ritirata; la 5.1 ha già letto e scritto Smeraldo e Rubino con riletture identiche. Il LED «Mode» del lettore è blu in Game Boy Advance (3,3 V) e rosso in Game Boy (5 V), misurato dal proprietario il 2026-09-15. Checkpoint per la cartuccia DS: il tutorial di Project Pokémon `using-checkpoint-r70` e ConsoleMods (`SOURCES.md`).

## Verde Foglia, con GBxCart RW e FlashGBX

Stato del 2026-11-17: FlashGBX 5.1 avviato e collegato, lettore GBxCart RW v1.4 con firmware R42+L14, «Game Boy Advance» selezionato, cartuccia ancora fuori dal lettore; il proprietario ha rifiutato l'aggiornamento proposto. Il riquadro di sinistra dice «No cartridge connected» perché la cartuccia non è inserita, ed è giusto così. Il proprietario ha chiesto un gesto per passo, in ordine: per questo i passi sono atomici.

Pulsanti che non si toccano mai: «Write Save Data», «Write ROM», «Analyze Flash Cart», che serve alle cartucce riscrivibili e non alle originali, le voci «Restore from save data file» ed «Erase cartridge save data», «Game Boy» mentre la cartuccia è inserita. Se FlashGBX chiede di aggiornare il programma o il firmware del lettore, si risponde sempre No (ADR-129). FlashGBX non ricorda la modalità fra una connessione e l'altra (misurato il 2026-09-15, `sub-smeraldo-save-fix.md`, e di nuovo il 2026-11-17): dopo ogni ricollegamento la riga di stato torna a «Please select Platform Mode» e «Game Boy Advance» si riseleziona a mano.

Prima parte, con la cartuccia fuori dal lettore.

1. Verde Foglia resta fuori dal lettore, sul tavolo.
2. Collega il GBxCart al PC con il cavo USB e apri FlashGBX.
3. FlashGBX si collega da solo: in basso a destra il pulsante dice «Disconnect». Se dice «Connect», premilo.
4. Clicca «Game Boy Advance», mai «Game Boy».
5. Guarda il LED «Mode» sul lettore: deve essere blu. Se è rosso, clicca di nuovo «Game Boy Advance» e riguarda; se resta rosso, fermati e avvisa l'agente.

Seconda parte, l'inserimento, sempre a cavo staccato.

6. Clicca «Disconnect».
7. Stacca il cavo USB dal lettore.
8. Inserisci Verde Foglia nella fessura per Game Boy Advance, dritta e fino in fondo, senza forzare, come per Smeraldo.

Terza parte, la lettura delle informazioni.

9. Ricollega il cavo USB al lettore.
10. Se in basso a destra il pulsante dice «Connect», premilo.
11. Clicca «Game Boy Advance», mai «Game Boy»: la modalità va riselezionata.
12. Guarda il LED «Mode»: deve essere blu. Se è rosso, non cliccare niente: stacca il cavo, togli la cartuccia e avvisa l'agente.
13. Clicca «Refresh». Legge soltanto, non scrive niente.
14. Controlla il riquadro di sinistra. Si aspetta: titolo di Verde Foglia (atteso «POKEMON LEAF», codice che finisce per I, la versione italiana), «Boot Logo» e «Header Checksum» non più in rosso, «Save Type» di tipo FLASH da 1 Mbit cioè 128 KiB, rilevato da solo come per Rubino e Smeraldo, «Real Time Clock» non disponibile. I menu «ROM Size», «Save Type» e «Profile» non si toccano a mano.
15. Fotografa la finestra e mandala all'agente, e aspetta il suo via prima del backup. Se dice ancora «No cartridge connected», oppure se il titolo è fatto di simboli senza senso e «Header Checksum» è «Invalid (0x00)», com'era il 2026-11-17 al primo inserimento («ROM Title» «/p{{{{», nessuna voce di database), i contatti non toccano bene: «Disconnect», stacca il cavo, togli la cartuccia, reinseriscila con decisione e riparti dal passo 9. Una lettura sbagliata non danneggia niente, perché legge soltanto, e il salvataggio di Verde Foglia sta in una memoria flash che non dipende dalla pila, quindi togliere e rimettere la cartuccia non lo tocca. Se il problema resta, non si insiste sulla stessa cartuccia: il 2026-11-17 sei letture dell'intestazione di Verde Foglia (riga di comando di FlashGBX, `--cli --debug --mode agb --action info`, sola lettura) erano tutte diverse e quasi tutte 0xFF, cioè nessun contatto. Le due prove che separano le cause sono l'avvio della cartuccia sul DS fino a «CONTINUA», senza salvare, e la lettura di Smeraldo nello stesso lettore; poi, se il lettore è sano, la pulizia dei contatti con alcol isopropilico, che è anche il primo rimedio del README di FlashGBX (sezione Troubleshooting: connessione instabile della cartuccia come causa più comune, poi altre porte USB e altri cavi). Verde Foglia si avvia sul Game Boy Advance SP (misura del proprietario, 2026-11-17).

Quarta parte, il backup, dopo il via dell'agente.

16. Clicca «Backup Save Data». Nella finestra di salvataggio vai in `E:\retrogame-mod-pok-dev\_notes\salvataggi\cartucce\verde-foglia\01-20261116-estrazione\`, scrivi il nome `lettura1.sav` e premi Salva. Aspetta che «Transfer Status» dica che ha finito, senza toccare cavo e cartuccia.
17. Clicca di nuovo «Backup Save Data» e salva nella stessa cartella come `lettura2.sav`, aspettando come prima.
18. Clicca «Disconnect».
19. Stacca il cavo USB.
20. Solo adesso togli la cartuccia.
21. Agente: controlla che i due file siano di 131072 byte e identici byte per byte, legge allenatore e Pokémon con PKHeX, li rinomina con allenatore, ID, ore di gioco e data, e li copia su J: con la verifica dello SHA-256.

## Smeraldo come cartuccia di riferimento, 2026-11-18

Il proprietario ha portato Smeraldo il 2026-11-18. Serve a una domanda sola: se il lettore legge una cartuccia GBA che sappiamo sana, il guasto di Verde Foglia sta nel suo contatto, e la pulizia con l'alcol del 2026-11-21 è il passo giusto; se non legge nemmeno Smeraldo, il guasto sta nel lettore o nel suo connettore, e Verde Foglia non si tocca. Tutta la prima e la seconda parte sono di sola lettura. Valgono gli stessi pulsanti da non toccare della sezione di Verde Foglia.

Prima parte, la prova del lettore, con la riga di comando dell'agente.

1. In FlashGBX clicca «Disconnect», poi chiudi la finestra di FlashGBX: la porta del lettore deve restare libera per lo script dell'agente.
2. Stacca il cavo USB dal lettore.
3. Inserisci Smeraldo nella fessura per Game Boy Advance, dritta e fino in fondo, nello stesso verso di Verde Foglia.
4. Ricollega il cavo USB al lettore, nella stessa porta del PC usata per Verde Foglia.
5. Scrivi all'agente «inserita» e non toccare niente.
6. Agente: lancia lo script di sola lettura usato per Verde Foglia il 2026-11-17 (`SetMode("AGB")` e `ReadROM(0, 0x180)` con i tre metodi di lettura, due volte ciascuno, con il Python e la libreria di FlashGBX 5.1 installata), che non legge né scrive il salvataggio. Esito atteso se il lettore è sano: sei letture identiche, titolo «POKEMON EMER», codice «BPEI», logo corretto. Esito del 2026-11-18, cavo nella porta frontale sinistra del PC: sei letture identiche con «POKEMON EMER», «BPEI» e logo corretto, quindi il lettore è sano e il guasto di Verde Foglia sta nel suo contatto.

Seconda parte, la copia di riserva di Smeraldo, solo se la prima parte è andata bene e dopo il via dell'agente. Serve comunque prima di qualunque scrittura futura su Smeraldo, perché l'ultima rilettura della cartuccia è del 2026-09-23.

7. Apri FlashGBX, clicca «Game Boy Advance» e controlla che il LED «Mode» sia blu.
8. Clicca «Refresh» e controlla che a sinistra compaia Pokémon Smeraldo con «Save Type» FLASH da 1 Mbit.
9. Clicca «Backup Save Data», vai in `E:\retrogame-mod-pok-dev\_notes\salvataggi\cartucce\smeraldo\07-20261118-estrazione\`, scrivi `lettura1.sav` e premi Salva. Aspetta la fine del trasferimento.
10. Di nuovo «Backup Save Data», stessa cartella, `lettura2.sav`.
11. «Disconnect», stacca il cavo, solo adesso togli la cartuccia.
12. Agente: controlla che i due file siano di 131072 byte e identici, li rinomina con lo schema di ADR-064 e li copia su J: con lo SHA-256.

Esito della seconda parte, 2026-11-18: due letture identiche di 131072 byte (SHA-256 che comincia per `b1117124`), rinominate per esteso con allenatore, ID, ore di gioco, data e «lettura 1 di 2» e «lettura 2 di 2, copia della cartuccia prima della scrittura», copiate su J: in `backup salvataggi pokèmon/smeraldo-07-20261118-estrazione/` con lo stesso SHA-256. Rispetto alla rilettura del 2026-09-23 la partita ha 8 ore e 14 salvataggi in più, e zaino, deposito PC ed esemplari sono identici.

Sospesa per un'ora il 2026-11-18 e poi ripresa: la Grotta Mutevole va sul Rubino (ADR-134, terza modifica), quindi il file qui sotto si scrive com'è. Terza parte, la scrittura di ADR-134, l'unico passo di questa sezione che scrive sulla cartuccia. Toglie la Roccia di Re doppia dalla tasca Oggetti, mette lo sfondo Plain sui box 10 e 11 e aggiunge le quattro decorazioni mancanti. Il file da scrivere sta in `E:/retrogame-mod-pok-dev/_notes/salvataggi/cartucce/smeraldo/08-20261118-ultimo-giro/`, ed è l'unico `.sav` della cartella, con «DA SCRIVERE» nel nome. Lo ha prodotto `gba-save-extraction-smeraldo/tools/emerald_ultimo_giro.py` dalla lettura 1, ed è verificato: sezioni valide in entrambi gli slot, 420 esemplari identici per PKHeX, Pokédex invariato. Prima di cominciare, la copia doppia della seconda parte esiste già su E: e su J:. Nella terza parte gli unici pulsanti di scrittura ammessi sono «Write Save Data» e la sua voce «Restore from save data file»; «Erase cartridge save data» e «Write ROM» restano vietati.

13. Inserisci Smeraldo a cavo staccato, poi collega il cavo nella porta frontale sinistra.
14. Apri FlashGBX, clicca «Game Boy Advance» e controlla che il LED «Mode» sia blu.
15. Clicca «Refresh» e controlla che a sinistra compaia Pokemon - Versione Smeraldo con «Save Type» 1M FLASH (128 KiB), come nella seconda parte.
16. Clicca la freccia di «Write Save Data» e scegli «Restore from save data file». Mai «Erase cartridge save data».
17. Nella finestra dei file vai nella cartella `08-20261118-ultimo-giro` e scegli il file con «DA SCRIVERE» nel nome.
18. FlashGBX non chiede conferma: appena scelto il file comincia a scrivere. Per questo il controllo del nome si fa al passo 17, prima di premere «Apri». Corretto il 2026-11-20 dal proprietario, che ha eseguito il passo; la versione precedente descriveva una finestra di conferma che FlashGBX 5.1 su questo percorso non mostra.
19. Aspetta senza toccare cavo e cartuccia, fino al messaggio «The save data was written and verified successfully!».
20. Clicca «Backup Save Data» e salva nella stessa cartella `08-20261118-ultimo-giro` come `rilettura.sav`. Aspetta che finisca.
21. «Disconnect», stacca il cavo, poi togli la cartuccia.
22. Agente: confronta byte per byte `rilettura.sav` con il file scritto, lo rinomina per esteso, copia tutto su J: con lo SHA-256, rigenera la mappa dei box e la sua stampa, che riportano gli sfondi, e aggiorna i registri.
23. Proprietario, quando gioca: accendi la console, carica la partita e controlla tre cose. Nella tasca Oggetti non c'è più la Roccia di Re e ci sono 29 oggetti. I box 10 e 11 hanno lo sfondo Plain. Nel PC, «Decorazione», le sedie sono 9 e i cuscini 10.

Esito della terza parte, 2026-11-20: scritta dal proprietario con «Restore from save data file» e messaggio di riuscita di FlashGBX; la rilettura `rilettura.sav` è identica byte per byte al file scritto, SHA-256 `90f80b6a…ac217544`, rinominata per esteso («rilettura dopo la scrittura, identica byte per byte al file scritto») e copiata su J: in `backup salvataggi pokèmon/smeraldo-08-20261118-ultimo-giro/` con lo stesso SHA-256. La mappa dei box e la stampa erano già generate da quel file, quindi non cambiano. Smeraldo è chiusa; resta il passo 23 in gioco.

## Diamante, con Checkpoint sul 3DS

Stato del 2026-11-17: FATTA. Due backup identici, copiati sul disco del progetto e sul secondo disco. Checkpoint limita la lunghezza del nome del backup: i nomi usati sono stati `20261117-diam-lett1` e `20261117-diam-lett2`, e la prossima volta conviene un nome breve come quelli. Checkpoint legge il salvataggio della cartuccia e lo copia sulla scheda SD: non scrive sulla cartuccia.

Pulsante che non si tocca mai: «Restore».

1. A 3DS spento, inserisci la cartuccia di Diamante nella fessura delle schede di gioco, come un gioco qualsiasi.
2. Accendi il 3DS. Non avviare Diamante: non serve.
3. Apri Checkpoint, come per i backup di Rubino Omega.
4. Nell'elenco dei giochi scegli quello con il logo DS, cioè Diamante. Se non compare, fermati e fotografa lo schermo.
5. Scegli «New...», poi «Backup», scrivi il nome `20261117-diamante-lettura1` e conferma. Aspetta la conferma che il salvataggio è stato scritto sulla scheda.
6. Ripeti il punto 5 con il nome `20261117-diamante-lettura2`.
7. Esci da Checkpoint e spegni il 3DS. Con la console spenta togli la cartuccia e la scheda SD, e metti la SD nel PC.
8. Agente: copia la cartella di Diamante di `/3ds/Checkpoint/saves/` in `_notes/salvataggi/cartucce/diamante/01-20261117-estrazione/` e su J:, controlla che le due letture siano identiche con lo SHA-256, e legge allenatore e Pokémon con PKHeX.
