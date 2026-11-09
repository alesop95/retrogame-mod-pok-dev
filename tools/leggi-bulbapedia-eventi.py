#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Estrae le schede degli esemplari dalle liste di distribuzioni di Bulbapedia salvate in HTML, e le confronta con le copie.

Perché esiste
-------------
Il 2026-11-06 il proprietario ha chiesto che Bulbapedia fosse letta per intero nelle sue liste di distribuzioni, per
generazione e per regione (ADR-118). Le liste sono composte di schede uguali, una per esemplare, con specie, numero
del Pokédex, livello, allenatore e ID; il 2026-11-07 l'API era dietro una verifica anti-bot e le pagine sono state lette
dalla Wayback Machine (ADR-119). Questo strumento legge quelle pagine, ne estrae le schede e cerca ogni scheda nel
giudizio delle copie per HOME per specie e allenatore, poi per specie e livello: ciò che resta sono le distribuzioni che
le copie non hanno, da esaminare una per una.

Uso
---
    python tools/leggi-bulbapedia-eventi.py CARTELLA_HTML GIUDIZIO.json USCITA.json
"""
import html, json, re, sys, unicodedata, glob, os, collections

def testo(h):
    h = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", h))
    return [x.strip() for x in t.split("\n") if x.strip()]

def norma(s):
    return re.sub(r"[\s\-－ー・.♂♀]", "", unicodedata.normalize("NFKC", re.sub(r"\(.*?\)", "", str(s or ""))).casefold())

def schede(righe, titolo):
    out = []
    for i, r in enumerate(righe):
        if r != "Dex No." or i + 1 >= len(righe) or not righe[i + 1].isdigit():
            continue
        finestra = righe[max(0, i - 4):i + 60]
        sp = next((x for x in reversed(righe[max(0, i - 4):i]) if re.fullmatch(r"[A-Z0-9'.:\- ♀♂É]{3,}", x)), None)
        def dopo(etichetta):
            if etichetta in finestra:
                k = finestra.index(etichetta)
                return finestra[k + 1] if k + 1 < len(finestra) else None
            return None
        lv = next((x for x in finestra if re.fullmatch(r"Lv \d+", x)), None)
        out.append({"pagina": titolo, "numero": int(righe[i + 1]), "specie": sp, "livello": int(lv[3:]) if lv else None,
                    "ot": dopo("OT"), "id": dopo("ID No."),
                    "natura": next((x.replace(" nature.", "") for x in finestra if x.endswith(" nature.")), None)})
    return out

def main():
    cartella, giudizio, uscita = sys.argv[1:4]
    tutte = []
    for f in sorted(glob.glob(os.path.join(cartella, "*.html"))):
        h = open(f, encoding="utf-8").read()
        titolo = os.path.basename(f)[:-5]
        tutte += schede(testo(h), titolo)
    g = json.load(open(giudizio, encoding="utf-8"))
    per_ot, per_lv = set(), set()
    for c in g["copie"]:
        for e in c["esemplari"]:
            per_ot.add((e["numero"], norma(e["allenatore"])))
            per_lv.add((e["numero"], e.get("livello_incontro")))
    mancanti = []
    for s in tutte:
        ot = norma(s["ot"])
        if ot and any(k[0] == s["numero"] and (k[1] == ot or (len(ot) > 2 and len(k[1]) > 2 and (k[1].startswith(ot) or ot.startswith(k[1])))) for k in per_ot):
            continue
        if (s["numero"], s["livello"]) in per_lv and not ot:
            continue
        mancanti.append(s)
    json.dump({"pagine": len(glob.glob(os.path.join(cartella, "*.html"))), "schede": len(tutte), "non_trovate": mancanti},
              open(uscita, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("pagine %d, schede %d, non trovate per specie e allenatore %d" % (len(glob.glob(os.path.join(cartella, "*.html"))), len(tutte), len(mancanti)))

if __name__ == "__main__":
    main()
