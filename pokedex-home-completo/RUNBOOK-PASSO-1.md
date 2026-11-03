# Passo 1: la prova pilota con Rubino Omega, giro 1, 930 esemplari

> Documento autorato, scritto il 2026-11-03 su richiesta del proprietario, che voleva ogni passo detto in modo inequivocabile, con la verifica di PKHeX compresa. Applica `rules/hardware-and-perimeter.md`: prima di ogni scrittura sulla console una copia di riserva in due copie su due percorsi distinti e verificata, e dopo ogni scrittura una rilettura confrontata sui byte. I passi segnati «agente» li esegue l'agente, con la scheda SD inserita nel PC. Il tratto da Pokémon Bank in poi resta del proprietario e fuori dall'assistenza, come dice la stessa regola: questo documento si ferma prima della banca e riprende con ciò che il proprietario riferisce dopo.

## Che cosa si porta e in che stato è

La copia è `_notes/salvataggi/prove/per-home/oras-giro-1-fin2/main`, la prima della tabella di `COPIE-PER-HOME.md`. È di Rubino Omega (versione OR), pesa 483.328 byte e ha SHA-256 che comincia con `5e8779e61b160cfa`. Contiene 930 esemplari in 31 box pieni da 30, giudicati tutti conformi il 2026-11-03 con la libreria 26.10.18 nel contesto del salvataggio, in `_notes/lavoro/giudizi-copie/dopo-bfe89c7.json`. Per il controllo a vista: box 1 posto 1 è Mew, livello 10, allenatore MYSTRY; box 1 posto 2 è Jirachi, livello 5, allenatore WISHMKR; box 31 posto 30 è Keldeo, livello 15, allenatore SMR2012.

Sulla console, al 2026-09-30, Rubino Omega porta ripristinata una copia superata, `scrittura-oras/giro-1`, che non va in banca. La partita vera del proprietario è la copia di riserva di Checkpoint `20260930-bef-giro1`, nella cartella `/3ds/Checkpoint/saves/0x011C4 Pokémon Omega Ruby/` della scheda SD. Luna porta la prima copia di Luna, quella difettosa, che non va in banca nemmeno lei: in questo passo Luna non si apre.

## A. Con la scheda SD nel PC

1. Proprietario: spegni il 3DS del tutto, tenendo premuto il tasto di accensione e scegliendo Spegni, non la modalità riposo.
2. Proprietario: togli la scheda SD, inseriscila nel lettore del PC e dimmi la lettera di unità che Windows le assegna.
3. Agente: copio l'intera cartella `/3ds/Checkpoint/saves/` della SD in due posti distinti, `E:\retrogame-mod-pok-dev\_notes\salvataggi\console\sd-checkpoint-2026-11-03\` e `J:\backup-sd-3ds\2026-11-03\`. Calcolo lo SHA-256 di ogni file sulla SD e nelle due copie, e mi fermo se un'impronta non coincide. Ti dico l'impronta di `20260930-bef-giro1/main`, che è la tua partita vera.
4. Agente: creo sulla SD la cartella `/3ds/Checkpoint/saves/0x011C4 Pokémon Omega Ruby/20261103-giro1/` e ci copio la copia del giro 1 con il nome `main`. Rileggo il file dalla SD e verifico che lo SHA-256 cominci con `5e8779e61b160cfa`.
5. Proprietario: espelli la SD in sicurezza da Windows, con l'icona «Rimozione sicura dell'hardware», poi rimettila nel 3DS.

## B. Sulla console

6. Proprietario: accendi il 3DS e avvia Checkpoint dal menu HOME.
7. Proprietario: scegli Pokémon Omega Ruby. Prima di tutto fai una copia di riserva dello stato attuale: premi Backup e dai il nome `20261103-prima`. È la copia superata, ma la regola vuole una copia di riserva prima di ogni scrittura, senza eccezioni.
8. Proprietario: nell'elenco delle copie di Pokémon Omega Ruby seleziona `20261103-giro1`, premi Restore e conferma.
9. Proprietario: esci da Checkpoint e avvia Rubino Omega. Carica la partita e, senza giocare né salvare, apri il PC dei box. Controlla tre cose: box 1 posto 1 è Mew livello 10, box 1 posto 2 è Jirachi livello 5, box 31 posto 30 è Keldeo livello 15, e i box da 1 a 31 sono pieni. Se una delle tre non torna, fermati e dimmelo.
10. Proprietario: esci dal gioco senza salvare, dal menu HOME, chiudendo il software.
11. Proprietario: avvia di nuovo Checkpoint, scegli Pokémon Omega Ruby, premi Backup e dai il nome `20261103-rilett1`. È la rilettura di ciò che la console ha davvero scritto.

## C. La verifica, di nuovo con la SD nel PC

12. Proprietario: spegni il 3DS del tutto, metti la SD nel PC e dimmi la lettera di unità.
13. Agente: confronto lo SHA-256 di `20261103-rilett1/main` con quello della copia del giro 1. Devono coincidere byte per byte. Se non coincidono, ma la differenza sta solo nei campi che il gioco riscrive all'apertura, lo misuro e te lo dico prima di andare avanti.
14. Agente: giudico `20261103-rilett1/main` con `tools/pkhex-elenco-copie`, cioè con la libreria PKHeX 26.10.18 nel contesto del salvataggio. Devono risultare 930 esemplari, 930 conformi, negli stessi box e posti del giudizio del 2026-11-03. Copio anche questa rilettura nelle due cartelle di riserva del punto 3.
15. Proprietario: espelli la SD in sicurezza e rimettila nel 3DS.

## D. Da qui il tratto è tuo

16. Proprietario: il passaggio dalla console a Pokémon Bank, il controllo in banca, il passaggio a Pokémon HOME e il controllo nel deposito sono tuoi, e l'assistenza non li copre (`rules/hardware-and-perimeter.md`). Se la banca o HOME rifiutano o segnalano un esemplare, fermati e non ripetere: dimmi quale e con quale messaggio, e lo confronto con il giudizio di PKHeX.
17. Proprietario: alla fine dimmi quanti esemplari risultano in HOME. Li registro in `COPIE-PER-HOME.md`, e solo allora si passa al giro 2. La partita vera di Rubino Omega torna sulla console soltanto al passo 6 della roadmap, dopo l'ultimo giro.
