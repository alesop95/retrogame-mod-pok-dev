# La tesi

Documento lungo che spiega, partendo dallo zero assoluto, come si trasporta un dato strutturato fra due sistemi digitali che non sono stati progettati per parlarsi, usando i cinque sottoprogetti di questo repository come casi di studio. Non è un documento sui Pokemon: è un documento su rappresentazione, integrità, trasmissione e conversione dell'informazione, dove quei giochi sono il laboratorio.

## Come si compila

```
python tools/build-bibliography.py
latexmk -pdf tesi.tex
```

Il primo comando serve solo se la tabella delle fonti è cambiata, e il secondo va lanciato dalla cartella `tesi/`. Non serve BibTeX né biber: la bibliografia è un ambiente `thebibliography` generato, e `\cite` funziona con il solo nucleo di LaTeX. La ragione di questa scelta è scritta nel docstring del generatore, ed è che la TinyTeX di questa macchina è minimale e non installa pacchetti.

## Come si garantisce che nel PDF finisca tutto

È il vincolo che governa la struttura, ed è meccanico invece di essere una buona intenzione. Il requisito è che ogni riga dei documenti Markdown del progetto finisca da qualche parte nel PDF; l'organizzazione in parti, capitoli e paragrafi è invece libera. Un capitolo può raccogliere pezzi di documenti diversi e un documento può finire spezzato fra più capitoli: non serve alcuna corrispondenza uno a uno.

L'unità su cui il controllo lavora è la sezione, cioè un'intestazione Markdown con il testo che le sta sotto. Contare le righe sarebbe illusorio, perché una riga riscritta per un lettore diverso non ha lo stesso testo e nessun confronto meccanico potrebbe dire se il contenuto è passato. La sezione è abbastanza piccola da rendere il controllo utile e abbastanza stabile da poter essere nominata.

Ogni capitolo dichiara in testa che cosa reclama, con il commit a cui la dichiarazione è stata verificata.

```
% copre: docs/03-integrita-checksum.md
% copre: docs/01-fondamenta-salvataggio.md#il-supporto-fisico
% verificato-al-commit: f41fd4c
```

Da qui `python tools/check-thesis-coverage.py` ricava quattro verifiche. La copertura, cioè quali sezioni nessuno reclama, con il conteggio delle righe che restano fuori. Il drift, cioè quali capitoli dichiarano un commit anteriore all'ultima modifica dei documenti che coprono. Le citazioni orfane, cioè i riferimenti senza voce in bibliografia. E le fonti che nessun capitolo cita, che sono un avviso.

Una quinta verifica nasce dalla forma della dichiarazione: se un titolo di sezione viene riscritto, il suo slug cambia e la dichiarazione che lo nominava risulta sconosciuta. Non è un falso allarme, è il segnale che quel capitolo va riletto.

Quando una sezione risulta reclamata il controllo non garantisce che il suo contenuto sia stato reso fedelmente: quello resta lavoro umano. Garantisce che nessuna sezione sia stata dimenticata, che è il modo in cui il contenuto si perde davvero.

Le omissioni deliberate si dichiarano in `non-coperti.txt`, per documento intero o per singola sezione, sempre con il motivo. Un'esenzione senza motivo viene rifiutata.

## Che cosa resta da distribuire

Alla verifica corrente il corpus da coprire è di 1698 righe di contenuto in 29 documenti, e la copertura è al dieci per cento. Le 264 sezioni scoperte si ripartiscono così, e la ripartizione dice dove sta il lavoro vero.

| documento | sezioni scoperte |
|---|---|
| `HANDOFF_frlg-ldn-trade.md` | 50 |
| `HANDOFF_progetto_3DS.md` | 25 |
| `HANDOFF_progetto_smeraldo.md` | 20 |
| `SOURCES.md` | 15 |
| `DATA-FORMATS_Gen1-Gen2-Gen3.md` | 13 |
| le note di `docs/` | 134 in tutto |
| il resto | 7 |

I tre handoff da soli sono 95 sezioni, cioè più di un terzo del lavoro, e sono materiale di natura diversa dalle note di studio: procedure operative scritte per chi ha l'hardware in mano. Il loro posto naturale nel documento è la parte sui cinque casi, non i capitoli teorici.

