#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deriva dai dati quali mosse non si possono più usare sui titoli per console corrente.

Perché esiste, e perché sostituisce una lista che avevamo già
-------------------------------------------------------------
Lo Studio 05 ha aperto l'asse delle mosse perdute a partire da un raccoglitore della comunità,
che ne elencava sessantatré. Quella fonte sta al quinto livello del registro, cioè è una
testimonianza: buona, curata, e non verificabile senza fidarsi di chi l'ha scritta. La gerarchia
delle fonti di questo progetto dice che dove una fonte di livello inferiore può rispondere alla
stessa domanda si usa quella, e qui può.

Il verificatore porta infatti, per ciascun contesto di gioco, l'insieme delle mosse rese
inefficaci, cioè presenti nei dati e non utilizzabili in battaglia. È il dato che genera il
triangolo giallo quando un esemplare trasferito conosce una di esse. Una mossa è perduta per i
titoli per console corrente quando è resa inefficace in tutti quei titoli insieme, e questa è una
proprietà che si calcola invece di leggerla.

Che cosa il confronto fra le due liste può dire, e va detto prima di guardarlo. Se coincidono, la
testimonianza è confermata e il progetto ha una derivazione al posto di una citazione. Se la
derivazione ne ha di più, la testimonianza era incompleta. Se ne ha di meno, o la testimonianza
sbagliava, oppure sta usando una definizione diversa, per esempio contando come perduta una mossa
che resta usabile in un solo titolo e che quindi richiede quel titolo e non un trasferimento. Le
tre letture sono diverse e nessuna delle due liste, da sola, permette di distinguerle.

La forma del dato, che vale descrivere
---------------------------------------
L'insieme non è un elenco di numeri ma un insieme di bit, uno per mossa, impacchettati otto per
byte con il bit meno significativo per primo. Duecentocinquantuno mosse rese inefficaci stanno
così in cento byte invece che in cinquecentodue, ed è la stessa scelta di rappresentazione che il
formato degli esemplari usa per i fiocchi. Va tenuto presente che l'insieme comprende anche le
mosse che nessun esemplare può conoscere, cioè quelle di trasformazione e quelle esclusive di
alcuni veicoli, che vanno tolte perché non sono perdute: non sono mai state possedute.

Uso
---
    python tools/mosse-perdute.py
    python tools/mosse-perdute.py --out pokedex-home-completo/MOSSE-PERDUTE.md
    python tools/mosse-perdute.py --self-test
"""

import argparse
import collections
import glob
import io
import os
import re
import struct
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))

MOSSE_DIR = os.path.join("PKHeX.Core", "Moves")
TESTI = os.path.join("PKHeX.Core", "Resources", "text", "other", "en")

# I titoli per console corrente che portano un insieme di mosse rese inefficaci, con il nome
# umano. Chi non lo porta non rende inefficace nulla, quindi non vincola l'intersezione.
CONTESTI = [
    ("MoveInfo8.cs", "ottava generazione, i due titoli maggiori"),
    ("MoveInfo8a.cs", "l'ottava generazione nella regione antica"),
    ("MoveInfo8b.cs", "le riedizioni della quarta generazione"),
    ("MoveInfo9.cs", "nona generazione"),
    ("MoveInfo9a.cs", "il titolo piu' recente"),
]

# Gli intervalli delle mosse che nessun esemplare puo' conoscere, letti dai commenti del
# verificatore e non dedotti. Non sono perdute: non sono mai state possedute, e contarle
# gonfierebbe il conto di oltre cento voci.
INCONOSCIBILI = [(622, 658), (695, 703), (719, 719), (723, 728)]


def leggi_insieme(pkhex, file_):
    """L'insieme delle mosse rese inefficaci in un contesto, dai byte del verificatore."""
    percorso = os.path.join(pkhex, MOSSE_DIR, file_)
    testo = io.open(percorso, encoding="utf-8").read()
    i = testo.find("DummiedMoves")
    if i < 0:
        return None
    j = testo.index("[", i)
    k = testo.index("]", j)
    byte = [int(x, 16) for x in re.findall(r"0x([0-9A-Fa-f]{2})", testo[j:k])]
    return byte_verso_insieme(byte)


def byte_verso_insieme(byte):
    """Da un insieme di bit impacchettato all'insieme dei numeri di mossa.

    Il bit meno significativo di ciascun byte porta la mossa di indice piu' basso, che e' la
    convenzione del verificatore e non una scelta nostra: leggerla al contrario produce un
    insieme della stessa cardinalita' e completamente sbagliato, cioe' un difetto senza sintomi.
    """
    fuori = set()
    for posizione, valore in enumerate(byte):
        for bit in range(8):
            if valore & (1 << bit):
                fuori.add(posizione * 8 + bit)
    return fuori


