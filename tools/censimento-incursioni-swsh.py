#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scrive il censimento delle incursioni di evento di Spada e Scudo dal dump di pkhex-incursioni-swsh.

Perché esiste
-------------
ADR-097 (2026-10-06) fa entrare nella collezione gli esemplari delle incursioni di evento di Spada e
Scudo, cioè le tane di distribuzione delle Wild Area News, cromatici e Gigantamax compresi. Il lavoro
sulla libreria lo fa `tools/pkhex-incursioni-swsh`, che scrive un dump di oltre un megabyte in
`_notes/incursioni-swsh.json` e il lotto dei mancanti con il suo `rapporto.json`. Nessuno dei due è
tracciato né leggibile in sequenza: questo strumento ne ricava un documento tracciato,
`pokedex-home-completo/CENSIMENTO-INCURSIONI-SWSH.md`, con i conteggi e il loro perimetro, la
copertura per chiave di collezione, il confronto con la pagina della Wild Area News del 2021 e lo
stato di ogni esemplare generato nel registro dei giudizi.

Che cosa legge
--------------
Il dump, il rapporto del lotto e il registro unico
`recreate-pokemon-distributions-events/giudizi-pkhex-core.json`. Un esemplare generato si dichiara
conforme soltanto se il registro porta una voce con lo stesso percorso, la stessa impronta SHA-256 e
l'esito conforme: il rapporto del generatore dice che cosa è stato scritto, il registro dice che
cosa è stato giudicato, e la riga del documento li tiene insieme.

Il campo che varia fra una corsa e l'altra
------------------------------------------
Il generatore prova ogni riga generando un esemplare da un seme casuale, e il riconoscimento come
tana di distribuzione dipende dal seme: due corse danno numeri che differiscono di qualche unità.
Il documento riporta quelli del dump che trova; `--check` confronta con quel dump, non con la
libreria.

Uso
---
    python tools/censimento-incursioni-swsh.py
    python tools/censimento-incursioni-swsh.py --check
