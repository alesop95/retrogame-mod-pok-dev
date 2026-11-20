# Una Switch usata da modificare, per la fase Switch

> Studio del 2026-11-17, chiesto dal proprietario per portare avanti i lotti della fase Switch mentre la banca è ferma. Fonti lette da un subagente di lettura web lo stesso giorno, registrate in `SOURCES.md` nella sezione del 2026-11-17. Ciò che è letto e ciò che è inferito sono distinti in ogni paragrafo.

## Perché serve e che cosa si chiede alla console

La fase Switch (voce «da ricordare sempre» di `.claude/memory/pending.md`) chiede di gestire salvataggi propri, di produrre e giudicare esemplari con la libreria di PKHeX sui propri giochi e, per il track del trading, di estrarre le proprie `prod.keys`. Tutto questo richiede una console che esegua codice non firmato. La console non serve per la pirateria e non si usa per quello: valgono `rules/hardware-and-perimeter.md` e il divieto di salvataggi di terzi.

## Quali console si modificano senza saldare

Letto su NH Switch Guide, pagina «Getting started», consultata il 2026-11-17: solo il primo modello di Switch, con il processore Tegra X1 detto Erista, ha la vulnerabilità del bootROM che si sfrutta in modalità di ripristino (RCM) senza aprire la console, e solo nei numeri di serie prodotti prima della correzione. Switch V2 (HAC-001-01) e Switch Lite hanno il processore Mariko con il bootROM corretto e senza un modchip non si modificano; la pagina non nomina l'OLED, che per inferenza, e per una fonte secondaria, è nella stessa condizione. La tabella corrente della guida è questa; fonti più vecchie davano limiti un po' diversi e va usata la corrente.

| Prefisso | Non corretta fino a | Forse corretta fino a | Oltre |
|---|---|---|---|
| XAW1 | XAW10065000000 | XAW10120000000 | corretta |
| XAW4 | XAW40011000000 | XAW40012500000 | corretta |
| XAW7 | XAW70017500000 | XAW70030000000 | corretta |
| XAJ1 | XAJ10020000000 | XAJ10030000000 | corretta |
| XAJ4 | XAJ40044000000 | XAJ40083000000 | corretta |
| XAJ7 | XAJ70040000000 | XAJ70050000000 | corretta |
| XAW9, XAJ9, XAK | nessuna | potenzialmente corrette | corretta |

Lo strumento della comunità `ismyswitchpatched.com` è in linea (letto) e confronta prefisso e sei cifre con i dati raccolti su GBAtemp. Il thread originale di GBAtemp risponde 403 e non è stato letto. Le Switch europee hanno di norma il prefisso XAW o XAJ; quale delle due sia più frequente in Italia non è verificato.

Per una console corretta, una Lite o una OLED la guida sostiene un solo modchip, il Picofly, e dice che l'installazione richiede esperienza di microsaldatura, con il rischio di una console che non si avvia. Per chi non salda, la via sensata è una V1 non corretta, oppure un installatore di fiducia: è una conclusione dell'agente, non della guida.

## Come si compra senza sorprese

Letto su `ismyswitchpatched.com`, guida al numero di serie: il numero comincia con X e sta sull'etichetta bianca del bordo inferiore, vicino alla porta USB-C; sulla scatola si legge dall'etichetta del codice a barre. La guida della comunità consiglia di leggerlo anche in Impostazioni di sistema, Console, Informazioni sul numero di serie, che è più affidabile dell'etichetta. Al venditore si chiedono quindi tre foto: l'etichetta della console a fuoco, l'etichetta della scatola e la schermata del numero di serie; poi la versione del firmware e la prova che si accenda. Il controllo di un ban non ha una procedura documentata: una console bannata non accede ai servizi online, quindi si chiede al venditore se è mai stata modificata e, se si prova di persona, si apre l'eShop. È una cautela dell'agente.

Il prezzo è una stima e non una misura, presa da risultati di ricerca non aperti, e sta nel livello privato del progetto perché il controllo di anonimizzazione non ammette importi nei file tracciati. Le piazze sono Subito, eBay italiano e tedesco, Wallapop e Vinted. Un annuncio che dice «unpatched» senza la foto del numero di serie non vale.