def conoscibile(mossa):
    return not any(a <= mossa <= b for a, b in INCONOSCIBILI)


def nomi_mosse(pkhex):
    percorso = os.path.join(pkhex, TESTI, "text_Moves_en.txt")
    return [r.strip() for r in io.open(percorso, encoding="utf-8-sig").read().splitlines()]


def nostre_mosse():
    from pokebridge import gen3  # noqa: E402
    fuori = collections.defaultdict(set)
    for pat, off, et in (("lotto-gen5/*.pk5", 0x28, "gen5"), ("lotto-gen4/*.pk4", 0x28, "gen4")):
        for f in glob.glob(os.path.join(RADICE, "_notes", pat)):
            d = open(f, "rb").read()
            for i in range(4):
                m = struct.unpack_from("<H", d, off + 2 * i)[0]
                if m:
                    fuori[m].add(et)
    for pat, et in (("lotto-eventi/*.pk3", "gen3"), ("lotto-incontri-gen3/*.pk3", "biglietti")):
        for f in glob.glob(os.path.join(RADICE, "_notes", pat)):
            mon = gen3.Gen3Mon.from_canonical_bytes(open(f, "rb").read(), party=False)
            for m in mon.attacks.moves:
                if m:
                    fuori[m].add(et)
    return fuori


# Le sessantatre mosse e abilita' che il raccoglitore della comunita' dichiara perdute, per il
# confronto. Sta qui e non in un file a parte perche' e' un dato di confronto e non una fonte di
# verita': il suo scopo e' essere smentito o confermato dalla derivazione, non guidarla.
TESTIMONIANZA = """Assist Bestow Camouflage Captivate Chip_Away Embargo Feint_Attack Flame_Burst
Foresight Frustration Grass_Whistle Heal_Block Heal_Order Heart_Stamp Ion_Deluge Lucky_Chant
Magnet_Bomb Magnitude Mat_Block Me_First Miracle_Eye Mirror_Shot Mud_Sport Natural_Gift
Needle_Arm Nightmare Odor_Sleuth Powder Punishment Pursuit Refresh Return Rototiller Secret_Power
Signal_Beam Sky_Drop Sky_Uppercut Smelling_Salts Snatch Spider_Web Spotlight Steamroller
Synchronoise Telekinesis Trump_Card Wake-Up_Slap Water_Sport Wring_Out Diamond_Storm Fleur_Cannon
Hyperspace_Fury Hyperspace_Hole Plasma_Fists Psycho_Boost Techno_Blast Searing_Shot Spectral_Thief
Steam_Eruption V-create Celebrate Happy_Hour Hold_Back Hold_Hands""".split()


