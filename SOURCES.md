# Registro delle fonti

Questo file è il registro unico delle fonti tecniche del progetto, condiviso da tutti i sottoprogetti. Nasce dal lavoro sul ponte fra generazioni, che è il track che ha richiesto la ricerca più profonda, ma non gli appartiene: i disassemblati dei giochi, la documentazione dell'hardware, i formati di salvataggio e gli editor servono anche alla correzione dell'inventario di Smeraldo, al modding del 3DS e allo scambio con la Switch, e tenerli in un posto solo evita che ogni handoff riscopra le stesse cose.

## Due file, due scopi

Questo è il registro: elenca, dice a cosa serve ciascuna voce e a quale sottoprogetto, e vale come inventario. Non dice perché una fonte è stata salvata né come si lega alle altre, perché una tabella non produce un grafo.

Quella parte sta in `docs/fonti/`, dove ogni fonte che porta peso tecnico ha una nota con il suo abstract, il motivo per cui è in archivio, il punto esatto del progetto che serve e le relazioni verso le altre fonti. L'indice è `docs/fonti/index-fonti.md`, e aprendo la radice del repository come vault Obsidian quelle relazioni diventano un grafo navigabile. Le note sono generate da `tools/build-source-map.py` a partire da una tabella unica: si modifica la tabella, non le note.

Da qui discende una regola che vale come vincolo e non come preferenza: questo file è l'unica fonte di verità sulle fonti, e nessuna informazione su una fonte vive soltanto altrove. La cartella locale `_notes/fonti/`, che git ignora, è una cache di materiale grezzo e non un archivio: contiene i collegamenti che l'utente salva mentre naviga e i testi che procura quando il recupero automatico non funziona, cioè trascrizioni di video, pagine salvate, porzioni di discussione copiate a mano. Ciò che quel materiale documenta viene letto e trasferito qui in prosa, con la profondità necessaria a poterlo citare senza riaprirlo, e da quel momento il file grezzo è sacrificabile. Non si cancella per igiene, si cancella perché non porta più informazione che non sia scritta qui. Il materiale grezzo resta comunque fuori dal repository, per volume e perché è contenuto di terzi: ciò che entra nel version control è la sintesi con l'attribuzione, non la copia.

## Come si usa

Ogni voce dichiara che cosa la fonte documenta in modo autorevole, non solo che esiste, perché il valore di una fonte sta in ciò su cui la si può citare. La colonna dei track usa le sigle BRI per il ponte fra generazioni, SME per la correzione del salvataggio di Smeraldo, 3DS per il modding della console e il dump delle cartucce, LDN per lo scambio fra GBA e Switch, AUT per lo studio dell'automazione su Switch, EVT per la ricreazione delle distribuzioni di eventi, ACE per l'esecuzione di codice come via di generazione, GEN per la generazione e lo scambio dai giochi su console moderna, BAT per la conservazione del supporto e la sostituzione della batteria tampone, PKD per il completamento del Pokedex nel deposito, e TUTTI quando serve trasversalmente.

Le fonti sono ordinate per affidabilità decrescente, e l'ordine è normativo quando due fonti si contraddicono. Il livello 1 è il codice del gioco e la documentazione dell'hardware ricostruita e verificata dalla community: è la verità operativa. Il livello 2 è la documentazione di dominio, wiki e riferimenti, accurata ma non infallibile. Il livello 3 sono le implementazioni di riferimento, cioè codice di terzi che funziona sul campo e quindi incorpora conoscenza verificata dall'uso, ma anche scelte arbitrarie che non vanno confuse con specifiche. Il livello 4 sono articoli, blog e video, preziosi per capire il perché e inaffidabili per gli offset. Il livello 5 sono forum e community, che rispondono a domande senza risposta scritta e non sono citabili finché non si verifica.

La gerarchia non è un formalismo, e vale la pena registrare cosa ha prodotto in concreto durante la stesura di `pokemon-gen12-gen3-bridge-original-hardware/DATA-FORMATS_Gen1-Gen2-Gen3.md`. Il livello 2 sbagliava la tabella caratteri di generazione 1, collocando le cifre a 0xF0 invece di 0xF6, e quella di generazione 3, collocando le maiuscole a 0xC1 invece di 0xBB. Sbagliava il calcolo del checksum di generazione 3, descrivendolo byte per byte invece che per parole da 16 bit, che è un errore capace di distruggere un Pokemon. Dava due cifre in conflitto sulla dimensione del blocco di scambio, 415 e 424, mentre la somma di costanti nel disassemblato dice 424 sul filo e 418 di dati. E il livello 3 si è rivelato in disaccordo con la propria documentazione, perché il PCCS documenta quattro metodi di conversione nel README e nel codice ne implementa uno. In tutti i casi ha vinto il livello 1.

Quando una sessione futura trova una fonte nuova che serve, la aggiunge qui con la sua riga e la sua colonna dei track, invece di lasciarla dentro il proprio handoff: gli handoff citano il registro, il registro non duplica gli handoff.

Nota operativa sul recupero automatico, che serve a non ripetere tentativi inutili. I file grezzi di GitHub e le pagine di Bulbapedia si recuperano bene, e per i repository conviene comunque un clone superficiale con `git clone --depth 1`, perché permette di cercare nel codice invece di leggere riassunti. Il dominio `glitchcity.wiki` respinge le richieste automatiche con un errore 403 e va letto dal mirror statico di Ninty Conservation o a mano dal browser. YouTube restituisce una pagina di consenso invece del contenuto, quindi i canali sono identificati per URL ma i video non sono stati guardati.

Su Reddit la situazione è cambiata il 2026-09-07 e va detta con precisione, perché per due settimane questo paragrafo ha detto il contrario. Reddit resta una fonte tecnica di prima qualità, e per un certo tempo il progetto l'ha catalogata senza leggerla: il crawler del modello è bloccato a livello di dominio, le sei vie tentate fallivano tutte, e la sesta falliva nel modo peggiore, cioè restituendo un codice duecento con una pagina di verifica anti-bot al posto del contenuto, che è un successo apparente e inganna più di un rifiuto. L'errore di ragionamento che teneva chiusa la questione era che quelle sei vie chiedevano tutte il contenuto a Reddit, quindi non erano sei vie diverse ma la stessa via ripetuta.

La via che funziona cambia il capo invece del tragitto ed è l'archivio pubblico Arctic Shift, successore di Pushshift, che conserva una copia dei contenuti pubblici di Reddit e ne pubblica di propria iniziativa un'interfaccia programmatica documentata senza credenziali. Lo strumento è `tools/fetch-reddit.py`, che non legge un post soltanto ma attraversa in ampiezza il grafo dei rinvii che parte da esso, perché un post di raccolta è un indice e non un documento. La diagnosi completa delle vie, il criterio che separa quelle legittime da quelle vietate e la tecnica in due passi per i collegamenti di condivisione stanno in `.claude/rules/web-sources-not-fetchable.md`. Le voci Reddit di questo registro ancora marcate come non lette lo sono per debito di lettura nostro e non per indisponibilità, che è una differenza sostanziale: si chiudono lanciando lo strumento.

Sulle condizioni dell'API ufficiale, che resta la via preferibile il giorno in cui fosse concessa, il progetto ha verificato direttamente la documentazione il 2026-08-26, e vale registrare cosa dice perché correggeva una supposizione. L'uso gratuito esiste e non richiede alcuna approvazione preventiva per il caso non commerciale: il modulo di contatto che la pagina cita serve alle richieste commerciali, aziendali, accademiche o di superamento dei limiti, non alla registrazione di un'applicazione di tipo script. Il limite è di cento richieste al minuto per identificativo di client, mediato su dieci minuti così da tollerare le raffiche, e va osservato leggendo le intestazioni di risposta. È obbligatorio autenticarsi con un token e dichiarare uno user agent descrittivo, perché quelli generici delle librerie sono deliberatamente limitati. C'è infine un obbligo che riguarda noi come archivio e non come lettori, e che vale anche per la via dell'archivio pubblico: il contenuto cancellato va rimosso anche dalle copie in proprio possesso, il che è la ragione per cui l'identificativo dell'autore viaggia accanto al contenuto e per cui qui sta la sintesi con l'attribuzione e non la copia.

## La struttura di questo file

Questa sezione descrive il file a chi lo apre per la prima volta, e serve perché un registro di trecento voci senza una mappa si legge cercando con il ricerca-testo invece che navigando, il che funziona solo per chi già sa che cosa cercare.

Il corpo del registro sono cinque livelli di affidabilità decrescente, e la loro numerazione è normativa e non decorativa: quando due fonti si contraddicono ha ragione quella di livello più basso, e la sezione precedente elenca i casi concreti in cui questa regola ha impedito di scrivere codice sbagliato.

| Sezione | Che cosa contiene | Quando la si cita |
|---|---|---|
| Livello 1 | disassemblati, decompilazioni e documentazione dell'hardware ricostruita e verificata dalla community | sempre, ed è l'unico livello su cui un'affermazione di formato si può dare per stabilita senza altra conferma |
| Livello 2 | wiki e riferimenti di dominio | per orientarsi e per il contesto storico; su un offset, un byte o una formula va confermato al livello 1 |
| Livello 3 | implementazioni di riferimento, cioè codice di terzi che funziona sul campo | per ciò che il codice fa davvero; le sue scelte arbitrarie non sono specifiche e non vanno citate come tali |
| Livello 4 | articoli, blog e ricerca applicata | per il perché di una cosa, mai per il come |
| Livello 5 | forum e community | per le domande che non hanno una risposta scritta altrove; una risposta in un thread non è una fonte finché non è verificata |

Attorno ai cinque livelli stanno quattro sezioni che non sono un sesto livello ma un taglio diverso dello stesso materiale, e vale dire quale.

La sezione sul corpus della collezione raccoglie le milleduecentonovantanove fonti che discendono da un solo post di raccolta, e si legge in due parti: le centosettantuno che il post cita direttamente, ordinate per argomento e con un livello ciascuna, e le millecentoventotto che il grafo ha trovato dentro i post rinviati, ordinate per host e senza livello perché nessuno le ha ancora lette. La prima parte è ordinata per argomento invece che per affidabilità, perché quel corpus porta già la propria tassonomia e conservarla lo tiene confrontabile con la fonte; il livello di ciascuna voce non si perde e sta in una colonna. La sezione dei canali e dei video raccoglie le fonti in forma parlata, che si citano soltanto attraverso la loro trascrizione: il video non è la fonte, la trascrizione lo è, e finché non esiste la voce vale come indicazione di dove guardare. La sezione delle fonti operative dei track su hardware fisico raccoglie ciò che serve a un runbook e non a un'argomentazione, cioè manuali, procedure e schede di prodotto, tenute separate perché il criterio di affidabilità che governa i cinque livelli non si applica a un manuale del produttore. La sezione su che cosa è stato usato davvero è il presidio contro il difetto tipico di un registro che cresce, cioè sembrare consultato quando è soltanto catalogato: separa le voci lette da quelle registrate come luoghi dove cercare, e una voce non letta lo dichiara nella propria riga con il motivo.

Chiude il file la sezione su ciò che non entra qui, che esiste per la ragione opposta e altrettanto importante: un registro che non dichiara i propri confini induce a credere che ciò che non contiene non esista.

Ogni riga porta quattro cose e la quarta è quella che si dimentica: il luogo, l'indirizzo, che cosa la fonte documenta in modo autorevole, e le sigle dei track che serve. La terza colonna non dice che la fonte esiste ma su che cosa la si può citare, ed è la differenza fra un elenco di collegamenti e un registro utilizzabile. Le sigle sono elencate nella sezione precedente e vanno messe tutte, perché una fonte senza track è una fonte che nessuna sessione futura ritroverà quando le servirà.

Sul rapporto fra questo file e il resto del progetto valgono due direzioni obbligate, e sono la ragione per cui il registro non è un archivio morto. Ogni fonte che entra qui e che porta peso su un'affermazione va poi citata nel punto o nei punti del progetto dove quell'affermazione vive, cioè nel documento di track, nella nota di studio o nel capitolo della tesi che la impiega: una fonte registrata e mai citata non sta corroborando nulla. E ogni affermazione scritta in un documento di progetto va accompagnata dalla fonte da cui è corroborata, il che è il vincolo speculare e il più facile da violare, perché una frase senza fonte non produce alcun errore visibile finché qualcuno non prova a verificarla.

## Le fonti sul vincolo delle macchine nascoste, consegnate il 2026-09-09

Nascono da una ricerca che l'utente ha condotto in un'altra sessione e consegnato come handoff. Il vincolo in sé il progetto lo aveva già, con la sua misura sul lotto di quarta generazione; queste fonti lo corroborano per vie indipendenti e portano la parte che mancava, cioè perché la mossa non si possa cancellare e quale via resti. L'assorbimento sta in `pokedex-home-completo/CATENA-DI-TRASFERIMENTO.md` e la misura in `MOSSE-MN.md`; il file dell'handoff è stato eliminato dopo l'assorbimento, come l'utente ha chiesto.

| Fonte | URL | Autorevole su | Track |
|---|---|---|---|
| Parco Amico, Pokemon Central Wiki | https://wiki.pokemoncentral.it/Parco_Amici | il rifiuto categorico degli esemplari che conoscono una macchina nascosta nel gioco d'origine; corrobora in italiano ciò che Bulbapedia dava dal 2026-08-28 | PKD, EVT |
| Scambio, Pokemon Central Wiki | https://wiki.pokemoncentral.it/Scambio | il Parco Amico come unico mezzo fra terza e quarta generazione | PKD |
| Trasferimento, Pokemon Central Wiki | https://wiki.pokemoncentral.it/Trasferimento | come il deposito tratta gli insiemi di mosse fra ambienti di gioco diversi | PKD |
| Pokemon HOME, Pokemon Central Wiki | https://m.wiki.pokemoncentral.it/Pok%C3%A9mon_HOME | i passaggi dalla banca e dal gioco per telefono verso il deposito | PKD |
| Pocket Monsters Stadium, Wikipedia | https://en.wikipedia.org/wiki/Pocket_Monsters_Stadium | che Surf su Pikachu è un premio di torneo di Stadium e che la specie non lo apprende altrimenti | EVT |
| Waxing Nostalgic About Surfing Pikachu, pokemon.com | https://www.pokemon.com/us/pokemon-news/waxing-nostalgic-about-surfing-pikachu | la storia del Pikachu surfista, dal titolare della serie | EVT |
| Dalla Tempocapsula a Pokemon HOME, Pokemon Millennium | https://www.pokemonmillennium.net/rubriche/184574-dalla-tempocapsula-a-pokemon-home-la-guida-completa-ai-passaggi-tra-generazioni/ | la guida ai passaggi fra generazioni, con gli aggiramenti esistenti e la loro assenza per Surf | PKD |
| Macchina nascosta, Bulbapedia | https://bulbapedia.bulbagarden.net/wiki/HM | quali mosse siano macchine nascoste in ciascuna generazione, che è la tavola su cui `tools/mosse-mn.py` poggia il controllo | PKD, EVT |

## Livello 1: disassemblati, decompilazioni e documentazione dell'hardware

Sono la fonte autorevole su ogni offset, ogni campo di bit, ogni formula e ogni tabella. Un dato letto qui non ha bisogno di conferma; un dato che li contraddice è sbagliato.

| Fonte | URL | Autorevole su | Track |
|---|---|---|---|
| 3dbrew, DISA e DIFF | https://www.3dbrew.org/wiki/DISA_and_DIFF | letto il 2026-09-04 con una richiesta locale, dopo che lo strumento di sessione aveva ricevuto un rifiuto: è la documentazione del contenitore dentro cui vive un salvataggio 3DS, ed è la fonte che chiude una questione aperta del track del Pokedex. Il valore di sicurezza esiste ed è documentato, ma non sta dove il progetto aveva ipotizzato: sta nell'intestazione del contenitore DISA, che riserva quattro voci da dodici byte a partire da 0x8C, ciascuna con un numero di posizione a trentadue bit e un valore a sessantaquattro, e dichiara a 0x69 quante ne siano in uso. Ne segue il fatto che cambia la diagnosi: il valore di sicurezza non è dentro il file `main`, quindi sostituire quel file non lo tocca, e la firma CMAC che protegge il contenitore è calcolata con una chiave che dipende dal supporto, cioè 0x19 e 0x33 per una cartuccia e 0x30 per la scheda | 3DS, PKD |
| pret/pokered | https://github.com/pret/pokered | strutture, salvataggio, protocollo di scambio e costanti seriali di Rosso e Blu; `macros/ram.asm`, `ram/wram.asm`, `constants/serial_constants.asm`, `engine/link/cable_club.asm` | BRI |
| pret/pokeyellow | https://github.com/pret/pokeyellow | clonato e confrontato il 2026-08-25: la macro `box_struct` e le costanti di lunghezza sono identiche a quelle di Rosso e Blu, quindi il parser di generazione 1 copre Giallo senza modifiche. Risultato negativo e utile | BRI |
| pret/pokegold | https://github.com/pret/pokegold | clonato e confrontato il 2026-08-25: la macro `party_struct` è identica a quella di Cristallo, quindi il parser di generazione 2 copre Oro e Argento senza modifiche. Restano diversi gli offset del salvataggio, che erano già registrati | BRI |
| pret/pokecrystal | https://github.com/pret/pokecrystal | ordine dei nibble dei DV in `engine/pokemon/move_mon.asm`, tabella caratteri in `constants/charmap.asm`, strutture di invio native e Time Capsule in `ram/wram.asm` | BRI |
| pret/pokeruby | https://github.com/pret/pokeruby | clonato e letto: nessuna chiave di cifratura, quindi nessuna maschera sulle quantità; conteggio squadra a 0x234, denaro a 0x490, tasche a 0x498, 0x560, 0x5B0, 0x600, 0x640 e 0x740 con capienze 50, 20, 20, 16, 64 e 46, e 349 oggetti. Tutti i valori che il nostro strumento già usava sono confermati | BRI, SME |
| pret/pokeemerald | https://github.com/pret/pokeemerald | struttura cifrata Gen 3 e checksum in `src/pokemon.c`, chiave di cifratura e offset dello zaino in `include/global.h`, maschera delle quantità in `src/item.c`, settori del salvataggio in `include/save.h` e `src/save.c` | BRI, SME |
| pret/pokefirered | https://github.com/pret/pokefirered | clonato e letto: chiave di cifratura a 0xF20 dentro un SaveBlock2 che misura 0xF24, e non a 0x0AF8 come riporta una fonte secondaria; conteggio squadra a 0x34, denaro a 0x290, tasche a 0x298, 0x310, 0x3B8, 0x430, 0x464 e 0x54C con capienze 30, 42, 30, 13, 58 e 43, e 375 oggetti in tutto | BRI, LDN, SME |
| Documentazione pokeemerald | https://pret-pokeemerald.mintlify.app/ | guida navigabile alla decompilazione di Smeraldo, comoda per orientarsi prima di aprire il sorgente | BRI, SME |
| Pan Docs | https://gbdev.io/pandocs/ | riferimento tecnico completo dell'hardware Game Boy, compreso il trasferimento seriale via cavo Link | BRI |
| Pan Docs, sorgente | https://github.com/gbdev/pandocs | la stessa cosa in Markdown, diffabile e citabile per revisione | BRI |
| GBATEK | https://problemkaputt.de/gbatek.htm | riferimento tecnico dell'hardware Game Boy Advance | BRI, SME, LDN |
| GBATEK, multiboot | https://problemkaputt.de/gbatek-bios-multi-boot-single-game-pak.htm | protocollo di avvio di un programma in RAM ricevuto dal cavo, cioè il meccanismo su cui poggia il ponte | BRI |
| GBATEK, porte di comunicazione | https://problemkaputt.de/gbatek-gba-communication-ports.htm | modalità normale, multiplayer, UART e JOY Bus della porta seriale GBA | BRI, LDN |
| Pan Docs, trasferimento seriale | https://gbdev.io/pandocs/Serial_Data_Transfer_(Link_Cable).html | letto: registri SB a 0xFF01 e SC a 0xFF02 con i loro bit, clock interno 8192 Hz su Game Boy e fino a 524288 Hz su Color, clock esterno accettato fino a 500 kHz e senza limite inferiore, necessità di un timeout perché con clock esterno il trasferimento non termina mai da solo. Blocca il crawler del modello, si scarica con `curl` locale | BRI |
| GBATEK, multiboot | https://problemkaputt.de/gbatek-bios-multi-boot-single-game-pak.htm | letto: sequenza di handshake con 0x6200 e risposta 0x0000, poi 0x610y e 0x720x; lunghezza del trasferimento multipla di 0x10 fra 0x100 e 0x3FF40; intestazione a 0x2000000 e programma da 0x20000C0 a 0x203FFFF; indirizzi assoluti da riferire a 0x2000000 e non a 0x8000000; XOR e checksum CRC a 16 bit; attesa del bit di start e ritardo di 36 microsecondi dopo ogni trasferimento | BRI |
| Copetti, architettura del Game Boy Advance | https://www.copetti.org/writings/consoles/game-boy-advance/ | letto: IWRAM 32 KB a 32 bit e EWRAM 256 KB a 16 bit fino a sei volte più lenta, bus cartuccia a 16 bit con 24 linee di indirizzo, buffer di prefetch da otto parole, retrocompatibilità Game Boy con rilevamento della forma della cartuccia e commutazione di tensione | BRI |
| rgbds | https://github.com/gbdev/rgbds | assemblatore necessario per compilare i disassemblati Game Boy | BRI |
| devkitPro e libtonc | https://github.com/devkitPro/libtonc | toolchain e libreria C per compilare homebrew GBA | BRI |
| Bulbapedia, distribuzioni italiane Gen 3 | https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III | letta il 2026-08-29: luogo, date e campi delle distribuzioni italiane. La manifestazione del 2006 in un parco di divertimenti, dal 23 al 25 giugno, ha allenatore di provenienza `10ANNI`, identificativo 06227, dieci specie al livello 70, e il partecipante poteva scegliere tre esemplari; quella del 2007 nel medesimo luogo distribuiva un Mew di allenatore `Aura` e identificativo 20078. È la fonte che identifica con precisione gli esemplari che l'utente possiede da quell'evento | EVT |
| Pokemon, collegamento di Rosso Fuoco e Verde Foglia con Home | https://www.pokemon.com/us/news/pokemon-firered-version-and-pokemon-leafgreen-version-link-with-pokemon-home | annuncio ufficiale del 13 agosto 2026, letto il 2026-08-31 attraverso la sintesi dei risultati di ricerca: le versioni per console moderna di quei due giochi si collegheranno a Pokemon Home a ottobre 2026, con l'aggiornamento 4.1.0 del servizio, e da quel momento un esemplare potrà entrare in Home direttamente senza passare da Bank. Il trasferimento è a senso unico, cioè un esemplare che lascia quei giochi non può rientrarvi e nessun esemplare di altri giochi può visitarli; la capienza del piano a pagamento sale da seimila a novemila; chi completa il registro riceve un Celebi. È la fonte che corregge la scadenza del progetto: per la terza generazione il 26 febbraio 2027 cessa di essere l'ultima porta, mentre resta l'ultima per prima, seconda, quarta e quinta generazione | ACE, EVT, LDN, 3DS |
| Pokemon, gestione dei dati alterati | https://support.pokemon.com/hc/en-us/articles/360055828671-Addressing-the-use-of-data-altered-via-unauthorized-means | politica ufficiale, letta il 2026-08-31 attraverso la sintesi dei risultati di ricerca. È l'unico elemento non congetturale sul rischio dei track che producono esemplari: chi risulti impiegare dati alterati può subire la restrizione del gioco in linea, la restrizione delle funzioni di scambio nella versione mobile e la sospensione di Pokemon Home nelle versioni per console e mobile, in forma temporanea o indefinita a discrezione del titolare e senza rimborso. Dichiara una eccezione che delimita il rischio e che non va letta come una assoluzione: non vi sono restrizioni per chi possieda dati alterati senza intenzione, per esempio ricevendoli in uno scambio senza saperlo | ACE, GEN, EVT |
| Nintendo, fine del servizio di Pokemon Bank | https://en-americas-support.nintendo.com/app/answers/detail/a_id/61543 | letta il 2026-08-28 ed è la fonte ufficiale della scadenza esterna del progetto: Pokemon Bank chiude giovedì 25 febbraio 2027 alle 19:00 PST, cioè il 26 febbraio alle 12:00 JST, e con esso cessa il trasferimento verso Pokemon Home. Nintendo dice di spostare prima ciò che si vuole conservare e non annuncia alcuna tolleranza. Va citata questa e non la stampa specializzata, perché la data governa una pianificazione | EVT, 3DS |
| Pokemon, il deposito intermedio diventa gratuito | https://www.pokemon.com/us/news/pokemon-bank-services-will-be-available-at-no-cost-to-players | indicata dall'utente e letta il 2026-09-03, ed è la fonte che chiude un falso problema che il progetto si era creato. Quando il negozio digitale della console è stato chiuso, il servizio è stato reso gratuito, e chi lo pubblica ha avvisato in anticipo del comportamento che ne consegue: i giocatori avrebbero visto la dicitura del periodo di prova gratuito seguita da un numero fra zero e novantanove, e quella riga va ignorata perché nessuna data di fine era prevista per il servizio gratuito. Nel marzo 2023 la medesima avvertenza è stata ripetuta. Serve al progetto per una ragione precisa: il 2026-09-03 quel numero era stato letto su una fotografia con la prima cifra illeggibile ed era stata aperta una voce di verifica per recuperarla, cioè una verifica su una stringa priva di significato. La scadenza vera resta quella della riga di Nintendo qui sopra, che il registro portava già dal 2026-08-28 | PKD, EVT, 3DS |
| Bulbapedia, Pokemon Bank | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Bank | letta il 2026-08-28: Poke Transporter accetta come sorgente soltanto i giochi di quinta generazione e le riedizioni su Virtual Console di prima e seconda, quindi la terza generazione non entra in Bank direttamente. Conferma la data di chiusura e che Bank e Transporter erano gli ultimi software 3DS con funzioni in linea dopo il 9 aprile 2024 | EVT, 3DS |
| Bulbapedia, distribuzioni da gioco in prima generazione | https://bulbapedia.bulbagarden.net/wiki/List_of_game-based_Pok%C3%A9mon_distributions_in_Generation_I | letta il 2026-09-03 e usata come controllo incrociato sui premi di Pokemon Stadium, con esito di accordo pieno sui nove esemplari, i loro livelli, le loro mosse, il nome dell'allenatore e l'identificativo. Porta due fatti che la tabella tecnica non dichiara: gli otto premi erano estratti a sorte uno per vittoria sul Castello dei Capipalestra, mentre il Psyduck era il premio del Pokedex completo, cioè dell'albo riempito con tutte e centocinquantuno le specie. E conferma in modo indipendente la scoperta che il byte del tasso di cattura porta l'identificativo della Scatola Normale o della Scatola Splendida: la fonte la chiama confezione del primo e del secondo giro, dove noi l'avevamo letta come un valore fisso richiesto dal verificatore | EVT, PKD |
| Bulbapedia, distribuzioni da gioco in seconda generazione | https://bulbapedia.bulbagarden.net/wiki/List_of_game-based_Pok%C3%A9mon_distributions_in_Generation_II | letta il 2026-09-03 sui due premi di Pokemon Stadium 2, e ha corretto un mio errore: la specie duecentosette è Gligar e non Sunkern, e lo avevo affermato a memoria invece di leggere la tabella dei nomi. Segnala che la mossa notevole è Staffetta sul Farfetch'd, indisponibile a quella specie in seconda generazione, mentre Terremoto sul Gligar era soltanto distribuito di rado. Divergenza registrata: attribuisce al Gligar quattro mosse contro le tre della tabella tecnica, aggiungendo Velenospina | EVT, PKD |
| Bulbapedia, distribuzioni in lingue europee in prima generazione | https://bulbapedia.bulbagarden.net/wiki/List_of_European_language_event_Pok%C3%A9mon_distributions_in_Generation_I | letta il 2026-09-03, ed è la fonte che ha scomposto un gruppo tecnico in una dozzina di eventi storici. La tabella del verificatore chiama tour europeo un tipo che accetta diciannove nomi di allenatore; questa pagina mostra che quei nomi appartengono a distribuzioni su tre continenti fra il novembre 1999 e la primavera 2001, cioè negozi di giocattoli statunitensi e canadesi, la rivista ufficiale, il tour degli stadi negli Stati Uniti dal 5 febbraio al 9 aprile 2000, la sua tappa canadese, e poi eventi nazionali in Svezia, Norvegia, Finlandia, Danimarca, Austria, Regno Unito e Irlanda. Conferma inoltre i valori individuali fissati, cioè cinque punti salute, dieci attacco, uno difesa, dodici velocità e cinque speciale, che è la conferma indipendente della lettura corretta di quei sei numeri. Riporta anche una distribuzione spagnola con valori individuali diversi che la tabella tecnica non copre | EVT, PKD |
| Bulbapedia, distribuzioni giapponesi in prima generazione | https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_I | letta il 2026-09-03: conferma le tre manifestazioni che stanno dentro un solo tipo di donatore e ne dà le tappe una per una, cioè Fukuoka il 7 dicembre 1997, Chiba il 10 e 11 gennaio 1998, Osaka il primo febbraio, Sapporo l'8 e Nagoya il 15, oltre allo Space World del 22-24 novembre 1997 al Makuhari Messe. Conferma i medesimi valori individuali fissati del gruppo internazionale. Non elenca il nome Makuhari fra quelli della coppa itinerante, che è la ragione per cui l'attribuzione di quel nome allo Space World del 1999 si può scrivere invece di essere supposta | EVT, PKD |
| Bulbapedia, distribuzioni del Pokemon Center di New York in seconda generazione | https://bulbapedia.bulbagarden.net/wiki/List_of_PCNY_event_Pok%C3%A9mon_distributions_in_Generation_II | letta il 2026-09-03, e ha trasformato una nostra congettura in un fatto. La tabella tecnica ammette quattro nomi di allenatore da PCNYa a PCNYd e noi avevamo scritto che fossero quattro postazioni oppure quattro periodi: al secondo piano del negozio, aperto il 16 novembre 2001, c'era una postazione con quattro macchine distributrici, e i quattro nomi sono le quattro macchine. Porta due fatti che cambiano come si leggono i nostri dati: tutti gli esemplari tranne gli evoluti, i leggendari e i mitici erano consegnati come uova, e ciascuna distribuzione aveva una probabilità del quindici per cento di essere cromatica salvo dichiarazione contraria, quindi le voci non marcate come cromatiche potevano esserlo e la nostra scelta di produrle non cromatiche è una fra due legittime | EVT, PKD |
| Bulbapedia, distribuzioni giapponesi in seconda generazione | https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_(Generation_II) | letta il 2026-09-03, ed è la fonte che ha chiuso l'ultimo gruppo di prima e seconda generazione senza provenienza. Le quindici voci che la tabella tecnica classifica come consegnate al destinatario, senza nome né data né luogo, sono le uova misteriose distribuite nei negozi Pokemon Center di Tokyo e Osaka in tre campagne, cioè dal 15 dicembre 2001 al 14 gennaio 2002, dal 16 marzo al 7 aprile 2002 e dal 27 aprile al 12 maggio 2002. La conferma non poggia sul nome ma sul conto e sulle mosse, che coincidono voce per voce, e il marcatore che separa le campagne è Petalodanza, assegnata dalla seconda a quasi tutte le proprie uova. Due voci coprono due consegne storiche ciascuna, perché coincidono nei byte | EVT, PKD |
| Bulbapedia, Parco Amico | https://bulbapedia.bulbagarden.net/wiki/Pal_Park | letta il 2026-08-28: il passaggio dalla terza alla quarta generazione richiede un Nintendo DS o DS Lite, cioè una console con lo slot per le cartucce Game Boy Advance, con i due giochi nella stessa lingua; sei esemplari per volta, non più di sei ogni ventiquattro ore in Diamante, Perla e Platino mentre HeartGold e SoulSilver rimuovono il limite, e nessun esemplare che conosca una mossa macchina nascosta | EVT, 3DS |
| Bulbapedia, Trasferitore | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Transfer | letta il 2026-08-28: il passaggio dalla quarta alla quinta generazione usa la comunicazione fra due console della famiglia DS, richiede il Pokedex nazionale e la storia completata sul gioco di destinazione, sposta sei esemplari per volta senza limite giornaliero, rifiuta uova e mosse macchina nascoste, e lascia indietro gli oggetti tenuti. Come il Parco Amico è irreversibile | EVT, 3DS |
| Discord, account automatizzati e self-bot | https://support.discord.com/hc/en-us/articles/115002192352-Automated-User-Accounts-Self-Bots | non aperta in sessione: il suo contenuto è riportato dalla consegna letta il 2026-08-31 e coincide con la decisione che il progetto aveva già preso il 2026-08-26. Distingue i bot account, descritti come dedicati all'automazione e autenticati con un token proprio, dai self-bot, cioè l'automazione di un account utente normale, dichiarata vietata con rischio di terminazione dell'account. È la fonte del criterio di ADR-018 e va aperta prima di citarla su un dettaglio | TUTTI |
| Discord, Channel Following FAQ | https://support.discord.com/hc/en-us/articles/360028384531-Channel-Following-FAQ | letta il 2026-08-31 attraverso la sintesi dei risultati di ricerca sulla pagina ufficiale, non aprendo la pagina. Documenta la sola via che non richiede il consenso del server di origine: i canali di annunci di un server community si possono seguire da un altro server, con replica dei messaggi pubblicati, e il permesso necessario è quello di gestire i webhook nel server di destinazione. Il limite è che riguarda i soli canali di annunci e non le discussioni, dove sta la conoscenza tecnica | TUTTI |
| 3dbrew | https://www.3dbrew.org | documentazione tecnica dell'hardware e del software di sistema del 3DS, compreso il formato dei salvataggi | 3DS |

## Livello 2: wiki e riferimenti di dominio

Vale la pena elencare le pagine singole e non solo i domini, perché una wiki grande è inutilizzabile come citazione mentre una pagina precisa è una fonte.

| Fonte | URL | Autorevole su | Track |
|---|---|---|---|
| Bulbapedia, struttura dati Gen 1 | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_I) | offset dei 44 e 33 byte, impaccamento dei PP | BRI |
| Bulbapedia, struttura dati Gen 2 | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_II) | offset dei 48 e 32 byte, dati di cattura di Cristallo, Pokerus | BRI |
| Bulbapedia, struttura dati Gen 3 | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_III) | intestazione in chiaro ed estensione di squadra | BRI, SME, LDN |
| Bulbapedia, sottostrutture Gen 3 | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_substructures_(Generation_III) | tabella delle 24 permutazioni e campi di bit delle quattro sottostrutture | BRI, SME, LDN |
| Bulbapedia, salvataggio Gen 1 | https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_I) | banchi, offset di squadra e box, checksum | BRI |
| Bulbapedia, salvataggio Gen 2 | https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_II) | offset per gioco e lingua, doppio checksum, copia di backup | BRI |
| Bulbapedia, salvataggio Gen 3 | https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_III) | sezioni da 4096 byte, firma, scelta dello slot | SME, BRI, LDN |
| Bulbapedia, valore di personalità | https://bulbapedia.bulbagarden.net/wiki/Personality_value | formule di natura, sesso, abilità, lucentezza, lettera di Unown | BRI |
| Bulbapedia, valori individuali | https://bulbapedia.bulbagarden.net/wiki/Individual_values | derivazione del DV dei punti salute, lucentezza da DV in Gen 2 | BRI |
| Bulbapedia, codifica caratteri Gen 1 | https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_I) | tabella caratteri; sbagliata sulle cifre, usare il charmap del disassemblato | BRI |
| Bulbapedia, codifica caratteri Gen 3 | https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_III) | codici di controllo 0xFC, 0xFD e 0xFE; sbagliata sulle maiuscole | BRI, SME |
| Bulbapedia, indici Gen 1 | https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_index_number_(Generation_I) | mappatura da indice interno a numero nazionale e posizioni di MissingNo | BRI |
| Bulbapedia, indici Gen 3 | https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_index_number_(Generation_III) | numerazione interna e ordinamento delle specie di Hoenn | BRI |
| Bulbapedia, esecuzione di codice arbitrario | https://bulbapedia.bulbagarden.net/wiki/Arbitrary_code_execution | inquadramento enciclopedico della tecnica e della sua storia | BRI |
| Glitch City Wiki | https://glitchcity.wiki | catalogo dell'esecuzione di codice arbitrario e dei glitch di Gen 1 e 2; respinge il recupero automatico | BRI |
| Glitch City, mirror statico | https://nintyconservation.github.io/glitchcity.wiki/glitchcity.wiki/Arbitrary_code_execution.html | la stessa conoscenza in forma recuperabile automaticamente | BRI |
| Glitch City, esecuzione remota | https://glitchcity.wiki/wiki/Remote_code_execution | il vettore che passa dal cavo Link, cioè quello che usa il ponte | BRI |
| Glitch City, cart-swap | https://glitchcity.wiki/wiki/Cart-swap_arbitrary_code_execution | esecuzione di codice sfruttando ciò che resta in RAM dopo uno scambio di cartuccia | BRI |
| Data Crystal, Gen 3 | https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_3rd_Generation | mappe di RAM e ROM dei giochi Gen 3, utili nella diagnosi di un salvataggio corrotto | SME, BRI |
| Data Crystal, mappa RAM di Cristallo | https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_Crystal/RAM_map | indirizzi in RAM di Gen 2, complementari al disassemblato | BRI |
| Data Crystal, mappa RAM di Rosso e Blu | https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_Red_and_Blue/RAM_map | indirizzi in RAM di Gen 1, utili per capire dove cade un payload | BRI |
| Hacks Guide Wiki, 3DS | https://wiki.hacks.guide/wiki/3DS:Dump_titles_and_game_cartridges | procedura di dump di titoli e cartucce, versione wiki e aggiornata della guida | 3DS |
| Hacks Guide Wiki, esportazione salvataggi | https://wiki.hacks.guide/wiki/3DS:Export_saves | estrazione dei salvataggi dalla console | 3DS |
| ConsoleMods Wiki, backup di gioco | https://consolemods.org/wiki/3DS:Creating_Game_Backups | seconda fonte indipendente sulla procedura di dump | 3DS |
| ConsoleMods Wiki, backup dei salvataggi | https://consolemods.org/wiki/3DS:Creating_Game_Save_Backups | seconda fonte indipendente sui backup dei salvataggi | 3DS |
| DS-Homebrew Wiki | https://wiki.ds-homebrew.com/godmode9i/ | GodMode9i, il gestore di file di basso livello del lato DS | 3DS |
| dumping.guide | https://dumping.guide/carts/nintendo/ds | procedura di dump delle cartucce DS orientata alla conservazione | 3DS |
| GameBrew | https://www.gamebrew.org/wiki/3DS_Save_File_Extraction_Tools | censimento degli strumenti di estrazione dei salvataggi 3DS | 3DS |
| PokeAPI | https://pokeapi.co | dati di specie, mosse e abilità via API, alternativa alla lettura da ROM per un tool su PC | BRI |
| Serebii | https://www.serebii.net | dati di gioco enciclopedici, utile come controprova rapida | TUTTI |
| Smogon, guide RNG | https://www.smogon.com/ingame/rng/ | comportamento del generatore pseudocasuale dei giochi | BRI |
| Bulbapedia, elenco dei Pokemon con differenze di forma | https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_with_form_differences | l'inventario enciclopedico delle differenze di forma, che distingue le categorie che il campo della forma non separa: forme regionali, forme di sesso, forme di sola battaglia, forme cosmetiche. È la fonte di controprova dell'asse delle forme, e serve in particolare sulle differenze di sesso, che il nostro censimento non vede perché non stanno nel campo della forma | PKD |
| Pokemon Fandom in italiano, forme regionali | https://pokemon.fandom.com/it/wiki/Forme_Regionali | l'elenco delle sole forme regionali con la nomenclatura italiana, utile come controprova mirata e come sorgente dei nomi da usare nei nostri documenti | PKD |
| Pokemon NJ Wiki, guida di Pokemon Home | https://pokemonnj.fandom.com/wiki/Pok%C3%A9mon_HOME/Features/Guidebook | trascrizione della guida interna del deposito, che è il punto in cui il servizio stesso dichiara quali specie abbiano forme alternative e quali no. Vale come indice della fonte primaria, non come sostituto | PKD |
| Serebii, archivio delle distribuzioni di eventi | https://www.serebii.net/events/ | l'archivio storico delle distribuzioni per generazione e per regione, tenuto dal 1999 e con la copertura più lunga di qualsiasi altra fonte. È il controllo indipendente da fare sulla base dei doni del verificatore, che conosce le carte e non gli eventi che non hanno lasciato una carta | EVT, PKD |
| Pokemon Showdown, vetrina dei dati | https://dex.pokemonshowdown.com/ | l'interfaccia di consultazione della medesima base dati già registrata al livello 3 come file JSON; è l'indirizzo che gli aggregati di terzi citano come propria sorgente, quindi va tenuto perché la catena delle derivazioni resti ricostruibile | PKD |
| Serebii, i Pokemon cromatici | https://www.serebii.net/games/shiny.shtml | la pagina di riferimento sui cromatici, con le probabilità, i metodi e l'elenco delle specie a cui il gioco impedisce di esserlo. È la fonte da confrontare con la misura che ricaveremo dagli archivi degli incontri, perché un elenco enciclopedico e una misura sul dato sono due cose diverse e la seconda va verificata contro la prima | PKD |

## Livello 3: implementazioni di riferimento

Codice che funziona sul campo. Va letto come prova di fattibilità e come repertorio di soluzioni, mai come specifica: dove una di queste implementazioni fa una scelta, la scelta è sua e non del formato.

| Fonte | URL | Che cosa offre | Track |
|---|---|---|---|
| Poke Transporter GB | https://github.com/Striaton-Lab-Team/Poke_Transporter_GB | il ponte di riferimento: homebrew GBA in multiboot, cavo GBC, licenza MIT; `source/gameboy_colour.cpp` mostra che il payload Z80 viaggia sul cavo al posto della squadra, e `tools/payload-generator` lo costruisce per lingua e variante di ROM | BRI |
| PCCS | https://github.com/Striaton-Lab-Team/Pokemon-Community-Conversion-Standard | specifica dei quattro metodi di conversione nel README e implementazione del solo ORIGINAL nel codice; `source/GBPokemon.cpp` contiene il campionamento con rifiuto del valore di personalità e l'uso dell'ID segreto per la lucentezza | BRI |
| Pokemon Automation | https://pokemonautomation.github.io/ | letto il 2026-08-26 nelle pagine principale, controller, domande frequenti e programma di base, e studiato in `poke-automation-study/STUDIO-01-architettura-e-perimetro.md`. È un anello di controllo chiuso su un sistema che non espone stato: la percezione è il fotogramma video più in alcuni titoli l'audio, l'attuazione è un controller emulato da un microcontrollore, la decisione è uno di oltre cento programmi. La tabella dei controller dichiara costo e difficoltà di ciascuna combinazione, dal Raspberry Pi Pico W in modalità USB a circa otto dollari e difficoltà uno, all'ESP32-S3 cablato a quindici dollari indicato come la scelta migliore per l'uso continuativo, fino alle famiglie RP2040 e RP2350 in modalità UART a difficoltà dieci e dichiarate vulnerabili al power glitching; le schede storiche sono dismesse. Il perimetro dichiarato è compatibile con le regole di questo progetto, perché è pensato per console non modificate, non accede alla memoria di gioco o di sistema e non risultano casi di sospensione per l'uso di schede di acquisizione e controller di terze parti; su console modificata l'attuatore diventa `sys-botbase`. Due limiti registrati: Linux non è ufficialmente supportato per lo sfarfallio dell'acquisizione video, e un Raspberry Pi o un tablet al posto del computer sono esclusi per il costo dell'inferenza. Il fatto più rilevante per gli altri track è che fra i titoli automatizzati compaiono Rosso Fuoco e Verde Foglia su Nintendo Switch | AUT, LDN |
| Gambatte con GameLink su TCP | https://gbatemp.net/threads/mission-wireless-trading-on-gen1-and-gen2-pokemon-games.632492/ | letto dagli screenshot dell'utente: un membro ha compilato una versione di Gambatte con il collegamento seriale emulato su TCP, funzionante in modalità client e server, e ha scambiato e combattuto con successo nei giochi di generazione 1 e 2 fra dispositivi diversi, Switch compreso. Non è specifico dei Pokemon: è un cavo seriale Game Boy generico su rete, quindi copre anche altri giochi multigiocatore. È la seconda via di collaudo del protocollo oltre a BGB | BRI |
| Pokemon-Gen3-to-Gen-X | https://github.com/Lorenzooone/Pokemon-Gen3-to-Gen-X | homebrew GBA che scambia fra Gen 3 e Gen 1 e 2 usando il protocollo normale e non exploit, più gestione dell'orologio di Rubino, Zaffiro e Smeraldo | BRI |
| PokemonGB_Online_Trades | https://github.com/Lorenzooone/PokemonGB_Online_Trades | implementazione in Python del protocollo di scambio Gen 1, 2 e 3 su adattatore USB o su BGB, con multiboot per il lato Gen 3; è la dimostrazione che il lato Game Boy si collauda su emulatore | BRI, LDN |
| PkSploit | https://github.com/binarycounter/PkSploit | letto, e il repository dichiara più della sua pagina: dumpa ROM e salvataggio e riscrive il salvataggio di qualunque cartuccia Game Boy e Game Boy Color, usando soltanto una cartuccia Gen 1 come vettore, un cavo Link e un microcontrollore compatibile Arduino. Contiene le cartelle `arduino`, `gb_asm` e `python`. L'autore avverte che è in sviluppo pesante e che la riscrittura su cartucce contraffatte è poco provata | BRI, SME |
| vaguilar/pokemon-red-cable-club-hack | https://github.com/vaguilar/pokemon-red-cable-club-hack | base dell'exploit e di parte del codice Arduino di PkSploit; non aperto | BRI |
| Phasip/PokemonLinkHack | https://github.com/Phasip/PokemonLinkHack | letto ed è la catena di exploit più completa documentata: sfrutta il buffer overflow del cavo per leggere e scrivere memoria arbitraria, aggiunge l'oggetto 0x7A allo zaino, fa eseguire dall'uso di quell'oggetto il nome dell'allenatore del Pokemon all'asilo, che salta ai dati del primo box, dove viene messo un programma che elenca ed esegue altri programmi nei box successivi. Per poter salvare lo stato avvelena la squadra. È una strategia di payload persistente, opposta a quella transitoria del ponte | BRI |
| Blog di Phasip | https://www.sn1.se/posts/pokemon/ | introduzione alla catena qui sopra; non letto | BRI |
| pokerom-trader | https://github.com/savaughn/pokerom-trader | clonato e letto nella struttura: scambio fra due file di salvataggio Gen 1 e Gen 2 su PC, in C con la libreria PKSav e interfaccia Raylib, con ricalcolo dei checksum e regole di evoluzione da scambio | BRI |
| CableClub | https://github.com/CableClub | quattro repository; l'organizzazione viene da un gruppo che ha completato scambi fra Game Boy reali attraverso internet | BRI |
| CableClub/cable-link | https://github.com/CableClub/cable-link | letto ed è il riferimento più importante per l'opzione D: PCB KiCad completo con gerber, firmware su Raspberry Pi Pico che apre SPI a 500 kHz, e `src/pokemon_gen1_link_protocol.h` con la macchina a stati e tutte le costanti del protocollo Gen 1. Licenza Apache 2.0, 2021 | BRI |
| kinnay/NintendoClients, wiki LDN | https://github.com/kinnay/NintendoClients/wiki/LDN-Protocol | letto ed è la specifica del protocollo LDN: action frame vendor-specific ogni 100 ms, OUI 00:22:AA, canali 1, 6 e 11 in banda 2.4 GHz, struttura dell'advertisement con i suoi offset, tre livelli di cifratura, derivazione delle chiavi dalle chiavi di console, sequenza di connessione e assegnazione degli indirizzi 169.254.X.Y | LDN |
| unlimitedcoder2/ldnd | https://github.com/unlimitedcoder2/ldnd | letto il 2026-08-26 nel sorgente: demone in C, GPL-2.0, che porta lo stack wireless di Linux su Windows collegando il kernel come libreria statica tramite LKL dentro un eseguibile MinGW, ricevendo l'adattatore via WinUSB e facendogli caricare i driver e i file di `linux-firmware`. La riga di comando del kernel incorporato è `mem=128M mac80211_hwsim.radios=0 rtw88_usb.switch_usb_mode=0`, e quell'ultimo parametro disabilita il passaggio a USB 3 che fa ri-enumerare il dispositivo e annulla la riassegnazione fatta con Zadig. Funziona solo con adattatori USB, e ha una compatibilità hardware diversa dalla via Linux perché scavalca gestore di rete e driver di sistema | LDN |
| ldn.readthedocs.io | https://ldn.readthedocs.io | documentazione delle classi e delle funzioni della libreria Python di kinnay; non letta | LDN |
| arduino-poke-gen2 | https://github.com/stevenchaulk/arduino-poke-gen2 | letto: adatta a Gen 2 la macchina a stati di `pepijndevos/arduino-boy`, e porta un fatto architetturale utile, cioè che in Gen 2 non serve memorizzare nulla perché rimandando indietro i byte ricevuti si ottiene la copia della squadra. Provato dall'autore su Cristallo, con schema di cablaggio incluso | BRI |
| pepijndevos/arduino-boy | https://github.com/pepijndevos/arduino-boy | origine di quella macchina a stati, per Gen 1; non aperto | BRI |
| MrCheeze/pokestadium-ace | https://github.com/MrCheeze/pokestadium-ace | letto: l'exploit sta nel sistema di scambio di Stadium, richiede due controller con Transfer Pak e presuppone di avere già l'esecuzione di codice su Rosso, Blu o Giallo. Documenta gli indirizzi in memoria N64 dove i box vengono convertiti dal formato Gen 1 al formato Stadium, che è un terzo esempio documentato di conversione fra formati oltre al Time Capsule | BRI |
| Goppier/GEN3PokemonDistributions | https://github.com/Goppier/GEN3PokemonDistributions | letto: non è un ponte ma una raccolta di cartucce di distribuzione per eventi Gen 3, e dà la procedura utente del multiboot che al progetto mancava, cioè accendere la console ricevente tenendo premuti start e select finché il logo Nintendo scompare, con il lato master del cavo, quello viola e più piccolo, inserito nella console che invia | BRI |
| Gen 3 ACE Pokemon Builder, sorgente e corpus | https://mankeymite.github.io/Gen3ACEPokemonBuilder/ | letto per intero il 2026-09-01, e il modo va dichiarato perché ne qualifica la portata: il sito non è impacchettato ma è un albero di sessantotto moduli serviti come file separati, quindi il codice arriva con i nomi originali, e insieme al codice porta un corpus di duecentodieci esemplari conservati con seme di origine, valore di personalità, valori individuali e sesso dell'allenatore. Quel corpus è il banco di prova su cui il progetto ha verificato le formule di generazione, con l'esito registrato in `recreate-pokemon-distributions-events/STUDIO-03-verifica-del-metodo-sul-corpus.md`: valori individuali riprodotti su duecentonove vettori su duecentonove, valore di personalità su duecentotto, sesso dell'allenatore su cento su cento per la derivazione a scorrimento di sette. Sono stati trovati due difetti, di cui uno con conseguenza operativa: la tabella dei caratteri colloca gli accentati nella fascia dei sillabari giapponesi e delle cifre, dichiarando di derivare dalla documentazione di dominio contro il sorgente del gioco, e la sua stessa tabella assegna due caratteri al medesimo byte; e una voce del corpus porta un valore di personalità che il proprio seme non produce. Lo strumento che esegue il confronto è `tools/confronta-ace-builder.py` | ACE, EVT, BRI |
| Gen 3 ACE Pokemon Builder, funzione dichiarata | https://mankeymite.github.io/Gen3ACEPokemonBuilder/ | la funzione dichiarata dal suo autore nel video del 26 agosto 2026, registrata prima che il sorgente fosse letto: la funzione dichiarata dal suo autore nel video del 26 agosto 2026 è costruire il dato completo di un esemplare di terza generazione, comprese le vecchie distribuzioni di evento, con informazioni dell'allenatore, statistiche e lucentezza a scelta, restituendo un codice da digitare nei nomi delle scatole ed eseguire con il glitch. L'autore dichiara le opzioni di generazione legale attive per difetto e dichiara di non poter garantire l'accettazione da parte di Pokemon Home. È il punto di convergenza con il track delle distribuzioni, perché produce lo stesso esemplare per una via opposta: quella scrive il risultato, l'altra fa rifare al gioco ciò che faceva allora | ACE, EVT |
| Sleipnir17, quattro elenchi di codici per Smeraldo | https://pastebin.com/kYfBzVE3 | non aperti, catalogati il 2026-09-01 dal canale dei collegamenti del server della comunità: sono i quattro elenchi storici di codici per l'esecuzione tramite i nomi delle scatole su Smeraldo, e gli altri tre stanno a `dFLaf2TB`, `7S63EDyL` e, il terzo, soltanto in una copia d'archivio su `web.archive.org` perché l'originale non è più raggiungibile. Quest'ultimo dato va registrato perché è un fatto sul dominio e non su un collegamento: in questa comunità la conoscenza vive su servizi di incollaggio che scompaiono, e una fonte catalogata senza copia è una fonte che si perderà | ACE |
| Mettrich, codici per Smeraldo e scrittore in base 64 | https://gist.github.com/claydolwithexplosion/017f1784deebcd118b61d3ad917edb3c | non aperto, catalogato il 2026-09-01. Codici per Smeraldo modificati o creati da Mettrich, che è l'autore dello scrittore in base sessantaquattro su cui poggia la costruzione di un esemplare completo in quattordici nomi di scatola. Accanto ad esso il canale elenca un ulteriore incollaggio dedicato ai valori individuali perfetti e alla lucentezza ottenuti con quello scrittore, a `Tgin3hvf` | ACE, EVT |
| ACE Code Generator | https://e-sh4rk.github.io/CodeGenerator/ | non eseguito. Genera la sequenza da digitare per ottenere l'esecuzione di codice, a partire da ciò che si vuole ottenere; esiste in variante generale e in variante per Rosso Fuoco e Verde Foglia all'indirizzo `index_frlg.html`. È il primo strumento della catena e quello che rende la tecnica accessibile senza scrivere assembly a mano | ACE |
| Hex to Base64 per Gen 3 | https://mankeymite.github.io/HexToBase64/ | non eseguito. Converte dati esadecimali nella forma digitabile che lo scrittore in base 64 accetta; serve al passo in cui i byte composti vanno immessi nel gioco | ACE |
| Gen3ItemToBoxNames | https://mankeymite.github.io/Gen3ItemToBoxNames/ | non eseguito. Converte la richiesta di un oggetto su Smeraldo in nomi di scatola da digitare, ed è il caso semplice della medesima tecnica: utile per capirla prima di applicarla a un esemplare | ACE |
| PokeGlitzer | https://github.com/E-Sh4rk/PokeGlitzer | non aperto. Editor di salvataggi dichiarato pensato per chi impiega i glitch, dello stesso autore dei generatori di codice; complementare a PKHeX, che resta il riferimento sulle regole di legittimità | ACE, SME |
| Gen 3 ACE Archive | https://mankeymite.github.io/gen3-ace-archive/ | letto il 2026-08-31. Raccoglie codici cercabili per gioco, lingua e piattaforma, guide video, generatori e documentazione di allestimento. Va registrata una assenza perché è significativa: non contiene alcuna dichiarazione sulla legittimità degli esemplari prodotti, sulla loro accettazione da parte dei verificatori né sui rischi per l'account, e tratta la tecnica come problema di implementazione e non di conseguenze | ACE |
| ACE3, guida scritta | https://e-sh4rk.github.io/ACE3/ | letta il 2026-08-31 e risultata un indice di rimandi e non un testo: contiene i collegamenti alle guide per Smeraldo e per Rosso Fuoco e Verde Foglia, al generatore di codice e a un editor, senza spiegare la tecnica né dire nulla sulla legittimità. Le guide vere sono le due pagine collegate, non ancora aperte | ACE |
| Guida ACE per FR/LG | https://pomeg-letterbombers.github.io/pokemon-ace-notes/frlg-non-jpn-pre-e4-route/ | non aperta. Procedura di allestimento per le versioni non giapponesi prima dei capi dei Quattro, che è il percorso dichiarato più accessibile | ACE |
| Guida ACE per R/S | https://claydolwithexplosion.github.io/doguu-codex/getting-ace-rs/index.html | non aperta. Procedura per Rubino e Zaffiro, che sono i due giochi Gen 3 dove il progetto ha già documentato l'esistenza del difetto sfruttabile nel motore di testo | ACE |
| DiscordChatExporter | https://github.com/Tyrrrz/DiscordChatExporter | letto il 2026-08-31 nel README e nelle pagine su token e riga di comando. Esporta la cronologia di un canale in HTML, testo, JSON o CSV, scarica gli allegati con `--media`, e ha comandi per un canale, un server intero o tutto ciò che è accessibile. Accetta entrambi i tipi di token, e la distinzione è il punto: con un bot token vede i soli canali in cui il bot è stato invitato, quindi ha la medesima portata di `tools/fetch-discord.py` e non aggira il consenso di chi amministra; con un token utente vede tutto ciò che vede l'account, ed è la via che l'autore stesso sconsiglia in due punti del proprio repository, scrivendo nel README che automatizzare un account utente è contro le condizioni d'uso e può portare al ban, e che se possibile si usi un bot. Il progetto lo adotta, e con quale token è deciso da ADR-019 il 2026-08-31: l'utente ha scelto il token personale sui server dove il bot non può essere invitato, accettando esplicitamente il rischio dopo che gli era stato esposto tre volte, con la cadenza di poche esportazioni all'anno. La catena è già in parte costruita perché `tools/read-chat-export.py` era stato scritto per digerire il suo JSON. Complementare e non alternativo al lettore proprio: DCE per l'esportazione grossa e i media, il lettore proprio per gli aggiornamenti incrementali con cursore dove il bot è dentro. La procedura d'uso completa, dai file da scaricare ai comandi, sta in `docs/22-strumenti.md` | BRI, LDN, EVT |
| PKHeX | https://github.com/kwsch/PKHeX | riferimento di fatto sul formato di salvataggio di tutte le generazioni e sulle regole di legalità | TUTTI |
| PKHeX web | https://pkhex-web.github.io/ | la stessa cosa nel browser, comoda per un'ispezione rapida senza installare | SME, 3DS |
| PKSav | https://github.com/ncorgan/pksav | libreria C per leggere e scrivere salvataggi Gen 1, 2 e 3, base di pokerom-trader; archiviata in sola lettura dal 2023, quindi da leggere e non da cui dipendere | BRI, SME |
| HexManiacAdvance | https://github.com/haven1433/HexManiacAdvance | editor esadecimale con le mappe dei dati delle ROM GBA | BRI, SME |
| rgen3 | https://github.com/crumblingstatue/rgen3 | libreria e utilità Rust per i salvataggi Gen 3, inclusa la codifica delle stringhe | BRI, SME |
| ads04r/Gen3Save | https://github.com/ads04r/Gen3Save | parser Python di un salvataggio Gen 3 | BRI, SME |
| aarant/gen3tools | https://github.com/aarant/gen3tools | strutture dati Python ed editor grafico per Gen 3 | BRI, SME |
| RNGReporter | https://github.com/Admiral-Fish/RNGReporter | analisi del generatore pseudocasuale | BRI |
| Gen3-WCTool | https://github.com/projectpokemon/Gen3-WCTool | strumenti per le Wonder Card e gli eventi Gen 3 | BRI |
| gba-link-connection | https://github.com/afska/gba-link-connection | letto ed è molto più di quanto il nome suggerisca: libreria C++ con moduli separati per la modalità multiplayer a 16 bit, l'invio di software multiboot ad altre console, l'adattatore wireless, il protocollo Joybus verso Wii e GameCube, le carte e-Reader, il Mobile Adapter GB, e soprattutto `LinkSPI.hpp`, che collega la GBA a un PC o a un Raspberry Pi con il cavo del Game Boy Color fino a 2 Mbit al secondo | BRI |
| progetto REON | https://github.com/REONTeam | letto: ricostruisce l'infrastruttura di rete del Mobile Adapter GB, con libreria del protocollo, server, emulatore per BGB, adattatore su Arduino e una utilità per lo scambio nel Trade Corner | BRI |
| REONTeam/libmobile | https://github.com/REONTeam/libmobile | letto: implementazione in C del protocollo dell'adattatore, dichiarata la più completa esistente, basata sulla ricerca pubblicata su Dan Docs | BRI |
| REONTeam/trade-corner | https://github.com/REONTeam/trade-corner | letto: script in C# che esegue scambi in Pokemon Cristallo attraverso il Trade Corner del PokeCom Center, da eseguire come lavoro pianificato non più di una volta l'ora perché il gioco stesso non permette controlli più frequenti. Basato su una scoperta pubblicata sui forum di Glitch City. È un canale di scambio alternativo al cavo per la generazione 2 | BRI |
| Dan Docs | https://shonumi.github.io/dandocs.html | raccolta di documenti tecnici sui protocolli delle periferiche di Game Boy e Game Boy Advance, compresi il Mobile Adapter GB e l'adattatore a quattro giocatori DMG-07; è la fonte su cui `libmobile` dichiara di basarsi | BRI |
| gba-link-cable-rom-sender | https://github.com/FIX94/gba-link-cable-rom-sender | letto: homebrew per GameCube e Wii, vuole una cartella `gba` sulla scheda con i file multiboot da 256 KB o meno, e li trasferisce alla console collegata alla porta 2 | BRI |
| usb-gba-multiboot | https://github.com/tangrs/usb-gba-multiboot | letto: firmware per Teensy più software su PC per caricare fino a 256 KB via USB, e spiega la scelta della modalità seriale normale perché è a 32 bit, riceve mentre invia ed è la più semplice da implementare, al prezzo di poter avviare una sola console per volta | BRI |
| BGB | https://bgb.bircd.org/ | emulatore Game Boy con cavo Link esposto su TCP e protocollo documentato, cioè il banco di collaudo del lato Game Boy | BRI |
| mGBA | https://mgba.io/ | emulatore con supporto multiplayer locale, seconda via per il collaudo del lato Game Boy | BRI |
| FlashGBX | https://github.com/lesserkuma/FlashGBX | lettura e scrittura di cartucce e salvataggi con il lettore GBxCart RW | SME, BRI |
| Checkpoint | https://github.com/BernardoGiordano/Checkpoint | gestore di backup dei salvataggi per 3DS e Switch, quello installato su questa console | 3DS |
| MSET9 | https://github.com/hacks-guide/MSET9/releases/latest | exploit di ingresso usato per l'installazione del custom firmware | 3DS |
| Luma3DS | https://wiki.hacks.guide/wiki/3DS:Luma3DS | firmware personalizzato installato sulla console | 3DS |
| SEEDconv | https://github.com/d0k3/SEEDconv/releases | conversione dei seed; produce materiale console-unico da trattare come segreto | 3DS |
| Azahar | https://azahar-emu.org/ | emulatore 3DS, per la verifica dei dump fuori dalla console | 3DS |
| kinnay/LDN | https://github.com/kinnay/LDN | documentazione del protocollo di rete locale della Switch | LDN |
| frlg-ldn-trade | https://github.com/unlimitedcoder2/frlg-ldn-trade | letto il 2026-08-26: proof of concept dello scambio fra PC e Rosso Fuoco o Verde Foglia su Switch e Switch 2, AGPLv3. Richiede Linux, Python 3.12 o successivo, le chiavi della console, almeno due `.pk3` e il gioco portato fino allo sbloccio della sala degli scambi, stimato in venti o quaranta minuti. La tabella di compatibilità dichiara affidabili ALFA AWUS036ACHM su `mt76x0u` e Realtek RTL8821CE su `rtw88_8821ce`, inaffidabile AMD RZ616 su `mt7921e`, e problematiche Intel AX200 su `iwlwifi` e Atheros AR9271 su `ath9k_htc`, entrambe incapaci di ottenere un indirizzo. Nella procedura la console fa da capo sessione, si approva la richiesta di ingresso di EMU, e il secondo membro simulato è quello che viene consegnato | LDN |
| tornadus/frlg-ldn-trade | https://github.com/tornadus/frlg-ldn-trade | scambio fra Rosso Fuoco e Verde Foglia su Switch e un PC via LDN | LDN |
| ldn_mitm | https://github.com/spacemeowx2/ldn_mitm | letto: sostituisce il servizio di rete locale del sistema ed emula la scansione delle console vicine usando UDP sulla rete locale, quindi si usa insieme a `switch-lan-play` | LDN |
| switch-lan-play | https://github.com/spacemeowx2/switch-lan-play | la controparte di `ldn_mitm` sul lato rete; non aperto | LDN |
| ryu_ldn_nx | https://github.com/Ethiquema/ryu_ldn_nx | letto: sysmodule per Switch che porta il multiplayer sui server LDN di Ryujinx senza configurazione di rete, licenza GPL v2. L'autore dichiara che il progetto è in sviluppo e non pronto al rilascio | LDN |
| PKHeX, tabelle delle statistiche di base per titolo | https://github.com/kwsch/PKHeX | lette il 2026-09-02 in `PKHeX.Core/Resources/byte/personal`, con `PKHeX.Core/PersonalInfo/Info/` per il formato dei record, `PKHeX.Core/Legality/Tables/FormInfo.cs` per le forme di sola battaglia e quelle totemiche, `PKHeX.Core/Game/Enums/Species.cs` per i numeri, e `PKHeX.Core/Legality/Verifiers/TransferVerifier.cs` per la regola dei trasferimenti. Sono la fonte che ha risposto alla domanda su che cosa la chiusura della banca vincoli, e la risposta è zero specie e zero voci-forma: l'unione dei titoli a via diretta copre tutte e milleventicinque le specie, e le dodici voci che soltanto la via indiretta dichiara sono dieci forme totemiche e due di sola battaglia. La regola dei trasferimenti è il pezzo decisivo e non era nella ricerca consegnata: una forma totemica deve arrivare all'ottava generazione già riportata alla forma base, e quattro specie non si trasferiscono affatto, quindi quelle voci non sono in attesa di scadenza ma irraggiungibili per costruzione. Un limite va dichiarato: il contrassegno di presenza dice che una voce esiste nei dati, non che sia ottenibile né che la via che parte da quel titolo funzioni | PKD |
| Pokemon Showdown, base dati delle specie | https://play.pokemonshowdown.com/data/pokedex.json | letta il 2026-09-02 come controllo incrociato, ed è la terza ricostruzione indipendente che concorda sul numero delle specie: milleventicinque voci base con numero da uno a milleventicinque, nessuno mancante. Sulle forme non è confrontabile con le tabelle del verificatore, e la ragione va conosciuta perché altrimenti la discrepanza sembra un errore: questa base dati serve il gioco competitivo, quindi enumera le forme che contano in una battaglia e omette quelle puramente estetiche, mentre le tabelle del verificatore enumerano tutto ciò che esiste nei dati. Le sue trecentocinquantacinque forme non base, di cui centoquarantatre senza marca di non standard, non sono dunque un conteggio alternativo delle millecinquecentotrentacinque voci-forma ma il conteggio di un'altra cosa. Porta inoltre centotrentasette voci inventate dalla comunità competitiva, con numero non positivo, che vanno filtrate | PKD |
| Project Pokemon, collezione di riferimento di theSLAYER | https://projectpokemon.org/home/files/file/4968-home-compatible-living-dex-regular-and-shiny/ | catalogata il 2026-09-02 dalla consegna dell'utente e non aperta: sono file che contengono l'intero contenuto delle scatole di un salvataggio, da sovrapporre a un salvataggio proprio della medesima coppia di versioni. La consegna riporta tre regole dell'autore che vanno tenute perché coincidono con quanto il progetto ha stabilito per altra via, cioè non modificare i valori immutabili, non toccare il codice di tracciamento del deposito, e non impiegarli in un gioco competitivo. Riporta anche due lacune dichiarate dall'autore, e la prima è l'unico punto che potrebbe dare una scadenza a una specie: Spinda esiste nel titolo che sarebbe la sua via diretta ma non vi si potrebbe depositare per un difetto di quella implementazione. Il progetto non ha verificato quella affermazione e non ha scaricato i file | PKD |
| PKHeX-Plugins, generazione automatica di esemplari legali | https://github.com/architdate/PKHeX-Plugins | catalogato il 2026-09-02 su segnalazione dell'utente e non letto. Il suo scopo dichiarato è produrre un esemplare legale a partire da una descrizione competitiva, cercando fra gli incontri conosciuti uno che la soddisfi. Il rapporto con il lavoro di questo progetto va detto perché non è di sostituzione: quello strumento risolve il problema di ottenere un esemplare qualunque che sia legittimo, mentre il generatore di questo progetto risolve il problema di riprodurre un esemplare determinato, cioè quello che una distribuzione consegnò, con il suo seme e i suoi campi. Il primo problema ammette molte soluzioni e il secondo una sola. Resta interessante come controllo incrociato e come strumento per la parte del Pokedex che non ha vincoli di identità | PKD, EVT |
| Reddit, dex vivente completo con forme alternative | https://www.reddit.com/r/PokemonBDSP/comments/1hm21he/ | letta dagli screenshot dell'utente il 2026-09-02, ed è una testimonianza e non un dato. Vale come prova di esistenza dell'obiettivo, cioè che una collezione vivente completa con forme alternative sia stata effettivamente portata a termine, e la sua data di inizio è luglio 2018. Non vale come dato sulla necessità della via indiretta, e la ragione va scritta perché l'elenco dei giochi impiegati induce in errore: quell'elenco comprende titoli anteriori all'ottava generazione perché nel 2018 quella era la via naturale, non perché fosse necessaria. Il conto sulle tabelle dei dati è più forte di questa testimonianza e la contraddice sul punto | PKD |
| Reddit, come trattare le forme regionali in un dex vivente | https://www.reddit.com/r/pokemon/comments/1kd2k17/ | catalogata il 2026-09-02 e non letta oltre il titolo, che dichiara la natura della discussione: è una questione di preferenza su come organizzare una collezione e non una questione di fatto. Resta pertinente a una decisione aperta del sottoprogetto, cioè che cosa significhi completo, e per quella una discussione di preferenze è materiale legittimo purché sia trattata come tale | PKD |
| Pokemon Millennium e Pokedex ufficiale, esplorazione delle specie | https://pokemonmillennium.net/pokedex/dex | catalogati il 2026-09-02 su segnalazione dell'utente e non letti. Sono strumenti di consultazione per esplorare specie e varianti, utili a chi guarda e non a chi conta: la domanda quantitativa del sottoprogetto è già risolta da tre ricostruzioni indipendenti concordi, e una pagina di consultazione non aggiunge nulla a quelle. Restano il posto giusto dove verificare a occhio una voce sospetta | PKD |
| Bulbapedia, distribuzioni di evento giapponesi di Gen 3 | https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pok%C3%A9mon_distributions_in_Generation_III | letta il 2026-09-02 ed è la fonte della provenienza storica di quattordici gruppi di evento su trentasette. Documenta ciò che nessuna fonte di primo livello registra, cioè date, luoghi e modo di consegna: sono i tre fatti che spiegano la rarità di un esemplare, e nessun disassemblato sa in quali negozi un dono venne distribuito. Concorda con la tabella del verificatore su tutti gli identificativi di allenatore che è stato possibile confrontare, il che è una convalida incrociata fra due fonti indipendenti. Su una voce diverge, cioè il Jirachi della stella dei desideri, e la divergenza è registrata nella voce corrispondente di `recreate-pokemon-distributions-events/provenienze-eventi.json` con l'argomento per cui vale la tabella: gli identificativi di questo catalogo codificano la data, e il valore della tabella si legge come una data coerente con la manifestazione mentre l'altro no. Diverge anche sul nome dell'allenatore delle uova del PokéPark, e quella questione resta aperta | EVT |
| Bulbapedia, distribuzioni di evento inglesi di Gen 3 | https://bulbapedia.bulbagarden.net/wiki/List_of_English_event_Pok%C3%A9mon_distributions_in_Generation_III | letta il 2026-09-02, fonte della provenienza di nove gruppi. Fra i fatti che porta e che il progetto non aveva, il più utile alla pianificazione è la durata delle finestre di distribuzione, che va dalle tre ore di un solo giorno per il Mew del mistero ai tre anni della correzione dell'orologio delle bacche: la rarità di un esemplare autentico è una funzione di quella durata, e conoscerla dice quali esemplari valga la pena cercare invece di ricreare. Tutti gli identificativi che dichiara concordano con la tabella del verificatore. Su un punto va usata con cautela e la cautela è registrata: associa il nome di allenatore del Jirachi occidentale a una manifestazione messicana, mentre la conoscenza comune lo associa al disco allegato al titolo per la console domestica, e finché una pagina dedicata non è letta la voce resta dichiarata incerta | EVT |
| Bulbapedia, distribuzioni di evento italiane di Gen 3 | https://bulbapedia.bulbagarden.net/wiki/List_of_Italian_event_Pok%C3%A9mon_distributions_in_Generation_III | letta il 2026-09-02, ed è la fonte che riguarda più direttamente questo progetto, perché documenta la distribuzione che l'utente possiede su cartuccia: la campagna del decennale in edizione italiana, tenuta dal 23 al 25 giugno 2006 al parco di Mirabilandia. Porta anche un dato che nessuna fonte di primo livello contiene e che ha cambiato ciò che il generatore scrive: il Pikachu di quella distribuzione teneva una Sfera Luminosa. La tabella del verificatore non lo dichiara, e non lo pretende, perché un oggetto tenuto si può togliere o scambiare e non è un vincolo di legittimità; resta un tratto dell'esemplare originale, quindi la distinzione fra un esemplare accettato e uno fedele passa per fatti di questo genere | EVT |
| PKHeX, algoritmo di generazione degli eventi Gen 3 | https://github.com/kwsch/PKHeX | letta il 2026-09-01 in `PKHeX.Core/Legality/Encounters/Templates/Gen3/Gifts/EncounterGift3.cs`, `PKHeX.Core/Legality/RNG/ClassicEra/Gen3/CommonEvent3.cs`, `PCJPFifthAnniversary.cs`, `WeightedTable3.cs`, `MystryMew.cs` e `CommonEvent3Checker.cs`. È la lettura che ha chiuso i metodi di generazione e ha corretto il modello di questo progetto in un punto sostanziale: la lucentezza non è un vincolo da soddisfare cercando un seme fortunato ma un ramo dell'algoritmo, e i rami della composizione del valore di personalità sono quattro. Due di essi consumano un numero di estrazioni diverso, quindi spostano anche la provenienza dei valori individuali. Il ramo a lucentezza negata porta una mutazione additiva, cioè somma otto e azzera i tre bit bassi quando il valore ordinario sarebbe cromatico, e quella mutazione spiega il solo vettore del corpus che il progetto non riusciva a riprodurre. La tabella dei doni del quinto anniversario si è rivelata una funzione aritmetica e non un elenco: otto voci di peso uguale, con specie, mosse e lucentezza ricavate dividendo il peso estratto. Il solo dato non derivabile è l'elenco degli ottantasei semi dell'evento del topo, che è un fatto storico | EVT, BRI |
| PKHeX, tabella dei caratteri giapponese di Gen 3 | https://github.com/kwsch/PKHeX | letta il 2026-09-01 in `PKHeX.Core/PKM/Strings/StringConverter3.cs`, dove le due tabelle della terza generazione stanno una accanto all'altra. Documenta il fatto che rende necessaria una seconda tabella e che non è evidente: in questa generazione un byte non ha un carattere ma due, e quale dei due si veda dipende dalla lingua del gioco. Il caso più netto è il byte 0x52, che rende due sillabe katakana diverse nelle due lingue, e il più insidioso è che scrivere un nome giapponese con la tabella internazionale non produce un errore ma un nome plausibile e sbagliato. È la fonte da cui il progetto ha estratto `data/charmap-gen3-jp.json`, con provenienza dichiarata di rango diverso dalle altre tabelle secondo ADR-025: non un disassemblato, che per questa generazione il progetto possiede nella sola versione internazionale, ma il codice contro cui gli esemplari verranno misurati | EVT, BRI |
| PKHeX, tabella eventi Gen 3 e vocabolario dei metodi | https://github.com/kwsch/PKHeX | letta il 2026-08-29 in `PKHeX.Core/Legality/Encounters/Data/Gen3/EncountersWC3.cs` e `PKHeX.Core/Legality/RNG/PIDType.cs`, ed è la fonte che ha spostato il track degli eventi dalla congettura al dato. La tabella porta 177 voci, ciascuna con il proprio metodo di generazione dichiarato, e vive nel codice perché, come dice il suo commento, i dati di quella generazione non sono mai stati conservati in forma binaria uniforme. La sigla BACD nomina l'ordine invertito con cui le quattro estrazioni compongono valore di personalità e valori individuali, e quell'inversione è la firma di un esemplare da evento: 114 voci usano `BACD_R_A`, cioè seme di origine ristretto a 16 bit più codice anti-lucentezza additivo. Conferma per via indipendente quattro affermazioni dei video, cioè il seme a 16 bit, il codice anti-lucentezza, i 214 semi della correzione delle bacche, che documenta come somma delle cifre di ore, minuti e secondi in decimale binario letta dall'orologio, e la selezione a pesi che costa due estrazioni; conferma anche che la distribuzione da console domestica usa un generatore diverso, `XDRNG` invece di `LCRNG`. Chiude un punto che i video dichiaravano aperto: la derivazione del sesso dell'allenatore dei tre leggendari del film è uno scorrimento di 15 bit dopo l'oggetto tenuto, con due avanzamenti, e non la divisione per 0xCC0 congetturata. Porta infine il fatto più notevole, cioè che il gioco riceve un'interruzione di sincronismo verticale fra la generazione della personalità e quella dei valori individuali, e che rimuoverla con una modifica alla ROM produce la correlazione ordinaria: il metodo dipende da un'interruzione hardware e non soltanto dal codice | EVT, BRI, SME |
| gen-iii-event-patcher | https://github.com/superguideguy/gen-iii-event-patcher | letto il 2026-08-29: strumento Java che trasforma la ROM di un gioco Gen 3 in ROM di distribuzione e applica uno script di evento a un salvataggio, con un compilatore elementare per gli script e un costruttore di checksum. Documenta il secondo canale di distribuzione, che il primo studio del track confondeva con il multiboot: il Dono Segreto non attiva una bandiera ma scarica nel salvataggio uno script di un kilobyte eseguito più tardi, capace di qualunque istruzione valida compresa quella che porta all'esecuzione di codice arbitrario. È il medesimo meccanismo che il dev log dello strumento di trasferimento descrive dall'altro capo, scoperto in modo indipendente da due progetti con scopi opposti. Dichiara che Rubino e Zaffiro hanno il precedente Evento Mistero, cosa diversa, e che la carta meraviglia passa dall'adattatore senza fili e non dal cavo | EVT, BRI |
| Project Wonder, distribuzioni per differenze | https://github.com/Goppier/Gen3DistributionRoms | letto il 2026-08-29: dieci differenze da applicare a una ROM di distribuzione preservata, che producono distribuzioni degli oggetti di evento, cioè i biglietti, la mappa marina e la grotta alterna, più due eventi costruiti dalla comunità e tre distribuzioni di uova, con supporto dichiarato a sei lingue fra cui l'italiano. È la via più pronta all'uso per gli oggetti di evento, che sbloccano gli unici incontri legittimi di alcune specie. Il fabbisogno dichiarato è di due Game Boy Advance, due adattatori senza fili e una scheda riprogrammabile | EVT |
| Project Pokemon, Events Gallery | https://github.com/projectpokemon/EventsGallery | non aperto: archivio collettivo della conservazione delle informazioni sugli eventi, per tutte le generazioni, ed è la controparte documentale del catalogo che questo repository genera. Serve a rispondere se i campioni degli eventi dichiarati non chiusi manchino davvero, cioè se il progetto possa contribuire alla conservazione invece di consumarla | EVT |
| awesome-gbadev | https://github.com/gbadev-org/awesome-gbadev | elenco curato di risorse per lo sviluppo GBA | BRI |
| awesome-gbdev | https://github.com/gbdev/awesome-gbdev | l'equivalente per il Game Boy, punto di ingresso a strumenti e documentazione | BRI |
| PokePC, dati statici | https://github.com/pokepc/dataset | dati in JSON su specie, giochi, Pokedex, preimpostazioni delle scatole e metadati del servizio. Dichiara di derivare da Pokemon Showdown, PokeAPI, Project Pokemon, Serebii e Bulbapedia, quindi è un aggregato e non una fonte primaria: va usato per confrontare la nostra enumerazione, mai per fondarla | PKD |
| PokePC, tracciatore classico | https://github.com/pokepc/classic.pokepc.net | applicazione web di tracciamento del Pokedex e organizzazione delle scatole di un living dex; rimanda per i dati a supereffective, quindi la catena delle versioni va risolta prima di fidarsi di una delle due | PKD |
| SuperEffective, cliente dei dati | https://github.com/itsjavi/supereffective/tree/main/src/lib/data-client | la sorgente dei dati che PokePC dichiara di usare, ed è il punto in cui verificare quale delle due sia la versione aggiornata | PKD |
| Monarium | https://github.com/kristopheles/monarium | applicazione di gestione di un living dex, indicata dalla community come la più completa; da valutare come strumento da ospitare in proprio dopo il confronto con la conoscenza costruita da questo progetto, non prima | PKD |
| PokePC, living dex in linea | https://pokepc.net/livingdex | l'istanza pubblica del tracciatore, utile per vedere che cosa uno strumento maturo consideri una voce da possedere | PKD |
| PokePC, radice dell'organizzazione | https://github.com/pokepc | il contenitore da cui pendono il dataset e il tracciatore; si registra la radice e non i soli repository perché è il punto da cui accorgersi di un repository nuovo | PKD |
| Project Pokemon, radice dell'organizzazione | https://github.com/projectpokemon | il contenitore dei repository di conservazione già registrati singolarmente, fra cui la galleria degli eventi e gli strumenti per le Wonder Card di terza generazione | EVT, PKD |
| PokeOS, generatore di Spinda | https://www.pokeos.com/it/tools/spinda-generator | strumento in linea che visualizza la configurazione delle macchie a partire dal valore di personalità; serve come controprova visiva del nostro generatore quando lo scriveremo, non come sua sorgente | PKD |
| PokePC Classic, dati del tracciatore di catalogo vivente | https://github.com/pokepc/classic.pokepc.net | l'anagrafica di 1599 voci con i contrassegni che dicono che cosa ciascuna sia, e sette disposizioni in scatole per il deposito, sotto licenza MIT: è la terza enumerazione indipendente del catalogo vivente e l'unica leggibile dal dato invece che dall'interfaccia. Il confronto con la nostra sta in `pokedex-home-completo/CONFRONTO-LIVINGDEX-POKEPC.md` | PKD |
| Monarium, generatore di disposizioni con marchi | https://github.com/kristopheles/monarium | tracciatore da installare per conto proprio, con oltre quindici opzioni di disposizione e cinque contrassegni per esemplare, cioè allenatore proprio, cattura nel titolo o nella regione di origine, cromaticità, sfera giusta e provenienza dall'applicazione per telefono | PKD |

### Nota sulla categoria degli strumenti

Diverse voci del livello 3 sono strumenti eseguibili e non documenti. Su `PKHeX` la distinzione va rifatta, perché dal 2026-08-29 non è più soltanto uno strumento da eseguire: due suoi file sono stati letti come fonte, cioè la tabella degli eventi di terza generazione e l'enumerazione dei metodi di generazione, e la voce dedicata sopra dichiara che cosa documentano. Lo strumento resta da eseguire quando esisterà un dato reale su cui puntarlo; il suo sorgente è già una fonte letta. Le altre voci di questo genere sono `PKSav`, `HexManiacAdvance`, `rgen3`, `Gen3Save`, `gen3tools`, `RNGReporter`, `Gen3-WCTool`, `FlashGBX`, `BGB`, `mGBA`, `Checkpoint`, `MSET9`, `SEEDconv`, `Azahar`. Non sono state lette e non ha molto senso leggerle: si eseguono. La loro pagina aggiunge poco a ciò che questo registro dice già, e il momento in cui servono è quando esiste un dato reale su cui puntarle. Sono quindi catalogate come strumenti da eseguire, non come fonti non lette, ed è una categoria diversa: la prima si usa quando serve, la seconda è un debito.

Restano invece fonti non lette, cioè debito vero, i repository di codice del livello 3 che documentano una tecnica e che non sono stati aperti: `Phasip/PokemonLinkHack`, `arduino-poke-gen2`, `MrCheeze/pokestadium-ace`, `Goppier/GEN3PokemonDistributions`, `gba-link-connection`, `gba-link-cable-rom-sender`, `usb-gba-multiboot`, `ldn_mitm`, `ryu_ldn_nx`, `pokerom-trader` oltre alla pagina, e i quattro disassemblati pret non ancora clonati, cioè `pokeyellow`, `pokegold`, `pokeruby` e `pokefirered`.

## Livello 4: articoli, blog e ricerca applicata

Ottimi per capire il ragionamento e il contesto, non citabili per un offset.

| Fonte | URL | Che cosa spiega | Track |
|---|---|---|---|
| Project Pokemon, salvataggi 3DS dichiarati corrotti | https://projectpokemon.org/home/tutorials/save-editing/managing-3ds-saves/troubleshooting-corrupt-saves-r92/ | letto il 2026-09-04, ed è la guida del medesimo sito da cui provengono i salvataggi esterni della raccolta. Distingue due situazioni che vanno tenute separate perché hanno cause diverse: il gioco dichiara corrotto un file che il verificatore apre senza problemi, e allora il difetto non è nei dati; oppure nemmeno il verificatore lo apre, e allora il file è rotto davvero, tipicamente per un trasferimento fatto in modo testuale invece che binario. Per la prima situazione, che è la nostra, la guida da' due cause sole e entrambe banali: il file deve chiamarsi esattamente `main`, e nella cartella da cui si ripristina non deve esserci nessun altro file. Vale come fonte di quarto livello e non come documentazione dell'hardware, ma su questo sintomo è la più pertinente che il progetto abbia, ed è quella che sposta l'ipotesi del valore di sicurezza al secondo posto | 3DS, PKD |
| Dev log di Poke Transporter GB | https://www.austinthomasweber.com/poke-transporter-gb | indice della serie, letto, con i dieci URL delle parti | BRI |
| Dev log, parte 0, Introduction | https://www.austinthomasweber.com/poke-transporter-gb/part-0 | letto: l'autore si impone il vincolo di usare lo scambio come meccanismo di trasferimento invece dell'invio diretto, e dichiara di aver scritto un programma proprio perché quello di Lorenzooone non implementava lo scambio | BRI |
| Dev log, parte 1, The GameBoy Advance | https://www.austinthomasweber.com/poke-transporter-gb/part-1 | letto: il multiboot invia una piccola ROM sul cavo e la esegue in WRAM, e da là si accede a ROM e RAM di cartucce diverse | BRI |
| Dev log, parte 2, What's in a Save? | https://www.austinthomasweber.com/poke-transporter-gb/part-2 | letto: quattordici sezioni da 0x1000 byte che ruotano di posizione a ogni salvataggio, doppio file con contatore per riconoscere il più recente, checksum per gruppi di quattro byte, Sala d'Onore che si comporta diversamente. L'autore dichiara Bulbapedia come fonte | BRI, SME |
| Dev log, parte 3, A Link Between Worlds | https://www.austinthomasweber.com/poke-transporter-gb/part-3 | letto: il cavo è SPI con due linee dati, clock e massa; Game Boy a 5 volt e Game Boy Advance a 3.3 volt, e i test di Goppier confermano che la differenza non danneggia nessuno dei due; il clock non deve essere né troppo veloce né troppo lento, ed è stata la parte più frustrante dello sviluppo | BRI |
| Dev log, parte 4, Time for an Upgrade | https://www.austinthomasweber.com/poke-transporter-gb/part-4 | letto: tratta la conversione dei dati, valore di personalità, sezioni cifrate e checksum. Non tratta l'esecuzione di codice, contrariamente a quanto un vecchio handoff aveva ipotizzato dal titolo | BRI |
| Dev log, parte 5, A Quick Break for Creativity | https://www.austinthomasweber.com/poke-transporter-gb/part-5 | letto: grafica presa da altri giochi, font da generazione 1, riquadri di testo da Platino, palette a quattro verdi del Game Boy originale | BRI |
| Dev log, parte 6, Texts and Dexes | https://www.austinthomasweber.com/poke-transporter-gb/part-6 | letto: motore di dialogo a oggetti script, e il Pokedex del programma sta in 1936 byte inutilizzati nell'area della Sala d'Onore del salvataggio, con un flag per ciascuna delle 251 specie | BRI |
| Dev log, parte 7, The Main Event | https://www.austinthomasweber.com/poke-transporter-gb/part-7 | letto ed è la scoperta architetturale più importante: il Pokemon entra in generazione 3 iniettando un evento Dono Segreto nella sezione RAM Script del salvataggio, con 2 byte di checksum, 2 di riempimento e 1000 byte di script che usa CallASM per chiamare il codice del gioco. Quarantotto versioni fra release e lingue, gestite con un compilatore assembly scritto per l'occasione | BRI |
| Dev log, sprite e animazione | https://www.austinthomasweber.com/poke-transporter-gb/blog-post-title-three-r2cs2-y9gym-c5pxe | letto: sprite dei menu di generazione 1 e 2, gestione delle palette e uno script Python di conversione. È la parte titolata A Day-Long Detour, e non tratta l'orologio interno come un vecchio handoff aveva ipotizzato | BRI |
| Dev log, scoperta dell'esecuzione di codice | https://www.austinthomasweber.com/poke-transporter-gb/blog-post-title-three-r2cs2-y9gym-tx7bl | letto ed è la fonte della specifica esatta dell'exploit: una squadra di 352 Pokemon con ID interno 0xE3 seguita da un Pokemon con ID interno 0xFC corrompe lo stack e dirotta l'esecuzione. È la parte titolata The Power of a REALLY Big Party, dove la squadra grande è l'exploit | BRI |
| GBPlay, emulare uno scambio | https://blog.gbplay.io/2021/05/11/Emulating-a-Pokemon-Trade-with-Generated-Link-Cable-Data.html | negoziazione dei ruoli, selezione della modalità e sequenza dello scambio Gen 1 | BRI |
| nitwhiz, falsificare uno scambio | https://blog.nitwhiz.dev/posts/002-pokemon-red-trade/ | i tre blocchi dello scambio e il preambolo 0xFD; da leggere sapendo che sulle dimensioni non concorda con il disassemblato | BRI |
| vaguilar, ACE in Pokemon Rosso | https://vaguilar.com/2015/05/26/arbitrary-code-execution-in-pokemon-red/ | come una lista di specie senza terminatore porta all'esecuzione di codice, con indirizzi concreti | BRI |
| vaguilar, Mew su hardware reale | https://vaguilar.com/2026/02/18/how-i-obtained-mew-in-pokemon-red-on-a-real-game-boy/ | la stessa tecnica portata a termine su console vera con un microcontrollore | BRI |
| RetroReversing, Game Boy | https://www.retroreversing.com/gameboy | letto: da qui vengono `gbtoolsid` per identificare la toolchain di una ROM, `gb-save-states` per gli stati di salvataggio su hardware originale, gli schemi ricreati da Gekkio, e il protocollo della Game Boy Printer con i byte magici 0x88 e 0x33 | BRI |
| Hackaday, il ponte impossibile | https://hackaday.com/2021/12/07/bridging-game-worlds-with-the-impossible-pokemon-trade/ | letto: il ponte di Goppier è un PCB semplice con le porte per i due tipi di cavo e un microcontrollore ARM Cortex in mezzo che traduce le strutture; l'articolo non pubblica né schemi né sorgenti | BRI |
| RetroReversing, GBA | https://www.retroreversing.com/gba | hub di risorse di reverse engineering per Game Boy Advance | BRI, SME |
| RetroReversing, Rosso e Blu | https://www.retroreversing.com/pokemonredblue | raccolta di strumenti e materiali su Gen 1 | BRI |
| Helix Chamber | https://helixchamber.com/2019/02/16/what-dreams-may-come/ | materiale di prototipazione di Gen 1, contesto storico sui dati interni | BRI |
| Reverse engineering di FireRed | https://betterprogramming.pub/low-level-explorations-reverse-engineering-pokemon-firered-through-rom-hacking-54edfb4426 | racconto didattico di un primo approccio al ROM hacking su Gen 3 | BRI, LDN |
| Guida al trading locale su Switch | https://www.dtgre.com/2026/03/fire-red-leafgreen-switch-local-wireless-guide.html | come funziona lo scambio locale nella versione Switch di Rosso Fuoco e Verde Foglia | LDN |
| Pokemon Rescue | https://pokemonrescue.com/ | servizio di recupero di salvataggi e cartucce dell'autore contattato per posta settimane prima; pertinente al track della batteria e a quello dello scambio fra GBA e Switch | BAT, LDN |
| Drew Works | https://www.drewworks.dev/ | sito dell'autore che lavora sull'adattatore fra GBA e console moderna; da tenere sotto osservazione perché il progetto è in evoluzione e non ancora documentato | LDN |
| ahenley17, profilo | https://x.com/ahenley17 | l'autore dell'adattatore che collega un Game Boy Advance originale all'emulatore ufficiale su console moderna, dimostrato con uno scambio riuscito su Rosso Fuoco e Verde Foglia | LDN |
| ahenley17, dimostrazione dell'adattatore | https://x.com/ahenley17/status/2095628437457088727 | il messaggio originale con la dimostrazione dello scambio fra hardware originale e emulatore ufficiale; dispositivo e software di interfaccia dichiarati ancora in sviluppo | LDN |
| Light_88, ripresa della dimostrazione | https://x.com/Light_88_/status/2095742903649816937 | ripresa della dimostrazione da parte di un account noto della community, con il dettaglio dei giochi coinvolti | LDN |
| Charmi, ripresa della dimostrazione | https://x.com/Charmi/status/2095775258489798852 | seconda ripresa indipendente della medesima dimostrazione | LDN |
| Nintendo Everything, l'elenco dei blocchi cromatici | https://nintendoeverything.com/every-shiny-locked-pokemon-in-2024/ | elenco divulgativo delle specie a cui il gioco impedisce di essere cromatiche, aggiornato al 2024; utile per il perché e per il contesto storico dei blocchi rimossi da distribuzioni successive, non citabile per una decisione senza il riscontro sul dato | PKD |

## Canali e video

Chiedere esplicitamente di battere questo terreno è stata una buona idea, perché alcuni di questi canali sono l'unica documentazione esistente di certe tecniche: gli autori pubblicano in video ciò che non hanno mai scritto. Il limite è l'ovvio, e va tenuto presente: un video non è citabile per un offset e non è diffabile.

La via di recupero è stata trovata e funziona, e va registrata perché non è quella ovvia. La pagina del video si scarica con `curl` locale e contiene il riferimento alla traccia dei sottotitoli automatici, ma l'endpoint che la serve restituisce zero byte a qualunque richiesta che non venga dal lettore vero, con o senza i parametri di formato. La via praticabile è `yt-dlp`, installato su questa macchina il 2026-08-25, che gestisce il token di origine e scarica i sottotitoli automatici senza toccare l'audio; il testo si ripulisce con `tools/vtt-to-text.py`, perché i sottotitoli a scorrimento ripetono ogni riga due o tre volte. Quando i sottotitoli automatici non esistono si passa al riconoscimento vocale locale del progetto `E:\local-audio-transcriptor`, che costa molto più tempo e resta la seconda scelta.

Dieci video sono stati trascritti e letti per intero, sei il 2026-08-25 e quattro il 2026-08-28 per il track delle distribuzioni di eventi, e le righe che seguono dicono cosa hanno reso davvero, non che esistono. Vale la pena registrare il bilancio, perché è controintuitivo: due di questi video sono, su punti specifici, la migliore fonte che il progetto possiede, e uno degli altri non ha reso nulla. Il limite del formato resta quello noto, cioè che un video non è citabile per un offset e non è diffabile, quindi ciò che dicono va confermato sul sorgente prima di finire in codice.

| Canale o video | URL | Perché conta | Track |
|---|---|---|---|
| Goppier | https://www.youtube.com/@Goppier | primo a realizzare il ponte fra Gen 2 e Gen 3, con documentazione sulle due versioni del cavo Link | BRI |
| Goppier, aggiornamento di sviluppo | https://www.youtube.com/watch?v=Qcp4vxyaUJc | trascritto e letto per intero il 2026-08-25, ed è la sola documentazione esistente del suo ponte, oltre a essere la fonte più densa di tutto il livello 4. Documenta sette cose che nessun'altra fonte dice. La prima è il vincolo di sincronizzazione, che è il problema architetturale del ponte: Gen 3 invia la squadra a blocchi di 200 byte, due Pokemon per volta, tre volte, e non consegna i successivi finché non riceve i propri, mentre Gen 2 invia in tre sezioni separate, cioè i dati principali di tutti e sei, poi i nomi degli allenatori originali, poi i soprannomi. Ne segue uno stallo: il ponte non conosce la squadra Gen 3 completa quando Gen 2 gli chiede la propria, e Gen 2 una volta finito di inviare smette anche di ricevere. La sua soluzione è dichiaratamente imperfetta e va conosciuta perché è istruttiva, cioè inviare dati di riempimento che costringono il giocatore ad annullare e ripetere lo scambio, perché al secondo passaggio il dispositivo conosce entrambe le squadre. La seconda è il valore di personalità generato in modo pseudocasuale con i DV come seme, così che lo stesso Pokemon trasferito due volte ottenga lo stesso valore. La terza è il gioco di origine forzato a Rosso Fuoco, perché il valore personalizzato usato prima compariva in Gen 4 come una sequenza di punti di domanda. La quarta è la conferma sul campo che in direzione Gen 3 verso Gen 2 le due proprietà non si possono conservare insieme, perché entrambe derivano dai DV, e la scelta è esposta come una politica commutabile con un pulsante, verde per le statistiche e giallo per l'aspetto, cioè genere, lettera di Unown e lucentezza. La quinta è che le specie introdotte in Gen 3 vengono mostrate come Ditto, perché altrimenti l'indice va in overflow e Gen 2 mostra una specie arbitraria; mosse di Gen 3 e oggetti non convertibili vengono eliminati. La sesta è la verifica della catena completa, cioè Gen 2 verso Gen 3, poi Pal Park verso Gen 4 dopo aver cancellato le MN, poi il laboratorio di trasferimento sulla Via 15 in Gen 5 con il gioco in download play, e infine Bank e Home: tutti accettati tranne uno. La settima, e la più importante per le nostre opzioni implementative, è che ha scritto una ROM GBA personalizzata che parla direttamente con i giochi Gen 2 sul cavo originale, dimostrando che il protocollo si può rispettare da un GBA senza hardware in mezzo | BRI |
| Goppier, primo video del ponte | https://www.youtube.com/watch?v=inMbtwmVlKQ | è l'altra metà del materiale di Goppier, cioè il video che presenta il dispositivo prima dell'aggiornamento. Verificato il 2026-08-26 che non ha sottotitoli, automatici o manuali, quindi richiede riconoscimento vocale locale e resta da trascrivere: è il più importante dei due arretrati, perché il video successivo si riferisce più volte a cose spiegate qui, fra cui la struttura del circuito e la questione se il protocollo del cavo Gen 2 possa essere rispettato direttamente da un GBA | BRI |
| Lorenzooone | https://www.youtube.com/@Lorenzooone | autore di Pokemon-Gen3-to-Gen-X e di PokemonGB_Online_Trades | BRI |
| im a blisy | https://www.youtube.com/c/imablisy | contributi comunitari citati dal progetto di riferimento | BRI |
| RETIRE | https://www.youtube.com/@RETIREglitch | ricerca sui glitch di Gen 1 e 2 | BRI |
| TheZZAZZGlitch | https://www.youtube.com/@TheZZAZZGlitch | primo a rendere affidabile l'esecuzione di codice arbitrario in Gen 1 e 2, dal 2013 | BRI |
| Retro Game Mechanics Explained | https://www.youtube.com/@RGMechEx | spiegazioni al livello del bit di meccaniche interne di console e giochi | BRI, TUTTI |
| Displaced Gamers | https://www.youtube.com/channel/UCWoSKWs8h6lFdiEDAjuIfpA | la serie Behind the Code, analisi del codice originale dei giochi classici | BRI, TUTTI |
| Poke Transporter GB, dimostrazione | https://www.youtube.com/watch?v=47A6p2hH2gU | trascritto con riconoscimento vocale il 2026-08-25 e risultato senza parlato: è una dimostrazione muta, quindi la fonte è visiva e non testuale | BRI |
| Poke Transporter GB, sviluppo | https://www.youtube.com/watch?v=9mSkGhEYBkg | trascritto e letto per intero il 2026-08-25, ed è il racconto in prima persona di come è stato costruito il ponte che oggi funziona meglio. Conferma dall'esterno la scelta del Dono Segreto invece della scrittura diretta del salvataggio, e ne spiega la meccanica: il codice assembly personalizzato viene scritto in una sezione non usata del salvataggio, che l'autore identifica come la sezione 30, e da là viene eseguito con il comando che chiama codice arbitrario, così che l'evento possa depositare fino a trenta Pokemon nel PC del giocatore. Aggiunge quattro dettagli operativi che valgono per il nostro codice. Il primo è un calcolatore che determina automaticamente quale lista di squadra e quali nomi servono a sovrascrivere lo stack, invece di trascrivere valori magici. Il secondo è che l'exploit è stato verificato su tutte le lingue con uno script Python appoggiato alla libreria gen-one-utils, e in ogni lingua è possibile in un modo o nell'altro. Il terzo è la differenza fra le generazioni: in Gen 1 l'exploit sfrutta l'assenza di un limite al numero di Pokemon in squadra, in Giallo è possibile ma più sporco perché manca un Pokemon glitch dal nome vuoto, e in Gen 2 il disegno dei nomi oltre il sesto è stato corretto ma non c'è alcun limite alla lunghezza del nome dell'allenatore, il che rende l'exploit più facile perché il contenuto è sotto controllo diretto. Il quarto è che ha scritto due compilatori dedicati, uno per gli eventi che copre le dodici versioni inglesi di Gen 3 e uno per l'assembly Z80, perché il payload cambia a seconda del gioco con cui si sta parlando. Da qui viene anche la genealogia del problema: Goppier per primo su hardware fisico ma senza schemi pubblicati, poi Lorenzooone con il solo hardware ufficiale via multiboot, e questo progetto nato per risolvere i due limiti di quello, cioè il trasferimento di grandi quantità e la sensazione di ufficialità | BRI |
| Dissezione di un salvataggio di Rosso | https://www.youtube.com/watch?v=VVbRe7wr3G4 | trascritto e letto per intero il 2026-08-25, ed è la conferma indipendente che serviva sul lato Gen 1, ottenuta per una via diversa dalla nostra, cioè il confronto fra due salvataggi che differiscono per un solo campo dentro un editor esadecimale. Conferma per differenza che il nome del giocatore è lungo sette byte e che la codifica non è ASCII, perché la lettera A vale 0x80 e la B vale 0x81, che è esattamente la tabella che il nostro generatore produce dal disassemblato. Conferma il checksum di generazione 1 nella forma che usiamo: si parte da 0xFF e si sottrae il valore di ogni byte da 0x2598 a 0x3522 compresi, e il risultato si scrive a 0x3523; se non torna il gioco dichiara il file distrutto. Documenta poi tre fatti sull'hardware che il progetto non aveva scritto da nessuna parte: la RAM della cartuccia è mappata da 0xA000 a 0xBFFF, cioè otto kilobyte per volta, e i giochi Pokemon ne usano quattro banchi commutati scrivendo due bit nell'area da 0x4000 a 0x5FFF, che appartiene alla ROM e viene riusata come registro di configurazione perché scrivere su una memoria di sola lettura non avrebbe altro significato; la RAM esterna si abilita e si disabilita scrivendo 0x0A oppure zero nell'area da 0x0000 a 0x1FFF, e il gioco la tiene abilitata solo il tempo del salvataggio, il che spiega perché in un debugger a volte appare vuota; il file `.sav` di un emulatore è esattamente un'immagine di quella RAM, quindi lavorare sul file e lavorare sulla cartuccia sono la stessa operazione su due supporti | BRI |
| Cavo Link negli emulatori | https://www.youtube.com/watch?v=jzLISDGrOWo | trascritto e letto il 2026-08-25, e ha reso poco perché mostra più di quanto spieghi: ottocento caratteri in tutto. Quel poco è comunque pertinente al collaudo e va registrato invece di essere buttato, cioè che su Game Boy Advance il cavo emulato funziona con un clic su mGBA e con qualche configurazione in più su VisualBoyAdvance, che entrambi permettono la connessione via rete con risultati variabili, e che sui giochi Game Boy il supporto di quei due è difettoso o assente, tanto che l'autore per quelli usa BGB. È una conferma per esperienza di terzi della scelta di collaudo che avevamo già fatto, cioè BGB per il lato Game Boy | BRI |
| Scambio locale su Switch in FRLG | https://www.youtube.com/watch?v=epCf87MTLnk | la funzione di scambio locale nella versione Switch vista dal lato utente, che è il presupposto del track LDN. Verificato il 2026-08-26 che non ha sottotitoli di alcun tipo, quindi richiede riconoscimento vocale locale e resta da trascrivere | LDN |
| Sostituzione della batteria di cartuccia | https://www.youtube.com/watch?v=vz05ZT63Jqc | trascritto e letto per intero il 2026-08-25, e documenta la tecnica che permette di sostituire la batteria di una cartuccia senza perdere il salvataggio, che è l'unico modo di farlo quando il salvataggio conta. Il principio è che la RAM della cartuccia è volatile e vive solo perché la batteria la alimenta, quindi la sostituzione si esegue a cartuccia inserita in una console accesa, che fornisce corrente al posto della batteria durante lo stacco: l'autore usa un Game Boy Advance perché lascia più spazio attorno alla cartuccia rispetto a un Game Boy Color, e la console resta accesa dal primo al secondo punto di saldatura. Servono un cacciavite a testa triangolare, una batteria di ricambio, per Giallo una CR2025, un saldatore e una pinzetta. Due avvertenze sono esplicite: la polarità va verificata sulla scheda perché non tutte le batterie di ricambio hanno la linguetta positiva sullo stesso lato, e le linguette nuove sono più grandi delle originali, quindi serve più stagno di quanto la piazzola ne porti. La verifica finale è un ciclo di alimentazione completo, cioè spegnere, estrarre, attendere e riaccendere: se la connessione non è buona il salvataggio si perde in quel momento e non prima. Da qui viene anche la distinzione che il track Smeraldo deve tenere presente: su Gen 1 e 2 il rischio è la batteria esaurita, su Gen 3 il salvataggio sta in memoria flash che non dipende dalla batteria, e la batteria serve solo all'orologio interno | SME |
| MankeyMite, non trasferire in Home prima di aver visto questo | https://www.youtube.com/watch?v=KtJGkd0Qvvg | trascritto e letto per intero il 2026-08-31, ed è la fonte più importante dei due track nuovi oltre che una correzione alla pianificazione dell'intero progetto. Tre cose. La prima è la catena ufficiale descritta passo per passo, che conferma quanto il progetto aveva già stabilito e aggiunge tre dettagli operativi: il Parco Amico richiede di avere battuto i capi dei Quattro e ottenuto il registro nazionale, sta sulla Via 221 nei primi tre giochi di quarta generazione e a Fucsiapoli negli altri due, e il passaggio verso la quinta generazione richiede il laboratorio sulla Via 15 dopo essere diventati campione. La seconda, che il progetto non aveva registrato, è che il trasferimento da Bank a Home richiede il piano a pagamento di Home, mentre Bank è gratuito, e che il piano gratuito di Home conserva trenta esemplari. La terza, e la più rilevante, è la risposta alla domanda sulla legittimità: Home conserva sul proprio lato l'informazione di quale via un esemplare abbia usato per entrare, quindi a parità di dati sottostanti non è garantito che un esemplare entrato dalla versione su console sia indistinguibile da uno passato per Bank, e i controlli che il servizio applicherà non sono noti perché la compatibilità non è ancora in funzione. Chiude con la raccomandazione che il progetto adotta: ciò che si può trasferire ora per la via ufficiale si trasferisce ora, senza attendere alcun aggiramento | ACE, EVT, 3DS, LDN |
| MankeyMite, un anno per il costruttore di esemplari Gen 3 | https://youtu.be/KvcmsxyHIX8 | trascritto e letto per intero il 2026-09-04, ed è la presentazione fatta dall'autore dello strumento che il progetto aveva già letto nel sorgente il 2026-09-01: non aggiunge nulla sul metodo di generazione, che avevamo verificato sul corpus, e aggiunge invece cinque fatti che il sorgente non dichiara. Il primo, e il più utile all'ambito, è che il costruttore non si limita alle distribuzioni ma espone anche gli incontri di Colosseum e XD, quelli selvatici e quelli da uovo, e che le mosse esclusive di XD sono selezionabili soltanto passando per quell'insieme: la portata dello strumento è dunque più larga della tabella delle carte meraviglia su cui il nostro asse degli eventi è costruito. Il secondo è che il giudizio di legittimità è reso da PKHeX Core eseguito nel browser e viene dato separatamente per la cartuccia e per la riedizione su console, e che sulla seconda cadono i nastri impossibili, gli incontri non scambiabili e gli oggetti non distribuiti: è la conferma pratica, su un caso mostrato, del marchio di origine che il track ACE aveva dedotto dal codice. Il terzo è la raccomandazione dell'autore, che coincide con il piano di questo progetto, cioè produrre sulla cartuccia e percorrere la catena, perché il deposito tratta l'esemplare come un trasferimento da Game Boy Advance. Il quarto è l'allestimento dello scrittore in base 64 attribuito a Mettrich, chiamato Weldr, con la specie stabile 0x410E, i tre codici in sequenza, le scatole da 11 a 14 come ambiente di esecuzione e un carico aggiuntivo che registra nel Pokedex l'esemplare creato. Il quinto è una dichiarazione dell'autore che vale come avvertenza sul corpus e non come critica: le centinaia di voci da evento sono nel costruttore ma non sono state provate tutte, quindi la concordanza che il nostro confronto ha misurato resta la misura migliore che abbiamo e non è garantita dall'autore | ACE, EVT |
| Regole del Parco Amici, consegnate dall'utente | https://nintendon.it/2026/02/28/30-anni-pokemon-guida-trasferimenti-generazioni-315363 | consegnate dall'utente il 2026-09-04 con quattro collegamenti di appoggio, di cui due su Reddit e uno su un video, non recuperabili dagli strumenti di sessione per la ragione già documentata. Confermano il fatto che il progetto aveva già registrato, cioè che in HeartGold e SoulSilver non esiste alcun limite giornaliero mentre Diamante, Perla e Platino ne hanno uno di un trasferimento ogni ventiquattro ore, e aggiungono quattro regole operative che il progetto non aveva e che entrano nei conti. La prima è che i gruppi sono esattamente di sei. La seconda, che è quella che decide il tempo di una sessione, è che i sei vanno catturati dentro il parco prima di potere avviare un trasferimento nuovo: la sessione non è quindi un'operazione di menu ma una caccia, e il suo costo va cronometrato. La terza è che un esemplare che conosca una macchina nascosta non si trasferisce e la mossa va tolta prima con l'Eliminamosse, ed è un vincolo che tocca cinque voci del nostro catalogo di terza generazione. La quarta è che serve un Nintendo DS o un DS Lite, perché occorre lo slot per le cartucce di Game Boy Advance | PKD, EVT |
| amiibodoctor, generare Pokemon per Champions | https://amiibodoctor.com/2025/08/25/how-to-generate-pokemon-to-use-in-pokemon-champions/ | letto per intero il 2026-09-01, recuperato con una richiesta locale al primo tentativo dopo essere stato catalogato come non letto per un giorno. Contro le attese ha reso molto più di una procedura, e la parte che vale è la descrizione del tracciatore di Pokemon Home: assegnato quando un esemplare tocca il servizio per la prima volta, permanente, invariante rispetto a ogni modifica successiva, ed è il modo in cui il servizio stabilisce da dove un esemplare provenga davvero. La fonte dichiara che è questo il tratto che distingue di più il controllo del servizio da quello dell'editor della comunità, e che un identificativo scritto a mano viene rilevato come falso perché il servizio non lo ha mai emesso: il tracciatore non è un campo del dato ma un riferimento a un archivio che sta dall'altra parte. Ne dichiara tre usi, cioè distinguere gli esemplari, rilevare i caricamenti duplicati da più account, e ricostruire lo stato di un esemplare gioco per gioco. Enuncia inoltre le cinque categorie che il servizio controlla, cioè compatibilità di gioco, legalità del contenitore che il servizio conserva e mostra, dati di evento che indica come causa tipica del rifiuto, sequenze di mosse conservate separatamente per ciascun gioco, e blocchi sulla lucentezza gestiti a mano dal titolare. Identifica infine il servizio di generazione che il track aveva registrato, dichiarando che non consente di scegliere il nome dell'allenatore e che ogni esemplare con quel nome è quindi riconoscibile. La sintesi sta in `generation-from-switch/STUDIO-01-scambio-automatico-e-provenienza.md`. È una fonte di quarto livello e la sua concordanza con il server della comunità sul tracciatore, indipendente e a un anno di distanza, è il grado di fiducia massimo ottenibile su una materia che il titolare del servizio non documenta | GEN, ACE, EVT |
| Goppier, la ricreazione delle distribuzioni Gen 3 | https://www.youtube.com/watch?v=NKBb-YS34wg | trascritto e letto per intero il 2026-08-28, ed è la fonte tecnica principale del track EVT e la sola esistente sul formato interno di una ROM di distribuzione. Il multiboot si trova nella ROM confrontando i byte che passano sul cavo, e si decomprime chiamando la funzione di BIOS che la fonte indica con il numero 11, dopo aver letto metodo e dimensione dalle prime parole del blocco compresso; la difesa è un checksum additivo su tutti i byte della ROM confrontato con un valore precalcolato, e l'errore numero 5 è il suo fallimento. La scoperta più utile per chi ricrea è che il programma di distribuzione riusa il codice del gioco, dove ogni parametro dell'esemplare ha un indice: cambiando l'indice si imposta un parametro diverso, ed è così che è stato ottenuto il nastro nazionale riusando il codice del flag di obbedienza. Documenta poi il ciclo anti-lucentezza e la sua disattivazione, il gruppo di esperienza da dichiarare, il flag che fa scegliere l'abilità dal primo bit del valore di personalità, la sesta chiamata del generatore divisa per tre che decide la bacca tenuta, e la posta, che ha richiesto di leggere e riscrivere il salvataggio. Su quest'ultimo punto conferma per via indipendente le quattordici sezioni, la rotazione fra gli slot e la doppia copia che il progetto ha verificato sul disassemblato, e aggiunge che la posta sta nella sezione quattro, dato non ancora verificato. Chiude un caso indeterminato per ricerca esaustiva sui 65536 semi possibili, trovando l'unico compatibile, cioè 0x6065, e ne lascia due aperti dichiarando improbabile la propria ipotesi | EVT, BRI |
| im a blisy, eventi e-Reader su cartuccia vera | https://www.youtube.com/watch?v=fK-Actf6kME | trascritto e letto per intero il 2026-08-28, ed è la fonte operativa del track EVT. Distingue il Dono Segreto dall'Evento Mistero, che non sono la stessa funzione, e documenta che in Smeraldo la seconda è stata rimossa dai menu e si riapre soltanto ricevendo un programma attraverso la prima. Le vie di iniezione sono quattro: due istanze di mGBA collegate con l'e-Reader come giocatore due, che pretende il BIOS reale estratto dall'hardware perché la sua ricostruzione manda gli eventi in errore, e l'orologio interno spento; l'e-Reader reale con un salvataggio da 128 KiB, con il capo largo del cavo nell'e-Reader; la scheda riprogrammabile con un salvataggio da 64 KiB; e la stampa delle carte con il codice a punti, a seicento punti per pollice su carta lucida, dichiaratamente capricciosa fino al punto di richiedere il driver sbagliato della stampante. Resta la via dell'iniezione diretta nel salvataggio con un editor di carte meraviglia, che porta l'avvertimento adottato come regola del track: se una carta è già presente va esportata prima di scrivere, perché può essere un evento non ancora preservato. Cita GBxCart RW fra i lettori raccomandati | EVT, SME |
| Hard4Games, la macchina del Pokemon Center di New York | https://www.youtube.com/watch?v=AVhqlol6k9o | trascritto e letto per intero il 2026-08-28, ed è la fonte storica su un apparecchio che si credeva distrutto. Il negozio aprì il 16 novembre 2001 e chiuse per ristrutturazione nel gennaio 2005, con divieto di fotografie che spiega la scarsità della documentazione; le campagne di seconda generazione andarono dal 22 novembre 2001 al 7 marzo 2003 e quelle di terza dal 30 agosto 2003 al 16 dicembre 2004. Ciò che è stato preservato sono due dischi in un formato proprietario di sviluppo leggibile solo da lettori dedicati, quattro schede di campagna che dichiarano gli esemplari e la finestra temporale, e due schede che fanno da chiave. Due dettagli contano per la ricreazione: l'orologio interno del GameCube deve cadere dentro la finestra della campagna, e il trasferimento passa da uno scrittore dedicato collegato alla console, mentre il Game Boy Advance sul cavo è scenografico, cosa che la fonte dichiara di aver verificato. Gli esemplari portano il nome del negozio con la postazione come allenatore originale e un identificativo incrementato a ogni distribuzione | EVT |
| SuperrSonic, contenuti bonus dal Game Boy Player | https://www.youtube.com/watch?v=GBEMP2kEpPw | trascritto e letto per intero il 2026-08-28, e apre una via che nessuna delle altre fonti del track nomina: l'interfaccia alternativa del Game Boy Player invia un programma multiboot senza alcun cavo, perché il collegamento fra console e periferica è interno, ed estrae BIOS, ROM e salvataggio potendo poi ripristinare quest'ultimo. L'intero ciclo di modifica avviene quindi sulla console, senza calcolatore né lettore esterno. Il programma dell'autore trasferisce il Jirachi del disco bonus, il Celebi non utilizzato della versione giapponese, un Pikachu, il Mew dell'evento e le uova di Pokemon Box. Il contributo più utile all'obiettivo di collezione non è però un esemplare ma un oggetto, perché il quiz del disco bonus consegnava i biglietti degli eventi e, su un salvataggio di Smeraldo, la mappa marina che porta all'incontro con Mew. L'autore dichiara di aver implementato i checksum leggendo Bulbapedia, che è la fonte su cui questo registro documenta già un errore in quella materia | EVT |
| Checkpoint su 3DS | https://www.youtube.com/watch?v=aZMVFBRp1xI | trascritto e letto per intero il 2026-08-25, ed è la fonte operativa sul backup dei salvataggi per il track 3DS, con un confronto diretto fra i due gestori. Documenta il flusso che ci interessa da vicino: Checkpoint distingue nella schermata se il salvataggio viene dalla cartuccia o dalla scheda SD, permette il backup con un nome scelto sul momento e la selezione multipla per salvare più titoli in un colpo, e consente di ripristinare in una copia digitale il salvataggio letto dalla cartuccia, così che la cartuccia possa restare nella custodia. La sequenza completa che mostra è quella che il nostro track userebbe, cioè dump della cartuccia con GodMode9, installazione della copia con FBI, primo avvio per far creare il salvataggio, e poi ripristino del backup della cartuccia dentro la copia installata. Due limiti vanno registrati perché cambiano la scelta dello strumento: Checkpoint richiede il custom firmware e non basta l'homebrew, mentre JKSM funziona anche su una console con solo homebrew, ed è quindi l'unica via su un dispositivo non modificato del tutto. I percorsi sulla scheda SD sono `3ds/Checkpoint/saves/` per uno e `JKSV/saves/` per l'altro, e da là i file si copiano via FTP oppure estraendo la scheda. Documenta infine che esiste anche il backup dei dati extra, che sono quelli creati al primo avvio di un titolo e servono per alcuni exploit | 3DS |

### Reddit, ricerche del 2026-08-26

Reddit non è raggiungibile né dal crawler del modello né da alcun motore alternativo provato, come documenta `.claude/rules/web-sources-not-fetchable.md`, quindi anche il solo ritrovamento degli indirizzi passa dall'utente. Le ricerche sono state concordate come filtri e consegnate come schermate. Il bilancio va scritto perché è istruttivo: la resa è stata molto inferiore a quella dei canali Discord, e la ragione è strutturale. Reddit è un forum di supporto generalista dove la ricerca a testo pieno pesca titoli di richieste di aiuto, mentre i canali letti il giorno prima sono luoghi dove si discute il codice. Su tre filtri su cinque la resa è stata nulla, e questo è a sua volta un dato.

| Fonte | Link | Cosa documenta in modo autorevole | Track |
|---|---|---|---|
| Reddit, sintesi con fonti su Poke Transporter GB | https://www.reddit.com/r/pokemon/ | l'unico blocco di questa passata con resa alta, prodotto dalla funzione di sintesi di Reddit su otto post di r/Games, r/pokemon, r/AnaloguePocket, r/PokemonHome e r/3dspiracy. Documenta che il tool modifica entrambi i salvataggi e lo dichiara all'utente, che va usato il file `.gba` della release e non il sorgente compilato, e che i dispositivi a FPGA come Analogue Pocket probabilmente non lo supportano perché la procedura richiede lo scambio a caldo della cartuccia mentre il programma gira. Sulla compatibilità conferma che gli offset di ROM e salvataggio vanno determinati per tipo, versione e lingua, che è l'origine delle quarantotto combinazioni. Il fatto più rilevante è che la rimozione del Pokemon dal salvataggio di partenza non c'era nelle prime versioni e vi è stata aggiunta proprio grazie all'esecuzione di codice arbitrario: è la risposta al perché quella tecnica serva, ed era la lamentela più comune. Sulla conversione delle statistiche la domanda è stata posta pubblicamente e non ha ricevuto risposta | BRI |
| Reddit, r/Gameboy, ricerche sui salvataggi | https://www.reddit.com/r/Gameboy/ | filtri `save write failed` e `Flashrom Type not supported`. Il secondo riguarda le cartucce EZ Flash e non i giochi originali, quindi non serve. Il primo individua tre discussioni pertinenti al track Smeraldo, non ancora aperte: una sui salvataggi che GBxCart non scrive, una sul recupero di un salvataggio di vent'anni da una cartuccia contraffatta di Rosso Fuoco, e una su un backup di Pokemon Blu che non funziona negli emulatori | SME |

### Canali di community letti il 2026-08-26

Queste due voci sono state lette per la prima volta il 2026-08-26, con la ricerca interna al canale e la consegna manuale del contenuto, secondo la procedura di `.claude/rules/web-sources-not-fetchable.md`. Non sono più fra le fonti soltanto catalogate.

| Fonte | Link | Cosa documenta in modo autorevole | Track |
|---|---|---|---|
| Pokemon Multiplayer Research, canali di supporto e generale | https://discord.gg/nBnTrv3UMn | letto con i filtri `monitor mode`, `adapter`, `AC600`, `T2U` e `8811`. Ha corretto tre cose che il progetto dava per certe: il chip degli adattatori AC600 provati con successo è un RTL8821CU servito dal driver in albero `rtw88`, dichiarato da un utente come `driver: rtw_8821cu`, e non un RTL8811AU; il Wireless Adapter del Game Boy Advance non è 802.11 ma un progetto proprietario, quindi nessuna scheda Wi-Fi può parlargli e la via è un microcontrollore che lo emula, che è l'opzione D di ADR-008 confermata da fonte indipendente; l'emulatore sulla console riproduce quel dispositivo in emulazione di alto livello, dove risulta sempre collegato, e non riproduce il cavo Link. Documenta inoltre che su Windows funzionano solo adattatori USB e su Linux anche interni, che le schede Intel non fanno modalità monitor, che il giocatore simulato senza Pokedex nazionale fa rifiutare molte specie e si corregge imponendo `0x0F` alle sue flag di progressione, che gli oggetti tenuti non passano nello scambio, e che il GBxCart RW o il GB Operator servono a produrre i `.pk3` di partenza da cartucce proprie. Il filtro `8811` non ha dato alcun risultato, quindi sul chip dell'adattatore in mano all'utente non esiste testimonianza | LDN, BRI |
| Glitch City Research Institute, canali per generazione | https://discord.com/invite/EA7jxJ6 | letto con i filtri `TRAINER 4`, `0xFC` e `party overflow`. Ha portato tutto ciò che il progetto sa sull'esecuzione di codice in generazione 3, che prima non copriva: 0xFC introduce un codice di controllo e 0xFD la sostituzione di una variabile nel motore di stampa del testo, e in Rubino e Zaffiro quelle funzioni sono prelevate da una tabella di puntatori senza controllo dei limiti mentre nelle altre tre versioni passano da un costrutto di scelta multipla che rende inerte un indice fuori intervallo, quindi la via esiste solo in Rubino e Zaffiro. La catena documentata su Smeraldo parte da una posta rimossa fuori da un edificio, che lascia una stringa non terminata, e attraversa la struttura secondaria e le tendenze di una città fino ai dati della squadra, dove l'ordine dei campi letti conferma dall'esterno il layout della sezione 5 della referenza. Dal lato generazione 2 documenta che un identificativo dell'allenatore contenente il byte 0xFF impedisce il traboccamento della squadra, perché introduce un terminatore dove non era previsto, e che il traboccamento sfruttato dal cosiddetto virus è proprio la stampa dei nomi delle specie della squadra avversaria nella schermata di scambio | BRI |
| GBAtemp, correzione dei salvataggi in Virtual Console | https://gbatemp.net/threads/tutorial-fix-all-save-problems-for-pokemon-games-vc-gba.433266/ | letto il 2026-08-26 nella prima delle tre pagine. Va registrato per ciò che è: riguarda i giochi iniettati come Virtual Console su Nintendo 3DS e non le cartucce fisiche, quindi non risponde alla domanda del sottoprogetto Smeraldo per cui era stato cercato, e serve al track 3DS se un giorno si iniettassero ROM proprie. La prima parte modifica la ROM cercando la sequenza `D0 88 8D 83 42` e azzerando due byte fra quella e `24 10 49 10 68`; la seconda rimuove il messaggio di salvataggio corrotto con offset dichiarati per Rubino e Zaffiro americani e francesi e per Smeraldo. Il thread stesso ne mostra i limiti, perché un utente riporta che quella sequenza non esiste in Rubino e Zaffiro americani, dove al suo posto c'è `6C 08 83 42 00 00 00 00 24 10 49 10 68` a 0x1DFB5E e 0x1DFAEE con i byte da azzerare già nulli, e perché gli offset della seconda parte per Rosso Fuoco e Verde Foglia non sono mai stati trovati in undici mesi di richieste | 3DS |
| Le configurazioni delle macchie di Spinda | https://www.youtube.com/watch?v=g5nZTDaGH64&t=23 | non recuperabile dagli strumenti di sessione, che su questo dominio ricevono una pagina di consenso: è un luogo dove cercare e non una fonte letta. Documenta che la posizione delle quattro macchie discende dai quattro byte del valore di personalità, quindi lo spazio ha cardinalità due alla trentaduesima | PKD |
| I blocchi cromatici, panoramica | https://www.youtube.com/watch?v=v6Lq1Cac_jM&t=20 | non recuperabile, stessa ragione; nominata dall'utente come sorgente dell'elenco dei blocchi | PKD |
| I blocchi cromatici, sintesi breve | https://www.youtube.com/shorts/efoQSb4haOo | non recuperabile, stessa ragione | PKD |
| I blocchi cromatici, sintesi su TikTok | https://www.tiktok.com/@yokevdog/video/7342262356958825774 | non recuperabile dagli strumenti di sessione; nominata dall'utente accanto alle precedenti | PKD |

## Livello 5: forum e community

Rispondono a domande che non hanno una risposta scritta altrove. Una risposta in un thread non è una fonte finché non è verificata. La clausola che stava qui dal 2026-08-25, cioè che i thread su Reddit non fossero stati letti perché il dominio non è raggiungibile, non vale più dal 2026-09-07: la settima via della regola sulle fonti non recuperabili, cioè l'archivio pubblico Arctic Shift interrogato da `tools/fetch-reddit.py`, li rende leggibili senza credenziali. Le voci Reddit ancora marcate come non lette lo sono per debito di lettura e non per indisponibilità, che è una differenza sostanziale: si chiudono lanciando lo strumento.

| Luogo | URL | Ambito | Track |
|---|---|---|---|
| MankeyMite, Discord | https://discord.com/invite/rjQGPhG7e3 | esportato il 2026-09-01 con ventiquattro canali e centounomilaottocentodiciassette messaggi, e interrogato per le domande che il progetto aveva dichiarato aperte invece di essere letto: la sintesi con le attribuzioni sta in `poke-ace/STUDIO-03-la-risposta-della-comunita-e-le-due-severita.md`. È la fonte che corregge la parte più importante dello Studio 01, perché stabilisce che i verificatori sono tre con severità decrescente, cioè lo strumento della comunità che pretende la corrispondenza fra valore di personalità e identificativi, il servizio che rileva i soli errori clamorosi come un luogo di incontro impossibile, e il gioco competitivo che squalifica. Porta inoltre quattro fatti che il progetto non aveva: il tracciatore univoco che il servizio assegna a ogni esemplare in ingresso, che rende l'esame permanente invece che istantaneo; la via composta per la terza generazione, che era un'inferenza marcata come tale e ora è attribuita al suo autore, e che non richiede lo scambio in rete perché l'esemplare si ricostruisce dentro la riedizione; il fatto che l'esecuzione di codice funzioni sulla riedizione per console moderna, con codici diversi da quelli su cartuccia per via del filtro sulle parole vietate; e la cifra di quattrocento esemplari da distribuzione, con la dichiarazione che non si finisce prima della chiusura del servizio. L'utente ne fa parte. È il server dedicato all'esecuzione di codice arbitrario in terza generazione, e il suo canale `ace-links` è la fonte dell'inventario degli strumenti registrato ai livelli superiori: l'elenco è stato consegnato dall'utente il 2026-08-31. Va corretta una valutazione mia del medesimo giorno: nell'inventario dei server accessibili avevo marcato questo come non valutato e presumibilmente personale, sulla base del solo nome, e non lo è. Il server è pertinente e va aggiunto alla tabella dei canali di `tools/export-discord.py` | ACE, EVT |
| berichandev, canale di trasmissione | https://www.twitch.tv/berichandev | letto il 2026-09-01 su consegna dell'utente come schermata del canale in diretta, che è la quarta via della regola sulle fonti non recuperabili ed è bastata perché i pannelli descrittivi contengono per esteso le quattro cose che si cercavano. Il servizio è attivo. Opera su cinque titoli, cioè i due dell'ottava generazione, le riedizioni della quarta, il primo titolo a mondo aperto, i due della nona e il titolo più recente, ciascuno con un comando di richiesta proprio e un'attesa dichiarata nell'ordine dei decimi di minuto. Dichiara di soddisfare gratuitamente qualunque richiesta di esemplare cromatico, e mostra fra i propri programmi automatici uno dedicato ai leggendari della nona generazione qualificati come conformi al deposito in rete. Il canale ospita insieme una seconda attività distinta, cioè incontri di gruppo a lucentezza forzata, dove l'esemplare lo si cattura da sé e la provenienza è quindi diversa. Due esiti vanno registrati come tali. Il primo è una correzione alla fonte di quarto livello che descriveva questo servizio al settembre 2025: il nome dell'allenatore non è più fisso, e i pannelli dichiarano che l'esemplare viene inviato con l'identificativo e il nome di allenatore del richiedente dove ciò sia possibile. Cade quindi il criterio di riconoscimento più economico che esistesse, mentre non cade nulla di ciò che riguarda la storia dell'esemplare. Il secondo è una tensione con la medesima fonte che il progetto non può risolvere leggendo: il servizio dichiara ogni richiesta conforme, mentre quella fonte afferma che un esemplare che non possa esistere senza essere passato dal deposito viene atteso con una storia di tracciatore che non c'è. Le due affermazioni non sono compatibili nel caso dei leggendari, e si risolvono con una misura e non con una terza fonte, cioè aprendo un esemplare ricevuto con il verificatore di conformità. La descrizione precedente, del 2026-08-31, resta qui per memoria di come la fonte era catalogata prima di essere letta. La fonte di quarto livello letta quel giorno lo identifica come il servizio di generazione gratuito più diffuso, e dichiara che non consente di scegliere il nome dell'allenatore di provenienza, il quale resta il proprio: ne segue che ogni esemplare così ottenuto è riconoscibile come costruito, e la fonte lo scrive senza attenuazioni. Quella descrizione è però al settembre 2025 e in questo dominio un anno è molto: ciò che manca e che soltanto la fonte diretta può dare è lo stato corrente, cioè se il servizio sia ancora attivo, su quali titoli operi oggi, se il nome dell'allenatore sia ancora fisso, e quali specie e forme copra. L'ultima delle quattro è la domanda che dice se il track serva all'obiettivo o soltanto lo tocchi | GEN |
| Pokemon HOME Checklist, Living Dex e marchi di origine | https://jacs720.github.io/Home-Checklist/ | letta il 2026-08-31, e il modo va dichiarato perché qualifica il grado di fiducia. La pagina è una applicazione a pagina singola e una richiesta HTTP ne restituisce il solo involucro: il contenuto è stato ricavato sondando per costanti il fascio JavaScript compilato, da cui enumerazioni, valori di configurazione ed etichette di interfaccia sono leggibili in chiaro anche dopo la minimizzazione. Ne è venuto il modello dei dati completo, cioè undici marchi di origine fra cui uno dedicato alla terza generazione e trattato nel codice come non ancora ottenibile, undici collezioni di provenienza speciale, quindici profili di collezione predefiniti, quattro livelli di reperibilità di cui uno esplicitamente ipotetico, e l'insieme dei ventitré mitici da evento. Il catalogo delle singole specie non è stato enumerato, perché non compare in chiaro e nessun servizio di dati esterno lo fornisce. La sintesi sta in `poke-ace/STUDIO-02-marchi-di-origine-e-che-cosa-conta-una-collezione.md` | ACE, GEN, EVT |
| Pokemon Multiplayer Research, Discord | https://discord.gg/nBnTrv3UMn | 377 membri, l'utente ne fa parte dal 2026-08-26 su segnalazione di uno degli autori dei video. È il più utile dei cinque per il track LDN, e ha già prodotto la sola testimonianza di campo che il progetto possiede sulle schede Wi-Fi capaci di modalità monitor, cioè che un TP-Link AC600 funziona mentre una Intel Pro Wireless 5100 AGN integrata non funziona. Il canale da guardare è quello di supporto, dove si allestisce il gioco in rete locale fra emulatore e console | LDN, BRI |
| PRET, Discord | https://discordapp.com/invite/vdTW48Q | la community dei disassemblati e delle decompilazioni, cioè gli autori delle fonti di livello 1 di questo progetto. La struttura dei canali, vista il 2026-08-26, ha una sezione per ciascun disassemblato, cioè pokered, pokecrystal, pokeruby, pokefirered, pokeemerald e i quattro di quarta generazione, più i canali di contribuzione asm2c e git e uno di risorse: ne segue che una domanda sui formati va nel canale del gioco pertinente e non in uno generico. La domanda che il progetto ha in sospeso per loro è la formula esatta di conversione da Stat Experience a Effort Value, che nessuna implementazione pubblica pubblica | BRI, SME |
| Glitch City Research Institute, Discord | https://discord.com/invite/EA7jxJ6 | la community che studia i glitch e l'esecuzione di codice arbitrario in generazione 1 e 2, cioè esattamente la tecnica su cui poggia il trasferimento vero invece della clonazione. La domanda in sospeso per loro è se il vettore che PokeTransporter GB usa, cioè l'identificativo interno 0xFC in coda a una squadra di 352 Pokemon, coincida con il punto di ingresso noto come TRAINER 4: è una congettura del progetto e non è verificata | BRI |
| GBAdev, Discord | https://discord.gg/ctGSNxRkg2 | la community dello sviluppo homebrew su Game Boy Advance e della sua toolchain, citata dall'autore di PokeTransporter GB come una delle due risorse che gli hanno permesso di partire senza esperienza sulla piattaforma. La domanda in sospeso per loro è se qualcuno abbia già collaudato il protocollo del cavo contro BGB via TCP, perché è il collaudo che il progetto intende fare e vale sapere in anticipo dove si rompe | BRI |
| Hex Maniac Advance, Discord | https://discord.com/invite/x9eQuBg | la community dell'editing di ROM di terza generazione, che serve ai due track che toccano Gen 3, cioè la correzione dello zaino di Smeraldo e il lato di destinazione del ponte | BRI, SME |
| Project Pokemon, protocollo Link Gen 1 | https://projectpokemon.org/home/forums/topic/58858-generation-1-link-protocol/ | letto: un gruppo ha costruito un dispositivo che fa da sorgente di clock per il protocollo, ha collaudato su BGB e ha completato scambi via internet fra due Game Boy reali nel 2021; da qui viene la scoperta dell'organizzazione CableClub | BRI |
| Project Pokemon, salvataggio Smeraldo corrotto | https://projectpokemon.org/home/forums/topic/61118-pok%C3%A9mon-emerald-gba-corrupt-save-file/ | letto: su cartuccia contraffatta entrambi gli slot contenevano un salvataggio d'inizio partita e i dati non erano corrotti ma assenti; insegna a distinguere corruzione da perdita, e che la dimensione dichiarata al software di dump cambia ciò che si legge | SME |
| Project Pokemon, algoritmo di generazione degli eventi Gen 3 | https://projectpokemon.org/home/forums/topic/39517-gen-3-event-generation-algorithm-research-10anniv-etc/ | letta il 2026-08-29 e utile per una cosa sola: dice come la conoscenza dei metodi è stata ottenuta, cioè per reverse engineering a partire da campioni raccolti e non da una specifica, il che spiega perché alcuni eventi restino non chiusi e perché la richiesta pubblica di campioni sia il modo in cui quella ricerca avanza. Riporta che il metodo di uno degli eventi dei negozi è stato risolto come variante a semi non ristretti in cui la metà alta del valore di personalità è in or esclusivo con la metà bassa, con l'identificativo dell'allenatore e con quello segreto. Sul dettaglio non è citabile: la forma consolidata della medesima conoscenza è la tabella di PKHeX | EVT |
| Project Pokemon, oggetti nella tasca sbagliata | https://projectpokemon.org/home/forums/topic/64794-pokemon-emerald-items-are-in-the-right-bag-using-the-app-but-when-i-load-it-into-a-cartridge-they-go-in-the-wrong-slots/ | letto, ed è la fonte più utile del livello 5: un editor aveva identificato un salvataggio di Smeraldo come Rubino o Zaffiro, e gli oggetti sono finiti negli slot sbagliati. Da qui il rilevamento automatico del gioco in `emerald_bag_decode.py` | SME |
| PokeCommunity, problema grave dello zaino in Smeraldo | https://www.pokecommunity.com/showthread.php?p=8992088 | letto dagli screenshot dell'utente e NON pertinente: il thread è del 2015 nella sezione di ROM hacking binario, e riguarda uno sprite corrotto della borsa in una modifica del gioco, che fa resettare la console quando si apre lo zaino in battaglia. Non ha nulla a che vedere con la corruzione di un inventario su un salvataggio reale. Era un falso positivo della mia ricerca, e la riga resta solo perché non venga ripescata | SME |
| GBAtemp, salvataggio Smeraldo non scrivibile | https://gbatemp.net/threads/save-failed-on-real-pokemon-emerald.645336/ | letto dagli screenshot dell'utente ed è il thread più importante per il track Smeraldo: su cartuccia genuina il messaggio di salvataggio fallito indica che la memoria di salvataggio sta cedendo, perché quella schermata compare quando vengono rilevati blocchi difettosi sul chip flash. Il consiglio dei rispondenti è dumpare subito il salvataggio finché si carica ancora, con un lettore USB o con l'homebrew GBA Backup Tool su Nintendo DS con flashcart, e ricostruirlo poi da un salvataggio funzionante | SME |
| GBAtemp, scrittura su cartuccia senza batteria | https://gbatemp.net/threads/gba-unlicensed-batteryless-sram-cart-pokemon-emerald-save-writing-issues.681601/ | letto dagli screenshot dell'utente: su una cartuccia di riproduzione senza batteria il salvataggio vive in SRAM da 64 KiB a 0xFC0000, e scriverci un salvataggio da 128 KiB fallisce sempre. La diagnosi che l'autore raggiunge da solo in due giorni è che la firma attesa 0x08012025 non compare nel dump, che è esattamente il controllo che il nostro strumento fa in una riga; PKHeX rifiuta quel dump per dimensione non supportata. Il rimedio indicato è usare una ROM con patch da 64 KiB e un salvataggio da 64 KiB coerente | SME |
| GBAtemp, LDN3 su console modificata | https://gbatemp.net/threads/ryujinx-adds-ldn3-feature-allowing-emulator-users-to-play-online-with-cfw-switch-consoles.622169/ | letto dagli screenshot dell'utente e ha reso poco: è il thread di commento a una notizia del novembre 2022, e la discussione riguarda il confronto fra emulatore e console originale, non l'allestimento. Nessuna testimonianza tecnica sulle schede Wi-Fi, che invece è arrivata dal Discord Pokemon Multiplayer Research | LDN |
| GBAtemp, tutorial sui problemi di salvataggio | https://gbatemp.net/threads/tutorial-fix-all-save-problems-for-pokemon-games-vc-gba.433266/ | scoperto dentro il thread sul salvataggio fallito, dove viene indicato come la guida da seguire quando compare il messaggio di salvataggio corrotto. Non letto: GBAtemp risponde 403 al recupero automatico, e serve uno screenshot o un salvataggio della pagina | SME |
| insideGadgets | https://shop.insidegadgets.com/product/gbxcart-rw/ | il produttore del lettore usato dal track Smeraldo, con la documentazione del prodotto | SME, BRI, BAT |
| insideGadgets, canale di assistenza su Discord | https://discord.gg/YQ5Bkzy | esportato il 2026-08-31 e letto per filtri il 2026-09-01: cinquantaquattromilasettecentocinquantuno messaggi, dai quali sono state estratte le testimonianze su cui poggia il runbook della batteria. È la fonte di ciò che nessuna documentazione di prodotto scrive, perché nessun produttore documenta i modi in cui il proprio strumento distrugge un dato. Quattro risultati vanno nominati. Il trabocchetto di tensione: nella revisione in cui la tensione è controllata dal software l'interfaccia parte a tre virgola tre volt, e inserire una cartuccia di seconda generazione in quella condizione cancella il salvataggio anche senza premere il pulsante di connessione, con un rimedio che è una sequenza e non un'impostazione. La soglia di ritenzione della memoria, fra uno virgola otto e due volt, che trasforma la diagnosi da nozione in misura. La prova per sapere se la pila tenga ancora, cioè salvataggio nuovo, spegnimento, cinque minuti di attesa e riaccensione. E la sequenza in tre passi per rimettere in ordine l'orologio della seconda generazione dopo la sostituzione. Sul track Smeraldo risponde inoltre alla domanda aperta sui driver del convertitore seriale: su Windows sono inclusi soltanto in alcune versioni, e la firma del problema è il punto esclamativo giallo nella gestione dispositivi | BAT, SME, BRI |
| reddit r/Gameboy | https://www.reddit.com/r/Gameboy/ | hardware, riparazioni, lettori di cartucce; non leggibile automaticamente | SME, BRI |
| reddit r/3dshacks | https://www.reddit.com/r/3dshacks/ | modding del 3DS e problemi di installazione; non leggibile automaticamente | 3DS |
| reddit r/PokemonROMhacks | https://www.reddit.com/r/PokemonROMhacks/ | ROM hacking e strumenti su Gen 3; non leggibile automaticamente | BRI, SME |
| reddit r/PokemonHome, thread indicato dall'utente | https://www.reddit.com/r/PokemonHome/s/DrfatG6MJW | LETTO il 2026-09-07 con `tools/fetch-reddit.py`, dopo aver risolto il collegamento breve con un inseguimento dei reindirizzamenti che restituisce l'identificativo `1vynvjy`. Indicato il 2026-08-28 come contesto dell'obiettivo di collezione, e il contenuto lo conferma senza aggiungere tecnica: è l'annuncio di un utente che dichiara di avere portato tutte e milleventicinque le specie nel deposito, con ventotto commenti quasi tutti di congratulazioni. La sola cosa operativa che porta è il meccanismo con cui la comunità risolve una specie che non si può ottenere, cioè il prestito con restituzione fra due depositi, mostrato su Zarude: non riempie una casella in modo stabile e non sostituisce una via di produzione, ma è un canale che il progetto non aveva registrato. Il valore vero della corsa sta nei due post che questo rinvia, registrati nelle due righe seguenti | EVT |
| reddit r/PokemonHome, come si riconosce un esemplare costruito | https://www.reddit.com/r/PokemonHome/comments/12vvhbk/ | letto il 2026-09-07, raggiunto in due passi di rinvio dal thread precedente attraverso le regole del canale. È la fonte più utile della corsa e tocca direttamente il perimetro di questo progetto, perché descrive dal di fuori i criteri con cui la comunità giudica un esemplare. Quattro cose vanno registrate. La prima è che l'unica prova positiva di legittimità è il contrassegno del gioco in realtà aumentata o quello di provenienza recente dal deposito, mentre il marchio di origine non prova nulla: ne segue che nessun esemplare prodotto da noi potrà mai essere dimostrato legittimo, e che la domanda corretta non è se sembri legittimo ma se sia conforme. La seconda è un rilevatore che l'utente possiede già e non sapeva di avere: se il deposito rifiuta di far scambiare un esemplare, il deposito lo ha già classificato come costruito, quindi la scambiabilità è una misura gratuita e ripetibile. La terza è la caratterizzazione del rischio, che differisce da quella della politica ufficiale già registrata: secondo l'autore l'esito più probabile non è la sospensione ma la trasformazione in uovo guasto. La quarta è l'elenco dei segnali di allarme, che è una lista di spunta applicabile ai nostri lotti: sei valori individuali perfetti, identificativo nullo o nome di allenatore sospetto, fiocchi in eccesso o mancanti rispetto al gioco di origine, lucentezza dove era vietata, mosse o abilità impossibili, e luogo di primo incontro uguale al primo luogo indicizzato nei file del gioco | EVT, ACE, GEN |
| reddit r/PokemonHome, regole del canale | https://www.reddit.com/r/PokemonHome/comments/15o0lv6/ | letto il 2026-09-07 come nodo intermedio della corsa. Non porta contenuto tecnico ma è il raccoglitore che rinvia alla guida della riga precedente, ed è la prova sul campo della premessa dello strumento: il nodo di partenza non conteneva nulla di utile e il valore stava a due passi di distanza nel grafo dei rinvii | EVT |
| Arctic Shift, archivio pubblico di Reddit | https://arctic-shift.photon-reddit.com | la settima via della regola sulle fonti non recuperabili, adottata il 2026-09-07 e provata contro il servizio reale. Successore di Pushshift, conserva una copia dei contenuti pubblici di Reddit e ne espone di propria iniziativa un'interfaccia programmatica documentata, senza credenziali. Sblocca da sola tutte le voci Reddit di questo registro, che dal 2026-08-25 erano catalogate e non lette. Le due debolezze sono strutturali e dichiarate: ha latenza, quindi un post recente può mancare e la sua assenza non prova che non esista; e conserva ciò che su Reddit è stato cancellato, quindi l'identificativo dell'autore viaggia accanto al contenuto perché una richiesta di cancellazione mirata resti eseguibile. Lo strumento che la percorre è `tools/fetch-reddit.py` | tutti |
| tswann89, elenco dei produttori noti di esemplari costruiti | https://tswann89.github.io/PokemonSV/blacklist | catalogata e non letta, trovata il 2026-09-07 fra i rinvii della guida sul riconoscimento. È un elenco di nomi di allenatore associati alla produzione di esemplari, mantenuto dalla comunità. Serve a una domanda sola e va letta soltanto quando quella domanda si pone: se la coppia di identificativi scelta per l'allenatore del progetto collida con una di quelle. Il criterio che guidò la scelta il 2026-09-04 escludeva gli identificativi delle distribuzioni storiche e le forme riconoscibili come costruite, e non conosceva questo elenco | EVT |
| reddit r/pokemonrng | https://www.reddit.com/r/pokemonrng/ | generatore pseudocasuale, valore di personalità e legalità; non leggibile automaticamente | BRI |

### Archivi di salvataggi contribuiti, letti il 2026-09-02

Questi archivi entrano nel registro perché ADR-024 lo prescrive: ogni salvataggio impiegato va registrato con la propria provenienza e il proprio livello, e la parola scaricato copre cose che non si somigliano. Stanno al livello cinque e non oltre, perché in tutti e quattro i casi il contenuto è caricato da singoli utenti senza revisione: la piattaforma che li ospita può essere autorevole su altro e non lo è su questi file, e la descrizione che accompagna un caricamento è una dichiarazione del suo autore, non un dato verificato.

Ciò che rende questi archivi utilizzabili non è la loro autorevolezza ma la verificabilità del loro contenuto, che è una proprietà diversa: un salvataggio si apre, si verificano le sue somme di controllo, si censisce il suo deposito e si giudica ciascun esemplare, e alla fine di quel percorso si sa che cosa si ha in mano indipendentemente da chi lo ha caricato. Lo strumento che esegue i primi tre passi è `tools/verifica-salvataggi.py` e l'esito sulla raccolta corrente sta in `pokedex-home-completo/CENSIMENTO-SALVATAGGI.md`; il quarto resta di PKHeX.

| Luogo | URL | Ambito | Track |
|---|---|---|---|
| Project Pokemon, salvataggi contribuiti dagli utenti | https://projectpokemon.org/home/files/category/195-user-contributed-saves/ | la categoria da cui viene la maggior parte della raccolta del 2026-09-02, cioè undici caricamenti fra salvataggi di Game Boy Advance, Nintendo DS, Nintendo 3DS e Pokemon Box su GameCube. Il caricamento più rilevante per questo progetto è un Pokedex cromatico completo di prima, seconda e terza generazione, dichiarato dal suo autore come ottenuto in emulazione con manipolazione del generatore pseudocasuale nel 2024: verificato il 2026-09-02 che i trecentonovanta esemplari sono tutti cromatici, tutti leggibili in forma canonica e coprono trecentottantacinque specie distinte. Il secondo per rilevanza è un salvataggio di Pokemon Box dichiarato contenere tutto ciò che in terza generazione si può ancora ottenere legittimamente, esemplari ombra e distribuzioni comprese: la sua somma di controllo torna, il censimento del suo deposito non è ancora fatto | PKD, EVT |
| Forum Community, salvataggi della serie principale | https://pokemon.forumcommunity.net/?t=63088833 | otto salvataggi in lingua italiana, da Rosso Fuoco a UltraSole, dichiarati con storia completata, Pokedex completo e valori massimizzati. Verificato il 2026-09-02 che tutti e otto sono integri e del gioco dichiarato; la dichiarazione sui valori massimizzati è coerente con esemplari costruiti e non ottenuti giocando, quindi questi salvataggi valgono come banco di prova dei formati e non come sorgente di esemplari | PKD |
| PokeWorld WiFi, salvataggi di quarta e quinta generazione | https://pokeworldwifi.forumfree.it/?t=64753881 | tre salvataggi italiani, due di Sinnoh e uno di Unima, con la descrizione di ciò che resta da catturare in ciascuno. Il salvataggio di Diamante dichiara Manaphy e il Jirachi del canale televisivo nella seconda scatola, che è interessante perché quel Jirachi è la sola voce del catalogo degli eventi che il nostro generatore dichiara fuori portata. Verificato il 2026-09-02 che i tre file sono integri e riconosciuti come Diamante o Perla i primi due e come i seguiti di Unima il terzo | PKD, EVT |
| Pokemon Chat, salvataggio di Rosso Fuoco | https://pokemonchat.forumcommunity.net/?t=56987893 | un solo salvataggio, dichiarato iniziato nel 2010 e completato senza trucchi tranne alcune eccezioni che il suo autore elenca, fra cui un esemplare con statistiche impossibili. Verificato il 2026-09-02: integro, Rosso Fuoco, allenatore con centosettantotto ore di gioco, duecentottantatre esemplari nel deposito di cui centonove cromatici e tredici uova. È il salvataggio della raccolta che più somiglia a una partita vera, e l'autore dichiara i propri interventi invece di tacerli, che è la ragione per cui è citabile | PKD |
| r/PokemonHome, il foglio del living dex | https://www.reddit.com/r/PokemonHome/s/1BqkNHm7xT | la discussione che indica il foglio di calcolo comunitario del living dex, ed è il livello di dettaglio che questo progetto vuole raggiungere fino alla specie 1025 | PKD |
| Foglio del living dex, in sola lettura | https://docs.google.com/spreadsheets/u/0/d/1fW_BE208ziLMgFlvS-k2XyLulo_GztxcznAfgElGSQ4/htmlview?pli=1 | il foglio comunitario che elenca le voci da possedere; scaricato in locale come `_notes/spreadsheets e passaggi home/LivingDex Spreadsheet.xlsx` | PKD |
| r/PokemonHome, discussione sul foglio | https://www.reddit.com/r/PokemonHome/s/A5mNdvHcE4 | la discussione da cui il foglio è stato raggiunto, consegnata come schermate dalla 43 alla 47 | PKD |
| r/PokemonHome, i Pokemon di N | https://www.reddit.com/r/PokemonHome/s/YDb38ZFGLJ | l'elenco dei Pokemon del personaggio N di quinta generazione, che sono una categoria a sé con identificativi propri; consegnata come schermate dalla 71 alla 75 | PKD, EVT |
| r/PokemonHome, monarium | https://www.reddit.com/r/PokemonHome/s/7y8hlCDBxZ | la discussione in cui l'autore presenta lo strumento di gestione del living dex; consegnata come schermate dalla 56 alla 69 | PKD |
| r/PokemonHome, informazioni tecniche | https://www.reddit.com/r/PokemonHome/s/00gpFvJHo4 | discussione tecnica sul deposito, consegnata come schermate dalla 76 alla 101, ancora da spogliare | PKD |
| r/PokemonHome, la chiusura della banca | https://www.reddit.com/r/PokemonHome/s/5KIb8SiyWK | discussione sulla chiusura del servizio con altri collegamenti nei commenti, consegnata come schermate dalla 102 alla 111; da spogliare, e i collegamenti nei commenti sono debito di lettura dichiarato | PKD, 3DS |
| Lista di controllo per la chiusura della banca, versione 0.5 | https://docs.google.com/spreadsheets/d/14QTf2q3rRFlaIqHxigfFyKiKZdL9o6uc_bQE-OtOTwk/edit?gid=1932480820 | foglio comunitario che elenca tutto ciò che va fatto prima della chiusura del servizio; scaricato in locale come `_notes/spreadsheets e passaggi home/Bank Closing all possible things checklist V0.5.xlsx` | PKD, 3DS |
| Foglio del living dex, scheda di lavoro | https://docs.google.com/spreadsheets/d/1fW_BE208ziLMgFlvS-k2XyLulo_GztxcznAfgElGSQ4/edit?gid=673849431 | la stessa cartella già registrata in sola lettura, aperta però su una scheda precisa; l'identificativo della scheda fa parte dell'indirizzo e va conservato, perché una cartella di calcolo con più schede non è un documento solo | PKD |
| r/PokemonHome, dai giochi derivati a quelli principali | https://www.reddit.com/r/PokemonHome/s/2mcgR0kgev | consegnata come schermate dalla 122 alla 132 il 2026-09-07, e tocca precisamente la categoria su cui il censimento del medesimo giorno ci ha trovati ciechi, cioè le consegne che non lasciano una carta. Nomina come canali verso i giochi principali il Mondo dei Sogni, chiuso nel 2014, la serie Ranger con l'uovo di Manaphy, Colosseum e XD con il fiocco che si ottiene soltanto purificando un esemplare ombra, il cercatore in realtà aumentata, Battle Revolution con tre esemplari in omaggio, e i due programmi di deposito su console domestica. È materiale di community e vale come indicazione di dove guardare, non come fonte verificata: ciascun canale va poi confermato sul censimento o sulla base dei doni | EVT, PKD |
| r/PokemonHome, elenco degli eventi ancora disponibili | https://www.reddit.com/r/PokemonHome/comments/1i3ikns/list_of_still_available_event_and_unique_pok%C3%A9mon/ | consegnata come schermate dalla 136 alla 147 il 2026-09-07 e non ancora presente nel registro. È un elenco compilato dalla community degli eventi e degli esemplari unici tuttora ottenibili, quindi una fonte sulla ottenibilità e non sulla esistenza: serve al controllo incrociato opposto a quello di Serebii, che dice che cosa è esistito, perché questa dice che cosa è ancora raggiungibile. Da spogliare e confrontare con la partizione fra ciò che scade e ciò che non scade | EVT, PKD |
| Foglio del catalogo per coppia di sessi | https://www.reddit.com/r/PokemonHome/comments/1djbdm0/ | definisce operativamente il profilo detto dell'arca, cioè un esemplare per ciascuno dei due sessi di ogni specie e di ogni forma, e conferma per via indipendente le 63 configurazioni della specie il cui dolcetto non è un campo della forma | PKD |
| Foglio della collezione con sei tracciatori | https://www.reddit.com/r/PokemonHome/comments/xp1ise/ | tiene insieme catalogo vivente, esemplari di taglia massima, marchi di origine, marchi ordinari, fiocchi e sfere: è la prima fonte che enumeri gli assi nella stessa forma in cui il progetto li ha ricostruiti, e li enumera quattro anni prima | PKD |
| Doni di quarta e quinta generazione dal servizio ricostruito | https://www.reddit.com/r/wiimmfi/comments/fugd8l/ | l'elenco per titolo dei doni che l'autore dichiara di avere ricevuto cambiando i server dei nomi sulla console, con 1384 commenti che lo aggiornano e due testimonianze del 2026-09-07 che dichiarano il canale ancora attivo; comprende due doni mai distribuiti ufficialmente. Risponde in parte al primo dei quattro passi del capitolo sulla produzione dentro il gioco | PKD, EVT |

## Il corpus della collezione: centosettantuno fonti da un solo post di raccolta

Questa sezione ha una forma diversa dalle precedenti e la ragione va detta prima delle righe. Le altre sezioni sono ordinate per affidabilità, perché quello è il criterio con cui si decide chi ha ragione quando due fonti si contraddicono. Questa è ordinata per argomento, perché nasce da un corpus unico e la sua tassonomia esisteva già: le voci vengono tutte dal medesimo post di raccolta, e i cluster sono le intestazioni che il suo autore ha scelto. Conservarli invece di rifonderli nei cinque livelli ha due vantaggi che non sono di comodo. Il primo è che restano confrontabili con la fonte, quindi chi verifica risale a colpo d'occhio. Il secondo è che una tassonomia scritta da chi conosce il dominio è quasi sempre migliore di una inventata da chi lo sta imparando. Il livello di affidabilità non si perde, e sta nella seconda colonna di ogni riga.

La provenienza. È il post `https://www.reddit.com/r/PokemonHome/comments/1vtj5hf/`, seconda versione di una guida alle collezioni nel deposito scritta da El_Boosty il 2026-08-20, che l'utente ha consegnato il 2026-09-08 come radice da spogliare. Il post dichiara esso stesso di essere una raccolta di collegamenti e non un testo, il che lo rende il caso ideale per il lettore ricorsivo: leggere il solo nodo di partenza significherebbe leggere l'indice credendo di aver letto il libro. La corsa ha attraversato in ampiezza il grafo dei rinvii fino alla profondità uno, producendo ottocentodiciassette nodi e novecentosessantadue archi, di cui sessantacinque post scaricati e trentasei pagine esterne ridotte a testo; trecentoquarantasette elementi restano non raggiunti perché oltre il tetto di profondità, dichiarati come tali e ripresi da un rilancio senza rifare il resto.

Il censimento completo, con la corsa da cui viene e l'esito di ciascun collegamento, sta in `pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md` e nella sua tabella `fonti-collezione.csv`, ed è generato da `tools/censimento-fonti-reddit.py`. Quel documento e questa sezione non sono ridondanti e vale dire in che cosa differiscono: là ogni riga porta l'esito tecnico della corsa, cioè se la fonte sia stata scaricata, catalogata con un motivo o non raggiunta; qui ogni riga porta il livello di affidabilità, che è un giudizio nostro e non un dato della corsa. Il primo si rigenera, il secondo si cura.

Il livello è assegnato per host da una tabella dichiarata dentro lo strumento invece che a mano riga per riga, e la scelta è deliberata: una classificazione fatta a mano su centosettantuno voci è incoerente per costruzione, perché la stessa fonte riceve livelli diversi a venti righe di distanza. Scritta in un posto solo la si può contestare, e una riga sbagliata si corregge una volta e il censimento si rigenera. Resta un limite dichiarato: il livello è una proprietà della fonte e non del suo contenuto, quindi un host che ospiti cose di natura diversa riceve il livello più prudente fra quelli plausibili e la sua voce va guardata a mano prima di essere citata.

Che cosa questo corpus aggiunge al progetto, detto senza gonfiarlo. La maggior parte delle voci riguarda il come ottenere giocando ciò che noi stiamo producendo, quindi non serve ai generatori ma serve alla domanda che li governa, cioè quali esemplari esistano e quali caselle vadano riempite. Tre cluster toccano invece direttamente il lavoro in corso: quello sulla chiusura della banca, che è il vincolo temporale dell'intero progetto; quello sulle liste trasversali, che porta enumerazioni da confrontare con le nostre; e quello sull'esecuzione di codice e la manipolazione del generatore, che è la stessa materia del track sulla generazione. Le voci di quei tre vanno lette per prime, e le altre restano catalogate finché una domanda non le chiama.

Due voci vanno segnalate a parte perché l'utente le aveva già procurate a mano prima che la corsa esistesse, e ritrovarle qui è una conferma della loro rilevanza e non una duplicazione. Il foglio di calcolo della sfida al catalogo padrone è salvato in locale come `_notes/spreadsheets e passaggi home/Pokémon Master Dex and Retro Dex Challenges.xlsx`. Il post sulla tabella della connettività compare nel corpus nella forma del collegamento di condivisione, e il suo identificativo canonico è `1siu40m`.

### Le fonti con un livello

| Cluster | Liv | Che cosa documenta | URL |
|---|---|---|---|
| Preambolo | 5 | post. Titolo della fonte: Guide on Pokemon Home Collections, di El_Boosty | https://www.reddit.com/r/PokemonHome/comments/1laqzce/guide_on_pokemon_home_collections/ |
| 1) Dex completions | 4 | LETTA il 2026-09-08 su consegna dell'utente come schermate, dopo che la corsa l'aveva mancata con un rifiuto della sfida anti-bot. È la definizione canonica dei quattro tipi di catalogo vivente, che il post di raccolta cita tre volte con tre ancore diverse e che è un solo documento. Il catalogo di forma vivente comprende forme regionali, pre-evoluzioni, differenze di forma e differenze di sesso; la sua versione ridotta toglie il sesso; il catalogo vivente semplice tiene le sole forme regionali e le pre-evoluzioni; il catalogo delle forme finali tiene le forme regionali e ogni specie alla sua ultima evoluzione. Il sesso è dunque l'asse che distingue il primo dal secondo, ed è la risposta alla domanda per cui la fonte era stata cercata. La pagina porta inoltre due dati che il progetto non aveva: il deposito è alla versione quattro e supporta i due titoli usciti dopo la nona generazione, e la decorazione di Alcremie vi è contata quarantasette e non nove né sessantatré | PKD |
| 1) Dex completions | 5 | Noah's Ark Dex - male/female of every pokemon. Titolo della fonte: I made a Noah's Ark Google Sheet Checklist so you don't have to!, di verified-skelly | https://www.reddit.com/r/PokemonHome/comments/1djbdm0/i_made_a_noahs_ark_google_sheet_checklist_so_you/ |
| 1) Dex completions | 5 | Origin Dex challenge - every pokemon from its original generation. Titolo della fonte: The Origin Living Dex challenge, di Faraknights | https://www.reddit.com/r/PokemonHome/comments/1h5p13d/the_origin_living_dex_challenge/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button |
| 1) Dex completions / Reddit | 5 | My living Origin Dex: Every Pokemon from its original game, plus oddities and events. Cloned Giveaway at the end!, di IzzybearThebestdog | https://www.reddit.com/r/PokemonHome/comments/1jmep9q/my_living_origin_dex_every_pokemon_from_its/ |
| 1) Dex completions / Pokemon Collection Trackers | 5 | Pokemon Home living dex list. Titolo della fonte: Pokemon Home COMPLETE Living Dex List, di rquinain | https://www.reddit.com/r/PokemonHome/comments/f3uaxj/pokemon_home_complete_living_dex_list/ |
| 1) Dex completions / Pokemon Collection Trackers | 3 | Suppereffective now different URL. Titolo della fonte: SuperEffective - Pokédex Tracker, News & more | https://classic.pokepc.net/ |
| 1) Dex completions / Pokemon Collection Trackers | 3 | Pokedextracker | https://pokedextracker.com/ |
| 1) Dex completions / Pokemon Collection Trackers | 4 | Austin John's tracker. Titolo della fonte: Pokemon Home Organizer — Austin John Plays | https://www.austinjohnplays.com/pokemonhome |
| 1) Dex completions / Pokemon Collection Trackers | 5 | Reddit user xtokri's customizable tracker. Titolo della fonte: Got frustrated with existing living-dex trackers, so I built one, di xtokri | https://www.reddit.com/r/PokemonHome/comments/1st10p1/got_frustrated_with_existing_livingdex_trackers/ |
| 1) Dex completions / Pokemon Collection Trackers | 5 | Reddit user Thundrosaur's Pokemon collection spreadsheet. Titolo della fonte: Pokémon Collection Spreadsheet, di Thundrosaur | https://www.reddit.com/r/PokemonHome/comments/xp1ise/pok%C3%A9mon_collection_spreadsheet/ |
| 1) Dex completions / Pokemon Collection Trackers | 3 | Up to date GO Dex tracker | https://godex.site/collection/90977 |
| 1) Dex completions / Gen 1 | 5 | Original Region Guides: Gen 1, di electroswingmix | https://www.reddit.com/r/PokemonHome/comments/1p0hzxn/original_region_guides_gen_1/ |
| 1) Dex completions / Gen 1 | 5 | Flying trainer glitch for all Gen 1 Pokemon with your OT. Titolo della fonte: [Guide] Getting ANY Pokémon you want in generations 1 through 3: Generation 1 (Part 1 of 3), di UW_Unknown_Warrior | https://www.reddit.com/r/pokemon/comments/49r66o/guide_getting_any_pok%C3%A9mon_you_want_in_generations/ |
| 1) Dex completions / Gen 1 | 5 | Map of possible encounters with flying trainer glitch. Titolo della fonte: This is a map of all the different pokemon you can encounter using the Mew glitch in R/B/Y., di LanAkou | https://www.reddit.com/r/pokemon/comments/48bflq/this_is_a_map_of_all_the_different_pokemon_you/ |
| 1) Dex completions / Gen 2 | 5 | Original Region Guides: Gen 2, di electroswingmix | https://www.reddit.com/r/PokemonHome/comments/1p362dn/original_region_guides_gen_2/ |
| 1) Dex completions / Gen 2 | 5 | Swarm manipulation GSC. Titolo della fonte: How to find Swarms, di Chamale | https://www.reddit.com/r/Pokemonguide/comments/7b07f6/how_to_find_swarms/ |
| 1) Dex completions / Gen 2 | 5 | Roamers GSC. Titolo della fonte: How to find Raikou, Suicune, and Entei: A mathematically optimal guide, updated and corrected, di Chamale | https://www.reddit.com/r/Pokemonguide/comments/7c2kcf/how_to_find_raikou_suicune_and_entei_a/ |
| 1) Dex completions / Gen 2 | 5 | Headbutt calculator GSC. Titolo della fonte: A tool for finding the right Headbutt Tree when looking for rare encounters, di TShadowKnight | https://www.reddit.com/r/pokemon/comments/72tbz7/a_tool_for_finding_the_right_headbutt_tree_when/ |
| 1) Dex completions / Gen 2 | 5 | Unown's last appearance and how to find all 28 forms, di TechnoTrainer | https://www.reddit.com/r/pokemon/comments/odmwcb/unowns_last_appearance_and_how_to_find_all_28/ |
| 1) Dex completions / Gen 3 | 5 | Original Region Guides: Gen 3, di electroswingmix | https://www.reddit.com/r/PokemonHome/comments/1vphi1w/original_region_guides_gen_3/ |
| 1) Dex completions / Gen 3 | 5 | National Dex Guide for RSE. Titolo della fonte: How to complete your Pokédex in generation 3 (Ruby/Sapphire/Fire Red/Leaf Green/Emerald), di Poison-Powder | https://www.reddit.com/r/Pokemonguide/comments/l0bwym/how_to_complete_your_pok%C3%A9dex_in_generation_3/ |
| 1) Dex completions / Gen 3 | 5 | Generation 3 Feebas Guide (also applies to Gen 4), di flipflipshift | https://www.reddit.com/r/pokemon/comments/lettfp/generation_3_feebas_guide_also_applies_to_gen_4/?utm_source=share&utm_medium=ios_app&utm_name=iossmf |
| 1) Dex completions / Gen 3 | 2 | Berry glitch Zigzagoon | https://bulbapedia.bulbagarden.net/wiki/Berry_glitch |
| 1) Dex completions / Gen 3 | 5 | Gen 3 Check: Pokémon you need to have in Pokémon HOME, di Dararakz | https://www.reddit.com/r/PokemonHome/comments/1p06clm/gen_3_check_pok%C3%A9mon_you_need_to_have_in_pok%C3%A9mon/ |
| 1) Dex completions / Gen 3 | 3 | Arbitrary Code Execution RSE for past events. Titolo della fonte: Pokemon Emerald ACE · GitHub | https://gist.github.com/claydolwithexplosion/017f1784deebcd118b61d3ad917edb3c |
| 1) Dex completions / Gen 4 | 5 | National Dex Guide for Platinum. Titolo della fonte: I've written the most comprehensive guide ever to completing the National Dex in Platinum, di big_bill_wilson | https://www.reddit.com/r/pokemon/comments/oyjuy7/ive_written_the_most_comprehensive_guide_ever_to/ |
| 1) Dex completions / Gen 4 | 2 | HGSS bug catching contest | https://bulbapedia.bulbagarden.net/wiki/Bug-Catching_Contest |
| 1) Dex completions / Gen 4 | 5 | Gen 4 Check: Pokémon you need to have in Pokémon HOME, di Dararakz | https://www.reddit.com/r/PokemonHome/comments/1pd8ve9/gen_4_check_pok%C3%A9mon_you_need_to_have_in_pok%C3%A9mon/ |
| 1) Dex completions / Gen 4 | 5 | Level 1 (shiny) Sinjoh ruins legendaries. Titolo della fonte: How did I get a low level Giritina? Here is a step by step guide so you too can get all the gen 4 and gen 5 event Pokemon! , di BoxLongjumping1067 | https://www.reddit.com/r/PokemonHGSS/comments/1hy3b12/how_did_i_get_a_low_level_giritina_here_is_a_step/ |
| 1) Dex completions / Gen 4 | 5 | HGSS Slugma, Mareep & Wooper special eggs. Titolo della fonte: TIL you can get a Slugma, Wooper and Mareep egg in Violet City right at the start of HGSS, di Merman101 | https://www.reddit.com/r/pokemon/comments/lwdw9o/til_you_can_get_a_slugma_wooper_and_mareep_egg_in/ |
| 1) Dex completions / Gen 5 | 2 | Dream radar Pokemon | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Dream_Radar |
| 1) Dex completions / Gen 5 | 2 | Hidden Grotto | https://bulbapedia.bulbagarden.net/wiki/Hidden_Grotto |
| 1) Dex completions / Gen 5 | 2 | B2W2 Pass Power | https://bulbapedia.bulbagarden.net/wiki/Entralink#Pass_Powers |
| 1) Dex completions / Gen 5 | 2 | N's Pokemon | https://bulbapedia.bulbagarden.net/wiki/N%27s_Pok%C3%A9mon |
| 1) Dex completions / Gen 6 | 5 | Vivillon Pattern 3DS Guide. Titolo della fonte: Reminder: You can set the Vivillon pattern of your game by changing your region before start!, di Starfighter-Suicune | https://www.reddit.com/r/pokemon/comments/7blfqr/reminder_you_can_set_the_vivillon_pattern_of_your/ |
| 1) Dex completions / Gen 7 | 2 | Totem Pokemon | https://bulbapedia.bulbagarden.net/wiki/Totem_Pok%C3%A9mon |
| 1) Dex completions / Gen 7 | 2 | Island scan | https://bulbapedia.bulbagarden.net/wiki/QR_Scanner#Island_Scan |
| 1) Dex completions / Gen 7 | 2 | Surf Pikachu - can be shiny hunted | https://bulbapedia.bulbagarden.net/wiki/Surfing_Pikachu#Pok%C3%A9mon_Ultra_Sun_and_Ultra_Moon |
| 1) Dex completions / Gen 8 | 2 | GMax Pokemon. Titolo della fonte: Pokémon Sword & Shield - Gigantamax Forms | https://www.serebii.net/swordshield/gigantamax.shtml |
| 1) Dex completions / Gen 8 | 5 | Alcremie Guide. Titolo della fonte: Guide for Alcremie in Scarlet/Violet., di Far-Board8733 | https://www.reddit.com/r/PokemonScarletViolet/comments/18p237c/guide_for_alcremie_in_scarletviolet/ |
| 1) Dex completions / Gen 9 | 2 | Titan mark Pokemon. Titolo della fonte: Pokémon Scarlet & Violet - Titan Pokémon | https://www.serebii.net/scarletviolet/titanpokemon.shtml |
| 1) Dex completions / Gen 9 | 2 | Mighty mark Pokemon. Titolo della fonte: Pokémon Scarlet & Violet - Tera Raid Battle Events | https://serebii.net/scarletviolet/teraraidbattleevents.shtml |
| 1) Dex completions / Gen 9 | 3 | SV sandwich simulator | https://cecilbowen.github.io/pokemon-sandwich-simulator/ |
| 1) Dex completions / Spinoffs | 2 | List of purfified shadow Pokemon from XD/Colosseum | https://bulbapedia.bulbagarden.net/wiki/List_of_Shadow_Pok%C3%A9mon |
| 1) Dex completions / Spinoffs | 5 | AlphaDex Pokemon. Titolo della fonte: AlphaDex, part 3, di Roval3 | https://www.reddit.com/r/PokemonHome/comments/1py3n1f/alphadex_part_3/ |
| 1) Dex completions / Spinoffs | 2 | Overview of possible titles for Pokemon Champions. Titolo della fonte: Pokémon Champions - Pokémon Titles | https://www.serebii.net/pokemonchampions/pokemontitles.shtml |
| 1) Dex completions / Overall lists for multiple generations | 5 | LETTA il 2026-09-08, e la cartella di calcolo che il post rende pubblica è stata scaricata con una richiesta locale in `_notes/fonti/2026-09-08-foglio-scambi-e-doni-greenpangolin17.xlsx`. Autorevole su che cosa esista come scambio in gioco, dono, uovo ed esemplare interagibile, con allenatore e soprannome di ciascuno: ottocentouno voci su quattro schede, di cui settantaquattro sui giochi derivati e cinquantasei sui giochi di deposito, che sono la parte a via chiusa e la materia del controllo all'indietro di ADR-049. La sintesi è in `pokedex-home-completo/STUDIO-06-le-enumerazioni-trasversali.md`. Titolo della fonte: I made a spreadsheet/checklist of all the in-game trades/gift pokemon/interactable pokemon in all the games, di greenpangolin17 | https://www.reddit.com/r/PokemonHome/comments/17rt8yo/i_made_a_spreadsheetchecklist_of_all_the_ingame/ |
| 1) Dex completions / Overall lists for multiple generations | 5 | LETTA il 2026-09-08, con la cartella di calcolo scaricata in `_notes/fonti/2026-09-08-foglio-ingame-events-chaboijish.xlsx`. Autorevole sull'enumerazione degli esemplari da evento interno al gioco, cioè millequattrocentocinquantotto voci più duecentotrentotto scambi, di cui novecentottantasei da titoli la cui via verso il deposito passa dalla banca. Sono in grandissima parte incontri ordinari, che per ADR-049 non si producono: entrano nella lista di spunta e non nella coda. Titolo della fonte: New checklist for Collectors! Every In-Game Event Pokemon!, di ChaBoiJish | https://www.reddit.com/r/pokemontrades/comments/18y648l/new_checklist_for_collectors_every_ingame_event/ |
| 1) Dex completions / Overall lists for multiple generations | 5 | LETTA il 2026-09-08. Non porta una enumerazione ma una conferma indipendente di quali classi la comunità riconosca come rare, e sono le due che il progetto ha in coda: i leggendari al livello cinque del sondatore dei sogni e i tre del tempo e dello spazio al livello uno dalle rovine di Sinjoh. Titolo della fonte: Rarest pokemon to have, di Dependent_Relief_652 | https://www.reddit.com/r/PokemonHome/comments/1flidyg/rarest_pokemon_to_have/ |
| 1) Dex completions / Overall lists for multiple generations | 2 | LETTA il 2026-09-08 con una richiesta locale, e salvata in `_notes/fonti/2026-09-08-bulbapedia-differenze-di-sesso.html`. È la fonte che enumera una per una le centodue specie con differenze di sesso visibili, più la forma di Hisui di Sneasel che sta fuori tabella: chiude la voce aperta il 2026-09-07 su quale fonte usare, e concorda con il foglio comunitario senza alcuna divergenza nei due versi. Lo strumento è `tools/enumera-differenze-sesso.py` e il documento `pokedex-home-completo/DIFFERENZE-DI-SESSO.md` | https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_with_gender_differences |
| 1) Dex completions / Overall lists for multiple generations | 5 | LETTA il 2026-09-08 nel corpo e non nella guida collegata. È la fonte da cui discende la scheda dei sottolivellati della lista di controllo che l'utente ha su disco, che la accredita per nome, ed è autorevole su quali esemplari sottolivellati esistano e con quale probabilità: un livello inferiore a quello di evoluzione non si ricrea in un altro titolo, quindi quell'asse si perde con la via che lo produceva. Titolo della fonte: A guide to underleveled Pokemon, di Pikmin34 | https://www.reddit.com/r/pokemon/comments/hhlm8k/a_guide_to_underleveled_pokemon/ |
| 1) Dex completions / Overall lists for multiple generations | 5 | Overview DNS glitch Gen 4&5. Titolo della fonte: [DNS] Gen IV & V events (list inside), di JoseGamer33 | https://www.reddit.com/r/wiimmfi/comments/fugd8l/dns_gen_iv_v_events_list_inside/?show=original |
| 1) Dex completions / Overall lists for multiple generations | 4 | List of obtainable DNS pokemon. Titolo della fonte: How to unlock Gen 4 and 5 Pokemon Mystery Events in 2018 / Shacknews | https://www.shacknews.com/article/108512/how-to-unlock-gen-4-and-5-pokemon-mystery-events-in-2018 |
| 1) Dex completions / Overall lists for multiple generations | 3 | DNS online trading Gen 4&5. Titolo della fonte: Poké Classic Network | https://pkmnclassic.net/ |
| 1) Dex completions / Overall lists for multiple generations | 5 | LETTA il 2026-09-08. Autorevole, con la cautela del livello, sulla meccanica dei timbri di provenienza: quelli dei titoli per console corrente restano, mentre il timbro della banca e quello del deposito vengono rimossi in modo permanente quando l'esemplare esce dal deposito e quello del gioco per telefono resta. Se confermato distingue la provenienza conservata internamente dal segno visibile su di essa, che sono due affermazioni diverse, e il progetto ne usava una sola. DA VERIFICARE su fonte migliore di una discussione. Titolo della fonte: Special Text About Many Pretty Symbols (STAMPS 6.0), di TwistedTextures | https://www.reddit.com/r/PokemonHome/comments/145ylee/special_text_about_many_pretty_symbols_stamps_60/ |
| 1) Dex completions / Overall lists for multiple generations | 2 | LETTA il 2026-09-08 nella sola parte sugli esemplari cromatici garantiti in gioco, che sono sette voci con il loro luogo, di cui tre nei titoli sotto scadenza. Va dichiarato un difetto nostro e non della fonte: l'estrattore che ha ridotto la pagina a testo ha perso i nomi delle specie conservando i luoghi, e il grezzo accanto al derivato permette una seconda passata senza ri-scaricare. Titolo della fonte: Serebii.net Games - Shiny Pokémon | https://www.serebii.net/games/shiny.shtml |
| 1) Dex completions / Overall lists for multiple generations | 5 | Scaricata il 2026-09-08 in `_notes/fonti/2026-09-08-foglio-scambi-e-doni-greenpangolin17.xlsx`. È l'indirizzo di pubblicazione della cartella di calcolo del post di greenpangolin17, distinto dal post che la annuncia, ed è quello da cui si riscarica una versione aggiornata | https://docs.google.com/spreadsheets/d/e/2PACX-1vTusrkjjQVxfqANVboZbw-VplOUBioFRDcHi5yEz4tXupmNvs9s2MHDBPA0jBzS38Ic9UT6Xulr0Sko/pubhtml |
| 1) Dex completions / Overall lists for multiple generations | 5 | Scaricata il 2026-09-08 in `_notes/fonti/2026-09-08-foglio-ingame-events-chaboijish.xlsx`. È la cartella di calcolo del post di ChaBoiJish, con la scheda degli eventi interni, quella degli scambi e una tabella di supporto sulle specie | https://docs.google.com/spreadsheets/d/1Np71tQe_CLWfVEHNY6158twKeGSq3lUdAJTxlRjuRAw/edit |
| 2) What are we loosing with Pokemon Bank | 5 | Scaricata il 2026-09-08. È la lista di controllo che SteelOfSpeed ha derivato dal post sulle sfide che la chiusura rende impossibili, e ne porta le trentasette esplicite in forma tabellare con la nota che le due di Rosso Fuoco e Verde Foglia torneranno possibili a ottobre. La fonte primaria su questo asse resta però l'applicazione, che porta anche le sfide che nessuna delle due elenca | https://docs.google.com/spreadsheets/d/11lZYY9qUE3I1d7_Kc3M3q03KIuYGFBaWvWqN2X_qSOk/edit |
| 2) What are we loosing with Pokemon Bank | 5 | The one and only Gigachad - Pokémon Bank Exclusives Masterpost. Titolo della fonte: Pokémon Bank Exclusives Masterpost, di electroswingmix | https://www.reddit.com/r/PokemonHome/comments/1apiuee/pok%C3%A9mon_bank_exclusives_masterpost/ |
| 2) What are we loosing with Pokemon Bank | 5 | Pokemon to transfer before Bank shuts down, di YuiAmon | https://www.reddit.com/r/PokemonHome/comments/175qgyy/pokemon_to_transfer_before_bank_shuts_down/ |
| 2) What are we loosing with Pokemon Bank | 5 | Summary of what will be lost across generations due to Bank closure, di dungeonrpg | https://www.reddit.com/r/PokemonHome/comments/1vog8zg/summary_of_what_will_be_lost_across_generations/ |
| 2) What are we loosing with Pokemon Bank | 5 | All Pokemon Home challenges that will become impossible after bank closes, di WillowOfWisps | https://www.reddit.com/r/PokemonHome/comments/1voa411/all_pokemon_home_challenges_that_will_become/ |
| 2) What are we loosing with Pokemon Bank | 5 | Unique or event pokemon to send. Titolo della fonte: PSA Lots and Lots of Unique or Event Mons to send up from Bank, di Fatalframe4 | https://www.reddit.com/r/PokemonHome/comments/1vrbbom/psa_lots_and_lots_of_unique_or_event_mons_to_send/ |
| 2) What are we loosing with Pokemon Bank | 5 | Every (shiny) pokemon that must be transferred Pre-Gen 8. Titolo della fonte: Every pokemon that must be transferred / obtained pre-gen 8, di EpiclyEpicGamerE | https://www.reddit.com/r/PokemonHome/comments/1vnlh42/every_pokemon_that_must_be_transferred_obtained/ |
| 3) Collections of one Pokemon species | 2 | Pikachu event dex. Titolo della fonte: Serebii.net Eventdex - #0025 Pikachu | https://www.serebii.net/events/dex/025.shtml |
| 3) Collections of one Pokemon species | 2 | Mark overview. Titolo della fonte: Pokémon Scarlet & Violet - Marks | https://www.serebii.net/scarletviolet/marks.shtml |
| 3) Collections of one Pokemon species | 3 | Curry mark | https://projectpokemon.org/home/forums/topic/57870-swsh-camp-encounters-after-making-curry/ |
| 3) Collections of one Pokemon species | 2 | Weather marks SWSH. Titolo della fonte: Pokémon Sword & Shield - Weather | https://www.serebii.net/swordshield/weather.shtml |
| 3) Collections of one Pokemon species | 2 | guide to all possible Pokemon, lvl, ball combination. Titolo della fonte: Serebii.net Games - PokéBall Details - Generation I | https://www.serebii.net/games/geniball.shtml |
| 4) Ribbon Master | 5 | Athis ribbon master guide. Titolo della fonte: My guide on the Ribbon Master Challenge, di Athis_891 | https://www.reddit.com/r/pokemonribbons/comments/pzzqt4/my_guide_on_the_ribbon_master_challenge/ |
| 4) Ribbon Master | 5 | In celebration of LGPE, here's a Pikachu Ribbon Master, di SatoSmogonFrog | https://www.reddit.com/r/pokemonribbons/comments/9xj21t/in_celebration_of_lgpe_heres_a_pikachu_ribbon/ |
| 4) Ribbon Master | 3 | u/10Sly10 ribbon guide website. Titolo della fonte: Ribbons.Guide - Ribbon Tracking and Guidance | https://ribbons.guide/ |
| 5) Other lists and spreadsheets | 5 | Spreadsheet of matching Pokemon-Ball colours. Titolo della fonte: Legal Matching Pokéballs 2.0 spreadsheet, di OracleLink | https://www.reddit.com/r/pokemon/comments/zi89xa/legal_matching_pok%C3%A9balls_20_spreadsheet/ |
| 5) Other lists and spreadsheets | 2 | List of all unique NPC and gift TIDs | https://bulbapedia.bulbagarden.net/wiki/List_of_notable_ID_numbers |
| 5) Other lists and spreadsheets | 2 | List of crossgen evolutions | https://bulbapedia.bulbagarden.net/wiki/List_of_cross-generational_evolutionary_lines |
| 5) Other lists and spreadsheets | 2 | List of Events | https://m.bulbapedia.bulbagarden.net/wiki/List_of_event_Pok%C3%A9mon_distributions |
| 5) Other lists and spreadsheets | 3 | Event gallery | https://projectpokemon.org/home/files/category/2-event-gallery/ |
| 6) How to still get Bank and other games/ 3DS modding | 5 | Creating the ultimate Pokemon machine. Titolo della fonte: Creating the Ultimate Pokémon Machine - Nintendo 3DS (v4), di SteveW_MC | https://www.reddit.com/r/pokemon/comments/1spdhic/creating_the_ultimate_pok%C3%A9mon_machine_nintendo/ |
| 6) How to still get Bank and other games/ 3DS modding | 3 | Modding your 3DS. Titolo della fonte: 3DS Hacks Guide | https://3ds.hacks.guide/ |
| 6) How to still get Bank and other games/ 3DS modding | 5 | [PSA] Pokémon Home & Bank Connectivity, the "Home Tracker," and 3rd-Party Tools, di javuier_himura | https://www.reddit.com/r/PokemonHome/comments/1vqrxf4/psa_pok%C3%A9mon_home_bank_connectivity_the_home/ |
| 6) How to still get Bank and other games/ 3DS modding | 5 | u/Muddy0258 connectivity chart 2026. Titolo della fonte: Pokemon Connectivity Chart Update - LINK TO HI RES IN TEXT, di Muddy0258 | https://www.reddit.com/r/PokemonHome/comments/1sazzdv/pokemon_connectivity_chart_update_link_to_hi_res/ |
| 7) General tools | 3 | Dragonfly calculators. Titolo della fonte: Calculators / The Cave of Dragonflies | https://www.dragonflycave.com/calculators |
| 7) General tools | 3 | Rotomlabs calculators. Titolo della fonte: Catch Rate Calculator for Pokémon Scarlet and Violet (Gen 9) - RotomLabs | https://rotomlabs.net/scarlet-violet/catch-calculator |
| 7) General tools | 3 | Blisy.net | https://blisy.net/ |
| 8) Shiny Hunting | 5 | Overview on shiny hunting methods with odds of every game. Titolo della fonte: These are all the Hunting Methods of every Game with their Shiny Odds!!, di NewAgeHydreigons | https://www.reddit.com/r/pokemon/comments/10wzzt9/these_are_all_the_hunting_methods_of_every_game/?show=original |
| 8) Shiny Hunting / Gen 1 | 3 | How to shiny hunt in Gen 1. Titolo della fonte: Generation 1 Shiny Hunting - Blue Moon Falls | https://bluemoonfalls.com/pages/shinies/gen-1-shiny-hunting |
| 8) Shiny Hunting / Gen 2 | 3 | Gen 1 and 2 shiny hunting guide. Titolo della fonte: Old-Gen Shiny hunter manual (Generations 1 & 2) - Buried Relic | https://buriedrelic.neocities.org/pages/manual/generations_1_2 |
| 8) Shiny Hunting / Gen 2 | 5 | Gen 2 chain breeding. Titolo della fonte: How to breed an army of Shinies with Red Gyarados, di Chamale | https://www.reddit.com/r/Pokemonguide/comments/8w0x5i/how_to_breed_an_army_of_shinies_with_red_gyarados/ |
| 8) Shiny Hunting / Gen 2 | 2 | Pokemon Crystal Odd Egg | https://bulbapedia.bulbagarden.net/wiki/Odd_Egg |
| 8) Shiny Hunting / Gen 2 | 3 | Shiny Gene Ditto. Titolo della fonte: DV Breeding For Shinies - Blue Moon Falls | https://bluemoonfalls.com/pages/shinies/dv-breeding |
| 8) Shiny Hunting / Gen 3 | 3 | Gen 3 shiny hunting guide. Titolo della fonte: Old-Gen Shiny hunter manual (Generation 3) - Buried Relic | https://buriedrelic.neocities.org/pages/manual/generation_3 |
| 8) Shiny Hunting / Gen 3 | 5 | Overview shiny hunting in Gen 3. Titolo della fonte: Long Shiny hunting guide for gen 3, di Octavius566 | https://www.reddit.com/r/pokemon/comments/6l20ef/long_shiny_hunting_guide_for_gen_3/?show=original |
| 8) Shiny Hunting / Gen 4 | 3 | Gen 4 shiny hunting guide. Titolo della fonte: Old-Gen Shiny hunter manual (Generation 4) - Buried Relic | https://buriedrelic.neocities.org/pages/manual/generation_4 |
| 8) Shiny Hunting / Gen 4 | 2 | Introduction to Masuda Method | https://bulbapedia.bulbagarden.net/wiki/Masuda_method |
| 8) Shiny Hunting / Gen 4 | 5 | How to shiny hunt Manaphy - only for complete maniacs. Titolo della fonte: [Discuss] A guide to shiny hunting Manaphy optimally, di pup_pup_pass | https://www.reddit.com/r/ShinyPokemon/comments/fdowih/discuss_a_guide_to_shiny_hunting_manaphy_optimally/ |
| 8) Shiny Hunting / Gen 5 | 3 | Gen 5 shiny hunting guide. Titolo della fonte: Old-Gen Shiny hunter manual (Generation 5) - Buried Relic | https://buriedrelic.neocities.org/pages/manual/generation_5 |
| 8) Shiny Hunting / Gen 5 | 2 | Introduction of the Shiny Charm in B2W2 | https://bulbapedia.bulbagarden.net/wiki/Shiny_Charm |
| 8) Shiny Hunting / Gen 5 | 2 | Increasing shiny odds with lucky pass power - french. Titolo della fonte: Dossier Shasse > Le secret des Auras Porte-Bonheur - Pokébip.com | https://www.pokebip.com/page/jeux-video/dossier-shasse/auras-porte-bonheur |
| 8) Shiny Hunting / Gen 6 | 5 | [talk] ORAS DexNav Survival Guide - How to chain, what the search level does, and more, di HuntaHuntaHunta | https://www.reddit.com/r/ShinyPokemon/comments/1i8rjzm/talk_oras_dexnav_survival_guide_how_to_chain_what/?show=original |
| 8) Shiny Hunting / Gen 7 | 5 | [Guide] Efficient Breeding in Generation 7, di jman100 | https://www.reddit.com/r/pokemon/comments/5iyoe1/guide_efficient_breeding_in_generation_7/ |
| 8) Shiny Hunting / Gen 7 | 3 | Ultra Wormhole shiny hunting in USUM. Titolo della fonte: Guide to Ultra Space in Pokémon Ultra Sun and Moon - Smogon University | https://www.smogon.com/ingame/guides/ultra_space_guide |
| 8) Shiny Hunting / Gen 8 | 5 | Information on Shiny Hunting in Gen 8. Titolo della fonte: [Gen 8] Updated Shiny Hunting Information, di thackattack42 | https://www.reddit.com/r/ShinyPokemon/comments/e06xqd/gen_8_updated_shiny_hunting_information/ |
| 8) Shiny Hunting / Gen 9 | 5 | Most Efficient Way to Shiny Hunt Mass Outbreak Pokemon in SV. Titolo della fonte: [9] [Guide] Most Efficient Way to Shiny Hunt Mass Outbreak Pokemon in Scarlet and Violet, di kyuuuuuuuuuuute | https://www.reddit.com/r/ShinyPokemon/comments/yzm2sq/9_guide_most_efficient_way_to_shiny_hunt_mass/ |
| 8) Shiny Hunting / Gen 9 | 5 | [Spoilers] Guide to Hunting Shiny Mass Outbreak Pokemon in Scarlet and Violet as Efficiently as Possible, di kyuuuuuuuuuuute | https://www.reddit.com/r/pokemon/comments/yzlk7z/spoilers_guide_to_hunting_shiny_mass_outbreak/ |
| 8) Shiny Hunting / Gen 9 | 5 | Sparkling Power sandwiches. Titolo della fonte: [IX] NEW SHINY SANDWICH GUIDE! Made by Myself!, di Scyfer1 | https://www.reddit.com/r/ShinyPokemon/comments/zsfv1n/ix_new_shiny_sandwich_guide_made_by_myself/?show=original |
| 8) Shiny Hunting / Spinoffs | 3 | Shadow shiny hunting in Pokemon Colosseum. Titolo della fonte: Shiny shadow hunting guide - Buried Relic | https://buriedrelic.neocities.org/pages/shadow_guide |
| 8) Shiny Hunting / Spinoffs | 3 | Shadow shiny hunting in Pokemon XD: Gale of Darkness. Titolo della fonte: Shiny hunting in Gale of Darkness - Buried Relic | https://buriedrelic.neocities.org/pages/GoD_shiny_guide |
| 8) Shiny Hunting / Spinoffs | 5 | Guide on shiny hunting in Pokemons Let's Go with Chain Catching. Titolo della fonte: Pokemon Lets Go Guide for Shiny Hunting, Tracking, and Builds, di Kipter76 | https://www.reddit.com/r/PokemonLetsGo/comments/1fendma/pokemon_lets_go_guide_for_shiny_hunting_tracking/ |
| 8) Shiny Hunting / Spinoffs | 5 | Pokeradar guide BDSP. Titolo della fonte: [BDSP] Poke Radar Guide, di Ephenia | https://www.reddit.com/r/PokeLeaks/comments/qsr6ze/bdsp_poke_radar_guide/ |
| 8) Shiny Hunting / Spinoffs | 3 | Overview on Massive Mass Outbreaks with Permutation hunting in PLA. Titolo della fonte: Shiny Hunting Massive Mass Outbreaks in Pokémon Legends: Arceus | https://rotomlabs.net/guide/shiny-hunting-massive-mass-outbreaks-legends-arceus |
| 8) Shiny Hunting / Spinoffs | 5 | Best shiny hunting locations in PLZA. Titolo della fonte: Best Shiny Hunting Locations/Methods, di -SpinSanity- | https://www.reddit.com/r/PokemonZA/comments/1of201i/best_shiny_hunting_locationsmethods/ |
| 8) Shiny Hunting / Spinoffs | 5 | Guide: How to effectively farm and use Hyper Berries, di SonGouki | https://www.reddit.com/r/PokemonZA/comments/1q2uxey/guide_how_to_effectively_farm_and_use_hyper/ |
| 8) Shiny Hunting / General tips | 5 | r/ShinyPokemon Introduction to Shiny Hunting | https://www.reddit.com/r/ShinyPokemon/wiki/index/#wiki_game_faq |
| 8) Shiny Hunting / General tips | 3 | Overview on utility pokemon for catching. Titolo della fonte: Utility Pokémon - Buried Relic | https://buriedrelic.neocities.org/pages/utility_pokemon |
| 8) Shiny Hunting / General tips | 2 | Shiny locked encounters | https://bulbapedia.bulbagarden.net/wiki/List_of_unobtainable_Shiny_Pok%C3%A9mon |
| 9) RNG Manipulation and Glitches / RNG Manipulation - the best sources to start | 3 | Pokemonrng.com. Titolo della fonte: Retail Emerald Egg RNG | https://www.pokemonrng.com/retail-emerald-egg/ |
| 9) RNG Manipulation and Glitches / RNG Manipulation - the best sources to start | 3 | RNG on retail overview. Titolo della fonte: Retail Pokémon RNG / Tutorials for Pokémon RNG Manipulation | https://retailrng.com/ |
| 9) RNG Manipulation and Glitches / RNG Manipulation - the best sources to start | 5 | Reddit RNG manip | https://www.reddit.com/r/pokemonrng/ |
| 9) RNG Manipulation and Glitches / RNG Manipulation - the best sources to start | 3 | Smogon RNG overview. Titolo della fonte: RNG Mechanics - Smogon University | https://www.smogon.com/ingame/rng/ |
| 9) RNG Manipulation and Glitches / Item Printer Gen 9 | 5 | Apriball RNG manip SV. Titolo della fonte: The Item Printer Trick: A Guide to Apriball Hoarding, di MaryHadALittleDog | https://www.reddit.com/r/PokePortal/comments/1c3c0n8/the_item_printer_trick_a_guide_to_apriball/ |
| 9) RNG Manipulation and Glitches / Item Printer Gen 9 | 5 | Pokeball RNG manip SV. Titolo della fonte: Item Printer Cheatsheet: Pokeball Edition, di Gimikyu_ | https://www.reddit.com/r/PokePortal/comments/1e3ga7e/item_printer_cheatsheet_pokeball_edition/ |
| 9) RNG Manipulation and Glitches / 8F for Gen 1 games | 5 | 8F glitch in Gen 1. Titolo della fonte: How to trick Pokebank into thinking your Gen 1 Mew is the "legit" one from the event via arbitrary code execution with 8F., di TransgenderPride | https://www.reddit.com/r/pokemon/comments/5q4meg/how_to_trick_pokebank_into_thinking_your_gen_1/ |
| 9) RNG Manipulation and Glitches / Coin Case Glitch for Gen 2 games | 2 | Coin Case glitch Gen 2. Titolo della fonte: Coin Case glitches - Glitch City Wiki | https://glitchcity.wiki/wiki/Coin_Case_glitches |
| 9) RNG Manipulation and Glitches / ACE coding in Gen 2 & Gen 3 | 5 | ACE whole Thread + comments. Titolo della fonte: Step by step guides on using ACE to break Gold, Silver and Crystal, applicable for all language releases, di TimoVM | https://www.reddit.com/r/pokemon/comments/17ldkt1/step_by_step_guides_on_using_ace_to_break_gold/ |
| 9) RNG Manipulation and Glitches / ACE coding in Gen 2 & Gen 3 | 5 | ACE Gen 2. Titolo della fonte: 8F + Coincase = Shiny Mew and Shiny Celebi - First Time Using a Pokemon Glitch outside Missingno!, di Hour_Training_832 | https://www.reddit.com/r/PokemonGlitches/comments/1cutdr9/comment/l4lckny/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1 |
| 9) RNG Manipulation and Glitches / ACE coding in Gen 2 & Gen 3 | 3 | ACE Gen 3. Titolo della fonte: ACE3 / Tutorial for gen3 ACE | https://e-sh4rk.github.io/ACE3/ |
| Commenti al post | 5 | here | https://www.reddit.com/r/PokemonHome/s/eAV1QP76Dh |
| Commenti al post | 2 | Serebii.net Event Database | https://www.serebii.net/events/ |
| Commenti al post | 5 | senza descrizione | https://www.reddit.com/r/PokemonHome/s/EluL4buXeT |

### Le fonti che un livello non lo hanno

Non sono di qualità inferiore: sono di natura tale che il criterio dei livelli non si applica, e la colonna dice perché. Un video non è citabile finché non esiste la sua trascrizione, un foglio di calcolo va esportato per essere letto, un'immagine non è testo, e una pagina che pretende l'autenticazione non è raggiungibile dagli strumenti di sessione. Restano qui perché sapere che esistono ha valore e perché ciascuna diventa citabile appena qualcuno paga il suo costo di conversione.

| Cluster | Perché non ha un livello | Che cosa documenta | URL |
|---|---|---|---|
| 1) Dex completions | canale o video: la fonte citabile è la trascrizione, non la pagina | Master Dex challenge - a unique challenge of fulling every spot with special pokemon by Lore Keeper Toby | https://www.youtube.com/watch?v=dKOjYQ5fhQQ |
| 1) Dex completions / Youtube | canale o video: la fonte citabile è la trascrizione, non la pagina | Austin John's Dex video | https://youtu.be/ISPbxFiZkNg?si=0rJM1QCSSX8Mpf4v |
| 1) Dex completions / Youtube | canale o video: la fonte citabile è la trascrizione, non la pagina | LEOsMIND Project OriginDex - German | https://www.youtube.com/watch?v=nhPcPZR9JRk&list=PLNPYWte3HzIUEkeSBiR3DS2H_7d-u3OZ0&pp=0gcJCf4COCosWNin |
| 1) Dex completions / Youtube | canale o video: la fonte citabile è la trascrizione, non la pagina | The domiNATION's Full Living Origin Dex | https://www.youtube.com/watch?v=NByMz7VUCr4&list=PLDaB1K5aJh3p7kkrJ4EpczZsIg_275Edp |
| 1) Dex completions / Youtube | canale o video: la fonte citabile è la trascrizione, non la pagina | Wolf Duckworth's A reasonable Living Pokedex | https://www.youtube.com/watch?v=-QhFxVzxc-0 |
| 1) Dex completions / Youtube | canale o video: la fonte citabile è la trascrizione, non la pagina | Lore Keeper Toby's The most ridiculous Pokedex challenge | https://www.youtube.com/watch?v=ni5DpLjidK8&t=1s |
| 1) Dex completions / Gen 3 | canale o video: la fonte citabile è la trascrizione, non la pagina | FRLG Safari Zone Research | https://www.youtube.com/watch?v=y81nojEHKh8 |
| 1) Dex completions / Gen 3 | canale o video: la fonte citabile è la trascrizione, non la pagina | Arbitrary Code Execution FRLG for past events | https://www.youtube.com/watch?v=fK4jxsuvAsk&t=2512s |
| 1) Dex completions / Gen 4 | canale o video: la fonte citabile è la trascrizione, non la pagina | HGSS ingame trades | https://www.youtube.com/watch?v=xOBSFSiK2R0 |
| 1) Dex completions / Gen 4 | canale o video: la fonte citabile è la trascrizione, non la pagina | HGSS Anti-softlock Tentacool | https://www.youtube.com/watch?v=H73ESn6VYvI |
| 1) Dex completions / Gen 5 | canale o video: la fonte citabile è la trascrizione, non la pagina | B2W2 Yancy/Curtis trades | https://www.youtube.com/watch?v=tb0eeLjTMOo |
| 1) Dex completions / Gen 6 | canale o video: la fonte citabile è la trascrizione, non la pagina | Transfer demo Glalie/Steelix | https://www.youtube.com/watch?v=0jePe3SyuOo |
| 1) Dex completions / Gen 7 | canale o video: la fonte citabile è la trascrizione, non la pagina | Shiny Cap Pikachu | https://www.youtube.com/watch?v=d-2mHUdbn8k |
| 1) Dex completions / Gen 7 | canale o video: la fonte citabile è la trascrizione, non la pagina | Transfer Ash Greninja | https://www.youtube.com/watch?v=o3TWbBsOv8I |
| 1) Dex completions / Gen 7 | canale o video: la fonte citabile è la trascrizione, non la pagina | Zygarde 100% Guide | https://www.youtube.com/watch?v=65OcoKMBK_o |
| 1) Dex completions / Gen 9 | immagine o galleria, non testo | SV sandwich overview | https://imgur.com/a/scarlet-violet-shiny-sandwich-recipes-by-papa-jef-BTuymY3#KpYAPbg |
| 1) Dex completions / Gen 9 | canale o video: la fonte citabile è la trascrizione, non la pagina | How to get all 19 Vivillon patterns in Pokemon Scarlet and Violet | https://www.youtube.com/watch?v=L27WJgiAfAE |
| 1) Dex completions / Spinoffs | richiede autenticazione: non recuperabile dagli strumenti di sessione | Current GO Home dex | https://x.com/gohomedex |
| 3) Collections of one Pokemon species | richiede autenticazione: non recuperabile dagli strumenti di sessione | Misty mark in SV | https://x.com/Sibun4a_Switch/status/1930459094202163632 |
| 5) Other lists and spreadsheets | canale o video: la fonte citabile è la trascrizione, non la pagina | Cherish ball dex | https://www.youtube.com/watch?app=desktop&v=mGM_nNGAEgU |
| 8) Shiny Hunting / Gen 4 | canale o video: la fonte citabile è la trascrizione, non la pagina | Gen 4 Pokeradar | https://youtu.be/AIslziEvNIU?si=ztdU_rYWgxwSsQuH |
| 8) Shiny Hunting / Gen 6 | canale o video: la fonte citabile è la trascrizione, non la pagina | Horde Hunting | https://www.youtube.com/watch?v=fMf-n-MbkuU |
| 8) Shiny Hunting / Gen 6 | canale o video: la fonte citabile è la trascrizione, non la pagina | Chain Fishing | https://www.youtube.com/watch?v=JgvW8fha7k4 |
| 8) Shiny Hunting / Gen 6 | canale o video: la fonte citabile è la trascrizione, non la pagina | A guide to Gen 6 Pokeradar | https://www.youtube.com/watch?v=tDwUBZP5llk&t=63s |
| 8) Shiny Hunting / Gen 6 | canale o video: la fonte citabile è la trascrizione, non la pagina | Friend Safari with all-friend-safari-patch | https://www.youtube.com/watch?v=_pvOsA7Q0KY |
| 8) Shiny Hunting / Gen 7 | canale o video: la fonte citabile è la trascrizione, non la pagina | SOS chaining method | https://www.youtube.com/watch?v=rt94JqpBm5s |
| 8) Shiny Hunting / Gen 8 | canale o video: la fonte citabile è la trascrizione, non la pagina | Shiny hunting in Dynamax adventures | https://www.youtube.com/watch?v=uAIxIe-IsDk |
| 8) Shiny Hunting / Spinoffs | canale o video: la fonte citabile è la trascrizione, non la pagina | Grand underground shiny hunting BDSP | https://www.youtube.com/watch?v=Ab7CrjKRdco |
| 8) Shiny Hunting / Spinoffs | canale o video: la fonte citabile è la trascrizione, non la pagina | Shiny hunting with donuts in Mega Dimensions in PLZA | https://www.youtube.com/watch?v=P1fxsWWvX6c |
| 9) RNG Manipulation and Glitches / RNG Manipulation - the best sources to start | canale o video: la fonte citabile è la trascrizione, non la pagina | YT I'm a blisy | https://www.youtube.com/@imablisy |
| 9) RNG Manipulation and Glitches / RNG Manipulation - the best sources to start | canale o video: la fonte citabile è la trascrizione, non la pagina | YT Lazyhunter | https://www.youtube.com/@ItsLazyHunter |
| 9) RNG Manipulation and Glitches / RNG Manipulation - the best sources to start | canale o video: la fonte citabile è la trascrizione, non la pagina | Cute Charm Glitch | https://www.youtube.com/watch?v=os0AOt1VMi0 |
| 9) RNG Manipulation and Glitches / Item Printer Gen 9 | canale o video: la fonte citabile è la trascrizione, non la pagina | Item RNG manip SV | https://www.youtube.com/watch?v=RvCZ_tHfsMA&list=LL&index=91&t=288s&pp=gAQBiAQB0gcJCd4JAYcqIYzv |
| 9) RNG Manipulation and Glitches / Glitches | canale o video: la fonte citabile è la trascrizione, non la pagina | YT Pape Jefe | https://www.youtube.com/@PapaJefeYT/videos |
| 9) RNG Manipulation and Glitches / ACE coding in Gen 2 & Gen 3 | canale o video: la fonte citabile è la trascrizione, non la pagina | ACE Gen 4 | https://www.youtube.com/watch?v=tmPzFAuKMA8&pp=ygUQcmV0aXJlIGFjZSBnZW4gNA%3D%3D |
| 10) Lastly, a shootout the YT channels I follow closely on the topic of collecting | canale o video: la fonte citabile è la trascrizione, non la pagina | https://www.youtube.com/@LEOsMINDgames | https://www.youtube.com/@LEOsMINDgames |
| 10) Lastly, a shootout the YT channels I follow closely on the topic of collecting | canale o video: la fonte citabile è la trascrizione, non la pagina | https://www.youtube.com/@AustinJohnPlays | https://www.youtube.com/@AustinJohnPlays |
| 10) Lastly, a shootout the YT channels I follow closely on the topic of collecting | canale o video: la fonte citabile è la trascrizione, non la pagina | https://www.youtube.com/@trailspokemon | https://www.youtube.com/@trailspokemon |
| 10) Lastly, a shootout the YT channels I follow closely on the topic of collecting | canale o video: la fonte citabile è la trascrizione, non la pagina | https://www.youtube.com/@ThedomiNATION | https://www.youtube.com/@ThedomiNATION |
| 10) Lastly, a shootout the YT channels I follow closely on the topic of collecting | canale o video: la fonte citabile è la trascrizione, non la pagina | https://www.youtube.com/@JohnstoneYT | https://www.youtube.com/@JohnstoneYT |
| 10) Lastly, a shootout the YT channels I follow closely on the topic of collecting | canale o video: la fonte citabile è la trascrizione, non la pagina | https://www.youtube.com/@PapaJefeYT | https://www.youtube.com/@PapaJefeYT |
| Commenti al post | foglio di calcolo: va esportato e conservato in locale per essere letto | https://docs.google.com/spreadsheets/d/1BL\_YM5paxN67KPik8Z6PLHdYFvGpcrO8Kp58EXGO8yI/edit?gid=1743142233#gid=1743142233 | https://docs.google.com/spreadsheets/d/1BL_YM5paxN67KPik8Z6PLHdYFvGpcrO8Kp58EXGO8yI/edit?gid=1743142233#gid=1743142233 |
| Commenti al post | canale o video: la fonte citabile è la trascrizione, non la pagina | https://www.youtube.com/watch?v=ni5DpLjidK8 | https://www.youtube.com/watch?v=ni5DpLjidK8 |

### Le fonti che il post non cita, ma che il grafo ha trovato

Le centosettantuno righe qui sopra sono i collegamenti che il post di raccolta cita direttamente. Il grafo che ne discende ne contiene molti di più, trovati dentro il corpo dei post che il primo rinviava, e per un giorno sono esistiti soltanto nella cartella grezza sotto `_notes/`, che git ignora e che un giorno sparirà. Questa sottosezione li porta nel registro, perché la frase scritta in testa a questo file, cioè che nessuna informazione su una fonte viva soltanto altrove, o è vera per tutte o non è una regola.

Sono millecentoventotto fonti su duecento host distinti. Il raggruppamento è per host e non per cluster, e la ragione non è di comodo: un cluster queste voci non ce l'hanno, perché nessuna intestazione le governa, e l'host è l'unico raggruppamento che non sia inventato da noi.

Vanno lette per quello che sono, e la distinzione con la sottosezione precedente è netta. Quelle hanno un livello di affidabilità e una descrizione che dice a che cosa servono secondo chi le cita. Queste hanno il titolo che la corsa ha recuperato e la profondità a cui stanno nel grafo, e nient'altro: nessuno le ha lette e nessuno le ha classificate. Una voce migra verso l'alto quando qualcuno la legge e ne ricava qualcosa da citare, e in quel momento prende un livello e una riga propria. Finché resta qui, è un indirizzo che sappiamo esistere e a quale argomento appartiene, il che è molto meno di una fonte e molto più di niente.

La colonna della profondità è il solo indizio di pertinenza che questa sottosezione porta, e conviene usarla: uno è citato dal post di raccolta, due da un post che esso rinvia, tre da un post che quest'ultimo rinvia. Più il numero cresce, più la voce è lontana dalla domanda che ha aperto la corsa.

### reddit.com (169)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 0 | Guide on Pokemon Home Collections - Updated Version, di El_Boosty | scaricato | https://www.reddit.com/r/PokemonHome/comments/1vtj5hf/ |
| 1 | [BDSP] Poke Radar Guide, di Ephenia | scaricato | https://www.reddit.com/r/PokeLeaks/comments/qsr6ze/ |
| 1 | The Item Printer Trick: A Guide to Apriball Hoarding, di MaryHadALittleDog | scaricato | https://www.reddit.com/r/PokePortal/comments/1c3c0n8/ |
| 1 | Item Printer Cheatsheet: Pokeball Edition, di Gimikyu_ | scaricato | https://www.reddit.com/r/PokePortal/comments/1e3ga7e/ |
| 1 | 8F + Coincase = Shiny Mew and Shiny Celebi - First Time Using a Pokemon Glitch outside Missingno!, di Hour_Training_832 | scaricato | https://www.reddit.com/r/PokemonGlitches/comments/1cutdr9/ |
| 1 | How did I get a low level Giritina? Here is a step by step guide so you too can get all the gen 4 and gen 5 event Pokemon! , di BoxLongjumping1067 | scaricato | https://www.reddit.com/r/PokemonHGSS/comments/1hy3b12/ |
| 1 | Special Text About Many Pretty Symbols (STAMPS 6.0), di TwistedTextures | scaricato | https://www.reddit.com/r/PokemonHome/comments/145ylee/ |
| 1 | RULES: READ BEFORE POSTING, di DrTallFuck | scaricato | https://www.reddit.com/r/PokemonHome/comments/15o0lv6/ |
| 1 | Pokemon to transfer before Bank shuts down, di YuiAmon | scaricato | https://www.reddit.com/r/PokemonHome/comments/175qgyy/ |
| 1 | I made a spreadsheet/checklist of all the in-game trades/gift pokemon/interactable pokemon in all the games. This might not be useful to almost anyone, but if there’s someone out there collecting them | scaricato | https://www.reddit.com/r/PokemonHome/comments/17rt8yo/ |
| 1 | Pokémon Bank Exclusives Masterpost, di electroswingmix | scaricato | https://www.reddit.com/r/PokemonHome/comments/1apiuee/ |
| 1 | I made a Noah's Ark Google Sheet Checklist so you don't have to!, di verified-skelly | scaricato | https://www.reddit.com/r/PokemonHome/comments/1djbdm0/ |
| 1 | Rarest pokemon to have, di Dependent_Relief_652 | scaricato | https://www.reddit.com/r/PokemonHome/comments/1flidyg/ |
| 1 | The Origin Living Dex challenge, di Faraknights | scaricato | https://www.reddit.com/r/PokemonHome/comments/1h5p13d/ |
| 1 | My living Origin Dex: Every Pokemon from its original game, plus oddities and events. Cloned Giveaway at the end!, di IzzybearThebestdog | scaricato | https://www.reddit.com/r/PokemonHome/comments/1jmep9q/ |
| 1 | Guide on Pokemon Home Collections, di El_Boosty | scaricato | https://www.reddit.com/r/PokemonHome/comments/1laqzce/ |
| 1 | Gen 3 Check: Pokémon you need to have in Pokémon HOME, di Dararakz | scaricato | https://www.reddit.com/r/PokemonHome/comments/1p06clm/ |
| 1 | Original Region Guides: Gen 1, di electroswingmix | scaricato | https://www.reddit.com/r/PokemonHome/comments/1p0hzxn/ |
| 1 | Original Region Guides: Gen 2, di electroswingmix | scaricato | https://www.reddit.com/r/PokemonHome/comments/1p362dn/ |
| 1 | Gen 4 Check: Pokémon you need to have in Pokémon HOME, di Dararakz | scaricato | https://www.reddit.com/r/PokemonHome/comments/1pd8ve9/ |
| 1 | AlphaDex, part 3, di Roval3 | scaricato | https://www.reddit.com/r/PokemonHome/comments/1py3n1f/ |
| 1 | Pokemon Connectivity Chart Update - LINK TO HI RES IN TEXT, di Muddy0258 | scaricato | https://www.reddit.com/r/PokemonHome/comments/1sazzdv/ |
| 1 | Got frustrated with existing living-dex trackers, so I built one, di xtokri | scaricato | https://www.reddit.com/r/PokemonHome/comments/1st10p1/ |
| 1 | Every pokemon that must be transferred / obtained pre-gen 8, di EpiclyEpicGamerE | scaricato | https://www.reddit.com/r/PokemonHome/comments/1vnlh42/ |
| 1 | All Pokemon Home challenges that will become impossible after bank closes, di WillowOfWisps | scaricato | https://www.reddit.com/r/PokemonHome/comments/1voa411/ |
| 1 | Summary of what will be lost across generations due to Bank closure, di dungeonrpg | scaricato | https://www.reddit.com/r/PokemonHome/comments/1vog8zg/ |
| 1 | Original Region Guides: Gen 3, di electroswingmix | scaricato | https://www.reddit.com/r/PokemonHome/comments/1vphi1w/ |
| 1 | [PSA] Pokémon Home & Bank Connectivity, the "Home Tracker," and 3rd-Party Tools, di javuier_himura | scaricato | https://www.reddit.com/r/PokemonHome/comments/1vqrxf4/ |
| 1 | PSA Lots and Lots of Unique or Event Mons to send up from Bank, di Fatalframe4 | scaricato | https://www.reddit.com/r/PokemonHome/comments/1vrbbom/ |
| 1 | Pokemon Home COMPLETE Living Dex List, di rquinain | scaricato | https://www.reddit.com/r/PokemonHome/comments/f3uaxj/ |
| 1 | Pokémon Collection Spreadsheet, di Thundrosaur | scaricato | https://www.reddit.com/r/PokemonHome/comments/xp1ise/ |
| 1 | Pokemon Lets Go Guide for Shiny Hunting, Tracking, and Builds, di Kipter76 | scaricato | https://www.reddit.com/r/PokemonLetsGo/comments/1fendma/ |
| 1 | Guide for Alcremie in Scarlet/Violet., di Far-Board8733 | scaricato | https://www.reddit.com/r/PokemonScarletViolet/comments/18p237c/ |
| 1 | Best Shiny Hunting Locations/Methods, di -SpinSanity- | scaricato | https://www.reddit.com/r/PokemonZA/comments/1of201i/ |
| 1 | Guide: How to effectively farm and use Hyper Berries, di SonGouki | scaricato | https://www.reddit.com/r/PokemonZA/comments/1q2uxey/ |
| 1 | How to find Swarms, di Chamale | scaricato | https://www.reddit.com/r/Pokemonguide/comments/7b07f6/ |
| 1 | How to find Raikou, Suicune, and Entei: A mathematically optimal guide, updated and corrected, di Chamale | scaricato | https://www.reddit.com/r/Pokemonguide/comments/7c2kcf/ |
| 1 | How to breed an army of Shinies with Red Gyarados, di Chamale | scaricato | https://www.reddit.com/r/Pokemonguide/comments/8w0x5i/ |
| 1 | How to complete your Pokédex in generation 3 (Ruby/Sapphire/Fire Red/Leaf Green/Emerald), di Poison-Powder | scaricato | https://www.reddit.com/r/Pokemonguide/comments/l0bwym/ |
| 1 | [talk] ORAS DexNav Survival Guide - How to chain, what the search level does, and more, di HuntaHuntaHunta | scaricato | https://www.reddit.com/r/ShinyPokemon/comments/1i8rjzm/ |
| 1 | [Gen 8] Updated Shiny Hunting Information, di thackattack42 | scaricato | https://www.reddit.com/r/ShinyPokemon/comments/e06xqd/ |
| 1 | [Discuss] A guide to shiny hunting Manaphy optimally, di pup_pup_pass | scaricato | https://www.reddit.com/r/ShinyPokemon/comments/fdowih/ |
| 1 | [9] [Guide] Most Efficient Way to Shiny Hunt Mass Outbreak Pokemon in Scarlet and Violet, di kyuuuuuuuuuuute | scaricato | https://www.reddit.com/r/ShinyPokemon/comments/yzm2sq/ |
| 1 | [IX] NEW SHINY SANDWICH GUIDE! Made by Myself!, di Scyfer1 | scaricato | https://www.reddit.com/r/ShinyPokemon/comments/zsfv1n/ |
| 1 | These are all the Hunting Methods of every Game with their Shiny Odds!!, di NewAgeHydreigons | scaricato | https://www.reddit.com/r/pokemon/comments/10wzzt9/ |
| 1 | Step by step guides on using ACE to break Gold, Silver and Crystal, applicable for all language releases, di TimoVM | scaricato | https://www.reddit.com/r/pokemon/comments/17ldkt1/ |
| 1 | Creating the Ultimate Pokémon Machine - Nintendo 3DS (v4), di SteveW_MC | scaricato | https://www.reddit.com/r/pokemon/comments/1spdhic/ |
| 1 | This is a map of all the different pokemon you can encounter using the Mew glitch in R/B/Y., di LanAkou | scaricato | https://www.reddit.com/r/pokemon/comments/48bflq/ |
| 1 | [Guide] Getting ANY Pokémon you want in generations 1 through 3: Generation 1 (Part 1 of 3), di UW_Unknown_Warrior | scaricato | https://www.reddit.com/r/pokemon/comments/49r66o/ |
| 1 | [Guide] Efficient Breeding in Generation 7, di jman100 | scaricato | https://www.reddit.com/r/pokemon/comments/5iyoe1/ |
| 1 | How to trick Pokebank into thinking your Gen 1 Mew is the "legit" one from the event via arbitrary code execution with 8F., di TransgenderPride | scaricato | https://www.reddit.com/r/pokemon/comments/5q4meg/ |
| 1 | Long Shiny hunting guide for gen 3, di Octavius566 | scaricato | https://www.reddit.com/r/pokemon/comments/6l20ef/ |
| 1 | A tool for finding the right Headbutt Tree when looking for rare encounters, di TShadowKnight | scaricato | https://www.reddit.com/r/pokemon/comments/72tbz7/ |
| 1 | Reminder: You can set the Vivillon pattern of your game by changing your region before start!, di Starfighter-Suicune | scaricato | https://www.reddit.com/r/pokemon/comments/7blfqr/ |
| 1 | A guide to underleveled Pokemon., di Pikmin34 | scaricato | https://www.reddit.com/r/pokemon/comments/hhlm8k/ |
| 1 | Generation 3 Feebas Guide (also applies to Gen 4), di flipflipshift | scaricato | https://www.reddit.com/r/pokemon/comments/lettfp/ |
| 1 | TIL you can get a Slugma, Wooper and Mareep egg in Violet City right at the start of HGSS, di Merman101 | scaricato | https://www.reddit.com/r/pokemon/comments/lwdw9o/ |
| 1 | Unown's last appearance and how to find all 28 forms, di TechnoTrainer | scaricato | https://www.reddit.com/r/pokemon/comments/odmwcb/ |
| 1 | I've written the most comprehensive guide ever to completing the National Dex in Platinum, di big_bill_wilson | scaricato | https://www.reddit.com/r/pokemon/comments/oyjuy7/ |
| 1 | [Spoilers] Guide to Hunting Shiny Mass Outbreak Pokemon in Scarlet and Violet as Efficiently as Possible, di kyuuuuuuuuuuute | scaricato | https://www.reddit.com/r/pokemon/comments/yzlk7z/ |
| 1 | Legal Matching Pokéballs 2.0 spreadsheet, di OracleLink | scaricato | https://www.reddit.com/r/pokemon/comments/zi89xa/ |
| 1 | In celebration of LGPE, here's a Pikachu Ribbon Master, di SatoSmogonFrog | scaricato | https://www.reddit.com/r/pokemonribbons/comments/9xj21t/ |
| 1 | My guide on the Ribbon Master Challenge, di Athis_891 | scaricato | https://www.reddit.com/r/pokemonribbons/comments/pzzqt4/ |
| 1 | New checklist for Collectors! Every In-Game Event Pokemon! Finish before pokebank goes away forever, di ChaBoiJish | scaricato | https://www.reddit.com/r/pokemontrades/comments/18y648l/ |
| 1 | [DNS] Gen IV & V events (list inside), di JoseGamer33 | scaricato | https://www.reddit.com/r/wiimmfi/comments/fugd8l/ |
| 2 | Video courtesy of u\/Gimikyu\_ | catalogato | https://reddit.com/link/1c3c0n8/video/f8gdakfb27uc1/player |
| 2 | Video courtesy of u\/Gimikyu\_ | catalogato | https://reddit.com/link/1c3c0n8/video/ye30qbit17uc1/player |
| 2 | shoot us a modmail and we'll restore your post | catalogato | https://reddit.com/message/compose?to=%2Fr%2FPokemonLetsGo |
| 2 | Delete | catalogato | https://reddit.com/message/compose?to=xkcd_transcriber&subject=delete&message=delete+t1_dcwjpb8 |
| 2 | Stop Replying | catalogato | https://reddit.com/message/compose?to=xkcd_transcriber&subject=ignore+me&message=ignore+me |
| 2 | collegamento del post | catalogato | https://www.reddit.com/gallery/145ylee |
| 2 | Nearly 13 years ago, I bred a Porygon2 for competitive use in BW during college. Now this digital duck has become one of my most treasured partners in every game since then up to this point. | catalogato | https://www.reddit.com/gallery/18n6upy |
| 2 | collegamento del post | catalogato | https://www.reddit.com/gallery/1hy3b12 |
| 2 | collegamento del post | catalogato | https://www.reddit.com/gallery/1p06clm |
| 2 | ^(delete this message to hide from others.) | catalogato | https://www.reddit.com/message/compose?to=RemindMeBot&subject=Delete+Comment&message=Delete%21+175qgyy |
| 2 | ^(delete this message to hide from others.) | catalogato | https://www.reddit.com/message/compose?to=RemindMeBot&subject=Delete+Comment&message=Delete%21+1apiuee |
| 2 | ^(Your Reminders) | catalogato | https://www.reddit.com/message/compose?to=RemindMeBot&subject=List+Of+Reminders&message=MyReminders%21 |
| 2 | ^(Custom) | catalogato | https://www.reddit.com/message/compose?to=RemindMeBot&subject=Reminder&message=%5BLink+or+message+inside+square+brackets%5D%0A%0ARemindMe%21+Time+period+here |
| 2 | **CLICK THIS LINK** | catalogato | https://www.reddit.com/message/compose?to=RemindMeBot&subject=Reminder&message=%5Bhttps%3A%2F%2Fwww.reddit.com%2Fr%2FPokemonHome%2Fcomments%2F175qgyy%2Fpokemon_to_transfer_before_bank_shuts_down%2Fk4mk9vw%2F%5D%0A%0ARemindMe%21+2023-10-19+22%3A25%3A31+UTC |
| 2 | **CLICK THIS LINK** | catalogato | https://www.reddit.com/message/compose?to=RemindMeBot&subject=Reminder&message=%5Bhttps%3A%2F%2Fwww.reddit.com%2Fr%2FPokemonHome%2Fcomments%2F1apiuee%2Fpok%C3%A9mon_bank_exclusives_masterpost%2Fkqavj9n%2F%5D%0A%0ARemindMe%21+2024-02-20+22%3A35%3A28+UTC |
| 2 | ^(Feedback) | catalogato | https://www.reddit.com/message/compose?to=Watchful1&subject=RemindMeBot+Feedback |
| 2 | Contact | catalogato | https://www.reddit.com/message/compose?to=sneakpeekbot |
| 2 | On a retro Pokémans trip atm and was surprised to find that outside of Zaksabeast’s VC patch, I haven’t been able to find any means of increasing emulator speeds / using Turbo similar to VBA or other  | scaricato | https://www.reddit.com/r/3dshacks/comments/8od01i/ |
| 2 | Creating the Ultimate Pokémon Machine, and more! (v2.0), di SteveW_MC | scaricato | https://www.reddit.com/r/3dspiracy/comments/143tqdv/ |
| 2 | Updated my overview: Transfer Pokémon from 2002 to 2024, di CengizMan | scaricato | https://www.reddit.com/r/NintendoSwitch/comments/1997g3p/ |
| 2 | Clip of Poke Radar Shiny Patch, di Ephenia | scaricato | https://www.reddit.com/r/PokeLeaks/comments/qspevp/ |
| 2 | r/PokePortal | catalogato | https://www.reddit.com/r/PokePortal |
| 2 | Poké Portal Hub | catalogato | https://www.reddit.com/r/PokePortal/channel/b72/Pok%C3%A9_Portal_Hub?entrypoint=chat_share&r=%21fK_JtrSAROOHch1_CB4IbQ%3Areddit.com |
| 2 | Dialga & Palkia Tera Raid Event | catalogato | https://www.reddit.com/r/PokePortal/channel/b73/Dialga_and_Palkia_Raids?entrypoint=chat_share&r=%214ttZggXySmWZ-ng7emYWZQ%3Areddit.com |
| 2 | Ogre Oustin' | catalogato | https://www.reddit.com/r/PokePortal/channel/bcl/Ogre_Oustin?entrypoint=chat_share&r=%21yIi_nXHGQu6__0xWYaRnbg%3Areddit.com |
| 2 | START HERE - YOUR NEW POKÉMON JOURNEY NOW BEGINS!, di madebypeppers | scaricato | https://www.reddit.com/r/PokePortal/comments/14a0wdd/ |
| 2 | User Flair Guide, di ChrisReturns | scaricato | https://www.reddit.com/r/PokePortal/comments/16mtka4/ |
| 2 | Trading Megathread, di AutoModerator | scaricato | https://www.reddit.com/r/PokePortal/comments/182zyzt/ |
| 2 | Blueberry Quest Matchmaking & Guide: 4-Star Sandwich, Dittos, Locations, and More, di Gimikyu_ | scaricato | https://www.reddit.com/r/PokePortal/comments/1c2xfg9/ |
| 2 | Item Printer Cheatsheet: Items Edition, di Gimikyu_ | scaricato | https://www.reddit.com/r/PokePortal/comments/1ctvivd/ |
| 2 | Rui said we had to save all the Shadow Pokemon, so we did!, di awestom | scaricato | https://www.reddit.com/r/PokemonColosseum/comments/1llibtk/ |
| 2 | A new project allows trading directly from your PC to an unmodified switch!, di MineOSaurus_Rex | scaricato | https://www.reddit.com/r/PokemonFireRed/comments/1ugck29/ |
| 2 | My new favorite Pokémon, di ccSleepy | scaricato | https://www.reddit.com/r/PokemonGlitches/comments/w0xt9y/ |
| 2 | Guide with Pictures: How to tell if a pokemon is legit or if it's hacked/genned/fake, di Maeno-san | scaricato | https://www.reddit.com/r/PokemonHome/comments/12vvhbk/ |
| 2 | Here's a Checklist to 100% Complete Pokémon HOME, di luuchuu808 | scaricato | https://www.reddit.com/r/PokemonHome/comments/1bwr0l1/ |
| 2 | Excitedly sitting at 95% completion after more than a decade of playing., di thezemekis | scaricato | https://www.reddit.com/r/PokemonHome/comments/1l8oz88/ |
| 2 | Pokemon Connectivity Chart Update - LINK TO HI-RES IN TEXT, di Muddy0258 | scaricato | https://www.reddit.com/r/PokemonHome/comments/1siu40m/ |
| 2 | Pokemon Home COMPLETE Living Dex List, Spreadsheet Edition, di tjdavis41 | scaricato | https://www.reddit.com/r/PokemonHome/comments/f3yj34/ |
| 2 | Shiny Chances - An Update, di SerebiiNet | scaricato | https://www.reddit.com/r/PokemonLetsGo/comments/a48ruf/ |
| 2 | [Megathread] Trade/Battle Hub, di MagnusRune | scaricato | https://www.reddit.com/r/PokemonLetsGo/comments/e5hyk7/ |
| 2 | Maxed Shiny Living Dex - Max AVs and IVs with (mostly) competitive natures and movesets, di Kipter76 | scaricato | https://www.reddit.com/r/PokemonLetsGo/comments/uxe12w/ |
| 2 | After 2 playthroughs, 3 Mt Battle climbs and a bunch of PokeSpot encounters, I completed and moved my XD living dex into HOME. I just couldn't leave any Pokemon behind with Cipher., di awestom | scaricato | https://www.reddit.com/r/PokemonXD/comments/1m55ms3/ |
| 2 | [Emerald] Officially dons with my Hoenn Pokédex!, di Dianecite | scaricato | https://www.reddit.com/r/ProfessorOak/comments/irslpt/ |
| 2 | RemindMeBot Info v2.1, di Watchful1 | scaricato | https://www.reddit.com/r/RemindMeBot/comments/e1bko7/ |
| 2 | After some tinkering I got Pokemon trading working on the TrimUI Smart Pro. Now I can make a living dex the good old fashioned way!, di TormentedSpirit | scaricato | https://www.reddit.com/r/SBCGaming/comments/1bygkqx/ |
| 2 | Tutorial GBA Multiplayer Online And Local, di PalacioGamer | scaricato | https://www.reddit.com/r/SBCGaming/comments/1d44nn6/ |
| 2 | Trading pokemon between two completely different devices is wild!, di villazeros | scaricato | https://www.reddit.com/r/SBCGaming/comments/1r8erdj/ |
| 2 | [gen2] How to breed an army of Shinies with Red Gyarados, di Chamale | scaricato | https://www.reddit.com/r/ShinyPokemon/comments/8w0ypo/ |
| 2 | [1] [2] Speed up gameplay (and egg hatching) in Virtual Console, di toddwithoned | scaricato | https://www.reddit.com/r/ShinyPokemon/comments/xpwue8/ |
| 2 | [IX] Shiny Sandwich Guide Revisions! I had some issues with my last one that I found, so I went through the calculator and found everything wrong with my recipe, in addition to the Cucumber/Pickle AND | scaricato | https://www.reddit.com/r/ShinyPokemon/comments/zt00q3/ |
| 2 | Wanna complete B2W2? ULTIMATE To-Do List of B2W2!!, di NewAgeHydreigons | scaricato | https://www.reddit.com/r/pokemon/comments/10ttogh/ |
| 2 | r/pokemon is looking for new moderators! Apply within, di DavidLuizshair | scaricato | https://www.reddit.com/r/pokemon/comments/1afr6fn/ |
| 2 | /r/Pokemon is looking for moderators! Apply within!, di Ferretsroq | scaricato | https://www.reddit.com/r/pokemon/comments/1mznkh2/ |
| 2 | Gen I Yellow - List of modified trainers and their spawned Pokémon when using the Trainer Fly glitch, di Kyphis | scaricato | https://www.reddit.com/r/pokemon/comments/1n164g4/ |
| 2 | Gen I R/B & Y - Map of Pokémon spawnable with the Trainer Fly Glitch, di Kyphis | scaricato | https://www.reddit.com/r/pokemon/comments/1n7627e/ |
| 2 | Pokémon Day Presents 2026 Hype Megathread, di pokemon-trainer-blue | scaricato | https://www.reddit.com/r/pokemon/comments/1rg7686/ |
| 2 | Japanese Pokewalker connect with North American HG/SS game?, di sourpickle28 | scaricato | https://www.reddit.com/r/pokemon/comments/2vmvwv/ |
| 2 | [Guide] Getting ANY Pokémon you want in Gold & Silver!, di UW_Unknown_Warrior | scaricato | https://www.reddit.com/r/pokemon/comments/4a6abq/ |
| 2 | Shiny Breeding Exploit., di anon14118 | scaricato | https://www.reddit.com/r/pokemon/comments/5iugaw/ |
| 2 | Step by step guide on how to obtain a Pokebank-compatible Mew in Red/Blue UE, with working 8F ACE setup, di Crystal__ | scaricato | https://www.reddit.com/r/pokemon/comments/5q6zyq/ |
| 2 | Getting gen 1 Mew in Yellow guide (Does not work on R/B and vice versa), di Masked_koopa | scaricato | https://www.reddit.com/r/pokemon/comments/5q8zlg/ |
| 2 | Guide to shiny breeding mechanics in Gen 2, di Nishi7 | scaricato | https://www.reddit.com/r/pokemon/comments/8hf859/ |
| 2 | DNS Exploit Gen 4 Checklist, di TLBidoof | scaricato | https://www.reddit.com/r/pokemon/comments/cs84d1/ |
| 2 | Complete list of Pokémon and shiny forms with matching Pokéballs, di OracleLink | scaricato | https://www.reddit.com/r/pokemon/comments/eey41z/ |
| 2 | Nearly 13 years ago, I bred a Porygon2 for competitive use in BW during college. Now this digital duck has become one of my most treasured partners in every game since then up to this point., di Noaxz | scaricato | https://www.reddit.com/r/pokemonribbons/comments/18n6upy/ |
| 2 | Any advice for the battle tree I'm about to give up, di LadyCiel97 | scaricato | https://www.reddit.com/r/pokemonribbons/comments/18sbp6k/ |
| 2 | Updated my overview: Transfer Pokémon from 2002 to 2024, di CengizMan | scaricato | https://www.reddit.com/r/pokemonribbons/comments/1997e0q/ |
| 2 | Poké Pelago: Shiny Hunting on Isle Abeens, di Asura_Ronin | scaricato | https://www.reddit.com/r/pokemontrades/comments/5o4skp/ |
| 2 | Rule 10B | catalogato | https://www.reddit.com/r/pokemontrades/wiki/rules |
| 2 | blacklist IX, di sneakpeekbot | scaricato | https://www.reddit.com/r/sneakpeekbot/comments/o8wk1r/ |
| 2 | Pokemon Diamond and Pearl mystery gifts not working?, di DazzlingExcitement | scaricato | https://www.reddit.com/r/wiimmfi/comments/ezoj8f/ |
| 2 | HGSS Mystery Gift, di Euphoric_Dealer_4841 | scaricato | https://www.reddit.com/r/wiimmfi/comments/skwg3j/ |
| 2 | Pokemon BW2 Mystery Gift Dates, di _TanMan | scaricato | https://www.reddit.com/r/wiimmfi/comments/wv6nsp/ |
| 2 | xkcd sub | catalogato | https://www.reddit.com/r/xkcd |
| 2 | Problems/Bugs? | catalogato | https://www.reddit.com/r/xkcd_transcriber |
| 2 | u/adamlutz | catalogato | https://www.reddit.com/u/adamlutz |
| 2 | u/AzuriteLeopard | catalogato | https://www.reddit.com/user/AzuriteLeopard |
| 2 | u/ChocoHammy | catalogato | https://www.reddit.com/user/ChocoHammy |
| 2 | u/ChrisReturns | catalogato | https://www.reddit.com/user/ChrisReturns |
| 2 | u/Gimikyu\_ | catalogato | https://www.reddit.com/user/Gimikyu_ |
| 2 | u/MaryHadALittleDog | catalogato | https://www.reddit.com/user/MaryHadALittleDog |
| 2 | u/TLBidoof | catalogato | https://www.reddit.com/user/TLBidoof |
| 2 | u/TheAstrogoth | catalogato | https://www.reddit.com/user/TheAstrogoth |
| 2 | u/greenpangolin17 | catalogato | https://www.reddit.com/user/greenpangolin17 |
| 2 | u/iriomote14 | catalogato | https://www.reddit.com/user/iriomote14 |
| 2 | u/madebypeppers | catalogato | https://www.reddit.com/user/madebypeppers |
| 3 | rNintendoSwitch Rules | catalogato | http://www.reddit.com/r/NintendoSwitch/about/rules |
| 3 | collegamento del post | catalogato | https://www.reddit.com/gallery/1n7627e |
| 3 | collegamento del post | catalogato | https://www.reddit.com/gallery/irslpt |
| 3 | reach out to us in modmail | catalogato | https://www.reddit.com/message/compose?to=%2Fr%2FNintendoSwitch |
| 3 | contact our mod team | catalogato | https://www.reddit.com/message/compose?to=%2Fr%2FPokePortal |
| 3 | here. | catalogato | https://www.reddit.com/message/compose?to=%2Fr%2Fpokemon |
| 3 | ^(delete this message to hide from others.) | catalogato | https://www.reddit.com/message/compose?to=RemindMeBot&subject=Delete+Comment&message=Delete%21+143tqdv |
| 3 | messages to the bot | catalogato | https://www.reddit.com/message/compose?to=RemindMeBot&subject=RemindMe |
| 3 | **CLICK THIS LINK** | catalogato | https://www.reddit.com/message/compose?to=RemindMeBot&subject=Reminder&message=%5Bhttps%3A%2F%2Fwww.reddit.com%2Fr%2F3dspiracy%2Fcomments%2F143tqdv%2Fcreating_the_ultimate_pok%C3%A9mon_machine_and_more_v20%2Fp7q2y57%2F%5D%0A%0ARemindMe%21+2026-09-05+05%3A33%3A38+UTC |
| 3 | this one | catalogato | https://www.reddit.com/message/compose?to=RemindMeBot&subject=Test&message=Test |
| 3 | Errors & Issues Wiki Page | catalogato | https://www.reddit.com/r/3dspiracy/wiki/err |
| 3 | What Games & Apps Can 3DS Play and How do I Get Them? | catalogato | https://www.reddit.com/r/3dspiracy/wiki/games |
| 3 | Common Issues Wiki Page | catalogato | https://www.reddit.com/r/3dspiracy/wiki/issues |
| 3 | 3DS SD Card Wiki Page | catalogato | https://www.reddit.com/r/3dspiracy/wiki/sd_cards |
| 3 | New to Reddit? | catalogato | https://www.reddit.com/r/NewToReddit |
| 3 | r/NintendoSwitch | catalogato | https://www.reddit.com/r/NintendoSwitch |
| 3 | rules | catalogato | https://www.reddit.com/r/PokePortal/wiki/index/rules |
| 3 | Quick Start Guide | catalogato | https://www.reddit.com/r/pokemontrades/wiki/quickstart |

### preview.redd.it (125)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | catalogato | https://preview.redd.it/0fnjmxsnhhmf1.png?width=6912&format=png&auto=webp&s=b5c31b811cc5b6830ca5b6294c13c472b05a5242 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/0qlsadv2mkcd1.png?width=2100&format=png&auto=webp&s=54da3f6f2975392777e4cbcf7f68eb605a2269f6 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/13bpdgsj7buc1.png?width=1137&format=png&auto=webp&s=fafbf21a41e2fc884059f3b2874ca54e2f8b6a1d |
| 2 | senza descrizione | catalogato | https://preview.redd.it/1he5x8nftxre1.jpeg?width=1284&format=pjpg&auto=webp&s=06030d3126d4c5750ef666dda5b9b9e9f884dfff |
| 2 | senza descrizione | catalogato | https://preview.redd.it/1j339kogz9uc1.png?width=1920&format=png&auto=webp&s=fa705f284a58be96df17bd82e155d818a520575c |
| 2 | senza descrizione | catalogato | https://preview.redd.it/1v4zx2q2nxre1.png?width=1080&format=png&auto=webp&s=febec097ea6e4acc6dac9f0868980ca3abf3a42d |
| 2 | senza descrizione | catalogato | https://preview.redd.it/2qhl43sfwauc1.png?width=1855&format=png&auto=webp&s=07e65c8eaa04c2cf90be882470a8c64ee24d4fff |
| 2 | Image credit to u\/MaryHadALittleDog and u\/Gimikyu\_ | catalogato | https://preview.redd.it/2y458ygw57uc1.png?width=1137&format=png&auto=webp&s=28962b87d70e88ffb9a06231f44bbed64f7b020e |
| 2 | senza descrizione | catalogato | https://preview.redd.it/3378nifdtxre1.jpeg?width=1284&format=pjpg&auto=webp&s=867aca36b663a9e9fdcfa66b07cbb067beab896f |
| 2 | senza descrizione | catalogato | https://preview.redd.it/34jwf022skre1.jpeg?width=1179&format=pjpg&auto=webp&s=394e2e36839a0304bc99255d97627f7c850ea8dd |
| 2 | senza descrizione | catalogato | https://preview.redd.it/3b60vobwt3se1.jpeg?width=1284&format=pjpg&auto=webp&s=27e9e882d0d1e66c3b2ba44edd9bd590d0837ee6 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/3s6fqzn81v1c1.jpeg?width=1170&format=pjpg&auto=webp&s=b91d128d66651813227517f6bd8c7355e1aa3eea |
| 2 | senza descrizione | catalogato | https://preview.redd.it/48tg1cz70edd1.jpeg?width=1170&format=pjpg&auto=webp&s=13e9469d448ecb33276230d1432b4089a5b2ce8a |
| 2 | senza descrizione | catalogato | https://preview.redd.it/4bpuyofgo0tg1.png?width=4800&format=png&auto=webp&s=2a7d802f4d06b60d444db212eb67c6d9a6b22987 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/4ebywpxvdase1.jpeg?width=931&format=pjpg&auto=webp&s=becc385fe48ca916192598a92b85045487f6158a |
| 2 | senza descrizione | catalogato | https://preview.redd.it/4hmzwmyofwre1.png?width=1080&format=png&auto=webp&s=c793286c11ca75c9d176b964dc58baa342969440 |
| 2 | Image credit to u\/MaryHadALittleDog and u\/Gimikyu\_ | catalogato | https://preview.redd.it/5p5xjjlqsauc1.png?width=938&format=png&auto=webp&s=c1943b60bb7680e882eb80a2cd77ac003303d5c9 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/647jcdzdauce1.jpeg?width=3024&format=pjpg&auto=webp&s=a0faa7797bd6b2b2ca6444d1e86be9a7d90445bf |
| 2 | senza descrizione | catalogato | https://preview.redd.it/67d3fhvm67uc1.png?width=1128&format=png&auto=webp&s=0a5acab3f22b878b2bc03978ecb413e5c8a68f9c |
| 2 | senza descrizione | catalogato | https://preview.redd.it/6keotrncuxjh1.jpeg?width=1080&format=pjpg&auto=webp&s=c8dd757a922794ca1fcdb2eae5ad1d31f034c7a2 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/6s67ltsbiihg1.jpeg?width=1170&format=pjpg&auto=webp&s=56a75c4181764ef9449097ba9f1ad0b85cf109fc |
| 2 | senza descrizione | catalogato | https://preview.redd.it/7iaikg5z27uc1.png?width=855&format=png&auto=webp&s=c5653a78d2c50d695962ab1eb498b7be8e96da37 |
| 2 | Image credit to u\/MaryHadALittleDog | catalogato | https://preview.redd.it/7o7oyvgv7buc1.png?width=1920&format=png&auto=webp&s=0955ed6fabe258f865364fad65edee12b8014147 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/89n2j4udcwre1.jpeg?width=1080&format=pjpg&auto=webp&s=4a0466749e8a2fc5b2a97deff042da88871f5a46 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/8ph5hib8bz1g1.jpeg?width=4032&format=pjpg&auto=webp&s=931bc98c319e5e90d211d8be4c4ce320d067f658 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/a0s6uftttxre1.jpeg?width=1179&format=pjpg&auto=webp&s=d63aa0d5f3b235778138db4c71ac60198d78c389 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/bkuemaqbdase1.jpeg?width=931&format=pjpg&auto=webp&s=43c0a6d062028da9ad6ef108c61ab8e0e6ce6cfe |
| 2 | Image credit to u\/MaryHadALittleDog and u\/Gimikyu\_ | catalogato | https://preview.redd.it/blb1dsfd67uc1.png?width=1126&format=png&auto=webp&s=f9b33de169d69b1fa78ee94aa7f33a616d962fa5 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/boy0wfpl3o8c1.png?width=1168&format=png&auto=webp&s=fc5b495977dc421e6c747a694c0df2fb630361d2 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/bzpd5bgqourg1.jpeg?width=2160&format=pjpg&auto=webp&s=b3abe958cade57264edc09b42308f148d258564f |
| 2 | senza descrizione | catalogato | https://preview.redd.it/cswslruf90qd1.jpeg?width=1170&format=pjpg&auto=webp&s=de82c2a0f79ffea04c36fc1d0d7f4b408ffda093 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/d5wo9clksj8d1.jpeg?width=1066&format=pjpg&auto=webp&s=19bbbd5d25e5afb564d3bb088700353e4ae04194 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/dadfqc6hkn2g1.jpeg?width=1080&format=pjpg&auto=webp&s=0df4deeb36b7b50bfc5bc83ee2512bb4716673fa |
| 2 | senza descrizione | catalogato | https://preview.redd.it/e2hzc17kbxjh1.jpeg?width=1228&format=pjpg&auto=webp&s=c1b8f6e575f77434f1cae8bad983d459752e3220 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ehpi5i4hagtc1.jpeg?width=1170&format=pjpg&auto=webp&s=1186e79995853b53dc1b91c00218521b7a3067d5 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/f7uz6qpphkzb1.jpeg?width=1170&format=pjpg&auto=webp&s=cf685c0b4da20cf34fe2fdcc3675d8cad73f57fa |
| 2 | senza descrizione | catalogato | https://preview.redd.it/f8qiq56cn0tg1.png?width=9600&format=png&auto=webp&s=2d532960dbec74530c85a96402b76da961ff4a6c |
| 2 | Image credit to u\/MaryHadALittleDog and u\/Gimikyu\_ | catalogato | https://preview.redd.it/iarrgyop67uc1.png?width=1126&format=png&auto=webp&s=ee639852fca1dee425601d63eebca7598739f965 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ivsm9yz75lcd1.png?width=842&format=png&auto=webp&s=5fbfd4fa859d79b8665e5d19782b0416f71d86db |
| 2 | senza descrizione | catalogato | https://preview.redd.it/kepgsj98wxre1.jpeg?width=1200&format=pjpg&auto=webp&s=308ae6a93565bf9b3f6f4c16e2aeec3aad965425 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/kiuku56nz9uc1.png?width=1920&format=png&auto=webp&s=776e099d90293fb8d0825902cf168db590d5faa6 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/klo8eykgm0se1.jpeg?width=1284&format=pjpg&auto=webp&s=c85a877fcfe058e4bc0fd284bcf3e4cfb887a4f5 |
| 2 | They look like this and they really stand out well | catalogato | https://preview.redd.it/l33l6z6oz6z71.png?width=1280&format=png&auto=webp&s=b10c04f546a000eec3a462b7aaa7f160bd7eb71f |
| 2 | senza descrizione | catalogato | https://preview.redd.it/le65449qo4qd1.jpeg?width=1125&format=pjpg&auto=webp&s=59549e9ccf7dd42de3766e03716bbdf8ad3d6c63 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/lehsgj0hrxwg1.png?width=1080&format=png&auto=webp&s=7625aaa182e302ccde84720bde2e80a79bb80c4e |
| 2 | senza descrizione | catalogato | https://preview.redd.it/lynmpk1wq5qe1.jpeg?width=1284&format=pjpg&auto=webp&s=4383c8ee86154a59e577c30e9e253c1d7fcd1ad3 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/m814c6xhcz1g1.png?width=1822&format=png&auto=webp&s=dad2b1a8fba3d92f8a25e2a619b897d4b9ddda31 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/mxmfnoesjwre1.png?width=1080&format=png&auto=webp&s=7cd5f015f69edf6414945eeeda2562f2b064d335 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/mxtgktc647uc1.png?width=1137&format=png&auto=webp&s=250512917b6947f60f1fb9790d46032b2085cde2 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/nx482vcs0xre1.jpeg?width=1080&format=pjpg&auto=webp&s=217a4cb73403d9d365cb6b1436b5307646e123a5 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/o5saweh9yc5b1.jpeg?width=1124&format=pjpg&auto=webp&v=enabled&s=ad81c1f09d9586d49cca2eb161d681c5ac70c2de |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ojd7oo3vtxre1.jpeg?width=1178&format=pjpg&auto=webp&s=4f012221753d3a382cb8758fe5f773d32b3bbdc8 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ossm8jdri0qd1.png?width=1080&format=pjpg&auto=webp&s=0e5b77eb746f17b1d6586fbe8cd4abb6af108904 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/pv7t5lw9gyjh1.jpeg?width=1125&format=pjpg&auto=webp&s=16764fba108f3caf9412bfb516db9f9ac58d8619 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/q2k9m6epn0se1.jpeg?width=1284&format=pjpg&auto=webp&s=e98283436c0c2e4416aa334c5c01d3a4252f814b |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ql9lmusiuxuc1.jpeg?width=1280&format=pjpg&auto=webp&s=b7ecdabcb1f29984036e45e00d51f2e6a1b1faf3 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/qn0u9pk8f85b1.jpeg?width=556&format=pjpg&auto=webp&v=enabled&s=0755b4f24b3241b871848bf9f9ca407adc833cdd |
| 2 | senza descrizione | catalogato | https://preview.redd.it/r1lkhh4tq8mh1.png?width=700&format=png&auto=webp&s=5f78f8c4748a8551826933975a71cb864eab1991 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/r5cvteio67uc1.png?width=1128&format=png&auto=webp&s=1770e0b9b2f313a1b97ca156ffe0eb78a0e36708 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/rfide9mu57uc1.png?width=1138&format=png&auto=webp&s=fa2b6cdad5bea0503822323fba89302b800be237 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ru5912x9jxbe1.png?width=1080&format=pjpg&auto=webp&s=4ee91cf1befd530afd0a1834e3caa8bac144e862 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/t8wb1hihz9uc1.png?width=1920&format=png&auto=webp&s=b00e7167e2ef8939b7487f71a73acefbb48a1d6a |
| 2 | senza descrizione | catalogato | https://preview.redd.it/tapf38lep0qd1.jpeg?width=828&format=pjpg&auto=webp&s=856c4e0d3ec5907d5b7affb24094e3829d675c5a |
| 2 | senza descrizione | catalogato | https://preview.redd.it/tk48jp7komje1.png?width=726&format=png&auto=webp&s=635ad7d5ede1bf28cbffc70526657d8bad4d1739 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/tzc70ywpvxre1.jpeg?width=1080&format=pjpg&auto=webp&s=cbd6ae14860f9776c3dc181404a8e1021de1b407 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/uaj39cuudywg1.png?width=1074&format=png&auto=webp&s=d52740ab5de1c02745484e416cd56d12cf7ec2f2 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ug7qbcp9ndmf1.png?width=6912&format=png&auto=webp&s=be7013ee4315862007d46fe45be6aa006c9ce7e4 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ulqlelparpre1.jpeg?width=1284&format=pjpg&auto=webp&s=d4dbeab70e1d38cb23a865402b068a8a7a599432 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/uztq02p8wauc1.png?width=1885&format=png&auto=webp&s=6906a462565fbacddaf71bf771e300fce1345ebe |
| 2 | senza descrizione | catalogato | https://preview.redd.it/vzyv7yxcp0se1.jpeg?width=1284&format=pjpg&auto=webp&s=69c93802b5823217b5257a0c8cee34770f3f25cd |
| 2 | senza descrizione | catalogato | https://preview.redd.it/w3n4tpysqhjh1.jpeg?width=1920&format=pjpg&auto=webp&s=e356229bae933ba04f8c9b8e5207133ffbfcfc7b |
| 2 | senza descrizione | catalogato | https://preview.redd.it/wqwppuahpxre1.png?width=1080&format=png&auto=webp&s=f0385fec7b5e7459cc20d131002475a1adb63b2d |
| 2 | senza descrizione | catalogato | https://preview.redd.it/x1rvwuxbp0se1.jpeg?width=1284&format=pjpg&auto=webp&s=f99f465058b96bda49609a815d39311029c8f97b |
| 2 | senza descrizione | catalogato | https://preview.redd.it/x8wru35hvauc1.png?width=1487&format=png&auto=webp&s=e03c18b975b235cee1801e786e795ef3ece7ff26 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/xiyliezrzt6f1.png?width=1440&format=png&auto=webp&s=5303f0e58aca8ed5d204555bed3bad3efe415aa5 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/xy062jdv8buc1.png?width=1920&format=png&auto=webp&s=59760fdfb92d1c3a918e00829b1d5f911e8f01ea |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ydu58lg1l2qd1.jpeg?width=3468&format=pjpg&auto=webp&s=277958d83bff24bab568d90dde378ab0eca47418 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/yfv9bzvbcwre1.jpeg?width=1080&format=pjpg&auto=webp&s=95603efaa2e7c9d7b10d5f1932dbb418fea35d0e |
| 2 | senza descrizione | catalogato | https://preview.redd.it/yj09gqatdrlb1.jpeg?width=4032&format=pjpg&auto=webp&s=9044e06e72dad0ec9bc77cabfa2ffe25b4a45156 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ymngby1w05bg1.jpg?width=1867&format=pjpg&auto=webp&s=6aed42649cf0af96bb23950ad4f576103075302d |
| 2 | senza descrizione | catalogato | https://preview.redd.it/ypn1gsalz9uc1.png?width=1920&format=png&auto=webp&s=5a2f8511cba290c6045c6e6a91c598f38677d1b2 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/yt5puzzco12g1.png?width=1080&format=png&auto=webp&s=91b9035a160566ef3e8719e5f0fa95c870214af6 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/yvghw1ulc9od1.png?width=995&format=png&auto=webp&s=4e19cb2541ab33b507428bb263c726162e19ae6d |
| 2 | senza descrizione | catalogato | https://preview.redd.it/zazewpl611qd1.jpeg?width=552&format=pjpg&auto=webp&s=73593f3c5e2bb6c2869660ede0032b65a6d81b83 |
| 2 | senza descrizione | catalogato | https://preview.redd.it/zq52r8bjz9uc1.png?width=1920&format=png&auto=webp&s=017e5037961e9c8ae757adc4c6970fd9ee748fc1 |
| 3 | Poke Portal Menu in Pokemon Scarlet \/ Violet | catalogato | https://preview.redd.it/2ze550pgb66b1.jpg?width=1280&format=pjpg&auto=webp&s=e733298a2f4b6ea6234dd9880f43d92ae550fff7 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/37fwjuc9hgkg1.jpeg?width=3000&format=pjpg&auto=webp&s=c74ca0103fc3e87bb9891209e1ba061c06c65345 |
| 3 | DNS Exploited Larvitar from VGE 2012 Event | catalogato | https://preview.redd.it/431czr856kva1.png?width=1080&format=png&auto=webp&s=f3f972fcb3cbba2774e2b4875f81f063f9db4810 |
| 3 | Megathread Sidebar Widget located on the right side of r\/PokePortal page | catalogato | https://preview.redd.it/4tnw0w65c2hb1.png?width=331&format=png&auto=webp&s=d9718dcec855d00acea42a47430de42c9d2583ba |
| 3 | senza descrizione | catalogato | https://preview.redd.it/4zfj0fz6hgjg1.jpeg?width=1080&format=pjpg&auto=webp&s=51daf319ce7f423ac9c4dd7ab63833909ac08ab0 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/5tq8ukwc6j6g1.jpeg?width=1179&format=pjpg&auto=webp&s=62e1cff17b05a88ebed239090ef349e188e72fb2 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/66p7ztgcsova1.png?width=2300&format=png&auto=webp&v=enabled&s=d8d16c0d2ca024702e2f9d48b1a2055b7f5dc8ae |
| 3 | senza descrizione | catalogato | https://preview.redd.it/6eow3crcvsmg1.jpeg?width=3024&format=pjpg&auto=webp&s=0860c0773426e61342bdbbcf49b05410e7a975c3 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/72oyhufvp01d1.png?width=2100&format=png&auto=webp&s=f532b82f90302ca8fdec0fc3ce4f07e0f0013124 |
| 3 | We choose YOU! | catalogato | https://preview.redd.it/7gm1jy8a15g91.png?width=1800&format=png&auto=webp&s=4dfac5eed2824f36b105d6d2ae195a92969f5cb8 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/8938p2z71i3f1.jpeg?width=3072&format=pjpg&auto=webp&s=2cf9f0f220b035a72df983323bfa4cca67e3357e |
| 3 | senza descrizione | catalogato | https://preview.redd.it/9yokzoynfmug1.png?width=9600&format=png&auto=webp&s=7fe7a48aaca35e569a9d1f7393977ca3e7018970 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/b2e86br8nhq91.jpg?width=4032&format=pjpg&auto=webp&s=cae260fad4fb2e4870189c52af093f73c9671113 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/bfd0iqminskd1.jpeg?width=1235&format=pjpg&auto=webp&s=96f649c8ec54377bd3a3f6ae7f77bb84f34a8ede |
| 3 | Ditto Blocks Map + Tips | catalogato | https://preview.redd.it/cgk1hulrm7uc1.png?width=2048&format=png&auto=webp&s=3c9bfd54df3aaafc9a3e116ede12c0fc0cf01a1e |
| 3 | senza descrizione | catalogato | https://preview.redd.it/cyxggbukdxyf1.jpeg?width=3024&format=pjpg&auto=webp&s=a3c15ed64488a80ed410abf1d78d49f4a18fb3a5 |
| 3 | Courtesy of u\/Gimikyu\_ | catalogato | https://preview.redd.it/e7y5vrf2kkzb1.png?width=1800&format=png&auto=webp&s=0176f17405efad3e27438dccdac3738dcba3dca8 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/et3i2y4evsmg1.jpeg?width=3024&format=pjpg&auto=webp&s=c89b93d5f2b721c2bded02afa36dfc5df78957f0 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/g07hbmoh98pb1.png?width=4420&format=png&auto=webp&s=a2683118c5dc3f20a0d04b3fa4d6c0f3bcffe5c7 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/g9sh9br8nhq91.jpg?width=4032&format=pjpg&auto=webp&s=de5cf5d49cfeff82c81cff6115a952df98bf4ca2 |
| 3 | BBQs Cheatsheet: 4-Star Sandwich, Wild Tera Pokemon, Locations, and Tips | catalogato | https://preview.redd.it/gdzyj0zlm7uc1.png?width=2048&format=png&auto=webp&s=1355d40d2877da70a880de71a3cc33f331a7d8c4 |
| 3 | This Phanpy has a natural IV distribution and looks good at first, until you notice that the OTID is 00000, which means it's very likely fake. | catalogato | https://preview.redd.it/gxyiazrr2kva1.jpg?width=1080&format=pjpg&auto=webp&s=a1d8890abfbc95e99596004a3e048d9899d2fa02 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/hehwq0dfupmf1.png?width=941&format=png&auto=webp&s=6daa9b5974178fe30546ed1ba925143aaa8927c9 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/iik81i3rrede1.png?width=1080&format=png&auto=webp&s=395c9522485fb3b121169ddde36af85375525ff2 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/ipeiqvefvsmg1.jpeg?width=3024&format=pjpg&auto=webp&s=277b0a73d1dd048f3a98427ccca4260e2ff7c416 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/j13lpz9259mg1.jpeg?width=1440&format=pjpg&auto=webp&s=98272860b2a122699e3cb75e2257667ffe5220ef |
| 3 | This Bulbasaur is obviously fake because it has 6 perfect IVs and the OT is BlainesYT, a youtuber and known genner. | catalogato | https://preview.redd.it/jnmwa86c2kva1.jpg?width=1080&format=pjpg&auto=webp&s=bf8df85c3d982d665ac3ab3320bbd2245bbb1f22 |
| 3 | Infographic by u\/MaryHadALittleDog | catalogato | https://preview.redd.it/knyo9yde98pb1.png?width=960&format=png&auto=webp&s=23514c3f9eff0d0a63cb25b1d9fed5474bf30cae |
| 3 | senza descrizione | catalogato | https://preview.redd.it/o0zs38z8tvpd1.jpeg?width=710&format=pjpg&auto=webp&s=fdc568d13e3c8f4d2e84addcf2aec6325c67e7e7 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/po955zpgvsmg1.jpeg?width=3024&format=pjpg&auto=webp&s=2ec04da33bbc89c4140ed823185f4819c82d161e |
| 3 | senza descrizione | catalogato | https://preview.redd.it/pwrs9gti0cqb1.png?width=1080&format=pjpg&auto=webp&s=1cbfd7d7a85510f41758b85d05c31fd529803d21 |
| 3 | Top Menu Bar, clicking the down arrow shows each individual Live Megathread | catalogato | https://preview.redd.it/q9bh6zrwe66b1.png?width=365&format=png&auto=webp&s=c0725a748ddd1a5e265f0b06e77822e94ae7dbfd |
| 3 | senza descrizione | catalogato | https://preview.redd.it/sl3kspdcz30c1.png?width=3024&format=png&auto=webp&s=9d9023919693770caab400bcea52a439b2afa7eb |
| 3 | Do you have a Link Code? | catalogato | https://preview.redd.it/slqj5o6xjkzb1.jpg?width=1280&format=pjpg&auto=webp&s=ff251068f225aaff557045d54e44800b4283291f |
| 3 | senza descrizione | catalogato | https://preview.redd.it/ucfxhdphvsmg1.jpeg?width=3024&format=pjpg&auto=webp&s=3c46be2315277bb2cc086f3373f34324b6ce42e7 |
| 3 | Live Megathreads located at the left side of this post as a list | catalogato | https://preview.redd.it/v6iy6hf1c2hb1.png?width=1260&format=png&auto=webp&s=df9484c2a53fce413e2d757ee40afdcb59cb9c75 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/v888sbhatvpd1.jpeg?width=788&format=pjpg&auto=webp&s=53369d55213d182394d18003bdf0c94ac0bd85d7 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/vvcinxvjzjva1.jpg?width=1080&format=pjpg&auto=webp&s=27c8cf33670cf3555efebfc0720b5231f4e06ee2 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/wb5auf4ubvne1.jpeg?width=3000&format=pjpg&auto=webp&s=a9fc970120eeb24539c67ef2f926dc3b3d88a918 |
| 3 | senza descrizione | catalogato | https://preview.redd.it/x4xm1u9vrede1.png?width=1080&format=png&auto=webp&s=a593a072d5be70017735931a9b1eca85d61a18f9 |

### youtube.com (81)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 1 | Cherish ball dex | catalogato | https://www.youtube.com/watch?v=mGM_nNGAEgU |
| 2 | Super Mario World -- Credits Warp in 5:59.6 (First Time Ever on Console) | catalogato | http://www.youtube.com/watch?v=14wqBA5Q1yc |
| 2 | Pokemon Sun and Moon PokeBank: How to transfer shiny Pokemon from Gen 1 (100% WORKS!!!) | catalogato | http://www.youtube.com/watch?v=5uDQLUi0ZEo |
| 2 | vegeta throws dog bones at guildo | catalogato | http://www.youtube.com/watch?v=6XX5nIQqjrQ |
| 2 | TasBlock at AGDQ 2017: TASBot | catalogato | http://www.youtube.com/watch?v=7CgXvIuZR40&t=2s |
| 2 | Pokemon Blue: "Jailbreaking" the Gameboy with 8F (no TASing needed) | catalogato | http://www.youtube.com/watch?v=D3EvpRHL_vk |
| 2 | File Select - Super Mario 64 Music Extended | catalogato | http://www.youtube.com/watch?v=DdDI53VeGAc |
| 2 | TFS Cell - I HAVE SO MANY QUESTIONS | catalogato | http://www.youtube.com/watch?v=NsEIu6-lciA |
| 2 | Tasbot does Tasblock - Awesome Games Done Quick 2017 - Part 170 | catalogato | http://www.youtube.com/watch?v=Ukq29ePnTqI&t=1740s |
| 2 | Using 8F to turn Pallet Town into "Twinleaf Town", 'permanently' (Red/Blue) | catalogato | http://www.youtube.com/watch?v=ddSHGg4-qSY |
| 2 | SNES Code Injection -- Flappy Bird in SMW | catalogato | http://www.youtube.com/watch?v=hB6eY73sLV0 |
| 2 | *^BrawlBRSTMs3 ^X* | catalogato | https://www.youtube.com/channel/UCN2hyYKiVMH4Ka-TCuO_obw |
| 2 | senza descrizione | catalogato | https://www.youtube.com/watch?v=14wqBA5Q1yc |
| 2 | Pomeg Glitch | catalogato | https://www.youtube.com/watch?v=1cEm84fUmE4&t=0s |
| 2 | Professor Oak | catalogato | https://www.youtube.com/watch?v=1nC7gAAdSPo&list=PLWQDwiGdrVjkPMnCe9P73FPzeDWUrgT6V&pp=iAQB |
| 2 | Here's | catalogato | https://www.youtube.com/watch?v=5CtLqTc8IaM |
| 2 | senza descrizione | catalogato | https://www.youtube.com/watch?v=5uDQLUi0ZEo&lc= |
| 2 | Have a biscuit! | catalogato | https://www.youtube.com/watch?v=6XX5nIQqjrQ |
| 2 | Catch 'em All | catalogato | https://www.youtube.com/watch?v=7dcg_XMBUTI&list=PLWQDwiGdrVjnvvVbFq9bM4nGc4mCx3_5-&pp=iAQB |
| 2 | here | catalogato | https://www.youtube.com/watch?v=CL3xn_Miai0 |
| 2 | here | catalogato | https://www.youtube.com/watch?v=Csq0y-npQhI |
| 2 | https://www.youtube.com/watch?v=Es6Lg0yCEZ4 | catalogato | https://www.youtube.com/watch?v=Es6Lg0yCEZ4 |
| 2 | senza descrizione | catalogato | https://www.youtube.com/watch?v=EvFSPUr6GFY |
| 2 | senza descrizione | catalogato | https://www.youtube.com/watch?v=H8AgGp5cqPI |
| 2 | here | catalogato | https://www.youtube.com/watch?v=ISPbxFiZkNg |
| 2 | This video details it out and has the QR Codes. | catalogato | https://www.youtube.com/watch?v=IdlKn5oJyxI |
| 2 | https://www.youtube.com/watch?v=Ld2YphF-HVI&t=1s | catalogato | https://www.youtube.com/watch?v=Ld2YphF-HVI&t=1s |
| 2 | The domiNATION's Origin Dex Challenge | catalogato | https://www.youtube.com/watch?v=NByMz7VUCr4 |
| 2 | here | catalogato | https://www.youtube.com/watch?v=NeJeWOcWS5Y |
| 2 | Semi-Perfect Cell is that you? | catalogato | https://www.youtube.com/watch?v=NsEIu6-lciA |
| 2 | this TAS | catalogato | https://www.youtube.com/watch?v=OPcV9uIY5i4 |
| 2 | original video | catalogato | https://www.youtube.com/watch?v=Om0Wljzq5Oc |
| 2 | senza descrizione | catalogato | https://www.youtube.com/watch?v=P28kp66XMw4 |
| 2 | here | catalogato | https://www.youtube.com/watch?v=PRq7rJ7E7hU |
| 2 | CandyEvie's "How to Clone Pokemon & Items WITHOUT a Cheating Device!" Guide | catalogato | https://www.youtube.com/watch?v=PRq7rJ7E7hU&pp=ygUUZW1lcmFsZCBjbG9uZSBnbGl0Y2g%3D |
| 2 | Youtube link | catalogato | https://www.youtube.com/watch?v=PsIb3OZaYAs |
| 2 | The domiNATION's Gen 2 Origin Dex Challenge | catalogato | https://www.youtube.com/watch?v=QyK6gKosVnk |
| 2 | Reshiram's Trainer's Switch-only HOME Dex Guide | catalogato | https://www.youtube.com/watch?v=RHybpfl1Cgo |
| 2 | The domiNATION's Gen 3 Origin Dex Challenge | catalogato | https://www.youtube.com/watch?v=UPgq1is8MNg |
| 2 | what they did this year | catalogato | https://www.youtube.com/watch?v=Ukq29ePnTqI&t=29m |
| 2 | here | catalogato | https://www.youtube.com/watch?v=XV2k8nhdIhQ |
| 2 | Cute Charm Glitch | catalogato | https://www.youtube.com/watch?v=XjBAf0E8Zv8 |
| 2 | lv23 Kingambits | catalogato | https://www.youtube.com/watch?v=alqy1Truez8 |
| 2 | this | catalogato | https://www.youtube.com/watch?v=ddSHGg4-qSY |
| 2 | here | catalogato | https://www.youtube.com/watch?v=g9rq5c8Lh7k |
| 2 | All Three Starters | catalogato | https://www.youtube.com/watch?v=g9rq5c8Lh7k&pp=ygUUc3RhcnRlcnMgZ2VuIDIgY2xvbmU%3D |
| 2 | Additional Video Guide | catalogato | https://www.youtube.com/watch?v=grQLseuc4YE |
| 2 | this guy | catalogato | https://www.youtube.com/watch?v=hB6eY73sLV0 |
| 2 | here | catalogato | https://www.youtube.com/watch?v=p9IhBTcTw9w |
| 2 | 8F Mew Guide | catalogato | https://www.youtube.com/watch?v=rvhuJsS4EhE |
| 2 | here | catalogato | https://www.youtube.com/watch?v=rvhuJsS4EhE&t=2259s&pp=ygUVYXVzdGluIGpvaG4gcGxheXMgbWV3 |
| 2 | here | catalogato | https://www.youtube.com/watch?v=ubPS74aiMRo |
| 2 | one | catalogato | https://www.youtube.com/watch?v=wQ39NwjFwfE |
| 2 | follow up | catalogato | https://www.youtube.com/watch?v=yyIa9611uZk |
| 2 | senza descrizione | catalogato | https://youtube.com/shorts/MC8UcAATaE4 |
| 3 | senza descrizione | catalogato | http://www.youtube.com/watch?v=Sw0h7ImFsAs |
| 3 | *^jelome1989* | catalogato | https://www.youtube.com/channel/UCJ6244ZF0wybrxZxUNS--AA |
| 3 | *^TheZZAZZGlitch* | catalogato | https://www.youtube.com/channel/UCKlA7qF9XKwu79ULYmVu28w |
| 3 | ReneaCollects | catalogato | https://www.youtube.com/channel/UCNOJh-R1C9OBC4TqNwEAMMg |
| 3 | *^Crystal_* | catalogato | https://www.youtube.com/channel/UCQcizw_rc-q55lmwU3w6-wA |
| 3 | senza descrizione | catalogato | https://www.youtube.com/watch?v=98_azamLeh4 |
| 3 | Video Proof of Isle Abeens Shiny Hunting | catalogato | https://www.youtube.com/watch?v=9EKfcIpYS2w&t=1s%2F |
| 3 | Youtube | catalogato | https://www.youtube.com/watch?v=Dh2WcRJOVPU |
| 3 | senza descrizione | catalogato | https://www.youtube.com/watch?v=E757YbGVWoo |
| 3 | collegamento del post | catalogato | https://www.youtube.com/watch?v=GWWCicAWpNY |
| 3 | senza descrizione | catalogato | https://www.youtube.com/watch?v=H8AgGp5cqPI&t=32s |
| 3 | senza descrizione | catalogato | https://www.youtube.com/watch?v=H8AgGp5cqPI&t=9m47s |
| 3 | https://www.youtube.com/watch?v=KlxO\_Ge\_BdI&t=72s | catalogato | https://www.youtube.com/watch?v=KlxO_Ge_BdI&t=72s |
| 3 | https://www.youtube.com/watch?v=NeJeWOcWS5Y&t=52s | catalogato | https://www.youtube.com/watch?v=NeJeWOcWS5Y&t=52s |
| 3 | https://www.youtube.com/watch?v=Qcp4vxyaUJc | catalogato | https://www.youtube.com/watch?v=Qcp4vxyaUJc |
| 3 | senza descrizione | catalogato | https://www.youtube.com/watch?v=WD_GVaQwn8o |
| 3 | link | catalogato | https://www.youtube.com/watch?v=fKiRIMDNj4A |
| 3 | Here's | catalogato | https://www.youtube.com/watch?v=jR5rov2e6PU |
| 3 | https://www.youtube.com/watch?v=k0HFRpqvSk4&t=3s&ab\_channel=Voltzo%28Manectric77%29 | catalogato | https://www.youtube.com/watch?v=k0HFRpqvSk4&t=3s&ab_channel=Voltzo%28Manectric77%29 |
| 3 | link | catalogato | https://www.youtube.com/watch?v=mQLkeK3ETP4 |
| 3 | Glitzer Popping | catalogato | https://www.youtube.com/watch?v=nOEwPnv2TFM |
| 3 | Odd Tinkering | catalogato | https://youtube.com/@OddTinkering |
| 3 | Retro Game Corps | catalogato | https://youtube.com/@RetroGameCorps |
| 3 | Scott the Woz | catalogato | https://youtube.com/@ScottTheWoz |
| 3 | The Retro Future | catalogato | https://youtube.com/@TheRetroFuture |
| 3 | Wulff Den | catalogato | https://youtube.com/@WulffDen |

### bulbapedia.bulbagarden.net (77)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | experience underflow glitch, enabling it to jump to level 100 immediately | catalogato | http://bulbapedia.bulbagarden.net/wiki/Experience |
| 2 | This list | catalogato | http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_index_number_%28Generation_I%29 |
| 2 | looked up here | catalogato | http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_index_number_(Generation_I\ |
| 2 | Bulbapedia article | catalogato | http://bulbapedia.bulbagarden.net/wiki/Mew_glitch |
| 2 | Alpha Pokemon | catalogato | https://bulbapedia.bulbagarden.net/wiki/Alpha_Pok%C3%A9mon |
| 2 | Birth Island | catalogato | https://bulbapedia.bulbagarden.net/wiki/Birth_Island |
| 2 | senza descrizione | catalogato | https://bulbapedia.bulbagarden.net/wiki/Catch_Combo |
| 2 | Celebi and Bellsprout are in the same group | catalogato | https://bulbapedia.bulbagarden.net/wiki/Category:Pok%C3%A9mon_in_the_Medium_Slow_experience_group |
| 2 | Coin Case Glitch | catalogato | https://bulbapedia.bulbagarden.net/wiki/Coin_Case_glitches |
| 2 | Curtis | catalogato | https://bulbapedia.bulbagarden.net/wiki/Curtis |
| 2 | Cute Charm Glitch | catalogato | https://bulbapedia.bulbagarden.net/wiki/Cute_Charm_(Ability |
| 2 | https://bulbapedia.bulbagarden.net/wiki/DexNav#Calculated\_rates | catalogato | https://bulbapedia.bulbagarden.net/wiki/DexNav |
| 2 | Dongle Method | catalogato | https://bulbapedia.bulbagarden.net/wiki/Dual-slot_mode |
| 2 | GBA eReader | catalogato | https://bulbapedia.bulbagarden.net/wiki/E-Reader |
| 2 | here | catalogato | https://bulbapedia.bulbagarden.net/wiki/Fight_Safari_Zone_Pok%C3%A9mon_trick |
| 2 | https://bulbapedia.bulbagarden.net/wiki/Gender#Generation\_I | catalogato | https://bulbapedia.bulbagarden.net/wiki/Gender |
| 2 | GTS | catalogato | https://bulbapedia.bulbagarden.net/wiki/Global_Trade_System |
| 2 | Hayley ones | catalogato | https://bulbapedia.bulbagarden.net/wiki/Hayley |
| 2 | Hayley's Trades from | catalogato | https://bulbapedia.bulbagarden.net/wiki/Hayley%27s_trades |
| 2 | here | catalogato | https://bulbapedia.bulbagarden.net/wiki/Headbutt_tree |
| 2 | here | catalogato | https://bulbapedia.bulbagarden.net/wiki/In-game_trade |
| 2 | here | catalogato | https://bulbapedia.bulbagarden.net/wiki/Item_duplication_glitch |
| 2 | trade with Jasmine in HeartGold/SoulSilver. | catalogato | https://bulbapedia.bulbagarden.net/wiki/Jasmine%27s_Steelix |
| 2 | senza descrizione | catalogato | https://bulbapedia.bulbagarden.net/wiki/List\_of\_Wi-Fi\_English\_event\_Pok%C3%A9mon\_distributions\_(Generation\_V |
| 2 | senza descrizione | catalogato | https://bulbapedia.bulbagarden.net/wiki/List\_of\_local\_English\_event\_Pok%C3%A9mon\_distributions\_(Generation\_IV |
| 2 | senza descrizione | catalogato | https://bulbapedia.bulbagarden.net/wiki/List\_of\_local\_English\_event\_Pok%C3%A9mon\_distributions\_(Generation\_V |
| 2 | This bulbapedia list | catalogato | https://bulbapedia.bulbagarden.net/wiki/List_of_local_Japanese_event_Pokémon_distributions_in_Generation_IV |
| 2 | senza descrizione | catalogato | https://bulbapedia.bulbagarden.net/wiki/Mew\_glitch |
| 2 | You can also get Mew from My Pokemon Ranch | catalogato | https://bulbapedia.bulbagarden.net/wiki/My_Pok%C3%A9mon_Ranch |
| 2 | My Pokémon Ranch | catalogato | https://bulbapedia.bulbagarden.net/wiki/My_Pokémon_Ranch |
| 2 | Pal Park | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pal_Park |
| 2 | Gen VIII | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pikachu_in_a_cap |
| 2 | Poké Radar Shiny Odds | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9_Radar |
| 2 | *Pokémon Battle Revolution* | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Battle_Revolution |
| 2 | *Pokémon Box Ruby & Sapphire* | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Box_Ruby_%26_Sapphire |
| 2 | *Pokémon Channel* | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Channel |
| 2 | *Pokémon Colosseum* | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Colosseum |
| 2 | WISHMKR Jirachi | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Colosseum_Bonus_Disc |
| 2 | *XD: Gale of Darkness* | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_XD:_Gale_of_Darkness |
| 2 | Poke-Transfer | catalogato | https://bulbapedia.bulbagarden.net/wiki/Poké_Transfer |
| 2 | Pokémon Battle Revolution | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pokémon_Battle_Revolution |
| 2 | Pokémon Box: Ruby & Sapphire | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pokémon_Box_Ruby_%26_Sapphire |
| 2 | Pokémon Channel | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pokémon_Channel |
| 2 | Pokémon Colosseum | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pokémon_Colosseum |
| 2 | Pokémon Dream RADAR | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pokémon_Dream_Radar |
| 2 | Pokémon Dream World | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pokémon_Dream_World |
| 2 | Pokémon Global Link | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pokémon_Global_Link |
| 2 | Pokémon Ranger | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pokémon_Ranger_series |
| 2 | Pokémon Gale of Darkness XD | catalogato | https://bulbapedia.bulbagarden.net/wiki/Pokémon_XD:_Gale_of_Darkness |
| 2 | You can get Darkrai by loading a save file with Darkrai (or the mission) in Shadows of Almia | catalogato | https://bulbapedia.bulbagarden.net/wiki/Ranger_Net |
| 2 | https://bulbapedia.bulbagarden.net/wiki/Record\_mixing#Feebas\_factor | catalogato | https://bulbapedia.bulbagarden.net/wiki/Record_mixing |
| 2 | Bulbapedia | catalogato | https://bulbapedia.bulbagarden.net/wiki/Roaming_Pok%C3%A9mon |
| 2 | More details on Bulbapedia. | catalogato | https://bulbapedia.bulbagarden.net/wiki/Sinjoh_Ruins |
| 2 | Time Capsule Exploit | catalogato | https://bulbapedia.bulbagarden.net/wiki/Time_Capsule_exploit |
| 2 | https://bulbapedia.bulbagarden.net/wiki/Turnback\_Cave#Before\_encountering\_a\_pillar | catalogato | https://bulbapedia.bulbagarden.net/wiki/Turnback_Cave |
| 2 | level 63 in Sw/Sh | catalogato | https://bulbapedia.bulbagarden.net/wiki/Victini_(Pok%C3%A9mon |
| 2 | https://bulbapedia.bulbagarden.net/wiki/Wild\_Area\_News/2021#February\_4\_to\_8.2C\_2021 | catalogato | https://bulbapedia.bulbagarden.net/wiki/Wild_Area_News/2021 |
| 2 | Yancy | catalogato | https://bulbapedia.bulbagarden.net/wiki/Yancy |
| 3 | senza descrizione | non raggiunto | http://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_event_Pokémon_distributions_in_Generation_I |
| 3 | This list of Pokémon by index number | non raggiunto | http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_index_number_%28Generation_II%29 |
| 3 | see here | non raggiunto | http://bulbapedia.bulbagarden.net/wiki/List_of_items_by_index_number_%28Generation_II%29 |
| 3 | senza descrizione | non raggiunto | http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_breeding |
| 3 | here | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/Anville_Town |
| 3 | Black City (Bulbapedia) | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/Black_City |
| 3 | here | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/Black_Tower |
| 3 | Honey Tree (Bulbapedia) | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/Honey_Tree |
| 3 | senza descrizione | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/List_of_Transform_glitches |
| 3 | here is a wifi events | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/List_of_Wi-Fi_English_event_Pokémon_distributions_(Generation_IV |
| 3 | here | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/List_of_glitches_(Generation_V |
| 3 | here is local events | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/List_of_local_English_event_Pokémon_distributions_(Generation_IV |
| 3 | the full list of locations in each game by index number. | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/List_of_locations_by_index_number |
| 3 | senza descrizione | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/Obedience |
| 3 | Pokémon: Let's Go, Pikachu! and Let's Go, Eevee! | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon:_Let%27s_Go,_Pikachu!_and_Let%27s_Go,_Eevee |
| 3 | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon\_HOME#Compatibility\_with\_Let.27s\_Go.2C\_Pikachu.21\_and\_Let.27s\_Go.2C\_Eevee.21 | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_HOME |
| 3 | here | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/Prop |
| 3 | here | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/Union_Room |
| 3 | White Forest (Bulbapedia) | non raggiunto | https://bulbapedia.bulbagarden.net/wiki/White_Forest |

### github.com (66)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Releases · Ajarmar/universal-pokemon-randomizer-zx · GitHub | scaricato | https://github.com/Ajarmar/universal-pokemon-randomizer-zx/releases |
| 2 | Home · Ajarmar/universal-pokemon-randomizer-zx Wiki · GitHub | scaricato | https://github.com/Ajarmar/universal-pokemon-randomizer-zx/wiki |
| 2 | GitHub - DS-Homebrew/GodMode9i: GodMode9i Explorer - A full access file browser for the Nintendo DS and DSi consoles :godmode: · GitHub | scaricato | https://github.com/DS-Homebrew/GodMode9i |
| 2 | Pokemon DPPt & HGSS stops finding Wii after connecting to Pokemon Battle Revolution & My Pokemon Ranch (Wii) · Issue #415 · DS-Homebrew/nds-bootstrap · GitHub | scaricato | https://github.com/DS-Homebrew/nds-bootstrap/issues/415 |
| 2 | GitHub - FlagBrew/PKSM: Gen I to GenVIII save manager. · GitHub | scaricato | https://github.com/FlagBrew/PKSM |
| 2 | Home · FlagBrew/PKSM Wiki · GitHub | scaricato | https://github.com/FlagBrew/PKSM/wiki |
| 2 | Basics · FlagBrew/PKSM Wiki · GitHub | scaricato | https://github.com/FlagBrew/PKSM/wiki/Basics |
| 2 | Settings · FlagBrew/PKSM Wiki · GitHub | scaricato | https://github.com/FlagBrew/PKSM/wiki/Settings |
| 2 | DLS1-Files/IRAO/_list.txt at master · InternalLoss/DLS1-Files · GitHub | scaricato | https://github.com/InternalLoss/DLS1-Files/blob/master/IRAO/_list.txt |
| 2 | 8F-Helper/README.md at master · KernelEquinox/8F-Helper · GitHub | scaricato | https://github.com/KernelEquinox/8F-Helper/blob/master/README.md |
| 2 | Cheat Engine · LumaTeam/Luma3DS Wiki · GitHub | scaricato | https://github.com/LumaTeam/Luma3DS/wiki/Cheat-Engine |
| 2 | GitHub - MechanicalDragon0687/ndsForwarder: Generate and Install NDS Forwarders · GitHub | scaricato | https://github.com/MechanicalDragon0687/NDSForwarder |
| 2 | GitHub - MechanicalDragon0687/ndsForwarder: Generate and Install NDS Forwarders · GitHub | scaricato | https://github.com/MechanicalDragon0687/ndsForwarder |
| 2 | GitHub - RiiConnect24/DNS-Server: This server will allow you to connect to RiiConnect24 Servers when your Internet Service Provider does not work allow using Custom DNS. · GitHub | scaricato | https://github.com/RiiConnect24/DNS-Server |
| 2 | GitHub - TurdPooCharger/GBAVCSM: A GodMode9 script dedicated to handling GBA VC saves. · GitHub | scaricato | https://github.com/TurdPooCharger/GBAVCSM |
| 2 | GitHub - TuxSH/TWLSaveTool: 3DS homebrew app that allows you to read, write, and erase save files from NDS cartridges (2015-2016) · GitHub | scaricato | https://github.com/TuxSH/TWLSaveTool |
| 2 | GitHub - andrewbenington/OpenHome: Application for importing and transferring Pokémon between save files · GitHub | scaricato | https://github.com/andrewbenington/OpenHome |
| 2 | Release Citra save support · concreted/3DSync · GitHub | scaricato | https://github.com/concreted/3DSync/releases/tag/citra-sync |
| 2 | GitHub - francesco265/RtcPwalker: Patch for Pokemon HG/SS that allows the game to communicate with the Pokéwalker by using the 3DS built-in IR transceiver. · GitHub | scaricato | https://github.com/francesco265/RtcPwalker |
| 2 | GitHub - ghnr/sneakpeekbot: sneakpeekbot from reddit · GitHub | scaricato | https://github.com/ghnr/sneakpeekbot |
| 2 | GitHub - kristopheles/monarium: Customizable Pokédex generator and tracker. Self-hosted, offline-first, 11 languages. · GitHub | scaricato | https://github.com/kristopheles/monarium |
| 2 | GitHub - kuroppoi/entralinked: A standalone Game Sync emulator for Pokémon Black & White. · GitHub | scaricato | https://github.com/kuroppoi/entralinked |
| 2 | GitHub - mtheall/ftpd: FTP Server for 3DS/Switch · GitHub | scaricato | https://github.com/mtheall/ftpd |
| 2 | GitHub - semaj14/Multi-PokemonFramework: A CTRPF plugin for the Nintendo 3DS Pokémon games that supports both the 6th and 7th generations. · GitHub | scaricato | https://github.com/semaj14/Multi-PokemonFramework |
| 2 | GitHub - suloku/BW_tool: Tool to modify Pokémon generation V savegames · GitHub | scaricato | https://github.com/suloku/BW_tool |
| 2 | GitHub - yuhasem/FeebasFinder: A tool to find which tiles you can get Feebas from · GitHub | scaricato | https://github.com/yuhasem/FeebasFinder |
| 2 | poc_utils/tas/notes.md at master · yuhasem/poc_utils · GitHub | scaricato | https://github.com/yuhasem/poc_utils/blob/master/tas/notes.md |
| 2 | GitHub - zaksabeast/DreamRadarCartRedirect: A patch for dream radar redirecting nds cart reading/writing to a file on the SD · GitHub | scaricato | https://github.com/zaksabeast/DreamRadarCartRedirect |
| 3 | NTR Launcher | non raggiunto | https://github.com/ApacheThunder/NTR_Launcher/releases/download/1.9.9/NTR_Launcher.cia |
| 3 | second menu | non raggiunto | https://github.com/DS-Homebrew/TWiLightMenu |
| 3 | here | non raggiunto | https://github.com/DS-Homebrew/TWiLightMenu/releases |
| 3 | nds-bootstrap | non raggiunto | https://github.com/DS-Homebrew/nds-bootstrap |
| 3 | PC client | non raggiunto | https://github.com/FlagBrew/PKSM-Scripts/blob/master/sendScript.py |
| 3 | senza descrizione | non raggiunto | https://github.com/FlagBrew/PKSM.git |
| 3 | Source | non raggiunto | https://github.com/FlagBrew/PKSM/issues/1055 |
| 3 | senza descrizione | non raggiunto | https://github.com/FlagBrew/PKSM/releases |
| 3 | senza descrizione | non raggiunto | https://github.com/FlagBrew/PKSM/wiki/Built-In-Scripts |
| 3 | Edit the Pokémon to make it legal | non raggiunto | https://github.com/FlagBrew/PKSM/wiki/Editor |
| 3 | senza descrizione | non raggiunto | https://github.com/FlagBrew/PKSM/wiki/Hex-Editor |
| 3 | senza descrizione | non raggiunto | https://github.com/Gericom/GBARunner2/releases/tag/v20200217-194452_0b8bbe3 |
| 3 | the Japanese do, I just havent been able to decipher it | non raggiunto | https://github.com/MersenneTwister-Lab/TinyMT/blob/master/jump/sample.c |
| 3 | senza descrizione | non raggiunto | https://github.com/Olmectron/Simple-Web-App-GUI-for-YANBF-Generator |
| 3 | senza descrizione | non raggiunto | https://github.com/RocketRobz/NTR_Forwarder/releases |
| 3 | senza descrizione | non raggiunto | https://github.com/TheLevelUp/pos-tls-patcher |
| 3 | senza descrizione | non raggiunto | https://github.com/Universal-Team/Universal-Updater/releases |
| 3 | senza descrizione | non raggiunto | https://github.com/Watchful1/RemindMeBot |
| 3 | senza descrizione | non raggiunto | https://github.com/YANBForwarder/YANBF/issues |
| 3 | senza descrizione | non raggiunto | https://github.com/YANBForwarder/YANBF/releases |
| 3 | senza descrizione | non raggiunto | https://github.com/YANBForwarder/assets |
| 3 | senza descrizione | non raggiunto | https://github.com/christianhaitian/retroarch-cores/tree/master |
| 3 | senza descrizione | non raggiunto | https://github.com/concreted/3DSync/commits/citra-sync |
| 3 | senza descrizione | non raggiunto | https://github.com/gdkchan/Ohana3DS-Rebirth |
| 3 | Wumiibo | non raggiunto | https://github.com/hax0kartik/wumiibo |
| 3 | senza descrizione | non raggiunto | https://github.com/joel16/3DShell |
| 3 | senza descrizione | non raggiunto | https://github.com/kuroppoi/entralinked.git |
| 3 | senza descrizione | non raggiunto | https://github.com/kwsch/PKHeX |
| 3 | senza descrizione | non raggiunto | https://github.com/lifehackerhansol/YANBF/releases/tag/v1.0.1 |
| 3 | senza descrizione | non raggiunto | https://github.com/lifehackerhansol/YANBF/releases/tag/v1.1.0 |
| 3 | 1 | non raggiunto | https://github.com/mamba2410/reverse-pokewalker |
| 3 | DaedalusX64 for 3DS | non raggiunto | https://github.com/masterfeizz/DaedalusX64-3DS/releases |
| 3 | senza descrizione | non raggiunto | https://github.com/polaris-/dwc_network_server_emulator/wiki/Nintendo-DS-Download-Content |
| 3 | pokered disassembly | non raggiunto | https://github.com/pret/pokered |
| 3 | EventsGallery (GitHub) | non raggiunto | https://github.com/projectpokemon/EventsGallery/tree/master/Released/Gen%205/C-Gear%20Backgrounds |
| 3 | EventsGallery (GitHub) | non raggiunto | https://github.com/projectpokemon/EventsGallery/tree/master/Released/Gen%205/Musicals |
| 3 | EventsGallery (GitHub) | non raggiunto | https://github.com/projectpokemon/EventsGallery/tree/master/Released/Gen%205/Pokedex%20Skins |
| 3 | EventsGallery (GitHub) | non raggiunto | https://github.com/projectpokemon/EventsGallery/tree/master/Released/Gen%205/World%20Tournaments |

### i.imgur.com (54)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | In this example, I’ve raised a Kadabra to 188 Special | catalogato | http://i.imgur.com/110bWGX.png?1= |
| 2 | senza descrizione | catalogato | http://i.imgur.com/54YGQqv.png |
| 2 | senza descrizione | catalogato | http://i.imgur.com/6wT4Pks.png |
| 2 | fight a trainer | catalogato | http://i.imgur.com/7KUidYJ.png?1= |
| 2 | there is the Pokémon you were looking for | catalogato | http://i.imgur.com/7cg3AYx.png?1= |
| 2 | senza descrizione | catalogato | http://i.imgur.com/8LMkJ0T.jpg |
| 2 | you should see the exclamation mark on the LD trainer | catalogato | http://i.imgur.com/B2UYqLi.png?1= |
| 2 | re-access SS. Anne and the truck | catalogato | http://i.imgur.com/DNIUIRu.png?1= |
| 2 | right before you fly off | catalogato | http://i.imgur.com/FnbFZNl.png?1= |
| 2 | Stand here | catalogato | http://i.imgur.com/LUTduWI.png?1= |
| 2 | gambler outside of underground path house west of Saffron City | catalogato | http://i.imgur.com/RdtPdUl.png?1= |
| 2 | senza descrizione | catalogato | http://i.imgur.com/Yf2aV9B.png |
| 2 | you should be facing west when you return to your game | catalogato | http://i.imgur.com/Z7ReGcr.png?1= |
| 2 | nugget bridge one | catalogato | http://i.imgur.com/fbgacRf.png?1= |
| 2 | Here | catalogato | http://i.imgur.com/ktn2bK3.jpg |
| 2 | senza descrizione | catalogato | http://i.imgur.com/oIMT53Q.png |
| 2 | Walk towards them, pressing start right before the step finishes | catalogato | http://i.imgur.com/rc3KeV7.png?1= |
| 2 | You’ll surf over the sailor | catalogato | http://i.imgur.com/uVn8uay.png?1= |
| 2 | the START menu will pop up | catalogato | http://i.imgur.com/vCWPwmK.png?1= |
| 2 | go to any of the long-distance trainers and stand just out of their reach | catalogato | http://i.imgur.com/xFrHYnj.png?1= |
| 2 | transform into Kadabra (or whatever Pokémon you've used | catalogato | http://i.imgur.com/ykmcESd.png?1= |
| 2 | Pokéball | catalogato | https://i.imgur.com/XgAhEXa.png |
| 3 | nature | catalogato | http://i.imgur.com/17PlyDA.jpg |
| 3 | the path shown in this image | catalogato | http://i.imgur.com/3o7klcA.png |
| 3 | this is the final state | catalogato | http://i.imgur.com/7grgOoS.png?1= |
| 3 | Hatch the egg | catalogato | http://i.imgur.com/8LDE3wO.png?1= |
| 3 | senza descrizione | catalogato | http://i.imgur.com/9zS2Nsv.jpg |
| 3 | Listen to the cry of either Machop, Machoke, Bellsprout, Omanyte or Celebi in the Pokédex | catalogato | http://i.imgur.com/AX0lYmk.png?1= |
| 3 | but it only knows Splash | catalogato | http://i.imgur.com/AkdJS3r.png?1= |
| 3 | it's beautiful | catalogato | http://i.imgur.com/CNxQwf6.jpg |
| 3 | This is what it looks like after I execute the first code | catalogato | http://i.imgur.com/DEs0AXG.png?1= |
| 3 | This is my initial item list | catalogato | http://i.imgur.com/EEjqFe7.png?1= |
| 3 | Open our Pokédex | catalogato | http://i.imgur.com/GkakEW8.png?1= |
| 3 | “Use” the coin case | catalogato | http://i.imgur.com/JMrUhTJ.png?1= |
| 3 | boss called RICK | catalogato | http://i.imgur.com/KMrQpaV.png?1= |
| 3 | Quagsire with Protein and 4 moves with the first being Sleep Talk | catalogato | http://i.imgur.com/KuQsNWD.png?1= |
| 3 | senza descrizione | catalogato | http://i.imgur.com/OJQJYN6.png |
| 3 | we fly to Cherrygrove City | catalogato | http://i.imgur.com/P9RfMJv.png?1= |
| 3 | an UMBREON should come out | catalogato | http://i.imgur.com/RzE7Bf1.png?1= |
| 3 | We give it a Rare Candy to level 1 and POOF, Umbreon will relearn all its default moves | catalogato | http://i.imgur.com/UwQI59C.png?1= |
| 3 | senza descrizione | catalogato | http://i.imgur.com/X75kwOi.jpg |
| 3 | senza descrizione | catalogato | http://i.imgur.com/YAGpXPd.png |
| 3 | MRW after getting excited for getting Mew, and then seeing how long and complex this and the 8F item methods are. | catalogato | http://i.imgur.com/YO9YFgc.mp4 |
| 3 | senza descrizione | catalogato | http://i.imgur.com/ZNn7K6j.png |
| 3 | We name Box 9 **!/RZ’v♂** | catalogato | http://i.imgur.com/ZXgSGNa.png?1= |
| 3 | little green guy | catalogato | http://i.imgur.com/eZqV6b6.jpg |
| 3 | IVs | catalogato | http://i.imgur.com/fo5WNjO.jpg |
| 3 | my Umbreon is now level 0 | catalogato | http://i.imgur.com/j3yeMjZ.png?1= |
| 3 | Step exactly 4 tiles to the right | catalogato | http://i.imgur.com/jKxEVTN.png?1= |
| 3 | go out | catalogato | http://i.imgur.com/kqmBl63.png?1= |
| 3 | I got a shiny | catalogato | http://i.imgur.com/mBznNBB.jpg |
| 3 | Go inside the Mart | catalogato | http://i.imgur.com/oaA4AXS.png?1= |
| 3 | lvl 254 Blissey with Tail Whip (which I defeat with Toxic) | catalogato | http://i.imgur.com/vOMd5Yq.png?1= |
| 3 | senza descrizione | catalogato | http://i.imgur.com/yefMuNy.jpg |

### serebii.net (50)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Pokémon Scarlet & Violet - Sandwich Ingredients | scaricato | https://serebii.net/scarletviolet/sandwichingredients.shtml |
| 2 | Pokémon Black 2 & Pokémon White 2 - Gift Pokémon | scaricato | https://www.serebii.net/black2white2/gift.shtml |
| 2 | Pokémon Black 2 & Pokémon White 2 - In-Game Events | scaricato | https://www.serebii.net/black2white2/ingameevent.shtml |
| 2 | Pokémon Black 2 & Pokémon White 2 - N's Pokémon | scaricato | https://www.serebii.net/black2white2/nspokemon.shtml |
| 2 | Pokémon Black & White - Wi-Fi Events | scaricato | https://www.serebii.net/blackwhite/wifievents.shtml |
| 2 | Pokémon Brilliant Diamond & Shining Pearl - Shiny Pokémon & Shiny Rates | scaricato | https://www.serebii.net/brilliantdiamondshiningpearl/shinypokemon.shtml |
| 2 | Serebii.net Eventdex - #0386 Deoxys | scaricato | https://www.serebii.net/events/dex/386.shtml |
| 2 | Serebii.net Eventdex - #0647 Keldeo | scaricato | https://www.serebii.net/events/dex/647.shtml |
| 2 | Serebii.net Eventdex - #0649 Genesect | scaricato | https://www.serebii.net/events/dex/649.shtml |
| 2 | Serebii.net Games - The Feebas Factor | scaricato | https://www.serebii.net/games/feebas.shtml |
| 2 | Serebii.net Games - PokéBall Details | scaricato | https://www.serebii.net/games/pokeball.shtml |
| 2 | Pokémon Heart Gold & Soul Silver - PokéWalker | scaricato | https://www.serebii.net/heartgoldsoulsilver/pokewalker.shtml |
| 2 | Pokémon Heart Gold & Soul Silver - The Wi-Fi Events | scaricato | https://www.serebii.net/heartgoldsoulsilver/wifievents.shtml |
| 2 | Serebii.net ItemDex - Salty Herba Mystica | scaricato | https://www.serebii.net/itemdex/saltyherbamystica.shtml |
| 2 | Pokémon Legends: Arceus - Massive Mass Outbreaks | scaricato | https://www.serebii.net/legendsarceus/massivemassoutbreaks.shtml |
| 2 | Pokémon Legends: Arceus - Mass Outbreaks | scaricato | https://www.serebii.net/legendsarceus/massoutbreaks.shtml |
| 2 | Pokémon Let's Go, Pikachu & Let's Go, Eevee - Wild Pokémon & Capture Mechanics | scaricato | https://www.serebii.net/letsgopikachueevee/capture.shtml |
| 2 | Pokémon Let's Go, Pikachu & Let's Go, Eevee - Catch Combo | scaricato | https://www.serebii.net/letsgopikachueevee/catchcombo.shtml |
| 2 | Pokémon Let's Go, Pikachu & Let's Go, Eevee - Gift Pokémon | scaricato | https://www.serebii.net/letsgopikachueevee/gift.shtml |
| 2 | Pokémon Let's Go, Pikachu & Let's Go, Eevee - Rare Spawns | scaricato | https://www.serebii.net/letsgopikachueevee/rarespawns.shtml |
| 2 | Pokémon Platinum - The Regi Factor | scaricato | https://www.serebii.net/platinum/regigigas.shtml |
| 2 | Pokémon Champions - Available Pokémon | scaricato | https://www.serebii.net/pokemonchampions/pokemon.shtml |
| 2 | Pokémon HOME - Changing Moves | scaricato | https://www.serebii.net/pokemonhome/changemoves.shtml |
| 2 | Pokémon Red & Blue - Japanese Green & Blue Versions | scaricato | https://www.serebii.net/rb/greenblue.shtml |
| 2 | Pokémon Scarlet & Violet - In-Game Trades | scaricato | https://www.serebii.net/scarletviolet/ingametrades.shtml |
| 2 | Pokémon Scarlet & Violet - Mass Outbreaks | scaricato | https://www.serebii.net/scarletviolet/massoutbreaks.shtml |
| 2 | Pokémon Scarlet & Violet - Sandwiches | scaricato | https://www.serebii.net/scarletviolet/sandwich.shtml |
| 2 | Pokémon Stadium - Prizes | scaricato | https://www.serebii.net/stadium/prizes.shtml |
| 2 | Pokémon Stadium 2 - Prizes | scaricato | https://www.serebii.net/stadium2/prizes.shtml |
| 2 | Pokémon Sun & Pokémon Moon - Unobtainable Pokémon | scaricato | https://www.serebii.net/sunmoon/unobtainable.shtml |
| 2 | Pokémon Sword & Shield - Max Raid Battles - Event Den Listings - Secrets of the Jungle Tie-In | scaricato | https://www.serebii.net/swordshield/maxraidbattles/eventden-secretsofthejungletie-in.shtml |
| 2 | Pokémon Sword & Shield - Shiny Pokémon | scaricato | https://www.serebii.net/swordshield/shinypokemon.shtml |
| 2 | Pokémon Ultra Sun & Ultra Moon - Alola Photo Club | scaricato | https://www.serebii.net/ultrasunultramoon/alolaphotoclub.shtml |
| 2 | Pokémon Ultra Sun & Pokémon Ultra Moon - Unobtainable Pokémon | scaricato | https://www.serebii.net/ultrasunultramoon/unobtainable.shtml |
| 3 | Serebii | non raggiunto | https://serebii.net/ |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/battlesubway.shtml |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/droppeditem.shtml |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/funfestmission.shtml |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/hiddengrotto.shtml |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/ingametrade.shtml |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/joinavenue.shtml |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/medals.shtml |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/pokestar.shtml |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/tmhm.shtml |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/trainercard.shtml |
| 3 | here | non raggiunto | https://www.serebii.net/black2white2/worldtournament.shtml |
| 3 | the eventdex for every pokemon on Serebii here | non raggiunto | https://www.serebii.net/events/dex |
| 3 | the full list of ribbons and their games on Serebii | non raggiunto | https://www.serebii.net/games/ribbons.shtml |
| 3 | ORAS Demo | non raggiunto | https://www.serebii.net/omegarubyalphasapphire/demo.shtml |
| 3 | Sun/Moon demo | non raggiunto | https://www.serebii.net/sunmoon/demo.shtml |

### docs.google.com (37)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | complete (I think) list | catalogato | https://docs.google.com/document/d/1hkdRJFgZOEzhKMHH0opOv0E2Qs8EecjpulPGFJefZ8c/edit?usp=sharing |
| 2 | senza descrizione | catalogato | https://docs.google.com/document/d/1lbcUDFVjqDQLn0INCJBrJvMTzzlQ-cpmzQCzp9rAQTs/edit?usp=drivesdk |
| 2 | a guide to collecting every possible underleveled Pokemon. | catalogato | https://docs.google.com/document/d/e/2PACX-1vSZHF4sdFUmF0ttnVfgwFrKzfa99gm1OEy0UJ9KkFWvBA4fFKPyNcwWyfqaGS5CbFGtuk0M67cKEWI8/pub |
| 2 | https://docs.google.com/spreadsheets/d/11lZYY9qUE3I1d7\_Kc3M3q03KIuYGFBaWvWqN2X\_qSOk/edit?usp=sharing | catalogato | https://docs.google.com/spreadsheets/d/11lZYY9qUE3I1d7_Kc3M3q03KIuYGFBaWvWqN2X_qSOk/edit?usp=sharing |
| 2 | Bank Closing all possible things checklist V0.5 | catalogato | https://docs.google.com/spreadsheets/d/14QTf2q3rRFlaIqHxigfFyKiKZdL9o6uc_bQE-OtOTwk/edit?gid=1932480820 |
| 2 | spreadsheet | catalogato | https://docs.google.com/spreadsheets/d/14QTf2q3rRFlaIqHxigfFyKiKZdL9o6uc_bQE-OtOTwk/edit?usp=sharing |
| 2 | https://docs.google.com/spreadsheets/d/160\_C7klF\_MFGlZJnnfmYe1cjW-uFAto9CB3yLSe8Tv0/edit?usp=sharing | catalogato | https://docs.google.com/spreadsheets/d/160_C7klF_MFGlZJnnfmYe1cjW-uFAto9CB3yLSe8Tv0/edit?usp=sharing |
| 2 | https://docs.google.com/spreadsheets/d/17K4aF5H3ALbvdi65IN5npJ4L7LxmUjgVUNS9-orS\_G8/edit?usp=sharing | catalogato | https://docs.google.com/spreadsheets/d/17K4aF5H3ALbvdi65IN5npJ4L7LxmUjgVUNS9-orS_G8/edit?usp=sharing |
| 2 | senza descrizione | catalogato | https://docs.google.com/spreadsheets/d/1ClSTolvZmTHeI4uItfKIVsSHfUxws7BnzlUTVV9zEYs/edit?usp=sharing |
| 2 | https://docs.google.com/spreadsheets/d/1JOdD5FECYkZqWuLoc6vV1mhbBl\_4AuvE/edit?gid=179090297#gid=179090297 | catalogato | https://docs.google.com/spreadsheets/d/1JOdD5FECYkZqWuLoc6vV1mhbBl_4AuvE/edit?gid=179090297 |
| 2 | 3DS Home Challenge\ | catalogato | https://docs.google.com/spreadsheets/d/1K8-2rWbMiVcV3RaW0uMmHF5Yeo7j-iUfjoBFqzzaJ2s/edit?usp=sharing |
| 2 | Kipter's Edition of Austin John's Shiny Dex Organizer with Extension to LGPE | catalogato | https://docs.google.com/spreadsheets/d/1LHYu6VQru7snvshafOvBItlVr_LTLf4WH4TYiQyO6GY/edit?usp=sharing |
| 2 | senza descrizione | catalogato | https://docs.google.com/spreadsheets/d/1Np71tQe_CLWfVEHNY6158twKeGSq3lUdAJTxlRjuRAw/edit?usp=sharing |
| 2 | https://docs.google.com/spreadsheets/d/1PO8Jj-xHmQXrQel-Xpaopgty1ozgEynv/edit?usp=sharing&ouid=105928561876625854556&rtpof=true&sd=true | catalogato | https://docs.google.com/spreadsheets/d/1PO8Jj-xHmQXrQel-Xpaopgty1ozgEynv/edit?usp=sharing&ouid=105928561876625854556&rtpof=true&sd=true |
| 2 | https://docs.google.com/spreadsheets/d/1S5LkoD502R9H2rbAkKsbnqrjckhlMqRP6ooG2iGyL5Q/edit?usp=sharing | catalogato | https://docs.google.com/spreadsheets/d/1S5LkoD502R9H2rbAkKsbnqrjckhlMqRP6ooG2iGyL5Q/edit?usp=sharing |
| 2 | **Legal Matching Pokéballs 2.0** | catalogato | https://docs.google.com/spreadsheets/d/1T5RMu189-uMrknJlAPNp3QbQAyp8t0N5/edit?usp=sharing&ouid=103067789524497045001&rtpof=true&sd=true |
| 2 | https://docs.google.com/spreadsheets/d/1TLEbEeXsaCsJgPNN-ehrVqTvNbP8KM9f3U5FLKNS6TI/edit?usp=sharing | catalogato | https://docs.google.com/spreadsheets/d/1TLEbEeXsaCsJgPNN-ehrVqTvNbP8KM9f3U5FLKNS6TI/edit?usp=sharing |
| 2 | senza descrizione | catalogato | https://docs.google.com/spreadsheets/d/1U_X4rB3LIAI66HpFE8lDIsCHkZbOiQ7rZAxmahUZ_Z4/edit?usp=sharing |
| 2 | senza descrizione | catalogato | https://docs.google.com/spreadsheets/d/1X4HlOobLKhBNfxMy3yUbXe015Sr_nZybKlQD7GuR8LU/edit |
| 2 | https://docs.google.com/spreadsheets/d/1asxeqWirsimzhBaFChP7Yavf5RdEFu9gHJ4tpmD6N5o/edit?usp=sharing | catalogato | https://docs.google.com/spreadsheets/d/1asxeqWirsimzhBaFChP7Yavf5RdEFu9gHJ4tpmD6N5o/edit?usp=sharing |
| 2 | hisuian voltorb/electrode | catalogato | https://docs.google.com/spreadsheets/d/1bvIx7Q2Lxp7efHRrUh48WkuwirNlKardwSHVz_R8kA0/edit |
| 2 | collegamento del post | catalogato | https://docs.google.com/spreadsheets/d/1nE47IB6uY81f8ESsg05iCuA34QmoCJNqYb3qNyUOm_A/edit |
| 2 | https://docs.google.com/spreadsheets/d/1uv3jgQw\_1yJeNZucT-DPzWWhHEwitx6-1qAzh9FQ6ZA/edit?gid=459916946#gid=459916946 | catalogato | https://docs.google.com/spreadsheets/d/1uv3jgQw_1yJeNZucT-DPzWWhHEwitx6-1qAzh9FQ6ZA/edit?gid=459916946 |
| 2 | https://docs.google.com/spreadsheets/d/1xvCQs2JprtSVOf47omRvoaMwTO7EXtRLKbdZyAnRc4U/edit?gid=1179485747#gid=1179485747 | catalogato | https://docs.google.com/spreadsheets/d/1xvCQs2JprtSVOf47omRvoaMwTO7EXtRLKbdZyAnRc4U/edit?gid=1179485747 |
| 2 | senza descrizione | catalogato | https://docs.google.com/spreadsheets/d/e/2PACX-1vTVVOEZbXLVQvjIdzGACpZ_IrOWgVDBr_Wa-xULK3191BP9lf1tep-z-PsmcAfaH_aE56j3GHDX_9UO/pubhtml |
| 2 | spreadsheet/checklist | catalogato | https://docs.google.com/spreadsheets/d/e/2PACX-1vTusrkjjQVxfqANVboZbw-VplOUBioFRDcHi5yEz4tXupmNvs9s2MHDBPA0jBzS38Ic9UT6Xulr0Sko/pubhtml |
| 2 | senza descrizione | catalogato | https://docs.google.com/spreadsheets/u/0/d/1bvIx7Q2Lxp7efHRrUh48WkuwirNlKardwSHVz_R8kA0/htmlview |
| 3 | senza descrizione | catalogato | https://docs.google.com/document/d/1Q733nUB-q_1Ao3qTMN_0pjFkwW2NyRXdsZtW9r795SU/edit |
| 3 | Click here to apply! | catalogato | https://docs.google.com/forms/u/0/d/e/1FAIpQLScQPusfkDX9P2IWBKo8KIdBitvjMXn43TFt2DEzHCTTtmHXSw/formResponse |
| 3 | Pokemon Home COMPLETE Living Dex List, Spreadsheet Edition | catalogato | https://docs.google.com/spreadsheets/d/11ov5BCgmdjftGcgtZ49TFglPXJdLBC05OZSLWwSxUMY/edit?usp=sharing |
| 3 | Updated Spreadsheet | catalogato | https://docs.google.com/spreadsheets/d/14W8CAS9SBq3jDuZAl0YncFrrtr8z6RWUGZoqtrKMxFc/edit?usp=sharing |
| 3 | https://docs.google.com/spreadsheets/d/17DXQplJ78ZsBbpMUWVTQSvtsL\_ivug1\_Iv4QBlitq8A/edit?usp=sharing | catalogato | https://docs.google.com/spreadsheets/d/17DXQplJ78ZsBbpMUWVTQSvtsL_ivug1_Iv4QBlitq8A/edit?usp=sharing |
| 3 | https://docs.google.com/spreadsheets/d/1R0H24zZ3MaxQY6IBnsPttUMD4MK4fXeOmcqPNrZJaKM/copy | catalogato | https://docs.google.com/spreadsheets/d/1R0H24zZ3MaxQY6IBnsPttUMD4MK4fXeOmcqPNrZJaKM/copy |
| 3 | completed spreadsheet of Matching Pokéballs | catalogato | https://docs.google.com/spreadsheets/d/1SQYaFkQlNjEhGaJpdpiMT331g2EAqeTojq1xGm-lajs/edit?usp=sharing |
| 3 | senza descrizione | catalogato | https://docs.google.com/spreadsheets/d/1T5RMu189-uMrknJlAPNp3QbQAyp8t0N5/edit?usp=drivesdk&ouid=103067789524497045001&rtpof=true&sd=true |
| 3 | Link to spreadsheet | catalogato | https://docs.google.com/spreadsheets/d/1uV8xqVUqPhyz52aKNzY3VkCg8MG7Lzsdy-FAKVZJzqw/edit |
| 3 | . | catalogato | https://docs.google.com/spreadsheets/u/0/d/1dItpqk-koxZJ3s5mGArWPHo2OGPj3R-Wc_q3bOrTMqg/htmlview |

### youtu.be (37)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | seconds | catalogato | https://youtu.be/1GF_LFPz34U?t=2647 |
| 2 | this video | catalogato | https://youtu.be/63LN2N2usbg |
| 2 | Mario 64 | catalogato | https://youtu.be/7CgXvIuZR40?t=2 |
| 2 | Wishmaker Jirachi | catalogato | https://youtu.be/8neWF6tQBRc |
| 2 | senza descrizione | catalogato | https://youtu.be/9EEnvrmy3vk |
| 2 | this video. | catalogato | https://youtu.be/Bfze_tFEzM4 |
| 2 | https://youtu.be/CmawneiP9L8?si=HVBLQnLEOssLTUlC | catalogato | https://youtu.be/CmawneiP9L8 |
| 2 | this guide | catalogato | https://youtu.be/CzNA5enSzOY |
| 2 | senza descrizione | catalogato | https://youtu.be/D3EvpRHL_vk |
| 2 | senza descrizione | catalogato | https://youtu.be/DdDI53VeGAc |
| 2 | senza descrizione | catalogato | https://youtu.be/HSYtttS0nWI |
| 2 | this video | catalogato | https://youtu.be/IdlKn5oJyxI |
| 2 | here | catalogato | https://youtu.be/PNHZ4xuJH7M |
| 2 | See video guide | catalogato | https://youtu.be/SrZAiR38e6E |
| 2 | Analogue Pocket | catalogato | https://youtu.be/e3SllwKRgMc |
| 2 | 3 beasts | catalogato | https://youtu.be/gjcrMzTGuwk |
| 2 | senza descrizione | catalogato | https://youtu.be/h5Igc18hc2Q |
| 2 | this video guide | catalogato | https://youtu.be/k0HFRpqvSk4 |
| 2 | This might help | catalogato | https://youtu.be/m42a5W7bUYI |
| 2 | senza descrizione | catalogato | https://youtu.be/tIwwBKTLFXw |
| 2 | More info here | catalogato | https://youtu.be/tPFUMRIYT08 |
| 2 | senza descrizione | catalogato | https://youtu.be/yesVqZcnIy0 |
| 3 | senza descrizione | catalogato | https://youtu.be/5uDQLUi0ZEo |
| 3 | Shiny Ditto Trick | catalogato | https://youtu.be/8Lb5pq0y6h8 |
| 3 | it sucks | catalogato | https://youtu.be/BNbXfuTocvU |
| 3 | senza descrizione | catalogato | https://youtu.be/G19RMhvOzbI |
| 3 | This video | catalogato | https://youtu.be/G_D3IIXaoTw |
| 3 | senza descrizione | catalogato | https://youtu.be/JBjSym_lfEs |
| 3 | collegamento del post | catalogato | https://youtu.be/Ld2YphF-HVI |
| 3 | 2 | catalogato | https://youtu.be/TzRL_opOvVM |
| 3 | this video | catalogato | https://youtu.be/UJTneOSkCcg |
| 3 | Video about it | catalogato | https://youtu.be/XyKTeQkzqys?t=115 |
| 3 | How to install | catalogato | https://youtu.be/XyKTeQkzqys?t=629 |
| 3 | Youtube of Crystal_ performing this glitch | catalogato | https://youtu.be/ffZjCabeNr4 |
| 3 | senza descrizione | catalogato | https://youtu.be/iL1PtXHDzFU |
| 3 | It’s even been used to a 43m47s speedrun in Pokémon Gold | catalogato | https://youtu.be/oklw2swIT4w |
| 3 | https://youtu.be/xxyQFPqltiM | catalogato | https://youtu.be/xxyQFPqltiM |

### imgur.com (29)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | You are the fucking man! | catalogato | http://imgur.com/CQlmBLe |
| 2 | IMGUR GUIDE HERE | catalogato | http://imgur.com/a/fzn0c |
| 2 | possible | catalogato | https://imgur.com/HeULTiq |
| 2 | [B | catalogato | https://imgur.com/MU4vusD |
| 2 | senza descrizione | catalogato | https://imgur.com/a/1YAfQGC |
| 2 | result | catalogato | https://imgur.com/a/5mbVq |
| 2 | used | catalogato | https://imgur.com/a/9S6J5 |
| 2 | senza descrizione | catalogato | https://imgur.com/a/F9FMS |
| 2 | https://imgur.com/a/JLwZFcW | catalogato | https://imgur.com/a/JLwZFcW |
| 2 | this image | catalogato | https://imgur.com/a/aT4oB4u |
| 2 | senza descrizione | catalogato | https://imgur.com/a/cuyXcl2 |
| 2 | collegamento del post | catalogato | https://imgur.com/a/jCZjo |
| 3 | legit shiny magikarp | catalogato | http://imgur.com/A6zfset |
| 3 | IMGUR GUIDE HERE | catalogato | http://imgur.com/a/RWaHc |
| 3 | the pride of my pokémon collection | catalogato | http://imgur.com/a/YGFwA |
| 3 | senza descrizione | catalogato | http://imgur.com/a/ZLcpv |
| 3 | senza descrizione | catalogato | http://imgur.com/gallery/8G4fJ |
| 3 | here | catalogato | https://imgur.com/a/3ypWcfh |
| 3 | senza descrizione | catalogato | https://imgur.com/a/F0ra5H7 |
| 3 | senza descrizione | catalogato | https://imgur.com/a/Ons79Zw |
| 3 | I made a quick diagram in paint to show the process | catalogato | https://imgur.com/a/TTubbHF |
| 3 | Imgur mirror in case it gets taken down | catalogato | https://imgur.com/a/YNabu |
| 3 | https://imgur.com/a/bCu6DyK | catalogato | https://imgur.com/a/bCu6DyK |
| 3 | Here | catalogato | https://imgur.com/a/gen-i-map-of-pok-mon-spawnable-with-trainer-fly-glitch-yAZgdND |
| 3 | https://imgur.com/a/tPk8I8n | catalogato | https://imgur.com/a/tPk8I8n |
| 3 | senza descrizione | catalogato | https://imgur.com/gallery/Yk2xt |
| 3 | proof I hatched it tonight | catalogato | https://imgur.com/gallery/bZrGU |
| 3 | here | catalogato | https://imgur.com/gallery/gen-i-chart-of-trainer-fly-glitch-information-OPQlqAE |
| 3 | Daily activities checklist in Pokemon Black 2 & White 2 - Imgur | catalogato | https://imgur.com/jyza4r9 |

### i.redd.it (23)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | collegamento del post | catalogato | https://i.redd.it/06z1325nkkcd1.png |
| 2 | collegamento del post | catalogato | https://i.redd.it/1z8tzc1ks7c61.png |
| 2 | collegamento del post | catalogato | https://i.redd.it/3rmu9k40o6xz.png |
| 2 | Any advice for the battle tree I'm about to give up | catalogato | https://i.redd.it/44lcsdbtnw8c1.jpeg |
| 2 | Updated my overview: Transfer Pokémon from 2002 to 2024 | catalogato | https://i.redd.it/9zh9ucz7c2dc1.png |
| 2 | collegamento del post | catalogato | https://i.redd.it/buu3s1tf1ejh1.png |
| 2 | collegamento del post | catalogato | https://i.redd.it/geqw2xyamtwg1.png |
| 2 | collegamento del post | catalogato | https://i.redd.it/j1gifqqtm05g1.png |
| 2 | collegamento del post | catalogato | https://i.redd.it/n329gxohj08c1.jpeg |
| 2 | collegamento del post | catalogato | https://i.redd.it/n6p7j7u3y7wz.png |
| 2 | collegamento del post | catalogato | https://i.redd.it/soq68t11ovsg1.png |
| 2 | collegamento del post | catalogato | https://i.redd.it/tashtuju1x711.png |
| 2 | collegamento del post | catalogato | https://i.redd.it/zm5mkt70ke7a1.png |
| 3 | collegamento del post | catalogato | https://i.redd.it/3j5vegztr1c91.jpg |
| 3 | collegamento del post | catalogato | https://i.redd.it/4vbh98sq1x711.png |
| 3 | collegamento del post | catalogato | https://i.redd.it/60blf9m4c2dc1.png |
| 3 | collegamento del post | catalogato | https://i.redd.it/6d4rk2bzebkg1.jpeg |
| 3 | collegamento del post | catalogato | https://i.redd.it/7w2t0lz8ahlf1.png |
| 3 | collegamento del post | catalogato | https://i.redd.it/93oog27zod9f1.jpeg |
| 3 | collegamento del post | catalogato | https://i.redd.it/9i3pw569nw0d1.png |
| 3 | collegamento del post | catalogato | https://i.redd.it/9v8cvm83k96f1.png |
| 3 | collegamento del post | catalogato | https://i.redd.it/ge39d5p4m4tc1.jpeg |
| 3 | collegamento del post | catalogato | https://i.redd.it/pd1oktdho4ef1.jpeg |

### gbatemp.net (18)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Game Saves / GBAtemp.net - The Independent Video Game Community | scaricato | https://gbatemp.net/download/categories/game-saves.134 |
| 2 | Game Saves / GBAtemp.net - The Independent Video Game Community | scaricato | https://gbatemp.net/download/categories/game-saves.88 |
| 2 | DeadSkullzJr's NDS(i) Cheat Databases / GBAtemp.net - The Independent Video Game Community | scaricato | https://gbatemp.net/threads/deadskullzjrs-nds-i-cheat-databases.488711 |
| 2 | [NDS] Yet Another nds-bootstrap Forwarder: more than 40 forwarders are now possible / GBAtemp.net - The Independent Video Game Community | scaricato | https://gbatemp.net/threads/nds-yet-another-nds-bootstrap-forwarder-more-than-40-forwarders-are-now-possible.606138 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/3ds-screen-recording-without-a-capture-card-ntr-cfw-method.423445 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/3dshell-multi-purpose-file-manager-for-the-3ds.471503 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/426174 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/609242 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/deadskullzjrs-flashcart-cheat-databases.488711/post-7673924 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/discussion-new-super-ultimate-injector-nsui.500376 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/discussion-new-super-ultimate-injector-nsui.500376/post-9174080 |
| 3 | GameYob DS | non raggiunto | https://gbatemp.net/threads/gameyob-a-gameboy-emulator-for-ds.343407 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/nds-forwarder-cias-for-your-home-menu.426174 |
| 3 | https://gbatemp.net/threads/pokemon-virtual-console-patches-debug-menu-speed-up-full-screen.498833 | non raggiunto | https://gbatemp.net/threads/pokemon-virtual-console-patches-debug-menu-speed-up-full-screen.498833 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/pokemon-virtual-console-patches-debug-menu-speed-up-full-screen.498833/page-2 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/release-godmode9-scripts-megathread.482150/page-10 |
| 3 | Source 1 | non raggiunto | https://gbatemp.net/threads/trading-in-gba-pokemon-games-on-ds.599309 |
| 3 | senza descrizione | non raggiunto | https://gbatemp.net/threads/xy-oras-sm-custom-3d-models-textures-sharing-thread.392711/page-108 |

### projectpokemon.org (15)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | catalogato | https://projectpokemon.org/forums/forums/topic/39841-pokemon-bank-update?page=2 |
| 2 | program on this projectpokemon post | catalogato | https://projectpokemon.org/home/files/file/647-feebas-fishing-spot-finder |
| 2 | senza descrizione | catalogato | https://projectpokemon.org/home/forums/topic/37192-feebas-fishing-spot-value-rusaem |
| 2 | There is an effort to recover | catalogato | https://projectpokemon.org/home/index/announcements/help-awaken-the-pokémon-dream-world-r162 |
| 2 | Add borders to .GB games | catalogato | https://projectpokemon.org/home/tutorials/rom/3ds-pokemon-games-hacking-tutorials/injecting-a-custom-virtual-console-frame-into-an-official-virtual-console-release-r120 |
| 2 | Use Checkpoint | catalogato | https://projectpokemon.org/home/tutorials/save-editing/managing-nds-saves/using-checkpoint-r70 |
| 2 | More Info Here | catalogato | https://projectpokemon.org/home/tutorials/save-editing/using-pkhex/how-to-use-the-batch-editor-in-pkhex-r77 |
| 2 | Legality checking and fixing with PKHeX and RNGReporter | catalogato | https://projectpokemon.org/home/tutorials/save-editing/using-pkhex/pid-mismatch-origin-game-rsefrlg-dppthgss-rngreporter-r31 |
| 3 | senza descrizione | non raggiunto | https://projectpokemon.org/ |
| 3 | PKHeX | non raggiunto | https://projectpokemon.org/home/files/file/1-pkhex |
| 3 | senza descrizione | non raggiunto | https://projectpokemon.org/home/files/file/2107-ohana3ds |
| 3 | senza descrizione | non raggiunto | https://projectpokemon.org/home/forums/forum/83-pkhex |
| 3 | senza descrizione | non raggiunto | https://projectpokemon.org/home/forums/topic/41730-managing-gba-saves-using-gba-backup-tool |
| 3 | this | non raggiunto | https://projectpokemon.org/home/forums/topic/56414-living-form-dex-in-home-checklist |
| 3 | senza descrizione | non raggiunto | https://projectpokemon.org/home/tutorials/save-editing |

### glitchcity.wiki (12)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Time Capsule exploit - Glitch City Wiki | scaricato | https://glitchcity.wiki/Time_Capsule_exploit |
| 2 | senza descrizione | catalogato | https://glitchcity.wiki/wiki/Coin_Case_glitches?oldid=51753 |
| 2 | GlitchDex/GS/255 - Glitch City Wiki | scaricato | https://glitchcity.wiki/wiki/GlitchDex/GS:255 |
| 2 | Guides:Mail Writer Codes - Glitch City Wiki | scaricato | https://glitchcity.wiki/wiki/Guides:Mail_Writer_Codes |
| 2 | Guides:RAM Writer - Glitch City Wiki | scaricato | https://glitchcity.wiki/wiki/Guides:RAM_Writer |
| 2 | Guides:TimoVM's gen 2 ACE setups - Glitch City Wiki | scaricato | https://glitchcity.wiki/wiki/Guides:TimoVM%27s_gen_2_ACE_setups |
| 2 | here\ | fallito | https://glitchcity.wiki/wiki/Main\_Page |
| 3 | senza descrizione | non raggiunto | https://glitchcity.wiki/wiki/GlitchDex/GS/255?oldid=52928 |
| 3 | senza descrizione | non raggiunto | https://glitchcity.wiki/wiki/Guides:Mail_Writer_Codes?oldid=47483 |
| 3 | senza descrizione | non raggiunto | https://glitchcity.wiki/wiki/Guides:RAM_Writer?oldid=47527 |
| 3 | senza descrizione | non raggiunto | https://glitchcity.wiki/wiki/Guides:TimoVM%27s_gen_2_ACE_setups?oldid=51789 |
| 3 | senza descrizione | non raggiunto | https://glitchcity.wiki/wiki/Time_Capsule_exploit?oldid=51684 |

### pastebin.com (10)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Arrange your bag as follows and use 8F:8F x1Any Item xAnyAnt - Pastebin.com | scaricato | http://pastebin.com/MDm58HSq |
| 2 | Mew Farming Setup - Pastebin.com | scaricato | http://pastebin.com/uFTQtwwZ |
| 3 | Pastebin | non raggiunto | http://pastebin.com/4Gp9Esm9 |
| 3 | this list for how to convert it into actual BOX9 code (courtesy of Crystal_) | non raggiunto | http://pastebin.com/4ZDpQXGe |
| 3 | senza descrizione | non raggiunto | http://pastebin.com/5HBY4Adv |
| 3 | senza descrizione | non raggiunto | http://pastebin.com/XVkbu6JL |
| 3 | you need to have these (and only these) items in your own PC item box | non raggiunto | http://pastebin.com/in4MS7zW |
| 3 | senza descrizione | non raggiunto | http://pastebin.com/wpvRzC01 |
| 3 | senza descrizione | non raggiunto | https://pastebin.com/3EdALBrP |
| 3 | https://pastebin.com/hr2vmPCN | non raggiunto | https://pastebin.com/hr2vmPCN |

### discord.gg (9)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | **Discord** | catalogato | https://discord.gg//legendsza |
| 2 | Pokémon Wiimmfi Club | catalogato | https://discord.gg/3D7YvjBrFD |
| 2 | r/PokemonLetsGo Discord | catalogato | https://discord.gg/dErW9Wm |
| 2 | Official Discord Server | catalogato | https://discord.gg/h8ykeMgV3z |
| 2 | Discord link | catalogato | https://discord.gg/t2QeKahNtK |
| 3 | senza descrizione | catalogato | http://discord.gg/JxMZBXy |
| 3 | https://discord.gg/FK3a6DZ | catalogato | https://discord.gg/FK3a6DZ |
| 3 | senza descrizione | catalogato | https://discord.gg/nBnTrv3UMn |
| 3 | senza descrizione | catalogato | https://discord.gg/pMs38vWAx3 |

### drive.google.com (9)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | https://drive.google.com/drive/folders/159W-2Wlo5sPA5DSqHwijdVWuA9z4-qfe | catalogato | https://drive.google.com/drive/folders/159W-2Wlo5sPA5DSqHwijdVWuA9z4-qfe |
| 2 | Battle Pyramid Glitch | catalogato | https://drive.google.com/drive/folders/15RNkGdAzbalwlzwijt1E8SnnMX9lHM8i |
| 2 | https://drive.google.com/drive/u/0/folders/1aBDkBWJbZj-3AYjDCd7K5NG9zCSFP9WT | catalogato | https://drive.google.com/drive/u/0/folders/1aBDkBWJbZj-3AYjDCd7K5NG9zCSFP9WT |
| 2 | https://drive.google.com/file/d/1e3YfLJkwYRn6UYjGAZ-gygqd27DrJyGP/view?usp=sharing | catalogato | https://drive.google.com/file/d/1e3YfLJkwYRn6UYjGAZ-gygqd27DrJyGP/view?usp=sharing |
| 2 | https://drive.google.com/file/d/1gX85mbFEIi7DrQSweJpX\_xWFNtCVwIJR/view?usp=sharing | catalogato | https://drive.google.com/file/d/1gX85mbFEIi7DrQSweJpX_xWFNtCVwIJR/view?usp=sharing |
| 3 | https://drive.google.com/file/d/1-IosLxZV1cVYWU9dyWV0qPTverNZmTk6/view?usp=sharing | catalogato | https://drive.google.com/file/d/1-IosLxZV1cVYWU9dyWV0qPTverNZmTk6/view?usp=sharing |
| 3 | . | catalogato | https://drive.google.com/open?id=16lH2ruXI6sR5w5jmm4vqcPIrYTcpSuhG |
| 3 | . | catalogato | https://drive.google.com/open?id=1LAGxOjbAPv6ppUq5giiRY17ybsUmPyzw |
| 3 | , | catalogato | https://drive.google.com/open?id=1zb60PTOoYWRjnHdmvTYEbNQlbktK_y4v |

### smogon.com (9)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Gen III Battle Frontier Discussion and Records / Smogon Forums | scaricato | https://www.smogon.com/forums/threads/gen-iii-battle-frontier-discussion-and-records.3648697 |
| 2 | Metagame - LGPE OverUsed / Smogon Forums | scaricato | https://www.smogon.com/forums/threads/lgpe-overused.3644015 |
| 2 | Shiny Hunting in Pokémon Sword and Shield - Smogon University | scaricato | https://www.smogon.com/ingame/guides/swsh_shiny_hunt |
| 3 | senza descrizione | non raggiunto | http://www.smogon.com/forums/threads/breeding-rng-quirk.3589338 |
| 3 | senza descrizione | non raggiunto | https://www.smogon.com/forums/threads/battle-tree-discussion-and-records.3587215 |
| 3 | senza descrizione | non raggiunto | https://www.smogon.com/forums/threads/dans-macabre-a-record-breaking-gen-3-battle-tower-singles-team.3651964 |
| 3 | senza descrizione | non raggiunto | https://www.smogon.com/forums/threads/emerald-battle-frontier-guide-please-help-developing.3579762/post-7800197 |
| 3 | senza descrizione | non raggiunto | https://www.smogon.com/forums/threads/lgpe-little-cup.3645797 |
| 3 | senza descrizione | non raggiunto | https://www.smogon.com/ingame/rng/dpphgss_rng_part5 |

### gamebrew.org (8)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 3DShell - GameBrew | scaricato | https://www.gamebrew.org/wiki/3DShell |
| 2 | New Super Ultimate Injector 3DS - GameBrew | scaricato | https://www.gamebrew.org/wiki/New_Super_Ultimate_Injector_3DS |
| 2 | PKHeX 3DS - GameBrew | scaricato | https://www.gamebrew.org/wiki/PKHeX_3DS |
| 2 | PKSM 3DS - GameBrew | scaricato | https://www.gamebrew.org/wiki/PKSM_3DS |
| 3 | senza descrizione | non raggiunto | https://www.gamebrew.org/index.php?title=3DShell&oldid=191635 |
| 3 | senza descrizione | non raggiunto | https://www.gamebrew.org/index.php?title=New_Super_Ultimate_Injector_3DS&oldid=154359 |
| 3 | senza descrizione | non raggiunto | https://www.gamebrew.org/index.php?title=PKHeX_3DS&oldid=209501 |
| 3 | senza descrizione | non raggiunto | https://www.gamebrew.org/index.php?title=PKSM_3DS&oldid=209458 |

### mtheall.com (7)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://mtheall.com/~mtheall/ftpd-classic.3dsx |
| 3 | senza descrizione | non raggiunto | https://mtheall.com/~mtheall/ftpd-classic.cia |
| 3 | senza descrizione | non raggiunto | https://mtheall.com/~mtheall/ftpd-classic.nro |
| 3 | senza descrizione | non raggiunto | https://mtheall.com/~mtheall/ftpd.3dsx |
| 3 | senza descrizione | non raggiunto | https://mtheall.com/~mtheall/ftpd.cia |
| 3 | senza descrizione | non raggiunto | https://mtheall.com/~mtheall/ftpd.nds |
| 3 | senza descrizione | non raggiunto | https://mtheall.com/~mtheall/ftpd.nro |

### twitter.com (7)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | https://twitter.com/JoeMerrick/status/1228055915573710849 | catalogato | https://twitter.com/JoeMerrick/status/1228055915573710849 |
| 2 | https://twitter.com/JoeMerrick/status/1664958038657187842 | catalogato | https://twitter.com/JoeMerrick/status/1664958038657187842 |
| 2 | Link | catalogato | https://twitter.com/REVERSALx7/status/1463350315579842563?t=qbnAE0Mh82ztKbZ1hz8uQQ&s=19 |
| 2 | senza descrizione | catalogato | https://twitter.com/riiconnect24/status/1583996519325147137?s=46&t=zixZJ1jNdh4EIWdujbBRGg |
| 3 | determined by the experience it has | catalogato | https://twitter.com/TheMantyke/status/824138136129339392 |
| 3 | the RNG abuse method is released | catalogato | https://twitter.com/pokemon_PhD/status/809313886117695488 |
| 3 | RNG Reporter | catalogato | https://twitter.com/pokemon_PhD/status/809906064649048065 |

### x.com (7)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | https://x.com/Sibuna\_Switch/status/1462473371917111303 | catalogato | https://x.com/Sibuna_Switch/status/1462473371917111303 |
| 2 | this | catalogato | https://x.com/Sibuna_Switch/status/1492970750264979456 |
| 2 | senza descrizione | catalogato | https://x.com/Sibuna_Switch/status/1495426743343194117 |
| 2 | here | catalogato | https://x.com/Sibuna_Switch/status/1538721002645073920 |
| 2 | https://x.com/Sibuna\_Switch/status/1768100276399968414?lang=en | catalogato | https://x.com/Sibuna_Switch/status/1768100276399968414?lang=en |
| 2 | Misty mark in SV | catalogato | https://x.com/Sibuna_Switch/status/1930459094202163632 |
| 3 | senza descrizione | catalogato | https://x.com/lewchube/status/1510382980132442113 |

### en.wikipedia.org (6)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | buffer overflow | catalogato | https://en.wikipedia.org/wiki/Buffer_overflow |
| 2 | game cart with IR | catalogato | https://en.wikipedia.org/wiki/Nintendo_Game_Card |
| 2 | program counter | catalogato | https://en.wikipedia.org/wiki/Program_counter |
| 3 | list | non raggiunto | https://en.wikipedia.org/wiki/Game_Boy_Advance_Wireless_Adapter |
| 3 | gaming the system | non raggiunto | https://en.wikipedia.org/wiki/Gaming_the_system |
| 3 | Here is the list of NA VC games | non raggiunto | https://en.wikipedia.org/wiki/List_of_Virtual_Console_games_for_Nintendo_3DS_(North_America |

### forums.glitchcity.info (6)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | catalogato | http://forums.glitchcity.info/index.php?board=11.0 |
| 2 | senza descrizione | catalogato | http://forums.glitchcity.info/index.php?topic=6638.0 |
| 2 | Link to Code Post | catalogato | http://forums.glitchcity.info/index.php?topic=6638.15 |
| 2 | Link to Code Post | catalogato | http://forums.glitchcity.info/index.php?topic=6638.msg200226.html |
| 3 | Glitchcity research thread | non raggiunto | http://forums.glitchcity.info/index.php/topic,6716.0.html |
| 3 | this guide | non raggiunto | http://forums.glitchcity.info/index.php?topic=6638.msg198625.html |

### 3ds.hacks.guide (5)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 3DS Hacks Guide | scaricato | http://3ds.hacks.guide/ |
| 2 | Dumping Titles and Game Cartridges / 3DS Hacks Guide | scaricato | https://3ds.hacks.guide/dumping-titles-and-game-cartridges |
| 2 | Dumping Titles and Game Cartridges / 3DS Hacks Guide | scaricato | https://3ds.hacks.guide/dumping-titles-and-game-cartridges.html |
| 2 | GodMode9 Usage / 3DS Hacks Guide | scaricato | https://3ds.hacks.guide/godmode9-usage |
| 2 | Key Information / 3DS Hacks Guide | scaricato | https://3ds.hacks.guide/key-information.html |

### en-americas-support.nintendo.com (5)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | How to Create a Nintendo Network ID on Nintendo 3DS / Nintendo Support | scaricato | https://en-americas-support.nintendo.com/app/answers/detail/a_id/2221/~/how-to-create-a-nintendo-network-id-on-nintendo-3ds |
| 2 | Compatible Wireless Modes and Wireless Security Types / Nintendo Support | scaricato | https://en-americas-support.nintendo.com/app/answers/detail/a_id/498/~/compatible-wireless-modes-and-wireless-security-types |
| 2 | Announcement of Discontinuation of Online Services for Nintendo 3DS and Wii U software / Nintendo Support | scaricato | https://en-americas-support.nintendo.com/app/answers/detail/a_id/63227 |
| 2 | Announcement of Discontinuation of Online Services for Nintendo 3DS and Wii U software / Nintendo Support | scaricato | https://en-americas-support.nintendo.com/app/answers/detail/a_id/63227/~/announcement-of-discontinuation-of-online-services-for-nintendo-3ds-and-wii-u |
| 3 | Nintendo's servers for Bank still work. They were never closed. | non raggiunto | https://en-americas-support.nintendo.com/app/answers/detail/a_id/61543/~/pok%C3%A9mon-bank-service-update |

### m.bulbapedia.bulbagarden.net (5)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Experience Group | catalogato | https://m.bulbapedia.bulbagarden.net/wiki/Category:Pok%C3%A9mon_in_the_Medium_Slow_experience_group |
| 2 | Diamond Storm | catalogato | https://m.bulbapedia.bulbagarden.net/wiki/Diamond_Storm_(move |
| 2 | senza descrizione | catalogato | https://m.bulbapedia.bulbagarden.net/wiki/Distribution_device |
| 2 | senza descrizione | catalogato | https://m.bulbapedia.bulbagarden.net/wiki/List_of_Wi-Fi_English_event_Pok%C3%A9mon_distributions_(Generation_IV |
| 3 | Bulbapedia | non raggiunto | https://m.bulbapedia.bulbagarden.net/wiki/List_of_Battle_Maison_Trainers |

### pokepast.es (5)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | this | catalogato | https://pokepast.es/e98bb534818c8ec3 |
| 3 | senza descrizione | non raggiunto | https://pokepast.es/1dd2ea15178a1758 |
| 3 | senza descrizione | non raggiunto | https://pokepast.es/219b988b78930fea |
| 3 | senza descrizione | non raggiunto | https://pokepast.es/74628316023deccd |
| 3 | senza descrizione | non raggiunto | https://pokepast.es/bd2463a0228eb753 |

### extratricky.com (4)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | on this tile | non raggiunto | https://www.extratricky.com/pokeworld/rb/1 |
| 3 | 100 coins here | non raggiunto | https://www.extratricky.com/pokeworld/rb/135 |
| 3 | the man at the top left of the hotel | non raggiunto | https://www.extratricky.com/pokeworld/rb/138 |
| 3 | in front of the first trainer, leaving a gap | non raggiunto | https://www.extratricky.com/pokeworld/rb/177 |

### gamefaqs.gamespot.com (4)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | https://gamefaqs.gamespot.com/boards/259372-pokemon-sword/78401974 | fallito | https://gamefaqs.gamespot.com/boards/259372-pokemon-sword/78401974 |
| 2 | this very helpful GameFAQs Thread | fallito | https://gamefaqs.gamespot.com/boards/359434-pokemon-violet/80618645 |
| 2 | GameFAQ's "False Swipe on Breeloom" Guide | fallito | https://gamefaqs.gamespot.com/gba/921905-pokemon-emerald-version/answers/558964-how-to-make-breloom-learn-false-swipe-in-pokemon-emerald- |
| 3 | Source 2 | non raggiunto | https://gamefaqs.gamespot.com/gba/918915-pokemon-firered-version/answers/127512-how-do-i-trade-between-firered-and-leafgreen-with-2-dss |

### glitchcity.info (4)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | link | non raggiunto | http://glitchcity.info/biglist.htm |
| 3 | senza descrizione | non raggiunto | http://glitchcity.info/wiki/Arbitrary%20code%20execution |
| 3 | recommends | non raggiunto | http://glitchcity.info/wiki/Arbitrary_code_execution |
| 3 | this list | non raggiunto | http://glitchcity.info/wiki/The_Big_HEX_List |

### sites.google.com (4)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | PokemonSlots | scaricato | https://sites.google.com/site/pokemonslots |
| 2 | PokemonSlots - Gen V | scaricato | https://sites.google.com/site/pokemonslots/gen-v?authuser=0 |
| 2 | Athis' Ribbon Handbook | scaricato | https://sites.google.com/view/athis-ribbon-handbook |
| 2 | Athis' Ribbon Handbook | scaricato | https://sites.google.com/view/athis-ribbon-handbook/home |

### datacrystal.romhacking.net (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | This Pokémon GS RAM Map | non raggiunto | http://datacrystal.romhacking.net/wiki/Pok%C3%A9mon_Gold:RAM_map |
| 3 | RAM Map | non raggiunto | http://datacrystal.romhacking.net/wiki/Pokémon_Red/Blue:RAM_map |
| 3 | ROM Map | non raggiunto | http://datacrystal.romhacking.net/wiki/Pokémon_Red_and_Blue:ROM_map |

### dragonflycave.com (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Main / The Cave of Dragonflies | scaricato | http://www.dragonflycave.com/ |
| 2 | Gen II Catch Rate Calculator / The Cave of Dragonflies | scaricato | https://www.dragonflycave.com/calculators/gen-ii-catch-rate |
| 2 | Gen III/IV Catch Rate Calculator / The Cave of Dragonflies | scaricato | https://www.dragonflycave.com/calculators/gen-iii-iv-catch-rate |

### gist.github.com (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | fallito | https://gist.github.com/claydolwithexplosion/017f1784deebcd118b61d3ad917edb3c.js&quot;&gt;&lt;/script&gt |
| 3 | https://gist.github.com/Bl4ckSh4rk/256ed3b857c9677310837d5180121f35 | non raggiunto | https://gist.github.com/Bl4ckSh4rk/256ed3b857c9677310837d5180121f35 |
| 3 | How to add rom hacks to 3DS games | non raggiunto | https://gist.github.com/figgyc/0d31b77fc6e4e8f9a49399d392740d46 |

### ibb.co (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | catalogato | https://ibb.co/LNWjPMT |
| 2 | senza descrizione | catalogato | https://ibb.co/mJRnpz2 |
| 2 | senza descrizione | catalogato | https://ibb.co/v4q9nFL |

### imgs.xkcd.com (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Image | catalogato | http://imgs.xkcd.com/comics/exploits_of_a_mom.png |
| 3 | senza descrizione | catalogato | https://imgs.xkcd.com/comics/exploits_of_a_mom.png |
| 3 | senza descrizione | catalogato | https://imgs.xkcd.com/comics/semaphore.png |

### lyra-made-a.website (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Lyra's Living Dex Guide | catalogato | https://lyra-made-a.website/pokemon_gen1/full_guide |
| 2 | Lyra's Gen 2 Living Dex Guide | catalogato | https://lyra-made-a.website/pokemon_gen2/full_guide |
| 2 | Lyra's Gen 3 Living Dex Guide | catalogato | https://lyra-made-a.website/pokemon_gen3/full_guide |

### np.reddit.com (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Info | catalogato | https://np.reddit.com/r/SubtleTV/wiki/mentioned_videos |
| 2 | top posts | catalogato | https://np.reddit.com/r/pokemonribbons/top?sort=top&t=year |
| 2 | Info | catalogato | https://np.reddit.com/r/sneakpeekbot |

### twitch.tv (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | the VOD itself | catalogato | https://www.twitch.tv/videos/117651897 |
| 3 | Twitch | non raggiunto | https://twitch.tv/Pokemon |
| 3 | starting from 17:05 in the video | non raggiunto | https://www.twitch.tv/videos/117651897?t=17m05s |

### wiki.gbatemp.net (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | GBARunner2/Link - WikiTemp, the GBAtemp wiki | scaricato | https://wiki.gbatemp.net/wiki/GBARunner2/Link |
| 3 | senza descrizione | non raggiunto | https://wiki.gbatemp.net/w/index.php?title=GBARunner2%2FLink&oldid=73221 |
| 3 | This is the compatibility list | non raggiunto | https://wiki.gbatemp.net/wiki/DaedalusX64_3DS_Compatibility_List |

### wolframalpha.com (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | **2023-10-19 22:25:31 UTC** | catalogato | http://www.wolframalpha.com/input?i=2023-10-19+22%3A25%3A31+UTC+To+Local+Time |
| 2 | **2024-02-20 22:35:28 UTC** | catalogato | http://www.wolframalpha.com/input?i=2024-02-20+22%3A35%3A28+UTC+To+Local+Time |
| 3 | **2026-09-05 05:33:38 UTC** | non raggiunto | http://www.wolframalpha.com/input?i=2026-09-05+05%3A33%3A38+UTC+To+Local+Time |

### xkcd.com (3)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | xkcd: Semaphore | scaricato | https://www.xkcd.com/ |
| 2 | xkcd: Exploits of a Mom | scaricato | https://xkcd.com/327 |
| 3 | senza descrizione | non raggiunto | https://xkcd.com/3295 |

### 0.0.0.0 (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 0.0.0.0 | catalogato | http://0.0.0.0/ |
| 2 | 0.0.0.0 | catalogato | https://0.0.0.0/ |

### 1.1.1.1 (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 1.1.1.1 — The free app that makes your Internet faster. | scaricato | http://1.1.1.1/ |
| 2 | 1.1.1.1 — The free app that makes your Internet faster. | scaricato | https://1.1.1.1/ |

### 164.132.44.106 (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 164.132.44.106 | catalogato | http://164.132.44.106/ |
| 2 | 164.132.44.106 | catalogato | https://164.132.44.106/ |

### 167.86.108.126 (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 167.86.108.126 | catalogato | http://167.86.108.126/ |
| 2 | 167.86.108.126 | catalogato | https://167.86.108.126/ |

### 172.104.88.237 (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 172.104.88.237 | catalogato | http://172.104.88.237/ |
| 2 | 172.104.88.237 | catalogato | https://172.104.88.237/ |

### 178.62.43.212 (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | **178.62.43.212** | catalogato | http://178.62.43.212/ |
| 2 | 178.62.43.212 | catalogato | https://178.62.43.212/ |

### 8.8.8.8 (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 8.8.8.8 | fallito | http://8.8.8.8/ |
| 2 | `8.8.8.8` | catalogato | https://8.8.8.8/ |

### altissimo1.github.io (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Alabaster Icelands Pokémon Map | scaricato | https://altissimo1.github.io/Supplementary-Series/Legends/Legends-Arceus/Pokemon/icelands.html |
| 2 | Pokémon Maps Home | scaricato | https://altissimo1.github.io/Supplementary-Series/Legends/Legends-Arceus/Pokemon/index.html |

### archives.glitchcity.info (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Battle Tower Glitch | catalogato | https://archives.glitchcity.info/forums/board-109/thread-7016/page-0.html |
| 3 | here's the archived ID list. | non raggiunto | https://archives.glitchcity.info/wiki/The_Big_HEX_List.html |

### bepis.io (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Pokémon Platinum National Dex Guide | scaricato | https://bepis.io/pokemon |
| 2 | Pokémon Platinum National Dex Guide | scaricato | https://bepis.io/pokemon/wild.html |

### cdn.discordapp.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Completely the same as the OG | catalogato | https://cdn.discordapp.com/attachments/907741323757506590/908875821769449472/2021111219280400-7DCC42E2AF4C1BBE54BB71700F7161B6.jpg |
| 3 | shiny Starly | catalogato | https://cdn.discordapp.com/attachments/907741323757506590/908898581681950720/2021111220582900-7DCC42E2AF4C1BBE54BB71700F7161B6.jpg |

### digiex.net (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 3DS GBA Save Backup and Restore with GodMode9 / Digiex | scaricato | https://digiex.net/threads/3ds-gba-save-backup-and-restore-with-godmode9.15395 |
| 3 | BW-tool | non raggiunto | https://digiex.net/threads/pokemon-black-white-1-2-save-tool-global-link-arceus-entralink-editor-medals-join-avenue.15061 |

### explainxkcd.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 327: Exploits of a Mom - explain xkcd | scaricato | https://www.explainxkcd.com/wiki/index.php/327 |
| 3 | senza descrizione | non raggiunto | https://www.explainxkcd.com/w/index.php?title=327%3A_Exploits_of_a_Mom&oldid=197752 |

### ezgif.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | PNG Image Compressor | scaricato | https://ezgif.com/optipng |
| 2 | https://ezgif.com/resize | scaricato | https://ezgif.com/resize |

### gamefaqs.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | here | fallito | http://www.gamefaqs.com/gameboy/198314-pokemon-yellow-version-special-pikachu-edition/faqs/27916 |
| 3 | Time Machine Breeding Method | non raggiunto | http://www.gamefaqs.com/boards/696959-pokemon-x/67960441 |

### inject.sigkill.tech (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | convert .SAV files to VC save files here | catalogato | https://inject.sigkill.tech/converter/3dsvc |
| 3 | convert .SAV files to VC save files | non raggiunto | https://inject.sigkill.tech/vc-save |

### mega.nz (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | Mega | non raggiunto | https://mega.nz/file/5YZE0b5T |
| 3 | senza descrizione | non raggiunto | https://mega.nz/folder/UNwxET6K |

### mgba.io (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | mGBA 0.9.0 - mGBA | scaricato | https://mgba.io/2021/03/28/mgba-0.9.0 |
| 3 | #190 | non raggiunto | https://mgba.io/i/190 |

### nintendo.co.uk (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Iwata Asks / 1. Just Making The Last Train / Iwata Asks - Pokémon HeartGold Version & SoulSilver Version / Nintendo UK | scaricato | https://www.nintendo.co.uk/Iwata-Asks/Iwata-Asks-Pokemon-HeartGold-Version-SoulSilver-Version/Iwata-Asks-Pokemon-HeartGold-Version-SoulSilver-Version/1-Just-Making-The-Last-Train/1-Just-Making-The-Last-Train-225842.html |
| 3 | senza descrizione | non raggiunto | https://www.nintendo.co.uk/en-gb/-225842.html&original_referer=https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Pokemon-HeartGold-Version-SoulSilver-Version/Iwata-Asks-Pokemon-HeartGold-Version-SoulSilver-Version/1-Just-Making-The-Last-Train/1-Just-Making-The-Last-Train-225842.html&source=tweetbutton&text=Iwata+Asks+-+Pokémon+HeartGold+Version+&+SoulSilver+Version&via=NintendoUK |

### nintendo.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Pokemon-HeartGold-Version-SoulSilver-Version/Iwata-Asks-Pokemon-HeartGold-Version-SoulSilver-Version/1-Just-Making-The-Last-Train/1-Just-Making-The-Last-Train-225842.html |
| 3 | senza descrizione | non raggiunto | https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Pokemon-HeartGold-Version-SoulSilver-Version/Iwata-Asks-Pokemon-HeartGold-Version-SoulSilver-Version/1-Just-Making-The-Last-Train/1-Just-Making-The-Last-Train-225842.html&original_referer=https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Pokemon-HeartGold-Version-SoulSilver-Version/Iwata-Asks-Pokemon-HeartGold-Version-SoulSilver-Version/1-Just-Making-The-Last-Train/1-Just-Making-The-Last-Train-225842.html&source=tweetbutton&text=Iwata+Asks+-+Pokémon+HeartGold+Version+&+SoulSilver+Version&via=NintendoUK |

### pbs.twimg.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Meaning there's more space for you to fail and break your chain even if you are following the rules, unlike before | catalogato | https://pbs.twimg.com/media/FEHhugrVkAA93od?format=png&name=360x360 |
| 2 | Papa Jefe’s 3-ingredient sandwiches | catalogato | https://pbs.twimg.com/media/FiigD-DWIAQViNI?format=jpg&name=medium |

### pokemon.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Pokémon Bank Services Will Be Available at No Cost to Players | scaricato | https://www.pokemon.com/us/pokemon-news/pokemon-bank-services-will-be-available-at-no-cost-to-players |
| 2 | Pokémon.com | fallito | https://www.pokemon.com/us/strategy/gigantamax-shiny-pokemon-sword-pokemon-shield-wild-area?cid=&amp%3Bamp%3Bamp%3Butm_source=tw&amp%3Bamp%3Bamp%3Butm_medium=social&amp%3Bamp%3Bamp%3Butm_campaign=swordshield&amp%3Bamp%3Bamp%3Butm_term=wildareaguide |

### pokemondb.net (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://pokemondb.net/ |
| 3 | here | non raggiunto | https://pokemondb.net/pokebase/99090/what-are-all-the-berries-you-can-possibly-get-in-black-2 |

### problemkaputt.de (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | http://problemkaputt.de/gbatek.htm |
| 3 | senza descrizione | non raggiunto | https://problemkaputt.de/gbatek.htm |

### raw.githubusercontent.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Source | scaricato | https://raw.githubusercontent.com/wiki/FlagBrew/PKSM/Built-In-Scripts.md |
| 3 | senza descrizione | non raggiunto | https://raw.githubusercontent.com/RiiConnect24/DNS-Server/master/dns_zones-hosts.txt |

### scontent-lhr3-1.xx.fbcdn.net (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | catalogato | https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/15940978_1883267241904863_4393868519816564903_n.jpg?oh=fe6b4c9bc9db5d56d37980e2d5136287&oe=58DD9CB9 |
| 3 | senza descrizione | catalogato | https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/16002849_1590518517630714_1630673376565328564_n.jpg?oh=c85275692d72c09026c831b70eabf57b&oe=59244C20 |

### stratospherix.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://www.stratospherix.com/products/filebrowser |
| 3 | senza descrizione | non raggiunto | https://www.stratospherix.com/setupvpn |

### subtletv.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Play All | catalogato | http://subtletv.com/_r5q4meg?ftrlnk=1 |
| 2 | Watch Playlist &#9654; | catalogato | http://subtletv.com/_r5q4meg?nline=1 |

### support.nintendo.com (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Nintendo Customer Support Region Selector - Official Site | scaricato | http://support.nintendo.com/ |
| 3 | senza descrizione | non raggiunto | http://support.nintendo.com/servicesupdate |

### v.redd.it (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | collegamento del post | catalogato | https://v.redd.it/lg0upuoiil191 |
| 3 | collegamento del post | catalogato | https://v.redd.it/mvbczpu4g9z71 |

### wiki.hacks.guide (2)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | see this guide | fallito | https://wiki.hacks.guide/wiki/3DS:Randomizing_Pokémon |
| 2 | 3DS Games - Remove Outlines | fallito | https://wiki.hacks.guide/wiki/3DS:Remove_outlines_in_Pokémon_games |

### 001.001.001.001 (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 001.001.001.001 | catalogato | http://001.001.001.001/ |

### 167.235.229.36 (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 167.235.229.36 | catalogato | http://167.235.229.36/ |

### 178.062.043.212 (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 178.062.043.212 | catalogato | http://178.062.043.212/ |

### 37.97.147.73 (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | LINK | catalogato | http://37.97.147.73/Headbutt%20Grid.htm |

### 3ds.eiphax.tech (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | PKHeX Desktop App | catalogato | https://3ds.eiphax.tech/pkhex |

### 3ds.guide (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | https://3ds.guide/ | non raggiunto | https://3ds.guide/ |

### 3ds.pokemon-gl.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | https://3ds.pokemon-gl.com/ | non raggiunto | https://3ds.pokemon-gl.com/ |

### 8.8.4.4 (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | `8.8.4.4` | catalogato | https://8.8.4.4/ |

### addons.mozilla.org (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Mentioned Videos for Reddit – Get this Extension for 🦊 Firefox (en-US) | scaricato | https://addons.mozilla.org/en-US/firefox/addon/mentioned-videos-for-reddit |

### amiibo.life (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | There are no mainline Pokémon games with Amiibo support | non raggiunto | https://amiibo.life/games |

### angelfire.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | DV Method | catalogato | https://www.angelfire.com/pokemon2/dv-info/shinies.html |

### apps.apple.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | ‎FileBrowser: Documents Manager App - App Store | scaricato | https://apps.apple.com/us/app/filebrowser-document-manager/id364738545 |

### archive.nyafuu.org (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | The hunt started | non raggiunto | https://archive.nyafuu.org/vp/thread/30676572 |

### archive.org (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | scan the QR codes | non raggiunto | https://archive.org/download/3ds-cia-qr-code |

### archives.bulbagarden.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | nightmare fuel | catalogato | https://archives.bulbagarden.net/wiki/Category:Red_and_Green_sprites |

### base64.guru (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Hex to Base64 / Base64 Encode / Base64 Converter / Base64 | scaricato | https://base64.guru/converter/encode/hex |

### bear.ces.cwru.edu (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | catalogato | http://bear.ces.cwru.edu/eecs_382/ARM7-TDMI-manual-pt3.pdf |

### billspc.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | BillsPC.com | non raggiunto | http://billspc.com/ |

### binance.bh (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://www.binance.bh/futures/ref?code=IHJUI7TF |

### binaryhexconverter.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | A Decimal to Hexadecimal converter | non raggiunto | http://www.binaryhexconverter.com/decimal-to-hex-converter |

### bluemoonfalls.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Time Changing Passcode Generator - Blue Moon Falls | scaricato | https://bluemoonfalls.com/pages/tools/time-passcode-generator |

### bobby-tables.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | http://bobby-tables.com/ |

### bulbagarden.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://www.bulbagarden.net/ |

### cantsay.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://cantsay.github.io/ |

### cdn.bulbagarden.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | this instead | catalogato | https://cdn.bulbagarden.net/upload/archive/7/70/20140517072647%21Ilex_Forest_GSC.png |

### cfwaifu.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | 3DS Game Cheats with Checkpoint (Sharkive) - CFWaifu | scaricato | https://www.cfwaifu.com/3ds-cheats |

### chrome.google.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Chrome | catalogato | https://chrome.google.com/webstore/detail/mentioned-videos-for-redd/fiimkmdalmgffhibfdjnhljpnigcmohf |

### classic.pokepc.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | catalogato | https://classic.pokepc.net/apps/livingdex |

### code.google.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | IR-GTS | catalogato | https://code.google.com/archive/p/ir-gts |

### cultivatenation.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | https://cultivatenation.com | non raggiunto | https://cultivatenation.com/ |

### davidgf.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://www.davidgf.net/2024/01/13/gba-wireless-adapter |

### degraiver.deviantart.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | catalogato | http://degraiver.deviantart.com/art/Pkmn-RBY-Stat-Calculator-V-0-9-82964356 |

### devkitpro.org (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://devkitpro.org/wiki/devkitPro_pacman |

### dexerto.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | https://www.dexerto.com/pokemon/pokemon-home-players-report-bizarre-magearna-pokedex-gift-bug-1328506 | non raggiunto | https://www.dexerto.com/pokemon/pokemon-home-players-report-bizarre-magearna-pokedex-gift-bug-1328506 |

### discord.kaeru.world (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://discord.kaeru.world/ |

### draw.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | draw.io | catalogato | http://draw.io/ |

### dropbox.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | this file | non raggiunto | https://www.dropbox.com/s/rzwr0ycdml3akk9/ntr_launcher.ini?dl=1 |

### ecs.csun.edu (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | catalogato | https://www.ecs.csun.edu/~smirzaei/docs/ece425/arm7tdmi_instruction_set_reference.pdf |

### eduatec-my.sharepoint.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | https://eduatec-my.sharepoint.com/:x:/g/personal/tiago\_cristo\_t0104843\_edu\_atec\_pt/EeQCiXq1X-hMkf8Bt\_y8HiIBWYD7J-ZChc2xjPx-IlS4VQ?e=69O49b | non raggiunto | https://eduatec-my.sharepoint.com/:x:/g/personal/tiago_cristo_t0104843_edu_atec_pt/EeQCiXq1X-hMkf8Bt_y8HiIBWYD7J-ZChc2xjPx-IlS4VQ?e=69O49b |

### emulation.gametechwiki.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | e-Reader Emulators | fallito | https://emulation.gametechwiki.com/index.php/GBA_e-Reader_emulators |

### en.m.wikipedia.org (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | Taiyaki | non raggiunto | https://en.m.wikipedia.org/wiki/Taiyaki |

### epilogue.co (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Play and manage Game Boy cartridges on your PC / GB Operator | scaricato | https://www.epilogue.co/product/gb-operator |

### exelotl.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | patched/converted | catalogato | https://exelotl.github.io/gba-eeprom-save-fix |

### feuniverse.us (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Rip a ROM from a cartridge via a DS, DS Lite, or GameCube | catalogato | https://feuniverse.us/t/dumping-roms-from-gba-cartridges-a-primer/3667 |

### filecenter.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://www.filecenter.com/blog/how-to-unzip-files-mac-iphone-android-windows |

### flagbrew.org (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://flagbrew.org/ |

### forms.gle (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | Click here to apply! | non raggiunto | https://forms.gle/xPPYT4sa4ZL55gt47 |

### forums.serenesforest.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | https://forums.serenesforest.net/topic/63781-gen-1-to-gen-2-gender-mechanics-regarding-trading/ | fallito | https://forums.serenesforest.net/topic/63781-gen-1-to-gen-2-gender-mechanics-regarding-trading |

### foryourinebriation.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | And delicious | catalogato | http://www.foryourinebriation.com/uploads/1/5/5/3/15536798/220954881.png?356= |

### gamerbymistake.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | How to Transfer Pokemon from Game Boy to Pokemon Home: Step-by-Step Guide - Gamer by mistake | scaricato | https://www.gamerbymistake.com/2023/06/how-to-transfer-pokemon-from-game-boy-to-pokemon-home.html |

### gamerguides.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | Black 2 and White 2 - Introduction - Intro and Gameplay / Pokémon: Black & White 2 / Gamer Guides® | non raggiunto | https://www.gamerguides.com/pokemon-black-white-2/guide |

### gaming.stackexchange.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | https://gaming.stackexchange.com/questions/294147/what-determines-the-gender-of-a-gen-1-pokemon | catalogato | https://gaming.stackexchange.com/questions/294147/what-determines-the-gender-of-a-gen-1-pokemon |

### gamingintel.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | one | fallito | https://gamingintel.com/how-to-increase-shiny-odds-in-pokemon-scarlet-violet |

### ghosteshop.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | Ghost eShop | non raggiunto | https://ghosteshop.com/ |

### global3.memecdn.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | catalogato | http://global3.memecdn.com/i-have-no-idea-what-im-doing_gp_865021.jpg |

### goo.gl (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | fallito | https://goo.gl/sPjdLp |

### gyazo.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://gyazo.com/7fc291f31533729c2b82cc7e66e37d52 |

### houssemamor.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Emerald ACE Generator (Web) | scaricato | https://houssemamor.github.io/Emerald-Stable-ACE |

### hq.porygon.co (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | here | non raggiunto | https://hq.porygon.co/ |

### hshop.erista.me (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | H Shop | non raggiunto | https://hshop.erista.me/ |

### i-made-a.website (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Lyra's Living Dex Guide | catalogato | https://i-made-a.website/ |

### i1.kym-cdn.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | catalogato | http://i1.kym-cdn.com/photos/images/original/001/070/953/1da.jpeg |

### is.4chan.org (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | catalogato | http://is.4chan.org/vp/1481893195109.png |

### kaeru.world (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Kaeru WFC - Kaeru Team | scaricato | https://kaeru.world/projects/wfc |

### kotaku.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | essentially unusable | non raggiunto | https://kotaku.com/a-lone-hacker-has-been-terrorizing-pokemon-fans-trying-1848144461 |

### kyraminol.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://kyraminol.github.io/3DSync |

### legendarypkmn.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Pokémon G/S Password Generator / LegendaryPKMN | scaricato | https://legendarypkmn.net/pass |

### linksharing.samsungcloud.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | catalogato | https://linksharing.samsungcloud.com/czNRSK1nNfFI |

### m.imgur.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | catalogato | http://m.imgur.com/HBb2Zzd,hFCCRWd,FS7VYSA,IzvZClq,a0cl6AS,4gbkU6e,JNAv85o |

### m.xkcd.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | xkcd: Exploits of a Mom | scaricato | https://m.xkcd.com/327 |

### marcrobledo.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Rom Patcher JS | scaricato | https://www.marcrobledo.com/RomPatcher.js |

### melonds.kuribo64.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | https://melonds.kuribo64.net/ | non raggiunto | https://melonds.kuribo64.net/ |

### mobile.twitter.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | No thanks😂 ive netted up to 3-4 shinies per sandwich with this method | catalogato | https://mobile.twitter.com/SilentDestroySR/status/1596430687091167235/photo/1 |

### mrnbayoh.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Pokemon 6G Chain Fishing Probability Analysis | scaricato | https://mrnbayoh.github.io/pkmn6gen/chain_fishing_shiny |

### mucksw.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Feebas Tile Calculator | scaricato | https://mucksw.github.io/Feebas-Tile-Calculator |

### nintendo.fandom.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://nintendo.fandom.com/wiki/List_of_Pok%C3%A9mon_games |

### nintendolife.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Picnic Breeding | catalogato | https://www.nintendolife.com/guides/pokemon-scarlet-and-violet-how-to-breed-pokemon |

### olmectron.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | http://olmectron.github.io/forwarders/sdcard.(fwd%7Cnds |

### pages.citebite.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | http://pages.citebite.com/v5l6v8x9t1sph |

### plailect.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | fallito | https://plailect.github.io/Guide |

### play.google.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | Sync for reddit | non raggiunto | https://play.google.com/store/apps/details?id=com.laurencedawson.reddit_sync |

### play.pokemonshowdown.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://play.pokemonshowdown.com/lgpeoverused |

### pokecommunity.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | follow this tutorial | non raggiunto | https://www.pokecommunity.com/showthread.php?t=378618 |

### pokemonlp.fandom.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Dual Slot Mode | fallito | https://pokemonlp.fandom.com/wiki/Dual-slot_mode |

### pokemonpostgame.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | Black & White 2 Post Game Checklist (pokemonpostgame.com) | non raggiunto | https://pokemonpostgame.com/src/PKMNPostGame.Web/b2w2_checklist.html |

### pokepal.rpintosh.eu (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | catalogato | https://pokepal.rpintosh.eu/ |

### pokewiki.de (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Follow this link | catalogato | https://www.pokewiki.de/Spezial:Geheimcode-Generator |

### prama-initiative.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | PRAMA Initiative - Accueil | scaricato | https://www.prama-initiative.com/ |

### pretendo.network (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Pretendo Network | scaricato | https://pretendo.network/ |

### psypokes.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | this calculator | non raggiunto | http://www.psypokes.com/gsc/dv.php |

### puu.sh (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | collegamento del post | catalogato | http://puu.sh/257S |

### pycosites.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Pokemon IV Calculator (Gen 1) | scaricato | https://pycosites.com/pkmn/ivcalc_gen1.php |

### r-roms.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | . | non raggiunto | https://r-roms.github.io/ |

### reddit.zendesk.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | Reddiquette here | non raggiunto | https://reddit.zendesk.com/hc/en-us/articles/205926439-Reddiquette |

### reddithelp.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | reddiquette | non raggiunto | https://www.reddithelp.com/en/categories/reddit-101/reddit-basics/reddiquette |

### redditinc.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | Reddit's Content Policy | non raggiunto | https://www.redditinc.com/policies/content-policy |

### repl.it (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | here | fallito | https://repl.it/@flipflipshift/FeebasMethod |

### retrohandhelds.gg (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | How To Backup Cartridge Saves on an Analogue Pocket / Retro Handhelds | scaricato | https://retrohandhelds.gg/how-to-backup-cartridge-saves-on-an-analogue-pocket |

### ribbons.guide (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Ribbons.Guide - Ribbon Tracking and Guidance | scaricato | http://ribbons.guide/ |

### rotomlabs.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | DexNav Shiny Chance Calculator - RotomLabs | scaricato | https://rotomlabs.net/omega-ruby-alpha-sapphire/dexnav-calculator |

### save-editor.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | DeSmuME SAVE CONVERTER (DSV⇔SAV) - SAVE-EDITOR.com | scaricato | https://www.save-editor.com/tools/wse_ds_save_converter_for_emulator_desmume_dsv.html |

### scarletviolet.pokemon.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | https://scarletviolet.pokemon.com/en-us/news/pokemon\_go\_connect/ | non raggiunto | https://scarletviolet.pokemon.com/en-us/news/pokemon_go_connect |

### skeetendo.proboards.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | RAM Map 2 | non raggiunto | http://skeetendo.proboards.com/thread/75/pokemon-golds-ram |

### smoda.elpais.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | senza descrizione | catalogato | https://smoda.elpais.com/wp-content/uploads/2016/12/cover43.jpg |

### ssbwiki.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | still applicable | non raggiunto | http://www.ssbwiki.com/index.php?title=Wobbling&mobileaction=toggle_view_desktop |

### store.xkcd.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://store.xkcd.com/products/signed-prints |

### strategywiki.org (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Mew glitch | fallito | https://strategywiki.org/wiki/Pok%C3%A9mon_Red_and_Blue/Mew_glitch |

### supereffective.gg (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | SuperEffective.gg | non raggiunto | http://supereffective.gg/ |

### tellu.wpblog.jp (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | http://tellu.wpblog.jp/rng-abuse/7thgen-rng-abuse/guide-for-breeding-abuse-on-sunmoon |

### thonky.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | How to Trade Between Two Pokémon Games - Pokemon Walkthroughs and Utilities | scaricato | https://www.thonky.com/pokemon/trading |

### timeanddate.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | [this stopwatch | fallito | https://timeanddate.com/stopwatch |

### translate.googleusercontent.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | google translate version | non raggiunto | https://translate.googleusercontent.com/translate_c?depth=1&hl=de&ie=UTF8&prev=_t&rurl=translate.google.com&sl=ja&tl=en&u=http%3A%2F%2Fblastoise-x.hatenablog.com%2Fentry%2FSM-breed&usg=ALkJrhiRnklaS0fZrdeVutgQ4qLI56h3QQ |

### tshadowknight.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | here | catalogato | http://tshadowknight.com/Headbutt%20Grid.htm |

### tswann89.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | list of known genners here | non raggiunto | https://tswann89.github.io/PokemonSV/blacklist |

### universal-team.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | pkmn-chest / Universal-Team | scaricato | https://universal-team.net/projects/pkmn-chest |

### vimm.net (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://vimm.net/vault |

### web.archive.org (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Nintendo Wi-Fi Connection service for Nintendo DS and Wii has ended - Nintendo Official Site | scaricato | https://web.archive.org/web/20140825172450/http://www.nintendo.com/whatsnew/detail/vyWpoM6CBIe6FjW8NIY7bvzOrgBURhzw |

### wii.guide (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://wii.guide/riiconnect24 |

### wiimmfi.de (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | https://wiimmfi.de | fallito | https://wiimmfi.de/ |

### wiki.ds-homebrew.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | TWiLight Menu++ / DS-Homebrew Wiki | scaricato | https://wiki.ds-homebrew.com/twilightmenu |

### wk.reddit.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | obtain the flair | catalogato | https://wk.reddit.com/r/pokemontrades/wiki/flair |

### ww1.microchip.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | catalogato | http://ww1.microchip.com/downloads/en/DeviceDoc/DDI0029G_7TDMI_R3_trm.pdf |

### xkcdref.info (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Statistics | catalogato | http://xkcdref.info/statistics |

### your-domain.com (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | senza descrizione | non raggiunto | https://your-domain.com/ |

### yuhasem.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 2 | Feebas Finder | scaricato | https://yuhasem.github.io/FeebasFinder |

### zetadesigns.github.io (1)

| Prof | Che cosa documenta | Esito nella corsa | URL |
|---|---|---|---|
| 3 | 3DS games | non raggiunto | https://zetadesigns.github.io/randomizing-layeredfs.html |


## Fonti operative dei track su hardware fisico

Queste erano già citate dentro i rispettivi handoff e le riporto qui nella parte che ha valore durevole, cioè guide e strumenti. La coda di discussioni, pagine di codici trucco e thread di assistenza resta negli handoff, dove ha il contesto che la rende comprensibile.

| Fonte | URL | Ambito | Track |
|---|---|---|---|
| 3ds.hacks.guide | https://3ds.hacks.guide/ | procedura canonica di modding del 3DS, incluse le pagine su MSET9 e sull'uso di GodMode9 | 3DS |
| 3ds.hacks.guide, dump | https://3ds.hacks.guide/dumping-titles-and-game-cartridges.html | dump di titoli e cartucce dalla console | 3DS |
| Manuale di GBxCart RW | https://www.gbxcart.com/wp-content/uploads/2019/10/GBxCart-RW-Manual-Rev43.pdf | procedura d'uso del lettore, revisione 43 | SME, BRI |
| Driver CH340 | https://www.wch-ic.com/downloads/CH341SER_EXE.html | driver seriale necessario al lettore su Windows | SME |
| Chiusura di Pokemon Bank | https://www.nintendolife.com/news/2026/08/pokemon-bank-is-shutting-down-in-february-2027 | vincolo temporale esterno che tocca le decisioni di trasferimento | 3DS |
| Annuncio ufficiale, Rosso Fuoco e Verde Foglia si collegano a Home | https://www.pokemon.com/us/news/pokemon-firered-version-and-pokemon-leafgreen-version-link-with-pokemon-home-this-october | letto per intero il 2026-09-07 ed è la fonte primaria su cinque fatti che nessuna fonte secondaria riportava con precisione: l'istante esatto della chiusura della banca, cioè giovedi 25 febbraio 2027 alle 19 del fuso del Pacifico; il regalo di Celebi nel deposito a chi completi il catalogo dei due titoli, senza obbligo di trasferire; i due biglietti consegnati automaticamente dopo la Sala d'Onore, che danno Lugia, Ho-Oh e Deoxys; l'aumento della capienza del piano a pagamento da seimila a novemila con la versione 4.1.0 di ottobre 2026; e il trasferimento, per la prima volta, degli esemplari catturati con la Safari Ball nell'applicazione per telefono, la cui palla diventa una Palla Strana. Dichiara inoltre che la banca non è attualmente scaricabile, il che spiega perché due voci restino fuori portata per chi non l'avesse già | PKD, 3DS, EVT |
| Pagina ufficiale del servizio, in italiano | https://www.pokemon.com/it/app/pokemon-home | la pagina che l'editore aggiorna con i limiti e i prezzi correnti dei due piani; è la fonte da riconsultare quando un numero di capienza va confermato, perché una notizia invecchia e una pagina di servizio no | PKD |
| Assistenza Nintendo Italia, domande frequenti sul deposito | https://www.nintendo.com/it-it/Assistenza/Nintendo-Switch/FAQ-Pokemon-HOME-1728294.html | il confronto fra piano base e piano a pagamento, con rimando alla pagina dell'editore per i limiti aggiornati | PKD |
| Servizio clienti dell'editore | https://support.pokemon.com/hc/it | la sezione di assistenza sul deposito, dove stanno le condizioni di servizio e le risposte operative | PKD |

## Che cosa è stato usato davvero

Un registro elenca ciò che esiste, non ciò che è stato consultato, e la differenza va dichiarata perché altrimenti l'ampiezza dell'elenco si scambia per profondità della verifica. L'inventario completo delle verifiche, con il file di sorgente che ha risposto a ciascuna domanda, sta in `docs/23-prove-eseguite.md`; qui basta la sintesi per livello.

Del livello 1 sono stati clonati e cercati nel codice sei repository, cioè i tre disassemblati `pokered`, `pokecrystal` e `pokeemerald`, più il PCCS, Poke Transporter GB e Pokemon-Gen3-to-Gen-X. Pan Docs e GBATEK non sono stati letti, e va corretta un'affermazione precedente di questa stessa sezione che diceva il contrario: la loro esistenza e il loro ambito sono stati confermati dai risultati di ricerca, nessuna delle due pagine è stata aperta, e nessuna affermazione tecnica del progetto poggia su di esse. Gli altri repository del livello 1 sono catalogati e non aperti.

Del livello 2 sono state lette le sedici pagine enciclopediche elencate più le cinque aggiunte il 2026-08-28 e il 2026-08-29 sulla catena di trasferimento e sulle distribuzioni italiane, ed è il livello che ha prodotto le quattro affermazioni sbagliate descritte più sopra. Del livello 3 sono stati letti i sorgenti di nove progetti, mentre gli editor e le librerie come `PKHeX`, `PKSav`, `HexManiacAdvance` e `FlashGBX` sono catalogati e non eseguiti: nessuno di essi è stato lanciato, per la ragione semplice che non esiste ancora un salvataggio reale su cui lanciarli. Il confronto dell'interpretazione dei campi con `PKHeX` è il prossimo controllo in ordine di convenienza, ed è registrato come tale.

Del livello 5 è stata letta anche la discussione sull'algoritmo di generazione degli eventi, che è la sola voce di quel livello a essere stata aperta per il suo contenuto tecnico e non come indicazione di dove cercare. Del livello 4 sono stati letti i quattro articoli tecnici che la tabella cita per contenuto specifico, e dieci video sono stati letti per trascrizione, sei il 2026-08-25 e quattro il 2026-08-28: la pagina di YouTube resta inaccessibile al crawler, ma i sottotitoli si scaricano con lo strumento a riga di comando, quindi il testo di un video è disponibile mentre il video non è stato guardato. Del livello 5 sono state lette le discussioni consegnate dall'utente come schermate. La frase che stava qui, cioè che i thread di Reddit restassero non letti perché il dominio non è raggiungibile, non vale più dal 2026-09-07 e va sostituita da un conto invece che da un'altra dichiarazione. Delle centosettantuno voci del corpus della collezione, sessantacinque post sono stati scaricati con il loro albero di commenti e trentasei pagine esterne sono state ridotte a testo: tutte e centouno stanno su disco sotto `_notes/`, nessuna delle due cifre significa però che siano state lette, e questa è la distinzione che questa sezione esiste per non far perdere. Scaricato vuol dire disponibile senza chiedere altro a nessuno; letto vuol dire che il suo contenuto è stato trasferito in prosa in un documento di progetto. Alla data di oggi il corpus è interamente scaricato e letto per un due per cento, e il debito che ne discende è registrato in `pending.md` con l'ordine di lettura, che non è l'ordine del post ma quello dell'utilità per il lavoro in corso.

Nessuno strumento hardware è stato usato, perché nessuno è disponibile: il lettore di cartucce del track Smeraldo non è ancora arrivato, e nessun emulatore è stato lanciato, nemmeno BGB, di cui è documentata la possibilità di collaudo su TCP.

## Cosa non entra in questo registro

Non entrano le fonti che documentano come ottenere materiale coperto dal perimetro dichiarato in `.claude/rules/hardware-and-perimeter.md`, né i salvataggi di terze parti, e non entra nulla che contenga o distribuisca materiale di chiave console-unica. Non entrano le pagine effimere, cioè thread di assistenza e discussioni che valgono per una singola sessione: quelle restano nell'handoff del track che le ha usate. Non entrano i mirror di ROM, che non servono a nessuno degli obiettivi di questo progetto, dato che si lavora su cartucce possedute. E non entrano le pagine di codici trucco, che sono la causa più probabile del problema che il track Smeraldo deve risolvere e non la sua soluzione.
