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

Questo programma fa il primo dei tre passi, cioè il conteggio, e lo fa in modo che il numero non
sia trascritto. La ragione per cui il conteggio merita un programma invece di una divisione fatta
a mano è che la divisione a mano sbaglia: quattro dei dodici file sono serie piatte di record di
lunghezza fissa e si dividono, ma tre non lo sono, e su uno di essi la divisione ingenua dà
settecentododici voci contro le settecentonove vere.

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
        diretto = all(n in DIRETTI for n in files)
        righe.append({"generazione": generazione, "titoli": titoli, "files": files,
                      "voci": voci, "byte": byte, "provenienza": provenienza,
                      "sotto_scadenza": generazione in SOTTO_SCADENZA and not diretto})
    antichi = []
    for nome in EVENTI_ANTICHI:
        percorso = os.path.join(cartella, nome)
        if os.path.exists(percorso):
            antichi.append((nome, os.path.getsize(percorso)))
    return righe, antichi, difetti


def stampa(righe, antichi, difetti):
    print("Voci della base dei doni segreti, per famiglia di titoli")
    print("")
    print("  %-4s %-44s %8s %10s" % ("gen", "titoli", "voci", "sotto scad"))
    for r in righe:
        print("  %-4d %-44s %8d %10s"
              % (r["generazione"], r["titoli"][:44], r["voci"],
                 "si" if r["sotto_scadenza"] else "no"))
    print("")
    scadenza = sum(r["voci"] for r in righe if r["sotto_scadenza"])
    diretto = sum(r["voci"] for r in righe if not r["sotto_scadenza"])
    print("  voci sotto scadenza, cioe' dalla quarta alla settima esclusa Let's Go: %d" % scadenza)
    print("  voci senza scadenza, cioe' ottava, nona e Let's Go:                     %d" % diretto)
    print("  totale:                                                                 %d"
          % (scadenza + diretto))
    print("")
    if antichi:
        print("  Prima e seconda generazione: %s. Non sono doni segreti, che allora non "
              "esistevano, ma le tabelle degli esemplari da evento di quelle generazioni; il "
              "loro formato non e' una serie di record di lunghezza fissa, quindi qui non si "
              "conta." % ", ".join("%s di %d byte" % (n, b) for n, b in antichi))
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
             "binari, e non le specie: le due grandezze differiscono di molto, perché la stessa "
             "distribuzione compare come voce distinta per ogni regione e ogni lingua in cui fu "
             "fatta. Il censimento delle specie è il passo successivo e non è ancora fatto.")
    r.append("")
    r.append("| Gen | Titoli | File | Voci | Sotto scadenza | Lunghezza del record |")
    r.append("|---|---|---|---|---|---|")
    for x in righe:
        r.append("| %d | %s | %s | %d | %s | %s |"
                 % (x["generazione"], x["titoli"], ", ".join("`%s`" % f for f in x["files"]),
                    x["voci"], "sì" if x["sotto_scadenza"] else "no", x["provenienza"]))
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
        r.append("## Prima e seconda generazione")
        r.append("")
        r.append("Nella medesima cartella la fonte tiene %s. Non sono doni segreti, che in quelle "
                 "generazioni non esistevano: sono le tabelle degli esemplari da evento allora "
                 "distribuiti, e il loro formato non è una serie di record di lunghezza fissa, "
                 "quindi questo programma ne riferisce l'esistenza e la dimensione senza contarle. "
                 "Servono al progetto perché la via da quelle generazioni al deposito esiste e "
                 "passa dalla banca, quindi condivide la scadenza."
                 % ", ".join("`%s`, di %d byte" % (n, b) for n, b in antichi))
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
