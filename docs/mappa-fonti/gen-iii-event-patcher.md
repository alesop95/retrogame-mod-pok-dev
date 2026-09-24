---
tipo: fonte
livello: 3
letto: si
track: [EVT, BRI]
url: https://github.com/superguideguy/gen-iii-event-patcher
tags: [fonte, livello-3]
conferma: "[[devlog-ptgb]]"
---

# gen-iii-event-patcher

https://github.com/superguideguy/gen-iii-event-patcher

## Abstract

Strumento in Java che trasforma la ROM di un gioco di terza generazione in una ROM di distribuzione, e che applica uno script di evento a un salvataggio per uso personale. Letto il 2026-08-29 nella descrizione e nella struttura del sorgente, che comprende un compilatore elementare per gli script di evento e un costruttore di checksum.

## Perché è in archivio

Documenta il secondo canale di distribuzione, che il primo studio del track confondeva con il primo: il Dono Segreto non attiva una bandiera ma scarica dentro il salvataggio uno script di un kilobyte eseguito più tardi, capace di contenere qualunque istruzione valida compresa quella che porta all'esecuzione di codice arbitrario. È il punto di convergenza più notevole della ricerca, perché è il medesimo meccanismo che il dev log dello strumento di trasferimento fra generazioni descrive dall'altro capo, scoperto in modo indipendente da due progetti con scopi opposti. Dichiara inoltre che Rubino e Zaffiro hanno il precedente Evento Mistero, che è cosa diversa, e che il trasferimento della carta meraviglia passa dall'adattatore senza fili e non dal cavo.

## A quale punto del progetto serve

- [[09-esecuzione-codice]], la sezione di script eseguibile come porta di servizio del formato
- [[10-multiboot-hardware]], il secondo canale, che non è il multiboot

## Relazioni con altre fonti

- conferma in modo indipendente [[devlog-ptgb]]

## Contesto

Livello 3 di affidabilità secondo la gerarchia di [[SOURCES]]. Track serviti: EVT, BRI. La mappa di tutte le fonti e delle loro relazioni è [[index-fonti]].
