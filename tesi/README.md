# La tesi

Documento lungo che spiega, partendo dallo zero assoluto, come si trasporta un dato strutturato fra due sistemi digitali che non sono stati progettati per parlarsi, usando i cinque sottoprogetti di questo repository come casi di studio. Non è un documento sui Pokemon: è un documento su rappresentazione, integrità, trasmissione e conversione dell'informazione, dove quei giochi sono il laboratorio.

## Come si compila

```
python tools/build-bibliography.py
latexmk -pdf tesi.tex
```

Il primo comando serve solo se la tabella delle fonti è cambiata, e il secondo va lanciato dalla cartella `tesi/`. Non serve BibTeX né biber: la bibliografia è un ambiente `thebibliography` generato, e `\cite` funziona con il solo nucleo di LaTeX. La ragione di questa scelta è scritta nel docstring del generatore, ed è che la TinyTeX di questa macchina è minimale e non installa pacchetti.

## Come si resta di pari passo con il resto del progetto

È il vincolo che governa tutta la struttura, ed è meccanico invece di essere una buona intenzione. Ogni capitolo dichiara in testa, come commenti LaTeX, quali documenti del progetto copre e a quale commit è stato verificato contro di essi.

```
% copre: docs/03-integrita-checksum.md
% verificato-al-commit: 3f1c9b3
```

Da qui `python tools/check-thesis-coverage.py` ricava quattro verifiche: i capitoli il cui documento coperto è cambiato dopo la verifica dichiarata, i documenti che nessun capitolo copre, le citazioni che non corrispondono ad alcuna voce di bibliografia, e le fonti che nessun capitolo cita. Le prime tre fanno fallire il controllo, la quarta è un avviso. È lo stesso meccanismo che `sync-context` applica alle schede di contesto, con la stessa logica: un documento che descrive un'area senza dichiararla resta verde mentre invecchia, e il modo di impedirlo è un confronto che fallisce.

Quando un documento resta fuori perimetro di proposito, va dichiarato in `non-coperti.txt` con il motivo. Un'esenzione senza motivo viene rifiutata.

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
