#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Che cosa si perde con la chiusura di Bank sull'asse delle sfere e su quello dei fiocchi, e che cosa le copie già coprono.

Perché esiste
-------------
Il 2026-11-04 il proprietario ha chiesto due ricerche, che si aggiungono all'ultimo lotto prima della chiusura di Bank.
La prima riguarda le combinazioni di specie e Poké Ball che dopo il 26 febbraio 2027 nessuno potrà più creare da capo.
La seconda riguarda i fiocchi: il set minimo di esemplari che li porta tutti, e l'esemplare che ne può portare di più.
Entrambe le risposte vengono da misure ripetibili e non da elenchi della comunità, che restano controprove.

Da dove vengono i dati
----------------------
Le sfere vengono da `tools/pkhex-sfere-prima-di-bank`: eredità della settima generazione e sfere selvatiche dei giochi
per Switch, dalla libreria del verificatore. Spinda è escluso da Diamante Lucente e Perla Splendente per la tabella di
connettività di HOME. Le specie Ombra e i fiocchi dono vengono da `tools/pkhex-fiocchi-prima-di-bank`. L'elenco dei
fiocchi e dei giochi in cui si ottengono viene da Bulbapedia, «List of Ribbons in the games», letta attraverso l'API e
salvata sotto `_notes/fonti/raccolte/bulbapedia-2026-11-04/`. Le copie per HOME vengono da `tools/pkhex-elenco-copie`,
che dal 2026-11-04 scrive anche i fiocchi di ogni esemplare.

Uso
---
    python tools/fiocchi-e-sfere-prima-di-bank.py            riepilogo
    python tools/fiocchi-e-sfere-prima-di-bank.py --scrivi   scrive i due documenti generati
