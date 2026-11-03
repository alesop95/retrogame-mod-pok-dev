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

Il 2026-10-09 il difetto opposto: una riga marcata «NON ANCORA LETTO» risultava chiusa, perché
l'espressione trova «LETTO» dentro la dicitura negata. Dal 2026-11-03 le forme negate («non
letto», «non ancora letto», «non verificata» e simili) si tolgono dalla riga prima di cercare le
tracce; «non recuperabile» resta un esito, perché dice che la lettura è impossibile e non che
manca. Dallo stesso giorno lo stato «CHIUSO» conta solo in maiuscolo, perché «chiusura» in minuscolo è un fatto e
non una lettura, e «riletto» è una lettura. `--prova` esegue i casi che lo dimostrano.

Uso
---
    python tools/conta-letti.py
    python tools/conta-letti.py --prova
"""
import re,csv,io,collections,sys
def k(u): return u.replace(chr(92),'').rstrip('/').split('#')[0]
letti=set(); stato={}
for x in csv.DictReader(io.open('pokedex-home-completo/data/residuo-corpus.csv',encoding='utf-8'),delimiter=';'):
    stato[k(x['indirizzo'])]=x['stato']
for r in io.open('pokedex-home-completo/CENSIMENTO-FONTI-COLLEZIONE.md',encoding='utf-8'):
    if r.startswith('|') and 'scaricato' in r:
        for u in re.findall(r'https?://[^\s|)]+',r): stato.setdefault(k(u),'scaricato dalla corsa')
LET=re.compile(r'\b(lett[oaie]|LETT[OAIE]|rilett[oaie]|trascritt|TRASCRITT|scaricat|consegnat|clonat|clone superficiale|verificat|irrecuperabil|non recuperabil|saltato|scartato|fuori perimetro|esportat|ESPORTAT|filtrat|FILTRAT|Stato al 2026-10-05)',re.I)
# Lo stato CHIUSO conta solo in maiuscolo: «chiusura» o «ha chiuso» in minuscolo descrivono un fatto, non una lettura
# (il 2026-11-03 la riga di IGN, che rimandava il lavoro «alla chiusura della banca», risultava letta).
CHIUSA=re.compile(r'\bCHIUS[OAIE]\b')
NEG=re.compile(r'\bnon\s+(?:ancora\s+|ancora\s+stat[oaie]\s+|stat[oaie]\s+)?(?:lett|trascritt|scaricat|consegnat|clonat|verificat|esportat|filtrat|chius)\w*',re.I)
def chiusa(r):
    r=NEG.sub(' ',r)
    return bool(LET.search(r) or CHIUSA.search(r))
if '--prova' in sys.argv:
    casi=[('| 1 | https://a.it/x | NON ANCORA LETTO |',False),('| 1 | https://a.it/x | non letta |',False),
          ('| 1 | https://a.it/x | letto: estratto |',True),('| 1 | https://a.it/x | non recuperabile, 403 |',True),
          ('| 1 | https://a.it/x | verificata, non letta per intero |',True),('| 1 | https://a.it/x | da leggere |',False),
          ('| 1 | https://a.it/x | non ancora verificato |',False),('| 1 | https://a.it/x | da fare alla chiusura della banca |',False),
          ('| 1 | https://a.it/x | CHIUSO il 2026-10-01 |',True),('| 1 | https://a.it/x | riletto il 2026-09-23 |',True)]
    errati=[c for c,a in casi if chiusa(c)!=a]
    for c in errati: print('ERRATO',c)
    print(len(casi)-len(errati),'casi superati su',len(casi)); sys.exit(1 if errati else 0)
FINALI={'letto','trascritto','catalogo letto','letto a vista','letto con OCR','irrecuperabile','saltato','scartato','scaricato dalla corsa'}
aperti=[]; tot=0
for i,r in enumerate(io.open('SOURCES.md',encoding='utf-8'),1):
    if not r.startswith('|'): continue
    us=re.findall(r'https?://[^\s|)`]+',r)
    if not us: continue
    tot+=1
    if chiusa(r) or any(stato.get(k(u)) in FINALI for u in us): continue
    aperti.append((i,us[0],r[:110].strip()))
print('righe con indirizzo',tot,'senza traccia di lettura',len(aperti))
for a in aperti: print(a[0],a[1][:90])
