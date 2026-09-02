#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera il catalogo delle distribuzioni, unendo i fatti meccanici alla provenienza storica.

Perché esiste
-------------
Il generatore di esemplari produce centoventidue file con nomi come `008-ANAPikachu-Pikachu.pk3`,
e quel nome è tutto ciò che dice da dove venga quell'esemplare. Non basta. Un esemplare da evento
è un oggetto storico prima che un dato: è stato consegnato in un luogo, in una finestra di giorni
che a volte durava tre ore e a volte tre anni, e in un modo che ne spiega la rarità. Chi ricrea
quegli esemplari senza sapere questo sta copiando byte; chi lo sa sta ricostruendo una collezione.

Il documento prodotto tiene le due cose separate e dichiarate, perché hanno gradi di verità
diversi. I fatti meccanici, cioè specie, livello, mosse, lingua, metodo di generazione,
lucentezza e derivazione del sesso, vengono dalla tabella del verificatore di conformità, che è
codice eseguito e non prosa, e si rigenerano a ogni corsa: se la tabella cambia, il documento
cambia. I fatti storici, cioè date, luoghi e modo di distribuzione, non stanno in nessuna fonte
di primo livello, perché nessun disassemblato sa in quali negozi un dono venne consegnato: stanno
nell'enciclopedia collaborativa, sono autorati in `provenienze-eventi.json` con il collegamento e
la data di lettura, e il documento li riporta attribuendoli.

La copertura è un numero e non un'impressione
---------------------------------------------
I gruppi senza provenienza documentata non vengono taciuti: il documento li elenca con la dicitura
esplicita, e il programma stampa quanti sono. È la differenza fra un catalogo che sembra completo
e uno che dice quanto è completo. Un documento che nasconda le proprie lacune è peggio di un
documento incompleto, perché toglie a chi lo legge la possibilità di colmarle.

Uso
---
    python tools/catalogo-eventi.py --ace _notes/fonti/ace-builder --pkhex _notes/fonti/pkhex
    python tools/catalogo-eventi.py --ace ... --pkhex ... --check

Il secondo modo non scrive nulla e riferisce se il documento in repository sia allineato alle
fonti, cosicché una modifica alla tabella o alle provenienze che non sia stata rigenerata risulti
visibile prima di un commit invece che dopo.
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

PROVENIENZE = os.path.join(RADICE, "recreate-pokemon-distributions-events",
                           "provenienze-eventi.json")
USCITA = os.path.join(RADICE, "recreate-pokemon-distributions-events", "CATALOGO-EVENTI.md")

# Le diciture italiane dei valori che la tabella scrive in inglese. Si traducono qui e non nel
# testo, perché un elenco chiuso di traduzioni è verificabile mentre una traduzione sparsa nel
# corpo del documento non lo è.
LUCENTEZZA = {
    None: "non vincolata",
    "Random": "non vincolata",
    "Never": "negata, cioè l'esemplare non può essere cromatico",
    "Always": "garantita, cioè l'esemplare è cromatico per costruzione",
}

SESSO = {
    None: "non dichiarata dalla tabella",
    "Recipient": "copiato da chi riceve, quindi non è un dato dell'evento",
    "Only0": "fissato a maschio",
    "Only1": "fissato a femmina",
    "RandD3": "bit meno significativo del quoziente per tre della quinta estrazione",
    "RandS3": "bit di posizione tre della quinta estrazione",
    "RandS7": "bit di posizione sette della quinta estrazione, negato",
    "RandSG15": "bit di posizione quindici della sesta estrazione, perché fra i valori "
                "individuali e il sesso si consuma l'estrazione dell'oggetto tenuto",
    "RandD3_0": "dichiarato maschio, con il seme tenuto coerente con la derivazione",
    "RandD3_1": "dichiarato femmina, con il seme tenuto coerente con la derivazione",
    "RandAlgo": "determinata da un algoritmo che la fonte stessa dichiara di non verificare "
                "con la logica ordinaria",
}

METODO = {
    "BACD": "composizione invertita, seme non ristretto",
    "BACD_A": "composizione invertita con anti-lucentezza",
    "BACD_R": "composizione invertita, seme ristretto a sedici bit",
    "BACD_R_A": "composizione invertita con anti-lucentezza additiva, seme ristretto a sedici bit",
    "BACD_RBCD": "seme ristretto a duecentoquattordici valori, letti dall'orologio della "
                 "cartuccia come somma delle cifre dell'ora in decimale codificato in binario",
    "BACD_TA": "seme passato per la tabella aritmetica degli otto doni, poi avanzato di due",
    "BACD_TS": "come il precedente, con lucentezza garantita dalla tabella",
    "BACD_U_AX": "anti-lucentezza per somma esclusiva, con un numero variabile di estrazioni",
    "BACD_M": "seme cercato in un elenco di ottantacinque valori effettivamente distribuiti",
    "Method_2": "composizione ordinaria seguita da una estrazione consumata e non usata",
    "Channel": "generatore pseudocasuale dei titoli per la console domestica, diverso da quello "
               "della terza generazione su cartuccia",
}

