---
tipo: nota di studio
livello: avanzato
tags: [ldn, wireless, monitor-mode, driver, switch, microcontrollore]
up: "[[index]]"
vedi_anche: ["[[08-cavo-link]]", "[[10-multiboot-hardware]]", "[[30-opzioni-implementative]]", "[[06-identita-pokemon]]", "[[SOURCES]]"]
---

# Il wireless locale, e il ponte verso la Switch

Questa nota copre il lato wireless del progetto, cioè il tratto che va da un computer a una Nintendo Switch che esegue Rosso Fuoco o Verde Foglia, e il tratto che va da un Game Boy Advance fisico a quel computer. Nasce dalla lettura del canale di supporto del server Pokemon Multiplayer Research fatta il 2026-08-26, insieme al codice e alla documentazione dei repository che quel canale discute, e sostituisce quanto il progetto sapeva prima, che era ricavato da README e da una sola testimonianza riassunta.

Vale la pena leggerla anche a chi interessa soltanto il ponte fra generazioni su hardware originale, perché contiene la conferma esterna dell'opzione D di [[30-opzioni-implementative]] e la ragione tecnica per cui quella è l'unica via praticabile quando all'altro capo c'è una console moderna.

## Il problema, detto in una riga

Un computer deve prendere il posto di una seconda console in uno scambio locale, e per farlo deve parlare un protocollo di rete che Nintendo non ha documentato, con hardware che non è stato progettato per parlarlo.

## LDN, e perché non è né ad-hoc né infrastruttura

LDN[^1] è il protocollo con cui due Switch vicine si trovano e si parlano senza passare da un punto di accesso. La sua particolarità, dichiarata dall'autore della libreria che lo implementa, è di stare a metà fra le due architetture classiche del wireless, e questo dettaglio apparentemente accademico decide l'intera implementazione.

In una rete di infrastruttura esiste un punto di accesso, e ogni stazione deve prima autenticarsi e poi associarsi a esso prima di poter trasmettere qualsiasi cosa. In una rete ad-hoc, che nel gergo di IEEE 802.11 si chiama IBSS[^2], non esiste alcun punto di accesso e le stazioni si parlano da pari a pari senza associazione. LDN prende da entrambe: quando una stazione entra nella rete deve autenticarsi e associarsi come se ci fosse un punto di accesso, ma una volta dentro tutti i nodi comunicano direttamente fra loro come in una rete ad-hoc. C'è anche un'asimmetria nei bit di direzione dei frame, perché quelli dell'host portano FromDS attivo mentre quelli delle altre stazioni non portano né FromDS né ToDS.

Entrare in una rete altrui non è mai stato il problema. Il problema è ospitarne una, ed è qui che il protocollo diventa ostile.

## Perché servono due modalità contemporaneamente

Il ragionamento che segue è il più istruttivo di tutta questa nota, perché è un caso limpido di specifica che non si mappa su nessuna astrazione offerta dal sistema operativo.

Il primo tentativo naturale è mettere l'interfaccia in modalità punto di accesso, dato che i client devono associarsi. Non funziona, perché in quella modalità è impossibile ricevere i frame indirizzati all'indirizzo di broadcast, cioè `ff:ff:ff:ff:ff:ff`: vengono scartati dal kernel o dal driver prima di arrivare all'applicazione, e LDN quei frame li usa. Il secondo tentativo è la modalità ad-hoc, dato che dopo l'associazione i nodi si parlano da pari a pari. Non funziona nemmeno quello, perché in modalità IBSS tutte le richieste di associazione vengono scartate, e LDN quelle richieste le pretende.

La soluzione adottata è usare due interfacce sulla stessa radio contemporaneamente. Un'interfaccia in modalità punto di accesso gestisce i frame di gestione della rete, cioè le richieste di sonda e di associazione; un'interfaccia in modalità monitor riceve e trasmette i frame di dati, compresi quelli in broadcast che l'altra modalità scarterebbe. I frame di dati vengono poi analizzati, decifrati e scritti su un'interfaccia TAP, così che il kernel Linux li veda come traffico di rete normale e lo stack IP funzioni sopra di essi.

