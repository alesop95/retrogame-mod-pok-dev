# -*- coding: utf-8 -*-
"""Strati di formato e conversione del ponte fra generazioni.

L'architettura è descritta in docs/20-architettura-codice.md. In breve: i dati generati
stanno in data/, i modelli e i lettori e scrittori qui, la conversione e il trasporto
arriveranno come strati separati. Nessuna dipendenza esterna, per scelta: gli strati dal
primo al quarto sono aritmetica su interi e manipolazione di byte, e restano portabili.
"""

from . import gb, gen1, gen2, gen3, charmap

__all__ = ["gb", "gen1", "gen2", "gen3", "charmap"]
