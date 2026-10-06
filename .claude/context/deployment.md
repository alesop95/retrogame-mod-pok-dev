---
generated-from-commit: 8cc1798
generated-from-branch: main
generated-date: 2026-08-24
covers-paths: []
last-verified-commit: 8cc1798
---

# Deploy

Non applicabile allo stato attuale del progetto. Il `covers-paths` vuoto è deliberato ed è il modo previsto dal sistema per tenere una scheda in attesa invece di lasciare un buco nell'anatomia: `sync-context` la classifica come non applicabile e non esegue alcun diff su di essa, quindi non produce falsi segnali di drift.

Non c'è nulla da distribuire perché non c'è software. I tre sottoprogetti attivi producono file che restano locali per scelta, cioè dump di cartucce e backup di salvataggio, ed è documentato altrove perché non entrano nel version control.

Questa scheda diventerà applicabile se il sottoprogetto del ponte fra generazioni imboccasse una delle strade che producono un artefatto distribuibile. In quel caso il contenuto dipenderebbe dalla scelta: la strada del tool offline su PC porterebbe a un pacchetto o a un eseguibile per Windows, quella del ponte hardware a una ROM multiboot da caricare su Game Boy Advance, quella del microcontrollore a un firmware da flashare. Fino ad allora non c'è niente di onesto da scrivere qui.

## Modello di separazione

Deciso al gate della skill `separazione-ambienti` il 2026-09-29, ADR-090. La spiegazione di ogni forma, con le vicine scartate, sta in `docs/separazione-ambienti/GUIDA.md`, e le fonti in `docs/separazione-ambienti/FONTI.md`. Nessun ambiente software è in esercizio né previsto: gli strumenti girano sulla macchina di sviluppo e producono file, e l'unica «produzione» sono le cartucce e le console possedute.

Asse R, R0. La produzione è l'hardware fisico, e la rete di sicurezza è il ripristino: il backup del salvataggio originale in doppia copia su due percorsi distinti prima di ogni scrittura, e la rilettura confrontata byte per byte dopo, come vuole `rules/hardware-and-perimeter.md`. Il fatto che decide è che un secondo esemplare della produzione non esiste, e non si può ricomprare uguale. Il presidio del difetto tipico di R0, cioè il backup rimasto un proposito, è il registro `_notes/salvataggi/cartucce/LEGGIMI.md` con le impronte di ogni scrittura.

Asse P, forma degenere di P1. C'è la sola branch `main`, senza rami di lavoro né richieste di modifica; il presidio del passaggio è il commit manuale del proprietario dopo la lettura del diff, e l'hook `commit-msg` non è ancora istanziato. Se nascesse un secondo contributore, la forma da adottare è P1 per intero.

Asse D, D3. Le prove sui dati reali si fanno sempre su una copia estratta dal salvataggio della cartuccia, su richiesta esplicita e in doppia copia, mai sull'originale; le suite automatiche, come quella di `pokebridge`, usano dati costruiti. I salvataggi di terzi presi da internet si usano solo sul PC, mai sulla console.

Asse L, L1. Un albero solo, `E:/retrogame-mod-pok-dev` su `main`, verificato con `git worktree list` il 2026-09-29.

Rischi trasversali del catalogo. Nessuno dei cinque si applica nella forma descritta dalla norma, perché non c'è un servizio esposto, né un fornitore di identità, né uno staging, né un artefatto costruito per ambiente. Quello che resta vicino è l'ambiente previsto scritto come se esistesse: questa scheda dichiara che nessuno è previsto, e diventerà applicabile, nei termini detti sopra, solo se il ponte producesse un artefatto distribuibile.
