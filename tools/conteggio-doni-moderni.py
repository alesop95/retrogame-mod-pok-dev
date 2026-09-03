#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conta le voci della base dei doni segreti dalla quarta alla nona generazione.

Perché esiste
-------------
Il catalogo degli eventi di terza generazione è stato costruito leggendo una tabella che vive nel
codice della fonte, perché quella generazione non ha mai avuto un formato binario uniforme per i
doni. Dalla quarta in avanti il formato esiste, e la fonte porta la propria base dati come una
serie di file binari: il lavoro non è dunque ricostruire un algoritmo ma contare, catalogare e
misurare una campagna, che è lavoro di natura diversa e molto minore.

Questo programma fa i primi due dei tre passi, cioè il conteggio e la catalogazione, e li fa in
modo che i numeri non siano trascritti. Dal 2026-09-03 legge anche la specie di ciascun dono, che
è il dato che serve al Pokedex: le voci non sono specie, perché la medesima distribuzione compare
come voce distinta per ogni regione e ogni lingua in cui fu fatta, quindi il conteggio delle voci
sovrastima di molto il contributo alla collezione e soltanto l'insieme delle specie distinte lo
misura.

Sul perché la lettura della specie sia stata aggiunta qui invece che in un programma nuovo, la
ragione è la lezione del 2026-09-03: due programmi che hanno bisogno della medesima lettura la
duplicano, e la duplicazione produce numeri plausibili e diversi. La tabella dei file e delle
lunghezze di record vive in un posto solo, e chi ha bisogno delle specie chiama questo.

La ragione per cui il conteggio merita un programma invece di una divisione fatta a mano è che la
divisione a mano sbaglia: quattro dei dodici file sono serie piatte di record di lunghezza fissa e
si dividono, ma tre non lo sono, e su uno di essi la divisione ingenua dà settecentododici voci
contro le settecentonove vere.

I tre casi che non si dividono
------------------------------
Il primo è la quinta generazione, dove ogni record porta un byte in più, raccolto in coda al file
invece che accanto al record: quel byte codifica in quattro bit la restrizione di versione e in
altri quattro quella di lingua. Il passo effettivo è dunque la lunghezza del record più uno, e
non la lunghezza del record.

Il secondo e il terzo sono la sesta e la settima generazione, dove la base è divisa in due file
per la medesima generazione: uno con la carta completa e uno con il solo dono. Non sono due
codifiche dello stesso insieme ma due insiemi distinti che la fonte concatena, quindi il conto
della generazione è la somma dei due e non il massimo.

Il conteggio porta con sé una verifica che vale dichiarare, perché è gratuita e coglie l'errore
più probabile. Se la lunghezza di un file non è un multiplo esatto del passo dichiarato, la
lunghezza del record che stiamo usando è sbagliata: il programma lo segnala come difetto invece
di arrotondare, e i tre casi speciali sopra sono stati trovati esattamente così.

Uso
---
    python tools/conteggio-doni-moderni.py --pkhex <clone di PKHeX>
    python tools/conteggio-doni-moderni.py --pkhex <clone> --markdown <file>
