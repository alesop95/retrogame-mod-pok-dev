#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le schede delle voci speciali: da dove viene ciascun esemplare, perche' e' esclusivo, a che punto e'.

Perche' esiste. Il proprietario ha chiesto il 2026-09-25 che ogni esemplare esclusivo sia descritto come gia'
lo sono quelli da evento: da dove viene, perche' non lo si ottiene in un altro modo, e che cosa il progetto ne
ha fatto. La checklist dice quali voci esistono e la loro resa, ma non le racconta; questo programma le
racconta, e lo fa da dati e non da memoria, cosi' che una scheda cambi quando cambiano i dati.

Che cosa legge. La lista degli eventi e la resa di ciascuno da `tools/checklist-pokedex.py`, chiamato come
modulo. Le posizioni del Pokewalker dalla pagina di Bulbapedia salvata in `_notes/fonti/consegne/`, che e'
una copia d'archivio e va dichiarata come tale. I giudizi e le descrizioni degli esemplari prodotti da
`recreate-pokemon-distributions-events/giudizi-pkhex-core.json`, scritto da `tools/pkhex-giudica`. I campi
delle carte dei doni da `_notes/lotti/lotto-doni-gen67/carte-descritte.json`, scritto da
`tools/pkhex-dono --descrivi`. La provenienza del Phanpy da `provenienze-eventi-gb.json`.

Che cosa non fa. Non inventa provenienze: dove una classe non ha ancora una fonte letta voce per voce, la
scheda lo dice. Le frasi sul perche' una classe sia esclusiva sono autorate qui sotto e poggiano sulle fonti
citate accanto a ciascuna.

Uso
---
    python tools/schede-esclusivi.py --pkhex <clone> --ace <clone>
    python tools/schede-esclusivi.py --pkhex <clone> --ace <clone> --check
