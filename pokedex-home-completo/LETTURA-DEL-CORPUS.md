# La lettura del corpus, cluster per cluster

Registro della lettura integrale del corpus della collezione, chiesta dall'utente il 2026-09-09 con la prescrizione che tutto vada letto prima di aprire altro lavoro di produzione. Non è un censimento generato: è un documento autorato che cresce a lotti, e ogni voce dice che cosa il cluster ha aggiunto, che cosa ha corretto e che cosa resta non letto con il motivo.

La misura del compito, fissata all'inizio perché serve a valutare l'avanzamento: il corpus scaricato è di duecentonovantadue documenti per sei milioni e duecentomila byte, distribuiti su quarantadue cluster più il preambolo e i commenti al post di raccolta. Il conto delle fonti registrate è centosettantuno, e le pagine non scaricate restano dichiarate come tali nel censimento generato.

## Lo stato, aggiornato a ogni lotto

| Cluster | Fonti | Stato | Dove sta l'esito |
|---|---|---|---|
| 2) What are we loosing with Pokemon Bank | 6 | letto il 2026-09-08 | `STUDIO-05` e `INDICE-FOGLI-ESTERNI.md` |
| 1) Dex completions / Overall lists | 10 | letto il 2026-09-08 | `STUDIO-06` |
| 9) RNG Manipulation and Glitches, sei sotto-cluster | 16 | letto il 2026-09-09 | `STUDIO-08` |
| 6) How to still get Bank / 3DS modding | 4 | letto il 2026-09-09 | `STUDIO-09` e questa nota |
| 5) Other lists and spreadsheets | 6 | letto il 2026-09-09, due voci non recuperabili | `ID-NOTEVOLI.md` e questa nota |
| 4) Ribbon Master | 3 | letto il 2026-09-09, il manuale resta da recuperare | questa nota |
| 3) Collections of one Pokemon species | 6 | letto il 2026-09-09 | questa nota |
| gli altri trentacinque cluster | il resto | da leggere | |

## Lotto del 2026-09-09: i cluster 6, 5, 4 e 3

### Che cosa ha aggiunto il cluster sull'accesso alla banca

La voce più importante era la spiegazione tecnica del tracciatore, ed è già in `STUDIO-09` perché cambia la pianificazione. Le altre tre voci del cluster aggiungono meno di quanto il titolo promettesse: la guida al modding della console è quella che il progetto già segue, la tabella della connettività è un file su un servizio di condivisione che non si scarica senza credenziali, e la guida alla console definitiva è una procedura di allestimento per chi parte da zero, quindi utile a chi deve comprare l'hardware e non a chi lo ha già.

Vale però registrare una cosa che quella guida dice e che il progetto non aveva scritto in forma esplicita: la catena richiede due console fisiche nello stesso momento per il passaggio dalla quarta alla quinta generazione, perché quel trasferimento avviene fra due apparecchi in comunicazione locale e non dentro una console sola. È un vincolo materiale e non una comodità, e il progetto lo ha implicitamente soddisfatto ma non lo aveva enunciato.

### Che cosa ha aggiunto il cluster delle altre liste, ed è la misura di una nostra cecità

La voce che ha prodotto lavoro è l'elenco enciclopedico degli identificativi di allenatore notevoli, che il crawler non aveva scaricato e che una richiesta locale ha restituito al primo tentativo. È una tabella di ottocentonovantasei righe utili, ciascuna con l'identificativo, il nome dell'allenatore e l'evento a cui appartiene, e serve a rispondere a una domanda che il progetto non poteva porsi da solo: quante coppie fra allenatore e identificativo siano documentate al di fuori delle nostre liste.

Lo strumento è `tools/censimento-id-notevoli.py`, il documento è `ID-NOTEVOLI.md`, e la misura è nei due versi come ADR-044 prescrive. Quattrocentosettantatre righe trovano corrispondenza esatta nelle nostre liste sulla coppia fra allenatore e identificativo. Trecentouno corrispondono sul solo identificativo, e la coincidenza è dichiarata debole perché due eventi diversi possono condividere un numero. Tre righe la fonte stessa le dichiara non appartenenti ad alcun esemplare da collezione, cioè gli identificativi dei Pokemon da noleggio e quello che il catalogo di un gioco usa internamente. Restano centodiciannove righe non coperte, e quella è la nostra cecità.

