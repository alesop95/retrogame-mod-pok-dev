#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L'elenco unico di produzione dei giri dedicati prima della chiusura di Bank, e quanti esemplari chiede.

Perché esiste
-------------
Le voci da produrre sono nate in quattro decisioni successive, ADR-108, ADR-109, ADR-110 e ADR-111, e ciascuna ha
il suo documento: le caselle in `COPERTURA-LOTTI.md`, le sfide in `SFIDE-BANK.md`, sfere e fiocchi nei due documenti
di ADR-110, gli assi da collezionista nel foglio «Bank Closing». Il proprietario ha chiesto il 2026-11-04 un elenco
solo, e ha posto la condizione che i posti di HOME bastino. Questo strumento mette insieme tutte le voci, toglie
quelle che le copie per HOME coprono già, e misura quanti esemplari servono.

Il conto degli esemplari è una stima, e si dichiara tale. Un esemplare solo chiude più voci quando i vincoli sono
compatibili: la stessa specie e forma, giochi d'origine che si intersecano, la stessa sfera o nessun vincolo di
sfera, lo stesso stato cromatico. Lo strumento fonde le voci per scelta golosa su questi soli vincoli; non chiede alla
libreria se la combinazione sia legale, quindi la stima può essere ottimista. Il tetto, cioè una voce un esemplare,
non lo è. Le voci che sono un incontro preciso (uno scambio in gioco, un dono, un esemplare della cartuccia, una
riga delle stelle o dei livelli minimi, il Fiocco Maestro) restano un esemplare ciascuna, e possono assorbire una
casella della stessa specie. Le mosse non hanno una specie: si assegnano dopo a un esemplare che le impari, e si
contano a parte, fra zero e una per mossa.

Le coperture degli assi sono misurate dove i dati delle copie lo permettono: l'origine sul gioco, gli scambi
sull'incontro di scambio, gli altri esemplari unici sul gioco e su un incontro non selvatico, i livelli minimi sul
livello. Il sesso e la forma per origine e le stelle del Master Dex non hanno un campo corrispondente nelle copie, e
si contano tutte da produrre, dichiarandolo.

Uso
---
    python tools/elenco-produzione.py            riepilogo
    python tools/elenco-produzione.py --scrivi   scrive pokedex-home-completo/ELENCO-PRODUZIONE.md e
                                                 _notes/lavoro/elenco-produzione.json
"""

import argparse
import collections
import csv
import importlib.util
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAVORO = os.path.join(RADICE, "_notes", "lavoro", "giudizi-copie")
ASSI = os.path.join(RADICE, "_notes", "fonti", "raccolte", "fogli-sfide-bank-2026-11-03", "assi")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "ELENCO-PRODUZIONE.md")
USCITA_JSON = os.path.join(RADICE, "_notes", "lavoro", "elenco-produzione.json")
POSTI_HOME = 9000
COPIE_FATTE = 3407          # COPIE-PER-HOME.md, 3272 per HOME, 121 decisione finale, 14 giapponesi
TETTO_STATICI = 2371        # ADR-106, tools/pkhex-conta-incontri


def modulo(nome):
    spec = importlib.util.spec_from_file_location(nome.replace("-", "_"), os.path.join(RADICE, "tools", nome + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# I giochi del foglio, scritti come li scrive il foglio, nei codici di gioco delle copie.
CODICI = {"RBY": {"RD", "GN", "BU", "YW"}, "RB": {"RD", "GN", "BU"}, "RG": {"RD", "GN"}, "B": {"B"}, "W": {"W"},
          "Yellow": {"YW"}, "Y": {"YW"}, "Blue (Jp)": {"BU"}, "GSC": {"GD", "SI", "C"}, "GS": {"GD", "SI"},
          "G": {"GD"}, "Gold": {"GD"}, "Crystal": {"C"}, "C": {"C"}, "HGSS": {"HG", "SS"}, "HG": {"HG"}, "SS": {"SS"},
          "RSE": {"R", "S", "E"}, "RS": {"R", "S"}, "E": {"E"}, "Emerald": {"E"}, "FRLG": {"FR", "LG"}, "FR": {"FR"},
          "LG": {"LG"}, "ORAS": {"OR", "AS"}, "OR": {"OR"}, "AS": {"AS"}, "DPPt": {"D", "P", "Pt"}, "DP": {"D", "P"},
          "Pt": {"Pt"}, "BW": {"B", "W"}, "B2W2": {"B2", "W2"}, "BWB2W2": {"B", "W", "B2", "W2"},
          "BWB2W3": {"B", "W", "B2", "W2"}, "B2": {"B2"}, "W2": {"W2"}, "XY": {"X", "Y"}, "SM": {"SN", "MN"},
          "USUM": {"US", "UM"}, "SMUSUM": {"SN", "MN", "US", "UM"}, "US": {"US"}, "UM": {"UM"},
          "Colosseum": {"CXD"}, "XD: Gale of Darkness": {"CXD"}, "Dream Radar": {"B2", "W2"},
          "My Pokémon Ranch": {"D", "P", "Pt"}, "Battle Revolution": {"D", "P", "Pt"}}


def giochi_foglio(testo):
    """I codici di gioco di una cella del foglio, o None se la cella non vincola (Any) o non è riconosciuta."""
    testo = (testo or "").strip()
    if not testo or testo == "Any":
        return None
    if testo in CODICI:
        return set(CODICI[testo])
    out = set()
    for parte in testo.replace("+", " ").split():
        if parte in CODICI:
            out |= CODICI[parte]
    return out or None


def nota(testo, n):
    """Una nota del foglio, senza le formule e gli indirizzi d'immagine che il foglio vi incolla, tagliata a n caratteri."""
    testo = re.sub(r'=image\([^)]*\)|https?://\S+', "", testo or "", flags=re.I).strip()
    return testo[:n]


