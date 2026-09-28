#!/usr/bin/env python3
"""Compone il Rubino di prova con il complemento di ADR-080 e ADR-087, in un file NUOVO.

Perché esiste
--------------

Il complemento, 376 esemplari generati con la libreria di PKHeX e giudicati legali, sta in
`_notes/lotti/lotto-complemento-rubino/esemplari/`, e la sua disposizione nelle scatole è quella di
`disposizione_rubino` in `emerald_mappa_box.py`, che è anche la disposizione mostrata dalla mappa e dalla
copia da stampare. Questo strumento la usa invece di ricalcolarla, così la mappa e la scrittura non
possono divergere, e prende da lì anche gli sfondi, con `sfondi_rubino`.

Che cosa garantisce
-------------------

Il file d'ingresso non si tocca e l'uscita non sovrascrive niente. Lo slot attivo dell'ingresso deve
essere integro e il deposito vuoto: la partita del Rubino è all'inizio, e una posizione occupata vorrebbe
dire che l'ipotesi su cui poggia la disposizione è falsa. Ogni file del complemento deve avere il checksum
interno giusto, e la verifica finale si fa sui byte prodotti: slot attivo integro, posizioni uguali a
quelle previste, ogni record leggibile e simmetrico, personalità tutte distinte, dati fuori dal deposito
(squadra, zaino, allenatore, eventi) identici all'ingresso, slot inattivo identico, sfondi scritti, nomi
dei box invariati. Se una sola verifica cade, il file non viene scritto.

Uso
---

    python gba-save-extraction-smeraldo/tools/rubino_complemento.py INGRESSO.sav USCITA-CORRETTO.sav
"""

import argparse
import collections
import hashlib
import importlib.util
import sys
from pathlib import Path

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
sys.path.insert(0, str(RADICE.joinpath("pokemon-gen12-gen3-bridge-original-hardware")))

from pokebridge import gen3, save3  # noqa: E402

PER_BOX = 30
VUOTO = bytes(save3.RECORD)