Guardate una per una, le centodiciannove hanno una spiegazione che conferma per via indipendente una decisione già presa: la grande maggioranza sono distribuzioni coreane e giapponesi, con il nome dell'allenatore in hangul o in katakana, cioè precisamente la classe che ADR-040 aveva escluso per la barriera della lingua. Le poche restanti sono eventi in gioco che nessuna carta ha lasciato, come il Floette del fiore eterno con identificativo zerozerozerozerozerouno, e distribuzioni locali di piccola scala. Ne segue che la copertura del progetto sulle distribuzioni documentate è buona e che il buco è dove il progetto ha deciso che fosse.

Due voci del cluster non si recuperano e sono catalogate con il motivo. Il foglio delle sfere abbinate, che sarebbe la fonte comunitaria dell'asse fra specie e sfera, sta su un servizio di condivisione che risponde con un rifiuto sia all'esportazione sia allo scaricamento diretto, perché è un file caricato e non un documento nativo. La tabella della connettività è nella stessa condizione. Entrambe sono materiale che l'utente può scaricare dal browser in un minuto, e stanno in `pending.md` con la domanda a cui servono.

### Che cosa ha aggiunto il cluster dei fiocchi

Poco in contenuto e una cosa in metodo. Il manuale comunitario dei fiocchi è ospitato su un servizio che rende le pagine nel browser, quindi il crawler ne ha salvato il solo guscio: mille e duecento byte di intestazione e nessun testo. Ciò che quel guscio porta è però significativo, perché è l'unica riga di testo che il servizio scrive nel documento iniziale, ed è un avviso: la banca chiude il 26 febbraio 2027, chi vuole completare la settima generazione lo faccia prima, ed esiste una pagina di preparazione d'emergenza per chi voglia chiudere un fiocco master entro la scadenza. Ne segue che quel manuale è una fonte da recuperare e non da archiviare, perché ha una pagina dedicata esattamente al nostro problema, e il recupero richiede il percorso giusto delle sue sotto-pagine oppure la consegna manuale.

### Che cosa ha aggiunto il cluster delle collezioni di una sola specie

È il cluster che documenta gli assi che il progetto chiama minori e che ADR-041 prescrive di misurare invece di moltiplicare. Le sue voci sono pagine dell'archivio enciclopedico sulle distribuzioni di una specie sola, cioè Pikachu, Genesect, Deoxys e Keldeo, e pagine sui contrassegni e sulle condizioni meteorologiche di ottava generazione.

La voce che serve al nostro lavoro è quella sui livelli minimi per sfera, che per ciascuna specie dichiara il livello più basso a cui la si può avere in ciascuna sfera, distinguendo fra l'esemplare cresciuto e quello selvatico. È esattamente la tavola che serve a comporre una coppia fra specie e sfera che il verificatore accetti, e va dichiarato un limite nostro: l'estrattore che ha ridotto quella pagina a testo ha perso le intestazioni delle colonne e conservato i numeri, quindi la tavola è oggi illeggibile nel derivato mentre il grezzo, che sta accanto, la contiene ancora.

I contrassegni e il meteo di ottava generazione non toccano la scadenza, perché quella generazione parla direttamente col deposito, e restano registrati come materia dell'asse dei contrassegni.

## Una correzione che viene dall'utente e non dalle fonti

Il vincolo di calendario che `STUDIO-09` aveva sollevato sul piano a pagamento è già soddisfatto: l'utente ha il piano attivo, e la banca è gratuita dal 2023, quando chiuse il negozio in rete della console portatile. Il contatore di giorni che l'applicazione della banca mostra è il residuo di quella gratuità e non un abbonamento da rinnovare, ed era già stato registrato il 2026-09-03 come artefatto privo di significato per la nostra pianificazione. Resta della sezione di `STUDIO-09` la sola parte che conta, cioè la capienza: seimila posizioni, novemila da ottobre 2026, e il tetto va contato nel piano perché il perimetro che ADR-051 apre è più grande di quella cifra.
