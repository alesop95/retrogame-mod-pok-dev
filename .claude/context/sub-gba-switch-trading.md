---
generated-from-commit: d08a011
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - gba-switch-pokemon-trading/
last-verified-commit: 7696c46
stato: in ricerca, nessun ambiente allestito
---

# Sottoprogetto: trading wireless locale fra PC e Nintendo Switch

Lo stato canonico di questo track e' questo file, insieme alla riga che lo riguarda in `memory/index.md`. La sezione 14 dell'handoff propone un prompt di ripartenza scritto per una chat: resta come storico, la precedenza e' qui.

Obiettivo: far comunicare un PC Linux con una Nintendo Switch tramite LDN, il protocollo wireless locale proprietario di Nintendo, per eseguire uno scambio di Pokemon con una copia di FireRed o LeafGreen in esecuzione sulla console. Il PC simula la seconda console. E' un proof of concept dimostrativo, non un tool finito.

## Dove siamo

Fase di ricerca conclusa, nessun ambiente allestito e nessun repository clonato. Sono identificati i due progetti su cui il lavoro si appoggerebbe: `kinnay/LDN`, la libreria Python del protocollo, e `tornadus/frlg-ldn-trade`, il proof of concept che la usa per il trade. Il funzionamento lato gioco dipende dalla decompilazione comunitaria `pret/pokefirered`, quindi un aggiornamento del gioco sulla console potrebbe romperne la compatibilita'.

Questo track ribalta il presupposto con cui era stato aperto: non e' una via verso Pokemon Home ne' una sovrapposizione con il track 3DS, come si era ipotizzato quando la cartella era vuota. E' un lavoro di rete e di reverse engineering, ed e' il secondo destinato a produrre software vero, accanto al ponte fra generazioni.

## Prossimo passo concreto

Clonare i due repository e leggere il codice di `frlgtrade.py` e del pacchetto `ldn`, che nessuno ha ancora aperto: l'handoff e' costruito su README e metadati, non sul sorgente. Da li' si colmano le lacune della sezione 13.

## Vincolo che condiziona tutto

Serve una scheda Wi-Fi che supporti la modalita' monitor, e la scelta e' il fattore critico dichiarato: le schede USB esterne di fascia adatta risultano affidabili nei test degli autori, mentre alcune schede interne moderne sono fino alla meta' piu' lente e soggette a deadlock. Prima di allestire qualsiasi cosa va accertato quale scheda e' disponibile su questa macchina, perche' da quella risposta dipende se il track e' praticabile o no.

## Materiale ora letto

Le due fonti portanti del track sono state lette per la prima volta. La libreria di kinnay richiede Linux con Python 3.12 o successivo, il privilegio `CAP_NET_ADMIN`, l'arresto di NetworkManager e hardware wireless capace di ricevere e trasmettere action frame in modalita' monitor. La specifica del protocollo non sta nel suo README ma nel wiki di NintendoClients, che documenta l'action frame vendor-specific trasmesso ogni 100 millisecondi con OUI 00:22:AA, i canali 1, 6 e 11 in banda 2.4 GHz, la struttura dell'advertisement campo per campo, i tre livelli di cifratura e la derivazione delle chiavi dalle chiavi di console, la sequenza di connessione con i suoi timeout e l'assegnazione degli indirizzi nella forma 169.254.X.Y.

Il proof of concept di tornadus richiede Python 3.12 o successivo, la libreria di kinnay, le chiavi della console e una scheda Wi-Fi compatibile, e opera facendosi passare per un giocatore che si collega come leader mentre la console avvia lo scambio dal Direct Corner. La logica sta in `frlgtrade.py` con la cartella `frlgsim/`, e i Pokemon si scambiano nei formati `.pk3` in chiaro e `.ek3` cifrato.

Sulla domanda che blocca il track la risposta e' arrivata, ed e' in due parti. La prima: questa macchina e' un computer fisso senza alcuna interfaccia Wi-Fi, quindi la scheda non c'e' e non va accertata, va procurata. La seconda: oltre alla lista del progetto, che dichiara affidabili ALFA AWUS036ACHM e Realtek RTL8821CE e poco affidabile AMD RZ616, esiste una testimonianza di campo nel canale di supporto del server Pokemon Multiplayer Research, dove un utente dichiara che il TP-Link AC600 funziona bene e che al contrario una Intel Pro Wireless 5100 AGN integrata non funziona.

Ne segue una indicazione pratica con la sua riserva. L'adattatore che l'utente ha in mente, il TP-Link Archer T2U Nano, e' della stessa famiglia AC600 e monta un chip Realtek RTL8811AU; la testimonianza citata riguarda il modello Archer T2U Plus, dello stesso chipset. Il supporto alla modalita' monitor su quel chip non esiste nel kernel Linux e passa da un driver fuori albero mantenuto dalla community, quindi la prova e' sensata ma non e' garantita. Chi volesse la via sicura compra l'adattatore che il progetto stesso dichiara affidabile.

## Da verificare prima di pianificare

La data di disponibilita' di Rosso Fuoco e Verde Foglia su Switch e' incerta: la sezione 7 dell'handoff 3DS dice ottobre 2026, mentre fonti secondarie trovate il 2026-08-25 indicano il 27 febbraio 2026, con scambio locale che emula l'adattatore wireless del Game Boy Advance. Se la seconda e' corretta il presupposto del track esiste gia'. Va verificato su fonte primaria.

## Decisioni aperte

Serve Linux, e l'handoff propone una chiavetta avviabile con Linux Mint. Questo mette il track in tensione con quello dello Smeraldo, che richiede Windows 11 per PKHeX: va deciso se convivono sulla stessa macchina in dual boot o live USB, o se si separano. La decisione non e' ancora presa e non e' urgente finche' il track resta in ricerca.

Restano da chiarire le discrepanze registrate nella sezione 13 dell'handoff: quale versione di Python sia realmente richiesta, quale scheda Wi-Fi sia quella usata nella dimostrazione, e soprattutto in che forma giri FireRed sulla console, dato che il materiale non chiarisce se sia emulazione, port ufficiale o altro. Quest'ultimo punto condiziona la spiegazione del meccanismo di scambio.

Il rapporto con il GBxCart RW non e' spiegato dal materiale: l'apparecchio compare fra i requisiti ma non e' detto in quale fase entri. E' lo stesso lettore del track Smeraldo, quindi una sovrapposizione hardware esiste, ma non e' documentata.

## Perimetro

Le `prod.keys` della console sono materiale di chiave proprietario, si estraggono solo da una console modificata e non sono redistribuibili. Sono escluse dal version control dal blocco dedicato del `.gitignore`, insieme ai file di dati `.pk3`, e valgono le stesse cautele del materiale di chiave del 3DS descritte in `design-and-security.md`.

## Evidenze e materiale locale

L'handoff `HANDOFF_frlg-ldn-trade.md` sta nella cartella del sottoprogetto ed e' l'unico materiale esistente. Non ci sono media. Il codice dei due repository di riferimento non e' ancora presente in locale.