def num(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return None


def righe(nome):
    with open(os.path.join(ASSI, nome), encoding="utf-8") as f:
        return list(csv.reader(f))


def voce(categoria, testo, numero=None, forma_n=0, giochi=None, sfera=None, cromatico=None, unico=False,
         coperta=False, misurata=True, sesso=None):
    return {"categoria": categoria, "voce": testo, "numero": numero, "forma_n": forma_n,
            "giochi": sorted(giochi) if giochi else None, "sfera": sfera, "cromatico": cromatico, "sesso": sesso,
            "unico": unico, "coperta": coperta, "misurata": misurata}


def raccogli():
    cop = modulo("copertura-lotti")
    sfi = modulo("sfide-bank")
    fes = modulo("fiocchi-e-sfere-prima-di-bank")
    attese = json.load(open(cop.ATTESE, encoding="utf-8"))
    copie = [x for c in json.load(open(cop.COPIE, encoding="utf-8"))["copie"] if c["gruppo"].startswith("HOME")
             for x in c["esemplari"]]
    nomi = {v["numero"]: v["specie"] for v in attese if v["forma_n"] == 0}
    nomi_forma = {(v["numero"], v["forma_n"]): v["forma"] for v in attese}
    home = {(x["numero"], x["forma_n"]) for x in copie}
    voci = []

    # ADR-109: le caselle fino alla settima generazione che le copie non coprono.
    for v in attese:
        if cop.escluso(v["numero"], v["forma_n"]):
            continue
        if (v["numero"], v["forma_n"]) not in home:
            voci.append(voce("caselle", "casella %s%s" % (v["specie"], " " + v["forma"] if v["forma_n"] else ""),
                             v["numero"], v["forma_n"]))

    # ADR-108: le sfide di HOME che dipendono da Bank, una voce per specie mancante con l'origine richiesta.
    for t in sfi.SFIDE:
        testo, specie, giochi, cromatico = t[:4]
        forme = t[5] if len(t) > 5 else None
        eventi = t[6] if len(t) > 6 else None
        for n in specie:
            if not any(sfi.soddisfa(x, n, giochi, cromatico, forme, eventi) for x in copie):
                voci.append(voce("sfide", "%s, per «%s»" % (nomi.get(n, n), testo), n, 0, giochi,
                                 cromatico=True if cromatico else None, unico=bool(eventi)))

    # ADR-108: i cromatici bloccati, ottenibili solo da Bank.
    for n in (151, 251, 327, 772, 804):
        if not any(x["numero"] == n and x["cromatico"] for x in copie):
            voci.append(voce("cromatici", "%s cromatico" % nomi.get(n, n), n, 0, cromatico=True))
    # Dal video `yyIa9611uZk`, trascritto in locale il 2026-11-04: cromatici che il video dà bloccati dietro Bank e che le
    # copie non hanno. Il video non dice se siano legali; la libreria lo decide prima della produzione.
    for n in (386, 490, 491):
        if not any(x["numero"] == n and x["cromatico"] for x in copie):
            voci.append(voce("cromatici", "%s cromatico, dal video yyIa9611uZk, legalità da verificare con la libreria"
                             % nomi.get(n, n), n, 0, cromatico=True))

    # ADR-110: le abilità registrabili solo da Bank.
    for n, f, ab in ((74, 1, "Galvanize"), (88, 1, "Power of Alchemy")):
        if not any(x["numero"] == n and x["forma_n"] == f and x.get("abilita_en") == ab for x in copie):
            voci.append(voce("abilità", "%s di Alola con %s" % (nomi.get(n, n), ab), n, f))

    # ADR-110: le combinazioni di specie e sfera perse dall'eredità e quelle precise del foglio.
    sfere = json.load(open(fes.SFERE, encoding="utf-8"))
    nelle = {(x["numero"], x["forma_n"], x["sfera"]) for x in copie}
    for v in sfere["voci"]:
        for s in v["sfere_perse"]:
            if (v["numero"], v["forma_n"], s) not in nelle:
                voci.append(voce("sfere", "%s%s in %s" % (v["specie"], " " + v["forma"] if v["forma_n"] else "", s),
                                 v["numero"], v["forma_n"], sfera=s))
    for n, nome, crom, s, gioco in fes.COPPIE_FOGLIO:
        if not any(x["numero"] == n and x["sfera"] == s and x["cromatico"] == crom for x in copie):
            voci.append(voce("coppie precise", "%s%s in %s, da %s" % (nome, " cromatico" if crom else "", s, gioco),
                             n, 0, sfera=s, cromatico=crom, unico=True))

    # ADR-110: il Fiocco Maestro, da una delle 18 specie Ombra che arrivano in tutti i giochi con fiocchi.
    voci.append(voce("Fiocco Maestro", "Fiocco Maestro da una specie Ombra di Colosseum o XD, `FIOCCHI-PRIMA-DI-BANK.md`",
                     None, None, {"CXD"}, unico=True))

    # ADR-110: gli esemplari conformi della cartuccia originale di Smeraldo.
    cart = json.load(open(os.path.join(LAVORO, "cartucce-originali.json"), encoding="utf-8"))["copie"]
    for c in cart:
        if c["gruppo"] != "SMERALDO":
            continue
        for x in c["esemplari"]:
            if x["conforme"]:
                voci.append(voce("Smeraldo", "%s della cartuccia, box %d posto %d" % (x["specie"], x["box"], x["posto"]),
                                 x["numero"], x["forma_n"], {"E"}, unico=True))

    # ADR-111: i sei assi del foglio «Bank Closing».
    def presente(n, giochi, cond=lambda x: True):
        return any(x["numero"] == n and (giochi is None or x["gioco"] in giochi) and cond(x) for x in copie)

    for r in righe("asse-origine.csv"):
        n = num(r[4]) if len(r) > 8 else None
        if n:
            g = giochi_foglio(r[8])
            voci.append(voce("asse origine", "%s con origine %s" % (nomi.get(n, r[5]), r[8]), n, 0, g,
                             coperta=presente(n, g)))
    # Il sesso e la forma regionale si misurano sulle copie; le altre forme del foglio sono scritte in inglese e non
    # hanno un numero di forma, quindi restano voci a sé, non misurate.
    for r in righe("asse-sesso-forma-origine.csv"):
        n = num(r[4]) if len(r) > 9 else None
        if not n:
            continue
        g = giochi_foglio(r[8])
        testo = "%s %s, origine %s" % (nomi.get(n, r[5]), nota(r[9], 60) or "forma", r[8])
        if r[9] in ("♂", "♀"):
            sx = "M" if r[9] == "♂" else "F"
            voci.append(voce("asse sesso e forma", testo, n, 0, g, sesso=sx,
                             coperta=presente(n, g, lambda x: x["sesso"] == sx)))
        elif r[9] == "Alolan Form":
            voci.append(voce("asse sesso e forma", testo, n, 1, g, coperta=presente(n, g, lambda x: x["forma_n"] == 1)))
        else:
            voci.append(voce("asse sesso e forma", testo, n, None, g, unico=True, misurata=False))
    for r in righe("asse-scambi-altro-ot.csv"):
        n = num(r[2]) if len(r) > 6 else None
        if n:
            g = giochi_foglio(r[1])
            voci.append(voce("asse scambi", "%s «%s» di %s, %s" % (nomi.get(n, r[3]), r[5], r[6], r[1]), n, 0, g,
                             unico=True, coperta=presente(n, g, lambda x: "Trade" in x.get("evento", ""))))
    for r in righe("asse-altri-unici.csv")[1:]:
        if len(r) > 5 and r[4] and r[4] != "Games":
            nome = r[1].split(" x")[0].strip()
            n = num(r[0]) or next((k for k, v in nomi.items() if v == nome), None)
            g = giochi_foglio(r[4])
            voci.append(voce("asse altri unici", "%s, %s: %s" % (r[1], r[4], nota(r[5], 80)), n, 0 if n else None, g, unico=True,
                             coperta=bool(n) and presente(n, g, lambda x: not x.get("evento", "").startswith("Wild"))))
    for r in righe("asse-stelle-master-dex.csv"):
        n = num(r[4]) if len(r) > 11 else None
        if n:
            voci.append(voce("asse stelle", "%s, %s, %s: %s" % (nomi.get(n, r[5]), r[11], r[8], nota(r[9], 70)), n, 0,
                             giochi_foglio(r[8]), unico=True, misurata=False))
    for r in righe("asse-livelli-minimi.csv"):
        n = num(r[0]) if len(r) > 5 else None
        if n:
            g = giochi_foglio(r[4])
            lv = num(r[5]) or 100
            voci.append(voce("asse livelli minimi", "%s al livello %s, %s" % (nomi.get(n, r[1]), r[5], r[4]), n, 0, g,
                             unico=True, coperta=presente(n, g, lambda x: x["livello"] <= lv)))

    # ADR-110: le mosse che esistono fino alla settima generazione e che nessuna copia conosce.
    mosse = json.load(open(os.path.join(LAVORO, "mosse-fino-gen7-mancanti.json"), encoding="utf-8"))["mancanti_fino_gen7"]
    return voci, mosse, nomi, nomi_forma


def compatibili(a, b):
    if a["numero"] != b["numero"] or a["forma_n"] != b["forma_n"] or a["numero"] is None:
        return False
    if a["giochi"] and b["giochi"] and not set(a["giochi"]) & set(b["giochi"]):
        return False
    if a["sfera"] and b["sfera"] and a["sfera"] != b["sfera"]:
        return False
    if a["cromatico"] is not None and b["cromatico"] is not None and a["cromatico"] != b["cromatico"]:
        return False
    if a.get("sesso") and b.get("sesso") and a["sesso"] != b["sesso"]:
        return False
    return True


def fondi(voci):
    """Scelta golosa: prima gli incontri precisi, ciascuno un esemplare; poi le altre voci, ciascuna nel primo
    esemplare compatibile o in uno nuovo. Un incontro preciso assorbe solo voci senza vincolo di sfera né di cromatico."""
    esemplari = []
    for v in sorted(voci, key=lambda v: not v["unico"]):
        for e in esemplari:
            if e["unico"] and v["unico"]:
                continue
            if e["unico"] and (v["sfera"] or v["cromatico"]):
                continue
            if compatibili(e, v):
                e["voci"].append(v["voce"])
                for k in ("giochi", "sfera", "cromatico", "sesso"):
                    if v[k] and not e[k]:
                        e[k] = v[k]
                if e["giochi"] and v["giochi"]:
                    e["giochi"] = sorted(set(e["giochi"]) & set(v["giochi"]))
                break
        else:
            esemplari.append(dict(v, voci=[v["voce"]]))
    return esemplari


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scrivi", action="store_true")
    a = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    voci, mosse, nomi, nomi_forma = raccogli()
    per = collections.OrderedDict()
    for v in voci:
        c = per.setdefault(v["categoria"], {"totale": 0, "coperte": 0, "non_misurate": 0})
        c["totale"] += 1
        c["coperte"] += bool(v["coperta"])
        c["non_misurate"] += not v["misurata"]
    da = [v for v in voci if not v["coperta"]]
    esemplari = fondi(da)
    tetto = len(da) + len(mosse)
    stima = len(esemplari)
    print("voci: %d, coperte dalle copie per HOME: %d, da produrre: %d; mosse senza specie: %d" %
          (len(voci), len(voci) - len(da), len(da), len(mosse)))
    for k, c in per.items():
        print("  %-20s totale %4d  coperte %4d  da produrre %4d%s" % (k, c["totale"], c["coperte"], c["totale"] - c["coperte"],
              ("  (%d senza misura possibile)" % c["non_misurate"]) if c["non_misurate"] else ""))
    print("esemplari: stima con fusione %d, tetto senza fusione %d (con le mosse a uno per mossa)" % (stima, tetto))
    for nome, n in (("stima", stima), ("tetto", tetto)):
        tot = COPIE_FATTE + TETTO_STATICI + n
        print("posti di HOME, %s: %d copie + %d statici + %d = %d su %d, restano %d" %
              (nome, COPIE_FATTE, TETTO_STATICI, n, tot, POSTI_HOME, POSTI_HOME - tot))
    if not a.scrivi:
        return 0
    os.makedirs(os.path.dirname(USCITA_JSON), exist_ok=True)
    with open(USCITA_JSON, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"voci": voci, "mosse": mosse, "esemplari": esemplari}, f, ensure_ascii=False, indent=1)
    r = ["# L'elenco unico di produzione prima della chiusura di Bank", "",
         "> Documento generato da `tools/elenco-produzione.py --scrivi`. Non si modifica a mano: si rigenera dopo ogni copia "
         "nuova e dopo ogni decisione che aggiunge voci. Mette insieme le voci di ADR-108, ADR-109, ADR-110 e ADR-111, toglie "
         "quelle che le copie per HOME coprono già (`tools/pkhex-elenco-copie`, PKHeX 26.10.18) e stima quanti esemplari "
         "servono. Lo stato di ciascuna voce e il suo perché stanno nei documenti di dettaglio citati in "
         "`DA-PORTARE-PRIMA-DI-BANK.md`; qui sta l'elenco da produrre.", "",
         "## Il conto", "",
         "| Categoria | Voci | Coperte dalle copie per HOME | Da produrre |", "|---|---|---|---|"]
    for k, c in per.items():
        cop = ("%d, e %d voci senza misura possibile" % (c["coperte"], c["non_misurate"])) if c["non_misurate"] else c["coperte"]
        r.append("| %s | %d | %s | %d |" % (k, c["totale"], cop, c["totale"] - c["coperte"]))
    r.append("| mosse senza specie | %d | 0 | %d, da assegnare a un esemplare che le impari |" % (len(mosse), len(mosse)))
    r += ["", "Voci da produrre: %d, più %d mosse. Esemplari stimati con la fusione delle voci compatibili: %d. Tetto, una "
          "voce un esemplare e una mossa un esemplare: %d. La stima non chiede alla libreria se una fusione sia legale, e "
          "può quindi essere ottimista; il tetto non lo è." % (len(da), len(mosse), stima, tetto), "",
          "I posti di HOME sono %d. Con le %d copie già fatte e il tetto di %d statici di ADR-106, che si sovrappone in parte "
          "agli altri esemplari unici e alle sfide, la stima porta a %d posti e il tetto a %d. Restano rispettivamente %d e "
          "%d posti per il lavoro su Switch dopo Bank." % (POSTI_HOME, COPIE_FATTE, TETTO_STATICI,
                                                          COPIE_FATTE + TETTO_STATICI + stima, COPIE_FATTE + TETTO_STATICI + tetto,
                                                          POSTI_HOME - COPIE_FATTE - TETTO_STATICI - stima,
                                                          POSTI_HOME - COPIE_FATTE - TETTO_STATICI - tetto), "",
          "Le coperture degli assi sono misurate sul gioco d'origine, sull'incontro di scambio, su un incontro non selvatico, "
          "sul livello, sul sesso e sulla forma di Alola, secondo l'asse. Le altre forme dell'asse del sesso e della forma, "
          "scritte in inglese nel foglio, e le stelle del Master Dex non hanno un campo corrispondente nelle copie e sono "
          "contate tutte da produrre.", "",
          "## Gli esemplari da produrre, con le voci che ciascuno chiude", "",
          "| Specie | Forma | Giochi d'origine | Sfera | Cromatico | Voci chiuse |", "|---|---|---|---|---|---|"]
    for e in sorted(esemplari, key=lambda e: (e["numero"] or 9999, e["forma_n"] or 0)):
        nome = nomi.get(e["numero"], "da scegliere") if e["numero"] else "da scegliere"
        forma = nomi_forma.get((e["numero"], e["forma_n"]), "") if e["forma_n"] else ""
        r.append("| %s | %s | %s | %s | %s | %s |" % (
            ("%d %s" % (e["numero"], nome)) if e["numero"] else nome, forma, ", ".join(e["giochi"] or []) or "qualunque",
            e["sfera"] or "", "sì" if e["cromatico"] else "", "; ".join(x.replace("|", "/") for x in e["voci"])))
    r += ["", "## Le mosse da assegnare", "", ", ".join(mosse) + "."]
    with open(USCITA, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(r) + "\n")
    print("Scritto " + os.path.relpath(USCITA, RADICE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
