---
tipo: fonte
livello: 3
letto: si
track: [LDN]
url: https://github.com/unlimitedcoder2/frlg-ldn-trade
tags: [fonte, livello-3]
usa: "[[kinnay-ldn]]"
---

# frlg-ldn-trade

https://github.com/unlimitedcoder2/frlg-ldn-trade

## Abstract

Proof of concept che fa scambiare Pokemon a un PC con Rosso Fuoco e Verde Foglia in esecuzione su Switch o Switch 2, simulando un giocatore che si collega come capo sessione. Richiede Linux, Python 3.12 o successivo, le chiavi della console, almeno due strutture .pk3 e un gioco portato avanti fino allo sbloccio della sala degli scambi. Licenza AGPLv3.

## Perché è in archivio

È il punto di partenza del track, e la sua tabella di compatibilità delle schede Wi-Fi è ciò che decide se il track sia praticabile su una macchina data: affidabili la ALFA AWUS036ACHM con driver mt76x0u e la Realtek RTL8821CE con rtw88_8821ce, inaffidabile la AMD RZ616 con mt7921e, e dichiaratamente problematiche la Intel AX200 con iwlwifi e l Atheros AR9271 con ath9k_htc, entrambe incapaci di ricevere un indirizzo. Il repository dichiara anche che la decompilazione pret/pokefirered comprende il port per Switch, e che il progetto e nato per dimostrare la possibilità di uno scambio non ufficiale.

## A quale punto del progetto serve

- [[06-identita-pokemon]], i formati .pk3 e .ek3 sono strutture Gen 3
- [[11-wireless-locale-e-ponte-switch]], requisiti hardware e procedura di scambio

## Relazioni con altre fonti

- usa come dipendenza o base [[kinnay-ldn]]

## Contesto

Livello 3 di affidabilità secondo la gerarchia di [[SOURCES]]. Track serviti: LDN. La mappa di tutte le fonti e delle loro relazioni è [[index-fonti]].
