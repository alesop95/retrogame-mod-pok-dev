# Le copie dei salvataggi per HOME, divise per gruppi

> Documento autorato, aggiornato a ogni giro di lavoro che cambia una copia o il suo stato. Nasce il 2026-09-30 su richiesta del proprietario, che vuole il riepilogo delle copie per gruppo ogni volta, con quello che è già passato a HOME e con ciò che le fonti aggiungono. Le copie si scrivono con `tools/pkhex-scrivi-salvataggio` secondo ADR-092, e stanno fuori da Git sotto `_notes/salvataggi/prove/`; accanto a ciascuna c'è il suo `main.rapporto.json`, con box, posto e impronta di ogni esemplare. La sostituzione delle copie sulla console si fa tutta alla fine, quando i lotti sono completi e si passa a HOME, e i passi si danno al proprietario in quel momento.

## Stato al 2026-09-30, sera

Nessun esemplare è ancora passato alla banca o al deposito. Ogni copia è stata ricontrollata nello stesso contesto in cui PKHeX apre il salvataggio.

| Gruppo | Copia | Gioco | Esemplari | Stato |
|---|---|---|---|---|
| per HOME | `per-home/oras-giro-1/main` | Rubino Omega, appoggio europeo | 930 | pronta, non trasferita |
| per HOME | `per-home/oras-giro-2/main` | Rubino Omega, appoggio europeo | 682 | pronta, non trasferita |
| per HOME | `per-home/oras-giro-3/main` | Rubino Omega, appoggio europeo | 914 | pronta, non trasferita |
| per HOME | `per-home/luna-giro-1/main` | Luna del proprietario | 93 | pronta, non trasferita |
| per HOME | `per-home/ultraluna-giro-1/main` | Ultraluna, appoggio europeo dalla rete | 575 | pronta, non trasferita |
| decisione finale, con la community | `a-parte/oras-macchine-nascoste/main` | Rubino Omega | 36 | pronta, in attesa di decisione |
| decisione finale, con la community | `a-parte/luna-eventi-da-cartuccia/main` | Luna del proprietario | 121 | pronta, in attesa di decisione |
| da provare a parte | Luna con regione giapponese | Luna | 14 | da preparare |
| generati, senza copia | `_notes/lotti/lotto-eventi-switch-scelta/` | formati Switch: una carta di dono per carta, una distribuzione per tipo, specie e forma | 701 | generati il 2026-10-01 e conformi; entrano in un gioco solo con una console Switch modificata, poi in HOME, che non ha scadenza. L'archivio completo di 29449 righe d'incontro sta in `lotto-eventi-switch-completo/` e non va in HOME |

Il gruppo per HOME conta 3194 esemplari, 0 non legali nel contesto di PKHeX, 0 specie che il gioco non conosca e 0 file ripetuti fra una copia e l'altra. Il gruppo della decisione finale conta 158 esemplari: le 36 voci con macchina nascosta, cioè le 31 di prima, il Phione del Ranch con Surf, due Pokéwalker del secondo tempo e due Suicune Ombra di Colosseum con Surf; e i 122 eventi di Game Boy da cartuccia, cioè i 121 della copia più il Mew `EVT-2-0006`. Il proprietario ha deciso che per entrambi si decide alla fine, dopo aver chiesto alla community.

Il giro 3 di Rubino Omega e la copia di Ultraluna sono il secondo tempo della collezione, cioè le voci sotto scadenza oltre la prima di ogni specie: 742 doni di sesta generazione e 167 periferiche nel primo, i 3 esclusivi di Ultrasole e Ultraluna e 572 doni di settima generazione nella seconda.

## La roadmap dei passaggi a HOME

Scritta il 2026-09-30 con il proprietario, che vuole fare i passaggi insieme all'agente, in ordine logico e cronologico, e con la sostituzione delle copie sulla console tutta alla fine, quando i lotti sono completi. Il tratto dalla banca in poi resta del proprietario e fuori dall'assistenza, come stabilisce `rules/hardware-and-perimeter.md`: questa roadmap dice che cosa passa e quando, non come si usa la banca.

Due vincoli di capienza la governano. Il deposito con il piano a pagamento tiene 6000 esemplari, 9000 dalla versione 4.1.0 di ottobre 2026, e il gruppo per HOME più quello della decisione finale e i giapponesi fanno 3366: il deposito non è un vincolo. La banca tiene 100 box da 30, cioè 3000 esemplari, meno dei 3194 del gruppo per HOME, quindi la banca va svuotata verso il deposito almeno una volta a metà; il dato è verificato il 2026-10-01 su Bulbapedia, nella copia della Wayback Machine dell'8 settembre 2026, registrata in `SOURCES.md`.