Un gruppo non compare in quella tabella ed è già risolto: le quaranta note di `docs/fonti/` sono generate dalla tabella delle fonti, e la bibliografia del PDF nasce dalla stessa tabella. Sono 1369 righe coperte per costruzione.

## Struttura e stato

Le parti sono sei più una parte zero. Accanto a ciascun capitolo previsto sta il documento che deve coprire, così che la corrispondenza sia leggibile prima che il capitolo esista.

### Parte zero: i fondamenti, senza dare nulla per scontato

| Capitolo | Copre | Stato |
|---|---|---|
| Prefazione, come si legge | `docs/31-glossario.md` | scritto |
| 1. Bit, numeri e la loro rappresentazione | `docs/02-numeri-e-bit.md` | da scrivere |
| 2. Memoria, indirizzi e supporti | `docs/01-fondamenta-salvataggio.md` | da scrivere |
| 3. Come un sistema si accorge che un dato è rotto | `docs/03-integrita-checksum.md` | scritto, è il capitolo campione |

### Parte prima: la rappresentazione

| Capitolo | Copre | Stato |
|---|---|---|
| 4. Testo che non è ASCII | `docs/05-testo-e-charmap.md` | da scrivere |
| 5. Cifrare con uno XOR e una permutazione | `docs/04-cifratura-gen3.md` | da scrivere |
| 6. La referenza byte per byte | `DATA-FORMATS_Gen1-Gen2-Gen3.md` | da scrivere |

### Parte seconda: identità e conversione

| Capitolo | Copre | Stato |
|---|---|---|
| 7. Che cosa identifica un'entità | `docs/06-identita-pokemon.md` | da scrivere |
| 8. La conversione come quantizzazione e come vincolo | `docs/07-conversione-vincoli.md` | da scrivere |

### Parte terza: la trasmissione

| Capitolo | Copre | Stato |
|---|---|---|
| 9. Un canale sincrono con un solo clock | `docs/08-cavo-link.md` | da scrivere |
| 10. Stallo e controllo di flusso fra protocolli asimmetrici | `docs/08-cavo-link.md` | da scrivere |
| 11. Il lato Game Boy Advance | `docs/10-multiboot-hardware.md` | da scrivere |
| 12. Il wireless locale, e un kernel come libreria | `docs/11-wireless-locale-e-ponte-switch.md` | da scrivere |

### Parte quarta: la sicurezza

| Capitolo | Copre | Stato |
|---|---|---|
| 13. Eseguire codice dove dati e istruzioni non si distinguono | `docs/09-esecuzione-codice.md` | da scrivere |
| 14. Il dato ricevuto come superficie di attacco | `docs/09-esecuzione-codice.md` | da scrivere |

### Parte quinta: la realizzazione

| Capitolo | Copre | Stato |
|---|---|---|
| 15. Stratificare il codice | `docs/20-architettura-codice.md` | da scrivere |
| 16. Verificare per proprietà invece che per casi | `docs/21-collaudo.md` | da scrivere |
| 17. Le quattro strade e il loro costo | `docs/30-opzioni-implementative.md` | da scrivere |

### Parte sesta: i cinque casi

| Capitolo | Copre | Stato |
|---|---|---|
| 18. Il ponte fra generazioni | schede e referenza | da scrivere |
| 19. L'inventario corrotto di Smeraldo | scheda del track | da scrivere |
| 20. Il modding della console e il dump | scheda del track | da scrivere |
| 21. Lo scambio con la Switch | `docs/11`, scheda del track | da scrivere |
| 22. L'automazione, e i suoi limiti | nota di studio del track | da scrivere |
| 23. Quando la fonte non si raggiunge | `docs/24-fonti-di-community.md` | da scrivere |

## Che cosa si versiona

Il `.tex` è la fonte e si versiona, come il preambolo, questo README, le esenzioni e la bibliografia generata. Il PDF e tutti gli ausiliari sono derivati e sono esclusi dal `.gitignore`, per la politica sui binari di ADR-005: si rigenerano con `latexmk`.

La bibliografia generata resta tracciata, ed è una scelta coerente con quella fatta per le tabelle dei caratteri sotto `data/`: il derivato si versiona insieme al suo generatore, così che un clone possa compilare senza dover prima rigenerare, e una modifica al derivato si veda nel diff. La differenza fra un derivato che si versiona e uno che no, in questo progetto, è se sia testo leggibile e diffabile: la bibliografia lo è, il PDF no.