"""
import argparse
import collections
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAVORO = os.path.join(RADICE, "_notes", "lavoro", "giudizi-copie")
SFERE = os.path.join(LAVORO, "sfere-prima-di-bank.json")
FIOCCHI = os.path.join(LAVORO, "fiocchi-prima-di-bank.json")
COPIE = os.path.join(LAVORO, "dopo-bfe89c7-pedigree.json")
BULBA = os.path.join(RADICE, "_notes", "fonti", "raccolte", "bulbapedia-2026-11-04", "List_of_Ribbons_in_the_games.json")
DOC_SFERE = os.path.join(RADICE, "pokedex-home-completo", "SFERE-PRIMA-DI-BANK.md")
DOC_FIOCCHI = os.path.join(RADICE, "pokedex-home-completo", "FIOCCHI-PRIMA-DI-BANK.md")

# Le coppie precise della scheda «Unique Ball Matching» del foglio «Bank Closing all possible things checklist V0.5»,
# letta il 2026-11-04 dall'esportazione in `_notes/fonti/raccolte/fogli-sfide-bank-2026-11-03/`. Non nascono
# dall'eredità ma da incontri precisi, quindi lo strumento della libreria non le vede.
COPPIE_FOGLIO = [
    (151, "Mew", False, "Poké Ball", "Rosso Fuoco e Verde Foglia giapponesi"),
    (151, "Mew", False, "Premier Ball", "Rosso Fuoco e Verde Foglia giapponesi"),
    (151, "Mew", False, "Cura Ball", "Rosso Fuoco e Verde Foglia giapponesi"),
    (151, "Mew", True, "Sub Ball", "Rosso Fuoco e Verde Foglia giapponesi"),
    (151, "Mew", True, "Mega Ball", "Rosso Fuoco e Verde Foglia giapponesi"),
    (151, "Mew", True, "Poké Ball", "Rosso Fuoco e Verde Foglia giapponesi"),
    (327, "Spinda", True, "Minor Ball", "qualunque gioco dalla terza alla settima generazione"),
    (327, "Spinda", True, "Safari Ball", "HeartGold e SoulSilver"),
    (327, "Spinda", True, "Friend Ball", "HeartGold e SoulSilver, Sole e Luna"),
    (327, "Spinda", True, "Premier Ball", "qualunque gioco dalla terza alla settima generazione"),
    (489, "Phione", False, "Pregio Ball", "My Pokémon Ranch"),
    (494, "Victini", False, "Bis Ball", "Nero e Bianco"),
    (494, "Victini", False, "Poké Ball", "Nero e Bianco"),
    (494, "Victini", False, "Cura Ball", "Nero e Bianco"),
]

# I fiocchi che si perdono, con il nome della proprietà della libreria con cui si leggono in un esemplare di sesta o
# settima generazione. Dalla sesta generazione i fiocchi di gara di terza e quarta si fondono nel Ricordo delle Gare,
# e quelli delle Torri Lotta di terza e quarta nel Ricordo delle Lotte, che sono contatori.
PROPRIETA = {
    "Artist Ribbon": "RibbonArtist", "Legend Ribbon": "RibbonLegend", "National Ribbon": "RibbonNational",
    "Earth Ribbon": "RibbonEarth", "Kalos Champion Ribbon": "RibbonChampionKalos",
    "Hoenn Champion Ribbon": "RibbonChampionG6Hoenn", "Training Ribbon": "RibbonTraining",
    "Skillful Battler Ribbon": "RibbonBattlerSkillful", "Expert Battler Ribbon": "RibbonBattlerExpert",
    "Alola Champion Ribbon": "RibbonChampionAlola", "Battle Royal Master Ribbon": "RibbonBattleRoyale",
    "Battle Tree Great Ribbon": "RibbonBattleTreeGreat", "Battle Tree Master Ribbon": "RibbonBattleTreeMaster",
    "Contest Memory Ribbon": "RibbonCountMemoryContest", "Battle Memory Ribbon": "RibbonCountMemoryBattle",
    "Country Ribbon": "RibbonCountry", "World Ribbon": "RibbonWorld",
}
FUSI_GARA = "fuso nel Ricordo delle Gare"
FUSI_LOTTA = "fuso nel Ricordo delle Lotte"
DONO = {"RibbonClassic": "Classic", "RibbonWishing": "Wishing", "RibbonPremier": "Premier", "RibbonEvent": "Event",
        "RibbonBirthday": "Birthday", "RibbonSpecial": "Special", "RibbonChampionWorld": "World Champion",
        "RibbonSouvenir": "Souvenir", "RibbonChampionBattle": "Battle Champion",
        "RibbonChampionRegional": "Regional Champion", "RibbonChampionNational": "National Champion",
        "RibbonCountry": "Country", "RibbonWorld": "World", "RibbonEarth": "Earth", "RibbonNational": "National"}


def esemplari(n):
    return "1 esemplare" if n == 1 else "%d esemplari" % n


def template_fiocchi(wikitext):
    """Ogni modello {{ribbon|...}} della pagina, con categoria, nome, generazione d'origine e luoghi per generazione."""
    voci, i = [], 0
    while True:
        j = wikitext.find("{{ribbon|", i)
        if j < 0:
            return voci
        d, k = 0, j
        while k < len(wikitext):
            if wikitext.startswith("{{", k):
                d, k = d + 1, k + 2
                continue
            if wikitext.startswith("}}", k):
                d, k = d - 1, k + 2
                if d == 0:
                    break
                continue
            k += 1
        corpo, i = wikitext[j + 2:k - 2], k
        parti, d, cur, n = [], 0, "", 0
        while n < len(corpo):
            if corpo.startswith("{{", n) or corpo.startswith("[[", n):
                d, cur, n = d + 1, cur + corpo[n:n + 2], n + 2
                continue
            if corpo.startswith("}}", n) or corpo.startswith("]]", n):
                d, cur, n = d - 1, cur + corpo[n:n + 2], n + 2
                continue
            if corpo[n] == "|" and d == 0:
                parti.append(cur)
                cur = ""
            else:
                cur += corpo[n]
            n += 1
        parti.append(cur)
        nominali = [p for p in parti if not re.match(r"^\s*\w+\s*=", p)]
        luoghi = {}
        for p in parti:
            m = re.match(r"^(\d)l=(.*)$", p.strip(), re.S)
            if m:
                luoghi[int(m.group(1))] = m.group(2)
        voci.append({"categoria": nominali[1], "nome": nominali[2], "origine": nominali[5] if len(nominali) > 5 else "",
                     "luoghi": luoghi})


def generazioni_in_gioco(v):
    """Le generazioni in cui il fiocco si ottiene giocando, cioè quelle il cui luogo non è un esemplare evento."""
    return sorted(g for g, testo in v["luoghi"].items() if "Event Pokémon" not in testo and "event Pokémon distributions" not in testo
                  and "Tournament Pokémon" not in testo)