"""

import argparse
import io
import json
import os
import sys

DUMP = os.path.join("_notes", "incursioni-swsh.json")
LOTTO = os.path.join("_notes", "lotti", "lotto-incursioni-evento-swsh")
REGISTRO = os.path.join("recreate-pokemon-distributions-events", "giudizi-pkhex-core.json")
USCITA = os.path.join("pokedex-home-completo", "CENSIMENTO-INCURSIONI-SWSH.md")
SCELTA = "lotto-eventi-switch-scelta"


def leggi(percorso):
    with io.open(percorso, encoding="utf-8") as f:
        return json.load(f)


def cella(testo):
    """Una cella di tabella su una riga sola, senza barre verticali che la spezzino."""
    return str(testo).replace("|", "/").replace("\n", " ") if testo not in (None, "") else "-"


def nome_forma(k):
    if k["forma"] == 0 and k["nome_forma"] in ("", "Normale", "Stato Normale"):
        return "-"
    return k["nome_forma"] or str(k["forma"])


def componi(dump, rapporto, registro):
    c = dump["conteggi"]
    voci_reg = registro["voci"]
    generati = {x["chiave"]: x for x in rapporto["esemplari"]}
    conformi_reg = {}
    for x in rapporto["esemplari"]:
        if not x.get("conforme"):
            continue
        v = voci_reg.get(x["file"])
        conformi_reg[x["chiave"]] = bool(v and v.get("sha256") == x["sha256"] and v.get("esito") == "conforme")
    n_conformi = sum(conformi_reg.values())
    non_generati = [x for x in rapporto["esemplari"] if not x.get("conforme")]
    chiavi = dump["chiavi"]
    solo_completo = [k for k in chiavi if k["coperta_da"] and SCELTA not in k["coperta_da"]]
    scoperte = [k for k in chiavi if not k["coperta_da"]]
    gen_s = [x for x in generati.values() if x["chiave"].endswith("-S")]
    gen_s_cromatici = sum(1 for x in gen_s if x.get("cromatico"))
    gen_altri_cromatici = sum(1 for x in generati.values() if not x["chiave"].endswith("-S") and x.get("cromatico"))
    gen_indistinti = [x for x in generati.values() if x.get("conforme") and not x.get("riconosciuto_come_distribuzione")]

    r = []
    a = r.append
    a("# Censimento delle incursioni di evento di Spada e Scudo")
    a("")
    a("> Documento generato da `tools/censimento-incursioni-swsh.py` dal dump di `tools/pkhex-incursioni-swsh` (`_notes/incursioni-swsh.json`), dal rapporto del lotto `_notes/lotti/lotto-incursioni-evento-swsh/` e dal registro `recreate-pokemon-distributions-events/giudizi-pkhex-core.json`. Non si modifica a mano: si rigenera. Per ADR-097 gli esemplari delle tane di distribuzione delle Wild Area News, cromatici e Gigantamax compresi, contano come esemplari da distribuzione; non scadono con la banca, perché Spada e Scudo parlano con HOME direttamente, e si portano in gioco per la via di `STRATEGIA-SWITCH.md`.")
    a("")
    a("## Che cosa si conta")
    a("")
    a("La fonte sono le tabelle interne `Dist_SW` e `Dist_SH` di `Encounters8Nest` nella libreria PKHeX.Core compilata dal clone in `_notes/fonti/cloni/pkhex`, classe `EncounterStatic8ND`, lette per riflessione. Una riga è un incontro distinto, cioè indice dell'evento, specie, forma, livello, livello Dynamax, fattore Gigantamax, stato del cromatico, abilità, IV perfetti e mosse; una chiave di collezione è specie, forma, Gigantamax (`G`) e cromatico garantito (`S`), ed è l'unità con cui la collezione conta questi esemplari.")
    a("")
    a("Righe di tabella: %d in Spada e %d in Scudo; righe distinte %d, di cui %d solo in Spada e %d solo in Scudo, su %d indici di evento. Chiavi di collezione: %d, che si riducono a %d contando solo specie, forma e Gigantamax e a %d contando solo specie e forma; %d portano il fattore Gigantamax e %d il cromatico garantito." % (
        c["righe_spada"], c["righe_scudo"], c["righe_distinte"], c["righe_solo_spada"], c["righe_solo_scudo"], c["indici_evento"],
        c["chiavi"], c["chiavi_specie_forma_gigantamax"], c["chiavi_specie_forma"], c["chiavi_gigantamax"], c["chiavi_cromatico_garantito"]))
    a("")
    # Dal 2026-10-06 il confronto conta anche la famiglia evolutiva per le chiavi senza fattore: prima Bulbasaur e Squirtle
    # risultavano solo da incursioni di evento, mentre il dono del Dojo ha il fattore e Venusaur e Blastoise stanno nelle
    # tane ordinarie. La logica è in tools/pkhex-incursioni-swsh, funzione Disponibilità; qui si riporta il conteggio.
    if "chiavi_anche_per_allevamento_o_evoluzione" in c:
        a("Fuori dagli eventi, letto dalle altre tabelle di `Encounters8` e `Encounters8Nest` per specie, forma e Gigantamax: %d chiavi esistono anche nelle tane ordinarie, %d soltanto in altri incontri (statici, grotte di cristallo, avventure Dynamax, selvatici, scambi), %d si ottengono per allevamento o evoluzione da un altro incontro, %d soltanto nelle incursioni di evento. Per una chiave senza fattore Gigantamax il confronto guarda anche la stessa specie con il fattore, perché il fattore non si eredita e la Zuppa Dynamax lo toglie, e gli altri membri della famiglia evolutiva nella stessa forma: le pre-evoluzioni, che si fanno evolvere, e le evoluzioni di una specie che si alleva, da cui nasce un uovo. Per una chiave con il fattore il confronto resta sulla sola terna, perché il fattore non viene da un uovo. Il confronto ignora il cromatico garantito, perché nessuna tana ordinaria lo garantisce." % (
            c["chiavi_anche_tane_ordinarie"], c["chiavi_anche_altri_incontri"], c["chiavi_anche_per_allevamento_o_evoluzione"], c["chiavi_solo_da_eventi"]))
    else:
        a("Fuori dagli eventi, letto dalle altre tabelle di `Encounters8` e `Encounters8Nest` per specie, forma e Gigantamax: %d chiavi esistono anche nelle tane ordinarie, %d soltanto in altri incontri (statici, grotte di cristallo, avventure Dynamax, selvatici), %d soltanto nelle incursioni di evento. Il confronto ignora il cromatico garantito, perché nessuna tana ordinaria lo garantisce." % (
            c["chiavi_anche_tane_ordinarie"], c["chiavi_anche_altri_incontri"], c["chiavi_solo_da_eventi"]))
    a("")
    a("Prova di ogni riga: il generatore costruisce un esemplare da ciascuna con l'allenatore del progetto e lo giudica con `LegalityAnalysis`. Righe legali %d su %d; righe che la libreria riconosce come tana di distribuzione, e non come tana ordinaria o come un'altra riga con un diverso stato del cromatico, %d; chiavi con almeno una riga riconosciuta %d. Il riconoscimento dipende dal seme casuale e varia di qualche unità fra una corsa e l'altra." % (
        c["righe_legali"], c["righe_distinte"], c["righe_riconosciute_come_distribuzione"], c["chiavi_distinguibili"]))
    a("")
    a("## Il cromatico garantito, e il suo opposto")
    a("")
    a("Nelle tane la lucentezza viene dal seme: la libreria non forza il cromatico su una riga che lo garantisce, e un esemplare non cromatico nato da quella riga non vi si accorda. Il generatore chiede quindi il cromatico sulle righe che lo garantiscono e il non cromatico su tutte le altre, sia su quelle con il blocco, dove la libreria lo impone da sé, sia su quelle libere, dove un seme cromatico capita una volta su 4096 e darebbe all'esemplare la chiave sbagliata. Dopo la generazione lo stato ottenuto si confronta con quello atteso e un esemplare che non vi corrisponde non si scrive. Esito su questo lotto: %d chiavi a cromatico garantito generate, %d cromatiche; %d esemplari cromatici fra le %d chiavi senza garanzia." % (
        len(gen_s), gen_s_cromatici, gen_altri_cromatici, len(generati) - len(gen_s)))
    a("")
    a("Un limite della libreria va detto perché tocca proprio questi esemplari. Per un esemplare cromatico di tana la libreria non verifica la correlazione con il seme, e attribuisce l'esemplare al primo incontro compatibile che trova, spesso una tana ordinaria con la stessa specie: l'esemplare è conforme, ma il verificatore non sa dire che venga da un evento. Fra i generati sono %d, elencati nella tabella delle chiavi con l'incontro che la libreria riconosce." % len(gen_indistinti))
    a("")
    a("## Copertura e generazione")
    a("")
    a("I lotti esistenti si leggono tutti, `.pk8` per `.pk8` (%d file letti, escluse le uscite di questo strumento, la cui cartella comincia con `lotto-incursioni-`); un file copre la chiave dell'esemplare quando la libreria lo riconosce come tana di distribuzione, oppure quando è nato da una tana di distribuzione e la libreria lo attribuisce a una tana ordinaria (%d file in questo caso). Chiavi coperte da `%s`, il lotto destinato a HOME: %d. Chiavi coperte da qualunque lotto: %d. Chiavi coperte soltanto da `lotto-eventi-switch-completo`: %d. Chiavi non coperte da alcun lotto: %d, %s." % (
        c["pk8_letti_nei_lotti"], c["file_static8nd_attribuiti_a_tana_ordinaria"], SCELTA, c["chiavi_coperte_da_scelta"],
        c["chiavi_coperte_da_qualunque_lotto"], len(solo_completo), len(scoperte),
        "tutte a cromatico garantito, perché `pkhex-eventi-switch` generava senza chiedere il cromatico" if scoperte and all(k["cromatico_garantito"] for k in scoperte)
        else "di cui %d a cromatico garantito" % sum(1 for k in scoperte if k["cromatico_garantito"])))
    a("")
    a("Il generatore produce un esemplare per ogni chiave che il lotto destinato a HOME non copre, con l'allenatore del progetto per i soli campi che l'evento lasciava a chi riceveva, preferendo la riga riconosciuta come distribuzione, poi quella presente in entrambe le versioni, poi Spada, poi il livello più alto. Generati %d, non generabili %d; conformi nel registro dei giudizi, con la stessa impronta e giudicati con un salvataggio vuoto della versione del file, %d su %d." % (
        c["generati"], c["non_generati"], n_conformi, len(conformi_reg)))
    if non_generati:
        a("")
        a("Non generabili:")
        a("")
        for x in non_generati:
            a("- `%s` %s: %s" % (x["chiave"], x["specie"], x.get("motivo", "")))
    a("")
    a("## Il confronto con la Wild Area News del 2021")
    a("")
    w = dump.get("wild_area_news_2021")
    if not w:
        a("Il dump non porta il confronto: il generatore è stato eseguito senza la pagina.")
    else:
        mancanti = [(e["evento"], v) for e in w["dettaglio"] for v in e["voci"] if not v["nella_libreria"]]
        nell_indice = sum(1 for e in w["dettaglio"] for v in e["voci"] if v["nell_indice_migliore"])
        a("La pagina Bulbapedia delle Wild Area News del 2021, nel testo recuperato in `_notes/fonti/corpus-residuo/recuperati-2026-10-05/%s`, elenca %d eventi, di cui %d con una tabella di incontri, e %d voci distinte per evento contate su specie, forma, Gigantamax e cromatico. Di queste %d hanno la chiave nella libreria e %d stanno nell'indice della libreria che ha più specie in comune con l'evento, misurato con l'indice di Jaccard sulle coppie di specie e forma. Le voci assenti dalla libreria sono %d." % (
            w["fonte"], w["eventi"], w["eventi_con_tabella"], w["voci_distinte"], w["voci_nella_libreria"], nell_indice, len(mancanti)))
        for ev, v in mancanti:
            a("")
            a("- %s, evento «%s», chiave `%s`: la pagina la descrive come incursione non catturabile, quindi la libreria correttamente non la porta." % (v["voce"], ev, v["chiave"]) if "Cinderace" in v["voce"] else "- %s, evento «%s», chiave `%s`." % (v["voce"], ev, v["chiave"]))
        a("")
        a("| Evento | Indice | Somiglianza | Voci | Nella libreria | Nell'indice |")
        a("|---|---|---|---|---|---|")
        for e in w["dettaglio"]:
            vv = e["voci"]
            a("| %s | %s | %s | %d | %d | %d |" % (cella(e["evento"]), cella(e["indice_migliore"]), e["somiglianza"], len(vv),
                                                 sum(1 for v in vv if v["nella_libreria"]), sum(1 for v in vv if v["nell_indice_migliore"])))
        a("")
        a("L'evento del primo aprile 2021 portava soltanto Magikarp non catturabili, e la somiglianza bassa con il suo indice migliore lo riflette: la chiave di Magikarp esiste nella libreria per altri eventi.")
    a("")
    a("## Le chiavi")
    a("")
    a("Una riga per chiave di collezione. Versioni e indici sono quelli delle righe della libreria con quella chiave; «Copertura» nomina i lotti che la coprono, oppure il file generato in `lotto-incursioni-evento-swsh` con l'esito nel registro; «Incontro riconosciuto» è quello che la libreria attribuisce all'esemplare generato.")
    a("")
    a("| Chiave | N. | Specie | Forma | G | S | Versioni | Indici di evento | Altrove | Copertura | Incontro riconosciuto |")
    a("|---|---|---|---|---|---|---|---|---|---|---|")
    for k in chiavi:
        g = generati.get(k["chiave"])
        if g and g.get("conforme"):
            cop = "generato %s, %s" % (g["file"], "conforme" if conformi_reg.get(k["chiave"]) else "non nel registro")
            inc = g.get("incontro_riconosciuto", "")
        elif g:
            cop, inc = "non generabile: " + g.get("motivo", ""), ""
        else:
            cop, inc = ", ".join(k["coperta_da"]), ""
        a("| %s | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            k["chiave"], k["numero"], cella(k["specie"]), cella(nome_forma(k)), "sì" if k["gigantamax"] else "-",
            "sì" if k["cromatico_garantito"] else "-", " ".join(k["versioni"]), " ".join(str(i) for i in k["indici_evento"]),
            cella(k["disponibilità"]), cella(cop), cella(inc)))
    a("")
    return "\n".join(r)


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="non scrive: dice soltanto se il documento sul disco sia allineato")
    a = ap.parse_args(argv)
    for p in (DUMP, os.path.join(LOTTO, "rapporto.json"), REGISTRO):
        if not os.path.exists(p):
            print("manca %s: il dump e il lotto stanno in _notes/, fuori da git, e si producono con tools/pkhex-incursioni-swsh" % p)
            return 2
    testo = componi(leggi(DUMP), leggi(os.path.join(LOTTO, "rapporto.json")), leggi(REGISTRO))
    if a.check:
        attuale = io.open(USCITA, encoding="utf-8", newline="").read() if os.path.exists(USCITA) else None
        if attuale != testo:
            print("%s non è allineato al dump: rigenerare" % USCITA)
            return 1
        print("%s allineato" % USCITA)
        return 0
    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    print("scritto %s" % USCITA)
    return 0


if __name__ == "__main__":
    sys.exit(main())