Da qui discende il requisito che decide se il progetto sia praticabile su una macchina data: la radio deve saper ricevere e trasmettere action frame in modalità monitor, e deve poter essere sottratta al controllo del gestore di rete del sistema. Quest'ultimo punto è la ragione per cui la procedura prescrive di fermare NetworkManager, e ha il costo evidente che mentre il programma gira quella macchina non ha rete.

## Il requisito reale non è il nome commerciale, è il driver

Il progetto dichiara una tabella di schede provate, e la lettura del canale la completa con i casi negativi, che sono la parte più utile perché dicono cosa non comprare. Le schede dichiarate affidabili sono la ALFA AWUS036ACHM esterna con driver `mt76x0u` e la Realtek RTL8821CE interna con driver `rtw88_8821ce`; la AMD RZ616 interna con driver `mt7921e` funziona a metà velocità e a volte si blocca prima di terminare. Fra quelle problematiche, la Intel AX200 con `iwlwifi` non riesce a ricevere un indirizzo IP, e l'Atheros AR9271 con `ath9k_htc` non ci riesce quasi mai.

Il ritornello del canale, ripetuto da più persone in tre mesi, è che le schede Intel non fanno modalità monitor e quindi non servono, e che il criterio operativo è se la scheda si possa mettere in stato non gestito. Su questo punto il progetto aveva registrato un'informazione che va corretta, ed è la correzione più utile emersa da questa lettura: ciò che determina il funzionamento non è il nome del prodotto ma il chip e quindi il driver, e due esemplari con lo stesso nome commerciale possono montare chip diversi a seconda della revisione. La testimonianza decisiva è un utente che riporta il proprio dispositivo come `driver: rtw_8821cu`, quindi un chip RTL8821CU servito dal driver in albero `rtw88`, e non l'RTL8811AU che il nome di quella famiglia di adattatori aveva fatto supporre. È anche la spiegazione del perché quell'utente non abbia avuto bisogno di alcun driver fuori albero.

La conseguenza pratica è che la domanda giusta da porsi davanti a un adattatore non è come si chiama, ma quale coppia di identificatori USB espone e quale modulo del kernel lo reclama.

## La via Windows, che ribalta un vincolo di piattaforma

Il progetto ha sempre dato per assodato che questo track richiedesse Linux, e da qui era nata la tensione con il track dello Smeraldo, che richiede Windows perché PKHeX è un'applicazione .NET Windows Forms. Quella tensione era registrata come decisione aperta fra dual boot e supporto avviabile. Esiste una terza via, ed è istruttiva per ragioni che vanno oltre questo progetto.

Il problema di portare il programma su Windows non è il programma, che è Python: è che dietro di esso c'è l'intero stack wireless del kernel Linux, cioè `mac80211`, i driver del chip e la nozione stessa di modalità monitor, che su Windows non esistono. Riscrivere quello stack sarebbe un lavoro fuori scala. La soluzione adottata dal demone `ldnd` è di non riscriverlo e di portarselo dietro: usa LKL[^3], che è il kernel Linux compilato come una libreria statica ordinaria, la collega dentro un eseguibile Windows costruito con MinGW, e le consegna l'adattatore attraverso WinUSB. Il kernel Linux gira quindi come una libreria dentro un processo Windows, carica i propri driver e i propri file di firmware, e presenta al programma l'interfaccia che si aspetta.

Due dettagli confermano che il meccanismo è esattamente questo. Il primo è che la procedura richiede di scaricare l'archivio `linux-firmware` e di tenerne i file accanto all'eseguibile, perché il driver che gira dentro l'eseguibile chiede il proprio firmware come lo chiederebbe su Linux. Il secondo è la riga di comando con cui il kernel incorporato viene avviato, che contiene `mem=128M mac80211_hwsim.radios=0 rtw88_usb.switch_usb_mode=0`, cioè parametri di modulo del kernel Linux passati a un programma Windows.

