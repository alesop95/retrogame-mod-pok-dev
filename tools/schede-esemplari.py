#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la scheda tecnica di ciascun esemplare producibile, con lo stato del suo giudizio.

Perché esiste
-------------
Quando un esemplare è dichiarato conforme da un verificatore indipendente, quel giudizio riguarda
una configurazione precisa di byte e non una categoria: vale per quel valore di personalità, quei
valori individuali, quel nome, quel seme. Registrare soltanto che l'esemplare è conforme perde
l'informazione che serve, cioè che cosa esattamente sia stato dichiarato conforme; e senza quella
non si può né riprodurre il caso, né riconoscere che una modifica successiva lo ha cambiato.

Questo documento è dunque l'inventario delle caratteristiche tecniche univoche di ciascun
esemplare, accanto allo stato del suo giudizio esterno. È generato e non trascritto, e non legge
i file prodotti: ricalcola gli esemplari dalle sorgenti con il medesimo codice che li scrive. La
differenza è sostanziale. Un documento che leggesse i file descriverebbe ciò che c'è sul disco di
questa macchina, che non è versionato e può non esserci; questo descrive ciò che il progetto
produce, e resta vero in un clone dove i file non sono stati ancora generati. È anche una
verifica implicita del determinismo: se due corse dessero schede diverse, la scelta del seme non
sarebbe riproducibile e il documento cambierebbe da sé, rendendo il difetto visibile.

Che cosa non contiene, e perché
-------------------------------
Le voci che dipendono dall'allenatore di destinazione non portano i valori derivati da esso, e lo
dichiarano. Non è una lacuna: quel dato non appartiene all'evento ma al salvataggio in cui verrà
riscattato, quindi scriverlo qui significherebbe fissare nel documento una scelta che appartiene a
chi lo userà.

Uso
---
    python tools/schede-esemplari.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex
    python tools/schede-esemplari.py --ace ... --pkhex ... --check
