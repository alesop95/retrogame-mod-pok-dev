---
tipo: fonte
livello: 1
letto: si
track: [LDN]
url: https://github.com/unlimitedcoder2/ldnd
tags: [fonte, livello-1]
alternativa-a: "[[kinnay-ldn]]"
---

# unlimitedcoder2/ldnd

https://github.com/unlimitedcoder2/ldnd

## Abstract

Demone in C, licenza GPL-2.0, che porta lo stack wireless di Linux su Windows: collega il kernel Linux come libreria statica tramite LKL dentro un eseguibile costruito con MinGW, riceve l adattatore USB attraverso WinUSB e gli fa caricare i driver e i file di linux-firmware. Espone il servizio su una pipe con nome, e la sua riga di comando passa parametri di modulo del kernel fra cui rtw88_usb.switch_usb_mode=0.

## Perché è in archivio

Ribalta il vincolo di piattaforma che il progetto dava per assodato, perché rende il track eseguibile su Windows e quindi compatibile con il track dello Smeraldo sulla stessa macchina. Ha anche una compatibilità hardware diversa dalla via Linux, verificata sul campo, perché scavalca il gestore di rete e il driver di sistema; in cambio funziona soltanto con adattatori USB e, dopo la riassegnazione a WinUSB, il dispositivo non funziona più come scheda di rete ordinaria.

## A quale punto del progetto serve

- [[11-wireless-locale-e-ponte-switch]], la via Windows, e il conflitto fra modalità USB 2 e USB 3

## Relazioni con altre fonti

- è un'alternativa a [[kinnay-ldn]]

## Contesto

Livello 1 di affidabilità secondo la gerarchia di [[SOURCES]]. Track serviti: LDN. La mappa di tutte le fonti e delle loro relazioni è [[index-fonti]].
