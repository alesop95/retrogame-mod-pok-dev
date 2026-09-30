# Le copie dei salvataggi per HOME, divise per gruppi

> Documento autorato, aggiornato a ogni giro di lavoro che cambia una copia o il suo stato. Nasce il 2026-09-30 su richiesta del proprietario, che vuole il riepilogo delle copie per gruppo ogni volta, con quello che è già passato a HOME e con ciò che le fonti aggiungono. Le copie si scrivono con `tools/pkhex-scrivi-salvataggio` secondo ADR-092, e stanno fuori da Git sotto `_notes/salvataggi/prove/`; accanto a ciascuna c'è il suo `main.rapporto.json`, con box, posto e impronta di ogni esemplare. La sostituzione delle copie sulla console si fa tutta alla fine, quando i lotti sono completi e si passa a HOME, e i passi si danno al proprietario in quel momento.

## Stato al 2026-09-30

Nessun esemplare è ancora passato alla banca o al deposito.

| Gruppo | Copia | Gioco | Esemplari | Stato |
|---|---|---|---|---|
| per HOME | `per-home/oras-giro-1/main` | Rubino Omega, salvataggio d'appoggio europeo | 930 | pronta, non trasferita |
| per HOME | `per-home/oras-giro-2/main` | Rubino Omega, salvataggio d'appoggio europeo | 682 | pronta, non trasferita |
| per HOME | `per-home/luna-giro-1/main` | Luna del proprietario | 147 | pronta, non trasferita |
| decisione finale, con la community | `a-parte/oras-macchine-nascoste/main` | Rubino Omega | 31 | pronta, in attesa di decisione |
| decisione finale, con la community | `a-parte/luna-eventi-da-cartuccia/main` | Luna del proprietario | 121 | pronta, in attesa di decisione |
| da fare | Ultraluna, da un salvataggio della rete da adattare | Ultraluna | 3 | da preparare |
| da provare a parte | Luna con regione giapponese | Luna | 13 | da preparare |

Il gruppo per HOME conta 1759 esemplari. Il gruppo della decisione finale conta 152 esemplari. Per le 31 voci con macchina nascosta la catena ufficiale le avrebbe rifiutate, e ADR-046 le teneva in attesa. Per i 122 eventi di Game Boy da cartuccia, cioè i 121 della copia più il Mew `EVT-2-0006`, PKHeX all'apertura di un salvataggio di settima generazione li giudica non legali, perché nell'epoca della Console Virtuale quegli eventi non esistono. Il proprietario ha deciso che per entrambi i gruppi si decide insieme alla fine, e che si chiede prima alla community.

## Che cosa manca, e perché

Tre esemplari esistono solo in Ultrasole e Ultraluna: Poipole, Zeraora e il Rockruff con Mentelocale. Luna non li conosce, e scritti lì il gioco li mostra corrotti. Il proprietario ha ritrovato una copia di Ultraluna, e la via decisa è adattare un salvataggio della rete; quello disponibile, `main (2)`, è di Ultrasole, quindi prima va verificato che Ultraluna lo accetti.

Tredici esemplari di Game Boy in lingua giapponese chiedono un salvataggio di settima generazione di console giapponese. Sono i nove doni di Pokémon Stadium giapponese, i due di Stadium 2 giapponese, il Phanpy `EVT-2-0146` e il Mew GF giapponese. Si proveranno a parte con una copia di Luna a regione giapponese.

Il Mew `EVT-2-0006` è contestato per cromaticità in ogni contesto, e resta da capire.

## Registro delle modifiche

- 2026-09-30: prima stesura, dalle copie dell'ottava parte del work log.
