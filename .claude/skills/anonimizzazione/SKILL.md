---
name: anonimizzazione
description: >
  Impedisce che dati che identificano persone reali finiscano in un file pubblicabile del
  repository, che è pubblico. Si carica quando si sta per scrivere in un file tracciato un nome
  e cognome reale, un indirizzo di posta personale, un indirizzo IP o fisico di una macchina
  reale; quando si salva una chat incollata dal proprietario; quando si prepara un commit che
  tocca documentazione; e quando il controllo `tools/Test-Anonymization.py` segnala un
  riscontro. Stabilisce che cosa si sostituisce e con quale segnaposto, dove vive la mappa
  privata, e che cosa fare di un valore reale già pubblicato.
---

## Che cosa fa questa skill

La norma sta per intero in `RIFERIMENTO.md`, accanto a questo file, e va letta prima di operare: qui c'è solo la porta d'ingresso. Il principio è che ciò che entra in un file tracciato resta nella storia git anche dopo una correzione, quindi un valore reale si sostituisce con un segnaposto prima di scriverlo, e la corrispondenza fra segnaposto e valore vive soltanto nel livello privato `_notes/`, ignorato da git.

## Quando si carica

Prima di scrivere in un file tracciato un nome reale, una casella personale, un indirizzo di rete o fisico di una macchina vera; quando il proprietario incolla una chat, che porta il suo nome; prima di consegnare i comandi git di un commit che tocca documentazione; e quando il controllo segnala un riscontro bloccante o da valutare.

## Procedura minima

Si esegue il controllo sull'intero perimetro pubblicabile, non sui soli file toccati, perché un residuo non si introduce ma si eredita.

```
python tools/Test-Anonymization.py
python tools/Test-Anonymization.py --tutti
```

La prima forma è bloccante e va verde prima del commit; la seconda include il livello privato e non è bloccante. Un riscontro vero si corregge nel file tracciato con il segnaposto, si aggiunge alla mappa `_notes/.anonymization-map.md` e, se è una categoria nuova, al file dei pattern `_notes/.anonymization-patterns.json`. Un valore già entrato nella storia non si toglie riscrivendola da soli: si annota come lavoro a parte, che il proprietario pianifica, come è stato fatto con ADR-087.

## Vincoli

Il file dei pattern e la mappa non si tracciano mai, e il loro contenuto non si copia in un file tracciato né in un messaggio di commit. Il rapporto del controllo stampa i valori trovati: in sessione si riferisce per categoria e per file, non incollando i valori.
