#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone il pedigree di ogni esemplare delle copie per HOME: un PDF stampabile e un documento generato per gruppo.

Perché esiste
-------------
Il proprietario ha chiesto, il 2026-09-30, un PDF separato e stampabile di tutta la collezione, aggiornato man mano
che il lavoro procede, con una piccola immagine del Pokémon presa dalla raccolta delle illustrazioni di Sugimori che
tiene in locale, e il 2026-10-01 che dicesse nel dettaglio che tipo di evento è ciascun esemplare. Il 2026-11-04
(ADR-111) ha chiesto che ogni esemplare abbia un pedigree nella documentazione e nella stampa. Il catalogo a righe del
2026-10-01 è stato sostituito quel giorno dalle schede di pedigree, e il suo codice tolto.

Le schede si compongono dai dati e non si scrivono a mano. `tools/pkhex-elenco-copie` legge le copie dei salvataggi,
che sono ciò che arriva in HOME, e dà per ogni esemplare i campi del pedigree e l'evento come lo riconosce la
libreria. Questo strumento lo arricchisce con la descrizione che il progetto ha già per i lotti che non portano una
carta: il nome dell'evento nel file degli eventi di terza generazione, i gruppi di `SCHEDE-EVENTI-GB.md`, la tabella
di `COMPLEMENTO-RUBINO.md` e la provenienza della checklist. Compone con LuaLaTeX e il design system di
`pokedex-home-completo/design-system/`, e cancella i file ausiliari di LaTeX dopo la composizione.

Le miniature si generano una volta in `_notes/stampa/miniature/` con Pillow, a 96 pixel, e non entrano in Git.

Uso
---
    python tools/stampa-collezione.py _notes/lavoro/giudizi-copie/dopo-bfe89c7-pedigree.json --pdf
    python tools/stampa-collezione.py ... --gruppo HOME1 --gruppo GIAPPONE
    python tools/stampa-collezione.py ... --immagini "<cartella delle illustrazioni, divisa per generazione>"
"""

import argparse
import glob
import io
import json
import os
import re
import subprocess
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMMAGINI = os.path.join(os.path.expanduser("~"), "Proton Drive", "alesop95", "My files",
                        "Sugimori Pokémon Gen1-9 DLC3 Organized", "Sugimori Pokémon Gen1-9 DLC3 Organized",
                        "Pokémon By Generation")

SOSTITUZIONI = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
                "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}

GIOCHI = {"RD": "Rosso", "GN": "Verde", "BU": "Blu", "YW": "Giallo", "GD": "Oro", "SI": "Argento", "C": "Cristallo",
          "R": "Rubino", "S": "Zaffiro", "E": "Smeraldo", "FR": "Rosso Fuoco", "LG": "Verde Foglia", "CXD": "Colosseum/XD",
          "D": "Diamante", "P": "Perla", "Pt": "Platino", "HG": "HeartGold", "SS": "SoulSilver",
          "B": "Nero", "W": "Bianco", "B2": "Nero 2", "W2": "Bianco 2", "X": "X", "Y": "Y", "OR": "Rubino Omega",
          "AS": "Zaffiro Alpha", "SN": "Sole", "MN": "Luna", "US": "Ultrasole", "UM": "Ultraluna"}

# I nomi d'incontro della libreria, resi in italiano quando non c'è una descrizione migliore.
INCONTRI = [("Event Gift", "evento"), ("Egg", "uovo"), ("Static Encounter", "incontro fisso"),
            ("In-game Trade", "scambio in gioco"), ("Virtual Console Transfer", "evento di Game Boy"),
            ("Wild Encounter", "selvatico"), ("Pokéwalker Encounter", "Pokéwalker"),
            ("Dream Radar Encounter", "Dream Radar"), ("My Pokémon Ranch", "My Pokémon Ranch")]

ETICHETTE_GB = {"stadium-jp": "Pokémon Stadium giapponese", "stadium2-jp": "Pokémon Stadium 2 giapponese",
                "uovo-strano": "Uovo Strano di Cristallo", "tour-jp": "Mew delle manifestazioni giapponesi"}


def tex(testo):
    return "".join(SOSTITUZIONI.get(c, c) for c in str(testo))


def descrizioni_del_progetto():
    """Il dettaglio dell'evento che il progetto ha già, per codice della checklist e per file di lotto."""
    per_codice, per_file = {}, {}
    chk = os.path.join(RADICE, "pokedex-home-completo", "CHECKLIST-COMPLETA.md")
    for riga in io.open(chk, encoding="utf-8"):
        m = re.match(r"\| `(EVT-[^`]+)` \| \d \| ([^|]+) \| \d+ \| \d+ \| ([^|]+) \|", riga)
        # Per i doni segreti e le tabelle di incontro la provenienza della checklist è generica, cioè l'elenco dei
        # giochi o la classe: il dettaglio viene allora dalla carta o dalle schede.
        if m and m.group(2).strip() not in ("dono segreto", "tabella di incontro"):
            per_codice[m.group(1)] = m.group(3).strip()
    gruppo = None
    for riga in io.open(os.path.join(RADICE, "pokedex-home-completo", "SCHEDE-EVENTI-GB.md"), encoding="utf-8"):
        if riga.startswith("## "):
            gruppo = riga[3:].strip()
        m = re.match(r"### (EVT-\d-\d{4}) ", riga)
        if m and gruppo:
            per_codice[m.group(1)] = gruppo
    for riga in io.open(os.path.join(RADICE, "pokedex-home-completo", "COMPLEMENTO-RUBINO.md"), encoding="utf-8"):
        celle = [c.strip() for c in riga.split("|")]
        if len(celle) >= 8 and re.match(r"\d{3}-", celle[1]):
            # L'origine di un esemplare del complemento è lotto-complemento-rubino/esemplari/... nei rapporti delle
            # copie scritti dal 2026-10-07, ed esemplari/... in quelli precedenti: valgono entrambe finché le copie
            # non sono rifatte (ADR-099). La forma breve era anche di lotto-parco-lotta, che non va nelle copie.
            for prefisso in ("lotto-complemento-rubino/esemplari/", "esemplari/"):
                per_file[prefisso + celle[1] + ".pk3"] = celle[6]
    # I file che la checklist collega per tabella, come gli incontri dei biglietti.
    sorgente = io.open(os.path.join(RADICE, "tools", "checklist-pokedex.py"), encoding="utf-8").read()
    for m in re.finditer(r'"(EVT-[^"]+)": \("([^"]+)", "([^"]+)"\)', sorgente):
        lotto = m.group(2)
        if per_codice.get(m.group(1)):
            per_file.setdefault("%s/%s" % (lotto, m.group(3)), per_codice[m.group(1)])
    return per_codice, per_file


