#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conta le righe di SOURCES.md che portano un indirizzo ma nessuna traccia di lettura.

Perché esiste
-------------
Il 2026-10-05 il proprietario ha chiesto «sì o no» se tutte le fonti del registro fossero lette.
La risposta si dà contando, non ricordando: questo strumento passa ogni riga di `SOURCES.md` che
contiene un indirizzo e la considera chiusa se il testo della riga dichiara un esito (letto,
trascritto, scaricato, clonato, verificato, irrecuperabile, saltato, scartato, fuori perimetro e
simili) oppure se il suo indirizzo ha un esito finale nel residuo del corpus
(`pokedex-home-completo/data/residuo-corpus.csv`) o è stato scaricato dalla corsa del lettore
(`pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md`). Stampa il totale e le righe aperte.
Nato come script di sessione in `_notes/fonti/`, tracciato dal 2026-10-07 con la mappa di
riorganizzazione (U1), perché `pending.md` lo indica per rifare la conta.

Il perimetro, da dichiarare accanto a ogni conta: le sole righe di `SOURCES.md` in forma di
tabella con un indirizzo `http` o `https`; non i collegamenti scritti negli altri documenti, che
sono il perimetro di `tools/verifica-link-progetto.py`.

Il 2026-10-07 la prima corsa dello strumento tracciato ha dato una riga aperta che non lo era:
la riga del clone del wiki di pokeemerald dice «clone superficiale [...] Coincide», e il vocabolario
conosceva «clonato» ma non «clone»; «clone superficiale» è entrato fra le tracce di lettura.

Uso
---
    python tools/conta-letti.py
"""
import re,csv,io,collections
def k(u): return u.replace(chr(92),'').rstrip('/').split('#')[0]
letti=set(); stato={}
for x in csv.DictReader(io.open('pokedex-home-completo/data/residuo-corpus.csv',encoding='utf-8'),delimiter=';'):
    stato[k(x['indirizzo'])]=x['stato']
for r in io.open('pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md',encoding='utf-8'):
    if r.startswith('|') and 'scaricato' in r:
        for u in re.findall(r'https?://[^\s|)]+',r): stato.setdefault(k(u),'scaricato dalla corsa')
LET=re.compile(r'\b(lett[oaie]|LETT[OAIE]|trascritt|TRASCRITT|scaricat|consegnat|clonat|clone superficiale|verificat|irrecuperabil|non recuperabil|saltato|scartato|fuori perimetro|esportat|ESPORTAT|filtrat|FILTRAT|CHIUS|chius|Stato al 2026-10-05)',re.I)
FINALI={'letto','trascritto','catalogo letto','letto a vista','letto con OCR','irrecuperabile','saltato','scartato','scaricato dalla corsa'}
aperti=[]; tot=0
for i,r in enumerate(io.open('SOURCES.md',encoding='utf-8'),1):
    if not r.startswith('|'): continue
    us=re.findall(r'https?://[^\s|)`]+',r)
    if not us: continue
    tot+=1
    if LET.search(r) or any(stato.get(k(u)) in FINALI for u in us): continue
    aperti.append((i,us[0],r[:110].strip()))
print('righe con indirizzo',tot,'senza traccia di lettura',len(aperti))
for a in aperti: print(a[0],a[1][:90])