Ne discende una proprietà non ovvia e verificata sul campo: le due implementazioni non hanno la stessa compatibilità hardware. Un utente riporta che la versione Linux originale non funziona con il suo adattatore mentre quella Windows sì, e la ragione è strutturale. La versione Linux dipende da come il kernel del sistema, il gestore di rete e il driver installato si comportano su quella macchina; la versione Windows scavalca tutto, prende il dispositivo USB grezzo e lo consegna a un kernel che si porta dietro. Meno cose possono intromettersi.

Il prezzo va detto perché è concreto. Il dispositivo va prima riassegnato al driver WinUSB con Zadig, e da quel momento non funziona più come normale scheda di rete, quindi serve un altro modo di accedere a internet su quella macchina. E funziona soltanto con adattatori USB, mai con schede interne, perché WinUSB può prendere soltanto un dispositivo USB: è il rovescio esatto del vincolo su Linux, dove anche una scheda interna va bene se il suo driver collabora.

## Un guasto che vale conoscere prima di incontrarlo

Il malfunzionamento più segnalato ha una causa sola e un rimedio noto, e sapere entrambi risparmia una serata. Alcuni chip Realtek USB, quando vengono inizializzati, negoziano il passaggio alla modalità USB 3, e per farlo si presentano di nuovo sul bus come se fossero stati staccati e riattaccati. Windows a quel punto rimette il proprio driver e la riassegnazione fatta con Zadig risulta annullata, con il sintomo che l'utilità mostra il dispositivo tornato al driver del produttore invece che a WinUSB. Il parametro `rtw88_usb.switch_usb_mode=0` disabilita quella negoziazione, ed è per questo che compare nella riga di comando del demone; il rimedio manuale è forzare il dispositivo su una porta USB 2, che diverse persone riportano come risolutivo.

## Il lato Game Boy Advance, e la conferma dell'opzione D

Qui c'è il fatto che collega questa nota al resto del progetto, e va scritto con precisione perché è facile dedurne la cosa sbagliata.

Il Wireless Adapter del Game Boy Advance non è un dispositivo 802.11. È un progetto interamente proprietario, con un protocollo radio che non ha nulla in comune con il Wi-Fi, e l'autore del progetto LDN lo afferma esplicitamente. Ne segue che nessuna scheda Wi-Fi, per quanto capace di modalità monitor, potrà mai parlare con un Game Boy Advance: la modalità monitor serve al tratto verso la Switch, non al tratto verso il Game Boy Advance.

La via che quell'autore indica per il tratto mancante è un microcontrollore che si finge il Wireless Adapter dal lato del Game Boy Advance. È parola per parola l'opzione D di [[30-opzioni-implementative]], formulata da chi ha scritto il codice dell'altro capo, e la sua conferma da una fonte indipendente sposta quell'opzione dal terreno delle ipotesi a quello delle cose fatte. Nel canale compare infatti la fotografia di una catena funzionante, descritta dal suo autore come Game Boy Advance, adattatore wireless finto costruito su misura, progetto LDN e Nintendo Switch, nell'ordine.

C'è una riserva tecnica che lo stesso autore solleva, ed è di quelle che si pagano in fase di collaudo e non in fase di progetto: la catena è già instabile con un solo salto radio, e aggiungere la latenza e la perdita di pacchetti di un secondo adattatore potrebbe essere troppo.

## Che cosa emula davvero l'emulatore sulla console

Su come i giochi di generazione 3 girino sulla Switch il progetto aveva un punto dichiarato aperto, e il canale lo chiude con due affermazioni che vanno prese insieme.

La prima è che l'emulatore implementa il Wireless Adapter in emulazione di alto livello, cioè non simula il dispositivo ma ne riproduce il comportamento a livello di funzioni, e in quella implementazione l'adattatore risulta sempre collegato. La seconda, e per noi la più importante, è che l'emulatore emula il Wireless Adapter e non emula il cavo Link.