VERSIONE = {
    "R": "Rubino", "S": "Zaffiro", "E": "Smeraldo", "FR": "Rosso Fuoco", "LG": "Verde Foglia",
    "RS": "Rubino o Zaffiro", "FRLG": "Rosso Fuoco o Verde Foglia",
    "EFL": "Smeraldo, Rosso Fuoco o Verde Foglia",
}


def carica_generatore():
    """Il generatore di esemplari, importato per percorso perché il suo nome porta trattini."""
    percorso = os.path.join(RADICE, "tools", "genera-evento-gen3.py")
    spec = importlib.util.spec_from_file_location("genera_evento_gen3", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def chiave(voce):
    """La coppia che individua un evento, scritta come una stringa sola.

    È il nome dell'allenatore e l'identificativo, e non l'identificativo da solo: nel catalogo
    esistono due coppie distinte che condividono l'identificativo e si distinguono per il nome,
    cioè il Pikachu di Sapporo con il Wobbuffet della trasmissione domenicale, e il Metang della
    festa giapponese con quello statunitense. Indicizzare per il solo identificativo unirebbe
    eventi diversi.
    """
    return "%s|%d" % (voce.get("ot", ""), int(voce.get("identificativo") or 0))


def raggruppa(voci):
    """Le voci raccolte per evento, conservando l'ordine in cui la tabella le dichiara."""
    gruppi = {}
    for indice, v in enumerate(voci):
        gruppi.setdefault(chiave(v), []).append((indice, v))
    return gruppi


def nome_specie(nomi, mappa, voce):
    """Il nome della specie, o la dichiarazione che non si è potuto risolvere."""
    interno = mappa.get(voce["nazionale"])
    if interno is None:
        return "specie con numero nazionale %d, non risolta" % voce["nazionale"]
    return nomi.get(interno, "identificativo interno %d" % interno)


def riga_voce(nomi, mappa, indice, voce):
    """La riga di tabella di una singola voce, con i suoi fatti meccanici."""
    mosse = [m for m in voce.get("mosse", []) if m]
    return "| %d | %s | %d | %s | %s | %s |" % (
        indice,
        nome_specie(nomi, mappa, voce),
        voce["livello"],
        VERSIONE.get(voce["versione"], voce["versione"]),
        "uovo" if voce.get("uovo") else "esemplare",
        str(len(mosse)) + (" mosse" if len(mosse) != 1 else " mossa"),
    )


def blocco_gruppo(prov, fonti, nomi, mappa, k, elementi):
    """La sezione di un gruppo di evento: prima la storia, poi i fatti meccanici."""
    ot, ident = k.rsplit("|", 1)
    p = prov.get(k)
    fuori = []
    titolo = p["nome"] if p else "Evento non ancora nominato"
    fuori.append("### %s" % titolo)
    fuori.append("")
    fuori.append("Nome dell'allenatore `%s`, identificativo %s, %d %s nel catalogo."
                 % (ot if ot else "(vuoto, cioè preso da chi riceve)", ident, len(elementi),
                    "voce" if len(elementi) == 1 else "voci"))
    fuori.append("")

    if p is None:
        fuori.append("Provenienza storica non ancora documentata. Questo gruppo non ha una voce "
                     "in `provenienze-eventi.json`, quindi di esso il progetto conosce i soli "
                     "fatti meccanici che la tabella dichiara, e non sa dire dove né quando né "
                     "come quel dono venne consegnato.")
        fuori.append("")
    else:
        if p.get("fonte"):
            f = fonti[p["fonte"]]
            attribuzione = ("Fonte: [%s](%s), letta il %s. Rango della fonte: %s."
                            % (f["titolo"], f["url"], f["letta"], f["rango"]))
        else:
            attribuzione = ("Fonte: nessuna ancora letta per questo gruppo, quindi ciò che "
                            "segue è dichiarato come non documentato e non va citato.")
        fuori.append("Quando: %s. Dove: %s. Come: %s." % (p["date"], p["luogo"], p["come"]))
        fuori.append("")
        fuori.append(attribuzione)
        fuori.append("")
        if p.get("oggetto_tenuto"):
            fuori.append("Oggetto tenuto: %s" % p["oggetto_tenuto"])
            fuori.append("")
        if p.get("note"):
            fuori.append(p["note"])
            fuori.append("")
        if p.get("divergenze"):
            fuori.append("Divergenza fra le fonti: %s" % p["divergenze"])
            fuori.append("")

    # I fatti meccanici, comuni al gruppo e poi voce per voce.
    prima = elementi[0][1]
    fuori.append("Metodo di generazione: %s. Lucentezza: %s. Sesso dell'allenatore: %s. "
                 "Lingua dichiarata: %s. Incontro fatidico: %s."
                 % (METODO.get(prima.get("metodo"), str(prima.get("metodo"))),
                    LUCENTEZZA.get(prima.get("lucentezza"), str(prima.get("lucentezza"))),
                    SESSO.get(prima.get("sesso_ot"), str(prima.get("sesso_ot"))),
                    prima.get("lingua", "non dichiarata, quindi quella di chi riceve"),
                    "sì" if prima.get("fatidico") else "no"))
    fuori.append("")
    fuori.append("| Indice | Specie | Livello | Gioco di origine | Forma | Mosse |")
    fuori.append("|---|---|---|---|---|---|")
    for indice, v in elementi:
        fuori.append(riga_voce(nomi, mappa, indice, v))
    fuori.append("")
    return fuori


def componi(ace, pkhex):
    """Il documento intero, come stringa."""
    g = carica_generatore()
    voci = g.voci_wc3(pkhex)
    mappa = g.nazionale_verso_interno(ace)
    nomi = g.nomi_specie_per_lingua(ace, "English")
    dati = json.loads(io.open(PROVENIENZE, encoding="utf-8").read())
    prov, fonti = dati["gruppi"], dati["fonti"]
    gruppi = raggruppa(voci)

    documentati = sum(1 for k in gruppi if k in prov and prov[k].get("fonte"))
    dichiarati = sum(1 for k in gruppi if k in prov and not prov[k].get("fonte"))
    assenti = sum(1 for k in gruppi if k not in prov)

    fuori = []
    fuori.append("# Catalogo delle distribuzioni di terza generazione, con la loro provenienza")
    fuori.append("")
    fuori.append("> Documento generato da `tools/catalogo-eventi.py`. Non si modifica a mano: i "
                 "fatti meccanici vengono dalla tabella del verificatore di conformità e si "
                 "rigenerano a ogni corsa, mentre la provenienza storica è autorata in "
                 "`provenienze-eventi.json`, che è il file da modificare.")
    fuori.append("")
    fuori.append("Questo catalogo esiste perché un esemplare da evento è un oggetto storico "
                 "prima che un dato. Il generatore produce file i cui nomi dicono la specie e "
                 "poco altro; qui accanto a ciascun gruppo stanno il luogo, la finestra di "
                 "giorni e il modo in cui quel dono venne consegnato, che sono le tre cose che "
                 "ne spiegano la rarità e che nessun disassemblato può dire.")
    fuori.append("")
    fuori.append("Le due categorie di fatti hanno gradi di verità diversi e restano separate. I "
                 "fatti meccanici, cioè specie, livello, mosse, lingua, metodo di generazione, "
                 "lucentezza e derivazione del sesso dell'allenatore, vengono da codice "
                 "eseguito da un verificatore. I fatti storici vengono da un'enciclopedia "
                 "collaborativa, sono attribuiti uno per uno con il collegamento e la data di "
                 "lettura, e dove essa contraddice la tabella la contraddizione è scritta "
                 "invece di essere risolta in silenzio.")
    fuori.append("")
    fuori.append("Stato della copertura: %d gruppi in tutto, di cui %d con provenienza letta da "
                 "una fonte citata, %d con una voce che dichiara esplicitamente di non avere "
                 "ancora una fonte, e %d senza alcuna voce. I gruppi senza fonte non sono "
                 "taciuti, e il conteggio è qui perché un catalogo che nasconda le proprie "
                 "lacune è peggio di uno incompleto: toglie a chi legge la possibilità di "
                 "colmarle."
                 % (len(gruppi), documentati, dichiarati, assenti))
    fuori.append("")
    fuori.append("## I gruppi, nell'ordine in cui la tabella li dichiara")
    fuori.append("")
    for k, elementi in gruppi.items():
        fuori.extend(blocco_gruppo(prov, fonti, nomi, mappa, k, elementi))
    return "\n".join(fuori).rstrip("\n") + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--ace", required=True, help="cartella del costruttore della comunità")
    ap.add_argument("--pkhex", required=True, help="cartella del clone del verificatore")
    ap.add_argument("--check", action="store_true",
                    help="non scrive nulla e riferisce se il documento è allineato alle fonti")
    a = ap.parse_args(argv)

    testo = componi(a.ace, a.pkhex)
    if a.check:
        if not os.path.exists(USCITA):
            print("il catalogo non esiste ancora: va generato")
            return 1
        attuale = io.open(USCITA, encoding="utf-8").read()
        if attuale == testo:
            print("il catalogo è allineato alle fonti")
            return 0
        print("il catalogo NON è allineato alle fonti: va rigenerato")
        return 1
    io.open(USCITA, "w", encoding="utf-8", newline="").write(testo)
    print("scritto " + os.path.relpath(USCITA, RADICE))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