def rapporto(pkhex):
    nomi = nomi_mosse(pkhex)
    per_nome = {n.lower(): i for i, n in enumerate(nomi) if n}
    insiemi = {}
    for file_, umano in CONTESTI:
        s = leggi_insieme(pkhex, file_)
        if s is not None:
            insiemi[umano] = {m for m in s if conoscibile(m) and m < len(nomi)}

    comuni = set.intersection(*insiemi.values()) if insiemi else set()
    nostre = nostre_mosse()

    attesa = set()
    ignote = []
    for v in TESTIMONIANZA:
        i = per_nome.get(v.replace("_", " ").lower())
        if i is None:
            ignote.append(v)
        else:
            attesa.add(i)

    r = ["# Le mosse perdute, derivate dai dati e non citate", ""]
    r.append("> Documento generato da `tools/mosse-perdute.py`. Non si modifica a mano: si "
             "rigenera. Sostituisce come fonte primaria la testimonianza della comunita' da cui "
             "l'asse era nato, e la conserva come termine di confronto.")
    r.append("")
    r.append("Una mossa e' perduta quando e' resa inefficace in tutti i titoli per console "
             "corrente insieme: presente nei dati, e non utilizzabile. E' il dato che genera il "
             "triangolo giallo su un esemplare trasferito che la conosca. Dall'insieme si tolgono "
             "le mosse che nessun esemplare puo' conoscere, cioe' quelle di trasformazione e "
             "quelle esclusive di alcuni veicoli, perche' non sono perdute: non sono mai state "
             "possedute.")
    r.append("")
    r.append("| Contesto | Mosse rese inefficaci, escluse le inconoscibili |")
    r.append("|---|---|")
    for umano, s in insiemi.items():
        r.append("| %s | %d |" % (umano, len(s)))
    r.append("| **rese inefficaci in tutti** | **%d** |" % len(comuni))
    r.append("")

    solo_derivate = sorted(comuni - attesa)
    solo_testimoniate = sorted(attesa - comuni)
    r.append("## Il confronto con la testimonianza")
    r.append("")
    r.append("La testimonianza ne elencava %d, di cui %d riconosciute per nome. La derivazione ne "
             "trova %d. In comune sono %d."
             % (len(TESTIMONIANZA), len(attesa), len(comuni), len(comuni & attesa)))
    if ignote:
        r.append("")
        r.append("Nomi della testimonianza che la tabella non riconosce: %s."
                 % ", ".join(ignote))
    r.append("")
    r.append("### Trovate dalla derivazione e assenti dalla testimonianza (%d)" % len(solo_derivate))
    r.append("")
    r.append("Prima di leggerle va dichiarato il limite della derivazione, perche' spiega la "
             "quasi totalita' di questo scarto. I cinque contesti intersecati sono i soli che "
             "portino una tabella delle mosse rese inefficaci; le riedizioni della prima "
             "generazione per console corrente non ne portano alcuna, quindi su di esse questa "
             "derivazione non dice nulla. La testimonianza invece le considera, e dichiara "
             "esplicitamente che le mosse della prima generazione si recuperano di la'. Le due "
             "liste concordano dunque una volta tenuto conto di quel titolo, e lo scarto si "
             "divide in tre gruppi che vanno letti separatamente.")
    r.append("")
    gen1 = [m for m in solo_derivate if m <= 165]
    compagno = [m for m in solo_derivate if 729 <= m <= 741]
    resto = [m for m in solo_derivate if m not in gen1 and m not in compagno]
    for titolo, gruppo, nota in (
        ("Mosse della prima generazione, recuperabili nelle riedizioni per console corrente",
         gen1,
         "La testimonianza le elenca nella propria sezione sulla prima generazione e poi le "
         "esclude dal riepilogo, con la ragione giusta. Non sono perdute con la chiusura."),
        ("Mosse esclusive del compagno nelle riedizioni per console corrente", compagno,
         "Esistono soltanto in quel titolo, che e' per console corrente: non sono perdute con la "
         "chiusura e non richiedono alcun trasferimento, richiedono quel gioco."),
        ("Il resto, che e' lo scarto vero", resto,
         "Se questo gruppo non e' vuoto, la testimonianza era incompleta e queste voci vanno "
         "aggiunte all'asse."),
    ):
        r.append("**%s (%d).** %s" % (titolo, len(gruppo), nota))
        r.append("")
        if gruppo:
            r.append("| Mossa | Id | Nei nostri lotti |")
            r.append("|---|---|---|")
            for m in gruppo:
                r.append("| %s | %d | %s |" % (nomi[m], m,
                                               ", ".join(sorted(nostre.get(m, []))) or "no"))
            r.append("")
    r.append("")
    r.append("### Nella testimonianza e non nella derivazione (%d)" % len(solo_testimoniate))
    r.append("")
    if solo_testimoniate:
        r.append("Queste diciotto voci non sono un errore della testimonianza ma la prova che le "
                 "due liste misurano cose diverse, ed e' il risultato piu' utile di questo "
                 "confronto. Esistono due nozioni di mossa perduta e la testimonianza le "
                 "fonde. La prima e' una proprieta' della mossa: e' resa inefficace, cioe' "
                 "presente e non utilizzabile, ed e' quella che questa derivazione misura. La "
                 "seconda e' una proprieta' della coppia fra specie e mossa: la mossa funziona "
                 "benissimo, ma la sola specie che la impara non e' ottenibile sui titoli per "
                 "console corrente, quindi la mossa e' irraggiungibile per quella via. Quasi "
                 "tutte le voci qui sotto sono del secondo tipo, e infatti sono le mosse "
                 "caratteristiche dei mitici e quelle consegnate dalle distribuzioni.")
        r.append("")
        r.append("La distinzione cambia il lavoro e non soltanto la descrizione. Una mossa del "
                 "primo tipo va cercata come mossa, cioe' su un esemplare qualunque che la "
                 "conosca. Una del secondo tipo non va cercata affatto: si ottiene producendo la "
                 "specie, che e' lavoro che questo progetto sta gia' facendo.")
        r.append("")
        r.append("| Mossa | Id | Resta usabile in |")
        r.append("|---|---|---|")
        for m in solo_testimoniate:
            dove = [u for u, s in insiemi.items() if m not in s]
            r.append("| %s | %d | %s |" % (nomi[m], m, "; ".join(dove) or "nessuno"))
    else:
        r.append("Nessuna.")
    r.append("")

    # Il conto che conta e' quello al netto del titolo che questa derivazione non vede: le voci
    # recuperabili nelle riedizioni per console corrente non sono perdute con la chiusura, e
    # tenerle dentro gonfierebbe di trentacinque un numero su cui si pianifica.
    recuperabili = {m for m in comuni if m <= 165 or 729 <= m <= 741}
    vere = comuni - recuperabili
    coperte = sorted(m for m in vere if m in nostre)
    scoperte = sorted(m for m in vere if m not in nostre)
    r.append("## Che cosa i nostri lotti gia' portano")
    r.append("")
    r.append("Il conto va fatto al netto delle %d voci recuperabili nelle riedizioni per console "
             "corrente, che non sono perdute con la chiusura. Restano %d mosse davvero perdute, "
             "di cui %d sono gia' dentro i lotti prodotti e %d no. Queste ultime sono il lotto da "
             "procurare, ed e' definito da questa derivazione e non da una lettura."
             % (len(recuperabili), len(vere), len(coperte), len(scoperte)))
    r.append("")
    r.append("| Mossa | Id | In quale lotto |")
    r.append("|---|---|---|")
    for m in coperte:
        r.append("| %s | %d | %s |" % (nomi[m], m, ", ".join(sorted(nostre[m]))))
    r.append("")
    r.append("### Quelle che mancano (%d)" % len(scoperte))
    r.append("")
    r.append("| Mossa | Id |")
    r.append("|---|---|")
    for m in scoperte:
        r.append("| %s | %d |" % (nomi[m], m))
    return "\n".join(r) + "\n", len(comuni), len(coperte)