## Ban e separazione delle memorie

Letto nelle FAQ della guida: i ban colpiti finora riguardano pirateria online, trucchi in rete, immagini del profilo personalizzate e installazione di applicazioni homebrew rilevate dalla telemetria, e la guida avverte che in futuro potrebbe toccare anche l'homebrew innocuo. L'emuMMC, cioè una copia del sistema sulla microSD, isola il lavoro modificato dalla memoria interna e, secondo la guida, toglie il rischio di ban; si consiglia 90DNS sulla copia. La memoria interna resta pulita e si avvia con il firmware originale per andare online. Nessuna fonte letta tratta Pokémon HOME su una console modificata: per inferenza HOME si usa soltanto dalla memoria interna pulita, mai dalla copia modificata.

## Che cosa serve oltre alla console

Letto nella stessa guida: un jig RCM per la guida del Joy-Con destro (gli oggetti di casa non sono supportati), un computer con un cavo USB dati per inviare il payload, una microSD da almeno 128 GB per l'emuMMC. Versioni correnti lette il 2026-11-17: Atmosphère 1.12.2, hekate 6.5.5, firmware 23.5.0 dell'11 novembre 2026. Le FAQ della stessa guida consigliano la microSD in FAT32 e dicono che una scheda da 32 GB o meno non basta né per il dump completo della memoria interna né per l'emuMMC. Copie locali delle fonti in `_notes/fonti/raccolte/switch-modding-2026-11-17/`.

## Come si cercano gli annunci

Il proprietario non ha una Switch del primo modello e la compra usata (2026-11-17). Gli annunci italiani si cercano a mano: il motore di ricerca dell'agente copre soltanto i siti americani e non indicizza Subito né eBay.it, e una ricerca del 2026-11-17 ha restituito solo annunci di eBay.com, OfferUp e Mercari. Le parole da cercare su Subito, eBay.it, eBay.de, Vinted e Wallapop sono «switch unpatched», «switch v1», «switch HAC-001», «switch 2017», «XAW1» e «XAJ1». Le ricerche di eBay si aprono già pronte con https://www.ebay.it/sch/i.html?_nkw=switch+unpatched e https://www.ebay.de/sch/i.html?_nkw=switch+unpatched, quelle di Vinted con https://www.vinted.it/catalog?search_text=switch%20unpatched.

Un annuncio si scarta in pochi secondi con due segni che non chiedono il numero di serie. Sul retro della console, la sigla HAC-001(-01) indica il secondo modello, con il processore corretto, che non si modifica senza saldare; serve la sigla HAC-001 senza il suffisso. La scatola interamente rossa è quella del secondo modello, come dicono le FAQ della guida («red box»). Se il primo controllo passa, si chiede il numero di serie e lo si confronta con la tabella sopra o con ismyswitchpatched: solo «non corretta» è un acquisto sicuro, «potenzialmente corretta» è una scommessa.

Il messaggio da mandare al venditore chiede le tre foto e una conferma, con queste parole: «Buongiorno, mi interessa la Switch. Mi può mandare una foto dell'etichetta bianca sotto la console con il numero di serie (inizia con X), una della scatola se c'è, e dirmi se la console è mai stata modificata o bannata? Grazie.» Un venditore che non manda il numero di serie non vende una console verificabile.

Per la modifica la console basta da sola, con un paio di Joy-Con qualunque per il jig: la base e i controller originali non servono. A parte servono un jig RCM, un cavo USB-C dati e una microSD da 128 GB in FAT32 comprata in un negozio e non su un sito di aste, come consiglia la guida.

## Domande aperte

CORREZIONE del 2026-11-17: l'agente aveva supposto che il proprietario avesse già una Switch del primo modello, perché gioca a Leggende Z-A; il proprietario ha precisato che non ha una Switch 1 e deve comprarla. Resta da decidere se la console nuova avrà un account Nintendo diverso o lo stesso, con la regola di una sola console principale: è da decidere prima di comprare, e il proprietario non ha Scarlatto né Violetto (pending, ADR-120).