def evento_di(e, per_codice, per_file):
    origine = e["origine"]
    nome = os.path.splitext(os.path.basename(origine))[0]
    parti = nome.split("-")
    if per_file.get(origine):
        return per_file[origine]
    if "carta" in e["evento"]:
        return e["evento"]
    if len(parti) >= 3 and parti[0] == "EVT" and per_codice.get("-".join(parti[:3])):
        return per_codice["-".join(parti[:3])]
    if origine.startswith("lotto-eventi/") and len(parti) >= 3:
        return "evento di terza generazione: " + re.sub(r"(?<=[a-z])(?=[A-Z0-9])", " ", parti[1])
    for chiave, etichetta in ETICHETTE_GB.items():
        if nome.startswith("GB-" + chiave + "-"):
            return etichetta
    for inglese, italiano in INCONTRI:
        if e["evento"].startswith(inglese):
            resto = e["evento"][len(inglese):].strip(" ()")
            return italiano + (" (%s)" % resto if resto else "")
    return e["evento"]


def miniatura(e, cartella, cache):
    """La miniatura della specie e della forma, generata una volta; None se l'illustrazione non c'è."""
    chiave = "%04d-%s" % (e["numero"], e.get("forma_en") or "")
    if chiave in cache:
        return cache[chiave]
    candidati = glob.glob(os.path.join(cartella, "*", "%04d *.png" % e["numero"]))
    scelto = None
    forma = (e.get("forma_en") or "").lower()
    if forma:
        scelto = next((c for c in candidati if forma in os.path.basename(c).lower()), None)
    if scelto is None:
        base = [c for c in candidati if re.fullmatch(r"\d{4} [^ ]+\.png", os.path.basename(c))]
        scelto = (base or sorted(candidati, key=len) or [None])[0]
    if scelto is None:
        cache[chiave] = None
        return None
    from PIL import Image
    uscita = os.path.join(RADICE, "_notes", "stampa", "miniature", re.sub(r"[^A-Za-z0-9-]", "_", chiave) + ".png")
    if not os.path.exists(uscita):
        os.makedirs(os.path.dirname(uscita), exist_ok=True)
        img = Image.open(scelto).convert("RGBA")
        img.thumbnail((96, 96))
        fondo = Image.new("RGBA", (96, 96), (255, 255, 255, 255))
        fondo.paste(img, ((96 - img.width) // 2, (96 - img.height) // 2), img)
        fondo.convert("RGB").save(uscita)
    cache[chiave] = uscita.replace("\\", "/")
    return cache[chiave]


# Il pedigree di ogni esemplare (ADR-111, 2026-11-04): una scheda per esemplare nel PDF stampabile, con il design
# system di `pokedex-home-completo/design-system/`, e una riga per esemplare nel documento generato e tracciato, dalla
# stessa funzione, così che i due non divergano. Lo stato viene dal gruppo: il giro 1 è in HOME dal 2026-11-03.
STATO_GRUPPO = {"HOME1": ("DSstatoinhome", "in HOME"), "HOME2": ("DSstatoinhome", "in HOME"),  # il giro 2 dal 2026-11-04
                "HOME3": ("DSstatoinhome", "in HOME"),  # il giro 3 dal 2026-11-06, HOME a 2600
                "HOME6": ("DSstatoinhome", "in HOME"),  # il giro 4 dal 2026-11-09, HOME a 3529
                "HOME8": ("DSstatoinhome", "in HOME"),  # il giro 5 dal 2026-11-09, HOME a 3785
                "HOME9": ("DSstatoinhome", "in HOME"),  # il giro 6 dal 2026-11-09, HOME a 4474
                "HOME4": ("DSstatoinhome", "in HOME"),  # il giro 7 dal 2026-11-09, HOME a 4567
                "HOME5": ("DSstatoinhome", "in HOME"),  # il giro 8 dal 2026-11-10, HOME a 5176
                "HOME7": ("DSstatoinhome", "in HOME"),  # il giro 9 dal 2026-11-13, HOME a 5818
                "HOME10": ("DSstatoinhome", "in HOME"),  # il giro 10 dal 2026-11-13, HOME a 6198
                "GIAPPONE2": ("DSstatoinhome", "in HOME"),  # il giro 11 dal 2026-11-13, HOME a 6223 con i due da GO
                "RIDATA2": ("DSstatoinhome", "in HOME"),  # il giro 12 dal 2026-11-16, HOME a 6791 (ADR-126)
                "RIDATA1": ("DSstatoinhome", "in HOME"),  # il giro 13 dal 2026-11-16, HOME a 7221 (ADR-126)
                "DIAMANTE1": ("DSstatoinhome", "in HOME"),  # il giro 14 dal 2026-11-17, HOME a 7466 prima di liberare (ADR-130)
                "VERDEFOGLIA1": ("DSstatoinhome", "in HOME")}  # il giro 15 dal 2026-11-24, HOME a 7825 prima di liberare (ADR-140)


# Gli esemplari che il gioco non lascia uscire dalla console anche se la libreria li giudica conformi nel loro gioco: il
# Pikachu Cosplay (forme da 1 a 6 in sesta generazione) non lascia Rubino Omega e Zaffiro Alpha
# (`pokedex-home-completo/CONNETTIVITA-HOME.md`, `FormVerifier.cs` righe 45-47). Al giro 6 del 2026-11-09 i sei della copia
# HOME9 sono rimasti nel box 16, e HOME è salito di 689 invece che di 695. La regola vale per esemplare e non per gruppo.
# Dal 2026-11-10 anche i doni di taglia totem di Marowak, Araquanid, Togedemaru e Ribombee della spiaggia di Kantai:
# la libreria li dichiara non trasferibili oltre la settima generazione (`EncounterStatic7.IsTotemNoTransfer`, usata da
# `TransferVerifier.cs` righe 149-157), mentre gli altri sette totem passano e tornano alla forma base. Al giro 8 la banca
# ha lasciato i quattro di HOME5 nel box 21 di Ultraluna, posti 3, 5, 7 e 10, e HOME è salito di 609 invece che di 613.
# Al giro 9 del 2026-11-13 il Restore della copia HOME7 ha sostituito quella partita: i quattro non sono più nella console
# ma nella riserva di Checkpoint `20261111-prima9`, nelle due riserve del PC e nella copia HOME5.
TOTEM_NON_TRASFERIBILI = {105: 2, 752: 1, 777: 1, 743: 1}


def resta_in_console(e):
    if e.get("generazione") == 7 and TOTEM_NON_TRASFERIBILI.get(e["numero"]) == e.get("forma_n", 0):
        return ("DSstatoincopia", "fuori da HOME",
                "Fuori da HOME: il dono di taglia totem di questa specie non lascia la settima generazione, e al "
                "giro 8 del 2026-11-10 la banca non l'ha preso con gli altri esemplari della copia. Dal giro 9 del "
                "2026-11-13 non è più nella partita di Ultraluna, sostituita dal Restore: sta nella riserva di "
                "Checkpoint 20261111-prima9, nelle due riserve del PC e nella copia HOME5.")
    if e["numero"] == 25 and e.get("generazione") == 6 and e.get("forma_n", 0) in range(1, 7):
        return ("DSstatoincopia", "fuori da HOME",
                "Resta fuori da HOME: il Pikachu Cosplay non lascia la sesta generazione, e al giro 6 del 2026-11-09 "
                "non è passato a HOME con gli altri esemplari della copia. Dal giro 13 del 2026-11-16 non è più nella "
                "partita di Rubino Omega, sostituita dal Restore: sta nella riserva di Checkpoint 20261116-prima13, nelle "
                "due riserve del PC e nella copia HOME9.")
    return None


# Dal 2026-11-16 (ADR-126): i doni da carta con la data di incontro fuori dalla finestra dell'evento hanno un sostituto,
# identico salvo la data, nelle copie RIDATA1 e RIDATA2, e vanno liberati in HOME dopo i giri di quelle copie. Il legame
# fra vecchio e nuovo lo scrive `tools/elenco-da-liberare.py`.
SOSTITUZIONI_RIDATA = os.path.join(RADICE, "pokedex-home-completo", "data", "sostituzioni-ridata.json")
_sost = json.load(io.open(SOSTITUZIONI_RIDATA, encoding="utf-8")) if os.path.exists(SOSTITUZIONI_RIDATA) else []
SOSTITUITI = {x["impronta_vecchia"]: x for x in _sost}
SOSTITUTI = {x["impronta_nuova"]: x for x in _sost}


def stato_esemplare(e):
    """Lo stato proprio dell'esemplare, se diverso da quello del gruppo: fermo in console, oppure sostituito."""
    fermo = resta_in_console(e)
    if fermo:
        return fermo
    x = SOSTITUITI.get(e.get("impronta"))
    if x:
        return ("DSstatoincopia", "da liberare in HOME",
                "Da liberare in HOME: la data di incontro %s sta fuori dalla finestra dell'evento (ADR-126). Il sostituto, "
                "identico salvo la data, %s, è nella copia %s, box %d, posto %d; questo esemplare si libera dopo che il "
                "sostituto è in HOME, cercandolo sotto l'etichetta «Bank %d»." % (
                    x["data_vecchia"], x["data_nuova"], x["gruppo_nuovo"], x["box_nuovo"], x["posto_nuovo"],
                    x["box_vecchio"]))
    x = SOSTITUTI.get(e.get("impronta"))
    if x:
        return STATO_GRUPPO.get(x["gruppo_nuovo"], ("DSstatoincopia", "in copia")) + (
                "Sostituisce l'esemplare di %s, box %d, posto %d, che aveva la data di incontro %s fuori dalla finestra "
                "dell'evento (ADR-126)." % (x["gruppo_vecchio"], x["box_vecchio"], x["posto_vecchio"], x["data_vecchia"]),)
    return None


DS =os.path.join(RADICE, "pokedex-home-completo", "design-system")
PEDIGREE_MD = os.path.join(RADICE, "pokedex-home-completo", "pedigree")
PEDIGREE_PDF = os.path.join(RADICE, "_notes", "stampa", "pedigree")
# dal 2026-11-17 (ADR-130) anche Diamante e le squadre delle cartucce, che portano il nome del proprietario e dei suoi amici
ORIGINI_PRIVATE = ("lotto-smeraldo-cartuccia/", "lotto-diamante/", "lotto-squadre-cartucce/", "lotto-verde-foglia/")
# La storia dell'evento e le sue fonti (richiesta del proprietario del 2026-11-04): per la terza generazione dai racconti
# autorati di `provenienze-eventi.json`, legati per allenatore e ID; dalla quarta alla settima dall'Eventdex di Serebii,
# letto e analizzato il 2026-11-04, legato per specie, allenatore e ID.
PROVENIENZE_GEN3 = os.path.join(RADICE, "recreate-pokemon-distributions-events", "provenienze-eventi.json")
# I Pokemon specifici della comunita' RNG (ADR-115): la storia e la fonte stanno nel file tracciato, il PID che li riconosce
# nel rapporto del lotto, che e' locale.
COMUNITA = [os.path.join(RADICE, "_notes", "lotti", "lotto-rng-comunita", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-rng-comunita-2", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-rng-comunita-3", "rapporto.json"),
            # il Rayquaza di Pokemon Box, Metodo 4 (2026-11-09)
            os.path.join(RADICE, "_notes", "lotti", "lotto-rng-comunita-4", "rapporto.json"),
            # i 117 di FINALE senza la mossa d'evento (ADR-121, 2026-11-09)
            os.path.join(RADICE, "_notes", "lotti", "lotto-finale-117", "storie.json"),
            # i 2 Farfetch'd di Stadium 2 bonificati (ADR-122, 2026-11-09)
            os.path.join(RADICE, "_notes", "lotti", "lotto-finale-farfetchd-bonificati", "storie.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-ranch-lingue", "rapporto.json"),
            # gli eventi dell'Eventdex di Serebii che mancavano alle copie, prodotti dalle carte della libreria (ADR-115)
            os.path.join(RADICE, "_notes", "lotti", "lotto-serebii-mancanti", "rapporto.json"),
            # le carte e i doni della libreria che nessuna copia aveva (ADR-116)
            os.path.join(RADICE, "_notes", "lotti", "lotto-carte-scoperte-2", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-skitty-pokepark", "rapporto.json"),
            # ADR-119, 2026-11-07: statici, doni e uova; JEREMY; Daisuki Club; Ranch in cinque lingue; Channel; varianti di
            # terza generazione; Magikarp di Hiroshima cromatico; premi del Blu giapponese
            os.path.join(RADICE, "_notes", "lotti", "lotto-statici-adr106-b", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-jeremy-2004", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-jeremy-2004-b", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-daisuki-club", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-daisuki-club-b", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-ranch-lingue-2", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-ranch-lingue-2-shellos", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-channel-sicuro", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-carte-varianti-adr119", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-hiroshima-magikarp", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-premi-blu-jp", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-gts-gen4", "rapporto.json"),
            os.path.join(RADICE, "_notes", "lotti", "lotto-marchio-game-boy", "storie.json"),
            # i Pokemon veri di Diamante e le squadre di Smeraldo e Rubino (ADR-130, 2026-11-17)
            os.path.join(RADICE, "_notes", "lotti", "lotto-diamante", "storie.json"),
            # i Pokemon veri di Verde Foglia (ADR-140, 2026-11-24)
            os.path.join(RADICE, "_notes", "lotti", "lotto-verde-foglia", "storie.json")]
EVENTDEX = os.path.join(RADICE, "_notes", "fonti", "raccolte", "serebii-eventdex-2026-11-04", "serebii-eventdex-eventi.json")


def _norma(testo):
    import unicodedata
    return unicodedata.normalize("NFKC", str(testo)).casefold().strip()


def carica_storie():
    gen3 = json.load(io.open(PROVENIENZE_GEN3, encoding="utf-8"))
    serebii, serebii_ot = {}, {}
    if os.path.exists(EVENTDEX):
        for ev in json.load(io.open(EVENTDEX, encoding="utf-8")):
            ots = ev["ot"] if isinstance(ev["ot"], list) else [ev["ot"]]
            for ot in ots:
                try:
                    serebii.setdefault((int(ev["numero"]), _norma(ot), int(ev["id"])), []).append(ev)
                except (TypeError, ValueError):
                    pass
                try:
                    serebii_ot.setdefault((int(ev["numero"]), _norma(ot)), []).append(ev)
                except (TypeError, ValueError):
                    pass
    comunita = {}
    for rapporto in [r for r in COMUNITA if os.path.exists(r)]:
        dati = json.load(io.open(rapporto, encoding="utf-8"))
        for ev in dati.get("esiti", dati.get("voci", [])):
            if ev.get("pid") and ev.get("storia"):
                # dal 2026-11-17 (ADR-130): una storia che dichiara la sua origine vale solo per l'esemplare con quella
                # origine, perche' i Pokemon veri di Diamante hanno lo stesso PID di gemelli gia' in HOME da altre copie
                if ev.get("origine"):
                    comunita[(ev["pid"].upper(), ev["origine"])] = (ev["storia"], [ev["fonte"]] if ev.get("fonte") else [])
                else:
                    comunita[ev["pid"].upper()] = (ev["storia"], [ev["fonte"]] if ev.get("fonte") else [])
    return gen3["gruppi"], gen3["fonti"], (serebii, serebii_ot), comunita


def storia_di(e, storie):
    """Il racconto dell'evento e i collegamenti alle fonti, se l'esemplare viene da un evento censito."""
    if not storie:
        return "", []
    gruppi, fonti, (serebii, serebii_ot), comunita = storie
    for chiave in ((str(e.get("pid", "")).upper(), e.get("origine")), str(e.get("pid", "")).upper()):
        if chiave in comunita:
            testo, collegamenti = comunita[chiave]
            return testo, list(collegamenti)
    testo, collegamenti = "", []
    g = gruppi.get("%s|%s" % (e["allenatore"], e["id"]))
    if g:
        testo = "%s: %s, %s; %s. %s" % (g["nome"], g["date"], g["luogo"], g["come"], g.get("note", ""))
        if g.get("fonte") in fonti:
            collegamenti.append(fonti[g["fonte"]]["url"])
    try:
        ev = (serebii.get((e["numero"], _norma(e["allenatore"]), int(e["id"]))) or [None])[0]
    except (TypeError, ValueError):
        ev = None
    # dal 2026-11-07 (ADR-119): se l'ID differisce da quello di Serebii, che sbaglia piu' spesso della carta, si lega per
    # specie e allenatore, purche' l'abbinamento sia unico
    if ev is None:
        cand = serebii_ot.get((e["numero"], _norma(e["allenatore"]))) or []
        if len({(c.get("evento"), c.get("data_inizio")) for c in cand}) == 1:
            ev = cand[0]
    if ev:
        if not testo:
            date = ev.get("data_inizio") or ""
            if ev.get("data_fine") and ev.get("data_fine") != date:
                date += " - " + ev["data_fine"]
            giochi = ev.get("giochi") or ""
            giochi = giochi if isinstance(giochi, str) else ", ".join(giochi)
            testo = "%s, %s, %s, %s; giochi: %s." % (ev.get("evento", ""), ev.get("regione", ""), ev.get("tipo", ""), date, giochi)
        collegamenti.append(ev["url"])
    # dal 2026-11-07 (ADR-119): ogni esemplare ha una storia. Dove nessuna fonte racconta l'evento, la storia si compone
    # dai dati dell'esemplare stesso, che sono misure e non ipotesi: come e' stato incontrato secondo il verificatore, in
    # quale gioco, dove, a che livello, quando e con quale allenatore; la fonte e' la libreria del verificatore.
    if not testo:
        data = e.get("data_incontro") or "data non registrata"
        testo = "%s: %s, %s, incontrato al livello %s, %s; allenatore %s, ID %s." % (
            (e.get("evento") or "incontro").rstrip(". "), GIOCHI.get(e["gioco"], e["gioco"]), e.get("luogo") or "luogo non registrato",
            e.get("livello_incontro"), data,
            "<ALLENATORE DELLA CARTUCCIA>" if e.get("origine", "").startswith(ORIGINI_PRIVATE) else e["allenatore"], e["id"])
        if not collegamenti:
            collegamenti.append("https://github.com/kwsch/PKHeX")
    return testo.strip(), collegamenti


def data_nel_lotto(e):
    """La data dell'esemplare nel file del suo lotto, prima che la conversione la cambiasse (2026-11-17)."""
    formato = e.get("formato_lotto") or ""
    if not formato:
        return "file del lotto non disponibile"
    if formato in ("PK3", "CK3", "XK3", "PK1", "PK2"):
        return "nessuna: il formato %s non registra la data" % formato
    testo = e.get("data_lotto") or "non registrata"
    if e.get("data_uovo_lotto"):
        testo += ", uovo ricevuto il %s" % e["data_uovo_lotto"]
    if (e.get("data_lotto") or "") == (e.get("data_incontro") or ""):
        testo += " (uguale alla copia)"
    return testo


def campi_pedigree(e, per_codice, per_file):
    """I campi del pedigree di un esemplare, come coppie etichetta e valore, nell'ordine di ADR-111."""
    iv = "/".join(str(v) for v in e["iv"])
    fiocchi = len(e["fiocchi"])
    return [
        ("gioco d'origine", GIOCHI.get(e["gioco"], e["gioco"])), ("luogo", e["luogo"]),
        ("data", e["data_incontro"] or "non registrata"),
        # dal 2026-11-17, su richiesta del proprietario: la data scritta nel file del lotto prima della conversione, cioe' per
        # i Pokemon veri il giorno vero della cattura o del Parco Amici, accanto a quella della copia che HOME mostra
        ("data nel lotto", data_nel_lotto(e)),
        ("livello", "%d, incontrato al %d" % (e["livello"], e["livello_incontro"])), ("sfera", e["sfera"]),
        ("lingua", e["lingua"]),
        ("allenatore", "%s, ID %s, SID %s" % (e["allenatore"], e["id"], e["sid"])), ("natura", e["natura"]),
        ("abilità", e["abilita"]),
        ("mosse", ", ".join(e["mosse"]) or "nessuna"), ("oggetto", e["oggetto"] or "nessuno"),
        ("fiocchi", ("%d" % fiocchi) if fiocchi else "nessuno"),
        ("IV", iv), ("PID", e["pid"]), ("EC", e["ec"]),
    ]


def scheda_tex(e, gruppo, per_codice, per_file, img, storie=None):
    storia, collegamenti = storia_di(e, storie)
    righe_storia = []
    if storia:
        righe_storia.append(r"{\scriptsize\itshape %s}\par" % tex(storia))
    if collegamenti:
        righe_storia.append(r"{\DSdati\tiny\color{DSseppia} Fonti: %s}\par" % "; ".join(r"\url{%s}" % u for u in collegamenti))
    gen = "DSgen" + "ABCDEFG"[max(1, min(7, e["generazione"])) - 1]
    colore, stato = STATO_GRUPPO.get(gruppo, ("DSstatoincopia", "in copia"))
    fermo = stato_esemplare(e)
    if fermo:
        colore, stato = fermo[0], fermo[1]
        righe_storia.insert(0, r"{\scriptsize\itshape %s}\par" % tex(fermo[2]))
    nome =tex(e["specie"]) + (" \\textnormal{\\small %s}" % tex(e["forma"]) if e["forma"] else "")
    segni = {"M": "♂", "F": "♀"}.get(e["sesso"], "") + (" ★" if e["cromatico"] else "")
    campi = campi_pedigree(e, per_codice, per_file)
    celle = []
    for i in range(0, len(campi), 3):
        celle.append(" & ".join("\\DScampo{%s} & %s" % (tex(k), tex(v)) for k, v in campi[i:i + 3]) + r"\\")
    mini = r"\DSminiatura[14mm]{%s}" % img if img else r"\tcbox[colback=DScartascura, colframe=DSfiletto, boxrule=0.4pt, arc=1.6mm, width=14mm, height=14mm]{}"
    giudizio = "conforme" if e["conforme"] else "NON conforme"
    return "\n".join([
        r"\begin{DSscheda}{%s}" % gen,
        r"\begin{minipage}[t]{16mm}\vspace{0pt}%s\end{minipage}\hspace{2mm}%%" % mini,
        r"\begin{minipage}[t]{\dimexpr\linewidth-18mm\relax}\vspace{0pt}",
        r"{\DStitoli\bfseries %s}\hspace{1.5mm}\DSnumero{%03d}\hspace{1.5mm}{\DSdati %s}\hfill\DSstato{%s}{%s}\par" % (
            nome, e["numero"], segni, colore, stato),
        r"{\footnotesize %s}\par" % tex(evento_di(e, per_codice, per_file)),
        *righe_storia,
        r"\vspace{0.6mm}",
        r"{\DSdati\scriptsize\setlength{\tabcolsep}{2pt}\begin{tabular}{@{}l L{29mm} l L{30mm} l L{34mm}@{}}",
        *celle,
        r"\end{tabular}}\par",
        r"{\DSdati\tiny\color{DSseppia} %s, PKHeX %s; %s box %d posto %d; impronta {\ttfamily %s}}" % (
            giudizio, tex(e["libreria"]), tex(gruppo), e["box"], e["posto"], e["impronta"]),
        r"\end{minipage}",
        r"\end{DSscheda}",
    ])


def pedigree(dati, cartella_immagini, pdf, solo=None):
    per_codice, per_file = descrizioni_del_progetto()
    storie = carica_storie()
    cache = {}
    g = json.load(io.open(os.path.join(DS, "tokens.json"), encoding="utf-8"))["geometria"]
    caratteri = os.path.join(RADICE, "_notes", "design-system", "caratteri").replace("\\", "/") + "/"
    os.makedirs(PEDIGREE_MD, exist_ok=True)
    os.makedirs(PEDIGREE_PDF, exist_ok=True)
    for c in dati["copie"]:
        gruppo, esemplari = c["gruppo"], c["esemplari"]
        if solo and gruppo not in solo:
            continue
        colore, stato = STATO_GRUPPO.get(gruppo, ("", "in copia"))
        md = ["# Pedigree degli esemplari del gruppo %s" % gruppo, "",
              "> Documento generato da `tools/stampa-collezione.py`, dalla stessa funzione che compone il PDF "
              "stampabile in `_notes/stampa/pedigree/%s.pdf`. Non si modifica a mano. Una riga per esemplare, nell'ordine di "
              "box e posto della copia, giudicata da `tools/pkhex-elenco-copie`; i campi sono quelli di ADR-111. Stato del "
              "gruppo: %s. Esemplari: %d, conformi: %d." % (gruppo, stato, len(esemplari),
                                                            sum(e["conforme"] for e in esemplari)) +
              ("".join(" Restano fuori da HOME, perché il gioco non li lascia uscire: %d." % n
                       for n in [sum(1 for e in esemplari if resta_in_console(e))] if n)) +
              ("".join(" Da liberare in HOME dopo i giri delle copie RIDATA, perché hanno un sostituto con la data "
                       "dentro la finestra dell'evento (ADR-126): %d." % n
                       for n in [sum(1 for e in esemplari if e.get("impronta") in SOSTITUITI)] if n)), "",
              "| Box | Posto | Specie | Forma | Sesso | Cromatico | Evento | Storia | Fonti | " +
              " | ".join(k[0].upper() + k[1:] for k, _ in campi_pedigree(esemplari[0], per_codice, per_file)) +
              " | Giudizio | Impronta |",
              "|" + "---|" * (11 + len(campi_pedigree(esemplari[0], per_codice, per_file)))]
        corpo = [r"""\documentclass[9pt,a4paper]{extarticle}
\usepackage[top=%(v)smm,bottom=%(v)smm,left=%(a)smm,right=%(m)smm]{geometry}
\def\DScaratteri{%(car)s}
\input{%(stile)s}
\usepackage[italian]{babel}
\usepackage{array}
\usepackage{url}\urlstyle{tt}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\setlength{\parindent}{0pt}
\pagestyle{plain}
\begin{document}
{\DStitoli\bfseries\fontsize{20}{24}\selectfont\color{DSrosso} Pedigree, gruppo %(gr)s}\par
{\DSdati\small\color{DSseppia} %(n)d esemplari, %(stato)s. Generato da tools/design-system.py e tools/stampa-collezione.py.}\par\medskip
""" % {"v": g["margine_verticale_mm"], "a": g["margine_anelli_mm"], "m": g["margine_mm"], "car": caratteri,
       "stile": os.path.join(DS, "collezione-stile.tex").replace("\\", "/"), "gr": tex(gruppo), "n": len(esemplari),
       "stato": tex(stato)}]
        for e in esemplari:
            img = miniatura(e, cartella_immagini, cache)
            corpo.append(scheda_tex(e, gruppo, per_codice, per_file, img, storie))
            valori = [v for _, v in campi_pedigree(e, per_codice, per_file)]
            # ADR-111: gli esemplari delle cartucce vere del proprietario portano allenatori reali, il suo e quelli di chi
            # glieli ha scambiati; nel documento tracciato e pubblico l'allenatore diventa un segnaposto, e il valore vero
            # resta solo nel PDF, che sta in _notes/ e non entra in Git. Anche PID ed EC restano, perche' non identificano
            # una persona.
            if e["origine"].startswith(ORIGINI_PRIVATE):
                etichette = [k for k, _ in campi_pedigree(e, per_codice, per_file)]
                valori[etichette.index("allenatore")] = "<ALLENATORE DELLA CARTUCCIA>"
            md.append("| " + " | ".join(str(x).replace("|", "/") for x in [
                e["box"], e["posto"], "%d %s" % (e["numero"], e["specie"]), e["forma"], e["sesso"],
                "sì" if e["cromatico"] else "", evento_di(e, per_codice, per_file),
                " ".join(x for x in [(stato_esemplare(e) or ("", "", ""))[2], storia_di(e, storie)[0]] if x),
                " ".join(storia_di(e, storie)[1])] + valori +
                ["conforme" if e["conforme"] else "NON conforme", e["impronta"]]) + " |")
        corpo.append(r"\end{document}")
        with io.open(os.path.join(PEDIGREE_MD, gruppo + ".md"), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(md) + "\n")
        uscita = os.path.join(PEDIGREE_PDF, gruppo + ".tex")
        with io.open(uscita, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(corpo) + "\n")
        if pdf:
            r = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", os.path.basename(uscita)],
                               cwd=PEDIGREE_PDF, capture_output=True, text=True, encoding="utf-8", errors="replace")
            if r.returncode != 0:
                print(r.stdout[-3000:])
                sys.exit("lualatex non ha compilato il pedigree di " + gruppo)
            for est in (".aux", ".log"):
                ausiliario = os.path.splitext(uscita)[0] + est
                if os.path.exists(ausiliario):
                    os.remove(ausiliario)
        print("%s: %d esemplari; %s%s" % (gruppo, len(esemplari), os.path.relpath(os.path.join(PEDIGREE_MD, gruppo + ".md"), RADICE),
                                          ", " + os.path.splitext(uscita)[0] + ".pdf" if pdf else ""))
    mancanti = sorted(k for k, v in cache.items() if v is None)
    print("miniature %d, senza illustrazione %d %s" % (len(cache), len(mancanti), mancanti[:10]))


# Il catalogo vivente di tutto HOME (ADR-127, ADR-138): un documento solo, in inglese su richiesta del proprietario del
# 2026-11-23, con i gruppi nell'ordine dei giri, cosi' che un giro nuovo aggiunga pagine in coda senza cambiare quelle
# gia' stampate. La copertina non si fora; dalla pagina 2 i fori a quattro con passo di 80 mm. I racconti degli eventi
# vengono da data/racconti-eventi.json, scritto da agenti sui soli dati del progetto e controllato da --check-racconti.
RACCONTI = os.path.join(RADICE, "pokedex-home-completo", "data", "racconti-eventi.json")
COLLEZIONE_PDF = os.path.join(RADICE, "_notes", "stampa", "collezione")
COPERTINA_COLLEZIONE = os.path.join(RADICE, "gba-save-extraction-smeraldo", "figure", "copertina-collezione.png")
GAMES_EN = {"RD": "Red", "GN": "Green", "BU": "Blue", "YW": "Yellow", "GD": "Gold", "SI": "Silver", "C": "Crystal",
            "R": "Ruby", "S": "Sapphire", "E": "Emerald", "FR": "FireRed", "LG": "LeafGreen", "CXD": "Colosseum/XD",
            "D": "Diamond", "P": "Pearl", "Pt": "Platinum", "HG": "HeartGold", "SS": "SoulSilver", "B": "Black",
            "W": "White", "B2": "Black 2", "W2": "White 2", "X": "X", "Y": "Y", "OR": "Omega Ruby", "AS": "Alpha Sapphire",
            "SN": "Sun", "MN": "Moon", "US": "Ultra Sun", "UM": "Ultra Moon"}
BALLS_EN = {"Bis Ball": "Repeat Ball", "Chic Ball": "Luxury Ball", "Cura Ball": "Heal Ball", "Esca Ball": "Lure Ball",
            "Gara Ball": "Sport Ball", "Luna Ball": "Moon Ball", "Mega Ball": "Great Ball", "Minor Ball": "Nest Ball",
            "Peso Ball": "Heavy Ball", "Pregio Ball": "Cherish Ball", "Rapid Ball": "Fast Ball", "Rete Ball": "Net Ball",
            "Scuro Ball": "Dusk Ball", "Sub Ball": "Dive Ball", "UC Ball": "Beast Ball", "Velox Ball": "Quick Ball"}
NATURES_EN = {"Ardita": "Hardy", "Schiva": "Lonely", "Audace": "Brave", "Decisa": "Adamant", "Birbona": "Naughty",
              "Sicura": "Bold", "Docile": "Docile", "Placida": "Relaxed", "Scaltra": "Impish", "Fiacca": "Lax",
              "Timida": "Timid", "Lesta": "Hasty", "Seria": "Serious", "Allegra": "Jolly", "Ingenua": "Naive",
              "Modesta": "Modest", "Mite": "Mild", "Quieta": "Quiet", "Ritrosa": "Bashful", "Ardente": "Rash",
              "Calma": "Calm", "Gentile": "Gentle", "Vivace": "Sassy", "Cauta": "Careful", "Furba": "Quirky"}


STORIE_EN = os.path.join(RADICE, "pokedex-home-completo", "data", "storie-en.json")
DATE_EVENTI = os.path.join(RADICE, "pokedex-home-completo", "data", "date-eventi.json")
MESI_IT = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre",
           "novembre", "dicembre"]


def _modulo_racconti():
    import importlib.util
    spec = importlib.util.spec_from_file_location("racconti_eventi", os.path.join(RADICE, "tools", "racconti-eventi.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def carica_racconti():
    """I racconti delle carte, le storie libere tradotte e le date d'inizio delle distribuzioni, tutti tracciati."""
    leggi = lambda p: json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else {}
    return {"carte": leggi(RACCONTI), "storie": leggi(STORIE_EN), "date": leggi(DATE_EVENTI),
            "in_inglese": _modulo_racconti().in_inglese}


def testo_en(e, evento, storia, racconti):
    return racconti["carte"].get(evento) or racconti["storie"].get(storia) or racconti["in_inglese"](storia or "")


def data_storica(e, evento, storia, racconti):
    """Il giorno in cui l'esemplare o il suo evento sono nati nella storia del gioco, o None se il progetto lo ha
    prodotto senza un evento (uova e catture): mai la data di produzione del 2026 né il giorno del Poké Transfer."""
    if evento in racconti["date"]:
        return racconti["date"][evento]
    carta = "(carta" in evento or re.search(r"\bWC\d|evento \(", evento)
    if carta and e["generazione"] >= 4 and (e["data_incontro"] or "9") < "2026":
        return e["data_incontro"]
    for g in re.finditer(r"(\d{4})-(\d{2})-(\d{2})|(\d{1,2}) (%s) (\d{4})" % "|".join(MESI_IT), storia or ""):
        d = g.group(0) if g.group(1) else "%s-%02d-%02d" % (g.group(6), MESI_IT.index(g.group(5)) + 1, int(g.group(4)))
        if d < "2026" and not ("Poké Transfer" in (storia or "")[max(0, g.start() - 40):g.start()]):
            return d
    return None


def scheda_en(e, gruppo, per_codice, per_file, img, storie, racconti):
    evento = evento_di(e, per_codice, per_file)
    storia, collegamenti = storia_di(e, storie)
    testo = testo_en(e, evento, storia, racconti)
    nel_lotto = racconti["in_inglese"](data_nel_lotto(e).replace("file del lotto non disponibile", "batch file not available")
                                       .replace("nessuna: il formato", "none: the format").replace("non registra la data", "does not store the date")
                                       .replace("uovo ricevuto il", "egg received on").replace("uguale alla copia", "same as the copy")
                                       .replace("non registrata", "not recorded"))
    campi = [("origin game", GAMES_EN.get(e["gioco"], e["gioco"])), ("met location", e["luogo"]),
             ("met date", e["data_incontro"] or "not recorded"), ("date in the batch", nel_lotto),
             ("level", "%d, met at %d" % (e["livello"], e["livello_incontro"])),
             ("ball", BALLS_EN.get(e["sfera"], e["sfera"])), ("language", e["lingua"]),
             ("OT", "%s, ID %s, SID %s" % (e["allenatore"], e["id"], e["sid"])),
             ("nature", NATURES_EN.get(e["natura"], e["natura"])), ("ability", e.get("abilita_en") or e["abilita"]),
             ("moves", ", ".join(e.get("mosse_en") or e["mosse"]) or "none"), ("held item", e["oggetto"] or "none"),
             ("ribbons", ", ".join(e["fiocchi"]) or "none"), ("IVs", "/".join(str(v) for v in e["iv"])),
             ("PID", e["pid"]), ("EC", e["ec"])]
    celle = [" & ".join("\\DScampo{%s} & %s" % (tex(k), tex(v)) for k, v in campi[i:i + 3]) + r"\\"
             for i in range(0, len(campi), 3)]
    forma = e.get("forma_en") or e["forma"]
    nome = tex(e["specie"]) + (" \\textnormal{\\small %s}" % tex(forma) if forma else "")
    segni = {"M": "♂", "F": "♀"}.get(e["sesso"], "") + (" ★" if e["cromatico"] else "")
    mini = r"\DSminiatura[14mm]{%s}" % img if img else r"\tcbox[colback=DScartascura, colframe=DSfiletto, boxrule=0.4pt, arc=1.6mm, width=14mm, height=14mm]{}"
    gen = "DSgen" + "ABCDEFG"[max(1, min(7, e["generazione"])) - 1]
    return "\n".join([
        r"\begin{DSscheda}{%s}" % gen,
        r"\begin{minipage}[t]{16mm}\vspace{0pt}%s\end{minipage}\hspace{2mm}%%" % mini,
        r"\begin{minipage}[t]{\dimexpr\linewidth-18mm\relax}\vspace{0pt}",
        r"{\DStitoli\bfseries %s}\hspace{1.5mm}\DSnumero{%03d}\hspace{1.5mm}{\DSdati %s}\hfill\DSstato{DSstatoinhome}{in HOME}\par" % (
            nome, e["numero"], segni),
        r"{\footnotesize %s}\par" % tex(racconti["in_inglese"](evento)),
        (r"{\scriptsize\itshape %s}\par" % tex(testo)) if testo else "",
        (r"{\DSdati\tiny\color{DSseppia} Sources: %s}\par" % "; ".join(r"\url{%s}" % u for u in collegamenti)) if collegamenti else "",
        r"\vspace{0.6mm}",
        r"{\DSdati\scriptsize\setlength{\tabcolsep}{2pt}\begin{tabular}{@{}l L{29mm} l L{30mm} l L{34mm}@{}}",
        *celle,
        r"\end{tabular}}\par",
        r"{\DSdati\tiny\color{DSseppia} %s, PKHeX %s; batch %s, box %d, slot %d, HOME label Bank %d; fingerprint {\ttfamily %s}}" % (
            "legal" if e["conforme"] else "NOT legal", tex(e["libreria"]), tex(gruppo), e["box"], e["posto"], e["box"],
            e["impronta"]),
        r"\end{minipage}",
        r"\end{DSscheda}",
    ])


def esemplari_in_home(dati):
    """I gruppi in HOME nell'ordine dei giri, senza chi resta in console e senza chi si libera (ADR-126)."""
    per_gruppo = {c["gruppo"]: c["esemplari"] for c in dati["copie"]}
    for gruppo in STATO_GRUPPO:
        if gruppo in per_gruppo and STATO_GRUPPO[gruppo][1] == "in HOME":
            yield gruppo, [e for e in per_gruppo[gruppo]
                           if not resta_in_console(e) and e.get("impronta") not in SOSTITUITI]


def check_racconti(dati):
    per_codice, per_file = descrizioni_del_progetto()
    racconti = carica_racconti()["carte"]
    eventi = {evento_di(e, per_codice, per_file) for _, es in esemplari_in_home(dati) for e in es}
    carte = sorted(x for x in eventi if "(carta" in x or re.search(r"\bWC\d|evento \(", x))
    mancano = [x for x in carte if x not in racconti]
    print("eventi con carta %d, con racconto %d, senza %d" % (len(carte), len(carte) - len(mancano), len(mancano)))
    for x in mancano[:20]:
        print("  senza racconto:", x)
    return 1 if mancano else 0


def collezione(dati, cartella_immagini, pdf):
    per_codice, per_file = descrizioni_del_progetto()
    storie, racconti, cache = carica_storie(), carica_racconti(), {}
    g = json.load(io.open(os.path.join(DS, "tokens.json"), encoding="utf-8"))["geometria"]
    caratteri = os.path.join(RADICE, "_notes", "design-system", "caratteri").replace("\\", "/") + "/"
    os.makedirs(COLLEZIONE_PDF, exist_ok=True)
    gruppi = list(esemplari_in_home(dati))
    totale = sum(len(es) for _, es in gruppi)
    corpo = [r"""\documentclass[9pt,a4paper]{extarticle}
\usepackage[top=%(v)smm,bottom=%(v)smm,left=%(a)smm,right=%(m)smm]{geometry}
\def\DScaratteri{%(car)s}
\input{%(stile)s}
\usepackage{babel}\babelprovide[import,main]{english}
\usepackage{array}
\usepackage{graphicx}
\usepackage{url}\urlstyle{tt}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\setlength{\parindent}{0pt}
\pagestyle{plain}
\begin{document}
""" % {"v": g["margine_verticale_mm"], "a": g["margine_anelli_mm"], "m": g["margine_mm"], "car": caratteri,
       "stile": os.path.join(DS, "collezione-stile.tex").replace("\\", "/")}]
    if os.path.exists(COPERTINA_COLLEZIONE):
        corpo.append(r"\newgeometry{margin=9mm}\thispagestyle{empty}\centering\includegraphics[width=\linewidth,height=\textheight,keepaspectratio]{%s}\restoregeometry\clearpage\raggedright"
                     % COPERTINA_COLLEZIONE.replace("\\", "/"))
    # dal 2026-11-23, su richiesta del proprietario: ordine cronologico, cioe' il giorno dell'evento o della cattura vera
    # di ciascun esemplare; poi, in un'appendice, quelli che il progetto ha prodotto senza un evento, per numero di
    # Pokedex. Un lotto nuovo puo' quindi inserire pagine in mezzo: il documento si stampa intero quando lo stato e' fermo.
    tutti = []
    for gruppo, es in gruppi:
        for e in es:
            evento = evento_di(e, per_codice, per_file)
            storia = storia_di(e, storie)[0]
            tutti.append((data_storica(e, evento, storia, racconti), e, gruppo))
    datati = sorted((x for x in tutti if x[0]), key=lambda x: (x[0], x[1]["numero"], x[1].get("forma_n", 0)))
    senza = sorted((x for x in tutti if not x[0]), key=lambda x: (x[1]["numero"], x[1].get("forma_n", 0), x[2]))
    corpo.append(r"""{\DStitoli\bfseries\fontsize{20}{24}\selectfont\color{DSrosso} The HOME living collection}\par
{\DSdati\small\color{DSseppia} %d Pokémon from %d batches. Part one, %d Pokémon, follows history: each one sits on the day its event was distributed, or the day it was really caught. Part two, %d Pokémon produced by the project without an event (eggs and catches), follows the National Pokédex. Every card lists the event story, the batch, box and slot of the copy it came from, the HOME label (Bank N) under which it is filed in HOME, and all data read by PKHeX. Generated by tools/stampa-collezione.py --collezione.}\par\clearpage""" % (totale, len(gruppi), len(datati), len(senza)))
    anno = None
    for data, e, gruppo in datati:
        if data[:4] != anno:
            anno = data[:4]
            corpo.append(r"\clearpage{\DStitoli\bfseries\Large\color{DSrosso} %s}\par\medskip" % anno)
        corpo.append(scheda_en(e, gruppo, per_codice, per_file, miniatura(e, cartella_immagini, cache), storie, racconti))
    corpo.append(r"\clearpage{\DStitoli\bfseries\Large\color{DSrosso} Produced by the project, in National Pokédex order}\par\medskip")
    for _, e, gruppo in senza:
        corpo.append(scheda_en(e, gruppo, per_codice, per_file, miniatura(e, cartella_immagini, cache), storie, racconti))
    # Chi e' in HOME senza venire da una copia: gli arrivi da GO e i doni, dal documento autorato, e i 34 che HOME conteneva
    # prima del giro 1 (964 dopo il giro di 930, ROADMAP.md), che il progetto non ha mai letto.
    go = []
    percorso_go = os.path.join(RADICE, "pokedex-home-completo", "ESEMPLARI-DA-GO.md")
    if os.path.exists(percorso_go):
        testo_go = io.open(percorso_go, encoding="utf-8").read()
        sezione = testo_go.split("## Gli esemplari", 1)[-1].split("\n## ", 1)[0]
        for riga in sezione.splitlines():
            celle = [c.strip() for c in riga.strip().strip("|").split("|")]
            if riga.startswith("| ") and len(celle) >= 2 and celle[0] not in ("Esemplare",) and not riga.startswith("|---"):
                data = re.search(r"\d{4}-\d{2}-\d{2}", celle[1])
                go.append("%s (%s)" % (celle[0], data.group(0) if data else "date not recorded"))
    corpo.append(r"\clearpage{\DStitoli\bfseries\Large\color{DSrosso} In HOME but not from the project's batches}\par\medskip")
    corpo.append(r"{\small %d Pokémon arrived from Pokémon GO or as HOME gifts: %s. Their details are in pokedex-home-completo/ESEMPLARI-DA-GO.md. 34 Pokémon were already in HOME before the first batch of 2026-11-03 (HOME counted 964 after a batch of 930); the project has never read them, so they are not documented here yet.}\par" % (
        len(go), tex("; ".join(go)) or "none"))
    corpo.append(r"\clearpage")
    corpo.append(r"\end{document}")
    uscita = os.path.join(COLLEZIONE_PDF, "HOME-COLLECTION.tex")
    with io.open(uscita, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(corpo) + "\n")
    print("collezione: %d esemplari in %d gruppi; %s" % (totale, len(gruppi), uscita))
    if not pdf:
        return
    r = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", os.path.basename(uscita)],
                       cwd=COLLEZIONE_PDF, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(r.stdout[-3000:])
        sys.exit("lualatex non ha compilato la collezione")
    for est in (".aux", ".log", ".tex"):
        ausiliario = os.path.splitext(uscita)[0] + est
        if os.path.exists(ausiliario):
            os.remove(ausiliario)
    fora(os.path.splitext(uscita)[0] + ".pdf")


def fora(percorso):
    """I fori a quattro con passo di 80 mm dalla pagina 2: la copertina si incolla sopra il quaderno (ADR-138)."""
    import fitz
    mm = 72 / 25.4
    documento = fitz.open(percorso)
    for indice, pagina in enumerate(documento):
        if indice == 0:
            continue
        orizzontale = pagina.rect.width > pagina.rect.height
        for pos in (28.5, 108.5, 188.5, 268.5):
            centro = fitz.Point(pos * mm, 12 * mm) if orizzontale else fitz.Point(12 * mm, pos * mm)
            pagina.draw_circle(centro, 2.75 * mm, color=(0.55, 0.55, 0.55), width=0.4)
    temporaneo = percorso + ".tmp"
    documento.save(temporaneo, garbage=3, deflate=True)
    documento.close()
    os.replace(temporaneo, percorso)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dati", help="JSON di tools/pkhex-elenco-copie")
    ap.add_argument("--immagini", default=IMMAGINI, help="cartella delle illustrazioni, divisa per generazione")
    ap.add_argument("--pdf", action="store_true", help="compila anche i PDF con lualatex")
    ap.add_argument("--gruppo", action="append", help="solo questo gruppo; si ripete")
    ap.add_argument("--collezione", action="store_true", help="il catalogo vivente di tutto HOME in un documento solo, in inglese (ADR-138)")
    ap.add_argument("--check-racconti", action="store_true", help="esce con 1 se un evento con carta in HOME non ha il racconto")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    dati = json.load(io.open(a.dati, encoding="utf-8"))
    if a.check_racconti:
        sys.exit(check_racconti(dati))
    if a.collezione:
        collezione(dati, a.immagini, a.pdf)
        return
    pedigree(dati, a.immagini, a.pdf, a.gruppo)


if __name__ == "__main__":
    main()