def _mappa():
    percorso = Path(__file__).resolve().parent.joinpath("emerald_mappa_box.py")
    spec = importlib.util.spec_from_file_location("emerald_mappa_box", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def squadra(save):
    """Specie e livello della squadra, per il rapporto: si legge, non si scrive."""
    fuori = []
    for i in range(save.conteggio_squadra()):
        mon = gen3.Gen3Mon.from_bytes(save.leggi_squadra(i)[:save3.RECORD])
        fuori.append((mon.growth.species, mon.nickname))
    return fuori


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("ingresso")
    p.add_argument("uscita")
    p.add_argument("--togli-copie-di", metavar="SALVATAGGIO",
                   help="toglie dal deposito gli esemplari che sono copie byte per byte di un esemplare di questo "
                        "salvataggio; rifiuta se anche una sola posizione occupata non lo è")
    args = p.parse_args()
    ingresso, uscita = Path(args.ingresso), Path(args.uscita)
    if uscita.exists() or uscita.resolve() == ingresso.resolve():
        sys.exit("l'uscita esiste già o coincide con l'ingresso: questo strumento non sovrascrive")

    mappa = _mappa()
    grezzo = ingresso.read_bytes()
    vecchio = save3.Save3(grezzo)
    if not vecchio.integro():
        sys.exit("lo slot attivo dell'ingresso non è integro")
    occupate = [i for i in range(save3.POSIZIONI) if vecchio.leggi_posizione(i) != VUOTO]
    # Il 2026-09-28 il Rubino aveva nei box 1-7 il carico di prova del 2026-09-15, 205 esemplari tutti copie
    # byte per byte di esemplari che la cartuccia completa di Smeraldo porta dal 2026-09-23: tenerli avrebbe
    # messo lo stesso esemplare su due cartucce. Si tolgono soltanto se la copia è dimostrata posizione per
    # posizione, così che niente di unico possa sparire.
    if occupate and args.togli_copie_di:
        altro = save3.Save3(Path(args.togli_copie_di).read_bytes())
        if not altro.integro():
            sys.exit("lo slot attivo di %s non è integro" % args.togli_copie_di)
        noti = {altro.leggi_posizione(i) for i in range(save3.POSIZIONI)} - {VUOTO}
        uniche = [i for i in occupate if vecchio.leggi_posizione(i) not in noti]
        if uniche:
            sys.exit("%d posizioni occupate non sono copie di %s, la prima è la %d: non si tolgono"
                     % (len(uniche), Path(args.togli_copie_di).name, uniche[0]))
        print("tolte %d copie byte per byte di esemplari di %s" % (len(occupate), Path(args.togli_copie_di).name))
    elif occupate:
        sys.exit("il deposito dell'ingresso non è vuoto: %d posizioni occupate, la prima è la %d" % (len(occupate), occupate[0]))

    voci = mappa.disposizione_rubino()
    previsto = [VUOTO] * save3.POSIZIONI
    if len(voci) > save3.POSIZIONI:
        sys.exit("il complemento ha %d voci e il deposito %d posizioni" % (len(voci), save3.POSIZIONI))
    for i, v in enumerate(voci):
        record = save3.record_da_file(mappa.RUBINO.joinpath(v["file"]).read_bytes())
        mon = gen3.Gen3Mon.from_bytes(record)
        if mon.to_bytes() != record:
            sys.exit("il file %s non è simmetrico: checksum o cifratura non tornano" % v["file"])
        previsto[i] = record
    per_box = [voci[b * PER_BOX:(b + 1) * PER_BOX] for b in range(-(-len(voci) // PER_BOX))]
    sfondi = list(vecchio.storage()[save3.OFF_SFONDI:save3.OFF_SFONDI + 14])
    for b, s in enumerate(mappa.sfondi_rubino(per_box)):
        sfondi[b] = s

    nuovo = save3.Save3(grezzo)
    for i, r in enumerate(previsto):
        nuovo.scrivi_posizione(i, r)
    nuovo._scrivi_in_buffer(save3.SEZIONI_STORAGE, save3.OFF_SFONDI, bytes(sfondi))
    prodotto = nuovo.to_bytes()

    riletto = save3.Save3(prodotto)
    errori = []
    if not riletto.integro():
        errori.append("slot attivo non integro")
    letti = [riletto.leggi_posizione(i) for i in range(save3.POSIZIONI)]
    if letti != previsto:
        errori.append("le posizioni non sono quelle previste")
    for i, r in enumerate(letti):
        if r != VUOTO:
            try:
                if gen3.Gen3Mon.from_bytes(r).to_bytes() != r:
                    errori.append("posizione %d non simmetrica" % i)
            except Exception as e:
                errori.append("posizione %d illeggibile: %s" % (i, e))
    pid = collections.Counter(int.from_bytes(r[:4], "little") for r in letti if r != VUOTO)
    doppie = [k for k, n in pid.items() if n > 1]
    if doppie:
        errori.append("%d personalità condivise, per esempio %08X" % (len(doppie), doppie[0]))
    if riletto.small() != vecchio.small() or riletto.large() != vecchio.large():
        errori.append("i dati fuori dal deposito sono cambiati")
    base = (1 - vecchio.attivo) * save3.SLOT
    if prodotto[base:base + save3.SLOT] != grezzo[base:base + save3.SLOT]:
        errori.append("lo slot inattivo è cambiato")
    st = riletto.storage()
    if list(st[save3.OFF_SFONDI:save3.OFF_SFONDI + 14]) != sfondi:
        errori.append("sfondi non scritti")
    if st[save3.OFF_NOMI_BOX:save3.OFF_SFONDI] != vecchio.storage()[save3.OFF_NOMI_BOX:save3.OFF_SFONDI]:
        errori.append("nomi dei box cambiati")
    if errori:
        for e in errori:
            print("VERIFICA FALLITA: %s" % e)
        sys.exit("il file non è stato scritto")

    uscita.write_bytes(prodotto)
    print("squadra, invariata: %s" % ", ".join("specie %d" % s for s, _ in squadra(riletto)))
    for k, n in collections.Counter(v["provenienza"] for v in voci).items():
        print("  %-14s %d" % (k, n))
    print("%d esemplari in %d box, personalità tutte distinte" % (len(voci), len(per_box)))
    print("sfondi: " + ", ".join("BOX %d %s" % (b + 1, mappa.NOMI_SFONDI_RUBINO[s]) for b, s in enumerate(sfondi[:len(per_box)])))
    print("scritto %s" % uscita)
    print("SHA-256 %s" % hashlib.sha256(prodotto).hexdigest())


if __name__ == "__main__":
    main()
