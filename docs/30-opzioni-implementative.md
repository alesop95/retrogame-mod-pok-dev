---
tipo: nota di studio
livello: decisione
tags: [adr-008, opzioni, roadmap, poke-transporter-gb]
up: "[[index]]"
vedi_anche: ["[[07-conversione-vincoli]]", "[[10-multiboot-hardware]]", "[[20-architettura-codice]]", "[[31-glossario]]", "[[SOURCES]]"]
---

# Le quattro strade, e quanto costano davvero

Questa nota raccoglie e aggiorna il contenuto decisionale che stava nell'handoff di ricerca del sottoprogetto, ritirato quando la sua conoscenza e' stata assorbita nei documenti che la superano. La decisione resta aperta e registrata come ADR-008; qui c'e' il materiale per prenderla.

## Perche' il ponte non esiste

Ogni generazione della serie ha storicamente permesso di portare avanti i propri Pokemon nella successiva, con un meccanismo ufficiale: il Time Capsule fra generazione 1 e 2, il Pal Park fra la 3 e la 4, e poi la catena che arriva fino ai servizi in rete. Fra la generazione 2 e la 3 quel meccanismo non e' mai esistito. Non e' una dimenticanza tecnica: il cambio di piattaforma dal Game Boy al Game Boy Advance ha portato con se' un cambio completo del formato dei dati, come mostrano [[06-identita-pokemon]] e [[04-cifratura-gen3]], e la ricostruzione dei campi mancanti non ha una risposta unica, come mostra [[07-conversione-vincoli]].

Chi vuole quel ponte deve quindi costruirlo, e la community lo ha fatto piu' volte in modi diversi.

## Il progetto di riferimento

Poke Transporter GB e' un programma homebrew per Game Boy Advance, sotto licenza MIT, che trasferisce Pokemon da Rosso, Blu, Giallo, Oro, Argento e Cristallo verso Rubino, Zaffiro, Smeraldo, Rosso Fuoco e Verde Foglia. Il lato sorgente e' supportato nelle versioni inglesi, il lato destinazione anche in italiano, spagnolo, tedesco e francese. Usa il PCCS come dipendenza per la conversione.

Tre fatti su questo progetto vanno tenuti in evidenza perche' cambiano le aspettative. Il primo e' che il trasferimento e' a senso unico e distruttivo sulla sorgente: il Pokemon trasferito viene rimosso dal gioco di generazione 1 o 2, esattamente come accade con i meccanismi ufficiali delle generazioni successive, e sia il salvataggio di partenza sia quello di arrivo vengono modificati. Il secondo e' che non funziona con cartucce contraffatte, e il modo in cui non funziona e' la perdita dei Pokemon trasferiti: la ragione tecnica e' spiegata in [[09-esecuzione-codice]], e sta negli indirizzi assoluti dentro il payload. Il terzo e' che non esiste emulatore su cui provarlo, con la precisazione fatta in [[10-multiboot-hardware]] su cosa invece si emula.

Dalla cronologia delle release, che si rilegge su GitHub e non vale la pena duplicare qui, restano due informazioni che confermano dall'esterno quanto ricostruito leggendo il codice. La prima e' che il supporto a Giallo e' passato per un punto di ingresso di esecuzione di codice nuovo e dedicato, che e' coerente con il fatto che il payload dipenda dalla variante di ROM. La seconda e' che una release e' stata dedicata a un bug critico di corruzione dei dati legato al byte 0xFE, cioe' esattamente il byte che il protocollo del cavo non puo' trasmettere e che la lista di correzione esiste per aggirare: il meccanismo descritto in [[08-cavo-link]] non e' una curiosita' storica, e' una fonte reale di difetti.

