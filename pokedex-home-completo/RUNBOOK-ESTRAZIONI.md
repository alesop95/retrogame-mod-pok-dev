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