Prima di cominciare, tre condizioni: l'esportazione di Discord letta, senza che smentisca nulla; il piano a pagamento del deposito attivo; la copia di riserva con Checkpoint delle partite vere del proprietario, che per Rubino Omega esiste già, `20260930-bef-giro1`.

Il passo 1 è la prova pilota con un solo giro, Rubino Omega giro 1, 930 esemplari: ripristino della copia, controllo dei box in gioco, passaggio alla banca, controllo in banca, passaggio al deposito, controllo nel deposito. Se il deposito rifiuta o segnala qualcosa ci si ferma, e si capisce prima di continuare. È il solo passo che mette alla prova tutta la catena con esemplari del progetto.

Il passo 2 sono i giri 2 e 3 di Rubino Omega, 682 e 914 esemplari, uno dopo l'altro, con la banca che resta sotto i 3000; poi il passaggio al deposito.

Il passo 3 sono Luna, 93 esemplari, e Ultraluna, 575: ognuna con il proprio ripristino, poi la banca, poi il deposito. Dopo questo passo il gruppo per HOME, 3194 esemplari, è tutto nel deposito.

Dentro il passo 3, deciso dal proprietario il 2026-10-02, ci sono i codici QR del Pokédex: dopo il ripristino della copia di Ultraluna e prima del suo passaggio alla banca, lo Scanner QR del gioco registra come viste le forme cromatiche dei Pokémon bloccati, la banca le copia nel proprio Pokédex e il deposito le riceve al passaggio successivo. Non sono esemplari e non cambiano i conti di questa pagina. I codici e la procedura passo per passo stanno nella pagina locale `_notes/qr-pokedex/index.html`, che si apre nel browser: 10 codici indispensabili il primo giorno, poi la verifica nel Pokédex del deposito con il filtro dei cromatici, poi, se la verifica riesce, circa 83 consigliati a 10 al giorno.

Il passo 4 è la prova dei 14 esemplari giapponesi di Game Boy, con una copia di Luna a regione giapponese, da preparare, e da provare prima con un solo esemplare.

Il passo 5 è il gruppo della decisione finale, 158 esemplari, dopo aver chiesto alla community, in un caricamento a parte.

Alla fine, il ripristino delle partite vere del proprietario dalle copie di riserva di Checkpoint.

Il catalogo stampabile dell'intera collezione si compone con `tools/pkhex-elenco-copie` e `tools/stampa-collezione.py` e sta in `_notes/stampa/collezione.pdf`, fuori da Git perché è un derivato; si rigenera a ogni cambiamento delle copie, e dopo i passaggi dirà anche che cosa è già nel deposito.

## Che cosa manca, e perché

Poipole, Zeraora e il Rockruff con Mentelocale esistono solo in Ultrasole e Ultraluna, e Luna li mostrava corrotti. Dal 2026-09-30 sono nella copia di Ultraluna, fatta da un salvataggio di console europea trovato in rete dal proprietario, `_notes/salvataggi/terzi/main-ultraluna`.

Quattordici esemplari di Game Boy in lingua giapponese chiedono un salvataggio di settima generazione di console giapponese. Sono i nove doni di Pokémon Stadium giapponese, i due di Stadium 2 giapponese (`EVT-2-0000` e `EVT-2-0001`), il Phanpy `EVT-2-0146`, il Mew GF giapponese e il Mew delle manifestazioni giapponesi (`EVT-1-0010`, allenatore マクハリ). Si proveranno a parte con una copia di Luna a regione giapponese.

Il Mew `EVT-2-0006` è contestato per cromaticità in ogni contesto, e resta da capire.

## Registro delle modifiche

- 2026-09-30: prima stesura, dalle copie dell'ottava parte del work log.
- 2026-09-30, sera: aggiunti il giro 3 di Rubino Omega e la copia di Ultraluna con il secondo tempo; il gruppo delle macchine nascoste sale a 34.
- 2026-09-30, notte: chiuso il secondo tempo; nel giro 3 il Victini del Passo Libertà e quattro Ombre di Colosseum, fra le macchine nascoste due Suicune con Surf, fra i giapponesi il Mew delle manifestazioni.
- 2026-09-30, notte: aggiunta la roadmap dei passaggi a HOME e il catalogo stampabile.
- 2026-09-30, notte: tolti i doppioni. Luna scende da 147 a 93: portava, convertiti, i 45 doni di sesta generazione già in Rubino Omega e i 9 Greninja con Morfosi già in Ultraluna.
