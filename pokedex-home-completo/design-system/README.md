# Il design system della collezione

> Documento autorato, nato il 2026-11-04 su richiesta del proprietario (ADR-110), che vuole per i documenti della collezione e per i PDF stampabili un design system proprio, retrò e ispirato a Ken Sugimori, costruito sulla suite ArtCraft installata in locale. È un'eccezione voluta al design system di account, registrata in ADR-110. Serve anche ad ADR-111, che chiede un pedigree per ogni esemplare nella documentazione e nella stampa.

## Da dove viene lo stile

Il riferimento sono le illustrazioni ad acquerello che Ken Sugimori disegnò per i primi giochi e la stampa giapponese degli anni Novanta che le accompagnava, cioè guide e libri del Pokédex: carta chiara, inchiostro caldo invece del nero pieno, colori stesi ad acquerello e mai saturi, forme tonde. A questo si aggiunge un solo richiamo al Game Boy, il carattere a punti dei numeri di Pokédex, e i due verdi dello schermo originale fra i colori di stato. Nessuna illustrazione ufficiale e nessun logo entrano nel design system: le sole immagini sono le miniature che `tools/stampa-collezione.py` ricava dalla raccolta locale del proprietario, come già prima.

## La fonte unica e i file che se ne ricavano

La fonte è `tokens.json`, in questa cartella, e si modifica solo lì. `tools/design-system.py genera` ne ricava due file, e `--check` esce con 1 se uno dei due non corrisponde più ai token.

```
pokedex-home-completo/design-system/tokens.json            la fonte: caratteri, colori, generazioni, stati, geometria, dimensioni
pokedex-home-completo/design-system/collezione-stile.tex   generato, il preambolo per LuaLaTeX del catalogo e dei pedigree
.claude/craft-stile.json                                   generato, lo stile che craft-documento.py --stile auto applica
```

Il primo serve alla catena che esiste già, cioè `tools/stampa-collezione.py` con LuaLaTeX, che dal quarto passo di ADR-110 compone i pedigree. Il secondo serve ai documenti e alle slide prodotti con WordCraft e DeckCraft, attraverso `craft-documento.py --stile auto`, che legge per primo lo stile del progetto.

## I caratteri

Sono cinque ruoli e quattro famiglie, tutte con licenza SIL Open Font License 1.1, dal repository dei Google Fonts al commit fissato nei token. I titoli sono in M PLUS Rounded 1c, un bastone tondo che ricorda la stampa giapponese del periodo. Il testo corrente è in Zen Old Mincho, un carattere con grazie di tradizione giapponese. I dati del pedigree sono di nuovo in M PLUS Rounded 1c, nel peso normale, perché in una tabella fitta un bastone si legge meglio di un carattere con grazie. I numeri di Pokédex sono in DotGothic16, il carattere a punti. Gli identificativi tecnici, cioè impronte e valori esadecimali, sono in IBM Plex Mono. Le prime due famiglie contengono i caratteri giapponesi, quindi i nomi degli esemplari giapponesi si compongono senza ripiego; per il coreano e il cinese resta il ripiego sui caratteri di sistema che il catalogo usava già.

I file non entrano in Git e non si installano nel sistema. `tools/design-system.py caratteri` li scarica in `_notes/design-system/caratteri/` e verifica l'impronta SHA-256 registrata nei token; LuaLaTeX li carica da quella cartella per percorso. Le applicazioni Craft invece cercano i caratteri per nome fra quelli installati: finché il proprietario non li installa per il suo utente, un documento di WordCraft ripiega su un carattere di sistema. L'agente non li installa di sua iniziativa.

## I colori

La carta è un crema chiaro, `F8F3E6`, e si usa come fondo delle schede e non della pagina, così che la stampa non consumi inchiostro sui margini. Il testo è un inchiostro caldo, `2B2622`, con una seppia `6E5E4E` per le etichette e un filetto `B9AA92` per i bordi. Gli accenti ad acquerello sono un rosso `B8433A`, che è il colore dei titoli, un blu `3F6A94` e un giallo `E0B04A`; i due verdi del Game Boy sono `306230` e `8BAC0F`. Ogni generazione ha il suo colore, che compare solo come striscia sul bordo sinistro della scheda: rosso per la prima, oro per la seconda, smeraldo per la terza, blu perla per la quarta, grigio scuro per la quinta, blu per la sesta, arancio per la settima. Gli stati dell'esemplare hanno ciascuno un colore: da produrre in rosso, in copia in giallo, in Bank in blu, in HOME nel verde scuro del Game Boy.

## La geometria e la scheda

Il margine sinistro resta di 26 millimetri per i fori del quaderno ad anelli, come nel catalogo di prima. Le schede hanno gli angoli tondi di 2,2 millimetri, un filetto di 0,6 punti e la striscia della generazione di 3,5 punti. La scheda di un esemplare, cioè l'unità del pedigree, è l'ambiente `DSscheda` del preambolo: la miniatura nella sua finestra bianca a sinistra, a destra il nome, il numero di Pokédex a punti, il bollino dello stato e il racconto della provenienza, e sotto la griglia dei campi. I campi sono quelli fissati da ADR-111.

## Il campionario

`tools/design-system.py campionario` compone in `_notes/design-system/campionario.pdf` una pagina con i caratteri, i colori, le generazioni e una scheda di pedigree d'esempio, il Mew di terza generazione del primo giro. La pagina si guarda con `pdfcraft-cli render campionario.pdf --page 1 --out campionario.png`, ed è stata guardata così il 2026-11-04, con PdfCraft 0.18.1. Il campionario sta fuori da Git perché contiene una miniatura.