Il suo autore ha pubblicato una serie di articoli sul processo di sviluppo, indicizzata in [[SOURCES]], che ripercorre in dieci parti l'architettura della GBA, il formato di salvataggio, il protocollo del cavo, la tecnica di esecuzione di codice, il motore di testo, il trasferimento e la gestione dell'orologio. E' la fonte piu' ricca sulle scelte implementative, perche' il codice dice cosa fa e gli articoli dicono perche'.

## Le quattro opzioni

L'opzione A e' usare o contribuire a Poke Transporter GB cosi' come e'. E' la strada che da' un risultato funzionante oggi, al costo di procurarsi l'hardware elencato in [[10-multiboot-hardware]]. Se l'obiettivo comprende lo sviluppo, il repository ha issue aperte e un supporto linguistico incompleto, quindi contribuire e' possibile.

L'opzione B e' un tool software su PC che legge un dump del salvataggio di generazione 1 o 2, applica la conversione e scrive un salvataggio di generazione 3. Richiede un lettore di cartucce per ottenere e riscrivere i dump, che il progetto ha gia' per il track Smeraldo, e non richiede ne' cavo Link ne' multiboot ne' scambio a caldo. E' la piu' semplice da collaudare e la piu' lontana dal vincolo del solo hardware originale, perche' il trasferimento avviene su un computer.

L'opzione C e' riprodurre il ponte hardware da zero, con la propria implementazione sia del lato che esegue codice sul Game Boy sia del programma ricevente sulla GBA. E' la piu' impegnativa e la piu' istruttiva, richiede la toolchain devkitARM, la conoscenza dell'assembly del Game Boy per il payload e hardware fisico per ogni prova del passaggio finale.

L'opzione D e' un dispositivo intermedio su microcontrollore che parla il protocollo seriale del Game Boy da un lato e comunica con un computer dall'altro. Il precedente piu' vicino e' `PkSploit`, che con un Arduino ottiene lettura e scrittura della SRAM passando dal cavo, e questa opzione ha una proprieta' interessante: eliminerebbe la necessita' di un lettore di cartucce, perche' il canale di accesso diventa il connettore del cavo.

## Come le tre novita' di quest'anno spostano il calcolo

La stratificazione descritta in [[20-architettura-codice]] mostra che gli strati dal primo al quarto sono identici in tutte e quattro le opzioni. Cambia solo il quinto, il trasporto. Questo e' il primo fatto che sposta il calcolo, e sposta anche l'ordine: non c'e' motivo di attendere la decisione per cominciare, perche' la maggior parte del lavoro non dipende da essa.

Il secondo e' che la conversione fedele delle statistiche non esiste in nessuna implementazione pubblica, perche' il PCCS documenta quattro metodi e ne implementa uno. Se la fedelta' e' un obiettivo, quel pezzo va scritto in ogni caso, anche scegliendo l'opzione A, che quindi non e' piu' la strada a costo zero di sviluppo che sembrava.

Il terzo e' che il protocollo del cavo si collauda su BGB via TCP, come spiegato in [[21-collaudo]]. Le opzioni C e D restano le sole che richiedono ferro per il passaggio finale, ma il loro strato di protocollo non e' piu' bloccato dalla disponibilita' di hardware.

## La sequenza che ne consegue

Non e' una decisione, e' un ordine di lavoro che resta valido qualunque decisione arrivi. Prima si costruiscono i dati generati e i tre lettori e scrittori, collaudandoli con la prova di simmetria descritta in [[21-collaudo]], perche' questo e' il lavoro comune e non richiede nulla. Poi si scrive la conversione con le sue politiche esplicite, che e' il pezzo che nessuno regala. Poi, in parallelo alla discovery hardware, si implementa il protocollo del cavo contro BGB. Solo a quel punto la scelta fra le quattro opzioni diventa una scelta su come chiudere l'ultimo tratto, e la si prende sapendo che cosa costa invece di stimandolo.

## Cosa leggere dopo

[[31-glossario]] per i termini, e la referenza byte per byte e' [[DATA-FORMATS_Gen1-Gen2-Gen3]].