"""

import argparse
import io
import os
import struct
import sys

MGDB = os.path.join("PKHeX.Core", "Resources", "legality", "mgdb")

# (generazione, titoli, file, lunghezza del record, passo, provenienza della lunghezza)
#
# Il passo differisce dalla lunghezza del record soltanto per la quinta generazione, e la
# ragione sta nel docstring. Le lunghezze vengono dai campi Size delle classi omonime in
# PKHeX.Core/MysteryGifts/, lette il 2026-09-02, e non sono misurate sui file: misurarle sui
# file significherebbe dedurre il formato dal dato, che è il ragionamento circolare per cui una
# lunghezza sbagliata sembra giusta.
FAMIGLIE = (
    (4, "Diamante, Perla, Platino, HeartGold e SoulSilver", ("wc4.pkl",), 0x358, 0x358, "PCD.Size"),
    (5, "Bianco, Nero e i loro seguiti", ("pgf.pkl",), 0xCC, 0xCC + 1, "PGF.Size piu' il byte di restrizione"),
    (6, "X, Y, Rubino Omega e Zaffiro Alpha", ("wc6full.pkl", "wc6.pkl"), None, None, "WC6Full.Size e WC6.Size"),
    (7, "Sole, Luna, UltraSole e UltraLuna", ("wc7full.pkl", "wc7.pkl"), None, None, "WC7Full.Size e WC7.Size"),
    (7, "Let's Go Pikachu ed Eevee", ("wb7full.pkl",), 0x310, 0x310, "WB7.Size"),
    (8, "Spada e Scudo", ("wc8.pkl",), 0x2D0, 0x2D0, "WC8.Size"),
    (8, "Leggende Arceus", ("wa8.pkl",), 0x2C8, 0x2C8, "WA8.Size"),
    (8, "Diamante Lucente e Perla Splendente", ("wb8.pkl",), 0x2DC, 0x2DC, "WB8.Size"),
    (9, "Scarlatto e Violetto", ("wc9.pkl",), 0x2C8, 0x2C8, "WC9.Size"),
    (9, "Leggende Z-A", ("wa9.pkl",), 0x2C8, 0x2C8, "WA9.Size"),
)

# I due file della sesta e della settima generazione hanno passi diversi fra loro, quindi la
# tabella sopra li lascia a None e questa dice quale passo vale per quale file.
PASSI_PER_FILE = {
    "wc6full.pkl": 0x310, "wc6.pkl": 0x108,
    "wc7full.pkl": 0x310, "wc7.pkl": 0x108,
}

# Gli offset dei campi dentro ciascun formato di record, letti dalle classi omonime in
# PKHeX.Core/MysteryGifts/ e dai template degli incontri in PKHeX.Core/Legality/Encounters/, il
# 2026-09-03. La chiave e' il nome del file, il valore dice dove sta la specie, dove la forma,
# dove il livello, e come si riconosce che il dono sia un esemplare e non un oggetto.
#
# Due fatti scoperti empiricamente e verificati su distribuzione plausibile, che vanno dichiarati
# perche' senza di essi il formato di quarta generazione sembrerebbe illeggibile. Il primo e' che
# i doni di quarta generazione contengono al proprio interno un esemplare nel formato del gioco,
# la cui parte utile e' normalmente cifrata; nella base dati della fonte sono invece conservati in
# chiaro, e la prova e' che duecentoquarantasette record su cinquecentonovanta portano un numero di
# specie compreso fra uno e quattrocentonovantatre mentre i restanti portano zero, che e' la firma
# di un oggetto e non di un esemplare. Il secondo e' che la specie di quel formato sta a otto byte
# dall'inizio dell'esemplare, che a sua volta sta a otto byte dall'inizio del dono.
#
# (specie, forma, livello, (offset del tipo, valori che indicano un esemplare), base della carta)
CAMPI = {
    # Prima e seconda generazione: non sono doni segreti ma tabelle di incontro, con i campi in
    # chiaro e senza alcun valore di personalita'. Da EncounterGift1 e EncounterGift2.
    "event1.pkl":    {"specie": 0, "byte": True, "livello": 1, "base": 0},
    "event2.pkl":    {"specie": 0, "byte": True, "livello": 1, "base": 0},
    # Quarta generazione: il tipo di dono e' una parola a inizio record, e i valori che indicano
    # un esemplare sono Pokemon, Uovo, Uovo di Manaphy e Pokemon da film, da GiftType4.
    "wc4.pkl":       {"specie": 8 + 0x08, "livello": None, "tipo": (0, {1, 2, 7, 13}),
                      "tipo16": True, "base": 0},
    # Quinta generazione: campi in chiaro nel record, con il tipo a 0xB3 e il valore uno per
    # l'esemplare. Da PGF.
    # Il passo di lettura differisce da quello del conteggio: vedi `leggi_specie`.
    "pgf.pkl":       {"specie": 0x1A, "forma": 0x1C, "livello": 0x5B, "tipo": (0xB3, {1}),
                      "base": 0, "passo_lettura": 0xCC},
    # Sesta e settima generazione: la carta e' identica nei due formati, e nel record esteso
    # comincia a 0x208, che e' la sua dimensione sottratta a quella del record. Da WC6, WC7, WB7 e
    # dai loro involucri. Il tipo sta a 0x51 e il valore zero indica l'esemplare.
    "wc6.pkl":       {"specie": 0x82, "forma": 0x84, "livello": 0xD0, "tipo": (0x51, {0}),
                      "base": 0},
    "wc6full.pkl":   {"specie": 0x82, "forma": 0x84, "livello": 0xD0, "tipo": (0x51, {0}),
                      "base": 0x208},
    "wc7.pkl":       {"specie": 0x82, "forma": 0x84, "livello": 0xD0, "tipo": (0x51, {0}),
                      "base": 0},
    "wc7full.pkl":   {"specie": 0x82, "forma": 0x84, "livello": 0xD0, "tipo": (0x51, {0}),
                      "base": 0x208},
    "wb7full.pkl":   {"specie": 0x82, "forma": 0x84, "livello": 0xD0, "tipo": (0x51, {0}),
                      "base": 0x208},
}


def leggi_specie(dati, nome, passo_conteggio, quante, campi):
    """Le specie dei doni di un file, con forma e livello dove il formato li porta.

    Riceve separatamente il passo con cui si contano le voci e quante voci ci siano, perche' su
    un formato i due numeri non coincidono e confonderli produce una lettura silenziosamente
    sbagliata. Il caso e' la quinta generazione, dove il byte di restrizione di ciascun record e'
    raccolto in coda al file: il passo del conteggio e' la lunghezza del record piu' uno, ma i
    record stanno l'uno accanto all'altro alla loro lunghezza vera, e i byte di coda seguono
    tutti insieme. Leggere a passo di conteggio disallinea progressivamente ogni record dopo il
    primo, e l'esito non e' un errore ma un numero plausibile: quindici esemplari su
    settecentonove, dove il vero e' un altro. Il difetto e' stato introdotto e corretto il
    2026-09-03, ed e' stato notato perche' quindici esemplari per la quinta generazione erano
    troppo pochi per essere credibili.

    Restituisce la lista delle terne trovate e il numero dei record che non sono esemplari. Un
    record che non e' un esemplare non e' un difetto: la medesima base dati porta oggetti, punti
    e altre consegne, e contarli fra le specie gonfierebbe il conto con voci che nessun Pokedex
    registra.
    """
    fuori, non_esemplari = [], 0
    base = campi.get("base", 0)
    passo = campi.get("passo_lettura", passo_conteggio)
    for indice in range(quante):
        off = indice * passo
        rec = dati[off:off + passo]
        if len(rec) < passo:
            break
        carta = rec[base:]
        tipo = campi.get("tipo")
        if tipo is not None:
            posizione, ammessi = tipo
            valore = (struct.unpack_from("<H", carta, posizione)[0]
                      if campi.get("tipo16") else carta[posizione])
            if valore not in ammessi:
                non_esemplari += 1
                continue
        if campi.get("byte"):
            specie = carta[campi["specie"]]
        else:
            specie = struct.unpack_from("<H", carta, campi["specie"])[0]
        if specie == 0:
            non_esemplari += 1
            continue
        forma = carta[campi["forma"]] if "forma" in campi else 0
        livello = (carta[campi["livello"]]
                   if campi.get("livello") is not None else None)
        fuori.append({"file": nome, "indice": indice, "specie": specie, "forma": forma,
                      "livello": livello})
    return fuori, non_esemplari


# I due file della prima e della seconda generazione. Non sono doni segreti, che in quelle
# generazioni non esistevano: sono le tabelle degli esemplari da evento distribuiti allora, e la
# fonte le tiene nella medesima cartella. Il loro formato non e' una serie di record di lunghezza
# fissa, quindi qui si riferisce la loro esistenza e la loro dimensione e non un conteggio.
EVENTI_ANTICHI = ("event1.pkl", "event2.pkl")

# Le generazioni che dipendono dalla banca per arrivare al deposito, cioe' quelle sotto scadenza.
# La settima comprende Let's Go, che pero' parla al deposito direttamente: e' l'eccezione che
# rende sbagliato sommare per generazione senza guardare il titolo.
SOTTO_SCADENZA = {4, 5, 6, 7}
DIRETTI = {"wb7full.pkl"}


def conta(pkhex):
    cartella = os.path.join(pkhex, MGDB)
    if not os.path.isdir(cartella):
        sys.exit("non trovo la base dei doni segreti in " + cartella + ": serve un clone di "
                 "PKHeX con quel percorso presente, e su un clone sparso va aggiunto")
    righe, difetti = [], []
    for generazione, titoli, files, _lunghezza, passo, provenienza in FAMIGLIE:
        voci, byte = 0, 0
        specie_trovate, non_esemplari = [], 0
        letti = True
        for nome in files:
            percorso = os.path.join(cartella, nome)
            if not os.path.exists(percorso):
                difetti.append((nome, "file assente"))
                continue
            dimensione = os.path.getsize(percorso)
            p = passo if passo is not None else PASSI_PER_FILE[nome]
            quoziente, resto = divmod(dimensione, p)
            if resto:
                # Il resto non si arrotonda: dice che il passo e' sbagliato, e proseguire
                # produrrebbe un conteggio plausibile e falso. E' cosi' che si e' scoperto il
                # byte di restrizione della quinta generazione.
                difetti.append((nome, "la dimensione %d non e' multipla del passo %d, resto %d: "
                                      "la lunghezza del record che stiamo usando e' sbagliata"
                                % (dimensione, p, resto)))
                continue
            voci += quoziente
            byte += dimensione
            campi = CAMPI.get(nome)
            if campi is None:
                # Il formato non e' fra quelli di cui questo programma sappia leggere i campi.
                # Va dichiarato come non letto e non come zero: uno zero non misurato e uno zero
                # misurato hanno lo stesso aspetto e significato opposto, ed e' precisamente il
                # difetto che questo progetto ha imparato a temere.
                letti = False
                continue
            trovate, scartati = leggi_specie(io.open(percorso, "rb").read(),
                                             nome, p, quoziente, campi)
            specie_trovate.extend(trovate)
            non_esemplari += scartati
        diretto = all(n in DIRETTI for n in files)
        righe.append({"generazione": generazione, "titoli": titoli, "files": files,
                      "voci": voci, "byte": byte, "provenienza": provenienza,
                      "sotto_scadenza": generazione in SOTTO_SCADENZA and not diretto,
                      "letti": letti,
                      "esemplari": len(specie_trovate),
                      "non_esemplari": non_esemplari,
                      "specie": sorted({v["specie"] for v in specie_trovate}),
                      "specie_forma": sorted({(v["specie"], v["forma"])
                                              for v in specie_trovate}),
                      "voci_dettaglio": specie_trovate})
    # Prima e seconda generazione. Dal 2026-09-03 non si limitano a essere nominate: il loro
    # formato e' stato letto ed e' banale, cioe' record di lunghezza fissa con i campi in chiaro,
    # otto byte in prima generazione e dodici in seconda. Ne segue un fatto che vale per la
    # roadmap piu' di qualunque conteggio: in quelle generazioni non esiste alcun valore di
    # personalita' e nessun generatore pseudocasuale da ricostruire, quindi produrre un esemplare
    # da evento significa scrivere la struttura con i campi dichiarati, che e' cio' che
    # `pokebridge` sa gia' fare e ha verificato.
    antichi = []
    for nome, passo in (("event1.pkl", 8), ("event2.pkl", 12)):
        percorso = os.path.join(cartella, nome)
        if not os.path.exists(percorso):
            continue
        dati = io.open(percorso, "rb").read()
        dimensione = len(dati)
        quoziente, resto = divmod(dimensione, passo)
        if resto:
            difetti.append((nome, "la dimensione %d non e' multipla del passo %d"
                            % (dimensione, passo)))
            continue
        trovate, scartati = leggi_specie(dati, nome, passo, quoziente, CAMPI[nome])
        antichi.append({"file": nome, "byte": dimensione, "voci": quoziente,
                        "esemplari": len(trovate), "non_esemplari": scartati,
                        "specie": sorted({v["specie"] for v in trovate}),
                        "voci_dettaglio": trovate})
    return righe, antichi, difetti


def stampa(righe, antichi, difetti):
    print("Voci della base dei doni segreti, per famiglia di titoli")
    print("")
    print("  %-4s %-40s %6s %6s %7s %6s %s"
          % ("gen", "titoli", "voci", "esempl", "specie", "forme", "scad"))
    for r in righe:
        if r["letti"]:
            campi = "%6d %7d %6d" % (r["esemplari"], len(r["specie"]),
                                     len(r["specie_forma"]))
        else:
            campi = "%6s %7s %6s" % ("-", "-", "-")
        print("  %-4d %-40s %6d %s %s"
              % (r["generazione"], r["titoli"][:40], r["voci"], campi,
                 "si" if r["sotto_scadenza"] else "no"))
    print("")
    non_letti = [r for r in righe if not r["letti"]]
    if non_letti:
        print("  I trattini non sono zeri: sono famiglie di cui questo programma non sa ancora")
        print("  leggere i campi, cioe' %s."
              % ", ".join(r["titoli"] for r in non_letti))
    print("")
    scadenza = sum(r["voci"] for r in righe if r["sotto_scadenza"])
    diretto = sum(r["voci"] for r in righe if not r["sotto_scadenza"])
    print("  voci sotto scadenza, cioe' dalla quarta alla settima esclusa Let's Go: %d" % scadenza)
    print("  voci senza scadenza, cioe' ottava, nona e Let's Go:                     %d" % diretto)
    print("  totale:                                                                 %d"
          % (scadenza + diretto))
    print("")

    # Il conto che serve al Pokedex non e' quello delle voci ma quello delle specie distinte, e
    # non si ottiene sommando: le generazioni distribuirono in gran parte le medesime specie,
    # quindi l'unione e' molto piu' piccola della somma. E' precisamente la differenza fra
    # contare e censire.
    sotto = set()
    senza = set()
    for r in righe:
        if r["letti"]:
            (sotto if r["sotto_scadenza"] else senza).update(r["specie"])
    print("  specie distinte nei doni sotto scadenza:  %d" % len(sotto))
    print("  specie distinte nei doni senza scadenza:  %d" % len(senza))
    print("  unione:                                   %d" % len(sotto | senza))
    print("  somma dei conti per generazione:          %d  (non significa nulla, ed e' qui per"
          % sum(len(r["specie"]) for r in righe if r["letti"]))
    print("                                                mostrare quanto la sovrapposizione")
    print("                                                pesi: le generazioni distribuirono")
    print("                                                in gran parte le medesime specie)")
    print("")

    if antichi:
        print("  Prima e seconda generazione, lette il 2026-09-03:")
        for a in antichi:
            print("    %-14s %5d byte  %4d voci  %4d esemplari  %3d specie distinte"
                  % (a["file"], a["byte"], a["voci"], a["esemplari"], len(a["specie"])))
        antiche = set()
        for a in antichi:
            antiche.update(a["specie"])
        print("    specie distinte fra le due: %d" % len(antiche))
        print("    Non sono doni segreti, che allora non esistevano, ma tabelle di incontro con i")
        print("    campi in chiaro. Ne segue il fatto che vale per la roadmap piu' di qualunque")
        print("    conteggio: in quelle generazioni non esiste alcun valore di personalita' e")
        print("    nessun generatore pseudocasuale da ricostruire, quindi produrre un esemplare")
        print("    da evento significa scrivere la struttura con i campi dichiarati, che e' cio'")
        print("    che pokebridge sa gia' fare e ha verificato.")
        print("")
    if difetti:
        print("  DIFETTI:")
        for nome, ragione in difetti:
            print("    %s: %s" % (nome, ragione))
        return 1
    return 0


def scrivi_markdown(percorso, righe, antichi):
    r = []
    r.append("# Conteggio dei doni segreti dalla quarta alla nona generazione")
    r.append("")
    r.append("> Documento generato da `tools/conteggio-doni-moderni.py`. Non si modifica a mano. "
             "Conta le voci della base dati dei doni segreti che la fonte porta come file "
             "binari, e dal 2026-09-03 anche le specie che quelle voci portano. Le due grandezze "
             "differiscono di molto, perché la stessa distribuzione compare come voce distinta "
             "per ogni regione e ogni lingua in cui fu fatta, e perché le generazioni "
             "distribuirono in gran parte le medesime specie: il conto delle voci misura il "
             "lavoro di trasferimento, quello delle specie distinte misura il contributo alla "
             "collezione, e i due non si confondono.")
    r.append("")
    r.append("| Gen | Titoli | File | Voci | Esemplari | Specie distinte | Voci specie e forma | Sotto scadenza | Lunghezza del record |")
    r.append("|---|---|---|---|---|---|---|---|---|")
    for x in righe:
        if x["letti"]:
            misure = "%d | %d | %d" % (x["esemplari"], len(x["specie"]),
                                       len(x["specie_forma"]))
        else:
            misure = "non letti | non letti | non letti"
        r.append("| %d | %s | %s | %d | %s | %s | %s |"
                 % (x["generazione"], x["titoli"], ", ".join("`%s`" % f for f in x["files"]),
                    x["voci"], misure,
                    "sì" if x["sotto_scadenza"] else "no", x["provenienza"]))
    r.append("")
    non_letti = [x for x in righe if not x["letti"]]
    if non_letti:
        r.append("Le celle che dicono non letti non sono zeri, e la distinzione è la stessa che "
                 "questo progetto ha già pagato altrove: uno zero non misurato e uno zero "
                 "misurato hanno lo stesso aspetto e significato opposto. Le famiglie di cui non "
                 "si sanno ancora leggere i campi sono %s, e sono tutte senza scadenza, quindi "
                 "la loro assenza non tocca alcun conto sotto scadenza."
                 % ", ".join(x["titoli"] for x in non_letti))
        r.append("")
    sotto, senza = set(), set()
    for x in righe:
        if x["letti"]:
            (sotto if x["sotto_scadenza"] else senza).update(x["specie"])
    r.append("Le specie distinte portate dai doni sotto scadenza sono %d, quelle portate dai doni "
             "senza scadenza %d, e la loro unione %d. La somma dei conti per generazione vale "
             "invece %d, e il confronto fra quella somma e l'unione misura quanto la "
             "sovrapposizione pesi: le generazioni distribuirono in gran parte le medesime "
             "specie, e sommare i conti per generazione produrrebbe un numero privo di "
             "significato. È lo stesso motivo per cui questo progetto ha dovuto passare dal "
             "contare al censire."
             % (len(sotto), len(senza), len(sotto | senza),
                sum(len(x["specie"]) for x in righe if x["letti"])))
    r.append("")
    scadenza = sum(x["voci"] for x in righe if x["sotto_scadenza"])
    diretto = sum(x["voci"] for x in righe if not x["sotto_scadenza"])
    r.append("Le voci sotto scadenza, cioè quelle delle generazioni che per arrivare al deposito "
             "dipendono dalla banca, sono %d. Quelle senza scadenza, cioè l'ottava, la nona e i "
             "due titoli di Let's Go, che parlano al deposito direttamente, sono %d. Il totale è "
             "%d." % (scadenza, diretto, scadenza + diretto))
    r.append("")
    r.append("Il confronto con la terza generazione dice l'ordine di grandezza del problema che "
             "resta: quella generazione ha centosettantasette voci di catalogo e le ha richieste "
             "settimane di studio, perché la sua tabella vive nel codice e il suo generatore "
             "pseudocasuale andava ricostruito. Le quattro generazioni sotto scadenza che la "
             "seguono ne hanno %d, cioè quasi venti volte tanto, e non richiedono alcuna "
             "ricostruzione: la fonte porta ciascun dono come record binario e il lavoro è di "
             "conteggio, catalogazione e misura della campagna. Ne segue che il vincolo su queste "
             "generazioni non è la conoscenza ma il tempo di trasferimento, ed è la ragione per "
             "cui il numero da misurare per primo resta il tasso del primo anello della catena."
             % scadenza)
    r.append("")
    if antichi:
        antiche = set()
        for a in antichi:
            antiche.update(a["specie"])
        r.append("## Prima e seconda generazione")
        r.append("")
        r.append("Nella medesima cartella la fonte tiene le tabelle degli esemplari da evento di "
                 "prima e seconda generazione. Non sono doni segreti, che in quelle generazioni "
                 "non esistevano: sono tabelle di incontro, e fino al 2026-09-02 questo programma "
                 "ne riferiva soltanto l'esistenza e la dimensione. Il 2026-09-03 il loro formato "
                 "è stato letto ed è il più semplice di tutti, cioè record di lunghezza fissa con "
                 "i campi in chiaro, otto byte in prima generazione e dodici in seconda, che "
                 "portano specie, livello, quattro mosse, restrizione di lingua e tipo di "
                 "allenatore.")
        r.append("")
        r.append("| File | Byte | Voci | Esemplari | Specie distinte |")
        r.append("|---|---|---|---|---|")
        for a in antichi:
            r.append("| `%s` | %d | %d | %d | %d |"
                     % (a["file"], a["byte"], a["voci"], a["esemplari"], len(a["specie"])))
        r.append("")
        r.append("Le specie distinte fra le due generazioni sono %d. Ne discende il fatto che per "
                 "la roadmap vale più di qualunque conteggio: in quelle generazioni non esiste "
                 "alcun valore di personalità e non esiste alcun generatore pseudocasuale da "
                 "ricostruire, perché natura, sesso e caratteristiche non derivano da un seme. "
                 "Produrre un esemplare da evento di prima o seconda generazione significa "
                 "dunque scrivere la struttura con i campi che la tabella dichiara, che è "
                 "esattamente ciò che `pokebridge` sa già fare e ha verificato su prove proprie. "
                 "Fra le sei generazioni con eventi sotto scadenza, queste due sono le meno "
                 "costose e non le più costose, contro ogni intuizione." % len(antiche))
        r.append("")
    io.open(percorso, "w", encoding="utf-8", newline="").write("\n".join(r) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--pkhex", required=True, help="clone di PKHeX")
    p.add_argument("--markdown", help="scrive il conteggio come documento tracciato")
    a = p.parse_args()
    righe, antichi, difetti = conta(a.pkhex)
    esito = stampa(righe, antichi, difetti)
    if a.markdown and not difetti:
        scrivi_markdown(a.markdown, righe, antichi)
        print("  scritto " + a.markdown)
    return esito


if __name__ == "__main__":
    sys.exit(main())
