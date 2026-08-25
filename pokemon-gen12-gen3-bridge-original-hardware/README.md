# Sottoprogetto: ponte Pokemon da Gen 1 e 2 verso Gen 3 su hardware originale

Costruire un trasferimento di Pokemon dalle generazioni 1 e 2 alla generazione 3, che ufficialmente non e' mai esistito perche' Nintendo non lo ha mai fornito. E' l'unico dei quattro sottoprogetti destinato a diventare software vero: gli altri tre sono runbook operativi su hardware fisico.

## Che cosa c'e' in questa cartella

Il documento di riferimento e' `DATA-FORMATS_Gen1-Gen2-Gen3.md`, che descrive byte per byte le strutture Pokemon, i salvataggi, le codifiche di testo, gli indici di specie, il problema della conversione e il protocollo del cavo Link per tutte e tre le generazioni. Ogni sua affermazione e' verificata sul disassemblato o sulla decompilazione del gioco, non sull'enciclopedia, e la sezione 11 dichiara cosa resta aperto e perche'.

In `data/` stanno le tabelle di codifica dei caratteri generate, e in `tools/extract_charmaps.py` il programma che le genera dai charmap dei disassemblati. Le tabelle non si modificano a mano: si rigenerano, e il generatore si rifiuta di scrivere se le sentinelle di controllo non tornano. Il motivo di questa scelta e' che le fonti secondarie sbagliavano quelle tabelle in due punti, con un errore che produce nomi plausibili e sbagliati.

Non esiste piu' un handoff di ricerca: la sua conoscenza e' stata verificata e assorbita fra questo documento e le note di studio, per ADR-013.

## Dove trovare il resto

| Cosa cerchi | Dove sta |
|---|---|
| offset, campi di bit, algoritmi | `DATA-FORMATS_Gen1-Gen2-Gen3.md`, in questa cartella |
| perche' le cose stanno cosi', spiegato per livelli | `docs/index.md`, in particolare le note da 01 a 10 |
| come si stratifica il codice e come si collauda | `docs/20-architettura-codice.md` e `docs/21-collaudo.md` |
| le quattro opzioni di ADR-008 e il loro costo reale | `docs/30-opzioni-implementative.md` |
| le fonti, con il livello di affidabilita' di ciascuna | `SOURCES.md` alla radice, colonna BRI |
| a che punto e' il track e qual e' il prossimo passo | `.claude/context/sub-gen12-gen3-bridge.md` |

Lo stato canonico del track vive nella scheda, e il quadro d'insieme di tutti i sottoprogetti in `.claude/memory/index.md`. Questo file dice cos'e' il sottoprogetto; quelli dicono a che punto e'.

## Due avvertenze prima di iniziare

Il trasferimento e' a senso unico e distruttivo sulla sorgente, cioe' il Pokemon viene rimosso dal gioco di partenza, e modifica entrambi i salvataggi: il backup in doppia copia richiesto da `.claude/rules/hardware-and-perimeter.md` non e' prudenza, e' il presupposto.

La verifica finale del ponte richiede hardware reale, perche' nessun emulatore riproduce l'interazione fra Game Boy e Game Boy Advance. Il collegamento fra due Game Boy invece si emula, quindi tutto il lato protocollo si collauda senza cartucce, come spiegato in `docs/21-collaudo.md`.