def misura_maestro():
    """La sezione della misura di `tools/pkhex-fiocco-maestro`, se il suo esito esiste."""
    p = os.path.join(LAVORO, "fiocco-maestro.json")
    if not os.path.exists(p):
        return []
    voci = json.load(open(p, encoding="utf-8"))["voci"]
    massimo = voci[0]["fiocchi"]
    migliori = [v for v in voci if v["fiocchi"] == massimo]
    esempio = next((v for v in migliori if v["specie"] == "Gardevoir"), migliori[0])
    conti = collections.Counter(v["fiocchi"] for v in voci)
    r = ["## Il massimo misurato con il verificatore dei fiocchi", "",
         "Il 2026-11-04, sull'elenco dei fiocchi di PokéOS letto dalle fotografie del proprietario (106 fiocchi e 53 emblemi), "
         "`tools/pkhex-fiocco-maestro` ha misurato quale esemplare legale ne raccoglie di più. Per ogni Pokémon Ombra e ogni sua "
         "evoluzione presente in Scarlatto e Violetto costruisce l'esemplare dall'incontro della libreria, lo purifica, lo porta "
         "fino alla nona generazione con il tracciatore di HOME, gli accende tutti i fiocchi e gli emblemi e spegne quelli che "
         "`RibbonVerifier` e la regola degli emblemi di `MarkVerifier` contestano. Combinazioni misurate: %d; per numero di voci "
         "tenute: %s." % (len(voci), ", ".join("%d con %d" % (n, k) for k, n in sorted(conti.items(), reverse=True))), "",
         "Il massimo è %d voci nel formato della nona generazione, raggiunto da %d combinazioni, tutte delle famiglie delle "
         "specie Ombra della tabella sopra. Chi ne ha una o due di meno manca da Spada e Scudo, che dà il fiocco Campione di "
         "Galar, o da Leggende Arceus, che dà il fiocco Hisui. Le %d voci contano come due i contatori del Ricordo delle Gare "
         "(40) e delle Lotte (8), che dalla sesta generazione riassumono 48 fiocchi distinti di terza e quarta: contati uno per "
         "uno sono %d fiocchi nella vita dell'esemplare, di cui 3 emblemi di Scarlatto e Violetto (Buongustaio, Cercaoggetti, "
         "Compagno). Gli altri emblemi si ottengono solo con la cattura in natura nei giochi per Switch, e i fiocchi dono solo "
         "con le distribuzioni: nessun esemplare li ha tutti, e la pagina di PokéOS li elenca insieme." %
         (massimo, len(migliori), massimo, massimo - 2 + 48), "",
         "L'esemplare proposto è %s, dall'Ombra %s di %s al livello %d: il livello basso permette il fiocco Vittoria della Torre "
         "Lotta di terza generazione, che la wiki di r/pokemonribbons ricorda di prendere con un esemplare al livello 50 o meno, "
         "e il fiocco Orma si prende in quarta generazione. Nei lotti di Bank entra con i fiocchi fino alla settima generazione; "
         "quelli di Switch li prende giocando dopo Bank (ADR-110). Le sue voci:" %
         (esempio["specie"], esempio["ombra"], esempio["origine"], esempio["livello_ombra"]), "",
         ", ".join("`%s`" % f for f in esempio["elenco"]) + ".", ""]
    return r


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scrivi", action="store_true")
    a = p.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    sfere = json.load(open(SFERE, encoding="utf-8"))
    fio = json.load(open(FIOCCHI, encoding="utf-8"))
    copie = [x for c in json.load(open(COPIE, encoding="utf-8"))["copie"] if c["gruppo"].startswith("HOME") for x in c["esemplari"]]
    bulba = json.load(open(BULBA, encoding="utf-8"))["parse"]
    voci_bulba = template_fiocchi(bulba["wikitext"])

    # Sfere: per ogni coppia persa, se una copia per HOME la porta già.
    nelle_copie = {(x["numero"], x["forma_n"], x["sfera"]) for x in copie}
    righe_sfere, coperte = [], 0
    for v in sfere["voci"]:
        for s in v["sfere_perse"]:
            c = (v["numero"], v["forma_n"], s) in nelle_copie
            coperte += c
            righe_sfere.append((v, s, c))
    righe_foglio = []
    for n, nome, crom, s, gioco in COPPIE_FOGLIO:
        c = any(x["numero"] == n and x["sfera"] == s and x["cromatico"] == crom for x in copie)
        righe_foglio.append((n, nome, crom, s, gioco, c))
    print("sfere: %d coppie perse dall'eredità, %d già nelle copie; %d coppie precise del foglio, %d già nelle copie" %
          (sfere["coppie_perse"], coperte, len(righe_foglio), sum(r[5] for r in righe_foglio)))

    # Fiocchi: quali si perdono, e quanti esemplari delle copie li portano già.
    portati = collections.Counter()
    for x in copie:
        for f in x["fiocchi"]:
            portati[f.split(":")[0]] += 1
    perdite, restano = [], []
    for v in voci_bulba:
        g = generazioni_in_gioco(v)
        if v["categoria"] == "gift" and v["nome"] not in ("National Ribbon", "Earth Ribbon"):
            continue
        nome = v["nome"]
        prop = PROPRIETA.get(nome)
        if v["categoria"] in ("cool", "beauty", "cute", "smart", "tough") and v["origine"] in ("III", "IV"):
            prop = FUSI_GARA
        if nome in ("Winning Ribbon", "Victory Ribbon") or (v["categoria"] == "tower" and v["origine"] == "IV"):
            prop = FUSI_LOTTA
        # Il fiocco Campione di terza generazione si ottiene ancora in Rosso Fuoco e Verde Foglia per Switch, che
        # mandano gli esemplari in HOME (tabella di connettività di HOME e libreria, versioni FRX e LGX).
        if nome == "Champion Ribbon":
            restano.append((nome, "Rosso Fuoco e Verde Foglia per Switch, collegati a HOME"))
            continue
        if g and max(g) <= 7:
            perdite.append((v, g, prop))
        elif g:
            restano.append((nome, "generazioni " + ", ".join(str(x) for x in g)))
    # Bulbapedia ripete il modello per le varianti d'oro dei due Ricordo; le gare di terza e quarta generazione hanno
    # nomi uguali (per esempio Cool Ribbon), quindi la chiave è nome più generazione d'origine.
    visti = set()
    perdite = [x for x in perdite if not ((x[0]["nome"], x[0]["origine"]) in visti or visti.add((x[0]["nome"], x[0]["origine"])))]
    print("fiocchi: %d che si ottengono giocando solo fino alla settima generazione, %d che restano ottenibili" % (len(perdite), len(restano)))
    maestri = [m for m in fio["maestri"] if not m["giochi_switch_assenti"]]
    print("Fiocco Maestro dalla purificazione: %d voci, da %d specie Ombra" % (len(maestri), len({m["ombra"] + m["origine"] for m in maestri})))

    if not a.scrivi:
        return 0
    r = ["# Le combinazioni di specie e Poké Ball che si perdono con la chiusura di Bank", "",
         "> Documento generato da `tools/fiocchi-e-sfere-prima-di-bank.py --scrivi`. Non si modifica a mano. Le coppie perse "
         "vengono dalla libreria PKHeX 26.10.18 attraverso `tools/pkhex-sfere-prima-di-bank`: una sfera è possibile prima di Bank "
         "se l'eredità della settima generazione la permette, e resta possibile dopo se la specie, o una sua pre-evoluzione, "
         "si trova in un gioco per Switch collegato a HOME che dà quella sfera in natura. Spinda non conta in Diamante Lucente e "
         "Perla Splendente, perché non si sposta fra HOME e quei giochi. Le specie non allevabili restano fuori dalla misura "
         "e le loro coppie stanno nella seconda tabella, presa dal foglio comunitario.", "",
         "Coppie perse dall'eredità: %d, su %d specie e forme; già portate dalle copie per HOME: %d. Coppie precise del foglio: %d; "
         "già nelle copie: %d." % (sfere["coppie_perse"], len(sfere["voci"]), coperte, len(righe_foglio), sum(x[5] for x in righe_foglio)), "",
         "Bulbapedia, pagine delle sfere lette il 2026-11-04, conferma che in Leggende Z-A si ottengono Dream Ball, Beast Ball, "
         "Safari Ball e le Ball Apricorn. Per questo Weedle, Pidgey, Kecleon, Furfrou, Pansage, Pansear, Panpour e le altre specie "
         "presenti in Z-A non compaiono qui, anche se l'elenco della comunità riportato dal foglio le cita: quell'elenco è "
         "anteriore a Z-A.", "",
         "## Coppie perse dall'eredità", "", "| Numero | Specie | Forma | Sfera | Giochi per Switch con la specie | Già nelle copie |", "|---|---|---|---|---|---|"]
    r += ["| %d | %s | %s | %s | %s | %s |" % (v["numero"], v["specie"], v["forma"] or "-", s,
                                           ", ".join(v["giochi_switch_con_la_specie"]) or "nessuno", "sì" if c else "no")
          for v, s, c in righe_sfere]
    r += ["", "## Coppie precise del foglio comunitario", "",
          "Dalla scheda «Unique Ball Matching» del foglio «Bank Closing all possible things checklist V0.5». Il foglio dichiara di "
          "ignorare la Cherish Ball quando è quella predefinita di un evento.", "",
          "| Numero | Specie | Cromatico | Sfera | Gioco d'origine | Già nelle copie |", "|---|---|---|---|---|---|"]
    r += ["| %d | %s | %s | %s | %s | %s |" % (n, nome, "sì" if crom else "no", s, g, "sì" if c else "no") for n, nome, crom, s, g, c in righe_foglio]
    r += ["", "Il foglio aggiunge due voci generali: un Fiocco Maestro di Colosseum o XD in una sfera che quei giochi danno, e un "
          "Pokémon Ombra in Premier Ball. Sono trattate in `FIOCCHI-PRIMA-DI-BANK.md`."]
    with open(DOC_SFERE, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(r) + "\n")

    r = ["# I fiocchi che si perdono con la chiusura di Bank, il Fiocco Maestro e il set minimo", "",
         "> Documento generato da `tools/fiocchi-e-sfere-prima-di-bank.py --scrivi`. Non si modifica a mano. L'elenco dei fiocchi "
         "e dei giochi viene da Bulbapedia, «List of Ribbons in the games», revisione %s, letta il 2026-11-04 attraverso l'API: "
         "un fiocco si perde se si ottiene giocando solo fino alla settima generazione. Le specie Ombra e i fiocchi dono vengono "
         "dalla libreria PKHeX 26.10.18 attraverso `tools/pkhex-fiocchi-prima-di-bank`; i fiocchi delle copie per HOME da "
         "`tools/pkhex-elenco-copie`." % bulba.get("revid"), "",
         "## I fiocchi che dopo Bank non si ottengono più giocando", "",
         "Le copie per HOME sono in giochi di sesta e settima generazione, dove i fiocchi di gara e di Torre Lotta di terza e "
         "quarta generazione sono già fusi nei due fiocchi Ricordo: per quelli la colonna rimanda al Ricordo.", "",
         "| Fiocco | Categoria | Generazione d'origine | Generazioni in cui si ottiene giocando | Esemplari delle copie che lo portano |", "|---|---|---|---|---|"]
    for v, g, prop in perdite:
        if prop in (FUSI_GARA, FUSI_LOTTA):
            n = prop
        elif prop:
            n = str(portati.get(prop, 0))
        else:
            n = "non letto"
        r.append("| %s | %s | %s | %s | %s |" % (v["nome"], v["categoria"], v["origine"], ", ".join(str(x) for x in g), n))
    r += ["", "Restano ottenibili dopo Bank: " + "; ".join("%s (%s)" % x for x in restano) + ".", "",
          "Il fiocco Nazionale e il fiocco Geo si ottengono solo in Colosseum e XD. La tabella di connettività di HOME non porta "
          "nessuna via da quei giochi se non attraverso Rubino, Zaffiro, Smeraldo, Rosso Fuoco e Verde Foglia su Game Boy Advance, "
          "quindi Bank. ribbons.guide li dà anche per XD su Switch, ma nessuna fonte letta porta XD su Switch verso HOME, e la "
          "libreria accetta un'origine di XD in HOME solo per un esemplare passato dalla via delle cartucce.", "",
          "## Il Fiocco Maestro che ne porta di più", "",
          "Un esemplare Ombra di Colosseum o di XD, purificato, porta il fiocco Nazionale e può prendere il fiocco Geo sul Monte "
          "Battaglia. Poi passa da tutti i giochi con fiocchi. I giochi per Switch accettano solo le specie del proprio Pokédex, "
          "quindi per arrivare al massimo la specie deve stare in Spada e Scudo, in Diamante Lucente e Perla Splendente, in "
          "Leggende Arceus e in Scarlatto e Violetto. Le specie Ombra che soddisfano la condizione, da sole o con un'evoluzione, sono:", "",
          "| Specie Ombra | Gioco | Specie che arrivano in tutti e quattro i giochi per Switch |", "|---|---|---|"]
    per_ombra = collections.OrderedDict()
    for m in maestri:
        per_ombra.setdefault((m["ombra"], m["origine"]), []).append(m["specie"])
    r += ["| %s | %s | %s |" % (o, g, ", ".join(s)) for (o, g), s in per_ombra.items()]
    r += ["", "Le specie Ombra sono %d: %d di XD e %d di Colosseum. Il manuale di Athis, letto il 2026-11-04, ne conta 13 di XD e 5 "
          "di Colosseum, e il foglio comunitario dà lo stesso elenco: le tre fonti coincidono." %
          (len(per_ombra), sum(1 for o, g in per_ombra if g == "XD"), sum(1 for o, g in per_ombra if g != "XD")), "",
          "Un solo esemplare di questo elenco può portare tutti i fiocchi della tabella precedente, perché ogni specie qui sta "
          "in tutti i giochi dalla terza alla settima generazione. Gli emblemi di ottava e nona generazione no, perché dipendono "
          "dalla cattura in quei giochi. Nessun esemplare porta anche i fiocchi dono, perché quelli arrivano solo con la "
          "distribuzione, e un esemplare di una distribuzione non è un Ombra.", ""]
    r += misura_maestro()
    r += ["## Il set minimo per avere tutti i fiocchi", "",
          "Il set minimo è fatto di un esemplare di tipo Fiocco Maestro dell'elenco sopra, che copre tutti i fiocchi che si "
          "ottengono giocando, e di carte evento che coprono i fiocchi dono. La base dei doni segreti della libreria, dalla quarta "
          "alla nona generazione, ha queste carte per fiocco: " +
          "; ".join("%s %d" % (DONO[k], v) for k, v in fio["carte_per_fiocco"].items()) + ".", "",
          "Una copertura golosa con %d carte:" % len(fio["copertura_dono"]), "",
          "| Generazione | Carta | Titolo | Specie | Fiocchi |", "|---|---|---|---|---|"]
    r += ["| %d | %d | %s | %s | %s |" % (c["generazione"], c["carta"], c["titolo"].replace("|", "/") or "-", c["specie"],
                                       ", ".join(DONO[x] for x in c["fiocchi_tutti"])) for c in fio["copertura_dono"]]
    gia = [DONO[k] for k in fio["carte_per_fiocco"] if fio["carte_per_fiocco"][k] and portati.get(k, 0)]
    mancano = [DONO[k] for k in fio["carte_per_fiocco"] if fio["carte_per_fiocco"][k] and not portati.get(k, 0)]
    fuori = [DONO[k] for k in fio["carte_per_fiocco"] if not fio["carte_per_fiocco"][k]]
    r += ["", "Le copie per HOME portano già: " + ", ".join("%s (%s)" % (d, esemplari(portati[[k for k in DONO if DONO[k] == d][0]])) for d in gia) +
          ". Fiocchi dono che la base delle carte ha e le copie no: " + (", ".join(mancano) or "nessuno") + ".", "",
          "Fuori dalla base delle carte: " + ", ".join(fuori) + ". National ed Earth si ottengono giocando, in Colosseum e XD. "
          "Country e World sono fiocchi di distribuzioni di terza e quarta generazione fuori dalla base delle carte: Country da "
          "Pokémon Festa 2004, 2005 e 2007; le copie per HOME portano Country in %d esemplari e World in %d. Regional Champion e National Champion non hanno luoghi su Bulbapedia; la loro "
          "distribuzione resta da verificare." % (portati.get("RibbonCountry", 0), portati.get("RibbonWorld", 0))]
    with open(DOC_FIOCCHI, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(r) + "\n")
    print("Scritti " + os.path.relpath(DOC_SFERE, RADICE) + " e " + os.path.relpath(DOC_FIOCCHI, RADICE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