La conseguenza per il ponte è netta e va registrata come vincolo: verso un gioco di generazione 3 in esecuzione su Switch non esiste alcuna via che passi dal cavo, e l'unico canale è quello wireless. Il protocollo del cavo studiato in [[08-cavo-link]] resta valido e necessario per il tratto fra Game Boy e Game Boy Advance su hardware originale, che è il nostro caso d'uso, ma non è trasferibile al caso della console moderna.

Un terzo dettaglio, minore per il ponte e rilevante per chi studia l'identità dei Pokemon, è che la presenza del Wireless Adapter cambia la cadenza con cui avanza il generatore pseudocasuale, e quindi i metodi di ricerca degli esemplari cromatici che si basano sul conteggio dei fotogrammi non si trasferiscono immutati. Il legame con [[06-identita-pokemon]] è quello.

## Un vincolo di gioco che nessuna documentazione dichiarava

Vale la pena registrare un dettaglio che una sola persona ha scoperto provando, perché colpirebbe esattamente il nostro caso d'uso. Il giocatore simulato dal computer ha un insieme di flag di progressione, e nella configurazione predefinita non ha il Pokedex nazionale. Finché non lo ha, il gioco rifiuta lo scambio di molte specie, perché il controllo di ammissibilità dello scambio dipende da quel flag. Chi ha risolto ha modificato il codice del giocatore simulato imponendo il valore `0x0F` a quelle flag.

Per un ponte che porta esemplari dalle generazioni 1 e 2 questo è centrale e non accessorio: sono precisamente le specie fuori dalla prima regione a essere rifiutate, e un tentativo che fallisse per questa ragione somiglierebbe molto a un errore di formato senza esserlo.

## Che cosa serve, in fila

Mettendo insieme le due implementazioni, i requisiti materiali sono i seguenti. Serve un adattatore wireless il cui chip abbia un driver Linux capace di modalità monitor, e serve che sia USB se si va per la via Windows. Serve un gioco di generazione 3 su Switch portato avanti fino allo sbloccio della sala degli scambi, che il materiale stima in venti o quaranta minuti di gioco. Servono le chiavi della console, sul cui trattamento vale senza attenuazioni quanto scritto in `rules/hardware-and-perimeter.md`. Servono almeno due strutture di Pokemon in formato `.pk3` da usare come controparte dello scambio, e il secondo membro della lista è quello che verrà consegnato alla console.

Sul come ottenere quelle strutture c'è l'anello che chiude il cerchio con l'altro sottoprogetto, ed è la risposta a una domanda che il progetto teneva aperta da giorni. L'autore dichiara di non distribuire dati di Pokemon ma soltanto strumenti, e indica che chi voglia partire dai propri salvataggi su cartuccia fisica usi un lettore, nominando il GBxCart RW e il GB Operator. Il lettore ordinato per il sottoprogetto dello Smeraldo è quindi lo stesso apparecchio che serve qui, e la fase in cui entra è la produzione delle strutture di partenza; chi lavora su copie proprie in emulazione non ha bisogno di alcun hardware.

## Cosa leggere dopo

[[08-cavo-link]] per il protocollo del tratto su hardware originale, che questa nota non sostituisce. [[30-opzioni-implementative]] per il posto che l'opzione D occupa fra le quattro strade di ADR-008, ora che una fonte indipendente la indica come la via giusta per il capo Game Boy Advance. [[09-esecuzione-codice]] per la primitiva che il ponte usa dal lato Game Boy, che è un problema diverso e resta indipendente da tutto questo.

[^1]: *LDN*, Local Discovery and Network - il protocollo proprietario con cui le console Nintendo Switch formano una rete locale senza punto di accesso; la sua specifica pubblica è il lavoro di reverse engineering documentato nel wiki di NintendoClients.

[^2]: *IBSS*, Independent Basic Service Set - il nome che lo standard IEEE 802.11 dà alla rete senza punto di accesso, quella che nell'uso comune si chiama ad-hoc.

[^3]: *LKL*, Linux Kernel Library - il kernel Linux compilato come libreria collegabile a un programma ordinario, così che i suoi sottosistemi, fra cui lo stack di rete e i driver, siano usabili in spazio utente e su sistemi operativi diversi da Linux.