"""

import argparse
import importlib.util
import io
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))

from pokebridge import eventi  # noqa: E402

GIUDIZI = os.path.join(RADICE, "recreate-pokemon-distributions-events", "giudizi-esterni.json")
PROVENIENZE = os.path.join(RADICE, "recreate-pokemon-distributions-events",
                           "provenienze-eventi.json")
USCITA = os.path.join(RADICE, "recreate-pokemon-distributions-events", "SCHEDE-ESEMPLARI.md")

# Le venticinque nature, nell'ordine in cui il resto per venticinque del valore di personalità le
# indicizza. L'ordine è quello canonico della terza generazione e non alfabetico.
NATURE = ("Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed",
          "Impish", "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild",
          "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky")

# L'ordine in cui i sei valori individuali escono dal generatore, che non è quello in cui il
# gioco li mostra: scriverlo qui evita di dedurlo dalla posizione dei bit ogni volta.
ORDINE_MOSTRATO = (("ps", "PS"), ("attacco", "Att"), ("difesa", "Dif"),
                   ("attacco_speciale", "Asp"), ("difesa_speciale", "Dsp"), ("velocita", "Vel"))


def carica_generatore():
    percorso = os.path.join(RADICE, "tools", "genera-evento-gen3.py")
    spec = importlib.util.spec_from_file_location("genera_evento_gen3", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def stato_giudizi():
    """Lo stato del giudizio esterno per indice di voce, dal registro autorato."""
    if not os.path.exists(GIUDIZI):
        return {}
    dati = json.loads(io.open(GIUDIZI, encoding="utf-8").read())
    fuori = {}
    for g in dati["giudizi"]:
        base = os.path.basename(g["file"])
        if len(base) > 3 and base[:3].isdigit():
            indice = int(base[:3])
            # Un giudizio successivo sostituisce il precedente sul medesimo esemplare: l'ultimo
            # in ordine di registro è lo stato corrente, e il registro è in ordine cronologico.
            fuori[indice] = g
    return fuori


def provenienze():
    """La provenienza storica per gruppo di evento, dal file autorato.

    Serve alle schede perche' un esemplare da evento e' un oggetto storico prima che un dato, e
    chi legge una scheda vuole sapere non soltanto quali byte porta ma da dove viene. Le due
    informazioni hanno gradi di verita' diversi e restano distinte anche nella scheda: i dati
    tecnici sono calcolati, la provenienza e' letta da una fonte che si cita.
    """
    if not os.path.exists(PROVENIENZE):
        return {}, {}
    dati = json.loads(io.open(PROVENIENZE, encoding="utf-8").read())
    return dati.get("gruppi", {}), dati.get("fonti", {})


def riga_provenienza(prov, fonti, nome_ot, ident):
    """Le righe di provenienza di una scheda, compatte e con la fonte citata.

    Sono compatte per scelta: la trattazione distesa di ciascun evento sta nel catalogo, e
    ripeterla in centosettantadue schede produrrebbe un documento in cui la medesima pagina
    ricorre venti volte. Qui stanno i fatti che chi guarda un esemplare vuole sapere subito,
    cioe' quale evento fu, quando, dove e in che modo, con il collegamento per approfondire.
    """
    chiave = "%s|%d" % (nome_ot, ident)
    v = prov.get(chiave)
    if v is None:
        return ["Provenienza storica non documentata per questo gruppo di evento.", ""]
    # Le parti si uniscono in una riga sola, perche' la convenzione del progetto vuole un
    # paragrafo su una riga sorgente unica e un documento generato deve nascere conforme: se
    # nascesse da unire, il controllo di formattazione fallirebbe dopo ogni rigenerazione e
    # qualcuno finirebbe per disattivarlo.
    parti = ["**%s.** Quando: %s. Dove: %s. Come: %s."
             % (v.get("nome", "evento senza nome"), v.get("date", "non documentate"),
                v.get("luogo", "non documentato"), v.get("come", "non documentato"))]
    if v.get("fonte") and v["fonte"] in fonti:
        f = fonti[v["fonte"]]
        parti.append("Fonte: [%s](%s), letta il %s." % (f["titolo"], f["url"], f["letta"]))
    else:
        parti.append("Fonte: nessuna ancora letta per questo gruppo, quindi le tre voci "
                     "precedenti sono dichiarate non documentate e non vanno citate.")
    if v.get("divergenze"):
        parti.append("Su questo gruppo le fonti divergono: la voce corrispondente del catalogo "
                     "riporta la divergenza e l'argomento con cui è stata risolta.")
    return [" ".join(parti), ""]


def scheda(g, voci, indice, contesto):
    """Il blocco di una singola voce, con tutte le sue caratteristiche derivate."""
    (ace, pkhex, mappa, per_id, gruppi, pp_base, nomi, semi_mystry, abilita, posizioni,
     storici, prov, fonti) = contesto
    v = voci[indice]
    nome_ot = v.get("ot", "")
    lingua = v.get("lingua", "English")
    specie_id = mappa.get(v["nazionale"])
    ident = v.get("identificativo")
    derivazione = v.get("sesso_ot")
    fuori = []

    titolo = v.get("commento") or (nome_ot or "evento") or "evento"
    fuori.append("### %03d %s" % (indice, titolo))
    fuori.append("")
    fuori.extend(riga_provenienza(prov, fonti, nome_ot, int(ident) if ident is not None else 0))

    if ident is None or derivazione == "Recipient" or not nome_ot:
        fuori.append("Questa voce prende dall'allenatore di destinazione uno o più fra nome, "
                     "identificativo e sesso, quindi le sue caratteristiche derivate dipendono "
                     "dal salvataggio in cui verrà riscattata e non sono fissate qui. Ciò che "
                     "l'evento fissa resta il metodo di generazione, cioè %s, la lucentezza %s "
                     "e la lingua %s."
                     % (v.get("metodo"), v.get("lucentezza") or "non vincolata", lingua))
        fuori.append("")
        return fuori

    semi = list(eventi.semi_ammessi(v["metodo"], semi_mystry))
    partenza = (1 + indice) & 0xFFFF or 1
    if v["metodo"] in ("BACD_RBCD", "BACD_M"):
        taglio = partenza % max(1, len(semi))
        semi = semi[taglio:] + semi[:taglio]
    else:
        semi = list(range(partenza, 0x10000)) + list(range(0, partenza))
    esito = eventi.esemplare_da_evento(
        v["metodo"], int(ident) & 0xFFFF, (int(ident) >> 16) & 0xFFFF, v.get("lucentezza"),
        specie=v["nazionale"], desiderio=v.get("desiderio"), derivazione=derivazione,
        semi_mystry=semi_mystry, semi=semi)
    if esito is None:
        fuori.append("Nessun seme soddisfa i vincoli dichiarati da questa voce.")
        fuori.append("")
        return fuori

    p = esito["personalita"]
    iv = esito["iv"]
    oggetto = 0
    if esito["estrazione_oggetto"] is not None:
        oggetto = eventi.oggetto_tenuto_desiderio(esito["estrazione_oggetto"])
    else:
        oggetto = storici.get("%s|%d" % (nome_ot, int(ident)), {}).get(v["nazionale"], 0)
    fiocchi = g.parola_fiocchi_merito(v.get("fiocchi", []), posizioni)
    mosse = [m for m in v.get("mosse", []) if m]

    fuori.append("| Campo | Valore | Da dove viene |")
    fuori.append("|---|---|---|")
    # Il nome di questo campo dipende dal metodo, e usarne uno solo sarebbe scorretto: per il
    # metodo a elenco il valore cercato non e' un seme ma la posizione nell'elenco degli
    # ottantacinque semi distribuiti, mentre per gli altri e' il seme stesso. Chiamarlo seme in
    # entrambi i casi confonderebbe due cose diverse, e il verificatore per quel metodo dichiara
    # come seme di origine il valore dell'elenco e non la posizione.
    if v["metodo"] == "BACD_M":
        fuori.append("| posizione nell'elenco | %d | l'elenco degli ottantacinque semi "
                     "storicamente distribuiti, percorso a partire dall'indice della voce |"
                     % (esito["seme"],))
        fuori.append("| seme di origine | `0x%08X` | il valore dell'elenco a quella posizione, "
                     "che è ciò che il verificatore ricostruisce |"
                     % (esito["seme_effettivo"],))
    else:
        fuori.append("| seme di origine | `0x%04X` | scelto fra gli ammessi verificando i "
                     "vincoli, con partenza dall'indice della voce |" % (esito["seme"],))
        if esito["seme_effettivo"] != esito["seme"]:
            fuori.append("| seme effettivo | `0x%08X` | il seme di origine avanzato di due "
                         "passi dalla consultazione della tabella dei doni; il verificatore lo "
                         "dichiara accanto al seme di origine, fra parentesi |"
                         % (esito["seme_effettivo"],))
    fuori.append("| valore di personalità | `0x%08X` | prime estrazioni, secondo il ramo del "
                 "metodo |" % (p,))
    fuori.append("| natura | %s | resto per venticinque del valore di personalità |"
                 % (NATURE[p % 25],))
    fuori.append("| bit dell'abilità | %d | bit meno significativo del valore di personalità, "
                 "oppure zero se la specie ha una sola abilità |"
                 % (g.bit_abilita(p, specie_id, abilita),))
    fuori.append("| cromatico | %s | somma esclusiva delle quattro parole sotto otto |"
                 % ("sì" if esito["cromatico"] else "no",))
    fuori.append("| valori individuali | %s | due estrazioni, cinque bit per campo |"
                 % (" / ".join("%d %s" % (iv[k], et) for k, et in ORDINE_MOSTRATO),))
    fuori.append("| allenatore | `%s` | dichiarato dalla tabella |" % (nome_ot,))
    fuori.append("| identificativo, segreto | %d, %d | dichiarati dalla tabella |"
                 % (int(ident) & 0xFFFF, (int(ident) >> 16) & 0xFFFF))
    fuori.append("| sesso dell'allenatore | %s | derivazione %s |"
                 % (esito["sesso_ot"], derivazione or "non dichiarata"))
    fuori.append("| lingua | %s | dichiarata dalla tabella |" % (lingua,))
    fuori.append("| specie interna, soprannome | %d, `%s` | numero nazionale %d, nome nella "
                 "lingua della voce |"
                 % (specie_id, nomi.setdefault(lingua, g.nomi_specie_per_lingua(ace, lingua))
                    .get(specie_id, "?"), v["nazionale"]))
    fuori.append("| livello, esperienza | %d, %d | livello dichiarato, esperienza dalla formula "
                 "del gruppo di crescita |"
                 % (v["livello"], g.esperienza(gruppi.get(specie_id), v["livello"])))
    fuori.append("| mosse | %s | dichiarate dalla tabella |"
                 % (", ".join(str(m) for m in mosse) or "nessuna",))
    fuori.append("| punti potenza | %s | dal valore base di ciascuna mossa |"
                 % (", ".join(str(pp_base.get(m, 0)) for m in mosse) or "nessuno",))
    fuori.append("| oggetto tenuto | %s | %s |"
                 % (oggetto or "nessuno",
                    "derivato dalla quinta estrazione" if esito["estrazione_oggetto"] is not None
                    else ("documentato dalla provenienza storica" if oggetto
                          else "l'evento non ne dichiara alcuno")))
    fuori.append("| fiocchi di merito | `0x%03X` | %s |"
                 % (fiocchi, ", ".join(v.get("fiocchi", [])) or "nessuno dichiarato"))
    fuori.append("| incontro fatidico | %s | dichiarato dalla tabella |"
                 % ("sì" if v.get("fatidico") else "no",))
    fuori.append("| metodo, lucentezza | %s, %s | dichiarati dalla tabella |"
                 % (v.get("metodo"), v.get("lucentezza") or "non vincolata"))
    fuori.append("")
    return fuori


def componi(ace, pkhex):
    g = carica_generatore()
    voci = g.voci_wc3(pkhex)
    mappa = g.nazionale_verso_interno(ace)
    _per_nome, per_id = g.specie_per_nome(ace)
    gruppi = g.gruppo_di_crescita(ace)
    pp_base = g.punti_potenza(ace)
    semi_mystry = g.semi_mystry_mew(pkhex)
    abilita = g.abilita_per_specie(ace)
    posizioni = g.bit_fiocchi(pkhex)
    storici = g.oggetti_documentati()
    prov, fonti = provenienze()
    contesto = (ace, pkhex, mappa, per_id, gruppi, pp_base, {}, semi_mystry, abilita,
                posizioni, storici, prov, fonti)
    giudizi = stato_giudizi()

    producibili = [i for i, v in enumerate(voci)
                   if v.get("metodo") in g.METODI_PRODUCIBILI and not v.get("uovo")
                   and "ot_irrisolto" not in v]
    conformi = [i for i in producibili
                if i in giudizi and "conforme" in (giudizi[i].get("esito") or "")]

    fuori = []
    fuori.append("# Schede tecniche degli esemplari producibili")
    fuori.append("")
    fuori.append("> Documento generato da `tools/schede-esemplari.py`. Non si modifica a mano, e "
                 "non legge i file prodotti: ricalcola gli esemplari dalle sorgenti con il "
                 "medesimo codice che li scrive.")
    fuori.append("")
    fuori.append("Un giudizio di conformità riguarda una configurazione precisa di byte e non "
                 "una categoria: vale per quel valore di personalità, quei valori individuali, "
                 "quel nome e quel seme. Registrare soltanto che un esemplare è conforme perde "
                 "l'informazione che serve, cioè che cosa esattamente sia stato dichiarato "
                 "conforme, e senza quella non si può né riprodurre il caso né riconoscere che "
                 "una modifica successiva lo ha cambiato. Questo documento è dunque "
                 "l'inventario delle caratteristiche univoche di ciascun esemplare, accanto "
                 "allo stato del suo giudizio.")
    fuori.append("")
    fuori.append("Che il documento sia ricalcolato e non letto dal disco ha una conseguenza che "
                 "vale dichiarare: esso è anche una verifica del determinismo della produzione. "
                 "Se due corse dessero schede diverse, la scelta del seme non sarebbe "
                 "riproducibile, e il difetto si manifesterebbe come una modifica del documento "
                 "senza che nulla sia stato modificato a mano.")
    fuori.append("")
    fuori.append("Stato: %d voci producibili, di cui %d dichiarate conformi da un verificatore "
                 "indipendente al momento dell'ultima generazione di questo documento. Le voci "
                 "conformi portano la dicitura accanto al titolo; le altre non sono state "
                 "giudicate oppure lo sono state con rilievi, e il registro dei giudizi in "
                 "`giudizi-esterni.json` dice quale dei due casi."
                 % (len(producibili), len(conformi)))
    fuori.append("")
    for i in producibili:
        blocco = scheda(g, voci, i, contesto)
        if i in giudizi:
            esito = giudizi[i].get("esito") or ""
            blocco[0] = blocco[0] + "  (giudizio: %s, %s)" % (esito, giudizi[i].get("data", ""))
        fuori.extend(blocco)
    return "\n".join(fuori).rstrip("\n") + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--ace", required=True)
    ap.add_argument("--pkhex", required=True)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    testo = componi(a.ace, a.pkhex)
    if a.check:
        if not os.path.exists(USCITA):
            print("le schede non esistono ancora: vanno generate")
            return 1
        if io.open(USCITA, encoding="utf-8").read() == testo:
            print("le schede sono allineate alle sorgenti")
            return 0
        print("le schede NON sono allineate alle sorgenti: vanno rigenerate")
        return 1
    io.open(USCITA, "w", encoding="utf-8", newline="").write(testo)
    print("scritto " + os.path.relpath(USCITA, RADICE))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