"""
import argparse
import html.parser
import importlib.util
import io
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USCITA = os.path.join(RADICE, "pokedex-home-completo", "SCHEDE-ESCLUSIVI.md")
BULBA_WALKER = os.path.join(RADICE, "_notes", "fonti", "consegne",
                            "2026-09-25-bulbapedia-pokewalker-wayback-20260822000650.html")
BULBA_URL = ("https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_found_through_the_Pok%C3%A9walker, "
             "copia della Wayback Machine del 2026-08-22")
GIUDIZI = os.path.join(RADICE, "recreate-pokemon-distributions-events", "giudizi-pkhex-core.json")
CARTE = os.path.join(RADICE, "_notes", "lotti", "lotto-doni-gen67", "carte-descritte.json")
PROVENIENZE_GB = os.path.join(RADICE, "recreate-pokemon-distributions-events", "provenienze-eventi-gb.json")

# I ventisette corsi nell'ordine dell'indice del file del verificatore, con il nome inglese che Bulbapedia
# usa nella colonna dell'area. L'ordine italiano e' quello di CORSI_POKEWALKER in
# tools/censimento-eventi-tabelle.py; il programma controlla che ogni nome inglese compaia nella pagina, e se
# uno manca lo dice invece di abbinare male.
CORSI_EN = (
    "Refreshing Field", "Noisy Forest", "Rugged Road", "Beautiful Beach", "Suburban Area", "Dim Cave",
    "Blue Lake", "Town Outskirts", "Hoenn Field", "Warm Beach", "Volcano Path", "Treehouse", "Scary Cave",
    "Sinnoh Field", "Icy Mountain Rd.", "Big Forest", "White Lake", "Stormy Beach", "Resort", "Quiet Cave",
    "Beyond the Sea", "Night Sky's Edge", "Yellow Forest", "Rally", "Sightseeing", "Winner's Path",
    "Amity Meadow",
)

PERCHE = {
    "pokewalker": (
        "Il Pokewalker è il contapassi venduto con HeartGold e SoulSilver. Un esemplare catturato camminando con "
        "l'apparecchio porta il Pokewalker come luogo d'incontro, e questo nessun'altra via del gioco lo "
        "riproduce. I ventidue corsi in dotazione si sbloccano accumulando watt, e ogni possessore dell'apparecchio "
        "poteva raggiungerli. I cinque corsi dal ventitreesimo in poi furono invece distribuiti come eventi e non "
        "sono più ottenibili: sono le voci che la checklist conta sotto scadenza con il peso di un evento. Per "
        "molte specie il Pokewalker dà anche un livello o una mossa che l'incontro selvatico non dà, e la colonna "
        "delle mosse, quando c'è, lo dice."),
    "ranch": (
        "My Pokemon Ranch è un gioco per Wii collegato a Diamante, Perla e Platino. Dal fattore del Ranch si "
        "ricevevano esemplari fissati dal gioco, con allenatore e identificativo propri, in cambio di esemplari "
        "depositati. Il servizio del gioco è chiuso, e questi esemplari non si ottengono più per la via "
        "originale. Le schede di questa classe non hanno ancora un dettaglio voce per voce da una fonte letta: la "
        "fonte da leggere è la pagina di Bulbapedia sul gioco, con la stessa via d'archivio usata per il "
        "Pokewalker."),
    "radar": (
        "Il Dream Radar è un'applicazione per Nintendo 3DS collegata a Nero 2 e Bianco 2. Gli esemplari arrivano "
        "nel gioco con l'abilità nascosta e nella Dream Ball, e il livello dipende da quando li si riceve. È una "
        "periferica e non un dono: la voce conta come esemplare di quella provenienza. Anche qui il dettaglio voce "
        "per voce aspetta la lettura della pagina di Bulbapedia sull'applicazione."),
    "dono": (
        "Un dono segreto di sesta o settima generazione esiste solo attraverso la carta con cui fu distribuito. La "
        "carta fissa allenatore, identificativo, mosse, sfera, strumento e nastri, e quelle combinazioni non si "
        "ottengono giocando. Le carte non sono più distribuite, e per il deposito questi esemplari passano "
        "soltanto dalla banca, quindi scadono il 26 febbraio 2027. I campi qui sotto sono quelli della carta "
        "come la libreria del verificatore la legge. La data della carta non compare, perché la libreria non la "
        "conserva e riporta al suo posto la data di oggi."),
    "scambio": (
        "Uno scambio in gioco è un esemplare che un personaggio del gioco consegna una sola volta per "
        "salvataggio, con soprannome, allenatore e identificativo fissati dal gioco. Nessun'altra via produce "
        "quella combinazione, e per questo il collezionista lo conta come un esemplare a sé. Il soprannome "
        "dipende dalla lingua del gioco, e qui è quello italiano."),
}


def carica_modulo(nome, percorso):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class Tabelle(html.parser.HTMLParser):
    """Le righe delle tabelle di una pagina, come elenchi di celle di solo testo."""

    def __init__(self):
        super().__init__()
        self.righe, self.riga, self.cella = [], None, None

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.riga = []
        elif tag in ("td", "th") and self.riga is not None:
            self.cella = []

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.cella is not None and self.riga is not None:
            self.riga.append(" ".join("".join(self.cella).split()))
            self.cella = None
        elif tag == "tr" and self.riga is not None:
            self.righe.append(self.riga)
            self.riga = None

    def handle_data(self, dati):
        if self.cella is not None:
            self.cella.append(dati)


def posizioni_pokewalker():
    """Le righe della pagina di Bulbapedia, per numero di Pokedex, area e livello."""
    if not os.path.exists(BULBA_WALKER):
        return None, []
    p = Tabelle()
    with io.open(BULBA_WALKER, encoding="utf-8") as f:
        p.feed(f.read())
    righe = [r for r in p.righe if len(r) >= 11 and r[0].isdigit()]
    aree = {r[5] for r in righe}
    mancanti = [c for c in CORSI_EN if c not in aree]
    indice = {}
    for r in righe:
        chiave = (int(r[0]), r[5], r[7])
        indice.setdefault(chiave, []).append({
            "sesso": r[3], "gruppo": r[4], "area": r[5], "sblocco": r[6], "livello": r[7],
            "passi": r[8], "rarita": r[9], "strumento": r[10]})
    return indice, mancanti


def stato_leggibile(resa, primo):
    testo = {"prodotta e conforme": "prodotta e giudicata conforme dalla libreria del verificatore",
             "producibile e verificata": "producibile e verificata",
             "censita, non ancora producibile": "censita, non ancora prodotta",
             "letta, non ancora producibile": "letta, non ancora prodotta"}.get(resa, resa)
    return testo + ("; è la voce scelta per la sua specie nel primo tempo" if primo else "")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pkhex", required=True)
    ap.add_argument("--ace", required=True)
    ap.add_argument("--check", action="store_true", help="non scrive: esce con 1 se il documento cambierebbe")
    a = ap.parse_args(argv)

    lista = carica_modulo("checklist", os.path.join(RADICE, "tools", "checklist-pokedex.py"))
    eventi = lista.voci_da_evento(a.pkhex, a.ace)
    lista.riconcilia_con_i_lotti(eventi)
    lista.ordina_per_specie(eventi)
    nomi = lista.nomi_specie(a.pkhex)
    giudizi = {}
    if os.path.exists(GIUDIZI):
        with io.open(GIUDIZI, encoding="utf-8") as f:
            giudizi = json.load(f)["voci"]
    carte = {}
    if os.path.exists(CARTE):
        with io.open(CARTE, encoding="utf-8") as f:
            carte = json.load(f)
    walker, corsi_mancanti = posizioni_pokewalker()

    r = ["# Schede delle voci speciali", "",
         "> Documento generato da `tools/schede-esclusivi.py`. Non si modifica a mano: si rigenera. "
         "Racconta, per ogni voce speciale del Pokedex completo, da dove viene l'esemplare, perché è "
         "esclusivo e a che punto è il progetto. Le voci da evento di prima, seconda, terza, quarta e quinta "
         "generazione hanno già le loro schede in `recreate-pokemon-distributions-events/`, e questo "
         "documento copre le classi che non ne avevano.", ""]

    # ------------------------------------------------------------------ periferiche
    per = [e for e in eventi if e.get("classe") == "periferica"]
    walk = [e for e in per if e["descrizione"].startswith("Pokewalker")]
    ranch = [e for e in per if e["descrizione"].startswith("My Pokemon Ranch")]
    radar = [e for e in per if e["descrizione"].startswith("Dream Radar")]

    r += ["## Il Pokewalker", "", PERCHE["pokewalker"], ""]
    if walker is None:
        r += ["La pagina di Bulbapedia non è sul disco, quindi le schede portano i soli dati del verificatore.", ""]
    else:
        r += ["Le posizioni vengono da %s. È una copia d'archivio e non la pagina viva, che risponde con una "
              "verifica anti-bot, e va citata come tale. %s" % (
                  BULBA_URL, "Tutti i ventisette corsi della tabella del verificatore compaiono nella pagina."
                  if not corsi_mancanti else "Non compaiono nella pagina i corsi: %s." % ", ".join(corsi_mancanti)), ""]
    italiani = carica_modulo("censtab", os.path.join(RADICE, "tools", "censimento-eventi-tabelle.py")).CORSI_POKEWALKER
    for e in walk:
        # "Pokewalker: corso <nome>, livello <n>, corso in dotazione|distribuito"
        parti = e["descrizione"].split(":", 1)[1].split(",")
        corso_it = parti[0].replace("corso", "", 1).strip()
        livello = parti[1].replace("livello", "").strip()
        corso_en = CORSI_EN[italiani.index(corso_it)] if corso_it in italiani else "?"
        distribuito = "distribuito" in e["descrizione"]
        r.append("### `%s` %s, corso %s" % (e["codice"], nomi.get(e["nazionale"], "?"), corso_it))
        r.append("")
        dove = "Pokewalker, corso %s (%s nella versione inglese), livello %s, %s." % (
            corso_it, corso_en, livello, "corso distribuito come evento" if distribuito else "corso in dotazione")
        trovate = (walker or {}).get((e["nazionale"], corso_en, livello), [])
        if trovate:
            dove += " " + " ".join(
                "Nella pagina: gruppo %s, sesso %s, si sblocca con %s, dopo %s, rarità %s, strumento %s." % (
                    t["gruppo"], t["sesso"], t["sblocco"], t["passi"], t["rarita"].lower(), t["strumento"])
                for t in trovate)
        elif walker is not None:
            dove += " La pagina non ha una riga con la stessa specie, lo stesso corso e lo stesso livello."
        r.append("**Da dove viene.** " + dove)
        r.append("")
        r.append("**Perché è esclusivo.** " + (
            "Il corso fu distribuito e non è più ottenibile, quindi questa voce ha il peso di un evento."
            if distribuito else
            "Il luogo d'incontro Pokewalker non si ottiene per altra via; il corso era raggiungibile da ogni "
            "possessore dell'apparecchio."))
        r.append("")
        r.append("**Stato.** " + stato_leggibile(e["resa"], e.get("primo_della_specie")) + ".")
        r.append("")

    for titolo, chiave, gruppo in (("My Pokemon Ranch", "ranch", ranch), ("Il Dream Radar", "radar", radar)):
        r += ["## " + titolo, "", PERCHE[chiave], ""]
        for e in gruppo:
            r.append("### `%s` %s" % (e["codice"], nomi.get(e["nazionale"], "?")))
            r.append("")
            r.append("**Da dove viene.** %s, generazione %d, secondo le tabelle del verificatore." % (
                e["descrizione"], e["generazione"]))
            r.append("")
            r.append("**Stato.** " + stato_leggibile(e["resa"], e.get("primo_della_specie")) + ".")
            r.append("")

    # ------------------------------------------------------------------ doni di sesta e settima
    r += ["## I doni segreti di sesta e settima generazione del primo tempo", "", PERCHE["dono"], ""]
    for codice in sorted(carte):
        c = carte[codice]
        e = next((x for x in eventi if x["codice"] == codice), {})
        g = next((v for k, v in giudizi.items() if k.startswith("lotto-doni-gen67/%s-" % codice)), None)
        r.append("### `%s` %s, carta %s" % (codice, c.get("nome_specie", "?"), c.get("CardID", "?")))
        r.append("")
        dettagli = ["titolo della carta «%s»" % c.get("CardTitle", "")]
        if c.get("OriginalTrainerName"):
            dettagli.append("allenatore della carta %s, identificativo %s" % (c["OriginalTrainerName"], c.get("TID16")))
        else:
            dettagli.append("allenatore di chi la riceve")
        dettagli.append("livello %s" % c.get("Level"))
        if c.get("IsEgg") == "True":
            dettagli.append("consegnato come uovo")
        if c.get("mosse"):
            dettagli.append("mosse " + ", ".join(c["mosse"]))
        if c.get("RestrictLanguage") not in (None, "0"):
            dettagli.append("riservata alla lingua con codice %s" % c["RestrictLanguage"])
        r.append("**Da dove viene.** Carta del dono segreto numero %s della generazione %s: %s." % (
            c.get("CardID"), codice.split("-")[1], "; ".join(dettagli)))
        r.append("")
        if g:
            d = g.get("descrizione", {})
            r.append("**L'esemplare prodotto.** %s, livello %s, allenatore %s, %s, luogo %s%s, sfera %s. Giudizio della "
                     "libreria: %s." % (d.get("specie_it"), d.get("livello"), d.get("allenatore"), d.get("lingua"),
                                        d.get("luogo"), (", uovo da %s" % d["luogo_uovo"]) if d.get("luogo_uovo") else "",
                                        d.get("sfera"), g.get("esito")))
            r.append("")
        r.append("**Stato.** " + stato_leggibile(e.get("resa", "?"), e.get("primo_della_specie")) + ".")
        r.append("")

    # ------------------------------------------------------------------ scambi
    r += ["## Gli scambi in gioco di quarta e quinta generazione", "", PERCHE["scambio"], ""]
    for chiave in sorted(k for k in giudizi if k.startswith(("lotto-scambi-gen4/", "lotto-scambi-gen5/"))):
        g = giudizi[chiave]
        d = g.get("descrizione", {})
        r.append("### `%s` %s «%s»" % (chiave.split("/")[1].rsplit(".", 1)[0], d.get("specie_it"), d.get("soprannome")))
        r.append("")
        r.append("**Da dove viene.** Scambio in gioco in %s, al luogo %s: il personaggio %s, identificativo %s, "
                 "consegna %s di livello %s con il soprannome «%s», sfera %s, mosse %s." % (
                     d.get("gioco_di_origine"), d.get("luogo"), d.get("allenatore"), d.get("id_allenatore"),
                     d.get("specie_it"), d.get("livello"), d.get("soprannome"), d.get("sfera"),
                     ", ".join(d.get("mosse", []))))
        r.append("")
        r.append("**Stato.** Rigenerato il 2026-09-25 con la libreria, giudizio: %s." % g.get("esito"))
        r.append("")

    # ------------------------------------------------------------------ il Phanpy
    prov = {}
    if os.path.exists(PROVENIENZE_GB):
        with io.open(PROVENIENZE_GB, encoding="utf-8") as f:
            prov = json.load(f).get("voci", {}).get("EVT-2-0146", {})
    g = giudizi.get("lotto-gb/EVT-2-0146-Phanpy.pk2", {})
    r += ["## Il Phanpy di seconda generazione `EVT-2-0146`", "",
          "**Da dove viene.** Uovo da evento di Oro, Argento e Cristallo, %s, riconoscibile dalla mossa %s. "
          "Nella tabella degli eventi del verificatore è la voce 146, con il vincolo di lingua giapponese e "
          "l'allenatore di chi lo riceve." % (prov.get("campagna", "campagna non registrata"),
                                              prov.get("marcatore", "?")), "",
          "**Perché è esclusivo.** La mossa Ripeti su un Phanpy di livello 5 non si ottiene in altro modo in "
          "seconda generazione: è la firma della distribuzione.", "",
          "**Stato.** Il lotto del 2026-09-04 lo aveva prodotto in inglese, e la libreria contestava la mossa, "
          "perché su un esemplare non giapponese quell'evento non esiste. Il 2026-09-25 è stato rigenerato in "
          "giapponese dalla voce 146, con allenatore アレシオ e identificativo 42317; giudizio: %s. La versione "
          "inglese è conservata in `_notes/archivio/lotto-gb-phanpy-inglese-2026-09-04/`. Un esemplare "
          "giapponese si scrive soltanto su una cartuccia giapponese di Oro, Argento o Cristallo." % g.get("esito", "?"), ""]

    testo = "\n".join(r) + "\n"
    if a.check:
        attuale = io.open(USCITA, encoding="utf-8").read() if os.path.exists(USCITA) else ""
        print("allineato" if attuale == testo else "disallineato: %s va rigenerato" % USCITA)
        return 0 if attuale == testo else 1
    with io.open(USCITA, "w", encoding="utf-8", newline="\n") as f:
        f.write(testo)
    print("scritto %s: %d Pokewalker, %d Ranch, %d Dream Radar, %d doni, %d scambi, 1 Phanpy" % (
        USCITA, len(walk), len(ranch), len(radar), len(carte),
        sum(1 for k in giudizi if k.startswith(("lotto-scambi-gen4/", "lotto-scambi-gen5/")))))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