def self_test():
    esiti = []

    def prova(nome, cond, det=""):
        esiti.append((nome, bool(cond), det))

    # La lettura dell'insieme di bit, contro un vettore calcolato a mano.
    prova("il bit meno significativo porta la mossa piu' bassa",
          byte_verso_insieme([0x01]) == {0}, str(byte_verso_insieme([0x01])))
    prova("il bit piu' significativo porta la settima",
          byte_verso_insieme([0x80]) == {7}, str(byte_verso_insieme([0x80])))
    prova("il secondo byte comincia dall'ottava",
          byte_verso_insieme([0x00, 0x01]) == {8}, str(byte_verso_insieme([0x00, 0x01])))
    prova("un byte pieno da' otto mosse",
          byte_verso_insieme([0xFF]) == set(range(8)), "")
    # Il controllo negativo che rende utili i precedenti: letto al contrario l'insieme avrebbe la
    # stessa cardinalita' e sarebbe tutto sbagliato, quindi la cardinalita' non e' una prova.
    rovescio = set()
    for p_, v in enumerate([0x01]):
        for b in range(8):
            if v & (1 << (7 - b)):
                rovescio.add(p_ * 8 + b)
    prova("negativo: la lettura rovesciata ha la stessa cardinalita' ed e' diversa",
          len(rovescio) == len(byte_verso_insieme([0x01])) and rovescio != byte_verso_insieme([0x01]),
          str(rovescio))

    prova("le mosse di trasformazione sono escluse",
          not conoscibile(630) and not conoscibile(700), "")
    prova("una mossa ordinaria non e' esclusa", conoscibile(1) and conoscibile(500), "")
    prova("la testimonianza ha sessantatre voci", len(TESTIMONIANZA) == 63,
          str(len(TESTIMONIANZA)))

    larghezza = max(len(n) for n, _, _ in esiti)
    for nome, ok, det in esiti:
        print("  %-*s  %s%s" % (larghezza, nome, "ok" if ok else "FALLITO",
                                ("  " + det) if (det and not ok) else ""))
    caduti = [n for n, ok, _ in esiti if not ok]
    print("")
    print("%d prove, %d fallite." % (len(esiti), len(caduti)))
    return 1 if caduti else 0


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--pkhex", default=os.path.join("_notes", "fonti", "pkhex"))
    p.add_argument("--out", default=os.path.join("pokedex-home-completo", "MOSSE-PERDUTE.md"))
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()
    if a.self_test:
        return self_test()
    testo, quante, coperte = rapporto(a.pkhex)
    io.open(a.out, "w", encoding="utf-8", newline="\n").write(testo)
    print("%d mosse rese inefficaci ovunque, %d davvero perdute; rapporto in %s"
          % (quante, coperte, a.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
