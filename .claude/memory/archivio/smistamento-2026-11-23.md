# Smistamento del 2026-11-23 delle voci aperte dell'archivio del registro

Tabella prodotta il 2026-11-23 da un subagente, su richiesta del proprietario («fai, immediatamente»), per le 131 voci della sezione «Da smistare dall'archivio» di `pending.md`, che rimandano a `pending-fino-al-2026-11-20.md` in questa cartella. Le prove di chiusura sono state cercate con grep su `progress.md`, `decisions.md`, `index.md` e `pending.md`; i numeri di riga del work log sono quelli del 2026-11-23 prima delle voci di quel giorno, quindi sono spostati di circa sedici righe. Tre voci CHIUSE sono state ricontrollate a campione dall'agente principale (righe 355, 583 e 117 dell'archivio): le prove esistono. Le CHIUSE e le SUPERATE escono dal registro; le APERTE e le INDETERMINATE restano in `pending.md`.

Conteggi: INDETERMINATA=35; SUPERATA=22; APERTA=19; CHIUSA=55;  totale 131

| riga archivio | sezione | etichetta | motivo e prova | che cosa resta (solo APERTA) |
|---|---|---|---|---|
| 25 | 2026-11-03 alla ripresa | APERTA | Hook SessionStart di controlla-eventi-nuovi.py gia' attivo; manca il confronto integrale delle liste Bulbapedia 8a/9a gen e HOME con i lotti Switch (nessun riscontro di chiusura nel work log) | Agente, fase Switch dopo Bank, non sotto scadenza |
| 41 | 2026-11-03 alla ripresa | CHIUSA | Il testo stesso: verifica dei sei punti TransferBad fatta il 2026-11-11 (COPIE-PER-HOME.md), esito zero su HOME7, HOME10, GIAPPONE2 |  |
| 43 | 2026-11-03 alla ripresa | CHIUSA | FATTO 2026-11-11: generatori via tools/rigenera_sicuro.py, bibliografia 134 voci; il promemoria dei --check e' ora in CLAUDE.md |  |
| 45 | 2026-11-03 alla ripresa | CHIUSA | Voce 119 dichiara CHIUSE le voci della CONSEGNA 2026-11-06; il residuo DOPO BANK sta in pending.md riga 9 («Si fanno con calma dopo il 26 febbraio 2027») |  |
| 49 | 2026-11-03 alla ripresa | CHIUSA | Giri 8 e 9 fatti e in HOME (voce stessa), poi giri 10-14 fino a 7466 (index.md, progress.md:157) |  |
| 51 | 2026-11-03 alla ripresa | CHIUSA | Decisione presa (voce 53), 996 doni riscritti (ADR-126, decisions.md:1700, voce 63); misura in DATE-INCONTRO.md |  |
| 53 | 2026-11-03 alla ripresa | CHIUSA | ADR-126; etichetta «Bank N» verificata sul Pumpkaboo (progress.md:235); 996 riscritti e liberazione ora in «Aperte adesso» |  |
| 55 | 2026-11-03 alla ripresa | APERTA | Verde Foglia (estrazione GBxCart, PUCCETTO, lotto) e le due squadre estratte in lotto-squadre-cartucce da portare con la data ADR-128; i 1964 gia' in HOME da ridatare a ridosso della chiusura di Bank (rimandato 2026-11-17) | Proprietario con agente; SOTTO scadenza Bank 2027-02-26 |
| 57 | 2026-11-03 alla ripresa | CHIUSA | Giro 12 e 13 in HOME (6791, 7221); liberazione dei 996 ora in «Aperte adesso»; la cartella «home 7221» non esiste piu' sul disco; resta_in_console fatto (voce 113) |  |
| 61 | 2026-11-03 alla ripresa | APERTA | Jirachi cromatici e giro 12 FATTI; resta il file unico stampabile della collezione in stile Sugimori: la voce 17-11 dice «non esiste ancora» e nessun riscontro dopo (ADR-127 regola la sola rigenerazione) | Agente, non sotto scadenza |
| 63 | 2026-11-03 alla ripresa | CHIUSA | 996 riscritti, giro 12-13 fatti, Jirachi ammessi e prodotti (voce 61); le cartelle lotto-ridata-20261116 e b non esistono piu' (resta solo la c) |  |
| 67 | 2026-11-03 alla ripresa | APERTA | Estrazione di Verde Foglia con GBxCart e doppia riserva, poi pedigree e giro con Bank; contatti puliti 2026-11-23, in «Aperte adesso» | Proprietario con agente; SOTTO scadenza Bank 2027-02-26 |
| 91 | 2026-11-03 alla ripresa | SUPERATA | Segnalazione hook del 2026-11-16 superata da letture del 2026-11-20 e 2026-11-23, segnate (pending.md «Aperte adesso»); allineamento template fatto (8620f4a) |  |
| 93 | 2026-11-03 alla ripresa | APERTA | CLAUDE.md misura 17133 byte contro tetto 15000 di tools/misura-istruzioni.py (misurato ora): sposta Apprendimenti recenti e blocco satelliti | Agente, non sotto scadenza |
| 99 | 2026-11-03 alla ripresa | APERTA | Da chiedere: quanti Meltan catturati e cromatico; pedigree in ESEMPLARI-DA-GO.md; Melmetal da 400 caramelle; in «Aperte adesso» c'e' l'Inkay per riaprire la Scatola (progress.md:269,275) | Proprietario risponde, agente scrive; non dipende da Bank |
| 103 | 2026-11-03 alla ripresa | APERTA | Jirachi cromatico FATTO (voce 61); resta Magearna Colore Originale, rinviata dopo Bank come dono di HOME (progress.md:235) | Agente, fase Switch dopo Bank, non sotto scadenza |
| 107 | 2026-11-03 alla ripresa | SUPERATA | Segnalazione hook del 2026-11-13 superata da letture 11-20 e 11-23 segnate; allineamento template fatto |  |
| 109 | 2026-11-03 alla ripresa | SUPERATA | Revisione di List of other event distributions in Gen VII letta e segnata in letture successive (voce 111, 11-20, 11-23) |  |
| 111 | 2026-11-03 alla ripresa | CHIUSA | Revisioni lette e segnate il 2026-11-11 (testo stesso); allineamento al template eseguito piu' volte (ultimo 8620f4a) |  |
| 113 | 2026-11-03 alla ripresa | CHIUSA | Giri 7 e 8 in HOME, pulizia superata, esemplari da GO coperti dalla voce 99 |  |
| 115 | 2026-11-03 alla ripresa | CHIUSA | ADR-121 e ADR-122 decisi, Farfetch'd bonificati (ADR-123), Rayquaza in HOME9, Psyduck STADIO passato (progress.md:493,503) |  |
| 117 | 2026-11-03 alla ripresa | CHIUSA | Giri 4-6 in HOME (3529, 3785, 4567); errore 006-0112 tolto da ADR-132; GO e Meltan restano in voce 99 |  |
| 119 | 2026-11-03 alla ripresa | CHIUSA | Il testo dice che le voci della CONSEGNA 2026-11-06 sono CHIUSE; tutte le copie pronte e giri in HOME fino al 14 |  |
| 121 | 2026-11-03 alla ripresa | APERTA | Magikarp del Pokemon Center di Hiroshima 2015 (normale e cromatico): fonte da leggere, nelle copie due non cromatici (HOME3 box 20); nessuna occorrenza di Hiroshima in progress/decisions | Agente; in lotto HOME quindi SOTTO scadenza Bank 2027-02-26 |
| 123 | 2026-11-03 alla ripresa | CHIUSA | Voce stessa: FATTO 2026-11-09 censimento e rilettura fonti vive segnati |  |
| 125 | 2026-11-03 alla ripresa | SUPERATA | Chiusura di sessione 2026-11-05 (commit 0e35390, giro 3 poi chiuso a 2600, progress.md:629) |  |
| 127 | 2026-11-03 alla ripresa | CHIUSA | Giro 3 punti 5-17 fatti (HOME 2600); 46 eventi senza carta confrontati (voce 119) |  |
| 129 | 2026-11-03 alla ripresa | CHIUSA | Giro 3 chiuso; candidati RNG e Jirachi prodotti (voci 61, 115); PDF collezione: stampabile ADR-127 |  |
| 131 | 2026-11-03 alla ripresa | CHIUSA | Giro 3 chiuso, pulizia superata (voce 113), 345 eventi Serebii e 46 senza carta ritrovati (voce 119) |  |
| 133 | 2026-11-03 alla ripresa | CHIUSA | Giri 2 e 3 chiusi; pulizia superata; voci non costruibili documentate in ELENCO-PRODUZIONE |  |
| 135 | 2026-11-03 alla ripresa | CHIUSA | Kyogre deciso con ADR-114 (blisy, ID 13181, decisions.md:967); pulizia superata; giro 2 chiuso |  |
| 137 | 2026-11-03 alla ripresa | CHIUSA | Allineamento 444190a applicato (voce 135), caselle 936/936 e pedigree 3407 schede, giri fatti, pulizia superata |  |
| 139 | 2026-11-03 alla ripresa | CHIUSA | Caselle 936 su 936 coperte (voce 135/129); COPERTURA-LOTTI.md rigenerabile |  |
| 143 | 2026-11-03 alla ripresa | CHIUSA | Sfide 47 su 47 coperte (voce 129); DA-PORTARE-PRIMA-DI-BANK.md |  |
| 145 | 2026-11-03 alla ripresa | CHIUSA | Elenco sfide completo: 47 su 47 controllate su cinque fonti (voce 143) |  |
| 149 | 2026-11-03 alla ripresa | APERTA | Resta il catalogo stampabile della collezione completa alla fine (ADR-107/ADR-127) e le schermate delle schede Scambi e Altro mai fotografate (decisions.md:1073) | Agente (catalogo) e proprietario (schermate); non sotto scadenza |
| 151 | 2026-11-03 alla ripresa | APERTA | Direttiva permanente da ricordare sempre: tracciare esemplari da evento; quelli Switch entrano nel lavoro su Switch dopo Bank | Agente, permanente; parte Switch dopo la scadenza |
| 153 | 2026-11-03 alla ripresa | CHIUSA | La cartella _notes/lavoro/storia/riscrittura-20261103.git non esiste piu' (ls) |  |
| 165 | 2026-11-03 alla ripresa | SUPERATA | Riscrittura storia decisa e fatta (ADR-105, voce 153: zero occorrenze dei valori); file corrente con zeri |  |
| 173 | 2026-10-06 verifica dopo spegnimento | CHIUSA | Tredici lacune chiuse (testo); documentazione di Checkpoint letta e usata (voce 55: tutorial Project Pokemon, ConsoleMods) |  |
| 183 | 2026-10-07 ordine di lavoro | SUPERATA | Debito della tesi: ADR-105 riscrive la tesi da capo; in «Aperte adesso» il piano della riscrittura |  |
| 185 | 2026-10-07 ordine di lavoro | CHIUSA | Voce con FATTO su ADR-099 e Manaphy (ADR-103); Rubino scritto 2026-11-20 (ADR-135) |  |
| 187 | 2026-10-07 ordine di lavoro | CHIUSA | MAPPA-DOCUMENTI.md riscritta da zero il 2026-11-20 (pending.md «Aperte adesso») |  |
| 189 | 2026-10-07 ordine di lavoro | SUPERATA | Rubino scritto (ADR-135), copie portate in HOME, decisione sui 158 presa (ADR-121); resta solo la Switch, in switch-modding/ (ADR-133) |  |
| 195 | 2026-10-07 ordine di lavoro | INDETERMINATA | Tabella connettivita' di HOME letta (voce 43, 11-11) e Biglietti verificati (progress.md:1053), ma il foglio dell'Azienda Lotta di BPark16 non compare nei registri (grep: nessun riscontro) |  |
| 199 | 2026-10-07 ordine di lavoro | INDETERMINATA | ADR-100 punto 4 parte deterministica fatta (progress.md:1051, censimento-fonti-codice.py); non trovo la chiusura del potenziamento completo |  |
| 205 | CORREZIONE 2026-10-06 | CHIUSA | verifica-link-progetto.py chiuso a zero (voce stessa); porting fatto: esiste in E:/template-claude-developing/.claude/templates/verifica-link/tools/ |  |
| 209 | risposte 2026-10-05 (ADR-096) | APERTA | Direttiva permanente: studiare gli strumenti interattivi per potenziare gli script; docs/strumenti-dal-web.md e strumenti-interattivi.md esistono ma la voce e' da ricordare sempre | Agente, permanente, non sotto scadenza |
| 217 | risposte 2026-10-05 (ADR-096) | CHIUSA | Risposte community tutte e quattro; 121 divisi (voce 115); decisione ADR-121/122 |  |
| 223 | risposte 2026-10-05 (ADR-096) | CHIUSA | Lotti nel registro dei giudizi (progress.md:1233, lotto-ombre-ereader-jp); copie rifatte (voce 185) |  |
| 239 | Quadro 2026-10-05 | SUPERATA | Lo smistamento delle voci superate e' il riordino del 2026-11-20 (pending.md); sezione PRIMA DI TUTTO CHIUSA con stato-residuo-corpus --check zero |  |
| 241 | Quadro 2026-10-05 | CHIUSA | Sette indirizzi recuperati (ESITO.md); incursioni di evento SwSh coperte da ADR-097 (progress.md:1237) |  |
| 247 | PRIMA DI TUTTO residuo corpus | INDETERMINATA | Cercati converti-salvataggio-vc e ftpd in progress/decisions: nessun riscontro di verifica dei 16 byte ne' di documentazione ftpd |  |
| 249 | PRIMA DI TUTTO residuo corpus | CHIUSA | Scambi di sesta e settima gen prodotti: pkhex-scambi-gen67, lotto-scambi-gen67 (progress.md:1233, voce 185) |  |
| 253 | PRIMA DI TUTTO residuo corpus | INDETERMINATA | GB-Link/switch.gblink.io: solo menzioni del 2026-10-05 e voce 384; nessuna verifica su chiavi e carte |  |
| 255 | PRIMA DI TUTTO residuo corpus | SUPERATA | HOME 4.1.0 e Rosso Fuoco/Verde Foglia per Switch verificati (progress.md:1053); la voce stessa dice che non cambia i lotti |  |
| 257 | PRIMA DI TUTTO residuo corpus | CHIUSA | Riassunto HOME 4.1.0 verificato su sette fonti (progress.md:1053) |  |
| 259 | PRIMA DI TUTTO residuo corpus | CHIUSA | Scambi gen 6/7 prodotti con lotto e decisione (progress.md:1233) |  |
| 261 | PRIMA DI TUTTO residuo corpus | INDETERMINATA | ID-NOTEVOLI.md bug 16/32 bit: nessun riscontro di correzione nei registri |  |
| 263 | PRIMA DI TUTTO residuo corpus | INDETERMINATA | Ponte di Goppier e gioco di origine: nessun riscontro nei registri |  |
| 274 | PRIMA DI TUTTO residuo corpus | SUPERATA | ADR-133 apre switch-modding/ (Switch di prima generazione usata) come via per la fase Switch |  |
| 291 | PRIMA DI TUTTO residuo corpus | INDETERMINATA | Cercato qwen2.5vl: nessun riscontro in progress/decisions/index |  |
| 301 | Da fare per primo 2026-09-29 | CHIUSA | Voce stessa: FATTO 2026-09-29, chiudi -SoloControlli verde |  |
| 317 | Da fare per primo 2026-09-29 | CHIUSA | VERIFICATO e Manaphy Ranger generato (testo); SCHEDE-ESEMPLARI-GEN4.md esiste e tools/schede-esemplari-gen4.py (progress.md:1211) |  |
| 321 | Da fare per primo 2026-09-29 | INDETERMINATA | Catena GPU pronta con chiave dedicata (progress.md:1615); non trovo conferma che la password sia stata cambiata |  |
| 345 | Da fare per primo 2026-09-29 | INDETERMINATA | Account Discord disattivato da Discord il 2026-10-01 (progress.md:1389), ma nessuna conferma che il proprietario abbia cambiato la password |  |
| 355 | Da fare per primo 2026-09-29 | CHIUSA | GIAPPONE e GIAPPONE2 (23 esemplari) in HOME (progress.md:269, ADR-125) |  |
| 363 | Da fare per primo 2026-09-29 | CHIUSA | Difetto CORRETTO (testo); copie rigenerate e giri successivi fatti |  |
| 367 | Da fare per primo 2026-09-29 | SUPERATA | Copie rifatte con le generazioni di giri 1-14 (voce 119); salvataggi di terzi usati solo come appoggio (ADR-124) |  |
| 373 | Da fare per primo 2026-09-29 | CHIUSA | Riserve Checkpoint fatte a ogni giro (es. sd-checkpoint-20261105, 20261116) |  |
| 375 | Da fare per primo 2026-09-29 | SUPERATA | Testo originale della voce precedente: lo strumento pkhex-scrivi-salvataggio esiste e i giapponesi sono passati (ADR-125) |  |
| 384 | Da fare per primo 2026-09-29 | INDETERMINATA | Verifica se prod.keys partono verso un server (GB-Link): nessun riscontro nei registri |  |
| 388 | Da fare per primo 2026-09-29 | INDETERMINATA | Fori a 80 mm: cercato nei registri, solo il margine di rilegatura di 2,5 cm (progress.md:1795), non la prova della prima pagina |  |
| 390 | Da fare per primo 2026-09-29 | CHIUSA | Voce stessa: CHIUSO 2026-10-07; Rubino scritto 2026-11-20 (ADR-135) |  |
| 537 | Parco Lotta dopo lettura 2026-09-21 | INDETERMINATA | Difetto IV nona serie e effetto riposo: nessun riscontro di verifica sul sorgente |  |
| 583 | Squadra Parco Lotta Lv.50 | CHIUSA | Rosso Fuoco/Verde Foglia su Switch, Deoxys e Celebi verificati (progress.md:1053); Victini via Passo Libertà (decisions.md:1183) |  |
| 589 | Squadra Parco Lotta Lv.50 | CHIUSA | decisions.md:1183: server di replica non si usa e non serve, Victini generato con la libreria |  |
| 607 | Squadra Parco Lotta Lv.50 | SUPERATA | ADR-076 (decisions.md:1496): i 27 cromatici si cancellano, nessun risanamento |  |
| 611 | Squadra Parco Lotta Lv.50 | CHIUSA | Complemento del Rubino in HOME (376, voce 55); Rubino scritto 2026-11-20 (ADR-135); resta solo il controllo in gioco passo 19, gia' in «Aperte adesso» |  |
| 621 | Squadra Parco Lotta Lv.50 | SUPERATA | ADR-076: i 27 cromatici e le 11 copie del noleggio sono cancellati (decisions.md:1496) |  |
| 893 | Decisione che richiede ADR | INDETERMINATA | Flag interno sulla visibilita' del PC: nessun riscontro di verifica |  |
| 1069 | Perimetro deciso 2026-09-09 | SUPERATA | Scambi in gioco prodotti con la libreria (ADR-081, pkhex-scambi-gen67); non serve il generatore a personalita' |  |
| 1070 | Perimetro deciso 2026-09-09 | INDETERMINATA | Incontri condizionati: nessun riscontro di chiusura |  |
| 1073 | Perimetro deciso 2026-09-09 | SUPERATA | ADR-052 applicato come ordine (progress.md:3566); la coda ora e' ELENCO-PRODUZIONE e i lotti pre-Bank sono prodotti |  |
| 1074 | Perimetro deciso 2026-09-09 | CHIUSA | ADR-054 deciso (decisions.md:779); caselle 936/936 coperte con le 63 configurazioni (progress.md:3316) |  |
| 1083 | ADR-049 apre | INDETERMINATA | Sondatore dei sogni, 181 voci: ADR-049 accolto (progress.md:3754) ma nessun riscontro sulla misura o produzione |  |
| 1094 | lotto lettura 2026-09-12 | CHIUSA | tools/pkhex-esclusivi-cxd legge le tavole delle ombre di Colosseum e XD (progress.md:1469; voce 223) |  |
| 1095 | lotto lettura 2026-09-12 | INDETERMINATA | Catalogo alfa con leggi-foglio-google.py: nessun riscontro; senza scadenza |  |
| 1096 | lotto lettura 2026-09-12 | INDETERMINATA | Proiezione delle 26 specie del sondatore: nessun riscontro di esecuzione |  |
| 1097 | lotto lettura 2026-09-12 | INDETERMINATA | Marchio e passaggio nel deposito: nessun riscontro |  |
| 1110 | lotto lettura 2026-09-14 | INDETERMINATA | Allenatore delle quattro uova di Stadium: nessun riscontro |  |
| 1111 | lotto lettura 2026-09-14 | INDETERMINATA | Tre classi a via chiusa non riclassificate: nessun riscontro |  |
| 1119 | Punti tecnici aperti | SUPERATA | Push riusciti dopo il 2026-09-14 (es. «commit pubblicato, origin/main allineato», progress.md:1217) |  |
| 1122 | Punti tecnici aperti | APERTA | tools/catalogo-eventi-gen3.py non contiene alcuna colonna del luogo d'incontro (grep luogo = 0) | Agente, non sotto scadenza |
| 1123 | Punti tecnici aperti | SUPERATA | decisions.md:1183: il server di replica non si usa; si compone con la libreria |  |
| 1124 | Punti tecnici aperti | APERTA | Pacchetto alignment rinviato al gate (ADR-091); index.md dice che il gate e' dovuto alla ripresa del 2026-11-23 | Proprietario (/gate-pacchetti); non sotto scadenza |
| 1127 | Punti tecnici aperti | SUPERATA | La tesi si riscrive da capo (ADR-105); la fragilita' dei slug sparisce con essa |  |
| 1128 | Punti tecnici aperti | APERTA | Richiesta esplicita della versione inglese: tesi/ non ha cartella per lingua e nessun riscontro nei registri | Agente con proprietario, con la riscrittura della tesi; non sotto scadenza |
| 1129 | Punti tecnici aperti | SUPERATA | Capitolo da riportare al criterio ADR-056: la tesi si riscrive da capo (ADR-105) |  |
| 1138 | Punti tecnici aperti | CHIUSA | Serebii confrontato per intero con le copie e 46 senza carta ritrovati (voce 119); caselle 936/936 |  |
| 1139 | Punti tecnici aperti | SUPERATA | Confronto integrale con Serebii fatto (voce 119): il perimetro e' stato riconciliato in pratica |  |
| 1140 | Punti tecnici aperti | INDETERMINATA | Casella di abilita' a meno uno: nessun riscontro |  |
| 1141 | Punti tecnici aperti | INDETERMINATA | Specie aggiunte dal salvataggio di Jack: nessun riscontro del conto |  |
| 1143 | Punti tecnici aperti | SUPERATA | Lotti scritti con scrittura diretta in Rubino Omega e Ultraluna e passati in giri (voce 119), non in un solo salvataggio |  |
| 1149 | Punti tecnici aperti | CHIUSA | Victini generato via Passo Libertà (decisions.md:1183), Zarude prodotto (progress.md:1431) |  |
| 1151 | Punti tecnici aperti | INDETERMINATA | Celebi del regalo 2017: dichiarato fuori portata (progress.md:4440) ma nessun riscontro di produzione |  |
| 1152 | Punti tecnici aperti | APERTA | Celebi HOME 2026-10 (EventsGallery «Simulated HOME Celebi.wc8» censito il 2026-11-20): formato del dono nel deposito da decidere | Agente, fase Switch; non sotto scadenza |
| 1154 | Punti tecnici aperti | CHIUSA | Asse delle sfere misurato: pkhex-sfere-prima-di-bank e 81 coppie di sfera (progress.md:791, voce 139) |  |
| 1155 | Punti tecnici aperti | APERTA | Varianti cromatiche di tutti gli eventi rinviate dopo Bank per direttiva (ADR-118) | Agente, dopo Bank; non sotto scadenza |
| 1156 | Punti tecnici aperti | APERTA | Obiettivo lontano dichiarato: generatore delle configurazioni di Spinda | Agente, non sotto scadenza |
| 1157 | Punti tecnici aperti | INDETERMINATA | Berretto del compagno e Celebi VC: nessun riscontro di produzione |  |
| 1158 | Punti tecnici aperti | INDETERMINATA | Nove forme fantasma di Pecharunt: nessun riscontro di correzione (solo progress.md:4480 di apertura) |  |
| 1159 | Punti tecnici aperti | CHIUSA | Criterio delle forme di sola battaglia riletto con FormInfo.IsBattleOnlyForm (progress.md:1627) |  |
| 1160 | Punti tecnici aperti | INDETERMINATA | Forme originarie di Dialga e Palkia: nessun riscontro di verifica |  |
| 1161 | Punti tecnici aperti | INDETERMINATA | Tre note del foglio sulla scadenza: nessun riscontro di chiusura |  |
| 1162 | Punti tecnici aperti | INDETERMINATA | Timbro della banca in uscita: nessun riscontro |  |
| 1163 | Punti tecnici aperti | INDETERMINATA | Lingua dei tre scambi di quarta generazione: nessun riscontro |  |
| 1164 | Punti tecnici aperti | INDETERMINATA | Cromaticita' in prima generazione: nessun riscontro di revisione delle 16 voci |  |
| 1166 | Punti tecnici aperti | CHIUSA | I due Farfetch'd di Stadium 2 bonificati (ADR-123, progress.md:503) |  |
| 1168 | Punti tecnici aperti | CHIUSA | Deoxys con Rosso Fuoco/Verde Foglia per Switch verificato (progress.md:1053, voce 255) |  |
| 1170 | Punti tecnici aperti | INDETERMINATA | Scappatoia Spada/Scudo: nessun riscontro |  |
| 1171 | Punti tecnici aperti | INDETERMINATA | Ponte di ottobre: nessun riscontro del test con un esemplare |  |
| 1175 | Punti tecnici aperti | CHIUSA | Debito di lettura chiuso: stato-residuo-corpus --check a zero e fonti lette (voci 239 e 205) |  |
| 1176 | Punti tecnici aperti | CHIUSA | Sfide spogliate, 47 su 47 coperte (voce 143) |  |
| 1177 | Punti tecnici aperti | INDETERMINATA | Schermate 43-111: nessun riscontro di spoglio completo |  |
| 1178 | Punti tecnici aperti | CHIUSA | Fogli comunitari assorbiti: CONFRONTO-FOGLIO-LIVINGDEX.md (voce 135) |  |
| 1179 | Punti tecnici aperti | INDETERMINATA | Valutazione di Monarium: solo registrazione fonte (progress.md:3384) |  |
| 1180 | Punti tecnici aperti | APERTA | Obiettivo lontano dichiarato, registrato per non perderlo: tutte le configurazioni di Spinda | Agente, non sotto scadenza |
| 1181 | Punti tecnici aperti | CHIUSA | Pedigree di ogni esemplare (ADR-111, 3407 schede) e SCHEDE-ESEMPLARI-GEN4.md esistono |  |
| 1225 | Decisioni aperte | INDETERMINATA | Distinzione allenatori distinti dalle traduzioni sulle 304 distribuzioni: nessun riscontro |  |
| 1241 | Strumenti da costruire | APERTA | SPOGLIO-CORPUS.md da rigenerare sul corpus di oggi: DA DECIDERE, nessuna decisione (progress.md:1653) | Proprietario decide; non sotto scadenza |

## Secondo passaggio sulle 35 indeterminate, 2026-11-23

Due subagenti, con `git grep`, storia dei commit e lettura dei file citati. Correzione dell'agente principale: la riga 1157 è CHIUSA e non aperta per il proprietario, perché il Pikachu con il berretto Compagni c'è in `pedigree/HOME5.md` e `pedigree/RIDATA2.md`, e il proprietario aveva già detto il 2026-09-07 che la sua Bank non risale a prima di marzo 2023. Le righe 1097 e 1162 riguardano l'uscita da HOME verso i giochi, perché da HOME non si torna a Bank: non sono domande per il proprietario ma ricerca dell'agente per la fase Switch.

### indeterminate-A.md

| riga | etichetta | prova o prossimo passo o domanda |
|---|---|---|
| 195 | APERTA-PROPRIETARIO | Tabella connettività HOME letta (CONNETTIVITA-HOME.md) e Biglietti verificati (progress.md:1101, HOME 4.1.0 su sette fonti). Resta aperto solo il foglio dell'Azienda Lotta fissato dal suo autore, che SOURCES.md:389 dice ancora da avere, senza consegna successiva. Domanda: hai ottenuto il foglio fissato nel canale Discord dell'Azienda Lotta, o lasciamo cadere il confronto (decisions.md:1193, Discord escluso)? Se consegnato, l'agente rilancia `parco_lotta_confronta_lrxc.py`. |
| 199 | APERTA-AGENTE | ADR-100 punto 4: fatta solo la parte deterministica (progress.md:1099, `tools/censimento-fonti-codice.py`, schede in docs/fonti-codice-schede.md). `docs/potenziamento-dalle-fonti.md:44` dichiara quattro lotti di lettura del codice e nessuno risulta eseguito (nessuna decisione per repository in docs/22-strumenti.md o docs/strumenti-dal-web.md). Prossimo passo: lotto 1, leggere il codice di PKHeX-Plugins, OpenHome, PKForge e Checkpoint e scrivere una decisione per repository. Sotto scadenza Bank: no; il lotto 4 (entralinked) può allargare la collezione e chiede una decisione del proprietario. |
| 247 | APERTA-AGENTE | (1) I 16 byte finali del `sav.dat` VC restano non verificati (docs/22-strumenti.md:849: PKHeX li tratta come coda di orologio e li scarta); la verifica richiede un salvataggio VC vero dalla console, quindi serve il proprietario solo se vuole usare lo strumento verso il 3DS: domanda, hai un salvataggio VC di Oro/Argento/Cristallo del 3DS da dumpare per confrontare i 16 byte? (2) ftpd come via facoltativa del passo 03: nessun riscontro in 3ds-related, archivio/handoff o nelle schede, compare solo in docs/strumenti-interattivi.md:26 e SOURCES.md. Prossimo passo agente: documentare ftpd (.3dsx) nella procedura del passo 03 (ora in archivio/handoff/3ds-related o nel README del 3DS). Sotto scadenza Bank: marginale, il 3DS è sul percorso verso Bank. |
| 253 | APERTA-AGENTE | I fatti di switch.gblink.io (carte di dono segreto, ESP32, quattro chiavi) stanno in SOURCES.md:1271 ma non sono stati portati in `sub-gba-switch-trading.md` (riga 95 cita solo il video Kevdog) né in `STRATEGIA-SWITCH.md` (nessun riscontro di gblink, RetroSync, Papa Jefé). Le tre verifiche non risultano fatte e non c'è un clone di GBLink-Firmware in `_notes/fonti/cloni`. Prossimo passo: shallow clone di `GB-Link/GBLink-Firmware`, lettura del sorgente della pagina, poi aggiornare le due schede (stesso lavoro della riga 384). Sotto scadenza Bank: sì in senso di decisione, è la via a HOME senza banca; serve prima del 2027-02-26 per scegliere se usarla. |
| 261 | APERTA-AGENTE | Difetto ancora presente: in `tools/censimento-id-notevoli.py`, `nostri()` (riga 99) e `classifica()` (riga 121) confrontano il valore grezzo, e `pokedex-home-completo/ID-NOTEVOLI.md` elenca ancora fra le non coperte Cotton 05720 (riga 40), Yancy 10303 (74), Diana 17074 (88), Slick 27658 (108), Curtis 54118 (121). Prossimo passo: per gli identificativi degli scambi aggiungere anche il valore ridotto a 16 bit (`& 0xFFFF`), rigenerare, aggiungere una prova. Sotto scadenza Bank: no (strumento di misura). |
| 263 | APERTA-AGENTE | Nessun riscontro nei documenti. Contraddizione interna: progress.md:5646 dice che il dispositivo di Goppier forza il gioco di origine a Rosso Fuoco, la voce dice un valore inventato Oro/Argento/Cristallo; `pokebridge/gen3.py:70` ammette solo 1-5 e 15 e in pokebridge non esiste ancora un convertitore Gen2-Gen3 che scelga il valore. Prossimo passo: rileggere la trascrizione di Goppier per stabilire quale delle due è vera, poi fissare in `sub-gen12-gen3-bridge.md` che il ponte scrive un gioco di origine valido. Sotto scadenza Bank: no. |
| 291 | SUPERATA | STACK.md:96-98 e progress.md:1009 e 1413: la macchina GPU è stata ripulita il 2026-10-02 e dal 2026-11-03 si usa solo con pesi già installati, senza pull né installazioni (aiutante in RAM via SSH). Il download di `qwen2.5vl:7b` con sudo non è più una via ammessa e nessuno strumento in tools/ lo cita. |
| 321 | APERTA-PROPRIETARIO | La parte tecnica è SUPERATA: ambiente `~/trascrizione` e chiave SSH del progetto rimossi il 2026-10-02 (STACK.md:98, progress.md:1413), `trascrivi-video-gpu.py` rimosso il 2026-10-06. Resta la sicurezza: la password dell'utente `ollama` scritta in chat il 2026-09-29 non risulta cambiata in nessun registro. Domanda: hai cambiato la password dell'utente ollama sulla macchina GPU, che avevi scritto in chat il 2026-09-29? |
| 345 | CHIUSA | progress.md:1437 e decisions.md:1207: il proprietario ha cambiato la password di Discord il 2026-10-01 alle 19:15, dopo la disattivazione dell'account delle 16:52, il che invalida il token incollato il 2026-09-30. |
| 384 | APERTA-AGENTE | Verifica sul sorgente non fatta (design-and-security.md:52 la dichiara ancora aperta; nessun clone del firmware). Indizio parziale, non prova: SOURCES.md:1271 riporta che la pagina dichiara le chiavi passate alla scheda via USB senza caricamento in rete. Prossimo passo: come riga 253 (clone di GBLink-Firmware e lettura del codice della pagina; Discord resta escluso, decisions.md:1193-1197, GitHub no). Sotto scadenza Bank: come riga 253. |
| 388 | APERTA-PROPRIETARIO | Lo strumento ha i fori a 80 mm (progress.md:1843, `emerald_mappa_box.py:154`: centri a 28,5, 108,5, 188,5, 268,5 mm), ma la prova è fisica e non registrata. Domanda: sulla prima pagina stampata, i quattro fori a 80 mm coincidono con gli anelli del quaderno? |
| 537 | CHIUSA | Verificato ora sul sorgente: `_notes/fonti/cloni/pokeemerald/src/battle_factory.c:744-756` (fuori limite alla serie 9 su `sFixedIVTable`, indice letto come punti individuali casuali) e riga 396 (`rentalMons[..].ivs = MON_DATA_ATK_IV`, quindi dopo salvataggio e ricarica tutti i punti prendono il valore dell'Attacco). `GUIDA-PARCO-LOTTA.md:89` li usa già come fatti. Residuo di registro: SOURCES.md:119 dice ancora DA VERIFICARE e va aggiornato (passo banale dell'agente). |
| 893 | SUPERATA | La decisione sul salvataggio scaricato non serve più: l'iniezione opera sui byte e Smeraldo è CHIUSA (sub-smeraldo-save-fix.md:8, 2026-11-20), il Rubino è scritto con rilettura identica byte per byte (progress.md:1819). Il flag di visibilità del PC non incide più sul lavoro. |
| 1070 | APERTA-AGENTE | Per la terza generazione le richieste con luogo e tipo di casella sono entrate (progress.md:1979: 37 incontri speciali, zero mancanti dopo). Per generazioni 4-5 e per le specie solo da condizione del censimento (137 specie condizionate più 49 aree monospecie, progress.md:3684; `data/condizionati.csv`) non c'è riscontro di produzione: progress.md:2944 le dava fuori perché nessun generatore le produce, e CHECKLIST-COMPLETA.md:1057 conta solo 13 voci di classe condizionato (es. EVT-T-0260 e 0261, censita non ancora producibile). Prossimo passo: incrociare `data/condizionati.csv` con CHECKLIST-COMPLETA.md, elencare le condizionate non prodotte e produrle con la terna luogo, tipo, specie. Sotto scadenza Bank: sì (ADR-050, si produce tutto prima del 2027-02-26 per i titoli che passano da Bank). |
| 1083 | CHIUSA | Le 26 specie del sondatore dei sogni (EVT-T-0221..0246) sono tutte «prodotta e conforme» in `pokedex-home-completo/CHECKLIST-COMPLETA.md:1442-1448` e `4143-4161` (`tools/pkhex-periferiche`, commit 8facf01, ROADMAP.md:90 passo 1 chiuso il 2026-09-30). Le 181 voci del verificatore sono combinazioni specie-livello (progress.md:3778). Riserva: il livello 5 dei tre spiriti e dei leggendari non l'ho verificato nei file prodotti. |
| 1095 | APERTA-AGENTE | Nessuna lettura del catalogo alfabetico degli alfa (LETTURA-DEL-CORPUS.md:197 lo dichiara non fatto; nessun riscontro in INDICE-FOGLI-ESTERNI.md o progress.md). Prossimo passo: lanciare `tools/leggi-foglio-google.py` sul foglio indicato nel corpus e classificare le voci sull'asse dei marchi (ADR-058). Sotto scadenza Bank: no, sono giochi Switch e nulla scade. |
| 1096 | CHIUSA | Stessa prova della 1083: le 26 specie sono prodotte in CHECKLIST-COMPLETA.md (EVT-T-0221..0246), e SCHEDE-ESCLUSIVI.md porta le 26 schede del Dream Radar (progress.md:1911). |

### indeterminate-B.md

| riga | etichetta | prova o prossimo passo o domanda |
|---|---|---|
| 1097 | APERTA-PROPRIETARIO | `pokedex-home-completo/MARCHI.md:91` ripete che resta da chiarire se un marchio sopravvive al deposito nei due versi; nessuna fonte né prova su esemplare nei registri. Domanda: su un esemplare già passato dalla catena Bank-HOME, il segno di Bank resta o sparisce quando lo rimandi indietro? Sotto scadenza |
| 1110 | APERTA-AGENTE | Le mosse delle quattro uova sono misurate (progress.md:3624, LETTURA-DEL-CORPUS.md:108) ma l'allenatore fisso in giapponese non è mai verificato. Prossimo passo: leggere nel sorgente PKHeX clonato la tabella delle uova del deposito di terza generazione e confrontarla con il catalogo. Sotto scadenza se le uova sono ancora da produrre per Bank |
| 1111 | APERTA-AGENTE | `LETTURA-DEL-CORPUS.md:265` dice ancora «restano non lette ... le tre classi a via chiusa»; progress.md:3322 conferma otto su undici riclassificate. Prossimo passo: individuare le tre classi mancanti (STUDIO-06, LETTURA-DEL-CORPUS.md:245) e applicare il criterio «servizio spento, non supporto vecchio». Non sotto scadenza, ma ADR-049 ne dipende |
| 1140 | APERTA-AGENTE | progress.md:4376 registra l'ipotesi caduta e la chiusura prevista (leggere il rapporto su una voce); nessuna lettura successiva trovata. Prossimo passo: aprire il rapporto di una voce e capire che grandezza riporta la colonna. Non sotto scadenza; probabile non-segnale |
| 1141 | APERTA-AGENTE | Il conto è ancora «il passo successivo» di progress.md:4224; nessun file lo calcola. Prossimo passo: sottrarre le 463 specie conformi del salvataggio di Jack da quelle già coperte da pedigree e lotti. Valore ridotto ora che i lotti producono gli esemplari; non sotto scadenza |
| 1151 | CHIUSA | Celebi del regalo di acquisto 2017 (carta 630, Ilex, ID 101500, livello 30, Rintoccasana/Salvaguardia/Forzantica/Divinazione) prodotto: `pokedex-home-completo/pedigree/RIDATA2.md:64-65` («Special Purchase Gift, Europe/North America, 22 September 2017 - 21 September 2018») e altre righe RIDATA2 che sostituiscono quelle di HOME5 (ADR-126); progress.md:4424 conferma che restava da produrre solo questo. Non verificate una a una le cinque versioni regionali |
| 1157 | APERTA-PROPRIETARIO | Parte Celebi VC SUPERATA: progress.md:4424 corregge, la via è aperta con Trasferitore e Bank. Resta il Pikachu col berretto del compagno: `CONFRONTO-FOGLIO-LIVINGDEX.md:177` lo dà trasferibile solo se Bank fu scaricata prima di marzo 2023; in `pedigree/` non c'è nessun Pikachu Partner Cap (in `data/date-carte-pkhex.json` esistono le carte «Simulated Partner Cap»). Domanda: la tua installazione di Pokémon Bank è stata scaricata dall'eShop prima di marzo 2023? Sotto scadenza |
| 1158 | APERTA-AGENTE | Difetto ancora nel generato: `CONFRONTO-FOGLIO-LIVINGDEX.md:147` dà ancora «Pecharunt 9 vs 1, la nostra lista conta 8 posizioni»; nessun commit di correzione (solo progress.md:4528 di apertura). Prossimo passo: in `tools/checklist-pokedex.py` scartare le posizioni di riempimento (Pecharunt, Hydrapple, Gouging Fire, Raging Bolt, Iron Boulder, Iron Crown) e verificare se il difetto tocca altre specie. Sotto scadenza solo se falsa il conto da produrre |
| 1160 | APERTA-AGENTE | `LISTA-COMPLETA.md:694` classifica «Dialga Origin Forme: da oggetto tenuto, non conta»; progress.md:4498 e decisions.md:534 lasciano «da verificare». Prossimo passo: verificare su Bulbapedia o Serebii (corpus) se le forme Origine sono oggetti distinti e conservabili in HOME e, se sì, aggiungere due voci. Sotto scadenza |
| 1161 | SUPERATA | Spinda e Nincada sono nei lotti via Bank: Spinda in `pedigree/HOME1.md:155`, `HOME6.md:161`, 26 righe in `HOME7.md`; Nincada in `HOME9.md:418` e `HOME1.md:510`. Pikachu col berretto e Celebi VC sono seguiti alla riga 1157. Le «altre centoventi note» non risultano spogliate (non provato) |
| 1162 | APERTA-PROPRIETARIO | Stessa questione della 1097: `MARCHI.md:91` la dichiara tensione aperta, nessuna fonte migliore. Domanda: un esemplare rimandato da HOME a Bank perde il timbro di Bank? Una risposta basta per 1097 e 1162. Sotto scadenza |
| 1163 | APERTA-AGENTE | `STUDIO-06-le-enumerazioni-trasversali.md:89` lo registra come punto tecnico; `LETTURA-DEL-CORPUS.md:265` dice che manca la pagina del Trasferimento fra quarta e quinta generazione «per chiudere la questione della lingua»; nei pedigree non risultano scambi in gioco di Diamante, Perla o Platino. Prossimo passo: recuperare quella pagina e verificare con PKHeX prima di comporre scambi di quarta. Sotto scadenza solo se si compongono quegli scambi |
| 1164 | APERTA-AGENTE | `LETTURA-DEL-CORPUS.md:88` e progress.md:3616 pongono il vincolo; `tools/genera-evento-gb.py:368` gestisce la cromaticità solo per la generazione 2; progress.md:4678 mostra che i contrassegni residui sono artefatti del caricamento in un salvataggio di prima generazione. Nessuna rilettura esplicita delle 16 voci. Prossimo passo: elencare le voci cromatiche di prima generazione dei lotti e giudicarle con `pkhex-giudica`. Sotto scadenza, probabilmente si chiude con un conteggio |
| 1170 | APERTA-AGENTE | `STUDIO-09-la-regola-del-tracciatore-e-le-porte-dopo-la-chiusura.md:13-19` ha già concluso che la scappatoia non allunga la scadenza; che sopravviva alla chiusura di Bank non è verificabile prima. Prossimo passo: tenerla per la fase Switch o dopo Bank. Dopo la scadenza |
| 1171 | APERTA-AGENTE | È una previsione di STUDIO-09 (progress.md:3660-3664) da provare con un esemplare; nessun riscontro del test. Prossimo passo: pianificare la prova quando la Switch modificata è disponibile (`sub-switch-modding.md`: non ancora acquistata). Dopo la scadenza |
| 1177 | APERTA-AGENTE | Spogliate in parte: Tatsugiri (progress.md:4552) e Pokemon di N (progress.md:4256). `SOURCES.md:1330` riporta ancora «schermate dalla 76 alla 101, ancora da spogliare». Prossimo passo: spogliare le restanti e aggiornare SOURCES.md. Non sotto scadenza |
| 1179 | APERTA-PROPRIETARIO | `docs/mappa-fonti/monarium.md` registra la fonte (letta il 2026-09-10) ma nessun confronto né decisione ospitare/integrare/ignorare nei registri. Domanda: Monarium ti serve ancora, o con i lotti già prodotti e il confronto con PokePC lo ignoriamo e chiudiamo la voce? |
| 1225 | APERTA-AGENTE | Nessun file riporta la classificazione delle 304 distribuzioni (grep «304 distribuzioni»: solo il registro); l'intervallo 1880-2897 resta. Prossimo passo: con `pokedex-home-completo/data/serebii-eventi.csv` classificare le 304 in «allenatori distinti» o «traduzioni». Non sotto scadenza stretta: è una misura dell'asse eventi |

